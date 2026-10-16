---json
{
  "id": "falando_de_grails_alt_ssima_produtividade_no_desenvolvimento_web",
  "title": "Falando de Grails Altíssima produtividade no desenvolvimento web",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "**Arquivo Original:** `Falando de Grails Altíssima produtividade no desenvolvimento web.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "alt",
    "desenvolvimento",
    "falando",
    "grails",
    "linguagens",
    "php",
    "produtividade",
    "ssima"
  ],
  "perguntas_tipo": [
    "Como utilizar Falando de Grails Altíssima produtividade no desenvolvimento web?",
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

# Falando de Grails Altíssima produtividade no desenvolvimento web

> **Arquivo Original:** `Falando de Grails Altíssima produtividade no desenvolvimento web.pdf`
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
1 Expulsando o tédio da plataforma Java EE 1
1.1 GroovyeGrailssãopontes . . . . . . . . . . . . . . . . . . . . 3
1.2 PorqueGroovy? . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.3 PorqueGrails? . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
1.4 Sobreestelivro . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
1.5 Código-fonte . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
1.6 Agradecimentos . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2 Groovy: uma breve introdu ção 13
2.1 Paraqueoutralinguagemdeprogramaç ão? . . . . . . . . . . 14
2.2 Afinaldecontas,oqueéoGroovy? . . . . . . . . . . . . . . . 15
2.3 InstalandoGroovy . . . . . . . . . . . . . . . . . . . . . . . . . 17
2.4 GroovyConsole:seulaboratóriopessoal . . . . . . . . . . . . 18
2.5 “Olámundo”. . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
2.6 Variáveis:tipagem“opcional”. . . . . . . . . . . . . . . . . . 21
2.7 TrabalhecomStrings . . . . . . . . . . . . . . . . . . . . . . . 22
2.8 OqueéverdadeemGroovy? . . . . . . . . . . . . . . . . . . . 24
2.9 Estruturasdecontrole . . . . . . . . . . . . . . . . . . . . . . . 27
2.10 Funçõesemétodos . . . . . . . . . . . . . . . . . . . . . . . . 34
2.11 Concluindo. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
i

## Página 4

Sumário CasadoCódigo
3 Mergulhando em Groovy 37
3.1 Orientaçãoaobjetos . . . . . . . . . . . . . . . . . . . . . . . . 37
3.2 Traits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
3.3 Tipagemdinâmicaouestática?Ambas. . . . . . . . . . . . . . 45
3.4 Closures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
3.5 Metaprogramação . . . . . . . . . . . . . . . . . . . . . . . . . 59
3.6 Invocaçãodinâmicademétodos . . . . . . . . . . . . . . . . . 65
3.7 Concluindo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
4 Precisamos falar sobre Grails 69
4.1 FalandodeGrails . . . . . . . . . . . . . . . . . . . . . . . . . 70
4.2 Oqueéumframework? . . . . . . . . . . . . . . . . . . . . . 73
4.3 InstalandooGrails . . . . . . . . . . . . . . . . . . . . . . . . . 74
4.4 Criandoaaplicação . . . . . . . . . . . . . . . . . . . . . . . . 80
4.5 Escrevendoasclassesdedomínio . . . . . . . . . . . . . . . . 86
4.6 Dandovidaaosistema . . . . . . . . . . . . . . . . . . . . . . 92
4.7 Acessandoobancodedados . . . . . . . . . . . . . . . . . . . 101
4.8 Instalandoaaplicação . . . . . . . . . . . . . . . . . . . . . . . 104
4.9 Nãoserepita(Don’t Repeat Y ourself DRY). . . . . . . . . . . 105
4.10 Concluindo. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
5 Domínio e persistência 107
5.1 Oqueéumaentidade(ouclassededomínio)? . . . . . . . . 108
5.2 Umamodelageminicial . . . . . . . . . . . . . . . . . . . . . . 109
5.3 OqueéoGORM? . . . . . . . . . . . . . . . . . . . . . . . . . 112
5.4 Datasource:conectando-seaoSGBD . . . . . . . . . . . . . . 113
5.5 Voltandoàmodelagemdasclassesdedomínio . . . . . . . . 134
5.6 Relacionandoentidades . . . . . . . . . . . . . . . . . . . . . . 140
5.7 Inserindo,editandoeexcluindoregistrosnobancodedados 148
5.8 Entendendoocascateamento . . . . . . . . . . . . . . . . . . 152
5.9 Customizandoomapeamento . . . . . . . . . . . . . . . . . . 159
5.10 Lidandocomherança . . . . . . . . . . . . . . . . . . . . . . . 166
5.11 Concluindo. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169
ii

## Página 5

CasadoCódigo Sumário
6 Buscas 171
6.1 GrailsConsole:nossomelhoramigo . . . . . . . . . . . . . . 172
6.2 Findersdinâmicos . . . . . . . . . . . . . . . . . . . . . . . . . 173
6.3 Criterias . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 183
6.4 Buscasporwhere(wherequeries) . . . . . . . . . . . . . . . . 200
6.5 HQL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 206
7 A camada web: controladores 213
7.1 Masantesvamosfalarumpoucosobrescaffolding? . . . . . 214
7.2 Entendendooscontroladores . . . . . . . . . . . . . . . . . . 219
7.3 DominandoURLs . . . . . . . . . . . . . . . . . . . . . . . . . 225
7.4 Redirecionandoações. . . . . . . . . . . . . . . . . . . . . . . 228
7.5 Renderizandoaresposta . . . . . . . . . . . . . . . . . . . . . 229
7.6 DataBinding . . . . . . . . . . . . . . . . . . . . . . . . . . . . 235
7.7 Commandobjects . . . . . . . . . . . . . . . . . . . . . . . . . 243
7.8 Evitandoasubmissãorepetidadeformulários . . . . . . . . . 248
7.9 Uploaddearquivos . . . . . . . . . . . . . . . . . . . . . . . . 249
7.10 Downloaddearquivos . . . . . . . . . . . . . . . . . . . . . . 252
7.11 Filtrandorequisições. . . . . . . . . . . . . . . . . . . . . . . 254
7.12 Escopodocontrolador . . . . . . . . . . . . . . . . . . . . . . 263
7.13 Escopodedados . . . . . . . . . . . . . . . . . . . . . . . . . . 265
8 A camada web: visualizaç ão 267
8.1 Oessencial . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 268
8.2 Tagscustomizadas . . . . . . . . . . . . . . . . . . . . . . . . . 273
8.3 Tagoufun ção? . . . . . . . . . . . . . . . . . . . . . . . . . . . 280
8.4 Lidandocomformulários . . . . . . . . . . . . . . . . . . . . . 281
8.5 Criandosuasprópriastagscustomizadas . . . . . . . . . . . . 285
8.6 Templates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 290
8.7 PadronizandolayoutscomSitemesh . . . . . . . . . . . . . . 292
8.8 Recursosestáticos . . . . . . . . . . . . . . . . . . . . . . . . . 296
8.9 Ajax . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 301
8.10 Customizandooscaffolding . . . . . . . . . . . . . . . . . . . 305
iii

## Página 6

Sumário CasadoCódigo
9 Camada de negócio: servi ços 307
9.1 Serviços. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 307
9.2 Escopos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 312
9.3 Transações. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 314
9.4 FalandodeSpring . . . . . . . . . . . . . . . . . . . . . . . . . 327
10 T estes 335
10.1 Antesumpoucodemetodologia:TDDeBDD . . . . . . . . 335
10.2 Nossasprimeirasespecificações. . . . . . . . . . . . . . . . . 339
10.3 Escrevendotestesunitáriosparacontroladores . . . . . . . . 354
10.4 Testandobibliotecasdetag . . . . . . . . . . . . . . . . . . . . 360
10.5 Testesintegrados. . . . . . . . . . . . . . . . . . . . . . . . . . 362
11 Modularizando com plug-ins 367
11.1 Oqueéumplug-in? . . . . . . . . . . . . . . . . . . . . . . . . 368
11.2 Criandonossoprimeiroplug-in . . . . . . . . . . . . . . . . . 371
11.3 Plug-insinline . . . . . . . . . . . . . . . . . . . . . . . . . . . 379
11.4 Empacotandooplug-in . . . . . . . . . . . . . . . . . . . . . . 380
381section.11.5
11.6 Oquenãoentranoplug-in . . . . . . . . . . . . . . . . . . . . 384
11.7 Adicionandométodosdinâmicosemtempodeexecução . . 385
11.8 Entendendoasobrescritadeartefatosemplug-ins . . . . . . 386
11.9 Preparando-separaoGrails3 . . . . . . . . . . . . . . . . . . 387
12 Grails 3.0 389
12.1 SaioGant,entraoGradle . . . . . . . . . . . . . . . . . . . . 390
12.2 Umanovabase:SpringBoot . . . . . . . . . . . . . . . . . . . 394
12.3 Qualomelhorcaminhoparaoupgrade? . . . . . . . . . . . . 395
12.4 Finalizando? . . . . . . . . . . . . . . . . . . . . . . . . . . . . 395
13 Apêndice 1 Lista de dialetos do Hibernate 397
Bibliografia 403
iv

## Página 7

Capítulo1
Expulsandootédioda
plataformaJavaEE
Nãomesurpreenderiasevocêestivessebuscandosabermaisarespeitode
GroovyeGrailsdevidoaumdosmotivosaseguir:
• AquelaimpressãodequeomodocomotrabalhamoscomJavaeJava
EEpoderiasermaispragmático,menosburocráticoemaisprodutivo.
Talvezatémesmotãoprodutivoquantosuaplataformadedesenvolvi-
mentoatual.
• Aqueledesejodesermaisprodutivocomumcustomenor.
• Vocêgostariadeentrarparao“mundoJava”massesenteinsegurocom
aquantidadedesiglasenomesquenormalmenteenvolvemestaplata-
forma.NomescomoEJB,JNDI,Servlet,JPA,JAX-RS,JAX-WSetantos

## Página 8

CasadoCódigo
outros.Pareceumainfinidadedetecnologiasque,sevocênãodominar,
vaiconseguirnomáximoresultadosmedíocres.
• Vocênãoacreditaquesejanecessárioconhecertantastecnologiaspara
“apenasescreverumaaplicaçãowebsimples”.
• SimplesmenteouviufalarsobreGroovyeGrailseficoucuriosoares-
peito.
Infelizmente,mesmoapóstantosavan ços,aplataformaJavaEEaindacar-
regaumaimagemnegativaparamuitosdesenvolvedores.Nuncaconhecial-
guémquenegasseoseupoder,massempremedeparocomaquelesquea
veemcomoummundoinacessível,excessivamentecomplexoeburocrático.
Edevoconfessar,essaspessoasestãocertaseGrailsprovaisto.
Grailsnosapresentaumamaneiradiferentedemanipularmosaplata-
formaJavaEE,maissimples,menosburocráticaeextremamenteprodutiva.
Esabemoqueémaisinteressante?Ummododetrabalhonoqualodesen-
volvedorsimplesmenteseesquecedeestarlidandocomoJavaEE:vocêsim-
plesmenteausa.
Este“novomododetrabalho”narealidadeéconsequênciadalinguagem
deprogramaçãonaqualGrailsébaseado,Groovy,que,naminhaopinião,
éondeotesourorealmenteseencontra. Groovyfoicriadocomoobjetivo
defacilitarodesenvolvimentodeaplicaçõesparaaJVM.Podemosdizerque
resolvedoisproblemasfundamentais:sercompatívelcomocódigoJavaexis-
tente,garantindocompletoreaproveitamentodecódigoe,aomesmotempo,
resolverdiversasdaslimitaçõesexistentesnapróprialinguagemJava.
Comooleitorveránodecorrerdestelivro,nãoéexagerodizerqueGro-
ovyécomoum“Java++": diversosnovosrecursosquesóforamincluídos
noJava8em2014jáestavampresentesemGroovydesdesuaintroduç ãoem
2004como,porexemplo, closures,facilidadesparalidarcomtiposnuméri-
cosediversasoutrasfacilidadessintáticasqueaumentamsignificativamente
aprodutividadedoprogramador.
EnquantoGroovyfacilitaotrabalhodoprogramador,eliminandoasdifi-
culdadesinerentesdalinguagemJava,oGrailstornaacessíveltodososrecur-
sosdaplataformaJavaEEdeumaformanuncaantesvistaparaaquelesque
2

## Página 9

CasadoCódigo Capítulo1. ExpulsandootédiodaplataformaJavaEE
desejamtirarproveitodesuasprincipaisvantagens:altadisponibilidade,es-
calabilidade,desempenhoerobustez.Nãohácomonegar,odesenvolvimento
deaplicaçõeswebnaplataformaJavamuitasvezeséumaatividademaisbu-
rocráticaqueonecessário.Grailsremoveesteaspectomorosoaonosoferecer
ummodelodedesenvolvimentobaseadoemconven ções:arquivosdeconfi-
guraçãoagorasomentequandoforodesejodoprogramador,enãomaisuma
exigênciadaplataforma.
GroovyeGrailsacabamcomotédioquepodesetornartrabalharcoma
plataformaJavaEE.Efinalizadoestelivrooleitorpoderáaproveitartodosos
seusrecursosdeumaformasurpreendentementesimplesedireta.
1.1 G roovy e Grails são pontes
Naminhaexperiência,omaiorganhodestastecnologiassãoofatodeserem
“pontes”.Quandousoestametáfora,refiro-meaofatodeelasnospossibilita-
remreaproveitarconhecimentosquejápossuímosemuitasvezessequernos
damoscontaouvalorizamos.
AprimeiragrandepontenaminhaopiniãoéalinguagemGroovy.Nãoé
raroquemeusclientessejamdesenvolvedoresproficientesemtecnologiasque
ficamforadoambienteJavaeposteriormentepassemadominá-lojustamente
porteremusadocomoponteoGroovy.
Groovyéumalinguagemcujasintaxeéfácildeserentendidaporaque-
lesquenãoestãoacostumadosaoJava. Coisassimplescomoocaractere ;
oumesmoousodeparêntesesemchamadasdefun çõespodemparecerbu-
rocráticosparaestesprogramadores(eelesestãocertos). Groovyostorna
opcionais,assimcomotantasoutras“frescuras”,oqueacabagerandouma
portadeentradaaoecossistemaJavamuitomaishospitaleira.
Ocontráriotambéméverdade:vejoprogramadoresJavasetornaremme-
lhoresprogramadoresJavagraçasaoGroovy(éomeucaso).Vocêtemaliber-
dadedeirexperimentandoaospoucosconceitosquemuitasvezesparecem
assustadores,comotipagemdinâmica,programaçãofuncionaletantosou-
tros. Esabeoqueémaislegal? AsintaxedoGroovyépróximaàdoJava:
namaiorpartedasvezessevocêcompilarseucódigoJavacomocompilador
Groovy,nãoháproblemas.
3

## Página 10

1.2. PorqueGroovy? CasadoCódigo
Mascomoassim? Nopenúltimoparágrafovocêdissequeasintaxedo
Groovyéparecidacomadelinguagensdeprogramaç ãoqueestãoforado
ecossistemaJava,enoúltimofalouqueparececomadoJava.Comoassim???
Istomesmo:Groovyépróximadosdoisextremosevocêoverácomdetalhes
apartirdospróximoscapítulos.
Voltandoàponte,vocênãoprecisadargrandessaltos,vocêcaminhanor-
malmentedeumaextremidadeaoutraaproveitandooquevocêjáconhece
eaprendendonovascoisasacadapasso. Groovymeensinouprogramaç ão
poliglota,oqueumalinguagemdinâmicarealmenteé,programaç ãofuncio-
nal,novasmaneirasdesepensarAOPemesmomeforneceuumavisãomais
críticaemrelaçãoaoJavaediversasoutraslinguagens.Etudoistoreaprovei-
tandooquejáconhecia:meuconhecimentosobreoJavaeasoutraslingua-
gensquemeformaram(PHP,Delphi,VisualBasic).
GrailséapontequenoslevaadominaraplataformaJavaEE.Nãoéum
exagerodizerquevocênãoprecisasaberpraticamentenadasobreoJavaEE
paradesenvolverumaaplicaçãowebcomGrails.Poucoapoucovocêiráex-
perimentandomaisoframework,curiosoarespeitodoseufuncionamento
e,conforme“caminhaporestaponte”,umbelodiaperceberáqueagoraco-
nheceumasérie(talveztodas)daquelassiglasenomesquesoavamestranhos
emseuprimeirocontatocomoJavaEE.
EsevocêforumprogramadorquejádominaoJavaEE?Grailslheforne-
ceráumavisãomaiscríticaarespeitodomodocomovocêinteragiacomsuas
tecnologiase,nãoraro,inclusivelheapresentaráemalgunsmomentosaas-
pectosdaplataformacomosquais,muitasvezes,acidentalmenteiráconhecer
nestecaminho.
1.2 P or que Groovy?
ExisteumacertaresistênciaaoGroovyporservistocomouma“meralingua-
gemdescript”eque,portanto,nãoseriaapropriadaparaaescritadeaplica-
çõesreais.Nadamaislongedaverdade:Groovytemsidousadoemprojetos
gigantescosdeimensaresponsabilidadeportodooglobo. Umexemploéo
projetoAsgard(https://github.com/Netflix/asgard),desenvolvidopelaNet-
flixqueéoresponsávelporgerenciartodooprocessodedeploydesuasapli-
4

## Página 11

CasadoCódigo Capítulo1. ExpulsandootédiodaplataformaJavaEE
caçõesnanuvem,alémdediversosoutrosprojetos.Outroexemplolegal?O
mecanismodebuildadotadoporpadrãoparaaplicaçõesAndroidhojeéo
Gradle(http://www.gradle.org),inteiramenteimplementadoem... Groovy.
Estessãoapenasalgunsexemplos,masnãoseassusteseumdiadescobrirque
jáusaalinguagemháumbomtemposemsaber,vistoqueécomponentede
diversasbibliotecaseframeworksdesucessoentreprogramadoresJavacomo,
porexemplo,oJasperReportseoSpring.
Groovyéumalinguagemdinâmica:istoquerdizerquepodemosalteraro
comportamentodonossocódigoenquantoesteéexecutado.Soaestranhoem
umprimeiromomentomas,comoveremosnodecorrerdestelivro,trata-se
deumaspectopoderosíssimoquenospermiteescreverprogramasqueseriam
muitomaistrabalhososemJavaconvencional. Estaé,inclusive,aprincipal
característicadalinguagemquepropiciouacriaç ãodoGrails.
Comoveremosnocapítuloseguinte,linguagensdinâmicasnospermitem
executartarefasemtempodeexecuçãoqueemoutraslinguagenssósãopossí-
veisnomomentodacompilaçãoouatravésdepadrõesdeprojetoousoluções
arquiteturaisquenemsempresãoasmaisamigáveis.
Adotaroparadigmafuncionaldeprogramaçãotambémémaisfácilgra-
çasàpresen çadastãofaladas closures,umrecursoquesóapareceunaversão
8doJava.Veremosoenormelequedepossibilidadesqueelasnospropiciam,
comoareduçãodecódigo boilerplatequenormalmenteprecisamosescrever
emJava.
Tambémnãopodemosdeixardecitarasmelhoriassintáticasoferecidas
peloGroovy:háconstrutoresquenospossibilitam,porexemplo,lidarcomas
coleçõesJava(aAPICollections)deumaformamuitomaissimpleseeficiente.
Alémdisto,entramcomoagregadosinteressantesumanovasintaxeparali-
darcomstrings,apossibilidadedesobrecarregarmosoperadores,lidarcom
númerosdotipo BigDecimaldeformamaisnatural,estruturasdecontrole
aprimoradasemuitasoutrasfacilidadesquetornamaescritadecódigouma
tarefamuitomaisprazerosaesimplesdoqueaexperiênciaquetemoscomo
Javatradicional.PenseemtodasascoisasnalinguagemJavadequevocênão
gosteeasexclua:esteéoGroovy.
Umacríticafrequenteàlinguagemdiziarespeitoaoseudesempenho,que
realmenteeraconsideravelmenteinferioraodoJava.Esta,entretanto,éuma
5

## Página 12

1.3. PorqueGrails? CasadoCódigo
realidadebastantediferentehojeemdia.Comosavan çosemseudesenvolvi-
mento,podemosdizerquenaversão2.4émuitopróximaàdoJava,oquea
tornaumaalternativaviávelparaaimplementaçãodamaiorpartedosproje-
tosvoltadosparaaJVMdesenvolvidosatualmente.Alémdisso,minimizaa
curvadeaprendizadodestaporaquelesquejáconhe çamoJavatradicional.
(Sebemquetodaconversasobredesempenhosófazsentidoquando
existeumrequisitoquenosdigaqualodesempenhoquenossosistemadeverá
apresentar.)
Parafinalizar,alinguagemGroovypossuioutracaracterísticaqueatorna
atraenteaosolhosdosdesenvolvedores: ofatodesercompletamentecom-
patívelcomseucódigoJavaexistente.Comisto,odesenvolvedorpoderea-
proveitartodaabagagemexistentenaplataformaJava,queatualmentepossui
amaiorbibliotecadecódigo-fontedesenvolvidaporterceirosnahistóriada
computação.SeucódigoJavapodeseracessadodeformatransparentepelo
seucódigoGroovyevice-versa.
Há,noentanto,umaspectobastantenegativonalinguagemGroovyque
jádevoadiantaraoleitor. Umavezadaptadoaoseumododetrabalho,
acostumar-senovamenteaomododeprogramaroferecidopelalinguagem
Javatorna-seumatarefabastantepenosa.:)
1.3 P or que Grails?
Grailséumframeworkparadesenvolvimentodeaplicaçõeswebprofunda-
menteinfluenciadopeloRubyonRails(seuprimeironomesequereraGrails,
massim“GroovyonRails”). Paraentenderosganhosqueelenostrouxe,
primeiroéprecisolembrardomundoem2004quandoRailschocouatodos
nós.
Aoserlan çadoem2004,RubyonRailsmudouparasempreamaneira
comaqualestávamosacostumadosaescreveraplicaçõeswebparaaplata-
formaJava(enemeravoltadoparaJava!).Foiumtapanacaradetodosnós,
desenvolvedoresJavaEE:derepentevíamosdiantedosnossosolhoscomo
erapossíveldesenvolveraplicaçõeswebsemanecessidadedeenfrentarin-
contáveisarquivosdeconfiguração,talcomoestávamosacostumadosafazer.
Emvezdisso,foiapresentadoalgocomumemoutrasplataformas:odesen-
6

## Página 13

CasadoCódigo Capítulo1. ExpulsandootédiodaplataformaJavaEE
volvimentobaseadoemconven çõeseemumalinguagemdinâmica,nocaso
Ruby.
Atéaquelemomento,estávamosacostumadosao“modoJava”detraba-
lhar:arquivosdeconfiguração XMLqueatingiamtamanhosdifíceisdeserem
gerenciados,comumcódigoburocráticoqueprecisavaimplementarumaou
maisinterfaces.
Alémdisso,haviaumambientededesenvolvimentobaseadoemumciclo
dotipoescreve,compila,instalanoservidoreoreinicializaparaversefunci-
onoudireitoocódigoimplementado.Umprocedimentotedioso,lentoeque
minavacompletamenteaprodutividadedodesenvolvedor.
Grailsfoiumadasrespostasapresentadasaestasituaç ão,cujaversão1.0
foilançadaem2008.EracomotrazeroRubyonRailsparaaplataformaJava.
Assimcomonaqueleambiente,tínhamosumframeworkdepilhacompleta
(full stack),ouseja,odesenvolvedornãoprecisavasepreocuparcomainte-
graçãodesuasdiversasbibliotecas,comooHibernateparapersistência,Log4J
paralogging,Springemuitasoutras.TínhamosalitodasasestrelasdoJava
finalmenteintegradas,prontasparaouso:odesenvolvedorpodiacome çara
implementarsualógicadenegócioimediatamente.
Tínhamostambémumprocessodedesenvolvimentobemmaiságil: o
antigocicloescreve-compila-instala-reiniciaviroupassado. Alteraçõesem
nossocódigo-fonteimediatamenteeramrefletidasnaaplicaçãoemexecução,
possibilitandoaoprogramadorverdemaneiraimediataoresultadodesuas
alteraçõesemtempodeexecução.
Eosarquivosdeconfiguraç ãoeram,emsuamaiorparte,apenasuma
tristelembrançadopassado.Comoamaiorpartedasbibliotecascomasquais
estávamoshabituadosatrabalharjáestavamprontamenteintegradas,tudo
oqueprecisávamosfazer(emesmoassimopcionalmente)eraconfigurara
nossaconexãocomobancodedados.
• Oscaffoldingqueautomaticamentegeraparaodesenvolvedorasca-
madasdevisualizaçãoecontroletendocomobasenossasclassesde
domínio.
• InjeçãodedependênciaseinversãodecontrolebaseadaemSpring.
7

## Página 14

1.3. PorqueGrails? CasadoCódigo
• DiversasdasprincipaisbibliotecaseframeworksJavaprontamentein-
tegrados,detalmodoquenãoprecisamosnospreocuparmaiscom
isto.
• Umaarquiteturadeplug-insquenospermitemodularizarnossospro-
jetoseenriqueceroframeworkdeumaformabastanteinteressante.
• Ébaseadoemumadaslinguagensmaisprodutivasjácriadas:Groovy.
• Enãopodemosesquecerdemencionarnossavibrantecomunidade,
tantonacionalquantointernacional.
Omodocomolidamoscomapersistênciaevalidaçãodedadostambémé
maissimplescomGrails.TemosoGORM,nossoframeworkparapersistên-
cia,queatualmentetrabalhatantocombasesdedadosrelacionaiscomonão
relacionais,comooMongoDB.Nãoénecessárioaodesenvolvedorsepreocu-
parcomanotaçõesouarquivosdemapeamento.Comoveremos,éumpro-
cedimentosimplesedireto. Odesenvolvedorsóprecisalidarcomomodo
comosuasclassessãomodeladas,comodeveriaserdesdeoinício.
PortrásdospanostemosoSpring,atualmenteumdosmelhores(talvez
omelhor) containerdeinversãodecontroleeinje çãodedependênciasdo
mercado.Paraasurpresademuitos,esteraríssimasvezesserávistodeforma
diretapelodesenvolvedor. Seuusotambémfoiradicalmentemelhoradoe
injetardependênciasnuncafoitãofáciletransparente.
ÉinteressanteobservarqueoacessoadiversasfuncionalidadesdoJavaEE
tambémfoisimplificadocomGrails.Paracadarecursodaplataformacorpo-
rativaJavaháumainterfaceGrailsquefacilitaoseuusoparatodosaqueles
quepossueminteresseemtrabalharcomJavaEEmassesentemintimida-
dosporsuaaparentecomplexidade. Grailsresolvedeumaformabastante
eleganteesteproblema.
Omaisimportanteéque,finalizadoseuprojetoGrails,oresultadoéuma
aplicaçãoJavaEEcompleta,comosmesmosdireitosquequalquerumaescrita
paraaplataformapossui:altadisponibilidade,escalabilidade,desempenhoe
robustez.E,comobrinde,hátambémofatodeocódigoGrailsseraltamente
portávelentreservidoresdeaplicação,evitando-lheestetipodedordecabe ça
nofuturo.
8

## Página 15

CasadoCódigo Capítulo1. ExpulsandootédiodaplataformaJavaEE
Trata-sedeumframeworkdiretoaofoco: odesenvolvedorvêminimi-
zadootempoqueatéentãoeragastocomcomplexidadesnãofuncionais,
comointegraçãodebibliotecasegerênciadeservidores.
Apartirdeagora,ofocopassaasernoquerealmenteinteressa,osistema
queprecisaserescrito,enãomaisemproblemasperiféricos.
AcomunidadeGrailstemcrescidobastantenoBrasil. Quandofundei
oGrailsBrasil(http://www.grailsbrasil.com.br)em2008,logonoprimeiro
mês,paraminhasurpresa,éramos60.Em2015,contamoscommaisde2100
membros(eonúmeronãoparadecrescer)queparticipamativamenteaju-
dandoaquelesqueestãoiniciando,resolvendosuasdúvidaseproblemas,es-
crevendonovosplug-insefuncionalidadesparaoframework.
AssimcomoGroovytornaaescritadecódigoumprocessomaissimples
epragmático,omesmoobservamoscomGrails,queacabacomotédiono
processodedesenvolvimentodeaplicaçõeswebparaaplataformaJava.
1.4 S obre este livro
Amaiordificuldadequeenfrenteiaoescreverestelivrodizrespeitoaoseu
formato. NãoacreditoqueanaturezadinâmicadeGroovyeGrailspossa
serpassadausandooformatodeprosatradicional,porestarazãoopteipelo
diálogocomomeioprincipaldenarração.Emminhaexperiênciacomocon-
sultornestaseoutrastecnologias,jáconstateiqueoprocessodeaprendizado
sedádeumaformamuitomaisnaturaleeficientequandoaprosaentraem
cenaeasformalidadessetornamapenasumacessório(necessário).
Aolê-lo,penseemumgrandediálogocomigoeaspersonagensqueentra-
rãoemsuavidaduranteaexperiência.Asconversasquevocêacompanhará
sãoreaiseasexperimentosemprequeapresentoestastecnologias.Esque çao
formato“manual”padrão:aofalarmosdeGroovyeGrails,oquerealmente
importaéainteraçãoeomodocomolidamosunscomosoutros.
Aliás,sabemosqueestemododedescreveromundofuncionamuitobem
desdeaGréciaantiga(láporvoltadeuns300a.C.),queexerceufortíssima
influêncianaescritadestelivro. Nãoháinovaçõesnoquefizaqui: apenas
resgateiumapráticaantiga.
Algumaspartesdolivrodevem,naminhaopinião,serlidascomaten-
9

## Página 16

1.4. Sobreestelivro CasadoCódigo
çãoredobrada.Nocaso,refiro-meaoscapítulossobreGroovyeGORM.Na
maiorpartedosprojetosemqueviaaplicaç ãodoGrailsfracassar,oprincipal
vilãofoisemsombradedúvidasonãoconhecimentodestasduastecnologias.
“PenseGroovy”aousarGrails,efiqueatentoàs“armadilhas”queapontodu-
rantetodoestetrabalho.
Éimportantelheavisarqueusootermo“armadilha”nãoéparaapontar
bugsnaplataforma,massimparasalientaraspectosdoseufuncionamento
quenãosãoconhecidospelavastamaioriadosprogramadoresequemuitas
vezespoderácustar-lheinúmerashorasquepoderiamsergastasemativida-
desmaisúteis. Sendoassim,aoveroíconeaseguir,jásabe:aten çãoredo-
brada!
Fig.1.1:Atençãoredobrada!
Duranteaescritadestelivrousamosaversão2.4.4doGrailseorelease
3.0.0estavaseaproximandoefinalmentefoilan çadonodia31/3/2015.Dado
serumaversãonaqualgrandespartesdoframeworkforamreescritas,aquan-
tidadedebugs(“oportunidadesdemelhoria”)costumasersignificativa,ra-
zãopelaqualnãolherecomendoadotarestaversãonestemomento(abrilde
2015),massimemumfuturopróximo,quandosaíremasversões3.0.4ou
posteriores.Masissonãoquerdizerqueestamoslan çandoumlivrodesatu-
alizado,pelocontrário!
Emdiversaspáginasvocêencontraráoíconeaseguir:
10

## Página 17

CasadoCódigo Capítulo1. ExpulsandootédiodaplataformaJavaEE
Fig.1.2:Compatibilidade
Eleindicaqueireifalarsobreoqueserádiferentenaversão3.0doGrails
oudomodocomoversõesantigasfuncionavam.Alémdisto,tambémmepre-
ocupeiemincluircomocapítulofinalumadescriçãodasprincipaismudan ças
trazidaspelaversão3.0.Nãoseassuste:sãopoucasepraticamentetudooque
veremosnestaspáginasseaplicaquasequesemalteraç ãonenhumananova
grandeversão.
1.5 C ódigo-fonte
Neste livro, iremos desenvolver uma aplicação cujo código-fonte pode
ser baixado no GitHub neste link:https://github.com/loboweissmann/
FalandoDeGrails
Tratam-sededoisprojetos: ConCot,queéaaplicaçãoprincipal(vocêverá
maissobreelamaisàfrente)e DDL-Plugin-Itens,queéumplug-inquede-
senvolveremos. Ofuncionamentodoprimeirodependedosegundo,sendo
assim,bastacopiarodiretórioraizdoprojetoparaumlocaldesuapreferên-
cia,quetudodeveráfuncionarperfeitamente.
Casotenhaalgumproblema,jásabe:podeentraremcontatodiretamente
comigoporqualquerumadasfontesaseguir:
• E-mail:kico@itexto.com.br
• Twitter:@loboweissmann
11

## Página 18

1.6. Agradecimentos CasadoCódigo
1.6 A gradecimentos
Estaéaquelapartedolivronaqualtenhocertezadequesereiinjustopoisa
quantidadedepessoasquemeincentivarameapoiaramnaconclusãodeste
trabalhoé muitogrande.
Paracomeçar,agradeçoatodososamigosquefiznacomunidadeJava
eGroovy,especialmentenoGrailsBrasil(http://www.grailsbrasil.com.br).
Quandomelembrodecomoascoisasseiniciaramem2008,naquelefórum
quecrieiusandophpBB(sim,PHP),quecome çouareunirpessoasqueque-
riamajudaroutroscolegaseaprenderaqueleframeworkelinguagemquenos
pareciamtãoalienígenas,equehojevejosendoaplicadosemumaimensidão
deempresaseprojetos,confessoficarsemfôlego.Agrade çoatodosvocês.
Agradeçotambémàpaciência(aparentementeinfinita!),suporteeaten-
çãoqueAdrianoAlmeidaePauloSilva,editoresda Casa do Códigoque,sem
exagero,consideroverdadeirosheróisquealavancamapropagaç ãodoco-
nhecimentoemnossaárea,mesmocomtodasasdificuldadesequeinclusive
apostaramnoformatodiferenciadoqueescolhiparaaescritadestelivro.
Nãotemcomonãoagradecertambémàmelhorcoisaqueocorreuemmi-
nhavidaquesechamaNanna(oficialmenteconhecidacomoMariaAngélica
ÁlvaresdaSilvaeSilva). Tantoscafés,discussõesesuportequenãotenho
palavrasparadescrever.
Ah,claro:nãotemcomonãoagradeceraoPlatão,Trasímaco,Xenofonte
ealgunsoutrosqueinfluenciaramdeformaprofundaomodocomodecidi
escreverestelivroe,claro, Daniel, Gutoe Dedéquesemsaberacabaramen-
trandonestahistória.
Paraevitarqueeusofra“consequênciasimprevisíveis”,novamenteagra-
deçoàminhamãe,SelmaWeissmann.:)
Obrigado,obrigadoemilvezesobrigadoatodosvocês!
Emildesculpasaqualquerumqueeunãotenhacitadodiretamenteaqui.
(Sebemqueninguémlêase çãodeagradecimentosmesmo.)
12

## Página 19

Capítulo2
Groovy:umabreveintrodução
Groovyéumalinguagemdeprogramaçãoquetemumasintaxebastantepare-
cidacomadoJava,oquetrazprósecontras:porumlado,facilitasuaado ção
porestesprogramadoresdadasuasimilaridadeetambémporsuprirdiversas
deficiênciasdalinguagem.Poroutro,acabagerandoproblemasparaaqueles
quecomeçamadarosprimeirospassoscomGrails:nãoérarooprograma-
doracreditarestarlidandocom“umaespéciedeJava”e,comisto,perdera
chancedetirarmáximoproveitodalinguageme,consequentemente,dopró-
prioGrails.
Casoqueiraadicionarmaisumalinguagemàsuacaixadeferramentas(o
quesemprerecomendo),bemvindo(a)!Tor çoparaqueaofinaldaleiturados
capítulossobreGroovyvocêsesintamotivadoaadotarestaque,acredito,seja
umadasmaisprodutivaslinguagensdeprogramaç ãoqueconhe ço.

## Página 20

2.1. Paraqueoutralinguagemdeprogramação? CasadoCódigo
2.1 P ara que outra linguagem de programação?
UmaperguntacorrentequeouvimossobreGrailsé: seráqueoframework
nãoseriamuitomaispopularsefossebaseadonalinguagemJavaemvezde
Groovy,dadoqueonúmerodeprogramadoresJavaé bemmaior?Parares-
ponderaestapergunta,bastaolharmosparaoanoemqueGrailschegouà
versão1.0:2008. NessaépocaaversãomaisusadadalinguagemJavaeraa
6.0,lançadadoisanosantes.Aperguntaquesefazé:oquefaltavanoJava?
Faltavamclosures,facilidadesdemetaprogramaçãofacilmentealcan çá-
veiscomlinguagensdinâmicasediversasoutrasfuncionalidadesdasquaisa
implementaçãodoGrailsusaeabusa.TodasestasausênciasdoJavapoderiam
sersuperadasusandoapróprialinguagemapartirdaimplementaç ãodeno-
vasbibliotecasouAPIs,masseráqueocustonaimplementaç ãodetodoeste
códigovaleriaapena? Sevalesse,hojeteríamosapenasJavaexecutandona
JVM,noentantonãoéoqueobservamosquandoolhamosparalinguagens
comoGroovy,Clojure,Scala,JRuby,Jythonetantasoutras.
EstaperguntanoslevaaumtemamuitointeressantedaCiênciadaCom-
putação:aquestãodaequivalênciaecompletudedeTuring[30]( Turing Com-
pletee Turing Equivalence). Nadécadade1930,omatemáticoinglêsAlan
Turingnostrouxesuafamosa Máquina de Turing,ummodelomatemático
quedefiniuomodocomo“tudooqueécomputacional”funcionaatéosdias
atuais.Estaéumateoriatãoprofundaquedeuorigeminclusiveaumramo
daciênciachamado Física Digital,quedizsertodooUniversodescritopor
informaçãoe,portanto,computávelepassíveldesertratadodigitalmente(e
nemmencioneiacomputaçãoatual).
AmáquinadeTuringnosforneceasoperaçõesbásicasportrásdacom-
putação,eumelementoédito Turing completequandoasconsegueexecutar.
UmalinguagemdeprogramaçãoorientadaaobjetoscomoGroovyeJavasão
Turing complete.Edeondevemestepapodeequivalência?SealinguagemA
éTuring completeassimcomoaB,entãoosprocedimentosdeApodemser
convertidosemBevice-versa.Aconsequênciaimediataéquenaessênciao
quevocêpodefazercomGroovyouScalatambémpodeserfeitoemJavae
vice-versa,ouseja,todasaslinguagensdeprogramaç ãoquecaibamnestaca-
tegoriasãoequivalentes.Então,porquenãoficamosapenasnoFortran?Por
quecriamostantaslinguagensdeprogramação?
14

## Página 21

CasadoCódigo Capítulo2. Groovy:umabreveintrodução
Arespostaésimples: notaçãoecomodidade. Sim, eupossoobtero
mesmoresultadocomputacionalcomJavanoFortran,masotrabalhoque
eutenhoparataléenormeesimplesmentenãocompensa.Estaéarazãopela
qualnovaslinguagensdeprogramaçãosurgem:assim,vocêpodefazermais
comumanotaçãomaisagradáveloupróximadoobjetivoaqueseuprograma
visa. ÉpossíveltermosorientaçãoaobjetosemC?Sim. Émaistrabalhoso
comCouJava?
EscrevercódigodinâmicoémaisfácilemGroovyouJava?Comoveremos
nestecapítuloenospróximos,comcertezaemGroovy.
2.2 A final de contas, o que é o Groovy?
Apóstodaestateoria,aperguntaóbviaaindanãofoirespondida: oqueé
Groovy?Obásicooleitorjásabe:trata-sedeumalinguagemdeprogramação.
AssimcomoJava,éorientadaaobjetosedesenvolvidaparaquesejaexecutada
na máquina virtual Java(JVM).
A Máquina Virtual Jav a
OquepermitequeumprogramaescritoemJavasejaexecutadoem
qualquersistemaoperacionaléaMáquinaVirtualJava,tambémconhe-
cidacomoJVM(Java Virtual Machine).Elabasicamentesimulaumcom-
putadorrealque,emvezdeexecutarcódigodemáquinanativocomo
ocorrecomseurelativofísico,interpreta bytecode.
BytecodeéalínguafrancaentendidapelaJVM.Todocódigo-fonte
Javaéconvertidoparaesteformato,queéindependentedesistemaope-
racional.Praticamentetudooqueumsistemaoperacionalprecisapara
poderexecutarcódigoJavaépossuirumaimplementaç ãodaJVM,por-
tanto.
Mashámaisdiferen ças:Groovyéumalinguagemdinâmica. Issoquer
dizerqueconsegueexecutartarefasqueemlinguagensestáticassóseconse-
gueemtempodecompilaçãoouadotandotécnicascomopadrõesdeprojeto
quenemsempresãosimples.Quetarefassãoessas?Basicamente,modificar
15

## Página 22

2.2. Afinaldecontas,oqueéoGroovy? CasadoCódigo
códigoexecutávelemtempodeexecução.Épossível,porexemplo,incluirno-
voscomportamentos(métodosefun ções)emnossasclassesoualterarcódigo
preexistente.Maisqueisto,nocasodoGroovy,aindatemosacessoàAPIde
reflexãodeumaformamuitomaissimplesediretadoquenoJavatradicional.
Nasemelhançatambémhádiferenças:Groovynosapresentaumasintaxe
muitopróximadoJava,reduzindoacurvadeaprendizado,masaomesmo
tempoaaprimora,simplificandotarefasatéentãochatasdalinguagem. A
grossomodo,nãoéexagerodizerqueGroovyéumaespéciede “Java++
. PenseemalgoquesejaverbosoemJava, comolidarcomaclasse
BigDecimal.Umrápidoexemplo:imaginequequeiramosimplementaro
deltadeumaequaçãodesegundograuemJava.Escreveríamosalgocomoo
códigoaseguir:
BigDecimal delta(BigDecimal a, BigDecimal b, BigDecimal c) {
return b.multiply(b).subtract(new BigDecimal(4).multiply( a).multiply(c)
}
EemGroovy?
BigDecimal delta(BigDecimal a, BigDecimal b, BigDecimal c) {
(b*b) - (4*a*c)
}
Comoveremosnestecapítuloenopróximo,hádiversasoutrasmelho-
riasapresentadaspelalinguagem.Apropósito,outramudan çainteressanteé
queapenassevocêquiseratipageméestática.Soaestranhoparaquemestá
acostumadocomJava,maséumestilodeprogramaç ãobastanteprodutivo.
Parasatisfazersuacuriosidade,nossaversãododeltapodeserescritaem
Groovytalcomoocódigoaseguir.Groovydescobriráemtempodeexecuç ão
comqualtipodevetrabalhare,acredite,semprefunciona!:)
def delta(a,b,c ) {
(b*b) - (4*a*c)
}
Étambémumalinguagemdescript. AocontráriodoJavaemquetodo
códigoexecutávelobrigatoriamenteprecisaestarcontidoemumaclasse,o
mesmonãoocorreemGroovy.Curiosodenovo?Compareosdoiscódigosa
seguircomobatidoexemplodo“Olámundo":
16

## Página 23

CasadoCódigo Capítulo2. Groovy:umabreveintrodução
public class OlaMundo {
public static void main(String args[]) {
System.out.println("Oi Mundo!");
}
}
EemGroovy?
println "Oi Mundo!"
SerumalinguagemdescriptqueexecutanaJVMtornaGroovyumaex-
celenteferramentaparamanuten çãoeadministraçãodesistemasJava. Por
quê?PorquecódigoGroovynofinaldascontasvirabytecodeeacessatrans-
parentementeseucódigoJavalegado. Sim: aindaháestavantagem. T odo
o seu código Java pode ser usado pelo Groovy e vice-versa. Outravanta-
gemdesteaspecto“script”équeaqueleciclodedesenvolvimentoescreve-
compila-executavirasimplesmenteescreve-executa,oqueaumentabastante
asuaprodutividade.Veremosmaissobreistonestecapítulo.
Muitateoriafoiexposta,éhoradeirmosàprática.
2.3 I nstalando Groovy
InstalaroGroovyébastantesimples.Vouexporaquiumprocedimentorá-
pidoquepodeseraplicadoaqualquersistemaoperacional.
1) Baixe a última versão do Groovy emhttp://www.groovy-lang.org/
download.html.Optepelaop çãonoformato zip;
2) Descompacteoarquivoemumdiretóriodesuapreferência;
3) Crieumavariáveldeambientechamada GROOVY_HOMEqueapontepara
odiretórionoqualvocêdescompactousuadistribuiçãodoGroovy;
4) Casoexistaumavariáveldeambientechamada JAVA_HOMEemseucom-
putador,certifique-sedequeelaaponteparaumainstalaç ãodoJDK(é
requisitoparaainstalaçãodoGroovy);
5) Adicioneodiretório GROOVY_HOME/binao PATHdoseusistema.
17

## Página 24

2.4. GroovyConsole:seulaboratóriopessoal CasadoCódigo
Apósessespassos,abrasuainterfacedelinhadecomandoeexecuteo
comando groovyconsole.Setudodercerto,surgiráumajanelasimilaràque
exponhoaseguir.
Fig.2.1:GroovyConsole:nossoamigonospróximoscapítulos
2.4 G roovy Console: seu laboratório pessoal
OGroovyConsoleéumapoderosaferramentaenosguiaránestelivrodaqui
parafrenteenquantonossofocoforalinguagemGroovy.Esteéoquenormal-
mentechamamosde REPL.REPLéumacrônimopara Read Eval Print Loop,
ouseja,umainterfacequeusamosparaexecutarrapidamentenossocódigo-
fonteeteracessoimediatoaoresultadodoseuprocessamento. Aimagem
aseguirilustramuitobemseufuncionamento. Digitamosnossocódigona
partedecimadajanela;eleéexecutadoevemosimediatamenteoresultado
18

## Página 25

CasadoCódigo Capítulo2. Groovy:umabreveintrodução
doprograma.
Fig.2.2:AinterfacedoGroovyConsole
Paraexecutarseucódigo-fontepeloGroovyConsolehádoiscaminhos.
Vocêpodeiraomenu Scripteclicarsobreaop ção Runousimplesmente
usaroatalhodeteclado Ctrl + R.Outroatalhomuitoútilé Ctrl + W,
quelimpaapartedebaixodajanela,facilmentepoluídaconformevamos
usandooREPLemnossosexperimentos.
VejaoGroovyConsolecomoseulaboratóriopessoal.Eleéumaexcelente
ferramentaquevocêpoderáusarparaesboçaralgoritmosetestarouaprender
algumaAPIquelheinteresse.
Casoestejatrabalhandoemumambienteprivadodeinterfacegráfica,há
umaalternativaparaoGroovyConsole:trata-sedocomando groovysh,que
iniciaráumREPLnomodosomentetextoparavocê,talcomoilustradona
imagemaseguir:
19

## Página 26

2.5. “Olámundo” CasadoCódigo
Fig.2.3:Groovysh:aversãotextualdoGroovyConsole
2.5 “O lá mundo”
Todaintroduçãoaumalinguagemdeprogramaç ãocome çacomoexemplo
maisrepetidodahistóriadacomputaç ão,o“Olámundo”. Narealidadejáo
expusnase ção2.2,maséinteressanterepeti-lo,paraquepossamosentender
oqueestáacontecendo.
println "Olá mundo"
NãoéprecisoenvolvernossocódigoemumaclassecomoocorreemJava
ouumafun ção maincomonoC.Ométodo printlntambémnosdizalgo.
Parece-lhefamiliar? TalvezvocêjáoconheçadoJava,comonoexemploa
seguir,quetambémfuncionaperfeitamenteemGroovy:
System.out.println("Olá mundo");
OmesmocódigopoderiatambémserescritodaseguinteformaemGro-
ovy:
println "Olá mundo"
20

## Página 27

CasadoCódigo Capítulo2. Groovy:umabreveintrodução
Istomesmo,parêntesessãoopcionaisemGroovy.Omesmopode-sefalar
arespeitodofamosocaracteredepontoevírgula(;),tambémopcional.Uma
versãomaispróximadoJavadonosso“Olámundo”podeservistaaseguire
éigualmenteválida:
println("Olá mundo");
Então,quandopontoevírgulaéusado?Quandovocêquiserincluirdois
oumaiscomandosemumamesmalinha:
println "Oi mundo" ; println "Tudo bem com você?"
Apropósito,oúltimopontoevírgulatambéméopcionalnestecaso,já
quenãoteremosmaisnenhumainstruçãonessalinha.
2.6 V ariáveis: tipagem “opcional”
Variáveissãoespaçosdememóriaparaarmazenarvaloresusadospornossos
programas.Todavariávelpossuitrêsatributos:tipo,nomeevalor.Quando
falamosemGroovy,oprimeirodestesatributos otipo podeserdescoberto
emtempodeexecução.Podemosatémesmonãoodeclarar,masporbaixo
dospanos,nãoseiluda,háumtipo.
Otipodeumavariávelpodeseralgocomotextos,números,booleanos
emuitosoutros.AdeclaraçãodeumavariávelemGroovypodeserfeitatal
comoestamosacostumadosemJava:
int numero
Noentanto,vistoqueotipoédescobertoemtempodeexecuç ãoquando
estamosfalandodeGroovy,estepodeseromitidonadeclaraç ãodeumava-
riável.Paratal,usamosapalavrareservada def,quenapráticasignificaria
algocomo não me importa saber qual o tipo desta variável, este será definido
em tempo de execução.Ocódigoaseguirexpõebemestecomportamento:
def variavel
// variável passa a armazenar um valor numérico
variavel = 4
21

## Página 28

2.7. TrabalhecomStrings CasadoCódigo
// variável passa a armazenar um valor textual
variavel = "Algum texto"
Casoovalordavariávelsejadefinidoemsuadeclaraç ão,apalavrareser-
vada defsetornaopcional.Ocódigoaseguiréperfeitamenteválido:
pi = 3.14 // automaticamente vira BigDecimal
Asmesmasregrasaplicadasnadeclaraçãodevariáveisvalemtambémna
definiçãodeparâmetrosemumafun ção. Podemosomitirtantootipode
retornoquantootipodecadaumdosparâmetros:
def soma(a,b) {
return a + b
}
EssessãoapenasalgunssimplescasosondeocódigoGroovyébemmais
enxutodoqueoescritoemJava.
2.7 T rabalhe com Strings
Usamosotipodedados Stringquandolidamoscominformaçãotextual
eesteéumaspectodoGroovyquecostumacativardiversosprogramado-
resJavaportornarasuamanipulaç ãomuitomaissimples. Aliás,nãomais
simples,massimcomosempredeveriatersido.
Aformamaistradicionaldedeclararuma StringemGroovyéexata-
mentecomofaríamosemJava.
String linguagem = "Groovy"
Não se engane, não estamos lidando aqui com a mesma string
que usamos em Java, mas sim uma GString ( Groovy String
groovy.lang.GString),quetrazconsigoalgunstruquesbeminteressan-
tes,acome çarpelaconcatenação,queagoraficabemmaissimples.EmJava,
concatenamosassim:
22

## Página 29

CasadoCódigo Capítulo2. Groovy:umabreveintrodução
String prefixo = "Programando em ";
String sufixo = "Groovy";
String fraseCompleta = prefixo + sufixo;
// Resultado: "Programando em Groovy"
EmGroovy,podemosfazerexatamentecomoemJava,masporquecon-
catenarsepodemos interpolar? AssimcomoemPHPeRuby,Groovynos
permitedefinirpontosemuma Stringqueserãopreenchidoscomoque
quisermosemseuinterior.Confuso?Vejaoexemploaseguir:
String sufixo = "Groovy"
String fraseCompleta = "Programando em ${sufixo}"
println fraseCompleta
// resultado: "Programando em Groovy"
Nointeriorde ${},deveserincluídaumaexpressãoqualquer,quepode
sertantoovalordeumavariávelcomooresultadodeumaexpressãomate-
máticaoulógica:
int a = 3
int b = 5
String expressao = "${a} + ${b} = ${a + b}"
println expressao
// resultado: "3 + 5 = 8"
Talvezvocênãoqueiraexecutarumaexpressãotãosimplescomoretornar
ovalordeumavariável. Nestecaso,tudooquevocêprecisafazeréusara
sintaxe $,queébastantesimples:
int a = 3
def texto = "Qual o valor de a? É $a"
println texto
//resulta em
//"Qual o valor de a? É 3"
Bastaqueseguindoocaractere $sejaincluído,semespaços,onomeda
variávelcujovalorqueremosinterpolaremnossa String.Simplesassim.
23

## Página 30

2.8. OqueéverdadeemGroovy? CasadoCódigo
Háoutratarefaquefazpartedocotidianodetodoprogramadoreque
normalmenteébastantechata: lidarcomstringsquesejamcompostaspor
maisdeumalinha.EmJava,nãoéraroencontrarcódigocomoeste:
String muitasLinhas = "Olá mundo!\n" +
"Estou aprendendo Groovy.\n" +
"E me encantando com a linguagem. :)";
EmGroovy,bastadeclararmosnossa Stringnãocomaspasduplas,mas
simtriplascomonoexemploaseguir:
String muitasLinhas = """Olá mundo!
Estou aprendendo Groovy.
E me encantando com a linguagem. :)"""
E,sim,tambémpodemosusarinterpolação:
int a = 3
int b = 5
String muitasLinhasInterpoladas = """a = ${a}
b = $b
a + b = ${a + b}"""
Aindahámaisumtipode Stringquepodemosusar,anativadopró-
prioJava, java.lang.String.Claroqueháumasintaxeespecialparaisto
também,asdeaspassimples:
String stringJava = 'Sou a string padrão do Java'
Sea GStringétãomaispoderosaquea StringpadrãodoJava,por
queusaramenospoderosa? Performance. Sevocênãofortrabalharcom
textopresenteemmúltiplaslinhasouinterpolaç ão,émuitomaisvantajoso
usaraversãomaissimplesquesuprebemasnecessidadesdoseucódigo,não
émesmo?
2.8 O que é verdade em Groovy?
OqueéverdadeiroemGroovy?Tambémtemosotipo boolean,querepre-
sentaosvaloresverdadeirooufalso.QuandopensamosemJava,temoscomo
verdadeirasasseguintescondições:
24

## Página 31

CasadoCódigo Capítulo2. Groovy:umabreveintrodução
• Ovalordealgoboolean;
• Oresultadodeumaexpressão,comocomparações.
EmGroovy,omesmoconceitoaindaseaplica,porémexpandido,eeste
éumpontonoqualdiversosprogramadoresJavaacabamcometendoerros
aoseaventurarnalinguagem. Oobjetivodoscriadoresdalinguagemfoi
aproximá-ladalinguagemcoloquial.Parafacilitaraexposiçãodesteconceito,
primeirovoulheintroduzirafun ção assertdoGroovy.Elarecebecomo
parâmetroumaexpressãoe,seestaforverdadeira,nadaocorre,mascaso
contrárioumaexceçãoserádisparada,talcomonoexemploaseguir:
def a = 3
assert a < 4 // nada ocorre: a realmente é menor que 4
assert a != null // nada ocorre
assert a > 5 // uma exceção será disparada
Aexceçãodisparadaébastanteinstrutiva,apontandoondeafalhaocor-
reu,comopodeservistonaimagemaseguir.
Fig.2.4:Assertexpondograficamenteoerro.
25

## Página 32

2.8. OqueéverdadeemGroovy? CasadoCódigo
Agoravoltemosaonossoconceitodeverdade.Seovalorfornulo,écon-
sideradofalso,casocontrárioéverdadeiroemGroovy.Istoevitatermosde
escrevercódigoverboso,oquecostumávamosfazeremJava:
if (pessoa != null &&
pessoa.getNome() != null &&
pessoa.getNome().equals("Henrique")) {
// faça algo após tudo isto
}
EmGroovyacoisaficabemmaissimples:
if (pessoa && pessoa.nome) {
// faça algo
}
Massabiaquedápraficarainda mais simples?
if (pessoa?.getNome()) {
//hein?
}
Ocaractere ?éoquechamamosemGroovydeoperadordenave-
gaçãosegura(safe navigation operator ). Oqueissofazéevitarafamosa
NullPointerException,queocorrequandotentamosacessarumatri-
butooufun çãodeumobjetoquesejanulo. Ocódigoaseguirexpõebem
estafacilidade:
def pessoa = null
pessoa?.grite() // NullPointerException não será disparada :)
Jásabemosqueexpressõesbooleanasenulidadedeobjetosnosdizem
seumaexpressãoéverdadeiraoufalsa. Masomesmotambémseaplicaa
Strings.Uma Stringvaziaéconsideradafalsa:
def texto = "texto"
assert texto // teste passa: verdadeiro, texto não vazio
def textoVazio = ""
assert textoVazio // teste não passa: texto vazio
26

## Página 33

CasadoCódigo Capítulo2. Groovy:umabreveintrodução
Oconceitodeverdadetambémseaplicaavaloresnuméricos. Assim
comonalinguagemC,seumnúmeroforigualazero,eleseráfalso. Caso
contrário,seráconsideradoverdade:
assert 1 // teste passa: verdadeiro pois é diferente de zero
assert -1 // teste passa: verdadeiro pois é diferente de zero
assert 0 // teste falha
Acoisaficainteressantequandoprecisamoslidarcomcole ções(veremos
coisasinteressantíssimasqueGroovynospossibilitafazercomestaAPI).Se
umacoleçãoforvazia,entãoaexpressãoéconsiderada:
def lista = new ArrayList ()
lista.add("Valor")
assert lista // teste passa: lista não vazia
lista.clear() // remove todos os itens
assert lista // teste falha
Casoumiteradornãopossuamaisitens,suaavaliaç ãotambémretornará
falso:
def lista = new ArrayList ()
def iterator = lista.iterator()
lista.add("valor")
assert iterator // verdadeiro: iterator tem itens
iterator.next() // fui para o final da lista
assert iterator // falso: sem mais itens
2.9 E struturas de controle
Édifícilpensaremumprogramaútilquenãopossuaumaestruturadecon-
trole.NocasodoGroovytemosasmesmasestruturascomasquaisestamos
acostumadosnoJava.
27

## Página 34

2.9. Estruturasdecontrole CasadoCódigo
If-then-else
Muitoprovavelmente,aestruturadecontrolemaisconhecidasejao if.
Elaéusadaquandoprecisamoslidarcomsituaçõesdotipo “se ocorrer esta
condição, faça isto, caso contrário, aquilo
.NocasodoGroovy,essaestruturafuncionaexatamentecomoestamos
acostumadosemJava:
def a = 3
if (a <= 3) {
println "Sou menor ou igual a 3"
}
// Saída: "Sou menor ou igual a 3"
if (a == 5) {
println "Sou igual a 5"
} else {
println "Sou igual a $a"
}
// Saída: "Sou igual a 3"
if (a == 5) {
println "Sou igual a 5"
} else if (a == 4) {
println "Sou igual a 4"
} else {
println "Sou diferente de 5 e 4. Sou $a"
}
// Saída: "Sou diferente de 5 e 4. Sou 3"
Outrafacedaestruturadesele ção iféooperadorternário,cujasintaxe
ébastantesimples:
(condição) ? (ação se verdadeiro) : (ação se falso)
Ousomaiscomumdooperadorternárioénaatribuiçãodevaloresauma
variável,talcomonoexemploaseguir:
def nome = "Henrique"
def mensagem = nome.equals("Henrique") ? "Belo nome" : "Outro nome"
assert mensagem == "Belo nome" // teste passa
28

## Página 35

CasadoCódigo Capítulo2. Groovy:umabreveintrodução
Ooperador ==emGroovyequivaleaumachamadaàfun ção equalsda
classe ObjectdoJava.Reparoucomoficamaissimplesassim?
Apenasparaclarificarmelhor,outroexemplodousodooperadorterná-
rio,destavezexecutandoprocedimentos.
def condicao = 1
condicao != 1 ? condicaoDiferenteDeUm() : condicaoUm ()
// executa condicaoDiferenteDeUm
Switch: o if escrito de forma diferente
Casonãoconhe çaestaestruturadecontrole,pensenelacomosefosse
umaespéciede “salvadora de ifs complicados
. Éusadaquandoprecisamoslidarcomsituaçõesnasquais,deacordo
comovalordeumavariável,algoprecisaserfeito.
Asintaxedestaestruturaésimples:
switch (variavel) {
case [valor_1]:
//faça isto
break
case [valor_2]:
// faça aquilo
break
default:
// caso seja qualquer outra coisa, execute isto
}
Nossasintaxeécompostapordoiscomponentes:ainstrução switchem
si,quesimplesmentenosdizalgomaisoumenoscomo “se o valor da variável
for...
seguidadeumoumaiscasos,representadosportrechosdecódigoencap-
suladospelainstrução case.Cada casepossuidoiscomponentes,quesão
ainstrução,cujovalorcorresponderáàcondiçãocomaqualdevemoscom-
pararovalor,seguidadoblocodecódigo,delimitadopelainstruç ão break.
Emnossasintaxetambémháumcasoespecialchamado default. É
acondiçãoaserdisparadacasonenhumadasdefinidasanteriormenteseja
29

## Página 36

2.9. Estruturasdecontrole CasadoCódigo
satisfeita(reparequeapalavra casenãoéusadanestasituação).Lembre-se
dequandoestiverprogramandoemGroovysempreincluí-locomooúltimo
caso.
Paraentendermosmelhoropoderdo switchvamosparaumexemplo
prático:
def valor = 4 // um tipo numérico
switch (valor) {
case 5:
println "Eu sou um cinco."
break
case 4:
println "Sou um quatro!"
break
default
println "Sou alguma outra coisa: $valor"
}
// Saída:
// "Sou um quatro!"
Noexemplo,podemosvertrêscomparações:aprimeiracomovalornu-
mérico5easegundacomovalor4.Reparenocasodefaultaofinal,queseria
executadocasoovalordenossavariávelfossequalquercoisadiferentede4e
5.
Háalgumassurpresasinteressantesemumainstrução switch.Observe
opróximoexemplo:
def valor = 4
switch (valor) {
case "4":
println "Sim, sou um quatro-string"
break
case 5:
println "Quero tanto ser um cinco!"
break
case 4:
println "Sou o quatro!"
break
30

## Página 37

CasadoCódigo Capítulo2. Groovy:umabreveintrodução
default:
println "Sou qualquer outra coisa"
}
Oqueseráimpresso? Sim, sou um quatro-string.Issoporque,durantea
comparação,aochegarnestaop ção,Groovytransformounossovaloremuma
stringe,emseguida,ocomparoucomo case.Emumainstrução switch
lembre-sesempredaseguinteregra: caso seja encontrada uma condição ver-
dadeira, havendo uma instrução break o controle sai do switch.
Hácasos,noentanto,emquequeremosquenosso switchsecomporte
comoum ou. Tudooquedevemosfazerédigitarasinstruções caseem
sequência:
def valor = 4
switch (valor) {
case "4":
case 4:
println "Sou um quatro"
break;
default:
println "Não sou um quatro :("
}
// Saída:
// "Sou um quatro"
Háaindaumpontoduvidosoaqui:defato,comoemnossasinstruções
switchpudemoscompararumvalordotiponuméricocomumastringe
mesmoassimobterumvalorverdadeiro?Portrásdascortinas,Groovyadi-
cionaumnovométodoadiversasclassesdaAPIJava,chamado isCaseque
recebecomoparâmetroumobjetoqualquer.Nocasodeuma String,este
éimplementadodeformamuitosimilaràexpostaaseguir:
def isCase(object) {
return object .toString().equals(this)
}
Sendoassim,qualquerclassequeimplementeométodo isCaseestá
aptaaserincluídaemumainstrução switch.PequenossegredosdoGroovy
dominadosporumaminoria.;)
31

## Página 38

2.9. Estruturasdecontrole CasadoCódigo
Aviso aos Javeiros
Aestrutura switchemGroovyébemmaisflexíveldoqueaque
temosemJava.EnquantonoJavasópodemosaplicaroswitchemvalores
dotipo enum,inteiro( Integer),caractere( char)etexto( String),
emGroovypodemosusarqualquerobjeto.
Obloco defaulttambéméligeiramentediferente: enquantoem
Javaestepodeserdigitadoemqualquerposiç ãodentrodainstruç ão
switch,emGroovydevevirsemprenofinal. Arazãopelaqualisso
ocorreéque,aocontráriodoJava,cadabloco casepossuiseupróprio
escopoepodeseraplicadoemcimadequalquertipodedados.
Loops com while
Toda(ouquasetoda)linguagemdeprogramaç ãoqueseprezedevepos-
suiraomenosumaestruturadecontrolequepermitaaescritadeloops,que
sãoestruturasdecontrolequegarantemquedeterminadoblocodecódigo
sejaexecutadoenquantoumacondiçãoforsatisfeita.
AformamaissimplesdeloopemGroovyéaconstruç ão whilecuja
sintaxeé:
while (condição) {
// bloco de código a ser executado
}
Umexemplorápidodeloopéexpostoaseguir:
def valor = 0
while (valor < 10) {
println valor
valor = valor + 1
}
// Saída:
// 0
// 1
// ...
// 9
32

## Página 39

CasadoCódigo Capítulo2. Groovy:umabreveintrodução
Loops com for
Umaestruturamaiscomplexaparaconstruirmosloopséo for,quepos-
suiduassintaxes,aprimeiraexpostaaseguir:
for (valor in iterável) {
// faça algo
}
Um iterável é qualquer objeto que implemente a interface
java.lang.Iterable,comolistas,conjuntosediversasoutrasestruturas.
Aseguirpodemosverumexemplodestaestrutura:
def lista = [1,2,3,4]
for (valor in lista) {
println valor
}
// Saída:
// 1
// 2
// 3
// 4
Háumasegundaformaparaestaestrutura,queébastanteparecidacom
aqueestamosacostumadosemlinguagenscomoJavaouC.Umpoucomais
complexa,porémigualmenteútil:
for (declare uma variável; condição de parada; altere o valor) {
//código
}
Éumaapresentaçãobemesquisita,masficamaisfácildesercompreen-
didacomumexemplosimples.
for (i = 0; i < 10; i+=4) {
println i
}
// Saída
// 0
// 4
// 8
33

## Página 40

2.10. Funçõesemétodos CasadoCódigo
Hátrêspassosnaexecuçãodoloop:primeirocriamosumavariávelcha-
mada i. Logoemseguida,vemacomparaçãocomumacondição. Sefor
verdadeira,oblocoéexecutado. Depoisvemaalteraç ãodovalor,queéa
terceiraoperaçãonocabe çalhodo for.
2.10 F unções e métodos
Seoleitorsópudesseprogramarcomoquefoiapresentadoatéestemomento
nolivro,comcertezatodososseusprogramasseriamverdadeirospesadelos
demanutenção. Aprimeiraestruturaemumalinguagemdeprogramaç ão
quepermiteomínimodemodularidadeereaproveitamentodecódigoéa
rotina. Hádoistiposderotinas:métodoefun ção. Aprimeiranãoretorna
umvalorenquantoasegundasim.Pragmaticamentenãohágrandediferen ça
entreelas,razãopelaqualatéofinaldestelivrousareiapalavra funçãopara
mereferiràsduascategorias.
Funçõessãoaestruturaquenospermitemummínimoreaproveitamento
decódigo. Imaginequevocêpreciseimplementarumcálculocomplicado,
porexemploodeltadaequaçãodeBhaskara(b*b-(4*a*c)).Porqueficar
repetindoocódigootempointeirosepodemosorganizá-loemumafun ção?
def delta(a,b, c) {
return (b*b) - (4*a*c )
}
Asintaxededeclaraçãodeumafun çãoéexpostadeformabemesque-
matizada:
[tipo] [nome da função] ([parâmetros opcionais]) {
//código
// valor de retorno
}
Seafun çãonãopossuirparâmetros,bastaquesejamincluídosapenasos
parêntesesapósoseunome.Vejaoexemploaseguirquenosretornaotempo
correntedosistemaemmilissegundos.
long tempoCorrente() {
return System.currentTimeMillis()
}
34

## Página 41

CasadoCódigo Capítulo2. Groovy:umabreveintrodução
Outropontoimportante:ainstrução returnéusadaparasairdobloco
decódigoquecompõeafun çãoretornandoumvalor,noentantoéumains-
truçãotambémopcional.Oretornodeumafun çãopodeserovalorresultante
daexecuçãodaúltimalinhadoblocodecódigo.
Poderíamosentãoreescrevernossafun çãoqueretornaotempoassim:
long tempoCorrente() {
System.currentTimeMillis() // return pra quê?
}
Hácasosnosquaisnãoqueremosousabemosqualseráotiporetornado
pelanossafun ção:afinaldecontasestamoslidandocomumalinguagemque
porpadrãopossuitipagemimplícita.Nestecaso,bastaqueotipodafun ção
sejarepresentadopelapalavrareservada def:
def tempoCorrente() {
System.currentTimeMillis()
}
2.11 C oncluindo
Nestecapítulo,vimosasestruturasmaisbásicasportrásdoGroovy,porém
apenastocamosomarcomapontadospés. Nestemomentovocêapenas
sabecomoprogramarproceduralmentecomalinguagem,masGroovyéuma
linguagemorientadaaobjetos,certo?E,maisqueumalinguagemorientadaa
objetos,épuramenteorientadaaobjetosetambémdinâmica.Esteéoassunto
dopróximocapítulo.
35

## Página 43

Capítulo3
MergulhandoemGroovy
AtéestemomentosóvimosoessencialdoGroovy: nadaquejustificassea
adoçãodalinguagemsecomparadaaoJavaouquenosajudasseaentendero
funcionamentodediversoscomportamentosdoGrailsqueveremosnores-
tantedestelivro.NestecapítulovamosmergulharemGroovymostrandoal-
gumasdesuascaracterísticasecomportamentosque,umavezconhecidos,
lhetornarãoumdesenvolvedorGrailsmaiseficientee,quemsabe,atémesmo
lhefornecerãoideiasparaquesetorneumprogramador Javamelhortam-
bém.:)
3.1 O rientação a objetos
Nestelivronãoiremosensinaraoleitorosconceitosfundamentaisportrás
daorientaçãoaobjetos,massimomodocomoGroovyimplementaestepa-
radigmae,principalmente,apresentaremostambémasprincipaisdiferen ças

## Página 44

3.1. Orientaçãoaobjetos CasadoCódigo
emrelaçãoaoJava.
POGOs Plain Old Groovy Objects
EmJava,temosoconceitodePOJO(Plain Old Java Object ),quesãoclas-
sesJavaqueessencialmenteimplementamopadrãoJavaBeans. Nocasodo
Groovy,temosPOGOs(Plain Old Groovy Objects)ejáavisoaoleitor:muito
provavelmente,apóstomarconhecimentoaseurespeito,programaremJava
setornaráumaexperiênciabastantefrustrante.Vamoslá.
O que são Jav aBeans?
JavaBeanssurgiramcomoumaconven çãocriadapelaSunMicrosys-
temsparafacilitaracriaçãodecomponentesreutilizáveisusandoalin-
guagemJava.NãosetratadeumabibliotecaouAPI,apenasumconjunto
deregrasquedevemseraplicadasàsnossasclassesJavaparaqueseade-
quemaopadrão.Asregrassãosimples:
• Todaclassedevepossuirumconstrutorpúblico.
• Todasaspropriedadesdeumaclassesãoacessíveisatravésdemé-
todos get, sete is,oterceiroaplicávelapenasaatributosdo
tipo boolean.
• Deveserimplementadaainterfacejava.io.Serializable.
Paramelhorentenderesteconceito,vamosprimeiroescreverumPOJO
simplesemJava,talcomoexpostoaseguir:
class Pessoa implements java.io.Serializable {
private String nome;
private String sobrenome;
private boolean ativa;
public String getNome() {
return this.nome;
38

## Página 45

CasadoCódigo Capítulo3. MergulhandoemGroovy
}
public void setNome(String valor) {
return this.nome = valor;
}
public String getSobrenome() {
return this.sobrenome;
}
public void setSobrenome(String valor) {
this.sobrenome = valor;
}
// Usamos "is" apenas para atributos booleanos
public boolean isAtiva() {
return this.ativa;
}
public void setAtiva(boolean valor) {
this.ativa = valor ;
}
}
AgoravejamoscomoficaaversãoGroovy:
class Pessoa implements Serializable {
String nome
String sobrenome
boolean ativa
}
EmGroovy,todoatributodefinidonaclasseporpadrãopossuivisibili-
dadepública,masnãosepreocupe,poisapesardeparecer,nãoiremosacessar
osatributosdiretamente.Observeoscriptaseguirusandoamesmadefiniç ão
exposta:
Pessoa pessoa = new Pessoa()
pessoa.setNome("Henrique")
println pessoa .getNome()
// imprimirá "Henrique"
39

## Página 46

3.1. Orientaçãoaobjetos CasadoCódigo
Groovygeraautomaticamenteparanóstodosos getterse setters
paraodesenvolvedor. NossaclasseimplementouopadrãoJavaBeansde
formacompletamentetransparenteecom 80% menos código.Sequisermos,
tambémpodemossobrescreverummétodo getterou settertalcomo
noexemploaseguir:
class Pessoa {
String nome
String sobrenome
boolean ativa
String getNome() {
"meu nome é $nome"
}
}
Pessoa pessoa = new Pessoa()
pessoa.setNome("Henrique")
println pessoa.getNome()
// imprimirá "meu nome é Henrique"
Ainda mais interessante, também não precisamos chamar o método
getter. Podemossimplesmentereferenciaremnossocódigoonomedo
atributo,gerandocódigomuitomaislimpoefácildeler:
Pessoa pessoa = new Pessoa()
pessoa.nome = "Henrique"
println pessoa.nome
// imprimirá "Henrique" (voltamos para a versão anterior da classe)
OutroaspectointeressanteenvolvendoPOGOsdizrespeitoaosconstru-
tores.SeoleitorjápossuiexperiênciacomJava,jádeveimaginarqueocons-
trutorpadrão(semparâmetros)estáimplícitonaclasse,certo?Narealidade,
maisdoqueisto,possuímosconstrutoresdinâmicosemGroovy.Nadame-
lhordoquevê-losemprática:
Pessoa pessoa = new Pessoa(nome: "Henrique", sobrenome:"Lobo")
println "${pessoa.nome} ${pessoa.sobrenome}"
// Imprimirá "Henrique Lobo"
40

## Página 47

CasadoCódigo Capítulo3. MergulhandoemGroovy
pessoa = new Pessoa(nome: "Henrique", ativa:true , sobrenome:"Lobo")
println "${pessoa.nome} ${pessoa.sobrenome} ${pessoa.ativa}"
// Imprimirá "Henrique Lobo true"
Portrásdospanos,quandodeclaramososparâmetrosdonossoconstru-
torcomoacabamosdefazer,Groovyestánarealidadeinterpretando-oscomo
sefossemummapa.Ocódigoaseguirpossuiomesmoresultado:
Pessoa pessoa = new Pessoa([nome:"Henrique", sobrenome:"Lobo"])
Éapenasumpoucodeaçúcarsintáticoquenosajudaaescreverconstru-
toresmaislimpos.EmJava,teríamosdeescreverinúmerosconstrutores,um
paracadavariaçãoquequiséssemos.EmGroovy,bastapassarosnomesdos
atributos,quealinguagemseencarregadoresto.
Talvezoleitordesejeacessardiretamenteosatributospresentesemnossa
classe.Issopodeserfeitousandooatributo @talcomonoexemploaseguir:
class Pessoa {
String nome
String getNome() {
"Meu nome é ${this.nome}"
}
}
Pessoa pessoa = new Pessoa(nome:"Henrique")
println pessoa .nome
// Imprimirá "Meu nome é Henrique"
println pessoa .@nome
// Imprimirá apenas "Henrique"
GroovyB eans ou POGOs?
Emdiversasfontes,comooexcelentelivro Groovy in Action,oleitor
encontraráreferênciasaGroovyBeans.
GroovyBeansePOGOsnapráticasãoamesmacoisa.
41

## Página 48

3.2. Traits CasadoCódigo
Menos burocracia e mais produtividade
EmJava,quandodeclaramosumaclassepública,estadeveteromesmo
nomequeoarquivonaqualaescrevemos.EmGroovy,issonãoénecessário.
Aliás,todaclassedeclaradaemGroovyporpadrãoépúblicae,aindamais
interessante,sequiser,vocêpodedeclararquantasclassesquiserdentrode
ummesmoarquivo.
Oúnicorequisitoéqueoarquivopossuaaextensão .groovyemseu
nome.
3.2 T raits
Imaginequevocêtenhadesenvolvidoumframeworkparaintegraçãodepla-
taformasquetenhasetornadoumsucesso.Aoserlan çado,inúmerosdesen-
volvedoresoadotaramcomoasoluç ãoidealparaseusproblemaseousam
desdeentãoemtodososseusprojetosquerequeiramintegraç ão.
Nesteframeworkcriadoporvocê,háumainterfacequedeveserimple-
mentadachamada Integrador,cujalistagempodemosveraseguir:
interface Integrador {
boolean iniciarIntegracao()
boolean finalizarIntegracao()
}
Nestemomentovocêestátrabalhandonaversão2.0doseuframework.
Idealmente,vocêquerquetodososseususuáriospossamfazeroupgradeda
formamaissimplespossível:simplesmentesubstituindoosbináriosdaversão
1.0pelosda2.0,masháumpequenoproblema.Suainterface Integrador
foiligeiramentemodificada.Vejalistagemaseguir:
interface Integrador {
boolean iniciarIntegracao()
boolean finalizarIntegracao()
boolean testarIntegracao()
}
42

## Página 49

CasadoCódigo Capítulo3. MergulhandoemGroovy
Agoraoupgradesetornouumpoucomaistrabalhoso,dadoqueseus
usuáriosprecisarãoescreverométodo testarIntegracaoemtodasas
suasclassesqueimplementamainterface. Comoresolveresteproblema?
Com traits.
Astraitsforamincluídasnaversão2.3.0doGroovy.Podemosdefini-las
deumaformabastantesimplescomosendo“interfacescommétodospadrão”,
talcomoexistenoJava8(default methods)[22].Maisdoquemétodospadrão,
traitstambémpodemteratributos(privadosoupúblicos)emétodospriva-
dos. Seseuframeworkdeintegraçãotivessesidoimplementadocomtraits,
nossaclasse Integradorseriasimilaràexpostaaseguir:
trait Integrador {
boolean iniciarIntegracao()
boolean finalizarIntegracao()
}
Naversão2.0,bastariaquevocêincluísseummétodopadrão(default )na
definiçãodainterface,comonoseguinteexemplo:
trait Integrador {
boolean iniciarIntegracao()
boolean finalizarIntegracao()
/*
Nossa integração por padrão é
válida se foi iniciada e finalizada
corretamente.
*/
boolean testarIntegracao() {
iniciarIntegracao() && finalizarIntegracao()
}
Pronto: agora todas as classes que implementavam a interface
Integradornaversão2.0doframework“ganharão”aimplementaçãodo
método testarIntegracao.Claro,casosejadeinteressedealgumusuá-
riodoframework,elepoderásobrescreverestemétodoporoutroquelheseja
conveniente:
43

## Página 50

3.2. Traits CasadoCódigo
class IntegradorEquipamentos implements Integrador {
// Ignorado restante da classe
// para facilitar a leitura
// Para este caso apenas finalizar
// já é suficiente
boolean testarIntegracao() {
finalizarIntegracao()
}
}
Comooleitordeveterobservado,usamosuma traitexatamentecomo
faríamoscomuma interface,usandoapalavra-chave implements.Uma
traittambémpodeincluirmétodosabstratos,for çandoasclassesqueaimple-
mentemasobrescreverométodo:
trait TesteEquipamentos {
// Basta usar a palavra chave abstract
abstract boolean isLigado()
}
Comoditonoiníciodase ção,umatraittambémpodetermétodosou
atributosprivadosquenãoestarãodisponíveisparaasclassesqueaimple-
mentem.Vejaoexemploaseguir:
trait Comunicador {
private boolean iniciada
private void iniciar() {
if (! iniciada) {
// executa lógica
iniciada = true
}
}
void enviarMensagem(String msg) {
iniciar()
// envia mensagem
}
44

## Página 51

CasadoCódigo Capítulo3. MergulhandoemGroovy
}
class Telefone implements Comunicador {
void teste() {
/*
Um erro será disparado pois
o método iniciar só existe
privado na trait.
*/
iniciar()
}
}
3.3 T ipagem dinâmica ou estática? Ambas.
UmaspectointeressantedoGroovyequemuitasvezesassustaosprincipi-
antesnalinguageméofatodesetratardeumalinguagemcujatipagemé
dinâmica.Estaéapenasametadedahistória:atipagemdosdadospodeser
tantodinâmicaouestática,deacordocomasuanecessidade. Maisdoque
isto:Groovypermiteaoprogramadorhabituadoaprogramaremlinguagens
estáticascomoJavaaoportunidadedeexperimentarooutroladodamoeda.
O que diferencia tipagem estática da dinâmica?
Antesdemaisnada,oqueétipagem(type system)?Comoopróprionome
diz,trata-sedacaracterizaçãodealgo.Nocasodaciênciadacomputaç ão,ao
usarmostermoscomotipos,tipagem,sistemasdetiposetc.,nosreferimosao
modocomodeterminada espéciededadoérepresentadaemumcomputador,
tantoemaltoquantobaixonível.
Aodeclararmosumavariáveleatribuirmosaestaumvalortalcomono
códigoJavaaseguir,estamosinformandoocomputadorqueelairárepresen-
tarumnúmerointeiro,cujovalorinicialé1979.Estamostambémdefinindo
omodocomodesejamosqueamemóriaocupadaporestavariávelsejama-
nipulada:32bits,umdosquaisusadoparadefinirosinaldovalornumérico.
int valor = 1979;
Todalinguagemdeprogramaçãojávemcomumconjuntodetiposde
45

## Página 52

3.3. Tipagemdinâmicaouestática?Ambas. CasadoCódigo
variáveispredefinidos.Oexemploapenasdefiniucomodesejamosquenossa
linguagemdeprogramaçãointerpreteoespaçodememóriareservadoparaa
variávelqueacabamosdedeclarar.Quandodefinimos explicitamenteotipo
deumavariável,estamosaplicandooconceitodetipagemestática.
NocasodoGroovy,talcomoditonoiníciodestase ção,podemostambém
tirarproveitodatipagemdinâmica:
def numero = 1979
Apalavra-chave defusadanadefiniçãodevariáveisinstruiocompilador
ainterpretaraqueladefiniçãocomoalgosimilara “apenas quero uma variável
que se chame ‘numero’. Esta deverá conter o valor numérico 1979. Não me
interessa se é int ou long, apenas aplique o tipo mais conveniente para a execução
do meu código.
.
Atipagemdinâmicaassumearesponsabilidadepelaescolhacorretado
tipodenossasvariáveisemvezdecontarcomaajudadoprogramador.Sei
queparadesenvolvedoreshabituadoscomlinguagensestaticamentetipadas
estaideiasoaassustadora,masacredite:jáfazmaisdequarentaanosquecon-
seguimosescrevercompiladorescapazesdeacertarotipodasnossasvariáveis
comextremaprecisão.
Indoumpoucoalém,vejamosoexemploaseguir:
def variavel = 1979
println variavel // imprimirá 1979, o número inteiro
variavel = "Um texto qualquer"
println variavel // imprimirá "Um texto qualquer"
Pelatipagemdinâmica,anaturezadenossasvariáveisseráalteradano
decorrerdaexecuçãodoprograma. Emumprimeiromomento,vimosque
tínhamosumnúmero(1979). Logoemseguida,atribuímosàvariáveluma
stringcomovaloreocódigofuncionouperfeitamente. Estacapacidadede
mudançadetipoéoquejustificaainclusãodapalavra“dinâmica”emtipagem
dinâmica.
Parapodermosfixarmelhorosconceitosdetipagemestáticaedinâmica,
duasdefiniçõesrápidas:
46

## Página 53

CasadoCódigo Capítulo3. MergulhandoemGroovy
•Tipagem estática: otipodavariávelédefinidoexplicitamenteantes
queestasejausada.
•Tipagem dinâmica:otipodavariávelédefinidoemtempodeexecu-
ção.
Tipagem dinâmica e estática: quais as vantagens e desvantagens?
Asvantagensdatipagemestáticasãomaisfáceisdesecompreender,por
issoiniciaremosporelas.Aprincipaldizrespeitoaotempodeexecuç ãodos
nossosprogramas.Comoocompiladorjásabedeantemãoqualotipoapli-
cadoacadavalor,elenãoprecisasepreocuparemdescobriroqueécada
variávelacadaexecuçãoe,aindamaisinteressante,possibilitaquesejaexe-
cutadaumasériedeotimizaçõesnocódigo-fonteduranteoprocessodecom-
pilação.
Outravantageminteressantedatipagemestáticaestánofatodequecom
elapodemosdetectaremtempodecompilaç ãoumaboagamadeproblemas
quepoderiamocorreremtempodeexecuç ão.Trata-sedeumaseguran çaa
maisparaoprogramador. Sevocêtrabalha,porexemplo,comcódigoque
lidacomestruturasmuitoprecisasdedados,estaseguran çaégarantida. É
uminteirode32bitsquevocêprecisa? Ocompiladorgarantiráqueapenas
estetipodevariávelsejaacessadapeloseucódigoe,casoalgumtrecholhe
envieumvalordiferente,oerroserádetectadoparavocê.
Atipagemestáticatrazessasensaçãoseguran çaaoprogramador,masé
importantesalientarqueuseiaquiapalavra“sensação”porumaboarazão:a
tipagemestáticaapenasconseguedetectaroserrosqueumprogramadorde
QIextremamentebaixocometeria.ObserveocódigoaseguirescritoemJava:
public class Calculadora {
public int soma(int x, int y) {
return x + y;
}
public static void main(String args[]) {
Calculadora calc = new Calculadora();
int x = java.lang.Integer.MAX_VALUE;
int y = 34;
47

## Página 54

3.3. Tipagemdinâmicaouestática?Ambas. CasadoCódigo
System.out.println(calc.soma(x,y));
}
}
Ocódigocompilaráperfeitamente(experimente). Emteoria,atipagem
estáticanosgarantequepassamosvaloresválidosparanossafun ção soma,
masqualseráovalorimpressonasaídadoprograma?Serápositivooune-
gativo,levando-seemconsideraçãoqueosparâmetrospassadoseramambos
positivos? Resposta: -2147483615. Seiqueesteéumexemplobastante
simplistaequeapenasumtoloescreveria,maséaltíssimaaprobabilidadede
sercometidopor vocêemumtestecasolhepe çamparaimplementaruma
buscabinária[32].
Oexemploserveapenasparadesbancarummitocomumrelativoàti-
pagemdinâmica:odequesuacoberturadetestesprecisaserbemmaior.A
esmagadoramaioriadoserrosdetectadospelatipagemestáticasão,narea-
lidade,errosdesanidadequeraríssimasvezespassambatidospelosprogra-
madores.Tantotipagemdinâmicaquantoestáticarequerempraticamentea
mesmaquantidadedetestes.
Jácomrelaçãoàtipagemdinâmica,suaprincipalvantageméaconcisão
docódigoescrito.Lendoatentamenteotrechoaseguir,ficaclaroqueháuma
“certa”redundâncianoqueestamosescrevendo:
/*
Eu sei que é um item, preciso repetir duas vezes?
*/
Item item = new Item()
Reparecomoficabemmaisclaronoexemploaseguir:
def item = new Item()
Oleitordevelevaremconsideraç ãoofatodequecódigosquealteram
repetidasvezesotipodeumavariávelsãoextremamenteraros.Naesmaga-
doramaioriadoscasosaoescrevermosnossosprogramasnãoprecisamosou
desejamosfazeristo. Umbomexemplodeconcisãoobtidacomatipagem
dinâmicapodeservistonafun çãoaseguir:
48

## Página 55

CasadoCódigo Capítulo3. MergulhandoemGroovy
def soma (a, b) {
a + b
}
Observequenãodefinimosostiposdosparâmetrosaeb,sendoassim,
qualquerumadascondiçõesaseguiréválida:
• inteiro,inteiro
• inteiro,long
• long,inteiro
• long,long
• BigDecimal,inteiro
• eporaívai
Seestivéssemosusandotipagemestática,serianecessárioescreveruma
variaçãodaquelafun çãoparacadaumadaspossibilidadesdecombinaç ãode
tiposnuméricosemnossalinguagem.Jáimaginou?Eusim:
int soma (int a, int b) { a + b }
long soma (long a, long b) { a + b }
// imagine o restante e agradeça pelo fato
// deste exemplo ser escrito em Groovy e não Java!
Agrandedesvantagemdatipagemdinâmicadizrespeitoaotempodeexe-
cução,vistoqueprecisamosdescobrirotipodecadaparâmetroouvariável
enquantooprogramaéexecutado.Noentanto,deveserlevadoemconside-
raçãoqueaquiestamosfalandodaJVM.EaJVMpossuiorecursodacompi-
lação just in time,queotimizanossossistemasdurantesuaexecuç ão.Sendo
assim,asprimeirasexecuçõesdesistemasquepossuamtipagemdinâmica
realmenteserãomaislentas,porémsetornarãomaisrápidasconformeoti-
mizaçõesforemdescobertaspelocompilador.Porexemplo,sefordetectado
queparaafun ção somaexpostanopenúltimoexemplosempreestãosendo
passadosvaloresinteiros,otimizaçõespoderãoserexecutadas. Mas,claro,
dificilmentechegaremosaodesempenhodeumcódigoestaticamentetipado.
49

## Página 56

3.3. Tipagemdinâmicaouestática?Ambas. CasadoCódigo
SabemoqueémaislegalemGroovy?Équepodemosteromelhordos
doismundos.Tipagemestáticaquandonecessáriaedinâmicaquandodese-
jável.
Aplicando tipagem estática
AplicartipagemestáticaemGroovyémuitosimples. Bastaqueaode-
clararmosnossasvariáveisjáforneçamosqualotipoqueesperamosparaela,
comonosexemplosqueseguem:
String queroUmaString
int queroUmInteiro
Item queroItem
Sequiser,vocêtambémpodereforçaraindamaisaaplicaçãodatipagem
estáticaemseucódigoGroovycomaanotação @CompileStatic,quepode
seraplicadatantoemmétodosquantoemdefiniçõesdeclasse. Oresultado
desuaaplicaçãoésimples:averificaçãodetiposseráfeitaem tempo de com-
pilação nocódigoanotado,proporcionandoaodesenvolvedorcódigocom
desempenhosuperior.Querveralgunsexemplos?
/*
Aplicando apenas em um método
*/
class Calculadora {
@CompileStatic
int soma(int x, int y) {
x + y
}
}
/*
Aplicando na classe inteira
*/
@Compilestatic
class Calculadora {
// conteúdo omitido
}
50

## Página 57

CasadoCódigo Capítulo3. MergulhandoemGroovy
Aplicando tipagem dinâmica
Bastafazerooposto:nãodeclareostiposdosseusparâmetrosouretorno
defunçõesalémdesuasvariáveis.:)
Princípio do pato
Atipagemdinâmicamostraoaumentodeprodutividadedodesenvolve-
dorprincipalmentequandoprecisamoslidarcomobjetos. Apropósito,há
umdetalhedalinguagemGroovyquenãomencioneiatéestemomento:ao
contráriodoJava,nãohátiposprimitivos.Reparenocódigoaseguir:
int i = 3
/*
Em Java a instrução abaixo sequer seria
compilada
*/
print i.getClass() //Imprime java.lang.Integer
TudoemGroovyéumobjeto,oquecaracterizaalinguagemcomosendo
puramenteorientadaaobjetos.Sendoassim,sedeclaramosumtipoprimi-
tivoemGroovy,esteéautomaticamenteconvertidoparaumaclasse wrapper,
como java.lang.Integer, java.lang.Booleanetc.Estarazãojunto
aoprincípiodopatoqueireiexporaseguirsãoospilaresquepossibilitamo
aspectodinâmicodocompilador.
Masoqueéoprincípiodopato?
• Andacomoumpato?
• Falacomoumpato?
• Voacomoumpato?
• Nadacomoumpato?
• É...temosumpato!
51

## Página 58

3.3. Tipagemdinâmicaouestática?Ambas. CasadoCódigo
Fig.3.1:Talvezsejapatoecoelho
Emcódigo-fonte,esteprincípioficaaindamaisevidente,observeoexem-
plo:
class Galinha {
String grite() {"Có!"}
}
class Pato {
def grite() {"Quá!!!"}
}
def fale(bicho) {
println bicho.grite()
52

## Página 59

CasadoCódigo Capítulo3. MergulhandoemGroovy
}
fale(new Galinha())
fale(new Pato())
// Imprimirá
// Có!
// Quá!!!
Vejaquedeclaramosduasclassesquepossuemummétodocomomesmo
nomeemesmonúmerodeparâmetros,ométodo grite.Aindamaisinte-
ressante,notequenãoháumainterfaceemcomumentreasclasses Galinha
e Pato,equeafun ção falerecebecomoparâmetroumvalorcujotipoé
indefinido.
Nossafunção faleinternamenteapenasesperaqueoobjetopassado
comoparâmetropossuaafun ção grite()equeestameretornealgumva-
lorqueserá,emseguida,impresso. Tantoaclasse Galinhaquanto Pato
possuemalgosimilar. Elesandam,falam,nadamevoamcomopatos:para
nossafunçãosãoportanto... patos.
Trata-sedecódigomuitomenorefácildesercompreendido. Podemos
compará-locomaversãofeitaemJavaaplicandoosconceitosdetipagemes-
tática:
public interface Grite {
String grite();
}
Pato implements Grite {
public String grite() {
return "Quá!!!";
}
}
class Galinha implements Grite {
public String grite() {
return "Có!";
}
}
53

## Página 60

3.4. Closures CasadoCódigo
class Torturador {
void fale(Grite grite) {
System.out.println(grite.grite());
}
}
EsteprincípiovaialémemGroovy.Eleéaplicadotambémnostiposnu-
méricosestrings. Porisso,nãoprecisamosfazercoer çãodetiposquando
somamosum longeum intemGroovy,oumesmoum longeum
BigDecimalouqualqueroutrotiponumérico.Esperamosquetodasessas
classesimplementemasoperaçõesaritméticasdamesmaforma,então,por
quenãomanterascoisassimples?
3.4 C losures
Jáqueestamosfalandodetiposdedados,somosobrigadosatrataraquide
umtipomuitoespecialcontidoemGroovydesdesuaprimeiraversãoeque
sósurgiunaversão8doJava:asclosures.Pensenelascomoumtipodeda-
dosqualquer,porémcomumadiferen çasutil:emvezdearmazenardados,
armazenacódigoexecutável. EstasutilidadetornaGroovyumalinguagem
perfeitamenteaptaàaplicaçãodoparadigmafuncionaldeprogramaç ão.
Masantesdefalardeprogramaçãofuncional,precisamosmostrarcomo
declaramosumaclosure. Noexemploaseguirdeclaroumaclosureque,ao
serexecutada,imprimirá“Olámundo":
def olaMundo = {
println "Olá mundo"
}
Umavezdeclarada,executarumaclosureébastantesimples:vocêofará
exatamentecomofariasefossechamarumafun ção:
olaMundo()
// imprime "Olá mundo"
Aclosureéumafun ção.Fun çõessemparâmetrostêmsuaaplicaçãobas-
tantelimitada.Possoincluirparâmetrosemumaclosure,certo?Sim,naver-
dade,semprehápelomenosumparâmetro.Observeocódigo:
54

## Página 61

CasadoCódigo Capítulo3. MergulhandoemGroovy
def duplique = {
it * 2
}
duplique(1) // retornará 2
Todaclosurepossuiumparâmetroimplícitochamado it.Sequiser,você
podetrocaronomedeletambém.
def duplique = {valor ->
valor * 2
}
duplique(1) // retornará 2
Asintaxeébastantesimples:bastaincluirosnomesdosparâmetrosantes
de ->.E,sim,vocêpodetambémaplicartipagemestáticanestesatributos.
def duplique = {int valor ->
valor * 2
}
duplique(2) // retornará 4
Ecomoéquandotemosmaisdeumparâmetro?
def soma = {x, y ->
x + Y
}
soma(2,3) // retornará 5
Closure como parâmetro
Atéestemomento,asclosuresnãopassamdeumacuriosidadeinteres-
santeou,quemsabe,nomáximoumamaneiradiferentedesedeclararfun-
ções.Orecursoficarealmenteinteressantequandonoslembramosqueclo-
suressãovariáveis. Sesãovariáveis,possopassá-lascomoparâmetrospara
outrasfunções.Quetalimplementarumacalculadorausandoclosures?
def soma = {x,y -> x + y}
def subtracao = {x,y -> x - y}
55

## Página 62

3.4. Closures CasadoCódigo
def multiplicacao = {x ,y -> x * y}
def divisao = {x,y -> x / y}
// A mágica acontece
def calculadora(closure, x, y) {
closure(x, y)
}
Declaramosquatroclosures(umaparacadaoperaç ãomatemáticaele-
mentar)eumafun çãoquerecebecomoparâmetroumaclosureeosparâme-
trosxey.Tudooqueestafun çãofazéexecutaraclosurecomosparâmetros
quelhepassamos.Quetalvermosistonaprática?
calculadora soma, 2, 4 // retorna 6
calculadora subtracao, 4, 2 // retorna 2
calculadora multiplicacao, 3, 6 // retorna 18
calculadora divisao, 6, 3 // retorna 2
Esteéumexemplobastantesimplesdaaplicaç ãodestatécnica,noen-
tanto,oleitorobservaráopoderdasclosuresquandoaplicadosnaescritade
bibliotecas,talcomoalinguagemaplicanaAPICollectionsdoJava.Observe
ocódigoaseguir:
def lista = ["z","38", "d", "a", "3k"]
lista.findAll {
it.length() > 1
}
// resultado: ["38", "3k"]
VáriasfunçõessãoincluídasnaAPICollections. Entreelas,encontra-
seafun ção findAll,querecebecomoparâmetroumaclosure. Espera-se
queestaclosureretorneumvalorbooleano.Emnossoexemplo,declaramos
aclosurediretamentenachamadadafun ção(umaclosureanônima),que
apenasverificaseovalorquelheépassadopossuiumtextomaiordoqueum
caractere.
VeremosestasaplicaçõesemtodaaAPIJavaqueoGroovytoca,alémde,
claro,extensivamenteemGrails.
56

## Página 63

CasadoCódigo Capítulo3. MergulhandoemGroovy
Escopo
Háoutroaspectointeressantenasclosures:elasherdamoescopodeonde
foramdeclaradas. Paraexplicarmelhoresteconceito,observeoscriptase-
guir:
class Pessoa {
String nome
def apresenteSe = {
println "Olá. Meu nome é $nome"
}
}
class Animal {
def closure
def nome
def fale() {
closure()
}
}
def pessoa = new Pessoa(nome:"Henrique")
def animal = new Animal(nome:"Cão")
animal.closure = pessoa.apresenteSe
animal.fale() //imprimirá "Olá. Meu nome é Henrique"
pessoa.nome = "Angélica"
animal.fale() //imprimirá "Olá. Meu nome é Angélica"
Aclosuresempreteráacessoatodasasvariáveis independentedavisibi-
lidadedaclassenaqualfoideclarada.Reparequenaclasse Animaltambém
háumatributochamado nome,cujovaloré “Cão
. Noentanto,afun ção faleaoexecutaraclosureapenasimprimeos
atributosdaclasse Pessoa.
this, owner e delegate
Nocorpodecadaclosurehátrêsatributosquesempreestarãopresentes:
57

## Página 64

3.4. Closures CasadoCódigo
this, ownere delegate.Éinteressantequevocêsaibacomotirarproveito
deles.
Osatributos thise owner,naprática,sãoamesmacoisa.Ambosre-
ferenciamaclassenaqualaclosurefoireferenciada. Vamosmodificarum
poucooúltimoexemploparaexporousodosatributos ownere this.
class Animal {
def fale() {
println closure .owner
closure()
}
}
def pessoa = new Pessoa(nome:"Henrique")
def animal = new Animal(nome:"Cão")
animal.fale()
// Imprimirá algo como
// Pessoa@5d38398
// Olá. Meu nome é Henrique
Oatributo thisnãoéacessívelexternamente.Aocontráriode owner,
delegatepodeseralteradoemtempodeexecuç ão.Sendoassim,podemos
modificarumpoucomaisoúltimoexemploparaexporseuuso:
class Pessoa {
String nome
def apresenteSe = {
println "Olá. Meu nome é $nome e meu delegate ${delegate.nome}"
}
}
class Animal {
def closure
def nome
def fale() {
closure.delegate = this
closure()
}
58

## Página 65

CasadoCódigo Capítulo3. MergulhandoemGroovy
}
def pessoa = new Pessoa(nome:"Henrique")
def animal = new Animal(nome:"Cão")
animal.closure = pessoa.apresenteSe
animal.fale() //imprimirá "Olá. Meu nome é Henrique e meu delegate Cão"
Oatributo delegatepodeseralteradoparaqualquerobjetodosistema.
Emnossoexemplo,alteramo-loparaquecorrespondesseàqueleresponsável
porexecutaranossaclosure,fornecendoaesteacessoatodososatributosdo
objetochamante.
E a programação funcional?
Noiníciodestase ção,mencioneiqueasclosurespermitemqueGroovy
setorneumaexcelentelinguagemparaaaplicaç ãodoparadigmafuncional,
lembra?Bastarelerestase çãoeobservarquecomclosuresconseguimosatin-
girosprincipaisaspectosquecaracterizamesteparadigma:
• Funçõesdeprimeiraclasse: sãofun çõesquevocêpodepassarcomo
parâmetroparaoutrasfun çõesouquepodemseroresultadodeuma
função.
• Funçõespuras: aquelasquenãoalteramoestadodosistema. Elas
apenasretornamumresultadoapartirdosparâmetrosquereceberam
comoentrada.
• Recursão:nossasclosurespodemserrecursivas.
3.5 M etaprogramação
Metaprogramaçãoéumdaquelesconceitosquevocêpodepassartodaasua
vidaprofissionalsemconhecermas,umavezconhecido,seperguntarácomo
podepassartantotempoignorando-o.Emsuaessência,estamosfalandoda
habilidadedeumprogramademanipularoumesmocriaroutrosprogramas.
59

## Página 66

3.5. Metaprogramação CasadoCódigo
Éumrecursopoderosíssimoequenosabreumaimensagamadepossi-
bilidadesnaescritadesoluçõesmaissimpleseelegantes.Casooleitoresteja
ansiosoparalidarcomGrails,pe çoparaquenãopuleestase çãopoiselafa-
cilitaráenormementesuacompreensãoarespeitodofuncionamentodeste
framework.
OquemostraremosaquipodeserobtidocomJavatambém,porémde
umaformaextremamentemaistrabalhosaatravésdousodebibliotecasque
manipulem bytecode(comoASMouCGLib).AgrandevantagemdoGroovy
équeobtemosomesmoresultadousandoapenasalinguagemenadamais.
Incluindo novos métodos e atributos em classes preexistentes
Imaginequeemumdenossossistemasprecisemosotempointeiroincluir
umastringentrecolchetes.Umasoluç ãosimplespoderiasercriarmosuma
novafunçãotalcomoaexpostaaseguir:
String entreColchetes(String valor) {
"[ $valor ]"
}
Talvezpudéssemosdeclará-lacomoummembroestáticodeumaclasse
e,emseguida,apenasreferenciaraquelaclasseemtodosospontosdonosso
sistema.Outrasoluçãoseriamodificarocódigo-fontedaclasse Stringdo
Java,masestanãoéumasoluçãoadequada.Alémdisto,estamoslidandocom
umaclassefinalequenãopodesermodificadaouestendida,certo?Sevocê
falaremJava,sim.JánomundoGroovy,não.Observeocódigo:
String.metaClass.entreColchetes = {
"[ $delegate ]"
}
"Groovy rocks".entreColchetes()
// Resultado: "[ Groovy rocks ]"
Você leu certo: acabei de incluir um novo método na classe
java.lang.String em tempo de execução. Quando programamos
em Groovy, em todas as classes do sistema, sempre é incluído o atri-
buto metaClass, quefuncionaexatamentecomoummapa. Oquefi-
60

## Página 67

CasadoCódigo Capítulo3. MergulhandoemGroovy
zemos foi essencialmente incluir uma nova chave neste mapa chamada
entreColchetesquerecebecomoparâmetroumaclosure.
Nointeriordestaclosure,estamosreferenciandooobjeto delegateque
apontará,nestecaso,paraainstânciadaclassequeacabamosdemodificar.
Porisso,conseguimoscolocaroconteúdoentrecolchetesapenasinterpo-
landostrings.
Aindamaisinteressante,vocêpodetambémadicionarnovoscomporta-
mentosnãoaumaclasse,massimaumainstânciaespecíficaapenas.Vejao
exemploaseguir:
class Pessoa {
String nome
void digaOi() {
println "Olá, sou $nome"
}
}
def pessoaNormal = new Pessoa(nome:"Henrique" )
// Imprimirá "Olá, sou Henrique"
pessoaNormal.digaOi()
def pessoaAlterada = new Pessoa(nome:"Juca")
pessoaAlterada.metaClass.digaOi = {
println "Fui alterado!"
}
// Imprimirá "Fui alterado!"
pessoaAlterada.digaOi();
// Imprimirá "Olá, sou Henrique"
pessoaNormal.digaOi()
Reparequepodemosacessaroatributo metaClassemapenasumains-
tânciasequisermos,mantendoinalteradaaclasseoriginal.Esteéumcom-
portamentointeressantequandodesejamosalterarnossosobjetosapenasem
casosmaisespecíficos.
Tambémépossíveladicionarmétodosaumaclasseouinstância. Basta
queadicionemosaoatributo metaClassquenãotenhacomovaloruma
closure:
class Pessoa {
// Repare que não há atributo algum
61

## Página 68

3.5. Metaprogramação CasadoCódigo
}
Pessoa.metaClass.nome = "Henrique"
de pessoa = new Pessoa()
// Yeap: Groovy já cria automaticamente o getter e setter para nós!
// imprimirá "Henrique"
println pessoa.getNome()
// E o setter também!
pessoa.nome = "Angélica"
// Imprimirá "Angélica"
println pessoa.nome
Interceptando chamadas a métodos
Seadicionarmétodosouatributosaclassesjáexistentespareceumaideia
interessante, imaginepoderinterceptarachamadadestesmétodos. Gro-
ovynospermitefazeristodeumaformabastantesimplesusandoafun ção
invokeMethoddanossaclasse.TodaclassenocontextoGroovyapossui,e
noexemploaseguirpodemosvercomoproceder:
class Pessoa {
String nome
void imprima() {
println "Meu nome é $nome"
}
}
// Aqui o truque é preparado
Pessoa.metaClass.invokeMethod = {String name, args ->
println "Vou chamar $name"
def metodo = delegate .metaClass.getMetaMethod(name, args)
metodo.invoke(delegate, args)
println "Chamei o método"
}
// Aqui a mágica ocorre
def pessoa = new Pessoa(nome:"Henrique")
pessoa.imprima()
// Eis a saída
62

## Página 69

CasadoCódigo Capítulo3. MergulhandoemGroovy
// Vou chamar imprima
// Meu nome é Henrique
// Chamei o método
Noexemplo,useiomesmoatributo metaClassquevimosnotópico
anterior.Reparequesobrescrevoométodo invokeMethoddanossaclasse
passandoumaclosurequeesperadoisparâmetros: oprimeiroobrigatoria-
mentedeveterseutipoexplicitamentedefinido(dizrespeitoaonomedafun-
ção/métodoaserinterceptado)enquantoosegundoidentificaosparâmetros
queserãopassadosparaométodoaserinterceptado.
Nointeriordenossaversão invokeMethod,vamosfazerduascoisas:
obterométodoemnossaclassechamandoafun ção getMethoddoatributo
metaClasseinvocá-lo. Masantesdistovamosinformaranossousuário
queinterceptamosométodoeaofinaldiremosqueexecutamosométodo
interceptado.
Bom,masporquevocêiriaquererinterceptarmétodosemumaclasse?
Dou-lheumaboarazão:paratirarproveitodeoutroparadigmadeprogra-
mação:a Programação Orientada a Aspectos (Aspect Oriented Programming
AOP).EsteéummomentonoqualpodemosveropoderdoGroovy:sabemos
queestamoslidandocomumalinguagemextremamentepoderosaquando
estanospermiteacessaroutrosparadigmasdeprogramaç ãodeumaforma
simples.EmJava,paratirarmosproveitodaAOPprecisamosdeframeworks
comoSpringouAspectJ.EmGroovy... precisamosapenasdoGroovy. Va-
mosagoraparaumexemplomaisconcreto:comofuncionaumframework
desegurança?
Umframeworkdeseguran çaapenasinterceptaaschamadasamétodos:
casoousuáriopossuaacessoàquelemétodo,nósoexecutamos.Casocontrá-
rio,bloqueamosoacesso.Vamosaumexemplorápido?
class Integrador {
def execute() {
// ignore o interior
// apenas para fins didáticos
}
}
63

## Página 70

3.5. Metaprogramação CasadoCódigo
// Nosso código de segurança
Integrador.metaClass.invokeMethod = {String name, args ->
if (testeAcessoUsuario()) {
// Usuário possuí acesso
return delegate.metaClass
.getMetaMethod(name, args)
.invoke(delegate, args)
} else {
// Usuário não possuí acesso
// dispare uma exceção
throw new RuntimeException("Acesso negado")
}
}
Neste exemplo não nos interessa saber como o método
testeAcessoUsuario funciona: o que interessa é que ele retornará
true caso quem chama a função possua acesso a esta. Observe algo
interessante:estamosretornandoovalordométodochamado.Sim:através
dainterceptaçãodemétodospodemossubstituirovalorretornado. Vejao
exemplo:
class Calculadora {
def soma(x, y) {
x + y
}
}
Calculadora .metaClass.invokeMethod = {String name, args ->
def method = delegate .metaClass.getMetaMethod(name, args)
return 2 * method.invoke(delegate, args)
}
// Retornará 10, e não 5
new Calculadora .soma(2,3)
Estamoslidandoaquicomumrecursoextremamentepoderosoeperi-
goso.Maspodemosiralém:seépossívelinterceptarachamadademétodos,
seráquetambémpodemosinterceptaraexecuçãodemétodosque não exis-
tem?Sim,podemos,eocódigoaseguirnosensinacomofazeristo.
64

## Página 71

CasadoCódigo Capítulo3. MergulhandoemGroovy
class Calculadora {
def soma(x,y) {x + y}
}
Calculadora .metaClass.methodMissing = {String name, args ->
println "Não conheço este método $name"
}
// Será impresso "Não conheço o método subtracao"
new Calculadora().subtracao(3,4)
Bastasobrescreverométodo methodMissingnanossaclassealvo,exa-
tamentecomofaríamosseestivéssemosinterceptandoachamadadefun ções.
Querumexemplodeaplicaçãodesterecurso?Os finders dinâmicosdoGrails
queveremosmaisàfrentenestelivrosãoimplementadosatravésdele.
Omesmoprincípiotambémpodeseraplicadoapropriedades.Bastaso-
brescreverafun ção propertyMissingtalcomonoexemploaseguir:
Calculadora .metaClass.propertyMissing = {String name ->
println "A propriedade $name não existe"
}
// Imprimirá "A propriedade nome não existe"
new Calculadora().nome
Igualmentesimples.Vocêpodetirarproveitodessafuncionalidadepara
marcarasclassesdasuaaplicaçãoqueaindanãotenhamsidoprocessadasde
algumamaneira.Imaginequevocêqueiraverificarseumaclassededomínio
dasuaaplicaçãojáfoiprocessadaincluindométodosdepersistência. Você
poderiasimplesmenteverificaraausênciadeumapropriedadenestaclasse.
3.6 I nvocação dinâmica de métodos
UmúltimorecursointeressantedoGroovy:invocaçãodinâmicademétodos
oupropriedades.Tentardescrevê-loseriamuitochato,sendoassimvouexpô-
loavocêusandocódigo:
class Calculadora {
def soma(x,y) {x+ y}
def subtracao(x,y) {x-y}
65

## Página 72

3.7. Concluindo CasadoCódigo
def multiplicacao(x,y) {x*y}
def divisao(x,y) {x/y}
}
def executeCalculo(String nomeOperacao, x, y) {
// Repare como executo o método pelo nome
new Calculadora()."$nomeOperacao"(x,y)
}
// Resultado: 7
executeCalculo("soma", 3, 4)
Podemosinvocarummétodoemnossosobjetostantoapartirdomodo
tradicionalcomoapartirdarepresentaçãodoseunomecomoumastring!Há
diversasaplicaçõesparaessetipoderecurso.Aprincipalquemenciononesta
seçãoserianacriaçãodeumaDSL(Domain Specific Language Linguagem
EspecíficadeContexto). Imagineumalinguagemsimilaràqueexponhoa
seguir:
soma 3 4
subtracao 34 4
divisao 4 2
É fácil implementar um parseador que leia cada uma das linhas ex-
postasnessearquivo, separeoscomponentesdecadaoperaç ãousandoo
caracteredeespaçoe, emseguida, envie-osrepetidamenteparaafun ção
executeCalculoqueexpusnoexemplodestase ção. Eesteéapenasum
exemplotolo. ConformevocêforadquirindomaispráticacomGroovy,vai
encontrarinúmerasoutraspossibilidadesemseussistemas. Especialmente
quandoestivertrabalhandocomGrails.
3.7 C oncluindo
Acreditoque,finalizadoestecapítulo,casoseubackgroundsejaJava,aper-
guntaquefiznocapítuloanterior“paraqueoutralinguagemdeprograma-
ção?” tenhasidoplenamenterespondida. Comopôdeservistonestecapí-
tulo,estamosdiantedenãoapenas“maisumalinguagemdeprogramaç ão”,
massim“umapoderosaalternativaaoJava”,quenospermitetirarmáximo
66

## Página 73

CasadoCódigo Capítulo3. MergulhandoemGroovy
proveitodeconceitoscomometaprogramação,AOP,invocaçãodinâmicade
métodosetantasoutrascoisasdeumaformaextremamentesimpleseprag-
mática.
Maisdoqueisto,nostreinamentosqueofere çosobreGrailsobservoque
diversosalunosquepulamoGroovyecaemdiretonoframeworktêmaim-
pressãodequeestãolidandocomfuncionalidadesquesurgem“automagica-
mente”.Comodeveterpercebido,nãosurgemcomomágica,massimcomo
consequênciadalinguagemnaqualoframeworkfoiescrito.
Vocêestáprontoparaquepossamoscome çarafalarsobreGrailsagora.
Sigaemfrenteecomeceacriaraplicaçõeswebextremamentepoderosascom
altíssimaprodutividade.
67

## Página 75

Capítulo4
PrecisamosfalarsobreGrails
NoFISL(FórumInternacionaldeSoftwareLivre)de2005queocorreuem
PortoAlegre,nós,desenvolvedoresJavabrasileiros,levamosomaisdelicioso
tapanacaraquepoderíamostomar. Graçasaumaapresentaçãode16mi-
nutosdeumsujeitochamadoDavidHeinemeierHansson(otaldoDHH),
acordamosparaofatodequeomodocomoqualestávamosacostumados
adesenvolvernossossistemaseralento,poucoprodutivo,repetitivoemuito
burocrático.Suaapresentaçãochamada How to build a blog engine in 15 mi-
nutes with Ruby on Rails[13](Como construir um motor de blog em 15 minutos
com Ruby on Rails)foilogoemseguidapublicadanoYouTubee,dodiapara
anoite,muitosdenós(meincluo)sesentiramenvelhecidosnomínimouns
50anos.
Foiumaapresentaçãocheiadefalhas,muitos“Ops!” eumaaplicação
espartanaparadizeromínimo,masissonãonosinteressava;oquenosfazia
babareraaexecuçãodeconceitossobreosquaisatéentãoouvíamosdizerque

## Página 76

4.1. FalandodeGrails CasadoCódigo
eramlegaismasnuncahaviamsemostradodeformatãoexplícita.Conceitos
comoDRY(Don’t Repeat Y ourself,Não se repita),conven çõessobreconfigu-
ração,testabilidade,KISS(Keep it Simple Stupid, Mantenha isto simples estú-
pido), scaffolding.Aquelegringoiaalterandosuasclassesdedomínioe,como
quepormágica,todasaspáginaseramgeradasautomaticamentenanossa
frente.
Apósaquelaapresentação,programaremJSF1.1,queeraaúltimapalavra
emdesenvolvimentowebnaplataformaJavaEE(em2006sairiaaversão1.2),
setornaraumtestedepaciênciaeaplataformaJavaEEsemostravacomo
umadasmaistediosas.Éengraçadopensarqueatéalgunsdiasanteseraalgo
realmentelegal.Umapena:Javaestavaacabado,eraofim.
Noexterior,RubyonRailsjáerabastanteconhecidoenaquelemesmo
anode2005jásurgiaumaalternativarealparasalvaroJavaEE:umnovo
frameworkbaseadoemGroovycomosugestivonome Groovy on Rails.Agora
tínhamosalgoqueestavanamesmaalturaqueoRubyonRails. Podíamos
fazertudoaquiloqueoDHHnosmostrou,sóquetendoacessodiretoatodo
onossocódigoJavaquelutamostantopara“tediosamente”escreveraolongo
de8anosdesdequeJavatomouomundodeassalto.Logodepois,apedido
donossoamigoDHH,oframeworktevedemudardenomepara Grailseeste
temsidoseunomedesdeentão.Inicialmentedesenvolvidoporumaempresa
chamadaG2One,foilogoemseguidacompradopelaSpringSource,quehoje
fazpartedaPivotal,umadivisãodaVMWare.
Grailséumframeworkcujomododetrabalhoéextremamentedinâmico
equeacabouinfluenciandotodososframeworksJavaquelhesucederamde
formaprofunda.Nãovejooutraformadeintroduzi-loavocêsquenãoseja
damaneiramaispráticapossível,ouseja,comoPlatãoofaria,dialogando.
4.1 F alando de Grails
Algunsmesesatrás,Kicofoicontratadocomoprogramadorporumaempresa
deengenhariaespecializadaemprojetosindustriaischamada DDL Engenha-
ria. ADDLseorgulhadeumalongatrajetóriaconstruídaaolongodetrês
décadasnoplanejamentoeexecuçãodeprojetosnasáreasdemineração,me-
talurgia,óleoegás.
70

## Página 77

CasadoCódigo Capítulo4. PrecisamosfalarsobreGrails
Comoécomumocorreremempresascujofoconãoédesenvolvimento
desoftware,astrêsdécadasdaDDLtrouxeramumlongofardodesistemasle-
gadosdesenvolvidosnosmaisvariadosambientesdedesenvolvimento,como
porexemploVisualBasic(pré.NET),Pascal,C,Fortran.Maisrecentemente,
iniciou-seatendênciadedesenvolveraplicaçõesusandoaplataformaJavaEE
naesperançadequesetratassedeumaplataformasólidaparaapróximadé-
cada.
Umdia,KicoseencontroucomGuto,responsávelpelosetordesupri-
mentosdaempresanasaladocaféenodecorrerdaconversarelatouseu
drama:
Kico,estouperdidocara.Atéentãoeumeviravamuitobemcomasmi-
nhasplanilhasnahoradecontrolarascotaçõesquefaçoparanossasobras,
masderepente,DONADAoMAIORCLIENTEDAEMPRESAresolveuque
todososseusfornecedoresdevemdisponibilizaronlineseussistemasdeco-
taçõesnainternet. Pergunteisedeixandominhasplanilhascompartilhadas
emalgumsiteadiantariamaselesdisseramquenão,quetemdeserinterface
web.
AhGuto,issoéfácilderesolver: eupossoescreverumaaplicaç ãoweb
paravocêemalgumashorasedepoisagentevaievoluindoacoisaconforme
novasdemandasvãoaparecendo,oquemediz?
Kico,vocêestátendoumadassuasalucinações.Aconselhoqueparede
tomaresteschásesquisitosoquantoantes,poisjáouviessahistóriainúmeras
vezes:vocêsvãochamarumtaldeanalistaderequisitosparavirconversar
comigo. Emseguida,estesujeitovaificarmeatazanandoODIAINTEIRO
semmedeixartrabalharedaquiaalgunsmesesvocêvaimeentregaraquele
negócioquenãovaimeatender.Nemvemcomessepapinhofuradopracima
demimcara.
Guto,tudooquevocêprecisafazerémeexplicaroquevocêprecisae
juntossairemosdasuasalacomumaversãoinicialdosistema,oquemediz?
ApostomeuPS4comvocê.
UmsorrisomaliciososurgianafacedeGuto.
O sistema
71

## Página 78

4.1. FalandodeGrails CasadoCódigo
NocaminhoparaasaladeGuto,oproblemafoiexposto. Oprocesso
decotaçãoconsistiabasicamentenaexecuç ãodeumapesquisadepre ços.
OtrabalhodeGutoera,dadoumitemparaoprojeto,comoporexemplo
umabombaouummotor,consultarsualistadefornecedoresembuscado
preçodesteproduto.Acotaçãonadamaisseriadoqueopre çodoitemem
umdadodiaporumfornecedorespecífico.Estaeraentregueaocliente,que
entãoescolhiaqualofornecedorquemelhorlheatendesse.
Entendo,Guto:entãoimaginoquenossosistemapossuaquatroentida-
des.Umacategorianaqualositensseencaixem,comoporexemplo Equipa-
mentosou Materiais,oitempropriamentedito,quepertenceaessascatego-
rias,como Britadore Cimento.Dadoqueapesquisasedáporfornecedores,
teríamostambémumalistadefornecedorese,finalmente,acotaç ãocomos
camposdevalor,fornecedor,itemedata,certo?
É...Mastemoutrodetalhe:agentefazprojetosparaoexterior,emuitos
itensdecotaçãovêmdefora,entãoamoedapodevariar.
Começouacomplicar,hein?
Vocêquequisapostar,sevira.
Terminaramosistemacomcincoentidadesiniciais:Categoria,Item,Co-
tação,FornecedoreMoeda,oquejáforneciaumabasemínimaparaquepu-
desseserexecutado.
Fig.4.1:Asentidadesiniciaisdosistema
72

## Página 79

CasadoCódigo Capítulo4. PrecisamosfalarsobreGrails
4.2 O que é um framework?
ADDLEngenhariapossuíaumalongatradiç ãonodesenvolvimentodeapli-
caçõesvoltadasparaoambientedesktop.EstaéarazãopelaqualVisualBasic
eraalinguagempredominante. Onovorequisitodoclienteiriatrazerum
impactomuitomaisprofundoàempresaefor çá-laa,pelaprimeiravez,de-
senvolverumasoluçãoparaumambientedeexecuç ãoinexplorado,aweb.
Omododetrabalhotambémeradiferente:atéentãotodosestavamacos-
tumadosaummodelodedesenvolvimentonoqualprimeirosedesenhava
obancodedadoseainterfacegráficausadaparaalimentá-loemumafer-
ramentaRAD(Rapid Application Development )comooVisualBasic. Caso
houvessefunçõesquefossemcompartilhadaspormaisdeumformulário,elas
eramincluídasemummódulocompartilhadoportodaaaplicaç ãoeassim
ia-sedesenvolvendoosistema,umformulárioeumatabelaporvez.
AcartaqueKicotraziaemsuamangaeraGrails: umframeworkfo-
cadonodesenvolvimentodeaplicaçõesweb. Framework,umapalavratão
comumentredesenvolvedoresJava,nemsempreéumconceitotãoautoevi-
dentequantoimaginamos.
Pararesolveresteproblema,usaremosGrails,Guto.Umframeworkpara
desenvolvimentowebbaseadonalinguagemGroovy.ElegeraaplicaçõesJava
EEe,portanto,podeserexecutadotantoemumservidorsimplesquantode
aplicaçõescorporativasJavaEE.
Huhn?Framework?Oqueéisto,umabibliotecacomoaquelasqueusa-
mosnasnossasaplicaçõescorrentesouumdaquelescomponentes?Palavri-
nhachiqueparameenrolarhein?
Nemumnemoutro,apesardepossuiratributosdeambos.Quandode-
senvolvemosumaaplicaçãocomVisualBasic,porexemplo,usamosbiblio-
tecasecomponentesqueexecutamsuastarefassomentequandonósprogra-
maticamenteosadicionamos,certo?
Correto:eusimplesmentechamominhasfun çõesquandoprecisodelas.
Oquevocêquerdizercomistoéquenoframeworkédiferente,comofunci-
onaisto?
Nocasodoframework,ocorreocontrário: nãosomosnósqueescre-
vemosocódigoqueacionanossoscomponentes. Nossopapeléescrevero
73

## Página 80

4.3. InstalandooGrails CasadoCódigo
componentequeseráacionadopeloframework. Porexemplo: aoinvésde
escreverocódigoquelidacomomomentonoqualnossoservidorrecebe
umarequisição,nósiremosdesenvolverocódigoqueéchamadopelofra-
meworkquandoumarequisiçãoérecebida(sãoostaiscontroladoresqueve-
remosmaisàfrente).
Oqueocorreaquiéachamadainversãodecontrole,quenapráticaaplica
oprincípiodeHollywood. Quandoamadoresprocuramprodutoresdeci-
nemaembuscadeumpapel,apresentamseuscurrículoscomsuascapacida-
desparaquesejamavaliadas. Oqueosprodutoresfazemélhesdizerpara
quenãolhesperturbemotempointeiroperguntandoseháumpapeldispo-
nível.Quando(se)houver,umatorseráchamadoimediatamente. “Não nos
procure, deixe que procuraremos você
.
Éoframeworkquechamanossoscomponentes,asituaç ãoseinverteu:
nãoprecisamosmaisnospreocuparcomalógicaportrásdoacionamento
destes.Naprática,umframeworkécomoumaaplicaçãosemipronta:todoo
códigodeinfraestruturajáseencontraimplementadoporalguémquepassou
mesesprojetandoamelhormaneiradelidarcomaquelasituaç ão(nonosso
caso,agrossomodo,lidarcomrequisiçõesweb).
Seiqueoconceitoprovavelmentenãoestámuitoclaronestemomento,
masficaráquandoterminarmosaprimeiraversãodonossosistemadecota-
ções.
4.3 I nstalando o Grails
HáduasmaneirasdeseinstalaroGrails.Nestecapítulo,trataremosdamais
comum: baixaradistribuiçãomaisrecente,descompactá-lae,emseguida,
alteraralgumasvariáveisdeambiente.Aoutramaneiraéatravésdealguma
IDE,quenormalmentejávemcomoframeworkembutidoentresuasdepen-
dênciaseportantotornamoprocessodeinstalaçãodesnecessário.
OprimeiropassonainstalaçãodoGrailsébaixaraúltimaversãonosite
oficialdoprojeto, http://www.grails.org. Duranteaescritadestelivro,foi
usadaaversão2.4.4.AsdistribuiçõesdoGrailsvêmnoformato zip.Tudoo
queousuáriodevefazerédescompactarestearquivoemumdiretóriodesua
74

## Página 81

CasadoCódigo Capítulo4. PrecisamosfalarsobreGrails
preferência.Nonossocasooconteúdofoidescompactadoemumdiretório
chamado C:\grails\grails-2.4.4.
NãoéprecisoteroGroovyinstaladoemseucomputadorparatrabalhar
comGrails:alinguagemjávemembutidanadistribuiç ãodoframework.O
únicorequisitoéterinstaladoemseucomputadoroJDKversão1.6ouposte-
rior.DêpreferênciasempreàúltimaversãodoJDK,poispodehaverplugins
quedependamderecursosdoJava7.Falaremosdissoadiante.
Énecessárioalteraralgumasvariáveisdeambiente. Esteprocedimento
variadeacordocomseusistemaoperacional.Vamosexporaquicomoexe-
cutaressatarefanostrêssistemasmaiscomuns:Windows,LinuxeMacOS
X.
V ariáveis de ambiente no Windows
AbraajanelaprincipaldoWindowsExplorerebusquepeloícone“Meu
Computador":encontrando-o,cliquecomobotãodireitodomousesobreeste
e,emseguida,sobreaop ção“Propriedades”. Naimagemaseguirpodemos
verumexemplodecomoencontrá-lonoWindows8.
75

## Página 82

4.3. InstalandooGrails CasadoCódigo
Fig.4.2:Oícone‘MeuComputador’doWindows8
Surgiráumajanelaexpondoinformaçõessobreoseusistema.Cliqueso-
breaop ção“Configuraçõesavançadasdosistema”paraexporajanela“Pro-
priedadesdoSistema”talcomonaimagemaseguir:
76

## Página 83

CasadoCódigo Capítulo4. PrecisamosfalarsobreGrails
Fig.4.3:PropriedadesdosistemanoWindows8
Cliquenobotão“VariáveisdeAmbiente”.Finalmente,poderemosagora
forneceraosistemaasvariáveisdeambientequepossibilitarãoaexecuç ão
corretadoGrails.
77

## Página 84

4.3. InstalandooGrails CasadoCódigo
Fig.4.4:VariáveisdeambientedoWindows8
VariáveisdeambientenoWindowspodemserincluídasemdoisgrupos:
apenasparaousuáriocorrenteouparaosistema,oqueastornarãodisponí-
veisparatodososusuárioscadastradosemseucomputador.Nesteexemplo,
iremosincluí-lasapenasnousuáriocorrente.
Aprimeiravariáveldeambientesechama GRAILS_HOME,eseuvalor
devecorresponderaodiretórionoqualvocêdescompactousuadistribuiç ão
doGrails.
Precisamosverificarseestápresenteemseusistemaavariáveldesiste-
mas JAVA_HOME.NocasodoWindows,énecessáriochecarasuapresen ça
78

## Página 85

CasadoCódigo Capítulo4. PrecisamosfalarsobreGrails
nasduascaixasdesele ção:“Variáveisdeambientedousuáriocorrente”e“Va-
riáveisdosistema”.Certifique-sedeque,casoexista,elatenhacomovaloro
diretórionoqualoJDKestáinstalado.Senãoexistir,bastaincluirovalorna
listagemdevariáveisdeambientedousuáriocorrente.
Para terminar, precisamos alterar a variávelPATH. Ela é respon-
sável por tornar disponíveis à interface de linha de comando todos os
arquivos executáveis que se encontram na lista de diretórios separada
por ponto e vírgula em seu valor. Certifique-se de que o diretório
bin dos valores JAVA_HOME e GROOVY_HOME encontram-se presen-
tes. Caso não estejam, basta incluir o conteúdo a seguir neste valor:
%JAVA_HOME%\bin;%GRAILS_HOME%\bin.
TestarsuainstalaçãodoGrailsésimples:inicieopromptdecomandoe
emseguidaexecuteocomando grails.Setudoestivercorreto,vocêverá
umasaídasimilaràdaimagemaseguir:
Fig.4.5:Grailsinstaladocorretamente
Linux e Mac OS X
AvidaémuitomaisfácilparausuáriosdesistemasLinuxeMacOSX.
Tudooquevocêprecisafazeréacrescentaroscriptaseguiraofinaldoarquivo
.bashrc(nocasodoLinux)ou .bash_profile(nocasodoMacOSX),
queseencontramnodiretório homedousuáriocorrente:
export JAVA_HOME=[o diretório da sua instalação do JDK]
export GRAILS_HOME=[o diretório da sua distribuição do Grails]
export PATH=$JAVA_HOME/bin:$GRAILS_HOME/bin
Tambéméimportantequevocêsecertifiquedequeosscriptspresentesno
diretório bindasuadistribuiçãoGrailspossuampermissãoparaexecuç ão.
Feitoisto,bastaexecutarocomando grailsnasuainterfacedelinhade
79

## Página 86

4.4. Criandoaaplicação CasadoCódigo
comando.Setudodercerto,umasaídasimilaràexpostanaimagemaseguir
surgirá:
Fig.4.6:GrailsinstaladocorretamentenoLinux/MacOSX
4.4 C riando a aplicação
ComoGrailsinstalado,nossospersonagensiniciamodesenvolvimentoda
aplicação,batizadaporambosde Controle de Cotações (ConCot).
BomGuto,paracome çarodesenvolvimentovamoscriarumnovoprojeto
comaferramentadelinhadecomandodoGrails. Tudooqueprecisamos
fazeréexecutarocomando grails create-app concot.Executadoo
comando,odiretório concotégerado.
Programação por convenç ão e a estrutura de diretórios do Grails
Oprimeiropontoquechamouaaten çãodeGutofoioconteúdododire-
tório concot.DadooquehaviaouvidofalararespeitodaplataformaJava,
imediatamentedisparoucontraKico:
Pelaquantidadedearquivosgeradosporestecomando,issoquerdizer
quevamosgastarumtempoimensoeditandoarquivos XML,certo?Seráque
conseguiremosterminarestetrabalhoantesdeomêsacabar(estamosnodia
10)?
Narealidade,éocontrário:dificilmenteprecisaremostocaremarquivos
deconfiguraçãoe,diga-sedepassagem,nãosão XML.IstoporqueoGrails
sebaseianoconceitode programação por convenção,eminglêschamadade
convention over configurationou coding by convention.
Essemodelodedesenvolvimentobuscareduzironúmerodeescolhasque
aequipedeprogramaçãoprecisafazerduranteaevoluçãodoseuprojeto.São
convençõesadotadaspeloframeworkquefacilitamacompreensãodosistema
80

## Página 87

CasadoCódigo Capítulo4. PrecisamosfalarsobreGrails
eminimizamaquantidadedeconfiguraç ão,osfamigeradosarquivos XML,
queprecisaserescrita.Aperguntaquesefazé:seoframeworkjápossuiuma
sériedepadrõespredefinidos,porquerepeti-lossobaformadearquivosde
configuração?
Estareduçãonaconfiguraçãopodeparecerassustadora: estaríamosna
realidadeoptandoporumasoluçãomenosflexível,mais“engessada"?Ares-
postaé não,poisosarquivosdeconfiguraçãonãodesaparecem.Oquemuda
éomomentonoqualsuapresen çasetornanecessária.Emumaabordagem
“tradicional”estemomentosurgequandoiniciamosodesenvolvimentodo
nossoprojeto,enquantonaabordagemdaprogramaçãoporconven çãoestes
sósetornarãovisíveisquandoasconven çõespropostaspeloframework
nãoforemadequadasaonossoprojeto.
Umexemplocomumnoqualtalvezprecisemostornarexplícitaaconfigu-
raçãosãoasclassesdedomíniodonossosistema.Grailstrabalhacomocon-
ceitodeclassesdedomínio,querepresentamasentidadesdonossosistemae
seusatributossãoautomaticamentepersistidosemumbancodedados.Cada
atributoporconven çãopossuiráumcampodemesmonomenatabelaonde
seusdadosserãoarmazenados.Muitasvezesjápossuímosumbancodeda-
dospronto:nessescasos,podemossubstituiraconven çãopadrãopelanossa
personalizada.Veremosmaisarespeitonocapítulo 5quandotrataremosdo
assuntoemdetalhes.
AestruturadediretóriosqueassustouGutoéumexcelenteexemplodo
modocomoaprogramaçãoporconven çãopodeseraplicada. Comecemos
peladescriçãododiretórioraizdoprojeto,expostonaimagemaseguirno
qualcadapastapossuiumafun çãomuitobemdefinida:
81

## Página 88

4.4. Criandoaaplicação CasadoCódigo
Fig.4.7:Odiretórioconcot
Comecemospelapasta src. Muitasvezespossuímoscódigo-fonteque
gostaríamosdereaproveitaremnossosprojetos. Nestecaso,estediretório
possuiduaspastas: groovye java,ondesãoarmazenadososarquivosde
código-fontedestasduaslinguagensequeestarãoacessíveisdeformatrans-
parenteparaorestodaaplicação.
Odiretório src/groovyéinclusivemuitasvezesusadoparaguardar
código-fontequenãoseencaixanasconven çõesdoGrails.Odiretório src
mostraumaspectobastantepositivodoGrailsqueéafacilidadecomque
podemosreaproveitarnossocódigo-fonte.Vocêtambémpodeusarsuasbi-
bliotecasJavafavoritasemGrailsdeformatransparente.Umaformadeob-
teresteresultadoécopiandoosarquivos JARqueacompõemparaapasta
lib.Feitoisso,vocêpoderáreferenciarsuasclassesdiretamenteapartirdo
código-fontedoseuprojeto.
UmaferramentaimportantíssimadoGrailséasuainterfacedelinhade
comando:amesmaqueusamosparacriaroprojeto concot. Ocomando
create-appqueusamosénarealidadeumscript Gant. Gantéumafer-
82

## Página 89

CasadoCódigo Capítulo4. PrecisamosfalarsobreGrails
ramentadebuildbaseadanapopularsoluç ãoAntusadaporprogramadores
Java,jáfazumbomtempo.Grailsnospossibilitaincrementaronossopro-
cessodebuildincluindonovosscriptsquesãosalvosnestapasta.
Grailséumframeworkquenosincentivaaescrevertestesparatodasas
funcionalidadesquecriemosemnossoprojeto. Odiretório testéonde
armazenamostodososnossostestesunitários,funcionaiseintegrados.
Comonossoprojetoéumaaplicaçãoweb,precisaremoslidarcomrecur-
sosestáticos,comoarquivosCSS,Javascript,imagensetc. Esteconteúdoé
armazenadonapasta web-app.
Finalmente, temos aquele que é o diretório mais importante:
grails-app. É ali que armazenaremos o código-fonte do responsável
porsualógicadenegóciosdanossaaplicaç ão.Naimagemaseguir,podemos
veroseuconteúdoqueépraticamenteautoexplicativo.
Fig.4.8:Odiretóriograils-app
83

## Página 90

4.4. Criandoaaplicação CasadoCódigo
Estrutura de diretórios no Grails 3.0
Fig.4.9:Compatibilidade
HáalgumaspequenasmudançasnaestruturadediretóriosdoGrails
apartirdaversão3doframework.Falamosarespeitonoúltimocapítulo
dolivro 12.1.
Comoditoalgunsparágrafosatrás,aprogramaçãoporconven çãonão
anulaosarquivosdeconfiguração. Époressarazãoqueexisteodiretório
conf,ondeficamosarquivosdeconfiguraç ãodoprojetoresponsáveispor
definir,porexemplo,nossaconexãocomobancodedados,dependências
externas,padrõesdeURLediversosoutrospontosdaaplicaç ão.
OpadrãodeprojetomaisimportanteadotadopeloGrailséoMVCeisso
érefletidonasuaestruturadediretórios.Todasasnossasclassesdecontrole
vãoestarnodiretório controllers,nossacamadadevisualizaçãonodi-
retório views,nossasclassesdedomínionapasta domaineasclassesonde
implementaremosnossalógicadenegócio(osserviços),napasta services.
UmaaplicaçãoGrailséinternacionalizadadesdeoprimeiromomento.
Todo conteúdo textual estático do sistema fica armazenado no diretório
i18n,quecontémumasériedearquivosnoformatochave-valor,sendoum
poridioma.
84

## Página 91

CasadoCódigo Capítulo4. PrecisamosfalarsobreGrails
Nodiretório taglib,armazenamosasbibliotecasdetagsquevamos
criarcomGrails. Esteéumrecursobastanteinteressantequenospermite
reaproveitarelementosdevisualizaçãodeumaformabastantesimples. No
capítulo8veremosemdetalhescomovocêpoderáescreverassuasdeuma
formabastantesimples.
Aversão2.0doGrailstrouxeumrecursoparticularmenteinteressante
paraaequiperesponsávelpelagerênciadeconfiguraçãoeDBAs:trata-sedo
plugin migrations,quenospermiteacompanharaevoluçãodastabelasdo
nossosistema.Énessediretórioqueficamosarquivosusadosporesteplugin.
Oúltimodiretórioéo utils,ondeficacódigo-fontequenãoseencaixa
bemnosdemaisdiretóriosdescritosnestase ção.
Comopodeservisto,aestruturadediretórioséquaseexplicativa,oque
minimizaanecessidadedeescrevermosarquivosdeconfiguraç ãoparadefi-
nir,porexemplo,ondeficamnossoscontroladores,nossosserviçosetc.
Eomaislegaldistotudo,Guto,équecomovocêtemconven çõesbemde-
finidas,novosprogramadorespodemseadaptarmaisfacilmenteaocódigo-
fontedonossoprojeto.
ExcelenteKico,istoquerdizerquepodemoscontinuaroprojetosemvocê
depois,certo?
É...
O que é MVC?
MVCéasiglaqueusamosparadenotaropadrãodeprojeto Model- View-
Controller,queéoidealquandolidamoscomaplicaçõesquepossuemuma
interfacegráfica.Seuobjetivoésimples:minimizaroacoplamentoentreos
componentesdaaplicação,quesãodivididosemtrêscategorias:o modelo,a
visualizaçãoeo controle.
Fig.4.10:OpadrãodeprojetoMVC
85

## Página 92

4.5. Escrevendoasclassesdedomínio CasadoCódigo
Omodeloéacamadaresponsávelpelalógicadenegóciodanossaapli-
cação,alémdelidarcomainteraçãodosistemacomcamadasinferiores,por
exemplointegraçãocomobancodedadosousistemademensageria.Énesta
partedosistemaondeescrevemosnossosalgoritmos,comonossosdadosse-
rãopersistidos,comoéaintegraçãocomoutrossistemasetc.
Avisualizaçãoéoqueousuáriodefatoverá(daíonome).Corresponde
àspáginasHTMLouaosformulárioscomosquaisousuáriofinaldosistema
iráinteragir.
Nomeiodocaminho,temosocontrolador,queéoresponsávelporor-
questrarainteraçãodousuárioprovenientedacamadadevisualizaç ãoede-
finirquaisasaçõesquedeverãoserexecutadaspelomodelo. Normalmente
sãofeitasconversõesdedadosnessacamada.QuandoacessamosumaURL
pelobrowserocomponenteativadoéocontrolador.
Comoomodelonãosabedaexistênciadeumvisualizadorevice-versa,
consegue-seassimmínimoacoplamentoentreestescomponentesdosistema.
4.5 E screvendo as classes de domínio
AgoraqueconhecemosaestruturadediretóriosdoGrails,inicia-seodesen-
volvimentodonossoprojeto.Pelainterfacedelinhadecomando,váparao
diretório concotquecriamose,emseguida,inicieomodointerativodo
Grailsexecutandoocomando grails.Seráexpostaumasaídasimilaràque
vemosnaimagemaseguir:
Fig.4.11:Modointerativoativado
Parecequenãotemosnadapronto,masnarealidadeaaplicaç ãoquecri-
amosjáéfuncional. Executeocomando run-appnomodointerativoe,
emseguida,peloseubrowser,acesseoendere çohttp://localhost:8080/concot.
Seremossaudadosporumapáginadeboas-vindassimilaràimagemaseguir:
86

## Página 93

CasadoCódigo Capítulo4. PrecisamosfalarsobreGrails
Fig.4.12:Bemvind(a|o)!
Um framework full stack
Grailsfoiprojetadoparafornecerumaexperiênciadefeedbackimedi-
ato.Aideiaéminimizarotempoqueodesenvolvedorgastamontandoseu
ambientededesenvolvimento.Éoquechamamosdeframework full stack.
Muitotempoégastonatarefademontaroambientededesenvolvimento:
oprogramadorprecisa,nocasodoJava,instalarumservidordeaplicações,
configurarumbancodedados,instalaralinguagemdeprogramaç ãoeinte-
grarasdiversasbibliotecaseframeworksqueirãocomporoseuprojeto.
Umframeworkjávemcomtudoistopré-configuradoeintegrado,pos-
sibilitandoaoprogramadorgastaroseutempocomoquerealmenteinte-
ressa,ouseja,nalógicadenegóciodoseuprojeto,poisalguémjáfeztodoo
trabalhodeinfraestruturaantes. Todaaarquiteturajáseencontraprontae
devidamenteconfigurada.
Apenasparamencionar,portrásdospanosumaaplicaç ãoGrailséna
87

## Página 94

4.5. Escrevendoasclassesdedomínio CasadoCódigo
realidadeumprojetobaseadoemSpringMVC,Hibernateediversasoutras
bibliotecas.Sefôssemosfazerestaintegraç ãomanualmente,facilmenteiría-
mosconsumirpelomenosumasemananessetrabalho.ComGrails,todoeste
processoéexecutadoemsegundosassimqueterminadaaexecuç ãodoscript
create-app.
Dentreasconfigurações,encontra-seadoservidordeaplicaçõesque,no
casodoGrails,pordefaultéoApacheTomcat7.Nãoéprecisosequerconfi-
gurarobancodedadosemumprimeiromomento,poisoGrailstambémjá
vemcomumSGBDpré-configurado,nocaso,oHSQLDB,queé100%escrito
emJava.
Criando as classes de domínio
Umaclassededomíniorepresentaumaentidadedosistema,ouseja,um
dosobjetosquenossosoftwareirágerenciar.Nocasodo ConCot,lidamos
comcincoentidades:Categoria,Item,Moeda,Cotaç ãoeFornecedor. Mais
doquerepresentarumaentidadedosistema,odomíniotambémteráseus
atributospersistidosemumbancodedados,garantindoqueseuestadose
tornepermanente.
Pelo modo interativo, criamos a classe de domínioCategoria
com o comando create-domain-class Categoria. Fi-
nalizada a execução do script, serão gerados dois arqui-
vos: grails-app/domain/concot/Categoria.groovy e
test/unit/concot/CategoriaSpec.groovy. O primeiro será
nossaclassededomíniopropriamentedita, eosegundooesqueletodos
testesunitáriosquepoderemosescreverparaelanofuturo. Reparequeo
Grailsotempointeironosincentivaaescrevernossostestes.
Ocomando create-domain-classseráexecutadomaisquatrovezes
paragerarasclassesdedomínioquefaltam: Item, Moeda, Cotacaoe
Fornecedor.
Nossoprimeirocontatocomasclassesdedomínioserácomamaissim-
plesdonossosistema: Categoria,cujocódigo-fontegeradopeloscript
create-domain-classpodemosveraseguir:
package concot
88

## Página 95

CasadoCódigo Capítulo4. PrecisamosfalarsobreGrails
class Categoria {
static constraints = {
}
}
Vemos uma classe Groovy padrão sem muita novidade, a não ser
pelo atributo estáticoconstraints, que recebe como valor um bloco
de código. É interessante observar que, ao executarmos o script
create-domain-class,nãofornecemosonomedopacote,queéopcio-
nal,sendoassimfoiinferido,combasenasconven çõesdoframework,queo
pacoteasergeradoconsistirianonomedoprojeto.Nossopróximopassoserá
incluirnessaclasseoúnicoatributoquepossuietambémadicionaralgumas
regrasdevalidação.Oresultadofinaléocódigoexpostoaseguir:
package concot
class Categoria {
String nome
static constraints = {
nome nullable: false, blank:false, maxSize:128, unique:true
}
}
Agoraficoumaisclaroparaqueserveobloco constraints.Nele,de-
finimosasregrasdevalidaçãoparacadaatributodanossaclassededomínio.
Nocasodoatributo nome,queremosqueovalorjamaissejanulo,alémde
nãopoderinserirtextoembrancoenemrepetições;dessaforma,temosas
regrasqueestãodentrodo constraints.
Comomencionado,todaclassededomínioépersistidaemumbancode
dados.Porpadrão,nessebancodedadoshaveráumatabelacujonomeequi-
valeráaodonossodomínioemletrasminúsculas.Casoatabelanãoexista,
serágeradapeloHibernate,queéaferramentaORMusadaporpadrãopelo
Grails.
Podemos influenciar a definição dos campos a partir do bloco
constraints;nocaso,definimosqueotamanhomáximoparaocampo
89

## Página 96

4.5. Escrevendoasclassesdedomínio CasadoCódigo
nomepossuirá128caracteresusandoaregra maxSize:128.Veremostodas
estasregras,alémdacorrelaçãocomobancodedadosnopróximocapítulo.
Porenquanto,oexpostonaclasse Categoriaéquasetudooqueprecisamos
saber.
Umaclassededomíniosozinhaemnossosistemanãoéalgoquejustifique
acriaçãodeumsoftware. Domíniosrelacionam-seentresi:vejamoscomo
ficouaclasse Item,queserelacionadiretamentecom Categoria.
package concot
class Item {
String nome
static belongsTo = [categoria:Categoria]
static constraints = {
nome nullable:false, blank:false, maxSize: 128
categoria nullable:false
}
}
Anovidadeéoatributoestático belongsTo,querecebecomovalor
ummapa. Essemapapossuiumaúnicachave, categoria,queaponta
paraaclasse Categoria. Oquefizemosaquifoiumrelacionamentoum-
para-muitos.Quandoonossoprojetoforexecutado,aclasse Itemreceberá
umnovoatributo, categoria,dotipo Categoria,fechandoorelaciona-
mento.
Nobloco constraints,foiincluídaumanovalinhadizendoqueoatri-
buto categorianãopodesernulo. Porbaixodospanos,oqueestamos
fazendoéinstruiroGrailsparaque,nomomentodecriaç ãodatabela,seja
tambémincluídaumachaveestrangeiranocampo categoriaapontando
paraatabeladomesmonome.
Aseguirpodemosvercomoficaramasdemaisclassesdedomíniodo
nossosistema,quenãotrazem,alémdosseusatributos,novidadealguma
paraoleitor.
class Fornecedor {
90

## Página 97

CasadoCódigo Capítulo4. PrecisamosfalarsobreGrails
String nome
static constraints = {
nome nullable: false, blank:false, maxSize:128, unique:true
}
}
class Moeda {
String nome
String simbolo
static constraints = {
nome nullable: false, blank:false, maxSize:64
simbolo nullable:false, blank:false, maxSize:4, unique:true
}
}
class Cotacao {
BigDecimal valor
Date data
static belongsTo = [ item:Item, moeda:Moeda, fornecedor:Fornecedor]
static constraints = {
}
}
Executandonovamenteocomando run-appnomodointerativo, o
bancodedadosserágeradoautomaticamenteeoresultadoserábastantesi-
milaraodiagramaexpostoaseguir:
91

## Página 98

4.6. Dandovidaaosistema CasadoCódigo
Fig.4.13:Nossobancodedadoscriado!
4.6 D ando vida ao sistema
Comnossasclassesdedomínioprontas,podemosdizerquetemosmeioca-
minhoandado. Precisamoscriarainterfacecomaqualnossousuárioirá
interagirincluindonovosregistros,gerandorelatóriosetc.
Vamoscriaragoranossoprimeirocontrolador,oqueusaremosparaca-
dastrartodasascategoriasdosistema.Usandooambienteinterativo,execu-
tamosocomando create-controller Categoria edoisarquivossão
gerados:
92

## Página 99

CasadoCódigo Capítulo4. PrecisamosfalarsobreGrails
grails-app/controllers/concot/CategoriaController.groovy e
test/unit/concot/CategoriaControllerSpec.groovy
Alémdisso,tambémécriadoumdiretóriochamado categoriadentro
dapasta views.Nestemomento,oquenosinteressaéapenasocódigo-fonte
docontrolador,queéexpostonalistagemaseguir:
package concot
class CategoriaController {
def index() { }
}
Éumaclassesemmuitosatrativosequepossuiumúnicométodo,cha-
mado index(),quenãorecebeparâmetros. Éinteressanteobservarque
duasconvençõessemanifestamnacriaçãodeumcontrolador:
• Todaclassedecontroleterminacomosufixo Controlleremseu
nome;
• Estarpresentenodiretóriograils-app/controllers.
Seguindo essas simples convenções, não precisamos informar ao fra-
meworkondeencontrarnossasclassesdecontrole. Tudoficamaissimples
efácildeentender.Acessandoapáginainicialdoprojeto ConCat,podemos
observarquealgomudou:
93

## Página 100

4.6. Dandovidaaosistema CasadoCódigo
Fig.4.14:Umnovolink.
Comocriamosumnovocontrolador,napáginainicialteremosumnovo
link,pois,porpadrão,estatelalistatodososcontroladorespresentesemnosso
projeto.
Nãocliquesobreestelinkainda,antesdistofaremosumapequenamodi-
ficaçãonaclasse CategoriaControllerparaquefiqueexatamentecomo
alistagemaseguir:
package concot
class CategoriaController {
static scaffold = Categoria
}
O novo atributo scaffold recebe como parâmetro a classe
Categoria, e o resultado é simplesmente incrível: o CRUD completo
da entidade é criado, sem que precisemos escrever uma única linha de
HTML,JavascriptouGroovy.
94

## Página 101

CasadoCódigo Capítulo4. PrecisamosfalarsobreGrails
O que é CRUD?
CRUDéumasiglaeminglêsquedenotaasquatrooperaçõesmais
comunsqueexecutamoscontraumabasededados:
•Create:criaçãoderegistros;
•Read:leitura;
•Update:edição;
•Delete:exclusão.
Clicandonolinkqueapareceunatelainicialdoprojeto,observea“má-
gica”queocorreu:todoocadastrodecategoriasencontra-seprontoparauso!
Ousuáriojápodecadastrartodasassuascategoriassequiseragora,esóes-
crevemosumaúnicalinhadecódigo.
Fig.4.15:Comomágicaocadastroestápronto
Scaffoldeminglêssignifica“andaime”. Oquediversosdesenvolvedores
observaraméquealgumastarefas,comocriaçãodeinterfacesCRUD,sãobas-
tanterepetitivaseocódigogeradoésempremuitosemelhante.Sendoassim,
pergunta-se:seráquenãopoderíamosautomatizaressatarefa?Éexatamente
oqueo scaffoldingfaz. Nocaso,automaticamenteégeradaainterfacegrá-
fica básicadeCRUD,queodesenvolvedorpodedepoiscustomizarcomple-
tamente,atendendoàsnecessidadesdoseuprojeto.
95

## Página 102

4.6. Dandovidaaosistema CasadoCódigo
Éimportantesalientarqueo scaffoldingtrazapenasobásico. Aideiaé
fornecerapenasoquesejaomaissimplesefuncionalpossível,masquetam-
bémnosforneçaflexibilidade.Vejao scaffoldingcomoumpontapéinicialna
escritadasuainterfacegráfica.Agora,seainterfacegeradalheatendercom-
pletamente,comonocasodocadastrodecategorias,apenasmantenhaoque
oGrailsgeraautomaticamenteparavocê.
Noentanto,éinteressanteobservarqueo“scaffoldbásico”doGrailsésu-
ficientementeevoluídoparalidarcomrelacionamentosentreentidadestam-
bém.Criadoocontrolador ItemController,cujocódigo-fonteéexposto
aseguir,podemosvercomoorelacionamentoentreumitemesuacategoria
apareceautomaticamentenoformuláriodecadastrodeitens.
package concot
class ItemController {
static scaffold = Item
}
96

## Página 103

CasadoCódigo Capítulo4. PrecisamosfalarsobreGrails
Fig.4.16:Scaffoldingdeitens
Observandoo scaffoldingdeitens,vemosqueomodocomoascategorias
sãoexpostasnacaixadesele çãoébastanteestranho: concot.Categoria
: 1. Otextoexpostonacaixadesele çãocorrespondeaoresultadodafun-
ção toString(),queéinjetadaemtodasasclassesdedomíniodoGrails.
Sendoassim,podemosmodificaraclasse Categoriaparaquefiquecomo
nocódigoaseguir,paramelhorarestarepresentaç ão:
package concot
97

## Página 104

4.6. Dandovidaaosistema CasadoCódigo
class Categoria {
String nome
// Modificando o modo como a representação textual é gerada
String toString() {
this.nome
}
static constraints = {
nome nullable:false, blank:false, maxSize:128, unique:true
}
}
Revisitandoamesmapágina,podemosverasutilmelhorianosvalores
expostospelacaixadesele ção:
98

## Página 105

CasadoCódigo Capítulo4. PrecisamosfalarsobreGrails
Fig.4.17:Melhorandoarepresentaçãodositens
Parafinalizaraimplementaçãodosistemanestemomento,vamoscriar
trêscontroladoresparaasclassesdedomínioqueaindanãopossuemcon-
troladores: Fornecedor, Moedae Cotacao. Aseguirpodemosvero
código-fontequeescrevemos:
package concot
class MoedaController {
99

## Página 106

4.6. Dandovidaaosistema CasadoCódigo
static scaffold = Moeda
}
class FornecedorController {
static scaffold = Forecedor
}
class CotacaoController {
static scaffold = Cotacao
}
Basicamenteescrevendocincoclasses,cadaumacomumaúnicalinha
decódigo,criamostodaainterfacegráficadequeprecisamosparainiciaro
cadastrodecotaçõesemnossosistema ConCot,Guto,nãoéincrível?
Escrevemostudoistoemmenosdeumahora,Kico!Jápossoporamão
namassaecadastrartodasasminhascotações?
Estamosquaselá,parafinalizaronossotrabalhodehoje,faltaconfigurar
oacessoaobancodedados,ok?
Mandabala,Kico!
100

## Página 107

CasadoCódigo Capítulo4. PrecisamosfalarsobreGrails
Scaffold dinâmico no Grails 3.0
Fig.4.18:Compatibilidade
Nestecapítulousamososcaffolddinâmicoaodeclararmosoatri-
butoestático scaffoldemnossasclassesdecontrole. Éimportante
salientarquenoGrails3.0esterecursonãoestápresente. Parageraro
código-fontedaspáginasecontroladoresvocêdeveráusarocomando
generate-all.
Masnãoseassuste:orecursodeverávoltarnaversão3.1(oumesmo
antes)doframework.
4.7 A cessando o banco de dados
Comomencionamosnoiníciodestecapítulo,Grailsnosforneceumambi-
entededesenvolvimentocompleto,incluindoosistemagerenciadordebanco
dedados. Aideiaéqueoprogramadorjácomeceoseutrabalhodeforma
imediata,semprecisarsepreocuparemumprimeiromomentoemsubstituir
componentesbásicosdosistemacomoporexemploobancodedados.
ApesardeoHSQLDBserumexcelentebancodedados,eletemumpro-
blema: na configuração original do Grails, o HSQLDB é configurado para
armazenar todos os dados apenas em memória. Aconsequênciaéque,
quandoreiniciamosaaplicaçãooufinalizamossuaexecuç ão,osdadossão
101

## Página 108

4.7. Acessandoobancodedados CasadoCódigo
automaticamenteperdidos.
ÉpossívelusarcomGrailsqualquerSGBDquepossuaumdriverJDBC
implementado,ouseja,praticamentetodosossistemasdebancosdedados
relacionaisdomercado.Sóprecisamosexecutardoispassos:
• IncluirodriverJDBCapropriadonoclasspathdosistema;
• AlteraraconfiguraçãodosistemaparamodificaraURLdeacessoao
SGBD.
Nonossocaso,vamosusarcomoSGBD,oMySQL,quejáerainclusive
usadopela DDLemdiversosdosseusprojetos.Vamoscome çarpeloprimeiro
passo,ouseja,ainclusãododriverJDBCno classpathdaaplicação.
OdriverJDBCdoMySQLpodeserbaixadogratuitamenteemsuapá-
ginaoficial: http://dev.mysql.com/downloads/connector/j/.Nestesite,serão
expostasdiversasop ções,dasquaisamaissimplesediretaconsistenadistri-
buiçãoemformato zip.Obtendoestearquivo,bastadescompactaroarquivo
.jar, mysql-connector-java-5.x.x-bin.jarecopiá-loparaapasta
libdoprojeto.
Osegundopassoconsistenoúnicomomentodestecapítuloemquepreci-
samosalterarumarquivodeconfiguração.Ousuáriodeveráeditaroarquivo
grails-app/conf/DataSource.groovy.Nãosepreocupecomaexten-
sãodoarquivo.Vamosvê-locomcalmanopróximocapítulo.
Nesteprimeiromomentotudooquesefaznecessárioéalteraroarquivo
DataSources. Primeiro,nobloco dataSourceiremosfornecerodriver
JDBCusadoparaestabeleceraconexãocomobancodedados,assimcomo
ascredenciaisdousuário. Emseguida,nobloco environmentsiremos
definirasURLsdeconexãocomobancodedadosparaosambientesdede-
senvolvimento( development),testes( test)eprodução( production).
Oarquivofinalserásimilaraoexpostoaseguir:
dataSource {
pooled = true
driverClassName = "com.mysql.jdbc.Driver"
username = "concot"
password = "concot"
102

## Página 109

CasadoCódigo Capítulo4. PrecisamosfalarsobreGrails
}
hibernate {
cache.use_second_level_cache = true
cache.use_query_cache = false
cache.region.factory_class = 'net.sf.ehcache.hibernate.EhCacheRegionFa
dialect = 'org.hibernate.dialect.MySQL5InnoDBDialect'
}
// environment specific settings
environments {
development {
dataSource {
dbCreate = "update"
// servidor instalado localmente
url = "jdbc:mysql://localhost:3306/concot"
}
}
test {
dataSource {
dbCreate = "update"
// servidor instalado localmente
url = "jdbc:mysql://localhost:3306/concot"
}
}
production {
dataSource {
dbCreate = "update"
// IP do servidor
url = "jdbc:mysql://192.168.2.20:3306/concot"
properties {
maxActive = -1
minEvictableIdleTimeMillis=1800000
timeBetweenEvictionRunsMillis=1800000
numTestsPerEvictionRun=3
testOnBorrow=true
testWhileIdle=true
testOnReturn=false
validationQuery="SELECT 1"
jdbcInterceptors="ConnectionState"
103

## Página 110

4.8. Instalandoaaplicação CasadoCódigo
}
}
}
}
Antesdeexecutaroprogramanovamente,certifique-sedetercriadono
MySQLumusuárioeobancodedadosparaonossosistema.Nãosabecomo
fazerisso?BastausaraferramentadelinhadecomandodoMySQLeexecutar
oscriptaseguir:
create database concot;
create user 'concot'@'localhost' identified by 'concot';
grant all on concot.* to 'concot'@'localhost';
Feitooprocedimento,Gutoesfregaasmãoseperguntaimpacientemente
aKico:
Possoatacaragora?
NãoGuto:vamosinstalaraaplicaçãoantes.
Ok...
4.8 I nstalando a aplicação
OúltimopassoparaqueGutopossacadastrarsuascotaçõeséainstalaç ão
donossoprojeto.Nocaso,iremosusarcomoservidordeaplicaçõesoApa-
cheTomcat.Tudooqueprecisamosfazeré,pelomodointerativodoGrails,
executarocomando war.
Oscript warirágerarumarquivodedeploynapasta target,queserá
criadaautomaticamentenodiretórioraizdoprojeto.Estearquivoteráonome
concot-0.1.war.Osufixocorrespondeaonúmerodeversãodaaplicaç ão,
queédefinidonoarquivo application.properties,presentenodire-
tórioraiz.
Renomeamosoarquivo concot-0.1.warpara concot.war(oque
farácomqueoTomcatmontesuaURLdecontextocome çandocom“con-
cot”enão“concot-01”)e,emseguida,ocopiamosparaapastawebappsda
nossainstalaçãodoTomcat.Voilà:Gutojápodecome çarocadastrodesuas
cotações.
104

## Página 111

CasadoCódigo Capítulo4. PrecisamosfalarsobreGrails
4.9 N ão se repita (Don’t RepeatYourself DRY)
Vamosabrirumparênteserápidoparafalarmosumpoucosobreoconceito
de Don’t Repeat Y ourself,quepodesertraduzidoparaoportuguêscomo“Não
seRepita”eéumdosprincípiosbásicosportrásdoGrails.Historicamente,
esseprincípioaparecepelaprimeiraveznolivro Pragmatic Programer[17]
deAndrewHunteDavid Thomas,publicadoem1999,excelenteleiturapor
sinal.
Emumprimeiromomento,parecequeelenosdizquesimplesmentenão
devemosrepetircódigoemnossoprojeto.Narealidade,éalgomaisqueisso.
Oquedefatonoséditoéquetodainformaç ãoemumsistemadeveserre-
presentadadeformaúnicaeinequívoca.Eque,alémdisso,estainformaç ão
tambémpodeserafonteparaageraç ãodediversosoutrosartefatosdosis-
tema.
Nestecapítulovimosissodeformabemclaraaolidarmoscomasclasses
deentidade.Cadaentidadeérepresentadacentralizadamenteatravésdeuma
classepresentenodiretório grails-app/domain. Naclassededomínio
estãotodasasinformaçõesqueadefinemcompletamente,eaindamais: é
tambémafontequeusamosparagerardoistiposdeartefato,atabelarelaci-
onadanobancodedadoseasinterfacesdeCRUD.
Imaginequeasdefiniçõesdonossodomínioestivessememmaisdeum
pontocomo,porexemplo,emumarquivonoqualincluíssemosadefiniç ão
dastabelasetambémnaprópriaclasse.Ocódigosetornamaiscomplexo,a
manutençãomaisdifícileapossibilidadedeerrosmaior.Alterandoapenas
aclassededomínio,podemosfacilmentegerarnovamenteosdoisartefatos
quemencionei.
Maisdoqueisto,oprincípio DRYtambémnosdizquetodoprocessoque
érepetitivoimploraporautomação.Mencionamosqueacriaçãodeinterfaces
CRUDéumprocessorepetitivo. Comcerteza,semo scaffolding,queéna
práticaumgeradordecódigos,nãoconseguiríamosescreverosistemaem
apenasumahora,comofizemosnestecapítulo.
105

## Página 112

4.10. Concluindo CasadoCódigo
4.10 C oncluindo
AquitivemosumavisãopanorâmicadomododetrabalhodoGrails.Vimos
comoescrevendopouquíssimocódigoépossívelcriarumaaplicaç ãomini-
mamentefuncional. Éimportanteavisarqueestaaindanãoéaaplicaç ão
completa:aindahámuitochãopelafrenteenoscapítulosseguintesvamos
aprimorá-laatéquesetorneumprojetocompleto.
PudemosvernapráticaaaplicaçãodosprincípiosqueregemoGrails,
comoo Don’t Repeat Y ourselfetambémprogramação por convenções,quemi-
nimizamdrasticamenteaquantidadedeconfiguraçãoqueprecisamosescre-
ver.
Agoraéhoradenosaprofundarmosnosaspectosquefazemdesteumdos
frameworksmaisprodutivosepoderososdaplataformaJavaEE.
Dica: ocódigo-fontedestecapítuloencontra-sedisponívelnoGitHub.
Basta fazer o checkout do repositóriohttps://github.com/loboweissmann/
concot
106

## Página 113

Capítulo5
Domínioepersistência
VamoscomeçarnossomergulhoemGrailsexplorandoseucomponentemais
complexoqueéoGORM(Grails Object Relational Mapping ),suacamadade
persistência.Antesprecisamosaomenostentarresponderumapergunta: o
que é uma entidade?
Lidandocomadefiniçãodeentidadevamosapresentaromodocomoas
modelamoscomGORM.Esteseránossopontodepartidaparaoutrosas-
pectosrelacionadosàpersistência:comoinserir,editareexcluirregistrosno
bancodedados?Comoescreverconsultascomaamplagamadepossibilida-
desqueoGORMnosoferece?
Éumlongocaminhoeneleiremostoparcomalgumasarmadilhas,mas
nãoseassuste: elasservirãoparaaumentarnossoconhecimentosobreo
GORMeastecnologiasqueeleenvolve,especialmenteoHibernate. Vale
muitoapenacorreralgunsriscos. Quecomeceadissecaç ãodoGORM:já
lheaviso,esteseráumcapítuloárduomascompensador!

## Página 114

5.1. Oqueéumaentidade(ouclassededomínio)? CasadoCódigo
5.1 O que é uma entidade (ou classe de domínio)?
Abuscapeloconceitodeentidadepartedaideiafilosóficade ente. Enteé
aquilosobreoqualfalamosarespeito[14],ouseja,éoqueexiste,mesmoque
nãosejamaterialmente.Porexemplo:estelivroquevocêtemdiantedesié
umente,eleexiste. Esabeesteconceitodeentidadedequeestoufalando?
Emsinãopossuiqualquermaterialidade,mascomofalamosaseurespeito,
tambémexiste,éoutroente.
Masapenasexistirnãotornaalgoumente:estetambémdeveserdiferen-
ciável.Amelhormaneiradeexplicaressacaracterísticadaentidadeéusando
umchavão:aadolescenteraivosaquepegaseunamoradocomoutraegrita
aosseteventosque todos os homens são iguais.
Afrase todos os homens são iguais possuiumaentidadequeéoconceito
de homem,mascomonossapersonagemquersereferiraoseunamoradoe
nãoaoconceitodehomempropriamentedito,elanãooreconhececomoente,
poisnãoodiferencioudosdemais nesta frase.
Logoemseguida,aaflitanamoradaviraparasuaamigaediz: Thomas não
prestaagorasimsereferindodiretamenteaoseunamorado.Pelonome,sabe-
mosqueéhomem(anãoserqueospaisde Thomassejampessoascruéis),e
tambémoidentificamosentretodososhomens.Háum atributoqueodi-
ferencia,eesteéseunome.Agorasimtemosaentidade namorado (provavel-
mente ex agora) da adolescente raivosa,elesechama Thomaseédiferenciado
dosdemaispelo atributo nome.Este grupodoqual Thomassediferencia
oshomens sãooquechamamosde classe, categoriaou conjunto.
Todoestepapofilosóficosemanifestanacomputaç ão: PeterChen[2]
iráaplicá-lanoseufamosoartigoemqueapresentaomodeloentidade-
relacionamento: “entidade corresponde a alguma coisa do mundo real que
possa ser identificada de forma direta
.Agrandediferen çada entidadenestecasoéomodocomoestaseapre-
sentanocontextodeumbancodedadoseasinformaçõesqueusamospara
descrevê-lasobaformadecampos. Correspondeàmodelagemdasnossas
tabelaseaomodocomogarantimosaidentidadedecadaregistro.Como?As
famosaschavesprimáriasqueestãopresentesemqualquerbancodedados
(relacionalounão).
108

## Página 115

CasadoCódigo Capítulo5. Domínioepersistência
NojargãoGrails,aousarmostermoscomo classes de domínioou domínio
nosreferimosàs entidadeseaomodocomooframeworkasmanipulaatravés
doGORM.Chegouahorademodelarmosalgumasclassesdedomínio.
5.2 U ma modelagem inicial
Peguemosoobjetivodo ConCotcomoexemplo4.Nossoproblemaéfornecer
umcadastrodecotaçõesdetodosositensquea DDL Engenhariausaemseus
projetos.GutoeKico,inclusive,fizeramumamodelageminicialdosistema
quandocomeçoutodaestahistóriasobreGrails 4.1.Todamodelagemsurge
deumdiálogocujaformainicial(normalmente)ébastantesimples.
Qualoobjetivodosistema?
Cadastrarcotaçõesdeitensusadosnosprojetosda DDL Engenharia.
Entãonossosistematerá cotações.Surgeoprimeiroobjetocomoqual
teremosdelidar: Cotação.
Umacotaçãopossuipre ço,dataeédadaporumfornecedor,certo?
Correto,entãoprecisamosdeumsegundocadastroparaincluirnossos
fornecedores,queiremosrelacionarcomnossascotações.Apareceaentidade
Fornecedor.
Masumacotaçãoéacotaçãodealgumacoisa.E "esta coisa" pode
apareceremdiversascotações,certo?
Comoassim?
Porexemplo: imaginequeprecisemoscotarumcaminhãodedetermi-
nadamarcaqueéoferecidopormaisdeumfornecedor.Esta coisanocaso
serianossocaminhão.Precisamosterumcadastrodestetipodeobjetotam-
bémpararelacionaràsnossascotações,concorda?
Correto:éinteressantetermosumcadastro destas coisas,quecha-
maremosde "itens".Antesqueumacotaçãosurja,oitemdevesercadas-
trado.Maisumaentidadeaparece: Item.
AcotaçãoseráfeitasempreusandocomomoedaoReal?
Não, podemosfazercotaçõesemoutrasmoedastambém, como, por
exemplo,oDolarouoEuro. Opa! Entãotemosdetertambémumpré-
cadastrodemoedas, oquetornanecessáriaapresen çadeumaentidade
Moeda.
109

## Página 116

5.2. Umamodelageminicial CasadoCódigo
Finalmente,vamospensarnositens. Seráqueéinteressanteagrupá-los
paragerarrelatóriosouseráquepossosimplesmentelistá-losnosistema?Por
exemplo,éinteressanteagrupá-losemcategoriascomo equipamentos, mate-
riaisetc.?
Sim,ébastanteinteressante.Assimépossíveldistribuirmelhorascota-
çõesnahoraemqueformostomarasdecisõesdecompraougerarmosrelató-
rios.Surgeoúltimocadastro(atéestemomento)dequeprecisamos:vamos
chamá-lode Categoria.
Estesobjetosquemencionamos Cotação,Item,Categoria,Moeda,For-
necedor sãooquechamamosdeentidadesoudomíniodosistema.Muitas
vezes,naprática,irãocorresponderatelasdecadastro,ouseja,ainterface
usadapelousuáriofinalparaexecutaremquatrooperaçõesfundamentaisem
todobancodedados:criação,edição,leituraeexclusão. Estasquatroações
possuemumnomebastantefamosoentreprogramadores:CRUD 4.6.
Éimportantelembrarquenemtodaentidadeirágerarumateladecadas-
tro:sempreháaquelasquerepresentamconceitosmaisabstratosdosistema
quenãopodemsercadastradasdiretamentepelousuáriofinal.Sãoalgomuito
comumepoderemosfalararespeitomaistarde:nestemomento,oquereal-
mentenosinteressasãoasentidadesqueidentificamosnosistema ConCote
quepodemosverrepresentadasnaimagemaseguir. Assetasrepresentam
relaçõesdedependência. Porexemplo:paraincluirumregistrodeitemno
bancodedados,eleobrigatoriamentedeveestarrelacionadoaumregistrode
categoria.
110

## Página 117

CasadoCódigo Capítulo5. Domínioepersistência
Fig.5.1:Asentidadesiniciaisdosistema
Voltemosaotermo classes de domínio. Adefiniçãodadapelaequipede
desenvolvimentodoGrailsé:“umaclassepersistentequeémapeadaemre-
laçãoaumatabelapresenteemumbancodedadosecujaimplementaç ãose
encontranodiretório grails-app/domain”.
Ah,“entenditudo”Kico. Persistente? Mapeada? Aúnicapartequeen-
tendifoiadequeasclassesficamnodiretório grails-app/domain.
Realmenteéumadefiniçãoespartana,entãovamosanalisaralgunsdos
termos usados pelo pessoal do Grails. Por “persistente”, entenda que o
valordosatributosdessaclasseserãosalvosemalgumrepositóriodeda-
dos para posterior consulta, alteração ou exclusão. Pense em banco de
dados: se existe uma classe que se encontra implementada no diretório
grails-app/domain,esta,deacordocomasconven çõesdosistemade-
verásersalvaemalgumlugar.Serpersistenteequivalea“sersalvoemalgum
repositóriodedados”como,porexemplo,umabasededadosrelacional.
Importante:senãoquerquesuaclassesejapersistida,jamaisasalve
nodiretório grails-app/domainpoisTUDOoqueestiverláirácriar
porpadrãoumatabelanoseubancodedados.
Eporfalarembasededados,voltemosàdefiniç ão.Aclasseé “mapeada
em relação a uma tabela presente em um banco de dados
111

## Página 118

5.3. OqueéoGORM? CasadoCódigo
. Quebancodedados? NocasodoGrails,porpadrãoestamosfalando
deumbancodedadosdotiporelacional,comoMySQL,PostgreSQL,SQL
Server,Firebird,Oracleemuitosoutros. Cadaclassededomíniopossuirá
nestebancodedadosumatabelacujoscamposvãocorresponderaosatribu-
tospresentesnaclassededomínioecujosvaloresvãocorresponderaoestado
daclassededomínionomomentoemqueforsalva(persistida)nobancode
dados.
Onomedestaassociaçãoentreatributosdeumobjetoecamposemuma
tabelasechamaMapeamentoObjeto-Relacional. Eminglês,éidentificado
pelasiglaORM(Object Relational Mapping ).Hádiversasferramentasnapla-
taformaJavausadasparaexecutarestatarefa,porexemplo,Hibernate,Eclipse
Link,JavaPersistenceAPI(JPA),JavaDataObjects(JDO)emuitasoutras.
NestecapítulovamostratardaquelaqueoGrailsadotou:oGORM.
5.3 O que é o GORM?
Estatecnologiaquepossuinomeengraçadoéumdosprincipaisresponsáveis
pelosucessodoGrails.GORMéumasigla,quesignifica Grails Object Rela-
tional Mapping.Trata-sedeumapoderosaAPIquetornaolidarcomtarefas
relacionadasàpersistênciadeobjetosalgotrivial.
UmfatomarcantenahistóriadoGORMfoiolan çamentodaversão2.0
doGrails.Nasversões1.xdoframework,oGORMerabasicamenteumafina
camadadecódigoGroovysobreoHibernate,oquefacilitavaousodoúltimo
aofornecerumainterfacedeprogramaç ãoquetirassemáximoproveitodas
característicasdinâmicasdoGroovy.
(Diga-sedepassagem:comoveremosnestecapítulo,oGORMéumdos
melhoresexemplosdeusodosrecursosdinâmicosdoGroovy.)
Naquela época já havia suporte para bases de dados não relacionais
(NoSQL),porémnamaiorpartedasvezessedavamatravésdaimplemen-
taçãodepluginsqueforneciamumaAPIalternativaaoGORM.Obacana
destaépocaéquemuitosprogramadores,aoveremasfacilidadesoferecidas
peloGORM,seinteressaramemvê-locomoumaferramentaquepudesseser
usadaforadoGrails. HouvediversastentativasdeseisolaroGORM,mas
todasatéaquelemomentoacabaramporapresentarum“sucesso”bastante
112

## Página 119

CasadoCódigo Capítulo5. Domínioepersistência
relativo.
Apartirdaversão2.0doGrails,oGORMdeixoudeserapenasestafina
camadaGroovysobreoHibernateepassouaservistocomoumaAPIdeper-
sistênciaGroovyreal.FoiinclusivecriadoumnomealternativoparaoGORM
(poucoconhecidopelamaiorpartedosprogramadoresGrailsbrasileirosaté
aleituradestelivro): Grails Datastore API.
Oobjetivoda Grails Datastore APIfoiflexibilizaraomáximoosmecanis-
mosdepersistênciadisponibilizadosaosprogramadoresGrails.Seatéaver-
são2.0haviadeformaoficialapenasoHibernate,apartirdeagoraépossível
desenvolversistemasemGrailsqueusemqualquertipodeSGBD(Sistema
GerenciadordeBancodeDados),relacionalounão. Bastaquesejaescrita
umaimplementaçãoda Grails Datastore APIparaoSGBDalvo.
Atéaescritadestelivro,existiamasseguintesimplementaçõesoficiaisdo
GORM:DynamoDB,Gemfire,Cassandra,Hibernate(3e4),JPA,MongoDB,
Neo4J,Redis,RiakeSimpleDB.Nestelivroiremoslidarapenascomaimple-
mentaçãoquevêmporpadrãocomoGrailsqueéabaseadaemHibernate,
masdadoquetodasasdemaissãoimplementaçõesdeumamesmaAPI,o
queforaprendidoparaaimplementaçãoHibernateseaplicadeformaprati-
camenteinalteradaparatodasasoutras.
Respondendoàperguntaquedánomeaestase ção,podemosdizerqueo
GORMéaAPIdepersistênciausadapeloGrails.Ecomumdetalhebacana:
tambémpodeserusadahoje independente do Grailscomsucesso.
5.4 D atasource: conectando-se ao SGBD
Feitanossamodelageminicial,eagoraquesabemosoqueéoGORM,precisa-
mosdeumSGBD.Sendoassimnestase çãovamosaprendercomoselecionar
estecomponentefundamentaldanossaarquiteturaetambémcomotirarmá-
ximoproveitodeumaatividade aparentemente trivial:conectar-seao
SGBD.
Comovimosnocapítuloanterior 4,Grailsjávemprontoparaqueode-
senvolvimentodeaplicaçõespossaseriniciadodaformamaisrápidapossível,
razãopelaqualprojetosGrailsaoseremcriadosjávêmpré-configuradospara
seconectaremaumabasededadosgerenciadapeloSGBDH2,umsistema
113

## Página 120

5.4. Datasource:conectando-seaoSGBD CasadoCódigo
gerenciadordebancodedadosquepodefacilmenteserembarcadoemapli-
caçõesexecutadasnaJVMporser100%implementadoemJava.
ApesardeoH2serumexcelenteSGBD,seimuitobemquenaprática
ébaixíssimaaprobabilidadedevocêviraadotá-loemseuprojeto. Sendo
assim,nestase çãoiremosaprendercomdetalhescomodeveserfeitoopro-
cedimentodeconfiguraçãodeacessoaumSGBDrelacional.Nestelivrousa-
remosoMySQLcomoexemplo,porémométodoaquiapresentadopodeser
aplicadoaqualqueroutrosistemagerenciadordebancosdedadosquepossua
umdriverJDBC.
Obtendo e configurando o driver JDBC
A inclusão do driver JDBC como uma das dependências do pro-
jeto é bastante simples e há duas maneiras de se executar essa ta-
refa. A primeira e recomendável consiste em incluí-lo no arquivo
grails-app/conf/BuildConfig.groovy,queéusadoparadefiniras
dependênciasdeumprojetoGrailsetambémosparâmetrosusadosportodos
oscomandosescriptsnalinhadecomandodoframework.Quandousamos
otermo dependência,estamosnosreferindoatodabibliotecaterceirizada(ou
mesmodesenvolvidainternamentepelasuaequipe).
Nonossocaso,adependênciaseráodriverJDBC(tipo4)doMySQL.
Bastaalterarobloco dependenciesdoarquivoincluindoumalinhatal
comoaexpostanocódigoaseguir:
dependencies {
runtime 'mysql:mysql-connector-java:5.1.27'
}
EstainstruçãoincluiumadependêncianoformatoMaven[?],claro,com
umaspectomais groovy.Oprimeiroelementoéoseuescopo,emnossocaso,
runtime.Emseguida,éexpostasuadefinição.Respectivamente,separados
pelocaracteredoispontosestãodefinidosogrupo,nomedadependênciae
suaversão.Quandoocomandograilsforexecutado,automaticamenteodri-
verserábaixadoparaocomputadordousuárioeestarádisponívelparaa
aplicação.
114

## Página 121

CasadoCódigo Capítulo5. Domínioepersistência
Maven e as dependências
OApacheMavenéumaferramentadeautomaç ãodebuildegestãode
projetosextremamentepopularnacomunidadeJavaqueforneceumaforma
padronizadadecompilar,empacotar,executartesteseexecutarprojetos,que
temcomoambientedeexecuçãoaJVM.
Dentreasinovaçõestrazidaspelaferramenta,semdúvidasamaisconhe-
cidaéomodocomogerenciaasdependênciasdeumprojetoJava. Todas
estassãodeclaradasemumarquivopadronizado( pom.xml)quesegueuma
sintaxebastantesimplesdefinidaapartirdequatroatributos:
•group (grupo)Identificaaorganização/empresaresponsávelpelama-
nutençãodabiblioteca/framework.
•name (nome) Onomedadependência.
•version (versão) Onúmerodeversãodadependência.
•scope (escopo) Emquemomentoadependênciaéusadanoprojeto.
Oescopopadrãodetodaséo compile,queindicaqueelaseráusada
nacompilaçãoeexecuçãodoprojeto. Umbomexemploéo test,
indicandoqueadependênciasóénecessáriaduranteaexecuç ãodos
testesautomatizadosdoprojeto.
TodasasdependênciasgerenciadaspeloMavensãoinicialmentearmaze-
nadasem repositórios remotosacessadospelaferramenta.QuandooMaven
éexecutado,casoadependênciadeclaradaparaoprojetonãoseencontrepre-
sentenocomputadordoprogramador(emseu repositório local),elaébaixada
e,emseguida,cacheadalocalmente,evitandoquesejanecessárioexecutaro
downloadapartirdasegundaexecuçãodoprojeto.
UmpontoimportantedogerenciamentodedependênciasdoMavenéo
fatodeestelidartambémcomasdependênciastransitivas,ouseja,neces-
sáriasparaaexecuçãodasuadependência.Paramelhorentenderestecon-
ceito,pensenadependência grails. Comosabemos,oGrailsébaseado
noSpring,logo,paraquepossaserexecutado,asclassesdoSpringdevem
115

## Página 122

5.4. Datasource:conectando-seaoSGBD CasadoCódigo
estarnoclasspathdoseusistema.Aodeclararmosadependência,automati-
camenteoMavenirábaixarparaocomputadordousuáriotodasasdepen-
dênciasrelacionadas,poupandoumenormetrabalhoàequipededesenvol-
vimento.
Muitasvezes,odriverJDBCnãoestádisponívelemumrepositóriore-
motoMaven,talcomoocorrecomalgunsSGBDscomerciaiscomooOracle.
Nessescasos,faz-senecessárioentraremcontatocomofornecedor,normal-
menteatravésdositeoficialparaaobten çãododriver.NocasodoMySQL,o
driver(Connector/J)podeserbaixadoem http://dev.mysql.com/downloads/
connector/j/.Nestesiteamelhorop çãoé,aoselecionaraplataformaalvo,es-
colheraop ção Platform Independenttalcomooexpostonaimagemaseguir:
Fig.5.2:DetalhedositeaondepodemosbaixaroConnector/J
Optandopelodownloaddoarquivo zipeextraindoseuconteúdo,o
116

## Página 123

CasadoCódigo Capítulo5. Domínioepersistência
programadoriráencontrarumaestruturacomoaseguinte:
Fig.5.3:CopiandooConnector/Jparaapastalibdoprojeto
Paratornarodriverdisponível,bastacopiaroarquivo(ouarquivos) JAR
dadistribuiçãodoseudriverparaodiretório libdoseuprojetoGrails.Com
isso,odriverjáestarádisponívelnoclasspathdasuaaplicaç ão.Aliás,essaé
umaexcelentemaneiradeaproveitarqualquercódigolegadooubiblioteca
casoestanãoestejapresenteemumrepositórioMaven:bastacopiarosar-
quivos JARparaapasta lib.
O que é um driver JDBC?
JDBC(Java Database Connectivity)éaAPIpadrãodaplataformaJavaSE
dedicadaàinteraçãocomsistemasgerenciadoresdebancosdedadosrelaci-
onais(SQL).
SozinhooJDBCnãopossuiutilidade:navegandonasclassesfornecidas
pelaJVMouJDKoqueodesenvolvedorencontraráseráapenasumasériede
classes(muitasabstratas)einterfaces. Amágicaocorrequandoosfornece-
doresdeSGBDsrelacionaisasusamparaimplementarseusdriversdeacesso:
osfamigeradosdriversJDBC.
UmdriverJDBCéaimplementaçãodasinterfaceseclassesabstrataspre-
sentesnaAPIJDBCdoJava.Seuobjetivoépossibilitaraosdesenvolvedores
JavainteragircomoSGBD.AgrandevantagemdoJDBCéofatodeque,
117

## Página 124

5.4. Datasource:conectando-seaoSGBD CasadoCódigo
aoprogramarmoscontraassuasinterfaces,enãodiretamentecontraasim-
plementaçõesdasmesmas,passamosatermaiormobilidadeemrelaç ãoao
SGBD.PrecisoumigrardoMySQLparaoPostgreSQL?Sesuasconsultasfo-
remSQLpadrãobastatrocaraimplementaç ãododriver.
AtualmentepraticamentetodososSGBDsdomercadooferecemumdri-
verJDBC.Paraquesuaaplicaçãointerajacomoservidordebancodedados,
bastavisitarositedofabricante,buscarpelodrivereinseri-lonoclasspathdo
seuprojeto(ou,nocasodoMaven,incluí-loentresuasdependências).
ParafinalizarestahistóriasobredriversJDBCéimportantemencionar
queelessedividememquatrotipos:
•Tipo 1 Ponte JDBC-ODBC:casonãoexistaumdriverJDBCparaoseu
SGBDmasexistaumdriverODBC,vocêpodeusaraversãoODBC
usandoestetipodedriver,queoencapsula,disponibilizandoaAPI
JDBCparaodesenvolvedor.
•Tipo 2 Driver API-Nativo:nestecasoodrivercostumaformadopor
doiscomponentes.CódigoJavaqueimplementaaAPIJDBCecódigo
nativoqueéinvocadoapartirdocódigoJava.
•Tipo 3 Driver de Protocolo de rede:traduzchamadasJDBCparaum
protocoloderede,quenormalmenteéoadotadopelopróprioSGBD
alvododriver.
•Tipo 4 Driver nativo:éotipoideal,100%implementadoemdrivere
tambémomaiscomum.Tudooqueodesenvolvedorprecisaparapo-
derusarestedriveréterseusarquivosJARpresentesemseuclasspath.
Nãobastaobterodrivereincluí-lonoseuclasspath: éprecisotam-
béminformaraoGrailsqueestedeveserusado. Entraemaç ãooarquivo
grails-app/conf/DataSource.groovy,queéolocalondedefinimos
todososparâmetrosrelacionadosàconexãocomobancodedados.
Oarquivoécompostoportrêsblocos: dataSource, hibernate(ape-
nasquandolidamoscombasesdedadosrelacionais)e environments.
Nesteprimeiromomentoiremostratarapenasdaprimeira,cujocódigo-fonte
expostoaseguirrefleteaconfiguraçãodonossoprojeto ConCot4.
118

## Página 125

CasadoCódigo Capítulo5. Domínioepersistência
dataSource {
pooled = true
jmxExport = true
driverClassName = "com.mysql.jdbc.Driver"
username = "concot_user"
password = "concot_senha"
}
Obloco dataSourcenormalmenteéopontoemqueincluímosascon-
figuraçõesmaisfundamentaisreferentesàobtençãodeconexõescomobanco
dedados.Asintaxeadotadaébastantesimples:doladoesquerdodigitamoso
nomedachavedeconfiguração,edoladodireitoovalorquedesejamospara
achave.
Nessaconfiguraçãodefinimoscincoatributos:
•pooled:indicaseiremosusarumpooldeconexõesounão.Veremos
maisarespeitomaisàfrentenestamesmase ção.
•jmxExport: casosejapassadoovalor true,indicaquepoderemos
acompanharostatusdanossafontededadosapartirdeumcliente
JMXcomo,porexemplo,oJVisualVMeJConsole.
•driverClassName: aclassedonossodriver. Deveserpassadocomo
valorumastringcontendoonomecompletodaclassedodriverJDBC,
ouseja,tantoonomequantoopacotenoqualseencontra.
•username:onomedousuáriousadonaobten çãodeconexãocomo
bancodedados.
•password:asenhausadaduranteaobten çãodeumaconexãocomo
bancodedados.
Oatributo driverClassNamevariadeacordocomoSGBDescolhido.
Parasaberqualvalordeveseradotado,énecessárioconsultaradocumenta-
çãodoseudriverJDBC.
119

## Página 126

5.4. Datasource:conectando-seaoSGBD CasadoCódigo
Configurando o Hibernate
CasoestejausandoumbancodedadosJDBCumase çãoimportantíssima
doarquivo DataSource.groovyéa hibernate,cujocódigopodemos
conferiraseguir:
hibernate {
dialect = 'org.hibernate.dialect.MySQL5InnoDBDialect'
cache.use_second_level_cache = true
cache.use_query_cache = false
}
Dostrêsatributosexpostosnessecódigo, dialectédefundamentalim-
portância,poisdefinequalodialetousadopeloHibernate,quedevereceber
comovalorumastring. Apesardeamaiorpartedosbancosdedadosrela-
cionaisadotaremopadrãoSQL,semprehávariaç ãoentreumSGBDeoutro
resultantedascaracterísticasintrínsecasdecadaimplementaç ão.Pararesol-
veresseproblemaoHibernateadotaoconceitodedialetos.
Para cada SGBD há uma implementaç ão da interface
org.hibernate.dialect.Dialect que ajuda o Hibernate a, no
momentoemqueforexecutarinstruçõesSQL,escolherasvariaçõescorretas
queocorrememcadaSGBD.NocasodoMySQL,hámaisdeumdialeto
implementado,deacordocomomotordearmazenamentoadotado.Como
desejamostirarproveitodaintegridadereferencial,usaremoscomodialetoo
valorexpostonaconfiguraçãoqueexpusemos,queéoadotadopeloInnoDB,
omotordearmazenamentodoMySQLqueoferecesuporteaintegridade
referencial.CasonãoestejausandooMySQL,consulteoApêndice1 13deste
livronoqualencontram-selistadostodososdialetosqueestãopresentesna
distribuiçãopadrãodoHibernate.
Casonãoestejalistadano Apêndice 1algumaimplementaçãododialeto
paraoseuSGBD,égrandeapossibilidadedequealguémjátenhacriadouma
implementaçãoparavocê.Nestecaso,asugestãoéconsultaracomunidade
opensourceembuscadeumaimplementaç ãoquelheatendapara,emse-
guida,incluí-lanoclasspathdoseuprojeto.
120

## Página 127

CasadoCódigo Capítulo5. Domínioepersistência
Detecção automática de dialetos
Casoachavedeconfiguração dialectnãoestejapresentenoar-
quivo DataSource.groovy,opróprioGrailspodedescobrirautoma-
ticamentequaldialetousar.
Paratal,pordebaixodospanos,Grailsnarealidaderegistraumbean
chamado dialectDetector, que verifica os metadados do objeto
dataSourcee,combasenestasinformações,inferequalodialetoque
deveseraplicadonasconfigurações.
Fig.5.4:Aten çãoredobrada!
Nemsempreestaéamelhoralternativa.NocasodoMySQL,desdea
versão5.5foidefinidocomomotordearmazenamentodefaultoInnoDB,
massesuaversãoformaisantiga,seráusadaaop çãopadrão MyISAM.
Sendoassim,éinteressantequeodesenvolvedorsempredefinaovalor
doatributo dialectdobloco dataSource.
Os outros dois atributos definidos na chavehibernate são o
cache.use_second_level_cachee cache.use_query_cache,que
ativamouinativamrespecitvamenteocachedesegundoníveledeconsul-
tasdoHibernate.
Ambientes de execução
Aterceirase çãodoarquivo DataSource.groovyéa environments,
naqualdefinimosquaisosambientesdeexecuç ãodonossoprojeto. Maso
queéumambientedeexecução?Paramelhorentenderesteconceito,vamos
pensarnostrêsmodoscomolidamoscomocódigo-fontedonossosistema.
Emumprimeiromodo,ocorrequandoconfiguramosoambientedeexe-
cuçãoparaqueosistemapossafuncionarnamáquinadoprogramador. É
121

## Página 128

5.4. Datasource:conectando-seaoSGBD CasadoCódigo
oquechamamosdeambientededesenvolvimento(development ). Normal-
mentenesteambientecadaprogramadorpossuiinstaladoemseucomputa-
doroservidordebancodedadosecontraesteexecutaocódigotestandoas
modificaçõesconformeestassemanifestamemseucódigo-fonte.
Mastestaracorre çãodocódigoapenasexecutandonãoéomelhordos
caminhos. QuandolidamoscomGrails,otempointeirooframeworknos
incentivaaescrevertestesautomatizados.Estestestesirãoincluirumasérie
deregistrosemumatabelaououtra,devezemquandoatémesmoapagaro
conteúdodobancodedadosinteiroparaexecutarumaverificaç ãoeporaí
vai.Nessasituação,éinteressante(praticamenteobrigatório)queasbasesde
dadosusadasparadesenvolvimentoetestessejamdistintas.Esseéoambiente
detestes(test ).
Finalmente,temosomomentodaentregadosistemaaoclientequejamais
poderáseroambientedetestesoudesenvolvimento,massimode produção
(production).Éondeoobjetivodosoftwareserealiza:ondeéimplantado.
NaconfiguraçãopadrãodoGrailssãodefinidosestestrêsambientes: de-
velopment(desenvolvimento), test(testes)e production(produção),oquefor-
neceàequiperesponsávelpelaevoluçãodocódigoaconfiguraç ãomínima
deinfraestruturaparaquepossasercontroladoociclodevidadaaplicaç ão.
Nocódigoaseguirpodemosvercomoestesambientesaparecemnoarquivo
DataSource.groovyrelacionadasaoprojeto ConCot4.
environments {
development
dataSource {
dbCreate = "update"
url = "jdbc:mysql://localhost/concot_dev"
}
}
test {
dataSource {
dbCreate = "update"
url = "jdbc:mysql://localhost/concot_test"
}
}
production {
122

## Página 129

CasadoCódigo Capítulo5. Domínioepersistência
dataSource {
dbCreate = "update"
url = "jdbc:mysql://localhost/concot"
}
}
}
}
Na definição de cada ambiente é incluído um bloco chamado
dataSource, que é o mesmo que vimos nesta seção quando mostra-
moscomodefinirodriverJDBC.Emtempodeexecuç ão,oqueocorreéque
osconteúdosdasduasse çõesdataSource,aisoladanoiníciodoarquivoe
apresenteemcadaambiente,serãomescladosemumasó.Quandoosistema
encontra-seemexecuçãocomaconfiguraçãodefinidaaqui,oresultadona
práticaseráumaconfiguraçãotalcomoaexpostaaseguir:
development {
dataSource {
pooled = true
jmxExport = true
driverClassName = "com.mysql.jdbc.Driver"
username = "paideia"
password = "quentecomopaideia"
dbCreate = "update"
url = "jdbc:mysql://localhost/concot_dev"
}
}
Afusãodeconfiguraçõessempreocorredecimaparabaixo.Sendoassim,
sehouverumachavedefinidaemumambientequetenhaomesmonome
daqueledefinidonobloco dataSource,adebaixoiráprevalecer.Épossível
portanto,porexemplo,terumambienteusandoumdriverJDBCdiferente
daqueledefinidonobloco dataSourcepresentenotopodoarquivo.
Assimcomoháumbloco dataSourcedefinidoparacadaambiente,é
possíveltambémterumbloco hibernatecustomizado,comooseguinte,
queativaocachedeconsultasparaoambientededesenvolvimento.
development {
hibernate {
123

## Página 130

5.4. Datasource:conectando-seaoSGBD CasadoCódigo
cache.use_query_cache = true
}
dataSource {
dbCreate = "update"
url = "jdbc:mysql://localhost/concot_dev"
}
}
Épossíveltambémteroseupróprioambientedeexecuç ãocustomizado:
imaginequesejanecessárioumambientechamado beta. Tudooqueode-
senvolvedorprecisafazeréadicionarumblocoem environmentscomeste
nome,comoexpostonocódigoaseguir:
environments {
beta {
dataSource {
dbCreate = "update"
url = "jdbc:mysql://localhost/concot_beta"
}
}
}
AescolhadoambientedeexecuçãonoGrails,éclaro,baseia-setambém
emconvenções. Aoexecutarocomando grails run-app,oambiente
developmentseráacionado,executandotestescom test-app,oambi-
ente teste,finalmente,aogeraroarquivo WARcomocomando war,
productionseráativado.
Paraexecutarumambientecustomizado,bastaqueoprogramadorpasse
oparâmetro -Dgrails.envnalinhadecomandodoGrails. Paragerar
umarquivo WARusandoasconfiguraçõesdoambiente betaaquiexposto,
portanto,bastariaexecutarocomandoaseguir:
grails war -Dgrails.env=beta
A URL de conexão
AURLdeconexão(tambémchamadade “string de conexão
),definidapeloatributo urldobloco dataSourceéaresponsávelpor
especificarcomodeveserfeitaaconexãoapartirdodriverJDBC.Estaaponta
124

## Página 131

CasadoCódigo Capítulo5. Domínioepersistência
paraumendere ço,cujadefiniçãoirávariardeacordocomodriverJDBC
escolhidoparaoprojeto.
NocasodoMySQL,aURLdeconexãosempreéiniciadacomoprefixo
jdbc:mysql://,seguidadonomeouIPdamáquinanaqualseencontra
emexecuçãooservidordebancodedados,ocaractere /e,finalmente,o
nomedobancodedados.
PodemserincluídostambémváriosatributosaofinaldaURLquenos
permitemdefinircomoodriverJDBCdeverásecomportar. Noexemploa
seguir,podemosverainclusãodoparâmetro autoReconnectnastringde
conexão,queinstruiodriveratentarreconectar-seaoservidoremcasode
errosdecomunicaçãoduranteaexecuçãodecomandosSQL:
environments {
beta {
dataSource {
dbCreate = "update"
url = "jdbc:mysql://localhost/concot_beta?autoReconnect=true"
}
}
}
MuitasvezesaURLdeconexãosetornaenormeconformeaumentao
númerodeparâmetrosqueincluímosaoseufinal.Nessescasos,háumaal-
ternativamaisinteressantepararesolveresteproblema:vocêpodeincluiro
bloco dbPropertiesnointeriorde dataSourcetalcomonocódigoa
seguir:
environments {
beta {
dataSource {
dbCreate = "update"
url = "jdbc:mysql://localhost/concot_beta"
dbProperties {
autoReconnect=true
jdbcCompliantTruncation=true
}
}
125

## Página 132

5.4. Datasource:conectando-seaoSGBD CasadoCódigo
}
}
A propriedades expostas nesse código são apenas algu-
mas específicas do driver Connector/J do MySQL, que po-
dem ser consultadas em http://dev.mysql.com/doc/connector-j/en/
connector-j-reference-configuration-properties.html, porém o mesmo
procedimentopodeseraplicadoaqualqueroutrodriverJDBC.
Geração automática do banco de dados
Porpadrão,programadoresGrailsnãoprecisamsepreocuparcomacri-
açãodastabelasnobancodedados.IssoporqueoHibernateofaráparanós
automaticamente.Épossívelfazerocontráriotambém,ouseja,primeirocri-
armosastabelas(oureaproveitarasexistentes)edepoisescrevermosasclas-
sesdedomínio,masagoravamostratarapenasdaabordagempadrãodofra-
mework.
Paratirarmáximoproveitodageraçãoautomáticadetabelas,éimpor-
tanteconheceroparâmetrodeconfiguraç ão dbCreate,quepodereceber
comovalorumadasop çõesaseguir:
•create:quandoaaplicaçãoéiniciada,asclassesdedomíniosãoanalisa-
dase,emseguida,casonãoexistaumatabelaparaalgumadasclasses
dedomínio,elaserácriada. Tambémsãoavaliadososatributosdas
classes,oquepoderáincluirnovosatributosnastabelasrelacionadas.
•create-drop:quandoaaplicaçãoforiniciada,ocomportamentodefi-
nidoem createéexecutado,equandoforfinalizada,obancodedados
seráinteiramenteexcluído.PERIGO: muito cuidado com esta opção..
•update:quandoaaplicaçãoéiniciada,verifica-seanecessidadedeno-
vastabelasseremcriadascasoaindanãoexistam,assimcomoapre-
sençaounãodecamposrelacionadosaosatributosdasclassesdedo-
mínio.
•validate:nenhumaalteraçãoseráfeitanabasededados.Apenasserá
verificadosetodasastabelasesperadasexistem,assimcomoapresen ça
doscampos.Nãoexistindo,odesenvolvedorseráinformadoarespeito.
126

## Página 133

CasadoCódigo Capítulo5. Domínioepersistência
Uma outra opção interessante para este atributo é simplesmente não
incluí-lonaconfiguraçãodoambiente,oqueirágerarcomoresultadoum
comportamentomuitoparecidoaodo validate:adiferen çaéqueoserrospo-
derãoaparecerapenasquandoosistematentaracessarumatabelaoucampo
inexistentenobancodedados.
Emambientededesenvolvimentoaop çãomaisinteressanteé update,
poisonormaléqueoprogramadortenhaumconjuntoderegistrosqueusa
duranteodesenvolvimentodasfuncionalidadesdosistema.
Emambientesdeprodução,observa-seumcomportamentosimilar:nas
primeirasversõesémuitonormalaconfiguraç ãooriginalser updatee,pos-
teriormente,conformeabaseaumentadetamanhoevaisetornandomais
estável,validatepassaráaseranorma.
Fig.5.5:Atençãoredobrada!
Armadilha
Eviteincluirachave dbCreatenobloco dataSourcepresenteno
iníciode DataSource.groovy: lembre-sequeelaseráusadacomo
padrãonosdemaisambientescasonestesnãosejadefinidooseuvalor.
Pool de conexões
Umpontoimportanteaserlevadoemconsideraç ãonaconfiguraçãode
qualquerfontededadoséagerênciadeconexões.Podenãoparecer,masuma
conexãocomobancodedadoséumrecursomuitocaro,cujamáadminis-
traçãoiráafetaraescalabilidade,estabilidadeedesempenhodosistema.
Amelhorestratégiausadaparaadministrarasconexõescomobancode
dadoséaado çãodeumpooldeconexões. Umpoolnadamaiséqueum
repositório(umcache)noqualincluímosobjetoscujacriaç ãoécaraeque
127

## Página 134

5.4. Datasource:conectando-seaoSGBD CasadoCódigo
possamserreaproveitados.Aideiaébastantesimples:secriarumaconexão
écaro,porquejogá-laforasepodemosusá-lanovamente?
Narealidade, naconfiguraçãodobloco dataSourcequevimosaté
agorafizemosumpooldeconexões,obradasconven çõesdoGrails.Umpool
queiráarmazenarnomáximo10conexões.Ok,vocêjásabequeumpoolé
estecachedeobjetos,mascomoelefunciona?
Imagineumpoolquecontenhaapenasumaconexão:quandonossaapli-
caçãorecebeumarequisição,elausaaconexãopresentenestepoole,fina-
lizadootrabalho,odevolveaopoolparaquepossaserusadoporumapró-
ximarequisição.Paraumsistemacompouquíssimosacessos(digamos,um
porhora),estaéumaconfiguraçãoque,aomenosingenuamente,fazalgum
sentido(quasenenhumnarealidade).
Agoravamosimaginarquederepenteoutrosusuáriosdescobremseu
projetoeagoratemosdoisusuáriosquedesejamacessá-laaomesmotempo.
Aprimeirarequisiçãoquechegaraosistemairáobteraconexão,deixandoa
requisiçãoconcorrenteemestadodeesperaatéqueestaconexãoestejadispo-
nívelepossaserusada.Tendosorte,oprocessamentodaprimeirarequisiç ão
serárápidoenossousuárioiráexperimentarapenasumalentidãoleveno
sistema.
Parapiorarumpoucomaisasituaç ão,imaginequeagoratrêsusuários
tentemacessarosistemaaomesmotempo.Doisficarãoemestadodeespera,
easituaçãosópioraconformenossaaplicaçãovaisetornandomaispopulare
cadavezmaispessoasqueremacessá-la.Asoluçãoéaparentementesimples:
bastaaumentarotamanhodonossopooldeconexões,certo?Vamosagora
pensaremumasituaçãooposta.
Aequipededesenvolvimentodanossaaplicaç ãoesperaqueumnúmero
grandedeusuáriosacesseosistema,entãoconfiguraumpooldeconexõesca-
pazdearmazenar500conexõeseaparentementeparecemteracertado,pois
namédiaháuns300usuáriosacessandodeformaconcorrenteosistema,mas
observamalgointeressante: háproblemasdedesempenho. Usandoferra-
mentasdemonitoramentonãoconseguemencontrarproblemasemseucó-
digoGrails.Oservidornãoestáconsumindo100%daCPUoudosrecursos
computacionais.
Équandoresolvemolharparaoservidornoqualseencontraemexecu-
128

## Página 135

CasadoCódigo Capítulo5. Domínioepersistência
çãooSGBD,enele,sim,oconsumodeCPUestáaltíssimo.Arazãoésimples:
aquelainstalaçãonãoestavapreparadaparalidarcomumnúmerodecone-
xõesmaiordoquecem.
Estesdoisexemplosmostrambemacomplexidadeenvolvidanaconfi-
guraçãodopooldeconexões. Nãoésimplesmentedefiniromaiornúmero
possível,massimanalisarosprincipaisatoresenvolvidos: suainstânciado
SGBDeseuservidordeaplicações.Nãoháumaregradeouroparaaobten-
çãodestenúmero.Leveissoemconsideração.
Asconfiguraçõesdopooldevemserinseridasnobloco properties,
presentenointeriorde dataSource,talcomonoexemploaseguir:
environments {
production {
dataSource {
dbCreate = "update"
url = "jdbc:mysql://localhost/paideia"
properties {
maxIdle = 50
maxActive = 50
minIdle = 10
testOnBorrow = true
}
}
}
}
Éimportantemencionarqueaschavesdeconfiguraç ãodopoolpodem
variardeacordocomoservidordeaplicações/servletadotado. Nestelivro,
seráexpostaamaispopularentredesenvolvedoresGrails,queéanativado
ApacheTomcat7;noentantoosvaloresexpostospossuemnomesquesãotão
comunsentreasdiversasimplementaçõesquenapráticaacabamformando
umpadrão.Vamosàschaves,portanto.
Astrêsprincipaischavesdeconfiguraçãodeumpooldeconexõessão
aquelasquedefinemoseutamanho.Emnossocasosãoasseguintes:
•maxIdle:onúmeromáximodeconexõesqueopooldevemanterpron-
tasemmododeespera.
129

## Página 136

5.4. Datasource:conectando-seaoSGBD CasadoCódigo
•minIdle:onúmeromínimodeconexõesqueopooldevemanterpron-
tasemmododeespera.
•maxActive:onúmeromáximodeconexõesativasquepodemsercri-
adasaomesmotempopelopool.
Ao definirmos o número mínimo de conexões em modo de espera,
quandoaaplicaçãoéiniciada,automaticamenteestasconexõesserãocria-
daseestarãoprontasparauso. Estaconfiguraçãoéimportantepoissebem
definidairáreduzirsignificativamenteotempodeesperaqueseusvisitantes
terãocasonãohajaaindaconexõesdisponíveisparaasuaaplicaç ão.
(Sabeaquelecasoemqueosusuáriosdoseusistemareclamamqueno
iníciododiaeleémuitolento? Nãoéraroacausadoproblemaseramá
configuraçãodoatributo minIdledopooldeconexões.)
Fig.5.6:Aten çãoredobrada!
Oleitordeveficaratentoparaumaarmadilhasutilenvolvendopoolsde
conexão: vocêsemprepodecorreroriscodeusarumaconexãoinválida.
Como?Simples:seuservidorSGBDirádescartaraquelasconexõesqueeste-
jaminativaspormuitotempoparaliberarrecursos.Aquiestáasituaç ão.
Imaginequesuaaplicaçãorecebadiversasrequisiçõesduranteodia,mas
queànoiteosacessosaelacessem.Esseéumcenáriomuitocomumemapli-
caçõescorporativas,cujopicodeacessoocorreduranteohoráriocomercial.
Seupooldeconexõesestácorretamenteconfigurado,asconexõesestãotodas
láetudoparecelindoeperfeitoatéqueosprimeirosacessosaosistemana
manhãseguinteresultamemumasériedeerrosdeconexãocomabasede
dados.
Essaéumasituaçãobastantecomumequeassombradiversosiniciantes
(jáviumcasonoqualaequipedeTItinhacomopráticaacessarosistema
pelamanhãparaevitarqueosusuáriostopassemcomesteerro)eaquiestáa
razãoportrásdestefenômenoecomoresolveroproblema.
130

## Página 137

CasadoCódigo Capítulo5. Domínioepersistência
TodoSGBDparaevitarconsumirtodaamemóriadoservidordescarta
aquelasconexõesqueencontram-seinativaspormuitotempo.Aodescartar
aconexão,noentanto,nãoavisaaoclientequeaquelaconexãoéinválida.E
oqueocorrequandoasuaaplicaç ãotentausaraquelaconexãoquefoiinva-
lidadapeloSGBD?Erro.
Asoluçãoparaoproblemaébastantesimples:bastadefiniralgumascha-
vesdeconfiguraçãonoseupool,comonocódigoaseguir:
environments {
production {
dataSource {
dbCreate = "update"
url = "jdbc:mysql://localhost/paideia"
properties {
maxIdle = 50
maxActive = 50
minIdle = 10
// as chaves abaixo resolvem o problema
testOnBorrow = true
validationQuery = "SELECT 1"
testWhileIdle = true
maxAge = 10 * 60000
}
}
}
}
Asquatrochavesexpostasnessecódigoservemparagarantirquetodaco-
nexãoretornadapelopooléválida.Aseguir,vemosadescriçãodestaschaves:
•testOnBorrowsedefinidocomo true,semprequeumclientedopool
requisitarumaconexão,vaiverificarseaconexãoéválida.Issoéfeito
executando-sealgumaconsultasimplescontraoSGBD,quenaquele
momentosaberáqueaconexãonãoestáinativahátantotempoassim.
•validationQuery éainstruçãoSQLenviadaaoSGBDquandoverifi-
camosseaconexãoéounãoválida.Optesemprepelainstruç ãomais
simplespossível,depreferênciaquenãorequeiradadoalgumpresente
131

## Página 138

5.4. Datasource:conectando-seaoSGBD CasadoCódigo
nobancodedados. Sempre use comandos simples e leves nesta con-
sulta.
•testWhileIdleasconexõestêmsuavalidadeverificadaenquantoestão
noestado idle.Seestiverativada,aop ção testOnBorrowpodeser
definidacomvalor false.
•maxAge qualotempomáximodevida(emmilissegundos)deuma
conexão.Issoevitaqueconexõesantigasfiquemnoseupooldecone-
xões.
JNDI
Talvezalgotenhaincomodadooleitornestanossase ção:ascredenciais
deacessoaoSGBDencontram-seexpostasemtodososexemplos.Aindapior:
muitasvezesnãosabemosquaisosparâmetrosquedevemosadotarnacon-
figuraçãodopooldeconexões.Seráqueérealmentesegurotornarexpostaa
nossaURLdeacessoaoSGBDtalcomotemosfeito?Háumamaneiramelhor
defazeristo?
Arespostaésim:umdosmaispoderososrecursosdaplataformaJavaé
oJNDI(Java Naming and Directory Interface),queéumaAPIparaacesso
aserviçosdediretórios. Umserviçodediretórioforneceaodesenvolvedor
umamaneirabastantepráticadesedisponibilizaràsaplicaçõesrecursosim-
portantes,como,porexemplo,fontesdedados(data sources),queéoassunto
destaseção.
Todososservidoresdeaplicação/servletJavaoferecemcomorecursoa
possibilidadedeproverfontesdedadosviaJNDI.Comisso,tudooqueo
programadorprecisasaberparapoderacessá-laseráocaminhodamesma,
comoconfiguradanoservidordeaplicação.
Agrandevantagemdestaabordageméamelhordivisãoderesponsa-
bilidades. Oresponsávelpordefinirosparâmetrosdepool,credenciaisde
acessoetudomaispassaaseroDBAouaqueleencarregadodeadminis-
traroSGBD,ocultandotodosestesdetalhesdaaplicaç ãoe,aindamaislegal:
simplificandoaoextremoaconfiguraçãoqueprecisamosdigitarnoarquivo
DataSource.groovy. NocódigoaseguirpodemosvercomousarJNDI
comGrails.
132

## Página 139

CasadoCódigo Capítulo5. Domínioepersistência
environments {
production {
dataSource {
jndiName = "java:comp/env/seuDataSource"
}
}
}
Comopôdeservistonocódigoanterior,tudooqueodesenvolvedorpre-
cisarádefiniréoatributo jndiNamefornecendocomovalorocaminhoJNDI
quelevaàfontededados.Suascredenciaisdeacessoestringdeconexãoao
SGBDnãoestãomaisnocódigo-fonte.Eomaisinteressante:agora,casoseja
necessárioalterarasconfiguraçõesdasuafontededados,nãoserámaisne-
cessáriofazerodeploydoseuarquivo WARnoservidor. Bastamodificara
configuraçãonopróprioservidordeaplicaçõese,emseguida,reiniciarasua
aplicaçãoparaqueessasmudan çasfaçamefeito.
Consulteadocumentaçãodoseuservidordeaplicaçõesparasabercomo
tirarproveitodesterecurso.
133

## Página 140

5.5. Voltandoàmodelagemdasclassesdedomínio CasadoCódigo
Configuração do sistema ConCot
Casoqueiraexecutarosistema ConCotnoseuambientededesenvol-
vimento,énecessárioterinstaladoemseucomputadoroMySQL5.5+.
Primeiro,devesercriadoumusuáriochamado concot,comsenha
concot.NoMySQL,crieesteusuáriocomocomandoaseguir:
create user concot@localhost identified by 'concot';
Devemsercriadostrêsbancosdedados,relativosaosambientesde
produção,testeedesenvolvimento.Bastausaroscriptaseguirque,além
deoscriar,tambémforneceusuáriototalaousuário concot.
create database concot_prod;
grant all on concot_prod.* to 'concot'@'localhost';
create database concot_dev;
grant all on concot_dev.* to 'concot'@'localhost';
create database concot_test;
grant all on concot_test.* to 'concot'@'localhost';
5.5 V oltando à modelagem das classes de domí-
nio
Tudooquepoderíamosfalarsobreconfiguraç ãoGrailsnestecapítulojáfoi
dito. ConhecemosemdetalhescomonosconectamosaumSGBDenoca-
minho,talcomoprometido,desarmamosasarmadilhasqueencontramos.
Convenhamos,configuraçãonãoéumassuntoexcitante,masescrevercó-
digosim,eapartirdeagoravamosarregaç arasmangaselidardiretamente
comcódigoGrailsescrevendonossasclassesdedomínio.
VamosentenderagoracomoomapeamentoobjetorelacionaldoGORM
funciona.Paratal,vamosvoltaraosistema ConCotcujaprimeiraimplemen-
taçãovimosnocapítulo 4.
134

## Página 141

CasadoCódigo Capítulo5. Domínioepersistência
O domínio e sua tabela
Segundoaconven çãoadotadapeloGrails,asclassesdedomíniodevem
estarnodiretório grails-app/domain. Umaveziniciado,oframework
vaivarrertodasasclassespresentesnestapastaeexecutarasseguintesações:
• Todasserãoanotadascom@grails.persistence.Entity(@En-
tity).
• Métodosestáticosdepersistênciaebuscaserãodinamicamenteinseri-
dos.
• DependendodaimplementaçãoadotadapeloGORM,asunidadesde
persistênciaserãoautomaticamentecriadasnoSGBD,ouseja,nocaso
doHibernate,astabelas,deacordocomaconfiguraç ãodefinidano
arquivo DataSource.groovyserãocriadasoumodificadas.
Nestaseçãoiremostratardesteterceiropassoeentendercomoéfeitoo
mapeamentoentreosatributosdenossasclassesdedomínioesuasrespecti-
vastabelasnobancodedados.
Se está em grails-app/domain, uma tabela será criada
Uma dúvida comum entre iniciantes em Grails é a seguinte:
é possível termos classes não persistentes dentro do diretório
grails-app/domain?Respostarápida:não.
Pelaconvenção,todaclassepresentenestediretórioiráautomatica-
mentegerarumatabelanobancodedadoserecebernovosmétodos
quandooGrailsforiniciado. Sevocêquiserterclassesnãopersisten-
tes,bastasalvarseucódigo-fonteemalgumaoutrapastadoseuprojeto,
preferencialmenteo src/groovy(ou src/javacasoqueiralidarcom
códigoJava).
Paraentenderomapeamentoobjeto/relacionalvamosprimeiroanalisara
classededomíniomaissimplespresenteno ConCot,queé Categoria,cujo
códigopodemosveraseguir:
135

## Página 142

5.5. Voltandoàmodelagemdasclassesdedomínio CasadoCódigo
package concot
class Categoria {
String nome
}
Nanossaconfiguraçãoparaoambientededesenvolvimentodefinimoso
atributo create-dbcomo updateusandooMySQL.Executandoaapli-
caçãoeconsultandoobancodedados,encontraremosumanovatabelacha-
mada categoria.Ocomando show fields doMySQLvainosexpora
suaestruturaealgumassurpresassurgirão.
mysql> show fields in categoria;
+---------+--------------+------+-----+---------+----------------+
| Field | Type | Null | Key | Default | Extra |
+---------+--------------+------+-----+---------+----------------+
| id | bigint(20) | NO | PRI | NULL | auto_increment |
| version | bigint(20) | NO | | NULL | |
| nome | varchar(255) | YES | | NULL | |
+---------+--------------+------+-----+---------+----------------+
EsequisermosverqualcomandoSQLgerouatabela categoria,basta
executarainstrução show create table categoria noMySQLpara
vermosomodocomoaestruturadatabelafoigerada:
CREATE TABLE `categoria ` (
`id` bigint(20) NOT NULL AUTO_INCREMENT,
`version` bigint(20) NOT NULL,
`nome` varchar(255) NOT NULL,
PRIMARY KEY (`id`),
UNIQUE KEY `UK_prx5elpv558ah8pk8x18u56yc` (`nome`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8
Ok,oatributo nomefoideclaradonaclasse Categoriaeovemosna
tabela,maseste ide versionnão.Deondevieram?Sãooresultadodas
convençõesdoGrails.
136

## Página 143

CasadoCódigo Capítulo5. Domínioepersistência
Que atributos viram campos em uma tabela?
Paraqueosatributosemumaclassededomíniogeremcamposem
umatabelarelacionada,estedevesuprirdoisrequisitos:
• Nasuadeclaração,otipodeveserbemdefinido,ouseja,umatri-
butodeclaradocomo def nome nãoirágerarumcampo,poiso
GORMnãosaberáqualoseutipo,porém String nome sim.
• Deveestarforadalistadeatributostransientes.
Casoqueiradefinirumatributonasuaclassededomínioquenão
devaserpersistidonabasededados,bastadeclararoatributodotipo
estáticotransientsnasuaclassededomínio.Oexemploaseguirnos
mostraumaclassededomíniocujasenhanãoserápersistida:
class Usuario {
String senha
static transients = ['senha']
}
UmaclassededomínioGrailsnãoprecisaterdeclaradooatributoidenti-
ficador(queiráresultaremumachaveprimária).Casonãoexistaumatributo
chamado“id”(ouconfiguraçãocustomizadadecamposcomoveremosmais
àfrente)oGORMocriaráparanós.
Reparouquenãoprecisamosimplementarnenhumainterfaceouesten-
derclassealgumaaoescrevermosumaclassededomínio?Istoocorregraç as
ànaturezadinâmicadoGroovy.NomomentoemqueoGORMéiniciado,ele
irávarrertodasasclassesqueseencontremnapasta grails-app/domain.
Paracadaumadestasiráporpadrãoincluirosdoisatributosdefinidosante-
riormente.
A influência das restrições (constraints)
137

## Página 144

5.5. Voltandoàmodelagemdasclassesdedomínio CasadoCódigo
O atributo id, como já era de se esperar, corresponde ao atributo
responsável por identificar a classe de domínio (torná-la umente, tal
comovistonoiníciodestecapítulo). Seutipoirávariardeacordocom
o SGBD escolhido, graças aos dialetos do Hibernate5.4que vimos al-
gumas páginas atrás. No caso do Grails 2.3 e posterior, ao lidarmos
com o MySQL, não é necessário definir o dialeto: por padrão este será
org.hibernate.dialect.MySQL5InnoDBDialect.Podemosverore-
flexodissonocomandoSQLquegerounossatabela.Reparequeemseufinal
háainstrução Engine=InnoDB.
Jáocampo versionéincluídopeloGrailscomoestratégiadebloqueio
(lock).Nãosepreocupenestemomentocomesteatributo,vamostratá-locom
detalhesmaisàfrentenestelivro.
Umpontointeressanteaobservaréotamanhodocampo nome:255ca-
racteres.EsteéotamanhopadrãodefinidopelodialetodoHibernatenacri-
açãodestescampos. Nãogosteidotamanhodestecampo. Alémdisto,não
gostariaquealgumusuáriocadastrassenobancodedadosumacategoriasem
nome. Possoresolveressasquestõesaplicandoalgumasregrasdevalidaç ão
(constraints).Bastamodificaraclasseparaquefiquecomonocódigoaseguir:
package concot
class Categoria {
String nome
static constraints = {
nome nullable:false, blank:false, maxSize:128, unique:true
}
}
Oblocoestático constraintsdefineasregrasdevalidaç ãoaserem
aplicadasàclassededomínio. Algumasdasregrasdevalidaç ãovãorefletir
emoutrosdoisaspectosdoframework:nageraç ãodastabelasepáginaspor
scaffolding.Nãosepreocupeaindaementendercomofuncionamessasregras
devalidação.Ointeressantenestemomentoésaberosefeitosdasregrasde
validaçãoemnossaclassededomínio,oquepodemosfazerapagandoata-
bela categoriadobancodedadoseexecutandonovamenteaaplicaç ão.O
138

## Página 145

CasadoCódigo Capítulo5. Domínioepersistência
comando show fields in categoria doMySQLiránosmostrarum
resultadodiferenteagora:
mysql> show fields in categoria;
+---------+--------------+------+-----+---------+----------------+
| Field | Type | Null | Key | Default | Extra |
+---------+--------------+------+-----+---------+----------------+
| id | bigint(20) | NO | PRI | NULL | auto_increment |
| version | bigint(20) | NO | | NULL | |
| nome | varchar(128) | NO | UNI | NULL | |
+---------+--------------+------+-----+---------+----------------+
Aregradevalidação maxSizerecebecomovalorumnúmerointeiro.
Comoopróprionomejánosdiz,éusadaparagarantirqueotextofornecido
pelousuáriorelativoaumcamponãosejamaiordoqueovalordefinidona
regradevalidação. Casosejamaior,aentidadenãoserápersistidaeuma
mensagemdeerroseráretornadaaousuário.Maisdoqueisto,elatambém
definequalotamanhomáximodeumcampoemumatabela(oualguma
outraestruturadedadosdependendodaimplementaç ãodoGORMadotada
peloseuprojeto).
Éimportanteconhecerasregrasdevalidaç ãoqueinfluenciamageração
detabelas.Algumasdasmaispopularesencontram-seexpostasnalistagema
seguir.AlistacompletavocêencontraránadocumentaçãooficialdoGrails.
•nullable:esperaumvalorbooleanoe,quandodefinidocomo true,
irádefinirocampodatabeladetalmodoquenãoaceitevaloresnulos.
•maxSize:esperaumvalorinteirocomovalor,defineotamanhomá-
ximodocamponobancodedados.
•minSize:éoopostode maxSize;defineotamanhomínimodocampo
nobancodedados.
•unique:esperaumvalorbooleanoe,quandodefinidocomo true,irá
criarumíndicedeunicidadenocamporelacionado.
•scale:quandoaplicadoaatributosdotipo BigDecimal,acabamde-
finindoaescalaemcamposdobancodedadosquelidemcomvalores
depontoflutuantecomprecisãopredefinida.
139

## Página 146

5.6. Relacionandoentidades CasadoCódigo
5.6 R elacionando entidades
Praticamentetodosistemapossui entidades,enãoapenas umaentidade.E
raríssimasvezesaonosreferirmosaestasclassesdedomíniopensamosnelas
isoladamente:sempreseencontramrelacionadasdealgumamaneira.
NestaseçãoentenderemoscomolidamoscomrelacionamentosemGrails
edequemodovocêpodetirarproveitodestesrelacionamentosnamodela-
gemdosseussistemas.Masoquequeremosdizerquandousamosapalavra
relacionamento?Responderemosaestaperguntarevisitandoasclassesdedo-
míniodosistema ConCot4.
Relacionamento muitos para um
Vamoscomeçarpelorelacionamentomaissimplespossível: muitos para
um(many-to-one),tambémchamadode filho pai. Esterelacionamentonos
dizalgobastantesimples:paraqueumaentidadeexista,elaobrigatoriamente
deveestarrelacionadaaumaoutra. Confuso? Vamosilustrá-lausandoo
ConCot.
Comovocêdeveselembrar,oobjetivoprincipalportrásdo ConCoté
cadastraracotaçãodediversositensusadosnosprojetosda DDL Engenharia.
Namodelagemdosistema,KicoeGuto[?]decidiramquenãopoderiahaver
umitemquenãopertencesseaumacategoria.
Combasenestadefinição,ousuáriodosistemaaocadastrarumitemde-
veria,obrigatoriamente,criarprimeirosuacategoria,casoelaaindanãoexista
nobancodedados. Umitemcotadonosistema ConCotobrigatoriamente
devepertenceraumacategoria.Podemosrepresentargraficamenteesterela-
cionamentousandoodiagramaaseguir:
Fig.5.7:RelacionamentomuitosparaumnoConCot
140

## Página 147

CasadoCódigo Capítulo5. Domínioepersistência
Maisdoqueisto,orelacionamentotambémdefineaessênciadonosso
item.Estesófazsentidoenquantopertencenteaumacategoria.Talveztoda
estaconversapare çaestranhanestemomento,porématéofimdestase ção
tudoseráclarificado.
141

## Página 148

5.6. Relacionandoentidades CasadoCódigo
UML, agregação e composição
Nestelivro, usamosanotaçãoUMLpararepresentarorelaciona-
mentoentrenossasentidades.Casonãoconhe çaestanotação(ouviva
seesquecendodecomofazê-lo)segueaquiumresumobemrápido.
Otermo agregaçãorepresentarelacionamentosdotipo possui umeo
focoestáno containerdarelaçãoquepodeounãoestarrelacionadoaou-
traentidade.No ConCotvemosaagregaçãoaopensarmosnacategoria,
quepodeexistirindependentedapresen çaounãodeitens.
Naimagemaseguir, vemoscomorepresentarumaagregaç ãoem
UML:olosangodeveserdesenhadosemestarpreenchidodoladodo
container.
Fig.5.8:Representandoumaagregação
Aousarmosotermo composição,ofocoestánoobjetocontido,que
sótemsentido(sópodeexistir)serelacionadocomoseucontainer.Vol-
tandoaoexemplodo ConCot,oitemsóexisteserelacionadoaumaca-
tegoria.
Naimagemaseguir,vemoscomorepresentaracomposiç ão. Olo-
sangoaparecerápreenchidodoladodaentidadecontainer.
Fig.5.9:Representandoumacomposição
142

## Página 149

CasadoCódigo Capítulo5. Domínioepersistência
EmGrails,definirorelacionamentodotipomuitosparaumébastante
simples:bastaincluirumatributonanossaclassededomíniocujotiposeja
outraclassededomíniotalcomonocódigoaseguir:
class Item {
String nome
Categoria categoria
}
Executandoaaplicação,serácriadaumatabelachamada itemcujaestru-
turapodemosveraseguirexecutandoocomando show fields in item
doMySQL:
mysql> show fields in item;
+--------------+--------------+------+-----+---------+----------------+
| Field | Type | Null | Key | Default | Extra |
+--------------+--------------+------+-----+---------+----------------+
| id | bigint(20) | NO | PRI | NULL | auto_increment |
| version | bigint(20) | NO | | NULL | |
| categoria_id | bigint(20) | NO | MUL | NULL | |
| nome | varchar(128) | NO | | NULL | |
+--------------+--------------+------+-----+---------+----------------+
4 rows in set (0.03 sec)
Ocamporesponsávelporgerarorelacionamentoentreastabelas iteme
categoriasechama categoria_idque,comojáesperávamos,possuio
mesmotipodachaveprimáriaquevimosnatabela categoria.Maisdoque
isto,oHibernatetambémcriouorelacionamentoentreestastabelas.Usando
umaferramentademodelagemcomo,porexemplo,oMySQLWorkbench,é
possívelvisualizargraficamenteesserelacionamento.
143

## Página 150

5.6. Relacionandoentidades CasadoCódigo
Fig.5.10:Orelacionamentoentreastabelascategoriaeitem
ArestriçãocriadanestecasopeloGORMimpedequesejamexcluídos
registrosdatabela categoriacasoexistaumoumaisregistrosnatabela
itemqueosrelacione.AinstruçãoSQLusadaparageraratabela itemtorna
istobastanteclaro,comopodemosconferirexecutandoocomando show
create table item noMySQL:
CREATE TABLE `item` (
`id` bigint(20) NOT NULL AUTO_INCREMENT,
`version` bigint(20) NOT NULL,
`categoria_id ` bigint(20) NOT NULL,
`nome` varchar(128) NOT NULL,
PRIMARY KEY (`id`),
KEY `FK_skts` (`categoria_id `),
CONSTRAINT `FK_sktsq` FOREIGN KEY (`categoria_id `) REFERENCES `categoria `
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
Atéestemomento,temosumrelacionamento unidirecional,ouseja,a
classe Itemsabedaexistênciadaclasse Categoria,masocontrárionão
seaplica. Bastaconferirmosaimplementaçãode Categoria,quepossui
apenasumatributopararepresentarseunome:
class Categoria {
String nome
static constraints = {
144

## Página 151

CasadoCódigo Capítulo5. Domínioepersistência
nome nullable:true, blank:false, unique:true
}
}
Um para muitos
Setodoitempertenceaumacategoria,existirãodiversosregistrosdeitens
nobancodedadosreferenciandoomesmoregistrodatabela categoria.
Atéestemomentonãotemosumrelacionamentobidirecionalentreasduas
entidades( Iteme Categoria).Tornaremosbidirecionalorelacionamento
comoatributoestático hasMany.Paratal,vamosmodificaranossaimple-
mentaçãodaclasse Categoriaparaquefiquetalcomoexpostoaseguir:
class Categoria {
String nome
static hasMany = [itens:Item]
static constraints = {
nome nullable:true, blank:false, unique:true
}
}
Oatributo hasManyquandousadodevesempreserdeclaradocomoes-
tático.Elerecebecomovalorummapa,noqualcadachaveequivaleaonome
doatributoqueserácriadonaclasseemquefoideclaradopeloGORMno
momentodesuainicializaçãoe,comovalorrelacionado,onomedaclasse
contraaqualseráfeitaaassociação.
QuandoumaaplicaçãoGrailséiniciada,oGORMirávarrertodasasclas-
sesdedomínioquepossuamdeclaradooatributo hasManye,paracadauma
daschavesdeclaradasnomapa,injetaránaclasseumnovoatributo,dotipo
coleção( java.util.Collection)queiráreferenciartodososregistros
relacionadosàquelaentidade. Sendoassim,nocasodaclasse Categoria,
apósainicializaçãodoGORMteremosalgo,emtempodeexecuç ão,similar
aocódigoaseguir:
class Categoria {
String nome
145

## Página 152

5.6. Relacionandoentidades CasadoCódigo
Set<Item> itens
}
Masqueremosiralém:comomencionadonestase ção,oregistrodeum
itemno ConCotsófazsentidoenquantorelacionadoaumacategoria.Oque
realmentedesejamoséinstruiroGORMparaque,casoumacategoriaseja
salva,seusitenstambémsejamsalvos,eomesmocomportamentotambém
deveseraplicadonaexclusão.Entraemcenaoatributo belongsTo.
Paratornaronossorelacionamentobidirecionalecomcascateamento
completo,bastamodificarmosaclasse Itemparaquefiquetalcomonocó-
digoaseguir:
class Item {
String nome
static belongsTo = [categoria:Categoria]
}
Assimcomooatributo hasMany, belongsTotambémdeveserdecla-
radocomoumatributoestáticoetambémdeverecebercomovalorummapa,
noqualaschavescorrespondamaosatributosqueserãocriadosnaclassede
domínioeosvalorescorrespondamaclassesdedomíniopresentesemnosso
projeto.
Outro modo de usar o atributo B E L O N G STO
Oatributo belongsTopoderecebercomovalor,casosuaclassede
domíniopossuaapenasumrelacionamento,apenasonomedaclassere-
lacionada,comonoexemploaseguir:
class Item {
String nome
static belongsTo = Categoria
}
Nestecasoserácriadoemtempodeexecuç ãoumatributochamado
categorianaclasse Item.
146

## Página 153

CasadoCódigo Capítulo5. Domínioepersistência
Modificadanossaclasse Item,podemosescreverumcódigotalcomoo
quesegue:
import concot.*
def categoria = new Categoria(nome:"Parafuso")
categoria.addToItens(new Item(nome:"Sem porca"))
categoria.addToItens(new Item(nome:"Com porca"))
categoria.save()
Nocódigodoexemplo,primeirocriamosumanovacategoriacomonome
Parafuso.Emseguida,chamamosomisteriosométodo addToItensduas
vezes,instanciandoobjetosdotipo Item:umchamado Sem porca eoutro
Com porca. Parafinalizar,chamamosométodo save(queveremoscom
detalhesmaisàfrente)que,comoopróprionomejánosdiz,persisteosdados
nobancodedados.
Ointeressanteéqueaofinaldoscripttemostrêsregistrosnobancode
dados:umparaatabela categoriaedoisparaatabela item.
Usamosométodo addToparainserirelementosdentrodeumdosatri-
butosdefinidonomapa hasManydaclassecontainer. Éumaaplicaçãodo
dinamismodoGroovy,porestarazãonosreferimosaestemétodocomo
addTo*,onde *devesersubstituídopelonomedoatributodefinidonomapa
hasMany.
Ométodo addTo*portrásdospanosexecutaosseguintespassos:
• Garantequeexisteumacoleçãonaclassepairelacionadaaoatributo
chamado.Senãoexistir,eleserácriado.
• Naentidadedependenteaseradicionada,oatributorelacionadoaopai
serápreenchido.
• Incluiainstânciadependentedentrodacoleçãorelacionadanaenti-
dadepai.
147

## Página 154

5.7. Inserindo,editandoeexcluindoregistrosnobancodedados CasadoCódigo
Armadilha com hasM any
Fig.5.11:Atençãoredobrada!
Umaarmadilhaimportante:evitecódigoscomooseguinte:
def categoria = new Categoria(nome:"Parafuso")
// Perigo 1
categoria.itens.add(new Item("Com porca"))
categoria.itens.add(new Item("Sem porca"))
// Perigo 2
categoria.save()
Hádoisperigosnessecódigo.Oprimeiroéofatodenãotermoscer-
tezaseoatributo itensdanossainstânciade Categoriajáfoiins-
tanciado(nãofoi). Nestecaso,vamostoparcomumaexce çãodotipo
NullpointerException.
Osegundoperigoestánofatodequeoatributo categoriadaclasse
Itemnãofoidefinido.
5.7 I nserindo , editando e excluindo registros
no banco de dados
Comnossasclassesminimamentemodeladas,éimportantesabercomoin-
seriroueditarregistrosqueasrepresentemnobancodedados.Nocasodo
Grails,issoéfeitousandoumúnicométodo: save. Podemosextrairuma
sériedeinformaçõesaseurespeitoobservandooscriptaseguirnoqualper-
sistimosumanovacategoria.
148

## Página 155

CasadoCódigo Capítulo5. Domínioepersistência
def categoria = new Categoria(nome:"Cimento")
categoria.save()
Oqueestamosfazendoébastantesimples:criamosumanovainstânciada
classededomínio Categoriaquepossuaonome Cimentoe,emseguida,
evocamosométodo savenapróximalinha.Comistoestamosinserindoo
novoregistronabasededadosquepoderáserusadoportodoorestantedo
sistema.
Fig.5.12:Atençãoredobrada!
Noentanto,imaginoqueoleitorgostedeexplorarasconsequênciasdo
queacabamosdefazer.Entãovocêexecutaumaconsultacontraatabelado
bancodedadossimilaràexpostaaseguir:
select * from categoria where nome = 'Cimento';
Enenhumregistroaparece. BugdoGORM?Não: apenasocomporta-
mentopadrãodoHibernate.UmcomponentefundamentaldoHibernateéa
sessão.Pensenelacomoumcachelocalquearmazenaoestadodetodosos
objetosdedomínioquepersistimosouobtemosapartirdobancodedados.
Quandochamamosométodo saveemumobjetodedomínio,porpadrão
apenasomarcamosparaquesejapersistido eventualmentenobancodeda-
dos.
Quão eventualmente?Atéfinalizarmosnossasessão,sobreaqualfalare-
mosmaisàfrente. Paraobtermáximodesempenho,oHibernatearmazena
emumafilatodasasoperaçõesquedeverãoserexecutadascontraobancode
dadosesomenteasenviaaoSGBDquandoumadasduascondiçõesadiante
ocorre:
• Afilaatingeumtamanhoespecífico.
• Asessãoéfechada.
149

## Página 156

5.7. Inserindo,editandoeexcluindoregistrosnobancodedados CasadoCódigo
Ocustodelatêncianoenviodoscomandosésignificativamentereduzido
graçasaestecomportamentodoHibernate.Emvezdetermostodoocusto
deenviarmosumcomando,esperaroresultadodoseuprocessamentoeem
seguidaobterarespostadoSGBD,ofazemosemlote.Chamamosesteenvio
emlotedeinstruçõesde flushdasessão.
Oproblemadestaabordageméqueoestadodoobjetoficadisponível
apenasnoprocessodaJVMemquefoiexecutadaainstruç ãodepersistência.
Emumambientedistribuído,noqualoacessoaoestadodoobjetodevesero
maisatualeimediatopossível,estecomportamentopadrãodoHibernatedeve
serevitado.Comofazemosisto?Simples:bastapassarumsimplesparâmetro
aométodo save,talcomonoexemploaseguir:
def categoria = new Categoria(nome:"Cimento")
categoria.save(flush:true)
Oparâmetro flushcomvalor trueinstruioGORMapersistirimediata-
menteosdadosnobancodedados,evitandoassimoproblemamencionado.
Noentanto,lembre-sequehaveráumcustodedesempenhonocasodeins-
truçõesqueprecisemalterarumgrandenúmeroderegistros.
Ecomoeditoumregistro?Exatamentecomofariaparainserir.Noexem-
ploaseguiralteramosoregistro categoria.
def categoria = Categoria.findByNome("Cimento")
categoria.nome = "Cimento editado"
categoria.save() // agora se chamará "Cimento editado"
Reparounaquelemétodo findByNome?Seráoassuntodapróximases-
sãodestecapítuloquandoformostratardosmétodosdepesquisa.Parafina-
lizar,vamosreaproveitaromesmoexemploparaexcluirumregistro:
def categoria = Categoria.findByNome("Cimento")
categoria.delete()
Ométodo deleteéusadoparaexcluirumregistroeapresentaomesmo
comportamentoqueométodo save,sendoassimvocêpodepassaroparâ-
metro flushparaele,garantindocomistoapersistênciaimediatanabase
dedados.
150

## Página 157

CasadoCódigo Capítulo5. Domínioepersistência
V alidando a persistência
Classesdedomíniopossuemregrasdevalidaç ão.Oqueocorrequando
mandamospersistirumobjetoquefiraumadasrestriçõesquedefinimosem
nossodomínio? Vamosveroqueacontececomumexperimentosimples.
Primeiro,leveemconsideraçãoadefiniçãodaclasse Categoriaexpostaa
seguir:
class Categoria {
String nome
static constraints = {
nome blank:false, nullable:false
}
}
Observeque,deacordocomasregrasdevalidaç ão,onomenãopodeser
nuloouumastringvazia.Agora,observeoresultadodoscriptaseguir:
// criamos uma nova instância de categoria cujo atributo
// nome ainda não tenha sido definido, ou seja, será nulo
def categoria = new Categoria()
assert categoria.save() == null // passa no teste!
Fig.5.13:Atençãoredobrada!
Ovalorderetornodométodo saveéumobjetodomesmotipoda-
quelequeacabamosdepersistir.Casoocorraalgumerrodevalidaç ão,ova-
lorretornadoseránulo.Oproblemadestaabordageméqueelaésilenciosa:
nenhumaexceçãoserádisparadaporpadrãoeseoprogramadornãotomar
cuidado,podeterafalsaimpressãodequetudoocorreucomoesperado.Uma
maneiradeevitaresteproblemaéreescreveroscripttalcomo:
151

## Página 158

5.8. Entendendoocascateamento CasadoCódigo
def categoria = new Categoria()
if (categoria.save()) {
// tudo ok, retornou um objeto válido
} else {
// algo deu errado. trate aqui
}
Umamaneiraaindamaisinteressantedeseevitaroproblemaéusandoo
parâmetro failOnErrorcomovalor true.Casoocorraalgumerro,uma
exceçãodotipo ValidationException.Oexemploaseguirexpõebem
estapossibilidade.
def categoria = new Categoria()
try {
categoria.save(failOnError:true)
} catch (ValidationException ex) {
// trate o problema aqui
}
Nessecaso,épossíveldefinirodisparodaexce çãoporpadrão. Basta
alteraroarquivo grails-app/conf/Config.groovyincluindoachave
grails.gorm.failOnError,comonoexemplo:
grails.gorm.failOnError = true
Épossíveltambémdefinirocomportamentoporclasses.Paratal,basta
passarcomoparâmetroumalistadestringsnaqualcadaumarepresenteuma
dasclassesdoseudomínio,comonalistagemaseguiremquedefinimoso
comportamentoparaasclasses Categoriae Item.
grails.gorm.failOnError = ['concot.Categoria', 'concot.Item']
5.8 E ntendendo o cascateamento
Háum“pequeno”detalhesobremodelagemdeentidadesnoGORMque
aindanãofoimencionado: comoficaaquestãodocascateamento? Aliás,
oqueé cascateamento(cascading)?
152

## Página 159

CasadoCódigo Capítulo5. Domínioepersistência
Umconceitoessencialnosbancosdedadosrelacionaisé integridade re-
ferencial.Casooleitorjáestejafamiliarizadocomesteconceito,sugiropular
paraopróximotópicodestecapítulo.Valorizamosaintegridadereferencial
quandosentirmosnapelesuafalta.Imaginequeobancodedadosdo ConCot
encontre-setalcomoexpostonaimagemaseguir:
Fig.5.14:Otristemundosemintegridadereferencial
Comojásabemos,atabela item,geradaapartirdadefiniçãodaclassede
domíniodemesmonomepossuiumachaveestrangeira( categoria_id)
queestabeleceumarelaçãoum-para-muitoscomatabela categoria.Ob-
servandocomaten çãoaimagem,nota-sequeoregistrocujocampo idpos-
suivalor4natabela itemenfrentaumpequenoproblema:nãoexisteum
registroequivalentenatabela categoriacujoidentificadorsejaonúmero
4.Umitemsemcategoria,umregistroórfão.Oregistroquedeveriaexistir
natabela categoriaéoquechamamosde registro pai.
Vemosduassoluçõesparaoproblema:apreguiçosaserácriarumregistro
comocampo idiguala4natabela categoria. Trata-sedeumafalsa
soluçãopoisoproblemanãofoiresolvido. Sesurgiuumprimeiroregistro
órfão,nadaimpedeaocorrênciadeumsegundo,terceirooun-ésimocaso.
AsoluçãorealéinstruiroSGBDanãopermitiracriaç ãoderegistros
órfãos. Éa integridade referencialquemencioneianteriormente. Paravê-
laemprática,vamosexecutarocomando show create table item no
MySQLparaveraestruturadatabela itemcriadapeloGORM.Oresultado
seráumainstruçãoSQLsimilaràexpostaaseguir:
CREATE TABLE `item` (
`id` bigint(20) NOT NULL AUTO_INCREMENT,
`version` bigint(20) NOT NULL,
153

## Página 160

5.8. Entendendoocascateamento CasadoCódigo
`categoria_id ` bigint(20 ) NOT NULL,
`nome` varchar(128 ) NOT NULL,
PRIMARY KEY (`id`),
KEY `FK_2323` (`categoria_id `),
CONSTRAINT `FK_dk37` FOREIGN KEY (`categoria_id `) REFERENCES `categoria `
) ENGINE=InnoDB DEFAULT CHARSET=utf8
Nosinteressaapenasapenúltimalinhadainstruçãonaqualécriadauma
chaveestrangeira( FOREIGN KEY)paraocampo categoria_idquere-
ferenciaocampo iddatabela categoria. Sefôssemostraduzirparao
português,estecomandoseriaalgocomo:
“Apenaspermitaainclusãoderegistrosnatabela itemcujocampo
categoria_idencontre-sepreenchidoereferencieoutroregistrojáexis-
tentenatabela categoriacomomesmovalornocampo id”
Maisdoqueevitarainclusãoderegistrosórfãosnobancodedados,ain-
tegridadereferencialnestecasotambémevitaageraç ãodosmesmosseten-
tarmosexcluirumregistrodatabela categoriaquejáestejarelacionado
apelomenosumregistronatabela item,oSGBDtambémirábloqueara
exclusãodesteregistro.
O que é cascateamento?
Entendidoofuncionamentodaintegridadereferencial,podemostratara
questãodocascateamento,queéoassuntoprincipaldestase ção.Aousarmos
otermo cascataoleitordeveteremmenteaideiadeconsequência. Que tipo
de ação ao ser aplicada a uma instância de uma classe de domínio também deve
ser aplicada aos seus relacionamentos, isto é, seus filhos?.VoltandoaoGORM,
vemosqueháumasériedemétodosdepersistênciaqueexecutamoscontra
umaclassededomíniocomo, save(), delete(), merge(). Podemospensarna
conceituaçãode cascateamentocomo:
Cascateamento é a regra que define se queremos ver a repetição das ações
de persistência que executamos em uma entidade pai propagada em seus
filhos.
Oconceitoficaclarocomalgumasperguntasqueoleitordevesefazerao
modelarsuasclassesdedomínio.Perguntascomo: quando eu excluir, editar
ou salvar minha entidade pai, devo excluir, editar ou salvar seus filhos tam-
154

## Página 161

CasadoCódigo Capítulo5. Domínioepersistência
bém?. Comoditonoparágrafoanterior,apropagaçãoocorreparacadaum
dostiposdeoperaçãoquepodemosexecutarcontranossasclassesdedomí-
nio. Noentanto,nestelivro(eem90%dasuavidaprática)sóprecisamos
nospreocuparcomapropagação(propaga çãoéumexcelentesinônimopara
cascateamento)dasoperações save()e delete().
Paravalorizaroconceitodecascateamento,vamosprocederexatamente
comofizemosaopensarnoconceitode integridade referencial.Vamosima-
ginaromundosemele.Paratal,convémlembrardadefiniç ãodasclassesde
domínio Categoriae Itemexpostasaseguir:
class Categoria {
String nome
}
class Item {
String nome
static belongsTo = [ categoria:Categoria]
}
Semcascateamento,casoeuqueiracriarumanovacategoriaeadicionar
aelatrêsitens,eudeveriaescreverumcódigocomooseguinte:
def materiais = new Categoria(nome:"Materiais")
materiais.save()
def cimento = new Item(nome:"Cimento", categoria:materiais)
cimento.save()
def argamassa = new Item (nome:"Argamassa", categoria:materiais)
argamassa.save()
def brita = new Item(nome:"Brita", categoria:materiais)
brita.save()
Paracadaumdositensfoinecessáriochamarindividualmenteométodo
save().Agora,voltemosaomundocomcascateamento,masantesfaremos
umapequenamodificaçãonaclasse Categoriaparaquetenhamosumre-
lacionamentobidirecional:
class Categoria {
String nome
155

## Página 162

5.8. Entendendoocascateamento CasadoCódigo
static hasMany = [itens:Item]
}
Aocriarmosesterelacionamentobidirecional,podemosusarométodo
addToquevimosnestecapítuloereescrevernossoscriptinicialdeumaforma
muitomaisconcisa:
new Categoria(nome:"Materiais")
.addToItens(new Item(nome:"Cimento"))
.addToItens(new Item(nome:"Argamassa"))
.addToItens(new Item(nome:"Brita"))
.save() //voilá!
Reparequesóprecisamosexecutarométodo save()naentidadedomi-
nantedorelacionamentoqueé Categoria.Tirandoproveitodocascatea-
mento,portrásdospanosoHibernateexecutouométodo save()primeiro
em Categoriae,emseguida,emtodososobjetosrelacionadosaeste.
Voltemosaoexemploanterior,eimaginemosquejátemosdefinidoem
nossobancodedadosumarestriç ãoquenosimpe çadeapagarumregistro
databela categoriacasoestajápossuafilhos. Semcascateamento,para
evitarmosaocorrênciadeumerroprecisaríamosexecutarumscriptcomoo
expostoaseguir:
/* Você entenderá o que este ::findByNome:: é
mais à frente neste capítulo.
Por enquanto pense nele apenas como uma consulta
que nos retorna uma instância de Categoria pelo
nome "Materiais" */
def categoria = Categoria.findByNome("Materiais")
/* O mesmo para este método findAllByCategoria ;) */
def itens = Item.findAllByCategoria(categoria)
for (item in item) {
item.delete()
}
categoria.delete()
Serianecessárioapagarcadaumdosregistrosrelacionadosesóaofinal
apagaroregistrodacategoriacujonomeé Materiais.Comoéomundo
comcascateamento?Exatamentecomonoscriptaseguir:
156

## Página 163

CasadoCódigo Capítulo5. Domínioepersistência
def categoria = Categoria.findByNome("Materiais")
categoria.delete() //todos os filhos serão apagados
Pelocascateamento,écomoseométodo delete()fossechamadopara
todososfilhosdainstânciade Categoriaqueencontramos. “Comose”,
poisnapráticaoHibernateotimizaráesteprocessoparaevitaroconsumo
excessivoedesnecessáriodosseusrecursoscomputacionais.
Istoéoquechamamosde propagaçãoou cascateamentodeoperaçõesde
persistência. Reduzimosaquantidadedecódigoqueprecisaríamosdigitar,
obtivemosumcódigomaislimpoecomumapossibilidadebastantemenor
deteralgumbugeuma maior garantia de que manteremos a integridade
referencial do nosso banco de dados.
Aoleitormaiscuriosoquequeirasabermaisdetalhessobrecomoocasca-
teamentorealmenteéimplementado,recomendoaleituradase ção Transitive
PersistencedadocumentaçãooficialdoHibernate[16].
Cascateamento no GORM
Comosconceitosbemcolocadoseentendidaarazãopelaqualexisteo
cascateamentopodemosagoravercomooGORMlidacomesteconceito.
Achaveparatirarmáximoproveitodesterecursoéentenderqueoatributo
estático belongsToéoresponsávelpeladefiniçãodoscascateamentosno
GORM.
Quando em Item adicionamos a definição belongsTo =
[categoria:Categoria] estamos informando ao GORM qual classe
dominaaquele relacionamento, neste caso,Categoria. Lembre-se: o
cascateamento sempre é direcionado do pai para seus filhos.
Tantofazseestamoslidandocomumrelacionamentodotipo um-para-
um, um-para-muitosou muitos-para-muitos. Semprequeestiverpresente
oatributo belongsTonadefiniçãodeumrelacionamento,asoperações
save()e delete()serãopropagadasdaentidadepaiemdire çãoaosseus
filhos.
Equandonãoadicionamosoatributo belongsTonadefiniçãodeum
relacionamento? Nessecaso,nenhumcascateamentoiráocorreretermina-
remosnasituaçãoexpostanotópicoanteriordestase çãoquandodescreve-
mosomundo“semcascateamento”.Háumaexceção,noentanto,queocorre
157

## Página 164

5.8. Entendendoocascateamento CasadoCódigo
quandousamosapenasoatributo hasManyemnossasclassesdedomínio.
Nessecaso,aentidadequecontémoatributoétidacomopaieaoperaç ão
save()serápropagadaàsentidadesfilhasrelacionadas.
Parafinalizarestase ção,éimportantequevocêconhe çaasconven ções
adotadaspeloGrailscomrelaçãoàsconfiguraçõesdecascateamentoqueirão
variardeacordocomomodocomomodelamososrelacionamentosentre
nossasentidades.Valelembrarquepodemoscustomizarestescomportamen-
toscasosejadenossointeresse.Paraentenderposteriormentecomoistodeve
serfeito,recomendoqueoleitorleiaocapítulo[?],destelivronoqualdes-
crevemoscomocustomizaromapeamentoobjetorelacionaldoGORM.
Oesquemaexpostoaseguiréinspiradonadocumentaç ãooficialdo
Grails[5]eexpõebemcomoasconfiguraçõesdecascateamentovariamde
acordocomamodelagemdosnossosrelacionamentos.
Relacionamento bidirecional um-para-muitos usando belongsT o
Usadoquandodefinimosrelacionamentossimilaresaoexpostoaseguir:
class Pai {
static hasMany = [filhos:Filho]
}
class Filho {
static belongsTo = [pai:Pai]
}
NaclassePaiocascateamentoencontra-seconfiguradoporpadrãocomo
ALL,ouseja,todaoperaçãodepersistênciaautomaticamenteserácascateada
nosfilhostambém. Jádoladofilhoocascateamentoencontra-sedefinido
como NONE,ouseja,operaçõesdepersistêncianosfilhosnãoserãoreplicadas
nasentidadespai.
Relacionamento unidirecional um-para-muitos usando apenas has-
Many
class Pai {
static hasMany = [filhos:Filho]
}
class Filho {
158

## Página 165

CasadoCódigo Capítulo5. Domínioepersistência
}
Ocascateamentoestaráativadoparaasaçõesdeinser ção( SAVE)eedição
( UPDATE)nosentidoPai->Filho.
Relacionamento bidirecional um-para-muitos sem usar belongsT o
class Pai {
static hasMany = [filhos:Filho]
}
class Filho {
Pai pai
}
Doladopai,aestratégiadecascateamentoseráparaasoperaçõesdeinser-
ção( SAVE)eedição( UPDATE).Jádoladofilhoasoperaçõesdepersistência
nãoirãocascatearnasentidadespai( NONE).
Relacionamento unidirecional um-para-um sem belongsT o
class Pai {
}
class Filho {
static belongsTo = [ pai:Pai]
}
Doladopaiocascateamentoserádotipo ALL,ouseja,abarcarátodasas
operaçõesdepersistênciaenquantodoladofilhonãohaverácascateamento(
NONE)algumchegandoàsentidadespaideclaradas.
5.9 C ustomizando o mapeamento
Muitasvezes,asconfiguraçõespadrãodemapeamentoadotadaspeloGORM
nãoseadequamàspolíticasdegestãodebancodedadosdoseuclienteou
empresa.Nessescasos,podemosalterarseucomportamentoparaquepossa
atenderaestesrequisitosdeumaformabastantesimplesusandoobloco
159

## Página 166

5.9. Customizandoomapeamento CasadoCódigo
mapping,quenospermitecustomizaraindamaisomodocomoomapea-
mentoobjetorelacionaldoGORMéfeito.
Outrarazãopelaqualéinteressantecustomizaromapeamentoocorre
quandovocêjápossuiumbancodedadosprontoequerapenasusarsuas
tabelasjácriadasemsuaaplicação,oquetambémébastantecomum.
Noexemploaseguirpodemosvercomodeclararobloco mappingem
nossasclassesdedomínio:
class Cotacao {
static mapping = {
}
}
Alterando o nome da tabela (e seu esquema e catálogo quando ne-
cessário)
Paraalteraronomedatabelaquedeveráreceberosdadosdanossaenti-
dade,bastaincluirainstrução tabletalcomonoexemploaseguirnaqual
iremosmudaronomedatabelapadrãoincluindooprefixo DDL.
class Cotacao {
static mapping = {
/*
Ao invés do padrão "cotacao",
o nome da tabela aonde armazenaremos
nossos dados será agora "DDL_cotacao"
*/
table "DDL_cotacao"
}
}
Emsituaçõesnasquaisvocêprecisecustomizaroesquemaoucatálogo
noqualatabelaseencontra,doisnovosparâmetrospodemserpassados:
schemae catalog,comoaseguir:
class Cotacao {
static mapping = {
160

## Página 167

CasadoCódigo Capítulo5. Domínioepersistência
table name:"DDL_cotacao", schema:"dbo", catalog:"cotacoes"
}
}
Observequeseformospassarmaisdeumparâmetroparaainstruç ão
tableprecisamosnomearexplicitamentetodososqueestiverempresentes.
Apenasquandoalteramosapenasonomedatabelapassamosumúnicovalor.
Oleitordeveterobservadoqueéincluídoumcampochamado version
emtodasasnossastabelas. Eleéusadopelapolíticadebloqueiootimista
(optimistic locking)adotadaporpadrãopeloGORM.
BloqueiootimistaéumrecursodisponibilizadopeloHibernatenoqual
écriadoumcampodeversionamentoemque,acadaatualizaç ão(update)
deumregistro,ovalordomesmoéincrementado.Oobjetivodesterecursoé
trataroacessoconcorrenteaummesmoregistronobancodedados.Paraen-
tenderseufuncionamento,imaginedoisusuáriossimultaneamenteeditando
amesmacotaçãono ConCot.
//Usuario 1 pega a cotacao de id 34
//Neste momento, o valor do campo version é 1
def cotacao1 = Cotacao.get(34)
cotacao1.valor = 56
//Paralelamente, o usuário 2 pega a mesma cotaçaõ
def cotacao2 = Cotacao.get(34)
//O valor do campo version ainda é 1
cotacao2.valor = 4
// É persistida a cotação e automaticamente o
// campo version será incrementado, passando a
// ter o valor 2
cotacao2.save(flush:true)
// Usuário 1 demora um pouco mais em seu processamento
// e irá atualizar o registro
cotacao1.save(flush:true)
Por trás dos panos, no momento em que o primeiro usuá-
rio tentar persistir os dados da cotação, o Hibernate irá verifi-
161

## Página 168

5.9. Customizandoomapeamento CasadoCódigo
car se o valor do campoversion na tabela cotacao bate com
o presente em memória. Se for diferente, uma exceção do tipo
org.hibernate.StaleObjectStateException será disparada e,
casoestejaexecutandoocódigoemumatransaç ão,orollbackseráexecu-
tado.
Claro,vocêpodedesabilitarolockotimistaemsuaentidade. Paratal,
bastapassarovalor falseparaainstrução versionnobloco mapping
talcomonoexemploaseguir:
class Cotacao {
static mapping {
version false
}
}
Talvezonomedocampo versionconflitecomsuatabelapreexistente
nobancodedados.Nestecaso,bastapassarcomovaloronomedocampotal
comonoexemploaseguir:
class Cotacao {
static mapping {
/*
Ao invés de "version", "bloqueio",
e o bloqueio otimista é mantido
*/
version "bloqueio"
}
}
Customizando o identificador
PorpadrãoparaamaiorpartedosSGBDsdomercado(aomenostodos
osqueconhe çoejátrabalheidiretamente)GORMiráusaraestratégiado
valorautoincrementalparaalimentarachaveprimáriadatabelarelacionada
àsuaclassededomínio.
Nemsempreestaéamelhorestratégia.Talvezvocêqueiraqueovalorda
suachaveprimáriauseumaestratégiacomoUUID[26]quearmazenaráseus
162

## Página 169

CasadoCódigo Capítulo5. Domínioepersistência
valoresemumaStringemvezdeumvalornumérico,oumesmodesejeusar
chavescompostasparadefiniroidentificadordasuatabela.
Primeiro,vamosvercomomodificarotipoeestratégiadegeraç ãodeda-
dosparaachaveprimária. Querqueseucampo idcontenhatextoeuse
aestratégiaUUID[26]? Oprimeiropassoédeclará-lodiretamenteemsua
classededomíniocomo Stringe,emseguida,usarainstruç ão id,como
noexemploaseguir:
class Cotacao {
String id
static mapping = {
/*
Atributo generator me diz qual estratégia de
geração adotar
E column me permite mudar inclusive o nome do
campo id na tabela!
*/
id id generator:'uuid', column:'identificador'
}
}
Hádiversasestratégiasdegeraçãodeidentificadoresdiferentes. Todas
estãodiretamenterelacionadasaoHibernateesãodemasiadamentevariadas
parapodersertratadasaqui,masvocêpodeconsultarsuadocumentaç ãoofi-
cialparaconhecê-lasmelhor[7].
Vocêtambémpodedefinirqueaidentificaçãodasuaentidadeécomposta
pormaisdeumatributo.Paraisso,bastausaroparâmetro composite,que
recebecomovalorumalistacontendooscamposqueirãogerarsuachave
composta:
class Cotacao {
static mapping = {
/*
Id gerado pelos atributos item e
fabricante.
*/
id composite:[ 'item','fabricante']
163

## Página 170

5.9. Customizandoomapeamento CasadoCódigo
}
}
Alterando a ordem padrão nas consultas
Vocêtambémpodecustomizaraordemnaqualoselementosdeuma
consultaàssuasclassesdedomínioserãoretornados.Paratal,bastausaras
instruçõessorte order,comonoexemploaseguirnoqualdefinimosque
todasascotaçõesvirãoordenadasporvaloremordemdecrescente:
class Cotacao {
static mapping = {
sort: 'valor'
order: 'desc' // 'asc' para ordem crescente, que é o padrão
}
}
Claro,issosóseráaplicadoquandovocênãodefiniraordenaçãoemsuas
consultas.Vejaaseguir,usandoumfinderdinâmico:
//Valores retornarão ordenados por valor
//em ordem decrescente
Cotacao.list()
Customizando as demais colunas
Claroqueacustomizaçãonãoparaporaqui,vocêtambémpodealterar
omodocomosãomapeadososdemaisatributosdasuaclassededomínio.
Paratal,bastaincluironomedoatributonoblocomappinge,emseguida,
aplicaralgunsparâmetroscomonoseguinteexemplo,emquecustomizamos
fortementeaentidade Usuario:
class Usuario {
String id
String login
String senha
static mapping = {
id generator:'uuid'
164

## Página 171

CasadoCódigo Capítulo5. Domínioepersistência
table 'DDL_usuarios'
version false
login column:'username', sqlType:'char', updatable:false
senha column:'password', sqlType:'char', updatable:false
}
}
Háumalistasignificativadeparâmetrosquepodemserusadosnomape-
amentodosseusatributos.Dentreeles,osmaiscomunssãolistadosaseguir:
•column:recebeumastringcomovalorrepresentandoonomedaco-
lunaaserusadanatabela.
•sqlType:vocêpodecustomizarqualtipoSQLaserusadonatabela.
Nestecaso,vocêdeveconsultaradocumentaç ãodoseuSGBDpara
descobrirquaisosvaloresdisponíveis.
•updatable:defineseocampoéatualizávelounão,permitindoque
seuvalorsejadefinidoapenasnomomentodeinser ção.Valorpadrão:
true.
•insertable:definequeovalordocampopodeserdefinidoapenas
poratualização,enãonainser ção.Valorpadrão: true.
•length:qualotamanhomáximodocamponatabela.
165

## Página 172

5.10. Lidandocomherança CasadoCódigo
Dica:mapeie views!
Muitasvezesencontramossituaçõesembasesdedadoslegadasnas
quaisprecisamosdeumaentidademasestanãoéfacilmentemapeada
paraumatabelaespecífica,massimumconjuntodetabelas.Nessesca-
sos,umaop çãointeressanteéusaromapeamentocustomizadocontra
umaview.Vocêperderáacapacidadedealterarosdados,maspelome-
nosteráumaopçãointeressanteparavisualizaçãoeconsultas!
Mapeandoviews,vocêpode,inclusive,tirarproveitodospoderosos
recursosdeconsultadoGrailsqueveremosnopróximocapítulopara
criaraplicaçõesquefacilitemaosseususuáriosextrairimportantesin-
formaçõesdesuasbasesdedadoslegadas.
5.10 L idando com herança
Antesdefinalizarestecapítuloéprecisofalardo“elefantebranco”queestá
entrenósedoqualatéagoranãofalamosarespeito: comolidarcomhe-
rança?Afinaldecontas,estamoslidandocomumaferramentaquefazoma-
peamento objetorelacional.:)
Infelizmente,no ConCotnãoháumexemplodeheran ça,sendoassim
porquenãousarumqueébastantepopular?Cadastrode“pessoas”.Nale-
gislaçãobrasileirahádoistiposde“pessoa":físicaejurídica.Oprimeirotipo
correspondeaindivíduoscomoeuevocê,easegundaaempresas.
Umamodelagemsimplesdestasituaçãopodeservistanodiagramaase-
guir:
166

## Página 173

CasadoCódigo Capítulo5. Domínioepersistência
Fig.5.15:Nossaspessoas
Eaimplementaçãoinicialdasnossasclassesdedomínioébastantemo-
desta,comopodeservistanasequência:
abstract class Pessoa {
String nome
}
class PessoaFisica extends Pessoa {
String sobrenome
String cpf
}
class PessoaJuridica extends Pessoa {
String cnpj
}
Claro,vocêestácuriosoegostariadevercomoastabelasficariamno
bancodedados,entãoiráexecutarocomando run-appparaveroresul-
tado,certo?Porpadrão,semqualquerconfiguraç ãodemapeamentocusto-
mizado,oqueteremoséageraç ãodeumaúnicatabelachamada pessoa,
cujaestruturapodemosveraseguir:
167

## Página 174

5.10. Lidandocomherança CasadoCódigo
OHibernatetrabalhaessencialmentecomduasestratégiasaomapearhe-
rança:umatabelaporhierarquia,queéopadrão(table per hierarchy )ouuma
tabelaporclasse. Comopôdeservistonaimagem,todososatributosque
definimosnasclasses PessoaJuridicae PessoaFisicaencontram-se
armazenadosnamesmatabela.
Observequeumnovocampofoiadicionado, class,queseráusadopelo
GORMparafazerabuscaporpessoasdeacordocomotipodaclasse,fazendo
adiferenciaçãoentreostipos.
Omaisimportanteaserobservadonaestratégia“umatabelaporhie-
rarquia”équeatributosdefinidosnasclassesderivadasserãomapeadospara
camposqueobrigatoriamentedeverãoaceitar nullcomovalor. Entender
estecomportamentoéfácil. Imaginequeocampo cnpjnãoaceite null
comovalor.Naprimeirainser çãodeumapessoafísica,oSGBDlheretorna-
riaumerro.
Paradesabilitarocomportamentode“umatabelaporhierarquia”basta
adicionarumúnicocomandonobloco mappingdaclassequeseencontra
naraízdahierarquiadeheran ça( Pessoa)talcomonoexemplo:
class Pessoa {
String nome
static mapping = {
tablePerHierarchy false
}
}
Oresultadoéqueagorateremostrêstabelas: pessoa, pessoa_fisica
e pessoa_juridica.
168

## Página 175

CasadoCódigo Capítulo5. Domínioepersistência
Fig.5.17:Comportamentodaheran çanastabelas
Serãocriadaschavesestrangeirasrelacionandoocampo iddastabe-
las pessoa_fisicae pessoa_juridicacomocampo iddatabela
pessoa.
Bastantesimples,nãoémesmo?
5.11 C oncluindo
Nestecapítulofoiexpostocomdetalhescomofuncionaomapeamentode
classesdedomíniocomGrails.Aprendemoscomomodelarosrelacionamen-
tosentrenossasclassesdedomínio,comonossosatributossetransformam
emcamposnastabelaseaindaentendemoscomdetalhesoprocessodeper-
sistênciadosdados.
Estaéametadedocaminho.Agorairemosentendercomotirarproveito
dasdiferentestecnologiasdepesquisaeobten çãodedadosqueoGrailsnos
fornece. Eclaro:algumasarmadilhasaparecerãodiantedenós,masnãose
preocupepoistodasserãodesarmadasevocêaindaaprenderáatirarproveito
delas.
169

## Página 177

Capítulo6
Buscas
Nocapítulo5aprendemoscomdetalhescomomodelarnossasclassesdedo-
mínioemGrailsetambémpudemosnosaprofundarnomodocomoéfeito
oprocessodepersistênciadedadosemumbancodedadosrelacional.Neste
capítulo(queserábemmaisdinâmicoqueoanterior)vamosagoraentender
comoencontrarinformaçõesemnossobancodedados.
Grailsnosforneceumaamplagamadetecnologiasvoltadasàobten ção
dedados:
• Findersdinâmicos
• Criterias
• Buscaswhere
• HQL(HibernateQueryLanguage)

## Página 178

6.1. GrailsConsole:nossomelhoramigo CasadoCódigo
Entenderemosaquiqualoambienteidealparacadaumadestasalternati-
vaseaindaexporemosalgumasdicasquetornarãosuavidacomGrailsmuito
maisprodutiva.Claro,usaremoscomoreferênciaonossosistema ConCotque
desenvolvemosatéaqui.
E,sim,duranteopercursoiremosdesarmaralgumasarmadilhasquecos-
tumampregarsustosnosiniciantesedificilmentesãodescobertas.
6.1 G rails Console: nosso melhor amigo
Lembrado Groovy Console2.4?Aequiperesponsávelpelodesenvolvimento
doGrailsreaproveitouaideianoframework,oquenospossibilitaexperi-
mentarinstruçõescontraasclassesdanossaaplicaçãoetodososrecursosdo
GrailsexatamentecomofizemoscomcódigoGroovy.
Oconsoleéportantoumaferramenta essencialparaoaprendizadodo
framework,especialmenteaspossibilidadesdeconsultadoGORMdeque
iremostratarnestecapítulo.Parainiciaroconsolebastaexecutarocomando
consolenainterfacedelinhadecomandodoGrails. Naimagemaseguir
podemosveraexecuçãodeumaconsultasimplesusandofindersdinâmicos
(nossopróximoassunto)noconsole:
172

## Página 179

CasadoCódigo Capítulo6. Buscas
Fig.6.1:‘GrailsConsole’emação
Parafacilitarsuavidanestecapítulo,dadoquetodososexemplosserão
executadoscontraasclassesdo ConCot,sugerimosquesejaincluídaainstru-
çãodeimportaçãodepacotesexatamentecomonocódigoaseguir:
import concot.*
6.2 Finders dinâmicos
Oprimeirocontatocomosfindersdinâmicos(dynamic finders)doGORM
normalmentetambéméumdaquelesmomentosemqueentendemososga-
nhosqueumalinguagemdinâmicacomoGroovypodeoferecer. Detodas
asopçõesdepesquisaoferecidaspeloGrailséamaissimples,masnãopor
istoamenosusada,pelocontrário:nageraçãodeCRUDfeitapelorecursode
scaffoldingdoGrailséinclusiveoúnicomododeobten çãodedadosadotado.
Bom,mascomoquesepareceestacriatura?
173

## Página 180

6.2. Findersdinâmicos CasadoCódigo
Assimcomoosmétodosdepersistênciaquevimosnocapítulo 5como
save()e delete(),osfindersdinâmicosparecemmétodosestáticosin-
cluídosemnossasclassesdedomínio. Damesmaforma,estesnãoexistem
diretamentenocódigo-fonte,massãogeradosdinamicamenteduranteaexe-
cuçãodaaplicação. Comoveremos,oGORMiráinterpretaronomedos
métodosqueinvocamose,seguindoalgumasconven çõesqueveremosnesta
seção,vaiexecutarbuscasnonossobancodedadosencontrando(ounão)
aquiloquedesejamos.
Obtendo uma única instância
EmdiversoscontroladoresgeradospeloscaffoldingdoGrails,iremosen-
contrar actions(ações)similaresaocódigoaseguir:
def get(long id) {
Categoria categoriaInstance = Categoria.get(id)
}
Apenasparalembrar,adefiniçãodaclassededomínio Categoriaé
bastantesimplescomopodemosveraseguir:
class Categoria {
String nome
// constraints omitidas para simplificar
}
Quandoiniciado,oGORMiráautomaticamenteincluiralgunsmétodos
emtodasasnossasclassesdedomínioqueservemparaverificaraexistência
deumaentidadeouobterumainstânciasuausandocomoparâmetrodebusca
suachaveprimária/identificador.
Destesmétodos,omaisusadoéo get,querecebecomoparâmetroum
valorquedeverácorresponderaoidentificadordaclassededomínio. No
scriptaseguirpodemosverumexemplodeuso:
// Busca uma instância de Categoria com id 1
Categoria comId1 = Categoria.get(1)
Casooregistronãoexistanobancodedados, nullseráoresultadoda
invocaçãodestemétodo. Háaindamaisumaop çãointeressanteparaeste
174

## Página 181

CasadoCódigo Capítulo6. Buscas
tipodeconsulta.Estamosfalandodafun ção read,cujousoépraticamente
idênticoaodo getconformevemosnoexemploaseguir:
// Busca uma instância de Categoria com id 2
Categoria comId2 = Categoria.read(2)
Adiferençaentre get()e read()?Basicamente getnosapontauma
armadilhaquecostumaassustardiversosprogramadoresinexperientescom
ofuncionamentoessencialdoHibernate.
Fig.6.2:Aten çãoredobrada!
Nocapítulo5.7mencionamosrapidamenteoconceitodesessãodoHiber-
nate.Apenaspararelembrar,trata-sedeumcachelocal,definidoemescopo
dethreadquearmazenaoestadodetodasasnossasclassesdedomínio(ou
entidades,sevocêpreferir)paraquesejampersistidosnobancodedados.Na-
quelemomentofalamossobreoconceitode flush,noentantooquenãofoi
mencionadoéque o Hibernate pode persistir o estado dos nossos objetos
mesmo que não invoquemos o método save()..
Achaveparamelhorentendercomoistoocorreestánomomentoem
queainstânciadeumaclassededomíniovaipararnasessãodoHibernate.
Este“ir parar na sessão do Hibernate”temumnometécnico:seranexado(em
inglês,attached)àsessão.Umavezanexado,dizemosqueoHibernatepassaa
gerenciaroestadodesteobjeto,persistindo-onobancodedadosnomomento
emqueoscomandosSQLserãotransmitidosaoSGBD.Quandoumobjetoé
anexadoaumasessãodoHibernate?
• Aoobtermosoobjetoatravésdeumaconsulta.
• Sepersistimosoobjetousandoométodosave().
• Quandomanualmenteoincluímosnasessão.
175

## Página 182

6.2. Findersdinâmicos CasadoCódigo
Oquenosinteressaagoraéoprimeirocaso. Porpadrãoaoalterarmos
ovalordequalqueratributomapeadooobjetoserámarcadoparaqueseu
estadosejapersistidonobancodedados. Esabemoqueémaislegal? Por
padrão,istoocorreránomomentoemqueasessãoforfechada. Estecom-
portamentoébastantesutil,sendoassimnadamelhorqueumscriptsimples
parailustrá-lo:
import concot.*
Categoria comId1 = Categoria.get(1)
comId1.nome = "Nada pode dar errado"
Aosairdoescopodoscriptasessãoéfechadaeoflushocorre.Vocêdeve
ternotadoqueoatributofoialteradomasqueemmomentoalgumchamamos
ométodo save().Intuitivamente,podemospensarqueonomeanteriordo
registrosemanteve,porémexecutandoaconsultaaseguirnoMySQLnota-se
queestenãofoioresultadoesperado.
mysql> select * from categoria where id = 1;
+----+---------+----------------------+
| id | version | nome |
+----+---------+----------------------+
| 1 | 4 | Nada pode dar errado |
+----+---------+----------------------+
1 row in set (0.00 sec)
Estecomportamentodedetecçãodealteraçãodeestadoeeventualper-
sistênciadasmudançasnobancodedadostambémtemumnometécnico:
detecção de sujeira (dirt detection).Dizemosqueumobjetogerenciadopelo
Hibernateestá“sujo”quandoseuestadofoialteradoeaindanãofoipersis-
tidonobancodedados.Háinclusiveumafun çãoanexadaatodasasnossas
classesdedomíniochamada isDirty()queretorna truecasooobjeto
seencontrenesteestado.Noscriptaseguirpodemosverumexemplodesua
aplicação.
import concot.*
Categoria comId = Categoria.get(1)
176

## Página 183

CasadoCódigo Capítulo6. Buscas
println comId.isDirty() // imprimirá 'false', nada foi alterado ainda
comId.nome = "Outro nome"
println comId.isDirty() // imprimirá 'true', o estado foi alterado e ainda
Afunção read()narealidadeiráapenasdesabilitaradetecçãodesujeira
naobtençãodasentidades.Assim,oobjetosóserápersistidodefatonobanco
dedadosquandoexplicitamentechamarmosométodo save(). Podemos
verumexemplodesuaaplicaçãonoscriptaseguir:
import concot.*
Categoria comId = Categoria.read(1)
println comId.isDirty() // imprimirá 'false', pois a detecção de sujeira f
comId.nome = "Qualquer coisa"
println comId.isDirty() // imprimirá 'false', pois a detecção de sujeira f
Lembre-se: read()retornaoobjetosemdetecçãodesujeira,noentanto
vocêaindapoderáalteraroestadodoseuobjetoepersisti-loexecutandoo
método save()semproblemas.
Finalmente,nemsemprequeremosobterumainstância,massimapenas
saberseelaexiste. Nessescasosusamosafun ção exists(),querecebe
comoparâmetrooidentificadordaentidadeenosretornaráumvalorboole-
anoindicandoounãosuaexistência.Umexemplosimplesdesuaaplicaç ão
podeservistonoscriptaseguir:
/* Imagine que exista uma categoira com id = 1 */
println Categoria.exists(1) // imprimirá 'true'
/* Em nosso banco de dados imaginário não existem registros com identifica
println Categoria.exists(-1) // imprimirá 'false'
Listando registros
Umaoperaçãobastantecomumnaimplementaç ãodetodapáginade
CRUDéalistagemderegistros. Parafacilitarnossavida,oGORMinjeta
emtodasasclassesdedomínioafun ção list()cujousomaissimples,sem
qualquerparâmetro,retornatodasasentidadesarmazenadasemumatabela
talcomonoexemploaseguir:
177

## Página 184

6.2. Findersdinâmicos CasadoCódigo
import concot.*
Categoria.list() // retorna todas as categorias cadastradas
Claroque,conformeonúmerodeinstânciasaumente,nãoéinteressante
sempreretornartodososregistros. Sendoassimháalgunsparâmetrosque
podemospassarparaestafun çãoqueatornamperfeitaparaaimplementaç ão
detelasdelistagemnasquaisdesejemospaginarosdados. Seguealistade
parâmetros:
•max númeromáximodeinstânciasaserretornado.
•offset aposiçãoapartirdaqualositensdeverãoserlistados.
•orderseosregistrosdeverãovirordenadosemordemascendenteou
descendente. Aceitaapenasdoistiposdevalor: asce desc. Caso
nenhumsejafornecido,opadrãoé asc.
•sort qualoatributoqueseráusadonaordenaçãodasinstâncias.
•readOnly desabilitaachecagemdesujeira. Funcionaexatamente
comoafun ção read().Ovalorpadrãodestemétodoé false.
•fetchSize defineotamanhodo fetch,ouseja,emumnívelmais
baixo,quantosregistrosporvezodriverJDBCdeveráreceberdurante
aconsultaSQL.Muitoútilnocasodeotimizações.
•timeoutquantotempoemsegundosdeveráserlevadoemconsidera-
çãonapolíticadetimeoutdaconsulta.Comisto,casohajaumademora
excessivanaobten çãodasinstânciasumaexce çãoserádisparada.
Aseguirpodemosveralgunsexemplosdeaplicaç ãodafun ção list().
// obtendo todas as categorias
def todas = Categoria.list()
// obtendo apenas as dez primeiras instâncias
def primeiras10 = Categoria.list(max:10)
// obtendo apenas as dez primeiras instâncias
// ordenadas pelo nome em ordem descendente
178

## Página 185

CasadoCódigo Capítulo6. Buscas
def primeirasDezInvertidas = Categoria.list(max:10, sort:'nome', order:'de
// agora, aplicando o offset para obter a partir da posição 11
def primeirasDezInvertidas11 = Categoria.list(max:10, offset:11, sort:'nom
Expressões de método
Oaspectomaisinteressantedos findersdinâmicosquesãoasexpressões
demétodo(method expressions),quenospermiteescreverconsultasdeuma
formabastantesimplestirandomáximoproveitodanaturezadinâmicado
Groovy.TodainvocaçãodemétodoemumaclassededomínioGORMéantes
interceptada.Nesteato,onomedométodoaserexecutadoéanalisadoe,se
batercomalgumasregrasdefinidaspeloGORM,umanovaconsultaseráge-
radaeenviadaparaoSGBD.Aseguirpodemosverumexemplobemsimples
daaplicaçãodesteprincípioaobuscarmosporumainstânciade Categoria
cujoatributo nomeseja Materiais.
/*
Retornará, caso exista no banco de dados,
uma instância de Categoria cujo atributo
nome seja "Materiais"
*/
def categoriaMateriais = Categoria.findByNome("Materiais")
Toda method expression deve começar com o prefixofindBy ou
findAllBy,usadosrespectivamenteparaobtercomoresultadoapenasuma
ouumalistadeinstâncias.Seguidoaesteprefixoconcatena-seonomedoatri-
butosobreoqualseráfeitaaconsulta.Tambémpodemosaplicaroperadores
lógicosecomparadorescomoobjetivodecriarconsultasmaiscomplexas.Na
documentaçãooficialdoGrails[4]háumesquemadasintaxeaseraplicada
emuma method expressionqueiremosdissecaratéorestantedestase çãocom
umasériedeexemplosquepodemosveraseguir:
ClasseDominio.[findBy|findAllBy]([Propriedade][Comparador]?[Operador boole
([Propriedade][Comparador])
Queseinicieadissecação.Apropriedadedizrespeitoaonomedoatri-
butodaclassededomínioqueseráusadonaconfecç ãodaconsulta. Não
179

## Página 186

6.2. Findersdinâmicos CasadoCódigo
hámuitooqueserditoaseurespeito,apenasquedeveserdigitadonofor-
mato camel case,sempreselembrandodecolocaraprimeiraletradonome
emmaiúscula. Opróximoelementoquenosinteressaseráocomparador.
Nalistaaseguirpodemosveralistadoscomparadoresdisponibilizadospelo
GORM:
* InList encontra-senalistapassadacomoparâmetro.* LessThan
menorque.* LessThanEqualsmenorouiguala.* GreaterThanmaior
que.* GreaterThanEquals maiorouiguala.* Like equivaleao like
doSQL.Usadoparafazerbuscaporsimilaridade.* ILikesimilara ILike
sóquenãoé case sensitive. * NotEqual diferentede. * InRange
dentrodoslimitessuperioreinferiorfornecidos. * RLike usadoparaex-
pressõesregularessimilarao Regexp LIKE doMySQL.* Between entre
doisvalores.* IsNotNull valornãoénulo.* IsNull valorénulo.
Oleitordeveobservarquenalistagemdecomparadoresnãoháalgum
paraigualdade.Arazãoparaistoésimples:esteéocomparadorpadrãocaso
nenhumoutrosejadefinido.Vamostreinarumpouco?Aseguirestáalista
dealgumasconsultasquepodemosfazerapenascomcomparadores:
// A busca por igualdade de nome, que já conhecemos
Categoria.findByNome("Materiais")
// Busca todas as categorias com nome nulo
// apenas como exemplo (ignore as restrições que definimos para esta classe
Categoria.findAllByNomeIsNull()
// Agora, buscando todas as categorias que não
// possuam o nome nulo
Categoria.findAllByNomeIsNotNull()
Apenasparaquepossamostreinarcomoutroscomparadores,vamosnos
lembrardadefiniçãodaclasse Cotacao,quepodeservistanalistagema
seguir:
class Cotacao {
BigDecimal valor
Date data
180

## Página 187

CasadoCódigo Capítulo6. Buscas
static belongsTo = [ item:Item,
moeda:Moeda ,
fornecedor: Fornecedor]
}
Agoravamosfazermaisalgumasconsultas,apenasparatreinarusando
comparadoresnuméricos:
// Todas as cotações com valor maior que 1000
Cotacao.findAllByValorGreaterThan(1000)
// Usando between: cotações com valor entre 100 e 400
Cotacao.findAllByValorBetween(100,400)
Acreditoquecomestesexemplosoleitorjádeveterpegadopartedojeito
dacoisa.Échegadoomomentodepensarmosemconsultasumpoucomais
complexasusandooperadoreslógicos.Nocasodosfindersdinâmicoshádois:
•And operadore
•Or operadorou
Imaginequedesejemosbuscartodasascotaçõesquetenhamvalorsupe-
riora 1000 reais. Agorausaremosdoisatributoseooperadorlógico And.
Comoficaria?Oscriptaseguirnosdáumexemplo:
/* Primeiro buscamos a moeda "Real"
Repare que usei 'findBy' pois queremos apenas um registro */
def real = Moeda.findByNome("Real")
// Agora, finalmente, a consulta completa
def cotacoes = Cotacao.findAllByMoedaAndValorGreaterThan(moeda, 1000)
Ou,sequisermossimplificarumpouco:
def cotacoes = Cotacao.findAllByMoedaAndValorGreaterThan(
Moeda.findByNome('Real'), 1000)
Atençãoespecialdeveserdadaaocomparador like.Imaginequetente-
mosbuscartodasascategoriasquetenham“ter”nonomeeemnossobanco
dedadoshápelomenosumregistrocomovalor“Material”cadastrado. A
consultaaseguirretornariaumalistavazia:
181

## Página 188

6.2. Findersdinâmicos CasadoCódigo
Categoria.findAllByNomeLike("mat")
Issoporqueprecisamosusarocaractereespecial%paradenotaraexpres-
são,talcomonosexemplosaseguir:
//Todas as categorias que comecem com "Mat"
Categoria.findAllByNomeLike("Mat%")
//Todas as categorias cujo nome termine em "ial"
Categoria.findAllByNomeLike("%ial")
//E finalmente, todas as categorias que tenham "ate" no nome
Categoria.findAllByNomeLike("%ate%")
Claro,tambémpodemospaginarosresultados. Comofazerisso? Pas-
sandocomoúltimoparâmetroparaaconsultaumobjetodotipo Mapcujas
chavescorrespondamaosparâmetrosqueapresentamosnadescriçãodafun-
ção list()6.2.Aseguir,novamente,algunsexemplos:
// Buscando apenas os 10 primeiros registros na busca por
// categorias que tenham "a" no nome
Categoria.findAllByNomeLike("%a%", [max:10])
// Agora, com offset
Categoria.findAllByNomeLike("%a%", [max:10, offset:11])
Persistindo com finders dinâmicos
Vocêtambémpodeusarfindersdinâmicosparagerarnovosregistrosno
seubancodedadoscasonenhumainstânciasejaencontrada.Como?Usando
oprefixo findOrSaveByeexecutandosuaconsulta.Observeoexemploa
seguir:
def equipamentos = Categoria.findOrSaveByNome("Equipamentos")
Casonãoexistaumacategoriacomonome“Equipamentos”,emvezdere-
tornar nullométodo findOrSaveByirácriarumnovoregistronobanco
dedadosenosretornarumainstânciaquerepresenteaqueledadorecém-
criado.
182

## Página 189

CasadoCódigo Capítulo6. Buscas
Quando usar finders dinâmicos?
Findersdinâmicossãoamelhorop çãoquandoprecisamosescrevercon-
sultassimplesenvolvendoumnúmeropequenodeatributos(emminhaexpe-
riência,trêsnomáximo).Oleitordevelevaremconsideraçãotambémuma
limitaçãoimportantedesterecurso:todososatributosenvolvidosnaconsulta
obrigatoriamentedevemestarcontidosnaclassededomíniosobreaquales-
tamosexecutandoaconsulta.
Éfácilmostrarcomoumaconsultacomfindersdinâmicospodesemos-
trarproblemática. Bastatentarinterpretaraconsultaaseguircomquatro
atributos:
def real = Moeda.findByNome("Real")
def item = Item.get(4)
Cotacao.findAllByMoedaAndItemAndValorGreaterThanOrDataIsNull(moeda,item,10
Criteria
6.3 C riterias
Sefindersdinâmicossãoumaboaalternativaparaconsultassimples,as cri-
teriasnosoferecemumapoderosaferramentaquandoprecisamosescrever
consultasmaiscomplexasemumabasededadosrelacionale,aindamaisin-
teressante,fornecendoumfeedbackvisualaoprogramadorquefacilitabas-
tantealeituradocódigoqueescrevemos.
CasooleitorjátenhaalgumaexperiênciacomHibernateonomelhesoará
familiar.Nãoéparamenos:ascriteriasdoGORMsãonarealidadeumaDSL
queporbaixodospanosefetuachamadasàAPICriteriadoHibernate.Talvez
vocêestejacuriosoarespeitodaaparênciadesterecurso,sendoassim,sem
muitademora,eisummododeusá-lo:
import concot.*
def criteria = Categoria.createCriteria()
criteria.get {
183

## Página 190

6.3. Criterias CasadoCódigo
eq 'nome', 'Materiais'
}
Estescomparadorespodemtambémserescritosusandoparênteses,afinal
decontas,sãoapenasfun çõesGroovynormais:
import concot.*
def criteria = Categoria.createCriteria()
criteria.get {
eq('nome', 'Materiais')
}
Qualformausar?Trata-sedeumaquestãosimplesmenteestética.
Estaéaformamaisverbosadesecriarumacriteria.Elafoiescolhidaape-
nasporsermaisdidáticanestemomentoenosapresentarumasériedeaspec-
tossobreorecurso.Afun ção createCriteria()éinjetadapeloGORM
emtodasasclassesdedomíniodasuaaplicaç ãoe,quandochamada,nos
retornaumobjetodotipo grails.orm.HibernateCriteriaBuilder.
Reparenosufixo:sim,ascriteriassãoumaaplicaç ãodoconceitodebuilder
doGroovyquevimosnestelivroquandotratamosdalinguagem.
Porserumbuilder,aconstruçãodeconsultassetornaalgonaturaldado
ànaturezahierárquicaqueenvolvetodaexpressãodebusca. Aoexecutara
função getdanossacriteria,passamoscomoparâmetroumblocodecó-
digoqueconsistiránaDSLimplementadapelaequipededesenvolvimentodo
GORMqueexecutaráoscomandoscontraaAPICriteriadoHibernate.No
caso,estamosusandoocomparadordeigualdade( eq),quesemprereceberá
doisparâmetros:oprimeiroéonomedoatributosobreoqualmontaremos
aconsulta,eosegundoovalorusadonasele çãodosdados.
184

## Página 191

CasadoCódigo Capítulo6. Buscas
Criteria, critério ou critérios?
Aindanãoencontreiumatraduç ãosatisfatóriaparaestetermoem
português. Aliteralseria“Critérios”,oproblemaéquenapráticavocê
iráusarotermo“criteria”otempointeiro.Sendoassim,opteiporusar
umneologismofosseomaispróximopossíveldoseudiaadia:“criteria”
ou“criterias”.
Éclaroqueoúnicocomparadornãoéodeigualdade.Aseguirestáuma
listacomalgunsdosprincipaiscomparadoresprovidospeloGORMeque
usaremosemalgunsexercíciospráticoslogonasequência. Vocêpodeob-
terumalistacompletanadocumentaç ãooficialdoGrails[3].Éimportante
ressaltarquequasetodosapresentarãoomesmofuncionamento:oprimeiro
parâmetrocorrespondeaonomedoatributosobreoqualéfeitoabuscaeos
restantes,quandohá,referenciamosvaloresadotadosemnossaconsulta.
•between ovalordapropriedadeseencontraráentredoisvalores.
Exemplo: between(‘valor’, 10, 100)
•eq igualdade.Exemplo: eq(‘nome’, ‘Materiais’)
•eq (case insensitive) épossíveldesabilitarocasesensitivede
equals. Paratal,bastaincluirumparâmetroamaisnofinaldaexe-
cuçãocomonoexemploaseguir: eq(‘nome’, ‘materiais’,
[ignoreCase:true])
•ne diferentede.Exemplo: ne(‘nome’, ‘Materiais’)
•eqPropertyquandoovalordeumapropriedadedeveserigualaode
outra.Exemplo: eqProperty(‘sobrenome’, ‘nome’)
•nePropertyumapropriedadepossuivalordiferentedaoutra.Exem-
plo: neProperty(‘nome’, ‘sobrenome’)
•gt o valor deve ser maior que o parâmetro. Variações:gt
(maiorouigual), lt(menorque), lte(menorouigual)Exemplo:
gt(‘valor’, 1000)
185

## Página 192

6.3. Criterias CasadoCódigo
•gtProperty ovalordeumapropriedadedevesermaiorqueode
outrapropriedade. Variações: ltProperty(menorqueapropri-
edade), gteProperty(maiorouigualpropriedade), lte(menor
ouigualapropriedade). Exemplo: gtProperty(‘valorVenda’,
‘valorCompra’)
•idEq usado quando se deseja fazer uma busca por identificador.
Exemplo: idEq(1)
•ilike expressãodotipo likesóquecaseinsensitive. Exemplo:
ilike(‘nome’, ‘%a%’)
•in ovalordapropriedadedeveestarentreaquelespresentesemuma
lista. Atençãoaomodocomoodigitamos,pois inéumapalavrare-
servadadoGroovy. Exemplo: ‘in’(‘nome’, [’Materiais’,
‘Equipamentos’])
•isEmpty usado para buscar registros nos quais uma de suas
propriedades, do tipo lista (um hasMany) está vazia. Exemplo:
isEmpty(‘itens’)
•isNotEmpty oposto de isEmpty. Exemplo:
isNotEmpty(‘itens’)
•like instruçãodotipo like,exatamentecomovimosnocasodos
findersdinâmicos.Exemplo: like(‘nome’, ‘%a%’)
•sizeEq usadaquandoonúmerodeitensemumrelacionamentodo
tipo hasManyéigualaovalorpassadocomoparâmetro.Hávariações:
sizeGt(tamanhomaiorque), sizeGe(tamanhomaiorouigual),
sizeLt(tamanhomenorque), sizeLe(tamanhomenorouigual).
Exemplo: sizeEq(‘itens’, 3)
•sqlRestriction falaremos com mais detalhes sobre este
item mais tarde. Basicamente ele nos possibilita enrique-
cer nossas consultas com instruções SQL nativas. Exemplo:
sqlRestriction("char_length(nome) < 30")
186

## Página 193

CasadoCódigo Capítulo6. Buscas
Pelalistadecomparadoresficanítidoopoderdascriteriaseoquãomais
avançadoéesterecursoemrelaçãoaosfindersdinâmicosquevimosagora
hápouco.Assimcomofizemosnaquelecaso,vamosnovamentenosexercitar
umpoucocomalgumasconsultasbemsimplesporenquanto,masantes,é
importantemostrarumaoutraformadesedeclararcriterias.Umamaneira
bemmaissimples,talcomopodemosveraseguir:
def categorias = Categoria.withCriteria {
}
Afunção withCriteriajácriaumacriteriaparanóseretornaalista
deresultados.Senãoincluirmosnenhumainstruç ãonadefiniçãodaconsulta
oresultadoserátodasasinstânciasdaclassededomínio.Háoutrasformas
também:
def criteria = Categoria.createCriteria()
// obtendo uma lista com o resultado
criteria.list {
}
// obtendo uma lista com ainda menos código
criteria {
}
/*
E se quisermos obter apenas um item na
nossa consulta? Simples. :)
Se a consulta retornar mais de um item como
resultado, um erro será disparado, sendo assim
cuidado na escrita do seu código.
*/
criteria.get {
eq 'nome', 'Materiais'
}
187

## Página 194

6.3. Criterias CasadoCódigo
Qualformausarficaporcontadasuacomodidade.Maisàfrentequando
formosfalardecriteriasdesanexadasveremoscomoreaproveitarnossascon-
sultas.Apenasparatreinarumpouco,aseguirpodemosvermaisumexemplo
deconsultaenvolvendotrêsatributosnaclasse Cotacao.
import concot.*
/*
com mais de um atributo
Todas as cotações feitas nos últimos 10 dias
e com valor maior ou igual a 1000, que não
tenham o atributo fornecedor nulo mas que
tenham a moeda nula
*/
def cotacoes = Cotacao .withCriteria {
le 'data', new Date() - 10
ge 'valor', 1000
isNotNull 'fornecedor'
isNull 'moeda'
}
Consultando associações
OsatributosdeumaconsultaCriterianãoprecisamsertodosdamesma
classededomínio.Imaginequedesejemosbuscartodasascotaçõescomva-
lorsuperioraR$ 1000,00.Usandofindersdinâmicosprecisaríamosdeduas
consultas,comcriterias,apenasumacomopodemosveradiante:
def cotacoes = Cotacao .withCriteria {
gt 'valor', 1000
moeda {
eq 'nome', 'Real'
}
}
Bastacriarmosumnovoblocodentrodacriteriaquepossuaomesmo
nomequeaassociaçãopresenteemnossaclassededomínio.Aestruturahie-
rárquicanaqualescrevemosnossocódigoinclusiveajudaatornarmaisfácil
deentenderaquiloquedesejamos. Apenasparatreinarumpouco,quetal
188

## Página 195

CasadoCódigo Capítulo6. Buscas
buscartodasascotaçõescomvalorsuperioraR$ 1000,00ecujositenscota-
dossejampertencentesàcategoria Materiais?
def cotacoes = Cotacao.withCriteria {
gt 'valor', 1000
moeda {
eq 'nome', 'Real'
}
item {
categoria {
eq 'nome', 'Materiais'
}
}
}
Conjunções, disjunç ões e negaç ões
Todasasconsultasquevimosatéestemomentoforamsimplesconjun-
ções.Aoexecutarmosumaconsultacomoaseguir:
def cotacoes = Cotacao.withCriteria {
gt 'valor', 1000
moeda {
eq 'nome', 'Real'
}
}
Na realidade estamos executando algo comotodas as cotações
com valor maior que 1000 **E** cuja moeda tenha como
nome ‘Real’. Agrandequestãoé: comousarumadisjun ção(ofamoso
“ou”)?Destemodo:
def cotacoes = Cotacao.withCriteria {
or {
gt 'valor', 1000
lt 'valor', 100
}
}
Assimobtivemostodasascotaçõescujovalorsejasuperiora1000ouin-
feriora100.Podemosusaradisjun çãodeformaexplícitatambém:
189

## Página 196

6.3. Criterias CasadoCódigo
def cotacoes = Cotacao .withCriteria {
and {
gt 'valor', 1000
moeda {
eq 'nome', 'Real'
}
}
}
Parafinalizar,tambémpodemosexecutarumanegaç ão. Imagineque
queremosnegarumblocointeirodentrodeumacriteria.Paratalbastausar
anegaçãocomonoexemploaseguir:
def cotacoes = Cotacao .withCriteria {
not {
gt 'valor', 1000
moeda {
eq 'nome', 'Real'
}
}
}
Nosúltimostrêsúltimosexemplosacreditoquetenhafortalecidoainda
maisasuaimpressãodequecomcriteriastemos,semsombradedúvidas,
umadasformasmaispoderosaseflexíveisparaescrevernossasconsultas.
Muitomelhorqueaconcatenaçãodestringsquenãoraroaparecememnos-
sossistemas,nãoémesmo?
Usando restrições SQL
Sempresurgemsituaçõesnasquaispoderíamosescrevernossasconsultas
deumaformamaissimplessepudéssemosacessaracamadainferiordoORM,
ouseja,seconseguíssemostirarproveitodoSQLexecutadopeloSGBD.Cri-
teriasnospermitemissograçasaocomparador sqlRestriction.
Éumcomparadorbastantesimplespoissórequerumparâmetro:ains-
truçãoSQLqueusaremosparafiltraroresultado.Imaginequesejadonosso
interessebuscarapenasascategoriascujonomepossuaquatrocaracteres.
Comofaríamosisto?Assim:
190

## Página 197

CasadoCódigo Capítulo6. Buscas
def categorias = Categoria.withCriteria {
sqlRestriction 'char_length(nome) = 4'
}
Oúnicopontoqueoleitordevelevaremconsideraç ãoéofatodeque
muitasvezesiráusarinstruçõesespecíficasdeumSGBD(noexemplo,usei
umainstruçãodoMySQL)quepodemnãoestarpresentesemoutrassoluções
domercado.
Projeções
Seformosbuscarporumadefiniçãodeproje çõesnocontextodoHiber-
nateencontraremosfrasescomo “são um recurso usado para customizar o re-
sultado de uma consulta
.Agrandequestãoé:customizarcomo?Naverdade,aplicamosproje ções
quandodesejamosqueoresultadodanossaconsultanãosejasimplesmente
umalistadeinstâncias,massimumalistadetuplascontendoatributosda
nossaclassededomínioouoresultadodeexpressõescomosoma,médiae
outras.Confuso?Vamosaalgunsexemplos.
Imaginequedesejamossaberqualasomadovalordetodasascotações
quevalhammaisqueR$ 1000,00.Comovocêfaria?Assim:
def criteria = Cotacao.createCriteria()
criteria.get {
gt 'valor', 1000
moeda {
eq 'nome', 'Real'
}
projections {
sum 'valor'
}
}
// será retornado um valor numérico apenas.
Seobloco projectionsestivercontidoemumacriteriaovalorretor-
nadodeixadeserumalistadeinstânciasdaclassededomínioepassaaser
191

## Página 198

6.3. Criterias CasadoCódigo
umalistadelistas.Cadaumadaslistasretornadasconteráemseuinterioras
projeçõesquedefinimosnobloco projections.Casouseafun ção gete
alistacontenhaapenasumalistacomumúnicovalornesta,seráretornado
apenasaqueleitem.
Voltando,imaginequenãoprecisemosdacotaçãointeira,massimapenas
deseuidentificadorevalor.Comofaríamos?
def criteria = Cotacao .createCriteria()
criteria {
gt 'valor', 1000
moeda {
eq 'nome', 'Real'
}
projections {
property 'id'
property 'valor'
}
}
// Exemplo de retorno:
// [[1, 1000], [2, 1010], [3, 4030.40]]
Ainstrução property,querecebecomoparâmetroonomedoatributo
presenteemnossaclassededomínio,determinaqueiremosretornarapenas
oconjuntodepropriedadesquedefinimosnasproje ções.Aseguirestáuma
listadeproje çõesparaqueoleitorpossaterumaideiadopoderdesterecurso.
Umalistacompletapodeserencontradanadocumentaç ãooficialdoGrails
[3].
•property Retornaapropriedadedaclasseemquefoiexecutadaa
consulta.Exemplo: property(‘nome’)
•distinct Retornaapenasvaloresdistintos,talcomoainstruç ãode
mesmonomequeusamosnoSQL.Exemplo: distinct(‘valor’)
•avg Amédiadosvaloresdeumacoluna.Exemplo: avg(‘valor’).
192

## Página 199

CasadoCódigo Capítulo6. Buscas
•sum A soma dos valores presentes em uma coluna. Exemplo:
sum(‘valor’).
Como minimizar o consumo de memória quando uma critéria nos
retorna um número significativo de instâncias
Nofuturo,osistema ConCotviusuabasededadoscrescersignificativa-
mente. Imaginequeumdiaalguémquisessevertodasascotaçõesdeitens
cujonomecontenhaaletra“a”,masabasededadosjácontacombilhões de
registros.Comovocêfaria?Vocêusaria scrollable results!
Scrollable Resultssãoumafuncionalidadebastanteinteressantecontida
noHibernateparalidarcomesteproblema.Essencialmente,aoinvésdeuma
criterianosretornarumalistacomtodosositens,elairánosretornarum
iterador(objetodotipo ScrollableResults)quenospermitenavegarentreos
registros.Podemosvercomotirarproveitodestafuncionalidadenalistagem
aseguir:
def criteria = Cotacao.createCriteria()
def scroll = criteria .scroll {
item {
like 'nome', '%a%'
}
}
while (scroll.next()) {
// vou lendo uma instância por vez e não todas!
def cotacao = scroll .get()
}
Osseguintesmétodosencontram-sedisponíveisnesteobjeto:
•next() obtémopróximoitemdoiteradoremoveparaopróximo.
Retorna truecasosejapossívelfazerestamovimentação.
•first() moveparaoprimeiroregistro.
•last() moveparaoúltimoregistro.
•get() retornaainstânciacorrente.
193

## Página 200

6.3. Criterias CasadoCódigo
•isLast() retorna truecasoestejamosnaúltimainstânciadoitera-
dor.
Uma lista completa pode dos métodos presentes na classe
ScrollableResults pode ser obtida na documentação oficial do
Hibernate[9].
Fig.6.3:Aten çãoredobrada!
MuitaatençãocomodriverConnector/JdoMySQL:nemsempreelefun-
cionacomogostaríamos.SegundoaAPIJDBC,osdadosdeveriamserenvi-
adosparaoclientesomentequandoaomovimentarmosocursorencontrás-
semosummomentonoqualtivéssemoschegadoaofimdalista,certo?Infe-
lizmente,oConnector/Japenasemulaestecomportamento,trazendoparao
clientetodososdadosparaamemória.
CasoestejausandooMySQL,verifiqueadocumentaç ãoatualdodriver
JDBCeconsulteestepost[29]noStackOverflow.
Criando criterias em tempo de execução
Umavantagemdousodecriteriaséofatodepodemoscriá-lasdinami-
camente. Lembre-sequeoquepassamosnaconstruç ãodeumaconsultaé
narealidadecódigoGroovy.Sendoassim,nadaimpedequepossamosmon-
tarnossasconsultasemtempodeexecuç ão. Umexemplosimples:imagine
queno ConCotimplementamosumafun çãoquedefinesedevemosbuscar
cotaçõesporumamoedaespecíficaounão:
def buscarCotacoes(String nomeMoeda, BigDecimal valor) {
Cotacao.withCriteria {
eq 'valor', valor
//Você pode incluir um if na construção de uma criteria
if (nomeMoeda) {
194

## Página 201

CasadoCódigo Capítulo6. Buscas
moeda {
eq 'nome', nomeMoeda
}
}
}
}
Narealidade,épossívelusarqualquerestruturadecontroledefluxoGro-
ovynadefiniçãodeumacriteria,oquetornaaspossibilidadespraticamente
infinitas.Aseguirpodemosverumoutroexemplousandoo switch:
def buscarCotacoes(int tipoItem, BigDecimal valor) {
Cotacao.withCriteria {
eq 'valor', valor
// Usando switch para o mesmo fim
switch (tipoItem) {
case 1:
item {
categoria {
eq 'nome', 'Materiais'
}
}
break
case 2:
item {
categoria {
eq 'nome', 'Equipamentos'
}
}
break;
default:
isNull 'item'
}
}
}
Paraentenderavantagemdesterecurso,oleitordeveselembrarcomo
seriaoprocedimentoparaseobteromesmoresultadousandoconsultasSQL
nativas:nessescasosénecessáriaaconcatenaçãodestrings,oqueresultaem
195

## Página 202

6.3. Criterias CasadoCódigo
códigomuitomaiscomplexoepropensoaerros.
Criterias desconectadas
Criteriasdesconectadas(detached criteria)nospossibilitamreaproveitar
consultasdeumaformabastanteinteressante. Aprincipaldiferen çaentre
estaseacriteriaconvencionaléofatodenãoestarassociadaanenhumasessão
doHibernate.
Criaruma Detached Criteriaésimples,bastaexecutarinstruçõessimilares
àexpostaaseguir:
import concot.*
import grails.gorm.DetachedCriteria // obrigatório
def criteria = new DetachedCriteria(Cotacao).build {
moeda {
eq 'nome', 'Real'
}
gt 'valor', 1000
}
Oconstrutordalistagemrecebecomoparâmetroumaclassededomínio
gerenciadapeloGORM,enquantoométodo buildcriaráacriteriaparanós.
Aosercriadanenhuma,consultaseráexecutada,apenasteremosoobjeto
prontoparaquepossaserreaproveitadoemoutrospontosdosistema.
Ecomoexecutamosumacriteriadesanexada? Executandoosmesmos
métodos liste getquevimosanteriormente:
import concot.*
import grails.gorm.DetachedCriteria // obrigatório
def criteria = new DetachedCriteria(Cotacao).build {
moeda {
eq 'nome', 'Real'
}
gt 'valor', 1000
}
196

## Página 203

CasadoCódigo Capítulo6. Buscas
//obtem a lista de cotações
def resultado = criteria.list()
Composição de criterias com Criterias Desconectadas
Muitasvezesvocêseveráescrevendorepetidasvezesomesmotrechoem
diferentesconsultasemseusistema.Nessescasos,criteriasdesconectadaspo-
demlheajudaraobterumamelhorcomponentizaç ão. Paratal,segueum
exemplopráticono ConCot.Sempreprecisamosbuscarcotaçõesqueestejam
emReais. Sendoassim,nadamaisnaturalquecriemosumacriteriadesco-
nectadaparaisto.
def buscaCotacaoEmReais = new DetachedCriteria(Cotacao).build {
moeda {
eq 'nome', 'Real'
}
}
Aconsultafoicriadaeestáprontaagoraparaserreaproveitada,talcomo
noexemploaseguir:
def cotacoesCaras = Cotacao.withCriteria {
buscaCotacaoEmReais //olha aqui a criteria desconectada :)
gt 'valor', 1000000
}
Aoserexecutado,ocódigonarealidadevaicorresponderaoseguinte:
def cotacoesCaras = Cotacao.withCriteria {
moeda {
eq 'nome', 'Real'
}
gt 'valor', 1000000
}
Processamento múltiplos registros com criterias desconectadas
Épossívelalterarmúltiplosregistrosdeumaúnicavezusandocrite-
riasdesconectadas. Paratal,bastausarmosasinstruções updateAllou
197

## Página 204

6.3. Criterias CasadoCódigo
deleteAlldestesobjetospara,respectivamente,editarouexcluiremmassa
umagamaderegistros.
Doisexemplosilustrambemessafuncionalidade:primeiro,vamoseditar
ovalordetodasascotaçõesparazerocasosuacategoriaseja“Gratuito”. A
seguirpodemosvercomoistoéfeito:
def criteriaCotacoes = new DetachedCriteria(Cotacao).build {
item {
categoria {
eq 'nome', 'Gratuito'
}
}
}
criteriaCotacoes.updateAll([valor:0])
Aométodo updateAllfornecemosumobjetodotipo Mapnoqualas
chavescorrespondamaonomedoatributodaclassededomínioasermodi-
ficadoeovalor,aquelequedesejamospersistirnobancodedados.
Paraexcluirtodosositensgratuitoséigualmentesimplescomovemosa
seguir:
def criteriaCotacoes = new DetachedCriteria(Cotacao).build {
item {
categoria {
eq 'nome', 'Gratuito'
}
}
}
// Sem itens gratuitos daqui pra frente. :)
criteriaCotacoes.deleteAll()
Paginação e ordenaç ão com criterias
Paginaçãoderesultadoscomcriteriasébastantesimples. Bastausaras
expressõesaseguirnoblocodasuaconsulta:
•maxResults(int) definequantasinstânciasserãoretornadaspela
criteria.
198

## Página 205

CasadoCódigo Capítulo6. Buscas
•firstResult(int)apartirdequalposiçãoosdadosserãoexpostos.
Alistagemaseguirexpõeumbomexemplodecomousaressasinstru-
ções:
/* Buscará 10 instâncias a partir da posição 11 */
def moedas = Moeda.withCriteria {
maxResults (10)
firstResult(11)
}
Ordenaçãoémuitoparecidacomoquevimosnosfindersdinâmicos.
Bastausarainstrução order,querecebedoisparâmetros.Oprimeirocor-
respondeaonomedoatributosobreoqualseráfeitaaordenaç ãoeosegundo
seseráemordemcrescente( asc)oudescendente( desc).Oexemploase-
guirexpõeousodainstruç ão:
/* Buscará 10 instâncias a partir da posição 11
ordenadas pelo nome em ordem decrescente */
def moedas = Moeda.withCriteria {
maxResults (10)
firstResult(11)
order('nome', 'desc')
}
Quando uso criterias?
Comoditonoiníciodestase ção,optepelousodecriteriassempreque
precisarescreverconsultasmaiscomplexasecujalegibilidadeécomprome-
tidaquandoescritaeminstruçõesSQL,HQL.
Seforobservadoquesempreérepetidoomesmotrechoemdiferentes
consultas,criteriastambémcaemcomoumaluva,poisevitamanecessidade
deconcatenaçãodestrings,quenormalmentedãoorigemacódigodealtís-
simacomplexidadeemuitopropensosaerros.
Além disso, como observado, são também uma excelente ferramenta
quandoprecisamosfazeraediçãoouexclusãodemúltiplosregistrosemnossa
basededadosdeumamaneirasimples.
199

## Página 206

6.4. Buscasporwhere(wherequeries) CasadoCódigo
6.4 B uscas por where (where queries)
Aoinseriremnaversão2.0doGrailsascriteriasdesconectadasaequipedede-
senvolvimentonãoestavaapenasbuscandoumamaneiramaisinteressantede
componentizaçãodeconsultas:queriamnarealidadeumanovaferramenta
depesquisaquetivesseomesmopoderqueascriteriasmascomumasintaxe
maispróximadoGroovy.Sim,estoufalandodasbuscaspor where.
Amelhorformadeapresentarasbuscaspor whereécomparando-as
comacriteria.Nalistagemaseguirpodemosveradiferen çadeformanítida:
// A versão criteria de uma consulta que já usamos bastante
// neste capítulo
Cotacao.withCriteria {
gt 'valor', 1000
moeda {
eq 'nome', 'Real'
}
}
// E a versão por where
Cotacao.findAll {
moeda.nome == 'Real' && valor > 1000
}
Buscaspor wherenosoferecemumaalternativamaisflexívelqueosfin-
dersdinâmicosebemmenosverbosaqueacriteria sem que tenhamos qual-
quer tipo de comprometimento.Antesdenosaprofundarmosnoassuntoé
importanteprimeiroentender por que o nome where queries.
Cotacao.where {
moeda.nome == 'Real' && valor > 1000
}
Afunção whereanexadaatodasasclassesdedomíniopeloGORMre-
cebecomoparâmetroumblocodecódigonoqualdigitamosnossaconsulta
comcódigoGroovyenosretornaumacriteriadesconectada. Sendoassim,
todasasfun çõesquevimosseremusadasparaatualizaçãoemmassadedados
( updateAlle deleteAll)escrollableresults( scroll)tambémpodem
serexecutadascontraesteobjeto.
200

## Página 207

CasadoCódigo Capítulo6. Buscas
Escrevendo consultas
SevocêconsegueescreverumaexpressãobooleanaemGroovybaseada
nosatributosdasnossasclassesdedomíniojásabecomousarasbuscaspor
where. Vamoscomeçarporalgumasconsultassimples,quejávimosaqui
escritascomcriterias,agorausando where.
// Buscando a moeda Real
Moeda.find {
nome == 'Real'
}
// Buscando agora as cotações com valor maior
// que 1000 reais
Cotacao.findAll {
moeda.nome == 'Real' && valor > 1000
}
Enquantoafunção wherenosretornaumacriteriadesconectadaquenão
executaconsultaalgumanaquelemomento(estecomportamentoéchamado
lazy),asfun ções finde findAllretornam,respectivamente,umúnico
resultadoouumalista.Claroquepodemosusarconjun ções(and)edisjun-
ções(or)emnossasconsultas.Paratal,bastaagruparmososcomponentesda
consultausandoalgofamiliaranós:parênteses.
// Usando conjunção
// Moeda = Real E valor > 1000
Cotacao.findAll {
(moeda.nome == 'Real') && (valor > 1000)
}
// Usando uma disjunção
// Com valores maior que 1000 ou menores que 100
Cotacao.findAll {
(valor < 100) || (valor > 1000)
}
// Misturando disjunções e conjunções
Cotacao.findAll {
(moeda.nome == 'Real') && ( (valor < 100) || (valor > 1000) )
201

## Página 208

6.4. Buscasporwhere(wherequeries) CasadoCódigo
}
// Se quiser, também pode usar os métodos da
// criteria desconectada. Lembra deles?
def consulta = Cotacao .where {
(moeda.nome == 'Real') && (valor > 1000)
}
def resultado = consulta.list(sort:'valor')
Nãoseesque çatambémdanegação.Sequisermostodasascotaçõesque
nãoforamfeitasemRealescreveríamosalgocomo:
def tudoMenosReal = Cotacao.findAll {
! (moeda.nome == 'Real')
}
Comopodeservisto,temosumaDSLextremamentenaturalaoprogra-
mador:umaquevocêjáconhece.Penseemumaexpressãobooleana,escreva-
aepronto:suaconsultaestápronta.Ecomovocêlidacomrelacionamentos?
Aprimeirapartevocêjáviu,lembra?
Cotacao.findAll {
moeda.nome == 'Real'
}
Bastaquevocêreferencieonomedaassociaçãonasuaconsultaepronto!
Osoperadoresdecomparaçãotambémfuncionamexatamentecomovocêes-
perariaquesecomportassememGroovy: ==(igual), !=(diferente), >
(maior), >=(maiorouigual), <(menor), <=(menorouigual). Mashá
algunsquenãosãotãointuitivos:trêsapenas.
•in ovalorseencontradentrodeumalista
•==~ likecasesensitive
•=~ likecaseinsensitive
// Todas as moedas que contenham e no nome.
// Retornará o 'Real'
202

## Página 209

CasadoCódigo Capítulo6. Buscas
Moeda.findAll {
nome ==~ "%e%"
}
//Todas as moedas cujo nome seja 'Real' ou 'Dolar'
Moeda.findAll {
nome in ['Real', 'Dolar']
}
Étambémpossívelescreverconsultascomooperador between.Como?
Usando rangescomonoexemploaseguir:
// Todas as cotações com valor entre 100 e 1000
Moeda.findAll {
valor in 100..1000
}
Nulidade?Fáciltambém.Bastacompararoatributocom null.
// Todas as cotações que não tenham fornecedor
Cotacao.findAll {
fornecedor == null
}
Ecomparaçãoentrepropriedades?
// Todos os itens com valor de compra igual ao de venda
Cotacao.findAll {
valorCompra == valorVenda
}
Tambémpodemosexecutarcomparaçõesrelacionadasaotamanhode
umaassociaçãodotipo hasManytalcomoaseguir:
// todas as categorias que tenham mais de 0 itens
// associados
def itens = Categoria .findAll {
itens.size() > 0
}
203

## Página 210

6.4. Buscasporwhere(wherequeries) CasadoCódigo
Consultas compostas
Senofundoumabusca whereéumacriteriadesconectada,nadaimpede
quetambémpossamostirarproveitodaquelacomponentizaç ãoquevimos
antes.Como?
// A consulta por moeda 'Real'
def buscaReal = Cotacao.where {
moeda.nome = 'Real'
}
// Compondo a consulta, agora por valor
def buscaValor = consultaReal.where {
valor > 1000
}
def resultado = buscaValor.list()
[code]
A segunda consulta é como se tivéssemos escrito
[code groovy]
def buscaValor = Cotacao.where {
moeda.nome == 'Real' && valor > 1000
}
Subconsultas
Nãoháprojeçõesemconsultas where,masháalgointeressantequeentra
emseulugar:sãoassubconsultas,quenospermitemescreverconsultascom
umgraumaiordeinteligênciaatravésdainclusãodefun çõesespeciaisdentro
deumaconsulta where.Paramelhorentenderesterecurso,vamoslistarestas
funções:
•avg retornaovalormédiodetodosositensemumaconsulta.
•sum retornaasomadovalordetodosositensnaconsulta.
•max retornaovalormáximodoatributonatabela.
204

## Página 211

CasadoCódigo Capítulo6. Buscas
•min retornaovalormínimonatabela.
•count quantositensestãonatabelaouconsulta.
•property retornaumapropriedadeapartirdalistadepropriedades.
Seeuquisersaberquaisascotaçõescujovalorsejamaiorqueamédia,
comofaço?Assim:
def cotacoes = Cotacao.findAll {
valor > avg(valor )
}
Etambémpodemosaplicaressasfun çõesasubconsultas. Porexemplo:
sequiséssemosqueaconsultaanteriorfosseaplicadaapenasaositenscuja
moedaéoReal.Paraisso,usaríamosométodo of,querecebecomovalor
umaoutraconsulta.
def cotacoes = Cotacao.findAll {
valor > avg(valor ).of {moeda.nome == 'Real'}
}
Hátambémalgumasfunçõesquevocêpodeusaremsuasconsultasque
sãomuitoúteis:
•second Retornaapenasosegundodapropriedadecasoelasejado
tipo Date.
•minuteRetornaapenasominutodeumapropriedadedotipo Date.
•hour Ahoradeumapropriedadedotipo Date.
•day Odiadeumapropriedadedotipo Date.
•month Omêsdapropriedadedotipo Date.
•year Oanodeumapropriedadedotipo Date.
•upper Converteovalordapropriedadeparaletrasmaiúsculas.
•lower Converteovalordapropriedadeparaletrasminúsculas.
205

## Página 212

6.5. HQL CasadoCódigo
•trim Removeocaracteredeespaçodoinícioedofimdeumastring.
•length Retornaotamanhodeumapropriedadedotipostring.
Com estas funções podemos escrever consultas interessantes. Talvez
comonafun çãoaseguir,quemeretornarátodasasminhascotaçõesdoano
passadocomoparâmetrodentrodeumdadointervalodevaloresparauma
moedacujonometambémserápassadocomoparâmetro:
def buscarCotacoes(String nMoeda, int ano, BigDecimal valorMinimo, BigDecim
Cotacao.findAll {
(year(data ) == ano) &&
(valor in (valorMinimo)..(valorMaximo)) &&
(lower(moeda.nome) == nMoeda.toLowerCase())
}
}
Quando uso buscas por where?
Comoditonoiníciodestase ção,buscaspor whereficamentrecrite-
riaefindersdinâmicos.Sãoumaexcelenteop çãodevidoàsualegibilidade,
porémcomoumapequenalimitação:nãopossuemproje ções.Sendoassim,
casoprojeçõessejamumrequisitoparaseucódigo,criteriassoamcomouma
melhoropção.
6.5 HQL
TalvezaopçãomaisflexívelorientadaaobjetosqueoGORMnosofereceseja
osuporteaHQL(Hibernate Query Language),umalinguagempoderosíssima
adotadapeloHibernatequepossuiumavantagembastanteinteressante: é
bastanteparecidacomSQL.SevocêaindanãoconheceHQL,masjápossui
algumaexperiênciacomSQL,pode-sedizerque,agrossomodo,emvezdeli-
darmoscomtabelasecolunasmanipularemosrespectivamenteobjetosesuas
propriedades.
Issonãoquerdizerquesejaumalinguagemdefácilaprendizado:neste
livroiremosapenasexporofundamentalparaquevocêpossacome çarati-
rarproveitodestatecnologia. Paraaprendê-laemprofundidade(oquere-
206

## Página 213

CasadoCódigo Capítulo6. Buscas
comendo),sugiroaleituradadocumentaç ãooficialdoHibernate[8]queé
bastanteinteressante.
Executando HQL
Em cada classe de domínio do seu projeto o GORM irá inserir dois
métodosparaquepossamosexecutarconsultasusandoHQL: findAlle
findque,respectivamente,nosretornamumalistadeobjetosouapenasum
(quandosuaconsultaforescritadetalformaqueapenasumitemsejare-
tornado). Hádiversasassinaturasparaestemétodo,masaprincipalrecebe
apenasumparâmetro,nossaconsulta,talcomoexpostoaseguir:
// Todas as categorias que tenham a letra A no nome
Categoria.findAll("from Categoria c where c.nome like '%a%'")
// A categoria cujo id é 1
Categoria.find("from Categoria c where c.id = 1")
SevocênuncatrabalhoucomHQLmasjáviuSQL,nãoseassustecom
aausênciadapalavra-chave select.Falaremosmaissobreelamaistarde.
Reparequeestamosdandoum alias(apelido)àentidade Categoriaape-
nasparafacilitaradigitaç ãodasinstruções. Aoinvésderepetirapalavra
Categoria,porquenãosimplificardigitandoapenas c?Claro,oaliaséopci-
onalquandoemnossaconsultasóreferenciamosumaentidade.Sendoassim,
asconsultasaseguirsãoigualmenteválidas:
// Todas as categorias que tenham a letra A no nome
Categoria.findAll("from Categoria where nome like '%a%'")
// A categoria cujo id é 1
Categoria.find("from Categoria where id = 1")
Tambémpodemosparametrizarnossasconsultas. Afinaldecontasnão
éinteressanteficarconcatenandostringsquandoqueremosvariarosvalores
usadosemnossaspesquisas,nãoémesmo?Vejamosalgunsexemplos.Pri-
meiro,comparâmetrosposicionais,comonoexemploaseguir:
import concot.*
207

## Página 214

6.5. HQL CasadoCódigo
Categoria.findAll("from Categoria where id = ?", [1l])
Ocaractere ?representaumparâmetro.Aformamaisprimitivadepas-
sarmosparâmetrosparanossasconsultassedácomonoexemploanterior.
Nósosfornecemosnointeriordeumalistanamesmaordememqueapare-
cemnotextodenossaconsulta.Éoquechamamosde parâmetros posicionais.
Asegundaforma,emaisinteressantesãoos parâmetros nomeados:
import concot.*
Categoria.findAll("from Categoria where id = :id", [ id:1l])
Adiferençaéqueagora,casooparâmetroserepitaemnossaconsulta,
comonocódigoadiante,nãoprecisamosfornecerovalorduasoumaisvezes,
massimapenasuma.
import concot.*
/*
Todos os itens cujo nome contenha em si
o mesmo nome que sua categoria.
(uma busca tola, apenas para fins didáticos)
*/
Item.findAll("from Item i where i.nome like '%:nome%' and \
i.categoria.nome = :nome", [nome:'Material'])
Apropósito,stringsdemúltiplaslinhasdoGroovynãofuncionamcom
HQL,sendoassim,casoqueiramostirarproveitodelasparafacilitaraleitura
donossocódigo,precisamosdigitá-lastalcomonoexemploanterior.Aliás,
nestemesmoexemploaprendemostambémaescreverconsultasquelidem
comassociações. Reparoucomoreferenciamosorelacionamento categoria
(dotipo belongsTo)daclasse Item?
Paginação e ordenaç ão
PaginarconsultasHQLéexatamentecomofizemosnocasodosfinders
dinâmicos.Sãoinclusiveosmesmosparâmetrostalcomopodemosverase-
guirquandobuscamosdezinstânciascontandoapartirdaposiç ão11.
208

## Página 215

CasadoCódigo Capítulo6. Buscas
/*
Simplesmente 'from Item' indica que iremos
buscar todos os registros, pois não há filtragem
de dados.
*/
Item.findAll("from Item", [max:10, offset:11])
JáaordenaçãoéfeitacomofaríamosemSQL.Adiferen çaestánofatode
queiremosreferenciarnaordenaçãoaspropriedadesdasclassesreferenciadas
naconsultaenãocolunas:
Item.findAll(from Item where nome like '%a%' sort by nome" ,
[max:10, offset:11])
Consultas para relatórios
Atéagorasófizemosconsultasquenosretornaminstânciasdaclassena
qualinvocamosométodo findAll(ou find),mashásituaçõesnasquais
queremosobterapenas partedaclassededomínio(ousuasreferências),tal
comofizemoscomasproje çõesnascriterias.Sim:apalavra-chave select
voltaaterusoaqui.
Imaginequedesejemosimplementarumrelatóriodecotaçõesquecon-
tenhaosseguintescampos:
• Identificadordacotação
• Categoriadacotação(apenasseunome)
• Nomedoitemcotado
• Moeda(apenasonome)
• Valordacotação
Esterelatórioreceberácomoparâmetroapenasadatadeinícioefim,que
usaremosnacomposiçãodanossafun çãocujaimplementaçãopodemosver
aseguir:
209

## Página 216

6.5. HQL CasadoCódigo
def cotacoesPorData(Date dataInicio, Date dataFim) {
Cotacao.findAll("select c.id, c.item.categoria.nome, \
c.item.nome, c.moeda.nome, c.valor \
from Cotacao c \
where c.data between :inicio and :fim",
[inicio:dataInicio, fim:dataFim])
}
Usamosapalavra-chave selectnapráticaquandoqueremoscustomi-
zaroqueseráretornado.Nestecaso,nãoviráumalistadeinstânciasdanossa
classededomínio,massimumalistadematrizesde Object( Object[]),
naqualaordemnointeriordecadamatrizcorresponderáàquedeclaramos
emnossaconsulta.Asfamosasfun çõesagregadoras.
Avantagemdeumaconsultadestetipoéasualeveza.Emvezdebuscar-
mosografocompleto,obtemosapenasaquiloqueinteressaaonossorelatório.
Claro,asregrasdepaginaçãoeordenaçãotambémseaplicamaessetipode
consultapoisqueremosevitarestourosdememóriaconformenossobanco
dedadosaumentadetamanho.
Assimcomonascriterias,tambémtemosfun çõesespeciaisquenosaju-
damaimplementarrelatóriosmaiscomplexos. Nalistaaseguirpodemos
veralgumasdestasfun ções.Paraumalistacompleta,recomendoaleiturada
documentaçãooficialdoHibernatesobreHQL[?].
•avg Amédiadosvaloresdeumdadoatributodanossaclassededo-
mínio.Exemplo: avg(cotacao.valor).
•sum A soma dos valores de um atributo do domínio. Exemplo:
sum(cotacao.valor).
•count Contaasocorrênciasdeumatributododomínio. Exemplo:
count(cotacao.moeda).
Umexemplorápidodeconsultausandoestesoperadores.Talvezqueira-
mosobterasomadetodasascotaçõesfeitasemReal.
Cotacao.find("select sum(c.valor) from Cotacao c\
where c.moeda.nome = 'Real'")
210

## Página 217

CasadoCódigo Capítulo6. Buscas
Ouentão,aindamaisinteressante:amédiadepre çosparadeterminado
item.
COtacao.find("select avg(c.valor) from Cotacao c\
where c.item.nome = ?", ['Britador'])
Quando usar HQL?
HQLéumaalternativainteressantíssimaquandoprecisamosescrever
consultasumpoucomaiscomplexasoufocadasnaimplementaç ãoderela-
tórios.Trata-sedeumalinguagemdeconsultabastantepoderosaequeneste
capítulo,devidoàlimitaçãodeespaço,acabamosportratarapenasdofun-
cionamentobásico. Suaúnicalimitaçãoaparecequandoprecisamosescre-
verconsultasdinâmicas,situaçõesnasquaisoprogramadoracabaprecisando
concatenarstringse,comisto,terminaporproduzircódigodifícildemanter,
dealtacomplexidadeemuitopropensoaerros.
211

## Página 219

Capítulo7
Acamadaweb:controladores
Nestecapítulovamosentenderoprocessoportrásdeumaaç ãosimplesexe-
cutadaporqualquerusuário. VeremoscomooatodeacessarumaURLdo
nossosistema,porexemplo http://localhost:8080/concot/categoria,resultana
renderizaçãodepáginascomoaexpostaaseguir.

## Página 220

7.1. Masantesvamosfalarumpoucosobrescaffolding? CasadoCódigo
7 .1 M as antes v amos falar um pouco sobre scaf-
folding?
No capítulo4 criamos alguns controladores mas não chegamos a ver
como estes funcionam pois os que vimos foram gerados com o auxí-
lio doscaffolding. Apenas para lembrar, veja como ficou a nossa classe
CategoriaControllernaquelemomento:
package concot
class CategoriaController {
static scaffold = Categoria
}
Esteatributoestáticochamado scaffoldrecebecomovaloraclassede
domínio CategoriaeseráusadopeloGrailspara,emtempodeexecuç ão,
214

## Página 221

CasadoCódigo Capítulo7. Acamadaweb:controladores
gerartodoocódigoresponsávelpornosfornecerumCRUDessencialpara
onossosistemaquenospermitiráincluir,alterar,editarelistarosnossos
registrosdecategoriasnobancodedados. Issoincluitantoocontrolador
quantoaspáginasGSPusadasnarenderização.
Atributo scaffold
Oatributoscaffoldnarealidadepodereceberdoisvalores.Oprimeiro
éaclassequedesejamosusarparageraroCRUD.Asegundaésimples-
menteovalorbooleano true.
Quandopassamos truecomovalor,oGrailsiráusarcomobasepara
descobrirqualaclassededomínioonomedocontrolador,talcomono
exemploaseguir,quegeraráoscaffoldingparaaclassededomínio Item.
class ItemController {
static scaffold = true
}
Fig.7.2:Compatibilidade
Naversão3.0doGrailsoscaffolddinâmiconãofoiincluídoentreos
recursosdoframework,masnãoseassuste:eleprovávelmenteestaráde
voltanaversão3.1oumesmoantes.:)
Éimportantequenoslembremosoqueéo“scaffolding”. Traduzindoa
palavraparaoportuguêstemosotermo“andaime”.Oqueéumandaime?É
215

## Página 222

7.1. Masantesvamosfalarumpoucosobrescaffolding? CasadoCódigo
umaestruturaquenospossibilitaobteracessoaalgumacoisaoulugaronde
possamosnosescorare,apartirdali,atingiralgumobjetivo.Otermotemsua
origemnaconstruçãocivile,casoonomelhepare çafamiliarmasaindanão
consigaselembrardetervistoum,afotoaseguirrefrescarásuamemória.:)
Fig.7.3:Scaffolding
OqueéesteandaimequeGrailsnosoferece?Aquedesejamosteracesso
comele?Comoassimmeescorar?Meescoraronde?Oquedesejamoscons-
truircomele?
Nãoseisevocêjáreparou,masalgumasdastarefasqueexecutamosdu-
ranteodesenvolvimentodeumaaplicaç ãosãobastanterepetitivas. Pegue
comoexemploocódigoquenormalmenteescrevemosparaconstruirum
simplesCRUD.Aimpressãoquetenhoéadequesempreexecutamosexa-
tamenteasmesmastarefas:
1) Usuáriopreencheumformulárioeosubmete.
2) Obtemososvalorespreenchidospelousuárioapósasubmissãodoformu-
lárioeosusamosparapreencherosatributosdeumoumaisobjetos.
3) Validamososvaloresparanoscertificardequeforamcorretamentepre-
enchidos.
4) Tudoestandook,persistimosnossoobjetodedomínioeemseguidaredi-
recionamosnossousuárioparaumapáginaqualquer.
216

## Página 223

CasadoCódigo Capítulo7. Acamadaweb:controladores
Evocêescreveráestecódigoinúmerasvezes.Éatépossíveltirarproveito
daorientaçãoaobjetosemodularizarboapartedestetrabalho,evitandotoda
essarepetição,masemsuaessênciaotrabalhosempreserábastantepróximo
disto. Maisdoqueisso,nãoseiseéoseucaso,masaesmagadoramaioria
dosprogramadoresachaessetipodetrabalhomuitotedioso.Seráqueinves-
timostantoassimnanossaformaçãopara,nofinaldodia,terminarfazendo
essencialmente...isto???
Dadoqueéumtrabalhorepetitivoequeocorreempraticamentetodo
projeto,nãoserialegalsehouvessealgocomoum“assistente”queogerasse
automaticamenteparanós? Melhorainda: eseesteassistentegerassepara
nóscódigofácildesercustomizado,detalmodoquenóssóprecisássemos
alteraraquiloquerealmenteimporta?
O que é este andaime?Éageraçãoautomáticadetodocódigo-fonteque
executetarefasrepetitivasduranteodesenvolvimentomasquenospermita
customizá-loconformesemostrenecessário. A que desejamos ter acesso com
este andaime?Umamelhorprodutividadeapartirdomomentoemquepo-
demosinvestirnossotemponaimplementaçãodepartesmaiscomplexasdos
nossossistemaseque realmente importem e agreguem valor. Como assim
me escorar?Elenosfornecetodoocódigo-fonteinicial,énelequemeescoro,
poisapenasprecisocustomizá-lodeacordocomasminhasnecessidades. O
que desejamos construir com este scaffolding?Todas(ouquase)aspáginasde
cadastrodonossosistema!
Esabemoqueémaisimportanteemandaimes? Depoisqueatingimos
nossoobjetivopodemossimplesmentenosesquecerdelesoumesmojogá-los
forajáqueotrabalhoestáprontoenãoprecisamosmaisdeles.Oscaffoldingé
isto:nósiremosusá-lorepetidasvezesatéchegarmosaopontoquedesejamos.
Depoisdissovocêsimplesmenteesquece-sedele.
Atéestemomentonossoandaimeéinvisível:apenasdeclaramosumatri-
butoestáticoeassociamosumaclasseaeleeoGrailsgentilmentegeratodo
ocódigo-fonteemtempodeexecuç ão(poristoochamodedinâmico). É
umaopçãomuitointeressantequandoaindaestamosmodelandonossasclas-
sesdedomínioequeremosexperimentarcomosecomportarãoaspáginas
deCRUDdanossaaplicação,masinfelizmentenãosãoumaboaalternativa
quandoprecisamoscustomizarseufuncionamento.
217

## Página 224

7.1. Masantesvamosfalarumpoucosobrescaffolding? CasadoCódigo
Sendoassimapresentoumnovocomandoaoleitor: generate-all,
querecebecomoparâmetroonomecompletodaclassededomínio(oque
incluiseupacote).Esteirágerarumnovocontroladorparanósalémdetodas
aspáginasGSPqueseriamgeradasemtempodeexecuç ãopeloframework,
oquenospermitiráagoracustomizá-lasdeacordocomnossasnecessida-
des. Paracomeçarnossoalvoseráaclassemaissimplesdonossosistema:
Categoria.Éoquechamode “scaffolding estático
.Bastaexecutarocomandoaseguir:
grails generate -all concot.Categoria
O script irá nos perguntar se desejamos substituir o arquivo
CategoriaController que já havíamos criado tal como exposto na
imagemaseguir.Bastadigitar“y”(yes)ou“a”(all)eemseguidapressionar
ENTER.
Fig.7.4:grailsgenerate-allconcot.Categoria
No diretório grails-app/views/categoriaserão gerados cinco
arquivosGSP: _form.gsp, create.gsp, edit.gsp, index.gspe
show.gsp.CorrespondemàspáginasquecompõemoCRUDdestaclassede
domínio.Tambémserácriadoumnovo CategoriaController.groovy
nodiretório grails-app/controllers/concot,destavezbemmaior
quenossaprimeiraversãoquecontinhaapenasumalinha.Agoravocêpode
customizar100%doseuscaffolding.
Fizestepequenoparêntesesobrescaffoldingapenasparacriaromate-
rialqueusaremosnorestantedestecapítulo. Maisàfrentefalaremosmais
sobrecomovocêpodecustomizarageraçãodecódigocomGrails,maspor
enquantosónosinteressaaclasse CategoriaController.
218

## Página 225

CasadoCódigo Capítulo7. Acamadaweb:controladores
7 .2 E ntendendo os controladores
Oqueéumcontrolador?Nósjáfalamossobreoqueéopadrãodeprojeto
MVC4.4,mascomoaequiperesponsávelpelodesenvolvimentodoGrails
defineumcontrolador? Definemcomooresponsávelporlidarcomasre-
quisiçõesrecebidaspelaaplicaçãoepreparararespostaqueéenviadacomo
resultadoparaousuáriodonossosistema,respostaestaquepodesergerada
peloprópriocontroladoroudelegadaparaacamadadevisualizaç ão.Oobje-
tivodestecapítuloédetalharcomoesteprocessoocorre.
ComotudoemGrails,nossoscontroladorestambémseguemalgumas
convenções.Comecemosporaquelasquesãoaplicadasnacriaç ãodaclasse
deumcontrolador:
• Deveestararmazenadanodiretóriograils-app/controllers.
• DevepossuirosufixoControllernonomedaclasse.
Você também pode gerar controladores usando um comando es-
pecial presente na interface de linha de comando do Grails chamado
create-controller,comonoexemploaseguir:
create-controller Importacao
Serão gerados tanto o arquivoImportacaoController.groovy
quantoseuarquivodetesteunitário ImportacaoControllerSpec.groovy.
Casonãosejafornecidoonomedopacote,seráusadocomopacotepadrão
onomedoseuprojeto.Éimportantesalientarquevocênãoprecisausareste
comandoparacriarseuscontroladores.Eleémeramenteumaconveniência.
Actions
Observeométodo indexincluídonaclasse CategoriaController
peloscaffoldingestático,oqualmodifiqueilevementeparafinsdidáticos:
def index() {
[categoriaInstanceList: Categoria .list(params),
categoriaInstanceCount: Categoria .count()]
}
219

## Página 226

7.2. Entendendooscontroladores CasadoCódigo
Este método é o que dentro do jargão Grails chamamos deaction.
Neste caso, a única ação executada por nossa primeira action é retor-
nar um mapa contendo duas chaves: categoriaInstanceList e
categoriaInstanceCount,representandorespectivamentealistadeca-
tegoriaseonúmeroderegistrospresentesnobancodedados.
Mas o que é uma action?Éafun çãoqueescrevemosemnossocontrolador
responsávelporlidarcomasrequisiçõesHTTPrecebidaspelanossaaplicação
web.Éseutrabalhotratarosparâmetrosrecebidos(pelaURL,formuláriosou
corpodarequisição),chamarosmétodosnecessáriosnacamadadenegócio,
transformá-loscasonecessárioparaquesetornemadequadosàrespostaen-
viadaaousuáriodosistema.Estarespostapodeseressencialmentequalquer
coisa:umarquivo(nocasodeumrelatóriooudownload),umdocumento
XML,JSONouemoutroformatoousimplesmenteumapáginaHTML.
Vocêdeveternotadoquefoipassadocomoparâmetroàfun ção listum
objetochamado params.Elerepresentaosparâmetrosquepodemtersido
fornecidosaométodoatravésdaURLqueiniciousuaexecuç ão,comoneste
endereço:http://localhost:8080/concot/categoria?max=10&offset=11,queiráge-
rarbuscaqueretornarádezitensapartirdadécimaprimeiraposiç ão.Fala-
remosmaissobreo paramsmaisàfrente. Mas como esta URL é formada e
como é feita a associação entre esta e nossas actions?
220

## Página 227

CasadoCódigo Capítulo7. Acamadaweb:controladores
Cuidado com seus métodos!
Fig.7.5:Atençãoredobrada!
Todométodopúblicoquevocêdeclararemumcontroladorseráin-
terpretadocomoumaaction. Sendoassim,certifique-sedesempresó
incluirmétodosnestasclassesqueatuemcomotal.
Essalimitaçãotemseuladopositivo:elalheobrigaaincluirsualó-
gicadenegócioemclassesdeserviço,quesãoondeestetipodecódigo
realmentedeveestar.
IncluirmétodosinúteisemseuscontroladorescrianovasURLsque
podeminclusiveserusadasporusuáriosmalintencionadoscontraseus
sistemas.Leveistoemconsideração!
Action default
Nocasodométodo indexestamoslidandocomoqueno“jargãoGrails”
chamamosdeactionpadrão(default action)docontrolador.Quandonossa
URLnãodefinequalactiondeveráserexecutada(veremoscomoissoéfeito
maisàfrente)comoGrailssabequalcódigoexecutar?Nocaso,aoacessarmos
oendereçohttp://localhost:8080/concot/categoriaGrailsiráexecutaraseguinte
lógica:
1) Existeapenasumaactionnocontrolador?Sesim,execute-a.
2) Existe um atributo no meu controlador chamadodefaultAction?
Existindo,esterecebecomovalorumastringqueidentificaaactionpa-
drãodomeucontrolador.
3) Existealgumaactionchamada“index"?Sesim,seráexecutada.
221

## Página 228

7.2. Entendendooscontroladores CasadoCódigo
Voltandoao ConCotpercebemosqueasduasprimeirascondiçõesnãosão
satisfeitas:hámaisdeumaactiondefinidanestaclasseetambémnãotemos
umatributochamado defaultAction,masháumachamada index,que
seráexecutada.
Executadanossaaction,estaretornaráummapacomduaschavestal
comovimosacimaenossousuárioserácontempladocomumapáginasi-
milaràexpostaaseguir:
Fig.7.6:Páginaindexgeradapeloscaffolding
Como esta página é renderizada? Outra convenção do fra-
mework: o leitor deve se lembrar que foi gerado um arquivo chamado
index.gspnodiretório grails-app/views/categoria.Nodiretório
grails-app/views/categoria encontram-se armazenadas todas as
páginasGSPquesãousadas por padrão pelocontrolador.Reparenonome
dapasta:correspondeaodonossocontroladorsemosufixo Controller.
E no interior da pasta onde armazenamos nossos arquivos GSP,
o que temos? Teremos arquivos cujos nomes corresponderão aos de
222

## Página 229

CasadoCódigo Capítulo7. Acamadaweb:controladores
nossas actions. Sendo assim, será renderizada por padrão a página
grails-app/views/categoria/index.gspparaaaction indexpre-
sentenaclasse CategoriaController.Simplesedireto.
Para que serve aquele mapa que nossa action retornou como valor?Aquele
mapapossuiumnomeespecialdentrodo“jargãoGrails":chama-se model,e
representaasinformaçõesqueserãoexpostasemnossaspáginas.Cadauma
daschavesdefinidasnessaestruturairácorresponderaumavariávelquees-
tarádisponívelemnossosarquivosGSP.Vocêdeveestarcuriosoparasaber
comoissoocorre,certo?Entãoobserveocódigoaseguirqueéumtrechodo
arquivo index.gsp.
<g:each in="${categoriaInstanceList}" status="i" var="categoriaInstance">
<tr class="${(i % 2) == 0 ? 'even' : 'odd'}">
<td>
<g:link action="show" id="${categoriaInstance.id}">
${categoriaInstance.nome}
</g:link>
</td>
</tr>
</g:each>
EsteéseuprimeirocontatocomatecnologiaGSP: Groovy Server Pages.
Falaremosmaisaseurespeitoadiante,masporenquantooquenosinteressa
nestetrechoéousoquefazemosdeumdosatributosdonossomapa,achave
categoriaInstanceList.
A tag <g:each> cria um loop responsável por iterarmos sobre to-
dosositensarmazenadosemumacole ção. Acoleção,nocaso,éachave
categoriaInstanceListretornadapelonossocontrolador,queiremos
passarcomovaloraoparâmetro in.Oatributo statusdefineonomede
umavariávelqueatuarácomoumcontador.Nósousaremosparaadicionar
aclasse evenou oddacadaumadaslinhasdenossatabela,gerandooefeito
listradoquevimosnaimagemanterior.Finalmente,oatributo vardefineo
nomedavariávelqueseráacessadanointeriordonossoloop.
Atag <g:link>éusadaparageraroslinksdanossaaplicaç ãoaserem
renderizadosemnossapágina. Usamosapenasdoisparâmetros: action,
identificandoonomedaactionquedeveráserexecutadaemnossocontrola-
223

## Página 230

7.2. Entendendooscontroladores CasadoCódigo
dore id,cujovalorcorrespondeaoatributodemesmonomedonossoobjeto
categoriaInstance.
EmumarquivoGSP,tudooqueestiverentre ${e }éinterpretadoe
ovalorobtidorenderizadoparaousuário. Soafamiliar? Acreditoquesim,
dadoqueéexatamenteomesmomecanismousadopelasstringsemGroovy.
:)
Actions no Grails 1.x
Fig.7.7:Compatibilidade
UmanotaimportanteparaosleitoresqueestejamvindodoGrails1.xou
precisemlidarcomaplicaçõesimplementadasnestafamíliadoframework:
apartirdaversão2.0todasasactionspassaramaserimplementadas,por
padrão,comofun çõesemnossoscontroladores,enãomaiscomoclosures.
Nasversõesanterioresà2.0todasasactionseramdeclaradasdestaforma:
def index = {
// código entrava aqui
}
Comoconsequência,odesenvolvedorsópoderátrabalharcombinding
baseadoemmapasehátambémocustoocultonoPermGenqueumaclo-
surenostrás. Todaclosureaosercompiladaétransformadaemumnovo
arquivo .class. Oresultadoéumconsumomaiordememórianaantiga
áreaPermGenusadapelasversõesdoJavaanterioresà8.
Amudançatrazidapelaversão2.0nostrouxealgunsbenefícios:
• Usaamemóriadosistemadeumaformamaiseficiente.
224

## Página 231

CasadoCódigo Capítulo7. Acamadaweb:controladores
• Permiteousodecontroladoresdotiposingleton(lembre-sedequeas
closurescarregamconsigooescopodeondesãodeclaradasefazem,
porsuavez,partedoestadodocontrolador).
• Permitesobrescreverasactionsdeumaformamaissimplesusandohe-
rança.
• Permiteainterceptaçãodemétodosatravésdemecanismosdeproxia-
mentopadrão,algoqueémaisdifícildesefazercomclosures,dadoque
estasacabamsendoconfundidasporestesmecanismoscomatributos
enãométodos.
Agora,sevocêquisercontinuarusandoclosuresemseusprojetos(tal-
vezvocêestejalidandocomcódigolegado)etertodososganhosobtidos
comonovopadrão,vocêpode!Bastaadicionaralinhaaseguirnoarquivo
grails-app/conf/Config.groovy:
grails.compile.artefacts.closures.convert = true
EstainstruçãoiráaplicarumatransformaçãoASTemtempodecompila-
çãonoseuprojeto,transformandotodasasclosuresdeclaradasemseuscon-
troladoresemmétodos.
7 .3 D ominando URLs
UmadasURLsgeradaspelatag <g:link>quevimosemnossoarquivoGSP
foi http://localhost:8080/concot/categoria/show/1.Háumasériedeinformações
contidasnesteendere çoquesãoexpostasnaimagemaseguir:
Fig.7.8:NossaURLdissecada
225

## Página 232

7.3. DominandoURLs CasadoCódigo
OcontextodizrespeitoàpartedaURLqueidentificaanossaaplica-
çãodentrodeumservidordeaplicações. Qualquerendere çoquecomece
com http://localhost:8080/concotirácairemalgumaaction(ouausênciade)
donossoprojeto.Oquerealmentenosinteressaaquiéoquevemaseguir:o
nomedocontroladorequalaactionaserexecutada.
SeemnossobrowserdigitarmosestaURL,aaction showdefinidana
classe CategoriaControllercujocódigo-fonteéexpostoaseguir(eque
modifiqueiligeiramente)seráexecutado.
def show(Long id) {
[categoriaInstance: Categoria.get( id)]
}
Oleitordeveestarconfusonestemomento:épassadooparâmetro 1à
nossaURL,eemnossaactiondefinimosumparâmetrodemesmonome.Mas
ondedefinimosqueaquele“1”aofinaldaURLcorrespondeaoparâmetro
iddafunção show?
Novamenteoutraconven çãodoGrails: senossaURLrecebeumúnico
parâmetronãonomeado,comoéocasodestaURL,eleporpadrãorecebeo
nomede id.Estecomportamentoéinclusivedefinidoviaconfiguraç ão,no
arquivo grails-app/conf/UrlMappings.groovy,ondeconfiguramos
comonossasURLsdevemsecomportar.Oarquivopadrãogeradocomtoda
aplicaçãoGrailséexpostoaseguir:
class UrlMappings {
static mappings = {
// É aqui que definimos a convenção do atributo "id" :)
"/$controller/$action?/$id?(.${format})?"{
constraints {
// apply constraints here
}
}
"/"(view:"/index")
"500"(view: '/error')
}
}
226

## Página 233

CasadoCódigo Capítulo7. Acamadaweb:controladores
E como seria a passagem de mais de um parâmetro para uma URL?Volte-
mosàaction index,queapenasexecutaumfinderdinâmico.Sequiséssemos
exporapenas10categoriaspaginandoatravésdadécimaprimeiraposiçãopo-
deríamosenviarumaURLcomoaseguinte:
http://localhost:8080/concot/categoria/index?max=10&offset=11
Observequeestamosacessandoaaction indexdiretamenteagora,sem
anecessidadedetirarmosproveitodasconven çõesreferentesàactionpadrão
docontrolador.Apenasparalembrar,aimplementaçãomodificadadestaac-
tionpodeservistanalistagemaseguir:
def index() {
[categoriaInstanceList: Categoria.list(params),
categoriaInstanceCount: Categoria .count()]
}
Oobjeto params,comoditoantes,énarealidadeummapaquearma-
zenatodososparâmetrosquenossaactionrecebeatravésdaURL,submissão
deformuláriooucorpoHTTP.Sendoassim,semodificássemosligeiramente
estaactionparaimprimiresteobjetotalcomo:
def index() {
println params
[categoriaInstanceList: Categoria .list(params),
categoriaInstanceCount: Categoria .count()]
}
AntesdeapáginaserrenderizadaveríamosnoconsoledoGrailsserim-
pressoumtextosimilara:
[max:10, offset:11]
Oleitordeveestarconfusoagora:porondesãoacessadososparâmetros?
Pelaassinaturadométodoquecompõeaactionoupeloobjeto params?Pe-
losdois,sódependedasuapreferência.Aprincipalvantagemnapassagem
dosparâmetrospelaassinaturadaactionestánafacilidadedeescritadetes-
tesedocumentaçãodoqueseesperaqueaquelemétodorecebacomoen-
trada.Casoestejamoslidandocommuitosparâmetros,oumesmosituações
nasquaisosparâmetrosrecebidospodemvariar,semsombradedúvidaso
227

## Página 234

7.4. Redirecionandoações CasadoCódigo
objeto paramsou command objects,queveremosmaisàfrenteirãocum-
prirmuitomelhorestatarefa.
7 .4 R edirecionando ações
Emalgumassituações,éinteressantequeumaactionredirecioneoprocessa-
mentoparaoutra.Apenashipoteticamente,imaginequeno ConCotsejado
nossointeressequeumusuáriosópossacriarnovascategoriascasojáesteja
autenticadonosistema. Bastamodificaraaction saveparaquefiquetal
comoocódigoaseguir:
def save() {
if (seguranca.usuarioAutenticado()) {
// faça o que precisa ser feito
} else {
// Redirecione o usuário para a action
// responsável pelo login
redirect(action:'login', controller:'entrada')
}
}
Nesteexemplousamosdoisparâmetrosparaidentificarqualocontro-
ladorequalactiondesejamosquesejaexecutadacasoousuárionãoesteja
autenticado. Épossíveltambémpassarparâmetrosparaaactionaserredi-
recionada.Paraisso,bastausarmosoparâmetro params.Vejaoexemploa
seguirnoqualincluímosoparâmetro acessoIndevidoparaocontrolador
entrada.
def save() {
if (usuarioAutenticado()) {
// faça o que precisa ser feito
} else {
// Redirecione o usuário para a action
// responsável pelo login
redirect(action:'login', controller:'entrada', params:[acessoIndev
}
}
228

## Página 235

CasadoCódigo Capítulo7. Acamadaweb:controladores
OutraalternativainteressanteéredirecionarousuárioparaumaURL.
Imaginequevocêestejadesenvolvendoumsitevoltadoaadultosedesejeque
menoresdeidadesejamdirecionadosparaoutrositequalquer.Bastausaro
parâmetro url:
def testeIdade() {
if (params.int('idade') < 21) {
redirect(url:'http://www.disney.com')
} else {
redirect(controller:'home')
}
}
Oleitordeveternotadoafun ção intusadanoobjeto params.Assim
como long,elaconverteoparâmetro(queporpadrãosempreéarmazenado
comoumastring)paraotipointeiroou long.Nomesmoexemplo,casoo
usuáriopassenotestedaidade,esteseráentãoredirecionadoparaaaction
padrãodocontrolador home.
7 .5 R enderizando a resposta
E se eu não quiser renderizar a página padrão da action, como faço?Usamosa
função renderqueseencontrapresenteemtodocontrolador.
Imaginequesejadonossointeresseescolherqualpáginairárenderi-
zarumacategoriarecém-persistidadeacordocomapermissãodeacessodo
usuário.Usamosafun ção renderpresenteemtodocontroladortalcomo
noexemploaseguir:
def save() {
/* ignoramos todo o início da action
o modelo já se encontra armazenado em
uma variável chamada resultado em nossa action */
if (condição) {
render(view:'pagina1', model:resultado)
} else {
render(view:'pagina2', model:resultado)
}
}
229

## Página 236

7.5. Renderizandoaresposta CasadoCódigo
Ométodoviewnestecasorecebedoisparâmetrosdeentrada: view,que
representaonomedapáginaGSPqueiremosrenderizar,porpadrãopre-
sentenodiretóriorelacionadoaocontroladoremqueaactionseencontra;
e model,representandoomodeloaserusadodurantearenderizaç ãoda
mesma.
OarquivoGSPnãoprecisaseencontrarnomesmodiretóriodocontro-
lador.Sequiserdelegararenderizaçãodarespostaparaumapáginaarmaze-
nadaemoutrapasta,bastaescreverocaminhocompletoaela:
def renderizaDiferente() {
/*
Renderiza a página contida
no diretório
grails-app/views/custom
*/
render(view:'/custom/pagina')
}
Renderizando apenas um trecho HTML, XML ou JSON
Esseexemploébastantecomum,masnemsemprequeremosrenderi-
zarumapáginainteira.Hásituações,comoporexemplo,emumachamada
AJAX,emquenossocontroladordeveretornarapenasumtrechoHTML.
Vocêpodefazerissodeumaformabastantesimples,comoocódigoadiante,
queirárenderizarumalistacompletadecategoriasembarcadasemHTML.
def pesquisa() {
//executa as consultas necessárias
//e armazena a lista de categorias em uma
//coleção chamada resultado
render(contentType: "text/html") {
table {
for (categoria in categorias) {
tr {
td(id:categoria.id) categoria.nome
}
}
}
230

## Página 237

CasadoCódigo Capítulo7. Acamadaweb:controladores
}
}
Trata-sedeumaDSLsimplesqueirátransformaraqueleblocodecódigo
vistoanteriormenteemHTMLsimilaraoexpostoaseguir:
<table>
<tr>
<td id="1">Equipamentos</td>
<td id="2">Materiais</td>
</tr>
</table>
ComoseriarenderizarXML?
def pesquisa() {
// restante omitido
render(contentType:"text/xml") {
categorias {
for (categoria in resultado) {
categoria(id:categoria.id, nome:categoria.nome)
}
}
}
}
Qualoresultado?Algosimilara:
<categorias>
<categoria id="1" nome="Equipamentos" />
<categoria id="2" nome="Materiais"/>
</categorias>
EJSON,comoeufaria?Achoquevocêjásabe,masvamosaoexemplo.
def pesquisa() {
// restante omitido
render(contentType:"application/json") {
array {
for (categoria in resultado) {
231

## Página 238

7.5. Renderizandoaresposta CasadoCódigo
[id:categoria.id, nome:categoria.nome]
}
}
}
}
Oresultado?
[ {id:1, nome:"Equipamentos"},
{id:2, nome:"Materiais"} ]
Comopodeservisto,ébastantesimples:bastapassarmosdoisparâme-
trosparaométodo render.Oprimeirocorrespondeao mime typedoque
desejamosretornaraoclientedanossaaction. Osegundoparâmetroéum
builderGroovy.
BuilderssãoumpoderosorecursooferecidopeloGroovyquenosper-
mitemrepresentarestruturashierárquicascomodocumentosXML,HTMLe
JSONdeumaformabastantesimples.Paramaioresinformaçõessobreeles,
convémconsultaradocumentaçãooficialdalinguagem[6].
Interpretadoobuilder,ométodo renderirásimplesmenteretornaro
resultadodiretamenteaoclientequefezasolicitaç ãoànossaaction.
Háumamaneiramaissimplesdeseobteromesmoresultado:
def pesquisa() {
// restante oculto
render(contentType:"o mime type de sua escolha") {
objetoQualquer
}
}
Nestecaso,oGrailsirápercorrertodososatributosdesteobjetogerandoo
resultadonoformatopassadocomovalorparaoparâmetro contentType.
Oproblemadestaabordageméquevocêpodegerardocumentosenormes
acidentalmentecasohajaumgrafocomplexonoqueforrenderizado. Não
consideroumasoluçãotãoelegante,portanto.Outroproblemaéquequando
estamosrenderizandodocumentos,napráticaestamoscriandoAPIs.Dado
queosatributosdenossasclassespodemvariar,estavariaç ãopoderiaquebrar
todososclientesquedependamdestaAPIquevocêacaboudecriar.
232

## Página 239

CasadoCódigo Capítulo7. Acamadaweb:controladores
E ainda é possível simplificar ainda mais esta renderização. Como?
Usandoo marshallingautomáticodeclasses de domíniousandoconverso-
resespeciaisparaosformatosXMLeJSON.Trata-sedeumafuncionalidade
tãofácildeserusadaquenemhámuitooqueserdito.Vamosaosexemplos:
// Basta incluir esta instrução de importação de classes
import grails.converters.*
// e na sua action...
// Como fazemos com JSON?
def renderizarJSON() {
// Como renderizamos para JSON uma
// lista de categorias
render Categoria.list() as JSON
}
// E para gerar XML?
def renderizarXML() {
render Categoria.list() as XML
}
Simplesassim.:)
Marshalling e unmarshalling
Umtermoquecostumaconfundiriniciantesé marshalling,possivel-
mentepornãohaverumatraduçãodiretaparaoportuguês.Marshalling
éoatodeestarmosgerandoconteúdoemalgumformato(XML,JSON)
tendocomobaseumobjeto. Eo unmarshalling? Ocontrário:vocêirá
instanciarobjetosepopulartodososseusatributostendocomobaseum
documentoemumformatoespecífico.
Content negotiation
MuitasvezesvocêusaráGrailsparaimplementarAPIsREST(ouSOAP).
Seesteforoseucaso,vocêficaráfelizpelofatodeoframeworkoferecersu-
233

## Página 240

7.5. Renderizandoaresposta CasadoCódigo
portenativoa content negotiation.Trata-sedeummecanismodefinidodentro
dopróprioprotocoloHTTPquepermiteofornecimentodediferentesversões
deummesmodocumentorepresentadoporumadadaURL.
NocasodoGrails,asdiferentesversõesdodocumentoequivalemaosfor-
matosJSONouXML.Senestepontooleitormaiscuriosojábrincouum
poucocomoscaffoldingestático,deveterpercebidoalgumasactionssimila-
resàqueexponhoaseguir,querepresentaalistagemdecategoriasno ConCot.
def index(Integer max) {
params.max = Math.min(max ?: 10, 100)
respond Categoria.list(params), model:[categoriaInstanceCount: Categoria
}
Oqueéeste respond? Afunção respondirátentarforneceraocli-
entequefezasolicitaçãoalistadecategoriasnoformatoapropriado:JSON,
XMLouumapáginaHTMLqueéopadrão.Nocaso,issopodeserfeitoatra-
vésdofornecimentodocabe çalhoHTTP Acceptpelocliente,pedindo,por
exemplo,quearespostasejaenviadanoformatoXMLouatravésdainclusão
doparâmetro formatnaURL,como http://localhost:8080/concot/categoria?
format=xml,queestápedindoquesejafornecidooconteúdonoformatoXML.
Porpadrão,todarequisiçãoHTTPfeitaànossaaplicaç ãocostumavir
comocabe çalho Accept,cujovalordefaulté */*.Parafornecimentono
formatoJSON,esteprecisariavircomovalor application/JSONe,para
XML, application/XML.
ApartirdoGrails2.0,vocêpodeinclusivecustomizarasuarespostade
acordocomoformatopedidopelocliente:
request.withFormat {
xml {
// trate o formato XML aqui,
// exatamente como faria se fosse um render
}
json {
// JSON
}
'*' {
// HTML padrão
234

## Página 241

CasadoCódigo Capítulo7. Acamadaweb:controladores
}
}
7 .6 D ata Binding
Ok,atéagorasóvimosactionsextremamentesimples,quenãolevamemcon-
sideraçãoorecebimentodeparâmetros.Oqueocorrecomosdadosquesub-
metemosaocontroladorusandoformulários,querystringsemumaURLou
mesmonocorpodeumarequisiç ão? Grailsnosforneceummecanismode
bindingextremamentericoepoderoso,quetornasuavidamuitomaissim-
ples.
O que é binding/data binding? Aousarmosumframeworkparadesen-
volvimentoweb,muitasvezesnosesquecemosdomodocomooprotocolo
HTTPfunciona. Basicamentetodososparâmetrospassadosàsnossasacti-
onsvêmcomoumaestruturadotipochave-valornaqualtodososparâmetros
encontram-senoformatotextual.
Issotrásalgunsproblemas,dentreosquaispodemoscitar:
• Comoparseardemaneiratransparenteparâmetrostextuaisparatipos
como integer, long, double, booleanetc.?
• Comopreencherautomaticamenteosatributosdeumobjetocom-
plexo,comoumaclassededomínio,apartirdaquelesparâmetros?
• Comovalidarestesparâmetrosdetalmodoque,estandonossaaction
esperandoumparâmetrodotiponumérico,realmentevenhaalgocon-
dizentecomestacondição?
• Preenchimentodeformulários:comotornarestatarefamenosárdua
paraoprogramador?
Todosessesproblemassãoresolvidosporaquelesquesepredispõema
escreverframeworksparadesenvolvimentoweb. NocasodoGrails,muito
doquevemosnestaáreaénarealidadeapenasoreaproveitamentodabase
adotadapeloframework:oSpringMVC.
Resumindo,oqueé data binding?Éoatodeligarmososparâmetrosfor-
necidosaoframeworkpeloprotocoloHTTPàspropriedadesdeumobjeto
235

## Página 242

7.6. DataBinding CasadoCódigo
oumesmoaumgrafocomplexodeobjetosdeformatransparenteparaode-
senvolvedor,quenãomaisprecisasepreocuparcomosproblemasquecitei.
Esteprocedimentopodeocorrerdediferentesmaneiras.Nestase çãose-
rãoexpostasasmaiscomunsnodiaadiadoprogramadorGrails.
Data binding baseado em mapas
Vejamoscomoéoformuláriodecadastrodecategoriasgeradopeloscaf-
foldingcujocódigomodifiqueiligeiramenteparafacilitarseuentendimento
inicial:
<g:form action="save" controller="categoria">
<label for="nome">Nome:</label>
<br/>
<g:textField name="nome"/>
<input type="submit" value="Salvar"/>
</g:form>
Háduasnovastagsaqui.Aprimeiraé <g:form>,queusamosparage-
rarumformuláriocujoatributo action,querepresentaaURLdedestino
dasubmissãoestejacorreta.Elerecebedoisparâmetrosqueidentificamcor-
retamentequalaactionaserexecutada: actione controller.
Emseuinteriortemosoutratag: <g:textField>,queirárenderizar
umcampotextualidentificadopor“nome”.Emseguida,temosumcampodo
tipo submit,quenadamaisédoqueobotãodesubmissãodesteformulário.
Odatabindingbaseadoemmapaspodeserfeitocomonaimplementaç ão
alternativadaaction saveaseguir:
def save() {
// Data binding em ação
def categoria = new Categoria(params)
// restante da action pode ser ignorado
}
Nessecaso,estamosapenasusandooprópriofuncionamentodosPO-
GOs. LembraquesepassarmosparaumaclasseGroovyummapaemseu
construtor,esteiráautomaticamentepreenchertodososatributosdela? É
apenasissooquefazemosaqui. Seumdosatributosde Categoriafosse
236

## Página 243

CasadoCódigo Capítulo7. Acamadaweb:controladores
dotipo int, boolean, longouqualqueroutroqueemJavaéprimitivo,
apróprialinguagemseencarregariadefazerasconversõesnecessáriaspara
nós.
Háoutrasmaneirasdeseusaroobjeto params,vocêtambémpodeusá-
loapósainstanciaçãodoseuobjeto.Issoémuitocomumemactionsdeedi-
ção,porexemplo:
def update() {
def categoria = Categoria.get(params.long('id'))
// Define todos os atributos do nosso objeto em
// uma única linha
categoria.properties = params
// restante da action
}
Narealidade,Grailsvaiumpoucoalémdomeroaproveitamentodocom-
portamentopadrãodosPOGOs.Imaginequemeuobjeto paramssejasimi-
laraoexpostoaseguir,relativoàpersistênciadeumobjetodotipo Item.
['categoria.id':'1', nome:'Motor']
Oatributo categoria.idpoderiavir,porexemplo,deumacaixade
seleção.Vejaaqueoscaffoldingcriaparaocadastrodeitensnaimagem:
Fig.7.9:Cadastrodeitens
237

## Página 244

7.6. DataBinding CasadoCódigo
Atéomomentoapenasvimosobindingcomumaentidadededomínio:
agoraestamosvendocomduas: Itemeseuatributodotipo Categoria.
Grailséinteligenteosuficienteparaperceberqueháumatributochamado
categoriaemnossaclasse Itemqueapontaparaoutraclassededomínio.
Antes de executar o data binding, Grails obterá uma instância de
Categoriacomoidentificadorpassadocomoparâmetroe,emseguida,o
injetaráemnossoobjeto. Depois,podeatémesmoalteraralgumatributo
desteobjetoanexado.Imaginequeestejamostambémmodificandoonome
dacategoriaduranteasubmissãoapartirdeumalistagemdeparâmetros:
['categoria.id':'1', 'categoria.nome':'Motores', nome:'Motor']
Executandoocódigoaseguir:
def save() {
def item = new Item(params)
item.save()
}
Quandooobjeto Itemforpersistido,acategoriacujoidentificadoréo
número 1teráseunomealteradopara "Motores".
Usando a assinatura da action
Outramaneirabastanteelegantedetirarmosproveitododatabindingdo
Grailséatravésdaassinaturadanossaaction,ouseja,apartirdosparâme-
trosqueelaespera. Voltandoaoexemplodaaction save,sabecomoelaé
implementadaporpadrãopeloscaffoldingdoGrails?Assim:
def save(Categoria categoriaInstance) {
// conteúdo da action ignorado neste exemplo
}
Havendoumúnicoparâmetronaassinaturadaaction,odatabindingserá
feitodiretamentesobreestetalcomopôdeservisto.Essecódigo,naprática,
executaotrabalhofeitopelodatabindingpormapas.Adiferen çaestáapenas
nomodocomoescrevemosnossocódigo.
238

## Página 245

CasadoCódigo Capítulo7. Acamadaweb:controladores
Umagrandevantagemdestamodalidadedebindingéqueaescritade
testesficamaisfáciletambémpodemostirarmáximoproveitodatipagem
estática,garantindocomistoumdesempenhosuperiorparaaquelecódigo.
Lidando com erros
Podem ocorrer erros durante o processo de binding? Yeap!Vocêpodeter
errosdetipagem. Imaginequeumdosatributosdasuaclassededomínio
sejadotiponuméricomassejasubmetidoumvalortextual. Novamente,a
soluçãoébastantesimples.
Vamossuporqueestamoslidandocomapersistênciadeumacotaç ão.
Apenasparalembrar,estaéadeclaraçãodaclasse Cotacao:
class Cotacao {
BigDecimal valor
Date data
static belongsTo = [ item:Item,
moeda:Moeda ,
fornecedor: Fornecedor]
}
Agora,suponhaqueestejamosrecebendoparafazerobindingosseguin-
tesparâmetros:
['valor':'dois reais','moeda.id':'1',
'item.id': '32', 'fornecedor.id':'3' ]
Háumerroclaronoparâmetro valor.Comoresolvemosesteproblema
emnossocontrolador?
def save(Cotacao cotacao) {
if (cotacao.hasErrors()) {
println "Erro no campo ${cotacao.errors.getFieldError('valor')}"
}
}
239

## Página 246

7.6. DataBinding CasadoCódigo
Simples:omecanismodevalidaçãoentraemação.Executandoafun ção
hasErrorsdasuaclassededomínio,épossívelverificarsehouvealgumerro
devalidação.Seretornarverdadeiro,jásabeoquepodeterocorrido.
Usandoafun ção getFieldErrordoatributo errorsdasuaclassede
domíniopassandocomoparâmetroonomedocampoépossívelchecaroque
aconteceu.Estaéumamaneirafácildelidarcomessetipodesituaç ão,com
umavantagembastantesimples:vocêjáiriafazeristonavalidaçãobásicadas
suasclassesdedomínio.
Masoleitordeveterobservadoquenesteexemplonãotoqueinobinding
comcamposdotipo Date,certo?
Lidando com datas
Háduasmaneirasdeselidarcomatributosdotipodata.Amaissimples
consisteemusaratag <g:datePicker>,querenderizaumcomponente
paraseleçãodedatasimilaraodaimagemaseguir:
Fig.7.10:Componentedatepicker
Ousodatagébastantesimples,talcomopodeservistonoformulárioa
seguirusadonocadastrodecotações:
<g:form action= "save" controller="cotacao">
240

## Página 247

CasadoCódigo Capítulo7. Acamadaweb:controladores
<label for="data">Data:</label>
<g:datePicker name="data" precision="day"/>
</g:form>
Oatributo nameiráidentificaronomedapropriedadedonossobean
quereceberáadatacomovalorfornecido,enquanto precisiondefineo
níveldeprecisãoquequeremosusarnaexecuç ãodobindingdenossatag.
Osseguintesvaloresencontram-sedisponíveis: year, month, day, hour,
minute, second.Quantomenoraunidadedemedidaselecionada,maior
seráonúmerodecamposusadosparacomportarofornecimentodadata.
Claro,nãoestamospresosàtag <g:datePicker>.Equandovocêqui-
serusarumcampotextualsimples,oumesmopassarumadatacomoparâ-
metrodeumaURLounocorpodeumarequisiç ãoHTTP?Hádoiscaminhos
aseguir.
O primeiro é simplesmente não fazer nada. Por padrão, o
Grails aceita datas que usem os seguintes formatos: yyyy-MM-dd
HH:mm:ss.S e yyyy-MM-dd’T’hh:mm:ss’Z. Se quiser, você
pode inclusive incluir os seus próprios formatos de data padro-
nizados. Como fazer isso? Basta adicionar uma chave de con-
figuração no arquivo grails-app/conf/Config.groovy:
grails.databinding.dateFormats, tal como no exemplo abaixo,
noqualincluoumaterceiraformataçãopadrão:
grails.databinding.dateFormats = ['MMddyyyy',
'yyyy-MM-dd HH:mm:ss.S',
"yyyy-MM-dd'T'hh:mm:ss'Z'"]
Semprequeobindingforexecutado,Grailsirátentaraconversãodo
campotextualcomumdosformatospresentesnestaconfiguraç ão. Are-
gradeformataçãodedatasusadaéapadrãodoJava, definidanaclasse
java.text.SimpleDateFormat. RecomendoquevocêleiaoJavaDoc
destaclasseparacompreendermelhorseufuncionamento[23].
Mastalvezvocêqueirafazeralgumacoisa.Quetalcustomizarodatabin-
dingparaumcampoespecíficodasuaclassededomínio? Issoéfeitocom
241

## Página 248

7.6. DataBinding CasadoCódigo
aanotação BindingFormat. Imaginequesejadonossointeressequeos
usuáriosdo ConCotdigitemasdatasdecotaçãonoformato dd/MM/yyyy.
Bastaalteraraclasse Cotacaoparaquefiquedestaforma:
import org.grails.databinding.BindingFormat
class Cotacao {
@BindingFormat('dd/MM/yyyy')
Date data
// restante omitido
}
Customizando a conversão de dados
Aproveitandooganchodobindingdedatas,vocêjásequestionoucomo
umtextocomo "1/1/2015"podeserconvertidoemumobjetodotipo
java.util.DatepeloGrails? Conseguimosfazerissograçasàpossibili-
dadedecustomizarmosoprocessodeligaç ão(binding).
Para expor esta funcionalidade, vamos implementar o nosso próprio
“binder”paradatas.Nossoexemploseráapenasumpoucodiferente.Ofor-
matodadatasempreseráprecedidocomoprefixo "data-"parasediferen-
ciardopadrãodoGrails.Aseguir,podemosvercomoficouaimplementaç ão
danossaclasse:
package concot.bind
import org.grails.databinding.converters.FormattedValueConverter
import java.text.SimpleDateFormat
class ExemploFormater implements FormattedValueConverter{
// Executa a conversão
def convert(value, String format) {
def formato = format.replaceAll("data-", "")
new SimpleDateFormat(format).parse(formato)
}
// O tipo de classe que o meu binder irá formatar
242

## Página 249

CasadoCódigo Capítulo7. Acamadaweb:controladores
Class getTargetType() {
java.util.Date
}
}
Afunção convertrecebedoisparâmetros: ovaloraserconvertidoe
astringqueidentificaoformatoaseraplicado. Seupapelésimplesmente
executaraconversãodeumastringparaumobjetoquedeveserdomesmo
tiporetornadopelafun ção getTargetType.
E como aplicamos isso em nossas classes de domínio oucommand
objects (nosso próximo assunto)? Simples: usando a mesma anotação
@BindingFormat:
class Cotacao {
@BindingFormat("data-dd/MM/yyyy")
Date data
}
Mas o trabalho ainda não acabou. Há um terceiro passo. Você
deve também declarar a nossa classe ExemploFormater como
um bean do Spring. Falaremos mais sobre isto no capítulo dedi-
cado aos serviços, mas já para adiantar, bastaria modificar o arquivo
grails-app/conf/spring/resources.groovyparaquefiquesimilar
aoexemploaseguir:
//Nome do bean (exemploConverter) e classe
exemploConverter concot.bind.ExemploFormater
7 .7 C ommand objects
Databindingvaialémdassuasclassesdedomínio. Hásituaçõesnasquais
vocêirácriarformuláriosmaiscomplexosquetalveznãoenvolvamqualquer
classededomínio. OquemefazlembrardodiaemqueGutochegouna
243

## Página 250

7.7. Commandobjects CasadoCódigo
DDLpedindoparaquefosseincluídoumformuláriodeenviodee-mailspara
nossosfornecedores...
Sabeoqueseriamuitolegal,Kico?Seno ConCothouvesseumformulário
noqualeupudesseenviarume-mailparaosfornecedores.
Comoassim,Guto?
Seguinte:euqueroalgomaisoumenosassim.Lánocadastrodeforne-
cedores,umapáginaquecontenhaosseguintescampos: ofornecedor,um
campoparaqueeucoloquemeunomeeoutronoqualeudigiteamensagem.
Aosubmeter,oformulárioenviariaume-mailparaofornecedor.Oqueme
diz?
Bacana:entãovouincluirumatributoamaisnaclasse Fornecedorpara
representarseue-mail.Enesteformuláriodeenviodemensagens,faltaum
campoamaistambémGuto,oe-mailparaoqualvocêdesejaqueofornecedor
enviearesposta,certo?
Perfeito,Kico!Temcomofazer?
Sóseforagora!
Nossoprimeiropassoéatualizarportantoaclasse Fornecedorparaque
fiquecomooseguinte:
class Fornecedor {
String nome
String email
String toString() {
this.nome
}
static constraints = {
nome nullable:false, blank:false, maxSize:128, unique:true
email nullable:false, blank:false, email:true
}
}
Reparequenestecasonãoénecessáriosalvaramensagemenviadano
bancodedados.Sendoassim,nãohárazãoalgumaparacriarmosmaisuma
244

## Página 251

CasadoCódigo Capítulo7. Acamadaweb:controladores
classededomínio.Noentanto,seriabacanasehouvesseumamaneirainte-
ressantedevalidarosdadosqueousuáriodigitanesteformulário.Algumas
validaçõessãonecessárias:
• Deveserselecionadoumfornecedor;
• Ousuáriodevefornecerume-mailválido;
• Algumamensagemdeveserdigitada.
Entraemaçãoo command object. Pensenelecomouma“classede
domínioquepossuiapenasvalidação”. Estetipodeobjetonãoépersistido,
nãoébuscadoemumbancodedados,nadadisto:apenasvalidaaentrada
dousuário.Ecomoimplementá-lo?Simples,bastacriarumaclasseGroovy
queimplementea trait grails.validation.Validateable. Criamos
umaclassechamada EnvioEmail,queseencontraarmazenadanodiretório
src/groovy/concotcujaimplementaçãopodemosveraseguir:
package concot
class EnvioEmail implements grails.validation.Validateable {
Fornecedor fornecedor
String email
String mensagem
static constraints = {
fornecedor nullable:false
email nullable:false, blank:false, email: true
mensagem nullable:false, blank:false
}
}
Seexcluíssemosatrait Validateabledestaclasse,elafacilmentepo-
deriaserconfundidacomumaclassededomínioconvencionaldoGrails.É
importantesalientartambémondesalvamosnosso command object.Lembre-
sequequalquerclassearmazenadaem grails-app/domainirágeraruma
classededomínio.
245

## Página 252

7.7. Commandobjects CasadoCódigo
Implementadonosso command object,opróximopassoéaimplementa-
çãodanossaprimeiraaction,responsávelporexporapáginadecomunicação:
class FornecedorController {
static scaffold = Fornecedor
def comunicacao() {
[fornecedores:Fornecedor.list(), mensagem:new EnvioEmail ()]
}
}
O arquivo GSP usado para a renderizaç ão (
grails-app/views/fornecedor/comunicacao.gsp) é exposto
emsuaformasimplificadaadiante:
<g:form action= "enviarMensagem">
<label for="fornecedor.id">Fornecedor</label><br/>
<g:select from="${fornecedores}" name="fornecedor.id" optionKey="id"/>
<br/>
<label for="email">E-mail:</label><br/>
<input type="email" name="email"/>
<br/>
<label for="mensagem">Mensagem:</label><br/>
<textarea name="mensagem">${mensagem.mensagem}</textarea><br/>
<input type="submit" value="Enviar"/>
</g:form>
Oresultadofinaléalgomuitoparecidocomodaimagem:
246

## Página 253

CasadoCódigo Capítulo7. Acamadaweb:controladores
Fig.7.11:Nossoformulário
Ecomoficaaactiondesubmissão?
class FornecedorController {
static scaffold = Fornecedor
// restante omitido
def enviarMensagem(EnvioEmail envio) {
envio.validate()
if (envio.hasErrors()) {
// Erro encontrado
flash.message = "Erro de validação"
render(view:"comunicacao",
model:[mensagem:envio,
247

## Página 254

7.8. Evitandoasubmissãorepetidadeformulários CasadoCódigo
fornecedores:Fornecedor.list()])
} else {
// Mensagem enviada (código omitido)
flash.message = "Mensagem enviada com sucesso"
render(view:'comunicacao')
}
}
}
Todososerrosdevalidaçãoficarãoarmazenadosnoatributo errorsdo
command object.Vocêpodeinclusiveiterarsobreestesexatamentecomofaria
sefosseumaclassededomíniopadrãocomovemosnoexemploaseguir:
def enviarMensagem(EnvioEmail envio) {
if (envio.hasErrors()) {
for (erro in envio.errors.allErrors) {
println erro
}
}
}
7 .8 E vitando a submissão repetida de formulá-
rios
Oformuláriodecomunicaçãocomfornecedoresfoiumsucessona DDL,de
talmodoqueacabousetornandoumadasprincipaisferramentasdecomu-
nicaçãodaempresa.Claro,todosucessonãovemdegraç aeumdosusuários
começouareclamarqueosistemaestavacomerros. Algunsfornecedores
estavamrecebendoduasvezesoMESMOe-mail.Como?
Simples:resultadodofamoso“dedinhotenso”.Emalgunsmomentosem
queo ConCotestavasobforteestresse,algunsusuáriosacidentalmentecli-
cavamrapidamenteduasvezessobreobotãodesubmissão.Aindabemque
estamosfalandodeGrailseasoluç ãodoproblemaébastantesimples:dois
passosresolvemoproblema. Oprimeiropassoconsisteemusaroatributo
useTokennatag <g:form>:
<g:form action="enviarMensagem" useToken="true">
248

## Página 255

CasadoCódigo Capítulo7. Acamadaweb:controladores
<%-- Conteúdo do formulário oculto --%>
</g:form>
Esteparâmetroincluiumnovoparâmetroemnossoformulário,umto-
ken,devaloraleatório,queseráusadoparaverificarasubmissãorepetida
dedados.Opróximopassoéaindamaissimples:bastamodificarlevemente
nossaaction enviarMensagem:
def enviarMensagem(EnvioEmail envio) {
withForm {
// submissão esperada
}.invalidToken {
// submissão duplicada detectada
}
}
Bastourefatorarlevementeocódigocolocandoaregradeenviodemen-
sagemdentrodoprimeiroblocodafun ção withFormeocódigoquelida
comasubmissãoduplicadadentrodobloco invalidToken. Bingo,pro-
blemaresolvido!
7 .9 U pload de arquivos
Conformeo ConCotviasuabasededadosaumentar,algunsusuárioscome-
çaramaenfrentardificuldadesnahoradeselecionaroitemcorretodeuma
cotação.Gutoachouqueseriaumaboaideiaincluirnestecadastroapossibi-
lidadedesubmissãodearquivosdeimagem.Porquenão?
Asoluçãomaissimplesconsisteemincluirumatributodotipo byte[]
naclassededomínio. Nestecaso,iríamosarmazenaroarquivosubmetido
dentrodoprópriobancodedadosemumcampodotipoBLOB.Paracome çar,
vamosfazerexatamenteissomodificandoaclasse Item,destaforma:
class Item {
String nome
249

## Página 256

7.9. Uploaddearquivos CasadoCódigo
byte[] imagem
String toString() {
this.nome
}
static belongsTo = [categoria:Categoria]
static constraints = {
nome nullable:false, blank:false, maxSize:128
categoria nullable:false
imagem nullable:true, maxSize:65536
}
}
Reparequejáincluímostambémumlimiteparaotamanhodoarquivo
quepodesersubmetido:65536bytes,ouseja,64Kb,oquenestecasoacredita-
mosserumtamanhoaceitável.Sevocêestiverusandoscaffoldingdinâmico,
comoestamosfazendoatéagoracom Itemnãoénecessáriofazernadamais.
Oformuláriodecadastrojávaiconterocampoparasubmissãodearquivos.
Vejaaimagem:
250

## Página 257

CasadoCódigo Capítulo7. Acamadaweb:controladores
Fig.7.12:Uploaddearquivo
Aosubmeteroformuláriocomumarquivodeimagem,estaautomatica-
menteseráarmazenadanoatributo imagemdaclasse Item.Oprópriodata
bindingdoGrailsresolveoproblemaparanós. Claro,ahistórianãoacaba
aqui,poisédenossointeresse“descartarnossoandaime”,certo?
Oprimeiropassoparatrabalharasubmissãodeformulárioséo...formu-
lário.Entraemaçãoatag <g:uploadForm>,queirá,narealidade,apenas
gerarumformuláriodotipo multipart,queéousadoquandosubmete-
mosarquivosnoprotocoloHTTP.Nossoformulárioparaocadastrodeitens
poderiaserportantoalgosimilaraocódigoaseguir:
<g:uploadForm action="save">
<label for="imagem">Imagem</label><br/>
<input type="file" name="imagem"/>
</g:uploadForm>
Resolvemosmetadedoproblema,agorabastavercomoobteroarquivo
apartirdanossaaction. Porbaixodospanos,Grailsusaumainterfacedo
251

## Página 258

7.10. Downloaddearquivos CasadoCódigo
Springchamada MultipartHttpServletRequest,quetornaomanuseio
deuploadumatarefatrivial.Duvida?
class ItemController {
def save(Item item) {
def arquivo = request.getFile('imagem')
if (arquivo.empty) {
// O arquivo é vazio. Isto é inválido
// trata o erro
}
// armazenamos o arquivo em um sistema de arquivos
arquivo.transferTo(new File('/arquivos/item/${item.id}'))
}
}
Oobjeto requestéumanovidade. Todocontroladorpossuiacesso
aesteobjeto, quenarealidadeéumainstânciadeumaconhecidainter-
facedaespecificaçãoservletdoJavaEE: HttpServletRequest.Afun ção
getFileretornaoobjetoquerepresentaoarquivosubmetido.Mostramos
aquiousodasduasfun çõesmaisusadas:
•empty retorna truecasooarquivosubmetidosejavazioounulo.
•transferTo recebe um objeto do tipo java.io.File
Masaindanãoacabamos...
7 .10 D ownload de arquivos
Odownloaddearquivospodeocorrer,comosempre,deduasmaneiras. A
maissimpleséaquelanaqualnãodefinimosumnomeparanossoarquivo:
apenasenviamosumarraydebytesparaoclientedaaplicaç ãoatravésdeuma
URL.
Éumaexcelentesoluçãoparaocasodasimagensquesubmetemospara
nossaclassededomínio Item. Entraemaçãomaisumatributodispo-
nível em todos os controladores:response, que na realidade é uma
instância de outra famosa interface da especificação Servlet do Java EE,
HttpServletResponse.
252

## Página 259

CasadoCódigo Capítulo7. Acamadaweb:controladores
Voltandoao ConCot,poderíamosescreverumaactionsimilaràseguinte:
class ItemController {
def imagem(long id) {
Item item = Item.get( id)
response.outputStream << item.imagem
}
static scaffold = Item
}
Ooperador <<foisobrescritoemtodostreamdesaída.Doladodireito
éfornecidooarraydebyteseesteserátransmitidoaocliente. Emnossos
arquivosGSP,obterestasimagensérelativamentesimples.Bastafazercomo
noexemploaseguir:
<img src="${createLinkTo(controller:'item', action:'imagem', id:item.id)}"
Oatributo srcdatag <img>apontaráparaanossaaction,queatu-
arácomosefosseumacessodiretoaoarquivo. Umasoluç ãobastantesim-
ples. Afunção createLinkTonarealidadeéumatagpresentenabibli-
otecadoGrails. Falaremosmaissobreelamaistarde. Oimportanteneste
pontoéapenassalientarqueteríamosumaURLsimilara http://localhost:
8080/concot/item/imagem/3,porexemplo,quebaixariaaimagemparaona-
vegador.
Nossa primeira versão de download foi bastante rudimentar. Nor-
malmente, é interessante fornecer mais alguns atributos do conteúdo
baixado para nossos clientes como, mimetype, nome do arquivo e
mesmoseutamanho. Bastachamarmososmétodosdaprópriainterface
HttpServletResponse.
class ItemController {
def imagem(long id) {
Item item = Item.get( id)
// qual o tipo do arquivo baixado?
response.setContentType('image/png')
// definimos o nome do arquivo
response.setHeader('Content-disposition', 'attachment;filename=ima
253

## Página 260

7.11. Filtrandorequisições CasadoCódigo
// o tamanho do arquivo baixado
response.setHeader('Content-Length', item.imagem.length)
// finalmente, o download
response.outputStream << item.imagem
}
}
Éinteressanteobservarquequantomaiorforonúmerodecabe çalhos
HTTPfornecidosduranteodownload,maisfácilsetornaoprocessodeob-
tençãodedadosporpartedocliente. Umalistacompletadoscabe çalhos
HTTPpodeserobtidanaWikipédiaparaconsulta[33](sim,euseiqueWi-
kipédianãoéumafonteconfiável,masestalistaébemcompleta).
7 .11 Filtrando requisições
Atéestemomento,nossosistema ConCotnãopossuiqualquermecanismode
segurança.Qualquerfuncionárioda DDL Engenhariapodelivrementeaces-
sarnossocadastrodecotações.Nãoseriainteressante(paranãodizerobri-
gatório)incluirmosalgummecanismodeautenticaçãoemnossoprojeto?
Porenquanto,implementaremosummecanismodeautenticaç ãoextre-
mamenterudimentar(paranãodizerineficiente).Nossoobjetivonãoétratar
dasegurançadenossasaplicaçõesGrailsnestecapítulo,massimapresentar
maisalgunsconceitosfundamentaisrelacionadosaofuncionamentodoscon-
troladores.
Estenossomecanismodeautenticaçãoterátrêscomponentes:umanova
entidaderepresentandonossosusuários,umformuláriodeautenticaçãoeum
mecanismodefiltragemderequisições.Ousuárioquefornecerascredenci-
aiscorretasiráteracessoatodososdados,poisnãoiremosimplementaraqui
ummecanismodeautorização.Nossoobjetivonestemomentoéapenasapre-
sentaromecanismodefiltragemderequisiçõesdoGrails.
Aclassededomínio Usuarioébastantesimples:
O “boot” do Grails
class Usuario {
254

## Página 261

CasadoCódigo Capítulo7. Acamadaweb:controladores
String login
String senha
static constraints = {
login nullable:false, blank:false, maxSize:16
senha nullable:false, blank:false, maxSize:312
}
}
Reparequequandodissequenossomecanismodeautenticaç ãoerasim-
pleseunãoestavamentindo,poisnóssequeriremossalvarasenhadenossos
usuáriosencriptadasnobancodedados.Comotodosistemaprecisaterpelo
menosumusuário,vamoscriá-lonomomentoemqueaaplicaçãoéiniciada.
Paratal,usamosoarquivo grails-app/conf/BootStrap.groovyque,
apósnossamodificação,ficouassim:
import concot.*
class BootStrap {
def init = { servletContext ->
Usuario.findOrSaveByLoginAndSenha("admin", "senha")
}
def destroy = {
}
}
Nobloco initincluímosasinstruçõesquedesejamosquesejamexecu-
tadasquandonossaaplicaçãoéiniciadapeloservletcontainer.Éolocalideal
paracriarmosnossousuárioadministradorpadrão,razãopelaqualocriamos
aliusandonossofinderdinâmico.
Ah,eaquelebloco destroy? Eleéexecutadoquandonossaaplicação
éfinalizadapelocontainer. Umblocobastanteútilquandoqueremoslim-
parqualquerbagun çaquetenhasidogeradapornossaaplicaç ãodurantesua
execução.
255

## Página 262

7.11. Filtrandorequisições CasadoCódigo
Sessão de usuário e nossa autenticação
Agoraquejátemospelomenosoprimeirousuáriocadastradoquandoo
sistemaéiniciado,nossopróximopassoconsistiráemimplementaromeca-
nismodeautenticação.Paraisso,primeiroiremoscriarumnovocontrolador
chamado Autenticacao,cujaimplementaçãoébemsimples:
class AutenticacaoController {
def autenticar(Usuario usuario) {
def registro = Usuario.findByLoginAndSenha(usuario.login, usuario.s
if (registro) {
session['usuario'] = registro
redirect(controller:'cotacao')
} else {
flash.message = "Acesso negado"
redirect(uri:'/')
}
}
}
Ofuncionamentoéextremamentesimples.Verificamosseexisteumre-
gistrodeusuáriocomologinesenhapassadoscomoparâmetroaocontrola-
dor.Existindo,redirecionamosnossoclienteparaaactiondefaultdocontro-
lador cotacao;nãohavendo,oredirecionamentoseráfeitoparaapágina
inicialdoprojeto.
Aprimeiranovidadedizrespeitoaomodocomolidamoscomasessão
dousuário. Todocontroladorpossuiumatributochamado session,que
funcionacomoummapa.Osobjetosqueinserirmosemseuinteriorirãolá
permanecerduranteotempodevidadasessãodousuário. Nonossocaso,
apenasincluímosaquiainstânciade Usuarioqueencontramosnobanco
dedados.
Armazenarousuárionasessãoéalgofundamentalemnossomecanismo
desegurançacomoveremosmaisàfrente. Asegundanovidadeéoescopo
flash.Eleconsisteemumconjuntodevariáveisdeduraç ãoextremamente
curta:eleécapazdemanterosvaloresarmazenadosemsiapenasnarequi-
siçãocorrenteenapróxima,oqueéidealparaonossocaso,poisqueremos
256

## Página 263

CasadoCódigo Capítulo7. Acamadaweb:controladores
informaràpessoaquetentouseautenticarnosistemaqueseuacessofoine-
gado.
Precisamostambémmodificarapáginainicialdo ConCot. Estaagora
possuiapenasumformuláriodeautenticaçãocujaimplementaçãopodeser
vistaaseguir:
<h1>ConCot</h1>
<g:form action="autenticar" controller="autenticacao">
Login:<br/>
<input type="text" name="login"/><br/>
Senha:<br/>
<input type="password" name="senha"/><br/>
<input type="submit" value="Entrar"/>
</g:form>
Nossapáginainicialpossuiagoraumaspectosimilaraodaimagem:
Fig.7.13:Formuláriodeautenticação
Finalmente, o filtro
Oúltimocomponentedonossodispositivodeseguran çaéofiltro.Filtros
sãoclassesquenospermiteminterceptartodasasrequisiçõesquechegamaos
257

## Página 264

7.11. Filtrandorequisições CasadoCódigo
nossoscontroladores.Novamente,devemserseguidasalgumasconven ções
paraquepossamosimplementarnossosfiltros.
• Aclassedevesercriadanodiretório grails-app/conf;
• AclassedevepossuirosufixoFiltersemseunome.
O filtro de acesso doConCot encontra-se implementado no arquivo
grails-app/conf/concot/AcessoFilters.groovy.Vamosescrevê-
lojuntosparaquevocêentendaofuncionamentodestepoderosorecursoofe-
recidopeloGrails.Aprimeiraversãodonossofiltropodeservistanalistagem
adiante:
package concot
class AcessoFilters {
def filters = {
}
}
Deveserdeclaradoumbloco filtersemtodaclassedefiltro.Casoes-
tejaausente,nossaaplicaçãosimplesmentenãoseráiniciada.Emseuinterior
équedeclaramosasregrasdeinterceptaçãoderequisições.Emnossocasohá
apenasuma:
class AcessoFilters {
def filters = {
acesso(controller:'*', action:'*' ) {
// preencheremos aqui mais tarde
}
}
}
Nossaprimeiraregrasechama acessoeosparâmetrosquedeclaramos
emseuinteriornosdizemoquedeveserinterceptado.Nestecaso,estamosin-
terceptandotodasasactionspertencentesaqualquercontrolador,razãopela
qualparaosdoisparâmetrospassamoscomovalorumasterisco. Masvocê
podesermuitomaisespecífico.Vejaalgunsexemplos:
258

## Página 265

CasadoCódigo Capítulo7. Acamadaweb:controladores
// Todas as actions do controlador cotacao
acesso(controller:'cotacao', action:'*')
// Apenas a action save do controlador cotacao
acesso(controller:'cotacao', action:'save')
// Talvez todas as actions save de qualquer controlador
acesso(controller:'*', action:'save')
Masnãotemosapenasosparâmetros controllere action.Seguea
listadetodososoperadoresquepodemosusarparafiltrarnossasrequisições:
•controller onomedocontrolador.Porpadrãoseuvaloré‘*’caso
nãooincluanadefinição.
•controllerExclude no caso de uma regra que se apli-
que a todos os controladores menos algum. Exemplo:
controllerExclude:’item’. Todos os controladores menos
item.
•action onomedaactionaserinterceptada. Seuvalorpadrãoé‘*’
casonãooforne çaemsuaregra.
•actionExclude omesmoque controllerExclude,sóquerela-
cionadoaactions.
•regex aplicadoaURLs.
•uri Aplicadoaumendere ço.Porexemplo: uri:/item/**.
•uriExclude Omesmoque controllerExclude,sóqueaplicado
aURIs.
•invert Inverteasuadefiniçãodeinterceptação.
Mas não basta saber o que interceptar: você também precisa saber
quando.PorestarazãoGrailsnosfornecetrêstiposdefiltros:
•before delongeomaiscomum,noqualvocêinterceptaarequisiç ão
antesqueestaexecuteasuaaction.
259

## Página 266

7.11. Filtrandorequisições CasadoCódigo
•after apósaexecuçãodaaction
•afterView apósarenderizaçãodaresposta
Emnossocaso,iremosimplementarumfiltrodotipo before,sendo
assimnossaimplementaçãoficarádestaforma:
class AcessoFilters {
def filters = {
acesso(controller:'*', action:'*' ) {
before = {
}
}
}
}
Masvocêtambémpodeincluirdentrodeumamesmaregramaisdeum
tipodefiltro,talcomonoexemploaseguir:
class AcessoFilters {
def filters = {
acesso(controller:'*', action:'*' ) {
before = {
}
after = {
}
afterView = {
}
}
}
}
Bom,mascomoficounossofiltronofinaldascontas?
260

## Página 267

CasadoCódigo Capítulo7. Acamadaweb:controladores
class AcessoFilters {
def filters = {
acesso(controller:'*', action:'*') {
before = {
if (session['usuario']) {
return true
} else {
if (controllerName == null || actionName == 'autent
return true
}
redirect(uri:'/')
}
}
}
}
}
Seofiltroretornarovalor true,aactionseráexecutadacomosenada
tivesseocorrido. Nossaregradeacesso,comopôdeservisto,ébastantees-
partana:seousuárioestiverautenticado(houveralgonachave usuarioda
sessão),todooacessoéliberado.
Orealmenteinteressanteocorrequandoousuárionãoestáautenticado
nosistema.Háumasériedevariáveisqueseencontramosdisponíveispara
onossofiltro,enósusamosalgumas.Avariável controllerNameindica
onomedocontroladordarequisiçãocorrente.Nocasodapáginainicialdo
sistema,nãohánenhum,poristoretornamos true(hádeexistirumponto
deentradanosistemaafinaldecontas).
Jáasegundavariáveldisponibilizadaé actionName,queidentificao
nomedaaction.Aúnicaactionlivreemnossosistemaé autenticar,ra-
zãopelaqualiremosretornar truetambémnestacondição. Finalmente,
nãopassandoporesterápidoteste,simplesmenteredirecionamosonossovi-
sitanteparaapáginainicialdosistemacasotenteacessaralgumaURLdo
sistemaaquenãopossuaacesso.
Sobreasvariáveisdisponíveisparaofiltro,seguealista:
261

## Página 268

7.11. Filtrandorequisições CasadoCódigo
•request oobjeto HttpServletRequestdaAPIServlet
•response oobjeto HttpServletResponsedaAPIServlet
•session asessãodousuário
•servletContext oobjeto ServletContextdaAPIServlet
•flash ocontextoflash
•actionName onomedaactioninterceptada
•controllerName onomedocontroladorinterceptado
•applicationContext oobjeto ApplicationContext
Vocêtambémtemacessoadoismétodosimportantes:
•redirect parafazerosredirecionamentosnecessários.
•render pararenderizarrespostascustomizadasemseusfiltros.
Mas ainda podemos filtrar ainda mais
Nestemomento,talvezvocêachequenossotrabalhoestácompleto,mas
verdadesejadita,aindanãoestá.Faltaumpequenodetalhe.Imaginequeal-
guémtenteacessaraseguinteURL: http://localhost:8080/concot/autenticacao/
autenticar?login=admin&senha=senha. Apessoaconseguiráseautenticarno
sistema,eaindavemosasenhanabarradeendere çosdonavegador.Como
resolveristo?LimitandoquaismétodosHTTPpossuemacessoàsnossasac-
tions!
Entraemaçãooatributo allowedMethodsemnossocontrolador.Va-
mosincluí-loemnossaclasse AutenticacaoControllerparaquefique
similaraocódigoaseguir:
class AutenticacaoController {
static allowedMethods = [autenticar:'POST']
}
262

## Página 269

CasadoCódigo Capítulo7. Acamadaweb:controladores
Agoraascredenciaisdosnossosusuáriosserãofornecidasapenasatravés
dométodo POSTHTTP,ouseja,atravésdeformuláriosapenas. Problema
resolvido.Sevocêquiser,épossíveldefinirmaisdeummétodoHTTPpara
umamesmaaction.Bastaquevocêincluacomovaloraestaumalista:
static allowedMethods = [autenticar:'POST', sair:['GET','DELETE' ]]
7 .12 E scopo do controlador
OcontroladorGrailsnarealidadeéumbeandoSpring.Veremosmaissobre
beanseescoposquandofalarmossobreserviços 9.2,poréméimportanteque
vocêentendaoessencialdesteconceitoagoracomoobjetivodeotimizaro
consumoderecursoscomputacionaisdoseuprojetoetambémevitaralguns
problemas.
Quandofalamosdeescopo,estamosnosreferindo,essencialmente,ao
tempodevidadeumainstância.Porquantotempodeveráexistirainstância
deumobjetodotipo CotacaoController,porexemplo?Otempodeuma
requisição?Asessãodeumusuário?Todootempodevidadaaplicaç ão?
Nocasodoscontroladores,hásuporteparatrêstiposdeescopo:
•prototypeéopadrãocasoaaplicaçãonãosejaconfiguradaparaum
escopodiferente.Umanovainstânciadocontroladorserácriadaacada
requisiçãoefinalizadaquandoseuprocessamentochegaraofim.
•session ainstânciadocontroladorexistiráenquantodurarasessão
dousuário.
•singletonainstânciaécriadajuntocomainicializaçãodaaplicação
eserámantidaenquantoestaestiveronline.
Sevocêquiseralteraroescopopadrãodetodososcontroladoresdasua
aplicação,bastaincluirachave grails.controllers.defaultScopeno
arquivo grails-app/conf/Config.groovy:
//Mudando o padrão para session
grails.controllers.defaultScope='session'
263

## Página 270

7.12. Escopodocontrolador CasadoCódigo
É importante observar que na configuração padrão do arquivo
Config.groovy a chave grails.controllers.defaultScope
jáestávindoháalgumtempocomovalor singleton.
Tambémépossívelmudaroescopodeapenasumcontrolador.Paratal,
bastaincluiroatributoestático scopeemsuadefinição:
class ItemController {
// Mudando o escopo para prototype
static scope = "prototype"
}
Cuidado com o estado
Fig.7.14:Atençãoredobrada!
Oescopo singletonéoidealseseuobjetivoforminimizaroconsumode
memóriadosistema,vistoqueserámantidaumaúnicainstânciadoseucon-
troladordurantetodootempodevidadaaplicaç ão.Entretanto,muitocui-
dadodeveserlevadonaimplementaçãodosseuscontroladores.
Eviteaomáximoapresen çadeestadoemseuscontroladoresaoadotar
esteescopo. Que estado?Simples,atributosemseucontroladorquenãosejam
actions,equepossamseralteradosdeacordocomasrequisiçõesqueeste
possareceber.
Preferencialmente,implementeseuscontroladoressempresemqualquer
atributoquenãosejaumserviço 9:idealmentecontroladoresdeveriampos-
suirapenasactions.
Casosejanecessárioincluirestadoemseuscontroladores,optepeloses-
copos scopeou session,evitandoassimqueumusuárioacidentalmente
obtenhaacessoaoestadodeoutro.Lembre-se:aplicaçõeswebsãoessencial-
menteaplicaçõesconcorrentes!
264

## Página 271

CasadoCódigo Capítulo7. Acamadaweb:controladores
7 .13 E scopo de dados
Assimcomoháescopoparacontroladores,hátambémescopoparadados.
Vimosalgunsnestecapítulo: flash, sessione params. Tratam-sede
estruturasdotipomapaqueusamosparaarmazenaralgumasvariáveisfor-
necidaspelousuárioemsuasrequisiçõesoudefinidaspeloprogramadorem
seuscontroladoresoufiltros.
Suaprincipalfun çãoédefinirotempodevidadevariáveis.Vocêjásabe
comotrabalharcomestasestruturas,dadoquevimosissoocapítulointeiro.
Oquetalveznãoconhe çasãoasdefiniçõesformaisdetodososescoposdis-
poníveisaoprogramador:
•params osparâmetrosenviadosaocontrolleratravésdasrequisições.
•session asessãodousuário.
•flashumescopoquearmazenaasvariáveissomentedurantearequi-
siçãocorrenteeapróximaparaummesmousuário.
•servletContext variáveisqueseencontramdisponíveisdurante
todootempodevidadaaplicaç ão.Usecomcuidadoesteescopo,pois
esteacabasetornandoumaespéciede“variávelglobal”dentrodoseu
projetoweb.
•request armazenavariáveisapenasduranteotempodevidadare-
quisiçãocorrente.
Fig.7.15:Atençãoredobrada!
Aolidarmoscomescopos,oleitordevesempreselembrardoquedisse
agoraapouco: uma aplicação web é essencialmente uma aplicação concor-
rente.Vocêteráotempointeiromaisdeumusuárioacessandoumamesma
265

## Página 272

7.13. Escopodedados CasadoCódigo
URLourecursoaomesmotempo.Sendoassim,tenha máximo cuidadocom
oescopo servletContext.Sóincluavaloresnesteescopoquesejamimu-
táveisduranteotempodevidadaaplicação,dadoquesãoinformaçõescom-
partilhadasportodososusuáriosdosistema.
266

## Página 273

Capítulo8
Acamadaweb:visualização
GSP(Groovy Server Pages)é AcamadadevisualizaçãooferecidapeloGrails.
Nadocumentaçãooficialéditoquefoifeitapensandoprogramadoresfami-
liarizadoscomtecnologiascomoJSPeASP,masacreditoquealguémacos-
tumadocomPHPsesentiráemcasacomoquemostrareiaqui. Digoisso
porexperiênciaprópria,poisjáconstateiqueprogramadoresPHPcostumam
gostarbastantedoGrails.Esperoque,casovocêvenhadoPHP,estesejaseu
casotambém.:)
SevocêjáprogramouemJSP,vaisesentirbastantealiviadonestepri-
meirocontatocomGSP,jáqueelenoslivradeumasériedeburocraciasa
queestenosfor ça,porexemplo,anecessidadededeclararmosnossastags,ou
mesmodeusarmosnossastagsapenascomosefossemtags,comoveremos
nestecapítulo.

## Página 274

8.1. Oessencial CasadoCódigo
8.1 O essencial
VocêcriaseusarquivosGSPexatamentecomofariaseestivessetrabalhando
comumapáginaHTMLconvencional,oquetornaatecnologiaumaexcelente
alternativaparaosmembrosdaequipequenãotrabalhamdiretamentecom
programação.OarquivoaseguiréumGSPperfeitamenteválido:
<!DOCTYPE html>
<html>
<head>
<title>GSP ou HTML?</title>
</head>
<body>
<h1>Apenas o HTML que você já conhece</h1>
<p>Designers adoram!</p>
</body>
</html>
Nãoéprecisodeclararbibliotecasdetag(tag libraries)ouincluirdireti-
vascomonocasodoJSP,noqualestaéumatarefapraticamenteobrigatória
namaiorpartedasvezes.Comovimosnocapítulosobrecontroladores 7,a
escolhadoGSPaserrenderizadopodesedartantoporconven çõesquanto
peladefiniçãoexplícitadoarquivopelocontrolador.Ointeressanteévocêter
emmenteque jamaisessesarquivosserãorenderizadosdiretamenteporuma
URL,apenasatravésdecontroladores,bibliotecasdetagoutemplates(deque
falaremosarespeitomaisàfrente).
Scriptlets
Atecnologiacome çaaficarinteressantejustamentequandofalamosso-
breorecursocujousoéomaisdesencorajado: scriptlets!Scriptletssão,
comoopróprionomejádiz,pequenosscripts(preferencialmente)quevocê
podeembutiremseusarquivosGSP.Idealmente,suaspáginasdevemsersim-
plesosuficientedetalmodoqueesterecursonãosejausado,mascasoseja
realmenteinevitável...use-ocomextremamoderação.
DeclararumscriptletésimplesebastantefamiliaraprogramadoresJSP:
bastaescrevê-losentre <% e %>talcomonoexemploaseguirreferenteao
268

## Página 275

CasadoCódigo Capítulo8. Acamadaweb:visualização
arquivo scriptlet.gsp.Oquedigitamosemseuinterior?CódigoGro-
ovy,éclaro!
<!DOCTYPE html>
<html>
<head>
<title>GSP ou HTML?</title>
</head>
<body>
<h1>Apenas o HTML que você já conhece</h1>
<p>Designers adoram!</p>
<%
// Declaro uma variável chamada "data" aqui
def data = new Date()
%>
<p>A propósito, agora é <%= data %></p>
</body>
</html>
Claro, a página não pode ser acessada diretamente, sendo as-
sim criei um controlador apenas para testar o recurso, que se chama
VisualizacaoController.
class VisualizacaoController {
def scriptlet() { }
}
EaoacessaraURL http://localhost:8080/concot/visualizacao/scriptletoque
obtemos?
269

## Página 276

8.1. Oessencial CasadoCódigo
Fig.8.1:Scriptlets!
Seuscriptlet,claro,podesermuitomaiscomplexoqueodesteexemplo,
falaremossobreistodaquiapouco,masointeressantenestemomentoéo
trechoquesalientoaseguir:
<p>A propósito, agora é <%= data %></p>
Entre <%= e %>,éincluídaumaexpressãoqualquer(quepodeser
tambémumavariável,comofiznesteexemplo).Oresultadoseráembutido
narenderizaçãofinaldapágina,masháumamaneiramaisinteressantedese
obteromesmoresultado:
<!DOCTYPE html>
<%
// Declaro uma variável chamada data, aqui
def data = new Date()
%>
<%-- Que tal uma expressão Groovy? --%>
<p>A propósito, agora é ${data}</p>
BastaincluirsuaexpressãoGroovyentre ${e }.Estaéinclusiveama-
neirarecomendadadeseincluirexpressõesemseusGSP,poisémuitomais
simpleselheafastará(aomenosemteoria)dosscriptlets.Vocêtambémpode
implementarloopsoucondicionaiscomGSPdeumaformamuitoparecida
comoquefazemosemJSPouPHP:
270

## Página 277

CasadoCódigo Capítulo8. Acamadaweb:visualização
<h1>Um loop com GSP</h1>
<%
def lista = concot.Categoria.list()
for (item in lista) {
%>
<h2>${item.nome} ( ${item.id} )</h2>
<%
}
%>
Cujoresultadodurantearenderizaçãopodeservistoaseguir:
Fig.8.2:Aplicandoloops
Claro,códigosimilartambémpoderiaserfeitousandocondicionaissem
problemaalgum:
<h1>Um loop com GSP</h1>
<%
def lista = concot.Categoria.list()
for (item in lista) {
/* Renderizaria apenas aqueles com id
maior que 1 */
if (item.id > 1) {
%>
<h2>${item.nome} ( ${item.id} )</h2>
<%
}
}
%>
271

## Página 278

8.1. Oessencial CasadoCódigo
ComentáriostambémpodemserincluídosemarquivosGSP.Estesfun-
cionamexatamentecomofaríamosemarquivosJSP,ouseja,estarãovisíveis
apenasnocódigo-fonte,enãodurantearenderizaç ão.Comofazemosisto?
<%-- Comentário com uma linha --%>
<h1>Um loop com GSP</h1>
<%
def lista = concot.Categoria.list()
for (item in lista) {
%>
<h2>${item.nome} ( ${item.id} )</h2>
<%
}
%>
<%--
Um comentário
com mais de uma
linha.
--%>
Tudooqueestiverentre <%--e --%>seráignoradopelocompilador
GSPemtempodeexecução.
Depurando GSP
Apropósito,arquivosGSP,assimcomoJSPcostumamoferecerdesem-
penhosuperiorpelofatodeseremcompiladosantesdeseremexecutados.
Haverámomentos(torçoparaqueosseussejamextremamenteraros),con-
formesuaspáginassetornammaiscomplexas,quevocêterádificuldadeem
entenderoquerealmenteestáocorrendoemseuinterioroumesmoimpe-
dindoumdesempenhoexcelente.UmrecursobastanteinteressantenoGSP
éapossibilidadedepodermosvisualizar,apenasnoambientededesenvolvi-
mento,ocódigo-fontequeégeradopelocompilador.
Como fa ço isso?. Simples, apenas adicione o parâmetro
showSource=true ao final da sua URL, tal comohttp://localhost:
8080/concot/visualizacao/scriptlet?showSource=true. Oresultadoéarenderi-
zaçãodocódigo-fontenajaneladoseunavegadorcomopodeservistoa
272

## Página 279

CasadoCódigo Capítulo8. Acamadaweb:visualização
seguir:
Fig.8.3:UsandooparâmetroshowSource
8.2 T ags customizadas
Tagscustomizadassãoumasoluçãodecomponentizaçãoparaacamadade
visualização. Comoveremosnestase ção,omodocomoGSPlidacomeste
recursoétãosimplesquantoasintaxeGSPqueacabamosdeveremuitomais
fácilqueomodocomoestamosacostumadosatrabalharcomJSP:nãoépre-
cisoincluirdeclaraçõesdeimportaçãonotopodasuapágina,tudooquevocê
precisafazeréusá-las.
GSPjávemcomumabibliotecadetagspadrãocujoprefixoé g:.Acre-
ditoqueamelhormaneiradeapresentarastagscustomizadasavocêépri-
meiroapresentarasfundamentaispara,logoemseguida,implementarasnos-
saspróprias tag libraries.
Renderização condicional
Tagscondicionaisdefinemoquedeveráserrenderizadoaoclientede
acordocomumacondiçãobooleana. GSPnosfornecealgumastagspara
isso,sendoamaisusadasemsombradedúvidas <g:if>talcomovemos
noexemploaseguir:
<g:if test="${1 + 2 < 4}">
<p>Sim, 1 + 2 é 3, que é menor que 4</p>
</g:if>
273

## Página 280

8.2. Tagscustomizadas CasadoCódigo
Oatributo testrecebecomoparâmetroumaexpressãoGroovyque,se
retornarverdadeiro,irárenderizarseuconteúdoembarcado(tambémcha-
madode“corpo”,obodydatag).Masestenãoéoúnicoatributoaceitopor
<g:if>: outrobastanteútildurantedesenvolvimentoé env,querecebe
comoparâmetroonomedoseu environment,oquepossibilita,porexemplo,
exporinformaçõesdedepuraçãoapenasnoambientededesenvolvimento
comonoexemploaseguir:
<g:if env="development">
<p>Informações úteis ao desenvolvedor apenas</p>
</g:if>
Sabemparaqueoatributo envtambémébastanteprático? Paraain-
clusãodecódigodemarcaç ãodeterceirosquesósejainteressanteserren-
derizadoemproduçãocomo,porexemplo,contadoresouanúnciosemsua
página.
<g:if env="production">
<%-- Código do seu contador de acessos --%>
</g:if>
Temostambématag <g:else>quenospermiterenderizarconteúdo
casodeterminadacondição não tenhasidoatendida. Estasempredeveser
incluídalogoapós </g:if>ou </g:elseif>.
<g:if test="${1 + 2 < 2}">
<p>A matemática enlouqueceu!</p>
</g:if>
<g:else>
<%-- Este bloco será renderizado --%>
<p>Ainda há sanidade matemática</p>
</g:else>
Tambémpodemoscontarcom <g:elseif>,quefuncionaexatamente
como <g:if>:aúnicadiferen çaestánofatodequenospermitetratarum
númeromaiordecasosdurantearenderizaçãocondicional.
<g:if env="production">
<p>Ambiente de produção</p>
274

## Página 281

CasadoCódigo Capítulo8. Acamadaweb:visualização
</g:if>
<g:elseif env="development">
<p>Ambiente de desenvolvimento</p>
</g:elseif>
<g:else>
<p>Nem produção nem desenvolvimento, mas sim
${grails.util.GrailsUtil.getEnvironment()}</p>
</g:else>
Oprimeiroblocoqueatenderàcondiç ãoseráorenderizado. Aclasse
grails.util.GrailsUtilfazpartedaAPIpadrãodoGrailsefoiusada
paranosretornaremtempodeexecuçãoqualo environmentcorrentedaapli-
cação.
Iterações
Emdiversosmomentos,énecessárioquevocêiteresobreumacole ção
deitensouexecutealgumloopenquantodeterminadacondiç ãosemostrar
verdadeira.Lembradapáginadelistagemgeradapelo scaffoldingdoGrails?
Fig.8.4:Listagemdecategorias
Elaéescritausandoatag <g:each>,talcomonoexemploaseguir:
275

## Página 282

8.2. Tagscustomizadas CasadoCódigo
<g:each in="${categoriaInstanceList}" status="i" var="categoria">
<tr class="${(i % 2) == 0 ? 'par' : 'impar'}">
<td>
<g:link action="show" id="${categoria.id}">${categoria.nome}</g:link>
</td>
</tr>
</g:each>
Ocorpodatagserárenderizadoenquantoaindahouveritensaseremper-
corridosnacole çãoquepassamoscomovaloraoparâmetro in(parâmetro
obrigatório).Jáoparâmetro vardefineonomedavariávelquerepresentao
itemcorrenteemnossaiteração.Outroatributobastanteútilé status,que
defineonomedavariávelquearmazenaráaposiçãocorrentedoitemdentro
daiteraçãoequepodeserusadopara,porexemplo,construiroefeitolistrado
usadonarenderizaçãodanossalistagem.
Outratagquepodeserusadaparalidarcomiteraçõesé <g:while>,que
possuiumúnicoparâmetro: testque,severdadeiro,irárenderizarocorpo
datag.Aseguir,mostrocomoexporumacontagemusandoesterecurso:
<% corrente = 0 %>
<g:while test= "${corrente < 10}">
<p>O valor corrente é ${corrente}</p>
<% corrente++ %>
</g:while>
Fig.8.5:Aten çãoredobrada!
Muitocuidadocom <g:while>: aoescreverseucódigo,certifique-se
dequeacondiçãodefinalizaçãodoloopchegaráaumvalorfalsoemalgum
momento.Ignoraressefatopoderágerarumloopinfinitoquepossivelmente
consumirátodososrecursoscomputacionaisdoseuservidor.
276

## Página 283

CasadoCódigo Capítulo8. Acamadaweb:visualização
Definição de variáveis
Jádefinimosalgumasvariáveisemnossaspáginasantes,mascomolhe
recomendeinoiníciodestecapítulo,devemosevitarousodescriptlets. A
equiperesponsávelpelodesenvolvimentodoGrailsconcorda,razãopelaqual
criouatag <g:set>.
Estatagpossuidoisparâmetrosobrigatórios: var,quedefineonomeda
variável,e value,quedefiniráoseuvalor.Nossoúltimoexemplopodeser
facilmentereescritousandoestatag:
<g:set var="corrente" value="${0}"/>
<g:while test= "${corrente < 10}">
<p>O valor corrente é ${corrente}</p>
<g:set var="corrente" value="${corrente++}"/>
</g:while>
Outroparâmetrointeressantepresentenestatagé scope,quenosper-
mitearmazenaravariávelemqualquerumdosescoposdedados 7.12que
vimosnocapítulosobrecontroladores.Sendoassim,sevocêquiserarmaze-
naralgumvalornasessãodousuáriobastausaratagtalcomonoexemploa
seguir:
<g:set var="autorDesteLivro"
value="Henrique Lobo Weissmann"
scope="session"/>
Links
Umatagquevocêcomcertezaviusendousadanocapítulosobrecon-
troladores7foi <g:link>,querenderizanasuapáginaumatag <a>con-
tendoaURLcorretaqueapontaráparasuaactionalvo.Amelhormaneirade
apresentá-laéusando-a,sendoassim,vamosaalgunsexemplos:
<%--
Para gerar...
<a href="http://localhost:8080/concot/cotacao">Cotações</a>
--%>
<g:link controller="cotacao">Cotações</g:link>
277

## Página 284

8.2. Tagscustomizadas CasadoCódigo
<%--
Para gerar
<a href="http://localhost:8080/concot/cotacao/create"> Criar</a>
--%>
<g:link controller="cotacao" action="create">Criar</g:link>
Fig.8.6:Aten çãoredobrada!
Lembre-sequeocontextodasuaaplicaç ãoirávariardeacordocomo
seuenvironment.Sendoassim,semprequeforcriarlinksinternosuseatag
<g:link>(oualgumadasvariantesexpostasnestase ção),poisistogarante
queserãogeradoslinkscomaURLcorretaparavocê.
Vocêtambémpodeincluirnatag <g:link>osparâmetrosnecessários
paramontarsuaURL.Paraisso,podemosusardoisparâmetros:
•id Quandovocêquerpassarapenasoatributo idàsuaURL,como
porexemploem http://localhost:8080/categoria/show/1.
•params Recebecomoparâmetroummapausadoparaacomposiç ão
doseulink.
Vamosaalgunsexemplos:
<%--
Para gerar
<a href="http://localhost:8080/cotacao/show/1">Expor</a>
--%>
<g:link controller="cotacao" action="show" id="${cotacao.id}">Expor</g:link
<%--
Para gerar
<a href="http://localhost:8080/cotacao?max=10&offset=11">Listagem</a>
--%>
<g:link controller="cotacao" params="[max:10,offset:11]"/>
278

## Página 285

CasadoCódigo Capítulo8. Acamadaweb:visualização
Talvezvocênãoprecisedatag <a>,masapenasdaURLgerada. Nesse
caso,usamosatag <g:createLink>.
createLinkTo
Fig.8.7:Aten çãoredobrada!
Háumatagchamada <g:createLinkTo>noGrailsquefoimar-
cadacomoobsoleta(deprecated ). Cuidadoparanãoconfundircom
<g:createLink>.Evite-a.
Elaéusadaquandoprecisamosincluirumlinkemalgumtrechodonosso
GSP,comoeminstruçõesJavaScriptnasquaissóprecisamosdoendere ço.
Podemosverumexemploaseguir:
<%-- Um exemplo usando jQuery --%>
<script type="text/javascript">
jQuery.get("${createLink(controller:'controller', action:'show', id:1)}",
function(data) {
// nosso código aqui
})
</script>
Reparouqueusamosatag <g:createLink>comosefosseumafun ção?
Sim: podemosfazeristocomGSP.Tagspodemserchamadastantonoseu
estadonaturalquantocomofun ções.Falaremosmaissobreissomaisàfrente
nestecapítulo8.2.
Muitasvezesvocêiráquererreferenciarconteúdoestático.Imagineque
tenhamosumarquivoCSSquesejadenossointeresseincluiremnossapá-
279

## Página 286

8.3. Tagoufunção? CasadoCódigo
gina.Entraemaçãoatag <g:resource>,quepodemosusartalcomono
exemploaseguir:
<head>
<link rel="stylesheet" href="${resource(dir:'css', file:'main.css')}"/>
</head>
Neste exemplo, referenciaremos o arquivo estático
web-app/css/main.css. Yeap: podemos armazenar conteúdo está-
ticonodiretório web-appdanossaaplicação. Oatributo dirdatag
apontaráparaodiretóriorelativoemseuinteriore file,oarquivoque
queremosincluiremnossolink. Tambémfalaremosmaissobrerecursos
estáticos8.8maisàfrentenestecapítulo.
8.3 T ag ou função?
Aotratarmosdatag <g:createLink>8.2vocêdeveterobservadoquea
usamoscomosefosseumafun çãoqualquer.Essaéumadasgrandesvanta-
gensportrásdomodocomoatecnologiaGSPmanipulatagscustomizadas:
vocêpodeusá-lascomosefossemfun ções. NãoapenasemarquivosGSP,
mastambémemcontroladoresedentrodassuasprópriasbibliotecasdetag
também.VocênãoprecisamaisficaraninhandotagstalcomofariaemJSP.
Lembracomoera?
<%-- Primeiro tínhamos de declarar a taglib... --%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%-- Quanto sofrimento! E agora aninhá-la! --%>
<a href="<c:url value='/item/list'/>">
Meu link
</a>
TodatagcustomizadaemGrailstemcomoretornoumobjetodotipo
org.codehaus.groovy.grails.web.util.StreamCharBufferque,
aoserimpresso,acabanosretornandoumastring. Imaginequeemumde
nossoscontroladoresprecisemossaberoendere çodeumaURLgeradapela
tag <g:createLink>.Comofaríamos?
280

## Página 287

CasadoCódigo Capítulo8. Acamadaweb:visualização
def actionQualquer() {
// Armazeno a URL na variável endereço
def endereco = createLink(controller:'cotacao')
}
Fig.8.8:Aten çãoredobrada!
Omodocomodeclareiachamadaàtagnocontrolador não é recomen-
dadopoispodegeraralgumconflitodenomeemseuinterior(imagineuma
outraactioncomonome createLinknamesmaclasse).Oidealésempre
precederonomedatagpeloseunamespace.Sendoassim,vamosreescrever
estecódigo:
def actionQualquer() {
// Armazeno a URL na variável endereço
// Agora usando o namespace correto!
def endereco = g.createLink(controller:'cotacao')
}
NemtodatagcustomizadaemGrailspossuiomesmonamespace g:.
Adiantenestecapítuloquandolheensinarcomocriarsuaspróprias tag li-
brariesmostrareicomodefiniroseupróprio,oqueésempreumaboaprá-
tica.Apenascomoexemplo,chamaremosumatagcustomizada(eimaginária
nestemomento)do ConCot( <concot:detalhesItem>):
def detalhesItem = concot.detalhesItem(item:item)
8.4 L idando com formulários
Claro,Grailstambémnosforneceumasériedetagsquefacilitamavidada-
quelesqueprecisamlidarcomformulários,ouseja,todosnós.Astagsfun-
damentaisnósjávimosaotratarmoscontroladores 7,maséimportanteque
noslembremosdelasagora.
281

## Página 288

8.4. Lidandocomformulários CasadoCódigo
Aprincipaledelongemaisusadaé <g:form>,paradeclararmosfor-
mulários. Emsuaessência,suaprincipalfun çãoégarantirqueoatributo
actiondatag <form>sejapreenchidocorretamente. Osatributosmais
importantesusadosnestatagportantosão:
•controlleronomedocontroladorquereceberáarequisição(opcio-
nalcasoestejamoslidandocomumapáginaqueestejaemumdiretório
cujonomecorrespondaaodocontrolador)
•action onomedaactionparaaqualfaremosasubmissão(obrigató-
rio)
•name opcional:preencheovalordoatributo iddatag <form>.
•useToken usadoparalidarmoscomsubmissõesduplicadasdofor-
mulário,conformevimosnocapítuloanterior 7.8.
Aseguirpodemosverumexemplosimplesdasuaaplicaç ão:
<g:form action= "save" controller="cotacao">
<%-- Conteúdo do formulário entra aqui --%>
</g:form>
Outravarianteimportanteé <g:uploadForm>,quepossuicomporta-
mentopraticamenteidênticoaode <g:form>,adiferen çaéqueirárenderi-
zarumformulárioparasubmissãodearquivos,sendoqueopreenchimento
doatributo enctypeécomovalor "multipart/form-data".Umexem-
plosimplesaseguir:
<g:uploadForm action="save" controller="item">
<input type="file" name="file"/>
</g:uploadForm>
Controles de entrada
Provavelmente os principais controles de entrada usados em qual-
quer formulário são os textuais. Para tal, Grails nos fornece duas tags:
<g:textField>e <g:textArea>.Ambospossuemdoisatributosessen-
ciais: namee value,representandorespectivamenteonomedaquelecampo
eovalornestearmazenado.Seuusoébastantedireto:
282

## Página 289

CasadoCódigo Capítulo8. Acamadaweb:visualização
<g:form action="save">
<label for="nome">Nome:</label>
<g:textField name="nome" value="${item?.nome}"/><br/>
<label for="descricao">Descrição:</label>
<g:textarea name="descricao" value="${item?.descricao}"/>
</g:form>
Estes campos irão renderizar, respectivamente, as tags <input
type="text" name="nome" id="nome"/> e <textarea
name="descricao" id="descricao"></textarea>.
Pararenderizarmosumcampoparapreenchimentodesenhas( <input
type="password"/>)usamosatag <g:passwordField>,quetambém
possuiosatributos namee value.Podemosverumexemplodesuaaplica-
çãonoformuláriodeautenticaçãodo ConCot:
<g:form action="autenticar" controller="autenticacao">
<label for="login">Login:</label><br/>
<g:textField name="login"/><br/>
<label for="senha">Senha:</label><br/>
<g:passwordField name="senha"/><br/>
<input type="submit" value="Entrar"/>
</g:form>
Finalmente, temos também a renderização de caixas de seleção (tag
<select>).Paraisso,Grailsnosforneceatag <g:select>,quenosper-
mitetratarestatarefa(quepodeserbastantetrabalhosa)deumaformabas-
tantesimples.
Aseguir,podemosverumexemplobastantesimples,usadonoformulário
decadastrodeitensdo ConCot,noqualousuárioselecionaqualacategoria
aqueumdadoitemasercadastradopertence.
<g:form action="save">
<label for="categoria.id">Categoria:</label>
<g:select name="categoria.id"
from="${categoriaList}"
optionKey= "id"
optionValue="nome"
value="${item?.categoria?.id}"/>
283

## Página 290

8.4. Lidandocomformulários CasadoCódigo
<%-- Restante do formulário omitido --%>
</g:form>
Entenderosignificadodosparâmetrosdestatagfacilitaráacompreensão
doseufuncionamento.
•name Obrigatório,defineonomedoitem.
•from Alistasobreaqualatagiráiterargerandoastags <option>
internasà <select>.
•optionKeyQualovalorqueseráarmazenadonoatributo valuede
cadaelemento <option>.
•optionValue Qualovalortextualquedeveráserexpostoemcada
umadasop çõesdacaixadesele ção.
•value Quandopreenchido,dizqualéoitemselecionadopelatag
<select>apósestatersidorenderizada.
Tambémtemosatag <g:checkBox>,queéusadapararenderizarcaixas
deseleção. Estetipodecampodeentradanormalmenteévinculadoaatri-
butosbooleanosdenossasclassesdedomínioou command object.Aseguir
podemosverumexemploaplicadoemumcadastrodeusuários:
<g:form action="save" controller="usuario">
<%-- Restante do formulário omitido --%>
<label for="ativo">Ativo:</label>
<g:checkBox name="ativo" checked="${usuario?.ativo}"/>
</g:form>
Oatributo checkedrecebecomoparâmetroumaexpressãobooleana
queindicaseoitemencontra-semarcadocomopositivoounegativo.
Éimportantemencionarquevocênãoprecisausarastagsdecomponen-
tesdeentradafornecidaspeloGrails,noentantoéinteressanteparasuaapli-
caçãodadoquemuitasvezes(comonocasode <g:select>)estasacabam
porfacilitarbastanteavidadoprogramador.Oformuláriodeautenticaç ãoa
seguir,porexemplo,éperfeitamenteválido:
284

## Página 291

CasadoCódigo Capítulo8. Acamadaweb:visualização
<g:form action="autenticar" controller="autenticacao">
<label for="login">Login:</label><br/>
<input type="text" name="login"/><br/>
<label for="senha">Senha:</label><br/>
<input type="password" name="senha"/><br/>
<input type="submit" value="Entrar"/>
</g:form>
8.5 C riando suas próprias tags customizadas
UmabibliotecadetagsnadamaiséqueumaclasseGroovyqueseguealgumas
convenções:
• Encontra-searmazenadanodiretóriograils-app/taglib.
• SeunomepossuiosufixoTagLib.
• Cadatagemseuinteriorérepresentadaporumaclosure.
HáumcomandodoCLIdoGrailsquegeraráestearquivodeformaau-
tomáticaparavocê(lembre-se,éapenasumacomodidade,seguindoessas
convençõesvocêteráomesmoresultado): trata-sede create-tag-lib.
Vamosusá-loparagerarabibliotecadetags Concot:
create-tag -lib Concot
Finalizada sua execução, serão gerados dois arquivos:
grails-app/taglib/concot/ConcotTagLib.groovy
(o pacote padrão é o nome da sua aplicaç ão) e
test/unit/concot/ConcotTagLibSpec.groovy, que é o esque-
letoparaquevocêescrevaseustestesunitáriosparasua tag library.
Oarquivogeradoébastantesimples:
package concot
class ConcotTagLib {
static defaultEncodeAs = [taglib:'html']
}
285

## Página 292

8.5. Criandosuasprópriastagscustomizadas CasadoCódigo
Segurança
Fig.8.9:Aten çãoredobrada!
Oatributoestático defaultEncodeAsdefinecomooconteúdogerado
pelanossabibliotecadeveráserrenderizadopelacamadadevisualizaç ão.O
valorpadrão,comopodeservisto,é ‘html’.Issopermitequeumasériede
falhasdeseguran çarelacionadasaXSS[25]sejaevitada.
Ovalorpadrãoparacadatagdefinidaemnossabibliotecaé ‘html’.A
razãoésimples:seguran ça.Imaginequeumusuáriomalintencionadodigite
comodescriçãodeumitemno ConCotumtextosimilaraoseguinte:
<script type="text/javascript">
while(true)
{alert('Travei sua tela')}
</script>
Senãohouvernenhumtratamentodurantearenderizaç ãodoconteúdo,
este texto será incluído em todas as páginas que expuserem o atributo
descricaodaqueleitem.Resultado?Suapáginairátravaremumloopin-
finito.Comoresolvemosisso?Comoatributo defaultEncodeAs,queirá
“escapar”otextoaserrenderizado,detalmodoqueteremosalgosimilarao
exemploaseguirdurantearenderização:
&lt;script type="text/javascript"%gt
while(true)
{alert('Travei sua tela')}
&lt;/script%gt;
Vocêestáprotegidoagora.Porpadrão,mantenhaestaconfiguração,anão
serquevocêsaibaexatamenteoqueestáfazendo.Casoqueiraexporotexto
puro(eevitarassimoescapedecaracteres),bastapassarovalor rawpara
esteatributo.
286

## Página 293

CasadoCódigo Capítulo8. Acamadaweb:visualização
Nossa primeira tag
Antesdecomeçar,ésempreumaboapráticadefinirmosqualonamespace
adotadopelanossa tag library.Essaéumaexcelentepráticapoisevitaconfli-
tosdenomesdetags.Fazemosissodefinindooatributoestático namespace,
talcomonaprimeiraevoluçãodonossoarquivo ConcotTagLib.groovy.
package concot
class ConcotTagLib {
// Nosso namespace
static namespace = 'concot'
static defaultEncodeAs = [taglib:'html']
}
Nossaprimeiratagirágerarumatag <a>comumlinkqueapontará
paraaaction imagemdocontrolador ImagemControllerqueimplemen-
tamosemnossocapítulosobrecontroladores 7.10.Estanossatagsechamará
imagem,evaigerarcomosaídacódigoHTMLquesabemosserseguro.Sendo
assim,nossoprimeiropassoéincrementaroatributo defaultEncodeAs
paraquefiquesimilaràlistagemaseguir:
class ConcotTagLib {
static namespace = 'concot'
static defaultEncodeAs = [taglib:'html', imagem:'raw']
}
Emseguida,entraemaçãoaprimeiraversãodanossatag:
/*
Tag que gera uma imagem para um
@attr item Objeto do tipo Item cuja imagem será renderizada caso exista.
*/
def imagem = {attrs, body ->
287

## Página 294

8.5. Criandosuasprópriastagscustomizadas CasadoCódigo
if (attrs.item?.imagem) {
def link = g.createLink(controller:'item' , action:'imagem', id:
out << "<img src=\"${link}\"/>"
}
}
Tudooquefizemosfoideclararumaclosureemnossaclassechamada
imagem,queesperadoisparâmetros: attrse body.Nestemomentonos
interessaapenasoprimeiro,querepresentaoquepassaremosànossatag.
Comopodeserobservadonalistagem,trata-sedeummapconvencionalque
podearmazenarqualquertipodeinformação.
Avariável outédisponibilizadaparatodasasbibliotecasdetagerepre-
sentaostreamdesaídadela.Nocaso,ooperador <<foisobrescrito:oque
vierdoladodireitoserá“transferido”paraostreamdesaída,queirá,emse-
guida,transmitiroconteúdoparaoclientedanossaaplicaç ão.Observeque
tiramosproveitodatag <g:createLink>emseuinteriorsobaformade
função,expondomaisumavezavantagemdestapossibilidade.
ÉmuitorecomendávelquevocêincluacomentáriosemformatoJavaDoc
emsuaaction,poisalémdoganhoóbvio,elesirãoajudarosuportea auto-
completedeIDEscomoJetBrainsIDEAeGGTS(GroovyeGrailsToolSuite).
Bastaescrevercomentárioscomooquefiz,listandocadaatributoesperado
pelatagprecedidopor @attr.
OpróximopassoéaaplicaçãodanossatagemnossosarquivosGSP.O
primeirolocalondeainserifoinapágina show.gspusadapelocontrolador
item.
<%--
itemInstance é uma das variáveis
definidas no modelo da action show de
ItemController
--%>
<concot:imagem item="${itemInstance}"/>
Repareque,comomencionado,foiumprocedimentoextremamentesim-
plesusarabiblioteca:nãoprecisamosincluirnenhumainstruç ãodeimpor-
taçãocomonoJSPnemnadaparecido.Bastausaratag!Oresultadodurante
arenderizaçãoficou...“ok”,paraesteprimeiromomento.
288

## Página 295

CasadoCódigo Capítulo8. Acamadaweb:visualização
Fig.8.10:Nossaprimeiratag
Infelizmentenossatagnãopossuiatributosparadefinirotamanhoda
imagemaserrenderizada.Ficacomoexercícioparavocêimplementaresta
funcionalidade.Dica:bastaesperarmaisumatributo.:)
E aquele parâmetro body?
Nadamaisédoqueotextoquenossastagscustomizadasenvolvem.Que
talaprimorarmosumpoucomaisnossatag <concot:imagem>paraque
tireproveitodesteatributo?Quetalexporotextoenvolvidopelatagcasoa
instânciade Itempassadacomoparâmetronãopossuaocampo imagem
preenchido?Fácilderesolver!
289

## Página 296

8.6. Templates CasadoCódigo
def imagem = {attrs, body ->
if (attrs.item?.imagem) {
def link = g.createLink(controller:'item' , action:'imagem', id:
out << "<img src=\"${link}\"/>"
} else {
// simplesmente passamos a execução de corpo()
// para ser renderizada!
out << body()
}
}
Repareque bodynarealidadeéumaclosurequepodeserexecutadaem
nossatag.Comoaplicaríamosestatagemnossosistemaagora?
<concot:imagem item="${itemInstance}">
<p>Item sem imagem </p>
</concot>
Otexto <p>Item sem imagem</p> serárenderizadonolugardatag
<a>.Bemsimples,concorda?Comosegundoexercício,quetaltentarimple-
mentaratag <g:if>?
def ifConcot = {attrs, body ->
if (attrs.test) {
out << body()
}
}
8.6 T emplates
Templatessãooutramaneiradesecomponentizarelementosusadospelaca-
madadevisualização.PensenelescomopequenostrechosdeGSPquevocê
podereaproveitaremmaisdeumpontodoseuprojeto. Umasoluç ãobem
maisinteressantequeonocivo,perigosoevelho“copiarecolar”.
Criarumtemplateésimples:bastaquevocêsalveseuarquivoGSPcomo
prefixo“_”emseunomeemalgumapastadentrodegrails-app/views
desuapreferência. Paracome çarmos, vamoscriarumtemplatequenos
possibilite padronizar o modo como itens são renderizados noConCot.
290

## Página 297

CasadoCódigo Capítulo8. Acamadaweb:visualização
Para tal, vamos criar um arquivo chamado_item.gsp no diretório
grails-app/views/item:
<div class="item">
<div class="categoria">${item?.categoria?.nome}</div>
<div class="nome">
<g:link action="show" controller="item" id="${item?.id}">
${item?.nome}
</g:link>
<concot:imagem item="${item}">
<p>Sem imagem :(</p>
</concot:imagem>
</div>
</div>
Observequenossopequenotemplateesperaseuprópriomodel,exata-
mentecomoemqualquerarquivoGSP.Háduasop çõesparaserenderizar
esteconteúdo.
Aprimeiraéatravésdatag <g:render>,querecebedoisparâmetros:o
nomedotemplateeomodeloaserrenderizado,comonoexemploaseguir:
<g:render template="/item/item"
model="[item:itemInstance]"/>
Observequenãoprecisamosdigitaroconteúdodoatributo modelcomo
sefosseumaexpressãoGroovy. Bastaqueexistaumavariávelchamada
itemInstancenocontextoemquenossotemplateestásendorenderizado.
Outropontodeaten ção:vocênãoprecisacolocarocaractere“_”aodeclarar
onomedotemplate.
Fig.8.11:Atençãoredobrada!
Claro,dadoqueotemplatenadamaisédoqueoutroarquivoGSP,você
tambémpodeusaratag <g:render>nointeriordelequandoprecisarcriar
291

## Página 298

8.7. PadronizandolayoutscomSitemesh CasadoCódigo
renderizaçõesrecursivasouqueusemoutrostemplatesemsuacomposiç ão.
Cuidado com isto.Templatessãoumasoluçãointeressantedecomponenti-
zação,masseuusoexcessivopodelevaracódigoGSP extremamente difícil
desermantidoeentendido. Apenasseimaginedecompondomentalmente
umprocessoderenderizaçãoenvolvendotemplatesembarcadosemoutros
templates.
Afun ção render,quepodeserusadatantoemcontroladoresquanto
tags,tambémpoderenderizartemplates.Bastapassarcomoparâmetrootem-
plateaserrenderizadoequalomodelo.
def renderItem(Item item) {
render(template:'/item/item', model:[item:item])
}
8.7 P adronizando layouts com Sitemesh
GrailsadotoudesdesuaprimeiraversãooSitemeshcomoseumotorde
layouts. Essetipodeferramentaéaresponsávelpornosajudaramantera
identidadevisualdanossaaplicaçãocomomínimoesfor çopossível.
Sevocênavegarpelaspáginasdo ConCotvaiperceberqueexisteuma
identidadevisualcompostaportrêselementosesquematizadosnaimagema
seguir:
Fig.8.12:EntendendooSiteMesh
292

## Página 299

CasadoCódigo Capítulo8. Acamadaweb:visualização
Aúnicapartequevariaéocorpo,enquantocabe çalhoerodapéseman-
têmosmesmossempre.Paraobteresteresultadopodemospensaremalgu-
massoluções.Aprimeiradelaspoderiaserterdoistemplates,representando
ocabe çalhoeorodapépadrãodosistema,quesimplesmenterenderizaría-
mosemtodasaspáginasdosistemausando <g:render>. Éumasolução
ruim,poisépropensaaerros(vocêpodeesquecerdeincluirostemplates)e
trabalhosa(vocêprecisarárepetiromesmoprocessoemtodasaspáginasdo
seuprojeto).
Apenasporcuriosidade,abraqualquerpáginaGSPdo ConCotnestemo-
mentoebusquepelotrechoHTMLnoqualologotipodoGrailséincluídono
cabeçalhodaspáginas.Vocênãooencontrará,mastalvezvocêpercebaum
trechointeressantenocorpodatag <head>:
<meta name="layout" content="main"/>
Tudoficarámaisclaroatéofinaldestase ção.;)
ÉoSitemeshportrásdospanosqueresolveaquestãodauniformidadevi-
sualemprojetosGrails.Tudocome çacomacriaçãodeumarquivodelayout,
noqualiremosdefinirospadrõesvisuaisqueserepetirãoemtodasaspáginas
do ConCot.Porpadrão,todososarquivosdelayoutsãoincluídosnodiretório
grails-app/views/layouts.Quandocriamosnossoprojeto,foicriado
tambémodefaultdaaplicaçãoqueéoarquivo main.gsp(lembradocorpo
datag <head>?),cujaversãosimplificadaparafinsdidáticospodeservista
aseguir:
<html>
<head>
<title><g:layoutTitle default="Grails"/></title>
<g:layoutHead/>
</head>
<body>
<div id="grailsLogo" role="banner">
<%-- O logotipo do Grails está aqui.
Foi removido da listagem apenas
para simplificar sua leitura --%>
</div>
<g:layoutBody/>
293

## Página 300

8.7. PadronizandolayoutscomSitemesh CasadoCódigo
</body>
</html>
EncontramosolocalondeologotipodoGrailsseencontra: oarquivo
main.gsp.Comovocêdeveterobservado,écomoseestearquivofossefun-
didocomtodasasnossasoutraspáginas.Narealidade,nãoé“comose":fun-
dirpáginaséexatamenteoqueoSitemeshfaz.
Ainstrução <meta name="layout" content="main"/> dizparao
Sitemeshaplicarolayoutdefinidonoarquivo main.gspnapáginacorrente.
Vamosanalisaroconteúdodestearquivodelayout,paraqueascoisasfiquem
maisclaras.
<g:layoutTitle>
Noarquivo main.gsppodemosobservarapresen çadealgumasnovas
tags.Aprimeiraé <g:layoutTitle>,comotexto Grailspassadocomo
valorparaoparâmetro default.Seufuncionamentoésimples:senapágina
sobreaqualseráaplicadaolayoutnãohouveratag <title>preenchida,o
valorselecionadoserá Grails,casocontrário,ovalordefinidonapágina
alvo.
<g:layoutHead>
Jáatag <g:layoutHead>iráincluirnoarquivodelayouttodoocon-
teúdodatag <head>presentenapáginaalvo,enquanto <g:layoutBody>
iráfazerexatamenteomesmotrabalho:adiferen çaestáagoranofatodeque
seráinseridonoarquivodelayoutoconteúdodatag <body>dapáginaalvo.
Oresultado?Asduaspáginasfundidassãoenviadascomorespostaaousuário
final.
Observequevocênãoprecisounaspáginasalvoescreveralgumanotação
estranha:apenasoHTMLnecessário,mantendoasintaxedoHTMLintactoe
facilitandootrabalhodasuaequipe,quenãoprecisaaprendernenhumaoutra
linguagemouficaralterandoarquivosdeconfiguraç ão,talcomoocorreem
outrassoluçõescomooApacheTiles[11](outromotordelayoutsbastante
popular,especialmenteentredesenvolvedoresSpringeStruts).
294

## Página 301

CasadoCódigo Capítulo8. Acamadaweb:visualização
Ativando layouts
HámaisdeumamaneiradeseativarlayoutsdoSitemeshnoGrails. A
primeiravocêacaboudever:bastaincluiratag <meta name="layout"
content="nome do layout"/> nocorpodatag <head>dasuapágina.
Lembre-sequenãoéprecisoincluiraterminaç ãodoarquivonointeriordo
atributo content.
Éimportantemencionarquevocêpodecriarquantaspastasquisernoin-
teriorde grails-app/views/layouts.Sendoassim,casoexistaumar-
quivochamado grails-app/views/layouts/principal/main.gsp,
vocêoreferenciariacomo
<meta name="layout" content="/principal/main"/>
Vocêtambémpodedefinirolayoutpadrãoparatodasasactionspresentes
emumcontrolador.Paraisso,bastaincluirnocódigo-fontedestecontrolador
oatributoestático layoutrecebendocomovaloronomedolayoutaser
aplicado:
class ItemController {
static layout = "main"
}
Fazendoisso,nãoénecessárioincluiratag <meta name="layout">
emsuaspáginasGSP.
Finalmente,aterceiraop çãoébasear-seemconven çõesdoGrails. Se
houvernointeriordapastadelayoutsumarquivocujonomesejaigualao
docontrolador,eleseráaplicadoàspáginasrenderizadasporeste.
Sendo assim, se por exemplo, existir o arquivo
grails-app/views/layouts/item.gsp, e não for definido o atri-
butoestático layoutouatag <meta>emseusarquivosGSP,esteseráo
layoutpadrão.Aindamelhor,vocêpodetambémdefinirolayoutparauma
actionespecífica,bastaqueoarquivosigaaseguinteconven çãoemseulocal
dearmazenamentoenome:
/views/layouts/[nome do controlador]/nomeDaAction.gsp
295

## Página 302

8.8. Recursosestáticos CasadoCódigo
A mesma regra se aplica: o arquivo
grails-app/views/layouts/item/create.gsp poderia ser o
layoutpadrãodapáginarenderizadapelaaction createdocontrolador
item.Novamente,apenassenãoforcriadooatributoestático layoutou
forincluídaatag <meta>noarquivoGSP.
8.8 R ecursos estáticos
Amanipulaçãoderecursosestáticosemumaaplicaçãowebéumadastare-
fasmaismenosprezadaspelosdesenvolvedoresetambémumadasquemais
podepenalizarodesempenhoeconsumodebandadoprojeto. Seráquea
melhormaneiradereferenciarrecursosestáticoscomoarquivosJavaScript,
CSSeimagensérealmenteapenasusaratag <g:resources>quevimos
nestecapítulo?Existealternativamelhor?Yeap!
Hádiversasoportunidadesdeotimizaçãoquepodemserlevadasemcon-
sideraçãoaotransmitirmosrecursosestáticosparanossosclientes:
• PodemosminimizarnossosarquivosCSSeJavaScriptantesdoenvio,
reduzindooconsumodabanda.
• Aindamelhor:paraevitarasdiversasrequisiçõesquepodemchegarao
nossoservidor,podemossimplesmentecombinarváriosdestesarqui-
vosemumsóeenviartodosminimizadosdeumaúnicavez.
• Muitoconteúdosóprecisaserenviadoumavez.Pensenologotipodo
seusite.Seráqueousuáriorealmenteprecisabaixá-lotodasasvezes?É
possívelenviarcabeçalhosHTTPparaoclientequeinformemadatade
expiraçãodaquelerecurso,evitandoquenovasrequisiçõessejamfeitas
aoservidorparabaixá-lo.
Todosestesproblemas(emaisalguns)sãoresolvidospeloplugin Asset
PipelinequejávemporpadrãocomoGrailsdesdeaversão2.4.0equeé
oassuntodestase ção. Oprimeiropontodeaten çãosãotrêsdiretóriosque
sãocriadoscomtodonovoprojetoGrailsquerepresentamoslocaisondeo
pluginirábuscararquivosdeimagens,JavaScripteCSS:
296

## Página 303

CasadoCódigo Capítulo8. Acamadaweb:visualização
•grails-app/assets/images
•grails-app/assets/javascripts
•grails-app/assets/stylesheets
Idealmente,todorecursoestáticodoseuprojetodeveserarmazenado
nestaspastasvisandocomistotirarproveitodasotimizaçõestrazidaspelo
AssetPipeline. E como eu faço para começar a usar o plugin?Simples,através
dealgumastagscustomizadasvoltadasparaessestrêstiposderecursos.
Paraincluirseusrecursos,bastausarastags <asset:javascript/>,
<asset:stylesheet>e <asset:image>. Todaspossuemoparâmetro
src,cujovalordeveráseronomedoarquivoasertransmitidoaocliente
ecujocaminhoérelativoaodiretórioraiznoqualéarmazenado. Seguem
algunsexemplos:
<%-- Incluindo o arquivo CSS
/views/assets/stylesheets/estilo.css
<link rel="stylesheet" href="assets/stylesheets/estilo.css"/>
--%>
<asset:stylesheet src="estilo.css" />
<%-- Incluindo o arquivo JavaScript
/views/assets/javascripts/scripts.js
<script src="assets/javascripts/script.js">
</script>
--%>
<asset:javascript src="scripts.js" />
Nosdoisexemplos,osseguintesprocessamentosserãoexecutadossobre
osarquivostransmitidos:
• SeráenviadoocabeçalhoHTTP Expires,informandoaobrowser
queestepoderácachearestesrecursos,evitandosubsequentesconsul-
tasaoseuservidor.
• Nocasodeconteúdotextual(CSS,JavaScript),esteseráminimizado,
reduzindootamanhodosarquivosbaixadospelonavegador.
297

## Página 304

8.8. Recursosestáticos CasadoCódigo
• Nocasodebundles(veremosmaisarespeitoaseguinte),estesserão
montadosefornecidosaoservidor.
Aúnicadiferençaestánatag <asset:image>,quepoderecebertodos
osatributosquenormalmentepassaríamosparaatagHTML <img>como,
porexemplo, id, style, class, width, heightouqualqueroutroque
vocêdeseje,talcomonosexemplosaseguir:
<%-- Incluindo a imagem
/views/assets/images/logo.png --%>
<asset:image src="logo.png"/>
<%-- Adicionando mais alguns atributos opcionais --%>
<asset:image src="logo.png"
class="logo"
width="450px"
style="border-style:none"
id="idLogo"/>
Criando bundles
Muitasvezesnossosrecursosestáticospossuemdependênciasentresi.
IstoémuitocomumquandolidamoscomJavaScript,porexemplo. Ima-
ginequetenhamosumarquivochamado scripts.jsqueuseabiblioteca
jQuery,armazenadanoarquivo jquery.js.SemousodoAssetPipeline,
paraquenossoscriptfuncionassecorretamente,precisaríamosescrevercó-
digosimilaraoabaixo:
<script type="text/javascript"
src="${resource(dir:'js', file:'jquery.js')}">
</script>
<script type="text/javascript"
src="${resource(dir:'js', file:'script.js')}">
</script>
Trata-sedeumamaneirabastanteineficientedesereferenciarnossosre-
cursos.Primeiro,porqueforamnecessáriasduasrequisiçõesaonossoservi-
dor(umaparacadaarquivo),esegundo,porquenãoháqualquerinformaç ão
sobrecacheamentosendofornecidaaonavegador.Umasoluç ãointeressante
298

## Página 305

CasadoCódigo Capítulo8. Acamadaweb:visualização
seriajuntaroconteúdodosdoisarquivosemumsó,masestaéumatarefa
propensaaerros,poisvocêpoderiasimplesmenteesquecerdefazê-locaso
nãoautomatizasseoprocesso.
Mas o que é um bundle?
Nadamaisdoqueumconjuntoderecursosestáticosinterdependen-
tesquesãocombinadosemumúnicoarquivo.
Uma alternativa muito mais interessante é armazenar os
dois arquivos no diretório apropriado lido pelo Asset Pipeline (
grails-app/views/assets/javascripts) e em seguida declarar
asdependênciasemummanifestocomooseguinte, quechamaremosde
bundle.js.
/**
//= require jquery.js
//= require script.js
*/
Ainstrução //= require incluiemnossobundleoconteúdodoar-
quivoreferenciado(observequeocaminhoaoarquivoérelativo). Emse-
guida,bastareferenciarnossobundleemnossoarquivoGSPtalcomono
exemploaseguir:
<asset:javascript src="bundle.js"/>
Emtempodeexecução,osdoisrecursosreferenciadosserãoincluídose
minimizadosemumbundle,queserátransmitidoparaoclienteincluindoo
cabeçalhoHTTP Expires,permitindoquenossonavegadorcacheieaquele
recurso,evitandofuturasrequisições.
Éinteressanteobservarquetodoesteprocessamentosóocorrenoambi-
entedeprodução,oqueproporcionaaodesenvolvedorcontinuaralterando
seusrecursosestáticosdurantedesenvolvimento,efacilitaenormementeo
processo,poisobundleserágeradoacadarequisiç ão.
299

## Página 306

8.8. Recursosestáticos CasadoCódigo
Aliás,nomomentodegeraçãodoarquivo WARtodososbundlessão
pré-compilados,evitandoqueemproduçãoesteprocessamentoocorrano-
vamente.Issoaumentaodesempenhodaaplicaç ãoereduzotempodeinici-
alizaçãonocontainerweb.
Ainstrução //= require éoquechamamosde diretiva de importação.
Umconjuntodediretivasformamoque,nojargãodoAssetPluginéchamado
demanifesto(manifest).Oprefixousadonaescritadadiretivavariadeacordo
comoformatodorecursoestático:
•CSS prefixo *=
•JavaScriptprefixo //=
Háoutrastrêsdiretivasalémde require:
•require_self incluioconteúdodoarquivonoqualadiretivaéin-
cluídanobundle.
•require_treeincluirátodooconteúdodaárvorenaqualoarquivo
debundleseencontra.
•require_full_tree incluirátodooconteúdodaárvorenaqualo
arquivodebundleseencontraetambémdetodosospluginsquepos-
suamarquivosnomesmodiretórioemsuaestrutura. Veremosmais
sobrepluginsemumcapítulodedicadoaoassuntonestelivro 11.
Voltandoaonossobundleinicial,poderíamosreescrevê-lousandoapenas
osarquivos script.jse jquery.js,comonoexemploaseguir:
/**
//= require jquery.js
//= require_self
*/
function processeItens() {
/*esta função poderia estar usando
as funções do jQuery sem problema agora. */
}
300

## Página 307

CasadoCódigo Capítulo8. Acamadaweb:visualização
Plugin Resources
Fig.8.13:Compatibilidade
Daversão2.0.xatéa2.3.x,opluginpadrãousadopeloGrailspara
gerenciaratransmissãoderecursosestáticoseraoResources[19],quea
partirdaversão2.4.0foisubstituídopeloAssetPipeline.Esteseráinclu-
siveopadrãoadotadonaversão3.0doframework.
EstasubstituiçãotrouxeumasériedevantagensaoGrailscomo,por
exemplo,umnúmeromenordedependênciasexternas,manipulaçãode
bundles(veremosmaisàfrente)maissimplesemelhoriasdedesempe-
nho.
ÉimportantemencionarqueoGrailsapartirdaversão2.2.0execu-
tadosobreaJVM7+jáécompatívelcomoAssetPipeline.Sevocêpossui
umprojetobaseadonestaversão(ouposterior)doGrailsasubstituiç ão
doantigopluginResourcespeloAssetPipelineéumexcelentenegócio
poisiráreduzirseutrabalhoduranteoupgradeparaaversão3.0dofra-
mework.
8.9 A jax
GrailsoferecesuportenativoaAjaxatravésdeumpequenoconjuntodetags,
quetornamaaplicaçãodestapráticaumatarefatrivial.Parailustrarsuaapli-
cação,vamosconstruirumformuláriodebuscadeitensno ConCot,substi-
tuindosuapáginainicial,cujoresultadofinalserásimilaraoexpostodaima-
gem:
301

## Página 308

8.9. Ajax CasadoCódigo
Fig.8.14:AplicandoAJAX
O primeiro passo é incluir a tag<g:javascript> no interior de
<head>:
<head>
<g:javascript library="jquery"/>
</head>
IssoiráativarosuporteaAjaxusandoabibliotecajQuery,quejávem
porpadrãoinstaladacomoGrails.Épossívelusaroutrasbibliotecasalémdo
jQuery,comoporexemploDojo,noentantonestelivrovamosfalarapenasa
respeitodabibliotecapadrãousadapeloGrails2.4.
302

## Página 309

CasadoCódigo Capítulo8. Acamadaweb:visualização
Atenção para o Asset Pipeline
Fig.8.15:Compatibilidade
Casovocêtenhamigradosuaaplicaçãoparaaversão2.4doGrails
e removido o plugin Resources, você deve evitar usar a instrução
<g:javascript>.Emseulugar,use <asset:javascript>talcomo
noexemploaseguir:
<head>
<asset:javascript src="jquery.js" />
<head>
Essecódigofor çaocarregamentodabibliotecausandoopluginAsset
Pipeline.
NossopróximopassoconsistiránaescritadoformulárioAjaxusandoa
tag <g:remoteForm>:
<g:formRemote name="formBusca" update= "resultado"
url="[controller:'item', action:'busca']">
Buscar item:
<g:textField name="nome"/>
<input type="submit" value="Buscar"/>
</g:formRemote>
<div id="resultado"></div>
Noatributo updatedefinimosoidentificadordatagHTMLquereceberá
oresultadodanossaconsulta.Oatributo urldefinequalaactionquedeverá
serexecutada.Notequepassamosummapacomovalorequeoconteúdodo
303

## Página 310

8.9. Ajax CasadoCódigo
formulárionãopossuinadadediferentesecomparadocomumformulário
convencional.
Nossaaction buscaébastantesimples:apenasrenderizaumtemplate
comoresultado.Vejaaseguir:
def busca() {
def itens = Item.findAllByNomeLike("%${params['nome']}%")
render(template:'resultado', model:[itens:itens])
}
O template grails-app/views/item/_resultado.gsp é igual-
mentesimples.
<table>
<thead>
<th>Nome</th>
<th>Imagem </th>
</thead>
<tbody>
<g:each in="${itens}" var="item" status="i">
<tr class="${i % 2 == 0 ? 'even' : 'odd'}">
<td>
<g:link action="show" id="${item.id}" >${item.nome}</g:link>
</td>
<td>
<concot:imagem item="${item}"/>
</td>
</tr>
</g:each>
</tbody>
</table>
Voilà: nosso formulário Ajax está pronto para ser usado e funci-
onará perfeitamente. Outra tag interessante que surte efeito similar é
<g:remoteLink>. Elafuncionadeumaformamuitoparecidacomatag
<g:link>. Adiferençaestánapresen çadoatributo udpateque,assim
comonocasode <g:formRemote>,recebecomovaloroidentificadorda
tagHTMLnaqualdeveráserrenderizadaarespostadoprocessamentoda
nossaaction.
304

## Página 311

CasadoCódigo Capítulo8. Acamadaweb:visualização
Tags Ajax consideradas obsoletas
Fig.8.16:Compatibilidade
Na documentação da versão 2.4.0 [10] é dito que as tags
<g:formRemote>, <g:remoteField>, <g:remoteFunction>e
<g:remoteLink>devemserconsideradasobsoletas(deprecated )eque
seriamremovidasdefuturasversõesdoGrails.Casoestejapensandoem
migrarseuprojetoparaGrails3.0,esteéumpontoquedeveserlevado
emconsideração.
Issonãoquerdizerqueastagsdeixarãodeexistir.Preocupadocom
isso,envieiume-mailparaalistadediscussãousadapelosdesenvolve-
doresdoframework[15]efuitranquilizadopelopróprioGraemeRocher,
principalresponsávelpelaevoluçãoemanuten çãodoGrails,quenos
dissequeessastagsnarealidadeserãomovidasparaumplugin.Sendo
assim,quandoaversão3.0doGrailssair,bastaráusaresteplugin,que
aindanãofoipublicado.
8.10 C ustomizando o scaffolding
Finalmente,umaúltimadica:vocêpodecustomizar100%doscaffoldingdo
Grails,sabia?Paratal,bastaexecutarocomando install-templatesna
interfacedelinhadecomando.Issoirásalvarnapasta src/templates.
O conteúdo armazenado em src/templates na realidade
são os mesmos usados pelos comandos create-domain-class,
create-controller, create-tag-lib, generate-views,
generate-all e basicamente todos os artefatos que conseguimos
305

## Página 312

8.10. Customizandooscaffolding CasadoCódigo
construiratravésdalinhadecomandodoframework.
O mais interessante é que podemos customizar o modo como o
scaffolding é gerado também. Basta modificar o conteúdo da pasta
src/templates/scaffolding.Comissoépossível,dentreoutrascoisas,
modificá-losdetalmodoquepassemausaralgumframeworkCSScomo,por
exemplo,TwitterBootstrapouZurbFoundation.
Bug na versão 2.4.4 do Grails
Fig.8.17:Atençãoredobrada!
Infelizmente,háumbugnaversão2.4.4doGrailsquenãopermite
queostemplatesusadosnageraçãodosarquivosGSP(osarquivosmais
customizadospelosdesenvolvedores!)nãosejamincluídosnodiretório
src/templates.Felizmenteesteéumproblemafácildeserresolvido.
No diretório de instalação do Grails, busque pelo arquivo
plugins/scaffolding-2.1.2.zip. Descompacte seu con-
teúdoemumapastaqualquerdesuapreferência,vocêencontraráuma
pastachamada scaffoldingnodiretório src/templates. Basta
copiá-laparaapasta src/templatesdoseuprojetoeoproblemaestá
resolvido:podecustomizarseuscaffoldingagora.;)
306

## Página 313

Capítulo9
Camadadenegócio:serviços
Ocódigomaisimportanteemtodosistemaéaquelenoqualescrevemosa
lógicadenegóciodocliente. Arquiteturalmente,estecomponentedevese
posicionardaformamaisisoladapossível,ouseja,nãodevepossuirdepen-
dênciaalgumacomascamadasdecontroleevisualizaç ão:idealmente,teria
apenascomacamadadepersistência.
Grailsnosincentivaaimplementaralógicadenegócioemserviços(ser-
vices). Nestecapítulovamosentendersuanaturezaecomissoconhecera
essênciadopróprioGrailsqueéoSpringFramework[31].
9.1 S erviços
Serviços(services)sãoasoluçãofornecidapelaequipededesenvolvimento
doGrailsparaqueoprogramadorpossaimplementardaformamaisisolada
possívelasregrasdenegóciodoseuprojeto. Masserviçosnãosãoapenas

## Página 314

9.1. Serviços CasadoCódigo
“códigoisolado":elestambémtiramproveitodoSpringFramework,quenos
fornecepoderososrecursoscomoinversãodecontrole,inje çãodedependên-
cias,transacionalidadeeAOP.
Mas por que não devemos implementar regras de negócio em controladores?
• Vocêperdeoisolamentodaregradenegócio,quepassaaficaracoplada
àcamadadecontroleevisualizaç ão.Normalmente,issoésintomade
umacoplamentoaindamaior.Exemplo:vocêalterasuapáginaGSPe
precisamudarocontrolador,aíderepentepercebequeprecisaalterar
aquelaregradenegóciotambém.Asituaçãolhesoafamiliar?
• Éperdidaaseparaçãoderesponsabilidades. Seucontroladorpassaa
serresponsáveltantoporgerenciarasrequisiçõesrecebidaspelasua
aplicaçãoquantoaregradenegóciosdoprojeto(vejaopontoacima).
• Atestabilidadeficacomprometida. Émuitomaisfáciltestarmosum
serviçoisoladamentepoisonúmerodedependênciasémenor.
• Oreúsoécomprometido:comoacessarocódigopresenteemumcon-
troladorapartirdeoutrasclassesquenãosejamcontroladores?
• Dadoqueaseparaçãoderesponsabilidadeséperdida,normalmentea
complexidadedocódigopresentenoscontroladoresaumentasignifi-
cativamente.
Vamosescrevernossoprimeiroserviço?
Nosso primeiro serviço
Nocapítulo 7vimosumprimeirocandidatoaserviço. Lembraquando
implementamos nosso comunicador com os fornecedores7.7? Podemos
implementá-loagoracomoumserviço.Novamente,duasconvençõesdevem
serseguidas.
• Aclassedeveestarnodiretóriograils-app/services
• Deveteremseunomeosufixo Service
308

## Página 315

CasadoCódigo Capítulo9. Camadadenegócio:serviços
Vocêtambémpodecriá-lausandoainterfacedelinhadecomando.Basta
executarocomando create-service Comunicacao:
create service Comunicacao
O comando irá criar dois arquivos:
grails-app/services/concot/ComunicacaoService.groovy
e test/unit/concot/ComunicacaoServiceSpec.groovy, onde
escreveremosnossostestes.Nesteprimeiromomento,apenasoprimeironos
interessa:
package concot
import grails.transaction.Transactional
@Transactional
class ComunicacaoService {
def serviceMethod() {
}
}
Éumaclassecomooutraqualquer:adiferen çaestánapresençadaanota-
ção @Transactionalsobreaqualfalaremoscomdetalhesmaisàfrente.É
inclusiveincluídoummétododeexemploque,naturalmente,iremosapagar
(paraqueummétodochamado serviceMethod?).
Nossaprimeiraversãodestemecanismoésimilaràexpostaaseguir.
Não se preocupe agora com o que colocaremos no interior do método
enviarMensagem.Primeirovamosusar(oumelhor,injetar)oserviçoonde
sefaznecessário.
@Transactional
class ComunicacaoService {
def enviarMensagem(Fornecedor fornecedor,
String email,
String mensagem) {
// Executa a tarefa de envio de e-mail
}
}
309

## Página 316

9.1. Serviços CasadoCódigo
Injeção de dependências: usando o serviço
Entraemcenaoconceitodeinje çãodedependências. Sevocênunca
trabalhoucomSpring,acreditoqueamelhormaneiradeentenderotermo
é a prática. Primeiro vamos fazer duas pequenas mudanças na classe
FornecedorController.
class FornecedorController {
// restante da classe omitido
def comunicacaoService
def enviarMensagem(EnvioEmail envio) {
envio.validate()
if (envio.hasErrors()) {
// tratamos o erro
} else {
flash.message = "Mensagem enviada com sucesso"
// Usamos nosso serviço
comunicacaoService.enviarMensagem(envio.fornecedor,
envio.email,
envio.mensagem)
render(view:'comunicacao')
}
}
}
Aodeclararmosumatributoemnossocontroladorcujonomecoincida
comodoserviçoqueacabamosdecriar( comunicacaoService), em
tempodeexecuçãoteremosiniciadooprocessodeinje çãodedependências,
ouseja,esteatributoirárecebercomovalorumainstânciadonossoserviço
quandoocontroladorforinstanciadoeestaráprontoparauso,queéexata-
menteoquefaremosnaaction enviarMensagem.
Enãoésóemcontroladoresqueainje çãodedependênciasfunciona:tam-
bémpodemosinjetarserviçosemclassesdedomínio, tag librariese command
objects,oqueexpõebemopoderdecomponentizaç ãodosserviços.
Como esta instância do serviço é criada e injetada?Primeirolhedirei quem
cuidadainstanciaçãoeinje ção:oSpringFramework.ChamamosGrailsde
310

## Página 317

CasadoCódigo Capítulo9. Camadadenegócio:serviços
frameworkmasnarealidadeestamoslidandocomum meta-framework,isto
porqueumaaplicaçãoGrailsnadamaiséqueumafinacamadaGroovycons-
truídaparatirarmáximoproveitodoSpring.
Observequevocênãoprecisouinstanciarmanualmenteumobjetodo
tipo Comunicacaoservice,istofoifeitoparavocêpelocontainerdein-
jeçãodedependênciaseinversãodecontroledoSpring,quecuidaránãosó
dainstanciaçãoeinje çãodoobjeto,mastambémsepreocuparáemprover
umasériedefuncionalidadesadicionaisparanós,especialmentetransacio-
nalidade,queveremosadiante,deumaformacompletamentetransparente.
Container Spring?
OnúcleodoSpringFrameworkéoquecostumamoschamardecontainer
deinversãodecontrole(IoT Inversion of Control )einje çãodedependências
(DI Dependency Injection). Estecomponenteéresponsávelporcuidardo
ciclodevidadeumobjeto,istoé: quandoumainstânciadevesercriadae
ondedeveráserinjetadaemoutrosobjetos.
O nome “inversão de controle” vem deste ato de delegarmos a res-
ponsabilidadepelainstanciaçãodosobjetosparaocontainer. Você, pro-
gramador, não precisa se preocupar em escrever código comonew
ComunicacaoService():quemexecutaestatarefaéocontainer,quetam-
bémseráoresponsávelpelodescartedestasinstânciasparavocê(veremos
maissobreeste“descarte”napróximaseçãodestecapítulo).
EstasinstânciasgerenciadaspeloSpringsãooquechamamosde spring
beansousimplesmente beans. Lembraquandodisseagorahápoucoqueo
Grailsénarealidadeummeta-frameworkequevocêpoderiainjetarseus
serviçosemcontroladores,classesdedomínio,bibliotecasdetage command
objects? Issoépossívelporquetodosesteselementos também são beans do
Spring.
Otermo“injeçãodedependências”tambémmereceumarápidaexplica-
ção.Quandonaclasse FornecedorControllerescrevemosotrecho:
class FornecedorController {
def comunicacaoService
}
311

## Página 318

9.2. Escopos CasadoCódigo
comunicacaoServiceéoquechamamosdeuma dependência da classe
FornecedorController.Oatodeinjetardependênciasequivaleaopro-
cessoexecutadopelocontainerdoSpringdeprimeirodescobrirquaisasde-
pendênciasnecessáriasparaaexecuçãodeum beaneemseguidainjetá-las
naqueleobjeto.
9.2 E scopos
VimosqueocontainerdoSpringseencarregadeinstanciarnossosserviços
etambéminjetá-losparanósondesefazemnecessários,masnarealidade
tambémresolveoutroproblema:quandooobjetodeveserdescartado?Por
quantotempoumainstânciadeveexistir?Dependedoescopo.
SabemosqueocontextopadrãodeumcontroladorGrailsé prototype
7.12,ouseja,serácriadaumanovainstânciaquedurarásomenteenquanto
arequisiçãoestiverativa(adescriç ãoquefiznaquelemomentodoescopo
prototypeéimprecisa,evocêentenderáporquedigoistoatéofinaldesta
seção).
Oescopoatendeduasfinalidades:amaisóbviaédefinirporquantotempo
umainstânciadeveexistir.Amenosevidenteéevitarproblemasdeconcor-
rência.Voltoarepetir:umaaplicaçãowebéumaaplicaçãointrinsecamente
concorrente. Otempointeiromaisdeumusuárioiráiniciaraexecuç ãode
métodosemumamesmaclasse,ecadainstância,porsuavez,possuiseupró-
prioestadointerno.Comoevitarqueumusuárioacesseoumodifiqueoes-
tadodeoutrogerandoerrosdifíceisdeseremdetectadoseresolvidos?Usando
oescopocorreto.
Adescriçãodosescoposnosajudaaentendermelhorcomooproblema
éresolvido.
•sessionUmainstânciadoobjetoécriadaeexistiráapenasdentrodo
períododeexistência eestaráacessívelnasessãodousuáriocorrente.
Sendoassim,havendodoisusuáriosnosistema,temosduasinstâncias
domesmoobjeto,umaparacadasessão,enãoveremosproblemasde
concorrência.
•prototype Todavezqueoobjetofornecessário,oSpringseencar-
regarádecriarumanovainstânciaparaoobjetoqueprecisadaquele
312

## Página 319

CasadoCódigo Capítulo9. Camadadenegócio:serviços
recurso. Quando o objeto é necessário?Nomomentoemqueseins-
tanciaumnovobeaneoSpringdetectasuasdependênciasouquando
pedimosdiretamenteaocontainerdoSpringumanovainstânciado
bean.
•singleton Omaisperigosoesedutordosescopos.Umaúnicains-
tânciaserácriadaecompartilhadaportodasasrequisiçõesquenossa
aplicaçãovenhaareceber. Porquesedutor? Economiaderecursos
computacionais. Porqueperigoso? Oestadoécompartilhadoentre
todososusuários.ÉoescopopadrãodetodoserviçonoGrails.
•request Umanovainstânciadaclasseserácriadaacadarequisi-
çãorecebidapelaaplicaçãoeexistiráenquantoaquelarequisiç ãoes-
tiverativa. Reparequeédiferentedoescopo prototype. Umbean
prototypepodesobreviverpormuitotempoapósfinalizadaumare-
quisição.
•flashOobjetoexistirádurantearequisiçãocorrenteeapróximaape-
nasparaumdadousuário.
Qualescopoadotardependedocontextodeusodoseuserviço.Seeste
nãopossuirestadoalgum, singletonpodeserumaescolhabastantein-
teressantepoislheeconomizarámuitosrecursoscomputacionais(instanciar
objetosécarotantodopontodevistadaCPUquantodememória,lembre-
sedisso). Seoserviçorequerestado,masdeveviverpoucotempo,talvez
requestou prototypelheatendammelhor.
313

## Página 320

9.3. Transações CasadoCódigo
O prototype que vira singleton
Fig.9.1:Aten çãoredobrada!
Lembre-sequeserviçostambémpodemreceberainje çãodeoutros
serviços. Sendoassim,muitocuidadocomseuserviçoquepossuies-
copo singletonequerecebecomodependênciaumbeancujoescopo
é prototype.
Ainje çãodedependênciasemumainstânciasóocorreumavez.
Sendoassim,oserviço prototypetambémseráinjetadoumaúnica
vezemseuserviço singleton,queserácompartilhadoportodosos
usuáriosconcorrentesdoseusistema.
Bom,apóstodaestateoria,umaperguntafundamentalsurge:comode-
finooescopodomeuserviço?Simples:comoatributoestático scope,que
recebecomovalorumastringrepresentandoonomedoescopo:
class ComunicacaoService {
// Definindo o escopo prototype
static scope = "prototype"
}
Lembre-se: se não for definido o escopo do seu serviço, este será
singletonporpadrão.
9.3 T ransações
Umdosrecursosmaisinteressantesdosserviçoséofatodeseremtransaci-
onais, mas o que é uma transação? Paraentendê-las,primeirovocêprecisa
conheceraideiade unidade de trabalho(unity of work),ouseja,éatentativa
314

## Página 321

CasadoCódigo Capítulo9. Camadadenegócio:serviços
deseconseguirtratarumconjuntodetarefasquevisamumobjetivofinal
comosefosseumaúnicaação.Oexemplomaispopularéodemovimenta-
çõesbancáriasquerepetireiaqui.Imagineaseguintemovimentação:
1) Usuárioefetuaumacompranainternetusandoseucartãodecréditoem
umsite.
2) Ositeenviaumamensagemàoperadoradecartãodecréditoinformando
acompra.
3) Obancoverificaseousuáriopodefazeracompraeavisaaositeseacom-
prapodeounãoserfeita.
4) Aprovadaacompra,oestoquedositeserádecrementadoeopedidopro-
cessado.
Outodasasquatrooperaçõessãoexecutadascomsucessoounenhuma
é.Esteconjuntodeatividadesformauma unidade de trabalho.Finalizadaa
execuçãodatransação,temosnossobancodedados(oubancosdedadosno
casodetransaçõesdistribuídas)todosemumestadoconsistente.
315

## Página 322

9.3. Transações CasadoCódigo
Transações ACID
Transaçõesembancosdedadosrelacionaisnormalmentesãocarac-
terizadaspeloacrônimoACID:
•Atômicas oconjuntodetarefasévistocomosendoúnicaunidade
detrabalho.
•Consistente oestadodobancodedadosémantidoconsistente
casoatransaçãosejafinalizadacomsucessoounão.
•Isoladas múltiplastransaçõesocorremaomesmotempocontra
obancodedados,masumanãointerferenofuncionamentoda
outra.
•Duráveis finalizada com sucesso a transação, os dados
encontram-se persistidos e mantidos no banco de dados com
segurança. Casoocorraalgumaquedadeservidorouqualquer
outroerrofatal,quandooSGBDvoltaraoperarnormalmente,
osdadosalteradosduranteatransaçãocontinuarãoarmazenados
emdiscoeconsistentes.
ÉimportantemencionarquenocasodebasesdedadosNoSQLnem
semprepodemoscontarcomtransaçõesdestetipopoisaobten çãodesta
característicairádependerdofornecedordoseuSGBD.
Serviçosnormalmentelidamcomumasériedeclassesdedomínio,alte-
randonormalmentemaisdeumregistroemnossobancodedados.Terase-
gurançadequetodososdadosestarãoconsistentesaofinaldeumatransaç ão
émaisumarazãopelaqualimplementarserviçoséuma excelenteprática.
Voltandoaonossoserviço ComunicacaoService,vocêdeveselem-
brarqueaclassecriadapelocomando create-serviceveiocomaanota-
ção @Transactionalsobreadeclaraçãodaclasse.Issoquerdizerquetodos
osmétodospresentesemnossoserviçoserãoexecutadosdentrodetransa-
ções.
316

## Página 323

CasadoCódigo Capítulo9. Camadadenegócio:serviços
import grails.transaction.Transactional
@Transactional
class ComunicacaoService {
}
No entanto, a presença desta anotação incluída pelo comando
create-serviceé uma novidade da versão 2.3.0 do Grails. Se nosso
serviçofosseimplementadotalcomonoexemploaseguir:
class ComunicacaoService {
}
todos os seus métodospor padrão iniciariam uma nova transação
quandofossemexecutados. Aanotação @Transactionaltemcomoob-
jetivoprincipalnosfornecerumaconfiguraçãomaisfinaarespeitodequais
métodosdevemounãoserexecutadosdentrodeumatransaç ão.
Sequiserdesativartodasastransaçõesemumserviço,bastaincluiroatri-
butoestático transactionalcomvaloriguala false:
class ComunicacaoService {
static transactional = false
}
Casosejadeseuinteressequealgumdosmétodosnãosejaexecutado
dentrodeumatransação,bastausaraanotaç ão @NonTransactional,o
quepermiteumaconfiguraçãomaisfinasobreomodocomotransaçõessão
iniciadasemnossosserviços.
import grails.transaction.Transactional
import grails.transaction.NonTransactional
@Transactional
class ComunicacaoService {
// Este método não será executado
// em uma transação
@NonTransactional
def naoTransacional() {
317

## Página 324

9.3. Transações CasadoCódigo
}
}
Quando transações não ocorrem
Fig.9.2:Aten çãoredobrada!
Transaçõessóocorrememserviçosinjetadosemnossosobjetos,ou
seja,sófuncionameminstânciasquesãogerenciadaspeloSpring.Sendo
assim,sevocêinstanciarmanualmenteumaclassedeserviçoocontexto
transacionalnãoseráativado.
Ocódigoaseguirnãoexecutatransacionalmente:
new ComunicacaoService().enviarMensagem(item, "kico@itexto.com.br", "Oi!"
Rollback
Finalizadaaexecuçãocomsucessodeummétodopresenteemseuser-
viço,osdadosseencontrarãopersistidoscorretamenteemseubancodeda-
dos. Éoquechamamosdeoperaçãode commit. Noentanto,tãoimpor-
tantequantosaberquandoo commitocorre(acabeidelhecontar)éentender
quandoo rollback,ouseja,ocancelamentodasoperaçõesquecompõem
suatransaçãoocorre.
O rollback ocorrerá de forma automática sempre que uma ex-
ceção do tipo runtime ocorrer durante a execução de um mé-
todo. Esse tipo de exceção é aquela que consiste em uma subclasse de
java.lang.RuntimeExceptionouentãoaprópria.Observeoexemplo
aseguir:
318

## Página 325

CasadoCódigo Capítulo9. Camadadenegócio:serviços
class ComunicacaoService {
def exemploRollback() {
def itens = concot.Item.list()
// Código suicida
for (item in itens) {
item.delete()
}
throw new RuntimeException("Volte para o estado anterior")
}
}
Essecódigosuicidairáapagartodosositenscadastradosnobancodeda-
dos(damaneiramenosperformáticainclusive,diga-sedepassagem),masao
finalédisparadaumaexce çãodotipo java.lang.RuntimeException.
Comisso,aoperaçãode rollbackéchamadadeformaautomáticaene-
nhumaexclusãoseconcretizouemnossobancodedados.
Fig.9.3:Aten çãoredobrada!
Éimportantíssimosalientarque o rollback automático só ocorrerá
com exceções do tipo runtime.Alógicaportrásdestaconven ção(queédo
Spring,nãodoGrails)ébastanteinteressante. Exce çõesdestetipoocorrem
quandoalgocatastróficoocorreucomosistemacomo,porexemplo,aqueda
dealgumservidoroualgumerrogravíssimoquenãopodesercontornado
peloprogramador.
Sendoassim,oleitordeveestarseperguntandoagoraoseguinte:comoeu
executoumaoperaçãode rollbackprogramaticamente?Usandoométodo
withTransaction,queéinjetadopeloGrailsemtodaclassededomínioe
querecebecomoparâmetroumaclosure.Observeoexemplo:
class ComunicacaoService {
def exemploRollback() {
Item.withTransaction { status ->
319

## Página 326

9.3. Transações CasadoCódigo
Item.list().each {
it.delete()
}
status.setRollbackOnly()
}
}
}
Aclosurepassadacomoparâmetroparaométodo withTransaction
recebeumúnicoparâmetroquechamamos status.Trata-sedeumobjeto
dotipo org.springframework.transaction.TransactionStatus
(observe a manifestação do Spring no Grails), cujo método
setRollbackOnlyexecutaaoperaçãode rollbackdatransação.
Estaclassepossuimaisalgumasfun çõescujamençãoéimportante:
•isCompleted retorna truecasoatransaçãotenhasidoconcluída.
•isRollbackOnly retorna truecasotenhasidoexecutadaaopera-
çãode rollback.
Atenção à anotação @Transactional
Fig.9.4:Aten çãoredobrada!
Seaanotação @Transactionalforaplicadaaapenasummétodo
denossaclasse,apenasaquelemétodoserátransacional.
Paraquetodososmétodossejamtransacionaisporpadrãoevocê
queirausar @Transactional, apliqueaanotaçãoprimeirosobrea
classe.
320

## Página 327

CasadoCódigo Capítulo9. Camadadenegócio:serviços
Isolamento
Você pode definir o isolamento da sua transação graças
à anotação @Transactional e seu atributo isolation.
Este recebe como valor uma das constantes definidas no enum
org.springframework.transaction.annotation.Isolation.
Primeiro devemos falar brevemente sobre as opções que este enum nos
ofereceparaemseguidateceralgunscomentários.Comoverá,aquestãodo
isolamentoémuitomaiscomplicadadoqueaparenta.
•READ_COMMITEDSuatransaçãosóteráacessoaregistrosnobancode
dadosquetenhamsidocomitadosporoutrastransações. Permiteno
entantoaocorrênciadeleiturasnãorepetitivas.
•READ_UNCOMMITEDSuatransaçãoteráacessoaregistrosnobancode
dadosqueaindanãoforamcomitadosporoutrastransações. Éoní-
veldeisolamentoquelhepermitemelhordesempenho,mastambém
omaisperigosopoisseuprocessamentopodelevaremconsideraç ão
registrosquenãomaisexistirãoapósafinalizaç ãodatransação.Possi-
bilitaleiturassujas(dirty reads).
•REPEATABLE_READGarantequesevocêforlerumregistronobanco
dedadosrepetidasvezesduranteatransaç ão,estesempreretornará
comomesmovalor;masnãoconsegueevitarleiturasfantasma(phan-
tom reads).
•SERIALIZABLE Garanteomaiorisolamentopossível,noentantoéa
configuraçãomaiscaradopontodevistacomputacional,poisiráblo-
quearosregistrosdoseubancodedadosepodeimpactarfortemente
odesempenhodoseusistema.
•DEFAULT PadrãoadotadopeloGrails.Suastransaçõesirãoadotaras
configuraçõespadrãodoseuSGBD.Cadaumpossuiumvalorpadrão.
MySQL,porexemplo,adota REPEATABLE_READScomopadrão.
No exemplo a seguir configuramos a transação do método
enviarMensagemparaoisolamentodotipo READ_UNCOMMITED.
321

## Página 328

9.3. Transações CasadoCódigo
import grails.transaction.Transactional
import org.springframework.transaction.annotation.Isolation
@Transactional
class ComunicacaoService {
@Transactional
(isolation=Isolation.READ_UNCOMMITED)
def enviarMensagem() {
// conteudo ignorado
}
// Neste método o isolamento padrão será DEFAULT
def outroMetodo() {
}
}
Nadescriçãodosvalorespossíveisparaoatributo isolationmenci-
oneialgumassituaçõesquenopadrãoSQL/92sãochamadosde fenômenos
de leitura(read phenomena)[24]envolvendooisolamentodetransações.É
importantequevocêosconhe çaparaque,comisso,possaselecionarquala
melhoropçãoparaoseucaso.
Oprimeirodestesfenômenossechama leitura suja(dirty reads)eocorre
quandoumatransaçãopossuipermissãodeleituraderegistrosqueforam
modificadosmasaindanãocomitadosporoutrastransaçõesconcorrentes.A
melhormaneiradeentenderestefenômenoéatravésdeumexemplosimples
envolvendoduastransações:T1eT2.
// T1 Executa a consulta abaixo na tabela nome
select nome from item where id = 1
// obtém o valor 'Motor elétrico'
//Na sequência, T2 executa uma operação de alteração
//no mesmo registro
update item set nome = 'Motor' where id = 1
//T1 executa uma segunda consulta contra o mesmo registro
select nome from item where id = 1
// obtém o valor 'Motor'
322

## Página 329

CasadoCódigo Capítulo9. Camadadenegócio:serviços
Comopodeservisto,nasegundaleituraT1perdeuoisolamento,poiso
valorfoimodificadoporT2executandoemparalelo. READ_UNCOMMITED
éaopçãoquenosfornecemelhordesempenhopoisoSGBDnãoprecisase
preocupartantocomoisolamentodastransações,masvocêiráencontrar
situaçõescomoest.
Osegundodestesfenômenossechama leitura não repetitiva(non repeata-
ble reads).Novamente,oqueocorreéaquestãodaconcorrênciaenvolvendo
nossasjáconhecidastransaçõesT1eT2.Adiferen çaestánofatodequeuma
delasseráfinalizadaantesdaoutra. Nadamelhorqueoutrobomexemplo
parailustrarasituação.
//Nossas duas transações já encontram-se iniciadas
//T1 lê o nome do item
select nome from item where id = 1
// obtém o valor 'Motor elétrico'
//T2 altera o valor do item e em seguida executa commit
update item set nome = 'Motor' where id = 1
commit;
//T1 lê novamente o nome do item
select nome fro mitem where id = 1
//obtém o valor 'Motor'
Aleituranãorepetitivaocorrequandoparaumamesmaconsultaéexe-
cutadaduasoumaisvezesemumamesmatransaç ãoeosvaloresobtidossão
diferentesporqueumaoutratransaçãoparalelaalterouosdadoseoscomitou
antesdesuafinalização.Observeadiferen çaemrelaçãoàleiturasuja:neste
caso,estamoslendodadosqueforamCOMITADOSnovamente,mascujo
valorédiferentenasegundaleitura.
Nossaterceirasituaçãosechama leitura fantasma(phantom reads)etrata-
sedeumcasoespecialda leitura não repetitiva.Ocorrequandoumatransação
paralelainsereregistrosnobancodedadoseacidentalmenteosobtemosem
umasegundaconsulta.Maisumexemplopráticoenvolvendonossasamigas
T1eT2:
//T1 busca todas as cotações para um item
//com valor entre 10 e 30
323

## Página 330

9.3. Transações CasadoCódigo
select * from cotacao where item_id = 1 and valor between 10 and 30
//obtém um conjunto de 2 registros
//T2 insere um novo registro e finaliza antes de T1
insert into cotacao (item_id, valor) values (1, 12)
commit
//T1 executa a mesma consulta novamente
select * from cotacao where item_id = 1 and valor between 10 and 30
//obtém um conjunto de 3 registros
Esteterceiroregistroéoquechameide“registrofantasma”. Écomose
elesimplesmentetivessesurgido“donada”,concorda? Estaéumasituação
inclusivebastanteperigosa,poisemcasosnosquaisumgrandenúmerode
registroséinseridoconcorrentementeàsuatransação,elapodesimplesmente
demoraremexcessoparaserfinalizada(nãoparamdechegarnovositens!).
NON_REPEATABLE_READSresolvejustamenteestetipodeproblema.
Bom Kico, agora você me confundiu todo. Qual nível de isolamento devo
usar?Arespostaésimples:sevocêtiverumDBAaoseualcanceouvocêti-
verumconhecimentomaisprofundosobreseubancodedados,perguntea
ele;senãosouber,mantenhaaconfiguraç ãopadrãodoGrails.Oimportante
équevocêsaibanestemomentoquenãoexistebaladeprataquandooas-
suntoéisolamentodetransações,masqueépossívelpelomenosmudaresta
configuraçãocasosemostrenecessário,certo?
Transações somente leitura
SuatransaçãotambémpodeinformaraoSGBDqueestáapenasfazendo
leituradosdados,oquelheforneceaoportunidadedeaplicarbloqueiosme-
nosagressivosemsuasestruturasecomistopropiciarummelhordesempe-
nhoparaseusclientes.
Usando a anotação @Transactional, basta definir o atributo
readOnlycomvalor truecomonoexemploaseguir:
@Transactional(read=true)
def metodoSomenteLeitura() {
}
324

## Página 331

CasadoCódigo Capítulo9. Camadadenegócio:serviços
Oleitormaiscuriosodeveterpercebidoqueestaanotaç ãoencontra-se
aplicadaemalgunscontroladoresgeradospelo scaffolding,talcomonoexem-
ploaseguir:
@Transactional(readOnly = true)
class CotacaoController {
}
Enestemomentodeveestarseperguntando: controladores podem iniciar
uma transação?. Respostarápida: sim! Issoporquesãobeansassimcomo
osserviços,portanto,podemsebeneficiardetodososbenefíciosdeles. No
entanto,issonãoquerdizerquevocêdevaescreversualógicadenegócio
neles,mashásituaçõesnasquaisnãovaleapenaescreverumserviço.Pense
emumaaction,porexemplo,queapenaslistaitensparaseuusuáriofinal.
Realmenteprecisaríamosdeumserviçoali?
Propagação
Finalmente,oterceiroconceitosobretransaçõesquedevefazerpartedo
seucintodeutilidades:comoumatransaç ãosepropaga?Émelhorexplicar
esteconceitocomalgumcódigo:imagineosdoismétodospresentesemum
serviçoimaginário:
class ImaginarioService {
def metodo1() {
// executa uma série de ações
metodo2()
}
def metodo2() {
//executa mais uma série de ações
}
}
Porpadrão,todométodoemumserviçoétransacional.Noentanto,ve-
mosaquique metodo1fazumachamadaa metodo2.Oqueocorrecoma
transaçãoiniciadaem metodo1?Elaéfinalizadaoucontinuaamesmaem
metodo2?Ouéfinalizadaem metodo1eumanovaécriadaem metodo2?
325

## Página 332

9.3. Transações CasadoCódigo
Atransaçãoquefoiiniciadaem metodo1seráfinalizadaem metodo2.
No entanto, você pode customizar este comportamento alterando o atri-
buto propagationdaanotação @Transactional. Novamente,vamos
verquaissãoosvaloresdisponíveis,quesãoasconstantesdefinidasnoenum
org.springframework.transaction.annotation.Propagation.
•REQUIRED Quandoométodoforinvocado,umanovatransaç ãoserá
iniciada.Casoumatransaçãojáestejaemexecução,estaémantida.
•SUPPORTS Seumatransaçãojátiversidoiniciada,elaserámantida
duranteaexecuçãodométodo.Casonãohajanenhumatransaç ãoem
execução,ométodofuncionadamesmaforma.
•MANDATORYOmétodosóéexecutadoseumatransaçãoestiveremexe-
cução.Tentarexecutá-losemumairádispararumaexce çãoemtempo
deexecução.
•REQUIRES_NEW Ométodoaoserexecutado sempreirácriaruma
novatransação.Seeleforchamadoeumatransaç ãojáestiveremexe-
cução,estaseráparalisadaatésuafinalização.
•NOT_SUPPORTEDSehouverumatransaçãoemexecução,iráparalisá-
laatésuafinalização.Internamenteexecutasemquequalquertransa-
çãosejainiciada.
•NEVER Executadeformanãotransacional. Seumatransaç ãoestiver
emexecução,umaexce çãoserádisparada.
•NESTED Sejáhouverumatransaçãoiniciada,estaéparalisada. En-
quantoisto,onovométodocriaráumanovatransaçãoindependente,
aexecutaráe,emseguida,retornaráocontroleparaaanterior.
Noexemploaseguirmudamosapropagaç ãodatransaçãopara NEVER.
import grails.transaction.Transactional
import org.springframework.transaction.annotation.Propagation
@Transactional
class PropagacaoService {
326

## Página 333

CasadoCódigo Capítulo9. Camadadenegócio:serviços
@Transactional(propagation=Propagation.NEVER)
def transacaoNever() {
}
}
9.4 F alando de Spring
Nestecapítulo,pudemosverqueograndeatorocultoportrásdoGrailséo
Spring.Tiramosproveitodediversasdassuasfuncionalidadescomoainje ção
dedependências,inversãodecontrole,transacionalidade,nossoscontrolado-
res,databindingediversosoutrospontos.Esabemoqueémaisinteressante?
VocêpodeacessaremodificarasconfiguraçõesdoSpringoumesmoacessar
oseucontainerdeinje çãodedependênciasdiretamente,sabia?Nestase ção,
iremosmostrarcomotirarproveitodestesrecursos.
Adicionando seus próprios beans
Namaiorpartedasvezes,controladores,classesdedomínioeserviçoirão
atendertodasassuasnecessidades,masesevocêtiveralgumcódigolegalcom
funcionalidadesqueseriaminteressantesdeseremreaproveitadasemnosso
sistema?
No ConCot temos uma classe, originalmente implementada em Java
usadaparacalcularimpostos. Chama-se CalculoImpostos.javaesua
implementaçãopodeservistaaseguir:
public class CalculoImpostos {
/** Tarifa a ser aplicada */
private double tarifa;
public double getTarifa() {
return tarifa;
}
327

## Página 334

9.4. FalandodeSpring CasadoCódigo
public void setTarifa(double valor) {
this.tarifa = valor;
}
public BigDecimal calcularTarifa(double valor) {
// Quem dera no mundo real ser tão
// fácil assim calcular impostos!
return valor * tarifa;
}
}
Observequeelapossuiumapropriedadechamada tarifa,queusare-
mosnasuatransformaçãoembean.Comoumaclasseviraumbean?Noti-
ficandooSpringdequeelaexiste.Amaneiramaissimplesémodificandoo
arquivo grails-app/conf/spring/resources.groovyqueoriginal-
menteéexatamentecomooexpostoaseguir:
beans = {
}
Paraincluirnosso bean CalculoTarifa,bastamodificá-loparaque
fiquedestaforma:
beans = {
calculoTarifa(concot.CalculoImpostos) {
tarifa = 0.5
}
}
Onomedonossobeanserá calculoTarifa,queiráinstanciarumob-
jetodotipo concot.CalculoImpostos,cujaimplementaçãoencontra-se
noarquivo src/java/concot/CalculoImpostos.java.Observeque,
logoemseguida,definimosovalordaspropriedadesdonosso bean: tarifa
receberáovalor 0.5.
Nasequência,bastainjetarestebeanondesefaçanecessário,porexemplo,
noserviçoaseguir.Tudooquevocêprecisafazerédeclararumatributoem
suaclassecujonomecorrespondaaodobeanqueacabamosdedeclarar:
328

## Página 335

CasadoCódigo Capítulo9. Camadadenegócio:serviços
class TributoService {
// Bean injetado
def calculoTarifa
def calcular(double valor) {
// basta usar o bean
calculoTarifa.calcularTarifa(valor)
}
}
Acessando o container do Spring diretamente
Finalmente, vocêtambémpodeacessarocontainerdoSpringdireta-
mente através da sua aplicação Grails. Isso é bastante útil para quando,
porexemplo,queremosevitarproblemascomoodo prototype que se
torna singleton quemencioneiagorahápouco.
Há duas maneiras de se conseguir isso. A primeira é modi-
ficar nossa classe de serviço para que esta implemente a interface
org.springframework.context.ApplicationContextAware
doSpringtalcomonoexemploaseguir:
import org.springframework.context.ApplicationContextAware
import org.springframework.context.ApplicationContext
class SpringAwareService implements ApplicationContextAware {
//O contexto do Spring
private ApplicationContextAware contextoSpring
void setApplicationContext(ApplicationContext ctx) {
this.contextoSpring = ctx
}
}
Aoimplementarmosestainterface,asinstânciasdonossoserviçoirão
terinvocadoométodo setContextAwareapósteremtodasassuasde-
329

## Página 336

9.4. FalandodeSpring CasadoCódigo
pendênciasinjetadas,permitindoacessarocontextodeaplicaçãodoSpring,
representadopeloparâmetro ctxquefoiexposto.
Apartirdestepontovocêpodeacessarlivrementeocontextoeobtero
beanquevocêquiserpelonomeoupelaclasse.Lembraaquele prototype
quevirava singleton?Vejacomopodemosevitaroproblema:
class SpringAwareService implements ApplicationContextAware {
//O contexto do Spring
private ApplicationContextAware contextoSpring
void setApplicationContext(ApplicationContext ctx) {
this.contextoSpring = ctx
}
def obtenhaBeanPrototype() {
contextoSpring.getBean("beanPrototype")
}
def usePrototype() {
obtenhaBeanPrototype().executeAlgo()
}
}
Afun ção getBeandocontextodoSpringretornaumbeanpeloseu
nome. Aochamá-lo,oSpringiránosretornarumnovo beancomescopo
prototypesempre.Emseguida,nóssimplesmenteousamos,talcomoéfeito
nafunção usePrototypeeesteserádescartadopelopróprio garbage col-
lectordaJVMapósalgumtempo,poisnãofoiassociadoanenhumatributo
danossaclasse.
Há também uma variante do método getBean do objeto
ApplicationContext que recebe como parâmetro uma classe e lhe
retornaráobeandomesmotipo.
Tirando proveito do ciclo de vida dos beans
OcontainerdeIoCdoSpringlidacomociclodevidadosbeans,ouseja,
330

## Página 337

CasadoCódigo Capítulo9. Camadadenegócio:serviços
elequesabequandoumbean“nasce”e“morre”. Vocêpodetirarproveito
disso,sabia?BastaimplementaralgumasinterfacesbemsimplesdoSpring.
Se quiser, por exemplo, que seu bean execute al-
gum código de inicialização após ter tido todas as suas
dependências injetadas, basta implementar a interface
org.springframework.beans.factory.InitializingBean:
import org.springframework.beans.factory.InitializingBean
class InicializadorService implements InitializingBean {
/*
Aqui entra seu código de inicialização
*/
void afterPropertiesSet() {
}
}
Implementando-a,seuserviçoseráconstruídodaseguintemaneira:
1) OSpringirácriarumanovainstânciadaclasse.
2) Serãoinjetadastodasasdependênciasnestainstância.
3) OmétodoafterPropertiesSetéexecutado.
4) Obeanédisponibilizadoparaserinjetadoemoutroouusadoporvocê.
Estaéumafuncionalidadebastanteútilquandovocêprecisa,porexem-
plo,executaralgumpreparoinicialnoseubeanantesqueestesejadisponibi-
lizadoparaosistema.Seseuserviçoprecisadedadosimutáveispresentesno
bancodedados,esteéumbommomentoparaqueosmesmossejamcarre-
gados.
Outravantageméevitarerrosdeconcorrência.Imaginequeduas threads
tentemacessarobeanaomesmotempoe,nestemomento,eleprecisecarregar
estasinformaçõesapartirdobancodedadospornãotersidopreviamente
preparado.Elepoderiaacidentalmenteexecutaromesmocódigodeconsulta
331

## Página 338

9.4. FalandodeSpring CasadoCódigo
DUASvezes,oumesmovocêpoderiasedepararcomerrosdeconcorrência
quesãodificilmentedetectadosouresolvidos.
Outro ponto do ciclo de vida de que você pode tirar pro-
veito é o momento em que o bean é descartado pelo contai-
ner. Novamente, basta implementar outra interface do Spring:
org.springframework.beans.factory.DisposableBean. O
método destroyseráexecutadoquandoobeanfordescartado. Aseguir
vocêpodeverumexemplorápidodesuaaplicação:
org.springframework.beans.factory.DisposableBean
class LimpezaBean implements DisposableBean {
void destroy() {
// executa a limpeza
}
}
Issoémuitoútilparaaquelecódigoque“arrumaacasa”quandoseubean
nãoémaisnecessário.Penseemaçõescomofechamentodeconexõescomo
bancodedadosououtroserviçoqualquer,porexemplo,quevocêmantenha
abertasduranteaexecuçãodobeandevidoaalgumarazãodeotimizaç ão.
Outrobomusoéaexclusãodearquivostemporários.
332

## Página 339

CasadoCódigo Capítulo9. Camadadenegócio:serviços
Cuidado com o prototype
Fig.9.5:Aten çãoredobrada!
Beansdotipo prototypesaemdodomíniodocontainerdoSpring
assimquesãogerados.Dessaforma,oSpringapenasconseguiráexecutar
ométodo afterPropertiesSet,enão destroy.
Tenhaissoemmenteaousarainterface DisposableBean.
333

## Página 341

Capítulo10
Testes
Grailséumframeworkqueincentivaseususuários(programadores)otempo
inteiroaescreveremtestes. Provavelmente,vocêjáobservouqueaoexe-
cutarmoscomandoscomo create-controllerou create-tag-lib
tambémsãogeradosesqueletosparatestesnapasta test/unitdoprojeto.
Chegouahoradeexploraresteconteúdo.
10.1 A ntes um pouco de metodologia: TDD e
BDD
UmassuntoqueatéhojegerapolêmicasãoaspráticasdeTDD(T est Driven
Development)eBDD(Behaviour Driven Development ).Ouvimossempreob-
jeçõescomo“agora vou gastar muito tempo escrevendo testes
, “minha produtividade (ou da minha equipe) irá baixar

## Página 342

10.1. Antesumpoucodemetodologia:TDDeBDD CasadoCódigo
ediversosoutros. Recentemente,DavidHeinemeierHansson(criador
doRubyonRails)levantounovamenteestaquestãoaopublicaremseublog
otexto TDD is dead. Long live testing[12]quecuriosamenteébastantecitado
masnãolido(quandoélido)comaaten çãoquemerece.
Naminhaexperiênciacomoconsultor,observoqueaado çãodestasprá-
ticasnasempresasemqueatuogeraresultadosbastanteinteressantes:desen-
volvedoresmaisconfiantes,acúmulomenordehorasextras,códigomaisfácil
desermantidoe,nãoraro,umaumentoatémesmodaautoestimadaequipe
comoumtodo.Seiquequandoestamoscome çandoédifícilacreditarnoque
estaspráticas(TDDeBDD)prometem,masgarantoquesevocêseesfor çar
iráentenderclaramenteseuvalor. Esabedeumacoisa? Vamosaplicá-las
nestecapítulo,masantesvoufalarumpoucoaseurespeito.
TDD em cinco minutos
ApráticadoTDD(T est Driven Development)podeserresumidadeuma
formabastanterudimentaremumafrase: escreva seus testes antes do código.
Énarealidadeaaplicaç ãodeummodelodedesenvolvimentobaseadoem
rápidosepequenosciclos.
Acadanovafuncionalidade,primeiroodesenvolvedorescreveumteste
quedescreveseucomportamentoesperadousandosuaferramentafavorita
(nocasodoGrailsedestelivro,vamosadotaroSpock).Somenteaíocódigo-
fonteéescritopelaprimeiravezeseráexecutadorepetidasvezescontraoteste
atéqueestesejafinalmenteexecutadocomsucesso.
Passadaaprimeirafase,entraasegundanaqualvocêdeverá,senecessá-
rio,refatorarocódigoparaquefiquedeacordocomasmelhorespráticasde
desenvolvimentooumesmoospadrõesinternosadotadospeloseutime. E
comosabersesuasmudan çasnãoirãoestragaroqueacaboudefazer?Exe-
cutandoostestescontraelas.
Seiquesoamuitoestranhoecontraprodutivodizerqueescreverostestes
antesdocódigopodeaumentarasuaprodutividade,masoqueobservoé
quequandonosexercitamosnestadire çãoacabamosporrefletirmelhora
respeito do objetivo final. Ecomissovocêacabaconhecendomelhornão
sóoquedeveserfeito,mastambém quandoestápronto(quandoostestes
passam).
336

## Página 343

CasadoCódigo Capítulo10. Testes
Maisdoqueisto,tambémnotoqueostestessãoexcelentesparasede-
tectarcódigoemestadodedecomposiç ão. Como? Simples,seestádifícil
escreverumtestequedescrevacomoaquelecódigodeveriasecomportar,é
sinaldequeháouproblemasnoentendimentoounomodocomoescrevemos
aquelecódigo.
Claro,odesenvolvedordevetomarcuidadotambém com o que testa.
Nãovaleapenatestarousodecódigoquetodossabemosfuncionarcomo,
porexemplo,oseuframeworkdepersistência,talcomonoexemploaseguir:
def salvar(Cotacao cotacao) {
cotacao.save()
}
NósjásabemoscomooGORMfunciona. Testarométodo savenão
iráagregarnadaaoseuprojeto,anãoserquevocêestejaexplorandoofun-
cionamentodaAPIoureportandoumbugàequipededesenvolvimentodo
Grails.
Écomotestarum getterou setterJava:associaçãodevaloreséalgoque
obrigatoriamentealinguagemdeprogramaçãodevenosfornecerparaque
possafuncionarminimamente.Então,oquevaleapenatestar?Alógicapela
qual vocêéresponsável,enãoseuframework,linguagemdeprogramaçãoou
biblioteca.
Normalmente,ascríticasenvolvendoprodutividadenaescritadetestes
nascemdesteponto: aescritadetestesquenarealidadenãoagregam,mas
apenascomplicamsuavida.
Alémdavantagemdefacilitaroprocessodedesign,outracaracterística
interessantedostesteséofatodeestesacabaremsetornandoumaespéciede
“documentaçãoviva”doseusistema,comoumaespecificaçãoformaleque
acabaporaumentarosentimentodeseguran çanasuaequipe.Vocêssabem
agoraquandosuasalteraçõesnosistemaintroduzemnovosbugs:ostesteslhe
contam!
E o BDD?
JáviapráticadoTDDoperarmilagresemdiversosprojetos,noentanto
háumapequenalimitação:seufocotendeaserosdesenvolvedores.Aprá-
337

## Página 344

10.1. Antesumpoucodemetodologia:TDDeBDD CasadoCódigo
ticadoBDD[20](Behaviour Driven Development )podeservistacomouma
evoluçãodoTDD,poisiremostrazerparaonossoladonãoapenastestadores
profissionais,massim todosaquelesquepossueminteressenosistemaaser
desenvolvido.
OtermoBDDfoiintroduzidoporDanNorth[21]apartirdasuaexpe-
riênciacomoinstrutordeTDD.Observandoassuasprópriasdificuldades,
assimcomoadosseusalunos[21],Northacabouporcriaresteconceitoque
vaimuitoalémdostestes.Trata-sedeumanovaformadedesenvolvimento.
DentreasinovaçõestrazidaspeloBDDestáoconceitode linguagem com-
partilhada(ubiquitous language),quenadamaiséqueabuscaporumvo-
cabuláriocomum,compreendidoportodososinteressadosnosistema,que
permitasatisfazeralgunsobjetivos:
• Garantirquetodosseentendamdamelhormaneirapossível.Desen-
volvedores,analistasderequisitose,principalmenteoclientefinalde-
verãotodosfalaromesmoidioma.
• Construiroconceitodepronto,ouseja, todossaberãocomprecisão
quandodeterminadafuncionalidadeencontra-seinteiramenteimple-
mentadaeprontaparaoambientedeproduç ão.
MencionamosaquioconceitodeBDDpelofatodenoGrailsusarmos
comoframeworkdetestesoSpock,quetemcomofocoauxiliaraado ção
desta prática. Como veremos, seu estilo de escrita é bastante diferente,
possibilitando-nosescrevertestesdetalmodoquetodososenvolvidosno
projetopoderãoentendê-lose,aindamaisimportante,adotá-loscomoparte
importantedadocumentaçãodosistema.
Apropósito,haverátambémalgumasmudan çasemnossovocabulário.
AopensarmosemBDD,trocaremosalgumaspalavras.Usaremosostermos
“comportamento”(behaviour)eespecificaçãoemvezde“testes”. Parasaber
maissobreoporquêdestamudan ça,recomendoquevocêleiaotexto Intro-
ducing BDDdopróprioDanNorth[21].
338

## Página 345

CasadoCódigo Capítulo10. Testes
10.2 N ossas primeiras especificações
EmumabelamanhãGutoprocurouDanielpedindoumnovorecursoparao
ConCot.
Daniel,aconteceualgomuitochatoaqui.Umdosnossosclientesrecebeu
nossalistadecotaçõesparaseuprojetoeachouquediversosdositensquein-
cluímosláeramexageradamentecarosparaele.Comosetratadeumapessoa
muito“sensível”,achouqueestávamosesnobando-oenosenviouume-mail
criticandonossotrabalho.
Eleédoido?
Não,apenaspão-duroechato.Então,estavapensando,seráquenósnão
poderíamoscriar“listasdecotações”paranossosclientes?
Comoassim?
Explicomelhor: imaginequetenhamosumclienteX.Criaríamosuma
listadecotaçõesexclusivaparaele. Nela,poderíamosincluirlimitesdeva-
lor.Porexemplo:“ovalormáximodeumbritadoréR$10.000,00”paraesta
listagem.Comisso,osistemasópermitiriaincluircotaçõescomvalordeno
mínimoR$10.000,00.Oqueacha?
Hmm...entendi.Etemlimitemínimotambém?
Nãohaviapensadonisto,maséumaboaideia! Tambémpodeterum
valormínimo.Tipo:nomínimoR$ 100,00paraaqueleitem.Oqueacha,é
viável?
Achoquesim,Guto.Olhandoaqui,teríamosdeincluirmaisduasenti-
dadesno ConCot.Umapararepresentaralistaeoutraparacolocaroslimites
devalor,certo?
Errado:temdetertambémumaterceiraentidadequerepresenteaco-
taçãoincluídanalista.Depreferênciacomadataemquefoiinserida.Pode
ser?
Uai,pode!
Ah,eoutracoisaDaniel:temdeserpossívelqueovalormáximoemí-
nimodoitempossamseropcionais,masquepelomenosumexista.
Comoassim?
Porexemplo: umitempodetervalormínimoemáximo,ouapenaso
valormínimoouapenasovalormáximo,entendeu?
339

## Página 346

10.2. Nossasprimeirasespecificações CasadoCódigo
Entendeu!
CombasenestaconversaDanieladicionouasnovasentidadesnosistema
eterminoucomummodelodeentidadestalcomooexpostonaimagema
seguir:
Fig.10.1:DiagramadeclassesdoConcot
Eimplementourapidamentetodasasclassesdedomínio:
class ListaCotacoes {
String nome
static constraints = {
nome nullable:false, blank:false, maxSize:128, unique:true
}
}
340

## Página 347

CasadoCódigo Capítulo10. Testes
package concot
class LimiteCotacao {
BigDecimal valorMinimo
BigDecimal valorMaximo
static belongsTo = [ lista:ListaCotacoes, item:Item, moeda:Moeda]
static constraints = {
valorMinimo: nullable:true
valorMaximo: nullable:true
}
}
class CotacaoLista {
Date dataInclusao
static belongsTo = [
lista: ListaCotacoes,
cotacao: Cotacao
]
static constraints = {
}
}
DanieljáconheciaoSpock,queéoframeworkdetestesadotadospelo
Grailscomopadrãodesdeaversão2.2etambémjáestavaestudandoBDD.
Sendoassim,combasenaconversaquetevecomGutoachouqueseriauma
boaideiacolocá-losemprática.
Começoupercebendoqueomaisimportantenãoseriamastelasdeca-
dastro,massimalógicadenegócio.Nadamaisinteressantedoquecome çar
pelaimplementaçãodeumserviçoquevalidasseainclusãodenovascota-
çõesemumalista. Sendoassim,executouocomando create-service
341

## Página 348

10.2. Nossasprimeirasespecificações CasadoCódigo
ListaCotacoesnainterfacedelinhadecomandodoGrailsecomissojá
crioutambémoarquivodeespecificaçãodoSpockqueusariaparaprimeiro
escreverseustestes(querdizer,especificações!).
O arquivo ListaCotacoesServiceSpec foi gerado na pasta
test/unit/concot, o que indica se tratar de um teste unitário, e seu
conteúdooriginaljánosmostracomoqueSpockseparece:
package concot
import grails.test.mixin.TestFor
import spock.lang.Specification
@TestFor(ListaCotacoesService)
class ListaCotacoesServiceSpec extends Specification {
def setup() {
}
def cleanup() {
}
void "test something"() {
}
}
342

## Página 349

CasadoCódigo Capítulo10. Testes
Testes unitários e de integração
Grailsnosforneceporpadrãodoistiposdetestes: unitárioeinte-
grado.Oobjetivodotesteunitárioénosforneceroferramentalnecessá-
rioparaquepossamosverificarofuncionamentodeumafuncionalidade
demodoisolado,ouseja,semqueprecisemosiniciartodoosistemapara
isto.
Issonospermitefocarapenasnalógicaqueestamosimplementando
naqueletrechodosistema,masporoutrolado,dadoquesemprepreci-
samosinteragircomoutroscomponentesarquiteturais,porexemplo,a
camadadepersistência,umnovoproblemasurge.Comofazê-lo?Ares-
postaésimples:criandoversõesfalsasdosmesmos(os mocks).Veremos
comdetalhesnestecapítulocomofazerisso.
Testesunitáriosnosfornecem,portanto,dependênciasdonossocó-
digoquefuncionamem“condiçõesideaisdetemperaturaepressão”,ou
seja,elasfuncionamexatamentecomogostaríamos,oquepodeserum
problema,masnosajudaafocarmelhornaquiloquedesejamosverificar.
Játestesintegradosresolvemoproblemada“condiçãoidealdetem-
peraturaepressão”aonosdisponibilizarosistemacompleto.Vocênão
precisamaisdemocks,poisestaráusandooprópriosistemaparaisso.
Sãofundamentaisparaquevejamosqualseráocomportamentodosis-
temaquandoforparaprodução,fornecendo-nosumambientequeéo
maissimilarpossívelaeste.
SevocêjátrabalhoucomtestesusandoframeworkscomojUnitdeveestar
achandomuitoestranhaadeclaraçãodeumdosmétodos:
void "test something"() {
}
Narealidade,senuncatrabalhoucomGroovyoununcausounenhum
frameworkBDDcomo, porexemplo, Cucumber, tambémdeveterestra-
nhadobastante.Oquetemosaquiéaaplicaç ãodeumdosprincípiosadota-
dosporDanNorth: “os nomes dos testes devem ser sentenças
343

## Página 350

10.2. Nossasprimeirasespecificações CasadoCódigo
[21].
Spocknosincentivaaescrevertestescujonomenãosejaumafun ção“pa-
drão”comotestIncluirCotacao,massimfrasesquepossamsercom-
preendidas,alémdeporprogramadores,tambémpelaequipedenegócio,
comoGuto,porexemplo.Sendoassim,antesdesequerescreveronossopri-
meirométodoem ListaCotacoesService,Danieljásapecaoprimeiro
comportamentoesperado:umsimplestestedesanidade.
void "verificando a sanidade do serviço para uma cotação nula"() {
when:"quando"
def cotacao = null
def lista = new ListaCotacoes()
def data = new Date()
then:"então..."
service.incluirCotacao(lista, cotacao, data) == null
}
NojargãodoSpock,nãotemostestes,massimcomportamentos. Este
foioprimeirocomportamentoaserdefinidoporDaniel.Oquefazerquando
passoumacotaçãonulaparanossoserviço?Nesteprimeiromomento,Daniel
tambémcomeçouapensaremcomoseriaaassinaturadométodoresponsável
porincluirumacotaçãoemumalista.Algoquedeverecebertrêsparâmetros:
alistanaqualseráfeitaainclusão,acotaç ãoeumadata.
Danieltambémachouinteressantedefiniraquiqualotipoderetorno
destafun ção: umainstânciade CotacaoListajápersistida,informando
assimaodesenvolvedorqueoitempodeserincluídocomsucessonalistade
cotações.Masoquesãoestasinstruções when:e then:.
ElasdemarcamblocosdeiteraçãousadospeloSpock.Oprimeiro, when:
(quando),éusadoparadefinirascondiçõesemcimadasquaisdeveremos
verificarumcomportamento. Énormalmenteondedefinimosasvariáveis
queserãousadasemnossaverificaç ão,comonoescritoporDanielemque
iremoschecarcomonossocódigosecomportaráaorecebercomovaloruma
cotaçãonula.
Opróximobloco, then:,demarcaaquiloquequeremosverificar.Neste
caso,deveserescritaumaexpressãobooleanaporlinha.Voltandoaocasodo
344

## Página 351

CasadoCódigo Capítulo10. Testes
Daniel,elequersecertificardequeseráretornadoovalornuloquandouma
cotaçãonulaforpassadacomoparâmetroparanossoteste.
Eaquele serviceali,deondevem? Vamosnoslembrardoiníciodo
arquivoondeestamosescrevendonossaespecificação:
package concot
import grails.test.mixin.TestFor
import spock.lang.Specification
@TestFor(ListaCotacoesService)
class ListaCotacoesServiceSpec extends Specification {
Aanotação @TestForrecebecomoparâmetroonomedaclassedeser-
viçoquecriamoscomocomando create-service. ElainstruioGrails
a,nomomentoemqueostestesforemexecutados,injetarumainstânciade
ListaCotacoesServicenaclasse ListaCotacoesServiceSpec.
Estainstânciaseráumatributocujonome,paraserviços,é service.
ElapodeseraplicadaatodososartefatostestadosdoGrails(serviços,clas-
sesdedomínio,controladores,bibliotecasdetag)eparacadaumdestesirá
criarumatributocujonomecorrespondaaseutipo,ouseja,respectivamente
service, domain, controller, tagLib.
ComotodobompraticantedeBDD/TDD,opróximopassodeDanielé
executarostestes,mesmosabendoqueirãofalhar(afinaldecontas,sequeres-
crevemosafun ção incluirCotacaoainda!).Paratal,noCLI(Command
Line InterfaceInterfacedeLinhadeComandos)doGrailsiráexecutaroco-
mando test-app :unit ListaCotacoesService.
345

## Página 352

10.2. Nossasprimeirasespecificações CasadoCódigo
O comando test-app
Ocomando test-appéusadonainterfacedelinhadecomandos
doGrailsparaexecutarostestes(ouespecificações!)escritaspornós.
Seuusoébastantessimples: semnenhumparâmetro,vaiexecutar
todasasespecificações,tantounitáriascomointegradas.
Sequiserapenasalguma,bastadigitarpartedonome,queapenas
asquecorrespondamaoprefixofornecidoserãoexecutadas. Exemplo:
test-app ListaCotacoesService vaiexecutaroarquivodetestes
ListaCotacoesServiceSpec.groovy.
Sequiserexecutarapenasostestesunitários,passetambémova-
lor :unit na linha de comando. Apenas os integrados? Use
:integration.
Oresultadoesperadoéobtido:ostestesnãoirãopassar,comopodeser
expostonasaídadoconsoleexpostaaseguir:
Fig.10.2:Erronostestes
Éimportantemencionarquesempreégeradotambémumrelatóriodos
testesnosformatostextoeHTMLnodiretório target/test-reports.A
seguirpodemosverumexemplodasaídadorelatórioatual:
346

## Página 353

CasadoCódigo Capítulo10. Testes
Fig.10.3:Orelatóriodetestes
Peloerroqueobtivemosnostestesironicamentesabemosqueelesfunci-
onam.Sendoassim,nossopróximopassoéimplementararegradenegócios
naclasse ListaCotacoesServicecombasenoquejátemospré-arranjado
emnossaprimeiraespecificaçãoformal,aomenosumaversãoqueatendaa
esteprimeirocomportamento.
class ListaCotacoesService {
/**
Verifica os limites
*/
private boolean testeLimites(ListaCotacoes lista, Cotacao cotacao){
// ainda não implementado neste momento
true
}
def incluirCotacao(ListaCotacoes lista, Cotacao cotacao, Date data){
if (lista && cotacao && data && testeLimites(lista, cotacao ))
{
return new CotacaoLista
(cotacao:cotacao,
lista:lista ,
dataInclusao:data).save()
}
null
}
}
347

## Página 354

10.2. Nossasprimeirasespecificações CasadoCódigo
Executandoostestesnovamente,agoraelespassam,masotrabalhoainda
nãoestácompleto.
Fig.10.4:Ostestespassaramcomsucesso!
Nãodefinimosqualcomportamentoesperamosquandoascotaçõesque
submetemosànossalistaestãodentroouforadoslimitesquenossocliente
definiu. Edadoqueestamoslidandocomtestesunitários,deondeiremos
obterosdados? Qualbancodedadosusar? Grailspossuiumaversãodo
GORMfeitaespecificamenteparatestesunitáriosquefuncionainteiramente
emmemória.
Tudo o que precisamos fazer é incluir a anotaç ão
grails.test.mixin.Mock na classe em que definimos nossa espe-
cificação informando quais classes de domínio precisamos que sejam
mockadaspeloGrailsparanós,talcomoDanielfez:
import grails.test.mixin.TestFor
import grails.test.mixin.Mock
import spock.lang.Specification
@TestFor(ListaCotacoesService)
// Recebe uma lista com o nome das nossas
// classes de domínio
@Mock([ListaCotacoes, Cotacao, Item,
Fornecedor , Moeda, Categoria,
LimiteCotacao, CotacaoLista])
class ListaCotacoesServiceSpec extends Specification {
}
Oresultado? Podemosescrevernossoscomportamentos(behaviours)
agoracomosetivéssemosumbancodedadosrealporbaixodospanos!
348

## Página 355

CasadoCódigo Capítulo10. Testes
Condições ideais de temperatura e pressão
Fig.10.5:Atençãoredobrada!
Lembre-sequenadasubstituiumtesteintegrado. Aversãoemme-
móriadoGORMusadaemtestesunitáriosoperaem“condiçõesideais
detemperaturaepressão”.Odesempenhosempreseráexcelenteevocê
nãoveráproblemasquesóencontraráemproduçãocomo,porexemplo,
errosemíndices,problemasdedesempenhoetc.
Avantagemdostestesunitáriosestáemnosauxiliarnofocodaló-
gicaqueestamosescrevendo sem que precisemos nos preocupar com
o ambiente de produçãonestemomentoapenas.
AgoraqueDanielpodetirarproveitodoGORMemmemória,tudooque
precisafazeréescreversuasegundaespecificação.
void "uma cotação cujo valor esteja no limite deve poder ser inserida"() {
when:
def fornecedor = Fornecedor.findOrSaveByNomeAndEmail
("Juca", "juca@juca.com")
def categoria = Categoria.findOrSaveByNome("Equipamento")
def item = Item.findOrSaveByCategoriaAndNome(categoria, "Motor")
def moeda = Moeda.findOrSaveByNomeAndSimbolo("Real", 'R$')
def cotacao =
Cotacao.findOrSaveByFornecedorAndItemAndMoedaAndValor
(fornecedor, item, moeda, 100)
def lista = ListaCotacoes.findOrSaveByNome("Lista de teste")
def limite = LimiteCotacao
.findOrSaveByListaAndItemAndMoeda(lista, item, moeda)
limite.valorMinimo = 10
349

## Página 356

10.2. Nossasprimeirasespecificações CasadoCódigo
limite.valorMaximo = 1000
def cotacaoForaDoLimite = Cotacao.findOrSaveByFornecedorAndItemAndMoeda
(fornecedor, item, moeda, 1)
limite.save()
then:
service.incluirCotacao(lista, cotacao, new Date()) != null
service.incluirCotacao(lista, cotacaoForaDoLimite, new Date()) == null
}
Uou! Reparou como pudemos tirar total proveito dos finders dinâ-
micosparagerarautomaticamenteoestadoesperadonobancodedados
paraquenossosistemafuncione?Novamente,Danielexecutaráocomando
test-appapenasparaverostestesfalharecomprovarseufuncionamento.
Opróximopassoseráimplementarumaversãode ListaCotacaoService
querespeiteestescomportamentos,oqueéfeito,gerandoumaversãoinicial
dafuncionalidade:
class ListaCotacoesService {
/**
Verifica os limites
*/
private boolean testeLimites(ListaCotacoes lista, Cotacao cotacao) {
def limite = LimiteCotacao.findByItemAndListaAndMoeda
(cotacao.item, lista, cotacao.moeda)
if ( limite &&
((limite.valorMaximo && cotacao.valor > limite.valorMaximo) ||
(limite.valorMinimo && cotacao.valor < limite .valorMinimo) ))
{
return false
}
true
}
def incluirCotacao(ListaCotacoes lista, Cotacao cotacao, Date data) {
if (lista && cotacao && data && testeLimites(lista, cotacao)) {
return new CotacaoLista
(cotacao:cotacao, lista:lista, dataInclusao:data).save()
}
350

## Página 357

CasadoCódigo Capítulo10. Testes
null
}
}
Executandoostestesnovamente,oquetemos? Sucesso! Danielexecu-
touoBDDquasequeperfeitamente. Sabemqualfoiaprincipallimitaç ão?
AausênciadeGutoduranteaescritadasespecificaçõescomSpock. Aose
encontrarem,esteerrosetornouevidente.
OlhaGuto,aquiestãoasespecificaçõesqueescrevi.Oqueacha?
UaiDaniel,parecemuitolegalistoaqui. Éaprimeiravezqueconsigo
entenderseucódigo!
Nãoseiseagrade çoouxingoGuto.Maseaí,oqueachou?
Aindatenhoalgumasdúvidas:eseeupassarumalista,umacotaç ãoden-
trodolimiteeadatafornula,retornafalso? Eseeupassarumalista,uma
data,eacotaçãoforinválida,elevaimeretornarnulo? Eseeupassartudo
certomenosacotação,elevairetornarfalso?Eseeupassaradatadeamanhã?
Eseforadatadeontem,comofica?Esealistanãotivernenhumarestriç ão,
qualquercotaçãoéaceita,certo?Ese..?Ese...?Ese....?
GutobombardeouDanielcomumasériedeexemplos.Eesseéomodo
comoaspessoasforadasalaouempresasdedesenvolvimentopensam.Acre-
dite:euevocêachamosGroovyumalinguagemmaravilhosa,masparaseu
clienteouorealmenteinteressadopelosoftwarequeestásendoescrito,ela
nãopassadealgumidiomaestrangeiroextremamentefeio.
Nemtudoestáperdido:Danielnãoprecisaimplementarumaquantidade
infinitadeespecificaçõesporqueSpocknospermiteescreververificaçõesba-
seadasemtabelas!
Danielcomeçatirandoproveitodeumafun çãoincluídaporpadrãono
arquivo ListaCotacoesServiceSpecquenãovimosatéestemomento:
setup. Éláquedefinimosoestadoquepoderásercompartilhadoporto-
dososcomportamentosdanossaespecificaç ão. Eométodo cleanup? É
oqueexecutaremosparalimparqualquersujeiraquetenhamosdeixado. É
importantemencionarque setupsempreéexecutadoantesdetodotestee
cleanupapóstodosostestespresentesnomesmoarquivo.
Parafacilitaraescritadessetipodetestes,énecessárioquesejamcria-
dosalgunsatributosnaclasse ListaCotacoesServiceSpec,quedevem
351

## Página 358

10.2. Nossasprimeirasespecificações CasadoCódigo
serprecedidospelaanotação @Shared(vocêprecisaráimportaropacote
spock.lang.Shared).TestesescritosemSpocksópodemacessarosatri-
butosdaclassenaqualsãodeclaradosseelesforemestáticosouprecedidos
destaanotação. Sendoassim,DanielaoladodeGutomodificaoinícioda
especificaçãoparaquefiquetalcomoexpostoaseguir:
import spock.lang.Shared
@TestFor(ListaCotacoesService)
@Mock([ListaCotacoes, Cotacao, Item,
Fornecedor , Moeda, Categoria,
LimiteCotacao, CotacaoLista])
class ListaCotacoesServiceSpec extends Specification {
/*
Lista que contém uma restrição para um item
"Motor" cujo valor deve variar entre 10 e 1000 Reais
*/
@Shared listaTeste
/*
Uma lista que não contém restrição alguma
*/
@Shared listaVazia
/* Uma cotação para o item "Motor" que vale 100 Reais */
@Shared cotacaoValida
/* Uma cotação para o item "Motor" que vale 1 Real */
@Shared cotacaoInvalida
def setup() {
/*
Código que inicia os atributos acima,
"persistindo-os" na versão em memória do GORM
disponibilizada pelo Grails para testes
unitários
*/
}
}
Logoemseguida,entranossonovocomportamento,queDanielescreve
aoladodeGuto.
352

## Página 359

CasadoCódigo Capítulo10. Testes
void "situações esperadas para a inclusão de cotações na lista"() {
expect:"o que esperamos"
resultado == (service.incluirCotacao( lista, cotacao, data) != null)
where:"alguns exemplos"
lista | cotacao | data | resultado
listaTeste | cotacaoValida | new Date() | true
listaTeste | cotacaoValida | null | false
listaTeste | cotacaoInvalida | new Date() | false
null | cotacaoValida | new Date() | false
listaVazia | cotacaoInvalida | new Date() | true
listaVazia | cotacaoValida | new Date() | true
}
Nobloco expect:Danielescreveumaexpressãoquedeveretornar
verdadeirooufalso(queéoúnicotipodeexpressãoválidaaí)que,neste
caso, verifica se um valor diferente de nulo será retornado pela função
incluirCotacao.
Amágicaocorrenobloco where:,quereceberácomovalorumatabela
delimitadapelocaractere |.Aprimeiralinhadefineosnomesdasvariáveis
eparâmetrosusadosnaexpressãoescritaem expect:.Aslinhasseguintes
apenasreferenciamosatributosquedefinimosnoiníciodanossaclassede
acordocomosexemplosqueGutolevantou.
Senovassituaçõessurgiremparaestecaso,bastaqueincluamosaslinhas
necessáriasnacolunaquedefinimosnobloco where:.Oresultado?Ostes-
tespassarameGutosaiubastantefelizcomofatodeterpodidocontribuir
comaevoluçãodo ConCot.Emaisainda,porquepôdelevarocódigo-fonte
daespecificaçãoparaumareuniãocomadiretoriada DDLetodosadora-
ramsaberqueagorapodemcontarcomestetipoderecursoaseraplicadona
evoluçãodetodosossistemasdaempresa!
Nestaevoluçãovimosalgumascoisasbastanteimportantes:
• ComoaplicarBDD(ouTDD)nãoétãodifícilquantoparece.
• AprendemosausaroSpock(sim,vimosquasetudoaseurespeitoaqui).
• Comoescrevertestesunitáriosparaserviços.
• ComosimularoGORM.
353

## Página 360

10.3. Escrevendotestesunitáriosparacontroladores CasadoCódigo
• ComoexecutartestesunitáriosnoGrails.
Daquiparafrente,deixaremosa DDL Engenhariaempaz(porenquanto)
paraexporosrecursosqueGrailsprovêaodesenvolvedorquedesejaescrever
testesparacontroladoresebibliotecasdetag. Issoporquevocêjáviucomo
escrevertestesparaclassesdedomíniotambém(bastausaraanotação @Mock
evocêconseguetestaratémesmosuasvalidaçõespersonalizadas).
10.3 E screvendo testes unitários para contro-
ladores
Escrevemostestesunitáriosparacontroladoresquaseexatamentecomofize-
mosparaocasodoserviço ListaCotacoesService.Adiferen çaestáno
fatodequeagoraaanotação TestForreceberácomovalorumaclasseque
representaumcontroladornanossaaplicaçãoGrails.
Nestaseção,vamosabordarumcontroladorhipotéticobastantesimples
chamado TestesControllernoqualvamossimularasoperaçõesmais
comunsquecostumamosencontrarnaescritadestetipodecomponente.
Nalistagemaseguir,podemosvercomoficouoiníciodanossaespecifi-
cação TestesControllerSpec.
package concot
import grails.test.mixin.TestFor
import spock.lang.Specification
@TestFor(TestesController)
class TestesControllerSpec extends Specification {
}
Será criado um novo atributo em nossa especificação chamado
controller,queusaremosparadescreveroscomportamentosesperados.
354

## Página 361

CasadoCódigo Capítulo10. Testes
T estando render
Vamoscomeçarpelasituaçãomaissimplespossível:umaactionqueren-
derizaumtextosimples.Paratal,imaginequenossocontroladorpossuauma
actionchamada indexcujaimplementaçãovemosaseguir:
def index() {
render "Olá mundo!"
}
Comoverificaríamosestecomportamento?
void "action index simples: testando o método render"() {
when:
controller.index()
then:
response.text == "Olá mundo!"
}
É criado um atributo chamado response na classe
TestesControllerSpec, que é uma instância de
GrailsMockHttpServletResponseque, porsuavez, estendeaclasse
MockHttpServletResponsedoSpring.Elacontémumasériedemétodos
úteisqueusaremosparatestarnossoscontroladores.Dentreeles,encontra-se
getText(),queretornaotextorenderizadoporumaaction.
Emnossoprimeiroexemplo, apenasverificamosseotextoretornado
quandoaactionéexecutadaéaquelequeesperamos.Deummodogeral,todo
testedecontroladorescomGrailséescritousandoapenasosblocos when:e
then:,comonoesquemaaseguir:
def "todo comportamento de controladores é assim"() {
when: "você apenas invoca a action ou prepara os parâmetros"
//você tem acesso a todos os escopos
//usei "params" como exemplo, mas session e flash
//também estão disponíveis
params.parametro = "algum valor"
controller.action()
then: "e em seguida você verifica se ocorreu o que você espera"
}
355

## Página 362

10.3. Escrevendotestesunitáriosparacontroladores CasadoCódigo
Verificando se a view correta foi usada
Outraaçãocomumdeumcontrolador:renderizaçãodeumapáginaGSP.
Novamente,algobastantesimplesdeserverificado.Imagineaactionaseguir:
def renderGSP() {
render view:'renderGSP', model:[nome:"Henrique"]
}
Quetalverificarnãosóseapáginacorretafoiusada,mastambémseo
modeléoesperado?Simples!
void "testando o model de uma action"() {
when:
controller .renderGSP()
then:"o model deve ter a chave nome"
model.nome == "Henrique"
view == "/testes/renderGSP"
}
Outroatributoéincluídonaclassedeespecificação: view,quearmaze-
naráonomedaviewusadanarenderizaç ão. Observequeéusadoocami-
nhocompletoparaestevalor. Reparouqueéincluídotambémumatributo
model? Eleéusadoparaverificarseoquefoienviadoparaapáginaestá
corretamentepreenchido.
T estando um model
Jáquefalamosdemodel,quetalexporcomotestarum? Imagineesta
action:
def actionModel() {
[nome:"Henrique", idade:10000]
}
Nemprecisamosdeatributosespeciaisemnossaclassedeespecificações
nestecaso.Bastadeclararmosanossaprópriavariávelsequisermos.Afinal
decontas,écódigoGroovycomoqualqueroutro.
356

## Página 363

CasadoCódigo Capítulo10. Testes
def "como verifico um model?"() {
when:
modelo = controller.actionModel()
then:
modelo.nome == "Henrique"
modelo.idade > 9000
}
T estando redirecionamentos
Talveznossocontroladorpossuaumaactionqueselecioneoqueousuário
deveacessarcombasenoparâmetroidade,comonocódigoaseguir:
def filtroIdade(int idade) {
if (idade > 18) {
redirect(action:"entrada")
} else {
redirect(uri:"http://www.disney.com")
}
}
Comotestamosisso?
def "usuário maior de idade"() {
when:
controller.filtroIdade(21)
then:
response.redirectedUrl == '/testes/entrada'
}
def "usuário menor de idade"() {
when:
controller.filtroIdade(17)
then:
response.redirectedUrl == 'http://www.disney.com'
}
Verificando respostas nos formatos JSON e XML
NãosãorarososmomentosnosquaisvocêiráusarGrailsparacriarAPIs
357

## Página 364

10.3. Escrevendotestesunitáriosparacontroladores CasadoCódigo
oumicrosserviços. Nessescasosaescritadetesteséfundamentale,claro,
Grailsnãoirianosdeixarnamãoaqui.
Sendoassim,vamosaalgunsexemplosnosquaisvamosespecificarofun-
cionamentodosnossoscontroladores,primeiroparaoformato JSON.Ima-
ginequetenhamosumaactioncomoaseguinte:
def renderizeJSON() {
render(contentType:"application/json") {
[
titulo:"Falando de Grails",
ano:2015,
capitulos:["Introdução", "Groovy: uma breve introdução",
"Mergulhando em Groovy", "Precisamos falar sobre Grails"
"Domínio e persistência", "Buscas",
"A camada web: controladores", "A camada web: visualizaç
"A camada de negócios: serviços", "Testes",
"Plugins", "Implantação"]
]
}
}
Cujasaídaserásimilara:
{titulo:"Falando de Grails",
ano: 2015,
capitulos:[ "Introdução", "Groovy: uma breve introdução",
"Mergulhando em Groovy", "Precisamos falar sobre Grails"
"Domínio e persistência", "Buscas",
"A camada web: controladores", "A camada web: visualizaç
"A camada de negócios: serviços", "Testes",
"Plugins", "Implantação"]}
Oobjeto responsenosauxiliaaquicomafun ção getJson(ouapenas
jsonseexecutadoapartirdoGroovy)quenosforneceumobjetojáparseado
combasenosvalores JSON.Vejacomoésimples:
void "verificando o retorno em JSON. Será bom o livro?"() {
when:
controller.renderizeJSON()
358

## Página 365

CasadoCódigo Capítulo10. Testes
then:
response.json.titulo == "Falando de Grails"
response.json.ano == 2015
// Verificando uma lista? Simples!
response.json.capitulos.length() > 0
}
Temosumprocedimentobastantesimilaraolidarmoscomactionsque
renderizem XML.Vamosamaisumexemplo.Suponhaaactionaseguir:
def renderizeXML() {
def capitulos = ["Introdução", "Groovy: uma breve introdução",
"Mergulhando em Groovy", "Precisamos falar sobre Grails"
"Domínio e persistência", "Buscas",
"A camada web: controladores", "A camada web: visualizaç
"A camada de negócios: serviços", "Testes",
"Plugins", "Implantação"]
render(contentType:"text/xml") {
livro(titulo:"Falando de Grails", ano:2015) {
indice() {
for (capitulo in capitulos) {
cap(titulo:capitulo)
}
}
}
}
}
Asaídadestaactionseráo XML:
<livro titulo= "Falando de Grails" ano="2015" >
<indice>
<cap titulo="Introdução"/>
<cap titulo="Groovy: uma breve introdução"/>
<cap titulo="Mergulhando em Groovy"/>
<cap titulo="Precisamos falar sobre Grails"/>
<cap titulo="Domínio e persistência"/>
<cap titulo="Buscas"/>
<cap titulo="A camada web: controladores"/>
<cap titulo="A camada web: visualização"/>
359

## Página 366

10.4. Testandobibliotecasdetag CasadoCódigo
<cap titulo="A camada de negócios: serviços"/>
<cap titulo="Testes"/>
<cap titulo="Plugins"/>
<cap titulo="Implantação"/>
</indice>
</livro>
Comoseriaonossoteste?
void "testando o retorno em XML"() {
when:
controller.renderizeXML()
then:
response.xml.@titulo.text() == "Falando de Grails"
response.xml.@ano == 2015
// listando com a lista de itens no índice?
response.xml.indice.list().size() > 0
}
Assimcomonocasodostestesenvolvendo JSON,aquiháumnovoatri-
buto, xml,quenosretornaráoconteúdoretornadointeiramenteparseado.
Hápequenasdiferençasnestecaso.Primeiro,parareferenciaratributos,você
precisaráusarooperador @.Segundo,paraoacessoalistadetagsvocêpre-
cisaráusarafunção list()talcomoexpostonoexemplo.
10.4 T estando bibliotecas de tag
Quandodescobriqueerapossíveltestar tag librariescomGrailsanosatrás
confessoqueminhaprimeirasensaçãofoichoque:atéaquelemomento,ode-
senvolvimentodestetipodeartefatoeraessencialmenteinterativo;euapenas
modificavaocódigo-fonteeemseguidaverificavavisualmentesemeatendia.
ComGrails,pelaprimeiravezcomeceiamudarminhavisãosobreestemodo
detrabalho.
Esabemoqueémaislegal?Essencialmenteháumaúnicamaneiraque
iráatendertodasassuasnecessidades. Sendoassim,talcomofiznocaso
doscontroladores,vamosimplementarumabibliotecadetagbemsimplória
apenasparailustrarosconceitos.Comecemospelacriaçãodanossabiblioteca
360

## Página 367

CasadoCódigo Capítulo10. Testes
usandoocomando create-tag-lib Testes,queirágerarparanóstanto
oesqueletodanossabibliotecaquantodasuaespecificaç ãoSpock.
Oiníciodanossa specvocêjápodeimaginarcomoé:
package concot
import grails.test.mixin.TestFor
import spock.lang.Specification
@TestFor(TestesTagLib)
class TestesTagLibSpec extends Specification {
}
Seráincluídonomomentodaexecuçãodostestesumnovoatributoem
TestesTagLibSpecchamado tagLib,queusaremosparaescrevernossos
comportamentos. Comecemospelatagmaissimpleseinútilpossível:uma
quesempreimprimaomesmoconteúdo.
def apenasUmTexto = { atributos, corpo ->
out << "Teste!"
}
Toda tag ao ser exeutada na realidade retorna um objeto do tipo
org.codehaus.groovy.grails.web.util.StreamCharBuffer. O
querealmentenosinteressaétransformá-loemtextoparaveroqueobtive-
moscomoresultado. Como faço isso? Bastachamarafun ção toString()
talcomofizemosemnossaprimeiradescriç ãodecomportamento.
def "quando é um texto simples..."() {
when:
// reparou no toString()?
def resultado = tagLib.apenasUmTexto().toString()
then:
resultado == "Teste!"
}
Sequiser,tambémpodeusarafun ção assertOutputEquals,emque
sóprecisamosdobloco expect:.
361

## Página 368

10.5. Testesintegrados CasadoCódigo
def "e como uso assertOutputEquals?"() {
expect:
/* Basta apenas digitar como a tag seria
usada no seu código GSP. Simples, não? */
assertOutputEquals "Teste!", "<g:apenasUmTexto/>"
}
Massabe,muitasvezesvocêquerapenasverificarseumpedaçobate.Não
serialegalpoderusarumaexpressãoregular?Vocêpode,bastausarafun ção
assertOutputMatches!
def "e se eu quiser uma expressão regular?"() {
expect:
// Atenção para o uso dos parênteses para assertOutputMatches
// eles são necessários ao lidarmos com expressões regulares
assertOutputMatches(/.*este.*/, "<g:apenasUmTexto/>"
}
10.5 T estes integrados
Éfundamentalquevocêselembredealgumasdiretrizesbemsimplesaoes-
creverseustestesunitáriosemGrails.Aprimeiradelaséselembrar por que
vocêosestáescrevendo.Sãoumaferramentadedesigneverificaç ãoquelhe
permitefocarsuaaten çãoapenasnaquelafuncionalidadecomqueestáli-
dando naquelemomento.
Seseutesteunitárioenvolvemaisdeumaclasse,easferramentasdemock
oferecidaspeloframeworknãolheatendem,repenseduascoisas:seráqueseu
códigonãoestámaiscomplicadodoquedeveriaevocêdeveriarepensarseu
design?Easegundaé:seráquevocênãodeveriaestarescrevendotestesde
integração?
Nestaseção,finalmenteveremoscomotrabalharcomtestesintegrados.A
boanotíciaéqueoquevimossobretestesintegradosseaplicaperfeitamente
aestetipodetestes,mascomumadiferen ça:vocênãoprecisacriarmocks,
poistodoosistemaestarádisponíveletudooqueénecessáriofazeréinjetar
aquilocujocomportamentoqueremosprojetarouverificar!
Vamos aqui reescrever a especificação que Daniel criou para
ListaCotacoesService. Você pode criar testes usando o comando
362

## Página 369

CasadoCódigo Capítulo10. Testes
create-integration-testdoGrails,quecriaráumarquivonapasta
test/integrationseguindoonomedopacoteeonomedotesteaser
criado. Emnossocaso,oconteúdodosnossostestesdeintegraç ãoemseu
estadoinicialpodeservistoaseguir:
package concot
import grails.test.spock.IntegrationSpec
class ListaCotacoesServiceIntegrationSpec extends IntegrationSpec {
def setup() {
}
def cleanup() {
}
void "test something"() {
}
}
Hápoucasmudanças:nossaclasseagoraestende IntegrationSpece
nãomais Specification,porémnomomentoemqueestiverescrevendo
suasespecificaçõesvocênãoprecisasepreocuparcomisto.Bastaagirquase
exatamentecomofarianocasodostestesunitários.
Outradiferençaimportanteéquenãousaremosmaisasanotações @Mock
e TestFor,poisnãoprecisamossimularnenhumcomponentedosistema:a
aplicaçãoestaráinteiramentedisponívelparanósagora.Osmétodos setup
e cleanuptambémfuncionamexatamentedamesmamaneira.Adiferen ça
équeagoravamosinteragircomelementosreaisdanossaarquiteturacomo,
porexemplo,seuSGBD.
Como não iremos simular objeto algum, podemos injetar o serviço
ListaCotacoesServiceemnossotesteintegrado:
import grails.test.spock.IntegrationSpec
import spock.lang.Shared
class ListaCotacoesServiceIntegrationSpec extends IntegrationSpec {
363

## Página 370

10.5. Testesintegrados CasadoCódigo
def listaCotacoesService
Deresto,bastaescreverseustestestalcomofoifeitonocasodostestes
unitários.Agrandediferen çaestaránofatodequeagoravocênãoirárefe-
renciar service,massim listaCotacoesService,enestemomento
vocêjásabefazerisso.;)
ÉimportantesalientaroutroscomportamentosadotadosporGrailsna
execuçãodostestesintegrados.Oprimeirodelesdizrespeitoaofatodeque
cadatesteéexecutadoemsuaprópriatransaç ão.Finalizadasuaexecução,é
feitoorollbackdatransaçãoe,comisso,evita-sequesejageradolixonoseu
bancodedadosdetestes.
Sequiserdesabilitaressecomportamentotransacional,bastaincluiro
atributoestático transactionalcomvaloriguala false,exatamente
comofaríamosseestivéssemosescrevendoumserviço.Apenaspararelem-
brar,observecomopoderíamosdesabilitaranaturezatransacionaldostestes
integradosaseguir:
import grails.test.spock.IntegrationSpec
import spock.lang.Shared
class ListaCotacoesServiceIntegrationSpec extends IntegrationSpec {
static transactional = false
}
Coisas que você deve levar em consideração em seus testes de inte-
gração
Oprimeiropontoaserlevadonaescritadetestesintegradoséofatode
mocksseremcompletamentedesnecessários.Casosepegueemumasituaç ão
naqualsevejafor çadoacriarummock,repense:deveríamosrealmenteestar
escrevendoumtesteintegrado?
Umaboapráticaaserlevadaemconsideraç ãonaexecuçãodetestesin-
tegradoséconfiguraro data source paraoambientedetestesparaque
obancodedadossejacriadoaoiniciarmosabateriadetestesedestruídoao
364

## Página 371

CasadoCódigo Capítulo10. Testes
seufinal. Issoevitaquesuaequipededesenvolvimento“vicie”obancode
dados,oqueterminariaportransferiroclássicoproblemado“naminhamá-
quinafunciona”parao“nomeuambientedetestesfunciona”.Fundamentalé
funcionarnoambientedeprodução!
365

## Página 373

Capítulo11
Modularizandocomplug-ins
Grailsnosforneceumaimensagamaderecursoscomopôdeservistodu-
ranteestelivro. Seoleitormaiscuriosoumdiaquiserentenderafundoo
frameworklendoseucódigo-fonte,observaráalgobastanteinteressante: o
núcleodoGrailsérelativamentepequenoepraticamentetodasasfuncionali-
dades,comooGORMescaffolding,porexemplo,sãonarealidadeplug-ins.
Naverdade,Grailsémaisqueumframeworkparadesenvolvimentoweb:
trata-sedeumaplataformaextensívelquepermiteaqualquerumenriquecê-
locomnovasfuncionalidadesatravésdaescritadeplug-ins.Nestecapítulo,
iremoscriarumplug-inbastantesimplesparaoprojeto ConCot,oquelhefor-
neceráumavisãobastanteinteressantesobreomodocomoesteimportante
elementodaarquiteturaGrailsfunciona.

## Página 374

11.1. Oqueéumplug-in? CasadoCódigo
11.1 O que é um plug-in?
Comosempre,partiremosapartirdadefiniç ãodotermochavedocapítulo
queéapalavra plug-in.Estaserefereaumtipoespecíficodesoftware,aquele
queprovênovasfuncionalidadesaoutropreexistentesemquetenhamosde
alterarseucódigo-fonte.Trata-sedeumpontodeextensãoprovidoporum
estilo arquitetural.
Esse estilo arquiteturaléoquepermiteaextensãodosoftwareeémuito
importantequevocêocompreendanocontextodoGrails. Aofalarmosde
umaarquiteturaextensível,vêmàmentealgunsexemplosbastanteconheci-
doscomo,porexemplo,osnavegadoresquenospermitemexecutardiferentes
conteúdosapartirdainstalaçãodeplug-ins,comooFlashouJava,oumesmo
soluçõesmaissofisticadascomoOSGi[1]ouJBossModules[18].
Cadaumadestassoluções/arquiteturaspossuialgunsatributosemco-
mum:
• Aaplicaçãohospedeira,quepermiteainstalaçãodeplug-insatravésdo
provimentodepontosdeextensão.
• Osplug-inseomodocomoelessãoimplementadospelosdesenvolve-
dores.
• Otemponoqualplug-inssãocarregados:compilação,execução?
NossaaplicaçãohospedeiraéopróprioGrails(quenarealidadesechama
Grails Core). ÉeleéqueforneceráasAPIsepontosdeextensãoqueserão
usadosnaimplementaçãodosplug-ins.
Comoosplug-inssãoimplementados? Umasurpresaagradávelpara
você:quaseexatamenteigualaomodocomoescrevemosaplicaçõesGrails
quevimosdurantetodoestelivro.Ocódigo-fontedoplug-inpossuiamesma
estruturadearquivosediretórioscomquevocêjáestáhabituadoatrabalhar
emseusprojetosGrails,oquenostrásalgumasvantagens:
• Vocêécapazdedarmanutençãoemplug-inspreexistentespoisjásabe
comoseucódigo-fonteéestruturado.
368

## Página 375

CasadoCódigo Capítulo11. Modularizandocomplug-ins
• Vocêesuaequipesãocapazesdefazeranálisesmaisdetalhadasares-
peitodeumplug-inquevocêsestejampensandoemadotaremseus
projetos.Comisso,onúmerode“surpresasdesagradáveis”decorrentes
daaplicaçãodeplug-insmalcodificadosouquenãoatendamsuasne-
cessidadesdiminuibastante.Pensenasbibliotecasnormalmenteado-
tadasemnossosprojetosJava:quantotempovocêlevariaparaentender
omodocomoseucódigo-fonteéestruturado?
• Já que sua equipe é capaz de entender de forma quase imediata o
código-fontedestescomponentes,épossíveltirarproveitodistopara
sersuaportadeentradaaomundoopensourceprovendomelhoriasa
plug-inspreexistentes(enocódigo-fontedopróprioGrails)oumesmo
provendoseusprópriosprodutos!
Quandopluginssãocarregados? Emtempodecompilaç ão. Vocênão
podecarregarnovosplug-insemumaaplicaç ãoGrailsapósestatersidoim-
plantadaemprodução.
Quando você pode tirar proveito dos plug-ins
Otermochaveaopensarmosemplug-insé componentização:vocêcria
umcomponentequandoobservaanecessidadedeseterdeterminadafunci-
onalidade(ouconjuntode)emmaisdeumprojetoequerevitararepetiç ão
doseuesfor ço.
369

## Página 376

11.1. Oqueéumplug-in? CasadoCódigo
Armadilha: componentização precoce
Fig.11.1:Atençãoredobrada!
Somentecomeceapensarnacriaçãodeumcomponenteapósterob-
servadosuanecessidadeemdoisoumaiscasos.Piorqueoretrabalhoé
acomponentizaçãoprecoceouexcessiva,quepodetornaramanuten ção
dosseusprojetosmuitomaiscomplexa.
Talvezmaisdeumdosseusprojetosnecessitamdefuncionalidadesque
nãoseencontrempresentesnoGrailscomo,porexemplo,interaç ãocomser-
vidoresJMSouagendamentodetarefastalcomoprovidopeloplug-inQuartz
[28].Esteéousomaisintuitivodeplug-ins:provernovasfuncionalidadesao
framework,masnãoéaúnica. Aquiseguemalgumaspossibilidadesigual-
menteinteressantes:
Aprimeiradelaséreaproveitamentodecódigoentreseusprojetos. Se
vocêoptoupeloGrailscomoframework,énaturalqueoapliquemaisdeuma
vezentresuasaplicações.Nãoérarovermosasmesmasclassesdedomínio
(ououtrosartefatos)serepetirementrediferentesprojetos.Pensenasclasses
quevocêcriapara,porexemplo,lidarcomaautenticaç ãoeautorizaçãode
usuários. Porquerepetirestetarefatodavezou,aindapior,ficarcopiando
arquivosdeumpontoparaoutro?Escrevaumplug-inereaproveiteesseco-
nhecimento!
Talvezvocêpossuarecursosestáticosoulayoutsquedesejereaproveitar
emseusprojetosecomissopadronizarsuaidentidadevisualnasuaempresa.
Vocêpodeincluirtodosemummesmoplug-inreaproveitado-osentresuas
aplicações.Implementeumavezseuslayouts,reaproveite-ossemprequepre-
cisar.
370

## Página 377

CasadoCódigo Capítulo11. Modularizandocomplug-ins
VocêpodetambémterimplementadosscriptsGant(Grails2.xe1.x)ou
Gradle(Grails3.xprafrente)queautomatizemepadronizemomodocomo
suaequipetrabalhaedesejaquesejamadotadosemtodososseusprojetos
Grails.
Outrousointeressanteéfazerdinheirocomplug-ins.Nãoéraroencon-
trarmossoluçõesgeniaisquefacilitamimensamenteavidadedesenvolvedo-
respelomundo. Maisàfrentequandoformosfalarsobreempacotamento
deplug-ins,mostrareicomoempacotá-losemarquivosbináriosdisponibi-
lizandoapenasoconteúdobinário. Jápensouemvenderseusplug-insou
mesmodisponibilizá-losparaacomunidade,ganhandocomistoumabela
visibilidadeoudinheiro?Apenasumaideia.;)
Essassãoapenasalgumaspossibilidades:quandofalarmossobremodu-
larização,suaimaginaçãoéolimite,noentantoomaisimportanteequese
manteráemtodasasoportunidadesébastantesimples:aoreaproveitarcó-
digovocêganhatempo,economizadinheiroeconstróiumabasesólidaque
poderáserseugrandediferencialnomercado.Tenhaissoemmente.
11.2 C riando nosso primeiro plug-in
Conformeo ConCotfoievoluindoeamadurecendona DDL Engenhariaa
diretoriacomeçouaseinteressarcadavezmaispelaspossibilidadesqueGuto
alardeava.Tantoqueumdiaapresidentedacompanhia,Dedé,resolveufazer
umavisitaaosprogramadoresdaempresaparaseinterarmaisarespeito.Foi
quandoelaseencontroucomDaniel,queacabavadevoltardocafé.
EaíDaniel,tudobem?Vimaquidizerum“oi”poisestoumuitofelizcom
osavançosquevocêjuntocomGutoeKicotiveramno ConCot.Opessoaldo
departamentodesuprimentosestágostandomuitodoresultado.
MuitobomouvirissoDedé,masvocêveioaquisóprameelogiar???
Sempredesconfiadohein,Daniel? Narealidadevimporquetiveuma
ideia,sabe... Gostomuitodocadastrodeitensdo ConCot,aquelenoqual
vocêsfornecemadescriçãoecategorizamositenscotadospelosistema.Es-
tavapensandosenãoseriapossívelvocê copiarestepedaçoparaumnovo
sistemaaquidaempresa.
Comoassim?
371

## Página 378

11.2. Criandonossoprimeiroplug-in CasadoCódigo
Seguinte:no ConCotagenteapenascotaositens,ouseja,agenteapenas
forneceospre çosqueencontramos,certo?
Sim.
Agoraeuprecisodealgonovo,quenosajudeapreencherumasplanilhas
quefazemosotempointeiroaquinaempresa. Nestasplanilhasincluímos
aquantidadedecadaequipamentoqueadotamosemnossosprojetos. Por
exemplo: iremos usar 4 britadores do tipo X, 6 motores do tipo Y etc.,entende?
Hmm...entendo.
Maisdoqueisto,eutambémgostariaquevocêadicionassemaiscampos
ao Itemquenãoestãorelacionadastantoàscotaçõesquantoaosquantitati-
vos.Queriamelhorarumpoucomaisestadescriç ãocomestesatributos.
Quaisatributos?(Danielcome çaasentiroperigo)
Algunsitenspodemnãosermaisfabricados,sabe? Entãoqueriaum
campochamado“obsoleto”nositens,assimagenteevitariaacotaçãoouin-
clusãodeitensemplanilhasquenãosejammaisfabricados.Etambémseria
muitolegalseagentepudesseincluirobservaçõesnosdescritivosdositens.
Vocêfazissopramim?
MasaíeuvouterdemexernosDOISsistemas!!!!!!
Qualé,cara!!!Vocêéinteligenteenãoirámedecepcionar,certoDaniel?
Claroquenão!(Danielsenteapressão)
Acriaçãodeumplug-inirátornaravidadeDanielmuitomaissimplese
lheeconomizarábastantetempo,alémdelhefornecerumativoreaproveitável
quepoderáserusadoemfuturosprojetosdaempresa(acredite,elessurgirão).
Éfundamentalsaber o quedeveráserincluídoemnossoplug-in.Como
estamosfalandodeativos reaproveitáveise compartilháveis,nãoestamos
falandodosnossoscontroladores.Afinaldecontas,hásempreregrasdena-
vegação(aomenosnocasoda DDL Engenharia)específicasparacadaaplica-
ção.Tambémnãoháregrasdenegócioimplementadasemserviçosreferentes
aoscadastrosdeitensoumesmopáginasatéagora.
Nestemomento,sóconseguimosvercomoativoreaproveitávelasclas-
sesdedomínio.Edadoqueprecisaremosinclusiveincluirnovoscamposque
serãocompartilhadosentreo ConCoteestenovosistema,elasacabamsetor-
nandonossoalvoasercompartilhado.
372

## Página 379

CasadoCódigo Capítulo11. Modularizandocomplug-ins
Criando o plug-in
Omodocomocriamosumplug-inémuitoparecidocomoqueadotamos
aoiniciarmosumprojetoGrailstradicional. Adiferen çaestánocomando:
create-pluginemvezde create-app.Éumaexcelentepráticapadro-
nizarosnomesdosseusplug-insusandoalgumprefixoqueosidentifique
comopertencentesaalgumgrupo(comosuaempresa,plataformaouqual-
queroutroagrupadorquelhefaç asentido).Comonossocontextoéa DDL
Engenharia,nadamaisnaturalqueadotemosoprefixo ddl-pluginenosso
primeiroplug-insechamaráportanto ddl-plugin-itens.Bastaexecutar
ocomandoaseguir:
grails create-plugin ddl-plugin-itens
Serácriadoumdiretóriocomomesmonomedoseuplug-in,exatamente
comoocorrequandocriamosumaaplicaçãoGrailstradicional.Enavegando
porestaárvoredediretóriosvocêsesentiráemcasa.Porquê?Vejaaocon-
teúdodapastacriada.
373

## Página 380

11.2. Criandonossoprimeiroplug-in CasadoCódigo
Fig.11.2:Estruturadediretóriosdoplug-in
Equaloconteúdodapasta grails-app?
374

## Página 381

CasadoCódigo Capítulo11. Modularizandocomplug-ins
Fig.11.3:Estruturadediretóriosdoplug-in
Exatamenteoconteúdoquevocêesperariaseestivessecriandoumaapli-
caçãoGrailspadrão. Eporquê? Porqueplug-insGrails sãoaplicaçõestra-
dicionais! Oconteúdoquevocêincluiránoprojetodoplug-inéquaseque
exatamenteigualaodeumaaplicaçãoconvencional,ouseja,sevocêleueste
livrosequencialmenteatéchegaraestecapítulo,jásabe pelo menos 80% do
queprecisaparacome çaracriarseusprópriosplug-ins!
375

## Página 382

11.2. Criandonossoprimeiroplug-in CasadoCódigo
Mudanças na estrutura de diretórios no Grails 3
Fig.11.4:Compatibilidade
Hápequenasmudançasnaestruturadediretóriosapartirdaversão3
doGrailsconformedescrevemosnoúltimocapítulodestelivro,masnão
seassuste,sãopequenasalteraçõesapenas.
A única diferença na estrutura de diretórios é a presença
de um arquivo que se encontra na raiz do projeto cujo nome é
DdlPluginItensGrailsPlugin.groovy. Grails sempre irá criar
um arquivo chamado [nome do seu plug-in]Plugin.groovy no
qualiremosincluirdiversasmetainformaçõessobrenossoplug-inalémde
tambémincluirpontosdeextensãobastanteinteressantes. Observequeo
prefixoaplicadoaonomedestearquivoconsistiránonomedoseuplug-in
noformato camel casedremovendoocaractere ‘-’.
Identificando o plug-in
Criadooplug-in,oarquivo DdlPluginItensGrailsPlugin.groovy
émuitoparecidoaoqueexpomosaseguir:
class DdlPluginItensGrailsPlugin {
// the plugin version
def version = "0.1"
// the version or versions of Grails the plugin is designed for
def grailsVersion = "2.4 > *"
// resources that are excluded from plugin packaging
def pluginExcludes = [
"grails-app/views/error.gsp"
376

## Página 383

CasadoCódigo Capítulo11. Modularizandocomplug-ins
]
// TODO Fill in these fields
def title = "Ddl Plugin Itens Plugin" // Headline display name of the
def author = "Your name"
def authorEmail = ""
def description = '''\
Brief summary/description of the plugin.
'''
// URL to the plugin's documentation
def documentation = "http://grails.org/plugin/ddl-plugin-itens"
// Restante omitido
}
Paracomeçarmosnossodesenvolvimento,primeiroprecisamosalteraro
valordealgunsatributosdaclasse DDlPluginIntensGrailsPlugin.Va-
mosàschavesprincipais:
•version Onúmerodeversãodoplug-in.Emnossocasomudamos
para 1.0.0.
•grailsVersion ComquaisversõesdoGrailsnossoplug-inécom-
patível.Nonossocaso,manteremosomesmovalor,poisnossoplug-in
foifeitopensadonoGrails2.4,noentantovocêpoderiaescreveralgo
como 1.1 > *,querepresenta“qualquerversãodoGrailsapartirda
1.1emdiante”.
•title O nome amigável do plug-in. Em nosso exemplo será
"Cadastro de itens da DDL Engenharia".Estenomeéoque
seráexposto,inclusive,comotítulonapáginadoplug-innositeoficial
doGrailscasosejapublicadolá.
•author Onomedoautor(ouautores)destecódigo-fonte.
•authorEmail Oe-maildecontatocomoautor.
377

## Página 384

11.2. Criandonossoprimeiroplug-in CasadoCódigo
•description Textodescritivocurtosobreoplug-in.
Adicionando conteúdo ao plug-in
Preenchidososmetadadosnecessários,opróximopassoédarmassaao
plug-in.Nocasodo ConCot,tudooqueprecisamosfazerémoveralgumasde
suasclassesdedomínioparaapasta grails-appdomaindoprojeto DDL
Plugin Itens. Comosóiremoslidarcomocadastrodeitens,asclasses
queiremosmoversão Iteme Categoriadopacote concot.
Parafacilitarnossavidaeparafinsdidáticosapenas,vamosmantera
mesmaestruturadepacotesnocódigo-fontedoplug-in.Emcasosreais,você
iráusarumnomedepacotecustomizadoparaonomedoplug-in.
AgoratudooqueprecisamosfazeréincluiroscamposqueDedépediu
aDanielquefosseincluídosnaclasse Item. Oresultadopodemosverna
listagemaseguir:
package concot
class Item {
String nome
byte[] imagem
boolean obsoleto = false
String observacoes
String toString() {
this.nome
}
static belongsTo = [categoria:Categoria]
static constraints = {
nome nullable:false, blank:false, maxSize:128
categoria nullable:false
imagem nullable:true, maxSize:65536
obsoleto nullable:false
observacoes nullable:true, blank:true, maxSize:1024
}
378

## Página 385

CasadoCódigo Capítulo11. Modularizandocomplug-ins
}
Pormaisincrívelquepossaparecer,nossoplug-inestápronto.Nãopre-
cisaremosmodificarmaisnenhumcódigo-fonteouarquivodeconfiguraç ão.
Querdizer,quasepronto,poisaindaprecisamosusá-lo.
11.3 P lug-ins inline
Movidasasclasses Iteme Categoriadoprojeto ConCot,vocênãoconse-
guirámaisexecutá-loouempacotá-locomoum WARpoisoscontroladores
apontarãoparaclassesquenãoestarãomaisdisponíveisnoclasspathdopro-
jeto.Vocêpoderesolveristodeumaformabastantesimplesreferenciandoo
código-fontedoplug-in DDL Plugin Itens.
Paratal,bastaqueocódigo-fontedoplug-insejaacessívelaodoseupro-
jeto.Vocêprecisaráapenasmodificaroarquivo BuildConfig.groovydo
projeto ConCottalcomonoexemploaseguir:
// Referência ao nosso plug-in
// Repare que incluímos o nome do plug-in como uma string
// ao final da expressão
grails.plugin.location."ddl-plugin-itens" = "../ddl-plugin-itens"
grails.project.dependency.resolution = {
// restante omitido
É muito importante que a instruç ão
grails.plugin.location.[nome do seu plug-in] seja incluída
foradobloco grails.project.dependency.resolution,poisesta-
moslidandocomoutrotipoderesoluç ãodedependênciasaqui: estamos
referenciandodiretamenteocódigo-fontedoplug-in. Quandoexecutamos
comandoscomo run-app, test-appouqualqueroutro,oGrailsirá,por
trásdospanos,mesclarasduasbasesdecódigo:adoplug-ineadaaplicaç ão.
Usarplug-insdeformainlinecomofizemosaquiéumaexcelenteprática
quandovocêestiverescrevendoseusprópriosplug-ins,poiscomistopoderá
testarseufuncionamentoexatamentecomoofariacomumaaplicaç ãoGrails
padrão. Vocêpode,porexemplo,alterarocódigo-fontedoplug-inevero
resultadonoseuprojetoemexecuçãocomocomando run-app.
379

## Página 386

11.4. Empacotandooplug-in CasadoCódigo
11.4 E mpacotando o plug-in
Namaiorpartedasvezesnãousamosplug-insinline,massimprovidospor
terceiros.Nocasoda DDL Engenharia,acreditoquenofuturoirãoadotareste
mesmotipodecomportamentoassimqueestabilizaremasmudan çasneces-
sáriasnasclasses Categoriae Item.
Nocasodeplug-ins, emvezdegerarmosumarquivo WARconven-
cional, vamos gerar por padrão um arquivo com a extensãozip con-
tendotodoocódigo-fontedonossoplug-inusandoocomando grails
package-pluginque,nocasodo DDL Plugin Itensirágerarumarquivo
chamado grails-ddl-plugin-itens-1.0.0.zipnaraizdoprojeto.
Outraalternativainteressanteéochamado plug-in binário,introduzido
comaversão2.0doGrails. Aprincipaldiferen çaestánofatodeocódigo-
fontenãoserincluídonoartefatofinal,massimapenassuaversãocompilada.
Tambémnãoégeradoumarquivo zip,massimumarquivo JARtradicional.
Estaabordagemtrazconsigoalgumasvantagens:
• Vocêpodepublicarseuplug-inemrepositóriosMaventradicionais.
• Vocêpodedeclará-loscomoqualqueroutrabibliotecaJava.
• Dadoqueocódigo-fontenãoéincluídonoartefatofinal,issofacilitaa
suacomercializaçãoemcasosnosquaisnãosejainteressantedisponi-
bilizarestainformação(ocódigo-fonte).
• IDEsconseguemanalisarmelhorasclassesquecompõemseuplug-in.
Para gerar um plug-in binário, você só precisa executar o comando
package-plugin --binary,eserágeradonodiretóriotargetdoprojeto
umarquivocomaextensão jar.Nocasodonossoplug-indeexemplo,este
arquivosechamará grails-ddl-plugin-itens-1.0.0.jar.
Háumavantagemocultanageraçãodeplug-insbinários:dadoqueeles
sãocompiladosantesdeseremempacotados,vocêconseguirádetectarerros
emseucódigo-fontequeimpediriamsuacompilaç ãonomomentoemqueo
plug-infosseusadopeloprojetocliente.
380

## Página 387

CasadoCódigo Capítulo11. Modularizandocomplug-ins
11.5 U sando plug-ins: o arquivo BU I L DCO N F I G.G R O O V Y
A última vez que vimos o arquivo BuildConfig.groovy foi
ao falarmos sobre a configuração do driver JDBC no capítulo em
que abordamos o tema persistência5. Chegou a hora de abor-
dar com detalhes aquela que possivelmente é sua seção mais usada:
grails.project.dependency.resolution.
Énesteblocoqueincluímostodasasdependências,issoé,bibliotecasde
terceirosqueusamosemnossosprojetosGrails(eplug-ins).Emseuinterior,
trêsblocosnosinteressam: repositories, dependenciese plugins.
Bloco repositories
Nestebloco,declaramostodososrepositóriosMavenqueusamosem
nossoprojeto.Casotodasassuasbibliotecaseplug-insnãotenhamsidousa-
dospelasuaequipeevocêsnãopossuamumgerenciadorderepositóriosin-
terno,tudooquevocêdevefazerédeixá-loinalterado.
Por padrão, serão incluídos os repositórios públicos Maven Central,
GrailsCentral(queincluitodasasbibliotecasterceirizadasusadaspelofra-
mework),GrailsPlugins(ondeficaorepositóriooficialdeplug-insdoprojeto
Grails)eGrailsHome(quecontémosplug-insprincipaisusadospeloGrails
Core).
Casosejanecessárioincluirrepositóriosterceirizados,tudooquevocê
precisafazeréincluirumachamadaàfun ção mavenRepo,passandocomo
valoraURLdorepositórioaserincluído.Noexemploaseguirpodemosver
acustomizaçãodestebloco:
repositories {
grailsPlugins()
grailsHome ()
mavenLocal ()
grailsCentral()
mavenCentral()
// Adicionando mais um repositório
mavenRepo "http://repository.codehaus.org"
}
381

## Página 388

CasadoCódigo
Bloco dependencies
Nesteblocovamosdeclarartodasasdependênciasexternasnecessárias
paraaexecuçãodonossoprojetoquenãosejamplug-ins. Aidentificaç ão
dasdependênciaséfeitaadotando-seasconven çõesdoMavenquevimosno
capítulosobrepersistência5.4,comonoexemploexpostoaseguir:
dependencies {
runtime 'mysql:mysql-connector-java:5.1.24'
build "org.fusesource.jansi:jansi:1.11"
}
Paracadalinhadeclara-seumadependênciacomseurelativoescopoque,
atualmente,podevirnosseguintessabores:
•build Adependênciaéusadaapenasduranteoprocessodebuildda
aplicação,ouseja,quandoexecutamososcomandosdisponibilizados
peloCLIdoGrails.
•runtime Adependênciaseráincluídanoartefatofinaldaaplicação,
ouseja,estarácontidanoarquivo WARqueiremosgerar.
•compile Adependênciaénecessáriaduranteosmomentosdecom-
pilação(compile time)e runtime.
•test Adependênciaestarápresenteapenasduranteaexecuçãodos
testesautomatizadosdoprojeto. Afinaldecontas,paraqueenviaras
bibliotecasdoSpockparaoseuservidor?
•provided Aaplicaçãoprecisadadependênciaemtempodeexecu-
ção,noentantoelajáéprovidapeloservidordeaplicaçõesouservlet
container.Exemplo:aAPIServlet.
Bloco plugins
Éoblocoquerealmentenosinteressaquandooassuntoéousodeplug-
ins. Seufuncionamentoéexatamenteigualaodobloco dependencies.
Adiferençaestánofatodequeaquisãodeclaradososplug-insusadospela
nossaaplicação.
382

## Página 389

CasadoCódigo Capítulo11. Modularizandocomplug-ins
Normalmente,tudooquevocêprecisafazerparausarseusplug-inséco-
piarparaesteblocoadeclaraçãodedependênciafornecidapelosprópriosau-
toresdoplug-in.NocasodoSpringSecurityCore,porexemplo,bastaincluir
aseguinteinstrução:
plugins {
compile ":spring-security-core:2.0-RC4"
// restante omitido para fins didáticos
}
BuildConfig.groovy não existirá no Grails 3
Fig.11.5:Compatibilidade
Aversão3.0doGrailssubstituioGantcomoferramentadebuildpadrão
doframeworkpeloGradle,umaalternativamuitomaispoderosaetambém
inteiramentebaseadanalinguagemGroovy. Essaéumamudan çabastante
profundanofuncionamentointernodoframeworke,dentreasprincipais
mudançasestáofatodequeoarquivo BuildConfig.groovynãomais
existiráemfuturasversõesdoframework.
Apartirdaversão3.0doframework,todososplug-inspassarãoaser
empacotadosporpadrãonoformatobinário,eseuusopelasaplicaçõesserá
exatamentecomoofaríamoscomqualqueroutrabibliotecaouframework
Java.VamosapenasreferenciarsuaidentificaçãonopadrãoMaven.
11.6 O que não entra no plug-in
383

## Página 390

CasadoCódigo
11.6. OQUENÃOENTRANOPLUG-IN
Tãoimportantequantosaberoqueincluímosemumplug-inéalistadosar-
tefatosquenãosãoincluídosnadistribuiç ãodosnossosplug-inspeloGrails.
Éumalistarelativamentepequena:
•grails-app/conf/BootStrap.groovy
•grails-app/conf/BuildConfig.groovy (apesar de que é
usado para incluir no pacote do plug-in um arquivo chamado
dependencies.groovy,quelistatodasasdependênciasnecessárias
paraaexecuçãodoplug-in).
•grails-app/conf/Config.groovy
•grails-app/conf/DataSource.groovy
•grails-app/conf/UrlMappings.groovy
•grails-app/conf/spring/resources.groovy
• Tudooqueestivernodiretório/web-app/WEB-INF
• Tudooqueestivernodiretório/web-app/plugins/
• Tudooqueestivernodiretório/test/
Além desta lista padrão, você também pode instruir o Grails a não
incluir parte do seu código-fonte na distribuição do seu plug-in. Para
tal, basta que no arquivo de descrição do plug-in (em nosso caso,
DdlPluginItensGrailsPlugin.groovy) seja preenchido o atributo
pluginExcludestalcomonoexemploaseguir, emqueinformamoso
Grailsanãoincluiroarquivo grails-app/views/error.gsp:
def pluginExcludes = [
"grails-app/views/error.gsp"
]
384

## Página 391

CasadoCódigo Capítulo11. Modularizandocomplug-ins
Customizarosarquivosquepodemounãoserincluídosnoartefatofinal
doseuplug-inpossibilitaaodesenvolvedorcriaroseupróprioambientede
desenvolvimentoparaageraçãodestetipodeprojeto.Asemelhan çadosplug-
inscomaplicaçõesGrailspadrãonãoestáapenasnaestruturadearquivose
diretórios: todososcomandosdoCLIdoGrailsfuncionamnodesenvolvi-
mentodeplug-ins.
Sendoassim,vocêpode,porexemplo,criarcontroladoresearquivosGSP
parasimularocomportamentodoseuplug-inemoutrasaplicaçõese,nahora
degeraropacotefinal,simplesmenteexcluirestesartefatosdageraç ãofinal.
11.7 A dicionando métodos dinâmicos em tempo
de execução
11.7. ADICIONANDOMÉTODOSDINÂMICOSEMTEMPODEEXE-
CUÇÃO
Escreverplug-insvaialémdesimplesmentefornecerclassesdedomínio,ser-
viço,controladoreserecursosestáticos.JáseperguntoucomooGORMadi-
cionatodosaquelesmétodosemnossasclassesdedomínio?
No arquivo descritor de plug-ins há um atributo chamado
doWithDynamicMethods, que recebe como valor uma closure cujo
único parâmetro se chamaapplicationContext (que é o contexto
do Spring). Mas o que realmente nos interessa é um atributo chamado
grailsApplication,quenosforneceacessoatodososartefatospadrão
doGrailscomo,porexemplo,controladores,classesdedomínioeserviços.
Noexemploaseguirvamosincluirummétodoqueapenasimprime“Olá
mundo”emtodososcontroladoresdoprojetonoqualoplug-inforaplicado.
def doWithDynamicMethods = { applicationContext ->
for (controlador in grailsApplication.controllerClasses) {
controlador .metaClass.digaOi = {->
println "Olá mundo"
}
}
}
O objeto grailsApplication é uma implementação da interface
385

## Página 392

CasadoCódigo
grails.commons.GrailsApplication. Paraacessaralistadeartefa-
tospertencentesadeterminadacategoria,bastausaraseguinteconven çãoao
buscarporestapropriedade: <tipo do artefato>Classes,ondetipo
doartefatopodeser:
• domain
• controller
• tagLib
• service
• codec
• bootstrap
• urlMappings
11.8 E ntendendo a sobrescrita de artefatos em
plug-ins
11.8. ENTENDENDOASOBRESCRITADEARTEFATOSEMPLUG-
INS
Émuitoimportanteentendercomoosartefatospresentesemumplug-insão
inseridosnaaplicaçãocliente,poisissolhepossibilitacustomizarofuncio-
namentodosseusplug-inssemmodificarseucódigo-fonteetambémevitar
problemasque,semesteconhecimento,sãobemdifíceisdeseremdetectados
eentendidosaousarmosumplug-in.
Aoexecutarmoscomandosqueenvolvamoempacotamentodeumaapli-
caçãoousuaexecução(incluindoexecuçãodetestes),oGrailsirácopiaro
código-fontedosplug-insparadentrodaestruturadediretóriosdaaplica-
ção.Noentanto,casonaaplicaçãoexistaalgumartefatocujonomecompleto
(oqueincluiodiretórionoqualencontra-searmazenado)coincidacomo
nomedoartefatopresenteemalgumplug-in,serámantidaaversãopresente
nocódigo-fontedaaplicação.
386

## Página 393

CasadoCódigo Capítulo11. Modularizandocomplug-ins
Sendo assim, voltando aoConCot, imagine que exista o arquivo
grails-app/domain/concot/Itemtantonocódigo-fontedaaplicaç ão
quantonoplug-inqueconstruímosnestecapítulo.Serámantidoaquelepre-
senteno ConCot.
11.9 P reparando-se para o Grails 3
11.9. PREPARANDO-SEPARAOGRAILS3
Enquantoestelivroéfinalizado,aversão3.0doGrailsseaproxima.Atéeste
momentousamosapenasaversão2.4.4paranossosexemplos,noentantoé
importantequevocêsaibadealgumascoisasqueirãomudaromodocomo
lidamoscomplug-ins.
Paracomeçar,omodocomooscriamoscontinuarásendoexatamenteo
mesmo.Ocomando create-pluginaindaexistirá,assimcomotodosos
demais.Aprincipalmudan çaocorreránomodocomoosempacotamos.O
modelopadrãoagoraseráobinário,possibilitando-noscomistotirarmá-
ximoproveitodainfraestruturaderepositóriosMavenjáexistentehoje.
Omodocomousamosplug-instambémserámodificado.Nãomaisusa-
remosoarquivo BuildConfig.groovyparadeclararnossasdependências,
massimosarquivosdeconfiguraçãodoGradle.Infelizmente,aindaestamos
noreleaseRC-1doGrails3.0,eascoisasestãosemodificandocommuitara-
pidez,noentantoapróximaatualizaçãodestelivro(queseráembreve,assim
quesairaversãofinaldoGrails3.0)conterámaioresinformaçõessobrecomo
proceder.
387

## Página 395

Capítulo12
Grails3.0
Fig.12.1:Compatibilidade
Aversão3.0doGrailssaiuenquantoeuterminavaestelivro.Atéaquitraba-
lhamoscomaversão2.4.4,masnãoseassuste:oqueaprendemossemanterá

## Página 396

12.1. SaioGant,entraoGradle CasadoCódigo
nanovaversãoetodooseuaprendizadonãoseráperdido,noentantoéim-
portantequesejamexpostasasprincipaismudan çasqueestanovaversãonos
traz.
Umpoucoantesdesairaversão3.0,saíramasversões2.4.5,quecontém
algumascorreçõesdebugsea2.5.0.Aprincipalnovidadenaversão2.5foram
asversõesdoSpringeGroovyqueforammudadaspara,respectivamente,as
versões4.1e2.4.Sendoassim,oquevimosatéaquinãomudaemquasenada.
12.1 S ai oGant , entra o Gradle
Desdesuaprimeiraversão,Grailssempreusoucomomecanismodebuildo
Gant,queéumaferramentadeconstruç ão(build)bastantepoderosaeque
nosserviumuitobemportodoesteperíodo.Noentanto,conformeotempo
foipassandonovasop çõesforamsurgindo,dentreelasoGradlequevaialém
doGant:trata-sedeumaferramentadegerenciadeprojetosquelidadesdea
gestãodedependências,padronizaçãodediretórios,ciclodevida,construç ão
emuitomais.PensenoGradlecomoum Gant com anabolizantes.
ÉporestarazãoquenãofalamossobreoGantnestelivro:esteéumco-
nhecimentoquevocê não levaráparaoGrails3.0. Daquiparafrente,será
apenasoGradle,queagorapermeiatodaaconstruç ãodoframework. Esta
mudançanãoveioapenasparajogarforatodososseusvelhosscriptsdebuild
escritosemGant.Hávantagenssignificativasnaado çãodoGradlecomo:
• MelhorsuportedasIDEs:serápossível,porexemplo,usarseusprojetos
GrailscomaversãogratuitadoIntelliJ,queoferecesuporteaoGradle.
• Aadoçãodeumaferramentadegestãodeciclodevidacomumaco-
munidadedeusuários muitomaioremaisativa.
• MuitomaisfacilidadesnaintegraçãodoseuprojetoGrailscomfer-
ramentasdeintegraçãocontínuacomoJenkins,Hudson,TeamCitye
muitasoutras.
• OGradlepossuiumaquantidadeimensadeplug-insdaqualvocêpo-
derátirarproveitoemseusprojetos.
390

## Página 397

CasadoCódigo Capítulo12. Grails3.0
Nova estrutura de arquivos e diretórios do projeto
UmadasconsequênciasinteressantesnaadoçãodoGradlefoiamudan ça
naestruturadediretóriosdeprojetosGrails.Sãomudan çasque,secompara-
dasàsversõesanterioresdoGrails,inclusivefazembastantesentido.Primeiro
vamosàmudan çadelocalizaçãodealgunsdiretórios:
•src/groovy e src/java Agora se encontram em
src/main/groovy. Grails é esperto o suficiente para conseguir
distinguircódigoJavadeGroovy. Éumamudan çabastanteinteres-
sante,poisnapráticatrata-sedeumdiretórioamenosparavocêse
preocupar.
•test/unit Agoraseencontraem src/test/groovy.
•test/integration Foipara src/integration-test/groovy.
•web-app Mudou-separa src/main/webapp.
Algunsarquivostambémmudaramde“endereço”oumesmodeixaram
deexistir,sendosubstituídosporalgumaoutrasoluç ão.
•grails-app/conf/BuildConfig.groovyNãomaisexiste,agora
todasasconfiguraçõesdeconstruçãoencontram-senoarquivodopró-
prioGradle,queficanaraizdoseuprojetoesechama build.gradle.
•grails-app/conf/Config.groovy Agora se chama
application.groovy e foi renomeado com o objetivo de ficar
maispróximodopadrãoadotadopeloSpringBoot(falaremosmais
sobreeleaseguir).
•grails-app/conf/UrlMappings.groovyUmamudançaquefez
bastantesentido:agoraficaem grails-app/init,poisodiretório
grails-app/confnãoémaisconsideradoumlocalondeéarmaze-
nadocódigo-fonte(oarquivo Config.groovyédeconfiguração).
•*GrailsPlugin.groovy Agoraficaráem src/main/groovy.
391

## Página 398

12.1. SaioGant,entraoGradle CasadoCódigo
AlgunsarquivosnãoexistemmaisnoGrails3.0,masnadacomoqual
vocêdevasepreocupartambém. Napráticasuavidaacabouficandoum
poucomaissimplesagora.Seguealista:
•application.properties Napráticasóusávamosestearquivo
paradefinironúmerodeversãodoprojeto.Dadoqueagoraestamos
usandooGradle,eemseuarquivodeconfiguraç ão build.gradleé
possíveldefinirpropriedadesrelativasaoqueseráconstruído,porque
nãousá-lo?Eissofoifeito,poiselefoisubstituídopor build.gradle.
•grails-app/conf/DataSource.groovy Yeap,
não mais existe. Você agora usará apenas o arquivo
grails-app/conf/application.yml sobre o qual falare-
mosmaistarde.Éumaboanotícia,poistrata-sedemenosumarquivo
deconfiguraçãoparanós.
•web-app/WEB-INF/applicationContext.xml Estearquivoque
era instalado pelo comandoinstall-templates foi removido.
Agora todos os seus beans customizados deverão ser incluídos em
grails-app/conf/spring/resources.groovy.
•web-app/WEB-INF/sitemesh.xmlOfiltrodoSitemeshnãoémais
usado,entãooarquivosetornacompletamentedesnecessárioagora.
Apasta target,naqualanteseraincluídooarquivo WARgeradopelo
comando wartambémnãoexistemais.Foisubstituídaporoutrachamada
build.
Seu novo arquivo de configuração: application.yml
Oantigoarquivo grails-app/conf/Config.groovyfoisubstituído
por grails-app/conf/application.yml,queadotaoformato YAML
(Y et Another Markup Language). Esteseráoformatopadrãoadotadopelo
framework.
No entanto, caso prefira o formato Groovy, basta pegar seu ar-
quivo grails-app/conf/Config.groovy e renomeá-lo para
application.groovy que deverá funcionar sem problemas na maior
392

## Página 399

CasadoCódigo Capítulo12. Grails3.0
partedoscasos.Éimportantesalientarque,nestemomentoemqueapenas
temos o Grails 3.0-RC1, não temos ainda certeza se este procedimento
funcionarásemqualquertipodetranstornoparavocês.
Valerelembraraquioquefoiditoagorahápouco:oconteúdodoarquivo
DataSource.groovyagoraseencontraemsuaintegridadeaqui,sendoas-
simémenosumarquivoparavocêsepreocupar.Porumladoissoébom,por
outro,trata-sedeumarquivomaioragoratambém.
Não existe mais a pasta lib
Umdosdiretóriosmaisúteisquandoprecisávamosreaproveitarcódigo-
fontelegadoeraestediretórionoqualcopiávamosnossosarquivos JAR.
Como você deverá fazer isto agora? Simples, basta usar o arquivo
build.gradle que lhe parecerá bastante familiar, visto que o arquivo
BuildConfig.groovycomotempofoiseaproximandoaospoucosdeste
emseuformatoeaparência.
Nelehátambémumblocochamado dependenciese repositories.
Nocaso,paracriarsuaprópriapasta“libretrô”bastaseguiresteprocedi-
mento.
1) Crieumapastachamada libnaraizdoseuprojeto.
2) Editeoarquivo build.gradleparaquefiquesimilaraoexemploase-
guir:
repositories {
// Adicione o bloco "flatDir"
flatDir {
dirs 'lib'
}
}
Inclusão de plug-ins
Nãohámaisoarquivo BuildConfig.groovycomojádissenestecapí-
tulo,sendoassim,bastaagorausaroarquivo build.gradle.Neste,háum
blocochamado dependencies.Novamente,tudooquevocêprecisafazeré
393

## Página 400

12.2. Umanovabase:SpringBoot CasadoCódigo
declararseuplug-incomosefosseumadependência,exatamentecomofaria
antes.Adiferen çaéquenãohámaisobloco plugins.
12.2 U ma nov a base: S pring Boot
Semsombradedúvidas,umdosprojetosmaisimportanteseexcitantesden-
trodoecossistemaSpringlan çadonosúltimosanosfoio Spring Boot.Assim
comoGrails,trata-sedeum metaframework,construídocombasenoSpring
4.1,quenostrazumasériedevantagensefacilidadesinteressantes:
• PossibilitaempacotarnossosprojetoswebcomoarquivosJAR.Nestes
arquivosseráembutidoumservletcontainer(TomcatouJetty),facili-
tandobastanteoprocessodeimplantação.
• Umaarquiteturademódulosextremamentericaefácildeusar. Você
temacessoa,porexemplo,módulosdeauditoria,seguran çaetodoo
ecossistemaSpringacessíveldeumaformaextremamentesimples.
Nestemomento,aprincipalnovidadepráticaparanóséainclusãode
umnovocomandochamado package,queirágerarumarquivo JARno
interiordapasta builddoseuprojeto.Comele,vocênãoprecisamaisfazer
aimplantaçãoemumservidordeprodução.Bastaexecutarocomando java
-jar [nome do arquivo gerado].jar esuaaplicaçãoseráiniciada.
PortrásdospanosoGrails,oumelhor,oSpringBoot,iráembarcaro
Tomcatemsuaaplicação,oquepoderáfacilitarbastanteaimplantaç ãodo
seuprojeto,vistoquenãoémaisnecessáriogerarum WAReexecutaropro-
cedimentodeimplantação(deploy)padrãodoseuservidordeaplicaç ãoou
containerservlet.
Claro,ocomando waraindaexisteepermanecerácasosejanecessário
gerarum WAR.Quandousarumououtro?Dependemuitodocaso.Sevocê
precisadopoderdeumservidordeaplicações, WARéocaminho,especial-
mentequandoaconfiguraçãodopooldeconexõescomobancodedadosé
feitaporele.Nocasodo JAR,modificaropoolirárequererageraçãodeum
novopacote.
394

## Página 401

CasadoCódigo Capítulo12. Grails3.0
12.3 Q ual o melhor caminho para o upgrade?
DeacordocomaequipededesenvolvimentodoGrails[27],oprocedimento
maisfácilconsisteemexecutarospassosaseguir.
1) CrieumnovoprojetocomoGrails3.0-RC1;
2) Copieseucódigo-fontedoprojetoantigoparaonovo;
3) Atualizeseusarquivosdeconfiguração.
Infelizmenteéumprocessomanualnestemomentoequepodeserum
poucotrabalhoso,masnãoéumatarefatãohercúleaquantoaparenta.
12.4 Finalizando?
Sevocêchegouaofinaldestelivroeoleudecaboarabo,ésinaldequegostou
doqueviuaqui. Muitoobrigado! EsperoquetenhaficadoclaroqueGrails
émuitomaisqueumframeworkparadesenvolvimentowebouumaplata-
forma:trata-sedeumamaneiradiferentedevermoseusarmosaplataforma
JavaEE.
Aversão3.0éemsuaessênciaumareescritaquasecompletadofra-
mework,noentantoéinteressanteobservarqueestemododetrabalhose
mantevepraticamenteinalterado. Aindaháasmesmasconven ções(apenas
algunsarquivosmudaramdelugar),amesmainterfacedelinhadecomando
e,oqueconsideromaisimportante:trata-sedeumaferramentaquenosfaz
repensardeumaformabastanteprofundaamaneiracomaquallidamoscom
umadasplataformasmaispoderosasdahistóriadacomputaç ão,queéoJava
EnterpriseEdition.
Acreditoqueaindaháumalonguíssimaestradapelafrenteparaestefra-
mework,especialmenteparaastecnologiasbaseadasemGroovyquevimos
nosprimeiroscapítulosdestelivro.Tor çoparaquesenopiorcasopossível,
ouseja,sevocêjamaisvierausaroGrailsemseusprojetos,aomenosele
tenhatefor çadoarepensarseumododetrabalho.
Muitoobrigado!
395

## Página 403

Capítulo13
Apêndice1 Listadedialetosdo
Hibernate
• Caché2007.1org.hibernate.dialect.Cache71Dialect
• CUBRID8.3+org.hibernate.dialect.CUBRIDDialect
• Oracle9DataDirectDriverorg.hibernate.dialect.DataDirectOracle9D
• DB2/390org.hibernate.dialect.DB2390Dialect
• DB2/400org.hibernate.dialect.DB2400Dialect
• DB2org.hibernate.dialect.DB2Dialect
• Derby10.5org.hibernate.dialect.DerbyTenFiveDialect

## Página 404

CasadoCódigo
• Derby10.6org.hibernate.dialect.DerbyTenSixDialect
• Derby10.7org.hibernate.dialect.DerbyTenSevenDialect
• Firebirdorg.hibernate.dialect.FirebirdDialect
• Frontbaseorg.hibernate.dialect.FrontBaseDialect
• H2org.hibernate.dialect.H2Dialect
• HSQL(HyperSQL)org.hibernate.dialect.HSQLDialect
• Informixorg.hibernate.dialect.InformixDialect
• Ingres10+org.hibernate.dialect.Ingres10Dialect
• Ingres9.3+org.hibernate.dialect.Intres9Dialect
• Ingres9.2org.hibernate.dialect.IngresDialect
• Interbaseorg.hibernate.dialect.InterbaseDialect
• JDataStoreorg.hibernate.dialect.JDataStoreDialect
• McKoiSQLorg.hibernate.dialect.MckoiDialect
• MySQL5org.hibernate.dialect.MySQL5Dialect
• MySQL 5.x para o motor de armazenamento InnODB
org.hibernate.dialect.MySQL5InnoDBDialect
• MySQLatéaversão4.xorg.hibernate.dialect.MySQLDialect
• MySQL para o motor de armazenamento MyISAM
org.hibernate.dialect.MySQLISAMDialect
• Oracle10gorg.hibernate.dialect.Oracle10gDialect
• Oracle9iorg.hibernate.dialect.Oracle9iDialect
• Oracle8iorg.hibernate.dialect.Oracle8iDialect
• Pointbaseorg.hibernate.dialect.PointbaseDialect
398

## Página 405

CasadoCódigo Capítulo13. Apêndice1 ListadedialetosdoHibernate
• PostgresPlusorg.hibernate.dialect.PostgresPlusDialect
• Postgres8.1org.hibernate.dialect.PostgreSQL81Dialect
• Postgres8.2+org.hibernate.dialect.PostgreSQL82Dialect
• Unisys 2200 Relational Database (RDMS)
org.hibernate.dialect.RDMSOS2200Dialect
• SAPDBorg.hibernate.dialect.SAPDBDialect
• MicrosoftSQL2005org.hibernate.dialect.SQLServer2005Dialect
• MicrosoftSQLServer2008org.hibernate.dialect.SQLServer2008Diale
• MicrosoftSQLServer2000org.hibernate.dialect.SQLServerDialect
• Sybase 11.9.2 (evita a sintaxe ANSI JOIN)
org.hibernate.dialect.Sybase11Dialect
• SybaseAnywhereorg.hibernate.dialect.SybaseAnywhereDialect
• Sybase Adaptive Server Enterprise (ASE) 15.7+
org.hibernate.dialect.SybaseASE157Dialect
• Sybase Adaptive Server Enterprise (ASE) 15+
org.hibernate.dialect.SybaseASE15Dialect
399

## Página 407

CasadoCódigo ReferênciasBibliográficas
Referências Bibliográficas
[1] OSGiAlliance.Websiteoficialdaosgialliance. http://www.osgi.org/.
[2] PeterPin-ShanChen. Theentityrelationshipmodel-towardaunified
viewofdata.1976.
[3] EquipededesenvolvimentodoGrails. createcriteria. http://grails.org/
doc/2.4.4/ref/Domain%20Classes/createCriteria.html,2014.
[4] EquipededesenvolvimentodoGrails. Dynamicfinders. http://grails.
org/doc/2.4.4/guide/GORM.html#finders,2014.
[5] EquipededesenvolvimentodoGrails.Understandingcascadingupdates
and deletes. http://grails.org/doc/2.4.4/guide/GORM.html#cascades,
2014.
[6] EquipededesenvolvimentodoGroovy.Groovybuilders. http://groovy.
codehaus.org/Builders.
[7] Equipe de desenvolvimento do Hibernate. Identifier ge-
nerator - documentação do hibernate. http://docs.jboss.
org/hibernate/core/3.6/reference/en-US/html/mapping.html#
mapping-declaration-id-generator.
[8] EquipededesenvolvimentodoHibernate. Hql: Thehibernatequery
language.2014.
[9] Equipe de desenvolvimento do Hibernate. Javadoc da classe
scrollableresults.http://docs.jboss.org/hibernate/core/3.6/javadocs/org/
hibernate/ScrollableResults.html,2014.
401

## Página 408

ReferênciasBibliográficas CasadoCódigo
[10] EquipededesenvovlimentodoGrails. Upgradedaversão2.3para2.4.
http://grails.github.io/grails-doc/2.4.0/guide/upgradingFrom23.html.
[11] ProjetoApacheFoundation.Apachetiles. http://tiles.apache.org.
[12] DavidHeinemeierHansson.Tddisdead.longlivetesting. http://david.
heinemeierhansson.com/2014/tdd-is-dead-long-live-testing.html.
[13] DavidHeinemeierHansson. Howtobuildablogenginein15minu-
teswithrubyonrails. http://www.youtube.com/watch?v=Gzj723LkRJY,
2005.
[14] MartinHeidegger.Ser e T empo.1927.
[15] Graeme Rocher Henrique Lobo Weissmann. Graeme rocher sobre
aobsolênciadastagsajax. https://groups.google.com/forum/#!topic/
grails-dev-discuss/4yesijtFSB4.
[16] Hibernate.Transitivepersistence.http://docs.jboss.org/hibernate/core/
3.6/reference/en-US/html/objectstate.html#objectstate-transitive.
[17] DavidHunt,Andrew;Thomas. The Pragmatic Programmer.1999.
[18] EquipeJBoss.Documentaçãodojbossmodules. https://docs.jboss.org/
author/display/MODULES/Home.
[19] Luke Daley e Peter N. Steinmetz Marc Palmer. Documentação
de referência do resources plugin.http://grails-plugins.github.io/
grails-resources/.
[20] DanNorth. Behaviourdrivendevelopment. http://behaviour-driven.
org/.
[21] DanNorth.Introducingbdd. http://dannorth.net/introducing-bdd/.
[22] Oracle. Defaultmethods.http://docs.oracle.com/javase/tutorial/java/
IandI/defaultmethods.html.
[23] Oracle. Javadocsimpledateformat. http://docs.oracle.com/javase/7/
docs/api/java/text/SimpleDateFormat.html.
402

## Página 409

CasadoCódigo ReferênciasBibliográficas
[24] Oracle. Preventable phenomena and transaction isolation le-
vels. http://docs.oracle.com/cd/B12037_01/server.101/b10743/consist.
htm#sthref1919.
[25] OWASP. Cross-sitescripting(xss).https://www.owasp.org/index.php/
Cross-site_Scripting_%28XSS%29.
[26] R.SalzP.Leach,MMealing.Rfc4122-uuid. http://tools.ietf.org/html/
rfc4122.
[27] GraemeRocher.Upgradedaversão2.xpara3.0dograils. http://grails.
github.io/grails-doc/latest/guide/upgrading.html.
[28] RyanVanderwerfSergeyNebolsin,GraemeRocher. Quartspluginfor
grails.https://grails.org/plugin/quartz.
[29] StackOverflow. Using hibernate’s scrollableresults to slowly read
90 million records. http://stackoverflow.com/questions/2826319/
using-hibernates-scrollableresults-to-slowly-read-90-million-records,
2013.
[30] AlanM.Turing. Oncomputablenumbers,withanapplicationtothe
entscheidungsproblem.1936.
[31] HenriqueLoboWeissmann. Vireojogocomspringframework. http:
//www.casadocodigo.com.br/products/spring.
[32] Wikipedia.Binarysearch.http://en.wikipedia.org/wiki/Binary_search_
algorithm.
[33] Wikipedia.Listadecabeçalhoshttp. http://en.wikipedia.org/wiki/List_
of_HTTP_header_fields.
403