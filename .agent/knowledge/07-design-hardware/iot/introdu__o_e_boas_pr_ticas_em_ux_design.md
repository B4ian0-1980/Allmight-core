---json
{
  "id": "introdu__o_e_boas_pr_ticas_em_ux_design",
  "title": "Introdução e boas práticas em UX Design",
  "categoria": "07-design-hardware",
  "subcategoria": "iot",
  "resumo": "**Arquivo Original:** `Introdução e boas práticas em UX Design.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "boas",
    "design",
    "hardware",
    "introdu",
    "iot",
    "ticas"
  ],
  "perguntas_tipo": [
    "Como utilizar Introdução e boas práticas em UX Design?",
    "Quais as boas praticas de iot?"
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
  "dono": "stack-iot",
  "prioridade": 2
}
---

# Introdução e boas práticas em UX Design

> **Arquivo Original:** `Introdução e boas práticas em UX Design.pdf`
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

CasadoCódigo
Prefácio
Porqueprodutosouserviçosdigitaissimilaresfazemmaissucessodoque
outros?Umfatordepesoestánarelaç ãoentreousuárioeoproduto.Nesse
mundoconectadoemquevivemos,cadavezmaisganhafor çaoquecon-
sideroantropocentrismodigital:ousuárioéorei. Seelenãotemumaboa
experiênciacomoprodutodigital,eledeixadeutilizá-loemigraparainter-
facesmaisinteligentes,agradáveisedefáciluso.Eodiferencialdoproduto
ouserviçodigitalpoderesidirjustamenteali.
Sevocêtrabalhacomalgumprodutoouserviçodigital,ouusaodigital
(website,mobileapp)paracomunicar-secomseupúblico,esselivroéobri-
gatórioemsuabiblioteca–mesmoquevirtual.
Nãotemostempoparalermanuais–seguimospadrõescognitivosde
navegaçãocadavezmaisintuitivos.Umsistemapodeserextraordinárioem
termosdacomplexidadededesenvolvimento,otimizaç ãonoprocessamento
computacionaloudasintegraçõescomNoutrossistemasonline. Seaquela
camadadosoftwarequefazainterfacecomousuárionãoéagradavelmente
usável,oresultadodetodooseuincríveltrabalhotecnológicodebastidores
podetersidoemvãoounegativamenteimpactado,poisnãoatingiuquem
deveria:ousuáriofinal.
SeoprofissionaldeUXjáfazpartedesuavidacomodesenvolvedorevocê
achaqueoentregáveldelerestringe-seawireframes,vocêveránesselivroque
existemuitomaisciêncianoseutrabalho,explorandoo userjourney, user
stories,blueprint,passandoporpersonasemapeamentodoecossistema.
ExistemuitotrabalhointelectualdepesquisadeumbomUXDesignere
dequestionamentoconstante:essasoluç ãodeinterfaceéaquemelhormate-
rializaumaboaexperiênciaparaousuáriodesseproduto?Ouainda:dentro
i

## Página 4

CasadoCódigo
doprazoquetemos,quaisfuncionalidadesdevemserpriorizadas?
DentrodaComputaç ãoexisteumadisciplinaqueàsvezesaparecena
gradecurricularumpoucoperdidaouatémesmonegligenciada,queéaHCI
ouIHC(InteraçãoHomem-Computador).Elademonstraqueapreocupaç ão
comousuárionãoéprivilégiodomundodigital,dainternet: asprimeiras
publicaçõesdatamdadécadade70. Éinteressantetambémobservarcomo
metodologiasquepassampelaáreadodesenvolvimento,comoAgileouLean
Design,sãonaturalmentetransportadasparaomundoUX.Essessãoapenas
exemplosparacomprovaroquantooUXtemumagrandeafinidadecoma
Computação.
Creioquesejaporissoque,desdeoiníciodeminhacarreiraemdesen-
volvimentoweb,encontreinesseprofissional–quenaépocaerachamado
apenasde arquitetodeinformação–umelodeligaçãoentreodesenvolvi-
mentoqueévinculadoàtecnologiaeàconcep çãodositeatreladoàcriaç ão.
Eraoprofissionaldaáreadecriaç ãoquetinhaumpensamentomaispróximo
aomeu,pendendoparaológicoeestruturado.
Onome“arquitetodeinformação”foipessoalmenteimportanteparaque
pudesseentenderoseupapelesuarelaç ãocomomeutrabalho:ambosestá-
vamosconstruindoumacasa,umedifícioouum“sítio”.Aele,comoarquiteto,
cabiadefinirquaiscômodosterianacasaesuasdisposiçõesparaqueapessoa
quefossevisitá-lativesseasensaç ãodequeerafuncionaleagradável.Amim,
comoprogramador–ouengenheiro–,construiroalicerce,levantarasvigas,
asparedes,alajeetodoonecessárioparadarvidaaoprojeto.Tecnicamente,
épossívelumengenheiroconstruirumacasasemumarquiteto? Sim. Ela
temchancedeserextraordináriaeúnicadopontodevistaestético?Difícil.
Masissonãoquerdizerqueoengenheironãopossaentenderumpoucodo
mundodoarquiteto,atéporestaremtãoconectadospeloprodutofinal.
Tiveasortedeencontrarpelomeucaminhobonsprofissionaisqueen-
tendiamque,parafazerbemoseutrabalho,precisavamdoinputdeoutras
pessoas–inclusivedosprogramadores–emumprocessodetrabalhomais
colaborativo.
Oautordesselivroéquemmelhorpersonificaparamimacompetên-
cianessamatéria,tantoporserumestudiosoincansáveldenovasmetodolo-
giasrelacionadasàevoluç ãodadisciplinaemsi,quantopelopapelquesem-
ii

## Página 5

CasadoCódigo
preexercenosprojetosemquetrabalha:apreocupaç ãocomousuáriofinal
ecomaspessoasquetrabalhamnesseprocesso,incentivando-asafazeros
mesmosquestionamentossobreusabilidadee,consequentemente,constru-
indoummelhorprodutofinal. Oimportanteparaelenãoéapenasofim,
masoprocessoparachegarlá,quepodeserigualmenterecompensador.Ou
atémais.Compartilhamosdessacren ça.
Compartilharoconhecimentofazpartedavidadoautor,sejanoblogque
mantém(http://arquiteturadeinformacao.com),nesseprópriolivroeatéem
sualistadelugaresparavisitarnoFoursquare. Sevocêumdiaquiserdicas
doquefazeremNYC,porexemplo,procureousuáriodelenessaredesocial,
queencontraráumalistadevidamentecategorizadaporassunto.
Nocapitulointrodutório,Fabriciosabiamenteprocuraalinharasexpec-
tativasdevocê,leitor,(jáéumaamostradecomoelesepreocupoucomasua
experiênciaaolerolivro)efazumconviteparatrilharcomeleajornadado
UXDesign,quenãoacabanesselivro.Refor çoesseconvite,poisvocênãovai
searrependerdeexploraressemundoqueestáemconstanteevoluç ão.Enão
sesurpreendaseaochegaraofinaldolivrovocêsesentirtentadoainvestigar
maisoassunto:éissoquefazemosbonslivros.
SobreEdson Sueyoshi
EdsonSueyoshi,éSeniorTechnologyDirectordaR/GAdeSãoPaulo,
trabalhouemportaisdeconteúdocomoUOLeGlobo.comeagênciade
publicidadedigitalcomoAgênciaClickdesenvolvendoprojetosdigitais
comositeseaplicativosparaclientescomoCoca-Cola,FIAT,ESPN,Sa-
dia,Citibank,MasterCard,TIMeGoogle. Jáprogramouemdiversas
linguagenscomoJava,.Net,Perl,PHPeRubyenosetupdeinfraestru-
turadeservidoreswebedeaplicaç ão.Seumaiorinteresseprofissionalé
exploraratecnologianocontextodaComunicaç ãoePublicidade.
iii

## Página 7

CasadoCódigo
Sobreoautor
FabricioTeixeiratrabalhacom UserExperienceDesign háváriosanos,de-
senhandoprodutosecampanhasdigitaisparagrandesmarcascomoGoogle,
YouTube,Metlife,Fiat,ESPN,Petrobras–entreoutras.GraduadoemPublici-
dadeePropagandaepós-graduadoemMídiasInterativas,tempassagenspor
agênciasdepublicidadedigitalcomoAgênciaClick,CrispinPorter+Bogusky
eR/GA,tantonoBrasilquantonosEUA.JáfoiprofessordeUserExperi-
encenaMiamiAdSchool/ESPMeparticipoucomopalestrantedeeventosde
grandeporterelacionadosàdisciplina.Entreosprêmiosacumuladosdurante
acarreiraconstamCannesLions,OneShowInteractive,WaveFestivaleiMas-
ters. TambémcolaboraparaoUpdateorDie,umcoletivonão-jornalístico
comprofissionaisdeváriasdisciplinasqueestimulamoaprendizadoeacria-
tividadeonline,alémdemanterumdosmaioresblogssobreUserExperience
eArquiteturadeInformaç ãodoBrasil(http://arquiteturadeinformacao.com)
. AtualmenteédiretordeUserExperiencenoescritóriodaR/GAemNova
Iorque.
v

## Página 9

CasadoCódigo
Agradecimentos
ÀCasadoCódigo,peloextremocuidadoeapoiocomapublicaç ãodolivro.
Aosdesigners, criadoreseamigosCaioBraga, LilianRousseau, Peter
Pawlick,ColbyDennison,JonathanLaCour,PonKattera,MauricioMelo,
AgathaKimeElisaVolpato,pelascontribuiçõesemotivaç ãoantesedurante
oprocesso.
AoamigoEdsonSueyoshi,queescreveuoprefácio.
Àminhafamília,porsempreincentivaraescrita–entreoutrasformasde
expressão–emminhavida.
vii

## Página 11

CasadoCódigo
Doquetrataolivro
UXDesign–IntroduçãoeboaspráticasnoDesigndaExperiênciadoUsuário é
umacoletâneadeartigossobreUserExperienceDesignparaquemtrabalha
comdesignedesenvolvimentodeprodutosdigitais–sejaemportais,agên-
ciasdepublicidade,startups,consultoriasouempresasquedealgumaforma
estejamenvolvidascomcriaç ãodesoftware.
Comasinterfacesdigitaisdominandocadavezmaisosnovosaspectos
denossasrotinas,aumentatambémaprocuraporprofissionaisespecializa-
dosemDesigndaExperiênciadoUsuário(UXDesign)paragarantirque
essesprodutossejam,acimadetudo,fáceiseagradáveisdeusar.Emummer-
cadocadavezmaiscompetitivo,diferenciam-seosprodutoseempresasque
colocamousuárionocentrodoprocessodeDesign,envolvendo-osdesdeas
etapasdeestratégiaeconcep çãoatéasetapasdedesenvolvimentoetestes.
Nos últimos anos tenho procurado colaborar com a comunidade
de designers e desenvolvedores brasileiros através de meu blog (http://
arquiteturadeinformacao.com),ondecompartilhoartigos,linksereflexões
relacionados a UX Design. Ainda assim, muita gente entra em contato
comigoprocurandosabermaissobreadisciplina,mencionandoadificuldade
emencontrartextosemportuguêssobreoassunto. Umdosobjetivosdeste
livroédisseminarinformaç ãosobreUXDesignpornovoscanais,deforma
didática,simplesecentralizada.
ix

## Página 13

CasadoCódigo Sumário
Sumário
1 OqueéUserExperience 1
1.1 AsdisciplinasdeUX . . . . . . . . . . . . . . . . . . . . . . . . 3
1.2 OquefazumUXdesigner . . . . . . . . . . . . . . . . . . . . 6
1.3 QualquerumpodeserUXdesigner . . . . . . . . . . . . . . . 8
1.4 AsdiferentesfacesdoUXdesigner . . . . . . . . . . . . . . . 9
1.5 OqueUXDesignnãoé . . . . . . . . . . . . . . . . . . . . . . 12
1.6 DesenvolvedorestambémsãoUXdesigners . . . . . . . . . . 12
2 MétodoseentregáveisdeUX 17
2.1 Definiçãodaestratégia . . . . . . . . . . . . . . . . . . . . . . 18
2.2 Geraçãodeideias . . . . . . . . . . . . . . . . . . . . . . . . . 26
2.3 Planejamentodoproduto . . . . . . . . . . . . . . . . . . . . . 29
2.4 Pesquisaevalidaç ão . . . . . . . . . . . . . . . . . . . . . . . . 33
2.5 Desenhodeinterfaces . . . . . . . . . . . . . . . . . . . . . . . 36
3 Wireframes,protótiposerabiscoframes 41
3.1 Comonascemoswireframes . . . . . . . . . . . . . . . . . . . 44
3.2 Comointerpretarumwireframe . . . . . . . . . . . . . . . . . 46
3.3 Asvantagensdeusarwireframesnoprocesso . . . . . . . . . 50
3.4 Alternativasaoswireframes . . . . . . . . . . . . . . . . . . . 51
3.5 Asvantagensdosprotótipos . . . . . . . . . . . . . . . . . . . 56
3.6 Comodecidirentreprotótiposewireframes . . . . . . . . . . 59
3.7 Comunicandoideiascomrabiscoframes . . . . . . . . . . . . 63
3.8 Boaspráticaspararabiscar . . . . . . . . . . . . . . . . . . . . 65
xi

## Página 14

Sumário CasadoCódigo
4 Aboaevelhausabilidade 69
4.1 Simplicidadenãoésimples . . . . . . . . . . . . . . . . . . . . 70
4.2 Ofere çainformaçõesempequenasdoses . . . . . . . . . . . . 72
4.3 Criehierarquianapágina . . . . . . . . . . . . . . . . . . . . . 75
4.4 Digaaousuáriooquefazeraseguir . . . . . . . . . . . . . . . 80
4.5 Dêfeedbacksobreoestadodosistema . . . . . . . . . . . . . 83
4.6 Eviteerrosantesqueaconte çam . . . . . . . . . . . . . . . . . 84
4.7 Simplifiqueformulários. . . . . . . . . . . . . . . . . . . . . . 88
5 Abelezadospequenosdetalhes 93
5.1 Eviteelementosemexcesso . . . . . . . . . . . . . . . . . . . . 97
5.2 Reveleinformaçõesprogressivamente . . . . . . . . . . . . . 98
5.3 Sejacuidadosocomotempodousuário . . . . . . . . . . . . 99
5.4 Crieexperiênciaspersonalizadas . . . . . . . . . . . . . . . . 101
5.5 Adivinheainten çãodousuário . . . . . . . . . . . . . . . . . 102
5.6 Façaotrabalhopesado . . . . . . . . . . . . . . . . . . . . . . 105
5.7 Sejahonestocomseuspedidos . . . . . . . . . . . . . . . . . . 106
5.8 Expresseapersonalidadedasuamarca . . . . . . . . . . . . . 107
6 Aimportânciadosmicrotextos 111
6.1 Ovalorfuncionaldosmicrotextos . . . . . . . . . . . . . . . . 113
6.2 Ovaloremocionaldosmicrotextos . . . . . . . . . . . . . . . 116
6.3 Comuniquebenefícios,nãofuncionalidades . . . . . . . . . . 117
6.4 Falealinguagemdosseususuários . . . . . . . . . . . . . . . 118
6.5 Mantenhaostextoscurtos . . . . . . . . . . . . . . . . . . . . 119
7 Construindoumabibliotecadepadrões 121
7.1 Asvantagensemterumabiblioteca . . . . . . . . . . . . . . . 124
7.2 Abibliotecacomoentregávelfinaldoprojeto . . . . . . . . . 126
7.3 Maispadronizaç ãonãosignificamenoscriatividade . . . . . 128
xii

## Página 15

CasadoCódigo Sumário
8 Testandocomusuários 131
8.1 Saiadasuamesacommaisfrequência . . . . . . . . . . . . . 133
8.2 Testesdeusabilidade . . . . . . . . . . . . . . . . . . . . . . . 135
8.3 Desculpascomunsparanãotestarcomusuários . . . . . . . 138
8.4 Incorporandopesquisacomusuáriosemseuprojeto . . . . . 140
8.5 Osnúmerosnãomentem . . . . . . . . . . . . . . . . . . . . . 144
8.6 TestesA/B . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145
9 Ospecadosdeusabilidade 147
9.1 Comoprevenirerrosdeusabilidade . . . . . . . . . . . . . . . 150
9.2 Op çõesdemais,op çõesdemenos . . . . . . . . . . . . . . . . 152
9.3 Osgatilhosinvisíveis . . . . . . . . . . . . . . . . . . . . . . . 153
10 Negligenciandoaperformancedaspáginas 157
10.1 Oimpactodaperformancedaspáginas . . . . . . . . . . . . . 158
10.2 Umabatalhademuitasfrentes . . . . . . . . . . . . . . . . . . 159
10.3 Otimizandoaperformance . . . . . . . . . . . . . . . . . . . . 161
11 Produtosqueninguémusa 165
11.1 Começandopelousuário . . . . . . . . . . . . . . . . . . . . . 166
11.2 Escolhendoumatecnologia . . . . . . . . . . . . . . . . . . . 167
11.3 Definindoaproposiçãodevalordoproduto . . . . . . . . . . 170
12 Priorizandofuncionalidades 175
12.1 Oeternoproblemadoescopoedoprazo . . . . . . . . . . . . 175
12.2 Aestratégiadoscupcakes . . . . . . . . . . . . . . . . . . . . . 177
12.3 Priorizandoasfeaturesdeumproduto . . . . . . . . . . . . . 179
12.4 Umprodutonuncaestápronto . . . . . . . . . . . . . . . . . 182
13 ChecklistdeUX 185
13.1 Simples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186
13.2 Acionável. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187
13.3 Inteligente. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187
13.4 Agradável. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 188
13.5 Relevante. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189
xiii

## Página 16

Sumário CasadoCódigo
14 UXnomundodosnegócios 191
14.1 Design=Dinheiro . . . . . . . . . . . . . . . . . . . . . . . . . 192
14.2 ConvencendootimeainvestiremUX . . . . . . . . . . . . . 192
15 ComocomeçaremUXDesign 195
15.1 OmercadodeUXnoBrasil . . . . . . . . . . . . . . . . . . . 196
15.2 Ondetrabalhar. . . . . . . . . . . . . . . . . . . . . . . . . . . 197
15.3 Comoconseguirumempregonaárea . . . . . . . . . . . . . . 197
15.4 ComoseconectarcomprofissionaisdeUX . . . . . . . . . . 199
15.5 Comosemanteratualizado . . . . . . . . . . . . . . . . . . . . 200
15.6 Comoaprenderausarasferramentas . . . . . . . . . . . . . . 203
15.7 MasporquetrabalharcomUX . . . . . . . . . . . . . . . . . 203
16 Ofuturodaexperiênciadousuário 207
17 Bibliografia 209
xiv

## Página 17

Capítulo1
OqueéUserExperience
ApesardoestrangeirismoquedeuorigemàsiglaUX(UsereXperience),o
termoébemmaissimplesdoqueparece.Experiênciadousuário.Experiência
dequemusa.
Nodecorrerdodianostornamos“usuários”deumaporçãodecoisas.
Oalarmedocelularquenosacordademanhã,acadeira,ocarro,ocont-
roleremotodoarcondicionado,oFacebook,ostalheres,ocaixaeletrônico,o
computadornotrabalho,ocopodecerveja–objetoseprodutos,digitaisou
não,quesão“usados”porpessoasequesãoprojetadosparacumpriralguma
função.Oalarmeparanosacordar,ocaixaeletrônicoparafazertransações
financeiras,acadeiraparadescansar.
Quandovocêusaalgumdessesobjetos,vocêtemumaexperiência. Se
vocêjápassounervosonafrentedocaixaeletrônicoporqueelenãoentregou
odinheiroquevocêestavaesperandoenãodeunenhumaexplicaç ãosensata

## Página 18

CasadoCódigo
sobreomotivodarecusa,vocêpossivelmenteteveumapéssimaexperiência
enquantousuáriodocaixaeletrônico.
Experiênciadousuárioexistedesdequeomundoémundo.Oumelhor,
desdequeaspessoascome çarama“usar”objetospararealizaralgumatarefa.
Depois,vieramprodutosdigitais.Websites,aplicativosdecelular,caixas
eletrônicos, quiosques interativos, tablets, TVs digitais, videogames. O
princípiocontinuouomesmo:aexperiênciadeusarumsite,porexemplo,
podeserpositivaounegativa,dependendodoseufluxodentrodele. Nor-
malmente,aexperiênciaépositivaquandovocêconseguerealizaratarefa
semdemora,frustraç ãoousemencontrarproblemasnomeiodocaminho.
Essatarefapodesertantofuncional(entrarnoseuinternetbankingparapa-
garumboletobancário)ouemocional(entrarnositedeumaredesocialpara
saberoqueseusamigosandamfazendo).
Experiênciassão,obviamente,subjetivas. Cadapessoatemumaexper-
iênciadiferenteaousarumcaixaeletrônico,porexemplo.Essaexperiênciaé
influenciadaporfatoreshumanos(suahabilidadeemusarcaixaseletrônicos,
suavisão,suahabilidademotora,suacapacidadedelereentenderoqueestá
escritonatela,seuhumornaquelemomentoetc.) eporfatoresexternos(o
horáriododia,oambienteondeocaixaeletrônicoestáinstalado,ofatodeter
umafiladepessoasatrásdevocê).Mas,apesardesubjetivas,essasexperiên-
ciassãoprojetadasporalguém.Alguémpensouedesenhouainterfacedigital
docaixaeletrônicoparaqueosclientesdobancopudessemfazertransações
semprecisardainterfacehumana.Éatal“interaç ãohomem-máquina”(HCI
—Human-ComputerInteraction),umcampodeestudograndiosíssimoque
mobilizaprofissionaisdeváriosperfisaoredordomundo.
“AmaioriadaspessoasacreditaqueUserExperienceésomenteencontrara
melhorsolu çãoparaosseususuários–masnãoé.UXsetratasobredefiniro
problemaqueprecisaserresolvido(oporquê),definirparaquemesse
problemaprecisaserresolvido(oquem),edefinirocaminhoquedeveser
percorridopararesolvê-lo(ocomo).”
–WhitneyHess
2

## Página 19

CasadoCódigo Capítulo1. OqueéUserExperience
1.1 As disciplinas deUX
Figura1.1:DiagramadasdisciplinasquecompõemUserExperience
DanSaffer,designerdeinteraç ãoeautordolivroDesigningforInteraction
(http://www.designingforinteraction.com), construiuumdiagramaháal-
gunsanosquedefinebemasintersecçõesenomenclaturasdadisciplina.
ReparecomoograndecírculodeUserExperienceDesignenglobauma
3

## Página 20

1.1. AsdisciplinasdeUX CasadoCódigo
sériedeoutrasdisciplinas:deArquiteturadeInformaç ãoaDesignIndustrial,
passandoatéporSoundDesign.Sim,aquelesonzinhoquetocaquandovocê
iniciaseuPCouMactambémfazpartedaexperiênciadousuário.E,como
todoelementodaexperiênciadousuário,tambémfoiprojetadoporalguém.
UmaoutraformainteressantedeilustraroqueéUserExperienceDesign
vemdeStephenAnderson,autordolivroSeductiveInteractionDesign(http:
//www.goodreads.com/book/show/9967766-seductive-interaction-design).
UXdesignerstrabalhamparaconstruirprodutosquesejamfáceisdeusar
(atal usabilidade),reduzindoafric çãoepermitindoqueosusuárioscom-
pletematarefadesejadaemmenostempo,commenosruídoeobstáculos.Ao
mesmotempo,apoiam-seemprincípiosda psicologiaparamotivarousuário
eincentivá-loaseguiradiante.
Vocêjádevetertidoaexperiênciadeficarhorasjogandoummesmojogo,
sejanovideogame,nocelularounocomputador.Osjogossãoexperiências
queconseguemequilibrarmuitobemessesdoisaspectos.
4

## Página 21

CasadoCódigo Capítulo1. OqueéUserExperience
Normalmente,lk./asprimeirasfasesdeumjogosãopropositalmentesim-
plificadasparafazerousuárioseengajarcomele:amecânicaeoscontrolesdo
jogosãoexplicados(usabilidade)eváriastécnicasmotivacionaissãousadas
parafazercomqueojogadorsesintaconfianteemsuasprópriashabilidades
(psicologia).
Figura1.2:“Parabéns,vocêcolheuseuprimeirotomate!
Amesmaregraseaplicaparaosprojetosnosquaisvocêtrabalha,se-
jamelesjogos,websites,aplicativosparacelular,serviçosdigitais,sitesdee-
commerceetc. Comofazeroseuusuáriocompletarastarefassemdificul-
dades?Comocriarumainterfacequesejarealmentesimplesdeusar?Como
manterousuáriomotivadoparaseguiradiante,parapassarmaistempous-
andooseuproduto,paradivulgaroseuprodutoparaosamigosouparavoltar
maisvezesaele?
5

## Página 22

1.2. OquefazumUXdesigner CasadoCódigo
1.2 O que faz um UX designer
Sevocêtrabalhaemagênciadepublicidade,portal,startup,consultoriaou
produtoradigital,ouqualquerempresaqueestejadealgumaformaenvolvida
emdesenvolvimentodesoftware,vocêjádeveteresbarradocomumUXde-
signeremalgumlugar. Sejaemummanualdeboaspráticasparaconstruir
sites,sejaemumaconferênciainternacionaldospublicitáriosquevoamde
primeiraclasseousejaaquelefulanode jobdescriptionnebulosoqueestásen-
tadonamesmasaladereuniãoquevocê.
Masapesardeonomedaprofissãoconterapalavra“designer”, esses
profissionaisnãonecessariamenteusamoPhotoshopparacriaraaparência
finaldoprodutoqueserávistopelaspessoas.Comoprojetistasdaexperiência
dousuário,omaisimportanteparaosUXdesignersédefinircomoaspessoas
irãointeragircomoproduto,quaistarefasconseguirãorealizardentrodele,
qualaordemnaqualastelasserãoapresentadas–eporaívai.Normalmente,
existeumaetapaseguinteaotrabalhodoUXdesignerondeumdiretorde
artefazcomqueainterfacetomeformanoPhotoshopefiquemuitomais
agradávelebemacabada.
UXdesignerscome çaramasurgirnessesambientescomo“arquitetosde
informação”,sendoessencialmenteresponsáveispororganizaroconteúdode
umsitedentrodomenuedesenharcaixinhascinzasquerepresentamcomo
umainterfaceiráfuncionar(ostais“wireframes”).
Masàmedidaqueoecossistemadigitaldasmarcassetornoucomplexo
demaisparacaberemmenus,essesmesmossujeitosacabaramassumindoum
papelumpoucomaisestratégiconoprocessocriativo.Hoje,algumasempre-
sasjácolocamoUXdesignerfazendoomeiodecampoentreopensamento
estratégico(planejarumproduto)eopensamentoprático(desenharumpro-
duto),ajudandoadefinircomoasideias,especialmenteasdigitais,irãotomar
forma.
Nodiaadia,oUXdesignertrabalhadesenhandoaestruturadessespro-
dutosdigitais.Elenãochegaadefiniraidentidadevisualdoproduto–nor-
malmente,issoficaacargodeumprofissionalespecializadoemDire çãode
Arte. Emvezdedefinirseobotãoseráazulouvermelho,retangularou
arredondado,opapeldoUXdesignerédefinirquestõesmaisestratégicasso-
bretalbotão:
6

## Página 23

CasadoCódigo Capítulo1. OqueéUserExperience
• Porqueobotãoexiste?
• Qual a importância dele naquele contexto ou página em que ele
aparece?
• Eleéaaçãoprimáriaousecundáriaqueousuáriopodetomarnaquele
momento?
• Paraondeousuárioserálevadoquandoclicarnobotão?
• Oqueotextodobotãodevedizerparaousuário?
• Obotãoestásempreativo,ouelesóéativadodepoisqueousuário
preencherdeterminadocampoemumformulário?
• Todososusuários,logadosounãonosite,veemomesmobotão?
• Otamanhodobotãoestáadequadoparaserclicadotantocomopon-
teirodomouseemumcomputadordesktopquantoporumdedohu-
manoemumainterfacetouch(celular,tablet)?
•Adinfinitum.
Alistaégrande. Reparequealgumasdessasdecisõesnãosãotomadas
exclusivamentepeloUXdesigner:algumasdelassãofeitasemconjuntocom
odiretordearte,comodesenvolvedor,comogerentedeprojetoseoutros
profissionaisquetambémestãoenvolvidosnacriaç ãodoproduto.
Costumo dizer que o profissional de UX é um ca-
maleão dentro do time (http://www.uxbooth.com/articles/
the-ux-chameleon-and-its-multidisciplinary-skin) : precisa saber se
adaptaradiferentescontextos,conhecerovocabuláriodediferentesprofis-
sionais (saber falar “a língua” do programador front-end, mas também
conhecerosjargõesdosdesigners)eentenderumpoucodecadadisciplina.
Mas,acimadetudo,osUXdesignersprecisamconhecersobrepessoas.
Ospróximoscapítulosdestelivrofalamumpoucomaissobreisso.
7

## Página 24

1.3. QualquerumpodeserUXdesigner CasadoCódigo
1.3 Qualquer um pode ser UX designer
HojeemdiaexistemuitomisticismoemtornodafiguradoUXdesigner,de
qualoseupapeldentrodeumtimeedequaisosrequisitosparaquealguém
coloqueasigla“UX”nonomedocargonoLinkedin. Naprática,bastater
bomsenso,organizaç ão,pensamentosistemáticoedisposiç ãodeentender
doqueaspessoasprecisam.
“EujátiveumpoucodeproblemaementenderoqueumUXdesignerfazde
verdade,eeucontinuochegandosempreàmesmaconclusão:umuser
experiencedesignernãofaznadadeespecial.Eleésóumdesigner.Todosos
produtostêmumaexperiênciadousuário(UX).Eessaexperiêncianãoé
explicitamentedesenhada;éumsubprodutodedesenharumainterface.”
–DanielEden
Fonte:http://daneden.me/2013/03/20/ux-is-not-a-standalone-job
Acitaçãovaidiretoaoponto:todososprofissionaisquecontribuemde
algumaformaparaaconstruç ãodeumainterfacequeseráusadaporpessoas
são,portabela,designersdaexperiênciadousuário(ouUXdesigners).
Aconven çãodeterumprofissional100%dedicadoa“puxarasardinha”
paraoladodousuárioéapenasoremédioparaumproblemaanterior:um
modelodetrabalhoquemuitasvezesnegligenciaaimportânciadesedesen-
harprodutosquesejamfocadosemnecessidadesreaisdepessoasreais.Não
adiantaumainterfacelinda,comcoresmarcantesebomgostovisual,seela
nãoestáresolvendoaquiloqueaspessoasqueremresolveraousá-la. Seo
gerentedeprojetosestápreocupadocomverbaeprazo,odesenvolvedorestá
preocupadocomaslimitaçõestécnicasdedeterminadalinguagemeocliente
estápreocupadocomosobjetivosdenegóciosdamarca,oUXdesigneréo
profissionalqueentranaequaç ãoparaassumiropapeldeadvogarpelosin-
teressesdousuário.
UmaprovadequeosrequisitosparaserumUXdesignersãomaissim-
plesdoquepareceméofatodequeváriosprofissionaisdaáreavêmdefor-
maçõesdiferentes:jornalistas,publicitários,designersgráficos,engenheiros,
bibliotecônomos.Tambémsãocomunsprofissionaisque,antesdeseremUX
designers, trabalhavamcomoprogramadoresfront-end, redatoresouger-
8

## Página 25

CasadoCódigo Capítulo1. OqueéUserExperience
entesdeprojetos. Algumasvezessãopessoasquedesempenhamumpapel
híbridoentreduasoumaisdessasdisciplinas.
1.4 As diferentes faces doUX designer
Porserumaáreabastanteampla,algunsUXdesignersacabamassumindo
funçõesmaisespecíficasàmedidaqueavan çamemsuacarreira.Éumpro-
cessonatural,jáqueperfisdiferentesdepessoaspodemtermaisfacilidade
comumaáreaououtradentrodoDesign.
Sevocêtemfacilidadeemorganizarconteúdo,épossívelqueprefirafocar
seusesfor çosemArquiteturadeinformaç ãooutaxonomia.Setemfacilidade
emlidarcompessoas,talvezprefirainvestiremPesquisacomusuários.
Masseessestermosaindanãosãofamiliaresparavocê,vejaaseguiruma
breveexplicaçãodealgumasdasprincipaissubáreasdeUX:
Arquiteturadeinformação:adisciplinatemsuasraízesnabibliotecono-
mia(organizarecatalogarostítulosdentrodeumabibliotecaparaquese-
jamfacilmenteencontradaspelovisitante)eédecertaformasimilarnoam-
bientedigital. Comofazercomqueasinformaçõessejamorganizadasno
menudeumsite,porexemplo,deformaquesejamacessadasfacilmentepe-
losusuários?Qualperfildeusuárioestábuscandoqualtipodeinformaç ão?
Comoositensestãoordenados,agrupadoseorganizadosdentrodaestrutura
dosite?
9

## Página 26

1.4. AsdiferentesfacesdoUXdesigner CasadoCódigo
Usabilidade: garantirqueasinterfacessejamfáceisdeusar. Ousuário
conseguerealizarumatarefasemtranstornooudemora? Emumnúmero
razoáveldepassos?Asinformaçõessãofáceisdeentender?Oresidualapósa
experiênciaépositivo,ouousuáriosaiucognitivamenteexaustodali?
Designdeinteração:entenderedefinirocomportamentodasinterfaces
quandoousuáriointeragecomelas.Oqueacontecequandoeuclicoemde-
terminadobotão?Comoainterfaceresponde?Comoeuarrastoumproduto
parameucarrinhodecompras?Qualaexataquantidadedeinformaç ãoque
ousuárioprecisasaberpararealizaratarefanaquelemomento?Comoain-
terfacepodeserusadaparacriarumanarrativanaexperiênciadousuário?
Taxonomia:organizarerotularainformaç ãodeformaquefaç asentido
paraousuário.Acategoriadalojavirtualirásechamar“Refrigeradores”ou
10

## Página 27

CasadoCódigo Capítulo1. OqueéUserExperience
“Geladeiras"?Eseousuáriobuscarpor“Freezer”,oqueacontece?Operfilde-
mográficodousuáriodaquelesite/appestáhabituadocomaquelalinguagem?
Comoclassificaraseditoriasdeumportaldenotícias?Quasetudoqueexiste
nomundopodeserclassificadodeacordocomalgumesquemataxonômico
—deespéciesdeplantasapaísesecontinentes.
Estratégiadedesign:éoentendimentoedefiniç ãodosporquêsdopro-
duto. Paraquemelefoicriado? Comooprodutoevoluicomopassardo
tempo?Quaisosseusobjetivosdenegócioecomoelesserãoalcan çadosem
cadaetapadesuaevoluç ão?Comomedirsucessoumavezqueoprodutoé
lançado?Qualoretornoesperado?Quaisferramentasdedesignpodemser
usadasparaatingiremensuraressesucesso?
Pesquisacomusuários:éoentendimentodopúblico-alvodoproduto.O
quefazumapessoairatéosite?Quaisasnecessidades,anseiosemotivações
queessapessoatemaousaroproduto? Quaisasprincipaistarefasqueela
querrealizar?Quaisasparticularidadesdocomportamentodessegrupode
usuáriosqueinfluenciamasdecisõesdedesignàmedidaqueoprodutoé
11

## Página 28

1.5. OqueUXDesignnãoé CasadoCódigo
construídoouevolui?
1.5 OqueUXD esign não é
Paracome çodeconversa: UXDesignnãoédire çãodearte. Tambémnão
éplanejamento,nãoégerênciadeprojetos,nãoédesenvolvimentodesoft-
ware.UXfazomeiodecampoentretodasessasdisciplinas,garantindoque
todaselasestejamcaminhandojuntasemdire çãoaummesmoobjetivo.Éo
UXdesigner,porexemplo,quetraduzaestratégiacriadapeloplanejadorem
formadetelasefluxosqueserãoutilizadospelousuário.
UXtambémnãoé,definitivamente,umadisciplinaexata.Muitasvezes,
aspessoasprocuramseaproximardeUXDesignparaconseguiremtomar
decisõessobre“qualtipodemenuusarnomeusite”ou“comomelhorara
usabilidadeparaaumentarasconversõesdomeuformuláriodecadastro”.
Ofatoéqueasrespostasparaessasperguntasdependemdeumaquanti-
dadetãograndedefatoresqueéimpossívelafirmarcomprecisãoqueocam-
inhocertoéoAouoB.MastambéméessagrandepartedabelezadoDe-
sign:ofatodequetudodependedecomoaspessoassecomportarão,algo
bastantedifícildeprever. OUXdesignernãoéumprofetaquesabecomo
aspessoaspensam;eleéumpesquisadorqueinvestigaoquelevouumade-
terminadapessoaaagirdedeterminadaformaeentãopropõemelhoriasde
designbaseadasnesses insights.
UXDesigntambémnãoéumadisciplinadeumsoftwareoulinguagem
só. PodematéexistirUXdesignersespecializadosemdesenharsitesem
HTML,ouaplicativosemC++; masporsercentradanocomportamento
humano,ateoriaqueestruturaotrabalhodesseprofissionaléagnósticade
código,plataformaoutamanhodetela.
1.6 Desenvolvedores também são UX designers
Antigamenteexistiaumcertoatritoentredesigners(nãosóUX)edesenvolve-
doresnodecorrerdoandamentodosprojetos.Emalgunslugaresissoaindaé
comum.Designersbrigandopelaperfeiç ãodospixels,queporfaltadecom-
petênciadodesenvolvedornãotinhamficadoiguaisaoPhotoshopnahora
12

## Página 29

CasadoCódigo Capítulo1. OqueéUserExperience
detransformarainterfaceemHTML.Dooutrolado,desenvolvedoresrecla-
mandodo“excessodecriatividade”dosdesignersnahoradebolarlayouts
quepudessemserreplicadosnalinguagemdoprodutofinal.
Figura1.3:Comodesigners,desenvolvedoresegerentesdeprojetosseveem
Masostemposmudaram. Alinguagemvisualdasinterfacesdigitais
amadureceumuitonosúltimosanos,foificandomaissóbria,flat,commenos
elementosdecorativosemaisfocoempermitirqueousuáriorealizetarefas
comfacilidade.Oadventododesignresponsivoeanecessidadedecriarlay-
outsfluidosqueseadaptemamúltiplasresoluçõesdetelatambémfizeram
comqueasequipesaospoucossedesapegassemdoexcessodegrafismoseda
precisãodospixels,quepassouaseralcan çávelapenasdentrodofantástico
mundodoPhotoshop.
Dooutrolado,desenvolvedorespassaramasepreocuparmaiscomaex-
periênciadousuárioeaaceitarsugestõesdosdesignersquefocassememmel-
13

## Página 30

1.6. DesenvolvedorestambémsãoUXdesigners CasadoCódigo
horarausabilidadedoproduto.Afinal,odesenvolvedorcompreendeuqueo
designernãoestavalásóparadificultarsuavida.
Essaaproximaçãoesimbioseentreasáreaséummovimentoextrema-
mentesaudável,equemsaiganhandoéousuáriofinal.
Hoje,bonsdesignersjáperceberamquesãoosdesenvolvedoresquefazem
deleumbomdesigner,jáquesãoelesosresponsáveisporfazersuasideias
tomaremforma.Designerssemdesenvolvedoressófazemlayoutsestáticos,
queficambonitosnoportfóliomasquenãochegamaimpactarpositiva-
mentearotinadopúblicofinal. Poroutrolado,desenvolvedoressemde-
signerscriamsistemasrobustosepoderosos,masqueàsvezespecamemser
agradáveisefáceisdeusar.
VejanoboxodepoimentodeBradFrost(http://bradfrostweb.com),um
programadorfront-endqueficouconhecidoporestudarecontribuircomo
conhecimentodacomunidadededesenvolvedoressobredesignresponsivo.
14

## Página 31

CasadoCódigo Capítulo1. OqueéUserExperience
Depoimento deBradFrost
“Mesmoquandomeucargoeranomeado‘webdeveloper’ou‘open
standards developer’, eu costumava me nomear ‘front-end designer’.
Agoraeusimplesmentemenomeio‘webdesigner’.Desenvolvimentode
HTMLeCSSédesign.Osprojetosmaisfrustrantesdequeparticipeisão
aquelesondeaspessoasnãoentendemporquedesenvolvimentofront-
endprecisavaserenvolvidocedonoprocessodedesign.Osprojetosmais
recompensadores,poroutrolado,foramaquelesqueenvolveramdesen-
volvedoresfront-enddesdeocome ço.
Euespecificamenteevitochamarmeucargodedesenvolvedorporque
aspessoasacabamassumindoqueeupossoprogramaremRubyounor-
malizaralgunsbancosdedados.EununcativenenhumaauladeCiência
daComputação. (...) Quasetodotrabalhodeprogramaç ãoqueeufiz
eraparamanipularelementosemumatela.Apesardeaospoucoscon-
tinuaraprendendocoisassobreprogramaç ão,eunãoousariamechamar
deprogramador.
HTMLnãoéprogramaç ão. CSSnãoéprogramaç ão. Mas,porque
elesaindaassimsãocódigos,desenvolvedoresfront-endmuitasvezessão
colocadosnamesmagavetadosprogramadoresPython,Java,PHP,Ruby,
C#,C++,ObjectiveCetc.,emvezdeseremcolocadosjuntosdotimede
design.Issoéumgrandeproblema.
ÀmedidaqueaWebcontinuasetornandoincrivelmentecomplexa,
ébastanteimportanteatentaràsinúmerasformaspelasquaisumaex-
periêncianawebpodeserdesenhada.Éimpossívelparadesignerstra-
balhandoemambientesestáticosconseguiremarticularrealisticamente
cadadispositivo,configuraç ãodeusuárioevariávelqueafetacomoo
designématerializado.Poressemotivo,desenvolvedoresfront-endpre-
cisamtrabalharmuitopróximosadesignersparagarantirqueoqueestá
sendodesenhadoérealistaefactível. Issoinclui,entreoutrascoisas,
garantirqueasentregasdefront-endfaç ampartedasentregasdedesign.”
BonsUXdesignersjásederamcontadaimportânciadetrazerodesen-
15

## Página 32

1.6. DesenvolvedorestambémsãoUXdesigners CasadoCódigo
volvedorparaasdiscussõescriativasoquantoantesnatimelinedeumpro-
jeto.Alémdegarantirmaisclarezasobreaquiloqueestásendocriado,essa
aproximaçãoentreasáreastambémpermitequeoprocessosejamaiságil,já
queotimeconseguepartirparaaetapadeprototipaç ãodaideiamesmoantes
deolayoutestarprontonoPhotoshop.“Testearlier,failfaster ”,dizemporaí.
Equantoantesvocêtestaseumasoluç ãofuncionaounão,antesvocêpode
começaramelhorá-la.
Otrabalhofeitopelosdesenvolvedorestemimpactodiretonaexperiência
dousuário,paraobemeparaomal.Nodecorrerdolivro,vocêveráalguns
exemplosdeboasemáspráticasdeinterfaceemaissituaçõesemqueaparce-
riaentredesignersedesenvolvedorespoderenderbonsfrutos.
16

## Página 33

Capítulo2
MétodoseentregáveisdeUX
QuasenadadaquiloqueédesenhadoouprojetadopeloUXdesigneracaba
sendo“visto”peloconsumidorfinal.Todososentregáveiseprocessosutiliza-
dosemUserExperiencetêmcomoobjetivofacilitaracomunicaç ãoentreos
membrosdotime,documentardecisõesqueforamtomadasemreuniõese
brainstorms,colherinsightssobreaquiloqueosusuáriosfinaisprecisame/ou
garantirquetodosestejamalinhadosarespeitodoqueestásendocriado.
OsentregáveisproduzidosporprofissionaisdeUXvariambastantede
acordocomotipodeprojeto,asexpectativasdocliente,osobjetivosdedesign
eosmembrosdotimeenvolvidosnahoradepensarnosdetalhesdoproduto.
Porsetratardeumaáreamultidisciplinar,osmétodoseentregáveisutilizados
eproduzidosnodiaadiadeumUXdesignersãofortementeinfluenciados
pelosprocessosemétodosdeoutrasáreasrelacionadas.
Definiraestratégiadedesign,gerarideiasatravésdebrainstorms,plane-
jarasfuncionalidadeseaevoluç ãodeumproduto,testá-locomusuáriose

## Página 34

2.1. Definiçãodaestratégia CasadoCódigo
capturarinsightsatravésdepesquisa–essessãoalgunsexemplosdeméto-
dosqueajudamnãoapenasoUXdesigner,mastodososmembrosdotime,
adesenharprodutosquesejamrealmenterelevantesparaaspessoas.
Nemtodososmétodoslistadosaquisãoutilizadosemtodososprojetos.
SevocênãotrabalhadiretamentecomUX,acabaconhecendoapenasdoisou
trêsmétodosmaiscomuns,quesematerializamementregáveiscomo Wire-
frames,SitemapsePersonas.Conheceressesmétodosesaberqualahoracerta
deusarcadaumdeleséumadashabilidadesmaisprocuradasemprofission-
aisdeUXnomercado.
Aideiaaquinãoéfazerumaanáliseaprofundadasobrecadaumdos
métodos.Nofinaldocapítuloháumlinkcasovocêtenhainteresseemsaber
maissobreeles.
2.1 Definição da estratégia
Nessegrupoentramosmétodosutilizadosnomomentoinicialdoprojeto,
quandoaestratégiaestásendodefinidaeotimeestápreocupadoemdire-
cionaroprodutoparaumladoouparaooutro.Aocontráriodosprocessos
maisfamosos,comowireframesesitemaps,apreocupaç ãoaquinãoédoc-
umentarcomoainterfacefunciona,esimembasardecisõesmaisabstratas
sobrea“razãodeser”doproduto.
Blueprint
Ummapaquemostratodosospontosdecontatoentreconsumidore
marca,bemcomoosprocessosinternosnecessáriosparaqueessainteraç ão
aconteça. Éútilparavisualizarocaminhoqueosconsumidorespercorrem
emmúltiploscanais(site,serviçodeatendimentoaoconsumidor,lojafísica
etc.)eparaidentificaroportunidadesdemelhoria.
18

## Página 35

CasadoCódigo Capítulo2. MétodoseentregáveisdeUX
Figura2.1:Blueprint—Fonte:http://www.servicedesigntools.org/tools/35
ConsumerJourneyMap
Umdiagramaqueexploraosmúltiplos(ealgumasvezesinvisíveis)passos
tomadospeloconsumidoràmedidaqueelesseengajamcomoserviço.Per-
mitequeosdesignersdefinamasmotivaçõesenecessidadesdoconsumidor
nasváriasetapasdajornada,criandosoluçõesdedesignquesejamapropri-
adasparacadaumadelas.
19

## Página 36

2.1. Definiçãodaestratégia CasadoCódigo
Figura2.2: ConsumerJourneyMap—Fonte: http://blog.uxpin.com/2202/
designing-an-online-store-its-all-about-the-side-doors/
UserStories
Umdetalhamentodecadatarefaqueousuáriodesejacumpriraointera-
gircomoproduto.Bompararelembrarotimedasmotivaçõesquelevamo
público-alvoausarcadaumadasfuncionalidadesdoproduto,assimcomoo
caminhoqueosusuáriospercorrerãoparafazê-lo.
20

## Página 37

CasadoCódigo Capítulo2. MétodoseentregáveisdeUX
Figura2.3:UserStories—Fonte: https://medium.com/the-job-to-be-done/
Personas
Umretratodopúblico-alvoquedestacadadosdemográficos,comporta-
mentos,necessidadesemotivaçõesatravésdacriaç ãodeumpersonagemfic-
cionalbaseadoeminsightsextraídosdepesquisa. Personasfazemcomque
osdesignersedesenvolvedorescriemempatiacomosconsumidoresdurante
oprocessodedesign.
21

## Página 38

2.1. Definiçãodaestratégia CasadoCódigo
Figura 2.4: Personas — Fonte: http://uxmag.com/articles/
personas-the-foundation-of-a-great-user-experience
22

## Página 39

CasadoCódigo Capítulo2. MétodoseentregáveisdeUX
Ecossistema
Uma visualização em mapa das propriedades digitais da marca, das
conexõesentreelasedesuafun çãonaestratégiademarketing. Oecossis-
temadáinsightsvaliosossobrecomoaproveitaraspropriedadesqueamarca
possui(easnovasqueestãosendocriadas)paraatingirosobjetivosdenegó-
cios.
Figura2.5:Ecossistema—Fonte:http://hfiuxcentral.ning.com/forum/topics/
new-white-paper-kindle-fire-solid-proof-that-usability-is-no
Análisecompetitiva
Umaanáliseextensadosprodutosconcorrentesquemapeiaasfuncional-
idadesexistentesemcadaumdelesdeformacomparativa.Ajudaaentender
ospadrõesqueestãosendocriadosnaindústriaeaidentificaroportunidades
deinovaremdeterminadomercado.
23

## Página 40

2.1. Definiçãodaestratégia CasadoCódigo
Figura 2.6: Análise competitiva — Fonte:http://www.onebigfield.co.uk/
clients/tyneside-cinema-ux-re-design-of-digital-offering/
Proposiçãodevalor
Ummétodoredutivonosestágiosiniciaisdadefiniç ãodoprodutoque
mapeiaseusaspectosprincipais:oqueoprodutoé,paraquemelefoicriado
ecomo/quandoeleseráusado. Ajudaotimeaafunilarasop çõeseacriar
consensosobreoprodutoqueelesestãoprestesadesenhar.
24

## Página 41

CasadoCódigo Capítulo2. MétodoseentregáveisdeUX
Figura 2.7: Proposição de valor — Fonte:http://www.goldsbrough.biz/
value-proposition/
EntrevistascomStakeholders
Roteirosdeentrevistacomosprincipais stakeholders(aspartesenvolvi-
das)deumprojeto,tantointernosquantoexternosàempresa,paracoletar
insightssobreosseusobjetivos. Ajudamapriorizarasfuncionalidadesea
definirasmétricasdesucessodoprojeto.
KeyPerformanceIndicators(KPIs)
Critériospreestabelecidosqueajudamamedirosucessodoprodutoem
relaçãoàestratégia,paragarantirqueoprodutoatinjaoresultadoesperado.
KPIsajudamnasdecisõesdedesignquesãotomadasnomeiodocaminhoe
tambémamedirresultadosdotrabalhodeUXDesign.
25

## Página 42

2.2. Geraçãodeideias CasadoCódigo
2.2 Geração de ideias
Essegrupodemétodoséutilizadoduranteaetapacriativadoprojeto. Eles
ajudamacoletarasideiasdetodososmembrosdotimeeagarantirqueeles
estejamalinhadosemrelaç ãoaoqueoprodutoestácome çandoasetornar.
Brainstorming
Oprocessocoletivodegeraç ãodeideias,semrestrições,querespondem
adeterminadobriefcriativo.Ajudaotimeavisualizarumagrandevariedade
desoluçõesdedesignantesdeefetivamentedecidiremcomqualop çãoeles
seguirãoemfrente.
Figura2.8: SessãodeBrainstorm—Fonte: http://www.duarte.com/blog/
take-your-meetings-by-storm/
Moodboard
Umacole çãodeimagensereferênciasqueeventualmentesetransfor-
marãonoestilovisualdoprodutoemquestão.Ajudaoscriativosamostrarem
paraosclienteseparaoscolegasdetimealinhavisualqueestãoimaginando
paraoprodutoantesmesmodeabriremoPhotoshopecome çaremafazero
26

## Página 43

CasadoCódigo Capítulo2. MétodoseentregáveisdeUX
layout.
Figura 2.9: Moodboard — Fonte: http://clearleft.com/thinks/
visualdesignexplorations/
Storyboards
Umaespéciedehistóriaemquadrinhosdasériedeaçõesqueosconsum-
idorestomarãoenquantoestãousandooproduto.Traduzemfuncionalidades
deformamaistangível,emsituaçõesreaisdodiaadia,ajudandodesignersa
criaremempatiacomoconsumidorenquantojácome çamaterumaideiado
escopodoproduto.
27

## Página 44

2.2. Geraçãodeideias CasadoCódigo
Figura 2.10: Storyboard — Fonte:http://www.fabiangarzon.com/mobile_
deals_2010.html
Fluxodousuário
Umarepresentaçãovisualdofluxodousuárioparacompletartarefasden-
trodoproduto.Ousuáriocome çapelahomepage,depoisentranapáginade
umproduto,depoisvaiatéocarrinhodecompras–eassimpordiante. É
aperspectivadousuáriosobreaorganizaç ãodosite,queajudaaidentificar
quaispassosprecisamsermelhoradosouredesenhados.
28

## Página 45

CasadoCódigo Capítulo2. MétodoseentregáveisdeUX
Figura2.11: Fluxodousuário—Fonte:http://wireframes.linowski.ca/2010/
04/grand-narratives-play-points/
Análisedetarefas
Umdetalhamentodasinformaçõeseaçõesnecessáriasparaqueousuário
completeumatarefa.Ajudadesignersedesenvolvedoresaentenderemosis-
temaatualecomoainformaç ãotransitadentrodele. Tambémajudaadis-
tribuirastarefascorretamentenonovoprodutoqueestásendodesenhado.
Taxonomia
Umaexploraçãoemtornodasmúltiplasformasdecategorizarconteúdo
einformação:comoaseditoriasemumsitedenotíciasouascategoriasde
produtosemume-commerce,porexemplo.Contribuiparaqueosdesigners
definamaestruturadeconteúdoerótulosqueajudarãoousuárioasemovi-
mentarpelosite.
2.3 Planejamento do produto
Essessãoalgunsdosmétodosusadosquando,passadaaetapadegeraç ãode
ideias,chegaahoradeplanejaredesenharoprodutoemquestão.
29

## Página 46

2.3. Planejamentodoproduto CasadoCódigo
Auditoriadeconteúdo
Éaatividadedelistartodooconteúdodisponívelemumsite. Alista
seráutilizadaemváriasetapasdoprojeto,ajudandoaenxergarsuatotalidade,
definiraestratégiadeconteúdoeaaveriguarosdetalhesdecadaumadas
páginas.
Análiseheurística
Umaanáliseminuciosadeumprodutoquedestacaasboasemáspráti-
casdeUX,usandoprincípiosconhecidosdeDesigndeInteraç ãocomoguia.
Ajudaavisualizaroestadoatualdosistemaemmatériadeusabilidade,efi-
ciênciaeeficáciadaexperiência.
Figura 2.12: Análise heurística — Fonte:http://www.smashingmagazine.
com/2011/12/16/a-guide-to-heuristic-website-reviews/
Sitemap
UmdosmétodosmaisconhecidosdeUX.Consisteemumdiagramadas
páginasdeumsiteorganizadashierarquicamente.Ajudaavisualizaraestru-
30

## Página 47

CasadoCódigo Capítulo2. MétodoseentregáveisdeUX
turabásicaeanavegaç ãoentreasdiferentespartesdosistema.
Figura2.13: Sitemap—Fonte:http://www.mattmairlowery.com/portfolio/
educationplus-portal/
Roadmapdefuncionalidades
Éoplanodeevoluç ãodoproduto,comasfuncionalidadesjápriorizadas.
Podeserumaplanilha,umdiagramaouumasériedepost-itsorganizados
sobreumpainel. Ajudaacompartilharavisãoestratégicacomotimeea
enxergarocaminhonecessárioparasechegaratélá.
31

## Página 48

2.3. Planejamentodoproduto CasadoCódigo
Figura 2.14: Roadmap de funcionalidades — Fonte: http://www.aha.io/
product/features/publish
Cenáriosecasosdeuso
Umalistaexaustivadoscenáriospossíveisenquantoosusuáriosestãoin-
teragindocomoproduto: logado,não-logado,primeiravisitaetc. Ajudaa
garantirquetodasasaçõessãopossíveisdentrodosistema,assimcomovisu-
alizarcomoelesecomportaemcadaumdoscenárioslistados.
Análisedemétricas
Análisedosnúmerosfornecidosporalgumaferramentademétricasque
dãoinsightssobrecomoosusuáriosinteragemcomoproduto:númerode
cliques,tempodenavegaç ão,palavras-chavebuscadasetc.Osnúmerosaju-
damadescobririnsightsvaliosossobreocomportamentodosconsumidores,
quemuitasvezesnãopodemsercapturadosemumtestedeusabilidade.
32

## Página 49

CasadoCódigo Capítulo2. MétodoseentregáveisdeUX
2.4 Pesquisa e v alidação
SãométodosutilizadospeloUXdesignerparaentendercomooconsumidor
pensa,oqueesperadoprodutoecomointeragecomele.
FocusGroup
Umpaineldediscussãocomváriosusuáriossobredeterminadoassunto
ouquestão.Ajudaaentenderossentimentosdaspessoas,suasopiniõeseaté
alinguagemqueutilizamaofalaremsobreoproduto.Útilquandootimenão
estámuitofamiliarizadocomopúblico-alvodoproduto.
Figura 2.15: Sessão de Focus Group — Fonte: http://www.
quest-research-solutions.co.uk/
Pesquisaquantitativa
Questõesqueproduzemumnúmerocomoresultado.Éumaformarápida
esimplesdemedirasatisfaç ãodosconsumidoresecoletarfeedbacksobreo
produto. Aspesquisasquantitativaspodemapontaranecessidadedeoutro
tipodepesquisaemprofundidade.
33

## Página 50

2.4. Pesquisaevalidação CasadoCódigo
Figura 2.16: Formulário de pesquisa quantitativa — Fonte:http://www.
surveygalaxy.com/default.asp?m=7&id=0009&dir=/articles/&lang=en-GB
Testedeusabilidade
Umaentrevistaum-a-umcomoconsumidor,naqualpede-seaeleque
realizeumasériedetarefasemumprotótipooumesmonoprodutofinal.
Àmedidaqueoconsumidorinteragecomoproduto,opesquisadorfazan-
otaçõessobreseucomportamentoesuasopiniões. Ajudaavalidarfluxos,
layoutsefuncionalidades.
34

## Página 51

CasadoCódigo Capítulo2. MétodoseentregáveisdeUX
Figura 2.17: Sessão de teste de usabilidade —
Fonte: http://curveagency.com/blog/user-experience/
responsive-wireframe-usability-testing-tips-and-tricks
CardSorting
Umatécnicaqueconsisteempediraosusuáriosqueagrupemconteúdos
efuncionalidadesemcategorias.Dáinputsvaliososaotimesobrehierarquia
deconteúdo,organizaçãoetaxonomia.
TesteA/B
Trata-sedeoferecerduasversõesdiferentesdoprodutoparadiferentes
usuárioseverqualdelastemmelhoresresultados. Ótimoparamelhorara
taxadeconversãodefunisdecompra,landingpagesouformuláriosdecadas-
tro.
35

## Página 52

2.5. Desenhodeinterfaces CasadoCódigo
Eyetracking
Umatecnologiaqueconsegueanalisaromovimentodosolhosdousuário
àmedidaqueeleinteragecomoproduto.Dáinformaçõessobreaspartesda
interfacequemaisinteressamaousuárioetambémsobrequalaordemde
leituradoselementosdatela.
Análisedeacessibilidade
Umestudoquemedeseositepodeserusadoporqualquerpessoa,in-
cluindousuárioscomnecessidadesespeciais.
2.5 Desenho de interfaces
EssessãoosentregáveismaiscomunsdeUXDesign:aquelesquedocumen-
tamcomodeterminadateladevefuncionar.Sãoótimasferramentasparaco-
municarideiascomoutrosmembrosdotime,clientesetodasaspartesen-
volvidasnoprojeto.
Sketches
Umaformarápidaderabiscarumanovainterfaceusandopapelecaneta.
Sketchespodemsermuitoúteisparavalidarrapidamenteconceitosdepro-
dutoseideiasdedesigncomosoutrosmembrosdaequipeecomusuários.
36

## Página 53

CasadoCódigo Capítulo2. MétodoseentregáveisdeUX
Figura2.18:Sketches—Fonte:http://www.smashingmagazine.com/2013/06/
24/sketching-for-better-mobile-experiences/
Wireframes
Umguiavisualquerepresentaaestruturadapágina,bemcomosuahier-
arquiaeosprincipaiselementosqueacompõem.Útilparadiscutirideiascom
otimeecomosclientes,etambémparainformarotrabalhodosdiretoresde
arteedesenvolvedores.
37

## Página 54

2.5. Desenhodeinterfaces CasadoCódigo
Figura 2.19: Wireframe — Fonte:http://fundamentals.melissacabral.com/
evening-example-information-architecture-and-wireframe/
Protótipos
Umprotótipoéumasimulaç ãodanavegaç ãoedasfuncionalidadesde
umsite,compostonormalmenteporwireframesclicáveisoulayouts.Éuma
formarápidadevalidaretestarumprodutoantesdedesenvolvê-lodocome ço
aofim.
Bibliotecadepadrões
Umalistapráticacomexemplos(eàsvezescódigo)dospadrõesdeinter-
açãoqueserãousadosemtodoosite.Nãosóajudaamanterodesignconsis-
tenteemdiferentestelas,mastambémfacilitaavidadosdesenvolvedoresna
horadeimplementaroselementos.
38

## Página 55

CasadoCódigo Capítulo2. MétodoseentregáveisdeUX
Alistaébastanteamplaemesmoprofissionaisespecializadosacabamnão
dominandoouusandotodosessesmétodoscomfrequência.Nodecorrerdo
livro,vocêveráemmaisprofundidadealgunsdeles: wireframes,protótipos,
sketches,bibliotecasdepadrões, testesdeusabilidade etestesA/B.
Gosta desse assunto?
SevocêseinteressaemconhecermaissobreosmétodosdeUX,acesse
http://fabricio.nu/metodosparavermaislinkseexemplos.
39

## Página 57

Capítulo3
Wireframes,protótipose
rabiscoframes
Wireframeéumdesenhobásicodaestruturadedeterminadainterfaceque
demonstradeformasimplificadacomooprodutofinaldeveráfuncionar.

## Página 58

CasadoCódigo
Figura3.1:WireframedoaplicativoPocketPass,daMetlife,quedesenvolvi
em2010
Normalmente,eleéfeitoemtonsdecinza,semimagens,eomaiorob-
jetivoéorganizaroselementosqueentrarãonacomposiç ãofinaldodesign.
Essetipodedocumentaç ãoajudatantoosdiretoresdearte–aentenderemos
elementosessenciaisnahoradecriarolayout–quantoosdesenvolvedores
–que,apartirdowireframe,jáconseguemestimaroesfor çodetrabalho,
começaramodelagemdedadoseatéatestarsoluçõesdefront-endquese
adequemàsoluçãopropostapeloUXdesigner.
Pensenoprocessodeconstruç ãodeumprédio.Antesdecome çaraer-
guerasparedes(emesmoantesdecomprartodoomaterialnecessáriopara
aconstrução),existeumaetapadeplanejamento.Éprecisoentenderoobje-
tivodaqueleespaçoqueseráconstruído(exemplo:moradia),asfun çõesque
42

## Página 59

CasadoCódigo Capítulo3. Wireframes,protótiposerabiscoframes
aspessoasrealizarãoalidentro(comer,dormir,socializar)e,apartirdaí,criar
asváriasseções(cômodos)paraaspessoascircularem.
Figura3.2:Oswireframesatéseparecemumpoucocomaplantabaixausada
porengenheirosearquitetos
Sóquandoestátudodefinido,aprovadoetestado,équeaconstruç ão
começaefetivamente. Noprocessodeconstruç ãodeprodutosdigitaiséa
mesmacoisa.
43

## Página 60

3.1. Comonascemoswireframes CasadoCódigo
3.1 Como nascem os wireframes
Paracriarowireframedeumproduto,oUXdesignercostumalevaremconta
váriosfatores:
• Osobjetivosdenegóciosdocliente,quenormalmentesãopassadosno
iníciodoprojetoemformatode briefing;
• Osrequisitostécnicosdosistema–sejaumnovosistemaouumsistema
legado;
• Oconceitocriativodoproduto,quandoexisteumtimedecriaç ãoen-
volvido;
• Osguidelinesdebrandingetomdevozdamarca/empresaemquestão;
• Asboaspráticasconhecidasdeusabilidadeenavegação;
• Aspossibilidadeselimitaçõestécnicasdaplataformaondeoproduto
finalserádesenvolvido(HTML,CSS,JS,C++etc.);
• Aspossibilidades,limitaçõeseboaspráticasdohardwareondeainter-
faceseráacessada(computadoresdesktop,smartphones,tablets,caixas
eletrônicosetc.).
Umavezquetodosessesrequisitossãolevantados,chegaahoradeoUX
designercolocarnopapelumaprimeiramaterializaç ãodoquesesabesobre
oproduto.Duranteoprocessodedesenhodeumwireframe,oprofissional
deUXprecisafazerumasériededecisõesqueeventualmenteinformarãoo
layoutdoproduto.
Qualaprimeiracoisaquevocêquerqueousuáriovejaquandoelechegar
nahomepagedosite? Queinformaçõesvocêprecisamostrarparaqueele
entendadoquesetrataoseuproduto?Comoaproveitaraaltavisibilidadeda
páginainicialparamostrarconteúdorelevanteparaosvisitantes?
44

## Página 61

CasadoCódigo Capítulo3. Wireframes,protótiposerabiscoframes
Figura3.3:WireframedositeGoogleCreativeSandbox,noqualtrabalheiem
2012
Alémdoconteúdodaspáginas,oUXdesignerprecisapensartambém
emummétododenavegaçãoquepermitiráqueousuárionavegueentreelas.
Algunssitesouaplicativospossuemmenusfixosnotopo,comlinkparatodas
(ouasprincipais)páginas.Éocasodose-commercesousitesinstitucionais,
porexemplo.Jáoutrossitespossuemumfluxomaislinear:háapenasuma(ou
algumas)açõesqueousuáriopodetomarnaprimeirapágina,edependendo
dessaaçãoeleveráumanovapágina,eoutra,eoutra. Paraalgunssitesfaz
sentidodisponibilizarumcampodebusca,paraoutrosnemtanto.
Determinadosoconteúdoeanavegaç ão,éprecisopensartambémnas
interações. Comoainterfacesecomportaquandoousuáriointeragecom
ela?Hásempreumatrocadepágina?Oualgumasvezesasaçõesdosusuários
revelarãonovosconteúdosnamesmapágina? Hásom? Háfeedbackpara
cadaaçãotomada?
45

## Página 62

3.2. Comointerpretarumwireframe CasadoCódigo
Nofimdascontas,umdocumentodewireframeéadocumentaç ãode
todasessasdecisõesdeformaclara,queconsigaserinterpretadaporoutros
profissionaisquetambémestãoenvolvidosnoprojeto.
3.2 Como interpretar um wireframe
Sevocêtrabalhacomdesenvolvimentodeprodutoseinterfacesdigitais,é
provávelquejátenhavistoeusadowireframesnoseudiaadia.Mesmoem
timesemquenãoháumUXdesignerouarquitetodeinformaç ão,outraspes-
soaspodemacabarficandoresponsáveisporplanejarosdetalhesdainterface
antesdeodiretordearteabriroPhotoshop–sejaoprópriodesenvolvedor,
umanalistadeespecificaç ãoou,àsvezes,oprópriogerentedeprojetos.
Aindaassim,muitagentetemdúvidasobrearealfun çãodeumwireframe
edecomofiltraroqueestásendomostradoalidamaneiracorreta.
46

## Página 63

CasadoCódigo Capítulo3. Wireframes,protótiposerabiscoframes
Figura3.4:WireframedoaplicativodeiPaddaDomino’s,noqualtrabalhei
em2011
Oqueowireframemostra:
•Ahierarquiadainterface.Elementoscommaispesovisualnowire-
frameindicamoselementosquedevemserpriorizadospelodiretorde
artenahoradecomporolayoutfinaldoproduto.
•Disposiçãodasinformaç õesnatela.Owireframenormalmentetraz
umasugestãoinicialdecomooselementosdevemserdispostosnain-
terfaceparagarantiraordemdeleituraadequadaparaousuário. É
claroqueodiretordeartepodepropormudan çasnahoradecompor
olayout,masaestruturanormalmentepermaneceamesma.
•Quantidadeetipodeconteúdo.Apesardeowireframeusartextose
imagensdemarcação,atravésdelejáépossívelvisualizarquaisosdifer-
entesatributosqueaparecerãonainterface.Porexemplo:napáginade
47

## Página 64

3.2. Comointerpretarumwireframe CasadoCódigo
umanotíciateremosotítulo,osubtítulo,otextocompleto,de3a5
imagens,onomedoautor,adatadepublicaç ãoeumespaçoparaco-
mentáriosdosleitores.
•Menuseelementosdenavegaç ão.Oswireframesquasesemprecon-
têmumasugestãodecomoomenudosite/aplicativoestaráestrutu-
rado:quaissãoositensdemenu,emqualordemelesaparecem,como
anavegaçãonomenufunciona.
•Comportamentoemváriostamanhosdetela. Nocasodesitesre-
sponsivosoumesmoaplicativosdesmartphonequefuncionemno
modoretratoepaisagem,oswireframespodemserusadosparaex-
plicarcomooconteúdodainterfaceseadaptaadiferentestamanhose
orientaçõesdetela.
•Requisitosdenegóciosesistema.ComooUXdesignerlevaemconta
osrequisitospassadospeloclienteepelotimededesenvolvedoressobre
comoosistemafunciona,owireframejáéumarepresentaç ãoapurada
dafuncionalidadedosistema.
•Variaçõeseestadosdiferentesdosistema.Owireframenormalmente
contémumaindicaçãodecomoumamesmatelasecomportaemdifer-
entescondições:quandoousuárioestádeslogado,quandoestálogado,
quandoacessaositepelasegundavez,quandoentrounositeatravésde
umbanneroupontodeentradaespecífico,quandoumadeterminada
listagemcontémzeroitem,umitemouduzentositens–eassimsucessi-
vamente.Normalmente,desenvolvedoresedesignerstrabalhamjuntos
paradefinirquaissãoasprincipaisvariaçõeseestadosdosistemaque
precisamserdocumentadospelowireframe.
48

## Página 65

CasadoCódigo Capítulo3. Wireframes,protótiposerabiscoframes
Figura3.5:Comparativoentrewireframeelayoutfinaldeumsite
Oqueowireframenãomostra:
•Olayoutfinal.Obviamente,owireframenãoéumespelhodoproduto
final.Botõespodemmudardeposiç ão,linkspodemvirarbotõesevice-
versa,imagenspodemacabarcomtamanhooupropor çõesdiferentes
nolayoutfinal,aordemdoselementoseaformacomoestãoagrupados
podemmudar.
•Aidentidadevisualdamarca.Detalhescomocores,tipografia,logo
equaisqueroutroselementosdebrandingserãorevisadospelodiretor
dearte.
•Textoeconteúdofinal.Depoisdowireframeterminado,normalmente
umredatoréquemvaitrabalharnosrótulosetextosfinaisdainterface.
ApesardeoUXdesignerjáfazerumasugestãodequalotamanhore-
comendadodostextos,épossívelquemuitacoisamudenahorade
popularainterfacecomoconteúdorevisado.
49

## Página 66

3.3. Asvantagensdeusarwireframesnoprocesso CasadoCódigo
•Todososcasosdeusodoproduto.Comoditoanteriormente,owire-
framenormalmenteconsideraosprincipaiscasosdeusoerefletevari-
açõesecenáriosmaiscomunsqueosusuáriosencontrarãonopro-
duto. Masexisteanecessidadedeumolharmaisapurado,normal-
mentefeitoporumanalistadeespecificaç ãooudesenvolvedor,sobre
todososcenáriosquepodemacontecerquandoaspessoasforemusar
oproduto.Essescenáriospodemserrepresentadosporumanovaro-
dadadewireframes,masemmuitoscasosapenasumadiscussãoentre
designersedesenvolvedoresésuficienteparadecidircomoainterface
secomportanessescasos.
3.3 As v antagens de usar wireframes no pro-
cesso
Wireframesexistemparaevitartrabalhodesnecessário. Équasecomoum
rascunhodolayoutfinal.Comotodorascunho,écriadoparaqueaspessoas
consigamdarfeedbacksobreele,paraqueeleentãopossaserajustadoeir
paraasoutrasáreasenvolvidasnoprojeto.
Umwireframenuncaestá100%pronto. Justamenteporserumdocu-
50

## Página 67

CasadoCódigo Capítulo3. Wireframes,protótiposerabiscoframes
mentofocadoemcolaboraç ãoediscussão,éimportantequeoUXdesignero
compartilhecomtodososmembrosdotime(desenvolvedores,diretoresde
arte,gerentedeprojetos,cliente)etambémcomousuáriofinal.Muitasvezes,
oswireframesjásãosuficientesparamostrarainterfaceparaumusuárioe
colherfeedbacksobreospontosfortesefracosdasoluç ãoproposta,antes
mesmodeolayoutfinalsercriadopelodiretordearte.
AprincipalvantagemdeusarwireframesemvezdelayoutsnoPhoto-
shopéafacilidadeeagilidadeemfazerajustes,mudartudooucome çaroutra
vez.Émuitomaisrápidoefazmuitomaissentido.Aprópriaaparência“de
rascunho”doswireframes(feitoemtonsdecinza,semimagensouconteúdo
final)colaboraparaqueaspessoassesintammaisàvontadeparadarfeed-
backesugerirmelhorias.Afinal,émuitomaisfácilvocêcriticarumtrabalho
quefoifeitorapidamenteempoucashorasdoquevocêpedirparaumdire-
tordearte,quegastoudiaspolindoainterface,pixelapixel,fazergrandes
alterações.
Muitosgestoresdeprojetospreferemesperarparaqueumwireframees-
teja100%aprovadopeloclienteeportodasasáreasenvolvidasantesdepassar
adocumentaçãoadianteparaodiretordearteeoprogramadorcome çarem
otrabalho. Éotaldeprocessodecascata,quemitigaoriscoderefaçõese
alteraçõesapósomomentoemqueodocumentofoiaprovado–apesarde
nãoeliminarosajustesdeúltimahorapedidospeloclienteoucausadospor
limitaçõestécnicasnahoradeimplementaroproduto.
Avantageméqueosprogramadores(tantofront-endquantoback-end)
jápodemcomeçarseutrabalhoapósadefiniç ãodoswireframes.Pormaisque
oprogramadorfront-endnãotenhaolayoutfinal,elejápodeirpensandona
arquiteturadastelas,estruturadepastas,arquivosdeestiloeoutrasdefinições
macro.Poroutrolado,oprogramadorback-endconsegueentenderamod-
elagemdedadosnecessária,ainfraestrutura,ostiposderequisiç ãoetráfego
deinformaçõesqueacontecerãonosistema.
3.4 Alternativ as aos wireframes
Wireframessãoumaótimaferramentanahoradedemonstrarcomouma
interfacedevefuncionarequaisinformaçõesestãocontidasnela.Alémdisso,
51

## Página 68

3.4. Alternativasaoswireframes CasadoCódigo
sãomuitomaisrápidosdeseremproduzidos(ealterados)doqueoslayouts
emPhotoshop.
Durantemuitosanos,owireframefuncionoucomope çaessencialem
projetosdigitaisdemédioegrandeporte. Éadocumentaç ãoemquetodas
asáreassebaseiamnahoradeiniciarseusesfor ços–sejaodiretordearte,o
programadorfront-end,back-endouoredator.
Noentanto,nosúltimosanossurgiramoutrasferramentaseentregáveis
queconseguemcumpriromesmopapelqueoswireframesemmuitomenos
tempoecomumpensamentoaindamaiságil.
Atéalgunsanosatrás,emgrandesempresas,eramuitocomumqueem
umprojetofossemdesenvolvidoswireframes, layoutsedepoisprotótipos
navegáveisdeumadeterminadainterface.Umprocessodetrabalhoemcas-
cata,emquecadaentregaévalidadacomoclienteparaqueaetapaseguintese
inicie.Essaéumaformaseguradegarantirqueovisualdesignersócome çará
atrabalharquandoowireframetiversido100%aprovado,evitandohorasdes-
perdiçadasemretrabalho.
Aconteceque,noexemplocitado,otimeacabadesenvolvendo3protóti-
possequenciais.Owireframenadamaisédoqueumprotótipo,umasimu-
laçãodecomoainterfacedevefuncionar. Olayoutem jpgtambéméum
protótipo,umasegundasimulaç ãodamesmainterface.EquandooUXde-
signerutilizaumaferramentadecriaç ãodelayoutsclicáveisouprotótipos
navegáveis,eleacabacriandoumterceiroprotótipodamesmatela.
O pior: nada disso é aproveitado na hora de os desenvolvedores es-
creveremocódigofinal. Essadocumentaç ãotodacriadapelosdesigners
acabasendousadoapenascomoreferênciaparaosdesenvolvedores.Ealguns
projetosexigemummétodomaiságildoqueessepensamentoemcascata.
FoicomesseobstáculoemvistaquealgunstimesdeUXdesignersno
Brasilenomundocome çaramatestaroutrasalternativasparaagilizaressa
etapadoprojeto.
Entreasalternativasmaiscomunsaoswireframesestáticos,estão:
Wireframescolaborativosentretodosdotime
EmvezdeoUXdesignerouarquitetodeinformaç ãodesenharoswire-
framessozinho,sentadoemsuamesa,épossívelpensaremummétodomais
52

## Página 69

CasadoCódigo Capítulo3. Wireframes,protótiposerabiscoframes
colaborativoparaacriaç ãodosmesmos:envolverodiretordearte,ogerente
deprojetos,oredator,ofront-enddeveloper,oback-enddevelopereoplane-
jadorecolocartodosjuntosemumasaladereuniãoparamontaremastelas
juntos–compapel,post-itsecaneta.
Cadaumcolocaseupontodevistaemcadadecisãotomada. Funciona
muito bem, especialmente para produtos com poucas telas. Em poucas
sessõesdeumaouduashorascada,épossíveldefinirofluxoprincipaldo
siteaváriasmãos.Amelhorparteéque,saindodareunião,todosjásabem
oqueositedeveconterejápodemcome çaratrabalharnomesmodia,sem
precisaresperarqueoUXdesignerfinalizeumdeckdewireframesdevárias
páginasparaisso.
Desenhosnopapel+guiasdeestilos
Emalgunscasosespecíficos,ficamaisfácildesenharempapeloconteúdo
datelaejápartirparaoPhotoshopcomodiretordearte.Adiferen çaéque,
emvezdefazerolayouttelaatela,odiretordeartecriaapenasoselementos-
53

## Página 70

3.4. Alternativasaoswireframes CasadoCódigo
chavedainterface,separadamente,comoemum styleguide.Oprogramador
front-endjuntaasduascoisas(osketchcomostyleguide),diretonocódigo.
IssotornaaetapadeUXearquiteturadeinformaç ãomuitomaiscurta,e
tambémsimplificaotrabalhododiretordearte.Maséummétodoquenão
funcionamuitobemcasoositetenhaumsistemaback-endmuitocomplexo
(comouminternetbanking,porexemplo);algumasregrasprecisamserdoc-
umentadasemmaisdetalhesparaosdesenvolvedores.
Protótiposnavegáveis
Aop çãodecriarprotótiposnavegáveispodeserfeitausandoalgumafer-
ramentadewireframingquepermitacriarlinksentreumatelaeoutra. No
final,emvezdeumwireframeestático,otimeconseguenavegarporumpro-
tótipoclicávelquesimula,emvariadosníveisdefidelidade,comoainterface
finalfuncionará.
Figura3.6:ExemplodeprotótiponavegávelcriadopeloUXdesigner
Avantagemdessaalternativaéqueficamuitomaisfácilparaoclienteen-
tendercomooprodutoiráfuncionar,semprecisarpercorrerextensaspági-
54

## Página 71

CasadoCódigo Capítulo3. Wireframes,protótiposerabiscoframes
nasdewireframesestáticos.Aparteruiméqueissonãodescartaotrabalho
inicialdepensarnaAIdapágina(ecomporolayout,casovocêqueiraque
omockuptenhaovisualfinal).Outropontonegativoéque,dependendoda
linguagemtécnicaemqueesseprotótipofoicriado,ocódigoacabanãosendo
aproveitadopelosdesenvolvedoresnahoradecolocaramãonamassaecriar
efetivamenteoproduto.
UXdesigneraprendendoaprogramar
Essaéumaótimaalternativa,paraqueopróprioUXdesignermonteo
wireframeouprotótipousandoHTMLeCSS.Muitagentetemfaladohoje
emdiasobre“desenharnoprópriobrowser”,emvezdedesenharainterface
primeironoPhotoshop.Aparteboaéqueoprotótipoficamuitomaisreal-
istaeodesenvolvedorconsegueaproveitarumapartedocódigonofuturo.
AparteruiméoriscodeoUXdesignerficarmuitoentretidonaslinhasde
códigoeterpoucotempoparaseafastardaexecuç ão,terumavisãoholís-
ticadaexperiênciaeadvogarmaispelousuáriodoquepelainterface–que,
convenhamos,éoqueoUXfazdemelhor.
UXedesenvolvedorfront-endcriandoprotótiposjuntos
Essepareceserumdosmelhorescaminhosparaondeostimesestãoru-
mando–ou,pelomenos,ocaminhoquetemfuncionadoparamaistiposde
projetos.Cria-seumadupladeUXdesigneredesenvolvedoreelesdesenham
emontamjuntosoprotótipo.Tudoéfeitosemmuitanecessidadededocu-
mentação,jáqueelessentamladoaladoediscutememtemporealasdecisões
dedesignqueprecisamserfeitas.Comoéoprópriodesenvolvedorfront-end
queestáescrevendoocódigo,100%deleéreaproveitadonoprodutofinal–
elesóprecisaadicionaroestilodepoisqueovisualdesignertiverdefinidoo
styleguidenoPhotoshop.
Umadasprincipaismotivaçõesnesseprocessodereinventarofluxode
trabalhodeumtimedeDesignéaconstataç ãodequewireframesestáticos
nãotêmtidoumbomdesempenhoemcertostiposdeprojeto.Entreosprin-
cipaisproblemasdeusarsomentewireframesestáticos,estão:
• Wireframesestáticosnãosãomuitobonsemrepresentarumdesign
55

## Página 72

3.5. Asvantagensdosprotótipos CasadoCódigo
responsivo,anãoserquevocêdesenhe5versõesdiferentesdeleoumais
(umaparacadatamanhodetela);
• Wireframesmuitasvezestentamsimularumcomportamentoquejáé
nativodoHTMLedoCSS(oudalinguagemdeprogramaç ãonaqual
oprodutofinalserácriado);
• Alteraçõesnowireframedealtafidelidadepodemlevarmaistempo
paraseremfeitasdoquenocódigo,pormaisquevocêuseelementos-
mestreseoutrastáticas.
Éclaroquenãoexisteumarespostadefinitivaparaamelhoralternativa
aoswireframes.Possivelmente,elesnuncaserãocompletamentesubstituídos,
jáquefuncionamecontinuarãofuncionandomuitobemparadeterminados
projetos,timesemétodosdetrabalho. Sevocêestácome çandoagoraase
aventurarpelomundodeUserExperience,oswireframescontinuamsendo
ocaminhomaisseguroerazoáveldedocumentaroseutrabalho.
Cadaumadessasalternativaslistadasanteriormentetemseusprósecon-
tras.CabeaoUXdesignereaodesenvolvedorentenderemaferramentaque
funcionamelhorparaaqueleprojeto,paraaqueleprazo,paraaqueletimee
paraaquelecliente. Éessacapacidadedeseadaptaradiferentescontextos
quediferenciaosmelhoresprofissionaisdeUXnomercado.
3.5 As v antagens dos protótipos
Protótipossãoversõesinterativasdoswireframes,ondeépossívelclicarou
interagircomalgumaspartesdatelaparasimularcomoseráoseufunciona-
mento–mesmoqueaindaafuncionalidadeaindanãotenhasidoimplemen-
tadacorretamente.Écomosefosseumrascunhodotrabalhoquedepoisserá
realizadopelodesenvolvedorfront-end.
Como mencionado anteriormente, a criação desse tipo de protótipo
navegávelpodeteralgumasvantagensemrelaç ãoaoswireframesestáticos:
Experiênciadenavegação
Apossibilidadedenavegarpeloprotótipofazmuitadiferen çanahorade
“sentir”comooprodutofinalfuncionará. Elesimulaoqueaconteceacada
56

## Página 73

CasadoCódigo Capítulo3. Wireframes,protótiposerabiscoframes
clique,acadainteraç ão–resultadoesse,quesóseriapossíveldepoisqueo
projetojátivessesidoprogramadoporumdesenvolvedorfront-end.
Documentosmaisenxutos
Diferentedoswireframesestáticos,osprotótipospermitemquevocêrep-
resenteváriosestadosdiferentesdainterfaceemumamesmapágina.Quando
oUXdesignercriaumwireframeem PDF,cadanovoelementoquesurgena
tela(mesmoqueelenãorepresenteumapáginaseparadanaestruturadosite)
precisaserdocumentadoemumapáginadiferentedodocumento.Jáospro-
tótipospermitemquevocêvejaoselementosemfuncionamentonopróprio
contextoondeelesaparecem,fazendocomqueodocumentofinalsejabem
maisenxutodoqueosextensos PDFscomwireframesestáticos.
Apresentaçãoparaclientes
Designersedesenvolvedoresestãoacostumadosareceberumwireframe
em PDFeabstrairofatodequeaqueledocumentoéapenasumarepresen-
taçãodecomoainterfaceiráfuncionar. Comosanosdeprofissão,elesse
acostumamaconseguirvisualizarcomoaquelewireframesematerializará
umavezqueoprodutocome çaraserconstruídonalinguagemfinal–seja
umsiteemHTML,umaplicativoparaiOSouumgame.
Masmuitosclientesnãoestãoacostumadosalidarcomwireframesno
diaadia. Protótiposcontribuemparaqueosclientesentendammelhora
propostaeagilizamaaprovaç ãodotrabalho.Nasreuniõesdeapresentaç ãode
trabalho,bastaoUXdesignerpilotaranavegaç ãoeinteragircomoprotótipo
nafrentedoclienteparaqueeleentendacomoainterfacefunciona.
Ferramentasdefácilaprendizado
Existemváriasferramentasdisponíveisnomercadoparasecriarprotóti-
posnavegáveis. AlémdenãoprecisarconhecernadasobreHTMLouCSS
paraprototiparumsiteusandoessessoftwares,porexemplo,vocêconsegue
aprenderadominarosrecursosdaferramentajánoprimeirodiadetrabalho.
Normalmente,asempresasquefornecemessessoftwaresdeprototipagem
tambémdisponibilizamtutoriaisedicasemseussites.
57

## Página 74

3.5. Asvantagensdosprotótipos CasadoCódigo
NoBrasil,umadasferramentasmaispopularesdeprototipaç ãoéoAxure,
masháumapor çãodelas–cadaumacomumusoespecífico.
Gosta desse assunto?
Se você tem interesse em saber mais, acessehttp://fabricio.nu/
ferramentasparavermaisferramentasdeprototipaç ãoewireframe.
Designerseprogramadoresmenosirritados
Abrirumdocumentodewireframeem PDFepercorrertodasaspági-
naslendotodasasanotaçõesescritaspeloUXdesignerpodeserumtra-
balhomaçante. Quandoodocumentoémuitoextenso,háaindaoriscode
osdiretoresdearte,programadoreseclientesnãoseatentaremaosdetalhese
acabaremnegligenciandoalgunspontosimportantes.Osprotótiposacabam
deixandoaexperiênciadenavegarpelotrabalhodoUXdesignermaisinter-
ativa,menoscansativaemaispróximadarealidade.
Aprenderenquantodesenha
ParaopróprioUXdesigner,aprototipageméumaprendizadointeres-
58

## Página 75

CasadoCódigo Capítulo3. Wireframes,protótiposerabiscoframes
santíssimodedesign.Àmedidaquevocêvaigerandooprotótipoetestando
aquiloqueacaboudedesenhar,ficamaisfácilvisualizarasfalhasecorrigi-
lasnodecorrerdoprocesso. Quandovocêdesenhaummenu,porexem-
plo,jáconseguetestarseomenuestá“usável”namesmahora–algoqueé
quaseimpossívelpreverquandovocêestácriandowireframesestáticosenão-
interativos.
Maisfacilidadeparatestarcomusuários
Comoprotótipoemmãos,émuitomaisrápidoconseguircolocá-lona
frentedeusuáriosreaisparatestaroproduto. Emalgunscasos,vocêpode
atémandarolinkdoprotótipoparaalguémtestarremotamente,colhendo
feedbackquaseimediatosobreaquiloqueestásendodesenhado.
3.6 Como decidir entre protótipos e wire-
frames
Nosúltimosanos,ostimesdeUXdesignpassaramaincorporarprotótipos
emseufluxodetrabalhocommuitomaisfrequência.Apesardeoswireframes
estáticoscontinuaremfirmesefortes,osprotótipossurgempararespondera
algumasnecessidadesquesetornaramessenciaisnodiaadiadoUXdesigner.
SejamosprotótiposcriadosdiretamenteemHTML+CSS+JSoupor
umaferramentadeprototipagem,comoexplicadoanteriormente,osobje-
tivosdacriaç ãodeprotótiposfuncionaiscontinuamosmesmos:representar
linksentretelas,detalharasinteraçõesentreumestadoeoutrodosistema,
sermaisfielnarepresentaç ãodainterfaceefacilitarostestescomusuários.
Wireframeseprotótipossãotodosmembrosdeumamesmafamília.En-
quantooswireframesrepresentamainterfacecommenorfidelidade,ospro-
tótiposrepresentaminterfacesdeformamuitomaispróximadoprodutofinal.
Qualcritériousarparadecidirentreumeoutro
Naverdade,énoplural:critérios.SegundoesteartigodoUsabilityGeek
(http://usabilitygeek.com/when-to-prototype-when-to-wireframe-fidelity),
existemváriosaspectosquedevemserlevadosemcontanessadecisão.Vejaa
59

## Página 76

3.6. Comodecidirentreprotótiposewireframes CasadoCódigo
seguirumaversãoadaptadadalista,mostrandooscritériosquemaispesam
nahoradedecidirentrewireframeseprotótiposfuncionais.
Maisimportantedoquetentardizerseprotótiposinterativossãomel-
horesoupioresdoquewireframesestáticos,oobjetivodestalistaésomente
clarearerelembrarpontosquepodempassarbatidosnahoradefazeressa
escolha.Pararummomentoantesdeoprojetoiniciarparafazeressadecisão
émuitomelhordoquesimplesmentesairfazendoumououtroedepoisse
arrependernomeiodocaminho.
Budget
Primeiro,éimportantedeixardeladoaafirmaç ãocegaquedizquepro-
tótiposgastammaishorasparaseremfeitosdoquewireframesestáticos.
Depois,éprecisolevaremconta:
• Osoftwarequevocêpretendeusarparacriarcadaumdeles;
• Oprofissionalqueiráfazê-lo;
• Ahabilidadedoprofissionalcomtalferramenta;
• Oníveldedetalhamentoquevocêquerqueoprotótipotenha.
Apartirdomomentoemquevocêtemvisibilidadedessesquatroaspec-
tos,opróximopassoéestimarashorasnecessárias.Játiveexperiênciasóti-
masemqueumprotótipoeracriadodiretamentenocódigoporumadupla
deUXdesigner+desenvolvedorfront-end,emmuitomenoshorasinvestidas
doqueseodesignerestivessecriandosozinho.Tambémjávicasosnosquais,
naausênciadealguémcomhabilidadeemcriaç ãodeprotótipos,amelhor
soluçãoeradocumentarwireframesestáticosilustrandopassoapassocomo
ainteraçãoacontece.Asduasop çõespodemfuncionarbem,desdequetodos
dotimeestejamcientesdequalseráutilizada.
Fasedoprojeto
Umoutroaspectoparalevaremcontaéomomentoemqueoprojetose
encontra.
60

## Página 77

CasadoCódigo Capítulo3. Wireframes,protótiposerabiscoframes
•Momentodegeraçãodeconceitos:seotimedesejacriarváriasversões
diferentesdeumamesmaideiaparatestarqualfuncionamelhor,wire-
framesdebaixafidelidadepodemgarantirmaisrapideze“desapego”à
soluçãocriada.Issopodeserfeitoatémesmousandopapelecaneta.
•Momentodevalidaç ãodeconceito:seotimejáoptouporumcam-
inhocriativoeagoradesejatestarafundoseelefunciona,protótipos
dealtafidelidadetendemasermaisefetivosnahoradevalidarcom
usuáriosreais.
•Momentodeprodu ção: seoprodutojáestásendodesenvolvido,a
decisãofica,namaiorpartedasvezes,acritériodotimedeprogra-
madores.Qualomelhorjeito,paraeles,dereceberadocumentaç ão?
Altaoubaixafidelidade?Estáticoouclicável?
Complexidadedainterface
Quandooprodutoqueestásendocriadodependefortementedeumain-
teraçãoespecífica(exemplo: arrastarobonequinhodoGoogleMapssobre
61

## Página 78

3.6. Comodecidirentreprotótiposewireframes CasadoCódigo
umaruaparaativaroStreetView),talvezomelhorjeitodesaberseessain-
teraçãofuncionasejacriandoumprotótipofuncional. Quandovocêtenta
documentaressemesmotipodeinteraç ãoatravésdewireframesestáticos,é
precisosermuitomaisdetalhistacomoqueaconteceemcadaumdospassos
(sejaatravésdeumadescriç ãoemtexto,sejaquebrandoodesenhodainter-
açãoemváriosquadros).
Masseotrabalhoépuramentedearquiteturadeinformaç ão–organizar
conteúdo,navegaçãoemostrarhierarquiaemcadatela–talvezowireframe
estáticoacabesendomaisefetivoesimplesdeserdesenvolvido.
Leveemcontatambémseodesignéresponsivoounão.Dependendoda
suaescolhadeferramenta,serãonecessáriashorasamaisouamenospara
representarcomoainterfaceseadaptaparadiferentesresoluçõesdetela.
Sofisticaçãodaaudiência
Paraquemadocumentaç ãoseráapresentada?
Normalmente,opúblicointernodaagênciaouempresaondevocêtra-
balhacostumatermaisfacilidadedeabstrairwireframesestáticoseentender
comoasinteraçõesfuncionamsemanecessidadedeumprotótiporealistada
interface.
Masacoisapodemudarumpoucodefiguranocasodeclientes(depen-
dendodamaturidadeeexperiênciaqueelestêmemlidarcomdocumentaç ão
deUX)edeusuáriosfinais(algumaspessoaspodemterdificuldadedeenten-
derqueaqueledesenhoquevocêestámostrandoparaeleséarepresentaç ão
deumainterfacedigitalanimadaeinterativa).
Eseoobjetivoéencantaroclienteparaconvencê-loacompraroprojeto,
certamenteosprotótiposcausammelhorimpressão.
Ferramentashíbridas
Umaoutrasaídainteressanteéutilizarumaferramentahíbrida,queper-
mitecriartantowireframesestáticosquantoprotótiposinterativos.OAxureé
umbomexemplo:vocêsóadicionalinkseinteraçõesentreastelassequiser.
Issoaliviaopesodessa“decisão”entrewireframesestáticoseprotótipose
aindapermitequeotimemudedeumtrilhoparaooutronodecorrerdo
projetocasonecessário.
62

## Página 79

CasadoCódigo Capítulo3. Wireframes,protótiposerabiscoframes
3.7 Comunicando ideias com rabiscoframes
Aexpressão“rabiscoframe”éumamisturabemhumoradadotermosketch
(esboço,rabisco)comojáconhecidotermowireframe.Emmuitostimesde
desenvolvimentojásetornouparteessencialdoprocessodedesenhodeinter-
faces,especialmentenaquelemomentodoprojetoemqueasideiascome çam
atomarformaesairdoetéreomundodoPowerPoint.
63

## Página 80

3.7. Comunicandoideiascomrabiscoframes CasadoCódigo
“Sketchingpermitequeexploremosoproblemaedefinamosasolução
aomesmotempo.Atécnicaajudaadefinirmelhoronossoentendimento
doproblema,aomesmotempoemquenosajudaapensarnaspossíveis
soluções.
Enquantonósrabiscamosaquiloemqueestamospensando,novas
ideiasemergem.Aambiguidadeeafaltadedetalhesemumsketchgeram
novasideias.Aqui,ambiguidadeéumacoisaboa,porquenósautomati-
camentecome çamosapreencherosespaçosvaziosnanossacabe ça. É
issoquefazdosketchumatécnica“generativa":elacapturaaideiaque
nósjátemoseaomesmotempodespertanovasideias.
Aorabiscarmosnovassoluçõesparaoproblema,podemosexplorá-
lassemnecessariamentenoscomprometermosanenhumadelas. Isso
nosdánovosinsightsenovasperguntasparaseremrespondidas.Sketch-
ingéessencialmenteumexercíciodebrainstorm.”
porLennartHennigs,SmashingMagazine
Veja mais em http://www.smashingmagazine.com/2013/06/24/
sketching-for-better-mobile-experiences/
Algunsprofissionaisusamosrabiscoframescomoumaespéciede“ras-
cunho”dowireframefinal. Depoisdaprimeirarodadadedesenhosedis-
cussõescomotime,aísimoUXdesigner“passaalimpo”omaterialemforma
dewireframemaisformal,feitoatravésdealgumsoftware.
Masemoutroscasos,não:oprópriorabiscoframeacabasendoadocu-
mentaçãofinalparaasoutrasáreas. Quandootimeestámaisentrosadoe
acostumadoatrabalharemconjuntoequandonãoháanecessidadedefor-
malizarotrabalhodoUXdesigneremumwireframecompleto,opróprio
sketchéusadopelosdiretoresdearte,programadoresegerentesdeprojeto
paradaremsequênciaaotrabalho.
Aquestãoéquemuitagenteaindatemreceiodeassumirorabiscoframe
comoetapadametodologia,sejapornãodominaratécnicadedesenho,seja
porconsiderarosketchalgomuitoimaturoemuitasvezesinfielaoresultado
finaldainterface.
64

## Página 81

CasadoCódigo Capítulo3. Wireframes,protótiposerabiscoframes
3.8 Boas práticas para rabiscar
Existemváriosartigosdisponíveisonlinesobreboaspráticasnahoradecriar
seusrabiscoframes.Muitaspessoastêmresistênciaaincorporarossketches
emsuarotinadetrabalho,simplesmentepornãodominarematécnicadede-
senho.MasaverdadeéquevocênãoprecisaserumDaVinciparaconseguir
traduzirsuasideiasnopapel.
Nãosaberdesenharnãoéumproblema
Oprimeiropassoparacome çararabiscarumaideiaésedesprenderda
vergonhadenãosaberdesenhar. Muitagentenãonasceucomessedome,
assimcomoeu,sempretirounotasbaixasnastarefasdedesenholivredaes-
cola. Aquestãoéqueissotempoucaimportâncianahoraderabiscaruma
tela. Saberexpressarideiasnopapelsetornouumaquestãodesobrevivên-
ciaparaquemquerevitardiscussõespoucoprodutivas,emquecadaumdos
participantestemumaimagemdiferentenacabe ça. Odesenhoéfeitopara
ilustrarinformalmenteumaideiaeiniciarumadiscussão.Esó.Comotempo,
os“rabiscadores”vãopegandoapráticaeperdendoavergonha.Alémdisso,
osrabiscoframesnormalmentecirculamapenasentreosprópriosmembros
dotime.Sevocêtemvergonhademostrarumaideiaparaummembrodeseu
própriotime,entãooproblemanãoéafaltadehabilidadecomdesenhos.
Orabiscoframenãoéumaentrega
Osrabiscosraramentesãoentreguesaoclienteouaalguémdadiretoria
daempresa/agênciaondevocêtrabalha.Elesservemapenasparaospróprios
designersedesenvolvedoresentenderemoqueseesperadedeterminadain-
terface,ealgumasvezesnãoeliminamanecessidadedewireframesmaisde-
talhadossobreseuconteúdoefuncionamento.Normalmente,osrabiscosdu-
ramapenasalgunsdiase,àmedidaqueassoluçõesdesenhadasvãoseaper-
feiçoando,sãodeixadosdeladoesubstituídosporprotótiposmaiscompletos.
Osketchingéumexercíciocoletivo
Poucasvezesfizumrabiscoframesozinho,sentadoemminhamesa,ten-
tandoilustraralgoquejáestavadecidido. Atáticadolápisepapelnor-
65

## Página 82

3.8. Boaspráticaspararabiscar CasadoCódigo
malmentesemostranecessárianasdiscussõescomoutrosparticipantesda
equipe,nomomentoemquecome çamasurgirasprimeirasdúvidasedi-
vergênciasdeopiniõessobrecomodeterminadateladevesecomportar.Sea
soluçãojáestádefinidaevocêsóprecisadocumentá-la,asugestãoéirdireto
aossoftwaresdewireframeouprototipagem.
Aborrachaédispensável
Sevocêsentevontadedecorrigiralgoqueacaboudedesenhar,ésinalde
quejáestáemumestágiodedetalhamentoposterioraorabiscoframe. Ele
exigeumaboadosedeabstraç ãodetodasaspartesenvolvidas. Discussões
como“menuhorizontalouvertical?”ou“imagemnaesquerdaounadireita?”
devemsertomadasmaisparafrente,oudiretonoPhotoshop.
Tenhasempreumcadernoàmão
Terumcadernoàmãoemqualquerdiscussãooubrainstorméumaboa
dicaparacome çarafazerdosrabiscoframesumhábito.Instigueodesigner
arabiscaraquiloqueeleestásugerindoeofere çaaeleseuprópriocaderno.
Cadernosfuncionammelhordoquefolhassoltas,jáqueelastendemase
perdernomisteriosoburaconegrodasnossasmesas.Enofim,háumcerto
orgulhoemguardaraquelecadernocheioderabiscoscriativos.
NãotentepintarumquadrodeRembrandt
Segundo este artigo de Owen Shifflett (http://viget.com/inspire/
5-things-to-consider-whilst-sketching), opropósitoinicialdeumsketch
nãoéproduzirumaobradearte. Naverdade,focarmuitonosdetalhesdo
sketchpodeatrasarseuprogressoeaindafazercomquevocêpensenos
detalhesmaisdoquedeveriaeseesque çadeolharparaoquerealmente
importa:conceitoedire ção.Fazerumsketchmenosbemfinalizadotambém
facilitaemoutroponto:aspessoasficammaisàvontadeparadarfeedbacke
alteraroseudesenhoquandoelenãoestáfinalizadooupolido.
Façasketcheslogo,ecomfrequência
Depoisqueossketchesforamaprovadospeloclienteepelotime,éhora
66

## Página 83

CasadoCódigo Capítulo3. Wireframes,protótiposerabiscoframes
derefinaroquevocêfez.Continuartrabalhandocomsketchespormaisum
tempoajudaaevitarasíndromedo“ficarmexendocaixinhasnoPhotoshop
atédesmaiar”.Alémdisso,essamudançadomouseparaolápisepapelpode
ajudarbastanteaevitarbloqueioscriativos.Oprincipaléficaromaistempo
possívellongedocomputador–eleéumagrandeferramenta,mastambém
podeacabarsugandosuaalma.
Anotetudo
Éimportantequeseusketchcomuniquedetalhesocomportamentoda
interface,jáque,visualmentefalando,elesnãosãodesenhostãorefinadosas-
sim.Anotenamargemdopapeloucrieumsistemadelegendas.Issotambém
podeajudá-loalembrardemaisdetalhesquandoolharparaossketchesno
outrodia.
Criestoryboardssemprequepossível
ContarhistóriassignificalevarosespectadoresdopontoAaopontoB.
Storyboardssãoótimosparaisso.Nesseponto,éimportanteserconsistente
ereutilizarelementosquejátenhamsidodesenhados, paraqueapessoa
queestávendoosketchnãopensesetratardeumnovoelemento. Repare
comocartunistasutilizamenquadramentoeposiç ãodospersonagenspara
adicionarumpoucodecontextoeinten çãoemcadaquadro. Issotambém
podeserusadonahoraderabiscarinterfacesouanimações.
Adicionecorsomentequandofizersentido
Colorirseussketchespodedeixá-losmaisbonitos, masnãoépreciso
comprarumestojodelápisdecoresairpintandotudooquevocêdesenha.
Useascoresparadardestaqueaumelementoimportanteequerealmente
mereçadestaque.
Adica,nofimdascontas,ésaberadaptarasuaferramentaàsnecessidades
doprojetoemquestão.Vocênãoprecisaserumespecialistaemwireframes
ouumdesenhistaprofissionalparasetornarumUXdesigner.Omaisimpor-
tanteéopensamentoqueexistejuntocomodesenho,eaclarezanahorade
comunicá-loparaoutraspessoas.
67

## Página 85

Capítulo4
Aboaevelhausabilidade
Usabilidadeéumtermousadoparadefinirafacilidadecomqueaspessoas
podemutilizarumaferramentaouobjetopararealizaremumatarefa. No
campode Human-ComputerInteractioneUserExperience,usabilidadenor-
malmenteserefereàsimplicidadeefacilidadecomqueumainterface(site,
aplicativo,programadecomputador,gameetc.)podeserutilizada.
Otermoganhoumaisnotoriedadenosúltimosanos,àmedidaquemais
profissionaiseempresasforamsendoenvolvidosnoprocessodecriaç ãode
interfaces.Hojeemdia,ausabilidadejáévistacomoumfatordecisivopara
osucessooufracassodeumprodutodigital.

## Página 86

4.1. Simplicidadenãoésimples CasadoCódigo
4.1 Simplicidade não é simples
PensenainterfacedocontroleremotodasuaTV.Umasériedebotõesagru-
padosemdiversasáreas,cadaumcomumafun çãodiferente. Apesardos
agrupamentosedousodeformatosecoresparadiferenciarosbotõesmais
usados,aindaassimexisteinformaç ãoemexcesso.
Agorapensenamesadedentrodeumasaladeestar.Umcontroleparaa
TV,outroparaoDVDPlayer,outroparaoaparelhodaTVacabo.Epense
queumamesmapessoaprecisasaberusartodosessescontrolespararealizar
tarefassimplescomogravarumprogramaoucomprarumfilmenopay-per-
view.
Chegaraumasoluç ãosimplesdeusabilidadeéumprocessobastante
complicado.Sãonecessáriosvárioseváriosroundsdeexploraçõesdedesign,
alémdediscussõessobrepriorizaç ãodasfun çõesquesãomaisimportantes,
quaispodemsereliminadas,escondidasoudespriorizadas.Avantagemdas
interfacesdigitaiséapossibilidadedeexibireesconderbotõesàmedidaque
ousuárioavançanofluxo.
Simplificaréumprocessotãodifícilerepetitivoquemuitagentedizque
“designnuncaacaba”. Sempreháapossibilidadedeotimizarmaisalguma
área,diminuiracargacognitivasobreousuáriooualterarovisualdosele-
mentosdainterfaceparaqueelespare çammaissimplesdeusar.
GilesColbournetratajustamentedissoemseulivroSimpleandUsable
(http://www.simpleandusable.com). Oautorpropõe4modelosparasolu-
cionaroexcessodeinformaç ãoeconseguirdesenharinterfacesrealmente
simples.
70

## Página 87

CasadoCódigo Capítulo4. Aboaevelhausabilidade
Remova: livre-sedequalquercoisaquenãosejaessencialparaaapli-
cação. Issopodesignificarremoverconteúdo,também,assimcomoalin-
guagemquevocêusanoslabelsdenavegaç ão.
Organize: distribuaoselementosdainterfacedeformaqueelesseen-
caixememgruposlógicos.Issopodesignificartantosebasearnosmodelos
mentaisdequemusa,quantoagrupá-losempadrõesdeinterfacequesejam
maisfamiliares.
Esconda:deixeapenasositensmaisimportantesaoalcance(fazendocom
queelessejamóbvios),eescondaosoutros,deixando-osacessíveisapenaspor
navegação.
Mova: coloquealgumasdasfuncionalidadesemoutrodispositivoou
outrolugar,deformaqueainterfacenãofiqueresponsávelpormostrartodas
asinteraçõespossíveisdeumavezsó.
Naspróximasse ções,vocêconferealgunsprincípioseboaspráticascon-
hecidosquandooassuntoétornarinterfacesdigitaismaisusáveisparaos
consumidores.
71

## Página 88

4.2. Ofereçainformaçõesempequenasdoses CasadoCódigo
4.2 Ofereça informações em pequenas doses
Apesardeseremosanimaismaisinteligentesdoplaneta,ossereshumanos
têmumacapacidadelimitadaemrelaç ãoàquantidadedeinformaç ãoque
conseguem(ouestãodispostos)adigerirquandoestãoocupadosrealizando
umatarefa.Dependendodanaturezadessatarefa,éimportantegarantirque
ainterfacenãoestejabombardeandoousuáriocominformaç ão,paraqueela
consigaserrealizadacomsucesso.
Quantasvezesvocêjánãoacessouoseuinternetbankingeficouvários
segundosaliparado,tentandoentenderondeéquevocêprecisaclicarpara
conseguirvisualizarseuextratobancário? Comopassardotempoecom
oenvolvimentodeprofissionaisdeUXnessetipodeprojeto,essasmesmas
interfacespassaramaserredesenhadasparafacilitaroacessoàinformaç ão
eàsferramentasqueousuárioestáprocurando. Hojeemdia,paracitaro
mesmoexemplo,écomumqueoextratodesuacontajáapare çanaprópria
telainicialdoseuinternetbanking,assimquevocêterminadefazerologin.
Informaçõesqueaspessoasbuscamcomfrequênciasãopriorizadas,semne-
cessidadedemuitoscliquesparasechegaratéelas.
72

## Página 89

CasadoCódigo Capítulo4. Aboaevelhausabilidade
73

## Página 90

4.2. Ofereçainformaçõesempequenasdoses CasadoCódigo
Naverdade,apresentarinformaçõescomsimplicidadeenoexatomo-
mentoemqueousuárioestáprocurandoporelajásetornouquestãopri-
mordialnahoradediferenciaraplicativoseprodutosdesucesso.
Atentaçãodeadicionarlinkseconteúdoemexcessonasinterfacesébas-
tantegrande.Afinal,vocêquerofereceromáximodeop çõesparaousuário
equerqueoseuprodutosejaomaiscompletopossívelparasediferenciarda
concorrência.
Masaregraaquié simplificar,reduzireoferecerinformaçõesemdoses
digeríveis,paraqueaspessoasnãosesintampressionadasatomaremde-
cisõesdemasiadasemváriospontosdiferentesdajornada.
• Qualaaçãoprincipalquevocêquerqueoseuusuáriofaç anessemo-
mento?
• Quaissãoasaçõessecundárias? Dentreelas,quaisvocêpoderiare-
moversemprejudicaratarefaqueousuárioquerrealizarnaquelemo-
mento?
• Qualomínimodeinformaçãoqueousuárioprecisasaberpararealizar
aquelatarefa?Qualamenorquantidadedetextopossível(commenor
númerodecaracteres)paraexplicaraquiloparaele?
• Asimagensquevocêpretendecolocarnainterfaceestãocontribuindo
paraqueousuáriorealizeatarefacommaisfacilidade? Comoessas
imagenspodemserrepensadaspara,alémdocaráterdecorativo,as-
sumiremtambémumpapelinformativoeajudá-lonofluxo?Cuidado
tambémcomexcessodebannerseoutrosboxesquetentamchamara
atençãodousuárioparaalgoquenãoénecessariamenteessencialpara
realizaratarefaqueeledeseja.
• Qualomínimodeelementosdenavegaçãoquevocêprecisaterna
telanaquelemomento? Omenuprecisaficarexpostootempotodo?
Daquelapágina,quaisasoutraspáginasqueousuáriopodequerer
acessar? Umadicaimportantenessepontoéolharparaasmétricase
veremquaislinksosusuáriosestãorealmenteclicando.Considereex-
cluirouesconderoslinksmenosclicadosparadeixarainterfacemais
simples.
74

## Página 91

CasadoCódigo Capítulo4. Aboaevelhausabilidade
4.3 Crie hierarquia na página
Hierarquianadamaisédoqueusardiferentesestilosvisuaisparaoselementos
datelademodoapriorizaroqueémaisimportante.
Atravésdeumaboahierarquia,épossívelguiarosolhosdousuáriopelo
caminhoquevocêdesejaqueelepercorra. Qualaprimeiracoisaquevocê
querqueeleleiaouvejaassimqueentrarnoseusite?
75

## Página 92

4.3. Criehierarquianapágina CasadoCódigo
Figura4.1:Etsy.com:hierarquiaclarausadaparachamaraten çãoparaoslo-
gan.Emumafraseousuárioentendeapropostadosite.
Umdosdesafiosnodesignparainterfacesdigitaisémanterahierarquia
claraàmedidaquenovoselementossãoadicionadosnatela.Vocêjádeveter
passadoporisso:oseuclientepedeparaadicionarmaisdoisoutrêsdestaques
napáginainicialdosite,alémdeumbannereumachamadaparaumapro-
moçãoespecial.Masénessemomentoqueahierarquiadapáginacome çaa
seperder.
Vejaoexemplodahomepagedomsn.com. Alémdefaltadehierarquia
claranotamanhodasfonteseoexcessodeelementosnoheaderdosite,a
adiçãodeumbannernadireitadatelacome çaacriarconflitovisualcoma
mancheteprincipaldahomedosite.
76

## Página 93

CasadoCódigo Capítulo4. Aboaevelhausabilidade
Ouaindaoexemplodomagazineluiza.com: apáginainicialpossui6
grandeschamadasparaousuárioclicar,cadaumacomumtamanhoeestilo
diferentedefonte.Qualdelasémaisimportante?
77

## Página 94

4.3. Criehierarquianapágina CasadoCódigo
Exemploscomoessesãocomunsnahoradedesenharahomepagedeum
site,porexemplo.Seucliente(oumesmootimeinternodolocalondevocê
trabalha)come çaapedirparaadicionarmaisemaischamadasparase ções
diferentesdosite,paraprodutosqueforamlan çadosouparanovidadesque
elesqueiramdivulgarparaosvisitantesdosite.
Aconteceque,quandotudoéimportante,nadaacabasendoimportante.
Éamesmacoisadoquechegarnaprateleiradeumafarmáciaetentares-
colherumshampooparaoseucabelo(principalmentesevocêforhomem).
Sãotantasop çõesquevocêficaparalisado,semsaberexatamentequaldelas
escolher.
Algumasboaspráticasparaconseguirumaboahierarquianaspáginas
são:
• Organizeitenssimilarescomvisualsimilar.
• Eviteinconsistências.Utilizeomesmoestilovisualparaelementosque
têmfunçõesparecidas.Estilosvisuaisinconsistentescausamconfusão
paraousuárioedeixamainterfacepoluída.
78

## Página 95

CasadoCódigo Capítulo4. Aboaevelhausabilidade
• Usecoresparadiferenciarasaçõesprincipais. Useocontrasteaseu
favorparaatrairoolhardousuárioparaaaç ãoquevocêquerqueele
faça.
• Categorize.Agrupelinksportemas,emvezdesimplesmentelistá-los
natela.
• Usetamanhosdefontediferentesparacriarhierarquianapágina,mas
limiteaquantidadedetamanhosdefonteparamanterharmonia.
• Tenhaumbomequilíbriodetextoseimagens.Lembre-seque,depen-
dendodatarefaqueousuárioestárealizando,imagensnemsempresão
bem-vindas.Seeleestánomeiodeumprocessodepagamento,ima-
genspodemacabartirandoofocodaaç ãoprincipalquevocêquerque
elefaça.
79

## Página 96

4.4. Digaaousuáriooquefazeraseguir CasadoCódigo
4.4 Diga ao usuário o que fazer a seguir
Figura4.2:E-commerceTopShopsinalizaclaramentequandoumiteméadi-
cionadoaocarrinhoesugereaousuárioqueprossigaparaocheckout–o
próximopassodofluxodecompra.
80

## Página 97

CasadoCódigo Capítulo4. Aboaevelhausabilidade
Umerrocomumdesiteseaplicativosécriarruassemsaídaparaosusuários.
Tenhacertezadeque,emtodaequalquerteladoseuproduto,estáclaropara
ousuáriooqueeledevefazeraseguir.Quandoousuáriosevêsemop ções,é
comumqueeleabandoneositeoutenhaquevoltarparaapáginainicialpara
tentarencontrarnovamenteoqueeleprocurava.
Umexercíciointeressanteparaotimizarausabilidadedoseuprodutoé
olharparacadaumadastelascomasseguintesperguntasemmente:
• O usuário sabe onde está? A tela comunica com clareza em que
página/site/passodofluxoeleseencontra?
• Ousuáriosabeoquefazeraseguir?Aaçãoprincipalestánítidaosu-
ficiente?
• Obotãoondeeuqueroqueousuáriocliqueestáclaro? Otextodo
botãodáaousuárioalgumadicadoquevemaseguir?
• Seessatelaéumateladeconfirmaçãonofinaldeumfluxo,euestou
aproveitandoparasugerirqueousuáriofaç aalgomais,aumentandoo
tempodenavegaçãoeoníveldeengajamentodelecomoproduto?
Figura4.3:Nomesdebotõesmaisclarosajudamousuárioaentendermelhor
aconsequênciadaação.
Umproblemaclássicodeváriasinterfacesexistenteshojeéatentativade
darop çõesdemaisaousuárioeacabarconfundindo-o. Umacoisaparase
81

## Página 98

4.4. Digaaousuáriooquefazeraseguir CasadoCódigo
teremmentenahoradecriarumdesignéquecadadecisãoquevocêfor ça
ousuárioatomarsignificaalgunssegundosamaisdeesfor çocognitivo.Ele
precisaolharasop çõesdisponíveis,entenderoquecadaumadelasfaz,eentão
decidirqualéaop çãodesejada.
Vejaoexemplodapáginadeprodutosdentrodositepontofrio.com:ela
oferece5op çõesdiferentesaousuáriodoquefazeraseguir.
Quandoousuárioclicaem Comprar(teoricamente,omaiorbotãoda
tela,oquelevaacrerqueéondeeledeveclicar),ositeexibeumamensagemde
errodizendoqueéprecisoselecionarumavoltagemparaomicro-ondasantes
deadicionaraocarrinho.Masnolayoutdapáginao Selecioneficaperdido
nomeiodetantasoutrasinformaçõesemuitodistantedobotão Comprar.
Infelizmente,arelaçãonãoestáclara.
82

## Página 99

CasadoCódigo Capítulo4. Aboaevelhausabilidade
4.5 Dê feedback sobre o estado do sistema
Clarezaéapalavradeordemaqui. Ousuárioprecisaentender,aqualquer
momento,oqueestásepassandocomosistema. Seelepreencheuumfor-
mulárioincorretamente,porexemplo,éprecisoqueainterfacecomunique
issocomclarezaparaele. Inclusivedandoinstruçõesprecisassobrecomo
resolveroproblema.
Figura4.4:Falhacatastrófica.Inclusivenaexperiênciadousuário.
Aregraessencialdequalquerprodutointerativoéquetodaaç ãotemque
terumareaç ão.Eumainterfacequerespondeimediatamenteaoscomandos
dousuáriocontribuibastanteparaumaboaexperiência.
83

## Página 100

4.6. Eviteerrosantesqueaconte çam CasadoCódigo
Figura4.5:Umoutrousuáriocomomesmonomejáexiste.Talvezsejaseu
irmãogêmeodomal.Assustador.
Vocêjádeveterpassadoporessaexperiênciaemalgumsite:terminade
preencherumformulárioenorme,apertaobotão Enviarenada.Nenhuma
resposta. Vocênãosabeaocertoseasuacompraestásendoprocessada,se
vocêprecisaaguardarouseprecisaclicarnovamente. Emmuitoscasos,a
faltadeclarezasobreostatusdosistemafazcomqueosusuárioscliquem
váriasvezesnomesmobotão–podendoacarretarduplicidadesdecadastros
ecompras,gerandomaistrabalhoecustosparaaempresa.
4.6 Evite erros antes que aconteçam
Maisinteressanteaindadoquecomunicarerroscomclarezaquandoeles
aconteceméevitarqueelesaconte çamemprimeirolugar. Errosnormal-
mentesãocausadosporerrosdosusuáriosaointeragiremcomosistema.
Massevocêpararprapensar,oerrodousuárioéculpadainterfacequenão
oguioucorretamentenahoraderealizaratarefa.
ReparenoexemploabaixodoiOS.Quandovocêselecionaumaimagem
noseuaplicativodefotosedecidecompartilhar,osistemaoferecealgumas
opções(mensagem,e-mail,Facebooketc.).Masrepareque,quandovocêse-
lecionamaisdoque5imagens(exemplodadireita),oiOSautomaticamente
ocultaaop çãodecompartilharpore-mail.Issoporqueelesabeque,nogeral,
6imagensanexadasaume-mailotornarãopesadodemaisparaserenviado,
podendoserrecusadoporalgunsprovedores.
84

## Página 101

CasadoCódigo Capítulo4. Aboaevelhausabilidade
Figura4.6:Quandomaisde5fotossãoselecionadas,oiOSocultaaop çãode
compartilharpore-mail,paraqueelenãofiquemuitopesado.
OTwitteréoutroexemplodeprodutoqueprefereevitarqueoserros
aconteçam,emvezdemostrarmensagensdeerroquandojáétardedemais.
Nahoradecomporumtweet,ainterfacedestacaemvermelhooscaracteres
excedentes(acimade140)edesabilitaobotãoparaevitarqueousuárioerre.
85

## Página 102

4.6. Eviteerrosantesqueaconte çam CasadoCódigo
Figura4.7:Oerroécomunicadocomclarezaeobotãoédesabilitadopara
queelesequeraconte ça.
ASiri(aassistentedevozdoiPhone)tambémconhecebemoserros
comunsdossereshumanos. Quandojápassoudameia-noiteevocêpede
paraelaregistrarumlembreteparavocêfazer“amanhã”,elaconfirmasepor
“amanhã”vocêquisdizeraquelemesmodiaouodiaseguinte.
86

## Página 103

CasadoCódigo Capítulo4. Aboaevelhausabilidade
OGmailvaimaislongenahoradeprevenirerros. Quandovocêclica
em Enviar,eleescaneiaotextodoseue-mail. Sevocêescreveupalavras
como“anexado”ou“anexo”enãoadicionounenhumarquivoanexadoàsua
mensagem,elemostraumalertaconfirmandosevocêrealmentenãoquer
enviarumarquivoousefoisomenteumadistraç ãosua.
87

## Página 104

4.7. Simplifiqueformulários CasadoCódigo
Figura4.8: Vocêescreveu‘anexei’namensagemmasnãotemnenhumar-
quivoanexado.Mandarmesmoassim?
Existemváriosmétodosparaprevenirerrosantesqueelesaconte çam.
Umaformainteressantededescobriroserrosmaiscomunsdosseususuários
aointeragiremcomseuprodutoéolharparaasmétricasdosite. Quaiser-
roselesestãocometendocommaisfrequência?Qualainformaç ãoqueeles
inseriramerradoparaqueoerroacontecesse? Porqueelespensaramque
deveriamfazerumaaç ãodiferentedaqueestavasendopedida?Comovocê
podeevitarqueesseerroaconte çacomnovosusuários?
Astaxasdeconversão(eoseucliente)agradecem.
4.7 Simplifique formulários
Qualomínimodeinformaç ãoquevocêprecisacoletardousuárioparaque
elepossaseguiradiantenofluxo?
Pareceumaperguntasimples,masmuitagentedeixaessadiscussãopas-
sarbatidanahoradeelaborarumformuláriodecadastrooudecompra.Uma
práticacomum(masnemsempreideal)éreuniremumúnicoformulárioto-
dososcamposquevocê,comoempresa,desejasabersobreoconsumidor.
Masseráquetodasasinformaçõesqueestãosendopedidassãoextrema-
mentenecessárias?Algumadessasinformaçõespodesercoletadaemummo-
88

## Página 105

CasadoCódigo Capítulo4. Aboaevelhausabilidade
mentofuturo?Estáclaroparaoconsumidorporqueaquelainformaç ãoestá
sendosolicitada?
Umótimoexemplodesimplificaç ãodeformulárioéodecadastrono
AirBNB,umsitedealugueldeimóveisquetemversõesemváriospaíses.
Oformulárioparaconsultarseumimóvelestádisponívelparaaluguel
pedeapenasasinformaç õesextremamenterelevantesparaaquelaaç ão.
Reparequeelesnãopedemparaousuáriosecadastrar,nempedemoen-
dereçodee-mail,nemnenhumaoutrainformaç ãoquenãotenharelaç ãodi-
retacomaquelatarefaqueousuáriopretenderealizar(consultardisponibil-
idadedeumimóvel).
UmoutroexemplointeressanteéodositeNike.com.Nahoradefechar
umacompra,elesdãoaousuárioaop çãode“GuestCheckout”(Comprar
comoconvidado),permitindoqueelesfechemacomprasemanecessidade
decriarumperfildentrodosite.
89

## Página 106

4.7. Simplifiqueformulários CasadoCódigo
“Comoassim,voudeixarapessoafazerumacomprasemsequerpedir
paraelacriarumloginesenha?”
Pareceassustadordopontodevistadaempresa.Maspareummomento
parapensarnoobjetivodousuárionaquelemomento:eleestásuperempol-
gadocomaideiadecomprarumtênisnovo.Pedirparaelecriarumcadastro
Nikenessemomentoseriaumdesvioderotaabsurdamentegrandenaexper-
iênciadousuário.
“Masassimeuestouperdendoaoportunidadedeganharumusuário
cadastrado!”
Seousuárioquercomprarotênis,omelhorasefazerégarantirqueele
consigarealizaressatarefadaformamaissimplespossível.Issovaiassegurar
umavendaamaisnoseue-commerce,quetemimpactodiretonalucrativi-
dadedaempresa.
“Edepoiseupercoesseusuárioparasempre?”
Não. OqueaNikefazéapenaspediroendere çodee-maildousuário,
comopartenaturaldoprocessodecompra. Depoisdealgunsdias,depois
queotênisfoientregueeousuárioestáfelizdavidacomonovoproduto,
elesmandamume-maildefollow-upconvidando-oaterminarocadastro,
criarumasenhaeusufruirdosinúmerosbenefíciosdeterumperfildentrodo
site.Aliás,quandoelesenviamessee-mailpós-compraelesoferecemalgum
90

## Página 107

CasadoCódigo Capítulo4. Aboaevelhausabilidade
tipoderecompensaparaousuário(“termineseucadastroenãopaguefrete
emsuapróximacompra”).Maisumexemplodacombinaçãode usabilidade
compsicologiamencionadanoiníciodolivro:eliminarbarreirasdofluxodo
usuárionahoradacompraedaraeleummotivoparavoltaraositeeterminar
ocadastromaistarde.
Aindanoassunto“formulários”, umaboapráticadeusabilidadeéter
certezadequevocêestáapresentandoomelhortipodecampoparaousuário.
Quandoousuárioprecisaselecionarumadata,porexemplo,émuitomais
fácilemuitomaisfamiliarparaeleapresentarasop çõesemformatodecal-
endário–emvezdemostrarsomenteumcampotextoetorcerparaqueele
digiteadatanoformatoDD/MM/AAAAquevocêprecisa.
Vejaoexemplodositefourseasons.com.Nahoradesolicitaradataem
quepretendesehospedaremumdoshotéis,ositeapresentaaosusuários
umcalendárioondeelepodeselecionaradatadecheck-inedecheck-outde
formamuitomaisvisualdoquesimplesmenteumcampodetexto.
Nosúltimosanos,várioswebsitesdecompanhiasaéreascome çarama
adotaromesmopadrãodeinteraç ãoparapermitirqueosusuáriossele-
cionemasdatasdosvooscommaiscomodidadeecommenoschancesde
erro.
Otópico“usabilidade”ébastanteextensoeháváriosanosmuitocon-
teúdosobreoassuntoépublicado,tantoonlinequantoemlivros. Existem
91

## Página 108

4.7. Simplifiqueformulários CasadoCódigo
diversosprincípiosdeusabilidadelistadosporautoresdiferentesetambém
muitospontosdediscórdiaentreeles.
Maisimportantedoquedecorarumalistaprontaécome çaraprestarmais
atençãoenquantoestiverutilizandoprodutosdigitaisecome çarajulgar,por
contaprópria,oquefuncionaeoquenãofuncionaemmatériadeusabilidade.
Gosta desse assunto?
Sevocêteminteresseemconhecermaissobreusabilidade,acesse http:
//fabricio.nu/usabilidadeparaversugestõesdelivrosmaisavan çados.
92

## Página 109

Capítulo5
Abelezadospequenosdetalhes
Aspessoasnãoexperienciamprodutoseserviçosdeumaúnicavez.Apesar
deoFacebookserumprodutogigante,comumasériedefuncionalidades,
aplicativos,páginaserecursos,nãoédessaformaqueousuáriocomumtem
contatocomaplataforma. OFacebookéaquelamensagemqueumamigo
mandouevocêrespondeuempoucossegundos. Éaquelepassatempode
passearpeloseufeeddenotíciasnoseucelularecurtirumououtropostde
seusamigosenquantoesperaoelevadorchegar.Éumanotificaç ãoquevocê
recebenomeiododia,éumafotoquedecidecompartilharcomsuafamília.
Aocontráriodaspessoasquetrabalhamcomodesenvolvimentoedesign
deprodutosdigitais,osusuáriosfinaiscostumamterumavisãofragmentada
sobreoqueoprodutorealmenteé.Oproduto,paraeles,éumasériedepe-
quenasinteraçõesqueformamumaimpressão(positivaounegativa)como
passardotempo.
Eparaconstruirexperiênciasquesejammemoráveiserelevantesparaas

## Página 110

CasadoCódigo
pessoas,muitasvezeséprecisoestaratentoaessaspequenasinteraçõesede-
talhes.
Os pequenos pontos de contato entre consumidor e marca são tão
importantesparaUXqueem2012DanSafferpublicouumlivro(http://
microinteractions.com)ondedavaumnomeparaessesmomentos: Microin-
terações.
Microinterações
“Microinteraçõessãomomentoscontidosdeumprodutoquegiram
emtornodeumúnicocasodeuso–elestêmapenasumafun çãoprinci-
pal.Cadavezquevocêmudaumaconfiguraç ão,sincronizaseudisposi-
tivo,configuraumalarme,criaumpassword,fazloginemumsite,define
umamensagemdestatus,favoritaou‘curte’algo,vocêestáengajando
comumamicrointeração.Elasestãoemtodolugar:nosdispositivosque
carregamos,noseletrodomésticosdanossacasa,nosaplicativosnonosso
celularecomputador,eatéembutidosnosambientesemquevivemose
trabalhamos.Muitosprodutoseaplicaçõessãoconstruídosinteiramente
emtornodeumaúnicamicrointeraç ão.”
Éotal“slidetounlock”doseuiPhone.Ouopadrãodedesenharasenha
paradesbloquearseusmartphoneAndroid.Obonequinhoquevocêarrasta
paraoGoogleMapsparaativaromodoStreetView.Oclássicobotão“iniciar”
doWindows.
Todosessessãoexemplosdemicrointeraçõesqueforampolidasaoex-
tremo.Ocuidadocomosdetalhescontribuiparaqueaquelepequenoponto
decontatoentreconsumidoremarcasejaúnico,icônico,prazerosoefácilde
usar.
94

## Página 111

CasadoCódigo Capítulo5. Abelezadospequenosdetalhes
Figura5.1:1.SlidetounlockdoiPhone,2.PulltorefreshdoTwitter,3.Ar-
rastaropegmannoGoogleMaps,4.BuywithoneclickdaAmazon,5.Botão
iniciardoWindows,6.PinchaparttoaplicativoClear.
Reparequecadaumdessesmomentoséapenasumpequenorecortede
umafuncionalidademaior. Emvezdeolharparaonúmerodefuncionali-
dadesqueoseuprodutopossui,aregraaquiéolharparaaspequenasinter-
açõesquecompõemtalfun ção.
DanSafferdefineasmicrointeraçõescomo“asmenoresunidadespos-
síveisdaexperiênciadousuário”.Masmenornãoquerdizer“insignificante”.
Naverdade,algumasinteraçõespodemterimpactograndiosoemcomoas
pessoasexperienciamoseuprodutoepercebemsuamarca.
Ofatoéquepoucosdesignersedesenvolvedoresdedicamtemposufi-
cienteparapensarnosdetalhesquefazemumprodutoserúnico–edeixam
passaroportunidadesexcelentesparamelhoraraexperiênciadosusuáriosem
suamanifestaçãomaisgranularecorriqueira.
95

## Página 112

CasadoCódigo
Bomparaosusuários,bomparaaempresa
Háquemdigaqueessetipodedetalheésupérfluo:“omaisimportanteé
fazeroprodutofuncionar,colocaroprodutonarua”,dizemosmaiscéticos.
Massevocêpretendecolocarumnovoprodutonomercado,aspequenas
nuancesdeinteraç ãopodemserumaoportunidadeetantoparacriardifer-
enciaçãoemrelaç ãoaoscompetidores.
Hojeemdia,écomumquenovosprodutossurjam,diariamente,emmer-
cadosquejásãoextremamentecompetitivos.Egrandepartedessesprodutos
queestãocompetindopelaaten çãodosconsumidorespossuemfuncionali-
dadesmuitoparecidasentresi.
Sãotantososprodutosdisponíveisporaíquecumpremamesmafun ção,
queosconsumidoresjáestãocome çandoaoptarporaquelesquesãomais
agradáveisdeusar.Nãoémaissobre“encontrarumaplicativoquemepermita
anotarminhato-dolist”,massim“encontraroaplicativoquefazcomqueessa
tarefasejaagradávelefácildefazer”.
Mas,alémdecriardiferenciaç ãoemmercadoscomparidadedeprodu-
tos,essespequenosdetalhes–quandobemprojetados–podemtrazeroutros
benefíciosparaosusuárioseparaasempresas:
Paraosusuários,interaçõesbemdesenhadassãofáceisdeusaredãoa
sensaçãodequeoprodutoémaiseficiente.Elastambémtornamoprocesso
maisagradável,ajudandoaaumentaroníveldeengajamentodosusuários
comaaplicação.
Paraasempresas,interaçõesbemdesenhadascriamfidelidadeentreos
usuárioseoproduto.Tambémaumentamastaxasdeconversãoaoreduzirem
africçãonofluxodousuário,permitindoqueelescompletematarefacom
maisfacilidade.Alémdisso,éclaro,proporcionamexperiênciasmemoráveis
emelhoramapercep çãoqueosusuáriostêmdasmarcas.Nãoéàtoaquede-
signerscostumampreferirprodutosdaApple,umaempresaqueganhoupop-
ularidadenosúltimosanospeloníveldecuidadoquetemcomospequenos
detalhesdasexperiênciasqueoferecem.
Um estudo realizado por Des Taynor (http://brucejacob.tumblr.com/
post/372896867/the-thickness-of-napkins)mostrouoquantoospequenos
detalhespodemafetarapercep çãoqueaspessoastêmdasexperiênciaspelas
quaiselaspassam,nãoapenasnomundodigital. Nosrestaurantes,porex-
96

## Página 113

CasadoCódigo Capítulo5. Abelezadospequenosdetalhes
emplo,aespessuradosguardanapos temimpactodiretonopre çoqueos
usuáriosestãodispostosapagarpelarefeiç ão.Umdetalhequemuitasvezes
passadespercebidoparaaquelesquesãoresponsáveispor“desenharaexper-
iênciadecomeremumrestaurante”,masqueafetaosubconscientedoscon-
sumidoreseimpactadiretamentenapercep çãoqueelestêmsobreoestab-
elecimento.
Naspróximasse ções,vocêveráalgumasboaspráticaseminterfacesdig-
itaisemqueaaten çãoaospequenosdetalhesfazumagrandediferen çana
experiênciadousuário.
5.1 Evite elementos em excesso
Umatentaçãocomumnahoradedesenharinterfaceséadicionarumnovo
elementonatelaquandovocêprecisaapresentarumanovainformaç ãopara
ousuário.Masseráquenãoépossívelreutilizarumelementoquejáestejalá?
AinterfacedepagamentodoGumroadutilizaummesmoelementopara
passarduasmensagensdiferentes:aminiaturadocartãodecréditonocanto
superiordireitoindicaabandeiradocartão(Visa)quandoousuáriodigitaos
números,mastambémservecomoumindicativodeondeelepodeencontrar
ocódigoverificador(CVC)quandoelepuladeumcampoparaooutrodo
formulário.
97

## Página 114

5.2. Reveleinformaçõesprogressivamente CasadoCódigo
5.2 Revele informações progressiv amente
ONewYorkTimestrazumasoluç ãointeligenteparasimplificarainterface
nocampodecomentáriosdeseusite.Emvezdeexibirlogodecaraoscampos
decadastronecessáriosparadeixarumcomentárioemumartigo,elepreferiu
simplificar.
Primeiro,ousuáriovêapenasumcampoconvidando-oacomentara
notícia.
Sódepoisdeclicaréqueoscamposdecadastrosãoexpostos.
98

## Página 115

CasadoCódigo Capítulo5. Abelezadospequenosdetalhes
Umamedidasimples,masqueevitaqueatelafiquemuitopoluídacom
elementosquenãosãoestritamentenecessáriosemumprimeiromomento.
5.3 Seja cuidadoso com o tempo do usuário
VejaoexemplodoFlickrnahoraemqueosusuáriosestãosubindoumasérie
defotosparapublicarnosite.
Comooprocessodeuploaddefotospodeserdemorado(dependendodo
númerodeimagensqueousuárioquerenviaredependendodaqualidadede
suaconexão),oFlickrresolveuevitarqueousuáriofiqueparadoesperando
ouploadserconcluído.
99

## Página 116

5.3. Sejacuidadosocomotempodousuário CasadoCódigo
Figura5.2:Flickrsinalizanaprópriaabadonavegadoraporcentagemdeup-
loaddasphotosdousuário.
Emvezdisso,eleutilizaoprópriotítulodaabacomoumindicadorde
progresso.Assim,ousuárioficalivreparapassearporoutrasabasdonaveg-
adorenquantooFlickrfazotrabalhopesadodesubirasfotosparaosite.
UmoutroexemploéodaBlizzard,duranteoprocessodeinstalaç ãode
jogospesadoscomoWorldofWarcraftouDiablo.Comootamanhodosar-
quivospodetotalizar5GBoumais,oprocessocompletodeinstalaç ãopode
levarlongosminutos.MasparecequeaBlizzardconhecebemoseupúblico-
alvoeocontextodeuso:gamersavan çadosqueacabaramdecomprarojogo
eestãoquasetendouminfarto,tamanhaaansiedadeparacome çarajogar.
Asoluçãoétrabalhosa.Primeiro,umasoluç ãotécnica:garantirqueosis-
100

## Página 117

CasadoCódigo Capítulo5. Abelezadospequenosdetalhes
temacomeceainstalaç ãopelosarquivosquesãoindispensáveisparaojogo
funcionar,edeixarosarquivos“supérfluos”(comoanimaçõeseminifilmes)
paraofinal. Depois,umasoluç ãodeUX:sinalizarcomcoresdiferentesa
evoluçãodabarradeprogresso. Apartirdomomentoemqueabarrade
instalaçãoficaamarela(segundaimagem),issosignificaqueojogojáestá
disponívelparaseriniciado,mesmoqueaindanãocontenhatodasasani-
maçõesefilmesdentrodele. Reparetambémque,nessemomento,obotão
de“Play”nocantodireitopassaaficarhabilitado,permitindoqueousuário
comeceajogarotãodesejadojogo.
Otempodousuárioéalgopreciosoparaele.Produtosqueentendemessa
importânciaconseguemutilizarissoafavordaexperiênciadousuário.
5.4 Crie experiências personalizadas
Àmedidaqueosusuárioscome çamainteragircomoproduto,umasériede
informaçõespodesercoletadasobreele,mesmoqueinvisivelmente.Ealgu-
masempresasjáperceberamquepodemusaressasinformaçõesparafazer
comqueaexperiênciadousuáriosejapercebidacomomaispersonalizada.
Vejaalgunsexemplossimples:
AinterfacedocaixaeletrônicodobancoWellsFargo“aprende”comopas-
sardotempoqualatransaç ãofinanceiraqueousuáriorealizacommaisfre-
quência.Napróximavezqueeleforatéumcaixaeletrônico,aquelatransaç ão
101

## Página 118

5.5. Adivinheaintençãodousuário CasadoCódigo
comum(sacar80dólares,nomeucaso)édestacadaemsuatelainicial.Uma
espéciede“atalho”paraatransaçãomaisfrequente. Seeufosseanotarna
pontadolápisquantotempoequantos“cliques”eujáeconomizeicomisso,
dariaparaescreverumlivro.
JáoEbay,comoédeseesperar,controlatodasascomprasquevocêjáfez
nosite.Quandovocêestávendoapáginadeumprodutoquevocêjátenha
compradoanteriormente,onomedobotãocomprarmudade“ Buy”para“
Buy Another”.
Éumdetalhesimples,masqueevitaqueusuáriosmaisdistraídoscom-
premduasvezesomesmoprodutosemquerer.Eparausuáriosquenãoes-
tavamdistraídosequerealmentequeremcompraromesmoprodutopela
segundavez,essapequenamudan çanonomedobotãooajudaatercerteza
dequeeleestárealmentecomprandooprodutoquejáutilizou.
5.5 Adivinhe a intenção do usuário
Asaçõesdousuáriogeralmentetêmumainten çãoportrás.Talvezainten ção
nãosejaexplícita,ouconsciente,mas,apartirdomomentoemqueoUX
designercome çaapesquisareentenderosmotivosportrásdaquelaaç ão,é
possívelbolarsoluçõescriativasparafacilitaravidadousuário.
VejaoexemplodoaplicativodebookmarksPocket. Aprincipalfun ção
102

## Página 119

CasadoCódigo Capítulo5. Abelezadospequenosdetalhes
doaplicativoésalvarlinksparaseremlidosmaistarde. Oqueelesfazemé
anteciparqualainten çãodousuário: quandoeleabreoaplicativoeexiste
umlinkcopiadoemsuaáreadetransferência,oaplicativoexibeumabarra
oferecendoparasalvarolink.Maisumavez:umatalho,paraevitarcliques
desnecessáriosdousuário.Seesseatalhonãoestivesseali,ousuárioteriaque
clicarem“SalvarNovoLink”,depoiscolarolinkqueestavacopiado,edepois
confirmar.Comesseatalho,ousuáriorealizaamesmatarefacomumúnico
clique.
Figura5.3:OaplicativoPocketexibeumatalhonaparteinferiordatelacaso
ousuáriotenhaumlinkcopiadoemsuaáreadetransferência.
OGoogleChromefazalgoparecido.Quandoelepercebequeousuário
vaiatéasconfiguraçõesdonavegadoreescolhedeletarohistóricodenaveg-
acãoduasvezesoumaisemumcurtointervalodetempo,elepassaaexibir
103

## Página 120

5.5. Adivinheaintençãodousuário CasadoCódigo
umapequenamensagemnapartedecimadainterface.
Figura5.4:“Psiu.Omodoincógnito(Ctrl+Shift+N)podeserútilnapróxima
vez.
Alémdepouparousuáriodotrabalhodeficardeletandoohistóricode
navegaçãotodavezqueelequerevitardeixarrastros,oChromeaproveitapara
ensinarousuáriosobreumadasfun çõesdonavegador.Équasecomoseele
tentassepreverqualainten çãodousuárionomomentoemqueeleinterage
comoproduto.
Umoutroexemplodessemesmoprincípiodeusabilidadeéodevários
playersdemúsicadisponíveisnomercado(iTunes,Spotify,entreoutros).
104

## Página 121

CasadoCódigo Capítulo5. Abelezadospequenosdetalhes
Quandovocêclicanobotão“Voltar”ou“Rewind”,existemduasal-
ternativasquepodemacontecer,semquevocêsequerperceba:
• Seamúsicaacaboudecomeçar,obotãoRewindvoltaparaamúsica
queestavatocandoantesdessa.
• Sejásepassaramalgunssegundos,omesmobotãoRewindvoltapara
osegundo0:00damúsicaqueestátocandoatualmente.
Porqueelesfazemisso?Porquequandovocêestáouvindoumamúsica,
gostamuitodelaequerouvi-lanovamente,nemsemprevocêconsegueaper-
tarobotãoRewindrápidoosuficiente,antesdeamúsicaterminar.Entãoo
aplicativolhedáalgunssegundos“defolga”.Mesmoqueapróximamúsicajá
tenhacome çado,vocêaindatemquatrooucincosegundosdedescontopara
apertarRewindevoltarparasuamúsicafavorita.
Ah,abelezadospequenosdetalhes.
5.6 Faça o trabalho pesado
ReparenoexemploaseguirdoGooglePlus.Comotodaredesocial,éobvia-
menteimportanteparaelesquevocêmantenhaoseuperfilomaiscompleto
possível.
Mas,emvezdeperguntarondevocêtrabalhacomumcampodetexto
aberto,fazendocomquevocêtenhaquedigitaronomedaempresa,elesbo-
laramumasoluç ãomaissimples. Elesvarremosperfisdosseusamigosna
redesocialeprocuramolocaldetrabalhodetodoseles.Aoobservaremque
umagrandeparceladosseusamigostrabalhanaempresaX,elesjálheofer-
ecemessaop çãodeempresaprontamentenahoraemquevocêfazloginno
105

## Página 122

5.7. Sejahonestocomseuspedidos CasadoCódigo
site.Tudooquevocêprecisafazeréclicarem“Sim”–eentãoelesatualizam
aquelainformaçãonoseuperfil.
Figura5.5:OGooglePlusfazotrabalhopesadoparaqueousuáriosóprecise
clicarumavezparaconfirmar.(viaLittleBigDetails)
5.7 Seja honesto com seus pedidos
Pedirparaousuáriofornecerinformaçõespessoaiséummomentodelicado
daexperiênciadousuário.Muitasvezeselenãovêobenefícioexplícitoem
forneceraquelainformaç ão–eacabaachandooformuláriotrabalhosode-
maisparaserpreenchido.
Masvejaoexemplodosserviçosdee-mailMailchimpnahoradepedir
paraousuáriocadastrarasinformaçõessobreoseusite.
106

## Página 123

CasadoCódigo Capítulo5. Abelezadospequenosdetalhes
Paracadainformaçãoqueelespedemaousuário,existeumabreveexpli-
caçãosobrecomoaqueledadoseráusado. Éumaformadiretaerápidade
fazercomqueatrocafiquemaisjusta:ousuárioficasabendonahoracomoé
queaquelainformaçãoseráusadapelaempresa,evêqualobenefícioqueele
recebeemtroca.
5.8 Expresse a personalidade da sua marca
Nosdiasdehoje,consumidoressãoexpostoscommuitomaisfrequênciaàs
interfacescriadasporumamarcadoquepelosesfor çosdecomunicaçãoquea
marcafazatravésdepropaganda,relaçõespúblicasoueventos,porexemplo.
PenseemquantasvezesvocêtiraoseuiPhoneouAndroiddobolsoe
utilizasuainterface;provavelmenteumnúmeroinfinitamentemaiordoque
onúmerodevezesquevocêviuumcomercialdealgumadasmarcasque
criaramessessistemasoperacionais.
107

## Página 124

5.8. Expresseapersonalidadedasuamarca CasadoCódigo
Figura5.6:CasovocêbusquealgonaGooglePlayStoresemdigitarnadano
campo,osistemabuscaautomaticamentepelotermo‘Unicórnio’.
Ospequenosdetalhesdasinterfacespodemdizermuitosobreaperson-
alidadedeumamarca. Quandovocêdigitaumpasswordincorretonoseu
MacOSounoseuiOS,ajanelasacodedeumladoparaoutro,comosefosse
umapessoabalan çandoacabe çanegativamente. Nãoháanecessidadede
umamensagemdeerroformaldizendoque“vocêdigitouoseupasswordin-
corretamente”.Afinal,issosoariamuitomaisfriodoqueadivertidaanimação
criadapelosdesignersdaApple.
Algumasmarcaspreferemsermaisexplícitasnahoradeexpressarsua
personalidade,usandooprópriotextodainterfaceparaintroduzirmomentos
dedescontraçãonaexperiência.
108

## Página 125

CasadoCódigo Capítulo5. Abelezadospequenosdetalhes
Figura5.7:Vocêsabeondevocêestá?VocêestánaSELVA,Ben.
UmdospapéisdoUXdesignerquandoestádesenhandointeraçõeséo
deidentificaroportunidadesdeprestaraten çãoaosdetalhes.Quemtrabalha
diretamentecomtestesdeusabilidadesabeoquãogratificanteéverareaç ão
dosusuáriosaumdetalhequevocêpensoucomcuidadonahoradecolocar
nainterface.
Nofimdascontas,éasomadessespequenosmomentosdesurpresae
deboausabilidadequefazcomqueaspessoasseapaixonempelosprodutos
queusamesetornemfiéisaumamarca. Evocê,comoUXdesigner,tema
possibilidadedemelhoraravidadaspessoas,umainteraç ãodecadavez.
Gosta desse assunto?
Sevocêteminteresseemaprendermaissobreostemasdestecapítulo,
acessehttp://fabricio.nu/detalhesparavermaisreferências.
109

## Página 127

Capítulo6
Aimportânciadosmicrotextos
Háalgunsanos,falava-semuitosobreofatodequeusuáriosnãoleemna
web.Masconvenhamos,issoeraemumaépocaemquegrandepartedasin-
terfacesdigitais(majoritariamente“sites”)utilizavamgrandesblocosdetexto
paracomunicarmensagensaosusuários.Talvezumaheran çadasrevistasim-
pressas,cartilhasoumanuaisdeinstruç ão,ondesepartedopressupostode
queousuárioestádispostoalertextosemprofundidade.
Anosdepois:mobile.Umamudan çadeparadigmaqueafetounãoapenas
aformacomoossistemassãodesenhados,mastambémamaneiracomoos
usuáriossecomportamaointeragiremcomeles.
Dopontodevistadosistema:interfacesextremamentepequenas,com
espaçolimitadoparatextoeumtipodeinteraç ãomuitomaiscurta,breve,
empequenasdoses.
Do ponto de vista do usuário: uso muito mais fragmen-
tado de tecnologia no decorrer do dia (150 vezes, em média,

## Página 128

CasadoCódigo
de acordo com o site http://tech.firstpost.com/news-analysis/
smartphone-users-check-their-phones-an-average-of-150-times-a-day-86984.
html),ohábitodomultitaskingeumníveldeconcentraç ãomuitodiminuído
sobreoqueestásendofeito.
Tendoissoemvista,énaturalqueaspessoasestejammuitomenosdis-
postasa“ler”interfaces.
Daísurgeotermo“microtexto”(“microcopy”eminglês). Naprática: a
artedeconseguirtransmitirumamensagemempequenosfragmentos,num
espaçolimitadodetexto,comconcisão,clarezaepersonalidade. Podeser
onomedeumbotão,umamensagemdeerroousucesso,umalinhadein-
struçãoexibidaacimadeumformulário,um tooltipdeajuda–qualquertexto
deinterface.
Umbomexemploparacome çar?
Figura6.1:Olinkde‘Like’doFacebook:microtextodocomeçoaofim.
O“Curtir”doFacebook.Reparecomoaaçãoinicialédescritasomente
emtexto.Quandoousuárioclica,ofeedbackétransmitidotambémsomente
emtexto(“Like”vira“Unlike”).
Eparadesfazeraaç ão?Somentetexto,denovo.
Éinteressanteobservarousodemicrotextosobdoisaspectos:ummais
funcionaleoutromaisemocional.
Oaspecto funcionaléofatodeexistirumaaç ãosimplesnaqualtodos
osestadossãotransmitidoscomclarezaaousuário.Semerro.Semruídoou
ambiguidade.
112

## Página 129

CasadoCódigo Capítulo6. Aimportânciadosmicrotextos
Jáoaspectoemocionaléumpoucomaisabstrato,naturalmente.Aaç ão
escolhidapeloFacebookfoi“Curtir”,poralgummotivo.Éoverboquemais
combinacomapersonalidadelevianadaredesocial.Imaginesefosse“Legal”.
Imaginesefosse“LOL”ou“Adorar”. TalvezvocêachasseoFacebookmuito
maispegajosodoquejáacha.Paracadapaísemqueoprodutoétraduzido,
oFacebookescolheoverboquefuncionamelhorculturalmentedentreoseu
público-alvo.
Figura6.2: JáoserviçodebloggingSvbtlepreferiuchamaroseubotãode
‘Kudos’;maisalinhadocomsuapersonalidade.
Omicrotextoajudanãoapenasousuárioaentenderoqueestáaconte-
cendonosistema,mastambémaformaremsuacabe çaapercep çãoqueele
temdaqueleproduto/marca.
6.1 O v alor funcional dos microtextos
Alémdeexplicarumaaç ão(“cadastrar”),ummicrotextopodeserusadopara
orientarousuárionarealizaç ãodeumatarefa(“suasenhadeveconterno
mínimo6caracteres”)oudarfeedbacksobreumaaçãoqueelerealizou(“sua
contafoicriadacomsucesso”).
Tambémépossívelusarmicrotextosparaanteciparnecessidades,anseios
oupreocupaçõesqueousuárioteráaorealizardeterminadatarefa. Veja
oexemploaseguir,citadonoartigodeJoshuaPorter(http://bokardo.com/
archives/writing-microcopy).
113

## Página 130

6.1. Ovalorfuncionaldosmicrotextos CasadoCódigo
Napáginadecompradolivro,oautoradicionouumalinhadetextoque
écrucialparaquemestáconsiderandoefetuaracompra:“astransaçõesuti-
lizamPayPal,masvocênãoprecisaterumacontaparacompraresselivro”.
Issoantecipaumadasprincipaispreocupaçõesquepassampelacabe ça
daspessoasquandoelasveemologotipodoPayPal(“ih,eunãotenhouma
contalá”)eevitaqueelasabandonemofluxoporcausadisso.
114

## Página 131

CasadoCódigo Capítulo6. Aimportânciadosmicrotextos
Figura6.3: Exemplodeantecipaç ãonoformuláriodecriaç ãodeumnovo
Tumblr.
Emseulivromaisrecente(http://microinteractions.com), DanSaffer
abordaoassunto“Microcopy”edáalgumasdicasúteisnahoradeescrever
essetipodetexto:
• Evitenomesdeaçõesmuitovagos,como“Enviar”.Oqueacontecede-
poisqueousuário“Envia”osdadosdoformulário?Seráqueonome
dobotãonãopodeexplicarissoparaousuário?
• Otextodeinstruçãoéabsolutamentenecessário?Vocênãoprecisaadi-
cionarum“Porfavor,façalogin”acimadeumformuláriodelogin,por
exemplo.
• Quandootextoémuitolongoeprecisasertruncadonainterface,tenha
certezadequeousuárioconseguelerotextocompletofacilmente.
• Testeseustextoscomusuáriosreais.Mostreumainteraçãocommicro-
textoparaelesepe çaparaelesdizerememvozaltaoqueachamque
aconteceráaoclicaremouinteragirem.
• Uselinguagemhumana,nãodesistema.“Postadohá3horas”émuito
115

## Página 132

6.2. Ovaloremocionaldosmicrotextos CasadoCódigo
maisfácildeentenderdoque“postadoem04/03/2014às14h33”–um
detalhequeacabapassandobatidoemmuitosprodutosporaí.
6.2 O v alor emocional dos microtextos
Essesdiaspreenchiminhadeclaraç ãodeimpostoderendaaquidosEUAus-
andoaferramentaTurboTax. Foiumaexperiênciatãosimplesetãocuida-
dosamentepensada,quequandotermineieuqueriasaircontandoparatodos
osmeusamigosUXerscomotinhasido.Eles,obviamente,jáestavamacos-
tumadoscomoproduto.
Preencheradeclaraç ãodeimpostoderendanãoéumatarefabreve(são
muitosemuitospassos),masointeressantedaexperiênciadoTurboTaxé
comoelesusammicrotextosparaencorajarosusuáriosaseguirememfrente.
Eles“celebram”cadapequenaconquistasuaàmedidaquevocêvaipercor-
rendocadaumdosmaisde50passosdoformulário.Oresultado?Durante
oprocesso,fiqueimuitomaistranquilodoqueacheiqueficariaantesde
começar.
Figura6.4:MicrotextonoTurboTax.comdepoisquevocêenviaadeclaraç ão:
impostoderendasemcomplicaç ão.
Emmuitosprodutos,omicrotextorepresentatambémumaótimaopor-
116

## Página 133

CasadoCódigo Capítulo6. Aimportânciadosmicrotextos
tunidadeparaexpressarapersonalidadedamarca. Apesardalimitaç ãode
pixelsecaracteresdosmicrotextos,aescolhacertadaspalavraspodeajudara
transmitiralgunsdosvaloresdamarcaparaseususuários(comooexemplo
doFacebook“Like”citadoanteriormente).
OMailchimp.com,porexemplo,usacadaoportunidadequetemparaex-
pressarsuapersonalidade. Elesinclusivepublicaramumguiasobretomde
voz(http://voiceandtone.com)paraquemcostumaredigire-mailmarketing.
6.3 Comunique benefícios, não funcionali-
dades
Sevocêexplicaparaaspessoasoporquêdevocêestarpedindoparaelasfaz-
eremalgo,émuitomaisprovávelqueelasaceitemsuasugestão.Éumpequeno
truquedetextomasquepodetergrandeimpactonosentidodeencorajaras
pessoasatomaremalgumaaç ão.
Emredação,hásempredoiselementoscomuns:funcionalidadesebene-
fícios.Oprimeiroésobreoqueumprodutofaz.Osegundoésobreoqueele
permitevocêfazer.
Reparenoexemplodapáginainicialdoairbnb.com.Emvezdefalar“so-
117

## Página 134

6.4. Falealinguagemdosseususuários CasadoCódigo
mosamaiorrededealuguéisdeimóveisdomundo”ou“alugueldeimóveis
semcomplicação”,aprimeirafrasequeousuáriovêaochegarnositeé“en-
contreumlugarparaficar”.
Éumadiferen çasutil,masmudarofocodeoqueoprodutofazparao
queoprodutovaipermitirqueoconsumidorfaç aémaisumaformasimples
decolocaroconsumidornocentroefacilitaroentendimentodaproposiç ão
devalordositeemquestão.
6.4 Fale a linguagem dos seus usuários
Aspessoasrespondembemapalavras,frasesetonsdevozdependendoda
própriapersonalidadedelas,enãoporquevocêescolheuapalavracertaou
errada.
Énessahoraquecriardocumentosdepersonaspodeserútilparaoseu
projeto.Aspersonassãoumaespéciede“retrato”dequeméopúblico-alvodo
seuproduto.Conhecerbemoperfildousuárioajudaamarcaasecomunicar
deumaformaquesoenaturalelógicaparaeles.
Vocênãodizparaumacrian ça“essaafirmaçãoéilógicae,portanto,in-
válida”.Amensagemquevocêquerpassarpodeatéseressa,masotomdevoz
usadodevesercompletamentediferenteparaqueelaentenda.Vocêdiz“não
éassimquefunciona,deixaeuteexplicar”.Umjeitomuitomaishumanode
trataracomunicaçãocomseuusuário.
VejaoexemplodositedaJohnson’sBaby.Nomenu,alinguagemescol-
hida(eatéascores,quetambémcontribuempararefor çaravozdamarca)
fazpartedouniversodasmãesqueestãonavegandonosite.
118

## Página 135

CasadoCódigo Capítulo6. Aimportânciadosmicrotextos
Jáoemotion.me,siteespecializadoemajudarnoivosaplanejaremocasa-
mento,usaexpressõescomo“OGrandeDia”nahoradeapresentaromenu
paraousuário.
Nofimdascontas,adequarsualinguagemparaouniversodoseupúblico-
alvoajudaacriarumaexperiênciadousuárioquesejaaomesmotempomem-
orávelefácildeentender.
6.5 Mantenha os textos curtos
Ofocoaquiéo“micro”dos“microtextos": mantenhaseustextoscurtos.
Clientescostumamsemprepedirmaispalavrasemumapágina.Masotexto
semprepodesermaiscurto.Enamaioriadoscasos,textosmaiscurtosgeram
melhoresresultados.Semprequepossível,reduza.
119

## Página 136

6.5. Mantenhaostextoscurtos CasadoCódigo
Figura6.5:Passwordé‘sEnSíVeL’amaiúsculaseminúsculas.
Textoéumape çafundamentaldaexperiênciadousuário,àsvezesnegli-
genciadaporprofissionaisdeUXdepoisqueowireframefoientregue.
Acompanharodesenvolvimentodostextosqueserãoexibidosnainter-
faceéimportantenãosóparagarantirboausabilidade,mastambémpara
tercertezaquetextoeimagemestãotrabalhandojuntosparatransmitiruma
mensagemalinhadacomotomdevozdamarca.
120

## Página 137

Capítulo7
Construindoumabibliotecade
padrões
Bibliotecasdepadrões,nouniversodeUserExperienceDesign,sãogalerias
quecontêmosprincipaiselementosinterativosquecompõemainterfacede
determinadoproduto–sejaeleumsite,umaplicativoouqualqueroutropro-
dutodigital.

## Página 138

CasadoCódigo
Acriaçãodebibliotecasdepadrõeséumaformadecolecionarassoluções
dedesignqueaparecemváriasvezesdentrodeummesmosite.Cadasoluç ão
écriadapararesolverumproblemadedesign.Asgaleriasdefotos,porexem-
plo,sãoumasoluç ãoparaexibirepermitirqueousuárionavegueporuma
sériedeimagensquefazempartedeummesmotema.
Comoosproblemasdedesigncostumamaparecermaisdeumavezden-
trodomesmoproduto,fazsentidoqueodesignereodesenvolvedor reuti-
lizemassolu ções emvezdereinventaremarodacadavezqueoproblema
aparecernovamente.
ObomUXdesignertiraproveitodisso. Nãoéprecisodesenharnova-
menteumfluxode“enviarpore-mail”oude“cadastro”acadaprojetoem
122

## Página 139

CasadoCódigo Capítulo7. Construindoumabibliotecadepadrões
cujamatrizdeescopoessesitensaparecem.Apartirdomomentoemquevocê
temumabibliotecadepadrõesàsuadisposiç ão,passaapoderreaproveitar
esseselementosefluxoscomomínimodeajustesemoutrostrabalhos.Isso
tambémdáumagrandeagilidadenaexecuç ãodoprojeto.
Elementosencontradoscomumenteembibliotecasdepadrõessão:
• Texto
• Estruturadapágina
• Tabelas
• Slideshows
• Elementosdenavegação
• Botõesderedessociais
• Ferramentadebusca
• Listagemdeartigos
• Galeriadefotos
• Módulodelinksrelacionados
• Carrosséis
• Botõesdeaçãoprimáriaesecundária
123

## Página 140

7.1. Asvantagensemterumabiblioteca CasadoCódigo
Figura7.1: Exemplodeumcarrossel,elementofrequentementeencontrado
embibliotecasdepadrões.
7.1 As v antagens em ter uma biblioteca
Consistêncianaexperiênciadousuário
Projetosmuitograndescostumamserdesenhadosedesenvolvidosporuma
porçãodeprofissionaisdiferentes. Algumasvezes,umtimeéresponsável
pordesenharahomepage,enquantooutrotimeestáfocadonaferramentade
busca,porexemplo.Muitasvezes,essasdiferentesfrentesestãotrabalhando
emparalelo.Masparaousuárioéumacoisasó:eleprecisasentirquetantoa
homepagequantoaferramentadebuscafazempartedomesmoproduto.
Quandoaexperiênciaéconsistenteeoselementosinterativossecom-
portamdemaneirasimilar,ousuáriopassaasaberoqueesperardosistemaa
cadanovaaç ãoqueeletoma.Quandonãoháconsistência,ousuárioprecisa
“reaprender”comointeragircomositeacadanovotipodeinteraçãoqueé
introduzidonaexperiência. Eisso,éclaro,contribuinegativamenteparaa
satisfaçãodousuário,paraausabilidadedosistemaeparaosresultadosde
negóciosdaempresaquecriouoproduto.
124

## Página 141

CasadoCódigo Capítulo7. Construindoumabibliotecadepadrões
Reutilizaçãodoselementospelotime
Cadavezqueumdesignercriaumnovopadrãodeinteraç ão,issogeraum
novocustoparaaempresaqueestádesenvolvendooproduto.Afinal,odire-
tordearteprecisatrabalharnolayoutdessenovoelemento,osprogramadores
front-endprecisamfazê-lofuncionaretc.Porisso,reutilizarpadrõesdeinter-
açãopodeserumjeitointeligentedereduzircustosnoprojeto,garantiruma
datadeentregaplausíveleevitarqueostimesgastemhorasafiorecriando
soluçõesquejáexistem.
Éimportante,porém,queabibliotecaestejafacilmenteacessívelaqual-
querprofissionaldotime,quetodossaibamdesuaexistênciaequesejam
encorajadosausaroselementosalipresentessemprequepossível.
Manutenção
Terumabibliotecadepadrõesdeinteraç ãoqueéutilizadaportodosos
designersedesenvolvedorestambémfazcomqueamanuten çãosejamais
simples. Quandooselementossãoprogramadosdamesmaforma,muitos
blocosdecódigopodemserreutilizados,reduzindoacargadetrabalhodos
programadores.
Épossíveltambémmensuraraeficáciadoselementosdabibliotecade
padrõesetrabalharemcimadelesparaquesuaperformancesejaotimizada.
Seumdeterminadomodelodegaleriadefotosestáperformandoabaixodo
esperado(osusuáriosnãoestãoclicandonasimagensseguintesparaexplo-
raragaleria),épossívelrefiná-loeotimizaroseufuncionamentoumavezsó,
dentrodabibliotecadepadrões.Apartirdomomentoemqueasmelhoriasde
designecódigosãofeitasnagaleriadefotospadrão,comumasimplesatual-
izaçãodecódigotodasasgaleriasdefotoqueaparecemnositetodotambém
sãoatualizadasparaanovaversão.
Paraisso,éimportantequeosdesenvolvedorestrabalhemcomoconceito
deelementosglobaisnocódigodoproduto:emvezdeinserirmanualmente
ocódigodagaleriadefotosemtodasaspáginasemqueumadelasaparece,
émuitomaisfácilterum includequeestásendoalimentadoporummodelo
globaldegaleria.
Élógicoqueasbibliotecasdepadrõescome çamafazermaissentidopara
projetosmaioresoutimesemquedesignersedesenvolvedoresestejamtra-
125

## Página 142

7.2. Abibliotecacomoentregávelfinaldoprojeto CasadoCódigo
balhandoemparaleloemdiferentespartesdainterface.Sevocêestácriando
umsitededuasoutrêspáginas,podeserquenãovalhaapenaotrabalhode
criar,poliremanterumagaleriadepadrõesseparadamente.
Outrocasocomuméodeempresasquepossuemdiversosprodutospara
oconsumidorfinal.VejaocasodoGoogle:muitoselementosdenavegaç ão
(comopaginação,botãode+1,galeriasdeimagensetc.)sãocompletamente
aproveitadosemprodutosdiferentes,comooGmail,GooglePlus,Google
Maps.Alémdetornaraexperiênciadousuáriomaisconsistenteeotimizar
ausabilidadedosprodutos,essapadronizaç ãotambémpermitequediversos
produtospare çamfazerpartedeumamesmafamília–contribuindoassim
paraapercep çãoqueousuáriotemdamarca.
Confiradoisexemplosdebibliotecasdepadrõesdegrandesmarcas,pub-
licadosonlineparaquemquiserconsultar.
Starbucks:http://www.starbucks.com/static/reference/styleguide/
Yahoo!:https://developer.yahoo.com/ypatterns/
7.2 A biblioteca como entregável final do pro-
jeto
Ummovimentorecentedasempresasquetrabalhamcomprojetosdegrande
porteéodeconsiderarabibliotecadepadrõesoentregávelfinaldedetermi-
nadoprojeto.
Penseemumsitequepossuimaisde50modelosdepáginasdiferentes;se-
riainsanoestruturar,layoutaredesenvolvertodasaspáginasseparadamente
etê-lascomooentregávelfinaldoprojeto.OquemuitosUXdesignersfazem
édesconstruiroselementosquecompõemessas50páginasecategorizá-los
dentrodeumabibliotecadepadrões–especialmentequandoaspáginaspos-
suemmuitoselementoscompartilhados.
Brad Frost, programador front-end que passou anos trabalhando em
agênciasdigitaisnosEUA,recentementeintroduziuparaacomunidadede
UXdesignersedesenvolvedoresoconceitode“DesignAtômico”. Eleparte
damesmapremissaquedeuorigemàsbibliotecasdepadrõesmuitosanos
atrás: ofatodeque,sevocêdesconstruiraspáginasdeumsite,épossível
126

## Página 143

CasadoCódigo Capítulo7. Construindoumabibliotecadepadrões
chegarnasmenoresunidadesdedesignpossíveis:os“átomos”dodesignde
interação.
Figura7.2:Modelo-metáforadeBradFrostconsideraátomos,moléculas,or-
ganismos,templatesepáginasnodesignweb.
SegundooesquemapropostoporBradFrost,épossívelfocarosesfor ços
dosdesignersedesenvolvedoresemconstruirosátomos,moléculaseorgan-
ismosquecompõemoproduto,emvezdefocarnaspáginascompletas.No
finaldoprojeto,emvezdeentregaras50páginas,oqueelepropõeéaen-
tregadeumúnicolink(emHTML,nocasodeumsite),queilustracomo
esseselementosdeinteraç ãosecomportam.
Apartirdaí,ficamaisfácilparaaempresamontaraspáginasemquestão:
bastaqueelareúnaessesdiversoselementosdeumjeitoquefaç asentidopara
osusuários(primeirooheader,depoisocampodebusca,depoisotítuloda
página,depoisumblocodetexto,depoisumagaleriadefotosetc.).
127

## Página 144

7.3. Maispadronizaçãonãosignificamenoscriatividade CasadoCódigo
Gosta desse assunto?
Sevocêseinteressapelotema,leiaadocumentaç ãoqueFrostpub-
licouemseusiteevejaalgunsexemplosdeprodutosqueforamcon-
struídosinteiramenteutilizandooconceitododesignatômico: http:
//bradfrostweb.com/blog/post/atomic-web-design.
7.3 Mais padronização não significa menos
criatividade
Hojeemdia,existemdiversasbibliotecasdepadrõesdisponíveisonlinepara
consulta.SitescomooPatternTap(http://patterntap.com)catalogampadrões
deinteraçãodediferentesaplicativos,siteseprodutosemumúnicolugar,per-
mitindoinclusivequeovisitantefiltreospadrõesportipo(menus,galerias,
paginação,formuláriosetc.).
Mas,apesardasinúmerasvantagensemseutilizarbibliotecasdepadrões
edafacilidadeemencontrarreferênciasnawebdepadrõesquefuncionam
bem,éimportanteestaratentoaumerrocomumdealgunstimes:pensarque
umaúnicasoluçãodedesignpoderesolverproblemasdedesigndiferentesde
empresasdiferentes.
Àsvezes,ummodelodepaginaç ãoquefuncionabemparaapáginade
resultadosdebuscadaAmazonpodenãofuncionartãobemparaumaga-
leriadeimagenscomooPinterest. Diferentescontextosexigemdiferentes
pensamentosdedesign,queeventualmentelevamadiferentessolu çõesde
interface.
Issosemcontarquevocêpodeestarperdendoaoportunidadedecriar
ummodelodeinteraç ãooriginal,icônicoequeexpresseapersonalidadeda
suamarca.
128

## Página 145

CasadoCódigo Capítulo7. Construindoumabibliotecadepadrões
Figura7.3: ApaginaçãodoGooglefogedoconvencionalecriaumdesign
icônicoparaamarca.
Porisso,aoencontrarumpadrãodeinteraç ãoemalgumsite,éimpor-
tanteexaminá-lonosmínimosdetalhesparaentenderqualfoioproblema
quelevouàquelasoluç ão.OresultadopodeterficadoincrívelnositeX,mas
nahoradetransportaramesmasoluç ãoparaoseuprodutovocêpodeacabar
causandoumdesastreemsuausabilidade.
Seráqueoproblemadaquelaempresaeraomesmoquevocêestáten-
tandoresolverparaoseuproduto?Quaismudan çasvocêpoderiafazerpara
deixarasoluç ãocustomizadaparasuainterfaceefazercomqueeleresolva
osproblemasreaisdosseususuários?
Essasperguntasnãosãofáceisdeseremrespondidas,masumaboaop ção
parachegaraessarespostaétestarainterfacecomusuáriosreaisdoproduto,
simulandoumasituaç ãorealdeuso.Opróximocapítulofalajustamenteda
etapadepesquisa:ahoradoprojetoemqueéprecisodeixarsuaconfortável
cadeiradeladoetestaroprodutocomquemmaisimporta.
Gosta desse assunto?
Sevocêdesejasabermaissobreotemadestecapítulo,acesse http:
//fabricio.nu/padroesparaverlinksdebibliotecasdepadrõesonline.
129

## Página 147

Capítulo8
Testandocomusuários
Nafigura8.1temosainterfacedoaplicativodaBritishGasparasmartphones.
Oobjetivodestatelaéfazercomqueoprópriousuárioconsigafazeraleitura
domedidordegásdesuacasa,paraqueacontadomêssejaprocessadapela
empresa.
Atarefaésimples:ousuáriosóprecisaolharonúmeroqueapareceno
medidordegásqueestáinstaladoemsuacasaeentraromesmonúmerona
interfacedoaplicativo.
Sóquereparenodetalhe:nocantosuperiordireitoháumatalhoparaque
osusuáriosconsigamligaraluzdoflashdocelular.Umaespéciedeinterrup-
tor,com“on/off”,queligaaluzdoflasheiluminaoambienteondeousuário
está.

## Página 148

CasadoCódigo
Aferramentafoiadicionada,obviamente,porqueosmedidoresdegás
costumamserinstaladosemlocaisnãomuitoiluminadosdentrodascasasdos
usuários:embaixodapia,emumporãoescuro,ouemalgumlugarfechado
pertodacaixadeeletricidadeedeágua.Nadamaisjustodoquepermitirque
ousuárioilumineoambientecomapróprialuzdosmartphonequejáestá
emsuasmãos.
Masapesardeaideiaparecerumtantoóbviadepoisdepronta,chegaraté
elanãoétãosimplesassim.Esseéotipodeideiaquesurgeapenasquando
osdesignerstêmtotalconsciênciaeentendimentodequalocontextodeuso
doaplicativo.Provavelmente,emumdostestesfeitoscomusuáriosreaisno
contextorealdeusodoapp,algumapessoadevetercarregadoumalanterna
consigonahoradeiratéoporãomostrarparaodesignercomoéqueelafaz
paraveronúmerodomedidordegás.
Nodiaadiadecriaç ãoedesenvolvimentodeinterfacesdigitais,émuito
comumqueosmembrosdaequipepassemlongashorasdodiasentadosem
suamesarabiscandooulayoutandocomodeterminadateladevefuncionar.
Sóqueexistemalgumasideiasquesósurgemquandovocêconheceempro-
fundidadequemsãoosseususuários,doqueelesprecisamequalorealcon-
132

## Página 149

CasadoCódigo Capítulo8. Testandocomusuários
textodeusodaquiloqueestásendocriado.
Alémdegeraremnovasideiasdefuncionalidadesparaosprodutos,re-
alizarpesquisascomusuáriospodemserúteispara:
• Validarseasoluçãodedesignquevocêcriourealmentefunciona;
• Encontrarpossíveisproblemasdeusabilidadenainterface;
• Testarseasoluçãoérealmenteútilparaaspessoas;
• Observarareaçãodaspessoasàmedidaqueusamoproduto;
• Descobriroutrasnecessidadesdosusuáriosquevocênemsabiaque
existiam;
• Validarseapessoarealmenteusariaaqueleprodutoemsuarotinaou
seelaprefeririausaroutrosmétodosouferramentaspararesolvero
mesmoproblema.
8.1 Saia da sua mesa com mais frequência
VejaaseguirumtrechodeumaentrevistacomJaredSpool,CEOdaUserIn-
terfaceEngineeringecoautordealgunslivrossobreUserExperienceeTestes
deUsabilidade.Emumadesuasrespostas,Spoolexplicaquetestesdeusabil-
idadesãomaisbaratosesimplesdeseremfeitosdoqueseimagina.
EntrevistacomJaredSpool
"Alguns times de desenvolvedores parecem procurar por formas mais
barataserápidasdevalidaremseudesign.Usabilidadeéfrequentementeperce-
bidacomosendomuitocara.Vocêachaqueostestesdeusabilidadedevemser
barateados?Perguntandomelhor:testedeusabilidade,hotornot?
Umtestedeusabilidade, emsuaformamaisbásica, custabasicamente
nada.Éumprocessosimples.Vocêsentadoladodealguémeoassisteexperi-
mentandoseudesign.Qualquercustoadicionalvemdatentativadeadicionar
rigoraoprocesso.Rigornãoprecisasercaro,maspodesercaro.
Pensequeécomopintarumacasa. Umapessoapodefazertudopratica-
mentesozinha,economizandoumaboaquantia,masprovavelmenteissovai
133

## Página 150

8.1. Saiadasuamesacommaisfrequência CasadoCódigo
tomarmuitotempoe,semasferramentasadequadas,elanãovaiproduzirum
resultadodealtaqualidade.Masvaiterpintadoacasa.
Aquestãoéquantovalemotempoeaqualidade. Háumarela çãoentre
quantovocêinvesteeaqualidadeevelocidadequevocêvaiterdevolta.Compre
umaescada,unspincéiserolosdemelhorqualidade,tintasmelhoresepe ça
aajudadealgumestudantecolegialdesempregado,evocêteráumapintura
melhoremsuacasa.
A mesma coisa acontece com testes de usabilidade. Investimentos in-
teligentesaumentamaqualidade.Masháumacoisaquediferedepintaruma
casa:podeserumerrocontrataralguémparatestarparavocê.
Oprincipalbenefíciodequalquerprojetodetestedeusabilidadenãoéo
relatórioderecomenda çõesqueéentreguenofinal.Nossapesquisamostraque
obenefícioéaexposi çãoqueotimetemaoobservarusuáriosreaisutilizando
seudesign.Quantomaioressaexposi ção,melhoressãoosprodutosentregues.
Sevocêcontrataalguémparafazeroseuteste,bem,émaisoumenoscomo
contrataralguémparacurtirsuasférias–atarefaéfeita,masvocêperdea
melhorparte. Então,omaiorinvestimentoemtestesdeusabilidadenãoéo
dinheiro–queatépodesernãomuitocaro.Éotempo.Nossapesquisamostra
queasequipesdasorganiza çõesmaiseficazesgastampelomenosduashoras
acadaseissemanasobservandousuáriosinteragiremcomseusprojetos.Cada
membrodaequipe.
Eaexperiênciasepagamuitorapidamente.Otimeagorasabecomoéusar
odesign.Elessabemquaismudan çastiveramoimpactoqueelesesperavam,e
quaisdelasnemforamnotadas.Eelesveemcomoalgunsproblemaspequenos
eirritantespodemarruinarsolu çõesconsideradasinovadoras.
Émuitobaratocome çarapraticartestes–seadúvidaéfazerounãoo
investimento. Agora,sevocêestiverpreocupadocomosgastos,eurecomendo
quevocêfaçaumprodutorealmentedebaixaqualidade.Semprehaveráuma
soluçãomaisbarata. (Eéinteressanteobservarque,sevocêquiserrealmente
fazerumprodutodebaixaqualidade,vocêconseguefazermuitorapidamente,
também.)”
MuitointeressanteametáforaqueJaredfezsobreapinturadacasa.
Asgrandesagênciaseestúdiosdigitaisjáenxergaramovalordostestes
com usuários para os negócios e passaram a incorporá-los naturalmente
134

## Página 151

CasadoCódigo Capítulo8. Testandocomusuários
comopartedoprocessodecriaç ãodeprodutosdigitais.
ExisteumasériedemétodosdepesquisacomusuáriosqueosUXdesign-
erscostumamrealizar:pesquisasquantitativas,entrevistasemprofundidade,
focusgroups,testesdeusabilidade,testesA/B,eyetracking,shadowing,diário
deusocontinuado–entreoutros.Naspróximasse ções,vocêconferemaisde-
talhessobre doismétodosmuitocomuns noprocessodedesenvolvimento
deinterfaces:ostestesdeusabilidadeeostestesA/B.Taismétodospodem
serutilizadostantopelopróprioUXdesignerquantoporumaempresater-
ceiraespecializadanoassunto.Ouentão,naausênciadeles,porpraticamente
qualquermembrodotimequeestejadispostoainvestigarmaissobreocom-
portamentodaspessoas.
8.2 Testes de usabilidade
Testesdeusabilidadetêmporobjetivoverificarafacilidadequeosoftware
ousitepossuideserclaramentecompreendidoemanipuladopelousuário.
São,pordefiniç ão,qualitativos–ouseja,focammaisnaqualidadeeprofun-
didadedosresultadosdoquenecessariamentenonúmerodeusuáriosque
participam.
135

## Página 152

8.2. Testesdeusabilidade CasadoCódigo
Veja a definição de Testes de usabilidade publicada na plataforma
Corais.org(http://corais.org/node/97):
“Usuáriospotenciaisdainterfacesãoincentivadosausá-lanumambiente
monitorado,ondesuasaçõessãogravadaseanotadas.Umprofissionalfacili-
tadorficaaoladodousuárioparaguiá-lopelotesteeincentivarqueverbalize
seusproblemasedesconfortos.
Numasalaseparada,podemestaroutrosmembrosdaequipededesign
dainterfaceparaobservarotesteaovivoseminterferirnocomportamento
dousuário.Apósoteste,osdadossãoanalisadoseégeradoumrelatóriocon-
tendorecomendaçõesparaaequipededesigneoconsultorficaàdisposiç ão
paradiscutirsoluçõesparaosproblemasencontrados.
Combaseempesquisasdeperfildosconsumidores, érecrutadoum
númeroreduzidodeusuáriospotenciais,representandoosprincipaisgrupos
deperfis.Cadausuáriotestaráainterfaceseparadamente,numasessãoque
duraaproximadamente1hora.Aofinaldasessão,eledevereceberumbrinde
paracompensarotempodispendido.
No início do teste, o facilitador explica por que a empresa está pro-
movendoostestese,emseguida,apresentaainterface,pedindoaopinião
136

## Página 153

CasadoCódigo Capítulo8. Testandocomusuários
dousuáriosobreaspectossubjetivosdainterface,comobeleza,atratividade
eetc. Depoisdisso,ousuárioérequisitadoarealizardeterminadastarefas,
comoporexemplo“descobrirseoaparelhoXpossuiumafuncionalidadeY”.
Aofinal,érepassadoaousuárioumquestionáriodesatisfaç ãopararegistrar
seuconfortoaorealizarastarefas.
As tarefas que o usuário realiza são escolhidas com base na análise
cruzadadelog(estatísticasdenavegaç ão),dee-mailsdesuporteedoatendi-
mentoonline. Essasfontesjápossuemdadosqueservemcomopistaspara
encontrarosprincipaisproblemasdeusabilidade.”
Entreosobjetivosmaiscomunsdostestesdeusabilidade,estão:
• Averiguaraaceitaçãodeumnovoprodutonomercado: seráqueas
pessoasestãodispostasacome çarausaroseuprodutopararesolvero
problemaqueelastêm?
• Avaliarausabilidadedoproduto:aspessoasconseguemcompletara
tarefasemdificuldades,emumtempoaceitávelecombaixonívelde
esforçocognitivo?
• Comprarausabilidadedeváriasversõesdiferentesdamesmainterface:
seráqueosusuáriostêmmaisfacilidadedeutilizarbotõesougestos
pararealizarumatarefa?Seráqueumaversãofuncionamelhordoque
aoutra? Testesdeusabilidadepodemserúteisparaentenderoque
funcionaeoquenãofuncionaemcadaumadasversõestestadas.
• Identificaromotivoquelevaaspessoasausaremouaabandonarem
oproduto: seráqueestãotendodificuldadeemumpassoespecífico
dofluxo?Seráqueainterfacenãoestáfornecendoasinformaçõessu-
ficientesparaoqueousuáriocompleteatarefa? Seráqueelesestão
tendodificuldadeementenderoqueestáacontecendocomosistema
àmedidaqueinteragemcomoproduto?
• Coletaropiniõeseideiasdemelhorias:duranteostestes,osusuários
fazemmuitocomentáriossobreoquegostameoquenãogostamem
determinadasoluçãodeinterface,emalgunscasospodendoatéfazer
sugestõesdefuncionalidadesqueelesgostariamdevernaquelepro-
duto.
137

## Página 154

8.3. Desculpascomunsparanãotestarcomusuários CasadoCódigo
• Mediraperformancedoproduto:quantotempoaspessoaslevampara
concluiraatividade?Quantospassossãonecessários?Qualaporcent-
agemdaspessoasqueconseguemefetivamenterealizaratarefacom
sucesso?
Apósumasessãodetestes,écomumqueoUXdesigner(ouaempresa
terceiracontratadapararealizá-los)crieumrelatóriocomosprincipaispon-
tosinvestigadoseasprincipaismelhoriasaseremfeitasnoproduto.Depois,
écomumqueelessereúnamcomtodososmembrosdotimeparapensarem
soluçõesparaaquelesproblemas.
Acadanovociclodetestes-análise-soluções,oprodutovaiamadurecendo
eficandomaisfácildeusar.Algumasempresasrealizamostestesnodecor-
rerdoprocessodedesenvolvimentoeantesmesmodeoprodutoserfinal-
izado,permitindoqueessasmelhoriassejamimplementadaslogonaprimeira
versãodoproduto. Outrasempresaspreferemumaabordagemdiferente:
primeirolan çamoprodutoedepoistestamcomusuáriosparaconseguirem
capturarasmelhoriasnecessáriasparaasversõesfuturas. Osdoisméto-
dossãoválidoseomaisimportanteéqueelescolocamasnecessidadesdos
usuárioscomofococentraldassoluçõesdodesign.Aliás,éessetipodeinicia-
tivaquecolocao“U”nonome“UserExperienceDesign":seoseudesignnão
levaemcontaousuário,entãotalvezvocênãoestejapraticandoUXDesign,
masapenasDesign.
8.3 Desculpas comuns para não testar com
usuários
Apesardeostestescomusuáriosseremcomprovadamenteeficazesparade-
senvolverprodutosquesejamfáceisdeusar,muitasempresasaindanegligen-
ciamessaetapadoprocessoeacabamcriandoprodutosbaseadosapenasna
intuiçãodosdesigners.
Intuiçãoéumelementobastanteválidonaequaç ão,masnãopodesero
único.UmdospilaresdoUserExperienceDesignéofatodeque vocênão
éousuário.Esevocênãoéoseuusuário,écertamentedifícilpreveroque
elevaipensar,sentiredesejarnahoraemqueestivercomoseuprodutonas
mãos.
138

## Página 155

CasadoCódigo Capítulo8. Testandocomusuários
Obviamente,existeaquestãodoscustosedoprazo. Incorporartestes
comusuáriosdentrodoprocessodeDesigntemumcertoimpactonasho-
rasgastasenoprazofinaldaentregadoproduto. Averdadeéquemuitas
vezesépreferíveladiarolan çamentodoprodutoemalgumassemanas,mas
tercertezadequeasoluç ãoérealmentesimplesdeusar–testadaeaprovada
pelosprópriosusuáriosdosite.
Veja a seguir uma lista com as 10 desculpas mais comuns
que as pessoas utilizam para não fazerem testes com usuários,
segundo o site Cardinal Path (http://www.cardinalpath.com/
top-10-lame-excuses-for-not-doing-usability-testing):
Eunãotenhoumlaboratóriodeusabilidade. Vocênãoprecisadeum
laboratóriocompleto,comequipamentosdeúltimageraç ãoecomsaladees-
pelho.Defato,vocênemquerterum.Laboratóriosmuitoelaboradospodem
deixarosparticipantesnervososeinfluenciarnoresultado. Umlugarmais
casualtrazmelhoresresultadosparaostestes.
Eunãotenhoumsoftwaredegravaç ãodetela. Bom,existemsoftwares
gratuitosdisponíveisonlinequefazemisso,ouentãoversões“Trial”desoft-
warespagosquevocêpodeusarporalgunsdias.Esevocênãopuderinstalar
umsoftwareparagravaroqueestásendotestado,faç aotestemesmoassim.
Vocêsempreaprenderáalgumacoisadosusuários.
Eunãoseifazerumaanáliseestatísticadosresultados. Nãoprecisa.
Testesdeusabilidadesãoqualitativos,pornatureza. Vocêestáembuscade
insights,nãodeestatísticas.
Eunãoconhe çoparticipantessuficientes. Jáquevocênãoestáprocu-
randoporestatísticas,esimporinsights,testecom3-5usuários.Naverdade,
testarcom1usuáriojáéinfinitamentemelhordoquetestarcom0usuário.
Édifícilencontrarusuáriosnoperfildemográficoqueestouprocu-
rando. Entãotestecomosparticipantesquemaisseaproximemdoperfil.
Acoisamaisimportanteétestarcompessoasqueusariamoserviço.Operfil
demográficopodeseraproximado.
Meuprodutoaindanãoestáfinalizado. Exato.Esseéoponto.Quanto
antesvocêtestar,melhor.Testeemprotótipos.Testeemwireframes.Testeno
versodoguardanapo. Sevocêesperarparatestarcomoprodutojápronto,
serámuitomaisdifícilfazermudan çasneledepoisdoteste.
139

## Página 156

8.4. Incorporandopesquisacomusuáriosemseuprojeto CasadoCódigo
Eunãotenhotempo. Façaotempoaparecer.Nãoprecisademuito.Se
forpreciso,façatestesremotos(porSkypeoucomserviçoscomoousertest-
ing.com).Vocêconseguiráinsightsempoucashoras.
Eunãotenhobudget. Entãofaç aostestesvocêmesmo. Tenteliberar
tempodeoutrasatividadesparaisso.
Eununcafizantes,nãotenhoideiadecomoaplicarumteste. Aprenda.
Leiasobreoassunto,ouentãoaprendafazendo.
Meuprodutoestáfuncionandobem,nãoprecisodeteste. Ok,essade-
sculpaquaseninguémusa,porquetodomundosabequequalquerproduto
podemelhorardepoisdostestes.Oquesignificaquetodososprodutospre-
cisamdetestes.
8.4 Incorporando pesquisa com usuários em seu
projeto
Émuitocomumouvirdeprofissionaisquetrabalhamemagênciasdepublici-
dadeouempresasdedesenvolvimentodesoftwareque“precisamoscome çar
afazermaispesquisa”.
Ou“precisamosincorporarpesquisanoprocesso.”
Ou“precisamosconseguirmaisverbaparafazerpesquisa.”
Ou“setivéssemosmaistempo,poderíamosterfeitopesquisa.”
Eentão“Pesquisa”ficasempresendoessetabu,essacoisaintangívelcuja
importânciaaspessoasadoramrefor çar,masninguémtemmuitafor çade
vontadedefazer.Emmenosdemetadedosprojetosemquetrabalheihouve
mobilizaçãosuficienteparafazeralgumtipodepesquisaqueenvolvesseos
usuáriosreaisdoproduto. Enão,issonãoéexclusividadedosbrasileiros:
foradopaísoíndiceépraticamenteigual.
Masascoisasestãomudando. Aospoucos,masestãomudando. Vejaa
seguiralgumasquestõesparasepensareparatentarconseguirincorporar
pesquisascomusuárioscommaisfrequênciaemseusprojetos.
Eseapesquisanãofosseumaetapa?
Aocontráriodoquemuitagenteimagina,atal“Pesquisa”nãoprecisaser
umaetapaseparada,queacontecelogonocome çodoprojeto.
140

## Página 157

CasadoCódigo Capítulo8. Testandocomusuários
Nãoprecisanecessariamenteterdatadeinício,datadetérmino,parceiros
contratados,CNPJ,burocracia,pranchetaouformulário. Pesquisanãopre-
cisaterletramaiúscula.
Pesquisa é simplesmente pesquisa. É simplesmente você consultar o
seuusuáriofinalparavalidarumahipóteseouteoriaquevocêtenha. Mas
tambémnãoobrigatoriamente;pesquisapodeserpuramentesentarcomo
usuárioeconversarsobreassuntosrandômicos,saberdascoisasqueeletem
feitoeoqueeleachoudocelularnovoqueelecomprounasemanapassada.
Issonãodeixadeserumaformadeestarmaispróximodoseuusuário.Bom,
melhordoquepassaroprojetotodosentadonoconfortodasuacadeirado
escritório.
Eseapesquisanãofosseumaescolha
Muitasvezes,ostimessereúnemparadecidirseépossívelounãorealizar
pesquisacomusuáriosemumprojeto.Maseseissonãofosseescolhapara
ninguém?Aoinvésdetratarpesquisacomoitem“opcional”,considereembu-
tiremseuscustosenãodarescolhaparaocliente.Seoclientenãopodeoptar
entre“escopocompletocompesquisa”ou“escoporeduzidosempesquisa”,ele
acabacomprandooescopodoprojeto,epronto.Tenhacertezadequedentro
dessesescoposjáexistaumapequenagorduradehorasdestinadasaisso–
ninguémprecisasaberdissoanãoseroUXdesignereogerentedeprojetos
Emumprojetorecentedoqualparticipeifoiassim:umamanhãporse-
mana,doisUXdesignersfazendopesquisadecampo.Nocasodesseprojeto,
olocaldapesquisaéumadaslojasdamarca,ondeosprodutossãovendidos.
Ogerentedeprojetostambémnãotevemuitaescolha.Informamospara
elequeàster ças-feirasdemanhãnósnãoestaríamosdisponíveis(domesmo
jeitoquevocêinformaseuchefequetodasextademanhãvocêprecisachegar
maistardeporquevailevarsuaavónaauladecapoeira).Aregraera“bloquear
ocalendárionoOutlook”enãosefalamaisnisso. Aospoucos,arotinado
restantedotimefoiseadaptandoaessasmanhãsocupadascompesquisa,e
depoisdeumtempoaspessoasjáesperavamansiosasagentevoltarparao
escritório,querendosabercomotinhasidoapesquisanaqueledia.
141

## Página 158

8.4. Incorporandopesquisacomusuáriosemseuprojeto CasadoCódigo
Eseosresultadosnãofossemtabulados
Essetambéméumvíciodequemestáacostumadoafazerpesquisasmuito
grandes(especialmenteasqueenvolvemparceiroscontratados). Semprese
esperaumrelatórioformal, comosdadostabuladosealgumasrecomen-
daçõesdoquedeveedoquenãodeveserfeitoemrelaç ãoaodesigndopro-
dutoapósapesquisa.
Masnãoprecisaserassim.Nessemesmoprojetoquemencionei,nocam-
inhodevoltaparaaagênciaosUXdesignersjáconversavamsobreoque
aprenderamnaquelasduashorasdepesquisaejáchegavamaoescritóriocom
3bulletpointsqueresumiamosaprendizadosdodia.Semprecisardereunião
formal,semnemprecisarsentarnamesaparapassarnadaalimpo:nopróprio
táxinósjáescrevíamosoresumodosresultadosenaprópriatardedater ça-
feirajácomeçávamosacompartilharcomotimeoqueaprendemos.
Eseapesquisanãofossemuitoplanejada?
Planejardemaisapesquisapodesignificardoisriscosparaoprojeto.O
primeirodelesévocêgastarhorasdemaisplanejandooquevaiserpergun-
tado,eessesuperplanejamentoacabarsaindocaro.Osegundoévocêensaiar
demaisenãofazernunca,porquesemprevaiteralgonoprojetoquetempri-
oridademaisaltadoqueapesquisaemsi.
Antesdesairparaoprimeirodiadepesquisa,nósnosreunimospor15
minutosparacombinarasregrasdojogo,eorestofoiimprovisaç ão.Sóvale
tomarcuidadoparanão“planejardemenos”apesquisaeinvalidarosre-
sultadosporcausadealgumerroprimário(comoentrevistaropúblico-alvo
erradoouagircomparcialidade).
Porsorte,paraesseprojetonóscontávamoscomoapoiodeumalojada
marcaqueestavacientedequenósestaríamosporlátodasaster ças-feiras
demanhãfazendoperguntasparaosvendedoreseparaoscompradores.Aos
poucos,fomosnosfamiliarizandocomosvendedoreseganhandoaconfian ça
delesparaqueelescompartilhassemmaisinformaçõesconosco.
Esecadapequenadecisãodedesignfossevalidada?
Éclaroquevocênãopodechegarparaoconsumidoreperguntaroque
142

## Página 159

CasadoCódigo Capítulo8. Testandocomusuários
eleachadonovobotãoquevocêadicionounasemanapassada. Mascomo
aspesquisasacontecemtodasemana,aospoucosvocêvaiseacostumando
adirecionaraconversaparasondarseaquelafuncionalidadenaqualvocê
trabalhounasemanapassadateriaboaaceitaç ãoounão. Tudocommuito
jogodecintura,éclaro,paranãodeturparoudirecionardemaisosresultados.
Quaisosbenefíciosdesse“método"?
Resumindoeconsolidandotudoemumaúnicalista:
• Custodepesquisa“invisível”,diluídonaprópriaverbadoprojeto.
• Nadadeinvestirmuitotempoemumaideiamalucaquedepoisserá
jogadafora: emmenosdeumasemanaumanovaideiajápodeser
validadacomosusuáriosparadescobrirseaquelaéounãoumaboa
ideia.
• Osinsightscolhidosempesquisaservemnãoapenasparavalidarno-
vasideiasquenascemdentrodaagência,mastambémcomopontode
partidaparanovosbrainstormsondeotimededesignersedesenvolve-
dorescriamnovasfuncionalidadesparaoproduto.
• Àmedidaquevocêvaiconversandocommaisconsumidores,épos-
sívelcriarpersonasparaoseuprojeto:umadocumentaç ãodequemé
esseconsumidor,qualoseuperfildemográfico,quaisassuasnecessi-
dades,desejoseanseiosquandoestãobuscandoumasoluç ãoparaseu
problema.
• Vocêacabaconhecendoumoutroladodobusinesscomoqualnão
teriatantocontatoseaspesquisasnãotivessemsidofeitas:opontode
vistadovendedordoproduto,quepassaodiatododentrodaloja–e
osinsightsquetimedemarketingnenhumconseguiriapassarparao
seutime.
• Maisconfiançadosdesignersnahoradeapresentarasideiasparao
cliente,jáqueelasjáhaviamsidopré-testadascomoconsumidorfinal.
143

## Página 160

8.5. Osnúmerosnãomentem CasadoCódigo
• MaisconfiançadoclientenaagênciaeespecialmentenotimedeUX
Designdoprojeto.
Equantoissocustanofimdascontas?
Essa é difícil precisar. Mesmo nesse exemplo que mencionei (das
pesquisasàster ças-feirasdemanhã).
Talvezseeunãoestivessefazendopesquisaàster çasdemanhãeuestaria
usandoessetempoparaadiantaroutrastarefasdoprojeto.Mastambémcor-
reriaoriscodeeutergastadoessetempodistraídonavegandoporaíoupreso
emalgumareuniãoimprodutiva.
Nofimdascontas,ocustofoiabsorvidonomontantedoprojetoeo
clientenemsentiunobolsoopesodetermosfeitopesquisa. Tambémnão
precisamos“comunicaroficialmente”nadaparaele;elesóficousabendoque
fizemospesquisaquandocome çamosacompartilharcomeleinsightscolhi-
dosdosconsumidoresduranteoprojeto.Foiaíqueelenosajudouagaran-
tirquealojaestivessesemprepreparadaparanosreceber,todasemana,às
terças-feirasdemanhã.
Éclaroqueesseexemplonãoéuma“fórmulamágica”decomofazer
pesquisascomusuários,masderepenteéumempurrãoparaquemesteja
comvontadedeincorporaressemétododentrodoprocessodeDesignenão
saibaporondecome çar.
Émuitocomumouvirreclamaçõesdeoutrostimesdizendoqueosfa-
toresexternos(verba/prazo)nãofavoreceramarealizaç ãodepesquisacom
usuários,maséraroouvirhistóriasdetimesquetoparamcorreroriscoe
promoveramudan ça. Comotudonessavida,paraquequalquermudan ça
aconteçaéprecisoquebraralgunsparadigmaseseaventurarumpoucomais
(mesmoquemuitasvezesvocêquebreacaraporcausadisso).
8.5 Os números não mentem
Umoutroladodaspesquisascomusuáriossãoosmétodos quantitativos.
Nasplataformasdigitais,épossívelmedirumasériedenúmerosquedizem
respeitoàformacomaqualaspessoasinteragemcomoseuproduto:tempo
denavegação,quantidadedecliques,linksmaisclicados,ordemdofluxode
144

## Página 161

CasadoCódigo Capítulo8. Testandocomusuários
navegação,taxasdeabandono,taxasdeconversãoetc.Bastaplanejamentoe
umaferramentaquepermitamedircadaaç ãoqueousuáriotomaenquanto
interagecomoseuproduto(oGoogleAnalyticséumótimoexemplodefer-
ramentacomessafinalidade).
Acontece que, apesar de muitas vezes a ferramenta quantitativa de
mediçãodedadosestarinstaladaefuncionandocorretamente,otimedede-
signersedesenvolvedoresacabamesquecendodeolharparaessesnúmeros
paraaprendersobreocomportamentodaspessoas.
Emmuitosprojetos,essaanálisedasmétricasdeumsitepodegerarin-
sightsvaliososparaosdesigners,ajudá-losaidentificarproblemaseainda
informarexatamentequalotipodeconteúdoqueosusuáriosmaisprocuram
nosite.Umexercíciosimpleséodeolharparaaspalavrasmaisdigitadasem
umcampodebuscaqueestejadisponívelemseusite:essalistadepalavras
podeajudarainformartodootimesobrequaisosconteúdosqueosusuários
maisprocurameoprodutopodeserredesenhadoparapriorizaressestemas
maisprocurados.
Existemváriosmétodosdepesquisasquantitativas. Aseguir,vocêvai
aprenderumpoucomaissobreosTestesA/B,umdosmétodosquemaistêm
sidousadosnasempresas–destartupsagrandescorporações.
8.6 TestesA/B
TesteA/Béummétodonoqualsetestamduasversõesdeumamesmatela
(versãoAeversãoB),ouemalgunscasosdiferentesversõesdeumpequeno
elementodatela(umbotão,umlink,ummenuetc.).Emmuitosprojetos,o
testeA/Béusadoparaidentificarmudan çasnapáginaquepodemprovocar
resultadospositivosounegativosnointeressedosusuários.
Normalmente,otesteA/Bfuncionadaseguinteforma:metadedosvis-
itantesdeumsitevêaversãoA,emetadevêaversãoB.Depoisdealguns
diasqueotesteestánoar,épossívelaveriguarosresultadosdecadaumadas
versõeseperceberqualdelasfuncionamelhor.
Nocasodeumalandingpage,porexemplo:emqualversãoosusuários
clicaramnobotãoprincipalparabuscarsabermaissobreoquevocêestava
oferecendo? Emqualversãoosusuáriosdecidiramsecadastrarnositee
145

## Página 162

8.6. TestesA/B CasadoCódigo
emqualversãoelesabandonaramapágina?Qualfoiotempodenavegaç ão
dousuárioemcadaumadasduasversões? Emqualdelasosusuárioscon-
seguiramprosseguirsemdificuldadespelofluxo?
UmadasgrandesvantagensdostestesA/Bemrelaç ãoaoutrostiposde
testeéa precisão,jáqueelesoferecemumfeedbackrealdemercado. Em
algunstiposdepesquisaqualitativos,écomumqueosusuáriosdigamuma
coisa,masnapráticafaç amoutra. Nostestesquantitativos,ahistóriajáé
muitomaisrealista,vistoquevocêestámedindoainteraç ãorealdaspessoas
comoproduto.
146

## Página 163

Capítulo9
Ospecadosdeusabilidade
Problemasdeusabilidadesãomaiscomunsdoqueparecem.Quantasvezes
vocêjánãoteveproblemascompainéisdeelevador,comosbotõesdeum
controleremotooucomasfun çõesconfusasdeumcaixaeletrôniconahora
desacardinheirooufazerumatransaç ãobancária?

## Página 164

CasadoCódigo
Figura9.1:Qualbotãoeudevoapertarparasubirequalbotãodevoapertar
paradescer?
Damesmaformaquearegranúmeroumdocomércioéque“ofreguês
sempretemrazão”,tambémfuncionaassimcomusabilidade: osusuários
sempreestãocertos. Porissomesmoessetipodeproblemaéchamadode
“problemadeusabilidade”eénecessariamenteatribuídoàinterface,enãoà
pessoaqueautiliza.Seumusuárionãoconseguerealizarumatarefadentro
doseusite,aplicativoouqualquertipodeinterfacequeseja,oproblemanão
édousuário;oproblemaédodesign.
Outroproblemacomumemváriosformuláriosdisponíveisporaí:ofato
deobotão“Enviar”eobotão“Limpar”estaremmuitopróximosumdooutro
eseremmuitoparecidosvisualmente. Ousuáriopodeacabarclicandoaci-
148

## Página 165

CasadoCódigo Capítulo9. Ospecadosdeusabilidade
dentalmentenobotão“Limpar”eperdertudooquedigitounoformulário.
Aliás,seráqueobotão“Limpar”érealmentenecessárionessecaso?
Ofatoéqueaindahojemuitossiteseaplicativosfracassammiseravel-
menteporcausadeproblemascomoesse. Quandoousuárionãoconsegue
realizaratarefadesejadaemdeterminadosite,émuitocomumqueeleaban-
doneepartaparaoutra. Afinal,comoémuitocomumafirmarnouniverso
deUX,oconcorrenteestáapoucoscliquesdedistância. Eéverdade. Você
149

## Página 166

9.1. Comoprevenirerrosdeusabilidade CasadoCódigo
mesmojádeveterpassadoporisso:seirritoutantocomumsitequedecidiu
fazersuascomprasemoutrolugar.
Aomesmotempo,produtosfáceisdeusartêmchamadocadavezmais
atençãodaspessoasegarantidousuáriosfiéiscomopassardosanos. Sea
pessoasesenteconfortávelaoutilizarumproduto,énaturalqueelaouti-
lizecomfrequênciaeacaberecomendandoparaamigosquetambémtêmas
mesmasnecessidadesqueela.
Problemasdeusabilidadepodemsematerializardeváriasformasepo-
demterorigememváriosaspectosdaexecuç ãodeumproduto.Umsiteque
demoraparacarregar,umbotãoquenãodeixaclaroqualaaç ãoqueserá
tomadaaoclicá-lo,umlinkquenãotemaparênciadelink,umamensagem
deerroquenãoexplicacomocorrigiroproblema,ummenucomplicadode
navegar,umaferramentadebuscaquenãoapresentaresultadosrelevantes
etc.
Outrosproblemaspodemsermenosvisíveiseseremcaracterizadospela
ausênciadealgo. Umalistagemdeaparelhoscelularesemume-commerce
semaop çãodefiltrarosprodutosporcor,capacidadeousistemaoperacional.
Umalistagemderesultadosdebuscasemnenhumtipodepaginaç ãopara
permitirqueousuáriovejapoucositensporvez.Umsitesemferramentade
busca,quefor çaosusuáriosautilizaremomenuparaencontraroqueestão
procurando.
9.1 Como prevenir erros de usabilidade
Masseusabilidadeétãoimportanteparaumprodutosucederoufracassar,
comogarantirqueoseuprodutonãopequenessequesito?
Atravésdeumbomdesign(eumbomdesigner)
Muitosproblemasdeusabilidadepodemserevitadosantesmesmodeo
produtocome çaraserdesenhado.OprópriofatodepossuirumUXdesigner
notime,quejátenhaexperiênciaemdesenharinterfaceshámuitosanos,
podeevitarqueproblemascomunsaconte çam.Umprofissionalcomoessejá
teveexperiênciasanterioresemdesenharinterfacesetestá-lascomusuários,o
quenormalmentesignificaqueelejásabequaissãoassoluçõesdenavegaç ão
150

## Página 167

CasadoCódigo Capítulo9. Ospecadosdeusabilidade
einteraçãoquefuncionammelhoremcadacaso.
Atravésdetestescomusuários
Masninguéméodonodaverdade.Mesmoprofissionaiscomváriosanos
deexperiênciaacabamcometendodeslizesdeusabilidade,oqueéaindamais
comumquandoseestádesenhandoumprodutonovo,semprecedentesno
mercado.
Éporissomesmoqueexistemmétodosdeverificaç ãodausabilidadedos
produtos.Testesdeusabilidade,análisedemétricas,entrevistasemprofundi-
dadecomusuáriosreais–todosessesmétodosajudamaaveriguarasoluç ão
criadaegarantirqueelaestejarealmenteajudandoosusuáriosarealizarema
tarefadesejada.
Mesmoinformalmenteépossívelverificarseasoluç ãocriadafunciona:
bastaodesignermostrarasoluç ãoparaoutraspessoasdentrodoprópriotime
e,comcerteza,essaspessoasterãocomentáriosconstrutivossobrecomomel-
horarausabilidadedaquelainterface. Profissionaisquetrabalhamcomde-
signedesenvolvimentodeprodutosdigitaiscostumamterolhoafiadonahora
deidentificarpotenciaisproblemasdeusabilidade,entãonadamaisjustodo
queconsultá-losàmedidaqueainterfaceestásendocriada.
Atravésdeboaspráticasdeusabilidade
Existemmuitoslivros,blogselinksquefalamjustamentesobreasboas
emáspráticasdeusabilidade.Tambémexistemsitesespecializadosemcat-
alogarsoluçõesdedesignportipo(menus,buscas,botões,listagens,pagi-
naçõesetc.).Umbomtimededesignestásempreseatualizandoemrelaç ão
aospadrõesdeinteraç ãoquefuncionammelhoremcadacaso,esabeonde
buscarboasreferênciasnahoradedesenharumnovoproduto.
Tambémexistemalgumasregrasuniversaisdeusabilidade(algumasdas
quaismencionadasnoscapítulosanterioresdestelivro),quevalemapena
conheceretersempreemmente,independentedocontextodeuso.
151

## Página 168

9.2. Opçõesdemais,op çõesdemenos CasadoCódigo
9.2 Opções demais, opções de menos
Nemtudoestarávisívelnainterfaceotempotodo.Aindabem.Ocultaritens
dainterfacedoprodutopodeserbastantesaudávelparadeixá-lomaissim-
ples,fácildedigerireagradáveldeusar. Especialmenteeminterfacespara
dispositivosmóveis,ondealimitaç ãodetamanhodeteladeixaaindamais
difícilatarefadelayoutartodososcomandosquevocêgostariadecolocarno
seuproduto.
Osbotões(ougatilhos)queiniciamasinteraçõespodemservisíveisou
invisíveis.Podeounãohaverumtexto,botãoououtradicavisualquemostra
aosusuáriosquealgumadeterminadaaç ãoépossívelali.
Independentedotipodeprodutoquevocêestácriando,nemtodosos
itensestarãoimediatamenteencontráveisassimqueousuárioabreoproduto.
Naverdade,teritensocultoscontribuiparadarmaisimportânciaaositens
queestãovisíveisnatela,criandohierarquiaparaasaçõesquesãomaisim-
portantesnaquelemomento.
Asaçõesnãoprecisamestartodasvisíveisaomesmotempo,maselaspre-
152

## Página 169

CasadoCódigo Capítulo9. Ospecadosdeusabilidade
cisamser“descobríveis”dealgumaforma.Sejaporacidente,porumtutorial,
porbocaabocaentreaspessoasqueutilizamoproduto,porumlinkdeajuda
contextualetc.
9.3 Os gatilhos invisíveis
Essetipodeaç ãoocultaéchamadapelosprofissionaisdeUXde“gatilhosin-
visíveis”(invisibletriggers),esãomaiscomunsdoquevocêimagina.Emdis-
positivoscomsensores(celularescomtouchscreen,microfone,acelerômetro
etc.) osgatilhosinvisíveiscostumamseraindamaisfrequentes–especial-
menteporquenemsempreasaçõessãoativadasexplicitamenteatravésde
umbotão.
Figura9.2: NoTwittereemoutrosaplicativos,você‘puxa’ainterfacepara
baixoparaatualizaralista.
Algunsexemplosdegatilhosinvisíveis:
• OscomandosdevozdaSiri,noiPhone;
153

## Página 170

9.3. Osgatilhosinvisíveis CasadoCódigo
• O“releasetorefresh”dotwitter;
• Balançaracabe çapositivamenteusandooGoogleGlass;
• SacodirocelularparadesfazeroquevocêdigitounoWhatsapp;
• OsatalhosnocantodateladoMacOS;
• Torneirasdebanheiroquesãoativadascomaaproximaçãodamão.
Apesardeosgatilhossereminvisíveisnessescasoslistadosanteriormente,
asregrasdosistemaprecisamserclaramentecomunicadasparaosusuários,
sejaantes,duranteoudepoisqueaaç ãoacontece. Aausênciadefeedback
podecausarconfusãoparaosusuários,aindamaisquandonãoestãoclaras
asregrasqueiniciamdeterminadaaç ão(porqueseráqueoWhatsappdeletou
oqueeutinhaescrito?).
Facebook:asregrasdecomoainteraç ãofuncionasãoexplicadasantesde
elaacontecer(“Vejamaiscomentários”).
154

## Página 171

CasadoCódigo Capítulo9. Ospecadosdeusabilidade
Clearapp:asregrassãoexplicadasenquantoainteraç ãoestáacontecendo
(“Puxeparabaixoparacriarumnovoitem”).
Whatsapp:asregrassãoexplicadasdepoisqueousuáriochacoalhaotele-
fone. Nessecaso,éprecisodaraousuárioaop çãodefacilmenterevertera
ação.
155

## Página 173

Capítulo10
Negligenciandoaperformance
daspáginas
A performance das páginas tem um impacto severo na experiência do
usuário.Segundosamaisnocarregamentodeumsitepodemsignificarfrus-
traçãoparaosusuáriose,consequentemente,menorestaxasdeconversão
paraempresas.

## Página 174

10.1. Oimpactodaperformancedaspáginas CasadoCódigo
As pessoas estão cada vez menos pacientes com páginas que
demoram para carregar. Um estudo recente feito pela Universi-
dade de Massachusetts (http://connecticut.cbslocal.com/2013/01/10/
study-streaming-video-viewers-lose-patience-after-2-seconds/) mostra
queusuáriosperdemapaciênciacomvídeosapósos2segundosdeespera.
Omesmoseaplicaapáginasweb.Aindamaisselevarmosemcontaofatode
quemaisemaispessoasestãoacessandoawebatravésdeseusdispositivos
móveis:muitasvezesabaixaqualidadedeconexãofazcomqueaexperiência
dousuáriosejafrustranteouatécatastrófica.
10.1 Oimpacto da performance das páginas
Vocêjádeveterpassadoporisso.Entraremumsiteesedepararcomuma
páginaquecarregadeformaextremamentelenta,imagenspesadas,elemen-
tosnãootimizadosparawebelayoutnãootimizadoparaodispositivoem
queestásendovisualizado.Issosemcontarossitesquecolocamum“Load-
ing”logonaentrada,achandoqueissobastaparaqueosusuáriosfiquemali
paradosvintesegundos(paraserotimista)esperandoapáginacarregar.
Comocrescimentodeempresasconcorrentesqueoferecemserviçossim-
ilares(todasacessíveisapoucoscliquesdedistância),émuitocomumqueas
pessoasdesistamepartamparaumoutrositequeconhecemesabemque
funcionamelhor. Mesmoquedeformanãoconsciente,tempoéumfator
decisivonapercep çãodaspessoassobredeterminadoserviço.
158

## Página 175

CasadoCódigo Capítulo10. Negligenciandoaperformancedaspáginas
Figura10.1: Quantasvezesvocêjápreferiupagarmaiscaroerenovarsua
carteirademotoristaemumdespachante,emvezdeencararasfilasinter-
mináveisdo(muitasaspas)Poupatempo?Oprincípioéomesmo.
Nocasodosdispositivosmóveis,aindaéprecisolevaremcontacommais
atençãoocontextoemqueositeéacessado.Cincosegundosnafrentedoseu
computadornãosãoofimdomundo.Mascincosegundossegurandoocelu-
larnafiladobancoquandosuavezestáprachegarpodemserincrivelmente
frustrantes.
10.2 Uma batalha de muitas frentes
Obviamente,essaéumabatalhaquenãoselutasozinho.
Primeiro,vocêprecisatercertezadequetodososmembrosdotime(de-
signerseprogramadores)estãocientesdequeessarelaç ãoentreperformance
eexperiênciadousuárioexiste,paraqueelesjácriemoprodutocomisso
159

## Página 176

10.2. Umabatalhademuitasfrentes CasadoCódigo
emmente.Emoutroscasos,vocêprecisaconvencerogerentedeprojetosa
reservaralgunsdiasdojáapertadocronogramaparaqueotimeconsigafocar
emresolveressesproblemasdeperformanceeotimizaropesoedesempenho
dosite.Eemoutroscasos,vocêprecisaconvenceroclienteainvestiralguns
cruzeirosamaisparaqueessaotimizaç ãoaconte ça.
Comoa“experiênciadousuário”éalgobastantesubjetivo,alguémpode
argumentarqueaperformancenemtemtantoimpactoassim.Jáouviclientes
falaremque“seoconteúdoébom,aspessoasesperamcarregarsemproble-
mas”.
É.
Umaformadecontornaressetipodeargumentaç ãoémostrarevidên-
ciasnuméricasemaistangíveisdecomoessarejeiç ãodosusuáriosporsites
pesadosimpactadiretamentenasvendas. Quandopesanobolso,ocliente
costumapensarmelhorsobreoassunto.
Vejaaseguiralgunsestudosdecasorecentessobreboasemáspráticasem
relaçãoàperformanceecomoelasafetaramdiretamenteoengajamentodos
usuárioscomositeouoretornosobreinvestimento(ROI)paraasempresas:
• Usuários esperam páginas carregarem em dois segundos. De-
pois do terceiro, até 40% dos usuários abandonam o site.
(http://www.mcrinc.com/Documents/Newsletters/201110_why_
web_performance_matters.pdf)
• AAmazonnotouque100milissegundosdeesperarepresentamum
declíniode1%nasvendas(http://sites.google.com/site/glinden/Home/
StanfordDataMining.2006-11-28.ppt?attredirects=0).
• O Google perdeu 20% de lucratividade e tráfego de usuários por
causadeumaumentodemeiosegundonotempodecarregamento
desuaspáginasderesultados(http://glinden.blogspot.com/2006/11/
marissa-mayer-at-web-20.html).
• A Akamai mostra em uma pesquisa recente como 75% dos com-
pradores online que experienciam algum tipo de congelamento,
link quebrado ou página que demora muito para carregar deixam
160

## Página 177

CasadoCódigo Capítulo10. Negligenciandoaperformancedaspáginas
de comprar daquele site (http://www.akamai.com/dl/reports/Site_
Abandonment_Final_Report.pdf).
• OGoogleMapsrealizouumestudoqueapontouquereduziropesoda
páginade100KBpara80KBfezcomqueotráfegoaumentasse10%na
primeirasemanae25%nastrêssemanasseguintes.
• OtimededesigndoEtsypercebeuumaumentonataxaderejeiç ão
em12%emdispositivosmóveisquandoresolveramadicionarmaisim-
agensnapágina,numtotalde160KB.
• A DoubleClick removeu um redirect de uma página (aquela
troca de URL que você às vezes nem percebe que aconteceu)
e viu um aumento de 12% no acesso da página em disposi-
tivos móveis (http://doubleclickadvertisers.blogspot.com/2011/06/
cranking-up-speed-of-dfa-leads-to.html).
• AAmazonverificouemtestesquecomprimirimagensemJPEGem
umapáginareduzaquantidadedebaterianecessáriaparacarregá-la
emumdispositivomóvelematé20%. NoFacebook,quetemmais
imagens,essaeconomiadebateriachegaa30%(http://www2012.org/
proceedings/proceedings/p41.pdf).
10.3 Otimizando a performance
Não existe uma única resposta para quem quer saber como otimizar
a performance de um produto. Existem várias delas, cada uma com
um ponto de vista diferente. Existem nichos de desenvolvimento front-
end que são focados somente nesse assunto – e seria pretensão de-
mais tentar explicar tudo isso por aqui. Mas a seguir você encon-
tra alguns pontos citados pelo A List Apart (http://alistapart.com/article/
improving-ux-through-front-end-performance) sobre boas práticas para
otimizaraperformancedeumsite.Nãoéumchecklistexaustivo,maséum
bomcome ço.Emesmoquevocênãosejaumdesenvolvedor,éválidoterem
menteessespontosourepassá-losparaseutime.
161

## Página 178

10.3. Otimizandoaperformance CasadoCódigo
•Limpe seu HTML.Renomeie elementos não-semânticos no seu
HTML.Agrupeelementospelafuncionalidadequeoferecem,nãopelo
conteúdo. MenosIDsnoCSS,menostempodecarregamento. Evite
tambémosexcessosdeDIVs–issotambémfacilitaaediçãodocódigo
nofuturo.
•LimpeseuCSS. Removaseletoresquenãoestãosendousados.Emmé-
dia,essaslinhasextrasdecódigoaumentamotempodecarregamento
dapágina(nãoopeso,repare)em5,5%.
•Reúse código sempre que possível.Elementos-mestre, includes,
padrõesdeinteraç ãoaplicadostambémaocódigo. MenosHTMLe
CSSdeixaamanuten çãomaisfácilereduzlevementeotempodecar-
regamento.
•Façamenosrequisi ções. Cadavezqueseusitefazumarequisiç ão
paraumserviço(ex.:“mostrarlistadeamigosquecurtiramestepro-
duto”),otempodecarregamentoaumentaconsideravelmente. Aliás,
emmuitoscasos,asrequisiçõesdemorammaistempodoquetodasas
imagensexistentesnapáginademoramparaseremcarregadas. Evite
tambémarequisiçãodarequisiç ãodarequisiç ão,quegeraaquelesredi-
rectsbizarrosquemencionamosaquiantes.Nãorequisitearquivosem
todasaspáginasseelenãoestásendorealmenteexibidoemtodaselas.
Quandopossível,substituascriptsderedessociaisporlinks.
•Otimizeasimagens. Passe-asporotimizadorescomooImageOptim.
Mesmoquandoaimagemestáemaltaresoluç ãoparadispositivoscom
tela-retina,comprima.
•Economizenasrequisi çõesdeimagens. Criesprites. Porexemplo:
parabackgroundsqueserepetem,crieumapararepetiç ãohorizontal,
outrapararepetiç ãovertical.
•Usemenosimagens. Verifiquequaisimagensvocêconseguesubsti-
tuircomefeitosdeCSS3. Alémdereduzirdrasticamenteopeso,isso
permitequevocêediteessasimagensnofuturoapenasviaCSS(para
162

## Página 179

CasadoCódigo Capítulo10. Negligenciandoaperformancedaspáginas
nãoterqueabrireeditaroassetoriginal).Existemtecnologiasqueper-
mitemembedarumaimagemnoCSSemvezdesempreapontarpara
umaURLqueirácarregá-la.
ComoUXevisualdesignerspodemcontribuirparaaotimizaç ão
dapágina?
Alémdessespontosmaistécnicos(consultesempreumprofissionalfront-
end)existeumúltimoqueimpactadiretamentenaformaemqueUXevisual
designerspodemcontribuirparaaotimizaç ãodaperformancedeumapágina
–criarumdesignquesejaotimizadoparaboaperformance,desdeoprimeiro
diadoprojeto.
Quantostamanhosdefontevocêestáusando? Precisamesmodetodos
eles?Lembre-sequecadatamanhodefonteviraumaclassenoCSS,eissoau-
mentaotempodecarregamento.Quantasimagensvocêestáusando?Você
estáusandoimagensfullscreensomentequandoérealmentenecessário?O
seulayout“combina”comotipodesitequevocêestádesenhando?Sevocê
estátrabalhandoemume-commerce,ondeaperformancedapáginatem
impactodiretonaconversãoevendas,temcertezadequeaquelaimagem
1600×1200quevocêadicionouérealmentenecessária?Vocêestáreutilizando
elementosdamelhorformapossível,aoinvésdecriarelementosnovosna
páginaacadavez?Todososblocosdeconteúdoquevocêcolocounapágina
sãorealmentenecessários?Quaisdelesvocêpoderiasacrificarembenefício
deummenortempodecarregamento?Quaiselementosvocêpodecarregar
somentedepoisqueousuáriocome çaadescerarolagem?
Alistaéextensa,oassuntoécomplexoeastécnicasdeotimizaç ãomudam
acadadia.
Gosta desse assunto?
Sevocêteminteresseemconhecermaissobreasquestõesdeperfor-
manceemdesign,acesse http://fabricio.nu/performance.
163

## Página 181

Capítulo11
Produtosqueninguémusa
ProfissionaisquetrabalhamemáreasdiretamenterelacionadasaDesigne
Tecnologiacostumamserfascinadosporinovaçõestecnológicas. Diaria-
mentelemosblogs,portaiseoutrossitescomnotíciasdetecnologiaefi-
camosrealmenteempolgadosquandoalgumagrandeempresalan çauma
novatraquitanatecnológica.
Masaspessoasqueutilizarãoosprodutosquecriamos,nemsempre.Al-
iás,quasenunca. Experimenteperguntarparaoseucabeleireiroouparao
caixadosupermercadoseelesabeoqueéHTML,oqueéoSnapchatouo
quesignificaRealidadeAumentada. Tecnologiasessasquefazempartedo
nossovocabulárioedemaisninguém. Pelomenosnãodovocabuláriodas
“pessoasnormais”,paraasquaisvocêdesenhamuitosprodutosnodecorrer
dasuacarreiracomodesigner.

## Página 182

11.1. Começandopelousuário CasadoCódigo
11.1 Começando pelo usuário
Umexemploclássicodafascinaç ãopelatecnologiaéocasodosQRCodes:
umaversãobidimensionaldoscódigosdebarrasqueviroufebrenosúltimos
anosentrealgumasempresas.Aideiaéinteressante:bastaousuárioescanear
oQRCodeusandoacâmeradoseusmartphoneeeleconsegueacessaralguma
URL“escondida”alinaquelecódigo.
MasoproblemaéqueosQRCodesnuncaforamfebre entreosusuários
–pesquisasmostramqueamassivamaioriadaspessoasnuncaouviufalarno
termoesequerpossuemumaplicativoqueconseguelerQRCodesinstalado
emseuscelulares.
Oassuntovirouatépiadanainternetemblogscomoo http://wtfqrcodes.
com/eo http://picturesofpeoplescanningqrcodes.tumblr.com/.
Casoscomoesse,detecnologiasquesófazemsentidoparaosusuários
avançados,masquenãosãoutilizadaspelosusuáriosmédios,sãomaisco-
munsdoqueparecem. Eaorigemdoproblemaéumasó:muitasvezesos
timescomeçamacriaroprodutopensandonatecnologiaqueseráuti-
lizada,emvezdepensaremnoproblemaqueeleestátentandosolucionar
navidadosusuários.
“Nósvamoscriaroprimeiroaplicativoderealidadeaumentadaintegrado
comBluetoothnopontodevenda”.
“Nósvamoscriarumasolu çãodeinterconectividadeentrebrowsere
bancodedadosqueutilizaprotocolosdeconexãoabertos”.
166

## Página 183

CasadoCódigo Capítulo11. Produtosqueninguémusa
“NósvamoscriarumsistemaqueconectaaAPIdoserviçoXcomo
serviçoYemandatudoporSMS”.
Convenhamos.Usuáriosintermediárioseiniciantesnãopensamassime
nuncapensarão.Oqueosusuáriosqueremé“umasoluçãoparapagarminha
contadeluznocelular”.Ou“umasoluçãoparagastarmenostemponafilado
banco”.
SteveJobstemumafrasemuitoconhecidasobreoassuntoquefunciona
bematéhoje:
“Comececomaexperiênciadousuárioedepoisdefinaatecnologiausada.”
–
11.2 Escolhendo uma tecnologia
Idealmente, um produto se inicia a partir de uma necessidade real dos
usuários. Existemváriasformasdesechegaratéumanecessidade: através
depesquisascomconsumidores,atravésderelatóriosdetendênciasproduzi-
dosporconsultoriasparceiras,oumesmoatravésdeuminsightquevocêteve
enquantoestavatentandoresolverumproblemanoseudiaadia.
Depoisdedefinidooproblemaqueoprodutoestátentandoresolvere
depassadaumaetapainicialdeconceituaç ãoebrainstorms,existeummo-
mentoemqueotimeprecisasereunirparadefinirqualseráatecnologia(ou
acombinaçãodediferentestecnologias)quepermitiráqueousuárioconsiga
resolveroproblema.
Ésónessahoraquetermoscomo“SMS”,“Bluetooth”ou“HTML”deve-
riamcome çarasurgirnamesa. Desenvolvedoreseprofissionaiscomback-
groundmaistécnicopodemassumirumpapelimportantenessahora: por
conheceremdecaboaraboastecnologiasdisponíveisnomercado,émais
fácilparaelesdefinirquaisdelaspodemserutilizadasnasoluç ão.
Nessemomento,opapeldoUXdesignerégarantirqueastecnologias
façamsentidoparaaspessoaseparaocontextoondeoprodutoseráuti-
lizado. Afinal,vocênãovaiquerercriarumaplicativodesmartphonepara
consumidoresdeclasseDeE,queraramentetêmacessoaessesdispositivos;
oumesmocriarumsitemobileparaseracessadodentrodeumshopping
167

## Página 184

11.2. Escolhendoumatecnologia CasadoCódigo
center,ondemuitasvezesosinaldeinternetasoperadorasdecelularéfraco
einsuficienteparagarantirumaboaexperiênciadousuário.
Outrocenáriocomuméodeotime receberumbriefingdoclienteque
jápossuaasolu çãotécnicadefinida.“Precisamoscriarumsiteresponsivo
paranossamarca”ou“precisamoscriarumaplicativodecelularparanossos
prospects”. Masseráqueaquelaérealmenteamelhorsoluçãotécnicapara
oproblemadamarcaedousuário? Seráqueaspessoasestãodispostasa
baixarumaplicativodamarcasóparaconseguiremconsultaropre çodos
produtos,porexemplo? Oideal,nessescasos,équeotimesereúnapara
discutirseaquelasoluç ãoérealmenteamelhorop çãoparaaqueleproduto.
Algunscritériosquepodemserlevadosemcontanahoradedecidirentre
umaououtratecnologiasão:
•Conteúdoefuncionalidadesdoproduto. Oqueoprodutoprecisa
fazer? Oumelhor:oqueaspessoasprecisamconseguirfazerusando
aqueleproduto? Quaisasfuncionalidadesessenciaisparaoproduto
existir?Qualamelhorplataformaetecnologiaparacriaraquelafun-
cionalidade?
•Expectativasdosusuários. Oqueousuárioesperaconseguirfazer
comoproduto,eoquevocêestáadicionandodebônusdentrodele?
Comquevelocidadeouqueníveldeesfor çoosusuáriosestãodispos-
tosarealizarematarefa? Elesestãofamiliarizadoscomatecnologia
escolhida?Elestêmacessoaela?
•Tempodedesenvolvimento. Qualocronogramadedesenvolvimento
paraaquelatecnologiaescolhida?Quaisasoutrasop çõesquepodem
tornarodesenvolvimentomaisbreve?Comoodesenvolvimentopode
serfaseadoparalan çarfeaturesoquantoantes–econseguirtestá-las
comusuários?
•Sistemaslegados. Comquaisoutrossistemasjáexistentesoproduto
precisasecomunicar?Quaistecnologiassãocompatíveiscomeles?
•Estratégiadedivulgaçãoeoutrospontosdeentrada. Comoeem
quaiscanaisoprodutoserádivulgado?Atecnologiaescolhidapermite
168

## Página 185

CasadoCódigo Capítulo11. Produtosqueninguémusa
queosusuáriosquefiquemsabendodoprodutoconsigamutilizá-lode
formarápidaefácil? Emquaisoutroscanaisosusuáriosutilizarãoo
produto?
Asdecisõesdetecnologiapodemsercruciaisparaosucessooufracasso
deumproduto,eénessemomentoqueoUXdesignerdevecontribuircom
inputsestratégicosquepossamajudarotimenessadecisão. Conhecero
público-alvoeastecnologiasàsquaiseletemacessopodeserumfatorde-
cisivoparainformaradecisãotécnica.
Masvamosdeixaressesexemplosumpoucomaistangíveis.Vejaaseguir
algumasdecisõescomunsquetenhonotadonosprojetosdequeparticipei
nosúltimosanos:
•Siteresponsivovs.sitededicadoparacadatamanhodetela. Umadas
decisõesmaiscomunsnahoradecriarumwebsiteépensaremcomo
odesignseadaptaráadiferentesresoluçõesdetela. Afinal,usuários
devemconseguiracessarositeindependentedodispositivoqueestão
usando: smartphones,tablets,laptops,desktops,TVsinterativasetc.
Nessecaso,qualamelhorop çãoparaoprojeto? Criarumúnicosite
comlayoutfluidoqueseadaptaautomaticamenteatodosessestaman-
hosdetela? Outerumsiteespecíficoparaseracessadoemcelular,
outrositeespecíficoparaseracessadoemdesktopetc.?
•Aplicativomobilevs. Sitemobile. Seoprodutoestásendocriado
paraqueosusuáriosacessemprioritariamentedeumsmartphone,
qualamelhorsoluç ãotécnicaparaisso? Pediraosusuáriosquein-
stalemumaplicativodamarca,oupermitirqueelesacessemumsite
dopróprionavegadordocelular? Existemvantagensedesvantagens
emcadaumdoscasos.Sitesestãosempreatualizados,sãocompatíveis
comváriossistemasoperacionais,sãomaisfacilmenteencontráveispe-
losbuscadoreseideaisparausuáriosqueestãotendocontatocoma
marcapelaprimeiravez. Poroutrolado,aplicativospodemtermel-
horperformance,podemserusadosofflineemalgunscasos,permitem
maisliberdadecriativanainterfaceeajudamacriarfidelidadecomos
usuários.
169

## Página 186

11.3. Definindoaproposiçãodevalordoproduto CasadoCódigo
•Conteúdoestáticovs.Conteúdodinâmico. Oconteúdodaspáginas
deumsiteseráatualizadocomfrequência? Afrequênciaéaltaosu-
ficienteparajustificarqueexistaumsistemagerenciadordeconteúdo
parafacilitaraadministraç ãoepublicaç ãodesseconteúdo?Ouaspági-
nasserãoatualizadascombaixafrequência?
Essessãosóalgunsexemplos,masalistadedecisõestécnicasébastante
extensa.Astecnologiasdecomunicaç ãopodemvariardeBluetoothaSMS,
passandoporradiofrequênciae tethering. Aslinguagensdeprogramaç ão
tambémsãoinúmeras:HTML,JavaScript,C++,ObjectiveC,PHP,Rubyetc.
Ossensorestambémvariam: GPS,acelerômetro,giroscópio,câmera,sen-
soresdepresen ça,impressõesdigitais,luminosidade.
ParaoUXdesigner,maisimportantedoqueconhecercomoastecnolo-
giasfuncionam(oumesmodominarcadaumadelas)éentendercomoas
pessoasinteragemcomelaecomoelasimpactamnaexperiênciadousuário
–tantopositivamentequantonegativamente.Afinal,issopodeserumfator
decisivoquandoumapessoaestáconsiderandoutilizaroseuprodutoouode
umconcorrente.
11.3 Definindo a proposição de v alor do pro-
duto
AProposiçãodevalor(ou ValueProposition)éoprocessodedefiniç ãodeum
produtoeoresultadoencontradoaofinaldesseprocesso.
Independentedevocêtrabalharemagênciasdepublicidade, estudos,
consultoriasoustartups,sãocadavezmaiscomunsosbriefingsquetratam
deajudardeterminadamarcaacriarumprodutodigital,enãoapenasdeen-
contrarformascriativasdecomunicá-loparaopúblico-alvo.
Acontecequeoprocessodecriaç ãodeprodutosdigitaisacabasendoum
poucocaótico.Dentrodeumaempresa,sãodiversososdepartamentos,áreas
enegóciosquetêmopiniõesdiferentessobreoqueoprodutodeveser,para
quemeledeveserdesenhadoe,principalmente,quaisfuncionalidadesele
deveconter. MasoexercíciodedefiniraProposiç ãodevalordoproduto
podeajudarbastantenessaetapa.
AlgunspontosqueaProposiç ãodevalorajudaadefinirsão:
170

## Página 187

CasadoCódigo Capítulo11. Produtosqueninguémusa
• Porqueestamosinvestindorecursosnesseproduto? Qualaoportu-
nidadedenegóciosqueaempresavêemcriaresseproduto?Quaisda-
doseestatísticasajudamacomprovarqueoprodutoéfinanceiramente
viável?
• Oqueéoproduto?Quaisfuncionalidadeselecontém?Qualaprincipal
função?Comoelesediferenciadoscompetidores?
• Paraquemeleestásendocriado?Qualoperfildemográficodousuário?
Emaisimportante:qualocomportamentoounecessidadequesãoes-
pecíficosdesseusuárioequeconectamdiferentesperfisdemográficos
emumgrupoconsistenteeuniforme?
• Ondeequandooprodutoseráusado? Quehorasdodia? Comque
frequência?Emcasa,emtrânsito,notrabalho?Éumprodutodeuso
constanteoualgoparausarumavezsó?
• Comoqueremosqueaspessoasusemoproduto?Qualéoobjetivode
UX?Oquequeremosqueaspessoassintamaoutilizaresseproduto?
Qualsensaçãoqueremoscausarequalproblemaqueremosresolver?
Eaperguntafinal:detudoissoquevocêlistouenquantotentavarespon-
deraessasperguntas,oqueémaisimportante?
Responder às perguntas listadas anteriormente é relativamente fácil.
Bastaumasessãodebrainstormcomosmembrosdotimeparaquevocêsper-
corramcadaumadelasecomecemalistarascaracterísticasdoproduto.Se
vocêquercriarumaplicativodecelularparaaspessoascombinaremcaronas
comosamigos,empoucomenosdeumahoraépossívelgerarumalistade
maisdecinquentaideiasdefuncionalidadediferentesparaoproduto.
Masdefiniraproposiç ãodevalorétambémumprocessodeafunila-
mento. Depoisdediscutircomtodosdotimesobreoqueoproduto não
éechegaraumaconclusãosobreoqueoproduto é,otimeprecisasepoliciar
evoltaraolharparaaproposiç ãodevaloracadanovadecisãodedesign,tec-
nologiaoumarketingqueprecisasertomada.Terumobjetivobemdefinido
paraoprodutoajudaaevitarqueoprodutosetransformeemoutracoisano
decorrerdocaminho.
171

## Página 188

11.3. Definindoaproposiçãodevalordoproduto CasadoCódigo
Éessencialsaberdecidiroquenãoserádesenhado.Oquevocênãode-
senhatambémédesign.
Existemváriosmodelosdisponíveisonlineparaadefiniç ãodaProposiç ão
devalordeumproduto.Algunsdelessãomaisprescritivosetentamorientar
otimeapreencherlacunasnahoradedefiniroqueumprodutofaz;outros
sãomaisabertosedãomaisliberdadeaotime.
Oprincipalriscoemnãodefiniressespontosclaramenteéacabarcom
um“produtoFrankenstein”.Aimpressãoqueasempresastêméquequanto
maisfuncionalidades,maisoprodutoseráútilparaaspessoas.Quequanto
maisabrangenteforopúblico-alvo,maisgenteiráutilizá-lo.Quequantomais
cenáriosdeusoforemmapeados,maiseleestarápresentenavidadaspessoas.
Oquenãoénecessariamenteverdade.
Oquenãofaltamporaísãoprodutoscomtoneladasdefuncionalidades,
masquenãosãousadosporninguém. Aliás,arriscodizerqueesseéum
dosprincipaisproblemasdasmilharesdestartupsquecriamprodutoscom
172

## Página 189

CasadoCódigo Capítulo11. Produtosqueninguémusa
cadavezmaisfrequêncianoBrasileforadele. Essailusãodequeumpro-
dutoprecisasergrandeparapoderservaliosopareceumpoucoinocente
demais—comoquandotentamoscozinharalgoeacabamoscolocandotanto
tempero,tantorecheio,tantacobertura,queaequaç ãodesaboracabapas-
sandodopontoeficandoenjoativa.
Gerarumalistadeideiasdefuncionalidadesparaumprodutoéumpro-
cessorelativamentefácil(apesardetergrandevalorparaoprojeto).Masde-
cidirquaisdelasentramequaisdelasnãoentraméumprocessoquepode
tomarsemanas,culhões,eumapitadadepesquisacomusuários.Éumpro-
cessoexaustivo,noqualtodosdotimeprecisamestarenvolvidoseprecisam
discutirporlongashoras.
DopontodevistaespecíficodoUXdesigner,saberidentificarumbrief-
ingqueestáinflacionadodemaisesaberdizernãoparaalgumascoisaséum
dosprincipaisdesafiosdaprofissão—mastambémumdosexercíciosmais
divertidos.
173

## Página 191

Capítulo12
Priorizandofuncionalidades
Quandovocêestáenvolvidodiretamentenacriaçãoedesenvolvimentodeum
produtodigital,énormalquereradicionarfuncionalidadesaeleparagarantir
queelesejao“maiscompletopossível”.
Masénessahoraquemuitosequívocosconceituaisacontecem.
Écomumquedesenvolvedorespensememprodutosdigitaiscomoum
conjuntodefeaturesquecoexistemefuncionamjuntasparaentregarvalor
aousuáriofinal.Acontecequenemsempretermaisfuncionalidadessignifica
terumprodutomelhor.
12.1 Oeterno problema do escopo e do prazo
Designersedesenvolvedoresfrequentementeseveememumasituaç ãoem
queexistelimitaçãodeprazooudebudget.Oprojetotemumadatadelan ça-
mentopré-estipulada,eaindaassimexistemuitacoisaaserfeitaatéqueo

## Página 192

12.1. Oeternoproblemadoescopoedoprazo CasadoCódigo
produtoestejaprontoparaserlan çado.Nessescasos,olharparaosdetalhes
daexperiênciadousuárioquefarãooprodutoterumaboausabilidadeeser
bemvistopelaspessoasqueoutilizamnormalmentesãodespriorizadosna
listadeafazeresdoprojeto.
Vocêjádeveterpassadoporisso. Oprojetoestáaalgumassemanasde
terminareositepossuidezenasdepáginasetemplates,masquandovocê
vaianalisaroresultadofinaldeperto,oquevocêvêsãopáginasmalorgani-
zadas,funcionalidadesquenãoforamtestadasexaustivamenteeproblemas
deusabilidadeemtodososmomentosdofluxo.
Masterumprodutogigantenãoénecessariamenteocaminhomaiscor-
reto.Aindamaissevocêeseutimequerementregarumprodutodealtaqual-
idadeparaomercadoeumaótimaexperiênciaparaosseususuários.
Emalgunscasos,épreferívelsacrificaralgumasfuncionalidadeselan çar
umprodutomenordoque“fazersóporfazer”ou“adicionarsóporadicionar”.
Quantidadenãoéqualidade,aindamaisemumassuntotãocomplexoecheio
depeculiaridadesquantoaexperiênciadousuário.
“Gooddesignisaslittledesignaspossible.Less,butbetter–itconcentrateson
essentialaspects.Productsarenotburdenedwithnon-essentials.Backto
purity,backtosimplicity.”
–O10ºprincípiodobomDesignsegundoDieterRams
(http://en.wikipedia.org/wiki/Dieter_Rams)
Figura12.1:Comoassim,lan çarumtelefonesemCopyandPaste?
176

## Página 193

CasadoCódigo Capítulo12. Priorizandofuncionalidades
VejaoexemplodoiPhoneilustradoaqui.Quandofoilan çado,oiPhone
nãotinhaafuncionalidadedeCopyandPaste,aqualmuitosdesignersede-
senvolvedoresconsiderariamessenciaisparaolan çamentodoproduto. Na
verdade,oiPhonenãotinhanemmetadedasfun çõesquetemhoje.Emesmo
assim,oprodutoeratãofácildeusaretinhaumaexperiênciadeusotãoúnica
ememorável,quefoiumgrandesucesso.
12.2 A estratégia dos cupcakes
"Entregueumcupcake,aoinvésdeumbolocomrecheioecobertura.”
EssafrasefoiusadapelaAdaptivePathemumvídeoquefalasobreo
planejamentodeprodutosdigitais.
Vejaovídeo: https://vimeo.com/19738421
Quandosetratadeplanejarfeaturesecriarumcronogramaparaqueelas
sejamlan çadasemumproduto,muitasempresasaindatêmumamentalidade
queopessoaldaAdaptivePathchamade“mentalidadedebolo”.
Primeiro,comececomobolo. Depoiscrieorecheio. Nofinal,impres-
sionetodomundoaoadicionarumadeliciosacobertura.
177

## Página 194

12.2. Aestratégiadoscupcakes CasadoCódigo
Masoproblemadessetipodementalidadeéqueascoisasacontecemem
sequênciacronológica.Eobolo,porsisó,semorecheioenemacobertura,
podesermuitosecoenãomuitoempolganteparaoconsumidor.
Oqueelespropõe,então,équevocê comececomumcupcake.
Apesardemenor,ocupcakeporsisójáébonitoesaborosoosuficiente
paraatrairaspessoasparaconsumi-lo.Depoisqueocupcakeestiverpronto,
aísimvocêpodepensaremconstruirumsegundocupcake,umbolomaior
ouatéumbolosuperdecorado.
Eavantagem,éclaro,équeocupcakelevamuitomenostempo(erecur-
sos)paraficarprontodoqueobolo.
Comosprodutosdigitaisoproblemaésimilar. Àsvezes,asempresas
miramtãoaltonoprodutoquequeremlan çar,queoprodutoacabanunca
sendolan çado.Oupior:élan çadosemocuidadocomosdetalhesquefarão
oprodutorealmentesediferenciardaconcorrênciaequedarãoaosusuários
motivossuficientesparavoltaremautilizá-lo.
178

## Página 195

CasadoCódigo Capítulo12. Priorizandofuncionalidades
12.3 Priorizando as features de um produto
Nahoradedecidirquaisfuncionalidadessãorealmenteessenciaisparaqueo
produtosesustente,UXdesigners,productownersedesenvolvedoresacabam
usandodiferentesmétodoselevandoemcontadiferentesfatoresnaequaç ão.
Masdeformaresumida,asfeaturesdevemserpriorizadaslevandoem
contaasnecessidadesdosusuários,asnecessidadesdenegócioseascondições
técnicasparaqueelassejampossíveis.Aparticipaç ãodeprofissionaisdeUX
nesseprocessodepriorizaç ãodefeaturesajudaacolocarousuárionocentro
doprocesso.Ummétodocomumutilizadoporeleséolevantamentodecasos
deusodoproduto.Emlinhasgerais:
1) Quaissãooscasosdeusomaiscomunsnoseuproduto?
2) Quaissãoosplayersouparticipantesenvolvidosnessecaso?
3) Paraqueessesparticipantesconsigamrealizara(s)tarefa(s)descrita(s)
nessecasodeuso,quaissãoasfuncionalidadesqueelesutilizam?
4) Dessalistadefuncionalidades,quaisdelassãoestritamentenecessárias
paraqueaaç ãoocorra?
Aofazeresseexercício,épossívelpercebercommaisclarezaque,apesar
deoprodutosergrandiosoeterumasériedefuncionalidades,apenasum
pequenogrupodelaséresponsávelpor80%a90%dousodeumproduto–
enquantooutrasmalchegamarepresentar1%doscasos.
179

## Página 196

12.3. Priorizandoasfeaturesdeumproduto CasadoCódigo
Umaformabastanteconhecidadepriorizarusosdecasoefuncionali-
dadeséochamadoKanoModel–criadonosanos80porNoriakaKano,um
expertemsatisfaç ãodosconsumidores.
Essencialmente,éumamatrizformadapordoisvérticesondeasfeatures
sãoposicionadaslevandoemcontaaSatisfaç ãodoconsumidoreoEsfor ço
deexecução.
Apartirdomomentoemquevocêpercorretodaalistadefuncionalidades
doseuprodutoeasposicionanessamatriz,ficamaisfácilvisualizarquais
delasdevemserpriorizadas,dependendodoobjetivodenegóciosdaempresa.
180

## Página 197

CasadoCódigo Capítulo12. Priorizandofuncionalidades
Normalmente,oprimeiropassoécumpriromínimonecessárioparaevi-
tarfrustraçãodosusuários(cantoinferiordireitodamatriz). Jánocanto
superioresquerdo,ficamoschamados“quickhits":aspequenasimplemen-
taçõesquenãorequeremgrandeesfor çotécnicoetrazemresultadosnotáveis
paraaexperiênciadousuário.
AlémdoKanoModel,existemmuitasoutrasmetodologiasparasepri-
orizarfuncionalidades,todasdefácilacessonawebparaquemseinteressa
peloassunto.Sãovariaçõesdomesmomodeloquepriorizamoutrosaspectos
quenãoasatisfaç ãodoconsumidor.MasjáqueaquioassuntoéUXdesign,
melhorseguircomoKanoModelecolocaroconsumidoremprimeirolugar.
181

## Página 198

12.4. Umprodutonuncaestápronto CasadoCódigo
12.4 Um produto nunca está pronto
Vocêjádeveterpassadoporissonoseutrabalho.Duranteasúltimassemanas
doprojeto,otimeviranoitesenoitesparadeixartudoredondinhoparao
lançamento.Depoisdealgunsconflitosepossíveisatrasos,finalmenteosite
élançado,otimecomemoraedepoisnuncamaistocanoassunto. Projeto
entregue,sitenoar,etantofazseaspessoasestãotendoumaboaexperiência
ounãoaointeragiremcomoprodutofinal.
Masaverdadeéquenemsempreprecisaserassim. Paradeterminados
tiposdeproduto,éimportanteplanejaroquevaiacontecercomeledepois
queaprimeiraversãoforlan çada. Éclaroquesevocêestádesenvolvendo
umalandingpageparaumeventoqueacontecesomenteemumdiaespecí-
fico,talvezessenãosejaoseucaso. Masmuitasvezesoprodutotemuma
grandeoportunidadedeevoluire,consequentemente,gerarnovosnegócios
paraasuaagência/produtora/empresaeumaexperiênciamaisrefinadapara
osusuários.
Lançarumnovosite,ouaplicativo,ouinterfacerequercuidado.Apósa
publicação,éprecisoanalisarcomoaspessoasestãorealmenteinteragindo
comeleparaconseguirotimizaraexperiênciadousuário.Muitasvezes,uma
funcionalidadequevocêdesenhouedesenvolveucommuitocuidadoestá
sendosubutilizadapelosusuários,ouentãoelesestãotendodificuldadesem
prosseguirnofluxoporumpequenodetalhedeusabilidadequepassoubatido
nahoradeentregaroprodutofinal.
Nessesentido,oUXdesignerpodeajudarogerentedeprojetosaplanejar
quaisserãoasetapasdeevoluç ãodoprodutoapósolan çamento.Existeuma
sériedemétodosparaseanalisarumprodutoepropormelhoriasnele,eum
dosprincipaiséolharparaasmétricas,entendercomoaspessoasestãoin-
teragindocomcadase ção,páginaefuncionalidadeedepoisproporpequenos
refinamentosparaajudaraspessoaseaempresaaatingiroobjetivooriginal.
Tambéméimportanteque,emdeterminadomomentodoprojeto,otime
chegueaumconsensoemrelaç ãoàsmétricasdesucesso,ou KeyPerfor-
manceIndicators (KPIs)doproduto. Comovocêsconseguirãomedirseo
produtorealmentecumpriuasmetaspreestabelecidas? QualoplanoB(e
planoC,eD,emalgunscasos)casoametanãosejaatingida? Quaismu-
dançasvocêspodemfazernoprodutoparaotimizarsuaperformance?
182

## Página 199

CasadoCódigo Capítulo12. Priorizandofuncionalidades
Depoisdeumtempoqueoprodutoestánoar,oUXdesignerpodeduplar
comumprofissionaldeAnálisedeMétricas(ouBusinessIntelligence)para
analisaroqueestáeoquenãoestáfuncionandoali. Nessemomento,pe-
quenosajustesnainterfacepodemfazerumagrandediferen çaparaosnegó-
cios–oqueajudaaconvenceroclienteainvestirumashorasamaisdepois
queoprodutoestálan çado.
Umoutrométodointeressantenessemomentoéo testedeusabilidade.
Agoraqueoprodutoestáfuncionando,oUXdesignerpodeorganizaralgu-
massessõesdetestesondeosusuáriossãoconvidadosautilizaremoproduto
edaremfeedbacksobreoquegostameoquenãogostam.Novamente:um
processocomoessegerainsightsvaliososparaotimizaraperformancedo
produto.Emparaleloaisso,apósalgumtempodelan çamento,épossívelob-
servarosoutroscanaisdeservi çoaoconsumidor queaempresapossuipara
avaliarcomoaspessoasestãoreagindoaonovoproduto.
Umexemplo:emumprojetoquelan çamosrecentementeaquinaagên-
cia,redesenhamoscompletamenteoe-commercedamarcaemquestão.Após
ummêsdolan çamentodonovosite,fizemosumasériedeentrevistascom
osoperadoresdocall-centerdamarcaparaentenderseosconsumidoreses-
tavammencionandodificuldadesemutilizaronovositepararesolverum
problema.Nofinaldasentrevistas,saímoscomumalistadecincomelhorias
relativamentesimplesqueprecisávamosfazernositeparaotimizaraexper-
iênciadosusuários.Apósessanovaversão,ocall-centerviuumaquedade8%
nonúmerodetelefonemasemrelaç ãoaosite.Menoscustoparaaempresa,
menosproblemasparaosusuários.
Omaisimportanteéestarpreparadoparaolan çamentoeterumplano
deação.Muitosprodutoshojeemdiasãolan çadosemversõesdrasticamente
simplificadasdaversãooriginal,comoforamconcebidosinicialmente.Mas
issonãoaconteceporfaltadeprazoouverba.Asempresas(principalmente
startups)jáperceberamquequantoantesumprojetovaiparaarua,maiores
aschancesdereceberfeedbackdosconsumidores,testareimplementarmel-
horias.Apartirdaí,éclaro,asnovasfuncionalidadespodemserprogressiva-
mente“plugadas”noprodutoàmedidaqueoprodutoeaempresaevoluem.
183

## Página 201

Capítulo13
ChecklistdeUX
UserExperiencenãoéumadisciplinabinária,ondeexisteo“certo”eo“er-
rado”.Paraalgunsusuários,determinadolayoutpodeparecerlindoesimples
deusar,enquantoparaoutrospodeseracoisamaisdifícildomundo. Na
essência,UXDesigntratadeentenderoqueosusuáriospensamecomose
comportamquandoestãotentandorealizaralgumatarefausandoumpro-
duto.
Mas,apesardainexatidãoesubjetividadedaexperiênciadousuário,exis-
temalgumasboaspráticasquepodemserúteisparaosUXdesignerseoutros
membrosdotime.
Listeiaseguirumaespéciede resumodetudooquefoifaladonolivroaté
agora. Menoscomo“asrespostascertas”emaiscomoumlembretesobreo
quevocêdeveteremmentequandoestiverprojetandoumaexperiênciapara
asoutraspessoas.
Aexperiênciadousuárioprecisaser...

## Página 202

13.1. Simples CasadoCódigo
13.1 Simples
•Reduzir. Épossívelretiraralgumelementoouinformaç ãodatelae
aindaassimpermitirqueousuárioconsigacumpriratarefasemprob-
lemas?
•Revelar.Vocêestárevelandoasinformaçõesprogressivamente,àme-
didaqueousuárioavan çanofluxo?Épossívelesconderalgumaparte
datelaesóexibi-laapósalgumaaç ãodousuário?
•Padronizar. Ovisualdatelaestáconsistente? Vocêestáusandoo
mesmoestilovisualparaelementosquepossuemfun çõessimilares?
Vocêestáreaproveitandopadrõesdeinteraçãoemdiferentespartesdo
produto?
•Simplificar.Asinformaçõesestãosendoapresentadasdaformamais
simplespossível,empequenasdoses?Épossívelreduzirtextosouocul-
taralgunselementosnaquelemomentoespecíficodaexperiência?
•Priorizar. Épossívelesconderoudespriorizarvisualmentealgumas
ações,paraqueaaç ãoprimáriarecebamaisimportância?Seexistem
gatilhosescondidosnatela,elessão“descobríveis”dealgumaforma
(poracidente,porumtutorial)?
•Adiar.Épossívelreduzirouretiraralgumcampodoformulário?Você
estárealmenteusandotodasasinformaçõescoletadas?Épossívelco-
letaralgumdessesdadosemummomentofuturodofluxodousuário?
•Testar.Ausabilidadedosistemajáfoitestadacomusuáriosreais?Ex-
isteumasoluç ãoparaosproblemasmaiscomunsqueosusuáriosen-
contramaointeragiremcomoproduto?
•Analisar.Otimeestáusandoasmétricasexistentes(ex.:GoogleAna-
lytics)damelhorformapossível?Quaissãopequenosajustesquepo-
demserfeitosnainterfaceparaotimizaraconversãodeusuários?
186

## Página 203

CasadoCódigo Capítulo13. ChecklistdeUX
13.2 Acionável
•Direcionar. Estáclaroparaousuárioaaç ãoprincipalqueeledeve
tomarnaquelemomentoounaquelatela?
•Explicar.Orótulodaaç ãoestáclaroedizaousuáriooquevaiaconte-
cerapóseleclicarouinteragir?Épossíveldeixaraindamaisclaro?
•Indicar.Osbotõeselinkstêmaaparênciaapropriadaparaexplicarao
usuárioqueelepodeinteragircomeles?
•Incentivar.Ostextosdatelaestãoincentivandoousuárioaseguiradi-
ante?Ousuáriotemacessoàsinformaçõesnecessáriasparacontinuar
semovendopelofluxo,semprecisarfazerdesviosderota?
•Situar. Ousuárioconsegueselocalizardentrodaestruturadosite
naquelemomento? Estáclaroparaelequaloestadodosistema? Ele
sabeemquepassoestádentrodofluxoequantospassosfaltampara
eleconcluiratarefa?
•Informar. Ousuáriotemacessoatodasasinformaçõesnecessárias
paraseguiradiante?
•Ajudar.Quandoumamensagemdeerroéexibida,estáclaroparao
usuáriooquecausouoerroeoqueeledevefazerparacorrigi-lo?
•Continuar.Osistemaevitacriarruassemsaídaparaousuário?Você
estásugerindoaçõesparaousuárioemcadapassodofluxo?
13.3 Inteligente
•Destacar.Qualaaç ãomaiscomumqueousuáriobuscaquandoin-
teragecomseusite? Épossíveldestacaressaaç ãoemdetrimentode
outras? Épossívelcriaratalhosparaasaçõesmaiscomunsemdeter-
minadatela?
•Prevenir.Osistemaprevineerrosantesdeelesacontecerem?Olhando
paraasmétricasdosite:quaisoserrosmaiscomunsqueosusuários
187

## Página 204

13.4. Agradável CasadoCódigo
cometem?Comoanteciparesseserrosedeixarasinstruçõesmaisclaras
paraqueelesnãoaconte çam?
•Tolerar.Osistemaétolerantecomdistraçõeseerrosdousuário? É
possível“perdoar”algunserrosnomeiodocaminho?Ousuáriocon-
seguedesfazeraçõescomfacilidade?
•Personalizar. Vocêestáusandoasinformaçõesquepossuisobreo
usuáriodamelhorforma? Comessasinformaçõesquevocêpossui,
comovocêpodefacilitaravidadousuáriooufazeraexperiênciaser
maispersonalizadaparasuasnecessidades?
•Automatizar.Épossívelautomatizaralgumprocessoparasimplificaro
níveldeesfor çorequeridodousuário?Épossívelutilizaralgumsensor
ououtrafontedeinformaç ãoemvezdepedirqueousuáriomanual-
menteaadicione?
•Extrapolar. Vocêestáaproveitandooutrossentidoscomotatoeau-
diçãoparatransmitiramensagemparaousuário?
13.4 Agradável
•Humanizar.Otomdevozdostextosdainterfaceestáalinhadocoma
personalidadedasuamarca?Sesuamarcafosseumapessoa,comoela
conversariacomosusuários?Qualvocabulárioelausaria?
•Alinhar. Asimagensutilizadasnainterfaceestãoalinhadascomo
brandingdaempresa? Facilitar.Otamanhodoselementosdainter-
facesãosuficientesparaqueousuáriointerajacomelesemtodosos
dispositivosemqueoprodutoéacessado?Ostextossãolegíveisosu-
ficiente?Hácontrasteehierarquianostamanhosdefonte?
•Mover.Asanimaçõesetransiçõesdeinterfaceestãosendousadasda
melhorformaparadarfeedbackaousuáriosobresuasaçõeseparaex-
pressarapersonalidadedamarca?
188

## Página 205

CasadoCódigo Capítulo13. ChecklistdeUX
•Considerar. O sistema evita criar desvios de rota na experiência?
Todas as ações que você pede para o usuário são extremamente
necessáriasparaoobjetivoqueeletememmenteaousarseuproduto?
•Explicar.Estáclaroparaousuárioporqueosistemaestásolicitando
determinadasinformações?Atrocaéjusta?Ousuáriovêcomclareza
obenefícioemforneceraquelesdados?
•Agilizar. Você está usando o tempo do usuário com parcimônia?
Quandoumaaçãotomamuitotempoparaserconcluída,osistemaper-
mitequeelefaç aoutrascoisasnomeiotempo?
•Surpreender. O sistema proporciona agradáveis surpresas para os
usuáriosnodecorrerdaexperiência?
13.5 Relev ante
•Entregar. As funcionalidades do produto são realmente as que o
usuárioesperaencontrar?Vocêjátestouoseuprodutocomusuários
reais?
•Refletir.Porqueaspessoasusariamoseuprodutoemvezdeumpro-
dutoconcorrente?Porqueelasdeixariamdefazeraquelaatividadedo
jeitoquejáfazem,paracome çaremafazerusandooseuproduto?
•Escolher. As tecnologias escolhidas para sustentar o produto são
compatíveiscomastecnologiasàsquaisosusuáriostêmacesso? Os
usuáriosdominamessastecnologias?Algumadelaspodeestarsetor-
nandoumabarreiraparanovosusuários?
•Acompanhar.Olhandoparaasmétricasdoproduto:quaisse çõesou
funcionalidadesestãosendopoucoacessadas?Issoénecessariamente
umproblemaparaosobjetivosdenegóciosdaempresa? Épossível
eliminarfun çõesirrelevantesparaaproposiç ãodevalordoproduto?
•Consultar.Paraperguntaraosusuários:nofinaldaexperiênciaopro-
dutoestáentregandooquesepropõeafazer?
189

## Página 206

13.5. Relevante CasadoCódigo
•Melhorar.Vocêestáusandoinformaçõescolhidasdosusuários(qual-
itativamenteouquantitativamente)parafazermelhoriasnoproduto?
Quaisnovasfuncionalidadeselesesperamver? Comoaperfeiçoaros
principaisfluxos?
190

## Página 207

Capítulo14
UXnomundodosnegócios
Nateoriaétudomuitobonito,masenaprática?Aessaalturavocêdeveestar
seperguntandosobreorealimpactodaexperiênciadousuárionosnegócios.
Afinal,todossabemosqueumapráticasóseconsolidacomoprofissãoapartir
domomentoemquecome çaagerarlucroparaasempresas–tornandoo
modelosustentávelparatodasaspartesenvolvidas.
Aboanotíciaéquecadavezmaisasempresasestãopercebendooimpacto
deUXparaosnegócios,apontodemontaremtimesinteirosdeprofissionais
deUXparaseusprojetos.
Porserumaprofissãoumpoucomaisestratégica,énaturalqueonúmero
deprofissionaisdeUXsejamenordoqueodediretoresdearte,oudesen-
volvedores,porexemplo.Paradarumaideia:emumaagênciadepublicidade
digitalbrasileirade200funcionários,onúmerodeUXdesignerscostuma
variarentre3e6.NosEUA,essenúmerovariaentre10e20.Jáemempresas

## Página 208

14.1. Design=Dinheiro CasadoCódigo
maiores(comoGlobo.com,Amazon,Google),osdepartamentosdeUXpo-
demchegara200,300profissionais,muitasvezesdivididosentrediferentes
subáreas(comoPesquisa,DesigndeInteraç ãoetc.).
Essamovimentaçãocome çouaacontecernosanos2000,quandoasem-
presasmaiorescome çaremaperceberoquantopequenasmelhoriasdeus-
abilidadepodemafetardiretamenteoslucros.
14.1 Design=D inheiro
Umexemploclássicoéocasodo botãode300milhõesdedólares daAma-
zon. Issomesmo. Umsimplesajusteemumbotãofezcomqueasvendas
dalojavirtualaumentassemem45%,gerandoumfaturamentoadicionalde
US$300milhõesnoprimeiroanodepoisdeimplementado. Quemcontaa
históriaéJaredSpool,da UserInterfaceEngineering—UIE(http://www.uie.
com/articles/three_hund_million_button).
AAmazonresolveuinvestigareincrementaroformuláriodecadastro
peloqualosconsumidorespassavamassimqueterminavamdeadicionaros
produtosaocarrinhodecomprasnalojavirtual. Emtestesdeusabilidade,
aequipedeJaredpercebeuqueoproblemanãoestavanausabilidadedos
formulários(queeramrelativamentesimplesdeserempreenchidos),massim
noqueoformuláriorepresentavaparaosconsumidores.
Osconsumidoresraramenteselembravamdeseunomedeusuárioe
senhanahoradefazerologinecontinuaracompra.Parasolucionaroprob-
lema,elessimplesmentesubstituíramobotãode“Cadastro”pelobotãode
“Continuar”,fazendocomqueologinouregistronositefosseumpassoop-
cionalnofluxodecompra.Afinal,osconsumidoresestãomaispreocupados
emconcluiracompradoqueemcriarumperfilemumsite.
14.2 Convencendo o time a investir em UX
QuemtrabalhacomUXháváriosanosjáestáacostumadoavisualizarore-
tornosobreinvestimento(ROI)queaáreatrazparaosnegócios.Pequenos
ajustesemfluxosdecadastropodemgeraraltasporcentagensdeconversão,
melhoriasemferramentasdebuscadentrodoseusitepodemaumentardras-
ticamenteotempodenavegaç ãodosusuáriosereduzirastaxasdeabandono,
192

## Página 209

CasadoCódigo Capítulo14. UXnomundodosnegócios
emudan çasnahomepagedeumsitepodemimpactardiretamentequaissão
aspáginasmaisacessadas.
Masemalgunscasos,obviamente,éprecisoconvenceroutraspessoasa
topareminvestiremUX;ocliente,oseuchefe,ochefedeoperaçõesdaem-
presae/ouosinvestidores.
Nãoéumatarefafácil. UsarestudosdecasocomoessedaAmazon
citadoanteriormentepodeajudarbastante.Masemcontextosdiferentessão
necessáriasestratégiasdiferentesdeajudaraoutraparteavisualizarapossi-
bilidadederetornoaoseinvestiremUX.
Internamente,algumasdasprincipaisvantagensdeterumprofissionalde
UXdentrodotimeéagilizaroprocessodedesign,evitarrefaçõesemlayouts
eaindafacilitaracomunicaç ãoentreosmembrosdotime.
Externamente,nahoradeprovaraoclientequeeleprecisainvestirem
umprofissionaldeUXnoprojeto,acoisamudadefigura:éprecisoencontrar
formascriativasdeexemplificarcomoosbenefíciosdeterumUXdesigner
notimeimpactadiretamenteosobjetivosdenegóciosdaempresa. Masa
dicaaquiécriarumoudoisexemplospráticosqueestejamdiretamenterela-
cionadosàprincipalmetadaempresa(porexemplo:otimizarocarrinhode
comprasnocasodeume-commerce).
193

## Página 211

Capítulo15
Comocome çaremUXDesign
Nosúltimosanos,tenhorecebidomuitasmensagensdepessoasquequerem
entrarnaáreadeUXmasnãotêmcertezadequalamelhorformadefazê-
lo.Foientãoqueresolviconectaralgunspontosparatentarajudarquemestá
começandoagoranomercado.
Estelivro,porexemplo,éumdessespontos. Sevocêchegouatéaqui,
esperoquetenhatidoumpanoramarelevantesobreoqueéUserExperience,
oquefazumUXdesignerequaissãoalgunsdosdilemasmaiscomunsda
profissão.
Sevocêgostoudoaperitivoeestáinteressadoemseguirumacarreiraden-
trodaáreadeUserExperienceDesign,estecapítuloéparavocê.

## Página 212

15.1. OmercadodeUXnoBrasil CasadoCódigo
15.1 Omercado de UX noBrasil
UXDesignéumacarreiramultidisciplinar, oqueacabatrazendoparao
mercadoumadiversidademuitoricadeprofissionais,formadosemdiversas
áreasdoconhecimento.Jornalistas,bibliotecônomos(ebibliotecários),pub-
licitários,designers,gerentesdeprojeto–oquecontamesmoéaorganização,
acapacidadedesecolocarnolugardosusuáriosemuito,muitobomsenso.
Em2011, aUXPA(UserExperienceProfessionalsAssociation)fezuma
pesquisaparalevantaroperfildosarquitetosdeinformaç ãobrasileiros:car-
acterísticasdemográficas,formação,cargo,salários,jobdescriptioneinter-
esses.Valeapenadarumaolhadanosresultadoseentenderumpoucomais
sobremercadonoqualvocêestápensandoementrar: http://www.slideshare.
net/upasaopaulo/perfil-do-profissional-de-ux-no-brasil.
Segundodadosdoestudo,feitoem2011,71%dosprofissionaisdeUX
brasileirosestãolocalizadosnaregiãosudestedopaís,46%nacidadedeSão
Paulo.Adistribuiç ãodegêneroséequilibrada:56%sãohomense44%mul-
heres.
86%dosprofissionaisbrasileirossãograduadose/oupossuemalgumtipo
depós-graduação,sendo41%delesemáreasrelacionadasaArteseDesign.
Aquiumdadoencorajadorparaquemestápretendendoentrarnomer-
cadoagora:40%dosparticipantesdoestudoseconsideramautodidatase37%
dizemque“aprenderamUXfazendo”.Somente22%aprenderamUXemal-
gumasaladeaula.
OssaláriosnoBrasilvariammuito,principalmentepelofatodenãoexistir
umaregulamentaçãoclaraparaaárea.SegundoamesmapesquisadaUXPA,
umprofissionalJúnior(cercade1anodeexperiência)ganhavaumsalário
mensalmédiodeR$2.252em2011.ParaprofissionaisPlenos(entre3e4anos
deexperiência),osalárioédeR$ 3.350eparaumSênior(cercade6anos
deexperiência),R$4.979.Noscargosmaisaltosamédiasalarialficavaentre
R$6.500parasupervisoreseR$ 8.831paragerentesem2011.Masnosúltimos
anosessenúmeroaumentoubastante,dadoocrescimentodaprocurapor
profissionaisqualificadosnomercadoemtodoopaís.
196

## Página 213

CasadoCódigo Capítulo15. ComocomeçaremUXDesign
15.2 Onde trabalhar
Apesardemaisemaisempresasprocuraremecontrataremprofissionaisde
UX,onúmerodeUXdesignersespalhadospelopaísaindaérelativamente
pequenosecomparadocomdiretoresdearteoudesenvolvedores–entãonão
émuitocomumencontrarumdelesnafiladosupermercadoounapadaria
pertodesuacasa.Masmesmoqueessasletrasmágicas(“UX”)nãoapareçam
nonomedocargodapessoa,issonãoquerdizerqueelanãoestejaprojetando
experiênciasparausuários.Comocitadonoiníciodolivro,umprogramador
aodesenvolverumsitetambémacabaparticipandocomoumUserExperi-
encedesigner.Afinal,aspessoasusarãoaquelainterfacequeoprogramador
estácriandoeissoteráimpactodiretonaexperiênciadelas.
Ainda que nem todo mundo coloque “UX” no nome do cargo do
Linkedin, o número de profissionais que o fazem ao redor do mundo é
gigante: uma rápida busca pelo termo “UX designer” retornará mais de
800milresultados,segundopesquisarealizadaemsetembrode2012(http:
//designmodo.com/future-user-experience-design). Dizematéque“UX”é
umdostermosquemaiscrescenaredesocial.
SegundoapesquisarealizadapelaUXPAem2011(http://www.slideshare.
net/upasaopaulo/perfil-do-profissional-de-ux-no-brasil) , os lugares mais
comunsparasetrabalharcomUXnoBrasilsão,nessaordem: agênciasde
publicidade,empresas-cliente(ex.:Bradesco,Nike,Fiat),consultorias,por-
tais(ex.:UOL,Globo.com)eprodutorasweb.Outroslugaresdalistaincluem
institutosdepesquisa,governo,agênciasdecomunicaç ãoestartups.
15.3 Como conseguir um emprego na área
Muitagenteentraemcontatocomigocomentandosobreavontadedemu-
darparaUXdefinitivamente. Normalmente,essaspessoasjáfazemalgum
trabalhorelacionadoaisso,masestãoprocurandoumempregomaisespe-
cializadonoassunto.
Maséumciclo:vocêsóserácontratadocomoUXdesignerquandotiver
umportfoliocomtrabalhosdeUX.MassevocênuncatrabalhoucomUX,
comoéquevaiconseguirmontarumportfolio?
O caminho mais certeiro é oestágio: as empresas normalmente re-
197

## Página 214

15.3. Comoconseguirumempregonaárea CasadoCódigo
queremnenhumaexperiênciaanterior,aresponsabilidadeémenorevocê
teráchancesdeerrar,acertar,eaprendernomeiodoprocesso. Depoisde
cercadeumanovocêteráexperiênciasuficientenocurrículoparaconseguir
umacontratação.
Senoseucasooestágioéfinanceiramenteinviável,umaop çãoésepro-
gramarantes(leia-se“juntardinheiro”)parapoderficaralgunsmesesesta-
giandoantesdesercontratado.Massevocêjátrabalhacomalgorelacionado
aDesign,épossívelqueconsigacome çardiretoemumcargodeUXdesigner
/arquitetodeinformaç ãojúnior. Nessecaso,éimportanteserhonestonas
entrevistasedeixarclaroquevocêestáfazendoatransiç ãoentreumaáreae
outra.
Mascomoencontraressasvagas?
UmadicaéprocurarnoLinkedin(ouemblogsesitesespecializadosno
assunto)nomesdeempresasquefazemumtrabalholegaldeUserExperience,
epassaraacompanharosetordevagasdeseussites. Ouentãotrocaruma
ideiacompessoasquejátrabalhamnaáreaepedirdicasdequaisempresas
possuemprofissionaisdeUXemseuquadrodefuncionários.
NoFacebook,existeumgrupoespecializadoemdivulgarvagasdeUX.Se
vocêestiverefetivamentebuscandoumavaga,recomendodarumapassada
porlá:https://www.facebook.com/groups/uxjobs.
Masseráqueeusouqualificadoosuficiente?
Comoditonoiníciodolivro,osprincipaisrequisitosparasetornarum
profissionaldeUXsãoempatia,bomsensoeorganizaç ão.Empatia,porqueé
precisoentender(egostardeinvestigar)oqueaspessoasprecisamequerem
verquandoestãousandoprodutosdigitais.Éprecisoconversarcompessoas,
éprecisosaberfazerasperguntascertasefiltrarosresultados(éaquiqueentra
obomsenso).
Massevocênuncaentrevistouusuários,nãoéprecisotermedo.Primeiro,
porqueéumprocessoqueseaprendecomaprática.Conhe çoprofissionais
quetrabalhamcompesquisaháanosedizemquecontinuamaprendendoa
cadanovasessãodeentrevistasoutestes.Esegundo,porquenãoexistecerto
ouerrado;oqueexistemsãoformasdiferentesdesechegaràmesmaresposta.
Organizaçãoéoutracaracterísticabastantedesejável.Nodiaadiadotra-
balhodeUXvocêacabarálidandocomgrandesquantidadesdeinformaç ão
198

## Página 215

CasadoCódigo Capítulo15. ComocomeçaremUXDesign
emformabruta,antesdefazeroexercíciodesimplificá-laetorná-ladigerível
paraosusuários.Éprecisoserorganizadoparanãodeixarescaparnenhum
detalhe,jáquenormalmentesãoospequenosdetalhesquefazeramaiordifer-
ençanaexperiênciadousuário–paraobemouparaomal.
Sevocêsentequeseencaixanesseperfil,váemfrente. Orestovocê
aprendenomeiodocaminho,àmedidaqueerraeacertaacadaprojeto.
15.4 Como se conectar com profissionais de UX
Agrandemaioriadasvagasnãoéanunciadaemlugarespúblicos;elassurgem
deconhecidos,decontatosprofissionaisouamigosdeamigos.Conversecom
profissionaisdaárea.Visiteempresasquetrabalhamcomissoedescubramais
dodiaadiadeumprofissionaldeUX.Participedeeventos–nãoapenaspelo
conteúdodaspalestras,maspelasconversasqueacontecemnosintervalos.
Façacontatosesigaessescarasnasredessociaisparaaprenderumpouco
sobrecomoelespensam.
Conversetambémcomprofissionaisdeáreasdiferentes.Grandepartedos
conhecimentosqueajudamumUXdesigneraserumbomprofissionalnãoé
exclusivodeUserExperience.Conversecomotimedetecnologia,comotime
deplanejamento,comosdecisoresdenegócios–oumesmocomamigosseus
deoutrasáreasquejátrabalharamcomalguémdeUXnopassado.Comoa
áreadeUXtransitaentreváriasoutrasáreasdoconhecimento,essatrocade
experiênciascomprofissionaisdeperfisdiferentesdoseuésempreválida.
Gruposelistasdediscussão
Gruposdediscussãotambémpodemserumaótimafonteparasabero
queestásendofaladonaáreaeestabelecercontatoscomoutrosprofissionais.
Minhasdicasdegrupos:
• NoFacebook:https://www.facebook.com/groups/designdeinteracao/
• NoLinkedin:https://www.linkedin.com/groups/AI-UX-Arquitetura-
Informa%C3%A7%C3%A3o-User-3209228
• No Google Plus: https://plus.google.com/communities/
113160149077207243924
199

## Página 216

15.5. Comosemanteratualizado CasadoCódigo
OIAI(InformationArchitectureInstitute)possuiumalistadediscussão
emportuguêsdaqualparticipamgrandepartedosprofissionaisdaárea.
Nessalistasãodiscutidasreferências,estudosdecaso,novastecnologias,pro-
cessos,metodologia,vagas,eventoseoutrosassuntosrelacionadosàprofis-
são,incluindoaorganizaç ãodeanimadoshappyhourseoutrosencontros
regionaisentreUXdesignersearquitetosdeinformaç ão.Nestapáginaépos-
sívelseinscreverparareceberose-mailseparticipardasdiscussões: http:
//www.iainstitute.org/.
HátambémalistadediscussãointernacionaldoIxDA,comumvolume
aindamaiordeparticipantesedediscussões,todasrealizadaseminglês: http:
//www.ixda.org/discussion.
15.5 Como se manter atualizado
Muitagenteperguntasobre“comoaprenderUX”,masprefirochamarde
“comosemanteratualizadosobreUX”.IssoporqueUXnãoéalgoquese
aprendedanoiteprodia.Lerblogsdoassunto,lerlivros,assistirapalestras
eouvirpodcastssãoboasformasdeiradquirindoconhecimento.Essescon-
teúdosestãocadavezmaisacessíveis,quasesempregratuitamenteeonline.
Treineoinglêsparaconseguirabsorvernovosconteúdos.Naprática,quando
vocêestárodeadoporessasinformaçõesecontinuaseatualizando,énatural
queduranteosprojetosvocêconsigapensaremtodososaspectosdaexper-
iênciadousuário,semsofrerouterreceiodefalhar.
200

## Página 217

CasadoCódigo Capítulo15. ComocomeçaremUXDesign
Links,sites,blogs,podcastseeventos
Háalgumtemporeuniemumúnicolinkasprincipaisfontesereferências
noassunto,incluindosites,blogs,links,podcasts,eventoseprofissionaispara
vocêseguir.Recomendoescolheralgunsdelesparacome çaraincorporaressa
leituranoseudiaadia: http://uxdesign.cc/.
Costumotambémpublicarartigosemportuguêssemanalmenteno http:
//arquiteturadeinformacao.com.Nãoesque çadedarumapassadaporlá.
201

## Página 218

15.5. Comosemanteratualizado CasadoCódigo
LivrosdeUX
Se você está procurando alguns livros para continuar sua jor-
nada de aprendizado, não deixe de conferir essa lista de livros de
UX no GoodReads: https://www.goodreads.com/group/bookshelf/
43635-user-experience-design.
Tambémselecioneialgunslivrosespecíficossobreusabilidadeem http:
//fabricio.nu/usabilidade.
Postseartigos
Compilei nesse link uma lista com os principais posts do meu blog
paraquemestáchegandoagoranaprofissão: http://arquiteturadeinformacao.
com/por-onde-comecar-em-ux-design.
PáginasnoFacebook
ExistetambémumcompiladodepáginasnoFacebookquefalamsobre
UXeArquiteturadeinformaç ão. Bastaassinaralistaparapassarareceber
atualizaçõesdiretonasuapáginainicialdoFacebook: https://www.facebook.
com/lists/10150623977151406.
202

## Página 219

CasadoCódigo Capítulo15. ComocomeçaremUXDesign
15.6 Como aprender a usar as ferramentas
UmadasvantagesdeUXéqueconheceredominarasferramentasnãoé
algoessencialparaconseguirumempregonaárea. Nãoexisteumpadrão
emrelaçãoàferramentautilizadaentreasempresas(comoéocasodopacote
Photoshop,IllustratoreInDesignparadiretoresdearte),enormalmenteos
wireframeseoutrosentregáveispodemsercriadosapartirdequalquerferra-
mentabásicadeediçãodeimagensouapresentações.Conhe çoprofissionais
quesóusamPowerPointeExcelequesãoUXdesignerstalentosíssimos.
Masaindaassimsevocêquiserirsefamiliarizandocomasferramentas
maisusadas,valeapenabaixardemosetestar,mesmoquesejacomumpro-
jetofantasma. Algumasdelassãoonlineegratuitas. Entendercomoessas
ferramentasfuncionameoqueépossívelfazercomelasémaisimportante
doquepossuiragilidadecomelas,ouconhecertodososatalhos–pelomenos
noiníciodacarreiradeUX.
Sequiserumalistacompletadeferramentas,recomendovisitar http://
fabricio.nu/ferramentas.Alistaéextensa,masnãosepreocupe:nodiaadia
vocêvaipoderescolhersuasfavoritaseasqueodeixammaisconfortáveis.Em
UXnormalmentenãoexisterestriç ão,jáqueomaisimportanteéoraciocínio
portrásdodocumentodoqueoformatofinaldele.
15.7 Mas por que trabalhar com UX
Essaéumaperguntadifícil,masimportante.Eumesmocomeceiminhacar-
reiracomodiretordearte,masresolvifazeramigraç ãoparaUXjánosegundo
outerceiroanodeprofissão. Nofimdodiaeusentiafaltadeparticipardas
discussõesmaisestratégicasarespeitodoqueestavasendocriado;iralém
dacamadavisualecome çarapensarnasfuncionalidadeseinteraçõesque
tornavamastarefaspossíveis.
VejaaseguirumtrechodeumaentrevistaquefizcomaElisaVolpato,
consultoraindependentedeUXquejátrabalhaháváriosanosnaprofissão:
203

## Página 220

15.7. MasporquetrabalharcomUX CasadoCódigo
Entrevista com ElisaVolpato
Comocome çouatrabalharnaárea?
Souformadaemjornalismo,masjánomeiodocursopercebiquenão
levavamuitojeito.Quandomeformeiefiqueinaquelacrisede“agoravou
terqueviraradulta”fuifazerumaentrevistadeempregoeouvifalarde
arquiteturadeinformação.Aentrevistanãodeucerto,masfoiapalavra-
chavedequeeuprecisavaparasairpesquisandoporaí.Acheiumexem-
plardoursobranco,coloqueiembaixodobraçoefuitrabalharemuma
consultoriaespecializadaemUX.
PorqueUX?
EudescobriqueUXeraoqueeuqueriafazerporquegostavadeorga-
nizareinvestigar.Gostomuitodeobservarpessoas,defazerentrevistas,
testes,inventartécnicasmalucasepensarnomelhorjeitodeinvestigar
umdeterminadoponto.Éincrívelquandodácertoeagentepensa“Zás!
Táaquiaoportunidade!Éissoqueagentetemquefazer!”
Meempolgaapossibilidadedecriarcoisasquepodemserúteisefazer
adiferen ça. Ficomuitofelizquandoumserviçofuncionabemegosto
depensarqueotrabalhoqueeufaçopodedeixaroutraspessoasfelizes
também. E,senãodeixar,esperoquepelomenosalguémmedêum
feedbackparaeucome çarociclotododenovo.
204

## Página 221

CasadoCódigo Capítulo15. ComocomeçaremUXDesign
Sequiser conferirmais entrevistascom profissionaisdeUX eenten-
der como eles começaram na área:http://arquiteturadeinformacao.com/
por-que-ux/
205

## Página 223

Capítulo16
Ofuturodaexperiênciado
usuário
Vocêdeveterreparadoqueamaioriadosexemploscitadosnestelivrotrata
desites,aplicativosdecelularouinterfacesquerodeiamnossodiaadia.
Maseoquevempelafrente?
Comofuncionaaexperiênciadousuárionosrelógiosinteligentes,nos
óculosinteligentes,oumesmonoseletrodomésticosinteligentesqueestão
começandoasurgir?
Arespostaéqueosprincípios,emsuaessência,sãoosmesmos.Usabil-
idadeéusabilidade,independentedaplataforma. Boasexperiênciasdeuso
nosacompanhamdesdequenascemos–emobjetosfísicos,emespaçosar-
quitetônicos,emprodutoseletrônicosedigitais.Eatendênciaéqueissocon-
tinueigual,sejaqualforanovatecnologiadomomento.

## Página 224

CasadoCódigo
Masalgumascoisasmudam.Aformacomoaspessoasinteragemnocelu-
lar,porexemplo,ébemdiferentedaformacomoaspessoasinteragemcom
computadoresdesktop–eosdesignerstiveramquereaprendertudoissocom
ocrescimentodousodecelularesnosúltimosanos.Osimplesfatodequenos
computadoresdesktopvocêinteragecomoponteirodomouseenossmart-
phonesvocêinteragecomapontadosdedosjáfazumadiferen çaenormena
formacomoasinterfacesprecisamserdesenhadas.
Amesmacoisaacontecerácomosóculosinteligentesetodososoutros
objetoscitadosanteriormente.Emvezdecliques,aspessoasinteragemcom
piscadas,acenosdecabe çaetoquesnahastedoóculos.Issomudacompleta-
menteaformacomoasinteraçõessãopensadas,masnãomudaaessênciae
osprincípiosdeusabilidadeeexperiência.
Nospróximosanos,certamentesurgirãolivrosespecializadosexplicando
“comodesenharinteraçõesparaos smartwatches”(substituapelonomede
qualquerobjetonovoquevenhaasurgir).
Osdesignersprecisarãomaisumavezreaprenderasmelhorespráticas,
evitaroserroscomunseadequarsuadocumentaç ãoparaessanovareali-
dade.Enavelocidadecomaqualatecnologiasetransforma,éesperadoque
numfuturopróximoessesprocessosde“reinvenção”aconteçameminterva-
losmuitomaiscurtosdetempo.
Mas,maisimportantedoqueexplicarosdetalhesdecadaumadessas
plataformas,oobjetivodestelivrofoiapresentarosconceitosbásicosdeUser
Experienceedespertarointeresseemaprendermaissobreoassunto.Sevocê
tiverinteresseemacompanharmaissobreessasnovasplataformas,tereitodo
oprazerdeacompanhá-lonajornada.
Vocêpodeentraremcontatocomigoem: http://fabricio.nu
208

## Página 225

Capítulo17
Bibliografia
SAFFER,Dan. DesigningforInteraction: CreatingSmartApplications
andCleverDevices.NewRidersPublishing,18dejulhode2006.
SAFFER,Dan.Microinteractions:DesigningwithDetails.O’ReillyMe-
dia,10demaiode2013.
COLBORNE,Giles.SimpleandUsableWeb,Mobile,andInteractionDe-
sign.NewRidersPublishing,16desetembrode2010.
Alémdoslivrosacima,duranteotextosãoreferenciadoslinkseartigos
publicadosem http://arquiteturadeinformacao.com.