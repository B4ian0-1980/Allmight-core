---json
{
  "id": "desbravando_java_e_orienta__o_a_objetos_um_guia_para_o_iniciante_da_linguagem",
  "title": "Desbravando Java e Orientação a Objetos Um guia para o iniciante da linguagem",
  "categoria": "03-linguagens",
  "subcategoria": "java",
  "resumo": "**Arquivo Original:** `Desbravando Java e Orientação a Objetos Um guia para o iniciante da linguagem.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "desbravando",
    "guia",
    "iniciante",
    "java",
    "linguagem",
    "linguagens",
    "objetos",
    "orienta"
  ],
  "perguntas_tipo": [
    "Como utilizar Desbravando Java e Orientação a Objetos Um guia para o iniciante da linguagem?",
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

# Desbravando Java e Orientação a Objetos Um guia para o iniciante da linguagem

> **Arquivo Original:** `Desbravando Java e Orientação a Objetos Um guia para o iniciante da linguagem.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 2

© Casa do Código
T odos os direitos reservados e protegidos pela Lei nº9.610, de
10/02/1998.
Nenhuma parte deste livro poderá ser reproduzida, nem transmitida, sem
autorização prévia por escrito da editora, sejam quais forem os meios:
fotográﬁcos, eletrônicos, mecânicos, gravação ou quaisquer outros.
Casa do Código
Livros para o programador
Rua Vergueiro, 3185 - 8º andar
04101-300 – Vila Mariana – São Paulo – SP – Brasil

## Página 3

CasadoCódigo
“Àminha esposaJordanae aomaiorpresente queumdia sonheireceber, nossa
filhaKatherine.”
–RodrigoTurini
i

## Página 5

CasadoCódigo
Agradecimentos
Não há outra maneira de começar este livro que não seja agradecendo a to-
dosqueincentivaramecontribuíramdiretaouindiretamenteemsuaedição.
VictorHarada,MaurícioAnicheeGuilhermeSilveiraforamalgunsdeles.
Fica um agradecimento especial ao Paulo Silveira, não só pela sua detal-
hada revisão e suas diversas sugestões e melhorias para esse livro, mas tam-
bémpelainfluênciadiretaquetememmeudiaadiaprofissional.
Gostaria também de estender o agradecimento para toda equipe da
Caelum. São profissionais exemplares que me incentivam a aprender e en-
sinardiariamente.
iii

## Página 7

CasadoCódigo Sumário
Sumário
1J a v a 1
1.1 NossoprimeirocódigoJava ................... 1
1.2 Algumasregraseconvenções .................. 3
1.3 Entendendoométodomain ................... 4
1.4 TrabalhandocomumaIDE .................... 6
1.5 Acesseocódigodesselivroeentreemcontatoconosco ... 9
2 Variáveisetiposprimitivos 11
2.1 Nossoprojeto ............................ 1 1
2.2 Declaraçãoea trib uiçãodevariá veis ............... 1 1
2.3 Tiposprimitivos .......................... 1 4
2.4 Castingdevalores ......................... 1 6
2.5 Adicionandocondicionais .................... 1 8
2.6 Loo p ingsemaisloo p ings..................... 2 1
3 Orientaçãoaobjetos 29
3.1 Criandoummoldedelivros ................... 3 0
3.2 Criandoumnovométodo .................... 3 4
3.3 Objetosparatodososlados! ................... 3 8
3.4 Entendendoaconstruçãodeumobjeto ............. 5 1
3.5 Vantagensdaorientaçãoaobjetos ................ 5 3
v

## Página 8

Sumário CasadoCódigo
4 Encapsulamento 55
4.1 LimitandodescontodoLivro ................... 5 5
4.2 Isolandocomportamentos .................... 5 9
4.3 Códigoencapsulado ........................ 6 1
4.4 GetterseSetters .......................... 6 2
4.5 Definindodependênciaspeloconstrutor ............ 6 7
5 Herançaepolimorfismo 75
5.1 Trabalhandocomlivrosdigitais ................. 7 5
5.2 Reescrevendométodosdasuperclasse ............. 8 0
5.3 RegrasprópriasdeumLivroFisico ............... 8 5
5.4 VendendodiferentestiposdeLivro ............... 8 7
5.5 Acumulandototaldecompras .................. 9 1
5.6 Herançaoucomposição? ..................... 9 4
6 Classeabstrata 95
6.1 Qualoti podecadaLivr o? .................... 9 5
6.2 Minilivronãotemdesconto! ................... 9 8
6.3 Métodoabstrato .......................... 1 0 2
6.4 Relembrandoalgumasregras ................... 1 0 4
7 Interface 105
7.1 OcontratoProduto ........................ 1 0 8
7.2 DiminuindoacoplamentocomInterfaces ........... 1 1 2
7.3 NovasregrasdainterfacenoJava8 ............... 1 1 4
8 Pacotes 119
8.1 Organizandonossasclasses .................... 1 1 9
8.2 Modificadoresdeacesso ..................... 1 2 6
9 Arrayseexception 129
9.1 Trabalhandocommultiplicidade ................ 1 2 9
9.2 Asdiferentesexceçõesecomolidarcomelas ......... 1 3 6
9.3 MuitasemuitasException .................... 1 4 2
9.4 Tambémpodemoslançarexceções! ............... 1 4 7
vi

## Página 9

CasadoCódigo Sumário
10 ConhecendoaAPI 151
10.1 Todoobjetotemumtipoemcomum .............. 1 5 1
10.2 Wrappersdostiposprimitivos .................. 1 6 1
10.3 Opacotejava.lang ......................... 1 6 3
11 CollectionFramework 169
11.1 Otrabalhodemanipulararrays ................. 1 6 9
11.2 OrdenandonossaListdeprodutos ............... 1 7 8
11.3 Gerenciandocuponsdedesconto ................ 1 8 2
11.4 java.util.Map ............................ 1 8 8
12 StreamsenovidadesdoJava8 193
12.1 OrdenandocomJava8 ...................... 1 9 3
12.2 forEachdoJava8 .......................... 1 9 8
12.3 Filtrandolivrospeloautor .................... 1 9 8
13 UmpoucodahistóriadoJava 203
13.1 Origemdalinguagem ....................... 2 0 3
13.2 Escrevaumavez,rodeemqualquerlugar! ........... 2 0 4
13.3 Linhadotempo .......................... 2 0 5
14 Continuandoseusestudos 211
14.1 Entreemcontatoconosco .................... 2 1 2
vii

## Página 11

Capítulo1
Java
1.1 NossoprimeirocódigoJava
Nolugardecomeçarcomconceitoseteorias,vamoslogopartirparaumaboa
dosedeprática! Abraseueditordetextopreferidoeescrevaoseguintecódigo
Java:
class MeuPrimeiroPrograma {
public static void main(String[] args){
System.out.println("O primeiro de muitos!" );
}
}
Esse programa imprime um texto simples. Confuso? Não se preocupe,
embrevecadaumadessaspalavrasteráseusentidobemclaro.

## Página 12

1.1. NossoprimeirocódigoJava CasadoCódigo
Salveoarquivoemalgumdiretóriodesuapreferência,maséimportante
queelesechame MeuPrimeiroPrograma.java.
Nossopróximopassoserácompilaressecódigofonte. Faremosissoman-
ualmenteutilizandoo javac,compiladorpadrãodaOracle.
Abra seu terminal e digite javac MeuPrimeiroPrograma.java .
Notequeparaissovocêprecisaestarnamesmapastadoarquivo ,oupassaro
caminhocompletoparaele.
Navegandopelaspastaselistandoarquivos
Você pode utilizar o comandocd (change directory)p a r an a v e g a r
pelassuaspastasviaterminal. UmexemploemWindowsseria:
D:\> cd Desktop\livro
D:\Desktop\livro>
OmesmocomandopodeserutilizadoemumambienteUnix(Linux
ou Mac OS). Para listar, há uma diferença. Em Windows utilizamos o
comando dir:
D:\Desktop\livro> dir
MeuPrimeiroPrograma.java
MeuPrimeiroPrograma.class
Porém, nos outros sistemas que foram citados o comando seráls.
Repare:
turini~$c dDesktop/livro
turini/Desktop/livr o~$l s
MeuPrimeiroPrograma.java
MeuPrimeiroPrograma.class
Note que, se nenhum erro de compilação ocorrer, no mesmo diretório
agora existirá um novo arquivo com o mesmo nome de nossa classe Java
(nestecaso, MeuPrimeiroPrograma),porémasuaextensãoserá .class.
Esteno voar quivoéobytecode geradopelocompilador.
2

## Página 13

CasadoCódigo Capítulo 1. Java
Para executá-lo, ainda pelo terminal, digite o comando java
MeuPrimeiroPrograma. O comando java éor e s p o n s á v e lp o re x e c u t a r
aJVM(máquinavirtual,ou JavaVirtualMachine)queiráinterpretaro byte-
codede seu programa. Repare que neste comando não passamos a extensão
doarquivo:
turini/Desktop/livr o ~ $ java MeuPrimeiroPrograma
O primeiro de muitos!
Epronto! VocêjácompiloueexecutouoseuprimeiroprogramaemJava.
Nãosepreocupe,aJVM, bytecodeeoutrosconceitosesiglasimportantes
serãomelhordetalhadosmaisàfrente.
InstalaçãodoJava
Para executar os códigos deste livro, você precisará ter o JDK (Java
Development Kit) instalado. Se precisar, você pode seguir as instruções
dolinkaseguirparainstalardeacordocomseusistemaoperacional:
http://www.caelum.com.br/apostila-java-orientacao-objetos/
apendice-instalacao-do-java/
Precisadeajuda? Nãodeixedenosmandarume-mailnogrupo:
https://groups.google.com/d/forum/livro-java-oo
1.2 Algumasregraseconvenções
Vocêpodeterreparadoqueseguimosalgumasregraseconvençõesatéagora.
Vamosentendê-lasumpoucomelhor.
Podemos começar pelo nome de nosso arquivo,
MeuPrimeiroPrograma. E mJ a v a ,on o m ed eu m ac l a s s es e m p r es e
inicia com letra maiúscula e, quando necessário, as palavras seguintes
tambémtêmseu casealterado. Dessaforma“ es seno medec las se
vira“EsseNomeDeClasse
.Essaabo r dagemébastan teco nhecidaco moCamelCase.
Um arquivo
.java possui a definição de uma classe. É uma prática
r e c o m e n d a d an o m e a rac l a s s eeoa r q u i v od am e s m af o r m a ,c a s oc o n t r á r i o
3

## Página 14

1.3. Entendendoométodomain CasadoCódigo
poderá existir alguma confusão no momento de executá-la. Por exemplo,
considere que temos um arquivomeu-primeiro-programa.java con-
tendoaclassequechamamosde MeuPrimeiroPrograma. Paracompilá-lo
faremos:
turini/Desktop/livr o ~ $ javac meu-primeiro-programa.java
Porém, o arquivo compilado (com o bytecode)t e r áon o m e
MeuPrimeiroPrograma.class. C o m oe x e c u t a re s s ep r o g r a m a ? A
respostaserácomonomedaclasse,enãodoarquivo. Nestecaso:
turini/Desktop/livr o ~ $ java MeuPrimeiroPrograma
Notetambémqueháumpardechaves {} definindooinicioefinal(es-
co po)desuaclasseeasinstruçõessem p r eterminamco mpo n toevírgula.
Porfim,éfundamentalperceberqueestaéumalinguagem casesensitive,
ouseja,levaemconsideraçãoo case(caixa)emqueasinstruçõessãoescritas.
Escrever System com letra minúscula, por exemplo, resultaria em um erro
decompilação.
Vocêpodelermaisarespeitodessasedeoutrasconvençõesdalinguagem
nodocumentooficial Code Conventions for the Java Programming Language,
disponívelnositedaOracle:
http://www.oracle.com/technetwork/java/index-135089.html
1.3 Entendendoométodomain
Ao ser executada, a máquina virtual (JVM) procura pelo bloco main
declarado em sua classe. Esse é um bloco especial (oumétodo,c o m op a s -
sar emosachamarapartirdeago ra)esepar ececo m:
public static void main(String[] args){
// seu código aqui
}
Suas aplicações Java, em geral, vão possuir apenas um métodomain,
umúnicopontodepartida. Quandorodamosocomando java passandoo
4

## Página 15

CasadoCódigo Capítulo 1. Java
nomedenossaclasse,dissemosparaaJVMexecutartodooconteúdoquees-
tiverdentrodocorpo(daschaves)dessemétodo. Emnossoexemplo,foiuma
simples instrução de impressão, o
System.out.println("o primeiro
de muitos!") .
Háaindacomopassarargumentosparaométodo mainaoexecutarum
programa Java. O parâmetroString[] args que o método recebe den-
tro de seus parênteses será o responsável por armazenar esses argumentos
para que possam ser acessados em nosso código. Mas, afinal, o que é esse
String[]?U m arrayde StringemJava,porém,porenquantonãoesta-
mosinteressadosementenderum arrayetodososseusdetalhes,tudooque
precisamossaberéqueelevaiarmazenarumamultiplicidadede Strings.
Umexemplodessapassagemdeparâmetroseria:
turini/Desktop/livr o ~ $ java MeuPrimeiroPrograma Java Rodrigo
Para isso funcionar, modificamos nosso código para exibir o conteúdo
g u a r d a d on a spo s i ç õe s0e1(args[0], args[1]) desse conjunto de argu-
mentos:
class MeuPrimeiroPrograma {
public static void main(String[] args){
System.out.println("O primeiro de muitos códigos
escritos em " +args[0]+ " pelo " + args[1]+ "!");
}
}
Execute para conferir o resultado! Não se esqueça que, como modifi-
camosnossocódigo,precisaremoscompilarnovamente:
turini/Desktop/livr o ~ $ javac MeuPrimeiroPrograma.java
turini/Desktop/livr o ~ $ java MeuPrimeiroPrograma Java Rodrigo
Nesseexemplo,oresultadoimpressoserá:
O primeiro de muitos códigos escritos em Java pelo Rodrigo!
5

## Página 16

1.4. TrabalhandocomumaIDE CasadoCódigo
Errodecompilação?
Um erro de digitação, a falta de um ponto e vírgula ou uma difer-
ença decase em seu código são alguns dos muitos motivos que podem
resultar em um erro de compilação. Conhecer e entender esses erros é
fundamental,talvezvocêqueirainclusiveprovocaralgumdelesparaver
comoseucódigosecomparta.
Qual será a mensagem caso eu esqueça de escrever um ponto e vír-
gula? Escrevaumtestesimplespradescobrir! Umexemplo:
System.out.println("sem ponto-e-virgula")
Amensagemdeerroserá:
Syntax error, insert ";" to complete BlockStatements
Lembre-se que você pode e deve tirar todas as suas dúvidas no GUJ,
emhttp://guj.com.br.
1.4 TrabalhandocomumaIDE
Escrever, compilar e executar seu código Java em um bloco de notas junto
com terminal é bastante trabalhoso. É fundamental conhecer esse processo,
masemseudiaadiavocêprovavelmentevaipreferirutilizaralgumadasmais
diversasferramentasdedesenvolvimentoconhecidasparaajudá-lonessetra-
balho.
Essas ferramentas são chamadas de IDE (Integrated Development Envi-
ronment) e podem tornar seu desenvolvimento muito mais produtivo e in-
teressante,oferecendo-lherecursoscomo syntaxhighlight eautocomplete das
instruçõesdeseucódigo.
Nodecorrerdestelivro,vamosutilizaro Eclipse,vocêpodefazerodown-
loaddesuaversãomaisrecenteem:
https://www.eclipse.org/downloads/
EssaéumaIDEgratuitaeopensource,semdúvidaumadaspreferidasdo
mercado e instituições de ensino. Seus diversos atalhos e templates prontos
6

## Página 17

CasadoCódigo Capítulo 1. Java
sãograndesdiferenciais.
E x i s t e md i v e r s a so u t r a sb o a so p ç õ e sn om e r c a d o ,c o m op o re x e m p l oo
NetBeansdaOracle,ouo IntelliJIDEA,sendoesteúltimopago.
CriandoseuprimeiroprojetonoEclipse
Depois de fazer o download, você não precisará instalar a IDE. Esta é
uma executável inteiramente escrita em Java, basta executá-la e escolher a
pasta onde será a sua área de trabalho (workspace). Escolha um local de sua
preferência.
Vamoscriarnossoprojeto! Paraisso,vocêpodepormeiodomenuescol-
her as opções File > New > Java Project . Vamos chamar o projeto
quedesenvolveremosduranteocursode livraria.
Repare que, depois de concluir, esse projeto será representando em seu
sistemaoperacionalcomoumapasta,dentrodo workspacequevocêescolheu.
Porenquanto,dentrodessediretóriovocêencontraráapasta src,ondeficará
todo o seu código.java et a m b é map a s t abin, onde ficará obytecode
compilado.
Produtividadeextrema
Agora que já criamos o projeto, vamos criar nossa primeira classe
pelo Eclipse. Você pode fazer isso pelo menu File > New > Class .
Para conhecer um pouco da IDE, vamos criar novamente a classe
MeuPrimeiroPrograma.
Depoisdepreencheronome,selecioneaopção finishevejaoresultado:
public class MeuPrimeiroPrograma {
}
Aestruturadesuaclassejáestápronta,vamosagoraescreverseumétodo
main. Parafazerisso,escrevaapalavra maindentrodesuaclasseepressione
oatalho Control + Espaço .
Esseéoatalhode codecompletion daIDE.Setudocorreubem,seucódigo
ficouassim:
7

## Página 18

1.4. TrabalhandocomumaIDE CasadoCódigo
public class MeuPrimeiroPrograma {
public static void main(String[] args){
}
}
Interessante, não acha? Além de termos mais produtividade ao escrever,
evitamosqueerrosdedigitaçãoaconteçam.
Vamos além, agora dentro do métodomain, digite syso e pressione
Control + Espaço parafazer codecompletion novamente.
V ocêpodeedeveusareab usardesser ecurso!
public class MeuPrimeiroPrograma {
public static void main(String[] args){
System.out.println("O primeiro de muitos!" );
}
}
Agora, com o código pronto, as próximas etapas seriam compilar e
executá-lo,masacompilaçãojáestápronta!
Issomesmo,conformevocêvaiescrevendoseucódigo,aIDEjácuidade
compilá-lo. Repare que se você apagar o ponto e vírgula, por exemplo, essa
linhaficarásublinhadaemvermelho. E ssaéumaindicaçãovisualdequeseu
códigonãoestácompilando.
Para executar o código, você pode clicar com o botão direito do mouse
emsuaclasseeselecionarasopções Run As > Java Application .O u
poratalho,pressionando Control + F11 .
Reparequeasaídadeseucódigovaiaparecernaaba Console.
O primeiro de muitos!
8

## Página 19

CasadoCódigo Capítulo 1. Java
AtalhosdoEclipse
ConhecerosatalhosdaIDEvaitorná-loumprogramadormuitomais
produtivo. Você pode ler mais a respeito e conhecer mais atalhos pela
documentaçãodoEclipseem:
https://www.eclipse.org/users/
Etambémnopost:
http://blog.caelum.com.br/as-tres-principais-teclas-de-atalho-do-eclipse/
Se esse for o seu primeiro contato com a linguagem, recomendamos que
você pratique bastante a sintaxe antes de partir para os próximos capítu-
los. Sinta-seconfortávelcomoprocessodeescrever,compilareexecutarseu
códigoJava. Tenhocertezadequeembreveessaserásuarotina.
1.5 Acesseocódigodesselivroeentreemcon-
tatoconosco
Todososexemplosdestelivropodemserencontradosnorepositório:
https://github.com/Turini/livro-oo
Masclaro,nãodeixedeescrevertodoocódigoquevimosparapraticara
sintaxe e se adaptar com os detalhes da linguagem. Além disso, sempre que
possívelfaçanovostestesalémdosaquisugeridos.
Ficou com alguma dúvida? Não deixe de me mandar um e-mail. A
seguinte lista foi criada exclusivamente para facilitar o seu contato conosco
ecomosdemaisleitores:
https://groups.google.com/d/forum/livro-java-oo
Suassugestões,criticasemelhoriasserãomuitomaisdoquebem-vindas!
O u t r or e c u r s oq u ev o c êp o d eu s a rp a r ae s c l a r e c e rs u a sd ú v i d a sep a r t i c -
ipar ativamente na comunidade Java é o fórum do GUJ, espero encontrá-lo
porlá.
http://www.guj.com.br/
9

## Página 21

Capítulo2
Variáveisetiposprimitivos
2.1 Nossoprojeto
Duranteolivro,vamoscriareevoluiraaplicaçãoJavadeumalivrariacomoa
CasadoCódigo . Essecontextovainospossibilitarcolocarempráticatodosos
principais recursos e conceitos da linguagem, desde o mais simples ao mais
avançado, além de conhecer e trabalhar com asAPIse featuresde sua mais
novaversão.
2.2 Declaraçãoeatribuiçãodevariáveis
V a m o sc r i a ru m an o v ac l a s s eJ a v ac u j oo b j e t i v os e r ác a l c u l a rov a l o r
total de livros do nosso estoque na livraria. Podemos chamá-la de
CalculadoraDeEstoque.

## Página 22

2.2. Declaraçãoeatribuiçãodevariáveis CasadoCódigo
public class CalculadoraDeEstoque {
public static void main(String[] args){
}
}
Precisamosagoraarmazenardentrodeseumétodo mainovalordenos-
soslivros. Umaformasimplesdefazerissoseria:
public class CalculadoraDeEstoque {
public static void main(String[] args){
double livroJava8;
double livroTDD;
}
}
Dessa forma, estamos pedindo ao Java que reserve regiões da memória
parafuturamentearmazenaressesvalores. Essainstruçãoquecriamosécon-
hecidacomoumavariável.
Repare que essas duas variáveis declaradas possuem um tipodouble
(número com ponto flutuante). Logo, conheceremos os outros tipos exis-
tentes, mas é importante reconhecer desde já que toda variável em Java pre-
cisaraterum.
Utilizamos o sinal
= (igual) para atribuir um valor para estas variáveis
querepresentamalgunsdenossoslivros:
double livroJava8;
double livroTDD ;
livroJava8 = 59.90;
livroTDD = 59.90;
Mas,nestecaso,comojásabemosovalorqueseráatribuídonomomento
de sua declaração, podemos fazer a atribuição de forma direta no momento
emquecadavariávelédeclarada:
12

## Página 23

CasadoCódigo Capítulo2. Variáveisetiposprimitivos
double livroJava8 = 59.90;
double livroTDD = 59.90;
Agoraquejátemosalgunsvaloresdelivros,vamoscalcularasuasomae
acumularemumanovavariável. Issopodeserfeitodaseguinteforma:
double soma = livroJava8 + livroTDD;
Pronto,issoétudoqueprecisamosporenquantoparacompletaranossa
CalculadoraDeEstoque. Após somar esses valores, vamos imprimir o
valordoresultadono console:
public class CalculadoraDeEstoque {
public static void main(String[] args){
double livroJava8 = 59.90;
double livroTDD = 59.90;
double soma = livroJava8 + livroTDD;
System.out.println("O total em estoque é "+ soma);
}
}
Escreva e execute esse código para praticar! Neste exemplo, o resultado
será:
O total em estoque é 119.8
Além do operador de soma (+), você também pode usar os seguintes
operadoresemseucódigoJava:
13

## Página 24

2.3. Tiposprimitivos CasadoCódigo
2.3 Tiposprimitivos
Vimosqueépossívelrepresentarumnúmerocompontoflutuanteutilizando
oti po double, mas existem diversos outros tipos para representar os difer-
entesvalorescomquetrabalhamosnodiaadia.
Para representar um número inteiro, por exemplo, podemos utilizar os
tipos byte, short, int ou long. Isso mesmo, o código a seguir compila
comqualquerumdessestipos:
byte inteiro1 = 10;
short inteiro2 = 10;
int inteiro3 =1 0 ;
long inteiro4 = 10;
Mas,afinal,quandoeudevoutilizarcadaumdesses? Agrandediferença
está no tamanho de cada um desses tipos. Por exemplo, umshort suporta
até2bytes,enquantoum longsuporta8bytes.
Muitodiferentedeantigamente,hojenãoháumapreocupaçãotãogrande
em economizar bytes na declaração de suas variáveis. Você raramente verá
um programador utilizando um
short para guardar um número pequeno,
14

## Página 25

CasadoCódigo Capítulo2. Variáveisetiposprimitivos
no lugar de usar logo umint. Mas claro, conhecer os diferentes tipos e a
capacidadedecadaumdeleséessencialparaumbomprogramador.
EssessãoospossíveistiposprimitivosdalinguagemJava:
Um detalhe simples, porém muito importante, sobre os tipos primitivos
é que, quando você atribui um valor para eles (utilizando o operador=),
este valor serácopiado para a sua variável. Por exemplo, repare no seguinte
código:
int numero =4 ;
int outroNumeroIgual = numero;
numero = numero +5 ;
System.out.println(numero);
System.out.println(outroNumeroIgual);
15

## Página 26

2.4. Castingdevalores CasadoCódigo
Nestecaso,comcertezaovalordavariável numeronomomentoemque
for impressa será 9, mas e quanto aooutroNumeroIgual? Repare que ela
recebe numeroeseuvalorfoialteradologoemseguida.
Execute esse código e você perceberá que ooutroNumeroIgual con-
tin uarácomovalor4,poisesteeraovalordavariável numeronomomento
da atribuição. Ou seja, a variáveloutroNumeroIgual guardou uma cópia
dovalor,enãoumareferênciaaelaoualgodotipo.
Tiposnãoprimitivos
Logoconheceremosoutrostipos(nãoprimitivos)dalinguagemJava,
masdesdejáreparequeumtexto,assimcomoqualqueroutrovalor,tam-
bémtemumtipo! Essetipoéconhecidopor String.
Vocêpoderia,nolugardefazer:
System.out.println("Eu sou uma String");
Declarardaseguinteforma:
String texto = "Eu sou uma String";
System.out.println(texto);
2.4 Castingdevalores
Como você já deve ter percebido, nem todos os valores são com-
patíveis. Por exemplo, se eu tentar declarar o valor de nossos livros na
CalculadoraDeEstoque como um int,u me r r od ec o m p i l a ç ã oa c o n t e -
cerá.
public class CalculadoraDeEstoque {
public static void main(String[] args){
int livroJava8 = 59.90;
int livroTDD = 59.90;
16

## Página 27

CasadoCódigo Capítulo2. Variáveisetiposprimitivos
int soma = livroJava8 + livroTDD;
System.out.println("O total em estoque é "+ soma);
}
}
Repare no Eclipse (ou qualquer outra IDE ou editor de texto que estiver
utilizandoemseustestes)queoseguinteerroseráexibido:
Type mismatch: cannot convert from double to int
Ou seja, um int n ã op o d eg u a r d a ru mn ú m e r oc o mp o n t ofl u t u a n t e(
double). Fazsentido.
Mas,sim,ocontrárioétotalmentepossível. Reparenocódigo:
public class CalculadoraDeEstoque {
public static void main(String[] args){
double livroJava8 =6 0 ;
double livroTDD =6 0 ;
double soma = livroJava8 + livroTDD;
System.out.println("O total em estoque é "+ soma);
}
}
Mesmo arredondando o valor dos livros para um número inteiro (neste
caso, 60), um double pode sim guardar esse valor. Portanto, eu posso
atribuir valores menores em variáveis com uma capacidade maior; o que eu
nãopossoéocontrário. Umaanalogiadevquegostomuitoeseencaixabem
aquié: “Vocêpodecolocarumaformiganacasadeumcavalo,ocontrárionão
dariacerto”.
Masreparequenemmesmooseguintecódigocompila:
double livroJava8 =6 0 ;
int numeroInteiro = livroJava8;
17

## Página 28

2.5. Adicionandocondicionais CasadoCódigo
Damesmaformaqueantes,estamostentandoatribuirum double(queé
umtipodetamanhomaior)emum int.Nãoimportaseovalorqueatribuí-
mosaeste doubleéumvalorinteiroválido(umbomcandidatoparaotipo
int) . Oc o m p i l a d o rv a is ep r e o c u p a rc o mot i p od es u a sv a r i á v e i s ,en ã o
com seus valores, até porque, como o próprio nome indica, esses valores são
mutáveis,portantoessaatribuiçãoseriaperigosa.
Em algum momento, você pode precisar forçar essa conversão de tipos,
dizendoaocompilador: “tudobem,eugarantoqueovalordeste doublepode
sermoldadoparaumnumerointeiro
. Paraisso,utilizamosumrecursoconhecidocomo casting.
int numeroInteiro =( int) livroJava8;
Neste caso, seu código vai compilar sem nenhum problema e a variável
numeroInteiroteráumacopiadovalor60.
Seov a l o rd olivroJava8 fosse 59.90, ou seja, um número com ponto
flutuanteevocêfizesseesse castingha veriaumaperdadeprecisão .Avar -
iável numeroInteiroteriaapenasovalor59copiado.
2.5 Adicionandocondicionais
Nossa CalculadoraDeEstoqueprecisadeumanovafuncionalidade. Seo
valortotaldelivrosformenorque150reais, precisamosseralertadosdeque
nosso estoque está baixíssimo, casocontrário, devemos mostrar uma men-
sagemindicandodequeestátudosobcontrole!
EmJava,podemosfazeressacondicionaldeumaformabemcomum,uti-
lizandoum
ife else. Observe:
public class CalculadoraDeEstoque {
public static void main(String[] args){
double livroJava8 = 59.90;
double livroTDD = 59.90;
double soma = livroJava8 + livroTDD;
18

## Página 29

CasadoCódigo Capítulo2. Variáveisetiposprimitivos
System.out.println("O total em estoque é "+ soma);
if (soma < 150) {
System.out.println("Seu estoque está muito baixo!");
} else {
System.out.println("Seu estoque está bom");
}
}
}
Comojáéesperado,essecódigosóvaiimprimiramensagemdeestoque
baixoseovalordasomaformenor( <)que150. Casocontrário,iráexecutar
oconteúdodedentrodobloco else.
Passamosumacondiçãocomoargumentofazendoumacomparaçãoen-
t r eov a l o rd av a r i á v e lsoma com o valor 150. Essa condição vai resultar em
um valor true quando verdadeira, oufalse caso contrário. Esse tipo de
condiçãoéconhecidocomo expressãobooleana. Seuresultadosempreserá
dotipo boolean:
boolean resultado = soma < 150;
Você pode usar qualquer um dos seguintes operadores relacionais pra
construir uma expressão booleana: > (maior), < (menor), >= (maior ou
igual), <= (menor ou igual),== (igual sim, são dois iguais! Lembre-se que
umúnicoigualsignificaatribuição)e,porfim, !=(diferente).
Há ainda a alternativa de encadear mais condições em nossoif.P o r
exemplo, para receber uma mensagem indicando que o estoque está muito
alto,podemosadicionaraseguintecondição:
public class CalculadoraDeEstoque {
public static void main(String[] args){
double livroJava8 = 59.90;
double livroTDD = 59.90;
double soma = livroJava8 + livroTDD;
19

## Página 30

2.5. Adicionandocondicionais CasadoCódigo
System.out.println("O total em estoque é "+ soma);
if (soma < 150) {
System.out.println("Seu estoque está muito baixo!");
} else if (soma >= 2000) {
System.out.println("Seu estoque está muito alto!" );
} else {
System.out.println("Seu estoque está bom" );
}
}
}
Operadorternário
É muito comum escrevermos condicionais como a seguinte, que, de
acordocomalgumacondiçãobooleana,retornaumvalordiferente. Re-
pare:
double valor =0 ;
if (v1 > v2){
valor = 100;
} else {
valor =0 ;
}
Uma alternativa bastante conhecida e utilizada para estes casos é o
operadorternário ?: . Comele,vocêpodefazeromesmodaseguinte
forma:
double valor = v1 > v2 ?1 0 0:0 ;
Semdúvida,ficabemmaisenxuto,nãoacha? Performaticamente,não
hánenhumavantagemsignificanteemusarumaououtraestratégia,mas
ésempreinteressantelevaremconsideraçãoalegibilidadedocódigo. Em
algunscasos,usarooperadorternáriopodecustarumpoucodalegibil-
idadeedeixarocódigomaiscomplexo.
20

## Página 31

CasadoCódigo Capítulo2. Variáveisetiposprimitivos
2.6 Loopingsemaisloopings
Considerando que todos os livros têm o preço 59.90, seria muito trabalhoso
criartantasvariáveisparaqueovalorda somaultrapasse2000reais. Paranos
ajudarnaconstruçãodesseslivrospodemoscriarumaestruturaderepetição
(um
looping). Umadasformasdesefazerissoseriautilizandoo while:
double soma =0 ;
int contador =0 ;
while (contador <3 5 ){
double valorDoLivro = 59.90;
soma = soma + valorDoLivro;
contador = contador +1;
}
O while é bastante parecido com oif. A grande diferença é que, en-
quanto sua expressão booleana fortrue, seu código continuará sendo exe-
cutado. Neste exemplo estamos criando uma variávelsoma para acumular
o valor total dos livros e também uma variávelcontador para controlar a
quantidadedevezesquequeremositerar.
Note que estamos adicionando 35 livros, já que a condição écontador
<3 5 equeacadai teraçãoincr emen tamos1aovalo rdo contador.
Nossocódigocompletoficadaseguinteforma:
public class CalculadoraDeEstoque {
public static void main(String[] args){
double soma =0 ;
int contador =0 ;
while (contador <3 5 ){
double valorDoLivro = 59.90;
soma = soma + valorDoLivro;
contador = contador +1;
}
21

## Página 32

2.6. Loopingsemaisloopings CasadoCódigo
System.out.println("O total em estoque é "+ soma);
if (soma < 150) {
System.out.println("Seu estoque está muito baixo!");
} else if (soma >= 2000) {
System.out.println("Seu estoque está muito alto!" );
} else {
System.out.println("Seu estoque está bom" );
}
}
}
Aoexecutá-loasaídaserá:
O total em estoque é 2096.5000000000014
Seu estoque está muito alto!
Loopinginfinito
É muito comum esquecermos de modificar o valor que está sendo
comparadodentrodo whileounasdiferentesformasqueveremospara
sefazerum looping. Issovairesultarnoquechamamosde loopinginfinito,
uma vez que a condição de looping sempre serátrue. Se quiser testar,
adicioneumcomentárionalinhaqueincrementaovalordo contador
eexecu teocódigo:
while (contador <3 5 ){
double valorDoLivro = 59.90;
soma = soma + valorDoLivro;
// contador = contador + 1;
}
Podemos deixar nosso código ainda mais enxuto utilizando o operador
deatribuição +=. Basta,nolugardefazer:
soma = soma + valorDoLivro;
22

## Página 33

CasadoCódigo Capítulo2. Variáveisetiposprimitivos
Mudarmosocódigopara:
soma += valorDoLivro;
Essaéumaformaequivalentedeseincrementarovalordeumavariável.
Omesmopoderiaserfeitocomnossocontador,repare:
contador += 1;
Podemosutilizaressatécnicacomosseguintesoperadores:
Mas para esse caso há uma forma ainda mais enxuta, utilizando o oper-
adorunário ++:
contador ++;
Ocódigodo whileagoraficadaseguinteforma:
while (contador <3 5 ){
double valorDoLivro = 59.90;
soma += valorDoLivro;
contador ++;
}
23

## Página 34

2.6. Loopingsemaisloopings CasadoCódigo
Nosso código pode ficar ainda mais enxuto utilizando uma outra forma
deloopingextremamenteconhecidaeutilizada,o for.
Observequeaestruturaqueutilizamosno whilefoi parecida com:
// inicialização do contador
while (condição ){
// atualização do contador
}
Como for,podemosfazerissodeumaformaaindamaisdireta:
for(inicialização; condição; atualização){
}
Issomesmo,alémdacondição booleanaeletambémreservaumlocalpara
inicialização de variáveis e atualização de seus valores. Com ofor nosso
códigopodeserescritoassim:
double soma =0 ;
for (int contador =0 ;contador <3 5 ;contador ++) {
soma += 59.90;
}
Semdúvida,éumaformamaisdireta. Vocêmuitasvezesveráessavariável
contador que criamos ser chamada dei (index, ou índice). Seguindo esse
padrão,nossocódigocompletoficaassim:
public class CalculadoraDeEstoque {
public static void main(String[] args){
double soma =0 ;
for (double i =0 ;i < 35; i ++){
soma += 59.90;
}
24

## Página 35

CasadoCódigo Capítulo2. Variáveisetiposprimitivos
System.out.println("O total em estoque é "+ soma);
if (soma < 150) {
System.out.println("Seu estoque está muito baixo!");
} else if (soma >= 2000) {
System.out.println("Seu estoque está muito alto!" );
} else {
System.out.println("Seu estoque está bom");
}
}
}
25

## Página 36

2.6. Loopingsemaisloopings CasadoCódigo
Trabalhandocom continue e break
Você pode utilizar a palavra-chavecontinue para pular uma iter-
ação de seu looping e forçar a execução do próximo laço. O código a
seguirvaiimprimirtodososnúmerosde0a10,masvaipularonúmero
7:
for(int i =0 ;i <= 10; i++) {
if (i == 7) {
continue;
}
System.out.println(i);
}
O u t r ap o s s i b i l i d a d ec o m u mép a r a rae x e c u ç ã od eu ml o o p i n g
dada uma determinada condição. Para isso, utilizamos a palavra-chave
break:
for(int i =0 ;i <= 10; i++) {
if (i == 7) {
break;
}
System.out.println(i);
}
N estecaso ,a penasosn úmer osde0a6serãoimpressos.
26

## Página 37

CasadoCódigo Capítulo2. Variáveisetiposprimitivos
Operadoreslógicos
Você pode e deve usar operadores lógicos em suas expressões
booleanas sempre que necessário. Por exemplo, repare no código a
seguir:
if (v1 > v2){
if (v2 < v3){
// é > que v1 e < que v3
}
}
Esse encadeamento de ifs prejudica um pouco a legibilidade, não
acha? Quetalfazer:
if (v1 > v2 && v2 < v3){
// é > que v1 e < que v3
}
O código terá o mesmo efeito com um únicoif, agora usando o
operadorand( &&). Outrasopçõessãoo or ( ||)ean e g a ti v a(!). Para
negar uma condição booleana tudo o que você precisa fazer é adicionar
osinal
!antesdesuadeclaração,veja:
boolean condicao =1>0 ;
if (!condicao){
// não vai entrar aqui
}
27

## Página 39

Capítulo3
Orientaçãoaobjetos
AlinguagemJavatemcomofortecaracterísticatercomoparadigmaa orien-
taçãoaobjetos , que estudaremos profundamente no decorrer do livro. Esse
paradigmaexistedesdeadécadade70,masfoidepoisdosurgimentodoJava
queficoubastantefamosoequepassouaserlevadomaisasério.
Repare que nossa CalculadoraDeEstoque está fazendo todo o tra-
balhodentrodeseumétodo main,aindadeformamuitoprocedural. Aori-
entação a objetos propõe uma maneira diferente de fazer isso, você passa a
trabalhar de um jeito mais próximo à realidade humana. Para cada necessi-
dadeimportanteteremosobjetosqueinteragementresiequesãocompostos
porestado(atributos)ecomportamento(métodos). Querumexemplo? Ob-
servecomoestamosrepresentandoopreçodenossoslivros:
double soma =0 ;

## Página 40

3.1. Criandoummoldedelivros CasadoCódigo
for (double i =0 ;i < 35; i ++) {
soma += 59.90;
}
O valor 59.90 está fazendo isso. Ele representa o valor do livro; mas, e
quanto ao seu nome, descrição e demais informações? Todas essas infor-
mações representam o que um livro tem e são extremamente importantes
para nosso sistema. O grande problema do paradigma procedural é que não
existeumaformasimplesdeconectartodosesseselementos,jánaorientação
aobjetospodemosfazerissodeumjeitomuitosimples! Assimcomonocon-
textoreal,podemoscriarumobjetopararepresentartudooqueumlivrotem
eoqueelefaz.
Umanovaformadepensar
Se você já está acostumado com algum outro paradigma, esse é o
momento de abrir a sua mente. Repare que esse é um paradigma to-
talmentediferente,vocêprecisarápensardemaneiradiferenteeescrever
seucódigodeoutraforma.
3.1 Criandoummoldedelivros
V a m o sc r i a ru m an o v ac l a s s eJ a v ac h a m a d aLivro. Essa classe será um
molde,querepresentaráoqueumlivrodeveterecomoeledevesecomportar
emnossosistema.
public class Livro {
}
Paradeixaressaclassemaisinteressante,vamosadicionaralgunscampos
pararepresentaroqueumlivrotem. Essessãoos atributosdenossaclasse:
public class Livro {
String nome ;
30

## Página 41

CasadoCódigo Capítulo3. Orientaçãoaobjetos
String descricao;
double valor;
String isbn ;
}
Repare que esses atributos são muito parecidos com variáveis que pode-
mos criar dentro de nosso métodomain, por exemplo. Mas eles não estão
dentro de um bloco e, sim, dentro do escopo da classe, por isso recebem o
nomediferenciadodeatributo.
Nosso molde já está pronto para uso. Por enquanto, um livro terá um
nome, descrição, valor e ISBN (um número de identificação,International
Standard Book Number).
Essescamposnãoserãopopuladosnaclasse Livro,elaéapenasomolde!
O que precisamos é criar um objeto a partir desse molde. Para fazer isso,
utilizamosapalavra-chave
new.
Livro livro = new Livro();
Observequeavariável livrotemumtipo,assimcomoqualquervariável
em Java, mas diferente de umint, double ou String como já estamos
acostumados,agoraseutip oéap r ó p riaclasseLivro.
Aocriarumobjetode Livro eatribuiraumavariável livro,es ta m os
estabelecendo uma forma de nos referenciar a esse objeto que até então não
temnenhumvalorpopulado.
Populandoosatributosdolivro
Agora que fizemos isso, a partir da variávellivro, podemos acessar o
objeto que foi criado em memória e popular os seus atributos. Um exemplo
seria:
Livro livro = new Livro();
livro.nome = "Java 8 Prático";
livro.descricao = "Novos recursos da linguagem";
livro.valor = 59.90;
livro.isbn = "978-85-66250-46-6" ;
31

## Página 42

3.1. Criandoummoldedelivros CasadoCódigo
Reparequeutilizamosum .(ponto)paraacessarosatributosdesseobjeto
emespecífico. Vocêtambémpoderecuperarasinformaçõesadicionadasnos
seusobjetosacessandoseusatributosdaseguinteforma:
System.out.println("O nome do livro é " + livro.nome);
Nestecaso,asaídaserá:
O nome do livro é Java 8 Prático
V a m o sc r i a ru m an o v ac l a s s ec h a m a d aCadastroDeLivros em nosso
projeto. Ela deve ter um métodomain q u ec r i au mn o v ol i v r o ,p r e e n c h e
algunsdeseusatributosedepoisimprimeosseusvalores. Algocomo:
public class CadastroDeLivros {
public static void main(String[] args){
Livro livro = new Livro();
livro.nome = "Java 8 Prático";
livro.descricao = "Novos recursos da linguagem";
livro.valor = 59.90;
livro.isbn = "978-85-66250-46-6" ;
System.out.println(livro.nome);
System.out.println(livro.descricao);
System.out.println(livro.valor);
System.out.println(livro.isbn);
}
}
Execu teaclasseparaverasaída!Deveráser:
Java 8 Prático
Novos recursos da linguagem
59.9
978-85-66250-46-6
32

## Página 43

CasadoCódigo Capítulo3. Orientaçãoaobjetos
ClassexObjeto
Umaclasseéapenasummolde. Umaespecificaçãoquedefineparaa
máquina virtual o que um objeto desse tipo deverá ter e como ele deve
secomportar. Nossalivrariapoderátermilharesdelivros(objetos),mas
existirá apenas uma classe
Livro (molde). Cada objeto que criarmos
do tipo Livro terá seus próprios valores, ou seja, cada livro terá o seu
p r ó p riono me,suadescrição ,umvalo reumn úmer odeIS BN .
Nosso CadastroDeLivros está muito simples, com um único livro.
Vamoscriarmaisum,jácomseusatributospreenchidos:
public class CadastroDeLivros {
public static void main(String[] args){
Livro livro = new Livro();
livro.nome = "Java 8 Prático";
livro.descricao = "Novos recursos da linguagem";
livro.valor = 59.90;
livro.isbn = "978-85-66250-46-6" ;
System.out.println(livro.nome);
System.out.println(livro.descricao);
System.out.println(livro.valor);
System.out.println(livro.isbn);
Livro outroLivro = new Livro();
outroLivro.nome = "Lógica de Programação";
outroLivro.descricao = "Crie seus primeiros programas" ;
outroLivro.valor = 59.90;
outroLivro.isbn = "978-85-66250-22-0";
System.out.println(outroLivro.nome);
System.out.println(outroLivro.descricao);
System.out.println(outroLivro.valor);
System.out.println(outroLivro.isbn);
33

## Página 44

3.2. Criandoumnovométodo CasadoCódigo
}
}
Porém, observe que até agora nossa classeLivro só tem atributos, ou
seja,sóguardavalores. Vimosqueumaclassevaialém,elatambémpodeter
comportamentos(métodos).
3.2 Criandoumnovométodo
A todo momento que criamos um novo objeto do tipoLivro, estamos im-
primindo seus valores. Essa é uma necessidade comum entre todos os livros
denossosistema,masdaformacomoestamosfazendo,todahorarepetimos
asmesmas4linhasdecódigo:
System.out.println(livro.nome);
System.out.println(livro.descricao);
System.out.println(livro.valor);
System.out.println(livro.isbn);
A única coisa que mudaéon o m ed av a r i á v e l ,d elivro para
outroLivro.
Pense na seguinte situação, em breve nosso cadastro terá cerca de 100
livros. Paracadalivro,teremos4linhasdecódigoimprimindoosseus4atrib-
utos. Ou seja, teremos 400 linhas de código muito parecidas, praticamente
repetidas.
Essa repetição de código sempre tem um efeito colateral de-
sagradável, que é a dificuldade de manutenção. Quer ver? O que
acontece se adicionarmos um novo atributo no livro, por exemplo a
data de seu lançamento? Para imprimir a data toda vez que criar um
livro, teremos que mudar 100 partes de nosso código, adicionando o
System.out.println(livro.dataDeLancamento).
Nolugardedeixaressalógicadeimpressãodosdadosdolivrotodaespal-
hada, podemos isolar esse comportamento comum entre os livros na classe
Livro!P araisso ,criamosummétodo. Umaformaseria:
34

## Página 45

CasadoCódigo Capítulo3. Orientaçãoaobjetos
void mostrarDetalhes() {
System.out.println(nome);
System.out.println(descricao);
System.out.println(valor);
System.out.println(isbn);
}
Esse método define um comportamento para classeLivro. Repare que
asintaxedeummétodoéumpoucodiferentedoqueestamosacostumados,
suaestruturaé:
tipoDeRetorno nomeDoComportamento() {
// código que será executado
}
Nesse caso, não estamos retornando nada e, sim, apenas executando in-
struções dentro do método, portanto, seu tipo de retorno évoid.E s s a
palavrareservadaindicaqueummétodonãotemretorno.
Ummétodotambémpodetervariáveisdeclaradas,comoporexemplo:
void mostrarDetalhes() {
String mensagem = "Mostrando detalhes do livro " ;
System.out.println(mensagem);
System.out.println(nome);
System.out.println(descricao);
System.out.println(valor);
System.out.println(isbn);
}
Av a r i á v e lmensagem foi declarada dentro do método, logo esse será
seu escopo, ou seja, ela só existirá e poderá ser utilizada dentro do método
mostrarDetalhes.
Nossaclasse Livroficoudestaforma:
public class Livro {
String nome ;
String descricao;
35

## Página 46

3.2. Criandoumnovométodo CasadoCódigo
double valor;
String isbn ;
void mostrarDetalhes() {
String mensagem = "Mostrando detalhes do livro " ;
System.out.println(mensagem);
System.out.println(nome);
System.out.println(descricao);
System.out.println(valor);
System.out.println(isbn);
}
}
Agoraquecadalivropossuiocomportamentodeexibirosseusdetalhes,
podemosremoveraslinhasquefaziamessetrabalhonométodo mainepas-
sarainvocaressenovométodo. Repare:
public class CadastroDeLivros {
public static void main(String[] args){
Livro livro = new Livro();
livro.nome = "Java 8 Prático";
livro.descricao = "Novos recursos da linguagem" ;
livro.valor = 59.90;
livro.isbn = "978-85-66250-46-6" ;
livro.mostrarDetalhes();
Livro outroLivro = new Livro();
outroLivro .nome = "Lógica de Programação";
outroLivro .descricao = "Crie seus primeiros programas" ;
outroLivro .valor = 59.90;
outroLivro .isbn = "978-85-66250-22-0" ;
outroLivro .mostrarDetalhes();
}
}
36

## Página 47

CasadoCódigo Capítulo3. Orientaçãoaobjetos
Ao isolar esse comportamento dentro da classeLivro já tivemos um
ganho evidente. Tivemos que escrever menos linhas em nosso main,o
código ficou com menos repetições pois teve maior reaproveitamento. Mas
essa não é a única vantagem em isolar um comportamento: mesmo que eu
tenha100livroscadastradoseuseométodo
mostrarDetalhes 100vezes,
emquantaspartesdomeucódigoeutereiquemexerparamodificaraforma
comooslivrossãoexibidos? Arespostaé: uma!
Agora que o comportamento está isolado, só precisaremos alterar o
método, um único ponto do nosso código, para refletir a mudança em to-
dos os lugares que o usam. Vamos colocar isso em prática, basta mudar o
método
mostrarDetalhespara:
void mostrarDetalhes() {
System.out.println("Mostrando detalhes do livro " );
System.out.println("Nome: " + nome);
System.out.println("Descrição: " + descricao);
System.out.println("Valor: " + valor);
System.out.println("ISBN: " + isbn);
System.out.println("--");
}
Executeagorao maindaclasse CadastroDeLivros. Semprecisarmu-
darnenhumalinhadeseucódigo,oresultadoserá:
Mostrando detalhes do livro
Nome: Java 8 Prático
Descrição: Novos recursos da linguagem
Valor: 59.9
ISBN: 978-85-66250-46-6
--
Mostrando detalhes do livro
Nome: Lógica de Programação
Descrição: Crie seus primeiros programas
Valor: 59.9
ISBN: 978-85-66250-22-0
--
Nosso código agora tem uma manutenabilidade muito maior! Sempre
devemoscriarmétodosdeformagenéricae reaproveitável,assimserámuito
37

## Página 48

3.3. Objetosparatodososlados! CasadoCódigo
maisfácileprodutivoevoluirocódigonofuturo.
3.3 Objetosparatodososlados!
Falando em evoluir código, precisamos saber mais informações sobre nos-
sos livros. Por exemplo, quem escreveu o livro? Qual o e-mail do autor? E
quandofoiasuadatadepublicação? Todasessasinformaçõessãorelevantes
paranossalivrariaetambémparanossosclientes. Podemosadicionaressase
outrasinformaçõesnaclasse
Livro:
public class Livro {
String nome ;
String descricao;
double valor;
String isbn ;
String nomeDoAutor;
String emailDoAutor;
String cpfDoAutor;
void mostrarDetalhes() {
System.out.println("Mostrando detalhes do livro " );
System.out.println("Nome: " + nome);
System.out.println("Descrição: " + descricao);
System.out.println("Valor: " + valor);
System.out.println("ISBN: " + isbn);
System.out.println("--");
}
}
Mas repare que todas essas novas informações pertencem aoautor do
livro e não necessariamente ao livro. Seautor é um elemento importante
paranossosistema,elepodeedeveserrepresentadocomoumobjeto! Vamos
fazeressaalteração,bastacriaraclasse Autoredeclararseusatributos:
public class Autor {
String nome ;
38

## Página 49

CasadoCódigo Capítulo3. Orientaçãoaobjetos
String email ;
String cpf ;
}
Portanto, podemos adicionar na classe Livro um atributo do tipo
Autor,queacabamosdecriar. Umaclassepodeteroutraclassecomoatrib-
uto, esse é um processo natural conhecido como composição. Nosso código
ficaassim:
public class Livro {
String nome ;
String descricao;
double valor;
String isbn ;
Autor autor ;
void mostrarDetalhes() {
System.out.println("Mostrando detalhes do livro " );
System.out.println("Nome: " + nome);
System.out.println("Descrição: " + descricao);
System.out.println("Valor: " + valor);
System.out.println("ISBN: " + isbn);
System.out.println("--");
}
}
Vamosagoracriaralgunsautoresno CadastroDeLivroseassociarao
seudevidolivro. Umaformadefazerissoseria:
Autor autor = new Autor();
autor.nome = "Rodrigo Turini" ;
autor.email = "rodrigo.turini@caelum.com.br";
autor.cpf = "123.456.789.10";
Nesse código, apenas criamos oautor e populamos os seus atributos.
Agora precisamos associar esse objeto ao seu livro. Podemos simplesmente
fazer:
livro.autor = autor;
39

## Página 50

3.3. Objetosparatodososlados! CasadoCódigo
Vamos fazer isso com os dois livros, nosso código completo deve ficar
parecidocom:
public class CadastroDeLivros {
public static void main(String[] args){
Autor autor = new Autor();
autor.nome = "Rodrigo Turini" ;
autor.email = "rodrigo.turini@caelum.com.br";
autor.cpf = "123.456.789.10";
Livro livro = new Livro();
livro.nome = "Java 8 Prático";
livro.descricao = "Novos recursos da linguagem" ;
livro.valor = 59.90;
livro.isbn = "978-85-66250-46-6" ;
livro.autor = autor;
livro.mostrarDetalhes();
Autor outroAutor = new Autor();
outroAutor .nome = "Paulo Silveira";
outroAutor .email = "paulo.silveira@caelum.com.br" ;
outroAutor .cpf = "123.456.789.10";
Livro outroLivro = new Livro();
outroLivro .nome = "Lógica de Programação";
outroLivro .descricao = "Crie seus primeiros programas" ;
outroLivro .valor = 59.90;
outroLivro .isbn = "978-85-66250-22-0" ;
outroLivro .autor = outroAutor;
outroLivro .mostrarDetalhes();
}
}
40

## Página 51

CasadoCódigo Capítulo3. Orientaçãoaobjetos
Referênciaaobjetos
Éfundamentalperceberque,quandoinstanciamosumnovoobjetocoma
palavrareservada new,um Autorporexemplo,guardamosemsuavariável
umareferênciaparaesseobjeto,enãoseusvalores. Ouseja,avariável autor
nãoguardaovalordeum nome, emaileoutrosatributosdaclasse Autor,
massimumaformadeacessaressesatributosdo autoremmemória. Muito
diferente de quando trabalhamos com tipos primitivos que guardam uma
cópiadovalor.
Aindanãoficouclaro? Observeoseguinteexemplo:
public class ComparandoReferencias {
public static void main(String[] args){
Autor autor = new Autor();
autor.nome = "Rodrigo Turini" ;
autor.email = "rodrigo.turini@caelum.com.br";
autor.cpf = "123.456.789.10";
Autor autor2 = new Autor();
autor2.nome = "Rodrigo Turini" ;
autor2.email = "rodrigo.turini@caelum.com.br";
autor2.cpf = "123.456.789.10";
}
}
Aqui estamos criando dois autores com as mesmas informações, mas o
queaconteceseeucompará-losdaseguinteforma?
if (autor == autor2){
System.out.println("Iguais, mesmo autor!" );
} else {
System.out.println("hein!? Por que diferentes?" );
}
Rodeocódigoparaconferiroresultado! Asaídaserá:
hein!? Por que diferentes?
41

## Página 52

3.3. Objetosparatodososlados! CasadoCódigo
Arespostaésimples,quandocomparamosutilizandoo ==estamoscom-
parando o valor da variável, quesempreseráareferência(endereço)para
ondeencontraroobjetonamemória . E,claro,cadaobjetoquecriamosfica
emumendereçodiferentenamemória.
A imagem a seguir representa os objetos em memória e cada variável de
referência:
Queiralém? Observeessecódigo:
Autor autor = new Autor();
autor.nome = "Rodrigo Turini" ;
Livro livro = new Livro();
livro.autor = autor;
livro.autor.nome = "Guilherme Silveira";
System.out.println(autor.nome);
Estamos criando um autor e adicionando o nomeRodrigo Turini .
Depois disso, criamos um livro e o associamos a esseautor.M a sr e -
pare que em seguida mudamos livro.autor.nome para Guilherme
42

## Página 53

CasadoCódigo Capítulo3. Orientaçãoaobjetos
Silveira. Qual será a saída ao imprimir o nome do autor original (
autor.nome)?
E x e c u t eoc ó d i g op a r av e ras a í d a .S ev o c êe s t a v ae s p e r a n d oRodrigo
Turini,nãofiquedesapontado.
Acontece que, depois de associar a referência deautor ao livro, es-
tamosatribuindoaoatributo livro.autoromesmoendereço(referência)
de memória que tem oautor. Ou seja, das duas formas a seguir estamos
acessandoomesmoobjeto:
autor.nome = "Rodrigo Turini" ;
livro.autor.nome = "Guilherme Silveira";
Achou complicado? Não se preocupe, durante a leitura faremos muitas
atribuições e relacionamentos entre objetos. Afinal, com certeza isso fará
partedeseudiaadia.
Maisemaismétodos
Nossocódigoevoluiu,agoratodo Livropodeterum Autor. Podemos
evoluir nosso método mostrarDetalhes para que ele passe a mostrar as
informaçõesdo autordecadalivro. Umaformadefazerissoseria:
43

## Página 54

3.3. Objetosparatodososlados! CasadoCódigo
void mostrarDetalhes() {
System.out.println("Mostrando detalhes do livro " );
System.out.println("Nome: " + nome);
System.out.println("Descrição: " + descricao);
System.out.println("Valor: " + valor);
System.out.println("ISBN: " + isbn);
System.out.println("Mostrando detalhes do autor " );
System.out.println("Nome: " + autor.nome);
System.out.println("Email: " +autor.email);
System.out.println("CPF: " + autor.cpf);
System.out.println("--");
}
I ssofuncionariabem,masaindanãoéasoluçãoideal.Oproblemadesse
código é que a classeLivro está fazendo mais do que é sua responsabili-
dade. Mostrar as informações deautor deveria ser um comportamento da
classe Autor! E, além disso, o que aconteceria caso nosso próximo objetivo
fossemostrarapenasosdadosdeumautor,semasinformaçõesdeseulivro?
Teríamosquerepetirtodasessasultimaslinhasdecódigo! Veja:
System.out.println("Mostrando detalhes do autor " );
System.out.println("Nome: " + autor.nome);
System.out.println("Email: " +autor.email);
System.out.println("CPF: " + autor.cpf);
Para evitar isso, podemos isolar esse comportamento na classeAutor!
Bastacriarummétodo mostrarDetalhesemseumodelotambém:
public class Autor {
String nome ;
String email ;
String cpf ;
void mostrarDetalhes() {
System.out.println("Mostrando detalhes do autor " );
System.out.println("Nome: " + nome);
System.out.println("Email: " + email);
44

## Página 55

CasadoCódigo Capítulo3. Orientaçãoaobjetos
System.out.println("CPF: " + cpf);
}
}
Pronto! Maisumavezevitamosrepetiçãodecódigousandobemaorien-
taçãoaobjetos. Todaclassepodeedeve,alémdeseusatributos,tercompor-
tamentos bem definidos, isolando suas regras de negócio. Podemos agora
remover essas linhas repetidas do método
mostrarDetalhes da classe
Livroeapenasdelegarachamadadessenovométodo:
void mostrarDetalhes() {
System.out.println("Mostrando detalhes do livro " );
System.out.println("Nome: " + nome);
System.out.println("Descrição: " + descricao);
System.out.println("Valor: " + valor);
System.out.println("ISBN: " + isbn);
autor.mostrarDetalhes();
System.out.println("--");
}
Depois de fazer essas mudanças, vamos executar mais uma vez a classe
CadastroDeLivros. Asaídaserá:
Mostrando detalhes do livro
Nome: Java 8 Prático
Descrição: Novos recursos da linguagem
Valor: 59.9
ISBN: 978-85-66250-46-6
Mostrando detalhes do autor
Nome: Rodrigo Turini
Email: rodrigo.turini@caelum.com.br
CPF: 123.456.789.10
--
Mostrando detalhes do livro
Nome: Lógica de Programação
Descrição: Crie seus primeiros programas
Valor: 59.9
ISBN: 978-85-66250-22-0
Mostrando detalhes do autor
45

## Página 56

3.3. Objetosparatodososlados! CasadoCódigo
Nome: Paulo Silveira
Email: paulo.silveira@caelum.com.br
CPF: 123.456.789.10
--
Métodoscomparâmetro
Depois de instanciado, um objeto do tipoLivro pode precisar ter seu
valor ajustado. É comum aplicar um desconto no preço de um livro, por ex-
emplo. Podemosescreveroseguintecódigoparaaplicar10%dedescontono
valo rdeumlivr o:
public static void main(String[] args){
Livro livro = new Livro();
livro.valor = 59.90;
System.out.println("Valor atual: " + livro.valor);
livro.valor -= livro.valor * 0.1;
System.out.println("Valor com desconto: " + livro.valor);
}
Note que a linha abaixo está calculando a porcentagem de desconto e já
subtraindodovalordolivro.
livro.valor -= livro.valor * 0.1;
Executandoocódigo,teremosasaídaesperada,queé:
Valor atual: 59.9
Valor com desconto: 53.91
Mas esse código não está nem um pouco orientado a objetos, estamos
escrevendo um comportamento do livro direto no métodomain! Já vimos
qual o problema em fazer isso, imagine que existam 100 livros e eu aplique
desconto em todos eles. A nossa lógica de aplicar desconto vai ficar repetida
eespalhadaportodoocódigo.
46

## Página 57

CasadoCódigo Capítulo3. Orientaçãoaobjetos
Como evitar isso? Se aplicar um desconto em seu valor é um comporta-
mento do livro, podemos isolar esse comportamento em um novo método!
Nolugardefazer:
livro.valor -= livro.valor * 0.1;
Podemos criar um métodoaplicaDescontoDe q u er e c e b eu mv a l o r
comoparâmetro. Repare:
livro.aplicaDescontoDe(0.1);
Sim,ummétodopodeedevereceberparâmetrossemprequeforpreciso.
Vejacomoficaasuaimplementação:
public void aplicaDescontoDe(double porcentagem){
valor -= valor * porcentagem;
}
Note que todo parâmetro de método também precisa ter um nome e
tipo definido. Aporcentagem receberá o valor 0.1 (double)q u ef o ip a s -
sadocomoargumentonomomentoemqueométodofoiinvocadoemnosso
método
main.
47

## Página 58

3.3. Objetosparatodososlados! CasadoCódigo
Nomesambíguoseo THIS
Oqueaconteceriaseonomedoparâmetrodométodofosseigualao
nomedoatributodaclasse? Vejacomoficariaonossocódigo:
public void aplicaDescontoDe(double valor ){
valor -= valor * valor;
}
Nolugardeuma porcentagem,chamamosoparâmetrode valor,
assimcomoonomedoatributodaclasse Livro.ComooJavavaisaber
qual valor queremos atualizar? A resposta é: ele não vai. Nosso código
vaisubtrairemultiplicarovalordoparâmetroporelemesmo,jáqueeste
t e mu me s c o p om e n o rq u eoa t r i b u t od ac l a s s e .O us e j a ,m e s m oc o ma
ambiguidadenestecasoocódigovaicompilar,maso
valorconsiderado
seráoquepossuiomenorescopo.
Paraevitaresseproblema,podemosutilizarapalavrareservada this
para mostrar que esse é umatributo da classe. Ainda que seja op-
cional, é sempre uma boa prática usar othis e ma t r i b u t o sp a r ae v i t a r
futuros problemas de ambiguidade e também para deixar claro que este
éumatributodaclasse,enãoumasimplesvariável.
Co misso ,ocódigodenossométodo aplicaDescontoDeficaassim:
public void aplicaDescontoDe(double porcentagem){
this.valor -= this.valor * porcentagem;
}
Eaclasse Livrocompleta:
public class Livro {
String nome ;
String descricao;
double valor;
String isbn ;
Autor autor ;
48

## Página 59

CasadoCódigo Capítulo3. Orientaçãoaobjetos
void mostrarDetalhes() {
System.out.println("Mostrando detalhes do livro " );
System.out.println("Nome: " + nome);
System.out.println("Descrição: " + descricao);
System.out.println("Valor: " + valor);
System.out.println("ISBN: " + isbn);
autor.mostrarDetalhes();
System.out.println("--");
}
public void aplicaDescontoDe(double porcentagem){
this.valor -= this .valor * porcentagem;
}
}
Métodoscomretorno
Nossaclasse Livrojápossuidoismétodos,masosdoissão void. Vimos
que o void representa a ausência de um retorno, mas há situações em que
precisaremos retornar algo. Por exemplo, como saber se um livro tem ou
nãoumautor? Umalternativaseriacriarummétodo temAutor,tendoum
booleancomoretorno. Observeumexemplodeuso:
if(livro.temAutor()) {
System.out.print("O nome do autor desse livro é " );
System.out.println(livro.autor.nome);
}
Aimplementaçãodessemétodoébemsimples,elenãoreceberánenhum
parâmetr oeteráoti poder eto rnoboolean:
boolean temAutor(){
// o que fazer aqui?
}
M a sc o m os a b e rs eoautor do livro existe ou não? Na verdade, é bem
simples: quando um objeto não foi instanciado, ele não tem nenhuma refer-
ência, portanto seu valor será
null. Sabendo disso, tudo o que precisamos
49

## Página 60

3.3. Objetosparatodososlados! CasadoCódigo
fazernocorpodométodoé retornarum boolean,informandoseoatrib-
uto autorédiferentede null. Pararetornarumvalor,utilizamosapalavra
reservada return:
boolean temAutor(){
boolean naoEhNull = this.autor != null;
return naoEhNull;
}
Podemosfazerissodeumaformaaindamaissimples,retornandodireta-
menteaexpressãobooleanasemacriaçãodavariável naoEhNull:
boolean temAutor(){
return this .autor != null;
}
Agora que o Livro ganhou esse novo comportamento, vamos tirar
proveitodeledentrodométodo mostrarDetalhesdaprópriaclasse. Pode-
mos mostrar os detalhes do autor apenas quando ele existir. Uma forma de
fazerissoseria:
void mostrarDetalhes() {
System.out.println("Mostrando detalhes do livro " );
System.out.println("Nome: " + nome);
System.out.println("Descrição: " + descricao);
System.out.println("Valor: " + valor);
System.out.println("ISBN: " + isbn);
if (this.temAutor()) {
autor.mostrarDetalhes();
}
System.out.println("--");
}
Pronto! Aoimprimirosdetalhesdeum livroquenãotemautor,apenas
osdadosdolivroserãoexibidos.
50

## Página 61

CasadoCódigo Capítulo3. Orientaçãoaobjetos
3.4 Entendendoaconstruçãodeumobjeto
Agoraquejáconhecemosumpoucosobreobjetos,podemosentendermelhor
comofuncionaseuprocessodeconstrução. Reparenasintaxeutilizadapara
criarumno vo
Livro:
Livro livro = new Livro();
Quandoescrevemosainstrução Livro() seguidadapalavrareservada
new, estamos pedindo para a JVM procurar a classeLivro ei n v o c a ros e u
construtor,queseparececom:
public Livro(){
}
Um construtorébastanteparecidocomummétodocomum,masele
não é um. Diferente dos métodos, um construtor tem o mesmo nome da
classeenãotemumretornodeclarado.
Mas,senuncaescrevemosesseconstrutor,quemofez? Semprequevocê
nãocriarumco nstru to rparasuasclasses,oco m p ilado rfaráissoparavocê.
Querumaprova? Vamosutilizaroprograma
javapquejávemno JDK
paraverocódigocompilado. Acessepeloterminaldoseusistemaoperacional
apasta
bindeseuprojetoerodeocomando javap Livro . Asaídadeverá
separecercom:
Turini@ ~/Documents/workspace/livro-oo > javap Livro
Compiled from "Livro.java"
public class Livro {
java.lang.String nome;
java.lang.String descricao;
double valor;
java.lang.String isbn;
public Livro();
void mostrarDetalhes();
public void aplicaDescontoDe(double);
}
Noteque,mesmosemcriaroconstrutorvazio,eleestápresenteemnosso
códigocompilado:
51

## Página 62

3.4. Entendendoaconstruçãodeumobjeto CasadoCódigo
public Livro();
E, sim, todo código que estiver declarado dentro do construtor será ex-
ecutado quando um objeto desse tipo for criado. Por exemplo, o código a
seguirimprimeumamensagemsemprequecriarmosumnovo Livro:
public class Livro {
String nome ;
String descricao;
double valor;
String isbn ;
Autor autor ;
public Livro() {
System.out.println("novo livro criado");
}
// demais métodos da classe
}
Para testar, podemos criar alguns livros dentro de um métodomain e
executaressecódigo:
public static void main(String[] args){
Livro livro1 = new Livro ();
Livro livro2 = new Livro ();
Livro livro3 = new Livro ();
Livro livro4 = new Livro ();
}
Comojáéesperado,asaídaserá:
novo livro criado
novo livro criado
novo livro criado
novo livro criado
Agoraquejátemosumconstrutor,ocompiladornãovaicriarmaisnen-
hum. Elesófazissoquandoasuaclassenãotemnenhumconstrutordefinido.
52

## Página 63

CasadoCódigo Capítulo3. Orientaçãoaobjetos
Veremos mais adiante que construtores também podem receber parâmetros
einicializarosatributosdesuasclasses.
3.5 Vantagensdaorientaçãoaobjetos
Vimos neste capitulo apenas algumas das muitas vantagens de se trabalhar
comorientaçãoaobjetos. Observecomatençãoocódigoquecriamos. Você
vai conseguir perceber que uma das grandes diferenças da OO é que temos
umaformafortedecriarconexãoentreinformaçõesefuncionalidades. Além
disso, nosso código fica muito mais organizado e evitamos muita repetição.
O que ganhamos? Um código mais flexível e, com isso, mais fácil de evoluir
eman ter .
Esseésóocomeço,nodecorrerdolivroveremosváriosconceitoserecur-
soscomo encapsulamento,herança,polimorfismoemuitosoutrosquetornam
oparadigmaaindamaisinteressante.
53

## Página 65

Capítulo4
Encapsulamento
4.1 LimitandodescontodoLivro
Quandocriamosométodo aplicaDescontoDe naclasse Livro,nãode-
terminamosaporcentagemtotaldedescontoqueumlivropodeter,masissoé
muitoimportanteparanossaregradenegócio. Umlivropodeternomáximo
30%dedesconto.
Umaformasimplesdeevoluirnossométodoseria:
public boolean aplicaDescontoDe(double porcentagem){
if (porcentagem >0 . 3 ){
return false ;
}
this.valor -= this.valor * porcentagem;
return true ;
}

## Página 66

4.1. LimitandodescontodoLivro CasadoCódigo
Repare que agora estamos retornando um boolean para indicar ao
usuário se o desconto foi aplicado ou não. No momento de usá-lo podemos
fazeralgocomo:
if (!livro.aplicaDescontoDe(0.1)){
System.out.println("Desconto não pode ser maior do que 30%" );
}
Códigoflexívelereaproveitável
O método aplicaDescontoDe poderia, sim, no lugar de retornar
um boolean já imprimir a mensagem de validação do limite de de-
sconto,comoporexemplo:
public void aplicaDescontoDe(double porcentagem){
if (porcentagem >0 . 3 ){
System.out.println("Desconto não pode ser
maior do que 30%" );
}
this.valor -= this.valor * porcentagem;
}
Comisso,nãoserianecessárioescrevero ifemnossométodo main,
mas repare que estamos perdendo a flexibilidade de customizar nos-
sas mensagens. Será que todos que forem utilizar esse método querem
mostrar a mensagemDesconto não pode ser maior do que 30%?Es ee u
quiser mudar esse texto dependendo do usuário ou simplesmente não
mostraramensagemdevalidaçãoemalgummomento?
Lembre-se sempre de evitar deixar informações tão específicas em
seus moldes, além de não sobrecarregá-los com comportamentos que
nãodeveriamserdesuaresponsabilidade.
Pronto! Nossa lógica já está bem definida, agora um livro não pode ter
um desconto maior do que 30%. Mas vamos testá-la para ter certeza. Para
isso ,bastacriaraclasse
RegrasDeDescontocomoseguintecenário:
public class RegrasDeDesconto {
56

## Página 67

CasadoCódigo Capítulo4. Encapsulamento
public static void main(String[] args){
Livro livro = new Livro();
livro.valor = 59.90;
System.out.println("Valor atual: " + livro.valor);
if (!livro.aplicaDescontoDe(0.1)){
System.out.println("Desconto não pode ser
maior do que 30%" );
} else {
System.out.println("Valor com desconto: "
+ livro.valor);
}
}
}
Aoexecutá-la,teremosoresultado:
Valor atual: 59.9
Valor com desconto: 53.91
E,mudandoovalordodescontopara0.4,asaídaserá:
Valor atual: 59.9
Desconto não pode ser maior do que 30%
Excelente! Éexatamenteo comportamentoqueestamosesperando. Mas
há um problema grave. Nada obriga o desenvolvedor a utilizar o método
aplicaDescontoDe, ele poderia perfeitamente escrever o código desta
forma:
public class RegrasDeDesconto {
public static void main(String[] args){
Livro livro = new Livro();
livro.valor = 59.90;
System.out.println("Valor atual: " + livro.valor);
57

## Página 68

4.1. LimitandodescontodoLivro CasadoCódigo
livro.valor -= livro.valor * 0.4;
System.out.println("Valor com desconto: " + livro.valor);
}
}
Ele consegue aplicar o desconto de 40% ou mais, independente de nossa
regradenegócio.
Op r o b lem aéq ueoa tri b u t ovalor daclasse Livro podeser acessado
diretamenteemodificadopelasoutraslógicasdonossosistema. Issoémuito
ruim! Como vimos, ao expor nossos dados, estamos abrindo caminho para
que os objetos possam ser modificados independente das condições verifi-
cadasemseusmétodos.
Apesar de ser um problema muito sério, a solução é bastante simples.
Bastamodificar avisibilidadedoatributo
valor, queatéentãoé default
(padrão). Podemos restringir o acesso para esse atributo para que fique
acessívelapenaspelaprópriaclasse
Livro. Repare:
public class Livro {
private double valor;
// outros atributos e métodos
}
Como estamos utilizando o modificador de visibilidade private,
ninguémmaisalémdaprópriaclasse Livro conseguiráacessaremodificar
essevalor. Portanto,aseguintelinhadaclasse RegrasDeDesconto nãoirá
compilar.
livro.valor -= livro.valor * 0.4;
Oe r r os e r áThe field Livro.valor is not visible . Ótimo,
isso fará com que a única forma de se aplicar um desconto em um livro
seja passando pela nossa regra de negócio, que está isolada no método
aplicaDescontoDe.
58

## Página 69

CasadoCódigo Capítulo4. Encapsulamento
Modificadoresdevisibilidade
Além do private e default (padrão), existem outros modifi-
cadoresdevisibilidade. Sãoeles: public e protected.N om o m e n t o
certo entenderemos a fundo cada um deles, mas tenha em mente desde
jáquetodoselessãodiferentesepossuemregrasbemespecíficas.
4.2 Isolandocomportamentos
Ao alterar a visibilidade do atributovalor para private todos os lugares
queacessavamesseatributopassaramanãocompilar,jáqueapenasaprópria
classe
Livro pode fazer isso. Por exemplo, observe como estávamos pas-
sandoovalordolivro:
livro.valor = 59.90;
Como esse acesso não pode mais ser feito, precisaremos criar um com-
portamento (método) na classeLivro para fazer a atribuição desse valor.
Poderíamoschamá-lode adicionaValor.
livro.adicionaValor(59.90);
Suaimplementaçãoserábemsimples,observe:
void adicionaValor(double valor){
this.valor = valor;
}
Háoutroerrodecompilaçãoqueprecisaremosresolver. Reparenaforma
comoestamosimprimindoovalordo Livro:
System.out.println("Valor atual:" + livro.valor);
Bem, você já pode ter imaginado que a solução será parecida. Preciso
criar um método retornaValor que não receberá nenhum argumento e
r eto rnaráoa trib u todouble valor . Algocomo:
59

## Página 70

4.2. Isolandocomportamentos CasadoCódigo
double retornaValor() {
return this .valor;
}
Ecomoessemétodonãorecebeparâmetros,ousodo thisseráopcional.
Agorapodemosimprimirdessaforma:
System.out.println("Valor atual: " + livro.retornaValor());
Quandousaroprivate?
Isso resolveu o problema dovalor do livro, mas e quanto aos demais
atributos? Quando devemos deixar um atributo de classe com visibilidade
private? Vocêdeveestarpensando: “quandonãoqueroqueninguémacesse
esse atributo diretamente
,eéverdade. Masaquestãoé: quandoeuqueroquealguémacessealgum
atributodeformadireta?
O nome dolivroestácomvisibilidade default,portantoestamosadi-
cionandodaseguinteforma:
livro.nome = "Java 8 Prático";
Considere que depois de alguns meses apareça a necessidade de validar
que a String passada possui ao menos duas letras, caso contrário não será
umnomeválido. Ouseja,nossocódigoprecisaráfazeralgocomo:
livro.nome = "Java 8 Prático";
if(livro.nome.lenght() < 2) {
System.out.println("Nome inválido" );
}
Reparequeométodo lenghtfoiusadopararetornarotamanhodeuma
String. Além desse há diversos outros métodos úteis definidos na classe
String, que conheceremos melhor adiante. O importante agora é perce-
ber que, se acessamos o atributonome diretamente em mil partes de nosso
código,precisaremosreplicaressamudançaemmillugares. Nadafácil.
Já vimos que todo comportamento da classeLivro deveria ser isolado
em um método, assim evitamos repetição de código possibilitando o reúso
60

## Página 71

CasadoCódigo Capítulo4. Encapsulamento
desse método por toda a aplicação. O ideal seria desde o começo ter criado
ummétodo adicionaNomecomessecomportamento.
M a sa pe n a sc ri a rom é t od oadicionaNome não teria resolvido o prob-
lema, percebe? Se a visibilidade do atributo ainda fossedefault,h a v e r i a
duas formas de se adicionar um nome ao livro e nossa lógica de adicionar
nomeaindapoderiaestarespalhadapelaaplicação.
Comogarantirqueissonuncaaconteça? Usando
privatesempre!Todo
atributodeclassedeveserprivado,assimgarantimosqueninguémosacesse
diretamenteevioleasnossasregrasdenegócio.
4.3 Códigoencapsulado
Essamudançaqueiniciamosemnossaclassefazpartedeumconceitomuito
importantedaOOconhecidocomo encapsulamento. Aideiaésimplesmente
escondertodososatributosdesuasclasses(deixando-os
private)e encap-
sularseus comportamentos em métodos. Além disso, encapsular é esconder
comofuncionamsuasregrasdenegócio,osseusmétodos.
Um bom termômetro para descobrir se o seu código está bem encapsu-
ladoéfazendoasduasperguntas:
• Oqueessecódigofaz?
• Comoessecódigofaz?
Vejaporexemploquandoaplicamosodescontoacessandooatributodi-
retamente:
livro.valor -= livro.valor * 0.4;
Olhandoparaessecódigo,nósconseguimosresponderasduasperguntas:
oq u eec o m oéf e i t o ,m a semumcódigobemencapsuladovocêsódeveria
conseguirresponderaprimeira .
Observeestesegundoexemplo:
livro.aplicaDescontoDe(0.1);
61

## Página 72

4.4. GetterseSetters CasadoCódigo
Reparequeficaclarooqueométodo aplicaDescontoDeestáfazendo,
masapenasolhandoparaelenãoconseguimosresponder comoistoseráfeito.
Seemalgummomentonofuturoresolvermosmandarume-mailsempreque
algumdescontoforaplicado,nãoprecisaremosmudarmilharesdepartesde
nosso código, mas sim esse único método que está bem encapsulado. Por-
tanto, oencapsulamentodeixanossocódigomuitomaispassíveldemu-
danças.
Interfacedaclasse
Osmétodospúblicosexistentesemsuaclassesãocomumentechama-
dos deinterface da classe, afinal em um código encapsulado eles são a
únicamaneiradevocêinteragircomosobjetosdessaclasse.
Pensaremalgumcontextodomundorealpodeajudaraentenderen-
capsulamento e interface da classe. Por exemplo, quando você vai escr-
everumtextoemumcomputador,oqueimportaéoteclado(ainterface
quevocêusaparafazerisso). Poucoimporta comoelefuncionainterna-
mente. Quandovocêmudardecomputadorousimplesmentedetipode
teclado,nãoprecisaráreaprenderausarumteclado.
Por mais diferente que eles funcionem internamente, isso não fará
diferença para um usuário final. Ninguém precisa desmontar a lateral
de um computador e manualmente mudar os circuitos para que o com-
putador possa interpretar os sinais enviados e mostrar os dados na tela,
afinal esse comportamento está muito bem encapsulado na interface do
teclado.
4.4 GetterseSetters
Se todos os atributos de nossas classes foremprivate, precisaremos criar
um método sempre que quisermos que alguém consiga adicionar um valor
a oa t r i b u t oeom e s m oq u a n d oq u i s e r m o sq u ealguém consiga ler e ex-
ibir este valor. Assim como fizemos com os métodos
adicionaValor e
retornaValor.
A convenção de nome para esses dois métodos é utilizar o prefixoget
62

## Página 73

CasadoCódigo Capítulo4. Encapsulamento
(pegar) e set (atribuir). Por exemplo, no lugar de chamar os métodos de
adicionaValor e retornaValor, podemos chamá-los desetValor e
getValor,respectivamente.
Nossocódigoficaassim:
public class Livro {
private double valor;
// demais atributos e métodos
public double getValor() {
return valor;
}
public void setValor(double valor){
this.valor = valor ;
}
}
R e p a r eq u eom é t o d oget n ã or e c e b en e n h u mp a r â m e t r oea p e n a sr e -
tornaoatributo,enquantoo setsemprerecebeumparâmetrocomomesmo
tipodoqueoatributoqueseráatualizado.
Eclipse:GGASeAutocomplete
Criar getters e setters pode parecer um processo trabalhoso,
mas, por ser um padrão de código muito comum, as principaisIDEsd o
mercadopossuematalhosetemplatesquenosajudamafazerisso.
Noeclipse,vocêpodefazerissodeformamuitoprodutivautilizando
o atalho Control + 3 e depois digitando ggas. Repare que essas
são as iniciais do comandoGenerate Getters and Setters .S e -
lecionandoestaopçãovocêpoderáescolherparaquaisatributoscriaros
métodoseclicarem Finish.
Tudopronto,oEclipsegerouocódigotodopravocê!
63

## Página 74

4.4. GetterseSetters CasadoCódigo
Os getters e setters possibilitam o acesso dos atributos de forma
controlada. Masémuitoimportanteperceberquenemtodoatributodeveter
um gettere setter,vocêsódevecriaressesmétodosquandohouveruma
realnecessidade. HáumpostdoPauloSilveiramuitointeressanteilustrando
essasituação:
http://blog.caelum.com.br/2006/09/14/nao-aprender-oo-getters-e-setters/
Depoisdecriaros
getterse settersnecessários,nossaclasse Livro
deveficarassim:
public class Livro {
private String nome ;
private String descricao;
private double valor;
private String isbn ;
private Autor autor ;
// demais métodos omitidos
public double getValor() {
return valor;
}
public void setValor(double valor){
this.valor = valor ;
}
public String getNome() {
return nome;
}
public void setNome(String nome ){
this.nome = nome;
}
public String getDescricao() {
return descricao;
}
64

## Página 75

CasadoCódigo Capítulo4. Encapsulamento
public void setDescricao(String descricao){
this.descricao = descricao;
}
public String getIsbn() {
return isbn;
}
public void setIsbn(String isbn ){
this.isbn = isbn;
}
public Autor getAutor() {
return autor;
}
public void setAutor(Autor autor ){
this.autor = autor ;
}
}
Precisamosfazeromesmoparanossaclasse Autor:
public class Autor {
private String nome;
private String email ;
private String cpf;
// demais métodos omitidos
public String getNome() {
return nome;
}
public void setNome(String nome ){
this.nome = nome;
}
65

## Página 76

4.4. GetterseSetters CasadoCódigo
public String getEmail() {
return email;
}
public void setEmail(String email ){
this.email = email;
}
public String getCpf() {
return cpf;
}
public void setCpf(String cpf){
this.cpf = cpf;
}
}
E,porfim,seránecessáriomodificaraclasse CadastroDeLivrospara
quedeixedeacessarosatributosdiretamente. Seucódigofinaldeveficarpare-
cidocom:
public class CadastroDeLivros {
public static void main(String[] args){
Autor autor = new Autor();
autor.setNome("Rodrigo Turini" );
autor.setEmail("rodrigo.turini@caelum.com.br" );
autor.setCpf("123.456.789.10" );
Livro livro = new Livro();
livro.setNome("Java 8 Prático");
livro.setDescricao("Novos recursos da linguagem");
livro.setValor(59.90);
livro.setIsbn("978-85-66250-46-6" );
livro.setAutor(autor);
66

## Página 77

CasadoCódigo Capítulo4. Encapsulamento
livro.mostrarDetalhes();
Autor outroAutor = new Autor();
outroAutor.setNome("Paulo Silveira");
outroAutor.setEmail("paulo.silveira@caelum.com.br" );
outroAutor.setCpf("123.456.789.10");
Livro outroLivro = new Livro();
outroLivro.setNome("Lógica de Programação");
outroLivro.setDescricao("Crie seus primeiros programas" );
outroLivro.setValor(59.90);
outroLivro.setIsbn("978-85-66250-22-0" );
outroLivro.setAutor(outroAutor);
outroLivro.mostrarDetalhes();
}
}
4.5 Definindodependênciaspeloconstrutor
Autoréumatributoobrigatório
Agora que nosso código já está bem encapsulado, precisamos atender outra
necessidadedenossalivraria. Todo Livroprecisaterum Autor.I s s oéb e m
simples: assim como já está sendo feito, logo após criar um livro, podemos
associá-loaoseuautorpelométodo
setAutor:
Autor autor = new Autor();
autor.setNome("Rodrigo Turini" );
// set dos outros atributos
Livro livro = new Livro();
// set dos outros atributos
livro.setAutor(autor);
Issojáresolveoproblema,masháumaquestão. Dessaforma,poralguns
instantes o Livro existe em memória sem ter umAutor relacionado. E
67

## Página 78

4.5. Definindodependênciaspeloconstrutor CasadoCódigo
esseneméopiordosproblemas,oqueaconteceráseesquecermosdechamar
o método setAutor? A resposta é: nada. Ou seja, da forma como nosso
códigoestáescrito,umlivropodeexistirsemseuautor.
Como resolver isso? Bem, como já vimos, toda classe tem um
construtor. Aindaqueeunãotenhadeclarado,ocompiladorfaráissopara
mim. Oqueaindanãovimoséqueconstrutorespodemreceberparâmetros.
Com isso, podemos obrigar a passagem de alguns valores logo no momento
decriaçãodenossosobjetos.
Vamoscriarumconstrutornaclasse
Livroquedevereceberum Autor
comoparâmetro. Seucódigodeveficarassim:
public Livro(Autor autor ){
this.autor = autor;
}
Reparequeeleficoucomaresponsabilidadedométodo setAutor,que
éatribuiro autordoparâmetr oaoa trib u todaclasse.
A partir do momento em que criamos esse construtor com parâmetro
na classe Livro, o compilador não criará mais o construtordefault(vazio).
Portanto,oseguintecódigonãocompila:
Livro livro = new Livro();
Seoúnicoconstrutorexistentenaclasserecebeum Autor,aúnicaforma
de fazer esse código compilar e criar umLivro será passando umAutor
comoargumento. Veja:
Autor autor = new Autor();
autor.setNome("Rodrigo Turini" );
// set dos outros atributos
Livro livro = new Livro(autor);
// set dos outros atributos
Claro, há situações em que queremos deixar as duas formas válidas, ou
seja, queremos criar umLivro passando ou não umAutor.P a r aq u ei s s o
funcionasse, precisaríamos adicionar na classeLivro um novo construtor
quenãorecebenenhumargumento. Seucódigoficariaassim:
68

## Página 79

CasadoCódigo Capítulo4. Encapsulamento
public class Livro {
private String nome;
private String descricao;
private double valor;
private String isbn;
private Autor autor ;
public Livro( Autor autor ){
this.autor = autor ;
}
public Livro() {
}
// setters, getters e outros métodos
}
Uma classe pode, sim, ter mais de umconstrutor, isso é conhecido
como uma sobrecarga (overloaded) de construtor. Mas, assim como nos de-
mais métodos, isso funcionará contanto que os construtores não tenham a
mesmaquantidadedeparâmetro. Porexemplo,seeutentarfazer:
public Livro() {
}
public Livro() {
System.out.println("novo livro criado");
}
Esse código não compilará, afinal, quando alguém fizernew Livro()
qualdosconstrutoresseriachamado?
Comonossaregradenegócioexigeum Autorparacada Livro,vamos
manter apenas o construtor com parâmetro. Para isso, precisaremos mudar
as nossas classes que criam um novoLivro para atender essa condição. A
classe CadastroDeLivrosdeveficarassim:
public class CadastroDeLivros {
69

## Página 80

4.5. Definindodependênciaspeloconstrutor CasadoCódigo
public static void main(String[] args){
Autor autor = new Autor();
autor.setNome("Rodrigo Turini" );
autor.setEmail("rodrigo.turini@caelum.com.br" );
autor.setCpf("123.456.789.10" );
Livro livro = new Livro( autor);
livro.setNome("Java 8 Prático");
livro.setDescricao("Novos recursos da linguagem");
livro.setValor(59.90);
livro.setIsbn("978-85-66250-46-6" );
livro.mostrarDetalhes();
Autor outroAutor = new Autor();
outroAutor.setNome("Paulo Silveira");
outroAutor.setEmail("paulo.silveira@caelum.com.br" );
outroAutor.setCpf("123.456.789.10");
Livro outroLivro = new Livro(outroAutor);
outroLivro.setNome("Lógica de Programação");
outroLivro.setDescricao("Crie seus primeiros programas" );
outroLivro.setValor(59.90);
outroLivro.setIsbn("978-85-66250-22-0" );
outroLivro.mostrarDetalhes();
}
}
70

## Página 81

CasadoCódigo Capítulo4. Encapsulamento
MantemosounãoométodosetAutor?
Seoco nstru to rjáa trib ui uoAutor dolivro,precisamosmanterum
setter para esse atributo? Isso vai depender de nossa necessidade, claro.
Pode ser que faça bastante sentido para nossa livraria modificar o autor
de um livro depois que ele foi criado. Mas fique atento! Você só deve
mantero setterseelerealmentefornecessário,lembre-sedaimportância
demantersuasrotinas encapsuladas.
Inicializandoatributosdaclasse
Por fim, outro ponto que precisamos resolver em nossa livraria
é relacionado ao número de ISBN de nossos livros. Em nosso
CadastroDeLivros, sempre que criamos um Livro, já atribuímos
seu número deISBN, mas normalmente esse identificador pode demorar
algunsdiasparaficarpronto.
Repare qual será o resultado do métodomostrarDetalhes quando o
ISBN nãoestiverpreenchido:
Mostrando detalhes do livro
Nome: Java 8 Prático
Descrição: Novos recursos da linguagem
Valor: 59.9
ISBN: null
Mostrando detalhes do autor
Nome: Rodrigo Turini
Email: rodrigo.turini@caelum.com.br
CPF: 123.456.789.10
Ov a l o rnull será impresso. Isso acontece pois, diferente dostipos
primitivos, que sempre possuem um valor padrão (default), objetos como a
Stringnãopossuem,portanto,antesdesereminicializadasterãosuarefer-
ênciaiguala null.
Esseéovalo rdefault decadatipoprimitivo:
71

## Página 82

4.5. Definindodependênciaspeloconstrutor CasadoCódigo
Outrousobemcomumdeum construtoréparainicializaçãodeatrib-
utos,comoocasodo ISBN.Parafornecerumvalorpadrãoparaesteatributo,
poderíamossimplesmenteinicializá-lono construtordaclasse:
public Livro(Autor autor ){
this.autor = autor;
this.isbn = "000-00-00000-00-0" ;
}
Nesse caso, aomostrarDetalhes deum Livro semISBN,teremosa
saída:
Mostrando detalhes do livro
Nome:Java 8 Prático
Descrição:Novos recursos da linguagem
Valor:59.9
72

## Página 83

CasadoCódigo Capítulo4. Encapsulamento
ISBN: 000-00-00000-00-0
Mostrando detalhes do autor
Nome: Rodrigo Turini
Email: rodrigo.turini@caelum.com.br
CPF: 123.456.789.10
Delegandoparaoutrosconstrutores
Repare que, se a classeLivro também tivesse um construtor sem
argumentos,comoaseguir:
public Livro(Autor autor ){
this.autor = autor ;
this.isbn = "000-00-00000-00-0" ;
}
public Livro() {
}
Ov a l o rd eISBNsó seria inicializado quando o construtor com um
Autorfossechamado. Pararesolverisso,vocêpodeencadearachamada
dosconstrutoresutilizandoapalavrareservada this,comoaseguir:
public Livro(Autor autor ){
this();
this.autor = autor ;
}
public Livro() {
this.isbn = "000-00-00000-00-0" ;
}
73

## Página 85

Capítulo5
Herançaepolimorfismo
5.1 Trabalhandocomlivrosdigitais
Por causa da sua praticidade e fácil portabilidade, muitos leitores preferem
livros digitais (e-books) aos livros físicos. Nossa livraria não pode ficar para
trás,portanto,passaremosatrabalharcomessenovotipodelivro.
Mas, afinal, como podemos diferenciar um Livro impresso de um
Ebook? Umaformasimplesdefazerissoseriaadicionandoumatributoque
defineotipodelivro. Poderiasimplesmenteserum boolean,ma r ca ndose
umlivroéimpressoounão. Repare:
public class Livro {
private String nome;
private String descricao;
private double valor;

## Página 86

5.1. Trabalhandocomlivrosdigitais CasadoCódigo
private String isbn ;
private Autor autor ;
private boolean impresso;
public Livro(Autor autor ){
this.autor = autor;
this.isbn = "000-00-00000-00-0" ;
this.impresso = true;
}
// outros métodos da classe
}
Notequeemnossoconstrutorjádefinimosumvalorpadrãoparaoatrib-
uto impresso.T o d oLivroquenãotenhaovalorde impressodefinido
seráconsideradoumlivroimpresso.
Essaéumaformasimplesderesolveroproblemaetalvezatépossaaten-
derbemasnossasnecessidades, masoproblemadessaabordageméqueum
Ebook temalgunscomportamentosbastantediferentesdoqueumlivroim-
presso. Por exemplo, o métodoaplicaDescontoDe da classe Livro at-
ualmentelimitaaporcentagemdedescontoem30%.
public boolean aplicaDescontoDe(double porcentagem){
if (porcentagem > 0.3) {
return false ;
}
this.valor -= this.valor * porcentagem;
return true ;
}
Masquandosetratadeum Ebook,aregraéumpoucodiferente: pode-
mos aplicar no máximo 15% de desconto. Podemos resolver esse problema
adicionandomaisumacondiçãoaométodo:
public boolean aplicaDescontoDe(double porcentagem){
if (porcentagem > 0.3) {
return false ;
} else if (!this.impresso && porcentagem > 0.15) {
return false ;
76

## Página 87

CasadoCódigo Capítulo5. Herançaepolimorfismo
}
this.valor -= this.valor * porcentagem;
return true ;
}
Agora nosso código funciona como esperado, mas está um pouco mais
verboso e difícil de entender. O grande problema aqui é que, a cada método
cujaregrasejadiferente,teremosquecolocarumnovo ifparecidocomesse,
isso sem contar que novos tipos deLivro podem aparecer e tornar nosso
códigoaindamaiscomplicadoecheiodecondicionais. Devemossemprees-
cr evernossocódigopensandoemco moserásuaevol uçãonofu tur o .
Além disso, existem alguns comportamentos e atributos que só servem
para um
Ebook.U md e l e séowatermark (marca d’água). Essa é a forma
de identificar discretamente o nome e e-mail do dono daquele livro digital,
no rmalmen tenor oda pédaspáginas.
Se
Ebookéumelementoimportante,possuicomportamentoseatributos
específicos, ele deveria ser representado como umObjeto! Podemos criar
umaclasse Ebookdefinindoosatributosecomportamentosespecíficosdesse
novotipo.
public class Ebook {
private String nome;
private String descricao;
private double valor;
private String isbn;
private Autor autor ;
private String waterMark;
public void setWaterMark(String waterMark){
this.waterMark = waterMark;
}
public String getWaterMark() {
return waterMark;
}
77

## Página 88

5.1. Trabalhandocomlivrosdigitais CasadoCódigo
// getters, setters e outros métodos
}
Nossocódigojáestáumpoucomaisinteressante,afinalnãoestamosmais
sobrecarregando a classe Livro com atributos e métodos que serão uti-
lizados apenas quando o tipo do livro for umebook. Mas há muito código
repetidoaqui: alémdoscomportamentosdo Ebook,temostodososatribu-
tosemétodosjáescritosnaclasse Livro.
Paraevitartodaessarepetiçãodecódigo,podemosensinaraocompilador
queo Ebookéumtipode Livro,ouseja,alémdeseusprópriosatributose
métodos,essaclassepossuitudooqueum Livrotem. Parafazeristo,basta
Ebookdizernadeclaraçãodaclassequeela éum Livro,queéuma extensão
dessaclasse:
public class Ebook extends Livro {
private String waterMark;
public Ebook(Autor autor){
super(autor );
}
public void setWaterMark(String waterMark ){
this.waterMark = waterMark;
}
public String getWaterMark() {
return waterMark;
}
}
78

## Página 89

CasadoCódigo Capítulo5. Herançaepolimorfismo
delegateconstructor
Comoaclasse Livrotinhaumconstrutorobrigandoapassagemde
um Autor como parâmetro, ao herdar de umLivro,ac l a s s eEbook
também herdou essa responsabilidade. Repare que utilizamos a palavra
superparadelegararesponsabilidadeparaa superclassequejátemesse
comportamentobemdefinido.
public Ebook(Autor autor ){
super(autor );
}
Ao utilizar a palavra reservada extends, estamos dizendo que um
Ebook (subclasse)herda t u d ooq u eac l a s s eLivro (superclasse) tem. Por-
tanto, mesmo sem ter nenhum desses métodos declarados diretamente na
classe Ebook,podemosexecutaroseguintecódigosemnenhumproblema:
Ebook ebook = new Ebook();
ebok.setNome("Java 8 Prático");
Como a classe Livro tem ossetters para o atributo nome declarados,
um Ebooktambémterá.
Herançamúltipla
Uma regra importante da herança em Java é que nossas classes só
podem herdar diretamente deuma classe pai. Ou seja, não há herança
múltipla como na linguagemC++. Mas sim, uma classe pode herdar de
uma classe que herda de outra e assim por diante. Você pode encadear
aherançadesuasclasses,noen tan to ,ver emosmaisàfr en teq ueessaes-
tratégia não é muito interessante por aumentar de mais oacoplamento
entresuasclasses.
79

## Página 90

5.2. Reescrevendométodosdasuperclasse CasadoCódigo
5.2 Reescrevendométodosdasuperclasse
Agora que temos uma forma forte de se representar umEbook, podemos
criarummétodo aplicaDescontoDecomodescontomáximode15%. As-
sim, evitamos aqueleif que verificava se umLivro era impresso ou não.
Na classe Livroométododeveficarassim:
public boolean aplicaDescontoDe(double porcentagem){
if (porcentagem > 0.3) {
return false ;
}
this.valor -= this.valor * porcentagem;
return true ;
}
M a sn ol u g a rd eac l a s s eEbook herdar esse comportamento (que deve
serdiferenteparaela),podemosreescrevê-locomoaseguir:
public class Ebook extends Livro {
private String waterMark;
public Ebook(Autor autor ){
super(autor );
}
public boolean aplicaDescontoDe(double porcentagem){
if (porcentagem > 0.15) {
return false ;
}
this.valor -= this .valor * porcentagem;
return true ;
}
// get e set do watermark
}
Por mais que um Ebook seja um Livro, quando alguém chamar o
método aplicaDescontoDe, o desconto será de 15%, e não de 30% com
oestádefinidonaclassepai.
80

## Página 91

CasadoCódigo Capítulo5. Herançaepolimorfismo
AJVMsemprevaiprocurarométodoprimeironoobjetoquefoiinstanci-
adoeapenasquandonãoencontrarprocuraráemsua superclasse. Vocêpode
verumexemploaqui:
81

## Página 92

5.2. Reescrevendométodosdasuperclasse CasadoCódigo
@Override
Opcionalmente podemos marcar os métodos reescritos com a ano-
tação @Overrride. Uma anotação é apenas uma marcação, como um
post-it com uma observação importante sobre o local anotado. Asan-
notations surgiram no Java 1.5, e têm um papel bastante importante na
maior parte das bibliotecas mais atuais da linguagem. Por questões de
compatibilidade, o uso do@Override é facultativo, mas é bastante in-
teressanteanotarosseusmétodosdessaforma, jáque, comisso, ocom-
piladornosajudaráavalidarqueessemétodoérealmenteumareescrita.
@Override
public boolean aplicaDescontoDe(double porcentagem){
if (porcentagem > 0.15) {
return false ;
}
this.valor -= this.valor * porcentagem;
return true ;
}
Ao anotar nosso método com@Override, o código não compilará
casoessemétodonãoexistanaclassepai( superclasse).
Antesdetestaressamudança,precisamosfazerumaultimaalteraçãopara
queessemétodoco m p ile.
Como a visibilidade do atributovalor da classe Livro é private,
alinhaqueoacessadiretamentedométodo aplicaDescontoDe daclasse
Ebooknãovaifuncionar. Afinal,umatributo privatesópodeseracessado
pelaprópriaclasse,nemmesmoasclassesfilhas( subclasses)podemviolaressa
regra.
Para que o código funcione, precisamos aumentar essa visibilidade, mas
já conhecemos o problema de deixar os atributospublic.U m aa l t e r n a t i v a
é modificar a visibilidade dos atributos da classeLivro para protected,
queéummeiotermoen tr e publice private.
82

## Página 93

CasadoCódigo Capítulo5. Herançaepolimorfismo
A visibilidade protected deixará os atributos visíveis também para as
classesfilhas,masnormalmenteevitamosutilizaressemodificadordevisibil-
idade porque ele acaba tendo mais algumas exceções que afrouxam o nosso
encapsulamento. Conheceremos mais sobre oprotected adiante, mas
desdejávamosevitaressaalternativa.
Umaformabeminteressanteesimplesderesolveroproblemaéutilizando
a interface da classepai, seus próprios métodos. Por exemplo, no lugar de
acessaroatributodiretamente,poderíamosutilizarosmétodos getValore
setValorcomoaseguir:
@Override
public boolean aplicaDescontoDe(double porcentagem){
if (porcentagem > 0.15) {
return false ;
}
double desconto = this.getValor() * porcentagem ;
this.setValor(this.getValor() - desconto);
return true ;
}
Dessaforma,nãoperderemosnemumpoucodo encapsulamento da
classe Livro!Q u a n t om a i sv o c êe s t u d a res eh a b i t u a rc o mao r i e n t a ç ã oa
objetos,maisvocêperceberáquegarantiro encapsulamentodasclassesé
fundamental. Ainda que um pouco, quando liberamos acesso dos atributos
dasuperclasseparasuasclassesfilhas,estamosviolandoo encapsulamento
dessaclasse.
83

## Página 94

5.2. Reescrevendométodosdasuperclasse CasadoCódigo
thisousuper?
No método aplicaDescontoDe da classe Ebook, chamamos o
getter e setter do atributo valor utilizando a palavra reservada
this. Uma outra forma de fazer isso seria utilizando osuper. Assim,
estamosdeixandoclaroqueométodoinvocadoédaclassepai. Existem
situaçõesemqueémuitointeressanteutilizar super,co monestecaso:
@Override
public boolean aplicaDescontoDe(double porcentagem){
if (porcentagem > 0.15) {
return false ;
}
return super .aplicaDescontoDe(porcentagem);
}
Repareque,logoapósfazeranossacondição,estamosdelegandopara
alógicadométodo aplicaDescontoDedaclassepai. Comisso,evita-
mosrepetiralógicaquejáestádefinidana superclasse. Masoqueacon-
teceriasenolugarde supertivéssemosutilizadoo this?
Nessecaso,ométodo aplicaDescontoDedaclasse Ebookestaria
chamandoelemesmo! Entraríamosemum looping infinito.
Pronto, chegou a hora de testar esse código para garantir que tudo está
funcionando como esperado. Abra (ou crie, caso já não exista) a classe
RegrasDeDescontoeescrevaoseguintecódigo:
public class RegrasDeDesconto {
public static void main(String[] args){
Autor autor = new Autor();
autor.setNome("Rodrigo Turini" );
Livro livro = new Livro( autor);
livro.setValor(59.90);
84

## Página 95

CasadoCódigo Capítulo5. Herançaepolimorfismo
if (!livro.aplicaDescontoDe(0.3)){
System.out.println("Desconto no livro não pode ser
maior do que 30%" );
} else {
System.out.println("Valor do livro com desconto: "
+ livro.getValor());
}
Ebook ebook = new Ebook(autor);
ebook.setValor(29.90);
if (!ebook.aplicaDescontoDe(0.3)){
System.out.println("Desconto no ebook não pode ser
maior do que 15%" );
} else {
System.out.println("Valor do ebook com desconto: "
+ ebook.getValor());
}
}
}
Asaídaserá:
Valor do livro com desconto: 41.93
Desconto no ebook não pode ser maior do que 15%
Mudando o valor de desconto passado para o e-book de 0.3 para 0.15, o
resultadoserá:
Valor do livro com desconto: 41.93
Valor do ebook com desconto: 25.415
Ótimo ,cadati podeli vr ot ev eas uar egradedesco n t odevida men t ea p li-
cada.
5.3 RegrasprópriasdeumLivroFisico
Deixamos os comportamentos específicos de um Ebook bem
encapsulados em sua classe, mas repare que há um problema em
85

## Página 96

5.3. RegrasprópriasdeumLivroFisico CasadoCódigo
nossaherança. Emquelugardevemoscolocarosmétodosquefazemsentido
apenas para um livro físico? Por exemplo, todo livro físico possui uma taxa
de impressão. Podemos criar um
getTaxaImpressao para nos retornar
essevalor,comoaseguir:
public double getTaxaImpressao() {
return this .getValor() * 0.05;
}
Mas ondeadicionamos esse método? Se adicionarmosna classeLivro,
o Ebookherdaráessecomportamentoquenãodeveriaexistiremseutipo.
Mais uma vez entramos na regra: se um elemento é importante e tem
regras específicas, ele deve ser representado como um objeto. Podemos
criar uma nova classe em nosso projeto, para representar tudo o que um
LivroFisicotemecomoelesecomporta. Observe:
public class LivroFisico extends Livro {
public LivroFisico(Autor autor ){
super(autor);
}
public double getTaxaImpressao() {
return this .getValor() * 0.05;
}
}
Dessa maneira, também temos uma forma forte de representar um
LivroFisico, bem encapsulada e que não causa nenhum efeito colateral
nosdemaisfilhosde Livro,co moo Ebook.
86

## Página 97

CasadoCódigo Capítulo5. Herançaepolimorfismo
Umanovaclasseacadatipodelivro?
Umareaçãobemcomumdequemestáaprendendoorientaçãoaob-
jetos é perguntar:e n t ã oe ud e v oc r i a ru m an o v ac l a s s ep r ac a d at i p od e
livro?. A resposta é sim. E você logo perceberá que isso não é um prob-
lema.
É muito mais interessante trabalhar com classes menores, que rep-
resentam bem os seus tipos e possuem suas regras específicas bem en-
capsuladas,doquetrabalharcomumaúnicaclassecarregandotodaessa
responsabilidade.
Poderíamos sim ter uma única classe
Livro que tivesse todos os
comportamentosdeum LivroFisico,um Ebookedosdemaistipos
quepodemaparecer. Masimagineotamanhodessaclasse,aquantidade
demétodose
ifsencadeadosparalidarcomasdiferentesregrasdecada
tipode Livro.Aclasseseriaeno rmeebemdifícildeman ter .
Lembre-sesempreque Javaéumalinguagemfortementetipada ,você
pode e deve criar objetos para representar cada tipo de elemento da sua
aplicação.
5.4 VendendodiferentestiposdeLivro
Para dar mais um passo em nossa aplicação, criaremos agora uma classe
RegistroDeVendas,porenquantocomummétodo maineoseguintecon-
teúdo:
public class RegistroDeVendas {
public static void main(String[] args){
Autor autor = new Autor();
autor.setNome("Mauricio Aniche");
LivroFisico fisico = new LivroFisico(autor);
fisico.setNome("Test-Driven Development" );
87

## Página 98

5.4. VendendodiferentestiposdeLivro CasadoCódigo
Ebook ebook = new Ebook( autor);
ebook.setNome("Test-Driven Development" );
}
}
Repare que criamos um LivroFisico eu m Ebook com o mesmo
Autor. Nosso próximo passo será adicionar esses dois elementos em um
CarrinhoDeCompras. Ocódigodeveficarparecidocomeste:
CarrinhoDeCompras carrinho = new CarrinhoDeCompras();
carrinho.adiciona(fisico);
carrinho.adiciona(ebook);
V a m o sa g o r ac r i a rac l a s s eCarrinhoDeCompras e seu método
adiciona. Comovamosadicionar LivroFisicosetambém Ebooks,uma
formadefazerissoseriacriandodoismétodos adiciona,umparacadatipo
de Livro(umasobrecarga):
public class CarrinhoDeCompras {
public void adiciona(LivroFisico livro){
System.out.println("Adicionando: " + livro );
}
public void adiciona(Ebook livro ){
System.out.println("Adicionando: " + livro );
}
}
Esse código funcionaria sem nenhum problema, mas repare que está
muito repetido. Além disso, a cada novo tipo deLivro, precisaremos criar
um novo método adiciona q u er e c e b ae s s et i p oc o m op a r â m e t r o ,oq u e
seriaumtantotrabalhosoedifícildemanter.
Paraevitarisso, podemosutilizarumrecursodalinguagembastanteútil
e poderoso. Como existe uma herança envolvida, podemos dizer que tanto
um LivroFisicocomoum Ebooksãofilhos( extensões)daclasse Livro.
Poderíamoscriarumúnicométodo adiciona,querecebeum Livro (su-
perclasse)co moparâmetr o:
88

## Página 100

5.4. VendendodiferentestiposdeLivro CasadoCódigo
Nãoestamostransformandoobjetos
Lembre-se que uma variável guarda uma referência para um objeto,
e não um objeto em si. Até agora, estávamos sempre declarando um
Ebookco moti poEbook. Repare:
Ebook ebook = new Ebook();
Mas, comovimos, também podemosdizerqueum Ebook édoti po
Livro,afinaleleherda( éum) Livro.
Livro ebook = new Ebook();
Maséfundamentalperceberquenãoestamostransformandoesseob-
jeto. Secriamosum Ebook,eleseráum Ebookeponto. Estamosapenas
nosreferenciandoaelecomoum Livro,umaabstração.
Perceba que, como estamos referenciando o parâmetro passado para o
método adicionadaclasse CarrinhoDeComprascomoum Livro,ape-
nas os métodos presentes na classeLivro poderão ser invocados sem que
umerrodecompilaçãoocorra.
Paraficarmaisclaro,aindaquepassandoumobjetodotipo Ebookpara
o adiciona,aotentarinvocarseumétodo getWaterMark,oseguinteerro
decompilaçãoocorrerá:
The method getWaterMark() is undefined for the type Livro
Faz sentido. Para que isso funcione, precisaríamos fazer umcasting
moldandooparâmetro livroparaoti po Ebook:
public void adiciona(Livro livro ){
Ebook ebook =( Ebook) livro;
ebook.getWaterMark();
// restante do código omitido
}
Isso vai funcionar muito bem, contanto que o valor passado de fato seja
do tipo Ebook. Isso é um tanto perigoso, pois podemos muito bem passar
90

## Página 101

CasadoCódigo Capítulo5. Herançaepolimorfismo
um LivroFisico como argumento. Neste caso até seria possível fazer um
ifparavalidarqueoobjetopassadoéumainstânciade Ebook,masdeixaria
deserumavantagemusar polimorfismoaqui.
5.5 Acumulandototaldecompras
O CarrinhoDeComprasprecisaacumularovalortotalqueestásendocom-
prado. Podemosfazerissodeumaformabemsimples,adicionandoumatrib-
uto totaleincrementandocomo valordo Livroacadaadição.
public void adiciona(Livro livro ){
System.out.println("Adicionando: " + livro);
total += livro.getValor();
}
Além disso, antes de acumular o total da compra, o métodoadiciona
aplicaráumdescontode5%paracadalivroadicionado:
public void adiciona(Livro livro ){
System.out.println("Adicionando: " + livro);
livro.aplicaDescontoDe(0.05);
total += livro.getValor();
}
Aofinal,nossaclasse CarrinhoDeComprasdeveficarassim:
public class CarrinhoDeCompras {
private double total;
public void adiciona(Livro livro ){
System.out.println("Adicionando: " + livro);
livro.aplicaDescontoDe(0.05);
total += livro.getValor();
}
public double getTotal() {
return total;
}
}
91

## Página 104

5.6. Herançaoucomposição? CasadoCódigo
Como esperado, apenas o desconto doLivroFisico foi aplicado, pois
ométodo aplicaDescontoDedaclasse Ebooklimitaodescontoa15%.
Portanto,nãoimportaaformacomonósnosreferenciamosanossosob-
jetos,nofimométodoexecutadosempreseráodele.
5.6 Herançaoucomposição?
Entenderemos melhor o problema mais à frente, massempre que possível
p r o c u r ef a v o r e c e rou s od ac o m p o s i ç ã oe n t r ec l a s s e sn ol u g a rd eu t i l i z a rh e r -
ança. Veremosqueousodaherançaaumentabastanteoacoplamentodesuas
classesedealgumaformasempreacabacomprometendoo encapsulamento.
Tudoissoserámelhoraprofundadonospróximoscapítulos,masdesdejá
você pode se interessar em ler o seguinte artigo no qualJames Gosling,c o n -
sideradopaidoJava,falasobreoassunto:
http://www.artima.com/intv/gosling3P.html
94

## Página 105

Capítulo6
Classeabstrata
6.1 QualotipodecadaLivro?
Agora que temos uma forma forte de representar os diferentes tipos de
Livro,podemosnosexpressarbemaofazerumavenda:
Ebook ebook = new Ebook(autor);
ebook.setNome("CDI");
carrinho.adiciona(ebook);
Além de Ebook, também temos umLivroFisico, que já provou ser
um objeto diferente por ter comportamentos diferentes. Mas o que estamos
vendendoquandofazemos newemum Livro?
Livro livro = new Livro(autor);
livro.setNome("CDI");

## Página 106

6.1. QualotipodecadaLivro? CasadoCódigo
carrinho.adiciona(livro);
A fi n a l ,oq u eéu mLivro agora? Um Ebook ou um LivroFisico?
Na verdade, nenhum dos dois. UmLivro é apenas umaabstraçãode tudo
queosdiferentestiposdelivrodevemter( herdar)emnossalivraria.
Ao fazer uma venda, queremos saber ao certo o tipo de livro que está
sendo vendido, nunca deveríamos permitir a venda de umLivro, mas sim
desuas subclasses.
Para nossa sorte, há uma forma bem simples de impedir que a classe
Livro sejainstanciadaeutilizadadessa forma: podemossimplesmenteadi-
cionaremsuadeclaraçãoomodificador abstract. Repare:
public abstract class Livro {
// continuação do código
}
A partir do momento em que tornamos nossa classe abstrata, o compi-
lador vai impedir que qualquer código tente instanciar umLivro. Por ex-
emplo,emnosso CadastroDeLivros:
Livro livro = new Livro(autor);
livro.setNome("Java 8 Prático");
livro.setDescricao("Novos recursos da linguagem" );
livro.setValor(59.90);
livro.setIsbn("978-85-66250-46-6" );
Oerrodecompilaçãoapresentadoserá:
Cannot instantiate the type Livro
Bemclar o ,nãoacha?N ãosepodemaiscriarum Livroepontofinal.
96

## Página 107

CasadoCódigo Ca p í tulo6. Classeabstra ta
Porqueprecisamosdaclasse LIVRO ?
Afinal, para que serve a classe Livro, se não podemos mais
instanciá-la? Lembre-se que essa classe idealiza tudo o que umLivro
tem,elaaindaestásendomuitoútilisolandotodososatributosecompor-
tamentos que são um padrão entre os diferentes tipos de livro. A classe
p a s s aas e r v i re x c l u s i v a m e n t ep a r aherançae polimorfismo, que são re-
cursosbastanteúteisepoderosos.
Todo livro criado agora precisa ter seu tipo bem definido, portanto pre-
cisaremosmudartodasaspartesdenossocódigoquecriavaum Livropara
usarumadesuasclassesfilhas. Aclasse CadastroDeLivros,porexemplo,
ficaráassim:
public class CadastroDeLivros {
public static void main(String[] args){
Autor autor = new Autor();
autor.setNome("Rodrigo Turini" );
autor.setEmail("rodrigo.turini@caelum.com.br" );
autor.setCpf("123.456.789.10");
Livro livro = new LivroFisico(autor);
livro.setNome("Java 8 Prático");
livro.setDescricao("Novos recursos da linguagem" );
livro.setValor(59.90);
livro.setIsbn("978-85-66250-46-6" );
livro.mostrarDetalhes();
// outros livros cadastrados
}
}
Apesar de não poder instanciar uma classe abstrata, você ainda pode (e
muitasvezesdeve)usá-lacomoreferência. Comonométodo adicionado
97

## Página 108

6.2. Minilivronãotemdesconto! CasadoCódigo
CarrinhoDeCompras:
public void adiciona(Livro livro ){
System.out.println("Adicionando: " + livro);
livro.aplicaDescontoDe(0.16);
total += livro.getValor();
}
Repare que ainda estamos recebendo umLivro como parâmetro para
continuar usando opolimorfismo. Isso é perfeitamente possível, afinal um
Ebook eu m LivroFisico são filhos de Livro,p o r t a n t oh e r d a mos e u
tipo.
Quandoumaclassedeveserabstrata?
Quandovocêforplanejarahierarquiaeherançadesuasclasses,você
verá que algumas classes são bastante específicas e que jamais deveriam
ser instanciadas. A classeAnimal pod ese rv i s tac o m ou me x e m p l o .O
queexatamenteéum Animal? Poderiaserum Leao,um Pinguimou
qualqueroutro Animal doplaneta. Essaclassepodedefinirtudooque
todos os animais têm em comum, mas cada tipo deAnimal tem suas
particularidadesedeveserrepresentadodeumaformaprópria.
6.2 Minilivronãotemdesconto!
Agora que Livro é abstrato, podemos adicionar um novo tipo deLivro
em nossa livraria. Será umMiniLivro, representando um livro mais enx-
utoecomalgumasparticularidadesquelogoconheceremos. Vamoscomeçar
criandoessano vaclasse:
public class MiniLivro extends Livro {
public MiniLivro(Autor autor ){
super(autor );
}
}
98

## Página 109

CasadoCódigo Ca p í tulo6. Classeabstra ta
O que acontecerá quando modificarmos o código da classe
RegrasDeDesconto criando um MiniLivro onde anteriormente
criávamos um Livro? Vamos fazer essa alteração e executá-la para ver o
resultado. Aclassedeveficarassim:
public class RegrasDeDesconto {
public static void main(String[] args){
Autor autor = new Autor();
autor.setNome("Rodrigo Turini" );
Livro livro = new MiniLivro(autor);
livro.setValor(39.90);
if (!livro.aplicaDescontoDe(0.3)){
System.out.println("Desconto no livro não pode
ser maior do que 30%" );
} else {
System.out.println("Valor do livro com desconto: "
+ livro.getValor());
}
// outros descontos omitidos
}
}
Aoexecutaressecódigooretornoserá:
aplicando desconto no Livro
Valor do livro com desconto: 27.93
Observequefoiaplicadoumdescontode30%novalordolivro,masum
MiniLivronãopodeterdesconto! Elejáéumlivrocompreçopromocional,
nãopodemospermitirquenenhumoutrovalordedescontosejaaplicado.
Aocriarum MiniLivro,mesmosemdefinirmosisso,elejápoderiater
um desconto de até 30% pois herdou esse comportamento da classeLivro.
Há uma forma simples de resolver o problema: poderíamos reescrever o
método aplicaDescontoDe da classe MiniLivro para sempre retornar
false. Seucódigoficariaassim:
99

## Página 110

6.2. Minilivronãotemdesconto! CasadoCódigo
public class MiniLivro extends Livro {
public MiniLivro(Autor autor ){
super(autor);
}
@Override
public boolean aplicaDescontoDe(double porcentagem){
return false ;
}
}
Essa solução resolveria o problema, mas é um tanto sensível. Será que
qualquerpessoaquecriasseessenovotipode Livro selembrariademodi-
ficarodescontopadrão? Provavelmentenão.
É bastante improvável que um novo desenvolvedor, ou mesmo quem
tenha criado a regra, lembre-se deste detalhe sempre que um novo tipo de
livroforcriado. Dependerdamemóriahumananuncaéumaboaestratégia.
Nolugardeprecisarsobrescreverométodosemprequehouverdesconto,
poderíamosinverterasituaçãodeixandoocomportamentopadrãodo Livro
abstrato retornar false. Dessa forma, por padrão nenhum livro terá de-
sconto. Sobrescrevemosessaregraapenasquandofornecessário.
Nossocódigoficariaassim:
public abstract class Livro {
private String nome ;
private String descricao;
private double valor;
private String isbn ;
private Autor autor ;
public Livro(Autor autor ){
this.autor = autor ;
this.isbn = "000-00-00000-00-0" ;
}
public boolean aplicaDescontoDe(double porcentagem){
100

## Página 111

CasadoCódigo Ca p í tulo6. Classeabstra ta
return false ;
}
// outros métodos, getters e setters
}
A go raqueométodoaplicaDescontoDedaclassepaisem p r er eto rna
false,p r e c i s a r e m o sm u d a rac l a s s eLivroFisico para permitir até 30%
dedesconto:
public class LivroFisico extends Livro {
public LivroFisico(Autor autor ){
super(autor );
}
public double getTaxaImpressao() {
return this .getValor() * 0.05;
}
public boolean aplicaDescontoDe(double porcentagem){
if (porcentagem > 0.3) {
return false ;
}
double desconto = getValor() * porcentagem;
setValor(getValor() - desconto);
System.out.println("aplicando desconto no LivroFisico" );
return true ;
}
}
Nossaclasse MiniLivronãoprecisarámaissobrescreverométodo. Seu
códigopodeficarassim:
public class MiniLivro extends Livro {
public MiniLivro(Autor autor ){
super(autor );
}
}
101

## Página 112

6.3. Métodoabstrato CasadoCódigo
Essa estratégia é um pouco mais interessante, afinal não permitiremos
maisdescontodoqueumaclassedeveriater. Oproblemaéqueprecisaremos
lembrardereescreveressecomportamentoemtodonovotipode Livroque
tenhadesconto. Aindacorremosoriscodeesquecere,destavez,nãopermitir
descontoparaum
Livroquetenhadireito.
6.3 Métodoabstrato
Se cada novo Livro terá uma estratégia de desconto diferente, ou seja, se
nãoháumdescontopadrãoentretodosostiposdelivro,poderíamossimples-
menteapagaressemétododessaclasseabstrataeescrevê-loapenasnasclasses
quedevemterdesconto. Oproblemadissoéqueperderíamoso polimorfismo,
afinal,seométodonãoestiverpresentenatipo
Livro,oseguintecódigonão
funcionará:
public void adiciona(Livro livro ){
System.out.println("Adicionando: " + livro);
livro.aplicaDescontoDe(0.16);
total += livro.getValor();
}
Nemtodo Livroteráométodo aplicaDescontoDe,nãohánenhuma
garantiadisso.
Podemos resolver o problema de uma forma mais efetiva. Toda classe
abstra ta,comoéocasodanossaclasse Livro,podeter métodosabstratos.
Toda classe filha (subclasse) concreta (não abstrata) é obrigada a escrever os
métodos abstratos da classe pai (superclasse), caso contrário seu código não
compilará.
Para tornar o métodoaplicaDescontoDe abstrato na classeLivro,
bastaadicionaromodificador abstractemsuadeclaraçãoeremovertodo
ocorpo,colocandoapenasumpontoevírgula. Repare:
public abstract class Livro {
private String nome ;
private String descricao;
private double valor;
102

## Página 113

CasadoCódigo Ca p í tulo6. Classeabstra ta
private String isbn;
private Autor autor ;
public Livro( Autor autor ){
this.autor = autor ;
this.isbn = "000-00-00000-00-0" ;
}
public abstract boolean aplicaDescontoDe(double porcentagem);
// outros métodos, getters e setters
}
Apenas classes abstratas podem ter métodos abstratos. Afinal, se al-
guéminvocasseométodo aplicaDescontoDedaclasse Livro,qualseria
oresultado? Nãohánenhumaimplementaçãonele,portantoelenãopoderia
serexecutado.
Apartirdomomentoemquetornamosométodo aplicaDescontoDe
abstrato, todas as classes filhas precisam escrevê-lo. Por esse motivo, a classe
MiniLivrovaiparardecompilar. Oerroserá:
The type MiniLivro must implement the inherited abstract method
Livro.aplicaDescontoDe(double)
Paraquetudofuncioneaclasseprecisaráficarassim:
public class MiniLivro extends Livro {
public MiniLivro(Autor autor ){
super(autor );
}
@Override
public boolean aplicaDescontoDe(double porcentagem){
return false ;
}
}
Ainda não é uma solução perfeita, estamos sendo obrigados a escrever
esse método na classeMiniLivro mesmo que ela não possua essa regra de
103

## Página 114

6.4. Relembrandoalgumasregras CasadoCódigo
desconto. Mas a grande vantagem é que eliminamos totalmente a possibili-
dade de esquecer de definir esse comportamento em novas implementações
daclasse
Livro. Apartirdeagora,todofilhode Livrologoquandocriado
jáprecisarádefinirqualasuaregradedesconto,casocontrárioocódigonão
compila.
6.4 Relembrandoalgumasregras
Não é nem um pouco complicado trabalhar com classes abstratas, mas exis-
temalgumasregrasqueprecisamserrespeitadas. Apenaspararelembrar,são
elas:
• Umaclassepodeserabstratasemternenhummétodoabstrato. Apar-
tirdomomentoemqueelasetornarabstrata,nenhumcódigopoderá
maisinstanciá-la.
• Sevocêdeclararummétodoabstrato ,precisarátornaraclasseabstrata
também! Vocênãopodetermétodosabstratosemumaclassequenão
éabstrata.
• Uma classe abstrata pode ter métodos abstratos e não abstratos (con-
cretos).
• T odaclassefilha(subclasse)precisaimplementarosmétodosabstratos
daclassepai( superclasse). Anãoserqueelatambémsejaabstrata.
104

## Página 115

Capítulo7
Interface
Além dos mais diversos tipos deLivros, nossa livraria também trabalhará
com Revistas e futuramente outros produtos. Podemos criar uma nova
classepararepresentá-la,comoaseguir:
public class Revista {
private String nome;
private String descricao;
private double valor;
private Editora editora;
// getters e setters
public boolean aplicaDescontoDe(double porcentagem){
if (porcentagem > 0.1) {

## Página 116

CasadoCódigo
return false ;
}
double desconto = getValor() * porcentagem;
setValor( getValor() - desconto);
return true ;
}
}
Repareque,alémdeum nome, descricaoe valor,umarevistatam-
bé mpo s s u iu m ar e g r ad ed e sc o n t oeéc o m po s tape l ac l a s seEditora.E s s a
éumaoutraclassebastantesimples:
public class Editora {
private String nomeFantasia;
private String razaoSocial;
private String cnpj ;
// getters e setters
}
Precisamos agora evoluir nosso CarrinhoDeCompras para que seja
possível,alémde Livros,adicionar Revistas. Umasoluçãoseriaduplicar
seumétodo adiciona:
public class CarrinhoDeCompras {
private double total;
public void adiciona(Livro livro ){
System.out.println("Adicionando: " + livro);
livro.aplicaDescontoDe(0.05);
total += livro.getValor();
}
public void adiciona(Revista revista ){
System.out.println("Adicionando: " + revista);
revista.aplicaDescontoDe(0.05);
total += revista.getValor();
106

## Página 117

CasadoCódigo Capítulo7. Interface
}
public double getTotal() {
return total;
}
}
Mas note como os dois métodos ficaram bastante parecidos, há muita
repetiçãodecódigo! Alémdisso,paracadanovoprodutoprecisaríamoscriar
umnovométodo,oquetornariatrabalhosaaevoluçãodessaclasse.
Poderíamos fazer a classeRevista herdar de Livro,d em o d oq u eo
polimorfismoseria aplicável e teríamos um único método adiciona. Mas ao
fazerissotoda Revistateriaum Autor, ISBNalémdosdemaisatributose
comportamentosquesóseaplicamparaos Livros,umaverdadeirabagunça.
Sim, podemos criar um nível a mais na hierarquia de nossas classes
adicionando a classe Produto, assim Livro e Revista herdariam de
Produto e poderíamos utilizar esse tipo nopolimorfismo. A hierarquia de
nossasclassesseria:
107

## Página 118

7.1. O contrato Produto CasadoCódigo
Ograndeproblemadessaabordageméqueaumentariademaiso acopla-
mento entre as classes, ou seja, o quanto uma classe depende da outra. A
herança cria uma relação muito forte entre as classes. Ao mudar a classe
Produto, por exemplo, todas assubclasses (e tambémsubclasses das sub-
classes)seriaminfluenciadas.
E se eu quiser aplicar a mudança apenas para algumas classes? Teríamos
quesobrescreveressenovocomportamentodeumaformadesnecessáriaem
todas as outras, assim como fizemos com a classe
MiniLivro. Mesmo sem
existir desconto para essa classe, ela foi obrigada a sobrescrever o método
aplicaDescontoDeparaapenasretornar false.
Com o passar do tempo, o uso da herança faz com que nossas classes
fiquemcadavezmaisacopladaseissodificultasuaevolução.
7.1 OcontratoProduto
EmJava,háumaoutraformaparasetirarproveitodetodososbenefíciosdo
polimorfismosem ter que acoplar tanto as suas classes com vários níveis de
herança. Vocêpodeestabelecerumfatoremcomumentreasclasses,criando
umaespéciedecontrato.
Paraessecontrato,nãoimportaaformacomoseráimplementado,aúnica
coisa que importa é que seus métodos (cláusulas) sejam implementados de
alguma forma. Isso lembra algo? Sim, é bastante parecido com ummétodo
abstratocujocorpovocêsódefinena superclasseparaquetodasas subclasses
herdemaobrigaçãodeimplementá-lo.
EssetipodecontratoJavaéconhecidocomo Interface.
Nãosetratadeumainterfacegráfica
É muito comum confundir no inicio, mas não estamos falando de
umainterfacegráficadeusuário( GUI).Tambémnãoestamosfalandoda
interface da classe, seus métodos públicos. Você perceberá no decorrer
docapítuloquesetratadeumrecursodiferente,um contratoJava.
Podemos criar uma interface Produto, que por enquanto terá um
único método abstrato estabelecendo que todo produto deve ter o método
108

## Página 119

CasadoCódigo Capítulo7. Interface
getValor. Uma interface se parece bastante com uma classe abstrata que
tenhaapenasmétodosabstratos,masnolugardedeclará-lacomoumaclasse,
utilizamosapalavrareservada interface:
public interface Produto {
public abstract double getValor();
}
Comotodométodo semcorpo deumainterfaceéabstrato,ousodomod-
ificador abstract é opcional. Não precisamos também adicionar o modi-
ficador public,poisseusmétodostambémsãopúblicosporpadrão. Pode-
mossimplificaraescritadainterface Produtodeixandoapenas:
public interface Produto {
double getValor();
}
Umainterfacenãopodeteratributose,atéaversão1.7dalinguagem,tam-
bém não pode ter nenhum método concreto, ou seja, com implementação.
Veremosque,apartirdoJava1.8,issomudouumpouco.
Podemosagorafazercomquetodasasclassesqueidealizam produtosde
nossa livraria assinem o contrato
Produto. Para fazer isso, basta adicionar
a palavra-chave implements seguida do nome da interface que deve ser
implementadanadeclaraçãodasclasses,veja:
public abstract class Livro implements Produto {
// atributos e métodos omitidos
}
public class Revista implements Produto {
// atributos e métodos omitidos
}
Como todas essas classes já possuem o métodogetValor declarado,
você não perceberá nenhuma diferença. Nosso código passa a funcionar
como esperado. Mas é importante perceber que se apagarmos o método
109

## Página 120

7.1. O contrato Produto CasadoCódigo
getValor a classe deixará de compilar, afinal toda classe que implementa
ainterface Produtoéobrigadaaimplementarseusmétodosabstratos.
Vejaquecomainterfaceodiagramadenossasclassesficaassim:
Como todos que implementam umainterface podem ser referenci-
ados por este tipo, podemos usarpolimorfismo com interfaces. Por exem-
plo,nométodo adicionado CarrinhoDeCompraspodemosreceberum
Produtocomoparâmetro:
public void adiciona(Produto produto ){
System.out.println("Adicionando: " + produto);
produto.aplicaDescontoDe(0.16);
total += produto.getValor();
}
Opolimorfismofuncionará,masoproblemadessecódigoéquenemtodo
Produtotemométodo aplicaDescontoDe,masapenasosfilhosdaclasse
110

## Página 121

CasadoCódigo Capítulo7. Interface
Livro. Sim, poderíamos mover o método abstratoaplicaDescontoDe
paraainterface Produto, massenemtodososprodutostêmumdesconto,
devemos evitar isso. Por enquanto, removeremos esse desconto, mas logo
veremosumaformamaisinteressantederesolveroproblema. Nossométodo
deveficarassim:
public void adiciona(Produto produto ){
System.out.println("Adicionando: " + produto);
total += produto.getValor();
}
Rodeaclasse RegistroDeVendasparaverquetudoestáfuncionando
comoesperado. Aclassecontinuaassim:
public class RegistroDeVendas {
public static void main(String[] args){
Autor autor = new Autor();
autor.setNome("Mauricio Aniche");
LivroFisico fisico = new LivroFisico(autor);
fisico.setNome("Test-Driven Development" );
fisico.setValor(59.90);
Ebook ebook = new Ebook(autor);
ebook.setNome("Test-Driven Development" );
ebook.setValor(29.90);
CarrinhoDeCompras carrinho = new CarrinhoDeCompras();
carrinho.adiciona(fisico);
carrinho.adiciona(ebook);
System.out.println("Total " + carrinho.getTotal());
}
}
Aoexecutá-la,oresultadoserá:
111

## Página 122

7.2. DiminuindoacoplamentocomInterfaces CasadoCódigo
Adicionado: LivroFisico@4f23c55
Adicionado: Ebook@21a33b44
Total 89.8
7.2 DiminuindoacoplamentocomInterfaces
Ousodainterfacejánosajudouaresolveroproblemade polimorfismodenos-
sos produtos. Agora há uma forma simples e flexível para representar qual-
quer Produto denossalivraria. Masaindaprecisamosresolveroproblema
dométodo aplicaDescontoDe.
Aoadicionaressemétodoabstratonaclasse Livro, obrigamos todas as
suas subclassesa implementá-lo, mas não é bem isso que precisamos. Essa
soluçãodeixadeserinteressantequandonemtodosos Livrostenhamesse
comportamento, como é o caso doMiniLivro, que não pode ter um de-
sconto.
Outra questão é que apenas os filhos da classe Livros têm essa
obrigação, sendo que uma Revista também deve possuir o método
aplicaDescontoDe. Podemos diminuir esse acoplamento de uma
forma bem simples, criando uma nova interface! Vamos chamá-la de
Promocional:
public interface Promocional {
boolean aplicaDescontoDe(double porcentagem);
}
Agora podemos remover o métodoaplicaDescontoDe abstrato da
classe Livro e dizer que apenas as classes promocionais, que possuem de-
sconto,implementamessanovainterface:
public class LivroFisico extends Livro implements Promocional {
// atributos e métodos omitidos
}
public class Ebook extends Livro implements Promocional {
// atributos e métodos omitidos
}
112

## Página 123

CasadoCódigo Capítulo7. Interface
public class Revista implements Produto, Promocional {
// atributos e métodos omitidos
}
Assimcomopodemosassinardiversoscontratosaolongodenossasvidas,
umaclassetambémpodeimplementardiversasinterfaces. Reparequeaclasse
Revista agora implementa duas interfaces, utilizando uma vírgula em sua
declaração.
A grande vantagem de trabalhar com interfaces é que apenas as classes
que a implementam são obrigadas a implementar seus métodos, portanto,
se eu não quero queMiniLivro tenha desconto, basta não implementar a
interface Promocional.
Observe como a estrutura de nossas classes está mais flexível. Qualquer
novaclassepodepassaraserpromocional,semherdarnenhumaoutraobri-
gação. O mesmo ocorre com o
Produto: tudo que uma classe precisa fazer
para ter o tipoProduto é assinar esse contrato e implementar seu método
getValor,semnenhumefeitocolateralindesejado.
113

## Página 125

CasadoCódigo Capítulo7. Interface
Adicionado: Ebook@21a33b44
Total 83.81
Mais à frente veremos que diversosdefault methodsforam adicionados
nas interfacesda API do Java. Foi possível evoluir seu comportamento sem
quebrar compatibilidade com suas implementações já existentes e bastante
utilizadas.
Interfacefuncional
Umainterfacenãoprecisaterumúnicométodoabstrato,masessaéuma
estrutura bem comum. Normalmente, trabalhar com interfaces menores é
umaestratégiainteressante,afinaltemosmaisflexibilidade. Sealguémimple-
mentar aquela interface é porque realmente precisa do comportamento que
elaestabelece.
ApartirdoJ a va8,asinterfaces queobedecemessaregradeterumúnico
métodoabstratopodemserchamadasde
interface funcional . Mesmo
semteressepropósito,nossasinterfaces Produtoe Promocionalpossuem
essaestruturaeseenquadramnoperfildeumainterfacefuncional.
Logoveremosquea interfacefuncional éachaveparaoutrosnovosrecur-
sosdalinguagem,quesãoasexpressões lambdaemethodreferences.
Aanotação @FunctionalInterface
Podemosmarcarumainterfacecomofuncionalexplicitamente,paraque
of a t od ee l as e ru m ainterface funcionalnão seja pela simples coincidên-
cia de ter um único método abstrato. Para fazer isso, usamos a anotação
@FuncionalInterface:
@FunctionalInterface
public interface Promocional {
boolean aplicaDescontoDe(double porcentagem);
default boolean aplicaDescontoDe10Porcento() {
return aplicaDescontoDe(0.1);
}
}
115

## Página 126

7.3. NovasregrasdainterfacenoJava8 CasadoCódigo
Ao fazer essa alteração, note que nada mudou. Ela continua com-
pilando e, executando nossas classes de teste, o resultado será o mesmo.
Mas diferente do caso de não termos anotado nossa interface com
@FunctionalInterface, tente alterá-la da seguinte forma, adicionando
umnovométodo abstrato:
@FunctionalInterface
public interface Promocional {
boolean aplicaDescontoDe(double porcentagem);
boolean naoSouMaisUmaInterfaceFuncional();
default boolean aplicaDescontoDe10Porcento() {
return aplicaDescontoDe(0.1);
}
}
Ocódigodeixarádecompilar,comaseguintemensagem:
Invalid '@FunctionalInterface' annotation;
Promocional is not a functional interface
Ea ot e n t a rc o m p i l a rf o r ad oE c l i p s e ,c o mojavac como fizemos no
primeirocapítulo,amensagemseriaaindamaisexplicativa:
java: Unexpected @FunctionalInterface annotation
Promocional is not a functional interface
multiple non-overriding abstract methods found
in interface Promocional
Outro detalhe que você já deve ter percebido é que podemos ter um ou
maisdefaultmethodsdeclaradosemnossainterfaceeissonãoinfluenciaofato
de ela ser ou não umainterface funcional , apenas métodos abstratos
sãoconsiderados.
HerançamúltiplanoJava8?
Métodos defaults foram adicionados para permitir que interfaces
evoluamsemquebrarcódigoexistente . Essa frase foi bastante repetida na
116

## Página 127

CasadoCódigo Capítulo7. Interface
lista de discussão da especificação dessa nova versão da linguagem. Eles não
foramcriadosparapermitiralgumavariaçãodeherançamúltiplaoude mix-
ins. Vale lembrar que há uma série de restrições para esses métodos. Em
especial, eles não podem acessar atributos de instância, até porque isso não
existe em interfaces! Em outras palavras, não há herança múltipla ou com-
partilhamentodeestado.
117

## Página 129

Capítulo8
Pacotes
8.1 Organizandonossasclasses
Por enquanto nossas classes estão todas em um mesmo arquivo, dentro da
pasta src.C o n f o r m eop r o j e t ov a ie v o l u i n d o ,m a i sem a i sc l a s s e ss ã oc r i -
adas e fica cada vez mais difícil manter a organização de nosso projeto. Mas
organizaçãonãoseráoúnicoproblemaaqui.
Comopassardotempo,trabalharemoscomclassesdeterceiros( bibliote-
cas) e classes da própriaAPI da linguagem, o que torna ainda maior o risco
decriarmosumaclassecomonomeigualaoutraexistenteemalgumadessas
bibliotecas.
Querumexemplo? Poderíamoscriarumaclassequesechama
Date:
class Date {
private int dia;

## Página 130

8.1. Organizandonossasclasses CasadoCódigo
private int mes;
private int ano;
// getters e setters
}
Em um métodomain qualquer de nossa aplicação, poderíamos instan-
ciaressaclassefazendo:
public static void main(String[] args){
Date date = new Date();
}
Mas na API do Java, já existe uma classe chamadaDate.C o m o a
JVM sabe diferenciar quando precisamos instanciar a nossa classeDate ou
quando deve ser oDate do Java? A resposta é bem simples: em Java classes
sãoagru padaspo rpaco tes(packages).
O pacote da classeDate da API do Java com certeza será diferente do
pacotedenossaclasse,portanto,paratiraraambiguidadepodemosinstanciar
aclassepeloseunomecompleto ,comoporexemplo:
public static void main(String[] args){
java.util.Date date = new java.util.Date();
}
Estranho? Não se preocupe, vamos melhorar a legibilidade desse código
logo. Masreparequeonomecompletodaclasse,ou fullyqualifiedname como
é comumente chamado, é composto pornome do pacote.( p o n t o )nome
daclasse . Neste caso, o nome do pacote onde se encontra a classeDate é
java.util.
120

## Página 131

CasadoCódigo Capítulo8. Pacotes
PacotesdaAPIdoJava
Além do java.util, existem diversos pacotes com classes essen-
ciais para nosso dia a dia trabalhando com Java. Algumas classes como
a String e System não precisam ser escritas com o nome completo,
poisfazempartedopacote java.lang,queéopacotepadrãodoJava.
No próximo capítulo estudaremos a fundo o pacotejava.lang e, no
decorrerdolivro,veremosalgunsdosdemaisprincipaispacotesda API.
Observandoocódigoaseguirvocêjádevetersentidoumaperdadeleg-
ibilidade:
java.util.Date date = new java.util.Date();
Podemos simplificar esse código adicionando umimport com o nome
completodaclassenoiníciodenossoarquivo. Repare:
import java.util.Date;
class Teste {
public static void main(String[] args){
Date date = new Date();
}
}
Sóseránecessárioescreveronomecompletodaclassesemum importse
poralgumarazãovocêprecisarusarduasclassescomomesmonomedentro
do mesmo arquivo. Nesse caso, você poderá fazer o
import de uma delas,
masutilizaronomecompletoquandoforsereferiràoutra.
A essa altura você já deve ter se perguntado: Qual o nome completo da
nossaclasse Date? Comonóscriamosaclassediretamentenodiretório src,
elanãotemumpacotedefinido. Dizemosqueelaestáno defaultpackage.
Isso não é nada bom, toda classe deve ser agrupada em pacotes. Isso,
além de ajudar na organização de nossos projetos, ajudará quando houver
umaambiguidadedenomes.
121

## Página 132

8.1. Organizandonossasclasses CasadoCódigo
NomenclaturapadrãodospacotesJava
Porpadrão,umpacoteemJavasempre:
• éescritoemletraminúscula( lowercase);
• deveserumnomededomínio,iniciadocom com,edu,govetc.
É muito natural que o pacote seja o seu domínio (ou da
empresa), como br.com.casadocodigo, br.com.alura ou
br.com.caelum. O link a seguir fala um pouco mais sobre as con-
vençõesdeno mencla turasdepaco tesdoJ a va:
http://www.oracle.com/technetwork/java/codeconventions-135099.
html
Agora que já sabemos disso, podemos criar alguns pacotes para melhor
organizar o nosso projeto. No Eclipse isso pode ser feito pelo menuFile
> New > Package ,ouutilizandooatalho Control + N eselecionandoa
opção package.
Aprincípio,criaremosospacotes:
• br.com.casadocodigo.livraria para as classes Autor e
Editora;
• br.com.casadocodigo.livraria.produtos para as interfaces
Promocional, Produtoesuasimplementações;
• br.com.casadocodigo.livraria.teste para nossas classes ex-
ecutáveis,ouseja,quepossuemométodo main.
Antes de mover as classes para seus devidos pacotes, é importante con-
heceralgumasregras. Aprimeiradelaséque nossasclassesdevemserpúbli-
cas para que fiquem visíveis entre os diferentes pacotes. Logo falaremos
mais sobre os modificadores de visibilidade e entenderemos a fundo as suas
regras,masdesdejámantenhaaregraemmente.
122

## Página 133

CasadoCódigo Capítulo8. Pacotes
Outro detalhe importante é que, para o caso das classes públicas, o ar-
quivo .java obrigatoriamente tem que ter o nome da classe. Por exemplo,
aclasse Livrotemquesersalvanoarquivo Livro.java. Comovimosno
iníciodestelivro,oidealévocêsempren omearsuasclassesdessaforma. Essa
éconsideradaumaboapráticaemJava.
Agorasim,mãosàmassa! Vocêpodearrastarasclassescomomousepara
m o v e re n t r ep a c o t e s ,m a su m aa l t e r n a t i v ai n t e r e s s a n t eéoa t a l h oControl
+A l t+V .Essea talhoéequivalen teaomen u Refactor > Move... .
V a m o ss e l e c i o n a ra sc l a s s e sAutor e Editora e mover para o pa-
cote br.com.casadocodigo.livraria. Nesse momento, alguns erros
de compilação devem aparecer, masdevemosterminardemoverasclasses
antesdecorrigirqualquerumdeles .
Promocional, Produto, Livro, LivroFisico, MiniLivro,
Ebook, Revista e qualquer outra implementação de Produto
que você tenha criado podem ser movidos para o pacote
br.com.casadocodigo.livraria.produtos.
Paraterminar,vamosmoverasdemaisclasses,quetêmummétodo main,
para o pacote br.com.casadocodigo.livraria.testes. Lembre-se,
emumprojetorealnãocriaríamosváriasclassescommétodo main,sóesta-
mosfazendoissoparatestarosnossosexemplos.
package, importepossíveiserros
Sevocêmoveuasclassesutilizandoo Eclipseoualguma IDEequivalente,
reparequefoiadicionadoum importparatodaclassequereferenciaalguma
presente em outro pacote. Caso você não tenha movido pelaIDEou por al-
gum motivo oimport não tenha sido adicionado, você precisará fazer isso
man ualmen teco monoexem plo:
package br.com.casadocodigo.livraria.testes;
import br.com.casadocodigo.livraria.Autor;
// outros imports
public class CadastroDeLivros {
123

## Página 134

8.1. Organizandonossasclasses CasadoCódigo
public static void main(String[] args){
Autor autor = new Autor();
autor.setNome("Rodrigo Turini" );
// continuação da classe
}
Comoaclasse Autorestáemumpacote( package)diferentedaclasse
CadastroDeLivros,o import é necessário. Ele sempre é necessário
quando queremos utilizar classes de outros pacotes. E não se esqueça que,
paraqueumaclassesejavisívelparaoutropacote,eladeveserpública.
Um outro detalhe é que agora todas as classes têm o package
a que pertencem declarado. Neste exemplo, o package da classe
CadastroDeLivrosé:
package br.com.casadocodigo.livraria.testes;
Ao r d e md a si n s t r u ç õ e sd es e u sa r q u i v o s.java agora será: primeiro o
package aoqualelapertence,seguidodo(s) import(s)quandonecessário
e,po rúl timo ,adeclaraçãodaclasse.
124

## Página 135

CasadoCódigo Capítulo8. Pacotes
Importandotodasasclassesdeumpackage
Nolugardefazerosseguintes imports:
import br.com.casadocodigo.livraria.Autor;
import br.com.casadocodigo.livraria.Editora;
Você também pode utilizar o* para importar todas as classes de
um package,nestecasoo importseria:
import br.com.casadocodigo.livraria.*;
É comum ouvirmos que isso prejudica a performance, mas na reali-
dade não afetará o tempo de execução. O problema dessa abordagem é
que não previne a ambiguidade de nomes. Por isso, é sempre recomen-
dado que você importe classe a classe, pois, além de evitar problemas
com classes de mesmo nome, tornará a legibilidade dos
importsm a i s
clara.
A i n d ae x i s t eu me r r od ec o m p i l a ç ã oe mn o s s op r o j e t o( o ut a l v e zm a i s ,
se o seu código não estiver idêntico ao do livro). Em nosso caso, o prob-
lemaénaprópriaclasse
CadastroDeLivros,quandoelainvocaométodo
mostrarDetalhesdo LivroFisico.Oerr odeco m p ilaçãoéoseguinte:
The method mostrarDetalhes() from the type Livro is not visible
Isso acontece porque, assim como as classes, para que um método seja
visível em outro pacote ele precisa serpublic. Podemos acessar a classe
Livroeadicionaromodificadordevisibilidade publicnométodooufazer
isso pelo atalhoControl + 1 do Eclipse (quickfix), selecionando a opção
Change visibility of method mostrarDetalhes() to public. No final, o método
deveficarassim:
public void mostrarDetalhes() {
System.out.println("Mostrando detalhes do livro " );
System.out.println("Nome: " + nome);
System.out.println("Descrição: " + descricao);
125

## Página 136

8.2. Modificadoresdeacesso CasadoCódigo
System.out.println("Valor: " + valor);
System.out.println("ISBN: " + isbn);
if (this.temAutor()) {
autor.mostrarDetalhes();
}
System.out.println("--");
}
Estruturadepastas
Notequeumpacoteérepresentadocomoumaestruturadepastasno
seu sistema operacional. Por exemplo, a classeLivro q u ee s t ál o c a l -
izada no pacote br.com.casadocodigo.livraria está dentro do
diretório br/com/casadocodigo/livraria, que se encontra den-
tr odapasta srcdeseuprojeto.
8.2 Modificadoresdeacesso
Agora que nossas classes estão organizadas em pacotes, podemos entender
um pouco melhor os diferentes modificadores de acesso. Já vimos que, para
uma classe ou método ser acessado de outro pacote, eles precisam ter visi-
bilidade
public. A regra é clara: uma classe pública pode ser acessada por
q u a l q u e ro u t r ac l a s sep r e se n t en om e s m op r o j e t o .Om e s m ov a l ep a r aa t r i b -
utos,métodoseconstrutores.
Também já conhecemos o
private. Esse modificador de acesso torna
classes, atributos, métodos ou construtores visíveis apenas para a própria
classe. Por esse motivo, uma classe não deve ser anotada com
private,
quem poderá acessá-la? Mas vimos que faz bastante sentido, para manter o
encapsulamento,sempredeixarseusatributos private.
Há ainda a visibilidadedefault (quando não há modificador algum).
A essa altura, você já pode ter percebido que neste caso apenas classesdo
mesmo pacotepodem ter acesso aos atributos, construtores, métodos ou
classescomaausênciadeummodificadordeacesso.
126

## Página 137

CasadoCódigo Capítulo8. Pacotes
O último modificador é oprotected, que tentamos evitar no capítulo
de herança. Todo elementoque forprotected fica rávi sí v e lpa raap r ó p ria
classe, para suas classes filhas etambémparaquemestivernomesmopa-
cote. Classestambémnãopodemutilizaressemodificadordeacesso.
A imagem a seguir representa cada modificador de acesso e sua visibili-
dade:
127

## Página 139

Capítulo9
Arrayseexception
9.1 Trabalhandocommultiplicidade
Nosso CarrinhoDeComprassóestáfazendoumapartedeseutrabalho,que
éacumularovalortotaldosprodutosadicionados. Tambémprecisaremoster
umatributonessaclasseparaguardarumareferênciaatodosesses Produtos
adicionados.
Poderíamos adicionar um número limitado de atributos do tipo
Produto,co mo:
public class CarrinhoDeCompras {
private double total;
private Produto produto1;
private Produto produto2;
private Produto produto3;

## Página 140

9.1. Trabalhandocommultiplicidade CasadoCódigo
private Produto produto4 ;
// ...
// demais métodos da classe
}
Deixando esses atributos com o tipoProduto,n ol u g a rd eu mLivro
ou Revista por exemplo, o polimorfismo nos daria a flexibilidade de
adicionar qualquer classe que implemente essa interfaceProduto.M a s ,
fora isso, nosso código não está nem um pouco flexível! Além de termos
um númerolimitado de produtos, no método adiciona precisaríamos
fazerváriascondiçõesparaverificarqualatributoestádisponívelantesdeadi-
cionar:
public class CarrinhoDeCompras {
private double total;
private Produto produto1 ;
private Produto produto2 ;
private Produto produto3 ;
private Produto produto4 ;
//..
public void adiciona(Produto produto ){
System.out.println("Adicionando: " + produto);
if (this.produto1 != null){
this.produto1 = produto;
}
else if (this.produto2 != null){
this.produto2 = produto;
}
else if (this.produto3 != null){
this.produto3 = produto;
}
else if (this.produto4 != null){
this.produto4 = produto;
}
// ...
130

## Página 141

CasadoCódigo Ca p í tulo9. Arra yseexcep tio n
else {
System.out.println("Não tem mais espaços");
return;
}
total += produto.getValor();
}
}
Imagine como seria para mostrar os detalhes dos produtos adicionados,
novamente precisaríamos repetir essesifs todos com as condicionais. Esse
códigoseriabemdifícildemanter,quaseinviável. Alémdisso,quantosatrib-
utos do tipo Produto um CarrinhoDeCompras teria? 10? 20? Isso vai
dependermuitodocliente,elepodeestarcomprandoumúnicolivroouuma
coleçãocompletaediversosoutrosprodutos.
Criandoum arrayde Produto
Evitamos até agora trabalhar com esse recurso, mas, como vimos
no primeiro capítulo, podemos resolver esse problema trabalhando com
arrays! Não lembra o que é isso? Dê uma boa olhada novamente na
declaraçãodométodo maindequalquerumadesuasclasses:
public static void main(String[] args){
// seu código aqui
}
Repare que ele recebe um array de Strings como parâmetro! O
String[] args .
Podemos utilizar essa mesma estratégia em nosso
CarrinhoDeCompras, basta remover todos estes atributos do tipo
Produto e declarar um único array. Como fazer isso? É bem simples,
basta adicionar [] d e p o i sd ot i p oep r o n t o .N o s s oCarrinhoDeCompras
vaificarassim:
public class CarrinhoDeCompras {
private double total;
private Produto[] produtos;
131

## Página 142

9.1. Trabalhandocommultiplicidade CasadoCódigo
public void adiciona(Produto produto ){
// precisamos adicionar no array
}
}
Um array éumtipo, umobjeto. Issosignificaque, antesdefazerqual-
quer operação com o atributoprodutos, precisaremos instanciá-lo. A sin-
taxeéumpoucodiferente,masébemsimples:
public class CarrinhoDeCompras {
private double total;
private Produto[] produtos = new Produto[10];
//..
}
Note que ao criar oarray fomos obrigados a informar o seu tamanho!
N e s t ec a s o ,c r i a m o su marray de 10 posições. Poderíamos sim receber
a quantidade de Produtosn oc o n s t r u t o rd ac l a s s eo uc r i a ru mm é t o d o
setProdutos, isso a deixaria um pouco mais flexível. Mas a princípio,
deixaremoso CarrinhoDeComprasassim,limitadoa10produtos.
Agora que estamos trabalhando com umarray, precisamos mudar o
método adiciona. Podemosfazeralgocomo:
public void adiciona(Produto produto ){
System.out.println("Adicionando: " + produto);
this.produtos[1] = produto;
this.total += produto.getValor();
}
Note que estamos adicionando todos os produtos na mesma posição do
array,n ap o s i ç ã o1 . U md e t a l h em u i t oi m p o r t a n t eéq u eap o s i ç ã o1éa
segundaposiçãodo array,enãoaprimeira. Issoacontecepoisseusíndices
vão de 0 (zero) até seu tamanho -1, ou seja, como criamos umarray de 10
posições,elevaide0a9.
Uma alternativa seria mudar a assinatura do métodoadiciona para
receberum int indice comoparâmetro,masdeixaressecontrolenamão
132

## Página 143

CasadoCódigo Ca p í tulo9. Arra yseexcep tio n
de quem vai chamar o método pode não ser muito interessante, isso abriria
caminho para chamar o método duas vezes com o mesmoindice eu m
elementosobrescreverooutro,porexemplo.
No lugar disso podemos criar um atributocontador que é incremen-
tadoacadanovaadição,veja:
public class CarrinhoDeCompras {
private double total;
private Produto[] produtos = new Produto[10];
private int contador =0 ;
public void adiciona(Produto produto ){
System.out.println("Adicionando: " + produto);
this.produtos[contador]=produto;
contador ++;
this.total += produto.getValor();
}
public double getTotal() {
return total;
}
}
Problema resolvido! Sim, ainda estamos deixando passar algumas situ-
ações, como por exemplo tentar adicionar mais produtos do que cabe den-
t r od en o s s oarray. E se eu tentar adicionar 11 produtos? Precisamos
tratar isso de alguma forma. Por enquanto, o código ficará assim, mas
em breve voltaremos para refatorar e cuidar desse tipo de detalhe da classe
CarrinhoDeCompras.
133

## Página 146

9.2. Asdiferentesexceçõesecomolidarcomelas CasadoCódigo
Oenhanced-for doJava5
Desde o Java 1.5, é possível iterar em umarray (ou qualquer outro
Iterable, que veremos nos próximos capítulos) com uma sintaxe um
poucodiferente. Nolugarde:
for (int i =0 ;i < produtos.length; i++) {
Produto produto = produtos[i];
if (produto != null){
System.out.println(produto.getValor());
}
}
Podemosfazeromesmodaseguinteforma,como enhanced-for:
for (Produto produto : produtos){
if (produto != null){
System.out.println(produto.getValor());
}
}
Repare que nesse caso não temos um indice e não pre-
cisamos conhecer o tamanho ( lenght)d o array para con-
seguir percorrê-lo, isso evitaria a confusão com o<= q u ec a u s o uo
ArrayIndexOutOfBoundsException.
9.2 As diferentes exceções e como lidar com
elas
ConhecendoaStacktrace
Podeparecerumpoucoassustadornocomeço,masa stacktracenormal-
mentenospassaasinformaçõesnecessáriasefundamentaisparaacompreen-
sãoeresoluçãodosproblemas. Vamosanalisá-lacommaisatenção:
Exception in thread "main"
java.lang.ArrayIndexOutOfBoundsException: 10
136

## Página 147

CasadoCódigo Ca p í tulo9. Arra yseexcep tio n
at br.com.casadocodigo.livraria.testes
.RegistroDeVendas.main(RegistroDeVendas.java:38)
E s s aéu m astacktrace bem pequena, você pode perceber o quanto é
fácildeentender. Aprimeiralinhaestánosinformandoqualonomedoprob-
lema(ou exception,comopassaremosachamá-lo)queocorreunocódigo
enosdizemqualposiçãodoarrayissoaconteceu( 10). Nasegundaeúltima
linha temos o fully qualified name da classe em que aexception
aconteceu,queaindanosdizemquallinha,nestecaso38!
Investigandoproblemas
É muito comum enviarmos astacktrace quando estamos procu-
rando por ajuda em fóruns (como ohttp://guj.com.br)o ul i s t a sd ed i s -
cussões. Issofacilitabastantenainvestigaçãodoproblema.
Tratandoexceptions
Evitaressa exceptionseriabemsimples,bastariacorrigiracomparação
com <=ouutilizaro enhanced-for. Masháumaformabastanteconhecida
ejáutilizadaemdiversaslinguagenspara tentarexecutarumblocodecódigo
deriscoe capturarcasoocorrauma exceptionnestebloco,evitandoquea
stacktracesejaexibidaparaousuáriofinalequeaexceçãopareaexecução
denossocódigo. Esserecursoéconhecidocomo try/catch.
Para testá-lo, coloque umsysout l o g oa p ó sofor q u ee s t ág e r a n d oo
problemano RegistroDeVendas,algoco mo:
for (int i =0 ;i <= produtos.length; i++) {
Produto produto = produtos[i];
if (produto != null){
System.out.println(produto.getValor());
}
}
System.out.println("Fui executado!");
137

## Página 148

9.2. Asdiferentesexceçõesecomolidarcomelas CasadoCódigo
Rode novamente e repare na saída, a mensagem"Fui executado!"
não foi impressa. Vamos agora adicionar otry/catch ee x ecu ta roc ód i g o
novamente:
for (int i =0 ;i <= produtos.length; i ++) {
try {
Produto produto = produtos[i];
if (produto != null){
System.out.println(produto.getValor());
}
} catch (ArrayIndexOutOfBoundsException e){
System.out.println("deu exception no indice: " + i);
}
}
System.out.println("Fui executado!" );
Agoraasaídaserá:
Total 83.81
53.91
29.9
deu exception no indice: 10
Fui executado!
Comoa exceptionfoidevidamentetratada,aexecuçãodocódigonão
foiinterrompida.
138

## Página 149

CasadoCódigo Ca p í tulo9. Arra yseexcep tio n
Entendendoasintaxedo TRY /CATCH
Podepareceumpoucoestranhoouatémesmoassustadornocomeço,
masasintaxedo try/catchnãotemnadadetãocomplicado. Veja:
try {
// algum código de risco
} catch (ArrayIndexOutOfBoundsException e){
// o que fazer aqui?
}
N e s sec a so ,d e n t r od ocatch podemos colocar o código que quere-
mosexecutarapenasquandouma exceptiondotipodeclaradoacon-
tecer. Ou seja, nele colocamos o código que queremos executar apenas
casoum ArrayIndexOutOfBoundsExceptionocorra.
T odaexceptionéfilhade Exception
Em nosso try/catchm estamos capturando apenas o
ArrayIndexOutOfBoundsException, mas o que aconte-
ceria se o array produtos fosse null? Mesmo que com o
try/catch declarado, receberíamos um outro tipo de exception, a
java.lang.NullPointerException.
Isso acontece porque estamos deixando claro no
parâmetro de nosso catch que queremos capturar
um ArrayIndexOutOfBoundsException,e n ã o u m
NullPointerException. Poderíamosfazeralgomaisgenéricocomo:
for (int i =0 ;i <= produtos.length; i++) {
try {
Produto produto = produtos[i];
if (produto != null){
System.out.println(produto.getValor());
}
} catch (Exception e ){
System.out.println("deu exception no indice: " + i);
139

## Página 151

CasadoCódigo Ca p í tulo9. Arra yseexcep tio n
Capturar Exceptionnemsempreémuitointeressante,afinalsetratade
um tipo muito genérico! Muitas vezes queremos dar uma tratativa diferente
paracadatipodeexceçãodocódigo. Umaalternativaparaissoseriacapturar
maisdeuma
exceptionemummesmobloco try:
try {
Produto produto = produtos[i];
if (produto != null){
System.out.println(produto.getValor());
}
} catch (ArrayIndexOutOfBoundsException e ){
System.out.println("deu exception no indice: " + i);
} catch (NullPointerException e ){
System.out.println("Aarray não foi instanciado!" );
}
Agoraestamosmostrandoumamensagemdiferenteparacadasituação.
MULTICATCH doJava7
Caso você queira executar a mesma ação para dois tipos de
Exception diferentes, desde o Java 7 você pode utilizar uma sintaxe
umpoucodiferente:
try {
Produto produto = produtos[i];
if (produto != null){
System.out.println(produto.getValor());
}
} catch
(ArrayIndexOutOfBoundsException | NullPointerException e ){
System.out.println("foi uma das duas" );
}
A mensagem "foi uma das duas" será exibida
caso uma ArrayIndexOutOfBoundsException ou um
NullPointerExceptiontenhaocorrido.
141

## Página 152

9.3. MuitasemuitasException CasadoCódigo
Executandoumaaçãocomousemexception
Existem momentos em que precisamos executar alguma ação após um
tryou catch,independentesehouveounãouma exceptionenvolvida.
Nessescasos,podemosutilizarumaterceiracláusulachamada finally.
Observesuasintaxe:
try {
// código de risco
} catch (NullPointerException e ){
// tratando NPE
} catch (Exception e){
// tratando Exception
} finally {
// alguma ação importante
}
Asinstruçõesdobloco finallyserãoexecutadassempre,independente
detudoteridobemoudealguma exceptionteracontecido.
Esserecursoémuitocomumquandoestamostrabalhandocomconexão
do banco de dados ou leitura/escrita de arquivos. Independente de qualquer
coisa,depoisdeusarumaconexão,porexemplo,semprequeremosfechá-la.
9.3 MuitasemuitasException
As RuntimeExceptions
Claro, além de um for tentando acessar mais índices do que deveria e a
tentativadeexecutarmosaçõesemreferênciasnulas,existemdiversasoutras
situações de risco em que a JVM lançará uma
exception. Cada situação
dessa tem uma forma (um tipo) forte de ser representada; conhecê-las pode
serm ui toim po rtan teparanossodiaadia.
Veremos diversas dessas situações e diferentes tipos de
Exception no
decorrerdestecapítuloedosdemaisdolivro,masdesdejáéinteressanteen-
tendermosquetodosestescasosquevimosatéagorapoderiamfacilmenteser
evitados deformasimplespeloprogramador.
142

## Página 153

CasadoCódigo Ca p í tulo9. Arra yseexcep tio n
Conhecemosestestiposde Exceptionscomo unchecked,poisocom-
piladornãoverifica(checa)seasestamostratando. Emoutraspalavras,nosso
códigocompilarácomousemos try/catchsdeclarados.
As unchecked exceptions não herdam diretamente da classe
Exception, mas sim de sua filhaRuntimeException. Os casos mais co-
munssão:
Checked Exception s
Diferentedisso,quandoestamosfazendoaleituradeumarquivoouqual-
quer outra operação de risco que não pode ser facilmente evitada (o ar-
quivo pode não existir, por exemplo) o compilador nos obriga a tratar esse
código! Esseéumoutrotipode
exceptiondalinguagem,conhecidacomo
checked exception .
Para testar, vamos escrever o seguinte código que realiza a leitura de um
143

## Página 154

9.3. MuitasemuitasException CasadoCódigo
arquivo que não existe. Não se preocupe com o código em si, entenderemos
aAPIdeIO(leituraeescrita)maisàfrente. Opontoaquiéperceberqueesse
códigonãocompila:
new java.io.FileInputStream( "arquivo.txt");
Oerr oserá“UnhandledexceptiontypeFileNotFoundException
. Notequeocompiladorchecouqueelanãoestásendotratada. Paraque
ocódigocompilepoderíamosfazeralgocomo:
try {
new java.io.FileInputStream( "arquivo.txt");
} catch (FileNotFoundException e1 ){
System.out.println("Não consegui abrir o arquivo");
}
Delegandoatratativacom throws
Uma alternativa para o try/catch nesse caso seria adicionando um
throws FileNotFoundException . Issosignificaqueestamosdelegando
atratativaparaquemchamarestemétodo:
public void abreArquivo() throws FileNotFoundException {
new java.io.FileInputStream( "arquivo.txt");
}
Dessaforma,o throwsestáindicandoaocompiladorquequemchamar
o método abreArquivo deverá tratar oFileNotFoundException.E m
outras palavras, isso diz:“Ei, esse é um código de risco, ele pode lançar uma
FileNotFoundException
.
Chamando-oapartirdeummétodo
mainpoderíamostrataroerro:
public static void main(String[] args){
try {
abreArquivo();
} catch (FileNotFoundException e1 ){
System.out.println("Não consegui abrir o arquivo");
}
}
144

## Página 155

CasadoCódigo Ca p í tulo9. Arra yseexcep tio n
Asaídaserá:
Não consegui abrir o arquivo
Ouainda,usaro throwsnovamente,noprópriométodo main:
public static void main(String[] args)
throws FileNotFoundException {
abreArquivo();
}
Dessa forma, ninguém tratará aexception, estamos deixando passar
paraaJVM.Asaídaserá:
Exception in thread "main" java.io.FileNotFoundException:
arquivo.txt (No such file or directory)
at java.io.FileInputStream.open(Native Method)
at java.io.FileInputStream.<init>(FileInputStream.java:131)
at java.io.FileInputStream.<init>(FileInputStream.java:87)
at br.com.casadocodigo.livraria.testes
.RegistroDeVendas.abreArquivo(RegistroDeVendas.java:62)
at br.com.casadocodigo.livraria.testes
.RegistroDeVendas.main(RegistroDeVendas.java:17)
THROW ou THROWS ?
É muito comum confundir no início, mas lembre-se que usamos
o throw no imperativo quando estamos efetivamente lançando uma
exeption. Quando escrito no indicativo, othrows apenas informa
aocompiladore aquemmaisinteressarquedeterminado métodolança
uma exception.
145

## Página 156

9.3. MuitasemuitasException CasadoCódigo
AfamiliaThrowable
Vimos que existem diversas Exceptions, sejam elas checked ou
unchecked, porém, além delas existem os tão temidosErrors. Estes são
como um tipo deexception, mas normalmente representam problemas
na JVM (como oOutOfMemoryError). Apesar de em alguns casos con-
seguirmos capturar/tratar estes erros, muitas vezes o melhor a fazer é deixar
a JVM encerrar sua execução. E apesar de ser possível, não devemos lançar
Erroremnossocódigo. Issonãoéconsideradoumaboaprática.
O Errore Exceptionsãoirmãos,poisambosherdamde Throwable!
Aimagemaseguirmostraumpoucodaimensafamília Throwable:
146

## Página 157

CasadoCódigo Ca p í tulo9. Arra yseexcep tio n
9.4 Tambémpodemoslançarexceções!
N o s s oc ó d i g ot a m b é mp o d el a n ç a ru m aexception caso algo inesperado
aconteça. E não estou falando de lançar umaexception acidentalmente.
Assimcomoum arraydisparao ArrayIndexOutOfBoundsException
quandofazemosalgoinesperado(tentaracessarmaisvaloresdoqueo array
suporta),podemosfazerissocomnossasregras.
Um exemplo simples é na própria classeLivro, onde desde o início
definimos que seria obrigatório passar umAutor como argumento. A re-
g r aéc l a r a :n ã os ep o d et e ru mLivro sem Autor e, para garantir isso,
criamosoconstrutorqueobrigavaapassagemdesseparâmetro:
public Livro(Autor autor ){
this.autor = autor;
this.isbn = "000-00-00000-00-0" ;
}
Isso já é bem interessante, mas o grande problema é que ainda podemos
passar uma referência nula deAutor no momento em que criamos o livro,
como:
Livro livro = new LivroFisico(null);
Atépoderíamosvalidarovalorpassadoparaoconstrutor:
public Livro(Autor autor ){
if (autor == null){
// o que fazer aqui?
}
this.autor = autor;
this.isbn = "000-00-00000-00-0" ;
}
Masoquepoderiaserfeitoseoautorfosse null? AssimcomoaAPIdo
Java,podemoslançar exceptionsparacasoscomoesse. Essaéumaforma
maisrobustadoquevalidareretornarum booleanouumamensagemque
podesimplesmenteserignorada.
Vejacomoficanossocódigo:
147

## Página 158

9.4. Tambémpodemoslançarexceções! CasadoCódigo
public Livro(Autor autor ){
if (autor == null){
throw new RuntimeException();
}
this.autor = autor;
this.isbn = "000-00-00000-00-0";
}
Repare que a palavra reservadathrow precede a exception que está
sendodisparada,nestecasouma RuntimeException. Háaindaapossibil-
idade de passar uma mensagem via construtor, comportamento presente na
superclasse Exception :
public Livro(Autor autor ){
if (autor == null){
throw new RuntimeException(
"O Autor do Livro não pode ser nulo" );
}
this.autor = autor;
this.isbn = "000-00-00000-00-0";
}
Asaídaserá:
Exception in thread "main" java.lang.RuntimeException:
O Autor do Livro não pode ser nulo
at br.com.casadocodigo.
livraria.produtos.Livro.<init>( Livro.java:16)
at br.com.casadocodigo.
livraria.produtos.LivroFisico.< init>(LivroFisico.java:9)
at br.com.casadocodigo.
livraria.testes.RegistroDeVendas.main( RegistroDeVendas.java:16)
Criandosuaprópria Exception
N ol u g a rd el a n ç a ru m aRuntimeException, podemos criar uma
exception bem específica para esse comportamento inesperado. Vamos
criara AutorNuloException!
148

## Página 159

CasadoCódigo Ca p í tulo9. Arra yseexcep tio n
Comofazerisso? Naverdade,ébemsimples: assimcomoqualqueroutra
Exception essa será uma classe normal que herda deException ou de
u m ad es u a sfi l h a s .P a r aq u ee l ase j aev i t á v e l(uncheked), vamos herdar de
RuntimeException:
package br.com.casadocodigo.livraria.exception;
public class AutorNuloException extends RuntimeException {
public AutorNuloException( String mensagem){
super(mensagem);
}
}
Notequecriamosumconstrutorquedelegaamensagemparaoconstru-
torda superclasse,dessaformanossocódigopoderáficarassim:
public Livro(Autor autor ){
if (autor == null){
throw new AutorNuloException(
"O Autor do Livro não pode ser nulo" );
}
this.autor = autor;
this.isbn = "000-00-00000-00-0" ;
}
Rodenovamenteocódigoproblemáticoevejaqueasaídaserá:
Exception in thread "main" br.com.casadocodigo.livraria.exception
.AutorNuloException: O Autor do Livro não pode ser nulo
at br.com.casadocodigo.livraria.produtos
.Livro.<init>(Livro.java:17)
at br.com.casadocodigo.livraria.produtos
.LivroFisico.<init>(LivroFisico.java:9)
at br.com.casadocodigo.livraria.testes
.RegistroDeVendas.main(RegistroDeVendas.java:16)
Vocêpodelermaissobre Exceptionsemsuadocumentação:
149

## Página 160

9.4. Tambémpodemoslançarexceções! CasadoCódigo
http://docs.oracle.com/javase/8/docs/api/java/lang/Exception.html
Reparequelogonoiniciodestearquivotemossuas subclassesdiretas
(DirectKnownSubclasses). Achouquesãomuitas? Eessassãoapenasasfilhas
diretas, ainda temos as filhas deRuntimeException ed es u a sd i v e r s a s
outras subclasses.
P o ri s s o ,s e m p r ea n t e sd ec r i a ru m aException própria, tente conferir
sejánãoháumaimplementaçãoexistentequerepresentebemasituaçãoin-
esperada.
150

## Página 161

Capítulo10
ConhecendoaAPI
10.1 Todoobjetotemumtipoemcomum
Criamos a interface Produto para o CarrinhoDeCompras suportar a
adiçãode Revistase Livros. Essainterfaceestabeleceumtipoemcomum
entreessasduasclasses,portantoo CarrinhoDeComprasficouassim:
public class CarrinhoDeCompras {
private double total;
private Produto[] produtos = new Produto[10];
private int contador =0 ;
public void adiciona(Produto produto ){
System.out.println("Adicionando: " + produto);
this.produtos[contador]=produto;

## Página 162

10.1. Todoobjetotemumtipoemcomum CasadoCódigo
contador ++;
this.total += produto.getValor();
}
// getters para o total e array de produtos
}
O polimorfismoéachaveparaqueissotudofuncione,nossométodo
adicionarecebeum Produtocomoparâmetroeoacumulano arrayde
Produtos.
Essa foi uma boa estratégia, mas as duas classes não precisariam im-
plementar nenhuma interface para ter um tipo em comum, pois sem-
pre que criamos uma nova classe em Java ela obrigatoriamente terá uma
superclasse.
A téaclasse Revistatemuma superclasse,masrepareemsuaassi-
natura:
public class Revista implements Produto, Promocional {
// código omitido
}
Não há nenhum extends declarado nessa classe, como ela pode es-
tar herdando de alguém? Essa é uma situação parecida com a do constru-
tor default, lembra? Na ausência de um construtor, o compilador adi-
cionará um construtor vazio para você. Assim é com a herança, na ausência
de um
extends, o Java dirá que sua classeextends um tipo conhecido
como Object.
Com isso, podemos concluir quetodaclasseemJavaéumObject ,s e m
exceção. Pode não ser diretamente, mas ainda que indiretamente, ela será,
poisherdarádealguémqueherdadiretamenteouindiretamentede
Object.
Agrandevantagemdessetipoemcomuméquetodaclasseherdaalguns
métodosdeclaradosnaclasse Objecteaindapodemserreferenciadascomo
tal. Logoveremosalgunsdessesmétodosecomotirarproveitodelesemnosso
diaadia.
152

## Página 163

CasadoCódigo Capítulo10. ConhecendoaAPI
Castingsemaiscastings
Se toda classe já tem esse tipo em comum, por que não mudamos
nosso CarrinhoDeCompras para receber e acumularObject, no lugar
de Produto,comoestamosfazendo? Nossocódigoficariaassim:
public class CarrinhoDeCompras {
private double total;
private object[] objects = new object[10];
private int contador =0 ;
public void adiciona(object object ){
System.out.println("Adicionando: " + object);
this.objects[contador]=object;
contador ++;
this.total += object.getValor();
}
// getters para o total e arrayde objects
}
Tente mudar seu código, que logo você perceberá o primeiro problema.
Aseguintelinhanãocompila:
this.total += object.getValor();
Já descobriu por quê? Object não tem o métodogetValor,n ã oh á
garantiaparaocompiladordequequalquercoisaquepassarmoscomoargu-
mentoparaessemétodoteráessemétodo.
Como resolver? Bem, poderíamos fazer umcasting como a seguir,
moldandoareferênciado Objectparaum Produto:
Produto moldado =( Produto) object;
this.total += moldado.getValor();
Mas, além de muito feio, esse código é muito perigoso, afinal e se o
argumento passado (que agora pode ser qualquer coisa) não implementar
Produto? Oresultadoseriaum ClassCastException.
153

## Página 164

10.1. Todoobjetotemumtipoemcomum CasadoCódigo
Eoproblemairiaalém. Porexemplo,paraimprimirovalordosprodutos
naclasse RegistroDeVendas,estamosfazendooseguintecódigo:
Produto[] produtos = carrinho.getProdutos();
for (int i =0 ;i <= produtos.length; i ++) {
try {
Produto produto = produtos[i];
if (produto != null){
System.out.println(produto.getValor());
}
} catch (ArrayIndexOutOfBoundsException e){
System.out.println("deu exception no indice: " + i);
e.printStackTrace();
}
}
Mas agora que já vimos que essa não é a melhor forma de iterar em um
array, podemos utilizar oenhanced-for do Java 7. Nosso código ficaria
assim:
Produto[] produtos = carrinho.getProdutos();
for (Produto produto : produtos){
System.out.println(produto.getValor());
}
Muitomaissimples,nãoacha? Sóquese produtosfosseum arrayde
Object,essecódigonãofuncionariacomoesperamos. Repare:
Object[] produtos = carrinho.getProdutos();
for (Object object : produtos){
System.out.println(object.getValor());
}
Novamente: Objectnãotemométodo getValor,po rtan to ,ocódigo
não compila. Poderíamos fazer o casting, claro, mas veja como ficaria
nossocódigo:
154

## Página 165

CasadoCódigo Capítulo10. ConhecendoaAPI
Object[] produtos = carrinho.getProdutos();
for (Object object : produtos){
try {
Produto moldado =( Produto) object;
System.out.println(moldado.getValor());
} catch(ClassCastException e){
System.out.println("O objeto passado não implementa Produto" );
}
}
Difícil de ler, manter e nem um pouco flexível. Você já deve ter perce-
bido que receber umObject como parâmetro nem sempre é uma boa al-
ternativa, pois sempre precisaremos decastingsem a i scastings, não
há muito como fugir. Manter o tipo do parâmetro e array da classe
RegistroDeVendas como Produto neste caso será uma estratégia bem
maisinteressante.
CASTING emumasólinha
Também podemos fazer nossos castings em uma única linha,
comonoexemplo:
double valor =( ( Produto)object).getValor();
O efeito do código seria o mesmo, mas talvez com uma sintaxe um
poucomaiscarregadacustandolegibilidade.
Algunsdosmétodosdaclasse Object
Vimos que o custo de fazerpolimorfismo com Object pode nem
sempre valer a pena, mas isso não invalida o quanto ela é importante para a
linguagem Java. Nela, estão presentes todos os métodos que toda classe em
Javadeveter!
Querumexemplo? Algumavezvocêjádeveterescritooseguintecódigo:
System.out.println(ebook);
155

## Página 167

CasadoCódigo Capítulo10. ConhecendoaAPI
contrário,ocódigonãocompilaria. Vamostestar,bastaimprimirum ebook
novamente:
System.out.println(ebook);
Agoraasaídaserá:
Eu sou um Ebook
É sempre interessante sobrescrever esse método, porque assim con-
seguimosestabelecercomorepresentarnossasclassescomoumtextodeuma
formamaiselegantedoqueopadrãodo Object. Jáestávamosfazendoisso
com o método mostrarDetalhes, lembra? Podemos modificar sua assi-
natura para que agora seja otoString das classes Livro e Autor,u m
exemplo:
public abstract class Livro implements Produto {
// código omitido
@Override
public void toString() {
System.out.println("Nome: " + nome);
System.out.println("Descrição: " + descricao);
System.out.println("Valor: " + valor);
System.out.println("ISBN: " + isbn);
if (this.temAutor()) {
autor.toString();
}
System.out.println("--");
}
}
Comparandoobjetoscom equals
Outrasituaçãomuitocomumemnossodiaadiaéanecessidadedecom-
parar objetos. Vimos nos primeiros capítulos do livro que== sempre com-
para o valor dos atributos, que em caso de objetos será sua referência. Isso
significaqueoresultadodaseguintecomparaçãoserá false:
157

## Página 168

10.1. Todoobjetotemumtipoemcomum CasadoCódigo
Autor autor = new Autor();
autor.setNome("Rodrigo Turini" );
Autor autor2 = new Autor();
autor2.setNome("Rodrigo Turini" );
if (autor == autor2){
System.out.println("Igual");
} else {
System.out.println("Diferente" );
}
Execute o código para comprovar: será impressa a palavraDiferente.
Faz sentido, já era de se esperar. Mas e se estivermos interessados em com-
parar os valores dos atributos? Podemos utilizar outro método muitíssimo
interessantedaclasse
Object,o equals. MasoJavaporsisónãovaisaber
como queremos comparar nossosAutores, se eu apenas mudar o código
parautilizaro equalsdaformaaseguir,oresultadoaindaserá false:
if (autor.equals(autor2)) {
System.out.println("Igual");
} else {
System.out.println("Diferente" );
}
Oresultadoaindaserá false,poisométodo equalsdaclasse Object
fazumacomparaçãocom ==,assimcomojáestávamosfazendo. Mas,afinal,
qualavantagemdeusaro equals? Podemossobrescrevê-loensinandoquais
sãooscritériosdecomparação. Umexemplo:
public class Autor {
// atributos e métodos omitidos
@Override
public boolean equals(Object obj){
Autor outro =( Autor) obj ;
return this .nome.equals(outro.nome);
158

## Página 169

CasadoCódigo Capítulo10. ConhecendoaAPI
}
}
Estamos definindo que, sempre que umAutor tiver um nome igual ao
outro, eles são iguais; em outras palavras, oequals deve retornar true.
V amosen tendermelho ressasob r escri ta,aco meçarpalalinha:
Autor outro =( Autor) obj ;
Note que o equals recebe Object como argumento, portanto a
primeiracoisaquefizemosaoimplementá-lofoimoldaresseparâmetropara
otipo Autor. Sim,háumriscobemgrandedeum ClassCastException
caso o parâmetro passado não seja realmente umAutor, depois veremos
algumasalterativasparalidarcomisso.
Vejaquelogoemseguidafazemososeguinteretorno:
return this .nome.equals(outro.nome);
Qualseriaoproblemadefazeroseguinte?
return this .nome == outro.nome;
Já percebeu? Claro, String é um objeto, logo estaríamos comparando
sua referência. Adiante falaremos mais sobre o problema da comparação
de
Strings, mas o importante agora é perceber que estamos delegando a
comparação do nome (String)p a r aom é t o d oequals da própria classe
String. Elefoisobrescritoparafazeracomparaçãopelotextopassado,enão
pelareferênciadememória.
Lidandocomo ClassCastException
Vimos brevemente que umaClassCastException pode ser lançada
casooparâmetropassadoparao equalsnãosejadomesmotipomoldado,
comonoseguinteexemplo:
if(autor.equals("Rodrigo")) {
System.out.println("iguais");
}
159

## Página 170

10.1. Todoobjetotemumtipoemcomum CasadoCódigo
Esse código compilará sem nenhum problema, afinal
String éu m Object. Mas ao executá-lo recebemos uma
java.lang.ClassCastException: java.lang.String cannot
be cast to br.com.casadocodigo.livraria.Autor .C o m o r e -
solver? Umamaneiraseriatratandocomum try/catch, mas veja como o
códigoficaverbosoedifícildeler:
@Override
public boolean equals(Object obj ){
Autor outro ;
try {
outro =( Autor) obj;
} catch (ClassCastException e){
return false ;
}
return this .nome.equals(outro.nome);
}
Uma forma mais interessante seria utilizando oinstanceof,c o m oa
seguir:
@Override
public boolean equals(Object obj ){
if (!(obj instanceof Autor)) return false ;
Autor outro =( Autor) obj;
return this .nome.equals(outro.nome);
}
Dessa maneira, se o parâmetro passado não foi uma instância do tipo
Autor,retornamos falseindicandoquenãosãoobjetosiguais.
Existemoutrosmétodosinteressantesnaclasse Object,algunsdelessão
o getClasse hashcode. Falaremosdesteúltimonopróximocapítulo,mas
saiba desde já que ele sempre acompanha oequals. Um exemplo simples
de uso dogetClass seria para mostrar o nome simples da classe, sem seu
pacote( fully qualified name ). Repare:
System.out.println(autor.getClass().getSimpleName());
160

## Página 171

CasadoCódigo Capítulo10. ConhecendoaAPI
10.2 Wrappersdostiposprimitivos
Jánãoénenhumasurpresaqueoseguintecódigocompile:
Object objeto = new Autor ("Rodrigo");
Nemmesmoseforapenasuma String,pois todoobjetoemJavaherda
diretaouindiretamentede Object.
Object objeto = "Uma String";
Masoquevocêachadocódigoaseguir?
Object objeto = 10;
Se você estiver utilizando uma versão maior que Java 1.4, ele compilará.
Issonãosignificaqueostiposprimitivoscomoo intherdamde Objectou
são do mesmo tipo que uma referência, esse é apenas um truque do compi-
ladoradicionadonoJava1.5parasimplificarumpoucoasintaxe. Esserecurso
éconhecidocomo
autoboxing.
Semisso,paraqueocódigocompileprecisaríamosfazer:
Object objeto = new Integer(10);
Notequeaclasse Integer éusadaparaembrulhar( wrapping)oti po
primitivo int, de forma que podemos tratá-la como uma referência, um
Object. Omesmoseaplicaaosdemaistiposprimitivos. Aimagemaseguir
mostracadaumdelesesuaclasse wrapper(box).
161

## Página 172

10.2. Wrappersdostiposprimitivos CasadoCódigo
Também podemos desembrulhar os valores primitivos das classes
wrappers:
Integer integer = new Integer(10);
int valor = integer.intValue();
Masessanãoéaúnicautilidadedasclasses wrappers,elasestãorepletas
de métodos estáticos que podem ser bastante úteis para manipular os tipos
primitivos.
Conversãodevalores
Comotransformarum booleanemuma String?Eocontrário?Como
transformar um texto em umdouble válido? Todas essas conversões po-
demserfeitasdeformabemsimplesapartirdasclassesqueembrulhamesses
162

## Página 173

CasadoCódigo Capítulo10. ConhecendoaAPI
tiposprimitivos. Porexemplo,ométodo parseBooleandaclasse Boolean
transformauma Stringemumbooleano. Veja:
boolean resultado = Boolean.parseBoolean( "false");
Omesmopodeserfei toparaosdemaisti pos:
byte parseByte = Byte .parseByte("1");
short parseShort = Short.parseShort("10");
int parseInt = Integer.parseInt("10");
long parseLong = Long .parseLong("10");
float parseFloat = Float.parseFloat("10.0");
double parseDouble = Double.parseDouble("10.0");
Paratransformarqualquerumdessesvaloresemuma String,podemos
utilizarseumétodoestático valueOf:
String numeroEmTexto = String.valueOf(10);
Claro,precisamostomarbastantecuidadocomovalorpassado,poisadi-
vinhequalseráoresultadodocódigoaseguir?
int parseInt = Integer.parseInt("ABC");
Uma Exception! Nestecaso: java.lang.NumberFormatException:
For input string: "ABC" . Faz bastante sentido, afinal, como transfor-
mar ABCemumnúmero?
Maismétodosúteis
Aproveite o momento para explorar os diversos métodos existentes
em Objectenasclasses wrappers,comoa Interger. Elescomcerteza
serãobemúteisemseudiaadiacodandoemJava!
10.3 Opacotejava.lang
Você já deve ter percebido que até agora não precisamos fazerimport de
nenhumadasnovasclassesquevimosnestecapítulo. Outrodetalheéqueem
163

## Página 174

10.3. Opacotejava.lang CasadoCódigo
nenhum momento anterior precisamos fazerimport daclasse String ou
mesmodaclasse System,nãoé?
Isso porque Object, String, System,c l a s s e swrappers dos tipos
primitivos entre diversas outras estão todas presentes no pacote padrão do
Java, o java.lang. Este pacote é automaticamente incluído em todas as
suasclasses,diferentedetodososdemaisdalinguagem.
Nelevocêencontraráclassescomoa Math,quetemumarsenalcompleto
de métodos que o auxiliam em operações numéricas como arredondamento
(
round),mínimo( min),máximo( max), seno( sin),entremuitosoutros.
Algunsexemplosdeuso:
long round = Math.round(3.99);
long max = Math.max(100, 10);
int min = Math.min(100, 10);
int abs = Math.abs(-5);
double sqrt = Math.sqrt(4);
Osvaloresdasvariáveis,respectivamente,serão:
4
100
10
5
2.0
Vocêpodeveradocumentaçãocompletadessaclasseem:
http://docs.oracle.com/javase/8/docs/api/java/lang/Math.html
Ou traclassem ui toú tilemnossodiaadiaéa
Random,vejacomoéfácil
imprimirumnúmeroaleatóriode0a10:
Random random = new Random();
System.out.println(random.nextInt(10));
Da mesma forma como onextInt, também existe um métodonext
paracadatipoprimitivo,comoo nextBooleanou nextDouble.
164

## Página 175

CasadoCódigo Capítulo10. ConhecendoaAPI
java.lang.String
ParafecharnossopasseiopelopacotepadrãodoJava,vamosentenderum
pouco melhor a classeString. É muito comum confundi-la com um tipo
primitivo,mas Stringsguardamreferênciasaobjetos. Aprovadissoéque
podemosinstanciá-ladaseguinteforma:
String java = new String( "Java");
Assim como qualquer outra variável de referência, não devemos
compará-lautilizandoooperador ==,massimo equalsquefoireescritona
classe String paracompararcadacaracteredotexto. Portanto,oresultado
docódigoaseguirserá true:
String java = "java";
String java2 = "java" ;
System.out.println(java.equals(java2));
Masalgobastanteinesperadoaconteceráaocompararmosduas Strings
destaforma:
String java = "java";
String java2 = "java" ;
System.out.println(java == java2);
Aqui, o resultado também serátrue! Por quê? Isso acontece pois, por
otimização, o Java cria umString pool ,u mt i p od ec a c h ed eStrings.
Sempreantesdeadicionaremmemória,aJVMconsultaesse poolparaver-
ificarsenãoháuma Stringigualquepossaserreutilizada.
Para que isso funcione bem, o Java não poderia permitir que a mudança
novalordeuma Stringafetasseoutras Stringsquetivessemseumesmo
valor. Porisso,todaStringéimutável .
Quer uma prova? Tente substituir o valor de umaString com seu
método replace. Ébemsimples,oprimeiroargumentoseráovaloratuale
osegundoovalorquedeverátomaroseulugar,porexemplo:
165

## Página 176

10.3. Opacotejava.lang CasadoCódigo
java.replace("v", "c");
System.out.println(java);
É natural esperar que o resultado impresso seja “jaca”, uma vez que sub-
stituímosocaractere“v”por“c”,masrodeocódigoparaveroresultado:
java
Éissomesmo ,ovalordavariá vel javacontinuouomesmo,jáquetoda
String éimutável. Paraobteroresultadoesperado,podemosresgatarore-
to rnodométodo replace,queseráumanova String. Repare:
String novaString = java.replace("v", "c");
System.out.println(novaString);
Omesmovaleparatodométodoqueaplicatransformaçõesda String,
elessempreretornamumareferêncianovaparaovalortransformado.
Agoraquejáconhecemosessacaracte rísticafundamental,podemosusar
osseusmaisde60métodos. Algunsexemplossão:
String replace = java.replace("v", "c");
String upperCase = java.toUpperCase();
String lowerCase = "JAVA".toLowerCase();
char charAt = java.charAt(0);
boolean endsWith = java.endsWith("a");
boolean startsWith = java.startsWith("s");
boolean equals = java.equalsIgnoreCase("JAVA");
Osvaloresdasvariáveis,respectivamente,serão:
jaca
JAVA
java
j
true
false
true
Dominar o pacote padrão do Java é um grande diferencial. Muitas vezes
já há algo implementado para nos ajudar com situações do dia a dia. Em
166

## Página 177

CasadoCódigo Capítulo10. ConhecendoaAPI
outras palavras, o pacotejava.lang com certeza fará parte de sua rotina.
Aproveite para estudar seus diversos outros métodos e classes. Você pode
encontraradocumentaçãocompletaem:
http://docs.oracle.com/javase/8/docs/api/java/lang/package-summary.
html
167

## Página 179

Capítulo11
CollectionFramework
11.1 Otrabalhodemanipulararrays
A princípio, deixamos nosso CarrinhoDeCompras limitando o total de
Produtos em 10 itens. Um número fixo e nem um pouco real. Uma forma
simplesdeflexibilizaraquantidadede Produtosseriaforçandoapassagem
do arrayde Produtospeloco nstru to r:
public class CarrinhoDeCompras {
private double total;
private Produto[] produtos;
private int contador =0 ;
public CarrinhoDeCompras(Produto[] produtos){
this.produtos = produtos;

## Página 180

11.1. Otrabalhodemanipulararrays CasadoCódigo
}
// outros métodos da classe
}
Issotornaseuusoumpoucomaisinteressante. Nomomentodecriarum
CarrinhoDeCompras,passamosaquantidadede Produtosquepoderáser
adicionada,como:
CarrinhoDeCompras carrinho =
new CarrinhoDeCompras(new Produto[1 0] ) ;
Mas como saber exatamente se teremos 2, 10, ou 100Produtosn e s t e
carrinho? Nãoháumvalorfixo,afinaloclientepoderácomprarquantospro-
dutos ele bem entender. O ponto é que a necessidade de passar um número
fixonomomentodeinstanciarum
array nãoa j udam ui tonestemo men to .
E o tamanho de umarray nunca muda; depois de criado, ele terá aquela
capacidadeeponto,nuncapoderáserredimensionado.
Poderíamos, sim, no momento de adicionar novos produtos verificar se
há espaço livre noarray, e caso não haja, criar um novo com mais espaço
e mover os objetos do antigo para ele. Mas isso seria muito trabalhoso, não
acha? Enãoéoúnicotrabalhoqueteríamosaoutilizarum
array.
Outra necessidade seria remover produtos doCarrinhoDeCompras.
Umaimplementaçãosimplesdométodo removeseria:
public void remove( int posicao){
this.produtos[posicao]=null;
}
Ao atribuir null para determinada posição, ganhamos uma série de
problemas. Repare como ficará nossoarray após removermos o elemento
deposição2:
170

## Página 181

CasadoCódigo Capítulo11. CollectionFramework
E agora, como faremos ao adicionar novos itens? Estávamos inserindo
sequencialmente, mas precisaremos considerar as possíveis posições vazias
nomeiodo array.
Uma possibilidade seria criar um outroarray, guardando as posições
livres,econsultá-loantesdeinserirumnovo Produto. Outrapossibilidade
seria sempre reordenar oarray depois de remover um item. Mas repare
bem,todaselasto rnariamnossocódigomaisco m plexoedifícildeman ter .
Manipular um array é bastante trabalhoso. Essas foram apenas algu-
masdasmuitasquestõesqueapareceriamemnossocódigo. Poresseeoutros
motivos, o Java2 1.2 introduziu um conjunto de classes e interfaces bastante
conhecido comoCollectionsFramework . Essa robustaAPI traz estruturas
bemmaisinteressantesparalidarcomosmaisdiferentestiposdedados.
ArrayListversus array
No lugar de trabalhar diretamente comarrays, podemos utilizar uma
ArrayList para representar a multiplicidade deProdutos e nos auxiliar
nas operações necessárias em nossoCarrinhoDeCompras. Essa classe é
uma das introduções daAPI de Collections, veja a seguir como seu uso
ésimples.
ArrayList lista = new ArrayList();
String valor = "conhecendo uma ArrayList" ;
lista.add( valor);
System.out.println(lista.contains(valor));
lista.remove( valor);
171

## Página 182

11.1. Otrabalhodemanipulararrays CasadoCódigo
System.out.println(lista.contains(valor));
Asaídaserá:
true
false
O ArrayList tem um conjunto de métodos que, na maior parte do
tempo, representam bem as nossas necessidades. O métodoremove pode
agora receber o próprio valor a ser removido, mas também tem uma sobre-
carga que recebe a posição que deve ser removida. Você pode escolher qual
opçãolheatendermelhor.
Um ponto muito interessante é que o
ArrayList, assim como as de-
mais classes daAPI de Collection, trabalham de forma genérica. Caso
contrário, haveria umaArrayList para cada tipo de dado que precisásse-
mosadicionar,comouma String,um int,oumesmoumadata. Todosos
seusmétodostrabalhamcom Object.
Portanto,oseguintecódigocompila:
ArrayList lista = new ArrayList();
lista.add(10);
lista.add("uma string");
lista.add(new Revista());
Mas já vimos o problema de trabalhar comObject dessa forma: será
necessário um casting sempre que precisarmos recuperar um valor dessa
lista. Porexemplo:
int valor =( int) lista.get(0);
E se o valor do índice zero não fosse umint? Como saber exatamente
otipodecadaelementoemcadaposiçãodalista? Trabalhardessaformanão
serianemumpoucosimples,nãoacha? Enamaiorpartedotempo,queremos
terumalistadeumúnicotipo,enãovárioscomofizemosagora. Porexemplo,
nosso
CarrinhoDeComprasdeveráterumalistade Produtos.
Para auxiliar nesse trabalho, desde o Java 5 podemos restringir o tipo
deobjetosdeumadeterminadalistautilizandoumrecursoconhecidocomo
Generics. Repare:
172

## Página 183

CasadoCódigo Capítulo11. CollectionFramework
ArrayList<Produto> produtos = new ArrayList< Produto>();
A sintaxe pode parecer estranha no começo, mas note que a única mu-
dança é que agora estamos indicando ao compilador que essa lista deve tra-
balhar com Produtos. Há dois grandes ganhos aqui, o primeiro será pela
nãonecessidadedeum castingaorecuperarvaloresdestalista. Veja:
Produto buscado = produtos.get(0);
O código fica bem mais limpo sem oscastings e evitamos as recorrentes
ClassCastExceptions. O outro ganho será a segurança de que não con-
seguiremos adicionar nada que não seja do tipoProduto nessa lista. O
seguintecódigonãocompila:
produtos.add("Eu não sou um produto" );
173

## Página 184

11.1. Otrabalhodemanipulararrays CasadoCódigo
diamondoperator doJava7
Desde o Java 7, no lugar de passar o tipo genérico duas vezes como
fizemos ao instanciar a lista deProdutos, podemos utilizar um re-
cursoconhecidocomo diamondoperator(operadordiamante),deixando
ocódigoassim:
ArrayList<Produto> produtos = new ArrayList<>();
Esse recurso era bastante limitado, funcionava basicamente se a
declaração fosse feita na mesma linha. No Java 8, a inferência de tipos
foibastantemelhoradae,comoumefeitocolateral,agorapodemosfazer
códigoscomoeste:
public class CarrinhoDeCompras {
private ArrayList<Produto> produtos;
public CarrinhoDeCompras() {
this.produtos = new ArrayList<>();
}
}
Note que só estamos instanciando o ArrayList no construtor
da classe, mas como o compilador sabe inferir bem qual o tipo do
this.produtos, conseguimos utilizar o diamante sem nenhum prob-
lema.
Vejacomoficanossaclasse CarrinhoDeComprasutilizandoumalista:
public class CarrinhoDeCompras {
private double total;
private ArrayList<Produto> produtos;
public CarrinhoDeCompras() {
this.produtos = new ArrayList<>();
174

## Página 185

CasadoCódigo Capítulo11. CollectionFramework
}
public void adiciona(Produto produto ){
this.produtos.add(produto);
}
public void remove(int posicao){
this.produtos.remove(posicao);
}
public double getTotal() {
return total;
}
public ArrayList<Produto> getProdutos() {
return produtos;
}
}
Muito mais simples, não acha? Não precisamos de um atributo
contador,nãotemosquelimitarotamanhodo array,entreoutrasdesvan-
tagenscomentadas.
É interessante reconhecer que umArrayList n ã oéu marray!E s s a
confusão é bastante comum, mas na verdadeArrayList usa um array
internamente para armazenar os dados, mas isso está bemencapsulado.E m
nenhummomentoprecisaremosrecuperarseu arrayinternoparafazerop-
eraçõesmaiscomplexas,nãotemosacessoaeleenemdeveríamos.
O ArrayList resolvetodososproblemasquecomentamosdo array.
Utilizá-lo,comcerteza,seráumamelhoropção. Masexistemoutrostiposde
listaquenãoutilizamnecessariamenteum arrayinternamente. Umexem-
plo é a LinkedList (lista ligada); enquanto aArrayList é mais rápida
parafazerpesquisas(iterar), a LinkedList ém a i srá p idapa rain serirer e-
mo verelemen tosdesuaspo n tas.
Cada estrutura tem suas vantagens, vale a pena conhecer as diferenças
entreelasparatomarumaboadecisãonomomentodeutilizarumalista.
Oq u et o d a se l a st ê me mc o m u méai n t e rface List, do pacote
java.util. Para não deixar nosso código dependendo de um tipo de lista
175

## Página 186

11.1. Otrabalhodemanipulararrays CasadoCódigo
específico(acoplamento),jáquepodemosaqualquermomentomudá-las,é
umaboapráticaprogramarvoltadoparaainterface. Reparecomoficanossa
classe
CarrinhoDeCompras:
public class CarrinhoDeCompras {
private double total;
private List<Produto> produtos;
public CarrinhoDeCompras() {
this.produtos = new ArrayList<Produto>();
}
public void adiciona(Produto produto ){
this.produtos.add(produto);
}
public void remove(int posicao){
this.produtos.remove(posicao);
}
public double getTotal() {
return total;
}
public List<Produto> getProdutos() {
return produtos ;
}
}
N o t eq u e ,a g o r aq u eot i p oArrayList aparece apenas no momento
de instanciar a lista, em todos os demais pontos nos referimos a ela como
uma List<Produto>. Isso torna nosso código muito mais flexível para
mudanças. Parautilizarum LinkedList,bastariamudarotipoemquees-
tamosdando newsemcausarnenhumefeitocolateralindesejadoaorestante
docódigo.
Aimagemaseguirmostraainterface Listealgumasdesuasimplemen-
tações:
176

## Página 187

CasadoCódigo Capítulo11. CollectionFramework
Parafinalizarnossamigraçãode arraypara List,precisamoscorrigir
oe r r od ec o m p i l a ç ã od ac l a s s eRegistroDeVendas, no momento em que
estamositerandopelositensdocarrinho:
Produto[] produtos = carrinho.getProdutos();
for (Produto produto : produtos){
System.out.println(produto);
}
177

## Página 188

11.2. OrdenandonossaListdeprodutos CasadoCódigo
A única mudança necessária será no tipo de retorno do método
getProdutos.B a s t am u d a rd eProduto[]para List<Produto>etodo
orestantecontinuaráigual.
List<Produto> produtos = carrinho.getProdutos();
for (Produto produto : produtos){
System.out.println(produto);
}
Isso significa que o enhanced-for também funciona com qualquer
tipo de List (na verdade, com qualquerIterable, como veremos mais
àfrente).
11.2 OrdenandonossaListdeprodutos
Ao imprimir os valores dessa lista, você perceberá que serão exibidos na
mesma ordem em que foram inseridos. Mas é fato que, sempre que estamos
trabalhandocomlistas,entreoutrostiposdecoleções,énaturalanecessidade
deexibirseusdadosdeformaordenadaseguindoalgumoutrocritério.
AtéoJava7,podíamosutilizarométodoestático
sort,presentenaclasse
java.util.Collections:
List<String > nomes = new ArrayList<>();
nomes.add("Rodrigo Turini" );
nomes.add("Adriano Almeida" );
nomes.add("Paulo Silveira");
Collections .sort(nomes);
System.out.println(nomes);
Executandoessecódigo,oresultadoserá:
[Adriano Almeida, Paulo Silveira, Rodrigo Turini]
Éimportanteperceberqueométodo sortefetivamentemodificouaes-
truturainternadalista,nestecasodeixando-aemordemalfabética.
178

## Página 189

CasadoCódigo Capítulo11. CollectionFramework
Ac l a s s eCollections possui diversos outros métodos que podem ser
muitoúteisquandovocêestátrabalhandocomcoleções,principalmentecom
Java7oumenor .LogoveremosqueoJava8introduziudiversosrecursospara
tornarseutrabalhocomcoleçõesaindamaispráticoefuncional.
Alguns outros exemplos de métodos da classe
Collections são: o
reverse,parainverteraordemdoselementosdalista;o copy,paracopiar
oselementosdeumalistaparaoutra;etambémo emptyList,queretornará
uma lista vazia. Você pode ver os diversos métodos dessa classe em sua de-
talhadadocumentação:
http://docs.oracle.com/javase/8/docs/api/java/util/Collections.html
O
sortemnossa List<Strings>utilizoucomocritériodeordenação
aordemalfabética. Masqualseriaoresultadodoseguintecódigo?
List<Produto> produtos = new ArrayList<>();
// populando a lista com alguns produtos
Collections .sort(produtos);
Essecódigonãocompila! Observeasaída:
The method sort(List<T>) in the type Collections
is not applicable for the arguments (List<Produto>)
Fazsentido,afinalqualseriaocritériodeordenação? Precisamosensinar
aométodo sortqualelementodevevirantesdequal,ouseja,comoordenar
elementosdotipo Produto.
O método sort precisa receber uma lista de elementos comparáveis,
que possuam um método específico ensinando-o como deve comparar tais
elementos. Para garantir que os elementos passados tenham esse método,
mais uma vez a API do Java fez uso de uma interface! Todo elemento or-
denável deve implementar a interface
java.lang.Comparable, que pos-
suiométodo compareTo.
Para que nosso código compile, podemos dizer que todoProduto im-
plementa Comparable,masreparenocódigoaseguir:
179

## Página 190

11.2. OrdenandonossaListdeprodutos CasadoCódigo
public interface Produto extends Comparable<Produto>{
double getValor();
}
Pode parecer um pouco estranho na primeira vez que você olhar, afinal
estamos utilizando extends,en ã oo implements. Já percebeu por quê?
Como Produto é uma interface, ela apenas herdará as obrigações da inter-
face Comparable. Já as classes que a implementarem agora além da obri-
gação de escrever seu métodogetValor terão também que implementar
compareTo,oquelogoveremos.
Apenas um último detalhe antes de partirmos para a implementação do
método: vocênotouqueo Comparabletambémfazusodo genericsdoJava
5? Se não tinha notado, dê uma boa olhada na assinatura da interface, que
tem um Comparable<Produto>. Com isso, eliminamos a necessidade de
fazero castingde Object,queéotipodoparâmetrodeseumétodo int
compareTo(Object).
Pronto, finalmente podemos partir para a implementação, que poderá
ser feita na classe abstrataProduto e, portanto, replicada a suas subclasses
LivroFisico, Ebook e MiniLivro. O critério de comparação será seu
valor:
public abstract class Livro implements Produto {
// código omitido
@Override
public int compareTo(Produto outro){
if (this.getValor() < outro.getValor()){
return -1;
}
if (this.getValor() > outro.getValor()){
return 1;
}
return 0;
}
}
180

## Página 191

CasadoCódigo Capítulo11. CollectionFramework
Om e s m op o d es e rf e i t on ac l a s s eRevista,q u en ã oéfi l h ad eLivro
mas também é um Produto que deve ser ordenado por valor. O código
pareceuconfuso? Nãosepreocupe,vamosentendê-loumpoucomelhor.
N o t eq u eom é t o d ocompareTo retorna um int. Devemos retornar
0 (zero) se o objeto comparado (parâmetrooutro) for igual a este objeto (
this),umnúmeronegativoseesteobjetoformenor(devavirantesquando
ordenado) que o objeto passado, ou um número positivo caso seja maior
(devavirdepois).
Executeoseguintecódigoparaveroresultadoemprática:
public class OrdenandoComJava {
public static void main(String[] args){
Autor autor = new Autor();
autor.setNome("Rodrigo Turini" );
LivroFisico fisico = new LivroFisico(autor);
fisico.setNome("Java 8 Prático");
fisico.setValor(59.90);
Ebook ebook = new Ebook(autor);
ebook.setNome("Java 8 Prático");
ebook.setValor(29.90);
List<Produto> produtos = Arrays.asList(fisico, ebook);
Collections .sort(produtos);
for (Produto produto : produtos){
System.out.println(produto.getValor());
}
}
}
Asaídaserá:
29.9
59.9
181

## Página 192

11.3. Gerenciandocuponsdedesconto CasadoCódigo
Outrasimplementações
Como estamos comparando apenas o valor do Produto,
poderíamos simplificar nossa implementação retornando apenas a
subtração de um valor pelo outro. Repare como nosso código fica mais
simples:
public abstract class Livro implements Produto {
// código omitido
@Override
public int compareTo(Produto outro){
return this .getValor() - outro.getValor();
}
}
Maissimples, nãoacha? Alternativamente, tambémpoderíamosuti-
lizar o método Integer.compare passando os dois valores como
parâmetro. Experimente utilizar alguma dessas estratégias para deixar
seucódigomaissimples,essaéumapráticabastantecomum.
11.3 Gerenciandocuponsdedesconto
A g o r aq u en o s s ac l a s s eCarrinhoDeCompras já está bem resolvida, pode-
mos seguir para uma outra necessidade de nosso projeto. Precisamos agora
gerenciarcuponsdedescontopromocionais.
Como ponto de partida, podemos criar a classe
GerenciadorDeCupons q u ep o s s u ii n t e r n a m e n t eu m al i s t ac o ma l -
gunscuponsjácadastrados. Repare:
public class GerenciadorDeCupons {
private List<String> cupons;
public GerenciadorDeCupons() {
182

## Página 193

CasadoCódigo Capítulo11. CollectionFramework
this.cupons = Arrays.asList("CUP74", "CUP158",
"CUP14", "CUP52", "CUP21", "CUP221", "CUP91" ,
"CUP327", "CUP410", "CUP275", "CUP484", "CUP207",
"CUP96", "CUP119", "CUP174", "CUP291", "CUP1",
"CUP115", "CUP222", "CUP272");
}
}
Note que setamos o método estático asList da classe
java.util.Arrays para criar nossa lista. Poderíamos criar um
ArrayList e chamar seu método add para cada elemento, mas é co-
mum utilizar esse novo método para simplificar esse processo. O método
asList é uma fábrica (factory)d e List e, com certeza, será muito útil em
seudiaadia.
Nossopróximopassoserácriarummétodoparavalidaroscuponspassa-
dos pelo cliente. Ele retornará umboolean indicando se o cupom passado
e s t áo un ã op r e s e n t ee mn o s s aList<String> cupons . Vamos chamá-lo
de validaCupom:
public boolean validaCupom(String cupom ){
return this .cupons.contains(cupom );
}
Note que utilizamos o já conhecido métodocontains para fazer essa
consulta. Bemsimples,nãoacha?
Já estamos prontos para testar esse código. Vamos criar uma nova classe
chamada ConsultaDeDescontos, que deve utilizar esse novo método, o
validaCupom. Repare:
public class ConsultaDeDescontos {
public static void main(String[] args){
GerenciadorDeCupons gerenciador =
new GerenciadorDeCupons ();
if(gerenciador.validaCupom("CUP1234")){
System.out.println("Cupom de desconto valido." );
183

## Página 194

11.3. Gerenciandocuponsdedesconto CasadoCódigo
// aplica o desconto desse cupom
} else {
System.out.println("Esse cupom não existe." );
}
}
}
Rode esse código para ver o resultado. Como o cupom não existe em
nossalista,asaídaserá:
Esse cupom não existe.
Trabalhar com umaList aqui resolve o problema, mas ela não é a es-
trutura ideal para fazer esse trabalho. Normalmente, trabalhamos com uma
listaquandoseuselementosinternospodemrepetiresuaordemtemalguma
i m p o r t â n c i a ,m a sn o t eq u en ã oée s s eoc a s od en o s s o sc u p o n s .U mc u p o m
é único, não há repetições e, além disso, a ordem deles não importa, afinal
estamosutilizandoessesdadosapenasparaconsulta.
Emcasoscomoeste,podemosutilizarumaoutraestruturadedadosbas-
tanteinteressante,umconjunto(
java.util.Set).
java.util.Set
Umconjunto(ou SetemJava)funcionadeformaparecidacomoscon-
juntos da matemática. Ela é uma coleção, assim como aList, mas em que
não há repetição de seus dados internos. Além disso, sua ordem não é nec-
essariamente a ordem em que os valores foram inseridos, isso pode variar
bastantedecadaimplementação.
Assimcomoa
List,o Setéapenasumainterface. Parautilizarum Set,
precisamos instanciar alguma de suas implementações, como aHashSet,
queéumadasimplementaçõesmaisusadas. Observecomoficanossocódigo
daclasse
GerenciadorDeCupons:
public class GerenciadorDeCupons {
private Set<String> cupons;
public GerenciadorDeCupons() {
184

## Página 195

CasadoCódigo Capítulo11. CollectionFramework
this.cupons = new HashSet<String>();
cupons.addAll(Arrays.asList("CUP74", "CUP158",
"CUP14", "CUP52", "CUP21", "CUP221", "CUP91" ,
"CUP327", "CUP410", "CUP275", "CUP484", "CUP207",
"CUP96", "CUP119", "CUP174", "CUP291", "CUP1",
"CUP115", "CUP222", "CUP272"));
}
public boolean validaCupom(String cupom ){
return this .cupons.contains(cupom);
}
}
Notequeutilizamosométodo addAllparafacilitaressamudança. Mas
é natural adicionar elementos noSet chamando seu método add, assim
comona List. Outrodetalheimportanteéquecontinuamosprogramando
voltados para a interface, isto é, apesar de darnew em HasSet,ot i p od o
atributo cuponséum Set. Essaéesempreseráumaexcelenteprática,posto
quediminuioacoplamentodenossaclasseefacilitaevoluçõesnofuturo.
Nosso código continua funcionando assim como antes. Rode a classe
ConsultaDeDescontos para confirmar! Aparentemente, tudo está igual,
masnaverdadealgumascoisasmudaram.
O primeiro ponto importante a se perceber é que, mesmo que você adi-
cione mais 500 mil cupons iguais nesse conjunto, ao mandar imprimir o seu
tamanho (size) ele ainda será 20. Você pode rodar o código a seguir para
confirmarisso:
HashSet<String> set = new HashSet<String>();
set.add("Não há repeticão em Conjuntos" );
set.add("Não há repeticão em Conjuntos" );
set.add("Não há repeticão em Conjuntos" );
set.add("Não há repeticão em Conjuntos" );
set.add("Não há repeticão em Conjuntos" );
System.out.println(set.size());
Qual foi o valor da saída? Exatamente1, ele ignorou as repetições. Para
ajudar a saber quando você está inserindo uma repetição em umSet,s e u
185

## Página 198

11.4. java.util.Map CasadoCódigo
11.4 java.util.Map
Nosso GerenciadorDeCupons já está quase completo. O próximo passo
seráaplicarodescontoespecíficoparadeterminadocupomquefoivalidado.
Mascomovincularumcupomúnicocomoseuvalordedesconto?
Essa é uma necessidade muito comum: vincular um objeto a uma chave
única, para conseguir buscar esse valor rapidamente. Poderíamos resolver
isso com uma lista, mas já vimos que essa não é a melhor estrutura quando
queremosfazerbuscas.
188

## Página 203

Capítulo12
StreamsenovidadesdoJava8
AAPIdeCollectionsébastanterobusta,semdúvidas. Hámuitooqueexplo-
rar em suas diversas estruturas e soluções. Mas o fato é que estamos falando
de uma API gigante e com mais de 15 anos, que com certeza possui algumas
limitaçõesecaracterísticasquenãopoderiamserevoluidassemquehouvesse
uma sobrecarga ou ainda quebra de compatibilidade (veremos no próximo
capítulooquantoissoéimportanteparaoJava).
PoresseediversosoutrosmotivosoJava8introduziudiversasnovidades
que nos trazem uma forma bem mais interessante e funcional de trabalhar
comnossascoleções. Veremosalgumasdessasnovidadesduranteocapítulo.
12.1 OrdenandocomJava8
Vimosqueumamaneiradeordenara List<Produto>eratornandoseusel-
ementoscomparávis, paraissoimplementando java.lang.Comparable.

## Página 204

12.1. OrdenandocomJava8 CasadoCódigo
Mas e se você tiver mais de um critério de ordenação? E se você quiser em
algunsmomentoscompararum Livropeloseu valoreemoutrospeloseu
nome?
Até o Java 7 uma forma de fazer isso seria criando uma nova classe, um
comparadorde Livropornome. Essaclasseprecisavaimplementarainter-
face java.util.Comparator,algoco mo:
public class ComparadorPorNome implements Comparator<Livro>{
@Override
public int compare( Livro l1 , Livro l2 ){
return l1.getNome().compareTo( l2.getNome());
}
}
O método sort da Collection t e mu m as o b r e c a r g aq u er e c e b eu m
Comparatorcomoparâmetro,portantoagorabastafazer:
Collections .sort(livros, new ComparadorPorNome());
Vamos ver esse código na prática! Crie a classeNovidadesDoJava8 e
adicioneoseguintecódigoparatestar:
public class NovidadesDoJava8 {
public static void main(String[] args){
Autor autor = new Autor();
autor.setNome("Rodrigo Turini" );
Livro javaoo = new LivroFisico(autor);
javaoo.setNome("Java O.O." );
Livro java8 = new LivroFisico(autor);
java8.setNome("Java 8 Prático");
Livro ruby = new LivroFisico(autor);
ruby.setNome("Livro de Ruby" );
194

## Página 205

CasadoCódigo Capítulo12. StreamsenovidadesdoJava8
List<Livro> livros = Arrays.asList(javaoo , java8);
Collections .sort(livros, new ComparadorPorNome());
for (Livro livro : livros ){
System.out.println(livro.getNome());
}
}
}
Agoraexecuteocódigoereparequeasaídaserá:
Java 8 Prático
Java O.O.
Livro de Ruby
Classesanônimaseolambda
O que pode incomodar bastante dessa solução é que para cada
novo critério de ordenação, precisaríamos criar uma nova classe como a
ComparadorPorNome. Ainda que seu código seja bem pequeno e não seja
reutilizadoemnenhumoutrolugar.
UmaalternativabastanteutilizadaatéoJava7eramasconhecidasclasses
anônimas. Vocêpodesimdar newemumainterface,masteráqueimplemen-
tarseusmétodosalimesmo,numamesm ainstrução. Podemosfazerissocom
ainterface Comparator,n ol uga rdecria rac la s seComparadorPorNome,
podemosfazer:
Collections.sort(livros, new Comparator<Livro>() {
@Override
public int compare( Livro l1 , Livro l2 ){
return l1.getNome().compareTo( l2.getNome());
}
});
Isso mesmo, é o mesmo código da classeComparadorPorNome, mas
declaradonumaúnicainstrução. Esserecursoéconhecidocomoclasseanôn-
ima, pois afinal essa classe não tem nem mesmo um nome! Achou a sintaxe
195

## Página 206

12.1. OrdenandocomJava8 CasadoCódigo
estranha? Feia? difícildeler? Bem... euconcordo! Issopoluibastanteonosso
código.
ParasimplificaresseprocessooJava8introduziualgumasmudanças,uma
delasfoiadicionandoométodo sortnaprópriainterface List!P o d ep a r e -
cerumamudançasimples,masagorapodemosfazer:
livros.sort(new Comparator<Livro>() {
@Override
public int compare(Livro l1, Livro l2 ){
return l1.getNome().compareTo( l2.getNome());
}
});
Para não quebrar a compatibilidade da interfaceList, esse método
sortéummétodoconcreto,comcódigodentro! Lembradonomedessere-
curso? Nocapitulodeinterfacebrevementecomenteisobreostais default
methods,heisumbomexemplo:
default void sort( Comparator<? super E> c){
Collections.sort(this, c);
}
Isso mesmo, esse métododefalt da List apenas delega a chamada
paraométodo sortde Collections,quejáfaziabemestetrabalho. Mas
issoaindanãoresolvetodososproblemasdeordenação,nãoé? Entãovamos
paraoutranovidade.
Tambémnocapitulodeinterfaces,vimosbrevementequeoJava8intro-
duziu o conceito deinterfacesfuncionais. Em poucas palavras, uma inter-
face com um único método abstrato pode ser considerada funcional, como
é o caso da interface
Comparator q u ep o s s u ia p e n a som é t o d ocompare.
Comissoganhamosalgumaspossibilidades,comoporexemplotransformar
aquela classe anônima em umaexpressãolambda! Uma primeira forma de
fazerissoseria:
livros.sort((Livro l1 , Livro l2 )- >{
return l1.getNome().compareTo(l2.getNome());
});
196

## Página 207

CasadoCódigo Capítulo12. StreamsenovidadesdoJava8
Notequeadiferençadessecódigoparaaclasseanônimaéquedeixamos
apenasosparâmetrosdométodo compare,seguidosdooperador -> es ua
implementação. Como o métodosort espera receber umComparator,o
co m p ilado rjáinfer equeesseéoti podaexpressão lambda .
Podemossimplificaraindamaisessecódigo,retirandootipo Livrodos
parêmetros,aschaves,o returneatémesmooponto-e-virgula. Repare:
livros.sort(
(l1, l2)- >l1.getNome().compareTo( l2.getNome())
);
Esse é um conceito um pouco mais avançado e com certeza
pode parecer bastante estranho ou mesmo assustador no ínicio. O
código (l1, l2) -> l1.getNome().compareTo(l2.getNome())
resulta em uma instância de Comparator que devolve
l1.getNome().compareTo(l2.getNome(). Não há necessidade
d ed e c l a r a rot i p o(Livro) dos parâmteros, o próprio compilador sabe
inferir isso pra você. Não há necessidade da palavrareturn e nem mesmo
dechaves,jáquetemosumaúnicainstruçãoapósooperador ->.
Para tornar o código ainda mais enxuto e um pouco mais fluente, o
métododefault comparingfoiadicionadonainterface Comparator. Eleé
umafábrica( factory)de Comparator,tudoqueprecisamosfazerépassar
umaexpressãolambdacomocritériodecomparaçãocomoaseguir:
livros.sort(comparing(l -> l.getNome()));
Notequecomoháapenasumparâmetronesse lambda,nãoprecisamos
passá-lo dentro de parênteses. Rode o código para ver o resultado! O que
acha?
Simplificandoaindamaiscom method reference
A expressão lambda l -> l.getNome() apenas diz ao comparing
qual o método que deverá ser utilizado em sua comparação. Ele está ape-
nas referenciando um método, neste caso o
getNome. Em casos como este
podemosaindafazer:
livros.sort(comparing(Livro::getNome));
197

## Página 208

12.2. forEachdoJava8 CasadoCódigo
Esse é um outro recurso do Java 8, conhecido como method
reference. Note que sua sintaxe é o nome da classe seguido de:>: eo
nomedométodo. Esserecursopodeserutilizadosemprequetemosumaex-
pressãolambdacomoa l -> l.getNome() ,queapenasdelegaachamada
deummétodo.
12.2 forEachdoJava8
Outro default method quecomtotalcertezafarápartedeseudiaadiaé
o forEach,presentenainterface Iterable. Notenaformacomoestamos
iterandopelalistadelivrosutilizandoo enhanced-for:
for (Livro livro : livros ){
System.out.println(livro.getNome());
}
NoJava8agorapodemosfazer:
livros.forEach(l -> System.out.println(l.getNome()));
Ométodo forEach,assimcomoamaiorpartedos default method s,
recebe uma interface funcional como parâmetro. Portanto note que foi pos-
sivelutilizaruma
expressão lambda pararepresentarnossasintenções.
Ol a m b d al -> System.out.println(l.getNome()) nada mas
dizdoque: “paracadalivro,chameométodoprintlnimprimindoseunome”.
12.3 Filtrandolivrospeloautor
Alémdaformadeordenareiterar,oJava8mudoubastanteaformadefazer
algumasoperaçõesrotineirasdequandoestamostrabalhandocomcoleções.
Querumexemploprático?
OtrabalhodefiltrarumaCollection
Dadaumalistadelivros,queremosfiltarapenasosquetenhamapalavra
Java em seu nome. Até o Java 1.7 uma das formas mais tradicionais de se
fazer isso seria criando uma nova lista para o resultado e condicionando os
elementosquedeveriamserinseridos,comoaseguir:
198

## Página 209

CasadoCódigo Capítulo12. StreamsenovidadesdoJava8
List<Livro> filtrados = new ArrayList<>();
for (Livro livro : livros ){
if (livro.getNome().contains( "Java")) {
filtrados.add(livro);
}
}
Para testar, adicione esse código na classeNovidadesDoJava8 e logo
depois mostre os resultadosdessa lista, fazendo um simplesfor como a
seguir:
for (Livro livro : filtrados){
System.out.println(livro.getNome());
}
Notequeasaídaserá:
Java 8 Prático
Java O.O.
Excelente, resolvemos o problema! Mas de uma boa olhada em seu
código... o que achou? Note que além de ser muito verboso, ele exigiu a cri-
ação de uma lista intermediária para o resultado. Esse é sem dúvidas um
códigobastanteimperativo.
Operações comuns como essa, filtrar elementos de uma coleção, estão
agorapresentesemumanovaAPI,conhecidacomo
Stream.O Streamtraz
para o Java uma forma mais funcional de trabalhar com as nossas coleções,
usando uma interface fluente! Separando as funcionalidades do
Stream
da Collection, também ficou mais fácil de deixar claro que métodos são
mutáveis,evitarproblemadeconflitodenomedemétodos,entreoutros.
Streameofilter
Comocriarum Stream? Issoébemsimples,umnovométodo default
chamado stream foi definido na interfaceCollection. Com isso, basta
fazer:
Stream<Livro> stream = livros.stream();
199

## Página 210

12.3. Filtrandolivrospeloautor CasadoCódigo
Apartirdessenosso Stream<Livro>conseguimosutilizarporexemplo
ométodo filter,comoaseguir:
livros.stream().filter(l -> l.getNome().contains( "Java"));
Estamos fazendo a mesma coisa que aquelefor com um if dentro do
Java7,sóqueagoradeumaformamuitomaisdeclarativa!
Nãodeixedetestar,mudeocódigodaclasse NovidadesDoJava8ees-
crevaoseguinte forparaexibiralistade livros:
for (Livro livro : livros ){
System.out.println(livro.getNome());
}
Rodeocódigoeor esul tados erá:
Java 8Prático
Java O.O.
Livro de Ruby
Ops, esse Livro de Ruby não deveria estar no resultado! O filtro não
funcionou? Naverdadefuncionou,masaAPIde Streamséimutável,issoé,
nãoalterasuacoleçãoinicial. Vocêpodefazerquantastransformaçõesquiser
semsepreocuparcomefeitoscolateraisemsualista.
Portanto, no lugar de iterar na lista original podemos utilizar o método
forEachtambémpresentenaAPIde Streamsdaseguinteforma:
livros.stream()
.filter(l -> l.getNome().contains( "Java"))
.forEach(l -> System.out.println(l.getNome()));
Agorasim,aoexecutarocódigoteremosapenasoselementosfiltrados:
Java 8Prático
Java O.O.
Claro,o filteréapenasumdoszilharesmétodospresentesnessanova
API.Vocêpodeveralistacompletaemealgunsexemplosem:
http://docs.oracle.com/javase/8/docs/api/java/util/stream/Stream.html
200

## Página 211

CasadoCódigo Capítulo12. StreamsenovidadesdoJava8
VimosnessecapituloapenasumpoucodomuitoqueoJava8introduziu
com seus novos recursos e APIs. O seguinte post do blog da caelum fala um
poucomaissobreessasnovidades:
http://blog.caelum.com.br/o-minimo-que-voce-deve-saber-de-java-8/
OlivroJava8Prático
Junto com Paulo Silveira escrevi o livroJava 8 Prático: Lambdas,
Streamseosnovosrecursosdalinguagem ,queentraafundoemcadade-
talheesumarizaosnovosrecursosdoJava. Sevocêgostoudasnovidades
comcertezavaigostardeseuconteúdo:
http://www.casadocodigo.com.br/products/livro-java8
201

## Página 213

Capítulo13
UmpoucodahistóriadoJava
13.1 Origemdalinguagem
Já colocamos em prática muitos dos conceitos da orientação a objetos e re-
cursos específicos da linguagem Java, mas para concluir essa primeira parte
doestudoéfundamentalconhecermosumpoucodesuahistória.
Acredito que quando foi iniciado oGreen Team,u mp r o j e t od aSun Mi-
crosystemscujo objetivo era criar uma plataforma de computação interativa,
ninguém imaginou que esse seria o início de uma linguagem que mudou o
rumodahistóriadaprogramaçãoequeatualmentepossuimaisde9milhões
dedesenvolvedores. Em1992foifeitaaprimeirademonstraçãodesseprojeto,
mas apenas em 1995 que foi anunciado o lançamento oficial da plataforma
Java.
Na época o uso principal da linguagem era focado em navegadores web

## Página 214

13.2. Escrevaumavez,rodeemqualquerlugar! CasadoCódigo
pararodarpequenasaplicações(ostãoconhecidos applets),tantoquefoiin-
seridano Netscape Navigatorqueeraoprincipalnavegadordomomento.
Desdeentãoagrandeidéiadalinguagemévocêescreverumaaplicaçãoe
executá-lanosdiferentesdispositivosexistentes. Ouseja,portabilidadeéuma
das características mais fortes e presente desde suas origens. Claro que essa
não é a única característica forte da linguagem, que também é robusta, par-
alelizável,seguraedentrediversasoutrasqueaindaserãomelhordetalhadas:
estável.
Algumas das características que tornam o Java muito bem vindo como
linguagem são sua estabilidade e retrocompatibilidade. Você pode reparar
issopelan umeraçãodesuasversões,r epa r eq uea pesa rdaestra tégiadema r -
keting de chamá-lo de Java 8, por exemplo, a versão continua sendo 1.8. Ou
seja,o1sem preestápresen teindicandoqueaindanãohouveumaquebrade
compatibilidadedesdeseulançamento.
Podemos então em 2014, com a versão mais recente da linguagem, com-
pilar e executar uma aplicação escrita por volta de 1995 com Java 1.0.2 sem
nenhuma dificuldade. Isso nos dá uma boa segurança de que uma atualiza-
çãodeversãonãoseráumproblema,porexemplo.
Há uma comunidade conhecida como JCP (Java Community Process)
cujoobjetivoégarantiressepadrãodeestabilidadeecompatibilidademulti-
plataforma da tecnologia Java. Você pode ler mais sobre a JCP e suas pro-
postasem:
https://www.jcp.org/en/introduction/overview
13.2 Escrevaumavez,rodeemqualquerlugar!
Diferente das demais linguagens, uma aplicação Java pode ser executada em
qualquerumdosdiferentessistemasoperacionaisexistentes,comoporexem-
plo Windows, Linux ou Mac OS. Essa possibilidade abre muitos caminhos e
foiumdosprincipaisfatoresquetornaramalinguagemtãoatraentepromer-
cado. Exibindo esse benefício, o Java teve como slogan oficial o termoWrite
once,runanywhere (escrevaumavez,rodeemqualquerlugar).
Agrandechaveparaessaportabilidadeéamáquinavirtual,ouJVM( Java
VirtualMachine). Nolugardeinstruçõesnativasparaumdeterminadohard-
204

## Página 215

CasadoCódigo Capítulo13. UmpoucodahistóriadoJava
ware,apóscompiladoumcódigo-fonteemJavaétraduzidoparaumformato
conhecidocomo bytecode.E s s ebytecodeindependedaarquiteturadosistema
emquefoigeradoeportantopoderáserexecutadoemqualquerplataforma,
contanto que ela tenha uma JVM instalada. A imagem a seguir representa
esseprocesso:
Inicialmente o desempenho da linguagem foi um fator preocupante,
tendo como parâmetro de comparação as demais linguagens compiladas em
instruções nativas para uma determinada plataforma. Ao ganhar em porta-
bilidade a linguagem sofreu um grande impacto por adicionar essa camada
intermediária. Empoucotempoodesempenhodeixoudeserumproblema,
com introduções e tecnologias que serão melhor detalhadas a seguir nas de-
scriçõesdasdiferentesversõesdaplataforma.
13.3 Linhadotempo
A linguagem foi sem duvida um caso de sucesso. Em sua primeira ver-
são tinha cerca de 250 classes e agora conta com mais de 4.200, ricas APIs,
poderososrecursoseéexecutadapormaisde3bilhõesdedispositivos. Para
entendermos melhor todo esse sucesso, precisamos conhecer um pouco de
suahistória,algunsdeseusprincipaisacontecimentoseintroduções.
205

## Página 216

13.3. Linhadotempo CasadoCódigo
Java1
Em 1991 a linguagem foi originalmente chamada deOak (carvalho, em
inglês) por influência da vista na janela do escritório de seu criador, James
Gosling. Somente a partir de sua primeira versão estável, que foi a 1.0.2 em
1995,passouaserchamadadeJava1.
Existiam diversos bugs nesse momento e a performance era bastante
problemática.
Java1.2
C o mm a i sd e2m i l h õ e sd ed o w n l o a d se ms u av e r s ã oa t u a l ,e m1 9 9 8f o i
lançado o Java 1.2. Nessa versão diversos bugs foram corrigidos e a perfor-
mance foi consideravelmente melhorada. Um dos principais fatores respon-
sáveisporessamelhorafoiaintroduçãodocompiladorJIT( Just In Time)em
que a compilação é feita durante a excecução do programa (emruntime)a o
invésdeantesdesuaexecução.
OutraintroduçãomuitoimportantedessaversãofoiaAPIde Collections,
queseráprofundamenteestudadamaisadiante.
Java2
Por uma estratégia de marketing da época a linguagem passou a se
chamarJava2(independentedesuaversão,porexemploaversão1.3era
conhecidacomo Java(TM)2Platform,StandardEditionversion1.3 ). Ape-
nasem2004naversão1.5queo2deixoudefazerpartedonomedalin-
guagem.
Java1.3
Em2000amaisnovaversãodojavafoilançada,oJava1.3. Alavancando
aindamaissuaperformace,umaJVMconhecidacomo HotSpotpassouasera
máquinavirtualpadrãodaSun. EssaJVMcombinavainterpretaçãodecódigo
ecompilaçãoJIT(emtempodeexecução).
OseucódigoJavaaindaerainicialmenteinterpretado,masduranteaex-
ecução do programa a JVM passou a identificar os pontos executados com
206

## Página 217

CasadoCódigo Capítulo13. UmpoucodahistóriadoJava
maior frequência (conhecidos como pontos quentes, ouHotSpots )eq u a n d o
necessário transformava esses códigos em instruções nativas da plataforma
quesãoexecutadasdiretamentenohardware.
Java1.4
Chegando a quase 3 mil classes, a API foi enriquecida com introduções
como expressões regulares (Regular Expression), processamento de XML,
Logging emuitomaisemsuaversão1.4,lançadaem2002. Essafoiaprimeira
versãodoJavadesenvolvidanoâmbitodaJCP( Java Community Process).
Java1.5
Semduvidaumadasversõesmaisimportantes, oJava1.5foilançadoem
setembro de 2004. Dentre diversas outras,Generics, imports estáticos, ano-
tações (metadata) e boxing de tipos primitivos foram algumas de suas novi-
dades.
Essa versão também ficou bastante conhecida por introduzir uma forma
maissucintadeiteraremcoleções,o enhancedfor queserámelhordetalhado
adiante.
Uma nova estratégia de marketingsurge. Para melhor refletir o nível de
maturidade,estabilidade,escalabilidadeesegurançadaplataforma,oJava1.5
deixou se ser Java2ep a s s o uas e rc o n h ecido como Java 5. Mas claro, não
estamosfalandodeumaquebradecompatibilidade,aversãocontinuasendo
1.5.
Desdeentãoasversõesdalinguagempassaramaserconhecidaspeloseu
ultimonumero.
Java1.6
A fim de impulsionar ainda mais a adoção da tecnologia, a Sun tornou
oJ a v aopen source. Ou seja, seu código foi aberto para comunidade com a
licençaGNU( GeneralPublicLicense ),amesmautilizadapelosistemaopera-
cional Linux. Além disso, diversas otimizações no core da plataforma e na
JVMmarcaramaversão1.6.
207

## Página 218

13.3. Linhadotempo CasadoCódigo
Java1.7
Quatro anos após sua ultima versão, essa foi a primeira versão após a
aquisição da Sun pela Oracle. O Java 7 foi lançado sob uma nova perspec-
tiva, teve como novidades uma nova API de I/O, recursos como o operador
diamante(diamond operator<>)eo try-with-resources.
Java8
A mais atual versão da plataforma sem duvida apresentou mudanças im-
pactantes para a linguagem. Seu lançamento aconteceu em março de 2014,
depoisde3anosdemuitaespera. Diversosrecursosforamintroduzidosnessa
versão, defalt methods, expressões lambdas emethod reference, que vimos
brevementenocapituloanterior,foramalgumdeles.
A versão também conta com uma nova API de datas baseada na con-
hecidabiblioteca Joda Time,alémdeumaformamaisfuncionaldetrabalhar
co msuascoleçõesco maAPIdeStream .
Vimosqueatéentãoseucódigoqueeraescritodessaforma:
List<Usuario> usuariosFiltrados = new ArrayList<>();
for(Usuario usuario : usuarios){
if(usuario .getPontos() > 100) {
usuariosFiltrados.add(usuario );
}
}
Collections .sort(usuariosFiltrados, new Comparator<Usuario >() {
public int compare( Usuario u1, Usuario u2){
return u1.getNome().compareTo( u2.getNome());
}
});
for(Usuario usuario : usuariosFiltrados){
System.out.println(usuario);
}
AgoracomJava8podeserescritodeformamuitomaisdeclarativaefun-
cional:
208

## Página 219

CasadoCódigo Capítulo13. UmpoucodahistóriadoJava
usuarios.stream()
.filter(u -> u.getPontos() > 100)
.sorted(comparing(Usuario::getNome))
.forEach(System.out::println);
V ocêpodelermaissobreahistóriadaplataformaeveratimeline completa
em:
http://www.java.com/en/javahistory/
http://oracle.com.edgesuite.net/timeline/java/
209

## Página 221

Capítulo14
Continuandoseusestudos
Não deixe de praticar cada exercício proposto durante o Livro e sempre ir
alémcomnovostestesecenáriosmaiscomplexos.
Há diversas formas de continuar seus estudos, o GUJ é uma delas. Não
apenas para postar suas dúvidas, mas também respondendo aos demais
usuários e sendo um membro ativo da comunidade Java do Brasil. Ensinar
é uma das mais efetivas formas de aprender, espero te ver ensinado e apren-
dendoporlá:
http://www.guj.com.br
Outro caminho natural para continuar seus estudos é o livroJava 8
Prático: Lambdas, Streams e os novos recursos da linguagem. Neleexplicamos
detalhadamente desde a sintaxe até o uso prático de cada novidade da mais
esperadaversãodoJava.
http://www.casadocodigo.com.br/products/livro-java8

## Página 222

14.1. Entreemcontatoconosco CasadoCódigo
14.1 Entreemcontatoconosco
Encaminhesuasdúvidasoucrietópicosparadiscussãonalistaquefoicriada
especialmen teparaesselivr o:
https://groups.google.com/d/forum/livro-java-oo
Alémdeperguntar,vocêtambémpodecontribuircomsugestões,críticas
emelhoriasparanossoconteúdo. Todasserãomuitomaisdoquebemvindas.
212