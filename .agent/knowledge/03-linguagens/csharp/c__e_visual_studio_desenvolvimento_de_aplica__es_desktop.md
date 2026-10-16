---json
{
  "id": "c__e_visual_studio_desenvolvimento_de_aplica__es_desktop",
  "title": "Ce Visual Studio Desenvolvimento de aplicações desktop",
  "categoria": "03-linguagens",
  "subcategoria": "csharp",
  "resumo": "**Arquivo Original:** `C# e Visual Studio Desenvolvimento de aplicações desktop.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "aplica",
    "csharp",
    "desenvolvimento",
    "desktop",
    "linguagens",
    "studio",
    "visual"
  ],
  "perguntas_tipo": [
    "Como utilizar Ce Visual Studio Desenvolvimento de aplicações desktop?",
    "Quais as boas praticas de csharp?"
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
  "dono": "stack-csharp",
  "prioridade": 2
}
---

# C# e Visual Studio Desenvolvimento de aplicações desktop

> **Arquivo Original:** `C# e Visual Studio Desenvolvimento de aplicações desktop.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 1

58814


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

## Página 5

CasadoCódigo
Introdução
Comosempredigonaaberturadetodososmeuslivros,ensinareaprender
sãotarefasqueandamjuntase,paraquesejaalcan çadooobjetivoemcada
umadelas,énecessáriomuitadedica çãoeestudoconstante. Nãohámá-
gicanoaprendizado,mashámuitadetermina çãoporpartedaquelequequer
aprender.
Estelivroapresentaumpoucodoqueo.NETpodeofereceremaplica-
çõesvoltadasaodesktop,fazendousodalinguagemC #edoVisualStudio
comoambiente(IDE–Integrated Development Environment)paraodesen-
volvimento.Cadarecursoapresentadoaquiéconceituadoeexpostopormeio
deexemplospráticos,osquaissãotrazidoscomoobjetivodeagu çarasuacu-
riosidade.
Certamente,estelivropodeserusadocomoumagrandeferramentaem
disciplinasquetrabalhamodesenvolvimentoparaambientesgráficoseinte-
grados(IDE),quersejaporacadêmicosouprofessores. Issoporqueeleéo
resultadodaexperiênciaquetenhoemministraraulasdessadisciplina,então
tragoparacáanseiosedúvidasdosalunosqueestudamcomigo.
Oobjetivodestetrabalhoétorná-loumaferramentapresenteeconstante
noensinoeaprendizadonodesenvolvimentodeaplica çõesparadesktop,fa-
zendousodeC #,maisprecisamenteedeformadirecionadaàsdisciplinas
ministradasemcursosqueenvolvaminformáticaecomputa ção,comoSis-
temasdeInforma ção,CiênciadaComputa ção,ProcessamentodeDados,e
AnáliseeDesenvolvimentodeSistemas. Paraisso,nestelivrotragodefini-
çõeseobserva çõesreferentesàspartesquecompõemodesenvolvimentode
aplicaçõesdesktopedalinguagemC #.Todoodesenvolvimentoérealizado
comauxíliodoVisualStudio2013.
i

## Página 6

CasadoCódigo
Talvezsurjamdúvidasemrela çãoàsversõesdoIDE,masoqueabor-
damosaquiéobásicoparavocêseiniciarnaprograma çãoparaambientes
visuais.Aliás,nãoseráobstáculoalgumcasovocêtenhaacessoaumaversão
diferente(anteriorousuperior)doqueatrabalhada.Issoporqueosconceitos
básicosapresentadosenecessáriosquevocêtenhaestãodisponíveisemtodas
asversõesexistentes.
Olivroétododesenvolvidoemoitocapítulos,todoscommuitaprática,e
deumaconclusãodostópicosvistos.Nasequência,sãoapresentadospeque-
nosresumosdoqueétrabalhadoemcadaumdestescapítulos.
O repositório com todos os códigos-fonte utilizados no li-
vro podem ser encontrados em: https://github.com/evertonfoz/
livro-windows-forms-casa-do-codigo. Estou trabalhando em um
blog, como laboratório para meu próximo livro. Acesse http:
//evertoncoimbra.wix.com/asp-net-mvc-e-efecontribua.
Capítulo1–Asprimeirasimplementações:estruturasequencial
Ostrêsprimeiroscapítulosdestelivroaplicamasestruturasbásicasque
todalinguagemoferece: sequencial,condicionalederepeti ção. Dessama-
neira,nesteprimeirocapítulosãoapresentadosproblemasquepodemser
resolvidosfazendousodeumaestruturasequencial.Duranteasimplemen-
taçõespropostas,princípiosefundamentosrelacionadosàplataforma.NET,
àlinguagemC #eaoVisualStudiotambémsãotrabalhadoseapresentados.
Todosassolu çõesserãobaseadasemumainterfacegráficacomousuário,
nomeadanaplataformacomo Windows Forms Application.
Capítulo2–Evoluindonacomplexidade:estruturacondicional
Dandosequência,estecapítuloapresentanovosproblemasquepodem
serresolvidospormeiodaaplica çãodeestruturascondicionais,tambémco-
nhecidascomoestruturasdesele ção. Paraessasimplementa ções,busca-se
apresentarnovosrecursosparaaplica çõesWindowsForms,assimcomouma
evoluçãonalinguagemC #,comnovosrecursosetécnicas.Umdessesrecur-
sosetécnicasrefere-seàvalida çãodevaloresinformadospelousuário,nos
controlesquepermitemintera ção.
ii

## Página 7

CasadoCódigo
Capítulo3–Resolvendoproblemasmaiscomplexos:estruturade
repetição
Existemsitua çõesnasquaisumproblemaexigeouapresentacomoreso-
luçãoumconjuntodeinstru çõesquedevemserexecutadaspormaisdeuma
vez. Paraessassitua ções,éfeitoousodeumaestruturaderepeti çãoque,
assimcomoacondicional,possuivaria çõesdesuaimplementa ção. Dessa
maneira,esteterceirocapítuloapresentaaúltimadastrêsestruturasbásicas
paraumalinguagemdeprograma ção,trazendoproblemasquepoderãoser
resolvidoscomousodessetipodeestrutura,usandosuasvaria ções.Novos
controleserecursostambémsãoapresentados,comoaleituraeescritadeum
arquivotexto,econtrolesparaintera çãocomconjuntosdedados.Também,
aaplica çãodeOrienta çãoaObjetos(OO)come çaasermostradanestecapí-
tulo.
Capítulo4–Váriosprojetosemumasolução:aplicandoconceitos
relacionadosaoMVCeOrienta çãoaObjetos
Noscapítulosiniciais,apreocupa çãofoinoconhecimentodosrecursos
básicosparadesenvolvimentodeaplica çõesWindowsForms,dalinguagem
C#edoVisualStudio,ondeosprojetoscriadoseramindependentes.Desta
maneira,estecapítuloapresentarecursos,conceitosetécnicasmaisavan ça-
dos,possibilitandoacria çãodeumasolu çãocomváriosprojetos,delegando
responsabilidadesacadaumdelesetornandoasolu çãoumaúnicaaplica ção.
Nessalinha,éapresentadooMVC(Modelo-Visão-Controleou Model- View-
Controller),ummodelodedesenvolvimento–quepodeservistocomoum
padrão–quepermitequecadacamada(noexemplo,cadacamadarefere-se
aumprojeto)realizeespecificamenteoqueédesuaresponsabilidade.Com
vistasàimplementa çãodeumasolu çãoemMVC,técnicasrelacionadasaOri-
entaçãoaObjetossãoapresentadas,assimcomoousodecole ções( collections)
eassocia çãoentreasclasses.
Capítulo5–AcessoadadospormeiodoADO.NET
Atéoquartocapítulo,osdadosutilizadospelaaplica çãosãoobtidose
fornecidosnomesmomomentoemqueelaéexecutada,nãohavendopos-
sibilidadederecuperarfuturamenteosdadosinformadosemumaexecu ção
iii

## Página 8

CasadoCódigo
anterior.Umaexce çãoparaessasitua çãosedánocapítulo 3,ondeépossível
persistirosdadosemumarquivodetextoserecuperá-losemqualquerexe-
cuçãofuturadaaplica ção.Entretanto,normalmenteapersistênciadedados
érealizadaemumabasededados,eo.NEToferecetodaumaarquitetura
paraessafuncionalidade,queéoADO.NET.Aqui,sãoapresentadosrecursos
eferramentasoferecidospelaplataforma,eoVisualStudioquepermitama
persistênciaerecuperaçãodedadosemumabasededados,permitindoapli-
cartodooconteúdojáapresentadoatéestecapítulo.Obancodedadosusado
nestelivroéoSQLServerExpressEdition.
Capítulo6–UtilizandoDataSettipadoparaacessoabasededados
ComoconhecimentodoADO.NET,apresentadonoCapítulo5,noqual
oacessoadadosérealizadopormeiodeclassesdaAPIeinstru çõesSQL,é
possívelsabercomoaintera çãocomobancodedadosocorre.Estecapítulo
avançaeapresentaque,paraacessarumabasededados,éfeitousodeumre-
cursochamadodeDataSetTipado.ODataSetéintroduzido,primeiramente,
semousodetabelasexistentesumumabasededados.Emseguida,sãotra-
balhadosrecursosquebuscamsubsidiarumaagilidadenodesenvolvimento,
comoacria çãodeumformulárioquerepresenteoCRUD( Create, Retrieve,
Update and Delete),comopera çõesdearrastaresoltar.
Capítulo7–ConhecendoaLanguageINtegratedQueryeoWin-
dowsPresentationFoundation
QuandofoiapresentadooADO.NET,asconsultasforamrealizadasfa-
zendousodeinstru çõesSQL,escritascomoumastring.Depois,comaapre-
sentaçãodoDataSetTipado,essasmesmasconsultasforamtransferidaspara
métodos,oquelevouaumaaproxima çãoàOrienta çãoaObjetos. Esteca-
pítuloapresentao Language INtegrated Query(LINQ)comoferramentapara
realizaçãodessasconsultas,quepodemserrealizadasemdiversasfontesde
dados,incluindobasesdedados.ComoLINQ,épossívelfazerusodeobje-
tosemsuasintaxe,permitindousoderecursosdoIDE,comooIntelliSense.
ParaaplicaroLINQ,tambéméfeitousodo Windows Presentation Foundation
(WPF),paraimplementa çãodainterfacegráficacomousuário.
iv

## Página 9

CasadoCódigo
Capítulo8–ApresentandooEntityFrameworkcomoferramenta
paraoMapeamentoObjetoRelacional
Apersistênciadedados,apresentadaemcapítulosanterioresaeste,ére-
alizadapormeiodoADO.NET,quersejafazendousodeinstru çõesSQLou
decomponentesqueencapsulamestasinstru ções(comooDataSetTipado).
ComoEntityFramework(EF),épossíveltrabalhardiretamentecomobjetos,
nãosepreocupandoemcomoaaplica çãoseconectaráaobancoecomoos
dadosserãocapturadosoupersistidos.Ousodesseframeworkpossibilitaao
programadorabstrairetrabalharsemprecomobjetos. Paraaaplica çãodos
exemplos,ocapítulofazusotambémdoWPFparaintera çãocomousuário,
quetrazumaimplementa çãodoCRUD.
Capítulo9–Osestudosnãoparamporaqui
Comestecapítulo,concluímosestelivrodestacandotodososassuntos
quevimosatéaqui,juntodeestímulosparaquevocêcontinuesuajornadade
aprendizagemeaplica çãodoC #.
Casotenhaalgumadúvidaousugestão,procureacomunidadedolivro
paratirardúvidas.Elaestádisponívelem https://groups.google.com/forum/
#!forum/livro-windows-forms-casa-do-codigo. Lápodemosdiscutirmais
sobreostemastratadosaqui.Vocêserámuitobem-vindo!
v

## Página 11

CasadoCódigo
Sobreoautor
EvertonCoimbradeAraújoatuanaáreadetreinamentoedesenvolvimento.
ÉtecnólogoemprocessamentodedadospeloCentrodeEnsinosuperior
deFozdoIgua çu,possuimestradoemCiênciadaComputa çãopelaUFSCe
doutoradopelaUNIOESTEemEngenhariaAgrícola.
ÉprofessordaUniversidadeTecnológicaFederaldoParaná(UTFPR),
campusMedianeira,ondelecionadisciplinasnoCursodeCiênciadaCom-
putaçãoeemespecializa ções.
JáministrouaulasdeAlgoritmos,TécnicasdePrograma ção,Estruturade
Dados,LinguagensdePrograma ção,Orienta çãoaObjetos,AnálisedeSiste-
mas,UML,JavaparaWeb,JavaEE,BancodeDadose.NET.
PossuiexperiêncianaáreadeCiênciadaComputa ção,comênfaseem
AnáliseeDesenvolvimentodeSistemas,atuandoprincipalmentenosseguin-
testemas:DesenvolvimentoWebcomJavae.NETePersistênciadeObjetos.
Oautorépalestranteemsemináriosdeinformáticavoltadosparaomeio
acadêmicoeempresarial.
vii

## Página 13

CasadoCódigo Sumário
Sumário
1 Asprimeirasimplementa ções:estruturasequencial 1
1.1 Trocadevalores . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2 Inserindoimagensemcontroles . . . . . . . . . . . . . . . . . 16
1.3 Obtendoorestodeumadivisão . . . . . . . . . . . . . . . . . 26
1.4 Registrandoogastoemumrestaurante . . . . . . . . . . . . . 33
1.5 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
2 Evoluindonacomplexidade:estruturacondicional 37
2.1 Tomandoumadecisãocombaseemumaidadeidentificada 38
2.2 Identificandoopesoidealparaumapessoa . . . . . . . . . . 48
2.3 Identificandoumreajustesalarial . . . . . . . . . . . . . . . . 55
2.4 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
3 Resolvendoproblemasmaiscomplexos:estruturasderepeti ção 69
3.1 Registrodoconsumodeenergiaemumcondomínio . . . . . 70
3.2 Leituradearquivotextoparacálculodereajusteemfolhade
pagamento . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
3.3 Informa çãodedadosparagera çãodearquivotexto . . . . . 98
3.4 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
4 Váriosprojetosemumasolu ção:aplicandoalgunsconceitosrela-
cionadosaoMVCeàOrienta çãoaObjetos 111
4.1 Introdu çãodosconceitos . . . . . . . . . . . . . . . . . . . . . 112
4.1.1 Objeto . . . . . . . . . . . . . . . . . . . . . . . . . . . 112
ix

## Página 14

Sumário CasadoCódigo
4.1.2 Classe . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
4.1.3 Abstra ção. . . . . . . . . . . . . . . . . . . . . . . . . 114
4.2 Implementandoosconceitosapresentados . . . . . . . . . . . 115
4.3 Associa çõesentreobjetos . . . . . . . . . . . . . . . . . . . . . 118
4.4 Composi çãoentreclassesfazendousodeCollections . . . . 121
4.5 Leituradearquivotextoparacálculodereajusteemfolhade
pagamento . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
4.6 Cria çãodosprojetosedefini çãodedependênciaentreeles . 125
4.7 Criandoacamadadeapresenta ção . . . . . . . . . . . . . . . 130
4.8 Criandoumajanelaprincipalparaaaplica çãoemenuspara
acessoaosformulárioscriados . . . . . . . . . . . . . . . . . . 141
4.9 Associandoobjetosnaimplementa çãodaNotadeEntrada . 147
4.10 Implementandoaintera çãodousuáriocomoregistrodo
CorpodaNotadeCompra . . . . . . . . . . . . . . . . . . . . 152
4.11 Implementandoaintera çãodousuáriocomoregistrodos
produtosdaNotadeCompra . . . . . . . . . . . . . . . . . . 160
4.12 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163
5 AcessoadadospormeiodoADO.NET 165
5.1 Introdu çãoaoADO.NET . . . . . . . . . . . . . . . . . . . . . 166
5.2 CriandoabasededadosutilizandooVisualStudio . . . . . . 167
5.3 Realizandoopera çõesrelacionadasaoCRUDemumatabela
dedados. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 175
5.4 Inserindoregistrosnatabeladefornecedores . . . . . . . . . 179
5.5 Obtendotodososfornecedoresexistentesnabasededados . 183
5.6 Obtendoumfornecedorespecíficonabasededados . . . . . 186
5.7 Removendodatabelaofornecedorselecionado . . . . . . . . 193
5.8 Realizandoaltera çõesemumfornecedorjáinserido . . . . . 195
5.9 Implementandoassocia çõesemtabelasdeumabasededados 198
5.10 Implementandoainterfacecomousuárioparaasassocia ções 208
5.11 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 217
x

## Página 15

CasadoCódigo Sumário
6 UtilizandoDataSetTipadoparaacessoàbasededados 219
6.1 Introdu ção . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 220
6.2 Desenhando o formulário para a implementação de um
exemplodeusodeDataSeteseuscomponentes . . . . . . . . 221
6.3 Implementandoacria ção,popula çãoeintera çãocomoDataSet 224
6.4 DataSetsTipados . . . . . . . . . . . . . . . . . . . . . . . . . . 229
6.5 Atualizandoabasededados . . . . . . . . . . . . . . . . . . . 230
6.6 CriandoosDataSetsTipadosnoVisualStudio . . . . . . . . 238
6.7 EntendendooscomponentesdoDataSetTipado . . . . . . . 243
6.8 CriandoumformulárioquefazusodeumDataSetTipado . 245
6.9 Entendendoocomportamentodoformulárioemrela çãoaos
seuscontroleseaoDataSet . . . . . . . . . . . . . . . . . . . . 252
6.10 Criandoumformulárioutilizandodadosdeumrelacionamento254
6.11 Concluindoosformuláriosparaaaplica çãodecompraevenda 263
6.12 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 291
7 ConhecendoaLanguageINtegratedQueryeoWindowsPresenta-
tionFoundation 293
7.1 Introdu çãoaoWindowsPresentationFoundation . . . . . . 294
7.2 Criandoumaaplica çãoWPF. . . . . . . . . . . . . . . . . . . 294
7.3 Introdu çãoaoLanguageINtegratedQuery . . . . . . . . . . . 300
7.4 Preparandoaaplica çãoparaumaconsultaLINQ . . . . . . . 301
7.5 ImplementandoumaconsultaLINQ . . . . . . . . . . . . . . 303
7.6 ConceitosbásicossobreconsultasnocontextoLINQ . . . . . 304
7.7 Conceitosbásicossobreexpressõesdeconsultas . . . . . . . 306
7.8 SintaxedeconsultasedemétodosnoLINQ . . . . . . . . . . 307
7.9 ExpressõesLambda(lambdaexpressions) . . . . . . . . . . . 308
7.10 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 309
8 ApresentandooEntityFrameworkcomoferramentaparaMapea-
mentoObjetoRelacional 311
8.1 Come çandocomoEntityFramework . . . . . . . . . . . . . 312
8.2 Criandoumprojetoparaaplica çãodoEntityFramework . . 312
xi

## Página 16

Sumário CasadoCódigo
8.3 HabilitandoaAPIdoEntityFramework(NuGetPackageto
Entity)paraoprojeto . . . . . . . . . . . . . . . . . . . . . . . 313
8.4 Criandoocontextocomabasededados . . . . . . . . . . . . 315
8.5 LendoeescrevendodadosnabasededadospormeiodoEF 316
8.6 Identificandoasa çõesdoEntityFramework . . . . . . . . . . 323
8.7 Ainicializa çãodabasededados . . . . . . . . . . . . . . . . . 325
8.8 Implementandoassocia ções/relacionamentos. . . . . . . . . 326
8.9 Estratégiasparainicializa çãodabasededados . . . . . . . . 329
8.10 Populandoabasededadoscomdadosparateste . . . . . . . 331
8.11 Criandoainterfacecomousuárioparaaplicaraassocia ção. 333
8.12 AplicandoBindingdeobjetosemumCRUD . . . . . . . . . 336
8.13 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 345
9 Osestudosnãoparamporaqui 347
Versão:18.9.2
xii

## Página 17

Capítulo1
Asprimeirasimplementa ções:
estruturasequencial
Paraasresolu çõesdosproblemasapresentadosnestelivro,objetivou-seum
padrãoúnicodetrabalho. Cadaenunciadoéacompanhadodeumaanálise
sobreumproblemae,nessaanálise,érealizadaumaexplana çãosobreele,es-
clarecendopontosimportantesparasuacompreensãoe,consequentemente,
auxiliando-onaresolu ção.
Fazpartetambémdecadaenunciadoaapresenta çãodaInterfaceGráfica
comoUsuáriodesejada( Graphical User Interface,tambémconhecidacomo
GUI)edetalhamentossobreofuncionamentoesperado.Todaimplementa-
çãorealizadaemcadatópicoéexplicada,trazendodetalhesquepossamme-
recerumamaioraten çãoporcontadalógicaaplicadaedosrecursosusados.
SemprequefornecessárioutilizarrecursosdoIDE( Integrated Develop-

## Página 18

1.1. Trocadevalores CasadoCódigo
ment Environment)eacontecerdeestesaindanãoteremsidoexplicados,fi-
quemtranquilos!Elesserãoapresentadosdemaneiradetalhada.Issotambém
ocorrerácomosconceitoseastécnicas.Osproblemasapresentadosnesteca-
pítulotrabalhamapenasaformasequencial.
Umaestruturasequencial éumaimplementa ção(programa),naqual
umalinhaéexecutadaapósaoutra,nãoocorrendodesviosourepeti ções.
Praticamentetodasaslinguagenstrabalhamcomessaestruturadeimplemen-
tação. Éamaneiramaissimplesdeprograma çãoeéutilizadaemconjunto
comestruturasdesele ção(condicional)erepeti ção,abordadasnoscapítulos
seguintes.
1.1 Troca de v alores
Pararealizarasolu çãodoproblemadetrocadevalores,crieumaaplica ção,na
qualsejamsolicitadosdoisvaloresaousuárioemumajanela,nãoimportando
otipodedadonestemomento.Emseguida,pormeiodaa çãodeumbotão,
façaosvaloresseremapresentadosdemaneirainversaaousuário.
Comoestelivrotrabalhaaplica çõesWindows,osvaloresserãoinforma-
dosemcontrolesquerepresentamumacaixadetexto. Dessamaneira,essa
trocadoproblemapropostorefere-seaoprocessodeinversãoentreosvalores
informadosnessascaixasdetexto(conhecidasechamadasapartirdeagora
de TextBox).Porexemplo,o TextBoxquerecebeoprimeirovalordeverá
ter,emsi,ovalorinformadoearmazenadonosegundo TextBox,quedeverá
terovalorinformadoearmazenadonoprimeiro.
Afigura1.1representaajanelaresponsávelpelaresolu çãoparaoproblema
proposto.
2

## Página 19

CasadoCódigo Capítulo1. Asprimeirasimplementações:estruturasequencial
Fig.1.1:Interfaceparaoproblemadetrocadevalores
Paraacria çãodaaplica çãonoVisualStudio,representadapelafigura 1.1,
éprecisocriarumprojeto.Entretanto,parasuaforma ção,éimportanteque
elefa çapartedeumasolu ção.
Umasolução(solution)éumprojetoquepodeteroutrosdiversosproje-
tosdentrodele. Elapodeserabstraídacomoumaaplica ção,poisumaapli-
caçãopodeestardivididaemdiversosprojetos,como:umparaacamadade
apresentação;umparatratamentodalógicadenegócio;outroparacontrolar
asintera çõesentreestasduas;eoutro,ainda,paraacessarummecanismode
armazenamentodedados.
NoVisualStudio,umasolu çãoeseusprojetospodemservisualizadosde
maneirahierárquicanajanela Solution Explorer. Paravê-la,acesseo
menu View  Solution Exploreroupressioneacombina çãodeteclas
Ctrl + Alt + L.
Paracriarumasolu çãoparaoprojeto,aindanesseprograma,selecione
omenu File  New Project. Najanelaqueabredentrodacatego-
ria,váem Installed  Templates  Other Project Types 
Visual Studio Solutionseselecioneotemplate Blank Solution.
Nocampo Name,digite SolucaoCapitulo01e,em Location,selecionea
pastaondeelaserácriada.Dentrodapastaselecionadaserácriadaoutracom
onomedasolu ção.Afigura 1.2apresentaajanelaparacria çãodessasolu ção,
tendodestacadasaspartescomentadas.
3

## Página 20

1.1. Trocadevalores CasadoCódigo
Fig.1.2:Janelawizardparaacria çãodeumasolu ção
Apósacria çãoda solution,ajanela Solution Explorerpassaaexibi-
la,comopodeserverificadonafigura 1.3.Detalhessobreasfuncionalidades
dessajanelaserãoapresentadoseexplicadosquandoforemnecessários.
Fig.1.3:JanelaSolutionExplorer
Asolu çãocriadaanteriormenteconterátodososprojetosqueforemcria-
dosnestecapítuloparaefeitodeorganiza ção.Paragerarmosoprimeiropro-
jeto,umdoscaminhoséclicarcomobotãodireitodomouseemcimado
nomedasolu çãono Solution Explorere,então,nomenudecontexto,
4

## Página 21

CasadoCódigo Capítulo1. Asprimeirasimplementações:estruturasequencial
escolheraop ção Add  New Project. Najanelaqueabre,dentroda
categoria Installed  Visual C#  Windows,selecioneo template
Windows Forms Application. Nocampo Name,digite TrocaDeValo-
reseverifiqueseem Location,apastadedestinoéadasolu ção.Dentro
dapastaselecionadaserácriadaoutracomonomedoprojeto. Afigura 1.4
apresentaajanelaparasuacria ção,tendodestacadasaspartescomentadas.
Fig.1.4:Janelawizardparaacria çãodeumprojetoWindowsFormsApplica-
tion
Assim,ajanela Solution Explorerpassaaexibi-lo,comopodeser
verificadonafigura1.5.
5

## Página 22

1.1. Trocadevalores CasadoCódigo
Fig.1.5:JanelaSolutionExplorercomoprojetocriadonasolu ção
Épossívelidentificarnahierarquiadoprojetoaexistênciadealgunsnós(
Propertiese References)ealgunsarquivos( App.config, Form1.cs
e Program.cs).Ainda,comopartedoarquivo Form1.cs,verifica-seou-
tro,o Form1.Designer.cs. Odetalhamentodosnós Propertiese
References edessesarquivosserãoexplicadosconformeforemusados.
Apósacria çãodeumprojetodotipo Windows Forms Application,
otemplateutilizadocria, emconjuntocomele, duasclasses: Program
e Form1. Cada uma delas está implementada em arquivos com o
mesmonome. Aclasse Form1(queestánoarquivo Form1.cs)estende
System.Windows.Forms.Formepodeserrepresentadaporumajanelano
padrãoWindowsquandoinstanciada.
Objetoéqualquerestruturamodularquefazpartedealgo.Elepodeser
algofísico(janela)ouumconceito(expressãomatemática).Umajanela,por
exemplo,éumobjetodeumacasa,deumcarrooudeumsoftwarecomin-
terfacegráficaparaousuário(umformulário). Pensetambémemumli-
vrocomopartedeumabiblioteca. Cadaobjetopossui propriedades,
comportamentose métodosqueoidentificamediferenciamdentreou-
trossemelhantes. Instanciarumaclasseéomesmoqueobterumobjetode
umaclasse.
6

## Página 23

CasadoCódigo Capítulo1. Asprimeirasimplementações:estruturasequencial
Classeéumconjuntoouumacategoriadeobjetosquetêmatributos,pro-
priedadesemétodos(semelhantesàsfun çõeseaosprocedimentos).É,nare-
alidade,aimplementa çãodoscomportamentosquerealizamalgoespecífico
jáprogramado.
Paraumaclasse Livro,verifiquequeelafazpartedeumaclassemais
geral,porexemplo, Publicação. Aestacaracterísticadamosonomede
Generalização.Naclasse Publicação,épossíveldetectaroutrasaindamais
específicas,como Computação, Matemática. Aissodamosonomede
Especialização.Extensãoéaespecializa çãodeumaclasse. Generalizaçãoe
Especializaçãosãotermosrelacionadosà HerançaemOrienta çãoaObjetos
(OO).
AOOseráutilizadademaneiragradativanestelivro.Ocapítulo 4apre-
sentaráeaplicaráessametodologiadeumamaneiramaisaprofundadaees-
pecífica.
OVisualStudioéum AmbienteIntegradodeDesenvolvimento (IDE).
Umadasferramentasdisponibilizadasporeleéa Área de Desenho de
Formulários,destacadanafiguraaseguir.
Fig.1.6:IDEdoVisualStudiocomdestaqueparaaÁreadeDesenhodeFor-
mulários
UmIDEéumambientecompostopordiversasferramentas,dentreelas:
compilador,editordetexto,ferramentaparadepura çãoealgunsacessórios
quetrazemrecursosamaisaoprocessodedesenvolvimento.
7

## Página 24

1.1. Trocadevalores CasadoCódigo
Odesenhodajanela,querepresentaráaaplica çãoresponsávelpelareso-
luçãodoproblemadase ção1.1,sedaránaclassecriadaemconjuntocomo
projeto,apresentadaporpadrãonaáreadedesenhodeformulárioseidenti-
ficadacomo Form1.
Essaatividadededesenhosedáporenquantopeloprocessodearrastare
soltar( drag and drop)controlesparaoformuláriodajanela,edeconfiguraras
propriedadesnecessáriasparacadaumdeles.Oscontrolespossíveisdeserem
arrastadosestãodisponíveisnajanelachamada Toolbox,queéexibidana
figuraaseguir.
Fig.1.7:Janelaquerepresentaabarradeferramentasdecontrolespossíveis
paraseremarrastados
8

## Página 25

CasadoCódigo Capítulo1. Asprimeirasimplementações:estruturasequencial
Existemdiversascategoriasdecontrolesnessajanelaeelasserãoapresen-
tadasdeacordocomanecessidadedeuso.Nesteexemplo,oscontrolesque
usaremosfazempartedacategoria Common Controls.
Paraaaplica çãoexibidanafigura 1.1,seráprecisoarrastartrêscomponen-
tesparaoformuláriodaáreadedesenho:um Label,dois TextBoxeum
Button.Aprincípio,procurepuxaroscomponenteseorganizá-losdama-
neiraapresentada.OVisualStudioofereceas“linhasguias”queorientamo
posicionamentoverticalehorizontal.Issopodeserverificadopelafigura 1.8,
quetemum Labeljáadicionadoemostraum TextBoxsendoarrastado.
Fig.1.8:Janelaapresentandolinhasguiasnomomentodearrastarcomponen-
tesparaoformulário
Cadacontroleinseridonoformulário,assimcomoopróprioformulário,
possuempropriedadesqueprecisamserconfiguradasparaqueoresultado
sejaoesperado. Paraconfiguraraspropriedadesdeumcontrole,épreciso
queeleestejaselecionado,bastandoapenasclicarnele.Feitoisso,énecessário
acessaraJaneladePropriedades( Properties Window),exibidanafigura
1.9.
9

## Página 26

1.1. Trocadevalores CasadoCódigo
Fig.1.9:Janeladeconfigura çãodepropriedadesdecontroles(PropertiesWin-
dow)
Umformulárioéumobjetodaclasse System.Windows.Forms.Form
querepresentaumajanelaouumacaixadediálogo,quepodemservistas
comointerfacecomousuárioemaplica ções.Aclasse Formpodeserusada
paracriarjanelaspadrões,deferramentas,sembordaseflutuantes.Estaspo-
demser Modal,comoumajaneladediálogo.
Utilizandoaspropriedadesdisponíveisnaclasse Form,épossíveldeter-
minaraaparência,tamanhoecor,alémdecaracterísticasdegerenciamento
deumajanelacriada.
10

## Página 27

CasadoCódigo Capítulo1. Asprimeirasimplementações:estruturasequencial
Adocumenta çãosobreaclasse FormpodeserverificadanaMSDN
(Microsoft Developer Network)emhttp://bit.ly/1KDiOM5. Sempreque
houveralgumadúvida,procureacessaraMSDN,poiselaéareferência
oficialparaosrecursosutilizadosnestelivro.
Para acessar a Properties Window, vá ao menu View 
Properties Windowoupressioneatecla F4.
Umacaracterísticadajanelaquevamoscriarénãopermitirqueousuá-
rioaltereseutamanho;algopossívelemalgumasaoarrastardebordas.Este
processo,semternoformulárioumaconfigura çãoadequadadesuaspropri-
edadesedeseuscontroles,farácomqueajanelasejaexibidadeumamaneira
visualerrada.
Aspropriedadesdoformulárioedoscontrolespodemseratribuídaspor
meiodecodifica ção,alémda Properties Window,quandohouverneces-
sidade.Altereovalordaspropriedadesparaesseformulárioconformeapre-
sentadonasequência.
Propriedadesparaoformulário
•Propriedade:FormBorderStyle
•Valorparaatribuir: FixedSingle
ApropriedadeFormBorderStyleéresponsávelpeloestilodabordadaja-
nelaqueoformuláriorepresentará.Elepodeterosseguintesestilosdeborda:
FixedSingle, Fixed3D, FixedDialog, Sizable, FixedToolWindow
e SizableToolWindow.Nomomento,serãodetalhadasapenas Sizable
e FixedSingle.
A Sizable,queéoestilopadrão,permitequeousuárioaltereotama-
nhodajaneladurantesuaexecu ção. JáaFixedSinglenãopermiteessa
mudança,ouseja,ajanelateráasdimensõesatribuídasemtempodedese-
nho.
•Propriedade:Text
11

## Página 28

1.1. Trocadevalores CasadoCódigo
•Valorparaatribuir: Trocadevalores
Apropriedade Textéresponsávelpelaidentificaçãodeumobjeto,como
onomedadoaumavariável.Nãohánecessidadedetodoobjetoterumnome
específicoatribuído,pois,quandoumcontroleéarrastado,oobjetoécriado
eumnomeéautomaticamenteatribuído.Entretanto,casoelesejausadona
codificaçãodesuaaplica ção,éaltamenterecomendadoqueonomeie. Esse
nomepodeseguirumaconven ção,naqualosprimeirostrêsdígitoscaracteri-
zamotipodoobjeto–comofrmparaformulário–eorestanteumadescrição
queassociefacilmenteaoseuconteúdo. Todocontrolepossuiessaproprie-
dade.
•Propriedade:Name
•Valorparaatribuir: frmTrocaDeValores
Apropriedade Name–queaparececomo(Name)najaneladepropri-
edades–éresponsávelpelaidentificaçãodeumobjeto,comoonomedado
aumavariável.Comoditoanteriormente,nãoénecessárionomearoobjeto,
porém,érecomendado,paracasoelesejautilizadoemalgumcódigo.
•Propriedade:Size( Widthe Height)
•Valorparaatribuir: 265paraWidthe115paraHeight
Apropriedade Sizeéresponsávelpeladefiniçãodotamanhodoformu-
lário.Elaésubdivididaemduassubpropriedades: Widthparacomprimento
e Heightparaaltura.Tambéméumapropriedadecomumemcontrolesque
sãoditos“visuais”.
Oscontrolespodemserdivididosem visuaisenãovisuais. Osvisuais
podemserexibidosemformulárioseosnãovisuaissãodisponibilizadospara
otrabalhopormeiodecódigo,oucomoumauxiliaraoutroscontroles.
Emrela çãoaos Labelsarrastadosparaoformulário,ovalorexibido
éLabelX,onde Xéovalorincrementadodeacordocomaquantidadede
Labelsarrastados.Essepadrãodenomea çãodecontroleséomesmopara
12

## Página 29

CasadoCódigo Capítulo1. Asprimeirasimplementações:estruturasequencial
todosostipos. Élógicoqueéprecisodeixarumtextoqueorienteousuá-
rio,comoexibidonafigura 1.1.Destamaneira,aspropriedadesqueprecisam
serconfiguradasparaos Labelssãoapresentadasnasequência.Proprieda-
desjádescritasterãoapenasseusnomesevaloresapresentadosparaserem
atribuídos.
Um Labeléumobjetodaclasse System.Windows.Forms.Label
querepresentaumtextoparaorientarousuárionormalmenteacompanhado
deumacaixadetexto( TextBox).Assimcomoo Form,eleeamaioriados
controlesvisuaispermitemconfigura çõesrelacionadasàsuaaparência.
PropriedadesparaoprimeiroLabel
•Propriedade:Location(XeY)
•Valorparaatribuir: 13paraXe27paraY
Apropriedade Locationéresponsávelpeladefini çãoda posição do
controleemseucontêiner,que,nestecaso,éoformulário.Elaécompostapor
duassubpropriedades:Xparaaposi çãohorizontal(esquerdado container)e
Yparaavertical(seutopo).
•Propriedade:Text
•Valorparaatribuir: Valor1:
PropriedadesparaosegundoLabel
•Propriedade:Location(XeY)
•Valorparaatribuir: 131paraXe27paraY
•Propriedade:Text
•Valorparaatribuir: Valor2:
13

## Página 30

1.1. Trocadevalores CasadoCódigo
Aspropriedadesqueprecisamterseusvaloresconfiguradosparaosdois
TextBoxssãoexibidasnasequência. Apropriedade Textexistetambém
parao TextBoxetemamesmafinalidade.Entretanto,comooobjetivodo
TextBoxépermitiraintera çãocomousuárioparaqueeleinformevalores
quepossamsertrabalhadospelaaplica ção,dificilmenteessapropriedadetem
umvaloratribuídoemtempodedesenho.
Um TextBox é um objeto da classe
System.Windows.Forms.TextBox, que representa uma caixa de
texto,naqualousuáriopoderádigitarvaloresqueservirãocomodadosde
entradaparaaaplica ção. Ovalorinformadoéatribuídonapropriedade
Texte,assimcomotodasaspropriedades,podeseracessadapormeiode
código.
PropriedadesparaoprimeiroTextBox
•Propriedade:Name
•Valorparaatribuir: txtPrimeiroValor
•Propriedade:Location(XeY)
•Valorparaatribuir: 54paraXe24paraY
•Propriedade:Size(WidtheHeight)
•Valorparaatribuir: 70paraWidthe20paraHeight
PropriedadesparaosegundoTextBox
•Propriedade:Name
•Valorparaatribuir: txtSegundoValor
•Propriedade:Location(XeY)
•Valorparaatribuir: 172paraXe24paraY
14

## Página 31

CasadoCódigo Capítulo1. Asprimeirasimplementações:estruturasequencial
•Propriedade:Size(WidtheHeight)
•Valorparaatribuir: 70paraWidthe20paraHeight
PropriedadesparaoButton
Parafinalizaresteprojeto,éprecisoconfigurarocontrole Button.Essa
configuraçãoéapresentadaaseguir.
Um Buttonéumobjetodaclasse System.Windows.Forms.Button
querepresentaumbotãodea ção,noqualalgumtipodeprocessamentoé
disparadoquandoousuáriooclica.
•Propriedade:Image
•Valorparaatribuir: Àescolhadoleitor
Detalhessobreapropriedade Imagesãoapresentadosnase ção1.2.
•Propriedade:Text
•Valorparaatribuir: Valor1:
•Propriedade:ImageAlign
•Valorparaatribuir: MiddleLeft
Apropriedade ImageAlignéresponsávelpeladefini çãoda posição
daimagem nocontroleemqueelaseráinserida. Naescolhadovalorno
Properties Window,asop çõesaparecememformadedesenho.
•Propriedade:Location(XeY)
•Valorparaatribuir: 87paraXe50paraY
•Propriedade:Size(WidtheHeight)
•Valorparaatribuir: 75paraWidthe23paraHeight
•Propriedade:TextAlign
15

## Página 32

1.2. Inserindoimagensemcontroles CasadoCódigo
•Valorparaatribuir: Middleright
Apropriedade TextAlignéresponsávelpeladefiniçãoda posiçãodo
textonocontrole.Naescolhadovalorno Properties Window,asop ções
aparecememformadedesenho,talcomoapropriedade ImageAlign.
1.2 Inserindo imagens em controles
Algunscontrolesvisuais,comonocasodo Button,permitemqueimagens
sejamexibidasporeles.Destamaneira,aoacessarapropriedade Imagedes-
sescomponentes,umajanelaéexibidaparaaimporta çãooureferênciada
imagemqueseráusada.
Fig.1.10:Janelaparasele çãoeimporta çãodeimagens
Nafigura1.10,existemduasmaneirasparaimporta çãodeumaimagem.
Aprimeira, Local resource,importaumaqueestejaarmazenadaemseu
discoparaocontroleemquestão. Dessamaneira,seaimagemintroduzida
forusadamaisdeumavez,seráprecisoimportá-laacadanecessidadede
uso.Parafacilitaresseseuusomúltiplo,existeasegundaop ção: Project
16

## Página 33

CasadoCódigo Capítulo1. Asprimeirasimplementações:estruturasequencial
resource file.Umaimagemimportadaporessaop çãoatraráparaum
arquivochamado Resources,deixando-adisponívelparareúsoemseupro-
jeto.
Dica:Ositehttp://www.iconfinder.com/ofereceumaexcelentefer-
ramentaparaobten çãodeimagens.
Ainterfacecomousuárioestáconcluída. Todososcontrolesinseridos
emumformuláriocausamaescritadeumcódigoreferenteaelesnaclasse
queosrepresenta,nestecaso Form1.Paraverificaressacodifica çãocriada,
no Solution Explorerexpandaonomedoformuláriocriadoedêum
duplocliquenoarquivo Form1.Designer.cs.
Fig.1.11:SolutionExplorerexibindosubarquivosparaformulário
Aoabriroarquivonoeditordecódigos,épossívelverificaraimplemen-
taçãodaclasse Form1,ilustradanafigura 1.12. Nalinha1,verifica-seade-
claraçãodo Namespacequeconteráaclasse;alinha2declaraaclasseem
si;easdeclara çõesentreaslinhas102e106referem-seatodososcontroles
arrastadosparaoformulário.
17

## Página 34

1.2. Inserindoimagensemcontroles CasadoCódigo
Fig.1.12:PartedaclasseForm1quecontémcódigorelacionadoaoscompo-
nentesinseridosnoformulário
Um Namespaceéumrecursoquepermiteorganizarlogicamenteasclas-
ses,criandoumaespéciedeestruturaemárvore,comosefossemdiretórios
oupastas. Dessamaneira,todaclassepossuiseunomedemaneiraqualifi-
cada,ouseja,elecompleto.Nocasodaclasse Form1,seunomequalificado
éTrocaDeValores.Form1.
OC #possuiumrecursomuitointeressantequepermitequeumamesma
classepossuaimplementa çãoemdiversosarquivos.Issoépossívelpormeio
dadefini çãodeclassescomousodapalavrareservada partial.
Aoexecutarmosaaplica ção,elafuncionaráperfeitamentenosentidode
aceitarqueousuáriodigiteosdoisvalores,masnadamaisqueisso,mesmo
18

## Página 35

CasadoCódigo Capítulo1. Asprimeirasimplementações:estruturasequencial
aopressionarobotão Trocar Valores. Pararodá-la, acesseomenu
Debug  Start Without Debuggingoupressioneacombina çãodete-
clas Ctrl + F5.Aindanabarradetarefas,épossívelclicarnobotão Start,
selecionando Releaseno comboboxqueexibe Debug.Estaéamaneiramais
leve;entretanto,casoqueira(ounecessite),épossíveltambémexecutarcom
asop çõesoferecidaspara Debug.
Debug(depuração)éoprocessodeinvestigarumaaplica ção,buscando
corrigirerrosemelhorarperformance. Paraisso,énecessárioferramentas
específicas,quejávêminstaladaseintegradasnoVisualStudio.
Paraqueaaplica çãoapresenteocomportamentodesejadonomomento
emqueousuárioclicarnobotão,deve-seimplementarestafuncionalidade.
Noentanto,todainterfacedeusuáriocriadaéorientadaaeventos.Destama-
neira,éprecisoidentificarumqueocorranomomentodesejado.Nosexem-
plospropostos,essemomentodeverser quandoousuárioclicarnobotão.
Éclaroqueédifíciladivinharquaiseventosestãodisponíveis.Paraisso,
oVisualStudio,pormeiodajanela Properties Window,exibetodosos
eventospossíveisdeseremcapturadosparacadacontroledisponívelnofor-
mulário.Comobotãoselecionado,cliqueem Events,ilustradocomoícone
deumrelâmpagonotopoda Properties Window,eoseventosdisponí-
veisserãoexibidos.
19

## Página 36

1.2. Inserindoimagensemcontroles CasadoCódigo
Fig.1.13:PropertiesWindowexibindooseventosparaumcontrole
Oevento Click,queaparececomoprimeiroeventodisponívelnarela-
çãoexibidanafigura 1.13,éoresponsávelporcapturaromomentoemqueo
usuárioclicanobotão.Paraimplementaressecomportamentodesejado,re-
alizeumduplocliquenaáreaembranco,aoladodonomedele.Issocausará
aaberturadoeditordecódigojácomométodoquerecebeadelega çãodesse
eventocriado(figura1.14).
20

## Página 37

CasadoCódigo Capítulo1. Asprimeirasimplementações:estruturasequencial
Fig.1.14: Estruturadométodoquerecebeadelega çãoparatratamentodo
eventoClick
Todocontrolepossuium eventopadrão e,nocasodo Button,esse
eventoéo Click.Essainforma çãoéútilcasodeseja-seacessardiretamente
ocódigoimplementadoparaele,noeditorvisualdoformulário. Paraisso,
bastarealizarumduplocliquenoprópriocontrole.
Nocódigodafigura 1.14,naslinhas11e13,épossívelconstataradeclara-
çãodo Namespacedaclasse,damesmamaneiraqueforamapresentadosos
códigosgeradospeloscontrolesarrastadosparaoformulário.Éimportante
saber,comoexplicadosobre partial class,queaclassedessearquivo
éamesmadaanteriormenteapresentada. Ocódigoentreaslinhas15e18
referem-seaoconstrutordaclasse.
Métodosconstrutoressãoresponsáveispelainicializa çãodeumobjeto,
21

## Página 38

1.2. Inserindoimagensemcontroles CasadoCódigo
preparando-oparaserusado.
Ométodobutton1_Click()–quenoprefixodeseunometemonome
docontroleeosufixocomonomedoevento–recebeadelega çãodeatender
aoeventoquandoeleocorrer.Esseéopadrãoparatodososnomesdeméto-
dosquerespondemaeventosequesejamcriadosdemaneiraautomáticapelo
VisualStudio.Adelega çãopodeservisualizadanoarquivoquetemtodosos
códigosgeradosdemaneiraautomática,apresentadoanteriormentenafigura
1.12.Vejaessecódigonafiguraaseguir.
Fig.1.15:Códigodeconfigura çõescriadoautomaticamenteparapropriedades
eeventos(arquivoForm1.Designer.cs)
Notequepartedaintera çãocomousuário,queépermitirquesejamin-
formadososvaloresdesejados,estáconcluída.Atrocadessesvaloresocorrerá
quandoobotão Trocar Valoresforpressionado.Ocódigoaserimple-
mentadoéapresentadonasequência.
Resolução1.1:eventoClickparaoButtondetrocadevalores
private void button1_Click ( object sender, EventArgs e) {
string auxiliar;
auxiliar = txtPrimeiroValor.Text;
txtPrimeiroValor.Text = txtSegundoValor.Text;
txtSegundoValor.Text = auxiliar;
22

## Página 39

CasadoCódigo Capítulo1. Asprimeirasimplementações:estruturasequencial
MessageBox.Show( "Troca de valores concluída" ,
"Informação" , MessageBoxButtons.OK,
MessageBoxIcon.Information);
}
Oevento Clickécapturadonomomentoemqueo Button–ouou-
trocontrolequepossuaesseevento–épressionado:oupelobotãoesquerdo
domouse,oupelofocoeatecla Enter(ou Barra de Espaço)emcon-
junto.Amaioriadoscontrolesvisuaisqueinteragemcomousuáriopormeio
domousetemessemesmocomportamento. Dessamaneira,emresolu ções
futuras,esseeventonãoserámaisdescrito.Essasdefini çõessãoválidaspara
todosquetrazemesseevento.
Oprimeiropontoasertratadonocódigoéadeclara çãodavariávelauxi-
liar,quetemseutipodefinidocomo string.Issodeve-seaofatodeapro-
priedade Textdocomponente TextBox,quereceberáovalorinformado
pelousuário,tambémserdefinidaassim.Vejaqueavariável auxiliardo
códigoanteriorrecebeovalorexistentenoprimeiro TextBoxeeste,porsua
vez,recebeovalorexistentenosegundo.Porém,estesegundorecebeuovalor
queestavanoprimeiroanteriormenteequeagoraestánavariávelauxiliar.
Épossívelqueemalgunsexemplosoulivrosquevocêpossaler, use
Stringe string.Ambasdefinemumobjetocomostring;entretantoouso
doprimeirocasorefere-seaotipodedadodefinidopelo.NET,comobasede
implementaçãoparaoutraslinguagens,sendoessaaclassedo namespace
System.String.JástringéotipodedadodalinguagemC #.
OC #utilizaumpadrãoparaquesetrabalhecomapropriedadedeum
controle,sejaparareceberumvalorcomoestásendofeitonessenossocó-
digo(atribui ção),ouparaobterovaloratribuídoaumapropriedade(re-
torno). Dessamaneira, asintaxedainstru çãosempredevereferenciaro
NomeDoControleea propriedadedesejadoseseparadosporumponto.
Apósaexecu çãodasinstru ções,aorodarmosaaplica ção,informarmos
osvaloreseclicarmosnobotão,umamensagemdetérminoéexibida,como
podeservistonafiguraaseguir.
23

## Página 40

1.2. Inserindoimagensemcontroles CasadoCódigo
Fig.1.16:Mensagemdeconfirma çãodatrocadevalores
Ométodoestático Show()daclasse MessageBoxfoiutilizadopara
informaraousuáriootérminodoprocessamentoreferenteàtrocadevalores
entreoscontroles.DiversasclassesemétodosnativosdoC #serãousadose,
amedidaqueosão,terãosuasdescri çõesapresentadas.
A classe System.Windows.Forms.MessageBoxé responsável por
fornecermétodosestáticosparaagera çãodejanelasinformativasedein-
teraçãocomousuário.
Métodosnormalmenteestãoligadosaosobjetos,sendoelesexclusivosde
cadainstância. Entretanto,existemsitua çõesemqueumpodepertencerà
classe,podendoserutilizadoparaqualquerobjetodela. Elessãoconheci-
doscomo métodosestáticos,poisnãoprecisamdeumobjetoepodemser
acessadosdiretamentedaclasse.Éprecisoterciênciadequequalquervariá-
veldeclaradanessaclasseseráacessívelparatodososseusobjetos,eovalor
dessavariávelserásempreomesmoparatodos.
Aassinaturausadanométodo Show()emnossoexemploéa public
static DialogResult Show(string text, string caption,
MessageBoxButtons buttons, MessageBoxIcon icon). Nela são
enviados: otextoaserexibidoaousuário,otítuloparaajanela,osbotões
disponibilizados, e o ícone a ser exibido na barra de títulos. O retorno
refere-seaqualbotãofoipressionadopelousuário.
Ométodoestático System.Windows.Forms.MessageBox.Show()
temcomoresponsabilidadeaexibi çãodemensagensparaousuário,permi-
tindoumaintera ção.Elepossuidiversasassinaturasquemerecemumestudo
aprofundado.Adocumenta çãooferecidapelaMicrosoftérica,bemescritae
comdiversosexemplos.
24

## Página 41

CasadoCódigo Capítulo1. Asprimeirasimplementações:estruturasequencial
Ummétodotemporobjetivorealizaralgumtipodeprocessamento. É
comumqueoproblemaaserresolvidoporelepossuaumconjuntovariável
deparâmetros. Quandoissoocorre,algunstendemadesenvolverdiversos
métodos,umparacadaquantidadeeparatiposdeparâmetrosrecebidos.En-
tretanto,quandotodosresolvemomesmoproblema,écorretoqueeletenha
omesmonome,variandoapenasnaquantidadeetiposdeparâmetrosque
recebe.Aissodamosonomede sobreposição,eacadaconjuntodeparâme-
trosdiferentesparaummesmométodochamamosde assinatura.Otipode
retornonãofazpartedaassinaturaquandosetratadesobreposi ção.
Aoexecutarmosaaplica ção,oquenotamoséosurgimentodoformulário
najanela.Entretanto,antesdeeleserexibido,éprecisoinstanciarsuaclasse.
Verifiqueno Solution Exploreraexistênciadeumarquivochamado
Program.cs.Elerefere-seaumaclassedemesmonome,comummétodo
estáticoespecial,Main().
Veja na figura 1.17 que a terceira linha desse método invoca o es-
tático Application.Run(), enviando como argumento a instância da
classe Form1. Aoinstanciá-la, seuconstrutoréexecutado, invocandoo
InitializeComponent(),declaradonamesmaclasse,porémnoarquivo
Form1.Designer.cs.Oconstrutorestádefinidonoarquivo Form1.cs.
25

## Página 42

1.3. Obtendoorestodeumadivisão CasadoCódigo
Fig.1.17:MétodoMain()invocandooformuláriocriado
OmétodoMain(),diferentedequalqueroutro,éconhecidocomo ponto
de entradaparaumaaplica çãoC #ouWindows. Quandoumaaplica çãoé
iniciada,eleéoprimeiroaserchamado.
1.3 Obtendo o resto de uma divisão
Agora,paratrabalharmosumnovoexemploenovosrecursos,seráimple-
mentandoumprogramaquepermiteousuárioinformardoisnúmeroseque,
aopressionarumbotão,fa çaaaplica çãoretornarorestodadivisãodopri-
meironúmeropelosegundo.
Normalmente,emumaopera çãodedivisão,odesejadoéseuquociente.
Entretanto,nesseproblemaproposto,oquenosinteressaéoseu resto;ouseja,
quantofaltouparaqueadivisãofosseexata. Paraisso,devemosconsiderar
queoquocienteéobrigatoriamenteumnúmerointeiro. OC #ofereceum
operadorderesto,conhecidocomomódulo,eque,nalinguagem,érepresen-
26

## Página 43

CasadoCódigo Capítulo1. Asprimeirasimplementações:estruturasequencial
tadopelosímbolodepercentagem(%).
Afigura1.18representaainterfacedesejadaqueseráimplementadapara
oproblemapropostonestase ção.
Fig.1.18:Interfaceparaoproblemadeobten çãodorestodeumadivisão
Sigaosmesmospassosdacria çãodoprojetoanteriorparaacria çãodesse
segundo,dandoaoprojetoonome RestoDaDivisao.Noanterior,utiliza-
mosoformuláriocriadopelotemplate,o Form1.Porém,oidealéquecada
formuláriotenhaumnomequeorepresente.Assim,elimineesseformulário
doprojeto,pressionandoobotãodireitoeescolhendoaop çãoderemo ção,
ouselecionandooformulárioepressionandoatecla deletedeseuteclado.
Paracriarumformulárionoprojeto,cliquecomobotãodireitodomouse
sobreseunomeeselecione Add  Windows Form.Confirmealinguagem
C#evejaseotemplate Windows Formsestáselecionado,comodemonstra
afiguraaseguir.Nomeieoformuláriocomo FormRestoDeDivisao.cs.
27

## Página 44

1.3. Obtendoorestodeumadivisão CasadoCódigo
Fig.1.19:Janelaparasele çãodetemplatenacria çãodeumWindowsForms
Apósacria çãodoformulário,arrasteoscontrolesparaquefiquemse-
melhantesaoapresentadonafigura 1.18. Sãoosmesmosvistosnoexemplo
anterior.
Emaplicativosquefazemusodejanelas,cadaumadelaspossuiumcon-
juntopadrãodeícones,osquaispermitemqueelasejaminimizada,maximi-
zada,fechadaemovidadelugar.Entretanto,existemjanelasquenãodevem
serminimizadasoumaximizadas,oquelevaanãonecessidadedessesbotões.
Nesteexemplo,essacaracterísticaétrabalhada.
Outroatributoparaessaaplica çãoéaexistênciadeumcontroledeen-
trada( TextBox)quenãodeverápermitiressaintera ção,ouseja,apenas
exibadados. Nasequência,sãoapresentadasasdescri çõesparaasproprie-
dadesdeformulárioaindanãovistaseosvaloresdasjáconhecidas.
Propriedadesparaoformulário
•Propriedade:ControlBox
•Valorparaatribuir: True
28

## Página 45

CasadoCódigo Capítulo1. Asprimeirasimplementações:estruturasequencial
Apropriedade ControlBoxéresponsávelpordefinirseoíconedajanela
conhecidocomo System Menu,exibidonoladoesquerdodabarradetítulo,
serámostradoounão. Atribuindoessapropriedadepara False,todosos
botõesdabarradetítulodeixamdeserexibidos.Ofechamentodajanelapode
ocorrerpelopressionamentoconjuntodasteclas Alt + F4ouporalgum
controlequeimplementeessafun ção.
•Propriedade:FormBorderStyle
•Valorparaatribuir: FixedSingle
•Propriedade:MaximizeBox
•Valorparaatribuir: False
Apropriedade MaximizeBoxéresponsávelpordefinirseobotãode
maximizaçãodeumajanela( Maximize),exibidoemconjuntocomoutros
doisbotões( Minimizee Close)doladodireitodabarradetítulo,será
mostradoounão.
•Propriedade:MinimizeBox
•Valorparaatribuir: True
Apropriedade MinimizeBoxéresponsávelpordefinirseobotãode
minimizaçãodeumajanela( Minimize),exibidoemconjuntocomoutros
doisbotões( Maximizee Close)doladodireitodabarradetítulo,será
mostradoounão.
•Propriedade:Name
•Valorparaatribuir: frmRestoDeDivisao
•Propriedade:Size(WidtheHeight)
•Valorparaatribuir: 331paraWidthe100paraHeight
•Propriedade:Text
29

## Página 46

1.3. Obtendoorestodeumadivisão CasadoCódigo
•Valorparaatribuir: Restodeumadivisão
Noformuláriocriadoparaaaplica ção,insiratrêsLabels,trêsTextBoxs
eum Button.Nos Labels,altereapenasapropriedade Text,deacordo
comoapresentadonafigura 1.18. Use-atambémparaposicionartodosos
controlesnoformulário.
Nos TextBoxs,nomeie-osdeacordocomseuobjetivo.Emcasodedúvi-
das,verifiqueasobserva çõesrelativasaelasnoexemploanterior.O TextBox
queteráaresponsabilidadedeexibirorestodadivisãoterásuaspropriedades
específicasapresentadasnasequência.
Casosejaprecisoatribuirummesmovaloramaisdeumcontrole,épossí-
velselecioná-losefazerissodeumaúnicavez.Paraisso,selecioneoprimeiro
controle,clicandosobreelecomobotãoesquerdodomouse.Paraosdemais,
asele çãoprecisarásercomatecla Ctrlpressionada.Apóstertodososcon-
trolesescolhidos,definaapropriedadedesejadaeatribuaaelaovalor.
PropriedadesparaoTextBox
•Propriedade:Name
•Valorparaatribuir: txtRestoDaDivisao
•Propriedade:ReadOnly
•Valorparaatribuir: False
Apropriedade ReadOnlyéresponsávelpordefinirseocontroledeverá
ounãoreceberofocoduranteanavega çãoentreoscontrolespormeiodo
pressionamentodatecla Tab. Casoovalorseja Falseeousuárioclique
nele,elereceberáofoco.
Todocontrolevisualquepermiteaintera çãocomousuáriopossuiduas
propriedadesresponsáveispelanavega çãodocursor,quandoutilizadaate-
cla Tab. Elassão TabIndex,quemantémaordemdocontroledentrode
seucontêiner;e TabStop,queinformaseocontrolereceberáounãoofoco
30

## Página 47

CasadoCódigo Capítulo1. Asprimeirasimplementações:estruturasequencial
quandoatecla Tabforpressionada.Casodeseje-sequeelenãorecebareal-
menteofocoequetambémnãopermitanenhumaintera ção,servindoape-
nasparaexibi çãodedados,pode-seoptarematribuir Falseàpropriedade
Enabled.
Resolução1.2:eventoClickparaoButtondecálculodorestoda
divisão
private void button1_Click ( object sender, EventArgs e){
int dividendo = Convert.ToInt32(txtDividendo.Text);
int divisor = Convert.ToInt32(txtDivisor.Text);
int resto = dividendo % divisor;
txtResto.Text = resto.ToString();
}
Asduasprimeiraslinhasdocorpodométodorealizamumprocessode
conversão,eoresultadodesseprocedimentoéatribuídoaumanovavariável
queexistiráapenasdentrodométodo.Aterceiralinharealizaaopera çãode
módulopormeiodooperador % atribuindoorestodadivisãoàvariável
resto.
Normalmente,todaentradadedadospormeiodeintera çãodecontro-
lesvisuaistemovalorinformadoarmazenadoemumapropriedadedotipo
string. Essesvalores,comonoexemploapresentado,podemsernecessá-
riosemalgumaopera çãoqueutilizeumtipodedadodiferente,oquelevaà
necessidadedeconverterodadoparaotipodesejado.Aclasse Converter
ofereceváriosmétodosestáticos,querecebemumvaloremumdeterminado
tipoeoconverte,retornandoodadonotipodesejado.Noexemplo,ovalor
enviadoparaométodo ToInt32()éuma stringeseráretornadoporele
um Int32(tipo.NET),querefere-seao intnoC #.Busqueinvestigaressa
classeeseusmétodosnadocumenta çãodoC #.
Ométodo ToString()existeemtodaclasse,jáqueeleédefinidona
classe Object,possíveistodasasclassesestendem-sedela. Suafunciona-
lidadeéretornaruma stringdoobjetoemqueométodoéinvocado. O
ToString()podesersobrescritoemqualquerclasse,casosejanecessário.
Todavariável,classe,campooumétodotemumacaracterísticaemrela-
çãoàsuavisibilidade,ou escopo.Estestermosreferem-sea quempodeaces-
31

## Página 48

1.3. Obtendoorestodeumadivisão CasadoCódigo
sarorecursoequalotempodevidadele.Nométodoapresentado,algumas
variáveisforamdeclaradase,emseguida,inicializadas.Adeclara çãodeuma
variáveloudeumrecurso,porsisó,defineseuescopo.Como,noexemplo,
foramdeclaradasdentrodeummétodo,otempodevidadelaséotempode
vidadométodo,eavisibilidadeéapenasdentrodele.
Épossívelimplementartodoocódigoapresentadoemquatrolinhas,em
apenasumaeissoéumapráticacomum.Porém,emalgunscasos,issopode
torná-loinelegível.Veja:
txtResto.Text = (Convert.ToInt32(txtDividendo.Text) %
Convert.ToInt32(txtDivisor.Text)).ToString();
}
Terminadatodaaimplementa çãoeconfigura çãodoformulário,épre-
cisotestá-lo.Comoessaaplica çãofazpartedeumasolu çãoquejápossuium
projeto,éprecisoinformaraoVisualStudioqualprojetodeveserexecutado
porpadrão.Paraisso,cliquecomobotãodireitodomousesobreseunome,
selecioneaop ção Set as Startup Projecteexecute-o.
Pormeiodafigura 1.20,épossívelverificarajanelaapósainforma ção
dosvaloreseopressionamentonobotão,querealizaasolu çãodoproblema
proposto.
Fig.1.20:Janelacomasolu çãoimplementada
Quandotrabalhamoscomváriosprojetosemumasolu ção,paraidentifi-
carvisualmentequalestáatualmenteemedi ção,bastaverificarqualdelestem
onomeem negrito.
Aimplementa çãorealizadanãotrabalhouahipótesedeousuáriodigitar
nodivisorovalor0(zero).Essaverifica çãodependederecursosaindanão
trabalhados.
32

## Página 49

CasadoCódigo Capítulo1. Asprimeirasimplementações:estruturasequencial
1.4 Registrando o gasto em um restaurante
Parafinalizarosexemplosdestecapítulo,implementeumprogramaqueper-
mitaadigita çãodeumvalorreferenteaumconsumoqualqueremumres-
taurante.Apósousuárioinformaressevalor,osistemaprecisacalcularataxa
deservi çoaserrepassadaaogar çom:10%dovalortotaldaconta.
Algumas características visuais serão trabalhadas na implementação
desseproblema,comoestilovisualdos Labelse TextBoxs,emrela çãoàs
coreseformata ção,eoposicionamentodajanelaquandoaaplica çãoforexe-
cutada.Oproblemaapresentadopeloenunciadoésimplese,comosrecursos
játrabalhados,épossívelrealizaraimplementa ção.
Afigura1.21representaainterfacedesejada,queseráimplementadapara
oproblemapropostonestase ção.
Fig.1.21:Interfaceparaoproblemadeobten çãodogastototalemumrestau-
rante
Crieumnovoprojetodenome GastoEmRestaurantenasolu çãojá
existente. Nele,elimineoformuláriocriadopelotemplateecrieumcha-
mado FormGastoEmRestaurante.Nãoexistemnovoscontrolesparase-
remarrastados;sãonovamente Labels, TextBoxse Button.Sendoassim,
arraste-oseposicione-osconformeafigura 1.21.Asnovaspropriedadestra-
balhadasnesseformuláriosãoapresentadasnasequência.
Propriedadesparaoformulário
•Propriedade:StartPosition
33

## Página 50

1.4. Registrandoogastoemumrestaurante CasadoCódigo
•Valorparaatribuir: CenterScreen
Apropriedade StartPositionéresponsávelpordefiniraposi ção
inicial da janela quando for exibida na primeira vez. Além do valor a
seratribuído,existemasop ções: Manual, WindowsDefaultLocation,
WindowsDefaultBoundse CenterParent.
Emrela çãoaoscontroles,apenasaspropriedadesrelacionadasasuasapa-
rênciasaindanãoforamapresentadas. Issoseráfeitoaseguir. Asdemais,
necessáriasparaoajustedeposi çãoetamanhousadosnoscontroles,jásão
conhecidas. Dessamaneira,arrumeoscontrolesparaassemelharem-seao
layoutapresentadopelafigura 1.21.
PropriedadesparaoLabeldocampoTotal
•Propriedade:Font(Bold)
•Valorparaatribuir: TrueparaBold
Apropriedade Fontécompostapordiversassubpropriedadesqueper-
mitemaconfigura çãodeumestilovisualparaotextoqueo Labelexibe.
Qualqueraltera çãopoderáserverificadaimediatamentenocontrole.Nesse
exemplo,apenasapropriedade Bold(Negrito)étrabalhada.Investigueas
demaisetesteemseuscontroles,nãoapenaso Label.
•Propriedade:ForeColor
•Valorparaatribuir: Blue
Apropriedade ForeColoréresponsávelpeladefiniçãodacoremque
otextoseráexibidonocontrole. Éumapropriedadecomumaoscontroles
visuais.Aoselecioná-la,umalistadecategoriasdecoreséexibida,permitindo
asele çãodadesejada. Noexemplo,acategoriaselecionadafoi Webeacor
Blue.
34

## Página 51

CasadoCódigo Capítulo1. Asprimeirasimplementações:estruturasequencial
PropriedadesparaoTextBoxdoTotal
•Propriedade:BackColor
•Valorparaatribuir: Yellow
A propriedade BackColor é responsável pela definição da cor de
fundodocontrole.Suasele çãoésemelhanteàoferecidaparaapropriedade
ForeColor.
•Propriedade:Enabled
•Valorparaatribuir: False
Apropriedade Enabledéresponsávelpordefinirseocontroleestáou
nãohabilitadoparaintera çãocomousuário,sejapormouseouteclado.
•Propriedade:Font(BoldeItalic)
•Valorparaatribuir: TrueparaBoldeItalic
Aresolu çãoparaoproblemapropostoeaimplementa çãodométodoque
executaoevento Clickdobotãosãoexibidasaseguir.
Resolução1.3:eventoClickparaoButtondecálculodototalda
conta
private void button1_Click ( object sender, EventArgs e) {
txtTotalDaConta.Text = (Convert.ToDouble(
txtDespesa.Text) * 1.10 ).ToString( "N" );
}
Todaaimplementa çãoocorreemapenasumalinha.Aclasse Converté
novamenteusada,porém,comométodo ToDouble(),pelacaracterísticado
valoraserexibido.Achamadado ToString()enviaagoraumargumento,
“N”,queformataa stringparaumvalornumérico.
35

## Página 52

1.5. Conclusão CasadoCódigo
Aformataçãodestrings éumapráticacomum,rápidaeeficientepara
formatarvalorespormeiodachamadaaométodo ToString(). Inicial-
mente,osseparadoresdecentenasedecimaissãoosatribuídosnas Configu-
raçõesRegionais deseusistemaoperacional;porém,issopodeserconfigu-
rado.
AMSDNofereceumavastadocumenta çãosobreisso, sendoum
linkimportante: http://msdn.microsoft.com/en-us/library/dwhawy9k.
aspx(relativoà StandardNumericFormatStrings ).
1.5 Conclusão
Estecapítuloapresentoutrêsproblemaspararesolu çãoeimplementa çãopor
meiodoVisualStudio2013.Cadaumgerouumprojetoetodosficaramalo-
cadosemumasolu ção.Cadaprojetopermitiuapresenta çãodecontroles,téc-
nicaspararesolu ção,conceitosedicassobreaplataforma,eIDEelinguagem.
Osproblemasdesenvolvidospossuemacaracterísticadeumaestrutura
sequencial,naqualofluxodeexecu çãoéumsó.Asresolu çõespropostastra-
balharamcontroles,componentesealgumasdesuaspropriedades,eventose
algunsrecursosdaC #. Essesconteúdossubsidiamumavan çonoconheci-
mentodoambienteedalinguagem,sendopossívelelaborarnovosprojetos
comestruturassemelhantes.
Problemasmaiscomplexosserãoapresentadosnopróximocapítulo,no
qualaestruturacondicionalpermitiráumamaiorcomplexidadeparasuas
resoluções.Pormaissimplesqueosproblemasmostradossejam,foipossível
conhecereaplicaralgunsrecursosdoVisualStudioeconhecerumpoucoda
linguagemC #.
36

## Página 53

Capítulo2
Evoluindonacomplexidade:
estruturacondicional
BuscandofornecernovosrecursosdisponíveisparaosformuláriosWindows
eparaalinguagemC #,estecapítuloapresentaproblemascujaresolu çãopode
dependerdarespostaaumadadaperguntaouumaavalia çãodeumadeter-
minadasitua çãoouexpressão,direcionandosuaexecu çãoparaumcaminho
ououtro.Essedirecionamentoéimplementadoporumaestruturaespecífica
decódigo,conhecidacomo estruturacondicional,ouainda, estruturade
seleção.Asinstru çõesresponsáveispelasuacodifica çãoserãoapresentadas
conformesuautiliza çãonosexemplos.
Umaestruturacondicional éumaimplementa ção,naqualinstru ções,
querepresentamexpressõesdeavalia çãodasrela çõesentreoperadores,dire-
cionamaexecu çãodofluxodecontroledaaplica ção.Issoocorresemprede

## Página 54

2.1. Tomandoumadecisãocombaseemumaidadeidentificada CasadoCódigo
acordocomosresultadosdaavalia çãorealizada.Aestruturacondicionalestá
sempreassociadaàsexpressõescomopera çõesrelacionaisentreumoudois
operadores.
2.1 Tomando uma decisão com base em uma idade
identificada
Comoprimeiroproblemaaserresolvidonestecapítulo,teremosumaescola
denata çãoquematriculaseusalunosemturmasdeacordocomsuacategoria
relacionadaàfaixaetáriadecadaum,conformealistaaseguir.
Faremosumalgoritmoparacalcularaidadedosalunosqueserãomatri-
culados,identificandoaqualcategoriaelepertence.
a) InfantilA:5a7anos;
b) InfantilB:8a10anos;
c) JuvenilA:11a13anos;
d) JuvenilB:14a17anos;
e) Adulto:Maioresde18anos.
Naimplementa çãodasolu çãoparaesseproblema,algunspontosnovos
serãotrabalhados.Inicialmente,parafacilitar,serãosolicitadosapenasoano
denascimentodoalunoeodoseuúltimoaniversário.Adatadoúltimoani-
versárionãopoderáserinformadaantesdadatadenascimento,quedeverá
obviamenteserinferioràdeseuúltimoaniversário. Combasenessapré-
análise,verificam-sealgunseventosquedeverãosercapturados(digita ção
dadatadoúltimoaniversárioantesdadenascimento)ediversascondi ções,
comoverifica çãodeordemnosanosinformadoseaidentifica çãodacatego-
ria,combasenaidadeobtida.
Afigura2.1representaainterfacedesejada,queseráimplementadapara
oproblemapropostonestase ção.
38

## Página 55

CasadoCódigo Capítulo2. Evoluindonacomplexidade:estruturacondicional
Fig.2.1:Interfaceparaoproblemadecálculodeidadeeidentifica çãodeca-
tegoria
Crieumanovasolu çãoparaosprojetosqueserãodesenvolvidosneste
capítulo.Nessasolu ção,crieumprojeto Windows Forms Application.
Nele,crieumformulárioespecíficoparaaimplementa çãodajaneladafigura
2.1.
Acaixaaoladodo Label“Categoria”,pormaisquepareçaum TextBox,
énarealidadeum Labelcomborda. Observetambémqueos Labels
possuemumaletrasublinhada. Sãoconhecidascomoteclasdeatalho,pois
quandocombinadascomatecla Alt,levamaintera ção(ocursor,ouaindao
focodaaplica ção)paraocontroleimediatamenteapóso Labelnaordemde
tabulação.Aspropriedadesespecíficasenovasparaoscontrolesdesseprojeto
sãoapresentadasnasequência.
PropriedadesparaoLabel
•Propriedade:Text
•Valorparaatribuir: &Nome:
Noteovaloraseratribuídonapropriedade Text,o &antesdaletra N.
Essesímbolocausaráaexibi çãodaletraseguinteaele,comosefossecomum
sublinhado. Estarepresentaçãodáàletramarcadaafuncionalidadedeum
“atalho”–quandocombinadacomateclaAlt–paraocontroleimediata-
menteapóso Labelemquestão,deacordocomaordemdetabula ção.
•Propriedade:UseMnemonic
39

## Página 56

2.1. Tomandoumadecisãocombaseemumaidadeidentificada CasadoCódigo
•Valorparaatribuir: True
Apropriedade UseMnemonicéresponsávelpordefinirse,casonapro-
priedade Textdeum Labelexistaosímbolo &,aletraqueessesímbolo
precedeservirádeatalho–quandocombinadacomatecla Alt–paraocon-
troleimediatamenteapósoreferido,tendoapropriedade TabIndexcomo
classificadordestaordem.
•Propriedade:BorderStyle
•Valorparaatribuir: Fixed3D
Apropriedade BorderStyleéresponsávelpordefinirumabordapara
o Label.Normalmente,um Labelnãopossuibordas.
•Propriedade:TextAlign
•Valorparaatribuir: MiddleCenter
•Propriedade:Autosize
•Valorparaatribuir: Faflse
Essapropriedadepermiteoredimensionamentoautomático,combaseno
tamanhodafonte.
•Propriedade:BackColor
•Valorparaatribuir: Yellow
Tendoaconfigura çãovisualsidoterminada,aprimeirafuncionalidade
queseráimplementadaéaresponsávelpornãopermitirqueoanodoúltimo
aniversáriosejadigitadosemqueoanodonascimentooseja. Paraisso,é
precisocapturaroeventoqueocorrequandoocontrolerecebeofoco.Esse
eventoéo Enter.Aimplementa çãoparaométodoquerecebeadelega ção
deatenderaeleéexibidaaseguir.
40

## Página 57

CasadoCódigo Capítulo2. Evoluindonacomplexidade:estruturacondicional
Resolução2.1:eventoEnterparaoTextFieldquerecebeoanodo
últimoaniversáriodoaluno
private void txtAnoUltimoAniversario_Enter ( object sender,
EventArgs e) {
if (txtAnoNascimento.Text.Trim().Length < 4 ) {
MessageBox.Show( "É preciso informar o ANO DE " +
"NASCIMENTO com 4 digitos" , "Atenção!" ,
MessageBoxButtons.OK,
MessageBoxIcon.Information);
txtAnoNascimento.Focus();
}
}
Ainstru ção if(),apresentadaanteriormente,éumainstru çãoavalia-
dora;umaexpressãológica,queavaliaumadeterminadasitua ção/condi ção.
Acondi çãoaquiavaliadaverificaseaquantidadedecaracteresdigitadosno
campoquerepresentaoanodenascimentodoalunoé4.
Paraaavalia çãodessaexpressãoforamusados: ométodo Trim()na
propriedade Textdo TextBox;apropriedade Length,quetodastring
possui;eooperadorrelacional <(menorque). Aopera çãosedáapenas
sobreoresultadode Lengthemcompara çãocomaconstante4. Ouseja,
Trim()operasobre Texteretornauma string,quefornece Length.
Tendoaavalia çãodaexpressãoretornadoumvalorpositivo(verdadeiro),
significaqueoanoinformadopelousuárionãopossui4dígitos, ounão
foiinformado. Dessamaneira,éimportantequeaaplica çãoinformeisso
aousuárioequeoredirecione–ouseja,envieofoco–paraocampoque
precisadodadoinformadodemaneiracorreta. Assim, ainforma çãodo
erro/advertênciaérealizadapelométodo Show()jáconhecido,eofocoé
redirecionadopelachamadaaométodo Focus()docontrolequeodeverá
receber.
Ainstru ção if()éresponsávelpelaimplementaçãodaestruturacondi-
cionalconhecida.empseudocódigo,como SE.Épossívelinserirumaúnica
expressãocomoargumentosparaainstru çãoouvárias.Nocasodemaisde
umaexpressão,elasprecisamserseparadasporumoperadorlógico: &&ou
||,querepresentam,respectivamente, EeOU.
41

## Página 58

2.1. Tomandoumadecisãocombaseemumaidadeidentificada CasadoCódigo
Casoapenasumainstru çãosejaexecutada,nocasodetodoo if()retor-
narverdadeiro,nãohánecessidadedosdelimitadoresdebloco { }.Porém,
comoboaprática,ébomutilizarsempre.Emconjuntocomo if(),épossí-
velusarasinstru ções else(senão)e else if()(senãose).
Ométodo Trim(),pertencenteàclasse String,remove–comaassi-
naturaapresentadanaresolu ção–osespaçosembrancodoinícioedofinal
da stringemqueeleéinvocado.Apósesseprocedimento,eleretornauma
nova string,semosespa ços.Existeumasegundaassinaturaparaométodo,
quepermiteremoverumarraydecaracteresespecíficos.
Apropriedade Length,existenteemqualquerobjeto string,retorna
umvalornuméricointeirocomocomprimentoda string,ouseja,aquan-
tidadedecaracteresqueelapossui.
Osoperadoresrelacionaisestabelecem,comoopróprionomediz,uma
relaçãoentreseusoperandos.Essesoperadoressão: ==(iguala), <(menor
que), >(maiorque), <=(menoreiguala), >=(maioreiguala), !=(diferente
de)eooperadorunário !(não/nega ção).Todaopera çãorelacionalretorna
umvalorlógico,verdadeirooufalso.
OmétodoFocus()éresponsávelporatribuirofocodaaplica ção(cursor
eintera ção)paraocontroleemqueéinvocado.Eleretorna truecasoconsiga
direcionarofoco,e falsecasocontrário.
Outrapreocupa çãorelacionadaàvalida çãodosdadoséagarantiadeque
oanodenascimentosejainferioraoanodoúltimoaniversário.Paraisso,é
precisoidentificarométodoqueéresponsávelporvalidaroquefoidigitado.
Avalida çãotemseucome çonomomentoemqueocontroleperdeofoco.
Quandoissoacontece,háaocorrênciadoevento Validating. Aimple-
mentaçãopodeserverificadanasequência.
Resolução2.2:eventoValidatingparaoTextFieldquerecebeoano
doúltimoaniversáriodoaluno
private void txtAnoUltimoAniversario_Validating ( object
sender, CancelEventArgs e) {
if (Convert.ToInt32(txtAnoUltimoAniversario.Text) <=
Convert.ToInt32(txtAnoNascimento.Text)) {
MessageBox.Show( "O ANO DO ÚLTIMO ANIVERSÁRIO " +
42

## Página 59

CasadoCódigo Capítulo2. Evoluindonacomplexidade:estruturacondicional
"deve ser superior ao do ANO DE NASCIMENTO." ,
"Atenção!" ,
MessageBoxButtons.OK, MessageBoxIcon.Error);
e.Cancel = true ;
}
}
Nocódigoimplementadoparaoevento Validating,aúnicainstru-
çãoaindanãotrabalhadaéa e.Cancel = true.Essainstru çãoatribuium
valorqueinformaqueavalida çãodeveserinterrompida,cancelada,nãoper-
mitindoqueofocosaiadocontrolequeestásendovalidado.
Canceléumapropriedadedaclasse CancelEventArgs,representada
peloobjeto e.Écomummétodosquerecebemdelega çãodeeventosrecebe-
remargumentos.Normalmente,essesargumentossãoenviadospeloevento
e,emalgunscasos,alémdetrabalharinternamentecomosdadosrecebidos
dentrodométodo,aaltera çãodelespodeimplicarnocomportamentodomé-
todoeintera çãodousuáriocomocontrole,comonoexemploapresentado.
Nesteponto,vamosavaliarumpoucoocódigoproposto;paraisso,exe-
cutesuaaplica ção.Digite2000noanodenascimento,2008noanodeúltimo
aniversárioe,depois,2013noanodenascimento.Setudoocorrerbem,oque
eraproibidofoipossíveldeserrealizado.Ouseja,oanodeúltimoaniversário
ficoumenorqueodenascimento.
Talvez,oprimeiropensamentosejaimplementaroevento Validating
docontroledoanodenascimento,damesmamaneiraquefoifeitoparao
controledeanodeúltimoaniversário. Funcionaria,masseriaredundân-
ciadecódigo. Umasolu çãoseriacapturaromesmométodoparaosdois
controles. Issoépossível,poissãocontrolesdomesmotipoeoeventoéo
mesmo. Comofazer? Selecioneo TextBoxdoanodenascimentoe,no
evento Validatingdele,nãodêduplocliquenaáreaembranco,massele-
cioneoeventojáimplementado.Vejanafiguraaseguir.
43

## Página 60

2.1. Tomandoumadecisãocombaseemumaidadeidentificada CasadoCódigo
Fig.2.2: Selecionandoummétodojáimplementadoparaacapturadeum
evento
Aoexecutaraaplica ção,informarumvalorparaanodenascimentoe
pressionaratecla Tabcausaráumerro,poisoanodoúltimoaniversário
nãopossuiaindavalor,oquegeraproblemasnaconversãodeuma string
vaziaparaum Int32.Comoresolver?Estavalida çãosódeveráseraplicada
quandoumvalorjátiversidoinformadoparaoanodoúltimoaniversário.
Dessamaneira,éprecisomudaraexpressãodo if()paraquevalideisso.
Alterepara:
if (txtAnoUltimoAniversario.Text != String.Empty &&
Convert.ToInt32(txtAnoUltimoAniversario.Text) <=
Convert.ToInt32(txtAnoNascimento.Text))
Observenestanovainstru çãoainser çãodeumanovaopera ção,aque
verificaseapropriedade Textdoanodoúltimoaniversárionãoestávazia,
semvalorinformado( !=quesignifica diferentede).Paraessaverifica ção,
utiliza-seapropriedade Emptyde String.Agora,aexpressãopassaaser
composta,possuindoduasopera çõesrelacionais,entãoéprecisoqueelasse-
jamavaliadas.Paraisso,faz-seousodooperadorlógico &&(E),queavalia
aprimeiraopera ção“e”.Aavaliaçãodasegundaopera çãosóocorrerácasoo
resultadoobtidonaprimeirasejaverdadeiro.
Osoperadoreslógicos servemparaavaliarmaisdeumaopera ção.Estes
operadoressãoo &&(E), ||(OU)e ^(OUexclusivo).
Concluídooprocessodevalida çãodosvaloresrelacionadosaosanosde
nascimentoedeúltimoaniversário,éprecisoidentificaraqualcategoriao
alunoseráatribuído.Esteprocessoseráimplementadonoevento Clickdo
Button,epodeserverificadonasequência.
44

## Página 61

CasadoCódigo Capítulo2. Evoluindonacomplexidade:estruturacondicional
Resolução2.3:eventoClickparaoButton
private void btnIdentificarCategoria_Click ( object sender,
EventArgs e) {
if (txtNome.Text == String.Empty ||
txtAnoNascimento.Text == String.Empty ||
txtAnoUltimoAniversario.Text == String.Empty) {
MessageBox.Show( "Todos os dados " +
"solicitados devem ser informados." ,
"Atenção!" , MessageBoxButtons.OK,
MessageBoxIcon.Information);
} else {
int idade =
Convert.ToInt32(txtAnoUltimoAniversario.Text) 
Convert.ToInt32(txtAnoNascimento.Text);
if (idade > 17 ) {
lblCategoria.Text = "Adulto" ;
} else if (idade > 13 ) {
lblCategoria.Text = "Juvenil B" ;
} else if (idade > 10 ) {
lblCategoria.Text = "Juvenil A" ;
} else if (idade > 7 ) {
lblCategoria.Text = "Infantil B" ;
} else if (idade >= 5 ) {
lblCategoria.Text = "Infantil A" ;
} else {
lblCategoria.Text = "Não existe categoria" ;
}
}
}
Aestruturacondicionalimplementadapelainstru ção if()aparecede
umamaneiramaiscompletanoexemplo. Inicialmente,verifica-sesetodos
osdadosobrigatóriosforaminformadose,casoalgumdelesnãocumpraesse
requisito,nadaéprocessado. Passandopositivamenteporessavalida ção,é
obtidaaidadedoaluno,eessaidadeéavaliadaporumasériedeexpressões
disjuntas.Naidentifica çãodacategoria,umtextoéatribuídoao Labelque
aexibirá.
45

## Página 62

2.1. Tomandoumadecisãocombaseemumaidadeidentificada CasadoCódigo
Normalmente,quandoserealizaocadastrodeumapessoa,odadorela-
cionadoàidadepartedeumadatadenascimento.Ocomumésolicitaradata
denascimentocompleta,enãoapenasoano. Entretanto,obteradiferen ça
entreduasdatasnãoenvolveapenasumaopera çãodesubtra ção.
Pararealiza çãodessecálculoedeoutrosqueenvolvamdata,sãousados
recursosoferecidospelalinguagem(classesemétodos).Afigura 2.3trazuma
novaversãoparaaresolu çãodoproblemada Resolução2.1.
Fig.2.3:Utiliza çãodedatasecontroleparacalendário
É possível verificar na nova janela duas mudanças: um calendário (
DateTimePicker)eum Labelqueapresentaadataatual.Paraqueadata
atualsejaexibidanajanelanomomentoemqueelaéexibida,foiimplemen-
tadaessaopera çãonoconstrutordaclassedoformulário.
Resolução2.4:construtordaclassedoformulário
public FormCategoriaPorIdadeV2 () {
InitializeComponent();
lblHoje.Text = "Hoje é " +
DateTime.Now.ToShortDateString();
}
Aclasse DateTimerepresentaasdatasehorasqueestejamnointervalo
de00h:00mde1dejaneirode1601até31dedezembrode9999,emumcalen-
46

## Página 63

CasadoCódigo Capítulo2. Evoluindonacomplexidade:estruturacondicional
dárioconhecidocomo Anno Domini(AD).Esteslimitespodemserobtidos
pelaspropriedades(deleitura) MinValuee MaxValue.Diversosmétodos
sãooferecidosparamanipulardatasehoras,assimcomopropriedadespara
consultareconfigurar.
Apropriedade Nowretornaadataehoraatualcombasenalocaliza-
çãoconfiguradaemseusistemaoperacional. Existemoutrasdiversaspro-
priedades quepodem serutilizadas, como: Date, Day, DayOfWeek,
DayOfYear, Hour, Kind, MiliSecond, Minute, Month, Second,
Ticks, TimeOfDay, Today, UtcNowe Year.
O métodoToShortDateString()formata a data para a máscara
dd/MM/aaaa,ouaquetenhasidoconfiguradanosistemaoperacional.Essa
máscaraexibeodia,mêseano,comvaloresnuméricos.
Assimcomoexistemdiversaspropriedadespara DateTime,existemdi-
versosmétodosquepodemserinvocadosparaoretornodapropriedade Now.
Cabeumaidentifica çãodeleseumainvestiga çãomaisdetalhada.
O DateTimePickeréumcontrolequepermiteaousuárioasele çãode
umadataespecífica,diretamenteemumcalendário.Elepossibilitaanavega-
çãoentremeses,anosesemanas,dentrediversasoutrasfuncionalidades.
Umavezqueajanelatenhasidoalteradaparaasele çãodadatadenasci-
mentoeexibi çãodadataatual,éprecisoalteraraimplementa çãodométodo
quecapturaoevento Click,queestáaseguir.
Resolução2.5:trechocomnovocódigoparaobten çãodaidade
private void btnIdentificarCategoria_Click ( object sender,
EventArgs e) {
// Trecho para validação do nome continua o mesmo e
// foi omitido aqui
TimeSpan tsQuantidadeDias = DateTime.Now.Date 
dtpDataDeNascimento.Value;
int idade = (tsQuantidadeDias.Days / 365 );
// Considerar o ano com 365 dias pode não resultar
// em um valor preciso
47

## Página 64

2.2. Identificandoopesoidealparaumapessoa CasadoCódigo
// Trecho para identificação das categorias continua o
// mesmo e foi omitido aqui
}
Pormeiodasubtra çãodasdatas,armazenandooresultadoemumobjeto
daclasse TimeSpan,épossívelobteretrabalharcomosresultadosrelacio-
nadosàdiferen çadesejada.Essaclassefornecediversaspropriedades,entre
elasa Days,quepossuiaquantidadedediasqueexistementreasduasda-
tasoperadas. Apósessaopera ção,umasimplesdivisãoretorna,demaneira
aproximada,aquantidadedeanosaquesereferemosdiasobtidos.Esseva-
loréaproximadopelofatodenãoseremlevadosemconsidera çãoosanos
bissextos.
Quandooresultadodeumadivisãoéatribuídoaumavariáveldotipo
int,apenasaparteinteira(oquociente)éarmazenada,sendodescartadoo
resto(partefracionária).
Agoraqueosconhecimentosparaobteroquocienteerestodeumadivi-
sãoforamapresentados,procureobteraidadecompletadeumapessoa,em
anos,mesesedias.Lembre-seapenasdequeconsiderarsempreumanocom
365diaseummêscom30diasnãoresultaráemumresultadopreciso.
Aimplementa çãoapresentadatrouxetambém,pelaprimeiravez,ouso
decomentários. Asbarras( //)identificamalinhacomocomentário,dis-
pensandoacompila çãonela.Épossíveltambéminserir comentárioemuma
instruçãofinalizadacompontoevírgula.Existemoutrosmeiosdefazeruso
decomentários,iniciandocom /*eterminandocom */,assimocomentário
seráemváriaslinhas.Casoqueiraqueocomentáriopossagerardocumenta-
çãoemXML,bastausar ///emcadalinhacomentada.
2.2 Identificando o peso ideal para uma pessoa
Dandosequênciacomumnovoproblema,desenvolvaumaaplica çãoque,
aosolicitaraousuárioaalturaesexodeumapessoa,sejapossívelinformar
comoresultadoopesoidealparaosdadosinformados. Paraidentifica ção
dessepeso,utilizeasfórmulasaseguir:
•Parahomens: (72.7*h)-58
48

## Página 65

CasadoCódigo Capítulo2. Evoluindonacomplexidade:estruturacondicional
•Paramulheres: (62.1*h)-44.7
Pelaleituradoenunciado,constata-sequeasolu çãoparaoproblemaé
constituídapor:umasitua çãodeleituradevaloresinformadospelousuário;
realizaçãodeumaanálisesobreestesdados;eatomadadedecisões,tendo
comobaseoresultadodessaanálise.Esteéocenáriotípicoparaproblemas
baseadosemcondi ções,noqualseaplicaumaestruturadesele çãoparaasua
resolução.
Combasenessasitua ção,aaplica çãodesenvolvidaparaesseproblemafaz
usodenovoscontroles,muitocomunsparaproblemascomessacaracterís-
tica.Tambémserãoapresentadasnovastécnicaserecursos.
Afigura2.4representaainterfacedesejada,queseráimplementadapara
oproblemapropostonestase ção.
Fig.2.4:Interfaceparaoproblemadecálculodepesoideal
Verifica-senafiguraquerepresentaaaplica ção,quenãoexistenenhum
botãoparaqueousuáriodispareoprocessamentodesejado.Doisnovoscon-
trolestambémpodemseridentificados:um container,comotítulo Sexoe,
dentrodeste,dois RadioButtons.Oresultadodesejado,queéopesoideal,
podeservisualizadonabasedajanela,comumafontemaior,emnegritoe
cordiferenciada.
Um container,emaplica çõesvisuais,éumcontrolequearmazena
dentrodesioutroscontroles.Atéomomento,apenasoformuláriofoivisto
comoumcontainer.Entretanto,écomumemumajanelaoagrupamentode
49

## Página 66

2.2. Identificandoopesoidealparaumapessoa CasadoCódigo
controles,deacordocomassuascaracterísticas,comoéocasoagoradouso
do GroupBox.
O GroupBoxéumcontainerdeoutroscontroles. Normalmente,den-
trodestecontrole,sãoinseridoscontrolesdotipo RadioButton.Aunião
delespermitequediversasop ções( RadioButtons)possamserinseridas
no GroupBox,comagarantiadequeapenasumadelasestaráselecionada
(checada).
Na Toolbox, nacategoria Containers, selecioneearrasteocon-
trole GroupBoxeposicione-ocorretamentenoformulário.Nacategoriade
controles Common Controlsda Toolbox,selecioneearrasteocontrole
RadioButtonduasvezes,dentrodo GroupBox.Aspropriedadesaserem
configuradasparaessescontrolessãoa Namee Text.Configure-ascombase
naimagemdafigura 2.4.
Comoformuláriocriadoeconfigurado,éprecisodefinireimplemen-
tarocomportamentodesejado.Paraobten çãodopesoideal,comovistona
fórmula,alémdaaltura,éprecisosaberosexodapessoa.Essaresposta,visu-
almente,éfacilmenteobtida,bastandoverificarqual RadioButtonestará
checado.Entretanto,“programaticamente”,paraseobterestaresposta,épre-
cisoverificaroestadodecadaumdeles;seestáchecado,ounão.Essaveri-
ficaçãoérealizadanapropriedade Checked,onde True,o RadioButton
estáchecado,e Falsenão.
Comoum Buttonnãofoiinseridonodesenhodajanela,nãoexiste,
aprincípio,umaa çãoquedispararátodooprocessamento,come çandopor
estaverifica ção.Entretanto,atécnicaadotadanesseexemploéqueoproces-
samentosedaráporeventosdisparadospelaaltera çãodo Sexoeda Altura.
Sendoassim,aclassedoformuláriomanteráumatributoqueseráoresponsá-
velemmantersempreatualizadoosexoinformado.Aseguir,apresentoessa
declaração.
Resolução2.6:trechodedeclara çãodavariáveldoRadioButton
selecionado
namespace ProjetoPesoIdeal {
public partial class CalculoDePesoIdeal : Form {
RadioButton rbnSelecionado = null ;
50

## Página 67

CasadoCódigo Capítulo2. Evoluindonacomplexidade:estruturacondicional
// Código restante omitido
}
}
Avariável rbnSelecionadoseráresponsávelporter,demaneiraatu-
alizada,o RadioButtonqueestejachecado(propriedade Checkedcomo
valor True).Essaatribui çãoserárealizadapelométodoquerecebeadelega-
çãodoevento CheckedChanged.
Resolução2.7:eventoCheckedChangedparaosRadioButtons
private void rbnMasculino_CheckedChanged ( object sender,
EventArgs e) {
RadioButton rbn = (RadioButton) sender;
if (rbn.Checked) {
rbnSelecionado = rbn;
SetPesoIdeal();
}
}
Oevento CheckedChangedédisparadoquandoháalgumamudan ça
na propriedade Checked. Dessa maneira, é possível saber quando um
RadioButtonmudaparaosestadoschecadoounãochecado.
Todososeventosapresentadosatéagoratrazememsuaassinaturaumar-
gumentoespecial,o object sender.Esseobjetotrazparaométodoocon-
trole(ouobjeto)quecausouoevento.Esterecursoémuitoútil,poispermite
queummesmométodoatendaaummesmoeventodediversoscontroles,
comodemonstradonafigura 2.2.
Com esta técnica, independente de qual controle tenha disparado o
evento,ométodosempresaberáqualfoioquecausouoevento.Dessama-
neira,aprimeiralinhadométodo,ondeo sender–apósumaoperação
de cast–éatribuídoàvariávelrbn,garantequeessavariávelterásempreo
controlequedisparouoevento.
O castéumaoperaçãoque“força”,semprequepossível,queumobjetode
determinadotiposejaconvertidoparaoutrotipo,parasuamanipula ção.No
51

## Página 68

2.2. Identificandoopesoidealparaumapessoa CasadoCódigo
exemplo,umobjeto( sender)declaradocomo object,paraseratribuídoa
umavariáveldotipo RadioButton,precisouserexplicitamenteconvertido
paraotipodedestino.
A instrução if()avalia, por meio da propriedadeChecked, se o
RadioButtonquecausouoeventoestáchecado.Casoeleesteja,ocampoda
classe rbnSelecionadorecebeainstânciadoquedisparouoevento.Após
essaatribui ção,ométodo SetPesoIdeal()éinvocado.Essemétodopode
servisualizadonasequência.
Resolução2.8:métodoSetPesoIdeal()
private void SetPesoIdeal () {
try {
double altura = Convert.ToDouble(txtAltura.Text);
double pesoIdeal;
if (rbnSelecionado.Text.Equals( "Masculino" ))
pesoIdeal = ( 72.7 * altura) - 58 ;
else
pesoIdeal = ( 62.1 * altura) - 44.7 ;
lblPesoIdeal.Text = pesoIdeal.ToString( "N" );
}
catch (Exception e) {
MessageBox.Show( "Selecione o sexo e informe a
altura corretamente ", " Atenção! ",
MessageBoxButtons.OK, MessageBoxIcon.Error);
}
}
Existemoutrastécnicasparaidentifica çãodequal RadioButtonestá
checadodentrodeum GroupBox.Umadelasfazusodo Language INtegra-
ted Query(LINQ)eexpressõesLambda,excelentesrecursosoferecidospelo
.NET.OLINQeexpressõesLambdanãoserãotratadosemdetalhesneste
ponto,masserãoapresentadosmaisàfrentenocapítulo 7. ComoLINQe
Lambda,emvezdeterumatributodaclassequeéatualizadoacadaaltera-
çãodeitemselecionado,apenasalinhaseguinteseriasuficiente:
rbnSelecionado = gbxSexo.Controls.OfType<RadioButton>().
SingleOrDefault(r => r.Checked == true );
52

## Página 69

CasadoCódigo Capítulo2. Evoluindonacomplexidade:estruturacondicional
A comparação de r.Checked == true é ilustrativa, pois como
Checkedébooleano,bastariautilizar r.Checked.
Ométodo Equals()éummétodovirtual,quepodesersobrescritopor
qualquerclasse. Elebusca,pormeiodeatributos–oucampos,comosão
chamadosemC #–,verificarseoobjetoqueinvocaométodoéigualaoobjeto
enviadocomoargumentoparaele.Ooperadordeigualdade( ==)éindicado
quandosebuscacompararvaloresquetêmseuarmazenamentoporvalor,e
nãoreferência.Quandoooperador ==forutilizadoentredoisobjetos,oque
ocorreéacompara çãoentreasreferênciasdeles,ouseja,seocupamomesmo
endereçodememória. Dessamaneira,semprequehouvernecessidadede
comparaçãoentreobjetosarmazenadosporreferência,eladeveocorrerpor
meiodométodo Equals().
Existemalgunsnovosrecursosetécnicasnestaimplementa ção. Apri-
meiraéajustificativadeummétodoespecífico. Porquenãoresolverno
métododelegadopeloevento? Bem,ocálculodopesonãoserárealizado
porumeventodeumúnicotipodecontrole.Alémdo CheckedValuedos
RadioButtons,oevento TextChangeddo TextBox,referenteàaltura,
tambémcausaráanecessidadedocálculo.Aseguir,apresentoométodoque
capturaoevento TextChanged.
Resolução2.9:eventoTextChangedparaosTextBoxs
private void txtAltura_TextChanged ( object sender,
EventArgs e) {
SetPesoIdeal();
}
Oevento TextChangedédisparadoquandoháalgumamudan çano
textoexistentenapropriedade Text.Dessamaneira,esseeventoocorre,por
exemplo,acadateclaquegeraumconteúdo.
Emboraasassinaturasdosdoismétodosquerecebemadelega çãodos
eventossejamasmesmas,existemsitua çõesemqueissonãoocorre. Dessa
maneira,nãoseriapossívelousodomesmométodoparaeventoscomassina-
turasdiferentes.Quandoforesteocaso,seriacorretoimplementaramesma
resoluçãoemmaisdeummétodo,oucriarummétodoespecíficoeinvocá-
lo?AsboaspráticaseoparadigmadaOrienta çãoaObjeto(OO)direcionam
53

## Página 70

2.2. Identificandoopesoidealparaumapessoa CasadoCódigo
paraareutiliza ção.Nestecaso,a reutilizaçãoéempregadanacria çãodeum
método.
Areutilizaçãodecódigoéumprocessoduranteodesenvolvimentode
umaaplica çãoqueousuáriofinalnãovê.Elaestádiretamenteligadaà ma-
nutenibilidade,alémdeoutrascaracterísticas.Estaúltimapodeser“notada”
pelousuáriofinal,poisumsistemabem-analisado,modeladoeprojetado,
aplicaareusabilidade,propiciandoumaexcelentemanutenibilidade.Ouseja,
mudançasquepossamocorrernocódigo,sejamestascorretivasouevoluti-
vas,tendemacausarummenorimpactoaousuáriofinal,assimcomosão
implementadasevalidadasemummenortempo.
Paraefeitodemonstrativo,nessaimplementa çãonãoforamusadososblo-
cosdelimitadoresparaasinstru çõesqueserãoexecutadasnaavalia çãoposi-
tivado if(),ounocasodo else.Comoapenasumainstru çãoseráexecu-
tada,aschaves( { })sãodesnecessárias.
OutraboapráticadeOOequefoiaplicadanessaresolu çãoéousode
tratamentodeexce ções.Essatécnicatrabalhaaseguintesitua ção:seexistea
possibilidadedeocorrênciadeerros,ecasoestasnãosejamverificadas(com
if()),oblocoéexecutado;ecasosejaprevistaapossibilidadedeerrosou
exceções,useaestrutura try...catchparaprevenir,capturaretrataresses
eventos.
Otratamentodeexce ções éutilizadoparacapturaretratarsitua çõesde
errosquepossamacontecerduranteaexecu çãodeumprograma. Quando
umaexce çãoacontece,significaquealgumproblemafoidetectado. Sendo
assim,busca-secapturaraexce çãoocorridaetratá-la,paraqueoprograma
nãosejainterrompidodemaneirabruscaousemotratamentodevido.
Naestrutura try...catch,asinstru çõesquefazempartedacláusula
trytêmasemânticade“tentarem”executar.Casoalgumaexceçãoocorra,o
fluxoéimediatamentedesviadoparaainstru ção catch,ignorandoqualquer
instruçãoseguintedacláusula try.
Quandoumaexce çãoocorre, umobjetodaclassequearepresentaé
enviadoparaacláusula catch,quecapturaessaocorrência. Dessama-
neira,épossíveltrataressaexce çãoepermitirumacontinuidadenaexecu ção,
semqueelasejainterrompida,ouqueumamensagemdeerro,queousuá-
rioprovavelmentenãoentenderá,sejaexibida. Existemdiversasexce ções,
54

## Página 71

CasadoCódigo Capítulo2. Evoluindonacomplexidade:estruturacondicional
Exceptionéamaisgeneralizada.
Paraconcluiraimplementa ção, atribuaométodocriadoparaevento
CheckedChanged do RadioButton do sexo masculino, para o
RadioButtondosexofeminino.
2.3 Identificando um reajuste salarial
Parafinalizarosexemplosdestecapítulo,desenvolvaumprogramaquesoli-
citeaousuárioqueinformeosaláriomínimoatualeosseguintesdadosde
umestagiário:oturnodetrabalho,afun çãoeonúmerodehorastrabalhadas
nomês.Combasenoturnodotrabalhodofuncionário,deverásercalculado
umcoeficiente,comosegue:
•Matutino:1%dosaláriomínimo;
•Vespertino:2%dosaláriomínimo;
•Noturno:3%dosaláriomínimo.
Tendoovalordocoeficientecalculado,combaseneleobtenhaosalário
brutodoestagiário,queéoprodutodele(coeficiente)eashorastrabalhadas.
Sobreosaláriobrutoéprecisoobterumimpostohipotéticoaserdescontado,
comosegue:
• Calouro:salário<300,00temimpostode1%;
• Salário>=300,00temimpostode2%;
• Veterano:salário<400,00temimpostode3%;
• Salário>=400,00temimpostode4%.
Paraalgunsestagiários,serátambémpagoumvaloremformadegrati-
ficação. Paraosquepreencheremtodososrequisitos,elaserádeR $50,00;
casocontrário,deR $30,00.
Osrequisitossão:
•Turno:noturno;
55

## Página 72

2.3. Identificandoumreajustesalarial CasadoCódigo
•Númerodehorastrabalhadas: superiora80.
Tambéméoferecidooauxílio-alimentação.Seoestagiáriopreencheral-
gumdosrequisitos,seuauxílio-alimenta çãoserádeumter çodoseusalário
bruto;casocontrário,serádemetadedesteter ço.Osrequisitossão:
•Categoria:calouro;
•Saláriobruto:menorqueametadedosaláriomínimo.
Umaclassifica çãodeveseratribuídaaosaláriolíquido:brutomenosim-
posto,maisgratifica ção,maisauxílio-alimenta ção.Essaclassifica çãodevese-
guirosrequisitosaseguir:
•MenorqueR $350,00:malremunerado;
•EntreR $350,00eR $600,00: normal;
•MaiorqueR $600,00: bemremunerado.
Para a resolução desse problema que possui vários pontos de avali-
ações, será feito uso de outra estrutura condicional (ou de seleção), a
switch...case. Umcontrolede“auxílio”aousuário, conhecidocomo
ToolTip,eumcontrolequerepresentaumalistadevaloresexibidosem
formadelinhas,conhecidocomo ListBox,serãointroduzidostambém
nessaresolu ção.
Afigura2.5representaainterfacedesejada,queseráimplementadapara
oproblemapropostonestase ção.
56

## Página 73

CasadoCódigo Capítulo2. Evoluindonacomplexidade:estruturacondicional
Fig.2.5:Interfaceparaoproblemadecálculodeumsalário
Nafiguraquerepresentaaaplica ção,épossívelverificarumcomponente
queexibeumresultadodosvaloresobtidosapósoprocessamentodosdados
informados.Essecontroleéo ListBox.Tambémévisívelum“balão”com
textoqueauxiliaousuárioemrela çãoaoqueinformaremumdeterminado
campodoformulário,queéo ToolTip.Acaixaemamarelo,querepresenta
asitua çãodosaláriodoestagiário,éum TextBoxcomformata çãoemseu
estilovisual.Osdemaiscontrolessãotodosjáconhecidos.
Umcontrole ListBoxexibeumalistadeitens.Essesitensnormalmente
sãostringsque,umavezselecionadas,podemdispararalgumaa çãonaapli-
cação.Alémdisso,elessãoarmazenadosnapropriedade Itemsepodemser
exibidosemumaúnicacolunaouemmúltiplas.
Paraaexibi çãoemmúltiplascolunas,àpropriedade MultiColumndeve-
seatribuirovalor true.Asele çãodositensnessecontrolepodeserconfigu-
radaparapermitirquemaisdeumitemsejaselecionado.Paraisso,épreciso
configurarapropriedade SelectionMode.Casootamanhovisualdocon-
trole(comositensexibidos)sejainferioràquantidadedositenstantoem
alturaquantocomprimento,barrasderolagemsãoexibidas,quandoconfi-
guradasparaexibi çãoautomática.
57

## Página 74

2.3. Identificandoumreajustesalarial CasadoCódigo
Lembre-sedeconsultarositedaMSDNparaobterinforma çõesdetalha-
daseexemplossobreoscontrolesapresentados.
O ToolTipéumcomponentequeofereceumótimorecursovisualpara
exibiçãodemensagensauxiliadorasparaosusuários.Paraqueotextopossa
serexibido,ousuárioprecisaapontarocursordomouseparaocontroleque
possuaumaconfigura çãoparaesserecurso.
Caberessaltarqueessecomponentenãoérepresentadograficamenteno
formulárioemtempodeimplementa ção.Eleficaalocadoemumaáreaespe-
cíficadaáreadedesenhodeformulários,conformeretratadonafigura 2.6,e
asconfigura çõessãorealizadasnele.Cadacontrolequefaráusodesserecurso
recebeumanovapropriedadequandoo ToolTipéarrastado.Estaproprie-
dadetemonome ToolTip on tooltip1,sendo tooltip1onomedado
aocomponente.
Todososcontrolesnecessáriosestãonacategoria Common Controlsda
ToolBox;arraste-os.Aoarrastaro ToolTip,solte-osobreoformulárioou
sobrealgumcontroledele.Verifique,pormeiodafigura 2.6,queeleficaem
umaáreanãovisualnaáreadedesenhodeformulários,comojácomentado.
Configureosdemaiscontroles,tendoaimagemdafigura 2.5comobase.
58

## Página 75

CasadoCódigo Capítulo2. Evoluindonacomplexidade:estruturacondicional
Fig.2.6:Áreadedesenhodeformulárioscomcontrolesnãovisuais
Comessecontrolenoformulário,umanovapropriedadeéinseridapara
oscontrolesvisuais(figura 2.7).Comoelepermiteconfigura çõesvisuaisque
podemserdiferentesparagruposdistintosdecontroles,épossívelinserir
quantos ToolTipsforemnecessáriose,paracadaum,umanovapropri-
edadeéinserida.
59

## Página 76

2.3. Identificandoumreajustesalarial CasadoCódigo
Fig.2.7:PropriedadeinseridanoscontrolesparaoToolTip
Comexce çãodo Button,oscontrolesterãoseusvaloresmanipuladose
verificadospormeiodecódigo.Dessamaneira,nomeie-osdeacordocoma
suasemântica. Deigualforma,configureapropriedade Textdecadaum
econfigureoestilodo TextBoxaoladodo Buttondamaneiraquepre-
ferir. Parao ListBox,configureafontepara Courier. Aspropriedades
queprecisarãodeumaconfigura çãoespecíficasãoparao ToolTipesão
apresentadasnasequência.
Semprequeprecisarquetodasasletrasdeumtextopossuamomesmo
tamanho,procureescolherumaletramonoespa çada,comoa Courier.
PropriedadesparaoToolTip
•Propriedade:IsBallon
•Valorparaatribuir: True
Quandoessapropriedaderecebeovalor True,otextoauxiliaraparece
emumbalãodediálogoemvezdeemumacaixaretangular.
•Propriedade:ToolTipIcon
•Valorparaatribuir: Info
Nascaixasdeauxílio(oubalões)exibidos,épossíveladicionarumícone,
oquedáumaboavisãosemânticadotipodeauxílioqueestásendoexibido.
Ocontroleoferecetrêspossíveisop ções: Info, Warninge Error.
•Propriedade:ToolTipTitle
•Valorparaatribuir: Ajuda
60

## Página 77

CasadoCódigo Capítulo2. Evoluindonacomplexidade:estruturacondicional
Essapropriedadecolocaemdestaqueumtítuloparaamensagemdeau-
xílioaousuário.
Oproblemapropostonesteexemploempregadiversasverifica ções,com
diversosprocessamentos,inclusivecomdependênciasentreeles. Aliadaa
essanovasitua ção,todaaresolu çãopropostaaquiserádelegadaaummé-
todoespecífico,que,porsuavez,teráaresponsabilidadedetambémdelegar
paramétodosaindamaisespecíficos.Ouseja,nãoéométodoquerecebea
delegaçãodoeventoquetemaresponsabilidadederesolveroproblema.Ele
precisasaberquemresolvee,então,encaminharparaoresponsáveloquea
interfacecomousuáriooferece,comoparâmetros.Aseguir,apresentoomé-
todoparaoevento Clickdo Button.
Resolução2.10:eventoClickparaoButton
private void btnCalcular_Click ( object sender, EventArgs e) {
RadioButton rbnTurno = gbxTurno.Controls.OfType
<RadioButton>().SingleOrDefault(r => r.Checked);
RadioButton rbnCategoria = gbxCategoria.Controls.
OfType<RadioButton>().SingleOrDefault
(r => r.Checked);
RealizarProcessamento(rbnTurno, rbnCategoria,
Convert.ToDouble(txtHorasTrabalhadas.Text),
Convert.ToDouble(txtSalarioMinimo.Text));
}
Oprocessamentoparaobterosvaloresdesejadosédelegadoaummé-
todochamado RealizarProcessamento(). Paracumprirseuobjetivo,
eleprecisasaberquaisop çõesestãoativas–ouqual RadioButtonpossui
apropriedade Checkediguala true–noscontainersdotipoGroupBox.
Dessamaneira,essesvaloressãoobtidoseenviadoscomoargumentopara
essemétodo,quetemseucódigoapresentadonasequência.
Resolução2.11:métodoRealizarProcessamento()
private void RealizarProcessamento (RadioButton rbnTurno,
RadioButton rbnCategoria,
61

## Página 78

2.3. Identificandoumreajustesalarial CasadoCódigo
double horasTrabalhadas,
double valorSalarioMinimo) {
double valorCoeficiente = GetCoeficiente(rbnTurno);
double valorGratificacao =
GetGratificacao(rbnTurno, horasTrabalhadas);
double valorSalarioBruto = horasTrabalhadas *
valorCoeficiente;
double valorImposto = GetValorImposto(rbnCategoria,
valorSalarioBruto);
double valorAuxilioAlimentacao =
GetValorAuxilioAlimentacao(rbnCategoria,
valorSalarioBruto, valorSalarioMinimo);
double valorSalarioLiquido = (valorSalarioBruto +
(valorGratificacao + valorAuxilioAlimentacao)) -
valorImposto;
ApresentarResultados(valorCoeficiente,
valorSalarioBruto, valorImposto,
valorGratificacao, valorAuxilioAlimentacao,
valorSalarioLiquido);
}
Observenaimplementa çãodométodo RealizarProcessamento()
quealgunsvaloressãoobtidospormeiodeinvoca çãoaoutrosmétodos.Esta
técnicaéimportante,poisnãotrazparaummétodoresponsabilidadesdife-
rentesdasqueeleefetivamentetem.Apósarealiza çãodetodososcálculos,
osvaloresobtidossãoapresentadostambémporummétodoespecífico. A
seguir,tragoaimplementa çãoparaométodo GetCoeficiente().
Resolução2.12:métodoGetCoeficiente()
private double GetCoeficiente (RadioButton rbnTurno) {
double valorCoeficiente = 0 ;
switch (rbnTurno.Text) {
case "Matutino" :
valorCoeficiente = Convert.ToDouble(
txtSalarioMinimo.Text) * 0.01 ;
break ;
case "Vespertino" :
62

## Página 79

CasadoCódigo Capítulo2. Evoluindonacomplexidade:estruturacondicional
valorCoeficiente = Convert.ToDouble(
txtSalarioMinimo.Text) * 0.02 ;
break ;
case "Noturno:
valorCoeficiente = Convert.ToDouble(
txtSalarioMinimo.Text) * 0.03 ;
break ;
}
return valorCoeficiente;
}
Todooprocessamentorealizadonessemétodoédefácilleitura. Entre-
tanto,aestruturacondicionaladotada, switch(),aparecepelaprimeira
vez.Essaestruturatrabalhasempreemrela çãoaumvaloravaliado,nocaso
o rbnTurno.Text.Ovalorcontidonessavariávelserácomparadocomas
constantesdecada case.Averifica çãoqueforverdadeiraterátodoocódigo
abaixodelaexecutado.
Devido a essa situação, cada conjunto de instruções atribuído a um
casepossuiumainstru ção break. Paraexemplificar,nocasodovalorde
rbnTurno.Textser “Matutino”,eanãoexistênciado break,todasas
instruçõesabaixoseriamexecutadas,atéqueum breakfosseencontradoou
o switch()finalizado.
Adocumenta çãodereferênciadefineaestruturacondicional switch()
comoumainstru çãodecontrolequelidacomváriassele ções,passandoocon-
troleparaumadasdemonstra çõesdecasosdentrodeseucorpo.Aexecu ção
étransferidaparao case,cujaexpressãoconstantecombinacomovalor
recebidocomoargumentoparao switch().Elapodeincluirqualquernú-
merode case,masdois casesnãopodemteromesmovalorconstante.
Aexecu çãodoblocodeinstru çõescome çanaprimeirainstru çãodo case
selecionadoecontinuaatéqueainstru ção breaksejaencontrada.Essains-
truçãodesalto( break)énecessáriaparacada case,inclusiveoúltimo
(MSDN).
Nasequência,háométodoGetGratificacao().Nele,sãorealizadas
verificaçõesealgunsprocessamentos,algojátrabalhadonolivro,portanto
nãoexigemaioresexplica ções.
63

## Página 80

2.3. Identificandoumreajustesalarial CasadoCódigo
Resolução2.13:métodoGetGratificacao()
private double GetGratificacao (RadioButton rbnTurno,
double horasTrabalhadas) {
double valorGratificacao = 30 ;
if (rbnTurno.Text.Equals( "Noturno" ) &&
horasTrabalhadas > 80 )
valorGratificacao = 50 ;
return valorGratificacao;
}
Ométodo GetValorImposto()érepresentadoaseguir.Nessaimple-
mentação,háousodasduasestruturascondicionaisemconjunto.
Resolução2.14:métodoGetImposto()
private static double GetImposto (RadioButton rbnCategoria,
double valorSalarioBruto) {
double valorImposto = 0 ;
switch (rbnCategoria.Text) {
case "Calouro" :
if (valorSalarioBruto < 300 )
valorImposto = valorSalarioBruto * 0.01 ;
else
valorImposto = valorSalarioBruto * 0.02 ;
break ;
case "Veterano" :
if (valorSalarioBruto < 400 )
valorImposto = valorSalarioBruto * 0.03 ;
else
valorImposto = valorSalarioBruto * 0.04 ;
break ;
}
return valorImposto;
}
Paraobten çãodovalordoauxílio-alimenta ção, éinvocadoométodo
GetAuxilioAlimentacao(),apresentadonasequência.
64

## Página 81

CasadoCódigo Capítulo2. Evoluindonacomplexidade:estruturacondicional
Resolução2.15:métodoGetAuxilioAlimentacao()
private double GetAuxilioAlimentacao (RadioButton
rbnCategoria, double valorSalarioBruto,
double valorSalarioMinimo) {
double valorAuxilioAlimentacao =
(valorSalarioBruto / 3 ) / 2 ;
if (rbnCategoria.Text.Equals( "Calouro" ) &&
(valorSalarioBruto <
(valorSalarioMinimo / 2 )))
valorAuxilioAlimentacao = (valorSalarioBruto / 3 );
return valorAuxilioAlimentacao;
}
Osdadosprocessadosprecisamserapresentadosaousuáriofinal. Para
isso,devemserresponsabilidadedeummétodoespecífico.Nestesentido,o
métodoApresentarResultados()formataeapresentaosresultadosno
controle ListBox,conformeapresentadonasequência.
Resolução2.16:métodoApresentarResultados()
private void ApresentarResultados ( double valorCoeficiente,
double valorSalarioBruto, double valorImposto,
double valorGratificacao, double
valorAuxilioAlimentacao, double
valorSalarioLiquido) {
txtSituacaoEstagiario.Text = GetSituacaoEstagiario(
valorSalarioLiquido);
lbxResumo.Items.Add(String.Format( "{0,-29}{1,12:C}" ,
"Valor do coeficiente:" , valorCoeficiente));
lbxResumo.Items.Add(String.Format( "{0,-29}{1,12:C}" ,
"Salário bruto:" , valorSalarioBruto));
lbxResumo.Items.Add(String.Format( "{0,-29}{1,12:C}" ,
"Valor do imposto :" , valorImposto));
lbxResumo.Items.Add(String.Format( "{0,-29}{1,12:C}" ,
"Valor da gratificação :" , valorGratificacao));
lbxResumo.Items.Add(String.Format( "{0,-29}{1,12:C}" ,
"Valor auxilio alimentação :" ,
65

## Página 82

2.4. Conclusão CasadoCódigo
valorAuxilioAlimentacao));
lbxResumo.Items.Add(String.Format( "{0,-29}{1,12:C}" ,
"Salário líquido:" , valorSalarioLiquido));
}
O último método a ser apresentado é o responsável pela identi-
ficação da situação do qualificador do salário do estagiário, que é o
GetSituacaoEstagiario()epodeservisualizadoaseguir.
Resolução2.17:métodoApresentarResultados()
private string GetSituacaoEstagiario (
double valorSalarioLiquido) {
if (valorSalarioLiquido < 350 )
return "Mal remunerado" ;
else if (valorSalarioLiquido < 600 )
return "Normal" ;
else
return "Bem remunerado" ;
}
Paraconcluiraimplementa ção,apliqueregrasparaqueos TextBoxsnão
estejamvaziosparaarealiza çãodoprocessamento.
2.4 Conclusão
Osproblemasapresentadosnestecapítuloaplicaramumaestruturaconhecida
comoestruturacondicional,oudesele ção. Elapartedeumaavalia ção,que
podeserbaseadaemumaouváriascondi ções.
Trêsenunciadosforampropostose,emcadaumdeles,novastécnicas,re-
cursosdalinguagemecontrolesforamapresentadosetrabalhados.Ressalta-
sequealinguagemC #ofereceduascategoriasparaestruturadesele ção: o
if...elseeo switch...case.Osexemplosbuscaramapresentarouso
isoladodecadaumadelas,mastambémdemonstraramqueelaspodemtra-
balharemconjunto.
Comoconhecimentoadquirido,comanovaestrutura,novoscontroles,
componentes,técnicaserecursosdalinguagem,aumenta-seohorizontede
66

## Página 83

CasadoCódigo Capítulo2. Evoluindonacomplexidade:estruturacondicional
possíveisproblemasquepodemserresolvidos.Opróximocapítulotrabalha
aúltimadastrêsestruturasbásicas,quepropiciaráumconhecimentoainda
maiordalinguagemC #.
67

## Página 85

Capítulo3
Resolvendoproblemasmais
complexos:estruturasde
repetição
Asduasestruturasdeexecu çãodeumfluxodeinstru ções,apresentadasnos
capítulos1e2,trouxeramalgumastécnicaserecursosquepodemser(esão)
usadoscomumente.Entretanto,osproblemaspropostostrabalharamaexe-
cuçãodessesfluxosumaúnicavez.
Existemsitua çõesondeumproblemaexigeouapresentacomoresolu ção
umconjuntodeinstru çõesquedevemserexecutadaspormaisdeumavez.
Paraessassitua ções,éfeitoousodeumaestruturaderepeti ção,que,assim
comoacondicional,possuivaria çõesdesuaimplementa ção. Estecapítulo
trazproblemasquepoderãoserresolvidoscomousodessetipodeestrutura,

## Página 86

3.1. Registrodoconsumodeenergiaemumcondomínio CasadoCódigo
utilizandosuasvaria ções.
Umaestruturaderepeti çãoéumaimplementa çãonaqualumainstru-
ção,ouumconjuntodelas,podeocorrermaisdeumavez.Estaitera çãopode
sesucederumnúmerodeterminadodevezes(repeti çãocontada)oucom
baseemumadeterminadacondi ção(verificadanoinícioouaofinaldaes-
trutura).Alémdessasestruturasclássicas,oC #oferecearepeti çãopara“var-
rer/percorrer”umacoleçãodeobjetos,conhecidacomo for each.
3.1 Registro do consumo de energia em um con -
domínio
Parainiciarosexemplosdestecapítulo,assumaque,emumcondomíniofe-
chadode10residências,acompanhiadefornecimentodeenergiaestáfa-
zendoumlevantamentodeconsumo.Oresponsávelporesselevantamento
informaráaoseuprogramaaquantidadedeKwconsumido(porresidência),
eesseprogramadeveráinformaraquantidadedeKwquerepresenta20%do
totalconsumidodecadaresidência.Aofinal,deveráinformaraproje çãode
consumototaldocondomínio,jádescontadoos20%decadaresidência.
Paraaresolu çãodesteproblema,serátrabalhadoousodeclassesdene-
gócio. OobjetivodestatécnicaétrazernovosconceitossobreOrienta çãoa
Objetos. Tambémseráutilizaremoscoleções( collections),quepossibilitam
quediversosobjetossejamarmazenadosemumúnicoobjeto,comoumcon-
junto.
Emrela çãoacontroles,seráapresentadoo DataGridView,queexibe
diversositens,comoumaplanilha. Aaplica çãodeverápermitiradigita ção
donúmerodacasaeaquantidadeconsumidaemKwparaacasainformada.
Acadaleiturarealizada,o DataGridViewdeveráexibi-la,comotambém
todasasleiturasjárealizadas.Umacasanãopoderátermaisdeumaleitura
realizadae,aofinaldoregistrodetodasasleituras,ousuáriopoderárealizar
oprocessamentoqueinformaráototalconsumidopelocondomínio,ototal
descontadoeovalorcomodesconto.
Afigura3.1representaainterfacedesejada,queseráimplementadapara
oproblemapropostonestase ção.
70

## Página 87

CasadoCódigo Capítulo3. Resolvendoproblemasmaiscomplexos:estruturasde...
Fig.3.1:Interfaceparaoproblemadeconsumodeenergia
Crieumanovasolu çãoparaosprojetosqueserãodesenvolvidosneste
capítulo. Crieumprojeto Windows Application,comumformulário
específicoparaaimplementa çãodajaneladafigura 3.1.Ocontrolequeexibe
asleiturasrealizadaséum DataGridView,queestánacategoria Data.Os
demaisjáconhecemos: Label, TextBoxe Button.
O DataGridViewéumcontrolequepermiteaexibi çãodedadospro-
venientesdediversasfontes,comoregistrosdeumatabelaemumabasede
dadosecole ções. Cadaitemdeumacole ção(oudeumregistrodetabela)
éexibidocomoumalinha,ecadacampodatabela(oupropriedadedeum
objeto)éexibidoemumacoluna. Existemdiversosrecursosquepermitem
personalizarovisualeopera çãodessecontrole.
BuscandointroduzirsempreconceitosrelacionadosàOrienta çãoaObje-
tos,essanovaimplementa çãotraráousodeclassesquerepresentemacamada
demodelodaaplica ção. Ajanelapossibilitaaousuárioinseririnforma ções
referentesaumaleituradeconsumodeenergia.Dessamaneira,aleiturapassa
aserumainstâncialigadadiretamenteaonegóciodaaplica ção.Elafazparte
doproblema.Assim,umaclasseespecíficaparaproverobjetosrelacionados
àleituradecadacasaseráutilizada. A Resolução3.1 trazaimplementa ção
dessaclassedenegócio,quenesseproblemaéchamadade Leitura.
71

## Página 88

3.1. Registrodoconsumodeenergiaemumcondomínio CasadoCódigo
Quandosedesenvolveumaaplica ção,principalmenteumaquebusque
seguiroparadigmadeOrienta çãoaObjetos,objetiva-seaomáximoode-
senvolvimentoemcamadas,ondecadaumadelastemsuaresponsabilidade
eoferecemeiosdeintera çãoentreasdemais.Umpadrãoconhecidoesolidi-
ficadoentreosdesenvolvedoreséo MVC(Modelo-Visão-Controle,doinglês
Model- View-Controller).
Pensandonestesentido,ascamadasdevisãoimplementadasnosprojetos
atéestemomentosãodefácilidentifica çãoesãocompostaspelosformulá-
rios/janelas. Acamadadecontrolepodeservistacomoaclassequetemo
comportamentodoformulárioimplementado,naqualosmétodosrealizam
ocontroleedelega çãodequematendeàsrequisi çõesdousuário.
Nesteexemploagoraproposto,surgeacamadademodelo,tambémco-
nhecidacomocamadadenegócio. Elaéresponsávelporclassesquefazem
parte,demaneiranatural,doproblemaaserresolvido,comoaleiturado
consumodeenergia,nestecaso. Assim,aclassedemodelotemnavisãoos
atributosqueacompõe,eosmétodosquecapturamoseventosdavisãocon-
trolamofluxodeexecu çãodaaplica ção.
Resolução3.1:classedenegócioLeitura
namespace ConsumoEnergiaCondominio {
class Leitura {
public string Casa { get ; set ; }
public double Consumo { get ; set ; }
public double Desconto {
get { return Consumo * 0.20 ; }
}
public Leitura ( string casa, double consumo) {
this .Casa = casa;
this .Consumo = consumo;
}
72
public override bool Equals (Object l) {
Leitura leitura = l as Leitura;
if (litura == null )

## Página 89

CasadoCódigo Capítulo3. Resolvendoproblemasmaiscomplexos:estruturasde...
return false ;
return (Casa.Equals(leitura.Casa));
}
public override int GetHashCode () {
return new { Casa, Consumo}.GetHashCode();
}
}
}
A classe Leitura tem sua implementação dentro donamespace
ConsumoEnergiaCondominio. Ocódigodaclassecome çacomadefini-
çãodesuaspropriedades Casa, Consumoe Desconto. Comexceçãoda
propriedade Desconto,queéapenasdeleitura( get),asoutrasduassãode
escritaeleitura( set/get).
Noteque,nadefini çãodeumapropriedadequesimplesmenterecebeou
retornaumdado,bastaaespecifica çãodonomedométodo.Entretanto,ode-
senvolvedortemtotalliberdadeparaimplementarocomportamentodesses
métodos,deacordocomasuanecessidade.
Umcampodeumaclasse ,quetambémpodeserchamadodevariável
paraobjetos,normalmentetemseuescopodefinidopormodificadoresde
acessocomo privado(private).Comestavisibilidade,essescamposnão
podemseracessadosexternamenteaoobjetoaquepertence.Acombina ção
decamposemétodospúblicosqueosacessaméconhecidocomo proprie-
dade. Cabesalientarqueotermo“campodeumaclasse”éousadonado-
cumentaçãodatecnologiadaMicrosoft. Assim,otermo“atributodeuma
classe”éequivalenteaeste.
Umapropriedadeéummembroqueforneceummecanismoflexívelpara
ler,gravaroucalcularovalordeum campoparticular.Propriedadespodem
serusadascomosefossemmembrosdedadospúblicos,massãométodos
realmenteespeciais,chamadosacessores. Issopermitequeosdadossejam
acessadoscomfacilidadeeaindaajudaapromoveraseguran çaeaflexibili-
dadedosmétodos.
ParacriarumapropriedadenoVisualStudio,noeditordecódigosdigite
prope,emseguida,pressioneatecla Tab.Assim,aestruturabásicadeuma
73

## Página 90

3.1. Registrodoconsumodeenergiaemumcondomínio CasadoCódigo
propriedadeseráfornecida.Casosedesejepersonalizarométodo set,ova-
lorrecebidopelométodoestaráemumavariávelimplícitachamada value.
Umavezquealeituraporcasadeveocorrerapenasumavez,épreciso
garantirquenãosejaminformadas,demaneiraequivocada,duasoumaislei-
turas.Comoosobjetosserãoarmazenadosemumacole ção,hápossibilida-
desdeseverificarsedeterminadoobjetoencontra-seemumasele ção.Para
queessacompara çãosejarealizada,cadaobjetoprecisaterummeioúnico
deseridentificado.Issopodeserrealizadocomaimplementa çãodosméto-
dos Equals()e HashCode(),comopodeserverificado,emdestaque,na
sequência.
Resolução3.2:classedenegócioLeitura,comdestaqueparaosmé-
todosEquals()eHashCode()
namespace ConsumoEnergiaCondominio {
class Leitura {
// Implementação ocultada
public override bool Equals (Object l) {
Leitura leitura = l as Leitura;
if (leitura == null )
return false ;
return (Casa.Equals(leitura.Casa));
}
public override int GetHashCode () {
return new { Casa, Consumo}.GetHashCode();
}
}
}
Ocapítulo2apresentouométodo Equals()(seção2.2)eseuobjetivo
decompara çãodeobjetos,pormeiodesuaspropriedades. Entretanto,tal
exemplotrabalhoucomstringseacompara çãofoirealizadacombasene-
las. Todavia,écomumacompara çãoentreobjetosdeclassesimplementa-
daspeloprogramador,comonocasoa Leitura.Quandoessanecessidade
ocorre,éimportantequeoprogramadorsobrescrevaosmétodos Equals()
e HashCode(),comofoifeitonaclasseda Resolução3.1enesta(represen-
74

## Página 91

CasadoCódigo Capítulo3. Resolvendoproblemasmaiscomplexos:estruturasde...
tamamesmaclasse).
Umcódigohash éumvalornuméricoqueéusadoparaidentificarum
objetoduranteotestedeigualdade. Elepodetambémservircomoumín-
diceparaumobjetoemumacole ção.Aimplementa çãopadrãodométodo
GetHashCode()nãogaranteumúnicovalorderetornoparadiferentesob-
jetos. Dessamaneira,aimplementa çãopadrãodessemétodonãodeveser
utilizadacomooidentificadorúnicodeumobjetoparapropósitosde hashing.
Aimplementa çãodométodo Equals()paraaclasse Leiturarealiza
umaopera çãode castparaatribuiraumavariáveldotipo Leituraoobjeto
querecebeucomo Object.Casoo castsejabemsucedido,verifica-seseo
valordavariávelrecebidaéounãonulo.Aidentifica çãoúnicaparaaclasse
Leituraestáapenasnapropriedade Casa,umavezquenãoépermitida
aleituradeconsumoparaduascasas. Comoapropriedade Casaéuma
string,ométodoretornaoresultadodacompara çãodacasadoobjetoatual,
comoobjetorecebido.
ParasobrescreverummétodonoVisualStudio,digite overrideepres-
sioneatecladeespa ço. Todososmétodosquepossamsofrerasobrescrita
aparecerão.Bastaselecionarodesejadoeaimplementa çãopadrãoseráexi-
bida,sendosuficienteapenaspersonalizarocódigodeacordocomasneces-
sidades.
Quandoseestendeumaclasse,existesempreapossibilidadedequemé-
todosimplementadosnelapossam(oudevam)sersobrescritos,ouseja,ter
seucomportamentoredefinidonasubclasse.A sobrescrita(overriding)
éumrecursodoparadigmaorientadoaobjetos.Ométodosobrescritopode,
ainda,fazerusodocomportamentodefinidoemsuasuperclasse. Paraum
métodopodersersobrescritoemsuadefini ção,eleprecisasermarcadocom
apalavravirtuale,aosersobrescrito,deveterapalavra override.
Em rela ção à implementa ção personalizada para o método
GetHashCode(),optou-sepelacria çãodeumobjetodetipoanônimo,com
osvaloresdaspropriedades Casae Consumo,paraquefosseobtidoovalor
dehashdessenovoobjeto.Existemdiversastécnicasparaasobrescritadesse
método,sendoautilizadanesteexemploumadelas.
Tiposanônimos fornecemumamaneiraconvenienteparaencapsularum
conjuntodepropriedadessomenteleitura,emumúnicoobjeto,semaneces-
75

## Página 92

3.1. Registrodoconsumodeenergiaemumcondomínio CasadoCódigo
sidadededefinirexplicitamenteumtipo.Onomedotipoégeradodinamica-
mentepelocompilador,quetambéminfereotipodecadapropriedade.Para
acria çãodetiposanônimos,faz-seusodooperador new,juntamentecom
uminicializadordeobjeto: { }.
Terminadatodaaexplana çãosobreaclassedemodelo Leituraedos
conceitosrelacionadosaela,háaseguiraimplementa çãodaclassequerepre-
sentaacamadadeapresenta çãoouvisão(oformulário).
Resolução3.3:códigocompletodaclassequerepresentaoformu-
lário
using System ;
using System.Collections.Generic ;
using System.ComponentModel ;
using System.Drawing ;
using System.Windows.Forms ;
namespace ConsumoEnergiaCondominio {
public partial class FormConsumo : Form {
private IList<Leitura> leituras =
new BindingList<Leitura>();
private BindingSource leituraSource =
new BindingSource ();
public FormConsumo () {
InitializeComponent();
leituraSource.DataSource = leituras;
dgvLeituras.DataSource = leituraSource;
}
private void BtnRegistrar_Click ( object sender,
EventArgs e) {
RegistraConsumo(txtCasa.Text,
Convert.ToDouble(txtConsumo.Text));
}
private void RegistraConsumo ( string casa,
double consumo) {
76

## Página 93

CasadoCódigo Capítulo3. Resolvendoproblemasmaiscomplexos:estruturasde...
Leitura leitura = new Leitura(casa, consumo);
if (leituras.Contains(leitura)) {
MessageBox.Show( "A leitura para esta casa
já foi registrada ", " Alerta ",
MessageBoxButtons.OK,
MessageBoxIcon.Warning);
}
else {
this .leituras.Add(leitura);
InicializaFormulario();
}
}
private void InicializaFormulario () {
txtCasa.Clear();
txtConsumo.Clear();
txtCasa.Focus();
}
private void BtnProcessar_Click ( object sender,
EventArgs e) {
ProcessarLeituras(dgvLeituras);
}
private void ProcessarLeituras (DataGridView dgv) {
DataGridViewCell cell =
dgvLeituras.Rows[ 0 ].Cells[ 0 ];
this .leituras.Add( new Leitura( "Total" , 0 ));
for ( int i = 0 ; i < 3 ; i++) {
dgv.Rows[dgvLeituras.Rows.Count - 1 ]
.Cells[i].Style.BackColor =
Color.Blue;
dgv.Rows[dgvLeituras.Rows.Count - 1 ]
.Cells[i].Style.ForeColor =
Color.Yellow;
dgv.Rows[dgvLeituras.Rows.Count - 1 ]
.Cells[i].Style.Font =
new Font (cell.InheritedStyle.Font,
FontStyle.Bold);
77

## Página 94

3.1. Registrodoconsumodeenergiaemumcondomínio CasadoCódigo
}
double totalConsumo = 0 , totalDesconto = 0 ;
foreach ( var leitura in leituras) {
totalConsumo += leitura.Consumo;
totalDesconto += leitura.Desconto;
}
dgv[ 0 , dgv.Rows.Count - 1 ].Value = "Total" ;
dgv[ 1 , dgv.Rows.Count - 1 ].Value =
totalConsumo.ToString( "N" );
dgv[ 2 , dgv.Rows.Count - 1 ].Value =
totalDesconto.ToString( "N" );
lblResultado.Text =
"Total consumo sem desconto: " +
(totalConsumo - totalDesconto)
.ToString( "N" );
}
}
}
Logonoiníciodaclassequerepresentaoformuláriodeintera çãocom
o usuário, existem dois campos (ou variáveis) definidos:leituras e
leituraSource. Oprimeiro, leituras,representaumacole ção. Jáo
segundo, leituraSource,representaum BindingSource,umobjeto
queservecomofontededadosparaumcontrolevisual,vistoemdetalhesna
sequência.
Resolução3.4:defini çãodoscamposquesãoutilizadosnaclasse
// Código omitido
namespace ConsumoEnergiaCondominio {
public partial class FormConsumo : Form {
// Código omitido
private IList<Leitura> leituras =
new BindingList<Leitura>();
private BindingSource leituraSource =
new BindingSource ();
78

## Página 95

CasadoCódigo Capítulo3. Resolvendoproblemasmaiscomplexos:estruturasde...
// Código omitido
}
}
Acole ção leiturastemcomotipoainterface IList,que,pormeio
de generics,garantequetodososdadosaseremarmazenadosnelase-
jamdotipo Leitura. PorIListserumainterface,nãoépossívelobter
umobjetodiretodessetipo.Entretanto,aclasse BindingListimplementa
essainterfaceeelaéinstanciada. Assim,tem-seumobjetoinstanciadopor
BindingListdotipo IList.Comisso,épossívelqueesseobjetopossaser
atribuídoaqualquervariávelde IList.
Anecessidadedecriaregerenciargruposdeobjetosrelacionadoséuma
característicacomumnasaplica ções. Paraimplementaressanecessidade,é
possívelfazerusodematrizes(arrays)ou coleções (collections).Ouso
dematrizeséútilquandoexisterigideznotipodedado,eonúmerodeele-
mentoséconhecido. Jáousodecole çõespropiciamaiorflexibilidade,per-
mitindoumaumentoouredu çãonaquantidadedeobjetosarmazenados,
deacordocomanecessidadedaaplica ção. Algumascole çõespermitema
atribuiçãodechavesparacadaobjetoarmazenado,possibilitandoumabusca
maiseficiente. Outrosgarantemqueobjetosiguaisnãosejamarmazenados
demaneirarepetida.
A IListéumainterfacegenéricaquerepresentaumacole çãodedados,
naqualositenspodemseracessadospormeiodeumíndice.Existemdiversas
classesqueaimplementameumadelaséa BindingList.
A BindingList*éumaclassequeimplementaainterface IList.Ela
representacole çõesqueprecisamoferecersuporteàvincula çãodedadoscom
controlesvisuais,comoo DataGridView.Oscontrolesvisuaisquerecebem
objetosdessaclassetêmsuavisãoatualizadaaomesmotempoemqueisso
ocorrenacole ção.
Ocomponente BindingSourceatendeamuitospropósitos.Primeiro,
elesimplificaaliga çãodecontrolesemumformulárioaumconjuntodeda-
dos,fornecendogerenciamentoconcorrente,notifica çõesdealtera çãoeou-
trosservi çosentrecontroles Windows Formsefontesdedados.Issoéfeito
pelaatribui çãodo BindingSourceàpropriedade DataSourcedocon-
79

## Página 96

3.1. Registrodoconsumodeenergiaemumcondomínio CasadoCódigo
trolequefaráusodosdados.Diversosrecursossãodisponibilizadosporesse
componentepormeiodesuaspropriedades,métodoseeventos.
Apósadeclara çãodasvariáveisdeobjeto,verifica-senocódigoocons-
trutorimplementadoparaaclasse.Esseconstrutor,criadoautomaticamente
peloVisualStudio,agora,alémdeinicializartodaainterfacecomousuá-
riopormeiodachamadaaométodo InitializeComponent(),atribui
ao BindingSourceacole çãocriadaparareceberosobjetosrelacionadosàs
leiturasrealizadasnocondomínio.
Alémdisso, ocódigoparaoconstrutorterminacomaatribui çãodo
BindingSourceàpropriedade DataSourcedo DataGridView. Após
essaatribui ção,combasenaspropriedadesdaclasseexplicitadanadeclara ção
einstancia çãodacole ção,o DataGridViewconsegueidentificarascolunas
queovãocompor,dandoaelasonomedaspropriedadespúblicasdaclasse
–nestecaso,aclasseLeitura.Aseguir,apresentooconstrutordaclasse.
Resolução3.5:códigodoconstrutordaclassedoformulário
public FormConsumo () {
InitializeComponent();
leituraSource.DataSource = leituras;
dgvLeituras.DataSource = leituraSource;
}
Umainterfacecontémapenasassinaturasdemétodos. Épraticamente
comoumcontratoentreaclasseeomundoexterno.Umaclasse,aoherdar
umainterface,estácomprometidaafornecerocomportamentopublicadopor
esta,ouseja,escrevertodososmétodosassinados.Devidoaessaobriga ção
pelaimplementa ção,utiliza-seotermo“aclasseXimplementaainterfaceY”.
Polimorfismo,quesignifica“váriasformas”,éumtermodesignadoaob-
jetosdeclassesdistintas,que,aofazeremousodeummesmométodo,po-
demreagirdeumamaneiradiferente.Éumdosresponsáveispelaextensão
emumaaplica çãoOO,poiscomportamentosdefinidos,masnãoimplemen-
tadosnasclassesmaisgenéricas,serãoimplementadosnasnovassubclasses.
Comaaplica çãoemexecu ção,ousuáriodeveráinformaronúmeroda
casaondealeituraocorreueovalorconsumidoporesta.Apósainforma ção
80

## Página 97

CasadoCódigo Capítulo3. Resolvendoproblemasmaiscomplexos:estruturasde...
dessesdoisdados,ousuárioprecisaregistraraleitura,oqueéfeitoquandoo
botão “Registrar”épressionado.Ométodo%BtnRegistrar_Click()
é o responsável pelo processamento do eventoClick desse botão. A
implementação desse método delega a responsabilidade para o método
RegistraConsumo(),querecebecomoargumentosonúmerodacasa(
string)eovalordoconsumo( double).
Aimplementa çãodométodo BtnRegistrar_Click()podeservisu-
alizadanasequência.
Resolução3.6:métodoClickdobotãoRegistrar
private void BtnRegistrar_Click ( object sender,
EventArgs e) {
RegistraConsumo(txtCasa.Text,
Convert.ToDouble(txtConsumo.Text));
}
OmétodoRegistraConsumo()instanciaaclasse Leitura,enviando
aoseuconstrutoronúmerodacasaeoconsumorecebidospelométodo.Com
oobjetocriado,éprecisogarantirquenãoestejasendorealizadaumanova
leituraparaamesmacasa,poisosistemadevegarantirqueapenasumaleitura
porcasasejaregistrada.
Uma vez que a classeLeitura tem implementados os métodos
Equals()e GetHashCode(),épossívelfazerusodeservi ços(métodos)
disponibilizadospelaclasse BindingList,comoométodo Contains().
Esteverificaaexistênciadoobjetoenviadocomoargumentonacole çãoem
queérealizadaachamadaaele.Casoaleiturajátenhasidoregistrada,ousuá-
rioéinformado;casocontrário,oobjetode Leituraéadicionadoàcole ção,
pormeiodométodo Add().Paragarantirqueousuárioregistreumanova
leitura,desdeoinício,ométodo InicializaFormulario()éinvocado.
Na sequência, trago a implementa ção do método
RegistraConsumo().
Resolução3.7:implementa çãodométodoRegistraConsumo()
81

## Página 98

3.1. Registrodoconsumodeenergiaemumcondomínio CasadoCódigo
private void RegistraConsumo ( string casa, double consumo){
Leitura leitura = new Leitura(casa, consumo);
if (leituras.Contains(leitura)) {
MessageBox.Show( "A leitura para esta casa
já foi registrada ", " Alerta ",
MessageBoxButtons.OK,
MessageBoxIcon.Warning);
}
else {
this .leituras.Add(leitura);
InicializaFormulario();
}
}
OmétodoInicializaFormulario()limpaos TextBoxs,parauma
novaentrada,ecolocaofocodaaplica ção(cursor)nocontrolequerecebeo
númerodacasa.Aseguir,apresentoestemétodo.
Resolução3.8:códigoparaométodoInicializaFormulario()
private void InicializaFormulario () {
txtCasa.Clear();
txtConsumo.Clear();
txtCasa.Focus();
}
Apósoregistrodeleiturasdetodasascasas,éprecisorealizaroproces-
samentodelas,buscandoidentificarosolicitadopeloenunciado.Ométodo
BtnProcessar_Click()éoresponsávelporisso.Seucomportamentode-
legaao ProcessarLeituras()aresponsabilidadepeloprocessamento,
enviandoo DataGridViewcomoargumento. Nasequência,apresentoo
códigoparaestemétodo.
Resolução3.9:códigoparaométodoreferenteaoeventoClickdo
botãoBtnProcessar
private void BtnProcessar_Click ( object sender,
EventArgs e) {
82

## Página 99

CasadoCódigo Capítulo3. Resolvendoproblemasmaiscomplexos:estruturasde...
ProcessarLeituras(dgvLeituras);
}
Garantaqueoprocessamentodasleiturasocorraapenascasoexistamlei-
turasrealizadas.
Ométodo ProcessarLeituras()trazemsuaimplementa çãoduas
estruturasderepeti ção;focodestecapítulo. Nométodo,asduasinstru ções
iniciaisreferem-seà:
1) Obtençãodeumacélulado grid,queservirádebaseparaconfigura ção
defonte,nalinhadetotais;
2) Inserçãodeumalinhaaofinaldo grid,paraexibi çãodostotais.
Emseguida,oprimeiroblocoderepeti çãoocorre.
Aseguir,reapresentoométodo ProcessarLeituras(),tendocomen-
tadootrechodestebloco.
Resolução3.10:métodoProcessarLeituras()
private void ProcessarLeituras (DataGridView dgv) {
DataGridViewCell cell = dgvLeituras.Rows[ 0 ].Cells[ 0 ];
this .leituras.Add( new Leitura( "Total" , 0 ));
// Início da estrutura de repetição for()
for ( int i = 0 ; i < 3 ; i++) {
dgv.Rows[dgvLeituras.Rows.Count - 1 ]
.Cells[i].Style.BackColor = Color.Blue;
dgv.Rows[dgvLeituras.Rows.Count - 1 ]
.Cells[i].Style.ForeColor = Color.Yellow;
dgv.Rows[dgvLeituras.Rows.Count - 1 ]
.Cells[i].Style.Font =
new Font (cell.InheritedStyle.Font,
FontStyle.Bold);
}
// Término da estrutura de repetição for()
83

## Página 100

3.1. Registrodoconsumodeenergiaemumcondomínio CasadoCódigo
double totalConsumo = 0 , totalDesconto = 0 ;
// Início da estrutura de repetição foreach()
foreach ( var leitura in leituras) {
totalConsumo += leitura.Consumo;
totalDesconto += leitura.Desconto;
}
// Término da estrutura de repetição foreach()
dgv[ 0 , dgv.Rows.Count - 1 ].Value = "Total" ;
dgv[ 1 , dgv.Rows.Count - 1 ].Value =
totalConsumo.ToString( "N" );
dgv[ 2 , dgv.Rows.Count - 1 ].Value =
totalDesconto.ToString( "N" );
lblResultado.Text =
"Total consumo sem desconto: " +
(totalConsumo - totalDesconto).
ToString( "N" );
}
Aestruturade repetiçãocontada érecomendadaquandosesabeprevi-
amenteporquantasvezesumdeterminadoconjuntodeinstru ções(ouum
terminadoprocesso)deveserrepetido. Essaquantidadedevezespodeser
umvalorconstanteouvariável,deacordocomanecessidadedousuárioou
doproblema.Ainstru ção for()éaimplementa çãodaestruturaderepeti-
çãocontadaparaoC #eemdiversasoutraslinguagens.
Aqui,épossívelverificarqueexistemtrêsinstru çõesqueestãodentrodo
bloco for().Destamaneira,assimcomonasestruturascondicionais,háa
necessidadededelimitadoresdebloco(chaves).Casoapenasumainstru ção
fosseexecutadademaneirarepetitiva,aschavesseriamopcionais.
Ainstru çãopossui,emseusargumentos,trêsexpressõescomponentes
(separadasporpontoevírgula).Aprimeiraéconhecidacomo inicializadora,
poisdeclaraavariável(ouvariáveis)decontrole.Asegunda avaliaacondi-
çãopararepeti ção,normalmenteumvalorinferior(ousuperior)aoutro,
quelimitaaquantidadedeexecu çõesdobloco.Jáaterceiratrazo processa-
mentoquedeveserexecutadoapóscadaitera çãodobloco.Hásitua çõesem
84

## Página 101

CasadoCódigo Capítulo3. Resolvendoproblemasmaiscomplexos:estruturasde...
queprogramadoresutilizamessainstru çãoapenascomasegundaexpressão,
como,porexemplo, for(;x!=null;).Entretanto,issonãoécomum,pois
existemestruturasprópriasparaestasitua ção.
Asinstru çõesdentrodobloco for()sãoresponsáveisporalterarafor-
mataçãovisualdastrêscolunasdo DataGridView,dalinhaqueapresentará
ostotais–nocasodesteproblema,aúltimalinha.Nestesentido,cadaitera ção
realizaráaconfiguraçãoparacadacéluladalinhadetotais.Porisso,acélula
(Cells)éindicadapor i,quevaide0(zero)até2(menorque3).
Apósotérminodessaprimeiraestruturaderepeti ção,variáveis“acumu-
ladoras”sãoinicializadas(totalConsumoe totalDesconto).Elasserão
atualizadascombaseemumavarredurarealizadanacole çãoquearmazena
asleituras,comainstru ção foreach().
Aestrutura foreachéresponsávelpelaleituradetodososelementosde
umacole ção,associandocadaumdelesacadaitera ção,aumavariável.
Finalizandoométodo,apóso foreach,osvaloresobtidosnasvariáveis
“acumuladoras”sãoatribuídosàúltimalinhadogrid,devidamenteforma-
tados,assimcomoovalorparao Labelaoladodo Button,queexibeo
totalconsumidosemosdescontos.
3.2 Leitura de arquivo texto para cálculo de
reajuste em folha de pagamento
Paratrabalharmoscomnovosrecursos,desenvolvaumaplicativoquedeverá
lerumarquivotexto,comvaloresdelimitadosporpontoevírgula( ;).Nele,
osdadosconstantesreferem-seaocódigoeaosaláriodefuncionáriosdeuma
empresa.Apósaleituradessearquivo,osdadoslidosdevemserprocessados,
objetivandoarealiza çãodocálculoparareajustedafolhadepagamentopara
essaempresa.Paraoreajustedossalários,queseráporfaixa,considereque:
• Paracadafuncionário,oreajusteseráde15%,casoseusaláriosejame-
norqueR $1.000;
• SeosalárioformaiorouigualaR$1.000,porémmenorouigualaR $
1.500,seureajusteseráde10%;
85

## Página 102

3.2. Leituradearquivotextoparacálculodereajusteemfolhadepagamento CasadoCódigo
• CasosejamaiorqueR$1.500,oreajustedeveráserde5%.
Apósaleituradoarquivoeidentifica çãodosnovossalários,aaplica ção
deveráexibir:
a) Ovalortotaldafolhadepagamentoantesdoreajuste;
b) Ovalortotaldafolhadepagamentoapósoreajuste;
c) Opercentualdeacréscimoàfolhadepagamento,emrela çãoàfolhaatual.
Naimplementa çãopropostacomoresolu çãoparaesteproblema,uma
novatécnicaserátrabalhada: ousodearquivostextoscomofontededa-
dos. Dois novos controles também serão apresentados: oPanel e o
TableLayoutPanel.Essescontrolessãocontainersepossibilitamumaboa
organizaçãodecontrolesvisuaisnodesenhodajaneladaaplica ção.
Aúnicaintera çãodousuáriocomaaplica çãoseráasele çãodoarquivode
texto,quepossuiasinforma çõesnecessáriasparaoprocessamentodesejado.
Apósasele çãocorreta,oarquivodeveráserlidolinhaalinha,cadaqualcom
osdadosseparadosporumsinaldepontoevírgula( ;)erepresentaumobjeto
deumaclassedenegócio.Comtodaaleiturarealizada,quandoossaláriosde
cadafuncionárioforemaplicadosàregraparareajuste,ostotaissolicitados
serãoexibidos.
Afigura3.2representaainterfacedesejada,queseráimplementadapara
oproblemapropostonestase ção.
86

## Página 103

CasadoCódigo Capítulo3. Resolvendoproblemasmaiscomplexos:estruturasde...
Fig.3.2:Interfaceparaoproblemadereajustedefolhadepagamento
Osdadosapresentadosnafigura 3.2foramlidosdeumarquivotexto(
*.txt)comosvalores(códigoesalárioatual)separadosporpontoevírgula.
Afigura3.3trazoconteúdodessearquivo.
87

## Página 104

3.2. Leituradearquivotextoparacálculodereajusteemfolhadepagamento CasadoCódigo
Fig.3.3:Conteúdodearquivotextoaserutilizadonaresolu ção
Crieumprojeto Windows Forms Applicationnasolu çãocriada
anteriormente, com um formulário específico para a implementação da
janela da figura 3.2. Os controles que exibem os totais são:Panel,
TableLayoutPanele Labels.Acimadessestotaisexisteum TextBoxde-
sabilitado( Enabled=False)eum Button.Aexibi çãodasleituras,abaixo
dostotais,érealizadapormeiodeum DataGridView.
Ocontrole Paneléusadoparafornecerumagrupamentoparaoutros
controlese,normalmente,parasubdividirumformulárioporcaracterísticas
dedadosoufuncionalidades.
Comoexemplo,emumformuláriopoderiaexistirdadosrelacionadosàs
contasapagareàscontaspagas,logo,poderiamexistirdois Panels,umpara
cadatipodeconta. Estatécnicadeagrupamentopodepropiciaraousuá-
rioumavisãológicadosdados. Emtempodedesenho,quandosemove
um Panel,todososcontrolesinseridosnelesãomovidosemconjunto.Um
Panelpossuiumapropriedadechamada Controls–todocontainertem
88

## Página 105

CasadoCódigo Capítulo3. Resolvendoproblemasmaiscomplexos:estruturasde...
essapropriedade–,quepermiteacessartodososcontrolescontidosneleem
tempodeexecu ção.
Jáocontrole TableLayoutPanelorganizaseuconteúdoemumata-
bela.Pelofatodeolayoutserrealizadotantoemtempodedesenhoquanto
deexecu ção,elepodemudardinamicamente,deacordocomamudan çado
ambientedaaplica ção.Essecontroleofereceaoscontrolesqueelecontéma
habilidadedeterseutamanhoalteradoproporcionalmente.
Qualquercontrolepodepertencerao TableLayoutPanel,incluindo
outros TableLayoutPanels. Issopermiteumacria çãodelayoutssofisti-
cados.Eleadicionaalgumaspropriedadesaoscontrolescontidosnele,sendo
elas: Cell, Column, Row, ColumnSpane RowSpan.
Noexemploanterior,acole çãodosdadosinformadospelousuárioestava
declaradadiretamentenaclassedoformulárioqueossolicitava. Umaboa
práticaéterumaclasseespecíficaparaisso,evitandoumacoesãoforteentre
ascamadasdeapresenta ção,denegócioedepersistência. Dessamaneira,
esseexemplotrazousodeumaclassequeaplicaoconceitoderepositório.
Elaseráresponsávelporteracole çãodosdadosinformadospelousuário,
assimcomoosmétodosparamanuten çãoeacessoaeles.Nasequência,háa
implementaçãodessaclasse,chamada RepositorioFuncionario.
Resolução3.11:classeresponsávelpormanterefornecerdadosdos
funcionários
namespace ReajusteDeFolhaDePagamento {
public class RepositorioFuncionario {
private IList<Funcionario> funcionarios =
new BindingList<Funcionario>();
public void Inserir (Funcionario funcionario){
funcionarios.Add(funcionario);
}
public IList<Funcionario> ObterTodos() {
return this .funcionarios;
}
89

## Página 106

3.2. Leituradearquivotextoparacálculodereajusteemfolhadepagamento CasadoCódigo
}
}
Aclasse RepositorioFuncionariotemsuaimplementa çãodentro
do namespace ReajusteDeFolhaDePagamento. Suaimplementação
tem,emseuinício,adefini çãodeumcampoprivado,responsávelpelaco-
leçãodedados,sendoestesrepresentadospelaclasse Funcionario. Ini-
cialmente,aclasseoferecedoismétodos(servi ços): umparaainclusãode
umnovofuncionárioeoutroqueretornatodososempregadosregistrados
nacole çãodesterepositório.Aseguir,apresentoaclasse Funcionario.
Resolução3.12:classedenegóciopararegistrodedadosdecada
Funcionario
namespace ReajusteDeFolhaDePagamento {
public class Funcionario {
public int Codigo { get ; set ; }
public double Salario { get ; set ; }
public double Percentual {
get {
if ( this .Salario < 1000 ) return 15 ;
else if ( this .Salario < 1500 ) return 10 ;
else
return 5 ;
}
}
public double NovoSalario {
get {
return ( this .Salario * this .Percentual /
100 )+ this .Salario; }
}
}
}
Aclasse Funcionariotraz4atributos.Doisdestespermitemescritae
leitura,poissãoosquereceberãoosdadoslidosdoarquivodetexto( Codigo
e Salario),eosoutrosdois( Percentuale NovoSalario)sãoapenas
deleitura,combaseemprocessamentonovalordo Salario. Notequeo
90

## Página 107

CasadoCódigo Capítulo3. Resolvendoproblemasmaiscomplexos:estruturasde...
processamentorealizadono get()dapropriedade Percentualrefere-
seàidentifica çãodopercentualdereajusteaseraplicado,deacordocomo
expostonoenunciado. Jáapropriedade NovoSalariorealizaapenasum
cálculoparaaplicarnosalárioatualopercentualidentificado.
Umavezquealeituradosdadosserárealizadacombaseemumarquivo
detexto,éprecisoforneceraousuáriodaaplica çãomecanismosparasele ção
dessearquivo.OC #ofereceumcomponentechamado OpenFileDialog,
quepossibilitaselecionarumarquivooumais.Essasele çãoocorrepormeio
dajanelabásicaoferecidapeloWindowsparaaberturadearquivos. Éuma
janelacomumemqualqueraplica çãoepodeserverificadanafiguraaseguir:
Fig.3.4:Janelaparasele çãodoarquivodeleitura
Parainserirocomponente OpenFileDialogemseuformulário,para
quepossaserusado,éprecisoarrastá-loparaaáreadedesenho.Localize-o
nacategoria Dialogs,na Toolbox,earraste-o. Eleseráposicionadoem
umaáreaabaixodadedesenho,quenãoévisual. Essaáreafoiapresentada
nocapítulo2(se ção2.3).Altereovalordaspropriedadesparaessecontrole
conformemostradonasequência.
•Propriedade:Name
91

## Página 108

3.2. Leituradearquivotextoparacálculodereajusteemfolhadepagamento CasadoCódigo
•Valorparaatribuir: ofdListaFuncionarios:
•Propriedade:DefaultExt
•Valorparaatribuir: *.txt:
Apropriedade DefaultExtdefine,dentreostiposdearquivosapon-
tadosnapropriedade Filter,qualéopadrãoqueseráutilizadoquandoa
janeladesele çãodearquivosforaberta.
•Propriedade:Filter
•Valorparaatribuir: Arquivostextos|*.txt:
Apropriedade Filterdefineumconjuntodeparesqueinformamos
tiposdearquivospossíveisdeseremselecionadosnajanela.Cadafiltroées-
pecificadoporumnomequeodescreveesuaextensão,separadosporum
pipe(|).
•Propriedade:Title
•Valorparaatribuir: Seleçãodoarquivocomdadosdefuncionários
Apropriedade Titledefineotítuloaseratribuídoparaajanelaaser
abertapormeiodocomponente.
Terminadatodaaexplana çãosobreasclassesderepositórioedenegócio,
assimcomosobreonovocomponenteutilizado,tragonasequênciaaimple-
mentaçãodaclassequerepresentaacamadadeapresenta ção(oformulário).
Resolução3.13: classequerepresentaoformuláriodeintera ção
comousuário
using System ;
using System.Collections.Generic ;
using System.Windows.Forms ;
namespace ReajusteDeFolhaDePagamento {
92

## Página 109

CasadoCódigo Capítulo3. Resolvendoproblemasmaiscomplexos:estruturasde...
public partial class FormLeituraArquivo : Form {
private RepositorioFuncionario repositorio =
new RepositorioFuncionario ();
private BindingSource leituraSource =
new BindingSource ();
public FormLeituraArquivo () {
InitializeComponent();
leituraSource.DataSource =
repositorio.ObterTodos();
dgvLeitura.DataSource = leituraSource;
}
private void button1_Click ( object sender,
EventArgs e) {
if (ofdListaFuncionarios.ShowDialog() ==
DialogResult.OK) {
txtArquivo.Text = ofdListaFuncionarios.
FileName;
ProcessarArquivo(txtArquivo.Text);
if (repositorio.ObterTodos().Count > 0 ) {
TotalizarValores(repositorio.
ObterTodos());
}
}
}
private void TotalizarValores (IList<Funcionario>
dadosLidos) {
double totalSemReajuste= 0 ,totalComReajuste= 0 ;
foreach ( var funcionario in dadosLidos) {
totalSemReajuste += funcionario.Salario;
totalComReajuste += funcionario.
NovoSalario;
}
double percentualReajuste = (totalComReajuste
- totalSemReajuste)* 100 /totalSemReajuste;
lblTotalSemReajuste.Text = string .Format(
"{0:c}" , totalSemReajuste);
93

## Página 110

3.2. Leituradearquivotextoparacálculodereajusteemfolhadepagamento CasadoCódigo
lblTotalComReajuste.Text = string .Format(
"{0:c}" , totalComReajuste);
lblPercentualDoReajuste.Text = string .Format(
"{0:n}%" , percentualReajuste);
}
private void ProcessarArquivo ( string nomeArquivo){
repositorio.ObterTodos().Clear();
string linhaLida;
var arquivo =
new System.IO.StreamReader(@nomeArquivo);
while ((linhaLida = arquivo.ReadLine()) !=
null ) {
var dadosLidos = linhaLida.Split( ';' );
var funcionario = new Funcionario
{
Codigo = Convert.ToInt32(
dadosLidos[ 0 ]),
Salario = Convert.ToDouble(
dadosLidos[ 1 ])
};
repositorio.Inserir(funcionario);
}
arquivo.Close();
}
}
}
Logonoiníciodaclassequerepresentaoformuláriodeintera çãocom
ousuário, existemdoiscampos(ouvariáveis)definidos: repositorio
e leituraSource. O primeiro representa a classe responsável pela
manutenção dos dados para processamento e o segundo representa um
BindingSource.
Ainda na classe que representa o formulário, após as propriedades
verifica-seque,noconstrutor,o BindingSourcerecebeacole çãoretornada
pelométodo ObterTodos()daclassederepositório.Noteque,nestemo-
mento,nenhumdadofoiaindaadicionado.Entretanto,comessaimplemen-
tação,tododadoinseridoseráautomaticamenteexibidono DataGridView,
94

## Página 111

CasadoCódigo Capítulo3. Resolvendoproblemasmaiscomplexos:estruturasde...
quetememsuapropriedade DataSourceesse BindingSource.Estali-
gaçãotambémpodeserverificadanoconstrutor.
Comaaplica çãoemexecu ção,ousuáriodeveráselecionaroarquivoque
possuiosdadosnecessáriosparaprocessamento.Paraisso,eleprecisaráclicar
nobotãoquetemtrêspontos( ...)e,então,buscarpeloarquivoeselecioná-
lo.Ométodo BtnSelecionarArquivo_Click()éoresponsávelpelain-
terfacequepermitiráissoetambémpeloiníciodeprocessamentosobreos
dadoscontidosnessearquivo.Aseguir,reapresentoaimplementa çãodesse
método.
Resolução3.14:métodoClickdobotãodesele çãodoarquivoaser
lido
private void BtnSelecionarArquivo_Click ( object sender,
EventArgs e) {
if (ofdListaFuncionarios.ShowDialog() ==
DialogResult.OK) {
txtArquivo.Text = ofdListaFuncionarios.FileName;
ProcessarArquivo(txtArquivo.Text);
if (repositorio.ObterTodos().Count > 0 ) {
TotalizarValores(repositorio.ObterTodos());
}
}
}
Aprimeiralinhaimplementadanessemétodoéresponsávelpelaexe-
cução do componente OpenFileDialog – pela chamada ao método
ShowDialog()–etambémpelaverificaçãodasele çãodoarquivodesejado.
Essaverifica çãodá-sepelacompara çãodovalorretornadopelométodocom
aenumera ção DialogResult.OK.Emcasoverdadeiro,issogarantequeo
usuárioselecionouumarquivoeclicounobotão OKdajanelaresponsável
pelalocaliza çãodeles.Ainda,emcasodesucesso,oarquivoselecionado–ar-
mazenadonapropriedade FileNamedocontrole–éatribuídoaoTextBox,
apenasporcaráterinformativoaousuário.
Em seguida, o arquivo é enviado para processamento pelo método
ProcessarArquivo(). Terminadooprocessamento,verifica-seseosda-
dosforaminseridosnorepositórioe,emcasopositivo,elessãoprocessados
95

## Página 112

3.2. Leituradearquivotextoparacálculodereajusteemfolhadepagamento CasadoCódigo
embuscadostotalizadoresdesejados.
O método ProcessarArquivo() é exibido na sequência e o
TotalizarValores()naResolução3.16.
Resolução3.15: métodoresponsávelpeloprocessamentodoar-
quivolido
private void ProcessarArquivo ( string nomeArquivo) {
repositorio.ObterTodos().Clear();
string linhaLida;
var arquivo = new System.IO.StreamReader(
@nomeArquivo);
while ((linhaLida = arquivo.ReadLine()) != null ) {
var dadosLidos = linhaLida.Split( ';' );
var funcionario = new Funcionario {
Codigo = Convert.ToInt32(dadosLidos[ 0 ]),
Salario = Convert.ToDouble(
dadosLidos[ 1 ])
};
repositorio.Inserir(funcionario);
}
arquivo.Close();
}
Aprimeiralinhadométodo ProcessarArquivo()realizaumalim-
peza na coleção do repositório. Essa limpeza é realizada pelo método
Clear(),definidonainterface IList. Nasequência,inicia-seoprocedi-
mentoparaleituradoarquivoselecionado.
Oprimeiropassoparaissoéabriroarquivo,oqueéfeitopelaclasse
StreamReader. Apósobterareferênciaparaoarquivo,umaestruturade
repetição while()éiniciada,realizandoaleituradoarquivo,umalinha
porvez, atéqueseufinalseja encontrado. Aleituradá-sepelo método
ReadLine().
Comoemcadalinhadoarquivoexistemdoisdados,queestãoseparados
porumpontoevírgula( ;),éprecisoqueelessejamarmazenadosdema-
neiraisolada,paraentãoseremprocessados.Essasepara çãoérealizadapelo
métodoSplit(),definidonaclasse String. Oretornodessemétodoé
96

## Página 113

CasadoCódigo Capítulo3. Resolvendoproblemasmaiscomplexos:estruturasde...
umamatrizcomcolunasquerepresentamcadadadoencontradoeseparado
nalinhalida.Comosdadoslidos,objetosdaclasse Funcionariosãoins-
tanciadose,pormeiodorecursodeinicializa çãodeobjetos,osvaloressão
atribuídosàspropriedadesdonovoobjeto,que,então,éinseridonoreposi-
tório.
Aclasse System.IO.StreamReaderdestina-seàleituradecaracteres
emumacodifica çãoespecífica,comoUTF-8ouANSI,porexemplo.Seuuso
édestinadoparaaleituradelinhasemumarquivodetexto.
Aestrutura whileéresponsávelpelaexecuçãodeumconjuntodeinstru-
çõesqueestejamdentrodosdelimitadoresdeblocooferecidosporela.Esta
função( while())recebeumargumentoqueéumaexpressãológica,que
garantiráaexecu çãodesseconjuntodeinstru ções,casoavaliadacomover-
dadeira. Seapenasumainstru çãocompuseraestrutura while,ousode
delimitadoresseráopcional.
Resolução3.16:métodoresponsávelpelatotaliza çãodosvalores
lidos
private void TotalizarValores (
IList<Funcionario> dadosLidos) {
double totalSemReajuste = 0 , totalComReajuste = 0 ;
foreach ( var funcionario in dadosLidos) {
totalSemReajuste += funcionario.Salario;
totalComReajuste += funcionario.NovoSalario;
}
double percentualReajuste = (totalComReajuste 
totalSemReajuste)* 100 /totalSemReajuste;
lblTotalSemReajuste.Text = string .Format( "{0:c}" ,
totalSemReajuste);
lblTotalComReajuste.Text = string .Format( "{0:c}" ,
totalComReajuste);
lblPercentualDoReajuste.Text =
string .Format( "{0:n}%" , percentualReajuste);
}
Estemétodoprimeiramenteinicializaasvariáveisacumuladoras,quete-
rãoostotaisdesejados.Apósisso,umavarreduranosvaloresrecebidospelo
97

## Página 114

3.3. Informaçãodedadosparagera çãodearquivotexto CasadoCódigo
métodoérealizada,paratotalizarosvaloresaseremexibidos.Apósaobten-
çãodostotais,opercentualdereajusteécalculadoe,então,osvaloressão
atribuídosaosrespectivos Labelsdajanela.
3.3 Informação de dados para geração de ar -
quivo texto
Comoterceiro(eúltimo)problemapropostoparaestecapítulo,desenvolva
umaplicativoquepermitaainser çãodedadosrelacionadosaosfuncionários
deumaempresa.Osdadossolicitadossãoapenasnomeesalário.Paraesse
problema,propõe-senovamenteousodearquivostextos,porémagoracomo
destinodosdadosinformadosnaaplica ção. Nenhumcontrolevisualnovo
seráapresentado.
Aquantidadedefuncionáriosquedeverãoterseusdadosinformados
deveserpassadapreviamentepelousuário,eosdadosdetodososempre-
gadosdeverãoserarmazenadosemumarquivotexto,delimitadosporponto
evírgula( ;).Paraestaexporta çãodedados,eleselecionaráapastaondeo
arquivoserácriado,assimcomoinformaráumnomeparaele.
Afigura3.5representaainterfacedesejada,queseráimplementadapara
oproblemapropostonestase ção.
98

## Página 115

CasadoCódigo Capítulo3. Resolvendoproblemasmaiscomplexos:estruturasde...
Fig.3.5:Interfaceparaoproblemadecria çãodearquivotexto
Crieumprojeto Windows Forms Applicationnasolu çãocriadaan-
teriormente,comumformulárioespecíficoparaaimplementa çãodajanela,
deacordocomapropostadeinterfaceapresentadanafigura 3.5. Todosos
controlesusadosjáforamapresentadosemexemplosanteriores. Configure
osbotões Criar arquivoe Reiniciarcomapropriedade Enabled,
comovalor False.
Noexemploanterior,umarquivodetextofoiutilizadoparafornecerda-
dosparaarealiza çãodeprocessamentosrelacionadosaumafolhadepaga-
mento.Agora,umarquivodetextoserágeradoapartirdedadosinformados
naaplica ção. Sendoassim,éprecisoforneceraoseuusuáriomecanismos
paragera çãodessearquivo.Paraisso,seráusadoumcomponentechamado
SaveFileDialog,quepossibilitaasele çãodeumapastadedestinoparao
arquivoasergerado,assimcomonomeaserdadoaele.Esseprocessoocorre
pormeiodajanelabásicaoferecidapeloWindowsparagrava çãodearquivos,
retratadanafiguraaseguir.
99

## Página 116

3.3. Informaçãodedadosparagera çãodearquivotexto CasadoCódigo
Fig.3.6:Janelaparasele çãodepastadedestinoparaarquivoasergerado
Oprocedimentoparaainser çãodocomponente SaveFileDialogé
semelhanteaousadoparainseriro OpenFileDialog.Localize-onacate-
goria Dialogs,na Toolbox,earraste-o.Eleseráposicionadoemumaárea
abaixodaáreadedesenho,quenãoévisual.Altereovalordaspropriedades
paraessecontrole,conformeapresentadonasequência.
PropriedadesparaoSaveFileDialog
•Propriedade:Name
•Valorparaatribuir: sfdGravarArquivo:
•Propriedade:DefaultExt
•Valorparaatribuir: *.txt
•Propriedade:Filter
•Valorparaatribuir: Arquivostextos|*.txt
100

## Página 117

CasadoCódigo Capítulo3. Resolvendoproblemasmaiscomplexos:estruturasde...
•Propriedade:Title
•Valorparaatribuir: Dadosparagera çãodearquivo
Terminadaaexplana çãosobreoproblemaesuainterfacederesolu ção,
tragonasequênciaaimplementaçãodaclassequerepresentaosmétodoscap-
turadospelacamadadeapresenta ção(oformulário).
Resolução3.17: classequerepresentaoformuláriodeintera ção
comousuário
using System ;
using System.IO ;
using System.Windows.Forms ;
namespace PreparacaoDeDadosParaGravacao {
public partial class FormGeracaoArquivoTexto : Form {
public FormGeracaoArquivoTexto () {
InitializeComponent();
dgvFuncionarios.ColumnCount = 2 ;
dgvFuncionarios.Columns[ 0 ].HeaderText =
"Nome" ;
dgvFuncionarios.Columns[ 0 ].Width = 230 ;
dgvFuncionarios.Columns[ 1 ].HeaderText =
"Salário" ;
dgvFuncionarios.Columns[ 1 ].Width = 67 ;
}
private void btnCriarLinhas_Click ( object sender,
EventArgs e) {
int numeroFuncionarios = Convert.ToInt16(
txtNumeroFuncionarios.Text);
if (numeroFuncionarios < 1 )
numeroFuncionarios = 1 ;
int i = 0 ;
do {
var linhaTabela = new DataGridViewRow();
linhaTabela.Cells.Add( new
101

## Página 118

3.3. Informaçãodedadosparagera çãodearquivotexto CasadoCódigo
DataGridViewTextBoxCell {
Value = string .Empty });
linhaTabela.Cells.Add( new
DataGridViewTextBoxCell { Value = 0 });
dgvFuncionarios.Rows.Add(linhaTabela);
} while (++i < numeroFuncionarios);
txtNumeroFuncionarios.Enabled = false ;
btnCriarArquivo.Enabled = true ;
btnReiniciar.Enabled = true ;
btnCriarLinhas.Enabled = false ;
}
private void btnReiniciar_Click ( object sender,
EventArgs e) {
dgvFuncionarios.Rows.Clear();
txtNumeroFuncionarios.Text = string .Empty;
txtNumeroFuncionarios.Enabled = true ;
btnCriarArquivo.Enabled = false ;
btnReiniciar.Enabled = false ;
btnCriarLinhas.Enabled = true ;
}
private void btnCriarArquivo_Click ( object sender,
EventArgs e) {
if (!ValidaDados()) {
MessageBox.Show( "Os dados possuem
problemas. Verifique se não deixou
nenhum nome em branco ou se existe um
valor correto para os salários de cada
um ");
}
else if (sfdGravarArquivo.ShowDialog() ==
DialogResult.OK) {
GerarArquivo();
MessageBox.Show( "Arquivo gerado com
sucesso ");
}
}
102

## Página 119

CasadoCódigo Capítulo3. Resolvendoproblemasmaiscomplexos:estruturasde...
private void GerarArquivo () {
StreamWriter wr = new StreamWriter(
sfdGravarArquivo.FileName, true );
for ( int j = 0 ;
j < dgvFuncionarios.Rows.Count;
j++) {
wr.WriteLine(dgvFuncionarios.Rows[j].
Cells[ 0 ].Value.ToString() + ";" +
dgvFuncionarios.Rows[j]. Cells[ 1 ].
Value.ToString());
}
wr.Close();
}
private bool ValidaDados () {
int i = 0 ;
bool dadosValidados = true ;
double stringToDouble;
do {
if ( string .IsNullOrWhiteSpace(
dgvFuncionarios.Rows[i].Cells[ 0 ].Value.
ToString()))
dadosValidados = false ;
if (!Double.TryParse(dgvFuncionarios.
Rows[i].Cells[ 1 ].Value.ToString(),
out stringToDouble))
dadosValidados = false ;
} while (++i < dgvFuncionarios.Rows.Count);
return dadosValidados;
}
}
}
Aocontráriodassolu çõesanterioresdestecapítulo,nessaclassequere-
presentaajaneladeintera çãonãoexisteadefini çãodeumrepositórioetam-
poucodeum BindingSource. Paraesseexemplo,avalida çãoeusodos
dadosparagera çãodoarquivoocorrerádiretamentesobreosdadosinfor-
madosno DataGridView.
103

## Página 120

3.3. Informaçãodedadosparagera çãodearquivotexto CasadoCódigo
Dessa maneira, verifica-se logo no início da classe o construtor, que
tem a implementação padrão de todo formulário, chamando o método
InitializeComponents().Estedefinidonoarquivoquecontrolaascon-
figuraçõesvisuaisdoscomponentesinseridosnoformulárioe,emseguida,
realizaconfigura çõesno DataGridView.Cabelembrarqueessasconfigu-
raçõespoderiamtambémtersidorealizadasvisualmentenocontrole.
Comaaplica çãoemexecu ção,ousuáriodeveráinformaraquantidade
defuncionáriosqueterãoseusdadosinformadoseclicarnobotão Criar
linhas para registro. Ométodoquecapturaoevento Clickpara
essebotãoestárepresentadonasequência.
Resolução3.18:métodoquecapturaoeventocliquedobotãode
criaçãodelinhas
private void btnCriarLinhas_Click ( object sender,
EventArgs e) {
int numeroFuncionarios = Convert.ToInt16(
txtNumeroFuncionarios.Text);
if (numeroFuncionarios < 1 )
numeroFuncionarios = 1 ;
int i = 0 ;
do {
var linhaTabela = new DataGridViewRow();
linhaTabela.Cells.Add( new DataGridViewTextBoxCell
{ Value = string .Empty });
linhaTabela.Cells.Add( new DataGridViewTextBoxCell
{ Value = 0 });
dgvFuncionarios.Rows.Add(linhaTabela);
} while (++i < numeroFuncionarios);
txtNumeroFuncionarios.Enabled = false ;
btnCriarArquivo.Enabled = true ;
btnReiniciar.Enabled = true ;
btnCriarLinhas.Enabled = false ;
}
Asprimeirasinstru çõesdestemétodosãoreferentesàconversãodovalor
digitadono TextBoxparainteiroegarantirque,aomenos,umfuncionário
104

## Página 121

CasadoCódigo Capítulo3. Resolvendoproblemasmaiscomplexos:estruturasde...
tenhaseusdadosinformados.Emseguida,umavariávelcontadoraqueserá
usadanaestruturaderepeti çãoédeclarada.
Após esses procedimentos, a estrutura de repetição do...while()
é iniciada. Dentro do bloco, para cada funcionário que terá dados li-
dosécriadaumanovalinha(classe DataGridViewRow). Depois, para
alinhacriada, sãoadicionadascélulas. Comoumacélulapodeserocu-
padapordiversostiposdecontroles, nesseexemplofoiutilizadaaclasse
DataGridViewTextBoxCell,queinserenacélulaum TextBox.
Duranteainstancia çãodaclasse,jáéinseridoovalor defaultparaela.
Tendoasduascélulassidocriadas,alinhaéadicionadaao DataGridView,
pormeiodométodo Add()dapropriedade Rows.Apósaestruturaderepe-
tição,o TextBoxquerecebeaquantidadedefuncionáriosédesabilitado,e
osbotõespara Criar Arquivoe Reiniciar o processo,habilitados.
Assim,obotão Criar linhas para registroétambémdesabilitado.
Aestrutura do...while()éresponsávelpelaexecuçãodeumconjunto
deinstru çõesqueestejamdentrodosdelimitadoresdeblocooferecidospor
ela.Comoacondi çãoparacontinuidadeounãodola çoestánofinal,asins-
truçõesdentrodelaserãoexecutadasaomenosumaúnicavez.Casoapenas
umainstru çãocomponhaaestrutura do...while(),ousodedelimitado-
reséopcional.
Comainterfaceliberadaparaousuárioinformarosdados,apósestes
teremsidoinformados,eleprecisainiciaroprocessoparagera çãodoarquivo
detexto.Paraisso,eleprecisaráclicarnobotão Criar arquivo,quetem
oevento Clickcapturadopelométodoapresentadoaseguir.
Resolução3.19:métodoquecapturaoeventocliquenobotãoque
disparaacria çãodoarquivo
private void btnCriarArquivo_Click ( object sender,
EventArgs e) {
if (!ValidaDados()) {
MessageBox.Show( "Os dados possuem
problemas. Verifique se não deixou
nenhum nome em branco ou se existe um
valor correto para os salários de cada
um ");
105

## Página 122

3.3. Informaçãodedadosparagera çãodearquivotexto CasadoCódigo
}
else if (sfdGravarArquivo.ShowDialog() ==
DialogResult.OK) {
GerarArquivo();
MessageBox.Show( "Arquivo gerado com
sucesso ");
}
}
Paraagera çãodoarquivotextocomosdadosinformadospelousuá-
rio, o primeiro passo é a realização de uma validação. Esse procedi-
mentoérealizadopelaprimeirainstru çãodométodoapresentadoaqui,o
ValidaDados(),invocadocomoargumentodo if().Essavalida çãotem
instruçõesqueserãoexecutadasquandoométododevalida çãoretornarum
valor false,ouseja,quandoelanãoforbem-sucedida. Aseguir,tragoo
métodoValidaDados().
Resolução3.20:métodoquerealizaavalida çãodosdadosinfor-
madosnoDataGridView
private bool ValidaDados () {
int i = 0 ;
bool dadosValidados = true ;
double stringToDouble;
do {
if ( string .IsNullOrWhiteSpace(
dgvFuncionarios.Rows[i].Cells[ 0 ].Value.
ToString()))
dadosValidados = false ;
if (!Double.TryParse(dgvFuncionarios.
Rows[i].Cells[ 1 ].Value.ToString(),
out stringToDouble))
dadosValidados = false ;
} while (++i < dgvFuncionarios.Rows.Count);
return dadosValidados;
}
Oprocessodevalida çãodosdadosinformadosérelativamentesimples.
Sãoapenasduasassitua çõesverificadas:
106

## Página 123

CasadoCódigo Capítulo3. Resolvendoproblemasmaiscomplexos:estruturasde...
1) Seacolunareferenteaonomedofuncionáriopossuiumvalorválido(para
issoéutilizadoométodoestático IsNullOrWhiteSpace()daclasse
string);
2) Seacolunareferenteaovalordosaláriopossuiumvalornuméricocorreto
(estaverifica çãoérealizadapelométodoestático TryParse()daclasse
Double).
Ométodo string.IsNullOrWhiteSpace(),comoopróprionome
diz,verificasea stringenviadacomoargumentoénula,ouseseuconteúdo
éformadoapenasporespa çosembranco.Seuusoéindicadoparavalida ção
destrings.Outrométodosimilaré string.IsNullOrEmpty()ouainda
apropriedade string.Empty.
Ométodo Double.TryParse()tentaconverterumdado string
paraum double.Emcasodesucesso,eleretorna trueearmazenaova-
loremseuargumentodesaída;casocontrário,ométodoretorna falseeo
valordesaídarecebe0(zero).
Continuandoaexplana çãoda Resolução3.19,casoosdadosinformados
estejamcorretoseoprocessodevalida çãoretorneumvalor true,ainstru ção
else if()éexecutada,invocandoométodo ShowDialog()doobjeto
sdfGravarArquivo. Essemétodoexibiráaousuárioajanelaresponsável
paraescolhadolocalondeoarquivoserágravado,assimcomoainforma ção
doseunome.
Caso o usuário realize de maneira correta essa operação, as instru-
ções dentro do bloco doelse if() serão executadas e o método
GerarArquivo()seráinvocadoparaacria çãodoarquivotextocomosda-
dosinformadospelousuário.Nasequência,apresentoessemétodo.
Resolução3.21:métodoresponsávelpelagera çãodoarquivocom
osdadosinformadosnoDataGridView
private void GerarArquivo () {
StreamWriter wr = new StreamWriter(
sfdGravarArquivo.FileName, true );
for ( int j = 0 ;
j < dgvFuncionarios.Rows.Count;
107

## Página 124

3.3. Informaçãodedadosparagera çãodearquivotexto CasadoCódigo
j++) {
wr.WriteLine(dgvFuncionarios.Rows[j].
Cells[ 0 ].Value.ToString() + ";" +
dgvFuncionarios.Rows[j]. Cells[ 1 ].
Value.ToString());
}
wr.Close();
}
Oprocessodegera çãodoarquivoérelativamentesimples.Obtém-seuma
referênciaparaoarquivoqueserácriado,pormeiodaclasse StreamWriter,
efazendousodométodo WriteLine()doobjetodessaclasse,osdadossão
escritos. Aofinal,oobjeto StreamWriteréfechado,gravando,assim,o
arquivo.
Aclasse System.IO.StreamWriterdestina-seàescritadecaracteres
emumacodifica çãoespecífica,comoUTF-8ouANSI,porexemplo.Seuuso
édestinadoparaaescritadelinhasemumarquivodetexto.
Oterceirobotãodisponibilizadonajanelapossibilitaaousuárioareinici-
alizaçãodoprocessocomoumtodo.Apresento,aseguir,ocódigodoevento
Clickdobotão Reiniciar.
Resolução3.22:métodoquecapturaoeventodecliquenobotão
parareiniciaroprocesso
private void btnReiniciar_Click ( object sender,
EventArgs e) {
dgvFuncionarios.Rows.Clear();
txtNumeroFuncionarios.Text = string .Empty;
txtNumeroFuncionarios.Enabled = true ;
btnCriarArquivo.Enabled = false ;
btnReiniciar.Enabled = false ;
btnCriarLinhas.Enabled = true ;
}
Oprocessoparareiniciarainforma çãodosdadossedá,comopodeser
verificadopelasinstru ções, aolimparaslinhasdo DataGridViewedo
TextBoxreferenteàquantidadedefuncionáriosqueserãoinformados. O
estadodesse TextBoxétambémhabilitado.Emseguida,osbotões Criar
108

## Página 125

CasadoCódigo Capítulo3. Resolvendoproblemasmaiscomplexos:estruturasde...
arquivoe Reiniciarsãodesabilitados,eo Criar linhashabilitado.
Comisso,aaplica çãoretornaaoestadoinicial,comosetivessesidoexecutada
pelaprimeiravez.
Emqualquerumadasestruturasderepeti çãomostradasanteriormente,
épossívelusarainstru ção breakparacancelararepeti çãoesairdola ço,ou
aindafor çarapróximaitera çãocomainstru ção continue.Quandoseopta
pelousodainstru ção break,aestruturaéinterrompida,independentemente
dacondi çãoimpostaparatérminoterocorridoounão.Jáquandosefazuso
dainstru ção continue,acondi çãodaestruturaéreavaliadaereiniciada
(ouconcluída),nãosendoexecutadasnaitera çãoasinstru çõesqueestiverem
apósainstru ção continue.
3.4 Conclusão
Estecapítuloapresentouinforma çõesessenciaissobreestruturasderepeti-
ção,quesãomuitoutilizadasnaprograma ção.Éprecisoentenderasquatro
estruturasapresentadas,poisexistemsitua çõesparaquecadaumasejausada.
Paraaaplica çãodessasnovasestruturas,foramusadosnovosrecursose
novastécnicas.Dentreelas,destacam-seaescritaeleituradearquivotexto,
umavezqueesseprocessoécomumenteutilizadoemdiversasaplica çõesco-
merciais.
Comestecapítulo,conclui-seaetapabásicaparaconhecimentodequal-
querlinguagem. Comostrêstiposdeestruturaapresentados–sequencial,
seleção/condicionalerepeti ção–,épossívelaresoluçãodamaioriadospro-
blemasquepossamaparecer.Éclaroqueparticularidadessempreocorrerão,
oqueolevaráaconhecerrecursosespecíficosdalinguagemescolhida.Alguns
dessesrecursossãoreferentesaclassesquedependemumadaoutraouum
conjuntodedeterminadotipodedado/objeto,quesãoapresentadosapartir
dopróximocapítulo.
109

## Página 127

Capítulo4
Váriosprojetosemumasolu ção:
aplicandoalgunsconceitos
relacionadosaoMVCeà
OrientaçãoaObjetos
Nostrêscapítulosanteriores,aOrienta çãoaObjetosfoiapresentadaeapli-
cada. Entretanto,asexplica çõesmantiveram-seapenasnosconceitos,eas
aplicaçõesbasearam-seemalgumastécnicaseusosderecursosjádisponibi-
lizadospelalinguagemeferramentas.Tambémnoscapítulosanteriores,cada
soluçãopossuíaapenasumprojeto.
Estecapítulosededicaráàcria çãodeumasolu çãocomdiversosprojetos,
buscandoaplicarconceitosdeMVCedaOO.Osexemplosfarãousotam-

## Página 128

4.1. Introduçãodosconceitos CasadoCódigo
bém,deumamaneiramaisreal,decole ções,ondeelasserãoutilizadasparaa
aplicaçãodoconceitodeassocia çõesentreobjetos.Recursosvisuaisnãose-
rãotrabalhadosnestecapítulo,masprocureaplicartudoquefoiapresentado
nosanteriores,paraenriquecersuasaplica ções.
4.1 Introdução dos conceitos
Osconceitosapresentadosdemaneirateóricanestecapítulonãoseprendem
anenhumalinguagemdeprograma ção. Sãopontosimportantesenecessá-
riosquebalizamomodeloorientadoaobjetosedequetodoprogramador
deveterconhecimento,mesmoquesejaapenasobásico.Algunsdelesjáfo-
ramapresentadosduranteasresolu çõespropostasnoscapítulosanteriores,
mas,porobjetivosdidáticos,seconcentramnovamenteaqui.Nasequência,
apresento-oscommaisdetalhes.
4.1.1 Objeto
Umobjetopodeserinterpretadocomoqualquerestruturamodularquefa ça
partedealgo,sejaumcarro,umapessoaouumacontecimentoetc. Tendo
umajanelacomoobjeto,pode-seafirmarqueelafazpartedeumacasa,de
umcarroouaindadeumaaplica ção(software). Tantoacasacomoocarro
ouaaplica çãopodemtambémservistoscomoobjetos,compondoobjetos
maiores,ouainda,se associandoaobjetosmaiores.
Emumavisãomaisabstrata,umobjetopodeserumaexpressãomatemá-
ticaouumaequa ção,nasquaisosoperandoseoperadores,alémdoresultado,
podemtambémservistoscomoobjetos.Éimportanteterconhecimentode
quecadaobjetopossui propriedades,comportamentosemétodos,queo
identificamediferenciamdentreoutrosobjetossemelhantes.
Propriedades
Umapropriedadepodeserconceituadacomoainterfacedeumobjeto
comomundoexterno.Essemundoexternopodeservistocomooutrosob-
jetosrelacionando-seentresi,quetambémpodemserchamadosdeobjetos
clientesdoservi çooferecido.Ainterfacedeumobjetoéaquiloqueousuário
(cliente)doobjeto(porexemplo,outroobjeto)visualizaeaoqualtemacesso.
112

## Página 129

CasadoCódigo Capítulo4. Váriosprojetosemumasolução:aplicandoalgunsconceitos...
Retornandoaoexemplodocarrocomoobjeto,a Cordocarropodeser
visualizadacomoumapropriedade. Combasenesseexemplo,identifica-se
queaspropriedadescaracterizamumobjeto,ouainda,oestadodele. Dois
carrospodemserdiferenciadosentresipormeiodesuaspropriedades.Eles
podemtermuitascaracterísticasemcomum,masumaodiferenciará:onú-
merodo chassi.Assim,identifica-setambéma identidadedoobjeto,queé
umapropriedadetambém.
Comportamentos
Emrela çãoaoscomportamentospossíveis(ouesperados)porumobjeto,
épossíveldefini-loscomorea çõesdeumobjetoemdecorrênciadealguma
interaçãocomele.
Tendoumobjetomaiscomumcomoobjetivodestelivro,pegaremos
comoexemploumajaneladeumaaplica ção.Nestaháumbotãolocalizado
nabarradetítulo,quetemaresponsabilidadedefechá-la.Aocorrênciadessa
responsabilidadeéumarea çãoaum eventosofrido,queseriao cliquenesse
botão.
Destamaneira,pode-seafirmarqueocomportamentodeumobjetoestá
relacionadoàsa ções(emdecorrênciaarea ções)poreleexecutadas,normal-
menterelacionadasàintera çãoentreobjetos,ouaindacomoprópriousuário
daaplica ção.
Métodos
Como comentado na explanação sobre comportamentos, para cada
eventoocorreumarea çãoeestesdoisitens,juntoscomosmétodos,caracte-
rizamarealiza çãodoscomportamentos.Osmétodos,narealidade,realizam
area çãodoseventoscapturadospelosobjetos.
Noexemplosobreofechamentodeumajaneladeaplica ção,aa çãode
fecharajanelaprecisaocorrer,poiselanãosefechasemumainstru çãoque
realizeesteprocesso.Semprequeocorreumevento,este delegaaummétodo
aresponsabilidadedeexecutarosprocedimentosnecessáriosparaarealiza-
çãodoevento.
Ummétodoécompostoporumconjuntodeinstru çõeseépormeiodeles
queocorreaintera çãoentreobjetos,oqueemalgumasliteraturasétambém
113

## Página 130

4.1. Introduçãodosconceitos CasadoCódigo
conhecidocomo troca de mensagens entre objetos. Ainda,demaneirasim-
plificada,épossíveldizerqueummétodorepresentaasa çõestomadaspelos
objetos,ouseja,osservi çosqueeledisponibilizaeexecuta.
4.1.2 Classe
Naexplica çãosobreobjetosfoidado pessoacomoexemplo.Jásobreproprie-
dades,oexemplodado(cordoscarros)apresentouasitua çãodemaisdeum
objetodeummesmotipo,precisandoinclusivedealgumapropriedadeque
identificasse(oudistinguisse)umobjetodeoutro. Comisso,pode-seiden-
tificarqueosobjetossãovistoscomoconjuntos,umconjuntode pessoasou
umconjuntode carros,porexemplo.
Quandoforamapresentadoscomportamentosemétodos,foicomentado
queexisteanecessidadedeumconjuntodeinstru çõesoferecidaserealizadas
porcadaobjeto. Entretanto,nãoseriapráticoquecadaobjetotivesseessas
instruçõesimplementadasnele? Inclusivepelofatodequeseesperaqueo
comportamento(oupropriedades)decadaobjeto,deummesmoconjunto,
sejaomesmo.Porexemplo,todososcarrospossuemumacor(propriedade)
esofremprocessosdefrenagemeacelera ção(comportamento).
Paraaimplementa çãodestesmétodosepropriedadescomuns,quese-
rãoutilizadosporumconjuntodeobjetos,usa-seoconceitodeclasses.Uma
classepodeservistacomoumacategoriza çãodeobjetoscomuns,uma cate-
goriaquerepresentaumconjuntode objetos. Destamaneira,todaacodi-
ficação(implementa ção)parapropriedadesemétodossedánaclasse,eos
objetosquerepresentamasclassestrazememsiapossibilidadedeutilizá-los.
4.1.3 Abstração
Aabstra çãonãoéumtermoexclusivodaáreadeinformática,éalgoquedia
adiatodosvivenciamourealizam.Umexemplo,jáfazendousodaleiturade
livros,podeserumasitua çãoemqueváriaspessoasleemumanarrativade
umromancenoqualopersonagemdescreveumapaisagem.
Certamentecadaleitorvisualizaráemsuamenteumapaisagemtotal-
mentediferentedoqueoutrosvisualizam,ou,aomenos,comparticulari-
dadesqueadiferenciam.Esteresultadoéacapacidadedeabstra çãoquecada
114

## Página 131

CasadoCódigo Capítulo4. Váriosprojetosemumasolução:aplicandoalgunsconceitos...
indivíduopossui:queéa“materialização”deconceitos,ideiasoupensamen-
tos.Levandooconceitodeabstra çãoparaaáreacomputacional,pode-seafir-
marqueelaéconsideradacomoahabilidadedemodelarcaracterísticasdo
mundoreal,deumdenominadoproblemaemquestão,queoprogramador
buscaresolver.
4.2 Implementando os conceitos apresentados
Comosconceitosbásicosapresentadosecomvistaparaaaplica çãodeles,o
desenvolvimentodeumpequenoexemploseráiniciado.Paraestaatividade,
oprimeiroconceitoaseraplicadoéodeabstra ção.Paraqueessaabstra ção
possaocorrer,éprecisoumestudosobreoproblemaparaque,comasua
compreensão,ummodelopossaserobtido.Nasequência,oenunciadoque
apresentaoproblema:
Supondo que uma empresa tenha a necessidade de uma aplicação que possi-
bilite o registro de compras realizadas por ela, crie um modelo para o formulário
que representará essa aplicação.
Combasenopropostoeumaanáliserealizada,abstrai-sequeoformulá-
rioparaomodeloprecisacontemplar:
• Os dados relacionados ao fornecedor dos produtos, como nome e
CNPJ;
• Emrelaçãoaosdadospertencentesaoprocessoderegistro,oformulá-
rioprecisadasdatasdeemissãodanotapelofornecedoreadataem
queoprodutotemaentradaregistradanaempresa,alémdonúmero
danotafiscal;
• Paraosprodutosadquiridos,éprecisoinformaradescrição,opre çode
custoeaquantidadecompradaparacadaum,alémdocódigoqueo
identifica.
Comaanáliseeaabstra çãosobreoenunciadorealizadaseasproprie-
dadesbásicasidentificadas,épossívelconstatarqueexistemdoisgruposde
informações:umqueserefereànotadeentrada(número,fornecedoreda-
tas)eoutroqueserefereaosprodutosadquiridosnacompra.Destamaneira,
115

## Página 132

4.2. Implementandoosconceitosapresentados CasadoCódigo
duascategoriasdeobjetossãoidentificadas,ouseja,duasclasses.Essacate-
gorizaçãoénecessária,demaneirabembásica,pelofatodequeumprocesso
deaquisi ção(acompra)relaciona-seaváriosprodutos.Assim,paracadaob-
jetoquerepresentaumanotadeentrada,poderãoexistirváriosobjetosque
representamosprodutos.
Aimplementa çãoinicialdaclassequerepresentaosdadosdanotapode
servisualizadanasequência.
Resolução4.1:classequerepresentaaNotadeEntrada(Versão1)
using System ;
namespace ModelProject {
class NotaEntrada {
public string NumeroNota { get ; set ; }
public string NomeFornecedor { get ; set ; }
public string CNPJ { get ; set ; }
public DateTime DataEmissao { get ; set ; }
public DateTime DataEntrada { get ; set ; }
}
}
ParaquemjátemumbomconhecimentoemOrienta çãoaObjetos(e
tambémembancodedados),certamenteverificouqueomodelonãoestá
normalizadoetampoucoestáemumagranularidadecorretaparaopara-
digmadeOO.Paraummodeloeimplementa çãocorretos,serianecessário
umparticionamentodaclasse NotaEntradaemduas,separandoosdados
pertencentesaofornecedorparaumaclasseespecífica( Fornecedor)eman-
tendonaclasseoriginalapenasosdadosrelacionadosaoprocessodecompra.
Aclasseinicialquerepresentacadaprodutoadquiridopelanotaéapre-
sentadaaseguir.
Resolução4.2:classequerepresentaaNotadeEntrada(Versão1)
namespace ModelProject {
class ProdutoNotaEntrada {
public string CodigoProduto { get ; set ; }
116

## Página 133

CasadoCódigo Capítulo4. Váriosprojetosemumasolução:aplicandoalgunsconceitos...
public string Descricao { get ; set ; }
public double PrecoCusto { get ; set ; }
public double QuantidadeComprada { get ; set ; }
}
}
Noprocessorelacionadoaoregistrodeumacompra,asduasclassesiden-
tificadasencaixam-seemumtipode“relacionamento”chamadodemaster-
detail,ouainda, pai-filhos. Nesterelacionamento,pode-sedizerquepara
cadaobjetodaclasse NotaEntradapodemexistirváriosobjetosdaclasse
ProdutoNotaEntrada. Com esta informação, é preciso apenas definir
comoimplementaressa associaçãoentreessasclasses. Nesteprimeiromo-
mento,seráfeitoousodeumamatrizparaisso.Aseguir,apresentoumanova
versãoparaaclasse NotaEntrada.
Matrizessãocomunsemsitua çõespráticasnasquaissenecessitarefe-
renciarumgrupodevariáveisdomesmotipo,pelomesmonomesimbólico.
Podemservistascomoumconjuntodevariáveisdomesmotipo,referenciá-
veispelomesmonomeeindividualizadasentresipormeiodesuaposi ção
dentrodesseconjunto.Sãoconhecidastambémcomo variáveis indexadas.
Resolução4.3: classeNotaEntradacomapropriedadeProdutos
adicionada(Versão2)
using System ;
namespace ModelProject {
class NotaEntrada {
public string NumeroNota { get ; set ; }
public string NomeFornecedor { get ; set ; }
public string CNPJ { get ; set ; }
public DateTime DataEmissao { get ; set ; }
public DateTime DataEntrada { get ; set ; }
public Produto[] Produtos { get ; set ; }
}
}
Anovapropriedade Produtoséumamatrizdotipo Produto. Na
definiçãodapropriedade,ousodoscolchetes( [])caracterizaqueelaserá
umamatriz.Emsuadefini ção,nãofoiestipuladoumtamanhofísicoparaela,
117

## Página 134

4.3. Associaçõesentreobjetos CasadoCódigo
ouseja,quantoselementos(ouprodutos)elapoderárecebercomomáximo.
Essetamanhoserádefinidonasuainicializa ção.
Épossívelverificarcomissoumlimitador,queéadefini çãodotamanho
paraapropriedadequerepresentaumconjunto/cole çãodedados/objetos.
Nestecaso,ousedefineumtamanhoenorme,paraevitarqueemumadeter-
minadasitua çãonãosejamaispossívelinserirnovoselementos,ouépreciso
saberquantoselementosserãoinseridosnela,antesdeutilizar. Asegunda
opçãoéamelhor,poisnocasodaprimeira,espa çosreservadosparapossí-
veiselementos,quenãoforemusados,terãofeitousoderecursos(espa çona
memória)demaneiraineficiente.
Apesardousodematrizserpossível,ascaracterísticasapresentadasan-
teriormentetrariamparaoprogramadordiversassitua çõesquenãofazem
partedoproblema,queéregistraraentradadeprodutos.Buscandominimi-
zaressesproblemasepossibilitandoaoprogramadordedicartodootempode
desenvolvimento(ouamaiorpartedele)paraaresolu çãoespecíficadopro-
blemaproposto,érecomendadoousodecole ções( Collections)quando
sefazusodeassocia ções.
4.3 Associações entre objetos
Anteriormente, na explica ção sobre a “ligação” entre as classes
NotaEntrada e ProdutoNotaEntrada, foi utilizado o termorelaci-
onamento, uma expressão comum quando falamos em banco de dados.
Entretanto,noparadigmaorientadoaobjetos,otermocorretoé associação,
tambémcomentadoanteriormente.
Umaassocia çãopossuialgumascaracterísticasquesãoimportantespara
omomentodaimplementa ção.Paraoexemplotrabalhado,aassocia çãoiden-
tificadaéade composição,quetrabalhaoconceitode todo-parte,noqual
apartetemseutempodevidadiretamenteligadoàpartetodo.Issosignifica
quequandoumobjetodaclassetodo( NotaEntrada)forremovido,todosos
objetosdaclasseparte( ProdutoNotaEntrada)tambémdeverãoser,pois
nãofazsentidosuaexistênciasemoobjetotodo.
EmOO,uma associaçãorepresentaumvínculoentreobjetosdeumaou
maisclasses,demaneiraqueestesserelacionem. Épossívelque,pormeio
118

## Página 135

CasadoCódigo Capítulo4. Váriosprojetosemumasolução:aplicandoalgunsconceitos...
dessesvínculos(associa ções),umobjetoinvoque(ourequisite)servi çosde
outroobjeto,ouqueacesseouatribuavaloresapropriedadesdeste.Asasso-
ciaçõespodemserunárias,ocorrendoemobjetosdamesmaclasse;binárias,
quandoocorreremcomdoisobjetosdeclassesdistintas;emúltiplas,quando
ocorreremmaisdedoisobjetosdeclassesdistintas.
Aassociaçãodireta aindapodeservistacomooconceitodeposse,em
que,noexemploapresentado,umobjetodaclasse NotaEntradatemum
conjuntodeobjetosdaclasse ProdutoNotaEntrada.
Composição éumacaracterísticadeumaassocia ção,naqualumob-
jeto é responsável por gerenciar o ciclo de vida de outros objetos. Fa-
zendo uma análise mais refinada na associação entre NotaEntrada e
ProdutoNotaEntrada, é possível constatar que um objeto da classe
NotaEntradaécompostoporobjetosdaclasse ProdutoNotaEntrada.
Nãohámotivosquejustifiquemaexistênciadeobjetosdasegundaclassesem
quehajaumobjetodaprimeira.
Paragarantirascaracterísticasdeassocia çãodiretaecomposi çãonas
resoluções apresentadas, é preciso detalhá-las um pouco mais. Para
umarealaplica çãodaassocia çãodireta,duasnovasclassesserãocriadas:
Fornecedore Produto. Tambémfaz-senecessáriaarealizaçãodealte-
raçõesnasclasses NotaEntradae ProdutoNotaEntrada.
Apresento,aseguir,aclasse Fornecedor.
Resolução4.4:classeFornecedor(Versão1)
using System ;
namespace ModelProject {
class Fornecedor {
public Guid Id { get ; set ; }
public string Nome { get ; set ; }
public string CNPJ { get ; set ; }
}
}
Um Guidrepresentaumnúmerointeirode16bytes,quepodeserusado
semprequefornecessárioumidentificadorquesejaúnico,compoucaproba-
119

## Página 136

4.3. Associaçõesentreobjetos CasadoCódigo
bilidadedeexistênciadeduplica çãodeseusvalores.Normalmente,eleéuti-
lizadoparaidentificarcomputadoresouredesdecomputadores;entretanto,
nadaimpedeoseuusonaidentifica çãodeobjetos.
Anovaclasse Fornecedortrazparasiaresponsabilidadedemanter
aspropriedadesreferentesafornecedoresemvezdenecessitarrepetiresses
dadosemcadaobjeto NotaEntrada.
Nasequência,tragoaclasse Produto.
Resolução4.5:classeProduto
namespace ModelProject {
class Produto {
public Guid Id { get ; set ; }
public string Descricao { get ; set ; }
public double PrecoDeCusto { get ; set ; }
public double PrecoDeVenda { get ; set ; }
public double Estoque { get ; set ; }
}
}
Semelhanteàclasse Fornecedor,aclasse Produtotrouxeparasia
responsabilidadedaspropriedadesquedizemrespeitoacadaproduto.Esses
dadosserãoinformadosumaúnicavezporprodutoemvezdesereminfor-
madosacadaregistrodenotadeentrada.E,noregistrodanotadeentrada,
essesdadosserãoobtidos.
Apresento, na sequência, a nova implementação para a classe
ProdutoNotaEntrada.
Resolução4.6:classeProdutoNotaEntradacomassocia ção(Ver-
são2)
namespace ModelProject {
class ProdutoNotaEntrada {
public Guid Id { get ; set ; }
public Produto ProdutoNota { get ; set ; }
public double PrecoCustoCompra { get ; set ; }
public double QuantidadeComprada { get ; set ; }
120

## Página 137

CasadoCódigo Capítulo4. Váriosprojetosemumasolução:aplicandoalgunsconceitos...
}
}
Nanovaimplementa çãodaclasse ProdutoNotaEntrada,épossível
verumaassociaçãodireta comaclasse Produto,pormeiodapropriedade
ProdutoNota.Verifica-seaexistênciadeumapropriedadeparaguardaro
preçodecustodoprodutonacompraaserregistrada,enquantoopre çode
custodaclasse Produtotemoobjetivoderegistrarocustoatualparacada
produto.
4.4 Composição entre classes fazendo uso de
Collections
Aestrutura foreachéresponsávelpelaleituradetodososelementosdeuma
coleção,associandocadaumdelesaumavariável,acadaitera ção.
Finalizandoométodo,apóso foreach,osvaloresobtidosnasvariáveis
“acumuladoras”sãoatribuídosàúltimalinhadogrid,devidamenteforma-
tados,assimcomoovalorparao Labelaoladodo Button,queexibeo
totalconsumido,semosdescontos.
4.5 Leitura de arquivo texto para cálculo de
reajuste em folha de pagamento
A associa ção realizada entre as classes NotaEntrada e
ProdutoNotaEntrada e apresentada naResolução 4.3 faz uso de
matrizes e apenas foi exibida sem determinar como os objetos seriam
registrados. Conformetambémcomentado, omaisindicadoéousode
Collections.Destamaneira,a Resolução4.7 trazanovaimplementa ção
paraessaclasse.
Abibliotecabásicadeclassesdo.NET,a Base Class Library(BCL),oferece
umvastoconjuntodeclassesparacole ções.Essasclassespossibilitamumfácil
gerenciamentodecole çõesdeobjetos,oquepodeserdificultosoquandose
usamatrizes.Entretanto,éprecisoconhecercadaumadelasparasaberqual
éamaisindicadaparaoproblemaasertrabalhado.Aescolhacorretapode
serachaveparaumaboaperformanceemanuten çãodeumaaplica ção.
121

## Página 138

4.5. Leituradearquivotextoparacálculodereajusteemfolhadepagamento CasadoCódigo
Resolução4.7: classeNotaEntradacomassocia çãopormeiode
umacole ção(Versão3)
using System ;
using System.Collections.Generic ;
namespace ModelProject {
class NotaEntrada {
public Guid Id { get ; set ; }
public string Numero { get ; set ; }
public Fornecedor FornecedorNota { get ; set ; }
public DateTime DataEmissao { get ; set ; }
public DateTime DataEntrada { get ; set ; }
public IList<ProdutoNotaEntrada> Produtos
{ get ; set ; }
}
}
Verifica-senadeclara çãodapropriedade Produtosqueelaédefinida
comosendo IList,queéumainterface.Nadeclara çãodotipodacole ção,
aindaexistenasintaxeadefini çãodotipodedadoúnicoquedeveseraceito
noselementosquevãocomporacole ção <Produto>. Estamaneirapara
definiçãodecole çõeséconhecidacomo Generics.
Conceitualmente,umacole çãoésemelhanteaumamatriz. Porém,os
benefíciostrazidosporumacole çãosãograndes.Estaoperasobreobjetosda
classe Object,ouseja,elapodepossuirqualquertipodeobjeto,aocontrário
deumamatriz,queemsuadeclara çãoespecificaotipodedadodosobjetos
queavãocompor.
Paratornarascole çõesmaiseficientes,surgiramos Generics,quede-
finemqueosobjetosdeumacole çãocomessacaracterísticasejamapenasdo
tipoespecificado.Issotornaacole çãofortementetipada,poisaceitaráapenas
essesobjetos.
Aassocia çãoporcomposi ção,quandoimplementada,precisagarantirsua
característica,queéademanterosobjetosda“parte”apenasenquantoo“todo
exista”. Paraoexemplo,osprodutosdanotadeentradasódeverãoexistir
enquantoanotaexistir,oquelevaparaaclasse“todo”aresponsabilidade
pelamanuten çãodessesdados.Paraisso,umanovaimplementa çãodeveser
realizada,queestáapresentadaaseguir.
122

## Página 139

CasadoCódigo Capítulo4. Váriosprojetosemumasolução:aplicandoalgunsconceitos...
Resolução4.8:classeNotaEntradacommétodosimplementados
(Versão5)
using System ;
using System.Collections.Generic ;
namespace ModelProject {
class NotaEntrada {
public Guid Id { get ; set ; }
public string Numero { get ; set ; }
public Fornecedor FornecedorNota { get ; set ; }
public DateTime DataEmissao { get ; set ; }
public DateTime DataEntrada { get ; set ; }
public IList<ProdutoNotaEntrada> Produtos
{ get ; set ; }
public NotaEntrada (){
this .Produtos = new
List<ProdutoNotaEntrada>();
}
public void RegistrarProduto (
ProdutoNotaEntrada produto) {
if (! this .Produtos.Contains(produto))
this .Produtos.Add(produto);
}
public void RemoverProduto (
ProdutoNotaEntrada produto) {
this .Produtos.Remove(produto);
}
public void RemoverTodosProdutos () {
this .Produtos.Clear();
}
}
}
Para que o métodoRemoverProduto()– que recebe uma instân-
ciadoobjeto ProdutoNotaEntrada–possarealmenteremoveroobjeto
123

## Página 140

4.5. Leituradearquivotextoparacálculodereajusteemfolhadepagamento CasadoCódigo
corretoeparaque,nométodo RegistrarProduto(),abuscarealizada
pelachamada Contains()possatambémserexecutadacorretamente,é
precisodefinirnaclassecomoeladeverátrataraidentidadedeseusobje-
tos. Estaimplementaçãodá-sepelasobrescritadosmétodos Equals()e
GetHashCode(),comomostroaseguir.
Resolução4.9:classeProdutoNotaEntradacommétodosEquals()
eGetHashCode()(Versão3)
namespace ModelProject {
class ProdutoNotaEntrada {
public Guid Id { get ; set ; }
public Produto ProdutoNota { get ; set ; }
public double PrecoCustoCompra { get ; set ; }
public double QuantidadeComprada { get ; set ; }
protected bool Equals (ProdutoNotaEntrada other) {
return Id.Equals(other.Id);
}
public override bool Equals ( object obj) {
if (ReferenceEquals( null , obj))
return false ;
if (ReferenceEquals( this , obj))
return true ;
if (obj.GetType() !=
typeof (ProdutoNotaEntrada))
return false ;
return Equals ((ProdutoNotaEntrada) obj);
}
public override int GetHashCode () {
return ProdutoNota.GetHashCode();
}
}
}
Aimplementa çãoparaométodo Equals()apresentadatemummé-
todo a mais do que a que vimos no capítulo 3. Esta nova implemen-
124

## Página 141

CasadoCódigo Capítulo4. Váriosprojetosemumasolução:aplicandoalgunsconceitos...
tação é o métodoEquals()específico da classe, e não o sobrescrito (
override). Nessenovométodo,oobjetorecebidoéodetipodesejado(
ProdutoNotaEntrada),enãoum Object. Épossívelverificartambém
queométodosobrescritorealizaumachamadaaessenovométodoquando
identificaqueotipodoobjetorecebidoé ProdutoNotaEntrada.
Pelaformacomoométodo Equals()foiimplementado,seousuário
inserirduasvezesomesmoproduto,essaopera çãoseráaceita,oquenãoé
correto,poisdeveriaserinseridoumavezomesmoproduto,comduasunida-
desnaquantidade.Busqueimplementaro Equals()combasenoproduto.
Asduasclassesimplementadasparaaassocia çãodecomposi çãodevem
servistascomoservi ços,ouseja,omodelodenegóciodaaplica ção.Paracon-
sumiressesservi ços,éprecisopensarnacamadaemqueousuáriointeragirá
comaaplica ção,ouseja,acamadadevisão,ainterfacecomousuário.Atela
deumanotadeentradaouumapáginawebsãoexemplosdeimplementa ção
dessacamada.
Independentedatecnologiaadotadaparaacamadadeapresenta ção,a
interaçãodelacomacamadademodelodenegócionãodeveocorrerdema-
neiradireta.Paraisso,umacamadadecontroleérecomendada.
4.6 C riação dos projetos e definição de depen -
dência entre eles
Paraaplicaroconceitoapresentado,crieumanovasolu ção. Nela,crieum
novoprojetodotipo Class Libraryedêaeleonomede ModelProject.
Nesse novo projeto, elimine o arquivo de classe criado e crie as classes:
Fornecedor, Produto, NotaEntradae ProdutoNotaEntrada,se-
guindoaimplementa çãoapresentadanaúltimaversãodasrespectivasresolu-
ções.Esseprojetoseráresponsávelpelaimplementa çãodacamadademodelo
(oudenegócio).
Paraimplementaracamadadeintera çãocomousuário(adeapresen-
taçãoouvisão),crienasolu çãoumnovoprojeto,agoradotipo Windows
Forms Application, dando a ele o nome deViewProject. Nesse
novoprojeto,removaoformuláriocriadoautomaticamenteecrietrêsnovos:
FormFornecedor, FormProdutoe FormNotaEntrada.
125

## Página 142

4.6. Criaçãodosprojetosedefini çãodedependênciaentreeles CasadoCódigo
Paraapersistênciadosobjetosinformadosnosformulários,seráfeitouso
decole ções.Destamaneira,osdadosexistirãoapenasenquantoaaplica ção
estiveremexecu ção. Reforça-sequeoimportantenestemomentoéoco-
nhecimentoeaaplica çãodastécnicaserecursosparaaplica çãodaassocia-
çãodecomposi ção. Oacessoaobancodedadosseráapresentadoetraba-
lhado,inicialmente,nocapítulo5.Sendoassim,crieumnovoprojeto Class
Library,chamado PersistenceProject.Nele,crieumaclassechamada
Repositoryeaimplementeconformeapresentadonasequência.
Resolução4.10:classeRepository
using System.Collections.Generic ;
using ModelProject ;
namespace PersistenceProject {
public class Repository {
private IList<Fornecedor> fornecedores =
new List<Fornecedor>();
private IList<Produto> produtos =
new List<Produto>();
private IList<NotaEntrada> notasEntrada =
new List<NotaEntrada>();
public Fornecedor InsertFornecedor (
Fornecedor fornecedor) {
this .fornecedores.Add(fornecedor);
return fornecedor;
}
public void RemoveFornecedor (Fornecedor fornecedor) {
this .fornecedores.Remove(fornecedor);
}
public IList<Fornecedor> GetAllFornecedores() {
return this .fornecedores;
}
public Fornecedor UpdateFornecedor (
126

## Página 143

CasadoCódigo Capítulo4. Váriosprojetosemumasolução:aplicandoalgunsconceitos...
Fornecedor fornecedor) {
this .fornecedores[ this .fornecedores.
IndexOf(fornecedor)] = fornecedor;
return fornecedor;
}
}
}
Aclasse Repositoryoferecemétodospúblicosparainserireatualizar
osobjetos.Ocorretoseriaqueessaclasseeoscontroladoresquefazemuso
deseusservi çospossuíssem,demaneirapública,apenasummétodo–neste
exemplo,o SaveFornecedor()–eesteinvocasseométododeinser ção
ouatualiza ção,quedeverãoserprivados,deacordocomoobjetoquerecebe.
IssoporquearegrainicialparainserirumobjetoéqueelenãopossuaumID.
Destamaneira,seométodo SaveFornecedor()receberumobjeto
comID,eledeveinvocaro UpdateFornecedor();casocontrário,omé-
todochamadodevesero InsertFornecedor(). Procureimplementar
essatécnica,masveremosnocapítulo 5comosefaz.
Essaresolu çãoapresentaapenasmétodosparaosfornecedores.Crie,de
maneirasemelhante,osmesmosmétodosparaosoutroscampos( produtos
e notasEntrada).
Aqui,épossívelverificarque,nasimporta çõesdenamespaces( usings),
há a referência para o projeto de modelo, oModelProject. A classe
Repositoryestádefinidanonamespace PersistenceProject.
Verifique que, por padrão, os namespaces das classes são idênticos
aos nomes dos projetos, mas é claro que é possível mudar isso e defi-
nirnamespacesespecíficosparacadauma. Emresumo, tem-seumpro-
jeto( PersistenceProject)fazendousoderecursos(classes)deoutro
(ModelProject).Oqueocorredemaneiramaistécnicaéqueoprimeiro
referenciaosegundo.
Paraconfigurarareferêncianecessária,cliquecomobotãodireitodo
mousesobreonomedoprojeto PersistenceProjecteselecioneaop-
ção Add Reference.Najanelaqueéexibida,expandaaop ção Solution
e,em Projects,marqueacaixadesele çãoaoladodonomedoprojeto
ModelProject.
127

## Página 144

4.6. Criaçãodosprojetosedefini çãodedependênciaentreeles CasadoCódigo
Fig.4.1:Selecionandoprojetoparatermosreferênciaadicionada
Casooprojeto ModelProjectnãoapare çanarela çãodeprojetosda
solução,éprecisoquesejarealizadoobuilddasolu ção.
Após confirmar a inclusão da referência clicando no botãoOK na
Solution Explorer,épossívelverificaraexistênciado ModelProject
noprojeto PersistenceProject,em References.
128

## Página 145

CasadoCódigo Capítulo4. Váriosprojetosemumasolução:aplicandoalgunsconceitos...
Fig.4.2:ReferênciaaoprojetoModelProjectadicionadaaoPersistenceProject
Nessaimplementa çãodeclasse,mesmoadicionandoareferênciaaopro-
jeto ModelProjecteinserindoainstru ção using ModelProjectnocó-
digo,aoreferenciaraclasse Fornecedor,ocompiladoraindaacusaráerro,
nãoidentificandoessaclasse. Issoocorreporqueaclasse Fornecedorno
ModelProjectnãotemnenhummodificadordeescopo(oudeacesso).É
precisoatualizartodasasclassesqueserãousadasemoutrosprojetospara
serempúblicas( public).Apenasparaexemplificar,a Resolução4.11apre-
sentaamudan çanaclasse Fornecedor.
Pormeiode modificadoresdeacesso épossíveldefinircomoasclasses
eseusmembrosserãovisíveisporoutrasclassesesuasinstâncias.Osmodi-
ficadoresdisponíveissão: public, private, protectede internal.
Quandoumaclasseécriadasemummodificadordeescopodefinido,éatri-
buídoo internalporpadrão.Pormeiodele,asclassessãovisíveisapenas
dentrodo assemblyqueasdefine.Nocasodoexemplo,apenasoprojeto
queimplementaaclasseareconhece.Umaclassedefinidaemumprojeto,e
queseráutilizadaemoutro,precisaserdefinidacomo public.
Resolução4.11:classeFornecedorcommodificadordeacessopu-
blic(Versão2)
129

## Página 146

4.7. Criandoacamadadeapresenta ção CasadoCódigo
namespace ModelProject {
public class Fornecedor {
public Guid Id { get ; set ; }
public string Nome { get ; set ; }
public string CNPJ { get ; set ; }
}
}
Realizenasdemaisclassesaaltera çãoapresentadaaqui,ondeasclasses
recebamomodificadordeescopo public.
4.7 Criando a camada de apresentação
Noprojetocriadoanteriormenteparaacamadadeapresenta ção,chamado
ViewProject,noformulário FormFornecedor,feitoparapermitirain-
teraçãodousuárionamanuten çãodosdadosrelativosafornecedores,imple-
menteajanelaapresentadanafiguraaseguir.
Fig.4.3:Formulárioparamanuten çãoemdadosdeFornecedores
Oformuláriodesenhadoeapresentadonafigura 4.3possuiumcompo-
nente TableLayoutPanel,divididoemlinhasecolunasparaumame-
lhordistribui çãodoscontroles.Os Labels Id, Nomee CNPJtêmaoseu
130

## Página 147

CasadoCódigo Capítulo4. Váriosprojetosemumasolução:aplicandoalgunsconceitos...
lado TextBoxs,quepermitirãoaintera çãocomousuário,comexce çãodo
TextBoxdo Id,queestádefinidocomodesabilitado( Enabled = False).
Botõesparaasopera çõesdemanipula çãonosdadostambémforaminseridos,
comotambémum DataGridViewaofinal,queexibirátodososfornecedo-
rescomdadosjáregistrados.
No SmartTagdo DataGridView,desmarqueos Checkboxscon-
formeafigura4.3.Atribuatambémàpropriedade SelectionModeovalor
FullRowSelect.
Fig.4.4:Configura çãodepropriedadespormeiodoSmartTagdoDataGrid-
View
Os dados informados neste formulário serão inseridos na cole-
ção fornecedores, definida na classe Repository no projeto
PersistenceProject.Entretanto,acamadadeapresenta çãonãopodein-
teragirdemaneiradiretacomacamadadepersistência,poispodeocorrerde
umadelasmudar;issorefletiriaemmuitamanuten ção.
Paraevitarisso,seráprecisocriarumprojetoquerepresentaráacamada
controladora, fechandoassimoMVC.Nasolu ção, crieumnovoprojeto
dotipo Class Libraryeonomeiecomo ControllerProject. Eli-
mineaclassecriadaporpadrãocomoprojetoecrieumaclassechamada
131

## Página 148

4.7. Criandoacamadadeapresenta ção CasadoCódigo
FornecedorController,comoapresentadonasequência.
Resolução4.12:classecontroladoraparaservi çosrelacionadosà
classeFornecedor
using System.Collections ;
using ModelProject ;
using PersistenceProject ;
namespace ControllerProject {
public class FornecedorController {
private Repository repository = new Repository();
public Fornecedor Insert (Fornecedor fornecedor) {
return this .repository.
InsertFornecedor(fornecedor);
}
public void Remove (Fornecedor fornecedor)
this .repository.RemoveFornecedor(fornecedor);
}
public IList<Fornecedor> GetAll() {
return this .repository.GetAllFornecedores();
}
public Fornecedor Update (Fornecedor fornecedor) {
return this .repository.UpdateFornecedor
(fornecedor);
}
}
}
Aqui, apresento apenas o controlador paraFornecedor. Crie, de
maneirasemelhante,umaclassecontroladoraparaasclasses Produtoe
NotaEntrada.
Note no código que existem as cláusulasusing ModelProject e
using PersistenceProject,oqueindicaanecessidadedeincluirasre-
ferênciasparaestesprojetosnoprojeto ControllerProject.
132

## Página 149

CasadoCódigo Capítulo4. Váriosprojetosemumasolução:aplicandoalgunsconceitos...
Acamadadeapresenta çãoprecisaacessaracamadadecontrole,paraque
elaseresponsabilizeemdelegarasresponsabilidadesparaacamadadenegó-
cio(modelo)ouadepersistência.Destamaneira,atribuaao ViewProject
a referência para oControllerProject. E, na classe do formulário
FormFornecedor,declareumcampoparaocontroladorcriado,comoapre-
sentadoaseguir.
Resolução4.13:declara çãodocontroladornacamadadeapresen-
tação(Versão1)
public partial class FormFornecedor : Form {
private FornecedorController controller =
new FornecedorController ();
// Código omitido
}
Comocontroladorimplementado,éprecisoimplementaroscomporta-
mentosdosbotõesdisponíveisparaaintera çãocomousuário. Oprimeiro
botãoaserimplementadoseráo Gravar.Veja,nasequência,aimplemen-
taçãoparaométodoquecapturaoevento Clickdessebotão.
Resolução4.14:métodoparaocliquedobotãoGravar(Versão1)
private void btnGravar_Click ( object sender, EventArgs e) {
this .controller.Insert(
new Fornecedor () {
Id = Guid.NewGuid(),
Nome = txtNome.Text,
CNPJ = txtCNPJ.Text
}
);
}
Aimplementa çãoparaestemétodoresume-seàinvoca çãodométodo
implementadonocontroladorparainser çãodeumfornecedor.Comexce ção
do Idparaofornecedor,queégeradonessemétodo,osdemaisvaloressão
obtidosdiretamentedoscontrolesdajanela.
133

## Página 150

4.7. Criandoacamadadeapresenta ção CasadoCódigo
Nestemomento,jáépossíveltestaraaplica ção.Realizeumbuildparave-
rificaçãodepossíveiserrose,emcasodeexistência,corrija-os.Paraexecutara
solução,cliquecomobotãodireitosobreonomedoprojeto View Project
e,então,cliqueem Set as Startup Project.Naclasse Program,de-
finaoformulário FormFornecedor.cs,comooqueseráinstanciadona
execuçãodaaplica ção.
Nesseexemplo,agera çãodovalorparao IDestánainvocaçãodométodo
responsávelpelainserção.Entretanto,ocorretoéqueessevalorsejagerado
nométodoquerealizaráainserçãoefetiva,métodoestequefazpartedaclasse
Repository.Busqueimplementarestatécnica.
Najanelaqueéexibida,comoocontrolequerepresentao Idestáde-
sabilitado,elenãorecebeofoco,sendopossívelinformarapenasosvalo-
resde Nomee CNPJparaofornecedor. Informe-osecliquenobotão
Gravar.Nestemomento,umnovoobjetofoiinseridoàcole ção,entretanto,
nãohácomovisualizaressesdados.Paraisso,éprecisoatribuiracole çãoao
DataGridView.Vejaqueapresentoumanovaversãoparaométododesta
resoluçãonasequência.
Resolução4.15:métodoparaocliquedobotãoGravarcomatuali-
zaçãodoDataGridView(Versão2)
private void btnGravar_Click ( object sender, EventArgs e) {
var fornecedor = this .controller.Insert(
new Fornecedor () {
Id = Guid.NewGuid(),
Nome = txtNome.Text,
CNPJ = txtCNPJ.Text
}
);
txtID.Text = fornecedor.Id.ToString();
dgvFornecedores.DataSource = null ;
dgvFornecedores.DataSource = this .controller.GetAll();
}
Aocontráriodoapresentadoemexemplosanteriores,nosquaisacole ção
atribuídaao DataSourcedo DataGridVieweraum BindingList,neste
134

## Página 151

CasadoCódigo Capítulo4. Váriosprojetosemumasolução:aplicandoalgunsconceitos...
exemploprevaleceoretornodométodo GetAll(),queéum IList.Isso
tornatantoocontroladorquantoorepositóriomaisindependentes.
Casosejadeinteresse(ounecessidadedacamadadeapresenta ção),a
transformaçãodesseretornoparaum BindingListésimples,bastaape-
nasinstanciaraclassepassandooretornode GetAll()comoparâmetro
paraoconstrutor.Pelofatodeacole çãoatribuídaao DataSourcenãocau-
saraatualiza çãoimediatadoscontrolesemqueelaestáligada,paraquecada
fornecedorinseridonacole çãopossaaparecerno DataGridView,torna-se
necessárioatribuirnullao DataSourcee,emseguida,ànovacole çãode
dados,comosefosseum resetdedadosnocontrole.
Nesteexemplo,agera çãodovalorparao IDestánainvocaçãodométodo
responsávelpelainserção.Entretanto,ocorretoéqueessevalorsejagerado
nométodoquerealizaráainserçãoefetiva,métodoestequefazpartedaclasse
Repository.Busqueimplementarestatécnica.
Apósainser çãodosdadosnacole çãoeaexibi çãoatualizadadelano
DataGridView,osdadosinformadostambémcontinuamaparecendonos
controlesemqueforaminformados.Nestemomento,casoousuáriodeseje
informarumnovofornecedor,éimportantequeoscontrolesestejamsemda-
dos. Aseguir,apresentoaimplementa çãodométodoquecapturaoevento
Clickdobotão Novo.
Resolução4.16:métodoparaocliquedobotãoNovo(Versão1)
private void BtnNovo_Click ( object sender, EventArgs e) {
txtID.Text = string .Empty;
txtNome.Text = string .Empty;
txtCNPJ.Text = string .Empty;
}
Opróximopassoépermitirqueousuárioalteredadosjáinformadose
armazenadosnacole ção.Amaneiraadotadaéqueoregistro(linha)selecio-
nadono DataGridViewteráosdadosatualizadosnos TextBoxs,permi-
tindo,assim,suaaltera ção.Comoo DataGridViewestáconfiguradopara
selecionaralinhainteirapormeiodocliquedomouse,éimportanteiden-
tificarqualeventodevesercapturado. Paraestecaso,oeventoescolhidoé
135

## Página 152

4.7. Criandoacamadadeapresenta ção CasadoCódigo
o SelectionChanged.Nasequência,háaimplementa çãodométodoque
capturaoeventoidentificado.
Resolução4.17:métodoquecapturaoeventoSelectionChangeddo
DataGridView
private void dgvFornecedores_SelectionChanged (
object sender, EventArgs e) {
txtID.Text = dgvFornecedores.CurrentRow.Cells[ 0 ].
Value.ToString();
txtNome.Text = dgvFornecedores.CurrentRow.Cells[ 1 ].
Value.ToString();
txtCNPJ.Text = dgvFornecedores.CurrentRow.Cells[ 2 ].
Value.ToString()
}
Comaimplementa çãodestemétodo,oscontroles TextBoxsserãosem-
preatualizadosquandoocorreragrava çãodosdadostambém,enãoapenas
quandoousuárioselecionarumanovalinhado DataGridView.Sendoas-
sim,éimportanteque,aoinserirumnovofornecedornacole ção,oscontroles
sejam“limpos”equeoDataGridViewnãotenhanenhumalinhaselecio-
nada. Paraisso,adapteométodoquecapturaocliquedobotão Gravar.
Mostroessaimplementa çãoaseguir.
Resolução4.18:métodoquecapturaoeventoClickdobotãoGra-
var(Versão3)
private void btnGravar_Click ( object sender, EventArgs e) {
var fornecedor = this .controller.Insert(
new Fornecedor () {
Id = Guid.NewGuid(),
Nome = txtNome.Text,
CNPJ = txtCNPJ.Text
}
);
dgvFornecedores.DataSource = null ;
dgvFornecedores.DataSource = this .controller.GetAll();
ClearControls();
}
136

## Página 153

CasadoCódigo Capítulo4. Váriosprojetosemumasolução:aplicandoalgunsconceitos...
Verifica-senanovaversãoparaestemétodoqueainstru çãoresponsável
pelaatribui çãodo Idaorespectivo TextBoxfoiretirada,equefoiinserida
umachamadaaumnovométodo,nomeado ClearControls(),apresen-
tadoaseguir.
Resolução4.19:métodoparalimpezadecontrolesdoformulário
private void ClearControls () {
dgvFornecedores.ClearSelection();
txtID.Text = string .Empty;
txtNome.Text = string .Empty;
txtCNPJ.Text = string .Empty;
txtNome.Focus();
}
Aprimeiralinhadestenovométodofazcomquenãoexistanenhuma
linha selecionada noDataGridView. Com isso, caso o usuário clique
emqualquerlinha,oeventodisparadopermitiráaatualiza çãocorretados
TextBoxs,umavezque,semprequeháaliga çãodocontrolecomumafonte
dedadospormeiodo DataSource,oprimeiroregistroémarcadocomo
selecionadono DataGridView.Astrêsinstru çõesseguintessãoasmesmas
implementadasnométodoquecapturaoevento Clickdobotão Novo.O
métodoterminaatribuindoofocodaaplica çãoaoprimeirocontroleeditável
doformulário,onomedofornecedor.
Ométodo ClearSelection()retiraqualquersele çãoexistenteemli-
nhasdo DataGridView.Estaopera çãoéinteressante,umavezque,quando
umalinhaforselecionada,osdadosdela(registro/objeto)sãoexibidosnos
controlesdeintera ção.
Épossíveltrazerparaométodo ClearControls()asinstru çõesde
atualizaçãodo DataGridViewquefazempartedométodo Clickdobo-
tão Gravar.Casotentedepuraraaplica ção,acompanhandoométodoque
capturaoevento SelectionChanged,serápossívelverificarque,acadaal-
teraçãonocontrole,essemétodoéinvocado.Issoporqueacadamudan ça,o
eventoédisparado.
Comestanovaimplementa ção,ométodoquecapturaoevento Click
dobotão Novotambémprecisaseralterado. Estepodeservisualizadona
137

## Página 154

4.7. Criandoacamadadeapresenta ção CasadoCódigo
sequência.Noteque,destamaneira,estásendopropiciadaareutiliza çãode
código,criandoummétodoespecíficoparaumaatividaderequeridaemdi-
versas“partes”daaplicação.
Resolução4.20:métodoquecapturaoeventoClickdobotãoNovo
(Versão4)
private void BtnNovo_Click ( object sender, EventArgs e) {
ClearControls();
}
Comapossibilidadedealtera çãodosdadosdeumfornecedorjáca-
dastrado,surgeumnovoproblema. Insiraumfornecedor,selecione-ono
DataGridViewecliqueemgravar. Notequeumnovofornecedorfoiin-
seridocomumnovo Id,quandooqueeradesejadoeraapenasaatualiza ção
dosdados,comamanuten çãodo Idoriginal.Paraisso,mudan çasdevemser
realizadasnométodoquecapturao Clickdobotão Gravar.Vejaanova
implementaçãoparaestemétodoaseguir.
Resolução4.21:métodoquecapturaoeventoClickdobotãoGra-
var(Versão4)
private void btnGravar_Click ( object sender, EventArgs e) {
var fornecedor = new Fornecedor() {
Id = (txtID.Text == string .Empty ?
Guid.NewGuid() : new Guid(txtID.Text)),
Nome = txtNome.Text,
CNPJ = txtCNPJ.Text
};
fornecedor = (txtID.Text == string .Empty ?
this .controller.Insert(fornecedor) :
this .controller.Update(fornecedor));
dgvFornecedores.DataSource = null ;
dgvFornecedores.DataSource = this .controller.GetAll();
ClearControls();
}
Ooperadorternáriotemafuncionalidadedevalidarumasimplesinstru-
ção if...else,onde,dadaumacondi ção,retorna-seumvalorpara true
138

## Página 155

CasadoCódigo Capítulo4. Váriosprojetosemumasolução:aplicandoalgunsconceitos...
ou false.Échamadode ternárioporpossuirtrêsoperandosseparadospe-
losoperadores ?e :. Suasintaxeé <condição a ser avaliada> ?
<valor_para_verdadeiro> : <valor_para_falso>.
Observequeofornecedoragoraécriadoforadachamadaaométodo
Insert()eque,apropriedade Idpodeterseuvaloratribuídodeduasma-
neiras:naprimeira,gerandoumnovo,casoo TextBoxdo Idestejavazio;
asegundaéobtendoo Idexistenteno TextBox,queexistiráapenasseum
fornecedorforselecionadono DataGridView.Paraessaatribui ção,foiuti-
lizadoooperadorcondicionalternário,o ?:.Essemesmooperadoréusado
nainvoca çãodométodoquegeraráaopera çãodeinser çãoouatualiza ção.
Paraqueaatualiza çãodofornecedorenviadocomoargumentopossa
efetivamente ocorrer, é preciso sobrescrever os métodosEquals() e
GetHashCode(),poisépormeiodelesqueseidentificaumobjeto,utilizada
pelométodoIndexOf()(ediversosoutrosquerealizambuscasnacole ção),
nadetermina çãodequalobjetodeveserbuscadonacole ção.Aseguir,apre-
sentoanovaimplementa çãoparaaclasse Fornecedor.
Resolução4.22:classeFornecedorcommétodosparaidentidade
deobjetos(Versão3)
using System ;
namespace ModelProject {
public class Fornecedor {
public Guid Id { get ; set ; }
public string Nome { get ; set ; }
public string CNPJ { get ; set ; }
protected bool Equals (Fornecedor other) {
return Id.Equals(other.Id);
}
public override bool Equals ( object obj) {
if (ReferenceEquals( null , obj)) return false ;
if (ReferenceEquals( this , obj)) return true ;
if (obj.GetType() != typeof (Fornecedor))
return false ;
139

## Página 156

4.7. Criandoacamadadeapresenta ção CasadoCódigo
return Equals ((Fornecedor) obj);
}
public override int GetHashCode () {
return
}
}
Nasequência,obotão Removerpossuiráaresponsabilidadederetirar
dacole çãodefornecedoresaquelequeestiveratualmentesendoexibidono
formulário.Paraisso,seráprecisogarantirqueexistaalgumfornecedorcom
dadosexibidosnoformulário,antesdepermitirsuaremo ção.Nasequência,
apresentoométodoquecapturaoevento Clickdobotão Remover.
Resolução4.23:métodoquecapturaoeventoClickdobotãoRe-
mover
private void BtnRemover_Click ( object sender, EventArgs e){
if (txtID.Text == string .Empty) {
MessageBox.Show(
"Selecione o FORNECEDOR a ser removido no GRID" );
}
else {
this .controller.Remove(
new Fornecedor () {
Id = new Guid(txtID.Text)
}
);
dgvFornecedores.DataSource = null ;
dgvFornecedores.DataSource =
this .controller.GetAll();
ClearControls();
}
}
Notequeastrêsúltimaslinhasdométodosãoidênticasàsdoquecaptura
oevento Clickdobotão Gravar(vistonaResolução4.18).Aexce çãoestá
noobjetofornecedorenviadoaométodo Remove(),quepossuiapenaso
140

## Página 157

CasadoCódigo Capítulo4. Váriosprojetosemumasolução:aplicandoalgunsconceitos...
Id.Umavezqueaidentidadedosobjetosestánestapropriedade,asdemais
nãosãonecessárias.
Outraabordagemseriaremoverumfornecedorcombaseapenasno Id,
nãoenviandoumobjeto,massimapenasovalor. Ficaodesafioparaaim-
plementaçãodeummétodoquepossaencapsularasinstru çõescomunsentre
ométodoparagravareremoverou,avaliarseessasinstru çõespodemfazer
partedométodo ClearControls().
Concluindoasfuncionalidadesparaestajanela,aseguirrepresentoomé-
todoquecapturaoevento Clickdobotão Cancelar.
Resolução4.24:métodoquecapturaoeventoClickdobotãoCan-
celar
private void BtnCancelar_Click ( object sender,
EventArgs e) {
ClearControls();
}
4.8 Criando uma janela principal para a apli -
cação e menus para acesso aos formulários
criados
Comacria çãodoformuláriopara Produtos,indicadanofinaldoiteman-
terior,oprojeto ViewProjectpossuirádoisformulários. Apósaimple-
mentaçãodosformuláriosparaasdemaisclassesjáidentificadas,estenúmero
aumentará.
Nãoéconvenientenemparatestesficaralterandooformuláriodeinicia-
lizaçãonaclasse Programacadaexecu ção.Porisso,vamoscriarumformu-
lário,representandoumajanelaprincipalparatodaaaplica ção.Nela,haverá
ummenucomacessoatodasasjanelasexistentesnaaplica ção. Noprojeto
ViewProject,crieumformuláriochamado JanelaPrincipal.
Nestenovoformulário,algumaspropriedadesdevemserconfiguradas,
conformemostradoaseguir.
•Propriedade:Name
141

## Página 158

4.8. Criandoumajanelaprincipalparaaaplica çãoemenusparaacessoaosformulárioscriadosCasadoCódigo
•Valorparaatribuir: FormJanelaPrincipal
•Propriedade:WindowState
•Valorparaatribuir: Maximized
Estapropriedadedefineoestadodajanelanomomentoemqueforexi-
bidapelaprimeiravez.Osvaloressão Maximized,oquefazcomqueajanela
sejaexibidamaximizada; Minimized,queatornaminimizada;e Normal
(padrão),quefazcomqueajanelasejaexibidadamaneiraqueelaédese-
nhada.
•Propriedade:Text
•Valorparaatribuir: Janelaprincipaldaaplica ção
•Propriedade:MaximizeBox
•Valorparaatribuir: False
Pormeiodestapropriedade, define-seseobotãoquemaximizauma
janela(ourestauraseutamanhoinicial)éexibidoounão. Normalmente,
quandoseexibeajanelamaximizada,nãosedesejaqueousuáriomudeseu
tamanho. Destamaneira,écomumquandoapropriedade WindowState
estejaem Maximizedequea MaximizeBoxseja False.
Comajanelacriadaeconfigurada,éprecisoinserirnelaocontroleres-
ponsável pelo menu de acesso aos formulários. Esse controle, chamado
MenuStrip,podeserencontradonacategoria Menus & Toolbars,como
podeserverificadopormeiodafiguraaseguir.
142

## Página 159

CasadoCódigo Capítulo4. Váriosprojetosemumasolução:aplicandoalgunsconceitos...
Fig.4.5:Categoriadecontrolesparamenusebarrasdetarefas
Arrasteocontrole MenuStripparaaáreadedesenhodoformulário,e
seuformuláriodeveráficarsemelhanteaoapresentado:
Fig.4.6:ControleMenuStriparrastadoparaoformulário
Ocontrole MenuStripadicionaumabarrademenusaumformulá-
riodeumaaplica ção Windows Forms.Pormeiodessecontrole,épossível
adicionarumaáreademenuse,então,adicionarmenusoucriarmenusper-
sonalizados,diretamentepormeiodoVisualStudio.
Aprincípio,nãohánecessidadedeconfigura çãoemnenhumaproprie-
143

## Página 160

4.8. Criandoumajanelaprincipalparaaaplica çãoemenusparaacessoaosformulárioscriadosCasadoCódigo
dadedessecontrole.Entretanto,éprecisoinserirasop çõesqueomenuprin-
cipaldajanelaoferecerá.Paraisso,napartecomotexto Type Here,digite
Cadastros.Aorealizaressadigita ção,umnovoespa çotambémcomotexto
Type Hereseráexibidoaoladodireitodomenu Cadastros,digiteRegis-
tros.Seuformuláriodeveestarsemelhanteaoapresentado:
Fig.4.7:Op çõesparaomenuprincipal
Asop çõesdemenu Cadastrose Registrosterãonovasop çõesli-
gadasaelas,poissãovistascomocategorias.Parainserirumaop ção,abaixo
de Cadastros,ondeestáescrito Type Here,bastadigitaradesejada. A
figura4.8apresentaessasop ções:
Fig.4.8:Cria çãodeop çõesparaomenuCadastros
Comosmenusesuasop çõescriados,faz-senecessáriaaimplementa-
çãoparaoacessoaoformuláriodesejado. Assimcomoosbotões,osme-
nuspossuemumevento Click,eénelequedeveserimplementadoocó-
digoqueexibiráajaneladesejadaaousuário. Paracriareacessaromé-
todo responsável pelo menuClickde um menu – que é um controle
ToolStripMenuItem–,pode-serealizarumduplocliquenoitemdesejado,
ou,pormeioda Properties Windowemeventos,acessaroevento Click.
Nasequência,representoométodoquecapturaoevento Clickparaomenu
144

## Página 161

CasadoCódigo Capítulo4. Váriosprojetosemumasolução:aplicandoalgunsconceitos...
Fornecedores.
Resolução4.25:métodoquecapturaoeventoClickdomenuFor-
necedores
private void fornecedorToolStripMenuItem_Click (
object sender, EventArgs e) {
new FormFornecedor ().ShowDialog();
}
Realizeobuildnasolu çãoeexecute-a. Najanelaprincipal,selecioneo
menudecadastrose,emseguida,odofornecedor.Ajanelaquerepresentao
formuláriodefornecedorseráexibida.Fa çaomesmoparaaop çãodemenu
referenteaprodutos.
Ocontrole ToolStripMenuItemrepresentaumaop çãoselecionável,
quepodeserexibidaporum MenuStripou ContextMenuStrip. Pode
servistocomoitensdeummenu.
Comaimplementa çãodaclassequerepresentaajanelaprincipaldaapli-
cação,osformuláriosagoranãosãoexecutadosdiretamente,massiminvoca-
dosporoutroformulário.Destamaneira,épossívelpensaremumainje ção
dedependência. Cadaformuláriocriadopossuiseucontrolador,queéde-
claradoeinstanciadonaprópriaclassedoformulário. Épossívelqueexista
maisdeumformulárioqueprecisedomesmocontrolador,oqueredunda-
riacódigo,possibilitandoinclusiveperdadeperformanceeconcorrênciados
dados.Umavezqueajanelaprincipalseráaresponsávelporinvocartodosos
formulários,oscontroladorespoderiamserdeclaradosnelaeelafornecerao
consumidor(osformulários)oscontroladoresjá“prontos”paraouso.Ase-
guir,apresentoadeclara çãodoscontroladoresnaclasse JanelaPrincipal.
Resolução4.26:declara çãodecontroladoresnoformuláriodaJa-
nelaPrincipal
public partial class FormJanelaPrincipal : Form {
private FornecedorController fornecedorController =
new FornecedorController ();
private ProdutoController produtoController =
new ProdutoController ();
145

## Página 162

4.8. Criandoumajanelaprincipalparaaaplica çãoemenusparaacessoaosformulárioscriadosCasadoCódigo
// Código omitido
}
Comoscontroladoresdefinidos,éprecisoinjetá-losnosformuláriosque
osutilizarão.Nasequência,apresentoonovocódigoparaométodoquecap-
turaoevento Clickdomenude Fornecedores.Éprecisoalterartambém
omenupara Produtos.
Resolução4.27:novaversãoparaométodoquecapturaoevento
ClickdomenudeFornecedores
private void fornecedorToolStripMenuItem_Click (
object sender, EventArgs e) {
new FormFornecedor (fornecedorController).
ShowDialog();
}
Observenachamadaaoconstrutordaclasse FormFornecedoroen-
viodeumargumento,queéocontrolador.Destamaneira,éprecisotambém
alterarocódigodaclasse FormFornecedor. Aseguir,mostroanovaim-
plementação.
Resolução4.28:novaversãoparaaclasseFormFornecedor(Versão
2)
public partial class FormFornecedor : Form {
private FornecedorController controller;
public FormFornecedor (
FornecedorController controller) {
InitializeComponent();
this .controller = controller;
}
// Código omitido
}
Injeçãodedependência (ID–Dependency Injection)éumtermotam-
bémconhecidocomo InversãodeControle (IoC–Invertion of Control). É
146

## Página 163

CasadoCódigo Capítulo4. Váriosprojetosemumasolução:aplicandoalgunsconceitos...
umpadrãodeprojetoquebuscaremoveroforteacoplamentoentrecompo-
nentesquesejamdependentes–comoocontroladoreacamadadeapresen-
tação. AIDpermitefacilitaraconcep çãoeimplementa ção,fazendousode
baixoacoplamentodeobjetosreutilizáveisetestáveis.AIoCtambémforta-
lecearecomenda çãoparaqueocontroledeinstânciadeumadeterminada
classe–comonocasodo controller–sejatratadoexternamente,como
naclasse JanelaPrincipal,enãodentrodaclasseconsumidora,comoa
FormFornecedor.Destamaneira,ocorreainversãodecontrole,pormeio
dainje çãodedependência.
4.9 Associando objetos na implementação da
Nota deEntrada
Para a aplicação de associação entre objetos, será feito uso da
classe NotaEntrada, associada a Fornecedor, e da classe
ProdutoNotaEntrada, associada a NotaEntrada e Produto. A
leitura dessas associações pode ser: uma nota de entrada é emitida por
um fornecedor, ela possui um ou vários produtos comprados e cada produto
comprado refere-se a um produto existente.
Aimplementa çãodainterfacecomousuárioésimples,poisofocoéa
associação.Elaestárepresentadapelafiguraaseguir:
147

## Página 164

4.9. Associandoobjetosnaimplementa çãodaNotadeEntrada CasadoCódigo
Fig.4.9:FormulárioquerepresentaaNotadeEntradadeProdutos
Pormeiodafigura 4.9, verifica-seaexistênciadeduasregiões: uma
para o corpo da nota, representado pela classeNotaEntrada; e ou-
tra para os produtos que compõem cada nota, representado pela classe
ProdutoNotaEntrada.
Napartequecompeteaocorpodanota,verifica-seaexistênciadeum
dadoreferenteao Fornecedor,enadosprodutoscomprados,verifica-se
tambémaexistênciadeumdadoreferenteao Produto.Abaixodessescam-
posqueterãoosdadosinformados,existemdoisgrids:umparaasnotasregis-
tradaseumparaosprodutosregistradosparacadanota,aparecendosempre
osquepertencemànotaselecionada.
Osdadosreferentesao Fornecedoreaos Produtosserãoregistra-
dos por meio de controlesComboBox, que estão na categoriaCommon
Controlse,inicialmente,nãoprecisamdenenhumaconfigura ção. Esses
controlesarmazenamumacole çãodedados–objetos,nestecaso–epermi-
temousuárioselecionarumdeles.Essacole çãodedados,nocaso Produtos
e Fornecedores,deveráestardisponívelnomomentoemqueousuáriovi-
sualizarajaneladenotasdeentrada.Destamaneira,oformuláriodenotade
148

## Página 165

CasadoCódigo Capítulo4. Váriosprojetosemumasolução:aplicandoalgunsconceitos...
entradadeveráreceberoscontroladoresdeprodutosefornecedores,paraen-
tãofornecerosrespectivosdadosaos ComboBoxs.
A princípio, configure nos ComboBoxs apenas a propriedade
DropDownStyle para DropDownList, para evitar que o usuário di-
gitevaloresnalista. Os DateTimePickers,paraasdatasdeemissãoe
entrada,têmapenasapropriedade Formatconfiguradapara Short. Os
demais componentes são todos já conhecidos e utilizados em exemplos
anteriores.Nasequência,apresentoocódigoinicialdaclassequerepresenta
o FormNotaEntrada.
Resolução4.29:declara çãodecontroladoresparaaclasseForm-
NotaEntrada
public partial class FormNotaEntrada : Form {
private NotaEntradaController controller;
private FornecedorController fornecedorController;
private ProdutoController produtoController;
private NotaEntrada notaAtual;
public FormNotaEntrada (
NotaEntradaController controller,
FornecedorController
fornecedorController,
ProdutoController produtoController) {
InitializeComponent();
this .controller = controller;
this .fornecedorController =
fornecedorController;
this .produtoController = produtoController;
InicializaComboBoxs();
}
// Código omitido
}
O ComboBoxéumcontrolequepossuiumalistasuspensacomitensque
podemserselecionados.Essalistapodeserexibidaouocultadapormeiode
umaintera çãocomousuário,normalmentecomocliquedomousesobrea
149

## Página 166

4.9. Associandoobjetosnaimplementa çãodaNotadeEntrada CasadoCódigo
setaexistentenocontrole. Peloteclado,ocontroleprecisaestarcomofoco
e,então,pressiona-seacombina çãodatecladeespa çoesetaparabaixo.Sua
aparênciapodeserconfiguradapormeiodapropriedade DropDownStyle,
eositensdalistasuspensasãoarmazenadoserecuperadosnapropriedade
Items.
Com exceção à última linha do construtor, todo o código é facil-
mente interpretado. Inicialmente, declaram-se os controladores, depois
oscamposaseremutilizadose, emseguida, oconstrutorqueregistraos
controladores e chama o método (última linha do construtor) responsá-
vel por inicializar osComboBoxsde Fornecedorese Produtos, o
InicializaComboBoxs().Esteéexibidonasequência.
Resolução4.30:métodoresponsávelpelainicializa çãodosCom-
boBoxs
private void InicializaComboBoxs () {
cbxFornecedor.Items.Clear();
cbxProduto.Items.Clear();
foreach (Fornecedor fornecedor in
this .fornecedorController.GetAll()) {
cbxFornecedor.Items.Add(fornecedor);
}
foreach (Produto produto in
this .produtoController.GetAll()) {
cbxProduto.Items.Add(produto);
}
}
Ométodo InicializaComboBoxs(),inicialmente, limpaoconteúdo
dos ComboBoxsedepoisos“popula”,pormeiodosmétodosGetAll()de
seuscontroladores.Notequeapropriedade Itemséumacole çãocomum
métodoAdd(),querecebeosobjetos Fornecedorese Produtos,recu-
perados.Paratestar,éprecisoinserirumaop çãonomenu Registrospara
acessaranotadeentrada.Crieessaop ção,comoexibidopormeiodafigura
aseguir:
150

## Página 167

CasadoCódigo Capítulo4. Váriosprojetosemumasolução:aplicandoalgunsconceitos...
Fig.4.10:Op çãodemenuparaCompraregistradanomenuRegistros
Nasequência,apresentoocódigoparaqueajaneladecomprasejainvo-
cada.
Resolução4.31:métodoquecapturaoeventoClickdaop çãoCom-
pradoMenuRegistros
private void compraToolStripMenuItem_Click ( object sender,
EventArgs e) {
new FormNotaEntrada (notaEntradaController,
fornecedorController, produtoController).
ShowDialog();
}
Paratestaraimplementa çãorealizadaatéestemomento, executesua
aplicação,acesseosformuláriosdefornecedoreseprodutos,registrealguns
itense,então,acesseoformuláriodecomprasecliqueno ComboBoxde
Fornecedorou Produto.Afigura4.11apresentaajanelacomo ComboBox
de Fornecedorexibindoosfornecedoresregistrados.
Fig.4.11:ComboBoxexibindofornecedorespreviamenteregistrados
151

## Página 168

4.10. ImplementandoainteraçãodousuáriocomoregistrodoCorpodaNotadeCompraCasadoCódigo
4.10 Implementando a interação do usuário
com o registro do Corpo daNota deCom-
pra
Com o formulário todo “desenhado”, é preciso implementar os compor-
tamentosparacadabotão. Inicialmente, osbotõesqueserãoimplemen-
tados referem-se ao corpo da nota, ou seja, os dados referentes à classe
NotaEntrada.Aseguir,apresentoocódigoimplementadoparaométodo
queimplementaobotão Novo,danotadeentrada.
Resolução4.32:métodoquecapturaoeventoClickdobotãoNovo
docorpodaNota
private void BtnNovoNota_Click ( object sender,
EventArgs e) {
ClearControlsNota();
}
Ométodo ClearControlsNota()temomesmoobjetivodométodo
ClearControls(),apresentadonacria çãodoformuláriodefornecedores.
Mostro,aseguir,suaimplementa ção.
Resolução4.33:métodoquerealizaaprepara çãodoscontrolesdo
corpodanotaparaumanovainser çãodedados
private void ClearControlsNota () {
dgvNotasEntrada.ClearSelection();
dgvProdutos.ClearSelection();
txtIDNotaEntrada.Text = string .Empty;
cbxFornecedor.SelectedIndex = - 1 ;
txtNumero.Text = string .Empty;
dtpEmissao.Value = DateTime.Now;
dtpEntrada.Value = DateTime.Now;
cbxFornecedor.Focus();
}
Nessecódigo,existeumpontoqueaindanãofoiapresentado,queéa
atribuiçãodevaloràpropriedade SelectedIndexdo ComboBoxdefor-
152

## Página 169

CasadoCódigo Capítulo4. Váriosprojetosemumasolução:aplicandoalgunsconceitos...
necedores.Atribuindoovalor -1àela,assume-sequenãoéparaapresentar
nenhumitemcomoselecionado,oqueéinteressanteemumprocessodein-
serção,noqualousuárioobrigatoriamenteprecisaráescolherumitem,no
caso,umfornecedor.
Asegundaimplementa çãoaserapresentadaparaocorpodanotadeen-
tradarefere-seobotão Gravar,quetemseucódigomostradonasequência.
Resolução4.34:métodoquecapturaoeventoClickdobotãoGra-
vardocorpodanotadeentrada
private void btnGravar_Click ( object sender, System.
EventArgs e) {
var notaEntrada = new NotaEntrada() {
Id = (txtIDNotaEntrada.Text ==
string .Empty ? Guid.NewGuid() :
new Guid (txtIDNotaEntrada.Text)),
DataEmissao = dtpEmissao.Value,
DataEntrada = dtpEntrada.Value,
FornecedorNota = (Fornecedor) cbxFornecedor.
SelectedItem,
Numero = txtNumero.Text
};
notaEntrada = (txtIDNotaEntrada.Text ==
string .Empty ? this .controller.Insert(
notaEntrada) : this .controller.Update(
notaEntrada));
dgvNotasEntrada.DataSource = null ;
dgvNotasEntrada.DataSource = this .controller.
GetAll();
ClearControlsNota();
}
Aprimeirainstru çãodocomportamentoparaométodoapresentadofaz
referênciaaométodoInsert()–queseráapresentadonaResolução4.35
–docontroladorespecíficoparaaclasseNotaEntradaeseurespectivofor-
mulário.Tambémparaocasodeanotaestarsendoalteradaenãoinserida,o
métodoUpdate()daResolução4.36 éinvocado,quandonecessário.
153

## Página 170

4.10. ImplementandoainteraçãodousuáriocomoregistrodoCorpodaNotadeCompraCasadoCódigo
Outranovainstru çãoéachamadaàpropriedade SelectedItemdo
ComboBox,queretornaoobjetoatualmenteselecionado,nestecaso,ofor-
necedorselecionadoparaanotadecompraaserregistrada. Aofinal, o
método GetAll()–daResolução4.37 –tambémdocontroladorparaa
notadeentradaéinvocado.Paraacria çãodaclassecontroladoraparanota
deentrada,sigaasorienta çõesfornecidasparaaimplementa çãodaclasse
FornecedorController.
Apropriedade SelectedItemdo ComboBoxpermiteatribuirerecu-
peraroitem(objeto)atualmenteselecionado.Casooobjetosejaatribuídoe
eleexistanalistadeitensdisponíveis,háumaatualiza çãonovalordaproprie-
dade SelectedIndex,querecebeovalordoíndiceondeoobjetoatribuído
seencontradentrodositensdisponíveis.
Resolução4.35:métodoInsert()daclasseNotaEntradaController
public NotaEntrada Insert (NotaEntrada notaEntrada) {
return this .repository.InsertNotaEntrada
(notaEntrada);
}
Resolução4.36:métodoUpdate()daclasseNotaEntradaControl-
ler
public NotaEntrada Update (NotaEntrada notaEntrada) {
return this .repository.UpdateNotaEntrada(
notaEntrada);
}
Resolução4.37:métodoGetAll()daclasseNotaEntradaController
public IList<NotaEntrada> GetAll() {
return this .repository.GetAllNotasEntrada();
}
Como pode ser verificado nasResoluções4.35 , 4.36e aqui, elas fa-
zem referências a métodos de um repositório, que é declarado de ma-
neira semelhante ao realizado na classeFornecedorController. As
154

## Página 171

CasadoCódigo Capítulo4. Váriosprojetosemumasolução:aplicandoalgunsconceitos...
Resoluções4.38 , 4.39e4.40 exibem a implementação, respectivamente,
dos métodos InsertNotaEntrada(), UpdateNotaEntrada() e
GetAllNotasEntrada(),declaradosnaclasse Repository.
Resolução4.38:métodoInsertNotaEntrada()daclasseRepository
public NotaEntrada InsertNotaEntrada (
NotaEntrada notaEntrada) {
this .notasEntrada.Add(notaEntrada);
return notaEntrada;
}
Resolução4.39:métodoUpdateNotaEntrada()daclasseReposi-
tory
public NotaEntrada UpdateNotaEntrada (
NotaEntrada notaEntrada) {
this .notasEntrada[ this .notasEntrada.
IndexOf(notaEntrada)] = notaEntrada;
return notaEntrada;
}
Resolução4.40:métodoGetAllNotasEntrada()daclasseReposi-
tory
public IList<NotaEntrada> GetAllNotasEntrada() {
return this .notasEntrada;
}
Ométodo InsertNotaEntrada()–tantonorepositórioquantono
controlador–retornamumobjeto NotaEntradae,aoverificarocódigo,
nãosevêomotivoparaisso. Entretanto,estatécnicaéimportante,poisna
camadadepersistência(Repository)deveocorreraatribui çãodo IDpara
cadaobjetopersistido(armazenado),oquenãoocorrenaaplica çãoapresen-
tada.Porém,prevendoessanecessidade,osmétodosjátêmesseretornoem
suasassinaturas.
Aterceiraimplementa çãoparaocorpodanotadeentradarefere-seao
botão Cancelar,quetemseucódigoapresentadonasequência.
155

## Página 172

4.10. ImplementandoainteraçãodousuáriocomoregistrodoCorpodaNotadeCompraCasadoCódigo
Resolução4.41:métodoquecapturaoeventoClickdobotãoCan-
celardocorpodanota
private void BtnCancelarNota_Click ( object sender,
EventArgs e) {
ClearControlsNota();
}
Aqui,verifica-sequeocomportamentoparaessebotãoéomesmoque
oimplementadoparaobotão Novo. Aquartaimplementação,mostradaa
seguir,refere-seaocomportamentoparaocliquenobotão Removerdanota.
Resolução4.42:métodoquecapturaoeventoClickdobotãoRe-
moverdocorpodanota
private void BtnRemoverNota_Click ( object sender,
EventArgs e) {
if (txtIDNotaEntrada.Text == string .Empty) {
MessageBox.Show(
"Selecione a NOTA a ser removida no GRID" );
}
else {
this .controller.Remove(
new NotaEntrada () {
Id = new Guid(txtIDNotaEntrada.Text)
}
);
dgvNotasEntrada.DataSource = null ;
dgvNotasEntrada.DataSource =
this .controller.GetAll();
ClearControlsNota();
}
}
Paraqueumanotasejaremovida,éprecisoqueseusdadosestejamexibi-
dosparaquevalideasuaexistência.Estaverifica çãoérealizadapormeioda
existênciadeumvalorparao IDdanota,queégeradoquandoelaégravada
pelaprimeiravez.Naimplementa çãodométodo,épossívelidentificaressa
156

## Página 173

CasadoCódigo Capítulo4. Váriosprojetosemumasolução:aplicandoalgunsconceitos...
avaliaçãoque,casosejaconfirmada,invocaométodo Remove()docontro-
lador.Oobjetoenviadoparaométodo,querepresentaumanotadeentrada,
recebeuapenaso ID,poisaidentidadedoobjeto(métodos Equals()e
GetHashCode())baseia-senessecampo.
Aimplementa çãodométodo Remove()podeserverificadanasequên-
cia.
Resolução4.43:métodoRemove()daclasseNotaEntradaControl-
ler
public void Remove (NotaEntrada notaEntrada) {
notaEntrada.RemoverTodosProdutos();
this .repository.RemoveNotaEntrada(notaEntrada);
}
Semelhanteaosdemaismétodosimplementadosnaclassecontroladora,
o métodoRemove(), que recebe a nota de entrada, invoca o método
RemoveNotaEntrada(),implementadonaclasse Repositoryequeé
apresentandoaseguir. Porém,antesdestachamada,ocorreainvoca çãoao
métodoRemoverTodosProdutos(),queretiradanotadeentradatodos
osprodutosregistradosnela.Éprecisoestaratentoparaocasodeocorrência
dealgumerronaexecu çãodométododo Repository,poisquandoanota
forrealmenteremovidadacole ção,seusprodutosjánãoexistirãomais.
Resolução4.44:métodoRemove()daclasseNotaEntradaControl-
ler
public void RemoveNotaEntrada (NotaEntrada notaEntrada) {
this .notasEntrada.Remove(notaEntrada);
}
Aúltimaimplementa çãoreferenteàintera çãocomosdadosqueperten-
cemaocorpodanotaéapresentadanasequência. Elaserefereaoevento
SelectionChangeddo DataGridViewqueexibeasnotasdeentradasre-
gistradas.
157

## Página 174

4.10. ImplementandoainteraçãodousuáriocomoregistrodoCorpodaNotadeCompraCasadoCódigo
Resolução4.45:métodoSelectionChanged()doDataGridViewde
NotasdeEntrada
private void dgvNotasEntrada_SelectionChanged (
object sender, EventArgs e) {
try {
this .notaAtual = this .controller.
GetNotaEntradaById((Guid) dgvNotasEntrada.
CurrentRow.Cells[ 0 ].Value);
txtIDNotaEntrada.Text = notaAtual.Id.
ToString();
txtNumero.Text = notaAtual.Numero;
cbxFornecedor.SelectedItem = notaAtual.
FornecedorNota;
dtpEmissao.Value = notaAtual.DataEmissao;
dtpEntrada.Value = notaAtual.DataEntrada;
UpdateProdutosGrid();
}
catch (Exception exception) {
this .notaAtual = new NotaEntrada();
}
}
Ométodoimplementadoestádentrodeumbloco try...catch().
Estatécnicafoiusada,poisométodoéchamadoaqualqueraltera çãodees-
tadodafontededadose,emcasodeinexistênciadedados,umaexce çãopode
ocorrer.
O método que realiza a busca pelo registro selecionado no
DataGridView é o GetNotaEntradaById(), implementado no
controlador–vistoaseguir. Esteretornaanotaencontrada,queéarmaze-
nada,eentãotemsuaspropriedadesutilizadasparapopularoscontrolesdo
formulário.Comocadanotapossuiumconjuntodeprodutosarmazenados,
ométodo UpdateProdutosGrid()–Resolução4.48 –éinvocadopara
atualizaro DataGridViewdeprodutos.
Resolução4.46:métodoGetNotaEntradaById()daclasseNotaEn-
tradaController
158

## Página 175

CasadoCódigo Capítulo4. Váriosprojetosemumasolução:aplicandoalgunsconceitos...
public NotaEntrada GetNotaEntradaById (Guid Id) {
return this .repository.GetNotaEntradaById(Id);
}
Nasequência,mostroométodo GetNotaEntradaById()daclasse
Repository.
Resolução4.47:métodoGetNotaEntradaById()daclasseReposi-
tory
public NotaEntrada GetNotaEntradaById (Guid Id) {
var notaEntrada = this .notasEntrada[
this .notasEntrada.IndexOf(
new NotaEntrada () {Id = Id}
)];
return notaEntrada;
}
Abuscapelanotadeentradaquepossuao Idenviadoparaométodose
dápormeiodométodo IndexOf()dacole ção,oquepodevariardeacordo
comacole çãoaserescolhida.
OmétodoIndexOf()fazumapesquisanacole çãodeobjetosàprocura
deumitemquecorrespondaaoenviadocomoargumento. Encontrando-o,
éretornadooíndicedesseelemento,tendocomobaseocomportamentode
umamatriz.
Resolução4.48:métodoUpdateProdutosGrid()
private void UpdateProdutosGrid () {
dgvProdutos.DataSource = null ;
if ( this .notaAtual.Produtos.Count > 0 ) {
dgvProdutos.DataSource = this .notaAtual.
Produtos;
}
}
159

## Página 176

4.11. ImplementandoainteraçãodousuáriocomoregistrodosprodutosdaNotadeCompraCasadoCódigo
4.11 Implementando a interação do usuário
com o registro dos produtos da Nota de
Compra
Algunscuidadosdevemserprevistosnessainterfacecriada.Umdeleséqueo
usuárionãopoderáregistrarumprodutosenãoexistirumanotaregistradae
selecionada.Paraisso,todososcontrolesquepermitemintera çãodevemestar
desabilitados,eserapenashabilitadosquandoumnovoregistroforsolicitado
eorequisitodeumanotadeentradaexistireforcumprido.
Altere para False a propriedade Enabled dos controles:
cbxProduto, txtCusto, txtQuantidade, btnGravarProduto,
btnCancelarProdutoe btnRemoverProduto.Osnomesapresentados
sãoautoexplicativosparaidentificaraqualcontrolesereferem.
Casoaindanãotenhanomeadooscontroles,fa ça-oagora.Ocontrolede
IDserásempredesabilitado,poisnãopermiteintera ção.Ahabilita çãodesses
controlessedaránomomentoemqueousuárioclicarnobotão Novopro-
duto,desdequeavalida çãosejabemsucedida.Aseguir,apresentoocódigo
paraométodoquecapturaoevento Clickdobotão Novo produto.
Resolução4.49:métodoquecapturaoeventoClickdobotãopara
umnovoproduto
private void BtnNovoProduto_Click ( object sender,
EventArgs e) {
ClearControlsProduto();
if (txtIDNotaEntrada.Text == string .Empty) {
MessageBox.Show( "Selecione a NOTA, que terá " +
"inserção de produtos, no GRID" );
}
else {
ChangeStatusOfControls( true );
}
}
Verifica-sequeacontradi çãoàexpressãoavaliada(o else)causaacha-
madaaummétodoemespecífico,o ChangeStatusOfControls(),man-
160

## Página 177

CasadoCódigo Capítulo4. Váriosprojetosemumasolução:aplicandoalgunsconceitos...
dandocomoargumentoovalorbooleano true. Aimplementaçãodesse
métodopodeserverificadanasequência.
Resolução4.50:métodoresponsávelpelahabilita çãoedesabilita-
çãodecontrolesreferentesaosprodutosdanota
private void ChangeStatusOfControls ( bool newStatus) {
cbxProduto.Enabled = newStatus;
txtCusto.Enabled = newStatus;
txtQuantidade.Enabled = newStatus;
BtnNovoProduto.Enabled = !newStatus;
BtnGravarProduto.Enabled = newStatus;
BtnCancelarProduto.Enabled = newStatus;
BtnRemoverProduto.Enabled = newStatus;
}
Comousuárioclicandonobotão Novoparainserirumproduto,oscon-
trolessãotodoshabilitadoseobotão Novotorna-seinativo.Comainterface
liberadaparaousuárioinformarosdados,elepodeoptarem Gravarsua
digitaçãoou Cancelarqualquerinforma çãodigitadanoscontroles.Ase-
guir,apresentoaimplementa çãoparaométodoquecapturaoevento Click
dobotão Gravar produto.
Resolução4.51:métodoquecapturaoeventoClickdobotãoGra-
varproduto
private void BtnGravarProduto_Click ( object sender,
EventArgs e) {
var produtoNota = new ProdutoNotaEntrada() {
Id = (txtIDProduto.Text == string .Empty ?
Guid.NewGuid() : new Guid(txtIDProduto.
Text)),
PrecoCustoCompra = Convert.ToDouble(
txtCusto.Text),
ProdutoNota = (Produto) cbxProduto.
SelectedItem,
QuantidadeComprada = Convert.ToDouble(
txtQuantidade.Text)
};
161

## Página 178

4.11. ImplementandoainteraçãodousuáriocomoregistrodosprodutosdaNotadeCompraCasadoCódigo
this .notaAtual.RegistrarProduto(produtoNota);
this .notaAtual = this .controller.Update(
this .notaAtual);
ChangeStatusOfControls( false );
UpdateProdutosGrid();
ClearControlsProduto();
}
A primeira instrução a ser discutida é a chamada ao método
RegistrarProduto(),pertencenteaoobjeto notaAtual,quepodeser
verificadonasequência.
Resolução4.52:métodoRegistrarProduto()daclasseFormNota-
Entrada
public void RegistrarProduto (ProdutoNotaEntrada produto) {
if ( this .Produtos.Contains(produto))
this .Produtos.Remove(produto);
this .Produtos.Add(produto);
}
Ométodo RegistrarProduto()inicialmentebuscapeloprodutore-
cebidoe,casoelejáexistanacole ção,eleéremovidoeonovoinserido.Esta
técnicaéutilizadaparaconhecimentodemeioseusosdemétodosdisponí-
veispelacole çãoadotada. Épossívelevitarestasitua çãoescolhendooutras
coleçõescommaisrecursosjáimplementados.
OmétodoCancelar edição/inserção de produtostemsuaim-
plementaçãoapresentadaaseguir.
Resolução4.53:MétodoquecapturaoeventoClickdobotãoCan-
celaredi ção/inser çãodeproduto
private void BtnCancelarProduto_Click ( object sender,
EventArgs e) {
ClearControlsProduto();
ChangeStatusOfControls( false );
}
162

## Página 179

CasadoCódigo Capítulo4. Váriosprojetosemumasolução:aplicandoalgunsconceitos...
Oúltimobotão, Removerproduto,temseucomportamentonométodo
representadoadiante.
Resolução4.53:métodoquecapturaoeventoClickdobotãoCan-
celaredi ção/inser çãodeproduto
private void BtnRemoverProduto_Click ( object sender,
EventArgs e) {
this .notaAtual.RemoverProduto(
new ProdutoNotaEntrada () {
Id = new Guid(txtIDProduto.Text)
}
);
this .controller.Update( this .notaAtual);
UpdateProdutosGrid();
ClearControlsProduto();
ChangeStatusOfControls( false );
}
Notequearemo çãodoprodutodanotasefazexatamentepelaretirada
deledacole çãodeprodutose,emseguida,ométodo Update()docontro-
ladoréinvocadoparaatualizaranota.
4.12 Conclusão
Estecapítulobuscouapresentartécnicasparaassociarobjetos,criandouma
aplicaçãocomdiversosprojetoseaplicandooconceitodeMVCcomumre-
positóriobaseadoemcole ções. Duranteodesenvolvimentodoprojetode
exemplo,diversasobserva çõesetécnicasforamapresentadasediscorridas.
Aofinal,obteve-seumaaplica çãocomasopera çõesCRUD( Create, Retri-
eve, Update and Delete)paraumconjuntodedados master-detail.Aospou-
cos,oarcabou çodeferramentasetécnicasdedesenvolvimento,recursosda
linguagemeambienta çãoaoIDEvemaumentando.Comoacessoabancode
dados,nopróximocapítulojáserápossívelodesenvolvimentodeaplica ções
realmentefuncionaisecondizentescomasnecessidadesdeumaempresa.
163

## Página 181

Capítulo5
Acessoadadospormeiodo
ADO.NET
Todaaplica çãodesenvolvidamanipulaeprocessadados.Essesdadospodem
sertransientes–informadosdiretamentenaaplica çãoeimediatamentepro-
cessados–,podemserobtidosdefontesexternas–comoumarquivotexto–
ouaindaregistradosemumacole çãoedepoisarmazenadosemumarquivo.
Entretanto,omeiomaiscomumparapersistênciaeobten çãodedadoséo
usodeSistemasGerenciadoresdeBasedeDados(SGBD),noqualtabelas
sãocriadaspararecebere/oufornecerdadosda/paraaplica ção. Estecapí-
tuloapresentaousodoADO.NETpararealiza çãodestaatividade,ondeos
exemplosdemonstrarãooqueesseframeworkoferece.
Inicialmente,serátrabalhadoapenascomcódigo,paraconhecimentoda
API( Application Program Interface),edepoisserãotambémapresentadosre-

## Página 182

5.1. IntroduçãoaoADO.NET CasadoCódigo
cursosoferecidospelaplataformaeoVisualStudio. Procurefazerusodas
técnicasapresentadasnoscapítulosanterioresemrela çãoàformata çãovisual
eàtécnicadediversosprojetosemumasolu ção,aplicandooMVC.
5.1 Introdução ao ADO.NET
OADO.NETéumconjuntodeclasses(API)quepossibilitaoacessoeama-
nipulaçãodediversostiposdefontesdedados( data sources)paraprograma-
doresdo.NETFramework.Normalmente,umafontededadoséumabasede
dados,esuastabelassãovisõese stored procedures,mastambémpodemser
umarquivodetexto,umaplanilhadoExcel,umarquivoXMLouaindaum
web service.
Emrela çãoàsbasesdedados,quesãoofocodestecapítulo,acomunica-
çãocomosSGBDsépossívelcomqualquerumdosmaisutilizados,como:
SQLServer–queéousadonolivro–,MySQL,Firebird,Oracleetc.
OscomponentesconsideradoscomoospilaresdoADO.NETincluemos
objetos:
a) Connection,responsávelporefetuaraconexãocomobancodedados;
b) Command,responsávelporexecutarcomandosdiretamentenobancode
dados;
c) DataAdapter,utilizadoparapreencherumobjeto DataSet.
Essestrêsitenssãoconhecidoscomo .NETFrameworkDataProvider
e,alémdeles,o DataSettambéméumapartefundamental. Todosesses
componentesserãoapresentadosetrabalhados.
Émuitocomumumaconfusãoentreostermos bancodedados ebase
dedados. Emalgunscasos,quemlê(ouescreve)nemsedeparacomessa
diferença,maséextremamenteimportantequevocêasaiba.Quandoseusa
otermo“bancodedados”,busca-sereferenciarosoftware,oprodutocomo
qualaaplica çãoseconectará.Jáotermo“basededados”refere-seaoproduto
fornecidopelosBancosdeDados,ouseja,osregistrosnelesarmazenados,
quersejamestesprocessadosounão.
166

## Página 183

CasadoCódigo Capítulo5. AcessoadadospormeiodoADO.NET
5.2 Criando a base de dados utilizando oVisual
Studio
ParaqueosrecursosdoADO.NETpossamserapresentados,exemplificadose
aplicados,faz-senecessárioumabasededados.Inicialmente,amanipula ção
dessabaseparacria çãodetabelasserárealizadapormeiodoVisualStudio.
Paraisso,crieumanovasolu ção,enelaumprojeto Windows Forms.Nesse
projeto,crieumapastachamada App_Data.
Afiguraaseguirapresentaa Solution Explorerobtida:
Fig.5.1:Selecionandoprojetoparaterreferênciaadicionada
Cliquecomobotãodireitodomousenanovapastacriada( App_Data)
eselecionenomenuaop ção Add  New Item. Najanelaqueseexibe,
selecioneacategoria Datae, dentrodela, otemplate Service-based
Database.Dêonome ADO_NETDataBase.mdfaoarquivodebasededa-
dosqueserácriado.Vejaafigura:
167

## Página 184

5.2. CriandoabasededadosutilizandooVisualStudio CasadoCódigo
Fig.5.2:Criandoabasededados
Um Service-base Databaseéumarquivoquerepresentaumabase
dedados.Énessearquivoqueestarãoosobjetoscriadoseusadospelaapli-
cação,como:tabelas, indexes, constraints, stored procedures, functionsetc.
Apósconfirmaracria çãodabasededados,casooerroapresentadopela
figura5.3apare ça,énecessárioqueoservi çoquerepresentaoSQLServerseja
iniciado.
Fig.5.3:ErroreferenteaoSQLServernãoestariniciadonacria çãodabasede
dados
Parainiciaroservi çodoSQLServer,acesseos Serviços Locais do
Windows. Lá,localizeoservi ço,cliquecomobotãodireitosobreeleena
opção Iniciar.Casoessaop çãoestejadesabilitada,éporquenacria çãoda
basededadosesseprocedimentoestavaemandamentoenãohaviaconcluído,
bastandorepetiroprocedimentojáexplicadoparaacria çãodoarquivo.Veja
nafiguraaseguiroservi çosendoiniciado:
168

## Página 185

CasadoCódigo Capítulo5. AcessoadadospormeiodoADO.NET
Fig.5.4:Iniciandooservi çolocaldoSQLServer
Apósacria çãoterocorridocomsucesso,oarquivocriadoéexibidona
Solution Explorer,comopodeserverificadonafigura:
Fig.5.5:SolutionExplorercomoarquivodebasededadoscriado
Comabasededadoscriada,éprecisoagorafazerastabelasqueavão
compor.Paraessaprimeiraatividade,seguindooexemplodocapítuloante-
rior,serácriadainicialmenteatabelareferenteaosfornecedores. Paraisso,
acessea Server Explorer(menu View  Server Explorer),como
mostraafigura 5.6. Se,aoexpandironó Data Connections,aconexão
comabasecriadaaparecercomumíconeemvermelho,significaqueelanão
foiaberta.Assim,bastaexpandironódabasededadosparaaconexãoser
169

## Página 186

5.2. CriandoabasededadosutilizandooVisualStudio CasadoCódigo
estabelecidaeexibirascategoriasdeobjetosdisponíveis.
Fig.5.6:ServerExplorerexibindoabasededadoscriada
Comascategoriasdepossíveisobjetosparaabasededados,épreciso
criaratabelaqueconteráeforneceráosdadosreferentesaosfornecedores.
Paraisso,cliquecomobotãodireitodomousesobre Tablesedepoisna
opção Add New Table:
170

## Página 187

CasadoCódigo Capítulo5. AcessoadadospormeiodoADO.NET
Fig.5.7:Adicionandoumatabelaàbasededados
Caso o menu de contexto exibido em sua máquina seja diferente
do apresentado na figura 5.7, aparecendo apenas as opções Refresh e
Properties,aferramenta SQLServerDataTools (SSDT)nãoestáinsta-
ladaemseuambiente.NoVisualStudio2013,elaéinstaladaautomaticamente
comoIDE.Mas,semesmoassimasop çõesnãoaparecerem,algumerroocor-
reuduranteainstala çãoeelaprecisaserrealizadanovamente.ParaoVisual
Studio2012,éprecisobuscarodownloaddessaferramenta.
OSSDTéumaferramentaquepermitequeacria çãoemanipula çãode
umabasededadospossaserrealizadadiretamentenoVisualStudio,sema
necessidadedeumaferramentaseparada,comoo SQLServerManagement
Studio.
Apósaconfirma çãodeadi çãodeumanovatabela,umajanelaoferecida
peloSSDTéexibida. Épormeiodelaqueatabelapoderásercriadatanto
visualmentecomopormeiodeinstru çõesSQL:
171

## Página 188

5.2. CriandoabasededadosutilizandooVisualStudio CasadoCódigo
Fig.5.8: Ambienteparadefini çãodeestruturadetabelaspormeiodoSQL
ServerDataToolsnoVisualStudio
Nocontextoapresentadonestelivro,emrela çãoaosbancosdedadosre-
lacionais,uma tabela(table)podeserdefinidacomoumconjuntodedados
dispostosemumnúmerofinitodecolunas(campos)eilimitadodelinhas
(registrosoutuplas).
Ascolunassãoconsideradascomo camposnatabela.Elascaracterizam
osdadosquecomporãoainforma çãoesperadaporcadalinha/registroou
tupla.Cadacolunapossuiumtipodedadoespecífico.
Aslinhas(registrosoutuplas)podemtrazertodasasinforma çõesar-
mazenadasemumatabela,comtodososcamposoualgunsdeles.Épossível
tambémquetabelassejamcombinadaspararetornaremregistrosquegerem
informaçãocomposta.Porexemplo,emumaúnicalinha,épossívelterdados
dasquatrotabelasqueserãoprocessadasnestecapítulo:fornecedor,produto,
notasdecompraedadosdecadaprodutocomprado. Aformadereferen-
ciarinequivocamenteumaúnicalinhaépormeiodautiliza çãodeumachave
primária.
Osregistrosdeumatabela,namaioriadasvezes,nãopodemseridên-
ticos. Paraesterequisitosergarantido,éprecisoqueatabelatenhasofrido
umprocessode normalização.Estetemaéextensoefogedosobjetivosdeste
172

## Página 189

CasadoCódigo Capítulo5. AcessoadadospormeiodoADO.NET
livro.Destamaneira,parasimplificar,éadotadooconceitode chaveprimá-
ria(ouprimarykey)ede identidade(ouautoincremento),emqueovalor
paraachaveprimáriaécriadoautomaticamenteenãofazpartedosdomínios
naturaisdecadatabela.
Ascolunas(campos)databelapodemserinformadastantonaáreade
desenho,ondeapareceumgridcomadefini çãopredefinidapara Id–que
seráachaveprimáriaparaatabela–,quantonaparteondeapareceocódigo
SQL.Nestapartedocódigo,mudeonomedatabelapara Fornecedorese,
napartevisual,selecionealinhadacoluna Id.Emseguida,ativeajanelade
propriedades,pressionandoatecla F4.Altereapropriedadedeconfigura ção
dacolunacomoidentidade.Oresultadopodeservistonafigura:
Fig.5.9:EstruturaparaatabelaFornecedores
SQL(Structured Query Language–LinguagemdeConsultaEstruturada)
éalinguagemparabancodedadosrelacional.Muitasdascaracterísticasori-
ginaisdoSQLforaminspiradasnaálgebrarelacional.Porserumassuntoque
porsisómereceumlivro,essetemanãoserádetalhadoalémdonecessário
nestelivro.
QuandosetrabalhacomSGBDs,umconjuntodecódigosestádisponí-
vel,sejaparadefini çãodabasededados,comoparaobten çãodedadose
informaçõesdessasbasesdedados.Ainstru çãoSQL CREATE TABLEéuma
instruçãoparadefini çãodabasededados,uma DDL(Data Definition Lan-
guage).
173

## Página 190

5.2. CriandoabasededadosutilizandooVisualStudio CasadoCódigo
Comadefini çãodaestruturapronta,éprecisoconfirmaracria çãodata-
bela. Paraisso,notopodajanela,cliquenobotão Update. Essaoperação
seráresponsávelporapresentarasopera çõesqueserãorealizadasnaatuali-
zaçãodabasededados:
Fig.5.10:Janeladepré-atualiza çãodabasededados
Pararealizaraatualiza çãodabasededados,cliquenobotão Update
Database. Setudoocorrerbem,aofinaldoprocessamento,aconsoledo
Data Tools Operationexibiráoresultadomostradonafiguraaseguir:
Fig.5.11:ConsoledoDataToolsOperationapósaatualiza çãodabasededados
Paraverificaratabelacriadano Server Explorer,pressioneobotão
174

## Página 191

CasadoCódigo Capítulo5. AcessoadadospormeiodoADO.NET
de Refresh.Elapoderáservisualizada,deacordocomafigura 5.12.
Fig.5.12:ServerExplorerexibindoanovatabelacriadaesuascolunas/campos
5.3 Realizando operações relacionadas ao
CRUD em uma tabela de dados
Inicialmente,oformulárioparaintera çãocomousuário,paraamanuten ção
dosdadosdefornecedores,serásemelhanteaotrabalhadonocapítulo 4:
175

## Página 192

5.3. RealizandooperaçõesrelacionadasaoCRUDemumatabeladedados CasadoCódigo
Fig.5.13:Formulárioparamanuten çãonosdadosdeFornecedores
Apósodesenhodoformulário,éprecisoforneceràaplica çãoinforma ções
paraqueelapossaacessaroarquivodebasededadoscriado.Estaconfigu-
raçãodeveserfeitanoarquivo App.Config,naraiz( root)doprojeto. O
nomeparaessaconfigura çãodeacessoaumabasededadosé Connection
String. Aseguir,tragoocódigonecessárioparaaconfigura çãodeuma
stringdeconexãocomoarquivodebasededadoscriadoanteriormente.
Resolução5.1:connectionStringparaconexãocomobancocriado
<?xml version= "1.0" encoding= "utf-8" ?>
<configuration>
<startup>
<supportedRuntime version= "v4.0"
sku= ".NETFramework,Version=v4.5" />
</startup>
<connectionStrings>
< add name= "CS_ADO_NET"
connectionString= "Data Source=(LocalDB)\v11.0;
AttachDbFilename=C:\Users\Everton\Dropbox\
Livros\Windows Forms\Capítulo 05 \SolutionADO_NET
\ADO_NETProject01\App_Data\ADO_NETDatabase.mdf;
176

## Página 193

CasadoCódigo Capítulo5. AcessoadadospormeiodoADO.NET
Integrated Security=True "
providerName= "System.Data.SqlClient" />
</connectionStrings>
</configuration>
Todaaconfigura çãonecessáriaparaumaaplica ção Windows Forms
podeserrealizadanoarquivo App.Config,alémdeusarimplementa ções
emC #,quepossamconfiguraraaplica çãotambémemtempodeexecu ção.
Aconfigura çãoapresentadaestá(edevesersempre)combaseemXML.O
elementomaisexternovisualizadoéo <configuration>,eaconfigura-
çãodeuma connectionStringdeveserrealizadadentrodesseelemento,
pormeiodeelementos <connectionString>.
Nocontextotrabalhadonestelivro,queéoacessoadados,uma connec-
tion string (oustringdeconexão)éumastringqueespecificainforma ções
sobreumafontededadosecomoacessá-la. Elapassa,pormeiodecódigo,
informaçõesparaum driverou providersobreoqueénecessáriopara
iniciarumaconexão. Normalmente,aconexãoéparaumabasededados,
mastambémpodeserusadaparaumaplanilhaeletrônicaouumarquivode
texto,dentreoutros. Umaconnectionstringpodeteratributoscomonome
dodriver,servidorebasededados,alémdeinforma çõesdeseguran ça,como
nomedeusuárioesenha.
Dentrodoelemento <connectionString>,háumelemento <add>,
queadicionaaocontextodaaplica çãoumanovaconnectionstring,ealguns
atributossãodefinidos:
a) name define o nome para a conexão a ser adicionada, neste caso
CS_ADO_NET;
b) connectionStringéumatributocomplexo,onde:
•Data Sourceéoservidorondeobancodedadosestáe,nestecaso,
éapontadoo Local Data Base. Ovalor (LocalDB)\v11.0
refere-seaocaminhonoqualoservidorlocaldebancodedadosestá
instaladoque, porpadrão, é C:\Program Files\Microsoft
SQL Server`\LocalDB\Binn.
177

## Página 194

5.3. RealizandooperaçõesrelacionadasaoCRUDemumatabeladedados CasadoCódigo
•AttachDbFileNamerefere-se,paraobancodedadoslocal,aoca-
minhofísicoparaoarquivoquerepresentaabasededados. Para
obterocaminhofísicodoarquivodebasededados,éprecisosele-
cionaroarquivona Solution Explorere,então,najanelade
propriedades,obterovalorde Full Path(figura5.14).
•Integrated Securitydefinecomoaautentica çãoseráutilizada
naconexão.Quandorecebe True,assume-seaautentica çãodosis-
temaoperacional(Windows,nocaso). Jáseovaloratribuídofor
False,seránecessárioinformaronúmerodeusuárioesenha.
c) providerNameforneceparaaconexãoonomedo Data Provider
responsávelporrealizaraconexãocomabasededados.
Fig.5.14:Obtendoocaminhofísicodoarquivodebasededados
Aescritadeuma connection stringpodevariardeacordocomomodo
deacessoaobancodedadosetambémcomobancodedados.Paraauxiliar
nestaatividade,cadaprodutoofereceinforma çãodecomocriarumastringde
conexão,precisandoapenasrecorreràdocumenta çãodisponibilizada.Bus-
candominimizaradificuldade,existeumsitequeéreferêncianoassunto,o
http://www.connectionstrings.com,quefornecetutoriais,dicaseartigosre-
levantes.
178

## Página 195

CasadoCódigo Capítulo5. AcessoadadospormeiodoADO.NET
5.4 Inserindo registros na tabela de fornece -
dores
Comoapresentadoanteriormente,relacionadoaodesenhodajanela,nacon-
figuraçãoparaconexãocomabasededados,jásetemonecessárioparaa
primeiraopera çãorelacionadaaumCRUD,queéainser çãodeumnovore-
gistro.
Crieummétodoparaoevento Clickdobotão Gravar,realizando
umduplocliquesobreobotão.Vocêpodetambémfazerissoselecionandoo
botãoe,na Properties Viewem Events,selecionaro Clickedarum
duplocliquenaáreaembranco,aoladodeseunome.
Implementenocorpodométodoocódigoapresentadonasequência.
Resolução5.2:métodoqueimplementaoeventoClickdobotão
Gravar(Versão1)
private void btnGravar_Click ( object sender, EventArgs e) {
string connectionString = ConfigurationManager.
ConnectionStrings[ "CS_ADO_NET" ].ConnectionString;
SqlConnection connection = new SqlConnection(
connectionString);
connection.Open();
SqlCommand command = connection.CreateCommand();
command.CommandText = "insert into FORNECEDORES(nome,
cnpj) values(@nome, @cnpj) ";
command.Parameters.AddWithValue( "@nome" , txtNome.Text);
command.Parameters.AddWithValue( "@cnpj" , txtCNPJ.Text);
command.ExecuteNonQuery();
connection.Close();
MessageBox.Show( "Fornecedor registrado com sucesso" );
}
Épossívelverificarnaprimeiralinhadométodoadeclara çãoeinicia-
lizaçãodeumavariáveldotipo string,quereceberáaconnectionstring
definida como CS_ADO_NET no App.Config. A obtenção desse va-
lorérealizadapormeiodapropriedade ConnectionStrings,daclasse
ConfigurationManager.Notequeonomedaconnectionstringéinserido
179

## Página 196

5.4. Inserindoregistrosnatabeladefornecedores CasadoCódigo
como stringdentrodoscolchetese,apóseles,éinformadaapropriedade
ConnectionString.
Aclasse ConfigurationManagerpermiteoacessopormeiodecó-
digo,emtempodeexecu ção,aoarquivodeconfigura ção( App.Config)
e suas seções. Uma de suas funcionalidades é o acesso rápido às se-
ções <appSettings> e <connectionStrings>. A propriedade
ConnectionStringsforneceosdadosdase ção <connectionStrings>
doarquivodeconfigura çãodaaplica ção.
Casoaclasse ConfigurationManagerapareçacomodesconhecida
(ouinexistente)emseucódigo,adicioneaoblocode namespaces,noinício
doarquivo,acláusula using System.Configuration.Semesmoassim
oproblemapersistir,éprecisoadicionaraoseuprojetooacessoao Assembly
dessaclasse.Paraisso,na Solution Explorer,cliquecomobotãodireito
domousesobre Referencesedepoisem Add Reference. Najanela
queéexibida,noladoesquerdocliquenacategoria Frameworkenoquadro
centralprocurepor System.Configuration 4.0.0.0.Então,marquea
caixadesele ção,paraqueoarquivosejaadicionadoaseuprojeto:
180

## Página 197

CasadoCódigo Capítulo5. AcessoadadospormeiodoADO.NET
Fig.5.15:Adicionandoumassemblyàsreferênciasdoprojeto
Asegundainstru çãoimplementadanométodorefere-seàcria çãodoob-
jetoresponsávelpelaconexãocomobancoSQLServer,queéumobjetoda
classe SqlConnection.Nachamadaaoconstrutordaclasse,emsuainstan-
ciação,éenviadaumastring,queéaconnectionstringanteriormenterecupe-
rada.Apósoobjetotersidoinstanciado,ainstru çãoseguinteabreaconexão,
pormeiodométodo Open().
Aclasse SqlConnectionéutilizadaparagerenciarconexõescombases
dedadosdoSQLServer. Pormeiodeobjetosdessaclasse,asconexõessão
abertasefechadas,epermitemacria çãodeobjetosquerepresentamcoman-
dos/instruçõesaseremexecutadosnabasededados.Elaforneceumgrande
númeroderecursosque,conformeforemsendousados,serãoapresentados.
Comaconexãocomabasededadosestabelecida,éprecisocriarumob-
jetoquepossibiliteaexecu çãodeinstru çõesnabasededados.Essesobjetos
sãodaclasse SqlCommandesãoobtidosdeacordocomainstru çãodaquarta
linhadaimplementa çãonométodo.
Aclasse SqlCommandéresponsávelporexecutarinstru çõesSQLem
181

## Página 198

5.4. Inserindoregistrosnatabeladefornecedores CasadoCódigo
bancosdedadosSQLServer,podendoserusadatantoparaconsultascomo
parainstru ções“nãoquery”,comoupdates, insertseexecu çãode procedures.
Dentreasdiversaspropriedadesoferecidaspelaclasse,asutilizadasna
implementaçãosão:
•CommandText,querepresentaainstru çãoSQLaserexecutada,como
um select, update, insertouonomedeum stored procedure
existente;
•Parameters,queéumacole çãodeobjetosdotipo SqlParameter
e,assimcomoamaioriadascole ções,possuimétodoscomo Add()e
Remove(),dentreoutros.
Os parâmetros dessa lista devem corresponder àqueles definidos no
CommandText (identificados por @ antes do nome). Os objetos
SqlParameterpossuemdiversosmétodostambém.Umdeles,queéusado
naimplementa ção,éo AddWithValue(),cujousoérecomendadoemvez
deseutilizarapenaso Add().
Retornandoàclasse SqlCommand,elatambémpossuimétodos. Den-
treeles,háo ExecuteNonQuery(),responsávelporexecutarasinstru ções
deatualiza çãodedados,comonocasoo insert. Essemétodoretornao
númerodelinhasquesofreramatualiza çõespelasuaexecu ção.
Asinstru çõesSQL,comoo insertapresentado,fazempartedacatego-
riaDML(Data Manipulation Language).Essasinstru çõesretornamdados(
select)eosatualizam( insert, updatee delete).
Finalizandoaimplementa çãodométodo,existeachamadaaométodo
Close()doobjeto SqlConnectioneumaexibi çãoaousuáriodeuma
mensagemreferenteaosucessodaopera ção.
Damesmamaneiraque,noexemplodocapítulo 4naResolução4.19(se-
ção4.7),oscamposeramlimpos,éprecisofazeromesmoapósainser çãodo
fornecedornatabela. Sigaoexemploapresentadonestaparteparaimple-
mentaressafuncionalidade.AbraumanovainstânciadoVisualStudiocom
asolu çãoabertaparalheauxiliar,pois,alémdessaimplementa ção,outrasjá
realizadasserãoapontadas.
182

## Página 199

CasadoCódigo Capítulo5. AcessoadadospormeiodoADO.NET
5.5 Obtendo todos os fornecedores existentes
na base de dados
Para obter todos os fornecedores existentes na tabela e popular o
DataGridViewcomestesdados,éprecisorealizarumaconsultanatabela
dabasededados.Estaérealizadapormeiodainstru çãoSQL select.
Aocontráriodorealizadonaimplementa çãodainser çãodeumregistro
queestáatreladaaummétodoquecapturaumevento,essanovaimplementa-
çãoserárealizadaemummétodoespecífico,seguindoapropostadestelivro,
decrescimentodoconhecimentoacadaimplementa çãoapresentada.
Resolução5.3:métodoresponsávelporobtertodososfornecedores
registradosnatabeladedados(Versão1)
private void GetAllFornecedores () {
string connectionString = ConfigurationManager.
ConnectionStrings[ "CS_ADO_NET" ].ConnectionString;
var connection = new SqlConnection(connection);
var adapter = new SqlDataAdapter( "select id, cnpj, nome
from FORNECEDORES ", connectionString);
var builder = new SqlCommandBuilder(adapter);
var table = new DataTable();
adapter.Fill(table);
dgvFornecedores.DataSource = table;
connection.Close();
}
Naimplementa çãodométodo GetAllFornecedores(),repete-sea
declaraçãoda connectionStringdaobten çãoeencerramentodaconexão
comoSQLServer,oquejádevelevaraumareflexãoderefatora çãodosdois
métodosjáimplementados,buscandoumareutiliza ção.
Nadeclara çãodasvariáveis adapter, buildere tablejáfoiutilizada
amaneiramaisatualdedeclara çãodevariáveis,comovistoemcapítulosante-
riores.Notequeaconexãonãofoiabertademaneiraexplícita,poisométodo
183

## Página 200

5.5. Obtendotodososfornecedoresexistentesnabasededados CasadoCódigo
Fill()do adaptertemcomoumadesuasatividadesaaberturadacone-
xãoneleregistrada.
Oprocessoparaasele çãodosdadossedápormeiodacria çãodeum
adapter,quepossuiainstru çãoSQLaserexecutadanoservidoreaco-
nexãocominforma çõesdabasededadosondeelaseráexecutada. Com
o adaptercriado,éprecisogeraros commandsparaasinstru çõesSQL
informadas nele. Diferentemente do apresentado na inserção dos regis-
tros,ondefoiusadaaclasse SqlCommand,essaimplementa çãousaaclasse
SqlCommandBuilder,quegerao SqlCommandcombasenastringSQL
enviadaemseuconstrutor.
Nasequência,um tableécriadoe,então,preenchidocomosdados
obtidospormeiodaexecu çãodométodo Fill()do adapter,querecebea
tablequeserápreenchida.Finalizando,o DataGridViewrecebea table
jápopuladaeaconexãoé,então,fechada.
Aclasse SqlDataAdapterrepresentauma“ponte”entreabasededados
eo DataTable(ou DataSet).Ométodo Fill()usadonaimplementa-
çãoexcutaainstru çãoSQL selecteutilizaoseuretornoparapopularo
DataTableenviadocomoparâmetro,alémdetambémrealizaraabertura
desuaconexão.
Aclasse SqlCommandBuildergera Commandsparaseremutilizados
porum SqlDataAdapter.
Aclasse DataTablerepresenta,demaneiralógica,umatabela. Esta
podeserumatabelafísica–existenteemumabasededados–,ouapenasuma
tabelacriadaeutilizadaemtempodeexecu ção.Aclasseoferecediversaspro-
priedadesemétodosquepodemserusadosdeacordocomasnecessidades.
Paravisualizarnainterfacecomousuárioaexecu çãodessemétodo,é
precisorealizaralgumasaltera ções.Aprimeiraénoconstrutor,paraque,ao
exibiroformulário,osfornecedoresregistradosjápossamservisualizados.
Asegundaénométodonoqualérealizadaainser çãodosdadosinformados
pelousuário,najanelademanuten çãoemdadosdefornecedores.Vejaambas
resoluçõesnasequência.
Resolução5.4:métodoresponsávelporobtertodososfornecedo-
resregistradosnatabeladedados(Versão1)
184

## Página 201

CasadoCódigo Capítulo5. AcessoadadospormeiodoADO.NET
public FornecedoresCRUD () {
InitializeComponent();
GetAllFornecedores();
}
Resolução5.5:métodoqueimplementaoeventoClickdobotão
Gravar(Versão2)
private void btnGravar_Click ( object sender, EventArgs e) {
using ( var connection = new SqlConnection(
this .connectionString)) {
connection.Open();
SqlCommand command = connection.CreateCommand();
command.CommandText = "insert into FORNECEDORES(
nome, cnpj) values(@nome, @cnpj) ";
command.Parameters.AddWithValue( "@nome" ,
txtNome.Text);
command.Parameters.AddWithValue( "@cnpj" ,
txtCNPJ.Text);
command.ExecuteNonQuery();
}
MessageBox.Show( "Fornecedor registrado com sucesso" );
ClearControls();
GetAllFornecedores();
}
Aprimeiraaltera çãoquepodesernotadaéaretiradadadefini çãoda
variávelconnectionString,quenãofazmaispartedométodo,massim
daclasse( Resolução5.6). Asegundaaltera çãorefere-seaousodainstru-
ção usingnadeclara çãoeinicializa çãodavariável connection. Estaé
amaneiramaiscorretadeseimplementarquandoseutilizaderecursosque
precisamserfechadoseliberados.
NaVersão1da Resolução5.5,nãohaviasidoinseridaachamadaaomé-
todo Dispose()de connectionapósachamadaaométodo Close().
Essachamadaserianecessáriacasonãofosseusadoo using.Tambémnão
haviasidoinseridaachamadaaométodo ClearControls(),quetema
mesmafinalidadedométododemesmonomeutilizadonocapítulo 4eque
podeservisualizadona Resolução5.7.
185

## Página 202

5.6. Obtendoumfornecedorespecíficonabasededados CasadoCódigo
Finalizando, a última instrução realiza a chamada ao método
GetAllFornecedores(), apresentado anteriormente na Resolução
5.3.
Resolução5.6:declara çõesdemembrosdaclasse(Versão1)
public partial class FornecedoresCRUD : Form {
private string connectionString = ConfigurationManager.
ConnectionStrings[ "CS_ADO_NET" ].ConnectionString;
//Código complementar omitido
Resolução5.7:métodoClearControls()(Versão1)
private void ClearControls () {
txtID.Text = string .Empty;
txtNome.Text = string .Empty;
txtCNPJ.Text = string .Empty;
txtNome.Focus();
}
Quando se utiliza um objeto que encapsula qualquer recurso, é pre-
cisogarantirquequandonãoprecisarmosmaisdesseobjetoseumétodo
Dispose()sejainvocado.Estaatividadepodesermaisfacilmenterealizada
comainstru ção using(using statement).
Ainstru ção usingsimplificaocódigoquecria,finalizaelimpaoobjeto.
Elaobtémorecursoespecificado,executaasinstru çõesefinalmenteinvocao
métodoDispose()doobjeto,paralimpá-lo.
5.6 Obtendo um fornecedor específico na base
de dados
Paraquesejapossívelaousuárioalterarosdadosdeumfornecedor,ouainda
removê-losdabasededados,épreciso–nestaaplica çãoexemplo–queele
sejaselecionadono DataGridViewetenhaseusdadosexibidos.Paraque
osdadosdofornecedorselecionadopossamserexibidos,éprecisoqueofor-
186

## Página 203

CasadoCódigo Capítulo5. AcessoadadospormeiodoADO.NET
necedortenhasidobuscadonatabelae,então,umobjetoqueorepresente
sejapopulado,paraassimfornecerosdadosparaoscomponentesvisuais.
Aclassequerepresentaráumregistrodatabeladefornecedorespodeser
visualizadanasequência,queésemelhanteàclassedemesmonomeimple-
mentadanocapítulo4,mudandoapenasotipodedadodapropriedade Id,
de Guidpara long.
Resolução5.8:classequemapeiaatabelaFornecedoresparaobje-
tos
public class Fornecedor {
public long Id { get ; set ; }
public string Nome { get ; set ; }
public string CNPJ { get ; set ; }
//Código complementar omitido
}
Demaneirasimplificada,o MapeamentoObjetoRelacional(ORM–Ob-
ject Relation Mapping)consistenaexistênciadeumaclassequetenhaemsuas
propriedadesoscamposexistentesemumatabela,ouocontráriodisso:que
umatabelapossuacamposquepossamreceberosvaloresdaspropriedades
deumobjeto.Existemdiversasferramentasqueautomatizamestaatividade,
adicionandopoderososrecursos. AMicrosoftofereceo EntityFramework
(EF),queéapresentadonocapítulo 8.
Nasimplementa çõesanteriores,aconexãoeraobtidademaneiradireta,
oquenãoécorreto.Éimportanterefor çarquecadaclassedevepossuiruma
únicaresponsabilidade,equecadamétododestaclasserealizeumaúnicaati-
vidadetambém.Aclasseondeoscódigosimplementadosestãoéumaclasse
controladora,querecebeedelegaintera çõesnainterfacecomousuário.
Noquedizrespeitoàconexãocomobanco,apresento,aseguir,umanova
classecriada.
Resolução5.9:classequeimplementaopadrãodeprojeto(Design
Pattern)Singletonparafornecerumaconexãocomobancode
dados
187

## Página 204

5.6. Obtendoumfornecedorespecíficonabasededados CasadoCódigo
public sealed class DBConnection {
private static volatile SqlConnection instance;
private DBConnection () { }
public static SqlConnection DB_Connection {
get {
if (instance == null ) {
instance = new SqlConnection(
ConfigurationManager.ConnectionStrings[
"CS_ADO_NET" ].ConnectionString);
}
return instance;
}
}
}
Ousodapalavrareservada sealednadefini çãodeumaclassegarante
queelanãosejaestendida.Ouseja,nenhumaclassepodetê-lacomoclasse
ancestral.Ousonaclassesedáaofatodeelaserespecíficaparaseracessada
damaneiraqueé,semnecessitardeespecializa ções.
Aosedefinirumcampodaclasseouummétodocomo static,define-
sequeoelementopertenceàclasse,enãoaumobjetoespecífico.Issosignifica
quenãohánecessidadedeinstanciaraclasseparaacessaromembrodesejado.
Destamaneira,todoobjetotambémtemacessoaomembro,compartilhando
seuestado.
Apalavrareservada volatilenadefini çãodeumcampoinformaque
estepodesermodificadopordiversaspartesdaaplica çãoaomesmotempo.
Ocampo instancedeclaradomanteráneleaconexãoqueseráutili-
zadaportodaaaplica ção.Eleéprivadoeestático,ouseja,pertenceàclasse
eapenasmétodosestáticospodemacessá-lo. Oobjetivoéque,naprimeira
chamadaàpropriedade DB_Connection,estecamporecebaseuvalore,em
novasinvoca ções,ovalorsejaapenasrecuperado.Issodámaioragilidadeà
obtençãodaconexão.
Pelofatodeaclasseimplementaropadrão Singleton,elanãopodeser
instanciada.Destamaneira,seuconstrutorpadrãoprecisaserexplicitamente
188

## Página 205

CasadoCódigo Capítulo5. AcessoadadospormeiodoADO.NET
implementadoeserprivadoàclasse,comopodeserverificadonaimplemen-
tação.
Singletonéumpadrãodeprojetoquegaranteaexistênciadeapenas
umainstânciadeumaclasse,mantendoumpontoglobaldeacessoaoseu
objeto.Naimplementa çãodessaresolu ção,opontoglobaldeacessoéapro-
priedadedeleitura DB_Connection,quefornecerásempreamesmacone-
xãoparaqualquerchamadaaele.Nãofazpartedoescopodolivrodetalhar
padrõesdeprojetosetampoucoafirmarseumpadrãoébomounão. En-
tretanto,éimportantequeoleitorbusqueinforma çõessobreessetema,pois
existemdiversoslivrosqueotrabalham.
A propriedade DB_Connection, que é apenas de leitura, é pública
e estática, pois acessará o campo também estático,instance. Inicial-
mente,verifica-seseocampoénuloe,casoseja,ainstancia çãodaclasse
SqlConnectionocorrerá,enviandoparaseuconstrutorastringdecone-
xãoexistenteno App.Config.
Comaimplementa çãodaclassedenegócio( Fornecedor)edaclasse
paraobten çãodaconexãocomobanco( DBConnection),restaagoraimple-
mentarabuscapelofornecedorqueestiverselecionadono DataGridView,
oqueveremosaseguir.
Resolução5.10: métodoquerecuperaumfornecedornatabela,
combasenoId(Versão1)
private Fornecedor GetFornecedorById ( long id) {
Fornecedor fornecedor = new Fornecedor();
var connection = DBConnection.DB_Connection;
var command = new SqlCommand( "select id, cnpj, nome
from FORNECEDORES where id = @id ", connection);
command.Parameters.AddWithValue( "@id" , id);
connection.Open();
using (SqlDataReader reader=command.ExecuteReader()) {
while (reader.Read()) {
fornecedor.Id = reader.GetInt32( 0 );
fornecedor.CNPJ = reader.GetString( 1 );
fornecedor.Nome = reader.GetString( 2 );
}
189

## Página 206

5.6. Obtendoumfornecedorespecíficonabasededados CasadoCódigo
}
connection.Close();
return fornecedor;
}
Paramapearoregistroquecontémofornecedordesejado,umobjetoda
classe Fornecedorécriado,eseráretornadocomosdadosdoregistroob-
tido.
Éimportanteressaltarque,pelocódigo,ométodosempreretornaráum
objeto,poisapesquisasempreocorrerácombaseemumregistroexistente.
Paraqueométodopossaserusadodemaneiragenérica–naqual,porexem-
plo,ousuáriodigiteum Ideessevalorpossanãoexistirnatabela–,épreciso
queométodoretorne nullquandonãoencontrarumfornecedornatabela.
Procureadaptarométodoparaestasitua ção.
Emrela çãoàconexãoeexecu çãodainstru çãoSQL,amudan çaestána
maneiradeseobteraconexão,queagorafazusodaclasse DBConnection.
Notequenãofoifeitousodainstru ção using,comoapresentadaanteri-
ormenteparaaconexão,poisissocausariaa“destrui ção”doobjetoe,pela
adoçãodo Singleton,issonãoédesejado. Tambémnãofoifeitousodo
SqlDataAdapter,massimdo SqlCommand,quetambémjáfoiutilizado,
poisanecessidadeéderecuperarumdadoparaserusadonocódigo,enão
popularumcontrolediretamente.
Apósaaberturadaconexão,umobjeto SqlDataReaderéusadoem
uma instrução using para receber o resultado retornado pelo método
ExecuteReader()do command,referenteàinstru çãoSQL select.Com
aobten çãodo reader,éprecisorealizaraleituradoconjuntoderegistros
recebidosporele.Estaérealizadapelométodo Read().
NaResolução5.10,aleituraestápresentenoargumentodainstru ção
while(). Nocasodométodoedafuncionalidadeasercumpridaporele,
nãohaverianecessidadedo while(),poisexisteagarantiadeexistênciado
registro,eapenasumregistroseráretornado. Naleituradosdadosdecada
coluna,érealizadaainvoca çãoaummétododotipododadoaserlido,envi-
andocomoparâmetrooíndicedacoluna.Porestanecessidadedeinformar
oíndice,éimportantequeascolunassejaminformadasno selectdains-
truçãoSQL.Apósaleituraeaatribui çãodosvaloresaoobjeto,comosefaz
190

## Página 207

CasadoCódigo Capítulo5. AcessoadadospormeiodoADO.NET
usode using,o readeréautomaticamentefechadoeencerrado.Porfim,
aconexãoétambémfechadaeoobjeto fornecedorretornado.
Aclasse SqlDataReaderfornecerecursosparaleituradeumcon-
juntoderegistrosdeumatabelaSQLServer.Oconjuntoretornadopodeser
lidoapenasemumúnicocaminho,doinícioaofim(tambémchamadode
forward-only). Paraaleituradoconjuntoexistenteemum reader,éfeito
usodométodo Read(),quelêumregistroporvez.
Aleituradecadacolunapodeserfeitapormétodosquerepresentamo
tipodedadodacolunaaserrecuperada.Dessaforma,éenviadoaométodo
ovalorordinaldela,ouaindaonomedacolunacomíndicedeumamatriz,
como,porexemplo: reader[“nomecoluna”].Nestaúltimasintaxe,oretorno
éumobjetoquerepresentaotiponativodacoluna.Apósotrabalhocomo
reader,éimportantefechá-lo(Close())eeliminá-lo( Dispose()),lem-
brandodafacilidadedeutilizaro using,queexecutaissoautomaticamente
aoseutérmino.
Comoométodoparaobterofornecedorselecionadono DataGridView
jáestáimplementado,énecessáriochamá-lo.Paraisso,oeventoCellClick
foiescolhidoeteveseucomportamentoimplementado,conformevemosna
sequência.
Resolução5.11:métodoquecapturaoeventoCellClickdoData-
GridView(Versão1)
private void dgvFornecedores_CellClick ( object sender,
DataGridViewCellEventArgs e) {
if (e.RowIndex < 0 || e.ColumnIndex < 0 )
return ;
this .fornecedorAtual = GetFornecedorById(Convert.
ToInt64(dgvFornecedores.Rows[e.RowIndex].Cells[ 0 ].
Value));
txtID.Text = this .fornecedorAtual.Id.ToString();
txtNome.Text = this .fornecedorAtual.Nome;
txtCNPJ.Text = this .fornecedorAtual.CNPJ;
}
191

## Página 208

5.6. Obtendoumfornecedorespecíficonabasededados CasadoCódigo
Oevento CellClickocorrequandoqualquerpartedeumacélulaécli-
cada,incluindobordaseespa çosembranco,ounomomentoemqueousuá-
riopressionaatecladeespa çoquandoumacélulaéumbotãoouumcheckbox
quetenhafoco;ocorrendoduasvezesparaestestiposdecélulaseelasforem
clicadasenquantosepressionaatecladeespa ço.
Comaimplementa çãodessemétodo,acadacliquedomouseemqual-
quercélulado DataGridView,oregistroreferenteao Iddofornecedorda
linhaquerepresentaacélulaselecionadaserábuscado.Entretanto,ascélulas
querepresentamocabe çalhodelinhasecolunastambémpodemserclica-
dasetêmesteeventocapturado. Poressemotivo,casoodisparodoevento
tenhaocorridoemumadessascélulas,oprocessamentoéinterrompidopela
invocaçãodainstru ção return.Casoacélulasejadeconteúdo,ométodo
GetFornecedorById()éinvocado,recebendoo Iddalinhaselecionada.
Aatribui çãodosdadosobtidospelométodoaoscomponentesdatelaéuma
operaçãojáconhecida.
Oobjeto fornecedorAtualfoiinseridocomocamponaclasse. Veja
nasequência.
Resolução5.12:declara çõesdemembrosdaclasse(Versão2)
public partial class FornecedoresCRUD : Form {
private string connectionString = ConfigurationManager.
ConnectionStrings[ "CS_ADO_NET" ].ConnectionString;
private Fornecedor fornecedorAtual;
//Código complementar omitido
}
Comaimplementa çãodaclasse DBConnection,paraobteraconexão
comobanco,ocampo connectionStringtorna-sedesnecessário.Desta
maneira,adapteosmétodosjáimplementadosparaquefa çamusodanova
classeeremovaadefini çãodocampo.
192

## Página 209

CasadoCódigo Capítulo5. AcessoadadospormeiodoADO.NET
5.7 Removendo da tabela o fornecedor seleci -
onado
Com a possibilidade de selecionar um determinado fornecedor no
DataGridView, agora é possível remover da tabela de fornecedores
umregistroemespecífico. Paraestaimplementa ção,umanovaclassefoi
implementada,a DAL_Fornecedor,queimplementaum Data Access Layer
(DAL),comopodeserverificadoaseguir.
Resolução5.13:classeDAL_Fornecedorcomométodopararemo-
çãodeumfornecedoremespecífico
public class DAL_Fornecedor {
private SqlConnection connection = DBConnection.
DB_Connection;
public void RemoveById ( long id) {
var command = new SqlCommand( "delete from
FORNECEDORES where id = @id ", connection);
command.Parameters.AddWithValue( "@id" , id);
connection.Open();
command.ExecuteNonQuery();
connection.Close();
}
}
Épossívelverificarque,nadefini çãodaclasse,existeumcampoquere-
presentaaconexãoemqueestatrabalhará.Ométodo RemoveById()tem
comonovidadeapenasachamadaaométodo ExecuteNonQuery()do
command,queexecutaráainstru çãoSQL delete.
Um Data Access Layeréumacamadaquerepresentademaneirasimplifi-
cadaoacessoadadosemumarmazenamentopersistente,comoumservidor
debancodedados.
Umanovaaltera çãonadeclara çãoénecessáriaparautilizaraclasseque
representao DAL,oqueveremosaseguir.
193

## Página 210

5.7. Removendodatabelaofornecedorselecionado CasadoCódigo
Resolução5.14:declara çõesdemembrosdaclasse(Versão3)
public partial class FornecedoresCRUD : Form {
private Fornecedor fornecedorAtual;
private DAL_Fornecedor dal = new DAL_Fornecedor();
//Código complementar omitido
}
Paraefetivamenterealizararemo çãodofornecedorselecionadodatabela,
éprecisoimplementarométodoquecapturaoevento Clickdorespectivo
botão,comopodeserverificadonasequência.
Resolução5.15:métodoquecapturaoeventoClickdobotãoRe-
mover(Versão1)
private void BtnRemover_Click ( object sender, EventArgs e) {
if (txtID.Text == string .Empty) {
MessageBox.Show( "Selecione o FORNECEDOR a ser
removido no GRID ");
} else {
this .dal.RemoveById( this .fornecedorAtual.Id);
ClearControls();
MessageBox.Show( "Fornecedor removido com sucesso" );
}
}
Lendo rapidamente todo o código, é possível notar que, na verifica-
çãodeexistênciadeumfornecedorselecionado,foifeitousodocontrole
txtIDe,noenviodovalordo Iddofornecedorselecionadoparaométodo
RemoveById(),foienviadoovalordapropriedade Iddoobjetoquerepre-
sentaofornecedoratualmenteselecionado.Estesdoisusosforamapenaspara
exemplificar;orecomendadoésempreutilizaroobjetoesuapropriedade.
Aoconcluiraremo çãodoregistro,éprecisoqueosregistrosexibidosno
DataGridViewsejamatualizados,poisnãopodeserexibidoaousuárioum
registrojáremovido.
OmétodoClearControls()sofreualtera ções,esuanovaversãopode
servisualizadaaseguir.
194

## Página 211

CasadoCódigo Capítulo5. AcessoadadospormeiodoADO.NET
Resolução5.16:métodoClearControls()(Versão2)
private void ClearControls () {
txtID.Text = string .Empty;
txtNome.Text = string .Empty;
txtCNPJ.Text = string .Empty;
GetAllFornecedores();
dgvFornecedores.ClearSelection();
this .fornecedorAtual = null ;
txtNome.Focus();
}
É possível verificar a inserção de três novas instruções, sendo elas:
GetAllFornecedores(), quedevesairdaimplementa çãodeinser ção;
dgvFornecedores.ClearSelection(),paragarantirquenãoseache
registroselecionadoaolimparoscontroles;e this.fornecedorAtual =
null,quelimpaoobjetoquerepresentaofornecedoratualmenteselecio-
nado.
5.8 Realizando alterações em um fornecedor
já inserido
Aúltimaopera çãodoCRUDaserimplementadoéodeatualiza çãodedados.
Estaatualiza çãorefere-seamudan çasemdadosquejáforaminseridosna
tabela.Seguindoopadrãodocapítulo 4,elaocorrerápormeiodométododo
botão Gravar,omesmousadoparainser ção. Ométodoresponsávelpela
atualizaçãodosdadospodeservistonasequência.
Resolução 5.17: método para atualização de dados na classe
DAL_Fornecedor
private void Update (Fornecedor fornecedor) {
var command = new SqlCommand( "update FORNECEDORES set
cnpj=@cnpj, nome=@nome where id=@id ",
this .connection);
command.Parameters.AddWithValue( "@cnpj" , fornecedor.
CNPJ);
195

## Página 212

5.8. Realizandoalteraçõesemumfornecedorjáinserido CasadoCódigo
command.Parameters.AddWithValue( "@nome" , fornecedor.
Nome);
command.Parameters.AddWithValue( "@id" , fornecedor.Id);
connection.Open();
command.ExecuteNonQuery();
connection.Close();
}
Ométodo Update()daclasse DAL_Fornecedorrecebeoobjetoque
temosdadosatualizadosequeprecisamserpersistidosnatabela.Asinstru-
çõesdométodosãotodasjáconhecidas. Entretanto,épossívelverificarna
definiçãodométodoqueeleestácomoprivado( private),ouseja,aces-
sívelapenaspormétodosdaprópriaclasse. Aseguir,apresentoométodo
chamador.
Resolução5.18: métodoquedelegaaatualiza çãoouinser çãode
registronaclasseDAL_Fornecedor
public void Save (Fornecedor fornecedor) {
if (fornecedor.Id != null )
this .Update(fornecedor);
else {
this .Insert(fornecedor);
}
}
Aclasse DALofereceráumúnicométodoparagravarofornecedorna
tabela,sejaainser çãodeumnovofornecedorouaatualiza çãodedadosde
umjáexistente. Paraidentificarqualopera çãoserárealizada,foiadotadaa
propriedade Idcomo flag.Seessapropriedadenãofornula,éporqueodado
jáfoiinserido,umavezqueocampoquemapeiaessapropriedadeéautoin-
cremento.
Recorde-sequeocampo Id,naclasse Fornecedor,édefinidocomo
longe,estetipodedadoévistocomoprimitivo.Sendoassim,possuiumva-
lor default,queézero,nãoaceitando,assim,umvalornulo.Entretanto,oC #
ofereceumrecursoquepermitequeissoocorra.Esteéexibidonasequência,
queapresentaumanovaversãoparaaclasse Fornecedor.
196

## Página 213

CasadoCódigo Capítulo5. AcessoadadospormeiodoADO.NET
Resolução5.19:classeFornecedorcompropriedadeIdaceitando
valornulo
public class Fornecedor {
public long? Id { get ; set ; }
public string Nome { get ; set ; }
public string CNPJ { get ; set ; }
public Fornecedor () {
this .Id = null ;
}
}
Vejanadefini çãodapropriedade Idque,apósonomedotipodedadoa
queelaserefere,éinformadoosímbolodeinterroga ção.Comestasintaxe,a
propriedadepassaaaceitarvaloresnulos.Tambémfoicriadoumconstrutor
padrãodemaneiraexplícita,paraque,aoinicializarumobjeto,ovalornulo
sejaatribuídoàpropriedade.
Mudançastambémsãonecessáriasnométododegrava çãodofornecedor,
pois,naversãoatual,ainser çãoérealizadanele,eagorafoitransferidapara
oDAL,oqueveremosaseguir.
Resolução5.20:métodoqueimplementaoeventoClickdobotão
Gravar(Versão3)
private void btnGravar_Click ( object sender, EventArgs e) {
dal.Save( new Fornecedor() {
Id = string .IsNullOrEmpty(txtID.Text) ?
( long? ) null : Convert.ToInt64(txtID.Text),
Nome = txtNome.Text,
CNPJ = txtCNPJ.Text
});
MessageBox.Show( "Manutenção realizada com sucesso" );
ClearControls();
}
Verifiquequeométodoagoratemaresponsabilidadedeinstanciarum
objetodaclasse Fornecedoreenviá-loaométodo Save()do DAL().
197

## Página 214

5.9. Implementandoassociaçõesemtabelasdeumabasededados CasadoCódigo
Notequenainicializa çãodapropriedade Idéfeitousodooperadorternário
condicional,ondeéenviado nullcasonãosejaumaaltera ção.Paraefeito
desintaxe,o nulléconvertidoparaotipodedadodapropriedade.
Comamudan çadotipodapropriedade Idpara long?,ométododa
classe DAL RemoveById()precisarádeatualiza çãonotipodedadoque
recebe,paraquesejaomesmodapropriedade,ouseja, long?.Fa çaisso.
Umavezalteradoométododobotão Gravar,ainser çãoprecisaser
transferidaparao DAL,damesmamaneiraqueexisteométodo Update().
Façaisso,lembrandoqueométodoprecisaser private.
Parafinalizaraimplementa çãodajanelaresponsávelpelaintera çãoe
manutençãocomdadosdefornecedores,codifiqueométodoparaoevento
Clickdosbotões Novoe Cancelar,damesmamaneiraquefoifeitono
capítulo4(Resoluções4.20 e4.24dase ção4.7,respectivamente).
5.9 Implementando associações em tabelas de
uma base de dados
Seguindoaindaoexemplodocapítulo 4,éprecisoagoratrazerparaaso-
luçãoaclassequerepresentaanotadeentradadeumacompra,nomeada
NotaEntrada,apresentadanasequência.
Resolução5.21:classeNotaEntrada(Versão1)
public class NotaEntrada {
public long? Id { get ; set ; }
public string Numero { get ; set ; }
public Fornecedor FornecedorNota { get ; set ; }
public DateTime DataEmissao { get ; set ; }
public DateTime DataEntrada { get ; set ; }
public NotaEntrada () {
this .Id = null ;
}
// Código não implementado
}
198

## Página 215

CasadoCódigo Capítulo5. AcessoadadospormeiodoADO.NET
Comparandoaclassedessaresolu çãocomafinal,implementadanoca-
pítulo4(Resolução4.8 dase ção4.5),verifica-seamudan çanotipodedado
do Id,aretirada(nomomento)doatributo Produtoseadefini çãodo
construtorpadrãodemaneiraexplícita.
Comaclassequerepresentaatabelacriada,éprecisoagoracriaratabela.
Sigaospassosapresentadosparaacria çãodatabela Fornecedorespara
criaratabela NotasDeEntrada,comaestruturaigualàapresentadapela
figura:
Fig.5.16:EstruturacriadaesalvaparaatabelaNotasDeEntrada
Verifiquenonomedatabelaqueelajáestácriadanabasededadosjá
atualizada.Paraatualizarabasededadosparaessacria ção,cliquenobotão
Update,logoacimadaestrutura.Noteocampo IdFornecedor,poisépor
meiodelequeaassocia çãodaclasse Fornecedorcom NotaEntradaserá
persistidacomoformade relacionamento.
Quandosemodelaumabasededados,define-seumdiagramachamado
DER(DiagramadeEntidadeseRelacionamentos),noqualsebuscarelacio-
narastabelas–aquinomeadasentidades–quepossuemalgumtipodeliga-
ção.
Quandosetrabalhacomoutraferramentavisual,o MER(ModelodeEn-
tidadeseRelacionamentos),define-seumacolunaqueservirácomochavees-
trangeira( Foreign key),nastabelasqueserãodependentesnorelacionamento
documentado.Estecampotem,inicialmente,afinalidadedeapontarparao
199

## Página 216

5.9. Implementandoassociaçõesemtabelasdeumabasededados CasadoCódigo
registrodatabela–ou“relação”,nestecontexto–primária,donadorelaci-
onamento,oregistroqueéresponsávelpelodadoarmazenadonacolunade
chaveestrangeira.
Destamaneira,estabelece-seumaregra,ondeodadodacolunadechave
estrangeiradeveexistirobrigatoriamentenacolunadechaveprimáriadata-
belaqueoriginaachaveestrangeira,ouseja,cria-seuma constraint.Este
assuntonãoseesgotaaqui,poisévastoemereceumestudodetalhado,oque
estáforadocontextodestelivro.
Umaassocia ção,parasermapeadaparaumatabelaemumabasededa-
dos,precisadeumrelacionamentoentreastabelasenvolvidas. Paracriaro
relacionamentoentreastabelas Fornecedorese NotasDeEntradanos
itensexibidosaoladodaestruturadefinida,cliquecomobotãodireitosobre
Foreign Keyse,então,em Add New Foreign Key:
Fig.5.17:Adicionandoumanovachaveestrangeira
Após confirmar a opção do menu de contexto, uma nova chave
estrangeira é criada, com o nome dela em edição; altere-o para
FK_NotasDeEntrada_ToFornecedor,comovemos:
200

## Página 217

CasadoCódigo Capítulo5. AcessoadadospormeiodoADO.NET
Fig.5.18:Nomeandoachaveestrangeiracriada
Tendocriadoenomeadoachaveestrangeira,éprecisoconfigurá-la.Para
isso,seráprecisoalterarocódigonaguia T-SQL,poisoSSDTnãooferece
ferramentavisualparaessafuncionalidade,vejaafiguraaseguir:
Fig.5.19:AlterandoocódigoSQLparaconfigura çãodachaveestrangeira
Aconfigura çãoda foreign keypodeservistanaúltimalinhadecódigoda
figura5.19.
Crieumaclasse Produtosemelhanteàclassedemesmonomecriadano
capítulo4(Resolução4.5dase ção4.3).Lembre-sedemudarotipodedadoda
propriedade Idedacria çãodoconstrutorqueinicializaráessapropriedade,
damesmamaneiraquefoifeitoparaasduasclassescriadasanteriormente.
Comaclasse Produtocriada,aclassequeseassociaráà NotaEntrada
tambémpodesercriada.Implementeaclasse ProdutoNotaEntrada,se-
guindoasorienta çõesdescritasparaacria çãode Produto.
201

## Página 218

5.9. Implementandoassociaçõesemtabelasdeumabasededados CasadoCódigo
Éprecisoagoracriaratabelaqueserámapeadaparaaclasse Produto.
Damesmamaneiraquefoicriadaatabela Fornecedoresanteriormente,
crieagoraatabela Produtos,quetemsuaestruturaapresentadapelafigura:
Fig.5.20:EstruturanecessáriaparaatabelaProdutos
Comatabelaeaclassequesereferenciama Produtosimplementadase
criadas,éprecisoagoracriarainterfacecomousuárioparaqueelepossarea-
lizarmanuten çõeseinser çõesdedadosnatabela.Seguindooexemplovisual
apresentadonocapítulo4,nestanovasolu ção,implementeanovajanela,já
interagindocomabasededados.Aproveiteecrietambémajanelaprincipal
paraaaplica çãoeosmenusdeacessoàsjanelas.
Da mesma maneira como foi feito com as tabelasFornecedores
e NotasDeEntrada,éprecisoagorarelacionaratabelaquerepresentará
osprodutosrecebidosemcadanotadeentrada. Paraisso, crieatabela
ProdutosNotasDeEntradadeacordocomoapresentadonafigura 5.21,
queserefereaocódigocompleto,necessárioparaacria ção.
202

## Página 219

CasadoCódigo Capítulo5. AcessoadadospormeiodoADO.NET
Fig.5.21:EstruturanecessáriaparaatabelaProdutosNotasDeEntrada
Notenoscamposdatabelaaexistênciadocampo IdNotaDeEntrada,
que não tem na classe que mapeia essa tabela uma propriedade seme-
lhante. Ao final da instrução CREATE TABLE, identificam-se as duas
chaves estrangeiras necessárias para implementar a associação com a ta-
bela Produtoseparaqueuma NotaDeEntradasaibaquaissãoseus
ProdutosDeNotasDeEntrada.
Umavezcriadasastabelasnabasededados,podeocorreranecessidade
derealizaralgumaaltera çãoemsuaestrutura,ou,ainda,anecessidadede
inserirregistrosdemaneiramanualnelas. Pararealizarqualquerumades-
sasopera ções,basta,no Server Explorer,clicarcomobotãodireitodo
mousesobreonomedatabelaeescolheraop çãodesejada: Show Table
Definitionparaexibiraestruturadatabelae,então,realizarmodifica ções;
ou Show Table Dataparaverosregistrosinseridos,alterá-losouinserir
novos:
203

## Página 220

5.9. Implementandoassociaçõesemtabelasdeumabasededados CasadoCódigo
Fig.5.22:Visualizandoopera çõespossíveisderealizaremumatabelajácriada
Agora com as classes e tabelas criadas, implemente na classe
NotaEntrada a propriedade Produtos, sua inicialização no cons-
trutor e os métodosRegistrarProduto(), RemoverProduto()
e RemoverTodosProdutos(), da mesma maneira que eles foram
implementadosnocapítulo4naResolução4.8 (seção4.5).
Comtodasasclassesimplementadas,éprecisocriarainterfacecomo
usuárioparaoregistrodanotadeentrada. Implementeoformuláriode
acordocomojácriadonocapítulo 4(figura4.8dase ção4.8).
Aimplementa çãodosmétodosqueserãoresponsáveispelaimplementa-
çãodorelacionamentoentreastabelasquemapeiamasassocia çõesentreas
classes Produto, Fornecedor, NotaEntradae ProdutoNotaEntrada
serárealizadanaclasse DAL_NotaEntrada,quetemsuadeclara çãoeseu
primeirométodoapresentadonasequência.
204

## Página 221

CasadoCódigo Capítulo5. AcessoadadospormeiodoADO.NET
Resolução5.22:métodoparainser çãodeumanotadeentradana
tabela
public class DAL_NotaEntrada {
private SqlConnection connection = DBConnection.
DB_Connection;
private void Insert (NotaEntrada notaEntrada) {
var command = new SqlCommand( "insert into " +
"NOTASDEENTRADA(IdFornecedor, Numero, " +
"DataEmissao, " DataEntrada) values( " +
"@IdFornecedor, @Numero, @DataEmissao, " +
"@DataEntrada)" , connection);
command.Parameters.AddWithValue( "@IdFornecedor" ,
notaEntrada.FornecedorNota.Id);
command.Parameters.AddWithValue( "@Numero" ,
notaEntrada.Numero);
command.Parameters.AddWithValue( "@DataEmissao" ,
notaEntrada.DataEmissao);
command.Parameters.AddWithValue( "@DataEntrada" ,
notaEntrada.DataEntrada);
connection.Open();
command.ExecuteNonQuery();
connection.Close();
}
}
Noteque,nainser çãodanotadeentradainformadapelousuário,não
existereferênciaaosprodutosdanota.Issodeve-seàregradeque,parainser-
çãodeprodutosemumanota,elajádeveexistirnatabela,talcomodefinido
nocapítulo4.Osegundométodoaserimplementadonaclasse DALseráo
de Update(),queéapresentadoaseguir.
Resolução5.23:métodoqueatualizadadosdeumadeterminada
notadeentradanatabela
private void Update (NotaEntrada notaEntrada) {
var command = new SqlCommand( "update NOTASDEENTRADA " +
"set IdFornecedor=@IdFornecedor, Numero=@Numero, " +
205

## Página 222

5.9. Implementandoassociaçõesemtabelasdeumabasededados CasadoCódigo
"DataEmissao=@DataEmissao, DataEntrada=" +
"@DataEntrada where (Id=@Id)" , connection);
command.Parameters.AddWithValue( "@IdFornecedor" ,
notaEntrada.FornecedorNota.Id);
command.Parameters.AddWithValue( "@Numero" ,
notaEntrada.Numero);
command.Parameters.AddWithValue( "@DataEmissao" ,
notaEntrada.DataEmissao);
command.Parameters.AddWithValue( "@DataEntrada" ,
notaEntrada.DataEntrada);
command.Parameters.AddWithValue( "@Id" ,
notaEntrada.Id);
connection.Open();
command.ExecuteNonQuery();
connection.Close();
DeleteAllProdutosFromNotaEntrada(notaEntrada.Id);
InsertProdutosNotaDeEntrada(notaEntrada.Id,
notaEntrada.Produtos);
}
Apenúltimainstru çãodométodo Update()éainvoca çãoaométodo
DeleteAllProdutosFromNotaEntrada(),querecebecomoargumento
o Iddanotadeentrada.Estemétodoseráresponsávelporremoverdatabela
ProdutosNotasDeEntradatodososregistrosquepertencemanotaque
estásendoatualizada(Resolução5.24).
A última instru ção invoca o método
InsertProdutosNotaDeEntrada(), que recebe oId da nota e a
coleçãoatualde Produtosqueestapossui( Resolução5.25).Estemétodo
será responsável por inserir na tabelaProdutosNotasDeEntrada a
coleçãoatualizadadeprodutos.
Resolução5.24:métodoqueremovedatabelatodososprodutos
deumadeterminadanotadeentrada
private void DeleteAllProdutosFromNotaEntrada ( long?
idNotaEntrada) {
var command = new SqlCommand( "delete from " +
NOTASDEENTRADA where (Id=@Id) ", connection);
206

## Página 223

CasadoCódigo Capítulo5. AcessoadadospormeiodoADO.NET
command.Parameters.AddWithValue( "@Id" ,
idNotaEntrada);
connection.Open();
command.ExecuteNonQuery();
connection.Close();
}
Resolução5.25:métodoqueinseredatabelatodososprodutosde
umanotadeentrada
private void InsertProdutosNotaDeEntrada ( long? idNotaEntrada,
IList<ProdutoNotaEntrada> produtos) {
var command = new SqlCommand( "insert into " +
"PRODUTOSNOTASDEENTRADA(IdNotaDeEntrada, " +
"IdProduto, PrecoCustoCompra, QuantidadeCompra) " +
"values(@IdNotaDeEntrada, @IdProduto, " +
"@PrecoCustoCompra, @QuantidadeCompra" ,
connection);
connection.Open();
foreach ( var produto in produtos) {
command.Parameters.Clear();
command.Parameters.AddWithValue( "@IdNotaDeEntrada" ,
idNotaEntrada);
command.Parameters.AddWithValue( "@IdProduto" ,
produto.Id);
command.Parameters.AddWithValue(
"@PrecoCustoCompra" , produto.PrecoCustoCompra);
command.Parameters.AddWithValue(
"@QuantidadeCompra" ,produto.
QuantidadeComprada);
command.ExecuteNonQuery();
}
connection.Close();
}
Verifiqueousodainstru ção foreach,quepercorreacole çãorecebida
comoargumento. Acadaprodutoexistentenacole ção,osparâmetrossão
limpos,inseridosdeacordocomcadaproduto,pormeiodachamadaaomé-
todo ExecuteNonQuery().
207

## Página 224

5.10. Implementandoainterfacecomousuárioparaasassocia ções CasadoCódigo
Opróximométodoaserimplementadoéoqueseráinvocadopelain-
terfacecomousuário,o Save(),quedelegaráaexecu çãoparaométodo
Update()ou Insert(),deacordocomoobjetorecebidocomoargu-
mento.Estepodeservisualizadonasequência.
Resolução5.26:métodoresponsávelpordelegaraatualiza çãode
dadosdeumanotadeEntradaparainser çãoouatualiza çãode
dados
public void Save (NotaEntrada notaEntrada) {
if (notaEntrada.Id == null )
this .Insert(notaEntrada);
else
this .Update(notaEntrada);
}
5.10 Implementando a interface com o usuário
para as associações
Com as tabelas criadas e os principais métodos para a classe
DAL_NotaEntrada já implementados, é preciso implementar a janela
daNotadeEntrada. Oprimeiropassoéadefini çãodos DALsqueserão
utilizadosnajanela,oqueveremosaseguir.
Resolução5.27:declara çãodecamposparaaclasse
public partial class NotasEntradaCRUD : Form {
private DAL_NotaEntrada dal = new DAL_NotaEntrada();
private DAL_Fornecedor dalFornecedor =
new DAL_Fornecedor ();
private DAL_Produto dalProduto = new DAL_Produto();
private NotaEntrada notaAtual;
// Código omitido
}
A janela de Nota de Entrada possui dados vindos de duas tabelas:
Fornecedorese Produtos.Paraselecionarofornecedordanotaeopro-
208

## Página 225

CasadoCódigo Capítulo5. AcessoadadospormeiodoADO.NET
dutodacompra,seráfeitousode ComboBox,damesmamaneiraquefoifeito
nocapítulo4,comadiferen çadequeagoraosdadosvêmdetabelas,enãode
coleções.Opreenchimentodesses ComboBoxsérealizado,inicialmente,no
construtordaclasse,vistonasequência.
Resolução5.28:métodoconstrutordainterfacecomousuáriopara
oregistrodasnotasdeentrada
public NotasEntradaCRUD () {
InitializeComponent();
InicializaComboBoxs();
}
Pelofatodeapopula çãodos ComboBoxspodersernecessáriaemdiver-
sosmomentosdaintera çãocomousuário,foiimplementadoummétodo(o
InicializaComboBox())paraestafuncionalidade,quepodeservisuali-
zadonasequência.
Resolução5.29:métodoqueinicializaosComboBoxs
private void InicializaComboBoxs () {
cbxFornecedor.Items.Clear();
cbxProduto.Items.Clear();
foreach (Fornecedor fornecedor in this .dalFornecedor.
GetAllAsIList()) {
cbxFornecedor.Items.Add(fornecedor);
}
foreach (Produto produto in this .dalProduto.
GetAllAsIList()) {
cbxProduto.Items.Add(produto);
}
}
Observenocódigoqueaprimeirafuncionalidadedométodoérealizara
limpezadositensdecada ComboBox.Tantoessalimpezacomoachamada
periódicaaessemétododeve-seaofatodeosdadosviremdeumatabelaede
209

## Página 226

5.10. Implementandoainterfacecomousuárioparaasassocia ções CasadoCódigo
que,umoutrousuário,acessandoaaplica çãoaomesmotempo,podeinserir
novosdadose,nasuaexecu ção,elespodemsernecessários.
Umsegundopontoimportanteéacole çãodedadosvindados DALs,
representadapormétodosqueretornamtodososdados,comoumacole ção
dotipo IList.Aimplementa çãodométodo GetAllAsIList()daclasse
DAL_Fornecedorpodeservisualizadaaseguir.
Resolução5.30:métodoquerecuperatodososfornecedoresdata-
beladedadoseretornacomoumobjetoIList
public IList<Fornecedor> GetAllAsIList() {
IList<Fornecedor> fornecedores =
new List<Fornecedor>();
var adapter = new SqlDataAdapter( "select id, cnpj,
nome from FORNECEDORES ", connection);
var builder = new SqlCommandBuilder(adapter);
var table = new DataTable();
adapter.Fill(table);
connection.Close();
for ( int i = 0 ; i < table.Rows.Count; i++) {
var row = table.Rows[i];
fornecedores.Add(
new Fornecedor () {
Id = Convert.ToInt64(row[ "id" ]),
CNPJ = ( string ) row[ "cnpj" ],
Nome = ( string ) row[ "nome" ]
});
}
return fornecedores;
}
Observenoblocoderepeti ção for()queéfeitousodaquantidade(
Count)delinhas( Rows)populadasno DataTable,comotérminodainte-
ração.Asinstru çõesanterioressãotodasjáconhecidasedispensamexplica-
ções.Notequeanavega çãoentreosregistrosérealizadaapósofechamento
210

## Página 227

CasadoCódigo Capítulo5. AcessoadadospormeiodoADO.NET
daconexãocomobanco,poisosdadosjáestãonamemória. Estaéuma
característicadoADO.NET:trabalhardemaneiradesconectada.
Asinstru çõesquecompõemobloco for()começamporobterumade-
terminadalinha(registrodatabela)deacordocomoseuíndice(variávelde
interação i).Comalinhaobtida,umobjeto Fornecedoréinstanciadoe,
então,adicionadoàcole çãodefornecedores.Notequecadacampoéacessado
nalinhapormeiodeseunome,identificadocomoíndice(emborasejautili-
zadostring).Oretornodecadacolunaéum object,porissoanecessidade
de casts.
Renomeie os métodos GetAll() das classes DAL para
GetAllAsDataTable(), pois fica mais condizente com o novo mé-
todocriado. Destamaneira, épossívelterváriosmétodoscomretornos
diferentesenomessemanticamentecompreensíveis.
Crie nas classesDAL_Produto e DAL_NotaEntrada os métodos
GetAllAsIList()e GetAllAsDataTable(),seguindoosmoldesdos
métodosdemesmonomedaclasse DAL_Fornecedor.
Comos ComboBoxspopulados,jáépossívelrealizarainclusãodenotas.
Implementeométodoqueimplementaoevento Clickdobotão Gravar,
deacordocomaresolu çãoquesegue.
Resolução5.31:métodoqueimplementaoeventoClickdobotão
GravardaNotadeEntrada
private void btnGravarNota_Click ( object sender,
System.EventArgs e) {
dal.Save( new NotaEntrada() {
Id = string .IsNullOrEmpty(txtIDNotaEntrada.
Text) ? ( long? ) null : Convert.ToInt64(
txtIDNotaEntrada.Text),
Numero = txtNumero.Text,
DataEmissao = Convert.ToDateTime(dtpEmissao.Value),
DataEntrada = Convert.ToDateTime(dtpEntrada.Value),
FornecedorNota = (Fornecedor) cbxFornecedor.
SelectedItem
});
MessageBox.Show( "Manutenção realizada com sucesso" );
211

## Página 228

5.10. Implementandoainterfacecomousuárioparaasassocia ções CasadoCódigo
ClearControls();
}
Alógicadométodonãoédiferentedasanteriores.Elafoiexibidaapenas
paraapresentar–emboratenhasidoapresentadonocapítulo4–comoobter
osdadosdos ComboBoxs.
Ométodo ClearControls()segueamesmalógicadosimplementa-
dosnestecapítulo.Entretanto,os ComboBoxseos DateTimePickerstêm
seuspadrõesdeinicializa ção. Sendoassim,recorraaocapítulo 4paraver
essasparticularidadeseimplementeessemétodo( Resolução4.33 dase ção
4.10).
Pararegistrarnanotadecompraosprodutoscomprados,éprecisoque
anotaestejadevidamentepersistidanatabelaeselecionadanoformulário
comosdadosdocorpodanota.Destamaneira,épossívelinformarosdados
dosprodutoscomprados. Entretanto,aoiniciaroformuláriodeentrada,é
precisoqueosregistrosjárealizadossejamexibidos. Paraisso,invoqueo
métodoGetAllNotas(),exibidonasequência,noconstrutordaclasseque
representaajaneladeintera çãocomousuário.
Resolução5.32: métodoquerecuperatodasasnotasregistradas
paraexibirnoDataGridView
private void GetAllNotas () {
dgvNotasEntrada.DataSource = dal.GetAllAsDataTable();
}
Aresolu çãoseguinteapresentaométodoreferenteàsele çãodeumanota
no DataGridView.
Resolução5.33:métodoquecapturaoeventoCellClickdoData-
GridViewdenotasdeentrada,parasele çãodeumanota
private void dgvNotasEntrada_CellClick ( object sender,
DataGridViewCellEventArgs e) {
if (e.RowIndex < 0 || e.ColumnIndex < 0 )
return ;
this .notaAtual = dal.GetById(Convert.ToInt64(
212

## Página 229

CasadoCódigo Capítulo5. AcessoadadospormeiodoADO.NET
dgvNotasEntrada.Rows[e.RowIndex].Cells[ 0 ].Value));
txtIDNotaEntrada.Text = notaAtual.Id.ToString();
txtNumero.Text = notaAtual.Numero;
dtpEmissao.Value = notaAtual.DataEmissao;
dtpEntrada.Value = notaAtual.DataEntrada;
cbxFornecedor.SelectedItem = notaAtual.FornecedorNota;
}
Ométodo GetById(),querealizaabuscadanotadeentradaselecio-
nadanatabela,pertenceao DAL,diferentementedoapresentadonaimple-
mentaçãodoformuláriodefornecedores.Suaimplementa çãopodeservisu-
alizadaaseguir.
Resolução5.34:métodoquerealizaabuscaporumanotadeen-
tradatendocomobaseseuId
public NotaEntrada GetById ( long id) {
NotaEntrada notaEntrada = new NotaEntrada();
DAL_Fornecedor dalFornecedor = new DAL_Fornecedor();
long idFornecedorNota = - 1 ;
var command = new SqlCommand( "select id, idfornecedor,
numero, dataemissao, dataentrada from NOTASDEENTRADA
where id = @id ", connection);
command.Parameters.AddWithValue( "@id" , id);
connection.Open();
using (SqlDataReader reader = command.ExecuteReader()) {
while (reader.Read()) {
notaEntrada.Id = reader.GetInt64( 0 );
idFornecedorNota = reader.GetInt32( 1 );
notaEntrada.Numero = reader.GetString( 2 );
notaEntrada.DataEmissao = reader.GetDateTime( 3 );
notaEntrada.DataEntrada = reader.GetDateTime( 4 );
}
}
connection.Close();
if (idFornecedorNota > 0 )
notaEntrada.FornecedorNota = dalFornecedor.
GetById(idFornecedorNota);
return notaEntrada;
213

## Página 230

5.10. Implementandoainterfacecomousuárioparaasassocia ções CasadoCódigo
}
Ao analisarmos o código, identificamos uma variável, a
idFornecedorNota. Sua finalidade refere-se ao fato de que, no mo-
mentodaleiturado SqlDataReaderquerecuperaanotadesejada,háa
invocaçãoaométodo GetByIddaclasse DAL_Fornecedor(). Osdois
métodoscompartilhamamesmaconexãoe,deacordocomasregraspara
ousodeum DataReader,nãoépossívelmanterdoisobjetosdessaclasse
abertosaomesmotempo,paraumamesmaconexão.Sendoassim,o Iddo
fornecedordanotalocalizadaéarmazenadoemumavariávele,aotérmino
dacláusula using,essevalor,casoumfornecedortenhasidoencontrado,
éenviadocomoargumentoparaométododo DALdefornecedores,oque
veremosnasequência.
Resolução5.35: métodoquerealizaabuscaporumfornecedor
tendocomobaseseuId
public Fornecedor GetById ( long id) {
Fornecedor fornecedor = new Fornecedor();
var command = new SqlCommand( "select id, cnpj, nome from
FORNECEDORES where id = @id ", connection);
command.Parameters.AddWithValue( "@id" , id);
connection.Open();
using (SqlDataReader reader = command.ExecuteReader()) {
while (reader.Read()) {
fornecedor.Id = reader.GetInt32( 0 );
fornecedor.CNPJ = reader.GetString( 1 );
fornecedor.Nome = reader.GetString( 2 );
}
}
connection.Close();
return fornecedor;
}
Comapossibilidadederegistrarosprodutoscompradosparaanotaem
edição,éprecisoagoraimplementarestafuncionalidade.Trata-sedoevento
Clickdobotão Novodosdadosdeprodutos.
214

## Página 231

CasadoCódigo Capítulo5. AcessoadadospormeiodoADO.NET
Implementeométodoquecapturaoevento Clickdobotão Novore-
ferenteaosdadosdoprodutoaserinformado.Aoimplementá-lo,vocêverá
(erecordará)quedoisnovosmétodostambémdevemserimplementados:
o ChangeStatusOfControls()eo ClearControlsProduto().Esses
trêsmétodossãoosmesmosimplementadosnocapítulo 4.
Emboraaassocia çãoerelacionamentoentreclasses/tabelasdeNotasde
EntradaeseusProdutosjátenhamsidoimplementadas,pormeiodosméto-
dosrelacionadosàatualiza çãodanota( Update()de DAL_NotaEntrada),
épossívelfazê-lodeumamaneiramaissimples,umavezquecadaobjetoda
classe ProdutoNotaEntradapossuiseu Idúnico,oquetambémocorre
natabela.Aseguir,tragoométodoresponsávelporinserironovoproduto
dacompra.
Resolução5.36:métododaclasseDALquerealizaainser çãodo
produtoregistradoemumacompra
private void InsertProduto (NotaEntrada notaEntrada,
ProdutoNotaEntrada produto) {
notaEntrada.Produtos.Add(produto);
var command = new SqlCommand( "insert into " +
"PRODUTOSNOTASDEENTRADA(idnotadeentrada, " +
"idproduto, precocustocompra, quantidadecompra) " +
"values(@idnotadeentrada, @idproduto, " +
"@precocustocompra, @quantidadecompra)" ,
this .connection);
command.Parameters.AddWithValue( "@idnotadeentrada" ,
notaEntrada.Id);
command.Parameters.AddWithValue( "@idproduto" ,
produto.Id);
command.Parameters.AddWithValue( "@precocustocompra" ,
produto.PrecoCustoCompra);
command.Parameters.AddWithValue( "@quantidadecompra" ,
produto.QuantidadeComprada);
connection.Open();
command.ExecuteNonQuery();
connection.Close();
}
215

## Página 232

5.10. Implementandoainterfacecomousuárioparaasassocia ções CasadoCódigo
Vejaqueométodorecebe,alémdoprodutoqueseráregistrado,anota
aqueesteserefere.Naclasse ProdutoNotaEntradanãoexistereferência
paraquenotacadaprodutopertence,masnatabelaexisteumcampocom
o Iddanotadeentrada.Paraqueorelacionamentoentreessasduaspossa
serimplementado,éprecisoqueestemétodosaibaqualéanotaquetemo
produto. Ométodoparaatualiza çãodosdadosdeumprodutojáinserido
podeserverificadonasequência.
Resolução5.37:métododaclasseDALquerealizaaatualiza çãona
tabeladedadosdeumprodutopreviamenteinserido
private void UpdateProduto (ProdutoNotaEntrada produto) {
var command = new SqlCommand( "update " +
"PRODUTOSNOTASDEENTRADA set idproduto=@idproduto, " +
"precocustocompra=@precocustocompra, " +
"quantidadecompra=@quantidadecompra) where " +
(id=@id) ", this.connection);
command.Parameters.AddWithValue( "@idproduto" ,
produto.Id);
command.Parameters.AddWithValue( "@precocustocompra" ,
produto.PrecoCustoCompra);
command.Parameters.AddWithValue( "@quantidadecompra" ,
produto.QuantidadeComprada);
command.Parameters.AddWithValue( "@id" , produto.Id);
connection.Open();
command.ExecuteNonQuery();
connection.Close();
}
Comosmétodosdeinser çãoeatualiza çãoimplementados,éprecisoim-
plementarométodopúblico,queseráinvocadopelométodoquecapturaro
evento Clickdobotão Gravardosprodutos.
Umavezqueocomportamentoesperadoparaométodoquecapturao
evento Clickdobotão Gravardosdadosdeprodutoséomesmoqueo
implementadoparaanotadeentrada–alterandoapenasoscomponentesde
origemdosdadoseoobjetoaserenviadoparaoDAL–,implemente-o.Ao
final,tambémprecisamosinvocaro ClearControlsProduto(),enãoo
ClearControls().
216

## Página 233

CasadoCódigo Capítulo5. AcessoadadospormeiodoADO.NET
Implemente o comportamento para o método que captura o evento
Clickdobotão Removerdeprodutos.Seráprecisotambémimplementar
ométodonaclasse DAL,queseráinvocadoporessemétodo.
Realizeaimplementa çãodométodoparaoevento Clickdobotão
Removerpararemoverumanota.Utilizeosmétodosjáimplementadospara
removeranotaselecionadaeosprodutosregistradosparaela.
5.11 Conclusão
Nestecapítulo,foitrabalhadooacessoabancosdedados.Umaadapta çãoda
soluçãoimplementadanocapítulo 4foiproposta.Novosconceitos,recursos
dalinguagem,ferramentasetécnicasforamapresentados,discutidosetraba-
lhados.
Agora,comoconhecimentodecomomanipularumabasededados,é
possívelacria çãodeumaaplica çãomaior,poisodomíniodeconhecimento
oferecidoatéestecapítulotrazsubsídiosparaisso.Opróximocapítuloapre-
sentaumanovatécnicaparaacessoadados,queéousode DataSetTipado.
217

## Página 235

Capítulo6
UtilizandoDataSetTipadopara
acessoàbasededados
Alguns dos recursos oferecidos pelo ADO.NET foram apresentados
no capítulo 5, onde foram utilizadas as classes SqlConnection,
SqlDataAdapter, SqlCommand, SqlDataReader e, de maneira
bem simples, aDataTable, para realizar seleções e manutenções em
registrosdeumabasededados. Todososexemplosfizeramuso,deforma
explícita,deinstru çõesSQL.
Outrorecursoparaamanipula çãodedadosoferecidopeloADO.NETé
oDataSet.Inicialmente,serãoutilizadosexemplosdiretos,semusodeinter-
facecomousuário,paraconhecimentoeaplica çãodesserecurso. Aofinal,
seráconstruída,comaprimoramentos,aaplica çãotrabalhadanocapítulo 5,
fazendousodeDataSetTipado.

## Página 236

6.1. Introdução CasadoCódigo
6.1 Introdução
O DataSet do ADO.NET é um componente que contém, de forma
direta, outros dois componentes: DataTableCollection e sua
DataRelationCollection.Elerepresentaumconjuntocompletodeda-
dos,incluindoastabelas(estruturas)quecontêmessesdados,seusrelacio-
namentos,suasclassifica çõesetambémasrestri çõesqueestespossamconter
ousofrer.
Épossívelafirmarqueum DataSetrepresentaumacompletabasede
dados,comtabelas,colunas,registros, constraints(restrições),chaves
primárias,chavesestrangeiraseíndices. Tudoissolocalmente,namemória
RAMdeseucomputador. Afigura 6.1apresentaumdiagrama,quetrazo
DataSet.
Fig.6.1:Selecionandoprojetoparaterreferênciaadicionada
Praticamentetodaestruturaapresentadanafigura 6.1foitrabalhadano
capítulo 5, no qual alguns dos recursos do .Net Framework Provider do
SQLServerforamusadosparaimplementaraaplica çãodeexemplo. Note
noladoesquerdodafiguraque,emumnívelmaisbaixo,encontra-seuma
basededadosquerecebeefornecedadosparaaestruturadeclassesque
ossubmetemerecebem. Aoladodireitodafiguraestáo DataSetcom
a DataTableCollectione,dentrodela,a DataTable,quetambémfoi
apresentadanocapítulo5.
220

## Página 237

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
Comopodeserverificadopelafigura 6.1,um DataTablepertenceauma
DataTableCollection, damesmamaneiraqueumatabelapertencea
umabasededados.Novamentenoladoesquerdodafigura,o DataAdapter
temcomocomponentesquatro Commands,cadaumrepresentandoumains-
truçãoSQL.Todaessaestruturarepresentao DataSet,quetemcomofonte
dedadoso XML,eseráapresentadaetrabalhadademaneiraintegradaneste
capítulo.
6.2 Desenhando o formulário para a implemen -
tação de um exemplo de uso de DataSet e
seus componentes
Como já dito e é possível de se verificar na figura 6.1, um DataSet
é uma coleção de DataTables, pois possui dentro dele um objeto
DataTableCollection. Parautilizarefetivamenteum DataSet,épre-
cisopossuiralguns DataTables.
Destamaneira,paraimplementarumexemplo,seguindoalógicaepro-
blemaapresentadonocapítulo 5,seráfeitousodedois DataTables: um
paraarmazenarestadosbrasileiroseoutroparaarmazenarascidadesdecada
estado.
NoVisualStudio,crieumanovasolu çãochamada SolutionDataSet
e,dentrodesta,umprojeto Windows Formschamado DataSetProject.
Apague o formulário criado pelo template e crie um novo, chamado
FormDataSetTest. Implementeseuformulárioparaquetenhaaaparên-
ciadoapresentadonafiguraaseguir:
221

## Página 238

6.2. Desenhandooformulárioparaaimplementa çãodeumexemplodeusodeDataSeteseus
componentes CasadoCódigo
Fig.6.2:Janelaparaintera çãoetestescomDataSets
Apartesuperiordoformulárioécompostapelosbotõesqueexecutarão
asatividadesrelativasaosseus captions. Nosbotõesfoiajustadaapenasa
fontedotexto,paraquesejadeumacordiferenteeemnegrito. Umnovo
controlefoiinserido,ocontainer TabControl,comduasguias( Pages).Na
primeiraguia–tambémchamadadeTab–,foiinseridoumTextBoxcom
apropriedade MultiLine,recebendo True,paraassimaceitarmúltiplas
linhas,jáqueissoseránecessárioparaaexibi çãodoXMLdosdados.
Naimplementa çãoqueseráapresentadanasequência,paraqueosdados
XMLapare çam,seráprecisoantesclicarnobotão Criar DataSete,em
seguida,no Inserir Dados,paraentãoclicarem Visualizar XML.
Asegundaguia,queexibeosdadosemcontrolesvisuais,podeservisua-
lizadanafiguraaseguir:
222

## Página 239

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
Fig.6.3:Controlesvisuaisparaintera çãocomDataSets
Naguiarepresentadanafigura 6.3,foiinseridoo TableLayoutPanel
comduaslinhaseduascolunas,sendoquenaprimeiraforaminseridosum
Labeleum ComboBoxe,nasegunda,um DataGridView.Otamanhoda
primeiracolunado TableLayoutPanelfoiconfiguradoparaserautomá-
tico,destamaneira,ocuparáalargurado Label.O DataGridViewdase-
gundalinhafoiinseridonaprimeiracélulaeteveapropriedade ColumnSpan
configuradacomovalor2.Paraacessá-la,seráprecisoseguiramesmaordem
daapresentadaparavisualizaroXML.
Um TabControlcontémTabPages,quesãorepresentadasporobje-
tos TabPage,quepodemserinseridospormeiodapropriedade TabPages.
Aordemdas TabPagesnacole çãodo TabControl( TabPages)reflete
diretamentenaordememqueasTabsaparecerãonocontrole.Ousuáriopo-
derámudaraTabPagecorrenteclicandoemqualquerumadasexibidaspelo
controle.Diversaspropriedadesemétodossãooferecidosparaessecontrole,
sendoumadaspropriedadesa SelectedTab,quepermiteatribuirouobter
aTabatualmenteemfoco.
Avisualiza çãodosdadosnoexemplodependerádaintera çãocomousuá-
rio.EleprecisarácriaroDataSet,popularedepoisvisualizar.Éinteressante
que,aoclicaremumadasguiasdevisualiza ção,elepossaverosdados,sem
anecessidadedecriaralgoquedeveriaestarcriado,umavezqueháapossi-
bilidadedevisualiza ção.Duassãoessaspossibilidades:
223

## Página 240

6.3. Implementandoacriação,popula çãoeintera çãocomoDataSet CasadoCódigo
1) Nãoexibirasguiasdevisualiza çãoatéqueosdadossejamdisponibiliza-
dos;
2) Aooptarporvisualizarosdados,casoelesnãoexistam,elesdevemser
criadosautomaticamente.
Pensenessassolu çõeseprocureimplementá-lasparapodermediroque
émaisprodutivo.
6.3 Implementando a criação , população e in -
teração com o DataSet
Oprimeirobotãodainterfacecomousuárioéresponsávelporexecutaras
instruçõesquecriarãooDataSeteodisponibilizarãoparaaaplica ção. De
maneiraanálogaaumabasededados,serãocriadasastabelaseseusrelacio-
namentos,comoéapresentadoaseguir.
Resolução6.1:métodoqueimplementaoeventoClickdobotão
CriarDataSet
private void btnCriarDataSet_Click ( object sender, EventArgs e){
dsEstadosCidades = InitializeDataSet();
MessageBox.Show( "DataSet inicializado com sucesso" );
}
Ométodo InitializeDataSet()–representadonaResolução6.3 –
criaum DataSeteseuscomponentesparaa DataTableCollectione
DataRelationCollection,eretornao DataSetcriado,queéatribuído
aocampo dsEstadosCidades,declaradonoiníciodaclasse.Vejaaseguir.
Resolução6.2:declara çãodoDataSetaserutilizado
public partial class FormDataSetTest : Form {
private DataSet dsEstadosCidades;
public FormDataSetTest () {
InitializeComponent();
224

## Página 241

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
}
// Código omitido
}
Resolução6.3:métodoqueinicializaoDataSetdaaplica ção
private DataSet InitializeDataSet () {
DataTable dtEstados = new DataTable( "Estados" );
dtEstados.Columns.Add( "id" );
dtEstados.Columns.Add( "uf" );
dtEstados.Columns.Add( "nome" );
DataTable dtCidades = new DataTable( "Cidades" );
dtCidades.Columns.Add( "id" );
dtCidades.Columns.Add( "idestado" );
dtCidades.Columns.Add( "nome" );
DataSet dsEstadosCidades = new
DataSet( "EstadosCidades" );
dsEstadosCidades.Tables.Add(dtEstados);
dsEstadosCidades.Tables.Add(dtCidades);
DataRelation drCidadeEstado = new
DataRelation( "CidadesEstados" ,
dtEstados.Columns[ "id" ],
dtCidades.Columns[ "idestado" ]);
dsEstadosCidades.Relations.Add(drCidadeEstado);
return dsEstadosCidades;
}
Observenocódigoque,nadefini çãodos DataTables,éenviadoao
construtoronomeparaatabelaqueserácriada. Umavezcriadaatabela,
éprecisoadicionarnelaascolunasqueacomporão.Vejaqueesteprocessoé
realizadopelainvoca çãodométodo Add()dapropriedade Columns,que
éumainstânciade DataColumnCollection.
Paraficarsimples,éusadoométodoquerecebeapenasonomeparaa
coluna,sendoqueotipodedadoserá string.Existemoutrasduassobre-
225

## Página 242

6.3. Implementandoacriação,popula çãoeintera çãocomoDataSet CasadoCódigo
cargasparaessemétodo,podendodefiniraqualtipodedadoacolunaaser
adicionadaserefere.Procureestudá-laseaplicá-las.
Criadas as duas tabelas, elas precisam ser adicionadas aoDataSet,
paraqueorelacionamentoentreelaspossaserconfiguradoeadicionado
ao DataSet. O relacionamento é estabelecido por meio de um ob-
jeto DataRelation que, em sua instanciação, recebe o nome para o
relacionamento, a coluna pai (Parent/Master Column) e a coluna filho
(Child/Details Column)e,então,éadicionadoàpropriedade Relations(
DataRelationCollection)do DataSet.
Como DataSeteastabelascriados,éprecisoagorapopulá-las,para
quepossamserutilizadas.Osegundobotão, Inserir Dados,temsuaim-
plementaçãoexibidanasequência.
Resolução6.4:métodoqueinseredadosnosDataTables
private void btnInserirDados_Click ( object sender, EventArgs e){
DataTable dtEstados = dsEstadosCidades.
Tables[ "Estados" ];
dtEstados.Rows.Add( 1 , "PR" , "Paraná" );
dtEstados.Rows.Add( 2 , "SP" , "São Paulo" );
dtEstados.Rows.Add( 3 , "SC" , "Santa Catarina" );
DataTable dtCidades = dsEstadosCidades.
Tables[ "Cidades" ];
dtCidades.Rows.Add( 1 , 1 , "Foz do Iguaçu" );
dtCidades.Rows.Add( 2 , 1 , "Medianeira" );
dtCidades.Rows.Add( 3 , 1 , "Curitiba" );
dtCidades.Rows.Add( 4 , 2 , "São Paulo" );
dtCidades.Rows.Add( 5 , 2 , "Ilha Solteira" );
dtCidades.Rows.Add( 6 , 3 , "Florianópolis" );
MessageBox.Show( "Dados inseridos com sucesso." );
}
Observequeainser çãodosdadossedápormeiodainvoca çãoaométodo
Add(),pertencenteàpropriedade Rows(DataRowCollection).Verifique
queaordemdosparâmetrosenviadoscorrespondeàordememqueascolu-
226

## Página 243

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
nasforamcriadas.Notetambémqueosvaloresparaoatributo idestado
sãoválidos,ouseja,respeitama constraintda Relationexistenteentre
asduas DataTables.
Agoraqueo DataSetjátemseusdadosregistrados,épossíveltrabalhar
avisualiza çãodeles.Comofoiverificadonafigura 6.1,um DataSetregistra
seusdadosemumarquivo XML,demaneiranativa.Destamaneira,ocódigo
quecapturaoeventoparaocliquedobotão Visualizar XMLéapresentado
nasequênciaeéresponsávelpelaexibiçãodeles(figura 6.2).
Resolução6.5:métodoquerepresentaoeventoClickdobotãoVi-
sualizarXML
private void btnVisualizarXML_Click ( object sender,
EventArgs e) {
tcResultados.SelectedTab = tpXML;
txtXML.Text = dsEstadosCidades.GetXml();
}
Ocódigodeterminaquea TabPagereferenteaoXMLsejaexibida–
noteonomequefoidadoao TabControlea TabPageemquestão–e,
emseguida,ométodoqueretornaoXMLreferenteaosdadosdo DataSet
éinvocadoeseuresultadoexibidono TextBox.
Ocomportamentoparaoúltimobotãoéemrespeitoàexibi çãodosdados
emcontrolesvisuaisdeintera çãodiretacomousuário,etevesuarepresenta-
çãodisponibilizadanafigura 6.3.Vejaseucódigonasequência.
Resolução6.6: métodoquerepresentaoeventoClickdobotão
ControlesVisuais
private void btnVisualizarControes_Click ( object sender,
EventArgs e) {
BindingSource bsMaster = new BindingSource();
BindingSource bsDetails = new BindingSource();
bsMaster.DataSource = dsEstadosCidades;
bsMaster.DataMember = "Estados" ;
bsDetails.DataSource = bsMaster;
227

## Página 244

6.3. Implementandoacriação,popula çãoeintera çãocomoDataSet CasadoCódigo
bsDetails.DataMember = "CidadesEstados" ;
tcResultados.SelectedTab = tpComboEGrid;
cbEstados.DataSource = bsMaster;
cbEstados.DisplayMember = "nome" ;
cbEstados.ValueMember = "id" ;
dgCidades.DataSource = bsDetails;
}
É possível verificar na implementação desse método o uso de
BindingSources, que já foram usados anteriormente. Dois destes
componentessãodeclarados: umresponsávelporapresentarosestadosno
ComboBox(tabelapaidorelacionamento)eoutroparaapresentarascidades
no DataGridView.
Note que, na definição da fonte de dados (DataSource) do
BindingSourcedeestados,éatribuídoo DataSetquecontémtodasasta-
belas.Destamaneira,éprecisoconfigurarqualdastabelasserárealmenteuti-
lizada.Issopodeserfeitoatribuindoseunomeàpropriedade DataMember.
Comofontededadospara BindingSourcefilho( bsDetails)–quecon-
teráascidades–,atribui-seoBindingSourcepaidarela ção,o bsMaster
–quecontémosestados–,eonomedorelacionamento(oDataRelation)
como DataMember.
Apósaconfigura çãodos BindingSources, procede-seaconfigura-
çãodoscontrolesvisuais. Ado DataGridViewésimplesejáfoirea-
lizada. Parao ComboBox, comoosdadosnãovêmdeumacole çãode
objetosdedomínio,massimdestrings,éprecisoconfigurarqualvaloré
exibido( DisplayMember)equalservirácomochave( ValueMember).
Comessaconfigura çãorealizada, somadaàsdo BindingSourceseda
DataRelation, quando o usuário alterar um estado noComboBox, o
DataGridViewexibiráapenasascidadesdaqueleestado.
Finalizando,comovistonaaplica çãoanteriormenteimplementadaeex-
plicada,um DataSetpermitequeumabasededadossejacriada,populada
eforne çatambémosdadosnelaarmazenados.Essabasededados,quefica
namemóriaRAM,podesofrermanuten çõeseintera ções,semanecessidade
deexistênciadeumbancodedadosparaarmazenamento,eosdadospo-
dempersistidosemumarquivoXML.Entretanto,ocomuméqueosdados
228

## Página 245

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
deumabasededadosestejamrealmenteemumbancodedados.Issotam-
bémépossívelfazendousodeDataSets,maisespecificamenteos DataSets
Tipados.
6.4 DataSetsTipados
Nocapítulo5,quefezusodepersistênciaemumabasedados,foipossível
identificarumadificuldadequandoseusaumabasededadosrelacionale
umaaplica çãoorientadaaobjetos.Estadificuldaderefere-seaomapeamento
dasinforma çõesfornecidaspelousuárioemsuainterfacecomaaplica ção(a
janeladeformulário),emobjetosquerepresentamalógicadenegócio(as
classes)eaomapeamentotambémdessesobjetosparaumbancodedados
relacional. Autilizaçãodosobjetosdenegócionacamadaintermediária–
entreinterfacecomousuárioeabasededados–trazumarelativaperda
deprodutividadeparaaequipedeprograma ção,aumentando,inclusive,a
complexidadedocódigodesenvolvido.
Pararelembrarsobreessadificuldade,najanelademanuten çãodosdados
defornecedores,docapítulo 5,ousuáriodigitavaloresem TextBoxs,estes
dadossãomapeadosparaumobjetodaclasse Fornecedore,emseguida,
aspropriedadesdesseobjetosãoobtidasparacomporumainstru çãoSQL
(insertou update)emuma string.Pararecuperá-los,umainstru ção
SQL selectétambémutilizada,seuresultadoémapeadoparaumobjetoda
classe Fornecedoreassuaspropriedadessãoatribuídasparaos TextBoxs.
Éprecisotambémdestacarque,alémdetodooprocessoapontadoante-
riormente,existemsitua çõesdevalida çãodosvaloresinformados,queainda
nãoforamapresentadasnemtrabalhadas. Umexemploseriaosvaloresde
nomeeCNPJdofornecedornãoseremvazios,eoCNPJserválido.Nanota
decompra,umavalida çãoseriaadatadeentradanãoserinferioràdeemissão
danota,eaquantidadecompradanãosermenorouigualazero.
Realizandoumaanálisenosproblemasapresentadosecomatecnologia
apresentadaatéomomento,conclui-sequeessasitua çãodeve-seaofatode
queosobjetosdenegócionãooferecemummeioparaliga çãodiretacom
ainterfacedousuário. Issotambémnãoocorrecomosdadosobtidosde
umabasededados.Sendoassim,entende-seanecessidadedeumobjetoque
229

## Página 246

6.5. Atualizandoabasededados CasadoCódigo
possarepresentarastabelas,relacionamentoseasrestri çõesdabasededados
equetambémpossaserfortementetipado,permitindoseuusotambémcomo
objetodenegócio.
Combasenestesproblemas,aMicrosoftpropõeumaarquiteturaqueuti-
lizaoDataSetcomoumobjetodenegócio,querepresentaasentidadesda
aplicação,pois,sendoeleindependentedeumabasededados–comovisto
noexemplointrodutóriodestecapítulo–,podeatenderbemàsnecessidades
apresentadasediscutidas.Paraisso,éprecisoqueoDataSetpossuatodauma
estruturasemelhanteaumabasededados,porém,conhecidocomoSchema
XML,equepossasercriadodemaneirasimplificadapeloVisualStudio.
6.5 Atualizando a base de dados
ParaaplicaroconceitodeDataSetTipado,novastabelasserãocriadas.Bus-
candoapresentarumanovaferramenta,serácriadaumabasededadosdireta-
mentenoservidordoSQLServerExpressetodoessetrabalhoserárealizado
pormeiodessaferramenta,queéo SQL Server Management Studio(SSMS).
ElapodeserbaixadademaneiraisoladadositedaMicrosoftou,dependendo
daversãodoSQLServerExpressquevocêinstalou,elapodejáestardisponi-
bilizadaemseuambiente.
Afigura6.4apresentaajanelainicialdo SSMS:
Fig.6.4:Autentica çãonoSQLServerManagementStudio
230

## Página 247

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
Onomedoservidorinformadonajaneladeautentica çãoéacomposi ção
donomedocomputadoremqueoSQLServerExpressfoiinstalado,com
umabarrainvertida(\)separando-odonomedainstânciadobanco,criada
duranteainstala ção. SQLEXPRESSéainstânciapadrão,casonãotenha
sidoalterada. Seaorealizaraautentica ção,ocorrerproblemasdeconexão,
verifiqueseoservi çoestáiniciado,comojáapresentadonocapítulo 5.
Comaconexãorealizadacomsucesso,éprecisocriarabasededados
paraaaplica ção. Todososprocessosdecria çãoemanuten çãoemobjetos
existentesnobancodedados(eemcadabasededados)podemserrealizados
pelajanela Object Browser(emportuguês,essajanelafoitraduzidapara
Pesquisador de Objetos),queéapresentadanafiguraaseguir.
Fig.6.5:Janelacomosobjetosexistentesnobancodedados
Paracriarabasededadosparaadefini çãodastabelasqueserãousadas,
cliquecomobotãodireitodomousesobreapasta Banco de Dados(que
atradu çãodeveriaserbasededados)e,então,em Novo Banco de Dados
(mesmaobserva çãoquantoàtradu ção).Umajanela,semelhanteàexibidana
figura6.6,seráapresentada.
231

## Página 248

6.5. Atualizandoabasededados CasadoCódigo
Fig.6.6:Janeladedefini çãodeparaacria çãodabasededados
Ajaneladafigura 6.6possuidiversascategoriaseinforma çõesquepodem
serpreenchidasparaacria çãodabasededados.Entretanto,paraofocodo
livro,bastainformaronomedela,queserá LivroDataBase.Apósinformar
onome,cliquenobotão OK,paraacria çãoserrealizada.
Apósaconclusãodacria çãodabasesedados,épossívelinserirastabelas
necessárias.Paraisso,expandaaguiadabasededadoscriadaecliquecom
obotãodireitodomousesobre Tabelase,então,em Nova Tabela. A
janelarepresentadapelafiguraaseguiréexibida.
232

## Página 249

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
Fig.6.7:Janeladefini çãodaestruturadeumatabela
Assumindoquenanovaaplica çãoqueserácriadaapartirdeagoraserão
necessáriasinformaçõesreferentesaoestadoecidadedeumfornecedor,crie
najaneladafigura 6.7aestruturaapresentadanafiguraseguinte:
Fig.6.8:JanelacomaestruturadefinidaparaatabelaEstados
Paraqueumcamposejadefinidocomochaveprimária,noSSMSclique
comobotãodireitosobreonomedacolunaecliqueem Definir Chave
Primária. Depois,éprecisodefinirqueovalorparaachaveprimária(o
campo idestado)seráautoincremento. Paraisso,najaneladeproprie-
dades,abaixodadefini ção,expandaapropriedade Especificação de
233

## Página 250

6.5. Atualizandoabasededados CasadoCódigo
Identidadeeatribua Simnasubpropridade (É Identidade),como
podeserverificadonafigura 6.8. Comtudodefinido,éprecisogravarata-
bela.Cliquenobotão Salvar,abaixodomenudajanela,ouem Arquivo
e Salvar Tabelaou,ainda, Ctrl-S.Umnomeserásolicitado.Informe
estecomo Estados.
Nasequência,seráprecisocriaratabela Cidades,deacordocomaes-
truturaapresentadanafigura 6.9,criandoocampodechaveprimária,mas
nãodefinindo-ocomoidentidade,nomomento.
Fig.6.9:EstruturaparaatabelaCidades
Umavezcriadaesalvaatabeladecidades,altereasubpropriedadeda
chaveprimáriaparaquesejaautoincrementoesalveatabela.Seapareceruma
mensagemdeerro,comoapresentadanafigura 6.10,seráprecisorealizaruma
configuraçãonoSSMS.
234

## Página 251

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
Fig.6.10:Mensagemdealertaparaaimpossibilidadedealteraraestruturada
tabela
Amensagemdeerro/alertaexibidanafigura 6.10refere-seàimpossibi-
lidadedeatualizaraestruturadatabela Cidades. Issoocorrepelofatode
ocampodechaveprimáriaalteraramaneiradepreenchimentodeseuva-
lor. Essaalteraçãopodecausarperdadedados,porissoaimpossibilidade.
Entretanto,épossívelconfiguraroSSMSparaquerealizeessaatualiza ção
quandoocorreressetipodeproblema. NomenudoSSMS,acesseaop ção
Ferramentasedepois Opções. Najanelaqueseráexibida,doladoes-
querdoselecioneacategoria Designersedesmarqueaop ção Evitar
alterações que exijam a recriação da tabela(figura6.11).
235

## Página 252

6.5. Atualizandoabasededados CasadoCódigo
Fig.6.11:Configura çãoparapermitiraltera çãodetabelasquesoframmodifi-
caçõesquecausemanecessidadederecriaratabela
Apósrealizadaaconfigura çãoindicada,cliquenobotão OKdajanelae
procedacomagrava çãodatabela,queocorreráperfeitamente.
Éprecisoagoraimplementarorelacionamentoentreastabelas Estados
e Cidades. Esserelacionamentosegueaideiaapresentadanocapítulo 5.
Entretanto,aimplementa çãonoSSMSéumpoucodiferente.Cliquecomo
botãodireitodomousesobreaáreadaestruturadatabelae,nomenuque
aparece,selecione Relacionamentos.Ajanelarepresentadapelafiguraa
seguirseráexibida.
236

## Página 253

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
Fig.6.12:Janelaparaadi çãoderelacionamentosentretabelas
Comajanelaativa,cliquenobotão Adicionar,paraqueoprocesso
deconfigura çãodorelacionamentocomecepelaexibi çãodamesmajanela,
porémcompropriedadesqueprecisamserconfiguradas(figura 6.13).
Fig.6.13:Janelaparaconfigura çãoderelacionamentos
Nas propriedades que aparecem ao lado direito, clique na categoria
237

## Página 254

6.6. CriandoosDataSetsTipadosnoVisualStudio CasadoCódigo
Especificação de Tabelas e Colunase,emseguida,nobotãoque
apareceaoladodireito.Comisso,umajanelaparatalespecifica çãoseráexi-
bida(figura6.14).
Fig.6.14:Configura çãodastabelasecolunasparaorelacionamentoaseradi-
cionado
Verifiquenadefini çãodastabelasecolunasqueatabela Estadoséatri-
buídacomoprimária,poiselatemosdadosdeestados,queserãonecessários
natabela Cidades.Destamaneira,achaveprimáriade Estadosestaráli-
gadacomocampo idestadodatabela Cidades,tornando-se,então,uma
chaveestrangeira.
6.6 C riando osDataSetsTipados noVisualStu-
dio
Crieumanovasolu ção,chamada SolutionDataSetTipado. Nela,crie
umprojeto Windows Formschamado DataSetTipadoProject. Apa-
gueoformuláriocriadopelotemplateecrienoprojetoumapasta( folder)
chamada DataSets.Cliquenonomedapastacomobotãodireitodomouse
238

## Página 255

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
eescolhaaop ção Adde New Item. Nacategoria Data,escolhaaop ção
DataSet,dêonomede DSEstadosECidadesparaoarquivoeconfirmea
criação.Umajanela,representadapelafiguraaseguir,seráexibida.
Fig.6.15:ÁreadedesenhodoDataSetTipado
AáreadedesenhoparaDataSetsTipadosésemelhanteàáreadedesenho
deumformulário,noquedizrespeitoàversatilidadedopadrãoarrastare
soltar,emboraoscomponentespossamserinseridoseconfiguradosdema-
neiraisolada. Oprimeiropassoparaadefini çãodastabelasquecomporão
esteDataSetédisponibilizarno Server Explorer,osobjetosdabasede
dadosdesejada.Paraisso,naguiado Server Explorer,cliquenobotão
Connect to DataBase(osegundobotão,daesquerdaparaadireita)e,
então,ajaneladispostanafiguraaseguirseráexibida.
239

## Página 256

6.6. CriandoosDataSetsTipadosnoVisualStudio CasadoCódigo
Fig.6.16:Definindoafontededadosparaaconexão
Noteque,pordefini ção,conexõescomoutrosbancosdedados,alémdo
SQLServer,estãodisponibilizadas. Paracontinuar,selecione Microsoft
SQL Server,comomostraafigura 6.16ecliqueemcontinuar,paraquea
janeladaetapaseguintesejaexibida(figura 6.17).
240

## Página 257

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
Fig.6.17:Estabelecendoparâmetrosparaaconexãocomabasededados
Nessajanela(figura 6.17),éprecisoinformaroservidor(máquina)ea
instânciadoSQLServerExpress,damesmamaneiraquefoiinformadopara
oacessoaoSSMS.Apósisso,seleciona-seabasededadosquedesejaconectar
e,então,pode-seclicarem Test Connection,oufinalizaraconfigura ção,
clicandonobotão OK.Comisso,abasededadosetodosseusobjetosficam
disponibilizadosno Server Explorer,comopodeserverificadopormeio
dafigura6.18.
241

## Página 258

6.6. CriandoosDataSetsTipadosnoVisualStudio CasadoCódigo
Fig.6.18:ObjetosdisponibilizadosnoServerExplorerreferentesàconexão
criada
Agora,comajaneladoDataSetTipadovisívelnoIDE,arrasteasduas
tabelas( Estadose Cidades)paraasuaáreadedesenho. Comisso,o
DataSetdeveráestarsemelhanteaoapresentadonafiguraseguinte:
Fig.6.19:DataSetTipadocriadocomduastabelasmapeadas
242

## Página 259

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
6.7 Entendendo os componentes do DataSetTi-
pado
CadatabelamapeadadabasededadosparaoDataSetécompostapordois
componentes:um DataTableeum TableAdapter.O DataTablere-
presentaaestruturadecamposdatabela,cujosnomessãoexibidosnafi-
gura6.19. JáoTableAdapterencapsulaneleaintera çãocomabasede
dados,paraatualizareobterdados.Lembrandootrabalhadonocapítulo 5,
o TableAdapterfazusodeobjetos SqlConnectione SqlCommands,
comopodeserverificadonajaneladepropriedadesdo TableAdapterde
Estados,o EstadosTableAdapter(figura6.20).
Fig.6.20:PropriedadesdoTableAdapterdeFornecedores
243

## Página 260

6.7. EntendendooscomponentesdoDataSetTipado CasadoCódigo
Veja,nafigura6.20,que,paraoobjeto EstadosTableAdapter,exis-
temconfigura çõesparaaspropriedades Connection, DeleteCommand,
InsertCommandeas SelectCommande UpdateCommand,quenãoapa-
recemnafigura.Casoapare çaapenaso SelectCommand,vocênãodeveter
definidoumachaveprimáriaparaatabela.Paraestemomento,arecomen-
daçãoéeliminaroarquivode DataSet,atualizaraestruturadastabelase
criarnovamenteo DataSet.
As subpropriedades de Connection estão definidas no arquivo
App.config,quefoimodificadoquandoaconexãocomabasededados
foicriada. Asinstru çõesdaspropriedades CommandTextforamdefinidas
combaseemtodososcamposdatabelaarrastada. Essescampospoderiam
serapenasalguns. Paraomomento,procurenãorealizarmodifica çõesnas
configuraçõescriadasautomaticamente.
Aspropriedadesparao DataTablesãoapenas3,dispensandoane-
cessidadedeumafigura. Entretanto,éinteressanteapresentarumafigura
paraaspropriedadesparaumacoluna,eafigura 6.21mostraasdacoluna
(DataColumn) idestado.
244

## Página 261

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
Fig.6.21:Propriedadesdacolunaidestado
NoDataSetTipado,alémdepodervisualizarastabelasmapeadas,épos-
sívelidentificarqueorelacionamentocriadotambémfoimapeadocomoum
DataRelation.Casoesserelacionamentonãoapare ça,vocêseesqueceude
criá-lonabasededados. Paraestemomento,arecomenda çãoéeliminaro
arquivode DataSet,atualizaraestruturadastabelasecriarnovamenteo
DataSet.
6.8 C riando um formulário que faz uso de um
DataSetTipado
Na Solution Explorer,noprojetocrieumapastachamada Formse
dentrodelaoutrachamada CRUDs. Dentrodesta,crieumformuláriocha-
mado FormEstados. Comonovoformuláriovisível,abraajanela Data
245

## Página 262

6.8. CriandoumformulárioquefazusodeumDataSetTipado CasadoCódigo
Sources(Menu View  Other Windows  Data Sources).Suaja-
neladeveráestarsemelhanteàapresentadapelafiguranasequência.
Fig.6.22:Propriedadesdacolunaidestado
Umaobserva çãoextremamenteimportanteéque,pararealizaroqueserá
apresentadoagora,éprecisoqueoformulárioquereceberáoscomponentes
do DataSetestejavisível. Comessainforma ção,notequeoprimeiroele-
mentodaárvoreexibidanajanelaé DataSets,queserefereàpastaonde
oDataSetTipadofoicriado. Logoabaixo,encontra-seopróprio DataSet
( DSEstadosECidades)e,dentrodeste,elementotodosos DataTables
neleexistentes.
Paracada DataTable,umarela çãodecolunaséexibida.Épossívelve-
rificaraocorrênciaduplicadade Cidades,que,narealidadenãoéumadu-
plicidade. Cidades,queestádentrode Estados,narealidaderepresenta
orelacionamentoentreasduastabelas.Poderia-sedizerque Cidades,que
estáabaixodo DataSet,refere-seatodososregistrosdatabelae, Cidades,
quepertencea Estados,trarásempreapenasascidadesparaoestadoatual.
Osíconesaoladodecadanome,tantodastabelascomodoscampos,
possuemumasemântica,queestádiretamenteligadaa comoosdadosserão
exibidosaousuário,ouseja,quaiscontrolesdevemsercriadosnoformulá-
rio. Comoajanelaqueserácriadaérelacionadaao CRUDde Estados,é
246

## Página 263

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
importantequeotemplateparaoscontrolessigamessaideiaeque,como
o IDdecadafornecedoréautoincremento,nãohánecessidadedeeleser
um TextBox.Realizeasaltera çõesclicandononomedatabelaenonome
docampo,eescolhaqualcontroleusará. Paraatabela Estados,escolha
Detailseparao idestado,escolha Label.Essamudan çapodeserveri-
ficadanafiguraseguinte.
Fig.6.23:Defini çãodecontrolesvisuaisparaatabeladeEstados
Comadefini çãoconcluída,cliquenonomedatabelade Estadosea
arrasteparaaáreacentraldoformulário.Oresultadodevesersemelhanteao
exibidonafiguraaseguir:
247

## Página 264

6.8. CriandoumformulárioquefazusodeumDataSetTipado CasadoCódigo
Fig.6.24:ÁreadedesenhodoformuláriocomcontrolesvinculadosaoData-
Set
Notenafigura 6.24queaáreadedesenhofoidivididaemduaspartes,
avisualenãovisual,quejáhaviasidotrabalhadanocapítulo 2. Naáreade
controlesnãovisuais,noteaexistênciadeobjetosreferentesao DataSet,ao
BindingSourceeao TableAdapter.Essescontrolesjásãoconhecidos,
entretanto,agorasãoutilizadosdemaneiravisual,commaiorprodutividade.
Doiscontrolesnovossãoapresentados:o TableAdapterManager,quege-
renciaafuncionalidadedesalvardadosrelacionados,organizandoaordem
de inserts, updatese deletes;eo BindingNavigator,queserefere
àbarradenavega çãolocalizadanoiníciodajanela.
Aliga çãodoscontrolescomoDataSetérealizadapormeiodapropri-
edade DataBindingsdecadacomponente,quepodeservistanafiguraa
seguir:
248

## Página 265

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
Fig.6.25:PropriedadeDataBindingsdoscontrolesvisuaisligadosaoDataSet
Verifiquequeasubpropriedade Text,de DataBindings,temumali-
gaçãocomo BindingSource,poiséelequeforneceosdadosvindosda
basededadoseosenviaparaela. Cliquena ComboBoxevejacomosedá
estaconfigura ção,representadaaseguirpelafigura:
Fig.6.26:Configura çãodapropriedadeText,deDataBindings
249

## Página 266

6.8. CriandoumformulárioquefazusodeumDataSetTipado CasadoCódigo
Verifiquenaspropriedadesdoobjeto estadosBindingSourcequeo
DataSourceéo DataSet,eo DataMemberéa DataTable,seguindoa
mesmaideiadoapresentadonoiníciodestecapítulo,porém,demaneiramais
simples,ágilevisual(figura 6.27).
Fig.6.27:Configura çãodapropriedadeText,deDataBindings
Paraquealgunstestessejamrealizados,insiraalgunsregistrosnatabela
de Estadospelo Server Explorer,damesmamaneiraquefoifeitono
capítulo5.Sequiser,podetambéminserirpeloSSMS,quetemamesmafun-
cionalidade.Afigura6.28apresentaosdadosinseridospormeiodo Server
Explorer.
250

## Página 267

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
Fig.6.28:DadosparatestesinseridosnatabelaEstados
Altereaclasse Program,parainstanciaroformuláriocriado,e,então,
executeaaplica ção,quedeveráapresentarumformuláriosemelhanteaoexi-
bidonafigura 6.29. Notequenaclasse Programseránecessárioinseriro
usingreferenteao Namespacedoformulário,queédiferentedeondeestá
essaclasse.
Fig.6.29:Janelaparamanuten çãonosdadosdofornecedor
Parafacilitarostestes,crieumajanelacommenusparaacessaremosfor-
muláriosqueforemsendocriadosaodecorrerdestecapítulo.
251

## Página 268

6.9. Entendendoocomportamentodoformulárioemrela çãoaosseuscontroleseaoDataSetCasadoCódigo
6.9 E ntendendo o comportamento do formulá -
rio em relação aos seus controles e ao Da-
taSet
Oprimeiropontoaserexplicadoéemrela çãoacomoosdadosdatabela
jáaparecemnoformulário. Lembre-sedequeo DataSetgeraumobjeto
queresidenamemóriaRAMdocomputador,ouseja,nãotemvínculodireto
depersistênciacomabasededados. Destamaneira,paraqueo DataSet
tenhaosdadosdetabelasmapeadas,éprecisopopulá-lo. Estaopera çãoé
realizadanomomentoemqueoformulárioécarregado( Load),comopode
serverificadonasequência.
Resolução6.7:métodoquecapturaoeventoLoaddoformulário
private void FormEstados_Load ( object sender, EventArgs e) {
// TODO: This line of code loads data into the
// 'dSEstadosECidades.Estados' table. You can move, or
// remove it, as needed.
this .estadosTableAdapter.Fill(
this .dSEstadosECidades.Estados);
}
Quandoocorreuoprocessodearrastaroscontrolesdo DataSource
para a área do formulário, o Visual Studio inseriu também alguns códi-
gos, sendo um deles para o eventoLoad do formulário. A primeira
parteérelacionadaaumcomentáriodeorienta çãosobrealinhainserida.
Essalinhatemachamadaaométodo Fill()do adapterdeestados(
estadosTableAdapter)erecebecomoargumentoo DataTabledees-
tados( estadosDataTable),quepertenceao DataSet. Essemétodoé
criadoautomaticamentepeloVisualStudioquandoummapeamentoécri-
adonaáreadedesenhodo DataSet,easuainvoca çãoremeteàexecu çãode
umainstru ção SELECTnabasededados,queestáinseridanapropriedade
SelectCommanddo TableAdapterdeestados. Essemétodo( Fill())
podeservisualizadoabaixodo TableAdapter,juntamentecomométodo
GetData(),queretornaum DataTable.
252

## Página 269

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
Asegundafuncionalidadeasertestadaeexplicadaéemrela çãoàinser-
çãodenovosdados.Executeaaplica çãoecliquenobotãoqueadicionaum
novoregistro.Nessenovoregistroinserido,vejaqueo Idrecebeumvalor
negativo.Preenchaosdadosecliquenobotãoresponsávelpelagrava ção(os
hintspodemseralteradosnormalmentepormeiodajaneladepropriedades).
Notequeo Idpassouaserpositivo,sendoexatamenteovalorseguinteao
Iddoúltimoregistro.
Verifique a propriedade AutoIncrementSeed da DataColumn
idestado, na DataTablede Estadosno DataSetcriado. O va-
lor é -1. Isso significa que sempre que os dados forem carregados (mé-
todo Fill()),essevalorservirádebase.Verifiquetambémapropriedade
AutoIncrementStep,queétambém-1. Comestainforma ção,acadain-
serçãoderegistro,ovalorparao Idaumentanegativamente.Quandoocorre
agrava çãodoregistro,háumaatualiza çãonabasededados,oquecausaa
realinser çãodosdadosnela.Vejaquetragonasequênciaocódigodoevento
Clickdobotãodegrava ção.
Resolução6.8:métodoquecapturaoeventoClickdobotãodegra-
vação
private void estadosBindingNavigatorSaveItem_Click ( object
sender, EventArgs e) {
this .Validate();
this .estadosBindingSource.EndEdit();
this .tableAdapterManager.UpdateAll(
this .dSEstadosECidades);
}
Aprimeirainstru çãorealizaumprocessodevalida çãonocontroleque
temofoconomomentodagrava ção.Essavalida çãosedápelodisparonos
eventos Validatinge Validated.Achamadaaométodo EndEdit()
realizaatualiza çõespendentesno DataSourcedocontrole. Finalizando,
achamadaaométodo UpdateAll()do tableAdapterManagerinvoca
osmétodosdeatualiza çõesdos TableAdaptersexistentesnoformulário,
enviandoo DataSetondeasaltera çõesfísicasdevemocorrer. Nestemo-
mento,identifica-seoquefoifeitolocalmenteeosrespectivos commandsdo
253

## Página 270

6.10. Criandoumformulárioutilizandodadosdeumrelacionamento CasadoCódigo
TableAdaptersãoinvocados. Podemserchamadosos commandstanto
parainser ção,atualiza çãoouexclusão,dependendosempredonúmeroeti-
posdeatualiza çõesqueforamrealizadaslocalmente.
Pararealizarumúltimoteste,executeaaplica ção,alterealgunsdados,e
excluaalgunsregistroseinsiraoutros.Assim,fecheaaplica çãosemsalvare
execute-anovamente.Vejaquenenhumadasmudan çasquefezfoipersistida
nobanco. Emseguida,refa çaasmesmasopera çõesegraveantesdefechar.
Executenovamenteaaplica çãoeconstatequetodasasmudan çasforamgra-
vadasdeumaúnicavez.
6.10 Criando um formulário utilizando dados
de um relacionamento
Orelacionamentoentreastabelas Estadose Cidadesimplicanaexistência
deumaoumaiscidadesparacadaestado,equecadacidadeprecisadeum
estado. Destamaneira,naimplementa çãodajanelareferenteao CRUDde
cidades,seráprecisoqueousuárioinformeoestadodecadacidadeaser
inserida,tendocomobaseosestadosjáarmazenados.
Crieumnovoformulárionapasta CRUDs,dentrodapasta Forms,edê
aeleonomede FormCidades. Comoformuláriovisível,acesseajanela
DataSources.Clicandononomeda DataTable Cidades,altere-apara
Details.Alterea DataColumn idcidadepara Label,ea idestado
para ComboBox.Arrastea DataTableparaaáreadedesenhodoformulá-
rio.Naclasse Program,definaonovoformulárioparaserexibidoeexecute
aaplica ção(secriouajanelacommenus,acessepormeiodeles). Atelade
suaaplica çãodeverásersemelhanteàapresentadanafiguraaseguir.
254

## Página 271

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
Fig.6.30:JaneladocadastrodeCidades,comumComboBoxparaselecionar
estados
Observe na figura 6.30 que, ao inserir uma nova cidade e clicar no
ComboBox, não aparecem os estados já gravados. Para configurar o
ComboBoxparaexibirosestadosjágravados,comajaneladecidadesvisí-
vel,váàjanela DataSources,cliquena DataTabledeestados,arraste-a
atéo ComboBoxesolte-a.Após,cliquena Smart Tagdo ComboBoxesua
janeladeverásersemelhanteàapresentadanafiguraseguinte.
Fig.6.31:Configura çãodoComboBox
Quando houve o processo de “arrastar e soltar” (drag and drop) do
255

## Página 272

6.10. Criandoumformulárioutilizandodadosdeumrelacionamento CasadoCódigo
DataTabledeestadosparao ComboBox,oVisualStudiorealizouaconfigu-
raçãobásicadocomponente.Primeiramente,aferramentamarcouaop ção
Use Data Bound Items,queinformaaocontrolequeosdadosforneci-
dosporeleserãoligadosaumafontededados,enãodigitadosdemaneira
estática.Emseguida,configurou-seafontededados,o Data Source.
Quandoo DataTabledecidadesfoiarrastado,foicriadoparaeleum
BindingSourcecomofontededadosparacidades.Afigura 6.32mostraa
seleçãodo BindingSource,sefosserealizadademaneiramanual.
Fig.6.32: Verificandoasele çãodemaneiramanualdoBindingSourcepara
umComboBox
Todososobjetos BindingSourcesqueconstamnestajaneladeconfi-
guraçãoexistemnoformulárioativo.Em Other Data Sources,épossível
obterobjetosqueexistemnoprojeto.Selecionandoum BindingSourcedo
projeto,umobjetoreferenteaeleécriadonoformulárioativo.
A ComboBoxreferenteao Display Memberrefere-seàsele çãodequal
DataColumnforneceráodadoqueseráexibidonalistadeitensdocontrole.
Vejaqueaconfigura çãofeitapeloarrastaresoltardefiniua UF,masocorreto
256

## Página 273

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
seria NOME.Procedacomacorre ção.
A ComboBoxreferenteao Value Membertratada DataColumnque
temovalorreferenteàchaveprimáriadodadoselecionadopelousuário.
Quantoà ComboBox Selected Value,elarefere-seà DataColumnda
DataTablequereceberáovalorselecionado,querepresentaachaveestran-
geira,mantendoaassocia çãoentreosobjetos.
Comtodaaconfigura çãorealizadaeexplicada,executeagoraaaplica ção,
insiraumnovoregistroeselecioneumestadoparaanovacidade(figura 6.33).
Fig.6.33:Visualizandoosestadospreviamentecadastradosparasele çãoem
umComboBox
Comoépossívelverificar,osnomesdosestadosapresentadosparasele ção
no ComboBoxnãoestãoemumaordemalfabética,oquepodedificultara
buscaporpartedousuário.Oprimeiropontopararealizarestamudan çaésa-
berondeestáocorrendoarecupera çãodosdadosquepopulamo ComboBox
(vistonasequência).
Resolução6.9:métodoLoadquepopulaosDataTablesdoformu-
lário
private void FormCidades_Load ( object sender, EventArgs e) {
this .estadosTableAdapter.Fill( this .dSEstadosECidades.
Estados);
this .cidadesTableAdapter.Fill( this .dSEstadosECidades.
257

## Página 274

6.10. Criandoumformulárioutilizandodadosdeumrelacionamento CasadoCódigo
Cidades);
}
Observe que, além da chamada ao métodoFill() enviando o
DataTable Cidadescomoargumento,háagoraumanovachamadaao
mesmométodo,porémenviandoo DataTabledeestados. Identificando
comoo DataTableépopulado,éprecisoadaptarométodo,oucriaroutro
quecarregueosregistroscombaseemumaclassifica ção,quenestecasoéo
nomedosestados.No DataSet,cliquecomobotãodireitodomousesobre
osnomesdosmétodosabaixodo TableAdapterde Estados(figura6.34).
Fig.6.34:MenudecontextodoTableAdapter
Omenudecontextoparao TableAdapterpossuiumaop çãoparacri-
açãodenovosmétodos,queéa Add Query.... Confirmeessaopçãoea
janelaparacria çãodeumanovaconsultaéapresentada(figura 6.35).
258

## Página 275

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
Fig.6.35:Janelaparasele çãodotipodeCommandqueserácriado
Aconsultaqueserácriadaésemelhanteàcriadaautomaticamenteparao
métodoFill(),eelafazusodainstru ção SELECTdaSQL.Destamaneira,
marqueessaop ção(queéapadrão)ecliquenobotão Next. Assim,uma
novajanelaaparece(figura 6.36).
259

## Página 276

6.10. Criandoumformulárioutilizandodadosdeumrelacionamento CasadoCódigo
Fig.6.36:Sele çãodotipodeinstru çãoaserexecutadapeloCommand
Com a opção padrão marcada, que é umSELECT que retorna
muitas linhas e/ou colunas,cliquenobotão Nexteumanovaja-
nelaéapresentada(Figura6.37).
260

## Página 277

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
Fig.6.37:Instru çãoqueseráexecutadapelométododoCommand
Nainstru çãoSQLapresentada,épossívelrealizaradapta çõesdamaneira
quedesejarouprecisar.Éimportantesaberquenãosedevemmudaroscam-
posqueserãoselecionados,poisoretornoseráparao DataTablejáexis-
tente. Insiraaofinaldainstru çãoacláusula“ORDER by nome”. Casoseja
desejáveltodaacria çãodainstru ção,podeserrealizadapelajanelaquese
exibequandosepressionao Query Builder....Concluindoamudan ça,
pressioneobotão Nexteajaneladafigura 6.38éapresentada.
261

## Página 278

6.10. Criandoumformulárioutilizandodadosdeumrelacionamento CasadoCódigo
Fig.6.38:DefinindoosnomesparaosmétodosqueserãocriadosnoTableA-
dapter
Nosnomesqueaparecemcomosugestãoparacadamétodo, existeo
sufixo By; complete o nome com o do campo que classifica a seleção.
Nestecaso, ométodoquepopulauma DataTabledeveráserchamado
de FillByNome(). Desmarque a opção do método que retorna uma
DataTable, ela não será necessária. Neste momento, você pode clicar
diretamente no botãoFinish. Verifique agora que, nos métodos do
TableAdapterde Estados,constaonovométodocriado.Adapte,nomé-
todoquecapturaoevento Loaddoformulário,paraque,emvezdechamar
ométodo Fill(),sejaagorachamadoométodo FillByNome().Execute
aaplica ção,insiraumanovacidadee,aoselecionaroestado,vejaqueagora
aparecememordemalfabética.
262

## Página 279

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
6.11 Concluindo os formulários para a aplica -
ção de compra e venda
Combasenoquefoiapresentadonestecapítulo,algumastabelasserãocria-
dasoumodificadas,tendosemprecomoexemploabasededadosdocapítulo
5.Comoprimeiraatividade,crieatabela Fornecedores(figura6.39).Essa
tabela,nesteexemploconteráumrelacionamento(figura 6.40)comatabela
Cidades.Lembre-sedeconfigurarachaveprimáriaparaseridentidade(au-
toincremento).
Fig.6.39:EstruturaparaatabelaFornecedores
Fig.6.40:RelacionamentoentreastabelasFornecedoreseCidades
263

## Página 280

6.11. Concluindoosformuláriosparaaaplicaçãodecompraevenda CasadoCódigo
Comatabelacriada,éprecisoagoralevá-laparaaaplica ção.Deixeaber-
tasasjanelasdo DataSetedo Server Explorer,encontreatabelaea
arrasteparao DataSet(figura6.41).
Fig.6.41:DataSetcomanovatabeladeFornecedoreseorelacionamentocom
Cidades
No TableAdapterdatabeladecidades,adicioneumnovométodo,cha-
mado FillByNomeComUF()(figura6.42).Eleseráusadoparaexibironome
dacidadeno ComboBoxda Cidade,najanelade Fornecedores,seguida
daUFdoestadoaqueelapertence,como: Foz do Iguaçu (PR).
Fig.6.42:Instru çãoSELECTparaobten çãodonomedacidadecomaUFde
origem
264

## Página 281

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
Como,aoladodonomedacidade,éprecisoobteraUFreferenteaela,e
estainforma çãonãoestánatabeladecidades–focoprincipaldo SELECT–,
éprecisotrazerparao SELECTatabeladeestadostambém.Estaopera çãoé
feitapelacláusula INNER JOIN,naqualelarecebecomoargumentoachave
estrangeiraqueseráligadaàchaveprimáriadatabelado INNER JOIN.
Asassocia çõesinternas(ou INNER JOIN)combinamtabelascompa-
randovaloresemcolunasquesejamcomunsaambasastabelas.Oresultado
paraumaconsulta,fazendousodessacláusula,retornasomenteregistrosque
correspondamàscondi çõesdaassocia ção. Destamaneira,casoexistamre-
gistrosque,nascolunasespecificadas,nãocorrespondamàopera ção,elesnão
farãopartedoresultadoobtido.
Casodeseje,o INNER JOIN,ouqualquertipoderelacionamentoousele-
çãodedadosaseremretornados,podeserimplementadopormeiodajanela
Query Builder.Paraisso,cliquenobotãoqueaexibeeajaneladafigura
6.43éapresentada.
Fig.6.43:Janelaparacria çãodeconsultasdemaneiravisual–QueryBuilder
Pormeiodajanela Query Builder,épossívelalterardiretamentea
265

## Página 282

6.11. Concluindoosformuláriosparaaaplicaçãodecompraevenda CasadoCódigo
instruçãoSQLoufazerusodorecursovisual,característicoemaplica ções
Windows. Cliquecomobotãodireitodomousesobreaáreaemqueapa-
receodesenhodatabela Cidades,selecione Add Table,escolhaatabela
Estados,cliquenobotão Adde,então,em Close(figura6.44).
Fig.6.44:FormuláriodeFornecedorescomComboBoxpersonalizadopara
seleçãodaCidade
Nanovatabelaqueapareceu,selecioneacoluna UF.Adapteainstru ção
SELECTparaquefiqueigualaapresentadaanteriormente,nafigura 6.42.Cli-
quenobotão OKedepoisem Finishparafinalizar.
Agora,paracriarainterfacedeintera çãocomousuário(ajanela),crie
umnovoformuláriopara Fornecedores–napastaCRUDs–(figura6.45),
seguindoamesmasitua çãoapresentadaparaoformuláriode Cidades.No
ComboBoxde Cidade,arraste,dajanela Data Sources,o DataTable
de Cidades. Adapteométododoevento Loadparachamarométodo
anteriormentecriado(vistonasequência).
266

## Página 283

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
Fig.6.45:FormuláriodeFornecedorescomComboBoxpersonalizadopara
seleçãodaCidade
Resolução6.10:métodoLoadquepopulaosDataTablesdoformu-
lário
private void FormFornecedores_Load ( object sender, EventArgs e){
this .cidadesTableAdapter.FillByNomeComUF( this .
dSEstadosECidades.Cidades);
this .fornecedoresTableAdapter.Fill( this .
dSEstadosECidades.Fornecedores);
}
Comainten çãodepraticarmaisaimplementa çãoderelacionamentos,
aaplica çãodestecapítulotrarápara Produtosacategoriza çãoemgrupos.
Destamaneira,crieumatabelade Grupos(figura6.46)eumade Produtos
(figura6.47),eatribuaaelasumrelacionamento(figura 6.48). Novamente,
lembre-sedeatribuirapropriedadedeidentidadeàschavesprimárias.
Fig.6.46:EstruturaparaatabeladeGruposdeProdutos
267

## Página 284

6.11. Concluindoosformuláriosparaaaplicaçãodecompraevenda CasadoCódigo
Fig.6.47:EstruturaparaatabeladeProdutos
Fig.6.48:RelacionamentoentreastabelasdeGruposeProdutos
Comastabelaseseusrelacionamentoscriados,opassoseguinteélevar
paraaaplica çãoessastabelas.Destamaneira,deixeasjanelasdo DataSete
Server Explorerativas,earraste-asparaaáreadedesenhodo DataSet.
No TableAdapterde Grupos,crieumnovométodoparaclassificara
seleçãoporordemdonomedogrupo,talqualfoifeitopara Cidades(figura
6.49).
268

## Página 285

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
Fig.6.49:TabelaserelacionamentosdeGruposeProdutosinseridosnoDa-
taSet,comométodoFillByNome()jácriado
Opassofinalparaotrabalhoreferentea Grupose Produtoséacri-
açãodosrespectivosformulários(figuras 6.50e6.51). Crieumformulário
paracadatabela,ativeajanela Data Sources,configureoscomponentese
arraste-osparaaáreadedesenho.Apósisso,najanelade Produtos,adapte
ométodoquecapturaoevento Loaddoformulário,paraquefa çausodo
novométododepopula çãodo DataTablede Grupos,quepreencheráo
ComboBox.Vejaissonasequência.
Fig.6.50:Formulárioparamanuten çãoeregistrosdegruposdeprodutos
269

## Página 286

6.11. Concluindoosformuláriosparaaaplicaçãodecompraevenda CasadoCódigo
Fig.6.51:Formulárioparamanuten çãoeregistrosdeprodutos
Resolução6.11:métodoLoadquepopulaosDataTablesdoformu-
lário
private void FormProdutos_Load ( object sender, EventArgs e) {
this .gruposTableAdapter.FillByNome( this .
dSEstadosECidades.Grupos);
this .produtosTableAdapter.Fill( this .
dSEstadosECidades.Produtos);
}
Comoumadicionalparaestecapítulo,aaplica çãopropostaoferecerá
tambémajanelaparavendasenãoapenasentrada(compra)deestoque.
Destamaneira,faz-senecessáriaumatabelade Clientes(figura6.52),com
suarespectivadisponibiliza çãono DataSet(figura6.53),eoformuláriopara
interaçãocomousuário(figura 6.54). Atualizeométododoevento Load
paraobterosdadosdométodoquepopularáo ComboBoxdecidades,criado
parao TableAdapterde Cidades.Vejaocódigoaseguir.
270

## Página 287

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
Fig.6.52:EstruturaparaatabeladeClientes
Fig.6.53:DataTabledeClientescomDataRelationparaCidades
Fig.6.54:Formulárioparamanuten çãodosdadoseregistrodeClientes
Resolução6.12:métodoLoadquepopulaosDataTablesdoformu-
lário
private void FormClientes_Load ( object sender, EventArgs e) {
this .cidadesTableAdapter.FillByNomeComUF( this .
dSEstadosECidades.Cidades);
this .clientesTableAdapter.Fill( this .
271

## Página 288

6.11. Concluindoosformuláriosparaaaplicaçãodecompraevenda CasadoCódigo
dSEstadosECidades.Clientes);
}
Ajanelaparaoregistrodeumanotadeentradaeseusprodutosseráaper-
feiçoadanestecapítulo,fazendousodosrecursosoferecidospelo DataSet.
Oprimeiropassoéacria çãodastabelasde NotasdeEntrada(figura6.55)
ede ProdutosNotasdeEntradas(figura6.57),eseusrespectivosrelacio-
namentos(figura6.56,6.58e6.59).
Fig.6.55:EstruturaparaatabeladeNotasdeEntrada
Fig.6.56:RelacionamentoentreastabelasdeNotasdeEntradaeFornecedores
272

## Página 289

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
Fig.6.57:EstruturadatabeladeProdutosparaNotasdeEntrada
Fig.6.58:RelacionamentoentreastabelasdeProdutosdeNotasdeEntradae
NotasdeEntrada
Fig.6.59:RelacionamentoentreastabelasdeProdutosdeNotasdeEntradae
Produtos
Comtodasastabelaseseusrespectivosrelacionamentosjácriados,faz-
senecessáriodisponibilizaressastabelasno DataSet. Novamente,como
DataSeteajanela Server Explorervisíveis,arrasteastabelasdenotas
deentradaeprodutosdenotasdeentradaparao DataSet(figura6.60).
273

## Página 290

6.11. Concluindoosformuláriosparaaaplicaçãodecompraevenda CasadoCódigo
Fig.6.60:Tabelaserelacionamentosrelacionadosàsnotasdeentrada
Najaneladeregistrodenotasdeentrada,seráfeitousodosrecursosdis-
ponibilizadospelo DataSet.Destamaneira,najanelade Data Sources,
configureo DataTabledenotasdeentrada,comomostraafiguraaseguir:
Fig.6.61:Configura çãodoDataTabledenotasdeentradaparadesenhoecon-
figuraçãodoformulário
Arrasteo DataTable NotasDeEntradaparaoformulário,configure
o ComboBoxde Fornecedoresparareceberosdadosdo DataTable
Fornecedoreseos DateTimePickersparaoformato Short. Acon-
figuraçãoinicialparaoformuláriodeverásersemelhanteaoapresentadona
274

## Página 291

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
figuraseguinte.
Fig.6.62:DesenhoinicialparaajaneladeNotasdeEntrada,comdadosda
nota
Asegundapartedajanelapararegistrodasnotasrefere-seàinforma ção
dosprodutosadquiridosnacompra.Umprimeiropassoédisponibilizar,por
meiodeum DataGridView,naáreaabaixodosdadosglobaisdanota,a
relaçãodeprodutosexistentesemcadanota,assimcomoapossibilidadede
inserção,remo çãoealtera çãodessesprodutos.Destamaneira,éprecisoque
osregistrosexibidosnanotaapresentemonomedoproduto,enãoseucódigo.
Arraste na área livre do formulário o controleGroupBox (den-
tro da categoria Containers da ToolBox). Dentro dele, arraste
um BindingNavigator (dentro da categoria Data da ToolBox)
e, abaixo do Navigator, arraste a DataTable de produtos da
nota de entrada, que está dentro daDataTable de notas de en-
trada. Na propriedade BindingSource do Navigator, selecione
produtosNotaDeEntradaBindingSource – ou o nome que tenha o
DataSourcedo DataGridViewparaprodutosdanotadeentrada,quefoi
criadoquandoorespectivo DataTablefoiarrastado.Aofinal,seuformu-
láriodeveestarsemelhanteaoapresentadonasequênciapelafigura:
275

## Página 292

6.11. Concluindoosformuláriosparaaaplicaçãodecompraevenda CasadoCódigo
Fig.6.63:Janeladenotasdeentradacomcontrolesparamanuten çãodospro-
dutosdasnotas
Comotodososcamposforaminseridosenãoseránecessáriaapresen ça
detodosnogrid, na SmartTagdo DataGridView, cliqueem Edit
Columns. Deixeapenasascolunas: idproduto, precocustocompra
e quantidadecomprada. Napropriedade HeaderTextdessascolunas,
deixe, respectivamente: Descrição, Custoe Quantidade. Naco-
luna idproduto/Descrição, napropriedade ColumnType, selecione
DataGridViewComboBoxColumn. Estetipodecolunatornaráacoluna
idproduto/Descriçãoum ComboBox,sendopossívelselecionaropro-
dutoaserinserido,diretamentedatabeladeprodutos. Finalizeaaltera ção
clicandonobotão OKeoformulárioagoradeveráestarsemelhanteaoda
figuraaseguir:
276

## Página 293

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
Fig.6.64:Janeladenotasdeentradacomcontrolesparamanuten çãodospro-
dutosdasnotasconfigurados
Paraaimplementa çãodaconfigura çãodo ComboBox,crieumnovomé-
todono TableAdapterdeprodutosparasele çãodosdados,porordemda
descriçãodosprodutos. Na ToolBox,logonoinícioexisteumacategoria
comonomedoprojetoe,dentrodela,existeo TableAdapterdeprodutos;
arraste-oparaaáreadecontrolesnãovisuaisdoformulárioetireonúmero1
aofinaldeseunome.Emseguida,implemente/altereocomportamentopara
ométodoquecapturaoevento Loaddoformulário,damaneiraapresentada
aseguir.
Resolução6.13:métodoLoadquepopulaosDataTablesdoformu-
lário
private void NotaDeEntrada_Load ( object sender, EventArgs e) {
this .produtosTableAdapter.FillByDescricao(
this .dSEstadosECidades.Produtos);
this .produtosNotaDeEntradaTableAdapter.Fill(
this .dSEstadosECidades.ProdutosNotaDeEntrada);
this .fornecedoresTableAdapter.Fill(
this .dSEstadosECidades.Fornecedores);
this .notasDeEntradaTableAdapter.Fill(
277

## Página 294

6.11. Concluindoosformuláriosparaaaplicaçãodecompraevenda CasadoCódigo
this .dSEstadosECidades.NotasDeEntrada);
((DataGridViewComboBoxColumn)dgvProdutos.Columns[ 0 ])
.DataSource = this .dSEstadosECidades.Produtos;
((DataGridViewComboBoxColumn)dgvProdutos.Columns[ 0 ])
.DisplayMember = this .dSEstadosECidades.Produtos.
descricaoColumn.ColumnName;
((DataGridViewComboBoxColumn)dgvProdutos.Columns[ 0 ])
.ValueMember = this .dSEstadosECidades.Produtos.
idprodutoColumn.ColumnName;
}
Aqui,oprimeiro Fillrefere-seàpopula çãodo DataTablequepopu-
laráo ComboBoxdeprodutos,configuradonofinaldestemétodotambém.
Osdemais FillsforamimplementadosautomaticamentepeloVisualStu-
dio,duranteoprocessodearrastaresoltardos DataTables.Asinstru ções
finaisreferem-seàconfigura çãodo ComboBoxparasele çãodeprodutosno
DataGridView. Elassãoautoexplicativas,somadasaoconhecimentoacu-
muladoatéestepontodolivro.
Executeaaplica çãoparatestaroformuláriodenotasdeentrada.Insira
umanota,informeosdadosdocorpodelaegrave-a. Cliquenobotãode
adicionaritemno BindingNavigatordeprodutosdanotaecliqueno
ComboBoxparaproduto. Suateladeveestarsemelhanteàapresentadana
figura:
278

## Página 295

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
Fig.6.65:Sele çãodeprodutopormeiodeumComboBoxdisponibilizadono
DataGridView
Toda manutenção realizada no DataGridView só será persistida
na base de dados com a gravação realizada pelo método que captura o
evento Click do botão de gravar doBindingNavigator, do topo
da janela. Caso os produtos não sejam gravados, verifique nas pro-
priedades do tableAdapterManager se o TableAdapter para o
produtoNotasDeEntradaTableAdapterestádefinido.
Ajanelaqueserápropostaparaoregistrodavendateráumcomporta-
mentodiferentedoapresentadoparaanotadeentrada,poiselacontarácom
ofechamentodavendaerealizaráaverifica çãodoestoqueparaoprodutoque
sedesejarávender.Oprimeiropassoéacria çãodastabelasdenotasdesaída
(figura6.66)edeprodutosdasnotasdesaídas(figura 6.68),eseusrespectivos
relacionamentos(figura6.67,6.69e6.70).
279

## Página 296

6.11. Concluindoosformuláriosparaaaplicaçãodecompraevenda CasadoCódigo
Fig.6.66:Estruturaparaatabeladenotasdesaída
Verifiquequeaúltimacoluna, notafechada,temcomovalorpadrão–
queseráatribuídoaosnovosregistros–ocaractere ‘N’,quefoiatribuídoà
propriedade Valor ou Associação Padrão.
Fig.6.67:RelacionamentoentreastabelasdeNotaDeSaidaeClientes
280

## Página 297

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
Fig.6.68:EstruturadatabelaProdutosparaNotaDeSaida
Fig.6.69:RelacionamentoentreastabelasProdutosNotaDeSaidaeNotade-
Saida
Fig.6.70:RelacionamentoentreastabelasProdutosNotaDeSaidaeProdutos
Comtodasastabelaseseusrespectivosrelacionamentosjácriados,faz-
senecessáriodisponibilizaressastabelasno DataSet. Novamentecomo
DataSeteajanela Server Explorervisíveis,arrasteastabelasdenotas
desaídaeprodutosdenotasdesaídaparao DataSet(figura6.71).
281

## Página 298

6.11. Concluindoosformuláriosparaaaplicaçãodecompraevenda CasadoCódigo
Fig.6.71:Relacionamentoentreastabelasdeprodutosdenotasdesaídaede
produtos
No formulário criado para o registro de notas de saída, arraste um
GroupBoxe,napropriedade Textdele,digite Dados da Nota. Confi-
gureo DataTabledenotasdesaídadeacordocomoapresentadonafigura
6.72.
Arrasteo DataTableparadentrodo GroupBox.Arrastea DataTable
declientes,dajanela Data Sources,parao ComboBox Cliente. No
TableAdapterde Clientes,no DataSetadicioneummétodo Fill()
queclassifiqueosclientespornome.Adaptenométodoquecapturaoevento
Load,paraqueométodo Filldo adapterdeclientessejaonovomé-
todocriado.Oformulárioparaasnotasdesaída,nestemomento,deveestar
semelhanteaodafigura 6.73.
282

## Página 299

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
Fig.6.72:Configura çãodoscontrolesparaasDataColumnsdanotadesaída
Fig.6.73:Formuláriodenotasdesaídacomosdadosdanota
Finalizandoodesenhodoformulário,arrasteumnovo GroupBox,agora
abaixodoprimeiro,eatribuaàpropriedade Textovalor Produtos da
Nota.Arrasteparadentrodessenovo GroupBoxum BindingNavigator,
econfiguresuapropriedade BindingSourceparao Binding Sourcede
produtosdanotadesaída.
Arrasteparabaixodo Navigatora DataTabledeprodutosdanota
desaída,queestádentroda DataTabledenotasdesaída. Configureo
283

## Página 300

6.11. Concluindoosformuláriosparaaaplicaçãodecompraevenda CasadoCódigo
DataGridViewdeprodutos,damesmamaneiraquefoiconfiguradoode
notasdeentrada,retirandoaschavesestrangeiraseprimárias,emodificando
acolunadeprodutoparaserum ComboBox.
Arraste para a área de controles visuais oTableAdapter, que
está na categoria de nome do projeto naToolbox, e configure no
TableAdapterManagerapropriedaderelativaaesse TableAdapter.Al-
teretambémotextodocabe çalhodascolunas.
Adapteométodoparaoevento Loadparaconfiguraresse ComboBox,
talqualfoifeitoparaanotadeentrada.Seuformuláriodeveestarsemelhante
aodafiguraaseguir:
Fig.6.74:Formuláriodenotasdesaídacomosdadosdanotaeseusprodutos
Algumas configurações agora serão realizadas para que cada nota
possaserfechadaeterseuestoqueatualizado. Configureapropriedade
Enabled dos dois GroupBox para False. Adicione um botão no
BindingNavigatordosdadosdanotaeatribuaumaimagemaele,com
asemânticadeedi ção/altera çãodosdados. Umsegundobotãoaserinse-
ridoéumqueserefiraaofechamentodanota,quandooestoqueserá,então,
284

## Página 301

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
atualizado.Ummétodoparadefini çãodoestadodosbotõesprecisaserim-
plementado.Vejaocódigonasequência.
Resolução6.14:métodoLoadquepopulaosDataTablesdoformu-
lário
private void SetBindingNavigatorButtonsState () {
bool podeFecharNota = false ;
if (notasDeVendaBindingSource.Current != null ) {
DataRowView drv = (DataRowView)
notasDeVendaBindingSource.Current;
DSEstadosECidades.NotasDeVendaRow nvRow =
(DSEstadosECidades.NotasDeVendaRow) drv.Row;
podeFecharNota = nvRow.notafechada.Equals( "N" );
}
bnbFirst.Enabled = !adding && !editing;
bnbPrior.Enabled = bnbFirst.Enabled;
bnbRecordNo.Enabled = bnbFirst.Enabled;
bnbNext.Enabled = bnbFirst.Enabled;
bnbLast.Enabled = bnbFirst.Enabled;
bnbAdd.Enabled = bnbFirst.Enabled;
bnbEdit.Enabled = bnbFirst.Enabled && podeFecharNota;
bnbRemove.Enabled = !editing && podeFecharNota;
bnbSave.Enabled = adding || editing;
bnbFecharNota.Enabled = podeFecharNota &&
(!adding && !editing);
gbxDadosDaNota.Enabled = adding || editing;
gbxProdutosDaNota.Enabled = editing;
}
O métodoSetBindingNavigatorButtonsState()tem, em sua
primeirainstru ção,adefini çãodeumavariávelqueterá,embaseaalgumas
avaliações,ovalor(verdadeirooufalso),responsávelpormanterativooude-
sativoobotãorelacionadoaoprocessodefecharumanota.
Obloco if(),vistocomosegundaimplementa çãodométodo,busca
verificarseoregistrocorrentedo BindingSource( Current)realmente
285

## Página 302

6.11. Concluindoosformuláriosparaaaplicaçãodecompraevenda CasadoCódigo
existe,poisatabelapodeestarvazia. Casopositivo,existeumregistrocor-
renteerecupera-sealinhaatual.Essarecupera çãosedáemduaslinhas,sendo
queaprimeirarecuperaa DataRowView,easegunda,alinharespectivaa
tabela( NotasDeVendaRow,queéumaespecializa çãode DataRow). Este
processopoderiatodoserexecutadoemumaúnicalinha.
Semprequeumdadoéexibido,comoemumcontrole DataGridView,
apenasumaversãodecadalinhapodeserexibidaeestaéum DataRowView.
Um objeto dessa classe pode ter quatro estados diferentes:Default,
Original, Currente Proposed.Apósinvocarométodo BeginEdit()
deuma DataRow,qualquervaloreditadosetornaráumvalor Proposed.
Atéqueométodo CancelEdit()ou EndEdit()sejainvocado,alinha(
row)teráumvalor Originaleum Proposed.Casosejachamadoomé-
todo CancelEdit(),aversãoproposta( Proposed)édescartada,eovalor
érevertidoparaaversão Original.Seainvoca çãoocorrerparaométodo
EndEdit(),a DataRowViewnãoterámaisaversão Proposed,poisela
setornaráovalorcorrente. Valores Defaultsãodisponíveisapenaspara
linhasquepossuemdefinidosumvalorpadrãoparaascolunas. Paraaim-
plementaçãoproposta,utilizou-seo DataRowViewparaobtero DataRow,
referenteao Current.
Objetosdasclasses DataRowe DataColumnsãocomponentesprimá-
riosdeuma DataTable.Essesobjetospodemserusados–assimcomosuas
propriedades–pararecuperareavaliar,inserir,removereatualizarvalores
deum DataTable.Naimplementa ção,esseobjeto DataRowfoiutilizado
pararecuperareavaliarodadodeumdeterminadocampo.
Oconjuntodeinstru çõesapósaestruturacondicional iféresponsável
pordefiniroestadodosbotõesdo BindingNavigator. Esseestadoterá
comobaseasvariáveis addinge editing,responsáveisporinformaremse
oestadoatualdoprocessoé(ounão)deadi çãoouedi ção,poisoestadodos
botõesdependedessasitua ção.Essescamposforamdefinidosnadeclara ção
daclasse,comomostronasequência.
Resolução6.15: definiçãodecamposparaaclasseedométodo
construtor
public partial class FormNotaDeSaida : Form {
286

## Página 303

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
private bool adding, editing;
public FormNotaDeSaida () {
InitializeComponent();
adding = false ;
editing = false ;
}
//Resto da implementação omitido
}
O métodoconstrutor da classe inicializa as variáveisadding e
editing,como false.Essaatribui çãonãoserianecessária,pois falseé
ovalor defaultparavariáveisbooleanas.Umanovaimplementa çãofoine-
cessáriatambémnométodoquecapturaoevento Loaddoformulário.Veja
ocódigoaseguir.
Resolução6.16:métodoquecapturaoeventoLoaddoformulário
private void FormNotaDeSaida_Load ( object sender, EventArgs e) {
// Implementação da Resolução 6.13
if (notasDeVendaBindingSource.Current == null ) {
SetBindingNavigatorButtonsState();
}
}
Nacargadoformulário, casonãoexistaumregistrocorrente, omé-
todo SetBindingNavigatorButtonsState()éinvocado. Estaverifi-
caçãofaz-senecessáriaparaevitarumachamadaduplicadaparaocasode
existirumregistro,poisquandoexiste,háamudan çadeposi çãodosregis-
tros,disparandoumeventoparaisso.Esteeventoéo PositionChanged,
apresentadonasequência.
Resolução6.17:métodoquecapturaoeventoPositionChangeddo
BindingSource
private void notasDeVendaBindingSource_PositionChanged (
object sender, EventArgs e) {
287

## Página 304

6.11. Concluindoosformuláriosparaaaplicaçãodecompraevenda CasadoCódigo
DataRowView drv = (DataRowView)
notasDeVendaBindingSource.Current;
if (drv != null ) {
DataRow dr = drv.Row;
if (drv != null && !(dr.RowState == DataRowState.
Detached)) {
SetBindingNavigatorButtonsState();
}
}
}
A condi ção para a chamada ao método
SetBindingNavigatorButtonsState() é que exista uma
DataRowView que não seja nula, e que o registro atual não seja um
registro novo. Novamente, esta avaliação impede uma redundância a
chamadasaessemétodo,quandoforoptadoporinserirumnovoregistro
(Resolução6.18),queévistocomodesconectado. Relembrando:asmanu-
tençõessãotodasrealizadasemmemóriae,sóaofinal,quandooptadopor
gravar(Resolução6.19),sãopersistidasnabasededados.
Resolução6.18:métodoquecapturaoeventoClickdobotãode
AdicionardoBindingNavigator
private void bnbAdd_Click ( object sender, EventArgs e) {
adding = true ;
SetBindingNavigatorButtonsState();
}
Nomomentoemqueousuárioclicarnobotãoresponsávelporadicionar
umnovoregistro,avariável addingrecebe trueparasinalizaresseestado.
Então,ométodo SetBindingNavigatorButtonState()éinvocado.
Resolução6.19:métodoquecapturaoeventoClickdobotãode
gravardoBindingNavigator
private void notasDeVendaBindingNavigatorSaveItem_Click (
object sender, EventArgs e) {
this .Validate();
288

## Página 305

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
this .notasDeVendaBindingSource.EndEdit();
this .tableAdapterManager.UpdateAll( this .
dSEstadosECidades);
adding = false ;
editing = false ;
SetBindingNavigatorButtonsState();
}
Observe que, após a chamada ao método UpdateAll() do
tableAdapterManager, há a redefinição das variáveis adding
e editing para false e, em seguida, a invocação ao método
SetBindingNavigatorButtonsState().
É preciso agora implementar os métodos para o botão de alteração
(Resolução6.20 )eométododeexclusão( Resolução6.21). Vejaquesuas
implementaçõessãosemelhantesarealizadaparaométododeadi çãodeum
novoregistro.
Resolução6.20:métodoquecapturaoeventoClickdobotãode
alterardoBindingNavigator
private void bnbEdit_Click ( object sender, EventArgs e) {
editing = true ;
SetBindingNavigatorButtonsState();
}
Resolução6.21:métodoquecapturaoeventoClickdobotãode
removerdoBindingNavigator
private void bnbRemove_Click ( object sender, EventArgs e) {
adding = false ;
editing = true ;
SetBindingNavigatorButtonsState();
}
Executeaaplica çãoerealizenelatestesdeinser ção,altera çãoeremo ção.
Verifiqueocomportamentodoestadodosbotões.
Háumproblemaaindacomaimplementa çãoqueprecisasertratada,
eficacomoatividadeparavocêimplementareresolveroproblema. Para
289

## Página 306

6.11. Concluindoosformuláriosparaaaplicaçãodecompraevenda CasadoCódigo
identificaresseproblema,crieumnovoregistro,grave-oecliquenobotão
alterar.
Esevocênãoquiseralterar,massimdescartarasmudan ças?Poisé.Crie
umnovobotãoparaestafinalidadee,então,implementeocomportamento
paraele.Anteriormentenestecapítulo,foiapresentadoo DataRowViewe,
nele,ométodo CancelEdit().Realizeessaatividade.
Agora,parafinalizarotrabalhocomoformuláriodenotasdevenda,
éprecisoimplementarocódigoparaobotão Fechar Nota. Aoclicar
nessebotão,ousuárioteráabaixadoestoquedosistemaeofechamento
danotaemsi,nãosendopermitidorealizaraltera çõesnelaapósessaope-
ração.Paraqueissopossaserrealizado,altera çõesnastabelasserãonecessá-
rias.Destamaneira,doismétodosprecisarãosercriados.Oprimeiroseráno
TableAdapterdeprodutos. Relembrando,paracriaressemétodo,clique
comobotãodireitodomousesobreesse TableAdapter,no DataSet.
Cliqueem Addedepoisem Query,deixeselecionadaaop ção Use SQL
statements,cliquenobotão Nexte,emseguida,marqueaop ção UPDATE.
Nocampodecódigo,informeainstru çãoSQL,visualizadanasequência.
Resolução6.22:instru çãoSQLparaonovométododoTableAdap-
terdeProdutos
UPDATE Produtos SET
quantidadeemestoque =
@quantidadeemestoque - @quantidadevendida
WHERE (idproduto = @idproduto)
}
Verifiquequeo UPDATEpossuidoisargumentosqueserãoutilizados:a
quantidadevendidaeo Iddoprodutoquesofreráaatualiza ção.
Uma segunda instrução SQL precisa ser implementada, agora no
TableAdapter de notas de venda. Esta alterará o valor do campo
notafechadapara S,oqueimpediráaltera çõesnanota. Vejaocódigo
mostradoaseguir.
Resolução6.23:instru çãoSQLparaonovométododoTableAdap-
terdeNotasdeVenda
290

## Página 307

CasadoCódigo Capítulo6. UtilizandoDataSetTipadoparaacessoàbasededados
UPDATE NotasDeVenda
SET notafechada = 'S'
WHERE (idnotadevenda = @idnotadevenda)
Executeaaplica çãoerealizenelatestesreferentesaofechamentodenota.
Valideoestoqueevejaseeleestárealmentesofrendoabaixacorreta.Ainda,
algunspontosnaaplica çãoficaramsemimplementa ção.Umdelesénãorea-
lizarabaixadoestoque,seelenãopossuirestoquesuficiente.Outropontoé
implementaressaatualiza çãodoestoquetambémnanotadeentrada.
6.12 Conclusão
Nestecapítulo,recursosepráticasrelacionadosao DataSetforamapresen-
tadosetrabalhados.Foipossívelverificarqueépossíveloseuusosemaneces-
sidadedeterumabasededadosparapopulá-lo,masqueousomaiscomum
éemsuaformaDataSetTipado.
Exemplosfazendorecursosdecontrolesvisuais,ligadosaoDataSeteseus
componentes,propiciaramumavisãodeprodutividade,fazendousodosre-
cursosvisuaisoferecidospeloVisualStudio.Aofinaldoexemplo,foidemons-
tradoousodacria çãodemétodosnos TableAdapters.OusodeDataSet
Tipadoérecomendadoparapequenasaplica ções,ouaindaparaprototipa ção.
Noscapítulosseguintes,serãoapresentadoso Language INtegrated Query
(LINQ)eo Entity Framework(EF),recursosfortementerecomendadospara
aplicaçõesquetenhamacessosàbasededados.
291

## Página 309

Capítulo7
ConhecendoaLanguage
INtegratedQueryeoWindows
PresentationFoundation
Language INtegrated Query(LINQ)éumatecnologiadesenvolvidapelaMi-
crosoftparafornecersuporteaoníveldelinguagem–comrecursosofereci-
dospeloambiente–eaummecanismodeconsultadedados,paraqualquer
quesejaotipodesteconjuntodedados,quepodemsermatrizes,cole ções,
documentosXMLoubasededados.
Comovistonosexemplosdoscapítulosanteriores,asconsultasadados
sãoexpressascomo strings,semquehajaumaverifica çãodocompilador
esemoferecerumsuporteporpartedoIntelliSense,doVisualStudio. Em
relaçãoao Windows Presentation Foundation(WPF),aMicrosoftoaponta

## Página 310

7.1. IntroduçãoaoWindowsPresentationFoundation CasadoCódigo
como“apróximageração”desistemasdeapresentaçãoparaconstru çãode
aplicaçõesclientes,que,visualmente,fazumusoextremodaexperiênciado
usuário.
ComoWPF,épossívelfazeraconstru çãodeaplica çõesquefuncionem
tantoemambientesdesktopcomoemnavegadoresweb.Estecapítuloapre-
sentaoLINQeoWPF,trazendoconceitosiniciaiseumasimplesaplica ção,
queopermitirãoterumano çãosobreestesconteúdos.
7.1 Introdução ao Windows Presentation Foun-
dation
OWPFéummecanismoquepossuiumnúcleobaseadoemrenderiza çãove-
torial,construídoparatirarvantagensdehardwaresgráficosmaismodernos.
Esteframeworkestendeumnúcleocomumconjuntoderecursosqueincluia
XAML( eXtensible Application Markup Language),controles,liga çãoadados,
layout,gráficos2Dou3D,anima ções,estilos,templates,documentos,mídias
etexto.
ÉpossívelutilizaroVisualStudiocomoambienteparadesenvolvimento
deaplica çõesWPF,entretanto,semprequepossível,opteporferramentases-
pecíficas,comooBlend.
7.2 Criando uma aplicação WPF
NoVisualStudio,crieumanovasolu çãoe,dentrodela,umprojeto WPF
Application(figura7.1).
294

## Página 311

CasadoCódigo Capítulo7. ConhecendoaLanguageINtegratedQueryeoWindows...
Fig.7.1:AdicionandoumprojetoWPFApplicationaumasolu ção
Duranteacria çãodoprojeto,oVisualStudiofazusodostemplatespara
projetosWPFe,aofinaldacria ção,exibeumaáreadetrabalhodeacordo
comoapresentadopelafiguraaseguir:
Fig.7.2:ÁreadisponibilizadapeloVisualStudioparaimplementa çãodeum
projetoWPFApplication
A Solution Explorerapresentatrêsarquivos:
295

## Página 312

7.2. CriandoumaaplicaçãoWPF CasadoCódigo
1) App.config,quepossuiomesmoobjetivodoarquivodeigualnome
paraprojetos Windows Forms Application,queéodepossibilitar
configuraçõesparaaaplica ção/projeto.
2) App.xaml,quedefineaaplica çãoWPFetodososrecursosdisponibili-
zadosparaela.Tambémpermiteaespecifica çãodequalinterfacecomo
usuário(UI–User Interface)seráexibidaautomaticamentequandoaapli-
caçãoforexecutada–nocaso, MainWindow.xaml(Resolução7.1).
3) MainWindow.xaml,queéoarquivodajanelaprincipaldaaplica çãocri-
ada, eexibeoconteúdocriadoempáginas( Resolução7.2). Aclasse
Windowdefineaspropriedadesdeumajanela( window)–comoseutítulo,
tamanhoouícone–egerenciaeventos–comoofechamento(closing)ou
aoculta ção( hiding)dajanela.
Resolução7.1:códigodoarquivoMainWindow.xamlapósacria ção
doprojetoWPFApplication
<Application x:Class= "WpfApplication1.App"
xmlns= "http://schemas.microsoft.com/winfx/2006/xaml/
presentation "
xmlns:x= "http://schemas.microsoft.com/winfx/2006/xaml"
StartupUri= "MainWindow.xaml" >
<Application.Resources>
</Application.Resources>
</Application>
Resolução7.2:códigodaUIcriadapelotemplatedoprojeto
<Window x:Class= "WpfApplication1.MainWindow"
xmlns= "http://schemas.microsoft.com/winfx/2006/xaml/
presentation "
xmlns:x= "http://schemas.microsoft.com/winfx/2006/xaml"
Title= "MainWindow" Height= "350" Width= "525" >
<Grid>
296

## Página 313

CasadoCódigo Capítulo7. ConhecendoaLanguageINtegratedQueryeoWindows...
</Grid>
</Window>
AXAMLéumalinguagemdeclarativaquepermite,dentreoutrasfun-
cionalidades,inicializarobjetoseconfigurarsuaspropriedades,utilizando
umaestruturadelinguagemqueapresentarelacionamentoshierárquicos.Por
meiodaXAML,épossívelcriarelementosvisíveisparainterfaces(UI)em
umatagXAMLdeclarativa,separandoemoutroarquivocódigosqueres-
pondamaeventos. Issopermiteamanipula çãodeobjetosdeclaradosem
umXAML.ArquivosXAMLsãoarquivosXMLquepossuemumaextensão
xaml.
Em relação ao elemento <Application.Resources> do arquivo
App.xaml(Resolução7.1), Applicationexpõeumescopoaonívelda
aplicaçãoparacompartilharrecursos,nomeadoscomo Resources. Por
padrão, apropriedade Resourceséinicializadacomumainstânciade
ResourceDictionary. Essainstânciaéusadaparaobtereatribuirpro-
priedadescomescopodeaplica ção,utilizando Resources.
Um Griddoelemento <Grid>(Resolução7.2)éumpainel,cujolayout
organizaseuscontrolesinternosemumaestruturatabulardelinhasecolunas.
SuafuncionalidadeésimilaraumatabelaHTML,entretanto,commaiorfle-
xibilidadedeconfigura ções.Umacélulapodecontervárioscontroleseestes
podemocupardiversascélulas.
ParaimplementarumexemploquepossaintroduzirtantooWPFquanto
oLINQ,serádesenhadaumajanela(figura 7.3eResolução7.3)comumalista
deobjetosdeumaclasse Candidato,quepossuicomopropriedades Nome
e Idade. Afuncionalidade,quefaráusodoLINQ,seráimplementadano
eventoquecapturaoevento Clickdeumbotão.
297

## Página 314

7.2. CriandoumaaplicaçãoWPF CasadoCódigo
Fig.7.3:Janelacombotão,GroupBoxseListBoxsparaaplica çãodoLINQ
Ajanelapossui4 GroupBoxs: umparaobotão, outroparaosdois
GroupBoxsinternos( Candidatose Maiores).Existemoutroscontainers
quepodemserusadosetrazerresultadosvisuaismelhores,masparacumprir
oobjetivoaquiproposto,o GroupBoxatendebem.
Odesenvolvimentodainterfacecomousuáriopodeserrealizadoar-
rastando controles para a área de desenho (guiaToolBox), e pode ter
suaspropriedadeseeventosconfiguradostambémdemaneiravisual(guia
Properties),ouoptarpelaescritadocódigo,fazendousodoIntelliSense
doVisualStudio.Parafacilitaravalida çãodocódigo,inicialmentetodaim-
plementaçãoteráseucódigoXAMLapresentado. Najanelade“desenho”,é
possívelalternarentreavisualiza çãodocódigoXAMLedoresultadoobtido
paraacodifica çãoemquestão.Tambémépossíveldividirajanelacomasduas
visualizações,bastaselecionarnabasedaáreadedesenhoaop çãodesejada.
Resolução7.3:implementa çãodajaneladaaplica ção
<Window x:Class= "WPFLINQIntroProject.MainWindow"
xmlns= "http://schemas.microsoft.com/winfx/2006/
xaml/presentation "
xmlns:x= "http://schemas.microsoft.com/winfx/2006/
xaml "
Title= "MainWindow" Height= "350" Width= "525"
HorizontalAlignment= "Center" VerticalAlignment=
298

## Página 315

CasadoCódigo Capítulo7. ConhecendoaLanguageINtegratedQueryeoWindows...
"Center" >
<Grid>
<!-- Início da Parte 1 -->
<Grid.RowDefinitions>
<RowDefinition Height= "Auto" />
<RowDefinition Height= "Auto" />
</Grid.RowDefinitions>
<!-- Fim da Parte 1 -->
<!-- Início da Parte 2 -->
<GroupBox Grid.Row= "0" >
<Button Content= "Iniciar verificação"
HorizontalAlignment= "Center" Margin= "0,10,0,0"
VerticalAlignment= "Center" Width= "150"
Height= "30" FontWeight= "Bold" Click=
"Button_Click" />
</GroupBox>
<!-- Fim da Parte 2 -->
<!-- Início da Parte 3 -->
<GroupBox Grid.Row= "1" >
<Grid>
<Grid.ColumnDefinitions>
<ColumnDefinition Width= "250" />
<ColumnDefinition Width= "250" />
</Grid.ColumnDefinitions>
<Grid.RowDefinitions>
<RowDefinition Height= "240" />
</Grid.RowDefinitions>
<GroupBox Grid.Column= "0" Header= "Candidatos" >
<ListBox Margin= "10,10,0,13" Name=
"lbxCandidatos" HorizontalAlignment=
"Left" VerticalAlignment= "Top"
Width= "230" Height= "Auto" />
</GroupBox>
<GroupBox Grid.Column= "1" Header= "Maiores" >
<ListBox Margin= "10,10,0,13" Name=
"lbxMaiores" HorizontalAlignment=
"Left" VerticalAlignment= "Top"
299

## Página 316

7.3. IntroduçãoaoLanguageINtegratedQuery CasadoCódigo
Width= "220" Height= "Auto" />
</GroupBox>
</Grid>
</GroupBox>
<!-- Fim da Parte 3 -->
</Grid>
</Window>
Nocódigo,existemcomentáriosdelimitandoconjuntosdeinstru ções.
Estescomentáriosedelimita çõesservirãoparaexplica çõesdasimplemen-
tações.Na Parte1,étrabalhadaadefini çãodaslinhasparao Gridqueestá
definidologonoiníciodaimplementa ção. Aquantidadedelinhasqueele
possuiráestárelacionada,nestecaso,comaquantidadedelinhasconfigura-
dasdentrodoelemento <Grid.RowsDefinitions>.
AParte2 defineum GroupBox,quedeveráseralocadonalinha0,na
primeiralinha(atributo Grid.Row=“0”).Dentrodesse GroupBox,édefi-
nidoum Button,comcaracterísticasdefinidaspormeiodeatributosparao
elemento Button.
JáaterceirapartedocódigoXAMLdefineo GroupBoxparaasegunda
linhado Grid. NesseGroupBoxédefinidoum Grid,comduascolunas
eumalinha. Emcadacoluna,éinseridoumcontrole ListBox,queserão
alimentadospormeiodecódigo.
NãofazpartedoescopodolivrodetalharoselementosXAMLeseusatri-
butos.Entretanto,comoconhecimentoadquiridoatéaqui,aleituraeinter-
pretaçãosemânticaauxiliamnainterpreta çãodoscontrolesesuasconfigura-
ções.
7.3 Introdução ao Language INtegrated Query
DeacordocomaMicrosoft,umaconsultaéumaexpressãoqueretornadados
deumafontededados.Consultassãousualmentedefinidasemumalingua-
gemespecializadaparaconsultas. Diferenteslinguagenseferramentastêm
sidodesenvolvidasparaosdiversostiposdedadosexistentesequesurgem,
comoporexemplo,aSQLparabancosdedadosrelacionais.Estaestratégia
fazcomosdesenvolvedoresprecisemaprendernovaslinguagensparacada
300

## Página 317

CasadoCódigo Capítulo7. ConhecendoaLanguageINtegratedQueryeoWindows...
tipodefontededados(ouformatosdedados)quesuasaplica çõesprecisam
suportar.
OobjetivodoLINQésimplificaressasitua ção,oferecendoummodelo
consistenteparatrabalharcomdiversostiposdefonteseformatosdedados.
EmumaconsultaLINQ,otrabalhosempreocorresobreobjetos.Destama-
neira,ousoéomesmoparaconsultaretransformardadosemdocumentos
XML,basesdedadosSQL,DataSets,cole çõesouqualqueroutrotipodedado
queofere çaum providerLINQ.
7.4 Preparando a aplicação para uma consulta
LINQ
ParaimplementaroprimeiroexemploemLINQ,umacole çãodeobjetosda
classe Candidato,apresentadanasequência,popularáo ListBoxcriado
najanelaapresentadanafigura 7.3.
Resolução7.4:classeCandidato
namespace WPFLINQIntroProject {
public class Candidato {
public string Nome { get ; set ; }
public int Idade { get ; set ; }
}
}
Definidootipodedadoqueserátrabalhado,éprecisocriarumacole ção
quesejapopuladacomobjetosdotipodefinido–nestecaso, Candidato.A
seguir,apresentoométodoquepossuiessaresponsabilidade.
Resolução7.5:métodoquepopulaumacole çãodeCandidatos
private void GenerateCandidatos () {
candidatos.Add( new Candidato() {Nome = "Yuri" ,
Idade = 25 });
candidatos.Add( new Candidato() {Nome = "Yara" ,
Idade = 23 });
301

## Página 318

7.4. PreparandoaaplicaçãoparaumaconsultaLINQ CasadoCódigo
candidatos.Add( new Candidato() {Nome = "Gabriel" ,
Idade = 20 });
candidatos.Add( new Candidato() {Nome = "Maria Clara" ,
Idade = 7 });
candidatos.Add( new Candidato() {
Nome = "Vicente Dirceu" , Idade = 6 });
candidatos.Add( new Candidato() {Nome = "Júlia" ,
Idade = 9 });
candidatos.Add( new Candidato() {Nome = "Lívia" ,
Idade = 64 });
candidatos.Add( new Candidato() {Nome = "Elio" ,
Idade = 74 });
candidatos.Add( new Candidato() {Nome = "Alba" ,
Idade = 44 });
candidatos.Add( new Candidato() {Nome = "Angélica" ,
Idade = 24 });
}
Adeclara çãoeinvoca çãodométodo GenerateCandidatos()pode
serverificadanasequência.
Resolução7.6:declara çãodecole çãodecandidatoseinvoca çãode
métodoparapopula çãodecole çãoeListBox
public partial class MainWindow : Window {
private List<Candidato> candidatos =
new List<Candidato>();
public MainWindow () {
InitializeComponent();
GenerateCandidatos();
PopulateListBox();
}
// Código omitido
}
Observeque,noconstrutordaclassequerepresentaajanela,existetam-
bémachamadaaométodo PopulateListBox()–apresentadoaseguir
302

## Página 319

CasadoCódigo Capítulo7. ConhecendoaLanguageINtegratedQueryeoWindows...
–,responsávelporpopularoListBoxcomos Candidatospreviamente
populadosnacole ção candidatos.
Resolução7.7:métodoquepopulaoListBoxdecandidatos
private void PopulateListBox () {
foreach ( var candidato in this .candidatos) {
lbxCandidatos.Items.Add(candidato.Nome);
}
}
7.5 Implementando uma consulta LINQ
Todaopera çãodeconsultaLINQconsistedetrêsa ções:
a) Obtençãodafontededados;
b) Criaçãodaconsulta;
c) Execuçãodaconsulta.
Essastrêsaçõesserãoapresentadasnaopera çãodeconsultaapresentada
aseguir,queédisparadanoevento Clickdobotão.
Resolução7.8:métodoquepopulaoListBoxdecandidatos
private void Button_Click ( object sender, RoutedEventArgs e) {
// Início da consulta LINQ
var maiores =
from candidato in this .candidatos
where candidato.Idade >= 18
select candidato;
// Término da consulta LINQ
foreach ( var maior in maiores) {
lbxMaiores.Items.Add(maior.Nome);
}
}
303

## Página 320

7.6. ConceitosbásicossobreconsultasnocontextoLINQ CasadoCódigo
Emboraoexemplopropostotrabalheemcole ções,asintaxeéamesma
paraqualquerfontededados.Nocódigo,aprimeiraparteéafontededados
(nestecaso, candidatos);jáasegundarefere-seàcria çãodaconsulta,queé
avariávelmaioresdotipo IEnumerable<Candidato>;eaúltimaparte
éaexecu çãodaconsulta,que,nesteexemplo,estáno foreach.
Aconsulta( query)especificaqueinforma çãoserárecuperadadafonte
dedados. Umaconsultapodetambémespecificarcomoainforma çãodeve
serclassificada,agrupadaefiltrada,antesdeserretornada.Aconsultaéar-
mazenadaemumavariáveldeconsulta( query variable)einicializadacoma
execuçãodeumaexpressãodeconsulta. Foibuscandotornaresseprocesso
simplesefácilquealinguagemC #introduziuumasintaxeparaconsultas.
Comojácomentado,avariáveldeconsulta apenasarmazenaemsiasins-
truçõesparaarealiza çãodeumaconsulta.Suarealexecu çãoéadiadaatéque
umresultadosejabuscado.Noexemploapresentado,esseresultadoveiopor
meiodeumaitera çãonoconjuntoretornado,pelainstru ção foreach.
Consultasquerealizamfun çõesdeagrega çãosobreumintervalodeele-
mentosprecisam,primeiramente,iterarnesseselementos,oquecausauma
execuçãofor çada.Exemplosdestasfun çõessão Count, Averagee First.
Paraessecaso,otipodedadodavariávelquerecebeoresultadoédeumvalor
simples,enãoumacole ção IEnumerable.Parafor çarumaexecu çãoime-
diatadequalquerconsulta,guardandoemcacheseusresultados,épossível
invocarométodo ToList<TSource>()ou ToArray<TSource>().
7.6 Conceitos básicos sobre consultas no con -
texto LINQ
Geralmente,afontededadoséorganizadalogicamentecomoumasequência
deelementosdomesmotipo. Umatabeladeumabasededadosrelacional
contémumasequênciadelinhas.Demaneirasimilar,um DataTablecon-
témumasequênciadeobjetos DataRow.EmumarquivoXMLexisteuma
sequênciadeelementosXML,organizadoshierarquicamenteemumaárvore.
Umacole çãodispostanamemórialocalcontémtambémumasequênciade
objetos.
Dopontodevistadeumaaplica ção,otipoespecíficoeaestruturaori-
304

## Página 321

CasadoCódigo Capítulo7. ConhecendoaLanguageINtegratedQueryeoWindows...
ginaldafontededadosnãosãoimportante. Aaplica çãosemprevêafonte
dedadoscomoumacole çãode IEnumerable<T>ou IQueryable<T>.
Destamaneira,deumamaneiraespecializada,parao LINQ to XML,afonte
dedadosévisívelcomoum IEnumerable<XElement>;parao LINQ to
DataSetécomoIEnumerable<DataRow>;eparao LINQ to SQLéum
IEnumerableou IQueryabledotipodedadosdosobjetosusadospara
representarosdadosnatabelaSQL.
Comaobten çãodessasequência,umaconsultapoderecuperarumsub-
conjuntodeelementosquepermitaproduzirumanovasequência,semmo-
dificaroselementosindividuais. Alémdisso,elatambémpodeclassificar
ouagruparasequênciadeváriasmaneiras. Umexemploéapresentadona
sequência.
Resolução7.9:recuperandoeclassificandoumconjuntodedados
var maiores =
from candidato in this .candidatos
where candidato.Idade >= 18
orderby candidato.nome descending
select candidato;
Aleituradainstru çãoLINQpodeserrealizadadaseguintemaneira:
ainstru ção select candidatoselecionaobjetosretornadosdainstru-
ção from candidato in this.candidatos. Porsuavez,osobjetos
retornadospara candidatosofremumasele ção,pormeiodeumcrité-
rio( where candidato.Idade >= 18)e,emseguida,sãoclassificados
( orderby candidato.nome descending). Pelofatodeaexce çãoda
leituracome çarpelaúltimalinha,umainstru çãoLINQassemelha-seàsins-
truçõesSQL,eelatemorecursodeautocomplemento,oferecidopeloVisual
Studio.
Aindacomaobten çãodasequência,umaconsultatambémpoderecu-
perarumvalorúnicosobreumafontededados,como:onúmerodeelemen-
tosquecorrespondamaumadeterminadacondi ção;oelementoquepossuio
maioroumenorvalor;oprimeiroelementoquecorrespondaaumacondi ção;
ouasomadevaloresespecíficosemumdeterminadoconjuntodeelementos.
Umexemploparaessafuncionalidadeéapresentadoaseguir.
305

## Página 322

7.7. Conceitosbásicossobreexpressõesdeconsultas CasadoCódigo
Resolução7.10:obtendoaquantidadedecandidatoscombaseem
umcritério
var qtdeMaiores =
( from candidato in this .candidatos
where candidato.Idade >= 18
orderby candidato.nome descending
select candidato).Count();
Outrapossibilidadeparaexecutaressetipodefuncionalidadeéobtera
variáveldeconsultae,depois,invocarométododeagrega ção.Issopodeser
vistonasequência.
Resolução7.11:obtendoamédiadaidadedoscandidatos
var idadesCandidatos =
from candidato in this .candidatos
select candidato.Idade;
var mediaIdade = idadesCandidatos.Average();
7.7 Conceitos básicos sobre expressões de con-
sultas
Asexpressõesdeconsulta( query expression)vêmsendoutilizadaseexplica-
dasconformesuasaplica ções. Agora,éprecisodetalhá-lasumpoucomais.
Destamaneira,umaexpressãodeconsultapodeserdefinidacomoumacon-
sultaqueéexpressaemsintaxeespecíficaparaconsultas.Elaésemelhantea
qualqueroutraexpressãoepodeserusadaemqualquercontextoemqueuma
expressãoC #sejaválida.
Essaexpressão( query expression)éformadaporumconjuntodecláusulas
escritasemumasintaxedeclarativa,semelhanteaoSQL.Cadacláusuladela
pode,porsiprópria,conterumaoumaisexpressõesC #,eestaspodemconter
oufazerpartedeumaexpressãodeconsulta.
Umaexpressãodeconsultaprecisacome çarcomumacláusula from,e
terminarcomum selectouacláusula group.Entreaprimeiraeúltima
cláusuladaexpressão,épossívelutilizarumaoumaiscláusulasopcionais,
306

## Página 323

CasadoCódigo Capítulo7. ConhecendoaLanguageINtegratedQueryeoWindows...
como: where, orderby, join, letouatémesmocláusulasadicionais
from.Épossíveltambémousodapalavra-chave into,parapermitirqueo
resultadodeum joinou groupsirvacomofontededadosparacláusulas
adicionaisdeconsulta,namesmaexpressão.
7.8 Sintaxe de consultas e de métodos no LINQ
Asconsultasapresentadasatéestemomentofazemusodasintaxedeclarativa
doLINQ.Entretanto,essasintaxedeconsultadevesertraduzidaemchama-
dasamétodos,paraseremexecutadasnaCLR( Common Language Runtime),
oqueocorrenoprocessodecompila ção. Essaschamadasamétodosinvo-
camosoperadorespadrõesdeconsulta,osquaistêmnomescomo: Where,
Select, GroupBy, Join, Maxe Average.
Semanticamente, assintaxesbaseadasemconsultaeemmétodossão
idênticas, porém, muitaspessoasveemasintaxedeconsultascomomais
simplesefáceisdeler. Entretanto, éprecisoterciênciadequealgumas
consultasprecisamnecessariamenteserescritascomchamadasamétodos.
Umexemploéanecessidadederecuperaraquantidadedeelementos(obje-
tos/registros)quecorrespondamaumadeterminadacondi ção.A Resolução
7.12apresentaumaconsultausandoasintaxedeconsultas,ea Resolução7.13,
asintaxedemétodos.
Resolução7.12:consultacomasintaxeemconsulta
var queryMaiores =
from candidato in this .candidatos
where candidato.Idade >= 18
orderby candidato.Nome
select candidato;
foreach ( var maior in queryMaiores) {
lbxMaiores.Items.Add(maior.Nome);
}
Resolução7.13:consultacomasintaxeemmétodos
307

## Página 324

7.9. ExpressõesLambda(lambdaexpressions) CasadoCódigo
var queryMaiores =
candidatos.Where(candidato => candidato.Idade >= 18 ).
OrderBy(candidato => candidato.Nome);
foreach ( var maior in queryMaiores) {
lbxMaiores.Items.Add(maior.Nome);
}
Oresultado(ouseja,oselementos)serãoosmesmosemambasimple-
mentações, inclusiveotipodedadosdavariável queryMaiores, queé
IEnumerable<Candidato>.
Nainstru çãoquedefineavariáveldeconsulta,acláusula whereéagora
expressacomoummétododoobjeto candidatos.Estenãoexistenaclasse
Candidatoetampouconainterface IEnumerable<T>.Entretanto,nain-
vocaçãodoIntelliSensedoVisualStudio,aoinserirmosoponto( .)apósa
variável,épossívelverificarquenãoapenasométodo Where()éoferecido,
masdiversosoutrostambém,como Select(), SelectMany(), Join()e
Orderby().Existemmétodosparatodososoperadorespadrõesdeconsulta.
Apesardetermosaimpressãoqueessesmétodosforamredefinidosem
IEnumerable<T>,nãoéissoqueacontece. Eles,quesãooperadoresbá-
sicosparaconsulta,sãoimplementadoscomoumtipodemétodoconhe-
cido como extension methods(métodos de extensão). Esses méto-
dos estendemum tipo existente, que podem ser invocados como se fos-
semmétodosdeinstânciadotipodoobjeto. Osoperadoresbásicospara
consultasestendem IEnumerable<T>eéporissoqueépossívelutilizar
candidatos.Where(...).
Métodosdeextensão( extension methods)habilitamaadi çãodemétodos
aumtipo(classe)jáexistente,semanecessidadedeestenderumaclassepara
essaimplementa ção.Elespodemservistostambémcomoumtipoespecialde
métodoestático,porém,sãochamadoscomosefossemmétodosdainstância
emumaespecializa ção.
7.9 ExpressõesLambda(lambda expressions)
Noexemploapresentadoanteriormente,verifiquequeaexpressãocondicio-
nal( candidato.Idade >= 18)épassadacomoumargumento in-line,
308

## Página 325

CasadoCódigo Capítulo7. ConhecendoaLanguageINtegratedQueryeoWindows...
paraométodo Where().Essaexpressão in-lineéchamadadeexpressão
lambda,queéumamaneiraconvenienteparaescrevercódigoquepoderia
normalmenteserescritodeumamaneiramaistrabalhosa,comopormeio
demétodosanônimos,deumadelega çãogenéricaouemumaexpressãoem
árvores.
EmC #,osímbolo =>éooperadorlambda,queélidocomo“vaipara”.
Avariávelcandidato,àesquerdadooperador,éavariáveldeentrada,que
correspondeàvariável candidatonaexpressãodeconsulta.Ocompilador
podeinferirotipode candidatopelofatodeelesaberque candidatosé
umtipogenérico IEnumerable<T>.Ocorpodaexpressãolambdaéexata-
mentecomoaexpressãonasintaxedeconsulta,ouemoutrasexpressõesC #;
elepodeincluirchamadasamétodoseoutraslógicascomplexas.O“valorde
retorno”éoresultadofornecidopelaexpressão.
Noexemploda Resolução7.13,ométodo OrderBy()éinvocadouti-
lizandoooperadorponto( .),apósachamadaaométodo Where(). O
método Where()produzumasequênciaselecionada(filtrada)e,então,o
operador Orderbyéaplicadoaessasequência,classificando-a. Devidoao
retornodeconsultasser IEnumerable,épossívelcomporaconsultapor
meiodasintaxedemétodos,peloencadeamentodechamadasaosmétodos
euma“única”instrução. Esteprocedimentoéoqueocompiladorrealiza
quandoseescreveconsultaspormeiodasintaxedeconsultas. Pelofatode
umavariáveldeconsultanãoarmazenarosresultados,épossívelmodificá-la
ouusá-lacomobaseparaumanovaconsultaaqualquermomento,mesmo
apóselatersidoexecutada.
7.10 Conclusão
Asferramentas,recursosetécnicasapresentadosnestecapítulotiveramcomo
objetivoumabreveintrodu çãoaoLanguageINtegratedQuery(LINQ)eao
WindowsPresentationFoundation(WPF),poderososrecursosquepoderão
trazerumganhodequalidadeeprodutividadenoacessoadados,eumanova
possibilidadeparagera çãodeaplica çõescomrecursosricosparaaintera ção
comousuário.
Comoexemploapresentadoeasexplana çõesrealizadas,verifica-sequeo
309

## Página 326

7.10. Conclusão CasadoCódigo
usodoLINQnoprocessoderealiza çãodeconsultastorna-semaisconfiável,
umavezquefazusodeumasintaxequenãoutilizadestringsparaaescritade
consultas.Tambémfoiintroduzidooconceitode extension methods(méto-
dosdeextensão)e lambdas expressions(expressõeslambdas),quecertamente
serãousadosamplamenteemsuasaplica çõesfuturas.
Naapresenta çãodoWPF,ajanelacriada,pormaisquesepare çaseme-
lhanteaumaaplica ção Windows Forms Application,épossívelverifi-
carqueaqualidadedoscontrolesvisuaisémaioraoexecutarmosaaplica ção.
Napartedeimplementa ção,foipossívelconheceroeXtensibleApplication
MarkupLanguage,ecomoimplementarecodificarasinterfacescomosusuá-
rios.
Nopróximocapítulo,seráfeitousodoEntityFramework(EF)e,nos
exemplosqueserãoapresentados,osrecursosdestecapítuloserãoúteis.
310

## Página 327

Capítulo8
ApresentandooEntity
Frameworkcomoferramenta
paraMapeamentoObjeto
Relacional
OEntityFramework(EF)éumframeworkparamapeamentosdeobjetospara
ummodelorelacionaledeummodelorelacionalparaobjetos(ORM– Object
Relational Mapping).PormeiodoEF,épossíveltrabalharcomdadosrelaci-
onaisfazendousodeobjetosdacamadadenegócio.Destamaneira,háuma
eliminaçãodecodifica çãodeacessoadadosdiretamentenaaplica ção,como
porexemploasinstru çõesSQL.
Comessascaracterísticasapresentadas,estecapítulotemporobjetivoin-

## Página 328

8.1. ComeçandocomoEntityFramework CasadoCódigo
troduziroEntityFrameworkcomoferramentaparapersistênciaeintera ção
comumabasededados,tendocomoapoiopartedaaplica çãojádesenvolvida
emcapítulosanteriores.Nãofazpartedoescopodestecapítuloumaprofun-
damentonotema,queporsisójáétemaúnicodediversoslivros.
8.1 Começando com o Entity Framework
ParainiciarasatividadesrelacionadasaodesenvolvimentousandoEF,opri-
meiropassoéobterosrecursosnecessáriosparautilizá-lo.Aprimeiraferra-
mentaqueprecisamosdisponibilizarnoVisualStudioéo EFToolsforVisual
Studio,quejáveminstaladanaversão2013.Asegundaferramentanecessária
éaEFRuntime,quedeveserdisponibilizadanasreferências( References)do
projeto,comoumPacote/Assembly,emumaDLL.Paraadicionarareferência
aoEFRuntime,omeiomaissimpleséfazerusodo NuGet,queinstalaráno
projetoselecionadoo EFNuGetPackage.
ONuGetéumgerenciadordepacotesparadesenvolvimentonaplata-
formaMicrosoft,oqueincluiodesenvolvimentodeaplica ções.NET.Essa
ferramentadispõeospacotesaseremutilizadosnaaplica çãoemumservidor
remoto,etambémferramentasclientesdoNuGet,quepermitemproduzire
consumirpacotesNuGets.
8.2 Criando um projeto para aplicação do En-
tityFramework
Oprojetoinicialparaaplica çãodoEntityFrameworkseráumaaplica ção
WindowsPresentationFoundation,comcontrolesparaentradaevisualiza-
çãodedadosporpartedeusuário. Éimportanterefor çaroconceitotraba-
lhadoanteriormenteemrela çãoaprojetosseparados,deacordocomassuas
responsabilidades.Procureaplicarissoemsuasaplica ções.
Assim,crieumanovasolu çãoe,dentrodela,umprojetoWPF.Nessepro-
jeto,crieumapastachamada POCOe,nela,aclasse Estado.Vejaocódigoa
seguir.
Resolução8.1:classedenegócioEstado(Versão1)
312

## Página 329

CasadoCódigo Capítulo8. ApresentandooEntityFrameworkcomoferramentapara...
public class Estado {
public long Id { get ; set ; }
public string UF { get ; set ; }
public string Nome { get ; set ; }
}
Comaclassedemodelocriada,jáépossívelcome çaraprepararoprojeto
parausodoEntityFramework.Oprimeiropassoéacria çãodocontexto,que
representaráaconexãocomabasededados.Comoacria çãodessecontexto
fazusodaclasse System.Data.Entity.DbContextedispõeumapropri-
edadedotipo DbSet<TEntity>,éprecisoadicionarareferênciaaoNuGet
PackagedoEntityFramework.
8.3 Habilitando a API do Entity Framework
(NuGetPackage toEntity) para o projeto
ParaqueoprojetoemdesenvolvimentopossafazerusodoEntityFramework,
cliquecomobotãodireitodomousesobreonomedoprojetoe,então,na
opção Manage NuGet Packages(figura8.1).
Fig.8.1:AcessandoagerênciadepacotesNuGet
Najanelaexibida,éprecisoselecionaracategoriadepacotesqueserão
exibidos/pesquisados. Cliquedoladoesquerdonaop ção on-linee,na
caixadebuscadoladodireito,digite EntityFramework. Comoresultado,
suajanelaestarásemelhanteàapresentadanafiguraaseguir:
313

## Página 330

8.3. HabilitandoaAPIdoEntityFramework(NuGetPackagetoEntity)paraoprojeto CasadoCódigo
Fig.8.2:BuscandoopacoteNuGetparainstala ção
ONuGetPackageparaoEntityFrameworkdeveráaparecercomopri-
meiroitem,deacordocomafigura 8.2. Assim,cliquenobotão Install,
queapareceaoladodireitodonomedopacote.Antesdoprocessodeinstala-
çãocome çar,ésolicitadaaleituradotermodalicen çadeusoeconfirma ção
doaceite(figura8.3).
Fig.8.3: Leituraeconcordânciacomotermodelicen çadeusodoNuGet
PackageparaoEF
Apósainstala ção,noteamarcaaoladodonomedopacote,queindica
314

## Página 331

CasadoCódigo Capítulo8. ApresentandooEntityFrameworkcomoferramentapara...
queelejáestáinstalado(figura8.4).
Fig.8.4:Indica çãodainstala çãobemsucedidadoNuGetPackageparaoEF
Apósfecharajanelademanuten çãodospacotesNuGets,verifiqueaadi-
çãoàsreferênciasdoprojetodosAssembliesdoEntityFramework(figura
8.5).
Fig.8.5:AssembliesdoEFadicionadosàsreferênciasdoprojeto
Quandoumpacoteéinstalado,oNuGetcopiaarquivosparaasolu ção
eautomaticamenterealizatodasasaltera çõesquesãonecessárias,comoa
adiçãodereferênciasemudan çasno app.config. Sedecidirremovera
biblioteca,oNuGetremoveosarquivoserevertetodasasaltera çõesrealizadas
noprojetoporele.
8.4 Criando o contexto com a base de dados
Paraqueaplica ções.NETpossamsebeneficiarcomoEntityFramework,é
precisoqueoframeworkacesseabasededadospormeiodeumcontexto,
315

## Página 332

8.5. LendoeescrevendodadosnabasededadospormeiodoEF CasadoCódigo
querepresentaráumasessãodeintera ção,sejaparaconsultaouatualiza ção
daaplica çãocomabasededados.
Para o EF, um contexto é uma classe que estenda
System.Data.Entity.DbContext. Destamaneira,crieemseuprojeto
umapastachamada Contextse,dentrodela,umaclasse EFContext.cs,
quedeveráteressaextensãoimplementada.Vejaocódigonasequência.
Resolução8.2:classequerepresentaráocontextocomabasede
dados(Versão1)
using System.Data.Entity ;
using EFApplication.POCO ;
namespace EFApplication.Contexts {
public class EFContext : DbContext {
public DbSet<Estado> Estados { get ; set ; }
}
}
No código, a primeira implementação diz respeito à importação do
namespacerelativoaoEF,o System.Data.Entity;. Nadeclaraçãoda
classe,aextensãode DbContextérealizada(:DbContext)e,porfim,uma
propriedadedotipo DbSet<Estado>,chamada Estados,écriada.
Propriedadesdaclasse DbSetrepresentamentidades( Entity)quesão
usadasparaasopera çõesdecria ção,leitura,atualiza çãoeremo çãodeobje-
tos(registrosdatabela). Destamaneira,senabasededadosháumatabela
queserámanipuladaporsuaaplica çãopormeiodoEF,éimportanteque,na
definiçãodocontexto,hajaumapropriedadequearepresente.
8.5 Lendo e escrevendo dados na base de dados
por meio doEF
Paraexemplificarainser çãodeumobjetoàbasededadoserecuperartodosos
jápersistidos,seráimplementadoumexemplo,fazendousodeWPFcomEF
edasclassesjáimplementadasnestecapítulo.Asfiguras 8.6e8.7apresentam
ainterfacequedeveráserimplementadaparaaintera çãocomousuário.
316

## Página 333

CasadoCódigo Capítulo8. ApresentandooEntityFrameworkcomoferramentapara...
Fig.8.6:Janeladeintera çãocomousuáriopararegistrodeEstados–Inse-
rindonovoestado
317

## Página 334

8.5. LendoeescrevendodadosnabasededadospormeiodoEF CasadoCódigo
Fig.8.7:Janeladeintera çãocomousuáriopararegistrodeEstados–Alte-
randoumestadojágravado
Asfiguras8.6e8.7possuemtrêsáreas. Aprimeiraéadeentradade
dados,para Id, UFe Nome do Estado.Emrela çãoao Id,elenãotemseu
valorinformadopelousuário,massimpelabasededadose,apósainser ção,
esteéatribuídoaoobjetoquerepresentaráoestadoinserido.
Jáasegundaáreaéreferenteaobotão Gravar,quefaráusodosdados
informadosnos TextBoxsparainstanciarumobjetode Estadoe,então,
enviá-loparapersistênciapormeiodoEF.A terceiraeúltimaparterefere-se
àapresentaçãodetodososestadosjápersistidos,pormeiodeum DataGrid.
Aseguir,tragoaimplementa çãodestajanela.
Resolução8.3:XAMLdajanelademanuten çãonosdadosdees-
tado
<Window x:Class= "EFApplication.MainWindow"
xmlns= "http://schemas.microsoft.com/winfx/2006/xaml/
presentation "
xmlns:x= "http://schemas.microsoft.com/winfx/2006/xaml"
Title= "Manutenção em dados de Estados" Height= "350"
318

## Página 335

CasadoCódigo Capítulo8. ApresentandooEntityFrameworkcomoferramentapara...
Width= "293.656" WindowStartupLocation=
"CenterScreen" ResizeMode= "NoResize" >
<Grid>
<!-- Definição e configuração de linhas e colunas para o Grid
(painel da janela) -->
<Grid.RowDefinitions>
<RowDefinition Height= "Auto" />
<RowDefinition Height= "Auto" />
<RowDefinition Height= "Auto" />
<RowDefinition Height= "28" />
<RowDefinition Height= "*" />
</Grid.RowDefinitions>
<Grid.ColumnDefinitions>
<ColumnDefinition Width= "Auto" />
<ColumnDefinition Width= "200" />
</Grid.ColumnDefinitions>
<!-- Registro e configuração dos controles que comporão o
formuário -->
<Label Grid.Row= "0" Grid.Column= "0" Content= "Id:" />
<Label Grid.Row= "1" Grid.Column= "0" Content= "UF:" />
<Label Grid.Row= "2" Grid.Column= "0" Content= "Nome:" />
<Label Grid.Row= "4" Grid.Column= "0"
Content= "Registrados:" VerticalAlignment=
"Center" />
<TextBox x:Name= "txtID" Grid.Column= "1" Grid.Row= "0"
Margin= "3,3,154,3" IsEnabled= "False" />
<TextBox x:Name= "txtUF" Grid.Column= "1" Grid.Row= "1"
Margin= "3,3,154,3" />
<TextBox x:Name= "txtNome" Grid.Column= "1" Grid.Row= "2"
Margin= "3" />
<Button Grid.Column= "1" Grid.Row= "3"
HorizontalAlignment= "Right" MinWidth= "80"
Margin= "3" Content= "Gravar" />
<!-- Controle responsável por exibir todos os estados já
persistidos -->
<DataGrid x:Name= "dgEstados" Grid.Row= "4"
Grid.Column= "1" AutoGenerateColumns= "True"
IsReadOnly= "True" >
</DataGrid>
319

## Página 336

8.5. LendoeescrevendodadosnabasededadospormeiodoEF CasadoCódigo
</Grid>
</Window>
Ocontrole DataGriddoWPFpermitequeumconjuntodedados(de
umabasededadosoucole ção)sejaexibidodemaneiratabular,semelhante
ao DataGridViewdo Windows Forms,porém,commaioresrecursos.As
funçõesbásicasoferecidasporestecontrolesão:gera çãoautomática(ouma-
nual)decolunas,sele çãodelinhasecolunas,agrupamentodedados,classi-
ficaçãoporcolunas,redimensionamentoereordenamentodascolunas,con-
gelamento(fixa ção)decolunas,dentreoutras.
Paraqueo DataGridpossaserpopuladocomosestadosjápersistidos
nabasededados,éprecisoaimplementa çãodeummétodoparaisso. Na
sequência,mostroummétodoquerecupera,pormeiodoEF,essesestados.
Resolução8.4:métodoqueretornaumalista
private IList<Estado> GetEstados() {
using ( var context = new EFContext()) {
return context.Estados.ToList<Estado>();
}
}
Pararetornartodososestadospersistidos,pormeiodoEF,éprecisoter
disponívelocontextodeacessoabasededados,queéfornecidopelaclasse
EFContext(Resolução8.2).Pormeiodocontexto,obtém-seapropriedade
Estados,queéuma IQueriable<Entity>e,então,aconsultaérealizada
pormeiodainvoca çãoaométodo ToList(),quetransformaoresultadoem
umalistagenérica.
Nasequência,éprecisocriarummétodoquesejaresponsávelporatuali-
zaro DataGrid,quesofreráatualiza çãoquandoajanelaforinstanciadaea
cadainser çãoqueocorrer.Apreferênciaemcriarummétodoespecíficopara
issoestáligadaaosprincípiosderesponsabilidadesdosmétodos.
OmétodoGetEstados()temaresponsabilidadedefornecerosdados,
enãodeatualizaro DataGrid. Aseguir,apresentoométodoresponsável
poratualizaro DataGrid.
320

## Página 337

CasadoCódigo Capítulo8. ApresentandooEntityFrameworkcomoferramentapara...
Resolução8.5:métodoqueatualizaoDataGrid
private void RefreshDataGrid () {
dgEstados.ItemsSource = GetEstados();
}
Comopodeserverificadonocódigodométodo RefreshDataGrid(),
apropriedadedo DataGridresponsávelpormanterosdadosaseremexi-
bidoséa ItemsSource,querecebeoretornodométodo GetEstados().
EssapropriedadetambémpodeserconfiguradanocódigoXAML,quando
existeum Binding(ligação)docontrolecomumafontededados.
Aprimeirainvoca çãoaessemétododeveocorrernainstancia çãodaja-
nela,ouseja,noconstrutordaclassequearepresenta.Vejaaseguir.
Resolução8.6:métodoConstrutordaclassequerepresentaaJa-
nela
public MainWindow () {
InitializeComponent();
RefreshDataGrid();
}
Ao executar a aplicação pela primeira vez, nada será exibido no
DataGrid,poisnadafoiinserido. Narealidade,nemabasededadosea
tabelaforamconstruídas.Paraainser çãodosdadosinformadosnajanela,é
precisoummétodoespecíficoparaisso,queéapresentadonasequência.
Resolução8.7:métodoquerealizaainser çãodeumestadonabase
dedados
private Estado SaveEstado (Estado estado) {
using ( var context = new EFContext()) {
context.Estados.Add(estado);
context.SaveChanges();
}
return estado;
}
321

## Página 338

8.5. LendoeescrevendodadosnabasededadospormeiodoEF CasadoCódigo
Verifiquequeoprocedimentodeobten çãodocontextoparaacessoàbase
dedadospeloEFéomesmoapresentadona Resolução8.4,tendocomoal-
teraçãoainvoca çãoaométodo Add()dapropriedade Estados,enviando
oobjetorecebidocomoargumento.
Nesteexemplo,foirealizadaapenasumainser çãodeobjetosgerenciáveis
pelocontexto.Entretanto,épossívelqueocorramvárias,sendoque,aofinal
dessasopera ções,éprecisoinvocarométodo SaveChanges()oferecido
pela DbContext.
Oretornodomesmoobjetorecebidoaométodochamadorpermiteque
atualizaçõesrealizadasduranteoprocessodeatualiza çãosejamdisponibili-
zadasparaaaplica ção,comoéocasodovalorparaapropriedade Id,queé
geradaquandooobjetoépersistido.
Paraqueumapropriedadedeumaclassesejaidentificadacomochave
primáriaparaatabela,bastaquesejanomeadade Id.Casoprecisenomear
apropriedadequerepresentaachaveprimáriacomoutronome,serápreciso
fazerusode Data Annotations.
Paraqueosdadosinformadospelousuáriopossamserpersistidospor
meiodométodo SaveEstado(),implementeocódigoquetragoaseguir,
nométodoquecapturaoevento Clickdobotão Gravar.
Resolução8.8:métodoquecapturaoeventoClickdobotãoGravar
private void btnGravar_Click ( object sender,
RoutedEventArgs e) {
var estado = SaveEstado( new Estado(){
UF = txtUF.Text,
Nome = txtNome.Text
});
txtID.Text = estado.Id.ToString();
RefreshDataGrid();
}
Comessaimplementa ção,executeaaplica ção,insiraumestadoeveja
que,apósaexecu ção,o DataGridoexibe.Fecheaaplica çãoeexecuteno-
vamente,oestadodeveaparecer.
322

## Página 339

CasadoCódigo Capítulo8. ApresentandooEntityFrameworkcomoferramentapara...
8.6 Identificando as ações do Entity Fra-
mework
Talvez,aprimeiradúvidanaexecu çãodoprojetosejasaberondefoicriadaa
basededados.Porpadrão( default),oEntityFrameworkcria-aautomatica-
mente,poisnenhumainforma çãosobreelafoiregistradanaaplica çãocriada.
A instância do SQL Server utilizada depende dos recursos que
você instalou em sua máquina: ou SQL Server completo, ou o Ex-
press Edition, ou ainda o Local Db. A base de dados é criada, por
padrão, com o nome qualificado. Para o exemplo, o nome usado
foi EFApplication.Contexts.EFContext, ou seja,NomeDoPro-
jeto.Namespace.Classe.ParavisualizaremanipularabasededadosnoVi-
sualStudio,najanela Server Explorercliquecomobotãodireitoem
Data Connectionse,emseguida,em Add Connection(figura8.8).
Fig.8.8:AdicionandoumanovaconexãocomoSQLServerExpress
Najanelaqueseabre,informeoendere çodoservidoreainstânciado
SQLServerExpress,edepoisselecioneabasededados,quedeveaparecerna
listadasdisponíveis(figura 8.9).
323

## Página 340

8.6. IdentificandoasaçõesdoEntityFramework CasadoCódigo
Fig.8.9:ConfigurandoaconexãocomabasecriadapeloEntityFramework
Apósterconfiguradoetestadoaconexão,confirmesuacria çãoclicando
nobotão OK,everifiquequeelaapareceno Server Explorer(figura8.10).
Fig.8.10: VisualizaçãodabasededadosetabelascriadaspeloEntityFra-
mework
Verifiquenalistadetabelasaexistênciadeduas: _MigrationHistory
324

## Página 341

CasadoCódigo Capítulo8. ApresentandooEntityFrameworkcomoferramentapara...
e Estadoes.Aprimeirafazpartedeumrecurso,quenãoserátrabalhado
nestelivro,chamado Code First Migration,easegundarepresentaos
estadospersistidos.Notequeonomedatabelasofreuumprocessode plura-
lização,porém,seguindooidiomainglês.Essapluraliza çãopodeserdesabi-
litada.
OEntityFrameworkCodeFirstMigration éumrecursooferecidopelo
EFparaauxiliarnasatualiza çõesrealizadasemumabasededados.Normal-
mente(eprincipalmente)quandosedesenvolveumaaplica ção,omodelode
negóciosofrealtera ções,eestasrefletemnabasededadosenaestruturadas
tabelasquandoutilizamosoEF.
Realizarestecontroledemaneiramanualéumtrabalhoárduo.Normal-
mente,odesenvolvedorrecorreaferramentasdeterceirosparaessaatividade.
OEF6trouxeoEntityFrameworkCodeFirstMigrationparasubsidiaressa
atividade.Apesardenãoserpartedoescopodestelivro,ahabilita çãodesse
recursoocorreporpadrão,mastambémpodeserdesabilitada.Recomenda-
seainvestiga çãoeusoefetivoemseusprojetosdoMigrations.
CodeFirstéumadasestratégiasdisponibilizadaspeloEntityFramework
paraomapeamentoentreobjetosetabelas(ORM)eéautilizadanestelivro,
naqualsedefineomodelodenegócio. Pormeiodessemodelo,oEFcriae
mantématualizadaabasededadosepermiteaintera çãocomosdados,para
assimobter,fornecer,atualizareremoverobjetos.
AsdemaisestratégiasModelFirsteDatabaseFirstnãofazempartedo
escopodestelivro,maséinteressanteumainvestiga çãosobreelas,principal-
menteseforrealizadoumdesenvolvimentosobreumabasededadosexis-
tente.
8.7 A inicialização da base de dados
OfluxoseguidopeloEFnoprocessodeinicializa çãodabasededados,no
exemploapresentado,foiodeverificarseoconstrutordaclassequeestende
DbContext(EFContext,nocaso)recebeuma Connection String.Se
essacondi çãofosseverdadeira,aconfigura çãorecebidaconteriaasdefini ções
paracriarabasededados,ouabri-lacasojáexistisse.
Comonoexemplonãofoipassadauma Connection String,oEF
325

## Página 342

8.8. Implementandoassociações/relacionamentos CasadoCódigo
passaàsegundaverifica ção,queéadeoconstrutorreceberuma stringque
contémonomedabasededadosqueserácriada,ouabertacasoelaexista.O
queocorreunoexemplotrabalhadoéquenemuma Connection String
nemuma stringcomonomeparaabasededadosfoiinformada,oque
resultounacria çãodabasededadoscomonomequalificado.
Adapteaimplementa çãodaclasse EFContext,deacordocomoapre-
sentadoaseguir.
Resolução8.9:classequerepresentaráocontextocomabasede
dados(Versão2)
using System.Data.Entity ;
using EFApplication.POCO ;
namespace EFApplication.Contexts {
public class EFContext : DbContext {
public EFContext () : base ( "EF_Intro" ) {}
public DbSet<Estado> Estados { get ; set ; }
}
}
Executeaaplica ção. Notequeosestadosinseridosanteriormentenão
existemmais,poisumanovabasededadosfoicriadacomamudan çarea-
lizadanaclasse EFContext. NoServer Explorer,adicioneessanova
basededados,damesmamaneiraqueinseriuaanterior. Paratestarcom
uma Connection String,crie-ano app.configeinformenoconstru-
toronomedadoaela.
8.8 Implementando associações / relaciona-
mentos
ParaimplementarnoEFassocia çõesentreclassesquesemapeiamemrela-
cionamentosdetabelas,aprincípiosegue-seoconceitobásicodeOrienta-
çãoaObjetos,trazendoapenasalgumascaracterísticasquepossibilitemuma
melhornavega ção(navegabilidade)entreosobjetosdaassocia ção.Aseguir,
apresentoaclasse Cidade,queseassociacom Estado.
326

## Página 343

CasadoCódigo Capítulo8. ApresentandooEntityFrameworkcomoferramentapara...
Resolução8.10:implementa çãodaclasseCidade
public class Cidade {
public long Id { get ; set ; }
public string Nome { get ; set ; }
public long EstadoId { get ; set ; }
public virtual Estado Estado { get ; set ; }
}
Verifiquenocódigodaclassequeareferênciaparaumobjeto Estado
ocorrededuasmaneiras.Naprimeira,ondeapropriedade EstadoIdpossui
otipo long,éarmazenadaachaveestrangeiradeestado,ouseja,achavepri-
máriadatabela Estado.Asegundamaneiraespecificaumapropriedadedo
tipo Estado,precedidadapalavra-chave virtual.Métodoseproprieda-
desdefinidoscomovirtuaispermitemasobrescrita( override)porsubclasses
emC #,queéumprocessoqueocorrequandousamosframeworks,comoo
EF.Assim,aoimplementarmosumasubclassede Cidade,oEFpodeaplicar
oprocessodecargatardia( lazy loading).
Quandoummodelodenegóciopossuiclassesassociadas,oframework
deORM(EF)precisatrazer,alémdoobjetorecuperado,o(s)objeto(s)associ-
ado(s)aele(registro).Esteprocessoprecisaserbempensado,paranãocausar
umasobrecargadesnecessárianaaplica ção.
Pensandonaassocia çãopropostade Estadoe Cidade,éprecisoavaliar
se,aorecuperarumestado,todasascidadespertencentesaeletambémpre-
cisamsercarregadasnomesmomomento( eager),ouapenasquandoforem
necessáriasparaaaplica ção( lazy).
OEntityFrameworkoferecesuporteparatrêsestratégiasderecupera-
çãodedadosdeumaassocia ção/relacionamento: eager loading, lazy
loadinge explicit loading.Esteúltimopodeserutilizadoquandote-
moso lazy loadingdesativadopor default,masemalgummomento
sedesejequecertaassocia çãotenhaumacargatardia.
Paragarantirumaassocia çãocomnavegabilidadebidirecional,épreciso
alteraraclasse Estado,conformemostradonasequência.
327

## Página 344

8.8. Implementandoassociações/relacionamentos CasadoCódigo
Resolução8.11:classedenegócioEstado(Versão2)
public class Estado {
public long Id { get ; set ; }
public string UF { get ; set ; }
public string Nome { get ; set ; }
public virtual List<Cidade> Cidades { get ; set ; }
}
Mesmonãotendoimplementadoumainterfacecomousuário(Janela)
paraoregistrode Cidades,executesuaaplica ção.Duranteaexecu ção,uma
janeladeerrosemelhanteàdafigura 8.11seráexibida.
Fig.8.11:Errodevalida çãodemodeloencontradopeloEntityFramework
328

## Página 345

CasadoCódigo Capítulo8. ApresentandooEntityFrameworkcomoferramentapara...
8.9 E stratégias para inicialização da base de
dados
Vamosrecapitular:naprimeiraetapadaaplica çãodeexemplo,apenasuma
classefoiimplementadaeaexecu çãoocorreusemproblemaalgum.Abasede
dadosfoicriada,registrosforaminseridos,aaplica çãofoifechadaeiniciada
outrasvezes,etudoocorreuperfeitamente.Jánasegundaetapa,foiaplicado
oconceitodeassocia ção,pormeiodaimplementa çãodaclasse Cidadeedas
propriedadesrelacionadas.Aoexecutar,aexce çãoapresentadanafigura 8.11
ocorreu.Essaexce ção( System.InvalidOperationException)ocorre
pelofatodeque,nomomentoemqueoEFbuscaocontexto( EFContext)
comabasededados,umavalida çãodomodelodenegócio(classes)comas
tabelas(basededados)érealizadae,comomudan çasforamfeitas,elasnão
casam–conformeinformaçãoadicionalnajaneladaexce ção: Additional in-
formation: The model backing the ‘EFContext’ context has changed since the
database was created. Consider using Code First Migrations to update the da-
tabase(http://go.microsoft.com/fwlink/?LinkId=238269).
Oqueseesperaéque,quandoaltera çõesforemrealizadasnomodelode
negócio(classes),estasatualiza çõessejampropagadasparaabasededados.
Paraisso,éprecisopensaremestratégiasparainicializa çãodocontextocoma
basededados,ouseja,oqueoEFdeverealizarquandoforrealizaraconexão.
Existemquatropossíveisestratégias:
•CreateDatabaseIfNotExists: éaestratégiapadrãoparaoEF.
Comopodesercompreendidopelonome,abasededadosserácriada
casoelanãoexista,aorealizaraconexão.Entretanto,quandomodifi-
caçõessãofeitasnomodelodenegócio,aoexecutaraaplica ção,háa
ocorrênciadeexceções,quefoioqueaconteceunoexemploanterior.
•DropCreateDatabaseIfModelChanges:fazendousodessaestra-
tégia,quandoocorreraltera çõesnomodelodenegócio,abasededados
éremovidaeumanovaécriada,casoelaexista.Essadeveriaseraes-
tratégiaparaoexemploapresentado. Entretanto,sesuaaplica çãojá
possuirdadosqueforaminseridosparatestes,elesvãoserperdidos.O
EFoferecerecursosparapopularumabasededadoscomdadospara
testes.
329

## Página 346

8.9. Estratégiasparainicializaçãodabasededados CasadoCódigo
•DropCreateDatabaseAlways:novamente,aleituradonomedessa
estratégiapermiteidentificarseucomportamento,queéremoverecriar
umanovabasededados,semprequeaaplica çãoforexecutada.
•Custom DB Initializer:pormeiodessaestratégia,épossívelper-
sonalizaramaneiracomoainicializa çãodo contextcomabasede
dadosdeveocorrer.
Parautilizarumadasestratégias,éprecisoregistrarautiliza çãonaclasse
decontexto.Adapteaclasse EFContext,conformemostradoaseguir.
OusodoMigrationsminimizaessesproblemasdeatualiza çãodabasede
dados.Considereseuusoemprojetosfuturos.
Resolução8.12:classequerepresentaráocontextocomabasede
dados(Versão3)
using System.Data.Entity ;
using EFApplication.POCO ;
namespace EFApplication.Contexts {
public class EFContext : DbContext {
public EFContext () : base ( "EF_Intro" ) {
Database.SetInitializer<EFContext>(
New
DropCreateDatabaseIfModelChanges<EFContext>()
);
}
public DbSet<Estado> Estados { get ; set ; }
}
}
Executeaaplica ção.Verifiquequeosestadosanteriormenteinseridosnão
existemmais.Casosejadoseuinteresse,épossíveldesabilitarosinicializado-
res,enviando nullcomoargumentoparaométodo SetInitializer().
Destamaneira,nãoocorreráaperdadosdados,atéquevocêoreconfigure.
330

## Página 347

CasadoCódigo Capítulo8. ApresentandooEntityFrameworkcomoferramentapara...
8.10 Populando a base de dados com dados para
teste
Quandorealizamostestesemumaaplica ção,oidealéqueelapossuaumcon-
juntodedadosdisponibilizadoparaqueopera çõesefuncionalidades–que
nãosejamainser ção–possamsertestadas. Paraqueosdadospossamser
persistidosnomomentodainicializa çãodocontexto,éprecisocriarumini-
cializadorpersonalizado.Assim,implementeum Custom Initializer,
conformeapresentadoaseguir.
Resolução8.13:classequerepresentaráocontextocomabasede
dados(Versão3)
public class EFInitializer :
DropCreateDatabaseAlways<EFContext> {
protected override void Seed (EFContext context) {
IList<Estado> estados = new List<Estado>();
estados.Add( new Estado()
{ UF = "PR" , Nome = "Paraná" });
estados.Add( new Estado()
{ UF = "SC" , Nome = "Santa Catarina" });
estados.Add( new Estado()
{ UF = "SP" , Nome = "São Paulo" });
estados.Add( new Estado()
{ UF = "MS" , Nome = "Mato Grosso do Sul" });
estados.Add( new Estado()
{ UF = "CE" , Nome = "Ceará" });
foreach ( var estado in estados) {
context.Estados.Add(estado);
}
context.SaveChanges();
base .Seed(context);
}
}
331

## Página 348

8.10. Populandoabasededadoscomdadosparateste CasadoCódigo
Verifiquequeaclasseestende DropCreateDatabaseAlways<EFContext>,
oquefazesseinicializadorespecializar-separasempreremoverecriarabase
dedados.Essaestratégiafoiadotadaaqui,maspoderiaseroutra,conforme
anecessidade.
Nestaclasse,hátambémasobrescritadométodo Seed(),paraqueda-
dosparatestespossamserinseridosnabasededadoseestejamdisponíveisna
aplicação.Acompreensãoébásica:declara-seumacole ção,insere-senelaos
objetosqueprecisamserpersistidose,emseguida,érealizadaumaitera ção
pormeiodo foreach(),parainserirosobjetosem Estados,quepertence
aocontextocomabasededados.Aofinal,asaltera ções(inser ções)sãosalvas.
Éprecisoagoraatualizaraclassedecontextoparaquefa çausodesseini-
cializador.Aliás,parafinalizarapartedomodelodenegóciomapeadopelo
EF,devemosinserirapropriedade Cidades. Tudoissoéapresentadona
sequência.
Resolução8.14:classequerepresentaráocontextocomabasede
dados(Versão4)
using System.Data.Entity ;
using EFApplication.POCO ;
namespace EFApplication.Contexts {
public class EFContext : DbContext{
public EFContext () : base ( "EF_Intro" ) {
Database.SetInitializer(
new EFInitializer ()
);
}
public DbSet<Estado> Estados { get ; set ; }
public DbSet<Cidade> Cidades { get ; set ; }
}
}
332

## Página 349

CasadoCódigo Capítulo8. ApresentandooEntityFrameworkcomoferramentapara...
8.11 Criando a interface com o usuário para
aplicar a associação
Afigura8.12apresentaajanelaparaainser çãodedadosreferenteacidades.
Fig.8.12:Errodevalida çãodemodeloencontradopeloEntityFramework
A implementação visual para a janelaCidades é representada na
sequência.
Resolução8.15:XAMLparaajanelaCidades
<Window x:Class= "EFApplication.Cidades"
xmlns= "http://schemas.microsoft.com/winfx/2006/xaml/
presentation "
xmlns:x= "http://schemas.microsoft.com/winfx/2006/xaml"
Title= "Cidades" Height= "146.448" Width= "266.672"
WindowStartupLocation= "CenterScreen" >
<Grid>
<Grid.RowDefinitions>
<RowDefinition Height= "Auto" />
<RowDefinition Height= "Auto" />
<RowDefinition Height= "Auto" />
<RowDefinition Height= "Auto" />
</Grid.RowDefinitions>
<Grid.ColumnDefinitions>
<ColumnDefinition Width= "Auto" />
<ColumnDefinition Width= "200" />
</Grid.ColumnDefinitions>
333

## Página 350

8.11. Criandoainterfacecomousuárioparaaplicaraassocia ção CasadoCódigo
<Label Grid.Row= "0" Grid.Column= "0" Content= "Id:" />
<Label Grid.Row= "1" Grid.Column= "0"
Content= "Estado:" />
<Label Grid.Row= "2" Grid.Column= "0" Content= "Nome:" />
<TextBox x:Name= "txtID" Grid.Column= "1" Grid.Row= "0"
IsEnabled= "False" Margin= "0,0,152,0" />
<ComboBox x:Name= "cbxEstados" Grid.Row= "1"
Grid.Column= "1" />
<TextBox x:Name= "txtNome" Grid.Column= "1"
Grid.Row= "2" />
<Grid Grid.Row= "3" Grid.ColumnSpan= "2" >
<Grid.RowDefinitions>
<RowDefinition Height= "5" />
<RowDefinition Height= "Auto" />
</Grid.RowDefinitions>
<Button x:Name= "btnGravar" Grid.Row= "1"
Content= "Gravar" />
</Grid>
</Grid>
</Window>
Comajaneladesenhadacomum ComboBoxparaapresentarosestados
disponíveis,éprecisoimplementarométodopararetornarosestadosqueo
popularão.Vejaocódigoaseguir.
Resolução8.16:implementa çãodométodoquerecuperaosesta-
dospersistidos
private IList<Estado> GetEstados() {
using ( var context = new EFContext()) {
return context.Estados.OrderBy(
estado => estado.Nome).ToList<Estado>();
}
}
Observe que, em relação ao método de mesmo nome para a janela
Estados,adiferen çadessemétodoestánaclassifica çãodosestados(por
nome), que, aprincípio, poderiatambémtersidorealizadanajanelade
Estados. Destamaneira,éinteressantepensaremumareutiliza ção,por
334

## Página 351

CasadoCódigo Capítulo8. ApresentandooEntityFrameworkcomoferramentapara...
meiodeumaclasse DAL(Data Access Layer). Nasequência,éprecisoim-
plementarummétodoquepopuleo ComboBox.Vejatudoissoaseguir.
Resolução8.17:implementa çãodométodoquepopulaeconfigura
oComboBox
private void PopulateComboBoxEstados () {
cbxEstados.ItemsSource = GetEstados();
cbxEstados.DisplayMemberPath = "Nome" ;
cbxEstados.SelectedValuePath = "Id" ;
}
A maneira como foi apresentada a configuração de ComboBox em
Windows FormsésemelhanteàquelaquandofeitaemWPF,alterandoape-
nasonomedaspropriedades. Apropriedade ItemsSource,talqualno
DataGrid,éresponsávelpormanterositensquepopularãoo ComboBox.
Resta agora invocar o métodoPopulateComboBoxEstados() no
construtor.Vejaocódigonasequência.
Resolução8.18:métodoconstrutorcomchamadaaométodoPo-
pulateComboBoxEstados()
public partial class Cidades : Window {
public Cidades () {
InitializeComponent();
PopulateComboBoxEstados();
}
// Código omitido
}
Comadisponibilidadedosestadosno ComboBox,éprecisoimplementar
oprocessodepersistênciadosdadosreferentesà Cidadequeseráregistrada.
Vejaocódigoaseguir.
Resolução8.19:métodoquepersisteumacidade
private Cidade SaveCidade (Cidade cidade) {
using ( var context = new EFContext()) {
335

## Página 352

8.12. AplicandoBindingdeobjetosemumCRUD CasadoCódigo
context.Cidades.Add(cidade);
context.SaveChanges();
}
return cidade;
}
Finalizandoestafuncionalidade,éprecisoimplementarométodoque
capturaoevento Clickdobotão Gravar.Vejaaseguir.
Resolução8.20:métodoquecapturaoeventoClickdobotãoGra-
var
private void btnGravar_Click ( object sender,
RoutedEventArgs e){
var cidade = SaveCidade( new Cidade() {
EstadoId = ( long ) cbxEstados.SelectedValue,
Nome = txtNome.Text
});
txtID.Text = cidade.Id.ToString();
}
Executeaaplica ção,insiraumacidadee,depois,confirmeainser çãono
Server Explorer.
8.12 AplicandoBinding de objetos em um CRUD
Osprimeirospassosparaaimplementa çãodasopera çõesrelativasaum
CRUDsão:ainser çãodebotõesquepossamimplementarasfuncionalida-
des;um DataGrid,paraqueosdadospersistidospossamserselecionados;
eaalimenta çãodedadosparatestes,nocaso,novascidades.
Aseguir,apresentoumanovaversãoparaométodo Seed()daclasse
EFInitializer,ondeobjetosquerepresentamascidadessãoinseridosna
basededados.
Resolução8.21:classequerepresentaumInitializerpersonalizado
paraocontextoeaestratégiadesempreremoverecriarabasede
dados(Versão2)
336

## Página 353

CasadoCódigo Capítulo8. ApresentandooEntityFrameworkcomoferramentapara...
public class EFInitializer :
DropCreateDatabaseAlways<EFContext> {
protected override void Seed (EFContext context) {
IList<Estado> estados = new List<Estado>();
estados.Add( new Estado()
{ UF = "PR" , Nome = "Paraná" });
estados.Add( new Estado()
{ UF = "SC" , Nome = "Santa Catarina" });
estados.Add( new Estado()
{ UF = "SP" , Nome = "São Paulo" });
estados.Add( new Estado()
{ UF = "MS" , Nome = "Mato Grosso do Sul" });
estados.Add( new Estado()
{ UF = "CE" , Nome = "Ceará" });
foreach ( var estado in estados) {
context.Estados.Add(estado);
}
IList<Cidade> cidades = new List<Cidade>();
cidades.Add( new Cidade() { Estado = estados[ 0 ],
Nome = "Foz do Iguaçu" });
cidades.Add( new Cidade() { Estado = estados[ 1 ],
Nome = "Blumenau" });
cidades.Add( new Cidade() { Estado = estados[ 2 ],
Nome = "Itapetininga" });
cidades.Add( new Cidade() { Estado = estados[ 3 ],
Nome = "Três Lagoas" });
cidades.Add( new Cidade() { Estado = estados[ 4 ],
Nome = "Fortaleza" });
foreach ( var cidade in cidades) {
context.Cidades.Add(cidade);
}
context.SaveChanges();
base .Seed(context);
}
}
337

## Página 354

8.12. AplicandoBindingdeobjetosemumCRUD CasadoCódigo
Emrela çãoànovajanela,afigura 8.13aapresenta.
Fig.8.13:Janelapararealiza çãodasopera çõesrelativasaoCRUDdecidades
Vejanasequênciaaimplementa çãoparaajaneladafigura 8.13.
Resolução8.22:implementa çãodaJanelaparaCidades(Versão2)
<Window x:Class= "EFApplication.Cidades"
xmlns= "http://schemas.microsoft.com/winfx/2006/xaml/
presentation "
xmlns:x= "http://schemas.microsoft.com/winfx/2006/xaml"
Title= "Cidades" Height= "300" Width= "267"
WindowStartupLocation= "CenterScreen" >
<Grid>
<Grid.RowDefinitions>
<RowDefinition Height= "Auto" />
<RowDefinition Height= "Auto" />
<RowDefinition Height= "Auto" />
<RowDefinition Height= "Auto" />
// Nova linha inserida no Data Grid
338

## Página 355

CasadoCódigo Capítulo8. ApresentandooEntityFrameworkcomoferramentapara...
<RowDefinition Height= "Auto" />
</Grid.RowDefinitions>
<Grid.ColumnDefinitions>
<ColumnDefinition Width= "Auto" />
<ColumnDefinition Width= "200" />
</Grid.ColumnDefinitions>
<Label Grid.Row= "0" Grid.Column= "0" Content= "Id:" />
<Label Grid.Row= "1" Grid.Column= "0"
Content= "Estado:" />
<Label Grid.Row= "2" Grid.Column= "0" Content= "Nome:" />
// Inserida a propriedade Text nos TextBoxs e ComboBox, com
// binding no Data Grid
<TextBox x:Name= "txtID" Grid.Column= "1" Grid.Row= "0"
IsEnabled= "False" Margin= "0,0,152,0"
Text= "{Binding SelectedItem.Id,
ElementName=dgCidades, Mode=OneWay} "/>
<ComboBox x:Name= "cbxEstados" Grid.Row= "1"
Grid.Column= "1"
Text= "{Binding SelectedItem.Estado,
ElementName=dgCidades, Mode=OneWay} "/>
<TextBox x:Name= "txtNome" Grid.Column= "1"
Grid.Row= "2" Text= "{Binding SelectedItem.Nome,
ElementName=dgCidades, Mode=OneWay} " />
// Grid que terá os botões para o CRUD
<Grid Grid.Row= "3" Grid.ColumnSpan= "2" >
<Grid.RowDefinitions>
<RowDefinition Height= "5" />
<RowDefinition Height= "Auto" />
</Grid.RowDefinitions>
<Grid.ColumnDefinitions>
<ColumnDefinition Width= "64" />
<ColumnDefinition Width= "64" />
<ColumnDefinition Width= "64" />
<ColumnDefinition Width= "64" />
</Grid.ColumnDefinitions>
<Button x:Name= "btnNovo" Grid.Row= "1"
Grid.Column= "0" Content= "Novo" />
339

## Página 356

8.12. AplicandoBindingdeobjetosemumCRUD CasadoCódigo
<Button x:Name= "btnAlterar" Grid.Row= "1"
Grid.Column= "1" Content= "Alterar" />
<Button x:Name= "btnGravar" Grid.Row= "1"
Grid.Column= "2" Content= "Gravar" />
<Button x:Name= "btnRemover" Grid.Row= "1"
Grid.Column= "3" Content= "Remover" />
</Grid>
// Inserção do Data Grid
<Grid Grid.Row= "4" Grid.ColumnSpan= "2" >
<DataGrid x:Name= "dgCidades"
ItemsSource= "{Binding}"
AutoGenerateColumns= "True" IsReadOnly= "True" >
</DataGrid>
</Grid>
</Grid>
</Window>
Parapopularo DataGrid, ummétodoespecíficofoiimplementado
(Resolução8.23),semelhanteaoprocessoanteriormenteapresentadopara
ajaneladeestados.Entretanto,nastagsXAMLparao DataGrid,apropri-
edade ItemsSourceagoraédefinidacomovalor {Binding},indicando
queelaestaráligadaaoutroscontroles.
Resolução8.23:métodoqueselecionaascidadesqueserãoexibidas
noDataGrid
private IList GetCidades () {
using ( var context = new EFContext()) {
var query = (
from c in context.Cidades
orderby c.Nome
select new {
c.Id, c.Estado, c.Nome });
return query.ToList();
}
}
Naimplementa çãodométodo GetCidades(),umtipoanônimoécri-
340

## Página 357

CasadoCódigo Capítulo8. ApresentandooEntityFrameworkcomoferramentapara...
adonasele çãodoscamposqueserãoretornados.Paraocasode c.Estado,
éprecisoalterarométodo ToString()daclasse Estado,paraqueonome
doestadosejaexibido.Vejaaseguir.
Resolução8.24:classedenegócioEstado(Versão3)
public class Estado {
public long Id { get ; set ; }
public string UF { get ; set ; }
public string Nome { get ; set ; }
public virtual List<Cidade> Cidades { get ; set ; }
public override string ToString () {
return this .Nome;
}
}
Oseguintepassoéinvocarométodo GetCidades()parapopulare
atualizaro DataGrid.Vejaocódigonasequência.
Resolução8.25:métodoqueatualizaDataGrid
private void RefreshDataGrid () {
dgCidades.ItemsSource = GetCidades();
}
Achamadaaométodo RefreshDataGrid()ocorreemdoispontos:
noconstrutor(Resolução8.26)enométodoquecapturaoevento Clickdo
botão Gravar(Resolução8.27).
Resolução8.26:métodoconstrutorcomchamadaaométodoRe-
freshDataGrid()
public partial class Cidades : Window {
public Cidades () {
InitializeComponent();
PopulateComboBoxEstados();
341

## Página 358

8.12. AplicandoBindingdeobjetosemumCRUD CasadoCódigo
RefreshDataGrid();
}
// Código omitido
}
Resolução8.27:métodoquecapturaoeventoClickdobotãoGra-
varcomchamadaaométodoRefreshDataGrid()
private void btnGravar_Click ( object sender,
RoutedEventArgs e) {
var cidade = SaveCidade( new Cidade() {
EstadoId = ( long ) cbxEstados.SelectedValue,
Nome = txtNome.Text
});
txtID.Text = cidade.Id.ToString();
RefreshDataGrid();
}
Nasequência,paraqueoscontrolesdeentradadedados( TextBoxse
ComboBox)estejamligadosao DataGrid,equeosdadosdelasejamatuali-
zadosnessescontroles,aoseselecionarumacidade,éprecisorealizaralgumas
configurações. Aseguir,apresentoumfragmentodocódigoda Resolução
8.22,referenteàjanela Cidades.
Resolução8.28:trechodecódigodebindingcomDataGrid
// Inserida a propriedade Text nos TextBoxs e ComboBox, com
// binding no Data Grid
<TextBox x:Name= "txtID" Grid.Column= "1" Grid.Row= "0"
IsEnabled= "False" Margin= "0,0,152,0"
Text= "{Binding SelectedItem.Id,
ElementName=dgCidades, Mode=OneWay} "/>
<ComboBox x:Name= "cbxEstados" Grid.Row= "1"
Grid.Column= "1"
Text= "{Binding SelectedItem.Estado,
ElementName=dgCidades, Mode=OneWay} "/>
<TextBox x:Name= "txtNome" Grid.Column= "1" Grid.Row= "2"
Text= "{Binding SelectedItem.Nome,
ElementName=dgCidades, Mode=OneWay} " />
342

## Página 359

CasadoCódigo Capítulo8. ApresentandooEntityFrameworkcomoferramentapara...
Umcontrolecomliga ção( binding)comoutrocontroleprecisatê-lade-
finidaemsuapropriedadequereceberáovalordessaliga ção(nocaso, a
Text).Essaliga çãoinformaqualapropriedadequedaráorigemaosdados(
SelectedItem),qualéocontrolequeforneceráaliga ção( ElementName)
equaléoseumodo( Mode).
OWPFfornecerecursosricosesimplesparaqueoselementosdeintera-
çãocomousuáriopossamexibirdados.Oscontroles(elementos)podemser
ligadosaumagrandevariedadedefontesdedados,comorecursosdaCLR,
XMLecontrolesetc.
Quandoseligamcontroles,paraqueosdadosdeumpossamatualizarou-
tros,éprecisodefiniremqualdire çãoocorreessaliga ção/atualiza ção.Asatu-
alizaçõesdeliga çãopodemocorrer:apenasnapropriedadededestino( tar-
get),apenasnapropriedadedeorigem/fonte( source)ouemambas.Paraisso,
éprecisoatribuirotipodedirecionamentoaoatributo Mode,quepodeser
TwoWay, OneWay, OneTime, OneWayToSourceou Default.
Executeaaplica ção,selecioneumacidadeno DataGrideverifiqueseos
controlesreferentesaosdadosdelasãoatualizados.Nasequência,épreciso
implementarocomportamentodosbotõesreferentesaoCRUD.Oprimeiro
éobotão Novo,quedeverá“limpar”oscontroles,paraquenovosdados
possamserinformados.Vejaaseguir.
Resolução8.29:métodoquecapturaoeventoClickdobotãoNovo
private void btnNovo_Click ( object sender, RoutedEventArgs e) {
dgCidades.UnselectAll();
}
Umavezqueosdadosdoscontrolesdeintera çãoestãoligadoscomo
DataGrid,aoremovermossuasele ção,oscontrolessãoautomaticamente
“limpados”,sendopossívelainserçãodeumnovoregistro.Testeestafuncio-
nalidade.
Nasequência,éprecisoimplementararemo çãodeumacidade.Paraisso,
ummétodoespecíficoprecisasercriado,conformeapresentoaseguir.
343

## Página 360

8.12. AplicandoBindingdeobjetosemumCRUD CasadoCódigo
Resolução8.30:métodoresponsávelpelaremo çãodeumacidade
private void RemoveCidade ( long idCidade) {
using ( var context = new EFContext()) {
var cidade = context.Cidades.Find(idCidade);
context.Cidades.Remove(cidade);
context.SaveChanges();
}
}
Observeque,paraaremo çãodeumacidade,oobjetoquearepresenta
precisouserrecuperadoetrazidoparaocontexto.Esteprocedimentoéne-
cessárioparaqueoEFcompreendaqueoobjetoenviadocomoargumento
nãoéumobjetodesconectado( detached).
Parainvocarométodo RemoveCidade(),implementeocódigoaseguir
nométodoquecapturaoevento Clickdobotão Remover.
Resolução8.31:métodoquecapturaoeventoClickdobotãoRe-
mover
private void btnRemover_Click ( object sender,
RoutedEventArgs e) {
RemoveCidade(Convert.ToInt64(txtID.Text));
RefreshDataGrid();
}
FinalizandooCRUDparacidades,éprecisoimplementarafuncionali-
dadeparaobotãodealtera çãodeumacidade.Vejaaseguir.
Resolução8.32:métodoparaatualiza çãodeumacidade
private void UpdateCidade (Cidade cidade) {
using ( var context = new EFContext()) {
var newCidade = context.Cidades.Find(cidade.Id);
newCidade.Nome = cidade.Nome;
newCidade.EstadoId = cidade.EstadoId;
context.SaveChanges();
}
}
344

## Página 361

CasadoCódigo Capítulo8. ApresentandooEntityFrameworkcomoferramentapara...
Vejanocódigodométodo UpdateCidade()queumacidadeérecu-
perada;nelasãoatualizadasaspropriedadesenãohánenhumachamadaa
algummétodoparaatualizaranovacidade. Essaatualiza çãoéfeitadema-
neiraautomáticapeloEF,poisoobjetoalteradopertenceaocontextocoma
basededados.
Achamadaaessemétodoérealizadanométodoquecapturaoevento
Clickdobotão Alterar.Vejaocódigoaseguir.
Resolução8.33:métodoquecapturaoeventoClickdobotãoAlte-
rar
private void btnAlterar_Click ( object sender,
RoutedEventArgs e) {
UpdateCidade( new Cidade() {
Id = Convert.ToInt64(txtID.Text),
Nome = txtNome.Text,
EstadoId = ( long ) cbxEstados.SelectedValue
});
RefreshDataGrid();
}
8.13 Conclusão
Ousodeumaferramentaquesubsidieomapeamentoautomáticodeobje-
tosparaumabasededadosrelacional–etambémocaminhoinverso,no
qualregistrossãomapeadosparaobjetos–éumarealnecessidadeemaplica-
çõesorientadasaobjetos. OEntityFramework,apresentadonestecapítulo,
permitequeaequipededesenvolvimentoconcentre-senalógicadenegócio,
nãosepreocupandoemcomoosdadosserãoarmazenadose/ourecuperados.
TampoucoháamescladecódigoOOcominstru çõesSQL.
OconteúdoapresentadosobreoEFnestecapítulonãoesgotouosre-
cursos,característicasetécnicaspossíveisdeseremaplicados. Osexemplos
limitaram-seaapresentaromapeamentoporconven ção,ondenenhumcó-
digoadicionalfoiimplementadonasclasses.Casoalgumaconfigura çãoseja
necessária,épossívelcustomizaramaneiracomooEFvisualizaráaclassede
negócio,emrela çãoàbasededados,fazendousode Data Annotations.
345

## Página 362

8.13. Conclusão CasadoCódigo
Comvistasparaaaplica çãodoEF,foiusadonovamenteoWindows
PresentationFoundation,trazendotambémnovosrecursos,comoousode
ComboBoxedeliga çõesentrecontroles.
Estecapítulofinalizaapropostadolivro.Agoraficaparavocêodesafio
deaplicartodooconhecimentoadquiridoemsuasaplica çõesfuturas.
346

## Página 363

Capítulo9
Osestudosnãoparamporaqui
O.NETjánãoéumanovidade,éumaplataformaestávelquevemganhando
cadavezmaisadeptosequetrouxeumanovaepoderosalinguagem,oC #,
comumacurvadeaprendizadorelativamenteboa.Umdosrecursosofereci-
dosporeleéodesenvolvimentodeaplica çõesparadesktop,sendoesteoobje-
tivodestelivrocujaleituravocêacaboudeconcluir,usandoconstantementeo
C#emtodososcapítulos.Paraodesenvolvimentodestetipodeaplicativo(e
detodososoferecidospelo.NET),aMicrosoftdisponibilizouoVisualStudio,
quetemversõespagasegratuitas.
Paraquevocêpudesseseambientardemaneiragradativacomaplata-
forma,alinguagemeoambientededesenvolvimento,atécnicausadanospri-
meiroscapítulosfoideapresentarresolu çõesbásicas,fazendousodasprinci-
paisestruturasdeimplementa çãodealgoritmos:sequencial,condicionalede
repetição.ComoC #éumalinguagemtotalmenteorientadaaobjetos,concei-
tosdesteparadigmatambémforamapresentados,todoscomaplica çõesque

## Página 364

CasadoCódigo
permitiramsuasimplementa ções.
Astecnologiasoferecidaspelo.NETsãodiversasealgumasdelasforam
apresentadasduranteolivro.Paraacessoàbasededados,aplataformaofe-
receoADO.NET,quepossuiumahierarquiadeclasses,possibilitandouma
conexão,consultaeatualiza ção. Dentrodestasclasses,existeo DataSet,
quepermitetrazeraestruturadeumabasededadosparaasuaaplica çãoe
trabalharcomelalocalmente,namemóriadamáquinadocliente.
OutratecnologiavistafoioLINQ,quepermiteconsultasacole çõesde
dados,sejamelasbaseadasnaAPICollectionsouemumabasededados.Foi
apresentadooEntityFrameworks(EF),umpoderosogerenciadordemapea-
mentodeobjetosparaumabaserelacional(evice-versa)–conhecidotambém
comoORM–,comotambémumframeworkparadesenvolvimentodeaplica-
çõesdesktop,oWindowsPresentationFoundation(WPF),utilizadotambém
deformaintrodutórianestelivro.
Espera-sequecomosrecursosetécnicasexibidos,algunstenhamprovo-
cadoemvocêumacuriosidadeouinteresseemumaprofundamento,oque
certamenteagorasetornarámaisfácil. ProgramarcomC #émuitobom,e
criaraplica çõesusando.NETnãoédifícil.
Comeceagoraacriarsuasprópriasaplica ções. Quandosurgiremdi-
ficuldades, você verá que a comunidade existente na internet, disposta
a lhe auxiliar, é muito grande. Vale relembrar do grupo de discus-
são deste livro em específico: https://groups.google.com/forum/#!forum/
livro-windows-forms-casa-do-codigo.
Sucesso,equeafor çaestejacomvocê!;-)
348

## Página 365

CasadoCódigo ÍndiceRemissivo
ÍndiceRemissivo
Abstração,114
Application–XAML,297
Assinaturademétodos,24
Associação,118
Associaçãodireta,119
Autoincremento,172
Autosize,40
BackColor,35
BCL–BaseClassLibrary,121
BindingSource,79
BorderStyle,40
Break,109
Button,15
Códigohash,75
Campo,73,172
CellClick,191
Chaveprimária(Primarykey),172
CheckedChanged,51
Classe,114
Classes,6
ClearSelection(),137
CodeFirst,325
Coleções(Collections), 79
Coluna,172
ComboBox,149
Comentários,48
Comportamentos,113
Composição,119
ConnectionString,177
Construtores,21
Container,49
Continue,109
ControlBox,29
Conversões,31
Createtable,173
DAL–DataAccessLayer,193
DataColumn,286
DataGrid–WPF,320
DataRow,286
DataRowView,286
DataTable,184
DateTime,46
DateTimePicker,47
DDL–DataDefinitionLanguage,173
Debug(depura ção),19
DefaultExt,92
DER–DiagramadeEntidadeseRe-
lacionamentos,199
do...while(),105
Enabled,35
EntityFrameworkCodeFirstMigra-
tion,325
349

## Página 366

ÍndiceRemissivo CasadoCódigo
Escopo,31
Estruturacondicional,37
Estruturaderepeti ção,70
Estruturasequencial,2
Filter,92
Focus,42
Font,34
ForeColor,34
Form,10
FormBorderStyle,11
Formulário,10
Generics,122
Grid–XAML,297
GroupBox,50
Guid,119
Herança,7
ID–Injeçãodedependência,146
IDE–IntegratedDevelopmentEnvi-
ronment,7
Identidade,172
If(),41
IList,79
Image,15
ImageAlign,15
IndexOf,159
InnerJoin,265
Interface,80
IoC–InversãodeControle,146
IsNullOrWhiteSpace,107
Label,12
Length,42
LINQ–LanguageINtegratedQuery,
293
Location,13
Métodos,113
Métodos de extensão (Extension
methods),308
Métodosestáticos,24
Main(),26
Manutenibilidade,54
Matriz,117
MaximizeBox,29,142
MenuStrip,143
MER–ModelodeEntidadeseRela-
cionamentos,199
MessageBox,24
MinimizeBox,29
Modificadoresdeacesso,129
MVC–Model-View-Controller,71
Name,12
Namespace,18
Now,47
NuGet,312
Objeto,6,112
Operadorternário,138
Operadoreslógicos,44
Operadoresrelacionais,42
Overriding(Sobrescrita),75
partial,18
Polimorfismo,80
Propriedade,73
Propriedades,112
350

## Página 367

CasadoCódigo ÍndiceRemissivo
RadioButtons,50
ReadOnly,30
Registro,172
Reutilização,54
Sealed,188
SelectedIndex,152
SelectedItem,154
Service-baseDatabase,168
Show(),24
Singleton,189
Size,12
Sobreposição,24
Solução(Solution),3
SolutionExplorer,4
SQL–StructuredQueryLanguage,
173
SqlCommand,181,182
SqlCommandBuilder,184
SqlConnection,181
SqlDataAdapter,184
StartPosition,33
Static,188
StreamReader,96
StreamWriter,108
TabControl,223
Tabela(Table),172
Text,11,39
TextAlign,16
TextBox,14
TextChanged,53
Tiposanônimos,75
Title,92
ToolStripMenuItem,145
ToShortDateString(),47
ToString(),31
Tratamentodeexce ções,54
Trim(),42
TryParse,107
Tupla,172
UseMnemonic,39
Usingstatement,186
Volatile,188
while,97
WindowState,142
WPF–WindowsPresentationFoun-
dation,293
XAML–eXtensibleApplicationMar-
kupLanguage,297
351