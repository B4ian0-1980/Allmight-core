---json
{
  "id": "java_8_pr_tico_lambdas__streams_e_os_novos_recursos_da_linguagem",
  "title": "Java 8 Prático Lambdas, Streams e os novos recursos da linguagem",
  "categoria": "03-linguagens",
  "subcategoria": "java",
  "resumo": "**Arquivo Original:** `Java 8 Prático Lambdas, Streams e os novos recursos da linguagem.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "java",
    "lambdas",
    "linguagem",
    "linguagens",
    "novos",
    "recursos",
    "streams",
    "tico"
  ],
  "perguntas_tipo": [
    "Como utilizar Java 8 Prático Lambdas, Streams e os novos recursos da linguagem?",
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

# Java 8 Prático Lambdas, Streams e os novos recursos da linguagem

> **Arquivo Original:** `Java 8 Prático Lambdas, Streams e os novos recursos da linguagem.pdf`
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
“ ÀfamíliaAlexandreVulcano”
–PauloSilveira
“ Àminhaamadaesposa”
–RodrigoTurini
i

## Página 7

CasadoCódigo
Agradecimentos
FoiumdesafioescreverumlivroduranteseismesesemqueoJDK8finalaindanão
existia.
Ficaumagradecimentoatodosquenosajudaramcomdúvidas,sugestões epar-
ticipaçõesnalista.AlbertoSouza,FranciscoSokol,GuilhermeSilveira,MichaelNas-
cimentoeOsvaldoDuoderleinsãoalgunsdeles.AgradecimentoespecialaAlexan-
dreAquiles,pelascorreções esugestões importantesduranteadetalhadarevisão.
U mmuitoobrigadoatodososdesenvolvedoresdoJDK8,queemmuitasvezes
responderamnossasdúvidasprontamente.DestaqueparaoBrianGoetz,líderdo
projetoLambdaesempremuitosolícito.
U mabraçoatodosdaCaelum,doAluraedaCasadoCódigo.Sãoequipesque
nosincentivamtodososdiasainvestigarnovastecnologias,paradigmasebibliote-
cas.
iii

## Página 9

CasadoCódigo Sumário
Sumário
1 Java8 1
1.1 U mbaldedeáguamorna? . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2 Acesseocódigodesselivroediscutacomagente! . . . . . . . . . . . 3
2 Olá,Lambda! 5
2.1 Loopsdamaneiraantigaedamaneiranova . . . . . . . . . . . . . . . 5
2.2 QueentreoLambda! . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
3 Interfacesfuncionais 11
3.1 Outroexemplo:listeners . . . . . . . . . . . . . . . . . . . . . . . . . . 13
3.2 Suaprópriainterfacefuncional . . . . . . . . . . . . . . . . . . . . . . 14
3.3 Aanotação@FunctionalInterface . . . . . . . . . . . . . . . . . . . . . 15
3.4 Indomaisafundo:primeirosdetalhes . . . . . . . . . . . . . . . . . . 16
4 DefaultMethods 19
4.1 OmétodoforEachnainterfaceIterable. . . . . . . . . . . . . . . . . . 19
4.2 AinterfaceConsumernãotemsóummétodo!. . . . . . . . . . . . . 20
4.3 MaisumnovométodoemCollection:removeIf. . . . . . . . . . . . . 22
4.4 Herançamúltipla?. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
5 OrdenandonoJava8 25
5.1 Comparatorscomolambda. . . . . . . . . . . . . . . . . . . . . . . . . 25
5.2 OmétodoList.sort. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
5.3 MétodosestáticosnainterfaceComparator . . . . . . . . . . . . . . . 27
5.4 ConhecendomelhoroComparator.comparing . . . . . . . . . . . . . 28
5.5 Ordenandoporpontoseoautoboxing . . . . . . . . . . . . . . . . . . 29
v

## Página 10

Sumário CasadoCódigo
6 MethodReferences 31
6.1 T o r n a n d otodososusuáriosmoderadores . . . . . . . . . . . . . . . . 31
6.2 Comparandodeumaformaaindamaisenxuta . . . . . . . . . . . . . 32
6.3 Compondocomparators . . . . . . . . . . . . . . . . . . . . . . . . . . 33
6.4 Referenciandométodosdeinstância . . . . . . . . . . . . . . . . . . . 34
6.5 Referenciandométodosquerecebemargumentos . . . . . . . . . . . 35
6.6 Referenciandoconstrutores . . . . . . . . . . . . . . . . . . . . . . . . 36
6.7 Outrostiposdereferências. . . . . . . . . . . . . . . . . . . . . . . . . 38
7 StreamseCollectors 41
7 . 1T o r n a n d omoderadoresos10usuárioscommaispontos. . . . . . . . 41
7 . 2Streams:tornandomoderadoresosusuárioscommaisde100pontos 42
7 . 3ComoobterdevoltaumaLista? . . . . . . . . . . . . . . . . . . . . . . 46
7 . 4Collectors. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
7 . 5A v a nçado:porquenãoháumtoListemStream? . . . . . . . . . . . . 48
7 . 6Listeapenasospontosdetodososusuárioscomomap . . . . . . . . 49
7 . 7IntStreameafamíliadeStreams. . . . . . . . . . . . . . . . . . . . . . 50
7 . 8OOptionalemjava.util . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
8 MaisoperaçõescomStreams 55
8.1 OrdenandoumStream . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
8.2 Muitasoperações noStreamsãolazy!. . . . . . . . . . . . . . . . . . . 56
8.3 Qualéavantagemdosmétodosseremlazy?. . . . . . . . . . . . . . . 57
8.4 Enxergandoaexecuçãodopipelinecompeek . . . . . . . . . . . . . . 58
8.5 Operações deredução . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
8.6 ConhecendomaismétodosdoStream . . . . . . . . . . . . . . . . . . 61
8.7 Streamsprimitivoseinfinitos . . . . . . . . . . . . . . . . . . . . . . . 63
8.8 Praticandooqueaprendemoscomjava.nio.file.Files . . . . . . . . . . 67
8.9 FlatMap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
9 Mapeando,particionando,agrupandoeparalelizando 71
9.1 Coletoresgerandomapas. . . . . . . . . . . . . . . . . . . . . . . . . . 71
9.2 groupingByepartitioningBy . . . . . . . . . . . . . . . . . . . . . . . . 7 4
9.3 Executandoopipelineemparalelo . . . . . . . . . . . . . . . . . . . . 78
9.4 Operações nãodeterminísticaseorderedstreams. . . . . . . . . . . . 79
vi

## Página 11

CasadoCódigo Sumário
10 ChegadeCalendar!NovaAPIdedatas 83
10.1 Ajava.timevemdoJodaTime . . . . . . . . . . . . . . . . . . . . . . . 83
10.2 Trabalhandocomdatasdeformafluente. . . . . . . . . . . . . . . . . 84
10.3 Enumsnolugardeconstantes . . . . . . . . . . . . . . . . . . . . . . . 88
10.4 FormatandocomanovaAPIdedatas . . . . . . . . . . . . . . . . . . 89
10.5 Datasinválidas. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
10.6 DuraçãoePeríodo. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91
10.7 DiferençasparaoJodaTime . . . . . . . . . . . . . . . . . . . . . . . . 94
11 UmmodelodepagamentoscomJava8 97
11.1 U m alojadedigitalgoodies. . . . . . . . . . . . . . . . . . . . . . . . . 97
11.2 Ordenandonossospagamentos . . . . . . . . . . . . . . . . . . . . . . 101
11.3 ReduzindoBigDecimalemsomas. . . . . . . . . . . . . . . . . . . . . 101
11.4 Produtosmaisvendidos. . . . . . . . . . . . . . . . . . . . . . . . . . . 103
11.5 Valoresgeradosporproduto . . . . . . . . . . . . . . . . . . . . . . . . 105
11.6 Quaissãoosprodutosdecadacliente? . . . . . . . . . . . . . . . . . .106
11.7 Qualénossoclientemaisespecial? . . . . . . . . . . . . . . . . . . . . 108
11.8 Relatórioscomdatas. . . . . . . . . . . . . . . . . . . . . . . . . . . . .109
11.9 Sistemadeassinaturas. . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
12 Apêndice:maisJava8comreflection,JVM,APIselimitações 113
12.1 Novosdetalhesnalinguagem . . . . . . . . . . . . . . . . . . . . . . . 113
12.2 QualéotipodeumaexpressãoLambda? . . . . . . . . . . . . . . . . 117
12.3 Limitações dainferêncianolambda. . . . . . . . . . . . . . . . . . . . 119
12.4 FimdaPermgen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
12.5 Reflection:parameternames. . . . . . . . . . . . . . . . . . . . . . . . 122
13 Continuandoseusestudos 125
13.1 Comotirarsuasdúvidas . . . . . . . . . . . . . . . . . . . . . . . . . . 125
13.2 BibliotecasquejáusamouvãousarJava8 . . . . . . . . . . . . . . . . 126
Versão: 17.0.21
vii

## Página 13

Capítulo1
J a v a8
Sãopraticamente20anosdeJavadesdeolançamentodesuaprimeiraversão.
Apenasem2004,comachegadadoJava5,houvemudançassignificativasna
linguagem.Emespecialgenerics,enumseanotações.
ComachegadadoJava8,em2014,issoacontecemaisumavez.Novaspossibili-
dadessurgemcomaentradadolambdaedosmethodreferences,alémdepequenas
mudançasnalinguagem.AAPIdeCollections,naqualasinterfacesprincipaissão
asmesmasdesde1998,recebeumsignificativoupgradecomaentradadosStreams
edosmétodosdefault.
Tudoissoseráextensivamentepraticadoduranteolivro.Éhoradeprogramar.
V o c êdevebaixareinstalaroJava8:
http://www.oracle.com/technetwork/java/javase/downloads/
Epodeacessarseujavadocaqui:
http://download.java.net/jdk8/docs/api/index.html
OEclipsepossuisuporteparaoJava8apartirdaversãoLuna(4.4).OKepler
(4.3)precisadoseguinteupdate:

## Página 14

1.1.Umbaldedeáguamorna? CasadoCódigo
https://wiki.eclipse.org/JDT/Eclipse_Java_8_Support_For_Kepler
OEclipseaindapossuialgunspequenosbugspararealizarinferênciasmaiscom-
plicadas.NetbeanseIntelliJtemsuasversões atualizadasparaJava8.
Parafixarasintaxe,vocêpodeoptarporrealizarostesteseexemplosdolivro
comumsimpleseditordetexto.
1.1 Um baldede á g u a morna?
SevocêestáesperandoalgotãopoderosoquantoemScala,ClojureeC#,certamente
sairádecepcionado.OlegadoeaidadedoJava,alémdaausênciadevaluetypese
reificaçãonosgenerics,impedemousodealgumasestratégias.Otimededesenvol-
vedoresdalinguagemtemtambémgrandepreocupaçãoemdeixarasintaxesempre
simples,evitandoformasobscurasquetrariampequenosganhos.Nanossaopinião,
fazbastantesentido.
Aomesmotempoéimpressionanteoquefoipossívelatingircomolançamento
dessanovaversão.V o c êvaisesurpreendercomalgunscódigoseabordagensutiliza-
das.Ofocoénãoquebraracompatibilidadedocódigoantigoeseromenosintrusivo
possívelnasantigasAPIs.Os Streams,queserãovistosquasequeaexaustão,cer-
tamentetêmumpapelcrucialnessaeleganteevolução.
OqueficoudeforadoJava8?
ParaquebrarmelhoraespecificaçãodoJava8emtarefasmenores,foramcriadas
asJEPs:JDKEnhancementProposals.ÉumaideiaquenasceudosPEPs,proposta
similardacomunidadePython.AJEP0éumalistacomtodasessaspropostas:
http://openjdk.java.net/jeps/0
Comovocêpodever,sãomuitasasnovidadesnoJDK8.Infelizmentenemtodas
tiveramtemposuficienteparaamadurecer.EntreasJEPspropostas,osV a l u eObjects
ficaramdefora:
http://openjdk.java.net/jeps/169
Assimcomoousodeliteraisparatrabalharcomcoleções:
http://openjdk.java.net/jeps/186
Entreoutrasideiasqueficaramdefora,temosdiversasmelhoriasaosGarbage
Collectorsjáembutidos,assimcomoapossívelreificaçãodosgenerics.
Dequalquermaneira,amaioriaabsolutadasJEPssobreviveuatéolançamento
daversãofinal.Veremosasprincipaismudançasdalinguagem,assimcomoasnovas
APIs,nodecorrerdolivro.
2

## Página 15

CasadoCódigo Capítulo1.Java8
1.2 Acesse o código desse livro e discuta co m a
gente!
Ocódigo-fonteparacadacapítulopodeserencontradoaqui:
https://github.com/peas/java8
Éclaroqueindicamosquevocêmesmoescrevatodoocódigoapresentadono
livro,parapraticaraAPIeasintaxe,alémderealizartestesdiferentesdossugeridos.
Háumalistadediscussãoporondevocêpodeconversarcomagente,mandar
sugestões, críticasemelhorias:
https://groups.google.com/forum/#!forum/java8-casadocodigo
Sepreferir,vocêpodetirardúvidasnofórumdoGUJ:
http://www.guj.com.br/
3

## Página 17

Capítulo2
Olá,Lambda!
Emvezdecomeçarcomumaboadosedeteoria,éimportantequevocêsintana
práticacomooJava8vaimudaraformacomquevocêprograma.
2.1 Lo o p sd amaneira antiga e d amaneira nov a
Éimportantequevocêacompanheolivrorecriandoocódigodaqui. Sóassima
sintaxetornar-se-ánaturalemaispróximadevocê.
Abraseueditorpreferido.V a m o scriarumaentidadeparapoderrodarexemplos
baseadosnela. Teremosaclasse Usuario,comtrêsatributosbásicos: pontos,
nomeeum boolean moderador,indicandoseaqueleusuárioéummoderador
donossosistema.Simplesassim:
class Usuario {
private String nome;
private int pontos;
private boolean moderador;

## Página 18

2.1.Loopsdamaneiraantigaedamaneiranova CasadoCódigo
public Usuario(String nome, int pontos) {
this.pontos = pontos;
this.nome = nome;
this.moderador = false;
}
public String getNome() {
return nome;
}
public int getPontos() {
return pontos;
}
public void tornaModerador() {
this.moderador = true;
}
public boolean isModerador() {
return moderador;
}
}
Não declaramosaclassecomopúblicapropositalmente. Casovocêestejaem
umeditordetextosimples,poderácriarseustestesemumaclassepúblicadentrodo
mesmoarquivo.
V a m o smanipularalgunsusuários,comnomesepontosdiferentes,eimprimir
cadaumdeles.Faremosissodamaneiraclássicaquejáconhecemos,semnenhuma
novidadedanovaversãodalinguagem.
public class Capitulo2 {
public static void main(String ... args) {
Usuario user1 = new Usuario("Paulo Silveira", 150);
Usuario user2 = new Usuario("Rodrigo Turini", 120);
Usuario user3 = new Usuario("Guilherme Silveira", 190);
List<Usuario> usuarios = Arrays.asList(user1, user2, user3);
for(Usuario u : usuarios) {
System.out.println(u.getNome());
6

## Página 19

CasadoCódigo Capítulo2. Olá,Lambda!
}
}
}
Omitimosdoisimports:do java.util.Listedo java.util.Arrays.Du-
ranteolivro,elesnãovãoaparecer,masnotaremossemprequeapareceremnovos
pacotesdoJava8.
Arrays.asListéumamaneirasimplesdecriaruma Listimutável.Masvocê
poderiasimtercriadoumanova ArrayListeadicionadocadaumdosusuários.
O forquefazemosétrivial.DesdeoJava5,podemosnavegarassimemqual-
querarrayoucoleção (naverdade,emqualquertipodeobjetoqueimplementea
interface java.lang.Iterable).
Umnovométodoemtodasascoleções: forEach
ApartirdoJava8temosacessoaumnovométodonessanossalista:o forEach.
Deondeelevem?Veremosmaisadiante.Iniciaremosporutilizá-lo.Podemosfazer
algocomo:
usuarios.forEach(...);
Paracadausuário,oqueeledevefazer?Imprimironome.Masqualéoargu-
mentoqueessemétodoforEachrecebe?
Elerecebeumobjetodotipo java.util.function.Consumer,quetemum
únicométodo,o accept.ElaéumanovainterfacedoJava8,assimcomotodoo
pacotedo java.util.function,queconheceremosnodecorrerdolivro.
V a m o scriaresseconsumidor,antesdeusaronovo forEach:
class Mostrador implements Consumer<Usuario> {
public void accept(Usuario u) {
System.out.println(u.getNome());
}
}
CriamosumaclassequeimplementaessanovainterfacedoJava8. Elaébem
trivial,possuindooúnicométodoacceptresponsávelporpegarumobjetodotipo
Usuarioeconsumi-lo.‘Consumir’aquiérealizaralgumatarefaquefaçasentido
pravocê.Nonossocaso,émostraronomedousuárionasaídapadrão. Depois
disso,podemosinstanciaressaclasseepassarareferênciaparaoesperadométodo
forEach:
7

## Página 20

2.2.QueentreoLambda! CasadoCódigo
Mostrador mostrador = new Mostrador();
usuarios.forEach(mostrador);
Sabemosqueéumapráticacomumutilizarclassesanônimasparaessastarefas
maissimples.Emvezdecriarumaclasse Mostradorsópraisso,podemosfazer
tudodeumatacadasó:
Consumer<Usuario> mostrador = new Consumer<Usuario>() {
public void accept(Usuario u) {
System.out.println(u.getNome());
}
};
usuarios.forEach(mostrador);
Issovaiacabargerandoum .classcomnomeestranho,comoporexem-
plo Capitulo2$1.class.Comonãopodemosnosreferenciaraumnomedessa
classe,chamamo-ladeclasseanônima,comojádeveserdeseuconhecimento.
Ocódigoaindaestágrande.Parecequeo fordemaneiraantigaeramaissu-
cinto.Podemosreduzirumpoucomaisessecódigo,evitandoacriaçãodavariável
local mostrador:
usuarios.forEach(new Consumer<Usuario>() {
public void accept(Usuario u) {
System.out.println(u.getNome());
}
});
Pronto!U mpoucomaisenxuto,masaindaassimbastanteverboso.
2.2 Que entre oLambda!
Simplificandobastante,umlambdanoJavaéumamaneiramaissimplesdeimple-
mentarumainterfacequesótemumúnicométodo.Nonossocaso,ainterface
Consumeréumaboacandidata.
Istoé,emvezdeescrever:
Consumer<Usuario> mostrador = new Consumer<Usuario>() {
public void accept(Usuario u) {
System.out.println(u.getNome());
}
};
8

## Página 21

CasadoCódigo Capítulo2. Olá,Lambda!
Podemosfazerdeumamaneiramaisdireta.Repareamágica:
Consumer<Usuario> mostrador =
(Usuario u) -> {System.out.println(u.getNome());};
Otrecho (Usuario u) -> {System.out.println(u.getNome());};
éumlambdadoJava8. Ocompiladorpercebequevocêoestáatribuindoaum
Consumer<Usuario>evaitentarjogaressecódigonoúnicométodoqueessain-
terfacedefine.Reparequenãocitamosnemaexistênciadométodoaccept!Issoé
inferidoduranteoprocessodecompilação.
Podemosiralém.Ocompiladorconseguetambéminferirotipo,semanecessi-
dadedeutilizar Usuario,nemparênteses:
Consumer<Usuario> mostrador =
u -> {System.out.println(u.getNome());};
Nãoestásatisfeito?Casooblocodentrode { }contenhaapenasumainstrução,
podemosomiti-loeremovertambémopontoevírgula:
Consumer<Usuario> mostrador =
u -> System.out.println(u.getNome());
Agoraficaatépossíveldeescreveremumaúnicalinha:
Consumer<Usuario> mostrador = u -> System.out.println(u.getNome());
Então u -> System.out.println(u.getNome()) infere pro mesmo
lambdaque (Usuario u) -> {System.out.println(u.getNome());},se
forematribuídosaum Consumer<Usuario>.Podemospassaressetrechodecó-
digodiretamentepara usuarios.forEachemvezdedeclararavariáveltempo-
ráriamostrador:
usuarios.forEach(u -> System.out.println(u.getNome()));
Difícil?Certamentenão. Porémpodelevaralgumassemanasatévocêsehabi-
tuarcomasintaxe,alémdasdiferentespossibilidadesdeutilizá-la.V a m o sconhecer
algumasnuancesetrabalharbastantecomaAPI,alémdesabercomoissofoiim-
plementado,queéumpoucodiferentedasclassesanônimas. Sevocêobservaros
.classgerados,poderáperceberqueocompiladornãocriouosdiversosarquivos
Capitulo2$N.class,comocostumafazerpracadaclasseanônima.
V a m o samaisumexemploessencial.V o c êpode,emvezdeimprimironomede
todososusuários,tornartodoselesmoderadores!
9

## Página 22

2.2.QueentreoLambda! CasadoCódigo
usuarios.forEach(u -> u.tornaModerador());
V a l elembrarqueessavariávelunãopodetersidodeclaradanomesmoescopo
dainvocaçãodo forEach,poisolambdapodecapturarasvariáveisdefora,como
veremosmaisadiante.
Nopróximocapítulovamostrabalharmaiscomlambda,paraexercitarasin-
taxe,alémdeconheceroutroscenáriosbásicosdeseuusojuntocomoconceitode
interfacefuncional.
10

## Página 23

Capítulo3
Interfacesfuncionais
Reparequeainterface Consumer<Usuario>,porexemplo,temapenasumúnico
métodoabstrato,o accept. Éporissoque,quandofaçoo forEachaseguir,o
compiladorsabeexatamentequalmétododeveráserimplementadocomocorpodo
meulambda:
usuarios.forEach(u -> System.out.println(u.getNome()));
Maseseainterface Consumer<Usuario>tivessedoismétodos?Ofatodeessa
interfaceterapenasummétodonão foiumacoincidência,massimumrequisito
paraqueocompiladorconsigatraduzi-laparaumaexpressão lambda. Podemos
dizerentãoquetodainterfacedoJavaquepossuiapenasummétodoabstratopode
serinstanciadacomoumcódigolambda!
Issovaleatémesmoparaasinterfacesantigas,pré-Java8,comoporexemploo
Runnable:
public interface Runnable {
public abstract void run();
}

## Página 24

CasadoCódigo
Apenasumlembrete:porpadrão, todososmétodosdeumainterfacenoJava
são públicoseabstratos.Veremos,maisàfrente,queháumnovotipodemétodo
nasinterfaces.
Normalmente,escrevemososeguintetrechoparainstanciaruma Threadeum
Runnablequecontade0a1000:
Runnable r = new Runnable(){
public void run(){
for (int i = 0; i <= 1000; i++) {
System.out.println(i);
}
}
};
new Thread(r).start();
Ainterface Runnabletemapenasumúnicométodoabstrato.U m ainterface
queseenquadrenesserequisitoéagoraconhecidacomoumainterfacefuncional!
Elasemprepodeserinstanciadaatravésdeumaexpressãolambda:
Runnable r = () -> {
for (int i = 0; i <= 1000; i++) {
System.out.println(i);
}
};
new Thread(r).start();
Poderíamosiralémefazertudoemumúnicostatement,comtalvezumpouco
menosdelegibilidade:
new Thread(() -> {
for (int i = 0; i <= 1000; i++) {
System.out.println(i);
}
}).start();
Comovocêjásabe,existeumnovopacotenoJava8,o java.util.function,
comumasériedeinterfacesfuncionaisquepodemedevemserreaproveitadas.Co-
nheceremosdiversasdelasaodecorrerdonossoestudo.
12

## Página 25

CasadoCódigo Capítulo3.Interfacesfuncionais
3.1 Ou t r oexemplo: listeners
U moutrousobemnaturaldeclasseanônimaéquandoprecisamosadicionaruma
açãonoclickdeumobjetodotipo java.awt.Button.Paraisso,precisamosim-
plementarum ActionListener.V o c êjápodetervistoumcódigoparecidocom
este:
button.addActionListener(new ActionListener() {
public void actionPerformed(ActionEvent e) {
System.out.println("evento do click acionado");
}
});
U s a m o sainterface ActionListenercomonadamaisdoqueumafunçãode
retorno,epelasuaestruturadeumúnicométodoelaseenquadranorequisitode
interfacefuncional:
public interface ActionListener extends EventListener {
/**
* Invoked when an action occurs.
*/
public void actionPerformed(ActionEvent e);
}
Assimcomotodainterfacefuncional,tambémpodemosrepresentá-lacomo
umaexpressãolambda:
button.addActionListener( (event) -> {
System.out.println("evento do click acionado");
});
Comojávimos,essaexpressãopodeficaraindamaissimples,semparêntesesno
únicoargumentoepodemostambémremovero {}e ;:
button.addActionListener(
event -> System.out.println("evento do click acionado"));
Pronto!Agoraestamosdandoamesmaaçãoao button,sóquesubstituindo
as5linhasqueusamoscomumaclasseanônimaporumaúnicalinhadeexpressão
lambda.
13

## Página 26

3.2.Suaprópriainterfacefuncional CasadoCódigo
Assim como a ActionListener que jáexiste e écomumente usada
nas versões pré-Java8, existem diversas outras interfaces do Java que pos-
suem essa mesma estrutura de um únicométodo,como por exemplo as in-
terfaces java.util.Comparator, java.util.concurrent.Callable e
java.io.FileFilter.Alémdo java.lang.Runnable,quejávimos.
Mesmosemteremalteradonadaemsuaestruturainterna,todasessasinterfaces
podemserchamadas,apartirdessanovaversãodalinguagem,deinterfacesfunci-
onais!
3.2 Su aprópria interface funcional
V o c ênão precisafazernadadeespecialparaqueumainterfacesejaconsiderada
funcional.Ocompiladorjáidentificaessetipodeinterfacepelasuaestrutura.
Imaginequetemosumainterfacede Validador<T>,comummétodoque
valida(T t)equedevolve boolean:
interface Validador<T> {
boolean valida(T t);
}
Costumamosutilizá-lacriandoumaclasseanônima,destaforma:
Validador<String> validadorCEP = new Validador<String>() {
public boolean valida(String valor) {
return valor.matches("[0-9]{5}-[0-9]{3}");
}
};
EcomopodemosusaressainterfacecomLambdaapartirdoJava8? Oque
precisamosmodificaremsuadeclaração?
Arespostaéfácil:absolutamentenada.Comojáhavíamosfalado,bastandoain-
terfacepossuirumúnicométodoabstrato,elaéconsideradaumainterfacefuncional
epodeserinstanciadaatravésdeumaexpressãolambda!Veja:
Validador<String> validadorCEP =
valor -> {
return valor.matches("[0-9]{5}-[0-9]{3}");
};
14

## Página 27

CasadoCódigo Capítulo3.Interfacesfuncionais
Para testar vocêpode executar em um métodomain simples, o código
validadorCEP.valida("04101-300");
Nossolambdaestáumpoucogrande.Vimosmaisdeumavezque,quandohá
umaúnicainstrução, podemosresumi-la. Eissoacontecemesmoseelaforuma
instrução de return! Podemosremoveropróprio return,assimcomooseu
pontoevírgulaeaschavesdelimitadoras:
Validador<String> validadorCEP =
valor -> valor.matches("[0-9]{5}-[0-9]{3}");
3.3 A anotação @FunctionalInterface
Podemosmarcarumainterfacecomofuncionalexplicitamente,paraqueofatode
elaserumainterfacefuncionalnãosejapelasimplescoincidênciadeterumúnico
método.Parafazerisso,usamosaanotação @FuncionalInterface:
@FunctionalInterface
interface Validador<T> {
boolean valida(T t);
}
Sevocêfizeressaalteraçãoecompilarocódigodonosso Validador<T>,vai
perceberquenadamudou.Masdiferentedocasodenãotermosanotadonossainter-
facecom @FunctionalInterface,tentealterá-ladaseguinteforma,adicionando
umnovométodo:
@FunctionalInterface
interface Validador<T> {
boolean valida(T t);
boolean outroMetodo(T t);
}
Aocompilaressecódigo,recebemososeguinteerro:
java: Unexpected @FunctionalInterface annotation
Validador is not a functional interface
multiple non-overriding abstract methods found in interface Exemplo
Essaanotação serveapenasparaqueninguémtorneaquelainterfaceemnão-
funcionalacidentalmente.Elaéopcionaljustamenteparaqueasinterfacesdasanti-
gasbibliotecaspossamtambémsertratadascomolambdas,independentedaanota-
ção,bastandoaexistênciadeumúnicométodoabstrato.
15

## Página 28

3.4.Indomaisafundo:primeirosdetalhes CasadoCódigo
3.4 Indo mais a fundo: primeiros detalhes
InterfacesfuncionaissãoocoraçãodorecursodeLambda.OLambdaporsisónão
existe,esimexpressões lambda,quandoatribuídas/inferidasaumainterfacefunci-
onal.DuranteodesenvolvimentodoJava8,ogrupoquetocouoLambdachamava
essasinterfacesdeSAMTypes(SingleA b s t r a c tMethod).
Seumainterfacefuncionalnãoestáenvolvida,ocompiladornãoconseguetra-
balharcomela:
Object o = () -> {
System.out.println("O que sou eu? Que lambda?");
};
Isso retorna um error: incompatible types: Object is not a
functional interface.Fazsentido.
Ésemprenecessáriohaveraatribuição (oualgumaformadeinferir)daquele
lambdaparaumainterfacefuncional.Aclasse Objectcertamentenãoéocaso!
Seatribuirmosolambdaparaumtipoquesejaumainterfacefuncionalcom-
patível,issoé,comosargumentoseretornosqueométodonecessita,aísimtemos
sucessonacompilação:
Runnable o = () -> {
System.out.println("O que sou eu? Que lambda?");
};
Masoqueexatamenteéoobjetoretornadoporestaexpressão?V a m o sdescobrir
maisinformações:
Runnable o = () -> {
System.out.println("O que sou eu? Que lambda?");
};
System.out.println(o);
System.out.println(o.getClass());
Asaídanãoémuitodiferentedoquevocêespera,sejáconhecebemasclasses
anônimas:
Capitulo3$$Lambda$1@1fc625e
class Capitulo3$$Lambda$1
16

## Página 29

CasadoCódigo Capítulo3.Interfacesfuncionais
AclassegeradaquerepresentaessenossoLambdaéa Capitulo3$$Lambda$1.
Naverdade,essenomevaidependerdequantoslambdasvocêtemnasuaclasse
Capitulo3.Reparequenãofoigeradoum .classnoseudiretório,essaclasseé
criadadinamicamente!
Atradução deumaexpressãoLambdaparaobytecodeJavanão étrivial. Po-
deriaserfeitodeváriasmaneiras,atémesmodamaneiracomoasclassesanônimas
trabalham,maselasnãofuncionamassim.Depoisdemuitadiscussão,optarampor
utilizar MethodHandlese invokedynamicparaisso. V o c êpodeverdetalhes
avançadossobreaimplementaçãoaqui:
http://cr.openjdk.java.net/\char126briangoetz/lambda/lambda-translation.html
AquiháumcomparativodaimplementaçãodoLambdadoScalacomadoJava
8:
http://www.takipiblog.com/2014/01/16/compiling-lambda-expressions-scala-vs-java-8/
Nocapítulo12.2,conheceremosmaisdetalhessobreainferênciadetiposeoutras
peculiaridadesdolambda.
Capturadevariáveislocais
Assimcomonumaclasseanônimalocal,vocêtambémpodeacessarasvariáveis
finaisdométodoaqualvocêpertence:
public static void main(String[] args) {
final int numero = 5;
new Thread(() -> {
System.out.println(numero);
}).start();
}
U mlambdadoJavaenclausuraasvariáveisqueestavamnaquelecontexto,assim
comasclassesanônimas.
Quermais?V o c êpodeatémesmoacessaravariávellocalquenãoéfinal:
public static void main(String[] args) {
int numero = 5;
new Thread(() -> {
System.out.println(numero);
}).start();
}
17

## Página 30

3.4.Indomaisafundo:primeirosdetalhes CasadoCódigo
Porém,eladeveserefetivamentefinal.Issoé,apesardenãoprecisardeclararas
variáveislocaiscomo final,vocênãopodealterá-lasseestiverutilizando-asdentro
dolambda.Oseguintecódigonãocompila:
public static void main(String[] args) {
int numero = 5;
new Thread(() -> {
System.out.println(numero); // não compila
}).start();
numero = 10; // por causa dessa linha!
}
EissotambémvaleparaasclassesanônimasapartirdoJava8.V o c ênãoprecisa
maisdeclararasvariáveislocaiscomo final,bastanão alterá-lasqueoJavavai
permitiracessá-las.
Claroqueproblemasdeconcorrênciaaindapodemacontecernocasodevocêin-
vocarmétodosquealteremestadodosobjetosenvolvidos.Veremosalgunsdetalhes
dissomaisàfrente.
18

## Página 31

Capítulo4
DefaultM e t h o d s
4.1 O método forEa c hn a interfaceIterable
A t éagoraengolimosométodoforEachinvocadoemnossa List. Deondeele
vem,sesabemosqueatéoJava7issonãoexistia?
U m apossibilidadeseriaaequipedoJavatê-lodeclaradoemumainterface,como
naprópria List.Qualseriaoproblema?T o d omundoquecriouumaclasseque
implementa Listprecisariaimplementá-lo.Otrabalhoseriaenorme,masesse
não éoprincipalponto. AoatualizaroseuJava,bibliotecasquetêmsuaprópria
List,comooHibernate,teriamsuasimplementaçõesquebradas,faltandométodos,
podendogerarosassustadores NoSuchMethodErrors.
Comoadicionarummétodoemumainterfaceegarantirquetodasasimple-
mentações opossuamimplementado? Comumnovorecurso,declarandocódigo
dentrodeummétododeumainterface!
Porexemplo,ométodo forEach queutilizamosestádeclaradodentrode
java.lang.Iterable,queémãede Collection,porsuavezmãede List.
Abrindoseucódigo-fonte,podemosver:

## Página 32

4.2. AinterfaceConsumernãotemsóummétodo! CasadoCódigo
default void forEach(Consumer<? super T> action) {
Objects.requireNonNull(action);
for (T t : this) {
action.accept(t);
}
}
Poisé.Métodocomcódigodentrodeinterfaces!Algoquenuncaesperaríamos
serpossívelnoJava.Essesmétodossãochamadosdedefaultmethods(nadocumen-
tação dobetapodesertambémencontradodefendermethodsouaindaextension
methods).
Como ArrayListimplementa List,queéfilha(indireta)de Iterable,
a ArrayListpossuiessemétodo,querelaqueiraounão. Époressemotivoque
podemosfazer:
usuarios.forEach(u -> System.out.println(u.getNome()));
Essedefaultmethod,o forEach,esperareceberumaimplementaçãodainter-
facefuncional Consumer<T>quejávimosserumadasinterfacespresentesnonovo
pacote java.util.functiondoJava8.Elapossuiumúnicométodoabstrato,o
accept,querecebeotipoparametrizado Teexecutaoquevocêacharinteressante.
4.2 A interfaceConsumer n ã o tem só u m método!
T o m a m o socuidado,noscapítulosanteriores,dedeixarclaroqueumainterfacefun-
cionaléaquelaquepossuiapenasummétodoabstrato!Elapodetersimmaismé-
todos,desdequesejammétodosdefault.
Observequeainterface Consumer<T>,alémdométodoaccept(T t),ainda
possuiodefaultmethod andThen:
@FunctionalInterface
public interface Consumer<T> {
void accept(T t);
default Consumer<T> andThen(Consumer<? super T> after) {
Objects.requireNonNull(after);
return (T t) -> { accept(t); after.accept(t); };
}
}
20

## Página 33

CasadoCódigo Capítulo4. DefaultMethods
Repareque,porserummétododefault,aclassepodeserexplicitamenteanotada
com @FunctionalInterface.
O método andThen pode ser usado para compor instânciasda interface
Consumerparaquepossamserexecutadassequencialmente,porexemplo:
public class Capitulo4 {
public static void main(String ... args) {
Usuario user1 = new Usuario("Paulo Silveira", 150);
Usuario user2 = new Usuario("Rodrigo Turini", 120);
Usuario user3 = new Usuario("Guilherme Silveira", 190);
List<Usuario> usuarios = Arrays.asList(user1, user2, user3);
Consumer<Usuario> mostraMensagem = u ->
System.out.println("antes de imprimir os nomes");
Consumer<Usuario> imprimeNome = u ->
System.out.println(u.getNome());
usuarios.forEach(mostraMensagem.andThen(imprimeNome));
}
}
Rodeocódigo.V o c êvaiverqueambososconsumidoresserãoexecutados:
antes de imprimir os nomes
Paulo Silveira
antes de imprimir os nomes
Rodrigo Turini
antes de imprimir os nomes
Guilherme Silveira
Podemos então ter implementações comuns de Consumer, e utilizá-las
emdiferentesmomentosdonossocódigo, passando-oscomoargumentosede-
pois compondo-os de maneira a reutilizá-los. Por exemplo, se vocêtem um
Consumer<Usuario> auditorqueguardanologqueaqueleusuáriorealizou
algonosistema,vocêpodereutilizá-lo,comousemo andThen.U mbomexemplo
dopatterndecorator.
21

## Página 34

4.3.MaisumnovométodoemCollection:removeIf CasadoCódigo
4.3 Maisu m novo método emCollection: removeIf
Ainterface Collectionganhounovosmétodoscomimplementaçãodefault.V i -
moso forEach. U moutroéo removeIf,querecebeum Predicate. O
Predicateéumainterfacefuncionalquepermitetestarobjetosdeumdetermi-
nadotipo. Dadoum Predicate,o removeIfvairemovertodososelementos
quedevolverem trueparaessepredicado.
Sedesejarmosremovertodososusuárioscommaisde100pontosdanossaco-
leção,podemosfazer:
Predicate<Usuario> predicado = new Predicate<Usuario>() {
public boolean test(Usuario u) {
return u.getPontos() > 160;
}
};
List<Usuario> usuarios = new ArrayList<>();
usuarios.add(user1);
usuarios.add(user2);
usuarios.add(user3);
usuarios.removeIf(predicado);
usuarios.forEach(u -> System.out.println(u));
Háumdetalheaqui:o removeIfinvocao removedeumacoleção,entãoela
nãopodeserimutável,ouum UnsupportedOperationExceptionserálançado.
Esseéocasodalistadevolvidapor Arrays.asList.Porisso,foinecessárioutilizar
umacoleçãomutávelcomo ArrayList.
Podemostambémusaraquiolambda.Nãoprecisamosnemmesmodeclarara
variávelpredicado! Podemospassaro u.getPontos() > 160diretoparao
removeIf:
usuarios.removeIf(u -> u.getPontos() > 160);
Quasesempreévantajosoutilizarumlambdaemvezdecriarumaclasseanô-
nima.U m adasrestrições dolambdaéquenãopodemosdeclararatributos,istoé,
manterestadodentrodela.Essasituaçãonãoaparececomfrequência,masveremos
simalgunscasosemqueousodolambdanão serápossívelouteriadeenvolver
atributosdaclasseexterna.
22

## Página 35

CasadoCódigo Capítulo4. DefaultMethods
Veremosoutrosmétodosqueentraramnascoleções. Porexemplo, Mapga-
nhou computeIfPresent, computeIfAbsent, getOrDefaulteoutrosmé-
todosúteisquecostumavamnosforçaraescreverumcódigobemcomum. Não
poderemosvertodos,masutilizaremosdiversasnovasfuncionalidades,interfacese
métodosnodecorrerdolivro.
4.4 Herança múltipla?
Métodosdefaultsforamadicionadosparapermitirqueinterfacesevoluamsem
quebrarcódigoexistente.Essaéumadasfrasesmaisrepetidasnalistadediscussão
daespecificação.
Elesnão foramcriadosparapermitiralgumavariação deherançamúltiplaou
demixins. V a l elembrarqueháumasériederestrições paraessesmétodos.Em
especial,elesnão podemacessaratributosdeinstância,atéporqueissonão existe
eminterfaces!Emoutraspalavras,nãoháherançamúltiplaoucompartilhamento
deestado.
BrianGoetzeosoutroslíderesdaespecificaçãopossuemargumentosfortesna
seção10destedocumento:
http://cr.openjdk.java.net/\char126briangoetz/lambda/lambda-state-final.html
Écertoqueháumaumentonoacoplamentomas,dadasasrestrições dessere-
cursonoJava8,não háamesmapossibilidadedeusosnocivoscomoemoutras
linguagens.Ésempreumtrade-off.
23

## Página 37

Capítulo5
OrdenandonoJ a v a8
5.1 Comparators co mo lambda
Seumaclasseimplementa Comparable, podemospassarumalistadeinstân-
ciasdessaclasseparao Collections.sort. Essenão éocasodenossaclasse
Usuario.Comoébemsabido,precisamosdeum Comparator<Usuario>.
V a m o scriarumqueordenapelonomedousuário,edepoispedirparaquealista
sejaordenada:
Comparator<Usuario> comparator = new Comparator<Usuario>() {
public int compare(Usuario u1, Usuario u2) {
return u1.getNome().compareTo(u2.getNome());
}
};
Collections.sort(usuarios, comparator);
Adivinhe! Comparatoréumainterfacefuncional,comapenasummétodoabs-
trato.Podemostirarproveitodolambdaereescreverainstanciaçãodaquelaclasse

## Página 38

5.2.OmétodoList.sort CasadoCódigo
anônimademaneiramaissimples:
Comparator<Usuario> comparator =
(u1, u2) -> u1.getNome().compareTo(u2.getNome());
Collections.sort(usuarios, comparator);
Ouainda,colocandotudoemumamesmalinha,semadeclaraçãodavariável
local:
Collections.sort(usuarios,
(u1, u2) -> u1.getNome().compareTo(u2.getNome()));
Muitomelhorqueoantigocódigo,não?
Os cuidados com comparators
A t e nção!Paradeixarocódigomaissucinto,nãonosprecavemosaqui
depossíveisusuárioscomatributo nomeiguala null.Mesmosendo
umainvariantedoseusistema,éimportantesemprechecaressescasos
particularesedefinirseumusuáriocomnomenuloiriaparaocomeço
oufimnessecritériodecomparação.
Há também a boa prática de utili-
zar comparators que já existem, como o
String.CASE_INSENSITIVE_ORDER. Seu código ficaria return
String.CASE_INSENSITIVE_ORDER.compare(u1.getNome(),
u2.getNome()ouaindaalgumdos java.text.Collactors,junto
comasverificações devaloresnulo.
5.2 O método List.sort
Podemosordenarumalistadeusuáriosdeformaaindamaissucinta:
usuarios.sort((u1, u2) -> u1.getNome().compareTo(u2.getNome()));
Issofinalmenteépossívelpoisexisteumnovométododefault sortdecla-
radonainterface List,quesimplesmentedelegaainvocaçãoparaojáconhecido
Collections.sort:
26

## Página 39

CasadoCódigo Capítulo5.OrdenandonoJava8
default void sort(Comparator<? super E> c) {
Collections.sort(this, c);
}
Esseéumexcelenteexemplodeusodemétodosdefault,poispermitiuaevolução
dainterface Listsemquebrarocódigoexistente.
5.3 Métodos estáticos n a interfaceComparator
Éissomesmo:alémdepodertermétodosdefaultdentrodeumainterface,agora
podemostermétodosestáticos.Ainterface Comparatorpossuialgunsdeles.
Onosso usuarios.sort(...)podeficaraindamaiscurto,comoauxíliodo
Comparator.comparing(...),queéumafábrica(factory)de Comparators.
Repare:
Comparator<Usuario> comparator =
Comparator.comparing(u -> u.getNome());
usuarios.sort(comparator);
Eleretornaum Comparatorqueusaráa Stringdonomedeusuáriocomo
critériodecomparação.
Aindapodemoscolocartudoemumalinha,semadeclaraçãodavariávellocal:
usuarios.sort(Comparator.comparing(u -> u.getNome()));
Com o uso do static import, poderemos fazer apenas
usuarios.sort(comparing(u -> u.getNome())); e ainda veremos
comomelhoraraindamaisnopróximocapítulo!
O uso do comparing só funciona passando um lambda que, dado um
tipo T (nonosso caso um usuário),devolvealgoqueseja Comparable<U>.
No nosso exemplo, devolvemos uma String, o nome do usuário,que é
Comparable<String>. Veremosumpoucomelhorseufuncionamentomaisà
frente.
Indexandopelaordemnatural
Esetivermosumalistadeobjetosqueimplementam Comparable,comopor
exemplo String?Antesfaríamos:
27

## Página 40

5.4.ConhecendomelhoroComparator.comparing CasadoCódigo
List<String> palavras =
Arrays.asList("Casa do Código", "Alura", "Caelum");
Collections.sort(palavras);
T e n t a rfazer,noJava8, palavras.sort()nãocompila.Nãoháessemétodo
sortem Listquenãorecebeparâmetro.Nemteriacomohaver,poisocompilador
nãoteriacomosaberseoobjetoinvocadoéuma Listde Comparableoudesuas
filhas.
Comoresolver?Criarumlambdade Comparatorquesimplesmentedelegao
trabalhoparao compareTo?Nãoénecessário,poisissojáexiste:
List<String> palavras =
Arrays.asList("Casa do Código", "Alura", "Caelum");
palavras.sort(Comparator.naturalOrder());
Comparator.naturalOrder()retornaum Comparatorquedelegaparao
próprioobjeto.Hátambémo Comparator.reverseOrder().
5.4 Conhecendo melhor oComparator .comparing
A p e s a rdenãoseronossofoco,éinteressantevercomoummétododesseséimple-
mentado.Nãosepreocupesevocênãodominatodososartifíciosdogenericseseus
lowereupperbounds.V a m o saométodo:
public static <T, U extends Comparable<? super U>> Comparator<T>
comparing(Function<? super T, ? extends U> keyExtractor) {
Objects.requireNonNull(keyExtractor);
return (Comparator<T> & Serializable)
(c1, c2) -> keyExtractor.apply(c1).
compareTo(keyExtractor.apply(c2));
}
Dadoumtipo T,o comparingrecebeumlambdaquedevolveumtipo U.Isso
édefinidopelanovainterfacedoJava8,a Function:
Depoisdisso,eleusaasintaxedolambdaparacriarum Comparator,quejá
utilizamosnocomeçodestecapítulo.Achamadado applyfazcomqueonosso
u.getNome()sejainvocado. Repareque applyéoúnicométodoabstratoda
28

## Página 41

CasadoCódigo Capítulo5.OrdenandonoJava8
interface Functionequeo comparinggerouum Comparatorquetambém
nãoprevineocasodeachavedecomparaçãosernula.
V o c êpoderiausaro comparingpassoapasso,paraissoficarmaisclaro:
Function<Usuario, String> extraiNome = u -> u.getNome();
Comparator<Usuario> comparator =
Comparator.comparing(extraiNome);
usuarios.sort(comparator);
5.5 Ordenando p o rpontos e o autoboxing
Ébemsimplesrealizarmosaordenaçãodosnossosusuáriospelaquantidadedepon-
tosquecadaumtem,emvezdonome.Bastaalterarmosolambdapassadocomo
argumento:
usuarios.sort(Comparator.comparing(u -> u.getPontos()));
Paraenxergarmelhoroqueacontece,podemosquebraressecódigoemmais
linhasevariáveislocais,comojávimos:
Function<Usuario, Integer> extraiPontos = u -> u.getPontos();
Comparator<Usuario> comparator =
Comparator.comparing(extraiPontos);
usuarios.sort(comparator);
Autoboxingnoslambdas
Háumproblemaaqui.O extraiPontosgeradoteráummétodoapplyque
recebeum Usuarioedevolveum Integer,emvezdeum int. Issogerará
umautoboxingtodavezqueessemétodoforinvocado.Eelepoderáserinvocado
muitíssimasvezespelo sort,atravésdo comparedo Comparatordevolvidopelo
Comparator.comparing.
EssetipodeproblemavaiaparecerdiversasvezesnasnovasAPIsdoJava8.Para
evitaresseautoboxing(eàsvezesounboxing)desnecessário,háinterfacesequiva-
lentesquetrabalhamdiretamentecom long, doublee int.
Em vez de utilizar a interface Function, devemos nesse caso utilizar o
ToIntFunction e, consequentemente,ométodo comparingInt, querecebe
ToIntFunctionemvezde Function:
29

## Página 42

5.5.Ordenandoporpontoseoautoboxing CasadoCódigo
ToIntFunction<Usuario> extraiPontos = u -> u.getPontos();
Comparator<Usuario> comparator =
Comparator.comparingInt(extraiPontos);
usuarios.sort(comparator);
Claroquevocêpode(edeve)usaraversãomaisenxuta,passandodiretamenteo
lambdaparaafábricadecomparators,eatémesmoinvocaro sortnamesmalinha:
usuarios.sort(Comparator.comparingInt(u -> u.getPontos()));
30

## Página 43

Capítulo6
M e t h o dReferences
Utilizamosasexpressões lambdaparasimplificarousodaquelasfunções decall-
back,interfacescomumenteinstanciadascomoclassesanônimas,comovimoscom
o ActionListenerpradarumaaçãoao button.
Comousodasexpressões lambda,escrevemosumcódigomuitomaisconciso,
entãoevitamosoqueéconhecidonaslistasdediscussões doJava8comoproblema
vertical,aquelasváriaslinhasdecódigoparaexecutarumaaçãosimples.
6.1 Tornando todos os usuários moderadores
Notequemuitasvezesvamosescreverumaexpressão lambdaqueapenasdelega
ainvocação paraummétodoexistente. Porexemplo,comofaríamosparatornar
moderadorestodososelementosdeumalistadeusuários?Poderíamosfazerum
forEachsimpleschamandoométodotornaModeradordecadaelementoite-
rado:
usuarios.forEach(u -> u.tornaModerador());

## Página 44

6.2. Comparandodeumaformaaindamaisenxuta CasadoCódigo
Masépossívelexecutaressamesmalógicadeumaformamuitomaissimples,
apenasinformandoaonosso forEachqualmétododeveráserchamado.Podemos
fazerissousandoumnovorecursodalinguagem,omethodreference.
usuarios.forEach(Usuario::tornaModerador);
Reparequeasintaxeébemsimples:eutenhoinicialmenteotipo(nessecasoa
classe Usuario),seguidododelimitador ::eonomedométodo,semparênteses.
JávimosqueométodoforEachesperareceberum Consumer<Usuario>
comoparâmetro,masporqueeupossopassarumareferênciademétodonolugar
dessainterfacefuncional?V o c êjádeveimaginararesposta:damesmaformacomo
umaexpressãolambda,omethodreferenceétraduzidoparaumainterfacefuncional!
Portanto,oseguintecódigocompila:
Consumer<Usuario> tornaModerador = Usuario::tornaModerador;
usuarios.forEach(tornaModerador);
Esse poderoso recurso étratado pelo compilador praticamente da mesma
formaqueumaexpressão lambda! Emoutraspalavras, Consumer<Usuario>
tornaModerador = Usuario::tornaModerador gera o mesmo
consumidor que Consumer<Usuario> tornaModerador = u ->
u.tornaModerador(). V a l efrisar que aqui não háreflection sendo utili-
zada,tudoéresolvidoemtempodecompilação, semcustosdeoverheadparaa
performance.
6.2 Comparando de u m a forma ainda mais enxuta
Podemosusarmethodreferenceparadeixaraimplementaçãodeumacomparação
aindamaissimpleseenxuta.
Vimosquepodemosfacilmenteordenarnossalistadeusuáriosusandoomé-
todo comparingdaclasse Comparator,passandoumaexpressãolambdacomo
parâmetro:
usuarios.sort(Comparator.comparing(u -> u.getNome()));
V a m o svercomoessecódigoficariausandoumareferênciaaométodogetNome,
nolugardaexpressão u -> u.getNome():
usuarios.sort(Comparator.comparing(Usuario::getNome));
32

## Página 45

CasadoCódigo Capítulo6. MethodReferences
Tiramososparêntesesdométodo,eooperadordesetadolambda.Agoranossa
expressãopareceestaraindamaissimpleseumpoucomaislegível,nãoacha?
Pensandonafluênciadonossocódigo,poderíamostambémfazerumimport
estáticodométodocomparing,eextrairnossaexpressãoparaumavariávelcom
nomebemsignificativo,algocomo:
Function<Usuario, String> byName = Usuario::getNome;
usuarios.sort(comparing(byName));
6.3 Compondo comparators
Assimcomoordenamospelonome,vimosquepodemosordenarosusuáriospelos
pontos:
usuarios.sort(Comparator.comparingInt(u -> u.getPontos()));
Utilizamoso comparingIntemvezdo comparingparaevitaroboxingdes-
necessário.
U s a n d oanovasintaxe,podemosfazer:
usuarios.sort(Comparator.comparingInt(Usuario::getPontos));
Esequisermosumcritériodecomparaçãomaiselaborado?Porexemplo:orde-
narpelospontose,nocasodeempate,ordenarpelonome.
Issoépossívelgraçasaalgunsmétodosdefaultexistentesem Comparator,
comoo thenComparing. V a m o scriarum Comparatorquefuncionadessa
forma:
Comparator<Usuario> c = Comparator.comparingInt(Usuario::getPontos)
.thenComparing(Usuario::getNome);
Existemtambémvariações dessemétodoparaevitaroboxingdeprimitivos,
como thenComparingInt.
Podemospassaressecomparatordiretoparao sort:
usuarios.sort(Comparator.comparingInt(Usuario::getPontos)
.thenComparing(Usuario::getNome));
Háoutrométodoquevocêpodeaproveitarparacomporcomparators,porém
passandoocompostocomoargumento:o nullsLast.
33

## Página 46

6.4. Referenciandométodosdeinstância CasadoCódigo
usuarios.sort(Comparator.nullsLast(
Comparator.comparing(Usuario::getNome)));
Comisso,todososusuáriosnulosdanossalistaestarãoposicionadosnofim,e
orestanteordenadopelonome!HátambémométodoestáticonullsFirst.
comparator.reversed()
Esedesejarordenarporpontos,porémnaordemdecrescente? Utilizamoso
métododefault reversed()no Comparator:
usuarios.sort(Comparator.comparing(Usuario::getPontos).reversed());
A p e s a rdolivronãotercomoobjetivocobrirextensamenteasnovasAPIs,éim-
portantequevocêestejainclinadoapesquisarbastanteeexperimentarumpouco
dosnovosmétodos.Dessaforma,vocênãoacabaescrevendooquejáexisteouin-
vocandométodosestáticosemoutrasclasses!
6.4 Referenciando métodos de instância
Dadaumareferênciaaumobjeto,podemoscriarummethodreferencequeinvoque
umdeseusmétodos:
Usuario rodrigo = new Usuario("Rodrigo Turini", 50);
Runnable bloco = rodrigo::tornaModerador;
bloco.run();
Ainvocação bloco.run()vaifazercomque rodrigo.tornaModerador()
sejainvocado.Paraficarmaisnítido,osdoisblocosaseguirsãoequivalentes:
Runnable bloco1 = rodrigo::tornaModerador;
Runnable bloco2 = () -> rodrigo.tornaModerador();
Repare que isso é bastante diferente de quando fazemos
Usuario::tornaModerador, pois estamos referenciando o métododo meu
usuárioexistente,enãodequalquerobjetodotipo Usuario.
Comoenxergarmelhoradiferença?Olambda rodrigo::tornaModerador
podeserinferidoparaum Runnable,poisessemétodonãorecebeargumentose
deixamosclarodequalusuárioéparaserinvocado.
Nocasodo Usuario::tornaModerador,ocompiladorpodeinferirolambda
para Consumer<Usuario>pois,apesarde tornaModeradornão receberum
argumento,énecessáriosaberdequalusuárioestamosfalando.Veja:
34

## Página 47

CasadoCódigo Capítulo6. MethodReferences
Usuario rodrigo = new Usuario("Rodrigo Turini", 50);
Consumer<Usuario> consumer = Usuario::tornaModerador;
consumer.accept(rodrigo);
A chamada consumer.accept(rodrigo) acaba invocando
rodrigo.tornaModerador(). O efeito éo mesmo, porémaqui precisa-
mospassaroargumento.Novamenteparareforçar,vejaqueosdoisconsumidores
aseguirsãoequivalentes,umusandomethodreferenceeooutrousandolambda:
Consumer<Usuario> consumer1 = Usuario::tornaModerador;
Consumer<Usuario> consumer2 = u -> u.tornaModerador();
Oquenãopodeémisturarexpectativasdenúmeroetiposdiferentesdosargu-
mentoseretorno!Porexemplo,oJavanãovaiaceitarfazer Runnable consumer
= Usuario::tornaModerador,poisessemethodreferencesópodeseratribuído
aumainterfacefuncionalquenecessariamenterecebaumparâmetroemseumétodo
abstrado,queseriautilizadonainvocaçãode tornaModerador.
6.5 Referenciando métodos que recebem argumen -
tos
T a m b é mpodemosreferenciarmétodosquerecebemargumentos,comoporexem-
ploo printlndainstância PrintStream outdaclasse java.lang.System.
Paraimprimirtodos os itensde uma lista de usuários,podemos fazer um
forEachquerecebecomoparâmetroumareferênciaaométodoprintln:
usuarios.forEach(System.out::println);
Essemétodocompila,masoqueelevaiimprimir?Nãoestamospassandone-
nhumparâmetroparaométodoprintln!
Na verdade, implicitamente estamos. Quando escrevemos
System.out::printlntemosumcódigoequivalenteaessaexpressão lambda:
u -> System.out.println(u). Ouseja,ocompiladorsabequeaoiterarum
umalistadeusuários,acadaiteraçãodométodoforEachteremosumobjetodo
tipo Usuario,einferequeesseéoparâmetroquedeveráserpassadoaomethod
reference.
NossocódigotraduzidoparaJava7 ,porexemplo,seriaequivalenteaocódigoa
seguir:
35

## Página 48

6.6. Referenciandoconstrutores CasadoCódigo
for(Usuario u : usuarios) {
System.out.println(u);
}
Paratestaresseexemplo,sobrescrevaométodo toString danossaclasse
Usuario:
public String toString() {
return "Usuario " + nome;
}
Agoraescrevaaseguinteclasse,quecriaumalistadeusuários,eimprimeo
toStringdetodososusuários.
public class Capitulo6 {
public static void main(String ... args) {
Usuario user1 = new Usuario("Paulo Silveira", 150);
Usuario user2 = new Usuario("Rodrigo Turini", 120);
Usuario user3 = new Usuario("Guilherme Silveira", 190);
List<Usuario> usuarios = Arrays.asList(user1, user2, user3);
usuarios.forEach(System.out::println);
}
}
6.6 Referenciando construtores
Assimcomométodosestáticos,podemosusarmethodreferencecomconstrutores.
Porsinal,écomumouviressetipodereferênciaserchamadadeconstructorreference.
Nestecaso,usamoso newparaindicarquequeremosreferenciarumconstrutor,
destaforma:
Usuario rodrigo = Usuario::new;
Aotentarcompilaressecódigo,recebemosaseguinteexception:
Capitulo6.java:11: error: incompatible types: Usuario is not a
functional interface
Usuario rodrigo = Usuario::new;
^
1 error
36

## Página 49

CasadoCódigo Capítulo6. MethodReferences
Claro,afinal,assimcomoasexpressões lambda,precisamosguardaroresultado
dessareferênciaemumainterfacefuncional!V a m o sutilizarainterface Supplier,
tambémpresentenopacote java.util.function.Noteaassinaturadeseumé-
todo:
@FunctionalInterface
public interface Supplier<T> {
T get();
}
Elatemaformadeumafactory.Podemosguardaraexpressão Usuario::new
emum Supplier<Usuario>echamarseumétodogetsemprequefordesejada
ainstanciaçãodeumnovoobjetodotipo Usuario:
Supplier<Usuario> criadorDeUsuarios = Usuario::new;
Usuario novo = criadorDeUsuarios.get();
Utilizamosum Suppliersempreparacriarumnovoobjetoapartirdeseu
construtordefault. Casoqueiramoscriarapartirdealgumconstrutorcomargu-
mentodaclasse,precisaremosutilizaralgumaoutrainterfacefuncional.Considere
oseguinteconstrutorquerecebeuma Stringparaatribuiraonomedo Usuario:
public Usuario(String nome) {
this.nome = nome;
}
Precisamosdeumainterfacefuncionalquerecebatantooqueserácriado,que
nestecasoéotipo Usuario,comotambémqualargumentoserápassadoparao
construtor!Podemosusarainterfacequevimosnocapítuloanterior,a Function!
Nossocódigodeveficarassim:
Function<String, Usuario> criadorDeUsuarios = Usuario::new;
Pronto!Agoraconseguimoscriarnovosusuáriosinvocandoseuúnicométodo
abstrato,o apply:
Function<String, Usuario> criadorDeUsuarios = Usuario::new;
Usuario rodrigo = criadorDeUsuarios.apply("Rodrigo Turini");
Usuario paulo = criadorDeUsuarios.apply("Paulo Silveira");
37

## Página 50

6.7.Outrostiposdereferências CasadoCódigo
Neste contexto, criar um usuárioda forma antiga, dando um new
Usuario("Nome"),éverdadeiramentemaissimples,masteremosmaisparafrente
situações emqueoconstructorreferencepodeajudarbastante.
Implementaro criadorDeUsuariosfoibemsimples,não? Afinal,criamos
umconstrutorquerecebeapenasumparâmetro.Masesequisermoscriarumusuá-
riousandooconstrutordedoisparâmetros?
public Usuario(String nome, int pontos) {
this.pontos = pontos;
this.nome = nome;
}
AAPIdoJavajápossuiumainterfacefuncionalqueseencaixaperfeitamente
nessecaso,a BiFunction.
Conseguimosutilizá-laparacriarumusuáriodaseguinteforma:
BiFunction<String, Integer, Usuario> criadorDeUsuarios =
Usuario::new;
Usuario rodrigo = criadorDeUsuarios.apply("Rodrigo Turini", 50);
Usuario paulo = criadorDeUsuarios.apply("Paulo Silveira", 300);
Igualmentesimples,nãoacha?Masseeuquisercriarumusuárioapartirdeum
construtorcom3argumentosaAPIpadrãonãovaimeajudar,nãoexistenenhuma
interfaceparaessecaso!Nãosepreocupe,sefossenecessáriopoderíamosfacilmente
implementaruma TriFunctionqueresolveriaoproblema.V o c êveráqueaAPI
não possuitodasascombinações, poisnão seriapossívelcomessaabordagemde
lambdadoJava8.
Referenciando o construtor de u mAr r a y
T a m b é mconsigousarconstructorreferencecomumarray,masneste
casoasintaxevaimudarumpouco.Bastaadicionaroscolchetesdoarray
antesdodelimitador ::,porexemplo: int[]::new.
6.7 Outros tipos de referências
Nãoparaporaí.Podemosreferenciarummétodosobreescritodaclassemãe.Neste
caso,usamosapalavrareservada super,comoem super::toString.
38

## Página 51

CasadoCódigo Capítulo6. MethodReferences
T a m b é mseráútilpoder se referenciar a métodosestáticos. Por exem-
plo,podemosatribuir Math::maxauma BiFunction<Integer, Integer,
Integer>,poiselarecebedoisinteirosedevolveuminteiro.
Novamenteocuidadocomoboxing
Aatençãoaoautoboxingdesnecessárioéconstante.Assimcomovimosnocaso
da Function,a BiFunctionpossuisuasinterfacesanálogasparatiposprimitivos.
Em vez de usar a BiFunction, poderíamos usar aqui uma
ToIntBiFunction<Integer, Integer>, evitando o unboxing do retorno.
Sim,épossívelevitartodoboxing,usandouma IntBinaryOperator,querecebe
dois intsedevolveum int.
Logo,asseguintesatribuições sãotodaspossíveis:
BiFunction<Integer, Integer, Integer> max = Math::max;
ToIntBiFunction<Integer, Integer> max2 = Math::max;
IntBinaryOperator max3 = Math::max;
Qualusar? IntBinaryOperatorcertamenteémaisinteressante,masvaide-
penderdométodoquereceberánossolambdacomoargumento.Normalmentenem
paramosparapensarmuitonisso,poispassaremos Math::maxdiretamentecomo
argumentoparaalgummétodo.
39

## Página 53

Capítulo7
StreamseCollectors
Ordenarumacoleção,queéumprocessobemcomumemnossodiaadia,foibas-
tantemelhoradocomosnovosrecursosdalinguagem. Mascomopodemostirar
maiorproveitodessesrecursosemoutrassituações comunsquandoestamostra-
balhandocomumacoleção? NestecapitulovamosmostrarosavançosdaAPIde
Collectionsdeumamaneirabemprática!
7 . 1Tornando moderadores os10 usuários co m mais
pontos
Parafiltraros10usuárioscommaispontosetorná-losmoderadores,podemosagora
fazeroseguintecódigo:
usuarios.sort(Comparator.comparing(Usuario::getPontos).reversed());
usuarios
.subList(0,10)
.forEach(Usuario::tornaModerador);

## Página 54

7.2.Streams:tornandomoderadoresosusuárioscommaisde100pontos CasadoCódigo
Reparequeissojáadiantabastantecódigo!AntesdoJava8serianecessáriofazer
algocomo:
Collections.sort(usuarios, new Comparator<Usuario>() {
@Override
public int compare(Usuario u1, Usuario u2) {
return u1.getPontos() - u2.getPontos();
}
});
Collections.reverse(usuarios);
List<Usuario> top10 = usuarios.subList(0, 10);
for(Usuario usuario : top10) {
usuario.tornaModerador();
}
Agoraquerofiltrartodososusuáriosquetêmmaisde100pontos.Comoeufaço?
7 . 2Streams : tornando moderadores os usuários
co m mais de100 pontos
Comofiltroumacoleção? Possofazerumlaçoe,paracadaelemento,usarum if
parasabersedevemosounãoexecutarumatarefa.
Paratornarmoderadoresosusuárioscommaisde100pontospodemosfazer:
for(Usuario usuario : usuarios) {
if(usuario.getPontos() > 100) {
usuario.tornaModerador();
}
}
Essecódigoestámuitograndeeimperativo.Aqualquermudançanafiltragem
ounaaçãoaserexecutadateremosdeencadearmaisblocosdecódigo.Emmuitas
linguagens,háummétodofilternasdiversasestruturasdedados.
Diferentedométodosort,queexisteem List,e forEach,queexisteem
Iterable,nãoháfilteremIterable!Nemem Collectionou List.Então
ondeacabouficandodefinidoessemétodo?
ElepoderiaperfeitamentetersidoadicionadonaAPIde Collection,mas
sabemosoquantoessaAPIjáégrande,equeseriacadavezmaisdifícilevoluí-la
42

## Página 55

CasadoCódigo Capítulo7 .StreamseCollectors
semhaverumaquebradecompatibilidade.EstamosfalandodeumaAPIcommais
de15anos!
U moutropontoéque,segundoaslistasdediscussões, analisandoousodas
coleções doJavafoipossívelidentificarumpadrãomuitocomum:aslistaseramcri-
adas,transformadaspordiversasoperações comooprópriofiltroquepretendemos
usare,apósessastransformações, tudoeraresumidoemumaúnicaoperação,como
umamédiaousomadosvalorestratados.Oproblemadessepadrãoidentificadoé
que,namaiorpartedasvezes,eleexigeacriaçãodevariáveispraguardarosvalores
intermediáriosdesseprocessotodo.
Tendoessaanálisecomomotivaçãoeconhecendoaslimitações deevoluiraAPI
de Collection,oJava8introduziuo Stream.O StreamtrazparaoJavauma
formamaisfuncionaldetrabalharcomasnossascoleções, usandoumainterface
fluente!Separandoasfuncionalidadesdo Streamda Collection,tambémficou
maisfácildedeixarclaroquemétodossãomutáveis,evitarproblemadeconflitode
nomedemétodos,entreoutros.
Mascomocriarum Streamquerepresenteoselementosdaminhalistadeusu-
arios?
U mnovo default method foi adicionado na interface Collection, o
stream():
Stream<Usuario> stream = usuarios.stream();
A partir desse nosso Stream<Usuario>, conseguimos utilizar o método
filter.Elerecebeumparâmetrodotipo Predicate<Usuario>,comumúnico
métododeteste.Éamesmainterfacequeusamosno Collection.removeIf.
Podemospassarumaexpressãolambdaparadeterminarocritériodefiltro,já
que Predicateéumainterfacefuncional:
Stream<Usuario> stream = usuarios.stream();
stream.filter(u -> {return u.getPontos() > 100});
Podemosremovero returnecomissoaschavesnão são maisnecessárias,
comojáhavíamosvisto:
Stream<Usuario> stream = usuarios.stream();
stream.filter(u -> u.getPontos() > 100);
Claro,podemosaindasimplificaressaoperaçãoremovendoavariáveltemporá-
ria:
43

## Página 56

7.2.Streams:tornandomoderadoresosusuárioscommaisde100pontos CasadoCódigo
usuarios.stream()
.filter(u -> u.getPontos() > 100);
V o c êveráqueagrandemaioriadosmétodosnovosseencontranafamíliadein-
terfacesdo Stream.Dessaforma,asinterfacesantigasnãoficamcheiasdemétodos
default. Alémdisso,háumavantagemgrandedeseutilizarstreams:evitarefeitos
colateraisnacoleçãocomqueestamostrabalhando.Repare:
class Capitulo7 {
public static void main (String... args) {
Usuario user1 = new Usuario("Paulo Silveira", 150);
Usuario user2 = new Usuario("Rodrigo Turini", 120);
Usuario user3 = new Usuario("Guilherme Silveira", 90);
List<Usuario> usuarios = Arrays.asList(user1, user2, user3);
usuarios.stream()
.filter(u -> u.getPontos() > 100);
usuarios.forEach(System.out::println);
}
}
Easaídadessecódigoserá:
Usuario Paulo Silveira
Usuario Rodrigo Turini
Usuario Guilherme Silveira
Porquenasaídaapareceuo Guilherme Silveira,sendoqueelenão tem
maisde100pontos? Elenão aplicouofiltronalistadeusuários!Issoporqueo
métodofilter,assimcomoosdemaismétodosdainterface Stream,nãoalteram
oselementosdostreamoriginal!Émuitoimportantesaberqueo Streamnãotem
efeitocolateralsobreacoleçãoqueooriginou.
Porisso,semprequeaplicamosumatransformaçãoemum Stream,comofize-
moscomofilter,elenosretornaumnovo Streamcomoresultado:
Stream<Usuario> stream = usuarios.stream()
.filter(u -> u.getPontos() > 100);
Podemosalterarnossaclasse Capitulo7parafazero forEachdessenovo
stream:
44

## Página 57

CasadoCódigo Capítulo7 .StreamseCollectors
class Capitulo7 {
public static void main (String... args) {
Usuario user1 = new Usuario("Paulo Silveira", 150);
Usuario user2 = new Usuario("Rodrigo Turini", 120);
Usuario user3 = new Usuario("Guilherme Silveira", 90);
List<Usuario> usuarios = Arrays.asList(user1, user2, user3);
Stream<Usuario> stream = usuarios
.stream()
.filter(u -> u.getPontos() > 100);
stream.forEach(System.out::println);
}
}
Agorasim,aoexecutaressecódigorecebemosasaída:
Usuario Paulo Silveira
Usuario Rodrigo Turini
O Streamentãoéumaoutracoleção?Certamentenão.Amaisclaradiferença
équeum Streamnuncaguardadados.Elenãotemumaestruturadedadosinterna
paraarmazenarcadaumdoselementos:elenaverdadeusaumacoleçãooualgum
outrotipodefonteparatrabalharcomosobjetoseexecutarumasériedeoperações
(umpipelinedeoperações). Eleestámaispróximoaum Iterator.O Streamé
umasequênciadeelementosquepodesertrabalhadadediversasformas.
Podemosencadearasinvocações ao Streamdemaneirafluente. Emvezde
fazer:
Stream<Usuario> stream = usuarios
.stream()
.filter(u -> u.getPontos() > 100);
stream.forEach(System.out::println);
V a m o sutilizaroretornodo filterparaencaixardiretamenteo forEach:
usuarios.stream()
.filter(u -> u.getPontos() > 100)
.forEach(System.out::println);
45

## Página 58

7.3.ComoobterdevoltaumaLista? CasadoCódigo
Adiferençaéque forEachdevolve void,entãonessepontonãotemosmais
areferênciaao Streamresultantedo filter.Dequalquermaneira,o Stream
édesenhadoparaquevocêutilize-oapenasumavez. Casoqueirarealizarnovas
operações, vocêdeveinvocar stream()nacoleção maisumavez,obtendoum
novo.
Voltemosàquestãooriginal.Parafiltraressesusuáriosetorná-losmoderadores,
fazemosassim:
usuarios.stream()
.filter(u -> u.getPontos() > 100)
.forEach(Usuario::tornaModerador);
Outroexemplo?Parafiltrarosusuáriosquesãomoderadores,podemosfazer:
usuarios.stream()
.filter(u -> u.isModerador());
Nessecaso,o filter,assimcomoqualquerumquerecebeumainterfacefunci-
onaleinvocaapenasummétodo,podetambémtirarproveitodemethodreferences.
usuarios.stream()
.filter(Usuario::isModerador);
7 . 3Co m o obter de v o l t au m aLista?
O forEachéummétodovoid. Seo forEachévoid,eo filterdevolve
Stream<T>,quemdevolveuma Listcasoeuprecise?
Poderíamosfazerissomanualmente:criarumalistaquevaiguardarosusuários
quetêmmaisde100pontose,depoisdefiltrarquemtemmaisde100pontos,no
forEacheuadicionoessesusuáriosanovacoleção:
List<Usuario> maisQue100 = new ArrayList<>();
usuarios.stream()
.filter(u -> u.getPontos() > 100)
.forEach(u -> maisQue100.add(u));
Podemossimplificar,tirandoproveitodasintaxedomethodreferenceaqui:
usuarios.stream()
.filter(u -> u.getPontos() > 100)
.forEach(maisQue100::add);
46

## Página 59

CasadoCódigo Capítulo7 .StreamseCollectors
Aindaassimémeioesquisito.Comoissoéumtrabalhoquevaiacontecercom
frequência,háumamaneiramaissimplesdecoletaroselementosdeum Stream.
7 . 4Collectors
Podemos usar o método collect para resgatar esses elementos do nosso
Stream<Usuario>parauma List.Porém,reparesuaassinatura:
<R> R collect(Supplier<R> supplier,
BiConsumer<R, ? super T> accumulator,
BiConsumer<R, R> combiner);
Elarecebetrêsargumentos.Ostrêssãointerfacesfuncionais.Oprimeiroéuma
factoryquevaicriaroobjetoqueserádevolvidonofinaldacoleta.Osegundoéo
métodoqueseráinvocadoparaadicionarcadaelemento.Oterceiropodeserinvo-
cadoseprecisarmosadicionarmaisdeumelementoaomesmotempo(porexemplo,
seformosusarumaestratégiadecoletarelementosparalelamente,comoveremosno
futuro).
Parafazeressatransformação simples,euteriaqueescreverumcódigocomo
esse:
Supplier<ArrayList<Usuario>> supplier = ArrayList::new;
BiConsumer<ArrayList<Usuario>, Usuario> accumulator =
ArrayList::add;
BiConsumer<ArrayList<Usuario>, ArrayList<Usuario>> combiner =
ArrayList::addAll;
List<Usuario> maisQue100 = usuarios.stream()
.filter(u -> u.getPontos() > 100)
.collect(supplier, accumulator, combiner);
Bastantecomplicado,nãoacha? Poderíamostentarsimplificardeixandoocó-
digoemumúnicostatement,masaindasimteríamosumaoperaçãocomplicadae
perderíamosumpouconalegibilidade:
usuarios.stream()
.filter(u -> u.getPontos() > 100)
.collect(ArrayList::new, ArrayList::add, ArrayList::addAll);
AAPIsimplificouessetrabalho,claro.Temosumaoutraopçãodeusodométodo
collect,querecebeum Collectorcomoparâmetro:
47

## Página 60

7.5.A v a nçado:porquenãoháumtoListemStream? CasadoCódigo
<R, A> R collect(Collector<? super T, A, R> collector);
Ainterface Collectornadamaiséquealguémquetemumsupplier,umac-
cumulatoreumcombiner.AvantageméqueexistemváriosCollectorsprontos.
Podemossimplificarbastantenossocódigo,passandocomoparâmetroemnosso
método collecto Collectors.toList(),umadasimplementações dessa
novainterface.
usuarios.stream()
.filter(u -> u.getPontos() > 100)
.collect(Collectors.toList());
Collectors.toListdevolveumcoletorbemparecidocomoqualcriamos
namão,comadiferençadequeeledevolveumalistaquenãosabemosseémutável,
seéthread-safeouqualasuaimplementação.
Fazendoumimportestáticopodemosdeixarocódigoumpoucomaisenxuto,
emumúnicostatement.
usuarios.stream()
.filter(u -> u.getPontos() > 100)
.collect(toList());
Pronto! Agoraconseguimoscoletaroresultadodastransformações nonosso
Stream<Usuario>emum List<Usuario>:
List<Usuario> maisQue100 = usuarios.stream()
.filter(u -> u.getPontos() > 100)
.collect(toList());
A p e s a rdoimportestáticodeixarnossocódigomaisenxuto,evitaremosabusar.
Omotivoésimples: paraficarmaisclarodurantealeituradolivroqualmétodo
estamosinvocando.
7 . 5Av ançado : p o rque n ã o h á u m toList emStream?
EssetemafoidiversasvezesdiscutidonalistadoJava8.BrianGoetzeoutroslíderes
dãoumarespostaparecida:hámuitos,muitosmétodosquecadapessoagostariaque
tivessecomodefaultmethodemdiversasinterfaces.Sefossemaceitartodasugestão
interessante,aAPIficariaaindamaisgigante.V o c êpodelermaissobreessadecisão
aqui:
48

## Página 61

CasadoCódigo Capítulo7 .StreamseCollectors
http://openjdk.5641.n7.nabble.com/easier-work-with-collections-default-Stream-toList-tt132277.
html
T a m b é mpodemosutilizarométodotoSetparacoletarasinformações desse
Streamemum Set<Usuario>:
Set<Usuario> maisQue100 = usuarios
.stream()
.filter(u -> u.getPontos() > 100)
.collect(toSet());
HáaindaométodotoCollection,quepermitequevocêescolhaaimplemen-
taçãoqueserádevolvidanofinaldacoleta:
Set<Usuario> set = stream.collect(
Collectors.toCollection(HashSet::new));
O toCollection recebeum Supplier<T>, quejávimos. Ainterface
Supplierécomoumafactory,possuindoumúnicométodo( get)quenão re-
cebeargumentoedevolve T.Relembrandomethodreferencescomconstrutores,
fazer toCollection(HashSet::new)éomesmoque toCollection(() ->
new HashSet<Usuario>())nessecaso.
V o c êtambémpodeinvocar toArrayquedevolveumarrayde Objectem
um Stream, ouinvocaro toArray passandoaformadeconstruirumaar-
ray(atravésdeum IntSupplier). U mexemploseria Usuario[] array =
stream.toArray(Usuario[]::new).
7 . 6Liste apenas os pontos de todos os usuários co m
o map
Comoseguintecódigo,nãomuitodiferentedoquefaríamoscomasversõespré-Java
8,conseguimosextrairumalistacomapontuaçãodetodososusuários:
List<Integer> pontos = new ArrayList<>();
usuarios.forEach(u -> pontos.add(u.getPontos()));
Masreparequeéprecisocriarumavariávelintermediáriacomalista,eadicionar
ospontosmanualmente.Aindanão estamostirandomuitoproveitodanovaAPI
doJava8! Alémdisso,onossolambdaestácausandoefeitoscolaterais:alterando
49

## Página 62

7.7.IntStreameafamíliadeStreams CasadoCódigo
oestadodevariáveiseobjetosforadeseuescopo.Háalgumasdesvantagensnessa
abordagemqueentenderemosposteriormente.
Háumaformabemmaisinteressanteeconhecidadequemjátemalgumconhe-
cimentodeprogramaçãofuncional:omap.
UtilizandoométodomapdaAPIde Stream,conseguimosobteromesmore-
sultadoaplicandoumatransformaçãoemminhalistasemanecessidadedevariáveis
intermediárias!Repare:
List<Integer> pontos = usuarios.stream()
.map(u -> u.getPontos())
.collect(toList());
Eutilizandoo map,podemostirarproveitodasintaxedomethodreference,sim-
plificandoaindamaisnossaoperação:
List<Integer> pontos = usuarios.stream()
.map(Usuario::getPontos)
.collect(toList());
Reparequenementramosemdetalhesparadizeroque maprecebecomoargu-
mento.Eletrabalhacom Function,queéumainterfacefuncional.Nonossocaso,
dadoum Usuarioeleprecisadevolverum Integer,definidopeloseuúnicomé-
todoabstrato,o apply.Éuma Function<Usuario, Integer>.Percebaque
nãofoinecessáriosaberexatamenteosargumentos,retornoenomedométodopara
lermosocódigoqueusao map,jáqueolambdaajudanalegibilidade.
7 . 7IntStream e a famíliadeStreams
Repare que, quando escrevemos o seguinte código, temos como retorno um
Stream<Integer>:
Stream<Integer> stream = usuarios.stream()
.map(Usuario::getPontos);
Issogeraoboxingdosnossosinteiros. Seformosoperarsobreeles,teremos
umoverheadindesejado,quepodeserfatalparalistasgrandesoucasohajamuita
repetiçãodessainstrução.
O pacote java.util.stream possui implementações equivalentes ao
Stream para os principais tipos primitivos: IntStream, LongStream, e
DoubleStream.
50

## Página 63

CasadoCódigo Capítulo7 .StreamseCollectors
Podemosusaro IntStreamaquiparaevitaroautoboxing!Bastautilizarmoso
métodomapToInt:
IntStream stream = usuarios.stream()
.mapToInt(Usuario::getPontos);
O mapToIntrecebeumafunçãomaisespecífica.Enquantoo maprecebeuma
Function,o mapToIntrecebe ToIntFunction,interfacequeométodoapply
sempreretorna intesechama applyAsInt.
No IntStream, existemmétodosquesimplificambastantenossotrabalho
quandoestamostrabalhandocominteiros,como max, sortede average.
Observecomoficoumaissimplesobteramédiadepontosdosusuários:
double pontuacaoMedia = usuarios.stream()
.mapToInt(Usuario::getPontos)
.average()
.getAsDouble();
Veremosdepoisqueo averageéumcasoespecialdachamadaredução.
Nasversões anterioresdalinguagem,teríamosqueiterarpelosusuariosso-
mandosuaspontuações emumavariáveltemporária,parasomentenofinaldividir
essasomapelaquantidadedeelementosdalista.Algocomo:
double soma = 0;
for (Usuario u : usuarios) {
soma += u.getPontos();
}
double pontuacaoMedia = soma / usuarios.size();
V o c êveráqueaoperaçãode mapéutilizadacombastantefrequência,diretaou
indiretamente.
7 . 8OOptional em j a v a.util
Utilizamos average().getAsDouble()pararecebero doubledamédia.O
queseráqueesse average()devolve?Eporquenãoum double?
Éparatentarevitaraquelespadrões deverificaçãodecasosextremos.Porexem-
plo:
51

## Página 64

7.8.OOptionalemjava.util CasadoCódigo
double soma = 0;
for (Usuario u : usuarios) {
soma += u.getPontos();
}
double pontuacaoMedia = soma / usuarios.size();
Oqueaconteceseonúmerodeusuáriosforzero? Teremoscomoresultadoo
positivoinfinito!Eraissoquegostaríamos?Casonão,vamosadicionarum if,para
retornarzero:
double soma = 0;
for (Usuario u : usuarios) {
soma += u.getPontos();
}
double pontuacaoMedia;
if (usuarios.isEmpty()) {
pontuacaoMedia = 0;
}
else {
pontuacaoMedia = soma / usuarios.size();
}
OJava8introduzaclasse java.util.Optional,queeramuitoesperadaejá
existiaemoutraslinguagens.Elapermitequepossamoscuidardessescasosdeuma
maneiramaissimples,utilizandoumainterfacefluente.Hátambémalgumasversões
primitivas,como OptionalDoublee OptionalIntqueajudamnessescasos.
O average,quesóexisteemstreamsprimitivos,devolveum OptionalDouble.
Repare:
OptionalDouble media = usuarios.stream()
.mapToInt(Usuario::getPontos)
.average();
double pontuacaoMedia = media.orElse(0.0);
Pronto.Sealistaforvazia,ovalorde pontuacaoMediaserá0.0.Semouso
do orElse,aoinvocaro getvocêreceberiaum NoSuchElementException,
indicandoqueo Optionalnãopossuivalordefinido.
Podemosescreveremumaúnicalinha:
52

## Página 65

CasadoCódigo Capítulo7 .StreamseCollectors
double pontuacaoMedia = usuarios.stream()
.mapToInt(Usuario::getPontos)
.average()
.orElse(0.0);
Ou ir ainda além, como lançar uma exception utilizando o método
orElseThrow.Elerecebeum Supplierdeexceptions,aquelainterfacefuncional
queparecebastanteumafactory.Podemosentãofazer:
double pontuacaoMedia = usuarios.stream()
.mapToInt(Usuario::getPontos)
.average()
.orElseThrow(IllegalStateException::new);
Podemosverificarocontrário:serealmenteexisteumvalordentrodoopcional.
E,nocasodeexistir,passamosum Consumercomoargumento:
usuarios.stream()
.mapToInt(Usuario::getPontos)
.average()
.ifPresent(valor -> janela.atualiza(valor));
Hádiversosoutrosmétodosnosoptionalsevoltaremosautilizá-los,poisosstre-
amscostumamtrabalharbastantecomeles.
Ocasomaisfrequenteéquandoumvalorpodeser null.Como Optional,
vocêserásempreobrigadoatrabalharcomacondiçãodeaqueleelementonãoexistir,
evitandoum NullPointerExceptiondescuidado.
Porexemplo:queremosousuáriocommaiorquantidadedepontos.Podemos
usarométodomaxparatal,querecebeum Comparator:
Optional<Usuario> max = usuarios
.stream()
.max(Comparator.comparingInt(Usuario::getPontos));
Sealistaforvazia,nãohaveráusuárioparaserretornado.Porisso,oresultado
éum Optional. V o c êdeveverificarseháounãoumusuáriopresentenessere-
sultado,usandoosmétodosquevimos.Podeserumsimples get,podendoreceber
um null,oualgomaisrebuscadocomo orElseou ifPresent.
V o c êpodeatémesmocontinuartrabalhandocom Optionaldemaneiralazy.
Sevocêquiseronomedousuáriocommaiornúmerodepontos,podemapear(trans-
formar)esseresultado:
53

## Página 66

7.8.OOptionalemjava.util CasadoCódigo
Optional<String> maxNome = usuarios
.stream()
.max(Comparator.comparingInt(Usuario::getPontos))
.map(u -> u.getNome());
Sim,vocêpoderiausaromethodreference Usuario::getNomeaqui.
54

## Página 67

Capítulo8
Ma i soperações comStreams
Trabalharcomstreamsvaifazerpartedoseudiaadia.ConhecerbemsuaAPIatra-
vésdeexemplospráticoséumaexcelenteformadeaprendermaisconceitosqueela
envolve.
8.1 Ordenando u mStream
Dadauma List<Usuario> usuarios,sabemoscomopodemosordená-lapor
nome:
usuarios.sort(Comparator.comparing(Usuario::getNome));
Eumstream?Imaginequequeremosfiltrarosusuárioscommaisde100pontos
eaíordená-los:
usuarios.stream()
.filter(u -> u.getPontos() > 100)
.sorted(Comparator.comparing(Usuario::getNome));

## Página 68

8.2. Muitasoperações noStreamsãolazy! CasadoCódigo
Nostream,ométododeordernação éo sorted. Adiferençaentreordenar
umalistacom sorteumstreamcom sortedvocêjádeveimaginar: ummé-
todoinvocadoem Streamnão alteraquemogerou. Nocaso,elenão alteraa
List<Usuario> usuarios. Sequisermosoresultadoemuma List,precisa-
mosusarumcoletor,comovisto:
List<Usuario> filtradosOrdenados = usuarios.stream()
.filter(u -> u.getPontos() > 100)
.sorted(Comparator.comparing(Usuario::getNome))
.collect(Collectors.toList());
U mcódigofácildelerebastanteenxuto.Talvezvocênãoestejaselembrandode
comoprecisariaescrevermuitomaislinhasnoJava7 ,perdendoumpoucodaclareza
esimplicidade:
List<Usuario> usuariosFiltrados = new ArrayList<>();
for(Usuario usuario : usuarios) {
if(usuario.getPontos() > 100) {
usuariosFiltrados.add(usuario);
}
}
Collections.sort(usuariosFiltrados, new Comparator<Usuario>() {
public int compare(Usuario u1, Usuario u2) {
return u1.getNome().compareTo(u2.getNome());
}
});
Énecessáriaumalistatemporáriaparaafiltragem,umlaçoparaessemesmo
filtro,umaclasseanônima parao Comparatorefinalmenteainvocação paraa
ordenação.
8.2 Muitas operações noStream são lazy!
Quandomanipulamosum Stream,normalmenteencadeamosdiversasoperações
computacionais.Esseconjuntodeoperações realizadoemum Streaméconhecido
comopipeline.OJavapodetirarproveitodessaestruturaparaotimizarasoperações.
Comoelefazisso?Evitandoexecutarasoperações omáximopossível:grandeparte
delassão lazyeexecutamrealmentesóquandonecessárioparaobteroresultado
final.
56

## Página 69

CasadoCódigo Capítulo8. Maisoperações comStreams
U mexemplo?Pensenocódigoanterior,antesdo collect:
usuarios.stream()
.filter(u -> u.getPontos() > 100)
.sorted(Comparator.comparing(Usuario::getNome));
Osmétodosfiltere sorteddevolvemum Stream.Nomomentodessas
invocações, essesmétodosnemfiltram,nemordenam:elesapenasdevolvemnovos
streamsemqueessainformaçãoémarcada.Essesmétodossãochamadosdeope-
raçõesintermediárias.Osnovosstreamsretornadossabemquedevemserfiltrados
eordenados(ouoequivalente)nomomentoemqueumaoperaçãoterminalfor
invocada.
O collectéumexemplodeoperaçãoterminalesónessemomentoostream
realmentevaicomeçaraexecutaropipelinedeoperações pedido.
8.3 Qu a lé a v antagem d o smétodos serem lazy?
Imaginequequeremosencontrarumusuáriocommaisde100pontos.Bastaume
servequalquerum,desdequecumpraopredicadodetermaisde100pontos.
Podemosfiltrarostream,coletá-loemumalistaepegaroprimeiroelemento:
Usuario maisDe100 = usuarios.stream()
.filter(u -> u.getPontos() > 100)
.collect(Collectors.toList())
.get(0);
Émuitotrabalhoparaalgosimples:aquifiltramostodososusuáriosecriamos
umanovacoleção comtodoselesapenasparapegaroprimeiroelemento. Além
disso,nocasodenãohavernenhumusuáriocommaisde100pontos,receberemos
umaexception.
O StreampossuiométodofindAnyquedevolvequalquerumdoselementos:
Optional<Usuario> usuarioOptional = usuarios.stream()
.filter(u -> u.getPontos() > 100)
.findAny();
Háduas vantagensaqui em trabalhar com Stream. A primeira éque o
findAnydevolveum Optional<Usuario>ecomissosomosobrigadosafazer
um getpararecebero Usuario,ouusarosmétodosdeteste(como orElsee
57

## Página 70

8.4. Enxergandoaexecuçãodopipelinecompeek CasadoCódigo
isPresent)parasaberserealmenteháumusuáriofiltradoaí.Asegundavantagem
éque,comotodootrabalhofoilazy,ostreamnãofoiinteiramentefiltrado.
Éissomesmo.O findAnyéumaoperaçãoterminaleforçouaexecuçãodopi-
pelinedeoperações. Aomesmotempo,essemétodoéescritodemaneirainteligente,
analisandoasoperações invocadasanteriormenteepercebendoquenãoprecisafil-
trartodososelementosdalistaparapegarapenasumdelesquecumpraopredicado
dado.Elecomeçaaexecutarofiltroe,assimqueencontrarumusuáriocommaisde
100pontos,retorna-oeterminaafiltragemalimesmo.Outrométodoquepodeser
útiléo findFirst,similarao findAny,masutilizandooselementosnaordem
percorridapelostream.
Essatécnicadeotimizaçãonemsempreépossíveldeseraplicada,dependendo
dopipelinedeoperações. Portanto,vocênãodeveterissocomogarantiaparaescre-
vercódigopossivelmenteineficiente.
Comoverqueaotimizaçãorealmenteacontece?
V o c êpoderiacolocarumbreakpointnométodogetPontosouimprimiruma
informaçãodelogquandoeleforinvocado.V o c êveriaqueeleseráinvocadoapenas
aquantidadedevezesnecessáriaatéencontraralgum Usuariocommaisde 100
pontos! Masháumaformamaisinteressante:utilizandoométodointermediário
peek.
8.4 Enxergando a execução d opipelineco m peek
Podemospedirparaqueostreamexecuteumtarefatodavezqueprocessarumele-
mento.Fazemosissoatravésdo peek:
usuarios.stream()
.filter(u -> u.getPontos() > 100)
.peek(System.out::println)
.findAny();
Podemosverquesóserãomostradososelementosatéquesejaencontradoalgum
elementoquecumpraopredicado u.getPontos() > 100. Assim,ficaclaroo
poderqueolazynesstemnaAPIde Stream.
Bemdiferentedeum forEach,quedevolve voideéumaoperaçãoterminal,
o peekdevolveumnovo Streameéumaoperaçãointermediária.Elenãoforçará
aexecuçãodopipeline.Oseguintecódigosimplesmentenãoimprimenada:
58

## Página 71

CasadoCódigo Capítulo8. Maisoperações comStreams
usuarios.stream()
.filter(u -> u.getPontos() > 100)
.peek(System.out::println);
Porquê?Poiso peekdevolveumnovo Stream,ondeestámarcadoparaim-
primirtodososelementosprocessados.Elesóvaiprocessarelementosquandoen-
contrarumaoperaçãoterminal,comoo findAny,o collectouo forEach.
Como peek,podemosverseoutrasoperações conseguemtirarvantagemdo
lazyness.Experimentefazeromesmotruquecomo sorted:
usuarios.stream()
.sorted(Comparator.comparing(Usuario::getNome))
.peek(System.out::println)
.findAny();
Aquio peekimprimetodososusuários,mesmosesóqueremosfazer findAny.
Dizemosqueo sortedéummétodointermediáriostateful. Operações stateful
podemprecisarprocessartodoostreammesmoquesuaoperaçãoterminalnãode-
mandeisso.
8.5 Operações de redução
Operações queutilizamoselementosdastreampararetornarumvalorfinalsão
frequentementechamadasdeoperações deredução (reduction). U mexemploéo
average,quejáhavíamosvisto:
double pontuacaoMedia = usuarios.stream()
.mapToInt(Usuario::getPontos)
.average()
.getAsDouble();
Háoutrosmétodosúteiscomoo average:o count,o min,o maxeo sum.
Esseúltimo,comoo average,encontra-seapenasnosstreamsprimitivos.O min
eo maxpedemum Comparatorcomoargumento.Todos,comexceçãodo sume
count,trabalhamcom Optional.Porexemplo:
Optional<Usuario> max = usuarios.stream()
.max(Comparator.comparing(Usuario::getPontos));
Usuario maximaPontuacao = max.get();
Sedesejarmossomartodosospontosdosusuários,fazemos:
59

## Página 72

8.5.Operações deredução CasadoCódigo
int total = usuarios.stream()
.mapToInt(Usuario::getPontos)
.sum();
Essasomaéexecutadaatravésdeumaoperaçãodereduçãoquepodemosdeixar
bemexplícita.Comoelafunciona?Elapegaoprimeiroelemento,queéapontuação
doprimeirousuáriodostream,eguardaovaloracumuladoatéentão, comuma
operação desoma. T a m b é mprecisamosterumvalorinicialque,paraocasoda
soma,ézero.
Podemosquebraressaoperaçãodesomaparaenxergarmelhoroqueéumaope-
raçãoderedução.Reparenasdefinições:
int valorInicial = 0;
IntBinaryOperator operacao = (a, b) -> a + b;
IntBinaryOperator éuma interface funcional que define o método
applyAsInt,querecebedoisinteirosedevolveuminteiro.Asomaéassim,nãoé
mesmo?
Comessasdefinições, podemospedirparaqueostreamprocessearedução,
passoapasso:
int valorInicial = 0;
IntBinaryOperator operacao = (a, b) -> a + b;
int total = usuarios.stream()
.mapToInt(Usuario::getPontos)
.reduce(valorInicial, operacao);
Pronto.Temosumcódigoequivalenteao sum.Poderíamosterescritotudomais
sucintamente,semadeclaraçãodevariáveislocais:
int total = usuarios.stream()
.mapToInt(Usuario::getPontos)
.reduce(0, (a, b) -> a + b);
Podemos ir além. Na classe Integer, háagora o métodoestático
Integer.sum, quesomadoisinteiros. Emvezdolambda,podemosusarum
methodreference:
int total = usuarios.stream()
.mapToInt(Usuario::getPontos)
.reduce(0, Integer::sum);
60

## Página 73

CasadoCódigo Capítulo8. Maisoperações comStreams
Qualéavantagemdeusarmosareduçãoemvezdo sum?Nenhuma.Oimpor-
tanteéconhecê-loparapoderrealizaroperações quenãoseencontramno Stream.
Porexemplo?Multiplicartodosospontos:
int multiplicacao = usuarios.stream()
.mapToInt(Usuario::getPontos)
.reduce(1, (a,b) -> a * b);
Hátambémalgunscasosespeciaisemqueinvocaro mappodesercustoso,eo
melhorseriafazeraoperaçãodesomadiretamente.Essenãoéonossocaso,massó
paraenxergarmosoexemplo,asomasemomapficariaassim:
int total = usuarios.stream()
.reduce(0, (atual, u) -> atual + u.getPontos(), Integer::sum);
Esseoverloaddo reducerecebemaisumlambdaque,nonossocaso,éo
Integer::sum. Esselambdaamaisserveparacombinarosvaloresdereduções
parciais,nocasodestreamsparalelos.
Não hánecessidadedequerersempreevitaronúmerodeoperações emum
stream.Sãocasosisoladosemquetiraremosproveitodessaabordagem.
Emoutraslinguagens,essaoperaçãotambéméconhecidacomofold.Veremos,
nopróximocapítulo,queessasoperações sãoparalelizáveisetiramgrandeproveito
dosstreamsparalelos.T a m b é mrepararemosqueo collectéumcasoderedução.
8.6 Conhecendo mais métodos d oStream
Sãomuitasasfuncionalidadesdo Stream.Olivronãotemintençãodecobrirtodos
osmétodosdaAPI,maspodemospassarrapidamenteporalgunsdosmaisinteres-
santes,alémdosquejávimosporaqui.
Alémdisso,conheceremosmaisalgunsdetalhessobreobomusodosstreams.
Trabalhandocomiterators
Vimosquepodemoscoletaroresultadodeumpipelinedeoperações deum
Streamemumacoleçãocomo collect.Algumasvezesnemprecisamosdeuma
coleção:bastariaiterarmospeloselementosdeum Stream.
Oqueseráqueacontecesetentarmospercorrero Streamdamaneiraantiga?
for (Usuario u : usuarios.stream()){
//...
}
61

## Página 74

8.6. ConhecendomaismétodosdoStream CasadoCódigo
Ocorreumerrodecompilação. Oenhancedforesperaouumaarrayouum
Iterable.
Masporquedecidiramfazercomque Streamnãosejaum Iterable?Pois
asdiversasoperações terminaisdeum Streamomarcamcomojáutilizado.Sua
segundainvocaçãolançaum IllegalStateException.V a l elembrarquesevocê
invocarduasvezes usuarios.stream()nãohaveráproblema,poisabrimosdois
streamsdiferentesacadainvocação!
Porém,podemos percorrer os elementos de um Stream atravésde um
Iterator.Paraisso,podemosinvocarométodoiterator:
Iterator<Usuario> i = usuarios.stream().iterator();
Ainterface IteratorjáexistehábastantetemponoJavaedefineosmétodos
hasNext, nexte remove.ComoJava8,tambémpodemospercorrerumiterator
utilizandoométodoforEachRemainingquerecebeum Consumercomoparâ-
metro:
usuarios.stream().iterator()
.forEachRemaining(System.out::println);
Masquandodevemosutilizarumiteratordeum Stream,seháum forEach
tantoem Collectionquantonopróprio Stream?
U mmotivoparausarum Iteratoréquandoqueremosmodificarosobjetos
deum Stream.Quandoutilizarmosstreamsparalelos,veremosquenãodevemos
mudaroestadodosobjetosqueestãonele,correndooriscodeterresultadosnãode-
terminísticos.OutromotivoéacompatibilidadedeAPIs.Podeserquevocêprecise
invocarummétodoquerecebe Iterator.
TestandoPredicates
Vimosbastanteousodo filter.Elerecebeumlambdacomoargumento,que
édainterface Predicate.Háoutrassituações emquequeremostestarpredicados
masnãoprecisamosdalistafiltrada.Porexemplo,sequisermossaberseháalgum
elementodaquelalistadeusuáriosqueémoderador:
boolean hasModerator = usuarios.stream()
.anyMatch(Usuario::isModerador);
62

## Página 75

CasadoCódigo Capítulo8. Maisoperações comStreams
Aqui o Usuario::isModerador tem o mesmo efeito que u ->
u.isModerador(), gerando um predicado que testa se um usuárioémode-
radoredevolveumbooleano.Oprocessamentodessaoperaçãovaipararassimque
ostreamencontraralgumusuárioqueémoderador.
Assimcomoo anyMatch,podemosdescobrirsetodososusuáriossãomode-
radorescom allMatchousenenhumdelesé,como noneMatch.
Hámuitosoutrosmétodosedetalhes!
V o c êpodeutilizaro countparasaberquantoselementosháno Stream, skip
parapularos npróximoselementose limitparacortaronúmerodeelementos.
T a m b é mháformasdevocêcriarum Streamsemaexistênciadeumacoleção.
Naprópriainterface Streamháosmétodosestáticosemptye of. Oprimeiro
claramentecriaum Streamvazio,eo ofdependedoquevocêpassarcomoar-
gumento,comoporexemplo Stream.of(user1, user2, user3)retornaum
Stream<Usuario>.V o c êtambémpodeconcatená-loscom Stream.concat.
Foradaprópriainterfacetambémpodemosproduzir Streams. Porexemplo,
vocêpodeusaraAPIderegexparadevolverum Stream<String>atravésdo
Pattern.splitAsStream,ouaindapegarum Streamdaslinhasdeumarquivo
como Files.lines.Seestivertrabalhandodiretamentecomumarray,podeusar
o Arrays.stream.
NãodeixedeconheceraAPIeinvestigarbastanteessaimportanteinterfacesem-
prequetivernovasideiasesentirfaltadealgummétodo:eleprovavelmenteexiste.
Outropontorelevante:comoalguns Streamspodemseroriginadosderecur-
sosdeIO,eleimplementaainterface AutoCloseableepossuio close. U m
exemploéusarosnovosmétodosdaclasse java.nio.file.Files,incluídano
Java7ecomnovidadesnoJava8,paragerarum Stream.Nessecaso,éfundamen-
taltratarasexceções eo finally,ouentãousarotrywithresources. Emoutras
situações, quandosabemosqueestamoslidandocomstreamsgeradosporcoleções,
essapreocupaçãonãoénecessária.
8.7 Streams primitivos e infinitos
Assimcomovimoscomo comparingInt,quedevolveum Comparatorquenão
temanecessidadedefazerounboxing,vimostambémocasodo mapToInt,que
devolveum IntStream,tambémparaevitaroperações desnecessárias.
63

## Página 76

8.7.Streamsprimitivoseinfinitos CasadoCódigo
O IntStream,o LongStreameo DoubleStreampossuemoperações espe-
ciaisequesãoimportantes.A t émesmoo iteratordelesdevolvem Iterators
diferentes.Nocasodo IntStream,éo PrimitiveIterator.OfInt,queim-
plementa Iterator<Integer>masque,alémdeum nextquedevolveum
Integerfazendooboxing,tambémpossuio nextInt.
T e maindamétodosdefactory,como IntStream.range(inicio, fim).
Streamsinfinitos
U moutrorecursopoderosodoJava8:atravésdainterfacedefactory Supplier,
podemosdefinirum Streaminfinito,bastandodizerqualéaregraparaacriação
deobjetospertencentesaesse Stream.
Porexemplo,sequisermosgerarumalista“infinita”denúmerosaleatórios,po-
demosfazerassim:
Random random = new Random(0);
Supplier<Integer> supplier = () -> random.nextInt();
Stream<Integer> stream = Stream.generate(supplier);
O Streamgeradopor generateélazy.Certamenteelenãovaigerarinfinitos
númerosaleatórios.Elessóserãogeradosàmedidaqueforemnecessários.
Aquiestamosgerandooboxingotempotodo.Podemosusaro IntSupplier
eo IntStream.Alémdisso,removeremosavariáveltemporáriasupplier:
Random random = new Random(0);
IntStream stream = IntStream.generate(() -> random.nextInt());
Agoraprecisamosdecuidado.Qualqueroperaçãoquenecessitepassarportodos
oselementosdo Streamnuncaterminarádeexecutar.Porexemplo:
int valor = stream.sum();
V o c êpodeapenasutilizaroperações decurto-circuitoem Streamsinfinitos.
Operaçõesdecurtocircuito
São operações quenão precisamprocessartodososelementos. U mexemplo
seriapegarapenasos100primeiroselementoscom limit:
Random random = new Random(0);
IntStream stream = IntStream.generate(() -> random.nextInt());
64

## Página 77

CasadoCódigo Capítulo8. Maisoperações comStreams
List<Integer> list = stream
.limit(100)
.boxed()
.collect(Collectors.toList());
Repareainvocação de boxed. Eleretornaum Stream<Integer>emvez
do IntStream,possibilitandoainvocação a collectdaformaquejávimos.
Semisso,teríamosapenasaopção defazer IntStream.toArray,ouentão de
chamaro collectquerecebetrêsargumentos,masnão teríamosondeguardar
osnúmeros.NãofoicriadonoJavaum IntListqueseriaoanálogoprimitivo
a List<Integer>,etambémnãoentraramnoJava8ostaisdosvalueobjectsou
valuetypes,quepossibilitariamalgocomo List<int>.
V a m o sreveromesmocódigocomainterfacefluente:
Random random = new Random(0);
List<Integer> list = IntStream
.generate(() -> random.nextInt())
.limit(100)
.boxed()
.collect(Collectors.toList());
O Supplier passadoao generate podeservir paragerarum Stream
infinito de constantes, por exemplo IntStream.generate(() -> 1) e
Stream.generate(() -> new Object()).
Podeserútilparaum Suppliermanterestado.Nessecaso,precisamosusar
umaclasseouclasseanônima, poisdentrodeumlambdanão podemosdeclarar
atributos. V a m o sgerarasequênciainfinitadenúmerosdeFibonaccidemaneira
lazyeimprimirseus10primeiroselementos:
class Fibonacci implements IntSupplier {
private int anterior = 0;
private int proximo = 1;
public int getAsInt() {
proximo = proximo + anterior;
anterior = proximo - anterior;
return anterior;
}
}
65

## Página 78

8.7.Streamsprimitivoseinfinitos CasadoCódigo
IntStream.generate(new Fibonacci())
.limit(10)
.forEach(System.out::println);
Veremosquemanteroestadoemumainterfacefuncionalpodelimitarosrecur-
sosdeparalelizaçãoqueum Streamfornece.
Alémdo limit,háoutrasoperações quesãodecurto-circuito.O findFirst
éumadelas.MasnãoqueremospegaroprimeiroelementoFibonacci.Queropegar
oprimeiroelementomaiorque100!Comofazer?Podemosfiltrarantesdeinvocar
o findFirst:
int maiorQue100 = IntStream
.generate(new Fibonacci())
.filter(f -> f > 100)
.findFirst()
.getAsInt();
System.out.println(maiorQue100);
O filternão édecurto-circuito: elenão produzum Streamfinitodado
um Streaminfinito.Bastaapenasquevocêtenhaumaoperaçãodecurto-circuito
nopipeline(sejaaoperaçãointermediáriaoufinal),quevocêteráchancesdeque
aexecuçãodopipelinenãotometempoinfinito.Porquedigochances? Pois,por
exemplo,senãohouvesseumelementodeFibonaccimaiorque100,issotambém
rodariaindefinidamente.
Osmatcherstambémsãodecurto-circuito.Podemostentardescobrirsetodosos
elementosdeFibonaccisãoparescom allMatch(f -> f % 2 ==0).Sehouver
algumimpar,eleretornaráfalso.Massehouvesseapenaspares,elerodariaindefini-
damente!Lembre-se:trabalharcom Streamsinfinitospodeserperigoso,mesmo
quevocêutilizeoperações decurto-circuito.
Quandofornecessáriomanteroestadodeapenasumavariável,podemosusar
o iterateemvezdo generate,querecebeum UnaryOperator.Parageraros
númerosnaturais:
IntStream.iterate(0, x -> x + 1)
.limit(10)
.forEach(System.out::println);
Hámodificações tambémnaAPIantigaparatrabalharcom Streamsinfinitos.
V o c êpodeverqueaclasse java.util.Randomjádevolve Streamsinfinitos,
atravésdemétodoscomo Random.ints().
66

## Página 79

CasadoCódigo Capítulo8. Maisoperações comStreams
8.8 Praticando o que aprendemos co m
j a v a.nio.file.Files
Aclasse java.nio.file.FilesentrounoJava7parafacilitaramanipulaçãode
arquivosediretórios,trabalhandocomainterface Path. Éumadasclassesque
agorapossuemmétodosparatrabalharcom Stream.Excelenteoportunidadepara
praticarmosboapartedoqueaprendemos.
Se quisermos listar todos os arquivos de um diretório, basta pegar o
Stream<Path>edepoisum forEach:
Files.list(Paths.get("./br/com/casadocodigo/java8"))
.forEach(System.out::println);
Querapenasosarquivos java?Podeusarum filter:
Files.list(Paths.get("./br/com/casadocodigo/java8"))
.filter(p -> p.toString().endsWith(".java"))
.forEach(System.out::println);
E se quisermos todo o conteúdodos arquivos? V a m o stentar usar o
Files.linesparalertodasaslinhasdecadaarquivo.
Files.list(Paths.get("./br/com/casadocodigo/java8"))
.filter(p -> p.toString().endsWith(".java"))
.map(p -> Files.lines(p))
.forEach(System.out::println);
Infelizmenteessecódigonãocompila.Oproblemaéque Files.lineslança
IOException. Mesmoqueométodoqueinvocao maplanceessaexception,
nãocompilará,poisnessecasoéaimplementaçãodolambdaqueestarálançando
IOException.O maprecebeuma Function,quetemométodoapplyeque
nãolançaexceptionalgumanaassinatura.
U m asoluçãoseriaescreverumaclasseanônimaouumlambdadefinidocomas
chavesecom try/catchpordentro.Outraseriafazerummétodoestáticosimples,
quefazo wrapdachamadaparaevitaracheckedexception:
static Stream<String> lines(Path p) {
try {
return Files.lines(p);
} catch(IOException e) {
67

## Página 80

8.9. FlatMap CasadoCódigo
throw new UncheckedIOException(e);
}
}
Emvezdeinvocarmos map(p -> Files.lines(p)),invocamosonosso
próprio lines,quenãolançacheckedexception:
Files.list(Paths.get("./br/com/casadocodigo/java8"))
.filter(p -> p.toString().endsWith(".java"))
.map(p -> lines(p))
.forEach(System.out::println);
Agoraocódigocompila.Asaídaéalgocomo:
java.util.stream.ReferencePipeline$Head@5b6f7412
java.util.stream.ReferencePipeline$Head@27973e9b
java.util.stream.ReferencePipeline$Head@312b1dae
java.util.stream.ReferencePipeline$Head@7530d0a
...
Oproblemaéque,comesse map,teremosum Stream<Stream<String>>,
poisainvocaçãode lines(p)devolveum Stream<String>paracada Pathdo
nosso Stream<Path>original!Issoficamaisclarodeobservarsenãousarmoso
forEacheatribuirmosoresultadoaumavariável:
Stream<Stream<String>> strings =
Files.list(Paths.get("./br/com/casadocodigo/java8"))
.filter(p -> p.toString().endsWith(".java"))
.map(p -> lines(p));
8.9 Fl a tMap
Podemosachatarum Streamde Streamscomo flatMap.Bastatrocarainvo-
cação,queteremosnofinalum Stream<String>:
Stream<String> strings =
Files.list(Paths.get("./br/com/casadocodigo/java8"))
.filter(p -> p.toString().endsWith(".java"))
.flatMap(p -> lines(p));
68

## Página 81

CasadoCódigo Capítulo8. Maisoperações comStreams
Issopodeserencadeadoemváriosníveis.Paracada Stringpodemosinvo-
car String.chars()eobterum IntStream(definiramassimparaevitarobo-
xingpara Stream<Character>).Sefizermos map(s -> s.chars()),obtere-
mosumindesejado Stream<IntStream>.Precisamospassaresselambdaparao
flatMaptoInt:
IntStream chars =
Files.list(Paths.get("./br/com/casadocodigo/java8"))
.filter(p -> p.toString().endsWith(".java"))
.flatMap(p -> lines(p))
.flatMapToInt((String s) -> s.chars());
O IntStreamresultantepossuitodososcaracteresdetodososarquivos java
donossodiretório.
MaisumexemplodeflatMap
Quandotrabalhamoscomcoleções decoleções, usamoso flatMapquando
queremosqueoresultadodanossatransformaçãosejareduzidoaum Stream‘sim-
ples’,semcomposição.
Imaginequetemosgruposdeusuários:
class Grupo {
private Set<Usuario> usuarios = new HashSet<>();
public void add(Usuario u) {
usuarios.add(u);
}
public Set<Usuario> getUsuarios() {
return Collections.unmodifiableSet(this.usuarios);
}
}
Equetenhamosalgunsgrupos,separandoquemfalainglêsequemfalaespanhol:
Grupo englishSpeakers = new Grupo();
englishSpeakers.add(user1);
englishSpeakers.add(user2);
Grupo spanishSpeakers = new Grupo();
69

## Página 82

8.9. FlatMap CasadoCódigo
spanishSpeakers.add(user2);
spanishSpeakers.add(user3);
Setemosessesgruposdentrodeumacoleção:
List<Grupo> groups = Arrays.asList(englishSpeakers, spanishSpeakers);
Podeserquequeiramostodososusuáriosdessesgrupos.Sefizermosumsim-
ples groups.stream().map(g -> g.getUsuarios().stream()),teremos
um Stream<Stream<Usuario>>,quenãodesejamos. O flatMapvaidesem-
brulharesses Streams,achatando-os.
groups.stream()
.flatMap(g -> g.getUsuarios().stream())
.distinct()
.forEach(System.out::println);
Temoscomoresultadotodososusuáriosdeambososgrupos,semrepetição.
Setivéssemoscoletadooresultadodopipelineemum Set,nãoprecisaríamosdo
distinct.
U moutro exemplo de uso de flatMap? Se nossos Usuarios pos-
suíssem List<Pedido> pedidos, chamar o usuarios.map(u ->
u.getPedidos()) geraria um Stream<List<Pedido>>. Se vocêtentar
fazer usuarios.map(u -> u.getPedidos().stream()), vai cair no
Stream<Stream<Pedido>>.Arespostaparaobterum Stream<Pedido>com
ospedidosdetodososusuáriosdanossalistaéfazer usuarios.flatMap(u ->
u.getPedidos().stream()).
70

## Página 83

Capítulo9
Map e a n d o,particionando,
agrupandoeparalelizando
Podemosrealizartarefasmaiscomplexaseinteressantescomousodestreamse
coletores. V a m o svercódigosmaiselaboradosenecessidadesqueaparecemcom
frequência.
9.1 Coletores gerando mapas
Vimoscomogerarum Streamcomtodasaslinhasdosarquivosdedeterminado
diretório:
Stream<String> strings =
Files.list(Paths.get("./br/com/casadocodigo/java8"))
.filter(p -> p.toString().endsWith(".java"))
.flatMap(p -> lines(p));

## Página 84

9.1.Coletoresgerandomapas CasadoCódigo
Poderíamosterum Streamcomaquantidadedelinhasdecadaarquivo.Para
isso,emvezdefazerum flatMapparaaslinhas,fazemosum mapparaaquantidade
delinhas,usandoo countdo Stream:
LongStream lines =
Files.list(Paths.get("./br/com/casadocodigo/java8"))
.filter(p -> p.toString().endsWith(".java"))
.mapToLong(p -> lines(p).count());
Sequisermosuma List<Long>comosvaloresdesse LongStream,fazemos
um collectcomojáconhecemos.
List<Long> lines =
Files.list(Paths.get("./br/com/casadocodigo/java8"))
.filter(p -> p.toString().endsWith(".java"))
.map(p -> lines(p).count())
.collect(Collectors.toList());
U mdetalhe: reparequepoderíamosusaro mapToLongedepoisinvocaro
boxedparafazero collect,masusamoso map,quejáretorna Stream<Long>
emvezde LongStream.
Dequalquermaneira,oresultadonãoparecemuitoútil:ummontede longs.
Oqueprecisamoscommaisfrequênciaésaberquantaslinhastemcadaarquivo,por
exemplo.Podemosfazerum forEachepopularum Map<Path, Long>,noqual
achaveéoarquivoeovaloréaquantidadedelinhasdaquelearquivo:
Map<Path, Long> linesPerFile = new HashMap<>();
Files.list(Paths.get("./br/com/casadocodigo/java8"))
.filter(p -> p.toString().endsWith(".java"))
.forEach(p ->
linesPerFile.put(p, lines(p).count()));
System.out.println(linesPerFile);
Oresultadoseráalgocomo:
{
./br/com/casadocodigo/java8/Capitulo3.java=45,
./br/com/casadocodigo/java8/Usuario.java=44,
./br/com/casadocodigo/java8/Capitulo8.java=156,
...
}
72

## Página 85

CasadoCódigo Capítulo9. Mapeando,particionando,agrupandoeparalelizando
Essaabordagemestácorretaejáémuitomaisconcisaeexpressivadoqueseti-
véssemosusado BufferedReaderseloopsparacriaresse Map.Aomesmotempo,
essasoluçãonãoémuitofuncional:olambdapassadoparao forEachutilizauma
variáveldeclaradaforadoseuescopo,mudandoseuestado,oquechamamosde
efeitocolateral.Issodiminuiapossibilidadedeotimizações, emespecialparaaexe-
cuçãoemparalelo.
Podemoscriaressemesmomapacomumoutrocoletormaisespecíficoparaesse
tipodetarefa,o toMap:
Map<Path, Long> lines =
Files.list(Paths.get("./br/com/casadocodigo/java8"))
.filter(p -> p.toString().endsWith(".java"))
.collect(Collectors.toMap(
p -> p,
p -> lines(p).count()));
System.out.println(lines);
O toMaprecebeduas Functions. Aprimeiraproduziráachave(nonosso
casoopróprio Path)easegundaproduziráovalor(aquantidadedelinhas).Como
écomumprecisarmosdeumlambdaqueretornaopróprioargumento(onosso p
-> p),podemosutilizar Function.identity()paradeixarmaisclaro.
Sequisermosgerarummapadecadaarquivoparatodaalistadelinhascon-
tidasnosarquivos,podemosutilizarumoutrocoletoregerarum Map<Path,
List<String>>:
Map<Path, List<String>> content =
Files.list(Paths.get("./br/com/casadocodigo/java8"))
.filter(p -> p.toString().endsWith(".java"))
.collect(Collectors.toMap(
Function.identity(),
p -> lines(p).collect(Collectors.toList())));
Certamente,o toMapvaiaparecerbastantenoseucódigo.Sãomuitososcasos
emquequeremosgerarmapastemporáriosparaprocessardadosegerarestatísticas
erelatórios.
Mapeartodososusuáriosutilizandoseunomecomochaveficafácil:
Map<String, Usuario> nameToUser = usuarios
.stream()
73

## Página 86

9.2. groupingByepartitioningBy CasadoCódigo
.collect(Collectors.toMap(
Usuario::getNome,
Function.identity()));
Se o Usuario fosse uma entidade JPA, poderíamos utilizar
toMap(Usuario::getId, Function.identity)paragerarum Map<Long,
Usuario>,noqualachaveéo iddaentidade.
9.2 grouping By e partitioningBy
Hámuitoscoletoresjáprontosquesabemgerarmapasimportantes.Paraosnossos
exemplosficaremmaisinteressantes,vamospopularnossalistadeusuárioscommais
objetos:
Usuario user1 = new Usuario("Paulo Silveira", 150, true);
Usuario user2 = new Usuario("Rodrigo Turini", 120, true);
Usuario user3 = new Usuario("Guilherme Silveira", 90);
Usuario user4 = new Usuario("Sergio Lopes", 120);
Usuario user5 = new Usuario("Adriano Almeida", 100);
List<Usuario> usuarios =
Arrays.asList(user1, user2, user3, user4, user5);
Considerequeo booleanpassadoparaasobrecargadoconstrutorde Usuario
éparadefinirseeleéummoderadorounão.
Queremosummapaemqueachavesejaapontuaçãodousuárioeovalorseja
umalistadeusuáriosquepossuemaquelapontuação. Istoé,um Map<Integer,
List<Usuario>>.
Parafazerissodemaneiratradicional,precisamospassarportodososusuários
eversejáexisteumalistaparaaquelapontuação. Casonão exista,criamosuma
ArrayList. Seexiste,adicionamosousuárioalista. Ocódigoficadaseguinte
forma:
Map<Integer, List<Usuario>> pontuacao = new HashMap<>();
for(Usuario u: usuarios) {
if(!pontuacao.containsKey(u.getPontos())) {
pontuacao.put(u.getPontos(), new ArrayList<>());
}
pontuacao.get(u.getPontos()).add(u);
7 4

## Página 87

CasadoCódigo Capítulo9. Mapeando,particionando,agrupandoeparalelizando
}
System.out.println(pontuacao);
Asaídaéaseguinte,aquiformatadaparafacilitaraleitura:
{
100=[Usuario Adriano Almeida],
150=[Usuario Paulo Silveira],
120=[Usuario Rodrigo Turini, Usuario Sergio Lopes],
90=[Usuario Guilherme Silveira]
}
NoJava8poderíamosdiminuirumpoucoessecódigocomaajudadenovos
métodosdefaultdo Map:
Map<Integer, List<Usuario>> pontuacao = new HashMap<>();
for(Usuario u: usuarios) {
pontuacao
.computeIfAbsent(u.getPontos(), user -> new ArrayList<>())
.add(u);
}
System.out.println(pontuacao);
OmétodocomputeIfAbsentvaichamara Functiondolambdanocasode
nãoencontrarumvalorparaachaveu.getPontos()eassociaroresultado(anova
ArrayList)aessamesmachave.Istoé,essainvocaçãodo computeIfAbsentfaz
opapeldo ifquefizemosnocódigoanterior.
Masoquerealmentequeremosétrabalharcom Streams. Poderíamoses-
creverum Collectoroutrabalharmanualmentecomo reduce,masháum
Collectorquefazexatamenteessetrabalho:
Map<Integer, List<Usuario>> pontuacao = usuarios
.stream()
.collect(Collectors.groupingBy(Usuario::getPontos));
Asaídaéamesma! Osegredoéo Collectors.groupingBy,queéuma
factoryde Collectorsquefazemagrupamentos.
Podemosfazermais.Podemosparticionartodososusuáriosentremoderadores
enãomoderadores,usandoo partitionBy:
75

## Página 88

9.2. groupingByepartitioningBy CasadoCódigo
Map<Boolean, List<Usuario>> moderadores = usuarios
.stream()
.collect(Collectors.partitioningBy(Usuario::isModerador));
System.out.println(moderadores);
Oresultadoéummapaparalistascomquemémoderadorequemnãoé:
{
false=
[Usuario Guilherme Silveira, Usuario Sergio Lopes,
Usuario Adriano Almeida],
true=
[Usuario Paulo Silveira, Usuario Rodrigo Turini]
}
O partitioningBynadamaisédoqueumaversão maiseficienteparaser
usadaaoagrupar booleans.
O partitioningBy(Usuario::isModerador) nos devolve um
Map<Boolean, List<Usuario>>. E se quiséssemosuma lista com os no-
mes dos usuários? Se fizermos stream().map(Usuario::getNome) não
poderemosparticionarpor Usuario::isModerador,poiso mapnosretornaria
um Stream<String>.
T a n t oo partitioningByquantoo groupingBypossuemumasobrecarga
quepermitepassarum Collectorcomoargumento.Háum Collectorquesabe
coletarosobjetosaomesmotempoquerealizaumatransformaçãode map:
Emvezdeguardarosobjetosdosusuários,poderíamosguardarumalistacom
apenasonomedecadausuário,usandoo mappingparacoletaressesnomesem
umalista:
Map<Boolean, List<String>> nomesPorTipo = usuarios
.stream()
.collect(
Collectors.partitioningBy(
Usuario::isModerador,
Collectors.mapping(Usuario::getNome,
Collectors.toList())));
Eoresultado:
76

## Página 89

CasadoCódigo Capítulo9. Mapeando,particionando,agrupandoeparalelizando
{
false=
[Guilherme Silveira, Sergio Lopes, Adriano Almeida],
true=
[Paulo Silveira, Rodrigo Turini]
}
V a m o sa maisum desafio. Queremosparticionarpor moderação, master
comovalornão osusuários,massimasomadeseuspontos. T a m b é mexisteum
coletorpararealizaressassomatórias, quepode serusadoemconjuntocomo
partitioningBye groupingBy:
Map<Boolean, Integer> pontuacaoPorTipo = usuarios
.stream()
.collect(
Collectors.partitioningBy(
Usuario::isModerador,
Collectors.summingInt(Usuario::getPontos)));
System.out.println(pontuacaoPorTipo);
Eoresultadoindicaquantospontostotalizamosmoderadoreseosusuáriosnor-
mais:
{false=310, true=270}
Conhecerbemtodaafactory Collectorscertamentevaiajudarsuasmanipu-
lações decoleções. Percebaquenãousamosmaisloopsparaprocessaroselementos.
A t émesmoparaconcatenartodososnomesdosusuáriosháumcoletor:
String nomes = usuarios
.stream()
.map(Usuario::getNome)
.collect(Collectors.joining(", "));
Comosstreamsecoletores,conseguimososmesmosresultadosdeantigamente,
porémemumestilofuncionaleconsequentementemaisenxutoeexpressivo.Além
disso,mesmoquevocênãotenhapercebido,acabamostrabalhandocommenosefei-
toscolateraisefavorecemosaimutabilidadedascoleções originais.
Equaléavantagemdeevitarefeitoscolateraisemutabilidade?Facilitarapara-
lelização.
77

## Página 90

9.3.Executandoopipelineemparalelo CasadoCódigo
9.3 Executando o pipelineem paralelo
V a m o svoltaraumexemplosimplesdeusodosstreams.Filtrarosusuárioscommais
de100pontos,ordená-losecoletaroresultadoemumalista:
List<Usuario> filtradosOrdenados = usuarios.stream()
.filter(u -> u.getPontos() > 100)
.sorted(Comparator.comparing(Usuario::getNome))
.collect(Collectors.toList());
Tudoacontecenaprópriathread,comoéesperado.Setivermosumalistacom
milhões deusuários,oprocessopoderálevarmaisquealgunssegundos.
Eseprecisarmosparalelizaresseprocesso? A t éseusmartphonepossui4pro-
cessadores.Escreverumcódigoqueuse Threadparafiltrar,ordenarecoletardá
bastantetrabalho.U m aopçãoseriatirarproveitodaAPIdeFork/Join.A p e s a rdejá
serumpoucomaissimples,aindaassimnãoéumatarefafácil.
Ascollectionsoferecemumaimplementaçãode Streamdiferente,ostreampa-
ralelo.Aousarumstreamparalelo,elevaidecidirquantasthreadsdeveutilizar,como
devequebraroprocessamentodosdadosequalseráaformadeuniroresultadofi-
nalemumsó. Tudoissosemvocêterdeconfigurarnada. Bastaapenasinvocar
parallelStreamemvezde Stream:
List<Usuario> filtradosOrdenados = usuarios.parallelStream()
.filter(u -> u.getPontos() > 100)
.sorted(Comparator.comparing(Usuario::getNome))
.collect(Collectors.toList());
Pronto!Oresultadoseráexatamenteomesmodaversãosequencial.
Casovocênãotenhaacessoaoprodutordedadosoriginal,o Streamtemum
métodoparallelquedevolvesuaversãodeexecuçãoemparalelo.Hátambémo
sequentialqueretornasuaversãoclássica.
Performancefinal
Seucódigovairodarmaisrápido?Nãosabemos. Seacoleção forpequena,o
overheaddeutilizaressaabordagemcertamentetornaráaexecuçãobemmaislenta.
Énecessáriotomarcuidadocomousodosstreamsparalelos.Elessãoumaforma
simplesderealizaroperações comaAPIdeFork/Join:otamanhodoinputprecisa
sergrande.
78

## Página 91

CasadoCódigo Capítulo9. Mapeando,particionando,agrupandoeparalelizando
Comumacoleçãopequena,nãopodemosenxergarasperdaseganhoscomfa-
cilidade.V a m o sgerarumaquantidadegrandedenúmeros,filtrá-loseordená-los,
parapoderterumabasedecomparação.
Paragerarosnúmerosde1aumbilhão,utilizaremoso LongStream.range.
Usaremoso paralleleo filterparafiltrar:
long sum =
LongStream.range(0, 1_000_000_000)
.parallel()
.filter(x -> x % 2 == 0)
.sum();
System.out.println(sum);
Emumcomputadorcom2cores,executamosocódigoem 1.276sdetempo
realmentegasto.Asconfiguraçõesdamáquinanãoimportammuito,oquequeremos
éfazeracomparação.
Removendoainvocaçãodo parallel(),otempoésignificativamentemaior:
1.842s.Nãoéodobro,poisparalelizaraexecuçãodeumpipelinesempretemseu
preço.
Essadiferençafavoreceo parallelpoistemosuminputgrandededados.Se
diminuirmosasequênciageradade1bilhãopara1milhão,ficaclarooproblema.O
paralelorodaem 0.239seosequencialem 0.201.Issomesmo:aversãoparalela
émaislentaporcausadooverhead:quebraroproblemaemváriaspartes,juntaros
dadosresultantesetc.
Sãodoisfatoresquepodemajudarsuadecisão: otamanhodoinputdosdados
eavelocidadedeexecuçãodaoperação. Somadenúmeroséumaoperaçãomuito
barata,porissoénecessáriouminputgrande.Seaoperaçãofossemaislenta,envol-
vesseoperações blocantes,otamanhonecessárioparavalerapenaseriamenor.
Microbenchmarkssãosempreperigososepodemenganarcomfacilidade,ainda
maissemsaberquaisserãoasoperações realizadas.Sejacéticoetesteseuspróprios
casos.
9.4 Operações n ã o determinísticas e ordered stre-
ams
Hádiversasoutrasconsiderações quedevemserfeitas.Algumasoperações nopipe-
linesãochamadasdenão-determinísticas. Elaspodemdevolverdiferentesresulta-
79

## Página 92

9.4. Operações nãodeterminísticaseorderedstreams CasadoCódigo
dosquandoutilizadasemstreamsparalelos.Osprincipaisexemplossãoo forEach
eo findAny.
Aoinvocaressesdoismétodosemumstreamparalelo,vocênãotemgarantiada
ordemdeexecução. Issomelhorasuaperformanceemparalelo.Casonecessitega-
rantiraordemdaexecução,vocêdeveutilizaro forEachOrderedeo findFirst
respectivamente.Namaioriadasvezeselesnãosãonecessários.
Mesmométodoscomo mappodemtersuaexecuçãoemparalelomelhoradas.
Quandocriamosum streamdeuma List(oudo LongStream.range),eleé
criadodemaneira ordered. Istoé,aocoletarmosalistaresultantedeum map
dafunção x -> x + 1noselementos 1, 2, 3,nofinalteremos 2, 3, 4.Se
gerarmosum streamcomomesmoconteúdo,sóquevindodeum HashSet,o
resultadofinalpodeser 3, 4, 2.Aoexecutaremparaleloo map,afasedefazer
ojoindosresultadosserábemmaissimplespornão necessitargarantiramesma
ordemdeentrada!
V o c êpoderelaxararestriçãodeordemdeum Stream ordered invocando
seu método unordered
U moutroobstáculoparaaperformancedo Streamparaleloéocoletorde
agrupamento. O Collectors.groupingBygaranteaordemdeaparição dos
elementosaoagrupá-los,oquepodesercustosonafasedefazerjoin. Utilizar
Collectors.groupingByConcurrentnão garanteessaordem,utilizandoum
únicomapaconcorrentecomo ConcurrentHashMap,masaperformancefinal
serámelhor.
Esetivéssemosefeitoscolaterais?
Osstreamsparalelossãoincrivelmentepoderosos,masnãohámágica:continu-
amosaterproblemassehouveroperações comefeitoscolateraisemestadocompar-
tilhado.
Imagineumaoutraformadesomarde1a1bilhão. Emvezdeusaro sum
do LongStream,vamoscriaratributo totalparaarmazenaroresultado. Pelo
forEachrealizamosasomanesseatributoemcomum.Repare:
class UnsafeParallelStreamUsage {
private static long total = 0;
public static void main (String... args) {
LongStream.range(0, 1_000_000_000)
.parallel()
80

## Página 93

CasadoCódigo Capítulo9. Mapeando,particionando,agrupandoeparalelizando
.filter(x -> x % 2 == 0)
.forEach(n -> total += n);
System.out.println(total);
}
}
Sevocêpossuirmaisdeumcore,cadavezquevocêrodaressecódigoobterá
provavelmenteumresultadodiferente!Ousoconcorrentedeumavariávelcompar-
tilhadapossibilitaointerleavingdeoperações deformaindesejada.Claro,vocêpode
utilizaro synchronizeddentrodoblocodolambdapararesolverisso,masper-
dendomuitaperformance.Estadocompartilhadoentrethreadscontinuasendoum
problema.
Parasabermais:Spliterators
AbasedotrabalhodetodoStreamparaleloéo Spliterator. Eleécomo
um Iterator,sóquemuitasvezespodeserfacilmentequebradoemspliterators
menores,paraquecadathreaddisponívelconsumaumpedaçodoseustream.
A interface Iterable agora também define um método default
spliterator(). Tudoque vimos de paralelização são abstrações que utili-
zam Spliteratorspordebaixodospanos,juntocomaAPIdeFork/Join.Caso
vocêvácriarumaoperaçãocomplexaparalela,éesseocaminhoquedeveseguir.
81

## Página 95

Capítulo10
ChegadeCalendar!N o v aAPIde
datas
TrabalharcomdatasemJavasemprefoiumtantocomplicado.Existemmuitascríti-
casàsclasses Datee Calendar:sãomutáveis,possuemváriaslimitações, decisões
dedesignestranhas,algunsbugsconhecidosedificuldadedesetrabalharcomelas.
U m agrandeintroduçãodoJava8foiopacote java.time,quenostrouxeuma
novaAPIdedatas!
10.1 A j a v a.time vem d oJodaTime
HámuitotempoexisteodesejodeumaAPIdedatasmelhor,baseadanoprojeto
Joda-Time.Essaafirmaçãofoiumadasmotivações usadasnapropostadessanova
feature.
OJoda-Timeéumapoderosabibliotecaopensourcebastanteconhecidaeutili-
zadanomercado,quetrabalhacomtempo,datasecronologia:

## Página 96

10.2.Trabalhandocomdatasdeformafluente CasadoCódigo
http://www.joda.org/joda-time/
Baseadanesseprojeto,anovaAPIdedataspossuimétodosmaisintuitivos,seu
códigoficoumuitomaisinteressanteefluente.V o c êpodeconhecermaisdaJSR310,
quecriouessaAPI,aqui:
https://jcp.org/en/jsr/detail?id=310.
ElafoiespecificadaporStevenColebourneeMichaelNascimento,doisnomes
bemconhecidosnacomunidade,sendoesteúltimoumbrasileiro.
10.2 Trabalhando co m d a t a sde forma fluente
Aplicarumatransformaçãoemum Calendaréumprocessomuitoverboso,como
porexemploparacriarumadatacomummêsapartirdadataatual.Repare:
Calendar mesQueVem = Calendar.getInstance();
mesQueVem.add(Calendar.MONTH, 1);
ComanovaAPIdedataspodemosfazeressamesmaoperaçãodeumaforma
maismoderna,utilizandosuainterfacefluente:
LocalDate mesQueVem = LocalDate.now().plusMonths(1);
Comoamaiorpartedeseusmétodosnãopossibilitaoretornodeparâmetros
nulos,podemosencadearsuaschamadasdeformafluentesemapreocupação de
receberum NullPointerException!
Damesmaformaquefizemosparaadicionaromês,podemosutilizarosmé-
todos plusDays, plusYearsemdiantedeacordocomnossanecessidade.Ede
formaigualmentesimples,conseguimosdecrementarosvaloresutilizandoosmé-
todos minuspresentesnessesnovosmodelos.Parasubtrairumano,porexemplo,
faríamos:
LocalDate anoPassado = LocalDate.now().minusYears(1);
U mpontoimportanteéqueaclasse LocalDaterepresentaumadatasemhorá-
rionemtimezone,porexemplo 25-01-2014.Seasinformações dehorárioforem
importantes,usamosaclasse LocalDateTimedeformabemparecida:
LocalDateTime agora = LocalDateTime.now();
System.out.println(agora);
84

## Página 97

CasadoCódigo Capítulo10.ChegadeCalendar!NovaAPIdedatas
U mexemplodesaídadessecódigoseria 2014-02-19 T17:49:19.587.
Háaindao LocalTimepararepresentarapenasashoras:
LocalTime agora = LocalTime.now();
Nestecaso,asaídaseriaalgocomo 17:49:19.587.
U m aoutraformadecriaruma LocalDateTimecomhorárioespecíficoéuti-
lizandoométodoatTimedaclasse LocalDate,repare:
LocalDateTime hojeAoMeioDia = LocalDate.now().atTime(12,0);
Assimcomofizemoscomessemétodo atTime,semprepodemosutilizaros
métodoatparacombinarosdiferentesmodelos.Observecomoficasimplesunir
umaclasse LocalDatecomum LocalTime:
LocalTime agora = LocalTime.now();
LocalDate hoje = LocalDate.now();
LocalDateTime dataEhora = hoje.atTime(agora);
T a m b é mpodemos,apartirdesse LocalDateTime,chamarométodoatZone
paraconstruirum ZonedDateTime,queéomodeloutilizadopararepresentaruma
datacomhoraetimezone.
ZonedDateTime dataComHoraETimezone =
dataEhora.atZone(ZoneId.of("America/Sao_Paulo"));
Emalgunsmomentoséimportantetrabalharcomotimezone,masoidealé
utilizá-loapenasquandorealmentefornecessário.Aprópriadocumentação pede
cuidadocomousodessainformação,poismuitasvezesnãoseránecessárioeusá-la
podecausarproblemas,comoparaguardaroaniversáriodeumusuário.
Paraconverteresses objetospara outrasmedidas de tempopodemos utili-
zarosmétodos to, comoéocasodo toLocalDateTimepresentenaclasse
ZonedDateTime:
LocalDateTime semTimeZone = dataComHoraETimezone.toLocalDateTime();
O mesmo pode ser feito com o método toLocalDate da classe
LocalDateTime,entrediversosoutrosmétodosparaconversão.
Alémdisso,asclassesdessanovaAPIcontamcomométodoestáticoof,queé
umfactorymethodparaconstruçãodesuasnovasinstâncias:
85

## Página 98

10.2.Trabalhandocomdatasdeformafluente CasadoCódigo
LocalDate date = LocalDate.of(2014, 12, 25);
LocalDateTime dateTime = LocalDateTime.of(2014, 12, 25, 10, 30);
E claro, émuitocomumprecisarmosinstanciaruma dataa partir de uma
String.Paraisso,podemosutilizarométodoparsequeserámelhordetalhado
adiante.
Reparequetodasessasinvocações nãosópodemcomodevemserencadeadas
porumbommotivo:omodelodo java.timeéimutável!Cadaoperaçãodevolve
umnovovalor,nuncaalterandoovalorinternodoshorários,dataseintervalosuti-
lizadosnaoperação. Issosimplificamuitacoisa,nãoapenasparatrabalharconcor-
rentemente.
Deformasimilaraos setters,osnovosmodelosimutáveispossuemosméto-
dos withsparafacilitarainserçãodesuasinformações. Paramodificaroanode
um LocalDate,porexemplo,poderíamosutilizarométodowithYear.Repare:
LocalDate dataDoPassado = LocalDate.now().withYear(1988);
Masepararecuperaressasinformações? Podemosutilizarseusmétodosgets,
deacordocomovalorqueestamosprocurando. Porexemplo,o getYearpara
saberoano,ou getMonthparaomês,assimpordiante.
LocalDate dataDoPassado = LocalDate.now().withYear(1988);
System.out.println(dataDoPassado.getYear());
Nestecaso,asaídaserá1988,quefoiovaloradicionadopelométodowithYear.
Issosimplificaumpouconossocódigo. Emum Calendar,porexemplo,te-
ríamosqueutilizarométodogetpassandoaconstante Calendar.YEARcomo
argumento.
Existemtambémoutroscomportamentosessencias,comosabersealgumame-
didadetempoaconteceantes,depoisouaomesmotempoqueoutra. Paraesses
casos,utilizamososmétodosis:
LocalDate hoje = LocalDate.now();
LocalDate amanha = LocalDate.now().plusDays(1);
System.out.println(hoje.isBefore(amanha));
System.out.println(hoje.isAfter(amanha));
System.out.println(hoje.isEqual(amanha));
86

## Página 99

CasadoCódigo Capítulo10.ChegadeCalendar!NovaAPIdedatas
Nesteexemplo,apenaso isBeforevairetornar true.
Háainda os casos em que queremos comparar datas iguais, porémem
timezonesdiferentes.Utilizarométodoequals,nessecaso,nãocausariaoefeito
esperado—claro,afinalasobrescritadessemétodonaclasse ZonedDateTimees-
peraqueo offsetentreasdatassejaomesmo:
@Override
public boolean equals(Object obj) {
if (this == obj) {
return true;
}
if (obj instanceof ZonedDateTime) {
ZonedDateTime other = (ZonedDateTime) obj;
return dateTime.equals(other.dateTime) &&
offset.equals(other.offset) &&
zone.equals(other.zone);
}
return false;
}
ParaestescasospodemosedevemosutilizarométodoisEqualexatamente
comofizemoscomo LocalDate.Repare:
ZonedDateTime tokyo = ZonedDateTime
.of(2011, 5, 2, 10, 30, 0, 0, ZoneId.of("Asia/Tokyo"));
ZonedDateTime saoPaulo = ZonedDateTime
.of(2011, 5, 2, 10, 30, 0, 0, ZoneId.of("America/Sao_Paulo"));
System.out.println(tokyo.isEqual(saoPaulo));
Nãomuitodiferentedoquepodemosesperar,oresultadoaindaseráfalse.
A p e s a rdasemelhançaentreasdatas,elasestãoemtimezonesdiferentes,portanto
nãosãoiguais.ParaqueoresultadodométodoisEqualdeum ZonedDateTime
seja true,precisamosacertaradiferençadetempoentreasduasdatas.U m aforma
defazerissoseriaadicionaras12horasdediferençanainstânciade tokyo,repare:
ZonedDateTime tokyo = ZonedDateTime
.of(2011, 5, 2, 10, 30, 0, 0, ZoneId.of("Asia/Tokyo"));
ZonedDateTime saoPaulo = ZonedDateTime
87

## Página 100

10.3.Enumsnolugardeconstantes CasadoCódigo
.of(2011, 5, 2, 10, 30, 0, 0, ZoneId.of("America/Sao_Paulo"));
tokyo = tokyo.plusHours(12);
System.out.println(tokyo.isEqual(saoPaulo));
Agorasim,aoexecutarométodoasaídaserátrue.
AnovaAPIpossuidiversosoutrosmodelosquefacilitambastantenossotra-
balho com data e tempo, como por exemploas classes MonthDay, Year e
YearMonth.
Paraobterodiadomêsatual,porexemplo,poderíamosutilizarométodo
getDayOfMonthdeumainstânciadaclasse MonthDay.Repare:
System.out.println("hoje é dia: "+ MonthDay.now().getDayOfMonth());
V o c êpodepegaro YearMonthdeumadeterminadadata.
YearMonth ym = YearMonth.from(data);
System.out.println(ym.getMonth() + " " + ym.getYear());
Avantagemdetrabalharapenascomanoemês,porexemplo,époderagrupar
dadosdeumaformamaisdireta. Como Calendar,precisaríamosutilizaruma
datacompletaeignorardiaehora,porexemplo.Soluções incompletas.
10.3 Enums no lugar de constantes
EssanovaAPIdedatasfavoreceousodeEnumsnolugardasfamosasconstantes
do Calendar. Pararepresentarummês,porexemplo,podemosutilizaroenum
Month. Cadavalordesseenumtemumvalorinteiroqueorepresentaseguindoo
intervalode1(Janeiro)a12(Dezembro).V o c ênãoprecisa,mastrabalharcomesses
enumséumaboaprática,afinalseucódigoficamuitomaislegível:
System.out.println(LocalDate.of(2014, 12, 25));
System.out.println(LocalDate.of(2014, Month.DECEMBER, 25));
Nosdoiscasos,ovalordesaídaé25/12/2014.
Outravantagemdeutilizarosenumssãoseusdiversosmétodosauxiliares.Note
comoésimplesconsultaroprimeirodiadotrimestrededeterminadomês,ouentão
incrementar/decrementarmeses:
88

## Página 101

CasadoCódigo Capítulo10.ChegadeCalendar!NovaAPIdedatas
System.out.println(Month.DECEMBER.firstMonthOfQuarter());
System.out.println(Month.DECEMBER.plus(2));
System.out.println(Month.DECEMBER.minus(1));
Oresultadodessecódigoserá:
OCTOBER
FEBRUARY
NOVEMBER
Paraimprimiro nomede um mêsformatado, podemos utilizar o método
getDisplayNamefornecendooestilodeformatação (completo,resumido,entre
outros)etambémo Locale:
Locale pt = new Locale("pt");
System.out.println(Month.DECEMBER
.getDisplayName(TextStyle.FULL, pt));
System.out.println(Month.DECEMBER
.getDisplayName(TextStyle.SHORT, pt));
Repareque,comoestamosutilizando TextStyle.FULLnoprimeiroexemplo
e TextStyle.SHORTnoseguinte,teremoscomoresultado:
Dezembro
Dez
Outroenumintroduzidono java.timefoio DayOfWeek. Comele,pode-
mosrepresentarfacilmenteumdiadasemana,semutilizarconstantesounúmeros
mágicos!
10.4 Formatando co m a nov aAPI de d a t a s
Aformataçãodedatastambémrecebeumelhorias.Formatarum LocalDateTime,
porexemplo,éumprocessobemsimples!Tudoquevocêprecisafazeréchamaro
métodoformatpassandoum DateTimeFormattercomoparâmetro.
Paraformataremhoras,porexemplo,podemosfazeralgocomo:
LocalDateTime agora = LocalDateTime.now();
String resultado = agora.format(DateTimeFormatter.ISO_LOCAL_TIME);
89

## Página 102

10.5.Datasinválidas CasadoCódigo
U mexemploderesultadoseria 01:15:45,ouseja,opatternéhh:mm:ss.
Note que usamos um DateTimeFormatter predefinido, o
ISO_LOCAL_TIME. Assim como ele existem diversos outros que vocêpode
vernojavadocdo DateTimeFormatter.
Mascomocriarum DateTimeFormattercomumnovopadrão? U m adas
formaséusandoométodoofPattern,querecebeuma Stringcomoparâmetro:
LocalDateTime agora = LocalDateTime.now();
agora.format(DateTimeFormatter.ofPattern("dd/MM/yyyy"));
O resultado do método format seria, por exemplo, 06/02/2014. T a m -
bémexiste uma sobrecarga desse métodoque, alémdo pattern, recebe um
java.util.Locale.
Deformaparecida,podemostransformaruma Stringemalgumarepresen-
taçãodedataoutempoválida,eparaissoutilizamosométodoparse!Podemos,
porexemplo,retornaronossoresultadoanterioremum LocalDateutilizandoo
mesmoformatador:
LocalDateTime agora = LocalDateTime.now();
DateTimeFormatter formatador = DateTimeFormatter.ofPattern("dd/MM/yyyy");
String resultado = agora.format(formatador);
LocalDate agoraEmData = LocalDate.parse(resultado, formatador);
Reparequefizemosoparsedesseresultadoemum LocalDate,enão em
um LocalDateTime, que éo tipo da data inicial. Não poderíamosretor-
narum LocalDateTime, afinalquandoformatamosemdata(coma padrão
dd/MM/yyyy),perdemosasinformações detempo! Essatentativaresultariaem
uma DateTimeParseException!
10.5 Da t a sinv álidas
Aotrabalharcom Calendar,algumavezvocêjápodetersesurpreendidoaoexe-
cutarumcódigocomoeste:
Calendar instante = Calendar.getInstance();
instante.set(2014, Calendar.FEBRUARY, 30);
SimpleDateFormat dateFormat = new SimpleDateFormat("dd/MM/yy");
System.out.println(dateFormat.format(instante.getTime()));
90

## Página 103

CasadoCódigo Capítulo10.ChegadeCalendar!NovaAPIdedatas
Levandoemconsideraçãoquefevereirodesteanosóvaiatéodia28,qualserá
oresultado? U m aexception? Essepodeseroresultadoesperado,afinalestamos
passandoumargumentoinválido!
Mas,naverdade,oresultadoserá:02/03/14.Issomesmo,o Calendarajus-
touomêsedia,semdarnenhumfeedbackdesseerroqueprovavelmentepassaria
despercebido.
Nemsempreissoéoqueesperamosaotentarcriarumadatacomvalorinválido.
Muitodiferentedessecomportamento,anovaAPIdedatasvailançaruma
DateTimeExceptionemcasoscomoesse.Repare:
LocalDate.of(2014, Month.FEBRUARY, 30);
O resultado será: java.time.DateTimeException: Invalid date
'FEBRUARY 30'.
Omesmoaconteceráseeutentarcriarum LocalDateTimecomumhorário
inválido:
LocalDateTime horaInvalida = LocalDate.now().atTime(25, 0);
Nestecaso,aexceptionsserá:java.time.DateTimeException: Invalid
value for HourOfDay (valid values 0 - 23): 25.
AprópriaAPIdoJoda-timedeixoupassarumproblemaparecidoaocriara
classe DateMidnight.NadocumentaçãodométodotoDateMidnightdaclasse
LocalDate,vocêvaiencontraraseguintenota:
“Desdeaversão1.5,recomendamosquevocêeviteo DateMidnightepassea
utilizarométodotoDateTimeAtStartOfDayporcausadaexceçãoqueseráde-
talhadaaseguir.Essemétodovailançarumaexceçãoseohoráriodeverãopadrão
começaràmeianoiteeesse LocalDaterepresenteessehoráriodatroca.Oproblema
équenãoexistemeianoitenessadatae,assim,umaexceçãoélançada” .
Ouseja,essemétodoéumtantoperigoso,poissemprelançaumaexceçãono
diaemquecomeçaohoráriodeverão.OpróprioStephenColebournedisseemseu
blogquenãoexisteumaboarazãoparaalgumdiautilizaraclasse DateMidnight.
Eclaro,essaclassenãoestápresentenanovaAPIdedatas.
10.6 Duração ePeríodo
Semprefoiproblemáticotrabalharcomadiferençadealgumamedidadetempoem
Java.Porexemplo,comocalcularadiferençadediasentredois Calendars?V o c ê
possivelmentejápassouporisso:
91

## Página 104

10.6.DuraçãoePeríodo CasadoCódigo
Calendar agora = Calendar.getInstance();
Calendar outraData = Calendar.getInstance();
outraData.set(1988, Calendar.JANUARY, 25);
long diferenca = agora.getTimeInMillis() - outraData.getTimeInMillis();
long milissegundosDeUmDia = 1000 * 60 * 60 * 24;
long dias = diferenca / milissegundosDeUmDia;
Resolvemosoproblema,claro,massabemosquetrabalharcomadiferençade
milissegundospodenãoseroideal.Hátambémalgunscasosparticularesquenão
sãocobertosnessecaso.Eacadanovanecessidade,precisaríamoscriarumcódigo
igualmenteverbosoedifícildemanter.
Agorapodemosfazeressamesmaoperaçãodeformamuitomaissimples,utili-
zandooenum ChronoUnitdanovaapi:
LocalDate agora = LocalDate.now();
LocalDate outraData = LocalDate.of(1989, Month.JANUARY, 25);
long dias = ChronoUnit.DAYS.between(outraData, agora);
Esseenumestápresentenopacote java.time.temporalepossuiumare-
presentação paracadaumadasdiferentesmedidasdetempoedata. Alémdisso,
possuiváriosmétodosparafacilitarocalculodediferençaentreseusvaloreseque
nosauxiliamaextrairinformações úteis,comoéocasodo between.
Masesetambémquisermossaberadiferençadeanosemesesentreessasduas
datas?Poderíamosutilizaro ChronoUnit.YEARSe ChronoUnit.MONTHSpara
obteressasinformações, maselevaicalcularcadaumadasmedidasdeformasepa-
rada.Repare:
long dias = ChronoUnit.DAYS.between(outraData, agora);
long meses = ChronoUnit.MONTHS.between(outraData, agora);
long anos = ChronoUnit.YEARS.between(outraData, agora);
System.out.printf("%s dias, %s meses e %s anos", dias, meses, anos);
Nestecaso,oresultadoseráalgocomo:9147dias,300mesese25anos.
U m aformadeconseguiroresultadoqueesperamos:osdias,meseseanosentre
duasdatas,éutilizandoomodelo Period. EssaclassedaAPItambémpossuio
métodobetween,querecebeduasinstânciasde LocalDate:
92

## Página 105

CasadoCódigo Capítulo10.ChegadeCalendar!NovaAPIdedatas
LocalDate agora = LocalDate.now();
LocalDate outraData = LocalDate.of(1989, Month.JANUARY, 25);
Period periodo = Period.between(outraData, agora);
System.out.printf("%s dias, %s meses e %s anos",
periodo.getDays(), periodo.getMonths(), periodo.getYears());
Notequeagoraoresultadoserá:16dias,0mesese25anos.
Aclasse Periodtemumasériedemétodosqueauxiliamnasdiversassituações
queenfrentamosaotrabalharcomdatas. Porexemplo,aocalcularumadiferença
entredatas,écomumanecessidadedelidarmoscomvaloresnegativos.Observeo
queacontecesealterarmosoanoda outraDatapara2015:
LocalDate agora = LocalDate.now();
LocalDate outraData = LocalDate.of(2015, Month.JANUARY, 25);
Period periodo = Period.between(outraData, agora);
System.out.printf("%s dias, %s meses e %s anos",
periodo.getDays(), periodo.getMonths(), periodo.getYears());
Asaídaseráalgocomo:-15dias,-11mesese0anos.
Essapodeserasaídaesperada,mascasonão seja,podemosfacilmenteper-
guntarao Periodseeleéumperíododevaloresnegativosinvocandoométodo
isNegative.Casoseja,poderíamosnegarseusvalorescomométodonegated,
repare:
Period periodo = Period.between(outraData, agora);
if (periodo.isNegative()) {
periodo = periodo.negated();
}
System.out.printf("%s dias, %s meses e %s anos",
periodo.getDays(), periodo.getMonths(), periodo.getYears());
Agoraasaídateráseusvaloresinvertidos:15dias,11mesese0anos.
Existem diversasoutrasformasde se criar um Period, alémdo método
between. U m adelaséutilizandoométodo of(years, months, days)de
formafluente:
Period periodo = Period.of(2, 10, 5);
93

## Página 106

10.7.DiferençasparaoJodaTime CasadoCódigo
T a m b é mpodemoscriarumperíodocomapenasdias,mesesouanosutilizando
osmétodos:ofDays, ofMonthsou ofYears.
Mascomocriarumperíododehoras,minutosousegundos? Arespostaé:
não criamos. Nestecaso,estamosinteressadosemoutramedidadetempo,queé
a Duration.Enquantoum Periodconsideraasmedidasdedata(dias,mesese
anos),a Durationconsideraasmedidasdetempo(horas,minutos,segundosetc.).
SuaAPIémuitoparecida,observe:
LocalDateTime agora = LocalDateTime.now();
LocalDateTime daquiAUmaHora = LocalDateTime.now().plusHours(1);
Duration duration = Duration.between(agora, daquiAUmaHora);
if (duration.isNegative()) {
duration = duration.negated();
}
System.out.printf("%s horas, %s minutos e %s segundos",
duration.toHours(), duration.toMinutes(), duration.getSeconds());
Repareque,comoagoraestamostrabalhandocomtempo,utilizamosaclasse
LocalDateTime.
10.7 Diferenças para oJodaTime
ÉimportantelembrarqueanovaAPIdedatas(JSR-310)ébaseadanoJoda-Time,
masquenãoéumacópia.Existemalgumasdiferençasdedesignqueforamcuida-
dosamenteapontadaspeloStephenColebourneemseublog,noartigoWhyJSR-310
isn’tJoda-Time:
http://blog.joda.org/2009/11/why-jsr-310-isn-joda-time_4941.html.
AsprincipaismudançasforaminspiradaspelasfalhasdedesigndoJoda-Time,
comoéocasodasreferênciasnulas. NoJoda-Timenão sóerapossívelfornecer
valoresnulosparagrandemaioriadeseusmétodos,comoissotinhaumsignificado
pracadamodelo.Porexemplo,paraasrepresentações dedataetempoovalor null
significava 1970-01-01T00:00Z.Paraasclasses Duratione Period, null
significavazero.
Essaéumaestratégiadedesignumtantoinesperada,equepodefacilmentecau-
sarbugsemnossasaplicações.
Háaindaocasodaclasse DateTimequeimplementa ReadableInstant,
sendoquecomoumainterpretaçãohumanadetemponãodeveria.Nofim,elaacaba
94

## Página 107

CasadoCódigo Capítulo10.ChegadeCalendar!NovaAPIdedatas
sendoumaprojeçãodeumalinhadotempodemáquinaemumalinhadotempo
humana,ficandolimitadaàprecisãodemilissegundos.
95

## Página 109

Capítulo11
U mmodelodepagamentoscom
J a v a8
V a m o samaisumexemplosucintoparapraticarosconceitoseprincipaispontosda
APIvistosatéaqui.Relembrandoquevocêpodeacessartodoocódigo-fontedolivro
aqui:
https://github.com/peas/java8
ParafixaranovaAPIesintaxe,pormaisquevocêjádomineoJava,éimportante
praticar.Sepossível,recrieocódigovocêmesmo,semcopiarecolar.
11.1 Uma l o j ade digitalgoodies
Venderbensdigitaiséodiaadiadanossaloja.
Vendemosdownloaddemúsicas,vídeoseimagensparaseremutilizadosem
campanhaspublicitárias.Cadaumdessesprodutospossuemumnome,umpreçoe
ocaminhodoarquivo:

## Página 110

11.1.Umalojadedigitalgoodies CasadoCódigo
class Product {
private String name;
private Path file;
private BigDecimal price;
public Product(String name, Path file, BigDecimal price) {
this.name = name;
this.file = file;
this.price = price;
}
public String getName() {
return this.name;
}
public Path getFile() {
return this.file;
}
public BigDecimal getPrice() {
return this.price;
}
public String toString() {
return this.name;
}
}
Nossoe-commercecontacomdiversosclientes,dosquaisparanósimportaape-
nasonome:
class Customer {
private String name;
public Customer(String name) {
this.name = name;
}
public String getName() {
return this.name;
}
98

## Página 111

CasadoCódigo Capítulo11.UmmodelodepagamentoscomJava8
public String toString() {
return this.name;
}
}
Equandoousuáriorealizaumacompranosistema,um Paymentéutilizado
pararepresentá-la,armazenandoumalistadeprodutoscomprados,omomentoda
compraequemarealizou:
class Payment {
private List<Product> products;
private LocalDateTime date;
private Customer customer;
public Payment(List<Product> products,
LocalDateTime date,
Customer customer) {
this.products =
Collections.unmodifiableList(products);
this.date = date;
this.customer = customer;
}
public List<Product> getProducts() {
return this.products;
}
public LocalDateTime getDate() {
return this.date;
}
public Customer getCustomer() {
return this.customer;
}
public String toString() {
return "[Payment: " +
date.format(DateTimeFormatter.ofPattern("dd/MM/yyyy")) +
" " + customer + " " + products + "]";
}
}
99

## Página 112

11.1.Umalojadedigitalgoodies CasadoCódigo
UtilizamosalgumasdasnovidadesdoJava8,comoo java.timeparaarmaze-
naradataeformatá-la.
Sim,poderíamostermodeladoasclassesdemiloutrasmaneiras. Emvezde
Pathpoderíamoster URLseconsiderarmosqueosarquivosestão nocloud. Po-
deríamosterdeixadoorelacionamentobidirecional,como Customerpossuindo
tambémum List<Payment>. Aescolhaaquiéosuficienteparaexercitarmoso
nossoaprendizadoeumamodelagemmelhorficasemdúvidaacargodousodo
TDDedeconhecerbemodomínio.
V a m o spopularumpoucoanossabasedetestes,criandoquatroclientes:
Customer paulo = new Customer("Paulo Silveira");
Customer rodrigo = new Customer("Rodrigo Turini");
Customer guilherme = new Customer("Guilherme Silveira");
Customer adriano = new Customer("Adriano Almeida");
Efazemosomesmocomosnossosprodutos,criandoseisdeles:
Product bach = new Product("Bach Completo",
Paths.get("/music/bach.mp3"), new BigDecimal(100));
Product poderosas = new Product("Poderosas Anita",
Paths.get("/music/poderosas.mp3"), new BigDecimal(90));
Product bandeira = new Product("Bandeira Brasil",
Paths.get("/images/brasil.jpg"), new BigDecimal(50));
Product beauty = new Product("Beleza Americana",
Paths.get("beauty.mov"), new BigDecimal(150));
Product vingadores = new Product("Os Vingadores",
Paths.get("/movies/vingadores.mov"), new BigDecimal(200));
Product amelie = new Product("Amelie Poulain",
Paths.get("/movies/amelie.mov"), new BigDecimal(100));
Agoraprecisamosdealgunspagamentos,relacionandoclientescomprodutos.
ReparequePaulofezpagamentosduasvezes.Porumaquestãodelegibilidade,uti-
lizamosoimportestáticode Arrays.asList:
LocalDateTime today = LocalDateTime.now();
LocalDateTime yesterday = today.minusDays(1);
LocalDateTime lastMonth = today.minusMonths(1);
Payment payment1 =
new Payment(asList(bach, poderosas), today, paulo);
Payment payment2 =
100

## Página 113

CasadoCódigo Capítulo11.UmmodelodepagamentoscomJava8
new Payment(asList(bach, bandeira, amelie), yesterday, rodrigo);
Payment payment3 =
new Payment(asList(beauty, vingadores, bach), today, adriano);
Payment payment4 =
new Payment(asList(bach, poderosas, amelie), lastMonth, guilherme);
Payment payment5 =
new Payment(asList(beauty, amelie), yesterday, paulo);
List<Payment> payments = asList(payment1, payment2,
payment3, payment4, payment5);
11.2 Ordenando nossos pagamentos
Oprimeirodesafioéfácil.Ordenarospagamentospordataeimprimi-los,para
quefiqueclaraanossabasededados.Paraisso,podemosencadearo sortedeo
forEachdo streamdessacoleção:
payments.stream()
.sorted(Comparator.comparing(Payment::getDate))
.forEach(System.out::println);
Oresultadonosajudaaenxergarasrespostasdospróximosdesafios:
[Payment: 16/02/2014 Guilherme Silveira
[Bach Completo, Poderosas Anita, Amelie Poulain]]
[Payment: 15/03/2014 Rodrigo Turini
[Bach Completo, Bandeira Brasil, Amelie Poulain]]
[Payment: 15/03/2014 Paulo Silveira
[Beleza Americana, Amelie Poulain]]
[Payment: 16/03/2014 Paulo Silveira
[Bach Completo, Poderosas Anita]]
[Payment: 16/03/2014 Adriano Almeida
[Beleza Americana, Os Vingadores, Bach Completo]]
11.3 ReduzindoBigDecimal em somas
V a m o scalcularovalortotaldopagamento payment1utilizandoaAPIdeStream
e lambdas. Háum problema. Se preço fosse um int, poderíamosusar o
mapToDoubleeinvocaro sumdo DoubleStreamresultante.Nãoéocaso.Tere-
mosum Stream<BigDecimal>eelenãopossuium sum.
101

## Página 114

11.3.ReduzindoBigDecimalemsomas CasadoCódigo
Nesse caso precisaremos fazer a redução na mão, realizando a soma de
BigDecimal.Podemosusaro (total, price) -> total.add(price),mas
ficaaindamaisfácilusandoummethodreference:
payment1.getProducts().stream()
.map(Product::getPrice)
.reduce(BigDecimal::add)
.ifPresent(System.out::println);
Arespostaé190.
O ifPresentédo Optional<BigDecimal>retornadopelo reduce. Se
invocarmoso reducequerecebeoargumentodeinicialização,teríamoscomore-
tornoum BigDecimaldiretamente:
BigDecimal total =
payment1.getProducts().stream()
.map(Product::getPrice)
.reduce(BigDecimal.ZERO, BigDecimal::add);
U m asimplesoperaçãocomoasomade BigDecimalapresentaváriassoluções.
Namaioriadasvezes,essassoluções sãoequivalentes,poisaestratégiadeexecução
dopipelineconsegueserbastanteeficienteparaevitarqualqueroperaçãorepetida.
CertamentepoderíamosterummétodogetTotalAmountem Product,caso
julgássemosnecessário.
E se precisarmos somar todos os valores de todos os pagamentosda lista
payments? Novamentenosdeparamoscomdiversasopções. Podemosusaro
mesmocódigoanterior,usandoo mapde payments:
Stream<BigDecimal> pricesStream =
payments.stream()
.map(p -> p.getProducts().stream()
.map(Product::getPrice)
.reduce(BigDecimal.ZERO, BigDecimal::add));
Reparequeocódigodentrodoprimeiro mapéomesmoqueodocódigoque
usamosparacalcularasomadosvaloresdo payment1.Comesse map,temoscomo
resultadoum Stream<BigDecimal>.Precisamosrepetiraoperaçãode reduce
parasomaressesvaloresintermediários.Istoé,realizamosasomadepreçosdos
produtosdecadapagamento,agoravamossomarcadaumdessessubtotais:
102

## Página 115

CasadoCódigo Capítulo11.UmmodelodepagamentoscomJava8
BigDecimal total =
payments.stream()
.map(p -> p.getProducts().stream()
.map(Product::getPrice)
.reduce(BigDecimal.ZERO, BigDecimal::add))
.reduce(BigDecimal.ZERO, BigDecimal::add);
Ocódigoestáumpoucorepetitivo.Emvezderealizarmosoperaçõesdesomaem
momentosdistintos,podemoscriarumúnicoStream<BigDecimal>comosva-
loresdetodososprodutosdetodospagamentos.Conseguimosesse Streamusando
o flatMap:
Stream<BigDecimal> priceOfEachProduct =
payments.stream()
.flatMap(p -> p.getProducts().stream().map(Product::getPrice));
Seestádifícillerestecódigo,leia-opassoapasso.Oimportanteéenxergaressa
função:
Function<Payment, Stream<BigDecimal>> mapper =
p -> p.getProducts().stream().map(Product::getPrice);
Essafunçãomapeiaum Paymentparao Streamquepasseiaportodososseus
produtos.Eéporesseexatomotivoqueprecisamosinvocardepoiso flatMape
nãoo map,casocontrárioobteríamosum Stream<Stream<BigDecimal>>.
Parasomartodoesse Stream<BigDecimal>,bastarealizarmosaoperaçãode
reducequeconhecemos:
BigDecimal totalFlat =
payments.stream()
.flatMap(p -> p.getProducts().stream().map(Product::getPrice))
.reduce(BigDecimal.ZERO, BigDecimal::add);
11.4 Produtos mais vendidos
Queremossabernossoscampeões devendas.Há,maisumavez,diversasmaneiras
derealizartaltarefa.Mapearemosnossosprodutosparaaquantidadequeelesapa-
recem.Paratal,criamosum Streamcomtodosos Productvendidos.Maisuma
vezentrao flatMap:
103

## Página 116

11.4.Produtosmaisvendidos CasadoCódigo
Stream<Product> products = payments.stream()
.map(Payment::getProducts)
.flatMap(p -> p.stream());
Emvezde p -> p.stream(),háapossibilidadedepassarolambdacomo
methodreference: List::stream:
Stream<Product> products = payments.stream()
.map(Payment::getProducts)
.flatMap(List::stream);
Semprepodemosjuntardois maps(independentedeumdelesser flat)em
umúnicomap:
Stream<Product> products = payments.stream()
.flatMap(p -> p.getProducts().stream());
Etambémnãohádiferençadeperformancesignificativa.Ficaaseucargoutilizar
oqueconsiderarmaislegível.ComoaAPIeoJava8sãomuitorecentes,boasprá-
ticasaindanãosurgiramparadizerqualdasduasabordagensémaisadequadapara
facilitaramanutenção. Pessoalmenteacreditamosqueasduassãosuficientemente
claras.
Precisamosgerarum Mapde Productpara Long.Esse Longindicaquan-
tasvezesoprodutofoivendido.Usaremoso groupingBy,agrupandotodosesses
produtospelopróprioproduto,mapeando-opelasuacontagem:
Map<Product, Long> topProducts = payments.stream()
.flatMap(p -> p.getProducts().stream())
.collect(Collectors.groupingBy(Function.identity(),
Collectors.counting()));
System.out.println(topProducts);
Podeserruimleroresultadodo System.out.println,poiso toString
donosso Mapgeraráumalinhabemcomprida.Podemospegaro entrySetdesse
mapaeimprimirlinhaalinha:
topProducts.entrySet().stream()
.forEach(System.out::println);
Certamentepoderíamosterencadeadoessachamadaao entrySetlogoapós
nosso collect,porémnãoteríamosmaisacessoao Map.
Nossoresultadoéparecidocomoseguinte:
104

## Página 117

CasadoCódigo Capítulo11.UmmodelodepagamentoscomJava8
Beleza Americana=2
Amelie Poulain=3
Bandeira Brasil=1
Bach Completo=4
Poderosas Anita=2
Os Vingadores=1
Pelovisto,Bachaindaéomaispopular.Mascomopegarapenasessaentradado
mapa?Bastapedirmosamaiorentradadomapaconsiderandoum Comparator
quecompareo valuedecadaentrada. V a l elembrarqueelaérepresentadapela
interfaceinterna Map.Entry:
topProducts.entrySet().stream()
.max(Comparator.comparing(Map.Entry::getValue))
.ifPresent(System.out::println);
O maxdevolveum Optional,porissoo ifPresent.
11.5 Valores gerados p o rproduto
Calculamosaquantidadedevendasporprodutos.Easomadovalorporproduto?
O processo émuito parecido. Em vez de agruparmos com o valor de
Collectors.counting,queremosfazeralgocomo Collectors.summing.Há
diversosmétodoscomoesseem Collectors,porémtodostrabalhamcomtipos
primitivos. Pararealizarasomaem BigDecimalteremosdedeixaro reduce
explícito:
Map<Product, BigDecimal> totalValuePerProduct = payments.stream()
.flatMap(p -> p.getProducts().stream())
.collect(Collectors.groupingBy(Function.identity(),
Collectors.reducing(BigDecimal.ZERO, Product::getPrice,
BigDecimal::add)));
Podemosusaramesmaestratégiado stream().forEach(System.out::println)
paramostraroresultado,masvamosaproveitareordenarasaídaporvalor:
totalValuePerProduct.entrySet().stream()
.sorted(Comparator.comparing(Map.Entry::getValue))
.forEach(System.out::println);
Assimobtemosoresultadodesejado:
105

## Página 118

11.6.Quaissãoosprodutosdecadacliente? CasadoCódigo
Bandeira Brasil=50
Poderosas Anita=180
Os Vingadores=200
Beleza Americana=300
Amelie Poulain=300
Bach Completo=400
11.6 Quaissão os produtos de cada cliente?
Em um primeiro momento, podemos ter, para cada Customer,
sua List<Payment>, bastando agrupar os payments com
groupingBy(Payment::getCustomer):
Map<Customer, List<Payment>> customerToPayments =
payments.stream()
.collect(Collectors.groupingBy(Payment::getCustomer));
Nãoestamosinteressadosnos paymentsdeum Customer,esimnaslistasde
Productdentrodecadaumdesses Payments.
U m aimplementaçãoinocentevaigeraruma List<List<Product>>dentro
dovalordo Map:
Map<Customer, List<List<Product>>> customerToProductsList =
payments.stream()
.collect(Collectors.groupingBy(Payment::getCustomer,
Collectors.mapping(Payment::getProducts, Collectors.toList())));
customerToProductsList.entrySet().stream()
.sorted(Comparator.comparing(e -> e.getKey().getName()))
.forEach(System.out::println);
Asaídamostraoproblemadaslistasaninhadas:
Adriano Almeida=[[Beleza Americana, Os Vingadores, Bach Completo]]
Guilherme Silveira=[[Bach Completo, Poderosas Anita, Amelie Poulain]]
Paulo Silveira=[[Bach Completo, Poderosas Anita], [Beleza Americana,
Amelie Poulain]]
Rodrigo Turini=[[Bach Completo, Bandeira Brasil, Amelie Poulain]]
Queremosessemesmoresultado,porémcomaslistasachatadasemumasó.
106

## Página 119

CasadoCódigo Capítulo11.UmmodelodepagamentoscomJava8
Háduasformas. Sim,umaenvolveo flatMapdomaparesultante. Dadoo
customerToProductsList,queremosqueo valuedecada entrysejaacha-
tado.Fazemos:
Map<Customer, List<Product>> customerToProducts2steps =
customerToProductsList.entrySet().stream()
.collect(Collectors.toMap(Map.Entry::getKey,
e -> e.getValue().stream()
.flatMap(List::stream)
.collect(Collectors.toList())));
customerToProducts2steps.entrySet().stream()
.sorted(Comparator.comparing(e -> e.getKey().getName()))
.forEach(System.out::println);
U s a m o so Collectors.toMapparacriarumnovomapanoqualachave
continuaamesma( Map.EntrygetKey) mas o valor é o resultado do
flatMap dos Liststreamdetodasaslistas.
Podemosverificaroconteúdodessemapa,obtendoomesmoresultadoanterior,
porémsemaslistasaninhadas:
Adriano Almeida=[Beleza Americana, Os Vingadores, Bach Completo]
Guilherme Silveira=[Bach Completo, Poderosas Anita, Amelie Poulain]
Paulo Silveira=[Bach Completo, Poderosas Anita, Beleza Americana,
Amelie Poulain]
Rodrigo Turini=[Bach Completo, Bandeira Brasil, Amelie Poulain]
Poderíamosterfeitotudocomumaúnicachamada.Creioquenessecasoestou-
ramosolimitedalegibilidadedousodessaAPI.Apenasparaefeitosdidáticos,veja
comoficaria:
Map<Customer, List<Product>> customerToProducts1step = payments.stream()
.collect(Collectors.groupingBy(Payment::getCustomer,
Collectors.mapping(Payment::getProducts, Collectors.toList())))
.entrySet().stream()
.collect(Collectors.toMap(Map.Entry::getKey,
e -> e.getValue().stream()
.flatMap(List::stream)
.collect(Collectors.toList())));
Difícildeseguirasequência.Certamentequebraremváriospassoséomais
indicado.
107

## Página 120

11.7.Qualénossoclientemaisespecial? CasadoCódigo
Comosempre,háoutrasformasderesolveromesmoproblema.Podemosusaro
reducingmaisumavez,poisqueremosacumularaslistasdecadaclienteagrupado.
Map<Customer, List<Product>> customerToProducts = payments.stream()
.collect(Collectors.groupingBy(Payment::getCustomer,
Collectors.reducing(Collections.emptyList(),
Payment::getProducts,
(l1, l2) -> { List<Product> l = new ArrayList<>();
l.addAll(l1);
l.addAll(l2);
return l;} )));
Tivemosdeescreveralgomuitoparecidocomoqueo Collectors.toList
devolve.Infelizmentenãoháummétodoauxiliarqueunaduas Collections,im-
pedindoasimplificaçãodoterceiroargumento,queéum BinaryOperator.Cri-
amosumcoletorquepegatodosos Payment::getProductsevaiacumulando
todooresultandoemumanova ArrayList.
Oresultadoéexatamenteomesmoquecomo flatMap.
11.7 Qu a lé nosso clientemais especial?
Qualseriaaestratégiaparaobterodesejado Map<Customer, BigDecimal>?
Seráamesmaqueadareduçãoanterior,apenasmudandoaoperação. Começare-
moscom BigDecimal.ZEROe,paracada Payment,faremosBigDecimal::add
dasomadospreçosdeseusprodutos.Poressemotivoumareduçãoaindaaparece
dentrodo reducing!
Map<Customer, BigDecimal> totalValuePerCustomer = payments.stream()
.collect(Collectors.groupingBy(Payment::getCustomer,
Collectors.reducing(BigDecimal.ZERO,
p -> p.getProducts().stream().map(Product::getPrice).reduce(
BigDecimal.ZERO, BigDecimal::add),
BigDecimal::add)));
Ocódigoestánomínimomuitoacumulado.Cremosjátermospassadodoli-
mitedalegibilidade.V a m o squebraressaredução,criandoumavariáveltemporária
responsávelpormapearum Paymentparaasomadetodosospreçosdeseuspro-
dutos:
Function<Payment, BigDecimal> paymentToTotal =
p -> p.getProducts().stream()
108

## Página 121

CasadoCódigo Capítulo11.UmmodelodepagamentoscomJava8
.map(Product::getPrice)
.reduce(BigDecimal.ZERO, BigDecimal::add);
Comisso,podemosutilizaressa Functionno reducing:
Map<Customer, BigDecimal> totalValuePerCustomer = payments.stream()
.collect(Collectors.groupingBy(Payment::getCustomer,
Collectors.reducing(BigDecimal.ZERO,
paymentToTotal,
BigDecimal::add)));
Novamente surge um forte indício de que deveria haver um método
getTotalAmount em Payment, que calculasse todo esse valor. Nesse
caso, poderíamos fazer um simples reducing(BigDecimal.ZERO,
PaymentgetTotalAmount, BigDecimaladd). Ao mesmo tempo, este
estásendoumexcelenteexercíciodemanipulaçãodecoleções erelacionamentos.
Jápodemosexibiroconteúdodessemapa:
totalValuePerCustomer.entrySet().stream()
.sorted(Comparator.comparing(Map.Entry::getValue))
.forEach(System.out::println);
Assimobtemosoresultadoesperado.
Rodrigo Turini=250
Guilherme Silveira=290
Paulo Silveira=440
Adriano Almeida=450
11.8 Relatórios co m d a t a s
É muito simples separarmos os pagamentos por data, usando um
groupingBy(Payment::getDate). Háum perigo: o LocalDateTime
vaiagruparospagamentosatépelosmilissegundos.Nãoéoquequeremos.
Podemos agrupar por LocalDate, usando um groupingBy(p ->
p.getDate().toLocalDate()),ouemumintervaloaindamaior,comoporano
emês.Paraissousamoso YearMonth:
Map<YearMonth, List<Payment>> paymentsPerMonth = payments.stream()
.collect(Collectors.groupingBy(p -> YearMonth.from(p.getDate())));
109

## Página 122

11.9.Sistemadeassinaturas CasadoCódigo
paymentsPerMonth.entrySet().stream()
.forEach(System.out::println);
Esequisermossaber,tambémpormês,quantofoifaturadonaloja?Bastaagru-
parcomomesmocritérioeusararedução queconhecemos: somandotodosos
preçosdetodososprodutosdetodospagamentos.
Map<YearMonth, BigDecimal> paymentsValuePerMonth = payments.stream()
.collect(Collectors.groupingBy(p -> YearMonth.from(p.getDate()),
Collectors.reducing(BigDecimal.ZERO,
p -> p.getProducts().stream()
.map(Product::getPrice)
.reduce(BigDecimal.ZERO,
BigDecimal::add),
BigDecimal::add)));
11.9 Sistema de assinaturas
Imaginequetambémoferecemososistemadeassinatura.Pagandoumvalormensal,
oclientetemacessoatodooconteúdodenossoe-commerce.Alémdovaloredo
cliente,uma Subscriptionprecisateradatadeinícioetalvezumadatadetérmino
deassinatura:
class Subscription {
private BigDecimal monthlyFee;
private LocalDateTime begin;
private Optional<LocalDateTime> end;
private Customer customer;
}
Reparenousodo Optional<LocalDateTime>. Ficainteressanteparaex-
pormoso getEnd,tornandoobrigatórioocuidadocomovalornuloporparteda
classequeutilizaráessainformação. Éclaroquepoderíamosterusadoumsimples
LocalDateTimecomoatributo,eogetterenveloparseuvaloremum Optional.
Teremosdoisconstrutores. U mparaassinaturasqueaindaestão ativas,outro
paraasqueseencerrarameprecisamterumadataespecíficaparatal:
public Subscription(BigDecimal monthlyFee, LocalDateTime begin,
Customer customer) {
110

## Página 123

CasadoCódigo Capítulo11.UmmodelodepagamentoscomJava8
this.monthlyFee = monthlyFee;
this.begin = begin;
this.end = Optional.empty();
this.customer = customer;
}
public Subscription(BigDecimal monthlyFee, LocalDateTime begin,
LocalDateTime end, Customer customer) {
this.monthlyFee = monthlyFee;
this.begin = begin;
this.end = Optional.of(end);
this.customer = customer;
}
Consideretambémosrespectivosgettersdecadaatributo.
Teremostrêsusuárioscomassinaturasde 99.90.Doisdelesencerraramsuas
assinaturas:
BigDecimal monthlyFee = new BigDecimal("99.90");
Subscription s1 = new Subscription(monthlyFee,
yesterday.minusMonths(5), paulo);
Subscription s2 = new Subscription(monthlyFee,
yesterday.minusMonths(8), today.minusMonths(1), rodrigo);
Subscription s3 = new Subscription(monthlyFee,
yesterday.minusMonths(5), today.minusMonths(2), adriano);
List<Subscription> subscriptions = Arrays.asList(s1, s2, s3);
Comocalcularquantosmesesforampagosatravésdaquelaassinatura? Basta
usaroqueconhecemosdaAPIde java.time.Masdependedocaso.Seaassina-
turaaindaestiverativa,calculamosointervalodetempoentre begineadatade
hoje:
long meses = ChronoUnit.MONTHS
.between(s1.getBegin(), LocalDateTime.now());
Eseaassinaturaterminou?Emvezdeenchermosnossocódigocom ifs,tira-
mosproveitodo Optional:
111

## Página 124

11.9.Sistemadeassinaturas CasadoCódigo
long meses = ChronoUnit.MONTHS
.between(s1.getBegin(), s1.getEnd().orElse(LocalDateTime.now()));
Paracalcularovalorgeradoporaquelaassinatura,bastamultiplicaressenúmero
demesespelocustomensal:
BigDecimal total = s1.getMonthlyFee()
.multiply(new BigDecimal(ChronoUnit.MONTHS
.between(s1.getBegin(),
s1.getEnd().orElse(LocalDateTime.now()))));
Destavezvamosfacilitarnossotrabalhoeadicionarumnovométodonaprópria
Subscription:
public BigDecimal getTotalPaid() {
return getMonthlyFee()
.multiply(new BigDecimal(ChronoUnit.MONTHS
.between(getBegin(),
getEnd().orElse(LocalDateTime.now()))));
}
Dadaumalistade subscriptions,ficafácilsomartodoototalpago:
BigDecimal totalPaid = subscriptions.stream()
.map(Subscription::getTotalPaid)
.reduce(BigDecimal.ZERO, BigDecimal::add);
112

## Página 125

Capítulo12
Apêndice:maisJ a v a8com
reflection,JVM,APIselimitações
12.1 No v o sdetalhes n a linguagem
Operadordiamantemelhorado
Ooperadordiamante(diamondoperator)éaquelequeevitadigitarmosdesnecessa-
riamenteemalgumassituações óbvias.Porexemplo,emvezdefazer:
List<Usuario> lista = new ArrayList<Usuario>();
Podemosfazer,apartirdoagoraantigoJava7:
List<Usuario> lista = new ArrayList<>();
Porémorecursoerabastantelimitado: basicamenteapenaspodiaserusado
juntocomadeclaraçãodavariávelreferência.Considerandoaexistênciadeumre-

## Página 126

12.1.Novosdetalhesnalinguagem CasadoCódigo
positórioquetemométodoadiciona(List<Usuario>),ocódigoaseguirfalha
noJava7:
repositorio.adiciona(new ArrayList<>());
ParacompilarnoJava7 ,vocêprecisariafazer repositorio.adiciona(new
ArrayList<Usuario>()),poisocompiladornãoconseguiainferirotipodecla-
radonaassinaturadométodo,quenestecasoéUsuario.
Se vocêconhece a API de Collections, sabe que ela possui o método
Collections.emptyList(). Podemosutilizá-lonesteexemplopararesolvero
problemasemterqueexplicitamenteinferirotipo Usuario,vistoqueocompila-
dornãofaráessainferênciaquandoutilizamosooperadordiamante.
Nossocódigoficaráassim:
repositorio.adiciona(Collections.emptyList());
Porémoseguinteerroseráexibidoaotentarcompilaressecódigo:
The method adiciona(List<Usuario>) in the type Capitulo12 is not
applicable for the arguments (List<Object>)
Issoacontecepoisocompiladorinferiuotipogenéricocomosendoum Object.
Paraqueessecódigocompileprecisaríamosfazer:
repositorio.adiciona(Collections.<Usuario>emptyList());
JánoJava8,osdoiscasosfuncionamperfeitamente,dadasasmelhoriasnainfe-
rência.
Agoraeupossoescreverecompilaroseguintecódigosemnenhumapreocupa-
ção,afinalocompiladorvaiextrairessainformaçãogenéricapeloparâmetroespe-
radonométodo.
repositorio.adiciona(new ArrayList<>());
repositorio.adiciona(Collections.emptyList());
V o c êpodelermaisarespeitodapropostademelhoriasnainferênciadostipos
aqui:
http://openjdk.java.net/jeps/101
114

## Página 127

CasadoCódigo Capítulo12.Apêndice:maisJava8comreflection,JVM,APIselimitações
Situaçõesdeambiguidade
Aindaqueainferênciadostipostenhasidobastantemelhorada,existemsitua-
ções deambiguidadeemqueprecisaremosajudarocompilador.Paraentenderesse
problemadeformapráticaconsidereaseguinteexpressãolambda:
Supplier<String> supplier = () -> "retorna uma String";
Comoainterfacefuncional Supplier<T>temapenasométodogetquenão
recebenenhumparâmetroeretornaotipogenérico,aexpressão () -> "retorna
uma String"podeterseutipoinferidosemnenhumproblema.
Masessanãoéaúnicainterfacefuncionalqueatendebemaessaexpressão,afinal
qualquerinterfacepodeterummétodoqueretornaumtipogenérico.Nósmesmos
podemoscriarinterfacescomumaestruturaparecida.
Paraessecasonemseráprecisocriarumcasodeambiguidade,poisdentroda
própriaAPIdoJavatemosainterface PrivilegedAction<T>quepossuiessa
estrutura,repare:
public interface PrivilegedAction<T> {
T run();
}
Sabendodisso,podemosdeclararamesmaexpressão () -> "retorna uma
String"comessesdoistipos!
Supplier<String> supplier = () -> "retorna uma String";
PrivilegedAction<String> p = () -> "retorna uma String";
Masissonãoseráumproblemaparaocompilador,claro,afinalessaexpressão
temseutipobemdeterminadoemsuadeclaração.
Issonemmesmoseráumproblemaquandopassarmosamesmaexpressãocomo
parâmetroparaummétodocomoesse:
private void metodo(Supplier<String> supplier) {
// faz alguma lógica e invoca supplier.get()
}
Jávimosque,aoexecutaroseguintecódigo,ocompiladoragoravaiinferiro
tipodalambdadeacordocomovaloresperadopelométodo,quenestecasoéum
Supplier.
115

## Página 128

12.1.Novosdetalhesnalinguagem CasadoCódigo
metodo(() -> "retorna uma String");
Masoqueaconteceseessemétodotiverumasobrecarga,querecebeumainter-
facefuncionalcomamesmaestrutura? Poderíamosterumaopção dessemétodo
recebendouma PrivilegedAction:
private void metodo(Supplier<String> supplier) {
// faz alguma lógica e invoca supplier.get()
}
private void metodo(PrivilegedAction<String> action) {
// faz alguma lógica e invoca action.run()
}
Tudobem,essepodenãoserumcasotãocomum,maséinteressantesaberque
essetipodeambiguidadepodeacontecer.Aoadicionaressesegundométodo,ocom-
piladornãovaiconseguirmaisinferirotipodessaexpressão:
metodo(() -> "retorna uma String");
Comoesperadoamensagemdeerroserá:
The method metodo(Supplier<String>) is ambiguous for the type Capitulo12
Nestecasoseránecessáriorecorreraocastingparaajudarnessainferência.Algo
como:
metodo((Supplier<String>) () -> "retorna uma String");
Conversõesentreinterfacesfuncionais
Outrodetalheinteressantesobreainferênciadetiposéquenãoexisteumacon-
versãoautomáticaentreinterfacesfuncionaisequivalentes.Porexemplo,considere
quetemosométodoexecutequerecebeum Supplier<String>comoparâ-
metroeapenasexibeoretornodeseumétodoget:
private void execute(Supplier<String> supplier) {
System.out.println(supplier.get());
}
U mexemplodeseuusoseriaalgocomo:
116

## Página 129

CasadoCódigo Capítulo12.Apêndice:maisJava8comreflection,JVM,APIselimitações
Supplier<String> supplier = () -> "executando um supplier";
execute(supplier);
Aoexecutá-lo,receberemosasaídaesperada:
executando um supplier
Mas e se eu definir o tipo dessa expressão como um
PrivilegedAction<String>? Paratodos os efeitosvimos que o resultado
final deveráser o mesmo, porém,ainda que estas interfaces funcionais sejam
equivalentes, não existiráuma conversão automática. O seguinte código não
compila:
PrivilegedAction<String> action = () -> "executando uma ação";
execute(action);
Issonão devefuncionar,afinalométodo execute(Supplier<String>)
não éaplicávelpara o argumento PrivilegedAction<String>. Paraque
essaconversãosejapossívelpodemosutilizarmethodreferencenessainstânciade
PrivilegedAction,assimestamosexplicitamenteindicandoaocompiladorque
desejamosessaconversão:
PrivilegedAction<String> action = () -> "executando uma ação";
execute(action::run);
Executandoocódigomodificadoreceberemosasaída:
executando uma ação
12.2 Qu a lé o tipo de u m a expressão Lambda?
T o d aexpressão lambdatemeprecisaterumtipo. Comovimosrapidamente,o
seguintetrechodecódigonãofunciona:
Object o = () -> {
System.out.println("eu sou um runnable!");
};
new Thread(o).start();
Pois Objectnão éumainterfacefuncional. Sempreprecisamosterumtipo
quesejaumainterfacefuncional,envolvidonaatribuição. Porexemplo,quando
definimosesse Runnable:
117

## Página 130

12.2.QualéotipodeumaexpressãoLambda? CasadoCódigo
Runnable r = () -> {
System.out.println("eu sou um runnable!");
};
new Thread(r).start();
Fica explicito que essa expressão lambda representa a interface funcional
Runnable,poisesteéotipoquedemosparasuavariávelr.Masequandofazemos
suadeclaraçãodeformadireta,emumúnicostatement?
new Thread(() -> {
System.out.println("eu sou um runnable?");
}).start();
Jánãoficaassimtãoclaro,nãoé?Mastudobem,sabemosqueométodocons-
trutordaclasse Threadesperareceberum Runnable,edamesmaformaocom-
piladortambémsabequedevetraduziressecódigolambdaparaum Runnable.
Ocompiladoréoresponsávelporinferirqualotipodeumaexpressãolambda,e
paraconseguirfazeressetrabalhoeleagoralevaemconsideraçãoocontextoemque
essaexpressãofoiaplicada,ouseja,infereotipodeacordocomotipoqueéesperado
pelométodoouconstrutor.Esse“tipoesperado”éconhecidocomoTargetT y p e.
Conhecerocontextofoiumpassomuitoimportanteparaocompiladorpoder
inferirotipodeumaexpressãolambda,poiscomojávimos,umamesmaexpressão
podetertiposdiferentes:
Callable<String> c = () -> "retorna uma String";
PrivilegedAction<String> p = () -> "retorna uma String";
Naprimeiralinhadessecódigo,aexpressão () -> "retorna uma String"
representaum Callable<String>,enasegundalinhaessamesmaexpressão
representaainterfacefuncional PrivilegedAction<String>. Foio Target
Typequemajudouocompiladoradecidirqualtipoessamesmaexpressãorepre-
sentavaemcadamomento.
Omesmovaleparamethodreferences
Essasituaçãotambémacontececomorecursodemethodreference.Amesma
referênciapoderepresentartiposdiferentes,contantoquesejamequivalentes:
Callable<String> c = callable::call;
PrivilegedAction<String> action = callable::call;
118

## Página 131

CasadoCódigo Capítulo12.Apêndice:maisJava8comreflection,JVM,APIselimitações
Como vimos, estes dois tipos possuem estrutura bem parecida, por-
tanto a referência callable::call pode ser representada como um
PrivilegedAction<String>.
Agrandediferençaéquequandoutilizamosmethodreferenceainferênciade
tipoémaisforte,afinalotipoestáexplícitoemsuadeclaração,diferentedequando
estamostrabalhandocomumaexpressãolambda.Outropontoéque,comojávimos,
existeaconversãoentreinterfacesfuncionais.
12.3 Limitações d ainferênciano lambda
Talvezvocêvásedepararcomessesproblemasbemmaisprafrente,maséimpor-
tanteterconhecimentodequeelesexistem:algumasvezesocompiladornãoconse-
gueinferirostiposcomtotalfacilidade,emespecialquandoencadeamosmétodos
queutilizamlambda.
V e j aquecommethodreferencesjávimosqueissocompila:
usuarios.sort(Comparator.comparingInt(Usuario::getPontos)
.thenComparing(Usuario::getNome));
Porém,usandooslambdasqueparecemequivalentes,nãocompila:
usuarios.sort(Comparator.comparingInt(u -> u.getPontos())
.thenComparing(u -> u.getNome()));
Seavisarmosqueo uéum Usuario,oretornodo comparingIntficamais
óbvioparaocompilador,ecomocódigoaseguirconseguimosumacompilaçãosem
erros:
usuarios.sort(Comparator.comparingInt((Usuario u) -> u.getPontos())
.thenComparing(u -> u.getNome()));
Outraformaseriaquebraradeclaraçãodo Comparator,perdendoainterface
fluente:
Comparator<Usuario> comparator = Comparator.comparing(
u -> u.getPontos());
usuarios.sort(comparator.thenComparing(u -> u.getNome()));
V o c êtambémpoderia forçar o tipo genéricodo métodoestático,fazendo
Comparator.<Usuario>comparingInt,queéumasintaxepoucovistanodia
adia.
119

## Página 132

12.3.Limitações dainferêncianolambda CasadoCódigo
Reparequetudofuncionouperfeitamentequandoutilizamosomethodrefe-
rence,jáquecomelesocompiladorpodefacilmentedizerquaissão ostiposen-
volvidos.
Omesmoaconteceparacasoscomencadeamentosdeinterfacesfluentesmais
simples.V o c êpodefazer,comovisto:
usuarios.sort(Comparator.comparingInt(Usuario::getPontos).reversed());
Masseusarolambdaemvezdomethodreference,nãocompila:
usuarios.sort(Comparator.comparingInt(u -> u.getPontos()).reversed());
Precisariaexplicitarostiposgenéricosouotiponolambda.Ouaindadeclararo
Comparatorantesesódepoisinvocaro reversed.Comoutilizamoscommais
frequênciaomethodreferencenessesencadeamentos,essesserãocasosraros.
Essaslimitações são muitobemdetalhadasnanovaversão daJavaLanguage
Specification:
http://cr.openjdk.java.net/\char126dlsmith/jsr335-0.8.0/D.html
Suporteamúltiplasanotaçõesiguais
U mdetalhequepodeserbastanteutilemnossodiaadiaéacapacidadedeaplicar
amesmaanotaçãorepetidasvezesemummesmotipo.Essapossibilidade,conhecida
comorepeatingannotations,foiadicionadananovaversãodalinguagem!
Considerequetemosaanotação @Roleparadeterminarotipodeacessoper-
mitidoparaumaclasse:
@Documented
@Retention(RetentionPolicy.RUNTIME)
@Target({ElementType.ANNOTATION_TYPE, ElementType.TYPE})
public @interface Role {
String value();
}
Paraadicionarduasrolesemumamesmaclassenasversões pré-Java8teríamos
quemodificarsuaestruturaprareceberumarrayde Strings,ouqualqueroutro
tipoquerepresenteumaregradeacessodeseusistema.
Aotentardeclararduasvezesaanotação,paratalvezmelhorarumpoucoalegi-
bilidade,receberíamosoerrodecompilação: Duplicate annotation @Role.
120

## Página 133

CasadoCódigo Capítulo12.Apêndice:maisJava8comreflection,JVM,APIselimitações
@Role("presidente")
@Role("diretor")
public class RelatorioController {
}
Para tornar isso possível agora podemos marcar a nossa anotação com
@Repeatable,passandocomoargumentoumaoutraanotação queservirápara
armazenarasanotações repetidas.Nestecaso:
@Repeatable(Roles.class)
@Documented
@Retention(RetentionPolicy.RUNTIME)
@Target({ElementType.ANNOTATION_TYPE, ElementType.TYPE})
public @interface Role {
String value();
}
Onde @Rolesconteráumarraydaanotaçãoqueelaarmazenará:
@Documented
@Retention(RetentionPolicy.RUNTIME)
@Target({ElementType.ANNOTATION_TYPE, ElementType.TYPE})
public @interface Roles {
Role[] value();
}
Tudopronto!Agoraoseguintecódigocompila:
@Role("presidente")
@Role("diretor")
public class RelatorioController {
}
Aplicamosasanotações repetidasemumaclassenesteexemplo,porémomesmo
podeserfeitoemqualquerlugarpassíveldeutilizarumaanotação.
DiversosmétodosforamadicionadosnaAPIdereflectionpararecuperaressas
anotações. U mexemploéométodogetAnnotationsByTypequerecebeaclasse
daanotaçãoprocuradacomoparâmetro:
121

## Página 134

12.4.FimdaPermgen CasadoCódigo
RelatorioController controller = new RelatorioController();
Role[] annotationsByType = controller
.getClass()
.getAnnotationsByType(Role.class);
Arrays.asList(annotationsByType)
.forEach(a -> System.out.println(a.value()));
Comosaída,teremososvaloresinseridosnasroles:
presidente
diretor
12.4 Fim d aPermgen
U mpontoquenãopodepassardespercebidonessanovaversãoéaremoçãocom-
pletadaPermGem(PermanentGeneration),conhecidaimplementaçãodeespaçode
memóriadaJVMreservadaparaosvalorespermanentes.Issosignificaquenunca
maisreceberemosofamoso java.lang.OutOfMemoryError: PermGen!
V o c êpodelermaissobreaproposta(JEP)dessaremoçãoaqui:
RemovethePermanentGenerationhttp://openjdk.java.net/jeps/122
ComosucessordestaimplementaçãoagoratemosoMetaspace,queéamemó-
rianativapararepresentaçãodosmetadadosdeclasse.V o c êjápodetervistouma
soluçãosemelhantenoJRockitdaOracle,ouJVMdaIBM.
Paraconhecermaisdetalhesavançadossobreperformanceeparticularidades
dessamigraçãovocêpodeseinteressarpeloseguinteartigo:
http://java.dzone.com/articles/java-8-permgen-metaspace
12.5 Reflection: parameter names
AAPIdereflectiontambémrecebeumelhorias.U m adelasfoiatãoesperadahabi-
lidadederecuperaronomedosparâmetrosdosmétodoseconstrutores.
Issoagorapodeserfeitodeformamuitosimples:bastainvocarmosométodo
getParametersdeummétodoouconstrutor.Podemosfazerissocomoseguinte
construtordaclasse Usuario:
public Usuario(String nome, int pontos) {
this.pontos = pontos;
122

## Página 135

CasadoCódigo Capítulo12.Apêndice:maisJava8comreflection,JVM,APIselimitações
this.nome = nome;
}
V a m o sutilizarométodogetConstructorfornecendoostiposdosparâme-
trospararecuperaresseconstrutorcomreflection:
Constructor<Usuario> constructor =
Usuario.class.getConstructor(String.class, int.class);
Agoratudoqueprecisamosfazeréchamarométodo getParameterspara
obtercomorespostaumarraydotipo java.lang.reflect.Parameter:
Constructor<Usuario> constructor =
Usuario.class.getConstructor(String.class, int.class);
Parameter[] parameters = constructor.getParameters();
Pronto!Agoradeformabemintuitivapodemosexibirseunomescomométodo
getName:
Constructor<Usuario> constructor =
Usuario.class.getConstructor(String.class, int.class);
Parameter[] parameters = constructor.getParameters();
Arrays.asList(parameters)
.forEach(param -> System.out.println(param.getName()));
Masnotequeaoexecutaressemétodooresultadoaindaserá:
arg0
arg1
Ainformação dosnomesnão estápresentenesseconstrutor! Paraconfirmar
isso,podemosimprimirtambémoresultadodométodoisNamePresentemcada
parâmetro:
Constructor<Usuario> constructor =
Usuario.class.getConstructor(String.class, int.class);
Parameter[] parameters = constructor.getParameters();
123

## Página 136

12.5.Reflection:parameternames CasadoCódigo
Arrays.asList(parameters)
.forEach(param -> System.out.println(
param.isNamePresent() + ": " + param.getName())
);
Reparequeoresultadoseráfalseparacadaparâmetro:
false: arg0
false: arg1
Issoaconteceupoisprecisamospassaroargumento -parametersparaocom-
pilador!Apenasdessaformaelevaimanterosnomesdosparâmetrosnobytecode
pararecuperarmosviareflection.Agorasim,aorecompilaraclasseteremosose-
guinteresultado:
true: nome
true: pontos
AntesdoJava8issotambémerapossívelaocompilarnossocódigocomaopção
-g(debug),masoproblemaéquenestecasoprecisamosmanipularobytecodedas
classeseissopodeserbastantecomplicado. Existemalternativasparasimplificar
essetrabalho,comoéocasodabibliotecaParanamer.Repareemumexemplode
seuuso:
Constructor<Usuario> constructor =
Usuario.class.getConstructor(String.class, int.class);
Parameter[] parameters = constructor.getParameters();
Paranamer paranamer = new CachingParanamer();
String[] parameterNames = paranamer.lookupParameterNames(constructor);
U m agrandevantagemdessaadiçãonaAPIdereflectionéque,alémdesimpli-
ficarbastantenossocódigo,evitaanecessidadededependênciasextrasemnossos
projetos.
V o c êpodelermaissobreapropostadessafeaturenolink:
http://openjdk.java.net/jeps/118
124

## Página 137

Capítulo13
Continuandoseusestudos
Existemdiversasformasparavocêcontinuarseusestudos.
U m adelaséexercitandooscódigosutilizadosnoscapítulosdolivro,quepodem
serencontradosnorepositório:
https://github.com/peas/java8
ParacriarumaintimidademaiorcomasnovidadesdaAPIeessanovaforma
funcionaldeprogramaremJava,recomendamosquevocêexercitebastanteosexem-
plosdesselivroequeváalém,fazendonovostestesalémdossugeridos.
13.1 Co m o tirar suas dúvidas
Encaminhesuasdúvidasoucrietópicosparadiscussãonalistaquefoicriadaespe-
cialmenteparaesselivro:
https://groups.google.com/forum/#!forum/java8-casadocodigo
Alémdeperguntar,vocêtambémpodecontribuircomsugestões, críticaseme-
lhoriasparanossoconteúdo.Envieseusexperimentosecódigos.

## Página 138

13.2.BibliotecasquejáusamouvãousarJava8 CasadoCódigo
V o c êsemprepodetirarsuasdúvidastambémpelofórumdoGUJ:
http://www.guj.com.br/tag/java
13.2 Bibliotecasque j á usam ou v ã o usar Ja v a8
AtualmenteexistemalgumasbibliotecasutilizandoJava8!U m aexemploéaGSCol-
lections,doGoldmanSachs,queoferecediversasclassesutilitáriaseumaformasim-
plesdetrabalharcomascoleções dojdkdeformacompatível.
V o c êpodevermaisdetalhesdessabibliotecaeconsultarseucódigo-fonteno
repositório:
https://github.com/goldmansachs/gs-collections/
Háalgumasbrincadeirasinteressantes,comoaimplementação desequências
lazy,nomelhorestilofuncional:
http://java.dzone.com/articles/lazy-sequences-implementation
OframeworkVRaptortambémvaiutilizarjdk8emsuaversão 4.5! Poren-
quanto,algunspluginsestão sendodesenvolvidosparaadicionaralternativasele-
gantesparaquemjáusaessaversãodalinguagememseusprojetos.
126

## Página 139

CasadoCódigo ÍndiceRemissivo
ÍndiceRemissivo
ActionListener,13
andThen,21
anotações, 120
autoboxing,29,33,63
average,59
BiConsumer,47
BiFunction,38
boxed,65
Calendar,83
ChronoUnit,92
close,63
closure,17
Collector,47
Collectors,48
Comparator,25
comparing,27
computeIfAbsent,75
construtor,36
Consumer,7,20
Date,83
decorator,21
defaultmethods,19
distinct,70
Duration,94
efeitocolateral,44,80
especificação,2,17,23,84,94,114
exceptions,67
factory,63
Fibonacci,65
Files,67
filter,43
final,17
findAny,57
findFirst,58
flatMap,68
fold,61
forEach,7,19
fork/join,78
formatters,89
Function,37,50,73
FunctionalInterface,15
generate,64
groupingBy,75
herançamúltipla,23
imutabilidade,86
IntBinaryOperator,38,60
interfacefluente,45
interfacefuncional,11
IntStream,50
invokedynamic,17
iterate,66
iterator,61
127

## Página 140

ÍndiceRemissivo CasadoCódigo
JEP,2,114
Jodatime,83
lambda,9,17
lazy,56–58,65
limit,64
limitações, 119
LocalDate,84
LocalDateTime,84
LongStream,72
métodosdefault,19
Map,72,75
map,50,54
mapToInt,50
mapToLong,72
max,53
metaspace,122
methodreferences,31
naturalOrder,27
operações decurtocircuito,64
operações determinísticas,79
operações intermediárias,57
operações terminais,57
operadordiamante,113
paralelização,78
paralelizaçãoperformance,78
parameternames,122
Paranamer,124
partitioningBy,75
Paths,67
peek,58
Period,92
permgen,122
pipeline,56
Predicate,22,43,62
random,64
redução,59
reduce,60
reflection,122
removeIf,22
reversed,34
Runnable,11
skip,64
sort,55
Spliterator,81
static,27,38
Stream,42
streaminfinito,64
sum,59
summing,77
super,38
Supplier,37,47,64
toArray,49
toCollection,49
ToIntBiFunction,38
ToIntFunction,29,50
toList,48
toMap,73
toSet,49
UnaryOperator,66
Validador,14
ZonedDateTime,85
128