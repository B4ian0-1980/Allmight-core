---json
{
  "id": "jsf_eficaz_as_melhores_pr_ticas_para_o_desenvolvedor_web_java",
  "title": "JSF Eficaz As melhores práticas para o desenvolvedor web Java",
  "categoria": "03-linguagens",
  "subcategoria": "java",
  "resumo": "**Arquivo Original:** `JSF Eficaz As melhores práticas para o desenvolvedor web Java.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "desenvolvedor",
    "eficaz",
    "java",
    "jsf",
    "linguagens",
    "melhores",
    "para",
    "ticas"
  ],
  "perguntas_tipo": [
    "Como utilizar JSF Eficaz As melhores práticas para o desenvolvedor web Java?",
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

# JSF Eficaz As melhores práticas para o desenvolvedor web Java

> **Arquivo Original:** `JSF Eficaz As melhores práticas para o desenvolvedor web Java.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 2

© Casa do Código
Todos os direitos reservados e protegidos pela Lei nº9.610, de 10/02/1998.
Nenhuma parte deste livro poderá ser reproduzida, nem transmitida, sem auto-
rização prévia por escrito da editora, sejam quais forem os meios: fotográficos,
eletrônicos mecânicos, gravação ou quaisquer outros.
Casa do Código
Livros para o programador
Rua Vergueiro, 3185 - 8º andar
04101-300 – Vila Mariana – São Paulo – SP – Brasil

## Página 5

CasadoCódigo
SobreoA u t o r
HébertCoelhodeOliveiratrabalhahámaisde10anoscomdesenvolvimentode
softwares.Possuiascertificações SCJP,SCWCD,OCBCD,OCJPAD.
Criadordobloghttp://uaiHebert.comvisualizadopor170paísestotalizando
maisde500milvisualizações emseus2anosemeiodevida,éaindaautordofra-
meworkEasyCriteria(http://easycriteria.uaihebert.com)queajudanautilizaçãoda
CriteriadoJPA,sendotestadocomHibernate,OpenJPAeEclipseLinkecom100%
decoberturanostestes.
FoirevisordeumlivroespecíficosobrePrimefacesecriadordepostsemseublog
comaplicações completasutilizandoJSF.EscreveuumpostsobreJSFcomdiversas
dicasquealcançoumaisde3milvisualizações noprimeirodia,umpostcom18
páginas,quefoiaideiaoriginaldesselivro.
PósGraduadoemMITEngenhariadeSoftware-desenvolvimentoemJava.A t u -
almenteatuacomoprofessorparaocursodePósGraduação,ensinandooconteúdo
deJavaW e b(JSP,Servlet,JSFeStruts)etópicosavançados,comoEJB,SpringeW e b -
Services.
i

## Página 7

CasadoCódigo
Agradecimentos
PrimeiramenteagradeçoaDeuspormecapacitarparaescreverolivro.
Agradeçoàminhaesposaportodasuapaciênciaduranteoprocessodeescrita
desselivro,eporsempremeanimarnosmomentosmaisdifíceis.
Aosmeuspaisquesempremeapoiaram. Soufeliztambémpelasminhasso-
brinhasque,mesmopequenas(LouanneeFernanda),participaramnoprocessodo
livro-afinalestiveramduranteumasemanaemmeusbraçosenquantoeuescrevia
olivro.Nãopossoesquecerdaminhairmãquesemprebrigacomigo.=D
Finalmente,agradeçoaopessoaldaCasadoCódigopormedaremessaoportu-
nidadeeapoiodurantetodooprocesso.
iii

## Página 9

CasadoCódigo
SobreoLivro
OJSFéumatecnologiamuitoútilepráticadeseraplicada,masquediversasvezesé
malutilizada.Muitasvezesporfaltadeconhecimentodequemestruturaaaplicação,
oprojetoacabaficandolentoededifícilmanutenção.
Estelivrotemporobjetivodardicaseexplicarconceitosquesãonecessáriospara
queumaboaaplicaçãoutilizandoJSFsejacriada.Àsvezesomínimodetalhequevai
desdecomochamarummétodooupassarumvalorparaumManagedBeanouaté
mesmoutilizarumconverterpodelevarahorasperdidasdepesquisasnainternete
testesnaaplicação.
Esselivrodemonstraráboaspráticas,dicaseacorretautilizaçãodoJSFemdi-
versosaspectosediferentessituações.
v

## Página 11

CasadoCódigo Sumário
Sumário
1 Escolhasqueafetamodesenvolvimentodaaplicação 1
1.1 SuspeiteseaaplicaçãoestáusandobemoJSF . . . . . . . . . . . . . . 2
1.2 Devoseguirtodasasdicasaopédaletra? . . . . . . . . . . . . . . . . 2
U s eosescoposcorretamente 5
2 @RequestScopedparaescoposcurtos 7
3 Mantenhaobeannasessãocom@SessionScoped 11
4 Entendaonovo@ViewScoped 17
5 Crieescoposlongosecustomizáveiscom@ConversationScoped 23
6 Apraticidadedoescopo@Dependent 27
7 Guardedadosparatodaaaplicaçãocomo@ApplicationScoped 29
8 Quandousaro@NoneScoped? 33
9 ExibindoObjetoseMensagensapósRedirecteoFlashScoped 37
CuidadoscomseusManagedBeans 43
10 ColocandológicaderenderednoMB 45
11 InicializandoObjetos 49
vii

## Página 12

Sumário CasadoCódigo
12 InjetandoManagedBeans 55
13 TargetUnreachable:EnfrenteaNullPointerExceptiondoJSF 59
14 Cuidadocomo“Valueisnotvalid” 63
Front-endsJSF 65
15 UtilizarJSPouxhtml? 67
16 Utilizandoimagens/css/javascriptdemodossimples 71
17 BoautilizaçãodoFacelets 75
18 EnviarvaloresparaoManagedBean 81
18.1 Envievalorcomoparâmetropelof:setPropertyActionListener . . . . 82
18.2 Envievalorcomoparâmetro. . . . . . . . . . . . . . . . . . . . . . . . 83
18.3 EnvievalorporBinding. . . . . . . . . . . . . . . . . . . . . . . . . . . 83
19 Temasdinâmicos 85
20 Oqueeuuso?ActionouActionListener? 87
20.1 Redirecioneousuáriocomaction . . . . . . . . . . . . . . . . . . . . . 87
20.2 T r a t eeventoscomactionListener . . . . . . . . . . . . . . . . . . . . . 88
Aproveiteasbibliotecasdecomponentes 91
21 Primefaces 93
21.1 DataTablecomseleçãocomumclick . . . . . . . . . . . . . . . . . . . 93
21.2 DragandDrop. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
21.3 Notificador . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
21.4 A u t oComplete. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
21.5 Poll. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
21.6 Considerações finais. . . . . . . . . . . . . . . . . . . . . . . . . . . . .109
22 TemasDinâmicoscomPrimefaces 111
viii

## Página 13

CasadoCódigo Sumário
23 ComponentesdoPrimefacesnãoAparecem 117
24 Richfaces 119
24.1 DataTablecomColunasCongeladas. . . . . . . . . . . . . . . . . . . . 119
24.2 T o o lTip. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
24.3 Log. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
24.4 PanelMenu. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
24.5 Repeat. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
24.6 Considerações Finais . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129
25 Icefaces 131
25.1 Menu . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
25.2 Dialog . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134
25.3 RichText. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136
25.4 Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
25.5 Considerações Finais . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139
26 EvitemisturarasImplementações/BibliotecasdeComponentes 141
27 Nãofaçapaginaçãonoladodoservidor 143
FuncionalidadesricascomJSF,segurançaeotimizaçãodoJSF 155
28 FacilitandoousodoAjax 157
28.1 Sempreindiquequearequisiçãoestáacontecendo . . . . . . . . . . .160
28.2 Dêmensagensdefeedbackparaousuário. . . . . . . . . . . . . . . . 161
28.3 Previna-sedasváriasações dousuárioemrequisições assíncronas. . 162
28.4 CuidadoaousarManagedBeansRequestScopedcomA j a x. . . . . . 163
29 InternacionalizaçãoeLocalizaçãodasuaaplicação 165
29.1 Permitaqueousuáriomudeoidioma . . . . . . . . . . . . . . . . . . 167
30 UtilizandorecursosdentrodeumConverter 173
30.1 AcesseumManagedBeanprogramaticamenteatravésdeExpression
Language . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 173
ix

## Página 14

Sumário CasadoCódigo
31 CDIcomJSF 175
32 Eviteo“CrossSiteScripting”emseusistema 177
33 Otimizandoanavegaçãoeperformance 179
Debugeinspeçãodeaplicações 181
34 Limpezadecomentáriosedebug 183
34.1 Escondaoscomentáriosdapágina. . . . . . . . . . . . . . . . . . . . 183
34.2 Debugdoscomponentes . . . . . . . . . . . . . . . . . . . . . . . . . . 184
35 Organizefuncionalidadesporambientedoprojeto 187
36 RefreshautomáticodosArquivos 191
37 RefreshautomáticodosArquivos 193
Versão: 16.2.5
x

## Página 15

Capítulo1
Escolhasqueafetamo
desenvolvimentodaaplicação
V o c êjásentiuumdesânimoporterquealterarumafuncionalidade? Outerque
procurarporaquelebugqueestáaparecendohámeses?Muitasvezesessedesânimo
podeacontecerpordecisões erradasduranteacriaçãodaaplicação. Apiorparteé
saberqueaoalterarumtrechodocódigo,podemosterefeitoscolateraisindesejados
emoutroslocais.
Épossívelencontrardiversosproblemastécnicosouatémesmoconceituaispor
escolhaserradasaoiniciarodesenvolvimentodeumanovaaplicação. Énecessário
estruturá-lacomconhecimentodasferramentasutilizadas;umaaplicaçãoquetem
frameworksmalutilizadosserárefémdelesparasempre.

## Página 16

1.1.SuspeiteseaaplicaçãoestáusandobemoJSF CasadoCódigo
1.1 Suspeites ea aplicação está usando bem oJSF
Certavezmefoidadaatrivialtarefademudarumaabadelugar.Atarefaeraapenas
pegarumaabaqueestavaentreoutraseexibi-laprimeiro.
Figura1.1:ExibirprimeiroaabaPessoa
Afigura1.1mostracomoeraolayoutecomo,teoricamente,seriasimplespassar
aaba Pessoaparaserexibidaantesdaaba Carro.
Oqueseriaumatarefade15minutossetransformouemumacaçaàsbruxasde
3dias.Aoalterarasabasdeposição,diversoserroscomeçaramaacontecer.Opri-
meiroerroqueapareceufoiocruel NullPointerException.Comoumdesen-
volvedorpoderiaimaginarque,aoalterarumaabadelugar,esseerroiriaaparecer?
OprincipalproblemadessaaplicaçãoeramosescoposdosManagedBeans.T o -
doseram SessionScopededependiamdeinformações emcomum. Aoentrar
naprimeiraaba( Carro),diversosdadoseramarmazenadosnasessão eutiliza-
dosemoutrasabasdiretamentenoManagedBeanquecuidavadaabaCarro. Ao
trocarasabasdelugar,diversasinformações não forampreenchidasnesseMana-
gedBeanequandooManagedBeandaabaPessoafosseacessaressasinformações, a
NullPointerExceptionaparecia.
Infelizmenteesseeraumdosproblemasdaaplicação; outroeraqueaocarre-
garatelatodasasinformações detodasasoutrasabaseramcarregadas.Eramuita
informaçãoemmemória,eerroscomeçavamaacontecersemexplicação.
Às vezesaescolhaéfeitapelosdesenvolvedores,outrasvezesporalgumdesen-
volvedorquefala:“assimsemprefuncionouevamoscontinuardessemodo”.Épre-
cisoentenderoframeworkcomoqualestamostrabalhando,parasóentãoapresentar
argumentosemelhorestécnicasnacriaçãodaaplicação.
1.2 De v oseguir todas a sdicasa op éd aletra?
Não.V o c êdevemanterseuespíritocrítico.Olivrovaiabrirsuamenteparaquevocê
evitecairemarmadilhasjátradicionais,mashásimsituações emquevocêacaba
2

## Página 17

CasadoCódigo Capítulo1.Escolhasqueafetamodesenvolvimentodaaplicação
subvertendooframework.
3

## Página 19

P a r t eI
U s eosescoposcorretamente
OJSFéumframeworkquetemumcomportamento“component-based” .Ele
temporcaracterísticaprincipalofatodequeapáginairábuscarainformação no
ManagedBean.
CadaManagedBeantemumtipodeescopoidealparacadasituação.Éfácilen-
contrarapologiasaousoindiscriminadodo SessionScoped,assimcomoadefesa
acirradadequeoidealparatodososcasoséo RequestScoped.V a m o sanalisar
cadacasoeverqualamelhorsoluçãoparacadaabordagem.
AnteséimportantesalientarosdoismodosdesedeclararumManagedBean.É
possívelutilizarumManagedBeanporCDIqueutilizaopacote javax.injectou
porManagedBeanencontradonopacote javax.faces.bean. Existediferença
entrecadacontextoqueforutilizadoeamboscomvantagensedesvantagens.Por-
tanto,éimportanteconhecerosescoposparaconseguirusá-loscorretamente.

## Página 21

Capítulo2
@RequestScopedparaescopos
curtos
Oescopo RequestScopedfuncionacomoumsimplesHTTPrequest.OMana-
gedBeannãomanteráseuestadoentreaschamadasdousuário.

## Página 22

CasadoCódigo
Figura2.1:RequestScopedManagedBeantratandorequisição
Aimagem2.1mostracomooJSFirátratararequisiçãoaoseutilizarumMana-
gedBeanRequestScoped:
1)Ousuárioiniciaráumarequisição;
2) OManagedBeanprocessaráasinformações necessárias;
3)AsinformaçõesdoManagedBeanficamdisponíveisparaoprocessamentodatela;
4) CasoalgumvalortenhasidoarmazenadonoManagedBean,essasinformações
serãodescartadas;
Acadarequisição, umanovainstânciadoManagedBeanserácriadaeusada,
dessamaneira,nãoháocompartilhamentodasinformações doManagedBeanentre
asrequisições.
import javax.faces.bean.*;
@ManagedBean
@RequestScoped
public class RequestScopedMB {
private int numeroDeAcessos;
public int getNumeroDeAcessos() {
return ++numeroDeAcessos;
}
8

## Página 23

CasadoCódigo Capítulo2. @RequestScopedparaescoposcurtos
public void setNumeroDeAcessos(int numeroDeAcessos) {
this.numeroDeAcessos = numeroDeAcessos;
}
}
Aoanalisarmosocódigo daclasse RequestScopedMB épossívelverque,
mesmoaclassetendooatributoprivado numeroDeAcessos,oseuvalorserásem-
preigualacadachamada.NotequenométodogetNumeroDeAcessos,ovalor
do numeroDeAcessoséalterado.Nãoimportaquantasvezesapáginasejaapre-
sentadaaousuário,ovalorretornadoserásempreum.
Bo aprática
Os ManagedBeans por padrão são @RequestScoped e com
isso, aanotação pode ser omitidanadeclaração dosbeans. Consi-
derecomoboapráticasempredeixarseuManagedBeananotadocom
@RequestScoped,poiscomelaficaclaroparaquemlêocódigoqual
éoescopodoManagedBean,mesmoparaumdesenvolvedorqueacaba
deentrarnoprojetoeaindanãoconheceoJSF.
OmelhorusodeumManagedBeannoescopode r e q u e s téemtelasquenão
necessitamdechamadaAJAX,ouemdealgumobjetosalvonamemória.
Considereumasituaçãonaqualnãoénecessárionenhumainformaçãoadicional
deumobjetoemmemória.Bastaenviarosdadospresentesdoformulárioqueum
objetoserácriadoeestaráprontoparaserpersistidonobancodedados.
9

## Página 24

CasadoCódigo
Figura2.2:UtilizandooRequestScopeddeumbommodo
Afigura2.2mostraumexemplodequandopoderíamosutilizarumManaged-
Bean @RequestScoped. Notequeafigura2.2tratadeumateladeinclusão de
dados,enãonecessárionenhumdadojáprocessadoanteriormente.
U mManagedBeandotipoRequestScopedéconsideradoThreadSafe,ouseja,
elenão teráproblemasrelacionadosaváriosusuáriosacessandoomesmoMBao
mesmotempo. Éumaboautilização nageração derelatório,poisnão haveriam
duaspessoasusandoamesmainstânciadoManagedBeaneorelatórioteriacomo
terinconsistênciadedados. Outraboautilização seriaaoenviardadosparauma
outratela;essaoutrapoderiaexibirtodososdadosdoobjetopresentenorequest.
10

## Página 25

Capítulo3
Ma nt e n h aobeannasessãocom
@SessionScoped
OsManagedBeans @SessionScopedtêmomesmocomportamentodasessãoweb
(HttpSession). T o d oatributodeumManagedBeanSessionScopedteráseuvalor
mantidoatéofimdasessãodousuário.

## Página 26

CasadoCódigo
Figura3.1:SessionScopedManagedBeantratandorequisição
Aimagem3.1mostracomooJSFirátratararequisiçãoaoseutilizarumMana-
gedBeanSessionScoped:
1)Ousuárioiniciaráumarequisição;
2) OManagedBeanprocessaráasinformações necessárias;
3)AsinformaçõesdoManagedBeanficamdisponíveisparaoprocessamentodatela;
4) T o d ainformaçãoquefoiatribuídaaoManagedBeanserámantidaenquantodurar
asessãodousuárionoservidor.
T o d ovalorqueforalteradoemumManagedBeanSessionScopedserámantido,
etodososvaloresdessebeanserãomantidosnamemória.
import javax.faces.bean.*;
@ManagedBean
@SessionScoped
public class SessionScopedMB {
private int numeroDeAcessos;
public int getNumeroDeAcessos() {
return ++numeroDeAcessos;
}
public void setNumeroDeAcessos(int numeroDeAcessos) {
this.numeroDeAcessos = numeroDeAcessos;
12

## Página 27

CasadoCódigo Capítulo3.Mantenhaobeannasessãocom@SessionScoped
}
public boolean isAdministrador(){
return usuario.getPerfil().equals(Perfil.ADMINISTRADOR);
}
}
Nocódigodaclasse SessionScopedMBovalorde numeroDeAcessosserá
alteradoacadarequisiçãodousuário,eumnovovalorseráexibidoparaeleacada
exibiçãodapágina.
O tipo SessionScoped estádisponíveltanto para ManagedBean do pacote
javax.faces.beancomoparaosManagedBeansqueutilizamCDI.
Amelhorutilização paraumManagedBeanSessionScopedéparaarmazenar
dadosrelativosaousuário.Essesdadosdevemservirparafacilitaroacessoàsin-
formações dousuárioouatémesmotrabalhar“regrasdeview”,ouseja,regrasque
definirãooqueumusuáriopodevisualizarouacessar,entreoutrasfuncionalidades.
// imports omitidos
@ManagedBean
@SessionScoped
public class UsuarioLoginMB {
private Usuario usuario;
private String localeUsuario = "pt_BR";
public void logout() throws ServletException, IOException {
HttpSession session = // busca a session
session.invalidate();
// efetua redirect
}
public boolean isAdministrador(){
return usuario.getPerfil().equals(Perfil.ADMINISTRADOR);
}
// gets e sets omitidos
}
13

## Página 28

CasadoCódigo
Nocódigodaclasse UsuarioMB,épossívelverqualseriaumaboautilização
paraumaManagedBeanSessionScoped.Métodoseatributospoderiamseradicio-
nados/removidosparafacilitaroacessoaosdadosdousuário,porexemplo,ummé-
todoparaverificarospapéisdousuárionopróprioManagedBeanparadiminuiro
caminhodaEL.Aoinvésde: ${usuarioMB.usuario.administrador}basta-
riafazer ${usuarioMB.administrador}enopróprioManagedBeanseriafeito
todootratamentodosdados.
OproblemadoSessionScopedéqueeleémuitofácildeusar.Seumdesenvol-
vedorprecisarenviarvalordeumatelaparaoutra,omodomaisfácildefazerseria
salvaressevaloremumManagedBeandotipoSessionScoped;masaomesmotempo
queeleéomaisfácilétambémomaisperigoso.
ÉprecisoteremmentequesemprequeumvaloréatribuídoaumSessionS-
coped,elepermaneceránamemória.Seoservidortivermilusuáriosativosecada
instânciade UsuarioMBtiverpelomenosumalistadecarrosquecontenham1000
itens...Bom,aíépossívelpercebercomoousodamemóriadoservidorcomeçariaa
aumentar.
QuandooSessionScopedémuitoutilizado,podemosterManagedBeansque
utilizaminformações deoutrosManagedBeans,sendoquetodosessesvaloresestão
salvosnasessão.ImagineosManagedBeans CarroMB, PessoaMBe CasaMB.Caso
PessoaMBremovaocarrodo CarroMBea CasaMBestejaprecisandodessevalor,
jáépossívelsentirocheirode NullPointerException...
OSessionScopedéumescopomuitoútil,maspodecausardiversosproblemas
edordecabeçasemalutilizado.
Énecessáriobastantecuidadoaousá-lo,aindamaisemtelasdelistagenseca-
dastro. Casoousuárioabraonavegadornatelade BairrosMB,edepoisacabe
abrindoumaabanovanomesmonavegadorapontandoparaatelada BairrosMB.
Aalteraçãorealizadaemumaaba,podeinterferirnofuncionamentodaoutra.
14

## Página 29

CasadoCódigo Capítulo3.Mantenhaobeannasessãocom@SessionScoped
Figura3.2:Aba1
Figura3.3:Aba2
Épossívelperceberquenasimagens3.2e3.3queseousuárioconfirmaraal-
teraçãodaAba2edepoisconfirmaraalteraçãodaAba1,algumainformaçãoserá
perdida.
OSessionScopedémuitoútil,massemalutilizadopodecausarsériospro-
blemasàaplicação.
15

## Página 31

Capítulo4
Entendaonovo@ViewScoped
OManagedBeanViewScopedéumtipodeescopoqueseencontraentreoSessionS-
copedeoRequestScoped.Eletemacaracterísticadeexistirnamemóriaenquanto
ousuáriopermanecernapáginaexibida. V e j aasimagens4.1e4.2paraentender
melhorofuncionamentodesseescopo.

## Página 32

CasadoCódigo
Figura4.1:ViewScopedcomDataTable
Figura4.2:ViewScopedcomDataTable
Seousuárioabrirumatelacomum dataTable,oManagedBeancomosdados
permanecerávivoeprontoparaexibirasinformações aqualquerchamadareali-
zada.U m avezqueousuáriomudedepágina,oManagedBeanserádescartadopelo
servidor.
18

## Página 33

CasadoCódigo Capítulo4. Entendaonovo@ViewScoped
Figura4.3:ViewScopedManagedBeantratandorequisição
Aimagem4.3mostracomooJSFirátratararequisiçãoaoseutilizarumMana-
gedBeanViewScoped:
1)Ousuárioiniciaráumarequisição;
2) OManagedBeanprocessaráasinformações necessárias;
3)AsinformaçõesdoManagedBeanficamdisponíveisparaoprocessamentodatela;
4) OManagedBeanmanteráosdadoscasoousuáriopermaneçanapáginaouna-
vegaráparaoutrapáginaeosdadosemmemóriaserãodescartados.
@ManagedBean
@ViewScoped
public class ViewScopedMB implements Serializable {
private int numeroDeAcessos;
public int getNumeroDeAcessos() {
return ++numeroDeAcessos;
}
public void setNumeroDeAcessos(int numeroDeAcessos) {
this.numeroDeAcessos = numeroDeAcessos;
}
public String somar() {
numeroDeAcessos++;
19

## Página 34

CasadoCódigo
return null;
}
}
Noexemplodaclasse ViewScopedMB,ovalordo numeroDeAcessosperma-
neceránamemóriaenquantoousuáriopermanecernapágina.Notequeométodo
somarretorna null,issofazcomqueaaçãoredirecioneparaaprópriapáginae
comoobeanéViewScoped,manteránamemóriaosseusvalores.
Éprecisoteremmentequeosdadospermanecerão “vivos”noManagedBean
quandoosmétodosexecutadosretornarem nullousejam void,dessaforma,
indicandoquedevampermanecernamesmatela.Qualquernavegaçãoparaoutra
página,ouatémesmoummétodoretornandooendereçodapáginaatualcausaráa
perdadosdadosdoManagedBean.
U mbomusoparaumManagedBeandotipoViewScopedéemumapáginacom
diversaschamadasAjax.Imagineum h:dataTablesendoexibidoediversos d i a-
logsparaexibirinformações deregistrosrelacionadosao dataTable.Dessemodo
asinformações estariamnamemóriaenãohaveriaanecessidadedevoltaraobanco
dedadosacadachamada.
Atente-seaumproblemaquepodeocorrercomrelação aacessodediversos
usuáriosaobancodedados.V e j anovamenteaimagem4.1enoteumacoisa:ovalor
queestásendoexibidoestáarmazenadoemmemória.Imaginequeumusuárioaltere
osdadosdoPlayer35nobancodedados.Nessecaso,seumoutrousuárioestivesse
comessatelaabertaamaistempo,elenãoveriaessaalteração.
Nocasodeumatelacomediçãooproblemaseriamaiorainda.V e j aasimagens
4.4e4.5paraentendercomooproblemapodeseagravar.
20

## Página 35

CasadoCódigo Capítulo4. Entendaonovo@ViewScoped
Figura4.4:EdiçãocomViewScoped
Figura4.5:EdiçãocomViewScoped
21

## Página 36

CasadoCódigo
ImaginequeousuárioAstrogildoabriuateladeedição 4.4efoiaobanheiro.
EnquantoissoausuáriaAntonieta,pormeiodoseuPC,entrounomesmoregistro,
alterouepersistiuaalteraçãonobancodedados4.5.Oqueaconteceria,aoretornar
dobanheiro,seAstrogildoapertasseobotão A l t e r a r?T o d aaalteraçãorealizadapela
Antonietaseriaperdida.
Paraevitaroproblemadedadosforadesincroniacomobancodedados,uma
rotinadeatualizaçãopoderiaserexecutada.Acada1minutoumaverificaçãopode-
riaserrealizada,outalvezantesdeexibircadaregistro.U m aoutraabordagemseria
adotaralgummecanismoou F r a m e w o r kparatomarcontadessafaltadesincronia.
OJPAcontacomaopçãodeverificarseoobjetofoialteradoporoutrapessoa,desse
modo,quandoAstrogildoapertasseobotão A l t e r a rumamensagemdeerroseria
exibida.
22

## Página 37

Capítulo5
Crieescoposlongosecustomizáveis
com@ConversationScoped
OManagedBeandotipo ConversationScopedtemumfuncionamentoparecido
como ViewScoped.Acaracterísticaprincipaldo ConversationScopedéque
ocontroledaexistênciadoManagedBeanéfeitomanualmente.

## Página 38

CasadoCódigo
Figura5.1:ConversationScopedManagedBeantratandorequisição
Aimagem5.1mostracomooJSFtrataráarequisiçãoaoseutilizarumManaged-
Bean ConversationScoped:
1)Ousuárioiniciaumarequisição;
2) OManagedBeanprocessaráasinformações necessárias;
3)AsinformaçõesdoManagedBeanficamdisponíveisparaoprocessamentodatela;
4) EnquantooManagedBeannãoforfinalizado,osdadosserãomantidos;
5)U m avezqueocomandoparafinalizaroManagedBeanforexecutado,seusdados
serãoeliminadosdamemória.
O ConversationScopedtemseutempodevidadefinidoprogramaticamente,
elefuncionabasicamentecomoumatransaçãodebancodedados.Parainiciarseu
ciclodevidaénecessárioumcomandodeinício,damesmaformaqueparaencerrar
oescopoénecessárioumcomandoqueidentifiqueofim.
ParaumManagedBeandotipo ConversationScoped funcionarcorreta-
menteeledeveseguiralgumasnormas:
•ComosópodeserutilizadocomCDI,oarquivo beans.xmldeveexistir
dentrodapasta WEB-INF;
•Utilizaraanotação javax.enterprise.context.ConversationScoped
naclasse;
24

## Página 39

CasadoCódigo Capítulo5.Crieescoposlongosecustomizáveiscom@ConversationScoped
•Injetarumobjetodotipo javax.enterprise.context.Conversation;
•Chamarosmétodosconversation.begin()e conversation.end()
parainiciarefinalizaroescopodoManagedBean.
// imports omitidos
@Named
@ConversationScoped
public class ConversationScopedMB implements Serializable {
@Inject
private Conversation conversation;
private int numeroDeAcessos;
public String iniciar(){
conversation.begin();
return null;
}
public boolean isTransient(){
return conversation.isTransient();
}
public String somar(){
if(!conversation.isTransient()){
numeroDeAcessos++;
}
return null;
}
public String finalizar(){
conversation.end();
return
"/paginas/parte2/conversationScoped.xhtml?faces-redirect=true";
}
public String navegar(){
if(conversation.isTransient()){
return null;
}
25

## Página 40

CasadoCódigo
return
"/paginas/parte2/conversationScoped2.xhtml?faces-redirect=true";
}
public int getNumeroDeAcessos() {
return ++numeroDeAcessos;
}
public void setNumeroDeAcessos(int numeroDeAcessos) {
this.numeroDeAcessos = numeroDeAcessos;
}
}
Nocódigodaclasse ConversationScopedMBtemummétodoparaabrirefi-
nalizaraconversaçãodoManagedBean,nessecaso iniciare finalizar,respec-
tivamente.Énecessáriosempreselembrardoescopo,ouentãorecursospoderão
ficaralocadosnamemóriadesnecessariamente.
Naclasse ConversationScopedMB,épossívelverquerealizamosumanave-
gaçãoemantivemosoescopovivo.AnavegaçãodevecomeçardedentrodoMana-
gedBean,porexemplo,atravésdométodonavegar,porqueassimosdadosper-
manecerãonamemória.
OManagedBeandotipo ConversationScoped temapenasdoisestados,
transiente long running.Oestadoserátransientantesdoinícioeapóso
fimdaconversação.
O ConversationScoped éideal paraser utilizadoemumatelanaqual
existe um h:dataTable com muitas chamadas ajax e os dados devem
ser mantidos atéuma determinada invocação. Outra vantagem em utilizar o
ConversationScopedémanterumobjetovivoentrediversastelas:anavegação
entretelasnãoeliminaráobjetosdamemória,diferentementedoViewScoped.
O ConversationScopedsópodeserutilizadocomCDI.Nãoexisteessaop-
çãoparaosManagedBeansdopacote javax.faces.bean.Casoasessãodousuá-
riotermine,oManagedBeandotipo ConversationScopedseráeliminadoda
sessão.
26

## Página 41

Capítulo6
Apraticidadedoescopo
@Dependent
Oescopo Dependenttemcomocaracterísticanãoterumcomportamentopróprio,
massimherdarocomportamentodeoutroManagedBeanemqueforinjetado.
//Imports omitidos
@Named
@Dependent
public class DependentScopedMB implements Serializable {
private int numeroDeAcessos;
public int getNumeroDeAcessos() {
return ++numeroDeAcessos;
}
public void setNumeroDeAcessos(int numeroDeAcessos) {
this.numeroDeAcessos = numeroDeAcessos;

## Página 42

CasadoCódigo
}
}
EsseéoescopopadrãoaoseusarJSFcomCDI.Nãoénecessárioutilizaraano-
tação @Dependentnaclasse.
Quando o @Dependent éutilizado diretamente em uma página,cada
EL resultarána criação de um ManagedBean novo. Caso uma páginaconte-
nha #{dependentScopedMB.total} #{dependentScopedMB.total}será
impresso 11. Em geral o escopo Dependent éinjetado dentro de outros
ManagedBeans, desse modo ele herdaráo escopo da classe principal. Se o
DependentScopedMBfosseinjetadono SessionScopedMB,seuescopotambém
seriadesessão.
// imports omitidos
public class MeuMB{
@Inject
private DependentScopedMB dependent;
public void encaminharRequisicao(){
int tempoSessao = dependent.buscarConfiguracao("tempoSessao");
}
// outros metodos omitidos
}
Bo aprática
Considero como boa prática sempre deixar anotado com
@Dependent. Por mais que algumas pessoas da equipe possam
saberqueovalorpadrãoéesse,comopassardotempohaverápessoas
quetalveznãosaibamdisso.Comovalor @Dependentficaclaropara
quemlêocódigoqualéoescopodoManagedBean.
T o m ebastantecuidadoaoinjetarum DependentManagedBeandentrodeum
ApplicationScoped.Essaabordagempodelevaraoproblemade Memory Leak.
A p ó summétodoutilizarumManagedBeandotipo Dependentelenão étotal-
mentedescartado,mantendoumareferênciaparao ApplicationScoped. Seo
mesmométodoforchamadonovamente,outrareferênciaserácriadaparaserutili-
zadaeassimemdiante.
28

## Página 43

Capítulo7
Guardedadosparatodaaaplicação
como@ApplicationScoped
O ApplicationScopedManagedBeantemocomportamentosemelhanteaodo
padrãodeprojeto Singleton,mantendoumaúnicainstânciadedeterminadobeanna
memória.

## Página 44

CasadoCódigo
Figura7.1:ApplicationScopedManagedBeantratandorequisição
Aimagem7 . 1mostracomooJSFtrataráarequisiçãoaoseutilizarumManaged-
Bean ApplicationScoped:
1)Ousuárioiniciaráumarequisição;
2) OManagedBeanprocessaráasinformações necessárias;
3)AsinformaçõesdoManagedBeanficamdisponíveisparaoprocessamentodatela;
4) OmesmoManagedBeanresponderáaoutrosrequestsdeusuários,dessaforma,
nãohaverádistinçãodequalusuáriopoderáounãoteracessoaodadosdoMa-
nagedBean.
Notequenãoexisteindividualidadequandosefalade ApplicationScoped.
NocasodeumManagedBean ApplicationScoped,todousuárioteráacessoà
mesmainstância.Seriaumapráticamuitoerradasalvaralgumainformaçãoemum
ApplicationScopedquepertencessesomenteaumdeterminadousuário.
Otipo ApplicationScopedestádisponíveltantoparaManagedBeandopa-
cote javax.faces.beancomoparaosManagedBeansqueutilizemCDI.
Amelhorutilizaçãoparao ApplicationScopedseriaparacontervaloresuti-
lizadosportodaaaplicação.
30

## Página 45

CasadoCódigo Capítulo7 .Guardedadosparatodaaaplicaçãocomo@ApplicationScoped
@ManagedBean
@ApplicationScoped
public class ApplicationScopedMB implements Serializable {
private int numeroDeAcessos;
public int getNumeroDeAcessos() {
return ++numeroDeAcessos;
}
public void setNumeroDeAcessos(int numeroDeAcessos) {
this.numeroDeAcessos = numeroDeAcessos;
}
}
A classe ApplicationScopedMB mostra como utilizar o
ApplicationScoped. Todos os usuáriosdo sistema que acessarem esse
ManagedBeanverãoocontadoraumentar.Essetipodeescopoéidealparaconter
valorescomoconfiguração,ouobjetoscarosdesecriarequedevemserinstanciados
apenasumavez.
U m aoutraobservaçãoimportantesobreo ApplicationScopedéqueasvezes
sefaznecessárioqueelesejainiciadoantesdetodosManagedBeans.Issoépossível
atravésdaconfiguração: @ManagedBean(eager = true).Comessaconfigura-
çãoumApplicationScopedManagedBeanseráiniciadoantesquequalquertelada
aplicaçãosejaacessada.
Esseconfiguraçãoébastanteútilquandojáqueremosalgumainformaçãocarre-
gadaemmemóriaantesquesejasolicitadapelousuário.Imaginequeumcachede
Cidadessejafeito:senãousasseo eager,ocachesefariaapenasquandoovalorfosse
solicitadopelaprimeiravez,causandodemoranachegadadainformação.
Outraaplicaçãoparaaopção eager=trueécasoumApplicationScopedMa-
nagedBeansejainjetadodentrodeoutroManagedBean.PodeacontecerqueoJSF
aindanãotenhainicializadooApplicationScopedeosvaloresestejamnulos.
31

## Página 47

Capítulo8
Quandousaro@NoneScoped?
ONoneScopedManagedBeantemporcaracterísticaservirapenasaumachamada
daELedepoissereliminadodamemória. V e j aquesuautilização diferedoRe-
questScopedquantoaduraçãodasinformaçõe., ORequestScopedduraporquantas
chamadasdeELforemrealizadasduranteumarequisição. ONoneScopedseráeli-
minadoapósumachamadadeEL.

## Página 48

CasadoCódigo
Figura8.1:NoneScopedScopedManagedBeantratandorequisição
Aimagem8.1mostracomooJSFtrataráarequisiçãoaoseutilizarumMana-
gedBeanNoneScoped:
1)Ousuárioiniciaráumarequisição
2) OManagedBeanprocessaráasinformações necessárias
3)Asinformações doManagedBeanficamdisponíveisparaoprocessamentodatela
4) OmesmoManagedBeannãoresponderáaoutraschamadas.Eleserádescartado
apósreceberumachamada.
Énecessárioentenderqueesseescopotemporcaracterísticaseraltamentedes-
cartável.
// imports omitidos
@ManagedBean
@NoneScoped
public class NoneScopedMB {
private int numeroDeAcessos;
public int getNumeroDeAcessos() {
return ++numeroDeAcessos;
}
public void setNumeroDeAcessos(int numeroDeAcessos) {
34

## Página 49

CasadoCódigo Capítulo8. Quandousaro@NoneScoped?
this.numeroDeAcessos = numeroDeAcessos;
}
}
Seo NoneScopedMBfosseutilizadodaseguinteformadeumaEL,como:
#{noneScopedMB.numeroDeAcessos} #{noneScopedMB.numeroDeAcessos}
Ovalorimpressoseria 1 1.O NoneScopedatenderiaapenasaumachamada
doELedepoisdeixariadeexistir.
AmelhorutilizaçãoparaoNoneScopedseriaparatarefaspontuais,comoforma-
tarumcampo,exibirhoraourealizarumcálculo.Outrobomusoseriaparaacessar
propriedadesdo faces-config.xml.
O NoneScoped ManagedBean está disponível através do pacote
javax.faces.bean.
35

## Página 51

Capítulo9
ExibindoObjetoseMensagensa p ó s
RedirecteoFlashScoped
Noprojetodeexemplodolivro,épossívelencontrarumateladecadastrocomona
imagem9.1.
Figura9.1:Cadastrodecidade
Cadastrosdedadosnaaplicaçãocostumamvircomalgumamensagemindica-
tivaparaousuáriodequeaqueleregistrofoisalvonobancodedadoscomsucesso.
Oproblemaacontecequando,apósrealizarapersistênciacomsucesso,nenhuma
mensageméexibidaaousuário,algocomonaimagem9.2.

## Página 52

CasadoCódigo
Figura9.2:Nãoexibedadosapósumaação
// finalizando cadastro
super.exibirMensagemParaUsuario(FacesMessage.SEVERITY_INFO,
"Nome da cidade cadastrada: " + cidade.getNome());
return "/cadastroComSucesso.xhtml?faces-redirect=true";
Mesmoadicionandoamensagemparaserexibidaaousuário,comonocódigo
visto,amensagemnãoéexibidaeosdadosdacidaderecémcadastradanãochegam
napróximatela.Issoaconteceporumpequenodetalhe,o redirect.
Muitosdesenvolvedorespercebemque,aorealizarum redirect,informações que
deveriamserexibidasnatelanão aparecem,comosetivessemsidoperdidas. Na
verdade,éumcomportamentoesperadoessasinformações seperderem,maspara
entendermosarazãoprecisamoscompreenderoimpactoemseutilizarum redirect.
V e j anafigura9.3comofuncionaoredirect:
Figura9.3:ComofuncionaoSendRedirect
Conseguimosentãoperceberque:
38

## Página 53

CasadoCódigo Capítulo9. ExibindoObjetoseMensagensapósRedirecteoFlashScoped
1)Ousuárioenviaráum requestaoManagedBean;
2) Aoexecutarocomando SendRedirect,oManagedBeanenviaparaobrowser
dousuárioumaURLcomumnovodestino(essevaloriráemum %headerdo
request);
3)ObrowserdousuárioanalisaráoresponseefaráumanovachamadaparaaURL
querecebeu;
4) Anovatelaseráexibidaaousuário.
QuandooManagedBeanredirecionaousuárioparaumanovatela,todososda-
dosdorequestoriginalseperdem.Dadosenviadosno form,mensagensparaserem
exibidasaousuárioeoutrosvaloresseperderão.
Paraajudarodesenvolvedoratrataressecomportamentofoicriadoochamado
FlashScope. Aoutilizaro FlashScopeparamanterosobjetosnamemória,o
próprioJSFmanteráoobjetonamemóriaatéqueelesejautilizado.V e j aocódigoda
classe SendRedirectMBquemostraquandooproblemapoderáacontecer.
@ManagedBean
@RequestScoped
public class SendRedirectMB extends AbstractMB{
private int valorParaExibir;
private static final String URL = "URL PARA PÁGINA";
public int getValorParaExibir() {
return valorParaExibir;
}
public void setValorParaExibir(int valorParaExibir) {
this.valorParaExibir = valorParaExibir;
}
public String redirecionarSemFlash() {
super.exibirInformacao("Valor Enviado é de: " + valorParaExibir);
return URL + "?faces-redirect=true";
}
public String redirecionarComFlash() {
super.exibirInformacao("Valor Enviado é de: " + valorParaExibir);
39

## Página 54

CasadoCódigo
FacesContext instance = FacesContext.getCurrentInstance();
ExternalContext externalContext = instance.getExternalContext();
externalContext.getFlash().put("valorParaExibir", valorParaExibir);
externalContext.getFlash().setKeepMessages(true);
return URL + "?faces-redirect=true";
}
}
U m avez que o método redirecionarSemFlash for executado, to-
dos os dados presentes no request original serão perdidos. O método
super.exibirInformacaonadamaisfazdoqueexibirumamensagemparao
usuárioquepodeservisualizadacomumh:messages.
Para exibir um objeto ou um atributo após um SendRedirect basta
fazer como no método redirecionarComFlash. Basta utilizar o FlashS-
cope externalContext.getFlash().put("valorParaExibir",
valorParaExibir);paraarmazenarovalorcomosefosseummapa;essemapa
armazenaráovaloratéofinaldoredirecionamento.Paraexibiressevalornaoutra
tela, bastafazer: <h:outputText value="#{flash.valorParaExibir}”
/>.A p ó sovalorseracessadonoFlashScopeeleseráeliminadodamemória.Épossí-
veltambémmanteroobjetonasessão,bastaacessaroobjetopor <h:outputText
value="#{flash.keep.valorParaExibir}”/>.
Para exibir uma mensagem para o usuárioexistem diferentes manei-
ras: duas fáceise uma mais complexa. A p ó sinserir a mensagem no con-
texto para exibi-la para o usuário,basta executar o seguinte comando:
externalContext.getFlash().setKeepMessages(true). Desse modo
a mensagem seráexibida para o usuárioapós ser redirecionado. O outro
modo de exibir a mensagem éadicionar a tag a seguir na página: <c:set
target="#{flash}”property="keepMessages”value="true”/>.
Dessemodoamensagemserásalvanoflasheexibidaaousuário.Oúltimomodo
envolvecriarum PhaseListenerquefaçaotrabalhomanualdepersistirovalor
nasessão edepoisremover;paramaioresinformações dessaabordagemvisiteo
link:http://uaihebert.com/?p=499.
V e j anaimagem9.4osdadossendoexibidosapósutilizarastécnicasapresenta-
dasaqui.
40

## Página 55

CasadoCódigo Capítulo9. ExibindoObjetoseMensagensapósRedirecteoFlashScoped
Figura9.4:Cadastrodecidade
41

## Página 57

P a r t eII
CuidadoscomseusManaged
Beans
T o d odesenvolvedorprecisaterbastantecuidadoaoadicionarcódigosqueli-
damcomalógicadevisualizaçãodasuaaplicação,comodefinições de“ oquepode
serexibidoparadeterminadousuário?”,“ c o m oexibirdeterminadainformaçãopara
perfisdiferentesdevisualizações”.
U mcódigocriadosempensaremboaspráticaspodelevarasériosproblemas
demanutenção,acabamosporterclassesgrandesecomplexas,emuitasfunções e
códigosrepetidos.
CitoaquiateoriadajanelaquebradaapresentadapeloscientistasJamesQ.Wi l -
soneGeorgeL.Kelling.Imagineumprédiocomjanelasquebradas.Seessasjanelas
nãoforemrapidamentereparadas,achancedevândalosquebraremmaisjanelasau-
mentam.Domesmomodoépossívelacontecercomsistemas.Bastaqueoprimeiro
código f e i osejaadicionadoaoprojeto,queaumentaráachancedeumsegundocó-
digo f e i oaparecereassimpordiante.

## Página 59

Capítulo10
Colocandológicaderenderedno
MB
Considereocódigodeumpanel,noqualexisteumalógicaparadeterminarseele
seráexibidoounão:
<h1>Relatório de Salários</h1>
<h:panelGrid columns="2"
rendered="#{relatorioMB.usuario.papel eq 'ADM'}" >
<h:outputText value="Salário do Funcionário:" />
<h:outputText value="#{funcionario.salario}" />
</h:panelGrid>
Otrechodeumrelatóriodesaláriospoderiaclaramenteexemplificaressasitu-
ação. Ocódigodo Relatório de Saláriosésimplesefácildeentender,nele
existeapenasalógicaparaverseousuárioéounãoadministrador.Casoousuário
sejaumadministrador,entãoserámostradoosaláriodofuncionário.

## Página 60

CasadoCódigo
U m aprimeiraboapráticaseriaaplicaroprincípio T e l l ,don’task(“Diga,não
pergunte”).Essapráticadizqueémelhordeixarqueopróprioobjetodigaseelepode
ounãofazertalaçãoenãooutroobjetocalcularessaaçãoporele.V e j aocódigoda
classe Usuario,quemostracomoficariaummétodoaplicandoesseprincípio.
public enum Papel {
ADM, GERENTE, USUARIO_SIMPLES;
}
public class Usuario {
private String login;
private String email;
private Papel papel;
public boolean isAdm() {
return Papel.ADM.equals(papel);
}
public boolean isGerente() {
return Papel.GERENTE.equals(papel);
}
public boolean isUsuarioSimples() {
return Papel.USUARIO_SIMPLES.equals(papel);
}
// getters e setters omitidos
}
Noteque a classe Usuario informa qual o papel do usuário. A vanta-
gemdessa abordageméquecaso a cláusula rendered="#{usuario.papel
eq 'ADM'}”passasse para rendered="#{usuario.papel eq 'ADM'and
usuario.dataAdmissao > '10-10-2000'}” bastaria alterar na classe
UsuarioquetodasasELsqueutilizassemonovométodonão precisariamser
alteradas.V e j acomoficaráocódigoalteradodorelatório.
<h1>Relatório de Salários</h1>
<h:panelGrid columns="2" rendered="#{relatorioMB.usuario.adm}" >
<h:outputText value="Salário do Funcionário:" />
<h:outputText value="#{funcionario.salario}" />
</h:panelGrid>
46

## Página 61

CasadoCódigo Capítulo10.ColocandológicaderenderednoMB
.
Notequenão importaquantasvezesaregraparacalcularseousuárioéum
administradormude,issonãoaferámaisaEL.IndependentedequantasvezesaEL
forutilizadaumaalteraçãonaregranãoserianecessáriaumaalteraçãonaspáginas.
Aindaassimépossívelnotarqueessecódigopodesermelhorado.Imagineque
agoraparaverosaláriodofuncionário,alémdeseradministradorousuárioprecisa
serdoRH.Seriabemsimplesalterarorelatórioeadaptaressaregra.
<h1>Relatório de Salários</h1>
<!-- relMB foi reduzido de relatorioMB para melhor visualização -->
<h:panelGrid rendered="#{relMB.usuario.rh and relMB.usuario.adm}" >
<h:outputText value="Salário do Funcionário:" />
<h:outputText value="#{funcionario.salario}" />
</h:panelGrid>
Realmenteocódigoestásimpleselegível,masimagineseessemesmoIFestá
repetido40xporessapágina,etalvezatéemoutraspáginas.
Éagoraqueentraatristerealidadedodesenvolvedor,aqueletrágicomomento
emquepercebemosqueseránecessáriovasculharcadapáginaeverondeessaregra
foiaplicada.Eapiorparteéquetalvezacondiçãorenderedestejaassim:
rendered="#{relatorioMB.usuario.rh and relatorioMB.usuario.adm}"
ou
rendered="#{relatorioMB.usuario.adm and relatorioMB.usuario.rh}"
ou
rendered="#{rel.user.adm and rel.user.rh}"
Essavariaçãopoderiacausaraimpossibilidadedeusarumapesquisaparaloca-
lizaroquenecessitariadealteração.
Existemaisumaabordagemsimplesqueajudaráaevitarmuitadordecabeça,
bastaisolaressasregrasemalgumlugar,comooManagedBean.Nãoénecessário
mágica,nemumconhecimentoprofundoemarquiteturaparaaplicaressasimples
abordagem.
Atagrenderedficariaassimrendered="#{relatorioMB.usuarioPodeVerSalario}”
Notequeapartirdeagoraquemestátomandocontadessaregradeviewéopróprio
ManagedBean. Éelequemdiráseousuáriopoderáverounão orelatório. Esse
47

## Página 62

CasadoCódigo
métodopoderiaserreplicadopormilharesdevezesque,casoaregramudasse,não
haveriaimpactonaspáginas.
public boolean isUsuarioPodeVerSalario(){
return usuario.isADM() && usuario.isRH();
}
Ométodo isUsuarioPodeVerSalariomostraexatamenteavantagemda
abordagemdecentralizarasregrasdeviewemumManagedBean.Casoométodo
fosseutilizadoem30validações diferentes,nãohaveriaproblemaalgumsearegra
alterasse.
48

## Página 63

Capítulo11
InicializandoObjetos
QuandoestamosimplementandoosManagedBeansdoprojeto,precisamostomar
bastantecuidadocomainicialização dosseusatributos,poisalgumasarmadilhas
podemnosesperar.Nocódigoaseguir,inicializamosalistadecarrosnoconstrutor,
masseráqueessaéamelhorprática?
@ManagedBean
public class InicializandoMB{
private List<Carro> carros;
@EJB
private CarroDAO carroDAO;
public InicializandoMB(){
carros = carroDAO.listAll();
}
// getters e setters omitidos
}

## Página 64

CasadoCódigo
U s a m o sumEJBnoconstrutordaclasseparabuscarnobancodedadosumalista
de Carro.Noentanto,ainjeçãodedependênciasaconteceapenasapósainvocação
doconstrutor.Nessecaso,receberemosuma NullPointerException,poisoEJB
aindanãoestaráinjetadoeprontoparaserinvocado.
U mmododeevitartodososproblemaslistadosacimaseriainicializarosatribu-
tosemummétodoanotadocom javax.annotation.PostConstruct.
Porcontrato,umaclasseJavaEEterátodosseusrecursosinicializadosantesdo
métodoanotadocom@PostConstructserinvocado.
@ManagedBean
public class InicializandoMB {
private List<Carro> carros;
@EJB
private CarroDAO carroDAO;
@PostConstruct
public void init() {
carros = carroDAO.listAll();
}
// getters e setters omitidos
}
A p ó salterarocódigodaclasse InicializandoMB,épossívelnotarqueocó-
digoquehavianoconstrutordaclassefoimovidoparaométodoinit()eocons-
trutorfoiremovidodocódigo.Opróprioservidorficaráencarregadodechamaro
métodoinit()egarantirqueelesejaexecutadoantesqueoManagedBeaninteraja
comchamadasexternas.
Infelizmente,háumadesvantagemnaabordagemdeinicializaçãodeatributos
emummétodoanotadocom @PostConstruct.ConsidereagoraqueesseMana-
gedBeantemoutrosmétodosquenãonecessitamdovalordalista carros.
@ManagedBean
public class InicializandoMB{
private List<Carro> carros;
@EJB
private CarroDAO carroDAO;
50

## Página 65

CasadoCódigo Capítulo11.InicializandoObjetos
@PostConstruct
public void init(){
carros = carroDAO.listAll();
}
public List<String> getMarcas(){
return carroDAO.getMarcas();
}
public List<String> getModelos(){
return carroDAO.getModelos();
}
// getters e setters omitidos
}
ReparequeométodogetMarcas()eométodogetModelospodemsercha-
madosporumapáginaquenãoutilizealistade carrosparanada.Adesvantagem
dessaabordagemé:mesmoqueapenasosmétodosgetMarcas()e getModelos
sejamutilizados,alistade carroscontinuaráasercarregadadobancodedados,
desnecessariamente.
Nessecaso,podemosusaraabordagem lazy(preguiçosa)desecarregarobjetos
noManagedBean.V e j ananovaversãodaclasse InicializandoMBcomoutilizar
aabordagemdeinicialização lazy.
@ManagedBean
public class InicializandoMB{
private List<Carro> carros;
@EJB
private CarroDAO carroDAO;
public List<Carro> getCarros(){
if (carros == null) {
carros = carroDAO.listAll();
}
return carros;
}
public List<String> getMarcas(){
return carroDAO.getMarcas();
51

## Página 66

CasadoCódigo
}
public List<String> getModelos(){
return carroDAO.getModelos();
}
// getters e setters omitidos
}
Ométodoinit()foiremovidodocódigoeométodogetCarrosfoialterado.
Casoalista carrosseja null,aconsultaserárealizadanobancodedados.Com
essaabordagem,seométodogetCarrosnuncaforinvocado,essalistanuncaserá
inicializadaemuitasviagensaobancodedadosdeixarãodeexistir.
Adesvantagemdessaabordageméofatodequecadamétodogetdeveterum
testedotipo if (objeto == null). Aquantidadedelinhasdaclassepoderá
subirconsideravelmente.
Serve para todo escopo
Notequeiniciarumobjetodemodo lazyoupelo@PostConstruct
éuma boa práticae pode/deve ser aplicada a qualquer tipo de es-
copo e não apenas no @RequestScoped, como exibido na classe
InicializandoMB.
Épossívelutilizarumaabordagemhíbridanaqualtemosatributoscarregados
emummétodoanotadocom @PostConstructeatributosinicializadosdemodo
lazy.
@ManagedBean
public class InicializandoMB{
private List<Carro> carros;
private List<Cidade> cidades;
@EJB
private CarroDAO carroDAO;
@EJB
private CidadeDAO cidadeDAO;
@PostConstruct
52

## Página 67

CasadoCódigo Capítulo11.InicializandoObjetos
public void init() {
cidades = cidadeDAO.listAll();
}
public List<Carro> getCarros() {
if (carros == null) {
carros = carroDAO.listAll();
}
return carros;
}
public List<String> getMarcas() {
return carroDAO.getMarcas();
}
public List<String> getModelos() {
return carroDAO.getModelos();
}
// getters e setters omitidos
}
Nocódigodaclasse InicializandoMB,épossívelverqueambasabordagens
foramutilizadas.Preferencialmente,métodosanotados @PostConstructdevem
carregarobjetosqueserãodeusocomumemtodasounamaiorpartedaschamadas
realizadasaoManagedBean.
U m aoutramaneiradeiniciarobjetoséinformandoaoJSFqueummétododeve
serexecutadoantesdecarregartodaapágina.Essemétodoéinformadoatravésda
página.V e j acomoaclasse InicializandoMBficaráapósumaleverefatoração.
@ManagedBean
public class InicializandoMB{
private List<Carro> carros;
private List<Cidade> cidades;
@EJB
private CarroDAO carroDAO;
@EJB
private CidadeDAO cidadeDAO;
public void inicializar(){
cidades = cidadeDAO.listAll();
53

## Página 68

CasadoCódigo
carros = carroDAO.listAll();
}
// outros métodos omitidos
}
Temosométodoinicializar,queserádisparadoquandoapáginaforcha-
madaatravésdatag f:event.
<f:event type="preRenderView"
listener="#{inicializandoMB .inicializar}"/>
Bastaadicionarocódigodatag f:eventqueoJSFchamaráométodoque
carregatodososatributosdatelaantesdeexecutarqualqueração.
54

## Página 69

Capítulo12
InjetandoManagedBeans
ConsidereumManagedBeanemque,paradecidirseousuáriopodeounão ver
determinadainformação,eleprecisadeterminarseousuáriotemoperfilnecessário.
// imports omitidos
@ManagedBean
public class CarroMB {
public List<Carro> getCarrosPorUsuario() {
List<Carro> carros = new ArrayList<Carro>();
usuario = // recupera usuário logado
adicionarCarrosSimples(carros, usuario);
adicionarCarrosEconomicos(carros, usuario);
adicionarCarrosLuxuosos(carros, usuario);
return carros;
}
// outros métodos...
}

## Página 70

CasadoCódigo
OmétodogetCarrosPermitidosPorUsuario()retornariaapenasoscar-
rosnecessáriosparadeterminadostiposdeusuário.
NotequeoManagedBean CarroMBprecisadeumusuáriopararealizarabusca
doscarros.Edeondeviriaesseobjetousuário?Esseobjetopoderiaserbuscadona
sessão,masocaminhoatéchegaraelaéumtantoquantolongo...
FacesContext context = FacesContext.getCurrentInstance();
ExternalContext externalContext = context.getExternalContext();
HttpServletRequest request = (HttpServletRequest)
externalContext.getRequest();
HttpServletSession session = request.getSession();
Usuario usuario = (Usuario) session.getAttribute("USUARIO_LOGADO");
Paraconseguiracessaro HttpSessionchamamos5métodosemumtrechode
códigomuitoextensoequeficadifícildeler.
U m apráticacomumédeterumManagedBeanquefaciliteoacessoaosda-
dosdousuáriologado.Porexemplo,paraacessarousuáriodasessãobastariafazer
usuarioMB.getUsuario().
ExisteummododeacessarumManagedBeanbuscandoovalordasessãoqueé
umcódigotãoverbosoquantoojámostradoanteriormente.
// código reduzido
userMB = (UsuarioMB) externalContext.getSessionMap().get("UsuarioMB");
userMB.getUsuario();
ÉpossívelextrairumManagedBeandiretamentedocontextodoJSF,masainda
assiméumcódigoqueficarálongo.U m aabordagemmaissimplesseriaatravésda
injeçãodoManagedBeancomodependência.
@ManagedBean
public class CarroMB{
@ManagedProperty(value = "#{usuarioMB}")
private UsuarioMB usuarioMB;
public void setUsuarioMB(UsuarioMB usuarioMB) {
this.usuarioMB = usuarioMB;
}
public List<Carro> getCarrosPorUsuario(){
56

## Página 71

CasadoCódigo Capítulo12.InjetandoManagedBeans
List<Carro> carros = new ArrayList<Carro>();
usuario = usuarioMB.getUsuario();
adicionarCarrosSimples(carros, usuario);
adicionarCarrosEconomicos(carros, usuario);
adicionarCarrosLuxuosos(carros, usuario);
return carros;
}
// outros métodos...
}
Paraqueainjeçãofuncione,algunspassossãonecessários:
•Utilizaraanotação @ManagedPropertysobreoatributodoManagedBean
aserinjetado;
•OManagedBeanaserinjetadoprecisadeummétodoset.
UtilizarinjeçãodeManagedBeandeixaocódigomaissimplesdelereentender.
Outrodetalhesobreainjeção deManagedBeanéquesópodemosinjetarum
ManagedBeandentrodeoutrocommesmoescopoouumescopomaisabrangente.
Porexemplo:épossívelinjetarumSessionScopeddentrodeumRequestScoped,mas
nãoépossívelfazeroinverso.
57

## Página 73

Capítulo13
TargetUnreachable:Enfrentea
NullPointerExceptiondoJSF
ComodesenvolvedoresJava,estamosacostumadosanosdepararcomasfamosas
NullPointerException. T a m b é mnãoestaremoslivresdissoaotrabalharcom
JSF;portanto,éprecisoaprenderalidarcomelas,naformacomopodemacontecer
noJSF.ConsidereosimplesManagedBeanaseguir:
@ManagedBean
public class CidadeMB {
private Cidade cidade;
public Cidade getCidade() {
return cidade;
}
// outros métodos
}

## Página 74

CasadoCódigo
Casoocódigo #{cidadeMB.cidade.nome}sejaexecutado,aseguintemen-
sagemdeerroseráexibida:
Target Unreachable, 'null' returned null
NoexemplodoManagedBean CidadeMB,épossívelverqueoatributo cidade
éretornadomasemnenhummomentoéinstanciado.Esseerropodeserfacilmente
contornadopelasabordagensdocapítulo11.
@ManagedBean
public class CidadeMB {
private Cidade cidade;
public Cidade getCidade() {
if(cidade == null){
cidade = new Cidade();
}
return cidade;
}
// outros métodos
}
Notequenocódigodaclasse CidadeMB,ométodogetCidade()agoracon-
témum ifparaverificarseoatributo cidadeestánull.
Seocódigo #{cidadeMB.cidade.estado.nome}forexecutado,omesmo
erropoderáacontecer. Énecessárioquetodososatributosnão primitivossejam
inicializadosantesdeseremutilizados.
U moutro motivo para esse erro aparecer poderia ser utilizar a EL
#{cidadeMB.cidade.estado.nome}, mas esquecer de anotar o Managed-
Beancom @ManagedBeanou @Named.
Esse erro tambémpode acontecer por máutilização da EL. Caso a EL
#{cidade.nome}sejaescrita #cidade.nome,amesmamensagempoderáapa-
recer.
Parafinalizar,essamensagemdeerropodevirdescritadosseguintesmodos:
Target Unreachable, 'null' returned null
javax.el.PropertyNotFoundException: /pagina.xhtml @13,154
60

## Página 75

CasadoCódigo Capítulo13.TargetUnreachable:EnfrenteaNullPointerExceptiondoJSF
value="#{cidade.nome}": Target Unreachable, 'null' returned null
Alvo inalcançável, SEU_ATRIBUTO retornou null
61

## Página 77

Capítulo14
Cuidadocomo“Valueisnotvalid”
Existemerrosqueacontecempordetalhessutis,cujosmotivosàsvezesdemoramos
horasparadescobrir.Oerro Value is not validéumdeles.
Eleécomumenteencontradoquandousamoscomponentesdotipo select.
Figura14.1:V a l u eisnotvalid
Devidoaofatodequeo selectéutilizadoemclasses,oJSFtentarácomparar
osvaloresatravésdosmétodoshashCodee equals. Esseerropodeacontecer
casosuaclassenãoestejaimplementandoessesdoismétodoscorretamente.Omé-
todo hashCodedevesempreretornaruminteiroquerepresentenumericamente

## Página 78

CasadoCódigo
aclasse.EsseinteiroécomumenteutilizadopelainterfaceSeteoutroscomponen-
tes. Ométodo equalsdevesempreretornarseumobjetoéigualaooutro,eo
resultadonãopodevariar.Paramelhoresdetalhesveja:http://tutorials.jenkov.com/
java-collections/hashcode-equals.html
public class Cidade{
private int id;
private String nome;
// outros métodos
@Override
public int hashCode() {
int hashCode = 33;
hashCode = hashCode * 17 + id;
hashCode = hashCode * 31 + nome.hashCode();
return hashCode;
}
@Override
public boolean equals(Object obj) {
if (obj instanceof Cidade) {
Cidade cidade = (Cidade) obj;
return cidade.id == id;
}
return false;
}
}
Aclasse Cidadeestádescritanoformatoadequadoparaserutilizadaemum
componente select.
64

## Página 79

P a r t eIII
Front-endsJSF
U mdosmaioresproblemasdepessoasqueusamoJSFcomeçapelosarquivos
depáginas.MáutilizaçãodoJSFpodelevaraproblemasdearquitetura,acompor-
tamentosestranhoseatémesmoadesenvolvedoresachandoqueéfalhadopróprio
JSF.
EscolherentreJSPouxhtml,otimizarousodoFacelets,saberquandoutilizar
actionou actionListenersãoassuntosqueserãovistosnessapartedolivro.

## Página 81

Capítulo15
UtilizarJSPouxhtml?
O JSPéumvelhoguerreiroeconhecidodomundoJavaW e b .Como JSPveioa
grandeutilizaçãodo Servletparafazeraintegraçãoeodesacoplamentoentreo
código HTMLeocódigo Java.
Nasprimeirasversões doJSF,o JSPfoiintensamenteutilizadoparaexibiras
informações paraousuário.Jácomaversão 2.0doJSF,apareceuo xhtml,com
umatecnologiachamada Facelets.
Notequeasvantagensdo JSPsobreo xhtmlestãomaisrelacionadascoma
questãodeestudoeaprendizado.MuitasempresasadotamoJSPaindapelofatode
seraprimeiratecnologiaaserutilizadaparaJavaW e b ,eacabasendomaispráticoe
baratocontinuarautilizaramesmatecnologia.
Conheçopessoasqueatéhojesãocontradeterminadosframeworks.Porexem-
plo,algumconhecidoqueusouaversão0.5doJSFenãogostoueespalhouissopara
frente.Reconheçoqueantesdaversão2.0eramuitodifícildesetrabalharcomoJSF,
maspoucossãoosquenãogostaramdessanovaversão.
Possocitarumcasoemqueumapessoamedisse:“odeioHibernatepoistem

## Página 82

CasadoCódigo
muitoXML”.Eurespondiqueatualmentepoderiasefazeraaplicaçãotodacomano-
taçãoeapessoamedissequeaindaassimpreferianemolharoHibernate.
Comrelação ao xhtml,quandoutilizadocom Facelets(queveremosem
breve),épossívelressaltarasseguintesvantagens:
•XHTMLcomFaceletspodemexecutaraté50%maisrápidoqueoJSP;
•T o d a sastagsutilizadasnaspáginassão declaradasdemododinâmico,não
necessitamestardeclaradasemumTLD(TagLibraryDescriptor);
•FaceletspermitemTemplatesdemodoavançado,emqueareutilizaçãodecó-
digoémuitoalta.
Nacodificaçãodaspáginas,épossívelvercomoocódigodeum JSPéseme-
lhanteaumapáginaxhtml.Sóépossívelnotaressasemelhançaempáginasimples,
umavezqueaspáginasaumentamsuacomplexidadeeemnúmerodecomponentes
ocódigoficarábastantedistinto.U mJSPficariacomo:
<%@ taglib uri="http://java.sun.com/jsf/core" prefix="f" %>
<%@ taglib uri="http://java.sun.com/jsf/html" prefix="h" %>
<html>
<head>
<title>Exemplo JSP</title>
</head>
<body>
<h:form>
<h:outputText value="Olá Mundo JSP!" />
</h:form>
</body>
</html>
Enquantoqueocódigoequivalenteno xhtmlficaria:
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"
xmlns:h="http://java.sun.com/jsf/html">
<h:head>
<title>Exemplo xhtml</title>
</h:head>
<h:body>
68

## Página 83

CasadoCódigo Capítulo15.UtilizarJSPouxhtml?
<h:form>
<h:outputText value="Olá Mundo xhtml!" />
</h:form>
</h:body>
</html>
69

## Página 85

Capítulo16
Utilizandoimagens/css/javascriptde
modossimples
Quandoprecisamostrabalharcomimagensemnossasaplicações, umaabordagem
muitoutilizadaépassarocaminhocompletodeumarquivo.
<!-- código que podem ou não exibir a imagem -->
<h:graphicImage value="../imagens/minhoca.jpg" />
<h:graphicImage
value="#{facesContext.externalContext.requestContextPath}
/WebContent/imagens/minhoca.jpg" />
Eamesmapráticatambémocorrequandofalamosdecssejavascript.
<!-- código que podem importar o css/javascript -->
<link rel="stylesheet" type="text/css" href="../meu_css/style.css">
<script type="text/javascript" src="../meu_javascript/script.js" />

## Página 86

CasadoCódigo
V e j aqueocaminhofísicofoipassadoparaapáginapoderexibirumaimagem
ouutilizarosrecursosdocssedojavascript.Oproblemaéquebastamudarapágina
delugarqueoscódigosjávistosparamdefuncionar.
Émuitocomplicadorefatorarosdiretóriosdaspáginasumavezqueexisteuma
dependênciatãoforteentreorecursoutilizado.
Pararesolveresseproblema,oJSF2temorecursochamado L i b r a r i e s(biblio-
tecas).Eletratarácadatipoderecursocomoumabiblioteca,ouseja,naaplicação
podeexistirumaoumaisbibliotecasparaimagens,cssejavascript.
Parautilizarosrecursosdenossaaplicação, bastacriarumapastachamada
resources,queficaránaraizdoprojeto. Essapastaconteráaestruturadepas-
tasearquivosnecessáriosparaseremutilizadoscomobibliotecas. Aimagem16.1
mostracomodeveficaressaestrutura.
Figura16.1:Estruturadaspastas
Notequeoutras3pastasexistemabaixode resources: css, imagense
javascript.Cadadiretórioqueforadicionadoabaixodapasta resourcesserá
tratadocomoumabiblioteca.
Avantagemdessaabordageméafacilidadeparaacessarosrecursos.
<!-- Código para importar os arquivos -->
<h:outputStylesheet library="css" name="estilo.css" />
<h:outputScript library="javascript" name="ola.js" />
72

## Página 87

CasadoCódigo Capítulo16.Utilizandoimagens/css/javascriptdemodossimples
<!-- Código para utilizar os recursos -->
<h:graphicImage library="imagens" name="minhoca.jpg" />
Paraadicionaro javascript,o csseutilizarumaimagembastaapontarparaa
bibliotecaeparaonomedorecurso.Aoutilizaressaabordagemépossívelmudaras
estruturasdaspáginas,quenãohaveráproblemasparalocalizarasbibliotecas.
Noteque,notrechodocódigoquemostracomoutilizarosvalores,emnenhum
momentofoiutilizadoocaminhofísicoparasechegaraosarquivos.
73

## Página 89

Capítulo17
B o autilizaçãodoFacelets
Incorporadooficialmenteàversão2doJSF,umadasvantagensdo Faceletséapos-
sibilidadedeseutilizarumesquemade Templatenaspáginasdaaplicação.
V e j anaimagem17.1comoficaráaestruturadaspáginasutilizadasnocódigo
fontedestelivro.
Figura17.1:Estruturadaspastas
<!-- master.xhtml -->

## Página 90

CasadoCódigo
<html xmlns="http://www.w3.org/1999/xhtml"
xmlns:ui="http://java.sun.com/jsf/facelets"
xmlns:h="http://java.sun.com/jsf/html"
xmlns:f="http://java.sun.com/jsf/core">
<h:head>
<h:outputStylesheet library="css" name="estilo.css" />
<h:outputScript library="javascript" name="ola.js" />
</h:head>
<h:body>
<f:view>
<div id="divLeft">
<ui:insert name="divLeft">
<ui:include src="left.xhtml" />
</ui:insert>
</div>
<div id="divMain">
<ui:insert name="divMain" />
</div>
</f:view>
</h:body>
</html>
Parautilizarumapáginaqueservirácomo Template,bastafazercomonocó-
digodapáginamaster.xhtml. Esselayoutésimples,apenascomummenula-
teraleumaáreaprincipalparaexibirasinformações. Sobreocódigodapágina
master.xhtmlépossíveldizer:
•<ui:insert name="divLeft"></ui:insert>defineumaáreaqueserá
substituída. Notequeessaáreapodeconterumvalorpadrão ouestarem
branco.
•<ui:include src="left.xhtml"/>fazainclusãodeumapágina.
Apáginadomenuéumapáginaaindamaissimples,apenascombotões que
serãoinseridosemtodasaspáginasqueutilizaremo Template.
<!-- left.xhtml -->
<h:body>
<ui:composition>
76

## Página 91

CasadoCódigo Capítulo17.BoautilizaçãodoFacelets
<h:form>
<p:button outcome="/applicationScoped.xhtml"
value="@ApplicationScoped" />
<p:button outcome="/conversationScoped.xhtml"
value="@ConversationScoped" />
<p:button outcome="/dependentScoped.xhtml"
value="@DependentScoped" />
</h:form>
</ui:composition>
</h:body>
Notequeocódigodapáginaleft.xhtmlnãotemconhecimentodapáginade
Template.Épossívelencontraratag <ui:composition>quedefinequeocódigo
aserinseridoseencontraalidentro.
Dica
Éconsideradaboapráticadeixartodoocódigoqueseráinseridovia
Templateenvolvidopelatag <ui:composition>.Avantagemdissoé
quetodocódigoqueestiverforado <ui:composition>seráignorado
pelo v i e whandlerdoJSF.Comessapráticaépossíveladicionarcódigono
<h:head>paraquesepossavisualizarapáginasemquesejanecessário
compilaroprojeto.
Lembradaimagemdaminhocaexibidanocapítulosobre16?Ocódigodapágina
estáutilizandoafuncionalidadede TemplatedoJSF2.0.
<!-- Página que exibe a minhoca utilizandoBibliotecas.xhtml -->
<h:body>
<ui:composition template="/templates/master.xhtml">
<ui:define name="divMain">
<h:button value="Ola via JavaScript" onclick="ola();" />
<br />
<p class="titulo">#{mensagens.bibliotecasTexto}</p>
<h:graphicImage library="imagens" name="minhoca.jpg" />
</ui:define>
</ui:composition>
</h:body>
77

## Página 92

CasadoCódigo
V e j acomo é simples e objetivo o código da página
utilizandoBibliotecas.xhtml. Atravésda tag ui:composition éin-
dicadoqualtemplateseráutilizado.Ecomatag ui:defineindicamosqualparte
docódigoiremossobrescrever.
Avantagemdeutilizar Facelets como Templateéqueépossívelmudar
todaaestruturadeumaaplicaçãosemafetartodasaspáginas.Notequeapágina
utilizandoBibliotecas.xhtmlnão temamínimaideiadequantosmenus
existemnaaplicação,ouseháduasoutrêsbarraslateraisnolayout.
Casoumareestruturação geralfossenecessária,com Facelets,oimpacto
aconteceriaapenasnaspáginasde Template,easpáginasqueexibemasinforma-
ções nãoseriammodificadas.
Éprecisotermuitocuidadoparanãoaninhar formshtml;paraaninharum form
bastariafazer <h:form><h:form></h:form></h:form>.Oproblemadeani-
nhar forméquecadabrowserpoderátercomportamentosinesperados,comose
perderaodarfocusaumcomponente,tabeoutros.
<!-- aninhar.xhtml -->
<ui:composition template="/templates/master.xhtml">
<h:form>
<ui:define name="divMain"><br/>
<p>Alguma coisa</p>
</ui:define>
<ui:define name="divRight"/>
</h:form>
</ui:composition>
V e j anocódigodapáginaaninhar.xhtmlqueaosubstituiro ui:define
emalguma,comalgumcódigoquecontenhaocomponente h:form, formsserão
aninhados.
Éprecisoestaratentoparanãodeixarqueessasituaçãode formaninhadoacon-
teçanaaplicação. U mproblemajápresenciadoemfórumeraquea actiondeum
botãonãoerachamada,poisobotãoestavadentrodeumfórumaninhado.
Outra facilidade do Facelets écolocar no Templateos componentes
que exibirão as mensagem para o usuário. Pode ser um h:messages ou
um p:growl do Primefaces, por exemplo. Desse modo não seránecessá-
rio declararesse componenteem todas aspáginas. V e j anocódigo da página
reutilizandoComponenteMessage.xhtml como seria possívelutilizar um
únicocomponentedemensagensparatodaaaplicação.
78

## Página 93

CasadoCódigo Capítulo17.BoautilizaçãodoFacelets
<!-- reutilizandoComponenteMessage.xhtml -->
<ui:composition template="/templates/master.xhtml">
<h:messages />
<ui:define name="divMain">
<p>Alguma coisa</p>
</ui:define>
</ui:composition>
Cuidadoaoterquesobrescreverdiversasregiões naspáginasapenasparaapagar
umtextoquenãodeveriaserexibido.Seriapossívelterumcódigodotipo:
<!-- codigo_feio.xhtml -->
<ui:composition template="/templates/master.xhtml">
<ui:define name="divLeft01"/>
<ui:define name="divLeft02"/>
<ui:define name="divMain"><br/><br/><br/>
<p>Alguma coisa</p>
</ui:define>
<ui:define name="divRight"/>
</ui:composition>
V e j aoexemplodapáginacodigo_feio.xhtml,nelasãosobrescritasdiversas
áreasparanãoexibiremdeterminadovalorpadrão. Emumapáginaououtranão
seriatantoincômodo, mascasoaconteçaemdiversaspáginasexisteummodode
evitaresseproblema:bastacriarumoutro Template. Épossíveltermaisqueum
Templateemumprojeto,demodoqueficariaorganizadoseseuprojetotivesse33%
daspáginasemum,eoutros67%emoutro Template.
79

## Página 95

Capítulo18
EnviarvaloresparaoManagedBean
Muitasvezesprecisamostransferirdadosqueestãosendoexibidosemumatabela
atravésdeum datatable,comoporexemploo iddeumainformaçãoqueque-
remoseditar.Épossívelenviarvaloresdeum datatableparaumManagedBean
dediversasmaneiras.
Paraenviarosobjetos,comodemonstradoabaixo,bastacolocarumbotãoem
umacoluna:
<!-- dataTable.xhtml -->
<h:form>
<p:dataTable value="#{cidadeMB.cidades}" var="cidade" >
<p:column>
<f:facet name="header">
#{mensagens.cidadeNome}
</f:facet>
<h:outputText value="#{cidade.nome}" />
</p:column>
<p:column>

## Página 96

18.1.Envievalorcomoparâmetropelof:setPropertyActionListener CasadoCódigo
<!-- BOTÃO AQUI -->
</p:column>
</p:dataTable>
</h:form>
OcódigodapáginadataTable.xhtmlmostraondedeveficarobotãopara
enviarumvalorparao ManagedBean.Eledeveestardentrodeum h:formpara
funcionarcorretamente.
AbaixoveremosmodosdeenviarovaloroManagedBeanmostrandoapenaso
codigodobotão.Serãomostradosaquitrêsmodosparaenviarumvalor:Utilizando
f:setPropertyActionListener,porparâmetroeporbinding.
18.1 Envie v a l o r co mo parâmetro p e l o
f:setPr o p e r t yActionListener
Esseéomododeenviaroparâmetroquenecessitademenosmétodos,emcompara-
çãocomoosoutros.Eleprecisaapenasdatag f:setPropertyActionListener
parainformaraoManagedBeanqueumalinhado dataTablefoiselecionada.
<p:commandButton value="#{mensagens.enviarValorSetProperty}"
onclick="exibirCidadeWidget.show()" update=":exibirCidadeGrid">
<f:setPropertyActionListener value="#{cidade}"
target="#{cidadeMB.cidade}" />
</p:commandButton>
public String atualizarCidade(){
cidadeDAO.atualizar(cidade);
return "cidade.xhtml";
}
A tag f:setPropertyActionListener tem como atributos value e
target. valueindicaqualoobjetoqueseráenviadoaoManagedBean; target
indicaqualoManagedBeanreceberáoobjeto.
Lembre-sedequeoescopodoManagedBeanfazdiferença. Casovocêutilize
oRequestScoped,ovalorpoderáseperder.Énecessárioentendercomofunciona
cadaescopoeutilizarotipoidealparacadacaso. ParaumManagedBeanoideal
seriaViewScoped(veja4).
ParaqueoobjetosejacorretamenteenviadoaoManagedBean,énecessárioter
métodosgetterse settersimplementadosparaoatributo.
82

## Página 97

CasadoCódigo Capítulo18.EnviarvaloresparaoManagedBean
18.2 Envie v a l o rco mo parâmetro
Outromodosimplesdeseenviarumatributoépormétodo.Essemétodoreceberá
oobjetodiretamentecomoparâmetroatravésdapágina.
<p:commandButton value="Enviar"
actionListener="#{cidadeMB.atualizarCidade(cidade)}" />
public String atualizarCidade(Cidade cidade){
cidadeDAO.atualizar(cidade);
return "cidade.xhtml";
}
Énecessárioutilizaraversão3.0doServleteaversão2.2deELparahabilitaresse
mododeenviodevalor.AversãodoELvemdojarutilizado.AversãodoServleté
definidanoweb.xml.
<web-app version="3.0"
xmlns="http://java.sun.com/xml/ns/javaee"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://java.sun.com/xml/ns/javaee
http://java.sun.com/xml/ns/javaee/web-app_3_0.xsd">
18.3 Envie v a l o rp o rBinding
Existeumatécnicachamada bindingquenadamaiséqueligarumcomponente
visualdiretamenteaumobjetonoManagedBean.
<p:dataTable value="#{cidadeMB.cidades}" var="cidade"
binding="#{cidadeMB.dataTable}" rowKey="#{cidade.id}" >
<!-- outras colunas -->
<p:column>
<p:commandButton value="Enviar"
actionListener="#{cidadeMB.selecionarCidade}" />
</p:column>
</p:dataTable>
private DataTable dataTable;
public String atualizarCidade(){
Integer rowIndex = dataTable.getRowIndex() + 1;
cidade = (Cidade) dataTable.getRowData(rowIndex.toString());
83

## Página 98

18.3.EnvievalorporBinding CasadoCódigo
cidadeDAO.atualizar(cidade);
return "cidade.xhtml";
}
Parautilizaro bindingbastaindicarnapáginaqualobjetodotipo DataTable
estaráligadoaoManagedBean.EparausarnoManagedBean,bastapegaroindexda
linhaquefoiselecionadaedepoisbuscarovalordentrodatabelaatravésdométodo
getRowData.
Oruimdessaabordageméquecriaumaacoplamentomuitoforteentreapágina
eoManagedBean,tornandomaisdifícilamanutençãodocódigo.
84

## Página 99

Capítulo19
Temasdinâmicos
Ésemprebompensaremagradarousuário,nãoapenascommaravilhosasfuncio-
nalidades,mastambémcomumvisualaomesmotempobonitoefuncionalemse
tratandodecores,imagensdefundo,tipografiaetc.
U m apráticainteressante poderia ser possuir um conjunto de temas pré-
definidos,noqualousuáriopudesseselecionarsuaopção preferida. U mMana-
gedBeandesessãopoderiaconterovalordefaultoucarregaralgumvalorpadrãodo
bancodedados.
@ManagedBean
@SessionScoped
public class UsuarioMB {
private String userCSS = "estilo.css";
private List<String> cssDisponivel;
@PostConstruct
private void init(){
cssDisponivel = new ArrayList<String>();

## Página 100

CasadoCódigo
cssDisponivel.add("estilo.css");
cssDisponivel.add("estilo2.css");
}
public String alterarEstilo(){
return null;
}
// getters e setters omitidos
}
Ométodo alterarEstilo()apenasretornanull,mantendoousuáriona
mesmapágina.
Ebastapermitirqueousuárioescolhaoestiloqueseráutilizado,porexemplo,
atravésdeum selectOneMenu:
<!-- utilizando o estilo dinâmico -->
<h:outputStylesheet library="css" name="#{usuarioMB.userCSS}" />
<!-- utilizando action que mantém usuário na mesma página -->
<p><h:outputText value="#{mensagens.troqueTema}:" /></p>
<p:selectOneMenu value="#{usuarioMB.userCSS}">
<f:selectItems value="#{usuarioMB.cssDisponivel}" />
</p:selectOneMenu>
<p:commandButton value="#{mensagens.troqueTemaTrocar}"
action="#{usuarioMB.alterarEstilo()}" ajax="false" />
Para utilizar o estilo dinâmico nas páginas, basta apontar a origem
do arquivo CSS para a saída do ManagedBean <h:outputStylesheet
library="css"name="#{usuarioMB.userCSS}”/> e um método que
retorneoestilodousuário.
Mantenha a opção escolhidap e l ousuário
A p e s a rdoexemplodessecapituloutilizartodososvaloresemme-
mória,épossívelsalvaressaconfiguraçãonobancodedados.Quandoo
usuárioentrarnaaplicação,aclasse UsuarioMBpoderiasimplesmente
acessarumobjetodasessãoebuscarovalordocsspadrãodele.
86

## Página 101

Capítulo20
Oqueeuuso?A c t i o nou
ActionListener?
U mdosmaioresdilemasduranteodesenvolvimentoemJSFéomomentoemque
devemosutilizar actionou actionListener.
OJSFtemdoismodosdetratarasaçõesdousuário.Oprimeiroépossíveldefinir
como:“ e s s eclickvaiexecutarumaaçãoeessaaçãodecidiráseousuáriopermanece
oumudadetela”.Enquantoosegundopodemosdefinircomo:“ e s s eclickrealizará
algumaação,masousuáriopermaneceránamesmatelaouseráforçadamenteredi-
recionado”.
20.1 Redirecioneo usuário co m action
<h:commandButton value="Click aqui!" action="#{managedBean.metodo}" />
public String metodo(){
// faz alguma coisa

## Página 102

20.2. T r a t eeventoscomactionListener CasadoCódigo
return "nova_pagina";
}
Retorno se m extensão
O código que mostra um exemplo de navegação return
"nova_pagina";nãoadicionaaextensãodapágina.OJSFprocurará
porumapáginacomamesmaextensãodaURLchamada.Seousuário
quechamouométodoestivernapáginahttp://site/index.jsfoJSFprocu-
raráumapáginachamada“nova_pagina.jsf”.Aoencontrarumapágina
chamada“nova_pagina.xhtml”eleentenderáqueéessearquivoodestino
final.
Oquemelhorcaracterizauma actionéummétodoqueretornaráumobjetodo
tipo String.A actionémelhorutilizadaemummétodoquedefiniráodestino
dousuário.Dessaforma,elepodepermanecernatelaqueestavaoumudarparauma
novatela.
Considerequeousuárioestejanateladecadastro,eumavezfinalizado,eleserá
redirecionadoparaateladelogin.Épossívelretornar nullefazercomqueousuá-
riopermaneçanamesmatelacasoalgumerroaconteça.
public String metodo(){
// mantém o usuário na mesma tela com todos os dados
return null;
}
20.2 Trate eventos co m actionListener
<!-- como utilizar uma actionListener -->
<h:commandButton value="Click aqui!"
actionListener="#{managedBean.metodo}" />
public void metodo(javax.faces.event.ActionEvent event){
// faz alguma coisa
}
U m adascaracterísticasdo actionListeneréqueousuáriosemprepermane-
ceránamesmatela. Essetipodemétodoémuitoutilizadoemchamada Ajax,
88

## Página 103

CasadoCódigo Capítulo20. Oqueeuuso?ActionouActionListener?
e em componentes próprios. U mactionListener recebe como parâmetroum
javax.faces.event.ActionEvent,comoqualvocêtemacesso,porexem-
plo, ao componenteque iniciou a ação. U m aboa analogia évocêassociar o
actionListenercomotratamentodeumeventodeumclique,deumaação.
ActionListenernaturalmentenão realizaráumanavegação,mesmoretornando
umaStringcomofeitoemuma A c t i o n.Pararealizarumanavegaçãoapartirdeum
métodoActionListenerseránecessárioutilizarométodosendRedirect.Paraexe-
cutarum sendRedirectbastafazercomonocódigoexibido:
FacesContext.getCurrentInstance()
.getExternalContext()
.redirect("/site.jsf”);
Notequeapesardeométodosechamar redirecteleécomumentechamado
de sendRedirect,utilizadoatravésdaclasse HttpResponse. sendRedirect.
Casoapareçaalgumamensagemdeerroaoexecutarfaçacomoabaixo:
response.sendRedirect();
FacesContext.getCurrentInstance().responseComplete();
OmétodoresponseComplete()implicitamenteinformaaoJSFquenãoserá
necessáriotrabalharo response.
89

## Página 105

P a r t eIV
Aproveiteasbibliotecasde
componentes
Quandoestamosdesenvolvendoumaaplicação,muitasvezesprecisamosqueos
elementosqueenvolvemanossatelatenhamcaracterísticasdiferentesdasquepor
padrãoelaspossuem.Porexemplo,gostaríamosdeterumcampodetextoondefosse
possíveladicionarumamáscara.Ouentão,um dataTablequefizesseordenação
dosdadosdentrodeleeassimpordiante.Nessecaso,precisamosdecomponentes
diferentes.Podemosencontraressescomponentesembibliotecas,desenvolvidase
disponíveisemvariadasformasnacomunidade.
Bibliotecasdecomponentessão focadasmaisnapartedefuncionalidades,em
geral,criando dialogs, datatables, galeriasetc,nasquais,entreasprincipais,sedes-
tacamoPrimefaces,Richfaces,IcefaceseOmniFaces.Aliásépossívelquequalquer
pessoapossacriarsuabibliotecadecomponenteedisponibilizá-laparaoutrosde-
senvolvedoresoureutilizá-laemdiferentesprojetos.
NestapartedolivroveremossobrealgumascaracterísticasdoPrimefaces,Ri-
chfaces,IcefaceseOmniFaces.Vantagensedesvantagenseexemplosdecódigode
funcionalidadesricaseinteressantesqueconseguimosfazercomessasbibliotecas.
Osexemplosdemonstradosaquinãosãoparacompararumabibliotecacoma
outra.Seusexemplosforamescolhidosapenasaleatoriamente.Hácomponentesque
existememtodasasbibliotecas,masoutrosapenasemuma.

## Página 106

Dica
Noscódigosapresentadosnolivroforamutilizadosdiversosnomes
demétodos,atributos,classesemportuguêsjustamenteparamostrarque
onomenãoinfluencianocomportamentodaação. Algunstutoriaisda
internetutilizamdenomesestranhoseàsvezesabusivosporacharem
queésócomaquelenomequetudoseresolve.

## Página 107

Capítulo21
Primefaces
Éconsideradopormuitosomaisavançadodomercado.Eletemdiversasfunciona-
lidadesprontasquefacilitamemuitoavidadodesenvolvedor.Possuimaisde130
componentesemseushowcasecomcódigoqueexplicacomoutilizar.
21.1 Da t aTableco m seleção co m u m click
U mDataTablepodeterdiversasconfigurações eajustesparamelhorarausabilidade
dousuário.U mmododeutilizaroDataTabledoPrimefacesbeminteressanteéper-
mitirquecomapenasumcliqueeleexibaovalordalinhaselecionada.

## Página 108

21.1.DataTablecomseleçãocomumclick CasadoCódigo
Figura21.1:DataTablePrimefacesseleçãoemumclique
Figura21.2:DataTablePrimefacesseleçãoemumclique
94

## Página 109

CasadoCódigo Capítulo21.Primefaces
Pelasimagens21.1e21.2épossívelvercomoéinteressanteaabordagemdeum
cliqueparaexibirosdadosdalinhaselecionada.Aaçãodocliquepoderiaserqual-
queraçãocomoexcluir,alteraretc.
Ecomoficariaocódigo?V e j aemseguidacomoésimples.
<!-- dataTable.xhtml -->
<h:form>
<p:dataTable value="#{primefacesMB.cidades}"
var="cidade"
selection="#{primefacesMB.cidade}"
selectionMode="single"
paginator="true"
rows="10"
paginatorTemplate="{CurrentPageReport}
{FirstPageLink}
{PreviousPageLink} {PageLinks}
{NextPageLink} {LastPageLink}
{RowsPerPageDropdown}"
rowsPerPageTemplate="5,10,15"
style="width: 40%"
lazy="true">
<p:ajax event="rowSelect"
update=":cidadeDialogForm"
oncomplete="cidadeWidget.show()"/>
<p:column>
<f:facet name="header">
#{mensagens.cidadeId}
</f:facet>
<h:outputText value="#{cidade.id}"/>
</p:column>
<p:column>
<f:facet name="header">
#{mensagens.cidadeNome}
</f:facet>
<h:outputText value="#{cidade.nome}"/>
</p:column>
<p:column>
<f:facet name="header">
#{mensagens.cidadeEstado}
</f:facet>
<h:outputText value="#{cidade.estado}"/>
95

## Página 110

21.1.DataTablecomseleçãocomumclick CasadoCódigo
</p:column>
</p:dataTable>
</h:form>
V e j aquenocódigo<!--dataTable.xhtml-->,queéumcódigofácildeenten-
der e de trabalhar, o atributo selection="#{primefacesMB.cidade}”
aponta onde ficará armazenada a linha selecionada. O atributo
selectionMode="single" éutilizado para definir os tipos de seleção pos-
sível. OoutropedaçodecódigorelativoaocliqueúnicoéachamadaA j a xpara
mostrarovaloremum dialog.
<p:ajax event="rowSelect"
update=":cidadeDialogForm"
oncomplete="cidadeWidget.show()"/>
A tag p:ajax tem o atributo event que informa qual ação deve
ser executada. update realizaráatualização de um componente.
oncomplete="cidadeWidget.show()"exibiráo dialogdecidades.
<!-- dialog.xhtml -->
<p:dialog widgetVar="cidadeWidget"
modal="true"
header="#{mensagens.cidade}">
<h:form id="cidadeDialogForm">
<h:panelGrid columns="2">
<h:outputText value="#{mensagens.cidadeId}"/>
<h:outputText value="#{primefacesMB.cidade.id}"/>
<h:outputText value="#{mensagens.cidadeNome}"/>
<h:outputText value="#{primefacesMB.cidade.nome}"/>
<h:outputText value="#{mensagens.cidadeEstado}"/>
<h:outputText value="#{primefacesMB.cidade.estado}"/>
</h:panelGrid>
</h:form>
</p:dialog>
Nocódigodapáginadialog.xhtmlépossívelvercomoutilizarumadialog
paraexibirovalor.Apropriedade widgetVaréumaformadefacilitarautilização
dejQuery/JavaScriptdentrodeum xhtml;achamada Ajaxexecutaocomandodo
widgetVarassim: cidadeWidget.show().
OManagedBeantemapenasget/setdoatributo: List<Cidade> cidades.
96

## Página 111

CasadoCódigo Capítulo21.Primefaces
21.2 Drag andDr o p
U m afunção queagradamuitoaosusuáriosdeaplicações éochamadoDragand
Drop,ouseja,arrastarobjetosdeumladoelargá-losemoutro.
Figura21.3:DragandDrop
97

## Página 112

21.2.DragandDrop CasadoCódigo
Figura21.4:DragandDrop
98

## Página 113

CasadoCódigo Capítulo21.Primefaces
Figura21.5:DragandDrop
Asimagens21.3,21.4e21.5mostramqueéumafuncionalidademuitointeressante
queatualmenteéfácildeencontraremdiversosprogramas.Ocódigoécomposto
99

## Página 114

21.2.DragandDrop CasadoCódigo
dedoiscomponentes p:fieldseteumoutrochamado p:droppable.
<p:fieldset legend="#{mensagens.primefacesEscolhaFotoMinhoca}">
<p:dataGrid id="fotosDisponiveis"
var="foto"
value="#{primefacesMB.fotos}"
columns="3">
<p:column>
<p:panel id="panelFotos"
header="#{foto.nome}"
style="text-align:center">
<h:panelGrid columns="1"
style="width:100%">
<p:graphicImage value="#{foto.path}"/>
</h:panelGrid>
</p:panel>
<p:draggable for="panelFotos"
revert="true"
handle=".ui-panel-titlebar"
stack=".ui-panel"/>
</p:column>
</p:dataGrid>
</p:fieldset>
Oprimeiro p:fieldSetéoqueexibeoselementosdisponíveisparaserem
arrastados.Dentrodeleépossívelencontrarum dataTable.Alistautilizadano
dataTableéList<Foto> fotos,ondeaclassefototemapenasduas Strings;a
primeiraStringéonomedafoto,easegunda,ocaminhofísicodafoto(porexem-
plo, /home/uaihebert/fotos). Ocomponente p:draggableéquemconfi-
guraqualobjetodatelapoderáserarrastado;eletemoatributo for,queaponta
quempoderáserarrastado;oparâmetro revert,queindicaquecasooobjetoseja
largadoemumlugarinválidoeledevevoltaraoseulugardeorigem;osparâmetros
handle,queestãofalandoqualclasseservirádeativadorparasemoveroobjeto,e
nocasofoiescolhidootítulodopanel–ousuárionãoconseguirámoveroobjetoa
nãoserpelotítulo; stack,quecontrolaautomaticamenteo“arrastar”docompo-
nente.
<p:fieldset id="fotosSelecionadas"
legend="#{mensagens.primefacesFotosSelecionada}"
100

## Página 115

CasadoCódigo Capítulo21.Primefaces
columns="3">
<p:outputPanel id="fotosDespejadas">
<h:outputText value="#{mensagens.primefacesArrasteAqui}"
rendered="#{empty primefacesMB.fotosSelecionadas}"
style="font-size:24px;"/>
<p:dataGrid var="foto"
value="#{primefacesMB.fotosSelecionadas}"
rendered="#{not empty
primefacesMB.fotosSelecionadas}">
<p:column>
<p:panel id="panelFotos"
header="#{foto.nome}">
<p:graphicImage value="#{foto.path}"/>
</p:panel>
</p:column>
</p:dataGrid>
</p:outputPanel>
</p:fieldset>
Osegundo p:fieldSetnadamaisédoqueoresponsávelporexibirosdados
dasfotosqueforamarrastadas.Logoabaixodo p:fieldSetviráoúltimocompo-
nentequedefiniráondeumobjetopoderáserjogado.
<p:droppable for="fotosSelecionadas"
tolerance="touch"
activeStyleClass="ui-state-highlight"
datasource="fotosDisponiveis"
onDrop="handleDrop">
<p:ajax listener="#{primefacesMB.fotoDespejada}"
update="fotosDespejadas fotosDisponiveis"/>
</p:droppable>
Ocomponente p:droppable definequalobjetoreceberáosobjetosjoga-
dos. for apontaqual componenteseguraráo objeto jogado; tolerance
aponta qual o tipo de ação para que ele considere que o objeto foi jogado;
activeStyleClass definequal estilo o componentequereceberáum objeto
teráenquantoelenão forjogado: vernafoto21.4. datasourceéocompo-
nentequecontémosobjetosquepoderão serarrastadose onDropéação que
seráexecutada(queveremosembreve). Existetambémumlistenerquerealiza
101

## Página 116

21.3.Notificador CasadoCódigo
atransferênciadafotodeumalista( #{primefacesMB.fotos})paraoutra(
#{primefacesMB.fotosSelecionadas}).
// método executado pelo listener
public void fotoDespejada(DragDropEvent event) {
Foto foto = (Foto) event.getData();
getFotos().remove(foto);
getFotosSelecionadas().add(foto);
}
function handleDrop(event, ui) {
var droppedCar = ui.draggable;
droppedCar.fadeOut('fast');
}
Efeito jQuery disparado pelo evento onDrop definido no componente
droppable
21.3 Notificador
Énormalenviarumarespostaparausuárioindicandoseaaçãofoirealizadaounão.
“Salvocomsucesso”,“Erroaoalterar”ou“Vocêtemcerteza? Sériomesmo?”são
mensagensquesãoexibidasparaosusuáriosdeaplicações.
V e j anasimagens21.6e21.7uminteressanterecursochamadoGrowl.
Figura21.6:DragandDrop
102

## Página 117

CasadoCódigo Capítulo21.Primefaces
Figura21.7:DragandDrop
ParautilizaroGrowlbastausarumcódigobastantesimpleseobjetivo:
<!-- growl.xhtml -->
<h:form>
<p:growl id="mensagens"/>
<h:outputText value="#{mensagens.mensagemSucesso}:"/>
<p:commandButton value="#{mensagens.enviar}"
actionListener="#{primefacesMB.mensagemSucesso}"
update="mensagens"/>
<h:outputText value="#{mensagens.mensagemErro}: "/>
<p:commandButton value="#{mensagens.enviar}"
actionListener="#{primefacesMB.mensagemErro}"
update="mensagens"/>
</h:form>
Ocódigodapáginagrowl.xhtmltemumcomponente p:growlqueéo
responsávelpormostraramensagemaousuário.Seucomportamentoéexatamente
igualaocomponente h:messagesdoJSF.Osbotões exibidosnaspáginasnada
maisfazemdoqueumachamada Ajaxquecriaamensagemaserexibida.Aofinal
dachamada Ajaxosbotões estãoconfiguradosparaatualizaremo growlatravésdo
atributo update="mensagens".
Parafazercomqueumamensagemsejaexibidaparaumusuário,bastafazer
comoocódigoaseguir:
private final String SUCESSO = "Operação realizada com sucesso";
private final String ERRO = "Ops! Ocorreu um erro inesperado";
public void mensagemSucesso(ActionEvent event) {
FacesContext instance = FacesContext.getCurrentInstance();
instance.addMessage(null,
103

## Página 118

21.4.AutoComplete CasadoCódigo
new FacesMessage(FacesMessage.SEVERITY_INFO,
SUCESSO,
SUCESSO)
);
}
public void mensagemErro(ActionEvent event) {
FacesContext instance = FacesContext.getCurrentInstance();
instance.addMessage(null,
new FacesMessage(FacesMessage.SEVERITY_ERROR,
ERRO,
ERRO)
);
}
21.4 Au t oComplete
OA u t oComplete,comodizonome,completaumainformaçãoqueousuárioestá
digitandoemum input.Assimcomonogoogle,épossívelteressemesmocompor-
tamentocomoPrimefaces.V e j anaimagem21.8e21.9comoficaessecomponente.
Figura21.8:AutoComplete
104

## Página 119

CasadoCódigo Capítulo21.Primefaces
Figura21.9:AutoComplete
Essecomponenteéaltamenteconfiguráveledeveserutilizadocomcautela.
<!-- autoComplete.xhtml -->
<p:autoComplete id="autoComplete"
forceSelection="true"
minQueryLength="3"
value="#{primefacesMB.cidade}"
completeMethod="#{primefacesMB.autoComplete}"
var="cidade"
itemLabel="#{cidade.nome}"
itemValue="#{cidade}"
label="#{mensagens.cidade}"
dropdown="true"
required="true"
queryDelay="3000"/>
<br/>
<p:commandButton value="#{mensagens.enviar}"
update=":cidadeDialogForm"
oncomplete="cidadeWidget.show()"/>
NotenocódigodapáginaautoComplete.xhtmlaquantidadedeconfigura-
ções (amaiorianãoobrigatória)queépossívelter,eexistemoutrasquenãoforam
utilizadas. forceSelectionindicaseaseleção dealgumvaloréobrigató-
ria,paraevitarqueousuáriodeixeumvalorqualquer,comoumacidadechamada
123***. minQueryLengthéaquantidademínimadecaracteresnecessáriospara
dispararachamadanoManagedBean. valueteráovalorselecionadopelousuá-
rio. completeMethod="#{primefacesMB.autoComplete}”éométodoque
retornaráalistafiltradapelovalorinformadopelousuário. varéonomeque
umitemdalistaretornadanométododefinidono completeMethodretornará;
105

## Página 120

21.4.AutoComplete CasadoCódigo
itemLabeléonomequeseráexibidoaousuário;e itemValueovalorselecio-
nadoqueseráenviadoaoManagedBean. dropdown="true"exibeounãoobotão
paraexibirosvalores.
queryDelay éum contadorpara disparara chamada Ajax. Imagineque
ousuáriodigitouABCqueéotamanhomínimodeumapesquisadefinidoem
minQueryLength.Aoatingir3caracteresoPrimefacesiniciaráumcontadorcom
umtempodefinidoemmilissegundosnaopção queryDelay.Casoousuárioedite
otexto,otempodeesperaseráreiniciado.Achamada Ajaxsomenteserádisparada
quandootempodeesperaforzerado.
// metodoAutoComplete.java
public List<Cidade> autoComplete(String valorPesquisado) {
final int maximoResultadosExibidos = 5;
if (valorPesquisado == null || valorPesquisado.isEmpty()) {
int comecarPesquisaPosicao = 1;
return cidadeDAO.buscaPorPaginacao(comecarPesquisaPosicao,
maximoResultadosParaExibido);
}
return cidadeDAO.findByNameLike(valorPesquisado,
maximoResultadosParaExibido);
Ométododaclasse MetodoAutoComplete.javaébemsimpleseretorna
umalista.Elerecebeumvalorenviadopelousuárioetestaseovalortemumparâ-
metropreenchido.Seousuárioclicarnobotãodo dropdownessevalornãoviria
preenchido.
Fiqueatentoaumdetalhe:todavezqueumvalordeumcomponente select
forumobjeto,seránecessárioum Converter.Emnossocasoo itemValuefoi
definidocom #{cidade}.
// CidadeConverter.java
@FacesConverter(forClass = Cidade.class)
public class CidadeConverter implements Converter {
@Override
public Object getAsObject(FacesContext arg0, U
IComponent arg1,
String key) {
CidadeDAO cidadeDAO = // busca o DAO;
106

## Página 121

CasadoCódigo Capítulo21.Primefaces
return cidadeDAO.findById(Integer.parseInt(key));
}
@Override
public String getAsString(FacesContext arg0,
UIComponent arg1,
Object cidadeObject) {
if(cidadeObject != null && cidadeObject instanceof Cidade){
Cidade cidade = (Cidade) cidadeObject;
return String.valueOf(cidade.getId());
}
return "";
}
}
U mconverternormaldeJSFquesimplesmenteconverteumvalorenviadopela
V i e wemobjetoouretornaoIDdoobjeto.
Dica
É preciso tomar bastante cuidado com a configuração/utilização
de um Converter. A anotação @FacesConverter(forClass =
Cidade.class) foiutilizadaparadefinirquetodaclasse Cidade
da aplicação utilizaráesse Converter. Infelizmentealgumas im-
plementações simplesmente ignoram esse valor da anotação e não
encontram o converter. A solução seria utilizar a anotação assim:
@FacesConverter(value = "cidadeConverter"). Eemcada
componentequenecessitassedeum Converterfazerusodoseguinte
atributo:converter="cidadeConverter”.
21.5 Poll
ExisteumrecursointeressantedoJSFqueérealizarchamadasaumManagedBean
semanecessidadedeserdisparadaporumusuário.Emoutraspalavras,oPrimefaces
automaticamentedisparachamadasemumperíodopredeterminadopormeiodo
componente Poll.
107

## Página 122

21.5.Poll CasadoCódigo
Figura21.10:Poll
Essecomponenteésimplesdeconfigurar.
<h:form>
<h:outputText id="contadorText"
value="#{mensagens.contadorTexto}:
#{primefacesMB.contador}"/>
<p:poll interval="3"
listener="#{primefacesMB.somar}"
update="contadorText"/>
</h:form>
Ocomponente p:pollrealizaráumachamada Ajaxacada3segundosaoMa-
nagedBeaneaofinaldachamadaatualizaráo outputTextparaexibironovovalor.
private int contador;
public void somar(){
contador++;
}
public int getContador() {
return contador;
}
public void setContador(int contador) {
this.contador = contador;
}
Ocomponente p:pollaquifoiutilizadocomoumcontador,maspoderiaser
utilizadoparaverificarseousuáriocontinuanapáginadosistema,porexemplo.
108

## Página 123

CasadoCódigo Capítulo21.Primefaces
21.6 Considerações finais
Atravésdoscomponentesexibidosfoipossívelverqueexistemdiversasfuncio-
nalidadesprontasequefuncionamsemanecessidadedecódigoscomplicadose
enormes. TodososexemplosforamretiradosdoshowcasedopróprioPrimefa-
ces:http://primefaces.org/showcase/.Épossívelfazerodownloaddocódigofonte
(SVN)detodososexemplosaqui:http://repository.primefaces.org/org/primefaces/
prime-showcase/.
EmseufórumépossívelfalardiretamentecomosmantenedoresdoPrimefaces.
Láelestiramdúvidaseatéregistrambugsparafuturosreparos.Émuitoutilizadoem
meioacadêmico(porjávircomumbeloCSS)eporsuafacilidadedeutilização.Os
exemploscitadosacimasãobemfáceisdeseremutilizadoseaplicadoscompoucas
linhasdecódigo.
Infelizmentenemtudosãoflores:existetambémo "Dark Side”doPrimefaces.
Elesnãosepreocupamnemumpoucocom retrocompatibilidade.Émuitocomum
vernainternetpessoasdizendo:“ e umudeidaversãoxparaax.1eatelaparoude
funcionar”.
Éprecisoterbastantecuidadoaomudardeversão,essecomponenteaindanão
estáconfiávelquantoamudanças. U mnovocomportamentointeressantedelesé
que,antigamenteaomudardeversão,casoumparâmetrofosseeliminadodeum
componente,atelaapresentariaerro.Hojeemdia,diversoscomponentesqueen-
contramumparâmetroquefoieliminadonãodãomaisamensagemdeerro.Aquele
parâmetrosimplesmentepassaaserignorado.
109

## Página 124

21.6.Considerações finais CasadoCódigo
Esteja atento
Nocapítulo20vimosquandoecomoutilizaractioneactionListener.
É preciso estar atento ao fato de que o componente
p:commandButtondoPrimefacesutilizaajaxporpadrão. Énormal
encontrarna internetdesenvolvedoresreclamandoque determinado
métodonãoéchamado,ouentãoqueanavegaçãodométodonãoestá
sendofeita.
Comovimosnocapítulo20,apenasuma actionexecutaumanavega-
çãodemodonatural.ÉnecessáriodesativaroajaxdocommandButton
paraqueuma actionsecomportenormalmente. Bastadefinirqueoa
opção ajaxsejaiguala false.
<p:commandButton ajax="false" />
Nadocumentação doPrimefaces(http://primefaces.org/documentation.html)
é possível encontrar todos os estilos de todos os componentes, como
cor/fonte/configuraçãodecss,epodemseralterados.
110

## Página 125

Capítulo22
TemasDinâmicoscomPrimefaces
U m adasvantagensdoPrimefaceséaquestãodotema. Existemdiversostiposde
temasjáprontosparaseremutilizadoseamaiorvantageméqueodesenvolvedor
tambémpodecriareutilizar.
V e j acomésimplesfazerusodeumtemadoPrimefaces.Primeirovamosutilizar
oManagedBeandesessãodousuárioparasaberqualoseutema.
// imports omitidos
@ManagedBean
@SessionScoped
public class UsuarioMB {
private String tema;
public String getTema() {
if(tema == null){
tema = "casablanca";
}

## Página 126

CasadoCódigo
return tema;
}
// outros métodos omitidos
}
V e j aquenaclasse UsuarioMBencontra-seumaStringchamada temaque
indicaráaoPrimefacesqualotemadousuário.U mdetalheinteressanteéquenoget
éfeitoumtesteparasaberseo temaestánullounão,serianessemomentoque,caso
o temaestivesse null,sepegariaainformaçãodousuáriologadonaaplicação.
Paradeixaraescolhadotemahabilitadoparaousuário,bastariautilizarocom-
ponentechamado ThemeSwitcherdopróprioPrimefaces.
<p:themeSwitcher value="#{usuarioMB.tema}">
<f:selectItems value="#{temasDisponiveis.temas}" />
</p:themeSwitcher>
@ApplicationScoped
@ManagedBean
public class TemasDisponiveis {
private List<String> temas;
public List<String> getTemas() {
if(temas == null){
temas = new ArrayList<String>();
temas.add("casablanca");
temas.add("cupertino");
temas.add("dark-hive");
temas.add("bluesky");
temas.add("blitzer");
}
return temas;
}
public void setTemas(List<String> temas) {
this.temas = temas;
}
}
Bastacolocarocomponente ThemeSwitcherdentrodeum h:formque,por
Ajax,oPrimefacestrocarátodaainterfacedeseuscomponentes.Notequefoicriado
112

## Página 127

CasadoCódigo Capítulo22.TemasDinâmicoscomPrimefaces
umManagedBeancomoescopo ApplicationScopedqueconterátodosostemas
daaplicação.
Eporúltimo,seránecessáriaumapequenaconfiguraçãonoweb.xmldaaplica-
ção.Ocódigoadicionadonoweb.xmlinformaráaoPrimefacesondebuscarotema;
emnossocaso,noManagedBean.
<context-param>
<param-name>primefaces.THEME</param-name>
<param-value>#{usuarioMB.tema}</param-value>
</context-param>
Eparaousuáriotrocarotemaatualporoutrosserábemsimples.V e j anasima-
gens22.1,22.2e22.3.
Figura22.1:T e m aselecionado
113

## Página 128

CasadoCódigo
Figura22.2:Escolhendonovotema
Figura22.3:Novotemaaplicado
É possível criar um evento ajax para persistir a alteração no
banco de dados para o usuário. Basta adicionar a linha <p:ajax
listener="#{usuarioMB.salvarTemaNoDB}"/> dentro do componente
ThemeSwitcherque,via Ajax,oPrimefaceschamaráessemétodoeessevalor
poderáserpersistido.
114

## Página 129

CasadoCódigo Capítulo22.TemasDinâmicoscomPrimefaces
Dica
Notequeoobjeto temadaclasse UsuarioMBéapenasumaString.
Emdiversostutoriais,livroseatémesmonoshowcasedoPrimefacessão
utilizadasclassesparaessevalor.
NestelivrofoiutilizadaaabordagemdeStringparaficarmaisfácilo
entendimentoeaplicação.
Amelhorpartedessahistóriaéqueparautilizarumdessestemasbastaadicionar
ostemaspredefinidosnopom.xmlounapasta WEB-INF/lib.
<!-- pom -->
<dependency>
<groupId>org.primefaces.themes</groupId>
<artifactId>cupertino</artifactId>
<version>${primefaces.tema}</version>
<scope>runtime</scope>
</dependency>
<dependency>
<groupId>org.primefaces.themes</groupId>
<artifactId>dark-hive</artifactId>
<version>${primefaces.tema}</version>
<scope>runtime</scope>
</dependency>
<dependency>
<groupId>org.primefaces.themes</groupId>
<artifactId>casablanca</artifactId>
<version>${primefaces.tema}</version>
<scope>runtime</scope>
</dependency>
<dependency>
<groupId>org.primefaces.themes</groupId>
<artifactId>bluesky</artifactId>
<version>${primefaces.tema}</version>
<scope>runtime</scope>
</dependency>
<dependency>
<groupId>org.primefaces.themes</groupId>
<artifactId>blitzer</artifactId>
115

## Página 130

CasadoCódigo
<version>${primefaces.tema}</version>
<scope>runtime</scope>
</dependency>
Paracriarseuprópriotemaváaosite:http://jqueryui.com/themeroller/.Nesse
siteépossívelestilizarosaspectosvisuaisdaaplicação;nomanualdoPrimefacesé
mostradocomoaplicaressetemarecém-criadoaoseuprojeto.
116

## Página 131

Capítulo23
ComponentesdoPrimefacesnão
Aparecem
Éfácilperderbonsminutosprocurandonainternetasoluçãoparaesseproblema.
Àsvezestemosumcódigotodocorreto,masoinfelizdocomponentedoPrimefaces
nãoaparecepornada.
<head>
</head>
<body>
<!-- exemplo.xhtml -->
<p:button value="Ola" />
</body>
Pormaisqueumcódigopareçacorreto,oPrimefacestemassuasregraspara
funcionar.Ocódigodoarquivo exemplo.xhtmlmostraumapáginacomtodos
osblocosnecessáriosdalinguagemHTML.Agrandepegadinhaaíéqueoscompo-
nentesnoPrimefacesnecessitamde h:headenão head,ede h:bodyemvezde

## Página 132

CasadoCódigo
apenas body.Essepequenodetalhefaztodadiferença.
Aindaexisteumporém.Às vezes,mesmoemumapáginacom h:heade
h:bodyocomponentenãoiráaparecer.
<h:head>
</h:head>
<h:body>
<!-- exemplo2.xhtml -->
<p:editor value="" />
</h:body>
Mesmoapáginaexemplo2.xhtmlcontendo h:heade h:bodyemalgumas
versões doPrimefacesessecomponentepodenãoaparecer.Qualseriaomotivo?
Diversos componentes do Primefaces necessitam estar envoltos pela tag
h:form. Nocódigoacimabastariacolocaratag h:formantesdo p:editore
fechá-laapóso p:editor.
118

## Página 133

Capítulo24
Richfaces
ORichfaceséumavelhabibliotecadecomponentesdoJSF,massivamenteutilizado
noJSF1.2.Suautilização noJSF1.2eraidealparacenáriosquenecessitassemde
Ajax.
Atualmentearecémversão4foilançadaparavoltaraconcorrercomasoutras
bibliotecasdomercado,quehojetemofoconoJSF2.0.ORichfacestembastantes
componentesdesenvolvidos,equefacilitamousododesenvolvedor.
24.1 Da t aTableco mColunasCongeladas
Afunção decongelarcolunasépossíveldeserutilizadanoExcelepodeseralgo
muitopráticonasaplicações JSF.ORichfacestemessafunção.

## Página 134

24.1.DataTablecomColunasCongeladas CasadoCódigo
Figura24.1:DataTablecomColunasCongeladas
Figura24.2:DataTablecomColunasCongeladas
120

## Página 135

CasadoCódigo Capítulo24. Richfaces
Figura24.3:DataTablecomColunasCongeladas
Asimagens24.1,24.2e24.3mostramcomoesserecursoéinteressanteparame-
lhorarautilizaçãodosusuáriosacostumadoscomessafacilidade.
<!-- dataTable.xhtml -->
<rich:extendedDataTable value="#{richfacesMB.cidades}"
var="cidade"
frozenColumns="2"
style="height:250px; width:400px;"
selectionMode="none">
<f:facet name="header">
<h:outputText value="#{mensagens.cidadePlural}"/>
</f:facet>
<rich:column>
<f:facet name="header">
<h:outputText value="#{mensagens.cidadeNome}"/>
</f:facet>
<h:outputText value="#{cidade.nome}"/>
</rich:column>
<rich:column>
<f:facet name="header">
<h:outputText value="#{mensagens.cidadeEstado}"/>
</f:facet>
121

## Página 136

24.2. T o o lTip CasadoCódigo
<h:outputText value="#{cidade.estado}"/>
</rich:column>
<rich:column>
<f:facet name="header">
<h:outputText value="#{mensagens.cidadeTotalRuas}"/>
</f:facet>
<h:outputText value="#{cidade.totalRuas}"/>
</rich:column>
<!-- outras 1000 colunas -->
</rich:extendedDataTable>
ODataTable,apesardeterumfuncionamentodiferente,temsuaconfiguração
bemparecidacomadequalqueroutroDataTable.Oqueotornadiferenteéacon-
figuração frozenColumns="2"quedeterminaaquantidadedecolunasaserem
congeladas.
24.2 To o lTip
AferramentadeT o o lTipébemcomumnomundoweb,bastapassaromouseque
umainformaçãosobreaquelaáreaseráexibida.Aimagem24.4mostracomoessa
ferramentafuncionacomoRichfaces.
Figura24.4:T o o lTipNormal
<rich:panel>
#{mensagens.richfacesToolTipNomal}
<rich:tooltip>
#{mensagens.richfacesToolTipNomalTexto}
</rich:tooltip>
</rich:panel>
O código para exibir um Tool Tip precisa apenas do componente
rich:tooltipdentrodaregiãoemqueeledeveserexibido.ORichfacestemou-
trasconfigurações possíveisparaum Tool Tip.
Aimagem24.5mostracomoseriaumT o o l T i pcom delay.
122

## Página 137

CasadoCódigo Capítulo24. Richfaces
Figura24.5:T o o lTipcomDelay
<rich:panel>
<h:outputText value="#{mensagens.richfacesToolTipDelay}"/>
<rich:tooltip followMouse="false" showDelay="2000">
<h:outputText value="#{mensagens.richfacesToolTipDelayTexto}"/>
</rich:tooltip>
</rich:panel>
O delayéusadoparaatrasaraexibiçãodo Tool Tipparaousuário.Parauti-
lizaro delaybastaconfigurarcomoatributo showDelay="2000"queotextodo
Tool Tipseráexibidoapósdoissegundos.Oatributo followMouse="false"
foiutilizadoparainformaraoRichFacesqueo Tool Tipnãodeveseguiromouse.
Aimagem24.6mostracomoseriaumT o o l T i pcomumtextochamadovia Ajax.
Figura24.6:T o o lTipviaA j a x
<h:form>
<rich:panel>
<h:outputText value="#{mensagens.richfacesToolTipAjax}"/>
<rich:tooltip mode="ajax">
<h:outputText value="#{mensagens.richfacesToolTipAjaxTexto}"/>
<h:outputText value="#{richfacesMB.contadorAjax}"/>
</rich:tooltip>
</rich:panel>
</h:form>
Paraqueumamensagemexibidasejacarregadavia Ajaxbastautilizaroatri-
buto mode="ajax".Oget/setdoatributocontadorAjaxsãonormaiscomaúnica
diferençadequeaumentamocontadoracadachamada.
123

## Página 138

24.2. T o o lTip CasadoCódigo
public int getContadorAjax() {
return ++contadorAjax;
}
public void setContadorAjax(int contadorAjax) {
this.contadorAjax = contadorAjax;
}
U m aoutraopçãointeressanteéadeexibiro Tool Tipapenasapósoclique.E
paratornaressaopçãomaisinteressanteumachamada Ajaxpoderiaserexecutada
apósoclique.
Aimagem24.7mostracomoseriaum Tool Tipcomumcliquee Ajax.
Figura24.7:T o o lTipviaA j a x
<rich:panel>
<h:outputText value="#{mensagens.richfacesToolTipPorClique}"/>
<rich:tooltip followMouse="false" showEvent="click" mode="ajax">
<h:outputText value="#{mensagens.porCliqueTexto}"/>
<h:outputText value="#{richfacesMB.contadorClique}"/>
</rich:tooltip>
</rich:panel>
ParadefinirqueumT o o l T i ppodeserapenasexibidoapósocliquebastautilizar
oatributo showEvent="click",eumget/setnoManagedBean.
public int getContadorClique() {
return contadorClique++;
}
public void setContadorClique(int contadorClique) {
this.contadorClique = contadorClique;
}
124

## Página 139

CasadoCódigo Capítulo24. Richfaces
24.3 Lo g
U m aferramentaquepodeajudaremrequisições Ajaxéaferramenta Log.Aima-
gem24.8mostracomoaferramenta Logtrabalha.
Figura24.8:LogdechamadasA j a x
Notequesãoexibidasasinformações relacionadasàchamada Ajax.Épossível
tambémrealizarchamadascomoutrosníveisdeLog(verníveldebug24.9).
Figura24.9:LogdechamadasA j a xcomlogemDebug
Eparautilizaresserecursoénecessárioadicionarumsimplescomponenteà
página:<a4j:log/>.Elerealizarátodootrabalhodecolocarachamada Ajaxeexibir.
Ocódigodapáginaexibidanasimagenspodeserencontradoabaixo.
125

## Página 140

24.4. PanelMenu CasadoCódigo
<h:form>
<h:inputText value="#{richfacesMB.nomeEnviado}"/>
<a4j:commandButton value="#{mensagens.enviar}"
render="textoEnviado"/>
<br/>
<a4j:outputPanel id="textoEnviado">
<h:outputText value="Hello #{richfacesMB.nomeEnviado}!"
rendered="#{not empty richfacesMB.nomeEnviado}"/>
</a4j:outputPanel>
</h:form>
<a4j:log/>
24.4 PanelMenu
O Panel Menuéumcomponentequeajudanaorganização dematerial,eaté
mesmofacilitaanavegação dousuário.V e j anaimagem24.10comoeleévisual-
mente.
Figura24.10:PanelMenu
Ointeressantedessecomponenteéqueelefuncionacomoumagrupadordecon-
126

## Página 141

CasadoCódigo Capítulo24. Richfaces
teúdo,temefeitoJqueryaosetrocardeblocosdecódigoseépossívelintegrarcom
chamadas Ajax.
<rich:panelMenu itemMode="ajax"
groupMode="ajax"
groupExpandedLeftIcon="triangleUp"
groupCollapsedLeftIcon="triangleDown"
topGroupExpandedRightIcon="chevronUp"
topGroupCollapsedRightIcon="chevronDown"
itemLeftIcon="disc"
itemChangeListener="#{richfacesMB.atualizarGrupoSelecionado}">
<rich:panelMenuGroup label="#{mensagens.richfacesGrupo} 1">
<rich:panelMenuItem label="Item 1.1" name="Item_1_1"/>
<rich:panelMenuItem label="Item 1.2" name="Item_1_2"/>
<rich:panelMenuItem label="Item 1.3" name="Item_1_3"/>
</rich:panelMenuGroup>
<rich:panelMenuGroup label="#{mensagens.richfacesGrupo} 2">
<rich:panelMenuItem label="Item 2.1" name="Item_2_1"/>
<rich:panelMenuItem label="Item 2.2" name="Item_2_2"/>
<rich:panelMenuItem label="Item 2.3" name="Item_2_3"/>
<rich:panelMenuGroup label="#{mensagens.richfacesGrupo} 2.4">
<rich:panelMenuItem label="Item 2.4.1" name="Item_2_4_1"/>
<rich:panelMenuItem label="Item 2.4.2" name="Item_2_4_2"/>
<rich:panelMenuItem label="Item 2.4.3" name="Item_2_4_3"/>
</rich:panelMenuGroup>
<rich:panelMenuItem label="Item 2.5" name="Item_2_5"/>
</rich:panelMenuGroup>
<rich:panelMenuGroup label="#{mensagens.richfacesGrupo} 3">
<rich:panelMenuItem label="Item 3.1" name="Item_3_1"/>
<rich:panelMenuItem label="Item 3.2" name="Item_3_2"/>
<rich:panelMenuItem label="Item 3.3" name="Item_3_3"/>
</rich:panelMenuGroup>
</rich:panelMenu>
OsatributositemMode="ajax"e groupMode="ajax"sãoconfiguraçõesre-
lacionadasao Ajax. itemChangeListener="#{richfacesMB.atualizarGrupoSelecionado}”
indicaqualmétodoseráchamadovia Ajaxacadamudançadeitem.
127

## Página 142

24.5.Repeat CasadoCódigo
24.5 Repeat
U m afunçãointeressantedoRichfaceséocomponentequepoderepetiroutroscom-
ponentes.Decertomodofuncionacomoumloop,mascomvaloresdiferentes.
<a4j:repeat value="#{richfacesMB.cidadesParaRepeat}"
var="cidade"
rows="20">
<rich:panel>
<f:facet name="header">
<h:panelGroup>
<h:outputText value="#{cidade.nome}" />
</h:panelGroup>
</f:facet>
<h:panelGrid columns="2">
<h:outputText value="#{mensagens.cidadeEstado}" />
<h:outputText value="#{cidade.estado}" />
<h:outputText value="#{mensagens.cidadeTotalHabitantes}" />
<h:outputText value="#{cidade.totalDeHabitacoes}" />
</h:panelGrid>
</rich:panel>
</a4j:repeat>
Ocomponente a4j:repeatreceberáumalistadeobjetosdaclasse Cidade
eoatributo rows="20"definequeserãorepetidos20objetosporpágina.V e j aa
imagem24.11comoessecomponenteévisualmente.
128

## Página 143

CasadoCódigo Capítulo24. Richfaces
Figura24.11:Repeat
24.6 Considerações Finais
Existemdiversoscomponenteshojequeajudamodesenvolvedorcomfuncionalida-
desefacilidades.
OutravantagemdoRichfaceséqueseucódigodoladodoservidoréconsiderado
omaisrobusto.Eletemumexcelenteenfileiramentodechamadas Ajax,utilizaJMS
paraocomponente a4j:pushejáimplementaavalidaçãoatravésda JSR-303(Bean
Validation).
InfelizmenteoRichfacestemumpequenonúmerodecomponentes,suadiversi-
dadeébaixa.OutramelhoriaquepoderiaserfeitanoRichfacesseriasuadocumen-
taçãoquecontivessemaisdetalhes.
129

## Página 145

Capítulo25
Icefaces
Dasbibliotecascitadasaqui,oIcefaceséomaisvelhodetodos,eumdosmenos
utilizados.
Ele tem uma biblioteca com diversos componentes para ajudar tanto na
partevisualcomono server-side. Seushowcasepodeseracessadoaqui: http://
icefaces-showcase.icesoft.org/showcase.jsf.
25.1 Menu
OIcefacesforneceumcomponentede Menuquepermitechamadas Ajax,alémde
colocarimagensdemodoatrativoaousuário.

## Página 146

25.1.Menu CasadoCódigo
Figura25.1:Menu
Aimagem25.1mostraummenuquepoderiaficaracessívelatodaaplicação.Ele
nãotemapenasumtipodeações, masindicaquepodehavertantoações específicas
(salvar,incluiretc)comonavegações.
<ace:menu type="plain" id="exampleMenu" >
<ace:submenu label="File" id="file">
<ace:menuItem id="new"
value="New"
actionListener="#{icefacesMB.fireAction}"
icon="ui-icon">
<ace:ajax event="activate"
execute="@this"
render="message" />
</ace:menuItem>
<ace:menuItem id="open"
value="Open"
actionListener="#{icefacesMB.fireAction}"
icon="ui-icon">
132

## Página 147

CasadoCódigo Capítulo25.Icefaces
<ace:ajax event="activate"
execute="@this"
render="message" />
</ace:menuItem>
<ace:menuItem id="save"
value="Save"
actionListener="#{icefacesMB.fireAction}"
icon="ui-icon ui-icon-disk">
<ace:ajax event="activate"
execute="@this"
render="message" />
</ace:menuItem>
<ace:menuItem id="delete"
value="Delete"
actionListener="#{icefacesMB.fireAction}"
icon="ui-icon ui-icon-close">
<ace:ajax event="activate"
execute="@this"
render="message" />
</ace:menuItem>
</ace:submenu>
<ace:submenu id="view" label="View">
<ace:menuItem id="horizontal"
value="Horizontal"
actionListener="#{icefacesMB.fireAction}"
icon="ui-icon">
<ace:ajax event="activate"
execute="@this"
render="message" />
</ace:menuItem>
<ace:menuItem id="vertical"
value="Vertical"
actionListener="#{icefacesMB.fireAction}"
icon="ui-icon">
<ace:ajax event="activate"
execute="@this"
render="message" />
</ace:menuItem>
<ace:menuItem id="fill"
value="Fill"
133

## Página 148

25.2.Dialog CasadoCódigo
actionListener="#{icefacesMB.fireAction}"
icon="ui-icon">
<ace:ajax event="activate"
execute="@this"
render="message" />
</ace:menuItem>
</ace:submenu>
<ace:submenu label="Links">
<ace:menuItem value="uaiHebert"
url="http://uaihebert.com"
target="_blank"
icon="ui-icon ui-icon-home"/>
<ace:menuItem value="GUJ"
url="http://www.guj.com.br"
target="_blank"
icon="ui-icon ui-icon-home"/>
<ace:menuItem value="Casa do Código"
url="http://www.casadocodigo.com.br"
target="_blank"
icon="ui-icon ui-icon-home"/>
</ace:submenu>
</ace:menu>
Omenuécompostodedoiscomponentes ace:menue ace:submenu.Am-
bosestãoenvolvendoumatagchamada ace:ajaxqueexecutaráumaação Ajax
quandocadaitemforselecionado.
25.2 Di a l o g
OIcefacestemumDialogqueésimplesdemontaresuasações sãofáceisdedefinir.
Figura25.2:Dialog
134

## Página 149

CasadoCódigo Capítulo25.Icefaces
Figura25.3:Dialog
Aimagem25.2e25.3mostraesseútilcomponenteque,emgeral,éutilizadopara
confirmarações emmuitaspartesdosistema.
<h:panelGrid styleClass="centeredPanelGrid" id="panelGridDialog">
<h:commandButton id="save"
value="Save"
onclick="confirmation.show()"
type="button"/>
<h:outputText id="outcome"
value="#{icefacesMB.resultadoDialog}"
rendered="#{icefacesMB.resultadoDialog != null}"/>
</h:panelGrid>
<h:form id="formConfirmDialog">
<ace:confirmationDialog id="confirmDialog"
widgetVar="confirmation"
message="Are you sure about this?"
header="Confirmation"
width="250"
height="100"
closable="true"
position="center">
<h:panelGrid columns="2" styleClass="centeredPanelGrid">
<h:commandButton id="yes" value="Yes"
onclick="confirmation.hide()"
actionListener="#{icefacesMB.dialogSim}"/>
<h:commandButton id="no" value="No"
onclick="confirmation.hide()"
actionListener="#{icefacesMB.dialogNao}"/>
135

## Página 150

25.3.RichText CasadoCódigo
</h:panelGrid>
</ace:confirmationDialog>
</h:form>
Ocomponente ace:confirmationDialogéutilizadoparaexibiraconfir-
mação.
25.3 RichText
Senecessáriosimularumeditordetexto,oIcefacestemumaboaopçãoparaagradar
ousuário.
Figura25.4:RichText
Eparausaressecomponentebastaumcódigobastantesimples.
<ace:richTextEntry value="#{icefacesMB.richText}"
skin="kama"
toolbar="Default"/>
136

## Página 151

CasadoCódigo Capítulo25. Icefaces
25.4 Data
Pordiversasvezescriarumcomponentededataquesejaagradávelaousuárioécom-
plicado.Diversoscódigosde JavaScriptecssexistemnomercadoparatentarfazer
umainterfacebonita.OIcefacesjátemumcomponentebastantesimplesdeutilizar.
Figura25.5:ComponentedeData
<ace:dateTimeEntry value="#{icefacesMB.data}"
pattern="dd/MM/yyyy"
renderAsPopup="true"/>
richTextEntryéocomponenteutilizadoparacriarumeditordetextocom
diversasopçõesdeformata ção.Aop ção skinhabilitaescolheralgumtemadispo-
níveldoIcefaces,eaop ção toolbarpermiteescolherquaiscomponentesestarão
disponíveisparaousuário.
[Resize]O ResizeéumcomponentedoIcefacesquepermiteaousuárioalteraro
tamanhodocomponentenatela.
137
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 152

25.4. Data CasadoCódigo
Figura25.6:Resize
Naimagem25.6épossívelverqueexisteumaop çãode Resizecommuitasopções
eumaop çãodeum Resizemaissimples.
<h:inputTextarea value="#{mensagens.icefacesResizeEfeito}">
<ace:resizable animate="true"
ghost="true"
effectDuration="slow"
minHeight="50"
minWidth="200"
maxHeight="250"
maxWidth="650"/>
</h:inputTextarea>
<ace:panel header="#{mensagens.icefacesResizePanel}">
<h:outputText value="#{mensagens.icefacesResizeGradual}" />
<ace:resizable handles="all"
grid="20"
138
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 153

CasadoCódigo Capítulo25. Icefaces
minHeight="160"
minWidth="300"
maxHeight="300"
maxWidth="700"/>
</ace:panel>
Parautilizaro ace:resizablebastacolocá-lodentrodeoutrocomponente.
Asconfigurações minHeight, minWidth, maxHeighte maxWidthdefinecon-
figuraçõesrelacionadasaotamanhomínimoemáximodelarguras( width)ealturas
(height).Aconfigura ção animateindicaparaoIcefacesqueumaanima çãodeve
serutilizada; ghost="true"iráexibirum“helper”semitransparenteduranteo
resize; effectDurationdefineavelocidadedoefeitoaserexecutado.
25.5 Considerações Finais
OIcefacestemavantagemdeusarumaabordagemchamadaDirect-2-Dom. Ele
mantémumacópiadoDOMexibidonapáginadousuário,quandoesteenviauma
solicitação:aoinvésderespondercomumapáginainteira,oIcefacesenviaráapenas
oquefoialteradocomoresposta.Eleverificaráadiferen çaentreoDOMnoservidor
eoDOMdousuárioparaenviarapenasonecessário.Comessatecnologiaotráfego
dedadosémenor.
OIcefacestemumagrandequantidadededocumenta çãoeexemplospelainter-
net.
SeumaiordefeitoéaquantidadedeproblemasabertosemseuJirasemcorre ção.
CópiaDesonesta?Ou se é código livre posso copiar?
UmoutrofatointeressantefoiqueoIcefacesfoiacusadodeumacópia
docódigofontedoPrimefacesdemododesleal.http://blog.primefaces.
org/?p=1692NoblogdoPrimefacesfoiexibidoumcódigoquefoitotal-
mentecopiado,masnãofoidadoodevidocréditoaquemrealmenteo
criou.Muitacoisaaconteceudepoisdessedia,ehojeoIcefacesreconhe-
ceuquemuitodosseuscomponentesforambaseadose“powered”pelo
Primefaces. IssosóaconteceudepoisqueocriadordoPrimefacesfez
umareclamação.
139
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 154

E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 155

Capítulo26
Evitemisturaras
Implementações/Bibliotecasde
Componentes
ÉmuitofácilencontraremumaImplementa çãoouBibliotecadeComponenteal-
gumcomponentequenosagrade,masessecomponentepodenãoexistirnaImple-
mentação/Bibliotecaqueéutilizadanaaplica çãoemquetrabalhamos.Imagineuma
aplicaçãoqueutilizeMojarracomIcefaces,mas,paraumnovorequisitodaaplica-
ção,umcomponenteexistentenoRichfacesseriaperfeito.
OproblemaéquecadaImplementa ção/Bibliotecatemsuaspeculiaridadesesuas
própriasrotinasparafuncionar.Porexemplo,oPrimefacescriouseuprocessadorde
Ajaxatravésdatag p:ajax.
Épossívelencontrarnainternetdiversosrelatosdeproblemasrelacionadosao
misturarocomponente rich:calendarcom p:toolTip.ORichfacestemseu
modoprópriodetrabalhar,assimcomoopróprioPrimefaces.Énecessárioentender
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 156

CasadoCódigo
quecadaImplementa ção/Biblioteca,apesardetersuabasenoJSF,nãotemcompa-
tibilidadegarantidacomasoutras.
Aviso doJBoss
Aoexecutarumaaplica çãonoJBosscomoMyFacesaseguintemen-
sageméexibida: "W ARN [JBossJSFConfigureListener] MyFaces JSF im-
plementation found!This version of JBoss AS ships with the java.net imple-
mentation of JSF .There are known issues when mixing JSF implementati-
ons. This warning does not apply to MyFaces component libraries such as
T omahawk. However, myfaces-impl.jar and myfaces-api.jar should not be
used without disabling the built-in JSF implementation.See the JBoss wiki
for more details “NotequeopróprioJBossavisaqueoidealseriaapenas
utilizarumaimplementa ção,aqueelefornece.
142
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 157

Capítulo27
Nãofa çapaginaçãonoladodo
servidor
UmadasgrandesdificuldadesdoJSFésobrecomofazerpagina çãopordemanda.
Quandoutilizamoso h:datatableépossívelverquenãoexisteop çãonativade
paginação,vejaaimagem27.1.
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 158

CasadoCódigo
Figura27.1:DatatabledoJSF
Essatabelaconseguimoscomoseguintecódigo:
<!-- dataTable nativo do JSF -->
<h:dataTable value="#{cidadesPaginadas.cidades}"
var="cidade">
<h:column>
<f:facet name="header">
#{mensagens.cidadeId}
</f:facet>
<h:outputText value="#{cidade.id}" />
</h:column>
<h:column>
<f:facet name="header">
#{mensagens.cidadeNome}
</f:facet>
<h:outputText value="#{cidade.nome}" />
</h:column>
<h:column>
<f:facet name="header">
#{mensagens.cidadeEstado}
</f:facet>
<h:outputText value="#{cidade.estado}" />
</h:column>
</h:dataTable>
144
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 159

CasadoCódigo Capítulo27. Nãofaçapaginaçãonoladodoservidor
Infelizmenteo dataTabledoJSFnãoédosmaisbonitosenempráticos. Se
vocêcolocarumacoleçãode100000itensparao dataTable,todosositensserão
exibidos.Dessaforma,alémdevocêmanternomínimo100000objetosnamemória,
arenderizaçãodatelademorarámuito,poisaquantidadedeinforma çãoquedeverá
sermostradaémuitogrande.Indomaisalém,éruimtambémparaousuário,jáque
ausabilidadeficaráprejudicada.Comoencontrarumainforma çãonumalistacom
outras100000?Écomoencontrarumaagulhanopalheiro.
Existemdiversasformasdefazerumapagina çãodosdadosemum dataTable,
porém,vamosprecisardaajudadoPrimefaces,quejápossuitodaainfra-estrutura
necessáriaparafacilitarnossatarefa.
Vejanaimagem27.2comoficaum DataTablepaginadopeloPrimefaces.
Figura27.2:DatatabledoPrimefaces
<!-- paginação nativa do primefaces -->
<p:dataTable value="#{cidadesPaginadas.cidades}"
var="cidade"
paginator="true"
rows="10"
paginatorTemplate="{CurrentPageReport} {FirstPageLink}
{PreviousPageLink} {PageLinks}
{NextPageLink} {LastPageLink}
{RowsPerPageDropdown}"
145
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 160

CasadoCódigo
rowsPerPageTemplate="5,10,15"
style="width: 40%">
<p:column>
<f:facet name="header">
#{mensagens.cidadeId}
</f:facet>
<h:outputText value="#{cidade.id}" />
</p:column>
<p:column>
<f:facet name="header">
#{mensagens.cidadeNome}
</f:facet>
<h:outputText value="#{cidade.nome}" />
</p:column>
<p:column>
<f:facet name="header">
#{mensagens.cidadeEstado}
</f:facet>
<h:outputText value="#{cidade.estado}" />
</p:column>
</p:dataTable>
OpróprioPrimefacescuidadenosoferecerdeantemãoumlayoutagradávelpara
o dataTable.Notequeocódigoébemparecidocomum dataTablenativodo
JSF,eadicionamospoucasconfigura çõesdoPrimefacesrelacionadasàpagina ção.
AoutilizaraPagina çãonativadoPrimefaces,todaalistaéalocadanasessãodo
usuário.Casoumaconsultaretornassemuitosobjetos,facilmentepoderiaestourar
amemóriadoservidor.Temosnessemomentoumapagina çãoqueaconteceapenas
noladodocliente.Elamelhoraausabilidadedaaplica ção,masaindaoneraousodo
servidor,mantendoobjetosdemaisepossivelmentedesnecessáriosnamemória.
Paraevitarisso,pode-seusaratécnicachamada“paginaçãopordemanda”(Lazy
Pagination).Éumatécnicabemsimplesquetrabalhaemcimadaseguintefilosofia:
“qualarazãodecarregarobjetosqueousuáriopodenemchegaraver?”.
Oprincípiodapagina çãopordemandaésimples:acadacliqueparairàpró-
ximapáginado dataTable,umanovaconsultaseráfeitanobancodedadosbus-
candonovosvaloresparaexibir.Avantagemdessatécnicaéqueaoinvésdetrazer
os100000registrosdeumasóvez,virádobancodedadosapenasoqueseráexibido
aousuário.
Vejanaimagem27.3e27.4comoficaráo DataTablecomPaginaçãoporDe-
146
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 161

CasadoCódigo Capítulo27. Nãofaçapaginaçãonoladodoservidor
manda.
Figura27.3:DatatabledoPrimefacescomLazyLoad
Figura27.4:DatatabledoPrimefacescomLazyLoad
<!-- paginação por demanda -->
<h:form>
<p:dataTable value="#{cidadesPaginadasMB.cidadesLazy}"
var="cidade" paginator="true" rows="10"
paginatorTemplate="{CurrentPageReport} {FirstPageLink}
{PreviousPageLink} {PageLinks}
{NextPageLink} {LastPageLink}
147
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 162

CasadoCódigo
{RowsPerPageDropdown}"
rowsPerPageTemplate="5,10,15"
style="width: 40%"
lazy="true">
<p:column sortBy="#{cidade.id}">
<f:facet name="header">
#{mensagens.cidadeId}
</f:facet>
<h:outputText value="#{cidade.id}"/>
</p:column>
<p:column sortBy="#{cidade.nome}"
filterBy="#{cidade.nome}">
<f:facet name="header">
#{mensagens.cidadeNome}
</f:facet>
<h:outputText value="#{cidade.nome}"/>
</p:column>
<p:column sortBy="#{cidade.estado}"
filterBy="#{cidade.estado}">
<f:facet name="header">
#{mensagens.cidadeEstado}
</f:facet>
<h:outputText value="#{cidade.estado}"/>
</p:column>
</p:dataTable>
</h:form>
Vejaqueocódigodapáginaéquaseomesmo,comumdetalhemuitoimpor-
tante. Precisamosinformarqueapagina çãoseráfeitadeforma lazy,atravésdo
atributo lazy="true". Foramadicionadasnocomponente p:columnosatri-
butos sortByparahabilitaraordena çãoe filterByparaindicarofiltro.Toda
colunaqueutilizaro sortByenviaráessevalornahoraemqueforalterado.Esse
parâmetrofuncionadomodoLazyedomodonormal. filterByfaráofiltrodo
campoassimqueseuvalorforalterado. Essaop çãotambémfuncionatantocom
FiltroLazycomodomodonormal.
Uma outra diferença está no atributovalue. Agora indicamos o valor
#{cidadesPaginadas.cidadesLazy}. Precisamosdealgumasmudan çasno
nossoManagedBean.Queméesse cidadesLazy?
@ManagedBean
@ViewScoped
148
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 163

CasadoCódigo Capítulo27. Nãofaçapaginaçãonoladodoservidor
public class CidadesPaginadasMB implements Serializable {
private List<Cidade> cidades;
private LazyDataModel<Cidade> cidadesLazy;
public List<Cidade> getCidades() {
if(cidades == null){
CidadeDAO cidadeDAO = AbstractManagedBean.getCidadeDAO();
cidades = cidadeDAO.listAll();
}
return cidades;
}
public void setCidades(List<Cidade> cidades) {
this.cidades = cidades;
}
public LazyDataModel<Cidade> getCidadesLazy() {
if(cidadesLazy == null){
cidadesLazy = new CidadeLazyList();
}
return cidadesLazy;
}
public void setCidadesLazy(LazyDataModel<Cidade> cidadesLazy) {
this.cidadesLazy = cidadesLazy;
}
}
Vejaqueocódigodaclasse CidadesPaginadasMBsofreualgumasaltera-
ções.Agora cidadesLazyéapenasumatributodeumaclasseabstratachamada
LazyDataModel. cidadesLazytemapenasum newemseu get,oqueindica
quetodoofuncionamentodapagina çãopordemandafoidelegadoparaaclasse
CidadesLazyList.
public class CidadeLazyList extends LazyDataModel<Cidade> {
private List<Cidade> cidades;
149
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 164

CasadoCódigo
@Override
public List<Cidade> load(int posicaoPrimeiraLinha,
int maximoPorPagina,
String ordernarPeloCampo,
SortOrder ordernarAscOuDesc,
Map<String, String> filtros) {
String ordenacao = ordernarAscOuDesc.toString();
if(SortOrder.UNSORTED.equals(ordernarAscOuDesc)){
ordenacao = SortOrder.ASCENDING.toString();
}
cidades = getDAO().buscaPorPaginacao(posicaoPrimeiraLinha,
maximoPorPagina,
ordernarPeloCampo,
ordenacao, filtros);
// total encontrado no banco de dados,
// caso o filtro esteja preenchido dispara a consulta novamente
if (getRowCount() <= 0 ||
(filtros != null && !filtros.isEmpty())) {
setRowCount(getDAO().countAll(filtros));
}
// quantidade a ser exibida em cada página
setPageSize(maximoPorPagina);
return cidades;
}
private CidadeDAO getDAO() {
return AbstractManagedBean.getCidadeDAO();
}
@Override
public Cidade getRowData(String rowKey) {
for (Cidade cidade : cidades) {
if (rowKey.equals(String.valueOf(cidade.getId())))
return cidade;
150
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 165

CasadoCódigo Capítulo27. Nãofaçapaginaçãonoladodoservidor
}
return null;
}
@Override
public Object getRowKey(Cidade cidade) {
return cidade.getId();
}
@Override
public void setRowIndex(int rowIndex) {
// solução para evitar ArithmeticException
if (rowIndex == -1 || getPageSize() == 0) {
super.setRowIndex(-1);
}
else
super.setRowIndex(rowIndex % getPageSize());
}
}
Aclasse CidadeLazyListapresentadiversosmétodoseconfigura ções,que
veremosumaauma.Ométodo public List<Cidade> loadrecebecomoatri-
butotodososparâmetrosnecessáriosparasefazerumaconsulta.
int posicaoPrimeiraLinhaindicadequallinhadobancodedadosapes-
quisadeveráiniciar.Dessaforma,casoseuvalorseja10,apesquisainiciaráapartir
dodécimoregistroqueaconsultadevolverdobancodedados.
int maximoPorPaginaindicaaquantidadeaserexibidaemcadapágina.
Casoessevalorestejadefinidocomo20,acadaquerydisparadanobancodeda-
dosapenas20resultadosdeverãoserutilizados.
String ordernarPeloCampoindicaemqualcamposeráordenadaapes-
quisa.
SortOrder ordernarAscOuDescéumEnumdopróprioPrimefacesquede-
monstraseéparaordenarASCENDING(crescente),DESCENDING(decrescente)
ouseéUNSORTED(semordena ção).
String ordenacao = ordernarAscOuDesc.toString();
if(SortOrder.UNSORTED.equals(ordernarAscOuDesc)) {
151
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 166

CasadoCódigo
ordenacao = SortOrder.ASCENDING.toString();
}
cidades = getDAO().buscaPorPaginacao(posicaoPrimeiraLinha,
maximoPorPagina,
ordernarPeloCampo,
ordenacao, filtros);
ODAOrealizaráapesquisanobancodedadosetrarátodaainforma çãoneces-
sária.MaisadianteveremosoDAO.
// total encontrado no banco de dados,
// caso o filtro esteja preenchido dispara a consulta novamente
if (getRowCount() <= 0 ||
(filtros != null && !filtros.isEmpty())) {
setRowCount(getDAO().countAll(filtros));
}
Informaao DataTableaquantidadederegistrosnobancodedadosnototal.
Casoofiltrosejaalterado,aconsultadeveserrefeita.Casoofiltronãosejaalterado,
aconsultaserádisparadaapenasumavez.
// quantidade a ser exibida em cada página
setPageSize(maximoPorPagina);
Informaao DataTableaquantidadederegistrosaserexibidoporpágina.
@Override
public Cidade getRowData(String rowKey) {
for (Cidade cidade : cidades) {
if (rowKey.equals(String.valueOf(cidade.getId())))
return cidade;
}
return null;
}
@Override
public Object getRowKey(Cidade cidade) {
return cidade.getId();
}
152
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 167

CasadoCódigo Capítulo27. Nãofaçapaginaçãonoladodoservidor
@Override
public void setRowIndex(int rowIndex) {
// solução para evitar ArithmeticException
if (rowIndex == -1 || getPageSize() == 0) {
super.setRowIndex(-1);
}
else
super.setRowIndex(rowIndex % getPageSize());
}
Os métodossetRowIndex, getRowKey e getRowData são utilizados
quandoalgumalinhado DataTableéselecionada. Casoum DataTableseja
utilizadosempagina çãopordemanda,essesmétodosnãosãonecessários.Elesape-
nasindicamqualalinhaselecionada,oobjetoqueseencontranalinhaequaloID
doobjetodalinhadeterminada.
É interessante notar que a classeCidadeLazyList estende da classe
org.primefaces.model.LazyDataModel, e por consequência, acaba her-
dandodiversosmétodosquejáestãoimplementados. Éumapráticacomum:um
dosseusmaisfamososexemploséquandosecriaumServleteaclasseestendidaéa
HttpServlet.
NosmétodosdoDAO,ésempreimportanteusarosrecursosdoseubancode
dadosparabuscarapenasasinforma çõesquedeverãoserexibidas.NoMySQL,por
exemplo,épossívelusarainstru ção limit,quedevolveráapenasumadeterminada
faixaderesultados.
153
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 168

E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 169

ParteV
FuncionalidadesricascomJSF,
segurançaeotimiza çãodoJSF
OJSFporsisónostrazalgunsrecursosquepermitemenriquecerasaplica ções
quedesenvolvemos.Vimosqueasbibliotecasdecomponentespotencializamainda
maisacria çãodefuncionalidadesavan çadas.Masseráquesempreprecisamosdelas?
Equandoprecisarmos,comopodemosimplementá-las?
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 170

E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 171

Capítulo28
FacilitandoousodoAjax
O Ajaxéumatécnicaque,entreoutrascoisas,permiteatualizarpartedeumatela
semprecisarrecarregartodaatelaparaousuário. Apesardepoderserconside-
radorelativamentesimplesdeseimplementar,éimportantemanteralgunscuidados
paraquenãosecaiaemalgumasarmadilhas,tantodopontodevistadausabilidade,
quantododesenvolvimento.
NadamelhordoqueumexemploclássicodeAjax,quepodeservistonasima-
gens28.1,28.8e28.3:
Figura28.1:UtilizandoAjaxparaselectOne
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 172

CasadoCódigo
Figura28.2:UtilizandoAjaxparaselectOne
Figura28.3:UtilizandoAjaxparaselectOne
NotequeénecessárioselecionarumEstado,paradepoisselecionarumacidade
efinalmenteumbairro.Mascarregartodosessesobjetosemmemóriapodeserum
problemadependendodaquantidadedeobjetosretornados. Salvartodasop ções
escondidasnatelaeutilizarJavaScriptéoutraop ção,mascasoaquantidadedere-
gistrossejamuitogrande,ousuáriolevarámaistempoparacarregarosvalores.
Asoluçãomaispráticaéutilizar Ajax,quefelizmentejávemnativonoJSF2.0.
NoJSF1.xeranecessáriorecorreraalgumabibliotecadecomponentesparaconse-
guirusarrequisi çõesassíncronas,enquantoqueapartirdoJSF2,bastautilizaratag
f:ajax.
<h:form>
<h:panelGrid columns="3">
<h:outputText value="#{mensagens.ajaxSelecioneEstado}: "/>
<h:outputText value="#{mensagens.ajaxSelecioneCidade}: "/>
<h:outputText value="#{mensagens.ajaxBairro}: " />
<h:selectOneMenu value="#{ajaxMB.estadoSelecionado}">
<f:selectItem itemLabel="#{mensagens.ajaxSelecione}"
itemValue=""/>
<f:selectItems value="#{ajaxMB.estados}"/>
<f:ajax execute="@this"
158
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 173

CasadoCódigo Capítulo28. FacilitandoousodoAjax
render="selectCidade selectBairro"
listener="#{ajaxMB.alterarEstado}" />
</h:selectOneMenu>
<h:selectOneMenu id="selectCidade"
value="#{ajaxMB.cidadeSelecionada}">
<f:selectItem itemLabel="#{mensagens.ajaxSelecione}"
itemValue=""/>
<f:selectItems value="#{ajaxMB.cidades}"/>
<f:ajax execute="@this"
render="selectBairro"
listener="#{ajaxMB.alterarCidade}" />
</h:selectOneMenu>
<h:selectOneMenu id="selectBairro"
value="#{ajaxMB.bairroSelecionado}">
<f:selectItem itemLabel="#{mensagens.ajaxSelecione}"
itemValue=""/>
<f:selectItems value="#{ajaxMB.bairros}"/>
</h:selectOneMenu>
</h:panelGrid>
</h:form>
O componente f:ajaxé responsável por executar a chamada assíncrona.
Toda vez que oselectOne for alterado, ele irá enviar o valor definido em
execute="@this",nessecasoo @thissignificaocomponenteatualequenesse
casoéo selectOnequeestáenvolvendoo f:ajax.
Oatributo renderindicaquaiscomponentesserãoatualizadosquandoares-
postadarequisi çãoassíncronafordevolvida. No selectOnedoEstado,indica-
mos selectCidade selectBairrocomotendoquesofreratualiza ção.Ouseja,
quandooEstadoforselecionado,oscamposdecidadeedebairroserãorecarrega-
dos,paramostrarasinforma çõescondizentescomaescolhadousuário.Aimagem
28.4mostracomofuncionaumarequisi ção Ajax.
159
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 174

28.1. Sempreindiquequearequisiçãoestáacontecendo CasadoCódigo
Figura28.4:Requisi çãoAjax
OManagedBeanapenasrecebeovalorselecionadoemum selectOnepara
decidirqualovaloraserexibidonopróximo.
28.1 Sempre indique que a requisição está aconte -
cendo
Devidoaofatodearequisi çãoAjaxserfeitadeformaassíncrona,emalgunsmo-
mentospodenãohaveracertezadequealgoestáacontecendoousendoprocessado
160
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 175

CasadoCódigo Capítulo28. FacilitandoousodoAjax
ecomisso,ousuáriodaaplica çãopodeterumarea çãoquenãosejaaadequada,
eporexemplo,realizarrepetidasvezesaa ção,atéquealgoaconte ça,dessaforma,
enfileirandováriasrequisições.
Umaboapráticaésempreindicarqueumaa çãoestásendoexecutada,sejaatra-
vésdeumaimagemouumaanima ção.
UmasoluçãointeressanteéapresentadapeloPrimefaces(tambémpresenteem
outrasbibliotecas):ocomponentechamado p:ajaxStatus.
<p:ajaxStatus onstart="statusDialog.show();"
onsuccess="statusDialog.hide();"/>
<p:dialog modal="true" widgetVar="statusDialog" header="Status"
draggable="false" closable="false">
<p:graphicImage library="gifs" name="ajaxloadingbar.gif" />
</p:dialog>
Ocomponente p:ajaxStatusautomaticamentedetectaráqueumachamada
Ajaxfoiiniciadaeexibiráumdialogparaousuário.Aofinaldoprocessamento Ajax
ocomponentefecharáodialogautomaticamente,comodemonstradonaimagema
seguir.
Figura28.5:Feedbackdea çãoiniciada
28.2 Dê mensagens de feedback para o usuário
Sempredêofeedbackdoqueestáacontecendoparaousuário.Umaformaalterna-
tivaàimageméusarsimplesmensagensqueindiquemaousuáriooqueestáacon-
tecendo. Todavezqueumaa çãoéexecutada,ousuárionaturalmenteesperapor
umresultado,mascomoelevaisabersealgoaconteceueoquê,semquenenhuma
mensagemindiqueparaele?OcomponenteGrowlexplicadonocapítulosobrePri-
mefaces(??)mostracomoelefunciona.
161
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 176

28.3. Previna-sedasváriasaçõesdousuárioemrequisi çõesassíncronas CasadoCódigo
28.3 Previna-se das v árias ações do usuário em re -
quisições assíncronas
Casoaa çãodisparadademoremaisdoqueoesperadoparafinalizareousuário
dependadoresultadodessaexecu çãoparacontinuaralgumaa ção,podemosmostrar
paraeleumamensagemindicandoademoradoprocessamento.
Namaioriadasvezes,énecessáriodesabilitarobotão,poisousuárioincansavel-
menteapertaráomesmobotãomilharesdevezes.Parafazerissoteremosqueusar
umpequenocódigojQuery.
<h:form>
<h:commandButton value="#{mensagens.ajaxBotaoTravado}">
<f:ajax execute="@form"
render="@form"
listener="#{ajaxMB.chamadaAjax}"
onevent="desabilitarBotao" />
</h:commandButton>
</h:form>
<script type="text/javascript">
function desabilitarBotao(evento) {
var botao = evento.source;
var statusAjax = evento.status;
switch (statusAjax) {
case "begin":
botao.disabled = true;
break;
case "complete":
break;
case "success":
botao.disabled = false;
break;
}
}
</script>
Atravésdafunção desabilitarBotaoobotãoserádesabilitadoaoiniciara
chamadaajax,eaofinaldachamadaseráhabilitadonovamente.Asimagensaseguir
mostramcomoficaráessebotão.
162
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 177

CasadoCódigo Capítulo28. FacilitandoousodoAjax
Figura28.6:Desabilitandobotão
Figura28.7:Desabilitandobotão
28.4 Cuidado ao usar ManagedBeans RequestSco-
ped comAjax
Quandousamosrequisi ções Ajax,precisamostomaralgunscuidadoscomosMa-
nagedBeans RequestScoped. Vejaoexemplodaimagem28.8,ondetemosum
cenárioclássicodeusoderequisiçõesassíncronas.
Figura28.8:UtilizandoAjaxparaselectOne
Naimagem28.8épossívelverumexemplonoqualquandocada selectOne
foratualizado,umoutro selectOneserápopulado.
163
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 178

28.4. CuidadoaousarManagedBeansRequestScopedcomAjax CasadoCódigo
Notequeumachamada AjaxaumManagedBeandotipoRequestScopedsem-
preprecisaenviarosdadosnecessáriosparaoprocessamento,jáqueoManagedBean
nãoguardaráasinformaçõesentreasdiferentesrequisi ções.Nessecaso,serianeces-
sárioenviaro Estadoselecionadoparahabilitaro selectOnedeCidades. Ao
escolheruma Cidadeserianecessárioenviarnovamente Estadoe Cidadepara
podercalcularosvaloresdo selectOnedeBairros.
Note que, com escopo derequest, poderá funcionar sem problemas, mas a
desvantageméessetrabalhodeenviartodososvaloresnecessáriosacadacha-
mada. Poderíamosevitaressanecessidadeatravésdeumbean ViewScopedou
ConversationScoped.
164
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 179

Capítulo29
InternacionalizaçãoeLocaliza ção
dasuaaplica ção
Muitasvezes,desenvolvemosaplica çõesqueserãoutilizadasporpessoasdevários
lugaresdomundo,comdiversascaracterísticasculturais,sendoumadasmaismar-
cantesoidioma.Dessamaneira,oidealéquenossaaplica çãoseadapteàsdiferentes
necessidadesdelocaisdistintos. Paraisso,precisamosquehajaalgumtipodesu-
portedoframeworkparaadaptarmosaaplica çãoaessasnecessidades.Issoéoque
chamamosdeinternacionalização.
OJSFprovêinternacionalizaçãoparanósatravésdesimplesconfigura çõesear-
quivos .properties,queconterãotodasasmensagensdosistema.Atradu çãodas
diversasmensagensparadiferentesidiomas,adapta çãodesinaismonetários,abre-
viaçõeseváriosoutrosrecursossãoconhecidoscomo localização.
Paracomeçarmosaadaptaraaplica ção,vamoscolocarosarquivoscomasmen-
sagens.Aimagem29.1mostracomoficariaoarquivoutilizandoa IDE Eclipse.
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 180

CasadoCódigo
Figura29.1:ArquivoscommensagensdosistemanoEclipse
Dentrodessesarquivospodemosterasmensagens,juntodesuasrespectivascha-
vesidentificadoras:
# arquivo bundle_pt.properties
bemVindo=Seja Bem Vindo
index=Pagina Principal
# arquivo bundle_en.properties
bemVindo=You are welcome
index=Welcome Page
Opróximopassoéconfiguraraexistênciadosarquivosdainternacionaliza ção
paraoJSF.Podemosfazerissoatravésdo faces-config.xml,noqualadiciona-
mosatag locale-configparaindicarqualseráoidiomapadrão,queemnosso
casoserápt,indicandooportuguês.Definimostambémonomearquivocomosidi-
omas,quechamamosde bundle.Comisso,teremosparacadaidiomaumarquivo
bundle_xx.properties,ondepodemossubstituir xxpelocódigodoidioma.
Vamosdefinirtambémumavariávelchamada mensagens,queéconfigurada
tambémnoarquivo faces-config.xml.
<application>
<locale-config>
<default-locale>pt</default-locale>
</locale-config>
<resource-bundle>
<base-name>bundle</base-name>
<var>mensagens</var>
</resource-bundle>
</application>
Épossívelespecificaraindamelhorqualalinguagemdoarquivoseseunomefor
166
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 181

CasadoCódigo Capítulo29. InternacionalizaçãoeLocaliza çãodasuaaplica ção
bundle_pt_BReomesmopodeseraplicadoparaasoutraslinguagens.Nessecaso,
estamosindicandoavaria çãodoportuguêsaserusado,nocaso,odoBrasil.
Outrocomportamentoimportantedeseprestaraten çãoéque,casoousuário
estejaemumalinguagemquenãodefinidanosistema,oJSFescolheráalinguagem
padrão,definidanatag default-locale.
29.1 Permita que o usuário mude o idioma
Semprequeousuárioacessaraaplica ção,umidiomaseráescolhidoparaqueocon-
teúdosejamostrado. Nãonecessariamentealínguapadrãoseráaqueousuário
gostaria.Porisso,precisamospermitirqueeleescolhaaquepreferir.
Compequenosajustesnaaplica ção,épossívelfazercomquealinguagemseja
escolhidapelousuário.Primeiro,énecessáriocriarumaop çãoparausuárioseleci-
onarqualoidiomadesejado. Podemosfazeratravésdeum selectOneMenuou
então,disponibilizandobandeirinhasdaslínguasdisponíveis,que,quandoclicadas,
mudaparaoidiomaadequado.
<h:outputText value="#{mensagens.internacionalizacaoTexto}:" />
<h:form>
<h:selectOneMenu value="#{usuarioMB.linguaEscolhida}">
<f:selectItem itemValue="pt"
itemLabel="#{mensagens.internacionalizacaoPT}"/>
<f:selectItem itemValue="en"
itemLabel="#{mensagens.internacionalizacaoEN}"/>
</h:selectOneMenu>
<h:commandButton action="#{usuarioMB.alterarIdioma}"
value="#{mensagens.internacionalizacaoTrocar}" />
</h:form>
Épossívelnotarqueo selectOneMenuapontaparaumManagedBeanque
define qual a linguagem a ser selecionada. E existe umaaction, chamada
alterarIdioma,quefarátodootrabalhoparanós.
@ManagedBean
@SessionScoped
public class UsuarioMB implements Serializable {
private String linguaEscolhida = "pt";
private Locale locale;
167
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 182

29.1. Permitaqueousuáriomudeoidioma CasadoCódigo
public String alterarIdioma() {
locale = new Locale(linguaEscolhida);
FacesContext instance = FacesContext.getCurrentInstance();
instance.getViewRoot().setLocale(locale);
return null;
}
public Locale getLocale() {
if(locale == null){
locale = new Locale(linguaEscolhida);
}
return locale;
}
// getters e setters necessários
}
NotequeoManagedBean UsuarioMBtemosatributosparainformarqual
o LocaleatualeumaStringquecontémumalínguapadrãoequeéutilizada
no selectOne.Dentrodométodo alterarIdioma,achamadaparaométodo
setLocaleéfeita,passandocomoparâmetrooidioma Localequeousuárioes-
colheu.
Umaoutraop çãoéenvolverumpeda çodeumtextoporumalinguagemqual-
quer.Casoemumpontoespecíficodapáginasejanecessárioteroutralíngua,basta
utilizaroatributo localedocomponente f:view.
<f:view locale="#{usuarioMB.locale}">
<!-- códigos do sistema aqui-->
</f:view>
168
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 183

CasadoCódigo Capítulo29. InternacionalizaçãoeLocaliza çãodasuaaplica ção
BoaPrática
Tenhaemmentequecolocartodootextodasuaaplica çãoemarqui-
voséumaboapráticamesmoquetenhaapenasumidioma.
Pode-seconsiderarainternacionaliza çãocomoboapráticapelosse-
guintesfatos:
• Facilitaaalteraçãodetextos. Casosejanecessáriotrocarapala-
vradeCarroparaAutomóvel,todosostextosseencontramem
umarquivoapenas.Nãoseránecessárioentraremcadapáginado
sistema.
• Casoapósumdeploysepercebaqueexisteumamensagemerrada,
bastariaalteraroarquivodepropriedades. Nãoserianecessário
editaraspáginasdosistema.
• Sefossenecessáriocriarumanovalinguagemparaosistema,bas-
tariatraduziroarquivo. Nãoserianecessáriaaltera çãoemtodas
aspáginas.
Parafinalizaresseassunto,épossívelsobrescreverasmensagensdefaultdoJSF.
Casoumcampoestejamarcadocomo required=trueumamensagememinglês
aparecerá:ValidationError: Value is required. Paraumsistemaemportuguês,essa
mensagempodeserbastantedesconfortávelparaousuário.
Para alterar as mensagens padrões do JSF, basta adi-
cionar a seguinte configura ção ao faces-config.xml:
<message-bundle>bundle</message-bundle>. Com essa configuração
oJSFprocuraránoarquivodebundlepelaschavesutilizadaspeloJSF.
<application>
<locale-config>
<default-locale>pt</default-locale>
</locale-config>
<resource-bundle>
<base-name>bundle</base-name>
<var>mensagens</var>
169
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 184

29.1. Permitaqueousuáriomudeoidioma CasadoCódigo
</resource-bundle>
<!-- configuração adicionada -->
<message-bundle>bundle</message-bundle>
</application>
# bundle_pt.properties
javax.faces.component.UIInput.REQUIRED=Campo necessário não preenchido
# bundle_en.properties
javax.faces.component.UIInput.REQUIRED=A required field is Empty
Bastaadicionaralinhacomachavedecampoobrigatóriaaoarquivodemen-
sagens,noprojetodolivrochamadodebundle,epronto.OJSFidentificaráquala
línguadousuárioeprocuraránorespectivoarquivodemensagens.
Vejanasimagens29.2e29.3comoficaráessatrocadinâmicadalínguadosis-
tema.
Figura29.2:MensagensemPortuguês
Figura29.3:MensagensemInglês
Noprojetodolivroalgumaschavesforamtraduzidas,porissoque,mesmoalte-
randoparainglês,nemtodasaspalavrasserãotraduzidas.
170
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 185

CasadoCódigo Capítulo29. InternacionalizaçãoeLocaliza çãodasuaaplica ção
Para utilizar os valores descritos no arquivo de propriedades basta utilizar
#{mensagens.bemVindo}. OJSFiráescolherquallínguautilizardeacordocomas
configuraçõeseoidiomadousuário.
171
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 186

E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 187

Capítulo30
Utilizandorecursosdentrodeum
Converter
CriarconversoreséumatarefabastanterecorrenteemprojetosJSF.Noentanto,uma
grandedificuldadeéqueatéaversão2.1doJSFnãoerapossíveltrabalharcominje ção
dedependênciasdentrodessescomponentes.Dessaforma,tendemosatercódigos
complexosededifícilmanuten çãodentrodoBean. Mascomopodemosfazerpra
mantermosnossocódigolimpoeelegantedentrodosconversores?
30.1 Acesse um ManagedBean programaticamente
através deExpressionLanguage
Semprequeprecisamos,naspáginas xhtml,temosacessoadiversosrecursosatra-
vésdas Expression Languages.Seriainteressantesedealgumamaneiratambémti-
véssemoscomoacessá-losdentrodosconversores.Esehouvesseumapossibilidade
deusarmosa Expression Languagededentrodoconversor?
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 188

30.1. AcesseumManagedBeanprogramaticamenteatravésdeExpressionLanguage CasadoCódigo
@FacesConverter(value = "bairroConverter")
public class BairroConverter implements Converter {
@Override
public Object getAsObject(FacesContext fc, UIComponent uic,
String key) {
FacesContext context = FacesContext.getCurrentInstance();
ELContext elContext = context.getELContext();
ELResolver elResolver = elContext.getELResolver();
BairroMB bairroMB = (BairroMB)
elResolver.getValue(elContext, null, "BairroMB");
return bairroMB.find(Integer.valueOf(key));
}
// outros métodos omitidos
}
Ocódigodaclasse BairroConvertermostracomobuscarumManagedBean
eutilizá-lopararealizarasrotinasnecessárias.Notequeométodo finddoMana-
gedBeanteriaacessoàsclassesinjetadas.
Aoutilizaressaabordagem,oidealéterumaclasseparaabstrairtodosospassos
necessáriosparaseacessarumManagedBean.
// imports omitidos
public class ManagedBeanLocator {
public static AbstractMB find(String managedBean) {
FacesContext context = FacesContext.getCurrentInstance();
ELContext elContext = context.getELContext();
ELResolver elResolver = elContext.getELResolver();
return (AbstractMB) elResolver.getValue(elContext, null,
managedBean);
}
}
Eparautilizarométodobastariafazer:
BairroMB bairroCrudMB = (BairroMB) ManagedBeanLocator.find("BairroMB");
174
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 189

Capítulo31
CDIcomJSF
AvantagemdoCDIéinjetarasdependênciaseutilizaraquelerecursosemquea
classetenhaquesepreocupareminstanciá-lo.
UmbomexemploseriautilizaroEntityManagerdoJPAdentrodeumMana-
gedBean.
@ManagedBean(name="usuarioLoginMB")
@SessionScoped
public class UsuarioLoginMB implements Serializable {
private String login;
private String senha;
@PersistenceUnit(unitName="meuPU")
private EntityManagerFactory emFactory;
@Resource
private UserTransaction userTransaction;
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 190

CasadoCódigo
public String login() {
// ...
}
}
NocódigodoManagedBean UsuarioLoginMBépossívelverquetemosinje-
tadoum EntityManagerFactoryeumobjetodotipo UserTransaction.
NotequeoManagedBeannãotemideiadeondevieramessasduasinstâncias,ele
apenasutilizaessesobjetos.AgrandevantagemdoCDIéqueumdesacoplamento
écriadoentreclasses.Notequenãofoinecessáriopassarconfigura çãoalgumarela-
cionadaaoarquivo persistence.xml.Opróprioservidorlocalizouessasinfor-
maçõesecriouumainstanciadoEntityManagerFactory.
ÉpossíveltambéminjetarumEJBeoutrosrecursosdentrodeumManaged-
Bean.
176
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 191

Capítulo32
Eviteo“CrossSiteScripting”emseu
sistema
Emumcampodetextodeumformulárioépossívelqueousuáriodigitequalquer
informação,mesmonãosendoasolicitadapelocampo.Porexemplo,emumcampo
cujadescriçãoé“Nome”,ousuáriopodedigitara“Idade”,oseu“Endereço”ouqual-
queroutrainforma çãoqueelequeira. Sendoassim,jáquenessecampoelepode
digitarqualquerinforma çãoquesejaalfanumérica,oqueoimpededepreencher
essecampocomumpequenocódigoJavaScript?Algocomo:
<script>alert('ola!');</script>
Comessainforma çãodigitadanocampo,elaserácadastradanobancodedados.
Atéaí,tudobem.Oproblemaacontecequandoqueremosmostraronomenatela.
<h:outputText value="#{cliente.nome}" />
Oconteúdodonome,quenocasoéopequenotrechodecódigoJavaScript,será
inseridodentrodoHTML.Issovaifazercomqueduranteaexibi çãodatela,amen-
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 192

CasadoCódigo
sagemdealertaapare ça,ouseja,ocódigoJavaScriptcadastradopelousuárioserá
executadoposteriormente.Quãoperigosoissopodeser?
Muitospodemimaginarqueissoéinofensivo,poisousuárionãovaidigitaralgo
dessanaturezanocampo.Noentanto,essabrechapodeserusadaparaumataque
poderoso,atémesmoparatirarosistemadoar.Porexemplo,jáqueépossívelintro-
duzircódigoJavaScriptqueemalgummomentofuturoseráexecutado,oqueimpede
apessoadecadastrarum loopinginfinitoqueenviarequisi çõesassíncronasparaa
aplicação?Pronto,suaaplica çãosetornoualvodeumataque.
Atacaraplicaçõesatravésdainje çãodecódigoJavaScriptéumatécnicachamada
Cross Site Scripting.
Asoluçãoparaesseproblemaéextremamentesimples.Paraexibirasinforma-
ções,utilizeatag h:outputText. Elajávemcomummecanismodeprote ção,
atravésdoatributo escape. truejáéovalorpadrãoutilizado,eelefarácomque
umcódigoJavascriptsejaapenasimpresso,masnãoexecutado.
Éumasolu çãoextremamentesimplesqueevitadoresdecabe çacomataquesa
quemuitossistemasestãovulneráveis.
178
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 193

Capítulo33
Otimizandoanavega çãoe
performance
O JSF dispara seu ciclo de vida quando uma navegação é disparada utilizando
h:commandLinkeo h:commandButton.Noentanto,quandoapenasqueremos
trocardepágina,semdisparara çãoalguma,nãoprecisamosquetodoocicloseja
executado.Asaídaparaessasitua çãoéutilizarocomponente h:outputLink,que
geraapenasumlinkconvencional.
Seuusoéextremamentesimples,bastandoindicarnoatributo outcomequalé
apáginadedestino:
<h:outputLink outcome="pagina.xhtml" value="Pagina 01"/>
Avantagemdeutilizaro h:outputLinkparanavegaçãoéqueelenãodispara
osciclodevidacompletodoJSF,tornandoanavega çãoumprocessomaisleve.
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 194

E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 195

ParteVI
Debugeinspe çãodeaplica ções
Duranteodesenvolvimentodasaplica ções,écomuminspecionarmosoquees-
tamosfazendoatravésdasmensagensdedebugecomentáriosquedeixamospelo
código.Mascomopodemosfazeressedebugdeumamaneiraquenãopoluanosso
códigoouatrapalheanossaaplica ção?
Nessaparte,vocêaprenderádicasdedesenvolvimentoecomoresolvererrosque
comunsdodiaadiadodesenvolvimentocomJSF.
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 196

E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 197

Capítulo34
Limpezadecomentáriosedebug
34.1 Esconda os comentários da página
Écomumdesenvolvedoresolharemocódigofontedesistemasesitesquenãoforam
feitosporeles. Noentanto,geralmenteaoabrirocódigofontedeumapágina,é
possívelencontrarcomentáriosnoHTMLresultante,quealémdepoluirasaída,
tornamarespostamaispesada.
ComoJSF,existeummodosimplesdeescondertodososcomentáriosquesão
colocadosnosXHTML.Bastaadicionarumaconfigura çãono web.xmleosco-
mentáriosnãoserãomaisexibidos.
<!-- adicionar ao web.xml -->
<context-param>
<param-name>javax.faces.FACELETS_SKIP_COMMENTS</param-name>
<param-value>true</param-value>
</context-param>
ÉconsideradaboapráticaesconderoscomentáriosdocódigoXHTML.Pri-
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 198

34.2. Debugdoscomponentes CasadoCódigo
meiro,pelofatodequecomentáriosemHTMLsãoenviadosparaonavegador,que
oignora,porémaumentaotamanhodoconteúdodarespostaaserdada.Esegundo,
poispessoaspodemburlardealgumamaneiraosistemadesenvolvidocasohajam
comentáriosqueexponhamaexistênciadealgumafalhanaimplementa ção.
Um desenvolvedor poderia escrever<!-- corrigindo falha da data
-->eapartirdessamensagem,elepoderiadescobrirqualfalhaéessa.Issopoderia
acarretaremumamensagemsimplesdeerro,atéfalhasempagamentos,prejuízo
financeiroouquedadoservidoremcasosmaisextremos.
34.2 Debug dos componentes
Muitasvezesfazemosmanipula çõesnatelaeperdemosocontroledoqueestáounão
estánaárvoredecomponentes,porexemplo.Ouentãoqualéoestadodoscompo-
nenteseassimpordiante.Pararesolveressaseoutrasquestõessobreasitua çãodos
componentes,podemosutilizaratag <ui:debug>.
Paraacessarosdadosfornecidospelo <ui:debug />bastautilizaroatalho
ctrl + shift + deumatelacomoamostradanasimagens34.1,34.2e34.3irá
aparecer.
Figura34.1:FunçãoDebugdoJSF
184
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 199

CasadoCódigo Capítulo34. Limpezadecomentáriosedebug
Figura34.2:Fun çãoDebugdoJSF
185
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 200

34.2. Debugdoscomponentes CasadoCódigo
Figura34.3:Fun çãoDebugdoJSF
Entreoutrascoisas,o debugéútilpararesolverproblemasde Ajaxquandoum
updatenãofunciona.Outrasitua çãoondeo debugpodeserutilizadoéparaverse
osvaloresenviadosporumManagedBeanestãochegandoà view.Apenastenhao
cuidadodecolocaro <ui:debug />aofinaldesuapágina,casocontrário,eledis-
pararáosgetterse settersdosManagedBeanmonitoradoseassimpoderáocasionar
comportamentosinesperados.
186
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 201

Capítulo35
Organizefuncionalidadespor
ambientedoprojeto
OJSFentendequecadaprojetopassapor estágiosecadaumpossuicaracterísticas
específicasqueajudamdediferentemodos.
HojenoJSFsãopossíveisencontrarosseguintesestágios: Development,
UnitTest, SystemTest, Productione Extension.
OsestágiosSystemTeste UnitTestpermitemquea çõessejamconfiguradas
paraseremexecutadasemum Listener.Casoalgumdado,objetoouconfigura ção
fossemnecessáriosapenasparateste,bastariaconfigurarno web.xmlqualoestágio
atualdaaplica ção.
Ométodo configurarAmbientemostracomooestágiopoderiaserconfi-
guradoemumManagedBeandotipo@ApplicationScoped. Dessemodo,bastaria
chamarométodoparaqueaaplica çãopossasecomportardependendodaconfigu-
ração.
public void configurarAmbiente() {
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 202

CasadoCódigo
FacesContext facesContext = FacesContext.getCurrentInstance();
Application application = facesContext.getApplication();
ProjectStage projectStage = application.getProjectStage();
if (projectStage.equals(ProjectStage.Development)) {
// realiza ações de desenvolvimento
} else if (projectStage.equals(ProjectStage.Production)) {
// realiza ações de produção
} else if (projectStage.equals(ProjectStage.SystemTest)) {
// realiza ações de testes de sistema
} else if (projectStage.equals(ProjectStage.UnitTest)) {
// realiza ações de testes de units
}
}
OsestágiosDevelopmente Productionsãoosmaisutilizados.
ÉnormalqueaosedesenvolvercomJSFerrosestejamacontecendoenenhuma
mensagemsejaexibida.Asvezessãoerrossimplesquecasoalgumamensagemfosse
exibidarapidamenteesseserrosseriamresolvidos.
Umadasvantagensdoestágio DevelopmentéqueoJSFadicionaautomati-
camente h:messagesnaspáginasparaexibirmensagensdeerro,oqueémuito
prático.
Jáoestágiode Production(queéovalorpadrão)temumacaracterística
opostaao Development,eleescondeerrosquepoderiamserexibidosaousuário
final.
AsimplementaçõesdoJSFpodemrealizara çõesparaotimizarcadaestágioes-
colhidoparaoprojeto. OMyFaces,porexemplo,noestágio Developmentfazo
deploydosarquivosdeJavaScriptseparadamente. Jánoestágio Productionele
iráreduzirminificaroarquivoecompactarosváriosarquivos,afimdeotimizara
performancedaaplica ção.
188
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 203

CasadoCódigo Capítulo35. Organizefuncionalidadesporambientedoprojeto
Para configurar o estágio da aplicação basta adicionar o parâmetro
javax.faces.PROJECT_STAGEno web.xml:
<!-- web.xml -->
<context-param>
<param-name>javax.faces.PROJECT_STAGE</param-name>
<param-value>Development</param-value>
</context-param>
189
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 204

E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 205

Capítulo36
RefreshautomáticodosArquivos
Emalgunsmomentosaltera çõessãorealizadasdiretamentenaspáginasdoprojeto
(arquivoxhtml/jsp),masnãosãorefletidasnocódigo.
ÉpossívelinformaroJSFqueeledeveverificarsealgumarquivodeumprojeto
foialterado.ComissooJSFiráatualizaroarquivoalteradonoprojetoemtempode
execuçãonoservidor.
Para ativar essa funcionalidade, basta adicionar a configura ção
javax.faces.FACELETS_REFRESH_PERIODnoarquivoweb.xml.
<context-param>
<param-name>javax.faces.FACELETS_REFRESH_PERIOD</param-name>
<param-value>2</param-value>
</context-param>
O tempo da configuração javax.faces.FACELETS_REFRESH_PERIODé
tratadaemsegundos.
E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 206

E-book gerado especialmente para Haylson Martins - haylson@gmail.com

## Página 207

Capítulo37
RefreshautomáticodosArquivos
Emalgunsmomentosaltera çõessãorealizadasdiretamentenaspáginasdoprojeto
(arquivoxhtml/jsp),masnãosãorefletidasnocódigo.
ÉpossívelinformaroJSFqueeledeveverificarsealgumarquivodeumprojeto
foialterado.ComissooJSFiráatualizaroarquivoalteradonoprojetoemtempode
execuçãonoservidor.
Para ativar essa funcionalidade, basta adicionar a configura ção
javax.faces.FACELETS_REFRESH_PERIODnoarquivoweb.xml.
<context-param>
<param-name>javax.faces.FACELETS_REFRESH_PERIOD</param-name>
<param-value>2</param-value>
</context-param>
O tempo da configuração javax.faces.FACELETS_REFRESH_PERIODé
tratadaemsegundos.
E-book gerado especialmente para Haylson Martins - haylson@gmail.com