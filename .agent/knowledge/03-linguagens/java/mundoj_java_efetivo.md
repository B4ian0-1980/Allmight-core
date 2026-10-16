---json
{
  "id": "mundoj_java_efetivo",
  "title": "MundoJ Java efetivo",
  "categoria": "03-linguagens",
  "subcategoria": "java",
  "resumo": "**Arquivo Original:** `MundoJ Java efetivo.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "efetivo",
    "java",
    "linguagens",
    "mundoj"
  ],
  "perguntas_tipo": [
    "Como utilizar MundoJ Java efetivo?",
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

# MundoJ Java efetivo

> **Arquivo Original:** `MundoJ Java efetivo.pdf`
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
1 Cuidando do lixo: coleta seletiva usando Referências 1
1.1 Gerenciamentodememória . . . . . . . . . . . . . . . . . . . 2
1.2 Referências. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
1.3 SoftReferences . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
1.4 WeakReferences . . . . . . . . . . . . . . . . . . . . . . . . . . 11
1.5 ReferenceQueue . . . . . . . . . . . . . . . . . . . . . . . . . . 14
1.6 PhantomReferences . . . . . . . . . . . . . . . . . . . . . . . . 17
1.7 Exemplodeusonabibliotecapadrão-WeakHashMap . . . . 19
1.8 ConsideraçõesFinais . . . . . . . . . . . . . . . . . . . . . . . 22
1.9 Referências. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
2 Conhecendo os Parâmetros de Configuraç ão da JVM 25
2.1 OrganizaçãodamemórianaJVM . . . . . . . . . . . . . . . . 26
2.2 YounggenerationeTenuredgeneration . . . . . . . . . . . . 28
2.3 JVM32-bitesualimitaçãodeusodememória . . . . . . . . 32
2.4 Memórianon-heapeproblemasdeestourodememória . . . 33
2.5 AmemóriaeaschamadasdiretasoGarbageCollector . . . . 38
2.6 OutrosParâmetros . . . . . . . . . . . . . . . . . . . . . . . . . 39
2.7 ComoverificarousodamemórianaJVM . . . . . . . . . . . 40
2.8 UtilizandoasclassesJAVAdopacotejava.lang.management . 41
2.9 DesmistificandoopooldeStrings . . . . . . . . . . . . . . . . 44
2.10 ConsideraçõesFinais. . . . . . . . . . . . . . . . . . . . . . . 48
2.11 Referências. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
i

## Página 4

Sumário CasadoCódigo
3 Serializaç ão de objetos: da memória para o disco 51
3.1 SerializaçãoeDesserialização . . . . . . . . . . . . . . . . . . 52
3.2 java.io.Serializable . . . . . . . . . . . . . . . . . . . . . . . . . 52
3.3 Nemtudoéperfeito . . . . . . . . . . . . . . . . . . . . . . . . 57
3.4 Persistindoatributos:normais,transienteseestáticos . . . . 59
3.5 EscrevendoXML . . . . . . . . . . . . . . . . . . . . . . . . . . 64
3.6 ConsideraçõesFinais . . . . . . . . . . . . . . . . . . . . . . . 66
3.7 Referências. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
ii

## Página 5

Capítulo1
Cuidandodolixo:coletaseletiva
usandoReferências
“Uma das características mais atraentes da linguagem Java frente a suas
predecessoras, como C/C++, é a existência do Garbage Collector (GC), que é
responsável por realizar o gerenciamento automático de memória,
descartando objetos não mais utilizados por uma aplicação. Isso se traduz em
ganhos de produtividade por parte dos desenvolvedores, ao mesmo tempo em
que torna as aplicações menos propensas a erros e problemas de vazamento de
memória. No entanto, ainda assim é possível incorrer em problemas desse tipo
quando o ciclo de vida dos objetos de uma aplicação não é tratado
adequadamente. Neste artigo, discutimos como as classes de objetos de
referência podem ser utilizadas para eximir o desenvolvedor de problemas de
vazamento de memória, bem como possibilitar a colaboração inteligente do

## Página 6

1.1. Gerenciamentodememória CasadoCódigo
GC com as aplicações. ”
–porAlexMarquesCamposeAlexandreGazola
Amaioriadaslinguagensmodernasdeprogramaç ãoédotadademeca-
nismosdegerenciamentoautomáticodememóriapormeiodeumGarbage
Collector(GC),quetemcomofun çãodescartarespaçosdememóriaaloca-
dosenãomaisnecessáriosemumaaplicação.EmJava,oGCpossuihojeuma
implementaçãobastanteeficiente,sendo,emmuitoscasos,superioremde-
sempenhoaogerenciamentomanualfeitoporalgumaslinguagens(verlinks
nasreferênciasparaartigocombenchmarksJavavs. C++). Apresen çado
GCtornabemmaisprodutivootrabalhodosdesenvolvedores,reduzindo
bastanteapossibilidadedeproblemasrelacionadosaogerenciamentodeme-
mória.
Mesmocomessafacilidade,noentanto,énecessárioqueosdesenvolve-
dorescompreendamesaibamtrabalharadequadamentecomociclodevida
dosobjetosdeumaaplicação.Oconhecidoerro OutOfMemoryError,por
exemplo,podeserlan çadoporumaaplicaçãoqueestejamanipulandomuitos
objetosdemaneiraindevida.
Nessecontexto,umaferramentabastanteútil,presentenoJDKdesdesua
versão1.2,e,curiosamente,desconhecidadamaioriadosdesenvolvedores
Java,sãoasclassesdeobjetosdereferênciadopacote java.lang.ref.Es-
sasclassespodemserutilizadasparaseadministrardeformamaiscontrolada
ociclodevidadosobjetosemumaaplicaç ão.
Nesteartigo,apresentamosasclassesdeobjetosdereferênciadeJava,
mostrandocomopodemserutilizadasparatratarproblemassutisdevaza-
mentodememóriaetambémmostramosalgunsusosinteressantesqueper-
mitemqueoGCcolaborecomaaplicaç ão.Paraisso,faremosumaintrodu-
çãobásicasobregerenciamentodememória(alocaçãodinâmica,referências,
garbagecollectionetc.)e,emseguida,explicaremos,comexemplospráticos,
cadaumadasclassespresentesnopacote java.lang.ref.
1.1 G erenciamento de memória
Demaneirabastantesimplificada,podemosdividiraáreadememóriade
umaaplicaçãoJavaemduasáreasprincipais: apilhaeoheap. Apilha
2

## Página 7

CasadoCódigo Capítulo1. Cuidandodolixo:coletaseletivausandoReferências
é utilizada, entre outras coisas, para armazenar as variáveis locais (e os
parâmetros)deummétodo. Jáoheapéumaáreadestinadaàalocaç ão
dinâmicadememória,eéondeosobjetossãoarmazenados.Comoexemplo,
considereotrechodecódigoexibidonalistagemaseguir.
Listagem 1.1-DiferençassobrevariáveisnapilhaenoheapemJava.:
void agendarReuniao(int a, int b, String obj) {
criarCalendario();
//...
}
void criarCalendario() {
int c = 5;
Calendar data = new GregorianCalendar(2009, 01, 01);
//...
}
Ométodo agendarReuniao(),quandoinvocado,recebecomoparâ-
metrodoisinteiroseuma String.Osinteirospassadoscomoparâmetros
têmseusvaloresarmazenadosnapilha,aopassoqueoobjeto Stringrefe-
renciadopeloparâmetro objestáarmazenadonoheap.Nessecaso,éarma-
zenadonapilhaapenasoendere çodaStringqueestánoheap.Assumindo
que agendarReuniao()sejachamadocomosparâmetros a = 2, b =
3e obj = “Sala 152”,numpontoqualquerdaexecuç ãodoprograma,
poderíamosteraconfiguraçãodememóriailustradanafigura 1.1.Comoestá
representadonafigura,apilhaédivididaem“frames”,ouregistrosdeati-
vação,osquaiscontêmasvariáveislocais(tambémchamadasdevariáveis
automáticas)decadamétododapilhadeexecução.
3

## Página 8

1.1. Gerenciamentodememória CasadoCódigo
Fig.1.1:Ilustraçãodealocaçãodememórianapilhaenoheap.
Quandoésolicitadaaalocaçãodeumnovoobjeto(oqueéfeitopormeio
dooperador new),comoocorrenainstanciaçãodo GregorianCalendar
no método criarCalendario() da listagem, a Java Virtual Machine
(JVM)procuraespaçosuficientenoheapparaarmazenaroobjeto. Caso
nãohajaespaçosuficientenoheap(oucasoaJVMjulguenecessário),ela
realizaumachamadaaoGarbageCollector(GC)paraqueestepossaeli-
minarcélulasdememóriaque,porventura,nãoestejammaissendorefe-
renciadas. Explicandodemaneiramaisdetalhada,consideremosométodo
criarCalendario():aotérminodaexecuçãodessemétodo,todasasva-
riáveislocaisalocadasnapilhaperdemseuescopo. Sendoassim,oobjeto
GregorianCalendar,outrorareferenciadopelavariável data,torna-se
elegívelparaserremovido(oucoletado)doheappeloGC,poiséumobjeto
quenãoestámaisacessívelpelaaplicação.
Um detalhe avançado que costuma ser cobrado na certificação de
programadorJava,equeaspessoasnãoentendemmuitobemomotivo,é
que,devidoaofatodeasvariáveislocaisseremalocadasnapilha,classes
internasdefinidasdentrodemétodosnãopodemacessarasvariáveislocais
dessesmétodos, amenosqueestassejamespecificadascomofinal, como
mostraapróximalistagem.Issofaztodoosentido,poisotempodevidada
instânciadaclasseinternapodeexcederaotempodeexecuç ãodométododa
classeexterna. Comoasvariáveisdesteúltimosãodesalocadasaotérmino
desuaexecução,oobjetodaclasseinternanãoconseguiriareferenciá-las
4

## Página 9

CasadoCódigo Capítulo1. Cuidandodolixo:coletaseletivausandoReferências
posteriormente. Umaexceçãoaissoocorrequandoasvariáveisdométodo
externosãofinais. Nessecaso,aJVMseencarregadecopiarovalordessas
variáveisparaaclasseinternae,então,oobjetopodereferenciá-laslivre-
mentenummomentoposterioraotérminodaexecuçãodométodoexterno.
Listagem 1.2 - Acessando variáveis locais externas dentro de uma classe
interna.:
public class Exemplo {
public ActionListener getTratadorDeEvento() {
int x = 5;
final String str1 = "abc";
// retorna um objeto de uma classe interna anônima
return new ActionListener() {
@Override
public void actionPerformed(ActionEvent e) {
int z = x + 1; // erro de compilacao
String str2 = str1; // OK, str1 é final.
}
};
}
}
AthreaddoGCexecutasemprequesetentacriarumobjetoenãoexiste
espaçosuficientenoheap(oGCtambémpodeexecutaremoutrosmomentos,
deacordocomapolíticadecoletadelixousada,comomencionadoanteri-
ormente). Quandoissoocorre,athreadcorrenteébloqueadaeérealizada
umacoletadelixo.SeoGCnãoconseguirliberarespaçosuficienteeoheap
nãopuderserexpandidopelaJVM,entãoacriaç ãodoobjetofalhacomo
lançamentodeum OutOfMemoryError,quenormalmenteculminacomo
términodathreadcorrente(seestanãocapturaroerrocomumblocotry-
catch).
OfuncionamentobásicodoGarbageCollectorébaseadonumavariante
doalgoritmoMark-and-Sweep(marcarevarrer),baseadoemreferênciasfor-
tes(strongreferences).Demaneirabemsimplificada,numaprimeiraetapa,
aetapademarcação,oGCcome çapelasreferênciasraízes(rootreferences),
5

## Página 10

1.2. Referências CasadoCódigo
percorrendotodoografodeobjetosemarcandotodososobjetosqueforem
alcançadosapartirdasraízes.Numaetapaposterior,aetapadevarredura,o
GCpercorretodososobjetosdoheap,eliminandoosobjetosquenãotenham
sidomarcados.Nesseprocesso,asreferênciasraízesutilizadaspeloGCnuma
aplicaçãoJavasimplessãobasicamenteasvariáveisarmazenadasnapilhaeas
variáveisestáticascarregadaspelaJVM.
Antesdeterminarestase ção,gostaríamosdemencionaraexistênciado
método finalize(),presentenaclasse java.lang.Objecte,portanto,
herdadoportodasasclasses.EssemétodoéchamadopeloGCantesdeum
objetosercoletado(aimplementaçãoherdadade Objectnãofaznada).A
idéiado finalize()édaraumobjetoaoportunidadederealizaralguma
limpezaderecurso(ex.: fechamentodeumarquivo)antesdeoobjetoser
eliminado.Normalmente,nãoérecomendadoconfiarnessemétodoparaum
corretoeeficienteusodaaplicação,pois,comoaexecuçãodo finalize()
estáatreladaaoGC,podeserqueelenuncasejaexecutado.Umefeitocolateral
importantequepodeserdesencadeadopelo finalize()éaressurreição
deumobjeto. Issopodeserfeitopassando-seoobjetoparaumareferência
forteaindaemusopelaaplicaç ão(referênciasfortessãodiscutidasnase ção
seguinte).
1.2 R eferências
UmareferênciaforteéotipohabitualdereferênciaqueusamosemJava(ex.:
Calendar data = new GregorianCalendar(),dataéumareferência
forte).Todareferênciafortemantémemmemóriaoobjetoreferenciadoen-
quantoareferênciaforteestivernapilha(obs.:todareferênciaraizétambém
umareferênciaforte).Ostópicosaseguirresumemosprincipaisconceitose
umpoucodaterminologiaqueéusadanasse çõesseguintes:
•Referência:Variávelquereferencia, ouaponta, paraumobjetono
heap.
•Objeto referenciado:Objetoapontadoporumareferência.
•Referência forte:ReferênciacomumdalinguagemJava.Todoobjeto
referenciadoporumareferênciafortenãoépassíveldesercoletado
6

## Página 11

CasadoCódigo Capítulo1. Cuidandodolixo:coletaseletivausandoReferências
peloGC.
•Classe de objeto de referência:Classesespeciaisquesimulamreferên-
ciasparaobjetos,masnãosãofortesosuficienteparaimpediracoleta
deseusreferenciadospeloGC.Compreendemostipos SoftRerence,
WeakReferencee PhantomReference.
Além das referências fortes, também podemos trabalhar com as
classes especiais de objetos de referência do pacotejava.lang.ref:
SoftReference, WeakReferencee PhantomReference(todasesten-
demaclasseabstrata Reference). Instânciasdessasclassessãotratadas
demaneiradiferenciadapeloGC.Diferentementedosobjetosreferenciados
porreferênciasfortes,objetosreferenciadosapenasporinstânciasdasclasses
ReferencesãoelegíveisparacoletapeloGarbageCollector,deacordocom
apolíticavinculadaaotipodereferência.Associadosaostiposdereferências,
podemosdefinirquatroníveisdealcancedosobjetosreferenciados:
•Fortemente alcanç ável: um objeto é dito fortemente alcançável
quandoforreferenciadopor,pelomenos,umareferênciaforte;
•Suavemente alcanç ável:um objeto é dito suavemente alcançável
quandonãoforfortementealcan çáveleforreferenciadopor,pelome-
nos,umareferênciasuave(SoftReference);
•Fracamente alcanç ável:um objeto é dito fracamente alcançável
quandonãoforsuavementealcan çáveleforreferenciadopor,pelome-
nos,umareferênciafraca(WeakReference);
•“Fantasmagoricamente” alcançável:umobjetoédito“fantasmago-
ricamente”alcançávelquandonãoforfracamentealcan çáveleforre-
ferenciadopor,pelomenos,umareferênciafantasma(PhantomRefe-
rence).
A segue uma lista de cada uma das classes encontradas no pacote
java.lang.ref,asquaissãoapresentadasemmaisdetalhesnaspróximas
seções.
7

## Página 12

1.3. SoftReferences CasadoCódigo
•Reference:Classeabstrataparaasclassesdeobjetosdereferência.
•SoftReference: Referência suave. Seus objetos podem ser co-
letados pelo GC quando houver falta de memória, desde que se-
jamsuavementealcan çáveis. Exemplo: Reference soft = new
SoftReference(obj);
•WeakReference: Referênciafraca. Seusobjetospodemserlivre-
mentecoletadospeloGC,desdequesejamfracamentealcan çáveis.
Exemplo: Reference weak = new WeakReference(obj);
•PhantomReference: Referência fantasma. Seus objetos podem
ser livremente coletados pelo GC, desde que sejam “fantasmagori-
camente” alcançáveis. Exemplo: Reference phantom = new
PhantomReference(obj, aReferenceQueue);
•ReferenceQueue:Filadereferências.Exemplo: ReferenceQueue
queue = new ReferenceQueue();
1.3 S oftR eferences
Umareferênciasuavepermitequeumobjetosuavementealcan çávelperma-
neçanoheapatéqueamemóriaporeleocupadasejarequisitadapelosis-
tema. Paracriarmosumareferênciasuaveparaumobjeto objqualquer,
fazemos Reference softReference = new SoftReference(obj).
Emoutrapartedocódigo,paraobtermosoobjetoreferenciado,chamamos
softReference.get(). SeelejátiversidocoletadopeloGC,ométodo
get()retornaránull.
Asreferênciassuavesparaobjetossuavementealcançáveisterãoseusobje-
tosreferenciadosliberadosantesqueum OutOfMemoryErrorsejalançado
pelaJVM.Poressemotivo,asreferênciassuavespodemservistascomouma
espéciedecachesimplesdememória.Simples,pelofatodeodesenvolvedor
nãotercontrolesobreapolíticadedescartedosobjetosreferenciados(sãoas
regrasusadaspelaJVMqueespecificamquandoequaisobjetosserãocoleta-
dos).Essefatonãodesmereceopapeldasreferênciassuaves,poiselaspodem
nosauxiliararesolverproblemascomuns,comoveremosaseguir.
8

## Página 13

CasadoCódigo Capítulo1. Cuidandodolixo:coletaseletivausandoReferências
Imaginequeescrevemosumprogramaparadiagramaç ãovisualdeele-
mentos,comoumprogramadeeditoraçãodedocumentos,eémuitocustoso
carregarasimagensqueousuárionecessitaparaseudocumento(asimagens
podemestaremdisco,naWeb,naredelocaletc.). Alémdisso,precisamos
dememóriadisponívelparaatenderaoutrosrequisitosdaaplicaç ão,como,
porexemplo,objetosqueguardamoposicionamentodoselementos,regras
decomposição,agrupamentosdeelementosetc.Gostaríamosdereterasima-
gensemmemóriaatéqueestasejanecessáriaparaoutrosobjetosdenegócio
demaiorimportância;todavia,controlaramemóriamanualmenteestáfora
decogitação.Oquefazer?
Esseéumcenárioquepodesebeneficiardousodereferênciassuaves,
comodemonstradonocódigodeexemplodaListagem3.Aclassefuncionada
seguintemaneira:quandoumusuárionecessitadeumaimagem,elechamao
métodocarregarImagem(),passandoaURIparaoarquivoquecontéma
imagem(lembre-se,aimagempodeestaremdisco,naWebetc.).Ométodo
verificaseexisteumareferênciaparaadadaimagememumcachederefe-
rências. Seexistirumareferêncianocache,significaqueadadaimagemjá
foirequisitadapelousuárioemalgumtempoanterior,masnãogaranteque
osdadosdaimagemestejamemmemória.Éaquiqueestáadiferen ça:como
usamosotipo SoftReference,nãosabemosse,emalgumpontoanterior
aessachamada,osistemanecessitoudememóriaparaoutroobjetoe,com
isso,liberoualgumdosobjetosquehavíamoscarregado.Porisso,precisamos
verificarseoobjetoreferenciadoaindaestáemmemória. Fazemosissoao
mesmotempoemquecriamosumareferênciaforteparaoobjetoreferenci-
ado( imagem = imagemRef.get()),casoesteexista.
Éimportanteressaltarque, semprequenecessitamosutilizaroobjeto
referenciado,precisamoscriarumareferênciafortetemporáriaparaele,de
modoagarantirqueoobjetonãoserácoletadopeloGCenquantoestiver
sendoutilizado.Issotambémseaplicaaotipo WeakReference.Paraexem-
plificar:
// código ruim! Não emule isto!
if (ref.get() != null) {
// objeto referenciado pode ser nulo aqui!
ref.get().aMethod(); // pode lançar uma NullPointerException
9

## Página 14

1.3. SoftReferences CasadoCódigo
} else {
return;
}
Voltandoaoexemplo,seaimagemcontinuaemmemória,nossotrabalho
estácompletoepodemosretorná-la. Seareferênciafornula(ousenão
existirareferência,poiséaprimeiravezemquesomossolicitadosporuma
dada URI), chamamos o métodocarregarImagem() para carregar a
imagemdeseuarmazenamento,criamosumanova SoftReferencepara
elanocachedereferênciaseretornamosaimagemparaochamador.Todoo
processoétransparente,eamemória,dopontodevistadaaplicaç ão,sempre
estádisponívelparaosobjetosmaisimportantes,demodoquecumprimos
nossoobjetivo.
Listagem 1.3 - Carregador de imagens implementado com referências
suaves.:
public class CarregadorDeImagem {
private final Map<URI,Reference<Image>> cacheDeImagem;
public CarregadorDeImagem () {
cacheDeImagem = new HashMap<URI,Reference<Image>>();
}
public Image fetchImage(URI imagePath) {
Image imagem = null;
Reference<Image> imagemRef =
getImagemRefDoCache(imagePath);
if (imagemRef != null) {
imagem = imagemRef.get();
}
if (imagem == null) {
imagem = carregarImagem(imagePath);
adicionarImagemAoCache (imagePath, imagem);
}
10

## Página 15

CasadoCódigo Capítulo1. Cuidandodolixo:coletaseletivausandoReferências
return imagem;
}
private Reference<Image> getImagemRefDoCache(URI imagemPath){
return cacheDeImagem.get(imagemPath);
}
private void adicionarImagemAoCache(URI imagemPath,
Image imagem) {
cacheDeImagem.put(imagemPath,
new SoftReference<Image>(imagem));
}
private Image carregarImagem(URI imagemPath) {
// Recupera a imagem de seu armazenamento...
return imagem;
}
}
1.4 W eakReferences
Uma referência fraca é uma referência a um objeto que pode ser li-
vremente coletado pelo GC, caso seja fracamente alcançável. Para cri-
armos uma referência fraca para um objetoobj qualquer, fazemos
Reference weakReference = new WeakReference(obj). Emou-
tra parte do código, para obtermos o objeto referenciado, chamamos
weakReference.get(). SeelejátiversidocoletadopeloGC,ométodo
get()retornaránull.
Paraentendermosautilidadedasreferênciasfracas,consideremosopa-
drãodeprojetoObserver.Oobjetivodestepadrãoéestabelecerumadepen-
dênciade“um-para-muitos”entreobjetos,demaneiraque,quandoumob-
jetomudadeestado,todososseusdependentessãonotificadosepodemser
atualizados.Osparticipantesprincipaisdopadrãosãoosseguintes:
• Subject(sujeito): objetoquemantémumalistadeobjetosobservers.
OSubjectforneceumainterfaceparaacrescentareremoverobjetose
enviaumanotificaçãoparaseusobserversquandoseuestadomuda;
11

## Página 16

1.4. WeakReferences CasadoCódigo
• Observer(observador):objetoqueéacrescentadoaumSubjecteque
ofereceumainterfacedeatualização. DizemosqueumObserverob-
servaumSubject.
Alistagemaseguirexibeumaimplementaç ãotradicionalde Subject
(o Observerestáabstraídoemumainterfacecomummétodoupdate()),
enquantoaListagemseguinteexibeumaimplementaç ãode Subjectque
usareferênciasfracas. Aimplementaçãotradicionaldopadrãoestabelece
a necessidade de queSubject possua um método para remoção de
observadores,deformaque,quandoumobjeto Observernãoprecisemais
recebernotificaçõesdedeterminadoobjeto Subject,podemossolicitarao
Subjectaremo çãodoreferidoobjeto. Noentanto,essaimplementaç ão
acabaadicionandoumapreocupaçãoaodesenvolvedor,oqualprecisaestar
atento em chamar o método para remoção do Observer quando este
perderseuescopodeutilizaçãonaaplicação.Casocontrário,porcontinuar
nalistado Subject,essesobservadorespermanecerãodesnecessariamente
noheap,gerandovazamentosdememória.
Listagem 1.4-Subjectcomimplementaçãotradicional.:
public class Subject {
private Set<Observer> observadores;
public Subject() {
observadores = new HashSet<Observer>();
}
public void adicionarObservador(Observer observador) {
observadores.add(observador);
}
public void removerObservador(Observer observador) {
observadores.remover(observador);
}
public void notificarObservadores() {
for (Observer observador : observadores) {
12

## Página 17

CasadoCódigo Capítulo1. Cuidandodolixo:coletaseletivausandoReferências
observador.atualizar();
}
}
}
Listagem 1.5-Subjectcomimplementaçãousandoreferênciasfracas.:
public class Subject {
private Set<Reference<Observer>> observadores;
public Subject() {
observadores = new HashSet<Reference<Observer>>();
}
public void adicionarObservador(Observer observador) {
observadores.add(
new WeakReference<Observer>(observador));
}
public void notificarObservadores() {
removerReferenciasMortas();
for (Reference<Observer> ref : observadores) {
//referência forte necessária
Observer observador = ref.get();
if (observador != null) {
observador.update();
}
}
}
private void removerReferenciasMortas() {
Set<Reference<Observer>> copiaObservadores =
new HashSet<Reference<Observer>>();
copiaObservadores.addAll(observers);
for (Reference<Observer> ref : copiaObservadores) {
Observer observador = ref.get();
if (observador == null) {
observadores.remove(ref);
}
13

## Página 18

1.5. ReferenceQueue CasadoCódigo
}
}
}
Aversãocomreferênciasfracas,ilustradanasegundaimplementaç ão,
dispensacompletamenteanecessidadedequeo Subjecttenhaummé-
todo removerObservador().Nessaimplementação,mantemosumcon-
juntodereferênciasfracasparaosobservadores. Dessaforma,quandoum
Observernãoémaisnecessárioemumaaplicação,osimplesfatodeperder
suasreferênciasfortesjáotornaelegívelparacoletapeloGC.Napróximase-
ção,veremoscomoométodo removerReferenciasMortas()podeser
melhoradopormeiodousodaclasse ReferenceQueue.
1.5 R eferenceQueue
Antesdeentenderofuncionamentodotipo PhantomReference,éneces-
sárioentenderofuncionamentoda ReferenceQueue. Seoleitorconsul-
taradocumentação,notaráqueosconstrutoresdasreferênciasquevimos
atéagora, SoftReferencee WeakReference,vêmemdois“sabores":
umquesórecebeoobjetoreferenciadoeoutroquerecebetambémuma
ReferenceQueue.
A ReferenceQueue(oufiladereferências)éumaestruturadedados
utilizadaparasuporteaousodereferências.Seufiméfacilitaradescoberta
dasreferênciascujosobjetosreferenciadosjátenhamsidomarcadosparaco-
letapeloGCe,portanto,jánãosejammaispassíveisdeseremutilizados(a
menosqueosobjetossejamressuscitadospelométodo finalize(),oque
podeocorrerapenascomreferênciassuavesefracas).
Umaalternativaaousodeuma ReferenceQueueépercorreraestru-
turadedadosemqueestãoarmazenadasasreferênciase,emseutempo,re-
moveraquelascujosobjetosreferenciadossejamnulos( reference.get()
== null).Buscarreferênciasinválidasémenoseficientedoquesaberdean-
temãoquaisreferênciasforaminvalidadas.Éexatamenteesseopropósitoda
ReferenceQueue.
Como exemplo de uso, vejamos como poderíamos adaptar o có-
digo do Subject discutido na seção anterior de modo a utilizar uma
14

## Página 19

CasadoCódigo Capítulo1. Cuidandodolixo:coletaseletivausandoReferências
ReferenceQueue,comomostraalistagemaseguir.
Listagem 1.6-SubjectcomimplementaçãousandoReferenceQueue.:
public class Subject {
private ReferenceQueue<Observer> referenciasMortas;
private Set<Reference<Observer>> observadores;
public Subject() {
observadores = new HashSet<Reference<Observer>>();
referenciasMortas = new ReferenceQueue<Observer>();
}
public void registrarObservadores(Observer observador) {
observadores.add(
new WeakReference<Observer>(
observador, referenciasMortas));
}
public void notificarObservadores() {
removerReferenciasMortas();
for (Reference<Observer> ref : observadores) {
Observer observador = ref.get();
if (observador != null) {
observador.atualizar();
}
}
}
private void removerReferenciasMortas() {
Reference<?> ref = referenciasMortas.poll();
while ( ref != null ) {
observadores.remove(ref);
ref = referenciasMortas.poll();
}
}
}
Nesteexemploatualizado,adicionamosuma ReferenceQueue,cha-
15

## Página 20

1.5. ReferenceQueue CasadoCódigo
mada referenciasMortas, na qual registramos cada uma das referências
para observadores, new WeakReference<Observer>(observador,
referenciasMortas). Quandoessesobservadoresperdemseuescopoe
setornamelegíveisparaseremcoletados,automaticamentesuasreferências
sãopostasna ReferenceQueueassociada.Valeressaltarqueasreferências,
enãoosobjetos(osobjetosjáforamcoletadospeloGC),équesãopostos
na ReferenceQueue.Ométodo removerReferenciasMortas()tem
aresponsabilidadederemovertodasasreferênciasinválidasdanossalistade
observadores. Essemétodoéchamadosemprequeprecisamosnotificaros
observadoresdeum Subject.
Nestepontotemosumadecisãodeprojetomuitocomum. Porsim-
plicidade,optamosporrealizaralimpezadasreferênciasinválidassempre
queocódigoprecisanotificarseusobservadores,utilizandoomododelei-
tura“não-bloqueante”daReferenceQueue ométodo poll(). Pode-
ríamos,entretanto,terescolhidoimplementarumathreadquemonitorasse
a ReferenceQueue,demodoarealizaressetrabalho. Ambassãoop ções
válidas,suportadaspela ReferenceQueueequaldelasescolherdepende
muitodocontextodeutilização(emboraimplementaçõesdeumaúnicath-
read,comoadoexemplo,sejammaiscomuns).Alistaaseguirtrazumre-
sumodaAPIda ReferenceQueue,quedásuporteaessesmodosdeuso.
Todososmétodosretirameretornamumobjetodotipo Reference<?
extends T> dafilaouretornam nullquandonãoexistemmaiselementos
nafila.
•pool():Verificaeretornaumareferênciadafila(seexistiralguma)ou
nullseafilaestivervazia.Estemétodonãobloqueiaathreadcorrente,
retornandoimediatamente.
•remove():Verificaeretornaumareferênciadafila(seexistiralguma)
oufazathreadcorrentebloquear,esperandoquealgumobjetosejanela
posto.
•remove(long timeout): Verificaeretornaumareferênciadafila
(seexistiralguma)oufazathreadcorrentebloquearportimeout(em
milissegundos)ouatéqueumobjetosejanelaposto oqueacontecer
16

## Página 21

CasadoCódigo Capítulo1. Cuidandodolixo:coletaseletivausandoReferências
primeiro(umvalordetimeoutigualazerofazathreadbloquearinde-
finidamente,comoachamadaderemovesemargumentosfaz).
1.6 P hantomR eferences
A referência fantasma é o tipo mais fraco de referência disponibilizado
pelalinguagemJava. Paracriarmosumareferênciafantasmaparaumob-
jeto obj qualquer, fazemos Reference phantomReference = new
PhantomReference(obj, referenceQueue). A referência fantasma
possuiumapeculiaridade:nãopodemosnemmesmoconsultarqualéoob-
jetoreferenciado,ouseja,chamadasaométodo get()emreferênciasdesse
tiposempreretornam null.Alémdisso,umareferênciafantasmaestásem-
preassociadaauma ReferenceQueue.Sendoassim,paraquêexatamente
servemasreferênciasfantasmas,ecomoutilizá-las?
Diferentementedasreferênciassuavesefracas,que,quandoassociadas
auma ReferenceQueuesãocolocadasnessafilatãologosejammarca-
dasparacoletapeloGC(oquepodeocorrerantesdaexecuç ãodométodo
finalize()dosobjetosreferenciados),asreferênciasfantasmassósãoco-
locadasnafiladereferênciasapósaexecuç ãodométodo finalize()dos
objetosreferenciadosedesdequeo finalize()nãoressusciteosobjetos.
Logo,podemosgarantirqueosobjetosoutrorareferenciadosporreferências
fantasmasqueestejamnuma ReferenceQueueforam,defato,eliminados.
Emoutraspalavras,referênciasfantasmassãoaúnicamaneiraseguradega-
rantirqueumobjetonãomaisexiste.Comisso,constituem-secomoumaal-
ternativa(superior)aométodo finalize()paralimpezaderecursosnão
maisnecessários(ex.: fechamentodeumarquivo). Referênciasfantasmas
tambémpoderiamserúteisparatestes“caseiros”nabuscadevazamentos
dememórianaaplicação,emcasosemqueseexigemaisagilidadedoque
aprovidapelosprofilers.
Alistagemaseguirtrazumexemploilustrandoousodereferências
fantasmas. Implementamos um gerenciador para fluxos de entrada a
partirdearquivos. Suafinalidadeégarantirqueométodo close()do
FileInputStreamseráchamadoquandonãohouvermaisreferênciaspara
aURIquedefineocaminhoparaoarquivo.Issopermitequeodesenvolvedor
17

## Página 22

1.6. PhantomReferences CasadoCódigo
nãosepreocupeemfecharofluxoexplicitamente,bastandoapenasmanter
vivooobjetoURIpelotempoemquenecessitardofluxorelacionadoaele.
Estaidéiapodeserextrapoladaparaumgerenciadorderecursosqueforne ça
handlesparaosrecursosqueele(gerenciador)manipule, simplificandoa
utilizaçãodestesegarantindosuacorretafinalizaç ão.
Listagem 1.7 - Gerenciador de fluxos de entrada com implementação
usandoreferênciasfantasmas.:
public class GerenciadorDeFluxosDeEntrada {
private final Map<Reference<URI>, FileInputStream>
fluxosDeEntrada;
private final ReferenceQueue<URI> referenciasMortas;
public GerenciadorDeFluxosDeEntrada() {
fluxosDeEntrada =
new HashMap<Reference<URI>, FileInputStream>();
referenciasMortas = new ReferenceQueue<URI>();
}
public FileInputStream obterFluxoDeEntrada(URI caminho)
throws FileNotFoundException {
removerReferenciasMortas();
File arquivo = new File(caminho);
FileInputStream fluxo = new FileInputStream(arquivo);
Reference<URI> referencia =
new PhantomReference<URI>(caminho,referenciasMortas);
fluxosDeEntrada.put(referencia,fluxo);
return fluxo;
}
private void removerReferenciasMortas() {
Reference<?> ref = referenciasMortas.poll();
while ( ref != null ) {
FileInputStream fluxo = fluxosDeEntrada.get(ref);
fluxosDeEntrada.remove(ref);
18

## Página 23

CasadoCódigo Capítulo1. Cuidandodolixo:coletaseletivausandoReferências
try {
fluxo.close();
} catch (IOException e) {}
ref.clear();
ref = referenciasMortas.poll();
}
}
}
1.7 E xemplo de uso na biblioteca padrão - We-
akHashM ap
NabibliotecapadrãodeJava,temosumexemplodeusodereferênciaspara
produzirumaestruturadedadosquejuntaodesempenhoeafacilidadedo
HashMapcomahabilidadedas WeakReferencesdenãofor çarumobjetoa
permaneceremmemória.Éa WeakHashMap.Essaestruturadedadosutiliza
WeakReferencesparaaschaves(enãoosvalores)quearmazenanomapa.
Osvaloresassociadosacadachavesãoreferênciascomuns(fortes).
Essecomportamentoéútilquandotemos,porexemplo,umasituaçãoem
quequeremosguardarmetadadossobreobjetos,masnãoqueremosqueo
fatodeguardaressesmetadadosinterfiranociclodevidanormaldestes.Ou-
troexemploéquandoqueremosassociarmetadadosaobjetos,masasclasses
dessesobjetosnãopodemsermodificadasnemestendidas.
Considereumsistemafictício, aserutilizadoemlocadoras, paraum
quiosquedeexibiçãodevídeos. Osistemadeveráexibiraosseususuários,
entreoutrasinformações,vídeosdepropagandaeostrailersdosfilmesque
alocadorapossui. Duranteoprojeto,foramidentificadasduasinterfaces
paraosistema,exibidasnasduaspróximaslistagens.Umaseráutilizadapara
abstrairovídeoeaoutraparaabstrairseusmetadados.
Listagem 1.8-Interfacedeabstraçãoparaumvídeo.:
public interface Video {
public void tocar();
public void pausar();
public void parar();
19

## Página 24

1.7. Exemplodeusonabibliotecapadrão-WeakHashMap CasadoCódigo
public void avancar(double multiplicador);
public void retroceder(double multiplicador);
public void buscar(long tempo);
}
Listagem 1.9-Interfacedeabstraçãoparaosmetadadosdeumvídeo.:
public interface MetadadosDeVideo {
public String getTitulo();
public String getAutor();
public List<String> getPalavrasChave();
public long getDuracao();
public List<String> getElenco();
public Date getDataDeLancamento();
}
Aresponsabilidadedeobterosdadosdovídeoserádeumsubsistema
especializado, já que também se pensa em permitir que um servidor de
streamingdevídeosejausadoemalgumpontodoprojeto. Porsuavez,
os metadados desses vídeos serão carregados de servidores de banco
de dados, arquivos (locais ou na rede), ou ainda por um serviço Web,
dependendo da configuração. De modo a uniformizar a experiência do
usuárioefacilitarocontroledosmetadados,foipropostoocachedemeta-
dadosdosarquivossendoexibidos,comoexemplificadonalistagemaseguir.
Listagem 1.10-Cachedemetadadosdosarquivosemexibiç ão.:
public class MetadadosDeVideosEmExibicao {
private final Map<Video, MetadadosDeVideo> informacoesVideos;
public MetadadosDeVideosEmExibicao() {
informacoesVideos =
new WeakHashMap<Video, MetadadosDeVideo>();
}
public void registrarVideo(Video video,
MetadadosDeVideo metadados) {
informacoesVideos.put(video,metadados);
}
20

## Página 25

CasadoCódigo Capítulo1. Cuidandodolixo:coletaseletivausandoReferências
public MetadadosDeVideo obterMetaDados(Video video) {
return informacoesVideos.get(video);
}
public int obterNumeroDeVideosRegistrados() {
return informacoesVideos.size();
}
}
A classe MetadadosDeVideosEmExibicao utiliza um
WeakHashMap como seu componente central. Quando um vídeo
é posto em exibição, seus metadados são carregados e registrados
junto à classe MetadadosDeVideosEmExibicao, com o método
registrarVideo(). Essemétodo,porsuavez,insereumanovaentrada
no WeakHashMap interno, usando a referência forte do objeto Video
passadacomoparâmetro. Achavedessanovaentrada,contudo,nãoserá
areferênciafortedoobjetoVideo,massimumareferênciafraca,criadae
mantidainternamentepelaclasse WeakHashMap.
Comooleitordeveternotado,nãoexisteummétodopara“desregistrar”
ummetadadodeumvídeo.Bastaoobjeto Videoemquestãosetornarfra-
camentealcançável(eoobjetosercoletado)paraqueseusmetadadossejam
automaticamenteeliminadosdenossoregistrodemetadados.
Oprocessoocorredaseguinteforma: quandooobjeto Videoécole-
tado,areferênciafracaqueservedechaveparaometadadodessevídeoé
postaemuma ReferenceQueueinternaao WeakHashMap. Sempreque
um WeakHashMapémanipulado,ummétodointernoéchamadoparaeli-
minarasreferênciasinválidas(asqueestãona ReferenceQueueinterna).
Comisso,dapróximavezemqueousuáriotentarmanipularomapa,essa
chaveseráeliminadae,juntocomela,areferênciafortequeomapamantém
paraometadadodessevídeo. Amenosqueousuáriotenhacriadoexplici-
tamenteumaoutrareferênciaparaoobjetodemetadadosdevídeo,ovalor
associadoàchaveeliminadatambémsetornapassíveldesercoletado.
Pormeiodousodeum WeakHashMap,nãosósimplificamosainterface
eautilizaçãodocachedemetadados,comotambémevitamosvazamentos
dememórianocasodeodesenvolvedornãoselembrarde“desregistrar”o
21

## Página 26

1.8. ConsideraçõesFinais CasadoCódigo
metadadoquandoovídeorelacionadonãoformaisnecessário.
1.8 C onsiderações Finais
ApresençadoGarbageCollectornaplataformaJavaimpulsionaaproduti-
vidadenodesenvolvimentodeaplicações,eximindoosdesenvolvedoresdo
compromissodefazerdesalocaçãoexplícitadeobjetosnãomaisnecessários
emsuasaplicações. Noentanto,osdesenvolvedoresaindaprecisamestar
atentosaociclodevidadosobjetosdesuasaplicações,pois,apesardetodoo
suporteoferecidopelalinguagem,problemascomovazamentosdememória
aindapodemocorrer.
Nesteartigo,apresentamosasclassesdeobjetosdereferênciaoferecidas
pelalinguagemJava,destacandocomopodemserusadasparacontornarpro-
blemassutisdegerenciamentodememória,efazendocomqueopróprio
GarbageCollectorpossaserumcolaboradornessatarefa. Porincrívelque
pareça,mesmopresentedesdeosprimórdiosdalinguagemJava,amaioria
dosdesenvolvedoresdesconheceessaAPI,que,comovimos,podeseruma
ferramentabastanteútil.
Nãoobstante,éimportantefrisarqueasclassesdeobjetosdereferência
devemserusadasparcimoniosamentenumaaplicação,poispodemacarretar
impactosemtermosdeeficiência.Alémdooverheadocasionadopelonível
deindire çãonoacessoaosobjetos,existeotrabalhoextraqueoGCdeve
realizarduranteascoletasdelixo. Mesmoousodasclassesmaisúteis(ex.:
WeakHashMap)paracachessimplespodeestressarbastanteoGC,quando
umaimplementaçãodecacheLRUdetamanhofixopoderiasermuitomais
apropriadaeperformática(comofazoHibernate,porexemplo).
Emtemposdeglobalizaçãoedesenvolvimentosustentável,devemosfazer
anossaparte.Amemóriaéumrecursomuitoimportanteedevemosutilizá-la
comconsciência,portanto,tratebemdeseusobjetosesepareseulixo!
1.9 R eferências
• http://weblogs.java.net/blog/enicholas/archive/2006/05/
understanding_w.html
22

## Página 27

CasadoCódigo Capítulo1. Cuidandodolixo:coletaseletivausandoReferências
• http://www.kdgregory.com/index.php?page=java.refobj
• Designpatterns; ErichGamma,RichardHelm,RalphJohnson,and
JohnVlissides
• ALinguagemdeProgramaçãoJava,4Ed.;Gosling,James;Arnold,Ken;
Holmes,David.
• http://java.sun.com/j2se/1.5.0/docs/api/java/lang/ref/
package-summary.html
• http://www.ibm.com/developerworks/java/library/j-jtp11225/index.
html
• http://www.ibm.com/developerworks/java/library/j-jtp01246.html
• http://chaoticjava.com/posts/how-does-garbage-collection-work/
• http://www.javaranch.com/campfire/StoryInner.jsp
• http://www.janeg.ca/scjp/gc/finalize.html
• Performance Java vs. C++:http://www.idiom.com/\char126zilla/
Computer/javaCbenchmark.html, http://www-128.ibm.com/
developerworks/java/library/j-jtp09275.html
23

## Página 29

Capítulo2
ConhecendoosParâmetrosde
ConfiguraçãodaJVM
“Muitas vezes, ao criarmos uma aplicação JA V A nos deparamos com erros
relacionados a estouro de memória, mesmo ainda havendo memória livre. O
que realmente aconteceu? Para entendermos perfeitamente as questões
envolvidas com esse problema, que eventualmente nos tira o sono, devemos
primeiramente observar como a memória é organizada na máquina virtual
JA V A. Neste artigo, veremos como a memória é organizada, os parâmetros
utilizados para inferir nos tamanhos de alocação de cada região e as causas
mais comuns de estouro de memória. Ao final, serão mostradas algumas
formas de monitorarmos a memória e como alterar os parâmetros para
algumas IDEs e servidores de aplicação. ”
–porRodrigodeAzevedo

## Página 30

2.1. OrganizaçãodamemórianaJVM CasadoCódigo
AlinguagemJAVAédotadademecanismossingularesexistentesemsua
gerênciadememória.Nesteartigo,buscaremosentendertaismecanismose
comoaMáquinaVirtualJava(JVM)tratacadaregiãoquecompõesuame-
mória.
Analisaremoscadaumadestasregiões,seupapelecomoinferiremsua
alocaçãoeoutrasfacilidadesproporcionadaspelosparâmetrosdeiniciaç ão
daJVM.Tambémserápossívelentendercomoeporqueocorremosredi-
mensionamentosdememória.
Evidenciaremosarazãodamaioriadoserrosrelacionadoscomestourode
memória( java.lang.OutOfMemoryError)ealgumasformasdeevitá-lo.
Veremos algumas formas de monitorar a utilização da memória na
JVMutilizandoasclassesdisponíveisnopacote java.util.management,
acompanhandoeverificandoaeficiênciadosciclosdoGarbageCollector
(GC)entreoutrasformasdisponíveis.
Aofinaldoartigo,teremosvistoinformaçãosuficienteparaentendimento
domacroprocessoqueaJVMutilizaparagerenciaramemóriaaumentandoa
capacidadedoleitoremevitaroserrosmaiscomunsqueocasionamoestouro
dememóriaemdiferentesregiõesdamemória.
2.1 O rganização da memória na JVM
Antesdeverificarmosaspossíveiscausasdeumestourodememória,vamos
primeiroprocurarentendercomoamemórianamáquinavirtualéorgani-
zadaeaprenderumpoucosobreosconceitosenomenclaturasenvolvidas.
AmemóriadaJVMédivididaemtrêspartesprincipais:
• Younggen(eden,survivor);
• Oldgen(tenured);
• Permgen(permanent).
Alémdisso,háaindaaumaáreadenominada“codecache”.Aregiãode-
nominadasurvivorédivididaemduassubregiões:
• From-space;
26

## Página 31

CasadoCódigo Capítulo2. ConhecendoosParâmetrosdeConfiguraçãodaJVM
• To-space.
Fig.2.1:OrganizaçãodamemórianaJVMsemmargempararedimensiona-
mentos.
Podemosaindadividiremdoisgrandesgrupos:
• Heap;
• Non-heap
Grupoheap:
• Younggeneration(eden,from-space,to-space);
• Oldgeneration(tenured).
Gruponon-heap
• Codecache;
• Permanentgeneration.
27

## Página 32

2.2. YounggenerationeTenuredgeneration CasadoCódigo
2.2 Y oung generation e Tenured generation
Agrandemaioriadasalocaçõesrealizadasemmemóriaérealizadanaregião
dayounggeneration.Estaregiãodamemóriaévoltadaeotimizadaparalidar
comobjetosquetêmumciclodevidacurto. Objetosquesobrevivemavá-
riosciclosdoGarbageCollectorsãomovidosparaaregiãoconhecidacomo
TenuredGeneration.
NormalmenteaYoungGenerationémenorqueaTenuredeosciclosde
GarbageCollector(GC)sãomaisfrequentes.NaTenuredGenerationosci-
closdeGCocorremcommuitomenosfrequência.
AregiãodenominadaYoungGenerationédivididaemtrêssubregiões:
• eden;
• to-space;
• from-space.
Asalocaçõesdeobjetoocorremprimeiramentenaedenecomotempoe
principalmentedepoisdealgunsciclosdeGCmovem-se(partedosobjetos,
poisorestanteforarecolhidopelocoletor)emdire çãoaregiãofrom-space.
Novamentequandoestassubregiõesficamcheiasoupróximasdesuaca-
pacidade,hánovociclodeGC.Nestemomento,aexpectativaéqueamaioria
dosobjetossejarecolhidapeloGarbageCollectoreaquelesquesobrevivem
sãoagoramovidosparaasubregiãoto-space. Apósalgunsnovosciclosdo
GC,finalmenteosobjetossobreviventessãomovidosparaaregiãodenomi-
nadaOldouTenuredGeneration.NaregiãoTenured,osciclosdoGarbage
Collectorsãomenosfrequentesemaislentos,poiséumaregiãoricaemob-
jetosativos.
Alémdasregiõescitadas,háaindaoutragranderegiãoconhecidacomo
PermanentGeneration. Nesta,osciclosdeGCocorremcommuitomenos
frequência.Nelaseencontram,entreoutrascoisas,osmetadadosdasclasses
utilizadas.
AregiãodenominadaCodeCacheéondeficamalocadasclassescom-
piladaspertencentesàJVMequedãosuporteasuagestãodealocaç ãode
memória,otimizaçõesarquiteturais(RISCxCISC)etc.
28

## Página 33

CasadoCódigo Capítulo2. ConhecendoosParâmetrosdeConfiguraçãodaJVM
Memória heap e problemas com estouro de memória
Amemóriaheapéaáreaondeosdadosnormalmentesãoalocados.Todas
asinstânciasdeclasseseosprimitivossãoalocadosnestaárea.Umaaplicaç ão
JAVAnormalmenteiniciacomoheaputilizandoovalordefinidopeloparâ-
metro-Xms.Quandoosobjetossãocriados,estessãoalocadosnestaregião.
Seamemóriaheapchegaraoseulimite,éautomaticamenteredimensionada
atéchegaraovalormáximofornecidopeloparâmetro-Xmx.
Fig.2.2:OrganizaçãodamemórianaJVMcommargemparaocorrerredi-
mensionamentosquandonecessário.
AoiniciaraMáquinaVirtualJAVAtodooespaçodefinidopelo -Xmxé
reservado.Seolimiteinferioresuperiorestiverdefinidocomvaloresdiferen-
tes,haverámargemparaaJVMrealizarredimensionamentos(expansãoou
encolhimento)quandonecessário. SeaoiniciarJVM,osvaloresfornecidos
demínimoemáximoforemiguaisparaalgumasdasregiões(heapouperm
gen,videfigura 2.1),nãoserápossívelocorrerredimensionamentonestaparte
damemória.
29

## Página 34

2.2. YounggenerationeTenuredgeneration CasadoCódigo
Oespaçototaldisponívelparaoredimensionamentoéadiferen çaentre
olimitesuperioreinferior.Esteespaçonãoédisponibilizado,apesardealo-
cado,imediatamenteparaaJVM.Nafigura 2.2,esteespaçoalocadopodeser
identificadocomo“virtual”eestadiferençaentreovalormínimoemáximo
éobserváveltantonaheapquantonapermgen.
Outrasterminologiassãoutilizadas,comoespaçoinicial(normalmente
definidopeloparâmetro -Xms),espaçousado(oespaçorealmenteutilizado
naqueleinstante),espaçocomitado(otamanhodaregiãonaqueleinstante
disponívelparaJVM)eespaçomáximo(normalmentedefinidopeloparâ-
metro -Xmx).
Entendendo quando acontecem os redimensionamentos da heap
ExistemalgumasverificaçõesquesãorealizadaspelaJVMnamemória
heapqueidentificamsehánecessidadederedimensionamento.Oscritérios
utilizadospararealizarqualqueraçãoderedimensionamentosãofornecidos
pelosparâmetros -XX:MinHeapFreeRatioe -XX:MaxHeapFreeRatio.
Estesparâmetrosaceitamvalorespercentuais,istoé,valoresquevariam
entre0a100.Casoestesparâmetrosnãosejaminformados(oquenormal-
menteacontece),existemvalorespadrõesdefinidospelaJVM.Estesvalores
percentuaispadrõesdependemdaarquitetura(32-bitou64-bit)edoS.O.uti-
lizado.
Adinâmicadefuncionamentobasicamentesegueoseguinteprincípio:
seforverificadoqueoespaçolivredamemóriaésuperioraopercentualde-
finidonoparâmetro -XX:MaxHeapFreeRatio(istoé,muitamemóriali-
vre),amesmaéredimensionada(encolhimento)buscandoficarabaixodo
valordefinidoporesteparâmetro,respeitandosempreolimiteinferiordefi-
nidopelo -Xms.Poroutrolado,seapósapassagemdeumciclodeGC,aheap
estivercomamemórialivreabaixodopercentualmínimodefinidopeloparâ-
metro -XX:MinHeapFreeRatio(istoé,escassezdememória),aheapserá
redimensionada(expansão)buscandoficaracimadovalordefinido,limitado
pelafronteirasuperiordadapeloparâmetro -Xmx.
Quando a memória heap chega ao seu valor máximo e não há mais
nenhumaformaderecuperação, mesmoapóstersidoexecutadoospro-
cessos do Garbage Collector, será lançado pela JVM o erro que in-
30

## Página 35

CasadoCódigo Capítulo2. ConhecendoosParâmetrosdeConfiguraçãodaJVM
dica o estouro de memória (out of memory) representado pela classe
java.lang.OutOfMemoryError. Normalmenteamensagemqueacom-
panhaesteerroé “java.lang.OutOfMemoryError: Java heap space”.
Motivos para o estouro de memória
Arazãomaissimplesparaesteincidenteestárelacionadaaumaaplica-
çãograndedemaisparaotamanhodaheapfornecida.Nestecaso,asoluç ão
ésimples,bastaaumentaroslimitesinferioresesuperioresdamemória.Ou-
tromotivopoderiaestarrelacionadocom“memoryleak”(vazamentodeme-
mória),istoé,osobjetossãoalocadosemmemóriaeapósnãoseremmais
utilizadosnosprocessosdaaplicaçãoaindacontinuamsendoreferenciados,
impedindodestaformaqueoGarbageCollectorpossaretirá-losdamemória.
Comotempo,podegeraroestourodamemória.
Umaaplicaçãoque,porexemplo,nãoestádeacordocomasboaspráticas
deprogramação,mádefiniçãodeescopoeoutraspráticasnãorecomenda-
dasaindaencontradasnomercadotorna-sebastantevulnerávelaesteerro.
Podemosdizerqueumaaplicaçãorodeadademáspráticaséumabomba-
relógio. Namaioriadasvezes,osimplesaumentodeprocessamentoeuso
faráosistemaqueatéentãosupostamentefuncionavaperfeitamentecome-
çaraapresentarerrosdeestourodememória.
Aumentar o espaço alocado para a heap
Paraaumentaroespaçoalocadonaheap,podemosutilizardoisparâme-
trosnainiciaçãodaJVM.
-Xms<inteiro>[ (padrão byte) | k | m | g]
Define o tamanho inicial da heap
Exemplo: -Xms4096m
-Xmx<inteiro>[ (padrão byte) | k | m | g]
Define o tamanho máximo da heap
Exemplo: -Xmx4g
31

## Página 36

2.3. JVM32-bitesualimitaçãodeusodememória CasadoCódigo
Como utilizar os parâmetros da JVM
Opçõesboleanassãohabilitadasutilizando -XX:+<opção>edesa-
bilitadasutilizando -XX:-<opção>.
Opções numéricas são definidas utilizando
-XX:<opção>=<inteiro>. Os números podem ser incluídos
utilizando “m”ou “M”paramegabytes, “k”ou “K”parakilobytese
“g”ou “G”paragigabytes.Senenhumaletrafordefinidaseráutilizada
aconfiguraçãopadrãoembytes. Nãoéaceitonúmerosfracionários,
apenasinteiros.
Opçõesemtextosãodefinidasutilizando -XX:<opção>=<texto>;
Geralmenteespecificamumarquivo,umcaminhoouumalistadeco-
mandos.
Opçõesqueiniciamcom -Xnãosãopadronizadase,portanto,po-
demserretiradasemfuturasimplementaçõesdaJVM.
Opçõesquesãoespecificadascomo -XXpodemserretiradasoumo-
dificadasemfuturasversões.
Apesardasduasafirmaçõesacima,épossívelnotarquenasVMsim-
plementadasamaioriadosparâmetrostemsobrevividoàsnovasversões.
2.3 JVM 32-bit e sua limitação de uso de memória
Atualmentequandofalamosdemáquinasextremamenterápidas,alémdees-
tarmosnormalmentenosreferindoamáquinascommúltiplosprocessadores,
estamosnosreferindoamemóriasextremamentegrandes,muitosuperiores
a4gigabytes.Comosabemos,umaarquiteturade32-bitsconseguealocarno
máximo4gigabytesdememória(éumalimitaç ãomatemática,afinal232=
4g).
UmJVMde32bitsrodandonestesistemaconseguiráalocarumpouco
menosdoqueos4gigabytesdememória. Amaioriadasimplementações
daMáquinaVirtualJava,alémdesofreremrestriçõesprovenientesdoS.O.
utilizado,conseguemutilizaralgoemtornode2a3.5gigabytes.
32

## Página 37

CasadoCódigo Capítulo2. ConhecendoosParâmetrosdeConfiguraçãodaJVM
Paraconseguirmosutilizar4gigabytesoumaisdememória,devemosuti-
lizarumaJVMde64bitseumSistemaOperacionaleprocessadorcujamá-
quinavirtualpossuiessesuporte.AoiniciaraJVMdeve-seinformarodesejo
deutilizarsuafun çãode64bits.Istoéfeitoatravésdoparâmetro-d64.
2.4 M emória non-heap e problemas de estouro
de memória
Existemduasregiões(CodeCacheePermGen)namemóriapertencentesao
gruponon-heap.Normalmenteaqueapresentamaiorincidênciadeproble-
masrelacionadosaestourodememóriaéaPermGen.
Non-heap Permanent Generation
A Perm Gen é usada para armazenar as instâncias deClass
( java.lang.Class) e metadados (instâncias de classes do pacote
java.lang.reflect).Aplicaçõesquepossuemmuitasclassescarregadas
(classloading)ougeraçãodinâmicadeclassespodemrapidamenteencher
estaregião. OutracaracterísticamarcanteéqueosciclosdoGarbageCol-
lectorocorremcommuitomenosfrequência.
Outrapreocupaçãoquedeveexistirnestaregiãoestárelacionadacomo
“pooldestrings”.Estepoolébasicamenteumatabelahashondeasreferências
dosobjetosStringsãomantidas.QuandocriamosumaStringutilizandoum
literal,estaéalocadaautomaticamentenestepool.Outraformadissoacon-
teceréutilizandoométododeinstânciadenominado intern()daclasse
String.
Ométodo intern()utilizaosconceitosdopadrãodeprojetoFlyweight,
poisverificaseoobjeto Stringresponsávelpelachamadajáexistenopool,
sejáexistirretornaesteobjeto,esenãooincluinopooleretornaopróprio
objeto.
Antesdecontinuarmos,éimportanteentenderalistagemaseguir.Note
queadeclaraçãoutilizadana s1seráalocadanopool, s2nãoserá,poisnãoé
utilizadaapenasliterais.A s3somenteutilizaliterais,portantoseráalocado
nopool. Ainstânciada s4utilizaapalavrareservada newe,portanto,
nãoseráalocadanopool.Jáosobjetosdotipo Stringreferenciadospelas
33

## Página 38

2.4. Memórianon-heapeproblemasdeestourodememória CasadoCódigo
variáveis s5e s6sãoinseridosnopoolporcausadométodo intern()
apesardenainstânciainicialutilizando newissonãoocorrer.
Listagem 2.1- Trecho de código que demonstra vários exemplos de alo-
caçãodeStringesuarelaç ãocomopool.:
String ola = "Ola ";
String s1 = "Ola Mundo";
String s2 = ola + "Mundo";
String s3 = "Ola " + "Mundo";
String s4 = new String("Ola Mundo");
String s5 = s3.intern();
String s6 = new String("Ola Mundo").intern();
System.out.println(s1 == s2); // Valor exibido: false
System.out.println(s1 == s3); // Valor exibido: true
System.out.println(s1 == s4); // Valor exibido: false
System.out.println(s1 == s5); // Valor exibido: true
System.out.println(s1 == s6); // Valor exibido: true
Motivosparautilizarométodo intern():
• poupaaalocaçãodosobjetos Stringnamemóriaheap;
• acomparaçãoentreobjetos Stringutilizando ==énormalmente
maisrápidaqueutilizandoométodo equals().Ex.: s1.intern()
== s2.intern().
Motivosparanãoutilizar:
• Seaalocaçãonãoforrealizadacomcuidado,aPermGenpoderásofrer
comumestourodememória.
Listagem 2.2-CódigoqueocasionaráestourodememórianaPermGende-
poisdealocarStringsdemasiadamentenopool.:
public class TestPoolString {
public static void main(String[ ] args) {
34

## Página 39

CasadoCódigo Capítulo2. ConhecendoosParâmetrosdeConfiguraçãodaJVM
// Utiliza o padrão de projeto FlyWeight.
String texto = "Uma pobre String na Perm Gen...";
List<String> lista = ArrayList<String>();
for (int i=0; true; i++) {
String textoFinal = texto + i;
// Utiliza o padrão de projeto FlyWeight.
textoFinal = textoFinal.intern();
// Manter referenciado para que não
// seja coletado pelo GC.
lista.add(textoFinal);
}
}
}
Listagem 2.3-Códigoqueocasionaráestourodememórianaheapdepoisde
alocarStringsdemasiadamentesemutilizaropool.:
public class TestStringSemPool {
public static void main(String[ ] args){
// Somente a String abaixo é alocada no pool
String texto = "Não fui para o pool, fiquei na heap...";
List<String> lista = new ArrayList<String>();
for (int i=0; true; i++) {
// Sem utilizar o pool
String textoFinal = texto + i;
// Manter referenciado para que não
// seja coletado pelo GC.
lista.add(textoFinal);
}
}
}
35

## Página 40

2.4. Memórianon-heapeproblemasdeestourodememória CasadoCódigo
Valeressaltarquenamaioriadasvezesanecessidadedeajustedoespaço
alocadopodeserignorada,poisotamanhopadrãodefinidoéadequado.Con-
tudo,conformemencionado,programascommuitasclassescarregadasealo-
cando Stringsdemaisnopoolpodemnecessitardeumespaçomaiorde
alocaçãonaPermGen.
Deve-seobservarqueoespaçodaPermGenéalocadoforadaheap. A
conseqüênciadiretadissoéquepodemosverificarqueosparâmetros -Xms
e -Xmxsomentealteramotamanhodaheapeemnadaafetamoespaçoalo-
cadoparaaPermGen. Comovimos,épossívelatravésdeparâmetrosde
iniciaçãodaMáquinaVirtualJAVA(JVM),redimensionarváriossegmentos
damemória,inclusivea“permamentgeneration”.
Motivos para o estouro da memória
Aprincipalrazãoparaocorrerumproblemadealocaç ãonaPermGendiz
respeitoàquantidadedeclassescarregadasnaJVM.Seaaplicaç ãoformuito
extensa,provavelmenteseránecessárioutilizaroparâmetroapropriadopara
aumentaroseutamanho.
OutromotivoparaocorreroestourodememórianaPermGenestáre-
lacionadocomosservidoresdeaplicaç ãoquenãorealizamoredeploying
corretamente,acabandoporduplicarasclassescarregadas(classloaders)em
memória.Esteéomotivopeloqualalgunsservidoresdeaplicaç ãonãoreco-
mendamoredeploysemrestartdaaplicaç ão(hotdeploy)emambientesde
produção.Normalmenteamensagemqueacompanhaoestourodememória
naPermGenés“java.lang.OutOfMemoryError: PermGen space”.
Java HotSpot Server e Client
AJavaHotSpotClientVMsubstituiuamáquinavirtualclássicaeoscom-
piladoresJIT(JustinTime)utilizadosemversãoanterioresaoJava2.Estáme-
lhorajustadaparaambientes-cliente,poisemessênciavisareduzirotempo
destart-updasaplicaçõeseofootprintdamemória.Éomododefunciona-
mentoutilizadocomopadrãodasJVMs.
OJavaHotSpotServerVMobjetivaemessênciaousoemsistemascontí-
nuosinstaladosemservidoresdeaplicações.Apreocupaçãocomavelocidade
écrítica,porémapreocupaçãocomotempodestart-updaaplicaç ãoestáem
36

## Página 41

CasadoCódigo Capítulo2. ConhecendoosParâmetrosdeConfiguraçãodaJVM
segundoplano.ParaexecutaraJVMnestemodo,deve-senomomentodaini-
ciaçãoforneceroparâmetro -server.Exemplo:
java -server MinhaAplicacao
Aumentar o espaço alocado para a Perm Gen
Épossívelaumentarotamanhodestaregiãoutilizandonainiciaç ãoda
MáquinaVirtualJAVA(JVM)oparâmetro -XX:MaxPermSize.
AsJVMscostumamaceitaroparâmetro -XX:PermSizequedefine
o tamanho inicial da Perm Gen. Se ao utilizar-XX:PermSize e o
-XX:MaxPermSizefordetectadoqueovalorinicialnãoéosuficientepara
aplicação,recomenda-secolocarovalorinicialemáximoiguais,poisdesta
formaevita-sealgunsciclosdefulldoGCquepoderiamocorrerquandoa
PermGentiverqueserredimensionada.
Uso real de memória
Porexemplo,aoutilizaroparâmetro -Xms1gparaalterarotama-
nhodaheapetambémaPermamentGenerationpara 128mutilizando
-XX:MaxPermSize=128m,tem-seaofinalnomínimooconsumode
1152mb.Éimportantemencionarqueaindafaltariasercontabilizadaa
memóriaCodeCache,algumamemóriaqueaprópriaJVMutilizainter-
namenteeautilizadaparastackdecada Thread.
Espaço alocado no Code Cache e possibilidades de estouro
Normalmente,oespaçodestinadoaoCodeCacheéutilizadoparacom-
pilarearmazenarcódigonativo. Oprocessodegeraç ãodecódigonativoa
partirdoJavavariadependendodaarquiteturadaplataforma.
Geralmenteédivididoentreaarquiteturax86eaRISC.Duranteafase
decompilação,osmétodossãotraduzidoseminstruçõesdemáquinaque
podemserotimizadasdependendodacaracterísticaarquitetural. Ocódigo
compiladoécolocadoempartenesteespaço.
37

## Página 42

2.5. AmemóriaeaschamadasdiretasoGarbageCollector CasadoCódigo
Sãorarasassituaçõesquemotivamaocorrênciadeestourodememória
nestaregião,entretanto,seapósmonitoramentoforidentificadoqueseráne-
cessárioaumentá-la,existeapossibilidadedesolicitaràMáquinaVirtualeste
aumento.
Para aumentar o espaço alocado no Code Cache é necessário uti-
lizar o parâmetro -XX:ReservedCodeCacheSize na iniciação da
JVM. -XX:ReservedCodeCacheSize=<numero>[ (padrão byte) |
k | m | g] defineotamanhodoCodeCache.
Segueumexemploutilizandotodososparâmetrosvistosatéagora
java -server -d64 -Xms4g -Xmx4g -XX:PermSize=128m
-XX:MaxPermSize=256m -XX:ReservedCodeCacheSize=92m
MeuServidorDeAplicacao
2.5 A memória e as chamadas diretas o Garbage
Collector
Iniciareidefatocomumafrasepolêmica.Énormalqueoconsumodame-
móriacontinuamenteaumenteeistonãonecessariamentesignificaquehá
umproblema.OGarbageCollectordoJavaintencionalmentesomenteéexe-
cutadoquandonecessário,poisosciclosdeexecuçãocostumamsercustosos.
Éverdadequeváriosforamosavan çosnaversão5,6e7.Finalizando,umalto
consumodaheapémuitasvezesnormal.
OsalgoritmosutilizadospeloGarbageCollectorsão,emgrandepartedas
vezes,senãonamaioriaabsoluta,muitomaiseficientessegerenciadospela
própriaJVM.Nãoserecomendaquechamemoso System.gc()direta-
mente. AMáquinaVirtualJAVA(JVM)temtotalcondiçãodedeterminar
quandoémaisapropriadopararealizaracoleta.
Sefordetectávelquesuaaplicaçãoestátendoproblemasconstantesno
processamentoocasionandopausasemmomentosqueoGabageCollector
estánitidamentesendoexecutadosemnecessidade,éprovávelqueexistainú-
meraschamadasao System.gc().Defato,oquesevê,einclusiveématéria
dacertificaçãodeprogramador,queachamadadiretaaoGarbageCollector
nãonecessariamentefarácomqueaJVMexecuteociclodoGC,entretanto,é
38

## Página 43

CasadoCódigo Capítulo2. ConhecendoosParâmetrosdeConfiguraçãodaJVM
possívelnotarquehásimumainduçãogeradaquemuitasvezesinterferena
decisãodomomentodeexecução.
Estaschamadaspodemseroriundasdesuaaplicaç ãoousimplesmente
de alguma API utilizada. Recordo-me que em minha vida profissional
tivequeutilizarumaAPIparaconstruç ãodearquivoscompatíveiscomo
formatoExcelqueinternamenterealizavainúmeraschamadasaoGCcau-
sandonítidas“paradas”noprocessamentonormaldaaplicação. Épossível
solucionartambémesteproblema,poisasJVMspossuemumparâmetro,
-XX:+DisableExplicitGC,quepodeserfornecidonainiciaç ãoquede-
sabilitatodaequalquerchamadadiretaaoGC.
2.6 O utros Parâmetros
Seguemoutrosparâmetrosquealteramasdimensõesdamemória,porémsão
menosutilizados:
•-XX:MaxNewSize=<número>Tamanhomáximodayoung(newge-
neration).DesdeaJDK1.4estevalorécalculadoapartirdoNewRatio.
•-XX:NewRatio=<número>Razãodayoung(eden+survivor)sobre
atenured(oldgeneration).
•-XX:NewSize=<número>Tamanhopadrãodayoung(newgenera-
tion).
•-XX:SurvivorRatio=<inteiro>Razãodamemóriaedensobrea
survivor.
Amaioriadosparâmetrostemvalorespadrõesdependentesdosistema
operacionaledaarquitetura(32-bitou64-bit).
AmemóriaYoungGenerationédefinidapeloparâmetroquedefineo
limiteinferior(NewSize)eoparâmetroquedefineolimitesuperior(Max-
NewSize). Comoécompostapelaedeneasurvivor(toefromspace),ao
serredimensionada,acabaporaumentarproporcionalmentetodasasregiões
envolvidas.
39

## Página 44

2.7. ComoverificarousodamemórianaJVM CasadoCódigo
2.7 C omo verificar o uso da memória na JVM
Podeserrealizadoutilizandooparâmetro-XX:+PrintGCDetailsparamos-
trarinformaçõessobretodaamemóriaatravésdecadaciclode“garbage
collection”enquantooprogramaestiveremexecução,dandoaofinalum
“snapshot”damemória.
Aseguirvemosumexemplodeocorrênciadedoisciclosdegarbagenor-
maleoutrofull.Oimportanteéentenderainformaç ão.Vejaquenestecaso
aTenurednãofoialiviadaapósaGC.NotetambémqueocicloFulldaGC
tambémnãoconseguiuliberarmemóriaalgumaeprovavelmenteembreve
teremosumestourodememória.
OsciclosFulldoGCnormalmenteocorremantesdequalquerredimen-
sionamentooudeatingirolimitedamemória.Éumprocessomaiscustoso
queumciclonormaldaGCevisaevitaroredimensionamentoliberando
maiorquantidadedememória,poisémaisminucioso(consequentemente
maislento)queociclodeGCnormal.
[ GC [ DefNew: 959K->64K(960K), 0.0014005 secs]
12289K->11633K(12728K), 0.0014619 secs]
[ Times: user=0.00 sys=0.00, real=0.00 secs]
[ GC [ DefNew: 960K->64K(960K), 0.0008898 secs]
[ Tenured: 11808K->11872K(11896K), 0.0367320 secs]
12529K->11872K(12856K), [ Perm : 18K->18K(12288K)],
0.0396587 secs] [ Times: user=0.05 sys=0.00, real=0.05 secs]
[ Full GC [ Tenured: 483968K->483968K(483968K), 1.5431730 secs]
520256K->520255K(520256K), [ Perm : 1691K->1691K(12288K)],
1.5433371 secs] [ Times: user=1.50 sys=0.03, real=1.53 secs]
AoiniciaraVMcomestaop ção,seráexibidoalgosemelhanteaoabaixo:
(nesteexemplofoiutilizadoaJDK6u10).
Heap
def new generation total 36288K, used 36287K
[ 0x02990000, 0x050f0000, 0x050f0000)
eden space 32256K, 100% used
[ 0x02990000, 0x04910000, 0x04910000)
40

## Página 45

CasadoCódigo Capítulo2. ConhecendoosParâmetrosdeConfiguraçãodaJVM
from space 4032K, 99% used
[ 0x04d00000, 0x050effe8, 0x050f0000)
to space 4032K, 0% used
[ 0x04910000, 0x04910000, 0x04d00000)
tenured generation total 483968K, used 483968K
[ 0x050f0000, 0x22990000, 0x22990000)
the space 483968K, 100% used
[ 0x050f0000, 0x22990000, 0x22990000, 0x22990000)
compacting perm gen total 12288K, used 1691K
[ 0x22990000, 0x23590000, 0x26990000)
the space 12288K, 13% used
[ 0x22990000, 0x22b36c98, 0x22b36e00, 0x23590000)
No shared spaces configured.
O“snapshot”exibidonesteartigopertenceaumaaplicaçãoJavafinalizada
atravésdométodo System.exit()umpoucoantesdeocorreroestouro
dememórianaheap.Éimportanteentenderocomportamentoaoutilizaro
parâmetro -XX:+PrintGCDetails.Reparequeseoestourodamemória
ocorresse,avisãodamemóriaexibidaseriacompletamentediferente,poisas
regiõesjáapareceriamesvaziadas.
2.8 U tilizando as classes JAV A do pacote
jav a.lang.management
Programaticamenteépossívelverificaramemóriacomoumtodoutilizando
classesdopacote java.lang.management.Asclassesnecessáriaspodem
servisualizadasnodiagramadeclassescontidonafigura 2.3.
41

## Página 46

2.8. UtilizandoasclassesJAVAdopacotejava.lang.management CasadoCódigo
Fig.2.3:DiagramadeClassesqueforneceinformaçõessobreousodamemó-
rianaJVMdopacotejava.lang.management.
Ocódigopresentenalistagemaseguiréutilizadoparaexemplificaras
informaçõesdememóriaquepodemserobtidascomalgumasdasclassesdo
pacote java.lang.management.
Listagem 2.4 - Implementação da classe que obtém informações da me-
mória.:
public class Main {
public static int MEGA = 1024 * 1024;
public static String FORMAT = " (%.2fmb)";
public static void main(String... args) {
MemoryMXBean memoryBean =
ManagementFactory.getMemoryMXBean();
42

## Página 47

CasadoCódigo Capítulo2. ConhecendoosParâmetrosdeConfiguraçãodaJVM
out.println("::: Memória heap :::");
out.println();
MemoryUsage heapMemory = memoryBean.getHeapMemoryUsage();
out.println("Tamanho Inicial :: " + heapMemory.getInit()
+ String.format(Locale.US, FORMAT,
(double) heapMemory.getInit() / MEGA));
out.println("Tamanho Atual :: " +
heapMemory.getCommitted()
+ String.format(Locale.US, FORMAT,
(double) heapMemory.getCommitted() / MEGA));
out.println("Usado :: " + heapMemory.getUsed()
+ String.format(Locale.US, FORMAT,
(double) heapMemory.getUsed() / MEGA));
out.println("Máximo :: " + heapMemory.getMax()
+ String.format(Locale.US, FORMAT,
(double) heapMemory.getMax() / MEGA));
out.println();
out.println("::: Memória non-heap :::");
out.println();
MemoryUsage nonheapMemory =
memoryBean.getNonHeapMemoryUsage();
out.println("Tamanho Inicial :: " +
nonheapMemory.getInit()
+ String.format(Locale.US, FORMAT,
(double) nonheapMemory.getInit() / MEGA));
out.println("Tamanho Atual :: " +
nonheapMemory.getCommitted()
+ String.format(Locale.US, FORMAT,
(double) nonheapMemory.getCommitted() / MEGA));
out.println("Usado :: " + nonheapMemory.getUsed()
+ String.format(Locale.US, FORMAT,
(double) nonheapMemory.getUsed() / MEGA));
out.println("Máximo :: " + nonheapMemory.getMax()
+ String.format(Locale.US, FORMAT,
(double) nonheapMemory.getMax() / MEGA));
out.println();
43

## Página 48

2.9. DesmistificandoopooldeStrings CasadoCódigo
out.println(":: Pool de memórias (organização JVM) ::");
out.println();
List<MemoryPoolMXBean> list =
ManagementFactory.getMemoryPoolMXBeans();
for (MemoryPoolMXBean m : list) {
out.println("Nome do Pool :: " + m.getName());
out.println("Grupo :: " + m.getType());
out.println();
MemoryUsage usage = m.getUsage();
out.println("Inicial: " + usage.getInit()
+ String.format(Locale.US, FORMAT,
(double) usage.getInit() / MEGA));
out.println("Atual: " + usage.getCommitted()
+ String.format(Locale.US, FORMAT,
(double) usage.getCommitted() / MEGA));
out.println("Usado: " + usage.getUsed()
+ String.format(Locale.US, FORMAT,
(double) usage.getUsed() / MEGA));
out.println("Maximo: " + usage.getMax()
+ String.format(Locale.US, FORMAT,
(double) usage.getMax() / MEGA));
out.println();
}
}
}
2.9 D esmistificando o pool deStrings
Váriasconfusõesdeentendimentoestãorelacionadasaopoolde Strings,
muitosacreditamqueapósumaStringseralocadanestaáreaficaráatéque
aJVMtenhasuaexecuç ãointerrompida. Outrosacreditamquenãoocor-
remciclosdeGCnaPermGen.Éimportantenotarqueosobjetos String
quesãoalocadosnopoolalipermanecemenquantoforemreferenciados.Ao
perderemareferência,opróximociclodeGCiráretirá-losdaPermGennor-
44

## Página 49

CasadoCódigo Capítulo2. ConhecendoosParâmetrosdeConfiguraçãodaJVM
malmente.
Emresumo,nãoacreditequeoobjeto Stringexistiránopoolatéofim
daaplicação,poisdefatonãoéesseocomportamento.Analisemosaclasse
mencionadanalistagemaseguirutilizandoasinformaçõesqueobtemosaté
agora.Estaclasseéresponsávelpelasaídavisualizadanalistagemposterior.
Listagem 2.5-ClassequedemonstraaocorrênciadoGCnaregiãoPermGen
paradesalocarobjetosStringarmazenadosnopool.:
public class TestePermGenString {
public static final int MEGA = 1024 * 1024;
public static final String FORMAT = "%.2f mb";
public static void main(String... args) {
String str = "Ola mundo";
List textos = new ArrayList();
MemoryPoolMXBean mp = getPermGenMemory();
for (int i = 0; true; i++) {
String str2 = (str + i).intern();
if (i % 100000 == 0) {
MemoryUsage mu = mp.getUsage();
System.out.println("PermGen inicial: "
+ String.format(FORMAT,
(double) mu.getInit() / MEGA)
+ " commitada:" + String.format(FORMAT,
(double) mu.getCommitted() / MEGA)
+ " utilizada: " + String.format(FORMAT,
(double) mu.getUsed() / MEGA)
+ " max: " + String.format(FORMAT,
(double) mu.getMax() / MEGA));
}
if (i == 200000) {
System.out.println("Retirar a " +
45

## Página 50

2.9. DesmistificandoopooldeStrings CasadoCódigo
"referência das Strings do pool.");
textos = new ArrayList();
}
textos.add(str2);
}
}
public static MemoryPoolMXBean getPermGenMemory() {
MemoryPoolMXBean mp = null;
List<MemoryPoolMXBean> lista =
ManagementFactory.getMemoryPoolMXBeans();
for (MemoryPoolMXBean m : lista) {
if ((m.getType() == MemoryType.NON_HEAP) &&
(m.getName().toUpperCase().indexOf("PERM") != -1)) {
mp = m;
break;
}
}
return mp;
}
}
Nestaclasse,utilizamosalguns“númerosmágicos”paravisualizarmos
emdeterminadospontosasituaçãodaPermGen. Alistagemaseguirnos
permiteobservarváriasquestõesreferentesàgerênciadememóriadaJVM.
Reparequecome çamosaaplicaçãocomaPermGeninicialmentedimensi-
onadapara4mbenodecorrerdaexecuç ãoestetamanhoéconstantemente
redimensionado (memória disponibilizada para JVM ou commitada) até
seulimitede16mbparaquepossasuportarasnovasalocaçõesnopoolde
Strings.
Listagem 2.6 - Visão dadinâmica de execução dos ciclosFull do GC na
PermGencomointuitodeevitaroredimensionamentoatéqueocorreo
estouro de memória provocado pelo excesso de Strings armazenadas no
pool.:
PermGen inicial: 4,00 mb commitada:4,00 mb
46

## Página 51

CasadoCódigo Capítulo2. ConhecendoosParâmetrosdeConfiguraçãodaJVM
utilizada: 1,72 mb max: 16,00 mb
[ Full GC [ Tenured: 1563K->665K(4096K), 0.0559573 secs]
2166K->665K(5056K), [ Perm : 8191K->8191K(8192K)],
0.0560523 secs] [ Times: user=0.06 sys=0.00, real=0.06 secs]
PermGen inicial: 4,00 mb commitada:8,25 mb
utilizada: 8,24 mb max: 16,00 mb
[ Full GC [ Tenured: 1441K->924K(4096K), 0.0785669 secs]
1612K->924K(5056K), [ Perm : 12287K->12287K(12288K)],
0.0786638 secs] [ Times: user=0.08 sys=0.00, real=0.08 secs]
PermGen inicial: 4,00 mb commitada:15,25 mb
utilizada: 15,11 mb max: 16,00 mb
Retirar a referência das Strings alocadas no pool.
[ Full GC [ Tenured: 2087K->216K(4096K), 0.0481254 secs]
2933K->216K(5056K), [ Perm : 16384K->4017K(16384K)],
0.0492858 secs] [ Times: user=0.05 sys=0.00, real=0.05 secs]
[ Full GC [ Tenured: 1046K->493K(4096K), 0.0678745 secs]
1715K->493K(5056K), [ Perm : 8191K->7276K(8192K)],
0.0680447 secs] [ Times: user=0.06 sys=0.00, real=0.06 secs]
PermGen inicial: 4,00 mb commitada:9,25 mb
utilizada: 9,00 mb max: 16,00 mb
[ Full GC [ Tenured: 1010K->924K(4096K), 0.1010554 secs]
1841K->924K(5056K), [ Perm : 11519K->11519K(11520K)],
0.1011260 secs] [ Times: user=0.09 sys=0.02, real=0.11 secs]
[ Full GC [ Tenured: 924K->924K(4096K), 0.1642016 secs]
1518K->924K(5056K), [ Perm : 15615K->15615K(15616K)],
0.1642776 secs] [ Times: user=0.16 sys=0.00, real=0.16 secs]
PermGen inicial: 4,00 mb commitada:16,00 mb
utilizada: 15,87 mb max: 16,00 mb
[ Full GC [ Tenured: 2087K->1312K(4096K), 0.1679544 secs]
2660K->1312K(5056K), [ Perm : 16383K->16383K(16384K)],
0.1680335 secs] [ Times: user=0.16 sys=0.02, real=0.17 secs]
[ Full GC [ Tenured: 1312K->1306K(4096K), 0.2110858 secs]
1312K->1306K(5056K), [ Perm : 16383K->16382K(16384K)],
0.2111585 secs] [ Times: user=0.22 sys=0.00, real=0.22 secs]
[ Full GC [ Tenured: 1306K->1306K(4096K), 0.1619602 secs]
1324K->1306K(5056K), [ Perm : 16384K->16384K(16384K)],
0.1620658 secs] [ Times: user=0.14 sys=0.01, real=0.16 secs]
[ Full GC [ Tenured: 1306K->1306K(4096K), 0.1750233 secs]
1306K->1306K(5056K), [ Perm : 16384K->16384K(16384K)],
47

## Página 52

2.10. ConsideraçõesFinais CasadoCódigo
0.1751015 secs] [ Times: user=0.17 sys=0.00, real=0.17 secs]
[ Full GC [ Tenured: 1306K->143K(4096K), 0.0573083 secs]
1325K->143K(5056K), [ Perm : 16384K->2186K(16384K)],
0.0584201 secs] [ Times: user=0.06 sys=0.00, real=0.06 secs]
Exception in thread "main" java.lang.OutOfMemoryError:
PermGen space
at java.lang.String.intern(Native Method)
Tambémépossívelnotarqueexisteumarelaçãodiretaentreaocorrência
deumcicloFulldeGCeoredimensionamentodamemórianestaregião.
Outrainformaçãointeressante,aopararmosdereferenciarosobjetosString
jáalocadasnopool,ocicloFulldeGCéeficazeconsegueliberarboaparte
damemória.
Continuandoaanálisedalistagempode-senotarqueapósaliberaç ão
inicialdosobjetosnãoreferenciados,continuamenterealizamosnovasaloca-
çõesefatalmente,mesmoapesardeváriosciclosFulldeGC(ineficazespois
háreferênciaasestas Stringsalocadasnopool)amemóriaétotalmente
preenchidaeocorreoestourodememórianestaregião.
IntencionalmenteforamretiradasdalistagemosciclosdeGCnãofullda
heap,poisocorremcommuitomaisfrequênciaeprejudicavamoentendi-
mentodoexemplo.
2.10 C onsiderações Finais
Oobjetivodesteartigoéaumentaroníveldeconhecimentodosprofissionais
comaorganizaçãodamemóriautilizadanamáquinavirtualJAVA.Também
éintençãoapresentaralgumastécnicasdeverificaçãodetodaamemóriabus-
candoevitarumestourodememóriapormáconfiguraç ão.Existeminúme-
rasaplicaçõesquemonitoramaJVM.Háduasquesedestacam:JConsolee
JVisualVM.Recomendoaosdesenvolvedoresdaremumaolhadanessasfer-
ramentasebuscartambémoutrasalternativas.
2.11 R eferências
• Java Application no Solarishttp://java.sun.com/j2se/1.5.0/docs/
tooldocs/solaris/java.html
48

## Página 53

CasadoCódigo Capítulo2. ConhecendoosParâmetrosdeConfiguraçãodaJVM
• OrganizaçãodamemóriaeGC http://java.sun.com/docs/hotspot/gc5.
0/gc_tuning_5.html
• PáginadaSUNsobreosparâmetrosdeiniciaçãodaJVM http://java.
sun.com/javase/technologies/hotspot/vmoptions.jsp
• Perguntas e respostas sobre Java Hotspot VMhttp://java.sun.com/
docs/hotspot/HotSpotFAQ.html
• PerguntaserespostassobreGCnaJavaHotspotVM http://java.sun.
com/docs/hotspot/gc1.4.2/faq.html
• ArtigosobreestourodememórianaPermamentGeneration http://
blogs.sun.com/fkieviet/entry/classloader_leaks_the_dreaded_java
• ExcelentecompilaçãosobreosparâmetrosaceitospelasJVMsSUN
http://blogs.sun.com/watt/resource/jvm-options-list.html
49

## Página 55

Capítulo3
Serializaçãodeobjetos:da
memóriaparaodisco
“ Aprenda a utilizar os recursos que a linguagem Java provê ao programador
para realizar de maneira simples, o armazenamento de objetos em formato
mais simples, a persistência dos dados em formato sequencial. ”
–porLeandroYung
Guardarinformaçõescontidasnosobjetospodesermuitoútilparaapli-
cações. Essasinformaçõespodemserusadasparamanteramemóriadas
configuraçõesatuaisparaumusofuturo,guardarosdadosdeumaagenda
telefônica,cálculosouqualqueroutracoisa.Alémdisso,podemosusareste
mesmomecanismoparaexportardadosentremesmasaplicaçõessendoexe-
cutadasemlocaisdistintos.Ouaindamaisalém,transferirinformaçõesentre
aplicaçõesatravésdarede.

## Página 56

3.1. SerializaçãoeDesserialização CasadoCódigo
TudoissoépossívelmuitofacilmentenatecnologiaJavapelaexistência
demecanismosdeconversãodeatributoseestadosdeobjetosemformasde
dadosmaissimples,númerosebitsemumprocessochamadodeserializaç ão
dedados.
3.1 S erialização e Desserialização
Serializaçãoéoprocessodearmazenarosdadosdeumobjetoeenvolvea
transformaçãodasvariáveisouatributosdeumobjetoemmemóriaemby-
tesoucaracteres,ouseja,converterdadosinteligíveisemnúmerosparapo-
dermosguardaremumarquivo.Desserializaçãoéoprocessocontrário,que
realizaaleituradosdadosemformadenúmerosoucaractereseconstróium
objetoapartirdomesmo.
Felizmente,paraoprogramadorJava,alinguagemprovêmecanismos
simpleseautomatizadospararealizarmosessatarefasemanecessidadede
escrevermosoutraduzirmosparaocomputadoramaneiraqueosdadosse-
rãoescritosoulidos.
3.2 jav a.io.Serializable
Serializaçãodedadoséoprocessomaissimplesdearmazenamentoouper-
sistênciadeobjetos.Paratanto,umobjetoquedesejamosarmazenar,precisa
apenas implementar uma interface chamadajava.io.Serializable.
Essainterfacenãopossuinenhummétodo,apenasserveparaindicaraoJava
queosobjetosdaclasseesubclassessãopossíveisdeserempersistidosdema-
neiraserializada.
Vamoscriarumaclassesimpleschamada Pessoaeiremospermitira
gravaçãodestanodisco,conformelistagemaseguir.
Listagem 3.1-Classequeseráserializada:
import java.io.Serializable;
public class Pessoa implements Serializable {
private String nome;
52

## Página 57

CasadoCódigo Capítulo3. Serializaçãodeobjetos:damemóriaparaodisco
private String telefone;
public Pessoa() {
}
public String getNome() {
return nome;
}
public void setNome(String nome) {
this.nome = nome;
}
public String getTelefone() {
return telefone;
}
public void setTelefone(String telefone) {
this.telefone = telefone;
}
}
Pode-senotarqueaclasse Pessoanãopossuimétodosdistintos,apenas
amarcação implements Serializable eissojábasta.Naclasse,defini-
mososatributos nomee telefonedotipo String.Emseguidaédefinido
umconstrutor,usadoduranteacriaçãodoobjeto,quenocasoéumconstru-
torvazio.Naslinhasdecódigoseguintessãodefinidososmétodosdeacesso
paraosatributos.
Métodosdeacessosãoumaboapráticaparaevitarqueosdadosdeum
objetosejamvistosealteradosdemaneiraindevida.Dessamaneira,oacesso
diretoparaumavariávelébloqueadaesóépermitidaseoprogramadortiver
escritoométodoparateracesso.Naprática,então,sósepodelereescrever
aquiloqueaclassepermite. Assim,porexemplo,nãodeveriaseracessível
paraleituraovalordeumasenha,casocontrário,qualquerprogramapoderia
iraoobjetoerecuperarasenhadomesmo.Damesmaforma,nãopodeser
acessívelparamodificaçãoocampocomototaldacompradeumcarrinhode
compras,casocontrário,umprogramapoderiairealteraromesmo,gerando
umainconsistência.
Temosentãoumobjetoquepodeserescritoeguardadodemaneira
‘Serializada’. Precisamosagoradesenvolverumprogramaqueirácriarum
53

## Página 58

3.2. java.io.Serializable CasadoCódigo
objetoeguardaresseobjetonodisco. Esseprogramaestáapresentadona
listagemaseguir:
Listagem 3.2-ClassequearmazenaumaPessoacomserializaç ão:
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
public class CriaEArmazenaPessoas {
public static void escreve(Pessoa p) {
try {
FileOutputStream fout =
new FileOutputStream("Grava.dados");
ObjectOutputStream oos =
new ObjectOutputStream(fout);
oos.writeObject(p);
oos.close();
fout.close();
} catch (IOException e) {
e.printStackTrace();
}
}
public static void main(String[] args) {
System.out.println("Criando Pessoa.");
Pessoa p1 = new Pessoa();
p1.setNome("Leandro");
p1.setTelefone("3xxx-xxxx");
System.out.println("Escrevendo Pessoa");
escreve(p1);
System.out.println("Terminado");
}
}
Nométodo main(),inicialmenteéimpressaamensagemnateladamen-
sagemeemseguidaécriadoumobjetodotipo Pessoa.Emseguidaosva-
loresdosatributossãoinseridosnoobjetoeporfiméexecutadoométodo
escreve()querecebecomoparâmetrooobjetodotipo Pessoa.
54

## Página 59

CasadoCódigo Capítulo3. Serializaçãodeobjetos:damemóriaparaodisco
Seráexecutadoentãoométodo escreve(),queiniciacomumbloco
detratamentodeerrosobrigatório,poistodoacessoaodiscopodegerarer-
rosduranteaexecução.Primeiramenteécriadoumfluxodeacessoaodisco
( FileOutputStream)paraoarquivochamado Grava.dados,quepode
aindanãoexistir(casooarquivoexista,aoexecutarmosoprograma,iremos
sobrescreverosdadosqueexistiamperdendoosdadosantigos).Emseguida,
cria-seumfiltrosobreofluxoacessoaodiscoparaobjetosserializáveis,cha-
mado ObjectOutputStream.Feitatodaestapreparação,estamosprontos
parapoderescreveroobjetoparaodisco.
Oobjetointeiroéenviadoparaofluxodesaídadeobjetosatravésdomé-
todo writeObject().Feitaaescrita,podemosfecharosfluxoseterminar
ométodo,voltarparaométodoprincipaleterminaroprograma.
Selistarmosoconteúdodoarquivo‘Grava.dados’,podemosverosdados
doobjetoarmAzenado.Parafazerisso,abraumajaneladoconsoleedigiteo
comandodelistagem(noWindows,digite typee,noUnix,digiteocomando
cat).Algocomoafigura 3.1serámostrado.
Fig.3.1:ListagemdoarquivoGrava.dados.
Pararestaurar,oudesserializaroconteúdonamemória,precisaremos
fazeraleituradosdadosnovamente,paratanto,vejaocódigodalistagema
seguir.
Listagem 3.3-Lendoumobjetoserializado:
import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
public class LeERestauraPessoas {
public static Pessoa le() {
try {
55

## Página 60

3.2. java.io.Serializable CasadoCódigo
FileInputStream fin =
new FileInputStream("Grava.dados");
ObjectInputStream ois =
new ObjectInputStream(fin);
Pessoa p = (Pessoa) ois.readObject();
ois.close();
fin.close();
return p;
} catch (IOException e) {
e.printStackTrace();
return null;
} catch (ClassNotFoundException e) {
e.printStackTrace();
return null;
}
}
public static void main(String[] args) {
System.out.println("Lendo Pessoa.");
Pessoa objetoLido = le();
System.out.println("Executado.");
System.out.println("Nome: "
+ objetoLido.getNome());
System.out.println("Telefone: "
+ objetoLido.getTelefone());
}
}
Novamente,oprogramainiciaaexecuçãopelométodo main().Apre-
sentaamensagemnatelaechamaométodo le().Depoisdoblocodetrata-
mentodeexce ções,écriadoumfluxodeleituradoarquivo,apontandoparao
arquivodenome Grava.dadosgeradoanteriormente.Emseguida,cria-se
umfluxodeleituradeobjetossobreofluxodeleituradearquivo,paramontar
objetosapartirdosdadoslidosdoarquivo. Porfim,éfeitaaleituradeum
objetoapartirdafonteefazemosumaconversão(typecasting)doobjetolido
paraoobjetodaclasse Pessoa.Ométodoéfinalizadofechandooleitorde
objetoseoarquivolido.
Casotudoestejacorreto,éretornadaareferênciaparaoobjetorecons-
56

## Página 61

CasadoCódigo Capítulo3. Serializaçãodeobjetos:damemóriaparaodisco
tituídonaleitura. Oprogramavoltaparaaexecuç ãodométodoprincipal,
colocandoovalordareferênciadoobjetolidonavariável objetoLido.Nas
linhasdecódigoseguinte,osdadossãoapresentadosnatela.
3.3 N em tudo é perfeito
Ótimo,conseguimosguardarosdadosedepoislê-loseutilizá-losnovamente.
Ficamosentãotentadosausaromecanismodeserializaç ão-desserialização
paraarmazenardadosdenossasaplicações, exportar, etc. Vamosalterar
nossaclasse Pessoaparaincluirumnovocampo, sobrenome,conforme
listagemaseguir.
Listagem 3.4-AdicionandoumnovoatributoaclassePessoa:
import java.io.Serializable;
public class Pessoa implements Serializable {
private String nome;
private String sobrenome;
private String telefone;
public Pessoa() {
}
public String getNome() {
return nome;
}
public void setNome(String nome) {
this.nome = nome;
}
public String getSobrenome() {
return sobrenome;
}
public void setSobrenome(String sobrenome) {
this.sobrenome = sobrenome;
}
public String getTelefone() {
return telefone;
57

## Página 62

3.3. Nemtudoéperfeito CasadoCódigo
}
public void setTelefone(String telefone) {
this.telefone = telefone;
}
}
Incluímosàclassejáexistente,ocampo sobrenomedotipo Stringe
adicionamosmaisdoismétodos, getSobrenome()e setSobrenome().
Orestodaclassepermaneceusemalteração.Serodarmosnovamenteaclasse
LeERestauraPessoas,oresultadoseráalgocomomostradonafigura 3.2.
Fig.3.2: FalhanaexecuçãodeLeERestauraPessoasapósalteraç ãodaclasse
serializada.
Oprogramaapresentouerroaolerosdadosarmazenados. Issoporque
osdadosforamguardadossegundoumaestruturaseq üencial,aolernova-
menteetentarcolocarosdadosseq üenciaisnoscamposcorrespondentesdo
objeto,oprogramaencontraoutroobjetodemesmonome,masincompatível
porserestruturalmentediferente,nãoconseguindoassimrestaurarosdados
originais.
Ocustodafacilidadeedousodemecanismospadronizadosdepersistir
osdadosdeumobjetotememcontrapartidaumamenorflexibilidadeamu-
danças. Umobjetoserializadopoderáserlidoeescritosemproblemassea
classeoriginárianãofoialterada,casosejaalterada,teremosproblemaspara
lê-lo.
58

## Página 63

CasadoCódigo Capítulo3. Serializaçãodeobjetos:damemóriaparaodisco
3.4 P ersistindo atributos: normais, transien-
tes e estáticos
Ocomportamentodosatributossãodistintos. Nemsempregostaríamosde
gravartodososdadossobformaserializada,poisalgumasvezesnãoquere-
mosguardaralgumasinformaçõesnoarquivo.
Asrazõespodemserdediversasnaturezas.Porexemplo,pelomotivodos
dadosdoarquivoserializadopoderemserfacilmentelidoscomumeditorde
textooubinário,temosrazõesdeseguran çaparanãoarmazenarmoscampos
desenhaenúmerodecartõesdecréditonestestiposdearquivos. Oupor
questõesdequeosdadosnomomentoqueforemrecuperadospodemnão
serválidos.Seriaocasodeatributoscomoodehoraatual,listadeusuários
presentesnosistema,cálculos,etc.
Algumasvezes,objetosreferenciadosemumdadomomentopodemnão
existiremumoutromomentonofuturo,comoporexemplo,objetosdeda-
dos,umajanelaespecíficadeapresentaç ão,umcampodetexto,entreou-
trascoisas.Outrasvezes,umobjetodependederecursosforadoJava,uma
Threadirá depender de recursos do sistema operacional; um objeto de
acessoaredeirádependerdeconexõeseoutrascoisasmais.
Paraessescasos, existeomodificador transient, quedizqueum
determinadoatributonãodeveserarmazenadoemdisco.Paraverificarum
exemplo,analiseofuncionamentodalistagemaseguir.
Listagem 3.5-AdicionandoumnovoatributoaclassePessoa:
import java.io.Serializable;
public class Item implements Serializable {
private static long numeroSequencia;
private String usuario;
private long matricula;
private transient String senha;
public Item() {
numeroSequencia = System.currentTimeMillis();
usuario = "Nenhum";
59

## Página 64

3.4. Persistindoatributos:normais,transienteseestáticos CasadoCódigo
matricula = System.currentTimeMillis();
senha = "Nenhuma";
}
public String toString() {
return "Item: numeroSequencia=" + numeroSequencia +
", usuario=" + usuario +
", matricula=" + matricula +
", senha=" + senha;
}
public static long getNumeroSerial() {
return numeroSequencia;
}
public static void setNumeroSerial(long numeroSerial) {
Item.numeroSequencia = numeroSerial;
}
public long getMatricula() {
return matricula;
}
public void setMatricula(long matricula) {
this.matricula = matricula;
}
public String getSenha() {
return senha;
}
public void setSenha(String senha) {
this.senha = senha;
}
public String getUsuario() {
return usuario;
}
public void setUsuario(String usuario) {
this.usuario = usuario;
}
}
ObservequeosatributosdaclasseItempossuemcaracterísticasdiferen-
tes.Omodificadordevisiblidade( private, protectedou public)não
alteraocomportamentodaserialização,enessaclassetodososatributossão
60

## Página 65

CasadoCódigo Capítulo3. Serializaçãodeobjetos:damemóriaparaodisco
private.
Temosoatributo numeroSequencia,umavariáveldeclasse(estática)
dotipolong. Variáveisestáticassãoaquelasquepertencemàclasseeterão
umúnicovalorparatodososobjetosdaquelaclasse,ouseja,semodificada
diretamenteouemumobjeto,essamudan çaserávistaportodososobjetos.
Temosoatributo usuario,umavariáveldeobjeto(não-estática)da
classe String.Variáveisdeobjetosãovariáveisdeinstância,seuconteúdo
nãoévistopelaclassediretamente,nemporoutrosobjetosexistentes.Temos
a matricula,outravariáveldeobjeto,dotipo long.Porfim,temos senha,
umavariáveldeobjeto String,noentanto,queestaestásendomodificada
pelomarcador transient.
Vejamosentãocomoestasvariáveisdistintassecomportamnoprocesso
deserialização. Vamoscriarumaclasseutilitáriaquepossuiummétodo
paragravaçãodeumobjetoeoutropararecuperaç ãodoobjeto,conformea
listagemaseguir.
Listagem 3.6 - Classe utilitária para gravação e recuperação de objetos
emarquivos:
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
public class FileUtilities {
public static void escreva(String nomeArq, Item item) {
try {
FileOutputStream fout =
new FileOutputStream(nomeArq);
ObjectOutputStream oos =
new ObjectOutputStream(fout);
oos.writeObject(item);
oos.close();
fout.close();
} catch (IOException e) {
e.printStackTrace();
61

## Página 66

3.4. Persistindoatributos:normais,transienteseestáticos CasadoCódigo
}
}
public static Item leia(String nomeArq) {
Item item = null;
try {
FileInputStream fin =
new FileInputStream(nomeArq);
ObjectInputStream ois =
new ObjectInputStream(fin);
item = (Item ) ois.readObject();
ois.close();
fin.close();
} catch (IOException e) {
e.printStackTrace();
} catch (ClassNotFoundException e) {
e.printStackTrace();
}
return item;
}
}
Ométodo escreva()recebeonomedoarquivoparaondeoobjetoserá
escritoeumobjetodotipo Itemparaescrevernoarquivo.Inicialmente,abri-
mosumfluxoparaestearquivo,eemseguidaumfluxodeescritadeobjetos
sobreofluxocriadoparaoarquivo.Porfim,escrevemosoarquivonofluxo
deobjetosefechamosassaídas.
Ométodo leia()recebeumnomedearquivoelêoobjeto Itemarma-
zenadodentrodele.Primieramente,criamosumavariávelquerecebeoobjeto
dotipo Itemlido.Emseguida,cria-seumfluxodeleituradearquivoapon-
tandoparaonomepassadocomoparâmetro,eumfluxodeleituradeobjetos
sobreoarquivodeleitura.Emsequenciatentamosleroobjetodoarquivoe
realizaraconversãodoobjetolidoparaotipo Item.Sealeituraocorreucor-
retamente,seráretornadooobjetorestaurado,ecasoocorraalgumproblema
seráretornadoovalornulo( null).
Temosnossaclassededadoseaclassequeiránosajudaraescrevere
lerobjetos. Faltaagorafazerasclassesdeaplicaç ãoparapodermosfazera
62

## Página 67

CasadoCódigo Capítulo3. Serializaçãodeobjetos:damemóriaparaodisco
execução,gravaçãoeleituradosobjetos.Vamoscome çarpelagravação,veja
aclassenalistagemaseguir.
Listagem 3.7-Classequecriaumitemeogravaemumarquivo:
public class CriaItem {
public static void main(String[] args) {
System.out.println("Criando Objeto");
Item item = new Item();
System.out.println(item);
System.out.println("Alterando Valores");
item.setMatricula(123456);
item.setSenha("Nova Senha");
item.setUsuario("Fulano");
item.setNumeroSerial(67890);
System.out.println(item);
System.out.println("Gravando Objeto");
FileUtilities.escreva("itemArq", item);
System.out.println("Finalizado");
}
}
Temosnaclasseométodo main()porondeiremosiniciaraexecuçãodo
código.OprogramacriaumobjetonovodotipoItemeéimpressonocon-
soleoobjetocriadocomosvaloresinicializadospeloconstrutor.Emseguida
alteramososvaloresdasvariáveiseimprimimosnovamnetenoconsole.Por
fim,realizamosagravaçãodoobjetoparaoarquivochamado itemArqe,
paraissoutilizamosométodo escreva()quecriamosanteriormentena
classe FileUtilities.
Aexecuçãodaclasse CriaItemgeraaseguintesaídanoconsole:
Criando Objeto
Item: numeroSequencia=1415361296961, usuario=Nenhum,
matricula=1415361296961, senha=Nenhuma
Alterando Valores
Item: numeroSequencia=67890, usuario=Fulano, matricula=123456,
senha=Nova Senha
Gravando Objeto
Finalizado
63

## Página 68

3.5. EscrevendoXML CasadoCódigo
Agora, precisamosrecuperarosdadosgravados. Serácriadaaclasse
RecuperaItemconformelistagemaseguir.
Listagem 3.8 - Classe qeu lê um item do arquivo e imprime seus dados
noconsole:
public class RecuperaItem {
public static void main(String[] args) {
System.out.println("Recuperando Objeto");
Item item = FileUtilities.leia("itemArq");
System.out.println("Apresentando Valores");
System.out.println(item);
}
}
Tambémtemosnaclasse RecuperaItemométodo main()poronde
iremosiniciaraexecuçãodocódigo.Oprogramadeclaraumareferênciado
tipoItemeutilizaométodo leia()daclasse FileUtilitiesparaob-
terumobjetodestetipo.Estaclasseiráseencarregarderealizaraleiturado
arquivo itemArq,passadocomoparâmetro,ederetornarumobjetorecons-
tituídoapartirdosdadoslidos.Aseguirimprimimosnoconsoleosdadosdo
objetorestaurado.
NaexecuçãodaclasseRecuperaItem,teremosalgocomoapresentadoa
seguir:
Recuperando Objeto
Apresentando Valores
Item: numeroSequencia=0, usuario=Fulano, matricula=123456,
senha=null
Então,comopodemosver,osvaloresdeatributosestáticosedeatributos
marcadoscom transientnãosãoserializadoseaorecuperaroobjetose-
rializadoelesassumemvalores-padrão(nullparaobjetose0paranúmeros).
3.5 E screvendo XML
Uma funcionalidade interessante acrescentada no Java 2 SE 1.4 foi a
possibilidadedeserializarobjetosemformatoXML.Parafazerisso, uti-
64

## Página 69

CasadoCódigo Capítulo3. Serializaçãodeobjetos:damemóriaparaodisco
lizamos as classesXMLEncodere XMLDecoder. Vamos utilizar nossa
classePessoacriadanocome çodesteartigoegravá-laemformatoXML.O
códigodaclasse EscrevePessoaXMLestáapresentadonalistagemaseguir.
Listagem 3.9-ExemplodeserializaçãoemXML:
import java.beans.XMLEncoder;
import java.io.FileOutputStream;
import java.io.IOException;
public class EscrevePessoaXML {
public static void main(String[] args) {
Pessoa pessoa = new Pessoa();
pessoa.setNome("Leandro");
pessoa.setSobrenome("Yung");
pessoa.setTelefone("3743-xxxx");
System.out.println("Gravando como XML");
try {
FileOutputStream fout =
new FileOutputStream("Pessoa.xml");
XMLEncoder xe = new XMLEncoder(fout);
xe.writeObject(pessoa);
xe.close();
fout.close();
} catch (IOException e) {
e.printStackTrace();
}
System.out.println("Ok");
}
}
Inicialmente,criamosumobjeto Pessoaqueiremosserializareabrimos
umfluxodesaídaparaarquivoapontandoparaoarquivo Pessoa.xml.Em
seguida,criamosumfluxodesaídaXMLsobreofluxodesaídaparaarquivo.
Porfim,escrevemosparaofluxodesaídaXMLoobjetopessoacriado.
AbrindooarquivoXMLgerado,eledeverápossuiraseguinteestrutura:
65

## Página 70

3.6. ConsideraçõesFinais CasadoCódigo
Listagem 3.10-XMLgeradopelaserialização:
<?xml version="1.0" encoding="UTF-8"?>
<java version="1.8.0" class="java.beans.XMLDecoder">
<object class="Pessoa">
<void property="nome">
<string>Leandro</string>
</void>
<void property="sobrenome">
<string>Yung</string>
</void>
<void property="telefone">
<string>3743-xxxx</string>
</void>
</object>
</java>
3.6 C onsiderações Finais
Osfundamentosdeserializaçãosãobastantesimples,porémsãoimportantes
paratecnologiasmaisavan çadas.Oprocessoémuitoimportanteparaconver-
terumaestruturaemmemóriaemdadosfacilmentearmazenáveisetranspor-
táveis,poressemotivo,vastamenteutilizadoemmecanismosdepersistência,
armazenamentoetransporte.
Paraoleitor,ospróximospassosseriamestudaroutrosaspectosdaseri-
alização,taiscomoonúmeroserial,personalizaç ãodoprocessodeleiturae
gravaçãoeousoparaenviodedadosnocontextodaprogramaç ãodistribuída.
3.7 R eferências
•TheJavaProgrammingLanguage, ThirdEdition-KeNArnold/James
Gosling/DavidHolmes
• Java Tutorial – Lesson I/O:http://docs.oracle.com/javase/tutorial/
essential/io/index.html
66