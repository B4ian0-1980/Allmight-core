---json
{
  "id": "java_se_7_programmer_i_o_guia_para_sua_certifica__o_oracle_certified_associate",
  "title": "Java SE 7 Programmer I O guia para sua certificação Oracle Certified Associate",
  "categoria": "03-linguagens",
  "subcategoria": "java",
  "resumo": "**Arquivo Original:** `Java SE 7 Programmer I O guia para sua certificação Oracle Certified Associate.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "associate",
    "certifica",
    "certified",
    "guia",
    "java",
    "linguagens",
    "oracle",
    "para"
  ],
  "perguntas_tipo": [
    "Como utilizar Java SE 7 Programmer I O guia para sua certificação Oracle Certified Associate?",
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

# Java SE 7 Programmer I O guia para sua certificação Oracle Certified Associate

> **Arquivo Original:** `Java SE 7 Programmer I O guia para sua certificação Oracle Certified Associate.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 2

CasadoCódigo Sumário
Sumário
1 Agradecimentos 1
2 Certificação? 3
3O b á s i c o d e J a v a 7
3.1 Definaoesco podevariá veis ................... 7
3.2 DefinaaestruturadeumaclasseJava .............. 1 3
3.3 CrieaplicaçõesJavaexecutáveiscomummétodomain ... 2 2
3.4 ImporteoutrospacotesJavaedeixe-osacessíveisaoseucódigo 32
4 TrablhandocomtiposdedadosemJava 47
4.1 Declarareinicializarvariáveis .................. 4 7
4.2 Diferencia entre variáveis de referências a objetos e tipos
primitivos .............................. 6 3
4.3 Leiaouescrevaparacamposdeobjetos ............. 6 6
4.4 Expliqueociclodevidadeumobjeto(criação,“dereferência”
egarbagecollection) ........................ 6 8
4.5 Chamemétodosemobjetos ................... 7 3
4.6 ManipuledadosusandoaclasseStringBuildereseusmétodos 78
4.7 CriandoemanipulandoStrings ................. 8 1
5 Usandooperadoreseconstruçõesdedecisão 95
5.1 UseoperadoresJava ........................ 9 5
5.2 Useparentêsesparasobrescreveraprecedênciadeoperadores 119
i

## Página 3

Sumário CasadoCódigo
5.3 Teste a igualdade entre Strings e outros objetos usando == e
equals() ............................... 1 2 0
5.4 Utilizeoifeif/else ......................... 1 3 0
5.5 Utilizeoswitch ........................... 1 3 8
6 Criandoeusandoarrays 147
6.1 Declare,instancie,inicializeeuseumarrayuni-dimensional 147
6.2 Declare,instancie,inicializeeuseumarraymulti-dimensional 158
6.3 DeclareeuseumaArrayList ................... 1 6 2
7 Usandolaços 173
7.1 Crieeuselaçosdotipowhile .................. 1 7 3
7.2 Crieeuselaçosdotipofor,incluindooenhancedfor .... 1 7 7
7.3 Crieeusolaçosdotipodo/while ................ 1 8 4
7.4 Compareostiposdelaços .................... 1 8 7
7.5 Use break e continue ....................... 1 9 0
8 Trabalhandocommétodoseencapsulamento 199
8.1 Criemétodoscomargumentosevaloresderetorno ..... 1 9 9
8.2 Apliqueapalavrachavestaticamétodosecampos ...... 2 0 8
8.3 Criemétodossobrecarregados .................. 2 1 4
8.4 Diferenciaentreoconstrutorpadrãoeconstrutoresdefinidos
pelousuário ............................ 2 2 2
8.5 Crieesobrecarregueconstrutores ................ 2 2 9
8.6 Apliquemodificadoresdeacesso ................ 2 3 4
8.7 Apliqueprincípiosdeencapsulamentoaumaclasse ..... 2 4 9
8.8 Determine o efeito que ocorre com referências a objetos e a
tiposprimitivosquandosãopassadosaoutrosmétodoseseus
valoresmudam ........................... 2 5 3
9 Trabalhandocomherança 259
9.1 Implementandoherança ..................... 2 5 9
9.2 Desenvolvacódigoquemostraousodepolimorfismo .... 2 6 9
9.3 Diferencieentreotipodeumareferênciaeotipodeumobjeto 285
ii

## Página 4

CasadoCódigo Sumário
9.4 Determinequandoénecessáriofazercasting ......... 2 9 7
9.5 Usesuperethisparaacessarobjetoseconstrutores ...... 3 0 8
9.6 Useclassesabstrataseinterfaces ................. 3 2 1
10 Lidandocomexceções 331
10.1 Diferencieentreexceçõesdotipochecked,runtimeeerros . 331
10.2 DescrevaoquesãoexceçõeseparaquesãoutilizadasemJava 333
10.3 Crieumblocotry-catchedeterminecomoexceçõesalteram
ofl uxono rmaldeump r ograma................. 3 3 5
10.4 Invoqueummétodoquejogaumaexceção .......... 3 4 2
10.5 Reconhecaclassesdeexceçõescomunsesuascategorias ... 3 5 7
11 Boaprova 365
12 RespostasdosExercícios 367
iii

## Página 6

Capítulo1
Agradecimentos
“Às três famílias que me acolhem no dia a dia, Azevedo Silveira, Bae Song e
Caelum”-GuilhermeSilveira
Escrever um livro é difícil, descrever pequenos detalhes de uma lin-
guageméumdesafiomaiordoquepoderíamosimaginar.
Fica um agradecimento ao Gabriel Ferreira, Márcio Marcelli, Leonardo
Cordeiro e ao Alexandre Gamma pelas valiosas revisões dos textos e exercí-
cios. Agradecimento especial ao Leonardo Wolter por sua revisão completa,
alémdediversassugestõesemelhorias.
Um abraço a todos da Caelum, do Alura e da Casa do Código, que nos
incentivam na busca contínua de conhecimento com a finalidade de melho-
riadaqualidadedeensinoeaprendizadodedesenvolvimentodesoftwareno
Brasil.

## Página 8

CAPÍTULO 2 
Certificação? 
As certificações J ava s ão, p elo b em ou p elo m al, mui to r econhecidas no 
mercado. Em sua última versão, a principal certificação foi qu ebrada em 
duas provas. Este livro vai guiá-lo por questões e assuntos abordados para 
a primeira prova, a Java SE 7 Programmer I, de maneira profunda e 
desafiadora. 
O livro vai percorrer cada tema, com detalhes e exercícios, para você 
chegar à prova confiante. Decorar regras seria uma maneira de estudar, mas 
não estimulante. Por que não compila? Por que não executa como esperado? 
Mais do que um guia para que você tenha sucesso na prova, nossa intenção é 
mostrar como a linguagem funciona por trás. 
Ao terminar essa longa caminhada, você será capaz de entender melhor 
a linguagem, assim como poder dizer com exatidão os motivos de determi­
nadas construções e idiomismos. 

## Página 9

CasadoCódigo
Comoestudar
Lembre-sedeusaralinhadecomandodoJava,nãouseoEclipseouqual-
quer outra IDE: os erros que o compilador da linha de comando mostra po-
demserdiferentesdodaIDE,evocênãoquerqueissoatrapalheseudesem-
penho.
L e m b r e - s ed efi c a ra t e n t o ,n ap r o v an ã ofi c a r ác l a r oq u a loa s s u n t oq u e
estásendotestadoevocêdeveseconcentraremtodoocódigo,nãosóemum
assun too uo u tr o .
E s s ep r o c e s s oél o n g oear e c o m e n d a ç ã oéq u ea g e n d eap r o v aa g o r a
mesmo no site da Oracle, para que não haja pausa desde o primeiro dia de
leitura,atéoúltimodiadeleitura,aexecuçãodediversossimuladoseaprova
emsi.
Não deixe de testar todo o código em que não sentir confiança. Os exer-
cícios são gerados de propósito para causar insegurança no candidato, para
levá-lo para um lado, sendo que o problema pode estar em outro. E faça
muitosexercíciosesimulados.
Nãohesite,tiresuasdúvidasnositedoGUJenosavisedesuacertificação
viatwitteroufacebook:
http://www.guj.com.br http://www.twitter.com/casadocodigo
http://www.facebook.com/casadocodigo
Bomestudo,boaprova,boasortee,acimadetudo,bem-vindoaogrupo
daquelesquenãosóusamumalinguagem,masadominam.
Seçõesdaprova
Osassuntoscobradoseabordadosaquisão:
1) JavaBasics
• Definethesco peo fvariables
• Definethestructur eo faJ a vaclass
• Cr ea teexecu tableJ a vaa p plica tio nswi thamainmethod
• ImportotherJavapackagestomakethemaccessibleinyourcode
4

## Página 10

CasadoCódigo Capítulo2. Certificação?
2) W o rkingW i thJ a vaDa taT ypes
• Declareandinitializevariables
• Differentiate between object reference variables and primitive vari-
ables
• Reado rwri tetoob jectfields
• Explain an Object’s Lifecycle (creation, “dereference” and garbage
collection)
• Callmethodsonobjects
• ManipulatedatausingtheStringBuilderclassanditsmethods
• CreatingandmanipulatingStrings
3) UsingOperatorsandDecisionConstructs
• UseJavaoperators
• Useparenthesistooverrideoperatorprecedence
• TestequalitybetweenStringsandotherobjectsusing==andequals
()
• Createifandif/elseconstructs
• Useaswitchstatement
4) CreatingandUsingArrays
• Declare,instantiate,initializeanduseaone-dimensionalarray
• Declare,instantiate,initializeandusemulti-dimensionalarray
• DeclareanduseanArrayList
5) UsingLoopConstructs
• Createandusewhileloops
• Createanduseforloopsincludingtheenhancedforloop
• Createandusedo/whileloops
5

## Página 11

CasadoCódigo
• Compareloopconstructs
• Usebreakandcontinue
6) WorkingwithMethodsandEncapsulation
• Createmethodswithargumentsandreturnvalues
• Applythestatickeywordtomethodsandfields
• Cr ea teano verloadedmethod
• Differentiatebetweendefaultanduserdefinedconstructors
• Createandoverloadconstructors
• Applyaccessmodifiers
• Applyencapsulationprinciplestoaclass
• Determine the effect upon object references and primitive values
whentheyar epassedin tomethodstha tchangetheval ues
7) WorkingwithInheritance
• Implementinheritance
• Developcodethatdemonstratestheuseofpolymorphism
• Differentiatebetweenthetypeofareferenceandthetypeofanobject
• Determinewhencastingisnecessary
• Usesuperandthistoaccessobjectsandconstructors
• Useabstractclassesandinterfaces
8) HandlingExceptions
• Differentiate among checked exceptions, RuntimeExceptions and
Errors
• Createatry-catchblockanddeterminehowexceptionsalternormal
programflow
• Describewha tExcep tio nsar eusedfo rinJ a va
• I n vokeamethodtha tthr o wsanexcep tio n
• Recognizecommonexceptionclassesandcategories
6

## Página 12

Capítulo3
ObásicodeJava
3.1 Definaoescopodevariáveis
Oescopoéoquedeterminaemquepontosdocódigoumavariávelpodeser
usada.
Variáveislocais
Chamamos de locais as variáveis declaradas dentro de métodos ou con-
strutores. Antesdecontinuar,vamosestabelecerumaregrabásica: ociclode
vida de uma variável local vai do ponto onde ela foi declarada até o fim do
blocoondeelafoideclarada.
Mas o que é um bloco? Podemos entender como bloco um trecho de
códigoentrechaves. Podeserummétodo,umconstrutor,ocorpodeum
if,
deum foretc.:

## Página 13

3.1. Definaoescopodevariáveis CasadoCódigo
public void m1() { // início do bloco do método
int x = 10; // variável local do método
if (x >= 10) { // início do bloco do if
int y = 50; // variável local do if
System.out.print(y);
} // fim do bloco do if
} // fim do bloco do método
Analisando esse código, temos uma variável x, que é declarada no
começo do método. Ela pode ser utilizada durante todo o corpo do método.
Dentro do if, declaramos a variávely. y só pode ser utilizada dentro do
corpodo if,delimitadopelaschaves. Setentarmosusar yforadocorpodo
if,teremosumerrodecompilação,poisavariávelsaiudoseuescopo.
Tome cuidado especial com loopsfor. As variáveis declaradas na área
deinicializaçãodoloopsópodemserusadasnocorpodoloop:
for (int i =0 , j =0 ; i < 10; i++)
j++;
System.out.println(j); // erro, já não está mais no escopo
Parâmetros de métodos também podem ser considerados variáveis lo-
cais ao método, ou seja, só podem ser usadosdentro do método onde foram
declarados:
class Teste {
public void m1(String bla ){
System.out.print(bla);
}
public void m2() {
// erro de compilação pois bla não existe neste
// escopo
System.out.println(bla);
8

## Página 14

CasadoCódigo Capítulo3. ObásicodeJava
}
}
Variáveisdeinstância
Variáveisdeinstânciaouvariáveisdeobjetosãoosatributosdosobjetos.
São declaradas dentro da classe, mas fora de qualquer método ou constru-
tor. Podem ser acessadas por qualquer membro da classe e ficam em escopo
enquantooobjetoexistir:
class Pessoa {
// variável de instância ou variável de objeto
String nome ;
public void setNome(String n){
// acessando a variável de instância no método
this.nome = n;
}
}
Variáveisestáticas(classvariables)
Podemos declarar variáveis que são compartilhadas por todas as instân-
cias de uma classe usando a palavra chavestatic. Essas variáveis estão no
escopodaclasse,eláficarãoenquantoaclasseestivercarregadanamemória
(enquantooprogramaestiverrodando,nagrandemaioriadoscasos).
class Pessoa {
static int id =1 ;
}
class Teste {
public static void main(String[] args){
Pessoa p = new Pessoa();
System.out.println(p.id); // acessando pelo objeto
System.out.println(Pessoa.id); // acessando direto pela
// classe
}
}
9

## Página 15

3.1. Definaoescopodevariáveis CasadoCódigo
No caso de variáveisstatic, não precisamos ter uma referência para
usá-lasepodemosacessá-lasdiretamenteapartirdaclasse,desdequerespei-
tandoasregrasdevisibilidadedavariável.
Variáveiscomomesmonome
Logicamente, não é possível declarar duas variáveis no mesmo escopo
comomesmonome:
public void bla() {
int a =0 ;
int a = 10;// erro
}
Mas,eventualmente,podemostervariáveisemescoposdiferentesquepo-
dem ser declaradas com o mesmo nome. Em casos em que possa haver am-
biguidade na hora de declará-las, o próprio compilador irá emitir um erro
evitando a confusão. Por exemplo, não podemos declarar variáveis de classe
edeinstânciaco momesmono me:
class Bla {
static int a;
int a; // erro de compilação,
}
...
System.out.println(new Bla().a); // qual variável estamos
// acessando?
Também não podemos declarar variáveis locais com o mesmo nome de
parâmetros:
public void metodo(String par ){
int par =0 ; // erro de compilação
System.out.println(par); // qual?
}
Apesar de parecer estranho, é permitido declarar variáveis locais ou
parâmetros com o mesmo nome de variáveis de instância ou de classe. Essa
10

## Página 16

CasadoCódigo Capítulo3. ObásicodeJava
técnicaéchamadade shadowing. Nessescasos, épossívelresolveraambigu-
idade: paravariáveisdeclasse,podemosreferenciarpelaprópriaclasse; para
variá veisdeinstância,usamosapala vracha ve this:
class Pessoa {
static int x =0 ;
int y =0 ;
public static void setX(int x){
// Usando a referência da classe
Pessoa.x = x;
}
public void setY( int y){
// usando o this
this.y = y;
}
}
Qua n don ãou sa m osothis o uon o m edac la s sepa rau sa rava riá v e l ,o
compiladorsempreutilizaráavariáveldemenorescopo:
class X{
int a = 10;
public void metodo() {
int a = 20; // shadowing
System.out.println(a); // imprime 20
}
}
1) Escolhaaopçãoadequadaaotentarcompilarerodarocódigoaseguir:
1 class Teste {
2 public static void main(String[] args){
3 for (int i =0 ; i < 20; i++) {
4 System.out.println(i);
5 }
11

## Página 17

3.1. Definaoescopodevariáveis CasadoCódigo
6 int i = 15;
7 System.out.println(i);
8 }
9 }
a) Errodecompilaçãonalinha6. Avariável inãopodeserredeclarada.
b) Errodecompilaçãonalinha7. Avariável iéambígua.
c) Compilaeroda,imprimindode0até19edepois15.
d) Compila e roda, imprimindo de 0 até 19, depois ocorre um erro de
execuçãonalinha6.
e) Compilaeroda,imprimindode0até19edepois19novamente.
2) Escolhaaopçãoadequadaaotentarcompilarerodarocódigoaseguir:
1 class Teste {
2 static int x = 15;
3
4 public static void main(String[] x){
5 x = 200;
6 System.out.println(x);
7 }
8 }
a) Ocódigocompilaeroda,imprimindo200.
b) Ocódigocompilaeroda,imprimindo15.
c) Ocódigonãocompila.
d) Ocódigocompilamasdáerroemexecução.
3) Escolhaaopçãoadequadaaotentarcompilarerodarocódigoaseguir:
1 class Teste {
2 static int i =3 ;
3
4 public static void main(String[] a){
5 for (new Teste().i = 10; new Teste().i < 100;
12

## Página 18

CasadoCódigo Capítulo3. ObásicodeJava
6 new Teste().i++) {
7 System.out.println(i);
8 }
9 }
10 }
a) Nãocompilaalinha4.
b) Nãocompilaalinha5.
c) Compilaeimprime100vezesonúmero3.
d) Co m p ilaeim p rimeosn úmer osde10a té99.
3.2 DefinaaestruturadeumaclasseJava
Nestaseção, iremosentenderaestruturadeumarquivojava, ondeinseriras
declaraçõesdepacoteseimportsecomodeclararclasseseinterfaces.
Para entender a estrutura de uma classe, vamos ver o arquivo
Pessoa.java:
1 // Declaração de pacote
2 package br.com.caelum.certificacao;
3
4 // imports
5 import java.util.Date;
6
7 // Declaração da classe
8 class Pessoa {
9 // conteúdo da classe
10 }
Pacotes
Pacotesservemparaseparareorganizarasdiversasclassesquetemosem
nossos sistemas. Todas as classes pertencem a um pacote, sendo que, caso o
pacotenãosejaexplicitamentedeclarado,aclassefarápartedoquechamamos
depacotepadrão ,o udefaultpackage . Todas as classes nodefault package
se enxergam e podem ser utilizadas entre si. Classes no pacote default não
podemserimportadasparausoemoutrospacotes:
13

## Página 19

3.2. DefinaaestruturadeumaclasseJava CasadoCódigo
1 // Uma classe no pacote padrão
2 classe Pessoa {
3 //...
4 }
Paradefinirqualopacoteaqueaclassepertence,usamosapalavra-chave
package, seguida do nome do pacote. Só pode existir um únicopackage
definido por arquivo, e ele deve ser a primeira instrução do arquivo. Após
a definição dopackage, devemos finalizar a instrução com um;. Podem
existircomentáriosantesdadefiniçãodeumpacote:
1 // declaração do pacote
2 package br.com.caelum.certificacao;
3
4 classe Pessoa {
5 //...
6 }
Aproveitando que tocamos no assunto, opackage deve ser a primeira
instruçãodecódigoquetemosdeclaradaemnossoarquivo. Comentáriosnão
sãoconsideradospartedocódigo,portanto,podemexistiremqualquerlugar
doarquivojavasemrestrições.
Parainserircomentárioemnossocódigo,temosasseguintesformas:
1 // comentário de linha
2
3 /*
4 comentário de
5 multiplas linhas
6 */
7 class /* comentário no meio da linha */ Pessoa {
8
9 /**
10 * JavaDoc, repare que a primeira linha do comentário tem
11 * 2 asteriscos
12 */
13 public void metodo() {
14 }
15 }
14

## Página 20

CasadoCódigo Capítulo3. ObásicodeJava
Parasabermais:JavaDoc
Javadoc é um tipo especial de comentário que pode ser utilizado
para gerar uma documentação HTML a partir de nosso código.
Parasabermais,acesse http://www.oracle.com/technetwork/java/javase/
documentation/javadoc-137458.html
Classe
Uma classe é a forma no Java onde definimos os atributos e comporta-
mentosdeumobjeto. Adeclaraçãodeumaclassepodeserbemsimples,ape-
nasapalavra
classseguidadonomeede {}:
1 class Pessoa {}
Existemoutrosmodificadoresquepodemserusadosnadefiniçãodeuma
classe,masveremosessasoutrasopçõesmaisàfrente,ondediscutiremosesses
modificadorescommaisdetalhes.
Vale lembrar que java écase sensitivee
Class éon o m ed eu m ac la s see
nãopodemosusá-loparadefinirumanovaclasse.
Dentrodeumaclasse,podemostervariáveis,métodoseconstrutores. Es-
sasestruturassãochamadasde membrosdaclasse.:
1 class Pessoa {
2
3 String nome ;
4 String sobrenome;
5
6 Pessoa(String nome , String sobrenome){
7 this.nome = nome;
8 this.sobrenome = sobrenome;
9 }
10
11 public String getNomeCompleto() {
12 return this .nome + this.sobrenome;
13 }
14 }
15

## Página 21

3.2. DefinaaestruturadeumaclasseJava CasadoCódigo
Nomesdosmembros
Podemostermembrosdetiposdiferentescomomesmonome. Fique
atento,ocódigoaseguircompilanormalmente:
1 class B{
2 String b ;
3
4 B() {
5 }
6
7 String b() {
8 return null ;
9 }
10 }
Variaveis
Usandocomoexemploaclasse Pessoadefinidaanteriormente, nomee
sobrenomesãovariáveis. Adeclaraçãodevariáveisébemsimples,sempreo
tiposeguidodo nomedavariável.
Dizemosqueessassãovariáveisdeinstância,poisexisteumacópiadelas
para cada objetoPessoa criado em nosso programa. Cada cópia guarda o
estadodeumacertainstânciadessesobjetos.
Existemaindavariáveisquenãoguardamvaloresoureferênciasparauma
determinadainstância,massimumvalorcompartilhadoportodasasinstân-
cias de objetos. Essas são variáveisestáticas, definidas com a palavra-chave
static.V er emosmaissob r eesseti podememb r omaisàfr en te.
Métodos
A declaração de métodos é um pouquinho diferente pois precisamos do
tipodoretorno ,seguidodo nomedométodo eseguidodeparênteses,sendo
quepodeounãohaverparâmetrosdeentradadessemétodo. Cadaparâmetro
éumadeclaraçãodevariávelemsi. Essalinhadométodo,ondeestádefinido
16

## Página 22

CasadoCódigo Capítulo3. ObásicodeJava
or e t o r n o ,on o m eeo sp a r â m e t r o séo n d et e m o saassinaturadométodo.
Cuidado,poisa assinaturadeummétodo incluisomenteonomedométodo
eostiposdosparâmetros.
Assimcomovariáveis,métodostambémpodemser static,co mov er -
emosmaisadiante.
Construtores
Uma classe pode possuir zero ou vários construtores. Nossa classe
Pessoa possui um construtor que recebe como parâmetros o nome e o so-
brenome da pessoa. A principal diferença entre a declaração de um método
eu mc o n s t r u t o réq u eu mconstrutornãotemretornoepossuiomesmo
nomedaclasse .
Métodoscomomesmonomedaclasse
Cuidadoscommétodosqueparecemconstrutores:
1 class Executa {
2
3 // construtor
4 Executa() {
5 }
6
7 // método
8 void Executa() {
9 }
10
11 }
N o tequeumco nstru to rpodeterumreturnvazio:
1 class X{
2 int j = -100;
3
4 X(int i){
17

## Página 23

3.2. DefinaaestruturadeumaclasseJava CasadoCódigo
5 if (i >1 )
6 return;
7 j = i;
8 }
9 }
C a s oov a l o rs e j am e n o ro ui g u a la1, o valor de j será -100,c a s o
contrário,seráomesmovalorde i.
Interfaces
Alémdeclasses,tambémpodemosdeclarar interfacesemnossosarquivos
java. Paradefinirumainterfaceusamosapalavrareservada interface:
1 interface Autenticavel {
2
3 final int TAMANHO_SENHA =8 ;
4
5 void autentica(String login , String senha );
6 }
Em uma interface, devemos apenas definir a assinatura do método, sem
a sua implementação. Além da assinatura de métodos, também é possível
declararconstanteseminterfaces.
Multíplasestruturasemumarquivo
Em java, é possível definir mais de uma classe/interface em um mesmo
arquivojava,emboradevamosseguiralgumasregras:
• Podemserdefinidosemqualquerordem;
• Se existir alguma classe/interface pública, o nome do arquivo deve ser
omesmodessaclasse/interface;
• Sópodeexistirumaclasse/interfacepúblicaporarquivo;
• Se não houver nenhuma classe/interface pública, o arquivo pode ter
qualquernome.
18

## Página 24

CasadoCódigo Capítulo3. ObásicodeJava
Logo,sãoválidos:
1 // arquivo1.java
2 interface Bar {}
3
4 class Foo {}
1 // Foo.java
2 public class Foo {}
3
4 interface X{ }
Pacotes e imports em arquivos com múltiplas estru-
turas
As regras de pacotes e imports valem também para arquivos com
múltiplasestruturasdefinidas. Casoexistaadefiniçãodeumpacote,ela
vale para todas as classes/interfaces definidas nesse arquivo, e o mesmo
valepara imports.
1) Escolha a opção adequada ao tentar compilar e rodar o arquivo a seguir
semnenhumparâmetronalinhadecomando,como java D :
1 package a.b.c;
2
3 import java.util.*;
4
5 class D{
6 public static void main(String[] args){
7 ArrayList< String> lista = new ArrayList<String>();
8
9 for (String arg : args){
10 if (new E().existe(arg))
11 lista.add(arg);
12 }
13 }
19

## Página 25

3.2. DefinaaestruturadeumaclasseJava CasadoCódigo
14 }
15
16 import java.io.*;
17
18 class E{
19 public boolean existe(String nome ){
20 File f = new File(nome);
21 return f.exists();
22 }
23 }
a) Oarquivonãocompila.
b) Oarquivocompilamasdáerrodeexecuçãopoisoarrayénulo.
c) Oarquivocompilamasdáerrodeexecuçãopoisoarraytemtamanho
zero.
d) Rodaeimprime false.
e) Rodaeimprime true.
f) Rodaenãoimprimenada.
2) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class Teste {
2 int Teste = 305;
3
4 void Teste() {
5 System.out.println(Teste);
6 }
7
8 public static void main(String[] args){
9 new Teste();
10 }
11 }
a) Ocódigonãocompila: errosnaslinhas24,25e26.
b) Ocódigonãocompila: erronalinha25.
c) Ocódigonãocompila: errosnaslinhas24e26.
20

## Página 26

CasadoCódigo Capítulo3. ObásicodeJava
d) Ocódigocompilae,aorodar,imprime 305.
e) Ocódigocompilaenãoimprimenada.
f) Ocódigocompilae,aorodar,imprimeumalinhaembranco.
3) Escolhaaopçãoadequadaaotentarcompilaroarquivoaseguir:
1 package br.com.teste;
2
3 import java.util.ArrayList;
a) Erronalinha1: definimosopacotemasnenhumtipo.
b) Erronalinha3: importamosalgodesnecessárioaoarquivo.
c) Compilasemerros.
4) Escolhaaopçãoadequadaaotentarcompilaroarquivo A.java:
1 class A implements B {
2 }
3 public interface B{
4 }
5 class C extends A {
6 }
7 class D extends A, implements B {
8 }
a) N ãoco m p ila:err onalinha7 .
b) Nãocompila: erronalinha1.
c) N ãoco m p ila:err onalinha1,5e7 .
d) Nãocompila: erronalinha3.
e) Compila.
21

## Página 27

3.3. CrieaplicaçõesJavaexecutáveiscomummétodomain CasadoCódigo
3.3 Crie aplicações Java executáveis com um
métodomain
Nesta seção, entenderemos as diferenças entre classes normais e classes que
podemserexecutadaspelalinhadecomando.
Uma classe executável é uma classe que possui um método inicial para a
execuçãodoprograma ométodo main,queseráchamadopelaJVM.Classes
semométodo mainnãosãoclassesexecutáveisenãopodemserusadascomo
pontoinicialdaaplicação.
Métodomain
O tal método de entrada deve seguir algumas regras para ser executado
pelaJVM:
• Serpúblico( public);
• Serestático( static);
• Nãoterretorno( void);
• T erono memain;
• Receber como parâmetro um array ou varargs de String (
String[]ou String...).
Sãoentãométodos mainválidososseguintesexemplos:
1 //Parâmetro como array
2 public static void main ( String[] args){ }
3
4 //Parâmetro como varargs
5 public static void main ( String... args){ }
6
7 //A ordem dos modificadores não importa
8 static public void main(String[] args){ }
9
10 //O nome do parâmetro não importa
11 public static void main ( String... argumentos){}
22

## Página 28

CasadoCódigo Capítulo3. ObásicodeJava
12
13 //Também é uma definição válida de array
14 public static void main ( String args []) {}
Executandoumaclassepelalinhadecomando
Para executar uma classe commain pela linha de comando, devemos
compilar o arquivo com o comandojavac ee x e c u t a rac l a s s ec o moc o -
mando java:
U sandooar quivoHelloWorld.javaaseguir:
1 public class HelloWorld {
2
3 public static void main(String[] args){
4 System.out.println("Hello World! " );
5 }
6 }
Compilamoseexecutamosnoterminalcomosseguintescomandos:
$ javac HelloWorld.java
$
$ java HelloWorld
Hello World!
Repareque,paracompilaraclasse,passamoscomoparâmetroparaoco-
mando javaconomedoarquivo,enquantoparaexecutar ,passamosapenas
ono medaclasse( HelloWorld)paraoco mando java.
Passandoparâmetrospelolinhadecomando
Ao executarmos uma classe pela linha de comando, podemos passar
parâmetros para o método main. Esses valores serão recebidos no ar-
ray do método main.P o re x e m p l o ,v a m o sp a s s a ru mn o m ep a r aac l a s s e
HelloWorld:
1 public class HelloWorld{
2
3 public static void main(String[] args){
23

## Página 29

3.3. CrieaplicaçõesJavaexecutáveiscomummétodomain CasadoCódigo
4 //Lendo o valor da primeira posição do array args
5 System.out.println("Hello " + args[0] + "!");
6 }
7 }
Para informar o valor do parâmetro, é só informá-loAPÓS on o m ed a
classequeestásendoexecutada:
java HelloWorld Mario
Hello Mario!
Vocêpodepassarquantosparâmetrosquiser,bastasepará-losporespaço.
Cada parâmetro informado será armazenado em uma posição do array, na
mesmaordememquefoiinformado.
Compilaçãoeexecução
Paracriarumprogramajava,éprecisoescreverumcódigo-fontee,através
deumcompilador,geraroexecutável(bytecode). OcompiladordoJDK( Java
DevelopmentKit)éojavac . Paraaprovadecertificação,devemosconhecero
comportamentodessecompilador.
Ae x e c u ç ã od ob y t e c o d eéf e i t ap e l aJVM (Java Virtual Machine). O co-
mando javainvocaamáquinavirtualparaexecutarumprogramajava. Ao
baixarmosoJava,podemosescolherbaixaroJDK,quejávemcomoJRE,ou
somenteoJRE(Java Runtime Environment),queincl uiaVirtualMachine .
Algumasquestõesdaprovaabordamaspectosfundamentaisdoprocesso
decompilaçãoedeexecução. Énecessáriosabercomooscomandos
javac
eo javaprocuramosarquivos.
javac
Imagineoarquivo Prova.javadentrododiretóriodemeuprojeto:
class Prova {
double tempo;
}
$ javac Prova.java
24

## Página 30

CasadoCódigo Capítulo3. ObásicodeJava
Ob y t e c o d ed ac l a s s eProva gerado na compilação é colocado no ar-
quivo Prova.class dentro do nosso diretório de trabalho, no meu caso,
projeto. Oresultadoé:
Osprojetosprofissionaisutilizamorecursodepacotesparamelhororga-
nizar os fontes e os bytecodes. Vejamos qual é o comportamento dojavac
comautilizaçãodepacotes. Colocamosoarquivo Prova.javanodiretório
certificacao:
package certificacao;
class Prova {
double tempo;
}
[certificacao]$ javac certificacao/Prova.java
Nesse exemplo, o arquivo Prova.class é colocado no diretório
certificacao.
EscolhendoaversãodoJavanahoradecompilar
Na hora da compilação, é possível definir em que versão do Java o
código-fontefoiescrito. Issoéfeitocomaopção -sourcedocomando
javac.( javac MinhaClasse.java -source 1.3 ).
25

## Página 31

3.3. CrieaplicaçõesJavaexecutáveiscomummétodomain CasadoCódigo
java
Vamos utilizar um exemplo para mostrar o funcionamento do comando
java,c r i a n d ooa r q u i v oTeste.java no mesmo diretório, no mesmo pa-
cote:
package certificacao;
class Teste {
public static void main(String[] args){
Prova p = new Prova();
p.tempo = 210;
System.out.println(p.tempo);
}
}
$ javac certificacao/Teste.java
$ java certificacao.Teste
Saída:
210.0
Eoresultadosãoosarquivos:
Somente o arquivoTeste.java foi passado para o compilador. Nesse
arquivo, a classe Teste utiliza a classe Prova q u es ee n c o n t r ae mo u t r o
arquivo, Prova.java. Dessaforma,ocompiladorvaicompilarautomatica-
men teoar quivoProva.javasenecessário.
Para executar, é preciso passar o nome completo da classe desejada para
a máquina virtual. O sufixo.class não faz parte do nome da classe, então
elenãoaparecenainvocaçãodamáquinavirtualpelocomando java.
26

## Página 32

CasadoCódigo Capítulo3. ObásicodeJava
Propriedadesnalinhadecomando
A prova ainda cobra conhecimentos sobre como executar um programa
javapassando parâmetrosoupropriedadesparaaJVMeessaspropriedades
sãoidentificadaspelo -Dantesdelas. Este -Dnãofazpartedachave .
java -Dchave1=abc -Dchave2=def Foo xpto bar
chave1=abc e chave2=def são parâmetros/propriedades e xpto e
barsãoargumentosrecebidospelométodo main.
Classpath
Para compilar ou para executar, é necessário que os comandosjavac e
javapossamencontrarasclassesreferenciadaspelaaplicaçãojava.
Aprovadecertificaçãoexigeoconhecimentodoalgoritmodebuscadas
classes. As classes feitas pelo programador são encontradas através doclass-
path(caminhodasclasses).
Oc l a s s p a t héf o r m a d op o rdiretórios, jars e zips que contenham as
classesepacotesdanossaaplicação . Porpadrão,oclasspathestáconfigurado
paraodiretóriocorrente( .).
Configurandooclasspath
Háduasmaneirasdeconfiguraroclasspath:
1)Configurandoavariáveldeambiente CLASSPATHnosistemaopera-
cional.
Basta seguir as opções do SO em questão e definir a variável. Isso é con-
siderado uma má prática no dia a dia porque é um classpath global, que vai
valerparaqualquerprogramajavaexecutadonamáquina.
2 )C o ma so p ç õ e s-cp ou -classpath dos comandos javac ou
java.
É a forma mais usada. Imagine que queremos usar alguma biblioteca
jun toco mnossop r ograma:
$ javac -cp /diretorio/biblioteca.jar Prova.java
$ java -cp /diretorio/biblioteca.jar Prova
27

## Página 33

3.3. CrieaplicaçõesJavaexecutáveiscomummétodomain CasadoCódigo
Ep o d e m o sp a s s a rt a n t oc a m i n h o sd eo u t r a sp a s t a sc o m od eJARs
ou zips. Para passar mais de uma coisa no classpath, usamos o
separador de parâmetros no SO (no Windows é ponto e vírgula, no
Linux/Mac/Solaris/Unixsãodoispontos):
$ javac -cp /diretorio/biblioteca.jar;/outrodir/ scjp/Prova.java
$ java -cp /diretorio/biblioteca.jar;/outrodir/ scjp.Prova
Parasabermais:arquivosJAR
Parafacilitaradistribuiçãodebibliotecasdeclassesoudeaplicativos,
oJDKdisponibilizaumaferramentaparaacompactaçãodasclassesjava.
Umarquivo JARnadamaiséqueapastadenossasclassesnoformato
ZIPmascomextensão .jar.
Paracriarum jarincluindoapasta scjpquefizemosantes:
jar -cf bib.jar scjp
Agorapodemosexecutarnossaclasseusandoesse jar:
java -cp bib.jar scjp.Prova
28

## Página 34

CasadoCódigo Capítulo3. ObásicodeJava
Parasabermais:META-INF/Manifest.mf
Ao criar o jar usando o comandojar do JDK, ele cria automatica-
mente a pasta META-INF, que é usada para configurações relativas ao
nosso jar. Edentrodela,criaoarquivo Manifest.mf.
Esse arquivo pode ser usado para algumas configurações. Por exem-
plo,épossíveldizerqualclassedonosso jaréaclasseprincipal( Main-
Class)equedeveserexecu tada.
Basta criar um arquivo chamadoManifest.mf com a seguinte in-
struçãoindicandoaclasseco mométodo main:
Main-Class: scjp.Teste
Edepoisgerarojarpassandoessearquivo:
jar -cfm bib.jar meumanifest scjp
Nahoraderodarumjarcom Main-Class,bastausar:
java -jar bib.jar
1) Qual é uma assinatura válida do métodomain para executar um pro-
gramajava?
a) public static void main(String... args)
b) public static int main(String[] args)
c) public static Void main(String []args)
d) protected static void main(String[] args)
e) public static void main(int argc, String[] args)
2 ) E s c o l h aao p ç ã oa d e q u a d ap a r ac o m p i l a rer o d a roa r q u i v oA.java, ex-
istentenodiretório b:
29

## Página 35

3.3. CrieaplicaçõesJavaexecutáveiscomummétodomain CasadoCódigo
1 package b;
2 class A{
3 public static void main(String[] args){
4 System.out.println("rodando");
5 }
6 }
a) javac A e java A
b) javac A.java e java A
c) javac b/A.java e java A
d) javac b/A.java e java b.A
e) javac b.A.java e java b.A
f) javac b.A e java b.A
3) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 System.out.println(args);
4 System.out.println(args.length);
5 System.out.println(args[0]);
6 }
7 }
a) N ãoco m p ila:arra ynãopossuimemb r olength.
b) Não compila: o métodoprintlnnãoconsegueimprimirumarray.
c) Aorodarsemargumentos,ocorreuma NullPointerExceptionna
linha5.
d) Aorodarsemargumentos,ocorreuma NullPointerExceptionna
linha4.
e) Aorodarsemargumentos,sãoimpressososvalores“1”e“A”.
f) Aorodarcomoargumento“certificacao”,sãoimpressososvalores“2”
e“ A ” .
30

## Página 36

CasadoCódigo Capítulo3. ObásicodeJava
4) Escolha a opção adequada para rodar a classeA.java presente no di-
retório b,quefoicompactadoemumarquivochamado programa.jar,
sendoquenãoexistenenhumarquivodemanifesto:
1 package b;
2 class A{
3 public static void main(String[] args){
4 System.out.println(args[0]);
5 }
6 }
a) java jar programa.jar
b) java jar programa.jar b.A
c) java -jar programa.jar
d) java -jar programa.jar b.A
e) java -cp programa.jar
f) java -cp programa.jar b.A
5) Escolhaaopçãoadequadaparacompilaraclasse A.java,definidacomo
no pacote b presente no diretório b, e adicionar também o arquivo
programa.jarnabuscadeclassesduranteacompilação. Lembre-seque
.significaodiretórioatual.
a) javac -cp b.A.java -cp programa.jar
b) javac -jar programa.jar b.A.java
c) javac -cp programa.jar:b A.java
d) javac -cp programa.jar:. b.A.java
e) javac -cp . -cp programa.jar
f) javac -jar programa.jar:. b/A.java
g) javac -cp programa.jar:b b/A.java
h) javac -cp programa.jar:. b/A.java
31

## Página 37

3.4. ImporteoutrospacotesJavaedeixe-osacessíveisaoseucódigo CasadoCódigo
3.4 Importe outros pacotes Java e deixe-os
acessíveisaoseucódigo
Se duas classes estão no mesmo pacote, elas se “enxergam” entre si, sem a
necessidadedecolocaronomedopacote. Porexemplo,imaginequeasclasses
Pessoae Enderecoestejamnomesmopacote:
1 package modelo;
2
3 class Endereco {
4 String rua ;
5 String numero ;
6 String bairro ;
7 //...
8 }
Eoo u tr oar quivo:
1 package modelo;
2
3 class Pessoa {
4 Endereco endereco ; // Pessoa usando o endereço
5 }
Parausarumaclassequeestáemoutropacote,temosduasopções: pode-
mosreferenciá-lausandooquechamamosde Full Qualified Name ,ou
seja,onomedopacoteseguidodonomedaclasse. Ocódigoficariaassim:
1 package financeiro;
2
3 class Pedido {
4 modelo.Pessoa cliente; // Usando a classe Pessoa de outro
5 // pacote
6 }
Tentamoscompilarmaselenãodeixa,porqueumaclasse,porpadrão,só
podeseracessadadentrodoprópriopacote,eanossaclasse Pessoaestáno
pacote modelo. Portanto, definiremos nossa classePessoa como pública.
Veremoscommaiscalmaosmodificadoresdeacessonaseçãoquecobraisso
32

## Página 38

CasadoCódigo Capítulo3. ObásicodeJava
na prova. Por enquanto, basta lembrar que classes públicas podem ser aces-
sadasporoutrospacotes,jáclassespadrãonãopodem.
1 package modelo ;
2
3 public class Pessoa {
4 Endereco endereco // Pessoa usando o endereço
5 }
O u t r ao p ç ã oéi m p o r t a rac l a s s eProduto e referenciá-la apenas pelo
nome simples dentro de nosso código. Para fazer oimport usamos a palavra
import, seguida do Full Qualified Name da classe. A instrução de
importdeveaparecernaclasselogoapóso package(seesteexistir),eantes
dadefiniçãodaclasse. Épossívelimportarmaisdeumaclasseporvez:
1 package modelo ;
2
3 // Importando a classe Produto do pacote estoque
4 import estoque.Produto;
5 // Outro import qualquer
6 import java.util.Date;
7
8 class Pedido {
9 Pessoa cliente; // mesmo pacote
10 Produto item; // importado
11 Date dataEmissao; //importado
12 }
Tambémépossívelimportartodasasclassesdeumdeterminadopacote,
bastausarum * a pósono medopaco te:
1 // Importando todas as classes do pacote estoque
2 import estoque.*;
Importandoclassescommesmonome
Quandoprecisamosusarduasclassescomomesmonomemasdepacotes
diferentes, só podemos importar uma delas. A outra deve ser referenciada
pelo
Full Qualified Name . Tentativas de importar as duas classes irão
resultaremerrosdecompilação:
33

## Página 39

3.4. ImporteoutrospacotesJavaedeixe-osacessíveisaoseucódigo CasadoCódigo
1 import java.util.Date;
2 import java.sql.Date; // Erro de compilação pois temos duas
3 // classes Date
4
5 class Teste {
6 Date d1 ;
7 Date d2 ;
8 }
Oco rr etoseria:
1 import java.util.Date;
2
3 class Teste {
4 Date d1 ; // java.util
5 java.sql.Date d2; // java.sql
6 }
Casotenhamosumimportespecíficoeumimportgenérico,oJavausao
específico:
import java.util.*;
import java.sql.Date;
class Teste{
Date d1 ; // java.sql
Date d2 ; // java.sql
}
Porpadrão,todasasclassesdopacote java.lang sãoimportadas. Um
pontoimportanteéquenenhumaclassedepacotequenãosejaopadrãopode
importarumaclassedopacotepadrão:
class Gerente {
}
package modelo;
classe Banco {
Gerente gerente ; // não compila pois não é possível importar
// tipos do pacote padrão de jeito *nenhum*
}
34

## Página 40

CasadoCódigo Capítulo3. ObásicodeJava
Pacotes
Nesta seção, entenderemos mais a fundo como funciona a declaração de
pacotes,ecomoissoinfluencianosimportsdasclasses.
Como já discutimos anteriormente, pacotes servem para organizar suas
classeseinterfaces. Elespermitemagruparcomponentesquetenhamalguma
relação entre si, além de garantir algum nível de controle de acesso a mem-
bros. Alémdeseremumadivisãológicaparaassuasclasses,ospacotestam-
bém definem uma separação física entre os arquivos de seu projeto, já que
espelhamaestruturadediretóriosdosarquivosdoprojeto.
Subpacoteseestruturadediretórios
Pacotessão usadospela JVMcomouma maneiradeencontrar asclasses
no sistema de arquivos, logo a estrutura de diretórios do projeto deve ser a
mesmadaestruturadepacotes. VamosusarcomoexemploaclassePessoa:
1 package projeto.modelo;
2
3 public class Pessoa {}
Oa r q u i v oPessoa.java deve estar localizado dentro do diretório
modelo, que deve estar dentro do diretorioprojeto, conforme a figura
aseguir:
Dizemos que modelo é um subpacote de projeto, já que está
dentro dele. Podemos ter vários subpacotes, como projeto.utils e
projeto.conversores, por exemplo. Usamos o caractere. como sepa-
radordepacotesesubpacotes.
35

## Página 41

3.4. ImporteoutrospacotesJavaedeixe-osacessíveisaoseucódigo CasadoCódigo
Convençõesdenomesparapacotes
Existem algumas convenções para nomes de pacotes. Elas não são obri-
gatórias,masgeralmentesãoseguidasparafacilitaroentendimentoeorgani-
zaçãodocódigo:
• Onomedopacotedevesertodoemletrasminúsculas;
• U mpaco tedeveco meçarco mosi tedaem p r esa,aoco n trário;
• A pósosi te,devevirop r o jeto;
• A pósop r o jeto ,aestru turaélivr e.
Importusandoclassesdeoutrospacotes
Existem diversas maneiras de referenciar uma classe de pacote diferente
emnossocódigo. Vamosanalisaressasopções:
FullQualifiedName
Podemos referenciar uma classe em nosso código usando o que
chamamos deFull Qualified Name,o uFQN.E l eéc o m p o s t op e l opacote
completomaiso nomedaclasse ,porexemplo:
1 class Pessoa {
2 // FQN da classe Calendar
3 java.util.Calendar dataDeNascimento;
4 }
import
Usaro FQNnemsempredeixaocódigolegível,portanto,emvezdeusaro
nomecompletodaclasse,podemosimportá-laeusarapenasonomesimples
daclasse:
1 import java.util.Calendar;
2
3 class Pessoa {
4 Calendar dataDeNascimento ;
5 }
36

## Página 42

CasadoCódigo Capítulo3. ObásicodeJava
Épermitidotambémimportartodasasclassesdeumpacotedeumavez,
usandoo * nol ugardono medaclasse:
1 import java.util.*;
2
3 class Pessoa {
4 // Calendar e List são do pacote java.util
5 Calendar dataDeNascimento ;
6 List<String> apelidos;
7 }
Casoexistamduasclassescomomesmonome,masdepacotesdiferentes,
sópodemosimportarumadelas. Aoutradeveserreferenciadapelo FQN:
1 import java.util.Date;
2
3 class Foo {
4 //do java.util
5 Date some ;
6 java.sql.Date other;
7 }
]
Multiplosimportscom*
Caso importemos dois ou mais pacotes que contenham classes com
o mesmo nome, será obrigatório especificar, usando oFQN,q u a ld a s
classesqueremosutilizar. Aotentarusarapenasonomesimplesdaclasse,
ter emosumerr odeco m p ilação:
1 import java.util.*;
2 import java.sql.*;
3
4 public class Testes {
5 private Date d; // Erro de compilação, de qual pacote é
6 // para usar?
7 }
37

## Página 43

3.4. ImporteoutrospacotesJavaedeixe-osacessíveisaoseucódigo CasadoCódigo
Importdesubpacotes
Em Java, não podemos importar todas as classes de subpacotes usando
*. Vejaaseguintesituação,considerandoquecadaclassefoidefinidaemseu
próprioarquivo:
1 package sistema .prova;
2
3 public class Pergunta {}
1 package sistema .banco;
2
3 public class PerguntaDao {}
1 package sistema ;
2
3 public class Exame {}
1 package sistema .teste;
2
3 import sistema.*; //só importou a classe Exame
4
5 public class Teste {}
Oúnicomododeimportartodasasclasseséexplicitamenteimportando
cadasubpacote:
1 package sistema .teste;
2
3 import sistema.*;
4 import sistema.prova.*;
5 import sistema.banco.*;
6 public class Teste {}
importstatic
Desde o Java 5, é possível importar apenas métodos e atributos estáticos
deumaclasse,usandoapalavra-chave staticjuntamentecomo import.
Podemosimportarumaumousimplesmenteimportartodosusando * :
38

## Página 44

CasadoCódigo Capítulo3. ObásicodeJava
1 package model;
2
3 public class Utils {
4
5 // Atributo estático público
6 public static int VALOR =0 ;
7 // Métodos estáticos públicos
8 public static void metodo1() {}
9 public static void metodo1(int a){ }
10
11 }
1 // Importando todos os membros public static de Utils
2 import static model.Utils.*;
3
4 public class Testes {
5
6 public static void main(String[] args){
7 int x = VALOR;
8 metodo1();
9 metodo1(x);
10 }
11 }
1) Escolha a opção adequada ao tentar compilar e rodar oTeste.A r q u i v o
nodiretórioatual:
1 import modelo.Cliente;
2 class Teste {
3 public static void main(String[] args){
4 new Cliente("guilherme").imprime();
5 }
6 }
Arquivonodiretório modelo:
1 package modelo ;
2
3 class Cliente {
39

## Página 45

3.4. ImporteoutrospacotesJavaedeixe-osacessíveisaoseucódigo CasadoCódigo
4 private String nome;
5 Cliente(String nome ){
6 this.nome = nome;
7 }
8 public void imprime() {
9 System.out.println(nome);
10 }
11 }
a) N ãoco m p ila:err onaclasseTeste.
b) N ãoco m p ila:err onaclasseCliente.
c) Errodeexecução: método main.
d) Rodaeimprime“Guilherme”.
2) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 import modelo.basico.Cliente;
2 import modelo.avancado.Cliente;
3
4 class Teste {
5 public static void main(String[] args){
6 System.out.println("Bem vindo!");
7 }
8 }
a) O código não compila, erro ao tentar importar duas classes com o
mesmonome.
b) Ocódigocompila,masaorodardáerroporterimportadoduasclasses
comomesmonome.
c) Ocódigocompilaerodaimprimindo Bem vindo! ,umavezquenen-
huma das classes importadas é usada no código, não existe ambigu-
idade.
3) Escolha a opção adequada ao tentar compilar e rodar o arquivo a seguir,
sabendo que existem duas classesCliente, uma no pacotebasico e
o u tranopaco teavancado:
40

## Página 46

CasadoCódigo Capítulo3. ObásicodeJava
1 import modelo.basico.Cliente;
2 import modelo.avancado.*;
3
4 class Teste {
5 public static void main(String[] args){
6 System.out.println("Bem vindo!");
7 }
8 }
a) O código não compila, erro ao tentar importar duas classes com o
mesmonome.
b) Ocódigocompilamasaorodardáerroporterimportadoduasclasses
comomesmonome.
c) Ocódigocompilaerodaimprimindo Bem vindo! .
4) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 import modelo.basico.Cliente;
2 import modelo.basico.Cliente;
3
4 class Teste {
5 public static void main(String[] args){
6 System.out.println("Bem vindo!");
7 }
8 }
a) O código não compila, erro ao tentar importar duas classes com o
mesmonome.
b) Ocódigocompila,masaorodardáerroporterimportadoduasclasses
comomesmonome.
c) Ocódigocompilaerodaimprimindo Bem vindo! ,umavezquenão
háambiguidade.
5) Escolhaaopçãoadequadaaotentarcompilarosarquivosaseguir:
a/A.java:
41

## Página 47

3.4. ImporteoutrospacotesJavaedeixe-osacessíveisaoseucódigo CasadoCódigo
1 package a;
2 class A{
3 b.B variavel;
4 }
a/C.java:
1 package a;
2 class C{
3 b.B variavel;
4 }
a/b/B.java
:
1 package a.b;
2 class B{
3 }
a) ErrodecompilaçãosomentenoarquivoA.
b) ErrodecompilaçãosomentenoarquivoB.
c) ErrodecompilaçãosomentenoarquivoC.
d) Err odeco m p ilaçãonosar quivosAeB .
e) Err odeco m p ilaçãonosar quivosAeC.
f) Err odeco m p ilaçãonosar quivosBeC.
g) Compilacomsucesso.
6) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 package A;
2 class B{
3 public static void main(String[] a){
4 System.out.println("rodei");
5 }
6 }
a) Nãocompila: avariáveldométodo maindevesechamar args.
42

## Página 48

CasadoCódigo Capítulo3. ObásicodeJava
b) Nãocompila: pacotecomletramaiúscula.
c) Co m p ilamasnãor oda:aclasseBnãoép ública.
d) Compilaeroda.
7) Escolhaaopçãoadequadaaotentarcompilarosarquivosaseguir:
a/A.java:
1 package a;
2 public class A{
3 public static final int VALOR = 15;
4 public void executa(int x){
5 System.out.println(x);
6 }
7 }
b/B.java:
1 package b;
2 import static a.A.*;
3 class B{
4 void m() {
5 Aa = new A();
6 a.executa( VALOR);
7 }
8 }
a) Bnãocompila: erronalinha2.
b) Bnãocompila: erronalinha5.
c) Bnãocompila: erronalinha6.
d) Tudocompila.
8) Escolhaaopçãoadequadaaotentarcompilarosarquivosaseguir:
a/A.java:
43

## Página 49

3.4. ImporteoutrospacotesJavaedeixe-osacessíveisaoseucódigo CasadoCódigo
1 package a;
2 public class A{
3 public static final int VALOR = 15;
4 public void executa(int x){
5 System.out.println(x);
6 }
7 }
b/B.java:
1 package b;
2 import a.A;
3 static import a.A.*;
4 class B{
5 void m() {
6 Aa = new A();
7 a.executa(VALOR);
8 }
9 }
a) Bnãocompila: erronalinha3.
b) Bnãocompila: erronalinha5.
c) Bnãocompila: erronalinha6.
d) Tudocompila.
9) Escolhaaopçãoadequadaaotentarcompilarosarquivosaseguir:
A.java:
1 public class A{
2 public static final int VALOR = 15;
3 public void executa(int x){
4 System.out.println(x);
5 }
6 }
b/B.java
:
44

## Página 50

CasadoCódigo Capítulo3. ObásicodeJava
1 package b;
2 import static A.*;
3 class B{
4 void m() {
5 Aa= new A();
6 a.executa( VALOR);
7 }
8 }
a) Não compila
b) Tudocompila.
45

## Página 52

Capítulo4
Trablhandocomtiposdedados
emJava
4.1 Declarareinicializarvariáveis
Qualquer programa de computador precisa manter informações de alguma
forma. As linguagens de programação permitem a criação de variáveis para
quepossamosarmazenarinformações. Porexemplo,seprecisarmosguardar
aidadedeumapessoa,podemosutilizarumavariávelquesejacapazdeman-
ternúmerosinteiros.
Quando precisamos de uma nova variável, devemos declarar que quere-
mos criá-la. A declaração de variável no Java, obrigatoriamente, deve infor-
mar otipoeonome que desejamos para ela. Por isso, essa linguagem é dita
explicitamentetipada (todasasvariáveisprecisamteroseutipodefinido).

## Página 53

4.1. Declarareinicializarvariáveis CasadoCódigo
// Declaração de uma variável chamada idade do tipo primitivo int
int idade;
Nemtodalinguagemexigequeasvariáveissejaminiciadasantesdeserem
utilizadas. Mas,noJava,a inicializaçãoéobrigatória epodeserimplícitaou
explícita. Édefundamentalimportânciasaberque,parausarumavariável,é
necessário que ela tenha sido iniciadaexplicitamente ou implicitamente em
algummomentoantesdasuautilização.
Variáveis locais (declaradas dentro de métodos/construtores) devem ser
iniciadasantesdeseremutilizadas,outeremosumerrodecompilação:
// Declaração
int idade;
System.out.println(idade); // erro de compilação
// Declaração
int idade;
// Inicialização explícita de uma variável
idade =10;
// Utilização da variável
System.out.println(idade); // ok
Podemosdeclarareiniciaravariávelnamesmainstrução:
// Declaração e inicialização explícita na mesma linha
double pi =3.14;
Se eu tenho umif, a inicialização deve ser feita em todos os caminhos
possíveis:
void metodo(int a){
double x;
if(a >1 ){
x =6;
}
System.out.println(x); // talvez x não tenha sido
// inicializado, portanto não compila
}
48

## Página 54

CasadoCódigo Capítulo4. TrablhandocomtiposdedadosemJava
Quandoavariávelémembrodeumaclasse,elaéiniciadaimplicitamente
juntocomoobjetocomumvalor default:
class Prova {
double tempo;
}
// Implicitamente, na criação de um objeto Prova,
// o atributo tempo é iniciado com 0
Prova prova = new Prova();
// Utilização do atributo tempo
System.out.println(prova.tempo);
Outro momento em que ocorre a inicialização implícita é na criação de
arrays:
int[] numeros = new int [10];
System.out.println(numeros[0]); // imprime 0
Quandoiniciadasimplicitamente,osvaloresdefaultparaasvariáveissão:
• primitivosnuméricosinteiros 0
• primitivosnuméricoscompontoflutuante 0.0
• boolean false
• char vazio,equivalen tea0
• referênciasnull
OstiposdasvariáveisdoJavapodemserclassificadosemduascategorias:
primitivosenãoprimitivos(referências).
49

## Página 55

4.1. Declarareinicializarvariáveis CasadoCódigo
Tiposprimitivos
TodosostiposprimitivosdoJavajáestãodefinidosenãoépossívelcriar
novos tipos primitivos. São oito os tipos primitivos do Java:byte, short,
char, int, long, float, doublee boolean.
O boolean é o único primitivo não numérico. Todos os demais ar-
mazenam números: double e float são ponto flutuante, e os demais, to-
dos inteiros (incluindo char). Apesar de representar um caractere, o tipo
char armazena seu valor como um número positivo. Em Java, não é pos-
sível declarar variáveis com ou sem sinal (unsigned), todos os números (ex-
ceto char)podemserpositivosenegativos.
Cadatipoprimitivoabrangeumconjuntodevalores. Porexemplo,otipo
byte abrange os números inteiros de -128 até 127. Isso depende do tamanho
embytesdotiposendousado.
Ostiposinteirostêmosseguintestamanhos:
• byte 1byte(8bits,de-128a127);
• short 2bytes(16bits,de–32.768a32.767);
• char 2b ytes(sóposi tivo),(16b i ts,de0a65.535);
• int 4bytes(32bits,de–2.147.483.648a2.147.483.647);
• long 8 bytes (64 bits, de –9.223.372.036.854.775.808 a
9.223.372.036.854.775.807).
Decorarotamanhodosprimitivosparaprova
Não há a necessidade de decorar o intervalo e tamanho de todos os
tiposdeprimitivosparaaprova. Oúnicointervalocobradoéodo byte
(-127a128).
É importante também saber que ochar, apesar de ter o mesmo
tamanhodeum short,nãoconseguearmazenartodososnúmerosque
cabememum short,jáqueo charsóarmazenanúmerospositivos.
50

## Página 56

CasadoCódigo Capítulo4. TrablhandocomtiposdedadosemJava
Parasabermais:calculandoointervalodevalores
Dadoonúmerodebits Ndotipoprimitivointeiro,parasaberosval-
oresqueeleaceitausamosaseguinteconta:
-2^(n-1) a 2^(n-1) -1
O char,porserapenaspositivo,temintervalo:
0 a 2^(16) -1
Ostipospontoflutuantetêmosseguintestamanhosemnotaçãocientífica:
• float 4bytes(32bits,de+/–1.4*10^45a+/–3.4028235*10^38);
• double 8 bytes (64 bits, de +/–4.9 * 10 ^324 a +/–1.7976931348623157
*10^308).
Todos os números de ponto flutuante também podem assumir os
seguintesvalores:
• +/–infinity
• +/-0
• NaN(NotaNumber)
Literais
Na codificação, muitas vezes o programador coloca os valores das var-
iáveisdiretamentenocódigo-fonte. Quandoissoocorre,dizemosqueovalor
foiliteralmenteescritonocódigo,ouseja,éum valorliteral.
Todososvaloresprimitivosmaioresque intpodemserexpressosliteral-
mente. Poroutrolado,asreferências(valoresnãoprimitivos)nãopodemser
expressasdemaneiraliteral(nãoconseguimoscolocardiretoosendereçosde
memóriadosobjetos).
Aoinicializarumavariável,podemosexplicitarquequeremosqueelaseja
dotipo
doubleou longusandoaletraespecífica:
51

## Página 57

4.1. Declarareinicializarvariáveis CasadoCódigo
// compila pois 737821237891232 é um double válido
System.out.println(737821237891232d);
// compila pois 737821237891232 é um longválido
System.out.println(737821237891232l);
// nao compila pois 737821237891232 é um valor maior que
// o int aceita
System.out.println(737821237891232);
Damesmamaneira, ocompiladoréumpoucoespertoepercebesevocê
tentaquebrarolimitedeum intmuitofacilmente:
// compila pois 737821237891232l é um longválido
long l = 737821237891232l;
// não compila pois o compilador não é bobo assim
int i = l;
// booleanos
System.out.println(true); // booleano verdadeiro
System.out.println(false); // booleano falso
// números simples são considerados inteiros
System.out.println(1); // int
// números com casa decimal são considerados double.
// Também podemos colocar uma letra "D" ou "d" no final
System.out.println(1.0); //double
System.out.println(1.0D); //double
// números inteiros com a letra "L" ou "l"
// no final são considerados long.
System.out.println(1L); //long
// números com casa decimal com a letra "F" ou "f"
// no final são considerados float.
System.out.println(1.0F); //float
52

## Página 58

CasadoCódigo Capítulo4. TrablhandocomtiposdedadosemJava
Basesdiferentes
Nocasodosnúmerosinteiros,podemosdeclararusandobasesdiferentes.
OJ a vasu po rtaabasedecimalemaisasbasesoctal ,hexadecimalebinária.
Um número na base octal tem que começar com um zero à esquerda e
podeusara penasosalgarismosde0a7:
int i = 0761; // base octal
System.out.println(i); // saída: 497
E na hexadecimal, começa com0x ou 0X eu s ao sa l g a r i s m o sd e0a1 5 .
Como não existe um algarismo “15”, usamos letras para representar algaris-
mosde“10”a“1 5” ,nocaso ,“ A ”a“ F” ,mai úsculaso umin úsculas:
int j =0 xAB3400; // base hexadecimal
System.out.println(j); // saída: 11219968
Jánabasebinária,começamoscom 0b,esópodemosusar“0”e“1":
int b =0 b100001011; // base binária
System.out.println(b); // saída: 267
Não é necessário aprender a fazer a conversão entre as diferentes bases
ead e c i m a l .A p e n a ss a b e rq u a i ss ã oo sv a l o r e sp o s s í v e i se mc a d ab a s e ,p a r a
identificarerrosdecompilaçãocomooquesegue:
int i = 0769; // erro, base octal não pode usar 9
Notaçãocientífica
Aodeclarar doublesou floats,podemosusaranotaçãocientífica:
double d = 3.1E2;
System.out.println(d); // 310.0
float e =2 e3f;
System.out.println(e); // 2000.0
float f =1 E4F;
System.out.println(f); // 10000.0
53

## Página 59

4.1. Declarareinicializarvariáveis CasadoCódigo
Usandounderlinesemliterais
ApartirdoJava7,existeapossibilidadedeusarmos underlines( _)quando
estamosdeclarandoliteraisparafacilitaraleituradocódigo:
int a = 123_456_789;
Existemalgumasregrassobreondeesses underlinespodemserposiciona-
dos nos literais, e caso sejam colocados em locais errados resultam em erros
decompilação. Aregrabásicaéqueelessópodemserposicionadoscom val-
oresnuméricosemambososlados . Vamosveralgunsexemplos:
int v1 =0 _100_267_760 ; // ok
int v2 =0 _x_4_13; // erro, _ antes e depois do x
int v3 =0 b_x10_BA_75; // erro, _ depois do b
int v4 =0 b_10000_10_11; // erro, _ depois do b
int v5 = 0xa10 _AF_75; // ok, apesar de ser letra
// representa dígito
int v6 = _123_341; // erro, inicia com _
int v7 = 123_432_; // erro, termina com _
int v8 = 0x1_0A0_11; // ok
int v9 = 144__21_12; // ok
Amesmaregraseaplicaanúmerosdepontoflutuante:
double d1 = 345.45 _e3; // erro, _ antes do e
double d2 = 345.45 e_3; // erro, _ depois do e
double d3 = 345.4 _5e3; // ok
double d4 =3 4 _5.45e3_2; // ok
double d5 =3 _4_5.4_5e3; // ok
double d6 = 345._45F; // erro, _ depois do .
double d7 = 345_.45; // erro, _ antes do .
double d8 = 345.45 _F; // erro, _ antes do indicador de
// float
double d9 = 345.45 _d; // erro, _ antes do indicador de
// double
54

## Página 60

CasadoCódigo Capítulo4. TrablhandocomtiposdedadosemJava
Iniciandochars
Os chars são iniciados colocando o caractere desejado entreaspassim-
ples:
char c = 'A';
Mas podemos iniciar com números também. Neste caso, o número rep-
resentaaposiçãodocaracterenatabelaunicode:
char c = 65;
System.out.println(c); // imprime A
Nãoénecessáriodecoraratabelaunicode,maséprecisoprestaratenção
apegadinhascomoaseguinte:
char sete =7 ; // número, pois não está entre aspas simples
System.out.println(sete); // Não imprime nada!!!!
Quando usando programas em outras línguas, às vezes queremos usar
caracteresunicode, masnãotemosumtecladocomtaisteclas(árabe, chinês
etc.). Neste caso, podemos usar uma representação literal de um caractere
unicodeemnossocódigo,iniciandoo
charcom \u:
char c = '\u03A9'; // unicode
System.out.println(c); // imprime a letra grega ômega
Identificadores
Quando escrevemos nossos programas, usamos basicamente dois tipos
determosparacompornossocódigo: identificadoresepalavrasreservadas.
Chamamos deidentificadores as palavras definidas pelo programador
paranomearvariáveis,métodos,construtores,classes,interfacesetc.
Jápalavrasreservadas oupalavras-chavesãotermospredefinidosdalin-
guagem que podemos usar para definir comandos (if, for, class,e n t r e
outras).
Sãodiversaspalavras-chavenalinguagemjava:
• abstract
55

## Página 61

4.1. Declarareinicializarvariáveis CasadoCódigo
• assert
• boolean
•b r e a k
• byte
•c a s e
• catch
•c h a r
•c l a s s
•c o n s t
•c o n t i n u e
• default
•d o
•d o u b l e
•e l s e
•e n u m
• extends
•f a l s e
•fi n a l
• finally
•fl o a t
•f o r
•g o t o
56

## Página 62

CasadoCódigo Capítulo4. TrablhandocomtiposdedadosemJava
•i f
• implements
•i m p o r t
•i n s t a n c e o f
•i n t
• interface
•l o n g
•n a t i v e
•n e w
• null
• package
•p r i v a t e
•p r o t e c t e d
• public
• return
• short
•s t a t i c
• strictfp
•s u p e r
• switch
• synchronized
• this
57

## Página 63

4.1. Declarareinicializarvariáveis CasadoCódigo
•t h r o w
• throws
• transient
•t r u e
•t r y
•v o i d
• volatile
• while
null,falseetrue
Outras três palavras reservadas que não aparecem nessa lista são
true, falsee null. Mas,segundoaespecificaçãonalinguagemJava,
essestrêstermossãoconsiderados literaisenãopalavras-chave(embora
tambémsejamreservadas),totalizando53palavrasreservadas.
http://java.sun.com/docs/books/tutorial/java/nutsandbolts/
_keywords.html
Identificadoresválidosdevemseguirasseguintesregras:
• Nãopodemserigualaumapalavra-chave;
• Podemusarletras(unicode),números,
$e _;
• Oprimeirocaractere nãopodeserumnúmero;
• Podempossuirqualquernúmerodecaracteres.
Os identificadores sãocase sensitive, ou seja, respeitam maiúsculas e
minúsculas:
58

## Página 64

CasadoCódigo Capítulo4. TrablhandocomtiposdedadosemJava
int umNome; // ok
int umnome; // ok, diferente do anterior
int _num; // ok
int $_ab_c; // ok
int x_y; // ok
int false ; // inválido, palavra reservada
int x-y; // inválido, traço
int 4num; // inválido, começa com número
int av#f; // inválido, #
int num.spc; // inválido, ponto no meio
1) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 int
4 idade
5 = 100;
6 System.out.println(idade);
7 }
8 }
a) Ocódigonãocompila: errosapartirdalinhaquedefineumavariável
dotipo int.
b) O código não compila: a variávelidade não foi inicializada, mas foi
usadaem System.out.println.
c) Ocódigoco m p ilaeim p rime0.
d) Ocódigocompilaeimprime100.
2) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 int idade;
4 if(args.length > 0) {
5 idade = Integer.parseInt(args[0]);
6 } else {
59

## Página 65

4.1. Declarareinicializarvariáveis CasadoCódigo
7 System.err.println("Por favor passe sua idade como
8 primeiro parâmetro" );
9 }
10 System.out.println("Sua idade é " + idade);
11 }
12 }
a) Nãocompila: erronalinhaquetentaacessaravariável idade.
b) Compilaeimprime0ouaidadequeforpassadanalinhadecomando.
c) Compilaeimprimeaidadequeforpassadanalinhadecomando.
d) Co m p ilaeim p rimeamensagemdeerr oo u“ S uaidadeé"eaidade.
3) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 boolean array = new boolean[300];
4 System.out.println(array[3]);
5 }
6 }
a) Imprime true.
b) Imprime false.
c) Imprime 0.
d) Imprime -1.
e) Imprime null.
f) Não compila.
4) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 boolean[] array = new boolean[300];
4 System.out.println(array[3]);
5 }
6 }
60

## Página 66

CasadoCódigo Capítulo4. TrablhandocomtiposdedadosemJava
a) Imprime true.
b) Imprime false.
c) Imprime 0.
d) Imprime -1.
e) Imprime null.
f) Não compila.
5) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 boolean argumentos;
4 if(args.length > 0)
5 argumentos =1;
6 else
7 argumentos =0 ;
8 System.out.println(argumentos);
9 }
10 }
a) Nãocompila: ométododeimpressãonãorecebe boolean.
b) Nãocompila: atribuiçãoinválida.
c) Não compila: o métodolengthdearraynãoéumapropriedade.
d) Não compila: o método length de String[]n ã oéu m ap r o -
priedade.
e) Compila e imprime0ou 1.
f) Compila e imprimefalseou true.
6) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 int n = 09;
4 int m = 03;
61

## Página 67

4.1. Declarareinicializarvariáveis CasadoCódigo
5 int x =1 _000;
6 System.out.println(x - n + m);
7 }
8 }
a) N ãoco m p ila:err onalinhaquedeclaran.
b) N ãoco m p ila:err onalinhaquedeclarax.
c) N ãoco m p ila:err onalinhaquedeclaram.
d) Compilaeimprimeumnúmeromenorque1000.
7) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 for(char c= 'a';c <= 'z';c++) {
4 System.out.println(c);
5 }
6 }
7 }
a) Nãocompila: nãopodemossomarumemumcaractere.
b) Nãocompila: nãopodemoscompararcaracterescom <.
c) Co m p ilaeim p rimeoalfabetoen tr eaez,incl usive.
8) QualdaspalavrasaseguirnãoéreservadaemJava?
a) strictfp
b) native
c) volatile
d) transient
e) instanceOf
9) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
62

## Página 68

CasadoCódigo Capítulo4. TrablhandocomtiposdedadosemJava
1 class A{
2 public static void main(String[] args){
3 boolean BOOLEAN = false;
4 if(BOOLEAN ){
5 System.out.println("Sim");
6 }
7 }
8 }
a) Nãocompila: nãopodemosdeclararumavariávelcomonomedeuma
palavrareservada.
b) Nãocompila: nãopodemosdeclararumavariáveliniciandocomletras
maiúsculas.
c) Compilaeroda,imprimindo Sim.
d) Compilaeroda,nãoimprimindonada.
4.2 Diferenciaentrevariáveisdereferênciasa
objetosetiposprimitivos
As variáveis de tipos primitivos de fato armazenam os valores (e não pon-
teiros/referências). Ao se atribuir o valor de uma variável primitiva a uma
o u travariá vel,ovalo réco p iado ,eoo riginalnãoéal terado:
int a = 10;
int b = a; // copiando o valor de a para b
b++; // somando 1 em b
System.out.println(a); // continua com 10.
Os programas construídos com o modelo orientado a objetos utilizam,
evidentemente, objetos. Para acessar um atributo ou invocar um método de
qualquerobjeto,énecessárioquetenhamosarmazenadauma referênciapara
omesmo.
Uma variável de referência é um ponteiro para o endereço de memória
ondeoobjetoseencontra. Aoatribuirmosumavariáveldereferênciaaoutra,
estamos copiando a referência, ou seja, fazendo com que as duas variáveis
a po n temparaomesmoob jeto ,enãocriandoumno voob jeto:
63

## Página 69

4.2. Diferenciaentrevariáveisdereferênciasaobjetosetiposprimitivos CasadoCódigo
class Objeto {
int valor;
}
class Teste{
public static void main(String[] args){
Objeto a = new Objeto();
Objeto b = a; // agora b aponta para o mesmo objeto de a
a.valor = 5;
System.out.println(b.valor); // imprime 5
}
}
Duasreferênciassãoconsideradasiguaissomenteseelasestãoapontando
para o mesmo objeto. Mesmo que os objetos que elas apontem sejam iguais,
aindasãoreferênciasparaobjetosdiferentes:
Objeto a = new Objeto();
a.valor = 5;
Objeto b = new Objeto();
b.valor = 5;
Objeto c = a;
System.out.println(a == b); // false
System.out.println(a == c); // true
Veremos bastante sobre comparação de tipos primitivos e de referências
maisàfrente.
1) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 int x = 15;
4 int y = x;
64

## Página 70

CasadoCódigo Capítulo4. TrablhandocomtiposdedadosemJava
5 y++;
6 x++;
7 int z = y;
8 z--;
9 System.out.println(x + y + z);
10 }
11 }
a) Imprime43.
b) Imprime44.
c) Imprime45.
d) Imprime46.
e) Imprime47.
f) Imprime48.
g) Imprime49.
2) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{
2 int v = 15;
3 }
4 class A{
5 public static void main(String[] args){
6 Bx = new B();
7 By = x;
8 y.v++;
9 x.v++;
10 Bz = y;
11 z.v--;
12 System.out.println(x.v + y.v + z.v);
13 }
14 }
a) Imprime43.
b) Imprime44.
c) Imprime45.
65

## Página 71

4.3. Leiaouescrevaparacamposdeobjetos CasadoCódigo
d) Imprime46.
e) Imprime47.
f) Imprime48.
g) Imprime49.
4.3 Leiaouescrevaparacamposdeobjetos
Ler e escrever propriedades em objetos é uma das tarefas mais comuns em
um programa java. Para acessar um atributo, usamos o operador. (ponto),
juntoaumavariáveldereferênciaparaumobjeto. Vejaaseguinteclasse:
class Carro {
String modelo ;
int ano;
public Carro() { ano = 2014; }
public String getDadosDeImpressao() {
return modelo + "-" + ano;
}
public void setModelo(String m ){
this.modelo = m;
}
}
V amosescr everumcódigoparausaressaclasse:
1 Carro a = new Carro();
2 a.modelo = "Palio" ; // acessando diretamente o atributo
3 a.setModelo("Palio"); // acessando o atributo por um método
4
5 // acessando o método e passando o retorno como argumento para
6 // o método println
7 System.out.println(a.getDadosDeImpressao());
8
9 }
66

## Página 72

CasadoCódigo Capítulo4. TrablhandocomtiposdedadosemJava
As linhas 2 e 3 têm exatamente o mesmo efeito. Como iniciamos o valor
dapropriedade anonoconstrutor,aochamarométodo imprimeDados,o
valor 2014éexib idojun toaono medomodelo .
Quando estamos dentro da classe, não precisamos de nenhum operador
para acessar os atributos de instância da classe. Opcionalmente, podemos
usar a palavra-chavethis, que serve como uma variável de referência para
opróprioobjetoondeocódigoestásendoexecutado:
class Carro{
int ano;
int modelo;
public Carro(){
modelo = "Indefinido"; // acessando variável de
// instancia sem o this
this.ano = 2014; // acessando com o this.
}
1) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{
2 int c;
3 void c(int c){
4 c = c;
5 }
6 }
7 class A{
8 public static void main(String[] args){
9 Bb = new B();
10 b. c=10 ;
11 System.out.println(b.c);
12 b.c(30);
13 System.out.println(b.c);
14 }
15 }
a) Nãocompila: conflitodenomedevariávelmembroemétodoemB.
67

## Página 73

4.4. Expliqueociclodevidadeumobjeto(criação,“dereferência”egarbagecollection) CasadoCódigo
b) Nãocompila: conflitodenomedevariávelmembroevariávellocalem
B.
c) Compilaeroda,imprimindo10e30.
d) Compilaeroda,imprimindooutroresultado.
4.4 Expliqueociclodevidadeumobjeto(cri-
ação,“dereferência”egarbagecollection)
O ciclo de vida dos objetos java está dividido em três fases distintas. Vamos
conhecê-laseentenderoquecadaumasignifica.
Criaçãodeobjetos
Todavezqueusamosooperador new,estamoscriandoumanovainstân-
ciadeumob jetonamemó ria:
class Pessoa {
String nome ;
}
class Teste {
public static void main(String[] args){
Pessoa p = new Pessoa(); // criando um novo objeto do
// tipo Pessoa
}
}
Reparequeháumagrandediferençaentrecriarumobjetoedeclararuma
variável. A variável é apenas uma referência, um ponteiro, não contém um
objetodeverdade.
// Apenas declarando a variável,
// nenhum objeto foi criado aqui
Pessoa p ;
// Agora um objeto foi criado e atribuído a variável
p = new Pessoa();
68

## Página 74

CasadoCódigo Capítulo4. TrablhandocomtiposdedadosemJava
Objetoacessível
Apartirdomomentoemqueumobjetofoicriadoeatribuídoaumavar-
iável,dizemosqueoobjetoestá acessível,ouseja,podemosusá-loemnosso
programa:
Pessoa p = new Pessoa(); // criação
p.nome = "Mário"; // acessando e usando o objeto
Objetoinacessível
Um objeto é acessível enquanto for possível “alcançá-lo” através de al-
gumareferênciadiretaouindireta. Casonãoexistanenhumcaminhodireto
ouindiretoparaacessaresseobjeto,elesetorna inacessível.:
1 Pessoa p = new Pessoa();
2 p.nome = "Mário";
3
4 // atribuímosapovalor null
5 // o objeto não está mais acessível
6 p = null
7
8 // criando um objeto sem variável
9 new Pessoa();
N e s s ec ó d i g o ,c r i a m o su mo b j e t od ot i p oPessoa e o atribuímos à var-
iável p. Na linha6 atribuímos null a p. O que acontece com o objeto
anterior? Elesimplesmentenãopodemaisseracessadopornossoprograma,
poisnãotemosnenhumponteiroparaele. Omesmopodeserditodoobjeto
criadonalinha 9. Apósessalinha,nãoconseguimosmaisacessaresseobjeto.
Outramaneiradeterumobjetoinacessíveléquandooescopodavariável
queapontaparaeletermina:
int valor = 100;
if( valor > 50) {
Pessoa p = new Pessoa();
p.nome = "João";
} // Após esta linha, o objeto do tipo Pessoa não está mais
// acessível
69

## Página 75

4.4. Expliqueociclodevidadeumobjeto(criação,“dereferência”egarbagecollection) CasadoCódigo
GarbageCollector
Todoobjetoinacessíveléconsideradoelegívelparao garbagecollector.A l -
gumasquestõesdaprovaperguntamquantosobjetossãoelegíveisaogarbage
collectoraofinaldealgumtrechodecódigo:
public class Bla {
int b;
public static void main(String[] args){
Bla b;
for (int i =0 ; i < 10; i++) {
b = new Bla();
b.b = 10;
}
System.out.println("fim");
}
}
Aochegarnalinha 9,temos 9objetoselegíveisparaoGarbageCollector.
ObjetoselegíveisXObjetoscoletados
Ogarbagecollector rodaemsegundoplanojuntamentecomsuaapli-
cação java. Não é possível prever quando ele será executado, portanto
não se pode dizer com certeza quantos objetos foram efetivamente co-
letados em um certo ponto da aplicação. O que podemos determinar
é quantos objetos são elegíveis para a coleta. A prova pode tentar se
aproveitar do descuido do desenvolvedor aqui: nunca temos certeza de
quantos objetos passaram pelo garbage collector, logo, somente indique
quantosestãopassíveisdeseremcoletados.
Porfim,éimportanteverumexemplodereferênciaindireta,noqualnen-
humobjetopodeser“garbagecoletado":
1 import java.util.*;
2 class Carro {
3
70

## Página 76

CasadoCódigo Capítulo4. TrablhandocomtiposdedadosemJava
4 }
5 class Carros {
6 List<Carro > carros = new ArrayList<Carro>();
7 }
8 class Teste {
9 public static void main(Stringarg s[]) {
10 Carros carros = new Carros();
11 for(int i =0 ; i < 100; i++)
12 carros.carros.add(new Carro());
13 // até essa linha todos ainda podem ser alcançados
14 }
15 }
Nesse código, por mais que tenhamos criados 100 carros e um objeto do
tipo Carros,nenhumdelespodesergarbagecoletadopoistodospodemser
alcançadosdiretaouindiretamenteatravésdenossa threadprincipal.
1) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{
2
3 }
4 class A{
5 public static void main(String[] args){
6 Bb ;
7 for(int i =0 ; i < 10;i++)
8 b = new B();
9 System.out.println("Finalizando!");
10 }
11 }
a) Não compila.
b) Compila e garbage coleta 10 objetos do tipo B na linha do
System.out.
c) Compilaenãopodemosfalarquantosobjetosdotipo Bforamgarbage
coletadosnalinhado System.out.
2) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
71

## Página 77

4.4. Expliqueociclodevidadeumobjeto(criação,“dereferência”egarbagecollection) CasadoCódigo
1 class B{
2
3 }
4 class A{
5 public static void main(String[] args){
6 Bb = new B();
7 for(int i =0 ; i <10;i++)
8 b = new B();
9 System.out.println("Finalizando!");
10 }
11 }
a) Não compila.
b) Compilae10objetosdotipo Bpodemsergarbagecoletadosaochegar
nalinhado System.out.
c) Compilae11objetosdotipo Bpodemsergarbagecoletadosaochegar
nalinhado System.out.
d) Compila e garbage coleta 11 objetos do tipo B na linha do
System.out.
3) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{
2
3 }
4 class A{
5 public static void main(String[] args){
6 B[] bs = new B[100];
7 System.out.println("Finalizando!");
8 }
9 }
a ) C o m p i l ae1 0 0o b j e t o sd ot i p oB são criados, mas não podemos falar
nada sobre o garbage collector ter jogado os objetos fora na linha do
System.out.
b) Co m p ilaenenh umob jetodoti poBécriado.
72

## Página 78

CasadoCódigo Capítulo4. TrablhandocomtiposdedadosemJava
c) Compila, cria 100 e joga fora todos os objetos do tipoB ao chegar no
System.out.
4.5 Chamemétodosemobjetos
Alémdeacessaratributos,tambémpodemosinvocarmétodosemumobjeto.
Para isso usamos o operador. (ponto), junto a uma variável de referência
paraumobjeto. Deve-seprestaratençãoaonúmeroetipodeparâmetrosdo
método,alémdoseuretorno. Métodosdeclaradoscomo
voidnãopossuem
retorno,logo,nãopodemseratribuídosanenhumavariáveloupassadopara
o u tr ométodoco moparâmetr o:
class Pessoa{
String nome ;
public String getNome(){
return nome;
}
public void setNome(String nome ){
this.nome = nome;
}
}
class Teste{
public static void main(String [] args){
Pessoa p = new Pessoa();
//chamando método na variável de ref.
p.setNome("Mario");
//Atribuindo o retorno do método a variável.
String nome = p.getNome();
// erro, método é void
String a = p.setNome( "X");
73

## Página 79

4.5. Chamemétodosemobjetos CasadoCódigo
}
}
Quandoummétodoestásendoinvocadoemumobjeto,podemoschamar
outro método no mesmo objeto através da invocação direta ao nome do
método:
class A{
void metodo1() {
metodo2(); // chama o metodo2 no objeto onde metodo1 foi
// chamado
}
void metodo2() {
}
}
Argumentosvariáveis:varargs
Ap a r t i rd oJ a v a5 ,varargs possibilitam um método que receba um
número variável (não fixo) de parâmetros. É a maneira de receber um array
deobjetosepossibilitarumachamadamaisfácildométodo.
Um caso especial é quando método recebe um argumento variável (
varargs). Neste caso, podemos chamá-lo com qualquer número de argu-
mentos:
class Calculadora{
public int soma(int... nums){
int total =0;
for (int a : nums){
total+= a;
}
return total;
}
}
nums realmente é um array aqui, você pode fazer umfor usando o
length,oumesmousaro enhanced for . Ainvocaçãodessemétodopode
serfeitadeváriasmaneiras:
74

## Página 80

CasadoCódigo Capítulo4. TrablhandocomtiposdedadosemJava
public static void main ( String[] args){
Calculadora c = new Calculadora();
//Todas as chamadas abaixo sao válidas
System.out.println(c.soma());
System.out.println(c.soma(1));
System.out.println(c.soma(1,2));
System.out.println(c.soma(1,2,3,4,5,6,7,8,9));
}
Em todos os casos, um array será criado, nuncanull será passado.
Umparâmetro varargsdevesersempreoúltimodaassinaturadométodo
paraevitarambiguidade. Issoimplicaqueapenasumdosparâmetrosdeum
métodoseja varargs.Ereparequeosargumen tosvariá veistêmqueserdo
mesmotipo.
EserádadaaprioridadeparaométodoquejápodiaexistirantesnoJava
1.4:
void metodo(int ... x ){}
void metodo(int x){ }
metodo(5);
Isso vai invocar o segundo método. Podemos também passar um array
de intsparaummétodoquerecebeum varargs:
void metodo(int ... x ){}
metodo(new int [] {1,2,3,4});
Mas nunca podemos chamar um método que recebe array como se ele
fosse varargs:
void metodo(int[] x){}
metodo(1,2,3); // não compila
1) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
75

## Página 81

4.5. Chamemétodosemobjetos CasadoCódigo
1 class B{
2 void x() {
3 System.out.println("vazio");
4 }
5 void x(String ... args){
6 System.out.println(args.length);
7 }
8 }
9 class C{
10 void x(String ... args){
11 System.out.println(args.length);
12 }
13 void x() {
14 System.out.println("vazio");
15 }
16 }
17 class A{
18 public static void main(String[] args){
19 new B().x();
20 new C().x();
21 }
22 }
a) Nãocompila: conflitoentremétodocom varargsesemargumentos.
b) Compilaeimprimevazio/vazio.
c) Compilaeimprimevazio/0.
d) Compilaeimprime0/vazio.
e) Compilaeimprime0/0.
2) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{
2 void x(int... x){
3 System.out.println(x.length);
4 }
5 }
6 class A{
76

## Página 82

CasadoCódigo Capítulo4. TrablhandocomtiposdedadosemJava
7 public static void main(String[] args){
8 new B().x(23789,673482);
9 }
10 }
a) Não compila: varargstemmétodoenãoa trib u tolength.
b) Compilaeaorodarimprimeosdoisnúmeros.
c) Co m p ilaeaor odarim p rime2.
3) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{
2 void x(int... x){
3 System.out.println(x.length);
4 }
5 }
6 class A{
7 public static void main(String[] args){
8 new B().x(new int []{23789,673482});
9 }
10 }
a) Não compila: varargstemmétodoenãoa trib u tolength.
b) Nãocompila: nãopodemospassarumarrayparaum varargs.
c) Compilaeaorodarimprimeosdoisnúmeros.
d) Co m p ilaeaor odarim p rime1.
e) Co m p ilaeaor odarim p rime2.
4) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{
2 void x(Object... x ){
3 System.out.println(x.length);
4 }
5 }
6 class A{
77

## Página 83

4.6. ManipuledadosusandoaclasseStringBuildereseusmétodos CasadoCódigo
7 public static void main(String[] args){
8 new B().x(new Object[]{23789,673482});
9 }
10 }
a) Não compila: varargstemmétodoenãoa trib u tolength.
b) Nãocompila: nãopodemospassarumarrayparaum varargs.
c) Compilaeaorodarimprimeosdoisnúmeros.
d) Co m p ilaeaor odarim p rime1.
e) Co m p ilaeaor odarim p rime2.
4.6 Manipule dados usando a classe String-
Buildereseusmétodos
Para suportar Strings mutáveis, o Java possui as classesStringBuffer e
StringBuilder. Aoperaçãomaisbásicaéo appendquepermiteconcate-
naraomesmoobjeto:
StringBuffer sb = new StringBuffer();
sb.append("Caelum");
sb.append("-" );
sb.append("Ensino e Inovação" );
System.out.println(sb); // Caelum - Ensino e Inovação
Reparaqueo appendnãodevolvenovosobjetoscomoem String,mas
alteraopróprio StringBuffer,queém u tá vel.
Podemoscriarumobjetodessetipodediversasmaneirasdiferentes:
// vazio
StringBuilder sb1 = new StringBuilder();
// conteudo inicial
StringBuilder sb2 = new StringBuilder("java");
// tamanho inicial do array para colocar a string
StringBuilder sb3 = new StringBuilder(50);
// baseado em outro objeto do mesmo tipo
StringBuilder sb4 = new StringBuilder(sb2);
78

## Página 84

CasadoCódigo Capítulo4. TrablhandocomtiposdedadosemJava
Tenhacuidado: aodefinirotamanhodoarray,nãoestamoscriandouma
Stringdetamanhodefinido,somenteumarraydessetamanhoqueseráuti-
lizadopelo StringBuilder,po rtan to:
StringBuilder sb3 = new StringBuilder(50);
System.out.println(sb3); // linha em branco
System.out.println(sb3.length()); // 0
Asclasses StringBuffere StringBuildertêmexatamenteamesma
interface (mesmos métodos), sendo que a primeira éthread-safeeaú l t i m a
não (e foi adicionada no Java 5). Quando não há compartilhamento entre
threads, use sempre que possível aStringBuilder,q u eém a i sr á p i dapo r
nãop r ecisarsep r eocu parco mlocks.
Inclusive,emJava,quandofazemosconcatenaçãodeStringsusandoo +,
por baixo dos panos, é usado umStringBuilder. Não existe a operação
+naclasse String.Ocompiladortrocatodasaschamadasdeconcatenação
por StringBuilders(podemosverissonobytecodecompilado).
PrincipaismétodosdeStringBuffereStringBuilder
Há a família de métodosappend com overloads para receber cada um
dos primitivos, Strings, arrays de chars, outrosStringBuffer etc. Todos
elesdevolvemopróprio StringBuffer/ Builderoquepermitechamadas
encadeadas:
StringBuffer sb = new StringBuffer();
sb.append( "Caelum").append("-" ).append("Ensino e Inovação" );
System.out.println(sb); // Caelum - Ensino e Inovação
O método append p o s s u iu m av e r s ã oq u er e c e b eObject e chama o
método toStringdeseuobjeto.
Há ainda os métodosinsert para inserir coisas no meio. Há versões
querecebemprimitivos,Strings,arraysdecharetc. Mastodostêmoprimeiro
argumentorecebendooíndiceondequeremosinserir:
StringBuffer sb = new StringBuffer();
sb.append( "Caelum - Inovação");
sb.insert(9, "Ensino e " );
79

## Página 85

4.6. ManipuledadosusandoaclasseStringBuildereseusmétodos CasadoCódigo
System.out.println(sb); // Caelum - Ensino e Inovação
Outro método que modifica é odelete, que recebe os índices inicial e
final:
StringBuffer sb = new StringBuffer();
sb.append("Caelum - Ensino e Inovação" );
sb.delete(6, 15);
System.out.println(sb); // Caelum e Inovação
Para converter um StringBuffer/ Builder em String,b a s t a
chamaro toStringmesmo. Ométodo reverseinverteseuconteúdo:
System.out.println(new StringBuffer("guilherme").reverse());
// emrehliug
Fora esses, também há o trim, charAt, length(), equals,
indexOf, lastIndexOf, substring.
Cuidado, pois o método substring não altera o valor do seu
StringBuilder ou StringBuffer, mas retornaa String quevocêde-
seja. Existe também o métodosubSequence que recebe o inícioeofi me
funcionadamesmamaneiraqueo substringcomdoisargumentos.
1) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 StringBuilder sb = new StringBuilder();
4 sb.append("guilherme").delete(2,3);
5 System.out.println(sb);
6 }
7 }
a) O código não compila: erro na linha que tenta imprimir o
StringBuilder.
b) Ocódigoco m p ilaeim p rimeglherme.
80

## Página 86

CasadoCódigo Capítulo4. TrablhandocomtiposdedadosemJava
c) Ocódigoco m p ilaeim p rimeguherme.
d) Ocódigoco m p ilaeim p rimegilherme.
e) Ocódigoco m p ilaeim p rimegulherme.
2) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 StringBuilder sb = new StringBuilder("guilherme");
4 System.out.println(sb.indexOf( "e")+ sb.lastIndexOf("e"));
5 System.out.println(sb.indexOf( "k")+ sb.lastIndexOf("k"));
6 }
7 }
a) Ocódigoimprime13e-2.
b) Ocódigoim p rime13e0.
c) Ocódigoimprime13e-1.
d) Ocódigoim p rime13e8.
e) Ocódigoimprime13e10.
f) Ocódigoim p rime1 5e-2.
g) Ocódigoim p rime1 5e0.
h) Ocódigoimprime15e-1.
i) Ocódigoim p rime1 5e8.
j) Ocódigoimprime15e10.
4.7 CriandoemanipulandoStrings
Existemduasmaneirastradicionaisdecriaruma String:
String nomeDireto = "Java";
String nomeIndireto = new String("Java");
A comparação entre esses dois tipos de criação deStrings éf e i t an a
seçãoTestequalitybetweenstringsandotherobjectsusing==andequals() 5.3
Existemoutrasmaneirasnãotãocomuns:
81

## Página 87

4.7. CriandoemanipulandoStrings CasadoCódigo
char[] nome = new char []{ 'J', 'a', 'v', 'a'};
String nomeComArray = new String(nome);
StringBuilder sb1 = new StringBuilder("Java");
String nome1 = new String (sb1);
StringBuffer sb2 = new StringBuffer("Java");
String nome2 = new String (sb2);
Como uma String não é um tipo primitivo, ela pode ter valornull,
lembre-sedisso:
String nome = null; // null explicito
Podemosconcatenar Stringscomo +:
String nome = "Certificação" + "" + "Java";
Caso tente concatenarnull com uma String, temos a conversão de
nullpara String:
String nula = null;
System.out.println("nula: " + nula); // imprime nula: null
OJ a v af a zac o n v e r s ã od et i p o sp r i m i t i v o sp a r aStrings automatica-
mente,maslembre-sedaprecedênciadeoperadores:
String nome = "Certificação" + '' + "Java" + '' + 1500;
System.out.println(nome);
String nome2 = "Certificação";
nome2 += '' + "Java" + '' + 1500;
System.out.println(nome2);
String valor =1 5+0 0+ " certificação";
System.out.println(valor); // imprime "15 certificação",
// primeiro efetuando uma soma
82

## Página 88

CasadoCódigo Capítulo4. TrablhandocomtiposdedadosemJava
Stringssãoimutáveis
Op rinci palpo n tosob r eS tringséqueelassãoim u tá veis:
String s = "caelum";
s.toUpperCase();
System.out.println(s);
Esse código imprime caelum em minúscula. Isso porque o método
toUpperCase não altera a String original. Na verdade, se olharmos o
javadocdaclasse String vamosperceberque todososmétodosquepare-
cemmodificarumaStringnaverdadedevolvemumanova .
String s = "caelum";
String s2 = s.toUpperCase();
System.out.println(s2);
Agora sim imprimiráCAELUM, uma nova String. Ou, usando a mesma
referência:
String s = "caelum";
s = s.toUpperCase();
System.out.println(s);
P a r atr a ta rm o sd e“ s tri n g sm u tá v e i s ” ,u sa m o sa sc la s se sStringBuffer
e StringBuilder.
Lembre-sequea Stringpossuiumarrayportráse,seguindoopadrão
doJava,suasposiçõescomeçamem0:
// 0=g, devolve 'g'
char caracter0 = "guilherme".charAt(0);
// 0=g 1=u, devolve 'u'
char caracter1 = "guilherme".charAt(1);
// 0=g 1=u 2=i, devolve 'i'
char caracter2 = "guilherme".charAt(2);
Cuidado ao acessar uma posição indevida, você pode levar
um StringIndexOutOfBoundsException (atenção ao nome da
Exception,nãoé ArrayIndexOutofBoundsException):
83

## Página 89

4.7. CriandoemanipulandoStrings CasadoCódigo
char caracter20 = "guilherme".charAt(20); // exception
char caracterMenosUm = "guilherme".charAt(-1); // exception
PrincipaismétodosdeString
Ométodo lengthimprimeotamanhoda String:
String s = "Java";
System.out.println(s.length()); // 4
System.out.println(s.length); // não compila: não é atributo
System.out.println(s.size()); // não compila: não existe size
// em String Java
J áométodo isEmptydizsea Stringtemtamanhozero:
System.out.println("".isEmpty()); // true
System.out.println("java".isEmpty()); // false
System.out.println("" .isEmpty()); // false
DevolvemumanovaString:
• String toUpperCase() tudoemmaiúscula;
• String toLowerCase() tudoemminúsculo;
• String trim() retiraespaçosembranconocomeçoenofim;
• String substring(int beginIndex, int endIndex) de-
volveasubstringapartirdosíndicesdecomeçoefim;
• String substring(int beginIndex) semelhante ao anterior,
mastomaasubstringapartirdoíndicepassadoatéofinaldaString;
• String concat(String) concatena o parâmetro ao fim da String
atualedevolveoresultado;
• String replace(char oldChar, char newChar) substitui
todasasocorrênciasdedeterminado charporoutro;
• String replace(CharSequence target, CharSequence
replacement) substitui todas as ocorrências de determinada
CharSequence(comoString)poroutra.
84

## Página 90

CasadoCódigo Capítulo4. TrablhandocomtiposdedadosemJava
Ométodo trimlimpacaracteresembranconasduaspontasda String:
System.out.println("" .trim()); // imprime só a quebra de
// linha do println
System.out.println("" .trim().isEmpty()); // true
System.out.println(" guilherme "); // imprime 'guilherme '
System.out.println(". ."); // imprime '.. '
O método replace substituirá todas as ocorrências de um texto por
outro:
System.out.println("java".replace("j", "J")); // Java
System.out.println("guilherme".replace("e", "i")); // guilhirmi
Podemos sempre fazer ochaining e criar uma sequência de “transfor-
mações”queretornamumanova String:
String parseado = " Quero tirar um certificado oficial de
Java! ".toUpperCase().trim();
// imprime: "QUERO TIRAR UM CERTIFICADO OFICIAL DE JAVA!"
System.out.println(parseado);
Para extrair pedaços de umaString,u s a m o som é t o d osubstring.
Cuidado ao usar o método substring com valores inválidos, pois eles
jogam uma Exception. O segredo do métodosusbtring éq u ee l en ã o
incluiocaracteredaposiçãofinal,masincluiocaracteredaposiçãoinicial:
String texto = "Java" ;
// ava
System.out.println(texto.substring(1));
// StringIndexOutOfBoundsException
System.out.println(texto.substring(-1));
// StringIndexOutOfBoundsException
System.out.println(texto.substring(5));
// Java
85

## Página 91

4.7. CriandoemanipulandoStrings CasadoCódigo
System.out.println(texto.substring(0, 4));
// ava
System.out.println(texto.substring(1, 4));
// Jav
System.out.println(texto.substring(0, 3));
// StringIndexOutOfBoundsException
System.out.println(texto.substring(0, 5));
// StringIndexOutOfBoundsException
System.out.println(texto.substring(-1, 4));
Comparação:
• boolean equals(Object) compara igualdade caractere a carac-
tere(herdadode Object);
• boolean equalsIgnoreCase(String) compara caractere a car-
actereignorandomaiúsculas/minúsculas;
• int compareTo(String) compara as 2 Strings por ordem lexi-
cográfica(vemde Comparable);
• int compareToIgnoreCase(String) compara as 2 Strings por
ordemlexicográficaignorandomaiúsculas/minúsculas.
Eaqui,todasasvariaçõesdessesmétodos. Nãoprecisasaberonúmeroex-
atoqueo compareToretorna,bastasaberqueseránegativocasoa String
na qual o método for invocado vier antes, zero se for igual, positivo se vier
depoisdoparâmetropassado:
String texto = "Certificado";
System.out.println(texto.equals("Certificado")); // true
System.out.println(texto.equals("certificado")); // false
System.out.println(texto.equalsIgnoreCase("certificado"));//true
System.out.println(texto.compareTo("Arnaldo")); // 2
86

## Página 92

CasadoCódigo Capítulo4. TrablhandocomtiposdedadosemJava
System.out.println(texto.compareTo("Certificado")); // 0
System.out.println(texto.compareTo("Grécia")); // -4
System.out.println(texto.compareTo("certificado")); // -32
System.out.println(texto.compareToIgnoreCase( "certificado"));//0
Buscassimples:
• boolean contains(CharSequence) devolve true se a String
contémasequênciade chars;
• boolean startsWith(String) devolve true se começa com a
Stringdoparâmetro;
• boolean endsWith(String) devolve true se termina com a
Stringdoparâmetro;
• int indexOf(char) e int indexOf(String) devolve o índice
daprimeiraocorrênciadoparâmetro;
• int lastIndexOf(char) e int lastIndexOf(String) de-
volveoíndicedaúltimaocorrênciadoparâmetro.
Ocódigoaseguirexemplificatodososcasosdessesmétodos:
String texto = "Pretendo fazer a prova de certificação de Java" ;
System.out.println(texto.indexOf("Pretendo")); // imprime 0
System.out.println(texto.indexOf("Pretendia")); // imprime -1
System.out.println(texto.indexOf("tendo")); // imprime 3
System.out.println(texto.indexOf("a")); // imprime 10
System.out.println(texto.lastIndexOf("a")); // imprime 45
System.out.println(texto.lastIndexOf("Pretendia")); //imprime -1
System.out.println(texto.startsWith("Pretendo")); // true
System.out.println(texto.startsWith("Pretendia")); // false
System.out.println(texto.endsWith("Java")); // true
System.out.println(texto.endsWith("Oracle")); // false
87

## Página 93

4.7. CriandoemanipulandoStrings CasadoCódigo
1) Considereoseguintecódigodentrodeum main:
class A{
public static void main(String [] args){
String s = "aba";
for(int i =0 ; i <9 ; i++) {
s = s +"aba";
}
System.out.println(s.length);
}
}
a) Não compila.
b) Compila e imprime 3.
c) Compila e imprime 30.
d) Compilaeimprime33.
e) Compila e imprime 36.
2) Dadaaseguinteclasse:
class B{
String msg ;
void imprime() {
if (!msg.isEmpty())
System.out.println(msg);
else
System.out.println("vazio");
}
}
Oqueacontecesechamarmos new B().imprime() ?
a) Não compila.
b) Compila,masdáexceçãonahoraderodar.
c) Compila,rodaenãoimprimenada.
88

## Página 94

CasadoCódigo Capítulo4. TrablhandocomtiposdedadosemJava
d) Compila,rodaeimprime“vazio”.
3) Dadaaseguinteclasse:
class B{
void imprime() {
String msg ;
if (!msg.isEmpty())
System.out.println(msg);
else
System.out.println("vazio");
}
}
Oqueacontecesechamarmos new B().imprime() ?
a) Não compila.
b) Compila,masdáexceçãonahoraderodar.
c) Compila,rodaenãoimprimenada.
d) Compila,rodaeimprime“vazio”.
4) Qualéasaídanosdo iscasos?
String s = "Caelum";
s.concat(" - Ensino e Inovação");
System.out.println(s);
StringBuffer s = new StringBuffer("Caelum");
s.append(" - Ensino e Inovação");
System.out.println(s);
a) ‘Caelum‘e‘Caelum-EnsinoeInovação‘.
b) ‘Caelum-EnsinoeInovação‘e‘Caelum-EnsinoeInovação‘.
c) ‘Caelum‘e‘Caelum‘.
d) ‘Caelum-EnsinoeInovação‘e‘Caelum‘.
89

## Página 95

4.7. CriandoemanipulandoStrings CasadoCódigo
5) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 String vazio = null;
4 String full = "Bem-vindo " + vazio;
5 System.out.println(full);
6 }
7 }
a) Nãocompilapoisvazioénulo.
b) Não compila por outro motivo.
c) Compilaeimprime“Bem-vindo“.
d) Compilaeimprime“Bem-vindovazio”.
e) Compila e imprime outro resultado que não foi mencionado nessas
alternativas.
6) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 String vazio ;
4 String full = "Bem-vindo " + vazio;
5 System.out.println(full);
6 }
7 }
a) Nãocompilapoisvazioénulo.
b) Não compila por outro motivo.
c) Compilaeimprime“Bem-vindo“.
d) Compilaeimprime“Bem-vindovazio”.
e) Compila e imprime outro resultado que não foi mencionado nessas
alternativas.
7) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
90

## Página 96

CasadoCódigo Capítulo4. TrablhandocomtiposdedadosemJava
1 class A{
2 String vazio ;
3 public static void main(String[] args){
4 String full = "Bem-vindo " + vazio;
5 System.out.println(full);
6 }
7 }
a) Nãocompilapoisvazioénulo.
b) Não compila por outro motivo.
c) Compilaeimprime“Bem-vindo“.
d) Compilaeimprime“Bem-vindovazio”.
e) Compila e imprime outro resultado que não foi mencionado nessas
alternativas.
8) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 static String vazio ;
3 public static void main(String[] args){
4 String full = "Bem-vindo " + vazio;
5 System.out.println(full);
6 }
7 }
a) Nãocompilapoisvazioénulo.
b) Não compila por outro motivo.
c) Compilaeimprime“Bem-vindo“.
d) Compilaeimprime“Bem-vindovazio”.
e) Compila e imprime outro resultado que não foi mencionado nessas
alternativas.
9) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
91

## Página 97

4.7. CriandoemanipulandoStrings CasadoCódigo
1 class A{
2 public static void main(String[] args){
3 String s = null
4 String s2 = new String(s);
5 System.out.println(s2);
6 }
7 }
a) Nãocompilaaotentarinvocaroconstrutor.
b) Compilaenãoimprimenada.
c) Compila e imprimenull.
d) Compilaedáerrodeexecuçãoaotentarcriarasegunda String.
10) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String [] args){
3 String s = "estudando para a certificação";
4 System.out.println(s.substring(3, 6));
5 }
6 }
a) Nãocompila: caracterecomacentoecedilhadentrodeumaString.
b) Não compila: substringé subString.
c) Compila e imprime “uda”.
d) Compilaeimprime“tuda”.
e) Compila e imprime “tud”.
11) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String [] args){
3 String s2 = new String(null);
4 System.out.println(s2);
5 }
6 }
92

## Página 98

CasadoCódigo Capítulo4. TrablhandocomtiposdedadosemJava
a) Nãocompilaaotentarinvocaroconstrutor.
b) Compilaenãoimprimenada.
c) Compila e imprimenull.
d) Co m p ilaedáerr odeexecuçãoaoten tarcriaraString.
12) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 int valor = 10;
4 int dividePor =4 ;
5 double resultado = valor / dividePor;
6 System.out.println(valor + dividePor +
7 " são os valores utilizados." );
8 System.out.println(resultado + " é o resultado");
9 }
10 }
a) Imprimeosnúmeros10,4e2.5.
b) Imprimeosnúmeros14e2.5.
c) Nenhumadasoutrasalternativas.
13) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 String s = "estudando para a certificação";
4 s.replace( "e", 'a');
5 System.out.println(s);
6 }
7 }
a) Não compila.
b) Compilaeimprime“estudandoparaacertificação”.
c) Compilaeimprime“astudandoparaacartificação”.
93

## Página 99

4.7. CriandoemanipulandoStrings CasadoCódigo
d) Compilaeimprime“studandoparaacrtificação”.
14) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 String s = "guilherme";
4 s.substring(0,2) = "gua";
5 System.out.println(s);
6 }
7 }
a) Errodecompilação.
b) Compilaeimprime“guilherme”.
c) Compilaeimprime“gualherme”.
94

## Página 100

Capítulo5
Usandooperadoreseconstruções
dedecisão
5.1 UseoperadoresJava
Para manipular os valores armazenados das variáveis, tanto as primitivas
quanto as não primitivas, a linguagem de programação deve oferecer oper-
adores. Um dos operadores mais importanteséoq u ep e r m i t eg u a r d a ru m
valoremumavariável. Esseoperadorédenominado operadordeatribuição .
No Java, o símbolo
= representa o operador de atribuição. Para atribuir
umvalorprecisamosdeumavariávelàqualseráatribuídoovalor,edovalor:
long idade =; // não compila, onde está o valor?
long = 15; // não compila, onde está o nome da variável?
long idade = 15; // compila

## Página 101

5.1. UseoperadoresJava CasadoCódigo
idade = 15;
// compila desde que a variável tenha sido declarada
// anteriormente
Paraumvalorseratribuídoaumavariável,ambosdevemsercompatíveis.
Umvalorécompatívelcomumavariávelseelefordomesmotipodelaoude
umtipomenosabrangente.
// Iniciando uma variável com o operador de atribuição "=".
int idade = 10;
// O valor literal 10 édo tipo int e a variável édo tipo long.
// Como int émenos abrangente que long essa atribuição está
// correta.
long idade = 10;
Procure sempre se lembrar dos tamanhos dos primitivos quando estiver
fazendo a prova. int é um número médio, será que ele “cabe” em uma
variável do tipolong (número grande)? Sim, logo o código compila. Mais
exemplos:
int a = 10; // tipos iguais
long b = 20; // int cabe em um long
float c =1 0 f; // tipos iguais
double d = 20.0f; // float cabe em um double
double e = 30.0; // tipos iguais
float f = 40.0; // erro, double não cabe em um float.
int g =1 0 l; // erro, long não cabe em int
float h =1 0 l; // inteiros cabem em decimais
double i = 20; // inteiros cabem em decimais
long j =2 0 f; // decimais não cabem em inteiros
A exceção a essa regra ocorre quando trabalhamos com tipos inteiros
menosabrangentesque int ( byte, short e char). Nessescasos,ocom-
piladorpermitequeatribuamosumvalorinteiro,desdequecompatívelcom
oti po:
byte b1 = 10;
byte b2 = 200; // não compila, estoura byte
96

## Página 102

CasadoCódigo Capítulo5. Usandooperadoreseconstruçõesdedecisão
char c1 = 10;
char c2 = -3; // não compila, char não pode ser negativo
Atribuiçãoereferência
Quando trabalhamos com referências, temos que lembrar do polimor-
fismo:
List<String > lista = new ArrayList<String>();
En oc a s od oJ a v a7 ,q u a n d oa t r i b u í m o sc o mgenericspodemos usar o
operadordiamante:
// operador diamante na atribuição e inicialização:
ArrayList<String> lista = new ArrayList<>();
// operador diamante e polimorfismo junto:
List<String > lista = new ArrayList<>();
Lembre que as atribuições em Java são por cópia de valor, sempre. No
tipo primitivo, copiamos o valor, em referências a objetos, copiamos o valor
dareferência(nãoduplicamosoobjeto):
List<String > lista = new ArrayList<>();
// copia o valor da referência, o objeto é o mesmo
List<String > lista2 = lista;
lista2.add( "Guilherme");
// verdadeiro
System.out.println(lista.size() == lista2.size());
int idade = 15;
int idade2 = idade; // copia o valor
idade2 = 20;
System.out.println(idade == idade2); // falso
97

## Página 103

5.1. UseoperadoresJava CasadoCódigo
Operadoresaritméticos
Oscálculossobreosvaloresdasvariáveisprimitivasnuméricassãofeitos
com os operadores aritméticos. A linguagem Java define operadores para as
principaisoperaçõesaritméticas(soma,subtração,multiplicaçãoedivisão).
int dois =2 ;
int dez = 10;
// Fazendo uma soma com o operador "+".
int doze = dois + dez;
// Fazendo uma subtração com o operador "-".
int oito = dez - dois;
// Fazendo uma multiplicação com o operador "*".
int vinte = dois * dez;
// Fazendo uma divisão com o operador "/".
int cinco = dez / dois;
Além desses, há um operador para a operação aritmética “resto da di-
visão”. Esse operador só faz sentido para variáveis primitivas numéricas in-
teiras.
int dois =2 ;
int dez = 10;
// Calculando o resto da divisão de 10 por 2.
int um = dez % dois;
O resultado de uma operação aritmética é um valor. A dúvida que surge
é qual será o tipo dele. Para descobrir o tipo do valor resultante de uma op-
eraçãoaritmética,devem-seconsiderarostiposdasvariáveisenvolvidas.
A regra é a seguinte: o resultado é do tipo mais abrangente entre os das
variáveisenvolvidasou,nomínimo,o int.
int idade = 15;
long anos =5 ;
98

## Página 104

CasadoCódigo Capítulo5. Usandooperadoreseconstruçõesdedecisão
// ok, o maior tipo era long
long daquiCincoAnos = idade + anos;
// não compila, o maior tipo era long, devolve long
int daquiCincoAnos2 = idade + anos;
Masdevemoslembrardaexceção: omínimoéum int:
byte b =1 ;
short s =2 ;
// devolve no mínimo int, compila
int i = b + s;
// não compila, ele devolve no mínimo int
byte b2 = i + s;
// compila forçando o casting, correndo risco de perder
// informação
byte b2 =( byte)( i + s);
Divisãoporzero
Dividir (ou usar mod) um inteiro por zero lança uma
ArithmeticException. Se o operando for um float ou double,
isso gera infinito positivo ou negativo (depende do sinal do operador). As
classes Floate Doublepossuemconstantesparaessesvalores.
int i = 200;
int v =0 ;
// compila, mas exception
System.out.println(i / v);
// compila e roda, infinito positivo
System.out.println(i / 0.0);
Aindaexisteovalor NaN (Not a Number), geradopelaradiciaçãodeum
númeronegativoeporalgumascontascomnúmerosinfinitos.
99

## Página 105

5.1. UseoperadoresJava CasadoCódigo
double positivoInfinito = 100 / 0.0;
double negativoInfinito = -100 / 0.0;
// número não definido (NaN)
System.out.println(positivoInfinito + negativoInfinito);
Comparadores
Acomparaçãoentreosvaloresdeduasvariáveiséfeitaatravésdosoper-
adores de comparação. O mais comum é comparar a igualdade e a desigual-
dadedosvalores. Existemoperadoresparaessasduasformasdecomparação.
• == igual
• != diferente
Além disso, os valores numéricos ainda podem ser comparados em re-
laçãoàordem.
• > maior
• < menor
• >= maiorouigual
• <= menorouigual
Uma comparação pode devolver dois valores possíveis: verdadeiro ou
falso. NoJava,umacomparaçãosempredevolveumvalor boolean.
System.out.println(1 == 1); // true.
System.out.println(1 != 1); // false.
System.out.println(2 < 1); // false.
System.out.println(2 > 1); // true.
System.out.println(1 >= 1); // true.
System.out.println(2 <= 1); // false.
Todacomparaçãoenvolvendovaloresnuméricosnãoconsideraotipodo
valor. Confira somente se eles têm o mesmo valor ou não, independente de
seutipo:
100

## Página 106

CasadoCódigo Capítulo5. Usandooperadoreseconstruçõesdedecisão
// true.
System.out.println(1 == 1.0);
// true.
System.out.println(1 == 1);
// true. 1.0 float é 1.0 double
System.out.println(1.0f == 1.0d);
// true. 1.0 float é 1 long
System.out.println(1.0f == 1l);
Os valores não primitivos (referências) e os valoresboolean devem ser
comparados somente com dois comparadores, o de igualdade (==)eod e
desigualdade( !=).
// não compila, tipo não primitivo sóaceita != e ==
System.out.println("Mario" > "Guilherme");
// não compila, boolean sóaceita != e ==
System.out.println(true < false);
Não podemos comparar tipos incomparáveis, como umboolean com
umvalornumérico. Maspodemoscomparar charscomnuméricos.
// não compila, boolean é boolean
System.out.println(true == 1);
// compila, 'a' tem valor numérico também
System.out.println('a' > 1);
Cuidado, é muito fácil comparar atribuição com comparação e uma pe-
gadinhaaquipodepassardespercebida,comonoexemploaseguir:
int a =5 ;
System.out.println(a = 5); // não imprime true, imprime 5
101

## Página 107

5.1. UseoperadoresJava CasadoCódigo
Precisão
Ao fazer comparações entre números de ponto flutuante, devemos
tomar cuidado com possíveis problemas de precisão. Qualquer conta
com estes números pode causar um estouro de precisão, fazendo com
que ele fique ligeiramente diferente do esperado. Por exemplo,
1= =
(100.0 / 100) podenãoserverdadeirocasoadivisãotenhaumapre-
cisãonãoexata.
Operadoreslógicos
Muitasvezesprecisamoscombinarosvalores booleansobtidos,porex-
emplo, com comparações ou diretamente de uma variável. Isso é feito uti-
lizandoosoperadoreslógicos.
Em lógica, as operações mais importantes são:
e, ou, ou exclusivo
e negação.
System.out.println(1 ==1&1>2 ) ; // false.
System.out.println(1 ==1|2>1 ) ; // true.
System.out.println(1 ==1^2>1 ) ; // false.
System.out.println(!(1 == 1)); // false.
Antes de terminar a avaliação de uma expressão, eventualmente, o re-
sultado já pode ser descoberto. Por exemplo, quando aplicamos a operação
lógica
e, ao achar o primeiro termo falso não precisamos avaliar o restante
daexpressão.
Quandousamosessesoperadores,sempreosdoisladosdaexpressãosão
avaliadosmesmonessescasosemquenãoprecisariam.
Para melhorar isso, existem os operadores de curto circuito&& e ||.
Quando já for possível determinar a resposta final olhando apenas para a
primeirapartedaexpressão,asegundanãoéavaliada:
System.out.println(1 != 1 &&1>2 ) ;
// false, o segundo termo não é avaliado.
102

## Página 108

CasadoCódigo Capítulo5. Usandooperadoreseconstruçõesdedecisão
System.out.println(1 == 1 ||2>1 ) ;
// true, o segundo termo não é avaliado.
Amaiordificuldadecomoperadoresdecurtocircuitoéseasegundaparte
causa efeitos colaterais (um incremento, uma chamada de método). Avaliar
ounão(independentedaresposta)podeinfluenciarnoresultadofinaldopro-
grama.
publicstaticboolean metodo(String msg){
System.out.println(msg);
return true ;
}
publicstaticvoid main(String[] args){
System.out.println(1 == 2 & metodo("oi"));
// imprime oi, depois false
System.out.println(1 == 2 && metodo("tchau"));
// não imprime tchau, imprime false
int i = 10;
System.out.println(i = =2& i++ == 0);
// imprime false, soma mesmo assim
System.out.println(i);
// imprime 11
int j = 10;
System.out.println(j = =2& & j++ == 0);
// imprime false, não soma
System.out.println(j);
// imprime 10
}
Incrementosedecrementos
Parafacilitaracodificação,aindapodemosteroperadoresquefazemcál-
culos(aritméticos)eatribuiçãoemumaúnicaoperação. Parasomarousub-
trairumvalorem1,podemosusarosoperadoresdeincremento/decremento:
int i =5 ;
103

## Página 109

5.1. UseoperadoresJava CasadoCódigo
// 5 - pós-incremento, i agora vale 6
System.out.println(i++);
// 6 - pós-decremento, i agora vale 5
System.out.println(i--);
// 5
System.out.println(i);
Eincrementosedecrementosantecipados:
int i =5 ;
System.out.println(++i); // 6 - pré-incremento
System.out.println(--i); // 5 - pré-decremento
System.out.println(i); // 5
Cuidado com os incrementos e decrementos em relação apré e pós.
Quando usamos pós-incremento, essaéaú l t i m ac o i s aas e re x e c u t a d a . E
quandousamosopré-incremento,ésempreaprimeira.
int i =10 ;
// 10, primeiro imprime, depois incrementa
System.out.println(i++);
// 11, valor já incrementado.
System.out.println(i);
// 12, incrementa primeiro, depois imprime
System.out.println(++i);
// 12, valor incrementado.
System.out.println(i);
Existem ainda operadores para realizar operações e atribuições de uma
sóvez:
int a =10 ;
104

## Página 110

CasadoCódigo Capítulo5. Usandooperadoreseconstruçõesdedecisão
// para somar 2 em a
a = a +2 ;
//podemos obter o mesmo resultado com:
a += 2;
//exemplos de operadores:
int i =5 ;
i += 10; //soma e atribui
System.out.println(i); // 15
i -= 10; //subtrai e atribui
System.out.println(i); // 5
i *=3 ; // multiplica e atribui
System.out.println(i); // 15
i /= 3; // divide a atribui
System.out.println(i); // 5
i %= 2; // divide por 2, e atribui o resto
System.out.println(i); // 1
System.out.println(i+=3); // soma 3 e retorna o resultado: 4
Nesses casos, o compilador ainda dá um desconto para operações com
tiposteoricamenteincompatíveis. Veja:
byte b1 =3 ; // compila, dá um desconto
b1 = b1 +4 ; // não compila, conta com int devolve int
byte b2 =3 ; // compila, dá um desconto
b2 += 4; // compila também, compilador gente boa!
Esse último caso compila inclusive sepassar valores absurdamente altos:
b2+=400 é diferente deb 2=b 2+4 0 0 . Ele faz ocasting er o d an o r m a l -
mente.
105

## Página 111

5.1. UseoperadoresJava CasadoCódigo
Cuidado também com o caso de atribuição com o próprio autoincre-
mento:
int a = 10;
a += ++a + a ++ + a;
Comoaexecuçãoédoprimeiroparaoúltimoelementodassomas,temos
asreduções:
a += ++a + a ++ + a;
a = a ++ + a + a ++ + a;
a = 10 +11 + a ++ + a;
a =1 0+1 1+1 1++ + a;
a =1 0+1 1+1 1+1 2 ;
a = 44; // a passa a valer 44
Umoutroexemplodeoperadorpós-incremento,cujoresultad oé1e2:
int j =0 ;
int i =( j++ * j + j++);
System.out.println(i);
System.out.println(j);
Pois:
i =( 0* j + j++); // j vale 1
i =( 0*1+ j++); // j vale 1
i =( 0*1+1 ) ; // j vale 2
i =1 ; // j vale 2
Podemos fazer diversas atribuições em sequência, que serão executadas
da direita para a esquerda. O resultado de uma atribuição é sempre o valor
daatribuição:
int a = 15, b = 20, c = 30;
a = b = c; // b = 30, portant oa=3 0
Outroexemplomaiscomplexo:
int a = 15, b = 20, c = 30;
a =( b = c +5 )+5 ; // c= 30, portanto b = 35, portant oa=4 0
106

## Página 112

CasadoCódigo Capítulo5. Usandooperadoreseconstruçõesdedecisão
Operadorternário Condicional
Hátambémumoperadorparacontroledefluxodoprograma,comoum
if. É chamado deoperadorternário. Se determinada condição acontecer,
elevaipo rumcaminho ,casoco n tráriovaipo ro u tr o .
Aestruturadooperadorternári oéas eguinte:
variável=teste_booleano ? valor_se_verdadeiro: valor_se_falso;
int i =5 ;
System.out.println(i = =5? "verdadeiro": "falso");// verdadeiro
System.out.println(i ! =5?1 :2 ) ; // 2
String mensagem = i %2= =0? "é par" : "é ímpar" ;
O operador condicional sempre tem que retornar valores que podemos
usarparaatribuir,imprimiretc.
Operadordereferência
Para acessar os atributos ou métodos de um objeto precisamos aplicar o
operador . (ponto) em uma referência. Você pode imaginar que esse oper-
adornaveganareferênciaatéchegarnoobjeto.
String s = new String("Caelum");
// Utilizando o operador "." para acessar um
// objeto String e invocar um método.
int length = s.length();
ConcatenaçãodeStrings
Quando usamos Strings, podemos usar o+ para denotar concatenação.
Éaúnicaclassequeaceitaalgumoperadorforaoponto.
Em Java, não há sobrecarga de operadores como em outras linguagens.
Portanto, não podemos escrever nossas próprias classes com operadores di-
versos.
107

## Página 113

5.1. UseoperadoresJava CasadoCódigo
StringBuilder
Ac o n c a t e n a ç ã od eS t r i n g séu msyntax sugarque o próprio com-
pilador resolve. No código compilado, na verdade, é usado um
StringBuilder.
Precedência
NãoénecessáriodecoraraprecedênciadetodosoperadoresdoJava,basta
saber o básico, que primeiro são executados pré-incrementos/decrementos,
depoismultiplicação/divisão/mod,passandoparasoma/subtração,depoisos
shifts(
<<, >>, >>>)e,porúltimo,ospós-incrementos/decrementos.
Asquestõesdacertificaçãonãoentramemmaisdetalhesqueisto.
Pontosimportantes
• Naatribuiçãodeumvalorparaumavariávelprimitiva,ovalordeveser
domesmoti podavariá velo udeummenosab rangen te.
EXCEÇÃO À REGRA:P a r ao st i p o sbyte, short e char,e m
atribuiçõescomliteraisdotipo int,ocompiladorverificaseovalora
seratribuídoestánorangedotipodavariável.
• Toda variável não primitiva está preparada somente para armazenar
referênciasparaobjetosquesejamdomesmotipodela.
• Todacomparaçãoetodaoperaçãológicadevolve boolean.
• Oresultadodetodaoperaçãoaritméticaénomínimo int ou do tipo
davariávelmaisabrangentequeparticipoudaoperação.
• Acomparaçãodevaloresnuméricosnãoconsideraostiposdosvalores.
• As referências e os valoresboolean só podem ser comparados com
==ou !=.
• T odaa trib uiçãoépo rcó p iadevalo r .
108

## Página 114

CasadoCódigo Capítulo5. Usandooperadoreseconstruçõesdedecisão
Observação:Or e c u r s od oautoboxingpermite fazer algumas operações
diferentesenvolvendovariáveisnãoprimitivas. Discutiremossobreautobox-
ingadiante.
Castingdetiposprimitivos
Nãopodemosatribuiraumavariáveldeumtipoumvalorquenãoécom-
patívelcomela:
double d = 3.14;
int i = d;
Sópodemosfazeressasatribuiçõesseosvaloresforem compatíveis.Co m -
patível é quando um tipo cabe em outros, e ele só cabe se orange(alcance)
delefo rmaisam ploqueodoo u tr o .
byte->short->int->long->float->double
char->int
Seestivermosconvertendodeumtipoquevaidaesquerdaparaadireita
nessa tabelinha, não precisamos de casting, aautopromoçãofará o serviço
pornós.
Se estamos indo da direita para a esquerda, precisamos docasting en ã o
importamosvaloresqueestãodentro. Exemplo:
double d =0 ;
float f = d;
Esse código não compila sem um casting! O casting é a maneira que us-
amosparamoldarumavariáveldeumtipoemoutro. Nósestamosavisando
o compilador que sabemos da possibilidade de perda de precisão ou trunca-
mento,masnósrealmentequeremosfazerisso:
float f =( float) d;
Podemos fazer casting entre ponto flutuante e inteiro, o resultado será o
númerotruncado,semascasasdecimais:
double d = 3.1415;
int i =( int) d; // 3
109

## Página 115

5.1. UseoperadoresJava CasadoCódigo
Dica
Não é preciso decorar a sequência int->long->float etc. Basta lem-
brar os alcances das variáveis. Por exemplo, ochar tem dois bytes e
guarda um número positivo. Será então que posso atribuir umchar a
um short? Não, pois umshort tem 2 bytes, e usa meio a meio entre
osnúmerospositivosenegativos.
1) Qualcódigoaseguircompila?
a) short s = 10;
char c = s;
b) char c = 10;
long l = c;
c) char c = 10;
short s = c;
2) Façacontascomdiferentesoperandos:
int i1 = 3/2;
double i2 = 3/2;
double i3 = 3/2.0;
long x =0 ; double d =0 ;
double zero = x + d;
System.out.println(i1 + i2 + i3 + x + d + zero);
Qualoresultado?
a) 3
b) 3.5
c) 4
d) 4.5
110

## Página 116

CasadoCódigo Capítulo5. Usandooperadoreseconstruçõesdedecisão
3) O código a seguir pode lançar umNullPointerException.C o m o
evitarissomantendoamesmalógica?
void metodo(Carro c){
if(c != null & c.getPreco() > 100000) {
System.out.println("possivel sequestro" );
}
}
a) Trocando !=por ==
b) Trocando >por <
c) Trocando &por |
d) Trocando &por &&
4) Algunstestesinteressantescomtiposprimitivos:
int i =( byte)5 ;
long l = 3.0;
float f = 0.0;
char c =3 ;
char c2 = -2;
Quais compilam?
a) i,fec
b) i,f,cec2
c) i,fec2
d) iec
e) fec
f) fec2
g) iel
h) l,fec
i) i,cec2
111

## Página 117

5.1. UseoperadoresJava CasadoCódigo
5) Aexpressãoaseguirpodeserreduzida,comopodemosfazer?
if ((trem && !carro)| |( ! trem && carro)) {
// ....
}
• Trocandoparausarumoperador &eum |
• Trocandoparausardoisoperadores &eum |
• Trocandoparausarumoperador !eum ^
• Trocandoparausarumoperador ^
• Removendoosparênteses
• Removendoo ||domeio
• Removendoos !
6) Imprima a divisão por 0 de números inteiros e de números com ponto
flutuante:
System.out.println(3 / 0);
System.out.println(3 / 0.0);
System.out.println(3.0 / 0);
System.out.println(-3.0 / 0);
Quaisosresultados?
7)1 class Xyz {
2 public static void main(String[] args){
3 int y;
4 for(int x =0 ; x<10; ++x){
5 y = x %5+2 ;
6 }
7 System.out.println(y);
8 }
9 }
Qualoresultadodessecódigo?
a) Errodecompilaçãonalinha3
112

## Página 118

CasadoCódigo Capítulo5. Usandooperadoreseconstruçõesdedecisão
b) Errodecompilaçãonalinha7
c) 1
d) 2
e) 3
f) 4
g) 5
h) 6
8)1 class Teste {
2 public static void main(String[] args){
3 byte b =1 ;
4 int i =1 ;
5 long l =1 ;
6 float f = 1.0;
7 }
8 }
Ocódigo:
a) Não compila a linha 3 pois “1” éint e não pode ser colocado em um
byte
b) Nãocompilaalinha4pois“1”é longenãopodesercolocadoemum
int
c) Não compila a linha 5 pois “1” éint e não pode ser colocado em um
long
d) Não compila a linha 6 pois “1.0” édouble e não pode ser colocado
emum float
e) Todasaslinhascompilam
9) class $_o0o_$ {
public static void main(String[] args){
int $$ =5 ;
int __ = $$++;
if (__ <+ + $$ || __-- > $$)
113

## Página 119

5.1. UseoperadoresJava CasadoCódigo
System.out.print("A");
System.out.print($$);
System.out.print(__);
}
}
Oestranhocódigo:
a) Não compila por causa do nome da classe
b) Nãocompilaporcausadosnomesdasvariáveis
c) Compilamasdáerronaexecução
d) Compila,rodaeimprimeA76
e) Compila,rodaeimprimeA75
f) Compila,rodaeimprimeA74
g) Compila,rodaeimprime76
1) Oqueacontececomoseguintecódigo? Compila? Roda?
public class Teste{
public static void main(String[] args){
byte b1 =5 ;
byte b2 =3 ;
byte b3 = b1 + b2;
}
}
1) Oqueacontececomseguintecódigo?
1 public class Teste{
2 public static void main(String [] args){
3 byte b1 = 127;
4 byte b2 = -128;
5 byte b3 = b1 + b2;
114

## Página 120

CasadoCódigo Capítulo5. Usandooperadoreseconstruçõesdedecisão
6 System.out.println(b3);
7 }
8 }
a) N ãoco m p ilapo rumerr onalinha3
b) N ãoco m p ilapo rumerr onalinha4
c) N ãoco m p ilapo rumerr onalinha5
d) Compila e imprime -1
1)1 public class Teste {
2 public static void main(String[] args){
3 int i;
4 for (i =0; i <5 ; i++) {
5 if (++i %3= =0){
6 break;
7 }
8 }
9 System.out.println(i);
10 }
11 }
Qualéor esul tadodocódigo:
a) imprime1
b) imprime2
c) imprime3
d) imprime4
2) Considerando o mesmo código da questão anterior, e se trocarmos para
pós-incrementodentrodo if?
1 public class Teste {
2 public static void main(String [] args){
3 int i;
4 for (i =0; i <5 ; i++) {
115

## Página 121

5.1. UseoperadoresJava CasadoCódigo
5 if (i+ +%3= =0 ){
6 break;
7 }
8 }
9 System.out.println(i);
10 }
11 }
Qualéor esul tado?:
a) imprime1
b) imprime2
c) imprime3
d) imprime4
3) Qualéor esul tadodoseguintecódigo:
public class Teste {
public static void main(String[] args){
int i;
for (i =0 ; i <5 ; i++) {
if (++i %3= =0 ){
break;
}
}
System.out.println(i);
}
}
4) Esetrocarmosopré-incrementoparapós-incremento( i++)?
5) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 byte b1 = 100;
4 byte b2 = 131;
116

## Página 122

CasadoCódigo Capítulo5. Usandooperadoreseconstruçõesdedecisão
5 System.out.println(b1);
6 }
7 }
a) Compilaeimprimeumnúmeropositivo.
b) Compilaeimprimeumnúmeronegativo.
c) Compilaedáumaexceptiondeestourodenúmero.
d) Compilaeimprimeumnúmeroquenãosabemosdizeraocerto.
e) Co m p ilaeim p rime“ N o tAN umber ” .
f) Não compila.
6) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 char c =65 ;
4 char c2 = -3;
5 System.out.println(c + c2);
6 }
7 }
a) Nãocompilanasduasdeclaraçõesde char.
b) Nãocompilanastrêslinhasdentrodométodo main.
c) Nãocompilasomentenadeclaraçãode c2.
d) N ãoco m p ilaso men tenaso madecaracter es.
e) Compilaeroda,imprimindo62.
f) Compilaeroda,imprimindoumoutrovalor.
7) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 char c =65 ;
4 char c2 =68-65 ;
117

## Página 123

5.1. UseoperadoresJava CasadoCódigo
5 System.out.println(c + c2);
6 }
7 }
a) Nãocompilanasduasdeclaraçõesde char.
b) Nãocompilanastrêslinhasdentrodométodo main.
c) Nãocompilasomentenadeclaraçãode c2.
d) N ãoco m p ilaso men tenaso madecaracter es.
e) Compilaeroda,imprimindo62.
f) Compilaeroda,imprimindoumoutrovalor.
8) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 double resultado =15/0 ;
4 System.out.println(resultado);
5 }
6 }
a) Não compila.
b) Compilaedáexception.
c) Compilaeimprimepositivoinfinito.
d) Compila e imprime 0.
9) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 String resultado = "divisao dá: " +15/0 . 0 ;
4 System.out.println(resultado);
5 }
6 }
a) Não compila.
118

## Página 124

CasadoCódigo Capítulo5. Usandooperadoreseconstruçõesdedecisão
b) Compilaedáexception.
c) Compilaeimprimepositivoinfinito.
d) Compila e imprime 0.
10) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 System.out.println(1==true);
4 }
5 }
a) Não compila.
b) Compilaeimprimeverdadeiro.
c) Compila e imprime falso.
5.2 Use parentêses para sobrescrever a pre-
cedênciadeoperadores
Às vezes desejamos alterar a ordem de precedência de uma linha, e nesses
instantesusamososparênteses:
int a =1 5*4+1 ; // 15 *4 = 60, depois 60 +1=6 1
int b =1 5*( 4+1 ) ; / /4+1=5 ,depois 15 *5 = 75
Devemostomarmuitocuidadonaconcatenaçãode Stringeprecedên-
cia:
System.out.println(15+0+ " é cento e cinquenta");
// 15 é cento e cinquenta
System.out.println(15 + (0 + " é cento e cinquenta"));
// 150 é cento e cinquenta
System.out.println(("guilherme" + " silveira").length());
// 18
119

## Página 125

5.3. TesteaigualdadeentreStringseoutrosobjetosusando==eequals() CasadoCódigo
1) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 String resultado =( "divisao dá: " + 15) /0.0;
4 System.out.println(resultado);
5 }
6 }
a) Não compila.
b) Compilaedáexception.
c) Compilaeimprimepositivoinfinito.
d) Compila e imprime 0.
2) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 System.out.println(((!(true==false))==true ? 1 : 0)==0);
4 }
5 }
a) Imprime true.
b) Imprime false.
c) Não compila.
d) Imprime1.
e) Imprime0.
5.3 Teste a igualdade entre Strings e outros
objetosusando==eequals()
ObserveoseguintecódigoquecriaduasStrings:
1 String nome1 = new String ("Mario");
2 String nome2 = new String ("Mario");
120

## Página 126

CasadoCódigo Capítulo5. Usandooperadoreseconstruçõesdedecisão
Comojáestudamosanteriormente,ooperador ==éutilizadoparacom-
paração. Neste caso, como se tratam de objetos, irá comparar as duas refer-
ênciaseverseapontamparaomesmoobjeto:
1 String nome1 = new String ("Mario");
2 String nome2 = new String ("Mario");
3
4 System.out.println(nome1 == nome2); // imprime false
Atéaquitudobem. Masvamosalterarumpouconossocódigo,mudando
amaneiradecriarnossasStrings,erodarnovamente:
1 String nome1 = "Mario";
2 String nome2 = "Mario";
3
4 System.out.println(nome1 == nome2); // o que imprime?
Aoexecutarocódigo,vemosqueeleimprime true. Oqueaconteceu?
PooldeStrings
OJ a vama n témumpooldeob jetosdoti po String. Antesdecriaruma
nova String, primeiro o Java verifica neste pool se uma String com o mesmo
conteúdojáexiste;casosim,eleareutiliza,evitandocriardoisobjetosexata-
menteiguaisnamemória. Comoasduasreferênciasestãoapontandoparao
mesmoobjetodopool,o
==retorna true.
Mas por que isso não aconteceu antes, com nosso primeiro exemplo? O
JavasócolocanopoolasStringscriadasusando literais. Stringscriadascom
ooperador newnãosãocolocadasnopoolautomaticamente.
1 String nome1 = "Mario"; //será colocada no pool
2 String nome2 = new String ("Mario");
3 /*
4 "Mario" é colocado, mas nome2 é outra
5 referência, não colocada no pool
6 */
Sabendo disso, temos que ter cuidado redobrado quando comparando
Stringsusandoooperador ==:
121

## Página 127

5.3. TesteaigualdadeentreStringseoutrosobjetosusando==eequals() CasadoCódigo
1 String s1 = "string";
2 String s2 = "string";
3 String s3 = new String("string");
4
5 System.out.println(s1 == s2); // true, mesma referencia
6 System.out.println(s1 == s3); // false, referências diferentes
7 System.out.println(s1.equals(s3 )); // true, mesmo conteúdo
Repareque,mesmosendoinstânciasdiferentes,quandocomparadasus-
andoométodo equals,oretornoé true,casooconteúdodasStringsseja
omesmo.
Quandoconcatenamosliterais,aStringresultantetambémserácolocada
nopool.
1 String ab = "a" + "b";
2 System.out.println("ab" == ab); // true
M a si s s oév e r d a d eapenasusandoliteraisemambososladosdacon-
catenação. Sealgumdosobjetosnãoforumliteral,oresultadoseráumnovo
ob jeto ,quenãoestaránopool:
1 String a = "a";
2 String ab = a + "b"; //usando uma referência e um literal
3 System.out.println("ab" == ab); // false
SabemosqueStringssãoimutáveis,equecadamétodochamadoemuma
String retorna uma nova String, sem alterar o conteúdo do objeto original.
Esses objetos resultantes de retornos de métodos não são buscados no pool,
sãonovosobjetos:
1 String str = "um texto qualquer";
2 String txt1 = "texto" ;
3 String txt2 = x.substring(3, 8); //cria uma nova string
4 System.out.println(txt1 == txt2); // false
5 System.out.println(txt.equals(x .substring(3, 8)); // true
122

## Página 128

CasadoCódigo Capítulo5. Usandooperadoreseconstruçõesdedecisão
osmétodosdeStringsemprecriamnovosobjetos?
Nemsempre. Seoretornodométodoforexatamenteoconteúdoat-
ualdoobjeto,nenhumobjetonovoécriado:
1 String str = "HELLO WORLD" ;
2 String upper = str.toUpperCase(); // já está maiúscula
3 String subs = str.substring(0,11); // string completa
4 System.out.println(str == upper); // true
5 System.out.println(str == subs); // true
6 System.out.println(str == str.toString()); // true
ContandoStrings
U m aq u e s t ã or e c o r r e n t en ap r o v aéc o n t a rq u a n t o so b j e t o sd ot i p o
String são criados em um certo trecho de código. Veja o código a seguir
etentedescobrirquantosobjetosStringsãocriados:
1 String h = new String ("hello ");
2 String h1 = "hello " ;
3 String w = "world";
4
5 System.out.println("hello " );
6 System.out.println(h1 + "world");
7 System.out.println("Hello " == h1);
Een tão?V amosverpassoapasso:
1 //Cria 2 objetos, um literal (que vai para o pool) e o outro
2 //com o new
3 String h = new String ("hello ");
4
5 //nenhum objeto criado, usa o mesmo do pool
6 String h1 = "hello " ;
7 //novo objeto criado e inserido no pool
8 String w = "world";
9
123

## Página 129

5.3. TesteaigualdadeentreStringseoutrosobjetosusando==eequals() CasadoCódigo
10 //nenhum objeto criado, usa do pool
11 System.out.println("hello " );
12
13 //criado um novo objeto resultante da concatenação,
14 // mas este não vai para o pool
15 System.out.println(h1 + "world");
16
17 //Novo objeto criado e colocado no pool (Hello com H maiúsculo).
18 System.out.println("Hello " == h1); // 1
Logotemos5Stringscriadas.
CuidadocomStringjácolocadasnopool
Para descobrir se uma String foi criada e colocada no pool é
necessário prestar muita atenção ao contexto do código e ao enunciado
daquestão. AStringsóécolocadanopoolnaprimeiraexecuçãodotre-
chodecódigo. CuidadocomquestõesquecriamStringsdentrodeméto-
dos,ouquedizememseuenunciadoqueométodojáfoiexecutadopelo
menosumavez:
1 public class Testes {
2 public static void main(String[] args){
3 for(int i =0 ; i< 10; i++)
4 System.out.println(metodo());
5 }
6
7 private static String metodo() {
8 String x = "x";
9 return x.toString();
10 }
11 }
Aoexecutaressaclasse,apenas umobjetoStringserácriado. Oúnico
l ugaro ndeaS tringécriadaénalinha8docódigo .
124

## Página 130

CasadoCódigo Capítulo5. Usandooperadoreseconstruçõesdedecisão
Ométodoequals
Para comparar duas referências, podemos sempre usar o operador==.
Dadaaclasse Cliente:
class Cliente {
private String nome;
Cliente(String nome ){
this.nome = nome;
}
}
Cliente c1 = new Cliente( "guilherme");
Cliente c2 = new Cliente( "mario");
System.out.println(c1==c2); // false
System.out.println(c1==c1); // true
Cliente c3 = new Cliente( "guilherme");
System.out.println(c1==c3);
// false, pois não é a mesma
// referência: são objetos diferentes na memória
Paracompararosobjetosdeumaoutramaneira,quenãoatravésdarefer-
ência, podemos utilizar o métodoequals, cujo comportamento padrão é
fazerasimplescomparaçãocomo ==:
Cliente c1 = new Cliente( "guilherme");
Cliente c2 = new Cliente( "mario");
System.out.println(c1.equals(c2)); // false
System.out.println(c1.equals(c1)); // true
Cliente c3 = new Cliente( "guilherme");
System.out.println(c1.equals(c3));
// false, pois não é a mesma
// referência: são objetos diferentes na memória
I s s oé ,e x i s t eu mm é t o d oe mObject que você pode reescrever
para definir um c r i t é r i od ec o m p a r a ç ã od ei g u a l d a d e. Classes como
String, Integer e muitas outras possuem esse método reescrito, as-
sim new Integer(10) == new Integer(10) dá false, mas new
Integer(10).equals(Integer(10))dá true.
125

## Página 131

5.3. TesteaigualdadeentreStringseoutrosobjetosusando==eequals() CasadoCódigo
Éi n t e r e s sa n t er ee sc r ev e re s sem é t od oq ua n d ov oc êj ul g a rn ec e s sá ri ou m
critério de igualdade diferente que o== retorna. Imagine o caso de nosso
Cliente:
class Cliente {
private String nome ;
Cliente(String nome ){
this.nome = nome;
}
public boolean equals(Object o){
if (! (o instanceof Cliente)) {
return false ;
}
Cliente outro =( Cliente) o;
return this .nome.equals(outro.nome);
}
}
O método equals não consegue tirar proveito dogenerics,e n t ã o
precisamos receber Object e ainda verificar se o tipo do objeto passado
comoargumentoérealmenteuma Cliente(ocontratodométododizque
vocêdeveretornar false,enãodeixarlançarexceptionemumcasodesses).
Agorasim,podemosusarométodo equalscomoesperamos:
Cliente c1 = new Cliente( "guilherme");
Cliente c2 = new Cliente( "mario");
System.out.println(c1.equals(c2 )); // false
System.out.println(c1.equals(c1 )); // true
Cliente c3 = new Cliente( "guilherme");
System.out.println(c1.equals(c3 )); // true
Cuidado ao sobrescrever o método equals: ele deve ser público, e
deve receber Object. C a s ov o c êr e c e b au m ar e f e r ê n c i aau mo b j e t od o
tipo Cliente, seu método não está sobrescrevendo aquele método padrão
da classe Object, mas sim crianod um novo método (overload). Por
polimorfismoocompiladorfaráfuncionarnestecasopoisocompiladorfaráa
126

## Página 132

CasadoCódigo Capítulo5. Usandooperadoreseconstruçõesdedecisão
conexãoaométodomaisespecífico,entre Objecte Cliente,eleescolherá
ométodoquerecebe Cliente:
class Cliente {
private String nome;
Cliente(String nome ){
this.nome = nome;
}
public boolean equals(Cliente outro){
return this .nome.equals(outro.nome);
}
}
Cliente c1 = new Cliente( "guilherme");
Cliente c2 = new Cliente( "mario");
System.out.println(c1.equals(c2 )); // false
System.out.println(c1.equals(c1 )); // true
Cliente c3 = new Cliente( "guilherme");
System.out.println(c1.equals(c3 )); // true
System.out.println(c1.equals((Object) c3));
// false, o compilador não sabe que Object é cliente,
// invoca o equals tradicional, e azar do desenvolvedor
Mas caso você use alguma biblioteca (como a API de coleções e de
ArrayListdoJava),oresultadonãoseráoesperado.
1) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 String s1 = "s1";
4 String s2 = "s" + "1";
5 System.out.println(s1==s2);
6 System.out.println(s1==("" + s2));
7 }
8 }
a) Não compila.
127

## Página 133

5.3. TesteaigualdadeentreStringseoutrosobjetosusando==eequals() CasadoCódigo
b) Compila e imprimetrue, false.
c) Compila e imprimetrue, true.
d) Compila e imprimefalse, false.
e) Compila e imprimefalse, true.
2) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 String s1 = "s1";
4 String s2 = s1.substring(0, 1) + s1.substring(1,1);
5 System.out.println(s1==s2);
6 System.out.println(s1.equals(s2 ));
7 }
8 }
a) Não compila.
b) Compila e imprimetrue, false.
c) Compila e imprimetrue, true.
d) Compila e imprimefalse, false.
e) Compila e imprimefalse, true.
3) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 String s1 = "s1";
4 String s2 = s1.substring(0, 2);
5 System.out.println(s1==s2);
6 System.out.println(s1.equals(s2));
7 }
8 }
a) Não compila.
b) Compila e imprimetrue, false.
128

## Página 134

CasadoCódigo Capítulo5. Usandooperadoreseconstruçõesdedecisão
c) Compila e imprimetrue, true.
d) Compila e imprimefalse, false.
e) Compila e imprimefalse, true.
4) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B extends C{}
2 class C{
3 int x;
4 public boolean equals(Cc ){
5 return c.x==x;
6 }
7 }
8 class A{
9 public static void main(String[] args){
10 Ca = new C();
11 Cb = new B();
12 a. x=1 ;
13 b. x=1 ;
14 System.out.println(a==b);
15 System.out.println(a.equals(b));
16 }
17 }
a) Não compila.
b) Compila e imprimetrue, false.
c) Compila e imprimetrue, true.
d) Compila e imprimefalse, false.
e) Compila e imprimefalse, true.
5) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B extends C{}
2 class D{
3 int x;
4 }
129

## Página 135

5.4. Utilizeoifeif/else CasadoCódigo
5 class C{
6 int x;
7 public boolean equals(Object c){
8 return c.x==x;
9 }
10 }
11 class A{
12 public static void main(String[] args){
13 Ca = new C();
14 Cb = new D();
15 a. x=1 ;
16 b. x=1 ;
17 System.out.println(a==b);
18 System.out.println(a.equals(b));
19 }
20 }
a) Não compila.
b) Compila e imprimetrue, false.
c) Compila e imprimetrue, true.
d) Compila e imprimefalse, false.
e) Compila e imprimefalse, true.
5.4 Utilizeoifeif/else
Imagine um programa que aceita comandos do usuário, ou seja, um sistema
interativo. Deacordocomosdadosqueousuáriopassar,oprogramasecom-
porta de maneiras diferentes e, consequentemente, pode dar respostas difer-
entes.
O programador, ao escrever esse programa, deve ter recursos para
definir o comportamento para cada possível comando do usuário, em out-
ras palavras, para cada situação. Com isso, o programa será capaz de tomar
decisõesduranteaexecuçãocomointuitodemudarofluxodeexecução.
As linguagens de programação devem oferecer aos programadores
maneiras parac o n t r o l a rofl u x od ee x e c u ç ã od o sp r o g r a m a s. Dessa forma, os
130

## Página 136

CasadoCódigo Capítulo5. Usandooperadoreseconstruçõesdedecisão
programas podem tomar decisões que afetam a sequência de comandos que
serãoexecutados.
if/else
Amaneiramaissimplesdecontrolarofluxodeexecuçãoédefinirqueum
determinadotrechodecódigodeveserexecutadoquandoumacondiçãofor
verdadeira.
Porexemplo,suponhaumsistemadelogin. Eledeveverificaraautentici-
dade do usuário para permitir ou não o acesso. Isso pode ser implementado
comum if/elsedoJava.
boolean autentico = true;
if (autentico){
System.out.println("Usuario aceito" );
} else {
System.out.println("Usuario incorreto" );
}
Asintaxedo iféaseguinte:
if (CONDICAO){
// CODIGO 1
} else {
// CODIGO 2
}
Acondiçãodeum ifsempretemqueserumvalo rbooleano:
1 if( 1-2 ){} // erro, numero inteiro
2
3 if( 1<2 ){ } //ok, resulta em true
4
5 boolean valor = true;
6 if (valor == false){ } // ok, mas resulta em false
7
8 if (valor){ } // ok, valor é boolean
Atençãodobradaaocódigoaseguir:
131

## Página 137

5.4. Utilizeoifeif/else CasadoCódigo
int a =0 , b =1 ;
if(a = b){
System.out.println("iguais");
}
Estaéumapegadinhabemcomum. Reparequenãoestamosfazendouma
comparaçãoaqui,esim,uma atribuição(umúnico =). Oresultadodeuma
atribuição é sempre o valor atribuído, no caso, um inteiro. Logo, este código
nãoco m p ila,po ispassamosumin teir oparaaco ndiçãodoif.
A única situação em que um código assim poderia funcionar é caso a
variável atribuída seja do tipoboolean, pois o resultado da atribuição será
boolean:
boolean a = true;
if(a = false){
System.out.println("Falso!");
}
N estecaso ,ocódigoco m p ila,masnãoim p rimenada.A pósaa trib uição ,
ovalo rdavariá vel aé false,eo ifnãoéexecutado.
Caso só tenhamos um comando dentro doif ou else,a sc h a v e ss ã o
opcionais:
if(!resultado)
System.out.println("Falso!");
else
System.out.println("Verdadeiro!");
Casonãotenhamosnadaparaserexecutadoemcasodecondição false,
nãop r ecisamosdeclararoelse:
boolean autentico = true;
if (autentico)
System.out.println("Usuario aceito" );
Mas sempre temos que ter algum código dentro doif, se não o código
não compila:
132

## Página 138

CasadoCódigo Capítulo5. Usandooperadoreseconstruçõesdedecisão
boolean autentico = true;
if (autentico)
else // erro
System.out.println("Acesso negado" );
Na linguagem Java,nãoexiste o comandoelseif. Para conseguir o efeito
do“elseif”,osifssãocolocadosdentrodos else.
if (CONDICAO1){
// CODIGO 1
} else if (CONDICAO2){
// CODIGO 2
} else {
// CODIGO 3
}
Grande parte das perguntas sobre estruturas deif/else são pegadin-
has,usandoaindentaçãocomoformadedistração:
boolean autentico = true;
if (autentico)
System.out.println("Usuario aceito" );
else
System.out.println("Usuario incorreto" );
System.out.println("Tente novamente");
A mensagem "Tente novamente" sempre é impressa, independente
dovalordavariável autentico.
Esse foi um exemplo bem simples, vamos tentar algo mais complicado.
Tentedeterminaroqueéimpresso:
int valor = 100;
if (valor > 200)
if (valor <400)
if (valor > 300)
System.out.println("a");
else
System.out.println("b");
else
System.out.println("c");
133

## Página 139

5.4. Utilizeoifeif/else CasadoCódigo
Eentão? "c"? Vamosreindentarocódigoparaverseficamaisfácil:
int valor = 100;
if (valor > 200)
if (valor <400)
if (valor > 300)
System.out.println("a");
else
System.out.println("b");
else
System.out.println("c");
É sempre complicado analisar código não indentado ou mal indentado,
e esse recurso é usado extensivamente em várias questões durante a prova,
fiqueesperto!
UnreachableCodeeMissingreturn
UmcódigoJavanãocompilaseocompiladorperceberqueaquelecódigo
nãoseráexecutadosobhipótesealguma:
class Teste {
public int metodo() {
return 5;
System.out.println("Quando isso será executado?" );
}
}
Teste.java:10: unreachable statement
System.out.println("Quando isso será executado?");
^
Oc ó d i g oa p ó soreturn não será nunca executado. Esse código não
compila. Vamosveralgunsoutrosexemplos:
class Teste {
public int metodo(int x){
if(x > 200) {
return 5;
}
134

## Página 140

CasadoCódigo Capítulo5. Usandooperadoreseconstruçõesdedecisão
}
}
Estetambémnãocompila. Oqueseráretornadose xfor <= 200 ?
Teste.java:12: missing return statement
}
^
1 error
Vamosmodificarocódigoparaqueelecompile:
class Teste {
public int metodo(int x){
if(x >2 00){
return 5;
}
throw new RuntimeException();
}
}
A p e s a rd en ã oe s t a r m o sr e t o r n a n d on a d ac a s ooif seja falso, o Java
percebequenessecasoumaexceçãoserádisparada. Aregraé: todososcam-
inhos possíveis devem retornar o tipo indicado pelo método, ou lançar ex-
ceção.
Emum
if,essaexpressãocompilanormalmente:
if(false) {.... } //compila, apesar de ser unreachable code
Sãopequenosdetalhes,tomecuidadoparanãocairnessaspegadinhas.
1) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 if(args.length > 0)
4 System.out.println("Um ou mais argumentos" );
5 else
6 System.out.println("0");
7 }
8 }
135

## Página 141

5.4. Utilizeoifeif/else CasadoCódigo
a) Não compila: lengthémétodo .
b) N ãoco m p ila:fal to ucha vesnoife else.
c) Seinvocarmossemargumentos,imprime 0.
d) Nuncaimprimirá 0.
2) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{
2 final boolean valor = false;
3 }
4 class A{
5 public static void main(String[] args){
6 Bb = new B();
7 if(b.valor = true){
8 System.out.println("verdadeiro");
9 }
10 }
11 }
a) Não compila.
b) Compila e imprimeverdadeiro.
c) Compilaenãoimprimenada..
3) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 int quantidade = 15;
4 if(quantidade=15) {
5 System.out.println("sim");
6 } else {
7 System.out.println("nao");
8 }
9 }
10 }
a) Não compila.
136

## Página 142

CasadoCódigo Capítulo5. Usandooperadoreseconstruçõesdedecisão
b) Imprime sim.
c) Imprime não.
4) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 if(args.length==1)
4 System.out.println("Um");
5 elseif(args.length==2)
6 System.out.println("Dois");
7 elseif(args.length==3)
8 System.out.println("Três");
9 else
10 System.out.println("Quatro");
11 }
12 }
a) Não compila.
b) Rodaeimprime“Um”quandopassamosumargumento.
c) Rodaeimprime“Três”quandopassamos4argumentos.
d) Rodaenãoimprimenadaquandopassamosnenhumargumento.
5) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 String nome = args[0];
4 if(nome.equals("guilherme"))
5 System.out.println(nome);
6 System.out.println("bom");
7 else
8 System.out.println("melhor ainda");
9 System.out.println(nome);
10 }
11 }
137

## Página 143

5.5. Utilizeoswitch CasadoCódigo
a) Errodecompilaçãono if.
b) Errodecompilaçãono else.
c) Compila e imprime o nome e “bom” caso o primeiro argumento seja
guilherme.
d) Co m p ilaedáerr odeex ecuçãocasonãopas sen enh uma r gum en t ona
linhadecomando.
5.5 Utilizeoswitch
Suponha que um programa tenha que reagir diferentemente para três casos
possíveis. Porexemplo,suponhaqueousuáriopossapassartrêsvalorespos-
síveis:
1, 2e 3.S ef o r1,oprogramadeveimprimir“PRIMEIRAOPCAO”,
sefor 2,“SEGUNDAOPCAO”,esefor 3,“TERCEIRAOPCAO”.
Isso pode ser implementado comif/else. Mas, há uma outra possi-
bilidade. O Java, assim como outras linguagens de programação, oferece o
comandoswitch. Ele permite testar vários casos de uma maneira diferente
do
if/else.
int opcao =1 ;
switch (opcao){
case 1:
System.out.println("PRIMEIRAOPCA O");
case 2:
System.out.println("SEGUNDAOPCA O");
case 3:
System.out.println("TERCEIRAOPCA O");
}
O switch tem uma sintaxe cheia de detalhes e uma semântica pouco
intuitiva. Vamos analisar cada um desses detalhes separadamente para ficar
maissimples.
O argumento do
switch d ev e rse ru m av a ri á v e lc o m p a t í v e lc o mot i po
primitivo int,um wrapperdeumtipomenorque Integer,uma Stringou
umenum. Enums Não são cobrados nessa prova, então vamos focar apenas
noso u tr osdo iscasos.
138

## Página 144

CasadoCódigo Capítulo5. Usandooperadoreseconstruçõesdedecisão
O valor de cadacase deve ser compatível com o tipo do argumento do
switch,casocontrárioserágeradoumerrodecompilaçãonalinhado case
inválido.
//argumento do switch int, e cases int
int valor = 20;
switch (valor){
case 10 : System.out.println(10);
case 20 : System.out.println(20);
}
//Argumento String, e cases String
String s = "Oi";
switch (s){
case "Oi": System .out.println("Olá");
case "Hi": System .out.println("Hello" );
}
//Argumento Byte, e cases byte
Byte b = 10;
switch (b){
case 10: System.out.println("DEZ");
}
//argumento do switch int, e cases string, não compila
int mix = 20;
switch (mix){
case "10" : System.out.println(10);
case "20" : System.out.println(20);
}
Cuidado pois switch de double não faz sentido conforme a lista de
argumentosquecitamoscompatíveiscomo switch!
double mix = 20;
switch (mix){ // não compila
case 10.0 : System.out.println(10);
case 20.0 : System.out.println(20);
}
139

## Página 145

5.5. Utilizeoswitch CasadoCódigo
Vocêpodeusarqualquertipoprimitivomenorqueum intcomoargu-
mentodo switch,desdequeostiposdoscasessejamcompatíveis:
//argumento do switch byte
byte valor = 20;
switch (valor){
// Apesar de ser inteiro, 10 cabe em um byte, o compilador
// fará o cast automaticamente
case 10 :
System.out.println(10);
}
switch (valor){
// Neste caso, o número é muito grande, o compilador não
// fará o cast e teremos um erro de compilação pois os tipos
// são incompatíveis
case 32768 : //erro
System.out.println(10);
}
Em cada case, só podemos usar como valor um literal, uma variável
final atribuída com valor literal, ou expressões envolvendo os dois. Nem
mesmo nullépermitido:
int valor = 20;
final int CINCO =5 ;
int trinta = 30;
switch (valor){
case CINCO: // constante
System.out.println(5);
case 10: // literal
System.out.println(10);
case CINCO *4 : // operação com constante e literal
System.out.println(20);
case trinta: // erro, variável
System.out.println(30);
case trinta + CINCO: //erro, operação envolvendo variável
140

## Página 146

CasadoCódigo Capítulo5. Usandooperadoreseconstruçõesdedecisão
System.out.println(35);
case null : // erro, null em case
System.out.println("null");
}
Constantesemcases
Para ser considerada uma constante em umcase, a variável, além
de ser final, também deve ter sido inicializada durante a sua declaração.
Inicializaravariávelemoutralinhafazcomqueelanãopossaserusada
comovaloremum
case:
int v = 10;
final int DEZ = 10;
final int VINTE; // final, mas não inicializada
VINTE = 20; // inicializada
switch (v){
case DEZ:
System.out.println("DEZ!");
break;
case VINTE: //erro
System.out.println("DEZ!");
break;
}
O switch também aceita a definição de um caso padrão, usando a
palavra default. O caso padrão é aquele que deve ser executado se nen-
hum case“bater”.
int opcao =4 ;
switch (opcao){
case 1:
System.out.println("PRIMEIRA OPCAO");
case 2:
System.out.println("SEGUNDA OPCAO" );
141

## Página 147

5.5. Utilizeoswitch CasadoCódigo
case 3:
System.out.println("TERCEIRA OPCAO");
default:
System.out.println("CASO PADRAO");
}
Umdetalhesobreasintaxedo defaultéqueelepodeaparecerantesde
umoudediversos cases. Destaforma:
int opcao =4 ;
switch(opcao){
case 1:
System.out.println("PRIMEIRA OPCAO");
case 2:
System.out.println("SEGUNDA OPCAO");
default:
System.out.println("CASO PADRAO");
case 3:
System.out.println("TERCEIRA OPCAO");
}
Um comportamento contraintuitivo doswitch éq u e ,q u a n d oe x e c u -
tado,sealgum case“bater”,tudoquevemabaixoéexecutadotambém,todos
os caseseo default, seeleestiverabaixo. Essecomportamentotambém
valesecairno default. Porexemplo,ocódigoanteriorimprime:
CASO PADRAO
TERCEIRA OPCAO
Comessecomportamento,podemosinclusivecriar casessemnenhum
blocodecódigodentro:
int v =1 ;
switch(v){
case 1:
case 2:
case 3:
System.out.println("Até 3");
}
142

## Página 148

CasadoCódigo Capítulo5. Usandooperadoreseconstruçõesdedecisão
Paramudaressecomportamentoenãoexecutaroquevemabaixodeum
case que bater ou dodefault, é necessário usar o comandobreak em
cada case.
int opcao =4 ;
switch(opcao){
case 1:
System.out.println("PRIMEIRA OPCAO");
break;
case 2:
System.out.println("SEGUNDA OPCAO" );
break;
default:
System.out.println("CASO PADRAO");
break;
case 3:
System.out.println("TERCEIRA OPCAO");
break;
}
Nestecaso,sóseráimpresso“TERCEIRAOPCAO”.
1) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 int tamanho = args.length;
4 switch(tamanho){
5 case 1:
6 System.out.println("1");
7 case 2:
8 System.out.println("2");
9 default:
10 System.out.println("mais argumentos");
11 }
12 }
13 }
a) Não compila.
143

## Página 149

5.5. Utilizeoswitch CasadoCódigo
b) Aorodarsemargumentosjogaumaexception..
c) Aorodarcomdoisargumentos,imprimesomente“2”..
d) Aorodarcom5argumentos,imprime“maisargumentos”.
2) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 int tamanhoEsperado =1 ;
4 int tamanho = args.length;
5 switch(tamanho){
6 case tamanhoEsperado:
7 System.out.println("1");
8 break;
9 default:
10 System.out.println("cade o argumento?" );
11 }
12 }
13 }
a) Não compila.
b) Aorodarsemargumentosjogaumaexception.
c) Aorodarcomumargumento,imprimesomente“1”.
d) Aorodarcom5argumentos,imprime“cadeoargumento?”
3) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String [] args){
3 switch("Guilherme"){
4 case "Guilherme":
5 System.out.println("Guilherme");
6 break;
7 case "42":
8 System.out.println("42");
9 default:
144

## Página 150

CasadoCódigo Capítulo5. Usandooperadoreseconstruçõesdedecisão
10 System.out.println("Outro nome" );
11 }
12 }
13 }
a) Nãocompila,poisumnúmeronãopodesercomparadocom String.
b) Compila e imprimeGuilherme.
c )N ã oc o m p i l a ,p o i soc ó d i g od ocase 42 e default nunca serão
executados.
4) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 int count = args.length;
4 switch(count){
5 case 0{
6 System.out.println("nenhum");
7 break;
8 } case 1{
9 } case 2{
10 System.out.println("ok");
11 } default {
12 System.out.println("default");
13 }
14 }
15 }
16 }
a) Errodecompilação.
b) Serodarcom1argumento,imprime okemaisumamensagem.
c) Serodarcom1argumento,nãoimprimenada.
d) Serodarcom5argumentos,imprime default.
e)
5) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
145

## Página 151

5.5. Utilizeoswitch CasadoCódigo
1 class A{
2 public static void main(String[] args){
3 switch(10) {
4 case < 10:
5 System.out.println("menor");
6 default:
7 System.out.println("igual");
8 case > 10:
9 System.out.println("maior");
10 }
11 }
12 }
a) Errodecompilação.
b) Compilaeimprime“igual”.
c) Compilaeimprime“igual”e“maior”.
6) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 switch(10) {
4 case 10:
5 System.out.println("a");
6 break;
7 System.out.println("b");
8 default:
9 System.out.println("c");
10 case 11:
11 System.out.println("d");
12 }
13 }
14 }
a) Não compila.
b) Imprime ae be ce d.
c) Imprime a.
146

## Página 152

Capítulo6
Criandoeusandoarra ys
6.1 Declare,instancie,inicializeeuseumarray
uni-dimensional
As linguagens de programação, normalmente, fornecem algum recurso para
o armazenamento de variáveis em memória sequencial. No Java, os arrays
permitemessetipodearmazenamento.
Um array é um objeto que armazena sequencialmente “uma porção” de
variáveis de um determinado tipo. É importante reforçar que os arrays são
objetos. Uma referência para um objeto array deve ser armazenada em uma
variáveldotipoarray.
Aprovadecertificaçãoverificaseocandidatoestáaptoamanipulartanto
arraysdetiposprimitivosquantodetiposnãoprimitivos.
Osquatropontosimportantessobrearrayssão:

## Página 153

6.1. Declare,instancie,inicializeeuseumarrayuni-dimensional CasadoCódigo
• Declarar
• Inicializar
• Acessar
• Percorrer
Arraysdetiposprimitivos
Declaração:
Paradeclararumarray,éutilizado []logoapósaotipodasvariáveisque
desejamosarmazenaroulogoapósaonomedavariável.
// Declaração de um array para guardar variáveis do tipo int.
int[] idades;
// Declaração de um array para guardar variáveis do tipo double.
double pesos[];
// Declaração de um array para guardar variáveis do tipo long.
long []pesos;
// Declaração de um array para guardar variáveis do tipo long.
long[]tamanhos;
// Perceba as formas de declarar um array.
Inicialização:
Comoumarrayéumobjeto,ainicializaçãoenvolveacriaçãodeumob-
jeto. Onew, operador que cria objetos, é utilizado para construir um array.
Sevocênãoexecutao new,qualovalorpadrão? Paraatributos,é null,epara
variáveislocais,nãohávalor,comoqualqueroutravariáveldereferência:
public class Clientes {
int[] idades;
public static void main(String[] args){
148

## Página 154

CasadoCódigo Ca p í tulo6. Criandoeusandoarra ys
Clientes c = new Clientes ();
System.out.println(c.idades); // imprime null
}
}
public class Produtos {
public static void main(String[] args){
int[] precos;
System.out.println(precos); // nao compila, não foi
// inicializada
}
}
Ecomoinstancioumarray?
// Inicialização do array idades.
idades = new int [10];
// Inicialização do array pesos.
pesos = new double [50];
Nainicialização,édefinidaacapacidadedoarray,ouseja,aquantidadede
variáveisqueeleterá. Quandofalarmosemtamanhodeumarray,estaremos
nosreferindoàsuacapacidade.
Cada variável guardada em um array é iniciada implicitamente no mo-
mento em que o array é criado. Os valores atribuídos às variáveis são os val-
ores
default.
// Imprime 0 pois esse é o valor default para int.
System.out.println(idades[0]);
Etemosalgunscasosextremos:
//compila e roda
int[] numeros = new int [0];
//compila, mas joga NegativeArraySizeException
numeros = new int [-1];
149

## Página 156

CasadoCódigo Ca p í tulo6. Criandoeusandoarra ys
// Coloca o valor 10 na primeira variável do array idades.
int idades[] = new int [10];
idades[0] = 10;
// Coloca o valor 73.14 na última variável do array pesos.
double pesos[] = new double [50];
pesos[49] = 73.14;
Oqueacontecesealguémtentaracessarumaposiçãoquenãoexiste?
// Erro de execução ao tentar acessar um posição que não existe.
// ArrayIndexOutOfBoundsException
pesos[50] = 88.4;
Será gerado um erro de execução (não de compilação). Aexception
lançadapeloJ a vaéArrayIndexOutOfBoundsException.
Percorrendo
Supondo que a capacidade de um array qualquer seja100, os índices
dessearrayvariamde 0até 99,ouseja,de 0atéacapacidademenosum.
O tamanho de um array é definido na inicialização e fica guardado no
próprioarray,podendoserrecuperadoposteriormente.
Para recuperar o tamanho ou a capacidade de um array, é utilizado um
atributochamado lengthpresenteemtodososarrays.
for (int i =0 ; i < idades.length; i++) {
idades[i]= i;
}
No for tradicional, as posições de um array são acessadas através dos
índices. Dessa forma, é possível, inclusive, modificar os valores que estão
armazenadosnoarray.
Porém, em determinadas situações, é necessário apenas ler os valores de
um array sem precisar modificá-los. Nesse caso, pode ser utilizado ofor
introduzidonaversão5doJava.
for(int idade : idades){
System.out.println(idade);
}
151

## Página 157

6.1. Declare,instancie,inicializeeuseumarrayuni-dimensional CasadoCódigo
Não há índices nofor do Java 5. Ele simplesmente percorre os valores.
Assimelenãopermitemodificaroarrayfacilmente.
Arraydereferências
Em cada posição de um array de tipos não primitivos é guardada uma
variávelnãoprimitiva. Esseéumfatofundamental.
// Declarando e iniciando um array de Prova
Prova[] provas = new Prova[10];
Lembrando que o new inicia as variáveis implicitamente e que o valor
padrãoparavariáveisnãoprimitivasé null, todas as dez posições do array
dessecódigoestão nullimedia tamen tea pósonew.
// Erro de execução ao tentar aplicar o operador "."
// em uma referência com valor null.
// NullPointerException
provas[0].tempo = 10;
Para percorrer um array de tipos não primitivos, podemos utilizar um
laço:
for (int i =0 ; i < provas.length; i++){
provas[i]= new Prova ();
provas[i].tempo = 210;
}
for (Prova prova : provas ){
System.out.println(prova.tempo);
}
Casoaclasse Provasejaabstrata,devidoaopolimorfismoépossíveladi-
cionar filhas deProva nesse array: o polimorfismo funciona normalmente,
portantofuncionaigualmenteparainterfaces.
class Prova {
}
class ProvaPratica extends Prova {
}
152

## Página 158

CasadoCódigo Ca p í tulo6. Criandoeusandoarra ys
class Test {
public static void main(String[] args){
Prova[] provas = new Prova[2];
provas[0] = new Prova ();
provas[1] = new ProvaPratica();
}
}
Umavezqueoarraydeobjetosésemprebaseadoemreferências,lembre-
sequeumobjetonãoserácopiado,massomentesuareferênciapassada:
Cliente guilherme = new Cliente();
guilherme.setNome("guilherme");
Cliente[] clientes = new Clientes[10];
clientes[0] = guilherme;
System.out.println(guilherme.getNome()); // guilherme
System.out.println(clientes[0].getNome()); // guilherme
guilherme.setNome("Silveira");
System.out.println(guilherme.getNome()); // silveira
System.out.println(clientes[0].getNome()); // silveira
Castingdearrays
Não hácastingdearraysdetipoprimitivo,portantonãoadiantatentar:
int[] valores = new int [10];
long[] vals = valores ; // não compila
Já no caso de referências, por causa do polimorfismo é possível fazer a
atribuiçãosemcastingdeumarrayparaoutrotipodearray:
String[] valores = new String[2];
valores[0] = "Certificação";
valores[1] = "Java";
Object[] vals = valores;
153

## Página 159

6.1. Declare,instancie,inicializeeuseumarrayuni-dimensional CasadoCódigo
for(Object valor : vals){
System.out.println(valor); // Certificação e depois Java
}
E o casting compila normalmente mas, ao executarmos, um array de
Objectnãoéumarra ydeS tringelevamosuma ClassCastException:
Object[] valores = new Object[2];
valores[0] = "Certificação";
valores[1] = "Java";
String[] vals =( String[]) valores;
for(Object valor : vals){
System.out.println(valor);
}
Issopoisaclassedosdoisédistintaeaclassepaide array de string
nãoéumarraydeobjeto,esim,um Object(lembre-se: todoarrayherdade
Object):
Object[] objetos = new Object[2] ;
String[] strings = new String[2] ;
System.out.println(objetos.getClass().getName());
// [ Ljava.lang.Object;
System.out.println(strings.getClass().getName());
// [ Ljava.lang.String;
System.out.println(strings.getClass().getSuperclass());
// java.lang.Object
1) Escolhaaopçãoquenãocompila:
a) int[] x ;
b) int x[] ;
c) int[]x;
d) int [] x ;
e) int[] x ;
f) []int x ;
154

## Página 160

CasadoCódigo Ca p í tulo6. Criandoeusandoarra ys
2) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 int x[] = new int [30];
4 int y[] = new int [3] {0,3,5};
5 }
6 }
a) Aprimeiralinhanãocompila.
b) Asegundalinhanãocompila.
c) Ocódigoco m p ilaer oda.
3) Escolha a opção adequada ao tentar compilar e rodar o arquivo a seguir,
emrelaçãoaslinhasdentrodométodomain:
1 class A{
2 public static void main(String[] args){
3 int x[] = new int [0];
4 int x[] = new int [] {0,3,5};
5 int x[] = {0,3,5};
6 }
7 }
a) Aprimeiraesegundalinhasnãocompilam.
b) Asegundaeterceiralinhasnãocompilam.
c) Somenteaterceiralinhanãocompila.
d) Oprogramacompilaeroda,dandoumaexception.
e) Oprogramacompilaeroda,imprimindonada.
4) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 int x[] = new int [3];
4 for(int i=x.length;i>=0;i--) x[i]=i*2;
155

## Página 161

6.1. Declare,instancie,inicializeeuseumarrayuni-dimensional CasadoCódigo
5 System.out.println("Fim!");
6 }
7 }
a) Oprogramanãocompila
b) Op r ogramaim p rimeFim.
c) Op r ogramaco m p ilaedáerr oemexecução .
5) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 int x[] = new int [3];
4 for(x[1]=x.length-1;x[0]==0;x[1]--) {
5 x[x[1]]=-5;
6 System.out.println(x[1]);
7 }
8 }
9 }
a) Não compila.
b) Compila,imprimealgunsnúmerosedáuma Exception.
c) Compilaenãoimprimenada.
d) Compila e imprime2.
e) Compila e imprime-5.
f) Compila e imprime2, -5.
g) Compila e imprime2, -5, -5.
h) Compila e imprime2, 1, -5.
i) Compila e imprime-5, -5.
j) Dáexception.
6) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
156

## Página 162

CasadoCódigo Ca p í tulo6. Criandoeusandoarra ys
1 class A{
2 public static void main(String[] args){
3 int x[] = new int [3];
4 for(x[1]=x .length-1;x[1]>=0;x[1]--) {
5 x[x[1]]=-5;
6 System.out.println(x[1]);
7 }
8 }
9 }
a) Não compila.
b) Compila,imprimealgunsnúmerosedáuma Exception.
c) Compilaenãoimprimenada.
d) Compila e imprime2.
e) Compila e imprime-5.
f) Compila e imprime2, -5.
g) Compila e imprime2, -5, -5.
h) Compila e imprime2, 1, -5.
i) Compila e imprime-5, -5.
j) Dáexception.
7) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 String[] valores = new String[2];
4 valores[0] = "Certificação";
5 valores[1] = "Java";
6 Object[] vals =( Object[]) valores;
7 vals[1] = "Daniela";
8 System.out.println(vals[1].equals(valores[1]));
9 }
10 }
a) Ocódigonãocompila.
157

## Página 163

6.2. Declare,instancie,inicializeeuseumarraymulti-dimensional CasadoCódigo
b) Ocódigoco m p ilaedáerr oemexecução .
c) Ocódigoco m p ilaeim p rimefalse.
d) Ocódigoco m p ilaeim p rimetrue.
8) Quais das maneiras adiante são declarações e inicializações válidas para
umarray?
a) int[] array = new int[10];
b) int array[] = new int[10];
c) int[] array = new int[];
d) int array[] = new int[];
e) int[] array = new int[2]{1, 2};
f) int[] array = new int[]{1, 2};
g) int[] array = int[10];
h) int[] array = new int[1, 2, 3];
i) int array[] = new int[1, 2, 3];
j) int array[] = {1, 2, 3};
6.2 Declare, instancie, inicialize e use um ar-
raymulti-dimensional
Podemosgeneralizaraideiadearrayparaconstruirarraysdeduasdimensões,
em outras palavras,arraydearrays. Analogamente, podemos definir arrays
dequantasdimensõesquisermos.
Declaração:
// Um array de duas dimensões.
int[][] tabela;
// Um array de três dimensões.
int[][] cubo[];
158

## Página 164

CasadoCódigo Ca p í tulo6. Criandoeusandoarra ys
// Um array de quatro dimensões.
int[] [][]hipercubo[];
// Perceba que as dimensões podem ser definidas do lado
// esquerdo ou direito da variável.
Inicialização:
// Inicializando a primeira dimensão com 1 0 e a segunda com 15
tabela = new int[10][15];
// Inicializando a primeira dimensão com 10 e deixando as outras
// para serem iniciadas depois
cubo = new int[10][][];
// Inicializando com valores
int[][] teste = new int [][]{{1,2,3},{3,2,1},{1,1,1}};
Acesso:
// Acessando a posição (0,1)
System.out.println(tabela[0][1]);
Podemos criar um array que não precisa ser “quadrado”, ele pode ter
tamanhosestranhos:
int[][] estranha = new int[2][];
estranha[0] = new int [20];
estranha[1] = new int [10];
for(int i=0;i< estranha.length;i++) {
System.out.println(estranha[i].length); // imprime 20 e 10
}
1) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 int zyx[][]=new int[3];
4 int[]x=new int [20];
159

## Página 165

6.2. Declare,instancie,inicializeeuseumarraymulti-dimensional CasadoCódigo
5 int[]y=new int [10];
6 int[]z=new int [30];
7 zyx[0]=x;
8 zyx[1]=y;
9 zyx[2]=z;
10 System.out.println(zyx[2].length);
11 }
12 }
a) N ãoco m p ila,err oaodeclararzyx.
b) Compilaedáerroaotentaratribuirosegundoarraya zyx.
c) Co m p ilaedáerr oaoten tarim p rimirotamanhodoarra y .
d) Compilaeimprime10.
e) Compilaeimprime20.
f) Compila e imprime 30.
2) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 int zyx[][]=new int[3][];
4 int[]x=new int [20];
5 int[]y=new int [10];
6 int[]z=new int [30];
7 zyx[0]=x;
8 zyx[1]=y;
9 zyx[2]=z;
10 System.out.println(zyx[2].length);
11 }
12 }
a) N ãoco m p ila,err oaodeclararzyx.
b) Compilaedáerroaotentaratribuirosegundoarraya zyx.
c) Co m p ilaedáerr oaoten tarim p rimirotamanhodoarra y .
d) Compilaeimprime10.
160

## Página 166

CasadoCódigo Ca p í tulo6. Criandoeusandoarra ys
e) Compilaeimprime20.
f) Compila e imprime 30.
3) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 int zyx[][]=new int[3][10];
4 int[]x=new int [20];
5 int[]y=new int [10];
6 int[]z=new int [30];
7 zyx[0]=x;
8 zyx[1]=y;
9 zyx[2]=z;
10 System.out.println(zyx[2].length);
11 }
12 }
a) N ãoco m p ila,err oaodeclararzyx.
b) Não compila, erro ao atribuir arrays de tamanho diferente de10 em
zyx.
c) Compilaedáerroaotentaratribuirosegundoarraya zyx.
d) Co m p ilaedáerr oaoten tarim p rimirotamanhodoarra y .
e) Compilaeimprime10.
f) Compila e imprime 20.
g) Compila e imprime 30.
4) class Teste {
public static void main(String[] args){
int[] idades = new int [10];
idades[0] = 1.0;
int[10][10] tabela = new int [10][10];
int[][][] cubo = new int [][][];
}
}
161

## Página 167

6.3. DeclareeuseumaArrayList CasadoCódigo
a) Ocódigonãocompila.
b) Ocódigoco m p ilaedáerr oemexecução .
c) Ocódigoco m p ilaer oda.
Compila? Roda?
6.3 DeclareeuseumaArrayList
Nestaprova,veremossomentea ArrayList,umalistaqueusainternamente
umarray. Rápidanométodo get,poissuaestruturainternapermiteacesso
aleatório(randomaccess)emtem poco nstan te.
J amaisseesqueçadeim po rtaraArrayList:
import java.util.ArrayList;
Op rimeir opassoécriaruma ArrayListvaziade Strings:
ArrayList<String> nomes = new ArrayList<String>();
A ArrayList herda diversos métodos abstratos e concretos e veremos
vários deles aqui, dentre esses, os principais para a certificação, vindos da
interface Collection.
Porexemplo,paraadicionaritens,fazemos:
ArrayList<String> nomes = new ArrayList<String>();
nomes.add("certificação");
nomes.add("java");
Pararemovereverificaraexistênciadomesmonalista:
ArrayList<String> nomes = new ArrayList<String>();
nomes.add("certificação");
nomes.add("java");
System.out.println(nomes.contains("java")); // true
System.out.println(nomes.contains("c#")); // false
// true, encontrado e removido
162

## Página 168

CasadoCódigo Ca p í tulo6. Criandoeusandoarra ys
boolean removido = nomes.remove("java");
System.out.println(nomes.contains("java")); // false
System.out.println(nomes.contains("c#")); // false
Note que oremove remove somente a primeira ocorrência daquele ob-
jeto.
Podemostambémverificarotamanhodenossa ArrayList:
ArrayList<String> nomes = new ArrayList<String>();
nomes.add("certificação");
nomes.add("java");
System.out.println(nomes.size()); // imprime 2
Eco n vertê-laparaumarra y:
ArrayList<String> nomes = new ArrayList<String>();
nomes.add("certificação");
nomes.add("java");
Object[] nomesComoString = nomes.toArray();
Caso desejarmos um array de String, devemos indicar isso ao método
toArraydeduasformasdiferentes:
ArrayList<String> nomes = new ArrayList<String>();
nomes.add("certificação");
nomes.add("java");
String[] nomes2 = nomes.toArray(new String[0]);
String[] nomes3 = nomes.toArray(new String[nomes.size()]);
AmbaspassamumarraydeString: oprimeiromenoreosegundocomo
tamanhosuficienteparaoselementos. Seelepossuiotamanhosuficiente,ele
mesmoseráusado,enquantoque,seotamanhonãoésuficiente,o toArray
criaumnovoarraydomesmotipo.
Alémdisso,podemosadicionarumacoleçãointeiraemoutra:
163

## Página 169

6.3. DeclareeuseumaArrayList CasadoCódigo
ArrayList<String> nomes = new ArrayList<String>();
nomes.add("certificação");
nomes.add("java");
ArrayList<String> paises = new ArrayList<String>();
paises.add( "coreia");
paises.add( "brasil");
ArrayList<String> tudo = new ArrayList<String >();
tudo.addAll(nomes);
tudo.addAll(paises);
System.out.println(tudo.size()); // imprime 4
Outros métodos são específicos da interface List e recebem uma
posição específica onde você quer colocar ou remover algo do array usado
na ArrayList.Om é t o d oget devolve o elemento na posição desejada,
lembrandoquecomeçamossemprecom0:
ArrayList<String> nomes = new ArrayList<String>();
nomes.add("certificação");
System.out.println(nomes.get(0)); // imprime certificação
J áométodo addfoisobrecarregadoparareceberaposiçãodeinclusão:
ArrayList<String> nomes = new ArrayList<String>();
nomes.add("certificação");
System.out.println(nomes.get(0)); // imprime certificação
nomes.add(0, "java");
System.out.println(nomes.get(0)); // imprime java
System.out.println(nomes.get(1)); // imprime certificação
Omesmoaconteceparaométodo remove:
ArrayList<String> nomes = new ArrayList<String>();
nomes.add("java");
nomes.add("certificação");
String removido = nomes.remove(0); // retorna java
System.out.println(nomes.get(0)); // imprime certificação
164

## Página 170

CasadoCódigo Ca p í tulo6. Criandoeusandoarra ys
Eom é t o d oset, que serve para alterar o elemento em determinada
posição:
ArrayList<String> nomes = new ArrayList<String>();
nomes.add("java");
nomes.set(0, "certificação");
System.out.println(nomes.get(0)); // imprime certificação
System.out.println(nomes.size()); // imprime 1
Osmétodos indexOfe lastIndexOfretornamaprimeiraouaúltima
posição que possui o elemento desejado. Caso esse elemento não esteja na
lista,eleretorna-1:
ArrayList<String> nomes = new ArrayList<String>();
nomes.add("guilherme");
nomes.add("mario");
nomes.add("paulo");
nomes.add("mauricio");
nomes.add("adriano");
nomes.add("alberto");
nomes.add("mario");
System.out.println(nomes.indexOf("guilherme")); // 0
System.out.println(nomes.indexOf("mario")); // 1
System.out.println(nomes.indexOf("joao" )); // -1
System.out.println(nomes.lastIndexOf("mario")); // 6
System.out.println(nomes.lastIndexOf("joao")); // -1
Iteratoreoenhancedfor
Ainterface Iteratordefineumamaneiradepercorrercoleções. Issoé
necessárioporque,emcoleçõesdiferentesde List,nãopossuímosmétodos
para pegar o enésimo elemento. Como, então, percorrer todos os elementos
deumacoleção?
• hasNext: retorna um booleano indicando se ainda há elementos a
serempercorridosporesseiterador;
165

## Página 171

6.3. DeclareeuseumaArrayList CasadoCódigo
• next: pulaparaopróximoelemento,devolvendo-o;
• remove: removeoelementoatualdacoleção.
Ocódigoquecostumaaparecerparapercorrerumacoleçãoéos eguinte:
Collection< String> strings = new ArrayList<String>();
Iterator<String> iterator = strings.iterator();
while (iterator .hasNext()) {
String atual = iterator.next();
System.out.println(atual);
}
O enhanced-fortambémpodeserusadonessecaso:
Collection< String> strings = new ArrayList<String>();
for (String atual : strings){
System.out.println(atual);
}
Ométodoequalsemcoleções
Amaioriaabsolutadascoleçõesusaométodo equalsnahoradebuscar
porelementos,comonosmétodos containse remove. Sevocêdesejaser
capazderemoveroubuscarelementos,teráqueprovavelmentesobrescrevero
método equalspararefletiroconceitodeigualdadeemqueestáinteressado,
enãosomenteaigualdadedereferência(implementaçãopadrãodométodo).
Cuidadoaotentarsobrescreverométodo equals,sevocêescrevê-lore-
cebendoumtipoespecíficoemvezde Object,nãooestarásobrescrevendo,
eo ArrayList continuará invocando o código antigo, a implementação
padrãode equals!
ArrayListereferências
ValelembrarqueJavasempretrabalhacomreferênciasparaobjetos,enão
criacópiasdeobjetoscadavezqueosatribuímosaumavariáveloureferência:
Cliente guilherme = new Cliente();
guilherme.setNome("guilherme");
166

## Página 172

CasadoCódigo Ca p í tulo6. Criandoeusandoarra ys
ArrayList<Cliente> clientes = new ArrayList< Cliente>();
clientes.add(guilherme);
System.out.println(guilherme.getNome()); // guilherme
System.out.println(clientes.get(0).getNome()); // guilherme
guilherme.setNome("Silveira");
System.out.println(guilherme.getNome()); // Silveira
System.out.println(clientes.get(0).getNome()); // Silveira
1) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 ArrayList< String> c = new ArrayList<String>();
4 c.add("a");
5 c.add("c");
6 System.out.println(c.remove("a"));
7 }
8 }
a) N ãoco m p ila:err oaodeclararaArrayList.
b) N ãoco m p ila:err oaoin vocarremove.
c) Compilaeaorodarimprime a.
d) Compilaeaorodarimprime true.
e) Compilaeaorodarimprime false.
2) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 import java.util.ArrayList;
2 class A{
3 public static void main(String [] args){
4 ArrayList< String> c = new ArrayList<String>();
5 c.add("a");
167

## Página 173

6.3. DeclareeuseumaArrayList CasadoCódigo
6 c.add("c");
7 System.out.println(c.remove("a" ));
8 }
9 }
a) N ãoco m p ila:err oaodeclararaArrayList.
b) N ãoco m p ila:err oaoin vocarremove.
c) Compilaeaorodarimprime a.
d) Compilaeaorodarimprime true.
e) Compilaeaorodarimprime false.
3) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 import java.util.ArrayList;
2 class A{
3 public static void main(String[] args){
4 ArrayList<String> c = new ArrayList<String>();
5 c.add("a");
6 c.add("a");
7 System.out.println(c.remove("a" ));
8 System.out.println(c.size());
9 }
10 }
a) N ãoco m p ila:err oaodeclararaArrayList.
b) N ãoco m p ila:err oaoin vocarremove.
c) Compilaeaorodarimprime ae0.
d) Compilaeaorodarimprime truee0.
e) Compilaeaorodarimprime ae1.
f) Co m p ilaeaor odarim p rimetruee1.
g) Compilaeaorodarimprime ae2.
h) Compilaeaorodarimprime truee2.
4) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
168

## Página 174

CasadoCódigo Ca p í tulo6. Criandoeusandoarra ys
1 import java.util.ArrayList;
2 class A{
3 public static void main(String[] args){
4 ArrayList< String> list = new ArrayList<>();
5 list.add("a");list.add("b");
6 list.add("a");list.add("c");
7 list.add("a");list.add("b");
8 list.add("a");
9 System.out.println(list.lastIndexOf("b"));
10 }
11 }
a) Não compila.
b) Compilaeimprime-1.
c) Compila e imprime 0.
d) Compila e imprime 1.
e) Compila e imprime 2.
f) Compila e imprime 3.
g) Compila e imprime 4.
h) Compila e imprime 5.
i) Compila e imprime 6.
j) Compila e imprime 7.
5) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 import java.util.ArrayList;
2 class A{
3 public static void main(String[] args){
4 ArrayList< String> l = new ArrayList<String>();
5 l.add("a");
6 l.add("b");
7 l.add(1,"amor");
8 l.add(3,"baixinho");
9 System.out.println(l);
10 String[] array = l.toArray();
169

## Página 175

6.3. DeclareeuseumaArrayList CasadoCódigo
11 System.out.println(array[2]);
12 }
13 }
a) Não compila.
b) Compila e imprime “amor”.
c) Compila e imprime “b”.
6) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 import java.util.ArrayList;
2 class A{
3 public static void main(String[] args){
4 ArrayList<String> a = new ArrayList<String>();
5 ArrayList<String> b = new ArrayList<String>();
6 ArrayList<String> c = new ArrayList<String>();
7 b.add("a"); c.add("c");
8 b.add("b"); c.add("d");
9 a.addAll(b);
10 a.addAll(c);
11 System.out.println(a.get(0));
12 System.out.println(a.get(3));
13 }
14 }
a) Não compila
b) Compila e imprimeae d.
c) Compila e imprimece b.
d) Compilaenãosabemosaordememqueoselementosserãoimpressos.
7) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 import java.util.ArrayList;
2 class A{
3 public static void main(String[] args){
4 ArrayList<String> a = new ArrayList<String>();
170

## Página 176

CasadoCódigo Ca p í tulo6. Criandoeusandoarra ys
5 a.add("a", 0);
6 a.add("b", 0);
7 a.add("c", 0);
8 a.add("d", 0);
9 System.out.println(a.get(0));
10 System.out.println(a.get(1));
11 System.out.println(a.get(2));
12 System.out.println(a.get(3));
13 }
14 }
a) Não compila.
b) Compila e imprimeabcd.
c) Compila e imprimedcba.
d) Compila e imprimeadcb.
e) Compila e imprimebcda.
8) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 import java.util.*;
2 class A{
3 public static void main(String[] args){
4 ArrayList<String> a = new ArrayList<String>();
5 a.add(0,"b" );
6 a.add(0,"a" );
7 for(Iterator<String > i=a.iterator();i.hasNext();i.next()) {
8 String element = i.next();
9 System.out.println(element);
10 }
11 }
12 }
a) Não compila.
b) Compila e imprimea.
c) Compila e imprimeae b.
d) Compila e imprimebe a.
171

## Página 177

6.3. DeclareeuseumaArrayList CasadoCódigo
e) Compila e imprimeb.
9) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 import java.util.ArrayList;
2 class A{
3 public static void main(String[] args){
4 ArrayList<String> ss = new ArrayList<String>();
5 ss.add("a");
6 ss.add("b");
7 ss.add("c");
8 ss.add("d");
9
10 for(String s:ss ){
11 if(s.equals("c")) s = "b";
12 else if(s.equals("b")) s= "c";
13 }
14 for(String s:ss ) System.out.println(s);
15 }
16 }
a) Não compila, sé finalporpadrão.
b) Compila e imprimea, c, b, d.
c) Compila e imprimea, b, c, d.
d) Compila e imprimea, c, c, d.
e) Compila e imprimea, c, b, d.
172

## Página 178

Capítulo7
Usandolaços
7.1 Crieeuselaçosdotipowhile
Outra maneira de controlar o fluxo de execução de um programa é definir
queumdeterminadotrechodecódigodeveexecutarváriasvezes,comouma
r epetiçãoo uumlaço .
UmalinguagemcomooJavaoferecealgunstiposdelaçosparaoprogra-
madorescolher. Ocomando
whileéumdeles.
int i =1 ;
while (i < 10) {
System.out.println(i);
i++;
}
Asintaxedo whileéaseguinte:

## Página 179

7.1. Crieeuselaçosdotipowhile CasadoCódigo
while (CONDICAO ){
// CODIGO
}
Assim como no if, a condição de um bloco while deve ser um
booleano. Da mesma maneira, se o bloco de código tiver apenas uma linha,
podemosomitiraschaves:
int i =0 ;
while( i < 10)
System.out.println(i++);
Ocorpodo whileéexecutadorepetidamenteatéqueacondiçãosetorne
falsa. Emoutraspalavras,enquantoacondiçãoforverdadeira.
Énecessáriotomarcuidadoparanãoescreverum whileinfinito,ouseja,
umlaçoquenãoterminariasefosseexecutado.
int i =1 ;
//Quando fica false?
while(i < 10){
System.out.println(i);
}
Em casos em que é explícito que o loop será infinito, o compilador é es-
pertoenãodeixacompilarcasotenhaalgumcódigoapósolaço:
class A{
int a() {
while(true){ //nunca fica false
System.out.println("Faz algo" );
}
return 1; // não compila, nunca chegará aqui
}
}
Mesmo que a condição use uma variável, pode ocorrer um erro de com-
p ilação ,casoavariá velsejafinal:
class A{
int a() {
174

## Página 180

CasadoCódigo Capítulo7. Usandolaços
final boolean RODANDO = true;
while(RODANDO){
System.out.println("Fazalgo");
}
return 1; // não compila, nunca chegará aqui
}
}
Agora, caso a variável não seja final, o compilador não tem como saber
seovalorirámudarounão,pormaisexplícitoquepossaparecer,eocódigo
compilanormalmente:
class A{
int a() {
boolean rodando = true; // não final
while(rodando){
System.out.println("Fazalgo");
}
return 1;
// compila, não tem como saber se o valor de rodando
// vai mudar
}
}
Casoumlaçonuncasejaexecutado,tambémteremosumerrodecompi-
lação:
//unreachable statement, não compila.
while(false ){ //código aqui }
//unreachable statement, não compila.
while( 1>2 ){ //código aqui }
Lembre-sequeocompiladorsóconsegueanalisaroperaçõescomliterais
oucomconstantes. Nocasoaseguir,ocódigocompila,mesmonuncasendo
executado:
int a =1 ;
int b =2 ;
175

## Página 181

7.1. Crieeuselaçosdotipowhile CasadoCódigo
while(a > b){ //compila, mas nunca executa
System.out.println("OI");
}
1) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 int a = 10;
4 while(a>100) a ++;
5 System.out.println(a);
6 }
7 }
a) Nãocompilapoisnuncaentranoloop.
b) Compilaeimprime99.
c) Compilaeimprime100.
d) Compilaeimprime101.
e) Compilaeimprimeoutrovalor.
2) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 boolean rodar = true;
4 while(rodar ){
5 System.out.println(rodar);
6 }
7 System.out.println("Terminou");
8 }
9 }
a) T ransfo rmaravariá velemfinalfazocódigocompilar.
b) Colocar uma linha dentro do laço que fazrodar = false faz o
códigocompilar.
c) Ocódigocompilaerodaemloopinfinito.
176

## Página 182

CasadoCódigo Capítulo7. Usandolaços
d) O código compila e roda, após algumas passagens pelo laço ele im-
primeumaexceptionepara.
7.2 Crieeuselaçosdotipofor,incluindooen-
hancedfor
Observando um pouco os códigos que utilizamwhile, dá para perceber
queelessãoformadosporquatropartes: inicialização,condição,comandose
atualização.
int i =1 ; // Inicialização
while (i < 10) { // Condição
System.out.println(i); // Comandos
i++; // Atualização
}
A inicialização é importante para que o laço execute adequadamente.
Mesmocomessaimportância ,ainicializaçãoficaseparadado while.
A atualização é fundamental para que não aconteça um “loop infinito”.
Porém,asintaxedo whilenãoacolocaemevidência.
Há um outro laço que coloca em destaque a inicialização, a condição e a
atualização. Esselaçoéo for.
for (int i =1 ; i < 10; i++) {
System.out.println(i);
}
O fortemtrêsargumentosseparadospor ;. Oprimeiroéainicialização,
osegundo,acondição ,eoter ceiro,aatualização.
A inicialização é executada somente uma vez no começo dofor.A
condição é verificada no começo de cada rodada (iteração). A atualização
éexecutadanofimdecadaiteração.
Todosostrêsargumentosdo
forsãoopcionais. Destaforma,vocêpode-
riaescreveroseguintecódigo:
for(;;){
// CODIGO
}
177

## Página 183

7 .2. Crieeuselaçosdoti pofo r ,incl uindooenhancedfo r CasadoCódigo
Oqueacontececomesselaço? Pararesponderessaperguntaénecessário
saber quais são os “valores default” colocados nos argumentos dofor,
quando não é colocado nada pelo programador. A inicialização e a atual-
ização ficam realmente vazias. Agora, a condição recebe por padrão o valor
true. Então,ocódigoanteriordepoisdecompiladoficaassim:
//loop infinito
for (;true;){
// CODIGO
}
Nos exemplos anteriores, basicamente o que fizemos na inicialização foi
declarar e inicializar apenas uma variável qualquer. Porém, é permitido
declarardiversasvariáveisdeummesmotipoouinicializardiversasvariáveis.
Na inicialização, não é permitido declarar variáveis de tipos diferentes.
Masépossívelinicializarvariáveisdetiposdiferentes. Vejaosexemplos:
// Declarando três variáveis do tipo int e inicializando as três.
// Repare que o "," separa as declarações e inicializações.
for (int i =1 , j =2 , k = 3;;){
// CODIGO
}
// Declarando três variáveis de tipos diferentes
int a;
double b;
boolean c;
// Inicializando as três variáveis já declaradas
for (a =1 , b = 2.0, c = true;;){
// CODIGO
}
Naatualização,épossívelfazerdiversasatribuiçõesseparadaspor ,.
//a cada volta do laço, incrementamo soiedecrementamos o j
for (int i=1,j=2;; i++,j--){
//código
}
178

## Página 184

CasadoCódigo Capítulo7. Usandolaços
Como já citamos anteriormente, não é possível inicializar variáveis de
tiposdiferentes:
for (int i=1, long j=0; i< 10; i++){ // erro
//código
}
No campo de condição, podemos passar qualquer expressão que resulte
emum boolean. Sãoexatamenteasmesmasregrasdo ife while.
No campo de atualização, não podemos só usar os operadores de incre-
mento,podemosexecutarqualquertrechodecódigo:
for (int i =0 ; i < 10; i += 3) { //somatório
//código
}
for (int i =0 ; i < 10; System.out.println(i++)) { // bizarro
//código
}
Enhancedfor
Quandovamospercorrerumacoleçãodeobjetosouumarray,podemos
usarumaversãosimplificadado forparapercorreressacoleçãodemaneira
simplificada. Essa forma simplificada é chamada deenhanced for,o uforeach
:
int[] numeros = {1,2,3,4,5,6};
for (int num : numeros){ //enhanced for
System.out.println(num);
}
A sintaxe é mais simples, temos agora 2 partes dentro da declaração do
for:
for(VARIAVEL : COLEÇÃO){
CODIGO
}
179

## Página 185

7 .2. Crieeuselaçosdoti pofo r ,incl uindooenhancedfo r CasadoCódigo
Nesse caso, declaramos uma variável que irá receber cada um dos mem-
brosdacoleçãoouarrayqueestamospercorrendo. Opróprio foriráacada
iteraçãodolaçoatribuiropróximoelementodalistaàvariável. Seriaoequiv-
alenteafazeroseguinte:
int[] numeros = {1,2,3,4,5,6};
for( int i=0; i < numeros.length; i++){
int num = numeros[i]; //declaração da variável e atribuição
System.out.println(num);
}
Se fosse umacollection, o código fica mais simples ainda se comparado
como fororiginal:
ArrayList<String> nomes = //lista com vários nomes
//percorrendo a lista com o for simples
for(Iterator<String > iterator = nomes.iterator();
iterator.hasNext();){
String nome = iterator.next();
System.out.println(nome);
}
//percorrendo com o enhanced for
for (String nome : nomes){
System.out.println(nome);
}
Existem,porém,algumaslimitaçõesno enhancedfor. Nãopodemos,por
exemplo, modificar o conteúdo da coleção que estamos percorrendo usando
avariávelquedeclaramos:
ArrayList<String> nomes = //lista com vários nomes
//tentando remover nomes da lista
for (String nome : nomes){
nome = null;
}
180

## Página 186

CasadoCódigo Capítulo7. Usandolaços
//o que imprime abaixo?
for (String nome : nomes){
System.out.println(nome);
}
Aoexecutaressecódigo,vocêperceberáqueacoleçãonãofoimodificada,
nenhumelementomudoudevalorpara null.
Outralimitaçãoéquenãoháumamaneiranaturaldesaberemqualiter-
ação estamos, já que não existe nenhum contador. Para saber em qual linha
estamos,precisaríamosdeumcontadorexterno. Tambémnãoépossívelper-
correr duas coleções ao mesmo tempo, já que não há um contador central-
izado. Paratodosessescasos,érecomendadousaro
forsimples.
1) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 for(;;) {
4 System.out.println("a");
5 }
6 System.out.println("b");
7 }
8 }
a) Não compila.
b) Compila e imprimeainfinitamente.
c) Compila e imprimeb.
d) Compila e imprimea,depois b,depoispara.
e) Compila, imprime a diversas vezes e depois dá um
StackOverflowError.
2) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
181

## Página 187

7 .2. Crieeuselaçosdoti pofo r ,incl uindooenhancedfo r CasadoCódigo
3 for(;false;) {
4 System.out.println("a");
5 break;
6 }
7 System.out.println("b");
8 }
9 }
a) Não compila.
b) Compila e imprimeb.
c) Compila,imprime ae b.
3) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 for(int i=0, int j=1; i<10; i++, j++) System.out.println(i);
4 }
5 }
a) Não compila.
b) Co m p ilaeim p rime0a té9.
c) Co m p ilaeim p rime0a té10.
d) Co m p ilaeim p rime1a té10.
e) Co m p ilaeim p rime1a té11.
4) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 for(int i=0, j=1; i<10 ;i ++, j++) System.out.println(i);
4 }
5 }
a) Não compila.
b) Co m p ilaeim p rime0a té9.
182

## Página 188

CasadoCódigo Capítulo7. Usandolaços
c) Co m p ilaeim p rime0a té10.
d) Co m p ilaeim p rime1a té10.
e) Co m p ilaeim p rime1a té11.
5) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 for(int i=0; i<10, false; i++) {
4 System.out.println('a');
5 }
6 System.out.println('b');
7 }
8 }
a) Não compila.
b) Co m p ilaeim p rime‘ a ’e‘b ’ .
c) Compila e imprime ‘b’.
6) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 for(int i=0; i<2; i++, System.out.println(i)) {
4 System.out.println(i);
5 }
6 }
7 }
a) Não compila.
b) Compila e imprime012 .
c) Compila e imprime001122 .
d) Compila e imprime01122 .
e) Compila e imprime0112 .
183

## Página 189

7.3. Crieeusolaçosdotipodo/while CasadoCódigo
7.3 Crieeusolaçosdotipodo/while
U maoutraopçãodelaço whileseriao do .. while ,queébemparecido
com o while. A grande diferença é que a condição é testada após o corpo
doloopserexecutadopelomenosumavez:
int i =1 ;
do { //executa ao menos 1 vez
System.out.println(i);
i++;
} while (i <10); // se der true, volta e executa novamente.
A condição do do .. while só é verificada no final de cada iteração
e não no começo, como nowhile. Repare que ao final do blocodo ..
whileexisteumpontoevírgula. Esseéumdetalhequepassadesapercebido
muitasvezes,masqueresultaemerrodecompilaçãoseomitido:
int i =1 ;
do {
System.out.println(i);
i++;
} while (i <10) // não compila, faltou o ;
Assimcomono while, casotenhamosapenasumalinha, aschavespo-
dem ser omitidas. Caso exista mais de uma linha dentro dodo .. while
enãoexistamchaves,teremosumerrodecompilação:
int i =0 ;
//compila normal
do
System.out.println(i++);
while(i<10);
//erro, mais de uma linha dentro do do .. while
do
System.out.print("o valor é: " ); //erro
System.out.println(i++);
while(i<10);
184

## Página 190

CasadoCódigo Capítulo7. Usandolaços
1) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 boolean i = false;
4 do {
5 System.out.println(i);
6 } while(i);
7 }
8 }
a) Não compila.
b) Compila e imprimefalse.
c) Compilaenãoimprimenada.
2) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 if(args.length< 10) {
4 do {
5 if(args.length>2) return;
6 } while(true);
7 }
8 System.out.println("Finalizou" );
9 }
10 }
a) Não compila.
b) Compila e entra em loop infinito caso seja passado zero, um ou dois
argumentos. Não imprime nada caso 3 a 9 argumentos. Imprime ‘Fi-
nalizou’caso10oumaisargumentos.
c) Compila e entra em loop infinito caso seja passado zero, um ou dois
argumentos. Imprime‘Finalizou’casocontrário.
d) Compilaesempreentraemloopinfinito.
185

## Página 191

7.3. Crieeusolaçosdotipodo/while CasadoCódigo
3) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 int i =0 ;
4 do System.out.println(i); while(i++>10);
5 }
6 }
a) Não compila.
b) Compilaenãoimprimenada.
c) Compila e imprime0.
d) Compila e imprime de0até 9.
e) Compila e imprime de0até 10.
f) Compilaenãoimprimenada.
4) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 int i =0 ;
4 do System.out.println(i) while(i++<10);
5 }
6 }
a) Não compila.
b) Compila e imprime de0até 9.
c) Compila e imprime de0até 10.
d) Compilaenãoimprimenada.
5) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 int i =0 ;
186

## Página 192

CasadoCódigo Capítulo7. Usandolaços
4 do; while(i++<10);
5 }
6 }
a) Não compila.
b) Compilaeentraemloopinfinito.
c) Co m p ilaesai.
7.4 Compareostiposdelaços
Emborao for, whilee do .. while sejamtodosestruturasquepermi-
tamexecutar loops,existemsimilaridadesediferençasentreessasconstruções
queserãocobradasnaprova.
Comparandowhileedo..while
No caso do while e do while , ambos são muito similares, sendo a
principal diferença o fato dodo .. while ter a condição testada somente
apósexecutarocódigodedentrodo looppelomenosumavez.
int i = 20;
//imprime 20, já que só faz o teste após a execução do código
do {
System.out.println(i);
i++;
} while(i < 10);
int j = 20;
//não imprime nada, já que testa antes de executar o bloco
while(j < 10){
System.out.println(i);
i++;
}
187

## Página 193

7.4. Compareostiposdelaços CasadoCódigo
Comparandoforeenhancedfor
Apesar de ser mais complexo, ofor simples é mais poderoso que o
enhanced for .C o moenhanced for ,nãopodemos:
• Percorrermaisdeumacoleçãoaomesmotempo;
• Removeroselementosdacoleção;
• Inicializarumarray.
Caso desejemos fazer uma iteração deleitura, portodososelementos
dacoleção ,aísimo
enhanced for éamelhoropção.
Comparandowhileefor
Ambas estruturas de laço permitem executar as mesmas operações em
nosso código, e são bem similares. Mas, apesar disso, existem situações em
queocódigoficarámaissimplescasooptemosporumadelas.
Geralmente optamos por usar for quando sabemos a quantidade de
vezes que queremos que o laço seja executado. Pode ser percorrer todos os
elementos de uma coleção, (onde sabemos a quantidade de vezes que o loop
seráexecutadoporsaberotamanhodacoleção)ousimplesmenteexecutaro
laçoumaquantidadefixadevezes.
Usamoso
whileou do .. while quandonãosabemosaquantidade
de vezes em que o laço será executado, mas sabemos uma condição que, en-
quantoforverdadeira,farácomqueolaçosejarepetido.
O exemplo a seguir mostra um código no qual conhecemos a condição
deparada,masnãofazsentidonenhumterumavariávelinicializadaouuma
condiçãodeincremento,entãoescolhemosum
while:
while(conta .getSaldo() > 0) {
conta.saca(1000);
}
Note que, caso queira contar quantas vezes foi sacado, faria sentido usar
um for:
188

## Página 194

CasadoCódigo Capítulo7. Usandolaços
int saques;
for(saques =0 ; conta .getSaldo() > 0; saques++) {
conta.saca(1000);
}
System.out.println("Saquei " + saques + " vezes" );
1) Qual o laço mais simples de ser usado quando desejamos iterar por duas
coleçõesaomesmotempo?
a) for
b) while
c) enhancedfor
d) do... while
2) Qual o melhor laço a ser usado para, dependendo do valor de um ele-
mento,removê-lodenossalista?
a) for
b) enhancedfor
3) Para todos os números entrei e 100 devo imprimir algo, sendo que,
mesmo que i seja maior que100, devo imprimir algo pelo menos uma
vez. Quallaçodevousar?
a) enhancedfor
b) do... while
c) while
4) Qualolaçoaserusadocasoqueiraexecutarumcódigoeternamente?
a) enhancedfor
b) for
c) forouwhile
189

## Página 195

7 .5. U seb r eakeco n tin ue CasadoCódigo
d) forouwhileoudo...while
e) whileoudo...while
5) Quallaçodeveserusadoparainicializarosvaloresdeumarray?
a) enhancedfor
b) for
7.5 Usebreakecontinue
Emqualquerestruturadelaçopodemosaplicaroscontroladores breakecon-
tinue.O break serve para parar o laço totalmente. Já ocontinue inter-
rompeapenasaiteraçãoatual. Vamosveralgunsexemplos:
int i =1 ;
while (i < 10) {
i++;
if (i == 5)
break; // sai do while com i valendo 5
System.out.println(i);
}
System.out.println("Fim");
Aoexecutaro break,aexecuçãodo whileparacompletamente. Temos
aseguintesaída:
2
3
4
Fim
V amosco m pararco mocontinue:
int i =1 ;
while (i < 10) {
i++;
if (i == 5)
190

## Página 196

CasadoCódigo Capítulo7. Usandolaços
continue; // vai para a condição com o i valendo 5
System.out.println(i);
}
Nestecaso,iremospararaexecuçãodaiteraçãoapenasquandoovalorda
variável for igual a 5. Ao encontrar umcontinue, o código volta ao início
daiteração,aopontodoloop. Nossasaídaagor aéas eguinte:
2
3
4
6
7
8
9
10
Fim
Isto é, o break q u e b r aol a ç oa t u a l ,e n q u a n t oocontinue v a ip a r aa
próximaiteraçãodolaço.
Tomecuidado,poisumlaçoquetenhaum whileinfinitodotipo true
e que contenha umbreak é compilável, já que o compilador não sabe se o
códigopoderáparar,possivelmentesim:
while(true ){
if(1==2) break;
System.out.println("em loop infinito compilável" );
}
Oscontroladoresdelaços, break e continue podemseraplicadosno
for.O break secomportadamesmamaneiraqueno while eno do ..
while, parar o laço por completo. Já ocontinue faz com que a iteração
atualsejaabortada,executandoemseguidaapartede atualizaçãodo for,e
emseguidaade condição. Vamosveroexemploaseguir:
for (int i =1 ; i < 10; i++) {
if (i == 8) {
break; // sai do for sem executar mais nada do laço.
}
191

## Página 197

7 .5. U seb r eakeco n tin ue CasadoCódigo
if (i == 5) {
// pula para a atualização sem executar o resto do corpo.
continue;
}
System.out.println(i);
}
Asaídadessecódigoé:
1
2
3
4
6
7
Rótulosemlaços(labeledloops)
Às vezes, encontramos a necessidade de “encaixar” um laço dentro de
outro. Porexemplo,um forden trodeum whileoudeoutro for. Nesses
casos, pode ser preciso manipular melhor a execução dos laços encaixados
comoscontroladoresdelaços, breake continue.
for (int i =1 ; i < 10; i++) { //laço externo
for (int j =1 ; j < 10; j++) { // laço interno
if (i * j == 25) {
break; // qual for será quebrado?
}
}
}
Quando utilizamos obreak ou o continue em laços encaixados, eles
sãoaplicadosnolaçomaispróximo. Porexemplo,nessecódigo,o breakirá
“quebrar” oformaisinterno. Sefossepreciso“quebrar”oformaisexterno,
comofaríamos?
Labeledstatements
Podemosadicionar labels(rótulos)aalgumasestruturasdecódigo,eusá-
los posteriormente para referenciarmos essas estruturas. Para declarar um
192

## Página 198

CasadoCódigo Capítulo7. Usandolaços
label usamos um nome qualquer (mesma regra de nomes de variáveis etc.)
seguido de dois pontos (:). Por exemplo, podemos dar um label para um
forcomooquesegue:
externo: //label
for(int i=0; i<10; i++){
//código
}
Podemos usar esseslabelspara referenciar para qual loop queremos que
o breakou o continuesejaexecutado:
externo: for (int i =1 ; i < 10; i++) {
interno: for (int j =1 ; j < 10; j++) {
if (i * j == 25) {
break externo; // quebrando o for externo
}
if (i * j == 16) {
continue interno; // pulando um iteração do for interno
}
}
}
Labelhttp
Ocódigoaseguirimprimeosvaloresd e1a10. Mascomoelecompila
sendoquetemosumaURIlogoantesdolaço for?
http://www.caelum.com.br
for (int i =1 ; i <= 10; i++) {
System.out.println(i);
}
}
Um rótulo ou label pode estar presente antes de umstatementqualquer,
massópodemosutilizarum statementde breakou continuecasoorótulo
esteja referenciando umfor, whileou switch:
193

## Página 199

7 .5. U seb r eakeco n tin ue CasadoCódigo
void rotuloEmQualquerLugar() {
rotulo: System.out.println("oi");
}
void rotuloEmQualquerLugarComBreakNaoCompila() {
rotulo: System.out.println("oi");
if(1<10) continue rotulo; // erro de compilação
}
Cuidado,mesmodentrodeum forousimilar,o continueeo break
só funcionarão se forem relativos a um label dentro do qual estão, e do tipo
for, do...while, switchou while. Valelembrarque switchsóaceita
break.
void rotuloEmQualquerLugarComBreakNaoCompila() {
rotulo: System .out.println("oi");
for(int i=0;i<10;i++) {
break rotulo; // não compila
}
}
void rotuloEmOutroLaco() {
rotulo:
for(int i=0;i<10;i++) {
System.out.println("oi");
}
for(int i=0;i<10;i++) {
break rotulo; // não compila
}
}
Rótulospodemserrepetidosdesdequenãoexistaconflitodeescopo:
void rotulosRepetidos() {
rotulo: for (int i =0 ; i < 10; i++) {
break rotulo;
}
rotulo: for (int i =0 ; i < 10; i++) {
break rotulo;
}
194

## Página 200

CasadoCódigo Capítulo7. Usandolaços
}
void rotulosRepetidosNestedNaoCompila() {
rotulo: for (int i =0 ; i < 10; i++) {
rotulo: for (int j =0 ; j < 10; j++) {
break rotulo;
}
}
}
N ã oh ác o n fl i t od en o m ee n t r er ó t u l o sev a r i á v e i s ,p o i ss e uu s oéb e m
distinto. O compilador sabe se você está referenciando um rótulo ou uma
variável:
class A{
int rotulo = 15;
void rotulosENomesDeVariaveisNaoConflitam() {
rotulo: for (int i =0 ; i < 10; i++) {
int rotulo = 10;
break rotulo;
}
}
}
Ummesmostatementpodeterdoislabels:
void rotulosNoMesmoStatement() {
primeiro: segundo: for (int i =0 ; i <1 0 ; i++) {
System.out.println(i);
}
}
Tomebastantecuidadocom breakse continuesquesãode switch
masparecemserde fors:
class TestaLacos {
public static void main(String [] args){
for(int i =0 ; i <4 ; i++) {
System.out.println("Estou antes do switch");
mario:
195

## Página 201

7 .5. U seb r eakeco n tin ue CasadoCódigo
guilherme: switch(i){
case 0:
case 1:
System.out.println("Caso " + i);
for(int j =0; j <3 ; j++) {
System.out.println(j);
if(j==1) break mario;
}
case 2:
System.out.println("Estou em i =" + i);
continue;
case 3:
System.out.println("Cheguei no 3");
break;
default:
System.out.println("Estranho...");
break;
}
System.out.println("Estou apos o switch" );
}
}
}
1) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String [] args){
3 fora: for(int a=0; a<30;a++)
4 for(int b=0;b<1;b++)
5 if(a+b==25) continue fora;
6 else if(a+b==20) break fora;
7 if(a==0) break fora;
8 else System.out.println(a);
9 }
10 }
a) Não compila.
b) Co m p ilaeim p rime1a té29
196

## Página 202

CasadoCódigo Capítulo7. Usandolaços
c) Compilaenãoimprimenada
d) Co m p ilaeim p rime1a té19,21a té24,26a té29
e) Co m p ilaeim p rime1a té24,26a té29
f) Co m p ilaeim p rime1a té19
2) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 fora: for(int a=0;a<30;a++)
4 for(int b=0;b<1;b++)
5 if(a+b==25) continue fora;
6 else if(a+b==20) break;
7 else System.out.println(a);
8 }
9 }
a) Não compila.
b) Co m p ilaeim p rime0a té29.
c) Compilaenãoimprimenada.
d) Co m p ilaeim p rime0a té19,21a té24,26a té29.
e) Co m p ilaeim p rime0a té24,26a té29.
f) Co m p ilaeim p rime0a té19.
3) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 int a = args.length;
4 int i =0 ;
5 switch(a){
6 case 0:
7 case 1:
8 for(i=0;i<15;i++, System.out.println(i))
9 if(i==5) continue;
197

## Página 203

7 .5. U seb r eakeco n tin ue CasadoCódigo
10 if(i==15) break;
11 case 2:
12 System.out.println("2");
13 }
14 System.out.println("fim");
15 }
16 }
a) Não compila.
b) Co m p ilaeaor odarco m0argumen tosim p rime0a té14,2,fim.
c) Co m p ilaeaor odarco m0argumen tosim p rime1a té1 5,2,fim.
d) Compilaeaorodarcom0argumentosimprime0até4,6até14,2,fim.
e) Co m p ilaeaor odarco m0argumen tosim p rime1a té4,6a té1 5,fim.
f) Compilaeaorodarcom0argumentosimprime0até4,6até9,2,fim.
g) Co m p ilaeaor odarco m0argumen tosim p rime1a té4,6a té9,fim.
h) Compilaeaorodarcom0argumentosimprime1até4,6até15,2,fim.
i) Co m p ilaeaor odarco m0argumen tosim p rime1a té1 5,2,fim.
j) Co m p ilaeaor odarco m0argumen tosim p rime1a té1 5,fim.
198

## Página 204

Capítulo8
Trabalhandocommétodose
encapsulamento
8.1 Criemétodoscomargumentosevaloresde
retorno
Classes,enumseinterfacespodemtermétodosdefinidosemseuscorpos.
Todo método tem umaassinatura(também chamada deinterface)eu m
corpo(somentenocasodemétodosnãoabstratos).
Aassinaturadométodosempretem:
• umnomeseguindoasregrasdeidentificadores;
• umti poder eto rno;

## Página 205

8.1. Criemétodoscomargumentosevaloresderetorno CasadoCódigo
• um conjunto de parâmetros (pode ser vazio), cada um com seu nome
eseutipo;
• um modificador de visibilidade (nem que seja implícito,package-
private).
E,aindanaassinatura,podemoster:
• final em caso de herança, o método não pode ser sobrescrito nas
classesfilhas;
• abstract obriga as classes filhas a implementarem o método. O
métodoabstrato nãopodetercorpodefinido;
• static atributosacessadosdiretonaclasse,seminstâncias;
• synchronized lockdainstância;
• native nãocainestaprova. Permiteaimplementaçãodométodoem
códigonativo(JNI );
• strictfp não cai nesta prova. Ativa o modo de portabilidade
matemáticaparacontasdepontoflutuante.
• throws <EXCEPTIONS> apósalistadeparâmetros,podemosindicar
quantasexceptionsquisermosparao throws.
A ordem dos elementos na assinatura dos métodos é sempre a seguinte,
sendo que os modificadores podem aparecer em qualquer ordem:
<MODIFICADORES> <TIPO_RETORNO> <NOME> (<PARÂMETROS>)
<THROWS_EXCEPTIONS>
Parâmetros
EmJava,usamosparâmetrosemmétodoseconstrutores. Definimosuma
lista de parâmetros sempre declarando seus tipos e nomes e separando por
vírgula:
200

## Página 206

CasadoCódigo Capítulo8. Trabalhandocommétodoseencapsulamento
class Param {
void teste(int a, int b){
}
}
// chamada
p.teste(1, 2);
A declaração das variáveis é feita na declaração dos métodos. A inicial-
izaçãodosvaloreséfeitaporquemchamaométodo. (Noteque,emJava,não
épossíveltervalores defaultparaparâmetrosetodossãoobrigatórios,não
podemosdeixardepassarnenhum).
O único modificador possível de ser marcado em parâmetros éfinal,
paraindicarqueaqueleparâmetronãopodeterseuvalormodificadodepois
dachamadadométodo(consideradoboaprática):
class Param {
void teste (final int a){
a = 10; // não compila
}
}
Promoçãoemparâmetros
Temos que saber que nossos parâmetros também estão sujeitos à pro-
moçãodeprimitivoseaopolimorfismo. Porexemplo,aclasseaseguirilustra
asduassituações:
class Param {
void primitivo (double d){
}
void referencia ( Object o ){
}
}
201

## Página 207

8.1. Criemétodoscomargumentosevaloresderetorno CasadoCódigo
O primeiro método espera umdouble. Mas se chamarmos passando
um int,um floatouqualqueroutrotipocompatível,esteserápromovido
a doubleeachamadafunciona:
Param p = new Param();
p.primitivo(10);
p.primitivo(10L);
p.primitivo(10F);
p.primitivo((short) 10);
p.primitivo((byte) 10);
p.primitivo( 'Z');
Amesmacoisaocorrecomométodoquerecebe Object: podemospas-
sarqualquerumque éum Object,ouseja,qualquerobjeto:
Param p = new Param();
p.referencia(new Carro());
p.referencia(new Moto());
Retornandovalores
Todo método pode retornar um valor ou ser definido como void,
quandonãodevolvenada:
class A{
int numero() {
return 5;
}
void nada() {
return;
}
}
No caso de métodos de tipo de retornovoid (nada), podemos omitir a
últimainstrução:
class A{
void nada() {
// return; // pois esta linha é opcional
}
}
202

## Página 208

CasadoCódigo Capítulo8. Trabalhandocommétodoseencapsulamento
Ummétododessetipotambémpodeterumretornoantecipado:
class A{
void nada(int i){
if(i >= 0) return;
System.out.println("negativo");
}
}
Nãopodemosternenhumcódigoqueseriaexecutadoapósumretorno:
class A{
void nada(int i){
if(i >= 0) {
return;
// não compila, pois nunca chegará aqui
System.out.println("era positivo ou zero");
}
System.out.println("negativo");
}
}
Todo método que possui um tipo de retorno definido (isto é, diferente
de void), deve retornar algo ou jogar umaException em cada um dos
caminhosdesaídapossíveisdométodo,casocontrárioocódigonãocompila:
String metodo( int a){
if(a >0 ){
return "positivo";
} else if (a <0 ){
return "negativo";
}
//não compila, o que acontece se não for nem if nem else if?
}
Lembre-sequeissoéfeitopelocompilador,entãoelenãosabeosvalores
davariável aesetodososcasosforamcobertos:
String metodo( int a){
if(a >0 ){
203

## Página 209

8.1. Criemétodoscomargumentosevaloresderetorno CasadoCódigo
return "positivo";
} else if(a <= 0) {
return "negativo ou zero";
}
//não compila, o que acontece se não for nem if nem else if?
//o compilador não consegue analisar os dois casos
}
Podemosjogaruma exceptionoucolocarum return:
String metodo(int a){
if(a >0 ){
return "positivo";
} else if (a <0 ){
return "negativo";
}
return "zero";
}
String metodo2( int a){
if(a >0 ){
return "positivo";
} else if (a <0 ){
return "negativo";
}
throw new RuntimeException("não quero zero!" );
}
Métodos que não retornam nada não podem ter seu resultado atribuído
aumavariável:
void metodo() {
System.out.println("oi");
}
void metodo2() {
// não compila, o método acima não retorna nada
int i = metodo();
}
Pelo outro lado, mesmo que um método retorne algo, seu retorno pode
serignorado:
204

## Página 210

CasadoCódigo Capítulo8. Trabalhandocommétodoseencapsulamento
int metodo() {
System.out.println("oi");
return 5;
}
void metodo2() {
int i = metodo(); / /i=5
// chamei novamente e não retornei nada, sem problemas
metodo();
}
1) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 x(args.length);
4 }
5 static int x(final int l){
6 for(int i=0;i<100;i++) {
7 switch(i){
8 case l:
9 System.out.println(l);
10 if(l==i) return;
11 case 0:
12 System.out.println(0);
13 }
14 }
15 System.out.println("Fim");
16 return -1;
17 }
18 }
a) Não compila.
b) Compilaeaorodarcomcincoparâmetros,imprime0,5eFim.
c) Compilaeaorodarcomcincoparâmetros,imprime0,5,-1eFim.
d) Co m p ilaeaor odarco mcincoparâmetr os,im p rime0e5.
e) Compilaeaorodarcomcincoparâmetros,imprime0,5e-1.
f) Compilaeaorodarcomcincoparâmetros,imprime0,5,0eFim.
205

## Página 211

8.1. Criemétodoscomargumentosevaloresderetorno CasadoCódigo
g) Compilaeaorodarcomcincoparâmetros,imprime0,5,0,-1eFim.
h) Co m p ilaeaor odarco mcincoparâmetr os,im p rime0e5.
i) Compilaeaorodarcomcincoparâmetros,imprime0,5,0e-1.
2) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 x(args.length);
4 }
5 static int x(final int l ){
6 for(int i=0;i<100;i++) {
7 switch(i){
8 case l:
9 System.out.println(l);
10 if(l==i) return 3;
11 case 0:
12 System.out.println(0);
13 }
14 }
15 System.out.println("Fim");
16 return -1;
17 }
18 }
a) Não compila.
b) Compilaeaorodarcomcincoparâmetros,imprime0,5eFim.
c) Compilaeaorodarcomcincoparâmetros,imprime0,5,-1eFim.
d) Co m p ilaeaor odarco mcincoparâmetr os,im p rime0e5.
e) Compilaeaorodarcomcincoparâmetros,imprime0,5e-1.
f) Compilaeaorodarcomcincoparâmetros,imprime0,5,0eFim.
g) Compilaeaorodarcomcincoparâmetros,imprime0,5,0,-1eFim.
h) Co m p ilaeaor odarco mcincoparâmetr os,im p rime0e5.
i) Compilaeaorodarcomcincoparâmetros,imprime0,5,0e-1.
206

## Página 212

CasadoCódigo Capítulo8. Trabalhandocommétodoseencapsulamento
3) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 System.out.println(a(args.length));
4 }
5 static int a(int l){
6 if(l<10) return b (l);
7 else return c();
8 }
9 static int b(int l){
10 if(l<10) return b (l);
11 else return c();
12 }
13 static long c() {
14 return 3;
15 }
16 }
a) N ãoco m p ila:err oaoin vocarométodob.
b) N ãoco m p ila:err oaoin vocarométodoc.
c) Nãocompilaporummotivonãolistado.
d) Compilae,aochamarcom15argumentos,imprime3.
e) Compilae,aochamarcom15argumentos,entraemloopinfinito.
4) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 System.out.println(a(args.length)[0]);
4 }
5 static int ,int a(int l ){
6 if(l==0) return {0, l };
7 else return {l, 0};
8 }
9 }
a) Não compila.
207

## Página 213

8.2. Apliqueapalavrachavestaticamétodosecampos CasadoCódigo
b) Aoinvocarcomnenhumparâmetro,imprime0.
c) Aoinvocarcom5parâmetros,imprime0.
8.2 Apliqueapalavrachavestaticamétodose
campos
O modificador estático diz que determinado atributo ou método pertence à
classe,enãoacadaobjeto. Comisso,vocênãoprecisadeumainstânciapara
acessaroatributo,bastaonomedaclasse.
public class Carro {
public static int totalDeCarros;
}
Edepois,paraacessar:
Carro.totalDeCarros = 5;
Um método estático é um método da classe, podendo ser chamado sem
umainstância:
public class Carro{
private static int totalDeCarros;
public static int getTotalDeCarros() [
return totalDeCarros;
}
}
int i = Carro.getTotalDeCarros();
Oquenãopodemosfazeréusarummétodo/atributodeinstânciadeden-
trodeummétodoestático:
public class Carro{
private static int totalDeCarros;
private int peso;
208

## Página 214

CasadoCódigo Capítulo8. Trabalhandocommétodoseencapsulamento
public static int getPeso() {
return peso;
}
}
Essecódigonãocompila,poispesoéumatributodeinstância. Sealguém
chamaressemétodo,quevaloreleretornaria,jáquenãoestamostrabalhando
comnenhumainstânciadecarroemespecífico?
Repare que a variável estática pode acessar um método estático, e esse
método acessar algo ainda não definido e ter um resultado inesperado à
primeiravista:
static int b = getMetodo();
public static int getMetodo() {
return a;
}
static int a = 15;
Ovalorde bserá0,enão15,umavezqueavariável aaindanãofoiinicial-
izadaepossuiseuvalorpadrãoquandodaexecuçãodométodo getMetodo.
Outro caso interessante é que uma variável estática pode acessar outra
estática, desde que a outra tenha um valor atribuído antes da definição da
atual:
static int inicial = 10;
static int segunda = inicial +5 ; // compila
static int outra;
static void inicializa() {
outra = 10;
}
static int naoCompila = outra +1 ;
// não compila, o método inicializa é ignorável
Um detalhe importante é que membros estáticos podem ser acessados
atravésdeinstânciasdaclasse(alémdoacessodiretopelonomedaclasse).
Carro c = new Carro();
int i = c.getTotalDeCarros();
209

## Página 215

8.2. Apliqueapalavrachavestaticamétodosecampos CasadoCódigo
Cuidadocomessasintaxe,quepodelevaraacreditarqueéummétodode
instância. Éumasintaxeestranhamasquecompilaeacessaométodoestático
normalmente.
Além disso, esteja atento pois, caso uma classe possua um método es-
tático, ela não pode possuir outro método não estático com assinatura que a
sobrescreveria(mesmoqueemclassemãe/filha):
class A{
static void a() { // não compila
}
void a() { // não compila
}
}
class B{
static void a() {
}
}
class C extends B {
void a() { // não compila
}
}
Outro ponto importante a tomar nota é que obindingdo método é feito
em compilação, portanto, o método invocado não é detectado em tempo de
execução. Leveemconsideração:
class A{
static void metodo() {
System.out.println("a");
}
}
class B extends A {
static void metodo() {
System.out.println("b");
}
}
210

## Página 216

CasadoCódigo Capítulo8. Trabalhandocommétodoseencapsulamento
Casootiporeferenciadodeumavariávelseja Aemtempodecompilação,
om é t o d os e r áod ac l a s s eA. Se for referenciado comoB, será o método da
classe B:
Aa = new A();
a.metodo(); // a
Bb = new B();
b.metodo(); // b
Aa 2 = b;
a2.metodo(); // a
}
}
A definição de uma variável estática pode invocar métodos e variáveis
estáticas:
class A{
static int idade = calculaIdade();
static int calculaIdade() {
return 18;
}
}
Apalavra-chave staticpodeseraplicadaaclassesaninhadas,maseste
tópiconãoécobradonestaprimeiracertificação.
1) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 x();
4 }
5 static x() {
6 System.out.println("x");
7 y();
8 }
9 static y() {
211

## Página 217

8.2. Apliqueapalavrachavestaticamétodosecampos CasadoCódigo
10 System.out.println("y");
11 }
12 }
a) Não compila.
b) Imprimex,y.
c) Imprimey,x.
d) Imprimex.
e) Imprimey.
2) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 x();
4 }
5 static void x() {
6 System.out.println("x");
7 y();
8 }
9 static void y() {
10 System.out.println("y");
11 }
12 }
a) Não compila.
b) Imprimex,y.
c) Imprimey,x.
d) Imprimex.
e) Imprimey.
3) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{
2 void y() {
212

## Página 218

CasadoCódigo Capítulo8. Trabalhandocommétodoseencapsulamento
3 this.z();
4 }
5 static void z() {
6 System.out.println("z");
7 }
8 }
9 class A{
10 public static void main(String[] args){
11 new A().x();
12 }
13 static void x() {
14 new B().y();
15 }
16 }
a) Nãocompilaaotentarinvocar y.
b) Nãocompilaaotentarinvocar z.
c) Nãocompilaaotentarinvocar x.
d) Compila e imprimez.
4) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{
2 static void x() {
3 System.out.println("x");
4 }
5 static void y() {
6 System.out.println("y");
7 }
8 }
9 class A extends B {
10 public static void main(String[] args){
11 this.x();
12 A.y();
13 }
14 }
a) N ãoco m p ila,err oaoin vocarx.
213

## Página 219

8.3. Criemétodossobrecarregados CasadoCódigo
b) Imprime x, y.
c) N ãoco m p ila,err oaoin vocary.
5) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{
2 static void x() {
3 System.out.println("x");
4 }
5 static void y() {
6 System.out.println("y");
7 }
8 }
9 class A extends B {
10 public static void main(String[] args){
11 x();
12 A.y();
13 }
14 }
a) N ãoco m p ila,err oaoin vocarx.
b) Imprime x, y.
c) N ãoco m p ila,err oaoin vocary.
8.3 Criemétodossobrecarregados
Um método pode ter o mesmo nome que outro, desde que a chamada não
fiqueambígua:os argumentosquesãorecebidostêmdeserobrigatoriamente
diferentes,sejaemquantidadeouemtipos.
class Teste {
public void metodo(int i){
}
protected void metodo(double x){
}
}
214

## Página 220

CasadoCódigo Capítulo8. Trabalhandocommétodoseencapsulamento
Jáocódigoaseguirnãocompila:
class Teste {
public int metodo() {}
protected double metodo() {}
}
Nesse exemplo, temos ambiguidade porque o tipo de retorno não é sufi-
cienteparadistinguirosmétodosduranteachamada.
O Java decide qual das assinaturas de método sobrecarregado (over-
loaded)seráutilizadaem tempodecompilação .
Métodossobrecarregadospodemterounãoumretornodiferenteeuma
visibilidadediferente. Maselesnãopodemterexatamenteosmesmostipose
quantidadedeparâmetros. Nessecaso,seriaumasobrescritademétodo.
No caso de sobrecarga com tipos que possuem polimorfismo, como em
Objectou String,ocompiladorsempreinvocaométodocomotipomais
específico(menosgenérico):
public class Teste {
void metodo(Object o){
System.out.println("object");
}
void metodo(String s){
System.out.println("string");
}
public static void main(String[] args){
new Teste().metodo("string"); // imprime string
}
}
Sequisermosforçarainvocaçãoaométodomaisgenérico,devemosfazer
ocastingforçado:
public class Teste {
void metodo(Object o){
System.out.println("object");
}
215

## Página 221

8.3. Criemétodossobrecarregados CasadoCódigo
void metodo(String s){
System.out.println("string");
}
public static void main(String[] args){
new Teste().metodo((Object)"string"); // imprime object
}
}
Um exemplo clássico é a troca de ordem, que é vista como sobrecarga,
afinalsãodoismétodostotalmentedistintos:
void metodo(String i, double x){
}
void metodo(double x, String i ){
}
Porém, apesar de compiláveis, às vezes o compilador não sabe qual
métododeveráchamar. Nocasoaseguir,osnúmeros2e3podemserconsid-
erados tanto int quanto double, portanto, o compilador fica perdido em
qualdosdoismétodosinvocar,edecidenãocompilar:
public class Teste {
void metodo(int i , double x){
}
void metodo(double x, int i){
}
public static void main(String[] args){
new Teste().metodo(2, 3);
}
}
Isso também ocorre com referências, que é diferente do caso com tipo
mais específico. Aqui não há tipo mais específico, pois onde um é mais es-
pecífico,ooutroémaisgenérico:
public class Xpto {
void metodo(Object o, String s ){
216

## Página 222

CasadoCódigo Capítulo8. Trabalhandocommétodoseencapsulamento
System.out.println("object");
}
void metodo(String s, Object o ){
System.out.println("string");
}
public static void main(String[] args){
new Xpto().metodo("string", "string");
}
}
Diferentedocasoemqueosegundométodoémaisespecífico:
class Xpto2 {
void metodo(Object o, Object o2 ){
System.out.println("object");
}
void metodo(String s, String s2 ){
System.out.println("string");
}
public static void main(String[] args){
new Xpto2().metodo("string", "string"); // imprime string
}
}
1) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 int x = b(15);
4 System.out.println(x);
5 System.out.println(15);
6 System.out.println(15.0);
7 }
8 static int b(int i){ return i;}
9 static double b(int i){ return i;}
10 }
217

## Página 223

8.3. Criemétodossobrecarregados CasadoCódigo
a) Não compila.
b) Compila e imprime15, 15, 15.
c) Compila e imprime15, 15, 15.0.
d) Compila e imprime15, 15.0, 15.0.
2) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 int x = b(15);
4 System.out.println(x);
5 System.out.println(15);
6 System.out.println(15.0);
7 }
8 static int b(int i){ return i;}
9 static double b(double i){ return i;}
10 }
a) Não compila.
b) Compila e imprime15, 15, 15.
c) Compila e imprime15, 15, 15.0.
d) Compila e imprime15, 15.0, 15.0.
3) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 System.out.println("[]");
4 }
5 public static void main(String... args){
6 System.out.println("...");
7 }
8 }
a) Não compila.
b) Compilaeimprime“[]”.
218

## Página 224

CasadoCódigo Capítulo8. Trabalhandocommétodoseencapsulamento
c) Compilaeimprime“...”.
d) Compilaedáexception.
4) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{}
2 class C{}
3 class D extends B{}
4 class A{
5 int a(Dd ){ return 1; }
6 int a(Cc ){ return 2; }
7 int a(Bb ){ return 3; }
8 int a(Aa ){ return 4; }
9 public static void main(String[] args){
10 System.out.println(a(new D()));
11 }
12 }
a) Não compila.
b) Compila e imprime1.
c) Compila e imprime2.
d) Compila e imprime3.
e) Compila e imprime4.
5) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{}
2 class C{}
3 class D extends B{}
4 class A{
5 int a(Dd ){ return 1; }
6 static int a(Cc ){ return 2; }
7 static int a(Bb ){ return 3; }
8 static int a(Aa ){ return 4; }
9 public static void main(String[] args){
10 System.out.println(a(new D()));
11 }
12 }
219

## Página 225

8.3. Criemétodossobrecarregados CasadoCódigo
a) Não compila.
b) Compila e imprime1.
c) Compila e imprime2.
d) Compila e imprime3.
e) Compila e imprime4.
6) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{}
2 class C{}
3 class D extends B{}
4 class A{
5 static int a(Dd ){ return 1; }
6 static int a(Cc ){ return 2; }
7 static int a(Bb ){ return 3; }
8 static int a(Aa ){ return 4; }
9 public static void main(String[] args){
10 System.out.println(a(new D()));
11 }
12 }
a) Não compila.
b) Compila e imprime1.
c) Compila e imprime2.
d) Compila e imprime3.
e) Compila e imprime4.
7) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{}
2 class C{}
3 class D extends B{}
4 class A{
5 static int a(Dd , Bb ){ return 1; }
6 static int a(Cc , Cc ){ return 2; }
220

## Página 226

CasadoCódigo Capítulo8. Trabalhandocommétodoseencapsulamento
7 static int a(Bb , Bb ){ return 3; }
8 static int a(Aa , Aa ){ return 4; }
9 public static void main(String[] args){
10 System.out.println(a(new D(), new D()));
11 }
12 }
a) Não compila.
b) Compila e imprime1.
c) Compila e imprime2.
d) Compila e imprime3.
e) Compila e imprime4.
8) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{}
2 class C{}
3 class D extends B{}
4 class A{
5 static int a(Dd , Bb 2 ){ return 1; }
6 static int a(Cc , Cc 2 ){ return 2; }
7 static int a(Bb , Bb 2 ){ return 3; }
8 static int a(Aa , Aa 2 ){ return 4; }
9 public static void main(String[] args){
10 System.out.println(a(new D(), new D()));
11 }
12 }
a) Não compila.
b) Compila e imprime1.
c) Compila e imprime2.
d) Compila e imprime3.
e) Compila e imprime4.
221

## Página 227

8.4. Diferenciaentreoconstrutorpadrãoeconstrutoresdefinidospelousuário CasadoCódigo
8.4 Diferencia entre o construtor padrão e
construtoresdefinidospelousuário
Quando não escrevemos um construtor na nossa classe, o compilador nos
dá um construtor padrão. Esse construtor, chamado dedefault não recebe
argumentos,temamesmavisibilidadedaclasseetemachamadaa super().
Aclasseaseguir:
class A{
}
... naverdade,acabasendo:
class A{
A() {
super();
}
}
Casovocêadicioneumconstrutorqualquer,oconstrutor defaultdeixa
deexistir:
class A{ }
class B{
B(String s ){ }
}
class Teste {
public static void main(String[] args){
new A(); // construtor padrão,compila
new B(); // não existe mais construtor padrão
new B("CDC"); // construtor existente
}
}
Dentrodeumconstrutorvocêpodeacessareatribuirvaloresaosatribu-
tos,suasvariáveismembro:
class Teste {
int i;
222

## Página 228

CasadoCódigo Capítulo8. Trabalhandocommétodoseencapsulamento
Teste() {
i = 15; // agora i vale 15
System.out.println(i); // 15
}
public static void main(String[] args){
new Teste();
}
}
Os valores inicializados com a declaração das variáveis são inicializados
antesdoconstrutor,justamenteporissoovalorinicialde ié0,ovalorpadrão
deumavariável intmembro:
class Teste {
int i;
Teste() {
System.out.println(i); // vale 0 por padrão
i = 15; // agora i vale 15
System.out.println(i); // 15
}
public static void main(String [] args){
new Teste();
}
}
Vale lembrar que variáveis membro são inicializadas automaticamente
para: numéricas0, boolean false ,referências null.
Cuidadoaoacessarmétodoscujasvariáveisaindanãoforaminicializadas
noconstrutor. Oexemploaseguirmostraumcasoemqueométododeini-
cialização é invocado antes de setar o valor da variável no construtor, o que
causaum
NullPointerException.
class A{
int i = 15;
String nome ;
int tamanho = tamanhoDoNome();
223

## Página 229

8.4. Diferenciaentreoconstrutorpadrãoeconstrutoresdefinidospelousuário CasadoCódigo
A(String nome ){
this.nome = nome;
}
int tamanhoDoNome() {
return nome.length();
}
A() {
}
}
Mesmo que inicializemos a variável fora do construtor, após a chamada
do método pode ocorrer um erro, como no caso a seguir, de um outro
NullPointerException:
class A{
int i = 15;
String nome ;
int tamanho = tamanhoDoSobrenome();
String sobrenome = "Silveira";
A(String nome ){
this.nome = nome;
}
int tamanhoDoSobrenome() {
return sobrenome.length();
}
A() {
}
}
Mudara ordemda declaraçãodas variáveisresolve oproblema, umavez
queométodoéagorainvocadoapósainicializaçãodavariável sobrenome:
224

## Página 230

CasadoCódigo Capítulo8. Trabalhandocommétodoseencapsulamento
class A{
int i = 15;
String nome ;
String sobrenome = "Silveira";
int tamanho = tamanhoDoSobrenome();
A(String nome ){
this.nome = nome;
}
int tamanhoDoSobrenome() {
return sobrenome.length();
}
A() {
}
}
Cuidadoaoinvocarmétodosnoconstrutorevariáveisestaremnulas:
class Teste {
String nome ;
Teste() {
testaTamanho(); // NullPointerException
nome = "aprendendo";
}
private void testaTamanho() {
System.out.println(nome.length());
}
public static void main(String[] args){
new Teste();
}
}
Emaiscuidadoaindacasoissoocorraporcausadesobrescritademétodo,
emquetambémpoderemosteressa Exception:
225

## Página 231

8.4. Diferenciaentreoconstrutorpadrãoeconstrutoresdefinidospelousuário CasadoCódigo
class Base {
String nome ;
Base() {
testa();
nome = "aprendendo";
}
void testa() {
System.out.println("testa");
}
}
class Teste extends Base {
void testa() {
System.out.println(nome.length());
}
public static void main(String[] args){
new Teste();
}
}
Jáseométodo testaforprivado,comoo bindingdachamadaaométodo
éfeitoemcom pilação ,ométodoin vocadopeloconstrutoréodaclassemãe,
semdara Exception:
class Base {
String nome ;
Base() {
testa();
nome = "aprendendo";
}
private void testa() {
System.out.println("testa");
}
}
class Teste extends Base {
void testa() {
226

## Página 232

CasadoCódigo Capítulo8. Trabalhandocommétodoseencapsulamento
System.out.println(nome.length());
}
public static void main(String[] args){
new Teste();
}
}
Vocêpodeentraremloopinfinito,cuidado, StackOverflow:
class Teste {
Teste() {
new Teste();
}
public static void main(String[] args){
new Teste();
}
}
Construtores podem ser de todos os tipos de modificadores de acesso:
private, protected, defaulte public.
É comum criar um construtor privado e um método estático para criar
seuobjeto:
class Teste {
private Teste() {
}
public static Teste cria() {
return new Teste();
}
}
Tenhamuitocuidadocomummétodocomnomedoconstrutor. Secolo-
carum voidnafrente,viraummétodo:
class Teste {
void Teste() {
System.out.println("Construindo");
}
227

## Página 233

8.4. Diferenciaentreoconstrutorpadrãoeconstrutoresdefinidospelousuário CasadoCódigo
public static void main(String[] args){
new Teste();
// não imprime nada, definimos um método e não o construtor
new Teste().Teste();
// agora imprime Construindo
}
}
Existemtambémblocosdeinicializaçãoquenãosãocobradosnaprova.
1) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 final String n ;
3 A() {
4 a();
5 n = "aprendendo";
6 }
7 void a() {
8 System.out.println("testa");
9 }
10 }
11 class B extends A {
12 void a() {
13 System.out.println(n.length());
14 }
15 public static void main(String[] args){
16 new B();
17 }
18 }
a) Não compila.
b) Compila e imprime “testa”.
c) Compila e imprimelength.
d) Compilaedáexception.
e) Compilaenãoimprimenada.
228

## Página 234

CasadoCódigo Capítulo8. Trabalhandocommétodoseencapsulamento
8.5 Crieesobrecarregueconstrutores
Construtorestambémpodemsersobrecarregados:
class Teste {
public Teste() {
}
public Teste( int i){
}
}
Cuidado com os exemplos de sobrecarga comvarargs, como vimos
an tes,enocasodeherança.
Quandoexistemdoisconstrutoresnamesmaclasse,umconstrutorpode
chamaroo u tr oa tra vésdachamadathis. Notequeloopsnãocompilam:
class Teste {
public Teste() {
System.out.println("construtor simples" );
}
public Teste( int i){
this();
}
public Teste( String s ){
this(s, s); // não compila, loop
}
public Teste( String s , String s2 ){
this(s); // não compila, loop
}
}
Temos que tomar cuidado com sobrecarga da mesma maneira que
tomamos cuidado com sobrecarga de métodos: os construtores invocados
seguemasmesmasregrasqueasdemétodos.
Quando um método utiliza varargs, se ele possui uma variação do
métodosemnenhumargumentoeinvocarmossemargumento,elechamará
o método sem argumentos (para manter compatibilidade com versões ante-
rioresdoJava):
229

## Página 235

8.5. Crieesobrecarregueconstrutores CasadoCódigo
void desativa(Cliente... clientes){
System.out.println("varargs");
}
void desativa() {
System.out.println("sem argumento" );
}
void metodo() {
desativa(); // imprime sem argumento
}
A instrução this do construtor deve ser sempre a primeira dentro do
construtor:
class Teste {
Teste() {
String valor = "valor...";
this(valor); // não compila
}
Teste(String s ){
System.out.println(s);
}
public static void main(String[] args){
new Teste();
}
}
Justoporissonãoépossívelterduaschamadasa this:
class Teste {
Teste() {
this(valor );
this(valor ); // não compila
}
Teste(String s ){
System.out.println(s);
}
230

## Página 236

CasadoCódigo Capítulo8. Trabalhandocommétodoseencapsulamento
public static void main(String[] args){
new Teste();
}
}
Ainstrução thispodeenvolverinstruções:
class Teste {
Teste() {
this(valor());
}
private static String valor() {
return "valor...";
}
Teste(String s){
System.out.println(s);
}
public static void main(String [] args){
new Teste();
}
}
Ainstruçãonãopodeserummétododaprópriaclasse,poisoobjetonão
foiconstruídoainda:
class Teste {
Teste() {
this(valor()); // valor não é estático, não compila
}
private String valor() {
return "valor...";
}
Teste(String s) {
System.out.println(s);
}
231

## Página 237

8.5. Crieesobrecarregueconstrutores CasadoCódigo
public static void main(String[] args) {
new Teste();
}
}
1) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{ B() { this(1); } B(int i){ this( ) ;}}
2 class A{
3 public static void main(String[] args){
4 new B();
5 }
6 }
a) Não compila.
b) Compilaejogaexception.
c) Compilaenãoimprimenada.
2) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B() { B(Aa ){ } B() {} }
2 class C() { C(Bb ){ } C() {} }
3 class A{
4 public static void main(String[] args){
5 new A(); new B(); new C();
6 }
7 }
a) N ãoco m p ilaaoin vocaroco nstru to rdeA.
b) N ãoco m p ilaaoin vocaroco nstru to rdeB.
c) N ãoco m p ilaaoin vocaroco nstru to rdeC.
d) Nãocompilanadefiniçãodasclasses Be C.
e) Compilaejogaexception.
f) Compilaenãoimprimenada.
232

## Página 238

CasadoCódigo Capítulo8. Trabalhandocommétodoseencapsulamento
3) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{ B(Aa ){ } B() {} }
2 class C{ C(Bb ){ } C() {} }
3 class A{
4 public static void main(String[] args){
5 new A(); new B(); new C();
6 }
7 }
a) N ãoco m p ilaaoin vocaroco nstru to rdeA.
b) N ãoco m p ilaaoin vocaroco nstru to rdeB.
c) N ãoco m p ilaaoin vocaroco nstru to rdeC.
d) Nãocompilanadefiniçãodasclasses Be C.
e) Compilaejogaexception.
f) Compilaenãoimprimenada.
4) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{ B(Aa ){ } B() {} }
2 class C{ C(Bb ){ } C() {} }
3 class A{
4 public static void main(String[] args){
5 new C(new B(new A()));
6 }
7 }
a) N ãoco m p ilaaoin vocaroco nstru to rdeA.
b) N ãoco m p ilaaoin vocaroco nstru to rdeB.
c) N ãoco m p ilaaoin vocaroco nstru to rdeC.
d) Nãocompilanadefiniçãodasclasses Be C.
e) Compilaejogaexception.
f) Compilaenãoimprimenada.
233

## Página 239

8.6. Apliquemodificadoresdeacesso CasadoCódigo
5) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{ B(Aa ){ new C(); } B() { new C(this);} }
2 class C{ C(Bb ){ new B(new A());} C() {new B();} }
3 class A{
4 public static void main(String[] args){
5 new C(new B(new A()));
6 }
7 }
a) N ãoco m p ilaaoin vocaroco nstru to rdeA.
b) N ãoco m p ilaaoin vocaroco nstru to rdeB.
c) N ãoco m p ilaaoin vocaroco nstru to rdeC.
d) Nãocompilanadefiniçãodasclasses Be C.
e) Compilaejogaexception.
f) Compilaenãoimprimenada.
8.6 Apliquemodificadoresdeacesso
Os modificadores de acesso, ou modificadores de visibilidade, servem para
definir quais partes de cada classe (ou se uma classe inteira) estão visíveis
para serem utilizadas por outras classes do sistema. Só é permitido usar um
únicomodificadordeacessoporvez:
private public int x; // não compila
OJavapossuiosseguintesmodificadoresdeacesso:
• public
• protected
• Nenhummodificador,chamadode default
• private
234

## Página 240

CasadoCódigo Capítulo8. Trabalhandocommétodoseencapsulamento
Classeseinterfacessóaceitamosmodificadores publicou default.
Membros (construtores, métodos e variáveis) podem receber qualquer
umdosquatromodificadores.
Variáveis locais (declaradas dentro do corpo de um método ou constru-
tor) e parâmetros não podem receber nenhum modificador de acesso, mas
podemreceberoutrosmodificadores.
TopLevelClasseseInnerClasses
Classes internas (nested classesou inner classes) são classes que são
declaradasdentrodeoutrasclasses. Essetipodeclassepodereceberqual-
quer modificador de acesso, já que são consideradas membros da classe
ondeforamdeclaradas( toplevelclass).
Nesta certificação não são cobradas classes internas, apenastop level
classes.
Para entender como os modificadores funcionam, vamos imaginar as
seguintesclasses:
1 package forma;
2
3 class Forma{
4 double lado;
5 double getArea(){
6 return 0;
7 }
8 }
1 package forma;
2
3 class Quadrado extends Forma{}
1 package forma.outro;
2 import forma.*;
3
4 class Triangulo extends Forma{}
235

## Página 241

8.6. Apliquemodificadoresdeacesso CasadoCódigo
Public
Omodificador publicéomenosrestritivodetodos. Classes,interfaces
e membros marcados com esse modificador podem ser acessados de qual-
quer componente, em qualquer pacote. Vamos alterar nossa classeForma,
marcando-aetodosseusmembroscomomodificador public:
1 package forma;
2
3 public class Forma{
4 public double lado;
5 public double getArea(){
6 return 0;
7 }
8 }
Agoravamosfazerumteste:
1 package forma.outro;
2 import forma.*;
3
4 public class TesteOutroPacote{
5
6 public static void main(String... args){
7 Forma f = new Forma(); //acesso a classe forma
8 f.lado = 5.5; //acesso ao atributo lado
9 f.getArea(); //acesso ao método getArea()
10 }
11 }
Repare que, mesmo nossa classeTesteOutroPacote e s t a n d oe mu m
pacotediferentedaclasse Forma,épossívelacessaraclasseetodososmem-
brosdeclaradoscomo public.
Protected
Membros definidos com o modificadorprotected podem ser acessa-
dos por classes e interfaces no mesmo pacote, e por qualquer classe que es-
tendaaquelaondeomembrofoidefinido,independentedopacote.
Vamosmodificarnossaclasse
Formaparaentendermosmelhor:
236

## Página 242

CasadoCódigo Capítulo8. Trabalhandocommétodoseencapsulamento
package forma;
public class Forma{
protected double lado; // agora protected
public double getArea(){}
}
Comomodificador protected,nossaclassedetestesemoutropacote
nãocompilamais:
package forma.outro;
import forma.*;
public class TesteOutroPacote{
public static void main(String... args){
Forma f = new Forma();
f.lado = 5.5; // erro de compilação
f.getArea();
}
}
Se criarmos uma nova classe de teste no pacoteforma, conseguimos
acessarnovamenteoatributo:
1 package forma;
2
3 public class Teste{
4
5 public static void main(String... args){
6 Forma f = new Forma();
7 f.lado = 5.5; // compila normal, mesmo pacote
8 }
9 }
Embora esteja em um pacote diferente, a classeTriangulo consegue
acessaroatributo lado,jáqueelaestendedaclasse Forma:
package forma.outro;
import forma.*;
237

## Página 243

8.6. Apliquemodificadoresdeacesso CasadoCódigo
class Triangulo extends Forma{
public void imprimeLado(){
//Como é uma classe filha, acessa
//normalmente os membros protected da classe mãe.
System.out.println("O Lado é " + lado);
}
}
A g o r ar e p a r eq u e ,s ee f e t u a r m o soc a s t i n gd oo b j e t oa t u a lp a r au m a
Forma,nãopodemosacessarseulado:
package outro;
import forma.*;
class Triangulo extends Forma{
public void imprimeLado(){
// compila
System.out.println("O Lado é " + lado);
// não compila
System.out.println("O Lado é " +( ( Forma) this).lado);
}
}
Isso ocorre porque estamos dizendo que queremos acessar a variável
membro lado de um objeto através de uma referência para este objeto, e
nãodiretamente. Diretamenteseriaousopurodo thisounada. Nessecaso,
apósusaro this,usamosumcasting,oquedeixaocompiladorperdido.
Default
Se não definirmos explicitamente qual o modificador de acesso, pode-
mosdizerqueaquelemembroestáusandoomodificador default,também
chamadode package private . Nestecaso,osmembrosdaclassesóserão
visíveisdentrodomesmopacote:
238

## Página 244

CasadoCódigo Capítulo8. Trabalhandocommétodoseencapsulamento
package forma;
public class Forma{
protected double lado;
public double getArea(){
return 0;
}
double getPerimetro(){ //default access
return 0;
}
}
Ométodo getPerimetro()sóserávisívelparatodasasclassesdopa-
cote forma. Nem mesmo a classeTriangulo que, apesar de herdar de
Forma,estáemoutropacote consegueverométodo.
package outro;
import forma.*;
class Triangulo extends Forma{
public void imprimePerimetro(){
//Erro de compilação na linha abaixo
System.out.println("O Perímetro é " + getPerimetro());
}
}
239

## Página 245

8.6. Apliquemodificadoresdeacesso CasadoCódigo
Palavra-chave DEFAULT
Lembre-se! A palavra-chavedefault é usada para definir a opção
padrão em um blocoswitch, ouparadefinirumvalorinicialemuma
Annotation. Usá-laemumadeclaraçãodeclasseoumembroéinválidoe
ca usaumerr odeco m p ilação:
1 default class Bola{ //ERRO
2 default String cor; // ERRO
3 }
Ap a rt i rd oJ a v a8 ,ap a l a v r adefault também pode ser usada para
definirumaimplementaçãoinicialdeummétodo.
Mas e se declararmos uma classe com o modificadordefault?I s s o
vai fazer com que aquela classe só seja visível dentro do pacote onde foi
declarada. Não importa quais modificadores os membros dessa classe ten-
ham, se a própria classe não é visível fora de seu pacote, nenhum de seus
membrosévisíveltambém.
Vejaaclasse
Quadrado,queestádefinidacomomodificador default:
1 package forma;
2
3 class Quadrado extends Forma{}
Veja o seguinte código, usando a classeTesteOutroPacote. Perceba
que não é possível usar a classeQuadrado, mesmo importando todas as
classesdopaco te forma:
package outro;
import forma.*;
public class TesteOutroPacote{
public static void main(String... args){
Quadrado q = new Quadrado (); // erro, esta classe não é
//visível
240

## Página 246

CasadoCódigo Capítulo8. Trabalhandocommétodoseencapsulamento
}
}
241

## Página 247

8.6. Apliquemodificadoresdeacesso CasadoCódigo
Linhacomerrodecompilação
Eventualmente,naprova,éperguntadoemquaislinhasocorreramos
errosdecompilação. Ébemimportanteprestaratençãonessedetalhe.
Porexemplo,nestecaso,oerrosempreaconteceráquandotentarmos
acessaraclasse Quadrado,quenãoévisívelforadeseupacote:
package outro;
//import de todas as classes PÚBLICAS do pacote, nenhum erro
import forma.*;
public class TesteOutroPacote{
public static void main(String... args){
// erro na linha 8, Quadrado não é visível, pois não
// é pública
Quadrado q = new Quadrado ();
}
}
O mesmo código pode apresentar erro em uma linha diferente, ape-
nasmudandoo import. Reparequeocódigoaseguirdáerronasduas
linhas,tantodo importquantonatentativadeuso:
package outro;
// erro na linha 3, não podemos importar classes não públicas
import forma.Quadrado;
public class TesteOutroPacote{
public static void main(String ... args){
//Erro, pois Quadrado não é acessível.
Quadrado q = new Quadrado ();
}
}
É muito importante testar vários trechos de código, para ver exata-
menteemquaislinhasdecódigooerrodecompilaçãoaparecerá.242

## Página 248

CasadoCódigo Capítulo8. Trabalhandocommétodoseencapsulamento
Private
private éomaisrestritivo detodososmodificadoresdeacesso. Mem-
brosdefinidoscomo privatesópodemseracessadosdedentrodaclassee
denenhumoutrolugar,independentedepacoteouherança:
package forma;
public class Forma{
protected double lado;
public double getArea(){}
//cor só pode ser acessada dentro da classe Forma,
//nem as classe Quadrado e Triangulo conseguem acessar
private String cor;
}
Privateeclassesaninhadasouanônimas
Classesaninhadasouanônimaspodemacessarmembrosprivadosda
classeondeestãocontidas. Nacertificaçãotaisclassesnãosãocobradas.
Métodos privados e padrão não podem ser sobrescritos. Se uma classe
o“sobrescreve”,elesimplesmenteéummétodonovo,portantonãopodemos
dizerqueésobrescrita. Veremosissomaisafundonaseçãosobresobrescrita.
9.1
Resumodasregrasdevisibilidade
Todososmembrosda classecomomodificadorde private sópodem
seracessadosdedentrodelamesma.
Todos os membros da classe sem nenhum modificador de visibilidade,
ouseja,comvisibilidade package-private,podemseracessadosdedentroda
própria classe ou de dentro de qualquer outra classe, interface ou enum do
mesmopacote.
243

## Página 249

8.6. Apliquemodificadoresdeacesso CasadoCódigo
Todososmembrosdaclassecomomodificador protectedpodemser
acessados:
• dedentrodaclasse,oudedentrodequalqueroutraclasse,interfaceou
enumdomesmopacote;
• dedentrodealgumaclassequederivadiretaouindiretamentedaclasse,
independentedopacote. Omembro protectedsópodeserchamado
atravésdareferência this,ouporumareferênciaquesejadessaclasse
filha.
Todososmembrosdaclassecomomodificador publicpodemseraces-
sadosdequalquerlugardaaplicação.
Enãopodemosterclasses/interfaces/enumstop-levelcomo privateou
protected.
U m ac l a s s eéd i t atop-levelse ela não foi definida dentro de outra classe,
interface ou enum. Analogamente, são definidas as interfaces top-level e os
enumstop-level.
1) Escolha a opção adequada ao tentar compilar e rodar oTeste.A r q u i v o
nodiretórioatual:
1 import modelo.Cliente;
2 class Teste {
3 public static void main(String[] args){
4 new Cliente("guilherme").imprime();
5 }
6 }
Arquivonodiretório modelo:
1 package modelo ;
2
3 public class Cliente {
4 private String nome;
5 Cliente(String nome ){
6 this.nome = nome;
7 }
244

## Página 250

CasadoCódigo Capítulo8. Trabalhandocommétodoseencapsulamento
8 public void imprime() {
9 System.out.println(nome);
10 }
11 }
a) N ãoco m p ila:err onaclasseTeste.
b) N ãoco m p ila:err onaclasseCliente.
c) Errodeexecução: método main.
d) Rodaeimprime“Guilherme”.
2) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 private static int a(int b){
3 return b(b)-1;
4 }
5 private static int b(int b){
6 return b-1;
7 }
8 public static void main(String[] args){
9 System.out.println(new A().a(5));
10 }
11 }
a) Nãocompilanasinvocaçõesdemétodos.
b) Nãocompilanadeclaraçãodevariáveisemétodos.
c) Compila e imprime 3.
d) Co m p ilaedáerr o .
3) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 private public int a(int b){
3 return b(b)-1;
4 }
5 private static int b(int b){
245

## Página 251

8.6. Apliquemodificadoresdeacesso CasadoCódigo
6 return b-1;
7 }
8 public static void main(String[] args){
9 System.out.println(new A().a(5));
10 }
11 }
a) Nãocompilanasinvocaçõesdemétodos.
b) Nãocompilanadeclaraçãodevariáveisemétodos.
c) Compila e imprime 3.
d) Co m p ilaedáerr o .
4) Escolhaaopçãoadequadaaotentarcompilarerodarosarquivosaseguir,
cadaumemseudiretórioadequado:
1 package a;
2 import b.*;
3 public class A extends B { protected int a(String s )
4 {return 2;} }
1 package b;
2 import a.*;
3 public class B{ public int a(Object s){ return 1;} }
1 import a.*;
2 import b.*;
3 class A{
4 public static void main(String[] args){
5 System.out.println(new A().a("a"));
6 }
7 }
a) Não compila.
b) Imprime1.
c) Imprime2.
d) Erroemexecução.
246

## Página 252

CasadoCódigo Capítulo8. Trabalhandocommétodoseencapsulamento
5) Escolhaaopçãoadequadaaotentarcompilarerodarosarquivosaseguir,
cadaumemseudiretórioadequado:
1 package a;
2 import b.*;
3 public class A extends B { protected int a(String s )
4 {return 2;} }
1 package b;
2 import a.*;
3 public class B{ public int a(Object s){ return 1;} }
1 import a.*;
2 import b.*;
3 class C{
4 public static void main(String[] args){
5 System.out.println(new A().a("a"));
6 }
7 }
a) Não compila.
b) Imprime1.
c) Imprime2.
d) Erroemexecução.
6) Escolhaaopçãoadequadaaotentarcompilarerodarosarquivosaseguir,
cadaumemseudiretórioadequado:
1 package a;
2 import b.*;
3 public class A extends B { protected int a(String s )
4 {return 2;} }
1 package b;
2 import a.*;
3 public class B{ default int a( Object s ){ return 1;} }
247

## Página 253

8.6. Apliquemodificadoresdeacesso CasadoCódigo
1 import a.*;
2 import b.*;
3 class C{
4 public static void main(String[] args){
5 System.out.println(new A().a("a"));
6 }
7 }
a) Não compila.
b) Imprime1.
c) Imprime2.
d) Erroemexecução.
7) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{
2 static int bs=0;
3 final int b =+ + bs;
4 private B() {}
5 static B b() { return new B(); }
6 }
7 class A{
8 public static void main(String [] args){
9 System.out.println(B.b().b);
10 }
11 }
a) Não compila.
b) Compila e imprime 1.
c) Compila e imprime 0.
d) Co m p ilaedáerr odeexecução .
248

## Página 254

CasadoCódigo Capítulo8. Trabalhandocommétodoseencapsulamento
8.7 Aplique princípios de encapsulamento a
umaclasse
Aassinaturadeummétodoéoquer ealmen tedeveim portarparaousuário
de alguma classe. Segundo os bons princípios do encapsulamento, a imple-
mentaçãodosmétodosdeveestar encapsuladaenãodevefazerdiferençapara
ousuário.
Oq ueéim po rta n t eemumac las seéoqueelafazenãocomoelafaz . O
queelafaz édefinidopeloscomportamentosexpostos,ouseja,pelosmétodos
esuasassinaturas.
Oconjuntodeassinaturasdemétodosvisíveisdeumaclasseéchamadode
interfacedeuso. Éatravésdessasoperaçõesqueosusuáriosvãosecomunicar
comosobjetosdessaclasse.
Mantendo os detalhes de implementação de nossas classes “escondidos”,
evitamos que mudanças na forma de implementar uma lógica quebre vários
pontosdenossaaplicação.
Umadasformasmaissimplesdecomeçaraencapsularocomportamento
de uma classe é escondendo seus atributos. Podemos fazer isso facilmente
usandoapalavra-chave
private:
public class Pessoa{
private String nome;
}
Caso precisemos acessar um desses atributos a partir de outra classes,
teremos que criar um método para liberar o acesso de leitura desse atrib-
uto. Seguindo a especificação dosjavabeans, esse método seria umgetter.
Damesmaforma,seprecisarmosliberaraescritadealgumatributo,criamos
ummétodo setter:
public class Pessoa{
private String nome;
public String getNome() {
return nome;
}
249

## Página 255

8.7. Apliqueprincípiosdeencapsulamentoaumaclasse CasadoCódigo
public void setNome(String nome ){
this.nome = nome;
}
}
Comessaabordagem,poderíamosfazerumavalidaçãoemnossosméto-
dos,paraevitarquenossosatributosfiquemcomestadoinválido. Porexem-
plo,podemosverificarseonomepossuipelomenos3caracteres:
public class Pessoa{
private String nome ;
private String sobrenome;
public String getNome() {
return nome;
}
public void setNome(String nome ){
if(nome!= null && nome.trim().length() >= 3)
this.nome = nome;
else{
throw new IllegalArgumentException(
"Nome deve possuir " + "pelo menos 3 caracteres" );
}
}
}
Encapsulamentoémuitomaisdoqueatributosprivadose gettersesetters.
Nãoénossofocoaquidiscutirboaspráticasdeprogramação,esimoconhec-
imento necessário para passar na prova. Em questões sobre encapsulamento
sempre, fique atento à alternativa que esconde mais detalhes de implemen-
tação da classe analisada. A prova pode utilizar tanto o termoencapsulation
como information hidingpara falar sobre encapsulamento (ou esconder in-
formações).
1) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{
2 private int b;
3 public int getB() { return b;}
250

## Página 256

CasadoCódigo Capítulo8. Trabalhandocommétodoseencapsulamento
4 public void setB(int b ){ this.b= b;}
5 }
6 class A{
7 public static void main(String[] args){
8 new B().setB(5);
9 System.out.println(new B().getB());
10 }
11 }
a) Não compila.
b) Compila e imprime 0.
c) Compila e imprime 5.
2) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{
2 private int b;
3 public int getB() { return b;}
4 public void setB(int b ){ this.b= b;}
5 }
6 class A{
7 public static void main(String[] args){
8 Bb = new B();
9 b.setB(5);
10 System.out.println(b.getB());
11 }
12 }
a) Não compila.
b) Compila e imprime 0.
c) Compila e imprime 5.
3) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{
2 private int b;
3 public int getB() { return b;}
251

## Página 257

8.7. Apliqueprincípiosdeencapsulamentoaumaclasse CasadoCódigo
4 public void setB( int b){ b = b;}
5 }
6 class A{
7 public static void main(String[] args){
8 Bb = new B();
9 b.setB(5);
10 System.out.println(b.getB());
11 }
12 }
a) Não compila.
b) Compila e imprime 0.
c) Compila e imprime 5.
4) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{
2 int b;
3 public void setB( int b){ b = b;}
4 }
5 class A{
6 public static void main(String[] args){
7 Bb = new B();
8 b.setB(5);
9 System.out.println(b.b);
10 }
11 }
a) N ãoco m p ila,po isnãoépossíveltersettersem getter.
b) Compila e imprime 0.
c) Compila e imprime 5.
5) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{
2 private final int b;
3 B(int b){ this.b = b;}
252

## Página 258

CasadoCódigo Capítulo8. Trabalhandocommétodoseencapsulamento
4 public int getB() { return b;}
5 public void setB(int b ){ b= b;}
6 }
7 class A{
8 public static void main(String[] args){
9 Bb = new B(10);
10 b.setB(5);
11 System.out.println(b.getB());
12 }
13 }
a) Não compila.
b) Compila e imprime 0.
c) Compila e imprime 5.
d) Compilaeimprime10.
8.8 Determine o efeito que ocorre com refer-
ênciasaobjetoseatiposprimitivosquando
são passados a outros métodos e seus val-
oresmudam
As informações que queremos enviar para um método devem ser passadas
como parâmetro. O domínio de como funciona a passagem de parâmetro é
fundamentalparaaprovadecertificação.
O requisito para entender passagem de parâmetro no Java é saber como
funcio naap ilhadeexecuçãoeoheap deobjetos.
Apilhadeexecuçãoéo“lugar”ondesãoempilhadososmétodosinvoca-
dosnamesmaordememqueforamchamados.
Oheapé o “lugar” onde são guardados os objetos criados durante a exe-
cução.
Considereoexemploaseguir:
class Teste {
public static void main(String[] args){
253

## Página 259

8.8. Determineoefeitoqueocorrecomreferênciasaobjeto seati posp rimi tivosquandosãopassadosa
outrosmétodoseseusvaloresmudam CasadoCódigo
Figura8.1: Pilhadeexecução
Figura8.2: Heap
A passagem de parâmetros é feita por cópia de valores. Dessa forma,
mudanças nos valores das variáveis definidas na lista de parâmetros de um
métodonãoafetamvariáveisdeoutrosmétodos.
Passagemdeparâmetrosprimitivos
Vejaoseguintecódigo:
254

## Página 260

CasadoCódigo Capítulo8. Trabalhandocommétodoseencapsulamento
class Teste {
public static void main(String[] args){
int i =2 ;
teste(i);
System.out.println(i);
}
static void teste(int i){
i =3 ;
}
}
Aoexecutaraclasse Teste,seráimpressoovalor 2. Énecessárioperce-
berqueasduasvariáveiscomonome iestãoemmétodosdiferentes. Háum
i no main() eo u tr oi no teste(). Alteraçõesemumadasvariáveisnão
afetam o valor da outra.
Passagemdeparâmetrosdereferência
A go ravejaestaclasse:
class Teste {
public static void main(String [] args){
Prova prova = new Prova();
prova.tempo = 100;
teste(prova );
System.out.println(prova.tempo);
}
static void teste(Prova prova ){
prova.tempo = 210;
}
}
class Prova {
double tempo;
}
Esseexemploébeminteressanteecausamuitaconfusão. Oqueseráim-
pressonasaída,aoexecutaraclasse Teste,éovalor 210. Osdoismétodos
255

## Página 261

8.8. Determineoefeitoqueocorrecomreferênciasaobjeto seati posp rimi tivosquandosãopassadosa
outrosmétodoseseusvaloresmudam CasadoCódigo
t ê mv a r i á v e i sc o mom e s m on o m e(prova). Essas variáveis são realmente
independentes,ouseja,mudarovalordeumanãoafetaovalordaoutra.
Poroutrolado,comosãovariáveisnãoprimitivas,elasguardamreferên-
ciase,nestecaso,sãoreferênciasqueapontamparaomesmoobjeto. Modifi-
caçõesnesseobjetopodemserexecutadasatravésdeambasasreferências.
Figura8.3: Passagemdeparâmetrosnãoprimitivos
M a ss ee ut r o c a rar e f e r ê n c i a ,s óe s t o ut r o c a n d on e s t av a r i á v e ll o c a l ,e
não no objeto referenciado, como no exemplo doteste2, em que estamos
trocandosomenteareferêncialocalenãoooutro:
256

## Página 262

CasadoCódigo Capítulo8. Trabalhandocommétodoseencapsulamento
}
static void teste2(Prova prova ){
prova = new Prova();
prova.tempo = 520;
}
static void teste(Prova prova ){
prova.tempo = 210;
}
static int teste( int i){
i =5 ;
System.out.println(i);
return i;
}
}
1) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 int i = 150;
4 i =+ + s(i);
5 System.out.println(i);
6 }
7 static int s(int i){
8 return ++i;
9 }
10 }
a) Não compila.
b) Compila e imprime 150.
c) Compila e imprime 151.
d) Compila e imprime 152.
2) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
257

## Página 263

8.8. Determineoefeitoqueocorrecomreferênciasaobjeto seati posp rimi tivosquandosãopassadosa
outrosmétodoseseusvaloresmudam CasadoCódigo
1 class A{
2 public static void main(String[] args){
3 int[] i = {150, 151};
4 i = s(i);
5 System.out.println(i[1]);
6 }
7 static int [] s(int[] i){
8 int[] j ={ i[0], i[1]};
9 i[1]++;
10 return j;
11 }
12 }
a) Não compila.
b) Compila e imprime 150.
c) Compila e imprime 151.
d) Compila e imprime 152.
e) Compilaeimprime153.
258

## Página 264

Capítulo9
Trabalhandocomherança
9.1 Implementandoherança
Em Java, podemos usar herança simples entre classes com oextends.A
nomenclaturausadaéde classemãe (parentclass)e classefilha (child class),
ousuperclasseesubclasse.
Herança entre classes permite que um código seja reaproveitado, de
maneira que a classe filha reutilize o código da parte mãe, preocupando-
se principalmente em sua especialização. A filha especializa a classe mais
genérica. Herança em Java pode ser entre classes, reaproveitando membros,
ouherançadeumainterface,comaqualreaproveitamosinterfacesdeméto-
dos.
class Mae {
}

## Página 265

9.1. Implementandoherança CasadoCódigo
class Filha extends Mae {
}
class Neta extends Filha {
}
Valelembrarquetodaclassequenãodefinedequemestáherdandoherda
de Object:
class Explicito extends Object {
}
class Implicito {
// extends Object por padrão
}
class FilhoDeImplicito extends Implicito{
// também herda de Object, indiretamente
}
Masnãopodemosherdardeduasclasses:
class Simples1{}
class Simples2 {}
class Complexa extends Simples1, Simples2 {
// não compila
}
Parapodermosherdardeumaclasse,aclassemãeprecisaservisívelpela
classefilhaepelomenosumdeseusconstrutorestambém:
class Pai {
Pai(int x){
}
}
class Filho1 extends Pai{
// não compila pois o construtor padrão chama super()
// e o Pai não tem construtor vazio
}
class Filho2 extends Pai{
Filho2() {
super(15); //compila
}
}
260

## Página 266

CasadoCódigo Capítulo9. Trabalhandocomherança
Alémdisso,aclassemãenãopodeser final:
final class Pai {
}
class Filho extends Pai {
// não compila, Pai é final
}
class Mae {
}
final class Filha extends Mae {
// uma classe final pode estender de alguém, compila
}
Herançademétodoseatributos
Todososmétodoseatributosdeumaclassemãesãoherdados(indepen-
dentedasvisibilidades).
class X{
int x;
public void y() {
}
}
class Y{
// tenho um x, e o método y
}
Dependendo da visibilidade e das classes envolvidas, a classe filha não
consegue enxergar o membro herdado. No exemplo a seguir, herdamos o
atributomasnãooenxergamosdiretamente.
class X{
private int x;
public void setX( int x){
this.x = x;
}
public int getX() {
return x;
261

## Página 267

9.1. Implementandoherança CasadoCódigo
}
}
class Y extends X {
public void metodo () {
this. x=5 ; // não compila: "x has private access in X"
this.setX(10); // compila e altero o x herdado mas
// não visível
}
}
Métodosestáticoseherança
Nãoexisteherançademétodosestáticos . Masquandoherdamosdeuma
classe com métodos estáticos, podemos chamar o método da classe mãe us-
andoono medafilha(embo ranãosejaumaboap rá tica):
class W{
static void metodo() {
}
}
class Z extends W {
}
class Teste {
public static void main(String[] args){
Z.metodo(); // melhor seria escrever W.metodo()
}
}
class W{
public static void metodo() {
System.out.println("w");
}
}
class Z extends W {
public static void metodo() {
262

## Página 268

CasadoCódigo Capítulo9. Trabalhandocomherança
// não existe super em contexto estático, não compila
super.metodo();
}
}
Pornãoexistirherança,omodificador abstractnãoéaceitoemméto-
dosestáticos.
Podemosatéescrevernaclassefilhaummétodoestáticodemesmonome,
masisso nãoésobrescrita (algunschamamderedefinição):
class W{
public static void metodo() {
System.out.println("w");
}
}
class Z extends W {
public static void metodo() {
System.out.println("z");
}
}
public class Teste {
public static void main(String[] args){
System.out.println(W.metodo()); // w
System.out.println(Z.metodo()); // z
}
}
Naverdadevocêatésegueasregrasdesobrescritademétodo(visibilidade
e retorno), mas no polimorfismo ele não funciona como métodos normais.
Ele simplesmente funciona com o tipo da variável em tempo de compilação
enãootipodoobjetoemtempodeexecução:
public class Teste {
public static void main(String[] args){
Ww = new W();
w.metodo(); // w
Zz = new Z();
263

## Página 269

9.1. Implementandoherança CasadoCódigo
z.metodo(); // z
W zPolimorfadoComoW = z;
zPolimorfadoComoW.metodo();
// este último imprime w,
// pois o binding é feito em compilação:
// zPolimorfadoComoW.metodo é uma referencia
// em compilação para W
}
}
Construtoreseherança
N ã oe x i s t eh e r a n ç ad ec o n s t r u t o r e s . Oq u ee x i s t eéac l a s s efi l h a
chamaroco nstru to rdamãe.
Sobrescritadeatributos
Nãoexistesobrescritadeatributos. Podemos,sim,terumatributona
classefilhacommesmonomedamãe,masnãochamamosdesobrescrita.
Nessescasos,oobjetovaiter2atributosdiferentes,umdamãe(acessível
com
super)eumnafilha(acessívelcom this).
Object
Em Java, toda classe é obrigada a usar a herança. Quando não escreve-
mos extends explicitamente, estamos herdando dejava.lang.Object
automaticamente.
IssoquerdizerquetodoobjetoemJava éum Objecte,portanto,herda
todososmétodosdaclasse Object(porissoessessãomuitoimportantes).
Há vários métodos emObject, que veremos ao longo do curso, mas o
maissimples talvezsejao toString, que podemos sobrescrever em nossas
classesparadevolveralguma Stringquerepresenteoobjeto:
264

## Página 270

CasadoCódigo Capítulo9. Trabalhandocomherança
class Carro {
String cor ;
public String toString() {
return "Um carro de cor " + this.cor;
}
}
Temos que lembrar que otoString é chamado automaticamente para
nósquandousamosoob jetonoco n textode String:
Carro c = new Carro();
c.cor = "Verde";
System.out.println(c); // chama toString
String s = "Mensagem: " + c; // chama toString
System.out.println(s);
1) class A{
public void metodo(long l){
}
}
class B extends A{
protected void metodo(int i){
}
}
Compila?
2) import java.io*;
class Veiculo {
protected void liga () throws IOException {}
}
class Carro extends Veiculo {
public void liga() throws FileNotFoundException {}
}
3) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
265

## Página 271

9.1. Implementandoherança CasadoCódigo
1 class B extends C { int m(int a){ return 1 ;}}
2 class C extends A { int m(double b){ return 3; } }
3 class A extends B {
4 int m(String c ){ return 3; }
5 public static void main(String [] args){
6 System.out.println(new C().m(3));
7 }
8 }
a) Ocódigonãocompila.
b) Compila e imprime 1.
c) Compila e imprime 2.
d) Compila e imprime 3.
e) Compilaeimprime1,2,3.
4) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{ int m(int a){ return 1 ;}}
2 class C{ int m(double b){ return 2 ;}}
3 class A extends B, C{
4 public static void main(String [] args){
5 System.out.println(new C().m(3));
6 }
7 }
a) Ocódigonãocompila.
b) Compila e imprime 1.
c) Compila e imprime 2.
d) Compilaeimprime1,2.
5) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{ private B() {} static BB (String s)
2 { return new B( ) ;}}
3 class A{
266

## Página 272

CasadoCódigo Capítulo9. Trabalhandocomherança
4 public static void main(String[] args){
5 Bb = B.B("t");
6 }
7 }
a) Não compila.
b) Compila e imprime “t”.
c) Compilaenãoimprimenada.
d) Compilaejogaumaexception.
6) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{ private B() {} static BB (String s)
2 { return new B( ) ;}}
3 class A extends B {
4 public static void main(String[] args){
5 Bb = B.B("t");
6 }
7 }
a) Não compila.
b) Compila e imprime “t”.
c) Compilaenãoimprimenada.
d) Compilaejogaumaexception.
7) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{
2 private String s ;
3 protected B() {}
4 static A B(String s ){
5 return new A();
6 }
7 }
8 class A extends B {
9 A(String s ){
267

## Página 273

9.1. Implementandoherança CasadoCódigo
10 this.s = s;
11 }
12 public static void main(String[] args){
13 Bb = A.B("t");
14 System.out.println(b.s);
15 }
16 }
a) Não compila.
b) Compila e imprime “t”.
c) Compilaenãoimprimenada.
d) Compilaejogaumaexception.
8) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{
2 protected String s;
3 protected B() {}
4 static A B(String s ){
5 return new A();
6 }
7 }
8 class A extends B {
9 A(String s ){
10 this.s = s;
11 }
12 public static void main(String[] args){
13 Ab = A.B("t");
14 System.out.println(b.s);
15 }
16 }
a) Não compila.
b) Compila e imprime “t”.
c) Compilaenãoimprimenada.
d) Compilaejogaumaexception.
268

## Página 274

CasadoCódigo Capítulo9. Trabalhandocomherança
9.2 Desenvolva código que mostra o uso de
polimorfismo
Reescrita ou sobrescrita é a maneira como uma subclasse poderedefinir o
comportamentodeummétodoquefoiherdadodeumadassuassuperclasses
(diretaouindiretamente).
class Veiculo {
public void liga() {
System.out.println("Veiculo está sendo ligado!" );
}
}
class Carro extends Veiculo {
public void liga() {
System.out.println("Carro está sendo ligado!" );
}
}
Agoraconsidere:
public class Teste{
public static void main(String [] args){
Veiculo v = new Carro();
v.liga();
}
}
Ométodochamadoaquiseráodaclasse Carro,independentedearefer-
ênciaserdotipo Veiculo(oqueim po rtaéoob jeto).
Qualmétodoseráexecutadoédescobertoem tempodeexecução (aassi-
natura é decidida em tempo de compilação!), isso é a chamada virtual de
método(virtualmethodinvocation ).
Parareescreverummétodo,énecessário:
• exatamenteomesmonome;
• osparâmetrostêmqueseriguaisemtipoeordem(nomespodemmu-
dar);
269

## Página 275

9.2. Desenvolvacódigoquemostraousodepolimorfismo CasadoCódigo
• retornodométododeveserigualoumaisespecíficoqueodamãe;
• visibilidadedeveserigualoumaiorqueodamãe;
• exceptionslançadasdevemseriguaisoumenosquenamãe;
• métodonamãenãopodeser
final.
Seessasregrasnãoforemrespeitadas,podehaverumerrodecompilação,
ouométododeclaradonãoseráconsideradoumareescritadométodo.
Aregrasobrevisibilidadeé: ummétodoreescritosópodetervisibilidade
maior ou igual à do método que está sendo reescrito. (Essa não é uma regra
mágica! Faz todo o sentido; pense um pouco sobre o que poderia acontecer
seessaregranãoexistisse).
Ocódigoaseguirnãocompila,pois
ligarépúbliconaclassemãe,então
sópodeserreescritocomvisibilidadepública:
class Veiculo {
public void liga() {
System.out.println("Veiculo esta sendo ligado!");
}
}
class Carro extends Veiculo {
protected void liga() {
System.out.println("Carro esta sendo ligado!" );
}
}
Muito cuidado com interfaces, pois a definição de um método é, por
padrão, public e o exercício pode apresentar uma pegadinha de compi-
lação:
interface A{
void a();
}
class B implements A {
void a() {
// não compila, o método deveria ser público
270

## Página 276

CasadoCódigo Capítulo9. Trabalhandocomherança
}
}
class C implements A {
public void a() {
// compila
}
}
Estranhamente, um método sobrescrito pode ser abstrato, dizendo para
o compilador que quem herdar dessa classe terá que sobrescrever o método
original:
class A{
void a() {
}
}
abstract class B extends A {
abstract void a(); // sobrescrevendo como abstrato
}
class C extends B{
// não compila, não redefiniu a
}
class D extends B{
void a() {
// compila pois redefiniu a
}
}
Sobreo retornocovariante: permitequeaclassefilhatenhaumretorno
igualoumaisespecíficopolimorficamente(umsubtipo).
Cuidado! Oretornocovariantenãovaleparatiposprimitivos. Umexem-
ploderetornocovariante:
class A{
List<String> metodo () {
// devolve lista
}
271

## Página 277

9.2. Desenvolvacódigoquemostraousodepolimorfismo CasadoCódigo
}
class B extends A {
ArrayList< String> metodo() {
// devolve array list
}
}
Outraregraimportantesobrereescritaéaassinaturaemrelaçãoao lança-
mentodeexceções ( throws). Ummétodoreescritosópodelançarasmesmas
exceções checkedou menos que o métodos que está sendo reescrito (quanto
àsunchecked,nãoháregrasesemprepodemoslançarquantasquisermos).
import java.sql.SQLException;
import java.io.IOException;
class A{
public void metodo () throws SQLException, IOException {
}
}
class B extends A {
public void metodo () throws IOException {
}
}
Esse código compila, pois o método na classeA lança menos exceções
quenaclassemãe,respeitandoaregra. Jáocódigoaseguirnãocompila:
import java.sql.SQLException;
import java.io.IOException;
class A{
public void metodo () throws SQLException {
}
}
class B extends A {
public void metodo () throws IOException {
272

## Página 278

CasadoCódigo Capítulo9. Trabalhandocomherança
}
}
Apesar de ambos os métodos lançarem apenas uma exceção, não é isso
queimporta,poiselassãodiferentes. Outrocasoquenãocompila:
import java.io.IOException;
class A{
public void metodo () throws IOException {
}
}
class B extends A {
public void metodo () throws Exception {
}
}
Exceptionémuitomaisque IOException.
Repareque,quandodizemos menosexceçõesquenamãe ,issoindicanão
apenasquantidade,mastambémdevemosconsideraropolimorfismo. Setro-
carmos o exemplo anterior, compilamos:
import java.io.IOException;
class A{
public void metodo () throws Exception {
}
}
class B extends A {
public void metodo () throws IOException {
}
}
Compila, pois IOException é mais específico queException na ár-
voredeherança.
273

## Página 279

9.2. Desenvolvacódigoquemostraousodepolimorfismo CasadoCódigo
Polimorfismoechamadasdemétodos
Imagineasclasses:
class Veiculo {
void liga() {
System.out.println("ligando o veiculo" );
}
}
class Carro extends Veiculo {
void liga() {
System.out.println("ligando o carro" );
}
void desliga() {
}
}
Se tivermos um objeto do tipo Carro com uma referência do tipo
Carro,ouseja,semusarpolimorfismo,podemosfazer:
Carro c = new Carro();
c.liga(); // ligando o carro
c.desliga();
Conseguimos chamar os dois métodos. E, como estamos trabalhando
co msob r escri ta,ométodoligachamadoéodaclassefilha Carro.
M aseseusarmospolimo rfismoear efer ênciapara Veiculo?
Veiculo v = new Carro();
v.liga(); // ligando o carro?
v.desliga();
Vamos linha por linha: primeiro, podemos chamar um Carro de
Veiculo porque ele éu m (compila sem problemas). Podemos também
chamar o método liga pois ambas as classes o possuem. Mas o método
queseráinvocadoseráodaclassefilha,osobrescrito.
Já a chamada ao métododesliga não compilará, porque ele não está
definidonaclasse Veiculo. Comoareferênciaédessetipo,ométodo(que
existenoobjeto)nãoévisível.
274

## Página 280

CasadoCódigo Capítulo9. Trabalhandocomherança
A regra é: para saber se um método de um objeto pode ser chamado,
olhamos para o tipo da referência em tempo de compilação. Para realmente
chamarométodoemtempodeexecução,devemosolharparaoobjetoaoque
demos
new.
Essa regra faz sentido quando pensamos em um método polimórfico
comooseguinte:
void metodo ( Veiculo v){
v.liga(); // compila
v.desliga(); // não compila
}
Se passarmos um objeto Carro para o método, teoricamente ambas
as chamadas funcionariam, já que a classe possui tanto oliga quanto o
desliga.
Masimagineumaclasse Moto quenãotemométodo desliga.C o m o
Moto éu m Veiculo, podemos passar como argumento. O que aconteceria
se pudéssemos ter chamado odesliga na referência Veiculo? Alguma
coisaestariaerrada.
Portanto, a regra geral é que somente podemos acessar os métodos de
acordo com o tipo da referência, pois a verificação da existência do método
é feita em compilação. Mas qual o método que será invocado, isso será con-
feridodinamicamente,emexecução.
Um ponto muito importante é que o compiladornuncasabeovalordas
variáveisdepoisdalinhaqueascria. Ouseja,ocompiladornãosabeseesta-
mos passando um
Carro ou uma Moto.Oq u ee l es a b eéa p e n a sot i p od a
variável;nocaso, Veiculo.Ec o m oVeiculonãotemométodo desliga,
ocódigonãopodeco m p ilar .
this,superesobrescritademétodos
Na ocasião em que um método foi sobrescrito, podemos utilizar as
palavras-chave supere thisparadeixarexplícitoqualmétododesejamos
invocar:
class A{
public void metodo() {
275

## Página 281

9.2. Desenvolvacódigoquemostraousodepolimorfismo CasadoCódigo
System.out.println("a");
}
}
class B extends A {
public void metodo() {
System.out.println("b");
super.metodo(); // imprime a
}
public void metodo2() {
metodo(); // imprime b, a
super.metodo(); // imprime a
}
}
Eseeuinvocarosegundométodonaprimeiraclasse? Semo this?
class A{
public void metodo() {
System.out.println("a");
metodo2();
}
public void metodo2() {
System.out.println("metodo 2 do pai");
}
}
class B extends A {
public void metodo() {
System.out.println("b");
super.metodo();
}
public void metodo2() {
System.out.println("c");
metodo();
super.metodo();
}
public static void main(String[] args){
new B().metodo2();
}
}
276

## Página 282

CasadoCódigo Capítulo9. Trabalhandocomherança
O Java entra em loop infinito, uma vez que o método será invocado no
objeto. Então faremos olookupdo metodo2 dinamicamente, encontrando
o metodo2quechama metodo,quechama metododopai,quechamano-
vamente metodo2. Notequeo lookupdosmétodos,o bindingdosmétodos,
éfeitoemexecuçãomesmoseinvocarmosdentrodeumpróprioobjeto. Até
mesmoousodapalavra-chave thisnãoevi tariaisso ,ca usandooloo p:
class A{
public void metodo() {
System.out.println("a");
this.metodo2();
}
public void metodo2() {
System.out.println("metodo 2 do pai");
}
}
class B extends A {
public void metodo() {
System.out.println("b");
super.metodo();
}
public void metodo2() {
System.out.println("c");
metodo();
super.metodo();
}
public static void main(String [] args){
new B().metodo2();
}
}
1) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{
2 void x() throws IOException {
3 System.out.println("c");
4 }
5 }
277

## Página 283

9.2. Desenvolvacódigoquemostraousodepolimorfismo CasadoCódigo
6 class C extends B {
7 void x() throws FileNotFoundException {
8 System.out.println("b");
9 }
10 }
11 class A{
12 public static void main(String[] args){
13 new C().x();
14 }
15 }
a) Não compila.
b) Compila e imprime ‘b‘.
c) Compila e imprime ‘c‘.
d) Compilaenãoimprimenada.
e) Compilaedáexception.
f) Compilaeentraemloop.
2) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 import java.io.*;
2 class B{
3 void x() throws IOException {
4 System.out.println("c");
5 }
6 }
7 class C extends B {
8 void x() throws FileNotFoundException {
9 System.out.println("b");
10 }
11 }
12 class A{
13 public static void main(String[] args) throws IOException {
14 new C().x();
15 }
16 }
278

## Página 284

CasadoCódigo Capítulo9. Trabalhandocomherança
a) Não compila.
b) Compila e imprime ‘b‘.
c) Compila e imprime ‘c‘.
d) Compilaenãoimprimenada.
e) Compilaedáexception.
f) Compilaeentraemloop.
3) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 import java.io.*;
2 class B{
3 void x(double i) throws IOException {
4 System.out.println("c");
5 }
6 }
7 class C extends B {
8 void x(int i) throws FileNotFoundException {
9 System.out.println("b");
10 }
11 }
12 class A{
13 public static void main(String[] args) throws IOException {
14 new C().x(3.2);
15 }
16 }
a) Não compila.
b) Compila e imprime ‘b‘.
c) Compila e imprime ‘c‘.
d) Compilaenãoimprimenada.
e) Compilaedáexception.
f) Compilaeentraemloop.
4) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
279

## Página 285

9.2. Desenvolvacódigoquemostraousodepolimorfismo CasadoCódigo
1 import java.io.*;
2 class B{
3 void x(double i) throws IOException {
4 System.out.println("c");
5 }
6 }
7 class C{
8 void x(int i) throws FileNotFoundException {
9 System.out.println("b");
10 }
11 }
12 class A{
13 public static void main(String[] args) throws IOException {
14 new C().x(3.2);
15 }
16 }
a) Não compila.
b) Compila e imprime ‘b‘.
c) Compila e imprime ‘c‘.
d) Compilaenãoimprimenada.
e) Compilaedáexception.
f) Compilaeentraemloop.
5) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 import java.io.*;
2 interface B{
3 public void x(double i) throws IOException {
4 System.out.println("c");
5 }
6 }
7 class C implements B {
8 public void x(int i) throws FileNotFoundException {
9 System.out.println("b");
10 }
11 }
280

## Página 286

CasadoCódigo Capítulo9. Trabalhandocomherança
12 class A{
13 public static void main(String[] args) throws IOException {
14 new C().x(3);
15 }
16 }
a) Não compila.
b) Compila e imprime ‘b‘.
c) Compila e imprime ‘c‘.
d) Compilaenãoimprimenada.
e) Compilaedáexception.
f) Compilaeentraemloop.
6) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 import java.io.*;
2 class B{
3 void x(int i) throws IOException {
4 System.out.println("c");
5 }
6 }
7 abstract class C extends B throws IOException {
8 abstract void x(int i);
9 }
10 abstract class D extends C {
11 void x(int i) throws IOException {
12 System.out.println("d");
13 }
14 }
15 class E extends D {
16 }
17 class A{
18 public static void main(String[] args) throws IOException {
19 new E().x(32);
20 }
21 }
281

## Página 287

9.2. Desenvolvacódigoquemostraousodepolimorfismo CasadoCódigo
a) Não compila.
b) Compila e imprime ‘b‘.
c) Compila e imprime ‘c‘.
d) Compila e imprime ‘d‘.
e) Compilaenãoimprimenada.
f) Co m p ilaedáexcep tio n.
g) Compilaeentraemloop.
7) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 import java.io.*;
2 class B{
3 void x(int i) throws IOException {
4 if(i<0) return ;
5 x(-1);
6 System.out.println("c");
7 }
8 }
9 abstract class C extends B {
10 void x(int i) throws IOException {
11 System.out.println("b");
12 super.x(i);
13 }
14 }
15 abstract class D extends C {
16 void x(int i) throws IOException {
17 super.x(i);
18 }
19 }
20 class E extends D {
21 }
22 class A{
23 public static void main(String[] args) throws IOException {
24 new E().x(32);
25 }
26 }
282

## Página 288

CasadoCódigo Capítulo9. Trabalhandocomherança
a) Não compila.
b) Compila e imprime ‘b‘.
c) Compila e imprime ‘c‘.
d) Compila e imprime ‘d‘.
e) Compilaenãoimprimenada.
f) Co m p ilaedáexcep tio n.
g) Compilaeentraemloop.
8) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 import java.io.*;
2 class B{
3 void x(int i) throws IOException {
4 if(i<0) return ;
5 this.x(-1);
6 System.out.println("c");
7 }
8 }
9 abstract class C extends B {
10 void x(int i) throws IOException {
11 System.out.println("b");
12 super.x(i);
13 }
14 }
15 abstract class D extends C {
16 void x(int i) throws IOException {
17 super.x(i);
18 }
19 }
20 class E extends D {
21 }
22 class A{
23 public static void main(String[] args) throws IOException {
24 new E().x(32);
25 }
26 }
283

## Página 289

9.2. Desenvolvacódigoquemostraousodepolimorfismo CasadoCódigo
a) Não compila.
b) Compila e imprime ‘b‘.
c) Compila e imprime ‘c‘.
d) Compila e imprime ‘b‘,‘c‘.
e) Compilaenãoimprimenada.
f) Co m p ilaedáexcep tio n.
g) Compilaeentraemloop.
9) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 import java.io.*;
2 class B{
3 void x(int i) throws IOException {
4 if(i<0) return ;
5 super.x(-1);
6 System.out.println("c");
7 }
8 }
9 abstract class C extends B {
10 void x(int i) throws IOException {
11 System.out.println("b");
12 super.x(i);
13 }
14 }
15 abstract class D extends C {
16 void x(int i) throws IOException {
17 super.x(i);
18 }
19 }
20 class E extends D {
21 }
22 class A{
23 public static void main(String[] args) throws IOException {
24 new E().x(32);
25 }
26 }
284

## Página 290

CasadoCódigo Capítulo9. Trabalhandocomherança
a) Não compila.
b) Compila e imprime ‘b‘.
c) Compila e imprime ‘c‘.
d) Compila e imprime ‘b‘,‘c‘.
e) Compilaenãoimprimenada.
f) Co m p ilaedáexcep tio n.
g) Compilaeentraemloop.
9.3 Diferencieentreotipodeumareferênciae
otipodeumobjeto
Semprequeestendemosalgumaclasseouimplementamosalgumainterface,
estamosrelacionandonossaclassecomaclassemãeouinterfaceusandoum
relacionamentochamadode éum.
Se
Carro extends Veiculo ,dizemosque Carro éu mVeiculo.O us e
ArrayList implements List dizemosque ArrayList éu mList.
O relacionamento deéum é um dos recursos mais poderosos da orien-
taçãoaobjetos. Eéchamadoformalmentede polimorfismo.
Polimorfismo é a capacidade que temos de referenciar um objeto de for-
masdiferentes,segundoseusrelacionamentosde éu m.
Emespecial,usamospolimorfismoquandoescrevemos:
Veiculo v = new Carro();
List l = new ArrayList();
Asherançaseimplementaçõesvãoformandoumaárvorequeterásempre
comoraizaclasse Object. Assim,diretaouindiretamente,todoobjeto éum
Object.
O polimorfismo pode ser aplicado à passagem de parâmetros (e é aí que
estáseugrandepoder). Imagineasclasses:
class Veiculo {}
class Carro extends Veiculo {}
285

## Página 291

9.3. Diferencieentreotipodeumareferênci aeoti podeumob jeto CasadoCódigo
class Moto extends Veiculo {}
class Onibus extends Veiculo {}
class Conversivel extends Carro {}
Setemosummétodoquerecebe Veiculo,podemospassarqualquerum
daquelesobjetos:
void metodo ( Veiculo v ){
}
// .....
metodo(new Carro());
metodo(new Moto ());
metodo(new Onibus());
metodo(new Veiculo());
metodo(new Conversivel());
Dessaforma,conseguimosobterumfortereaproveitamentodecódigo.
Repare que, quando usamos polimorfismo, estamos mudando o tipo da
referência, mas nunca o tipo do objeto. Em Java, objetos nunca mudam seu
ti po ,queéaqueleo ndedemosnew. Oquefazemoséchamar(referenciar)o
objeto de várias formas diferentes. Chamar de várias formas.... é o polimor-
fismo.
Podemos referenciar um objeto pelo seu próprio tipo, por uma de suas
classespai,ouporqualquerinterfaceimplementadaporele,diretaouindire-
tamente:
interface A{ }
interface B{ }
class C implements A {}
class D extends C implements B {}
public class Teste {
public static void main(String[] args){
// mesmo tipo, compila
Dd = new D();
286

## Página 292

CasadoCódigo Capítulo9. Trabalhandocomherança
// D extends C, todoDéu mC , compila
Cc= new D();
Cc 2 = d;
// D implements B, todo D implementa B, compila
Bb = new D();
Bb 2 = d;
// D implements A indiretamente, compila
Aa = new D();
Aa 2 = a;
Dd 2 = new C(); // não, C não é D, não compila
Dd 3 = new D();
Cc 3 = d3; // compila
Dd 4 = c3; // não compila, por mais que o ser humano
// saiba, em execução, nem todo C é um D.
}
}
Ecomofuncionaoacessoàsvariáveismembroeaosmétodos? Setemos
uma referência para a classe mãe, não importa o que o valor seja em tempo
de execução, o compilador não conhece o tempo de execução, então ele só
compilachamadasaosmétodosdefinidosnaclassemãe:
class Veiculo {
public void liga() { }
}
class Carro {
public void mudaMarcha() {}
}
// teste
Veiculo v = new Veiculo();
v.liga(); // compila
Carro c = new Carro(); // ok
287

## Página 293

9.3. Diferencieentreotipodeumareferênci aeoti podeumob jeto CasadoCódigo
c.mudaMarcha(); // compila
Veiculo v2 = c;
v2.liga(); // todo veiculo tem método liga, compila
v2.mudaMarcha(); // não compila, nem todo veiculo tem
Mesmo em casos em que “achamos” que todo veículo tem, se o método
nãofoidefinidonaclassedereferência,ocodigonãocompila:
abstract class Veiculo {
public void liga() { }
}
class Carro {
public void desliga() { }
}
class Moto {
public void desliga() { }
}
Carro c = new Carro(); // ok
c.desliga(); // compila
Veiculo v2 = c;
v2.desliga(); // não compila, Veiculo não tem o método desliga
// definido
Omesmovaleráparavariáveismembro:
class Veiculo {
int velocidade ;
}
class Carro {
int marcha;
}
// teste
Veiculo v = new Veiculo();
v.velocidade = 3; // compila
Carro c = new Carro(); // ok
288

## Página 294

CasadoCódigo Capítulo9. Trabalhandocomherança
c.marcha = 1; // compila
Veiculo v2 = c;
v2.velocidade = 5; // compila
v2.marcha = 7; // não compila
Etemosquecuidardemaisumcasoespecífico: oqueaconteceseestamos
trabalhandocompacotesdistintos?
Seométododaclassepaiqueestásendosobrescritoé public,osméto-
dosquesobrescrevemdevemser public,entãonãotemmuitagraça.
J áseométododaclassepaié protected,osfilhossão protectedou
public,quetambémnãotemgraça,poisofilho mesmoemoutropacote já
tinhaacessoaométododopai.
Masoqueaconteceseométodonopaié privateeeutentosobrescrevê-
lo? Ou se o método é default e tento sobrescrevê-lo em outro pacote?
O mesmo valerá tanto paraprivate quando para modificador de escopo
padrão:
package financeiro;
public class ContaFinanceira extends modelo.Conta {
void fecha() {
System.out.println("fechando financeiro" );
}
}
package modelo ;
public class Conta {
void fecha() {
System.out.println("fechando conta normal" );
}
}
Ao invocar o métodofecha através de uma referência paraConta ou
ContaFinanceira,oresultadoserátotalmentediferente:
ContaFinanceira c = new ContaFinanceira();
c.fecha();
Conta d = c;
d.fecha();
289

## Página 295

9.3. Diferencieentreotipodeumareferênci aeoti podeumob jeto CasadoCódigo
O código não compila, dependendo do pacote onde ele está. Como as-
sim? Acontece que o método não foi sobrescrito, a classe filha nem sabe da
existência do método (privado ou default) do pai, portanto o que ela fez foi
criarummétodoto talmen teno vo .
Nessecaso,aoinvocarmosométododurantecompilação,o bindingéfeito
para o método específico de cada uma delas, uma vez que são métodos to-
talmente diferentes. Se o código está no pacote de modelo, a chamada ao
método
fecha de Conta compilaeimprimiria normal. Seestivermosno
pacote financeiro,achamadaao ContaFinanceiracompilaeimprime
financeiro.
Lembre-se que os métodos privados terão um efeito equivalente: eles só
sãovistosinternamenteàclasseondeforamdefinidos.
1) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class D extends C {
2 void x() { System.out.println(1); }
3 }
4 class C extends B {
5 void x() { System.out.println(2); }
6 }
7 class B{
8 void x() { System.out.println(3); }
9 void y(Bb ){
10 b.x();
11 }
12 void y(Cb ){
13 c.x();
14 }
15 void y(Db ){
16 d.x();
17 }
18 }
19 class A{
20 public static void main(String[] args){
21 new B().y(new C());
22 }
23 }
290

## Página 296

CasadoCódigo Capítulo9. Trabalhandocomherança
a) Não compila.
b) Compila e imprime 1.
c) Compila e imprime 2.
d) Compila e imprime 3.
2) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class D extends C {
2 void x() { System.out.println(1); }
3 }
4 class C extends B {
5 void x() { System.out.println(2); }
6 }
7 class B{
8 void x() { System.out.println(3); }
9 void y(Bb ){
10 b.x();
11 }
12 void y(Cc ){
13 c.x();
14 }
15 void y(Dd ){
16 d.x();
17 }
18 }
19 class A{
20 public static void main(String[] args){
21 new B().y(new C());
22 }
23 }
a) Não compila.
b) Compila e imprime 1.
c) Compila e imprime 2.
d) Compila e imprime 3.
291

## Página 297

9.3. Diferencieentreotipodeumareferênci aeoti podeumob jeto CasadoCódigo
3) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class D extends C {
2 void x() { System.out.println(1); }
3 }
4 class C extends B {
5 void x() { System.out.println(2); }
6 }
7 class B{
8 void x() { System.out.println(3); }
9 void y(Bb ){
10 b.x();
11 }
12 }
13 class A{
14 public static void main(String[] args){
15 new B().y(new C());
16 }
17 }
a) Não compila.
b) Compila e imprime 1.
c) Compila e imprime 2.
d) Compila e imprime 3.
4) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class D extends C {
2 void x() { System.out.println(1); }
3 void y(Cb ){
4 x();
5 }
6 }
7 class C extends B {
8 void x() { System.out.println(2); }
9 }
10 class B{
11 void x() { System.out.println(3); }
292

## Página 298

CasadoCódigo Capítulo9. Trabalhandocomherança
12 void y(Bb ){
13 b.x();
14 }
15 }
16 class A{
17 public static void main(String[] args){
18 new B().y(new C());
19 }
20 }
a) Não compila.
b) Compila e imprime 1.
c) Compila e imprime 2.
d) Compila e imprime 3.
5) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class D extends C {
2 void x() { System.out.println(1); }
3 void y(Cb ){
4 x();
5 }
6 }
7 class C extends B {
8 void x() { System.out.println(2); }
9 }
10 class B{
11 void x() { System.out.println(3); }
12 void y(Bb ){
13 b.x();
14 }
15 }
16 class A{
17 public static void main(String[] args){
18 new D().y(new C());
19 }
20 }
293

## Página 299

9.3. Diferencieentreotipodeumareferênci aeoti podeumob jeto CasadoCódigo
a) Não compila.
b) Compila e imprime 1.
c) Compila e imprime 2.
d) Compila e imprime 3.
6) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
package financeiro;
public class ContaFinanceira extends modelo.Conta {
void fecha() {
System.out.println("fechando financeiro" );
}
}
package modelo ;
public class Conta {
void fecha() {
System.out.println("fechando conta normal" );
}
}
1 package codigo ;
2 import modelo.*;
3 import financeiro.*;
4 class A{
5 public static void main(String[] args){
6 new Conta().fecha();
7 }
8 }
a) Não compila.
b) Compilaerodajogandoexception.
c) Compilaeroda,imprimindo‘fechandofinanceiro‘.
d) Compilaeroda,imprimindo‘fechandocontanormal‘.
7) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
294

## Página 300

CasadoCódigo Capítulo9. Trabalhandocomherança
package financeiro;
public class ContaFinanceira extends modelo.Conta {
void fecha() {
System.out.println("fechando financeiro" );
}
}
package modelo;
public class Conta {
public void fecha() {
System.out.println("fechando conta normal" );
}
}
1 package modelo;
2 import modelo.*;
3 import financeiro.*;
4 class A{
5 public static void main(String[] args){
6 new Conta().fecha();
7 }
8 }
a) Não compila.
b) Compilaerodajogandoexception.
c) Compilaeroda,imprimindo‘fechandofinanceiro‘.
d) Compilaeroda,imprimindo‘fechandocontanormal‘.
8) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
package financeiro;
public class ContaFinanceira extends modelo.Conta {
void fecha() {
System.out.println("fechando financeiro" );
}
}
295

## Página 301

9.3. Diferencieentreotipodeumareferênci aeoti podeumob jeto CasadoCódigo
package modelo ;
public class Conta {
protected void fecha() {
System.out.println("fechando conta normal" );
}
}
1 package codigo ;
2 import modelo.*;
3 import financeiro.*;
4 class A{
5 public static void main(String[] args){
6 new Conta().fecha();
7 }
8 }
a) Não compila.
b) Compilaerodajogandoexception.
c) Compilaeroda,imprimindo‘fechandofinanceiro‘.
d) Compilaeroda,imprimindo‘fechandocontanormal‘.
9) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
package financeiro;
public class ContaFinanceira extends modelo.Conta {
public void fecha() {
System.out.println("fechando financeiro" );
}
}
package modelo ;
public class Conta {
public void fecha() {
System.out.println("fechando conta normal" );
}
}
296

## Página 302

CasadoCódigo Capítulo9. Trabalhandocomherança
1 package codigo;
2 class A{
3 public static void main(String[] args){
4 new Conta().fecha();
5 }
6 }
a) Não compila.
b) Compilaerodajogandoexception.
c) Compilaeroda,imprimindo‘fechandofinanceiro‘.
d) Compilaeroda,imprimindo‘fechandocontanormal‘.
10) Oqueacontececomocódigoaseguir?
interface Veiculo {
int getMarcha();
void liga();
}
abstract class Carro implements Veiculo {
public void liga() {
System.out.println("ligado!");
}
}
class CarroConcreto extends Carro implements Veiculo {
public int getMarcha() {
return 1;
}
}
9.4 Determinequandoénecessáriofazercast-
ing
Às vezes, temos referências de um tipo mas sabemos que lá há um objeto de
outrotipo,ummaisespecífico:
297

## Página 303

9.4. Determinequandoénecessáriofazercasting CasadoCódigo
public class Teste{
public static void main(String...args){
Object[] objetos = new Object[100];
String s = "certificacao";
objetos[0] = s;
String recuperada = objetos[0];
}
}
Ocódigoacimanãocompila:
Teste.java:3: incompatible types
found : java.lang.Object
required: java.lang.String
String recuperada = objetos[0];
^
1 error
T e m o su ma r r a yd er e f e r ê n c i a sp a r aObject. Nem todo Object é
uma String, então o compilador não vai deixar você fazer essa conversão.
Lembre-seque,emgeral,ocompiladornãoconheceos valoresdasvariáveis,
apenasseustipos.
Vamosprecisar moldarareferênciaparaqueocódigocompile:
String recuperada =( String) objetos[0];
A partir de agora, esse código compila. Mas será que roda? Du-
r a n t eae x e c u ç ã o ,ocastingvai ver se aquele objeto é mesmo compatível
com o tipo String (no nosso caso é). Se não fosse, ele lançaria uma
ClassCastException(exceçãounchecked).
Considereasclasses:
class Veiculo {}
class Moto extends Veiculo {}
class Carro extends Veiculo {}
298

## Página 304

CasadoCódigo Capítulo9. Trabalhandocomherança
Eocódigo:
Veiculo v = new Carro();
Moto m = v;
Na primeira linha, usamos polimorfismo para chamar umCarro de
Veiculo (éum ). Na segunda linha, o que o compilador sabe é quev éd o
tipo Veiculo.E nem todo Veiculo éu m aMoto. Por isso, essa linha não
compila.
Masexistem alguns Veiculoquesão Moto. Então,ocompiladordeixa
quefaçamosocasting:
Veiculo v = new Carro();
Moto m =( Moto) v;
C o mi s s o ,oc ó d i g oc o m p i l a ,m a sr e p a r eq u e ,e mt e m p od ee x e c u ç ã o ,
v aponta para um objeto do tipoCarro. Quando o código for executado,
haverá um erro de execução:ClassCastException. Carronão éu m a
Moto.
Cuidado que, se ocasting for totalmente impossível, o compilador já
acusaráerro:
Carro c = new Carro();
Moto m =( Moto) c;
Um Carronunca poderá ser umaMoto. Então, nem com casting isso
compila.
É importante lembrar que quando não precisamos de casting, ele é op-
cional,portantotodasaslinhasaseguirfuncionamcomousemcasting:
299

## Página 305

9.4. Determinequandoénecessáriofazercasting CasadoCódigo
String guilherme = "guilherme";
String nome = guilherme;
String nome2 =( String ) guilherme;
Object nome3 = guilherme;
Object nome4 =( String ) guilherme;
Object nome5 =( Object ) guilherme;
Regrageral!
Se você está subindo na hierarquia de classes, a autopromoção vai
fazer tudo sozinho; e se você estiver descendo, vai precisar de casting.
Senãoho uverumcaminhopossível,nãoco m p ilanemco mcasting.
Na prova, faça sempre os diagramas de hierarquia de tipos que fica
extremamentefácilresolveressescastings.
Castingcominterfaces
Dadoocódigoaseguir:
Carro c = new Carro();
Moto m =( Moto) c;
Quando dizemos que ele não compila, é porque umCarro nuncapode
ser uma Moto. Mas como o compilador sabe que isso é impossível mesmo?
Existealgumachancedealgumobjetodequalquertiposer,aomesmotempo,
Carroe Moto?
class X extends Moto, Carro { // não compila!
}
AúnicamaneiradeissoacontecerseriaseJavasuportasseherançamúlti-
pla; aí escreveríamos uma classe que herdasse deCarro e Moto ao mesmo
tempo. ComoJavanãotemherançamúltipla,issorealmenteéimpossívelde
acontecer.
Masequandofazemoscastingcominterfacesenvolvidas? Apesardenão
existir herança múltipla, podemos implementar múltiplas interfaces! Fazer
300

## Página 306

CasadoCódigo Capítulo9. Trabalhandocomherança
casting para interfaces sempre é possível e vai compilar (há apenas uma ex-
ceçãoaessaregra).
Pegue uma interfacequalquer, por exemplo Runnable. O código a
seguircompila:
Carro c = new Carro();
Runnable r =( Runnable) c ;
Um Carro pode serum Runnable? Sabemosqueaclasse Carro pro-
priamentenãoimplementaessainterface. Masexisteapossibilidadedeexistir
algumobjetoemJavaqueseja,aomesmotempo,
Carroe Runnable?
Arespostaésim! Esetivéssemosumaclasse CarroRodavel?
class CarroRodavel extends Carro implements Runnable { ... }
Ocompiladornãosabeovalordavariável cnesseexemplo. Elenãosabe
q u en av e r d a d eéu m ai n s t â n c i ad eCarro e não de CarroRodavel.E l e
sabe apenas que é do tipoCarro e, pela simples possibilidade de existir um
objetoqueseja Carroe Runnable,eledeixaocódigocompilar.
Masreparequeaclasse CarroRodavelnãoexistenodiagramaoriginal.
Mesmo assim, o código compila! Apenas com apossibilidadede existir uma
classe dessa, o compilador já aceita aquele casting, mesmo que uma classe
dessasnãoexistanaprática.
Cla r oq u eoo b je t oéd oti poCarro, que não implementaRunnable e,
emtempodeexecução,vaiocorreruma ClassCastingException.
Efinal
Dizemosqueocódigoanteriorcompilaporqueháapossibilidadede
umaclassecomo CarroRodavelexistiralgumdia. Masseráquesem-
preháessapossibilidademesmo?
Se a classe Carro for final, é impossível existir uma classe filha
dela. Ecomoaprópria Carro nãoimplementa Runnable,nessecaso,
seráimpossívelfazerocastingpara Runnable(oprópriocompiladorjá
acusaerro).
301

## Página 307

9.4. Determinequandoénecessáriofazercasting CasadoCódigo
Dica
Muitos exercícios são sobre casting de referência. Uma dica é seguir
oqueépossível,impossíveleóbvio.
S eéó b v i oq u eoc a s t i n gf u n c i o n a ,i s s oé ,s eac o n v e r s ã oés e m p r e
verdade,aautopromoçãofazsozinha.
Seocastingépossível,masnemsempreéverdade,ocastingcompila,
maspodelançarerroemtempodeexecução.
Se o casting é impossível, isto é, ele nunca pode dar certo, o código
nãovaicompilarnemcomcasting.
Emalgunslivros,vocêencontratabelascomplicadasegrandesqueo
“ajudam” a decidir se o casting compila e roda, mas é muito mais fácil
seguirpelalógica.
instanceof
O operador instanceof ( a instanceof Classe ) devolve true
casoareferência aaponteparaumobjetocompatível( assignable,atribuível)
aotipo Classe.
Object c = new Carro();
boolean b1 = c instanceof Carro; // true
boolean b2 = c instanceof Moto; // false
O instanceof nãocompilaseareferênciaemquestãoforobviamente
incompatível,porexemplo:
String s = "a";
boolean b = s instanceof java.util.List; // não compila
302

## Página 308

CasadoCódigo Capítulo9. Trabalhandocomherança
Detalhe
instanceof é um operador que deve ser usado com extremo
cuidadonodiaadia. Emmuitoscas os,eleindicaafracamodelagemde
umsistema,comblocosqueparecem“ switchs”epoderiamsertrocados
porpolimorfismo.
1) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 interface Z{ }
2 interface W {};
3 interface Y extends Z , W {}
4 class B{ }
5 class C extends B implements Y {}
6 class D extends B implements Z, W {}
7 class E extends C {}
8 class A{
9 public static void main(String[] args){
10 Bb = new C();
11 }
12 }
a) Nãocompilanadefiniçãodasclasseseinterfaces.
b) Nãocompiladentrodométodo main.
c) Compilaerodasemexception.
d) Compilaerodadandoexception.
2) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 interface Z{ }
2 interface W{ }
3 interface Y extends Z , W {}
4 class B{ }
5 class C extends B implements Y {}
6 class D extends B implements Z, W {}
303

## Página 309

9.4. Determinequandoénecessáriofazercasting CasadoCódigo
7 class E extends C {}
8 class A{
9 public static void main(String[] args){
10 Cc =( C) new B();
11 }
12 }
a) Nãocompilanadefiniçãodasclasseseinterfaces.
b) Nãocompiladentrodométodo main.
c) Compilaerodasemexception.
d) Compilaerodadandoexception.
3) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 interface Z{ }
2 interface W{ }
3 interface Y extends Z , W {}
4 class B{ }
5 class C extends B implements Y {}
6 class D extends B implements Z, W {}
7 class E extends C {}
8 class A{
9 public static void main(String[] args){
10 Yy = new D();
11 }
12 }
a) Nãocompilanadefiniçãodasclasseseinterfaces.
b) Nãocompiladentrodométodo main.
c) Compilaerodasemexception.
d) Compilaerodadandoexception.
4) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 interface Z{ }
2 interface W{ }
304

## Página 310

CasadoCódigo Capítulo9. Trabalhandocomherança
3 interface Y extends Z , W {}
4 class B{ }
5 class C extends B implements Y {}
6 class D extends B implements Z, W {}
7 class E extends C {}
8 class A{
9 public static void main(String[] args){
10 Yy =( Y) new D();
11 }
12 }
a) Nãocompilanadefiniçãodasclasseseinterfaces.
b) Nãocompiladentrodométodo main.
c) Compilaerodasemexception.
d) Compilaerodadandoexception.
5) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 interface Z{ }
2 interface W{ }
3 interface Y extends Z , W {}
4 class B{ }
5 class C extends B implements Y {}
6 class D extends B implements Z, W {}
7 class E extends C {}
8 class A{
9 public static void main(String[] args){
10 Zz =( Z)( B) new D();
11 }
12 }
a) Nãocompilanadefiniçãodasclasseseinterfaces.
b) Nãocompiladentrodométodo main.
c) Compilaerodasemexception.
d) Compilaerodadandoexception.
305

## Página 311

9.4. Determinequandoénecessáriofazercasting CasadoCódigo
6) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 interface Z{ }
2 interface W{ }
3 interface Y extends Z , W {}
4 class B{ }
5 class C extends B implements Y {}
6 class D extends B implements Z, W {}
7 class E extends C {}
8 class A{
9 public static void main(String[] args){
10 Yy =( Y) new A();
11 }
12 }
a) Nãocompilanadefiniçãodasclasseseinterfaces.
b) Nãocompiladentrodométodo main.
c) Compilaerodasemexception.
d) Compilaerodadandoexception.
7) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 interface Z{ }
2 interface W{ }
3 interface Y extends Z , W {}
4 class B{ }
5 class C extends B implements Y {}
6 class D extends B implements Z, W {}
7 class E extends C {}
8 class A{
9 public static void main(String[] args){
10 Dd =( D)( Y)( B) new D();
11 }
12 }
a) Nãocompilanadefiniçãodasclasseseinterfaces.
b) Nãocompiladentrodométodo main.
306

## Página 312

CasadoCódigo Capítulo9. Trabalhandocomherança
c) Compilaeroda.
8) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 interface Z{ }
2 interface W{ }
3 interface Y extends Z , W {}
4 class B{ }
5 class C extends B implements Y {}
6 class D extends B implements Z, W {}
7 class E extends C {}
8 class A{
9 public static void main(String[] args){
10 System.out.println(((B)( Z)( W)( Y) new D()) instanceOf D);
11 }
12 }
a) Nãocompilanadefiniçãodasclasseseinterfaces.
b) Nãocompiladentrodométodo main.
c) Compila e imprimetrue.
d) Compila e imprimefalse.
9) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 interface Z{ }
2 interface W{ }
3 interface Y extends Z , W {}
4 class B{ }
5 class C extends B implements Y {}
6 class D extends B implements Z, W {}
7 class E extends C {}
8 class A{
9 public static void main(String[] args){
10 System.out.println(((B)( Z)( W)( Y) new D()) instanceof D);
11 }
12 }
a) Nãocompilanadefiniçãodasclasseseinterfaces.
307

## Página 313

9.5. Usesuperethisparaacessarobjetoseconstrutores CasadoCódigo
b) Nãocompiladentrodométodo main.
c) Compila e imprimetrue.
d) Compila e imprimefalse.
9.5 Usesuperethisparaacessarobjetosecon-
strutores
Um construtor pode ser sobrecarregado assim como os métodos, e pode ter
qualquermodificadordevisibilidade.
Opontomaisimportantesobreosconstrutoreséque,paraconstruirum
objetodeumaclassefilha,obrigatoriamente,precisamoschamarumconstru-
tordaclassemãeantes. Sempre,emtodososcasos. Parachamaroconstrutor
damãe,usamosachamadaao
super(passandoounãoargumentos):
class Mae {
public Mae(String msg ){
System.out.println(msg);
}
}
class Filha extends Mae {
public Filha(String nome ){
super("construindo parte mae" );
System.out.println("construindo parte filha" );
}
}
Mas, na maioria dos casos, não chamamos o construtor da mãe ex-
plicitamente. Se nenhum construtor da mãe foi escolhido através da
palavra super(...), o compilador colocaautomaticamente super();
noco meçodonossoco nstru to r ,semnemolharparaaclassemãe.
class Mae {
public Mae() {
System.out.println("construindo parte mae" );
}
308

## Página 314

CasadoCódigo Capítulo9. Trabalhandocomherança
}
class Filha extends Mae {
public Filha( String nome ){
// super() esta implícito!!!
System.out.println("construindo parte filha" );
}
}
Considerandoagoraocódigo:
public class X{
public static void main(String [] args){
Filha filha = new Filha("Teste");
}
}
Vai primeiro imprimir “Construindo parte mae” e só depois “Constru-
indopartefilha”.
U m ao u t r ap o s s i b i l i d a d e ,n oc a s od et e r m o sm a i sd eu mc o n s t r u t o r ,é
chamarmos outro construtor da própria classe através dothis():
class Mae {
public Mae() {
System.out.println("construindo parte mae" );
}
}
class Filha extends Mae {
public Filha() {
// super() implicito!
System.out.println("construindo filha parte 1" );
}
public Filha( String nome ){
this();
System.out.println("construindo filha parte 2" );
}
}
309

## Página 315

9.5. Usesuperethisparaacessarobjetoseconstrutores CasadoCódigo
public class X{
public static void main(String [] args){
Filha filha = new Filha( "Teste");
}
}
Agora vai produzir “Construindo parte mae”, “Construindo parte filha
parte1”e“Construindopartefilhaparte2”.
Atenção,achamadadoconstrutorcom super ou this sópodeapare-
cercomoprimeirainstruçãodoconstrutor. Portanto,sópodemosfazeruma
chamadadessestipos.
class Filha extends Object {
public Filha() {
// super() implicito!
}
public Filha(String nome ){
this();
}
public Filha(int idade){
super();
this(); // não compila, ou um ou outro!
}
public Filha(long valor){
this();
this(); // não compila, só uma vez!
}
public Filha(char caracter){
super();
super(); // não compila, só uma vez!
}
}
310

## Página 316

CasadoCódigo Capítulo9. Trabalhandocomherança
thisevariáveismembro
Por vezes, temos variáveis membro com o mesmo nome de variáveis lo-
cais. Oacessosempreseráavariávellocal,excetoquandocolocamoso this,
queindicaqueavariávelmembroseráacessada. Ocódigoaseguirimprimirá
3edepo is5:
class Teste {
int i =5 ;
void roda(int i){
System.out.println(i);
System.out.println(this.i);
}
public static void main() {
new Teste().roda(3);
}
}
No acesso a variáveis membro com othis podem parecer que serão
acessados somente valores da classe atual, mas buscam também nas classes
daqualelaherda:
class A{
int i =5 ;
}
class Teste extends A {
void roda(int i){
System.out.println(this.i); // imprime 5
}
public static void main() {
new Teste().roda(3);
}
}
Tentaracessarumavariávellocalcom thisnão compila:
class Teste {
void roda(int i){
System.out.println(this.i); // não há variável membro i
}
311

## Página 317

9.5. Usesuperethisparaacessarobjetoseconstrutores CasadoCódigo
public static void main() {
new Teste().roda(3);
}
}
Como mostramos, caso a variável seja escondida por uma variável com
mesmo nome em uma classe filha, podemos diferenciar o acesso à variável
membrodaclassefilhaoudapai,explicitando thisou super:
class A{
int i =5 ;
}
class Teste extends A{
int i = 10;
void roda(int i){
System.out.println(i); // imprime 3
System.out.println(this.i); // imprime 10
System.out.println(super.i); // imprime 5
}
public static void main() {
new Teste().roda(3);
}
}
O this é em geral opcional para acessar um método do nosso objeto
atual(seelenãofoiredefinido,daclassemãe):
class A{
int i() { return 5; }
}
class Teste extends A{
void roda() {
System.out.println(this.i()); // imprime 5
}
public static void main() {
new Teste().roda();
}
}
class Teste2 {
312

## Página 318

CasadoCódigo Capítulo9. Trabalhandocomherança
int i() { return 5; }
void roda() {
System.out.println(this.i()); // imprime 5
}
public static void main() {
new Teste().roda();
}
}
thisesuperemvariávelmembro
Eoqueacontecequandoumavariávelmembrotemomesmonomequea
definidanaclassequeherdamos? Senãodefinirmosoacessoatravésde this
nem super,oacessoéàvariáveldaclassefilha. Seusarmos thiséàclasse
filhano vamen teeseusarmos superéàclassepai:
class Veiculo {
double velocidade =30 ;
}
class Carro extends Veiculo {
double velocidade = 50;
void imprime() {
System.out.println(velocidade); // 50
System.out.println(this.velocidade); // 50
System.out.println(super.velocidade); // 30
}
}
class Teste {
public static void main(String[] args){
Carro c = new Carro();
c.imprime();
}
}
Lembre-se que o binding de uma variável ao tipo é feito em compi-
lação, portanto se tentarmos acessar a variável velocidade fora doCarro
a t r a v é sd eu m ar e f e r ê n c i aaCarro, o valor alteradoéod av a r i á v e l
Carro.velocidade:
313

## Página 319

9.5. Usesuperethisparaacessarobjetoseconstrutores CasadoCódigo
class Veiculo {
double velocidade =3 0 ;
}
class Carro extends Veiculo {
double velocidade =5 0 ;
void imprime() {
System.out.println(velocidade ); // 1000
System.out.println(this.velocidade); // 1000
System.out.println(super.velocidade); // 30
}
}
class Teste {
public static void main(String[] args){
Carro c = new Carro();
c.velocidade = 1000;
c.imprime();
}
}
Esefizermosomesmoatravésdeumareferênciaa Veiculo,alteramos
avelocidadedo Veiculo:
class Veiculo {
double velocidade =3 0 ;
}
class Carro extends Veiculo {
double velocidade =5 0 ;
void imprime() {
System.out.println(velocidade ); // 50
System.out.println(this.velocidade); // 50
System.out.println(super.velocidade); // 1000
}
}
class Teste {
public static void main(String[] args){
Carro c = new Carro();
((Veiculo) c).velocidade = 1000;
c.imprime();
}
}
314

## Página 320

CasadoCódigo Capítulo9. Trabalhandocomherança
Estáticonãotemthisnemsuper
Contextos estáticos não possuem nemthis nem super,u m av e zq u e
ocódigonãoéexecutadodentrodeumobjeto:
class A{
int i =5 ;
}
class Teste extends A {
int i = 10;
public static void main() {
this. i=5 ; // this? não compila. código estático
super.i = 10; // super? não compila. código estático
}
}
Por fim, uma última restrição: interfaces não podem ter métodos estáti-
cos,nãocompila(métodos defaultnãosãocobradosnestaprova).
1) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{
2 int x =1 ;
3 }
4 class A extends B {
5 static int x =2 ;
6 public static void main(String[] args){
7 System.out.println(x);
8 }
9 }
a) Não compila.
b) Compila e imprime 1.
c) Compila e imprime 2.
d) Compilaedáexception.
2) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
315

## Página 321

9.5. Usesuperethisparaacessarobjetoseconstrutores CasadoCódigo
1 class B{
2 int x =1 ;
3 }
4 class A extends B {
5 static int x =2 ;
6 public static void main(String[] args){
7 System.out.println(this.x);
8 }
9 }
a) Não compila.
b) Compila e imprime 1.
c) Compila e imprime 2.
d) Compilaedáexception.
3) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{
2 int x =1 ;
3 }
4 class A extends B {
5 static int x =2 ;
6 public static void main(String[] args){
7 System.out.println(super.x);
8 }
9 }
a) Não compila.
b) Compila e imprime 1.
c) Compila e imprime 2.
d) Compilaedáexception.
4) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{
2 int x =1 ;
316

## Página 322

CasadoCódigo Capítulo9. Trabalhandocomherança
3 }
4 class A extends B {
5 static int x =2 ;
6 public static void main(String[] args){
7 System.out.println(new A().super.x);
8 }
9 }
a) Não compila.
b) Compila e imprime 1.
c) Compila e imprime 2.
d) Compilaedáexception.
5) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{
2 void B() {
3 }
4 void B(String s ){
5 this();
6 this(s);
7 }
8 }
9 class A{
10 public static void main(String[] args){
11 Bb = new B();
12 }
13 }
a) Não compila.
b) Compilaedáexception.
c) Compilaenãoimprimenada.
d) Compilaeentraemloopinfinito.
6) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
317

## Página 323

9.5. Usesuperethisparaacessarobjetoseconstrutores CasadoCódigo
1 class B{
2 B() {
3 }
4 B(String s ){
5 this();
6 this(s);
7 }
8 }
9 class A{
10 public static void main(String[] args){
11 Bb = new B();
12 }
13 }
a) Não compila.
b) Compilaedáexception.
c) Compilaenãoimprimenada.
d) Compilaeentraemloopinfinito.
7) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{
2 B() {
3 }
4 B(String s ){
5 this();
6 }
7 }
8 class A{
9 public static void main(String[] args){
10 Bb = new B();
11 }
12 }
a) Não compila.
b) Compilaedáexception.
c) Compilaenãoimprimenada.
318

## Página 324

CasadoCódigo Capítulo9. Trabalhandocomherança
d) Compilaeentraemloopinfinito.
8) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{
2 B() {
3 }
4 B(String s ){
5 this();
6 }
7 }
8 class A{
9 public static void main(String[] args){
10 String s = null;
11 Bb = new B(s);
12 }
13 }
a) Não compila.
b) Compilaedáexception.
c) Compilaenãoimprimenada.
d) Compilaeentraemloopinfinito.
9) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{
2 int x() { return y();}
3 int y() { return 3; }
4 }
5 class C extends B {
6 C() {
7 this(x());
8 }
9 C(int i){
10 System.out.println(i);
11 }
12 int y() { return 2; }
319

## Página 325

9.5. Usesuperethisparaacessarobjetoseconstrutores CasadoCódigo
13 }
14 class A{
15 public static void main(String[] args){
16 new C();
17 }
18 }
a) Não compila.
b) Compilaeimprime‘2‘.
c) Compilaeimprime‘3‘.
10) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class B{
2 int x() { return y();}
3 int y() { return 3;}
4 }
5 class C extends B {
6 C() {
7 super();
8 z(x());
9 }
10 void z(int i){
11 System.out.println(i);
12 }
13 int y() { return 2; }
14 }
15 class A{
16 public static void main(String[] args){
17 new C();
18 }
19 }
a) Não compila.
b) Compilaeimprime‘2‘.
c) Compilaeimprime‘3‘.
320

## Página 326

CasadoCódigo Capítulo9. Trabalhandocomherança
9.6 Useclassesabstrataseinterfaces
Classesemétodospodemserabstratos.
U maclasseabstra tapodenãoternenh ummétodoabstra to:
// compila
abstract class SemMetodos {
}
Seumaclassetemummétodoqueéabstrato,eladeveserdeclaradacomo
abstrata,ounãocompilará.
// não compila, se tem método abstrato, tem que implementar
class ComMetodoAbstrato {
public abstract void executa();
}
Umaclasseabstratanãopodeserinstanciadadiretamente:
abstract class X{
}
public class Teste{
public static void main(String[] args){
Xx = new X();
}
}
Ac l a s s eTeste não compila! Classes abstratas não podem ser instanci-
adasdiretamente:
Teste.java:7: Xis abstract; cannot be instantiated
Xx = new X ();
^
1 error
Ummétodoabstratoéummétodosemcorpo,somentecomadefinição.
Umaclassequetemumoumaismétodosabstratosprecisaserdeclaradacomo
abstrata.
Nãoimportaseométodofoiescritodiretamenteoufoiherdado:
321

## Página 327

9.6. Useclassesabstrataseinterfaces CasadoCódigo
abstract class Veiculo {
public abstract void liga();
}
// compila pois implementou
class Moto extends Veiculo {
public void liga() {
}
}
// compila pois a classe é abstrata, com método herdado
// abstrato ainda
abstract class QuatroRodas extends Veiculo {
}
// não compila pois a classe não é abstrata,
// com método herdado abstrato ainda
class SemRodas extends Veiculo {
}
Um método abstrato tem de ser reescrito ou herdado pelas suas filhas
concretas.
Agoravejaoexemploaseguir:
abstract class Veiculo {
public abstract void liga();
}
class Moto extends Veiculo {
public void liga() {
}
}
O método liga foi implementado na classe filha, então ela pode ser
concreta. Bastapensarquemétodosabstratosherdadossão responsabilidades
herdadas: você não poderá ser um objeto concreto enquanto tiver respons-
abilidadesaseremtratadas.
322

## Página 328

CasadoCódigo Capítulo9. Trabalhandocomherança
Quandoherdamosdeumaclasseabstrataquepossuiummétodoabstrato,
temos que escolher: ou implementamos o método, ou somos abstratos tam-
bém epassamos adiantea responsabilidade. Note que a classe pode imple-
mentarométodoemesmoassimtambémserabstrata.
abstract class Veiculo {
public abstract void liga();
}
abstract class Moto extends Veiculo {
}
class MotoEspecial extends Moto {
public void liga() {
}
}
// compila: decidi implementar mas mesmo assim
// manter a classe abstrata
abstract class QuatroRodar extends Veiculo {
public void liga() {
}
}
Código de uma classe abstrata pode acessar o código da classe concreta,
umavezqueelesóseráexecutadoquandooobjetoforcriado:
abstract class X{
abstract void x() {
System.out.println(y());
}
abstract String y();
}
class Y extends X {
String y() {
return "codigo";
}
323

## Página 329

9.6. Useclassesabstrataseinterfaces CasadoCódigo
}
public class Teste {
public static void main(String[] args){
new X().x(); // imprime código
}
}
Interfaces
Uma interface declara métodos que deverão ser implementados pelas
classes concretas que queiram ser consideradas como tal. Por padrão, são
todosmétodospúblicoseabstratos.
interface Veiculo {
void ligar();
// public abstract! Você pode escrever, mas é por padrão
// isso.
public abstract int pegaMarcha();
}
Quando você implementa a interface em uma classe concreta, é preciso
implementartodososmétodos. Similarmente,aoherdarumaclasseabstrata,
a classe concreta deve implementar todos os métodos que não foram imple-
mentadosainda:
// compila, todos os métodos implementados
class Carro implements Veiculo {
public void ligar() {
}
public int pegaMarcha() {
return 0;
}
}
// não compila, onde está o pegaMarcha?
class Moto implements Veiculo {
public void ligar() {
}
}
// não compila, o método pegaMarcha definiu escopo default,
324

## Página 330

CasadoCódigo Capítulo9. Trabalhandocomherança
// quando deveria definir public
class Triciclo implements Veiculo {
public void ligar() {
}
int pegaMarcha() {
return 0;
}
}
Valemasmesmasregrasdequandovocêherdadeumaclasseabstrata: ou
vocêtemtodososmétodosreescritos,eaípodedeclará-lacomoconcreta,ou
entãovocêprecisadeclará-lacomoabstrata.
// compila, pois a classe éabstrata
abstract class Moto implements Veiculo {
public void ligar() {
}
}
Umaclassepodeimplementardiversasinterfaces:
abstract class MinhaClasse implements Serializable, Runnable {
}
Justamente por isso, a prova vê como um bom uso de interfaces quando
você quer herdar de dois lugares mas a herança de classes não permite. Para
a prova, essa razão é suficiente, mas na prática existe uma diferença grande
entrecomposição(herançadeinterfacesnãoenvolveherdarcomportamento
ev a r i á v e i sm e m b r o )eh e r d a rc o m p o rtamento e variáveis membro de uma
classe mãe. Como a implementação de uma interface nos obriga a escrever
todososmétodos,estamoscompondonossaclassedediversasinterfaces.
Lembre-sequeumainterfacepodeherdardeoutra,inclusivedediversas
interfaces:
interface A extends Runnable {}
interface B extends Serializable {}
interface C extends Runnable, Serializable {}
Notequeumainterfacenuncaimplementaoutrainterface:
325

## Página 331

9.6. Useclassesabstrataseinterfaces CasadoCódigo
interface A implements Runnable {} // não compila
Vocêpodedeclararvariáveisemumainterface,todaselasserão public
final static ,istoé,co nstan tes.
interface X{
int i =5 ;
// você até pode escrever public static final, mas é sempre
// assim
}
Umainterface,porsuavez,podeestenderoutrainterface,herdandosuas
responsabilidades e constantes. Uma interface pode estender mais de uma
interface!
interface X extends Runnable, Comparable {}
1) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 abstract class B{
2 void x() {
3 System.out.println(y());
4 }
5 abstract int y();
6 }
7 abstract class C extends B {
8 int y() { return 1; }
9 }
10 class D extends C {
11 int y() { return 2; }
12 }
13 class A{
14 public static void main(String [] args){
15 Dd =( D)( C) new D();
16 d.x();
17 }
18 }
a) Não compila.
326

## Página 332

CasadoCódigo Capítulo9. Trabalhandocomherança
b) Compilaeimprime‘1‘.
c) Compilaeimprime‘2‘.
d) Compilaerodacomexception.
2) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 abstract class B{
2 abstract void x() {
3 System.out.println(y());
4 }
5 abstract int y();
6 }
7 abstract class C extends B {
8 int y() { return 1; }
9 }
10 class D extends C {
11 int y() { return 2; }
12 }
13 class A{
14 public static void main(String[] args){
15 Dd =( D)( C) new D();
16 d.x();
17 }
18 }
a) Não compila.
b) Compilaeimprime‘1‘.
c) Compilaeimprime‘2‘.
d) Compilaerodacomexception.
3) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 abstract class B{
2 void x() {
3 System.out.println(y());
4 }
327

## Página 333

9.6. Useclassesabstrataseinterfaces CasadoCódigo
5 abstract int y();
6 }
7 abstract class C extends B {
8 abstract int y();
9 }
10 class D extends C {
11 int y() { return 1; }
12 }
13 class A{
14 public static void main(String[] args){
15 Dd =( D)( C) new D();
16 d.x();
17 }
18 }
a) Não compila.
b) Compilaeimprime‘1‘.
c) Compilaeimprime‘2‘.
d) Compilaerodacomexception.
4) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 abstract class B{
2 void x() {
3 System.out.println(y());
4 }
5 int y() {
6 return 2;
7 }
8 }
9 abstract class C extends B {
10 abstract int y();
11 }
12 class D extends C {
13 int y() { return 1; }
14 }
15 class A{
16 public static void main(String [] args){
328

## Página 334

CasadoCódigo Capítulo9. Trabalhandocomherança
17 Dd =( D)( C) new D();
18 d.x();
19 }
20 }
a) Não compila.
b) Compilaeimprime‘1‘.
c) Compilaeimprime‘2‘.
d) Compilaerodacomexception.
5) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 abstract class B{
2 void x() {
3 System.out.println(y());
4 }
5 final int y() {
6 return 2;
7 }
8 }
9 abstract class C extends B {
10 int y() {
11 return 3;
12 }
13 }
14 class D extends C {
15 int y() { return 1; }
16 }
17 class A{
18 public static void main(String[] args){
19 Dd =( D)( C) new D();
20 d.x();
21 }
22 }
a) Não compila.
b) Compilaeimprime‘1‘.
329

## Página 335

9.6. Useclassesabstrataseinterfaces CasadoCódigo
c) Compilaeimprime‘2‘.
d) Compilaerodacomexception.
6) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 abstract class B{
2 void x() {
3 System.out.println(y());
4 }
5 Object y() { return "a";}
6 }
7 abstract class C extends B {
8 abstract String y();
9 }
10 class D extends C {
11 String y() { return "b";}
12 }
13 class A{
14 public static void main(String[] args){
15 Dd =( D)( C) new D();
16 d.x();
17 }
18 }
a) Não compila.
b) Compila e imprime ‘a‘.
c) Compila e imprime ‘b‘.
d) Compilaerodacomexception.
330

## Página 336

Capítulo10
Lidandocomexceções
10.1 Diferencie entre exceções do tipo
checked,runtimeeerros
Durante a execução de uma aplicação, erros podem acontecer. A lin-
guagem Java oferece um mecanismo para que o programador possa definir
asprovidênciasapropriadasaseremtomadasnahoraemqueum errodeex-
ecuçãoocorrer.
Os erros de execução são classificados em algumas categorias. É funda-
mental que você seja capaz de, dado um erro de execução, determinar seu
tipo. Aclassificaçãodascategoriasdependeexclusivamentedahierarquiadas
classesquemodelamoserrosdeexecução.
A classe principal dessa hierarquia é a
Throwable. Qualquer erro de
execuçãoéumobjetodessaclasseoudeumaquederivadela.

## Página 337

10.1. Diferencieentreexceçõesdotipochecked,runtimeeerros CasadoCódigo
Comofilhasdiretasde Throwabletemos: Errore Exception.
Os Errors são erros de execução gerados por uma situação total-
mente anormal que não deveria ser prevista pela aplicação. Por exemplo,
um OutOfMemoryError é gerado quando a JVM não tem mais memória
RAMdisponívelparaoferecerparaasaplicações. Emgeral,essetipodeerro
nãoéresponsabilidadedasaplicaçõespoisquemcuidadogerenciamentode
memóriaéaJVM.
Poroutrolado,as
Exceptionssãoerrosdeexecuçãoquesãoderespon-
sabilidadedasaplicações,ouseja,sãoasaplicaçõesquedevemtratarouevitar
esses erros. Por exemplo, um
SQLException é gerado quando algum erro
ocorre na comunicação entre a aplicaçãoeob a n c od edados. Esse tipo de
errodevesertratadoouevitadopelaaplicação.
Por sua vez, as Exceptions são divididas em duas categorias: as
uncheckedsea scheckeds. As uncheckedssão exceptions que teoricamente
podem ser mais facilmente evitadas pelo próprio programador se ele codi-
ficardemaneiramaiscuidadosa. As checkedssãoexceptionsqueteoricamente
não são fáceis de evitar, de modo que a melhor abordagem é estar sempre
preparadoparaseuacontecimento.
As uncheckeds são definidas pelas classes que derivam de
RuntimeException, que por sua vez é filha direta de Exception.
A so u trasclassesnaárvo r edaExceptiondefinemascheckeds.
332

## Página 338

CasadoCódigo Capítulo10. Lidandocomexceções
Essasdiferençasnaoficamapenasnateoria. Ocompiladoriráverificarse
seuprogramapodelançaralgumacheckedexceptione,nestecaso,obrigá-loa
trataressaexceptiondealgumamaneira. Nocasodasexceptionsunchecked,
nãohánenhumaverificaçãoporpartedocompiladorpelotratamentoounão.
1) Dentreasclassesaseguirqualdelasnãoéchecked?
•
java.io.IOException
• java.sql.SQLException
• java.lang.Exception
• java.lang.IndexOutOfBoundsException
• java.io.FileNotFoundException
10.2 Descrevaoquesãoexceçõeseparaquesão
utilizadasemJava
Imagineasituaçãoemquetentamosacessarumaposiçãoemumarray:
public void fazAlgo(int[] idades){
System.out.println(idades[0]);
}
Oqueaconteceseoarrayenviadoparaométodoévazio? Seessecódigo
imprimissenuloouumnúmeropadrão,nessecaso,teríamossemprequenos
preocupar,comoem:
public void fazAlgo(int[] idades){
if(idades [0]==null) return;
// return para caso o Java devolva nulo ao acessar
// uma posição inválida
System.out.println(idades[0]);
}
333

## Página 339

10.2. DescrevaoquesãoexceçõeseparaquesãoutilizadasemJava CasadoCódigo
Pense como seria difícil tratar todas as situações possíveis quefogem do
padrãode comportamento que estamos desejando. Nesse caso, o comporta-
mentopadrão,aquiloqueacontece99%dasvezesequeesperamosqueacon-
teça é que a posição acessada dentro do array seja válido. Não queremos ter
queverificartodavezseovaloréválido,enãoqueremosentupirnossocódigo
comdiversos
ifsparadiversascondições. Asexceçõesàregra,as exceptions,
sãoaalternativaparaocontroledefluxo: emvezdeusarmos ifs paracon-
trolarofluxoquefogedopadrão,épossívelusaras exceptionsparaessepapel.
Veremosadiantecomotratarerros,comooacessoaposiçõesinválidas,tentar
acessarvariáveiscomvaloresinválidosetc.
Casoumaexceptionestoureesua stack tracesejaimpressa,teremosalgo
como:
Exception in thread "main"
java.lang.ArrayIndexOutOfBoundsException: 0
at SuaClasse.fazAlgo(SuaClasse.java:20)
at SuaClasse.main(SuaClasse.java:30)
Note como astack traceindica que método estava sendo invocado, em
qual linha do arquivo fonte está essa invocação, quem invocou este método
etc.
Oimportanteélembrarqueas exceptionspermitemqueisolemosotrata-
mento de um comportamento por blocos, separando o bloco de lógica de
nosso negócio do bloco de tratamentos de erros (sejam elesExceptions ou
Errors, como veremos adiante). O stack trace de uma
Exception também
ajudaaencontrarondeexatamenteoproblemaocorreueoqueestavasendo
executadonaquela Threadnaqueleinstante.
1) Escolha2opções.
Exceptionéummecanismopara...
• tratarentradadedadosdousuário.
• que você pode usar para determinar o que fazer quando algo ines-
peradoacontece.
• queaVMusaparafecharoprogramacasoalgoinesperadoaconteça.
334

## Página 340

CasadoCódigo Capítulo10. Lidandocomexceções
• controlarofluxodaaplicação.
• separarotratamentodeerrosdalógicaprincipal.
2) De que maneira a API de exceptions pode ajudar a melhorar o código de
seuprograma?
Escolha2opções:
• P ermi tindosepararotra tamen todeerr odalógicadop r ograma.
• P ermi tindotra taroerr onomesmopo n too ndeeleoco rr e.
• Permitindo estender as classes que já existem e criar novas excep-
tions.
• Disponibilizando várias classes com todas as exceptions possíveis
prontas.
• Aumentandoasegurançadaaplicaçãodisponibilizandooserrosnos
logs.
10.3 Crieumblocotry-catchedeterminecomo
exceções alteram o fluxo normal de um
programa
O programador pode definir um tratamento para qualquer tipo de erro de
execução. Antes de definir o tratamento, propriamente, é necessário deter-
m i n a rot r e c h od ec ó d i g oq u ep o d eg e r a ru me r r on ae x e c u ç ã o .I s s ot u d oé
fei toco moco mando
try-catch.
try {
// trecho que pode gerar um erro na execução.
} catch (Throwable t){ // pegando todos os possíveis erros de
//execução.
// tratamento para o possível erro de execução.
}
335

## Página 341

10.3. Crieumblocotry-catchedeterminecomoexceçõesalteramofluxonormaldeumprogramaCasadoCódigo
A sintaxe do try-catch tem um bloco para o programador definir o
trechodecódigoque podegerarumerrodeexecução. Esseblocoédetermi-
nadopelapalavra try. Oprogramadortambémpodedefinirquaistiposde
erroelequerpegarparatratar. Issoédeterminadopeloargumentodo catch.
Porfim,otratamentoédefinidopeloblocoqueécolocadoapósoargumento
do catch.
Durante a execução, se um erro acontecer, a JVM redireciona o fluxo de
execuçãodalinhadoblocodo tryquegerouoerroparaoblocodo catch.
Importante! Aslinhasdoblocodo tryabaixodaquelaquegerouoerronão
serãoexecutadas.
Fazer um catch em Throwable não é uma boa prática, pois todos os
errospossíveissãotratadospelaaplicação. Porém,os Errorsnãodeveriam
ser tratados pela aplicação, já que são de responsabilidade da JVM. Assim,
tambémnãoéboap rá ticadar
catchem Errors.
Modificando o argumento docatch, o programador define quais erros
devemserpegosparaseremtratados.
try {
// trecho que pode gerar um erro na execução.
} catch (Exception e){ // pegando todas as exceptions.
// tratamento para o possível erro de execução.
}
Para a prova, é fundamental saber quando o programador pode ou não
p o d eu s a rotry-catch. A única restrição de uso do try-catch en-
volve as checked exceptions. Qual é a regra? O programador só pode usar
try-catch em uma checked exception se o código do bloco dotry pode
realmentelançaracheckedexceptionemquestão.
try {
System.out.println("não acontece SQLException" );
} catch(SQLException e){ // pegando SQLException.
// tratamento.
}
Essecódigo nãocompilapoisotrechoenvolvidonoblocodo trynunca
geraria a checked SQLException. O compilador avisa com um erro de
336

## Página 342

CasadoCódigo Capítulo10. Lidandocomexceções
“unreachable code”. Já o exemplo a seguir compila, pois pode ocorrer um
FileNotFoundException:
try {
new java.io.FileInputStream( "a.txt");
} catch(java.io.FileNotFoundException e){
// tratamento.
}
Ocódigoaseguirnãotemnenhumproblema,poisoprogramadorpode
usaro try-catchemqualquersituaçãoparaoserrosdeexecuçãoquenão
sãocheckedexceptions.
try {
System.out.println("Ok");
} catch (RuntimeException e){ // pegando RuntimeException
// (unckecked).
// tratamento.
}
Podemospegartudo,exceptionseerros:
try {
System.out.println("Ok");
} catch (Throwable e){
// tratamento
}
Quando a exception é pega, o fluxo do programa é sair do blocotry
ee n t r a rn ob l o c ocatch, portanto, o código a seguir imprimepeguei e
continuando normal :
String nome = null;
try {
nome.toLowerCase();
System.out.println("segunda linha do try");
} catch(NullPointerException ex ){
System.out.println("peguei");
}
System.out.println("continuando normal");
337

## Página 343

10.3. Crieumblocotry-catchedeterminecomoexceçõesalteramofluxonormaldeumprogramaCasadoCódigo
Mas, se a exception que ocorre não é a que foi definida no catch, a
chamadadométodoparaevolta,jogandoaexceptioncomosenãohouvesse
um try/catch. Ocenárioaseguirdemonstraessasituaçãoenãoimprime
nada:
String nome = null;
try {
nome.toLowerCase();
System.out.println("segunda linha do try" );
} catch(IndexOutOfBoundsException ex ){
System.out.println("peguei");
}
System.out.println("continuando normal" );
Lembre-se sempre do polimorfismo, portanto, pegarIOException é
o mesmo que pegar todas as filhas deIOException também. O código a
seguir trata o caso de o arquivo não existir além de todas as outras filhas de
IOException:
try {
new java.io.FileInputStream( "a.txt");
} catch(java.io.IOException e){
// tratamento.
}
Blocofinally
Tem coisas que não podemos deixar de fazer em hipótese alguma. Seja
nosucessoounofracasso,temosobrigaçãodecumprircomalgumastarefas.
Imagine um método que conecta com um banco de dados. Não im-
porta o que aconteça, no fim desse método a conexão deveria ser fechada.
Durante a comunicação com o banco de dados, há o risco de ocorrer uma
SQLException.
void metodo(){
try {
abreConexao ();
fazConsultas();
fechaConexao();
338

## Página 344

CasadoCódigo Capítulo10. Lidandocomexceções
} catch (SQLException e){
// tratamento
}
}
Nesse código, há um grande problema: se umSQLException ocorrer
duranteasconsultas,aconexãocomobancodedadosnãoseráfechada. Para
tentar resolver esse problema, o bloco docatch poderia invocar o método
fechaConexao(). Então, se acontecesse umSQLException o bloco do
catchseriaexecutadoe,consequentemente,aconexãoseriafechada.
Masaindanãosolucionamosoproblema,poisoutrotipodeerropoderia
acontecer nas consultas. Por exemplo, umaNullPointerException que
não está sendo tratada. Para resolver o problema de fechar a conexão, um
outro recurso do Java será utilizado, o blocofinally. Esse bloco é sempre
executado,tantonosucessoquantonofracassoporqualquertipodeerro.
void metodo(){
try {
abreConexao ();
fazConsultas(); // Não precisa mais fechar a conexao
// aqui.
} catch(SQLException e){
// tratamento
} finally {
fechaConexao(); // fechando a conexao no sucesso ou no
// fracasso.
}
}
Para melhor entender o fluxo dotry-cacth com o finally,v e j ao
próximoexemplo.
class A{
void metodo() {
try{
//A
//B
}catch(SQLException e){
339

## Página 345

10.3. Crieumblocotry-catchedeterminecomoexceçõesalteramofluxonormaldeumprogramaCasadoCódigo
//C
}finally{
//D
}
//E
}
}
• Em uma execução normal, sem erros nem exceções, ele executariaA,
B, D, E.
•C o mSQLExceptionem A,eleexecutaria C, D, E.
•C o m NullPointerException em A, ele executaria apenas D e
sairia.
•S e A fosse um System.exit(0);, ele apenas executaA e encerra o
programa.
• Seocorresseumerro A,executariaapenas D(dependendodoerro).
Uma outra maneira um pouco menos convencional de usar ofinally
ésemobloco catch,comonoexemploaseguir.
class A{
void metodo() {
try {
System.out.println("imprime algo" );
} finally {
// sempre permite fechar
}
}
}
1) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 String nome ;
340

## Página 346

CasadoCódigo Capítulo10. Lidandocomexceções
4 try {
5 nome.toLowerCase();
6 System.out.println("a");
7 } catch(NullPointerException ex ){
8 System.out.println("b");
9 }
10 System.out.println("c");
11 }
12 }
a) Não compila.
b) Co m p ilae,aor odar ,im p rime“ abc ” .
c) Co m p ilae,aor odar ,im p rime“bc ” .
d) Co m p ilae,aor odar ,im p rime“ a ” .
e) Co m p ilae,aor odar ,im p rime“b ” .
2) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 String nome = null;
4 try {
5 nome.toLowerCase();
6 System.out.println("a");
7 } catch(NullPointerException ex ){
8 System.out.println("b");
9 }
10 System.out.println("c");
11 }
12 }
a) Nãocompila..
b) Co m p ilae,aor odar ,im p rime“ abc ” .
c) Co m p ilae,aor odar ,im p rime“bc ” .
d) Co m p ilae,aor odar ,im p rime“ a ” .
e) Co m p ilae,aor odar ,im p rime“b ” .
341

## Página 347

10.4. Invoqueummétodoquejogaumaexceção CasadoCódigo
3) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 public static void main(String[] args){
3 String nome ;
4 try {
5 nome.toLowerCase();
6 System.out.println("a");
7 } catch(NullPointerException ex ){
8 System.out.println("b");
9 } finally {
10 System.out.println("c");
11 }
12 System.out.println("d");
13 }
14 }
a) Não compila.
b) Co m p ilae,aor odar ,im p rime“ abcd ” .
c) Co m p ilae,aor odar ,im p rime“bcd ” .
d) Co m p ilae,aor odar ,im p rime“ ac ” .
e) Co m p ilae,aor odar ,im p rime“bc ” .
f) Co m p ilae,aor odar ,im p rime“ ad ” .
g) Co m p ilae,aor odar ,im p rime“bd ” .
10.4 Invoqueummétodoquejogaumaexceção
Eventualmente, um método qualquer não tem condição de tratar um deter-
minadoerrodeexecução. Nessecaso,essemétodopodedeixarpassaroerro
paraop r ó ximométodonap ilhadeexecução .
Para deixar passar qualquer erro de execução que não seja uma checked
exception,émuitosimples: bastanãofazernada.
class Teste {
342

## Página 348

CasadoCódigo Capítulo10. Lidandocomexceções
void primeiro(){
System.out.println("primeiro antes");
this.segundo();
System.out.println("primeiro depois" );
}
void segundo() {
String s = null;
System.out.println("segundo antes" );
s.length();
System.out.println("segundo depois" );
}
}
O segundo método declara uma variável não primitiva e a inicializa
com null. Logo em seguida, ele utiliza o operador . em uma refer-
ência que sabemos estar nula. Nesse ponto, na hora da execução, um
NullPointerException é gerado. Perceba que não hátry-catch no
segundo método, então ele não está pegando e tratando o erro, mas sim
deixando-o passar. O primeiro método não define otry-catch, ou seja,
também deixa passar o NullPointerException. O resultado é a im-
pressãode primeiro antes , segundo antes .
Agora, para deixar passar uma checked exception, o método é obrigado
a deixar explícito (avisado) que pretende deixar passar. Na assinatura do
método, o programador pode deixar avisado que pretende deixar passar de-
terminadoserrosdeexecução. Issoéfeitoatravésdapalavra-chave
throws.
class Teste {
void primeiro(){
try {
System.out.println("primeiro antes");
this.segundo();
System.out.println("primeiro depois" );
} catch(IOException e){
// tratamento.
System.out.println("primeiro catch");
}
343

## Página 349

10.4. Invoqueummétodoquejogaumaexceção CasadoCódigo
System.out.println("primeiro fim" );
}
void segundo() throws IOException {
System.out.println("segundo antes");
System.in.read(); // pode lançar IOException
System.out.println("segundo depois" );
}
}
O segundo método invoca oread() no System.in. Essa invocação
p o d eg e r a ru mIOException, de modo que o segundo método tem duas
alternativas: ou pega e trata o possível erro ou o deixa passar. Para deixar
passar, o comandothrows deve ser utilizado na sua assinatura do segundo
método. Issoindicaráqueum IOExceptionpodeserlançado.
Dessaforma,oprimeirométodoqueinvocaosegundopodereceberuma
IOException. Então,eletambémtemduasescolhas: oupegaetratausando
try-catch, ou deixa passar usando othrows.Or e s u l t a d oéai m p r e s s ã o
de primeiro antes , segundo antes , primeiro catch e primeiro
fim.
Gerandoumerrodeexecução
Qualquermétodo,aoidentificarumasituaçãoerrada,podecriarumerro
de execução e lançar para quem o chamou. Vale lembrar que os erros de ex-
ecução são representados por objetos criados a partir de alguma classe da
hierarquiadaclasse
Throwable,logo,bastaométodoinstanciarumobjeto
dequalquerumadessasclassesedepoislançá-lo.
Seoerronãoforumacheckedexception,bastacriaroobjetoeutilizaro
comando throw para lançá-lo na pilha de execução (não confunda com o
throws):
class Teste {
void primeiro(){
try {
this.segundo();
344

## Página 350

CasadoCódigo Capítulo10. Lidandocomexceções
} catch (RuntimeException e){
// tratamento.
}
}
void segundo() {
throw new RuntimeException();
}
}
Se o erro for uma checked exception, é necessário também declarar na
assinaturadométodoocomando throws:
class Teste {
void primeiro(){
try {
this.segundo();
} catch(Exception e){
// tratamento.
}
}
void segundo() throws Exception {
throw new Exception();
}
}
Podemosaindacriarnossasprópriasexceções,bastandocriarumaclasse
queentrenahierarquiade Throwable.
class MinhaException extends Exception{}
Emqualquerlugardocódigo,éopcionalousodo trye catchdeuma
unchecked exception para compilar o código. Em uma checked exception, é
obrigatórioousodo try/catchou throws.
O exemplo a seguir mostra uma unchecked exception sendo ignorada e
oerrovazando,enadaseráimpresso:
345

## Página 351

10.4. Invoqueummétodoquejogaumaexceção CasadoCódigo
public class Teste {
public static void main(String[] args){
metodo();
System.out.println("Apos a invocacao do metodo" );
}
private static void metodo() {
int[] i= newint [10];
System.out.println(i[15]);
System.out.println("Apos a exception");
}
}
Ao pegarmos a exception, será impresso também “Apos a invocacao do
metodo ”umavezquea pósoca tch,ofl uxovol taaono rmall:
public class Teste {
public static void main(String[] args){
try {
metodo();
} catch(RuntimeException ex){
System.out.println("Exception pega");
}
System.out.println("Apos a invocacao do metodo" );
}
private static void metodo() {
int[] i= newint [10];
System.out.println(i[15]);
System.out.println("Apos a exception");
}
}
Podemos ter também múltiplas expressões do tipocatch. Nesse caso,
será invocada somente a cláusula adequada, e não as outras. No código a
346

## Página 352

CasadoCódigo Capítulo10. Lidandocomexceções
seguir, se ometodo2 jogar uma ArrayIndexOutOfBoundsException,
seráimpresso runtime:
void metodo1() {
try {
metodo2();
} catch(IOException ex){
System.out.println("io");
} catch(RuntimeException ex){
System.out.println("runtime");
} catch(Exception ex){
System.out.println("exception qualquer" );
}
}
Eaordemfazdiferença? Sim,oJavaprocuraoprimeiro catchquepode
trabalhara Exceptionadequada.
Repare que RuntimeException herda de Exception e, portanto,
devevirantesdamesmanaordemde catches.
Casoelaviessedepois,elanuncaseriainvocada,poisoJavaverificariaque
toda RuntimeExceptioné Exceptione Exceptionteriatratamentode
preferência(porsuaordem). Oexemploaseguirnãocompilaporestemotivo:
void metodo1() {
try {
metodo2();
} catch(IOException ex){
System.out.println("io");
} catch(Exception ex){
System.out.println("exception qualquer" );
} catch(RuntimeException ex){
// não compila pois jamais será executado
System.out.println("runtime");
}
}
Cuidadotambémcomexceptionsnosinicializadores:
class AcessoAoArquivo {
// não compila, pois ao instanciar, pode dar IOException,
347

## Página 353

10.4. Invoqueummétodoquejogaumaexceção CasadoCódigo
// mas o construtor não fala nada
private InputStream is = new FileInputStream("entrada.txt");
}
Nessescasos,precisamosdizernoconstrutorquea Exceptionpodeser
jogada:
class AcessoAoArquivo {
private InputStream is = new FileInputStream("entrada.txt");
AcessoAoArquivo() throws IOException{
// estou avisando os clientes dessa classe
// que ao instanciar pode dar essa exception
// e agora compila
}
}
1) Qualclassepodemoscolocarnocódigoaseguirparaqueelecompile?
1 import java.io.*;
2 class X{
3 InputStream y() throws NOME_AQUI {
4 return new FileInputStream("a.txt");
5 }
6 void z() throws NOME_AQUI{
7 InputStream is = y();
8 is.close();
9 }
10 }
* java.io.IOException * java.sql.SQLException *
java.lang.Exception* java.lang.IndexOutOfBoundsException
* java.io.FileNotFoundException
2) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 void m2() {
3 System.out.println("e");
348

## Página 354

CasadoCódigo Capítulo10. Lidandocomexceções
4 int[][]x = new int[15][20];
5 System.out.println("f");
6 }
7 void m() {
8 System.out.println("c");
9 m2();
10 System.out.println("d");
11 }
12 public static void main(String[] args){
13 System.out.println("a");
14 new A().m();
15 System.out.println("b");
16 }
17 }
a) Não compila.
b) Compila e imprimeacefdb.
c) Compila e imprimeaceejogauma Exception.
d) Compila e imprimeacedbejogauma Exception.
e) Compila e imprimeace,jogauma Exceptioneim p rimedb.
3) Escolhaaopçãoadequadaaotentarcompilarerodaroarquivoaseguir:
1 class A{
2 void m2() {
3 System.out.println("e");
4 int[] x = new int [15];
5 x[20] = 13;
6 System.out.println("f");
7 }
8 void m() {
9 System.out.println("c");
10 m2();
11 System.out.println("d");
12 }
13 public static void main(String [] args){
14 System.out.println("a");
349

## Página 355

10.4. Invoqueummétodoquejogaumaexceção CasadoCódigo
15 new A().m();
16 System.out.println("b");
17 }
18 }
a) Não compila.
b) Compila e imprimeacefdb.
c) Compila e imprimeaceejogauma Exception.
d) Compila e imprimeacedbejogauma Exception.
e) Compila e imprimeace,jogauma Exceptioneim p rimedb.
4) Escolha a opção adequada ao tentar compilar e rodar o arquivo a seguir,
semqueoarquivoexista?
1 class A{
2 void m2() {
3 System.out.println("e");
4 new java.io.FileInputStream( "a.txt" );
5 System.out.println("f");
6 }
7 void m() {
8 System.out.println("c");
9 m2();
10 System.out.println("d");
11 }
12 public static void main(String[] args){
13 System.out.println("a");
14 new A().m();
15 System.out.println("b");
16 }
17 }
a) Não compila.
b) Compila e imprimeacefdb.
c) Compila e imprimeaceejogauma Exception.
d) Compila e imprimeacedbejogauma Exception.
350

## Página 356

CasadoCódigo Capítulo10. Lidandocomexceções
e) Compila e imprimeace,jogauma Exceptioneim p rimedb.
5) Escolha a opção adequada ao tentar compilar e rodar o arquivo a seguir,
semqueoarquivoexista?
1 class A{
2 void m2() throws java.io.FileNotFoundException {
3 System.out.println("e");
4 new java.io.FileInputStream( "a.txt");
5 System.out.println("f");
6 }
7 void m() throws java.io.IOException {
8 System.out.println("c");
9 m2();
10 System.out.println("d");
11 }
12 public static void main(String[] args)
13 throws java.io.FileNotFoundException {
14 System.out.println("a");
15 new A().m();
16 System.out.println("b");
17 }
18 }
a) Não compila.
b) Compila e imprimeacefdb.
c) Compila e imprimeaceejogauma Exception.
d) Compila e imprimeacedbejogauma Exception.
e) Compila e imprimeace,jogauma Exceptioneim p rimedb.
6) Escolha a opção adequada ao tentar compilar e rodar o arquivo a seguir,
semqueoarquivoexista?
1 class A{
2 void m2() throws java.io.FileNotFoundException {
3 System.out.println("e");
4 new java.io.FileInputStream( "a.txt");
351

## Página 357

10.4. Invoqueummétodoquejogaumaexceção CasadoCódigo
5 System.out.println("f");
6 }
7 void m() throws java .io.FileNotFoundException {
8 System.out.println("c");
9 m2();
10 System.out.println("d");
11 }
12 public static void main(String[] args) throws
13 java.io.IOException {
14 System.out.println("a");
15 new A().m();
16 System.out.println("b");
17 }
18 }
a) Não compila.
b) Compila e imprimeacefdb.
c) Compila e imprimeaceejogauma Exception.
d) Compila e imprimeacedbejogauma Exception.
e) Compila e imprimeace,jogauma Exceptioneim p rimedb.
7) Escolha a opção adequada ao tentar compilar e rodar o arquivo a seguir,
semqueoarquivoexista?
1 class A{
2 void m2() throws java.io.FileNotFoundException {
3 System.out.println("e");
4 new java.io.FileInputStream( "a.txt");
5 System.out.println("f");
6 }
7 void m() throws java .io.FileNotFoundException {
8 System.out.println("c");
9 try {
10 m2();
11 } catch(java.io.FileNotFoundException ex){
12 }
13 System.out.println("d");
352

## Página 358

CasadoCódigo Capítulo10. Lidandocomexceções
14 }
15 public static void main(String[] args) throws
16 java.io.IOException {
17 System.out.println("a");
18 new A().m();
19 System.out.println("b");
20 }
21 }
a) Não compila.
b) Compila e imprimeacefdb.
c) Compila e imprimeaceejogauma Exception.
d) Compila e imprimeacedbejogauma Exception.
e) Compila e imprimeacedb.
f) Compila e imprimeace,jogauma Exceptioneim p rimedb.
8) Escolha a opção adequada ao tentar compilar e rodar o arquivo a seguir,
semqueoarquivoexista?
1 class MyException extends RuntimeException {
2
3 }
4 class A{
5 void m2() throws java.io.FileNotFoundException {
6 System.out.println("e");
7 new MyException();
8 System.out.println("f");
9 }
10 void m() throws java.io.FileNotFoundException {
11 System.out.println("c");
12 try {
13 m2();
14 } catch(java.io.FileNotFoundException ex){
15 }
16 System.out.println("d");
17 }
18 public static void main(String [] args) throws
353

## Página 359

10.4. Invoqueummétodoquejogaumaexceção CasadoCódigo
19 java.io.IOException {
20 System.out.println("a");
21 new A().m();
22 System.out.println("b");
23 }
24 }
a) Não compila.
b) Compila e imprimeacefdb.
c) Compila e imprimeaceejogauma Exception.
d) Compila e imprimeacedbejogauma Exception.
e) Compila e imprimeace,jogauma Exceptioneim p rimedb.
9) Escolha a opção adequada ao tentar compilar e rodar o arquivo a seguir,
semqueoarquivoexista?
1 class MyException extends RuntimeException {
2
3 }
4 class A{
5 void m2() throws java.io.FileNotFoundException {
6 System.out.println("e");
7 throws new MyException();
8 System.out.println("f");
9 }
10 void m() throws java .io.FileNotFoundException {
11 System.out.println("c");
12 try {
13 m2();
14 } catch(java.io.FileNotFoundException ex){
15 }
16 System.out.println("d");
17 }
18 public static void main(String[] args) throws
19 java.io.IOException {
20 System.out.println("a");
21 new A().m();
354

## Página 360

CasadoCódigo Capítulo10. Lidandocomexceções
22 System.out.println("b");
23 }
24 }
a) Não compila.
b) Compila e imprimeacefdb.
c) Compila e imprimeaceejogauma Exception.
d) Compila e imprimeacedbejogauma Exception.
e) Compila e imprimeace,jogauma Exceptioneim p rimedb.
10) Escolha a opção adequada ao tentar compilar e rodar o arquivo a seguir,
semqueoarquivoexista?
1 class MyException extends RuntimeException {
2
3 }
4 class A{
5 void m2() throws java.io.FileNotFoundException {
6 System.out.println("e");
7 boolean sim = true;
8 if(sim) throws new MyException();
9 System.out.println("f");
10 }
11 void m() throws java.io.FileNotFoundException {
12 System.out.println("c");
13 try {
14 m2();
15 } catch(java.io.FileNotFoundException ex){
16 }
17 System.out.println("d");
18 }
19 public static void main(String[] args) throws
20 java.io.IOException {
21 System.out.println("a");
22 new A().m();
23 System.out.println("b");
24 }
25 }
355

## Página 361

10.4. Invoqueummétodoquejogaumaexceção CasadoCódigo
a) Não compila.
b) Compila e imprimeacefdb.
c) Compila e imprimeaceejogauma Exception.
d) Compila e imprimeacedbejogauma Exception.
e) Compila e imprimeace,jogauma Exceptioneim p rimedb.
11) Escolha a opção adequada ao tentar compilar e rodar o arquivo a seguir,
semqueoarquivoexista?
1 class MyException extends RuntimeException {
2
3 }
4 class A{
5 void m2() throws java.io.FileNotFoundException {
6 System.out.println("e");
7 boolean sim = true;
8 if(sim) throw new MyException();
9 System.out.println("f");
10 }
11 void m() throws java .io.FileNotFoundException {
12 System.out.println("c");
13 try {
14 m2();
15 } catch(java.io.FileNotFoundException ex){
16 }
17 System.out.println("d");
18 }
19 public static void main(String[] args) throws
20 java.io.IOException {
21 System.out.println("a");
22 new A().m();
23 System.out.println("b");
24 }
25 }
a) Não compila.
b) Compila e imprimeacefdb.
356

## Página 362

CasadoCódigo Capítulo10. Lidandocomexceções
c) Compila e imprimeaceejogauma Exception.
d) Compila e imprimeacedbejogauma Exception.
e) Compila e imprimeace,jogauma Exceptioneim p rimedb.
10.5 Reconheca classes de exceções comuns e
suascategorias
Paraaprova,énecessárioconheceralgumasexceptionsclássicasdoJava. Na
sequência,vamosconheceressasexceptionseentenderemquesituaçõeselas
ocorrem.
ArrayIndexOutOfBoundsExceptioneIndexOutOfBoundsExcep-
tion
Um ArrayIndexOutOfBoundsException ocorre quando se tenta
acessarumaposiçãoquenãoexisteemumarray.
class Teste {
public static void main(String [] args){
int[] array = new int [10];
array[10] = 10; // Aqui ocorre
// ArrayIndexOutOfBoundsException.
}
}
Da mesma maneira, quando tentamos acessar uma posição
não existente em uma lista , a exception é diferente, no caso
IndexOutOfBoundsException:
class Teste {
public static void main(String [] args){
ArrayList<String> lista = new ArrayList<String>();
//Aqui ocorre IndexOutOfBoundsException
String valor = lista.get(2);
}
}
357

## Página 363

10.5. Reconhecaclassesdeexceçõescomunsesuascategorias CasadoCódigo
NullPointerException
Toda vez que o operador . é utilizado em uma referência nula, um
NullPointerExceptionélançado.
class Teste {
public static void main(String[] args){
String s = null;
s.length(); // Aqui ocorre uma NullPointerException
}
}
ClassCastException
Quando é feito um casting em uma referência para um tipo incom-
patívelcomoobjetoqueestánamemóriaemtempodeexecução,ocorreum
ClassCastException.
class Teste {
public static void main(String[] args){
Object o = "SCJP"; // String
Integer i =( Integer)o ; // Aqui ocorre
// ClassCastException.
}
}
NumberFormatException
U mproblemacom umqueoprogramadorenfren tanodiaadiaéterque
“transformar” texto em números. A API do Java oferece diversos métodos
para tal tarefa. Porém, em alguns casos não é possível “parsear” o texto, pois
elepodeco n tercaracter esinco rr etos.
class Teste {
public static void main(String[] args){
String s = "ABCD1";
// Aqui ocorre um NumberFormatException.
int i = Integer.parseInt(s);
358

## Página 364

CasadoCódigo Capítulo10. Lidandocomexceções
}
}
IllegalArgumentException
Qualquermétododeveverificarseosvalorespassadosnosseusparâmet-
ros são válidos. Se um método constata que os parâmetros estão in-
válidos, ele deve informar quem o invocou que há problemas nos val-
ores passados na invocação. Para isso, é aconselhado que o método lance
IllegalArgumentException.
class Teste {
public static void main(String[] args){
try {
divideEImprime(5,0);
} catch (IllegalArgumentException e ){
// tratamento.
}
}
public static void divideEImprime(int i, int j){
if(j == 0) { // Evita dividir por zero.
throw new IllegalArgumentException();
}
System.out.println(i/j);
}
}
IllegalStateException
Suponhaqueumapessoapossafazertrêscoisas: dormir,acordareandar.
Paraandar,apessoaprecisaestaracordada. Aclasse Pessoamodelaocom-
portamentodeumapessoa. Elacontémumatributo booleanqueindicase
ap e s s o ae s t áa c o r d a d ao ud o r m i n d oeu mm é t o d op a r ac a d ac o i s aq u eu m a
pessoafaz( dormir(), acordar()e andar()).
O método andar() não pode ser invocado enquanto a pessoa está
dormindo. Mas, se for, ele deve lançar um erro de execução. A bib-
lioteca do Java já tem uma classe pronta para essa situação, a classe é a
359

## Página 365

10.5. Reconhecaclassesdeexceçõescomunsesuascategorias CasadoCódigo
IllegalStateException. Ela significa que o estado atual do objeto não
permi tequeométodosejaexecu tado .
class Pessoa {
boolean dormindo = false;
void dormir() {
this.dormindo = true;
System.out.println("dormindo...");
}
void acordar() {
this.dormindo = false;
System.out.println("acordando...");
}
void andar() {
if(this.dormindo) { // Só pode andar acordado.
thrownew IllegalStateException( "Deveria estar
acordado!");
}
System.out.println("andando...");
}
}
ExceptionInInitializerError
Nomomentoemqueamáquinavirtualédisparada,elanãocarregatodo
o conteúdo doclasspath, em outras palavras, ela não carrega em memória
todasasclassesreferenciadaspelasuaaplicação.
Umaclasseécarregadanomomentodasuaprimeirautilização. Issosedá
quandoalgummétodoestáticoouatributoestáticosãoacessadosouquando
umob jetoécriadoapartirdaclasseemquestão .
N oc a r r e g a m e n t od eu m ac l a s s e ,aJ V Mp o d ee x e c u t a ru mt r e c h od e
códigodefinidopeloprogramador. Essetrechodeveficarnoqueé chamado
blocoestático.
class A{
static {
360

## Página 366

CasadoCódigo Capítulo10. Lidandocomexceções
// trecho a ser executado no carregamento da classe.
}
}
É totalmente possível que algum erro de execução seja gerado no bloco
estático. Se isso acontecer, a JVM vai “embrulhar” esse erro em um
ExceptionInInitializerErroredispará-lo.
Esseerropodesergeradotambémnainicializaçãodeumatributoestático
sealgumproblemaocorrer. Exemplo:
class A{
static {
if(true)
throw new RuntimeException("nao vou deixar nao...");
}
}
public class Teste {
public static void main(String[] args){
new A();
}
}
Geraoerrodeinicialização:
Exception in thread "main" java.lang.ExceptionInInitializerError
at Teste .main(Teste.java:11)
Caused by: java.lang.RuntimeException: nao vou deixar nao...
at A.<clinit>(Teste.java:4)
... 1 more
class P{
static int a = Integer.parseInt("a");
}
StackOverflowError
TodososmétodosinvocadospeloprogramaJavasãoempilhadosna Pilha
deExecução . Essapilhatemumlimite,ouseja,elapodeestourar:
361

## Página 367

10.5. Reconhecaclassesdeexceçõescomunsesuascategorias CasadoCódigo
class Teste {
public static void main(String[] args){
metodoSemFim();
}
static void metodoSemFim() {
metodoSemFim();
}
}
Repareque,nesseexemplo,o metodoSemFim() chamaelemesmo(re-
cursão). Dojeitoqueestá,osmétodosserãoempilhadoseternamenteeapilha
deexecuçãovaiestourar.
NoClassDefFoundError
Na etapa de compilação, todas as classes referenciadas no código-fonte
precisam estar noclasspath. Na etapa de execução também. O que será que
acontece se uma classe está noclasspathna compilação mas não está na exe-
cução? Quandoissoacontecerserágeradoum NoClassDefFoundError.
Para gerá-lo, podemos criar um arquivo com duas classes onde uma ref-
erenciaaoutra:
class OutraClasse {
}
class Teste {
public static void main(String[] args){
new OutraClasse();
}
}
Compilamos o arquivo, gerando dois arquivos.class.A ía p a g a m o so
arquivo OutraClasse.class.P r o n t o ,oJ a v an ã os e r ác a p a zd ee n c o n t r a r
aclasse,dandoumerr o , NoClassDefFoundError.
362

## Página 368

CasadoCódigo Capítulo10. Lidandocomexceções
OutOfMemoryError
Durante a execução de nosso código, o Java vai gerenciando e limpando
a memória usada por nosso programa automaticamente, usando ogarbage
collector(GC).OGCvairemoverdamemóriatodasasreferênciasdeobjetos
quenãosãomaisutilizados,liberandooespaçoparanovosobjetos. Masoque
acontece quando criamos muito objetos, e não os liberamos? Nesse cenário,
oGCnãovaiconseguirliberarmemória,eeventualmenteamemórialivreirá
acabar,ocasionandoum
OutOfMemoryError.
Ocódigoparafazerumerrodogêneroésimples,bastainstanciarinfinitos
objetos,sempermitirqueogarbagecollectorjogue-osfora. Fazemosissocom
Stringsparaqueoerr oaco n teçalogo:
void metodo() {
ArrayList< String> objetos = new ArrayList<String>();
String atual = "";
while(true ){
atual += " ficou maior" ;
objetos.add(atual);
}
}
1) Escolha a opção adequada que indica oThrowable que ocorrerá no
códigoaseguir:
1 class A{
2 public static void main(String[] args){
3 main(args);
4 }
5 }
a) IndexOutOfBoundsException
b) ArrayIndexOutOfBoundsException
c) NullPointerException
d) OutOfMemoryError
e) StackOverflowError
363

## Página 369

10.5. Reconhecaclassesdeexceçõescomunsesuascategorias CasadoCódigo
f) ExceptionInInitializationError
2) Escolha a opção adequada que indica oThrowable que ocorrerá no
códigoaseguir:
1 import java.util.*;
2 class A{
3 public static void main(String[] args){
4 ArrayList<String> strings = new ArrayList<String>();
5 for(int i=0;i<10;i++)
6 for(int j=0;j <10;i++)
7 strings.add("string " + i + "" + j);
8 System.out.println(strings.get(99999));
9 }
10 }
a) IndexOutOfBoundsException
b) ArrayIndexOutOfBoundsException
c) NullPointerException
d) OutOfMemoryError
e) StackOverflowError
f) ExceptionInInitializationError
364

## Página 370

Capítulo11
Boaprova
Agora que você acabou todo o livro, está na hora de revisar os pontos em
que ficou com dúvida. Refaça os exercícios para reforçar o conteúdo e faça
diversossimuladoscomooscitadosnocomeçodolivro.
Para efetuar a prova, primeiro compre o voucher no site da Oracle.
Busque no site dela pelo código da prova que deseja fazer, a Java SE 7 Pro-
grammerI(1Z0-803),adicioneamesmaaocarrinhoeefetueacompra.
Hojeopagamentoéfeitoviaboletoenviadoporemail,tomecuidadopois
elepodecairemsuacaixadespam,etomeaindamaiscuidadoparanãopagar
umboletodespam. DepoisdeconfirmadoorecebimentoporpartedaOracle
vocêreceberáumcódigodeconfirmaçãocomoqualserácapazdeagendara
da taelocaldesuap r o va.
Lembre-se de reler os pontos que tem mais dificuldade no dia que ante-
cedeaprova.

## Página 371

CasadoCódigo
Maisumavez,boaprova. Desejoquetodoesseprocessotenhaabertosua
mente sobre como a linguagem Java funciona, seus limites e suas caracterís-
ticasgerais.
Depoisdessacertificação,quevenhaapróxima,queexigeaindamaiscon-
hecimentodalinguagemedeAPIsfundamentaisdamesma.
366

## Página 372

Capítulo12
RespostasdosExercícios
3.1 -Exercícios
1. Arespostacertaé(c). Avariável ideclaradano forsóévisíveldentro
do for.
2. A resposta certa é (c), a variável x declarada como parâmetro do
método main efetua um shadowing. Nesse instante, ao dizermosx
= 200 , tentamos atribuir umint au ma r r a yd eString,e r r od e
compilação.
3. A resposta certa é (d). Isso porque o acesso à variável estática pode
ser feito através da instância da classe ou diretamente caso seja uma
variávelestáticasendoacessadaporummétodoestático.

## Página 373

CasadoCódigo
3.2-Exercícios
1. A resposta certa é (a). O arquivo não compila pois não podemos ter
um importapósadefiniçãodeumaclasse.
2. Arespostacertaé(e). Ocódigocompilaeroda,nãoimprimindonada,
poisnãochamamosométodo Teste.
3. Arespostacertaé(c). Ocódigocompilasemerros: aordem package
e importestáadequada,eostipossãoopcionaisdentrodeumarquivo
java.
4. Arespostacertaé(d). Umavezqueoarquivochama A.java,oúnico
tipopúblicoquepodeexistirdentrodeledevesechamar A,oq uenão
éverdade: tentamosdefinirumtipo Bpúblico.
3.3 -Exercícios
1.Om é t o d omain não pode devolver int nem Void. Ele também
deveserpúblicoesóreceberumargumento: umarray(ouvarargs)de
String.P o r t a n t o :
public static void main(String... args)
Arespostacertaé(a).
2. Para compilar, estamos trabalhando com arquivos e diretórios, por-
tanto javac b/A.java ;enquanto,pararodar,estamospensandoem
pacoteseclasses: java b.A .Arespostacertaé(d).
3. Ao rodar sem argumentos, nosso array tem tamanho zero, por-
tanto, ao tentar acessar seu primeiro elemento recebemos um
NullPointerExceptionnalinha5. Arespostacertaé(c).
4. Para rodar um programa dentro de umjar sem ter um manifesto,
devemosusaroclasspathcustomizado. Colocamoso jarnoclasspath
e dizemos qual classe desejamos rodar:java -cp programa.jar
b.A.Ar espostacertaé(f).
368

## Página 374

CasadoCódigo Capítulo12. RespostasdosExercícios
5. Durante a compilação, para adicionar o arquivoprograma.jar ao
classpath,devemosusar -cp programa.jar e,paraespecificaroar-
quivoadequado,usamos b/A.java. Aopçãoqueapresentaessasduas
características é javac -cp programa.jar:. b/A.java .Ar e -
spostacertaé(h).
3.4-Exercícios
1. Arespostacertaé(a). Ocorreumerrodecompilaçãonaclasse Teste
aotentarimportarumaclassenãoacessívelaoutrospacotes.
2. Arespostacertaé(a). Oerrodeambiguidadeédadono importenão
nautilização,portantooarquivonãocompila.
3. A resposta certa é (c). Não existe ambiguidade uma vez que o import
específicotempreferênciaemcimado * .
4. Arespostacertaé(c). Nãoháerrodeambiguidade, simplesmenteum
importédesnecessárioenãogeraerronenhum,apenasum warning.
5. Arespostacertaé(e). OarquivoBcompilapoiséumaclassenormal. O
arquivo C não compila pois tenta acessar B, que está em outro pacote,
maslembre-sequedevemosacessarospacotesdiretamente,nãoexiste
sub paco te.OmesmovaleparaA.P o rtan to ,nemAnemCco m p ilam.
6. A resposta certa é (d). Um pacote pode ter nome começando com
m a i ú s c u l o ,i s s on ã oa f e t ae mn a d a .M a sn ã oéopadrão. O nome de
variáveis locais e parâmetros não afetam a assinatura de um método
emJava. Umaclassenãoprecisaserpúblicaparaserrodada. Portanto
ocódigoco m p ilaer oda.
7. Arespostacertaé(b). NãoimportamosaclasseA,somenteseusmem-
bros,errodecompilaçãoaotentarreferenciá-lanalinha5.
8. A resposta certa é (a).
import static é o uso adequado, e não
static import ,err onalinha3.
369

## Página 375

CasadoCódigo
9. A resposta certa é (a). B não compila pois tenta acessar uma classe
dopacotepadrão(semnome). Classesdopacotepadrãosópodemser
acessadasporoutrostiposdopacotepadrão. Nãocompila.
4.1-Exercícios
1. A resposta certa é (d). O código compila e imprime 100. Podemos ter
espaçosembrancodesdequenãoquebreumapalavra-chave,nomede
método,classeetc. aomeio. Ondepodeterumespaçoembranco,pode
havervários.
2. A resposta certa é (a). O código não compila pois tentamos acessar
av a r i á v e l
idade que pode não ter sido inicializada. Não é certeza
(somentesecairno ifelaseráinicializada).
3. Arespostacertaé(f). Nãocompila,doladodireitodaatribuiçãotemos
um array de boolean e do lado esquerdo uma variável simples do tipo
boolean.
4. A resposta certa é (b). Imprime
false pois um array de tipos primi-
tivosapósainicializaçãotemseusvalorescomovalorpadrãodotipo.
Paranuméricosé0,para
booleané falseeparareferênciasé null.
5. Arespostacertaé(b). Nãocompilapois booleanemJavasópodeser
falseou true.
6. Arespostacertaé(a). Onúmerooctal09nãoexiste. Vocênãoprecisa
a p r enderatransfo rmarumabaseemo u tra,maséim po rtan telemb rar
que binários são compostos de 0s e 1s, octais são compostos de 0s até
7s,hexadecimaissãode0saté9seAsatéFs(maiúsculoouminúsculo).
Ocaractere
_ épermitidodesdequedosdoisladosdeletenhamosal-
garismos válidos, que é o caso de 1_000. Portanto, o único número
inválidoé09(porcuriosidade,onúmero9embaseoctalé011).
7. A resposta certa é (c). Compila e imprime o alfabeto pois caracteres
sãonúmerosemJava.
370

## Página 376

CasadoCódigo Capítulo12. RespostasdosExercícios
8. A resposta certa é (e).instanceOf não é palavra reservada: note a
letramaiúsculanomeiodela. Nenhumapalavra-chaveemJavapossui
caracteremaiúsculo.
9. Arespostacertaé(d). Compilaeroda,nãoimprimindonada. Lembre-
sequeosidentificadoressão case-sensitive.
4.2-Exercícios
1. A resposta certa é (e). Imprime 47, pois a atribuição é por cópia do
valor.
2. A resposta certa é (f). Imprime 48, pois a atribuição de objetos é feita
porcópiadareferência,criamossomenteumúnicoobjetodotipo B.
4.3-Exercícios
1. Arespostacertaé(d). Nãoexisteconflitodenomesentrevariávelmem-
broemétodoouvariávelmembroevariávellocal. Aoinvocarométodo
c,p o rc a u s ad oshadowing da variável c, não acessamos a variável
membro, sem alterá-la. O resultado é a impressão dos valores 10 e 10
novamente.
4.4-Exercícios
1. Arespostacertaé(c). Compilaenãopodemosfalarnada.
2. Arespostacertaé(b). Somente10objetospodemsergarbagecoletados
poisoúltimocontinuareferenciadopelavariável b.
3. A resposta certa é (b). O código compila, mas como não chamamos
nenhumconstrutor,oúnicoobjetocriadoqueseassemelhaa B,porém
não é B, é um array do tipoB, com 100 espaços. Nenhum objeto é
criado. Notequeparacriardevemos,porpadrão,invocaroconstrutor.
371

## Página 377

CasadoCódigo
4.5-Exercícios
1. A resposta certa é (b). O código compila e devido à regra de sempre
invocaromaisespecífico,elesempreinvocaométodosemargumentos.
Portanto,oresultadoévazio/vazio. Lembre-sequeemJavaaordemde
definição de métodos não importa para a invocação. Já a ordem das
variáveispodeimportar,casoumadependadaoutra.
2. Arespostacertaé(c). Ocódigocompilaeimprime2.
3. Arespostacertaé(e). Ocódigocompilaeimprime2.
4. A resposta certa é (e). O código compila e imprime 2. Esse é o caso
absurdoondeoarrayétantoum
Objectquantoumarrayde Object.
PorpadrãooJavatratarácomoumarrayde Object.
4.6-Exercícios
1. A resposta certa é (e). O array começa na posição 0, portanto, o
primeirocaractereremovidoseencontranaposição2,o i.E l er e m o v e
todos os caracteres até a posição 3, exceto o da posição 3, portanto so-
menteo
iéremovido.
2. A resposta certa é (a). Os dois métodos retornam-1 quando não en-
contram nada, portanto, o segundo resultado é-2. Como a posição
começaem 0,oresultadodasletras esão 5e 8,totalizando 13.
4.7-Exercícios
1. A resposta certa é (a). Não compila, poislength() éu mm é t od od e
String,diferentedosarraysemque lengthéuma trib u to .
2. A resposta certa é (b). DáNullPointerException! msg énull e
nãodáp rachamar isEmptyem null.
3. Arespostacertaé(a). Nãocompilapoisavariávelnãofoiinicializada.
372

## Página 378

CasadoCódigo Capítulo12. RespostasdosExercícios
4. Arespostacertaé(a). ‘Caelum‘e‘Caelum-EnsinoeInovação‘.
5. Arespostacertaé(e). Compilaeimprime Bem-vindo null
6. Arespostacertaé(b). NãocompilapoisaStringnãofoiinicializada
7. Arespostacertaé(b). Nãocompilaporoutromotivo:avariável vazio
nãoéestática.
8. Arespostacertaé(e). Compilaeimprime Bem-vindo null .
9. Arespostacertaé(d). Dá NullPointerExceptionaotentarcriara
segunda String.
10. Arespostacertaé(c). Ocódigocompilaeimprime uda.
11. Arespostacertaé(a). Nãocompilapois Stringpossuidiversoscon-
strutoresquerecebemumargumento: ocompiladornãosabequalde-
les você deseja invocar pois os tipos que são argumentos do constru-
tor não possuem herança entre si (um não herda necessariamente do
outro).
12. A resposta certa é (c). Nenhuma das alternativas dadas com número,
poisprimeiroelesoma
valore dividePor,imprimindo14. Aconta
de divisão é feita entreint, devolvendo umint de valor 2. Quando
esse número é atribuído a umdouble, continua sendo 2. Portanto,
imprime 14e 2.0.
13. Arespostacertaé(a). Ocódigonãocompilapoisométodo replace
possui duas maneiras de ser invocado: com doischars ou com duas
Strings. Forampassadosuma Stringeum char,métodoquenão
existe.
14. Arespostacerta é(a). Pensamosque podeser gualherme, maslem-
bramos que String em Java é imutável e ela não foi reatribuída. O
= dá uma impressão de reatribuição de parte daString, mas isso
nãoexisteemJava,oladoesquerdodeumaatribuiçãodevesersempre
uma variável e não uma chamada a um método. Por isso, a linha do
substringnão compila.
373

## Página 379

CasadoCódigo
5.1-Exercícios
1. As opções (a) e (c) não compilam e precisam do casting mesmo com
shorte chartendo2bytes.
Na opção (a), pode ocorrer de oshort ser negativo e, portanto, não
caber no intervalo doschars. Na opção (c), ochar pode ser muito
grandeesairforadoalcancedospositivosdo short.
Aopção(b)compila,poiso charquepossui2bytespodeseratribuído
paraum longquepossui8bytes.
2. Arespostacertaé(b). Análiselinhaalinha:
– divisãointeira: i1vale1
– divisãointeira,quedepoisépromovidoa double:i2vale1.0
– divisão double:i3vale1.5
– xvale0Ledvale0.0(d uasp r o moções)
– Oresultadoé3.5
3. A resposta certa é (d). Mesmo c sendo null, por estarmos us-
andoooperador &,asegundapartedaexpressão( c.getPreco() >
10000) será avaliada, causando umaNullPointerException na
chamada do método getPreco() caso c seja null. Poderíamos
evitarissousandoooperadordecurto-circuito, &&.
4. Arespostacertaé(d): iec.
5. A resposta certa é (d). Pode-se utilizar o operador booleano de ou ex-
clusivo ^:
if (trem ^ carro){
// ....
}
6. 1ª linha: ArithmeticException: / by zero 2ª linha:
Infinity3ªlinha: Infinity4ªlinha: -Infinity
374

## Página 380

CasadoCódigo Capítulo12. RespostasdosExercícios
7. A resposta certa é (b). O código não compila na linha 7. O compi-
lador não tem certeza se a variávely vai ser iniciada sempre. Como a
declaraçãoéfeitaeoúnicovaloratribuídoédentrodo for, o compi-
ladornãotemcertezaseo forvaiserexecutadomesmo.
8. Arespostacertaé(d).
9. Arespostacertaé(e). Compila,rodaeimprimeA75. Cuidadoaocom-
pilarerodarpoisalgunscaracterespodemprecisarserescapadospelo
seu shellou bash(nãocobradonaprova).
5.1-Exercícios
1. Nãocompila! Todacontadevolvenomínimoum int. Oresultadode
b 1+b 2 é int. Podemosfazercastingoudeclarar b3como int.
5.1-Exercícios
1. Arespostacertaé(c). Nãocompila,poistodacontadevolvenomínimo
um int,eum intnãocabeemum byte.
5.1-Exercícios
1. Arespostacertaé(c),3.
O forexternovaicontarde0a5,masdentrodo fortemum ifque
pré-incrementa o i.E s s eif v a iq u e b r a rol o o pn om o m e n t oq u eo
valo rr eto rnadofo rdivisívelpo r3,istoé,quandoivaler3nessecaso.
2. Arespostacertaé(a),1.
Dessa vez, o valor dei será usado no if e só depois incrementado.
Como o resto de0dividido por qualquer número também é0,o for
sóexecutaumavez. Masovalorde iaindaseráincrementado,impri-
mindoovalorde 1.
375

## Página 381

CasadoCódigo
3. Vaiimprimir3.
O forexternovaicontarde0a5,masdentrodo fortemum ifque
pré-incrementao i.E s s eifvaiquebraro loopnomomentoemqueo
valo rr eto rnadofo rdivisívelpo r3,istoé,quandoivaler3nessecaso.
5. A resposta certa é (f). A segunda linha do métodomain não compila
poisestouraolimitedebyte.
6. Arespostacertaé(1). Ocódigonãocompilapoisnãopodemosdeclarar
um charnegativo.
7. Arespostacertaé(f). Ocódigocompilaeimprimeumoutrovalor(65
+3).
8. A resposta certa é (b). O código compila e joga uma exception por
causadadivisãointeira(são ints)porzero.
9. Arespostacertaé(c). Ocódigocompilaeimprimepositivoinfinito. A
precedênciadeoperadoreséprimeiroadivisão,porissocompila.
10. A resposta certa é (a). Não compila, não há comparação entre
booleanenúmeros.
5.2-Exercícios
1. A resposta certa é (a). Não compila pois o resultado do parenteses é
uma Stringquenãopossuiooperadordedivisão.
2. A resposta certa é (b). true==false é false. O inverso disso é
true. Concatenandocom ""oresultadoé true,queéiguala true.
Portanto,ooperadorternáriodevolve 1queédiferentede0,imprim-
indo false.
376

## Página 382

CasadoCódigo Capítulo12. RespostasdosExercícios
5.3-Exercícios
1. Arespostacertaé(b). Ocódigocompilaeimprime truee false.
2. A resposta certa é (d). Compila e imprimefalse, false,u m av e z
queaS tring2vale s.
3. Arespostacertaé(c). Compilaeimprime true, true. Pormaisque
substringdevolvaumanovaString,nessecasoeledevolveuaString
inteira,aprópriaString.
4. A resposta certa é (c). O código imprimetrue e true. Note que o
método equalsnão foi sobrescrito.
5. Arespostacertaé(a). Ocódigonãocompilapois Dnãoédoti po C.
5.4-Exercícios
1. A resposta certa é (c). O código compila normalmente e imprime0
casonãosejapassadonenhumargumento.
2. A resposta certa é (a). O código não compila pois a variávelvalor é
final e não pode ser alterada, mas tentamos efetuar uma atribuição
dentrodo if.
3. A resposta certa é (a). O código não compila pois tenta atribuir 15 a
umavariá veleco nferirovalo r1 5co mosefosseumboolean.
4. A resposta certa é (a). O código não compila pois não existe palavra-
chave elseif. Devemosfazerum else if paracompilar.
5. A resposta certa é (b). O código não compila pois oelse não está
aplicado ao if: para ser aplicado aoif, ele deve vir imediatamente
após seu bloco. Como oif não possui chaves, somente a primeira
linhapertenceaele.
377

## Página 383

CasadoCódigo
5.5-Exercícios
1. Arespostacertaé(d). Aorodarcom5argumentos, ocódigoimprime
mais argumentos .
2. Arespostacertaé(a). Ocódigonãocompilapois tamanhoEsperado
não é uma constante. Somente podemos verificarcase de switch
emvariáveisfinaisinicializadasdiretamente.
3. A resposta certa é (b). AString "42" éu m aString umavezque
elaestáen tr easpas.P o rtan to ,ocódigoim p rimeGuilherme.
4. A resposta certa é (a). A sintaxe docase éc o m: e não com {,o
códigonãocompila.
5. A resposta certa é (a). O código não compila pois ocase não aceita
expressões como <x , mas sim um valor definido em tempo de com-
pilação.
6. A resposta certa é (a). O código não compila pois há código que não
seráexecutadoapós break.
6.1 -Exercícios
1. Arespostacertaé(f). Nãofazsentidotercolchetesantesdadeclaração
dotipo,portanto []int x não compila.
2. Arespostacertaé(b). Asegundalinhanãocompilapois,ouvocêpassa
otamanho,oupassaosvalores.
3. A resposta certa é (x). O programa não compila pois a segunda e a
terceira linha tentam redefinir uma variável já definida. Caso o nome
da variável seja corrigido, o código compila e imprime nada ao rodar
(umarraypodetertamanhozero).
4. Arespostacertaé(c). Oprogramainicializa
i para o tamanho do ar-
ray,acessandoumaposiçãoinexistente. Portantodáerroemexecução
(exception).
378

## Página 384

CasadoCódigo Capítulo12. RespostasdosExercícios
5. A resposta certa é (b). Não tenha medo de simular o código na mão.
Sim uleamemó riaeper cebaquedáuma Exception.
6. A resposta certa é (f). Não tenha medo de simular o código na mão.
Simule a memória e perceba que o resultado é2, -5. Para isso, de-
senhe os três espaços do array, aponte os valores iniciais 0 e continue
atribuindovalores,executandoocódigo.
Durante a prova, simular os arrays e os ponteiros é ideal para não se
perderemcódigoscomplexosdereferênciasevalorescomarrays.
7. A resposta certa é (d). Compila e imprimetrue: note que não existe
criação de um novo array, nós simplesmente temos duas referências (
valorese valsparaomesmoarraynamemória).
8. Asrespostascorretassão(a),(b),(f)e(j).
6.2-Exercícios
1. Arespostacertaé(a). Nãocompilapois,aoinicializarmosoarray zyx,
utilizamosumarraydeumaúnicadimensão.
2. Arespostacertaé(f). Naposição2,temosoarray z,quetem30casas,
portantotemosoresultado 30.
3. Arespostacertaé(g). Ocódigocompilaeimprime 30 normalmente.
Nãoháproblemaalgumemapontarparaumnovoarray.
4. A resposta certa é (a). Nesse exemplo, é guardado um valordouble
em uma das posições do array deint idades . Isso está incorreto
portanto não compila.
Na declaração do array de duas dimensõestabela, são informa-
dos os tamanhos das dimensões. Errado pois os tamanhos devem ser
definidosnainicializaçãoenãonadeclaração.
Na inicialização do arraycubo, não foi colocado o tamanho de nen-
humadasdimensões.
379

## Página 385

CasadoCódigo
6.3 -Exercícios
1. Arespostacertaé(a). Ocódigonãocompila,poisaclasse ArrayList
nãofoiimportada.
2. A resposta certa é (d). O código roda e imprimetrue, pois foi re-
movidoumelementodalista.
3. A resposta certa é (f). O código roda e imprime 1 pois ele remove o
primeiroelementoigualaoelementopassado.
4. Arespostacertaé(h). Ocódigocompilaeimprime5.
5. Arespostacertaé(a). Ocódigonãocompila,poisométodo toArray
semargumentosretornaumarrayde Object.
6. Arespostacertaé(b). Ocódigoincluioselementossemprenofinalda
ArrayList,po rtan toim p rimeaedepois d.
7. A resposta certa é (a). O código não compil,a pois a ordem dos
parâmetrosparaométodo addé int, String .
8. A resposta certa é (b). O código compila e imprime somentea.I s s o
porqueeleexecutaum nextduranteopassodeiteraçãodolaço for,
oqueacabaconsumindoosegundoelementosemimprimi-lo.
9. Arespostacertaé(c). Ocódigocompilaeimprime a, b, c, d,po iso
laço está alterando o valor referenciado pela variávels,en ã oov a l o r
contidodentrodanossa ArrayList.
7.1-Exercícios
1. Arespostacertaé(e). Ocódigocompilaeaorodar, anãoémaiorque
100,po rtan toim p rime10.
2. Arespostacertaé(c). Ocódigojácompilapoisavariávelnãoéfinal,e
entraemloopinfinito.
380

## Página 386

CasadoCódigo Capítulo12. RespostasdosExercícios
7.2-Exercícios
1. Arespostacertaé(a). Ocódigonãocompila,poisolaçonuncaéque-
bradoenuncachegaaexecutarocódigoqueimprime b.
2. A resposta certa é (a). O código não compila, pois o código dentro de
fornuncaseráexecutado.
3. A resposta certa é (a). O código não compila, pois tentamos definir o
tipodeduasvariáveisnonosso for.
4. Arespostacertaé(b). Compilaeimprimeosvalores0até9.
5. A resposta certa é (a), O código não compila pois a condição de um
fordeveserúnica.
6. Arespostacertaé(e). Ocódigocompilaeimprime 0112
7.3-Exercícios
1. A resposta certa é (b). O código compila e imprimefalse,p o i se l e
sempreentranolaçopelomenosumavez.
2. A resposta certa é (b). Compila e entra em loop infinito caso seja pas-
sadozero ,umoudoisargumentos.N ãoimprimenadacaso3a9argu-
mentos. Imprime‘Finalizou’caso10oumaisargumentos.
3. Arespostacertaé(c). Ocódigocompilaeimprime‘0‘,jáqueacondição
é‘i‘maiorque10.
4. A resposta certa é (a). O código não compila, pois faltou um ponto e
vírgula.
5. Arespostacertaé(c). Compilaesai.
381

## Página 387

CasadoCódigo
7.4-Exercícios
1. A resposta certa é (a). Quando iteramos por duas coleções ao mesmo
tempo, podemos usar tanto ofor quanto o while, mas o for é
maissimples, poispassaportodos oselementosjácoma inicialização
eincrementobemdefinidosdentrodolaço.
2. A resposta certa é (a). Usamos o for tradicional (com ou sem
Iterator) para remover elementos. Poderíamos usar owhile, mas
elenãoestánalistaderespostas.
3. A resposta certa é (b). Devemos usar odo...while, que garante a
execuçãopelomenosumavezdocódigo.
4. A resposta certa é (d). for, while ou do...while resolvem o
p r oblema,masomaisco m uméowhile.
5. Arespostacertaé(b). Nãoépossívelinicializarosvaloresdeumarray
como enhanced for ,po rtan tousamoso for.
7.5-Exercícios
1. O código não compila pois o segundoif está fora do bloco do for e
tenta acessar uma variável definida dentro dele. Lembre-se que o es-
copo de um bloco
for sem chaves é uma única instrução, no caso o
primeiro if else if .
2. Arespostacertaé(d). Compilaeimprime0até19,21até24,26até29.
3. Arespostacertaé(j). Compilaeaorodarcom0argumentosimprime
1a té1 5,fim.
8.1-Exercícios
1. A resposta certa é (a). O código não compila pois existe umreturn
semvalor.
382

## Página 388

CasadoCódigo Capítulo12. RespostasdosExercícios
2. Aresposta certaé(a). Nãocompila, poisnãobasta avariávelser final;
parafuncionarno switch,elatemqueserdefinidacomvalorconstante
(sempre5,porexemplo).
3. A resposta certa é (b). O código não compila porque o métodoc re-
tornaum long,eesse longéutilizadocomoretornonométodo ae
no método b. Ambos precisam de um retorno do tipoint, que não
temconversãoautomática.
4. A resposta certa é (a). O código não compila, pois não existe retorno
demétodocomdoisvalorescomo int, int.
8.2-Exercícios
1. A resposta certa é (a). O código não compila pois os métodos não
possuem tipo de retorno definido. Típica pegadinha: parece focar em
staticmasestáfocadoemoutracoisa.
2. Arespostacertaé(b). Imprimex,depoisy.
3. Arespostacertaé(d). Compilaeimprime z.
4. A resposta certa é (a). O código não compila pois tenta acessarthis
dentrodeumcontextoestático.
5. Arespostacertaé(b). Ocódigocompilaeimprime xe y.
8.3-Exercícios
1. A resposta certa é (a). O código não compila, pois não há sobrecarga
demétodoaoalterarsóoretorno.
2. Arespostacertaé(c). Compilaeimprime 15, 15e 15.0.
3. Arespostacertaé(a). Ocódigonãocompila.
4. Arespostacertaé(a). Nãocompila: osmétodosnãosãoestáticos.
383

## Página 389

CasadoCódigo
5. Arespostacertaé(d). Compilaeimprime 3.
6. Arespostacertaé(b). Compilaeimprime1.
7. A resposta certa é (a). Não compila, pois tem várias variáveis locais
(parâmetros)comomesmonome.
8. Arespostacertaé(b). Compilaeimprime1.
8.4-Exercícios
1. A resposta certa é (d). O código compila e joga um
NullPointerException.
8.5-Exercícios
1. Arespostacertaé(a). Ocódigonãocompilaporcausadoloop,quando
umconstrutordeumtipochamaoutroconstrutordomesmotipoem
loopdireto.
2. A resposta certa é (d). O código não compila pois as classes definem
parêntesesamais. Cuidado.
3. Arespostacertaé(f). Ocódigocompilaenãoimprimenada.
4. Arespostacertaé(f). Ocódigocompilaenãoimprimenada.
5. Arespostacertaé(e). Ocódigocompilaejogaexceptionaoentrarem
loopinfinito.
8.6-Exercícios
1. Arespostacertaé(a). Ocorreumerrodecompilaçãonaclasse Teste
aotentarchamaroconstrutorcomacesso defaultdeoutropacote.
2. Arespostacertaé(c). Compilaeimprime 3.
384

## Página 390

CasadoCódigo Capítulo12. RespostasdosExercícios
3. Arespostacertaé(b). Nãocompilanadeclaraçãodométodo private
public.
4. Arespostacertaé(a). Ocódigonãocompila,poisaclasse Aéaprópria
classedométodo main,eelanãotemmétodo a.
5. Arespostacertaé(b). Imprime 1,poisométodoquerecebe String
nãoestávisívelnopacoteprincipal.
6. Arespostacertaé(a). Nãocompila,poisapalavra defaultnãopode
serusadacomomodificadoradevisibilidadedemétodo(elaéusadaa
partirdoJava8deoutramaneira,quenãoécobradanestaprova).
7. Arespostacertaé(b). Ocódigocompilaeimprime1
8.7-Exercícios
1. Arespostacertaé(b). Compilaeimprime0,sãoduasinstânciasde B!.
2. Arespostacertaé(c). Compilaeimprime5.
3. Arespostacertaé(b). Compilaeimprime0,existe shadowingaquino
setter.
4. Arespostacertaé(c). Compilaeimprime5.
5. Arespostacertaé(d). Compilaeimprime10,existe shadowingaquino
setter,en tãonãoháp r oblemadeavariá velser final.
8.8-Exercícios
1. A resposta certa é (a). Não compila pois somente variáveis podem ter
aplicadasautoincrement edecr emen to .
2. Arespostacertaé(c). Compilaeimprime151.
385

## Página 391

CasadoCódigo
9.1-Exercícios
1. Aqui não ocorre sobrescrita. Como os parâmetros são diferentes,
o c o r r eu m as o b r e c a r g a( n ã oc o n f u n d i rn ap r o v aoverloadcom over-
write).Ouseja,éumoverload comherança.
2. A reescrita é válida, poisFileNotFoundException és u b c l a s s ed e
IOException.
3. A resposta certa é (a). O código não compila pois há um ciclo na her-
ança.
4. Arespostacertaé(a). Ocódigonãocompilapoisusaherançamúltipla
declasses,quenãoexisteemJava.
5. Arespostacertaé(c). Ocódigocompilaenãoimprimenada.
6. Arespostacertaé(a). Ocódigonãocompilapoisnãoexisteconstrutor
de Baoqual Atenhaacessoparaherdardomesmo.
7. A resposta certa é (a). O código não compila poisA não tem acesso a
variávelde B.
8. Arespostacertaé(b). Compilaeimprime‘t‘
9.2-Exercícios
1. Arespostacertaé(a). Ocódigonãocompilapoisfaltouo import de
java.io.*.
2. Arespostacertaé(b). Ocódigocompilaeimprime‘b‘.
3. Arespostacertaé(c). Ocódigocompilaeimprime‘c‘.
4. A resposta certa é (a). O código não compila:C n ã op o s s u im é t o d o
quereceba double.
386

## Página 392

CasadoCódigo Capítulo12. RespostasdosExercícios
5. Arespostacertaé(a). Nãocompila,poisinterfacenãopodetermétodo
comcorpodamaneiracomofoidefinidoaqui.
6. Arespostacertaé(d). Compilaeimprime‘d‘
7. Arespostacertaé(g). Compilaeentraemloop.
8. Arespostacertaé(b). Compilaeimprime‘b‘.
9. Arespostacertaé(a). Nãocompila,nãoexiste super.xnaclasse B.
9.3-Exercícios
1. Arespostacertaé(a). Nãocompilapoisháumerrode copyepastenos
nomesdasvariáveis.
2. Arespostacertaé(c). Compilaeimprime2.
3. Arespostacertaé(c). Compilaeimprime2.
4. Arespostacertaé(c). Compilaeimprime2.
5. Arespostacertaé(b). Compilaeimprime1.
6. A resposta certa é (a). O código não compila pois o métodofecha
nãoépúblico.
7. Arespostacertaé(d). Ocódigoimprime‘fechandocontanormal‘.
8. A resposta certa é (a). O código não compila pois, ao sobrescrevê-lo,
tentamos definir um escopo menor. Não compila também porque o
método fechaépackageprotected dentrode Conta.
9. A resposta certa é (c). O código compila e imprime ‘fechando finan-
ceiro‘.
387

## Página 393

CasadoCódigo
10. O código compila normalmente. Apesar de o métodoligar não es-
tar declarado na classeCarroConcreto, a classe herda este método
de Carro, logo, não é necessário reescrevê-lo (poderia reescrever se
achassenecessário).
A declaração de queCarroConcreto implementa Veiculo tam-
bém não era necessária, pois Carro já implementa Veiculo e
CarroConcretoéum Carro.
9.4-Exercícios
1. Arespostacertaé(c). Ocódigocompilaeroda,aorodarnãodáexcep-
tion.
2. Arespostacertaé(d). Ocódigocompilaeroda,aorodardáexception.
3. Arespostacertaé(a). Ocódigonãocompila: Datéimplementa Ze W
masnãoimplementa Y.
4. A resposta certa é (d). O código compila: algum subtipo deD pode
implementar Y.Aorodar,eledáexception.
5. Arespostacertaé(c). Compila, poisapesarde B nãoimplementar Z,
um subtipo dele pode (e na prática já o faz) implementá-lo. Ao rodar
nãodáexceptionnenhuma.
6. Arespostacertaé(d). Ocódigocompilaerodadandoexception.
7. Arespostacertaé(a). Dnãoimplementa Y,nãocompila.
8. Arespostacertaé(b). Ocódigonãocompila: instanceof éminús-
culo.
9. Arespostacertaé(c). Ocódigocompilaeimprime true.
388

## Página 394

CasadoCódigo Capítulo12. RespostasdosExercícios
9.5-Exercícios
1. Arespostacertaé(c). Ocódigocompilaeimprime2.
2. Arespostacertaé(a). Ocódigonãocompila.
3. Arespostacertaé(a). Ocódigonãocompila.
4. Arespostacertaé(a). Ocódigonãocompila: nãofazsentidoacessaro
} superdeoutroobjetoquenãoeumesmo.
5. Arespostacertaé(c). Ocódigocompilaenãoimprimenada:ométodo
definidonãoéumconstrutor!
6. Arespostacertaé(a). Nãocompilapoistentamosinvocardois this.
7. Arespostacertaé(c). Compilaenãoimprimenada.
8. Arespostacertaé(c). Compilaenãoimprimenada.
9. A resposta certa é (a). Não compila: não podemos referenciar um
métododeinstânciaaoinvocarumconstrutor this.
10. Arespostacertaé(b). Compilaeimprime‘2‘.
9.6-Exercícios
1. Arespostacertaé(c). Compilaeimprime‘2‘.
2. Arespostacertaé(a). Aclasse Bnão compila.
3. Arespostacertaé(b). Compilaeimprime‘1‘.
4. Arespostacertaé(b). Compilaeimprime‘1‘.
5. Arespostacertaé(a). Nãocompila,poisométodoéfinal.
6. Arespostacertaé(c). Compilaeimprime‘b‘.
389

## Página 395

CasadoCódigo
10.1 -Exercícios
1. Arespostacertaé(d). Aúnicaexceptiondalistaquenãoécheckedéa
IndexOutOfBoundsException
10.2-Exercícios
1. (b) e (e) são corretas. (a) está errada pois podemos usar exceptions
mesmosementradasdousuário. (c)estáerradapoispodemosmanter
oprogramarodandomesmoqueumaexceptionocorra. (d)estáerrada
p o i sd e v e m o su s a ro u t r a se s t r u t u r a sp a r ac o n t r o l a rofl u x od en o s s o
programa,como
ifporexemplo.
2. (a) e (c) estão corretas. (b) e (d) estão incorretas por serem os opos-
tosdascertas,e(e)estáincorretapoisexceptionsnãosãomaneirasde
aumentarasegurança.
10.3 -Exercícios
1. Arespostacertaé(a). Ocódigonãocompilapoisavariávellocalnunca
foiinicializada.
2. A respostacerta é (c). Quando ocorre aexception, ofluxo desvia para
imprimir“b”edepoiscontinuanormalcomo“c”.
3. A respostacerta é(c). Quando ocorrea exception, ofluxo desvia para
imprimir “b”, passa pelo
finally imprimindo “c”, e depois continua
no rmalco mo“ d ” .
10.4-Exercícios
1. A resposta certa é (a). Devemos colocar uma
java.io.IOException.
2. A resposta certa é (b). O código compila pois ele cria um array de di-
mensão2. Eleimprime acefdb.
390

## Página 396

CasadoCódigo Capítulo12. RespostasdosExercícios
3. Arespostacertaé(c). Ocódigocompilaeimprime ace,jogandouma
Exception.
4. A resposta certa é (a). O código não compila pois o métodom2 deve
trataroujogar java.io.FileNotFoundException.
5. Arespostacertaé(a). Ocódigonãocompilapoisométodo maindeve
trataroujogar java.io.IOException.
6. Arespostacertaé(c). Compila,imprime aceejogaa Excepion.
7. Arespostacertaé(e). Compila,eimprime acedb.
8. A resposta certa é (b). Compila, e imprimeacefdb, note que não
jogamosaexception,somenteainstanciamos.
9. A resposta certa é (a). Não compila: o System.out do f é
unreachable.
10. A resposta certa é (a). Não compila: a palavrathrow deveria ter sido
usadaparajogaraException.
11. A resposta certa é (c). Compila, e imprime ace e estoura uma
Exception.
10.5-Exercícios
1. Arespostacertaé(e), StackOverflowError.
2. A resposta certa é (d).OutOfMemoryError, pois tem um loop in-
finito.
391

## Página 397

ÍndiceRemissivo CasadoCódigo
ÍndiceRemissivo
abstract,321
Casting, 297
classpath,27
Constantes,326
Herança,259
interfaces,324
javac,24
overload,214
Palavras-chave,55
sobrecarga,214
varargs,74
392