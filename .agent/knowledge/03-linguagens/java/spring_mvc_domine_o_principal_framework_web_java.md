---json
{
  "id": "spring_mvc_domine_o_principal_framework_web_java",
  "title": "Spring MVC Domine o principal framework web Java",
  "categoria": "03-linguagens",
  "subcategoria": "java",
  "resumo": "**Arquivo Original:** `Spring MVC Domine o principal framework web Java.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "domine",
    "framework",
    "java",
    "linguagens",
    "mvc",
    "principal",
    "spring",
    "web"
  ],
  "perguntas_tipo": [
    "Como utilizar Spring MVC Domine o principal framework web Java?",
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

# Spring MVC Domine o principal framework web Java

> **Arquivo Original:** `Spring MVC Domine o principal framework web Java.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 2

CasadoCódigo
Agradecimentos
EsseéoprimeirolivroqueescrevopelaCasadoCódigoeasatisfaç ãoé
imensa.Serumdosautoresdaeditoraquedesburocratizouacriaç ãodelivros
nopaíséumaenormehonra.Porcontadissomeuprimeiroagradecimento
vaiparaPauloeAdriano,pormedaremespaçoparaescrever.Ecomojáéde
praxenaminhavida,voudeixaraquioagradecimentoparaLarissa,minha
esposa,poraguentaraausêncianecessáriaparaescreverumlivro.
Porúltimoqueroagradeceravocê,quetemsededeconhecimentoequer
estarsempreaprendendo.Sãodepessoasassimqueomundoprecisaeeues-
pero,sinceramente,quecadagotadesuordirecionadoparaseuaprendizado
setransformeemumpassoamaisdadonasuacarreira.
i

## Página 4

CasadoCódigo Sumário
Sumário
1 Introdu ção 1
1.1 PorqueoSpringMVC . . . . . . . . . . . . . . . . . . . . . . 2
1.2 Amargemdaespecificação. . . . . . . . . . . . . . . . . . . . 3
1.3 Comeceaaventura . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.4 Público-alvo . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
1.5 Código-fonte . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
1.6 Pedindoajuda . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2 Come çando o projeto 7
2.1 Configuraçãobásicaecriaçãodoprojeto . . . . . . . . . . . . 7
2.2 Acessandooprimeiroendere ço. . . . . . . . . . . . . . . . . 18
2.3 HabilitandooSpringMVC . . . . . . . . . . . . . . . . . . . . 20
2.4 Configurandoapastacomaspáginas . . . . . . . . . . . . . . 23
2.5 Umpoucopordentrodoframework . . . . . . . . . . . . . . 25
2.6 Conclusão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
3 Cadastro de produtos 29
3.1 Formuláriodecadastro . . . . . . . . . . . . . . . . . . . . . . 29
3.2 Lógicadecadastro . . . . . . . . . . . . . . . . . . . . . . . . . 31
3.3 Gravandoosdadosnobancodedados . . . . . . . . . . . . . 33
3.4 ConfigurandoaJPAcomoHibernate . . . . . . . . . . . . . . 36
3.5 Habilitandoocontroletransacional . . . . . . . . . . . . . . . 41
3.6 Conclusão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
iii

## Página 5

Sumário CasadoCódigo
4 Melhorando o cadastro e a listagem 45
4.1 Recebendoumalistadevaloresnoformulário . . . . . . . . . 45
4.2 Disponibilizandoobjetosnaview . . . . . . . . . . . . . . . . 48
4.3 Listandoosprodutos . . . . . . . . . . . . . . . . . . . . . . . 50
4.4 MelhorusodosverbosHTTP . . . . . . . . . . . . . . . . . . 52
4.5 ModularizaçãodasURLsdeacesso . . . . . . . . . . . . . . . 54
4.6 ForwardxRedirect . . . . . . . . . . . . . . . . . . . . . . . . 55
4.7 Parâmetrosextrasnosredirects . . . . . . . . . . . . . . . . . 57
4.8 Conclusão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
5 V alidaç ão e conversão de dados 61
5.1 Validaçãobásica . . . . . . . . . . . . . . . . . . . . . . . . . . 61
5.2 Exibindooserros . . . . . . . . . . . . . . . . . . . . . . . . . 69
5.3 Exibindoasmensagensdeerrodemaneiraamigável . . . . . 73
5.4 Mantendoosvaloresnoformulário . . . . . . . . . . . . . . . 78
5.5 IntegraçãocomaBeanValidation . . . . . . . . . . . . . . . . 80
5.6 Convertendoadata . . . . . . . . . . . . . . . . . . . . . . . . 82
5.7 Conclusão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
6 Upload de arquivos 87
6.1 RecebendooarquivonoController . . . . . . . . . . . . . . . 87
6.2 Salvandoocaminhodoarquivo . . . . . . . . . . . . . . . . . 91
6.3 Configuraçõesnecessárias. . . . . . . . . . . . . . . . . . . . 92
6.4 Gravandoosarquivosforadoservidorweb . . . . . . . . . . 94
6.5 Conclusão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
7 Carrinho de compras 105
7.1 URItemplates . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
7.2 CarrinhodecompraseoescopodeSessão . . . . . . . . . . . 111
7.3 Exibindoositensdocarrinho . . . . . . . . . . . . . . . . . . 116
7.4 Conclusão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
iv

## Página 6

CasadoCódigo Sumário
8 Retornos assíncronos 121
8.1 Executandooperaçõesdemoradasassincronamente . . . . . 127
8.2 DefferedResulteummaiorcontrolesobreaexecuç ãoassín-
crona . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
8.3 Conclusão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133
9 Melhorando performance com Cache 135
9.1 Cacheandooretornodosmétodosdoscontrollers . . . . . . 136
9.2 Equandotiveremnovoslivros? . . . . . . . . . . . . . . . . . 139
9.3 Usandoumprovedordecachemaisavan çado. . . . . . . . . 140
9.4 Conclusão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
10 Respondendo mais de um formato 143
10.1 Expondoosdadosemoutrosformatos . . . . . . . . . . . . . 143
10.2 ContentnegotiationeoutrosViewResolvers . . . . . . . . . . 145
10.3 Curiosidadesobreoobjetoaserserializado . . . . . . . . . . 148
10.4 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148
11 Protegendo a aplicaç ão 151
11.1 ConfigurandooSpringSecurity . . . . . . . . . . . . . . . . . 152
11.2 Garantindoaautenticação . . . . . . . . . . . . . . . . . . . . 154
11.3 Configuraçãodafontedebuscadosusuários . . . . . . . . . 157
11.4 Cross-siterequestforgery . . . . . . . . . . . . . . . . . . . . . 165
11.5 Customizandomaisalgunsdetalhes . . . . . . . . . . . . . . . 168
11.6 Exibindoousuáriologadoeescondendotrechosdapágina . 171
11.7 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 172
12 Organizaç ão do layout em templates 173
12.1 Templates. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 175
12.2 Deixandootemplateaindamaisflexível . . . . . . . . . . . . 178
12.3 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 180
v

## Página 7

Sumário CasadoCódigo
13 Internacionalizaç ão 181
13.1 Isolandoostextosemarquivosdemensagens . . . . . . . . . 182
13.2 Accept-Languageheader . . . . . . . . . . . . . . . . . . . . . 184
13.3 Passandoparâmetrosnasmensagens . . . . . . . . . . . . . . 185
13.4 Deixequeousuáriodefinaalíngua . . . . . . . . . . . . . . . 186
13.5 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189
14 T estes automatizados 191
14.1 TestesdeintegraçãonoDAO . . . . . . . . . . . . . . . . . . . 192
14.2 Utilizeprofilesecontroleseuambiente . . . . . . . . . . . . . 197
14.3 Testesdocontroller . . . . . . . . . . . . . . . . . . . . . . . . 201
14.4 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 206
15 Outras facilidades 209
15.1 ResolvendooproblemageradopeloLazyLoad . . . . . . . . 209
15.2 Liberandoacessoarecursosestáticosdaaplicação . . . . . . 212
15.3 Enviandoe-mail . . . . . . . . . . . . . . . . . . . . . . . . . . 213
15.4 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 216
16 Deploy da aplicaç ão 217
16.1 ConfigurandooMavenparaoHeroku . . . . . . . . . . . . . 217
16.2 QualbancoseráusadonoHeroku . . . . . . . . . . . . . . . . 219
16.3 NovaaplicaçãonoHeroku . . . . . . . . . . . . . . . . . . . . 221
16.4 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 222
17 Hora de praticar 223
17.1 Mantenhacontato . . . . . . . . . . . . . . . . . . . . . . . . . 223
vi

## Página 8

Capítulo1
Introdução
JáexistemdiversosframeworksMVCnomercadoeaprimeiraperguntaque
vocêdevefazeré:existeanecessidadedeaprendermaisum?Emgeral,exis-
temalgumastecnologiasque,quandosãoescolhidasparaseremusadasem
umaaplicação,nãosãofacilmentereversíveis.OframeworkMVCéumade-
las.
Elevaifazerpartedeumaboapartedasuarotinadedesenvolvimento.
Quasesemprequeumanovafuncionalidadeforpedidaparaseuprojeto,além
deimplementararegradenegócioespecífica,vocêteráquecriaralgumacoisa
relativaaessaregranacamadawebdasuaaplicaç ão.Eaí,vocêmaisumavez
estaráinteragindocomoframeworkescolhido.
Atravésdesseprisma,vocêdevesercapazdeanalisarospontospositivos
enegativosdecadaumadassuasop çõesetomaramelhordecisãopossível.

## Página 9

1.1. PorqueoSpringMVC CasadoCódigo
1.1 P or que o Spring MVC
OSpringéumprojetodelongadata,eleganhoumuitanotoriedadenostem-
posemqueaespecificaçãoJavaEEaindaeramuitoburocrática. Tiroupro-
veitodissoetomoudeassaltoomercadodesdemuitotempoatrás,atéosdias
dehoje.
AideiadelesemprefoiserumaalternativaaoJavaEEe,paraatingiresse
objetivo,elescriaramdiversosprojetosaoredordomóduloprincipal,queé
ode injeção de dependências.
Fig.1.1:módulosdoSpring
Esseéumdosprincipaismotivosparaaado çãodoSpringMVC,queé
justamenteomóduloweb. Nahoradaado çãodeumframework,umdos
pontosmaisrelevanteséoqueelelheentregademaneiragratuita,eoSpring
MVCécompletamenteintegradocomtodasasextensõesproduzidasemcima
dopróprioSpring.Essaimagemmostraapenasasprincipaiscaracterísticas
2

## Página 10

CasadoCódigo Capítulo1. Introdução
doframework.Paraconhecertodasasop ções,valeapenaacessarolink http:
//spring.io/projects.
Umoutropontoaltamenterelevanteéoquantodeajudavocêpodeobter
atravésdainternet.Enesseponto,osprojetosrelacionadosaoSpringtambém
sebeneficiambastante.Elestêmumapáginaexclusivacomquestõesdo Stac-
kOverflow,apenascomasperguntasmarcadascomtagsrelativasaoSpring.
Você pode dar um olhada seguindo este: linkhttp://spring.io/questions.
Alémdisso,aZeroTurnaround,empresafamosaporferramentascomooJRe-
bel,fezumlevantamentodosframeworksMVCmaisusadosnomercado,
oSpringMVClideroucom40%. Vocêpodedarumaolhadaneste: link
http://tinyurl.com/nq8n4zx.
Quase zero de configuração em XML
Atualmente,oSpringsuportaqueamaioriadassuasconfiguraçõesseja
feitademaneiraprogramática,ouseja,vocênãoprecisacriarnenhumXML
paraqueseusmóduloscomecemafuncionar.Esseémaisumpontoquefa-
cilitouaindamaissuaado ção. Emalgummomentodotempo,pareceuque
configuraçõesemXMLeramasaídaparadeclararinformaçõespertinentes
aoprojeto,
masopontoé:semprequevocêalteraumadessasconfigurações,
énecessárioqueumanovainstalaçãodoprojetosejagerada.Dadaessacon-
dição,porquevamosdeixardeescrevercódigoemJavaparaescrevercódigo
emXML?Comumaboaseparaç ãodepacotes,conseguimosdeixarnossas
configuraçõesbemmodulareseissoserámostradonodecorrerdolivro.
1.2 A margem da especificação
AsespecificaçõesproduzidaspelacomunidadeJavasãodegrandevaliapara
asempresas,
issoéinegável.TerumaempresacomoaOracleabalizandoas
decisõesqueenvolvemaplataformapassaseguran çaparaostomadoresde
decisãoquequeremusarestalinguagemesuasferramentasnoseuprojeto.
Opontonegativo,assimcomoquasetodasasdecisõesquetomamos,é
quemuitasvezesasespecificaçõesdemoramparasercriadasesomosobriga-
dosarecorreraprojetosdeterceiros,quemuitasvezesnãoestãointegrados
comasespecificaçõesjáexistentes,paraconcluirmosalgumatarefa.Eéjus-
3

## Página 11

1.3. Comeceaaventura CasadoCódigo
tamenteaíqueentraumdiferencialdosprojetosqueusamoSpringcomo
base.
Comoelesnãoprecisamseguirasespecificações,vocêjátemdiversasop-
çõesdeintegraçõesqueaindanãoforamespecificadasoucujasespecificações
aindaestãoimaturas.Algunsexemplos:
• SpringSocialparafazerloginssociais;
• Quartzparaintegraçãocomesteagendadordetarefas;
• SpringDataparaintegraçãocombancosdedadosnãorelacionais;
• SpringSecurityparafornecerautenticaçãoeautorização;
• SpringCacheparaterapossibilidadedecacheardiversaspartesdocó-
digo.
Essassãoextensõesquevocêpodeusarnosseusprojetosquetenhamo
Springcomobase. Usaremosalgunsdelesnodecorrerdolivro. Valesem-
prelembrar,nadaimpedevocêdetirarproveitodomelhordecadaumdos
mundos.Casoseidentifiquemaiscomummódulodaespecificaç ãodoque
comodoSpring,use-osemmedoalgum.Talvezoleitoratentolembreque
jáexistemespecificaçõesparaagendamentoeCache,eéverdade.Elassónão
estãotãomadurasquantoasop çõesOpenSourcequejáexistem.
1.3 C omece a aventura
Duranteolivrovamosconstruirumaaplicaçãomuitoparecidacomaprópria
CasadoCódigo.Desenvolveremosfuncionalidadesquenoslevarãodesdeos
detalhesmaisbásicosdousodoSpringMVCatépartesavan çadascomo:
• customizaçãodecomponentesdevalidaçãoeconversão;
• Cachesderesultados;
• Processamentoassíncrono;
• Testesdeintegração;
4

## Página 12

CasadoCódigo Capítulo1. Introdução
• Detalhesescondidosdoprocessodeinternacionalização.
Fiquejuntocomigoeleiacadacapítulocomcalma;eusemprelhedirei
seéhoradedarumapausaoudejápularparaopróximo.Esperoquevocê
tenhaumagrandejornada!
1.4 P úblico-alvo
Parapessoasquejáconhe çamumpoucosobreaestruturadeumprojetoba-
seadonoDesignPatternMVC.Olivrovaiajudardesdepessoasquenãoco-
nhecemnadadoSpringMVCatéusuáriosquejáutilizamoframeworkna
prática.Quasetodocapítulovaicobrirdetalhesquevãoalémdousonormal
evaideixá-lomaiscríticoemrelaçãoaousodatecnologia.
1.5 C ódigo-fonte
Todoocódigo-fontedolivroestádisponívelnoGithub,bastaacessaroende-
reçohttps://github.com/livrospringmvc.Fiqueàvontadeparanavegarpelos
arquivosdoprojeto.Oscommitsforamdividosdeacordocomoscapítulosdo
livro,justamenteparaquevocêpossaacessarocódigocompatívelaocapítulo
queestejasendolido.
1.6 P edindo ajuda
Parafacilitaratrocadeideiasentreosleitoresfoicriadoumfórumdediscus-
sãoespecíficoparaolivro.Bastaquevocêacesseoendere çohttps://groups.
google.com/forum/?hl=pt-BR#!forum/livro-springmvc.
5

## Página 14

Capítulo2
Começandooprojeto
2.1 C onfiguração básica e criação do projeto
Oobjetivodolivroéconstruirumaaplicaç ãosemelhanteadaprópriaCasa
doCódigo.Porserumsitedee-commerce,aaplicaç ãonosforneceachance
deimplementardiversasfuncionalidadese,alémdisso,éumdomínioque
nãovainoscausarmuitasdúvidas.
Aprimeiracoisaqueprecisamosfazeréjustamentecriareconfiguraro
mínimonecessárioparaternossaaplicação,comoSpringMVC,rodando
corretamente. ComovamosusaroMavenparagerenciarasnossasdepen-
dências,somosobrigadosacriaroprojetoseguindoumaestruturadetermi-
nadaporessaferramenta.Olayoutdaspastas,comodecostume,vaiseguir
oseguinteformato:

## Página 15

2.1. Configuraçãobásicaecriaçãodoprojeto CasadoCódigo
Fig.2.1:Estruturadepastas
Provavelmentevocêjádeveterfeitoestaatividadealgumasvezes,então,
paramudarumpoucoasuarotina,vouutilizarummodoumpoucodife-
rentedecriaroprojeto. UsaremosumprojetodaRedHatchamado Jboss
Forge,quepodeserbaixadonestelink http://forge.jboss.org/download. O
JbossForgefornecevárioscomandosprontosparaacriaçãodeprojetos.Após
baixado,extraiaoarquivoemumapastadesuapreferência.Acesseoterminal
doseucomputadoredigiteoseguintecomando:
$caminhoParaSuaInstalacao/bin/forge
Issoabriráumaaplicaçãonopróprioconsole.
8

## Página 16

CasadoCódigo Capítulo2. Começandooprojeto
Fig.2.2:Consoledoforge
Agorabastaquedigitemosocomandoresponsávelpelacriaç ãodopro-
jeto.
project-new --named casadocodigo
Pronto! IssoésuficienteparavocêcriaroseuprojetobaseadonoMa-
ven. Aestruturadepastasjáestápronta,sóprecisamosrealizarasdevidas
configurações.
Dependências necessárias
Precisamosadicionartodasasdependênciasnecessáriasparaqueseja
possívelcomeçarmosatrabalharnoprojeto. Paraisso,vamosteroarquivo
pom.xmleadicionamosatag <dependencies>,dentrodaqualcolocamos
cadaumadasdependênciasnecessáriasparacomeçaroseuprojetousandoo
SpringMVC.
<dependencies>
<dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-webmvc</artifactId>
<version>4.1.0.RELEASE</version>
</dependency>
<dependency>
<groupId>org.apache.tomcat</groupId>
<artifactId>tomcat-servlet-api</artifactId>
<version>7.0.30</version>
<scope>provided</scope>
9

## Página 17

2.1. Configuraçãobásicaecriaçãodoprojeto CasadoCódigo
</dependency>
<dependency>
<groupId>javax.servlet.jsp</groupId>
<artifactId>jsp-api</artifactId>
<version>2.1</version>
<scope>provided</scope>
</dependency>
<dependency>
<groupId>javax.servlet.jsp.jstl</groupId>
<artifactId>jstl-api</artifactId>
<version>1.2</version>
<exclusions>
<exclusion>
<groupId>javax.servlet</groupId>
<artifactId>servlet-api</artifactId>
</exclusion>
</exclusions>
</dependency>
<dependency>
<groupId>org.glassfish.web</groupId>
<artifactId>jstl-impl</artifactId>
<version>1.2</version>
<exclusions>
<exclusion>
<groupId>javax.servlet</groupId>
<artifactId>servlet-api</artifactId>
</exclusion>
</exclusions>
</dependency>
<!-- Logging -->
<dependency>
<groupId>org.slf4j</groupId>
<artifactId>slf4j-api</artifactId>
<version>1.6.1</version>
</dependency>
<dependency>
<groupId>org.slf4j</groupId>
<artifactId>jcl-over-slf4j</artifactId>
<version>1.6.1</version>
10

## Página 18

CasadoCódigo Capítulo2. Começandooprojeto
<scope>runtime</scope>
</dependency>
<dependency>
<groupId>org.slf4j</groupId>
<artifactId>slf4j-log4j12</artifactId>
<version>1.6.1</version>
<scope>runtime</scope>
</dependency>
<dependency>
<groupId>log4j</groupId>
<artifactId>log4j</artifactId>
<version>1.2.16</version>
<scope>runtime</scope>
</dependency>
</dependencies>
Percebaqueforammuitasdependênciasenemtodasforamnecessari-
amentedeprojetosligadosdiretamenteaoSpringMVC.Nãopercatempo
analisandominuciosamentecadaumadelas. Lembre-sesempre: vocêestá
emumprojetousandoalinguagemJava;setiverpoucadependêncianãotem
graça.
Agoraqueo pom.xmlestáconfiguradocorretamente,chegouahorade
importá-loparaasua idefavorita. Duranteolivro,usaremoso Spring T o-
ols Suite,queébasicamenteumEclipsecomalgunspluginsespecíficospara
projetosbaseadosnoSpring.CasoprefirausaroseuEclipsecomum,nãohá
nenhumproblema.
Vamosimportaroprojetocomoum Maven Project;assim,paracada
nova dependência necessária, basta alterarmos opom.xml e o próprio
Eclipseseencarregarádeatualizaronosso classpath.
11

## Página 19

2.1. Configuraçãobásicaecriaçãodoprojeto CasadoCódigo
Fig.2.3:Tipodeimportaçãodeprojeto
Clicandono next,seráexibidoo wizarddeimportação.Bastaescolher
ocaminhoondeseuprojetofoicriado.
12

## Página 20

CasadoCódigo Capítulo2. Começandooprojeto
Fig.2.4:Teladeimportaçãodoprojetomaven
Pronto,agoratemosnossoprojetoimportado.Oúltimopassoéadicioná-
loaumservidor,paraquepossamosrealizarnossostestesevercomoaapli-
caçãovaiandando.Paraisso,vamosseguirocaminhopadrãodecriaç ãode
servidoresdentrodoEclipse.
13

## Página 21

2.1. Configuraçãobásicaecriaçãodoprojeto CasadoCódigo
Fig.2.5:Adicioneumnovoservidor
Fig.2.6:Escolhadaversão7paracima
14

## Página 22

CasadoCódigo Capítulo2. Começandooprojeto
Fig.2.7:Aponteocaminhodeinstalaç ão
15

## Página 23

2.1. Configuraçãobásicaecriaçãodoprojeto CasadoCódigo
Fig.2.8:Op çãodeadicionarprojeto
16

## Página 24

CasadoCódigo Capítulo2. Começandooprojeto
Fig.2.9:Adicioneoprojetoaoservidor
Parafinalizarmos,vamossubiroservidoreversetudofuncionacorreta-
mente.
17

## Página 25

2.2. Acessandooprimeiroendereço CasadoCódigo
Fig.2.10:Consoleindicandoqueoservidorsubiu
2.2 A cessando o primeiro endereço
Comtudoconfigurado,chegouahoraderealmentecome çarmosaproduzir
algumacoisa!Onossoprimeirodesafioélevaronossousuárioparaahome
daCasadoCódigo.Oendere çoquequeremosqueeledigiteéo /home.Em
umcenáriomaiscomum,aURLquelevaousuárioparaahomeéopróprio
/.Faremosessaalteraçãonofinaldocapítulo.Nestemomento,casoousuá-
riodigite http://localhost:8080/casadocodigo/home,elereceberáumerrodo
servidorindicandoqueesseendere çonãopodeseratendidoporninguém.
Respondendo a URLs
Emgeral,comoSpringMVC,assimcomocomquasequalqueroutro
frameworkMVC,semprequequisermosresponderaumaURL,teremosque
criarumaclasseresponsávelporisso.
package br.com.casadocodigo.loja.controllers;
public class HomeController {
}
Apenasporconven ção,ésugeridoqueonomedaclasseterminecom
osufixo Controller. AgoraprecisamosensinaraoSpringMVCqueessa
classe, efetivamente, é responsável por atender requisições vindas de um
18

## Página 26

CasadoCódigo Capítulo2. Começandooprojeto
cliente, nessecasoonavegador. Paraisso, vamosadicionaraannotation
@Controllernela.
package br.com.casadocodigo.loja.controllers;
@Controller
public class HomeController {
}
Ecomovamosfazeralógicadecarregamentosdeprodutosparaserem
exibidosna home?Nadamaiscomumdoquecriarmosummétodo.
@Controller
public class HomeController {
public void index(){
//aqui ainda vamos carregar os produtos.
}
}
Agoraimagineoseguintecenário.Vocêprovavelmenteterádiversoscon-
trollers,comasmaisvariadasresponsabilidadesemétodos.ComooSpring
MVCvaisaberqualmétododeveserchamadoparacadaumadasURLs?É
paraissoqueserveaannotation @RequestMapping:
@Controller
public class HomeController {
@RequestMapping("/home")
public void index(){
//aqui ainda vamos carregar os produtos.
System.out.println("Carregando os produtos");
}
}
Essaúltimaconfiguraçãoqueacabamosdefazerétambémconhecida
como binding.Fizemosaligaçãoentreumarotaeométodoresponsávelpor
tratá-la.Oproblemaéquemesmoquevocêtenteacessaroendere çoagora,
19

## Página 27

2.3. HabilitandooSpringMVC CasadoCódigo
aindacontinuarárecebendoocódigodeerro404,indicandoqueoservidor
nãoconseguelidarcomessaURL.
2.3 H abilitando oSpring MVC
Pormaisquejátenhamoscriadonossoprimeirocontroller,aindanãofize-
mosnenhumaconfiguraçãoparahabilitarqueoSpringMVCreconhe çaessas
classes. Casovocêpuxepelasuamemória,vailembrarque,paraconseguir
responderaURLs,emprojetoswebseguindoaespecificaç ãodeServlets,é
necessárioternomínimoum Filterouuma Servletconfigurada.Eéjusta-
menteessepassoquevamosrealizarapartirdeagora.
Configuração programática
A Servlet responsável por tratartodas as requisições que chegam
para o Spring MVC é aDispatcherServlet. Precisamos justamente dela
para que tudo comece a funcionar. A maneira tradicional seria fa-
zer essa configuração através do arquivoweb.xml mas, como vocês
podem ver, esse arquivo nem foi criado. Tudo será feito através de
classes Java. A primeira tarefa é criar uma classe que seja filha de
AbstractAnnotationConfigDispatcherServletInitializer.
package br.com.casadocodigo.loja.conf;
//imports omitidos
public class ServletSpringMVC extends
AbstractAnnotationConfigDispatcherServletInitializer {
@Override
protected Class<?>[] getRootConfigClasses() {
return null;
}
@Override
protected Class<?>[] getServletConfigClasses() {
return null;
20

## Página 28

CasadoCódigo Capítulo2. Começandooprojeto
}
@Override
protected String[] getServletMappings() {
return new String[] { "/"};
}
}
Oobjetivodeherdardessaclasseéjustamentenãoterqueficarfazendo
oregistrodo DispatcherServletnamão. Temosalgunsmétodosinte-
ressantes,vamoscome çarpelo getServletMappings. Aquiéondevocê
dizqualéopadrãodeendere çoquevaiserdelegadoparaoServletdoSpring
MVC.Casofôssemosusaro web.xml,essaconfiguraçãoseriaequivalente
ao <url-mapping>.
EcomooSpringMVCvaisaberquaiscontrollersdevemsermapeadose
quaisoutrasclassesdevemsercarregadaspelocontainerdopróprioSpring?
Paraessaquestão,usamosométodo getServletConfigClasses.Nele,
seráretornadaumaoumaisclassesresponsáveisporindicarquaisoutrasclas-
sesdevemserlidasduranteocarregamentodaaplicaç ãoweb.
@Override
protected Class<?>[] getServletConfigClasses() {
return new Class[]{AppWebConfiguration.class};
}
Agoravamoscriaraclasse AppWebConfiguration.
package br.com.casadocodigo.loja.conf;
@EnableWebMvc
@ComponentScan(basePackageClasses={HomeController.class})
public class AppWebConfiguration {
}
Percebaqueéumaclasseumtantoquantoestranha.Temummontede
annotation,masnenhumcódigo. Oobjetivoprincipaldelaéexporparaa
ServletdoSpringMVCquaissãoasclassesquedevemserlidasecarregadas.
21

## Página 29

2.3. HabilitandooSpringMVC CasadoCódigo
Neste exato momento, a principal annotation aqui é a
@ComponentScan. Através dela indicamos quais pacotes devem ser
lidos. Percebaquepassamoscomoparâmetroaclasse HomeController
paraqueoSpringleiaopacotedela.Dessaforma,nãopassamosumaString
eevitamosumpossívelerrodedigitaç ão.
Aannotation EnableWebMvcnãoénecessáriaagora,mascomoelajá
habilitaváriasfuncionalidadesqueserãousadasnanossaaplicaç ãoweb,já
vamosdeixá-laaí.Paravocênãoficarseperguntandoquaisseriamessasfun-
cionalidades,segueumalistacomalgumasdelas:
• ConversãodeobjetosparaXML
• ConversãodeobjetosparaJSON
• Validaçãousandoaespecificação
• SuporteageraçãodeRSS
Umaúltimaobservaçãoimportanteéquedevemosmanteressasclas-
ses em um pacote separado, focado justamente em classes que ser-
vem apenas de configuração. Por isso estamos usando o pacote
br.com.casadocodigo.loja.conf.
Agoraquetemostudoconfigurado,casovocêtenteacessaroendere ço
/home,infelizmentedeveráreceberaseguinteteladeerro.
Fig.2.11:Viewnãofoiencontrada
22

## Página 30

CasadoCódigo Capítulo2. Começandooprojeto
2.4 C onfigurando a pasta com as páginas
Oerroquevimosnase çãoanteriorindicaqueoSpringMVCnãoachouuma
páginaresponsávelpormontaroHTMLrelativoaorequest. Puxandopela
memória,ofluxopadrãodeumaaplicaçãoMVCé:Clientefazrequest,Servlet
principalatendeedelegaparaumcontrollerdaaplicaç ãoe,finalmente,uma
páginaémontadapararesponderarequisição. Pordefault,oSpringMVC
seguejustamenteessasequência.
Comooretornodonossométodoé void,eleprocurouporumapágina
comnomeembrancoeelanãofoiencontrada.Oprimeiropassoparatentar-
moscontornaroerroéretornarumaString,indicandoocaminhodapágina.
@RequestMapping("/")
public String index(){
System.out.println("Carregando os produtos");
return "hello-world.jsp";
}
Casovocêtenteacessaragora,vaireceberoutroerro.
Fig.2.12:ExceptiongeradapelafaltadeumresolvedordeView
O Spring MVC não sabe onde procurar por essa página, precisamos
ensiná-lo! Parafazerisso,precisamosconfigurarumobjetocujaresponsa-
bilidadeéinformarondeaspáginasdevemserencontradas. Esempreque
falamosemconfiguração,pelomenosporenquanto,estamosnosreferindoà
classe AppWebConfiguration.
23

## Página 31

2.4. Configurandoapastacomaspáginas CasadoCódigo
@Bean
public InternalResourceViewResolver
internalResourceViewResolver() {
InternalResourceViewResolver resolver =
new InternalResourceViewResolver();
resolver.setPrefix("/WEB-INF/views/");
resolver.setSuffix(".jsp");
return resolver;
}
Aclasse InternalResourceViewResolver,comopodeserlidono
própriocódigo,guardaasconfiguraçõesdapastabaseedosufixoquedevem
seradicionadosparaqualquercaminhoquesejaretornadopormétodosdos
controllers. Aannotation @BeanindicaparaoSpringqueoretornodesse
métododeveserregistradocomoumobjetogerenciadopelo container.Em
geral,noSpring,essesobjetossãochamadosdeBeans.Paradeixartudocor-
reto,vamosapenasalteraroretornodométodo index,donossoprimeiro
controller.
@Controller
public class HomeController {
@RequestMapping("/")
public String index(){
System.out.println("Carregando os produtos");
return "hello-world";
}
}
Agorabastaquevocêcrieumapáginachamada hello-worlddentro
dapasta WEB-INF/viewsetudofuncionarácorretamente.
Talvezvocêestejaseperguntandoomotivodedeixarapáginadentroda
pastaWEB-INF.Agrandesacadaévocêquasequeobrigarosdesenvolvedores
aescreveremmétodosnocontrollerparacadafuncionalidade.Dessejeito,o
seuprojetoestáseprotegendodeterlógicasjogadasdiretamentedentrodas
páginas.
24

## Página 32

CasadoCódigo Capítulo2. Começandooprojeto
2.5 U m pouco por dentro do framework
Umpontoquemuitasvezesdiferencia“usuários”doframeworkde“enten-
dedores”éjustamenteteroconhecimentodoqueacontecepordentroda
ferramenta. Porexemplo,comooSpringMVCfazcomqueanossaclasse
ServletSpringMVCsejacarregada? Ondeestáocódigodecarregamento
da DispatcherServlet? Essassãoperguntasque,pormaisquenãote-
nhamavercomoseucódigodenegócioemsi,podemserimportantespara
entenderalgumfluxodoframework.
O web.xml é desnecessário
Desdeaversão3daespecificaç ãodeServlets,justamenteparafacilitara
configuraçãodosframeworks,foicriadoumoutrotipodearquivochamado
de web-fragment.xml.Aideiaéqueessearquivopossaserdeixadodentro
dapasta META-INF,no jardabiblioteca.Dessaforma,quandooservidor
webforiniciadoeaaplicaçãoforcarregada,essearquivovaiserlidoeosser-
vletsoufiltrosqueláestiveremserãocriadoseregistradosdentrodoservidor.
Nãoporacaso,o jardoSpringMVCpossuiestearquivo:
<?xml version="1.0" encoding="ISO-8859-1"?>
<web-fragment ....>
<name>spring_web</name>
<distributable/>
</web-fragment>
Analisando, ele é bem simples. Tem um nome e usa a tag
distributable, apenasparadizerqueaaplicaç ãousandoessearquivo
podeserdistribuídaentreváriosservidores.Sóque,umpontointeressanteé:
ondeestáaconfiguraçãodoservletdoSpringMVC?
Um pouco mais a fundo na especificação
Oweb-fragmentéapenasparadizerqueoSpringMVCpodesernoti-
ficadosobreoiníciodaaplicaç ãoweb. Contudo,destamaneiraeleainda
nãoestáfazendonada. Umoutroarquivointeressante,dentrodo jar,é
25

## Página 33

2.5. Umpoucopordentrodoframework CasadoCódigo
o javax.servlet.ServletContainerInitializer.Eletambémfica
dentrodapasta META-INFeoconteúdoéoquesegue:
org.springframework.web.SpringServletContainerInitializer
Essearquivo,especificamentecomestenome,élidopeloservidorwebem
questãoeaclasseconfiguradaécarregada.
@HandlesTypes(WebApplicationInitializer.class)
public class SpringServletContainerInitializer implements
ServletContainerInitializer {
@Override
public void onStartup(Set<Class<?>> webAppInitializerClasses,
ServletContext servletContext)
throws ServletException {
List<WebApplicationInitializer> initializers = new
LinkedList<WebApplicationInitializer>();
if (webAppInitializerClasses != null) {
for (Class<?> waiClass : webAppInitializerClasses) {
if (!waiClass .isInterface() &&
!Modifier.isAbstract(waiClass.getModifiers()) &&
WebApplicationInitializer.class.
isAssignableFrom(waiClass)) {
try {
initializers.add(
(WebApplicationInitializer)
waiClass.newInstance());
}
catch (Throwable ex) {
throw new ServletException("Failed to
instantiate WebApplicationInitializer
class", ex);
}
}
}
26

## Página 34

CasadoCódigo Capítulo2. Começandooprojeto
}
if (initializers.isEmpty()) {
servletContext.log("No Spring
WebApplicationInitializer types detected on
classpath");
return;
}
AnnotationAwareOrderComparator.sort(initializers);
servletContext.log("Spring WebApplicationInitializers
detected on classpath: " + initializers);
for (WebApplicationInitializer initializer :
initializers) {
initializer.onStartup(servletContext);
}
}
}
Aannotation @HandlesTypesrecebecomoargumentoumconjunto
deinterfaces,cujasclassesfilhassãopassadascomoparâmetroparaomé-
todo onStartup. Caso você esteja curioso, verá que a nossa classe
ServletSpringMVCéfilhadainterface WebApplicationInitializer,
justamenteaquefoipassadaparao @HandleTypes!
2.6 C onclusão
Estecapitulofoiumpoucolongoe,paraserbemsincero,atésimples.Opro-
blemaéquefoinecessáriamuitaconfiguraçãoparaumsimples hello world.
Aparteboadessahistóriaéquevocêpassouporumadasetapasmaisdifíceis
noaprendizadodequalquerframework,osetupinicial.Agoratudotendea
sermaisfluido!Porisso,euindicoquevocêcontinuealeitura.Nopróximo
capítulojácomeçaremosaacessarobancodedadosparacadastrarelistaros
produtosdaloja.
27

## Página 36

Capítulo3
Cadastrodeprodutos
Passadaafasedeconfiguração,chegouahoradecome çarmosaimplementar
algumasdasfuncionalidadesdaloja.Umadasfeaturesmaisbásicas,porém
importante,éocadastrodelivros,jáquesemlivrosnãoexistemcompras.
3.1 F ormulário de cadastro
Vamoscomeçaranossaimplementaçãojustamentepelapartemaispróxima
donossousuáriofinal,queéoformuláriodenovoproduto.
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Cadastro de produtos</title>
</head>

## Página 37

3.1. Formuláriodecadastro CasadoCódigo
<body>
<form method="post">
<div>
<label for="title">Titulo</label>
<input type="text" name="title" id="title"/>
</div>
<div>
<label for="description">Descrição</label>
<textarea rows="10" cols="20" name="description"
id="description">
</textarea>
</div>
<div>
<label for="pages">Número de paginas</label>
<input type="text" name="pages" id="pages"/>
</div>
<div>
<input type="submit" value="Enviar">
</div>
</form>
</body>
</html>
Nãotemnadademais,apenasumHTMLnormal.Sóparaconstar,nosso
modelodelivronãoprecisasermuitocomplexo,temapenasumtítulo,des-
criçãoeonúmerototaldepáginas.
Umdetalheimportantequeficoufaltando:paraondevamosenviarasin-
formaçõescadastradas?Aindanãocriamosnadaquetrateessalógica,masjá
podemosimaginarparaqualURLqueremosenviar.Paraisso,vamosalterar
adeclaraçãodatag <form>evamosadicionaroatributo action.
<form method="post" action="/casadocodigo/produtos">
Aquivaleumaobservação. Foiusadoonomedocontextodemaneira
hard coded,enquantoaestratégiamaisusadanomercadoéousodatag
<c:url>,quevemnopacotedetagspadrãoJSTL.Omotivodessaescolhaé
30

## Página 38

CasadoCódigo Capítulo3. Cadastrodeprodutos
simplesmenteodafacilidadedoentendimentodocódigo.Atag,misturada
comasaspasdosatributosdastags html,muitasvezesconfundemmaisque
ajudam,pelomenosdurantealeituradolivro.
Eondevamoscriaressearquivo?Anossaconfiguraç ãoatualdizquede-
vemoscriarnossasviewsdentrodapasta WEB-INF/views.Comoestamos
lidandocomocadastrodeprodutos,vamosmanterumaorganizaç ãoecriar
umaoutrasubpasta,chamada produtos.Ocaminhofinaldoarquivodeve
ser WEB-INF/views/products/form.jsp. Usaremosessatáticapara
criaçãodaspróximaspáginas,duranteodecorrerdolivro.
3.2 L ógica de cadastro
Nesteexatomomento,seonossousuáriotentarcadastrarumproduto,elevai
receberofamosoerrodepáginanãoencontrada.Afinaldecontas,aindanão
criamosocontrollerresponsávelporessafuncionalidade.Vamoscome çara
resolveresteproblemaagora.
br.com.casadocodigo.loja.controllers;
@Controller
public class ProductsController {
@RequestMapping("/produtos")
public String save(){
System.out.println("Cadastrando o produto");
return "products/ok";
}
}
Atéaqui,nadaquejánãotenhamosvisto.Criamosumcontrollereum
método,amboscomasanotaçõesnecessáriasparaoSpringMVCreconhecer
ocontrolleretambémfazero bindingentrearotaeorespectivométodo.E
ondeestáoprodutoqueestamostentandocadastrar?
Recebendo objetos como parâmetros
Aquinãovamosternenhumanovidade. Todoframeworkquesepreze
devepermitirqueoobjetosejamontadoepassadocomoparâmetronomé-
31

## Página 39

3.2. Lógicadecadastro CasadoCódigo
todo.
br.com.casadocodigo.loja.controllers;
@Controller
public class ProductsController {
@RequestMapping("/produtos")
public String save(Product product){
System.out.println("Cadastrando o produto "+product);
return "products/ok";
}
}
Nãotemosaclasse Product,chegouahoradecriá-la:
br.com.casadocodigo.loja.models;
public class Product {
private String title;
private String description;
private int pages ;
//getters e setters
}
Percebaqueosnomesdoscamposdonossoformuláriobatemexatamente
comosnomesdos settersqueserãogeradosparanós.
• title=>setTitle
• description=>setDescription
• pages=>setPages
ÉdessaformaqueoSpringMVCconseguepopularoobjetoemques-
tão. Casovocêqueira,adicioneum toStringnaclasse Product. Dessa
forma,aimpressãovaimostrarexatamenteosvaloresqueforampreenchidos
noformulário.
32

## Página 40

CasadoCódigo Capítulo3. Cadastrodeprodutos
URL para chegar ao formulário
Umpontoqueoleitormaisatentodeveestarseperguntandoé:qualéo
endereçoqueousuáriovaidigitarparachegarnoformulário? ComoaJSP
estádentrodapasta WEB-INF,elanãoestávisívelparaseracessadapelolado
deforadoservidor.
Asoluçãoéjustamentecriarmaisummétodonocontroller,paralevaro
usuárioparaapáginaemquestão.
package br.com.casadocodigo.loja.controllers;
@Controller
public class ProductsController {
//resto do código
@RequestMapping("/produtos/form")
public String form(){
return "products/form";
}
}
Ométodovazio,muitasvezes,éalgoqueincomodaoprogramador.Po-
demosaténosperguntar:porquenãodeixamosaJSPforadapasta WEB-INF
efazemosoacessodireto? Oproblemadessaabordageméqueestásendo
dadaumabrechaparaquealgumalógica,alémdanecessáriaparaavisualiza-
ção,sejacolocadadentrodapágina.Umpoucomaisparaafrente,aindaneste
capítulo,vamosprecisarcarregarostiposdelivrosquepodemservendidos.
Casonãotivessesidocriadoessemétodo,ondeessecódigoseriacolocado?
Podemosdizerqueesseéummalqueveioparanossobem.
3.3 G rav ando os dados no banco de dados
Pormaisquenossoformuláriojáestejaumtantoquantofuncional,aindanão
estamosefetivamentegravandoasinformaçõespassadas.Paramelhoraressa
parte,vamoscome çaraefetuarasalteraçõesnecessáriasapartirdonosso
controller.
Aprimeiracoisaécome çarausarum DAOresponsávelpeloacessoaos
dadosreferenteàclasse Product.
33

## Página 41

3.3. Gravandoosdadosnobancodedados CasadoCódigo
Lembrete sobre o DAO
ODataAccessObjectéapenasumaclassecujoobjetivoéisolaro
acessoaosdadosdeumdeterminadapartedosistema.Nonossoexem-
plo,vamosprecisargravar,listarecarregarumproduto.Nãoqueremos
misturaressapartedeacessoàinfraestruturacomnossaslógicas.
Ocódigodométodo savedeveficarparecidocomoquesegue:
public String save(Product product){
productDAO.save(product);
return "products/ok";
}
Edeondevemessainstânciadaclasse ProductDAO?Umadasop çõesé
queagentemesmotenhacriadoesseobjeto,namão.
private ProductDAO productDAO = new ProductDAO();
public String save(Product product){
productDAO .save(product);
return "products/ok";
}
Oproblemaéque,provavelmente,oconstrutordo ProductDAOvaipre-
cisarreceberalgumobjetoquerepresenteaconexãocomobancodedados
e,nessecaso,vamosterquecome çaracontrolaressasdependênciasnamão.
EssaéumaótimaparteparausarmosoSpringMVC,poiscomoeleécom-
pletamenteintegradocomoSpring,podemospedirqueoSpringcrieesse
objetoparagente.Onossoúnicotrabalhoéindicarqueprecisamosreceber
injetadoumainstânciado ProductDAO.
public class ProductsController {
...
@Autowired
34

## Página 42

CasadoCódigo Capítulo3. Cadastrodeprodutos
private ProductDAO productDAO;
public String save(Product product){
productDAO.save(product);
return "products/ok";
}
}
Aannotation @Autowiredéjustamentearesponsávelporindicaros
pontosdeinje çãodentrodasuaclasse.
Nesseexatomomento,nossocódigonãocompila,jáquenãocriamos
aindaaclasse ProductDAO,assimcomonãoexisteométodo save.Chegou
ahoraderesolvermosessapartedonossocódigo.
package br.com.casadocodigo.loja.daos;
@Repository
public class ProductDAO {
@PersistenceContext
private EntityManager manager;
public void save( Product product){
manager.persist(product);
}
}
AquiestamosusandoaJPApararealizarapartedeacessoefetivoaonosso
bancodedados. Napróximase çãojávamostratardecomoconfigurá-la.
Voltandoaonosso ProductDAO,elaéumaclassebemnormaleoúnico
detalheaoqualficaratentoéemrelaçãoaousodaannotation @Repository.
ParaqueoSpringcarregueessaclasseegerencietodoseuciclodevida,é
necessárioquesejausadaumaanotação.Nonossoexemplo,estamosusando
a @Repository,apenasparaindicarqueessaclasse,alémdesergerenciada
peloSpring,étambémresponsávelpeloacessoadados.Existemalgunstipos
possíveisdeannotationsquepodemosusarquandoqueremosindicarque
umaclassesejagerenciadapelocontainer.
35

## Página 43

3.4. ConfigurandoaJPAcomoHibernate CasadoCódigo
•@Component: asemânticaenvolvidaéqueessaclasseéumbeando
Spring.
•@Respository:aclasseéresponsávelpeloacessoadados.
•@Controller:paraindicarqueessaclasseinteragecomosrequests
vindosdaweb.
•@Service:paraindicarqueaclasserepresentaumcomponenteinti-
mamenteligadoaalgumaregradenegóciodosistema.
Oidealésempreusaraannotationquecarregaasemânticamaispróxima
aousodaclasse.Alémdisso,oseuusodeformacorretaaindafacilitaavida
doSpring.Porexemplo,quandovocêutilizaa @Controllerestáindicando
queosmétodosdaclasseemquestãosãoresponsáveisportratarrequisições
eissofazcomqueelessejamescaneadospeloSpring.
3.4 C onfigurando a JP Acom o Hibernate
Estamosquaseconseguindogravaroproduto,sófaltaagoraconfigurarmosa
JPAparaquenossoacessoaobancodedadosfiquecompleto.Parafazerisso,
precisamosseguiralgunspassos.
Dependências para a JP A, Hibernate e o Mysql
É necessário que sejam adicionadas as dependências ao arquivo
pom.xml,dessaformaoMavenpodebaixaros jarsnecessários.
<project ....
<dependencies>
...
<!-- configuracao jpa e driver -->
<dependency>
<groupId>org.hibernate</groupId>
<artifactId>hibernate-entitymanager</artifactId>
<version>4.3.0.Final</version>
</dependency>
36

## Página 44

CasadoCódigo Capítulo3. Cadastrodeprodutos
<dependency>
<groupId>org.hibernate</groupId>
<artifactId>hibernate-core</artifactId>
<version>4.3.0.Final</version>
</dependency>
<dependency>
<groupId>org.hibernate.javax.persistence</groupId>
<artifactId>hibernate-jpa-2.1-api</artifactId>
<version>1.0.0.Final</version>
</dependency>
<dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-orm</artifactId>
<version>4.1.0.RELEASE</version>
</dependency>
<dependency>
<groupId>mysql</groupId>
<artifactId>mysql-connector-java</artifactId>
<version>5.1.15</version>
</dependency>
</dependencies>
</project>
Comoimportamosnossoprojetocomoum Maven Project, opróprio
eclipsejávaibaixareatualizaronossoclasspathcomasnovasdependências!
Mapeando a entidade
Comasdependênciasdevidamenteconfiguradas,chegouahoradefa-
zermosasconfiguraçõesnecessáriasparaqueosobjetosdaclasse Product
possamsersalvos.Umpassoimportanteéensinaraimplementaç ãodaJPA,
nossocasooHibernate,queaclasse Productvairepresentarumatabelano
bancodedados.
@Entity
public class Product {
37

## Página 45

3.4. ConfigurandoaJPAcomoHibernate CasadoCódigo
@Id
@GeneratedValue(strategy = GenerationType.IDENTITY)
private Integer id;
private String title;
@Lob
private String description;
private int pages ;
AquiusamosalgumasannotationsespecíficasdaJPApararealizaresses
ensinamentos.
•@Entity:indicaqueaclassevaivirarumatabela.
•@Id:indicaqueoatributoemquestãoéachaveprimária.
•@GeneratedValue:indicaamaneiracomovaisergeradaachavepri-
mária.
•@Lob: indicaqueoatributoemquestãovaisersalvocomoClobou
Blobnobancodedados.
CasovocênãosejafamiliarizadocomaJPA,fiquetranquilo,vamosfi-
carapenasnobásicodela,nossofocoaquiéoSpringMVC.Detodojeito,a
documentaçãodoHibernateéumafontedeestudos.
Isolando a configuração da JP A
Agora,comoparaqualqueracessoaobancodedados,énecessárioque
informemosalgumasdetalhesimportantescomo:
• Driverquedeveserusadoparaoacesso;
• LogineSenhadobancodedadosinstalado;
• URLdeacessoaobanco;
• ConfiguraçõesdaimplementaçãodaJPA.
38

## Página 46

CasadoCódigo Capítulo3. Cadastrodeprodutos
Pararealizaressasconfigurações,vamoscriarumanovanaclasse,nopa-
cote br.com.casadocodigo.loja.conf.
public class JPAConfiguration {
@Bean
public LocalContainerEntityManagerFactoryBean
entityManagerFactory(){
LocalContainerEntityManagerFactoryBean em = new
LocalContainerEntityManagerFactoryBean();
em.setDataSource(dataSource());
em.setPackagesToScan(new String[]
{ "br.com.casadocodigo.loja.models" });
JpaVendorAdapter vendorAdapter =
new HibernateJpaVendorAdapter();
em.setJpaVendorAdapter(vendorAdapter);
em.setJpaProperties(additionalProperties());
return em;
}
@Bean
public DataSource dataSource(){
DriverManagerDataSource dataSource =
new DriverManagerDataSource();
dataSource .setDriverClassName( "com.mysql.jdbc.Driver");
dataSource .setUrl(
"jdbc:mysql://localhost:3306/casadocodigo");
dataSource .setUsername( "root" );
dataSource .setPassword( "" );
return dataSource;
}
private Properties additionalProperties() {
Properties properties = new Properties();
properties .setProperty("hibernate.hbm2ddl.auto",
"update");
39

## Página 47

3.4. ConfigurandoaJPAcomoHibernate CasadoCódigo
properties.setProperty("hibernate.dialect",
"org.hibernate.dialect.MySQL5Dialect");
properties.setProperty("hibernate.show_sql", "true");
return properties;
}
}
Aconteceubastantecoisanessetrechodecódigo,masnadamuitodife-
rentedoquevocêjáconhece. Ométodo dataSource()serveparacon-
figurarmososparâmetrosdeconexãocomobancodedados.Vocêvaiusar
essemesmoestilodeconfiguraçãomesmoqueestejausandoJDBCpuro,ou
qualqueroutroframeworkdeacessoadados.
Já o métodoentityManagerFactory precisa de um pouco mais
de carinho. Ele cria alguns objetos que são importantes para o
nosso entendimento do que realmente está acontecendo. A classe
LocalContainerEntityManagerFactoryBeanéaabstraçãodoarquivo
persistence.xml,quegeralmenteénecessárioparatermosaJPAfuncio-
nandononossoprojeto. Aclasse HibernateJpaVendorAdapterrepre-
sentaanossaescolhadeimplementaç ãodaJPAque,nonossoprojeto,será
oHibernate. Omódulode ORMdoSpringsuportaainda,nativamente,o
EclipseLinkeaOpenJPA.
Aannotation @Bean,usadaemcimadosmétodos,éparaindicarqueos
objetoscriadosporelesvãosergerenciadospeloSpringepodemserinjetados
emqualquerpontodocódigo.
Agoraosúltimosdetalhesdeconfiguração.Oprimeiroéqueprecisamos
informaraoservletdoSpringMVCqueeletambémdevecarregaressaclasse,
paraquetodosessesmétodospossamserlidoseosobjetosdisponibilizados.
public class ServletSpringMVC extends
AbstractAnnotationConfigDispatcherServletInitializer {
...
@Override
protected Class<?>[] getServletConfigClasses() {
return new Class[]{AppWebConfiguration.class,
40

## Página 48

CasadoCódigo Capítulo3. Cadastrodeprodutos
JPAConfiguration.class};
}
}
Osegundoéquena AppWebConfiguration,énecessárioinformarque
opacotedaclasse ProductDAOdeveserlido,paraquetodasasclassesque
possuamalgumadasannotationsdecomponentesdoSpring,possamsercar-
regadas.
@EnableWebMvc
@ComponentScan(basePackageClasses = { HomeController.class,
ProductDAO .class })
public class AppWebConfiguration extends WebMvcConfigurerAdapter {
...
}
@PersistenceContext
Naclasse ProductDAO,parapedirmosainje çãodo EntityManager,foi
usadaaannotation @PersistenceContext.Essaannotationvemdapró-
priaespecificaçãoJPA.Geralmente,elaéusadadentrodosservidoresJavaEE,
masnadaimpededeoutroframeworkqualquerfazerusodamesma.Perceba
queonome PersistenceContexttemtodoumvalorsemântico:elereal-
menteindicaqueaclassequerreceberalium EntityManager.Comoissovai
serimplementado,issoéproblemadecadaferramenta.
3.5 H abilitando o controle transacional
Casovocêsejaumleitorumpoucomaisansioso,jádevetertentadogravarum
novoprodutonobancodedadose,provavelmente,nãoestámuitocontente
comoresultadoquerecebeu.
41

## Página 49

3.5. Habilitandoocontroletransacional CasadoCódigo
Fig.3.1:Exceptionporfaltadeumgerenciadordetransações
Comoaprópriaexceptioninforma,nãotemosaindaum EntityManager
capazderealizaroperaçõestransacionais. Paraanossasorte,issoéapenas
maisumpassoquedevemosconfigurar.Vamosadicionarmaisummétodoe
umaannotationnaclasse JPAConfiguration.
@EnableTransactionManagement
public class JPAConfiguration {
...
@Bean
public PlatformTransactionManager transactionManager
(EntityManagerFactory emf){
JpaTransactionManager transactionManager =
new JpaTransactionManager();
transactionManager.setEntityManagerFactory(emf);
return transactionManager;
}
}
@EnableTransactionManagementéannotationqueindicaqueagora
vamosusarocontroletransacionaldoSpring.
Além de indicar que queremos o controle transacional, preci-
samos informar por qual implementação vamos optar. A classe
PlatformTransactionManager é justamente o ponto central do
42

## Página 50

CasadoCódigo Capítulo3. Cadastrodeprodutos
Springparaessecontrole.Nonossocasoestásendousadaaimplementaç ão
paraaJPA.Aindapoderíamos,porexemplo,usaraimplementaç ãodireta
paraoHibernateouatéparaoJDBC.
Além desse passo, precisamos informar que os métodos da
ProductsController precisam de transação. Para isso, basta que
seja adicionada a annotation@javax.transaction.Transactional
emcimadaclasse.
@Controller
@Transactional
public class ProductsController {
...
}
Assimcomoa @PersistenceContext,a @Transactionalpertence
aumaespecificaçãodoJavaEE,sóquenessecaso,aJTA.
Pronto,agoraocadastrodeprodutosdeveestarfuncionandocorreta-
mente.Salvealgunsprodutosedepoisconsultenobancodedados,paraver
seestátudolá!
3.6 C onclusão
Nestecapítulo,navegamosporalgunspontosimportantesdoprojeto.Agora
jásabemoscomoreceberobjetosmontadosapartirdeparâmetrosdofor-
mulário,assimcomovimoscomorealizartodaconfiguraçãonecessáriapara
usaraJPAdentrodonossoprojeto.Casonãoestejaaindacansado,jáleiao
próximocapítulo,poisvamosincrementarocadastro,fazeralistagememais
algumascoisas.
43

## Página 52

Capítulo4
Melhorandoocadastroea
listagem
4.1 R ecebendo uma lista de v alores no formu-
lário
Onossoformuláriojáfazocadastrobásicodeumproduto,sóquenaCasa
doCódigoomesmolivropodeservendidoemformatosdiferenteseanossa
implementaçãoatualnãosuportaisso.Oprimeiropontoaseralteradoéque
nossaclasse Productdevesuportarumalistadepre çoseseusrespectivos
formatos.
...
@Entity

## Página 53

4.1. Recebendoumalistadevaloresnoformulário CasadoCódigo
public class Product {
...
@ElementCollection
private List<Price> prices = new ArrayList<Price >();
//getters e setters
}
Agoraprecisamoscriaraclasse Price.
package br.com.casadocodigo.loja.models;
@Embeddable
public class Price {
@Column(scale = 2)
private BigDecimal value;
private BookType bookType;
//getters e setters
}
Paratermosostiposdelivrosbemdefinidos,vamosusaruma enum,no
casoa Booktype.
public enum BookType {
EBOOK,PRINTED,COMBO
}
Agora, se rodarmos a aplicação, por conta da criação do
EntityManagerFactory, o nosso banco de dados já vai ser alterado
eanovatabelajávaisercriada.
Modificando nosso formulário
Comaclassejáalterada,precisamosfazerasdevidasmodificaçõesnapá-
ginaquecontémoformuláriodecadastrodoproduto.
46

## Página 54

CasadoCódigo Capítulo4. Melhorandoocadastroealistagem
<%@taglib uri="http://java.sun.com/jsp/jstl/core" prefix= "c"%>
...
<c:forEach items="${types}" var="bookType" varStatus="status" >
<div>
<label for="price_${bookType}">${bookType}</label>
<input type="text" name="prices[${status.index}].value"
id="price_${bookType}"/>
<input type="hidden"
name="prices[${status.index}].bookType"
value="${bookType}"/>
</div>
</c:forEach>
Dêumarespirada,jáqueessepequenotrechoamaisnoformuláriojá
contémmuitacoisa. Opontomaisimportanteaquiéque,parapassaruma
listadevaloresdoformulárioparaocontrollerdoSpringMVC,énecessário
ousodo []. Usamosoatributo varStatusparaconseguirteracessoao
índiceatualdoloope,comisso,irconstruindoosinputs.Nasituaç ãoatual,
o htmlgeradoseriacomooquesegue:
<div>
<div>
<label for="price_EBOOK">EBOOK</label>
<input type="text" name="prices[0].value"
id="price_EBOOK"/>
<input type="hidden" name="prices[0].bookType"
value="EBOOK"/>
</div>
<div>
<label for="price_PRINTED">IMPRESSO</label>
<input type="text" name="prices[1].value"
id="price_PRINTED"/>
<input type="hidden" name="prices[1].bookType"
value="IMPRESSO"/>
</div>
47

## Página 55

4.2. Disponibilizandoobjetosnaview CasadoCódigo
<div>
<label for="price_COMBO">COMBO</label>
<input type="text" name="prices[2].value"
id="price_COMBO"/>
<input type="hidden" name="prices[2].bookType"
value="COMBO"/>
</div>
</div>
Comoanossaclasse Productpossuiagoraosmétodosdeacessoaoatri-
buto prices,opróprioSpringMVCvaipopularonossoobjeto.Essaregra
serveparaqualquersituaçãoquevocêqueirapassarumalistadeinforma-
çõesdoformulárioparaocontroller.Ousodo [índice]serásempreneces-
sário. Porexemplo,comodesafio,oleitorpodefazerummétodonaclasse
ProductsControllerquerecebaumalistadelivrosaseremcadastrados.
4.2 D isponibilizando objetos na view
Umpontoquetalveztenhachamadoaaten çãofoiarealizaçãodo forEach
sobreavariável types.Afinaldecontas,ondeelafoicriadaecomoelafoidis-
ponibilizada?Essavaiserjustamenteumadasfinalidadesdométodo form,
naclasse ProductsController. Chegamosatéacomentar,nocapítulo
anterior,queusaríamosestemétodoparanãodarachancedenenhumusuá-
riochegaràpáginadoformuláriodiretamentepelaJSP.Oargumentofoijus-
tamenteque,casofossenecessáriodisponibilizarobjetosparaaview,seria
melhorqueessecódigoficassedentrodeumaclasseenãodeumapágina.
Paraessetipodetarefa,oSpringMVCofereceaclasse ModelAndView.
@RequestMapping("/form")
public ModelAndView form(){
ModelAndView modelAndView =
new ModelAndView("products/form");
modelAndView.addObject("types", BookType.values());
return modelAndView;
}
48

## Página 56

CasadoCódigo Capítulo4. Melhorandoocadastroealistagem
Aclasse ModelAndViewpossuimétodosquenospermitemiradicio-
nandoobjetosqueserãodisponibilizadosnaview.Paraquemquiserfazero
paralelo,portrásdospanosoSpringMVCvaipegaraschavesevalorespas-
sadosparaesseobjetoerepassarparaorequestatual,algoparecidocomo
quesegue:
Map<String,Object> modelMap = modelAndView.getModelMap();
Set<String> keys = modelMap.keySet();
for(String key : keys ){
Object value = modelMap.get(key);
request.setAttribute(key,value );
}
Nofimdascontas,éométodo setAttributequegarantequeosobje-
tosestarãoacessíveisnaview.
EparaqualviewoSpringMVCdeveir,jáqueagoraestásendodevol-
vidoumobjetodotipo ModelAndView?Éjustamenteparaissoqueserveo
construtorrecebendoaString.
new ModelAndView("products/form");
Vale lembrar que, por conta da configuraç ão do
InternalResourceViewResolverestamosapenaspassandoapastaeo
nomedapágina,queestãodentrode WEB-INF/views.
49

## Página 57

4.3. Listandoosprodutos CasadoCódigo
Outra maneira de passar objetos para a view
Emvezderetornarumobjetodotipo ModelAndView,podemos
recebercomoparâmetrodométodo,umobjetodotipo Model.
public String form(Model model){
model.addAttribute("types", BookType.values());
return "products/form";
}
Aquiémaisumaquestãodegosto. Naminhaopinião,retornarum
objetodotipo ModelAndViewdeixamaisclaroqueométodoestádis-
ponibilizandoobjetosparaapágina.
Umoutropontoaserobservadoéorecebimentodesseparâmetro.
EssaéoutrapossibilidadedeoSpringinjetarobjetosnasclasses.
4.3 L istando os produtos
OutrafuncionalidadeimportantenaCasadoCódigoéadelistaroslivros.O
interessantedessaimplementaçãoéquenãoprecisaremosusarnadadenovo,
eservirácomorevisãodealgunsdosconceitosqueforamdiscutidosatéaqui.
Mais uma vez, vamos começar pensando na página, que terá
o nome de list.jsp e ficará, como já era esperado, na pasta
WEB-INF/views/product:
<%@ page language= "java" contentType="text/html; charset=UTF-8"
pageEncoding="UTF-8"%>
<%@taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;
charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
<table>
<tr>
50

## Página 58

CasadoCódigo Capítulo4. Melhorandoocadastroealistagem
<td>Titulo</td>
<td>Valores</td>
</tr>
<c:forEach items="${products}" var="product">
<tr>
<td>${product.title}</td>
<td>
<c:forEach items="${product.prices}"
var="price">
[${price.value} - ${price.bookType}]
</c:forEach>
</td>
</tr>
</c:forEach>
</table>
</body>
</html>
Paraousuáriochegaraessapágina,teráquepassarpelonossocontroller.
Logo,jávamoscriarométodoresponsávelporisso.
@Controller
@Transactional
public class ProductsController {
//resto do código
@Autowired
private ProductDAO productDAO;
@RequestMapping("/produtos")
public ModelAndView list(){
ModelAndView modelAndView =
new ModelAndView("products/list");
modelAndView.addObject("products", productDAO.list());
return modelAndView;
}
}
Agora,paraessecódigocompilar,precisamoscriarométodo listna
51

## Página 59

4.4. MelhorusodosverbosHTTP CasadoCódigo
classe ProductDAO.
@Repository
public class ProductDAO {
@PersistenceContext
private EntityManager manager;
...
public List<Product> list() {
return manager.createQuery("select distinct(p) from
Product p join fetch p.prices",Product.class)
.getResultList();
}
}
Umdetalhequeoleitormaisatentopodeternotadoéqueosmétodos
savee list,naclasse ProductsController,estãocomamesmaURL.
Eagora?
4.4 M elhor uso dos verbos HTTP
Nestemomento,casoaURL /produtossejaacessada,vamosreceberase-
guinteexception:
java.lang.IllegalStateException: Ambiguous mapping found....
Orestodaexceptionfoiocultado,jáqueocome çodeladiztudo.Temos
doismétodostentandousaromesmomapeamentodeURLs.Pensandobem
nasURLs,elasatéfazemsentido:
•/produtos, paraadicionarumnovoprodutoemumalistaquejá
existe;
•/produtos,paralistarosprodutoscadastrados.
Oproblemaaquiéqueestamosdeixandodeusarumrecursoimportante
doprotocoloHTTP,osverbos.
52

## Página 60

CasadoCódigo Capítulo4. Melhorandoocadastroealistagem
•POST:usadoquandoexisteanecessidadedecriaç ãodealgumrecurso;
•GET:usadoquandoointeresseéoderecuperaralgumainformaç ão;
•DELETE:comoonomediz,deveserusadoparaexcluiralgumrecurso;
•PUT:associadocomalgumaoperaç ãodeatualizaçãoderecursosno
servidor.
Estestalvezsejamosverbosmaisconhecidos,comdestaqueparao post
eo get.Porsinal,quandocriamosumaclassequeherdade HttpServlet,
temosaop çãodeimplementarcadaumdeles,separadamente.
O verbo, junto com a URL, serve justamente para indicar o tipo de
operaçãoquedeveserrealizadanoservidor. Porexemplo,seoendere ço
/produtosforacessadoatravésdeum get,querdizerqueumalistagem
estásendorequisitada. Casosejaacessadaatravésdeum post,estásendo
pedidoparaumnovoprodutosercriado.Vamosvercomoficaarepresenta-
çãodessateoriaemnossocódigo:
...
@RequestMapping(value="/produtos",method=RequestMethod.POST)
public String save(Product product){
...
}
@RequestMapping(value="/produtos",method=RequestMethod.GET)
public ModelAndView list(){
...
}
Pronto!AgoraoSpringMVCvaiescolherqualmétododeveserusadoem
funçãodoverboutilizadonoacessoaoendere ço/produtos. Essaéuma
ótimaprática,tentesempredefinirqualverbodeveserutilizadoparaacessar
cadaURLdoseusistema.
53

## Página 61

4.5. ModularizaçãodasURLsdeacesso CasadoCódigo
4.5 M odularização das URLs de acesso
AindasobreosmapeamentosdasnossasURLs,percebaquetodososende-
reçosrelacionadoscomocadastrodeprodutoscome çamcom /produtos.
@RequestMapping("/produtos/form")
public String form(){
return "products/form";
}
@RequestMapping(value="/produtos",method=RequestMethod.POST)
public String save(Product product){
...
}
@RequestMapping(value="/produtos",method=RequestMethod.GET)
public ModelAndView list(){
...
}
Provavelmente,essepadrãovaiapareceremdiversosmódulosdasuaapli-
caçãoe,paradiminuiressarepetiç ão,oSpringMVCpermitequevocêanote
umendereçobasediretamentesobreaclasse.
@Controller
@Transactional
@RequestMapping("/produtos")
public class ProductsController {
@RequestMapping("/form")
public String form(){
return "products/form";
}
@RequestMapping(method=RequestMethod.POST)
public String save(Product product){
...
}
@RequestMapping(method=RequestMethod.GET)
54

## Página 62

CasadoCódigo Capítulo4. Melhorandoocadastroealistagem
public ModelAndView list(){
...
}
}
Percebaqueagora,quandonecessário,vocêpodecolocarapenasocom-
plementodoendere ço.
4.6 F orw ard x Redirect
Agoraquejáinserimoselistamos,chegouahorademelhorarumpouco
fluxoentreessasoperações.Nestemomento,quandoumprodutoéinserido,
ousuárioélevadoparaumapáginachamada ok.jsp,queapenasindica
queumnovolivrofoicadastradocomsucesso.Nessetipodecenário,ofluxo
maisindicadoévoltarcomousuárioparaalistagem,talvezmostrandouma
mensagemdesucesso.
@RequestMapping(method=RequestMethod.POST)
public ModelAndView save(Product product){
productDAO .save(product);
return list();
}
Essecódigoimplementajustamenteofluxosugerido.Quandoacabamos
desalvarumnovoproduto,invocamosométodo lista,queéoresponsá-
velporlistarosprodutosejogá-losparaapágina products/list.jsp.O
pontonegativodessasoluçãoéqueoendere çoqueficanabarradonavega-
doraindaéoúltimoacessadopelousuário,quenessecasofoium postpara
/produtos.Casoonossoclienteaperteum F5,onavegadorvaitentarre-
fazeraúltimaoperação,causandoumanovainser çãodeprodutonosistema.
55

## Página 63

4.6. ForwardxRedirect CasadoCódigo
Fig.4.1:Problemadoforwarddepoisdeumpost
Observequeopróprionavegadorpercebequetemalgodeestranhoe
perguntasevocêtemcertezadequequerreenviarosdados.Essatécnicade
redirecionamentoqueaconteceapenasdoladodoservidoréoquechama-
mos,nomundoJava,de forward.Obrowsernemsabeoqueaconteceu,tanto
que,seolharmosnoconsoledoChrome,elesóvaiidentificarumrequest.
Fig.4.2:Chrometoolsindicaapenasumrequest
Éconsideradaumamápráticarealizarumforwardapósousuárioter
feitoum post,justamenteporcontadoproblemadaatualizaç ão.Paraesse
cenário,amelhorsoluçãoéforçarousuárioafazerumanovarequisiçãopara
anossalistageme,dessaforma,permitirqueeleatualizeapáginasemque
umnovo postsejarealizado.
@RequestMapping(method=RequestMethod.POST)
public String save(Product product){
productDAO.save(product);
return "redirect:produtos";
}
Oprefixo redirect:indicaparaoSpringMVCque,emvezdesim-
plesmentefazerumforward,énecessárioqueeleretorneostatus302parao
56

## Página 64

CasadoCódigo Capítulo4. Melhorandoocadastroealistagem
navegador,solicitandoqueomesmofaçaumnovorequestparaonovoende-
reço.
Fig.4.3:Chrometoolsindicadoisrequests
Percebaqueentreoscabe çalhoscontidosnarespostaexisteumchamado
Location,queinformajustamentequaléoendere çoaoqualonavegadordeve
fazerapróximarequisição.Essatécnica,ondefazemosumredirectdolado
doclientelogoapósum post,éumpadrãoconhecidodawebchamadode
Always Redirect After Postedevesersempreutilizado.
4.7 P arâmetros extras nos redirects
Aindasobreonossoredirect,geralmenteénecessárioqueindiquemospara
ousuárioquerealmentetudoocorreubem.Issoéfeitoexibindoumamen-
sagemdesucessoparaoclienteemquestão.
Umadasmaneirasderealizaressatarefaéutilizandoalgumasclassesque
jáestudamos.
@RequestMapping(method=RequestMethod.POST)
public ModelAndView save(Product product){
productDAO .save(product);
ModelAndView modelAndView =
new ModelAndView("redirect:produtos");
57

## Página 65

4.7. Parâmetrosextrasnosredirects CasadoCódigo
modelAndView.addObject("sucesso",
"Produto cadastrado com sucesso");
return modelAndView;
}
Comooendere çopassadoparao ModelAndViewcontémumredirect,
opróprioSpringMVCvaipegarosobjetosadicionadosepassá-loscomoar-
gumentosdaURL /produtos.
http://localhost:8080/casadocodigo/produtos?
sucesso=Produto+cadastrado+com+sucesso
Essatécnicafuncionatranquilamente,masumdosmedosdosdesenvol-
vedoreséquealgumclientepossaalteraraURLecausaralgumdanopara
osistema. Outraquestãoéqueosobjetosadicionadosno ModelAndView
paraumredirect,sópodemserdotipoString.Omotivoéque,comojámos-
tramos,elesserãousadoscomoparâmetrosdaURL.
Outramaneiradepassarmosessesobjetoséguardando-osnasessãodo
usuário.Oproblemaéqueessesobjetosserãomantidosenquantonossousuá-
rioestiverativonaaplicaçãoe,nanossasituação,queremosapenasqueeles
sejammantidosatéopróximorequest.Foijustamenteparaestetipodecená-
rioquecriaramumnovoescopodentrodosframeworks,chamadode flash.
@RequestMapping(method=RequestMethod.POST)
public String save(Product product,
RedirectAttributes redirectAttributes){
productDAO.save(product);
redirectAttributes.addFlashAttribute("sucesso",
"Produto cadastrado com sucesso");
return "redirect:produtos";
}
Aclasse RedirectAttributeséjustamentearesponsávelporisso.
Todoobjetoadicionadonela,atravésdométodo addFlashAttribute,fi-
carádisponívelatéopróximorequest,sendoacessíveldemaneirasimples
atravésdaExpressionLanguage.
${sucesso}
58

## Página 66

CasadoCódigo Capítulo4. Melhorandoocadastroealistagem
4.8 C onclusão
Nestecapítulo,estudamosmaisdetalhessobrecomooSpringMVClidacom
osformulários.Alémdisso,vimoscomopodemossermaisespecíficosemre-
laçãoàsnossasURLs,usandoosverbos.Parafechar,deixamosnossosende-
reçosmaismodulareseaindadiscutimos forwardse redirects,inclusivevendo
comofuncionaapassagemdeobjetosparaosdoismodelosderedireciona-
mentos.
59

## Página 68

Capítulo5
Validaçãoeconversãodedados
Onossocadastrojáestáfuncional,masestamosdeixandodefazerumacoisa
básica:validarosdadosdeentrada.Nestemomento,casoumusuárioqueira
cadastrarumnovolivro, eletemaop çãodedeixartodososcamposem
branco.
5.1 V alidação básica
Aprimeiraop çãodesoluçãoparaessasituaçãoéescreverocódigodevalida-
çãodentrodoprópriométodo save,daclasse ProductsController.
@RequestMapping(method=RequestMethod.POST)
public String save(Product product,
RedirectAttributes redirectAttributes){
if(StringUtils.isEmpty(product .getTitle())){

## Página 69

5.1. Validaçãobásica CasadoCódigo
//adiciona erro de validação
}
if(StringUtils.isEmpty(product.getDescription())){
//adiciona erro de validação
}
productDAO.save(product);
redirectAttributes.addFlashAttribute("sucesso",
"Produto cadastrado com sucesso");
return "redirect:produtos";
}
Alógicanãotemnadadenadadecomplicado,naverdadedeveserbem
parecidacomváriasqueoleitorjápresenciou.Umpontonegativodessasolu-
çãoéqueocontroller,queidealmentedeveriaapenasficarchamandológicas
dosistemaecontrolandoqualéopróximodenavegaç ão,agoratambémestá
responsávelpelocódigodevalidação.Umaoutraquestãoéqueoobjetodo
tipo Productpodeservalidadoemoutroslugaresdosistema,porexemplo
nafuncionalidadedesalvarvárioslivrosdeumavez.Paracontornarmosessas
situações,podemosdeixaralógicadevalidaçãoemumaoutraclasse,espe-
cializadaapenasparaisso.Ecomoessaéumafuncionalidaderequeridaem
váriasaplicações,oSpringjápossuiummódulofocadoapenasemvalidação,
vamoscomeçarausá-lo.
package br.com.casadocodigo.loja.validation;
import org.springframework.validation.Validator;
public class ProductValidator implements Validator{
@Override
public void validate(Object target, Errors errors) {
ValidationUtils.rejectIfEmptyOrWhitespace(errors,
"title", "field.required");
ValidationUtils.rejectIfEmptyOrWhitespace(errors,
"description", "field.required");
Product product = (Product) target;
62

## Página 70

CasadoCódigo Capítulo5. Validaçãoeconversãodedados
if(product.getPages() == 0){
errors.rejectValue("pages", "field.required");
}
}
}
Aregradevalidaçãopermanecebasicamenteamesma,omaisinteres-
santeéapartequeoSpringnosfornece. Primeiramenteimplementamosa
interface Validator,quenosobrigaaescreverdoismétodos:
•supports:analisaremosessemétodoemalgunsminutos.
•validate:responsávelpelavalidaçãoemsi.
Ométodo validaterecebecomoargumentooobjetoaservalidado,
nocasoespecificadopeloparâmetro targeteumoutroobjetodotipo
Errors,ondevamosguardandocadaumadasfalhasdevalidaç ão.Aclasse
ValidationUtilséum helperdoSpringValidationpararealizaralgumas
validaçõesbásicas.Aquiéinteressanteanalisaraassinaturadosmétodosque
começamcom reject.
public static void rejectIfEmpty(Errors errors, String field,
String errorCode) {....}
•Errors errors: objetoondeseráguardadocadaumdoserrosde
validação.
•String field: representaoatributodomodeloquedeveservali-
dado.
•String errorCode:chavequeseráusadaparabuscarmosamensa-
gemrelativaaesseerro.
Umdetalheimportanteemrelaçãoaoparâmetro fieldéque,porexem-
plo, sequisermosvalidaroestadodosobjetosdotipo Price, danossa
classe Product,teríamosqueusaraseguintesintaxe: price.value.Isso
63

## Página 71

5.1. Validaçãobásica CasadoCódigo
valeparaoutroscasostambém. Sefornecessáriovalidarasinformações
deendereçodeumaclasse Usuario,provavelmenteseriapassadaaString
endereco.ruaeassimpordiante.
Parafechar,casosejaprecisofazerumalógicadevalidaç ãoquenãoexista
naclasseutilitária,podeserusadoométodo rejectValueparaadicionar
amensagemnalistadeerros.Essemétodoédaprópriaclasse Errors.
public class ProductValidator implements Validator{
@Override
public void validate(Object target, Errors errors) {
....
Product product = (Product)target;
if(product .getPages() == 0){
errors.rejectValue("pages", "field.required");
}
}
Na verdade, isso é o que é feito dentro dos métodos da classe
ValidationUtils.
Configurando a validação no Controller
Agoraquetemosnossaclasseresponsávelpelavalidaç ãodeobjetosdo
tipo Product,precisamospedirparaoSpringMVCfazerusodela,nomo-
mentodaconstruçãodoobjetocomosdadosvindosdoformulário.
@RequestMapping(method=RequestMethod.POST)
public String save(@Valid Product product,
RedirectAttributes redirectAttributes){
...
}
Aannotation @Validvemdaespecificação Bean Validation,eé
utilizadapordiversosframeworksparaindicarodisparodoprocessodeva-
lidação.Agora,umpensamentoimportante:comooSpringMVCvaisaber
queéparausaraclasse ProductValidatorparavalidaroobjetodotipo
64

## Página 72

CasadoCódigo Capítulo5. Validaçãoeconversãodedados
Product?PararesolverissovamosfalarparaoSpringMVCqualvalidator
eledeveusar.
@Controller
@Transactional
@RequestMapping("/produtos")
public class ProductsController {
@InitBinder
protected void initBinder(WebDataBinder binder) {
binder.setValidator(new ProductValidator());
}
...
}
Aannotation @InitBinderindicaqueessemétododeveserchamado
semprequeumrequestcairnocontrolleremquestão. Onomedométodo
nãoéimportante,podeserqualquerum.Oimportanteéquevocêrecebeum
objetodotipo WebDataBindere,comele,épossívelregistrarnovosvali-
dators.Alinha binder.setValidator(new ProductValidator());
mostraexatamenteessaop ção.Atravésdesseobjeto,tambémpodemosadici-
onarnovosconversoresdetiposeinformarquaiscampospodemserenviados
peloformulário,entreoutrascoisas.
Paraessecódigojáficarfuncional,precisamosadicionarasdependências
necessáriasparapodermosusaraBeanValidation.Nonossocaso,vamosusar
oHibernateValidatorcomoescolhadeimplementaçãodessaespecificação.
<!-- JSR 303 with Hibernate Validator -->
<dependency>
<groupId>javax.validation</groupId>
<artifactId>validation-api</artifactId>
<version>1.0.0.GA</version>
</dependency>
<dependency>
<groupId>org.hibernate</groupId>
<artifactId>hibernate-validator</artifactId>
<version>4.1.0.Final</version>
</dependency>
65

## Página 73

5.1. Validaçãobásica CasadoCódigo
Umaúltimainformaçãorelevante:adicionamoso ProductValidator
comosendoovalidadorqueseráutilizadoparaqualquerformulárioqueen-
volvaocadastrodenovoslivros.Opontoaquié:podemexistirsituaçõesem
queoformuláriosejaumpoucodiferentee,aí,nãovamosterumaassociaç ão
tãodiretacomnossaclassedemodelo.Nessasocasiões,umaestratégiaécriar
umaoutraclassequerepresentejustamenteesseformulário.
public class UpdateProductForm {
// atributos que podem não existir na classe Product.
}
Poderiasercriadoumvalidatorespecíficoparaesteformulário.
public class UpdateProductFormValidator implements Validator{
....
}
Porfim,vocêadicionariamaisessevalidadorno WebDataBinder,ano-
tariaoparâmetrodométodocom @ValideoSpringMVCpoderiautilizá-lo.
Sóqueaperguntaé:comooframeworkvaisaberqueparadeterminadopa-
râmetroeledeveusarumvalidadoreque,paraoutroparâmetro,eledeveusar
outro?Arespostaéométodo supports,quetambémdeveserimplemen-
tadodentrodaclassequeimplementaainterface Validator.
public class ProductValidator implements Validator{
@Override
public boolean supports(Class<?> clazz) {
return Product.class.isAssignableFrom(clazz);
}
...
}
Essemétodorecebeaclassedoobjetoqueestáquerendoservalidadoe
retornaseovalidadorconseguelidarcomele.EssaéaformacomooSpring
MVCcontrolaqualvalidaçãodeveseraplicada.Inclusive,éumaótimama-
neiradesepararregrasdevalidaç ãoemváriasclassesedeixarqueoSpring
MVCexecutecadaumadelasparavocê.
66

## Página 74

CasadoCódigo Capítulo5. Validaçãoeconversãodedados
UmacuriosidadesobreousodasvalidaçõescustomizadasdoSpring:
casovocêassocieumaclassedevalidaçãoaumcontroller,masseumétodo
supportsnãoaceiteoparâmetroanotadocom @Valid,serálançadauma
exceptionparecidacomaquesegue.
java.lang.IllegalStateException: Invalid target for Validator
br.com.casadocodigo.loja.validacao.ProductValidator
Voltando para a tela de erro
Comavalidaçãobásicaconfigurada,nãoémaispermitidoquefaç amos
ocadastrodeumprodutocomdadosinválidos.Oproblemaéqueatelade
erro,nestemomento,nãoémuitoamigável.
Fig.5.1:Statusderequestinválido
Ocódigodeerro400indicaquearequisiç ãofoiexecutadacomdados
inválidos.Entretanto,nossousuárionãoentendenadadisso,oqueelequeré
voltarparaateladeformulário,parapreencheroscamposdevidamente.
@RequestMapping(method=RequestMethod.POST)
public String save(@Valid Product product,
BindingResult bindingResult,
RedirectAttributes redirectAttributes){
if(bindingResult.hasErrors()){
return "produtos/form";
}
productDAO .save(product);
redirectAttributes.addFlashAttribute("sucesso",
"Produto cadastrado com sucesso");
return "redirect:produtos";
}
67

## Página 75

5.1. Validaçãobásica CasadoCódigo
Paraconseguirmosverificarseoformulárioteveerroounão,fazemos
usodoobjetodotipo BindingResult.Essaclassepossuiváriosmétodos,
tantoparaverificarseexistemerrosdevalidaç ão,quantoparaacrescentar
novoserros,casooprogramadorqueiraefetuaralgumalógicadevalidaç ão
diretamentenométododocontroller.
Reaproveitando métodos no controller
Aindaprecisamoscompletarnossofluxo,jáqueosdadosenviadospelo
usuárionãoestãosendomostradosnoformulário,apósavalidaç ão. Além
disso,aindatemosoutroproblema,oscamposdepre çosportipodelivronão
estãomaissendoexibidos.Oproblemaéqueagenteretornaousuáriopara
oformulário,masnãoadicionano ModelAndViewostiposdelivros.Para
resolverisso,podemosfazerumalevemodificaç ãonométodo save,para
quesejapossívelreaproveitaralógicadométodo form.
@RequestMapping(method=RequestMethod.POST)
public ModelAndView save(@Valid Product product,
BindingResult bindingResult,
RedirectAttributes redirectAttributes){
if(bindingResult.hasErrors()){
return form();
}
productDAO .save(product);
redirectAttributes.addFlashAttribute("sucesso",
"Produto cadastrado com sucesso");
return new ModelAndView("redirect:produtos");
}
Agora,casosejaencontradoalgumerrodevalidação,éretornadooobjeto
dotipo ModelAndViewcriadopelométodo form,quejáéresponsávelpor
disponibilizarostiposdelivronaview. Casotudotenhaocorridobem,é
retornadoum ModelAndViewcomaStringderedirectparaURLdelistagem
deprodutos.
68

## Página 76

CasadoCódigo Capítulo5. Validaçãoeconversãodedados
5.2 E xibindo os erros
Nossousuário,apósumproblemadevalidação,jáéretornadoparaoformu-
lárioinicial.Sóqueaindanãomostramososerrosenemestamosmantendo
osdadospreenchidosporele.Essessãodoisproblemasqueprecisamserre-
solvidos.
Vamoscomeçarpelaexibiçãodoserrosnapágina.Semprequealgumerro
acontece,oSpringMVCdisponibilizaumobjetodotipo BindingResult
paraaJSP,contendotodasasinformaçõesnecessárias. Lembre-sequeesse
objetoéomesmoqueusamosnométododocontrollerparaverificarseforam
encontradoserrosdevalidação.
<%@taglib uri= "http://java.sun.com/jsp/jstl/core" prefix= "c"%>
...
<c:forEach
items="${requestScope['org.springframework.validation.
BindingResult.product'].allErrors}" var="error">
${error.code}<br/>
</c:forEach >
O método allErrors retorna uma lista de objetos do tipo
FieldError, o qual possui as informações relevantes sobre cada pro-
blemaencontradonoprocessodevalidação.
Essamaneiradeexibiroserrorsatéfunciona,oúnicoproblemadelaéo
nomehorríveldavariável. Issoéumadecisãointernadoframeworke,em
geral,essetipodecoisapodemudarfacilmente,atédeumupdateparaoutro.
Dessaforma,nãoébombasearqualquercódigodanossaaplicaç ãoemuma
Stringcomoessa.
Usando a tag hasBindErrors
Parafacilitaraexibiçãodasmesmasmensagensdeerro,podemosusar
uma taglibfornecidapeloSpringMVC.
69

## Página 77

5.2. Exibindooserros CasadoCódigo
<%@ taglib prefix= "spring"
uri="http://www.springframework.org/tags"%>
...
<spring:hasBindErrors name="product">
<ul>
<c:forEach var="error" items="${errors.allErrors}">
<li>${error.code}</li>
</c:forEach>
</ul>
</spring:hasBindErrors>
A tag hasBindErrors disponibiliza o mesmo objeto do tipo
BindingResultparavocê,sóqueagorasobavariável errors. Avan-
tageméqueocódigonãoficaacopladocomumaStringcriadadentrodofra-
mework.Elaaindapossuioatributo nameque,curiosamente,recebeucomo
argumentoaString produto. Todososerrosdevalida çãoouconversão,
capturadospeloprocessoSpringMVC,sãoassociadosaalgumparâmetro
emquestão.
public String save(@Valid Product product,...){
...
}
Nocasodométodo saveotipodoparâmetroé Producte,exatamente
porisso,passamosumaStringdemesmonome,comaprimeiraletraemmi-
núsculo,paraoatributo name,datag.Issoémuitoimportante,poiscasoo
métodopossuaoutrosparâmetrosquedevamservalidados,oserrosdecada
umficarãodisponíveisassociadosaotipodomesmoparâmetro. Paraficar
aindamaisclaro,vamoslembrardoprimeirocódigoutilizadoparaexibiros
problemasdevalidação.
<c:forEach
items="${requestScope['org.springframework.validation.
BindingResult.product'].allErrors}" var="error">
${error.code}<br/>
</c:forEach>
70

## Página 78

CasadoCódigo Capítulo5. Validaçãoeconversãodedados
Percebaqueavariávelacabacom .producteéjustamenteessamesma
variávelqueseráusadainternamentepelatag. Paraoleitormaiscurioso,
segueotrechodecódigodatagdoSpringMVCresponsávelporisso.
public class RequestContext {
....
public Errors getErrors(String name, boolean htmlEscape) {
Errors errors = this.errorsMap.get(name);
boolean put = false;
if (errors == null) {
errors = (Errors) getModelObject(
BindingResult.MODEL_KEY_PREFIX + name);
// Check old BindException prefix for backwards
// compatibility.
if (errors instanceof BindException) {
errors =
((BindException) errors).getBindingResult();
}
....
}
}
Atag hasBindErrorsfazpartedoconjuntodetagssobaURI http:
//www.springframework.org/tags. Essemesmonamespaceaindapossuidi-
versasoutrastagsquepodemserúteisparasuaaplicaç ão.Algunsexemplos:
•message: umaextensãodatagdemensagenspadrão,queexistena
JSTL.
•transform:paraaplicarconversõesdetiposespecíficosparaString.
•url:umaextensãodatagURLpadrão,queexistenaJSTL
•mvcUrl:fun çãoqueajudaareferenciarasURLsdosmétodosdentro
daJSP.
Afun ção mvcUrlmereceumaaten çãoespecial,poisvainosajudara
contornarumproblemaquejáestamosenfrentando.Atéagora,naactiondo
71

## Página 79

5.2. Exibindooserros CasadoCódigo
formuláriodecadastro,parareferenciarmosoendere çoquelevaatéométodo
decadastro,foiusadaaURLcompleta.
/casadocodigo/produtos
Issoatéfunciona,mastemosdoisproblemas:
• casoonomedocontextomude,temosquemudaraURL;
• casoaURLmude,seremosobrigadosamudaremtodoslugares.
Pararesolverosdoiscasos,existeafun ção mvcUrl.
<form action="${spring:mvcUrl("PC#save").build()}" method= "post">
Essafunçãorecebecomoparâmetroasletrasemmaiúsculodoseucon-
trollereonomedométodo,separadospelo #. Ométodo build()serve
pararealizaraconstruçãodaURL.Asaídaficariaassim:
http://localhost:8080/casadocodigo/produtos
Avantageméque, casovocêqueiramudaraURLdoseucontroller,
vocênãoprecisarámudaroslinksdasuapágina.Parafinalizar,sevocênão
gostardasintaxecomo #,épossívelusaroatributo namedaannotation
@RequestMappingedefinirumnomeparaserusadodentrodafun ção.
@RequestMapping(method=RequestMethod.POST,name="saveProduct")
public ModelAndView save(....){
....
}
Agora,quandoafun ção mvcUrlforutilizada,elapoderecebercomoar-
gumentoovalorpassadoparaoatributo namedaannotation.
${spring:mvcUrl("saveProduct").build()}
72

## Página 80

CasadoCódigo Capítulo5. Validaçãoeconversãodedados
5.3 E xibindo as mensagens de erro de maneira
amigável
Pormaisqueoformulárioestejasendovalidado,asmensagensdeerroainda
nãodizemmuitacoisasobreoproblemaemquestão.Atualmente,omáximo
quepodemosconseguiréexibiroserrosdaseguinteforma:
numeroPaginas - typeMismatch
titulo - field.required
descricao - field.required
numeroPaginas - field.required
Apenasparanãoficardúvidas,amensagem typeMismatchindicaque
aconteceuumproblemadeconversão. Nessecasoomotivoéqueocampo
númerodepáginasfoideixadoembrancoenomodelo Product,eleéum
atributodotipo int.
PararesolveresseproblemaprecisamosensinaraoSpringMVCondeele
devebuscarasmensagenscorretase,paraisso,vamoscriarumarquivoex-
ternocontendoasmesmas.Vamosdarumaolhadanoconteúdodele.
field.required = Campo obrigatorio
field.required.product.title = Titulo obrigatorio
Aqui configuramos uma mensagem padrão para a chave
field.required e ainda optamos por deixar uma específica para o
títulodoprodutoemquestão, field.required.product.title
Essearquivodevesercriadodentrodasuapasta WEB-INFegeralmenteé
chamadode messages.properties.AgoraénecessárioavisaraoSpring
MVCqueeledeveusá-loparabuscarasmensagensrelativasàschavesque
estãoconfiguradas. Paraisso,vamosadicionarumnovométodonaclasse
AppWebConfiguration.
@Bean
public MessageSource messageSource(){
ReloadableResourceBundleMessageSource bundle =
new ReloadableResourceBundleMessageSource();
bundle.setBasename("/WEB-INF/messages");
bundle.setDefaultEncoding("UTF-8");
73

## Página 81

5.3. Exibindoasmensagensdeerrodemaneiraamigável CasadoCódigo
bundle.setCacheSeconds(1);
return bundle;
}
Percebaqueindicamosalocalizaçãodoarquivobasedemensagens.Mais
paraafrente,vamosvoltarautilizá-loparafazernossaaplicaç ãosuportarvá-
riosidiomas. Ummétodointeressanteéo setCacheSeconds. Eleserve
paraindicarqueoarquivodemensagensdeveserrecarregadoacadainter-
valodetempo,nocaso,foiconfiguradoapenasumsegundo.Essaéumacon-
figuraçãotípicadeambientededesenvolvimento,jáquenãoqueremosficar
parandoesubindooservidoracadaalteraç ãodessearquivo.
Umdetalhemuitoimportante,masnãomuitoclaro,équeonomedo
métododeveser messageSource. OSpringMVCvaiprocurarporum
Beanregistradocomessenome,paraquepossacarregarasmensagens.Uma
alternativa,paranãoterquesepreocuparcomonomedométodo,éutilizar
oatributo namedaannotation @Bean.
@Bean(name="messageSource")
public MessageSource loadBundle(){
...
}
Naopiniãodesteautornãoexisteummelhorqueooutro.Atéporquevocê
nãoficaalterandoonomedosmétodosdeconfiguraç ão. Nãopercatempo
comisso,apenasfaçaaconfiguraçãonecessáriaparaquevocêpossacontinuar
odesenvolvimentodadaaplicação.
Agora,finalmente,estamosprontosparaexibirasmensagensdentroda
nossapágina.
<spring:hasBindErrors name="product">
<ul>
<c:forEach var= "error" items="${errors.allErrors}">
<li><spring:message code="${error.code}"
text="${error.defaultMessage}"/></li>
</c:forEach>
</ul>
</spring:hasBindErrors>
74

## Página 82

CasadoCódigo Capítulo5. Validaçãoeconversãodedados
Atag message,comomostramos,serveparabuscarasmensagensasso-
ciadasàschaves.Oatributo textnosajudaadeixarumamensagempadrão
ondeaschavesaindanãoestiveremconfiguradasnoarquivo.
Alterando a mensagem de conversão
Voltandoumpoucoparaosproblemasdevalidaç ão,umoutroerroque
podeexistirnoformuláriodecadastroéaentradadeumvalornãocondi-
zentecomotipodocampo.Porexemplo,umusuáriopodedigitar“dez”em
vezde“10”nocampodenúmerodepáginas.Essetipodesituaçãotambém
acontece,emgeral,comcamposdedatas.Paraexibirmensagensamigáveis,
relativasaoserrosdeconversão,adicionamosaschavesquecome çamcom
typeMismatch.
field.required = Campo obrigatorio
field.required.product.title = Titulo obrigatorio
typeMismatch.product.pages = Digite um número, exemplo "100"
typeMismatch.java.lang.Integer = Digite apenas números
typeMismatch.int = Digite apenas numeros
typeMismatch = O tipo esta errado
Percebaqueadicionamosasmensagensparaproblemasdeconversãode
tiposinteirosnogeraleaindaindicamosumamaisespecíficaparaoatributo
pages.
Posicionamento da mensagem de erro
Asmensagensdeerrosestãosendoexibidasnoiníciodanossatela,mas
nãoéincomumqueoclienterequisitequeamesmamensagemsejaexibida
aoladodocampo.Eéjustamenteoquevamosfazeragora.
<spring:hasBindErrors name="product">
...
<form action= "${spring:mvcUrl("PC#save").build()}"
method="post">
75

## Página 83

5.3. Exibindoasmensagensdeerrodemaneiraamigável CasadoCódigo
<div>
<label for="title">Titulo</label>
<input type="text" name="title"
id="title" />
<c:forEach var="error"
items="${errors.getFieldErrors('title')}">
<span>
<spring:message code="${error.code}"
text="${error.defaultMessage}"/>
</span>
</c:forEach>
</div>
</form>
</spring:hasBindErrors>
Fizemosumapequenamodificaçãoedeixamosoformuláriointeiroden-
trodatag hasBinderrors. Comessaalteração,podemosusaravariá-
vel errorsdoladodecadacampodeleenestecasofoiusadoométodo
getFieldErrorsparapegaroerrodecadaatributo.
Oúnicoproblemadessecódigoéqueeleprovavelmenteseránecessário
emváriaspáginasdonossosistema. Paranãotermosqueficarcopiandoe
colandoessecódigo,vamosutilizarumaoutratagprovidapeloSpringMVC.
<%@ taglib prefix= "spring"
uri="http://www.springframework.org/tags"%>
<%@ taglib prefix= "form"
uri="http://www.springframework.org/tags/form"%>
<form:form action="${spring:mvcUrl("PC#save").build()"
method="post"
commandName="product">
<div>
<label for="title">Titulo</label>
<input type="text" name="title" id="title"/>
<form:errors path="title"/>
</div>
76

## Página 84

CasadoCódigo Capítulo5. Validaçãoeconversãodedados
</form:form>
Ocódigoficoumuitomaislegível! Atag errorsfazpraticamenteo
mesmopapeldonossocódigoanterior.Elavaiexibirtodososerrosdoatri-
butoemquestão.Elaaindapossuialgunsatributosparaquevocêpossadefi-
nir,entreoutrascoisas,oestiloeatagHTMLquevaiserutilizadapararen-
derizaroserros.Paraqueatag errorsfuncione,énecessárioqueelaseja
usadadentrodatag form.
<form:form action="${spring:mvcUrl("PC#save").build()"
method="post"
commandName="product">
...
<form:errors path="title"/>
</form:form>
O ponto que precisa de mais atenção na tag form é o atributo
commandName. Ele tem o mesmo propósito do atributoname na tag
hasBindErrors,ouseja,recebeotipodoparâmetroqueestásendovali-
dadopelonossocontroller,comaprimeiraletraemminúsculo.Apenaspara
refrescaramemória:
save(@Valid Product product....)
Umúltimodetalhe,foinecessárioimportarmaisumconjuntodetags
paraanossapágina.
<%@ taglib uri="http://www.springframework.org/tags/form"
prefix="form"%>
Esseconjuntopossuitagsquenosajudamaescreverumformulárioem
si.Seguemalgunsexemplos:
• checkbox
• select
• hidden
77

## Página 85

5.4. Mantendoosvaloresnoformulário CasadoCódigo
• form
Napróximase çãojávamosfazerumpoucomaisdeusodessastags.
5.4 M antendo os v alores no formulário
Paracompletarnossoformulário,precisamosdarapossibilidadedeousuário
continuaropreenchimentodeondeeleparou. Atualmente,casoaconte ça
algumerrodevalidação,voltamosparaamesmatela,masnãomantemosas
informaçõespreviamentepreenchidas.VamosvercomooSpringMVCpode
nosajudar.
<form:form action="${spring:mvcUrl("PC#save").build()"
method="post" commandName="product">
<div>
<label for="title">Titulo</label>
<form:input path="title"/>
<form:errors path="title"/>
</div>
<div>
<label for="description">Descrição</label>
<form:textarea path="description" rows="10"
cols="20" />
</div>
...
<div>
<label for="releaseDate">Data de lançamento</label>
<form:input path="releaseDate" type= "date"/>
<form:errors path="releaseDate"/>
</div>
</form:form>
Fizemosusodaqueleconjuntodetagsespecíficasparaoformulário.Além
da errors,usamosa inputea textarea. Percebaquetodastêmo
atributo path, quedefineapropriedadedomodeloquequeremosusar.
Valelembrarquenãoestamosnosreferindoaoatributoprivadoesimaos
gettersexpostosnaclasse. Basicamente,oqueessastagsfazeméacessar
78

## Página 86

CasadoCódigo Capítulo5. Validaçãoeconversãodedados
avariávelcomomesmonomedo commandName,eirinvocandoosgetters
necessários.
O método form e o atributo commandName
Casooleitormaiscuriosotenhaexecutadoocódigocomastagsdeajuda
doformulário,nestemomento,eleterárecebidoumaexceptionumtanto
quantoestranha.
java.lang.IllegalStateException: Neither BindingResult nor
plain target object for bean name 'product' available as
request attribute
Quandoacessamosateladoformuláriopelaprimeiravez, atravésda
URL /produtos/form, fazemos uso do métodoform(), da classe
ProductsController. Jáfoiexplicadoque,paraatag form:formfun-
cionar,elaprecisadeacessoaoobjetorecebidocomoparâmetro. Nocaso
dessenossométodo,ondeestáoparâmetro? Éjustamenteporessemotivo
queestamosrecebendoessaexception.
Paraconseguirmoscontornarisso,vamosfazerumalevealteraç ão.
public ModelAndView form(Product product) {
...
}
Forçamosométodo formareceberumparâmetrodotipo Product,
apenasparaoSpringMVCdisponibilizá-locomovariáveldorequest.Caso
vocêestejapensandoqueessaalteraçãoestásendoimpostapeloframework,
váseacostumando.Muitasvezestemosqueescreverumcódigoquenãoque-
remosapenasparaagradaratecnologiaemquestão,masdadoquejáganha-
mosbastante,éumtradeoffmaisdoquejusto. Agora,paranossocódigo
voltaracompilar,énecessárioalterarainvocaçãodométodo formapartir
dométodo save.
public ModelAndView cadastra(@Valid Product product...){
if(bindingResult.hasErrors()){
return form(product);
}
}
79

## Página 87

5.5. IntegraçãocomaBeanValidation CasadoCódigo
A annotation @ModelAttribute
Estamos sempre configurando o atributocommandName com o
mesmonomedotipodoparâmetrorecebidonométodo. Casovocê
queiraalterarisso,porexemplopassandoovalor“objetoAtual”,podeuti-
lizaraannotation @ModelAttribute.
save(@Valid @ModelAttribute("objetoAtual") Product product)
Essaannotationpodeserútilcaso,poralgummotivo,suaempresa
tenhaumapadrãoparanomesdevariáveisdisponíveisnasuaJSP.
5.5 I ntegração com a Bean Validation
Anossavalidaçãojáfuncionaintegralmente,masaindatemumpontoque,
pelomenosparaesteautor,aindaéumpoucoruim.Onossovalidadorcus-
tomizadorealizaverificaçõesmuitobásicas.
ValidationUtils.rejectIfEmptyOrWhitespace(errors,
"title", "field.required");
Essetipodevalidaçãoétãocomumque,comojácomentamos,virouaté
especificaçãonomundoJava,a Bean Validation. Ecomonãopodiaserdi-
ferente,omódulodevalidaçãoécompletamenteintegradocomela.Sópara
lembraroleitor,jáconfiguramosoMavenparautilizarmosaimplementaç ão
feitapelotimedoHibernate,chamadade Hibernate Validator. Oprimeiro
passo,paraafelicidadedequalquerequipedeprogramaç ão,équenãopre-
cisamosdonossovalidadorcustomizado. Logo,lembredeapagá-lodoseu
código,oupelomenosnãoconfiguremaisparaeleserutilizadopeloSpring
MVC.
//por enquanto não precisamos mais desse metodo.
//Comente ou apague.
@InitBinder
protected void initBinder(WebDataBinder binder) {
binder.setValidator(new ProdutoValidator());
}
80

## Página 88

CasadoCódigo Capítulo5. Validaçãoeconversãodedados
AgoraprecisamosdeoutraformaparaensinaroSpringMVCqueelepre-
cisavalidarosdadosbásicosdeumlivro.
@Entity
public class Product {
@Id
@GeneratedValue(strategy = GenerationType.IDENTITY)
private Integer id;
@NotBlank
private String title;
@Lob
@NotBlank
private String description;
@Min(30)
private int pages ;
Pronto,comalgumasannotationsconseguimosomesmoefeitodevali-
dação. Agora,casovocêtesteumnovocadastroinválido,asmensagensde
validaçãoaindanãoestarãodamaneiracomoesperamos.
• @NotBlank->“maynotbeempty”
• @Min->“mustbegreaterthanorequalto?”
Comojáfizemosantes,vamosalteraroarquivo message.properties
eadicionarasnovaschavesdevalidaç ão.
NotBlank.java.lang.String = Campo obrigatorio
NotBlank.product.title = Titulo obrigatório
Min.product.pages = O numero minimo de paginas é {1}
Percebaquesimplesmenteadicionamosonomedaannotationnafrente
dachave,orestosegueomesmopadrãoquejáutilizamos. Umpontoaser
observadoéamensagemreferenteaomínimodepáginas.Temosqueusaro
valordoargumentoquefoiconfiguradonaannotation.
@Min(30)
private int pages;
81

## Página 89

5.6. Convertendoadata CasadoCódigo
OSpringMVCdisponibilizaissocomoparâmetrodasuamensagem.No
casodamensagemdevalidação,oargumento {0}sempreéonomedoatri-
butosendovalidado.Porisso,foiusadoo {1}.Casovocêqueiraalteraras
mensagenspadrões,queestãoassociadasacadaumadasannotationsdaBean
Validation,sigaestelink: http://tinyurl.com/oocl5ro.
...
org.hibernate.validator.constraints.NotBlank.message =
may not be empty
Elevailheforneceraschavesnecessárias,quedevemsersubstituídas,para
queoHibernateValidatortrabalhecomasmensagenscustomizadas. Basta
quevocêcopienoseuarquivo messagesetroqueovalorassociadoaela.
...
org.hibernate.validator.constraints.NotBlank.message =
Campo obrigatório
5.6 C onvertendo a data
NaCasadoCódigo,muitoslivrossãoescritosotempotodo.Paraterumfluxo
interessantedelançamentos,foidecididoqueoslivroscadastradosdevemter
umadatadelan çamento.
@Entity
public class Product {
...
private Calendar releaseDate;
//getter e setter.
}
Agoraprecisamoscolocarumcamponovononossoformulário.
<div>
<label for="releaseDate">Data de lançamento</label>
<input type="date" name="releaseDate" />
<form:errors path="releaseDate"/>
</div>
82

## Página 90

CasadoCódigo Capítulo5. Validaçãoeconversãodedados
Casonossousuárioefetueoteste,apareceráumamensagemdefalhade
conversão.
Failed to convert property value of type java.lang.String to
required type java.util.Calendar for property releaseDate;
nested exception is java.lang.IllegalStateException: Cannot
convert value of type [java.lang.String] to required type
[java.util.Calendar] for property releaseDate: no matching
editors or conversion strategy found
AexceptionindicaqueoSpringMVCnãoconseguiuachar,demaneira
automática,umconversordeStringparaotipo Calendar. Paraqueeste
problemasejaresolvido,énecessáriousarmosumaannotationindicandoque
queremosaconversão.
@DateTimeFormat
private Calendar releaseDate;
Agora,setentarmosmaisumavezocadastro,receberemosaseguinte
exceptiondeconversão:
Failed to convert property value of type java.lang.String to
required type java.util.Calendar for property releaseDate;
nested exception is
org.springframework.core.convert.ConversionFailedException:
Failed to convert from type java.lang.String to type
@org.springframework.format.annotation.DateTimeFormat
java.util.Calendar for value 2015-02-20; nested exception is
java.lang.IllegalArgumentException: Unable to parse 2015-02-20
O problema é que o formato default usado pelo conversor re-
gistrado no Spring MVC é oM/d/yy, representado pela constante
DateFormat.SHORT;eovalorenviadopelonossoformulário,jáqueusa-
mosoinputcujotipoéo date,semprevainoformato yyyy-MM-dd.Paraa
nossasorte,esseformatoéomuitousadonomundo http://pt.wikipedia.org/
wiki/ISO_8601eoSpringMVCjátemosuportepronto.
@DateTimeFormat(iso=ISO.DATE)
private Calendar releaseDate;
83

## Página 91

5.6. Convertendoadata CasadoCódigo
Redefinindo o formato global
Semprequetemosdelembrardefazeralgumaconfiguraç ãononossocó-
digo,porváriosmotivos,acabamosesquecendoepassandomuitotempoten-
tandocorrigir.Éjustamenteoquepodeacontecercomanossaestratégiade
conversãoatual.Sempretemosquenoslembrardepôroestilodeconversão
naannotation @DateTimeFormat.
Paramelhoraressapartedanossaaplicaç ão,vamosensinaraoSpring
MVCqueelesempredeveusaressaformataç ão. Vamosadicionarmaisum
métodonaclasse AppWebConfiguration.
@Bean
public FormattingConversionService mvcConversionService() {
DefaultFormattingConversionService conversionService =
new DefaultFormattingConversionService(true);
DateFormatterRegistrar registrar =
new DateFormatterRegistrar();
registrar.setFormatter(new DateFormatter("yyyy-MM-dd" ));
registrar.registerFormatters(conversionService);
return conversionService;
}
Respire,poisestáacontecendomuitacoisanessecódigo.Aprimeirain-
formaçãoéqueonomedométodo temqueser mvcConversionService.
PoisesseéonomeusadointernamentepeloSpringMVCpararegistraroob-
jetoresponsávelporagruparosconversores. Paraqueissonãopare çatão
mágico,oleitorpodechecaraclasse WebMvcConfigurationSupport,di-
retamentenocódigo-fontedoSpring, http://tinyurl.com/na3g9jp.
O próximo passo importante é o uso do objeto do tipo
DateFormatterRegistrar. Ele implementa a interface
FormatterRegistrar,quedeveserusadaquandoénecessárioagrupar
váriostiposdeconversões. Nocasodadata,temosváriaspossibilidades,
seguemalgunsexemplos.
• CalendarparaLong
• LongparaCalendar
84

## Página 92

CasadoCódigo Capítulo5. Validaçãoeconversãodedados
• DateparaCalendar
• CalendarparaDate
Depoisdecriarmosoobjetodotipo DateFormatterRegistrar,in-
formamosqualaformataçãoquedeveseraplicadaporpadrão.
registrar.setFormatter(new DateFormatter("yyyy-MM-dd"));
Porfim, éfeitooregistrodetodososconversoresnoobjetodotipo
FormattingConversionService.Omesmoéinstanciadocomum true
noconstrutor,indicandoquetodosconversorespadrões,devemseradicio-
nados.
Entendendo mais sobre os formatadores do Spring MVC
UmadasbelezasdosformatadoresdoSpringMVCéqueanossaconfi-
guraçãodeformataçãodasdatasvaleparaosdoisladosdamoeda.
• AStringdeentradaéconvertidaparaoCalendardoseumodelo.
• OCalendardoseumodeloéformatadoparaserapresentadonofor-
mulário.
Paraficarmaisclaro,dêumaolhadanainterfacequedefineosformata-
dores.
public interface Formatter<T> extends Printer<T>, Parser<T> {
}
AstagsdoSpringMVCtiramproveitodosformatadores,comissonão
precisamosficarnospreocupandoemtratarosdadosquedevemserexibidos
nosinputsdosformulários.
<div>
<label for="releaseDate">Data de lançamento</label>
<form:input path="releaseDate" type="date"/>
<form:errors path="releaseDate"/>
</div>
Percebaquesóindicamosonomedapropriedadequedeveserusadae,
pelotipodamesma,oSpringMVCvaidecidirqualformatadorutilizar.
85

## Página 93

5.7. Conclusão CasadoCódigo
5.7 C onclusão
Conseguimoscobrirtudoqueénecessárioparavocêaplicarasvalidações
necessáriasnossistemasqueserãodesenvolvidos. Passamospelafaseonde
vocêmesmopoderiacriaroseuvalidadorevimoscomolidarcomoerrode
validaçãoredirecionandoousuárioparaolocalcorreto.Tambémanalisamos
aspossibilidadesdeconfiguraçãodasmensagensdeerrosecomoexibiras
mesmasdentrodaspáginas.
Parafechar,fomosalémevimosaintegraçãocomasannotationsdaBean-
Validatoneentendemoscomofuncionamosconversoresdetiposdentrodo
SpringMVC.Minhadica,nessemomento,équevocêdescanseumpouco,
tentepraticaroquevimosatéaquiesódepoiscontinuealeitura.
86

## Página 94

Capítulo6
Uploaddearquivos
Umacaracterísticaimportantedaslivrariasonlineéadisponibilizaçãodosu-
máriodoslivrosqueestãoàvenda. ACasadoCódigo,comonãopoderia
deixardeser,tambémdeveofereceressapossibilidadeaseususuários.
6.1 R ecebendo o arquivo no Controller
VamoscomeçaralterandoapáginadaCasadoCódigoresponsávelpelaen-
tradadedadosdecadaumdosnovoslivros.
<form:form action="${spring:mvcUrl('PC#save').build()}"
method="post"
commandName="product">
...

## Página 95

6.1. RecebendooarquivonoController CasadoCódigo
<div>
<label for="summary">Sumario do livro</label>
<input type="file" name="summary"/>
<form:errors path="summaryPath"/>
</div>
...
Aúnicamudan çafoiaadiçãodoinputquevaireceberoarquivoque,
nestecaso,deveserdotipo file.Agora,setentarmosenviarosdadosdesse
formulário,devemosreceberoseguinteresultado:
Fig.6.1:Orequestnãoémultipart
“The current request is not a multipart request
signifcaquetentamosenviaroarquivodeumamaneiraqueoSpring
MVC não consegue entender. Basicamente, o que acontece é que todos
osdadosdoformuláriosãoenviadosdealgumaformae,odefaultéque
elessejamsubmetidosusandooformato application/x-www-form-
urlencoded. Dessemodo,osdadossãoenviadosseguindoquasequeas
mesmasregrasutilizadasquandoutilizamosométodo GET.Umasequência
dechavesevalores.
Anossasituaçãoatualexigequefaç amosumaalteraçãonesseformato,
demodoqueoarquivopossaserintegralmentepassadodonavegadorparao
servidor.Éporissoquevamosutilizaroformato multipart/form-data.
88

## Página 96

CasadoCódigo Capítulo6. Uploaddearquivos
<form:form action="${spring:mvcUrl('PC#save').build()}"
method="post"
commandName="product"
enctype="multipart/form-data">
...
</form>
Oatributo enctypeservejustamenteparaindicarmoscomoqueremos
mandarosdadosdonavegadorparaoservidoreo multipart/form-data
éojeitoutilizadoquandonecessitamostransmitirarquivos.Porexemplo,já
existeumtrabalhosendofeitoparaqueoseu formpossaenviarosdados
atravésdoformato JSON.Casofiquecurioso,navegueaté http://www.w3.
org/TR/html-json-forms/.
Alterando o método do controller
Agora que nosso formulário já envia o arquivo, precisamos
recebê-lo e lidar com ele. Faremos isso no métodosave da classe
ProductsController.
public class ProductsController {
@RequestMapping(method=RequestMethod.POST)
public ModelAndView save(
Part summary, @Valid Product product,...) {
System.out.println(summary.getName() + ";"
+summary.getHeader("content-disposition"));
//resto do código
}
}
Aparteimportantedessecódigoéoparâmetrodotipo Part. Elefoi
introduzidoapartirdaversão3daespecificaç ãodeServletseainterfaceres-
ponsávelporrepresentaroarquivoquefoienviadopeloformulário.Perceba
queonomedoargumentoéomesmonomedoinputquedeclaramosnofor-
mulário.Aquiusamosdoismétodos:
•getName():retornaonomedoinputusadonoformulário;
89

## Página 97

6.1. RecebendooarquivonoController CasadoCódigo
•getHeader():usadopararecuperaralgumainformaçãosobreoque
foienviado.
Ecasoagentequeirarecuperaronomedoarquivo,comovamosfazer?
Oleitormaisexperientedeveestarpensandoquetemalgummétodoquejá
retornaissoprontoeesseéjustamenteoproblema. Ainterface Partéa
maneiramaisprimitivadetratarmososdadosenviadosatravésdo enctype
multipart/form- data. Naverdade,podemosacessarovalordecada
umdoscamposdoformulário,bastaquedeclaremosumparâmetrodotipo
Partparacadainput. Paraficarumpoucomaisclaro,dêumaolhadana
maneiracomoessesdadossãoenviadosapartirdonavegador.
Fig.6.2:Corpodorequestparaumarequisiç ãomultipart
Paraoscamposquenãorepresentamarquivos,oSpringMVCjánosajuda
bastanteefazaligaçãodiretacomaspropriedadesdonossomodelo. Para
nãonosdecepcionar,eletambémofereceumjeitomaisfácildelidarcomo
arquivoquefoisubmetido.
public class ProductsController {
@RequestMapping(method=RequestMethod.POST)
public ModelAndView save(MultipartFile summary,
@Valid Product product,...) {
90

## Página 98

CasadoCódigo Capítulo6. Uploaddearquivos
System.out.println(summary.getName() + ";"
+summary.getOriginalFilename());
//resto do código
}
}
Ométodo getNamecontinuafazendoamesmacoisa,sóqueagorajá
temosoutrométodo,o getOriginalFilename(),quejánosretornao
nomedoarquivoquefoienviado.
6.2 S alv ando o caminho do arquivo
Agoraquejátemosoobjetoquerepresentaoarquivoenviadoemnossas
mãos,énecessáriogravá-loemalgumlugar.
public class ProductsController {
@Autowired
private FileSaver fileSaver;
@RequestMapping(method=RequestMethod.POST)
public ModelAndView save(MultipartFile summary,
@Valid Product product,...) {
//faz a validação
String webPath =
fileSaver.write("uploaded-images",summary);
product.setSummaryPath(webPath);
products.save(product);
//fim do método
}
}
@Component
public class FileSaver {
@Autowired
private HttpServletRequest request;
91

## Página 99

6.3. Configuraçõesnecessárias CasadoCódigo
public String write(String baseFolder, MultipartFile file) {
String realPath = request.getServletContext()
.getRealPath("/"+baseFolder);
try {
String path =
realPath+"/"+file.getOriginalFilename();
file.transferTo(new File(path));
return baseFolder+"/"+file.getOriginalFilename();
} catch (IOException e) {
throw new RuntimeException(e);
}
}
}
Dêumarespiradaeolhecomcuidadoparaocódigo. Percebaquenão
fizemosnadademais,apenascriamosoutraclasseresponsávelporgravaro
arquivoemumapastadanossaaplicaç ão.Aideiaénãodeixarqueessecó-
digoatrapalheofluxodométodo save,nonossocontroller. Alémdisso
énecessáriocriaroatributo summaryPathnaclasse Product,juntamente
comoseugetteresetter.
Dessaforma,casosejanecessáriocriarumlinkparaosumário,bastaque
façamosalgoparecidocomoquesegue:
<img src="${product.summaryPath}"/>
6.3 C onfigurações necessárias
Casovocêtenharodadoaaplicação,percebeuquenossouploaddearqui-
vosaindanãoestáfuncionando.Estásendolan çadaumaexceptiondotipo
IllegalArgumentException.
java.lang.IllegalArgumentException: Expected
MultipartHttpServletRequest: is a MultipartResolver configured?
Ainterface MultipartResolveréaquedefineosmétodosnecessá-
riosparaotratamentoinicialdeumrequestcujomododeenvio,também
92

## Página 100

CasadoCódigo Capítulo6. Uploaddearquivos
conhecidocomo contentType,éo multipart/form-data.Precisamos
proverumaimplementaçãodessainterfaceparaqueoSpringMVCpossafa-
zerseutrabalho.Paraisso,bastaqueadicionemosmaisummétodonaclasse
AppWebConfiguration.
@EnableWebMvc
@ComponentScan(basePackageClasses={HomeController.class,
ProductDAO .class,FileSaver.class})
public class AppWebConfiguration {
...
}
@Bean
public MultipartResolver multipartResolver(){
return new StandardServletMultipartResolver();
}
Aquifoiescolhidaaimplementaçãoqueusaorecursodetratamentode
uploadprovidopelaespecificaçãodeServlets.Outraalternativaéusaraim-
plementaçãobaseadanabiblioteca commons-fileupload. Nessecaso,a
classeescolhidaseriaa CommonsMultipartResolver.
Além disso, na annotation@ComponentScan, passamos a classe
FileSavercomoobjetivodequeoSpringvasculheopacoteemqueela
seencontra.
Agora,casooleitortentesalvarumnovolivro,vairecebermaisumaex-
ception.Sóquedestavezelaédiferente,oqueindicaqueresolvemosopro-
blemaanterior.
java.lang.IllegalStateException: Unable to process parts as
no multi-part configuration has been provided
Apartemaisimportantedessaexceptioné: “no multi-part configuration
has been provided
.Quandoconfiguramosotratamentodeupload,podemosdefiniralgu-
mascoisas:
• Localdearmazenamentotemporárioenquantooarquivoestásendo
recebido;
93

## Página 101

6.4. Gravandoosarquivosforadoservidorweb CasadoCódigo
• Tamanhomáximodoarquivo;
• Tamanhomáximodorequestcomoumtodo.
NaespecificaçãodeServlets,essaconfiguraç ãoéfeitaatravésdaclasse
MultipartConfigElement.
//outros imports
import javax.servlet.ServletRegistration.Dynamic;
public class ServletSpringMVC extends
AbstractAnnotationConfigDispatcherServletInitializer {
...
@Override
protected void customizeRegistration( Dynamic registration) {
registration.setMultipartConfig(
new MultipartConfigElement(""));
}
}
Sóparalembrar, aclasse ServletSpringMVCforneceitensbásicos
como:mapeamentodeURLdoservletdoSpringMVCequaisoutrasclasses
deconfiguraçõesdevemsercarregadas.Agora,alémdisso,sobrescrevemoso
métodocustomizeRegistration.Elerecebecomoparâmetroumobjeto
dotipo Dynamic,quenospossibilita,entreoutrascoisas,registraronosso
objetodeconfiguraçãodotipo MultipartConfigElement. Oconstru-
torrecebendoapenasumaStringvaziaindicaqueopróprioservidorwebvai
decidirqualéolocaldearmazenamentotemporáriodosarquivos.
Pronto,agoranossaaplicaçãoestáprontaparareceberqualquertipode
arquivoatravésdosformulários.
6.4 G rav ando os arquivos fora do servidor
web
Nossalógicadeuploadgravaosnovosarquivosemumapastadentrodapró-
priaaplicaçãoweb. Oproblemadessaabordagem,mesmoquandoestamos
94

## Página 102

CasadoCódigo Capítulo6. Uploaddearquivos
emambientededesenvolvimento,équeacadanovaalteraç ãoquetemosno
projetoanossaIDEfor çaum hot deploynoservidor.Emgeral,o hot deploy
destróiaaplicaçãoqueestavanoservidorecriaumanova,fazendocomque
percamososarquivosquejátinhamsidoenviados.
Alémdisso,umfatoqueincomodaodesenvolvedoréperceberqueos
arquivosenviadosnãoficamexatamentedentrodoprojetoqueeleestávisu-
alizando,porexemplo,noEclipseesimnainstalaç ãodoservidorquefoies-
colhida.Parasimplificartudoisso,facilitandoinclusiveoprocessodedeploy
quediscutiremosmaisparaofimdolivro,équepodemosusarumserviço
comoo Amazon S3.Basicamente,aAmazonforneceumservidorondepo-
demosenviarnossosarquivoseelesficamdisponíveisparaseremacessados
pelaweb.Elespossuemservidoresdedicadossóparaisso.
Integração com o Amazon S3
Paraquemestiverinteressadonessaop ção,aprimeiracoisaquedevemos
fazeréalterarocódigoqueestánaclasse FileSaver,queéaresponsável
porgravaroarquivo.
@Component
public class FileSaver {
public String write(String baseFolder,
MultipartFile multipartFile) {
AmazonS3Client s3 = client();
try {
s3.putObject("casadocodigo",
multipartFile.getOriginalFilename(),
multipartFile.getInputStream(),
new ObjectMetadata());
return "https://s3.amazonaws.com/casadocodigo/"
+multipartFile.getOriginalFilename();
} catch (AmazonClientException | IOException e) {
throw new RuntimeException(e);
}
95

## Página 103

6.4. Gravandoosarquivosforadoservidorweb CasadoCódigo
}
private AmazonS3Client client() {
AWSCredentials credentials = new BasicAWSCredentials(
,
);
AmazonS3Client newClient =
new AmazonS3Client(credentials,
new ClientConfiguration());
newClient.setS3ClientOptions(new S3ClientOptions()
.withPathStyleAccess(true));
return newClient;
}
}
Percebaquetemosmaiscódigosrelativosàintegraç ãocomaAmazondo
querelacionadoaoSpringemsi. Detudoquefoiescritoanteriormente,as
linhasmaisimportantessãoasqueestãoaseguir:
AmazonS3Client s3 = client();
...
s3.putObject("casadocodigo",
multipartFile.getOriginalFilename(),
multipartFile.getInputStream(),
new ObjectMetadata());
Oobjetodotipo AmazonS3Clientencapsulatodaalógicaeoproto-
colodecomunicaçãocomaAmazon. Onossoúnicotrabalhoépassaros
parâmetros.
• Oprimeiroéapastaremotaondeoarquivovaisersalvo,tambémco-
nhecidocomo bucket;
• Osegundoéonomedoarquivo;
96

## Página 104

CasadoCódigo Capítulo6. Uploaddearquivos
• Oterceiroéalgumaimplementaçãodaclasse InputStream,quere-
almenterepresentaoarquivo;
• Oquartosãoinformaçõesextrascomo:datadeexpiraçãodoarquivoe
qualqueroutrainformaçãoquesejaespecíficadaaplicação.
Aoutrapartedocódigoéamesmaparaqualquerintegraç ãoquevocêvá
fazercomaAmazon.Sempreprecisamoscriarumobjetoquecontémascre-
denciaisdeacesso,paragarantirquesóodonodacontapossafazeruploads
paraobucket.
private AmazonS3Client client() {
AWSCredentials credentials = new BasicAWSCredentials(
,
);
AmazonS3Client newClient = new AmazonS3Client(credentials,
new ClientConfiguration());
newClient.setS3ClientOptions(new S3ClientOptions()
.withPathStyleAccess(true));
return newClient;
}
Basicamenteessasseriamasalteraçõesqueteríamosquefazernonosso
código. Comodeixamosencapsuladaalógicadegravaç ãodoarquivo,não
somosobrigadosaalterarnenhumalinhadonossocontroller.
Simulando o S3 localmente
Oempecilhocomessasoluçãoéquevamosterquerealmentecriarum
contanaAmazonparaconseguirrealizarnossostestes,oqueécompleta-
menteinviável. Pararesolveresteproblema,existeumprojetochamado S3
Ninja,quepodeserencontradoem http://s3ninja.net/. Elescriamestepro-
jetocomoobjetivodeservircomoumemuladorparaoS3real,daAmazon.O
S3NinjaéumaaplicaçãowebescritaemJavaquesobeumservidorqueaceita
requisiçõesvindasdopróprioSDKdaAmazon.Justamenteoqueestávamos
procurando.Umapartemuitoboaéqueseuusoébemsimples.
Oprimeiropassoérealizarodownloaddo zip. Bastaacessaroende-
reçohttps://oss.sonatype.org/content/groups/public/com/scireum/s3ninja/2.
97

## Página 105

6.4. Gravandoosarquivosforadoservidorweb CasadoCódigo
3/s3ninja-2.3-zip.zip. Vocêtambémpodeencontrarolinkno readmedo
GitHubdoprojetoem https://github.com/livrospringmvc/lojacasadocodigo.
Umavezquevocêbaixouoprojeto,descompacteemumapastadasuaprefe-
rência.Aindadentrodapastadescompactada,precisamoscriarumestrutura
simplesdesubpastasquevãosimularos bucketsdaAmazon. Vamoscriar
primeiroapasta datae,dentrodela,criaremosumaoutra,chamada s3.A
estruturafinalvaificarparecidacomaquesegue.
Fig.6.3:Estruturadepastasdos3ninja
Agoraqueaestruturaestácriada,bastaqueiniciemososervidordoS3
Ninja.
java IPL
Percebaque IPLéjustamenteumarquivo javacompiladoquejávem
naraizdodiretóriodescompactado.Apósexecutarocomando,vocêdevever
aseguintesaída.
I N I T I A L P R O G R A M L O A D
---------------------------------------
IPL from: /Users/alberto/ambiente/servidores/s3ninja-2.3-zip
IPL completed - Loading Sirius as stage2...
Opening port 9191 as shutdown listener
Oservidorestárodandonoendere çohttp://localhost:9444/.Vocêpode
acessá-lopelonavegador.
98

## Página 106

CasadoCódigo Capítulo6. Uploaddearquivos
Fig.6.4:Teladeboas-vindasdos3ninja
Agoraqueonossoemuladorestárodando,precisamosalterarocódigo
deconfiguraçãodeacessoaAmazonefazê-loapontarparaoservidorlocal.
private AmazonS3Client client() {
AWSCredentials credentials = new BasicAWSCredentials(
,
);
AmazonS3Client newClient = new AmazonS3Client(credentials,
new ClientConfiguration());
newClient.setS3ClientOptions(new S3ClientOptions()
.withPathStyleAccess(true));
//nova linha
newClient.setEndpoint("http://localhost:9444/s3");
return newClient;
}
Pronto!Quandocadastrarmosumnovolivro,oarquivodosumáriovai
sergravadonapasta data/s3/casadocodigo/nomedoarquivo,nolocal
quevocêescolheuparaexecutaroS3Ninja.Percebaquetambémalteramos
oretornodométodo write,daclasse FileSaver.
public String write(String baseFolder,
MultipartFile multipartFile) {
AmazonS3Client s3 = client();
99

## Página 107

6.4. Gravandoosarquivosforadoservidorweb CasadoCódigo
try {
s3.putObject("casadocodigo",
multipartFile.getOriginalFilename(),
multipartFile.getInputStream(),
new ObjectMetadata());
//url de acesso ao arquivo
return "https://s3.amazonaws.com/casadocodigo/"
+multipartFile.getOriginalFilename()+"?noAuth=true";
} catch (AmazonClientException | IOException e) {
throw new RuntimeException(e);
}
}
Aideiaéqueénossométodojáretorneoendere çodeacessoaoarquivo
enviado,paraquepossamosusá-lonoslinksdonossosistema.
Isolando a criação do AmazonS3Client
Anossaalteraçãonoslevouadeixarocódigodecriaç ãodoobjetode
acessoàAmazonmisturadocomocódigodaclasse FileSaver.Comojá
discutimosquandorecebemosinjetadooDAO,onossoobjetivonessecódigo
éusaroclientedaAmazonenãoficarcriando. Portanto,vamoscome çar
recebendoumobjetodotipo AmazonS3Client,emvezdecriá-lo.
@Component
public class FileSaver {
@Autowired
private AmazonS3Client s3;
public String write(String baseFolder,
MultipartFile multipartFile) {
try {
s3.putObject("casadocodigo",
multipartFile.getOriginalFilename(),
multipartFile.getInputStream(),
100

## Página 108

CasadoCódigo Capítulo6. Uploaddearquivos
new ObjectMetadata());
return "http://localhost:9444/s3/casadocodigo/"
+multipartFile
.getOriginalFilename()+"?noAuth=true";
} catch (AmazonClientException | IOException e) {
throw new RuntimeException(e);
}
}
}
Paraestecódigofuncionar,precisamoscriarumaclassedeconfiguraç ão
queconstruaoobjetoparanós.
package br.com.casadocodigo.loja.conf;
import org.springframework.context.annotation.Bean;
import com.amazonaws.ClientConfiguration;
import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.services.s3.AmazonS3Client;
import com.amazonaws.services.s3.S3ClientOptions;
public class AmazonConfiguration {
@Bean
public AmazonS3Client s3Ninja() {
AWSCredentials credentials = new BasicAWSCredentials(
,
);
AmazonS3Client newClient =
new AmazonS3Client(credentials,
new ClientConfiguration());
newClient.setS3ClientOptions(new S3ClientOptions()
.withPathStyleAccess(true));
newClient.setEndpoint("http://localhost:9444/s3");
101

## Página 109

6.4. Gravandoosarquivosforadoservidorweb CasadoCódigo
return newClient;
}
}
Percebaqueéumaclassenormal,apenascriamosummétodoeusamos
anotação @Beanparadizerqueeleproduzumobjetoquedevesergerenciado
peloSpring.OúltimopassoéensinaraoSpringqueessaclasseexistee,para
isso,vamosalteraraclasse ServletSpringMVC.
package br.com.casadocodigo.loja.conf;
...
public class ServletSpringMVC extends
AbstractAnnotationConfigDispatcherServletInitializer {
@Override
protected Class<?>[] getRootConfigClasses() {
return new Class[] { SecurityConfiguration.class,
AppWebConfiguration.class,
JPAConfiguration.class,
AmazonConfiguration.class };
}
...
Agoravocêtemduasop çõesparasalvarosarquivosenviadospelosseus
usuários. Esteautorsugerequevocêsempreguardeoarquivoemumlocal
foradoservidorweb.Acomplexidadeadicionadaaoprojetoécompensada
pelaflexibilidadedemanterosarquivosentrereloadsdaaplicaç ão,emtempo
dedesenvolvimento.Alémdisso,ainstalaçãonoambientedeproduçãovaiser
facilitada,jáquevocênãovaiterquesepreocuparemmanterosarquivosque
játenhamsidoenviadospelosusuários.Tudovaiestaremumlugarseparado.
102

## Página 110

CasadoCódigo Capítulo6. Uploaddearquivos
6.5 C onclusão
Nestecapítulo,focamosunicamentenouploaddearquivos.Essaéumafun-
cionalidademuitocomumnasaplicações,masmuitasvezesesquecemosde
olharcomdetalhes,paraentenderexatamentecomofunciona. Esperoque
estecapítulotenhaajudadoadeixarasconfiguraçõesumpoucomaisclaras
paravocê.
Nãopareagora,jáváparaopróximocapítuloondevamossimularofe-
chamentodeumacompraeaintegraç ãocomumoutrosistema. Também
vamosvercomopodemosajudaroservidoraprocessarrequestsmaislon-
gos.
103

## Página 112

Capítulo7
Carrinhodecompras
JátemosocadastrodelivrosealistagemdosmesmosnalojadaCasadoCó-
digo,chegouomomentodeimplementarmosoprocessodecompra.Paraco-
meçarmosessafase,precisamos,primeiramente,possibilitarqueosusuários
escolhamoslivrosquemaislhesinteressameoscoloquememumcarrinho
decompras.
7 .1 URI templates
VamostentarseguirexatamenteomesmoprocessousadonositedaCasa
doCódigo.Porlá,paraovisitantedositecolocarumlivronocarrinho,ele
precisanavegaratéapáginadedetalhesdolivro.

## Página 113

7.1. URItemplates CasadoCódigo
Fig.7.1:Páginadedetalhesdolivro
Para seguir a mesma ideia, vamos criar a nossa página de detalhes
do livro. Aqui, para ficar ainda mais claro que estamos literalmente re-
produzindoaaplicação,seráusadoomesmoHTMLdaCasadoCódigo.
Como o código da página é relativamente grande, o leitor pode nave-
gar até o linkhttps://github.com/livrospringmvc/lojacasadocodigo/blob/
master/src/main/webapp/WEB-INF/views/products/show.jsp
paraverapáginacompleta.Notrechoaseguir,veja
algumaspartesimportantes.
<header id="product-highlight" class="clearfix">
<div id="product-overview" class="container">
<img itemprop="image" width="280px" height="395px"
src=''
class="product-featured-image"
alt="${product.title}">
<h1 class="product-title" itemprop="name">
${product.title}
</h1>
<p class="product-author">
<span class="product-author-link">
${product.title}
106

## Página 114

CasadoCódigo Capítulo7. Carrinhodecompras
</span>
</p>
<p itemprop="description" class="book-description">
${product.description}
Veja o <a
href="<c:url value='/${product.summaryPath}'/>"
target="_blank">sum&#225;rio</a> completo do
livro!
</p>
</div>
</header>
<section class="buy-options clearfix">
<form action= "<c:url value="/shopping"/>" method="post"
class="container">
<input type="hidden" value="${product.id}"
name="productId"/>
<ul id="variants" class="clearfix">
<c:forEach items="${product.prices}" var="price">
<li class="buy-option">
<input type="radio"
name="bookType" class="variant-radio"
id="${product.id}-${price.bookType}"
value="${price.bookType}"
${price.bookType.name()=='COMBO'?'checked':''
}>
<label class="variant-label"
for="${product.id}-${price.bookType}">
${price.bookType}
</label>
<p class="variant-price">${price.value}</p>
</li>
</c:forEach>
</ul>
<input type="submit" class="submit-image icon-basket-alt"
107

## Página 115

7.1. URItemplates CasadoCódigo
alt="Compre agora"
title="Compre agora '${product.title}'!"
value="comprar"/>
</form>
</section>
Apenasparavocênãoficarperdido,onomedessearquivoé show.jsp
eficanapasta WEB-INF/views/products.
Percebaquesimplesmenteusamosasinformaçõesquejápossuíamosso-
breumdeterminadoproduto.Oúnicopontoparaoqualaindanãofizemos
osuporteéparaaURL /shopping,cujocontrollervaiserresponsávelpor
adicionaroprodutonocarrinhodecompras. Aindanãosepreocupecom
ela,vamosresolverissonomomentocorreto.Umoutrodetalhecomquenão
nospreocupamosfoioderecuperarosarquivosdeestilosusadospelaCasa
doCódigo,estamosapenasreaproveitandoaestruturadoHTML.
Agoraquejátemosapágina,énecessárioconstruirométododocontrol-
lerquecarregaoproduto.Faremosissonaclasse ProductsController.
@RequestMapping(method=RequestMethod.GET,value="/show")
public ModelAndView show(Integer id){
ModelAndView modelAndView =
new ModelAndView("products/show");
Product product = productDAO.find(id);
modelAndView.addObject("product", product);
return modelAndView;
}
Precisamostambémadicionarumlinknalistagemdeprodutos,paraque
osusuáriospossamfazeranavegaçãopelanossaaplicação.
...
<c:forEach items="${products}" var="product">
<tr>
<td>
<a
href="${spring:mvcUrl('PC#show').arg(0,product.id)
.build()}">
108

## Página 116

CasadoCódigo Capítulo7. Carrinhodecompras
${product.title}
</a>
</td>
<td>
<c:forEach items="${product.prices}" var="price">
[${price.value} - ${price.bookType}]
</c:forEach>
</td>
</tr>
</c:forEach>
...
Maisumavezfizemosusodafun ção mvcUrl,paraqueelanosajudea
montaraURL.Aúnicadiferen çaéque,antesdeinvocarométodo build(),
tivemosquechamaro arg(indice,valor)paraqueoendere çopossaser
montadoutilizandocorretamenteosparâmetros.
Oendereçoqueaparece,apósousuárioclicarnolinkquelevaparaapá-
ginadedetalhedoproduto,éo casadocodigo/produtos/show?id=2.
Naverdade,essaéamaneirapadrãodepassarparâmetrosviagetsóque,se
olharmosparaomesmoendere çonositedaCasadoCódigo,veremosqueele
possuiumaestruturaumpoucodiferente, http://www.casadocodigo.com.br/
products/livro-apis-java.
Otrecho livro-apis-java,funcionabasicamentecomoumidden-
trodosistemadaCasadoCódigo. Aocontráriodanossaimplementaç ão,
esseparâmetrovaicomopartedaprópriaURL,técnicaconhecidacomo URI
T emplate.
Equalomotivodepassarmosoparâmetrodeumamaneiradiferente?
Osmotoresdebusca,tipooGoogle,preferemendere çosque,seacessados,
sempreretornemomesmoresultado. Eestaéadiferen ça:quandousamos
a ?estamosdizendoquebastaumamudan çanovalordoparâmetroqueo
resultadodapáginamudae,quandousamosoparâmetrocomopartedaURI,
issopassaaideiadequeaqueleéumendere çofixo.
Émuitosimplesaplicarmosessamudan çanonossoprojeto.
@RequestMapping("/{id}")
public ModelAndView show(@PathVariable("id") Integer id){
109

## Página 117

7.1. URItemplates CasadoCódigo
ModelAndView modelAndView =
new ModelAndView("products/show");
Product product = products.find(id);
modelAndView.addObject("product", product);
return modelAndView;
}
Usamos a notação {nomeDoParametro} para montar a URL com
argumentos misturados. Além disso, temos que usar a annotation
PathVariableparaindicaroparâmetrodonossométodoquedeveserpo-
puladocomarespectivapartedaURL.Casotivéssemosagrupadooslivros
porcategorias,poderíamosteralgoparecidocomoquesegue.
//apenas um exemplo
@RequestMapping("/{categoryId}/{productId}")
public ModelAndView show(@PathVariable ("categoryId")
Integer categoryId, @PathVariable("productId") Integer id){
ModelAndView modelAndView =
new ModelAndView("products/show");
Product product = products.find(id);
modelAndView.addObject("product", product);
return modelAndView;
}
UmdetalheimportanteéqueosparâmetrosdeURLsópodemserasso-
ciadoscomtiposconsideradosmaissimples,porexemplo:
• tiposprimitivos
• String
• Date
• Calendar
110

## Página 118

CasadoCódigo Capítulo7. Carrinhodecompras
7 .2 C arrinho de compras e o escopo de Sessão
Agora,quejáconseguimosnavegarparaapáginadedetalhedolivro,pode-
moscomeçaraimplementarafuncionalidadedeadicioná-losaocarrinhode
compras.VamosapenasrelembrarotrechodaJSPresponsávelporisso.
<section class="buy-options clearfix">
<form action= "<c:url value="/shopping"/>" method="post"
class="container">
<input type="hidden" value="${product.id}"
name="productId"/>
<ul id="variants" class="clearfix">
<c:forEach items="${product.prices}" var="price">
<li class="buy-option">
<input type="radio"
name="bookType" class="variant-radio"
id="${product.id}-${price.bookType}"
value="${price.bookType}"
${price.bookType.name()=='COMBO'?'checked':''
}>
<label class="variant-label"
for="${product.id}-${price.bookType}">
${price.bookType}
</label>
<p class="variant-price">${price.value}</p>
</li>
</c:forEach>
</ul>
<input type="submit" class="submit-image icon-basket-alt"
alt="Compre agora"
title="Compre agora '${product.title}'!"
value="comprar"/>
</form>
</section>
A URL que deve ser acessada é a/shopping e, além do ID do
produto, precisamos saber qual o tipo de livro que o usuário pretende
111

## Página 119

7.2. CarrinhodecompraseoescopodeSessão CasadoCódigo
comprar. Para isolar essa lógica, vamos criar um novo controller, o
ShoppingCartController.
@Controller
@RequestMapping("/shopping")
public class ShoppingCartController {
@Autowired
private ProductDAO productDAO;
@Autowired
private ShoppingCart shoppingCart;
@RequestMapping(method=RequestMethod.POST
public ModelAndView add(Integer productId,BookType bookType){
ShoppingItem item = createItem(productId , bookType);
shoppingCart.add(item);
return new ModelAndView("redirect:/produtos");
}
private ShoppingItem createItem(Integer productId,
BookType bookType) {
Product product = productDAO.find(productId);
ShoppingItem item = new ShoppingItem(product,bookType);
return item;
}
Aquinãotemnenhumcódigoquevocêjánãotenhavistonolivro:um
controllernormal,recebendosuasdependênciasinjetadaseosmétodosque
tratamasrequisiçõesdosusuários.Asclassesnovassãoasquerepresentam
ocarrinhodecompras,nocasoa ShoppingCartea ShoppingItem,que
representaolivrosendoadicionadonocarrinho. Nãovamosperdertempo
dissecandoalógicadessasclasses,vamosficaratentosapenasàspartesque
estejamligadasaoSpring.Casoqueiraconferirocódigocompletodelas,basta
acessaroendere çohttp://tinyurl.com/pajz3dh.
ÉnecessárioavisaroSpringdequequeremosinjetarumobjetodotipo
ShoppingCartemoutrosobjetosdonossocódigo.
@Component
public class ShoppingCart {
112

## Página 120

CasadoCódigo Capítulo7. Carrinhodecompras
....
}
Bastaadicionaraannotation @Componente,alémdisso,precisamosalte-
raraclasse AppWebConfigurationepedirqueopacotedessaclassepasse
aserescaneado.
@EnableWebMvc
@ComponentScan(basePackageClasses={HomeController.class,
ProductDAO.class,FileSaver.class,ShoppingCart.class})
public class AppWebConfiguration {
...
}
Adicionando produtos no carrinho
Jápodemoscomeçaraadicionarositensdentrodonossocarrinhoe,por
sinal,tudopareceestarcorrendobem.Ovalorqueestásendoimpressoden-
trodonossocontrollercresceacadanovolivroqueéadicionado.Agoraserá
feitoumteste,vamosabrirumanovapáginadoseunavegadorusandoofa-
moso Private Browsing.Dessamaneiraonavegadornãosalvanemreaproveita
nenhumainformaçãoquejáexistiapreviamente.
• NoChrome,pressioneCtrl + Shift + N
• NoFirefox,pressioneCtrl + Shift + P
Agoratenteadicionarmaisumlivroaocarrinhoeconfiraovalorim-
presso.Provavelmente,apareceuovalorincrementado,comosesóexistisse
umcarrinhoparatodosusuáriosdosite!Issoaconteceporque,pordefault,
oSpringmantémosobjetosgerenciadosporelenoescopoconhecidocomo
Application.Ouseja,elecriaapenasumainstânciaeareaproveitadurante
todaaexecuçãodoprograma.Paraficarmaisclaro,vocêpoderiafazerassim:
@Component
@Scope(value = WebApplicationContext.SCOPE_APPLICATION)
public class ShoppingCart {
...
}
113

## Página 121

7.2. CarrinhodecompraseoescopodeSessão CasadoCódigo
Oquenecessitamosédequeexistaumainstânciadocarrinhoparacada
sessãodenavegaçãoqueexistirnaquelemomento.Esseéoescopomaisco-
nhecidocomo Session.
@Component
@Scope(value = WebApplicationContext.SCOPE_SESSION)
public class ShoppingCart {
...
}
Mudar o escopo é muito simples, basta passarmos o valor que que-
remosatravésdaannotation @Scope. Outroescopomuitocomumem
aplicações web é o deRequest, que você pode usar com a constante
WebApplicationContext.SCOPE_REQUEST.
Injetando objetos de escopos menores
Casovocêtenhatentadosubiraaplicação,deveterpercebidoquefoilan-
çadaumaexceptioncomumamensagemumtantoquantogrande. Vamos
verapenasumapartedela.
No thread-bound request found: Are you referring to request
attributes outside of an actual web request ...
A exception está nos informando de que estamos tentando usar um
objeto de escopo relativo à web em outro objeto cujo escopo não tem
nadaavercomaweb. Eéjustamenteoqueestáacontecendo, aclasse
ShoppingCartControllernãotemnenhumaanotaçãorelativaaoescopo
e,comojávimos,odefaultéode Application.Nestasituação,oSpring
nãoconsegueresolverainje ção,poisumobjetodeescopodeaplicaç ãonão
temnadaavercomosescoposwebemsi.Aregrageralé:injetesempreobje-
tosdeescoposmaioresemobjetosdeescoposmenores,nuncaaocontrário.
• ObjetosnoescopoApplicationpodemserinjetadosemqualquer
lugar.
• ObjetosnoescopodeSessionpodemserinjetadosemoutrosdo
mesmoescopoouemescopode Request.
114

## Página 122

CasadoCódigo Capítulo7. Carrinhodecompras
Pensandonisso,amaneiramaisfácilderesolveresseproblemaémodi-
ficandoaclasse ShoppingCartControllereatransformandoemobjeto
deescopode Request.
@Controller
@RequestMapping("/shopping")
@Scope(value=WebApplicationContext.SCOPE_REQUEST)
public class ShoppingCartController {
...
}
AopiniãodesteautorédequeoSpringMVCfalhounessequesito.Pen-
sandoemumaaplicaçãoweb,faztodoosentidoqueosobjetosquerepre-
sentamcontrollerssejamdeescopoderequisiç ão.Afinaldecontas,essaéa
naturezadeumaaplicaçãoweb;objetossãocriadosedestruídosaofimde
umarequisição.Sóquequerernãoépoder,entãotemosquenosadequarao
queoframeworknosfornece.
ComooescopodeAplicaçãoémuitocomumemaplicaçõesqueusam
oSpring,elesforneceramoutramaneiraderesolveroproblema,bemmais
obscura.
@Component
@Scope(value = WebApplicationContext.SCOPE_SESSION,
proxyMode = ScopedProxyMode.TARGET_CLASS)
public class ShoppingCart {
...
}
Podemosusaroatributo proxyModeparaindicarcomoosobjetosge-
renciadosdevemsercriados.Omododefaultécriarumainstâncianormal,
viareflectionmesmo.Algoparecidocomoquesegue.
Class klass = //recupera classe do objeto
klass.newInstance();
Eesseéjustamenteomotivodoproblema,jáqueelesóvaipodercriaro
objetodotipo ShoppingCartquandoexistirumarequisiçãoweb.Quando
definimoso proxyModeiguala ScopedProxyMode.TARGET_CLASS,esta-
mospedindoqueoSpringmodifiqueamaneiracomoelecriaoobjeto,neste
115

## Página 123

7.3. Exibindoositensdocarrinho CasadoCódigo
casousandoumabibliotecaespecializadanisso,chamada cglib. Usando
esseartifício,conseguimosinjetarumobjetodeescopomenor,nocasode
sessão,emummaior,nocasodeaplicaç ão.
Proxy , um Design Pattern
Onomedoatributoé proxyModenãoporacaso.EleavisaaoSpring
queoDesignPatternProxydeveseraplicadoparaacriaç ãodosobjetos.
Basicamente,aimplementaçãodessepatternfazcomque,emvezdetra-
balharmoscomoobjetoalvo,nestecasoo ShoppingCart,sejacriada
umasegundaclassequecontrolatodooacessoaooriginal.Oprópriodá
suporteàcriaçãodeumProxy,sóqueeleimpõequesejamcriadasin-
terfacesparaisso.Atravésda cglib,conseguimosamesmaimplemen-
tação,sóquebaseadanaclasseconcreta.OSpring,comoeraesperado,
suportaasduasmaneiras.
Entendoqueusaroproxyéojeitomaiscomumdomercadodeatingira
injeção,masnestecasocontinuoachandoquecolocaroescopode request
nocontrolleréasoluçãomaislimpa.Fiqueàvontadeedecidaqualsoluç ão
seencaixamelhornoseuproblema.
Pronto,agoranossosusuáriospodemfazersuascomprassemqueum
coloqueitensnocarrinhodooutro.
7 .3 E xibindo os itens do carrinho
Napáginadedetalhedolivro,alémdepodermoscolocá-lonocarrinho,tam-
bémépossívelexibironúmerodeitensquejáexistematualmente.
<ul class="clearfix">
<li><a href=""
rel="nofollow">Seu carrinho (${shoppingCart.quantity})
</a></li>
....
116

## Página 124

CasadoCódigo Capítulo7. Carrinhodecompras
</ul>
Lembre-se que esse é mais um trecho da mesma página de deta-
lhe, seu código completo você pode ver direto no Github, basta seguir
este link: http://tinyurl.com/odjn4j3
Oproblemaaquiéque,semprequeapáginadedetalheéacessada,otre-
choquedeveriaexibiraquantidadedeitensnãoexibenada.
Seu carrinho ()
AcomplicaçãoaquiéqueoSpringMVCestádisponibilizandooobjeto
ShoppingCartcomoutronomenaExpressionLanguage.
${sessionScope['scopedTarget.shoppingCart'].quantity}
Achavecriadafoia scopedTarget.shoppingCarte,comotemum
.(ponto)nonome,somosobrigadosaacessarachaveatravésdasintaxede
mapa.Apenasporcuriosidade,avariávelcomonome sessionScopeestá
sempredisponívelnasJSPsparaquequevocêtenhaacessodiretamenteao
mapadevariáveisqueestejamnesteescopo.Omesmoacontececomosobje-
tosqueestãonorequest,queficamdisponíveisatravésdo $requestScope.
Sóqueap er
guntaquenãoquercalaré: porqueoSpringMVCcolocoua
variávelcomeçandocom scopedTarget.?
Oproblema
foijustamenteanossaabordagempararesolverainje çãodo
carrinhodecompras. Comofoiescolhidaaestratégiabaseadanoproxy,o
frameworkcolocaosobjetosnoescopocomesseprefixo,justamentepara
poderdarumtratamentodiferenciadointernamente. Casotivéssemosop-
tadopelaabordagemdetrocaroescopodonossocontrollerpelorequeste,
nãohouvesseanecessidadedetrocaramaneiracomocriamososobjetosdo
tipo ShoppingCart,oSpringMVCteriacolocadonasessãoavariávelcom
omesmonom
edaclasseenossaJSPfuncionariatranquilamente.Lembre-se
semprequetudoéumatroca:quandodecidimosirporumcaminhotemos
queteremmenteque,talvez,umpre çosejacobrado.
117

## Página 125

7.3. Exibindoositensdocarrinho CasadoCódigo
Detodaforma,agoranossoproblemaestáresolvido.Casonãotenhagos-
tadodessaabordagem,oqueécompletamentecompreensível,podemosten-
taroutroscaminhos.
Expondo os beans na Expression Language
PodemosensinaraoSpringMVCquequeremosquetodososnossosobje-
tosgerenciadosfiquemdisponíveisparauso,atravésdaExpressionLanguage.
...
public class AppWebConfiguration {
@Bean
public InternalResourceViewResolver
internalResourceViewResolver() {
InternalResourceViewResolver resolver =
new InternalResourceViewResolver();
resolver.setPrefix("/WEB-INF/views/");
resolver.setSuffix(".jsp");
//essa linha expõe todo mundo
resolver.setExposeContextBeansAsAttributes(true);
return resolver;
}
...
}
Comessaalteraçãootrecho ${shoppingCart}jávaifuncionar. Ele
vaiusaronomequeestáregistradodentrodo containerdoSpring,quepor
defaultéomesmodaclasse.Essasoluç ãoatéfunciona,aúnicapreocupação
ésealguémcomeçaraacessartudoqueéobjetoapartirdaJSP.
Pararestringirumpoucoafanfarra,pode-seliberarapenasalgunsobjetos
paraseremexpostos.
@Bean
public InternalResourceViewResolver
internalResourceViewResolver() {
InternalResourceViewResolver resolver =
new InternalResourceViewResolver();
resolver.setPrefix("/WEB-INF/views/");
118

## Página 126

CasadoCódigo Capítulo7. Carrinhodecompras
resolver.setSuffix(".jsp");
//passamos o exato nome da classe que será registrada
resolver.setExposedContextBeanNames("shoppingCart");
return resolver;
}
Dessamaneira,vocêpodecontrolarquaisobjetosdevemestarsempre
disponíveis.
7 .4 C onclusão
Agorajáconseguimosmanterobjetosemescoposdiferenteseacessá-losnas
nossaspáginas.Nestemomentodolivro,vocêjátemferramentassuficientes
paracomeçarafazersuamaisnovaaplicaç ão!Nãopercatempo,jácomece
apensarnopróximoprojetoparapraticartudoquefoiestudadoatéagora.
Casonãoestejacansado,jáleiaopróximocapítulo,poisvamosfazeruma
integraçãocomumsistemaexterno,justamenteparafecharoprocessode
compradonossousuário.
119

## Página 128

Capítulo8
Retornosassíncronos
Nossousuáriojáestáquasefechandoacompradele. Agora,comoslivros
jácolocadosnocarrinho,sófaltaqueelepreenchaosdadosdepagamentoe
efetivamentecompreoslivros.Aqui,vamosapenassimplificaroprocessoe
deixarquenossousuáriocompreumlivroapenasapertandoumbotão.
<tbody>
<c:forEach items="${shoppingCart.list}" var="item">
<tr>
<td class="cart-img-col">
<img src="" alt="${item.product.title}"/>
</td>
<td class="item-title">
${item.product.title} - ${item.bookType}
</td>
<td class="numeric-cell">

## Página 129

CasadoCódigo
${item.price}
</td>
<td class="quantity-input-cell">
<input type="number" min="0" readonly="readonly"
value="${shoppingCart.getQuantity(item)}">
</td>
<td class="numeric-cell">
${shoppingCart.getTotal(item)}
</td>
</tr>
</c:forEach>
</tbody>
<tfoot>
<tr>
<td colspan="2">
<form
action="${spring:mvcUrl('PC#checkout').build()}"
method="post">
<input type="submit" class="checkout"
name="checkout" value="Finalizar compra "
id="checkout"/>
</form>
</td>
<td class="numeric-cell">
${shoppingCart.total}
</td>
<td></td>
</tr>
</tfoot>
Essa é a página onde nossos usuários poderão ver os itens adicio-
nados ao carrinho. O nome dela éitems.jsp e vai ficar na pasta
WEB-INF/views/shoppingCart. Lembre-seque,paraconferirocódigo
completo,bastaquevocênavegueatéorepositóriodoprojeto, https://github.
com/livrospringmvc/lojacasadocodigo.Comoédepraxe,nossousuárionão
podenavegardiretamenteparaessapágina,oendere çodeacessodeveser
referenteaummétodonanossaclasse ShoppingCartController.
122

## Página 130

CasadoCódigo Capítulo8. Retornosassíncronos
@RequestMapping(method=RequestMethod.GET)
public String items(){
return "shoppingCart/items";
}
Todo o código presente nesse JSP é bem normal, não tem nada que
não foi estudado até agora. O único detalhe novo é a presença do for-
mulário de checkout, que aponta para o métodocheckout da classe
PaymentController,exatamenteocódigoquevamoscome çaraconstruir.
@Controller
@RequestMapping("/payment")
public class PaymentController {
@Autowired
private ShoppingCart shoppingCart;
@RequestMapping(value="checkout",method=RequestMethod.POST)
public String checkout() {
BigDecimal total = shoppingCart.getTotal();
//código de integração
return "redirect:/success";
}
}
Éumcontrollercomum,oúnicodetalhequevamosterqueimplemen-
taragoraéaintegraçãocomomeiodepagamento. Paradeixaraaplicaç ão
maisreal,foicriadaumaaplicaç ãowebchamada book-payment,queestá
hospedadaatualmentenoHeroku.
CasoqueiraefetuarumtesteeestivernoLinuxouMac,bastaexecutar
um curl.
curl --header "Content-type: application/json" --request POST
--data '{"value": 600}'
http://book-payment.herokuapp.com/payment
Alógicaésimples: sóaceitamospagamentosdeaté500reais. Somos
obrigadosapassarosdadosusandoo JSON,umformatodedadosbastante
123

## Página 131

CasadoCódigo
usadoemaplicaçõesquerealizamintegraçõesviaHTTP.Casoovalortenha
seguidoaregra,éretornadoostatus 201,queindicaqueumnovorecurso
foicriado,nestecaso,opagamento.Poroutrolado,setiversidopassadoum
valormaiorque500,éretornadoostatus 400,oqueindicaquearequisiç ão
possuidadosinválidos.
RestT emplate
Vamosprecisardeumabibliotecaquenosajudearealizararequisiç ão
HTTP,paraquenossaintegraçãofuncione.Alibmaisfamosaéa Http Com-
ponents,quepodeserencontradaaqui http://hc.apache.org.
Paranãotermosquelidarcomosdetalhesdabiblioteca,vamosutilizar
umobjetoquejáencapsulatodaessalógica.
@Controller
@RequestMapping("/payment")
public class PaymentController {
@Autowired
private ShoppingCart shoppingCart;
@Autowired
private RestTemplate restTemplate;
@RequestMapping(value = "checkout",
method = RequestMethod.POST)
public String checkout() {
BigDecimal total = shoppingCart.getTotal();
String uriToPay =
"http://book-payment.herokuapp.com/payment";
try {
String response =
restTemplate.postForObject(uriToPay,
new PaymentData(total), String.class);
return "redirect:/payment/success";
} catch (HttpClientErrorException exception) {
return "redirect:/payment/error";
}
124

## Página 132

CasadoCódigo Capítulo8. Retornosassíncronos
}
}
Oobjetodotipo RestTemplatejádisponibilizadiversosmétodos,que
podemosusarpararealizardiversostiposderequisições. Percebaquefoi
muitosimples,apenasapontamosoendere çoeinvocamosométodoque
realizao POSTeesperacomorespostaumasimplesString. Paraconse-
guirmosainje çãodesteobjeto,precisamostambémalteraranossaclasse
AppWebConfigurationpararegistrarobeanno containerdoSpring.
@Bean
public RestTemplate restTemplate(){
return new RestTemplate();
}
Outro detalhe que pode chamar a atenção é a utilização da classe
PaymentData. Qualomotivodenecessitarmosdela? Osistemadepaga-
mentocomqueestamosrealizandoaintegraçãopedequeoformatododado
passadosejaoseguinte:
{"value": 600}
Écomosefosseum Map,precisamosdeumachavechamada value
associadaaumvalorqualquer. Casoagentepasseo BigDecimaldireto,
qualseriaonomedessachave? Éjustamenteporissoqueprecisamoscriar
umaclasse.
package br.com.casadocodigo.loja.models;
import java.math.BigDecimal;
public class PaymentData {
private BigDecimal value;
public PaymentData() {
}
125

## Página 133

CasadoCódigo
public PaymentData(BigDecimal value) {
this.value = value;
}
public BigDecimal getValue() {
return value;
}
}
Reparequetemosumatributoquesechamaexatamente value,justa-
menteparaqueoSpringMVCpossapegaroobjetoegeraro JSONcom
aschavescorretas.
Configurando o converter para JSON
Nestemomento,onossocódigodeintegraç ão,setestado,lan çaráuma
exception.
org.springframework.web.client.RestClientException:
Could not write request: no suitable HttpMessageConverter
found for request type
[br.com.casadocodigo.loja.models.PaymentData]
OSpringMVCestánosdizendoquenãoconseguiuacharumamaneira
deconverteroobjetodotipo PaymentDataparao JSON.Comojáestamos
vendofazumtempo,eleémuitomodulare,paratudodequenecessitamos,
temosqueiradicionandoasdependênciasnecessárias.Nessecaso,precisa-
mosadicionarumabibliotecachamadaJackson,muitafamosanomundoJava
noquedizarespeitoàtransformaçãodeobjetosem JSON.Precisamosreali-
zaraalteraçãoaseguir,nonossoarquivo pom.xml.
<dependency>
<groupId>com.fasterxml.jackson.core</groupId>
<artifactId>jackson-core</artifactId>
<version>2.5.1</version>
</dependency>
126

## Página 134

CasadoCódigo Capítulo8. Retornosassíncronos
<dependency>
<groupId>com.fasterxml.jackson.core</groupId>
<artifactId>jackson-databind</artifactId>
<version>2.5.1</version>
</dependency>
Pronto,agorajáconseguimosrealizaranossaintegraç ãosemmaiores
problemas!
8.1 E xecutando operações demoradas assin-
cronamente
Agoraquenossocódigodeintegraç ãojáfunciona,vamostentarpensarum
poucoadiante. ACasadoCódigoéumaempresadesucesso,oBrasilin-
teirocompralivrosdetecnologianela. Emcertosmomentosdoano,como
naBlackFriday,elaliberacertaspromo çõesquefazemcomqueositefique
muitomovimentadoe,comisso,temosmuitosusuáriosconcluindocompras
aomesmotempo.Algosimilaraconteceemtodasoutrasempresas.
Nãoéraro,nessassituaçõesdeusointenso,queossistemasfiquemum
poucomaislentosouatéquecaiamefiquemforadoarporumtempo,oque
podegerarumprejuízogrande.Emgeraltodosossistemastêmseuspontos
degargaloe,comonãopoderiaserdiferente,nóstemosonossotambém.
Jáseperguntouquantotempopodelevarparaanossaaplicaç ãofazeruma
requisiçãoparaosistemadepagamento?Casoesseoutrosistemademore,o
quepodeacontecercomonossosite?
Neste exato momento o funcionamento é basicamente o seguinte.
QuandoumanovarequisiçãocheganonossoTomcat,elefazumtratamento
inicialedelegaaresponsabilidadeparaaServletconfigurada,nessecasoado
SpringMVC.A DispatcherServletvaidescobrirqualdosnossoscon-
trollersdevetratararequisiç ãoefazerotrabalhoparaqueissorealmente
aconteça.Todoessefluxo,acontecedentrodeuma ThreadcriadapeloTom-
cat,paraqueelepossatratarváriasrequisiçõessimultaneamente.Essa Thread
sóéliberadaquandoométododonossocontrolleracabadefazerotrabalhoe
indicaparaqualendere çodevemosir.Essemodelodetrabalho,ondealguém
ficaesperandoooutroacabar,paraaísimcontinuarseutrabalho,éconhe-
127

## Página 135

8.1. Executandooperaçõesdemoradasassincronamente CasadoCódigo
cidocomomodelo síncrono.OproblemadessemodeloéqueoTomcattem
umnúmerolimitadode Threadsquepodemsercriadase,casoessenúmero
cheguenolimite,asrequisiçõesdosnossosusuáriosvãocome çaraserenfi-
leiradasepodemosterumalentidãonasaplicações.
Comojácomentamos,emumpicodeacesso,podemossofrerdestepro-
blemajustamentenomomentoemqueprecisamosrealizaraintegraç ãocom
umsistemaexterno,noqualnãotemosnenhumcontrolesobreotempode
resposta.
Indo para o assíncrono
Agrandesacadaparaessetipodesituaç ãoétentarliberaroTomcatpara
atenderoutrasrequisiçõesenquantorealizamosaintegraç ãocomonosso
meiodepagamento. Éexatamenteparaissoque,desdeaversão3daespe-
cificação,vocêpodecriarumaServletqueconseguetrabalhardemodoas-
síncrono!E,paraanossasorte,aServletdoSpringMVCjávempreparada
paratrabalhardessejeito.
@RequestMapping(value = "checkout", method = RequestMethod.POST)
public Callable<String> checkout() {
return () -> {
BigDecimal total = shoppingCart.getTotal();
String uriToPay = "http://localhost:9000/payment";
try {
String response =
restTemplate.postForObject(uriToPay,
new PaymentData(total), String.class);
return "redirect:/payment/success";
} catch (HttpClientErrorException exception) {
return "redirect:/payment/error";
}
};
}
Bastaqueretornemosumobjetodotipo Callable,queexistedesdeo
Java5eéumanálogoaoobjetotipo Runnable,muitocomumparaquem
usaThreads.Aúnicadiferençado Callableéqueelenospermitedarum
128

## Página 136

CasadoCódigo Capítulo8. Retornosassíncronos
retorno,algonecessárioparanós,jáqueprecisamosinformarparaqualen-
dereçovamosdepoisdaintegração. Sódevocêretornarum Callable,o
SpringMVCjávaicriariniciarumcontexto assíncronoemsuaServlete
liberarparaqueoTomcatpossausara Threaddeleparaatendernovasre-
quisições.Assim,quandorecebermosarespostadaintegração,retornamoso
endereçoderedirecteomesmoéinformadoparaoTomcat.Percebaquetudo
ocorredemaneirabemtransparente,nãoprecisamosemnenhummomento
lidarcomaServletassíncronaemsi,sóprecisamosestarcientesdequeisso
sóépossívelporqueaespecificaçãoteveapreocupação.
Éimportantenotarquenãoestamostratandodaperformancedonosso
site,provavelmenteotempoderequisiç ãovaiseromesmo. Oqueestamos
tratandoaquiédaescalabilidade,estamostentandomanterotempomédio
derequisiçãomesmoqueaaplicaç ãosofracomumacessoacimadonor-
mal. Vocêpodeusaressatécnicaparatodométododocontrollerquetiver
derealizarumaintegraçãocomumsistemaquevocênãoconhece.Umoutro
exemploseriaoenviodee-mail.
129

## Página 137

8.2. DefferedResulteummaiorcontrolesobreaexecuçãoassíncrona CasadoCódigo
Sintaxe do Jav a8 para classes anônimas
Usamosasintaxedos lambdas,disponívelnoJava8,pararetornar-
mosumobjetodotipo Callable. Casovocêestejautilizandouma
versãoinferiordoJava,podetrocaraquelecódigopeloseguinte:
return new Callable<String>() {
@Override
public String call() throws Exception {
BigDecimal total = shoppingCart.getTotal();
String uriToPay = "http://localhost:9000/payment";
try {
String response =
restTemplate.postForObject(uriToPay,
new PaymentData (total), String.class);
return "redirect:/payment/success";
} catch (HttpClientErrorException exception) {
return "redirect:/payment/error";
}
}
};
Queeraocomum,quandosefazianecessárioousodeclassesanôni-
mas.
8.2 D efferedResult e um maior controle sobre
a execução assíncrona
Ousodo Callableéamaneiramaissimplesderealizaraexecuç ãodeum
códigoassíncronodentrodonossocontroller.Talvezoúnicopontonegativo
équevocênãotemnenhumcontroledecomoessecódigovaiserexecutado.
Porexemplo:
• QuantasnovasThreadsexistemdisponíveisparaaexecuçãodocódigo
assíncrono?
• Eseeuquisercontrolaracriaçãodas Threads?
130

## Página 138

CasadoCódigo Capítulo8. Retornosassíncronos
• Eseeuprecisarrodaressecódigodentrodeumafiladeprocessamento?
Casovocêsevejaemalgumasdessassituações,podemosusaroobjeto
dotipo DefferedResultque,emumatraduçãolivre,seriaalgoparecido
comoretornopostergado.
@RequestMapping(value = "checkout", method = RequestMethod.POST)
public DeferredResult<String> checkout() {
BigDecimal total = shoppingCart.getTotal();
DeferredResult<String> result = new DeferredResult<String>();
IntegrandoComPagamento integrandoComPagamento =
new IntegrandoComPagamento(result, total, restTemplate);
Thread thread = new Thread(integrandoComPagamento);
thread.start();
return result ;
}
Respire,poismuitacoisaaconteceunessecódigo.Estouaquijustamente
paraexplicarcadaumdospassos.Aparteprincipaléquecriamosumobjeto
dotipo DefferedResulteopassamoscomoargumentoparaaconstruç ão
deumoutroobjeto,quevaiexecutaremuma Threaddiferentee,emalgum
momento,vaisinalizarqueacabouderealizaroprocessamento. Essareal-
menteéapartemaisimportantedessecódigo.Semprequevocêfortrabalhar
como DeferredResult,oobjetoquefoiretornadoéomesmoquevaiser
passadocomoargumentoparaaexecuçãoemoutra Thread.
Nocódigoanterior,extraímosaintegraç ãocomomeiodepagamento
paraumaoutraclasse,cujocódigovaiserexecutadona Threadquecriamos
manualmente:
package br.com.casadocodigo.loja.service;
public class IntegrandoComPagamento implements Runnable {
private DeferredResult<String> result ;
private BigDecimal value;
131

## Página 139

8.2. DefferedResulteummaiorcontrolesobreaexecuçãoassíncrona CasadoCódigo
private RestTemplate restTemplate;
public IntegrandoComPagamento(DeferredResult<String> result,
BigDecimal value, RestTemplate restTemplate) {
super();
this.result = result;
this.value = value;
this.restTemplate = restTemplate;
}
@Override
public void run() {
String uriToPay = "http://localhost:9000/payment";
try {
String response =
restTemplate.postForObject(uriToPay,
new PaymentData(value), String.class);
//linha de notificação
result.setResult("redirect:/payment/success");
} catch (HttpClientErrorException exception) {
result.setResult("redirect:/payment/error");
}
}
}
O método setResult é parte importante desse trecho de código.
Quando você o invoca, o objeto do tipoDeferredResult notifica o
SpringMVCdequeocontextoassíncronoacabouequeelepodegerarore-
tornoparaousuáriodaaplicação.
Ousodo DeferredResultaindapermiteumcontrolemaisfinoda
execuçãoassíncrona,disponibilizandoalgunsoutrosmétodosquepodemser
úteis.
•onTimeout(Runnable callback):registreumobjetoquedeveter
ométodoinvocadocasoexpireumdeterminadotempo.
•onCompletion(Runnable callback): registre um objeto que
deveterométodoinvocadoquandoaexecuç ãoacabar.Porexemplo,
132

## Página 140

CasadoCódigo Capítulo8. Retornosassíncronos
registrarumlog.
8.3 C onclusão
Nestecapítuloconseguimosrealizarumaintegraçãocomumsistemadeter-
ceiroe,paraficaraindamelhor,aintegraçãopodeserfeitasemtravaronosso
servidor.Vocêdevelevaressaliçãoparaasuavida,quandoforrealizarqual-
quertipodeoperaçãoqueenvolvaumoutrosistemaquevocênãoconhece;
nuncafiquefaçanenhumacomunicaçãodemaneirablocante. Éumapena
queasAPIsdisponíveisnomundoJavajánãosejamtodaspensadasdessa
maneira.ImagineseaespecificaçãoJDBCobrigassetodososdriversareali-
zaremasconsultasdemaneiraassíncrona,tudoseriamuitomelhor.
Nestemomento,meuconselhoéquevocêdescanseumpouco.Esteca-
pítulo,apesardenãomuitolongo,envolveuconceitosnãotãosimples.Pense
umpoucosobreelesefaçaunstestes,tenteverondeessetipodesoluç ãopo-
deriaseencaixarnoseuatualtrabalho.
133

## Página 142

Capítulo9
Melhorandoperformancecom
Cache
SemprequeentramosnositedaCasadoCódigo,elanosmostraummontede
livrosquepodemoscomprar.Oleitormaisatentojádeveterpercebidoque
essalistagemnãomudamuitodentrodeumdeterminadointervalodetempo.
Eofatodenãomudarnoslevaaumquestionamento. Seráquerealmente
precisamosficarexecutandoalógicadométododocontrolleremtodasas
vezesqueumusuárioacessaressapágina?

## Página 143

9.1. Cacheandooretornodosmétodosdoscontrollers CasadoCódigo
9.1 C acheando o retorno dos métodos dos con-
trollers
Umdospontosondemaispodemosganharemtempodeexecuç ãodentro
deumaaplicaçãoéjustamentequandonãonecessitamosrealizaramesma
lógicadiversasvezes.Pensandoemtodaaarquiteturadeumaaplicaç ãoweb
padrão,existemmuitoslugaresondeissoépossível.
• Evitaracessocontínuoaobancodedados;
• Evitarqueonavegadorfiquerealizandorequisiçõesparaarquivoses-
táticos;
• Evitarqueummétododocontroller,cujoretornonãomudamuito,
fiquesendoexecutadodiversasvezes.
Podemosatacarcadaumdospontoscitadosaqui,eolhaqueessessãoos
maisevidentes.Essetipodeestratégia,ondeguardamosumresultadoefica-
mosreaproveitando,écomumenteconhecidocomo Cache.Comojáestamos
acostumados,oSpringMVCtambémforneceajudanessaárea.
Aideiaaquié:queremosguardaroretornodométodo,docontrollerres-
ponsávelporretornaro ModelAndViewrelativoaoendereçodeexibiçãodos
livroscadastrados.Sópararelembrar,dêumaolhadanocódigo:
@Controller
@Transactional
@RequestMapping("/produtos")
public class ProductsController {
@RequestMapping(method=RequestMethod.GET
public ModelAndView list(){
System.out.println("listando");
ModelAndView modelAndView =
new ModelAndView("products/list");
modelAndView.addObject("products", products.list());
return modelAndView;
}
}
136

## Página 144

CasadoCódigo Capítulo9. MelhorandoperformancecomCache
Semprequeousuárioacessaoendere ço/produtos,oSpringMVCin-
vocaessemétodoondeacessamosobancoecarregamososlivroscadastrados.
CasonossapáginafosseinteiramentefielàCasadoCódigo,teríamosainda
maisumaconsulta,queretornariaoslivrosquesãolan çamentos.Ogrande
pontoéqueessasinformaçõesnãomudamacadaacesso,logonãofazmuito
sentidoficarmosexecutandoessalógicaotempointeiro.
Pararesolvermosisso,oSpringMVCprovêumasoluçãomuitosimples.
@RequestMapping(method=RequestMethod.GET)
@Cacheable
public ModelAndView list(){
ModelAndView modelAndView =
new ModelAndView("products/list");
modelAndView.addObject("products", products.list());
return modelAndView;
}
Apenascolocaraannotation @Cacheableemcimadométodofazcom
oqueoSpringMVCsaibaque,umavezqueocódigoforexecutado,eledeve
guardaroretornoeutilizá-loparatodasaspróximasrequisiçõesquecaiam
nomesmolugar. Agorajápodemostentarfazerumteste,paraverificarse
realmenteonossométodosóestásendoexecutadodaprimeiravez.Sóque
quandotentamoslevantaroservidor,apareceaseguinteexception:
java.lang.IllegalStateException: No cache names could be detected
on 'public org.springframework.web.servlet.ModelAndView
br.com.casadocodigo.loja.controllers.ProductsController.list()'
Essaexceptionnãoémuitoclara.OmódulodecachedoSpringpedeque
vocêdefinanomesquepodemagruparumoumaisobjetosquevocêdecida
colocarnocache.Porexemplo,todososlivrosqueficaremnocachepodem
ficaragrupadossobachave books.Issotambéméconhecidocomo cache
region.
@RequestMapping(method=RequestMethod.GET)
@Cacheable (value="books")
public ModelAndView list(){
ModelAndView modelAndView =
137

## Página 145

9.1. Cacheandooretornodosmétodosdoscontrollers CasadoCódigo
new ModelAndView("products/list");
modelAndView.addObject("products", products.list());
return modelAndView;
}
Essa é uma parte importante, quase sempre quando usarmos o
@Cacheable,vaisernecessáriodefinirovalorparaaregiãodecache.
Pronto,agorapodemossubiroservidornormalmentee,alémdisso,pre-
cisamosverificarseocacheestáfuncionando.Parafazeressachecagem,po-
demosacessarateladeprodutosmaisdeumavez.Onormalseriaquea query
realizadapeloHibernatesófossemostradadaprimeiravez,indicandoqueo
método listdonossocontrollersóexecutounoprimeiroacesso.Sólem-
brando,asqueriesestãoexibidasporquefizemosessaconfiguraç ãonaclasse
JPAConfiguration.
Casovocêtenharealizadooteste,deveterpercebidoqueométodoainda
continuasendoexecutadotodasasvezes.
Habilitando e configurando um provedor de Cache
Vamosprecisarhabilitarousodocache,paraqueoSpringpossacome çar
aguardarosretornosdoslocaisindicadoscomaannotation @Cacheable.
@EnableWebMvc
@ComponentScan(basePackageClasses={HomeController.class,
ProductDAO .class,FileSaver.class,ShoppingCart.class})
@EnableCaching
public class AppWebConfiguration {
...
}
Esseéjustamenteopapeldaannotation @EnableCaching.Agora,de-
poisdehabilitado,nomomentodostartdoservidor,outraexceptionélan-
çada.
java.lang.IllegalStateException: No bean of type CacheManager
could be found.Register a CacheManager bean or remove the
EnableCaching annotation from yourconfiguration.
138

## Página 146

CasadoCódigo Capítulo9. MelhorandoperformancecomCache
PercebaqueelanosinformaqueoSpringnãofoicapazdeencontrarne-
nhumaclassequesejaresponsávelporefetivamenteguardarosobjetosque
devemsercacheados.Areferênciaàinterface CacheManageréimportante,
poissemprequequisermosusarumaimplementaçãoquefaçaopapeldoca-
cheparaagente,teremosquebuscarclassesqueimplementemessainterface.
...
public class AppWebConfiguration {
@Bean
public CacheManager cacheManager(){
return new ConcurrentMapCacheManager();
}
}
Nessecódigo,fizemosusodaimplementaç ãomaissimples,quejávem
prontadentrodopróprioSpring,a ConcurrentMapCacheManager.Nesse
momento,elaémaisdoqueosuficienteparaoquenecessitamos.Casonão
sejasuficienteparaoseuprojeto,dêumpuloatéofinaldocapítuloejáveja
comopodemosusarumasegundaop ção. Comessasconfigurações,nossa
aplicaçãojádevesubireconseguirguardarosobjetosemcache!
9.2 E quando tiverem novos livros?
EstamosmantendonocacheoretornodométodoquelistaoslivrosnaCasa
doCódigo. Equandofizermosocadastrodeumnovolivro? Oquedeve
acontecercomalistagem?Esseéumproblemaclássicodocache,emalgum
momentoprecisamosrenová-lo.UsandoaAPIdecacheprovidapeloSpring,
nãopoderiasermaisfácil.
@RequestMapping(method=RequestMethod.POST)
@CacheEvict (value="books", allEntries=true)
public ModelAndView save(...){
...
}
Aannotation @CacheEvicttemjustamenteessainten ção. Podemos
configurarque,quandoalgummétodoforinvocado,determinadaregiãodo
139

## Página 147

9.3. Usandoumprovedordecachemaisavan çado CasadoCódigo
cachedeveterseusvaloresinvalidados. Usamosoatributo allEntries
paraindicarquequeremosquetodososvaloressejamretirados.Essaanno-
tationsuportaconfiguraçõesmaisespecíficas,entretanto,invalidartodosos
valoresgeralmentevaisermaisdoqueosuficienteparaasuaaplicaç ão.Vale
lembrarqueoatributo valuepodereceberumarraydenomes. Issoseria
especialmenteútilsetivéssemoscacheadooretornodométodoquecarrega
umprodutoeotivéssemoscolocadoemoutraregião,porexemplo.
9.3 U sando um provedor de cache mais av an-
çado
O ConcurrentMapCacheManager,comojáfoicitado,éumaimplemen-
taçãodecachemuitosimples.Váriosfatoressãoimportantes,quandovamos
colocarobjetosnocache.
• Qualotempomáximo?
• Qualonúmerolimitedeobjetos?
• Qualonúmerolimitedeobjetosdedeterminadotipo?
• Qualotempomáximoinativo?
Claroquearespostadessasquestõesdependemdacomplexidadedopro-
blemaquevocêestáquerendoresolver. Paratentarcobriralgumasdessas
questões,podemosusarumaimplementaçãoprovidapeloGuava,umabibli-
otecacriadapeloGooglecomváriasclassesquepodemserúteisemqual-
querprojeto.Sigaestelink: https://code.google.com/p/guava-libraries/wiki/
GuavaExplainedparamaisdetalhessobreoqueéoferecido.
Pararesolveronossoproblema,vamosficarapenascomapartedecache,
fornecidapeloGuava.
@Bean
public CacheManager cacheManager() {
CacheBuilder<Object, Object> builder =
CacheBuilder.newBuilder()
.maximumSize(100)
140

## Página 148

CasadoCódigo Capítulo9. MelhorandoperformancecomCache
.expireAfterAccess(5, TimeUnit.MINUTES);
GuavaCacheManager cacheManager = new GuavaCacheManager();
cacheManager.setCacheBuilder(builder);
return cacheManager;
}
Aclasse CacheBuilder,dopróprioGuava,serveparacriarmosnossa
configuração de cache. Perceba que conseguimos definir alguns valores
querespondemaalgumasdasperguntasquefizemosanteriormente. Além
disso,oSpringjácriouumaextensãoquepossuiumaimplementaç ãoda
interface CacheManagerjustamente para suportar o Guava, no caso a
GuavaCacheManager. Comessamudan ça,saímosdeumprovedorbem
simplesdecacheparaumjámaiscompletoeque,provavelmente,vocêvai
poderusaremalgumdeseusprojetos.
ApenasumúltimodetalheemrelaçãoàutilizaçãodoprovedordoGuava:
precisamosalterarnossoarquivo pom.xmlparaadicionaraextensãodo
Spring.
<!-- cache -->
<dependency>
<groupId>com.google.guava</groupId>
<artifactId>guava</artifactId>
<version>18.0</version>
</dependency>
<dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-context-support</artifactId>
<version>4.1.0.RELEASE</version>
</dependency>
Alémdasopçõescitadasaquinolivro,oSpringtambémsuportaoutros
provedoresdecache,jáprontos.
• EhCache
• GemFire
141

## Página 149

9.4. Conclusão CasadoCódigo
• JSR-107,especificaçãodoJavaparapadronizarasAPIsdecache.
Casonenhumdessessirvaparavocê,aindaexisteapossibilidadedevocê
implementarainterface CacheManagereplugarasuasolução.
9.4 C onclusão
Nestecapítulo,vimosumadassoluçõesmaisimportantesquandoestamos
falandodeperformancedeumaaplicação.Evitaroacessoaodiscoouaalgum
serviçoremoto,podefazercomquesuaaplicaçãodiminuadrasticamenteo
tempoderespostadasrequisições.Oúnicopontoaquevocêdeveficarmuito
atentoéemrelaçãoaquaisobjetosdevemirparaocache.Lembre-sesempre,
quandoumobjetoestácacheado,vocêdeveaceitarqueseususuários,nem
quesejaporumcurtoperíododetempo,podemverdadosquenãosãoos
maisatualizados.
142

## Página 150

Capítulo10
Respondendomaisdeum
formato
Nossaaplicação,atéopresentemomento,sólidacomrequisiçõesvindasde
umnavegador,sóqueagoravamosumpoucoalémdoquejáexistenaCasa
doCódigo.Sitesdevendasmuitograndes,comoaAmazoneoSubmarino,
alémdeexporemosseusprodutosemseussites,fazemparceriascomoutros
sitesparaqueessasoutrasaplicaçõestambémpossamexibirseusprodutos.
10.1 E xpondo os dados em outros formatos
Quandofalamosdeintegraçãocomoutrasaplicações,oprimeiropontoem
quetemosquepensaré:qualéoformatoquevamosusarpararealizarain-
tegração?Atualmente,nossaaplicaçãosóécapazderetornarpáginasparaos

## Página 151

10.1. Expondoosdadosemoutrosformatos CasadoCódigo
clientes,nocasoosnavegadores,em HTML.Umoutrotipodecliente,hoje
jámuitocomum,sãooscelularescomAndroidouiOS.Ecomovocêjádeve
esperar,exibirdadosatravésde HTMLpodenãoseroformatoidealparaser
usadonessesaparelhos.
Aprimeiratarefaqueprecisamosfazeréterumoutrométodononosso
controller,quesejacapazderetornaralistadelivrosemoutroformato. O
escolhidoaquivaisero JSON,queéumformatomuitocomumnomercado.
...
public class ProductsController {
@RequestMapping(method = RequestMethod.GET,value="json")
@ResponseBody
public List<Product> listJson() {
return products.list();
}
}
Perceba que só adicionamos mais um método à classe
ProductsController, a única diferença foi que usamos a annota-
tion @ResponseBody. ElainformaparaoSpringMVCqueoretornodo
métodoéparaserusadodiretamentecomocorpodaresposta.Casovocênão
useessaannotation,elevaiprocurarporumapágina,queéocomportamento
padrão. Bastaquealguémacesseoendere ço/produtos/json, queo
retornojávaiserum JSON.
Talvezoleitormaiscuriosoestejaseperguntando:porqueoretornovai
serum JSON,ondefoiqueconfiguramosisso?Comojáadicionamosade-
pendênciadoJacksonnonossoclasspath,oSpringMVCjáentendequeesse
éoúnicoformato,alémdo HTML,cujaconfiguraçãojátemos.
Esetivermosclientesquetrabalhemmelhorcom XMLdoquecom JSON?
Comovamosfazer? Nessemomento,temosqueterummétodoparacada
formatoderespostaqueprecisamos.
144

## Página 152

CasadoCódigo Capítulo10. Respondendomaisdeumformato
10.2 C ontent negotiation e outros ViewResol-
vers
Terummétodoparacadaformatoderespostadiferenteatéfunciona,oúnico
problemaéquevocêvaiacabarcomcódigosrepetidos. Lembre-sequeo
únicopontoquevaimudaréarepresentaç ãodoretorno,alógicaparare-
cuperarodadovaiseramesma. Vamostentarresolveresteproblema. Pri-
meiro,precisamosapagaraquelemétodonovoedeixarapenasoantigo,que
jáadicionaalistadeprodutosno ModelAndView.
@Controller
@Transactional
@RequestMapping("/produtos")
public class ProductsController {
//apenas lembrando do nosso método que já existe.
@RequestMapping(method=RequestMethod.GET)
@Cacheable(value="lastProducts")
public ModelAndView list(){
ModelAndView modelAndView =
new ModelAndView("products/list");
modelAndView.addObject("products", products.list());
return modelAndView;
}
}
O ponto agora é: quando um cliente fizer o request para a URL
/produtos,qualformatovamosretornar?Essaéaparteinteressante,opro-
tocoloHTTPjáforneceumjeitodelidarcomesseproblema! Elepermite
queoclienteindiquequaloformatoderespostaqueeleprefere. Segueum
exemploderequisiçãousandoaferramenta CURL,famosanomundoUnix.
curl -H "Accept:application/json" -X GET
"http://localhost:8080/casadocodigo/produtos"
curl -H "Accept:text/html" -X GET
"http://localhost:8080/casadocodigo/produtos"
145

## Página 153

10.2. ContentnegotiationeoutrosViewResolvers CasadoCódigo
Noprimeiroexemplo,fizemosumarequisiçãoindicandoquedesejamos
oretornonoformato application/json.Issoéfeitoatravésdocabe çalho
Accept. Percebaquenosegundojáindicamosquequeremos HTMLcomo
formato.Essatécnicaéconhecidacomo Content Negotiationeémuitouti-
lizadaemintegraçõesbaseadasnoHTTP,tambémconhecidacomoREST.
ApartebemlegaléqueoSpringMVCjáofereceessesuporteparanós.
Precisamosapenasensiná-loqueagoraeletemquedecidirqualformatore-
tornarbaseadono Accept.
ContentNegotiatingViewResolver
Para ensinar o Spring MVC sobre qual formato ele
deve retornar, vamos usar um novo tipo de ViewResolver, o
ContentNegotiatingViewResolver.
...
public class AppWebConfiguration {
...
@Bean
public ViewResolver contentNegotiatingViewResolver(
ContentNegotiationManager manager) {
List<ViewResolver> resolvers =
new ArrayList< ViewResolver>();
resolvers.add(internalResourceViewResolver());
resolvers.add(new JsonViewResolver());
ContentNegotiatingViewResolver resolver =
new ContentNegotiatingViewResolver();
resolver.setViewResolvers(resolvers);
resolver.setContentNegotiationManager(manager);
return resolver ;
}
}
Perceba que criamos uma lista com implementações de
ViewResolver diferentes e depois criamos o objeto do tipo
ContentNegotiatingViewResolver e passamos a lista. Basica-
146

## Página 154

CasadoCódigo Capítulo10. Respondendomaisdeumformato
mente,vocêpodecriaro ViewResolverquevocêquiser,masvamosficar
narealidade,retornar HTML, JSONe XMLjávaisersuficiente,quasesempre.
Outrodetalheimportanteéque,paralidarcompáginasnormais,apro-
veitamosométodo internalResourceViewResolverquejáretornao
objetoresponsávelpelasJSPs.Jáoresponsávelportrataro JSONvamoster
quecriar,poisoSpringMVCnãodisponibilizaumporpadrão.
package br.com.casadocodigo.loja.viewresolver;
...
public class JsonViewResolver implements ViewResolver {
@Override
public View resolveViewName(String viewName, Locale locale)
throws Exception {
MappingJackson2JsonView view =
new MappingJackson2JsonView();
view.setPrettyPrint(true);
return view;
}
}
Oimportanteéquedevemosretornarumobjetodotipo View, que
efetivamenteseráresponsávelporescreverarespostanocliente. Nonosso
caso, estamos aproveitando a classeMappingJackson2JsonView, que
jáestádisponívelnoprojeto, desdequeadicionamosasdependênciasdo
Jackson,nocapítuloanterior. Comonãovamosdirecionarparanenhum
arquivo, não é necessário o uso do parâmetro que indica o nome da
view. Apenascomoinformação, existeumpostnoblogdoSpringsobre
estemesmoassunto, bastaseguirolink: http://spring.io/blog/2013/06/03/
content-negotiation-using-views/.
Pronto,agoraonossomesmométodoécapazderetornarformatosdife-
rentesemfun çãodotipo.Parafacilitaraindamais,oSpringMVCjásuporta
quevocêdefinaoformatoquevocêqueratravésdaprópriaURL.Casovocê
queiraforçaroretornoem JSONpelonavegador,bastaqueacesseaURL
147

## Página 155

10.3. Curiosidadesobreoobjetoaserserializado CasadoCódigo
comaextensão .json. Porexemplo,http://localhost:8080/casadocodigo/
produtos.json.Omesmovalepara HTMLeoutrosformatosquevocêqueira
suportar.
10.3 C uriosidade sobre o objeto a ser seriali-
zado
Onossométododelistagemretornaumobjetodotipo ModelAndView,
dentrodoqualpodemosadicionarquantosobjetosquisermosparaquesejam
usadosnaview.Comoqueoserializadorde JSONsabequaldestesobjetos
escolher?
Amaneirapadrãoéiterarportodasaschavesdo ModelAndViewegerar
o JSONparacadaumdosobjetosencontrados. Casovocêqueiramudar
isso,especificandoumadeterminadachave,épossívelinvocarummétodode
configuração.
@Override
public View resolveViewName(String viewName, Locale locale)
throws Exception {
MappingJackson2JsonView view = new MappingJackson2JsonView();
view.setPrettyPrint(true);
//define a chave
view.setModelKey("products");
return view;
}
Dessaforma,estamosfor çandoo MappingJackson2JsonViewaigno-
rarasoutraschaves.Éimportantenotarqueessecomportamentodeanalisar
todososobjetosdo ModelAndViewnãoéopadrão.Oserializadorde XML,
baseadonaespecificaçãodoJAX-B,buscapeloprimeiroobjetocompatível!
10.4 C onclusão
Nestecapítulo,foiabordadoumtemaqueestáemevidência:integraç ãode
sistemasviaREST.SuportaroContentNegotiationéfundamentalparavocê
darflexibilidadeàsaplicaçõesclientessobrequalformatoelaspreferem.Um
148

## Página 156

CasadoCódigo Capítulo10. Respondendomaisdeumformato
outropontoimportantefoiousodaannotation @ResponseBody, elaé
muitoútilquandovocêquiserqueoretornodométodojásejaocorpoda
resposta. Sónãoficamoscomelaporquequeríamossuportaroretornoem
HTMLe,paraisso,tivemosqueusero ModelAndViewparaindicarapágina
quedeveriaserusada.
Umaannotationquenãoabordamos,masquetambémpodeserútil,é
@RestController. Bastavocêcolocaremcimadoseucontrollersempre
quetiverumaclasseondetodososmétodosdevemusaroretornodireta-
mentecomocorpodaresposta.Casoonossocontrollersóretornasse JSON
ou XML,podíamosterfeitoissoenospoupadodeescrever @ResponseBody
emtodosmétodos.
149

## Página 158

Capítulo11
Protegendoaaplicação
Atéagora,todasasURLsdonossosistemaestãoacessíveisportodososusuá-
rios.Algumasatésãoliberadas,comoaquelevaparapáginainicial,quedeve
exibirtodososlivros. SóquetemosalgumasURLsquenecessitamdeum
usuáriologado,comoaquecadastraosnovoslivroseadecheckout.
Podemosatéimplementartodaessapartedeseguran çanamão, mas
comojávemsendofeitonodecorrerdolivro,vamosusarummódulodo
Springqueimplementaboapartedoqueagenteprecisa.Ébomsemprelem-
brarqueimplementarumaestratégiadeseguran çanãoétrivial.Alémdefor-
çarologinparaalgumasURLs,énecessárioterpreocupaçãocompelomenos
maisalgunsitens.
• QuaisperfispodemacessarasURLs,tambémconhecidocomoautori-
zação;
• URLsacessadasporváriosperfis,mascomtrechosdepáginarestritos;

## Página 159

11.1. ConfigurandooSpringSecurity CasadoCódigo
• Fontesdedadosdiferentespararealizaçãodelogin.
11.1 C onfigurando o Spring Security
Paraconseguirmosusarasclassesdo Spring Security,precisamosadicionar
maisalgumasdependênciasaonossoprojeto. Porisso,vamosalteraroar-
quivo pom.xmldenovo.
...
<dependencies>
<!-- Spring security -->
<dependency>
<groupId>org.springframework.security</groupId>
<artifactId>spring-security-config</artifactId>
<version>4.0.0.M2</version>
</dependency>
<dependency>
<groupId>org.springframework.security</groupId>
<artifactId>spring-security-taglibs</artifactId>
<version>4.0.0.M2</version>
</dependency>
<dependency>
<groupId>org.springframework.security</groupId>
<artifactId>spring-security-web</artifactId>
<version>4.0.0.M2</version>
</dependency>
<dependency>
<groupId>org.springframework.security</groupId>
<artifactId>spring-security-core</artifactId>
<version>4.0.0.M2</version>
</dependency>
</dependencies>
<repositories>
<repository>
<id>spring-milestones</id>
<name>Spring Milestones</name>
<url>http://repo.spring.io/milestone</url>
152

## Página 160

CasadoCódigo Capítulo11. Protegendoaaplicação
<snapshots>
<enabled>false</enabled>
</snapshots>
</repository>
</repositories>
AversãoestáveldoSpringSecurityaindaéa3,masjávamosusara4
paragarantircompatibilidadecomosoutrosmódulosquejáestamosuti-
lizando. Comoaversão4aindaestáemfasedeconstruç ão,temosapenas
acessoaos milestones. Porcontadisso,fomosobrigadosaadicionarmais
umrepositório,paraqueoMavenconsigabuscartodosos jarsnecessários.
Comoonossoprojetofoiimportadocomo Maven project,o classpathjáé
atualizadoemfun çãodecadaalteraçãoquefazemosnoarquivo.Casovocê
tenhaimportadocomoprojetonormal,lembre-sesempredefazerum mvn
eclipse:eclipse.
Configuração do filtro
Toda lógica de segurança do Spring Security é iniciada na classe
FilterSecurityInterceptor,queéumfiltrodaespecificaç ãodeSer-
vlets.Precisamosapenasconfigurarparaqueestefiltrosejacarregado.
package br.com.casadocodigo.loja.conf;
//imports
public class SpringSecurityFilterConfiguration
extends AbstractSecurityWebApplicationInitializer{
}
Aquiusamosamesmaestratégiadaclasse ServletSpringMVC.As
duas,nofim,implementamainterface WebApplicationInitializer,
queécarregadapeloSpringparafazeroregistrodosServlets,filtrosetudo
relativoàespecificaçãodeServlets.Casonãoselembre,jácomentamossobre
elanosegundocapítulodolivro.
Sóque,emvezdeimplementardiretamenteainterface,herdamosda
classe AbstractSecurityWebApplicationInitializer,quejávem
153

## Página 161

11.2. Garantindoaautenticação CasadoCódigo
prontanoSpringSecurityefaztodootrabalhoderegistroparaagente.
Pronto,ofiltrojáestáconfigurado!
11.2 Garantindo a autenticação
Casovocêtenhafeitoaconfiguraçãoinicialejátentenavegarpelaaplicaç ão,
vaiperceberquetodasasURLsaindaestãoliberadas.Odetalheéqueofiltro
jáestálá,masnãoensinamosnadaparaeleainda.
package br.com.casadocodigo.loja.conf;
//imports
@EnableWebSecurity
public class SecurityConfiguration
extends WebSecurityConfigurerAdapter{
}
Aqui herdamos da classeWebSecurityConfigurerAdapter, que
já fornece toda a infraestrutura pronta para começarmos a fazer nos-
sas configurações de segurança. Além disso, utilizamos a annotation
@EnableWebSecurity,quedevesercolocadaemcimadasclassesdeconfi-
guraçãodoSpringSecurityresponsáveisporefetivamentecontrolarasregras
deacesso.Essaannotationfazcomqueoutroscomponentessejamcarrega-
dos.Seguemalgunsexemplos.
•SecurityExpressionHandler,responsávelporavaliaralinguagemes-
pecíficadecontroledeseguran ça,aindavamospassarporela.
•WebInvocationPrivilegeEvaluator, responsável por verificar se os
usuáriostemacessosaosendere ços.
Nofim,podemosfazertudoissonamão.Oproblemaéquegastaríamos
tempoconfigurandoenquantopoderíamosestarresolvendooproblemada
aplicação,queécontrolaroacesso.Umúltimopontonecessárioéinformar
queessaclassedevesercarregadaquandonossaaplicaç ãoforiniciada.Vamos
fazerissonaclasse ServletSpringMVC.
154

## Página 162

CasadoCódigo Capítulo11. Protegendoaaplicação
@Override
protected Class<?>[] getRootConfigClasses() {
return new Class[]{SecurityConfiguration.class};
}
@Override
protected Class<?>[] getServletConfigClasses() {
return new Class[]{AppWebConfiguration.class,
JPAConfiguration.class};
}
Antestínhamosusadoométodo getServletConfigClasseseagora
fomosobrigadosausarométodo getRootConfigClasses.Oproblemaé
queofiltrodoSpringSecurityécarregadoantesdoServletdoSpringMVC,
logo,precisamosqueosobjetosdeconfiguraçãorelativosaeleestejamdispo-
níveisantes.Éjustamenteparaissoqueserveo getRootConfigClasses,
elefazcomqueasclassessejamlidasecarregadasdentrodeum Listener
queélidoquandooservidorsobe. NocasodoSpringMVC,essaclasseé
a ContextLoaderListener.
Agora,semfazermaisnada,jáadicionamosanecessidadedeautenticação
atodasasURLs.Casoalgumusuáriotenteacessarqualquerendere ço,elevai
serredirecionadoparaumateladelogin.Oúnicoproblemaé:ondefoique
criamosessasregrasedeondeveioessateladelogin?
Customizando as regras de acesso
Como a gente não fez nada, o Spring Security usou o método
configure,quejáexistenaclasse WebSecurityConfigurerAdapter,
parasaberquaiseramasnossasconfiguraçõesdecontroledeacesso.
protected void configure(HttpSecurity http) throws Exception {
http.authorizeRequests()
.anyRequest().authenticated()
.and()
.formLogin().and()
.httpBasic();
}
155

## Página 163

11.2. Garantindoaautenticação CasadoCódigo
Oobjetodotipo HttpSecurityéopontodeentradaparaquepossa-
moscustomizarasregrasdeautenticaçãoeautorização.Existemváriosmé-
todossendoinvocadosnessetrechodecódigo,vamossóentenderofluxo
umpoucomais.Ométodo authorizeRequests()éoquenosretornao
objetoondepodemosconfigurarasregrasdeacessoemsi.Logoapósasua
invocação,dizemosquetodorequest( anyRequest)temqueserfeitopor
alguémautenticado( authenticated).Ométodo formLoginindicaque
queremosquenossosistemasuporteautenticaçãobaseadaemumformulário
comum.Oúltimométodo,o httpBasic,indicaquesuportamostambém
omodelodeautenticação,demesmonome,providopelopróprioprotocolo
HTTP.Fiqueatentoaométodo and(),eleserveparairmosvoltandoaoob-
jetodotipo HttpSecurity,paraqueadicionemosasconfiguraçõesneces-
sárias.Aindavamosmexerbastantenessaconfiguração,paradarmossuporte
atodasasnossasnecessidades.
EssaimplementaçãoéaquevempordefaultnoSpringSecurity,comoela
obrigatodorequestaserautenticado,nãoconseguimosnemmaisacessara
listagemdelivros.
Agora,antesdemaisnada,vamoscolocarasconfiguraçõesnecessáriasde
autenticaçãoeautorizaçãoparanossosusuários.
@Override
protected void configure(HttpSecurity http) throws Exception {
http.authorizeRequests()
.antMatchers("/produtos/form").hasRole("ADMIN")
.antMatchers("/shopping/**").permitAll()
.antMatchers(HttpMethod.POST,"/produtos").hasRole( "ADMIN")
.antMatchers("/produtos/**").permitAll()
.anyRequest().authenticated()
.and().formLogin();
}
Ocódigoéquasequeautoexplicativo.Vamospegaralgunstrechospara
darumaolhada.
antMatchers ("/produtos/form").hasRole("ADMIN")
Estamosdizendoque,alémdeestarlogado,ousuárioprecisaser ADMIN
paraacessaresteendere çodanossaaplicação.Umoutrocasointeressante:
156

## Página 164

CasadoCódigo Capítulo11. Protegendoaaplicação
.antMatchers(HttpMethod.POST,"/produtos").hasRole( "ADMIN")
Casooendere ço/produtossejaacessadoatravésdoverbo POST,só
liberamosacessocasotenhasidodisparadoporumusuáriocomperfil AD-
MIN.Umúltimoquevaleaobservação:
.antMatchers("/produtos/**").permitAll()
Aquiestamosdizendoquetodososoutrosendere çosquecomecemcom
/produtosestãoliberados.Ométodo antMatcherrecebeumaexpressão
regularnomesmoestilosuportadopelaferramenta ANT,famosanomundo
Javanapartedebuilds.
ApósasconfiguraçõesdeURLs,informamosquetodoorestosóestálibe-
radocasoousuárioestejanomínimoautenticado.Fiqueatentoparaaordem
dasinvocações,elaéimportante!Primeiro,façaasrestriçõese,depois,libere
todooresto. OSpringSecurityverificaasrestriçõesnaordememqueelas
foramcadastradas.Casovocêadicionearegraquebloqueiatudonoinícioda
configuração,todasasURLsficarãobloqueadas.
11.3 C onfiguração da fonte de busca dos usuá-
rios
OsacessosàsnossasURLsjáestãodevidamenteconfigurados,entretanto,
ninguémaindaconseguefazerologinnanossaaplicaç ão. Precisamosen-
sinar ao Spring Security de onde ele deve buscar os usuários para apli-
car as nossas regras. Visando permitir implementar a busca da melhor
maneiraparacadaaplicação,elesdisponibilizaramumainterfacechamada
UserDetailsService. Vamosdarumaolhadaemcomovaificarnossa
classedeconfiguraçãodepoisdetermosimplementadoainterface.
@EnableWebSecurity
public class SecurityConfiguration
extends WebSecurityConfigurerAdapter{
....
@Autowired
157

## Página 165

11.3. Configuraçãodafontedebuscadosusuários CasadoCódigo
private UserDetailsService users;
@Override
protected void configure(AuthenticationManagerBuilder auth)
throws Exception {
auth.userDetailsService(users).
passwordEncoder(new BCryptPasswordEncoder());
}
Percebaquevamosreceberinjetadajustamenteaimplementaçãodainter-
facequeaindavamoscriar.Depoisdisso,usamosumasobrecargadométodo
configurequerecebeum AuthenticationManagerBuilder,objetoque
nospermiteassociarumnovo UserDetailsServiceaoSpringSecurity.
Alémdisso,aindaforçamosqueasenhasejamantidautilizandoumalgoritmo
dehash;escolhemosoBCrypt.Poderiamexistirvárioscapítulossomentede-
dicadosaalgoritmosdehash,jáqueestesformamumavastaáreadeestudo.
Aquinolivro,vamosnosrestringirsomenteausaroBCrypt,queaprópria
documentaçãodoSpringSecurityestimulaquesejausado.
Criando o nosso UserDetailsService
Nocasodonossosistema,pararecuperarumusuárioatravésdologin,
vamossimplesmentecriarumDAO.
package br.com.casadocodigo.loja.daos;
//imports
@Repository
public class UserDAO implements UserDetailsService{
@PersistenceContext
private EntityManager em;
@Override
public UserDetails loadUserByUsername(String username)
throws UsernameNotFoundException {
String jpql = "select u from User u
158

## Página 166

CasadoCódigo Capítulo11. Protegendoaaplicação
where u.login = :login";
List<User> users = em .createQuery(jpql,User.class)
.setParameter("login", username).getResultList();
if(users.isEmpty()){
throw new UsernameNotFoundException
("O usuario "+username+" não existe");
}
return users.get(0);
}
}
"
Nossométodoébemcomum:simplesmenterealizamosumaqueryede-
vemosretornarumusuárioencontrado,ouumaexceptionindicandoocon-
trário. Percebaqueonomedométodoé loadUserByUsername,justa-
menteoqueainterfacenosobrigaimplementar.Umaoutraquestãointeres-
santeéqueelenãorecebeasenhacomoargumento,porqueserá?Oprincipal
motivoéparavocênãoterquelidarcomoprocessodeaplicarohashnase-
nhaantesdefazeraconsulta.VocêsimplesmentebuscapelologineoSpring
Securityvaiverificarseasenhacadastradabatecomasenhacomquefoien-
viadapeloformulário.
Aindaemrelaçãoàassinaturadométodo loadUserByUsername,outro
pontoquechamaaaten çãoéoretorno. Elenosfor çaaretornarumobjeto
queimplementaainterface UserDetails.E,sepensarmosbem,faztodo
osentido. Comoobjetoquerepresentaousuáriologadonamão,comoo
SpringSecurityiasaberqualeraasenhadele?Equaisperfisestãoassociados
aele?Éparaissoqueserveainterface:paradefinirosmétodosqueelepoderá
invocarerecuperarestasinformações.
Parasatisfazê-lo,vamoscriarnossaclasse Usereimplementarainterface
exigida.
package br.com.casadocodigo.loja.models;
//outros imports
159

## Página 167

11.3. Configuraçãodafontedebuscadosusuários CasadoCódigo
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;
@Entity
public class User implements UserDetails{
@Id
private String login;
private String password;
private String name;
@ManyToMany(fetch = FetchType.EAGER)
private List<Role> roles = new ArrayList<>();
//outros getters e setters
@Override
public String getPassword() {
return password;
}
@Override
public Collection<? extends GrantedAuthority>
getAuthorities() {
return roles;
}
@Override
public String getUsername() {
return login;
}
@Override
public boolean isAccountNonExpired() {
return true;
}
@Override
public boolean isAccountNonLocked() {
160

## Página 168

CasadoCódigo Capítulo11. Protegendoaaplicação
return true;
}
@Override
public boolean isCredentialsNonExpired() {
return true;
}
@Override
public boolean isEnabled() {
return true;
}
}
Fomosobrigadosaimplementaratémaismétodosdoqueestávamoses-
perando,vamosdarumaolhadanosmaisimportantesparaagente.
•getPassword:retornaopassworddousuário;
•getUsername:retornaologindousuário;
•getAuthorities:retornaosperfisdousuárioautenticado.
Osoutrosmétodossãoparaumcontrolemaisfino.Oimportanteé:to-
dososmétodosqueretornam booleandevemretornar trueparagarantiro
acessodousuárioàsURLsprotegidas.Casooseusistemaprecisecontrolar
renovaçãodesenhaou,porexemplo,bloqueioporinatividade,estesoutros
métodospodemserúteis.
Percebaqueométodo getAuthoritiesdeveretornarumalistadeob-
jetosqueimplementamainterface GrantedAuthority.Essaéjustamente
ainterfacequenossaclassequerepresentaoperfildeveimplementar.
package br.com.casadocodigo.loja.models;
//outros imports
import org.springframework.security.core.GrantedAuthority;
161

## Página 169

11.3. Configuraçãodafontedebuscadosusuários CasadoCódigo
@Entity
public class Role implements GrantedAuthority {
@Id
private String name;
@Override
public String getAuthority() {
return name;
}
Pronto,comambasasclassesimplementandoainterfaceesendoentida-
desgerenciadaspelaJPA,jápodemosrealizarefetivamenteologindosusuá-
rios.Apenasparafacilitar,vocêpodeexecutarosinsertsaseguirparacadas-
trarusuárioseseusperfis.
insert into Role values('ROLE_ADMIN');
insert into Role values('ROLE_COMPRADOR');
insert into User(login,name,password)
values('comprador@gmail.com',
'Alberto',
);
insert into User(login,name,password)
values('admin@casadocodigo.com.br'
,'Administrador',
);
insert into User_Role(User_login,roles_name)
values('comprador@gmail.com','ROLE_COMPRADOR');
insert into User_Role(User_login,roles_name)
values('admin@casadocodigo.com.br','ROLE_ADMIN');
Provavelmente,noseusistema,vocêvaiprecisarcadastrarnovosusuários
atravésdeumformulário.Paraaplicarohashnasenhapassadapeloformu-
láriodecadastro,lembre-sedeusaraclasse BCryptPasswordEncoder.
162

## Página 170

CasadoCódigo Capítulo11. Protegendoaaplicação
Problema com a ordem de carregamento das configurações
Casovocêtentesubiraaplicação,vaireceberaseguinteexception:
Caused by: org.springframework.beans.factory
.NoSuchBeanDefinitionException:
No qualifying bean of type
[org.springframework.security.core.userdetails
.UserDetailsService]
Elainformaquenãoconseguiuacharnenhumaimplementaç ãoparaain-
terface UserDetailsService.OproblemaéqueoDAOestáconfigurado
parasercarregadonaclasse AppWebConfigurationeelasóécarregada
nomomentodecarregamentodoServletdoSpringMVC.
@Override
protected Class<?>[] getServletConfigClasses() {
return new Class[]{AppWebConfiguration.class,
JPAConfiguration.class};
}
Precisamosqueelapasseparaométodo getRootConfigClassespara
sercarregadanoiniciodaaplicaçãoejáfazercomqueosobjetosfiquemdis-
poníveisparaseremlidospelofiltro.
@Override
protected Class<?>[] getRootConfigClasses() {
return new Class[]{SecurityConfiguration.class,
AppWebConfiguration.class};
}
@Override
protected Class<?>[] getServletConfigClasses() {
return new Class[]{JPAConfiguration.class};
}
Casotentesubiroservidordenovo,vaiverquefelizmenteoerrovaimu-
dar.
163

## Página 171

11.3. Configuraçãodafontedebuscadosusuários CasadoCódigo
Error creating bean with name 'userDAO': Injection of persistence
dependencies failed; nested exception is
org.springframework.beans.factory.NoSuchBeanDefinitionException:
No qualifying bean of type
[javax.persistence.EntityManagerFactory] is defined
Elenãoconseguecriaroobjetodotipo UserDAO,jáquenãosabecomo
criaruma EntittyManagerFactory. Éomesmoproblemadocasoan-
terior: paracriaroDAO,énecessáriaacriaçãodo EntityManager,eo
mesmosóécarregadonomomentodecriaç ãodoServlet.Vamosfazeraúl-
timaalteraçãonessaclasse!
@Override
protected Class <?>[] getRootConfigClasses() {
return new Class[]{SecurityConfiguration.class,
AppWebConfiguration.class,JPAConfiguration.class};
}
@Override
protected Class <?>[] getServletConfigClasses() {
return new Class[]{};
}
Agoratudoécarregadonoinício,ecomissoresolvemosesseproblema
chatodaordemdecarregamento.
Curioside sobre o prefixo ROLE_
Talvezoleitormaisatentoestejaseperguntandoomotivodecadastrar-
mososperfiscomoprefixo ROLE_. Paraimplementarasverificaçõesde
acesso,tantodeusuárioautenticadoquantodeautorizado,oSpringSecurity
forneceumainterfacechamada AccessDecisionVoter.Aclassepadrão,
quefazaverificaçãodosperfis,éa RoleVoter.
public class RoleVoter implements AccessDecisionVoter<Object> {
private String rolePrefix = "ROLE_";
164

## Página 172

CasadoCódigo Capítulo11. Protegendoaaplicação
public boolean supports(...){
//verifica se deve aplicar verificações
}
}
Percebaqueelafor çaousodoprefixo,éapenasumadecisãodepro-
jeto. Imaginequevocêpossacriarum AccessDecisionVotercustomi-
zadoeassociaroutropadrãointernodeperfildasuaempresa;comoqueo
RoleVoteriasabersedeviaaplicaraverificaç ãoounão?Éjustamentepara
issoqueelefor çaousodoprefixo.Vocêagoradeveestarimaginandooutra
coisa.Lánaconfiguraçãoinicial,nãofoibemassimquefizemos.
.antMatchers("/produtos/form").hasRole("ADMIN")
Ondeestáoprefixo?Équeométodo hasRolejáadicionaparaagente.
Assert.notNull(role, "role cannot be null");
if (role.startsWith("ROLE_")) {
throw new IllegalArgumentException(
"role should not start with 'ROLE_'
since it is automatically inserted.
Got '" + role + "'");
}
String role = "ROLE_" + role ;
...
Ométodo hasRolesóexisteporcontado RoleVoter.
11.4 C ross-site request forgery
Agoraquejáconseguimoslogar,podemosnavegarentreaspáginasdosis-
tema.Umproblemaacontecenahoraquetentamos,porexemplo,adicionar
umprodutoaonossocarrinhodecompras.Quandoclicamosnobotãopara
realizaraação,éretornadoostatus403,indicandoacessonegado.Aindavem
acompanhandodaseguintemensagem:
HTTP Status 403 - Invalid CSRF Token 'null' was found on the
request parameter '_csrf' or header 'X-CSRF-TOKEN'.
165

## Página 173

11.4. Cross-siterequestforgery CasadoCódigo
AsiglaCSRFsignifica Cross-Site Request Forgeryeéumtipodeataqueque
podeserfeitocontrasuaaplicação.Aideiabasicamenteéquedadospossam
serenviadosparaanossaaplicaçãosendoprovenientesdeumaoutrapágina
qualquer,abertanoseunavegador.ComoaCasadoCódigoébemfamosa,
algumoutrositepoderiaesconderumformulárionasuapáginae,quandoum
usuárioqueestivesselogadonaCasadoCódigointeragissecomessapágina
externa,elapoderiasubmeterdadoscomumvalormentirosoparaoendere ço
decheckout. Paraconseguirmaisinformações,vocêpodeacessarapágina
dopróprioSpringSecurity, http://docs.spring.io/spring-security/site/docs/4.
0.0.M2/reference/htmlsingle/#csrf.
Comofoifaladonoiniciodocapítulo,seguran çavaialémdeverificarlo-
gineperfis,eseprotegerdeataquescomoessefazpartedopacote.Aprote-
çãopadrãocontraoCSRFéfeitaatravésdageraç ãodeumnúmeroparacada
usuárioqueseloguenosistema.Apartirdisso,todo POSTqueforfeitodeve
seracompanhadodessenúmero,tambémchamadode token.Dessaforma,
pormaisqueositemaliciosocoloqueumformulárioescondido,orequestnão
vaiseracompanhadodotoken,sendoautomaticamentebanidopelanossa
aplicação.
Paraanossasorte,oSpringSecurityjáprovêaimplementaç ãoparaa
proteçãocontraoCSRF.Talvezoleitortenhapercebidoqueaprote çãojáestá
ativadaatépararequestsparaURLsquenãoestãosobprote ção.Porpadrão,o
SpringSecurityjágeraotokenapartirdoprimeirorequestdousuário,para
aaplicaçãoqueestáfazendousodomódulo. Aconsequênciadissoéquea
verificaçãodoCSRFjáéfeitaparatodo POST.Paraadicionarmosotoken,
bastaqueadicionemosoparâmetrocomotokennosnossosformulários.
<form ...>
<input type="hidden"
name="${_csrf.parameterName}"
value="${_csrf.token}"/>
</form
Avariáveldenome _csrfcontémareferênciaparaumobjetodotipo
DefaultCsrfToken. Atravésdele,temosacessoaonomedoparâmetroe
aovaloratualdotoken.Onomenomedavariávelpodesermodificado,mas
nãoénecessárionemqueescrevamosoinputemsi.Podemosimportarum
166

## Página 174

CasadoCódigo Capítulo11. Protegendoaaplicação
conjuntodetaglibsdoSpringSecurityquejápossuiatagquegeraomesmo
input.
<%@taglib uri="http://www.springframework.org/security/tags"
prefix="security" %>
...
<form ...>
<security:csrfInput/>
</form>
Asegundaop çãoébemmelhor,jáquenãoénecessárioficarlembrando
donomedavariávele,muitomenos,ficarcorrendooriscodeescrevererrado.
Casovocênãoestejacontentecomnenhumadasduas,aindapodemosoptar
porumaterceira.
AnotamosaclassedeconfiguraçãodoSpringSecuritycomaannotation
@EnableWebSecurity.Sóqueessaannotationcarregaconfiguraçõesim-
portantesparaumaaplicaçãoweb,masnãoassumequeestamosusandoo
SpringMVCcomoframeworkweb.Podemos,emvezdisso,come çarausar
aannotation @EnableWebMvcSecurity. Elacarregaosmesmoscompo-
nentesdaanterioreaindaadicionaconfiguraçõesespecíficasparaoprojeto
queutilizaoSpringMVC.UmadelaséadicionaroinputdoCSRFemto-
dososformuláriosconstruídoscomatag <form:form>. Nossaclassede
configuraçãoficariacomooexemploaseguir.
@EnableWebMvcSecurity
public class SecurityConfiguration extends
WebSecurityConfigurerAdapter{
...
}
Agorasóprecisamostrocarosnossosformulários.Vamospegarodeadi-
çãodeumprodutonocarrinho,porexemplo.Atualmente,eleestáassim:
<form action="<c:url value="/shopping"/>" method="post"
class="container">
...
</form>
167

## Página 175

11.5. Customizandomaisalgunsdetalhes CasadoCódigo
Podemossubstituí-lopelatagdegeraçãodeformuláriodoSpringMVC.
<form:form servletRelativeAction="/shopping"
cssClass="container">
....
</form:form>
Pronto,agoranãoprecisamosmaisnospreocuparemadicionaroinput
comotokendoCSRF.Debrinde,aindanãoprecisamosmaisficarusandoa
tag <c:url>.Quandoutilizamosoatributo servletRelativeAction,o
contextodaaplicaçãojáéadicionadoantesdaURL!Lembre-se,éumaótima
práticausarastagsdeformuláriodoSpringMVC,geralmenteelajávaifazer
boapartedotrabalhopadrãoparavocê,comojávimosquandodiscutimosa
validação.
11.5 C ustomizando mais alguns detalhes
Atéagoratemosusadoumateladeloginquetemsidogeradaautomatica-
mentepelopróprioSpringSecurity.Sóque,nanossaaplicaç ão,precisamos
teraop çãodecriarumatelacomacaradaCasadoCódigo.Eéclaroqueisso
nãovaiserumproblema,bastaensinarmosaoSpringSecurityqueaURLde
logindeveserdirecionadaparaumcontrollerdanossaaplicaç ão.
@EnableWebMvcSecurity
public class SecurityConfiguration extends
WebSecurityConfigurerAdapter{
@Override
protected void configure(HttpSecurity http) throws Exception{
http.authorizeRequests()
.antMatchers("/produtos/form").hasRole("ADMIN")
.antMatchers("/shopping/**").permitAll()
.antMatchers(HttpMethod.POST,"/produtos")
.hasRole("ADMIN")
.antMatchers("/produtos/**").permitAll()
.anyRequest().authenticated()
.and()
.formLogin().loginPage("/login").permitAll();
}
168

## Página 176

CasadoCódigo Capítulo11. Protegendoaaplicação
O método formLogin() retorna um objeto do tipo
LogoutConfigurer e, através dele, conseguimos trocar as configura-
çõesquevêmpordefaultparaaURLdoformuláriodelogin. Esseéo
objetivodométodo loginPage,elerecebecomoargumentoaURLque
deveserusadaparairparaateladelogin. Devemosinvocarométodo
permitAllparainformarqueesseendere çoestáliberadoparatodosos
usuários.
OJSPdatelapodiaserparecidocomoquesegue:
<%@ taglib uri="http://www.springframework.org/tags/form"
prefix="form"%>
<form:form servletRelativeAction= "/login">
<div>
<label>
User
<input type='text' name='username' value= ''>
</label>
</div>
<div>
<label>Password
<input type='password' name='password' />
</label>
</div>
<div>
<input name="submit" type="submit"
value="Login" />
</div>
</table>
</form:form>
Onomedosparâmetrosdeloginesenhatambémsãodefinidosatravésdo
LoginConfigurer.Odefaulté usernameparaologine passwordpara
asenha.Aactiondoformulárioestácomovalor /login,queéaURLque,
quandofeitoum POST,disparaoprocessodeloginpelofiltro.Ocontroller
quelevaparaessapáginaficaporsuaconta,leitor!
169

## Página 177

11.5. Customizandomaisalgunsdetalhes CasadoCódigo
URL de logout e telas de erro
Parahabilitarumendere çoquedisparaoprocessodelogoutdaaplicação
bastaqueinvoquemosométodo logout().
.formLogin().loginPage("/login").permitAll()
.and()
.logout().logoutRequestMatcher(new AntPathRequestMatcher(
"/logout"));
Pordefault,oSpringSecuritysóliberaqueologoutsejafeitoatravésde
POST,justamenteparafor çarapassagemdotokendoCSRF.Aquifizemosum
poucodiferente,porissoainvocaçãodométodo logoutRequestMatcher.
AURLpassadaparaelepodeseracessadavia GETe,mesmoassim,oprocesso
delogoutvaiseriniciado.
Outrodetalheimportanteéateladeacessonãoautorizado. Elaacon-
tecequandoousuáriologadonãotemoperfilnecessárioparaacessaraURL,
éocasodocadastrodelivros,sóusuáriosadministradorespodemacessar.
QuandoumusuáriotentaacessarumaURLdessas,oSpringSecuritygera
umretornocomostatus403,quesignifica Not Authorized.Paracustomizar
essateladeerro,bastaquefaç amosusodoarquivo web.xmldaaplicação.
<error-page>
<error-code>403</error-code>
<location> /WEB-INF/403.jsp</location>
</error-page>
Umdetalheinteressanteéqueatéagoranãotínhamosprecisadodessear-
quivo.Paraquemnãoselembra,eleéutilizadoparafazermosdiversascon-
figuraçõesrelativasànossaaplicaçãoweb,mascomoquasetudopodeser
configuradoviacódigoouannotation,eleestásendousadocadavezmenos.
ParageraroarquivopeloEclise,bastausaraop ção Generate deployment
Descriptor stub.
170

## Página 178

CasadoCódigo Capítulo11. Protegendoaaplicação
Fig.11.1:Menudegeraçãodearquivoweb.xml
11.6 E xibindo o usuário logado e escondendo
trechos da página
Umdetalhecomuméexibironomedousuáriologadonaspáginasqueele
acessadentrodosistema.Podemosfazerissousandoastaglibsdisponibiliza-
daspelopróprioSpringSecurity.Vamosalterarapágina list.jsp:
<%@ taglib prefix= "security"
uri="http://www.springframework.org/security/tags" %>
<security:authentication property= "principal" var="user"/>
Olá ${user.name}
A taglib authentication acessa o objeto do Spring Security que
guardaousuárioquefoicarregadopelo UserDetailsService.Eleimple-
mentaainterface Authentication,quepossuiométodo getPrincipal.
Porisso,passamosovalor principalparaoatributo property.Interna-
mente,ataglibvaibuscarpelo getterrelativoàpropriedade.Parapoder-
mosusá-lonorestodapágina,exportamo-loparaavariável user.
Aindaemrelaçãoaessaparte,sobrouumdetalhe.Essapáginapodeser
acessadatantoporusuárioslogadoscomoporqualqueranônimo.Casoacon-
teçaoúltimocaso,nestemomento,vamosreceberumerroinformandoque
apropriedade namenãoexiste.Pararesolverisso,vamosexibiressetrecho
apenasparausuárioslogados!
171

## Página 179

11.7. Conclusão CasadoCódigo
<sec:authorize access="isAuthenticated()">
<sec:authentication property="principal" var="user"/>
<div>
Olá ${user.name}
</div>
</sec:authorize>
Atag authorizeservejustamenteparaexibirumtrechodepáginaape-
nassealgumacondiçãoforatendida. Nessecaso,estamosverificandoseo
usuárioestálogado.Oatributo accessrecebealgumasexpressõesquesão
suportadaspeloSpringSecurity. Foiusadaa isAuthenticated(),mas
podiamserváriasoutras.Outramuitocomumé hasRole(...),quegeral-
menteéusadaquandosedesejarestringircertotrechodapáginaapenaspara
algunsperfis.
<sec:authorize access="hasRole('ROLE_ADMIN')">
<li><a href="${spring:mvcUrl('PC#form').build()}">
Cadastrar novo produto</a>
</li>
</sec:authorize>
Paraalistacompleta,vocêpodeacessaradocumentaç ãodoSpringSe-
curity.Casoprecise,sigaestelink: http://docs.spring.io/spring-security/site/
docs/4.0.0.M2/reference/htmlsingle/#el-access.
11.7 C onclusão
Nestecapítulo,vimososuficientedoSpringSecurityparaamaioriadasapli-
cações.EsteéumdosmelhoresmódulosdoSpringeháaindaváriasoutras
configuraçõespossíveis.Outropontoimportanteéqueeleébemextensível,
talvezvocêselembredasinterfacesqueforammostradasduranteocapítulo.
Casovocêprecisedealgumdetalheespecífico,pesquiseprimeirodentrodo
frameworkantesdefazerumasoluçãocaseira.
Comoocapítulofoimuitoextenso,dêumapausaparatomarumaágua
eprocessartudoquevocêleu.Ospróximoscapítulos,apesardeimportantes,
sãomaissimplesdeserementendidos.
172

## Página 180

Capítulo12
Organizaçãodolayoutem
templates
Jáimplementamosalgumasdasfuncionalidadesqueexistemdentrodosis-
temarealdaCasadoCódigo.Umapartecomquenãonospreocupamosaté
agoraéemrelaçãoaolayoutdaaplicação.Sóqueatémaisimportantequeo
layoutécomovamosorganizá-lo.Porexemplo,atualmente,entreaspáginas
quejáimplementamos,temosadeexibiç ãododetalhedeumlivroeaque
exibeosprodutosdocarrinhodecompras.Olhandocomaten çãoparaelas,
vamosperceberqueambaspossuemomesmoheaderefooter.
<header id="layout-header">
...
</header>
<nav class="categories-nav">

## Página 181

CasadoCódigo
...
</nav>
<!-- resto da página-->
<footer id="layout-footer">
...
</footer>
Aquitemosoproblemaclássicoderepetição.Casoalgumamudan çaseja
necessárianessestrechos,vamosterquesaircaç andoemtodasaspáginas.
Umamaneiracomumderesolveressasituaç ãoéutilizandoosistemade in-
cludesquejáexistenasJSPs.
<!doctype html>
<!--[if lt IE 7]><html class="no-js lt-ie9 lt-ie8 lt-ie7"
lang="pt">
<![endif]-->
<!--[if IE 7]>
<html class="no-js lt-ie9 lt-ie8" lang="pt">
<![endif]-->
<!--[if IE 8]><html class="no-js lt-ie9" lang="pt"><![endif]-->
<!--[if gt IE 8]><!-->
<html class="no-js" lang="pt">
<!--<![endif]-->
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta name="viewport"
content="width=device-width, initial-scale=1,
maximum-scale=1">
<title>${title}</title>
</head>
<body class="${bodyClass}">
<%@include file ="/WEB-INF/header.jsp" %>
<!-- resto da página -->
174

## Página 182

CasadoCódigo Capítulo12. Organizaçãodolayoutemtemplates
<%@include file="/WEB-INF/footer.jsp" %>
Atéisolamosoheadereofooter,sóquesobrouesseiniciodedeclaraç ão
doHTML.Eaívocêpodepensar“nãotemproblema,ésócriarmaisuma
includeeissotambémvaiestarisolado”. Sóqueaíéqueentraoproblema:
paraumapessoanovamontarumapágina,seguindoopadrãodosistema,
elatemquesaberdetodasessa includeseaindatemquesaberaordem! A
tendênciaésópiorar.
12.1 T emplates
Paraamenizaresseproblema,aespecificaçãodeJSPjápensouemumasolu-
ção.Aideiaéquepossamoscriarummodelodepáginaquepossaserutilizada
portodasasoutraspáginas.
<%@taglib tagdir="/WEB-INF/tags" prefix="customTags"%>
<customTags:pageTemplate>
<section class="container middle">
<h2 id="cart-title">Seu carrinho de compras</h2>
<table id="cart-table">
<colgroup>
<col class="item-col">
<col class="item-price-col">
<col class="item-quantity-col">
<col class="line-price-col">
<col class="delete-col">
</colgroup>
<thead>
<tr>
<th class="cart-img-col"></th>
<th width="65%" >Item</th>
<th width="10%" >Preço</th>
<th width="10%" >Quantidade</th>
<th width="10%" >Total</th>
<th width="5%"></th>
</tr>
175

## Página 183

12.1. Templates CasadoCódigo
</thead>
<tbody>
...
</customTags:pageTemplate>
Aindanãosepreocupecomatag masterPage,vamosresolvê-ladaqui
apouco.Vamosfocarnaestruturadapágina.Nãoprecisamosnospreocupar
commuitacoisa,apenasemadicionarumatagqueindicaquequeremosusar
ummodelodepágina.Aideiaéqueessatagdefinaoheader,footer,outros
trechosemcomumeapenasrecebacomoparâmetroocorpodapáginaespe-
cífica.Eseaequipedefrontquiserreformularaestruturadapáginaemudar
aordemdosmenus,ondedevemosmudar?Apenasnotemplate!
Percebaqueimportamosastagsapontandoparaumapastaem WEB-INF.
Diferentedoquefizemosnocapítulodevalidação,vamoscriarumatagquase
comosefosseumaJSP,tambémconhecidacomo Tag File. Nessecaso,
vamoschamaranossatagde pageTemplate.tag. Aespecificaçãonos
obrigaadeixarosarquivos .tagdentrodapastatags.
<%@taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt"%>
<%@ taglib
uri="http://www.springframework.org/tags/form" prefix= "form"%>
<%@taglib uri="http://www.springframework.org/tags"
prefix="spring" %>
<!doctype html>
<!--[if lt IE 7]>
<html class="no-js lt-ie9 lt-ie8 lt-ie7" lang="pt">
<![endif]-->
<!--[if IE 7]>
<html class="no-js lt-ie9 lt-ie8" lang="pt">
<![endif]-->
<!--[if IE 8]><html class="no-js lt-ie9" lang="pt"><![endif]-->
<!--[if gt IE 8]><!-->
<html class="no-js" lang="pt">
<!--<![endif]-->
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
176

## Página 184

CasadoCódigo Capítulo12. Organizaçãodolayoutemtemplates
<meta name="viewport"
content="width=device-width, initial-scale=1,
maximum-scale=1">
<title>Titulo da página</title>
</head>
<body class="classeDoBody">
<%@include file="/WEB-INF/header.jsp" %>
<jsp:doBody/>
<%@include file="/WEB-INF/footer.jsp" %>
</body>
</html>
ÉquaseumaJSP,aúnicadiferen çaéqueelapodeserreaproveitadacomo
umatag.Percebaquecome çamosoHTMLeusamosas includesparadeixara
páginaorganizada.Agrandejogadaestánousodatag <jsp:doBody>,ela
queéaresponsávelporcapturarocorpopassadocomoparâmetroeutilizá-lo
dentrodanossaestrutura.
Outropontoimportanteéquetodapáginadefineumtítuloeumaclasse
quedeveserusadanatag body.Comocriamosumatag,nadanosimpede
dedeclararatributosparaela.
<%@attribute name="title" required="true" %>
<%@attribute name="bodyClass" required="true" %>
...
<title>${title}</title>
...
<body class="${bodyClass}">
<%@include file="/WEB-INF/header.jsp" %>
177

## Página 185

12.2. Deixandootemplateaindamaisflexível CasadoCódigo
<jsp:doBody/>
<%@include file="/WEB-INF/footer.jsp" %>
</body>
Existemoutrasbibliotecasquepodemserusadasparaacriaç ãodetem-
plates,comooFreemarker,Sitemesh,TileseVelocityeoSpringMVCtem
integraçãocomtodaselas. Opontoéqueamesmafuncionalidadejáésu-
portadapelaJSPe,poressemotivo,esteautorprefereficarcomoquejávem
prontonalinguagem.
12.2 D eixando o template ainda mais flexível
Umdetalhecomoqualéumpoucomaiscomplicadodelidaréquecertas
páginasprecisamdeumtrechoextradeJavascriptlogoantesdofechamento
dobody.Porexemplo,apáginadelistagemdositensdocarrinhoexigequeo
seguintetrechosejacolocado:
<script>
$(function () {
$('#checkout').click(function () {
_gaq.push([ '_trackPageview',
'/checkout/finalizaCompra' ]);
});
$('.book-suggest').click(function() {
var book = $(this).data('book');
_gaq.push([ '_trackEvent', 'Recomendação',
'Livro', book ]);
});
});
</script>
<script>
$(function () {
$('a[href^="http"]').not('.dont-track')
.filter(function(index) {
var ccb = $(this).attr('href')
178

## Página 186

CasadoCódigo Capítulo12. Organizaçãodolayoutemtemplates
.indexOf("casadocodigo.com.br");
if (ccb == -1)
ccb = $(this).attr('href').indexOf("localhost");
return ccb != 7 && ccb != 11;
}).click(function(event) {
var domain = this.href;
domain = domain.substring(7);
domain = domain.substring(0, domain.indexOf('/'));
if (domain.substring(0, 4) == 'www.')
domain = domain.substring(4);
_gaq.push([ '_trackPageview', '/LinkExterno/' +
this.href ]);
});
});
</script>
Paracontornaresseproblema,podemosdizerquenossatagpodereceber
fragmentosextrasdepáginas.
<%@attribute name="title" required="true" %>
<%@attribute name="bodyClass" required="true" %>
<%@attribute name="extraScripts" fragment="true" %>
<body class="${bodyClass}">
<%@include file="/WEB-INF/header.jsp" %>
<jsp:doBody/>
<%@include file="/WEB-INF/footer.jsp" %>
<jsp:invoke fragment="extraScripts"/>
</body>
</html>
Agoraqualquerpáginaqueprecisepodepassaressefragmentoextra.
179

## Página 187

12.3. Conclusão CasadoCódigo
<customTags:pageTemplate bodyClass= "cart" title="${title}" >
<jsp:attribute name="extraScripts" >
...
</jsp:attribute>
<jsp:body>
<!-- Resto do corpo da página-->
</jsp:body>
</customTags:pageTemplate>
Atag <jsp:attribute>éutilizadaparaindicarotrechoquedeve
serusadopelatag <jsp:invoke>. Vocêpodeterquantosfragmentosfo-
remnecessários,tudovaidependerdacomplexidadedoseutemplate.Ape-
nasparacompletar,algunsdetalhesimportantes. Quandofazemosusodo
attributesomosobrigadosausaratag <jsp:body>parapassarocorpo,
nãopodemosmaisdeixá-lolivre.Umúltimopontoéaordem:énecessário
queo <jsp:body>sejaaúltima.
12.3 C onclusão
Estecapítulofoibemrápido, apenasorganizamosumpoucomaisnosso
layout.NãotevenadaavercomoSpringMVCemsi.Mesmoassiméimpor-
tante,jáqueastelascompõemumapartefundamentaldequalqueraplicaç ão.
Nãopareagora,jácomeceopróximocapítuloparaquepossamosfazercom
quenossastelasfalemdiversaslínguas.
180

## Página 188

Capítulo13
Internacionalização
Atéestemomento,todosostextosdaaplicaç ãoestãoescritosdiretamente
naspáginas. Porexemplo,vamosanalisaromenudenavegaç ãoda include
quecontémoheaderdoprojeto.
<ul class="container">
<li class="category">
<a href="http://www.casadocodigo.com.br">Home</a>
<li class="category"><a href="/collections/livros-de-agile">
Agile </a>
<li class="category">
<a href="/collections/livros-de-front-end">Front End</a>
<li class="category"><a href="/collections/livros-de-games">
Games </a>
<li class="category"><a href="/collections/livros-de-java">
Java </a>

## Página 189

13.1. Isolandoostextosemarquivosdemensagens CasadoCódigo
<li class="category"><a href="/collections/livros-de-mobile">
Mobile </a>
<li class="category"><a
href="/collections/livros-desenvolvimento-web"> Web </a>
<li class="category">
<a href="/collections/outros"> Outros </a>
Todosostextosdaaplicaçãoestãoescritosdiretamentenapáginae,em
geral,talvezissonãosejaumproblema.Entretanto,aCasadoCódigojátem
asuaversãointernacional,aCodeCrushing.Elastêmomesmolayoutesó
mudamemumacoisa:todosostextossãoescritoseminglês.
13.1 I solando os textos em arquivos de mensa-
gens
Casocontinuemoscomaestratégiadeescreverostextosdiretamentenapá-
gina,teríamosqueduplicarcadaumadelas. Paraconseguirmos internaci-
onalizarnossaaplicação,vamosterqueisolarostextosnonossoarquivo
properties.
...
navigation.category.agile = Agilidade
navigation.category.front_end = Front end
navigation.category.games = Jogos
navigation.category.java = Java
navigation.category.mobile = Desenvolvimento móvel
navigation.category.web = Web
navigation.category.others = Outros
Mantivemosaschavesquejáexistiamláeadicionamosasnovas,referen-
tesaomenu.Anomenclaturaemumarquivo propertiessempreéfonte
dediscussão.Aquiestamosseguindoomaisbásico:dividimososgruposcom
o .eusamos _parasepararonomedoitememsi.Agoraquejáisolamos
ostextosnoarquivo messages,podemosusaraschavesnasnossaspáginas
etags.
182

## Página 190

CasadoCódigo Capítulo13. Internacionalização
<%@taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt"%>
<%@taglib uri= "http://www.springframework.org/tags"
prefix="spring" %>
...
<nav class="categories-nav">
<ul class="container">
<li class="category">
<a href="http://www.casadocodigo.com.br">Home</a>
<li class="category">
<a href="/collections/livros-de-agile">
<fmt:message key="navigation.category.agile"/>
</a>
<li class="category">
<a href="/collections/livros-de-front-end">
<fmt:message key="navigation.category.front"/>
</a>
<li class="category">
<a href="/collections/livros-de-games">
<fmt:message key="navigation.category.games"/>
</a>
<li class="category">
<a href="/collections/livros-de-java">
<fmt:message key="navigation.category.java"/>
</a>
<li class="category">
<a href="/collections/livros-de-mobile">
<fmt:message key="navigation.category.mobile"/>
</a>
<li class="category">
<a href="/collections/livros-desenvolvimento-web">
<fmt:message key="navigation.category.web"/>
</a>
<li class="category">
<a href="/collections/outros">
<fmt:message key="navigation.category.others"/>
</a>
</ul>
</nav>
183

## Página 191

13.2. Accept-Languageheader CasadoCódigo
Percebaqueusamosatag <fmt:message>.OSpringjádisponibilizaas
chavesnocontextodaJSTLparaquepossamoscontinuarusandoamesma
tag.Outraop çãoseriausaratagdopróprioSpring.
<spring:message code="navigation.category.agile"/>
AdiferençaéqueatagdoSpringjátemmaisalgumasop ções,comoo
valordefaulteformamaisfácildepassarparâmetros.
13.2 A ccept-Language header
Atéagoratemosapenasoarquivo messages.propertiescomostex-
tosemportuguês. Sóqueprecisamossuportarasmensagenstambémem
inglês. Parafazerisso,precisamoscriaroarquivocomaextensãodalo-
calizaçãoquequeremossuportar. Porexemplo, podemoscriaroarquivo
messages_en_US.properties.
shoppingCart.title = Shopping cart
navigation.category.agile = Agile
navigation.category.front = Front end
navigation.category.games = Games
navigation.category.java = Java
navigation.category.mobile = Mobile
navigation.category.web = Web
navigation.category.others = Others
Podemostambémcriaroarquivocomaextensão _pt.properties,
parasuportaroportuguêspadrão.Eagoraaparteboa:nãoprecisamosfazer
maisnada! Bastaquefaçamosatrocadalínguapadrãodonavegador,que
oarquivocorretovaiserescolhido. Aperguntaqueficaé: comooSpring
descobrequalidiomaonavegadorprefere?
184

## Página 192

CasadoCódigo Capítulo13. Internacionalização
Fig.13.1:Headercomaop çãodelíngua
Arespostaestánocabe çalhodarequisiçãoHTTP.Percebaquetemuma
chavechamada Accept-Languageeénelaquevêmaslínguasprediletasdo
seuusuário.Nocasodonavegadordoautordestelivro,estácomoportuguês.
Tantoqueaprimeiraop çãoéo pt,mascasonossosistemanãosuporteesse
idioma,elefalaqueprefereo en-US.Carregaroarquivodemensagensem
funçãodalínguadonavegadoréamaneirapadrãodeoSpringMVClidar
comainternacionalização.
13.3 P assando parâmetros nas mensagens
Outrasituaçãomuitocomumnomomentodeexibirasmensagensinterna-
cionalizadaséanecessidadedequeamensagemsejaconstruídadinamica-
mente. Porexemplo,napáginadelistagemdelivros,queremosdarboas-
vindasaousuárioqueacaboudelogarnosistema.
Olá ${user.name}
Vamosdeixarinclusiveessamensageminternacionalizada.Paraisso,va-
mosacrescentaraentradanoarquivodemensagens.
users.welcome = Olá {0}
Pararepresentarosparâmetros,usamososíndices. Estatécnicajávem
suportadaporpadrãonosuporteàinternacionalizaç ãopresentenopróprio
Java.Agora,parausarnapágina,podemosusaratagdoSpring.
<spring:message code="users.welcome" arguments="${user.name}"/>
185

## Página 193

13.4. Deixequeousuáriodefinaalíngua CasadoCódigo
Noatributo argumentspassamostodososvaloresquedeverãosubsti-
tuirosíndicesnamensagem.Casotenhamosmaisdeum,podemossepará-
lospor ,. ParaomesmoprocessoserfeitousandoaJSTL,teríamosalgo
parecidocomoquesegue:
<fmt:message key="users.welcome">
<fmt:param value="${user.name}"/>
</fmt:message>
Oprimeiromodoébemmaisdireto,porissooptamosporelenestemo-
mento. Lembre-sedeadicionarasentradasnosarquivosdasduaslínguas
pois,casovocêbusqueporumachaveinexistente,comatagdoSpring,uma
exceptionvaiserlan çada.
13.4 D eixe que o usuário defina a língua
Respeitaroidiomasugeridopelonavegadoréumaótimaformadetentarmos
acertaralínguapreferidapelousuário.Oproblemadessaabordageméseo
idiomaconfiguradonãoforrealmenteopreferidodele.Nessemomento,caso
vocêestejaachandoquetodomundopodetrocarissofacilmente,penseem
todasaspessoasquevocêjáconheceuquenãotinhammuitoconhecimento
decomputação.Meupaiporexemplo,apesardeusardiariamenteumnave-
gador,nãosaberiacomofazeressatroca.
Umaestratégiaadotadaporalgunssiteséadeoferecerlinksparaqueo
própriousuáriopossadefiniroidiomapredileto.
Fig.13.2:Bandeirasdospaíses
VamosadotaramesmaabordagemparaaCasadoCódigo.Inicialmente,
vamosadicionaroslinksparaqueousuáriopossaescolher.Faremosissono
186

## Página 194

CasadoCódigo Capítulo13. Internacionalização
arquivo header.jsp:
<nav id="main-nav">
<ul id="clearfix">
...
<li>
<a href="<c:url value="/produtos?locale=pt"/>">
Português
</a>
</li>
<li>
<a href="<c:url value="/produtos?locale=en_US"/>">
Inglês
</a>
</li>
</ul>
</nav>
Jáatépassamosumparâmetroindicandoosidiomasquequeremos. A
perguntaqueficaé:quemvaireceberesseparâmetroetrocaralínguaprefe-
rida?Denovo,nãoprecisamosnospreocupar,oSpringMVCjávemcomo
suportepronto.
public class AppWebConfiguration extends WebMvcConfigurerAdapter{
...
@Override
public void addInterceptors(InterceptorRegistry registry) {
registry.addInterceptor(new LocaleChangeInterceptor());
}
@Bean
public LocaleResolver localeResolver(){
return new CookieLocaleResolver();
}
...
}
187

## Página 195

13.4. Deixequeousuáriodefinaalíngua CasadoCódigo
O métodolocaleResolverretorna uma implementação da inter-
face LocaleResolver. No nosso caso, optamos por usar a estratégia
que guarda o idioma preferido em um cookie. Existem outras, como a
SessionLocaleResolver,quepermitequeapreferênciafiqueguardada
diretamentenasessãodousuário.Alémdisso,precisamosensinaraoSpring
MVCqueeledevetrocarovalordalínguaemfun çãodoparâmetropassado.
Umamaneirapadrãodefazerissoseriacriandoum @Controller.Só
que,emvezdeusaressaestratégia,vamosusarum interceptorjápronto,
fornecidopeloSpringMVC.Interceptorsfuncionamcomofiltros,sóqueden-
trodoframework.Aideiaéqueelespossamserexecutadosantesoudepois
daexecuçãodealgummétododosnossoscontrollers.Umaaplicaç ãocomum
deleséquandooprogramadordecidefazeroprocessodeautenticaç ãona
mão.Comoeletemqueverificarseousuárioestálogadoparatodarequisi-
ção,elecriauminterceptorparafazeressachecagemantesdosmétodosdos
controllers.Nonossocaso,o LocaleChangeInterceptorverificasefoi
usadooparâmetro localenarequisiçãoe,emcasopositivo,eleefetuaa
trocadoidioma.Segueoseucódigo,apenasparacuriosidade:
public class LocaleChangeInterceptor extends
HandlerInterceptorAdapter {
/**
* Default name of the locale specification parameter: "locale".
*/
public static final String DEFAULT_PARAM_NAME = "locale";
private String paramName = DEFAULT_PARAM_NAME;
public void setParamName(String paramName) {
this.paramName = paramName;
}
public String getParamName() {
return this.paramName;
}
188

## Página 196

CasadoCódigo Capítulo13. Internacionalização
@Override
public boolean preHandle(HttpServletRequest request,
HttpServletResponse response, Object handler)
throws ServletException {
String newLocale = request.getParameter(this.paramName);
if (newLocale != null ) {
LocaleResolver localeResolver =
RequestContextUtils.getLocaleResolver(request);
if (localeResolver == null) {
throw new IllegalStateException
("No LocaleResolver found: not
in a DispatcherServlet request?");
}
localeResolver.setLocale(request, response,
StringUtils.parseLocaleString(newLocale));
}
// Proceed in any case.
return true;
}
}
Ométodo preHandler,comoopróprionomediz,éinvocadoantesda
execuçãodonossocontroller.Umpontoquedeveserlembradoé:apartirdo
momentoemqueocookiedousuáriofoisetado,oSpringMVCsempredará
preferênciaaeleemdetrimentodoheader Accept-Language.
13.5 C onclusão
Estecapítulotambémfoitranquilo.Internacionalizaçãoéumtemamuitoco-
mumentretodasasaplicações,lembre-seapenasdenãoserradical.Casovocê
nãotenhaplanosdefazeroutrasversões,nãosepreocupecomestedetalhe.
Sóouseserealmentefornecessário,afinaldecontasvocêestádeixandode
darmanutençãosóemumlugarparadaremdois!Anteseraapenasapágina,
agoraépáginaearquivodemensagens.
189

## Página 197

13.5. Conclusão CasadoCódigo
Paraoleitormaisesquecido,ocarregamentodoarquivodemensagensjá
foiconfiguradobemnoiníciodolivro.
@Bean
public MessageSource messageSource() {
ReloadableResourceBundleMessageSource bundle =
new ReloadableResourceBundleMessageSource();
bundle.setBasename("/WEB-INF/messages");
bundle.setDefaultEncoding("UTF-8");
bundle.setCacheSeconds(1);
return bundle;
}
190

## Página 198

Capítulo14
Testesautomatizados
Nossosistemajáestácomasprincipaisfuncionalidadesimplementadas.Ca-
dastramoselistamososlivros,adicionamosprodutosaocarrinhodecompras
eatésimulamosintegraçãocomumsistemaexterno.Podemosaindaadicio-
narmaiscoisas,comosólistaroslivrosqueforamaprovados,colocarlivros
emdestaque,associá-losàsrespectivascategoriasetc.Vocêjáécapazdeim-
plementartudoisso. Umdetalhemuitoimportante,quenãofoitratadoaté
estemomento,éapartedetestesdanossaaplicaç ão.Nãoqueremosficarro-
dandotudomanualmenteparasaberseascoisasestãofuncionando.
Existemalgumascategoriasdeteste,geralmentedivididasentretestesde
unidade,deintegraçãoedeaceitação.Aprimeiracategorianãovaiserabor-
dadaporestelivropoisoSpringnãotemnadadenovoparaoferecernessa
área. VocêcontinuaráusandooJUnitdamesmamaneiracomojádeveter
lidoemvárioslugares.Emrelaçãoaostestesdeaceitação,oSpringtambém
nãooferecenadadenovo,vocêcontinuarátrabalhandocomferramentasno

## Página 199

14.1. TestesdeintegraçãonoDAO CasadoCódigo
estilodoSelenium. Paraumabasemaiorsobreateoriarelacionadaacada
tipodeteste,aconselhoolivro TDD no Mundo Real,doespecialistaeótimo
autorMaurícioAniche.
14.1 T estes de integração no DAO
Aúnicacategoriaquesobroufoiadetestedeintegraç ão,masnãoseengane:
vocêvaipassarumaboapartedotempotrabalhandonele.Porexemplo,como
sabersesuas queriesnosseusDAOsestãorealmentefuncionando? Geral-
mente,oscódigosquenecessitamdealgumainfraestrutura,porexemplodo
acessoaobancodedados,exigemquevocêfaç abastanteconfiguraçãoesi-
mulecenários,dosquaisoseuframeworkjácuidaparavocê.Paraessestipos
detestes,oSpringpodelheajudarmuito.
Vamoscomeçaradicionandoumrelatórionanossaaplicação.Precisamos
saberototalvendidoparacadatipodelivro.
@Repository
public class ProductDAO {
@PersistenceContext
private EntityManager manager;
...
public BigDecimal sumPricesPerType(BookType bookType) {
TypedQuery< BigDecimal> query = manager.createQuery(
"select sum(price.value) from Product p join
p.prices price where price.bookType =:bookType",
BigDecimal .class);
query.setParameter("bookType", bookType);
return query.getSingleResult();
}
}
Pormaisquevocêconfienassuashabilidadescomoprogramador,sem-
preéinteressantesaberseaconsultaestáfuncionandocomovocêespera-
ria. Paraverificarisso,podemoscriarumtestequeefetivamentecadastra
algunslivroseverificaoretorno. Vamoscriaraclasse ProductDAOTest
192

## Página 200

CasadoCódigo Capítulo14. Testesautomatizados
namesmaestruturadepacotejáexistente,sóquevamoscolocá-ladentrodo
src/test/java.
package br.com.casadocodigo.loja.daos;
public class ProductDAOTest {
@Test
public void shouldSumAllPricesOfEachBookPerType(){
ProductDAO dao = new ProductDAO();
//salva uma lista de livros impressos
List<Product> printedBooks = ProductBuilder.
newProduct(BookType.PRINTED, BigDecimal.TEN)
.more(4).buildAll();
//foreach do Java8, fique à vontade para usar um for
//normal
printedBooks.stream().forEach(productDAO::save);
//salva uma lista de ebooks
List<Product> ebooks = ProductBuilder.
newProduct(BookType.EBOOK, BigDecimal.TEN)
.more(4).buildAll();
//foreach do Java8, fique à vontade para usar um for
//normal
ebooks.stream().forEach(productDAO::save);
BigDecimal value =
dao.sumPricesPerType(BookType.PRINTED);
Assert.assertEquals(new BigDecimal (50).setScale(2),
value);
}
}
Nãosepreocupecomaclasse ProductBuilder,elafoicriadaapenas
paraisolaracriaçãodoslivros.Maistardedamosumaolhadanelacommais
carinho. Opontoimportanteéquesalvamosalgunslivros,depoisinvoca-
mosométodoquefazasomadasvendaseverificamosoresultadonofinal.
Nesteexatomomento,ocódigonãodevenemestarcompilando,jáquenão
193

## Página 201

14.1. TestesdeintegraçãonoDAO CasadoCódigo
importamosoJUnitparanossoprojeto.Bastaquesejaadicionadamaisuma
dependênciano pom.xml.
...
<dependency>
<groupId>junit</groupId>
<artifactId>junit</artifactId>
<version>4.12</version>
<scope>test</scope>
</dependency>
Comtudoconfigurado,jápodemosrodarostestes.Oproblemaéquena
horadaexecuçãorecebemosumsonoro NullPointerException.
Fig.14.1:ProductDAOnãorecebeuoEntityManagerinjetado
O problema está dentro métodosave e não tem escapatória, o
nosso EntityManager está nulo. Para o nosso DAO funcionar, um
EntityManagerdeveserinjetadopeloSpring,sóquefomosnósqueinstan-
ciamosoobjeto.ComooSpringvaicontrolarasdependênciasdeumobjeto
seéoprogramadorqueoestácriando?
194

## Página 202

CasadoCódigo Capítulo14. Testesautomatizados
OmaisinteressantenessetipodecenárioéusaropróprioSpringecriar
osobjetosatravésdele. Inclusive,vamosterquecontrolaratransaç ãopara
garantirqueosobjetossejaminseridosantesdeexecutarmosas queries.
@Test
public void shouldSumAllPricesOfEachBookPerType() {
AnnotationConfigApplicationContext ctx =
new AnnotationConfigApplicationContext(
JPAConfiguration.class, ProductDAO.class);
productDAO = ctx.getBean(ProductDAO.class);
PlatformTransactionManager txManager =
ctx.getBean(PlatformTransactionManager.class);
TransactionStatus transaction = txManager
.getTransaction(new DefaultTransactionAttribute());
//até aqui foi configuração do spring
List<Product> printedBooks = ProductBuilder
.newProduct(BookType.PRINTED, BigDecimal.TEN).more(4)
.buildAll();
printedBooks.stream().forEach( productDAO::save);
List<Product> ebooks = ProductBuilder
.newProduct(BookType.EBOOK, BigDecimal.TEN)
.more(4).buildAll();
ebooks.stream().forEach(productDAO::save);
BigDecimal value =
productDAO.sumPricesPerType(BookType.PRINTED);
Assert.assertEquals(new BigDecimal(50).setScale(2), value );
txManager.commit(transaction);
ctx.close();
}
Nãofiquemuitoassustadocomessecódigo,elesódemonstraumpouco
doqueaconteceportrásdospanosquandovocêestáutilizandooSpring
MVC.TivemosquecriarocontextodoSpringnamãoetambémusamosos
objetosdelepararecuperarosobjetosecontrolaratransaç ão.Opontoaqui
195

## Página 203

14.1. TestesdeintegraçãonoDAO CasadoCódigo
é:játemosmuitaspreocupaçõescomnossostestesparaaindaterqueficar
aprendendoalidarcomosdetalhesinternosdoframework. Paranãoficar
presonessetipodesituação,oSpringcriouummódulofocadoapenasem
ajudarnessestiposdetestes.
Configuração do Spring T est
Comojáédepraxe,precisamosadicionarasdependênciasno pom.xml.
...
<dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-test</artifactId>
<version>4.1.0.RELEASE</version>
<scope>test</scope>
</dependency>
Agoravamospartirpararealizaromesmoteste,sóquetrocandoaquele
códigopelasannotationsprovidaspeloSpringTest.
@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(classes =
{ProductDAO.class,JPAConfiguration.class})
public class ProductDAOTest {
@Autowired
private ProductDAO productDAO;
@Transactional
@Test
public void shouldSumAllPricesOfEachBookPerType(){
List<Product> printedBooks = ProductBuilder
.newProduct(BookType.PRINTED, BigDecimal.TEN)
.more(4).buildAll();
printedBooks.stream().forEach(productDAO::save);
List<Product> ebooks = ProductBuilder
.newProduct(BookType.EBOOK, BigDecimal.TEN)
.more(4).buildAll();
196

## Página 204

CasadoCódigo Capítulo14. Testesautomatizados
ebooks.stream().forEach(productDAO::save);
BigDecimal value =
productDAO .sumPricesPerType(BookType.PRINTED);
Assert.assertEquals(new BigDecimal (50).setScale(2),
value);
}
}
Respire,vamosdesvendaressasnovasannotations. Ocódigodoteste
ficoumuitoparecidocomoinicial. Aprincipalmudan çaéqueagorare-
cebemoso ProductDAOinjetadoetambémpodemosusarajáconhecida
@Transactionalparadizerquenossométodoprecisarodardentrodeuma
transação.
Apartemaisnovasãoasannotationsqueforamusadasemcimadanossa
classe.A @RunWithéespecíficadoJUniteéfornecidaparaqueframeworks
possamsernotificadosdasfasesdeexecuçãodoteste.Porexemplo,aextensão
doSpringTesténotificadadacriaçãodainstânciadotesteemsie,apartir
disso,conseguefazertodasasinje çõesnecessárias. Eaíentraaoutraper-
gunta:quaisclassesdevemsercarregadas?Éjustamenteparaissoqueservea
annotation @ContextConfiguration.Reparequepassamosdiretamente
aclasse ProductDAOealémdissopassamosa JPAConfiguration,que
contémconfiguraçãodetodosobjetosnecessáriosparautilizarmosaJPA.
Umúltimoponto,quenaverdadeéomaisimportante,équenossoteste
aindaestáfalhando. Oproblemaéqueestamosinserindoosprodutosna
tabelaquevemsendousadaparadesenvolvimentoelá,porconsequência,já
existemmaislivrosdoqueoplanejado.
14.2 U tilize profiles e controle seu ambiente
Precisamoscriarumambienteespecíficoparaostestes,deformaquetenha-
moscontroleabsolutosobreoqueexistenobancodedados,paraumaope-
raçãonãoatrapalharaoutra. Aprimeiraaç ãoquedevemosrealizaréade
criarum Datasourcequeaponteparaoutrobancodedados.Podemoscriar
umaclassedeconfiguraçãosóparaisso,lembre-sequeestamostrabalhando
no source folderdetestes.
197

## Página 205

14.2. Utilizeprofilesecontroleseuambiente CasadoCódigo
package br.com.casadocodigo.loja.conf;
//imports
public class DataSourceConfigurationTest {
@Bean
public DataSource dataSource(){
DriverManagerDataSource dataSource =
new DriverManagerDataSource();
dataSource .setDriverClassName( "com.mysql.jdbc.Driver");
dataSource .setUrl(
"jdbc:mysql://localhost:3306/casadocodigo_test");
dataSource .setUsername("root");
dataSource .setPassword("");
return dataSource;
}
}
Agorabastaqueadicionemosestaclassenalistadeclassecarregadas:
@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(classes =
{DataSourceConfigurationTest.class ,
ProductDAO .class,JPAConfiguration.class})
public class ProductDAOTest {
...
}
Mesmocomessaalteração,quandorodamosonossoteste,vemosque
eleestácomomesmoproblemadoanterior. Oresultadofinalaindaestá
sendoinfluenciadopelastabelasusadasemambientededesenvolvimento.
Sóquenossanovaclassefoiadicionadaaoinicionalistae,dessaforma,o
Datasourceconfiguradodentrodaclasse JPAConfigurationficasendo
oúltimoaserregistrado.
Claro,podemostrocaraordem,masnãoprecisanempensarmuitopara
saberqueissovaidarumaconfusãogrande. Oquequeremoséconfigurar
queo Datasourcedetestesdevasercarregadoemumcontextodetestes
198

## Página 206

CasadoCódigo Capítulo14. Testesautomatizados
enquantoooutrodevesercarregadoemambientededesenvolvimento.Para
fazerisso,podemosusarorecursode ProfilesdoSpring.
public class DataSourceConfigurationTest {
@Bean
@Profile("test")
public DataSource dataSource(){
DriverManagerDataSource dataSource =
new DriverManagerDataSource();
dataSource.setDriverClassName("com.mysql.jdbc.Driver");
dataSource.setUrl(
"jdbc:mysql://localhost:3306/casadocodigo_test");
dataSource.setUsername( "root" );
dataSource.setPassword( "" );
return dataSource;
}
}
Agora, na classeJPAConfiguration, podemos dizer que o outro
Datasourcedeveserutilizadonoambientededesenvolvimento.
@Bean
@Profile("dev")
public DataSource dataSource(){
DriverManagerDataSource dataSource =
new DriverManagerDataSource();
dataSource .setDriverClassName( "com.mysql.jdbc.Driver");
dataSource .setUrl(
"jdbc:mysql://localhost:3306/casadocodigo");
dataSource .setUsername( "root" );
dataSource .setPassword( "" );
return dataSource;
}
Porfim,nonossotesteinformamosqueoprofileativoéode test.
@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(classes =
{DataSourceConfigurationTest.class
199

## Página 207

14.2. Utilizeprofilesecontroleseuambiente CasadoCódigo
,ProductDAO.class,JPAConfiguration.class})
@ActiveProfiles("test")
public class ProductDAOTest {
...
}
Comoopróprionomeinforma,aannotation @ActiveProfilespode
serusadaparaindicarqualprofileestáativo.Elacasamuitobemcomaparte
detestes,porissovemdentrodoSpringTest. Dessaforma,conseguimos
deixarnossotestepassando!Alémdisso,jáganhamosumbrinde:oSpring
Testautomaticamentelimpaobancodedadosacadateste.Issojánoslibera
deterqueescreverestetipodecódigoe,alémdisso,nãovamosterumteste
influenciandoooutro.
200

## Página 208

CasadoCódigo Capítulo14. Testesautomatizados
Ative o profile para a aplicação web
Neste exato momento, nossa aplicação web parou de funcionar.
Comonãodefinimosnenhumprofilenela,o Datasourcenãoconse-
gueserencontrado.Paraconsertamosisso,podemosconfiguraroprofile
atravésdeumparâmetroquedeveserlidonoiniciodoservidor.Pode-
mosfazê-lonaclasse ServletSpringMVC.
@Override
public void onStartup(ServletContext servletContext)
throws ServletException {
super.onStartup(servletContext);
servletContext.addListener(RequestContextListener.class);
servletContext.setInitParameter("spring.profiles.active",
"dev");
}
Outra possibilidade seria fazer a configuração diretamente no
web.xml.
<context-param>
<param-name>spring.profiles.active</param-name>
<param-value>live</param-value>
</context-param>
14.3 T estes do controller
TestarosDAOs,alémdostestesdeunidadesemsi,jáforneceumaboaconfi-
ançaànossabasedecódigo.Afinaldecontas,amaioriadasaplicaçõesébem
focadanousodobancodedados.Outrocomponentequetalvezvalhaapena
sertestadoéonossocontroller.
Geralmente,elesnãovãopossuirtantalógica,basicamentevãocontrolar
fluxosdechamadasparaoutrosobjetos.Mesmosendoatécertopontotriviais
deserementendidos,algunscontrollersnãopodemfuncionardemaneira
equivocada. Porexemplo,aURLdeprodutosdevesemprelistaroslivros
201

## Página 209

14.3. Testesdocontroller CasadoCódigo
queestãonobancodedados,casocontrárioaCasadoCódigopodeestar
perdendovendas.
OscontrollerssãoacessíveisatravésdasURLseparaqueissofuncione
precisamosqueoservidorestejadepé. Estetesteatépodeserfeitoegeral-
menteéusadaumabibliotecacomooSeleniumparaajudaremtodoopro-
cesso.Opontonegativodessaabordageméjustamenteprecisaresperartodo
otempodestartdoservidor. OSpringTestpodenosajudaraí. Eleconse-
guemontaroambientenecessárioparaqueconsigamosacessaroscontrollers
atravésdasURLs,semanecessidadedeterumservidorrodando.
package br.com.casadocodigo.loja.controllers;
//imports
@RunWith(SpringJUnit4ClassRunner.class)
@WebAppConfiguration
@ContextConfiguration(classes = { AppWebConfiguration.class,
JPAConfiguration.class, SecurityConfiguration.class,
DataSourceConfigurationTest.class })
@ActiveProfiles("test")
public class ProductsControllerTest {
@Autowired
private ProductDAO productDAO;
@Autowired
private WebApplicationContext wac;
private MockMvc mockMvc;
@Before
public void setup() {
this.mockMvc =
MockMvcBuilders.webAppContextSetup(this.wac)
.build();
}
@Test
@Transactional
202

## Página 210

CasadoCódigo Capítulo14. Testesautomatizados
public void shouldListAllBooksInTheHome() throws Exception {
this.mockMvc.perform(get("/produtos"))
.andExpect( MockMvcResultMatchers
.forwardedUrl("/WEB-INF/views/products/list.jsp"));
}
Aparteimportantedessecódigoéasimulaç ãodorequest. Percebaque
conseguimosfazerum getedizerqueesperamosquetenhasidogeradoum
forwardparaaJSPdelistagemdosprodutos.Porexemplo,podemosiralém
echecarseefetivamentefoiadicionadaumavariávelcomnome products,
paraficardisponívelnapágina.
this.mockMvc.perform(get("/produtos"))
.andExpect( modelAndViewMatcher )
.andExpect( MockMvcResultMatchers
.model()
.attributeExists("products"))
.andExpect( MockMvcResultMatchers
.forwardedUrl("/WEB-INF/views/products/list.jsp"));
Essecódigoésuficienteparafazernossotestepassar. Vamosapenas
analisaressetrechoumpoucomais,paraentendermelhoroqueométodo
andExpectesperacomoargumento.
Matchers
ResultActions andExpect(ResultMatcher matcher) throws Exception;
O método andExpect espera como parâmetro um objeto do tipo
ResultMatcher,cujasimplementaçõessimplesmentefazemumaverifica-
çãoparaagente. Sãoobjetosdessetipoquesãoretornadospelosmétodos
attributeExists(...)ou forwardedUrl(...).
public ResultMatcher attributeExists( final String... names) {
return new ResultMatcher() {
@Override
public void match( MvcResult result) throws Exception {
203

## Página 211

14.3. Testesdocontroller CasadoCódigo
ModelAndView mav = getModelAndView(result );
for (String name : names) {
assertTrue ("Model attribute '" + name +
"' does not exist", mav.getModel().get(name)
!= null);
}
}
};
}
Casovocêprecisedealgumachecagemquenãoexistepronta,nãofique
acanhado,váláecrieoseu ResultMatcher.
Objetos e annotations de configuração
Voltandoumpoucoparaosetupdoteste,vamosdarumaolhadanos
objetoseannotationsnecessáriosparafazeronossocódigofuncionar.
@RunWith(SpringJUnit4ClassRunner.class)
@WebAppConfiguration
@ContextConfiguration(classes = { AppWebConfiguration.class,
JPAConfiguration.class, SecurityConfiguration.class,
DataSourceConfigurationTest.class })
@ActiveProfiles("test")
public class ProductsControllerTest {
@Autowired
private ProductDAO productDAO;
@Autowired
private WebApplicationContext wac;
private MockMvc mockMvc;
@Before
public void setup() {
this.mockMvc =
MockMvcBuilders.webAppContextSetup(this.wac)
.build();
}
204

## Página 212

CasadoCódigo Capítulo14. Testesautomatizados
Em relação às annotations, a única novidade é a
@WebAppConfiguration. Ela é responsável por fazer oRunner do
Spring Test carregar os objetos necessários para uma aplicação web, por
exemplo,o HttpServletRequesteo HttpServletResponse. Além
disso, precisamoscriaroobjetoresponsávelporsimularosrequestspara
nós,nocasoo MockMvc. Oobjetodotipo WebApplicationContexté
arepresentaçãodocontextodoSpringparaprojetosweb. Precisamosdele
paramontaro MockMvc,jáqueseránecessáriosimularrequests,response
etc.
T estes para garantir o controle de acesso
Umúltimotestequepodemosfazeréoquegarantequesóusuárioscom
perfilde ADMINpossamacessaroendere çodecadastrodeprodutos.
@Test
public void onlyAdminShoudAccessProductsForm()
throws Exception {
RequestPostProcessor processor =
SecurityMockMvcRequestPostProcessors
.user("comprador@gmail.com").password("123456")
.roles("COMPRADOR");
this.mockMvc.perform(get("/produtos/form")
.with(processor))
.andExpect(MockMvcResultMatchers.status().is(403));
}
Funcionabasicamentenomesmoestilodoanterior,aúnicadiferen çaé
queusamosumaclasseespecíficadomódulodetestesdoSpringSecurity.
Pedimosparaquesejacriadoumusuáriocomascaracterísticasdequea
genteprecisaetentamosacessaraURLprotegida.Deveserretornadoostatus
403,informandoqueaqueleusuárionãotemautorizaçãoparaacessardeter-
minadaURL.Oobjetodotipo RequestPostProcessorpodeserusado
quandoprecisamosadicionaralgumacoisaaorequestantesdeeleserproces-
sado.Éexatamenteissoqueéfeitoeumobjetoquerepresentanossousuário
éadicionado,descartandoanecessidadedetermosqueiraobancodedados
fazerabusca.
205

## Página 213

14.4. Conclusão CasadoCódigo
Comoquasesempre, vamosparaasconfiguraçõesfinais. Ofiltrodo
SpringSecuritydeveseradicionadoao MockMvcparaqueelepossainter-
ceptarorequesteaplicarasregrasnecessárias.
@ContextConfiguration(classes = { AppWebConfiguration.class,
JPAConfiguration.class, SecurityConfiguration.class,
DataSourceConfigurationTest.class })
@ActiveProfiles("test")
public class ProductsControllerTest {
@Autowired
private Filter springSecurityFilterChain;
@Before
public void setup() {
this.mockMvc =
MockMvcBuilders.webAppContextSetup(this.wac)
.addFilters(springSecurityFilterChain).build();
}
Recebemosinjetadoofiltro,jáqueeleécarregadoatravésdanossaclasse
SecurityConfigurationeoadicionamosàsimulaçãodanossaaplicação
web.Paraqueessapartefuncione,precisamosadicionarmaisumadependên-
ciaaonosso pom.xml.
<dependency>
<groupId>org.springframework.security</groupId>
<artifactId>spring-security-test</artifactId>
<version>4.0.0.M2</version>
<scope>test</scope>
</dependency>
14.4 C onclusão
Testaréumaparteessencialdanossaaplicaç ãoeostestesdeintegraç ãotêm
umpapelbemimportantenisso. ComaajudafornecidapeloSpringTest,
tudoficamuitomaissimples,vocêtemquefocarapenasnaescritadoteste
emsi.
206

## Página 214

CasadoCódigo Capítulo14. Testesautomatizados
Outropontoaserlembradodestecapítuloéautilizaç ãodasannotations
deprofile.Elassãodegrandeajudatantonocenáriodetestesquantoemrela-
çãoaousodeobjetoscomligaç ãocomomundoexterior.Porexemplo,você
nãovaificarquerendofazeruploaddearquivosparaaAmazonenquantoestá
emdesenvolvimentoe,paracontornarisso,podeusarumprofilequecarre-
gueumobjetoquefiquesalvandonodiscolocal.Existemváriasaplicações,
fiquesempreatento.
207

## Página 216

Capítulo15
Outrasfacilidades
Jápassamosporbastantecoisanodecorrerdolivro,masparafecharcom
chavedeourovamosvermaisfacilidadesprovidaspeloSpringque,comcer-
teza,serãoúteisnoseudiaadiadeusuáriodoframework.
15.1 R esolvendo o problema gerado pelo Lazy
Load
Nãoseisevocêestálembrado,masnahoradaescritadosmétodosdanossa
classe ProductDAOusamosaexpressão join fetch paraficarcarregando
alistadepre çosrelativasaumlivro.
public List<Product> list() {
return manager.createQuery(
"select p from Product p join fetch p.prices",

## Página 217

15.1. ResolvendooproblemageradopeloLazyLoad CasadoCódigo
Product.class).getResultList();
}
SófazemosissoporquenanossaJSPtentamoscarregaressamesmalista.
Olheocódigoaseguirpararefrescaramemória.
<c:forEach items="${product.prices}" var="price">
[${price.value} - ${price.bookType}]
</c:forEach>
Casovocênãoutilizeo fetch join vaireceberaseguinteexception:
org.hibernate.LazyInitializationException: failed to lazily
initialize a collection of role:
br.com.casadocodigo.loja.models.Product.prices
ElainformaqueoHibernatenãoconseguiucarregaracole çãodepre ços.
EssaéaparteboaeruimdeusarumframeworkcomooHibernate.Quando
vocêcarregaseusobjetos,elesubstituialgumaspropriedadesparapermitir
quevocêprogramedemaneiraorientadaaobjetos.Porexemplobastainvocar
ométodo getPrices()queelevaitentardispararumaquerynobanco.O
pontoruiméquevocêprecisaentenderumpoucomaisdele,paraconseguir
tirarproveitodessafuncionalidade. Basicamente,o EntityManagertem
queficarabertodurantetodoociclodarequisiç ão,inclusivenomomentoem
quevocêestámontandoaJSP.
Parafacilitarnossavida,omódulodoSpringdeintegraç ãocomaJPAe
Hibernatejáforneceumfiltro,daAPIdeServlets,quefazessetrabalhopara
agente.
public class ServletSpringMVC extends
AbstractAnnotationConfigDispatcherServletInitializer {
....
@Override
protected Filter[] getServletFilters() {
return new Filter[]{
new OpenEntityManagerInViewFilter()};
}
}
210

## Página 218

CasadoCódigo Capítulo15. Outrasfacilidades
Bastaquefaçamosoregistrodofiltroqueagoravocêpodeinvocarosmé-
todosquevocêquiser,o EntityManagervaiestarsempreaberto.Nãoes-
tranhequeestamoscriandoofiltronamão,desdeaversão3daespecificaç ão
deServlets,podemosregistrarquasetudodemaneiraprogramática.
Casovocêtireo fetch join daconsultaeacesseateladelistagemde
produtos,vaiperceberquetudoacontecerásemproblemaalgum.Casovocê
sejaumpoucomaiscuriosoeanaliseoquesaiunoconsoledoservidor,verá
algocomooexemploaseguir.
Hibernate: select prices0_.Product_id as Product_1_0_0_,
prices0_.bookType as bookType2_1_0_, prices0_.value as
value3_1_0_ from Product_prices
prices0_ where prices0_.Product_id=?
Hibernate: select prices0_.Product_id as Product_1_0_0_,
prices0_.bookType as bookType2_1_0_, prices0_.value as
value3_1_0_ from Product_prices prices0_ where
prices0_.Product_id=?
Hibernate: select prices0_.Product_id as Product_1_0_0_,
prices0_.bookType as bookType2_1_0_, prices0_.value as
value3_1_0_ from Product_prices prices0_ where
prices0_.Product_id=?
...
Paracadaprodutocarregado,oHibernatefezumaquerynobancopara
buscarospre çosnecessários. EsseéoproblemadasN + 1queriescausado
pelousodoLazyLoad.Naopiniãodesteautor,vocêdeveriatentarplanejaro
máximodequeriesquepudesseedeixarparausaroLazyLoadsóemúltimo
caso.Inicialmentevaiparecerqueeleestáajudandomuito,mascomopas-
sardotempovocêvaicome çaraperceberquemuitasconsultasestãosendo
realizadassemquevocêtenhacontrole.
211

## Página 219

15.2. Liberandoacessoarecursosestáticosdaaplicação CasadoCódigo
15.2 L iberando acesso a recursos estáticos da
aplicação
Continuandocomasdicasdefinaldelivro.Paramontarastelasdanossaapli-
cação,emalgunsmomentos,copiamoso HTMLgeradopelositedaCasado
Código.AdicionamosoSpringSecuritynanossaaplicaç ãoetudocontinuou
funcionandodamaneiracomodeveria.Umaquestãoparapensarmosé:ese
tivéssemosadicionadoarquivosdeJavascriptedeCSS,oqueaconteceria?
Vamos fazer um teste simples. Vou criar um novo arquivo.js
na pasta src/main/webapp/resources/js. Para simular uma si-
tuação real, podemos criar o arquivo com o nome dejquery.js.
Agora iniciamos o servidor e tentamos acessá-lo através da URL loca-
lhost:8080/casadocodigo/resources/js/jquery.js.Vocêvaiperceberquepron-
tamenteoSpringSecurityodirecionouparaateladelogin.Paraoframework,
éapenasmaisumaURLe,comonãofizemosaconfiguraç ãoliberandoo
acessoaela,somosbloqueados.
Pararesolverisso,vamossobrescreverumoutrométododeconfiguração.
@EnableWebMvcSecurity
public class SecurityConfiguration extends
WebSecurityConfigurerAdapter{
...
@Override
public void configure(WebSecurity web) throws Exception {
web.ignoring().antMatchers("/resources/**");
}
}
Aocontráriodoprimeiro configure,querecebecomoargumentoum
objetodotipo HttpSecurity,esserecebeum WebSecurity.Oprimeiroé
utilizadoparafazeraconfiguraçãogeral.Comovimos,elefazmuitomaiscoi-
sasdoqueapenaspermitiroacessoaalgumasURLs.Estequeestamosvendo
agoraéespecíficoparaaaplicaçãoweb.Porexemplo,estamospedindoparao
SpringSecurityignorarqualqueracessoaURLquecomececom resources.
212

## Página 220

CasadoCódigo Capítulo15. Outrasfacilidades
Agora,quandovocêtentaracessaamesmaURL,oservidorvairetornaro
status404.OproblemaéqueaServletdoSpringMVCestáachandoquevocê
estáacessandoumendere çomapeadoparaumcontroller,oqueclaramente
nãoéocaso.Pararesolverisso,vamossobrescrevermaisummétodo,agora
nanossaclasse AppWebConfiguration.
@Override
public void configureDefaultServletHandling(
DefaultServletHandlerConfigurer configurer) {
configurer .enable();
}
Quando você invoca o método enable() na classe
DefaultServletHandlerConfigurer, você está informando para
oSpringMVCque,casoelenãoconsigaresolveroendere ço,eledevedelegar
achamadaparaoServletContaineremuso.Pronto,agoravocêjáconsegue
servirosseusconteúdosestáticos. Lembre-sededeixá-losdentrodeuma
pastaespecífica,paraficarfácildevocêconfigurar.
15.3 E nviando e-mail
Umaúltimatarefaquevocêvaiacabarprecisandorealizaréadeenviare-
mails.Quasetodosistematemumafuncionalidadedaqualenviarumalerta
viae-mailéparteintegrante.Comonãopoderiaserdiferente,oSpringjávem
comaabstraçãonecessáriaparaquepossamosenviarume-maildeforma
simples.
OsistemadaCasadoCódigo,porexemplo,temasituaç ãoideal.Quando
umacompraérealizadacomsucesso,precisamosmandarume-mailparao
comprador.
@RequestMapping("/payment")
public class PaymentController {
...
@Autowired
private MailSender mailer;
@RequestMapping(value = "checkout",
213

## Página 221

15.3. Enviandoe-mail CasadoCódigo
method = RequestMethod.POST)
public Callable<ModelAndView> checkout(
@AuthenticationPrincipal User user) {
return () -> {
BigDecimal total = shoppingCart.getTotal();
String uriToPay =
"http://book-payment.herokuapp.com/payment";
try {
restTemplate.postForObject(uriToPay,
new PaymentData(total), String.class);
//enviando email
sendNewPurchaseMail(user);
return new ModelAndView(
"redirect:/payment/success");
} catch (HttpClientErrorException exception) {
return new ModelAndView(
"redirect:/payment/error");
}
};
}
private void sendNewPurchaseMail(User user) {
SimpleMailMessage email = new SimpleMailMessage();
email.setFrom("compras@casadocodigo.com.br");
email.setTo(user.getLogin());
email.setSubject("Nova compra");
email.setText("corpo do email");
mailer.send(email);
}
}
Percebaqueapenasrecebemosumobjetodotipo MailSender,queé
umainterfacedoSpring,emandamosoe-mail. Maissimples,impossível.
Debrinde,aindausamosaannotation @AuthenticationPrincipal,que
permitequerecebamosousuáriologadocomoparâmetrodonossométodo.
Pensandoemdesigndecódigo,poderíamostercriadooutraclasseunica-
menteresponsávelporenviare-mailsnosistemaetê-lausadononossocon-
214

## Página 222

CasadoCódigo Capítulo15. Outrasfacilidades
troller.Essaéumatarefaqueficaparavocê!
ParaoSpringconseguirfazerainje ção,precisamosensinar-lhequalim-
plementaçãoseráusada. Parafazermosisso,maisumavez,criaremosum
métodonanossaclasse AppWebConfiguration.
@Bean
public MailSender mailSender() {
JavaMailSenderImpl javaMailSenderImpl =
new JavaMailSenderImpl();
javaMailSenderImpl.setHost("smtp.gmail.com");
javaMailSenderImpl.setPassword("password");
javaMailSenderImpl.setPort(587);
javaMailSenderImpl.setUsername("seulogin");
Properties mailProperties = new Properties();
mailProperties.put("mail.smtp.auth", true);
mailProperties.put("mail.smtp.starttls.enable", true);
javaMailSenderImpl.setJavaMailProperties(mailProperties);
return javaMailSenderImpl;
}
Osmétodossãobemlegíveis.Aúnicacoisaamais,éaconfiguraç ãodo
Properties. Algunsprovedoresdee-mail,comoogmail,vãopedirque
vocêfaçaumaconexãoemmodoseguro,porissoahabilitaç ãodo Transport
Layer Security(TLS).
Parafinalizar,comonãopoderiadeixardeser,vamosadicionarasdepen-
dênciasnecessáriasparaqueoSpringpossautilizaraespecificaçãodee-mail,
providapelopróprioJava.
<!-- email -->
<dependency>
<groupId>javax.mail</groupId>
<artifactId>mail</artifactId>
<version>1.4.7</version>
</dependency>
215

## Página 223

15.4. Conclusão CasadoCódigo
15.4 C onclusão
Essasúltimasfacilidadesforamapenasparamostrarque,mesmopassando
pormuitacoisaaodecorrerdolivro,aindativemosmaisdetalhesparamos-
trar. TomebastantecuidadocomadecisãodeusaroHibernatenoprojeto
porque,pormaisqueeleabstraiamuitodacomplexidadedapersistência,ele
vaiexigirquevocêentendamaisafundoofuncionamentodele,justamente
paranãocairnasarmadilhas. Vimostambémqueéimportanteconfigurar
nossosframeworksparaqueelesnãobloqueiemnossosrecursosestáticos,
comoJavascripteCSS.
Nãopareagoraejáleiaopróximocapítulo.Vamosfazerasconfigurações
necessáriaspararealizarodeploydanossaaplicação.
216

## Página 224

Capítulo16
Deploydaaplicação
Trabalhamostantoduranteolivro,queseriainjustovocêacabá-loenãopo-
dermostrarparaninguémoquedesenvolveu.Pararesolvermosisso,vamos
instalarnossaaplicaçãono Heroku,umaplataformaquesuportaodeployde
aplicaçõesdasmaisvariadaslinguagens.
16.1 C onfigurando o Maven para o Heroku
Aocontráriodamaioriadoshosts,oHerokunãopedequevocêsubaoar-
quivo .wardasuaaplicaçãoparaoTomcatouJettydele. Emvezdisso,é
necessáriousarmosumaoutraversãodoTomcat,chamadade embedded.A
diferençaprincipaléqueelenãosuportamúltiploscontextos.Simplesmente
orodamos,podeatéserapartirdeummétodo mainepassamosalocalização
donosso war.

## Página 225

16.1. ConfigurandooMavenparaoHeroku CasadoCódigo
java -jar target/dependency/webapp-runner.jar target/*.war
O jar webapp-runner équeovamosbaixarparaconseguirexecutar
aversãominimalistadoservidor.VamosensinaraoMavenque,quandoele
forgeraronossoarquivodeinstalaç ão,eledevebaixaroTomcat embeddede
copiarparao jar webapp-runner.jar.Paraisso,vamosalteraroarquivo
pom.xml.
<dependencies>
...
</dependencies>
<build>
<plugins>
<plugin>
<groupId>org.apache.maven.plugins</groupId>
<artifactId>maven-dependency-plugin</artifactId>
<version>2.3</version>
<executions>
<execution>
<phase>package</phase>
<goals>
<goal>copy</goal>
</goals>
<configuration>
<artifactItems>
<artifactItem>
<groupId>com.github.jsimone</groupId>
<artifactId>webapp-runner</artifactId>
<version>7.0.57.2</version>
<destFileName>
webapp-runner.jar
</destFileName>
</artifactItem>
</artifactItems>
</configuration>
</execution>
</executions>
218

## Página 226

CasadoCódigo Capítulo16. Deploydaaplicação
</plugin>
</plugins>
</build>
AdicionamosumplugindoMavenquerealizaacópianecessáriaparanós.
EsseprocedimentoestátambémdescritonaprópriapáginadoHeroku.Basta
seguirolink: https://devcenter.heroku.com/articles/java-webapp-runner.
Agoraqueopluginestáconfigurado,podemospedirparaoMavengerar
nosso war.
caminhoInstalacaoMaven/bin/mvn package
16.2 Q ual banco será usado no Heroku
Nesseexatomomento,temosdosprofilesparacarregaro DataSourcecom
osdadosdeconexãodobancodedados.Umparaoambientedetesteseoutro,
queéodefault,paraoambientededesenvolvimento.Eparaoambientede
produção,qualbancovamosusar? Essetambéméumcasoqueapartede
profilepodenosajudar.
OSpringpermitequevocêcrieumavariáveldeambienteinformando
qualprofiledevesercarregadopelaaplicaç ão.Outramaneira,maissimples,
épassarumargumentonaexecuçãodoprograma,indicandoquevocêquer
deixarumavariáveldisponível,comosefosseumadeambiente.Seguemas
duasopções:
SPRING_PROFILES_ACTIVE=prod
java -jar target/dependency/webapp-runner.jar target/*.war
java -jar -Dspring.profiles.active=prod
target/dependency/webapp-runner.jar target/*.war
Éimportantequevocêexecuteessescomandosemapenasumalinha.
Definindoavariável,nahoradecarregarocontainer,oSpringvaipro-
curarpor beansqueestejamanotadoscom @Profile("prod").Paraque
tudofuncione,podemoscriaroutraclassedeconfiguraçãoquecontenhaape-
nasaversãodo DataSourceapontandoparaooutrobanco.
219

## Página 227

16.2. QualbancoseráusadonoHeroku CasadoCódigo
@Profile("prod")
public class JPAProductionConfiguration {
@Autowired
private Environment environment;
@Bean
public DataSource dataSource() throws URISyntaxException{
DriverManagerDataSource dataSource =
new DriverManagerDataSource();
dataSource.setDriverClassName("org.postgresql.Driver");
URI dbUrl =
new URI(environment.getProperty("DATABASE_URL"));
dataSource.setUrl("jdbc:postgresql://"
+ dbUrl.getHost() + ":"
+ dbUrl.getPort() + dbUrl.getPath());
dataSource.setUsername(dbUrl.getUserInfo()
.split(":" )[0]);
dataSource.setPassword(dbUrl.getUserInfo()
.split(":" )[1]);
return dataSource;
}
}
Eisumpontoquepodeterficadonasuacabe çaemrelaçãoaobanco
usadoparaoambientedeprodução.Oleitormaisatentodeveternotadoque
foiusadooPostgreSQLemvezdoMYSQL.Fomosporestecaminhoapenas
porqueoHerokuusaoPostgrecomodefault.Detodojeito,valeressaltarque
omelhorseriausaromesmobancoemdesenvolvimentoeemproduç ão.As
informaçõesdeconexãoforamextraídasdavariáveldeambientefornecida
pelopróprioHeroku.Segueumexemplodaformataç ão:
export
DATABASE_URL=postgres://user:password@localhost:5432/nomeDaApp
Podemos acessar qualquer variável de ambiente através da classe
Environment,jádisponibilizadapelopróprioSpring.Atravésdelatambém
220

## Página 228

CasadoCódigo Capítulo16. Deploydaaplicação
podemossaberemqualambienteestamosrodando,porexemplo.
Lembre-sequetambémprecisamosadicionaressanovaconfiguraç ãoà
classe ServletSpringMVC.Aideiaéqueelaserásemprecarregada,sóque
vaiserusadaapenasquandooprofiledeproduç ãoestiverativo.
public class ServletSpringMVC extends
AbstractAnnotationConfigDispatcherServletInitializer {
@Override
protected Class<?>[] getRootConfigClasses() {
return new Class[] { SecurityConfiguration.class,
AppWebConfiguration.class,
JPAConfiguration.class,
JPAProductionConfiguration.class };
}
....
}
16.3 N ov a aplicação no Heroku
Nossaaplicaçãojáestádevidamenteconfiguradaparaserdeployada. Para
finalizar,precisamosapenascriarumanovaaplicaçãonopróprioHeroku.
OHerokufaztodoprocessodedeployserbaseadono git,demodoqueé
imprescindívelquevocêotenhainstaladoemsuamáquina.Casonãootenha,
sigaospassosaqui: https://help.github.com/articles/set-up-git/. Comogit
configurado,acesseapastadasuaaplicaçãoeexecuteosseguintescomandos:
git init
git add -A
git commit -m "versionando o código para deploy"
Opróximopassoéinstalaroprogramadelinhadecomandofornecido
peloHeroku. Pararealizarodownloadsigaospassossugeridosnestelink:
https://toolbelt.heroku.com/.
221

## Página 229

16.4. Conclusão CasadoCódigo
Como Heroku T oolbeltinstalado,podemoscriarumanovaaplicaç ão.
Rodeocomandodedentrodapastadasuaaplicaç ão,dessaformaoutilitário
jávaiconfiguraroseurepositório,fazendocomqueeleaponteparaoHeorku.
heroku apps:create cdcspringmvc
Essalinhaésuficienteparasercriadaumanovaaplicaç ão.Tomeapenas
cuidadocomonome,porqueelepodejátersidousado.Parafinalizaraconfi-
guração,precisamosensinaraoHerokuquallinhaeledeverodarparainiciar
anossaaplicação.Paraisso,naraizdoprojeto,temosquecriarumarquivo
chamado Procfile,comoseguinteconteúdo,etudonamesmalinha:
web: java $JAVA_OPTS -jar -Dspring.profiles.active=prod
target/dependency/webapp-runner.jar --port $PORT target/*.war
O JAVA_OPTSéapenasumavariáveldeambientedefinidapeloHeroku,
cujautilizaçãoésugeridaparasubiraaplicação.
Agoraéahoradeserfelizesubiroseucódigo!
git push heroku master
Pronto,vocêacabouderealizaroprimeirodeploynoHeroku.Estaéuma
vantagemgrandedosClouds,tudojáestáconfiguradoeautomatizadodolado
doservidor,bastaquevocêseadequeumpoucoeteráumdeploytranquilo.
16.4 C onclusão
Nestecapítulo,estudamosumpoucodoprocessodedeploydaaplicaç ão.
Aindaconseguimosverumpoucomaisdecomoapartedeprofilepodenos
ajudar.
Duasliçõesdecasaparavocê,apenasparadeixaraaplicaç ãoaindamais
legal:énecessárioquevocêcrieumendereçoparacadastrodenovosusuários,
parapoderconseguirrealizarologindaaplicaç ão.Alémdisso,podeserlegal
adicionaralgumCSSparadeixarovisualmaisinteressante.
222

## Página 230

Capítulo17
Horadepraticar
Muitoobrigadoporterficadocomigodurantetodaajornadadolivro! É
muitoimportantequevocêtentepraticartudoquefoiestudado.Temchance
deescolheratecnologiadonovoprojeto?Nãofiqueacanhado,useoSpring
MVCefoquenassuasregrasdenegócioentregandomuitomaisvalorparao
seucliente.Semcontarque,mesmoesteditadosendovelho,apráticalevaà
perfeição.Emcadanovoprojeto,vocêvaiencontrarnovosdesafiosquefarão
comquevocêentendacadavezmaissobreoframework.
17 .1 M antenha contato
Euestoucompletamentedisponívelparaajudá-loondeforpossível. Você
podemeachardasseguintesformas:

## Página 231

17.1. Mantenhacontato CasadoCódigo
• Por e-mail, basta enviar uma mensagem para livros-
pringmvc@gmail.com
• CasouseoTwitter,ésóacessarhttps://twitter.com/alberto_souza
• AindaháapossibilidadedeacompanharmeusprojetospeloGithub,
bastaacessar https://github.com/asouza.
• Casoqueirapostarumadúvidaeaindaajudaroutraspessoas,useo
fórumcriadoespecialmenteparaolivro, http://groups.google.com.br/
d/forum/livro-springmvc
• Váalémdoconteúdodolivroetambémacompanheospostsfeitosno
bloghttps://domineospring.wordpress.com.
Porúltimo,todoequalquerfeedbacksobreolivroébem-vindo. Useo
fórumoumandediretamenteparameue-mail.Escreverolivrofoiumgrande
desafio,esperoqueeletenhasidodealgumavaliaparavocê.
224