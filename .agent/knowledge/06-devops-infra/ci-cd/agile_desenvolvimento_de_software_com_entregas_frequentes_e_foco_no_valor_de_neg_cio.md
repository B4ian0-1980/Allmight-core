---json
{
  "id": "agile_desenvolvimento_de_software_com_entregas_frequentes_e_foco_no_valor_de_neg_cio",
  "title": "Agile Desenvolvimento de software com entregas frequentes e foco no valor de negócio",
  "categoria": "06-devops-infra",
  "subcategoria": "ci-cd",
  "resumo": "**Arquivo Original:** `Agile Desenvolvimento de software com entregas frequentes e foco no valor de negócio.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "agile",
    "cio",
    "com",
    "desenvolvimento",
    "devops",
    "entregas",
    "foco",
    "frequentes"
  ],
  "perguntas_tipo": [
    "Como utilizar Agile Desenvolvimento de software com entregas frequentes e foco no valor de negócio?",
    "Quais as boas praticas de ci-cd?"
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
  "dono": "stack-ci-cd",
  "prioridade": 2
}
---

# Agile Desenvolvimento de software com entregas frequentes e foco no valor de negócio

> **Arquivo Original:** `Agile Desenvolvimento de software com entregas frequentes e foco no valor de negócio.pdf`
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
Agradecimentos
Escreverestelivrofoiumgrandedesafioparamim,epassarporessedesafiofoium
grandelembretedoquãovaliosossãomeusfamiliares,amigos,colegasdetrabalho
edecomunidade.Semelesesselivronãoteriasetornadorealidade.
AgradeçoàEditoraCasadoCódigonaspessoasdePauloSilveiraeAdrianoAl-
meidapelaoportunidadequemefoiconcedidaepelaconfian çaparaescreversobre
umassuntotãoimportantenosdiasdehojecomoodesenvolvimentoágildesofware.
AgradeçoàBluesofteatodososseuscolaboradoresquesempremeapoiameins-
piramparabuscarmelhorespráticaseabordagensnodesenvolviementodesoftware
enagestão.
Emumadasvezesquefoientrevistado,SteveJobssugeriuquedevemosnosex-
poràsmelhorescoisasquesereshumanosjáfizeram(suasobras,seustrabalhos)
eentãotentartrazeressascoisasparaoquevocêestáfazendo. Bem,jáfazalgum
tempoqueeuvenhotentandoseguiresseconselho.
Éporissoqueeuagrade çotambémaquiatodosaquelesquedesdeoManifesto
Ágilvêmsededicandoparaquepossamosencontrarmelhoresmaneirasdesede-
senvolversoftware.
AgradeçotambémàminhanoivaFernanda,queéminhamaiorfontedeinspi-
raçãoesempremeapoiaemtodososmeusdesafios.
Finalmente,agradeçoavocêleitor,vocêérazãopelaqualesselivroexiste,sem
você,essetrabalhonãoseriasequernecessário.Aproveitealeitura!
i

## Página 7

CasadoCódigo
Quemsoueu?
MeunomeAndréFariaGomes.Atualmente,sousócioediretordeprodutosetec-
nologianaBluesoftemSãoPauloetambémAssociatedTrainernaAdaptworks.
SouBacharelemSistemasdeInformaç ãopelaFIAP,BlackBeltemLeanSeis
SigmapelaFundaçãoVanzolini,eManagement3.0LicensedTrainer.
Ofocoprincipaldomeutrabalhoénodesenvolvimentodesoftware,atuando
naliderançadeequipes,nocoachingdemétodoságeis,enodesenvolvimentode
produtosparaaInternetcomdiversastecnologiaseplataformas.
MinhacarreiraemTIcome çouem1999edesdeentãotrabalheicomumagrande
diversidadedetecnologias.
Desde2007venhoaplicandométodoságeisnodiaadia,esemprebuscandome-
lhoresformasdeselidarcomosdesafiosdagestãoedodesenvolvimentodesoftware.
Atuotambémcomopalestrante,tradutor,escritorepodcaster.Escrevoartigos
pararevistaseportaisdeTI,emantenhomeublogandrefaria.com.
iii

## Página 9

CasadoCódigo
Prefácio
Oanoera2001eeuestavaprestesaabandonaracarreiradegerentedeprojetosde
software.Eunãoaguentavamaisaquilo.Eraoescopoquesempremudava.Oprazo
ecustoquesempreestouravam.Oclientequenuncasabiaoquequeria.Acorreria
defimdeprojeto.Finsdesemanaemadrugadastrabalhando.Conflitos.Prejuízo.E
aeternaesperan çadeque“nopróximoseriadiferente”.Nãodavamais.
NaquelemesmoanoumamigomeemprestouumlivrosobreumatalFDD
(Feature-DrivenDevelopment)e,apóslereversentidoemmuitodoqueestavaali,
decidimedarmaisumachanceetentarnovamente,masagoradeumaformadife-
rente,afinal,pensei,sevocênãopodemudarumasituaç ão,devemudarsuaatitude
emrelaçãoaela.Naquelemomento,abrindominhamenteàspossibilidades,abra-
ceiAgile-semsaberqueaquiloeraAgile-emudeicompletamenteomeudestino
profissional.Depoisdoprimeiroprojetoconseguindoterminhaqualidadedevida
eauto-estimaprofissionalrecuperadas,evendoosorrisonorostodocliente,decidi
mergulhardecabe çanestemundo.Nãohaveriavolta.
Hoje,depoisdoquevinaprática,nastrincheiras,portodosessesanos,euafirmo
avocê:oresultadodosprojetosdedesenvolvimentodesoftwarequeutilizamméto-
doságeisémuitosuperiorsecomparadoàstécnicasmaistradicionaisdegestãode
projetoseengenhariadesoftware. Equandoeufaloemmelhorresultado,nãoes-
toufalandoapenasdeumamaiorentregadevalor,tópicobrilhantementeabordado
nestelivro,masfalotambémdeaspectosquevãodesdeageraç ãodeprodutoscom
qualidadetécnicaàconstruçãodeummelhorambientedetrabalho.Estoucertode
queempoucosanosnoslembraremosdeAgilecomoummarconanossaprofissão,
ummarcoparaaáreadetecnologia.
Mas,afinaldecontas,oqueéAgile? Éumametodologia? Umprocesso? Um
conjuntodevalores?Ummanifesto?Ferramentas?Práticas?Ummovimento?Bem,
porincrívelquepare ça,estaéumaperguntadifícildeserrespondida. Umadas
razõeséporqueAgilepodenãosernadadoquecitei,e,aomesmotempo,pode
v

## Página 10

CasadoCódigo
compreendertudoaquilo.ÉmuitodifícilexplicarAgilesemmostraraprática.De
fato,frequentementecitoqueaformacorretadeexplicaroqueéAgiledeveriaser
“Ei,venhaaquivercomoestoufazendo!”Eénestepontoquedestacoovalorde
cadaumadaspáginasdestelivro,elasmostramoAgiledo“mundoreal”,infestado
depragmatismoedepreciosasanotaçõesdequemvalorizasimumaboateoria,mão
nãoantesdepratica-la,devê-larealmentefuncionando.
UmlivrodeverdadesobreAgilenãopoderiatercapítuloscujostítulosfossem
puramenterelacionadosaumaregra,artefatoouferramentadeumououtrométodo
ágil.UmverdadeirolivrosobreAgiledeveriamanterofocodeseuscapítulosnaen-
tregadevaloraonegócio,naotimizaç ãodestevalorenaconstruç ãodeumnovo
ambientedetrabalho,umanovagestão.UmverdadeirolivrodeAgiletirariaosho-
lofotesdosfamososmétodoságeis,taiscomoScrum,XPeKanban,eosapresentaria
apenascomoummeioparasedesenvolverdaformacertaprodutosquerealmente
agreguemvaloraquempagaaconta:nossosclientes.
Sendoassim,nãoexitoemafirmarqueesteéumverdadeirolivrodeAgile.Éo
livroquevocêdevelercasoqueiraconstruirumnovoemelhorcaminhoparaasua
carreiranaáreadeprojetosdesoftware.
AlexandreMagno
Agile Expert e Fundador da AdaptWorks
vi

## Página 11

CasadoCódigo Sumário
Sumário
1 IntroduçãoàMétodosÁgeis 1
1.1 OManifestoÁgil . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2 MétodosÁgeis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.3 CompreendendoosValoresÁgeis . . . . . . . . . . . . . . . . . . . . . 8
1.4 BenefíciosdosMétodosÁgeis . . . . . . . . . . . . . . . . . . . . . . . 9
1.5 AgregandoMaisValorcomScrum . . . . . . . . . . . . . . . . . . . . 12
1.6 ExcelênciaTécnicacomXP. . . . . . . . . . . . . . . . . . . . . . . . . 14
1.7 FluxoContínuocomKanban . . . . . . . . . . . . . . . . . . . . . . . 16
1.8 QualéoMelhorMétodo? . . . . . . . . . . . . . . . . . . . . . . . . . . 18
1.9 Eagora,oqueeufaçoamanhã? . . . . . . . . . . . . . . . . . . . . . . 19
2 FluênciaÁgil 21
2.1 EvoluçãoeMaturidadedeumaEquipeÁgil . . . . . . . . . . . . . . . 23
2.2 Ordem,CaoseComplexidade . . . . . . . . . . . . . . . . . . . . . . . 26
2.3 Eagora,oqueeufaçoamanhã? . . . . . . . . . . . . . . . . . . . . . . 29
3 FocoemValorparaoNegócio 31
3.1 DisseminandoaVisãodoProjeto . . . . . . . . . . . . . . . . . . . . . 33
3.2 PlanejamentoeDesenvolvimentoIterativo . . . . . . . . . . . . . . . . 35
3.3 PlanejandoumaIteração . . . . . . . . . . . . . . . . . . . . . . . . . . 38
3.4 AReuniãoDiária . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
3.5 LimitandooTrabalhoemProgresso . . . . . . . . . . . . . . . . . . . 44
3.6 EscrevendoHistóriasdeUsuário . . . . . . . . . . . . . . . . . . . . . 45
3.7 Mapeandohistóriasdeusuários . . . . . . . . . . . . . . . . . . . . . . 51
3.8 ConhecendoosUsuáriosatravésdePersonas . . . . . . . . . . . . . . 53
vii

## Página 12

Sumário CasadoCódigo
3.9 MelhorandoaPrevisibilidadecomEstimativas . . . . . . . . . . . . . 56
3.10 DefinindoEntregascomoPlanejamentodeReleases . . . . . . . . . . 57
3.11 RoadmapdoProduto . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
3.12 MantenhaasOpçõesAbertas . . . . . . . . . . . . . . . . . . . . . . . 61
3.13 Eagora,oqueeufaçoamanhã? . . . . . . . . . . . . . . . . . . . . . . 65
4 EntregandoValor 67
4.1 TestesÁgeis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
4.2 SimplificandooCódigocomRefatoração . . . . . . . . . . . . . . . . 74
4.3 CódigoLimpo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76
4.4 PropriedadeColetivadoCódigo . . . . . . . . . . . . . . . . . . . . . . 77
4.5 Linguagemubíqua . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
4.6 DesignÁgiléDesignIterativo . . . . . . . . . . . . . . . . . . . . . . . 78
4.7 DefinindoosignificadodePronto . . . . . . . . . . . . . . . . . . . . . 80
4.8 IntegraçãoContínua . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
4.9 ProgramaçãoemPar . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
4.10 RevisãodeCódigo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
4.11 DívidaTécnica. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
4.12 AgilidadeExplícitacomMuraldePráticas . . . . . . . . . . . . . . . . 89
4.13 Eagora,oqueeufaçoamanhã? . . . . . . . . . . . . . . . . . . . . . . 90
5 OtimizandoValor 93
5.1 DirecionandoaEquipe . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
5.2 MétricasÁgeis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
5.3 ApresenteoResultadoemReuniõesdeDemonstraç ão . . . . . . . . . 101
5.4 MelhoriaContínuacomRetrospectivas . . . . . . . . . . . . . . . . . . 101
5.5 EliminandoDesperdícioscomLean . . . . . . . . . . . . . . . . . . . . 111
5.6 Eagora,oqueeufaçoamanhã? . . . . . . . . . . . . . . . . . . . . . . 114
6 OtimizandooSistema 117
6.1 AGestãopodeserÁgil? . . . . . . . . . . . . . . . . . . . . . . . . . . . 118
6.2 Feedback . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
6.3 EscalandoÁgilcomProgramasePortfólios . . . . . . . . . . . . . . . 129
6.4 FormaçãodasEquipes . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
6.5 PráticasdeAprendizagem . . . . . . . . . . . . . . . . . . . . . . . . . 133
viii

## Página 13

CasadoCódigo Sumário
6.6 Hackathons. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138
6.7 ComunidadesdePrática. . . . . . . . . . . . . . . . . . . . . . . . . . 139
6.8 Eagora,oqueeufaçoamanhã? . . . . . . . . . . . . . . . . . . . . . . 141
7 ApêndiceA:FerramentasdeApoio 143
Bibliografia 149
ix

## Página 15

Capítulo1
IntroduçãoàMétodosÁgeis
Nasemanapassada,entrevisteiJoana,umamo çaquehaviapassado8mesestra-
balhandoemumprojetoparaumgrandebanco. Elaesuaequipepassaramtodo
essetempoapenasfazendolevantamentoderequisitosedocumentandosuasdes-
cobertas,atéquedescobriramqueoproblemaqueosoftwareaserdesenvolvidose
propunhaaresolverjáhaviasidosolucionadoporumaferramentatrazidadeuma
fusãocomoutrobanco(hádoisanosatrás)ejánãoeramaisumproblema.Oprojeto
foicancelado.
Oresultadode8mesesdetrabalhodeumaequipe,maisoinvestimentodotempo
dediversosinteressadosquecolaboraramcominformaçõesparaoprojetoseresu-
miuaum“bolodedocumentação”queagora,provavelmente,nuncamaisseráse-
querlidaporninguém.Joanaestavafrustradacomsuaúltimaexperiência,eprova-
velmentequemquerqueestivessepagandoporesseprojetotambém.
AexperiênciadeJoananãoéumcasoisolado. Naverdade,muitosemuitos
projetostiverame,infelizmente,aindaterãodestinossemelhantesaesse. Maspor
quê?Seráqueháumaformamelhordegerenciaredesenvolversoftwarequeevite

## Página 16

1.1. OManifestoÁgil CasadoCódigo
tantodesperdício?Aboanotíciaéquehá!Métodoságeissãoumavacinacontrao
desperdício.
Porisso,nosúltimosanos,osmétodoságeisvêmganhandomaisemaispopula-
ridade,egrandesempresascomoGoogle,Yahoo!,Microsoft,IBM,Cisco,Symantec
eSiemensostêmutilizado[66].Masafinaloqueosmétodoságeistrazemdedife-
rente?Oquetemdespertadotantointeressenessesgrandesplayersdomercadode
tecnologia?Paracompreendermelhor,vejamoscomotudocome çou.
Noiníciodadécadade90,nointuitodedesburocratizarosprocessosdede-
senvolvimentodesoftware,novasabordagenschamadasde“processosleves”,como
Scrum,ExtremeProgramming(XP),eFeatureDrivenDevelopment(FDD),para
citaralgumas,come çaramaemergir,mostrando-semaisbemsucedidasdoqueten-
tativasanteriores.
1.1 OManifestoÁ gil
Devidoaograndenúmerodereferênciasaessesprocessosleves,queemergiamcomo
respostaaosconstantesfracassosdeprojetosutilizandoabordagenstradicionais,em
fevereirode2001umgrupodeprofissionaisextraordináriosdodesenvolvimentode
softwarereuniu-seemumResortdeSkiemWasatchRangeparadiscutirmelhores
maneirasdedesenvolversoftware.Esseencontrodeuorigemaomanifestoágil,uma
declaraçãocomosprincípiosqueregemodesenvolvimentoágil[64]:
2

## Página 17

CasadoCódigo Capítulo1. IntroduçãoàMétodosÁgeis
OM anifestoÁ gil
Estamosdescobrindomaneirasmelhoresdedesenvolversoftware,
fazendo-onósmesmoseajudandooutrosafazê-lo. Atravésdessetra-
balho,passamosavalorizar:
•Indivíduoseainteraçãoentreeles maisqueprocessoseferra-
mentas;
•Softwareemfuncionamentomaisquedocumentaçãoabrangente;
•Colaboraçãocomocliente maisquenegociaçãocontratual;
•Responderamudançasmaisqueseguirumplano.
Mesmohavendovalornositensàdireita,valorizamosmaisositensà
esquerda.
Alémdesses4valores,omanifestoágiltambémécompostopor12princípios:
• Nossamaiorprioridadeésatisfazeroclienteatravésdaentregacontínuaeadi-
antadadesoftwarecomvaloragregado.
• Mudançasnosrequisitossãobem-vindas,mesmotardiamentenodesenvol-
vimento. Processoságeistiramvantagemdasmudan çasvisandovantagem
competitivaparaocliente.
• Entregarfrequentementesoftwarefuncionando,depoucassemanasapoucos
meses,compreferênciaàmenorescaladetempo.
• Pessoasdenegócioedesenvolvedoresdevemtrabalhardiariamenteemcon-
juntoportodooprojeto.
• Construaprojetosemtornodeindivíduosmotivados.Dêaelesoambientee
osuportenecessárioeconfienelesparafazerotrabalho.
• Ométodomaiseficienteeeficazdetransmitirinformaçõesparaeentreuma
equipededesenvolvimentoéatravésdeconversafaceaface.
• Softwarefuncionandoéamedidaprimáriadeprogresso.
3

## Página 18

1.2. MétodosÁgeis CasadoCódigo
• Osprocessoságeispromovemdesenvolvimentosustentável.Ospatrocinado-
res,desenvolvedoreseusuáriosdevemsercapazesdemanterumritmocons-
tanteindefinidamente.
• Contínuaatençãoàexcelênciatécnicaebomdesignaumentaaagilidade.
• Simplicidade-aartedemaximizaraquantidadedetrabalhonãorealizado-é
essencial.
• As melhores arquiteturas, requisitos e designs emergem de equipes auto-
organizáveis.
• Emintervalosregulares,aequiperefletesobrecomosetornarmaiseficaze
entãorefinaeajustaseucomportamentodeacordo.
OsprofissionaisquederamorigemaomanifestoágilforamKentBeck,MikeBe-
edle,ArievanBennekum,AlistairCockburn,WardCunningham,MartinFowler,
JamesGrenning,JimHighsmith,AndrewHunt,RonJeffries,JonKern,BrianMa-
rick,RobertC.Martin,SteveMellor,KenSchwaber,JeffSutherlandeDave Thomas.
Aolongodesselivronósestudaremoscomoessesvaloreseprincípiosãocoloca-
dosempráticanasatividadesenodia-a-diadasequipeságeis.
1.2 MétodosÁ geis
OManifestoágiléoembasamentofilosóficodetodososmétodoságeisediversos
métodosdedesenvolvimentodesoftwareestãoalinhadosaele.Amaioriadelesse
utilizadecicloscurtos,quesãochamadosdeiteraçõesenormalmentetêmduraç ão
depoucassemanas,dessaformagarantindofeedbackfrequenteerespostasrápidas
àsmudanças.
Cadaiteraçãocontémtodasasetapasnecessáriasparaqueserealizeumincre-
mentonoproduto,ouseja,nosoftware:planejamento,análise,design,codificaç ão,
testesedocumentação.Emmétodosnãoágeis,tambémconhecidoscomométodos
tradicionais,geralmenteseencontraumprocessoemcascataemquetodasaseta-
pascitadassãoexecutadasumaúnicavezeemsequência(aindaqueidealmente,
prevendo-serevisõesincrementaisdecadaetapa,senecessário).
Scrum,ExtremeProgramming(XP),CrystalCleareFeatureDrivenDevelop-
mentsãoexemplosdemétodoságeis.Cadaumdelestrazumaabordagemdiferente
queincluidiversosvalores,práticasereuniões. OScrum,porexemplo,trazuma
4

## Página 19

CasadoCódigo Capítulo1. IntroduçãoàMétodosÁgeis
abordagemmaisvoltadaparaagestão,commaiorfoconasreuniões,noplaneja-
mentoenamelhoriacontínua.JáoXP,trazemmaiorenfoquenaspráticastécnicas.
Aodecorrerdolivroestudaremosmelhoressesmétodoseexploraremosalgumas
práticaságeis.
ACascatadosMétodosTradicionais
“Não é o mais forte que sobrevive, nem o mais inteligente, mas o que melhor se
adapta às mudanças. ”
–CharlesDarwin
Emcontrapartida,osprocessostradicionaisouemcascata(figura 1.1),queeram
amplamenteutilizadosdomercadoantesdosmétodoságeis,assumemqueodesen-
volvimentodesoftwarepodeserrealizadoatravésdeumasequênciadeatividades
facilmenteidentificadas,previsíveiserepetíveis,masdiferentedeoutrasengenha-
rias,desenvolvimentodesoftwarerequercriatividade,egeralmenteenvolveumalto
nívelderiscoseincertezas[38].
Oprocessocascatacostumaserrealizadoatravésdefasesdeanálisederequisitos,
projeto(design),implementação,testes,integraçãoemanuten ção,deformaqueuma
faseéiniciadasomentequandoaanteriortermina. Otermofoioriginadoemum
artigopublicadoem1970porW.W.Royce[52].Opróprioautordescreveuométodo
comoarriscadoepropensoafalhas.
5

## Página 20

1.2. MétodosÁgeis CasadoCódigo
Figura1.1:ProcessoemCascata(Waterfall)
Éclaroquedesenvolvimentoágilnãoéaúnicaformadeseencararodesenvol-
vimentodesoftware,neméaúnicamaneiraeficiente;comodisse,FrederickBrooks
em1986,nenhumatecnologiaoutécnicadegestãoresolvetodososproblemasde
todososcontextos.Eleresumiuessaideiadizendoque“nãohápratadebala”[15].
Métodoságeisassumemimprevisibilidadenaturaldodesenvolvimentodesoft-
ware, porisso, considera-sequeoclientetambémestáaprendendosobreoque
precisae,queacadafeedbackpodemudardeideiaealteraroescopodoprojeto.
Assume-setambémqueestimativasdeesfor çoetempodedesenvolvimentosão,de
fato,estimativas,enãodevemsertratadascomoalgocertoesemmargemdeerro.
Porassumiraimprevisibilidadeenvolvidanodesenvolvimentodesoftware,mé-
todoságeissebaseiamnosciclosdefeedbackconstantepermitindoqueoclienteea
equipededesenvolvimentopossamadaptar-seàsmudan ças,aumentandoassimas
chancesdesucessodoprojeto.
Umfatointeressante,quemuitasvezesédeixadodeladonasdiscussõessobre
métodoságeis,équeomanifestoágilnãofoiumareaçãoapenasaosmétodostradi-
cionaiseburocráticos,mastambémfoiumareaçãoaosmétodoscaóticosqueresul-
6

## Página 21

CasadoCódigo Capítulo1. IntroduçãoàMétodosÁgeis
tavamemprodutosdebaixaqualidade.Osmétodoságeisrepresentam,justamente,
ummeiotermoentremétodosestruturadosdemaisemétodossemestrutura,sãoo
meiotermoentreaordemeocaos[8].
Comintuitodepromoverosmétodoságeis,foiinstituídaaAlian çaÁgil(Agile
Alliance),queapoiouerealizouumasériedeeventoseconferênciasaoredordo
mundo. Comotempo,maisemaisempresasepessoasforamadotandométodos
ágeiseatualmentemilhõesdepessoasconsideram-sepraticantesdessesmétodos.
MétodosPrescritivoseAdaptativos
Métodoságeissãoadaptativosaoinvésdeprescritivos,porisso,incentivama
melhoriacontínua(implicandoemumconstanteestadodemudan çasetransfor-
mação,visandoalcan çarumestadomelhor)atravésdeciclosinspe çãoeadaptação.
Esseéomotivopeloqualmétodoságeisutilizamprocessosempíricos,emvezde
prescritivos[36].
Enquantoprocessosempíricossãoapropriadosparadomíniosinstáveisecom
altoníveldemudan ças,processosprescritivossãoindicadosparaatividadesorde-
nadasquepodemseralcan çasatravésdeumasequênciadepassos.
Figura1.2:MétodosMaiseMenosPrescritivos
Éporissoquemétodoságeissãomenosexplícitosemtermosdepapéis,ativida-
deseartefatosdoquemétodostradicionais(prescritivos).Paraseterumaideia,o
7

## Página 22

1.3. CompreendendoosValoresÁgeis CasadoCódigo
RUPpossuimaisde120prescrições,oXP13,oScrum9,eKanbanapenas3[34].
Quantomaisprescritivoummétodofor,maisespecíficoparaumdeterminado
tipodecontextoeleserá.Emcontrapartida,quantomaisadaptativo,maiorserásua
aderênciaeflexibilidadeparaquesejaotimizadocommaioreficiênciaemdiferentes
contextos.
Emregrageral,aoutilizarummétodoprescritivocomoRUP,porexemplo,você,
possivelmente,precisaráencontrarámuitomaisdoquerealmenteprecisa,ejácom
métodosmenosprescritivoscomoScrum,vocêprecisaráincluirtudoaquiloque
estiverfaltandoparaqueoprocessosejaeficienteemseucontexto.
1.3 Compreendendo os ValoresÁ geis
Conformecitadoanteriormente,oManifestoÁgiléformadoporquatrovaloresfun-
damentais,queagoravamosexploraremmaisdetalhes.
Oprimeirovalor,quediz“indivíduoseainteraçãoentreelesmaisqueproces-
soseferramentas”,tratadeentenderqueumaequipeéformadaporpessoase,que
cadaumaédiferenteeúnicaepossuipontosfortesefracos,enãosãovistasapenas
“recursos”homogêneosesubstituíveis.
Obomrelacionamentosentreosmembrosdaequipeéconsideradocrucial,epor
isso,aagilidadedoambienteestimulaotrabalhoemequipe,acolaboraç ão,eacomu-
nicaçãoconstante.Asequipes,geralmente,sãoformadasporpessoascomdiferentes
papéis,queseresponsabilizamjuntaspeloresultadodotrabalhoquerealizam.
Processossãorealizadosporpessoas,easferramentassãoutilizadasporpessoas.
Seainteraçãoentreelasnãoestiverfluídaebemequilibrada,provavelmente,aeficá-
ciadosprocessoseferramentasserácomprometida.Porisso,nosmétodoságeis,as
pessoasestãoemprimeirolugar.Outrofatorimportanteéqueexcelentesferramen-
taseprocessossempessoasexcelentesenvolvidas,muitoprovavelmente,produzirão
umresultadomedíocreemvezdeexcelente[19].
Poroutrolado,éimportanteressaltarqueasferramentastambémsãoimpor-
tantes,apenasnãosãomaisimportantesdoqueaspessoas. Essalógicavalepara
todososvaloresdomanifesto:oelementodaesquerdaémaisimportantedoqueo
dadireita,porémodadireitatambéméimportanteerelevante.
Osegundovalor“softwareemfuncionamentomaisquedocumentaçãoabran-
gente”éumarespostaaprojetostradicionaisemque,porseremrealizadosporfases,
costumava-sepassarmesesproduzindoapenasdocumentaç ão,queporsisó,não
agregamuitovalor,ou,talveznenhumvaloraocliente.
8

## Página 23

CasadoCódigo Capítulo1. IntroduçãoàMétodosÁgeis
Anaturezaiterativadosmétodoságeispermitequesoftwareemfuncionamento
sejaentregueaoclienteemcurtosperíodosdetempo,dessaformaagregandova-
lormaioremcurtoespaçodetempo. Éclaroqueumavezqueadocumentaç ãoé
importanteparaoprojeto,acadaentrega,elapoderáserdevidamenteproduzidae
entreguejuntocomosoftwareemfuncionamento.
A“colaboraçãocomoclienteémaisvalorizadadoquenegociaçãocontratual”
justifica-seporqueoobjetivodaequipeágiléentregarumprodutoqueagreguevalor,
eparaissoéprecisoestarsempreprontoaadaptar-seàsmudan çasque,geralmente,
ocorremnomundodosnegócios,econsequentementeafetamumaideiadeescopo
inicialqueoclientetinhadoprojetoaserdesenvolvido.
Contratos,geralmente,sãonecessários,masmuitossãoprotecionistasdemais
eprocuramfecharoescopodoprojetodesdeoinício,reduzindoassimasoportu-
nidadesdecolaboraçãoedescobertajuntocomoclienteaolongodoprocessode
desenvolvimento,resultandoemprodutosque,muitasvezes,nãoatendemàneces-
sidadedequemestápagando.
Oimportanteéqueocontratomatenhaomáximodeop çõesabertasparaqueo
projetopossamudarnamedidadonecessárioedessaformaoprojetosejaadaptável
e,realmente,gerevaloraocliente.
Alémdisso,éessencialacolaboraçãoeparticipaçãodoclienteduranteodesen-
volvimento.Métodoságeisprocuramtrazeroclienteparapertodaequipe,ocliente
fazpartedoprojetoetemumpapelmuitoimportanteparaqueoprojetosejabem-
sucedido.
A única coisa constante é a mudança. ”
–HeráclitodeÉfeso
Finalmente, “responderamudançasémaisimportantedoqueseguirum
plano”,dizrespeito,essencialmente,àcapacidadedeadaptaçãoqueumaequipeágil
precisapossuir.Planejarépreciso,masplanosnãoprecisamser“escritosempedras”,
elespodemserapagados,corrigidos,refeitos.
Acapacidadedeadaptar-seemummundoemconstantemudan çaéumaquali-
dadeessencialentregarprojetosrelevantesebem-sucedidos.
1.4 Benefícios dosMétodosÁ geis
Umadasmaioresmotivaçõesparaatransiçãoparamétodossãoosbenefíciosque
sãotrazidosparaaorganizaçãodevidoaovalorqueéagregadoaoclientecomqua-
9

## Página 24

1.4. BenefíciosdosMétodosÁgeis CasadoCódigo
lidadeevelocidade[63].Métodoságeisajudamorganizaçõesarespondermaisrapi-
damenteàsnecessidadesdomercado,muitasvezes,resultandoemgrandevantagem
competitiva.
UmapesquisarealizadapelaVersionOne.comem2011[65]envolveumaisde
6.000pessoaseorganizaçõesdosmaisvariadosperfisnaindustriadedesenvolvi-
mentodesoftware.Elanosmostraalgunsdosprincipaisbenefíciosobtidosporessas
organizaçõesapósatransiçãoparmétodoságeis.Osprincipaisbenefíciossão:
•MelhorTime-to-marketeMaiorRetornosobreoInvestimento: Quanto
maiscedoosclientespuderemcome çarautilizaroproduto,maisrápidorece-
beráoretornodovalorinvestidonodesenvolvimentodoproduto,sejaatravés
delucrosdiretosgeradospeloprodutoouatravésdosbenefíciosgeradospela
utilizaçãodoprodutonaorganização.
•MaiorSatisfaçãodoClienteeMelhorGestãodeMudanç asdePrioridades:
Oplanejamentoiterativopermitequeoclientefacilmentemudesuasprio-
ridadescomimpactoreduzidonaprodutividadedaequipeporqueplaneja-
sedetalhamentoapenasdaquiloqueestámaispróximodeserfeito,evitando
tambémdesperdíciosecustosdesnecessários. Acomunicaçãoconstanteea
proximidadecomoclientefrequentementeresultatambémemummelhor
alinhamentoentreosobjetivosdeTIecomosobjetivosdenegóciodaorga-
nização.
•MelhorVisibilidadedosProjetos: Fazpartedaculturaágilmanterasin-
formaçõesdoprojetovisíveisetransparentesatravésdeferramentascomo
burndown-charts,ecardwalls(discutidasposteriormente),comasquaisa
equipeegestãopodemacompanhardiaadiaaevoluç ãodoprojetoemrela-
çãoàsmetasdoprojetoedasiterações;
•MaiorProdutividade:Infelizmente,nãoháumaformauniversalmenteaceita
desemedirprodutividadedeequipesdedesenvolvimentodesoftware.Mui-
tosconsideramessatarefaatéimpossíveloualgosubjetivodemais,masna
pesquisasupracitada,75%dosparticipantesafirmaramteralcan çadomelhor
produtividadedepoisdatransiçãoparamétodoságeis;
•EquipesmaisMotivadas: Métodoságeispromovemritmossustentáveisde
trabalho,sãomuitososcasosemqueorganizaçõesreportaramumadiminui-
çãosignificativanashorasextrasemadrugadastrabalhadasdepoisdatransi-
10

## Página 25

CasadoCódigo Capítulo1. IntroduçãoàMétodosÁgeis
çãoparamétodoságeis[20].Apromo çãodoritmosustentável,deumacul-
turadequalidade,deconstantecomunicaçãoetrabalhoemequipesãoalguns
dosfatoresquecontribuemparaequipesmaismotivadasesatisfeitascomseu
ambientedetrabalho.
•MelhorDisciplinanaEngenhariaeMelhorQualidadeInterna: Autiliza-
çãodepráticaságeiscomoreduçãodedívidatécnica(melhoraraqualidade
internadoproduto),refactoring,desenvolvimentoorientadoatesteseprogra-
maçãoempar,unidoaomindsetdequalidadeestimuladodepelosmétodos
ágeis,contribuemparaaentregadeprodutoscommelhormantenabilidade,
extensibilidadeecommenosdefeitos.
•ProcessodeDesenvolvimentoSimplificado: Osmétodoágeissão,emre-
grageral,menosprescritivosdoqueosmétodostradicionais,definemmenos
papéisemenosartefatos.Sãomaisfacilmentecompreendidospelaequipe,e
oferecemmaiormargemparaotimizaçãoeadaptaçãoparaamaioreficiência
nocontextodaorganizaçãoemqueestásendoaplicado.
•ReduçãodeRisco:Oplanejamentoiterativoeas releasesfrequentespermitem
queasprioridadesdoprojetosejamreajustadasconstantemente.
Métodoságeispossibilitamqueasincertezasdoprojeto,noníveldosrequi-
sitos,ounoníveltécnico,sejamestimadasedistribuídasdeformainteligente
nos releases,paramanteroriscosemprebalanceado.Alémdisso,asentregas
emprazoscurtosoferecemmaiorvisibilidadedavelocidadedotime,ofere-
cendomaiorprevisibilidadedoprazonecessárioparaconcluiroprojeto.
•ReduçãodeCustos:Equipeságeissãomenospropensasadesenvolverfun-
cionalidadesdebaixaprioridadeouquesetornaramdesnecessáriasaolongo
dotempo[20]. Abordagensnãoágeisgeralmentetendemacairnessepro-
blemadevidoaograndeespaçodetempoentreolevantamentodosrequisitos
eentregadoproduto.
11

## Página 26

1.5. AgregandoMaisValorcomScrum CasadoCódigo
1.5 Agregando MaisValor com Scrum
Figura1.3:Scrum
Scruméumdosmétodoságeismaispopularesnaatualidadeetemfocomaiornos
aspectosgerenciaisdodesenvolvimentodesoftware.Nele,cadaiteraç ãoéchamada
desprint.Geralmentecadasprinttemumperíododemêsquepodevariardepoucos
diasaalgumassemanas.Aspessoasenvolvidasnoprocessodedesenvolvimentosão
dividasnoScrumemtrêspapéisprincipais:oScrumMaster,o Product Owner(dono
doproduto)eaequipe.
O Product Owneréomaiorinteressadonosoftware,éaquelequeteve(ouque
representaquemteve)anecessidadedoproduto,eporissotemavisãodoproduto.
Defineoquedeveserfeito,epriorizaasfuncionalidadesaseremdesenvolvidas,
mantendo-asemumartefatochamadode product backlog,quenadamaisédoque
umalistadetodasasfuncionalidadesquedevemserimplementadas,ordenadaspor
prioridade.
Étambémresponsabilidadedo Product Ownerpassartodaainformaçãodene-
gócioquefornecessáriaparaqueaequipepossatransformarsuasideiasemsoftware.
AEquipeécompostaporumnúmeroquevariadecincoanovepessoaseé cross-
funcional,istoé,hápessoasdosmaisvariadosperfis,comotestadores,desenvolve-
12

## Página 27

CasadoCódigo Capítulo1. IntroduçãoàMétodosÁgeis
dores,designers,analistasdenegócioetc.integrandoaequipe.Oprincipalobjetivo
delaéimplementarasfuncionalidadesqueforamselecionadasparaseremdesenvol-
vidasnaiteraçãoeentregá-lasemfuncionamentoaofinaldesseperíodo.Nocapítulo
6abordaremosmaisafundoasvantagensdesetrabalharcomequipespequenas.
OScrumMaster,tambémchamadodefacilitador,éresponsávelpormantero
processoemfuncionamento,assegurandoquetodasasregrasestãosendoaplica-
das,eremoverosimpedimentosdaequipe,istoé,resolverqualquerproblemaque
possaatrapalharoprogressododesenvolvimento,garantindoassimqueoobjetivo
daiteraçãosejaatingido.
ÉimportanteressaltarqueoScrumMasternãoatuacomoumgerenteouchefe
daequipeporqueelaéauto-organizável.OScrumMasternãodeterminaoquecada
membrodaequipedeveounãofazer:aequipesecomprometecomaentregadas
funcionalidadese,então,seauto-organiza,definindoporquemeemqualmomento
astarefasserãorealizadas.
Todasprintcome çacomumareuniãodeplanejamento,queédivididaemduas
partes.Aprimeiradelastemumenfoquemaisestratégico,naqualsedecideoque
seráfeito,istoé,quaisfuncionalidadesserãoimplementadasedefine-seumameta
paraaSprint.Paraisso,o Product Ownerapresentaositensdo product backlog,ea
equipeobtéminformaçõessuficientessobrecadaumdositens,dessaforma,épossí-
velfornecerumaestimativaqueexpresseumtamanhoouumnúmerodehoraspara
otrabalhoeassimsejadefinidoquantasequaistarefaspoderãoserdesenvolvidas
nosprint(deacordocomavelocidadedaequipequeécalculadaatravésdedadosde
sprintspassados).
Depoisdedefinidasquaistarefasserãodesenvolvidasnosprint,aequipeutiliza
asegundapartedareunião,quetemumenfoquemaistático,paradecidircomo
serãofeitasastarefas. Entãoseanalisatarefaportarefacommaisdetalhes,mais
informaçõesdenegóciosãoapresentadaseépossíveltomardiversasdecisõesde
negócioedecisõestécnicas.
Aofimdareuniãodeplanejamentoaequipecome çaatrabalharnastarefas,res-
peitandoasprioridades:fazendosempreprimeiroastarefasmaisimportantes,que
representammaiorvalorparaoprodutodeacordocomo Product Owner. Todos
osdiasérealizadaumareuniãoparaqueaequipeconversesobreoandamentodo
sprint.Posteriormenteapresentaremosemmaisdetalhesasreuniões.
AolongodaSprintaequipemantémsempreemmenteasuametaequandoo
andamentodascoisasfogedoquefoiprevisto,elapodenegociaroescopocomo
Product Owner,deformaquenãocomprometaameta[59].
13

## Página 28

1.6. ExcelênciaTécnicacomXP CasadoCódigo
Timeboxes
OScrumrefor çaaideiadequetodasascerimôniasdotimepreci-
samterum timebox(tempodefinido)equeémuitoimportantequees-
sestempossejamrespeitadosparasemanterumritmosustentável. Se
as Sprints,porexemplo,temduraçãodeduassemanas,éimportanteque
nãosejamextendidas.Seareuniãodiáriadura15minutos,éimportante
queareuniãonãosejaextendida.Os timeboxesdasoutrasreuniõesva-
riamdeacordoo timeboxda Sprinteepodemvariartambémdeacordo
comcadacontextodaequipe.
OstempossugeridosparaumSprintde30diassão[59]:
• ReuniãoPlanejamento:8horas.
• ReuniãodeRevisão(Demonstração):4horas.
• ReuniãodeRetrospectiva:3horas.
Aofimdosprint,maisduasreuniõesacontecem:areuniãoderevisãoeareu-
niãoderetrospectiva.Nareuniãoderevisãoaequipeapresentaao Product Ownero
trabalhoquefoidesenvolvidoduranteosprint,paraqueelepossaoferecerfeedback,
eaprovarounãotudooquefoiproduzido.Nareuniãoderetrospectivaosprincipais
acontecimentosdosprintsãoapresentadosediscute-sesobreasliçõesaprendidase
melhoriasquepodemseraplicadasaoprocesso.
1.6 ExcelênciaTécnica comXP
OmétodoágilExtreme Programming(emportuguêsProgramaçãoExtrema),mais
conhecidasimplesmentecomoXP,foicriadoeinicialmentedivulgadoporKentBeck
nosanos90,eéumdosmétodoságeisquemelhorcobreaspectostécnicosdode-
senvolvimentodesoftwarecomocodificação,designetestes,veremosmaisdetalhes
aseguir.
SegundooXP,duranteoprocessodedesenvolvimentoháquatroatividadesbá-
sicasaseremexecutadas:Ouvir,Desenhar,CodificareTestar.
Éprecisoouvirporquedesenvolvedoresnemsemprepossuemoconhecimento
14

## Página 29

CasadoCódigo Capítulo1. IntroduçãoàMétodosÁgeis
denegócionecessárioparaseconstruirosoftware. O Planning Gameéumareu-
niãoqueaconteceumavezacadaiteraç ão,emqueoprincipalobjetivoédecidir
quaisfuncionalidadesserãodesenvolvidasnaiteraçãoeaprendermaissobreelas.O
clienteescreve históriasdeusuário emcartõesquerepresentamanecessidadede
funcionalidadeaserdesenvolvida,eexplicaparaosdesenvolvedorestudooquefor
precisoparaqueelespossamimplementá-la.
Umbom designéumaexcelenteferramentaparaquetodospossamcompreender
melhorossistemascomplexos,suasestruturas,dependênciaseregrasdenegócio.O
principalobjetivoémantero designsempresimples,evitandoaumentaracomple-
xidadecomacriaçãodefuncionalidadesquenãosejamrealmentenecessárias.
EssaéamáximadoprincipioYAGNI(Y ou aren’t gonna need it –Vocênãovai
precisardisto)quebasicamentedizquedevemosfazerascoisassomentenomo-
mentoemquerealmenteprecisarmosdelas:muitasvezesantecipamosodesenvolvi-
mentoantesmesmoquesurjaanecessidadereal,assumindoqueumdiaelachegará,
porém,essanecessidadepodenuncachegar.
Aomanterodesignsimplesefazersomenteaquiloquefornecessário,vocêpou-
parátempo,porquedeixarádeescrevercódigoquenãoprecisaeterámaistempo
paraseconcentrarnaqualidadedoquerealmenteénecessárioequevaiagregarva-
lorparaademandarealeatualdocliente.
Codificaréumaatividadeessencialparaodesenvolvimentodesoftware,afinal
decontas,semcódigonãoexistesoftwarealgum.Nessaetapa,éextremanteimpor-
tantequeoclientecontinueacessívelparaquepossaoferecerfeedbackeresponder
àsdiversasdúvidasquesurgemduranteodesenvolvimento.
ComXP,ostestesdeunidadesãoescritosantesdocódigodeproduç ão(dis-
cutiremosemdetalhesmaisàfrente);todoocódigofontequeseráexecutadoem
produçãoédesenvolvidoempares;aintegraç ãodocódigofonteérealizadafre-
quentementeatravésdapráticadeintegraçãocontínua;eo códigofonteécoletivo,
ouseja,pertenceatodososmembrosdaequipe,edeveserescritodeacordocomos
padrõesdefinidospeloprópriotime.
Testaréumaatividadedeextremaimportânciaparagarantiraqualidadedosoft-
wareenãoéalgoopcionalcomXP,aocontrário,todocódigodevepossuirtestesde
unidade,etodosostestesdevemserexecutadoscomsucessoantesqueumaentrega
sejafeita.Quandoumdefeitoéencontrado,cria-seumtestedeunidadeparaasse-
gurarqueessemesmodefeitojamaisvolteaacontecer.NoXPostestessãoescritos
antesdocódigodeproduçãoatravésde TDD(T est Driven Development,ouDesen-
volvimentoGuiadoporTestes).
15

## Página 30

1.7. FluxoContínuocomKanban CasadoCódigo
DevidoaofocotécnicodeXPeaofocomaisgerencialdoScrum,muitasempre-
sasoscombinamparaobterumprocessomaiscompleto,visandoumprocessomais
eficiente.Estudaremosmaisafrentecadaumadaspráticascitadas.
1.7 FluxoContínuo com Kanban
Figura1.4:Kanban
Kanbanéummétodoágilque,diferentementedamaioriadosmétodoságeis,não
possuiiterações. Aoinvésdisso,desacoplaoplanejamento,priorização,desenvol-
vimentoeentrega,deformaquecadaumadessasatividadespossatersuaprópria
cadênciaparamelhorseajustaràrealidadeenecessidadequeoprocessodemanda.
Cadênciassãorepetiçõesquesesucedememintervalosregulares.Esteéumcon-
ceitodométodoKanbanquedeterminaoritmodeumdeterminadotipodeevento.
Priorização,entregas,retrospectivas,equalquereventorecorrentepodemtersua
própriacadência.
Métodoságeis,nogeral,controlamcadênciasatravésdasiteraçõesquegeral-
menteduramdeumaaquatrosemanas.Dentrodecadaiteraç ão,realiza-seplaneja-
mento,desenvolvimento,testes,revisões,retrospectivasetc.Tudoissodentrodeum
períodopré-definido.
JácomKanbanoprocessoéumfluxocontínuoenãoéprecisoquetodootra-
balhoplanejadoestejaconcluídoparaqueumaentregasejarealizada.Nomomento
16

## Página 31

CasadoCódigo Capítulo1. IntroduçãoàMétodosÁgeis
daentrega,algumastarefasestarãoprontaseoutrasemprogresso;asqueestiverem
prontasfarãopartedaentrega,easquenãoestiveremficarãoparaapróxima.
Emmeadosde2007,RickGarbereDavidJ.Andersonapresentaramnasconfe-
rênciaso“LeanNewProductDevelopment”e“Agile2007”,osresultadosprelimina-
resdousodeKanbannaCorbis,umaempresaquevendeimagenseclipsdevídeo
fundadaporBillGates,daMicrosoft.Desdeentão,oKanbanvemganhandomaise
maisforçanacomunidadededesenvolvimentodesoftwareemaisempresaspassa-
ramaadotá-lo.
KanbanestábastanterelacionadocomoconceitodePullSystems(sistemasde
produçãopuxados),do T oyota Production System(TPS).Tradicionalmente,antesda
Toyota,agrandemaioriadasindústriasutilizavaoconceitodePushSystems(siste-
masdeproduçãoempurrada).
Umsistemadeproduçãoempurradacaracteriza-sequandoaprimeiraoperaç ão
doprocessorecebeumaordemdeproduçãoeaexecuta,empurrandooresultadoda
operaçãoatualparaaoperaçãoseguinte.Emsistemasempurrados,nãoháligaç ão
diretaentreoqueéproduzidoeademandadocliente,ouseja,pode-sedizerque
ofatodeumitemtersidoproduzidonãosignificaqueumoutroitemtenhasido
vendido.
Jáumsistemadeproduçãopuxadaexigequecadaoperaç ãodoprocessoseja
alimentadapelademandadaetapaanterior,estabelecendoumaligaç ãodiretaentre
oconsumorealdoclienteeaquantidadeproduzida.Dessaforma,ofatodeumitem
tersidovendido,gerariaademandaparaafabricaç ãodeoutro.Emumaabordagem
dedesenvolvimentodesoftware,poderíamosdizerqueademandaparasetrabalhar
emumanovafuncionalidadeseriageradaquandoalgumaoutrafosseentregue.
Kanbanéumapalavrajaponesaquesignificacartãosinalizador.Éutilizadono
SistemaToyotadeProdução(TPS)etambémpordiversasempresasqueaderiramà
filosofiaLeanpararepresentar,emumsistemapuxadodeproduç ão,umsinalpara
quesepuxemaistrabalho,ouseja,paraqueoprocessosejaalimentado.
Kanbanédosmétodosdedesenvolvimentodesoftwaremenosprescritivos,que,
deacordocomHenrikKniberg,possuiapenastrêsprescrições[34]:
1) Visualizarofluxodetrabalho(workflow);
2) Limitarotrabalhoemprogresso;
3) Gerenciaremedirofluxo.
17

## Página 32

1.8. QualéoMelhorMétodo? CasadoCódigo
Kanbanincentivaaadaptaçãobaseadaemcontexto. Destemodo,parte-seda
premissaquenãoexisteumaúnicasoluç ãoqueresolvatodososproblemasdeto-
dososdiferentescontextos,eporissoháanecessidadedeadaptaç ão,emquecada
processodeveseadequaràsnecessidadesdocontextoaquepertence.
Kanbantambémrecomendaqueseme çaoleadtime,tempomédioparasecom-
pletarumitem,deformaqueoprocessodevesercontinuamenteotimizadopara
tornaressetempocadavezmenoremaisprevisível.
1.8 Qual é oMelhorMétodo?
Knibergdefineferramentacomo“qualquercoisaquepossaserusadaparaatingir
umatarefaouobjetivo”,eprocessocomo“aformaquesetrabalha”[34].Paraele,
métodoscomoScrum,XPeKanbansãoferramentasparaprocessos,equestionar
qualéomelhordeleséomesmoquecompararseumgarfoémelhordoqueuma
faca,ouseja,issodependedocontextoedoobjetivoemquestão.
Nenhummétodoécompletoenenhuméperfeito,porisso,sinta-selivrepara
combinarasferramentaseaproveitaroquefuncionarmelhorparaseucontexto,ou
seja,considerandoaculturadasuaorganizaç ão,ashabilidadesdasuaequipeeas
restriçõesdeseuprojeto.Écomum,porexemplo,queseadotepráticasdeengenha-
riadeXP,comoprogramaçãoempareintegraçãocontínua,emtimesqueutilizam
Scrum.
Todoprojetodedesenvolvimentodesoftwareédiferente,possuipessoascom
habilidadesdiferentes,níveisdeexperiênciadiferentes,or çamento,prazo,escopoe
riscosdiferentes. Osvaloresdaorganizaçãoesuasmetastambémsãoespecíficos,
ecomtodaessavariação,semdúvida,asrestriçõestambémserãodiferentes. Por-
tanto,vocêdeveprocurarcompreendê-lasdeformaaexplorá-lasdamelhormaneira
possívelvisandoatingirbonsresultados.
Assimcomoaspráticas,ospapéisemumaequipeágil,podemvariardeacordo
comométodoutilizadoecontextodaequipe.Fiqueatentoparautilizarapenaspa-
péisquedefatoagreguemvalor,eparanãoincluirpapéisconflitantes.
Cadanovométodoquevocêestudaeconheceémaisumaferramentaparasua
caixadeferramentas,aperguntacertanãoé“qualéomelhormétodo”,mas“qualo
métodomaisadequadoparaessecontexto”,eentão,munidodesuacaixadeferra-
mentas,vocêterácondiçõesdeescolheramelhorabordagemparacadadesafio.
18

## Página 33

CasadoCódigo Capítulo1. IntroduçãoàMétodosÁgeis
1.9 E agora, o que eu faço amanhã?
Reviseosquatrovaloreságeis:vocêacreditaquesuaorganizaçãorefleteessevalores?
Senão,oquepoderiaserfeitodiferenteparaqueissomelhorasse?
Reflitasobreseuprojetoatual: Vocêeseuscolegasestãodefatotrabalhando
colaborativamenteemequipe?Estãoentregandosoftwareemfuncionamentocom
numafrequênciaadequada?Comovocêslidamcomasmudan çasdeprioridadede
negóciodocliente?
Quaissãoosbenefíciosquevocêesperaalcan çarcomautilizaçãodemétodos
ágeisemsuasequipe?Oquemétodoságeispodemtrazerdepositivoparaseucli-
ente?Comopodembeneficiarsuaequipe?Verifiquecadaumdosbenefícioslistados
nestecapítuloepenseseestãoemalinhamentocomoquevocêesperamelhorarem
suaorganização.
Pensenosdiferentespapéisepráticasdesuaequipe. Todoselesdefatoestão
agregandovaloraoprojeto?
19

## Página 35

Capítulo2
FluênciaÁgil
Emumexperimentocientífico[58],umgrupodecientistascolocoucincomacacos
numajaula.Nomeiodajaula,haviaumaescadaesobreela,umcachodebananas.
Quandoummacacosubianaescadaparapegarasbananas,oscientistasjogavam
umjatodeáguafrianosoutrosmacacosqueestavamnochão.
Depoisdecertotempo,quandoummacacotentavasubirnaescada,osoutros
batiamnele(commedodetomaroutrojato). Depoisdealgumtempo,nenhum
macacosubiamaisaescada,apesardatentaç ãodasbananas.
Oscientistas,então,trocaramumdosmacacosporoutronovo.Quandoeleten-
tousubiraescadaparapegarasbananas,tambémapanhoudosoutros.Outroma-
cacofoisubstituídoeomesmoepisódioserepetiupordiversasvezes,einclusiveos
novosmacacosaprenderamabaternosoutrosquetentavampegarasbananas.
Depoisdealgumtempo,todososmacacosforamsubstituídos,porémohábito
permaneceu,emesmososmacacosquenuncaviramojatod’águacontinuavamba-
tendonaquelesquetentavamsubirparapegarbananas.
Sefossepossívelperguntaraalgumdelesporqueelesbatiamemquemtentasse

## Página 36

CasadoCódigo
subiraescada,comcertezaarespostaseriaalgodotipo: “Nãosei,masascoisas
sempreforamassimporaqui”.
Vocêjáviualgumacoisadessetipoacontecernasempresasemquetrabalhou?
Algumaregraquejánãofazmaissentido,masque,porém,continuasendoutilizada
portodos,mesmosemquesaibaomotivo?Infelizmente,issonãoétãoincomum,e
inclusiveequipeságeispodemcairnesseengano.
Métodoságeisganharambastantepopularidadee,atualmente,vêmsendoutili-
zadosporgrandepartedasorganizaçõesquedesenvolvemsoftware,masessapopu-
laridadetambémtrouxealgunsproblemas.
Muitos passaram a se interessar por métodos ágeis apenas porque grandes
playersdomercadoestãoutilizando,porémnãobuscaramentenderaessência(co-
laboração,agregarvalordenegócio,entregasfrequentesetc.),eficaramapenasna
forma(quadrosnaparede,estimativascomcartas,backlogs,etc.).
DianaLarseyeJamesShore[57]afirmaramquemuitoslíderesdeorganizações
aindasequeixamdequenãoestãoconseguindoalcan çarosbenefíciosqueesperam
comaado çãodemétodoságeise,porisso,desenvolveramummodelodefluência
ágilparaajudarasorganizaçõesaalcan çaremessesbenefícioscommaiseficiência.
ParaLarseyeShore,afluênciaágildizrespeitoàmaneiracomqueaequiperes-
pondequandoestásobpressão:“Qualquerumpodeseguirumconjuntodepráticas
quandohátempoparafocaremumasaladeaula,masaverdadeirafluênciarequer
habilidadeepráticafrequentequepersistemesmoquandosuamenteestádistraída
comoutrascoisas,éumaquestãodehábitos”.
Essafluênciaágilestárelacionadanãoapenascomacapacitaçãodosmembrosda
equipe,mastambémcomasestruturasdegestão,comosrelacionamentos,acultura
organizacionalepráticasdaequipe.
Paraconquistarafluênciaágil,umaequipedeverápassarpor4estágiosdistintos:
1) FoconoValor(AtuarnaCulturanaEquipe).
2) EntregadeValor(AtuarnasHabilidadesdaEquipe).
3) OtimizaçãodeValor(AtuarnaEstruturaOrganizacional).
4) OtimizaçãoSistêmica(AtuarnaCulturalOrganizacional).
Aolongodestelivro,nósexploraremosoquevocêpodefazerparaajudarsua
equipeesuaorganizaçãoatrilharessecaminhoqueoslevaráaummelhorapro-
veitamentodosbenefíciosqueosmétodoságeispodemoferecer. Eparaquenão
22

## Página 37

CasadoCódigo Capítulo2. FluênciaÁgil
façamoscomoosmacacos,nósvamosbuscarentendernãoapenasaformadasprá-
ticas,mastambémaessênciadecadaumadelas.
2.1 Evolução e Maturidade de uma EquipeÁ gil
“Unir-se é um bom começo, manter a união é um progresso, e trabalhar em conjunto é
a vitória. ”
–HenryFord
Semprequeumanovaequipeéformada,naturalmente,umprocessodematuri-
dadeacontece[51].Énotávelqueumequipequeacaboudeseformarnãotrabalha
comamesmaprodutividadeedinamismoqueumaequipecujaspessoasjátiveram
algumtempoparaseconhecer,osseuspontosfortesesuasdificuldades.
Métodoságeisrequeremverdadeirasequipes,nãoapenasgrupos[53].Everda-
deirasequipeságeissãoformadasdepessoas,comumadiversidadedehabilidades,
quetrabalhamcolaborativamentecomumavisãocompartilhadaparaatingirdeter-
minadosobjetivos.
Aspessoasprecisamtrabalharalgumtempojuntasepassarportodosessesestá-
gios,porissonãosedevemoverpessoasdeumaequipeparaoutracomaltafrequên-
cia,comosefossempe çasdexadrez,essainstabilidadetodapodedestruiraintegri-
dadedotime.Issonãosignificaquedevezemquantonãosejainteressantequeas
pessoasmudemdeequipeparaquepossamdiversificarsuasexperiências,masépre-
cisoencontrarumpontodeequilíbriosaudável.Ambososextremossãoineficientes.
Noartigo "Y our Path to Agile Fluency”,DianaLarseyeJamesShore[57]afirmam
queo“turnoveréaprincipalcausadaperdadefluênciaemumaequipeágil,eque
quandoumaequipeganhaouperdemembros,enfrentaproblemasparasustentar
aquiloquejáhaviasidoaprendido.”
Em1977,BruceTuckman,criadordateoriadasdinâmicasdegrupos,publicou
umaartigochamado“EstágiosdeTuckman”quedescreveesseprocessodematuri-
dadeemquatroestágios:Formação,Confronto,NormatizaçãoePerformance(veja
nafigura2.1.
23

## Página 38

2.1. EvoluçãoeMaturidadedeumaEquipeÁgil CasadoCódigo
Figura2.1:EstágiosdeTuckman
Cadaumdosestágioscitadosanteriormentepossuialgumascaracterísticaspró-
prias:
1. Formação: Esteéoprimeiroestágiopeloqualumaequiperecémformada
passará,éomomentoemqueosmembrosdaequipecome çamaconhecerunsaos
outros,procuramentenderquaissãoashabilidadedecadaum,eastendênciasde
comportamentodecadapessoa.Nesseestágiotambémseestabelecemosprimeiros
objetivoscoletivosecompletam-sealgumastarefas,masaênfasedaspessoasainda
émaisindividualdoquecoletiva.
2.Confronto:Conflitosaparecemàmedidaquediferentesideiasparaatingir
objetivosvãosurgindoeasmetascoletivasidentificadasnoestágiodeformaç ãosão
questionadas.Algunsmembrospodemseabalarporessasituaç ão.Umalideran ça
forteéextremamenteimportanteparaqueaequipepasseporesteestágio.
3.Normatização:Énesteestágioqueaspessoasrealmentepassamapriorizar
osobjetivoscoletivosdaequipesobreosobjetivosindividuaisdecadamembro,por
isso,aequipeconsegueentraremconsensomaisfacilmente.
4.Performance:Aequipejápossuitodasascompetênciasnecessáriasparaatin-
girseusobjetivos,todosestãocomprometidosemotivados,eatuamcomverdadeiro
espíritodeequipe,pensandoemtermosde“nós”emvezde“eu”ou“eles”.Conflitos
sãofacilmentesolucionados.
24

## Página 39

CasadoCódigo Capítulo2. FluênciaÁgil
MaturidadeÁgil
Alémdeumaequipeunidaefortequesaibatrabalharcolaborativamente,épre-
cisoaprenderasetrabalharcommétodoságeis,eamadurecernautilizaç ãodasprá-
ticaságeis.
AartemarcialAikido,utilizaummétododeaprendizagemdesenvolvidonoJa-
pãoamaisde4séculosatráschamado Shu-Ha-Ri[17](figura2.2)queconsisteem
trêsníveisdehabilidadequepodemserutilizadoscomoreferênciaparaqualquer
novaprática,habilidadeoucompetênciaaseraprendida,inclusivemétodoságeis.
Ostrêsestágiossão:
Figura2.2:ShuRaHi
1.Shu:Representaoprimeiroestágiodaaprendizagemdeumahabilidade,em
queénecessárioseconstruirabase,afundaçãodoqueseestáaprendendo.
Oaprendizbuscaobservar,copiareimitaroquealguémquejátemexperiência
faz,geralmente,ummestre.Nesteestágioémaiseficienteseguirregrasdoquetentar
improvisaroumodificartécnicas.
Umaequipequeestácomeçandoatrabalharcommétodoságeis,certamente,por
algumtempoestaránesseestágio.Éummomentoimportanteparaseguirasregras
dométodonumaabordagem“by-the-book”,ouseja,semalteraçõesouimprovisos.
SeumaequipeestáutilizandoScrum,nesteestágio,porexemplo,éimportanteque
todosospapéissejamassumidos,equetodasasreuniõessejamrealizadasdeacordo
comas“regras”.Esseéummomentoemquepodeserimportanteprocurarajudade
alguémquetenhaexperiênciacommétodoságeis.
2.Ha:Esseéosegundoestágio,emqueoestudantejácome çaapensarmaispro-
fundamentesobreosporquêsdascoisas,quebraalgumasregras,erompeumpouco
25

## Página 40

2.2. Ordem,CaoseComplexidade CasadoCódigo
comatradição.Agora,jáépossívelrefletirsobreoquefoiaprendidoecompreender
melhorosprincípiosemvezdeapenasrepetirouseguirregras.
Énesseestágioquealgumasadaptaçõesaocontextopodemcome çarsurgir,no-
vaspráticassãoinseridas,e insightsdeexperiênciaspassadasservemcomobasepara
tomadasdedecisão.Agora,mesmoqueascoisasmudemumpoucoemsuaforma
(práticas,papéis,reuniões),aequipeestaráprontaparamanteraessênciadaagili-
dade(entregasfrequentes,respeitoàspessoas,comprometimento,colaboraç ão,co-
municaçãoetc.).
3.Ri:Nesteúltimoestágio,apráticajásetornapartedequemestáaprendendoe,
apesardeaindaseguiralgumasregras(mesmoaquelasqueforamquebrasereinven-
tadas)[4],tudoparecesernatural,eoaprendizadovemdapráticaedaexperiência.
Éimportantenotarqueumaequipepodeestaremestágiosdiferentesdepen-
dendodareferência,porexemplo,umtimepodeestarnoestágio Riemsefalando
deentregasfrequentes,maspodeestarnoestágio Shuemrelaçãoàprogramaçãoem
par.
Umaliçãoimportantedestemodeloéqueháummomentocertodematuridade
parasequebrarasregras,adaptareimprovisar.Umalunoiniciante(noestágio Shu)
deartesmarciaisquetentarmudarosmovimentosensinadospelomestrepoderá
facilmentefazeralgoerradoesemachucar,jáumalunointermediário(noestágio
Ha),provavelmente,estarámaispreparadoparaencontrarseupróprioestilosem
correraltosriscos.
Omesmoocorrecomumaequipequeestáutilizandométodoságeis,senum
momentoprecocetentaradaptarouquebrarasregras,antesdetercompreendido
maisprofundamenteosprincípios,correoriscodeestarfazendoalgumaoutracoisa
qualquereascontinuarchamandodemétodoságeis.
2.2 Ordem,C aos eComplexidade
Assimcomohámuitostonsdecinzaentreopretoeobranco,entreocaos(de-
sordem)eaordem,hátambémalgunsníveis[8]. Quandotentamostrazernossas
organizaçõesparaoextremodaordem,paraquepossamostornarascoisasmais
previsíveisemantertudosobcontrole,criamosumasérieregras,eenrijecemoso
sistema,tornando-opoucoadaptativoeburocrático. Poroutrolado,quandonão
hánenhumaregra,nenhumarestrição,nenhumlíder,osistemaseencontranoque
chamamosdecaossemnenhumaprevisibilidadeevocênãoconsegueteramenor
ideiadoqueestáacontecendoouparaaondeascoisasestãocaminhando.
26

## Página 41

CasadoCódigo Capítulo2. FluênciaÁgil
Parailustraradiferen çaentreaOrdemeoCaos,imaginequevocêestáindo
comsuafamíliapassarofinaldesemananapraia. Vocêtemdoisfilhospequenos
edanados,ummenino,eumamenina.Seucônjugefoifazerumcaminhadaevocê
ficouresponsávelpelascrianças.SevocêoptarpeloCaosextremo,nãodiránadapara
ascriançaseasdeixarácompletamentelivresparafazeremaquiloquequiserem,não
asadvertirá,nãohaverálimites,nemrestrições,nemregras.Liberdadetotal,tudoé
possível!Neméprecisofalarqueaprobabilidadedeumacrian çaseafogareaoutra
entrarnomeiodeumjogodefuteboletomarumaboladaébemalta.
Agora,sevocêoptarpelaordemextrema,diráaseusfilhos:
Sentem-se aqui na minha frente, brinquem de fazer castelo com 500 metros de altura
e duas torres, usem o balde e as pazinhas, não saiam daqui enquanto eu não
autorizar, não chorem, não gritem, não levantem, e (imagine e inclua mais umas 50
regras aqui).
–
Numcontextototalmenteordenado,todasasvariáveisdevemserisoladas,epor
issoépossívelpreveracontecimentos,porém,notequeambososextremossãoexa-
gerados.Noprimeiro,ascrian çasacabamsemachucandoporexcessodeliberdade
enegligência,nosegundoexemplo,ascrian çasmalpodemsedivertirpoispreci-
samseguirordensrestritasenãotêmliberdadealgumaparaseauto-organizarou
expressarsuaindividualidadeecriatividade.
Omeiotermoentreessesextremos,seriadaràscrian çasalgumasrestriçõesbá-
sicasparacertificar-sedequeelaspoderãobrincarsemquenadademalocorraa
elas.Vocêdiriaalgodotipo:-“Criançaspodembrincardoquequiserem,efiquem
ondeeupossavê-los,enãodeixemqueaáguaultrapasseacinturadevocês.”
Agorapenseemumaequipededesenvolvimentodesoftwarequenãopossui
nenhumaregracomumentreosmembrosdaequipe,cadaumescrevecódigoda
maneiraqueachamelhor,unsescrevemtestesoutrosnão,algunsutilizamcertas
convenções,outrosutilizamoutras,cadaumtrabalhaemsualinguagemdeprogra-
maçãopreferida,algunstrabalhamnoescritóriooutrosdecasa,cadaumdefinesua
frequênciadeintegraçãodocódigo.
Dápraimaginarqueessecenárioseriaumbagun ça,nãoé?Poroutroladouma
equipequeestánoextremodaordempossuiregrasparatudo,nãotemnenhuma
liberdadeparaexpressarsuacriatividadeouparasolucionarosproblemas,todosos
horáriosestãodefinidos,astecnologias,aslinguagensdeprogramação,oquesepode
fazer,oquenãosepodefazer.Hápoucaounenhumavariaç ão.
27

## Página 42

2.2. Ordem,CaoseComplexidade CasadoCódigo
Osmétodoságeissãoumarespostaaocaoseàordem,epropõemumcenário
queestájustamentenomeiotermo:acomplexidade[8](vejanafigura 2.3.Muitos
autoreschamamissodea“beiradocaos”.Vocêsóprecisadeumpoucoordempara
queosistemapossaseauto-organizarparaatingirumdeterminadoobjetivo. Não
maisdoqueisso. Eessa“ordem”geralmenteestápresentenosmétodoságeisna
formaderestrições.
Figura2.3:Complexidade
“T oda organização é um sistema complexo adaptativo, é como um jogo em que as
regras são mudadas ao longo do curso, e pelos próprios participantes. ”
–JurgenAppelo
PensenoScrum,comoumexemplo.Aequipeprecisapossuirde5a9membros.
Todososdiasotimedevefazerumareuniãodiáriadeaté15minutos.Todaiteraç ão
temcomoresultadoumpotencialincrementonoprodutoetc.Essasregraserestri-
çõesasseguramqueaequipetrabalheemumestágiointermediárioentreaordeme
ocaos.Tudoaquiloqueficaimplícitoéespaçoparaqueelapossaseauto-organizare
adaptar-separarealizaromelhortrabalhopossívelnocontextoemqueestáinserida.
Emumaabordagemágil,otrabalhodogestornãoécriarregrasnaorganizaç ão,
mascertificar-sedequeaspessoaspodemcriarsuasprópriasregrasjuntas,eéjus-
tamenteesseesfor çoconjuntoquepermitequeosistemaalcance“abeiradocaos”
[8]. Nessavisãoagestãoocupa-seapenascomalgumasrestriçõesdealtonível. O
restopodeserdefinidopelaprópriaequipe,eénessecenárioqueaauto-organizaç ão
acontece,porqueelatemliberdadeparacriarsuasprópriasregrasetomardecisões.
Quandotodasasdecisõesvêmdecimaparabaixo,nãoháauto-organizaç ão.
Auto-organizaçãorequerempoderamento,eempoderamentorequerconfian ça.
Agestãoprecisafazeruminvestimentodeautonomiaparaqueequipepossatomar
decisõeseseorganizardaformamaiseficienteparaatingirosobjetivosdaorgani-
zação.
28

## Página 43

CasadoCódigo Capítulo2. FluênciaÁgil
Outropontoimportante,éque aauto-organizaçãoporsisó,nãoéboa,nem
ruimepodelevaraqualquerresultado.Porissoéessencialqueaequipeseauto-
organizeemtornodeumobjetivo,demetasimportantesparaosucesso.Écomose
agestãoapontasseaondeaorganizaçãoquerchegarequaléadire çãoaseguir,masa
equipetivesseautonomiasuficienteparadecidirqualéamelhorformadesechegar
atélá.
2.3 E agora, o que eu faço amanhã?
Façaumlevantamentodo turnoverdasuaequipe. Quantaspessoasdeixarama
equipenosúltimosseismeses,equantasnovaspessoasforamrecebidas?Reflitaso-
breoimpactodessasmudan çasnaprodutividadedasuaequipe.Vocêsrotacionam
osmembrosdasequipesdetemposemtempos? Issofoibomouruim? Porquê?
Qualtemsidooimpactodessasmudan çasnaperformancedaequipe?
PenseemqualdosestágiosTuckmansuaequipeseencontranoseupontode
vistaemrelaçãoàagilidade. Oquepodeserfeitoparavencerosdesafiosatuaise
seguirparaopróximoestágio?
Conversecomsuaequipesobreosseusobjetivos.Vocêssabemqualéopapelde
vocêsnaorganização?Casoestesobjetivosnãoestejamclaros,procurecompreendê-
los,conversarcomagestão,etorná-losexplícitosparaquetodaaequipesaibapara
ondeestãoindoeaondedevemchegar.
Aequipetemliberdadeparadecidirqualamelhorformadeatingirseusobje-
tivos,ouasdecisõessãoimpostaspelagestão?Discutacomsuaequipesobrecomo
vocêspodemganharmaisconfiançadagestãoparacriarumambientemaisfavorável
àauto-organização.
Pensesobreasquaissãoasregrasdasuaequipe.Sãorealmentenecessárias?Será
quealgumadelasfoiútilnopassadomasagorajáperdeuosentido?
29

## Página 45

Capítulo3
FocoemValorparaoNegócio
Nãoéincomumouvirmoshistóriasdetimesquepassaramanosconstruindoum
produtoqueninguémjamaisusou,ouentãodeequipesquepassarammesesotimi-
zandoumprodutoparaqueeletivessemáximaperfomanceeescalabilidade,cons-
truindosemprecomtecnologiadeponta,masaprimeirafrasedoclienteaovero
produtofuncionandoé“Nãoerabemissoqueestavaquerendo”.
Todoprodutodesoftwarerepresentadealgumaformavalorparaalguémeesse
éoprincipalmotivodaexistênciadosoftware,masapesardepareceralgoóbvio,
muitasvezesoperdemosdevistaeacabamosconstruindoumprodutoquepodeaté
sertecnicamentefantástico,masquenãoagregaovalordequeoclienteprecisa.
Éporissoquemétodostêmfocoemvalordenegócio,eoprimeiroestágioda
fluênciaágildizrespeitoaagregarvalordenegócioaoclienteeamelhoraravisibi-
lidadedotrabalhodaequipe[57].
O objetivo é aprender a deixar de planejar apenas em termos técnicos, e
preocupar-seemplanejarlevandoemcontaovalordenegócioqueosoftwarede-
senvolvidopoderáagregaraocliente,assimcomorefletiredecidirsobrequaisas

## Página 46

CasadoCódigo
melhoresmaneirasdepotencializá-lo.
Paradarsuporteaesseobjetivoasequipeságeisfazemusodeferramentascomo
backlogs,iteraçõesequadroskanban.
Osprincipaisbenefíciosalcan çadosnesteestágiosão:atransparência,queper-
mitequeoprogresso(ouafaltadeprogresso)dotimesejafacilmentevisualizado
portodos,inclusivepelagestão,amelhoriacontínuaparaseagregaracadaitera-
çãomaisemaisvalor,eummelhoralinhamentoqueresultaráemumaequipemais
colaborativa,commenosmausentendidosemenosatrasosdesnecessários.
Éomomentoemqueaequipedeveráganharmaturidadepararesponsabilizar-se
peloresultadodotrabalho,nãoapenasemtermostécnicos,mastambémemtermos
dovalordenegócioagregado,emaisdoqueisso,devemresponsabilizar-sepelo
resultadodotimeenãoapenasporsuascontribuiçõesindividuais.
Éclaroqueparaqueaequipetenhaessavisãodevaloremtermosdenegócioé
essencialapresen çadealguémcomumperfildenegóciospróximoparaajudá-losa
compreenderoquedefatoédevaloreoquenãoé.
Quantomaiscedoforpossívelagregarvaloraocliente,melhorseráoresultado.
Quandooclienterecebeosoftwarefuncionandoemumcurtosintervalosdetempo,
alémdeganharvantagemcompetitiva,otrabalhoemprogressotambémdiminui
(WIP).Consequentemente,aquantidadedetrabalhoparcialmenteprontodiminuirá
odesperdício,conformeabordadoanteriormente.
ADellComputadores,porexemplo,nãoacumulaestoqueseentregapedidos
personalizadosemmenosdeumasemanae,exatamentepornãopossuirestoques
acumulados,podeofereceraseusclientesnovosprodutosantesdeseusconcorrentes,
semterquesepreocuparemqueimarestoquesdeprodutosantigos.
AssimcomoafazaDell,umaequipedesoftwarequeentregarapidamenteeman-
témumbaixoníveldetrabalhoparcialmenteprontopoderesponderrapidamentea
novasnecessidadesquevenhamasurgirsemsepreocuparemdeixarotrabalhoque
jáfoicomeçadoparatrás.
Asorganizaçõesqueentregamrapidamenteestruturam-sedeformaqueaspes-
soassaibamcomootrabalhodeveserfeitosemquealguémprecisedizeraelaso
quefazer[48].Essaspessoasdevemsercapazesderesolverproblemasefazeradap-
taçõespararesponderamudanças.Essasdiretrizessãoprofundamenteaplicadasna
Toyota.
Entregarrapidamenteécomplementaraoprincípiodetomardecisõesnoúl-
timomomentopossível.Porexemplo:seoclienterecebeentregasdesoftwaretoda
semana,nãoprecisadecidirsobreoqueseráfeitodaquianovemeses.Entretanto,
32

## Página 47

CasadoCódigo Capítulo3. FocoemValorparaoNegócio
seoclienterecebesoftwaresomenteacadatrêsmeses,entãoprecisarádecidirsobre
asnovasfuncionalidadesnomínimotrêsmesesantesdepodervê-lasemfunciona-
mento.
Nessecapítuloabordaremoscomoequipespodemaplicarpráticaságeisparaga-
rantirqueoclienterecebavalordenegóciocomfrequênciaatravésdaentregaitera-
tivadesoftwareemfuncionamento.
3.1 Disseminando a Visão do Projeto
Projetossemprenascemdeideiasdepessoas.Ideiasque,geralmente,nascemdeten-
tativasdetornarumdeterminadoprocessomaiseficiente.Seusdonossãochamados
devisionários,porqueelespossuemavisãodoprojetoe,entendemanecessidadee
conhecemoproblemaqueosoftwaredeveresolver.Avisãorevelaparaondeopro-
jetoestáindoeporqueeleestáindoparalá.
Todoprojetopossuiumoumaisvisionários,alguémqueconseguiuenxergar
umanecessidadeeteveumaideiadesoluç ãoparasupriressanecessidade. Ainda
queumprojetopossuamuitosvisionários,énecessárioquealguémtomearesponsa-
bilidadedepromoverecomunicaressavisãoàequipededesenvolvimentoeatodos
osoutrosinteressadosnoprojeto.
Essepapel,geralmente,éderesponsabilidadedogerentedeprojetos,dopróprio
cliente,oudealguémquerepresenteocliente. NométodoScrum,porexemplo,a
visãodoprojetoéresponsabilidadedo Product Owner.
Émuitoimportantequeovisionárioestejabempróximoàequipededesenvol-
vimentoparaesclarecerasfrequentesdúvidasquesurgemaolongodoprojeto.Por
isso,umdosprincípiosdométodoXPétero ClientePresente.Umavezquetodos
foremcontagiadoscomavisãodoprojeto,aschancesdesucessosetornammuito
maiores.
Hátrêsperguntasessenciaisqueovisionárioprecisacomunicaràequipe:
1) Queobjetivooprojetodeveatingir?
2) Porqueesseprojetoagregarávalor?
3) Comomedirseoprojetofoibemsucedido?
Paraqueaequipepossadesenvolverumsoftwarealinhadocomavisãodopro-
jeto,énecessárioqueavisãoestejasempreacessívelparatodos,porissoaimportân-
ciadovisionárioestarpresentenaequipe.
33

## Página 48

3.1. DisseminandoaVisãodoProjeto CasadoCódigo
Muitasequipesmantêmumabrevedescriçãodavisão,comoporexemplo,ares-
postadastrêsperguntasacima,emumwikiouportalinterno,ouatémesmoim-
pressoeanexadoaoquadrodaequipe. Oimportanteéqueestejaaoalcancede
todos.
Osvisionáriosdevemestarpresentesnosmomentosdetomadadedecisão,nas
reuniõesdeplanejamento,nasapresentaçõesdedemonstraçãodasiteraçõesoureu-
niõesderevisão. Seissonãoacontecer,provavelmenteaequipenãoentenderáo
propósitodoprodutoqueestãodesenvolvendo. Poderíamoscompararissoaum
médicoquefazumacirurgia,quenãosabedequemalestátentandolivraropaci-
ente.
Equipesdedesenvolvimentodesoftwaretomammilharesdepequenasdecisões
todososdias,esemumaboavisãogeralecontextodoqueestásendoconstruído,é
muitodifíciltomarbosasdecisões.
Comograndepartedasequipeságeisadotamumúnicorepresentantedavisão
doproduto,deagoraemdiante,ovisionárioseráreferidocomo Product Ownerou
PO.
Será que todos estão na mesma página?
MarcBenioff,CEOdaSalesforce.com,contaqueumcertodiaesta-
vamnoelevadorumtestador,umengenheiro,eumdesenvolvedordesua
empresa.Derepentealguémdeoutroconjuntoentrounoelevadoreper-
guntouaeles“oqueexatamenteaSalesforce.comfaz?”.Paraasurpresa
doCEO,cadaumdeuumarespostadiferente[5].
Depoisdesteevento,Beniofftomouumasériedeprovidênciaspara
garantirquetodos“estivessemnamesmapágina”edepoisdealgum
tempoinvestindoemdisseminaressavisão,alémdetodosganharem
maisassertividadeeconhecimentodoqueestavamfazendo,todosos
membrosdaequipedetornaram“potenciaismarqueteirosevendedo-
res”doproduto.
Quandooprojetopossuiumavisãoúnicaecoesa,atomadadedecisãosetorna
muitomaisfácil,etodososmembrosdaequipe,depossedavisão,podempartici-
parmaisativamente,oferecersugestões,erealizarumtrabalhomaisprodutivoede
melhorqualidade.
34

## Página 49

CasadoCódigo Capítulo3. FocoemValorparaoNegócio
ODiscursodoElevador
Imaginequevocêentrounoelevador,eencontra,ninguémmenosdoqueaquele
investidorquevocêsempresonhouquepudesseseinteressaremseuproduto.Você
tempoucossegundosatéqueoelevadorodeixeemseuandar,eprecisaaproveitar
aoportunidadeparafalarsobreoquevocêesuaequipeestãofazendo.Oquevocê
diráaele?
Aideiapordetrásdodiscursodoelevadoréencontrarumaformadetransmitira
essênciadeumaideiaemumespaçomuitocurtodetempo[49].Fazeresseexercício
oajudaráatrazermaisclarezaeobjetidadeparasuavisãoeseráútilparapensarno
produtosobreopontodevistadoclienteedequeformaoprodutoagregarávalora
ele.
AHarvardBusinessSchoolcriouum websitequeajudaacriaroDiscursodo
Elevadorparaseuproduto,alémdefazerumaanálisecomsugestõesparaquevocê
possamelhorarseusdiscurso[54].DeacordocomaHBSseudiscursodevecontem-
plarosseguintesitens:
1) Quem:Oquevocêmaisquerqueseuouvinteselembrearespeitodesuaorgani-
zaçãoouproduto?
2) Oquê:Dequeformaseuprodutoagregarávaloretraráresultadosouimpactará
onegóciodeseuouvinte?
3) Porquê:Quaissãoosbenefíciosexclusivos,osdiferenciaisqueseuprodutoofe-
rece?
4) Objetivo:Oquevocêesperaqueoouvintefaça?
Criarumdiscursodoelevadorparaseuprodutopodeserumaformadivertida
erápidadedesenvolverummensagemrápida,objetivaeconvincentedeapresentar
seuprodutoparaosmembrosdaequipeeparapotenciaisclientes.
3.2 Planejamento e Desenvolvimento Iterativo
Oplanejamentopermiteentenderaexpectativadoclienteemrelaç ãoaoprojetoe
traçarestratégiasparaatendê-las.Éomomentodeentenderasideiasenecessidades
doclienteedescobrirasfuncionalidadesqueosoftwareprecisaráoferecer.
35

## Página 50

3.2. PlanejamentoeDesenvolvimentoIterativo CasadoCódigo
Nodesenvolvimentoágildesoftwareotimeinteiroestáenvolvidoemdefinir
requisitos,otimizá-los,implementá-los,testá-los,integrá-los,eentregá-losaoscli-
entes[37]. Alémdisso,emumambienteágil,planejaréumaatividadeconstante.
Dessaforma,épossívelresponderrapidamenteàsmudan çaserealizarasadapta-
çõesqueforemnecessáriasparaqueosoftwaresejaentreguecomomáximograude
qualidadeeeficiência.
Nosmétodoságeisosprojetossãodivididosemiteraçõescurtasquegeralmente
têmumaoualgumaspoucassemanasdeduração.Acadaiteraçãoérealizadauma
reuniãodeplanejamentoparadefiniroqueseráfeitoduranteaiteraç ão.Oseuob-
jetivoéidentificarjuntoaoclienteoquepoderáagregarmaisvaloraonegócio.
OprocessodeplanejamentonométodoXPéchamadode“JogodoPlaneja-
mento”,noScrumsimplesmentedePlanejamento. Oobjetivodojogodoplaneja-
mentoégarantirqueomáximodevalorpossívelserágeradonodiaadiadetrabalho
atravésdacriatividadeedashabilidadesdaequipe.
Oplanejamentodaiteraçãoaconteceemumareuniãonoiníciodecadaiteraç ão.
Éimportantequenestareuniãoestejampresentesaequipededesenvolvimentoeo
cliente. Assume-sequeoclientetemtodaainformaç ãonecessárianoquedizres-
peitoaoqueagregavaloraosoftware,equeaequipededesenvolvimentotemtoda
ainformaçãonecessáriaemrelaçãoaquantocustaparaagregartalvalor.
Agrandesacadaéminimizaroscustosemaximizarovaloragregado. Atra-
vésdaestimativa,osdesenvolvedorespodemdizerquantocusta,emoutraspala-
vras,quantotempolevaparadesenvolverdeterminadafuncionalidade;eatravésda
priorização,oclientepodedefinirquantovalorumahistóriapodeagregar,ouseja,
quaisfuncionalidadespodemtrazermaisbenefícios. Temosentãoumarelaç ãode
custo/benefício.
Atravésdessacolaboraçãoentreaequipededesenvolvimentoeoclienteépos-
síveltraçarumplanoparaatingirsucessonoprojeto. Ojogodoplanejamentoé
divididoemduasfases:oplanejamentode releaseseoplanejamentodeiterações.
Umdosprincipaisbenefíciosdoplanejamentoiterativoéaeliminaç ãododes-
perdíciodeumalongaanáliseprematura,queéconsideradoumdosmaioresdes-
perdíciosnodesenvolvimentodesoftware[49].Écomumemprojetoswaterfallque
aanálisedetodososrequisitossejafeitadeantemão,deformaquenomomento
dodesenvolvimentoosrequisitosjámudaramedamaneiraqueforamanalisadosjá
nãopodemmaisagregarvaloraocliente.Essapráticadelevantamentoprematuro
derequisitoséconhecidacomo Big Requirements Up Front(BRUP).
36

## Página 51

CasadoCódigo Capítulo3. FocoemValorparaoNegócio
BacklogsDEEP
Paraajudar Product Ownersanãocaíremnoerrodolevantamento
prematuroderequisitos,MikeCohn,criouoacrônimoDEEP[20]que
representa4qualidadesdeumbom backlog:
1) D-DetalhadoApropriadamente:Ositensdemaiorprioridadedevem
sermaisdetalhadoseositensdemenorprioridadenãoprecisamde
muitosdetalhes.
2) E-Estimado:SetodosositensdoBacklogestiveremestimadospela
equipe,oPOterámaisfacilidadeempriorizaro backlogeterámelhor
previsibilidadedoprojeto.
3) E-Emergente:O Product Backlogéumartefatovivo,istoé,devemu-
darfrequentementedeacordocomasmudan çasdenegócio.Novos
itenssãoincluídos,itensantigossãoremovidosoumodificados.
4) P-Priorizado:Ositensdo backlogdevemestarpriorizadosdomaior
valordenegócioparaomenorvalordenegócioparaqueositensmais
importantessejamdetalhadoseimplementadosantesdosmenosim-
portantes.
Alémdisso,emabordagenstradicionais,eramuitocomumqueosrequisitosfos-
semtransmitidosaodesenvolverapenasporescritoatravésdeumdocumento.Em
contrapartida,aessênciadacomunicaçãonosmétodoságeiséa comunicaçãoface
aface.
DeacordocomAlistairCockburn,acomunicaçãoatravésdepapeléfriaepobre,
porquenãoháoportunidadeparaperguntaserespostas,acomunicaç ãoentrepes-
soasfaceafaceéquenteemuitomaisricaporqueofereceaoportunidadedeiteraç ão
entreaspartes[17].
Éclaroqueissonãotorna,deformaalguma,acomunicaç ãoescritairrelevante,
pelocontrário,elatambéméimportante,masnãoésuficiente,enemmaiseficiente
emtodososcenários.
Éporissoquemuitosmétodoságeisdefendemaideiadeumareuniãodepla-
nejamentoemqueaequipeeo Product Ownerparticipemjuntos,eque,atravésde
37

## Página 52

3.3. PlanejandoumaIteração CasadoCódigo
umaconversa,criemhistóriasdeusuárioquerepresentamasfuncionalidadesase-
remimplementadasnosoftware.
Aodecorrerdestecapítulo,oconceitodehistóriasdeusuárioserámaisampla-
menteexplorado,mas,antesdisso,explicaremosumpoucomaisoquesefazemum
planejamentodeiteração.
3.3 Planejando uma Iteração
Oplanejamentodeiteraçõespermiteestruturarasatividadesdodiaadiadaequipe.
Um releasepodeconterváriasiterações(figura 3.1),deformaqueashistóriasque
precisamserentreguesno releasesãoincluídasemumaoumaisiterações.Durante
aiteraçãoashistóriassãodesenvolvidasenofinalsetemumsoftwaredesenvolvido
etestadoe,aoterminarumaiteraç ão,umanovaiteraçãoéiniciada.
Figura3.1:ReleaseseIterações
Asiteraçõesgeralmentetêmperiodicidadesemanal,porém,tantootempodas
iteraçõescomodos releasespodemserdefinidosdeacordocomanecessidadede
cadaorganização.Otamanhoidealparaumaiteraç ãoéomenortempopossívelque
sejanecessárioparaqueaequipeconsigaentregaralgodevalorcomqualidadepara
ocliente.
Aoplanejarumanovaiteração,éimportanteteremmãosoresultadodaiteraç ão
passada,istoé,asomadasestimativasdashistóriasqueforamdesenvolvidas.Esseé
onúmerodepontosdeestimativaquesepodeesperarparaapróximaiteraç ão.Essa
somadepontoséconhecidacomovelocidadedaequipe.Háquemutilizeumamédia
dasvelocidadesdasiteraçõespassadasparadefinirquantospontosdecomplexidade
serãoinseridosnanovaiteraç ãoeháquemprefirautilizarapenasavelocidadeda
últimaiteração.
Parainserirashistóriasnaiteraçãoéprecisoqueelasestejamestimadasemcom-
plexidadeepriorizadassegundoovalordenegócio,oqueprovavelmentejáterásido
38

## Página 53

CasadoCódigo Capítulo3. FocoemValorparaoNegócio
feitonoplanejamentode release.Dessaforma,selecionarashistóriasparaaiteraç ão,
geralmente,éalgorápido.Oclienteverificahistóriaporhistória,easincluinanova
iteraçãodeacordocomaprioridade. Asomatóriadepontosdashistóriasselecio-
nadas,idealmente,nãodevesermaiordoqueadefinida,sejacombasenaiteraç ão
passadaounamédiadasanteriores.
Depoisdeselecionadasquaishistóriasserãoimplementadasnanovaiteraç ão,é
precisoexplicá-lasàequipe.NessemomentoéimportantequeoPOoupessoasde
negóciopossaestarpresentesparaquepossamesclareceraosdesenvolvedoressuas
dúvidasdenegócio,permitindoqueaofinaldareuniãoosdesenvolvedoresestejam
preparadosparaimplementarestashistórias.
Seaequipeconseguirentregartodasashistóriasantesdofimdaiteraç ão,épre-
cisosolicitaraoclientemaishistórias. Então,oclienteescolhequaisdeverãoser
adicionadasàiteraçãoconsiderandootemporestanteesuaprioridade.Napróxima
iteraçãooclientepoderáincluirumnúmeromaiordepontos,considerandoquea
velocidadedaequipemelhorou.Issogeralmenteaconteceàmedidaqueaequipevai
amadurecendoeganhandomaisdomíniosobreatecnologiautilizadanoprojetoe
nosconceitosdenegócio.
Umproblemamuitocomumquepodeafetaraordemdedesenvolvimentodas
históriassãoasdependênciastécnicasentreelas.Épossívelqueoclientedetermine
queumahistóriaespecíficatenhaprioridadeemrelaç ãoàoutra,porém,tecnica-
mentepodesermaisviávelfazerocontrário.Nessescasoséimportantequeaequipe
sejasinceracomoclienteemrelaçãoàsdificuldadestécnicaseapresenteaeleosbe-
nefíciosdeimplementarashistóriasnaordeminversa. Entretanto,ésemprereco-
mendadoqueaequipepermitaqueoclienteescolhaoqueelequerquesejaentregue
primeiroeseesforceaomáximoparaentregardeacordocomaprioridadedetermi-
nadaporele.
EmsefalandodeXPeScrum,nãoérecomendadoadicionarnovashistóriasa
umaiteraçãoquejátenhasidoiniciada.Écomumqueaolongodeumaiteraç ãoocli-
entesolicitequealgumanovahistóriasejaadicionadacomurgência.Atenderaeste
tipodesolicitaçãoemergenteenãoplanejadapodeimpactarnegativamentenoanda-
mentodotrabalhodaequipee,comomencionadoanteriormente,pelamesmarazão,
nãoérecomendadoalterarashistóriasdeumaiteraç ãoemandamento.Sehouver
muitoscasosdemudan çasdeescopodentrodeumaiteraç ão,eisso,realmente,for
importanteparaonegócio,talvezsejaocasodeavaliarutilizarummétodoágilde
fluxocontínuoaoinvésdeiterativo,comoKanban,porexemplo.
Alterarumaiteraçãoemandamentopodesignificartrabalhoperdido,desgaste,
39

## Página 54

3.4. AReuniãoDiária CasadoCódigo
perdadaconcentraçãoeatrasos. Noentanto,responderrapidamenteàsnecessi-
dadesdenegóciodoclienteéumvalorágilealgoquedevesersemprelevadoem
consideração.
Emcasoscomoeste,épossívelnegociarcomocliente,edepoisdeconscientizá-
lodaproblemáticadealterariteraçõesemandamento,incluirahistóriaemergente
comacondiçãoderetirardaiteraçãooutrahistóriacomumvalordeestimativade
esforçoigualoupróximo.Deve-seevitar,éclaro,retirarhistóriasquejátenhamseu
desenvolvimentoiniciado.
Ocliente,provavelmente,ficarácontenteporsuasolicitaçãoemergentetersido
atendidaemaisvalortersidoagregadoaoseunegócio.Porém,éprecisotercuidado
paraqueessasemergênciasnãosetornemalgoconstanteeprejudicial.Solicitações
emergentesdevemseresporádicas.Éprecisoinsistirparaqueoclientetenhadisci-
plinaerespeiteasiteraçõesparaqueascoisaspossamcaminharconformeoplane-
jamento.
Outrostiposdedemandasnãoplanejadaspodemsurgiraolongodaiteraç ão.
Umexemplomuitocomumsãoosindesejáveisdefeitos.Pormaioresquesejamas
atitudespreventivasdaequipeparamanteraqualidadedosoftwarecomtestesein-
tegraçãocontínua,écomumquedefeitosseapresentemaquiouali. Nessescasos
podesernecessárioqueaequipepareotrabalhoetomeprovidênciasparasanaro
problema.
Alógicaésimples: seumadeterminadafuncionalidadejáestáemproduç ão,
significaqueelaeramaisimportantedoqueasoutrasqueficarampendentes,por
issofoipriorizadaedesenvolvidaantesdasoutras. Casoumdefeitosurjaeeessa
paredefuncionar,provavelmente,serámaisimportantecorrigirodefeito,doque
entregaralgoquetinhamenosprioridade.
Valeapenaacompanharasdemandasdetrabalhonãoplanejadoquesurgem
duranteumaiteração.Seformuitofrequentesfiqueatento:algoprovavelmenteestá
erradooutalvezsejamaisinteressanteavaliartrabalharcomfluxocontínuoemvez
deiterações.
3.4 AR eunião Diária
Estabelecerumacomunicaçãoeficienteentreosmembrosdaequipeéextremamente
importante.Asreuniõesdiárias,conhecidasnoXPcomo“Stand Up Mettings”(Reu-
niõesemPé)enoScrumcomo Daily Scrum(ScrumDiário)sãopráticasmuitoefi-
cazesparaquetodosestejamsempreapardo statusatualdoprojeto.
40

## Página 55

CasadoCódigo Capítulo3. FocoemValorparaoNegócio
Todososdiasemumhoráriopreestabelecido,geralmentenoiníciododia,a
equipesereúnepormaisoumenos15minutosparasincronizaroestadodoprojeto
emantertodosinformadossobreosúltimosacontecimentosecomoascoisasestão
ounãoevoluindo.
Atravésdareuniãodiáriatodososmembrosdaequipeficamcientesdoanda-
mentodoprojetoepodemaproveitaraoportunidadeparaapresentarsuasdificul-
dadesepedirajudaaosoutrosmembros.
NoScrum,porexemplo,cadamembrodotimerespondeatrêsperguntasna
reuniãodiária:
1) Oqueeufizdesdeaúltimareunião(ontem)?
2) Oquefareiatéapróximareunião(atéamanhã)?
3) Queproblemasestãomeimpedindodeprogredir?
TimOttinger,sugereoutras4perguntasquetêmumfocomaiorementrega,
aprendizagemecolaboração[44]:
• Quehistóriasvocêajudouaterminardesdeaúltimareuniãodiária?
• Quehistóriavocêajudaráaterminarhoje?
• Comoorestodotimepodeaajudaraempurrarumahistóriapara“pronto”.
• Oquevocêaprendeudenovo?
Umfatorimportantequedeveserconsideradoparaumaboacomunicaç ãoéo
númerodeintegrantesdaequipe:quantomaispessoas,maisdifícilsetornaaco-
municação. Porisso,equipeságeisgeralmentesãocompostasporumnúmerode
membrosquevariadecincoanovepessoas.Nocapítulo 6abordaremoscommais
profundidadealgumasboaspráticasparaformaçãodeequipes.
Éimportantequetodostenhamoportunidadedefalarnareuniãodiária,nos
primeirosdiaséimportantequealguématuecomofacilitador(geralmentealguém
compapeldescrummaster)paraassegurarqueninguémdomineareuniãoefale
sozinhoduranteos15minutos,ouquealguémdeixedefalar.
Paracriaressadisciplina,algumasequipesutilizamalarmesquetocamde2em2
minutos,porexemplo,paraevitarquealguémfaledemais.Outraspassamumbola
demãoemmãoatéquetodosabolavolteapessoaquefalouprimeironareunião.Ao
41

## Página 56

3.4. AReuniãoDiária CasadoCódigo
passoqueaequipecompreendeosbenefíciosdeumaboareuniãodiária,essetipo
deferramenta,geralmente,torna-sedesnecessária,maspodeserútilparacome çar.
KenSchwaber,ressaltaqueéimportantequeareuniãodiáriasejarealizadaem
umlocalconhecidoportodos[55],equesedeveevitarentraremdiscussõesque
fujamdocontextodastrêsperguntasprincipaiscomo,porexemplo,discutirsobre
problemas,abordagensdedesign,asnotíciasdojornaldodiaetc.Seumproblema
querequerdiscussãoforidentificado,senecessário,deve-semarcarcomosinteres-
sadosumareuniãoparasediscutirapósareuniãodiáriaouemoutromomento.
42

## Página 57

CasadoCódigo Capítulo3. FocoemValorparaoNegócio
Porcos eGalinhas
Figura3.2:PorcoseGalinhas
AgalinhadizparaoPorco:
-EiPorco,euestavapensando...Nósdeveríamosabrirumrestaurante
juntos.
Oporcoresponde:
-Nãoseinão...Qualseriaonome?
Agalinharesponde:
-Quetal“OvoscomBacon"?
Oporcoresponde:
-Nãoobrigado.Euestariacomprometido,evocêestariaapenasen-
volvida.
NoScrumtodosasatividadesdegestãodoprojetosãodividasentre
ospapéisdeScrumMaster, Product OwnereTime,essassãoaspessoas
comprometidascomooprojeto.OScrumdefendequeaquelesqueestão
comprometidosdevemterautonomiaparafazeroqueforprecisoparao
sucessodoprojeto,equeaquelesqueestãoapenasenvolvidosnãofaç am
intervençõesdesnecessárias.
Nareuniãodiária,porexemplo,noScrum,asgalinhasnãopodem
falar,fazerobservações,fazercaretasouintervir,sequiseremparticipar
devemficarnaperiferiaapenascomouvintes. Issopermitequeotime
fiquefocadonoqueéimportantesemexplicaçõesoudebatesdesneces-
sários.
43

## Página 58

3.5. LimitandooTrabalhoemProgresso CasadoCódigo
3.5 Limitando o Trabalho em Progresso
“Pare de começar e comece a T erminar”
–SterlingMortensen
Discutimosanteriormentequeestoqueemdesenvolvimentodesoftware,ére-
presentadoportrabalhoquefoicome çado,porémaindanãofoiterminadoe,de
acordocomopensamentolean,issoédesperdício,edevesereliminado.
Existeumarelaçãoentreotrabalhoemprogresso(WIP)eo lead time. Éuma
relaçãolinearproporcional,issoquerdizerqueo lead timecresceàmedidaqueotra-
balhoemprogressocresce,ediminuiamediaqueotrabalhoemprogressodiminui.
Essarelaçãoéconhecidanaindustriacomo“aleidelittle”[50].
Definimosolimitedotrabalhoemprogressonoquadroadicionandolimitesex-
plícitosquedefinemquantositenspodemestaremprogressoemcadaestadodo
fluxodetrabalho,ouseja,cadacolunadoquadro.Vejanafigura 3.3:
Figura3.3:QuadrocomWIP
Reduzirotrabalhoemprogresso,reduztambémo leadtime,permitindoquese
entreguecommaisfrequência.Paraissoéimportantedefinirseseráounãopermi-
tidoquecadamembrotrabalheemmaisdeumatarefaaomesmotempo.
Trabalharparalelamenteemduastarefaspodelevaraproblemascomointerrup-
ções,faltadefoco,desperdíciodetemponamudan çadecontexto,ouatémesmona
mudançadeambientededesenvolvimento,coisasquelevamàperdadeprodutivi-
dade.Experimentosempíricosdevemserfeitosemcadaequipeparaverificaroque
funcionamelhor.
44

## Página 59

CasadoCódigo Capítulo3. FocoemValorparaoNegócio
Oslimitespodemserdefinidosinicialmentecomumpoucomaisdoqueaquan-
tidadedepessoasquetrabalhanaquelaetapadoprocesso.Numaequipecomdois
testadores,porexemplo,poder-se-iainiciarcomumlimitede3,efazerexperimentos
aolongodotempoparasechegarnolimiteideal.
Noquadrodafigura3.3,olimitedodesenvolvimentoestáestourado,eosdesen-
volvedoresnãopodempuxarmaishistórias,nemostestadoresqueestãonolimite.
Nessasituaçãoaequipetodaprecisafocarementregarashistóriasqueestãomais
próximasdofinaldoprocessoantesdepodercome çaratrabalharemnovashistó-
rias.
Semlimitedetrabalhoemprogresso,maistrabalhoseriacome çado,epoderia-
secorreroriscodenadatade releaseaequipenãoterterminadoaindaumasérie
dehistóriasedefeitosquemesmoestandoemandamentonãoestariamprontospara
serementreguesaocliente.
Quandoumahistóriaficarprontanoestágioemqueseencontrae,esperando
paraserpuxadaparaopróximoestágio,estáemumafila. Asfilasdevemsertão
pequenasquantopossível.Recomenda-seconsideraracriaçãodepequenasfilaspara
queabsorvamavariaçãodoprocessoepermitamquefluxonãosejainterrompido.
Muitosprocessos,senãopossuíremfilas,poderãofazercomqueaspessoasfi-
quemdesocupadas,gerandotempoocioso,devidoavariaçõesnotempoquecada
itemlevaparaficarpronto.Novamente,éimportanteobservarseuprocessoe,em-
piricamente,optarpelasoluçãoquepermitirmelhorfluidez.
3.6 Escrevendo Histórias deUsuário
Históriasdeusuáriosãodescriçõessimplesecurtasdefuncionalidadesquedeverão
serimplementadasnosoftware.AsHistóriassão,geralmente,escritaspelopróprio
Product Owner,comsuasprópriaspalavrase,então,sãoregistradasemcartõesque
posteriormentesãoanexadasaoquadrodaequipe.
Ashistóriascontêmapenasumabrevedescriç ãoquerepresentaumanecessi-
dadedocliente,porém,apesardasimplicidadedahistória,oclientedevepossuir
oconhecimentonecessárioparadisponibilizarinformaçõesdenegócioparaquea
equipepossatransformarsuanecessidadeemsoftware.Porexemplo,imagineuma
históriacujafuncionalidadesejadesenvolverumrelatóriodebalan çocontábil;será
necessárioqueoclientepossuaoconhecimentodenegócionecessário,issoé,saiba
oqueéumbalan çocontábilequaissãosuascaracterísticas,paraqueassimpossa
explicaràequipeoqueexatamentedevemdesenvolver.
45

## Página 60

3.6. EscrevendoHistóriasdeUsuário CasadoCódigo
Todahistóriadeusuáriodevepossuirumcritériodeaceitaç ão,tambémdefi-
nidopelocliente,quepermiteàequipeidentificarquandoelaestáimplementada
porcompletoecomsucesso.Aoescreverumahistóriaoclienteassumeresponsabi-
lidadesobreela.
Ashistóriasdeusuáriotêmcaráterdenegócio,porisso,“instalaroservidorde
integraçãocontínua”ou“atualizaraversãodabibliotecadeinjeçãodedependências”,
geralmente,nãosãoexemplosválidos.Podematéserexemplosdetarefas,masnão
dehistóriasdeusuários.Veremosadiferen çaentrehistóriasetarefasmaisadiante.
Algunsexemplosdehistóriadeusuáriosválidasemumprojetodedesenvolvi-
mentodeumsitederelacionamentospodemser:
• Umusuáriopodepublicarsuasfotosemseuperfil;
• Usuáriospodemcriareparticipardecomunidades;
• Comunidadesdevempossuirmoderadores.
MikeCohnpropôsumformatointeressantequeéamplamenteconhecidoeuti-
lizadonomercado:
“Eu,comoum(papel)quero(funcionalidade)paraque(valordenegócio).”
Seaplicarmosomodelopropostonashistóriascitadasanteriormente,elasfica-
riamdaseguinteforma:
• Eucomoumforistaqueropublicarminhafotoemmeuperfilparaqueos
outrosparticipantespossammeidentificarmaisfacilmente.
• Eucomoumusuáriogostariadecriarumacomunidadeparaqueeupossa
reunirpessoascominteressessemelhantesaosmeus.
• Eucomoummoderadorgostariaaprovarourejeitarrespostasatópicosdo
forumparaevitarpostagensinadequadas.
InvestindoemBoasHistórias
SegundoMikeCohn,autordolivro:“UserStoriesApplied”,boashistóriasdevem
conterasseiscaracterísticasseguintes:
1.Históriasdevemserindependentesparaevitarproblemasdeplanejamentoe
estimativa.Seduashistóriaspossuíremdependênciaentreelas,eumativerpriori-
dadealtaeaoutrabaixa,provavelmenteahistóriadependentedeprioridadebaixa
46

## Página 61

CasadoCódigo Capítulo3. FocoemValorparaoNegócio
precisaráserdesenvolvidaantesdasoutrastarefas,assimquechegarahoradahis-
tóriadeprioridadealtaserdesenvolvida. Nessescasos,podeserinteressanteunir
ambasemumaúnicahistória;
2.Históriasdevemsernegociáveis,nãodevemservistascomorequisitosquede-
verãoserimplementadosaqualquerpre ço.Lembre-se,históriassãoapenascurtas
descriçõesdefuncionalidadesquedeverãoseranalisadasediscutidascomocliente
nomomentoemquesuaprioridadeforatingida,ouseja,nomomentoemqueahis-
tóriafizerpartedeumaiteraç ão.Éimportantequeahistóriasejadetalhadaapenas
quandoomomentodeseudesenvolvimentoestiverpróximo,istoé,quandochegar
omomentodeahistóriaentrarnaiteraç ãocorrente.Quantomaiscedoelaforana-
lisadaedetalhada,maioresserãoaschancesdehaverretrabalhoeatémesmoperda
detempoeenergia,considerandoqueoclienteaprendeemudadeideiaàmedida
queasiteraçõesvãosendoconcluídas.
Parailustrarmelhoresteexemplo,imagineumahistóriaquetenhacomoobje-
tivoacriaçãodeumrelatóriodeapuraç ãodeimpostos.Imagineque,segundosua
prioridade,elaseráimplementadasomentedaquiaseismeses,masqueaindaas-
sim,inicia-seumtrabalhodeanáliseediscussãosobreela. Seogovernorealizar
algumamudançanoplanotributário,vocêprovavelmenteterádesperdiçadotempo
edinheiro!
3.Históriasdevemagregarvaloraosclientes.Comomencionadoanteriormente,
históriasdevemdescreverfuncionalidadesquedealgumaformaoferecerãoaocli-
enteretornoaoseuinvestimento. Poressarazão,históriasdecarátertécniconão
sãoaconselháveis,porexemplo,“atualizaroSpringFrameworkparaversão2.5”não
agregavalordenegócioaosoftware,pelomenosnãodiretamente,issonãosignifica
quevocênãopossafazê-lo,maséaconselhávelqueexistaumahistóriaescritapelo
clientequeajustifique;
4.Históriasdevemserestimáveis.Éimportantequeosdesenvolvedoressejam
capazesdeestimá-las. Paraquesejamestimáveisénecessárioqueosdesenvolve-
dorespossuamoutenhamacessoatravésdoclienteaoconhecimentodenegócio,
epossuamtambémoconhecimentotécniconecessárioparatransformarahistória
emsoftware.Seriainviávelpediraumdesenvolvedorquenuncaescreveuumalinha
decódigoemJavaqueestimeoesfor çoparadesenvolverumpedidodevendaem
umprojetoJavaEEcomEJB3.Omesmoaconteceriasepedíssemosaodesenvolve-
dorparaqueestimasseoesfor çoparacriarumrelatóriodefluxodecaixa,semantes
explicaraeleoqueéumfluxodecaixa;
5. Históriasdevemserpequenas. Históriasmuitograndessãodifíceisdeesti-
47

## Página 62

3.6. EscrevendoHistóriasdeUsuário CasadoCódigo
mar,porissodeve-setomarosdevidoscuidadosparamantê-lassemprecurtase,
quandonecessário,quebrá-lasemhistóriasmenores.Parailustrarmelhor,imagine
aseguintehistória: “Umusuáriopoderealizarcomprasnalojavirtual”. Elapode
envolvermuitasfuncionalidadesqueestãoimplícitas,eporisso,podegerardiferen-
tesinterpretaçõeselevarosdesenvolvedoresaoerro.Emcasoscomoeste,podemos
quebrarahistóriagrandeemoutrashistóriasmenores:“Umusuáriopodeadicionar
produtosaoseucarrinhodecompras”,“Aofinalizaracompraousuáriodeveesco-
lheraformadepagamento”,“ParacomprasacimadeR$100,00ofretedeveráser
gratuito”etc.;
6.Históriasdevemsertestáveis.Éprecisotercritériosdeaceitaç ãobemdefini-
dosparaqueumdesenvolvedorpossasaberquandoumahistóriaestáounãocon-
cluída.Umaboapráticaaousarcartõesparaescreverashistóriasépediraocliente
queescrevaalgunscritériosdeaceitaçãonoversodocartão.
Paraqueahistóriasejatestável,éprecisoqueoclienteescrevacritériosobjetivos
econcretos. Porexemplo,“Orelatóriodeveserintuitivo”éumexemplodecrité-
riodifíciltestar,porqueoconceitodeintuitivoéabstratoesubjetivo,podepossuir
significadosdiferentesparacadapessoa. Aoinvésdisso,“orelatóriodevepossuir
umrodapécomasomadosvalores”ou“otítulodascolunasdevesemanterfixoao
navegarentreoslan çamentos”sãoexemplosdecritériosfáceisdetestar,bastando
queodesenvolvedorcertifique-sedequeelesestãosendoatendidosparasabersea
históriaseráaceitapelocliente.
EssascaracterísticasformamoacrônimoINVEST:
• I-Independente
• N-Negociável
• V-Valiosa
• E-Estimável
• S-Sucinta
• T-Testável
Temas,Épicos,FuncionalidadeseHistórias
Écomumquemuitosprojetosdesoftware,naturalmente,possuamumaestru-
turahierárquicaderequisitos,deformaquealgumasnecessidadesdousuáriodealto
48

## Página 63

CasadoCódigo Capítulo3. FocoemValorparaoNegócio
nívelpodemserderivadasemdiversaspartesmenoresque,porsuavez,podemser
dividasnovamenteatéumagranularidadequepossasermaisfacilmentecompreen-
didaequepossaserdesenvolvidaemumdeterminadoespaçodetempo.
DeanLeffingwell,sugerequeahierarquiaderequisitoscomececom Temasque
representamumconjuntodeiniciativasqueguiamosinvestimentosemsistemas,
produtos,serviçoseaplicações[37]. Dessestemassãoderivadososépicos,inicia-
tivasdedesenvolvimentoquetêmpotencialdeagregarvaloraotemadoqualfoi
derivado.Sãorequisitosemaltonívelenãosãoimplementadosdiretamente,antes,
sãoquebradosemfuncionalidades,queposteriormentesãoquebradasemhistórias
deusuário(vejanafigura 3.4).
Temas >>Épicos >>Funcionalidades >>Histórias
Figura3.4:HierarquiadeRequisitos
Épicossãorequisitosgrandesque,geralmente,nãopodemserimplementados
emumaúnicaiteraçãoe,normalmente,contemplamdiversoseventos,fluxosece-
nários.Porquestõesdeorganizaçãoepriorização,muitavezes,éinteressantemanter
49

## Página 64

3.6. EscrevendoHistóriasdeUsuário CasadoCódigo
essesitensno backlog,semdetalharexatamenteoquedeveráserfeito,eentão,so-
mentequandoaprioridadedoépicoforaumentandoeahoradetrazê-loparao
planejamentoestiverseaproximando,seráomomentocertoparadividi-loemhis-
tóriasdeusuário.
Paramelhorilustrarimagineumsistemadegestãoempresarial.Osistemapode
tertemascomoComercial,FinanceiroeContábil,porexemplo.
OtemaFinanceiropodeserderivadoemÉpicoscomoCobran çasePagamentos,
jáoÉpicoPagamentospodeserderivadoemfuncionalidadescomoPagamentopor
BoletosePagamentosporDepósitos.
AFuncionalidadePagamentoporBoleto,poderiaserderivadaemdiversashis-
tórias,como,porexemplo,PagamentodeBoletosVencidos,PagamentodeBoletos
comJurosetc.
DividindoHistórias
Écomumquealgumashistóriasdeusuáriossejamgrandesdemaisparaserem
implementasemumaúnicaiteração.Nessescasos,éinteressantedividi-lasemvá-
riashistóriasmenores.Éimportante,porém,manteroaspectoINVEST.Vocêpode
dividirhistóriasporvariaçõesnasregrasdenegócio,porvaria çõesnosdados,por
diferentescenáriosdeusoetc.
QuebrandoHistóriasemTarefas
Deummodogeral,históriasrequeremcertoesfor çoparaseremimplementadas.
Porissoelassãodividasemtarefas,querepresentamospassosnecessáriosparaque
afuncionalidadedahistóriasejadesenvolvidaeentregueemfuncionamentoaocli-
ente.Érecomendadoqueashistóriassejamquebradasemtarefasquenãoprecisem
demaisdeumdiadetrabalhoparaseremdesenvolvidas.Posteriormenteveremos
comoissoaconteceecomoasatividadestécnicassãogerenciadas.
ApenasdepoisdeouviroPOecompreenderahistória,aequipeaquebraem
partesmenores,chamadassimplesmentedetarefas.Nestemomentoapresen çado
POémenosimportante,porqueastarefastêmumâmbitomaistécnico,egeralmente
terãodescriçõescomo:criarastabelasnobancodedados,criarobjetosdenegócio,
realizarintegraçãoatravésdewebservicesetc.
Nãoéprecisoentraremdetalhesminuciosossobrecadatarefaenestemo-
mentopode-setomaralgumasdecisõesde design que a equipe considerar
importante, como linguagens, frameworks,bibliotecasepadrõesaserem
50

## Página 65

CasadoCódigo Capítulo3. FocoemValorparaoNegócio
utilizados,alémdequestõesqueenvolvamperformanceeescalabilidade.Decisões
queaequipeconsiderarmenosimportantespodemsertomadasmaistarde,apenas
nomomentodaimplementação.
3.7 Mapeando histórias de usuários
Mapeamentodehistóriaséumatécnicaqueconsistebasicamenteemdecomporati-
vidadesdeusuáriodealtonívelemum workflowquepodeserdecompostoposte-
riormenteemumconjuntodehistóriasdeusuário.Atécnica,quefoipopularizada
porJeffPatton,écentradanaperspectivadousuário[53].
Primeiramente,temososépicosrepresentandorequisitosdealtonível,depois
temosasfuncionalidades,efinalmenteashistórias 3.5:
Figura3.5:Mapadehistórias
Dependendodaabordagemosnomesdosníveisderequisitospodemmudar.Na
abordagemoriginaldemapeamentosdehistórias,PattonusaAtividades,Tarefase
Subtarefasemvezdeépicosefuncionalidadesehistórias.Outrasfontesentendem
51

## Página 66

3.7. Mapeandohistóriasdeusuários CasadoCódigo
queépicossãomaioresquetemas,porexemplo,masissonãoimportamuito:uma
vezcompreendidaaessênciadaprática,vocêpodeescolherasemânticaqueformais
adequadaaoseucontexto.
Notequetudoestápriorizadoemdoiseixos,tantodaesquerdaparaadireita,que
representaaprioridadeentrediferentesépicos,ediferentesfuncionalidades,quanto
debaixoparacimaquerepresentaaprioridadeentrediferenteshistóriasdeusuário.
Depoisdeprontoepriorizado,vocêpodeutilizaromapaparadefinir releases
emcamadas,ouseja releasesquecontêmumpoucodecadadefuncionalidade(veja
nafigura3.6.
Figura3.6:ReleasesnoMapadeHistórias
Parailustrar,imagine,porexemplo,umsitedecomércioeletrônicoqueserá
compostoporfuncionalidadesdecarrinhodecompra,vitrineeletrônicaeConsulta
dePedidos. Emvezdeentregarumafuncionadecompletacomtodasashistórias
envolvidas,épossívelentregaralgumashistóriasdecadafuncionalidadepor release.
Dessaforma,oprodutopoderiaserlan çadocomobásicodecadafuncionalidade
ejápoderiaserutilizado.Àmedidaqueosoutros releasesforementrandonoar,as
funcionalidadesseriamaprimoradascomaentregadeoutrashistórias.
52

## Página 67

CasadoCódigo Capítulo3. FocoemValorparaoNegócio
Recomendações
• Desenvolvaomapadehistóriascolaborativamente,convideoPO,
analistasdenegócio,desenvolvedoresetc.
• Mantenhaomapasemprevisívelparaqueotimepossadiscutir
frenteaele,etomardecisõesmaisfacilmenteumavezqueomapa
dáumavisãomelhordo“todo”esobrecomoasdiferentesfunci-
onalidadesehistóriasdeusuárioestãoconectadasaobjetivosde
negócio[43].
3.8 Conhecendo os Usuários através de Personas
Personassãoperfisbaseadosnosclienteseusuáriosdoproduto.Acriaç ãodeper-
sonasajudaaidentificarPerfisdeClienteseUsuáriosimportantesparaosucesso
doprodutoeamelhoraroentendimento,acomunicaç ãoeatomadadedecisãodo
timesobreosdiferentesusuários,deformaaotimizarsuasfuncionalidadesparao
perfildousuáriofinal,egarantirqueasnecessidadesdediferentesperfissejambem
atendidaspeloprodutoemdesenvolvimento.
Vejaumaexemplodepersonanafigura 3.7:
53

## Página 68

3.8. ConhecendoosUsuáriosatravésdePersonas CasadoCódigo
Figura3.7:Persona
54

## Página 69

CasadoCódigo Capítulo3. FocoemValorparaoNegócio
Modelo paraCriação de Personas
Nãoháumaformacertaouerradadesedesenvolverpersonas,mas
essassãoalgumascaracterísticascomunsquepodemajudarotimea
compreenderumperfildeusuário.Vocêpodeescolheralgumasdessas
paracomeçaradesenvolveraspersonasdeseuproduto:
• Nome
• Papel
• Valores
• Objetivos
• Problemas
• Necessidades
• Desejos
• Expectativas
• Preferências
• PadrõesdeComportamento
• CasosdeUso
• Atividades
Depoisdecriadasaspersonasdoproduto,éinteressanteassociá-lasàshistó-
riasdeusuário,paraqueotimesaibaqueméousuáriointeressadonahistóriaa
serdesenvolvida.Épossívelfazerissotornandoapersonaexplicitanadescriç ãoda
história:
Comoumcontadoreugostariadebuscarosúltimoslan çamentos...
Comoumgerentesdecontas eugostariadeatualizarosaldo...
Comoumconsumidoreugostariade...
55

## Página 70

3.9. MelhorandoaPrevisibilidadecomEstimativas CasadoCódigo
3.9 Melhorando a Previsibilidade comEstimativ as
Aestimativapermitequeaequipeme çaaprodutividadeesaibaquantotemposerá
necessárioparaconcluirodesenvolvimentodashistóriasdoprojeto,alémdeajudar
oclienteaentenderqualocustododesenvolvimentodecadahistóriaequaléa
médiadetempoqueseránecessárioparaqueafuncionalidadesejadesenvolvidae
entregue.
Estimativassãocomplexasenãosãoprecisas. Umasériedefatoresdevemser
levadosemconsideração,entreeles,amaturidadedaequipeemrelaç ãoaoprojetoe
àstecnologiasaplicadasnele.
Écomumquenoiníciodoprojetofuncionalidadesdecomplexidadessemelhan-
teslevammaistempoparaseremimplementadasdoquenofinaldoprojeto. Isso
ocorreporqueaequipeganhaprodutividadeàmedidaqueaprendemaissobreone-
gócioesobreatecnologiautilizada. Assumindoessapremissa,épossívelconcluir
queaestimavadeumadeterminadahistóriapodemudaraolongodotempo.
Éimportantequetodososmembrosdaequipeparticipemdoprocessodeesti-
mar.Quandoumdesenvolverestimaumahistóriasozinho,eleofazcombaseem
suasexperiênciaspessoais.Quandoaestimativaérealizadaemequipe,o expertise
envolvidoémuitomaioreaschancesdeobterumresultadomaisadequadotambém.
Umadasmedidasmaiscomunsdeestimativasãohoras.Aequipeindicaquan-
tashorasserãoconsumidasparaqueumafuncionalidadesejaimplementada. No
desenvolvimentoágil,émaiscomumutilizarpontospararealizarestimativas.
Pontospodemtersignificadosdiferentesdeacordocomcadaequipeouprojeto.
Umadasformas,comorecomendadonométodoXP,équantificarumpontocomo
sendoumdiaidealdetrabalho,ouseja,umdiatotalmentededicadoarealizaruma
tarefa,seminterrup ções. Dessaforma,doispontosseriamdoisdiaseassimpor
diante.
Outraforma,recomendadapelométodoScrum,éutilizarpontosrelacionados
aoesforço,emvezdetempo. Dessaforma,toma-seumafuncionalidadesimples
comoreferência,porexemplo,odesenvolvimentodeumateladecadastro,eassume-
sequeessareferênciavaledoispontos.Aoestimaroutratarefaavalia-seemquantas
vezesmaisfáciloumaisdifícilemrelaçãoàreferênciaéahistóriaatual.
Outratécnicaparatentarabsorveraincertezaefaltadeprecisãodasestimativas
éautilizaçãodeintervalos,comoasequênciadeFibonacci:“0,1,2,3,5,8,13,21,
34,55,89,144”ouumasequênciasimplificada“0,1,2,3,5,8,13,20,40,100”.Assim,
utiliza-seapenasosvaloresdentrodasequênciapararepresentaroesfor çonecessário
paraaimplementaçãodahistória.
56

## Página 71

CasadoCódigo Capítulo3. FocoemValorparaoNegócio
NoScrum,utiliza-seoPlanningPoker,ouPokerdePlanejamento. Nestatéc-
nicacadamembrodaequiperecebeumconjuntodecartascomosvaloresdeuma
sequência,comoasdescritasanteriormente.Emseguidatodasashistóriassãoanali-
sadasseparadamente,ecadamembrodaequipecolocaumacartasobreamesacom
onúmerodepontosqueconsideraqueahistóriaconsumirá.
Quandohouvergrandesdiferen ças,aspessoasquejogaramascartasdemaiore
menorvalorexplicamsuasrazõesparaescolheraquelevalore,então,combasenas
explicações,ascartassãojogadasnovamenteatéqueumconsensosejaencontrado
eaestimativasejadefinida.
Narealidade,nãoimportaqualtécnicasuaequipeutiliza,oimportanteéque
todososmembrosdaequipeparticipemequesejadefinidoumvalordeesfor ço
oucustoparaquesejapossívelmediravelocidadedaequipeparafundamentar
oplanejamentode releasesedarumacertaprevisibilidadeparaosinteressados
(stakeholders).
3.10 DefinindoEntregas com o Planejamento de Re-
leases
Oobjetivodasreuniõesdeplanejamentode releasesédefinirquandonovosincre-
mentosdoprojetoserão,finalmente,instaladosemproduç ão.Assimcomoosoutros
procedimentos,estareuniãotambémdevepossuirumacadência;geralmente,acada
duassemanasoumensal.
Todososinteressadosdoprojetopodemparticipardareunião.Especialistasde
integração,especialistasderedes,desenvolvedores,testadores,designersetodosque
estiveremrelacionadosaoprocessodeentrega(deployment)devemestarpresentes.
Oimportanteéqueareuniãosejacompostapelaspessoascapazesdetomardecisões
técnicas,denegócioegerenciais.
Quandooprocessode releaseémuitocomplexo,podeserinteressanteteruma
pessoaresponsávelporcoordená-lo.Écomumqueumgerentedeprojetosassuma
essepapel,liderandoareunião,alémdecoordenaros releases.
Duranteareuniãodeplanejamentode releasesdeve-sedeliberarsobrequeitens
irãocomporopróximo release.Esteéummomentooportunoparaselevantarecon-
siderarosricos,pensarsobreplanosdecontingênciaetreinamentos,analisarquanto
tempooprocessodedeploydeverálevar,quemdeveráestarpresentenomomento
dodeployequandoeleserárealizado.
57

## Página 72

3.10. DefinindoEntregascomoPlanejamentodeReleases CasadoCódigo
Paraqueos releasessejamcurtosénecessáriotentardividirashistóriasdasitera-
çõesemgruposquerepresentemomínimopossíveldefuncionalidadequeagregue
algumvalor.Dessaformaoclientenãoprecisaráesperarmuitotempoparareceber
retornodeseuinvestimento,ereceberáesseretornofrequentementeemfuncionali-
dadesqueseriamadicionadaspoucoapoucoaoproduto,agregandoassimcadavez
maisvaloraosoftware.
Oplanejamentode releasesofereceummapaparaalcan çaroobjetivodoprojeto.
Imagineumprojetodeseismesesparaumsupermercado.Poderíamosdividi-loem
seis releasesdeummêscada. Noprimeiro releasepoderíamosentregaromódulo
degerenciamentodepre ços,nosegundo releaseomódulodepedidodecompra,
noterceiroosrelatóriosgerenciais,eassimpordiante.Assim,acadamêsocliente
poderiaresgatarumpoucodeseuinvestimentoemformadesoftware.
Éimportantebuscarentregaromáximodevaloragregadoaoclienteacada rele-
ase,masissonãosignificaomesmoqueentregaromaiornúmerodefuncionalida-
des.Éprecisoentenderoqueagregarámaisvalor.
Muitasvezesumaúnicafuncionalidadepodeagregarmaisvalordoquedezenas
deoutrasjuntas. NoScrum,porexemplo,fala-sedoconceitodevalordenegócio
ou business value,quepodeserrepresentadoporumintervalonumérico,comopor
exemplode0a100. OvalordenegócioédefinidopeloPO,eéatravésdeleque
aprioridadedasfuncionalidadesaseremdesenvolvidasédeterminada. Essevalor
podemudaraolongodotempo,porissoéimportanteestarpreparadoparaadaptar
oplanejamento.
Outrofatorimportanteemsetratandodepriorizaçãoédetalharequebrarapenas
osrequisitosdemaiorimportânciaparaquesejamaissimplessemanterashistórias
priorizadaseorganizadas.Porexemplo,sevocêestádesenvolvendoumsistemafi-
nanceiro,esabequenãofaráocalculodefinanciamentonospróximos5 releases,é
melhormanterapenasumépico“Financiamento”doquejáquebraremhistóriases-
pecíficas“CalcularFinanciamentocomSistemaSAC”,“CalcularFinanciamentocom
SistemaPrice”etc.
58

## Página 73

CasadoCódigo Capítulo3. FocoemValorparaoNegócio
Mantenha o BacklogPequeno
Paraseterumaideiadecomoacomplexidadedepriorizarhistó-
riasaumentaàmedidaqueseadicionahistóriasnobacklog: sevocê
tiver3estóriasnobacklog(A,B,C),vocêpodeter6ordensdeprio-
ridadediferentes(A,B,C),(B,A,C),(B,C,A),(A,C,B),(C,A,B)e
(C,B,A).Agora,sevocêtiver5itens,poderáter120ordenaçõesdife-
rentes,setiver10itenspoderáter3.628.800esetiver20itenspoderá
ter2.432.902.010.000.000.000ordenaçõesdiferentes.Issomesmo,éum
calculofatorial,comonascorridasdecavalos.
Umdosprincipaisbenefíciosdosmétodoságeisedodesenvolvimentoemite-
raçõeséareduçãodotempodasentregasparaocliente. Duranteoplanejamento
de releaseséimportanteprocurarpotencializaro time-to-market,porissodevemos
descobrirqualescoponecessárioparaagregaralgumvaloraoclientee,então,definir
umreleaseparaentrega.Quantomenoresforemosciclosderelease,maisrápidoo
clientepoderásebeneficiardoproduto,eoferecerfeedbackparaqueelepossaser
melhorado.
Paratraçarumplanejamentode releaseséprecisoestabelecerperíodosfixosde
entrega.Recomenda-sequesejaumcurtoespaçodetempo.Comavisãodoproduto
emmenteénecessárioestabelecerquaissãoasfuncionalidadesquepodemagregar
maiorvalor,ouseja,asquepossuemmaiorvalordenegócioeserãoincluídasmais
rapidamentenos releases.
Tendoemmãosavelocidadedotimeépossívelterumaideiadequantasfun-
cionalidadespodemserincluídasemumdeterminadoperíododetempo,eentão
dividirasfuncionalidadesem releases.
Nãoplanejeparaprazosmuitolongos.Quantomaislongooprazo,maiorain-
certeza.Nãoénecessário,enemrecomendável,escrevereanalisartodasashistórias
noiníciodoprojeto. Damesmaformaqueaequipeaprendeeaprimorasuastéc-
nicasdedesenvolvimentoacada release,oclienteutilizaosoftwareenovasideias
surgem,bemcomoideiasantigaspodemserdeixadasdelado. Éporissoquenão
éinteressantetentarpreverfuturosmuitodistantes:quantomaisdistante,maiora
incerteza.
Umagrandediferen çadosmétodoságeisemrelaçãoaostradicionaiséqueos
métodoságeisnãotentamimpediroclientederealizarmudan çasnoplanejamento.
59

## Página 74

3.11. RoadmapdoProduto CasadoCódigo
Emvezdisso,considera-sequeoclientetambémaprendeaolongodoprojetoesuas
mudançastrarãobenefício.Éclaroquedevehaveralgumtipodeprote çãoparaque
asmudançascomfrequênciaexageradanãotornemoprojetoinviável.TantooXP
comoScrumaconselhamqueaomenosaiteraç ãoatualnãosejamodificada.
Éimportanteentenderadiferen çaearelaçãoentreiteraçãoe release.Os releases
representamentregaseasiteraçõesrepresentamciclosqueestãocontidosdentro
dos releases.Asiteraçõesrepresentamumdeterminadointervalodetempoemque
algumashistóriasserãoimplementadas.
Nasiteraçõespodemestarcontidasdiversasatividadescomoasreuniõesdere-
visãoeretrospectivas,discutidas.Épossível,porexemplo,definir releasesmensais
comquatroiteraçõesdeumasemanacada.Nãoexisteregraquantoàperiodicidade
dos releases,afinalcadaprojetotemsuasparticularidadeseum releasepodeimplicar
emumasériedefatores,comoporexemplo,implantaç ãoetreinamento.Porisso,o
númerode releaseseiteraçõesestipuladosdevemestaralinhadosàsnecessidadesda
suaorganização.
Aofinaldo releaseosoftwareéentregueparaoclienteprontoparaproduç ão.
3.11 Roadmap doProduto
ORoadmapéumaferramentaútilparatraçarumplanodealtonívelsobrefuturos
releasesemarcosimportantesdoprodutoqueserãoalcan çadosaolongodotempo.
ORoadmapoferecevisibilidadedequefuncionalidadesserãoentreguespri-
meiroequaisserãoentreguesdepoiseemquais releases,ealémdissoapresenta
marcosimportantesdoprodutoqueestásendoconstruindo(verfigura 3.8).
Figura3.8:Roadmap
60

## Página 75

CasadoCódigo Capítulo3. FocoemValorparaoNegócio
Comodesenvolvimentodesoftwareéaltamentecomplexopornaturezaedifícil
deseestimareprever,numcontextoágil,oroadmapéumaferramentaútilpara
mostrarintençõesdereleaseeapresentarmarcosdoproduto,masnãotantopara
definirprazosexatosdeentregadefuncionalidades,justamenteporqueénatural
quemudançasnoescopodoprodutoocorramaolongododesenvolvimento. Por
issousa-semaiscomoumcritériorelativodoqueabsoluto,porexemplo,nafigura
3.8pode-severqueafuncionalidadedepre ço,serálançadadepoisdadepedido,mas
seestádefinindoumadataexataparaisso.
MuitasvezesoroadmappodeserútilparaequipesdeMarketingedeNegóciose
posicionarememrelaçãoa(maisoumenos)quandodeterminadasfuncionalidades
estarãodisponíveisparafinsdepublicidade,treinamentosetc.
3.12 Mantenha as Opções Abertas
Umdoprincípiospordetrásdemuitaspráticasdosmétodoságeiséa“liberdadede
escolha”[40].ChrisMattseOlavMaassenchamam-nodeOp çõesReais(eminglês
Real Options).
Apesardenãoserexatamenteamesmacoisadoqueasop çõesdomercadofi-
nanceiro(stockoptions),háumarelaçãoentreosconceitos.Asop çõesdomercado
financeiroconferemaotitularodireito(enãoobrigaç ão/compromisso)decomprar
umdeterminadoativo(ação,títulooubemqualquer)porumvalordeterminado,
enquantoovendedoréobrigadoaconcluiratransaç ão.
Quandovocêcompraumingressoparaocinema,porexemplo,paravocêéuma
opçãoporquemesmotendocompradooingressovocêpodeounãoirverofilme;já
paraocinemaissoémaisumcompromisso,porqueelejátevendeuobilheteeagora
precisarápassarofilmenohoráriodeterminado.Vaidependerdopontodevistade
cadaumdosladosdarelação.
Muitasvezesnósvemoseencaramosascoisascomocompromissosemsituações
quepoderíamosencararcomoop ções.Opçõesquepodemosounãoexercer.
Opensamentodeop çõesreaisconsisteemenxergareavaliartodasessasop ções
aoseuredorecomprometerapenasdeformadeliberada. Casocontrário,sempre
sedevedeixarparaassumirocompromissonoúltimomomentopossível,ouseja,
quandovocêtemasinformaçõesqueprecisaparatomaradecisãodecomprometer-
sedeverdade.
Umaopçãoéumaescolha,umadecisãodeescolherumaestratégiaemvezda
outra,deescolherumcaminhoemvezdooutro,decomprarumprodutoemvezdo
61

## Página 76

3.12. MantenhaasOpçõesAbertas CasadoCódigo
outro,detrabalharemumafuncionalidadeemvezdeemoutra.Cadaumadessas
escolhastemumretornosobreoinvestimento.Odesafioétrabalharcomaop ção
quetiveromelhorretornosobreoinvestimento.
Adiferençaprincipalentrecompromissoseop çõeséquepodemosmudarde
escolhadeop çõessemcustoalgum,oucomumbaixocusto,masmudarumcom-
promisso,geralmente,geracustosouproblemascasoelenãosejacumprido.Temos
ocustodaop çãoeoretornosobreoinvestimentoquecadaumaoferecer.
Omaisinteressanteéquehávalornasop çõesqueconhecemosenaquelasque
nãoconhecemostambém.Porissoésempreimportanteconsiderartodasasop ções
possíveiseprocuraraprendersobreop çõesatéentãodesconhecidasantesdesecom-
prometercomumadeterminadaop ção.
Decidirnoúltimomomentopossível(nãoconfundircomnegligenciar)éum
dosprincípiosdeLeanSoftwareDevelopment,etambéméalgoquefazpartedeuma
sériedepráticasutilizadasemequipeságeiscomoRefactoringeDesignEmergente(o
designnãoédefinidodeantemãomasvaievoluindoaolongododesenvolvimento),
PlanejamentoIterativo(aequipesecomprometeapenascomashistóriasdeusuário
deumiteraçãoeorestodobacklogtorna-seumaop çãoparao Product Owner;essas
históriaspodemounãosetornarumaobrigaç ãoseincluídasnoplanejamentoda
próximaiteração),IncrementosPotencialmenteEntregáveis(OPOpodeexercerou
nãoaop çãodefazerum releasedoresultadodeumaiteração)etc.
Jácommétodostradicionais,oclienteprecisadecidirsobretodooescopodean-
temão,eseprecisardealteraçõesterácustosextras,porisso,élevadoatomaruma
sériede(más)decisõesantecipadas,eessemesmoerropermanecenoBigRequire-
mentsUpFrontenoBigDesignUpFront.
Muitaspessoaspreferemestarerradasdoqueestaremdúvida.Porisso,acabam
tomandodecisõesruins,porseremprecipitadas[30].Op çõesReaisnosapresentam
umamelhorformadelidarcomnossasdecisões.
TrêsregrasdasOpçõesReais:
1.Opçõessãovaliosas:Op çõessãovaliosasporquepodemserexecutadas.No
exemplodoingressodocinema,paraocompradoréumaop çãoqueestájustamente
napossibilidadedeentrarnasessãoparaverofilme.Ovalorestáemterop çõesem
poderescolher.
2.Opçõesexpiram:Op çõestêmumtempodevida,nocasodoticketdecinema,
elesóvaleduranteotempodofilme,apósasessãodofilme,aop çãoperdeseuvalor,
independentedesersidoexercidaounão.
3.Nuncasecomprometacedo,amenosquesaibaoporquê:Quandovocêse
62

## Página 77

CasadoCódigo Capítulo3. FocoemValorparaoNegócio
comprometecomumaop çãoestáabrindomãodetodasasoutrasedovalorqueelas
podemoferecer.Quandonoscomprometemoscedodemais,háumgranderiscode
nãoconhecermostodasasop çõesounãoescolhermosamelhor.
InjeçãodeFuncionalidades
Muitosprojetoscome çamcomumagrandelistadefuncionalidadesabstratasa
seremdesenvolvidase,então,otimeprecisacorreratrásdeumvalordenegócio
poucoclaroedesconhecido.Ouseja,écomosesoubessemquetêmquecorrer,mas
nãosoubessemadire çãoenemporqueestãocorrendo.
Quandoalguémlhepedeparaalteraralgodainterfacedeusuário,porexemplo,
qualéovalorqueestáportrásdessamudan ça?ReduzirotempodoProcesso?Ga-
nharnovosUsuários?Reduzirachancedequeumerroaconte ça?Quandoocliente
diz“PrecisoquesejaincluídooCampoXnoSistema”,vocêsabeomotivo?Quevalor
estáportrásdisso?Seráqueissorealmentevaiagregaralgumvalor?Paraquem?De
queforma?
ÀsvezesoPOdáênfaseno“como”emvezdeenfatizar“oporquê”.Masseisso
forinvertido,eoPOtrouxeroporquê,juntocomotime,podemchegaraum“como”
muitomelhor.
AInjeçãodeFuncionalidadeséumProcessodeAnálisedeNegócioscriadopor
ChrisMattscombasenaTeoriadasOp çõesReaispararesolveresseproblema. O
processopossuitrêspassosbemsimples.
1.PersigaoValordeNegócio
Quandoovalordenegócionãoestáclaro,asequipesnãopodembuscarfor-
masdiferentesemaiseficientesdeseconseguirovalor.Afuncionalidadepodeser
entregue,porémdeformadistorcidaenãolevarovalorqueeraesperado.
AInjeçãodeFuncionalidades(eminglêsFeatureInjection)propõequetudoco-
mececomummodelodeentregadevalor[6],comoporexemplo:“Nósesperamos
queotempomédiodefaturamentoreduzade20minutospara5minutos,queonú-
merodecolaboradoresdedicadosaoprocessoreduzade100para40,eaquantidade
deemissõesincorretasreduzade900notasfiscaispara100notasfiscais.”
Ummodelocomoessepermitequeotimeavalieasfuncionalidadesqueestão
desenvolvendoese,defato,poderãoounãocontribuirparaqueomodelodevalor
sejacolocadoemprática. Torná-loexplícitoajudaacriarumentendimentocom-
partilhadodeondeovalorestávindo. Comumobjetivoclaro,tambémficamais
fácilparasedefiniroqueentraounãoentranoescopoequalaprioridadedecada
63

## Página 78

3.12. MantenhaasOpçõesAbertas CasadoCódigo
itemdobacklog.Bastaprocurarentenderemqueafuncionalidadecontribuirácom
omodelodevalor.
2.InjeteasFuncionalidades
Depoisdeteromodelobemdefinido,éhoradecriarumalistadefuncionali-
dadesquedeverãoserdesenvolvidasparaatingirovalordenegócio.Oimportante
équedevehaverumaligaç ãoclaraeobjetivaentreasfuncionalidadesevalorde
negócio[6].
Muitos Product Ownerscomeçamperguntando“oque”nósprecisamos,emvez
perguntar“paraque”nósprecisamos,eissoacabalevandoaumasériedefunciona-
lidadesqueparanadacontribuem. Porisso,comInje çãodeFuncionalidadesvocê
começadetrásparafrente,ouseja,emvezdeperguntaroqueeupreciso(asentradas
dosistemas)vocêpensanoporquêdeprecisar(nassaídasdosistema).
Éimportantelembrarqueovalornãoestánasfuncionalidadesemsi,masno
resultadoqueousodelasforneceaousuário.
Tradicionalmente,aspessoasdenegóciovêmcomsoluçõesmeioprontasemvez
deapresentarovalordenegócioqueestãobuscando.ComInje çãodeFuncionali-
dadesotimepropõesoluçõesemcimadovalorapresentado.
Decertaforma,aInje çãodeFuncionalidadesésemelhanteaTDD(Desenvol-
vimentoGuiadoporTestes),porqueemvezdecome çarporescreverocódigoda
funcionalidade,noTDD,vocêcome çafazendoumtestequeverificaseoresultado
estácorretoedepoisfazaimplementaçãodafuncionalidade.ComInje çãodeFun-
cionalidades,vocêcomeçacomoOutputdoSistema(Saídas,Resultado)edepois
descobreosInputs(Entradas)dequeprecisaparaconseguiroOutput.
Paradaraindamaisênfasenovalordenegócio,CrisMatts,propõeumainversão
noformatotradicionaldashistóriasdeusuáriodeMikeCohn:
Comoum<papel>
Euquero<funcionalidade>
paraque<valordenegócio>
AinjeçãodeFuncionalidadescome çapelovalordenegócio:
Paraque<valordenegócio>
comoum<papel>
euquero<funcionalidade>
64

## Página 79

CasadoCódigo Capítulo3. FocoemValorparaoNegócio
Exemplo deInjeção de Funcionalidade
Paraaumentaronúmerodevisitantesnomeusitecomoumpublici-
tário(eaquientramasop ções)
Paraaumentaronúmerodevisitantesnomeusitecomoumpublici-
tárioeuquerointegrarnossositecomoFacebook
Paraaumentaronúmerodevisitantesnomeusitecomoumpublici-
tárioeuqueropublicarnotíciasdiariamente
Paraaumentaronúmerodevisitantesnomeusitecomoumpublici-
tárioeuquerootimizarositeparamecanismosdebuscas
Notequeovalorpermanece,masafuncionalidadepodemudar.Porissoéim-
portantequeotimefoqueemobterovalordenegócioenãoafuncionalidade.
3.EncontreExemplos
Agoraéprecisoencontrarasvariáveisquepodemafetaroresultado,ouseja,
expandiroescopoecomaInje çãodeFuncionalidades.Issoéfeitoatravésdeexem-
plos: trabalharcomexemploséumaótimaformadeverificarseaspremissasdos
requisitossãodefatoválidas.
Comececomosexemplosmaissimples,depoispartaparaosmaisespecíficose
complicados.Busqueexemplosespecíficosenãogeneralizados.
Procureporcenários,porcasosreais.Éhorasdebuscaros“quandos”,os“ses”,
os“naquelecaso”,os“emparticular”etc. Peçaexemplosreaisparaaspessoasde
negócio.
AInjeçãodeFuncionalidadepermitequevocênãosecomprometacedodemais
comoumasoluçãoruimquepodenemsequeragregarvalor,masque,emvezdisso,
ovalordenegóciosejaofocodoprocessoequepuxetudoomaisqueforpreciso
paraqueelepossaserconquistado.
3.13 Eagora, o que eu faço amanhã?
Vocêseresponsabilizaativamentepeloresultadodoseutime,ouapenasporsuas
contribuiçõesindividuais?Reflitasobreisso.
Avisãodoprodutoquevocêestáajudandoaconstruirestádisseminadaentre
todososmembrosdasuaequipe? Quetalcriarumdiscursodeelevadorparaseu
produto?
65

## Página 80

3.13. Eagora,oqueeufaçoamanhã? CasadoCódigo
Quaissãoosmarcosmaisimportantesdoseuproduto?Faç aumroadmapdeseu
produtoeidentifique-os.
Quaisosdiferentesperfisdeusuáriosqueutilizamouutilizarãooprodutoque
vocêestáajudandoacriar?Discutacomsuaequipeecriealgumaspersonas,procure
associá-lascomasfuncionalidadesquevocêsestãodesenvolvendoatualmente.
Qualéafrequênciacomquevocêsentregamsoftwareparaocliente? Essa
frequênciapoderiaserdiminuídadealgumaforma?
Nopróximoplanejamentodasuaequipe,proponhafazerummapeamentodas
históriasdeusuário,depoisdeescreverashistóriaseorganizá-lasverifiqueseestão
atendendooscritériosINVESTediscutasobreissocomaequipe.
Suaequipejáestáutilizandolimitesdetrabalhoemprogresso(WIP)?Senão,
quetalconversarcomtimeedefiniralgunslimitesiniciaisparaidentificargargalos
eproblemasdetrabalhoparado?
Seutimeestámantendoasop çõesabertas?Noquevocêestãosecomprometendo
cedodedemaissemsaberoporquê?
Vocêeseutimesabemoqualéovalordenegócioqueestáportrásdecadauma
dasfuncionalidadesqueestãodesenvolvendo?SeráquevocêspodemajudaroPOa
encontrarformasmaiseficientesebaratasseconquistarovalordenegócioqueestá
sendoperseguido?
66

## Página 81

Capítulo4
EntregandoValor
Esteéosegundoníveldefluênciaágil,noqualosbenefíciospredominantessãoa
altaprodutividadeeamelhorianaqualidadeexternadoproduto.
Éummomentooportunoparainvestimentonascapacidadestécnicasdaequipe
e,porisso,agoraserãoapresentadasalgumastécnicasepráticasdeengenhariautili-
zadasporequipeságeis.
Equipesnesteníveldefluênciatêmahabilidadedemanterseusprodutossempre
(ouquasesempre)emumestadodepronto-para-entrega,permitindoassimqueo
produtosejaatualizadocomavelocidadeefrequênciaqueomercadoexige.
Capacitarumaequipeparaalcan çarumaltoníveldehabilidadetécnicarequer
tempo,esforçoemuitaprática.Cursos,treinamentos,contrataçãodedesenvolvedo-
resexperientesparaensinarosmenosexperientespodemserimportantesparase
atingiresseobjetivo[57].
Oaprendizadodetécnicasmaisavan çadaseopagamentodadívidatécnicacri-
adapelafaltadeexperiênciaecódigolegadopodemreduziraprodutividadeneste
momento. Masapesardoaltoinvestimento,umaequipebemcapacitadatecnica-

## Página 82

4.1. TestesÁgeis CasadoCódigo
mentepoderácriarprodutoscommenosdefeitos,oqueresultaráemmaistempo
paraproduzirfuncionalidadesquerealmentepossamagregarvalor.
Algumaspráticaspredominantesnesteestágiosão:programaçãoempar,inte-
graçãocontínua,propriedadecoletivadecódigo,edesenvolvimentoorientadoates-
tes(TDD).
Aseguirfaremosumrápidoestudosobrecadaumadessaspráticaságeis.
4.1 TestesÁ geis
Métodoságeisdefendemaideiadequeéprecisocriarsoftwaredequalidadedesde
oinício,aoinvésdeasseguraraqualidadeapenasnofinaldoprocesso.
Novasfuncionalidadesserãoentreguescomaltafrequênciaenãosepodepermi-
tirqueasalteraçõesrealizadasnosoftwareparacriarasnovasfuncionalidadesfaç am
comquefuncionalidadesjáexistentesdeixemdefuncionar.Éparaprevenirqueisso
aconteçaqueexistemostestesderegressãoquepodemserrealizadosmanualmente
ouautomatizados.
Alémdisso,deve-seprevenirdefeitosatodoomomento,porquequantoantes
umdefeitofordetectado,maisrápidoebaratoserápararesolvê-lo.
Oqueémaisbarato: descobrirqueumaalteraç ãoemumapartedosoftware
criouumdefeitoemoutraatravésdofeedbackdeumtestesdeunidadeduranteo
desenvolvimentoeentãoresolveroproblemanamesmahora,enquantoaindase
estácomasregrasdenegócioemmente;oudescobrirposteriormentequeodefeito
existeporquenãopassoupelaqualidadeou,aindapior,descobrirqueoproblema
existeapenasquandoosoftwarejáestiveremproduç ão?
Aresposta,claro,émuitoóbvia: quantomaiscedovocêdescobrirqueopro-
blemaexiste,maisrápidoebaratoserápararesolvê-lo.Amesmaideiaéaplicadana
Toyotaparadefeitosemcarros.
Aolongodestase ção,estudaremosdiversastécnicaseabordagensdiferentespara
testesque,combinadas,podemserúteiseimportantesparaodesenvolversoftware
comqualidade.
Apirâmidedetestes,criadaporMikeCohn[20]éummodelointeressanteque
alémdedefenderquediferentestiposdetestespodemsercombinados,tambémsu-
gereumapropor çãodentreosdiferentestipos,comopodeservistonafigura 4.1:
68

## Página 83

CasadoCódigo Capítulo4. EntregandoValor
Figura4.1:PirâmidedeAutomaçãodeTestes
Diferentestiposdetestestêmobjetivosdistintoseseucustodeautomaç ãoe
tempodeexecuçãotambémdiferem.
TestesdeUnidade,geralmente,sãoosmaisrápidossedeautomatizaretambém
sãorápidosdeexecutar,porisso,elesestãonabasedapirâmideerepresentama
maiorpartedostestespropostospelomodelo.
Emseguida,temosostestesdeintegraç ão(tambémchamadosdetestesdeser-
viçooutestesdeAPI).Elessãomaiscompletose,geralmente,combinamdiferentes
componentesquetrabalhamemconjuntopararealizaremumdeterminadosistema.
Sãorealizadosdiretamentenaaplicaçãosempassarpelainterfacedeusuário.
Emterceirolugar,enotopodapirâmide,temosostestesdepontaaponta(tam-
bémchamadosdeinterfacedeusuário,testesdesistema,outestesdeaceitaç ão)que,
comoonomesugere,testamaaplicaç ãodesdeainterfacedousuário,porissosão
osmaiscompletose,geralmente,sãotambémosmaiscarosdeseautomatizar,eos
maislentosparaseexecutar.
Éimportanteanalisaroscustosebenefíciosdecadaumdostiposdetestespro-
postosnapirâmideparasefazerbonsinvestimentosemautomaç ãodetestes.
Hátambémostestesexploratórios,quesãoexecutadossempremanualmente
69

## Página 84

4.1. TestesÁgeis CasadoCódigo
porummembrodotime,comafinalidadedeiralémdeondeostestesautomati-
zadospuderamchegar. Elesnãoseguemumscriptpré-planejadoesebeneficiam
dacapacidadedeinvestigação,daobservação,daanaliseedaadaptaçãodotestador.
Atravésdelesostestadoresbuscameencontramriscosqueextrapolamouniverso
deriscosquepuderamserprevistosdeantemãopelaequipe.
Emsefalandodepreven çãodedefeitosdesoftware,TDD(Test-DrivenDeve-
lopment)éumaótimaferramentanamaioriadoscontextos.Essatécnicasugerea
escritadetestesdeunidadeantesmesmodesecodificarafuncionalidadeasertes-
tada.Comisso,épossívelgarantiraltacoberturadetestes[7]e,consequentemente,
feedbackrápidoemcasodealteraçõesquepossamgerarefeitoscolateraisquebrando
outrasfuncionalidades.
Aseguirexploraremosumpoucomelhorcadaumdosdiferentestiposdetes-
tes.Éimportanteteremmentequenenhumaabordagemémelhordoqueaoutra;
naverdade,cadaumdeleséumaboaferramentaspararesolvercertostiposdepro-
blemae,você,provavelmente,precisarácombinartodosparagarantiraqualidade
necessárianoprodutoqueestádesenvolvendo.
TestesdeUnidade
Escrevertestesdeunidadeéumapráticaessencialparasegarantiraqualidadede
umsoftware.Umdesenvolvedorágilevitaaomáximoescrevercódigosemescrever
tambémumtestedeunidadeparaverificarsetudoestáfuncionandodaformacomo
deveria,porisso,nométodoXP,utiliza-seumapráticaconhecidacomoTDD-Test-
DrivenDevelopmentouDesenvolvimentoGuiadoporTestes.
ComTDDostestesdeunidadesãoescritosantesmesmodoqueasclassese
métodosaseremtestados,melhorandoassimagarantiadequetodoocódigoestá
cobertoportestes.ÉimportanteressaltarqueoconceitodeTDDvaimuitoalémde
apenasescrevertestesdeunidade,eapresenta,naverdade,umaformainovadorade
sepensarnodesigndeumsoftware.
Émuitoraroqueumdesenvolvedoracreditequepossaescrevercódigoquesem-
prefuncionaránaprimeiravez. Naverdade,muitosficamsurpreendidosquando
issoacontece. Porisso,independentedeescrevertestesantesoudepois,épreciso
testarparagarantirqueosoftwareestáfuncionadodamaneiraquedeveriafuncio-
nar.
Umaalteraçãoemumdeterminadotrechodecódigodeumapartedeumsistema
podecausarumproblemaemoutraparte,eoscomponentesgeralmentecontêmde-
pendências,quequandoalteradaspodemmodificarseuscomportamentosdeforma
70

## Página 85

CasadoCódigo Capítulo4. EntregandoValor
inesperada:sãoosconhecidosefeitoscolaterais.
Alémdeajudarnamelhoriadaqualidade,ostestesdeunidadepodemajudar
odesenvolvedoraentendermelhorasregrasdenegóciodosistema,umavezque,
provavelmente,haveráumtesteparacadaregra.Dessaforma,elespoderãosercon-
sideradostambémuma“documentaçãoviva”,porquealémservircomoreferência
paracompreensãodasregrasdenegócio,servirãotambémparagarantirqueessas
regrasestejamimplementadascorretamenteequeosoftwareestejasecomportando
damaneiraqueseespera.
Éimportantequeostestessejamfáceisdeseexecutar,porquepoucoadiantará
tertestesdeunidadequenuncasãoexecutadosouquesãoexecutadoscomuma
frequênciamuitobaixa.
TestandoantescomDesenvolvimentoGuiadoporTestes
DesenvolvimentoGuiadoporTestes(TDD)éumprocessoemqueodesenvolve-
dorcomeçaaimplementaçãodeumanovafuncionalidadepelotesteedeve,otempo
todo,fazerdetudoparaqueseucódigofiquesimplesecomqualidade[7].
TDDérealizadoatravésdeumciclocomosseguintespassos:
Figura4.2:CiclodeTDD(ImagemdeMaurícioAniche)
1) Adicioneumtesterapidamente.
2) Executetodosostesteseobserveonovotestefalhar.
71

## Página 86

4.1. TestesÁgeis CasadoCódigo
3) Façaumapequenamudan çaparafazerotestepassar.
4) Executetodosostesteeobservequeforambemsucedidos.
5) Refatore.
OusodeTDDasseguraquetodocódigoadicionadoaorepositóriosejatestado
e,alémdisso,dáênfaseemseescreverapenasocódigonecessárioparaqueostes-
tespassem,evitandoqueodesenvolvedorescrevamaisdoqueénecessário,contri-
buindoparaumcódigomaissimples,enxutoetambémmaisfácildesedarmanu-
tenção.
TestandodePontaapontacomtestesdeAceitaç ão
TestesdeUnidadenãosãoosúnicostiposdetestequedevemserrealizados.
Existemoutrostiposque,unidosaosunitários,poderãotrazerumaqualidadeainda
melhoraosoftware.Éocasodostestesdeaceitaç ão,tambémconhecidoscomotestes
funcionaisoutestesdeusuáriofinal.
Testesdeaceitação,diferentedostestesdeunidadequeverificamapenasocom-
portamentodeumaclasseoumétodo,testamocomportamentodosistemadeuma
formamaisampla.Geralmente,representamocontextocompletodeumahistória
deusuário,oucasodeuso.Ostestesdeaceitaç ão,sãobaseadosemcritériosdeacei-
taçãorelacionadoscomregrasdenegócioquepodemserespecificadaspelo Product
Owner.
Épossívelrealizartestesdeaceitaç ãomanualmenteouautomatizá-los.Areali-
zaçãodetestesmanuaispodereduzirdrasticamenteavelocidadedotime,porisso,
recomenda-seaautomaçãodostestes.
AlgumasferramentascomooSelenium,porexemplo,permitemrealizaraau-
tomaçãodetestesdeaceitaç ãoemaplicaçõesweb,gravandoaçõesdousuáriono
navegadorparaqueocenáriopossaserreproduzidoeosresultadosverificadospos-
teriormente.
Váalémdetestesexploratórios
TestesManuaissãotestesrealizadosporpessoas,geralmente,quetêmopapel
detestadoresemumtimededesenvolvimentodesoftware.Algunstestesmanuais
consistembasicamentenaexecuçãodeumscriptescritodeantemãoquepossuiuma
sequênciadepassosaseremseguidoseumresultadoaservalidado.Essetipodeteste
podeserfacilmenteautomatizados.
72

## Página 87

CasadoCódigo Capítulo4. EntregandoValor
Há,porém,umsegundotipodetestequeérealizadomanualmente,conhecido
comotestesexploratórios.Elesseaproveitamdetodosopotencialdotestadorpara
investigaredescobrircenários,epossivelmentedefeitosouefeitoscolaterais,que
nãohaviamsidoprevistosanteriormente.
Paraestetipodetestesnãoháumscriptpreestabelecidoeotestadorvaimuito
alémdoóbviocriandoeadaptandosuaabordagemaolongodoprocesso.
LidandocomCódigoLegadosemCoberturadeTestes
Émuitocomumqueumaequipequenãotrabalhavacommétodoságeisepassa
porumatransiçãosedeparecomumprojetoparaevoluirquenãopossuitestesau-
tomizadosporquenaculturaanteriortestareautomatizarnãoeraumapráticadis-
seminadadentreosmembrosdotime.
Fazeralteraçõesemumsistemaquenãopossuiumbomconjuntodetestesau-
tomizadosémuitodifícil.Omaiorriscoéquevocêpodefacilmentequebraralguma
funcionalidadesemqueninguémperceba.
PorissoMichaelFeathersemuitosoutrosagilistasconsideramquecódigosem
coberturadetestesécódigolegado,nãoimportasefoiescritooitoanosouoitohoras
atrás[24].
Umadasop çõesparamudaressacenárioémelhoraracoberturadetestespouco
apoucoacadaiteração.Paraisso,HenrikKnibergsugereoseguinteprocesso[35]:
1) Listeseuscasosdetestes.
2) Classifiquecadatesteporrisco,ocustodesetestarmanualmenteeoesfor çopara
automatizaroteste(vejanafigura 4.3.
3) Ordeneporprioridade.
4) Automatizealgunstestesacadaiteração,come çandopeloscasosdemaiorprio-
ridade.
73

## Página 88

4.2. SimplificandooCódigocomRefatoração CasadoCódigo
Figura4.3:ListadeCasosdeTeste
Umaveztendoalistaprontaeclassificadaépossívelpriorizarecome çarpe-
lostestescujafaltaapresentamaiorrisco,equepossuemmaiorcustoderealizaç ão
manualemenorcustodeautomação.
Quandonãosetemtestesautomatizadosaúnicaformadegarantirqueumaal-
teraçãonãoquebrouumafuncionalidadepreexistenteérealizandotestesmanuais.
Nãoéincomumqueocustoderealizarostestesmanualmentesejamaiordoqueo
custodeautomatizar,porissopodeserinteressanteestimareapresentaraosinte-
ressadosnoprojetoparaquepossamentenderocustobenefíciodoinvestimentona
automaçãodeles.
Nemsempretemosaoportunidadedetrabalharemnovosprojetosemquepo-
demosgarantiraltacoberturadetestedesdeoprincípiomasissonãoémotivopara
desanimar;poucoapouco,iteraçãoaiteraçãoépossívelmudararealidadedopro-
jetoemelhoraraqualidade,aumentandoacoberturadetestes.
4.2 Simplificando oCódigo com Refatoração
Complicar é fácil. Difícil é simplificar
–MaxGehringer
Énaturalqueaolongodotempoabasedecódigodeumsistemavásetornando
74

## Página 89

CasadoCódigo Capítulo4. EntregandoValor
cadavezmaior,assimcomoonúmerodefuncionalidadesdisponíveiseacomplexi-
dadedocódigofonte.
Semboaspráticasparamanterocódigolimpoeorganizado,àmedidaquemais
códigovaisendoacrescentado,maisdesorganizadoedifícildesecompreendero
repositóriovaisetornando. Issoimpactanegativamentenaprodutividadedosde-
senvolvedoresqueencontrarãomaisdificuldadeemdarmanuten çãonasfunciona-
lidadesexistenteseemadicionarnovasfuncionalidades.
Qualquer idiota pode escrever código que um computador pode entender. Bons
programadores escrevem código que seres humanos podem entender.
–MartinFowler
Refatoraréalteraraestruturadocódigosemalteraroseucomportamento. É
umapráticaquepermitequeodesenvolvedormelhoreodesigndocódigo,tornando-
omaislimpoefácildesecompreender.Éumatécnicaessencialparaprevenirqueo
códigosedeteriore[20].
Masparaqueodesenvolvedorpossaalterarocódigocomseguran çadequeo
comportamentonãoseráalterado,éessencialqueocódigopossuaumaboabasede
testesqueatuemcomoumarededeseguran çaprevenindoqueocomportamento
dosoftwarepercaaconsistência. Porisso,escrevertesteserefatorarsãotécnicas
que,geralmente,sãoutilizadasemconjuntoeéexatamenteporissoqueambassão
utilizadasnodesenvolvimentoguiadoportestes,conformeestudaremosaseguir.
Umbomdesignevoluiaolongodavidadeumsistema,masPoppendieckafirma
queumbomdesignnãoaconteceporacidente. Porisso,aoencontraralgoerrado
nabasedocódigo,éprecisoparardeincluirnovoscomportamentosaosoftwaree
resolveroproblema.
Paragarantirumaboaqualidadedecódigoéprecisorefatorar. Àmedidaque
novoscomportamentossãoincluídosnosoftware,porconsequênciaaumentandoa
complexidade,existeumagrandetendênciadeseescrevercódigoduplicadoetorná-
lomaisdifícildecompreenderededarmanuten ção.
Poroutrolado,éprecisotomarcuidadoparanãocairemumperfeccionismo
extremoegastartempotentandoaperfeiçoardetalhessemimportância.Parafacili-
taraidentificaçãodomomentocorretopararealizararefatoraç ão,Poppendieckcita
cincocaracterísticasdeumsistemaíntegro.Sequalquerumadestasestiverfaltando,
ésinaldequeéhoraderefatorar.Sãoelas:
1. Simplicidade: Namaioriadasvezesumdesignsimpleséomelhordesign.
75

## Página 90

4.3. CódigoLimpo CasadoCódigo
DesignPatterns,quandobemaplicados,sãoumaótimaferramentaparaaplicarso-
luçõessimplesaproblemascomplexos;
2.Clareza:Ocódigofontedeveserfacilmentecompreendidoportodososmem-
brosdaequipe. Todososelementosdocódigodevemserdevidamentenomeados
paraquesejamfacilmentecompreendidosportodos;
3.Eficácia:Umbomdesigndeveproduziroresultadocorreto,istoé,deveatingir
oobjetivopeloqualfoicriado;
4.Semrepetição:Omesmocódigonãodeveexistiremdoislugaresdiferentes.
Quandoumamudan çaprecisaserfeitaemmuitoslugaresoriscodedefeitoscresce
exponencialmente;
5.Utilidade:Todafuncionalidadedeumsistemaprecisaserútilparaseususuá-
rios. Quandoumafuncionalidadedeixadesernecessária,cria-sedesperdícioem
mantê-la;emmuitoscasosémelhoreliminá-la.
4.3 CódigoLimpo
RobertC.Martin,umdoscriadoresdoManifestoÁgil,conhecidonacomunidade
comoUncleBob,defendecomafincoaideiadeque,aolongodotempo,abasede
códigodeumprojetovaisetornandomaisbagun çada,edifícildeseentender,im-
pactandofortementenaprodutividadedaequipe,quetendeazero,ouseja,aponto
deemumdeterminadomomentoaequipenãoconseguirmaisevoluireincluirno-
vasfuncionalidadesnosoftware[41].
Defato,muitossoftwares,chegamaumtalpontoqueprecisamserreescritosdo
zeroparaquepossamcontinuaraserevoluídos.
Algumascaracterísticasdecódigolimposão:
• Elegante,fácildesecompreender,eagradáveldeseler.
• Simplesedireto.
• Segueprincípiosdeprogramação.
• Semduplicidade.
• Bemtestado.
• Parâmetros,Métodos,Funções,ClasseseVariáveispossuemnomessignifica-
tivos.
76

## Página 91

CasadoCódigo Capítulo4. EntregandoValor
• Códigoéautoexplicativo(semnecessidadedecomentáriosparacompreender
ocódigo).
• Códigobemformatado(épossívellerocódigosemprecisarutilizarabarra
derolagem).
• MétodoseClassesdevemterumaúnicaresponsabilidade(princípiodares-
ponsabilidadeúnica).
Trabalharparamanterocódigosemprelimpoé,alémdeumaatitudeprofissional
dodesenvolvedor,muitoeficienteemtermosdecustosparaaorganizaç ão,umavez
queamantenabilidadedosoftwareserásustentávelamédioelongoprazo.
ParaUncleBob,desenvolvedoresprofissionaisescrevemcódigocomoprofissio-
nais,ecódigoescritoporprofissionaisécódigolimpo!
4.4 PropriedadeColetiv a doCódigo
APropriedadeColetivadoCódigoéumadaspráticasdeXPeconsistenaideiade
queotimeéresponsávelportodoorepositóriodecódigoemvezdeosindivíduos
seremresponsáveisapenaspelocódigoqueelesmesmosescreveram.
Essapráticafazcomquemanteregarantiraqualidadedocódigosejaresponsa-
bilidadedetodososmembrosdotime.Qualquerumpoderealizarasalteraçõesque
foremnecessáriasemqualquerpartedosistema[66].
Nessaabordagem,quandoumdesenvolvedorprecisaralterardeterminadaparte
docódigo,nãoprecisarápedirpermissãoparaodesenvolvedorqueoescreveueterá
totalautonomiadefazeroqueprecisaserfeito.
Essapráticafuncionamuitomelhorquandoemconjuntocomrevisõesdecó-
digo,programaçãoempareintegraç ãocontínua. Alémdemelhoraraqualidade,
tambémajudanaeliminaçãodeilhasdeconhecimento.
Vocêjáviuumasituaçãoemquedeterminadapartedeumprojetoprecisaser
alteradamasaúnicapessoadotimequeescreveu,compreendeeconheceaquele
códigoestádeférias?Estapessoaéumilhadeconhecimento,eessasituaçãoénociva
paraoprojeto,porquesecriaumadependênciamuitograndeemumaúnicapessoa,
oquepossivelmentetambémresultaráemgargalosesobrecarga.
CódigoColetivoéumaboavacinacontrailhasdeconhecimento,ereduzorisco
sealguém,poralgumarazão,deixaroprojeto.
77

## Página 92

4.5. Linguagemubíqua CasadoCódigo
Nessaabordagemdepropriedadedecódigo,seumdesenvolvedorencontrarum
códigopoucoclaro,semtestes,ouforadospadrõesequalidade,nãoimportaquem
oescreveu,essecódigopoderáedeverásermelhorado.
4.5 Linguagem ubíqua
Desenvolvedor:-“NósestamoscomumproblemanoNFBusinessDelegatequando
enviamosoobjetoparaoService,parecequeatransaç ãonãoéiniciadaeoDAOe,
então,nãofuncionabem.”
Cliente:-?
Desenvolvedoresdevemfalaralinguagemdenegócio[66].
Umdosgrandesdesafiosdodesenvolvimentodesoftwareé,muitasvezes,aco-
municaçãoentredesenvolvedoresquenãosão experts no domínio (áreas de
negócio) do software com os expertsdonegócio.[66].
EmseulivroDomain-drivendesign(DDD),EricEvanscunhouotermoLingua-
gemUbíquaquedizrespeitoàcriaç ãodeumalinguagemcomumentreexpertsno
negócioeotimededesenvolvimentodesoftware.Dessaforma,essamesmalingua-
gemdenegócioéutilizadanoprópriocódigofontedosoftware,nahoradarnomes
aparâmetros,métodos,variáveis,classes,testes,etc.
Éimportantequeotimecompreendacadaumdostermosutilizadosporclien-
tes.Écomumqueosexpertsdonegóciotenhamseusprópriosjargões,assimcomo
desenvolvedoresetestadorestambémtêmseuspróprios.Emumprojetosemuma
linguagemcomum,otempotodo,desenvolvedoresprecisamtraduzirseustermos
paraoexpertdenegócio,assimcomoessetambémtêmquetraduzirseustermos
paraosdesenvolvedores,eissoprejudicaacomunicaç ão[23].
Comumalinguagemcomumalinguagemdasdiscussõesedoplanejamentoserá
amesmautilizadanocódigo.Se,emumsistemadelogística,porexemplo,ocliente
serefereacargas,osdesenvolvedores,nocódigofonte,utilizarãoomesmootermo
cargas,emercadorias,ouprodutos,oulote,porexemplo.
Oprimeiropassoparamelhoraracomunicaç ãoéreconhecerasuafragilidade,
ealinguagemubíquaéumaexcelenteferramentaparaajudarvocêesuaequipease
comunicaremmelhorcomaspessoasdenegócioenvolvidasemseuprojeto.
4.6 D esignÁ gil éDesignIterativo
Umdosmaioreserrosdodesenvolvimentoemcascataéacharqueoconhecimento
existeapenasnaformaderequisitoslevantadosantesdoiníciodaimplementaç ãoe
78

## Página 93

CasadoCódigo Capítulo4. EntregandoValor
separadosdodesenvolvimento.
Emumaperspectivaágil,odesenvolvimentodesoftwareéumprocessodecria-
çãodeconhecimento,equenaprática,odesigndetalhadodeumsoftwareocorreso-
mentenacodificação.Umdesignprematuro,ousejarealizadoantesdacodificaç ão,
nãopodepreveracomplexidadeencontradaduranteaimplementaç ão,etampouco
podeutilizar-sedofeedbackquesópodeserrecebidoaolongododesenvolvimento.
Odesigndeumsoftwaredeveevoluiraolongodeseudesenvolvimento.Tentar
fixá-loprematuramenteresultaráemdesperdício.
Emsetratandoderequisitos,deve-seseguiramesmalinhadepensamento,de
formaqueosrequisitosdevemserdetalhadosapenasquandoestiverempertoda
horadedesenvolvê-los. Éimportantetambémestarpreparadoparaasprováveis
mudançasneles,umavezqueoclientetambémestáaprendendoeevoluindosuas
ideiasarespeitodasoluçãoqueestásendodesenvolvida.
Asabordagensprematurasdelevantamentoderequisitosededesignsãochama-
das,respectivamente,deBigRequirementsUpFront(BRUP)eBigDesignUpFront
(BDUF),etêmsidoamplamenteabordadasnacomunidadeágilcomopráticasase-
remevitadas,poisoconhecimentonãoégeradoporantecipaç ão,massimatravés
deexperimentação,codificaçãoe releasesfrequentesquepermitemreceberfeedback
dosclientes.Odesenvolvimentodesoftwareiterativoeincrementalencaixa-seper-
feitamentenessalinhadepensamento.
YAGNI:Você não v ai precisar disso...
“Não pague o preço da complexidade a menos que você realmente precise. ”
–NealFord
OprincípioYAGNI(Y ou Ain’t Gonna Need ItouVocênãovaiprecisar
disso)muitodisseminadonacomunidadeágil,defendeaideiadeque
vocêdeveevitarespeculaçõesnodesenvolvimentodesoftware[25].
Issoocorrenaquelassituaçõesemquesepensa“Euachoquevamos
precisardissonofuturo,então,vouaproveitarejáfazer”. Dessaforma,
adiciona-se complexidade desnecessariamente no projeto, e, quando
maiscomplexidade,maisdifícildesealterartorna-seosoftware.
Procurefazerapenasaquiloquerealmenteéprecisoagora!
79

## Página 94

4.7. DefinindoosignificadodePronto CasadoCódigo
4.7 Definindo o significado dePronto
ADefiniçãodePronto(eminglêsDefinitionofDone,referenciadocomoacrônimo
DoD),é,basicamente,um checklistdoquedeveserfeitoantesqueumahistória
possaserconsideradapotencialmenteentregável.
Nãoháum checklistoficialquedevaserusadoportodasasequipeságeisdo
mundo, porque, considerandoacomplexidadedodesenvolvimentodesoftware,
cadaequipeéúnicaeestáresolvendoumproblemadentrodeumcontextoúnico.
Porisso,cadaequipedeverádescobriroquedevefazerpartedesuadefiniç ãode
prontodeacordocomseucontextoouseja,levandoemconsideraç ãoanaturezado
produto,atecnologiaqueestásendoutilizada,asnecessidadesdosusuáriosetc.
Algunsitenscomunssão:
• Códigorefatorado.
• Códigodentrodospadrõesdecodificação.
• Códigorevisadooufeitoempar.
• Códigointegradonosistemadecontroledeversão.
• Documentaçãodearquiteturaatualizada.
• Testesdeunidaderealizados.
• Testesdeaceitaçãorealizados.
• Testesexploratóriosrealizados.
• Nenhumdefeitoconhecidopendente.
• POaceitounahistória.
• ManualdoUsuárioatualizado.
Éimportantequeessadefiniçãosejaescritaequefiquedisponívelevisívelpara
todos.Issoevitaque,porexemplo,umahistóriadeusuáriosejadadacomopronta,
masadocumentaçãoparaousuáriofinalnãotenhasidoescritaainda,eque,então,
essetrabalhopendentesejaempurradodeumaiteraç ãoparaaoutra,porémnãoseja
consideradonasestimativasfazendocomqueumfalsosensodebaixaprodutividade
permeieoambiente.
80

## Página 95

CasadoCódigo Capítulo4. EntregandoValor
Alémdisso,adefiniçãotambéméimportanteparaquehajaummesmoenten-
dimentodosignificadodeprontoparatodososmembrosdotime,eparaquenada
deimportantesejaesquecidooudeixadodelado.
Amesmaideiapodeseraplicadaparaalémdashistóriasdeusuários:também
paraiteraçõesereleases.Geralmente,entende-sequeumaiteraçãoestáprontaaofim
deumintervalodetempopredefinido,maspodeserinteressantequedeterminadas
atividadessejamrealizadasantesdesedarumaiteraç ãocomopronta,comopor
exemplofazer deployemumservidordehomologaçãooualgodotipo.
AparticipaçãodoPO,naconstruçãodessadefiniçãoémuitoimportante,uma
vezqueeleconhecemelhordoqueninguémasexpectativasdocliente.
Adefiniçãodeprontonãodeveserestática,aocontráriodisso,énaturalque,à
medidaqueotimeforevoluindoeamadurecendo,adefiniç ãodeprontosejaalterada
paraatendercritériosdemaisemaisqualidade[59].
4.8 Integração Contínua
Énaturalqueemumprojetodedesenvolvimentodesoftwareosdesenvolvedores
dotimetrabalhememparalelonodesenvolvimentodefuncionalidadesecorre ções.
Muitasvezes,podemacabarporalterarasmesmosarquivosgerandoconflitos,ou
atémesmo,alterararquivosdiferentes,quedepoisdecombinadasasalterações,o
softwareapresenteumcomportamentoinadequado.Dequalquerforma,detempos
emtempos,asalteraçõesprecisarãoserintegradasemumabasecomumdecódigo.
Oprocessodeintegração,geralmente,évistopordesenvolvedorescomoalgo
custosoedemorado:aspe çasfuncionambemquandoseparadas,porém,paratentar
uni-lasefazê-lastrabalharemconjuntoocenáriosetornamaiscomplicado.
Manterocódigosempreintegradoeprontoparaserentregueéumgrandede-
safio,eessaéumadasfinalidadesdaintegraç ãocontínua. Aideiadaintegração
contínuaéquetodososdesenvolvedoresrealizemintegração,issoé,sincronizemo
códigofonteproduzidocomosistemadecontroledeversão,amaiorquantidadede
vezespossívelaolongododia.
Érecomendadoqueacadaintegraç ãotodosostestesdeunidadesejamexecu-
tadosparaassegurarqueo buildnãosejaquebradoequetudoestáfuncionando
corretamente.
Chamamosde build(construção)oprocessodegerarumpacoteexecutávelde
software.Issoincluiacompilaçãodecódigofontee,alémdisso,pode-seacoplaruma
sériedeoutrosprocessosparagarantirqueopacoteestáemboascondições,como
81

## Página 96

4.9. ProgramaçãoemPar CasadoCódigo
análiseestáticadecódigo,verificaçãodepadrõesdecodifica ção,execuçãodetestes
automatizados,etc. Algunsexemplosdeferramentasdebuildsão: make,Gradle,
ant,maveneBuildR.
Seosoftwarepossuirumbomníveldecoberturadetestes,eostestesforem
bemescritos,essapráticapodereduzirconsideravelmenteonúmerodedefeitosem
produçãoegarantirqueocódigofonteproduzidoparaimplementarnovasfuncio-
nalidadesnãofezcomquealgodeixassedefuncionarcomodeveria.
Existemdiversasferramentas,naverdadeservidoresdeintegraç ãocontínua—
inclusivealgunssãodeusolivreeopen-source—quepodemajudarnaintegraç ão
contínua.
Épossívelconfiguraressasferramentasparaquecadavezquealgumdesenvol-
vedorenviaralgumnovocódigofonteparaosistemadecontroledeversão,todos
ostestessejamexecutadoseodesenvolvedorrecebaumanotificaç ãocasoo build
tenhasidoquebradoporque,porexemplo,algumtestetenhafalhado.
Muitosservidoresdeintegraçãocontínuatambémpossuemextensõesqueper-
mitemquesejamgeradosrelatóriosdecoberturadetestes,identificaç ãodedefeitos
óbviosnocódigo(atravésdeferramentasdeanáliseestática),entreoutrascoisasin-
teressantes.
Sevocêaindanãousanenhumaferramenta,eusugiroquecomeceverificandoo
Jenkins(jenkins-ci.org)eoCruiseControl(cruisecontrol.sourceforge.net).
4.9 P rogramação em Par
Aprogramaçãoemparéumatécnicanaqualdoisprogramadorestrabalhamem
ummesmoproblema,aomesmotempoeemummesmocomputador. Enquanto
umapessoa(ocondutor)assumeotecladoedigitaoscomandosquefarãopartedo
programa,aoutra(onavegador)aacompanhafazendoumtrabalhodeestratégia
[60].
Arevisãodecódigo,naprogramaçãoempar,aconteceemtemporeal.Enquanto
umdesenvolvedorestácodificando,ooutroestárevisandoocódigo.Pequenoser-
ros,quepoderiamserextramentedifíceisdesecorrigirposteriormente,podemser
facilmenteidentificadosecorrigidosnessemomento.
Osantigosjádiziamque“duascabeçassãomelhoresdoqueuma”,eaprograma-
çãotambémsebeneficiadisso.Doisdesenvolvedorescomumconjuntodeconheci-
mentoeexperiênciadistintossão,emregrageral,capazesderesolverumproblema
82

## Página 97

CasadoCódigo Capítulo4. EntregandoValor
deformamuitomaiseficientedoquepoderiamfazerseestivessemtrabalhandoso-
zinhos.Éoprincípiodasinergiaaplicadoàprogramaç ão.
Emumprimeiroolhar,pode-sepensarqueaprogramaç ãoemparéumatécnica
quereduzaprodutividadedaequipe,equeseambososdesenvolvedoresestivessem
trabalhandoemparaleloresolveriamumdeterminadoproblemamaisrapidamente
doquetrabalhandojuntos.
Aprogramaçãoemparéapráticadedesenvolvimentoágildesoftwarecommais
estudoscientíficosrealizadosnaAcademiaatéagora,ealgunsdessesestudosde-
monstramque,naprática,aprogramaçãoemparnãoapresentagrandesdiferen ças
deprodutividade[67],eque,emgeral,oprodutoéentreguecommenosdefeitose
commelhorqualidade,issosignificaquemenostemposerádesperdiç adoemcorre-
çõesdedefeitosequeafuturamanuten çãodosoftwareserámaisfácil,ouseja,em
umaanálisedemédioprazo,podemosconcluirqueaprogramaçãoemparé,defato,
eficiente.
Umdosfatoresqueapoiamessaaltaprodutividadeépressãodospares.Nestes
temposderedessociais,e-mail,SMS,ediversasoutrasdistrações,umdesenvolvedor
podefacilmenteperderofocoesedistrairquandotrabalhasozinho.
Trabalhandoempar,odesenvolvedorassumeumcompromissocomseucolega
reduzindoassimadistraçãoeaperdadefoco,ecomoháumcolegaacompanhando
acodificação,háumpreocupaçãomaioremcriarsoluçõescommaisqualidadee
elegância.
ProgramaçãoemPareAprendizado
“ Aprender é a única coisa de que a mente nunca se cansa, nunca tem medo e nunca se
arrepende. ”
–LeonardodaVinci
Trabalhandoempar,oconhecimentodotimeserárapidamentedisseminadoen-
treosmembrosdotimeajudandonaeliminaç ãodeilhasdeconhecimento.Paraque
issoaconteçadeformaeficiente,éimportantequehajaumrevezamentoconstante
entreospares,deformaquetodostenhamoportunidadesdetrabalharcomtodos.
83

## Página 98

4.9. ProgramaçãoemPar CasadoCódigo
AP irâmide dos Pares
Umaferramentainteressanteparaincentivarorevezamentoentreos
paresetonarvisivelquemestápareandocomquemaolongodeuma
iteraçãoéaPirâmidedosParesouPair-amid[44].
Trata-sebasicamentedeumamatrizquecruzatodososmembrosdo
time,edesconsideraoscruzamentosrepetidoseoscruzamentosdein-
divíduocomelemesmo,vejanafigura 4.4.
Figura4.4:PirâmidedosPares
Noexemploacima,podemosverqueatéagoraoRobsoneoLuiz
numcaparearam,masqueoRobsonpareou3vezescomAlineevezes
comaCarol.
Seapirâmidedosparesficarvisívelnoquadrodotime,tornar-se-
áumaferramentaútilparaincentivaraprogramaç ãoempareoreve-
zamentodosparesresultandoemmaiorcompartilhamentodeconheci-
mentoentreosmembrosdotime.
Aprogramaçãoemparcriaumespaçoparaaprendizadocontínuodentroda
equipe[60]. Otrabalhoempartambémpodesermaiseficienteparadisseminar
conhecimentodoquedocumentaçõesumavezquenãoselimitaaoqueestáescrito
eporquehátrocadeconhecimentoentreambasaspartes.
Éimportante,porém,diferenciarprogramaçãoepardementoria[1],arelaç ão
daprogramaçãonãoédeestudanteeprofessor,masemvezdisso,éumrelaç ãode
84

## Página 99

CasadoCódigo Capítulo4. EntregandoValor
duaspessoastrabalhandojuntas. Seháumadiferen çamuitoelevadanonívelde
conhecimentodedoisprofissionaistrabalhandoempar,provavelmenteoquevai
aconteceréqueumdelesiráensinarooutronamaioriatempo,criandoassimuma
relaçãoquecaracterizariamaismentoriadoquecomprogramaç ãoempar.
Amentoriaétambém,semdúvida,umapráticamuitoválidaeimportanteem
umaequipededesenvolvimentodesoftware,maséimportantesepararumconceito
dooutro,eestarcientedequeamentoria,geralmente,nãoresultanamesmapro-
dutividadedaprogramaçãoempar,eque,muitasvezes,éuminvestimentomaisde
longoprazocomparadocomaprogramaçãoempar.
Emsuma,osprincipaisbenéficosdaprogramaçãosãomelhorqualidade,equipe
maismotivada, maisconfiançaetrabalhoemequipe, disseminaçãodeconheci-
mento,eaprendizadocontínuo[33].
Mito:S emProgramação em Par, não há Agilidade
MartinFowler,umadaspersonalidadesmaisrespeitadasnomundo
dodesenvolvimentodesoftware,escreveuumartigoem2006levantando
algunsdosprincipaisenganossobreprogramaçãoempar.
Fowleresclareceemseuartigoque“nãoénecessárioprogramarem
parparaestarpraticandoumprocessoágil”[29],nemmesmosepodedi-
zerqueparaaplicarExtremeProgrammingvocêéobrigadoaprogramar
empar. Omáximoquesepodedizeréquealguémquequeraprender
XPdevetentarprogramarempareversefuncionaemseucasoempar-
ticular.
Aprogramaçãoemparnãoénemmesmocitadanomanifestoágil,
porém,éumapráticaaltamenterecomendadaparaquesealcanceos
princípioságeis.
4.10 Revisão de Código
Arevisãodecódigoconsisteemumoumaisdesenvolvedoresleremocódigofonte
comoobjetivodeasseguraraqualidadedocódigoeaprendernoprocesso.Especi-
almentenaimplementaçãodehistóriasquenãoforamdesenvolvidascomprogra-
maçãoempar,recomenda-se,apráticaderevisãodecódigo.
Arevisãodecódigomelhorasuaqualidadeereduzataxadedefeitos[31]. As
revisõessãooportunidadesnãoapenasdeseprevenirerrosnocódigo,mastambém
85

## Página 100

4.11. DívidaTécnica CasadoCódigo
decompartilharedisseminaroconhecimentoentreosintegrantesdotime.Aorevi-
sarocódigoalguémpodedescobrirboaspráticasquenãoconhecia,ou,emcasode
encontraralgumamápratica,entãopassaaserumaboaoportunidadedediscutir
sobreformasmelhoresdesolucionaroproblemaemquestão.
Paraqueasrevisõesdecódigosejamdefatoconstrutivasparaotime,éimpor-
tantemanterumaatitudedetrabalhoemequipequandoumproblemaforencon-
tradoeevitarencontrarculpadosoudebochardaquelequecometeuoerro.
Emumambienteágil,parte-sedoprincípiodequetodosestãofazendooseu
melhor,então,seeventualmenteumproblemaforencontrado,procuresecertificar
dequetodossaibamcomoevitarqueoproblemavolteaocorrer,esigaemfrente.
Asrevisõesdecódigotantopodemfazerpartedadefiniç ãodeprontoe,conse-
quentemente,doprocesso,comopodemseresporádicas,sendorealizadasdetem-
posemtempos. Emalgumasequipesumdesenvolvedorrevisaocódigodeoutro,
emoutrasequipes,arevisãoécoletivaenvolvendováriaspessoas.
Algumasorganizaçõesfazemumamesclaentreprogramaçãoemparerevisãode
código,deformaquetudooquenãofordesenvolvidoempares,érevisado.Nãohá
fórmulasecretaparaisso,éinteressantetestardiversosmétodoseencontraraquele
quefuncionamelhornocontextodesuaequipe.
4.11 DívidaTécnica
Imaginequevocêéumdesenvolvedordesoftwarequeestátrabalhandoemumsis-
temadetransferênciasbancárias. Vocêestáfazendoumaalteraçãoque,teorica-
mente,seriamuitosimples,maspercebequeodesignatualdosistemaprecisaria
sofreralgumasalteraçõesparaquefossepossívelcriartestesdeunidadeparaaalte-
raçãoqueestáfazendo.
Você,agora,precisatomarumadecisão:fazerumtrabalho“rápidoesujo”para
resolveroproblemarapidamente,masdeixandoocódigosemtestes,ourefatorare
alteraro designparaquesejapossívelescrevertestesdeunidade.
Desenvolvedoresprecisamtomardecisõescomoessasdiariamentee,acada“tra-
balhorápidoesujo”quefazem,aumentamadívidatécnicadoprojeto.
DívidatécnicaéumametáforacriadaporWardCunninghamqueilustraascon-
sequênciasdessestrade-offs.Aideiabásicaportrásdotermoéquediminuiraqua-
lidadeaumentaotempodedesenvolvimentoalongoprazo.
ParaCunningham,dividatécnicaincluicoisasquevocêescolhenãofazeragora,
masqueimpediráodesenvolvimentofuturosedeixadodelado[21]. Issoinclui,
86

## Página 101

CasadoCódigo Capítulo4. EntregandoValor
protelaçãoderefatoração,masnãoincluiprotelaçãodefuncionalidade,anãoemser
casosqueaentregafoi“boaosuficiente”porémnãosatisfazalgumtipodepadrão
dedesenvolvimento.
DívidaTécnica ouDébitoTécnico
Noconteúdosobremétodoágeisdacomunidadebrasileira, espe-
cialmenteemblogs,encontra-semuitootermo“débitotécnico”,mas
entende-seque“dívida”éumatraduçãomaiscorretapara debt.Emin-
glêsapalavradebtquerdizerdívida(umvalorquenãofoipagoedeverá
serpagofuturamente),jáapalavra debitsignificadébito(umvalorque
foiretiradodeumacontabancária,porexemplo).
DepoisdadefiniçãodeCunninghamnoiníciodosanos90,acomunidadecon-
tinuouaevoluiroconceito[53]e,atualmente,diversos“atalhos”taiscomodesign
ultrapassado,defeitosconhecidosquenãoforamresolvidos,baixacoberturadetes-
tesdeunidade,excessodetestesmanuais,entreoutros,tambémsãoconsiderados
partedadívidatécnica.
Seelaforignorada,emalgummomentoocódigopodesetornartãoconfusoe
caóticoquesuamanuten çãoseráprejudicada,aumentandoocustodedesenvolvi-
mentoesuporte,diminuindoaprodutividadedotime,aumentandoonúmerode
defeitosdevidoàaltacomplexidadeedificuldadedecompreensãodocódigo,efi-
nalmentediminuindoamotivaçãodaequipe,devidoàbaixaprodutividadeealto
númerodedefeitos.Éprevisívelque,emnumcenáriocomoesse,osclienteseusuá-
rios,provavelmente,tambémnãoestarãomuitoscontentes.
Ovalordametáforadadívidatécnicaestáemtornarotimeconscientedesses
problemasedecomoaprodutividadepodeestarsendoafetada.Seotimefizerum
acompanhamentodadívidatécnica,épossívelevitarqueelasetornecadavezmaior
e,emvezdisso,trabalharparapagá-lapoucoapouco.
Éimportantequeaequipemantenhaumbacklogdedívidatécnica,ouseja,uma
listadetarefasquepodemserrealizadasparamelhorarocódigo,eessalistapodeser
priorizadapelotimee,então,pode-senegociarcomo Product Ownerparaquepouco
apouco,essesitenssejamincluídosnasiterações.
Poderíamosteritenscomo“RefatorarMétodode2000linhasnaClassedeTrans-
ferênciaBancária”,ou“AtualizarBibliotecaPOIparaVersãomaisRecenteparaevitar
87

## Página 102

4.11. DívidaTécnica CasadoCódigo
VazamentodeMemória”,ou“AumentarCoberturadeTestesdoMódulodeEmprés-
timos”etc.
Algunstiposdedívidatécnicapodemserdeliberadamentedeixadosdelado,por
nãohavervaloremresolvê-los.Porexemplo,emcasosdeprodutospróximosaotér-
minodeseuclicodevida,oudeumprotótipocomobjetivoúnicodeaprendizagem,
ouprodutoscomciclosdevidamuitocurtos(comoprojetosparacampanhasde
marketingpontuais,porexemplo). Éimportantequeotimefoquenaquiloquede
fatotrarábenefíciosparaaprodutividadedotimeequalidadedoproduto.
Eentão? Seutimeestáprontoparapagarsuasdívidas? Lembre-sequeassim
comonasdívidasfinanceiras,quantomaistempolevamosparapagar,maisdifícil,
porquepaga-secomjuros.
Nada deJanelasQuebradas
Pesquisasnocampodecriminalidadeedecadênciaurbana,descobri-
ramqueumajanelaquebradapoderapidamentelevarumprédiolimpo
eintactoasetornarumprédiodecadenteeabandonado[68].
ATeoriadaJanelaQuebradaafirmaqueumajanelaquebrada,senão
consertadaporalgumtempo,transmiteparaaspessoasumsensoque
ninguémseimportacomoprédio[61].Então,derepente,outrajanelaé
quebrada,lixoseacumula,paredessãopichadas,empoucotempoopré-
dioficatãoprejudicadoqueodonojánãoconseguemaisrepará-lo,então
oqueanteseraapenasumsensodeabandono,agorasetornarealidade.
Damesmaforma,quandoumdesenvolvedordeixaumcódigosem
coberturatestes,porexemplo,opróximodesenvolvedortemessasen-
saçãoquenãohouvezeloporaquelecódigo,ecriaumnovométodo,
deixando-osemtestartambém.
Comotemposerápossívelnotarumagrandequedanacoberturade
testes,tantoquetalvezsetornemuitodifícilparaaequipereverteroce-
nário. Omesmopoderiavalerparacódigodeixadosemrefatorar,ou
qualqueroutramápráticadedesenvolvimento.
Quandoumajanelaédeixadaquebrada,outraseráquebrada,eoutra,
eoutra...Porisso,nãodeixejanelasquebradaseacharuma,enuncaseja
oprimeiroaquebrarumajanela.
88

## Página 103

CasadoCódigo Capítulo4. EntregandoValor
4.12 AgilidadeExplícita comMural dePráticas
“Nós somos aquilo que fazemos com frequência. Excelência, então, não é um ato, mas
um hábito”
–Aristóteles
Desculpe-me,maseutenhoquedizer:“Nãoéoquadronaparedequefazdasua
equipeumaequipeágil”.
OfilósofogregoAristótelesqueviveuhámaisde300A.C.járeconheciaquenós
somosfrutosdosnossoshábitos,dasnossasaçõesfrequenteseconstantes. Nessa
linhadepensamento,vocênãopodedizerqueéumapessoacaridosa,sóporque
umaveznavidafezumadoaç ãoparaumacausabeneficente,nãopodedizerqueé
umapessoaaventureirasequandotinha17anosdeidadepuloudebungeejumpno
parquedediversões.
Vocêtambémnãopodedizerquesuaequipeéágilsóporque1dos25desenvol-
vedoresdoseutime,umavez,tentouaplicardesenvolvimentoguiadoportestesem
seutempolivre,enempodedizerquesuaorganizaç ãotemumaculturadeapren-
dizagemsóporqueháumespaçoparapalestrasumaveznoano.Dejeitonenhum.
Aristótelessabiabemdoqueestavafalando.
Opontoéque“nóspodemosdizerquesomoságeisporquenósestamosfrequen-
tementeutilizandopráticaságeis”e“nóspodemosdizerquenossaorganizaçãotem
umaculturadeaprendizagemporqueestamosaprendendoalgonovotodososdias”.
Quanto mais eu treino, mais sorte eu tenho.
–TigerWoods
Aperguntaé:quaissãoaspráticasquefazemdenósumaequipeágil? Euma
ferramentamuitosimplesparaajudarasequipesasefazeremessaperguntacom
frequênciaéomural de práticas,queconsistebasicamenteemtornarexplícitasto-
dasaspráticasdeumaequipeatravésdepequenosíconesexpostosemumaáreado
quadrodaequipe(vejanafigura 4.5.
89

## Página 104

4.13. Eagora,oqueeufaçoamanhã? CasadoCódigo
Figura4.5:MuraldePráticas
Incluatodasaspráticasdoseutime,aquelasdasquevocêsseorgulhamedasque
nãoseorgulham,tornetudoexplícitoparaquepossamvisualizarediscutirfrequen-
tementeseelasaindafazemsentidoequandonovaspráticaspoderãoseracrescen-
tadas.
Vocêpodeinclusiveassociarmétricasacadaumadessaspráticasparaassegurar
queelasrealmentefazempartedodiaadiadotimeenãoestãonomuralapenasde
enfeite.
Lembre-se,nóssomosaquiloquefazemoscomfrequência. Oquevocêeseu
timeestãofazendocomfrequência,queostornamágeis?
4.13 Eagora, o que eu faço amanhã?
Seutimejápossuiumadefiniçãodeprontoparahistórias,iteraçõese releasesexplí-
citaevisívelparatodos. Aindanão? QuetalreunirotimeeoPOparapropore
discutirumadefinição?Sevocêsjápossuemdefiniçõesdepronto,façaumarevisão
everifiqueseelaestáatualizadaeseestá,defato,representandooestadodepronto
idealparaocontextodasuaequipe.
Reúnaotimeeidentifiqueaspráticaságeisquefazempartedodiaadiadotime,
construaummuraldepráticasetornetudoexplícito. Napróximaretrospectiva,
90

## Página 105

CasadoCódigo Capítulo4. EntregandoValor
discutacomotimeaspráticasatuais,setodaselasaindafazemsentido,equenovas
práticaspoderiamseracrescentadasparabenefíciodoprojetoedaequipe.
ReconheçaePaguesuasDívidasTécnicas:Reúnasuaequipe,efaç aumlevanta-
mentodadívidatécnicadoseuprojetoatual.Classesdifíceisdesecompreenderou
alterar,códigosemcoberturadetestes,gambiarrasdeixadasparatrásetc. Levante
tudoquepuder,eprocurefazerpriorizarjuntocomotimedeacordocomoquanto
cadaumdositensprejudicaaperformancedotime. LevealistaaoPO,enegocie
comeledequeformaessesitenspodemsersolucionadosaolongosdasiterações.
Suaequipetemumapolíticaparaprogramaç ãoempar? Tudoéfeitoempar?
Nadaéfeitopar?Define-seoqueseráounãofeitoemparnaReuniãoDiária?Que
talconversarcomequipesobreissoedefiniralgumacoisaparaapróximaiteraç ão?
Quetalproporumasessãoderevisãodecódigocomalgunsmembrosdoseu
time? DuranteasessãoapresenteaseutimealgunsdosconceitosdeCleanCode
vistosnessecapítulo.
Quaismétodosvocêsestãoutilizandoparaguiaroprocessodedesenvolvimento?
Seráquepodemincluiralgumaspráticasdeoutrosmétodosparaaprimoraropro-
cesso?
91

## Página 107

Capítulo5
OtimizandoValor
Esseéoterceironíveldefluêncianoqualaequipepassaaentregaraindamaisvalor
agregadoetorna-secapazdetomarmelhoresdecisõesparaosprodutosemdesen-
volvimento.
Nessemomentoaequipecompreendemuitobemoqueomercadoestápedindo,
assimcomoquaissãoasnecessidadesdenegócio,ecomosatisfazê-las.
Agora,aequipe,apresentaseusresultadosatravésdemétricasconcretasdene-
góciocomoROI(RetornosobreoInvestimento),MargemdeLucroLíquidopor
Colaborador,SatisfaçãodoClienteetc[57].
LarseyeShoreafirmamqueparaseatingiresseníveldefluênciaaequipepre-
cisarádemembrosespecializadosemnegóciotrabalhandoemtempointegralcomo
partedaequipe(analistasdenegócio,gerentesdeproduto,vendedores,publicitários,
entreoutrosdeacordocomodomíniodenegóciodoprodutoemdesenvolvimento).
5.1 Direcionando aEquipe
“Para quem não sabe para onde vai, qualquer caminho serve. ”

## Página 108

5.1. DirecionandoaEquipe CasadoCódigo
–LewisCarroll,AlicenoPaisdasMaravilhas
Definiravisão,ospropósitos,objetivosemetasdaorganizaç ãoedoprojetoem
queotimeestátrabalhandoéumaótimaformademostraratodosadire çãopara
qualdevemjuntoslevaraorganizaç ãoatravésdotrabalhorealizadonodiaadia.
Tudoissosãoferramentasparauniredirecionaraspessoascomalgumasmudan ças
sutisemtermosdeabrangênciaefoco.Nósvamosignoraressassutilezasenosreferir
apenasametas.
Umadiferençacrucialentresmetastradicionaisemetaságeiséqueascaracterís-
ticasecritériosparadefiniçãodaságeisnãosãofixas,masvariáveisdeacordocom
ocontexto[8].
Dependendodoobjetivofinal,algumasmetaspodemsermaisinspiradoras,ou
memoráveis,ouespecíficas,ouambiciosas,enfim,ascaracterísticasdametanãopre-
cisamatenderaumconjuntodecritérioscomoSMART(Específicas,Mensuráveis,
Atingíveis,Realistas,Tangíveis)porexemplo,paraquesejamúteisparaguiarotime.
AWikimedia,fundaçãoportrásdafamosaenciclopédiadigitalWikipedia,apre-
sentasuamissãocomo:“AmissãodaFundaçãoWikimediaéempoderareengajar
pessoaspelomundoparacoletaredesenvolverconteúdoeducacionalsobumali-
cençalivreounodomíniopúblico,eparadisseminá-loefetivamenteeglobalmente.”
[26],jásuavisãoé“Imagineummundoondecadaserhumanopossacompartilhar
livrementenasomadetodooconhecimento.Esseéonossocompromisso."[27].
NotequeambasdeumaformaoudeoutramostramexatamenteoqueaWi-
kimediaestáfazendo,enoqueseuscolaboresdevemconcentrarseusesfor çospara
conquistar.Esseéoponto.
Jamaisusemetasparaintimidaraspessoasouameaç á-las,emvezdisso,para
ajudá-lasaentenderoqueaorganizaçãoprecisaquefaçamnaqueledadomomento,
eparaquetodospossam“remarobarconamesmadire ção”.
Nãoassociemetasarecompensasfinanceiras,pesquisasapontamqueissopode
destruiracolaboraçãoetirarofocodaspessoasdoquerealmenteimporta[47],é
importantequearealizaçãodametasejaaprópriarecompensaparaotime.
Éimportantequeasmetassejamcomunicadasepermane çamsempreexplícitas
evisíveisparaotime.Dequevaleumametaseaspessoasqueprecisamrealizaro
trabalhoparaqueelassejamatingidasnãoaconhe çam?
Metassãoferramentas,ecomoqualqueroutraferramenta,podemserbemou
malutilizadas. Quandobemusadaspodemuniredirecionarotime,quandomal
usadaspodemdividiraspessoas,quebraracolaboraç ãoedesmotivar.
Façabomusodemetas!
94

## Página 109

CasadoCódigo Capítulo5. OtimizandoValor
5.2 MétricasÁ geis
“Tudo que pode ser contado não necessariamente conta; Tudo que conta não
necessariamente pode ser contado. ”
–AlbertEinstein
Métricaspodemserúteisparaajudarotimeacompreenderondeestão,eajudá-
losacompararcomoestadoemquequeremestar.Assimcomoasmetas,asmétricas
tambémdevemestarsempreexplícitasevisíveisparaotime.
OScrum,porexemplo,sugerequeasequipesutilizemburndownchartspara
quetodospossamterfeedbackdecomoestáoandamentodaiteraç ão(estadoatual)
emrelaçãoaoplanejamento(estadodesejado).
Nafigura5.1podemosverumexemplodeburndown,emqueaequipenãocon-
seguiuentregartudooquefoiplanejado.Oeixoverticalrepresentaototaldetraba-
lhopendente,nessecasopontosdehistóriadeusuário(poderiaserqualqueroutra
medidadetrabalhodependente),enquantooeixohorizontalrepresentaotempo,
nessecasodiasdasemana(poderiaserqualqueroutramedidadetempocomoite-
raçõesousemanas,porexemplo).
Figura5.1:BurndownChart
Notequenodia4háumadiferen çagrandeentreoidealeorealizadoe,éuma
boaoportunidadeparaqueotimepossadiscutirsobreoqueestáacontecendoe
tomaralgumaaçãoparaeventualmentemelhorareinvestirnosucessodaiteraç ão,
enquantoaindahátempo.
95

## Página 110

5.2. MétricasÁgeis CasadoCódigo
Noburndownchart,semprequealgumtrabalhoforconcluído,ográficocai,
quandootrabalhoéreestimado,ográficosobe,quandoalgumtrabalhoéacrescen-
tado,ográficosobe,equandoalgumtrabalhoéremovido,ográficodesce[19].
Umaalternativaaoburndownchart,éburnupchart,queemvezdedescerà
medidaqueotrabalhovaisendoconcluído,vaisubindo.Algunstimespreferemusar
oburnupporqueémaisfácildeexpressaralteraçõesdoescopo,comoporexemplo,
umamelhoriaoudefeitourgentequesurgiuaolongodeumaiteraç ão,comopode
servistonaFigura 5.2.
Figura5.2:BurnupChart
EquipesqueaplicamométodoKanban,geralmente,utilizamumgráficoseme-
lhanteaoburnupchart,porémdetalhadoporetapadoprocesso,permitindovisua-
lizaravariaçãodotrabalhoemprogressoaolongodotempo,trata-sedodiagrama
defluxocumulativo(eminglêsCumulativeFlowDiagramouCFD),vejanafigura
5.3.
96

## Página 111

CasadoCódigo Capítulo5. OtimizandoValor
Figura5.3:CumulativeFlowDiagram
ComoCFD,épossívelobservarexatamenteondeotrabalhoemprogressoestá,
equaisosgargalos.Observenafigura 5.3,quedepoisdasemana3aetapa“testando”
nãoparoudeaumentardetamanho,diminuindoasentregas(etapapronto). Isso
podeserumsinalqueostestessetornaramumgargaloequealgoprecisaserfeito
paratornaroprocessomaiseficiente,aumentandoo throughput(entregas).
Nagrandemaioriadasvezes,esseacumulodetrabalhoemdeterminadaetapado
processoéumsinaldequeénecessáriotrabalharoslimitesdetrabalhoemprogresso
conformeestudamosnase ção3.5.
Depoisdealgumasiteraçõesépossívelmedirtambémavelocidadedotimepor
iteração(totaldepontosentreguesporiteraç ão)eavelocidademédia,vejanafigura
5.4.
97

## Página 112

5.2. MétricasÁgeis CasadoCódigo
Figura5.4:GráficodeVelocidade
Avelocidade,oescopopendente/entregueeotrabalhoemprogressosãoasmé-
tricasmaisacompanhadasporequipeságeis,masnãosãoasúnicas.Porisso,agora
estudaremosostiposdemétricas,equaisoutraspodemtrazervisibilidadee feed-
backparaaequipeeosinteressadosnoprojeto.
TiposdeMétricas
JurgenAppeloeMikeCohnrecomendamqueseusedoistiposdeindicadores
[8][20]:IndicadoresIndutoreseIndicadoresdeResultado.
IndicadoresIndutores(leading indicators)ajudamadetectarumaumentona
probabilidadeounagravidadedeumeventoantesqueapare çamnosindicadores
deresultado.
Quandoumindicadorindutormuda,significaquevocêpodeestarnocaminho
paraatingirumobjetivooumeta.Porexemplo,aumentaracoberturadetestesoua
quantidadedetestescriadospodeindicarmaisqualidadenoproduto.
Vocêpodeterdiversosobjetivosemumaequipededesenvolvimentodesoftware,
comoporexemplo,aumentonaqualidade,aumentonaprodutividade,produç ãode
melhoresestimativas,reduçãodocustododesenvolvimento,maiorprevisibilidade
docronograma,aumentonasatisfaçãodousuário,releasesmaisfrequentesetc.Para
cadaobjetivovocêdeveteraomenosumindicadorindutoreumderesultado.
JáosIndicadoresdeResultado(lagging indicators)ajudamaconfirmarqueum
eventopodeocorrerereagemmaislentamenteàsmudan çasnoambientedoque
98

## Página 113

CasadoCódigo Capítulo5. OtimizandoValor
osindicadoresindutores.Sãométricasqueverificamquevocêatingiuseuobjetivo
depoisdetercompletadootrabalho. Porexemplo,reduzironúmerodedefeitos
reportadosporclientesapontaqueaqualidadedoprodutodefatomelhorou.
Meça times e não indivíduos
Quandoaspessoasacreditamqueserãoafetadaspelosresultadosde
métricassobreseustrabalhosindividuais,elasrapidamenteencontram
formasdecorrompertaismétricas[38],alémdisso,medirindivíduos
podedestruiracolaboraçãodotime,umavezqueajudarumoutromem-
brodotimepodesignificarmelhoraramétricadedesempenhodelee
prejudicarasuaprópria.
Jáquandomede-seotimeemvezdoindivíduo,jáqueacolaboraç ão
tendeamelhoraraperformancedotimecomoumtodo,acolaboraç ão
entreaspessoasserámaisincentivada.
Essessãoalgunsdosindicadoresmaiscomumemambienteságeis:
• VelocidadedoTime:Quantidadedepontosdehistóriaqueumtimeconsegue
entregaremumadeterminadaiteração.
• Aceleração:Alteraçãodavelocidadedotime,aolongodasiterações.
• Leadtime:Otempoentreopedidodoclienteeaentrega(oinícioeofimdo
processo). Ex:2diasdobacklog(registrodopedidodocliente)àproduç ão
(entregadosoftwarefuncionando).
• Cycletime(tempodeciclo):Otempototalentreoinícioeofimdaproduç ão
oudaprestaçãodeserviço.Ex:6horasporhistóriadeusuáriodo“todo”ao
“done“.
• TempodeVida:Quantidadedetempoemqueumahistóriadeusuárioestá
noBacklog.
• Quantidadedehistóriasimpedidas:Listadehistóriasimpedidasporfaltade
informaçõesourecursos.
• TaxadeDefeitosporhistória: Aquantidadedefeitosparacadahistóriade
usuário.
99

## Página 114

5.2. MétricasÁgeis CasadoCódigo
• SaúdedoBuild:TempoqueoBuildestápassandoemrelaçãoaotempoque
estáquebrado.
• ValordeNegócioAgregado:Totaldevalordenegóciodashistóriasentregues
naiteração.
• HorasTrabalhadas:Somadashorasdedicadasaoprojetoportodososmem-
brosdotime.
• CoberturadeTestes:Percentualdecoberturadetestesdeunidade.Podeser
facilmenteobtidoporferramentasdeanálisedecobertura.
• QuantidadedeCenáriosdeTeste:Contagemdoscenáriosdetestesdisponí-
veis.
•Throughput(Produção):Quantidadedehistóriasentreguesemdeterminado
períododetempo.
• HappinessIndexdaEquipe: IndicaaMotivaçãodoTime,ésubjetivo,mas
podesermuitoútilparaperceberquandooclimaestáruimetomaralguma
açãoparamelhorar.
• TrabalhoemProgresso(WIP):Quantidadedehistóriascomeçadasenãoen-
tregues.
• Lucro: Influenciadasentregasnolucroobtidoatravésdosincrementosno
produtoemdesenvolvimento.
Essessãoapenasalgunsindicadoresquepodemounãofazersentidonoseu
contexto.Aspossibilidadessãoinfinitas,porém,procureencontrarasmétricasque
maispodemagregarvaloraotime,edêvisibilidadeaelasparaqueotimepossa
acompanhá-lasemelhoraracadanovaiteração.
MasqueméResponsávelpelaMétricas?
NométodoXPháumpapelimportante,quemuitasvezeséesquecido,trata-se
dotracker . O trackeracompanhaaagendadotime,ealgumasmétricas,sendoa
maisimportantedelasavelocidadedotime,queéarelaç ãodetempoidealestimado
paraastarefaseotempogastonaimplementaç ão.
Eledevemanterseusolhosnosdadosimportantesaseremacompanhados,como
avariaçãodavelocidade,horasextrastrabalhadas,arelaç ãodetestesquepassaram
100

## Página 115

CasadoCódigo Capítulo5. OtimizandoValor
equefalharam,aquantidadededefeitos,emétricascomo leadtime eotempode
ciclo,alémdemétricasmaistécnicasvoltadasaocódigofontecomocoberturade
testes,métricasdecomplexidade,coesãoeacoplamento.
MartinFowlereKentBeckresumemqueopapeldo trackerdizrespeitoafazer
perguntassimplesqueapontempossíveisproblemas[28].
5.3 Apresente o Resultado em Reuniões deDemons-
tração
Acadanovoincrementoqueérealizadonoproduto,éinteressantereunirtodosos
envolvidosnoprojetoparaumareuniãodedemonstraç ão.
Nessareuniãoaequipeapresentaoquehádenovonoprodutodemonstrandoas
novasfuncionalidades.NoScrum,essareuniãoéchama“SprintReviewMeeting”.
NasReuniõesdeDemonstraçãoapresentaçõesdePowerPointnãosãorecomen-
dadas[18],emvezdisso,apresenta-seosoftwareemfuncionamento.Funcionalida-
desquenãoestãoprontasnãodevemserdemonstradas.
Duranteareunião,osinteressadosnoprodutopodemfazercomentários,ob-
servaçõesemanifestardesejosdemudan çasnasfuncionalidadesapresentadas,tudo
issopodeseranotadoetratadoposteriormentepelo Product Owner.
Paraumaiteraçãode1mês,KenSchwaberrecomendaumtempomáximode1
horadepreparaçãoe4horasdeduraç ão[55].
O Product Owner nãoprecisanecessariamenteaguardaratéareuniãodede-
monstraçãoparaveroincrementoaserfeitonosoftwareedarfeedbackaequipe.
Algumasequipestemapráticade“Just-in-TimeReviews”[46],issoé,assimquea
históriaficarpronta,aequipesereunecomo Product Ownerparaumarápidade-
monstração.
5.4 MelhoriaContínua com Retrospectiv as
Cadaequipeéúnicaepossuicaracterísticasdiferentes,nenhumprocessoéperfeito
e,raramente,cobrirátodasasnecessidadesdeumaequipeouprojeto.Poressara-
zão,énecessáriotrabalharcontinuamentenamelhoriaeadaptaçãodoprocesso.As
reuniõesderetrospectivasãoumaexcelenteformaparafazê-lo.
Asretrospectivassãonaturais,afinaltodofinaldeano,você,provavelmente,faz
asualistadedesejosparaoanonovoeumareflexãosobretudoqueconquistouno
anoqueestáacabando. Deformasemelhante,aofinaldecadaiteraç ãoasequipes
101

## Página 116

5.4. MelhoriaContínuacomRetrospectivas CasadoCódigo
sereúnemparaumaretrospectivaquevisalevantartodososacontecimentosimpor-
tantesdaiteraçãoerefletirsobreoquefoibom,oquedevesermantidoeoquepode
sermelhorado.
Nessasreuniõestodososmembrosdaequipetêmaoportunidadedefalarsobre
oqueestáounãofuncionandobem,sugerirnovaspráticas,tecnologias,eapresen-
taroutrasideiasemgeral,dessaformatodospodemcontribuirparaamelhoriado
processo.
Outropontomuitoimportantedasretrospectivaséolevantamentodosacon-
tecimentosmaissignificantesdaiteração,quandoaequipeapresentaasprincipais
liçõesaprendidasqueserãolevadasparaofuturo.
Asretrospectivasnãotêmcomofocoapenasquestõesvoltadasaoladotécnicodo
desenvolvimentodesoftware,masvãoalém,edevemtratartambémdoladohumano
edorelacionamentoentreaspessoasenvolvidasnoprojeto. Isso,segundoEsther
DerbyeDianaLarser,duasdasmaioresespecialistasnoassunto,sãoquestõestão
desafiadorasquantooumaisdesafiadorasdoqueasquestõestécnicas[22].
Nenhumprocessoéperfeito!Alémdisso,suaequipeéúnica,eprovavelmente
estásempreenfrentandodesafiosdiferentesdetodasasoutras,porisso,oprocesso
deveseradaptadoemelhoradocontinuamenteparaatenderdeformaeficienteas
necessidadesdaequipe.Éexatamentenissoqueasretrospectivaspodemajudarum
equipededesenvolvimentodesoftware.
Nasretrospectivasépossívelqueaequipereflitaeidentifiquemudan çaseme-
lhoriasquepoderãoaumentaraqualidadedosoftwareeaprimorarseudiaadiade
trabalho.
Retrospectivassãonaturaisemmétodoságeisquefocamemadaptaç ãoeres-
postasrápidasamudan ças,porém,podemtambémserrealizadasemequipesque
utilizammétodostradicionais.
JamesShoreeShaneWarden,sugeremqueapenasosmembrosdaequipeparti-
cipemderetrospectivas[66],paraqueessespossamsentir-seàvontadeequeefetiva-
mentepossamfalarabertamentedeseusproblemasdocotidiano.Deve-seentender
por“equipe”todasaspessoasenvolvidasnoprojetoquesãodiretamenteligadasao
desenvolvimentodosoftware,issoexclui,porexemplo,clientes,investidoresecuri-
osos.
102

## Página 117

CasadoCódigo Capítulo5. OtimizandoValor
Não Subestime oPoder daRetrospectiv a
Retrospectivas,infelizmente,costumamseraprimeirapráticaaser
cortadadoprocessoemmomentosqueaequipeestásobpressão,mas
ocorreque,geralmente,aretrospectivaéamelhoroportunidadequeo
timetemdeentenderporqueestánessasituaçãodepressãoeoquepode
fazerparasairdela.
OFacilitadordeRetrospectivas
Todareuniãoderetrospectivadeveterumfacilitador(tambémchamadodelíder
deretrospectiva).Ofacilitadordevegarantirquetodososparticipantesmantenham
ofoconosobjetivosdaretrospectivaeajudaraequipeaseorganizarpararealizaras
atividadesqueosdirecionemadescobriroqueprecisasermelhoradoeoquepode
serfeitoparamelhorar.
Osfacilitadoresfocamnaestruturaenoprocessodaretrospectiva,edevemes-
tarconstantementeatentosàsatividadeseaotempo.Éimportantequeotempode
duraçãodareuniãosejabemdefinido,apresentadoatodos,assimcomorespeitado.
Ultrapassarotempodefinidopodefazercomqueosparticipantesfiquemdispersos
esintam-sedesrespeitados,umavezquepodemteroutroscompromissos,atividades
eobrigaçõesquerequeremsuaaten çãoapósareunião.Reuniõesquenãoterminam
notempodefinidotendemasetornarcansativasepoucoprodutivas.
Osoutrosparticipantesdaretrospectiva,emcontrapartida,devemestartotal-
mentefocadosnoconteúdo,nadiscussãoenatomadadedecisões,completamente
despreocupadoscomoprocessodaretrospectiva,deixando-oacargodofacilitador.
Opapeldefacilitadorpodeserrotativodentreosmembrosdaequipe,deforma
queacadaiteraçãopossaexistirumapessoadiferenteassumindoessepapel.Defato,
érecomendávelquecadareuniãoderetrospectivapossuaumfacilitadordiferente,de
modoquetodospossamexercitaressepapeletreinarashabilidadesporeleexigidas.
Ofacilitadordevepermanecerneutroemdiscussõesmesmoquandohouverfor-
tesopiniõesarespeitodotemaemdiscussão.Seeleestiverengajadonadiscussão,
provavelmentenãoconseguiráfazerumbomtrabalhonalideran çadaretrospectiva.
Ofacilitadordeveevitarqueocorramconversasemparalelo,edeveassegurar
quetodossejamdevidamenteouvidos.Contudo,eledeveaindacortarasdiscussões
quandoestiverempropensasaestourarotempodareuniãoouimpedirquetodosos
103

## Página 118

5.4. MelhoriaContínuacomRetrospectivas CasadoCódigo
tópicosimportantessejamabordados.
Éessencialquetodostenhamoportunidadedefalarequeosmaisfaladoresnão
dominemareunião. Ofacilitadordeveestarsempreatentoàspessoasquefalam
demaisoudemenoseincentivarpessoascommaiordificuldadedeexpressarseus
pensamentosemgrupoafalarem.
Outraresponsabilidadedofacilitadordaretrospectivaélidarcomcomporta-
mentosinadequadosaolongodareunião.LarseneDebbyaconselhamevitarchamar
aatençãodaspessoasindividualmente,buscandosemprechamaraten çãodogrupo
enquantoforpossível,enfatizandoocomportamentoenãoapessoa.
Alémdisso,deve-seevitarqueaspessoasutilizemaretrospectivaparaapontar
culpados,transformando-aemalgoconhecidocomojogodeculpas,oquegeral-
mentefazcomqueaspessoas“levemparaoladopessoal”,percamofocodare-
trospectivaecriemumclimadesagradávelecompetitivo,impedindoqueogrupo
trabalhecolaborativamente.
Aoinvésdeculparalguémporterquebradoobuild,porexemplo,deve-sepro-
curarexporproblemasporfaltadeaten çãoaoenviarocódigoaorepositóriosem
antesexecutarostestesdeunidade,eressaltaraimportânciademanter-sealertaa
essaprática.Focoestásemprenoproblemaenãonapessoa(oupossíveisculpados).
NormKerthemseulivro“ProjectRetrospectives”apontouumafrase,aqual
chamoudeprimeiradiretrizdasretrospectivas:
“Independentementedoquedescobrirmoshoje,nóscompreendemoseacredi-
tamosquetodosfizeramomelhortrabalhoquepodiam,dadooqueconheciam,suas
competênciasehabilidades,osrecursosdisponíveis,bemcomoasituaçãoemmãos.
[32]”
Kerthrecomendaquenoiníciodasretrospectivasofacilitadorleiaaprimeira
diretrizparaaequipe.Elaéumaferramentaparatrazerconsciênciaparaotrabalho
colaborativoeparaaconfian çaqueosmembrosdaequipedevemdepositarentresi.
Dessaforma,épossívelevitarproblemascomoataqueaindivíduosedistribui-
çãodeculpa.Éessencialqueaspessoasdeixemdeladoacompetiç ãoecolaborem
paraalcançarumbomresultadonaretrospectiva,podendoestenderissotambémao
trabalhododiaadia.
Aprendasobreahistóriaeoambientedasuaequipe. Éimportanteanalisara
históriaemoraldaequipe,especialmenteemrelaç ãoaoprojetoatual.
Estudequaissãoosartefatosdisponíveisequaispodemserincorporadospara
ajudar,conversecomlíderesformaiseinformais.Essainvestigaç ãopoderáajudá-lo
104

## Página 119

CasadoCódigo Capítulo5. OtimizandoValor
afazerasperguntascertasduranteareuniãoeoajudarãoapreverquaisproblemas
devemserenfrentados.
Emsuma,ofacilitadordeveguiarareunião,assegurarquetodososmembros
daequipeestejamcompreendendoosobjetivosdasatividadesequetodostenham
chancedefalareexporseuspensamentos.
Quanto tempo deve lev ar uma reunião de retrospec-
tiv a?
Nãoexisteumafórmulaparadefinirestevalor.Comocostumamdi-
zerosconsultores: depende. Vocêdevelevaremconsideraçãoalguns
fatorescomootempodaiteraç ão,otamanhodaequipe,propensãoa
conflitosecontrovérsia,ecomplexidadedosassuntosaseremdiscuti-
dos. OmétodoScrum,porexemplo,sugereduashorasdereuniãode
retrospectivaparaumsprintde30dias.
Afacilitaçãoeatémesmoaparticipaç ãoemretrospectivaséumprocessode
aprendizadocontínuo: quantomaisprática,maiorseráaeficiênciaparaalcan çar
bonsresultados.Vocêdeveavaliaroresultadodasretrospectivasatravésdosbene-
fíciosconquistados,istoé,dasmelhoriasrealizadaspormeiodasaçõesqueforam
definidaseefetivamenterealizadas.
As5etapasdasretrospectivas
DianaeDerbypropõemcincopassosbásicosparaarealizaç ãoeficientedeuma
reuniãoderetrospectivaágil[22].Essespassosajudarãoofacilitadoraguiarareu-
niãoelevarosmembrosdaequipeatrazeràtonapossíveisitensaseremmelhorados
eideiasparaalcan çarasmelhorias.
1) Preparação
2) ApresentaçãodosDados
3) Insights
4) Decidiroquefazer
5) Fechamento
105

## Página 120

5.4. MelhoriaContínuacomRetrospectivas CasadoCódigo
AbrindoaRetrospectiva
Antesdetudoéimportanteprepararaspessoasparareuniãoparaquefoquemno
trabalhoquedeveserrealizadoaolongodaretrospectiva.Crieaatmosferaidealpara
queaspessoassintam-seconfortáveisemdiscutirtópicoscomplexoseestabelecer
diálogosdesafiadores.
Definaumametaparaaretrospectiva.Umametabemclaraofereceàspessoas
umsensoderazãopelaqualestãoinvestindoseutempo.Procureescolherumameta
abrangenteparaqueaequipefiquelivreparautilizarsuacriatividadeealcan çarin-
sights.
Considereocontextodaequipeedescubrametasqueaajudarão. Écertoque
todaequipetemsuasparticularidades,diferentespontosfortesefracos. Nomo-
mentodeelaborarametadaretrospectiva,procurealgoquerepresenteabuscadas
melhoriasquepodemtrazermaiorbeneficioparasuaequipeemparticular.
ApresentandoDados
Depoisdapreparação,vemaapresentaçãodosdados.Aindaqueosbenefícios
dereunirinformaçõesdeumaitera çãoquetenhaduradoumaoupoucassemanas
possanãoserevidente,essaéumapráticamuitoimportanteparaaretrospectiva.
Emumaiteraçãosemanal,porexemplo,perderumdiasignificaperder20%dos
acontecimentos. Mesmoqueaspessoasestejampresentes,elasnãoveemtudoo
queacontece.Alémdisso,pessoasdiferentesveemosmesmosacontecimentoscom
perspectivasdiferentes.Portanto,reunirinformaçõesfazcomqueaequipecrieuma
visãocompartilhadadetudooqueaconteceu,expandindoaperspectivadetodaela.
Éimportanteapresentarmétricas,históriasdeusuárioconcluídas,decisõesto-
madas,resultadosdeoutrasreuniõesrealizadasaolongodaiteraç ão,desafiosen-
frentados,novastecnologiasadotadasetudoquetiversignificadoparaaequipe.
Vocêpodeutilizarcomométricasoburndownchart,avelocidadedaequipe,o
númerodehistóriasprontas,onúmerodedefeitosresolvidos,acoberturadetestes
etc.
Outratécnicainteressanteparaapresentarosacontecimentosdaiteraç ãoécriar
umalinhadotempoepermitirqueaspessoasenumeremacontecimentos.Issofaz
comqueaspessoaslembrem-sedoseventosrelevantesaoprojeto,comoreleases,
milestoneseproblemasdiversosquepodemserposteriormenteanalisados.
Independentedatécnicautilizada,aequipedevedescreverosacontecimentos
eprincipalmenteosproblemasqueestãoenfrentando,istoé,devemrefletirefalar
106

## Página 121

CasadoCódigo Capítulo5. OtimizandoValor
sobreoquenãoestáindobem.Abaixoapresentamosalgunsexemplosdeproblemas
comunsquesãolevantadosporequipesnessaetapadaretrospectiva:
• Nãoestamosfazendotestesdeunidade;
• Temosdúvidassobreashistóriasdeusuárioeninguémestádisponívelpara
nosajudar.
• Hámuitoretrabalho.
• Faltadeconhecimentotécnico.
• Muitosdefeitos.
GerandoInsights
Depoisdeanalisarosdadoséhoradeperguntarosporquês,pensarsobreoque
sepodemudareidentificaroquefazerdeformadiferente.
Aequipedeveutilizarosdadosreunidosparaidentificarospontosfortesefracos
daúltimaiteração,eentãoexporsuasideiasparafortalecerospontosfracosenão
permitirqueospontosfortesenfraque çam.
Insightssãograndesideiasqueaequipeacreditaque,seaplicadas,serãoeficien-
tesnaobten çãodemelhoresresultados.Busqueporcondições,interaçõesepadrões
quecontribuíramparaosucessoemmelhoriasanterioresparaencontrarnovosin-
sights.
Essesinsightsajudarãoaequipeadescobrirformasdetrabalharcommaiorefici-
ência,queéograndeobjetivodaretrospectiva.Aoidentificarproblemas,evitesim-
plesmenteaceitaraprimeirasoluçãoqueforproposta.Elapodedefatoseramais
adequada,porém,valeconsideraroutraspossibilidades,analisarcausaseefeitose
permitirqueaequipecolaborativamentealcanceamelhorsoluç ão.
Brainstormingéumatécnicainteressanteparainstigaraequipeaterinsights.
Atécnicaconsisteemdaràequipeumtempoparapensar,exporeconstruirideias
sobreoutrasideiasanteriormentepropostas.
Depoisdelevantadoumnúmerosuficientedepropostaspararesolverproblemas
oualcançarmelhorias,aequipedevedefinirfiltroseaplicá-losparareduzironúmero
deideiaseentãolevá-lasàpróximaetapaparaefetivamentedecidiroquefazer.
Umatécnicainteressantepararesolverisso,éa votaçãoporpontos (figura5.5.
Imaginequehá20proposta.Escrevacadaumaemumcartãoedêacadamembro
107

## Página 122

5.4. MelhoriaContínuacomRetrospectivas CasadoCódigo
daequipe5pontos.Então,cadamembropodeinvestirseuspontosemnoscartões.
Tantofazsequiserinvestiros5pontosemumúnicocartãoou1pontoem5cartões
diferentes.Oscartõescommaiornúmerodepontosserãoosescolhidos.
Figura5.5:VotaçãoporPontos
Outraferramentapoderosaparaobten çãodeinsightséatécnicados5porquês.
Comdadosefatosemmãos,aequipepoderealizaressaatividadeparamelhorcom-
preenderasrazõespelasquaisdeterminadoseventosocorreram.
Atécnicaconsisteemanalisarumdeterminadoacontecimentoperguntandopor
queeleaconteceu,eparaarespostaaessaperguntaquestiona-senovamenteoseu
porquê,eassimsucessivamenteatéalcan çarcincorespostas(vejaumexemplona
figura5.6.
108

## Página 123

CasadoCódigo Capítulo5. OtimizandoValor
Figura5.6:Os5porquês
Essatécnica,muitoutilizadapararesoluçãodeproblemas,foidesenvolvidapor
SakichiToyodanaToyotaefazpartedemétodoscomoLeanManufacturingeSix
Sigma.Identificandoacausa-raizdoproblema,deve-seentãotrabalharemsuaso-
lução,ouseja,buscarinsights.
Esseexercíciopodeserrealizadoportodaaequipeemumgrupogrande,ou
empares,quedepoisapresentamoresultadoatodoogrupoparaconsolidaç ãodas
ideias.
DefinindoasA çõesdaRetrospectiva
Oquartopassotemoobjetivodeajudaraequipeadecidiroquedeveserfeito.
Agoraqueaequipetemumalistadepotenciaisideiasdeexperiênciasemelhorias
aseremrealizadas,éprecisoselecionarositensconsideradosmaisimportantes(ge-
ralmenteumoudoisporiteração)eplanejaroquefazer,ouseja,queaçõestomar.É
nestemomentoqueofocodareuniãoémudadodopassadoparaofuturo,istoé,da
iteraçãoanteriorparaapróximaiteraç ão.
Éimportantequeaequipeestejacomprometidacomositensqueforamseleci-
onadosparaseremmelhoradosnaiteraç ão.Umexemplodeaçãoasertomadaem
109

## Página 124

5.4. MelhoriaContínuacomRetrospectivas CasadoCódigo
umanovaiteraçãoé:“Todososmembrosdaequipetrabalharãoempardoisdiaspor
semana”.
Eviteatodocustosairdaretrospectivasemumalistaclaradeaçõesaseremto-
madasparaalcan çarmelhorias.Mantenhasempreofocoemcoisasqueefetivamente
podemsermelhoradaseeviteinvestirmuitotempoemquestõesquenãodependem
daequipeounãopodemsermudadas,comomautempo,trânsitoetc.
Éimportantequearesponsabilidadederealizarasaçõesdefinidasnaretrospec-
tivasejacompartilhadaedivididaportodaaequipe. Nãopermitaqueapenasum
oupoucosmembrosdaequipeconstantementetomemessaresponsabilidadeparasi
impedindoqueoutroscolaborem.
EncerrandoaRetrospectiva
Finalmente,noquintopasso,aequipedevedefinircomodocumentaroquefoi
decididoeaprendidonareunião. Paraisso,algumasequipesfotografamoquefoi
escritonalousa,outraselegemummembrodaequipeparacriarumapauta,outros
escrevemtodosositensemcartõeseosguardam,issoficaacritériodaequipe.
Éimportantequeasdecisõestomadasfiquemdisponíveisdealgumaformapara
consultadetodoseutilizaçãoemretrospectivasfuturas.Algumasequipesmantêm
todasasmelhoriasdefinidasnareuniãoderetrospectivaemum backlogdemelho-
rias,queémantidoepriorizadopeloprópriotime.
110

## Página 125

CasadoCódigo Capítulo5. OtimizandoValor
Comece com o formato mais Simples
Tantainformação,etapas,tempo,preparação,técnicasetc. podem
parecerumpoucodemaisparaquemestácome çando.Nãoseintimide
comisso,comecereunindootimeemfrenteaumquadrobrancoouum
flip-chartediscutacomotimesobreasseguintesperguntas:
• Oqueestáindobem?
• Oquepodesermelhorado?
Nofinaldascontasoquerealmenteimportaéqueareuniãotenha
comoresultadoaçõesaseremtomadaspelaequipeparaqueamelho-
riacontínuasejaaplicada,equenapróximaretrospectiva,aequipeseja
melhordoqueeranaúltima.
Amedidaqueotimeforevoluindonautilizaç ãodemétodoságeis,
procurevariarumpoucoastécnicasutilizadasparaqueareuniãonãose
torneprevisívelemassante.Dinamizarealteraroformatodaretrospec-
tivasemdúvidaestimularáacriatividadedotimeparabuscarsoluções
paramelhorarcontinuamente.
Vocêpodepesquisarpornovastécnicasedinâmicasdegrupopara
utilizarnasretrospectivasnossites: http://retrospectivewiki.orgehttp:
//tastycupcakes.org.
5.5 Eliminando Desperdícios comLean
TaiichiOhno,criadordoToyotaProductionSystem(TPS),definiu-ocomoum“sis-
temadegerenciamentoparaaeliminaçãoabsolutadedesperdícios”,edissequeoque
deveserfeitoéumalinhadotempoentreomomentoqueoclientefazumpedido
atéomomentoemquerecebeoprodutoepagaporele,ousejaoprocessocompleto.
Depoisdeidentificartodasasetapasdessalinhadotempo,deve-sereduzi-la,
removendotudooquenãoagregavalor,ouseja,deve-seeliminartodoodesperdício.
Emsuma,qualqueratividadequeconsumatempooudinheiroenãoagregavaloré
desperdício.
111

## Página 126

5.5. EliminandoDesperdícioscomLean CasadoCódigo
DesperdíciocomTrabalhoParcialmentePronto
Paraindústriasemgeral,acumularestoqueéconsideradodesperdício.Oesto-
queprecisasermovimentadodeumladoparaooutro,armazenado,rastreado,pode
serperdido,roubado,ficarobsoleto,quebraretc.Éporissoqueoidealéteromí-
nimodeestoquepossível.
Vocêdeveestarseperguntando:qualéarelaçãodeestoquecomsoftware?Esto-
quenaperspectivadesoftware,paraPoppendieck,representatrabalhoparcialmente
pronto,trabalhoquepodeficarobsoleto,podeserperdido[48].
Trabalhoparcialmenteprontopodeser,porexemplo,requisitosespecificados
comexcessodedetalhesantesdodesenvolvimentoseriniciado.Lembre-sequere-
quisitospodemmudaretornar-seobsoletos,ouaindahistóriasdeusuáriosdesen-
volvidasaguardandoparaseremvalidadasporumaequipedequalidade,ouaguar-
dandoparapassarporumprocessodeintegração.Tudoissoétrabalhoparcialmente
prontoeconsequentementedesperdício.
Desperdíciocomfuncionalidadesquenãoagregamvalor
AmaiorfontededesperdíciopodeservistaclaramentenoChaosReport[3]:
somente20%dasfuncionalidadesdesenvolvidasemsoftwaresãoefetivamenteutili-
zadasregularmente;osoutros80%sãoprovavelmentefuncionalidadessuperficiais,
responsáveispelamaiorpartedocustodesedesenvolverosoftware–emoutraspa-
lavras,desperdício.Alémdisso,aindaaumentamsignificativamenteacomplexidade
dabasedocódigoeocustoparamantê-lo.
Ocustodacomplexidadeéexponencial,nãolinear. Quandoabasedecódigo
émuitocomplexa,aconfian çaderealizaralteraçõesdeformaseguraépequena.
Consequentemente,equipesinteligentesmantêmseucódigofontesimples,claroe
reduzido. Porém,paraqueissoaconte ça,todanovafuncionalidadedeveteruma
boajustificativadopontodevistadonegócio,deformaquesejaalgoquerealmente
agreguevalor.Poppendieckalertaquesoftwareécomplexopornatureza,eporisso,
nãogerenciarsuacomplexidadecuidadosamenteéumareceitaparaofracasso.
Desperdíciocomdocumentação
Produzirdocumentosqueninguémlêédesperdício.Documentaréumaativi-
dadequeconsomeotempodaspessoaseaumentaotempodedesenvolvimento.
Evitedocumentaçõesburocráticasquenãoserãolidasporninguémenãoagre-
garãovaloraoproduto,econcentre-seemdocumentarsomenteoquefornecessário.
112

## Página 127

CasadoCódigo Capítulo5. OtimizandoValor
Cuidado,porém,paranãolevaressaideiaaoextremo.Nãodeixededocumentaro
queforimportante.
LarryBurns[16]dáalgumasdicasparaevitardesperdícioscomdocumentaç ão:
• Nãoproduzadocumentaçãoquenãoserálida.
• Eviteproduzirdocumentaçãoquenãoseráatualizada(amenosquesejadeli-
beradamenteproduzidaparasatisfazerumrequisitotemporário,comoaten-
derumalicitação,porexemplo).
• Nãodocumentecoisasóbvias,triviais,redundantesouinformaçõesquepo-
demfacilmenteserobtidasemoutrasfontes.
• Adocumentaçãodeveestardisponívelepoderserfacilmenteacessadapelos
interessados.
Éimportanteencontrarumequilíbriosaudável,ediscernirentreoquedeveeo
quenãodeveserdocumentado.
Desperdícioporfaltadefoco
DeacordocomolivroPeopleware,deTomDeMarcoeTimothyLister,toda
vezquealguéméinterrompidoduranteaexecuç ãodeumatarefaparatrabalhar
emoutra,ouajudaralguémemalgumassuntodecontextodiferentedoqueestava
fazendo,umtemposignificativoégastoparaseconcentrarnanovatarefaevoltarao
estadodeprodutividadeanterior[39].Logo,quantomaisinterrup çõeshouver,maior
seráodesperdício.Poressamesmarazãonãoérecomendávelqueumdesenvolvedor
pertençaaváriasequipes.
Aprogramaçãoemparéumbomexemplodetécnicaqueajudaaevitarinter-
rupções,umavezqueduaspessoastrabalhandojuntasetrocandoconhecimentos
muitoprovavelmentenãoprecisarãointerromperoutrosmembrosdotimeparare-
solverproblemas.
Desperdícioporatrasos
Umadasmaioresfontesdedesperdícionodesenvolvimentodesoftwaresãoos
atrasos.Atrasosporaprovaçãoourevisãoderequisitos,atrasosporcontrataç ãode
pessoal,atrasosnostestes,atrasosnaentregaetc.
113

## Página 128

5.6. Eagora,oqueeufaçoamanhã? CasadoCódigo
Quantomaioroatraso,maistemposeránecessárioparaqueoclienteobtenha
retornosobreoinvestimentorealizadonodesenvolvimentodosoftware.
Astécnicasestudadasanteriormenteparalimitarotrabalhoemprogresso,een-
tregasfrequentesfor çamoprocessoasermaisenxutoefluídoreduzindoassimesse
tipodedesperdício.
Desperdícioporrecursosoupessoasindisponíveis
Quandoo Product Ownernãoestápresenteenãoháninguémqueorepresente,
eexistealgumadúvida,pontoaseresclarecidooudecisãoasertomada,épreciso
esperarqueeleestejapresenteparadarcontinuidadeaodesenvolvimento,ounopior
doscasos,porfaltadeinformações,odesenvolvedorpodeseguirporumcaminho
inadequadoqueprovavelmenteresultaráemumdefeito.
Poressarazãoémuitoimportantequeo Product Ownerestejapresente,próximo
daequipe.
Desperdíciopordefeitos
Defeitossãosemdúvidaumadasmaioresfontesdedesperdícionodesenvolvi-
mentodesoftware,equantomaistempoumdefeitolevaparaseridentificado,maior
seráodesperdíciogerado.
Poressarazão,defeitosdevemseridentificadoseresolvidosomaisrápidopos-
sível.
Essassãoapenasalgumasdasmuitasfontesdedesperdíciosquetodasasequipes
dedesenvolvimentodesoftwarepossuememmaioroumenorgrau. Oexercício
constantedeanalisarequestionaroprocessoéessencialparaqueelespossamse
tornarcadavezmenoresemenosrelevantes.
5.6 E agora, o que eu faço amanhã?
Quaismétricasvocêsutilizamparaacompanharaprodutividadeequalidadedotra-
balhodasuaequipe? Reviseasmétricasapresentadasnase ção5.2everifiquese
algumadelaspoderiaajudar.
Quetalutilizarumdosgráficosapresentados(CFD,BurndownouBurnup)e
deixá-lovisívelparaquetodaaequipepossaacompanharoprogressodaiteraç ão?
Quaisdosdesperdíciosapresentadosnase ção5.5vocêreconhecenoseuprojeto?
Oquevocêpoderiafazerparaajudarareduziroueliminá-lo?
114

## Página 129

CasadoCódigo Capítulo5. OtimizandoValor
Procureumatécnicaderetrospectivadiferente,umaquenuncafoiutilizadaem
suaequipeantes,eofere ça-separaserofacilitadordapróximaretrospectiva.
115

## Página 131

Capítulo6
OtimizandooSistema
Esseéoquartoníveldefluência,falaremossobreoalinhamentodaorganizaç ão
comoumtodo,osvaloreságeisepráticaságeis,assimcomoosobjetivosdaorga-
nização,edecomoaagilidadepodeimpactardeformasistemáticaaperformance
daorganizaçãoalémdotime.
Ateoriadopensamentosistêmiconosensinaqueumsistemaconsistedepartes
interdependentesqueinteragementresiporummesmopropósito.Umsistemanão
éapenasasomadesuaspartes,mastambémoprodutodesuasinterações.
Asmelhorespartesnãonecessariamentefazemomelhorsistema,deformaque
ahabilidadedeumsistemadeatingiroseupropósitodependedequãobemsuas
partestrabalhamjuntasenãoapenasdecomoatuamindividualmente.
Emprojetosdedesenvolvimentodesoftware,énotávelqueexistaumatendência
desemediroprogressodoprojetoatravésdetrêsmétricas:escopo,prazoecusto.
Acontrassenso,mesmootimizandocadaumadessasmétricas,nemsempreo
projetoserábemsucedido,poiselasnãolevamaqualidadeenemmesmoasatisfaç ão
doclienteemconsideração.Paranãoserpegodesurpresa,TomeMaryPoppendieck

## Página 132

6.1. AGestãopodeserÁgil? CasadoCódigo
sugeremaplicarumamétricademaisaltonível,queconsidereoresultadodeforma
maisampla:oretornosobreoinvestimento.Ecomplementam:“Sevocêotimizaro
querealmenteimporta,osoutrosnúmerostomarãocontadesimesmos”[48].Por
issodevemosdarpreferênciaparamétricasglobaisemvezdemétricaslocais[8].
Paramelhorilustraresseconceito,imaginequedeterminadaempresaterceiriza
ostestesdossoftwaresquedesenvolve,equeaempresaterceirizadarecebeporde-
feitoencontradonosistema.Espera-seentãoquetodososdefeitossejamidentifica-
dospelaempresaterceirizadaantesqueosoftwareentreemproduç ão.Entretanto,
quandoumdefeitoforencontrado,provavelmenteaempresaterceiranãoirácola-
borardevidamentecomaequipequedesenvolveuosoftwareparaquedefeitosde
mesmanaturezanãovoltemaocorrerporquenãoédeseuinteressequeaquanti-
dadededefeitosdiminua.
Seosdefeitosforemencontradoseresolvidosantesdosoftwareirparaproduç ão,
então,amétricadeveapresentarumbomresultadoepode-sevirapensarqueas
coisasestãoindobem,masnaverdadenãoestáseconsiderandoarealcausado
defeito,eoproblemanãoestásendoresolvidoemsuaraiz.
Oobjetivoéotimizaroprocessodacadeiadevalorcomoumtodoenãoemcada
etapadoprocessoisoladamente.
6.1 AG estão pode ser Á gil?
“ Aqueles que não fazem acontecer não são nem gerentes nem líderes. ”
–JohannaRothmaneEstherDerby
Muitaspessoasacreditamqueagestãonãoimporta,equebonstécnicosvão
produzirbonsresultados,independentedaqualidadedagestão.JohannaRothman
eEstherDerbydiscordamdisso.Paraelasosbonsgestoresatingemmetasedesen-
volvempessoas. Elasafirmamaindaacreditaremquemuitosgerentesqueremser
bonsgerentes,porém,nãosabemcomofazerumbomtrabalho.
Sevocênãoestácertodequemfazopapeldegestordasuaorganizaç ão,pergunte
sobrequemseresponsabilizapelotreinamentoedesenvolvimentodacarreiradas
pessoas.Quemdáfeedbacksobreotrabalhodaspessoas?Quemmonitoraotrabalho
daequipedeformasistêmica?Essapessoaprovavelmenteassumiuopapeldegestor.
Opontoéqueagestãoestásemprepresente,aquestãoéseopapeldegestorestá
divididoentretodasaspessoasenvolvidasouseestárepresentadoporalguém.
JurgenAppelo,noLivroManagement3.0,propõeumanovaabordagemparaa
gestão,maisalinhadaaosmétodoságeis,ecoerentecomateoriadacomplexidade.
118

## Página 133

CasadoCódigo Capítulo6. OtimizandooSistema
“Para todo problema complexo há uma resposta clara, simples e errada”.
–H.L.Mencken,JornalistaeEscritor(1880–1956)
Omundomudou,emuitosdosconceitosqueaplicamosemnossagestãomo-
dernaforamherdadosdaeraindustrialepré-industrialquandolidamoscomprofis-
sionaisdeperfiscompletamentediferentesdenossosatuaisprofissionaisdaerado
conhecimento.Devemosreinventaragestãoparaquepossamosendere çarosdesa-
fiosqueomundodosnegóciosnosoferecenostemposatuais.
MuitosmétodosefilosofiascomoSixSigma,TotalQualityeTeoriadasRestri-
çõesforammuitoimportantesparamelhoraragestãodenossasorganizações,po-
rémestesaindapartemdomesmoprincípiodequeasorganizaçõesoperamdecima
parabaixoatravésdeumahierarquia. Agestão3.0trásumaabordagemsistêmica
quetrataaorganizaçãocomosistemavivoqueestáconstantementeemprocessode
aprendizagemeadaptação.
Agrandedificuldadequetemosemlidarcomsistemascomplexossedeveàs
nossasmenteslinearesquepreferemcausalidadeàcomplexidade.Nósprocuramos
propósitoecausaemtodasascoisas,buscamosporcausaeefeitoemtudo.Estamos
acostumadosaestudareaprenderdeformalinear,acontarhistórias,eédessaforma
queenxergamosomundo,comoumlugarrepletodeeventosfáceisdeseremexpli-
cadosatravésdesimplesefeitosecausas.GeraldWeinbergchamouissodeFalácia
daCausalidade.
Agestãoágiltemsuasbasesnacomplexidade,porisso,ofocodagestãoágildeve
estarnaadaptabilidadeaoinvésdeprevisibilidade,umavezqueseaceitaquemuitos
fatoresemprojetossãoimprevisíveis.
Paraentendermelhoragestão3.0,vamosentendermelhoroqueéaGestão1.0
ea2.0,afinaldecontas,esse3.0nãopoderiaserapenasMarketing.
Gestão1.0: Focadaemhierarquias,estaversãodagestãoficoumundialmente
conhecidaatravésdomodelocomando-e-controle.Podernamãodepoucosemuma
estruturadedecisõestop-down. Aquifoicriadoaqueleconhecidojargão“manda
quempode,obedecequemtemjuízo”. Podemosdizer,sempossibilidadedeerro,
queaindaéomodelodegestãomaisutilizado“naprática”.
Gestão2.0:Focadaemtécnicas,estaversãoprocura“corrigir”algunsdos“pro-
blemas”daprimeiraversãodegestão,masmantendoamesmaestruturatop-down,o
que–nãosurpreendentemente–resolvemuitopouco.Poderíamosdizerqueéuma
Gestão1.0“turbinada”porBalancedScorecards,SixSigma,TQMeoutrosadd-ons.
Gestão3.0:Focadanacomplexidade,estagestãoencaraasorganizaçõescomo
119

## Página 134

6.1. AGestãopodeserÁgil? CasadoCódigo
redes,enãocomohierarquias;enessasredesaspessoaseseusrelacionamentosde-
vemestarnofocodagestão,maisdoqueosdepartamentoseseuslucros.
AGestão3.0sugerequeagestãotrabalhecomseisvisões. Nãoàtoa,essasvi-
sõessãorepresentadasporummodeloumpoucodiferentedosconhecidoscírculos,
flechaseretângulosdedesenhosorganizacionais(vejanafigura 6.1);algobemmais
próximodoquemuitasdasorganizaçõesseparecem:monstros.
Figura6.1:Martie,OModelodeGestão3.0(DesenhoporJurgenAppelo)
Energizarpessoas
“Uma pessoa com paixão é melhor que quarenta pessoas simplesmente interessadas. ” E
–.M.Forster–RomancistaInglês
Pessoassãoapartemaisimportantedeumaempresa,certo? Gerentesdevem
portantofazeroqueforpossívelparamantê-lasativas,criativasemotivadas.
ATeoriaXdaMotivaçãonosdizqueaspessoasnãogostamdetrabalhar,traba-
lhampornecessidade,porqueprecisameporisso,precisamdamotivaç ãoextrínseca
120

## Página 135

CasadoCódigo Capítulo6. OtimizandooSistema
paratrabalhar,ealémdissoprecisamdecontroleparagarantirqueestãodefatore-
alizandoseutrabalhocomodevem. Poroutrolado,aTeoriaYdaMotivaç ão,nos
dizqueaspessoasgostamdeseutrabalhoequeencontramprazeremtrabalhar,e
porissopodemsermotivadasporseusdesejosintrínsecosenãosomenteporalgo
externo.
Amotivaçãoextrínseca,segundoJurgen,podeservistacomoumfatorhigiênico,
porquepodemoscompará-laaescovarosdentes,outomarbanho,porexemplo.Não
éaquantidadevezesqueescovamososdentesquenostornamaisfeliz,maséafalta
daoportunidadedeescovarosdentesquenosfariatristes.
Pesquisasapontaramqueamotivaçãoextrínseca(emgeraldinheiro,bônus,prê-
mios,erecompensas)nãoésuficienteparamanteraspessoasmotivadas,épreciso
entenderquaissãoosdesejosenecessidadesdecadaindivíduoatravésdaabordagem
damotivaçãointrínsecaparaqueentão,dealgumaforma,sejapossívelalinharesses
desejosdaspessoasàrealidadedaorganizaç ão,encontrarumaintersecçãoentreos
propósitosdecadapessoaeopropósitodaorganizaç ão.
Éimportantenotarquepessoasdiferentessãomotivadaspordesejosintrínsecos
diferentes,taiscomocompetência,aceitação,curiosidade,honra,idealismoepro-
pósito,independênciaeautonomia,ordem,poder,statussocial,relacionadossociais
etc.Porissoosgestoresprecisamestaratentosedevemdedicar-seaconheceracada
pessoaindividualmente,paraentendercomopodemotivá-las.
Empoderartimes
Timesdevemseauto-organizar,masparaissoprecisamempoderamento,auto-
rizaçãoeconfian çadagestão.
Apesardeosgestoresaindadeteremopoderdecontrataredemitirpessoas,em
ambientesdetrabalhoqueemconhecimentoéalgocrucial,ostrabalhadoresdoco-
nhecimentopossuemostrabalhosgeralmentecríticos,enessecenárioogestorpode
servistocomoumlíderfacilitadorqueempoderaosprofissionaisparaquepossam
tomarasdecisõesnecessáriaspararealizarotrabalhoquesãobonsemrealizar.
Delegar é ato de transferir responsabilidades para outra pessoa, geralmente
mantendo-seresponsávelpeloresultado. Empoderarémaisquedelegar—oudi-
zemalguns,delargar—,paraempoderaréprecisoconsiderarodesenvolvimento
daspessoas,assumirriscos,eemmuitasorganizaçõeséprecisomudaracultura.A
teoriadacomplexidadenosdizqueosproblemasdevemserresolvidosomaispró-
ximopossíveldonívelemqueelesacontecem.
Empoderarnãoéalgobinário,tratarcomodessaformaalienaasoutraspessoas
121

## Página 136

6.1. AGestãopodeserÁgil? CasadoCódigo
queconsideramnãoterautoridadedeseresponsabilizarpelosproblemasdaorga-
nizações,jáque“nãoéminharesponsabilidade”.Devemosescolheronívelcertode
empoderamento.
1) Contar(Nível1):Você(ogerente)tomaadecisãoeanunciaàspessoas.
2) Vender(Nível2):Vocêtomaadecisãomastentaganharocompromissodaspes-
soas“vendendo”suaideiaparaaspessoas.
3) Consultar(Nível3):Vocêouveasopiniõesdaspessoasedepoistomaumadeci-
são.
4) Concordar(Nível4):Vocêconvidaaspessoasparaumadiscussãoeentraemum
acordocomelas,chegaaumconsenso.Nestenível,suavozéigualadosoutros.
5) Aconselhar(Nível5):Vocêtentainfluenciaraspessoasdizendoaelassuaopinião,
masdeixaaelasaresponsabilidadedetomarumadecisão.
6) Questionar(Nível6): Vocêpermitequeaspessoasdecidamantes,masdepois
pedeaelasquevendamadecisãoavocê.
7) Delegar(Nível7):Vocêpermitequeaspessoastomemumadecisãosemqualquer
níveldeenvolvimentodasuaparte.
Alémdedefinirosníveisdeempoderação,éimportantetambémdeixarexplí-
citoparaquetodossaibam“ondepodempisar”. JurgenAppelodesenvolveuuma
formasimpleseeficientedetornaradelegaç ãotransparenteatravésdoQuadrode
Delegação[12](vejanafigura 6.2.
122

## Página 137

CasadoCódigo Capítulo6. OtimizandooSistema
Figura6.2:QuadrodaDelegação
Notopodoquadro,temosos7níveisdeemporamento,enaslinhastemosas
áreasdedelegação-chave(essasáreasvãovariardeacordocomocontexto,esseé
apenasumexemplo). Nascolunasnostemosadefiniç ãodequeméresponsável
(representadoporumapessoa,umpapel,ouumaequipe).
Porexemplo,noquadrodafigura 6.2,salárioestánonível2enaresponsabili-
dadedeumapessoachamadaBill. IssoquerdizerqueBilldefineossaláriosmas
tenta“vender”paraotimesuasdecisõessobresalários. Jáoitemcomprarlicen-
çasestánaresponsabilidadedaMarynonível3,issosignificaqueapesardeelaser
responsávelportomaressadecisão,elaprecisarápediraopiniãodotimeantesde
decidir. Jáoitemdefinirtecnologiaestánaresponsabilidadedotimenonível7,o
quesignificaqueotimetemtotalautonomiaparadecidirsobretecnologiaequenão
hánecessidadedeconsultaragestãoantesdedecidir.
Oquadrodeautoridadeéumaótimaformaparatornartransparentequempode
fazeroquê. Identifiquequaissãoasáreasdedecisão-chavenasuaorganizaç ãoe
procuredefinirosníveisdedelegaçãodecadaum.Umavezvisíveletransparente,
serámaisfácildequestionareidentificaroquepodemudarparamelhor.
AlinharRestrições
“O que é medido é gerido”
–PeterDrucker
AGestão3.0nosapresentaoempoderamentocomouminvestimentoquefaze-
mosnaspessoas.Éprecisocompreenderqueseráprecisotempoparaqueaspessoas
123

## Página 138

6.1. AGestãopodeserÁgil? CasadoCódigo
ganhemexperiênciaeadquiramconhecimentoparaquepossamfazerdeterminadas
coisastãobemquantoquemasdelegouécapazdefazer.
Alinharrestrições: auto-organizaçãopodenãofuncionar,paradiminuiresta
possibilidadedêàspessoasumpropósitoclaroemetascompartilhadas.
Aauto-organizaçãopodelevaraqualquerresultado,bomouruim,fazpartedo
papeldogestordaràspessoasumametacompartilhadaparaquepossamseauto-
organizar,deumaformaqueproduzavalorparaaorganizaç ão. Oobjetivodesta
metacompartilhadaédaràspessoasumadire çãoaseguir.
Nosúltimosanos,temosrepetidoquenossasmetasdevemserSMART(Espe-
cíficas,Mensuráveis,Atingíveis,Realistas,eOportunas),porémdopontodevista
dacomplexidade,podemosentenderquemetascomobjetivosespecíficospossuem
característicadiferenteumasdasoutras.Porexemplo,seasuametaéaproveitaras
fériasnaNoruega,comovocêvaimedirisso?Contaráseunúmerodesorrisospor
dia?
Alémdissoénecessáriotermétricasdiferentesparaosdiferentesinteressadosdo
projeto(equipe,cliente,gerente,comunidadeetc.).Osresultadosdevemserexplí-
citosevisíveisparaqueosenvolvidospossamentendercomoestãoeaondedevem
chegaretomaraçõesparamelhorar.
Desenvolvercompetências
O encontro da preparação com a oportunidade gera o rebento que chamamos sorte.
–AnthonyRobbins
Timesnãoconseguirãoatingirsuasmetascasoalgunsdeseusmembrosnãoes-
tiveremsuficientementecapacitados. Agestãodevecontribuirparaodesenvolvi-
mentodascompetênciasdaspessoas.
Maisadiantenessecapítulotrataremosdeváriaspráticasúteisquepodemser
utilizadaspelotime,comapoiodaGestãoparafomentaroaprendizadoecapacitaç ão
daspessoas.
Estruturar
Muitostimestrabalhamdentrodeumcontextoorganizacionalcomplexo,por-
tantoéimportanteconsiderarestruturasquepromovamacomunicaç ão.Comodi-
vidiraspessoasemequipes?Uniraspessoasdeacordocomsuasfun çõesouformar
equipesqueentreguemoprodutodoinícioaofim?Comoessasequipespoderãose
124

## Página 139

CasadoCódigo Capítulo6. OtimizandooSistema
comunicar,diretamenteouporintermédiodealguém?Qualaquantidadeidealde
membrosemumtimeágil?Todasessassãoquestõesrelevantesemsetratandode
estruturaraorganização.
Maisadiante,falaremosdeformaçõesdeequipes,eabordaremosesseassunto
commaisprofundidade.
Melhorartudo
O importante é não parar de questionar.
–AlbertEinstein
Enquantomuitosdenóspassaavidareclamandoqueascoisasnãosãodaforma
comogostaríamosquefossem(queospolíticossãocorruptos,queaempresaéchata,
queomercadoestádominadopormercenários,ousejaláoqueforquenãoestá
bem), MahatmaGandhifoiumverdadeiroexemplodeixando-nosessafilosofia:
“Sejaamudançaquevocêquervernomundo”.
AgilidadetemavercomMelhoriaContínua. Enadamelhorasepermanecer
comoestá. Ascoisasmelhoramquandomudam. Então,paramelhorar,pessoas,
times,eorganizaçõesprecisammelhorarcontinuamenteparaevitarfalhaseevoluir
sempre.
AGestão3.0trazumaabordagemsistêmicaparaGestão3.0queconsisteem[10]:
1) Considerarosistema:Umaredesocialécomplexaeadaptativa.Elavaiseadaptar
àssuasações,evocêtambémdeveseadaptaràredesocial.Écomodan çarcom
osistema.
2) Considerarosindivíduos: Saibaqueaspessoassãoapartecrucialdosistema
social,equeelassãodiferentesumasdasoutras.Nãoháumaabordagemúnica
quesirvaparatodos.Simplesmentepedirparaqueaspessoasmudem,raramente,
ésuficiente.Adiversidadeéoquefazsistemascomplexosfuncionarem,eépor
issoquetrabalharcomumadiversidadedemétodosécrucialparalidarcomas
pessoas.
3) Considerarasinterações:Umcomportamentoseespalhaatravésdeumsistema
complexo.Emumaredesocial,tudogiraemtornodeindivíduosedasinterações
entreeles.Comportamentosseespalhamdeformaviral,eestimulararedesocial
podeajudarasevenceraresistênciaàsmudan çaseatransformarumaorganiza-
çãoporcompleto.
125

## Página 140

6.2. Feedback CasadoCódigo
4) Consideraroambiente:Aspessoassempreseorganizamdentrodocontextode
umambiente.Oambientedeterminacomoosistemapodeseauto-organizar,e
vocêdevesercapazdeajustaroambiente. Issoporqueocomportamentodas
pessoasdependedoambiente,esevocêmudaroambiente,vocêtambémmuda
aspessoas.
NolivroComoMudaroMundo:GestãodeMudan ças3.0,JurgenAppelo,des-
creveemdetalhescomovocêpodeaplicarcadaumadessasabordagensparasetornar
umagentedemudan çasbemsucedido.
6.2 Feedback
NãoéàtoaqueumdosvaloresdeXPéFeedback[13]. Aconstantemudan çado
mundoànossavoltacriaanecessidadededarmosereceberfeedbackcomfrequên-
cia.
Desenvolvedoresprecisamreceberfeedbacksobreasalteraçõesquefizeramno
software,precisamreceberfeedbackacadaalteraçãoparaquesaibamseostestesde
regressãocontinuampassando,porissoutilizamintegraç ãocontínuaeTDD.Além
disso,precisamsaberseocódigoqueescrevemestálegíveldopontodevistadeseus
pares.O Product Ownerprecisadefeedbackdosusuários,otimeprecisadefeedback
dagestão,eagestãodefeedbackdotime. Osciclosdefeedbacksãoimportantes
enecessáriosemdiversasatividadeserelacionamentosexistentesnoprocessode
desenvolvimento.
Quantomaisrápidoefrequenteforofeedback,maisrápidopode-seresponder,
corrigiremelhorar. Existemalgumaspráticaseferramentasquepodemajudaras
pessoasadarereceberfeedback.Aseguir,estudaremosalgumasdelas.
ReuniõesOne-on-ones:conhecendootime
Paraliderarpessoas,éprecisoconhecê-lasbem.Cadapessoaéúnicaepossuir
diferentesdesejos,pontosfortesefracos.Umbomgestorprecisarásaberquemsão
aspessoas(seuspontosfortes,fracoseinteresses)eemqueestãotrabalhando,qual
amissãodaequipeedequeformaelaagregavalorecomoasequipesseencaixam
naorganizaçãocomoumtodo.
Asreuniõesone-on-onesbasicamentesãooportunidadesemqueogestorse
reúnecomcadamembrodaequipe,umaumparaconversar,eperguntarcoisas
como:
126

## Página 141

CasadoCódigo Capítulo6. OtimizandooSistema
• Comoascoisasestão?
• Comoseuprojetoestáindo?
• Oquevocêmaisgostanoseutrabalho?
• Quaissãoosaspectosmaisfrustrantes?
• Vocêpoderiamefalarmaisarespeitode...?
ReuniõesOne-on-ones,realizadasdaformacorreta,constroembonsrelaciona-
mentos. Gestoresquefazemessasreuniõescomfrequênciamuitasvezesasconsi-
deramumdosmelhoresusosdeseutempoeumaferramentaprimordial.Asone-
on-onespodemajudarsuaequipeasaberoquevocêesperadeles,alémdecriarum
canalparacoaching,desenvolvimentodecarreira,confian ça,feedbackeoportuni-
dadeparareportarostatusdotrabalho.
TothmaneDerbyrecomendamqueosgerentesfaç amreuniõesone-on-onesse-
manalmente.NaBluesoftnósasfazemosacadatrêsmeses,esemdúvidas,podemos
dizerqueelastrazembonsresultados.
Dicas paraReuniõesOne-on-ones
• Ritmo:Encontreaspessoasnomesmodiaeporvoltadomesmo
horário,issocriaritmoefazcomqueaspessoasvenhamprepara-
das.
• Presença:nãopermitaqueareuniãosejainterrompidaporliga-
ções,e-mailsetc.
• Compromisso: cancelar ou desmarcar por qualquer razão de-
monstraquevocênãoseimporta.
• Consistência:Procuremanterumformatosemelhanteemdiferen-
tesencontros.
• Adaptabilidade:Adapteafrequência,formatoaomomentoecir-
cunstanciasdotime.
127

## Página 142

6.2. Feedback CasadoCódigo
Nãoseenganecomaideiadequeogestornãodeveriapassartantotempocomas
pessoasparanãoperderofocodagestão,porqueissofazpartedagestão.Aprender
sobreaspessoasfazparte.Saberemqueelasboasequaissãoseuspontosamelhorar
fazparte.Aprendersobreseusdesejoseaspiraçõesfazparte.
Feedback360
Feedbackéessencialparaoamadurecimentoeevoluçãodaspessoas.Precisamos
saberseestamosindobem,eemqueprecisamosmelhorar.
Imaginesevocêpudessereceberfeedbackdediversospontosdevistavariados
dediferentespessoasparasaberexatamenteemquevocêpodemelhorar.Épossível!
HáumaferramentaconhecidacomoFeedback360graus.
Ofeedbackpodesercontextualizadoemcompetênciasqueotimejulgarne-
cessáriasparaquepossamatingirsuasmetas,entregarresultadosdequalidade,e
atenderasexpectativasdosclientes,emanterumbomrelacionamentoeambiente
detrabalho. Podeseavaliartantocompetênciascomocomunicação,colaboração,
comocoisasmasespecíficascomoconhecimentosemtecnologias,ouboaspráticas
dedesenvolvimento.
Comotodaferramenta,podeserbemoumalutilizada.Infelizmente,algunsge-
rentesautilizampararealizaravaliaçõestradicionaisnoestilodecimaparabaixo
[8]emqueapenasgerentesavaliamsubordinadosesubordinadosavaliamgerentes.
Éimportanteevitarfazerumrelaçãodiretadoresultadodofeedbacks,compromo-
ções,demissões,punições,bônusetc.paranãoperderaconfian çadaspessoasecriar
umclimadetensãonaequipe.
Éimportanteprepararaspessoas,eexplicaroobjetivodofeedback,paraquenão
setorneumasessãode“fogoparatodolado”emquecríticasdestrutivassãotrocadas
pelosmembrosdaequiperesultandoapenasemegosferidos.
Aessênciadofeedback360graus,deumpontodevistaágil,équevocêpossa
darfeedbackparatodososmembrosdoseutime,receberfeedbackdetodose,em
algunscasos,inclusive,seautoavaliarcomobjetivodequetodospossamutilizaresse
feedbackparamelhorar. Jáaformapodevariarbastante. Hádiversasabordagens
quepodemserusadas,porexemplo,podeseranônimo,podeserfaceaface,pode
sermaissubjetivoeaberto,oumaisobjetivoerelacionadoametasespecíficas,o
resultadopodeserparticular,oupodeserpublicadoparatodos.Algunsdosformatos
maiscomunssão:
1.Faceaface:Umareuniãoinformalemumambientecasual,emquecadaparti-
cipanteofereceerecebefeedbackdecadaumdosoutros[8].DeacordocomJurgen
128

## Página 143

CasadoCódigo Capítulo6. OtimizandooSistema
Appelo,reuniõesinformaisfuncionammelhordoqueavaliaçõesmaistradicionais
porqueaspessoaspodemdiscutirabertamenteeesclarecerdúvidasparaentender
melhorpedindoexemplosreais.
2. Envelopes: Essaéumaformaquegeralmenteéumpoucoaberta,emque
todososmembrosdotime,recebemumenvelopecomseusnomesescritos,contento
folhasembranco.Aequipe,então,sentaemformatodecírculo,eosenvelopessão
passadosemsentidohoráriodeforma,quecadaumdosmembrosdotime,aopegar
oenvelopedocolegaescrevealgopositivosobreeleealgoqueelepodemelhorar.
Aofinal,osenvelopesvoltamamãodeseusdonoscomasfolhaspreenchidascomo
feeback.Cadaumficacomseusresultadosparaanalisaroquepodemelhorar.
3.Formulários:Aformamaistradicionaléatravésdeformulários(quepodem
serdigitaisouempapel)emquecadamembrodotimeavaliaobjetivamentecada
umadascompetênciasdetodososseuscolegas,atravésdeumanota,quepodeserde
1a10,porexemplo.Depoisdetodosteremavaliado,osresultadossãoconsolidados
ecadaumrecebeseusresultados,assimcomosuaavaliaç ãoemrelaçãoamédiado
time,esuaprópriaautoavaliação.
Definaumtimeboxparaofeeback,paraevitarqueasessãosetornecansativae
interminável.
Vocêpodetentardiversosformatosatéqueencontreumquefuncionemelhor
emsuaequipe,ouvariaroformatoacadanovasessãodefeedback. Omaisim-
portanteéteremmentequeoobjetivoéfomentarofeedbackparaqueaspessoas
melhorem.
6.3 EscalandoÁ gil comProgramas e Portfólios
Equandoumaequipeágilnãoforsuficiente? Equandoaorganizaç ãotivervários
produtosouprodutosgrandesdemaisparaumaúnicaequipeágil?Comoescalara
agilidade? Comodeterminarquemtrabalhanoquê? Essassãoperguntascomuns
quenosfazemosaonosdepararcomsituaçõesemqueprecisamosdediversasequi-
pesparaatingirosobjetivosdaorganizaç ão.
Desenvolvimentodesistemasdelargaescalapodemserrealizadosatravésdedi-
versostimestrabalhandoparalelamenteemummesmociclodereleases,geralmente
comdataequalidadefixos,porém,comescopovariável[37]. Esseníveldedesen-
volvimentoemqueháváriasequipestrabalhandocomumobjetivofinalcomumé
oníveldePrograma.
Emumcenáriocomoesses,écomumquealguémdesempenheopapel Product
129

## Página 144

6.4. FormaçãodasEquipes CasadoCódigo
Manager,ouquehajaumacomunidadedepráticade Product Ownersparacoorde-
nar,alinharelidarcomessesrequisitosdemaisaltonível,quesãoorganizadose
priorizadosemum Program Backlog.
Paraorganizarmuitosprogramas,trabalha-secomportfólios,ondesetratados
requisitosdemaisaltonível,osépicos.Nessenívelérealizadaagestãodetodosos
investimentosdaorganizaçãoqueserãorealizadosatravésdeprogramaseprojetos.
AssimteremosumahierarquiaformadaporPortifólios,ProgramaseProjetos,
emquecadaprojetoserádesenvolvidoporumapequenaequipeágil.
6.4 F ormação das Equipes
Umapremissaimportantedodesenvolvimentoágilsãoasequipescross-funcionais,
ousejaequipesquepossuempessoascomtodasashabilidadesnecessáriasparaen-
tregarashistóriasdeusuáriodoinícioaofim. Elassãogeralmentechamadasde
equipesde feature teamsoufuncionalidades.
Édiferentedasequipesfuncionaisque,geralmente,eramformadasnosproces-
sostradicionais,combasenafun ção,porexemplo,equipedeprogramadores,equi-
pesdeanalistas,equipesdetestadoresetc.Emorganizaçõesqueutilizamessespro-
cessostradicionaisgeralmenteotrabalhopassadeumaequipeparaaoutraatéque
fiquepronto,resultando,muitasvezes,emburocraciaeproblemasdecomunicaç ão.
Afigura6.3ilustraadiferen çanaformaçãodeequipesfuncionaisecross-funcionais:
130

## Página 145

CasadoCódigo Capítulo6. OtimizandooSistema
Figura6.3:EquipesFuncionaiseCross-Funcionais
Nasequipescross-funcionaistodossãoresponsáveispeloresultadodaentrega,
enãoapenasporsuaáreadeespecializaç ão.Alémdisso,écomumqueosespecia-
listasensinemosoutrosumpoucosobresuaáreadeconhecimentodemodoque,
comotempo,todospodemajudarnoquemaisfornecessário,alavancandoassima
produtividadedotime[56].
Issonãosignificaquetodostêmquesaberfazertodootrabalho,equetêmque
fazertodootrabalhomuitobem.Naverdade,equipeságeisincentivamaformaç ão
deespecialistasgeneralistas,sãopessoasquefazemumtipodetrabalhoextrema-
mentebem—desenvolver,porexemplo—,porémtambémsãocapazesdefazer
outrostipodetrabalho—documentaroutestar,porexemplo. Equipesformadas
comprofissionaisassimtendemaeliminardesperdíciosegargalosnaorganizaç ão
[8].
EssesprofissionaissãoconhecidoscomoProfissionaisT,porquesãoespeciali-
zadosemalgumaáreadeconhecimento,representadapelapela“perna”daletraT,
131

## Página 146

6.4. FormaçãodasEquipes CasadoCódigo
porémsãocapazesdefazercoisasemoutrasáreasdeconhecimentorepresentado
pelaamplitudeda“cabeça”daletraT,vejaumexemplonafigura 6.4:
Figura6.4:ProfissionalT
Equipes cross-funcionais nem sempre nãofeature teams , em podem
também ser componentteams,adiferen çadessasequipeséqueemvezdecons-
truirosoftwaredepontaapontaeentregá-loprontoparaqueoclientefinalpossa
utilizar,essasequipesconstroempartesdaaplicaç ão,oucomponentes,que,geral-
mente,sãoentreguesparaqueoutraequipepossautilizareenfimagregarafuncio-
nalidadequeprecisaparaserentregueaocliente.
Por exemplo, o time A pode estar trabalhando em um componente visual
defront-end, enquantootimeBestápreparandoobackenddaaplicaç ão. Em-
bora seja recomendável trabalhar comfeature teams, Mike Cohn alerta
que em certas situações e contextos pode ser interessante se
utilizar de componentteams.
Equipeságeissãocapazesdeentregarsoftwarefuncionandoacadaiteraç ãopor-
quesãoformadasdeespecialistasgeneralistascapazesdejuntosconstruirfunciona-
132

## Página 147

CasadoCódigo Capítulo6. OtimizandooSistema
lidadesdepontaaponta.
Outradiferençanotáveléotamanhodasequipes,emprocessostradicionaisera
comumencontrarequipesfuncionaiscommaisde30pessoas,muitasvezesche-
gandoemextremosdemaisde100. Asopiniõesquantoatamanhoidealdeuma
equipeágilpodemvariar,mas,geralmentesãoequipespequenasquevariamde5a
12integrantes.Quantomaispessoasenvolvidasmaisfrágilsetornaacomunicaç ão
dotime,maiscoordenaçãosetornanecessária,e,geralmente,menoréaprodutivi-
dade[66].
Éimportantelevaremconsideração,comodiscutimosnocapítulo 5queaspes-
soasprecisamtrabalharjuntasporumtempoparaquesejamumaequipedeverdade,
enãoapenasumgrupodetrabalho.Porisso,éimportantequeelaspossamperma-
necerporalgumtemponamesmaequipe,embora,detemposemtempos,pequenas
mudanças,rotacionandomembrosdeumequipeparaaoutra,podemserpositivas
paradisseminaroconhecimentodentreasequipes.
Contratação Colaborativ a
Algoquesemdúvida,influencianaformaçãodeequipes,sãoosnovos
membrosquesãocontratadosaolongodotempo.Acontrataç ãocolabo-
rativaéumapráticaquebasicamenteconsisteempermitirqueaspessoas
daequipedaqualpossivelmenteocandidatofarápartepossaparticipar
doprocessodecontratação,fazendoperguntasecriandodesafiosparao
candidato.
Éclaroqueessaprática,requerconfian çadagestãoematuridadeda
equipe,mas,dessaforma,alémdeotimecolaborarparaselecionarpes-
soasmaisaderentesàculturaeàsnecessidadesdaorganizaç ão,asequi-
pestendemaaceitarmelhoronovomembro,dadoqueparticiparam
ativamentedoprocessodecontrataçãoesele ção,econcordarãoqueo
novomembrotemascaracterísticasqueconsideramimportantesparaa
equipe.
6.5 Práticas de Aprendizagem
“Sejamos claros: Sua carreira é sua responsabilidade, seu empregador não é sua Mãe”
–RobertC.Martin
133

## Página 148

6.5. PráticasdeAprendizagem CasadoCódigo
Háumantigoditadoquedizque“comonanatureza,ouvocêestáverdeecres-
cendooumaduroeapodrecendo”. Naáreadetecnologiadainformaçãoataxade
mudançaeinovaçãoémuitoalta,enósprofissionaisnãopodemosparardeapren-
der.
JurgenAppelo,afirmaqueaeducaçãodoscolaboradoresnãoéaprincipalativi-
dadedaorganização.Poroutrolado,esperarqueaspessoassedesenvolvamsozinhas
nemsempreéumaabordagembem-sucedida:“Euacreditoqueamaioriadaspes-
soasqueraprenderporémnãosabecomo,ouacabamfocandoemcoisasirrelevantes.
Definarestriçõesnoambienteparaqueaspessoasaprendamcoisasrelevantes.”[11]
Algunsprofissionais,infelizmente,nãoseresponsabilizamporseuprópriode-
senvolvimentoprofissional,ecomoemorganizaçõestambémnãoháincentivo,esses
acabamficandoimprodutivosedesatualizadoscomotempo.
EmseulivroCleanCode,RobertMartinenfatizaaimportânciadequetodos
osprofissionaisseresponsabilizemporsuascarreiras[42],algumasorganizaçõesin-
centivamoaprendizadoecriamumambienterepletoderecursosparaqueaspessoas
naturalmenteestejamsempreaprendendoalgonovo. Issoéfantástico,mas,sesua
organizaçãonãoderespaçoparaatividadesdeaprendizagem,nãodesanimeporisso,
afinalaresponsabilidadeaindaésua.
Nessetópicoabordaremosalgumaspráticasquevocêeseutimepodemutilizar
paraestimularoaprendizadodetodos.
Oambientefazdiferença
AequaçãodeLewin,desenvolvidapelopsicologoKurtLewin,defendequeo
comportamentodeumapessoaéumafun çãodesuapersonalidadeedeseuambiente
[45].Issosignificaqueaomudaroambientevocêpodemudarocomportamentode
alguém.
Parailustrar,imaginequevocêéumdesenvolvedorqueacaboudesercontratado
porumanovaempresa.Emseuprimeirodiadetrabalho,notouquetodososseus
colegastêmohábitodelereestudarbastante,hálivrosportodaaparteespalhados
nasmesasdaspessoas,aoouvirumaconversasobretecnologianocafévocêporum
momentopensouqueaspessoasestavamfalandoemgrego:Scala,BigData,Clojure,
Crystal,Datawarehouse,BusinessIntelligence,Hadoop,Kernel... Naverdade,era
apenasumaconversanormalsobretecnologiacomumasériedepalavras-chaveque
vocênuncatinhaouvidofalarantes.
Emumambientecomoesse,háumagrandeprobabilidadedequevocêchegará
emcasae,naturalmente,come çaráaestudarebuscarequiparaçãocomseuscolegas
134

## Página 149

CasadoCódigo Capítulo6. OtimizandooSistema
e,paraacompanhá-los,criaráohábitodemanter-sesempreatualizado.
Agora,pensenumcenáriodiferente,emqueaochegaremseuprimeirodiade
trabalho,vocêpercebequeaspessoassãobemacomodadas,queatecnologiaque
háempresaestáatualmenteutilizandojáestáultrapassadahámuitotempoeque
ninguémpareceseimportaremestudaroubuscarnovasabordagens. Vocêteráa
mesmamotivaçãodeestudaraochegaremcasa?Provavelmentenão.
Oqueocorrequeénóstemosumagrandetendênciadenosconformarmosao
ambienteemqueestamosinseridos.
Éporissoqueumambientequefacilitaepromoveoaprendizadoémuitoimpor-
tanteparafomentarequipestecnicamenteexcelentes.Aseguirvocêseráapresentado
aalgumaspráticasparaajudá-loacriarumambientequefacilitaaaprendizagem.
Comprometa-secomsuacarreira
Muitosdenósacreditaqueaoterminarafaculdadeestáformadomas,naver-
dade,especialmenteemumaáreatãovolátilquantoaáreadetecnologiadainfor-
mação,essaformaçãodeveduraravidainteiraparaquevocêcontinuesendoum
profissionaleficienteerelevanteparaomercadodetrabalho.
Quandoestánafaculdade,vocêdedicaemmédia4horasdoseudiaparasua
formação,paraestudar.Depoisqueacabaafaculdade,muitos,infelizmente,passam
adedicarzerohoras.Éimportantequevocêtenhaumcompromissoconsigomesmo
demanter-seemconstanteestadodeaprendizagemeparaissovocêprecisarádedicar
algumashorasnasuasemana. Nãopodededicar4horascomofazianaépocana
faculdade? Nãotemproblema. Quevocêdedique20minutospordiaentão. Mas
façaeveráqueissofarágrandediferen çanasuacarreira.
OBásico
Inglês:Nostemposglobalizadosemquevivemossaberfalarapenassualíngua
nativajánãoémaissuficiente.Grandepartedomaterialdisponívelparaaprendizado
estáeminglês,eotempodetraduçãoparaoportuguêsé,muitasvezes,longodemais.
Estudeinglêsdeformaapoderlerdocumentaçãodeprojetosopen-source,tutoriais,
artigos,eassistirapalestraseapresentações.
Leitura:Crieohábitodeler.Nãoapenaslivros,mastambémblogseportaisde
tecnologia(comooInfoQ.com,porexemplo).Fiqueligadonoqueestámudandoe
nasnovastecnologiasqueestãosurgindoatodomomento.
Estejasemprelendoumlivro. Quandoterminardelerestelivro,nãoespere.
135

## Página 150

6.5. PráticasdeAprendizagem CasadoCódigo
Comecealerumpróximoenãoparenunca. Eu,particularmente,mantenhoum
BacklogdelivrosnoGoodReads.com,hácentenasdelivrosquequerolereman-
tenhoumalistapriorizadalá,sempreseiqualopróximolivroquecome çareialer
assimqueacabaroatual.
Cuidadoporém,paranãocairnohábitodecomprarmaislivrosdoquepode
ler,faloporexperiênciaprópria.Emcertaalturadaminhavida,percebique,mais
aindadoqueler,eugostavadecomprarlivros. Mantenhasualistadelivros,evá
comprandoàmedidaqueforterminandodelerolivrosquejátem.
EventoseMídia:Participedeeventoseconferênciassobretecnologiaseassun-
tosdoseuinteresse,troqueinformaçõescomoutrosprofissionaiseconstruauma
redederelacionamentos. Hojeemdia,temosumagranderiquezadematerialem
áudioevídeodisponíveisonline(Screencasts,Podcasts,Vídeos),alémdisso,muitas
conferênciasgravamsuaspalestrasedisponibilizamonlineparaacomunidade.Use
tudoissoaseufavor.
CodingDojo
CodingDojoéumareuniãodedesenvolvedorescomoobjetivodetrabalharem
umdesafiodeprogramação.Elessedivertemeseengajamparatrabalharnasoluç ão
doproblemaaopassoquedesenvolvemsuashabilidades[2].
Apremissabásicaéqueoaprendizadodehabilidadesdecodificaç ãoéumpro-
cessocontínuoquedesenvolvedoresdevemsedaraoportunidadedecodificarcom
oobjetivodetreinar.Nãoimportaqualoníveltécnicodosdesenvolvedores,todos
participameaprendemjuntos.
Aprimeiraideiadesessõesdepráticadeprogramaçãoindividuaiseforadohorá-
riodetrabalhofoipropostaporDave Thomas[62]posteriormenteLaurentBossavit,
propôsCodingDojos,commesmoobjetivo,porémcomaparticipaç ãodeumgrupo
deprogramadores[14].
Oambientedeumcodingdojoestimulaoaprendizadocolaboraç ão,diversão,eé
propícioparasetentaraplicarnovasideiaseboaspráticasdeprogramação,comoDe-
senvolvimentoGuiadoporTestes(TDD),Refatoração,eProgramaçãoempar,por
exemplo. Alémdisso,desenvolvedoresaprendemmuitoaoverasdiferentespers-
pectivaseabordagensdeoutrosdesenvolvedores.
Tudoqueéprecisopararealizarumcodingdojoéumcomputador,umteclado,
umprojetor,umdesafiodeprogramaçãoparaserresolvidoedesenvolvedoresinte-
ressadosemparticipar.
136

## Página 151

CasadoCódigo Capítulo6. OtimizandooSistema
ExistemdiferentesformatosdeCodingDojos,o RandoriKata e o Prepared
Kata.
NoformatoRandori,osprogramadorestrabalhamjuntosnasoluç ãododesafio
deprogramação[14],seguindooseguinteprocesso:
1) Escolherumdesafiodeprogramação:Dica,umasimplesbuscanoGooglepor
“sourceofproblemsforcodingdojos”traráalgumasideiasinteressantescomo:
transformarnúmerosromanosemarábicos,escrevernúmerosporextensoetc.
2) Umpardedesenvolvedoresvaiatéocomputadoretrabalharemparnoproblema,
acadaXminutos(geralmente,7minutos)onavegador,assumeopapeldecon-
dutordandolugarparaqueaalguémdaaudiênciaassumaopapeldenavegador,
eocondutoranteriorvoltaaplateia,onovopardácontinuidadedeondeopar
anteriorestava. OprocessoserepetedeXemXminutos,atéofinaldotime-
box.Osdesenvolvedoresaplicamdesenvolvimentoguiadoportestes,eenquanto
abarraestiververde,indicandoqueostestesestãopassando,todosdaplateia
podemdarsugestõesoudiscutirabordagens,masquandoabarraestiververme-
lha(indicandoqueostestesestãoquebrando)apenasonavegadoreocondutor
podemfalar.
3) Umarápidaretrospectivaparaqueosparticipantesapontemoquecorreubeme
oquepodesermelhoradonopróximocodingdojo.
JánoformatoPreparedKataalguémquejáresolveuumdesafiodeprogramação
anteriormenteapresentaasoluçãodeumproblemapassoapassodesdeopontozero,
utilizandodesenvolvimentoguiadoportestes. Cadapassodevefazersentidopara
todososparticipantes(audiência),deformaqueaspessoaspodeminterrompera
qualquermomentoemcasodedúvidas[2].
Dojossãoumaexcelenteferramentadeaprendizadoparadesenvolvedores,e
organizaçõespodemcedertempoe/ouespaçoparaquedesenvolvedorespossam
realizá-loscomointuitodepraticarsuashabilidadesesetornaremmelhorespro-
fissionais.
ClubesdeDiscussãodeLivros
UmClubedoLivroéumgrupodepessoasleemomesmoolivroesereúnemcom
determinadafrequênciaparadiscutircapítulosoutrechosdolivro,expressandosuas
opiniões,aprendizados,coisasquegostaramenãogostaramarespeitodosconceitos
137

## Página 152

6.6. Hackathons CasadoCódigo
eideiasapresentadasdolivro. Geralmente,aspessoasvãolendoolivroàmedida
queosencontrosacontecem.Sãocomum,porexemplo,reuniõessemanais,emque,
antesdecadareuniãolê-seumdoscapítulosparadiscussão.
Numaorganizaçãoemtransiçãoparamétodoságeis,porexemplo,podeseruma
excelenteideiaformarumclubedolivro,eescolherumlivrosobremétodoságeis
paraenvolvertodaaequipenoaprendizadoquesemdúvidaserámuitoútilnatran-
sição.
BrownBagSessions
“BrownBagSessions”sãoreuniõesduranteapausaparaoalmo çoemqueas
pessoasfazemapresentaçõesecompartilhaminformações. NosEstadosUnidosé
comumqueaspessoaslevemseuslanchesparaoalmo çoemsacosdepapelpardos
(brownbags),comoaquelesqueaspadariascostumamutilizarparapãesaquino
Brasil,daíonome“BrownBagSessions”.
Duranteessasreuniões,geralmente,aspessoascomemenquantoassistemauma
apresentaçãopreparadaporumdosmembrosdotime.Éumaformafácilerápida
desecriarumaoportunidadeparaaprendizado,umavezqueéumhorárioquena
maioriadasvezesmaispessoaspoderãoparticipardoqueantesoudepoisdohorário
detrabalho.
Sevocêgostariaquesuaorganização,investisseemumtempoduranteohorário
detrabalhoparaessetipodeatividadedeaprendizado,“BrownBagSessions”podem
serumaótimaformadesecome çar,porquenãoafetaotempodetrabalhodaequipe.
Aopassoqueaspessoasparticipamdasreuniõeseosresultadossemostrampromis-
sores,oapoiodagestãopararealizaç ãodessasatividadespoderásermaisfacilmente
conquistado.
6.6 H ackathons
UmHackathonéumdiadetrabalhocomfoconoaprendizadoeautodesenvolvi-
mentoatravésdeexperimentosetestesdenovasideias.
UmaempresaaustralianachamadaAtlassianpossuiumeventorealizadoacada
trêsmeseschamadoShipItDays. Nessediatodasasempresasdaempresapodem
escolherumadesuasideiasparatrabalhar,demodoque,aofinalde24horas,todas
devementregaralgumacoisapronta.OutrasempresascomoaFacebookeSpotify
adotaramabordagenssemelhantes[11],eatualmente,essatemsidoumapráticade
inovaçãoeaprendizadoorganizacionalmuitoutilizadaemstartupseorganizações
138

## Página 153

CasadoCódigo Capítulo6. OtimizandooSistema
inovadoras.
Osprojetospodemserfeitosindividualmente,oupodemsercolaborativos. É
comumquenoiníciodoHackathonhajaumtempoemquetodossereúnempara
apresentarsuasideiaseentãoequipessejamformadasdemaneiraauto-organizada.
Muitosdessesprojetosacabamsetornandoprodutosreaisdasempresasquere-
alizamHackathons.Écomumquealgumaequipetenhaideiasparaosprodutosque
desenvolvemporém,poralgumarazão,nãoestãonobacklog,outêmbaixapriori-
dade.Essaéumaoportunidadedetentarcolocaraideiaempráticaeapresentaro
resultadoao Product Ownereaotime.Talvez,aideianuncafaç apartedoproduto,
defato,talveztorne-seumafuncionalidadeimportantedoproduto;oqueinteressa
équeoaprendizadotrazidodaexperiênciapoderáser,porsisó,muitorecompen-
sador.
Hackathonssãooportunidadesparaqueaspessoaspossamaprender,experi-
mentareinovar.Sãoeventosmotivadoresquepermitemqueaequipequebrearo-
tinaeexperimentecoisasqueemumcontextonormaltalvezfossemarriscadasou
teriambaixaprioridade.
6.7 Comunidades de Prática
Organizaçõesprecisamharmonizarpráticas,processos,eferramentasediversosti-
mesedepartamentos,alémdissoaspessoasprecisamcompartilharconhecimentoe
desenvolverem-sealémdoslimitesdasorganizações[9].Paraesseobjetivocultivar
comunidadesdepráticapodeserdegrandeajuda.
Equipeságeis,geralmente,sãocross-funcionais,ouseja,profissionaiscompa-
péiseinteressessemelhantesestãodistribuídosentrediversostimes.Nessecenário,
formarcomunidadesdepráticasparacriaroportunidadesdecompartilhamentoe
aprendizadoparaessesprofissionaispodealavancarconsideravelmenteodesenvol-
vimentodaspessoas.
Imagineumaorganizaçãocom10timesdeScrum,cadatimepossuiumScrum
Master,epelomenosdoistestadores,algunsdesignersealgunsdesenvolvedores.A
criaçãodecomunidadesdepráticanessaorganizaçãopermitiriaqueemmomentos
oportunostodososScrumMasterssereunissemparatratardeassuntosrelevantes
paratodoseles,assimcomotodosostestadores,todososdesignersetodososde-
senvolvedores.Vejanafigura 6.5umexemplo:
139

## Página 154

6.7. ComunidadesdePrática CasadoCódigo
Figura6.5:ComunidadedePrática
Comunidadesdepráticasãogruposdeprofissionaisquecompartilhaminteres-
sescomunsouumaáreacomumdetrabalho.Podemserformadasaoredordetemas,
papéisnaorganização,tecnologiasetc.Osparticipantesaprendemecompartilham
informaçõesrelevantes,ideias,eboaspráticas,epadronizammétodosdetrabalho.
Amaneiracomaqualasorganizaçõeslidamcomascomunidadesdeprática
podevariarbastante,algumaspodempossuircomunidadesdepráticasinformais
quenãosãoreconhecidasnemapoiadaspeloorganizaç ão,outraspodemserreco-
nhecidaseapoiadas[20]equepodeminclusivepossuirresponsabilidades,emui-
tasvezesatéterumtemporeservadoduranteohoráriodetrabalhoparareuniões
ediscussões. Issodependedovalorqueacomunidadedepráticapodeagregarà
organizaçãoedacapacidadedagestãodeenxergareapoiaressasiniciativas.
140

## Página 155

CasadoCódigo Capítulo6. OtimizandooSistema
6.8 E agora, o que eu faço amanhã?
Façaumexercíciocomasuaequipe,crieumalistacomdezproblemasquevocês
tenhamenfrentadonaúltimasemanadetrabalho,eentãoparacadaumdelesve-
rifiquecomoforamresolvidos.Seráquevocêsrealmenteforamembuscadacausa
doproblemaeoresolveramdeumavezportodasousimplesmenteaplicaramum
paliativoparaaliviarossintomasdoproblematemporariamente?
Quetalmarcarumaprimeirarodadadeone-on-ones?
Procureumassuntodeinteressedesuaequipe,eproponhaaformaç ãodeum
ClubedoLivroparafomentaradiscussãoeaprendizado.
Marqueumprimeirocodingdojocomseutime.
Façaumaapresentaçãosobreessecapítulo,emarqueuma“BrownBagSessions”
paraapresentaroquevocêtemaprendido.
Conversecomsuaequipesobreideiasdeprojetos,melhoriasquesemprequise-
ramvernosprodutosdasuaorganizaç ão,ouexperimentosquegostariamdefazer.
QuetalproporumHackathonparacriarumaoportunidadedecolocaressasideias
emprática?
Existealgumassunto,tecnologia,práticaquelheinteressanocontextodasua
organização.Vocêachaqueoutraspessoastambémpoderiamestarinteressadasem
discutireevoluiressetemanasuaorganizaç ão? Quetalformarumacomunidade
práticaemcimadisso?
Proponhaàgestãodasuaorganizaç ãoacriaçãodeumquadrodeautoridade
paradeixarasautonomiadoseutimetransparentedetreasdiversasáreasdedecisão-
chavedoseuprojeto.
141

## Página 157

Capítulo7
ApêndiceA:FerramentasdeApoio
Éessencialparaequipesdistribuídas,ouequipesquepossuemmembrosquetraba-
lhamemregimede home-office(trabalharremotamentedecasa),possuirumsoft-
warequeosajudeamanteravisualizaç ãodofluxodetrabalho,emesmoparatimes
quetrabalhemcolocados,umsoftwarepodeserdegrandeajuda,emboranãoseja
essencial.
Umadasprincipaisvantagensdeseutilizarumsoftwarecomoapoio,sãoasfun-
cionalidadesquepermitemarmazenardetalhesextrasdashistóriasdeusuário,visu-
alizaçãodemétricascomotempodecicloe lead time,geraçãodegráficosdeburn-
downeburnup,entreoutrosfacilitadores.
AlgunssoftwaresquesuportamKanbansão: Acelerato(emportuguês),Lean
KitKanban,AgileZen,TargetProcess,SilverCatalyst,RadTrack,Kanbanery,Versi-
onOne,Greenhopper(comJira),Flow.io,entreoutros.
Sehouverumquadrofísicoeumvirtual,éimportantegarantirqueambosper-
maneçamatualizadoseconsistentes.Porissoexisteopapeldo“StickyBuddy”(su-
geridoporDarrenDavis),quenadamaisédoquealguémqueassumearespon-

## Página 158

CasadoCódigo
sabilidadedemanteroquadrofísicosempreatualizadoemcasodealguémestar
trabalhandoremotamenteenãopodermoverositensdoquadrofísico.
144

## Página 159

CasadoCódigo ReferênciasBibliográficas
ReferênciasBibliográficas
[1] Pairprogramming.http://www.extremeprogramming.org/rules/pair.html.
[2] What is a coding dojo. http://codingdojo.org/cgi-bin/wiki.pl?
WhatIsCodingDojo.
[3] Chaosreport.http://www.standishgroup.com,2008.
[4] LyssaAdkins.Coaching Agile T eams: A Companion for ScrumMasters, Agile Co-
aches, and Project Managers in Transition.Addison-WesleyProfessional,2010.
[5] MarcBenioff;CarlyeAdler. Behind the Cloud: the untold story of how sales-
force.com went from idea to billion-dollar company—and revolutionized an in-
dustry.Jossey-Bass,2009.
[6] ChrisMatts;GojkoAdzic.Featureinjection:threestepstosuccess. http://www.
infoq.com/articles/feature-injection-success,2011.
[7] MauricioAniche. T est-Driven Development: T este e Design no Mundo Real.
CasadoCódigo.
[8] JurgenAppelo. Management 3.0: Leading Agile Developers, Developing Agile
Leaders.Addison-WesleyProfessional,2011.
[9] Jurgen Appelo. Business guilds: Management 3.0 workout.http://www.
management30.com/workout/business-guilds,2012.
[10] JurgenAppelo.Como Mudar o Mundo: Gestão de Mudanças 3.0.2012.
[11] JurgenAppelo. Explorationdays: Management3.0workout. http://www.
management30.com/workout/exploration-days,2012.
145

## Página 160

ReferênciasBibliográficas CasadoCódigo
[12] JurgenAppelo. Delegationboards: Management3.0workout. http://www.
management30.com/workout/delegation-boards,2013.
[13] KentBeck.Extreme Programming Explained: Embrace Change, Second Edition.
Addison-WesleyProfessional,2004.
[14] DaniloSato;HugoCorbucci;MarianaBravo.Codingdojo:anenvironmentfor
learningandsharingagilepractices.2008.
[15] FrederickP.Brooks.The Mythical Man-Month: Essays on Software Engineering.
Addison-WesleyProfessional,1995.
[16] LarryBurns.Building the Agile Database: How to Build a Successful Application
Using Agile Without Sacrificing Data Management.TechnicsPublications,2011.
[17] AlistairCockburn.Agile Software Development:The Cooperative Game, Second
Edition.Addison-WesleyProfessional,2006.
[18] MikeCohn. User Stories Applied: For Agile Software Development. Addison-
WesleyProfessional,2004.
[19] MikeCohn.Agile Estimating and Planning.PrenticeHall,2005.
[20] Mike Cohn. Succeeding with Agile: Software Development Using Scrum.
Addison-WesleyProfessional,2009.
[21] WardCunningham.Technicaldebt.http://c2.com/cgi/wiki?TechnicalDebt.
[22] DianaLarsen;EstherDerby. Agile Retrospectives.PragmaticBookshelf,2006.
[23] EricEvans. Domain-Driven Design: T ackling Complexity in the Heart of Soft-
ware.Addison-WesleyProfessional,2003.
[24] MichaelFeathers. Working Effectively with Legacy Code.PrenticeHall,2004.
[25] NealFord.The Productive Programmer.O’ReillyMedia,Inc.,2008.
[26] WikimediaFoundation. Missãodawikimedia. http://wikimediafoundation.
org/wiki/Mission.
[27] WikimediaFoundation.Visãodawikimedia. http://wikimediafoundation.org/
wiki/Vision.
146

## Página 161

CasadoCódigo ReferênciasBibliográficas
[28] KentBeck;MartinFowler. Planning Extreme Programming. Addison-Wesley
Professional,2000.
[29] MartinFowler. Pairprogrammingmisconceptions.http://martinfowler.com/
bliki/PairProgrammingMisconceptions.html.
[30] OlavMaassen;ChrisMatts;ChrisGeary. Commitment. HathawayteBrake
Publications,2013.
[31] KevlinHenney. 97Things Every Programmer Should Know. O’ReillyMedia,
Inc.,2010.
[32] NormanL.Kerth.Project Retrospectives: A Handbook for T eam Reviews.Dorset
House,2001.
[33] LaurieWilliams;RobertKessler. Pair Programming Illuminated. Addison-
WesleyProfessional,2002.
[34] HenrikKniberg.Kanban and Scrum: making the most of both.Lulu.com,2010.
[35] HenrikKniberg. Lean from the Trenches: Managing Large-Scale Projects with
Kanban.PragmaticBookshelf,2011.
[36] CraigLarman. Agile and Iterative Development: A Manager’s Guide.Addison-
WesleyProfessional,2003.
[37] DeanLeffingwell.Agile Software Requirements: Lean Requirements Practices for
T eams, Programs, and the Enterprise.Addison-WesleyProfessional,2010.
[38] ScottW.Ambler;MarkLines. Disciplined Agile Delivery: A Practitioner’s Guide
to Agile Software Delivery in the Enterprise.IBMPress,2012.
[39] TomDeMarco;TimothyLister. Peopleware: Productive Projects and T eams.
DorsetHouse,1999.
[40] ChrisMatts;OlavMaassen.Realoptionsunderlieagilepractices. http://www.
infoq.com/articles/real-options-enhance-agility,2007.
[41] RobertC.Martin. Clean Code: A Handbook of Agile Software Craftsmanship.
PrenticeHall,2008.
[42] RobertC.Martin. The Clean Coder: A Code of Conduct for Professional Pro-
grammers.PrenticeHall,2011.
147

## Página 162

ReferênciasBibliográficas CasadoCódigo
[43] LindsayRatcliffe;MarcMcNeill. Agile Experience Design: A Digital Designer’s
Guide to Agile, Lean, and Continuous.NewRiders.
[44] TimOttinger.Continuous Improvement In A Flash: A Guide For Scrum Masters.
Leanpub.
[45] CarolSansone;CarolynCMorf;A.T.Panter. The Sage Handbook of Methods
in Social Psychology.SAGEPublications,2004.
[46] RomanPichler.Agile Product Management with Scrum: Creating Products that
Customers Love.Addison-WesleyProfessional,2010.
[47] DanielH.Pink. Drive: The Surprising Truth About What Motivates Us. Ri-
verheadBooks,2011.
[48] MaryPoppendieck;TomPoppendieck. Lean Software Development: An Agile
T oolkit.Addison-WesleyProfessional,2003.
[49] JonathanRasmusson.The Agile Samurai: How Agile Masters Deliver Great Soft-
ware.PragmaticBookshelf,2010.
[50] DonaldG.Reinertsen. Managing the Design Factory.FreePress,1997.
[51] KenHoward;BarryRogers. Individuals and Interactions: An Agile Guide.
Addison-WesleyProfessional,2011.
[52] WinstonRoyce.Managingthedevelopmentoflargesoftwaresystems.1970.
[53] KennethS.Rubin. Essential Scrum: A Practical Guide to the Most Popular Agile
Process.Addison-WesleyProfessional,2012.
[54] HarvardBusinessSchool.Hbselevatorpitchbuilder. http://www.alumni.hbs.
edu/careers/pitch.
[55] KenSchwaber.Agile Project Management with Scrum.MicrosoftPress,2004.
[56] KenSchwaber.The Enterprise and Scrum.MicrosoftPress,2007.
[57] Diana Larsen; James Shore;. Your path through agile fluency.http://
martinfowler.com/articles/agileFluency.html.
148

## Página 163

CasadoCódigo ReferênciasBibliográficas
[58] G.R.Stephenson. Cultural acquisition of a specific learned response among rhe-
sus monkeys. In: Starek, D., R. Schneider, and H. J. Kuhn (eds.). Progress in Pri-
matology.Fischer,1967.
[59] KenSchwaber;JeffSutherland. Software in 30 Days: How Agile Managers Beat
the Odds, Delight Their Customers, And Leave Competitors In the Dust. John
WileyandSons,2012.
[60] ViníciusManhãesTeles. Extreme Programming: Aprenda como encantar seus
usuários desenvolvendo software com agilidade e alta qualidade.NovatecEditora
Ltda.,2004.
[61] AndrewHunt;DavidThomas. The Pragmatic Programmer: From Journeyman
to Master.Addison-WesleyProfessional,1999.
[62] DavidThomas.Codekata:Howtobecomeabetterdeveloper. http://codekata.
pragprog.com/2007/01/code_kata_backg.html,2007.
[63] AlanShalloway;GuyBeaver;JamesR.Trott. Lean-Agile Software Development:
Achieving.Addison-WesleyProfessional,2009.
[64] KentBeck;MikeBeedle;ArievanBennekum;AlistairCockburn;WardCun-
ningham;MartinFowler;JamesGrenning;JimHighsmith;AndrewHunt;Ron
Jeffries;JonKern;BrianMarick;RobertC.Martin;SteveMellor;KenSchwa-
ber;JeffSutherland;Dave Thomas. Manifestoforagilesoftwaredevelopment.
http://agilemanifesto.org,2001.
[65] VersionOne.Stateofagiledevelopmentsurveyresults.
[66] JamesShore;ShaneWarden. The Art of Agile Development.O’Reilly,2007.
[67] LaurieWilliams.Strengtheningthecaseforpair-programming.
[68] James Q. Wilson and George Kelling.The police and neighborhood sa-
fety.http://www.theatlantic.com/magazine/archive/1982/03/broken-windows/
304465/,1982.
149