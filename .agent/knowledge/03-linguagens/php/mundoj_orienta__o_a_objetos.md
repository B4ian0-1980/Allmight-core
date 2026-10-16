---json
{
  "id": "mundoj_orienta__o_a_objetos",
  "title": "MundoJ Orientação a Objetos",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "**Arquivo Original:** `MundoJ Orientação a Objetos.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "linguagens",
    "mundoj",
    "objetos",
    "orienta",
    "php"
  ],
  "perguntas_tipo": [
    "Como utilizar MundoJ Orientação a Objetos?",
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

# MundoJ Orientação a Objetos

> **Arquivo Original:** `MundoJ Orientação a Objetos.pdf`
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
1 CriandoSoftwaremaisPróximoaoClientecomDomainDriven
Design 1
1.1 DomaineUbiquitousLanguage . . . . . . . . . . . . . . . . . 2
1.2 ConstruçãodoDomainModel . . . . . . . . . . . . . . . . . . 2
1.3 ImplementandooDomainModel . . . . . . . . . . . . . . . . 3
1.4 DDD(quase)naprática . . . . . . . . . . . . . . . . . . . . . . 4
1.5 Implementar . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
1.6 Repositórios,DAOs,Layersemuitaconfusão . . . . . . . . . 8
1.7 ConsideraçõesFinais . . . . . . . . . . . . . . . . . . . . . . . 10
1.8 Referências. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2 ProjetandoeCodificandoumaDSLInterna 13
2.1 Exemplo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
2.2 BoasOportunidadesParaoUso . . . . . . . . . . . . . . . . . 23
2.3 Desvantagens . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
2.4 Persistência. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
2.5 Consideraçõesfinais. . . . . . . . . . . . . . . . . . . . . . . . 25
2.6 Referências. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
3 MelhoriaContínuadoCódigocomRefatoraç ão 27
3.1 OqueéRefatoração? . . . . . . . . . . . . . . . . . . . . . . . 28
3.2 Arefatoraçãonodia-a-dia . . . . . . . . . . . . . . . . . . . . 30
3.3 RefatoraçãoeExtremeProgramming(XP) . . . . . . . . . . . 35
i

## Página 4

Sumário CasadoCódigo
3.4 Exemploderefatoração . . . . . . . . . . . . . . . . . . . . . . 36
3.5 Cuidadosparaaplicarasrefatorações . . . . . . . . . . . . . . 51
3.6 Consideraçõesfinais. . . . . . . . . . . . . . . . . . . . . . . . 55
3.7 Referências. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
4 OsPrincípiosdaModelagemÁgil 57
4.1 Paraodesenvolvimentodesoftware,nãoexisteseparaç ãoen-
tredesigneconstrução . . . . . . . . . . . . . . . . . . . . . . 59
4.2 Desenvolvimentodesoftware:humanasouexatas? . . . . . . 61
4.3 Acomunicaçãoricado“papelsobreamesa”. . . . . . . . . . 62
4.4 Rascunhos:umaformademodelagemeficaz . . . . . . . . . 63
4.5 Rascunhosparaobterqualidadeexternanosoftware . . . . . 65
4.6 AprofundaremdetalhesantecipadamenteéRUIM! . . . . . 67
4.7 Nãovolteparacasaparaescreverdocumentosderequisitos! 70
4.8 Utilizandoamodelagemparaobterqualidadeinterna . . . . 71
4.9 Conceitossempreprovadoscomcódigo . . . . . . . . . . . . 75
4.10 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
4.11 Referências. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76
ii

## Página 5

Capítulo1
CriandoSoftwaremaisPróximo
aoClientecomDomainDriven
Design
“”
–porSérgioLopes
Domain-DrivenDesigncaiunabocadopovo.Quemnavegaporfórunse
listasdediscussãosobreJavajápercebeuointeressequeDDDtemdespertado
naspessoas(aquinaCaelummesmotemosaltasdiscussõessobreoassunto).
E,juntocomtodaessaaten ção,tambémaparecemmuitasdúvidaseidéias
erradas.
Oobjetivodesteartigoéserumaintroduç ãoà Domain-DrivenDesign

## Página 6

1.1. DomaineUbiquitousLanguage CasadoCódigo
(DDD),mostrarsuasprincipaisidéiaseprovocardiscussõesemtornodeste
tematãopolêmico.
1.1 Domain eUbiquitousLanguage
OpontofundamentaldoDDDéoprimeiroD,o Domain. Tudogiraem
tornodessetaldeDomínio. Odomínioé,empoucaspalavras,oproblema
quequeremosresolvercomoprogramaqueestamosdesenvolvendo.Alguém
(umcliente)temumproblemanaáreadeatuaçãodele(geralmentenadaaver
cominformática)econtrataumaequipedeprogramaçãoparaajudá-lo(nós!).
SegundooDDD,é impossívelresolveresseproblemasatisfatoriamente
sementenderdireitooqueacontecenodomíniodocliente.Nãobastaosde-
senvolvedoressaberemmaisoumenos:énecessárioentrarfundonodomínio
docliente.
Mas,éclaroquenossoobjetivonãoénostornarmosespecialistascomple-
tosnaáreadocliente,masapenascompreendê-la.Apalavra-chaveparaisso
aconteceréConversa.Conversaconstanteeprofundaentreosespecialistas
dedomínioeosdesenvolvedores.
Aquelesqueconhecemodomínioemdetalhesdevemconversarcom
aquelesqueconhecemprogramaçãoemdetalhes. Juntos,tentarãochegara
umalínguacomumemquetodosconsigamseentenderequeseráusadaem
todasasconversas. ÉoqueoDDDchamade UbiquitousLanguage(UL):
umalínguabaseadanostermosdodomínio,nãototalmenteaprofundada
neste,massuficienteparadescreveroproblemasatisfatoriamente.
1.2 Construção do Domain Model
Duranteaconversaconstante,todosjuntoschegarãoaumconsensosobreo
Domínio.Osespecialistasdedomínio,eventualmente,criarãosimplificações
parafacilitaraconversa;eosdesenvolvedorespodemintroduzirconceitos
técnicossimples.
Comisso,todoscriamum modelododomínio,o DomainModel. Para
oDDD,éumaabstraçãodoproblemareal,desenvolvidaemparceriapelos
especialistasdodomínioedesenvolvedores.
2

## Página 7

CasadoCódigo Capítulo1. CriandoSoftwaremaisPróximoaoClientecomDomain...
SegundooDDD, éessemodeloqueosdesenvolvedoresvãoimplemen-
taremcódigo. Literalmente. Itemporitem,comofoiacordadoportodos.
Serádesenvolvidoumcódigolimpo,compalavrasdodomínio,querepre-
senta,naprogramação,odomínioemdiscussão.
UsandoDDD,seuprogramaorientadoaobjetosdeveexpressarariqueza
dodomainmodel. Qualquermudan çanomodelo(e,acredite,issoémuito
comum)deveserrefletidaimediatamentenocódigo. Sealgodomodelo
torna-seinviáveldeseimplementartecnicamente,nãosefazum“ajustezinho”
nocódigo;omodelodevesermudadoparasermaisfácildeseimplementar.
Ouseja,noDDD, sempreseucódigoseráexpressãodomodelo,que,
porsuavez,ébaseadototalmentenodomínio.
1.3 Implementando o Domain Model
Escrevercódigoeleganteéumdosmaioresdesafiosqueosprogramadores
enfrentam. Simplesmenteescreverporescrever,qualquerferramentazinha
quegerecódigoconseguefazer.Masescreverbonscódigos,legíveis,flexíveis
ericoséorealdesafio.
ODDDdefineumasériededesignpatternsparafacilitaraimplemen-
taçãodomodeloemcódigo.Comoqualquerdesignpattern,éumaidéiade
comocodificarcertosproblemascomunsdeformaelegante.
Mas,percebaqueoobjetivodeumdesignpatternéajudaroprograma-
dor! EoprincipalparaoDDD,comovimos,éoDomain. Ospatternssão,
portanto,apenasferramentasquefacilitamaimplementaçãodoDomainMo-
delnocódigo. Mas,comabsolutacerteza,essenãoéopontoprincipaldo
DDD.
Observocomfreq üênciainfindáveisdiscussõesemtornodepatternsdo
DDD,ondesurgemreceitasmágicasqueaparentementepodemseraplicadas
emqualquerprojetoepronto,temosDDD.Esseéumdosmaioreserrosque
sepodecometer.
Nãoexistereceitapronta,nãoexistecertoouerradoaoescreversuasclas-
ses.SequerusarDDD,lembre-sedoprincipal: oDomain.Vocêpodecriar
umModelriquíssimoeumcódigomuitobemescrito;masseelenãofor
expressãodoDomain,senãoforapartirdalínguacomum,vocênãoestá
3

## Página 8

1.4. DDD(quase)naprática CasadoCódigo
usandoDDD.
Reparequenãosoucontrárioaospatterns,muitopelocontrário.Sãoex-
tremamenteúteisparaoprogramador,abremacabe çaparasoluçõesquenor-
malmentenosatormentamecriamumapadronizaçãonasferramentasdodia
adiadodesenvolvedor.CriticoaquiquemencaraoDDDcomoumconjunto
depatterns.Nãoé,eestálongedisso.
1.4 DDD(quase) na prática
Domain-DrivenDesignéentãosobreoDomain.Sobretodosconversarema
respeitododomínio.Sobreacriaçãodeumalínguacomumentredesenvolve-
doreseespecialistasdedomínio.Então,parausarDDD,temosqueconversar
muito!Calma,caroleitor,nãoofareiconversarcomarevista.Maspodemos
tentarsimularalgo.
AConversa
Imaginequesomosaequipededesenvolvedorescontratadaporalguém
interessadoemmontarumalojadepeixes.Evamostodosláconversar:
•Desenvolvedor: Boa tarde, eu sou programador Java certificado
SC#@$.
•Cliente: Boatarde,masnãoerabemissoqueeuprecisava... queria
alguémpradesenvolverumsistemapramim.
•Desenvolvedor: Ops,desculpe.Eusouumdesenvolvedor.Essascoisas
queeufaleisãodetalhesquenãointeressammesmo.
•Cliente: Ótimo!Bom,meunomeéMr.SellFishequeroabrirumaloja
quevendepeixesquetenhoaquinomeulago.
•Desenvolvedor: Certo...LojadePeixes...tipoumpeixe-espada?
•Cliente: Não. Peixe-espadaéumtriquiurídeo,deáguasalgada. Eu
vendopeixesdomeulago,águadoce.Tenholambaris,carpas,tamba-
quis,tilápiaseoutrosciclídeos.
4

## Página 9

CasadoCódigo Capítulo1. CriandoSoftwaremaisPróximoaoClientecomDomain...
•Desenvolvedor: ????
•Cliente: Deixe-mesimplificar:tenhováriospeixes,cadaumdeuma
espéciediferente.
•Desenvolvedor: Ahsim.Váriospeixes,váriasespécies,cadapeixeéde
umaespécie...Háoutrasinformaçõesimportantessobrecadapeixe?
•Cliente: Comcerteza!Aquinossospeixestêmumnomedebatismo,a
idadedeleepossuemcoresdiferentestambém.
•Desenvolvedor: Humm...vejameudesenho:
•Cliente: Interessante.OtraçosignificaqueoPeixetemumaespécie,
certo?Masqueraiosé“id”?
•Desenvolvedor: Éumcódigoúnicoqueprecisoparacadacoisanosis-
tema,coisasdacomputação.Vouchamarde“código”prafacilitarnosso
entendimento.
•Cliente: Ótimo! Vouprecisarcadastrartodososmeuspeixesesuas
espécies.Querofazerumalojadiferentecheiaderecursosparaocliente
encontraropeixecertopraele.
5

## Página 10

1.4. DDD(quase)naprática CasadoCódigo
•Desenvolvedor: Entãooclienteteráalgumasbuscasavan çadas...quais
seriamimportantes?
•Cliente: Querosaberquaispeixessãodeumadeterminadaespécie
oudeumadeterminadacor,buscarpeixespelonomeetalvezoutras
coisas.
•Desenvolvedor: Vejamos:
•Cliente: Muitobom! Achoqueestouentendendo... Mascomovou
buscarpelonomemesmo?
•Desenvolvedor: Ahsim...Bom,naverdadevocêprecisaé,dadotodos
ospeixesdisponíveis,saberquemtemdeterminadonome.Eupreciso
entãoprocuraressespeixesemalgumlugar...possochamaresselugar
deRepositóriodePeixes?
•Cliente: Repositório?Podesim...Umrepositórioentãoéondeestão
todosospeixes,certo? E,porlá,euconsigosaberqualPeixetemtal
nome?
•Desenvolvedor: Isso!
6

## Página 11

CasadoCódigo Capítulo1. CriandoSoftwaremaisPróximoaoClientecomDomain...
AnalisandoaConversa
Obviamenteaconversaquevocêleuagorasooubastanteartificial. Mas
umaconversarealcomoclientenãodevefugirmuitodisso.Devesersimples
egiraremtornododomínio.Algumasliçõesquequerodestacar.
Evitecolocarnaconversatermostécnicosdesnecessários.Efaç aoespe-
cialistadodomínioevitarcolocardetalhesmuitoespecíficosdodomíniona
conversa.
Mastomemuitocuidadoparanãoabstrairdemaisaconversaeacabar
fugindodoprincipal,odomínio.Sevocêvaiprecisarentenderqueciclídeos
sãopeixesdeáguadoce,aprendaisso. Masnãopermitaquesejamcriadas
simplificaçõesaoextremoquefaçamcomqueaconversafujadodomínio
real.
Mesmacoisaparatermostécnicosentraremnaconversa.Sevocê,desen-
volvedor,consideraqueéprecisoumrepositórionosistema,faç aoespecia-
listadenegócioconcordarcomvocêeintroduzaoconceitoaele.
Aconversadeveterumalínguacomum,aUbiquitousLanguage.Eessa
línguatemqueseropontodeencontrodosdesenvolvedorescomosespeci-
alistasdedomínio.Sealguémnãoconcordacomalgumtermoouachaque
determinadotermotemquefazerpartedaUL,issodeveserconversado.
Tudoissoporque,depois,seucódigodeveserexatamenteaquiloquefoi
7

## Página 12

1.5. Implementar CasadoCódigo
conversado.AprogramaçãodeveserexpressãodaUL.Jamaisprogramecó-
digoscomconceitosquenãofazempartedaUL.
1.5 Implementar
Oobjetivodesseartigonãoéentraremdetalhesdeimplementaç ão,maspo-
deríamosesboçaralgumcódigocombasenoDomainModel. E,paraisso,
podemosusaralgunsdesignpatternspropostosporEricEvans,autordoli-
vroDomainDrivenDesign,principalreferênciasobreoassunto.
Teríamosasclasses Peixee Especiequeseguemopadrão Entity.
Resumidamente,sãoobjetoscomidentidadeecomciclodevidaqueque-
remoscontrolar. Aclasse Corsegueopadrão ValueObject. Éumobjeto
geralmenteimutávelondeoquerealmenteinteressaéovalordele(nãohá
identidade,doisobjetoscommesmovalorsãoiguais).
Quantoàsentidadesdosistema,frequentementeestamosinteressadosem
controlarseuciclodevidabemdeperto.Criamosváriosobjetosqueprecisam
serarmazenadosemalgumlugarseguro,etodahoraprecisamosrecuperar
essesobjetosbuscando-osdasmaisvariadasformas. Opadrão Repository
representa,noDomainModel,olugarondejogamosobjetosedepoisospe-
gamosdevolta(maissobreRepositorynapróximase ção).
Hámuitosoutrospadrões(Service, Aggregate,etc),muitasformasde
integrá-losedetalhesdeimplementaçãoquefogemdoescopodesseartigo.
Paramaioraprofundamento,recomendooestudodasreferênciasapresenta-
dasaofinaldoartigo.
1.6 Repositórios,DAO s,L ayers e muita confu-
são
Todomundoquecome çaaaprenderorientaçãoaobjetosdecentementelogo
aprendeoqueéencapsulamento.Etodomundoquecome çaaaprenderausar
bancosdedadoscom,porexemplo,Java,aprendeofamosopadrão DAO–
DataAccessObject.
ContampragentequeoDAOéumaboapráticadeprogramaç ãopois
serveparaencapsularasparticularidadesdoacessoabancodedados(oualgo
8

## Página 13

CasadoCódigo Capítulo1. CriandoSoftwaremaisPróximoaoClientecomDomain...
dogênero)eisolaressacomplexidadedorestantedoprograma. Aidéiaé
deixarapartefeiadacoisaencapsuladanoDAOetodoorestodoprograma
usaobjetosbonitinhossemnemteridéiadoqueacontecenobanco.
Agora,chegaalguémdizendoqueexisteumtalde repositórioquerepre-
sentaolugarondenossosobjetossãocolocadosparaquedepoispossamos
recuperá-los. E,infelizmente,nacabeçademuitagente,conclui-sequeRe-
positórioeDAOsãoamesmacoisa. Nãosão,emboraeuconcordequeisso
tudopossagerarmuitaconfusão.
ODDD(eoutraspessoastambém)propõequedesenvolvamosnosso
softwaredividoemcamadas(layers)parafavorecerencapsulamento,flexibi-
lidadeemuitasoutrascoisasboas.Evans,emparticular,propõeadivisãoem
4camadasprincipais: PresentationLayer,ApplicationLayer,DomainLayere
InfrastructureLayer.
AhistóriatodadeDDDestá,obviamente,focadaexclusivamentena Do-
mainLayer.ÉondevocêvaiimplementaroDomainModel,escreverocó-
digoquerepresentaoDomainetudoaquiloquediscutimos.Mas,nóssabe-
mosque,algumahora,vamosprecisardecoisasforadoDomain(umHTML
pramostraramensagemprousuário,umSQLprafazerumabusca,umexe-
cutenumaActiondoStruts,...).Porissoexistemasoutrascamadas.
EscreverSQLecódigodemanipulaçãodebancodedadosnãofazparteda
DomainLayer(amenosqueseudomíniosejabancosdedados).Tudoissofaz
partedacamadadeinfraestrutura,lugarondeseuDAOdeveestar.Perceba
que,usandoDDDounão,éboapráticateroDAO;masoDDDmesmonão
diznadasobreisso,jáqueeleestáforadoDomain.
RepositórioéumconceitodoDomainLayer,temquefazerpartedoDo-
mínio. Percebaadiferença: DAOsurgedoproblemadeencapsularcoisas
feiasdeinfra-estrutura;Repositóriosurgedanecessidadedoclientedeobter
objetosdodomínio.Oclientenãotemidéiadebancodedados,nãosabeo
queéSQL.
Onomerepositórionãodeveseralgointernoaocódigo,mas devefazer
partedaUbiquitousLanguage,deveaparecernasconversasenoDomain
Model.Ouseja,repositóriodeveserumconceitoqueoespecialistadedomí-
niotambémentendee,porqueestánoModel,éelequevaiparaocódigo.
NãoháproblemaemtrazerpalavriadotécnicoparaaUbiquitousLan-
9

## Página 14

1.7. ConsideraçõesFinais CasadoCódigo
guage,desdequeopríncipiodaULsejamantida:todosentendemoconceito.
E,se,eventualmente,nocontextododomíniosendotratado,outronomefaç a
maissentidoquerepositório,essenome deveserusado(mesmoquenós,téc-
nicos,saibamosque,nofundo,aquiloéumRepository).Mas,claro,onome
DAOnãofazpartedaUL.
Entendidaadiferen çaentreDAOeRepositoryficaadúvida:comoim-
plementarumRepositório? ExistesimalgumarelaçãoentreRepositóriose
DAOs,vistoquegeralmenteasbuscasdoclientesãofeitasnoBancodeDa-
dos. Masascoisas,comovimos,estãoemlayersdiferentes. Háváriasim-
plementaçõespossíveis(enenhumaregramágicafixa),todasboassegundoo
DDDdesdequesigamososconceitosdiscutidos.
Sóparaexemplificar:eugostoderepresentaroRepositórionacamadado
domínioatravésdeumainterfaceJava.Paracasosmaissimples,implemento
ainterfacediretonoDAOnacamadadeinfraestrutura;emcasosmaiscom-
plexos,meurepositóriopodeserumaclasseconcretaquedelegacoisaspro
DAOdainfraestrutura.AquinaCaelummesmousamosabordagensdiferen-
tesdependendodasituação.
Maslembre-se:issonãoéregra!Desenvolvapensandonodomínioete-
mosDDD.
1.7 Considerações Finais
Domain-DrivenDesigntentatrazermaisqualidadeparaodesenvolvimento
desoftware,tantoparaoprocessodedesenvolvimentoquantoparaoproduto
final. E,paraisso,partedoprincípiodequeosoftwaredeveseguirarisca
idéiasdodomínioparaoqualelefoidesenvolvido.
1.8 Referências
• EVANS,Eric.Domain-DrivenDesign:TacklingComplexityintheHe-
artofSoftware.EditoraAddison-Wesley.
• www.domaindrivendesign.org
• Domain-DrivenQuickly. LivrogratuitodaInfoQ:http://www.infoq.
com/minibooks/domain-driven-design-quickly
10

## Página 15

CasadoCódigo Capítulo1. CriandoSoftwaremaisPróximoaoClientecomDomain...
• BlogdaCaelum:http://blog.caelum.com.br
11

## Página 17

Capítulo2
ProjetandoeCodificandouma
DSLInterna
“Osconceitosdedomain-specificlanguage(DSL)estãoficandocadavezmais
próximosdosdesenvolvedores,emboraatualmenteexistampouquíssimasboas
referências.UmaótimareferênciaéonovolivrodeMartinFowler,ondeo
autortrataoassuntodividindo-oemdoisramos,DSLinternaeexterna.Este
artigoiráexploraracria çãodeumaDSLinternautilizandoalinguagemJava.”
–porLeandroRibeiroMoreira
Asempresasdesejamqueasmudan çasnosnegóciossejamcadavezmais
hábeis,logoossistemasdeinformaçãodevemacompanharessatendência
namesmaintensidade.Criarsoftwaredequalidadeexigebonsprofissionais,
atualmentealguns“gurus”daáreaestãonotandoquedevemmanterofoco
dodesenvolvimentonoscomponentesrelacionadosaodomínio,paraassim

## Página 18

CasadoCódigo
obtersistemasflexíveis. Odomíniocomoocentrodaaplicaç ãoéumadas
práticasaconselhadasdomodoDDDdesecriarsistemas.Vistoaatualten-
dênciadesevalorizarodomínioaomáximo,oassuntoDSL(quejáéantigo)
voltaatonacomnovosares. Normalmentequandofazemosumaprimeira
leiturasobreDSLpensamosqueéalgoaindaintangível,porémnemchega-
mosaperceberqueomundodossoftwaresestárepletodeDSLs,como,por
exemplo,hamcrest,jmock,hibernatecriteriaejodatime.Ossistemasopera-
cionaisbaseadosnoUNIXtêmumagamamuitograndedeDSLs,como,por
exemplo,algunsformatosdearquivosdeconfiguração.UmaDSLéumalin-
guagemvoltadaparaumdomínioespecificodiferentementedaslinguagens
deprogramaçãotradicionais,comoJava,C#,Rubyeoutrasquesãodeuso
geral.OspesquisadoresclassificamaDSLemdoistipos:internaeexterna.
UmaDSLinternapodeserdefinidacomoumestilodesecodificarAPIs
quesejammaisricasemexpressividadeparaumdomínioespecifico,quepos-
samatémesmogerarexpressõeslegíveisaalguémquenãosaibanadasobre
Java,masquetenhaexperiêncianodomínioemquestão.Criarumalingua-
gemcomumquesejacompreensíveltantoaoexpertdodomínioquantoaos
desenvolvedores,ouseja,umaubiquitouslanguage,podeajudarmuitoode-
senvolvimentodeumaDSL.Porserumassuntonovoàmuitosdesenvolve-
dores,háconfusãodosconceitos,ealgunsacreditamatéqueDSLinternae
externasãosinônimos.Osprópriospesquisadoresdoassuntoàsvezesentram
emcontradição.Porexemplo,paraalgunsumaDSLinternaeumainterface
fluentesãosinônimosjáparaoutrosháalgumasdiferen ças. Háváriospa-
drõesparaseescreverumaDSLinterna.Normalmente,opadrãomaisusado
naconstruçãodeDSLinternaséomethodchainning,esteoferecemeiospara
queosobjetosfaçamchamadasemsequênciaaprópriainstanciadoobjeto.É
importantenotarque,devidoaofatodasDSLsinternasseremescritassobre
umalinguagemdeprogramação(aqualsedenominalinguagemhospedeira),
elassofremasmesmaslimitaçõesdalinguagememqueforamescritas.
14

## Página 19

CasadoCódigo Capítulo2. ProjetandoeCodificandoumaDSLInterna
InterfaceFluente
No ano de 2005, Martin Fowler e Eric Evans estavam em um
Workshopconversandoarespeitodeumestilodeinterface,osdoisre-
solveramnomearessedeinterfacefluente.Maistarde,porvoltadoano
de2007,Fowlerafirmouque,daperspectivadeAPI,vêumainterface
fluentecomosinônimodeDSLinterna.
2.1 Exemplo
Esteartigoirádemonstraracriaç ãodeumaDSLinternanaprática,para
acompanhar-lobastaterinstaladooJDK6,ousodeumIDEpodeauxiliarna
codificação.ParafacilitaracriaçãodeumaDSLinternaémaisfácilescrever
primeiroaAPI,paradepoisverificaraviabilidadedeimplementaç ão.
Oexemplotrabalhadotratarádodomíniodevídeolocadoras.Pelofatode
queescreveralgocomplexogastariamuitotempo,oexemploébemreduzido
eabstraimaioresdificuldades.Oprocessodelocaç ãodevídeosésimples:o
clientevaiàlocadora,escolheosvídeos,sedirigeaobalcãoparaconcretizar
alocação,ocaixasolicitaaidentificaç ãodapessoa,registravídeoavídeo,
perguntaseopagamentoserárealizadonaentregaounomomentodaloca-
ção,ocaixainformaemqualdatadeverãoserentreguesosvídeoseentregao
comprovantedelocaçãoparaocliente.
Paracome çar, crieaclassequeiráutilizaraDSLinterna, essaclasse
sechamaráTestadoraeterá, inicialmente, ométodo main(), conforme
listagemaseguir.
Listagem2.1-Pré-implementaçãodaclasseconsumidora.:
package br.com.mundojava.DSLinterna;
public class Testadora{
public static void main(String[] args){
}
}
15

## Página 20

2.1. Exemplo CasadoCódigo
Partindodadescriçãodecomofuncionaoprocessodelocaç ão,imple-
menteumapequenapartequerepresenteomomentoemqueoclientese
identifica.Insira-adentrodométodomaindalistagemanterior.
Cliente paulo = new Cliente(“19784567892”,”Paulo”);
Locacao locacao = Locacao.para(paulo);
Notequeométodo para(),daclasse Locacao,implementaopadrão
FactoryMethod comumnomenãomuitocomum,masdealtalegibilidade.
Seguindoadescrição,ocaixaregistravídeoavídeoeperguntaaoclientepara
quandoseráopagamento.Estetrechopodeserdescritodaseguinteforma:
locacao.adicionar(tropaDeElite, osSimpsons, vanillaSky)
.paraDevolver(daquiA(DOIS_DIAS)).aPagar();
Nasimplesinstruçãodocódigoestásendofeitoasolicitaç ãodoregistro
deumalocaçãodetrêsfilmesparaseremdevolvidosemdoisdiasecompa-
gamentoagendadoparaomomentodaentrega.Percebaqueseocódigofosse
mostradoaumexpertdalocadora,provavelmenteeleentenderiaointuitodo
mesmo.Depoisderegistradaalocação,umcupoméimpressoeentregueao
cliente.Ocódigoquepoderiasintetizaressemomentoseriasimplesmente:
GerenciadorLocadora.imprimir(locacao);
Ocódigoparcial,usadonaclasseconsumidoradessaDSL,éapresentado
nalistagemaseguir.
Listagem2.2-Implementaçãoparcialdaclasseconsumidora.:
package br.com.mundojava.DSLinterna;
public class Testadora{
public static void main(String[] args){
Cliente paulo = new Cliente(“19784567892”,”Paulo”);
Locacao locacao = Locacao.para(paulo);
locacao.adicionar(tropaDeElite, osSimpsons, vanillaSky)
.paraDevolver(daquiA(DOIS_DIAS))
.aPagar();
GerenciadorLocadora.imprimir(locacao);
16

## Página 21

CasadoCódigo Capítulo2. ProjetandoeCodificandoumaDSLInterna
}
}
AtéomomentosófoiescritaaAPI,semnenhumcódigoqueaimple-
mente. PodeserdegrandeajudatentarcodificarumaDSLinternaapartir
daperspectivadeseuuso,quereflitaomaispróximopossíveldodomínio.
Agoraparaimplementarocódigo,crieumaclassechamada Cliente,que
possuaumconstrutoredoisatributos: nomee cpf. Ocódigofontepode
servisualizadonalistagemaseguir.
Listagem2.3-Implementaçãodaclassecliente.:
package br.com.mundojava.DSLinterna;
public class Cliente{
private String cpf;
private String nome;
public Cliente(String cpf, String nome){
this.cpf = cpf;
this.nome = nome;
}
//getters omitidos
}
Opróximopassoéimplementaraclasse Locacao,aclassequetemum
métodofábricanomeadopara(),erecebeumobjeto Clientecomoparâ-
metroedevolveumainstânciadesi.Ométodo adicionar()seaproveita
dafuncionalidadevarargsdoJavaerecebeumouváriosvídeos. Ométodo
paraDevolverEm()recebeumadataquerepresentaadatadedevoluç ão
dovídeo.Hámaisdoismétodos,um jaPago()eoutro aPagar(),queex-
pressamasituaçãodopagamentodalocação.Afigura 2.1mostraodiagrama
declasseealistagemaseguirdemonstraocódigo.
17

## Página 22

2.1. Exemplo CasadoCódigo
Fig.2.1:Diagramadeclasses
Listagem2.4-ImplementaçãoparcialdaclasseLocacao.:
package br.com.mundojava.DSLinterna;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
public class Locacao{
private Cliente cliente;
private List<Video> relacaoVideo = new ArrayList<Video>();
private Date dataDevolucao;
private boolean pago;
private Locacao(Cliente cliente){
this.cliente = cliente;
}
public static Locacao para(Cliente cliente){
return new Locacao(cliente);
}
public Locacao adicionar(Video... videos){
for (Video vd : videos){
relacaoVideo.add(vd);
}
return this;
}
public Locacao paraDevolver (Date data){
18

## Página 23

CasadoCódigo Capítulo2. ProjetandoeCodificandoumaDSLInterna
dataDevolucao = data;
return this;
}
public Locacao aPagar(){
pago = false;
return this;
}
public Locacao jaPago(){
pago = true;
return this;
}
//getters omitidos
}
Naimplementaçãodaclasse Locacaoénotávelanecessidadedacriação
deoutrocomponente,aclasse Video. ParaoferecermaiorriquezaàDSL
interna,aclasse Videoseráprojetadamaispróximadadefiniçãodosexperts
emvídeo.Segueadescrição:umvídeotemumtitulooriginal,titulotraduzido,
umoumaisgêneros,atoresquecompõemoelencoeumpequenoresumo.
Comoanteriormente, inicia-seescrevendoaAPIparaposteriormente
implementa-la.
Video theSimpsonsMovie = new Video(“Os Simpsons”);
theSimpsonsMovie.nomeOriginal(“The Simpsons Movie”)
.com(“Homer,Marge, Lisa, Bart ...”)
.doGenero(“animação/comédia”)
.pequenoResumo(“A família mais queridado mundo agora " +
"em um longa-metragem...”);
Sefosseusadoomodotradicionaldesecodificar,aAPIficariaumpouco
diferente.
Video theSimpsonsMovie = new Video(“Os Simpsons”);
theSimpsonsMovie.setNomeOriginal(“The Simpsons Movie”);
theSimpsonsMovie.setAtores(“Homer,Marge, Lisa, Bart ...”);
theSimpsonsMovie.setGeneros(“animação/comédia”);
19

## Página 24

2.1. Exemplo CasadoCódigo
theSimpsonsMovie.setResumo(“A família mais queridado mundo " +
"agora em longa-metragem...”);
Ocódigodaclasse Videoéapresentadonalistagemaseguir.
Listagem2.5-ImplementaçãodaclasseVideo.:
package br.com.mundojava.DSLinterna;
public class Video{
private String nome;
private String nomeOriginal;
private String genero;
private String elenco;
private String sinopse;
public Video(String nome){
this.nome = nome;
}
public Video nomeOriginal(String nome){
this.nomeOriginal = nome;
return this;
}
public Video doGenero(String genero){
this.genero = genero;
return this;
}
public Video com(String elenco){
this.elenco = elenco;
return this;
}
public Video pequenoResumo(String resumo){
this.sinopse = resumo;
return this;
}
20

## Página 25

CasadoCódigo Capítulo2. ProjetandoeCodificandoumaDSLInterna
//getters omitidos
}
Voltandoàpropostainicial,insiraacriaçãodosfilmesnocódigo.
public static void main (String[] args){
Cliente paulo = new Cliente(“19784567892”,”Paulo”);
Locacao locacao = Locacao.para(paulo);
Video tropaDeElite = new Video(“Tropa de Elite”);
tropaDeElite.nomeOriginal(“Tropa de Elite”)
.doGenero(“ação/crime/drama”)
.com(“Wagner Moura,Caio Junqueira...”)
.pequenoResumo(“Filme retrata o trabalhodo B.O.P.E. "+
"em ação...”);
//a criação dos outros filmes omitida
locacao.adicionar(tropaDeElite, osSimpsons, vanillaSky)
.paraDevolver(daquiA(DOIS_DIAS))
.aPagar();
GerenciadorLocador.imprimir(locacao);
}
Notequeaindaháproblemasnãoresolvidos:aconstante DOIS_DIAS,o
método daquiA()eaclasse GerenciadorLocador,aindainexistemna
soluçãoatual.
Parasolucionaroproblemadaconstantebastacriaraclasse DataUtil
(apresentadanalistagemaseguir)eincluirum static import paraessa
classenaclasse Testadora.Issosolucionaráoprimeiroproblema.
import static br.com.mundojava.DSLinterna.DataUtil.*;
Listagem2.6-ImplementaçãodaclasseDataUtil.:
package br.com.mundojava.DSLinterna;
import java.util.Date;
21

## Página 26

2.1. Exemplo CasadoCódigo
public class DataUtil{
public static final int UM_DIA = 1;
public static final int DOIS_DIAS = 2;
public static final int TRES_DIAS = 3;
public static final int QUATRO_DIAS = 4;
public static Date daquiA(int dataMs){
dataMs = new Date().getDate() + dataMs;
Date data = new Date();
data.setDate(dataMs);
return data;
}
}
O segundo problema requer a criação de uma classe chamada
GerenciadorLocador. Essa classe deverá conter um método está-
ticochamado imprimir(),comopodeservistonalistagemaseguir.
Listagem2.7-ImplementaçãodaclasseGerenciadorLocador.:
package br.com.mundojava.DSLinterna;
public class GerenciadorLocador {
public static void imprimir(Locacao suaLocacao) {
System.out.println("Nome: " +
suaLocacao.getCliente().getNome());
for (Video mv : suaLocacao. getRelacaoVideo()){
System.out.println(mv.getNome() + " - " +
mv.getGenero());
}
System.out.println("Total: R$ " + suaLocacao.getTotal());
System.out.println("Devolver em " +
suaLocacao.getDataDevolucao());
System.out.println("Assinatura:________");
}
}
22

## Página 27

CasadoCódigo Capítulo2. ProjetandoeCodificandoumaDSLInterna
Paraummelhorresultadofoiimplementadoummétodo getTotal()
naclasse Locacao.
public String getTotal() {
if (!pago) {
int valor = this.relacaoVideo.size() * 2;
return valor + ",00";
} else {
return "0,00";
}
}
Otestefinalpodeserfeitoexecutandoaclasse Testadora.
Algumasmelhoriaspoderiamserfeitasutilizandoaclasse Calendar
aoinvésde Dateouelaborandoumasoluçãomaiseleganteparaclasse
DataUtil,porexemplo.
2.2 BoasOportunidades Para oUso
EsteartigodemonstraalgunsconceitosqueumaDSLinternadeveterecomo
implementá-loséumexemplorelativamentesimplesmascomaltovalordi-
dático.NormalmenteacriaçãodeumaDSLinternatrazmaisbenefíciospara
quemestádesenvolvendoumabibliotecaouframework,reduzindoacurva
deaprendizadodeseususuários.
Outrasituaçãoseriaodesenvolvimentodeumgrandesistema,ondevá-
riasequipessãoresponsáveisporsubprojetosdiferentes. Comumenteuma
determinadaequipeprecisaráusaralgumcomponenteouserviçoqueoutra
equipeestádesenvolvendo. Nessecaso,umaDSLinternapodeserumaso-
luçãointeressante. Porexemplo,aequipeAprecisasaberseumapessoajá
esteveounãodelicen çamédica.Noentanto,aequipeAestáengajadanuma
partedosistemaqueémaisrelacionadaaodomíniofinanceiro,seaequipe
B(responsávelpelodesenvolvimentodossistemasdesaúde)oferecesseuma
DSLinterna,aequipeAteriamenosdificuldadesparasoluç ãodoproblema.
boolean tirouLicenca = APIGestaoMedica.
funcionario(pedro).jaTirouLicenca();
23

## Página 28

2.3. Desvantagens CasadoCódigo
EmoutraocasiãoaequipeBprecisasaberadatadopagamentodeum
boletoquepertenceaumfuncionário,bastariaaequipeAfornecerumaDSL
interna.
Date dataPagamento = APIFinanceiro.
funcionario(pedro).pagou(boleto).quando();
Osexemplosforamsomenteparademonstraroquantoequipesdiferen-
tesemumgrandeprojetopodemsebeneficiardousodeDSLinternas. Se
vocêéusuáriodealgumframework,penseoquantoseriabomseotimede
desenvolvedoresoferecessealgumasDSLinternas,possivelmenteosusuários
teriamumaprendizadomaisrápidoeintuitivo.
2.3 Desv antagens
ComoaindahápoucaspessoaspesquisandoprofundamentesobreDSLs,
sabe-sepoucosobreoscontrasdousodeDSLinternas. Umadesvantagem
notáveléqueseucódigoorientadoaobjetosdevesofreralgumasmodifica-
ções“estranhas”,comoporexemplo,termétodosqueretorneminstanciade
simesmo.
Outropontonegativo,quantomaisexpressividadeaAPIfornecermaior
seráadificuldadedeseimplementaremanterocódigo,oqueébomparaos
clientesdaAPIpodeserumatormentaparaosdesenvolvedoresdamesma.
Nemsempreoretornodaprópriainstância(this)iráresolvertodosospro-
blemas,àsvezesénecessáriocriarobjetosintermediários,aumentandomais
adificuldadedaescritadaAPI.
2.4 Persistência
CriarumaDSLinternaemaplicaçõesondeoestadodosobjetosnecessitaser
persistidorequeracriaçãodeummecanismoparaquetaltarefasejafeita.
HáváriosmétodospararealizarapersistênciaemumaDSLinterna,serão
apresentadososdoisquesedestacampelasimplicidadeefacilidadedecom-
preensão.
Oprimeiromodoécriarummétodo persistir(),oqualdeveser
chamadoapósaconclusãodesolicitaç ãodeserviçosaDSLinterna.
24

## Página 29

CasadoCódigo Capítulo2. ProjetandoeCodificandoumaDSLInterna
locacao.adicionar(tropaDeElite)
.paraDevolver(daquiA(DOIS_DIAS))
.aPagar()
.persistir();
EstaprimeiraabordagemdeixaaDSLmenosrelacionadaaodomínio,o
quevaiaocontráriodopropósitoinicialdasDSLsinternas. Outrométodo
éencadearasmensagensaosobjetosdeformaquefaciliteapersistênciana
DSLsemqueoclienteperceba.
GerenciadorLocacao.imprimir(locacao.adicionar(tropaDeElite)
.paraDevolver(daquiA(DOIS_DIAS))
.aPagar());
Nométodoimprimir,querecebeumalocação,vocêpodepersistiroob-
jetosemqueissofiquetãoclaroparaoclientedaDSLinterna.
public static void imprimir(Locaca locacao){
//códigos para prover persistência e imprimir comprovante...
repositorioLocacao.adiciona(locacao);
}
2.5 Considerações finais
EnfimcriarumaDSLinternaésomentecriarmeiosparaqueaAPIsejamais
fácildeentendereusarnumcontextorestritoaumdomínioespecifico,tam-
béméimportantecitarqueaDSLnãoprecisaserlegívelaqualquerumesim
entendívelaumexpertdodomínio.Porsetratardeumaáreaaindaemes-
tudoeevoluçãotodoequalquercuidadosãopoucos,leréomelhorconselho,
obtenhainformaçõesdediversasfontes,facilitandoterumaposiç ãocritica
sobreoandamentodessesnovostermosquepoderãotomarcontadovoca-
bulário,jáextenso,dosdesenvolvedores.Existemdivergênciasdeopiniões,e
possivelmentesemprehaverá,entreospesquisadoresdoassuntoeosdesen-
volvedoresemgeral,maséessadiscussãoquefazcomqueoconhecimento
sejacompartilhado,analisado,criticadoeadotadooudescartado.
25

## Página 30

2.6. Referências CasadoCódigo
2.6 Referências
• Wikipédiahttp://en.wikipedia.org/wiki/Captcha
• JCaptchahttp://jcaptcha.sourceforge.net/
• SimpleCaptchahttp://simplecaptcha.sourceforge.net/
• Kaptchahttp://code.google.com/p/kaptcha/
• Configuração do Kaptcha http://code.google.com/p/kaptcha/wiki/
ConfigParameters
26

## Página 31

Capítulo3
MelhoriaContínuadoCódigo
comRefatoração
“Muitaspessoasacreditamqueamodelagemdeumaaplica çãoéuma
atividadequedevevirantesdasuaimplementa ção.Comessaidéia,a
modelagemeaestruturainternadaaplica çãonãoacompanhamsuaevolu ção
eacabamsetornandorapidamenteobsoletas.Oobjetivodesteartigoé
apresentaratécnicadarefatora ção,quepermitequeaatividadedemodelagem
aconteçadeformacontínuaeaqualidadedocódigosejasempreaprimorada.”
–porEduardoGuerra
Emumaabordagemclássicadeengenhariadesoftware,oprojetodasclas-
sesérealizadoantesdaimplementaç ão. Aaplicaçãodeváriospadrõesde
projetoéfeitadeformaaprocurarflexibilizaraestruturaomáximopossí-
vel.Depoisdoprojetofeito,osprogramadorespossuemafun çãodeapenas

## Página 32

3.1. OqueéRefatoração? CasadoCódigo
implementarosmétodosprevistosnodiagramadeclasse,baseadosnosdi-
agramasdesequênciaoucolaboração. Seforprecisoalteraralgoquetenha
impactonaformacomoosistemafoimodelado,osdiagramassãoalterados
eoprogramadorquesevireparaadaptarocódigoquejáestápronto. Isto
quandooprojetistajánão“saiudecena”eoprogramadorprecisadaraquele
“jeitinho”parainseriraquelenovorequisito.
Seráqueestaéamelhorformadesefazerascoisas?Seráquealguémjá
viuumprojetocomamodelagemtãopesadaquepareceestartentandomatar
umamoscacomumabazuca?Quejogueaprimeirapedraquemnuncaolhou
umcódigo,muitasvezesdesuaprópriaautoria,epensou:“Istonãoestáchei-
randomuitobem...”.Semfalarquandoosprogramadoresdecidemporconta
própriaqueamodelagemnãoestáboaeapartirdeumpontoignoramtodo
otrabalhoquefoifeito,come çandoamudarváriascoisasdeformadescon-
trolada,muitasvezesatéviolandoaarquiteturadosistema.
Sevocêseidentificoucomalgumdosproblemasacima,ficareimuitofe-
lizemteraoportunidadedelheapresentaratécnicadarefatoraç ão.Usara
refatoraçãonãosignificaquevocêprecisajogarforatodooconhecimentode
seuslivrossobreUMLepadrõesdeprojeto.Arefatoraç ãoéumaferramenta
poderosaquepodeserutilizadaemconjuntocomoutrastécnicasparaau-
mentarcadavezmaisaqualidadedocódigo.Comissoeleficamaisclaroe
limpo,fazendocomquemelhoriasnocódigoounamodelagempossamser
feitasdeformamaisseguraecontrolada.Oobjetivodesteartigoémostrar,
nateoriaenaprática,atécnicadarefatoraç ãoecomoelapodeserutilizada
namelhoriacontínuadeumprojetodesoftware.
3.1 O que éRefatoração?
SegundoMartinFowler,oautordolivro“Refatoração:AperfeiçoandooPro-
jetodeCódigoExistente”,arefatoraçãoéumatécnicademodificaçãodeum
softwaredeformaanãoalteraroseucomportamentoexternoemelhorarsua
estruturainterna,sendoumaformadisciplinadadeselimparocódigoque
minimizaaschancesdeintroduçãodebugs.
Destadefiniçãoumdosconceitosimportantesquepodeseretiraréanão-
alteraçãodocomportamentodocódigo.Nomomentoemqueserealizauma
28

## Página 33

CasadoCódigo Capítulo3. MelhoriaContínuadoCódigocomRefatoração
refatoraçãonãosetemainten çãodeseadicionarumanovafuncionalidade
oualterarumajáexistente.Aúnicamotivaçãodeumarefatoraçãodeveser
deixarocódigomaissimplesdesermodificado. Oobjetivodeumarefato-
raçãoétornarocódigomaisclaroelimpo,sejacomumamudan çasimples,
comoalteraronomedeumavariável,oucomplexa,comoamudan çadeuma
estruturadeclasses.
Porquesedeverefatorar?
Arespostaésimples,umcódigoqueéconstantementerefatoradoémais
fácildeseralterado,ouseja,umcódigomaisfácildeler,semduplicaç ão,sem
lógicascondicionaismirabolantesetc.Comumcódigofácildeseralterado,
osdesenvolvedorespodemsepreocuparemcriarumcódigoenxutoparaos
requisitosqueelespossuemhoje. Casonofuturosejanecessárioalteraros
requisitos,comestecódigoconstantementerefatoradoémaisfácildeimple-
mentarasmodificações.Destaforma,nãoexistemaisanecessidadedeficar
inventandosoluçõesqueprocuramresolverproblemasqueaindanãoexis-
temeque,casovenhamaexistir,muitoprovavelmentenãoserãodaforma
quehaviamsidoprevistasinicialmente.
Éfácilescreverumcódigoqueocomputadorentenda,difíciléescreverum
códigoqueasoutraspessoasentendam.
Dentreasvantagensdeseutilizararefatoraç ãopodemoscitar:
• melhoracontinuamenteaestruturadaaplicaçãofazendocomquea
modelagem,enãosóocódigo,acompanheasmudan çasderequisito;
• deixaocódigo-fontemaislegível,tornandomaisfácilasuacompreen-
são;
• ajudaaencontrarbugsnocódigo.Umaformadeseencontrarumbug
emumcódigoconfusoéirrefatorandoesimplificandoomesmoaté
encontraroproblema;
• aumentaavelocidadededesenvolvimento,vistoqueébemmaisfácil
deseacrescentarfuncionalidadesemumcódigoclaroelimpo;
29

## Página 34

3.2. Arefatoraçãonodia-a-dia CasadoCódigo
• ajudaaprepararocódigoparareceberumanovafuncionalidade,de
formaanãosernecessáriocomplicarocódigoenquantonãoforpre-
ciso.
3.2 A refatoração no dia-a-dia
Amodelagemconhecidacomoupfrontéaquelaemquetodooprojetoére-
alizadoantesdacodificação,sendodeixadoparaosimplementadoresapenas
atarefadecodificarosmétodos.Estaabordagem,comofoicitadonaintro-
dução,possuiseusproblemascomoadificuldadedeadaptaç ãoamudan çase
oriscodecriarcomplexidadedesnecessária.Nestaabordagem,égastobas-
tantetemponatentativadeseprevertodososproblemasecenários,sendo
quequasesempreexistirãoquestõesquesóserãoidentificadasnomomento
daimplementação.
Poroutrolado,seapenasarefatoraç ãofosseutilizadacomoferramenta
demodelagem,aimplementaçãoocorreriadaprimeiraformaqueviesseaca-
beçaedepoisocódigoseriareestruturadoatéamodelagemchegarnoponto
emquesedeseja.Estaabordagemtambémtemosseusproblemas,poisexiste
dificuldadedeiniciaraimplementaçãosemsepensarmuitonoproblemae
semsaberdireitoporondecome çar.Existiriatambémumretrabalhoexces-
sivovistoqueonúmeroderefatoraçõesparaajustarocódigoseriagrande.
Asoluçãoparaestedilemaéaproveitaromelhordasduasabordagens.
Devesercriadaumamodelagem,antesdesecome çaradesenvolver,queser-
virácomoumaabordageminicialparatentarresolveroproblema. Odife-
rencialnestecasoéqueestamodelagemnãoprecisatentarprevertodasas
situaçõesquepodemocorrereporestemotivonãoprecisasergastomuito
temponestafase.Apartirdestamodelagemcriada,éiniciadaaimplementa-
çãoe,àmedidaqueoutrasquestõesvãosurgindo,arefatoraç ãoservecomo
umajustefinoàmodelagemcriadainicialmente.Tambémnãoéprecisoten-
tarcontemplarnamodelageminicialflexibilidadesparapossíveisrequisitos
futuros,poiscomocódigolimpoesimplesépossívelrefatoraramodelagem
jáexistenteparaaadiçãodestenovorequisito.
Umafamosafrasediz“Projeteparaofuturo,codifiqueparaomomento”,
porém,nestanovaabordagemcomarefatora ção,deve-secriarocódigomais
30

## Página 35

CasadoCódigo Capítulo3. MelhoriaContínuadoCódigocomRefatoração
claropossívelparapermitiraadi çãodenovasfuncionalidadeseevitarprever
requisitosfuturos,sendoquedestaformadeve-se“Projetarparaomomentoe
codificarparaofuturo”.
Quandorefatorar?
Arefatoraçãocostumaseraplicadaantesoudepoisdeseimplementar
umafuncionalidade,porémexisteumaregraquesempredeveserseguida:
nuncarefatorarduranteainclusãodeumafuncionalidade.Searefatoraç ãoé
umatécnicadesemelhorarocódigosemaalteraç ãodocomportamento,não
fazsentidoalterarocomportamentoenquantoserefatora.
Écomumverumarefatoraçãofeitaantesdaadiç ãodeumafuncionali-
dadecomoumaformadeseprepararoterrenoparasuaintroduç ão. Por
exemplo,sequandoumaclassevaiseradicionadanota-sequevárioscom-
portamentosnecessáriossãoiguaisaodeumaclassejáexistente,estaéuma
boahoraparaaextraçãodeumasuperclasseouparaaquebradaclasseexis-
tenteemduasclasses,sendoumaparaaqualserádelegadoocomportamento
emcomum.Arefatoraçãofeitadepoisdaadiçãodafuncionalidadeservepara
daraquelesajustesfinaisnamodelagemdocódigo. Noexemplodado,caso
estaexistênciadestaclassecomcomportamentoemcomumnãofossenotada
antesdodesenvolvimento,arefatoraçãopoderiaserfeitadepoissemnenhum
problema.
Arefatoraçãotambémpodeserumaferramentavaliosaquandoestásefa-
zendoumarevisãodecódigooumesmotentandoentenderalgumtrecho.Ela
tambéméespecialmenteútilquandoseprocuraerrosemumcódigoalheio.
Comoexperiênciapessoal,possocitarumasituaçãonaqualocódigodeuma
classeestavamuitoconfusoeparaentenderoqueestavaacontecendooptou-
sepelarefatoraçãodaquelecódigo. Nofimdascontas,ocódigodaclasse
ficoucercadeumquartodoqueerainicialmente,semalteraç ãonocompor-
tamento.Destaforma,oerroqueestavasendoprocuradofoimaisfacilmente
encontradoe,comoefeitocolateral,ocódigodaclasseficoumuitomaisen-
xuto.Certamenteumdosmaioresprazeresdequemrefatoraédeletarcódigo
duplicado!
31

## Página 36

3.2. Arefatoraçãonodia-a-dia CasadoCódigo
Refatorandocomsegurança
Umsábioditadopopulardizqueemtimequeestáganhandonãosemexe.
Porém,enquantoserefatoraestásemexendoemcódigoquejáestáfuncio-
nando,ouseja,otimeestáganhandoeaosealteraressecódigocorre-seo
riscodainser çãodeumbugnão-intencional. Mesmocomautilizaç ãode
ferramentasquefazemasrefatoraçõesdeformaautomatizada,ocomporta-
mentodocódigoaindapodeseralterado(oquadro“Cuidadonahoradeapli-
carrefatorações”mostraumexemplo).
Emumgrandeprojetocorporativonãosepodecorreroriscodeinserir
umbugemumsistemaquejáestáemproduç ão.Dessaforma,énecessário
algoquegarantaqueocomportamentodocódigonãofoialteradodurante
umarefatoração. Énestepontoquesefazpresenteaimportânciadeseter
umasuítedetestesdeunidade.Comtodosostestespassandodepoisdeuma
alteração,odesenvolvedortemmaisseguran çadequeocomportamentonão
foialterado.
Nãoestánoescopodesteartigofalarsobretestesdeunidade,apesarde
elesteremumpapelfundamentalnapráticadarefatoraç ão.Oquadro“Refa-
toraçãoeExtremeProgramming”falaumpoucosobrearefatoraçãonocon-
textododesenvolvimentoorientadoatestes.Noexemploqueseráapresen-
tado,serámostradaumaclassedetestesdeunidadedaclassequeserárefato-
rada,afimdegarantirqueseucomportamentonãoseráalterado.
“Maucheiro”nocódigo
“Maucheiro”éotermoutilizadoquandoumdeterminadocódigopossui
algumindíciodequeestáprecisandoserrefatorado.Umcódigopossuirum
“maucheiro”nãosignificanecessariamentequeeledeveserrefatorado,mas
quedeveserinvestigadoseeleprecisaounãoderefatoraç ão.
Adetec çãode“maucheiro”podeseralgobemintuitivo!Quandohouveral-
gumadificuldadeparaentenderumcódigoouseidentificaralgoquenãoparece
muitolegal,provavelmenteaquelecódigoprecisaserrefatorado.
Umdos“mauscheiros”quecertamenteprecisaderefatoraçãoéaexis-
tênciadecódigoduplicado.Nessecaso,éprecisorefatoraçãomesmo!Outros
“mauscheiros”dificilmentenãoindicamalgumproblema,comoporexemplo
32

## Página 37

CasadoCódigo Capítulo3. MelhoriaContínuadoCódigocomRefatoração
aexistênciadeumaclassemuitolonga,ummétodomuitolongooumesmo
umalistadeparâmetrosmuitolonga.Elementosmuitolongossãodedifícil
análiseemanutenção,equasesempreexisteumaformamelhordeseobtero
mesmocomportamento.
Outros“mauscheiros”nãosãotãoóbviosassim.Quandoumaclasseco-
meçaaacessarmuitosatributosdeoutraclasse,temosumcasoclássicode“in-
vejadefuncionalidade”.Istonoslevaaseguintepergunta:seráquearesponsa-
bilidadedestetrechodecódigonãodeveriaemoutraclasse?Existetambém
ocasoclássicodasvariáveisquegostamdeandarsemprejuntas,comoem
parâmetrosdemétodosouemvariáveisdeinstância.Talvezesta“amizade”
entreestasvariáveissignifiquequeelasdeveriamformarumanovaclasse.
Comcerteza,umdostiposde“mauscheiro”maispolêmicoéaexistência
decomentáriosnocódigo.Euseiqueduranteasuavidainteiratefalaramque
istoeraumaboaprática,porémmuitasvezesoscomentáriosservemcomo
“desodorantes”paraumcódigodifícildeentender.Muitasvezesémuitomais
fácildescreverumcódigo“macarrônico”emumcomentário,doquefazer
comqueelefiqueclaroparaquemestiverlendo.Ocomentárioemsinãoé
mau,masapresen çadelepodeindicarqueumcódigodedifícilentendimento
precisasermelhorado.
Oobjetivonestase çãofoimostrarapenasalgunsdosmuitostiposde
“mauscheiros”existentes,paraquesepossateridéiadotipodecoisaque
podeindicaranecessidadedeumarefatoração.NolivrodoMartinFowlerso-
brerefatoraçãocitadoanteriormente,existemdiversosoutrostiposde“mau
cheiro”documentados.Comofoidito,nemsempreum“maucheiro”indica
umproblemarealnocódigo,porémelessãodicasdequealgumacoisapode
estarerrada.
RefatoraçãoxDesempenho
QuandoFowlerdefiniurefatoraçãoeledeixoubemclaroqueoobjetivo
darefatoraçãoeradeixarocódigomaislimpoemaisclaro.Oatoderefatorar,
muitasvezes,nãotemainten çãodemelhorardesempenho,sendoqueinclu-
sivealgunscódigosdepoisdeseremrefatoradosapresentamumdesempenho
inferioremrelaçãoaocódigooriginal.Porexemplo,seécriadoummétodo
parasubstituirumavariávellocalquerecebeumcálculofeitocomvariáveis
33

## Página 38

3.2. Arefatoraçãonodia-a-dia CasadoCódigo
deinstância,seométodoforinvocadomaisdeumavez,ocálculoseráfeito
maisdeumaveze,comcerteza,odesempenhoseráinferior.
Masseráqueéaceitávelterumaperdadedesempenhoporumcódigo
maisclaro?Issovaidependermuitodaperdaedamelhorianaclarezanocó-
digo.Nãoexisteumaregraqueirávalerparatodososcasos.Nessaquestãoo
queirápesarbastantesãoosrequisitos,sendoqueemalgunscasosestasper-
dasnodesempenhoserãoperfeitamenteaceitáveiseemoutroscasosnão.De
qualquerforma,terumcódigoclaroelimpofacilitabastantenaotimizaç ão
dodesempenho.
Refatoreocódigodeformaadeixá-loomaisclaroelimpopossível. De-
pois,seodesempenhonãoforsatisfatório,serámuitomaisfácilfazerosajustes
necessários.
Quandoédifícilrefatorar
Existemalgunscasosemquearefatoraçãosetornaalgodifícildeserfeito,
eemsuagrandemaioriadevidoaumaltograudeacoplamentoentrepartes
daaplicação.Quandoarefatoraçãoaserfeitaenvolvebancodedados,princi-
palmentequandoomesmoéutilizadoemmaisdeumaaplicaç ão,asituação
secomplica. Oacoplamentodaaplicaçãocomaestruturadobancoacaba
sendobemalto,eestadependênciadificultaarefatoraç ão.Aadiçãodeuma
camadadepersistênciaqueprotejaaaplicaçãodosdetalhesdobanco,utili-
zando,porexemplo,JPA,ajudabastante,masnãoresolvecompletamenteo
problema.Olivro“RefactoringDatabases:EvolutionaryDatabaseDesign”de
ScottAmblerePramodkumarSadalagefalacommaisdetalhessobrearefa-
toraçãodebancodedados,queémuitomaistrabalhosaeenvolvemuitomais
passosdoqueumarefatoraçãoemcódigo-fonte.
Outroproblemaéquandoarefatoraçãoesbarraemumainterfacecom
outrosistema.Muitasvezesnãosetemacessoàaplicaç ãoqueestáutilizando
asuaclasse,eamudan çadaassinaturadeummétodo,porexemplo,fariacom
queestaoutraaplicaçãonãofuncionassecomanovaversão.Quandosetra-
balhacomestetipodesoftware,como,porexemplo,umcomponentedispo-
nibilizadoaoutrasaplicações,amudan çadevesergradual,primeirocriando
ométodonovoedeixandoométodoantigocomo deprecated,esóde-
poisremovendoaversãoantiga.Nestecaso,outrasoluç ãoseriautilizaruma
34

## Página 39

CasadoCódigo Capítulo3. MelhoriaContínuadoCódigocomRefatoração
classeAdaptercommétodoscomaassinaturaantigaqueinvocamosnovos
métodosdaclassecomanovaimplementação.Existemtrabalhosacadêmicos
recentesquebuscamsoluçõesparaessasquestões.Otrabalho“Annotations
forSeamlessAspect-BasedSoftwareEvolution”(verreferências)propõeouso
deanotaçõesemcódigorefatoradoparaqueaversãoantigadocódigosejage-
radaesincronizadacomaversãonova.
3.3 Refatoração e Extreme Programming (XP)
Apesardearefatoraçãoserumatécnicaquepodeseraplicadaindependente
dametodologiaqueestásendoutilizada,umagrandeparceladesuapopulari-
zaçãoperanteacomunidadededesenvolvimentofoigraçasasuautilizaçãona
metodologiaExtremeProgramming(XP).Arefatoraçãoéumadasprincipais
práticasdessametodologiaetambémépartefundamentaldatécnicadede-
senvolvimentoconhecidacomodesenvolvimentodirigidoportestes(TDD).
Nessaseção,seráfaladocomoarefatoraçãoseencaixanaXPecomoelain-
teragecomasoutraspráticas.
NaXPexisteapráticadocódigocoletivo,emquecadaartefatodecódigo
nãopossuiumdonoepodesertrabalhadoporqualquerumdaequipe.Isto
permitequesemprequefordetectadaanecessidadedeserefatorar,sendoem
umcódigodoprópriodesenvolvedoroucriadoporoutro,aalteraç ãopossa
serfeitasemproblemas,poisocódigopertenceatodos.Aexistênciadainte-
graçãocontínuafazcomqueseumarefatoraç ãofeitaentraemconflitocomo
trabalhodeoutrodesenvolvedor,istosejadetectadoemumcurtoespaçode
tempo.
Aprogramaçãoempareseapráticadeumritmosustentávelajudamo
desenvolvedoratermaiscoragemeacometermenoserros.Ousodepadrões
decódigoeapráticadeumamodelagemsimplesdeixamocódigomaisfácil
deentendereconsequentementemaisfácilderefatorar.
Ostestesfeitosantesdocódigocomcertezasãoatécnicaquemelhor
apóiamapráticadarefatoração. NaXP,amodelagemeacodificaç ãosão
feitaspormeiodeumatécnicachamadadesenvolvimentodirigidoportestes
(TDD).Nestatécnica,quandosedesenvolveumaclasse,primeiroseescreve
umtestequeirárefletirocomportamentodaquelaclasseperanteumdeter-
35

## Página 40

3.4. Exemploderefatoração CasadoCódigo
minadocenáriodeuso. Comotestepronto,éfeitoomaissimplespossível
paraqueaqueletestesejaexecutadocomsucesso.Estandotudofuncionando,
ocódigoérefatoradoparaaeliminaçãodeduplicação.Comessespequenos
ciclos,ocódigovaisendodesenvolvidoiterativamenteecadapassoédado
comsegurança.Comousododesenvolvimentodirigidoportestes,ocódigo
vaisendosemprerefatoradoemelhorado.Asuítedetestesqueéresultante
dautilizaçãodestatécnicaserveparadarumagrandeseguran çacasosejane-
cessáriaaexecuçãodeumagranderefatoração.
Destaforma,ousodarefatoraç ãonaXPéapoiadoporoutraspráticas,
criandoumasinergianodesenvolvimento.Umaparceladoméritodafamosa
curvaquedizquenaXPocustodemudan çanotempoapartirdeumdeter-
minadopontosetornaconstante,podeseratribuídaàpráticadarefatoraç ão.
Istoéverdadeporqueoganhoemqualidadeobtidocomumarefatoraç ão
contínuadocódigofazcomqueaalteraç ãodeumrequisitosejamuitomais
fácildeserinserida.
3.4 Exemplo de refatoração
Nessemomento,acreditoquetodosdevemestarcansadosdeteoriaeansi-
ososparaverumcódigoserrefatorado. Quemnuncarefatorouumcódigo
nãosabecomoébomogostinhodevertudoficandomaissimpleseistosem
mudarocomportamentodaclasse!Paramostraresteexemploseráutilizado
oIDEEclipseEuropa,porémoutrosIDEspoderiamserutilizadossempro-
blema.NoEclipse,asfuncionalidadesderefatoraç ãopodemserencontradas
abrindoomenuRefactor,conformemostradonafigura 3.1,ouclicandocom
obotãodireitodomousesobreocódigoeentrandonosubmenuRefactor.
36

## Página 41

CasadoCódigo Capítulo3. MelhoriaContínuadoCódigocomRefatoração
Fig.3.1:MenuderefatoraçãodaferramentaEclipse
Contextodoexemplo
Oexemploqueserámostradonãotemainten çãodesercompletoecom
muitasfuncionalidades.Seuobjetivoéserdidáticoeilustrarcomoum“mau
cheiro”édetectadoemumcódigoecomoarefatoraçãoprocedepassoapasso.
Paraarealizaçãodeumarefatoraçãocomseguran ça,teremosumaclassede
testedeunidadequeirágarantirqueocomportamentodenossasclassesde
37

## Página 42

3.4. Exemploderefatoração CasadoCódigo
exemplonãoseráalterado.
Afuncionalidadeprovidaporestasclassesémuitosimples. Aclasse
ProcessadorDeItens,apresentadanapróximalistagem,possuiummé-
todo getItens()querecebeum InputStreamelêemcadalinhaos
dadosdeumitemseparadospor“;”. Essemétodocolocaestesdadosdos
itensemumobjetodaclasse Item,apresentadanalistagemseguinte,ere-
tornaumalistadeobjetosdotipo Item. Estaclassetambémpossuiomé-
todo getValorTotalPorTipo(),querecebeum InputStreameuma
Stringquerepresentaotipodeitemeretornaasomadosvalorestotaisde
cadaitem(aquantidadevezesovalorunitário)daqueletipodeitem.
Aclasse Itemnãopossuimuitafuncionalidadeesimplesmentearma-
zenaosvaloresdascaracterísticasdeumitem. Ofatodeestaclassenãoter
muitafuncionalidadejádeixauma“pulgaatrásdaorelha”: seráqueoutra
classeestáfazendocoisasqueeramresponsabilidadedestaclasse?
Listagem3.1-ClasseProcessadorDeItens.:
public class ProcessadorDeItens {
public List<Item> getItens(InputStream input)
throws IOException {
List<Item> listItens = new ArrayList<Item>();
BufferedReader reader =
new BufferedReader(new InputStreamReader(input));
String line = null;
while ((line = reader.readLine()) != null) {
Item item = new Item();
String[] elementos = line.split(";");
item.setCodigo(elementos[0]);
item.setTipo(elementos[1]);
item.setQuantidade(Integer.parseInt(elementos[2]));
item.setValorUnitario(
Double.parseDouble(elementos[3]));
listItens.add(item);
}
return listItens;
}
38

## Página 43

CasadoCódigo Capítulo3. MelhoriaContínuadoCódigocomRefatoração
public double getValorTotalPorTipo(InputStream input,
String tipo) throws IOException {
double valorTotal = 0;
BufferedReader reader =
new BufferedReader(new InputStreamReader(input));
String line = null;
while ((line = reader.readLine()) != null) {
String[] elementos = line.split(";");
if (tipo.equals(elementos[1]))
valorTotal += Double.parseDouble(elementos[3])
* Integer.parseInt(elementos[2]);
}
return valorTotal;
}
}
Listagem3.2-ClasseItem.:
public class Item {
private String codigo;
private String tipo;
private int quantidade;
private double valorUnitario;
public String getCodigo() {
return codigo;
}
public void setCodigo(String codigo) {
this.codigo = codigo;
}
public int getQuantidade() {
return quantidade;
}
public void setQuantidade(int quantidade) {
this.quantidade = quantidade;
}
public String getTipo() {
return tipo;
39

## Página 44

3.4. Exemploderefatoração CasadoCódigo
}
public void setTipo(String tipo) {
this.tipo = tipo;
}
public double getValorUnitario() {
return valorUnitario;
}
public void setValorUnitario(double valorUnitario) {
this.valorUnitario = valorUnitario;
}
}
Napróximalistagemestáocódigodotestedeunidadequeirágarantir
queasmodificaçõesnocódigoqueforemfeitasnãoafetarãoocomporta-
mentoexternodaclasse.
Listagem 3.3- Teste de unidade para garantir o funcionamento do có-
digo.:
import static org.junit.Assert.assertEquals;
public class TestProcessadorDeItens {
private final static String dadosDeTeste =
"3123123;Eletrodomestico;1;1000.00\n"+
"7567123;Eletrodomestico;3;500.00\n"+
"3978876;Eletroeletronico;2;700.00\n"+
"1236543;Movel;7;350.00\n"+
"9324423;Movel;4;600.00\n";
@Test
public void testGetItens() throws IOException {
ProcessadorDeItens proc = new ProcessadorDeItens();
List<Item> itens = proc.getItens(
new ByteArrayInputStream(dadosDeTeste.getBytes()));
assertEquals("Recuperacao de todos os itens",
itens.size(),5);
40

## Página 45

CasadoCódigo Capítulo3. MelhoriaContínuadoCódigocomRefatoração
assertEquals("Recuperacao de Codigo",
"3123123",itens.get(0).getCodigo());
assertEquals("Recuperacao de Tipo",
"Eletrodomestico",itens.get(1).getTipo());
assertEquals("Recuperacao de Quantidade",
2,itens.get(2).getQuantidade());
assertEquals("Recuperacao de Valor Unitario",
350.00,itens.get(3).getValorUnitario());
}
@Test
public void testGetValorTotalporTipo() throws IOException{
ProcessadorDeItens proc = new ProcessadorDeItens();
double totalEletromesticos = proc.getValorTotalporTipo(
new ByteArrayInputStream(
dadosDeTeste.getBytes()),"Eletrodomestico");
double totalMovel = proc.getValorTotalporTipo(
new ByteArrayInputStream(dadosDeTeste.getBytes()),
"Movel");
assertEquals("Compara o total eletrodomesticos",
totalEletromesticos,2500.0);
assertEquals("Compara o total movel",
totalMovel,4850.0);
}
}
Acertandoasresponsabilidadesdasclasses
Aprimeiracoisaquemeincomodanestecódigoestãonaslinhasdentro
do whiledométodo getItens().Umtrechodecódigoquechamaqua-
trométodosdeumaclasseemquatrolinhasdecódigo,parece-meestarcom
invejadafuncionalidadedestaclasse.Parecefazersentidoquesejaresponsa-
bilidadedaclasse Itemsabercomoextrairosseusdadosseparadospor“;”
deumaString. Destaforma,aprimeirarefatoraç ãoaserfeitaéaextraç ão
destetrechodecódigoparaummétododaclasse Item.
Infelizmenteestarefatoraçãonãodáparaserfeitadiretamenteeserápre-
cisofazeralgunspassosantesdeatingiroestadodesejado.Oprimeiropassoé
41

## Página 46

3.4. Exemploderefatoração CasadoCódigo
marcarascincolinhasdecódigoreferenetsaessafuncionalidadeeiraomenu
Refactoreescolheraop ção ExtractMethod. Seráexibidaajanelamostrada
nafigura3.2.Notequeosparâmetrosnecessáriosjávêmconfigurados,basta
daronomeaométodo, carregarItemDaString()epressionarobotão
ok.Casodesejevercomoaclassevaificarantesdeaplicarefetivamenteare-
fatoração,cliquenobotão Preview>.Nestecaso,umajanelamostrarátodas
asmodificaçõesqueserãofeitasnocódigo,conformefigura 3.3.
Fig.3.2:Janelapop-updeextraçãodemétodo.
42

## Página 47

CasadoCódigo Capítulo3. MelhoriaContínuadoCódigocomRefatoração
Fig.3.3:Previewdasalteraçõesqueserãorealizadascomaextraç ãodomé-
todo.
Aoconcluirarefatoração,serágeradoumnovométodoetrechodeonde
ométodofoiextraído,ocódigooriginal,ésubstituídopelachamadaaeste
novométodo.Aseguirtemosonovométodogerado:
private void carregarItemDaString(String line, Item item) {
String[] elementos = line.split(";");
item.setCodigo(elementos[0]);
item.setTipo(elementos[1]);
item.setQuantidade(Integer.parseInt(elementos[2]));
item.setValorUnitario(Double.parseDouble(elementos[3]));
}
Esteéumbommomentoparaaexecuç ãodaclassedeteste!Felizmente
ostestescontinuamexecutandocomsucessoepode-seseguirparaopróximo
passoqueémoverométodoextraídoparaaclasse Item.Paraisso,coloca-se
ocursorsobreaassinaturadométodoeescolhemosnomenu Refactorarefa-
toraçãoMove.Ajanelanafigura 3.4éexibidaefelizmentejáfoiidentificada
queaclasse Iteméumacandidataparareceberométodo.Onomedomé-
todoserámodificadopara carregarDaString()epodemosconfirmara
43

## Página 48

3.4. Exemploderefatoração CasadoCódigo
refatoraçãopressionando ok. Seforapontadoumproblemadevisibilidade
donovométodonaclasse Item,depoisdeconfirmararefatoração,altereo
modificadordeacessodométodo carregarDaString()para public.
Fig.3.4:Janelapop-updarefatoraçãoMoveMethod.
CasonasuaversãodoEclipseométodo carregarItemDaString()
daclasse ProcessadorDeItensnãoforeliminado,bastaclicarsobreele
enomenu Refactorescolherarefatoração Inline. Comestarefatoraçãoem
todososlugaresemqueestemétodoforutilizado,serásubstituídaachamada
dométodopelasuaimplementação(nocaso,achamadaaonovométododa
classeItem).
Comarefatoraçãoterminada,éumaboahoraparaserodarostestesde
44

## Página 49

CasadoCódigo Capítulo3. MelhoriaContínuadoCódigocomRefatoração
unidadeparaverificarsetudofoifeitocorretamente.Setudocorreucomoo
esperado,onovocódigodasclasses Iteme ProcessadorDeItensserá
osqueestão,respectivamente,nasduaspróximaslistagens.
Listagem 3.4- Classe ProcessadorDeItens depois da primeira refatora-
ção.:
public class ProcessadorDeItens {
public List<Item> getItens(InputStream input)
throws IOException{
List<Item> listItens = new ArrayList<Item>();
BufferedReader reader =
new BufferedReader(new InputStreamReader(input));
String line = null;
while((line = reader.readLine()) != null){
Item item = new Item();
item.carregarDaString(line);
listItens.add(item);
}
return listItens;
}
public double getValorTotalporTipo(InputStream input,
String tipo) throws IOException{
double valorTotal = 0;
BufferedReader reader =
new BufferedReader(new InputStreamReader(input));
String line = null;
while((line = reader.readLine()) != null){
String[] elementos = line.split(";");
if(tipo.equals(elementos[1]))
valorTotal += Double.parseDouble(elementos[3])
*Integer.parseInt(elementos[2]);
}
return valorTotal;
}
}
}
45

## Página 50

3.4. Exemploderefatoração CasadoCódigo
Listagem3.5-ClasseItemdepoisdaprimeirarefatoraç ão.:
public class Item {
private String codigo;
private String tipo;
private int quantidade;
private double valorUnitario;
//métodos getters e setters omitidos
public void carregarDaString(String line) {
String[] elementos = line.split(";");
setCodigo(elementos[0]);
setTipo(elementos[1]);
setQuantidade(Integer.parseInt(elementos[2]));
setValorUnitario(Double.parseDouble(elementos[3]));
}
}
Deixandoocódigomaisclaro
No método getValorTotalporTipo() da classe
ProcessadorDeItens, os valores retirados de cadaString que re-
presenta um item são utilizados diretamente, de forma que fica difícil
entenderosignificadodeumcálculocomoodalinhaabaixo:
valorTotal += Double.parseDouble(elementos[3])
*Integer.parseInt(elementos[2]);
Umapessoaqueleressecódigopelaprimeiraveznãoirárapidamente
compreenderqueocálculoestámultiplicandoovalorunitáriodecadaitem
pelaquantidade.Umaformadecontornaroproblemaseriacolocarumco-
mentárioparaexplicaroqueestáacontecendo.Masparaquêfazerissoseo
códigopodefalarporsipróprio?
Dessaforma,paradeixarocódigomaisclaro,seráutilizadoométodo
queacabamosdeextrairemoverparaaclasse Item.Antesdefazermosos
cálculos,ométodocarregarDaString()iráextrairosdadosda String
46

## Página 51

CasadoCódigo Capítulo3. MelhoriaContínuadoCódigocomRefatoração
eserãoutilizadososmétodosdeacessodaclasse Itemparaarealizaçãodos
cálculos.Onovocódigodafun çãoestárepresentadoabaixo:
public double getValorTotalporTipo(InputStream input,
String tipo) throws IOException{
double valorTotal = 0;
BufferedReader reader =
new BufferedReader(new InputStreamReader(input));
String line = null;
while((line = reader.readLine()) != null){
Item item = new Item();
item.carregarDaString(line);
if(tipo.equals(item.getTipo()))
valorTotal += item.getValorUnitario()
*item.getQuantidade();
}
return valorTotal;
}
Apesardonúmerodelinhasdecódigoteraumentado,ocódigoagoraé
bemmaisclaro.Nemseránecessáriocomentáriosparacomunicaroqueestá
acontecendo.Porém,antesdeavan çarparaopróximopassodarefatoraç ão,
existealgoqueaindanão“cheirabem”nessecódigo:ofatodeométodoestar
calculandoovalortotaldoitempareceserumtantoinvejoso. Assim,faz
muitomaissentidoessecálculoserresponsabilidadedaprópriaclasse Item.
Destaforma,oseguintemétodofoicriadonaclasse Item:
public double getValorTotal(){
return getValorUnitario()*getQuantidade();
}
Alémdesubstituirocálculonométodo getValorTotalPorTipo(),
para evitar confusões, também será alterado o nome da variável local
valorTotalpara valorTotalPorTipo. Colocandoocursoremcima
davariáveleselecionandonomenu RefactoraopçãoRename,oIDEpermite
noprópriocódigoaalteraç ãodonome. EmversõesanterioresdoEclipse,
umajanelaeraabertacomumcampoparasecolocaronovonomedavariá-
vel.Depoisdeconfirmadaarefatoraç ão,todasasreferênciasàquelavariável
serãoalteradas.
47

## Página 52

3.4. Exemploderefatoração CasadoCódigo
Pormaisquepare çanãofazerdiferen ça,nomesexplicativosparavariá-
veis,métodoseclassessãoessenciaisparaaclarezadocódigo.Experimente
utilizarapenasnomedevariáveismonossílabasparavercomoissoaumenta
acomplexidadedocódigoabsurdamente.Seumnomenãoparecebom,não
penseduasvezes,troque-oimediatamente!
Depois de feita a refatoração, é mais uma boa hora para serem
executados os testes e para verificar se o comportamento não foi alte-
rado. A seguir, pode ser visto como ficou o código do novo método
getValorTotalPorTipo():
public double getValorTotalPorTipo(InputStream input,
String tipo) throws IOException{
double valorTotalporTipo = 0;
BufferedReader reader =
new BufferedReader(new InputStreamReader(input));
String line = null;
while((line = reader.readLine()) != null){
Item item = new Item();
item.carregarDaString(line);
if(tipo.equals(item.getTipo()))
valorTotalporTipo += item.getValorTotal();
}
}
return valorTotalporTipo;
}
Eliminandoduplicaçãodecódigo
Oúltimo“maucheiro”queseráeliminadodessecódigoéaduplicação
decódigoexistenteentreosdoismétodosdaclasse ProcessadorDeItens.
Observandobemosdoismétodos,épossívelfacilmenteobservarqueafunci-
onalidadeébemparecida.Amboslêemdaclasse InputStreamas Strings
relativasaositensedecodificamemobjetosdotipo Item.Adiferen çaéque
ummétodoadicionaosobjetosemumalistaeooutroosutilizaparacalcular
osomatóriodosvalorestotaisdeitensquepossuemumdeterminadotipo.
Oquepoderiaserfeitoparaeliminarestaduplicaç ãodecódigoé,no
método getValorTotalporTipo(), utilizar o métodogetItens()
48

## Página 53

CasadoCódigo Capítulo3. MelhoriaContínuadoCódigocomRefatoração
pararecuperaraslistasdeobjetosdotipo Itemparaqueoscálculospossam
serfeitosdepois. Infelizmente,refatoraçõescomoestanãoexisteIDEque
faça, pois são muito específicas do domínio. Dessa forma, será preciso
realizá-ladeformamanualmesmo. Felizmente,existeumasuítedetestes
deunidadeparanosmostrarqueocomportamentoverificadopelostestes
nãofoialterado.Ocódigofinaldasclasses ProcessadorDeItense Item
podemservistosnasduaspróximaslistagens.
Listagem 3.6- Classe ProcessadorDeItens depois de todas as refatora-
ções.:
public class ProcessadorDeItens {
public List<Item> getItens(InputStream input)
throws IOException{
List<Item> listItens = new ArrayList<Item>();
BufferedReader reader =
new BufferedReader(new InputStreamReader(input));
String line = null;
while((line = reader.readLine()) != null){
Item item = new Item();
item.carregarDaString(line);
listItens.add(item);
}
return listItens;
}
public double getValorTotalporTipo(InputStream input,
String tipo) throws IOException{
double valorTotalporTipo = 0;
List<Item> listItens = getItens(input);
for(Item item : listItens)
if(tipo.equals(item.getTipo()))
valorTotalporTipo += item.getValorTotal();
return valorTotalporTipo;
}
}
Listagem3.7-ClasseItemdepoisdetodasasrefatorações.:
49

## Página 54

3.4. Exemploderefatoração CasadoCódigo
public class Item {
private String codigo;
private String tipo;
private int quantidade;
private double valorUnitario;
//métodos getters e setters omitidos
public void carregarDaString(String line) {
String[] elementos = line.split(";");
setCodigo(elementos[0]);
setTipo(elementos[1]);
setQuantidade(Integer.parseInt(elementos[2]));
setValorUnitario(Double.parseDouble(elementos[3]));
}
public double getValorTotal(){
return getValorUnitario()*getQuantidade();
}
}
Consideraçõesfinaisdoexemplo
Aoserobservadoocódigoinicialeocódigofinaldasclasses,épossível
perceberque,depoisdarefatoração,realmentehouveumagrandemelhoria
emtermosdeclarezadocódigo. Emmuitosdosexemplosderefatoraç ão,
existemcoisashorrendasnocódigoinicial!Nesteexemplo,procureicolocar
umcódigodecertaformarazoávelparaquefossevistoquemesmoumcó-
digosimpleseaparentementesemproblemaspodesermelhoradodeformaa
aumentaraclarezaemanutenibilidadedomesmo.Seforalterado,porexem-
plo,oformatodecomoosdadosvêmparaseremprocessados,asmudan ças
nocódigoseriampontuaisenãoespalhadaspordiversasfun ções.
Dopontodevistadedesempenho,onovocódigoacabasendoinferiorao
códigooriginalnométodoemqueovalortotalportipodeitemécalculado.
Istoocorre,pois,aoinvésdehaverapenasumlaçoparaocálculo,éutilizado
umparaaconstruçãodeumalistadeitenseoutroparaosomatóriodosvalo-
res.Gostariadedeixar,comoexercícioparaosleitores,arefatoraç ãodaclasse
50

## Página 55

CasadoCódigo Capítulo3. MelhoriaContínuadoCódigocomRefatoração
ProcessadorDeItensparatransformá-laemumaclassequerepresentasse
umconjuntodeitense,emseguida,refatorarocódigodeformaaseobterum
desempenhocompatívelcomodométodooriginal.
3.5 Cuidados para aplicar as refatorações
Paraefetuarqualquerrefatoração,mesmocomautilizaç ãodeumaferra-
menta,érecomendávelquesetenhacuidadoeoapoiodeumasuítedetestes
deunidade,paragarantirqueocomportamentodaaplicaç ãonãofoialte-
rado. Estaseçãoirámostrarumexemplodeumaextraç ãodemétodofeita
comferramentaquenãomantémocomportamentooriginaldocódigo.
Esseexemploirárefatorarométodoapresentadonapróximalistagem.
Ele recebe um array com linhas e um documento e insere dentro, nas
páginasdestedocumento,tabelascontendoestaslinhas.Asclasses Linhae
Documentonãoserãoapresentadas,poisoimportanteéalógicadocódigo
enãoocomportamentodasclassesenvolvidasnoexemplo.
Listagem3.8-CódigodométodogeraTabelas().:
public void geraTabelas(Linha[] linhas, Documento documento) {
Tabela tabela = null;
tabela = new Tabela();
tabela.inserirCabecalho();
tabela.inicializaColunas();
for(Linha linha : linhas){
tabela.inserirLinha(linha);
if(tabela.isTamanhoPagina(documento)){
documento.inserePagina(tabela);
tabela = new Tabela();
tabela.inserirCabecalho();
tabela.inicializaColunas();
}
}
}
Aoobservarocódigo, umdesenvolvedorvêocódigoduplicado(em
destaquenaListagem)edecideextrairométodoutilizandoafuncionalidades
51

## Página 56

3.5. Cuidadosparaaplicarasrefatorações CasadoCódigo
deseuIDE.Ocódigoficaconformemostradonalistagemaseguir.
Listagem3.9-CódigodométodogeraTabelas()refatorado.:
public void geraTabelas(Linhas[] linhas, Documento documento) {
Tabela tabela = null;
inicializaTabela(tabela);
for(Linha linha : linhas){
tabela.inserirLinha(linha);
if(tabela.isTamanhoPagina(documento)){
documento.inserePagina(tabela);
inicializaTabela(tabela);
}
}
}
private void inicializaTabela(Tabela tabela){
tabela = new Tabela();
tabela.inserirCabecalho();
tabela.inicializaColunas();
}
Aoexecutarocódigo,odesenvolvedorsedácontaqueocódigoqueestava
funcionando,derepente,paroudefuncionar.Aoobservarocódigocommais
cuidado,eleobservaque,aopassaravariável tabelacomoparâmetro,é
passadaumareferênciaparaoobjetoqueestánométodo geraTabelas().
Essareferência,aprincípio,apontaparaomesmoobjetodométodoqueo
chamou,comomostradonafigura 3.5. Nomomentoemquesechamao
construtor,avariável tabeladométodo inicializaTabela()passa
aapontarparaoutrainstância,masavariáveldométodo geraTabelas()
continuaamesma,conformefigura 3.6.
52

## Página 57

CasadoCódigo Capítulo3. MelhoriaContínuadoCódigocomRefatoração
Fig.3.5:Asduasvariáveisapontamparaomesmoobjeto.
Fig.3.6:Avariávelqueapontavaparaoobjetoagoraapontaparaoutro.
Paraarefatoraçãodoexemplofuncionarcorretamente,deveríamosfazer
comqueonovométodoretornasseumareferênciaparaoobjetocriadoe,no
métodoprincipal,queelafosseatribuídaàvariávelquesedeseja.Alistagem
aseguirapresentaocódigorefatoradocorreto.
Listagem 3.10- Código do método geraTabelas() refatorado de forma
correta.:
public void geraTabelas(Linhas[] linhas, Documento documento) {
Tabela tabela = null;
tabela = inicializaTabela();
for(Linha linha : linhas){
tabela.inserirLinha(linha);
if(tabela.isTamanhoPagina(documento)){
documento.inserePagina(tabela);
tabela = inicializaTabela();
}
53

## Página 58

3.5. Cuidadosparaaplicarasrefatorações CasadoCódigo
}
}
private Tabela inicializaTabela(){
Tabela tabela = new Tabela();
tabela.inserirCabecalho();
tabela.inicializaColunas();
return tabela;
}
OserrosqueosIDEscometememrefatoraçõessãomaiscomunsdoque
seimagina.Oartigo SoundandExtensibleRenamingforJava,apresentado
noOOPSLAde2008(videreferências),mostradiversoserrosqueosIDEs
cometemnasrefatorações Renameepropõeumasoluç ãoparaessestipos
de refatoração. Um dos exemplos mostrados no artigo está apresentado
nasduaspróximaslistagens. ConsiderequenoIDEEclipserenomeia-se,
naprimeiralistagem,avariável ypara x. Oresultadoéumcódigocom
comportamentodiferentedooriginal,apresentadonalistagemseguinte. A
variávelyérenomeadapara xnainstrução System.out.println(y);
oquefazcomquenaverdadesejautilizadaoutravariáveldeinstânciada
innerclassquetambémsechama x.
Listagem3.11-Códigoexemplodeumaclassecomplexa.:
class A {
public static void main(String[] args) {
final int y = 23;
new Thread() {
int x = 42;
void run() {
System.out.println(y);
}
}.start();
}
}
Listagem3.12-Códigoexemplorefatoradoerradamente.:
class A {
public static void main(String[] args) {
54

## Página 59

CasadoCódigo Capítulo3. MelhoriaContínuadoCódigocomRefatoração
final int x = 23;
new Thread() {
int x = 42;
void run() {
System.out.println(x);
}
}.start();
}
}
Aliçãoquedevesertiradadessesexemploséque,pormaisqueasferra-
mentasfacilitemanossavidacomfuncionalidadesderefatoraç ãodecódigo,
arefatoraçãodeveserfeitaapartirdeumaanálisecríticadocódigoaserre-
fatorado.NãoéporqueumarefatoraçãoéautomatizadaemumIDEquesua
aplicaçãosempreirámanterocomportamentooriginaldocódigo.Deprefe-
rência,tenhasempreumasuítedetestesqueverifiqueocomportamentode
suasclassesantesdesairrefatorandotodoocódigo.
3.6 Considerações finais
Arefatoraçãoéumapráticafundamentalparaumdesenvolvimentoiterativo,
emque,acadaitera ção,ocódigodevesermodificadoenovasfuncionalida-
dessãoconstantementeadicionadas.Ousodepadrõesdeprojetoédegrande
importânciaparaamodelagemmacrodeumaaplicaç ão,porémarefatora-
çãovaimuitomaisfundo.Arefatoraç ão,alémdemelhoraramodelagemda
aplicaçãocomaeliminaçãodecódigoduplicado,mexeemdetalhesmenores,
comoemlógicascondicionaiscomplicadaseatémesmonanomenclaturados
elementosdocódigo.Oaumentonaqualidadefinaldocódigoésignificativo!
Aaplicaçãodasrefatoraçõesdeveserfeitacombastantecuidado,mesmo
comautilizaçãodeIDEsqueautomatizempartedoprocesso.Aexistênciade
testesdeunidadedáaoprocessoderefatoraçãocontroleeseguran ça.Assim
comoparaaplicarpadrõesnoprojetodeumsoftware,aprenderasdiferentes
formasdeserefatorarumcódigoexigebastanteestudo.Váriasrefatorações
acabamtendocomoresultadoaaplicaçãodeumpadrão(verlivroRefactoring
toPatternsnasreferências).Dessaforma,aprenderarefatorarumcódigoé
aprenderatrabalharcomsuamodelagemdeformacontínua,realizandomu-
55

## Página 60

3.7. Referências CasadoCódigo
dançaspassoapassocontroladamante,semprevisandoàmelhoradaquali-
dadeedaclarezadocódigo-fonte.
3.7 Referências
• Refatoração:AperfeiçoandooProjetodeCódigoExistente.MartinFo-
wler(Bookman,2004)
• RefactoringtoPatterns.JoshuaKerievsky(Addison-Wesley,2004)
• RefactoringDatabases:EvolutionaryDatabaseDesign. ScottW.Am-
blerePramodkumarJ.Sadalage(Addison-WesleyProfessional,2006)
• AnnotationsforSeamlessAspect-BasedSoftwareEvolution. Susanne
CechPrevitalie ThomasR.Gross(RAM-SE’08-5thECOOPWorkshop
onReflection,AOPandMeta-DataforSoftwareEvolution,2008)
• SoundandExtensibleRenamingforJava. MaxSchäfer,TorbjörnEk-
maneOegedeMoor(OOPSLA08)
56

## Página 61

Capítulo4
OsPrincípiosdaModelagemÁgil
“Oqueprecisamosmodelar?Quantoprecisamosmodelar?Paraquemodelar?
Osvalores,princípiosepráticasdaModelagemÁgil(AgileModeling),um
métododefendidoporScottAmbler,podemauxiliarsuaequipenessa
importantetarefadodesenvolvimentodesoftware.Artefatos“bonitos”feitos
porferramentascarasnemsempresãoosmelhoresparamelhorara
comunicaçãooumelhoraraqualidadedoseucódigo.Modelarosoftwareem
grupoecomaparticipa çãodosusuários,utilizando,porexemplo,um
rascunho,éumadasmaneirasinteressantesdeseconseguirqualidadenoseu
design.”
–porRodrigoYoshima
Umadasdúvidasmaiscomunsnasequipesdedesenvolvimentoé:“Como
conseguirefetivamentecapturarasnecessidadesdosusuáriosecomunicá-las
semruídoparadentrodaminhaequipededesenvolvimento?”.Pararespon-

## Página 62

CasadoCódigo
deraprimeirapartedessaperguntaéfácil:éimpossívelcapturarasreaisne-
cessidadesdosusuários.Umadasquestõesmaisdefendidasnesteartigoéo
desenvolvimentoiterativo,emqueentregamossoftwarefuncionandocons-
tantementeparaobservarseasnecessidadesforamatendidas.Requisitosnão
são“verdade”atéqueseprovejuntamentecomousuárioatravésdesoftware
funcionando.
Jácomrelaçãoàcomunicaçãodaequipe,podemosaplicarpráticasearte-
fatosparaqueaspessoasenvolvidasnoprojetocolaboremparaqueasoluç ão
atendaaonegócioe,aomesmotempo,boaspráticasdeprogramaç ãosejam
respeitadas.
Aoiniciarestaleitura,vocêspodempensarquesetratadeassuntode
“Analistas”,porém,nãoéinteressanteseaterapapéis. Umaequipedede-
senvolvimentodesoftwareémaiseficientesetodossãocapazesdefazerto-
dasasatividades. Considerecadamembrodasuaequipecomo“analista-
programador-tester”. Observoquesepararaequipeentreanalistas,progra-
madoresetesterséumamáinterpretaçãodomercadocomrelaçãoaoRUP.
Nasuaequipe,algumaspessoasterãoqualidadesdiferenciadas,masgeral-
menteelasnãosãorelacionadascomas“etapas”daconstruçãodosoftware,e
simcomoutrosfatoresmenosdeterministas.Vocêpodeterumapessoacom
excelentedesenvolturaparaconversarcomosusuários,outrapessoaconse-
guecodificarcomumarapidezacimadonormalecomqualidade! Outra
pessoapodeterumconhecimentoabrangenteparadarsoluçõesaproblemas
complexos.Aspessoaspossuemhabilidadesdiferenciadas,porém,comrela-
çãoàsetapasdedesenvolvimentoépreferívelquetodastenhamcapacidade
deexercê-las.Issofavoreceumamaiorprodutividade.
Duranteoartigo,vamosapresentarpráticaságeisparamelhoraracomu-
nicação,aprodutividadeegeraradocumentaç ãonamedidacerta.Tudoisso
éfundamentadonostrêscritériosdesucessodasuaaplicação:
1) Asoluçãoatendeaonegócio(qualidadeexterna).
2) Osoftwareéfácildemantereevoluir(qualidadeinterna).
3) Menorcustoeprazopossível(qualidadedoprojeto).
58

## Página 63

CasadoCódigo Capítulo4. OsPrincípiosdaModelagemÁgil
Tudooquevocêfaznoseuprocessodedesenvolvimentodeveterpropó-
sitosclarosesubstanciaisparaobteroscritériosacima.Muitasvezes,deter-
minadaspráticassãosoluçõesqueprocuramporumproblema. Outrassão
declaradamentecontraoscritériosacima.Avalieseuprocessodedesenvolvi-
mentoouamaneiracomoasuaequipesecomportaevejaseoseudia-a-dia
éfocadoemobteroscritériosapresentados.
4.1 Para o desenvolvimento de softw are, não
existe separação entre design e construção
Écomumaspessoasenvolvidasnastarefasgerenciaisdeumprojetodesoft-
wareacharemqueaEngenhariadeSistemasépróximadaEngenhariaCivil
ouEngenhariaMecânica.Nasengenhariastradicionais,existeseparaç ãoen-
tredesigneconstrução,naEngenhariadeSoftwarenãoexisteestaseparaç ão.
Quandoumedifícioéconstruído,ogerenciamentodeprojetotradicio-
nalfazsentido,poisparaessetipodeproduto(oprédio),énecessárioteruma
plantadetalhadaparapoderiniciaraconstruç ão.Nesseprojeto,queméres-
ponsávelpelaatividadededesignéumarquitetoouengenheiroquepossui
qualificaçõesintelectuaisdistintasdequemiráefetuaroprojeto(aconstru-
ção). Otrabalhodeconstruçãoserádesempenhadopelopedreiro,quenão
necessitateroconhecimentototaldaengenhariaparafazeroseutrabalho.
Essadivisãoaconteceporcontadascaracterísticastotalmentediferentesen-
treosdoistrabalhos:uméaltamenteintelectual,ooutroémaisbraç al.Um
engenheiropodeterumcustoalto.Opedreirotemumcustomuitomenor.
Umengenheiropodegerarsubsídiosparaotrabalhodeaté100pedreiros.
Dadoanaturezadoprojetocivil,élógicoqueexistaessadivisãodetra-
balhoentredesigneconstrução.Nessecenário,nãofazsentidoaspessoasdo
projetoserem“engenheiro-pedreiro”,comopodesernaengenhariadesoft-
ware.
Quandofalamosemsoftware,temosbasicamentequatroatividadesprin-
cipais:
1) Compreenderoqueousuárioquer.
59

## Página 64

4.1. Paraodesenvolvimentodesoftware,nãoexisteseparaçãoentredesigneconstruçãoCasadoCódigo
2) Definir como os elementos de software resolverão as necessidades do
usuário.
3) Escreveresseselementosdesoftwareeintegrá-los.
4) Testaroselementosehomologá-loscomousuário.
Antesdetudo,ressaltoqueessasatividadesocorremmilharesdevezes
dentrodeumprojetoenemsemprenaordemqueoquadrosugere(não
façoumaapologiaaodesenvolvimentoemcascata!).Porém,olhandoalista
apresentada,adiferen çaquetemoscomrelaçãoàengenhariaciviléquenão
existemdiferençasbruscasnonívelintelectualnecessárioparadesempenhar
essasatividades.Aatividadedeescreveroselementosdesoftwarenãoéin-
telectualmenteinferioràatividadedecompreenderoqueousuárioquerou
definiracolaboraçãoentreelementosdesoftware.Sãoatividadesdiferentes,
masnãotãodiferentescomootrabalhodoengenheiroedopedreiro.Oerro
quemuitasempresascometeméacharqueanalistasdesistemassãocomo
engenheirosciviseprogramadoressãocomopedreiros.Issoéumcompleto
absurdo!
Issotambéméumagrandeinjustiçacomosprogramadores.Programar
éaatividademaisintensa,aquemaisrequeraten ção,amaissujeitaaestresse
eaquemaisemergeriscosnodesenvolvimentodesoftware. Processadores
detextoeferramentasUMLaceitamqualquerbesteiraqueumanalistaes-
creveoumodela. Jáocompiladoréimplacável:ouvocêcodificadireitoou
aaplicaçãosimplesmentenãofuncionará. Ouvocêintegracorretamenteos
componentesouelessimplesmentenãoirãofuncionarjuntos. Oserrosde
programaçãosãoosmaisvisíveisdoprojeto,tantoqueatétemnome:BUG.
Olhandoporesselado,aposturalógicaseriaasempresasinvestiremmais,e
remuneraremmelhor,osprogramadores.Entretanto,écomumanalistasse-
remmaisbemremuneradosdoqueprogramadores,mesmoqueessadivisão
dospapéisnãofaçasentidoalgum.
60

## Página 65

CasadoCódigo Capítulo4. OsPrincípiosdaModelagemÁgil
4.2 Desenvolvimento de softw are: humanas ou
exatas?
Quandopegamosumprojetoefocamosnostrêscritériosdesucessocita-
dosnaintrodução,temosdificuldadeemsaberquaisqualidadesnósenossa
equipedevemterparabalancearessastrêsvariáveis.Basicamente,oqueque-
remoscomamodelagemdosistemaésatisfazerou“balancear”asnecessida-
desdosusuários,garantindoaqualidadeinternadosoftwareerespeitandoas
restriçõesdecustoeprazodoprojeto.
Determinados sistemas são críticos em funcionalidades aos usuários.
Capturaressasnecessidadeséumaatividadealtamentesocialquerequer
muitacomunicaçãoclaraeumagrandeproximidadecomosstakeholders.
Essetipodesistemarequerumamaioraten çãonaqualidadeexternaeacon-
centraçãomaiordamodelageméviradaparaoladodosusuários.
Jáoutrossistemasprezammaispelaqualidadeinterna. Quandotemos
quelidarcommuitacomplexidadetécnica,quegeralmenteocorreemsis-
temasquelidamcommilharesdegigabytes,milharesdeusuários,milhares
detransaçõeseprocessamentodistribuído,umpequenodesviodedisciplina
podelevarosistemaaocaos.Nessecaso,amodelagemévoltadaparaoas-
pectotécnico,emqueéobrigatórioconheceraestruturainternadoscompo-
nentes,asdependências,algoritmoscomplexos,etc.
Agora,tenhaemmentequeoscritériosdesucessoprecisamserequilibra-
dos.Todoprojetopossuirestriçõesdecustoeprazo.Nãotemostodotempoe
dinheirodomundoparafazerosoftware.Suamissãocomoumbom“mode-
lador”écontrolarasexpectativasdoclienteesempreavaliarquaisproblemas
realmentesãoPROBLEMAS.Fazerasoluç ãoatenderaonegócioéoponto
deparada.Saberfazerousuáriosepararaquiloqueédesejáveldaquiloqueé
imprescindíveltambéméumahabilidadeimportanteparaaequipedopro-
jeto.
Umadascoisasqueasmetodologiaságeistrouxeramàtonaéaimportante
participaçãodosusuáriosouclientesparaauxiliarnamodelagemdosistema,
sejaelaborandoummapamental,ourascunhandoumatela,outestandoum
releasequeacabou“desairdoforno”. Osusuários,ouclientesoustakehol-
derspossuemumpapelimportantíssimoparagerarasdemandascorretase
61

## Página 66

4.3. Acomunicaçãoricado“papelsobreamesa” CasadoCódigo
avaliaraqualidadedostrabalhosexecutados.Issorequerumacomunicaç ão
ricaentreoclienteetodososenvolvidosnoprojeto.
4.3 A comunicação rica do “papel sobre a mesa”
AlistairCockburnéumdosautoresdoManifestoÁgilde2001etambémé
umdosnomesquemaisdefendeumacomunicaç ãoaberta,intensaehonesta
dentrodosprojetosdedesenvolvimentodesoftware.Cockburnfoioprimeiro
autoradefenderqueatéadisposiçãofísicadasalaondeosmembrosdaequipe
trabalhampodeacarretaremproblemasparaosprojetos.
Emumdeseusartigos,Cockburnapresentouumresultadodeseuestudo
sobreaeficiênciadeartefatosemeiosdecomunicação.
Fig.4.1:Valordocanaldecomunicação.
Ográficodafigura 4.1nosmostraa“Eficiência”versusa“Temperatura”
demeiosdedocumentação.Alinhavermelhamostraasmídiasdedocumen-
taçãodeumprojeto.Comopodemosver,documentosempapelsãoosmenos
eficienteseosmais“frios”paraarmazenaredemonstraridéias.Aindanali-
nhavermelha,conteúdoemvídeos(imagemevoz)podeseraop çãomais
eficienteemaisamigávelparaoregistrodeinformaçõesdoprojeto. Atual-
62

## Página 67

CasadoCódigo Capítulo4. OsPrincípiosdaModelagemÁgil
mente,tenhoutilizadoapresentaçõescomimagemesom(screencasts)para
demonstrararquiteturasdeaplicações. Vejaumexemplonasreferênciase
notecomoumscreencastpodepouparaescritadeumdocumentodearqui-
teturade10a20páginaseaindamelhoraroentendimento.
Aindasobreográficodafigura 4.1,alinhaazulmostraasmídiasdecomu-
nicação,osmeiosqueduaspessoas,ouumgrupodepessoas,utilizampara
evoluiridéiasparaobomdesenvolvimentodoprojeto.Desenvolvimentode
softwareéextremamentedependentedecomunicação.Essacomunicaçãoé
críticatantonorelacionamentodoclientecomaequipecomotambémaco-
municaçãointernadaprópriaequipe.
Afiguranosdizqueopiormeiodecomunicaç ãoedocumentaçãosão
artefatossendotrocadosviae-maile,infelizmente,muitosprojetosutilizam
somenteessemeiopobredecomunicação.Estaéamaneiramenoseficiente
emaisfriadetrocaridéias.Jáummeioricodetrocaridéiaséacomunicaç ão
faceaface,preferencialmenteutilizandoumamaneiracompartilhadadede-
monstrargraficamenteasidéiascomoumpapelderascunhoouumquadro
branco.Aidéiaébemsimples:junteaspessoasnumasalaefaç a-ascolabo-
rarementresi,trocandoidéiasesentimentoscomoauxíliodeumamídia
gráficacompartilhada(umquadrobranco,umflip-chartoupapéisderascu-
nhocomlápissãoexcelentes). Aeficiênciadessatécnicaécomprovadaem
Workshopsderequisitoscomoclienteouemdiscussõesarquiteturaisdentro
daequipe.Oresultadodessasreuniõessãorascunhosquepodemserfeiosna
forma,massãoperfeitosparaopropósitodemodelagemdosistema.
4.4 Rascunhos: uma forma de modelagem efi-
caz
Semprequefalamosemrascunhos,aspessoas,principalmentenanossaárea,
ficamcomaquelaimpressãodecoisasmalfeitasouinformalidadeemexcesso.
Apesardenãoapoiarmuitoousodedefiniçõesdedicionários,nessecaso,
creioquesejainteressantedefiniroqueérascunho.
rascunho: s.m.,minuta;esbo ço;delineamento;trabalhopréviodereda ção
emquesefazememendasourasuras,antesdeserpassadoalimpo.
Essadefiniçãonosdeixaclaroquerascunhonãoprecisasernecessaria-
63

## Página 68

4.4. Rascunhos:umaformademodelagemeficaz CasadoCódigo
mentemalfeitoeneminformal.Apalavraquemaisgosteidessadefiniç ãoé
DELINEAMENTO,éexperimentarnosentidodetestarumamaneiramais
simplesdealgoquepodeserrefinadoemtempooportuno. Poralgumara-
zão,profissionaisdeinformáticapossuemumvíciopor“coisas”digitais.Nós
queremostudoemarquivosdigitaisqueestãoemalgumlugardoHD.Entre-
tanto,aindústriasobreviveuváriasdécadassemocomputador,eváriasáreas
deatuaçãovivemempazsemousodasmáquinas. Naáreadedesenvolvi-
mentodesoftware,nóspodemosutilizarmídiasquenãosãodigitais.Sempre
quepensoemrascunhoslembrodaobradobrasileiroOscarNiemeyer,um
dosmaioresnomesdaArquiteturaModerna.OscarNiemeyerobtevemuito
sucessorascunhandoprojetosdemaneiragenial.
Fig.4.2:RascunhosdoCongressoNacionalemBrasíliaporOscarNiemeyer.
Olhandoafigura 4.2vemosqueorascunhoéumaferramentainteressante
paraobservarofuturo.TalvezaobradoCongressoNacionaltenhademorado
anos,porém,osrascunhosquetraduziamaidéiaoriginaldoclienteficaram
prontosempoucosinstantes. Ointeressanteéqueaobrafinalficoumuito
parecidacomoquesequeriadefato.
Nodesenvolvimentodesoftware,nóspodemosaplicartécnicasparecidas,
masemescalamenor,aplicandoiteratividade(lembre-sequesãoengenharias
diferentes!).Fazeroclientenosauxiliarnamodelageméumadasmaneirasde
fornecerumavisãodaquiloqueseráosoftwarenofuturo,mesmoqueusando
artefatoslevescomoumrascunhonumapáginaA4.
64

## Página 69

CasadoCódigo Capítulo4. OsPrincípiosdaModelagemÁgil
4.5 Rascunhos para obter qualidade externa
no softw are
Afigura4.3temumrascunhodesenhadojuntocomoclienteecomaequipe
técnicadoERP(outrostakeholder)quefoicriadonareuniãodeconcep ção
ágildoprojetoFertFórtil.
Fig.4.3:RascunhosiniciaisdoprojetoFertFórtil:integraç ãoeseparaçãode
módulos.
Esseprojeto-exemplofoiapresentadonoartigo“EntregueSoftwareFun-
cionando! GerenciamentodeProjetoÁgil”destacolunanaediçãoanterior
(MundoJavanúmero26).Sóparasituaroprojeto,vejaalistadefuncionali-
dadesnafigura 4.4.
65

## Página 70

4.5. Rascunhosparaobterqualidadeexternanosoftware CasadoCódigo
Fig.4.4:ProductBackloginicialdaaplicaç ãoSFAFertFórtil
AaplicaçãoSFAFertFórtilbasicamenteéaemissãodepedidospelosven-
dedoresatravésdeumclienteremotodesconectado(notebook).Atualmente,
osvendedorespassamopedidoviafaxparaacentral.Comonovosistema,
elesutilizarãoumnotebookparacapturaretransmitiropedido.Essepedido
seráintegradonoERPdaFertFórtil.“Clienteremotodesconectado”significa
queatransaçãonãoéon-line,issoé,ovendedorpodecapturarpedidosdos
clientesodiatodoetransmitirtodosospedidosemlotequandochegaem
casa,utilizandoainternet.Ospedidossãoacumuladoslocalmentenonote-
bookdealgumaforma.
Essalistadefuncionalidadesdafigura 4.4éofrutodaconcep çãodosoft-
ware.Essetrabalhodeconcep çãoéumesfor çoinicialemquetentamospegar
“aidéia”geraldoproblemaqueosoftwarepretenderesolver. Éoprimeiro
contatoquevocêtemcomoclienteoucomosfuturosusuários.Aconcep ção
éumaatividadealtamentesocial,emquehabilidades,comoacomunicaç ão,
acuriosidade,ointeresseeofoco,entreoutrascapacidadesinterpessoaise
não-técnicas,sãopostasàprova.Masmaisimportanteparaesteartigoéque
nasreuniõesiniciaisdeconcep çãonósmodelamosmuito. Nessasreuniões
surgemosmodelosmaisimportantesparaagarantiadaaderênciadaaplica-
çãoàsnecessidadesprincipaisdocliente.
66

## Página 71

CasadoCódigo Capítulo4. OsPrincípiosdaModelagemÁgil
Nafigura 4.3temosumresumogeraldaaplicaç ão. Comojádissemos,
todasaspessoasinteressadasnessediagramacontribuíramparaaelaboraç ão
dele. OpessoaldoERPmencionouqueaintegraç ãocomelesocorreatra-
vésdeconectoresHTTPemXML(Webservices). Essaéumainformaç ão
importanteparaavaliarmosaintegraçãoeissoconstadeumamaneirabem
simplesnodiagramanessemomento. Detalhessobreessaintegraç ãoserão
levantadosmaisadiante(maisespecificamentenaiteração2,videfigura 4.4).
Outrasinformaçõesimportanteslevantadasnessediagramasão:adivi-
sãodemódulosdaaplicação,adescobertadanecessidadedeummódulode
interfacedetransmissãoeodelineamentodoescopodosistema.Sobreoes-
copo,alinhapontilhadaverticaldeixaclaroquenossafun çãoésópreparar
paraqueosdadosentremconsistentesnoERP,porém,apartirdisso,toda
responsabilidadepassaaserdoERP.
4.6 A profundar em detalhes antecipadamente
éRUIM!
Quandofalamosemmodelagem,sejadeprojetosdeengenharia,deumaem-
balagem,deumacasaoudesoftware,éimportanteteremmentequaléo
objetivodomodeloquetrabalhamosnomomento.Umadasgrandesdúvidas
dasequipesdeprojetoéquãolongedevemosnosaprofundaremdetalhes.
Pararesponderaessadúvida,vamosanalisarmaisumavezafigura 4.3,mas,
dessavez,tenteresponderàsperguntasaseguir.
1) Qualéomomentodoprojeto?
2) Qualéadúvidaquetenho?
3) Quempoderiamodelarissojuntocomigoparaobterasrespostas?
4) Qualéomodelocerto?
Respondendoàsperguntasfocandoafigura 4.3:estamosnoprimeiromo-
mentocomoclienteequerendosaberoqueéoprojeto,descobrindoosobje-
tivos,oescopo,asfuncionalidades,osriscos.Logicamentequemnosajudará
67

## Página 72

4.6. AprofundaremdetalhesantecipadamenteéRUIM! CasadoCódigo
aobteressasrespostaséocliente,eparacompreenderasimplicaçõesdainte-
graçãocomoERP(umdosgrandesriscos),osrepresentantesdesserecurso
tambémestãopresentes.Tendoessaspessoasnasala,opontoprincipaldessa
reuniãoéterumacompreensãodeALTONÍVELdosistema,enãotodosos
detalhes.Nãoéconvenientenessareuniãodiscutirasminúciasdaintegraç ão
comoERP.Detalhesserãoadicionadositerativamenteedemaneiraincre-
mentaldurantetodooprojeto.
Afigura4.3 éummodelodealtonível. Modelossãomanifestaçõesde
decisõesoupercep ções. Nessecasoéamanifestaçãodapercep çãodainte-
gração,dosmódulosedoescopoinicialdoprojeto.
Umdosvaloresdamodelagemágilé“modelarcomumpropósito”e,mui-
tasvezes,modelarcomumpropósitosignificabuscaroscritériosdesucesso
doprojetoapresentadosnoquadro1.Vocêmodelaparaqueosoftwareatenda
aousuário(comofizemosnafigura 4.3),ouparaqueosoftwaretenhaquali-
dadeinterna,ouparareduzircustoouprazodoprojeto.Éaltamentequesti-
onávelquandovocêmodelasóparacumprir“etapas”doprocessooumodela
porqueseuprocessodedesenvolvimentoexigeomodelo. Comojáfaleino
artigo“UMLnãoéDocumentação”naMundoJavanúmero19:vocêmodela
oqueprecisasermodelado.
68

## Página 73

CasadoCódigo Capítulo4. OsPrincípiosdaModelagemÁgil
Fig.4.5:Protótipodateladepedidosnonotebook.
69

## Página 74

4.7. Nãovolteparacasaparaescreverdocumentosderequisitos! CasadoCódigo
Umadasquestõesrelevantesé“Qualéomodelocerto?”. Éimportante
ressaltarquetemosumaquantidadeinfinitademaneirasdepodemosmo-
delar. Umaprovadissoéoprotótipodateladepedidosdafigura 4.5. Este
protótipofoielaboradonamesmareuniãocomocliente,poisemissãodepe-
didosfazpartedaprimeiraiteraçãodoprojeto(figura 4.4).Umesbo çofeito
deformarápidaeconjuntacomaspartesinteressadaséummeiomuitoefi-
cientedecapturarrequisitosedescobrircomoatingiroobjetivodefazerum
softwarecomqualidadeexterna,queatendaàsexpectativasdosusuários.
4.7 Não volte para casa para escrever docu-
mentos de requisitos!
Avantagememsefazercomqueosclienteseusuáriosparticipemdamode-
lagemdosistemautilizandoartefatoseferramentassimples,comorascunhos
empapelounoquadrobranco,épromoveracolaboraç ãoeganharagilidade
nacapturaderequisitos. Porém,algumaspessoasouempresassofremde
excessodecerimônia,deformaanãoreconhecerartefatosempapelcomo
“válidos”noprocessodedesenvolvimento. Issolevaaumaburocratização
desnecessárianacapturaderequisitos.
Muitaspessoaslevantamrequisitosemartefatosinformaisparadepois
transformá-losemcasosdeuso,especificaçõessuplementares,protótipos,
documentosderegrasdenegócioeoutrosquando“voltamparacasa”,isso
é,preenchemessestemplatesdepoisdasreuniões,formalizandoolevanta-
mento. Comohouveumatransformaçãodeartefatosétípicaumarevisão
comoclienteparaobteruma“aprovação”.Oproblemaéqueessaaprovação
nuncaocorre!Aoverosartefatostransformadosocliente“selembra”demais
requisitosquesãomaisumavezcapturadosemartefatosinformaiseociclose
repetemuitasvezes.Comisso,levam-sesemanaspara“aprovarosrequisitos”
eumtempopreciosoéperdido.
Aidéiadetrabalharcomrascunhosérapidamentetransformá-losem
“softwarefuncionando”(numespaçodeumasemana)deformaquedapró-
ximavezquevocêencontraroclientevocêentregarásoftwareaserhomo-
logadoenãodocumentosaseremaprovados. Nãopercatempoaprovando
documentosderequisitosdepoisqueforamlevantados,poiselesnuncase-
70

## Página 75

CasadoCódigo Capítulo4. OsPrincípiosdaModelagemÁgil
rãoaprovados,emesmoquesejam“aprovados”oclientepoderámudarde
idéiaquandoverrealmenteoqueelequerdefato(osistema!). Lembre-se:
documentosderequisitossãoabstrações! Issotambémnostrazadefiniç ão
abaixo:
SOFTWAREFUNCIONANDOéomelhorartefatoparalevantamentode
requisitos
Comojádefendiváriasvezesaquinosartigosdarevista,desenvolvimento
iterativoéentregaconstantedesoftwareprontoparaosstakeholders.Dessa
forma,osusuáriosolhamosoftwareesolicitamalteraçõesnosoftwareenão
emdocumentos.Softwareéaúnicacoisaconcretaquerealmentevalidamos
comosusuários.
Muitosartefatospodemserusadosparadocumentarrequisitos.Osrascu-
nhosempapel,umarquivoMP3comoconteúdodareuniãodelevantamento,
protótiposvisuais,casosdeuso,documentosemtexto,etc.Documentosde
requisitostêmcomoobjetivoregistraroqueosusuáriosesperamdaaplicação
independentedasoluçãotécnica.Issofazcomqueessesdocumentossejam
simpleserápidosdeseremelaborados.Vocêpodeusarváriosdelesparare-
gistrarosanseiosdosusuários(aprática“Utilizeoartefatocorreto”doAgile
Modeling). Masmaisimportanteéqueessesartefatossejamelaboradosna
reuniãodelevantamentoenão“emcasa”. Sevocêquermodelarumavisão
geraldosistema,useummodelocomoodafigura 4.3.Sevocêquermodelar
umatela,useumrascunhocomodafigura 4.5.Sevocêquerdocumentaruma
interaçãocomousuário,escrevaumcasodeusoalimesmonareunião.Saia
dareuniãocomrequisitoslevantadosedocumentados(prafalaraverdade
nãoexisteseparaçãoentreessesdois),depoisdisso,éfazerosoftwarepara
cumpriroplanejamentodaiteração.
4.8 Utilizando a modelagem para obter quali-
dade interna
Atéopresentemomentoutilizamosamodelagemágilparamelhoraredo-
cumentardecisõesfocadasnaqualidadeexternadaaplicaç ão.Usamosuma
modelagemconjuntacomocliente.Amodelagemágiltambémpodeseruti-
lizadadentrodasuaequipededesenvolvimento. Acomunicaç ãoentreos
71

## Página 76

4.8. Utilizandoamodelagemparaobterqualidadeinterna CasadoCódigo
membrosdaequipesegueomesmopadrãodográficoapresentadonafigura
4.1.Acomunicaçãofaceafaceecomumrascunho(mídiacompartilhada)é
amaneiramaisindicadaparadiscutiredisseminaridéiasdentrodotime.
Umadaspráticasquetenhoaplicadoemmuitosprojetossãoreuniões
paradiscussãodearquitetura. Quandotemosumaequipedesenvolvendo
software,aspessoastêmatendênciadefocarnosseusprópriosproblemas
semdiscutiremgrupoasquestões.Paraisso,marcarumareuniãoespecifi-
camenteparadiscutiressaspendênciasésaudávelparaoprojeto.
Semprequefalamosnoladotécnicodoprojetofocamosemboaspráti-
casdeprogramaçãoOOe,comisso,umsistemacomboaqualidadeinterna
possuibasicamenteasduascaracterísticasdeumbomdesign:
1) ALTACOESÃO;
2) BAIXOACOPLAMENTO.
Énessasduas“medidas”quevocêdevefocarnodesigndosseusobje-
tos. Nessasreuniõesdearquitetura,juntamosaequipeeadinâmicanãoé
muitodiferentedareuniãocomosclientes.UsamosmuitopapelA4emui-
tosdesenhosnoquadrobranco.Nessasreuniões,surgemmodeloscomoos
retratadosnasfiguras 4.6e4.7.Nessesencontros,nós“falamos”UML.UML
éumalinguagem,elaserveparacomunicação!Nessecenárioéquevemoso
valoremterumanotaçãopadrão:oqueummembrodaequipe“fala”emum
rascunhotodoscompreendem.
72

## Página 77

CasadoCódigo Capítulo4. OsPrincípiosdaModelagemÁgil
Fig.4.6:Rascunhodediagramadesequência.
73

## Página 78

4.8. Utilizandoamodelagemparaobterqualidadeinterna CasadoCódigo
Fig.4.7:Domainmodeldaaplicação.
FerramentasUMLtambémsãoúteis(sim,eutambémusoferramentas
UML!).Determinadosmodelossãoimportantesedevemsermantidoscomo
documentaçãopermanentedoprojeto. Muitosdelesconstamnumdocu-
mentodearquitetura.Porém,modelossãonaturalmentedifíceisdemanter.
Seseumodeloestámuito“profundo”atendênciaéquefiquemaisdefasado
comocódigo.Amodelagemágilpossuiumprincípiochamado“TravelLight”.
Nãoseicomotraduzirissodemaneiraefetiva,masaidéiaé“nãoviajepara
muitolongecomseumodelo”. Oprincípionosdizquemantermodelosé
difícil,epodesetornarmaisdifícilsevocêtivermuitosmodelosemuitode-
talhados. Talveztrêsouquatromodelosquefornecemumavisãogeralda
análise,daarquiteturaedodesignsãosuficientesparamelhoraracomuni-
caçãodaequipe.Éerradopensarquequantomaisdocumentaç ãomelhor.A
documentaçãoprecisaserenxuta.Outrosmodelospodemsersimplesmente
descartadosdepoisquecumpriramseupapeltransformando-seemcódigo.
74

## Página 79

CasadoCódigo Capítulo4. OsPrincípiosdaModelagemÁgil
4.9 C onceitos sempre prov ados com código
Umadasdiscordânciasquemuitaspessoastêmcontrametodologiaságeisé
ofoconocódigo.Porém,énocódigoqueaaltacoesãoebaixoacoplamento
oferecembenefícios. UmdosprincípiosdaModelagemÁgilé:“Provecom
Código”. Issoé,osmodelossãosomenteumaabstraçãodaquiloquevocê
estáconstruindodefato.Masseráqueomodeloestácorreto?Seráqueeleé
implementável?Parasaberessarespostaénecessário“provaromodelocom
código”.
Éimportanteressaltarqueaatividadedemodelagemvisaobterumaqua-
lidadedocódigoenãodomodelo.Nósmodelamosparaocódigo.Umaboa
modelagemtemcomoobjetivoobterumbomcódigo,enãoumbommo-
delo.Aqualidadesempredevefocarocódigoeosimportantesconceitosde
altacoesãoebaixoacoplamento.A“beleza”domodelonãoénecessariamente
qualidade.
Outropontoéquevocêtambémpodemodelardiretamentenocódigo.
ModelosemUMLpodemteajudarbastantenumaconversadareuniãode
arquiteturaouparateravisãogeraldeummódulo.Vocêpodetambémapli-
carDomain-DrivenDesigncomUMLconformedemonstradonafigura 4.7.
Poroutrolado,vocêtambémpodemodelardiretamentenocódigoutilizando
apráticadaprogramaçãoemparesdoExtremeProgrammingetambématra-
vésdeTDD(Test-DrivenDevelopment).Comojáciteiaqui,nãoexistesepa-
raçãoentredesigneconstruçãonaEngenhariadeSoftware.Nosoftware,não
precisamosnecessariamenteda“planta”parafazerocódigo.
Olhandoparaasperguntasapresentadas,ocódigopodeserconsiderado
ummodelo.Modelageméumaatividadedecriaçãoenãodepreenchimento
detemplatedeartefato.
4.10 Conclusão
Esteartigodemonstrouqueartefatossimplespodemserutilizadosparaapli-
carboaspráticasdemodelagem.Modelageméumaatividadeemgrupo,na
maioriadasvezes,etudoquefazemosdeveserfocadoemmelhoraraquali-
dadeinterna,aqualidadeexternaouaprodutividade.Modelarsimplesmente
para“teromodelo”deveserevitado! Muitasoutraspráticasevaloressão
75

## Página 80

4.11. Referências CasadoCódigo
importantesna“AgileModeling”erecomendofortementeoestudodasrefe-
rênciaslistadas.
Masomaisimportantedetudoéfocarnasatividadesdodesenvolvimento
enãonosartefatoscriados. Quandovocêlevantarequisitos,aatividadede
conversarcomousuário,obterinformaçõeseenriqueceroconhecimentoé
maisimportantequeoscasosdeuso,protótipos,modelosquesurgiremdessa
atividade. Omesmovaleparaumamodelagemdedesign. Oimportanteé
acriatividadeparasolucionarasdependênciasdosobjetos,aseparaç ãodos
conceitos,asmensagenstrocadas.Omodelodedesignésóumamanifestaç ão
dessasdecisões.Atomadadessasdecisõesémaisimportantequeamanifes-
taçãodelas.
Essealertaéimportante,poismuitaspessoasconfundemaatividade“le-
vantamentoderequisitos”com“preenchimentodostemplatesdeartefatos
derequisitos”.E,piorainda,muitasvezesessepreenchimentodeartefatosé
feitosimplesmenteparacumprirtarefasinúteisdeumprocessodedesenvol-
vimentopesado,burocráticoequeroubaacriatividadedaspessoas.
ASATIVIDADESDENTRODODESENVOLVIMENTODESOFTWARE
SÃOMAISIMPORTANTESQUEOSARTEFATOSGERADOS.
Tomecuidadocomprocessosdedesenvolvimentoqueparecemorgani-
zados. Muitosdelesnãosãoorganizadosdefato. Oqueoclientequeréo
softwareenãoosdocumentosqueabstraemoqueseesperadosoftware.De
fato,muitosdosmeusartefatossãorascunhosdeDomainModels,rascunhos
decasosdeuso,rascunhosdeprotótiposdetela,rascunhosdediagramade
atividades.TudoempapelA4,desenhadosjuntocomocliente(ecomisso,
automaticamenteaprovadosporele,pelomenosatéeleverosoftware).Com
essesrascunhosnamão,voltoparacasaetransformoissoemsoftwarefunci-
onando,seguindoboaspráticasdeengenharia.
4.11 Referências
• Muito sobre separação entre Design e Construção: http://www.
martinfowler.com/articles/newMethodology.html
• AMBLER,SCOTT,2002.AgileModeling:www.agilemodeling.com
76

## Página 81

CasadoCódigo Capítulo4. OsPrincípiosdaModelagemÁgil
• COCKBURN,ALISTAIR.www.alistair.cockburn.us
• VídeoArquiteturaHotMotors:www.aspercom.com.br/hotmotors
• OscarNiemeyer:http://www.niemeyer.org.br/
• EVANS,ERIC,2004.Domain-DrivenDesign
• IBMRATIONAL,2007.RationalUnifiedProcess7.0
77