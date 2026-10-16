---json
{
  "id": "php-e-laravel-crie-aplica__es-web",
  "title": "PHP_e_Laravel_Crie_aplicações_web",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "**Arquivo Original:** `PHP_e_Laravel_Crie_aplicações_web.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "aplica",
    "crie",
    "laravel",
    "linguagens",
    "php",
    "web"
  ],
  "perguntas_tipo": [
    "Como utilizar PHP_e_Laravel_Crie_aplicações_web?",
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

# PHP_e_Laravel_Crie_aplicações_web

> **Arquivo Original:** `PHP_e_Laravel_Crie_aplicações_web.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 2

CasadoCódigo
“ A tudo que tenho de mais importante nessa vida, minha esposa Jordana e
nossa primeira filha, Clara. ”
–RodrigoTurini
i

## Página 4

CasadoCódigo
Agradecimentos
Pormaisqueeuqueiraetentemuito,nenhumconjuntodepalavrasseráo
suficienteparaexpressarmeueternoagradecimentoàminhaesposaJordana
enossafamília,queagoraestámaiorcomachegadadapequenaClara.
GostariatambémdeagradeceraoDanielTurini,quesempreinfluenciou
emmeucrescimentopessoaleprofissional.Foielequemdeumeuprimeiro
computadoremeencaminhouaomundodaCiênciadacomputaç ãoerecen-
tementeaosdiversosprojetosemPHPquedesenvolvemosjuntos.
AgradeçotambémàsequipesdaCaelum,AluraeCasadoCódigo,que
sãoempresassensacionaisconstituídasporprofissionaisextraordinários.Em
especialameusamigosPauloeGuilhermeSilveira,VictorHarada,Maurício
AnicheeLuizCorteReal.
iii

## Página 6

CasadoCódigo
Prefácio
ApesardeserintimamenteligadoaoJava,umaoutralinguagemdeprograma-
ção,hápoucomaisdeumanorecebiodesafiodemanteraaplicaç ãointerna
deumaempresaamericana,totalmenteescritaemPHP.Nocome ço,otraba-
lhofoibemmaisdifícildoqueeuesperava,jáquesetratavadeumprojeto
legado,nemumpoucoorientadoaobjetosemuitíssimocomplicadodeman-
ter. Depoisdeumtempo,vimosqueasoluç ãomaissimplesparaessecaso
seriareescrevertodooprojeto,utilizandoboaspráticas,testesautomatizados
easpossibilidadesmaisatuaisdalinguagem.ÉaíqueentraoLaravel.
Eujáhaviatidoalgumcontatocomesseframeworkquandoestavatraba-
lhandonoconteúdotécnicodocursodePHPdaCaelum,masaoestudá-loa
fundoenquantoviabilizavaasop çõesatuais,tiveasensaç ãodequeseriauma
excelenteescolha.Hoje,eutenhocerteza.
OobjetivodesselivroserámostrarporqueoLaraveléaapostadomer-
cadoatualeminhaprimeiraop çãodeframeworkMVCemPHP.Criarapli-
caçõeselegantesempoucotemponuncafoitãofácil.
v

## Página 8

CasadoCódigo Sumário
Sumário
1 Introdu ção 1
1.1 Oprojetoeastecnologias . . . . . . . . . . . . . . . . . . . . . 1
1.2 Oqueveremosduranteolivro . . . . . . . . . . . . . . . . . . 3
1.3 DownloaddoLaravel . . . . . . . . . . . . . . . . . . . . . . . 4
1.4 Acesseocódigodesselivro . . . . . . . . . . . . . . . . . . . . 5
1.5 Aproveitandoaomáximooconteúdo . . . . . . . . . . . . . . 5
1.6 Tirandosuasdúvidas . . . . . . . . . . . . . . . . . . . . . . . 5
2 Novo projeto com Laravel 7
2.1 Comocriarcincotelasdeumaaplicaç ãoweb? . . . . . . . . . 7
2.2 Framework,praquetequero? . . . . . . . . . . . . . . . . . . 7
2.3 Novoprojeto:Umaappdecontroledeestoque . . . . . . . . 9
2.4 Entendendoaestruturadepastas . . . . . . . . . . . . . . . . 12
2.5 AlterandoonamespacepadrãocomArtisan . . . . . . . . . . 13
2.6 Criandonossaprimeiralógica . . . . . . . . . . . . . . . . . . 14
2.7 ConflitoentrerotasdoLaravel . . . . . . . . . . . . . . . . . . 17
2.8 Antesdecontinuar . . . . . . . . . . . . . . . . . . . . . . . . . 18
3 MVC e conexão com banco de dados 19
3.1 Model-View-Controller . . . . . . . . . . . . . . . . . . . . . . 19
3.2 ColocandoMVCemprática . . . . . . . . . . . . . . . . . . . 21
3.3 Trabalhandocombancodedados . . . . . . . . . . . . . . . . 23
3.4 ConfiguraçãoeconexãocomMySQL . . . . . . . . . . . . . . 27
3.5 Parasabermais:Environment . . . . . . . . . . . . . . . . . . 30
3.6 Aondechegamoseparaondequeremosir . . . . . . . . . . . 32
vii

## Página 9

Sumário CasadoCódigo
4 Camada de modelo, migrations e seeds 33
4.1 OmodeloProduto . . . . . . . . . . . . . . . . . . . . . . . . . 33
4.2 Trabalhandocommigrations . . . . . . . . . . . . . . . . . . . 35
4.3 Apagandoatabelaprodutos . . . . . . . . . . . . . . . . . . . 38
4.4 Executandomigrações . . . . . . . . . . . . . . . . . . . . . . 38
4.5 Inserindodadosnatabelaprodutos . . . . . . . . . . . . . . . 39
5 Trabalhando com a View 45
5.1 Cadacoisaemseulugar:camadaView . . . . . . . . . . . . . 46
5.2 Consultandoosarquivosdelogdoframework . . . . . . . . 49
5.3 Incluindoparâmetrosnaview . . . . . . . . . . . . . . . . . . 52
5.4 Algunsdetalhesecuriosidades . . . . . . . . . . . . . . . . . . 53
5.5 Melhorandoaaparênciadanossalistagem . . . . . . . . . . . 55
5.6 Aondechegamoseparaondequeremosir . . . . . . . . . . . 60
6 Parâmetros da request e URL 61
6.1 Exibindodetalhesdoproduto . . . . . . . . . . . . . . . . . . 61
6.2 Enviandoparâmetrosnarequest . . . . . . . . . . . . . . . . . 67
6.3 Recuperandoparâmetrosdarequest . . . . . . . . . . . . . . 68
6.4 ConhecendoumpoucomaisdaRequest . . . . . . . . . . . . 71
6.5 URLsmaissemânticas . . . . . . . . . . . . . . . . . . . . . . 72
6.6 RecuperandoparâmetrosdaURL . . . . . . . . . . . . . . . . 73
6.7 Algunscuidadosnecessários . . . . . . . . . . . . . . . . . . . 76
7 Views mais flexíveis e poderosas 79
7.1 Blade,atemplateenginedoLaravel . . . . . . . . . . . . . . . 81
7.2 Variáveiscomblade . . . . . . . . . . . . . . . . . . . . . . . . 87
7.3 MigrandoalistagemparaBlade . . . . . . . . . . . . . . . . . 89
7.4 Loopingsemaisloopings . . . . . . . . . . . . . . . . . . . . . 90
7.5 Adicionandocondiçõesnaview . . . . . . . . . . . . . . . . . 92
7.6 Marcandoprodutosemfaltanoestoque . . . . . . . . . . . . 95
7.7 Organizandonossasviews . . . . . . . . . . . . . . . . . . . . 99
7.8 Estilizandootemplateprincipal . . . . . . . . . . . . . . . . . 103
viii

## Página 10

CasadoCódigo Sumário
8 Request e métodos HTTP 109
8.1 Criandoformuláriodenovosprodutos . . . . . . . . . . . . . 109
8.2 Criandoométodoadiciona . . . . . . . . . . . . . . . . . . . 113
8.3 InserindoosprodutosnoBD . . . . . . . . . . . . . . . . . . . 118
8.4 Retornandoumaviewdeconfirmaç ão . . . . . . . . . . . . . 118
8.5 UtilizandoosmétodosdoHTTP . . . . . . . . . . . . . . . . 123
8.6 MaismétodosHTTPequandoutilizá-los . . . . . . . . . . . 128
9 Os diferentes tipos de resposta 129
9.1 Redirecionandoparaoutraslógicas . . . . . . . . . . . . . . . 129
9.2 Maseamensagemdeconfirmaç ão?. . . . . . . . . . . . . . . 132
9.3 Recuperandovaloresdarequisiç ãoanterior . . . . . . . . . . 134
9.4 Escolhendoquaisvaloresmanter . . . . . . . . . . . . . . . . 136
9.5 Outrostiposderedirect . . . . . . . . . . . . . . . . . . . . . . 137
9.6 Parasabermais:rotasnomeadas . . . . . . . . . . . . . . . . . 138
9.7 Outrostiposderesposta . . . . . . . . . . . . . . . . . . . . . 140
10 Eloquent ORM 143
10.1 Conheçaasoluç ão:ORM . . . . . . . . . . . . . . . . . . . . . 144
10.2 TudomaissimplescomEloquent . . . . . . . . . . . . . . . . 145
10.3 BuscandopeloIDcomEloquent . . . . . . . . . . . . . . . . . 147
10.4 Migrandoainser çãodeprodutos . . . . . . . . . . . . . . . . 149
10.5 Funçãoderemoverprodutos . . . . . . . . . . . . . . . . . . . 153
10.6 CódigofinaldoProdutoController . . . . . . . . . . . . . . . 155
11 V alidando os dados de entrada 159
11.1 ValidaçãocomLaravel . . . . . . . . . . . . . . . . . . . . . . 161
11.2 ValidandocomFormRequests . . . . . . . . . . . . . . . . . . 165
11.3 UsandoFormRequestaoadicionar . . . . . . . . . . . . . . . 169
11.4 Exibindoerrorsdevalidaç ão . . . . . . . . . . . . . . . . . . . 171
11.5 Customizandoasmensagens . . . . . . . . . . . . . . . . . . . 176
11.6 Customizandomensagensdeumcampoespecífico . . . . . . 178
11.7 Boaprática:experiênciadeuso . . . . . . . . . . . . . . . . . 180
ix

## Página 11

Sumário CasadoCódigo
12 Autenticaç ão e seguranç a 183
12.1 Teladelogineautenticaç ão. . . . . . . . . . . . . . . . . . . . 183
12.2 Entendendoologindaaplicaç ão . . . . . . . . . . . . . . . . 188
12.3 Criandoumalógicadeautenticaç ão. . . . . . . . . . . . . . . 191
12.4 AutorizaçãocomMiddlewares . . . . . . . . . . . . . . . . . . 197
12.5 Registrandoomiddlewarepararotasespecíficas . . . . . . . 202
12.6 Utilizandoomiddlewarepadrão . . . . . . . . . . . . . . . . . 205
13 Mais produtividade com Artisan 207
13.1 Comolembrardetodososcomandos? . . . . . . . . . . . . . 208
14 Os próximos passos 213
x

## Página 12

Capítulo1
Introdução
1.1 O projeto e as tecnologias
Nossoprojetoserádecontroledeestoque.Comousuáriofinal,seremosca-
pazesdegerenciarosprodutosqueserãopersistidosemumbancodedados
MySQL,visualizarcomfacilidadeosqueestãoemfaltanoestoque,emais.O
contextoésimples,masseráumaboabaseparaexplorarospoderososrecur-
sosefacilidadesqueoLaraveloferece.
Aofinaldestelivro,teremosumalistagemparecidacom:

## Página 13

1.1. Oprojetoeastecnologias CasadoCódigo
Fig.1.1:Listagemcomalgunsprodutos.
Adiçãodeprodutoscomvalidaç ãodedados:
Fig.1.2:Adiçãoevalidaç ãodeprodutos.
Autenticaçãoeseguran ça:
2

## Página 14

CasadoCódigo Capítulo1. Introdução
Fig.1.3:FormuláriodeLogindaaplicaç ão.
Emuitomais,comoveremosaseguir.Umpontoimportanteéqueolivro
nãofocaráapenasnasfuncionalidadesdaaplicaç ão,massimnosconceitose
recursoscomoumtodo.Vocêentenderá,entrediversosoutros,comofunci-
onaoMVCeimportantesconceitosrelacionadosaosprojetosweb.
1.2 O que veremos durante o livro
Durantealeituraveremos:
• ComocriareconfigurarumaaplicaçãocomLaravel.
• Comoconfigurarrotasnoarquivoroutes.php.
• ComofuncionaopadrãoarquiteturalMVC,comoeleseaplicaaofra-
meworkequaissuasvantagens.
• Quaisasconfiguraçõesnecessáriasparaintegrarseuprojetowebcom
umbancodedados.
• ComoutilizarofacadeDBparaexecutarinstruçõesnobancodedados.
• ComotirarproveitodoEloquent,umpoderosoframeworkORM.Suas
vantagenseprincipaisoperações.
3

## Página 15

1.3. DownloaddoLaravel CasadoCódigo
• Comoenviarparâmetrosparaaview,redirecionarparaoutrasaçõese
recuperarparâmetrosdarequisiç ãodonavegador.
• ComodominaroBlade,ummecanismodetemplatepadrãodoLaravel,
utilizarlayoutseoperadoreslógicos.
• Serializaroresultadoemdiferentesformatos,comoJSON.
• Criarvalidaçõesdedadoseentenderoconceitode Form Requests.
• Cuidardaautenticaçãoeseguran çacom Middlewares.
• ComotirarproveitodoszilharesdecomandosdoArtisan.
1.3 D ownload do Laravel
SeaindanãotemoLaravelinstalado,vocêpodefazerseudownloadeverum
passoapassodetalhadodeinstalaç ãoemseuprópriosite:
http://laravel.com/docs/installation
Setiverqualquerproblemanoprocessodeinstalaç ão,quevaivariarde
acordocomosistemaoperacional,nãodesanime. Envieume-mailnalista
dediscussõesdesselivroquevamosajudá-lo.Oendere çoé:
https://groups.google.com/d/forum/livro-laravel
Laravel Homestead
Sepreferir,emvezdeinstalaroPHP,Laraveletodasassuasdepen-
dênciasemsuamáquinalocal,vocêpodeutilizaro Laravel Homestead
paraprepararoambientedeumaformabemsimpleseeleganteemuma
máquinavirtual.O HomesteadéumasoluçãooficialejáincluiPHP5.6,
MySQL,alémdediversosoutrosrecursosdequevocêpodeprecisarpara
desenvolveraplicaçõescompletasemLaravel. Sequiser,vocêpodeler
maisarespeitoeverinstruç ãodeinstalaç ãoeusoem:
http://laravel.com/docs/homestead
4

## Página 16

CasadoCódigo Capítulo1. Introdução
1.4 A cesse o código desse livro
Ocódigocompletodoprojetoquedesenvolveremosnodecorrerdesselivro
estádisponívelemmeurepositóriodoGitHub.Vocêpodeacessá-loem:
https://github.com/Turini/estoque-laravel
1.5 A proveitando ao máximo o conteúdo
Paratirarummaiorproveitodessaleitura,nãofiquepresoàteoria.Vocêpode
edeveacompanharolivrocomseueditorfavoritoaberto,escrevendotodoo
códigoetestesdoscapítulos.Alémdisso,eusemprerecomendoquevocêvá
alémescrevendonovostestesparasolidificaraindamaisoconhecimento.
1.6 T irando suas dúvidas
Ficoucomalgumadúvida? Nãodeixedemeenviarume-mail. Alistade
discussãoaseguirfoicriadaexclusivamenteparaestelivro:
https://groups.google.com/d/forum/livro-laravel
Essalistaéumcanaldecomunicaç ãodiretacomigoecomosdemaislei-
tores,portantofiqueàvontadeparalevantardiscussõestécnicas,apontarcor-
reções,indicarmelhoriasetc.Seufeedbackésempremuitobem-vindo.
Alémdalista,nãodeixedeconsultaradocumentaç ãodoframeworkdu-
rantetodooaprendizado.Elaébemcompletaeexplicativa:
http://laravel.com/docs/
Outrorecursoquevocêpodeutilizarparaesclarecersuasdúvidasepar-
ticiparativamentenacomunidadeéofórumdoGUJ.Lávocênãosópode
perguntar,mastambémresponder,editar,comentareassistiradiversasdis-
cussõessobreouniversodaprogramaç ão.
http://www.guj.com.br/
5

## Página 18

Capítulo2
NovoprojetocomLaravel
2.1 C omo criar cinco telas de uma aplicação
web?
Imagineumaaplicaçãoquetenhaasfun çõesdeadicionar,remover,listar,en-
viare-mail,entrediversasoutrasquesãoessenciaisparatodaaplicaç ãoweb.
Paracadauma,devemosexecutarumcódigodelógica,buscarouatualizar
informaçõesdobanco,mostrarumHTMLcomoresposta.Bastantecoisare-
petitiva,nãoé?Seráquealguémnãopodenosajudar?
2.2 Framework, pra que te quero?
Independentedalinguagemoutecnologiaqueestamosusando,umconceito
globalé: não queremos ficar nos preocupando com infraestrutura. Éaí

## Página 19

2.2. Framework,praquetequero? CasadoCódigo
queosframeworksentram. Elesnosajudamemuitoaagilizaroprocesso
dedesenvolvimento,deformaorganizada,evitandorepetiçõesdecódigoe
muitomais.
Quemnuncafoicriarumprojetonovoeacaboucopiandoaestruturade
algumoutroprojetoquejátinhacriadoantes?Issoaconteceporqueboaparte
dessaestruturaseráigual,vocênãoprecisareinventararodaacadanovopro-
jeto. Essaéumadasideiasdosframeworks,ofereceressaestruturapadrão
entreosprojetos,deformabemorganizadaefácildemanter,segundoasme-
lhorespráticasdomercado.Essareutilizaç ãodecódigoentreváriosprojetos
vailhepouparmuitotempoetrabalho.Precisaconectarcomobanco?En-
viarume-mail?Migrarseubancodedados?Vocêperceberáqueo Laravel,
assimcomodiversosoutrosframeworksdomercado,játemtudoissopronto
epré-configurado.
Aolongodesselivrovocêperceberáquenãoprecisausarframeworks,
nãoéobrigatório.Masmesmoassimvocênãovaiquerermaisviversemeles,
quenostornammuitomaisprodutivosesimplificambastanteoprocessode
desenvolvimento.
Algumas outras opções famosas
Alémdo Laravel,quevamosaprender,existemdiversasop çõesbastante
interessantesnomercado.Umadasmaispopulareséo Zend Framework 2,da
própria Zend T echnologies.Alémdele,hátambémoCodeIgniter, Symphony,
CakePHP, Phalcon,entrediversosoutros.
O Laraveléumadasmaioresapostasdaatualidade.Muitosedeveàsua
simplicidade,sintaxe,flexibilidadeericadocumentaç ão. Alémdeseusite
oficial,queéohttp://laravel.com,vocêtambémcontacombastanteconteúdo,
discussões,exemplosdecódigo,perguntaserespostasemumsitedereceitas,
ohttp://laravel-recipes.com/. Eurecomendoque,alémdolivro,vocêusee
abusedessessitesparadominarcompletamenteaferramenta.
8

## Página 20

CasadoCódigo Capítulo2. NovoprojetocomLaravel
2.3 N ovo projeto: Uma app de controle de esto-
que
Paracome çaraaprenderLaravel, vamoscriarumnovoprojetochamado
estoque.Fazerissoéverdadeiramentesimples,desdeocome çovocêjáper-
cebeasvantagensemusaroframework.Quervercomoéfácil?Sevocêjátem
oLaravelinstalado,tudoqueprecisafazerérodarocomando laravel new
peloterminal,passandoonomedoprojetoquequeremoscriar. Emnosso
casoserá:
laravel new estoque
Asaídaseráparecidacom:
Fig.2.1:Criandooprojetoviaterminal,napastaDesktop.
Otexto Application ready! Build something amazingseráexibidoepronto,
elecuidoudetodootrabalhopesado. Notequeumapastacomonomedo
projeto( estoque,nestecaso)foicriadanomesmodiretórioemquevocê
executouocomando.Elajátemtodaaestruturadepastas,algumasclassese
dependênciasconfiguradas.
9

## Página 21

2.3. Novoprojeto:Umaappdecontroledeestoque CasadoCódigo
Fig.2.2:Estruturainicialdoprojeto.
Legal,nãoé?Sevocêestáseperguntandooquesignificacadaumades-
saspastas,nãosepreocupe:embrevevamosfalarmaissobreessaestrutura
inicialeaentenderemosmaisafundonodecorrerdolivro.Logovocêestará
dominandotudoisso.Masporagora,vamosrodaroprojeto estoquepara
garantirquetudoestáfuncionandoconformeoesperado?
Normalmenteusamosopróprio Apachedoservidoremquefizermos de-
ploy,masemambientededesenvolvimento,podemosservirnossaaplicaç ão
utilizandoocomando php artisan serve,queexecutaaaplicaç ãono
servidordedesenvolvimentodoPHP.Bastarodaressecomandodedentro
dapastadoprojeto:
Fig.2.3:ExecutandoservidordedesenvolvimentodoPHPcomLaravel.
10

## Página 22

CasadoCódigo Capítulo2. NovoprojetocomLaravel
Navegando nas pastas do OS pelo terminal
Vocêpodeutilizarocomando cd(change directory)paranavegar
pelassuaspastasviaterminal.UmexemploemWindowsseria:
D:\> cd Desktop\estoque
D:\Desktop\estoque>
OmesmocomandopodeserutilizadoemumambienteUnix(Linux
ouMacOS).Paralistar,háumadiferen ça. EmWindowsutilizamoso
comando dir:
D:\Desktop\estoque> dir
// vai mostrar todos os arquivos
Porém,nosoutrossistemasqueforamcitadosocomandoserá ls.
Repare:
turini ~ $ cd Desktop/estoque
turini/Desktop/estoque ~ $ ls
// vai mostrar todos os arquivos
Considerando,portanto,quemeuprojetosechama estoqueefoi
criadodentrodapasta Desktop,paraexecutarocomandoqueiniciao
servidorvocêprecisaráexecutarosdoiscomandos:
cd Desktop/estoque/
php artisan serve
Setudocorreubem,amensagem Laravel development server
started on http://localhost:8000deveteraparecidonoseuterminal. Va-
mostestar?BastaacessaressaURLnonavegadordesuapreferência.Oresul-
tadoserá:
11

## Página 23

2.4. Entendendoaestruturadepastas CasadoCódigo
Fig.2.4:Páginadeboas-vindasdoLaravel5.
Noteque,paracriarumprojetoeexecutaroLaravel,nósnãoprecisamos
denenhumaconfiguraç ãoextra. Bastacriaroprojetoemalgunssegundos,
comocomando laravel new,esairusando! Issoémuitoconveniente
quandoestamoscome çandoumnovoprojeto.Podemosgastarnossotempo
comoquerealmenteimporta:nossasregrasdenegócio.
Precisafazeralgumaconfiguraç ãoadicional? Oframeworkfaztodoo
possívelparaquevocênãopreciseficarconfigurandonada,masemalguns
momentosissopodesernecessário.Sealgodequevocêprecisanãoestácon-
figuradopor default,comoporexemploo locale,vocêpodefazerissofacil-
mentepeloarquivodeconfiguraçõespresenteem app/config/app.php.
Quersabermaissobreessasconfiguraçõesadicionais?Talvezvocêqueira
darumaolhadanapáginadeconfiguraçõesdoframework,disponívelem:
http://laravel.com/docs/configuration
Mas,porenquanto,nãoprecisaremosdenenhumaconfiguraç ãoadici-
onalemnossoprojeto. Seeleexecutousemnenhumproblema,jáestamos
prontosparaprosseguir.
2.4 E ntendendo a estrutura de pastas
Comovimos,aocriarumnovoprojeto,diversasclassesearquivosforamcri-
ados.Oobjetivodessaestruturainicialéoferecerumpadrãoeomínimode
esforçopossívelparacome çaroseuprojeto.Issoébemlegal,masclaro,caso
preferir,vocêtambémpoderenomearasclassesemudaraestruturadepastas
12

## Página 24

CasadoCódigo Capítulo2. NovoprojetocomLaravel
paraficarcomomelhorlheagrada,oframeworknãoimpõemuitasrestrições
quantoaisso.
Durantetodoolivroconheceremosumpoucomaissobreaspastaseessa
estruturainicial,masdesdejápodemosterumabreveno çãodoquevaiem
cadalugar.Essassãoalgumasdasprincipaispastas:
•app:nelaficamseus modelos, viewse controllers,queserãobemde-
talhadosnopróximocapítulo. Empoucaspalavras,éondeboaparte
doseucódigovaificar. Elapossuiumasériedesubdiretórios,como
Commands, Console, Http, Events,entreoutros.Nãosepreocupe
ementenderosignificadodecadaumdelesagora,vamosvê-losmelhor
conformeformosprecisando.
•config:comoonomejáindica,éondeficamosarquivosdeconfigura-
çãodoseuprojeto.Sevocêprecisaralterarasconfiguraçõesdecache,
e-mail,bancodedados,entreoutras,jásabeondeencontrar.
•public:éapastapraondeseuwebservervaiapontar.Láficaoarquivo
index.php,queapontaparasuaaplicaç ão.Alémdisso,écomumco-
locarmososarquivos css, imagens, javascriptetodososdemais
arquivospúblicosnessediretório.
•vendor:éondeficao source codedoLaravel,pluginseoutrasdepen-
dências.Tudoquevocêusardeterceiros(bibliotecas,frameworksetc.)
deveficarnela.
Esseésóumpouco,claro,masjáéobastanteporagora. Vamosentrar
maisafundonesseconteúdonodecorrerdolivro,massequiseradiantar,
talvezqueiradarumaolhadanapáginadoLaravelqueexplicaessaestrutura
inicial:
http://laravel.com/docs/structure
2.5 A lterando o namespace padrão com Artisan
O namespacepadrãodetodaaplicaç ãocomLaravelé App,masémuitoco-
mumebastanterecomendadoquevocêaltereonamespaceparaonomeda
13

## Página 25

2.6. Criandonossaprimeiralógica CasadoCódigo
suaaplicação. Comofazerisso? Émuitofácil,bastarodarumsimplesco-
mandoepronto.
Prasubiroserveretestar,usamoso php artisan serve,lembra?
Esse Artisanéumaferramentadelinhadecomandojáinclusanoframework.
Elanosofereceumasériedecomandosúteisparatornarnossodesenvolvi-
mentomaisprodutivo.
Paramudaro namespace,porexemplo,podemosusaro php artisan
app:name. Vamosmudá-loparaestoque,queéonomedoprojeto. Basta
executaroseguintecomandopeloterminal,dentrodapastadeseuprojeto:
php artisan app:name estoque
Asaídaseráparecidacom:
Fig.2.5:AlterandoonamespacecomArtisan.
Tudopronto, namespacealterado!
2.6 C riando nossa primeira lógica
AgoraquejáconhecemosumpoucomaissobreoLaravel,queremosensiná-
locomoqueremosqueelereajaquandoalguémacessardeterminadaURL,
istoé,criarasnossasprópriasrotas.Masquãocomplicadoéfazerisso?
Quandoacessamoshttp://localhost:8000/,ouseja,aURL /danossaapli-
cação,emalgumlugarfoiconfiguradoqueapáginapadrãodoLaraveldeveria
serexibida,nãoé?Essetrabalhoéfeitonooarquivo routes.php,quefica
dentrodapasta app/Http/.Abraoarquivoparaconferirseuconteúdo,que
deveestarparecidocom:
14

## Página 26

CasadoCódigo Capítulo2. NovoprojetocomLaravel
<?php
// comentário omitido
Route::get(’/’, ’WelcomeController@index’);
Route::get(’home’, ’HomeController@index’);
Route::controllers([
’auth’ => ’Auth\AuthController’,
’password’ => ’Auth\PasswordController’,
]);
IssopodemudardeacordocomaversãodoLaravelquevocêestiveruti-
lizando.Naversão5.1,porexemplo,oconteúdoserá:
<?php
// comentário omitido
Route::get(’/’, function () {
return view(’welcome’);
});
Comovocêpodever,elejávemcomalgumasrotasconfiguradas,como
a /quenoslevaparaapágina defaultdoLaravel. Ocódigopodeparecer
diferentenocome ço,masnãoécomplicado. Vamosentenderemdetalhes
cadalinhadecódigodessearquivo,masantesdisso,apaguetodoessecódigo
paracriarmosnossaprópriarota. Queacha? Ébemfácil,bastadeixarseu
arquivovazio,sócomatagdophp:
<?php
// nosso código vai aqui
Eagora,usaro Route:getparadefinirumanovarota.Podemosfazer
algocomo:
<?php
15

## Página 27

2.6. Criandonossaprimeiralógica CasadoCódigo
Route::get(’/’, function()
{
return ’Primeira lógica com Laravel’;
});
Sucesso,jácriamosnossaprimeirarota. Vamosentenderoqueaconte-
ceu?
Usamosométodoestático get,daclasse Route,passandodoisparâme-
tros.Oprimeiroéarota(caminho,ou path comocomumenteéchamado)
queseráacessadopelonavegador.Osegundoparâmetroéumafun çãocoma
respostaquedeveráserenviada.Empoucaspalavras,essecódigoensinaque,
quandoalguémacessaraURL /,oLaraveldeveretornarotexto Primeira
lógica com Laravel paraonavegador.
Vamostestar? Bastarodarocomando php artisan serve parasu-
bir o servidor novamente (caso ainda não esteja startado) e acessehttp:
//localhost:8000/emseunavegador.Vejaaresposta:
Fig.2.6:PrimeiralógicacomLaravel.
Perfeito,otextofoiexibidononavegador!Mandamosumtextocomum,
maspodemosrespondercomqualquerHTMLválido. Porexemplo,envol-
vendoessetextoemum h1paraterumdestaquemaiornapágina:
<?php
Route::get(’/’, function()
{
return ’<h1>Primeira lógica com Laravel</h1’;
});
16

## Página 28

CasadoCódigo Capítulo2. NovoprojetocomLaravel
Vocênãoprecisarestartaroservidor,bastaacessarapáginanovamente
paraveroresultado:
Fig.2.7:Respostacomtaghtml.
2.7 C onflito entre rotas do Laravel
Éimportanteperceberdesdejáquevocêpodecriarquantasrotasquiserno
arquivo routes.php:
<?php
Route::get(’/’, function()
{
return ’<h1>Primeira lógica com Laravel</h1’ ;
});
Route::get(’/outra’, function()
{
return ’<h1>Outra lógica com Laravel</h1’;
});
Agoratemosduasrotas,umaparaaURL /eoutrapara /outra.Mas
oqueaconteceriaseasduasfossemregistradasnamesmaURL?Na /,por
exemplo.
<?php
Route::get(’/’, function()
{
return ’<h1>Primeira lógica com Laravel</h1’ ;
17

## Página 29

2.8. Antesdecontinuar CasadoCódigo
});
Route::get(’/’, function()
{
return ’<h1>Outra lógica com Laravel</h1’;
});
Tenterodaressecódigoparaveroresultado,asegundarotavaisobres-
creveraprimeiraeotexto Outra lógica com Laravel seráexibido.Ou
seja,emcasodeambiguidadesempreaúltimarotaéquemseráregistrada.Há
outrasformasdelidarcomambiguidade,comoquandousamosdiferentes
métodosHTTP,masentraremosnesseassuntoumpoucomaisàfrente.
2.8 A ntes de continuar
Sequiserpraticarumpoucomais,eurecomendoquecrieoutrasrotasenovos
testesantesdeseguirparaopróximocapítulo.Nãosepreocupeementender
aspartesqueaindanãovimos,ok?Foqueapenasnesteconteúdoinicial.Ficou
comqualquerdúvida?Nãodeixedeperguntar!Lembre-sequeumgrupode
discussõesfoicriadoespecialmenteparaestelivro:
https://groups.google.com/d/forum/livro-laravel
Agoraquejásabemosoessencial,podemospartirparaasregrasdene-
góciodonossosistemadeestoque.Estápreparado?
18

## Página 30

Capítulo3
MVCeconexãocombancode
dados
3.1 M odel-View-Controller
Reparenovamentenaformacomofizemospararegistrarnossaprimeiraló-
gica:
Route::get(’/’, function()
{
return ’<h1>Primeira lógica com Laravel</h1> ’;
});
Oproblemadedefinirasrotasdessaforma,comocódigoderesposta
implementadodiretamenteemuma função anônima,équenãoestamosse-

## Página 31

3.1. Model-View-Controller CasadoCódigo
guindonemumpoucoasboaspráticasdaorientaç ãoaobjetos.Ocódigofica
todoespalhado,difícildemanterereutilizar.
Conformenossaaplicaç ãoforcrescendo,vamosprecisarfazeracessoao
bancodedados,executarlógicascomnossasregrasdenegócioetc.Tudoisso
ficarádentrodomesmoarquivo route.php? Seriaumabagun ça! Além
disso,vamosmisturarnossalógicadenegóciocomnossalógicadeapresen-
tação,oHTMLderesposta.
Precisamosdeumaformamelhordedividirasresponsabilidadesdenossa
aplicação.Éaíqueentrao MVC,ou Model View Controller.
Agrandeideiadessepadrãoarquiteturaléquevocêseparesuasregras
denegócioem3camadas,cadaumacomsuaresponsabilidademuitobem
definida:
•Modeléacamadaondeficamnossasregrasdenegócio,nossasentida-
deseclassesdeacessoaobancodedados.
•Viewéaresponsávelporapresentaraspáginaseoutrostiposdere-
sultadoparaousuário(oumesmoparaoutrossistemas,quesecomu-
nicam). Éarespostaqueoframeworkenviaparaonavegador,que
normalmenteéumHTML.
•Controlleréquemcuidadereceberasrequisiçõeswebedecidiroque
fazercomelas.Nessacamadadefinimosquais modelosdevemserexe-
cutadosparadeterminadaaç ãoeparaqual viewvamosencaminhara
resposta.Emoutraspalavras,essacamadaquemfazolinkentretodas
asoutras.
Diversosframeworks,dasmaisdiferenteslinguagens,seguemessepadrão
doMVC.ComLaravelnãoédiferente,ofluxoficaassim:
20

## Página 32

CasadoCódigo Capítulo3. MVCeconexãocombancodedados
Fig.3.1:FluxodoMVCcomLaravel.
Repareque,quandonossoclienteenviaumarequisiç ãopelonavegador,
primeiramentetemosumarquivoPHP,queéo routes.php,queestáfrente
detodos.Elecuidadeatenderasrequisiçõeseenviá-lasparaolocalcorreto,
nocasoosnossoscontrollers. Oscontrollers,porsuavez,decidemoque
fazercomasrequisições,passandopelacamadademodel(quefazemacesso
aobanco,executamasregrasdenegócioetc.)elogoemseguidadelegampra
viewqueseráexibidacomorespostanonavegadordocliente.
Agoraquejásabemosumpoucodateoria,vamoscolocaroMVCem
prática?
3.2 C olocando MVC em prática
Emvezdedefinirtodasaslógicasdonossosistemanessearquivoúnico,o
routes.php,vamosorganizá-lasdesdeoinícioem Controllersdistintos.
Nossosistemadeestoquesvaiterumapáginaprincipal,comalistagemde
produtos.Podemoscome çarporela.
Vamoscriarumnovoarquivochamado ProdutoController,dentro
dapasta app/Http/Controllers,queéodiretóriopadrãoparaessetipo
declasse.Dentrodocontroller,crieummétodochamado lista.Oarquivo
ProdutoController.phpficaráassim:
<?php namespace estoque\Http\Controllers;
class ProdutoController {
21

## Página 33

3.2. ColocandoMVCemprática CasadoCódigo
public function lista(){
// nosso código vai aqui
}
}
Noteque,comoestamostrabalhandocomumaestruturadediretórios,
tivemosquedefiniro namespacenocabe çalhodoarquivo. Outraregraim-
portanteéquetodocontrollerdoLaraveldeveherdardeumaclassecha-
mada Controller,quefoicriadaautomaticamentejuntocomnossopro-
jeto.Paraisso,sóprecisamosadicionar extends Controller nadeclara-
çãodanossaclasse,queficaráassim:
<?php
class ProdutoController extends Controller {
public function lista(){
// nosso código vai aqui
}
}
Aclasse Controllerexisteexclusivamenteparaquesejapossívelde-
finirmoslógicasemcomumquepodemsercompartilhadasentretodosos
controllerdenossaaplicaç ão.Alémdisso,elajátrazalguns imports( uses)
essenciaisparaoscontrollers,queserãodetalhadosconformeformospreci-
sando.
Inicialmente,vamosfazerométodo listaretornarumHTMLpuro,
comocabe çalhodalistagemdeprodutos.Ocódigoficaráassim:
<?php
class ProdutoController extends Controller {
public function lista(){
return ’<h1>Listagem de produtos com Laravel</h1>’;
}
}
Eagoraquetemosessecomportamentodefinidonocontroller,vamos
criarumarotaparaelenoarquivo routes.php,quecontinuaresponsá-
22

## Página 34

CasadoCódigo Capítulo3. MVCeconexãocombancodedados
velpeloregistrodenossasrotaseoutrasconfigurações,masadiferen çaéque
agoraeleapenasapontaráparaométododocontrollerquedeveserexecu-
tado.
Oarquivoderotasdeveficarassim:
<?php
Route::get(’/produtos’, ’ProdutoController@lista’);
// demais rotas omitidas
Notequeopadrãoéonomedocontroller,seguidodeum @eonome
dométodo.Agoraquandoumarequisiç ãoforfeitaparaaURL /produtos,
ométodo listado ProdutoControllerseráexecutado.Bemsimples,
nãoacha?
Vamostestar?Bastaacessar http://localhost:8000/produtosemseunave-
gador.
Fig.3.2:Iníciodalistagemdeprodutos.
Sucesso,oHTMLderespostafoiexibidoconformeesperado.
3.3 T rabalhando com banco de dados
Alistagemaindaestámuitosimples,aindaestamosmostrandoapenasum
textoondequeremosmostrartodososprodutos.Nossoobjetivoagoraserá
23

## Página 35

3.3. Trabalhandocombancodedados CasadoCódigo
buscaressasinformaçõesdeumbancodedados,comoénaturalnasaplica-
çõesdodiaadia.
Iniciando com MySQL
UsaremosobancodedadosMySQLemnossoprojeto,jáqueéumdos
bancosdedadosrelacionaismaisutilizadosnomercado,égratuitoebastante
simplesdeinstalar. SevocêaindanãotemoMySQLinstalado,podefazer
downloadpelolink:
http://dev.mysql.com/downloads/mysql/
Fig.3.3:PáginadedownloaddoMySQL.
Aofinaldapágina,vocêencontraráumcampoparaescolherseusistema
operacional.Selecioneedepoiscliqueemdownload,naop çãoquepreferir:
24

## Página 36

CasadoCódigo Capítulo3. MVCeconexãocombancodedados
Fig.3.4:Selecionandoop çãodedownloaddeacordocomosistemaoperaci-
onal.
Nomesmosite,vocêencontraumtutorialdeinstalaç ãodeacordocomo
seusistemaoperacional.Ouvocêpodeacessarotutorialdiretamenteem:
http://dev.mysql.com/doc/refman/5.7/en/installing.html
ApósbaixareinstalaroMySQL,vamosnoslogarnoMySQLecriarabase
dedados(database)denossoprojeto.Oprimeiropassoébemsimples,tudo
quevocêprecisafazerparaselogaréabrirseuterminaledigitar:
mysql -u SEU_USUARIO -p SUA_SENHA
Comoemmeucasoousuárioé rooteeunãotenhoumasenha,só
precisofazer:
mysql -u root
25

## Página 37

3.3. Trabalhandocombancodedados CasadoCódigo
Fig.3.5:TelainicialdoMySQLCommandLine
MySQL Command Line ou Workbench?
Háquemprefirautilizaro MySQL Workbench,queéumaferramenta
visual.Pelasimplicidade,nosexemplosdolivrovamosutilizaro MySQL
Command Line. Nele,nósexecutamosasinstruçõesdiretamentepela
linhadecomando,noterminal.
Setiverqualquerdificuldadeparainstalarouexecutaroscomandos,
nãopenseduasvezesantesdemandarume-mailparalistadestelivro.
Agoraquejáestamoslogados,podemoscriarumanova databasecha-
mada estoque_laravel.Issopodeserfeitocomocomando:
create database estoque_laravel;
Apósexecutá-lo,asaídadeveserparecidacom:
Query OK, 1 row affected (0.00 sec)
Perfeito,játemosobanco.Paraevitarquevocêtenhaquecriartodasas
tabelasecadastraralgumasinformaçõesmanualmentenessemomento,va-
mosimportaroarquivo dump.sqlcomalgunsprodutosjácadastradosem
26

## Página 38

CasadoCódigo Capítulo3. MVCeconexãocombancodedados
umatabeladeprodutos. Nãosepreocupe,muitoembrevesubstituiremos
esse dumpcomrecursosoferecidospeloLaravel.Umarquivode dumpéum
arquivodetextocominstruçõesSQL,comos insertsdedadosouatémesmo
comasinstruçõesdecriaç ãodetabelas.
Criando seu próprio dump
Sequisersabermaissobreessearquivode dump,oumesmocriaro
seupróprio,vocêpodedarumaolhadanolink:
http://dev.mysql.com/doc/refman/5.0/en/mysqldump-sql-format.
html
Issopodeserbemútilquandoqueremosfazer backupsdeseguran ça
denossasbasesdedados.
Façaodownloaddo dump.sqlnesselink:
http://bit.ly/1BKZMgo
Feitoisso,tudoqueprecisamosfazerparaimportaresse dumpemnosso
bancodedadoséexecutaraseguinteinstruç ãonoterminal:
mysql -uroot estoque_laravel < CAMINHO_COMPLETO_PARA_O_DUMP
Parafacilitaroprocesso,vocêpodecopiaroarquivo dump.sqlparaa
pastaraizdeseuusuário,eexecutarapenas:
mysql -uroot estoque_laravel < dump.sql
Ótimo!Jápodemosdaropróximopasso.
3.4 C onfiguração e conexão com MySQL
Agora que já temos o banco instalado e configurado, nosso objetivo
será estabelecer uma conexão com o MySQL. O Laravel torna essa ta-
refabemfácil,bastaadicionarasinformaçõesdonossobanconoarquivo
config/database.php.Elejávempré-configuradonoprojeto,sópreci-
samosmudarotrechodecódigodoMySQL,quedeveestarassim:
27

## Página 39

3.4. ConfiguraçãoeconexãocomMySQL CasadoCódigo
’mysql’ => [
’driver’ => ’mysql’,
’host’ => env(’DB_HOST’, ’localhost’),
’database’ => env(’DB_DATABASE’, ’forge’),
’username’ => env(’DB_USERNAME’, ’forge’),
’password’ => env(’DB_PASSWORD’, ’’),
’charset’ => ’utf8’,
’collation’ => ’utf8_unicode_ci’,
’prefix’ => ’’,
’strict’ => false,
],
Nocampodatabaseusaremos estoque_laravel,usuário rootese-
nhavazia.CasoseuMySQLtenhaumusuárioousenhadiferente,bastasubs-
tituirovalordessescampos.Otrechodeconfiguraç ãodoMySQLnoarquivo
database.phpficaráassim:
’mysql’ => [
’driver’ => ’mysql’,
’host’ => env(’DB_HOST’, ’localhost’),
’database’ => env(’DB_DATABASE’, ’estoque_laravel’),
’username’ => env(’DB_USERNAME’, ’root’),
’password’ => env(’DB_PASSWORD’, ’’),
’charset’ => ’utf8’,
’collation’ => ’utf8_unicode_ci’,
’prefix’ => ’’,
’strict’ => false,
],
Pronto, isso é tudo que precisamos configurar para acesso ao banco
de dados. Vamos testar? Uma forma simples, porém bem manual,
de rodar SQLs pelo Laravel é utilizando a classeDB, presente em
Illuminate\Support\Facades\DB.Elatemumasériedemétodospara
nosajudararealizaroperaçõesnobancodedados,como select, insert
etc.
Quervercomoésimples?Parabuscartodososregistrosdatabelaprodu-
tos,bastautilizarométodo selectcomaSQLdeconsulta:
$produtos = DB::select(’select * from produtos’);
28

## Página 40

CasadoCódigo Capítulo3. MVCeconexãocombancodedados
Nossocontrollerficaráassim:
<?php namespace estoque\Http\Controllers;
use Illuminate\Support\Facades\DB;
class ProdutoController extends Controller {
public function lista(){
$produtos = DB::select(’select * from produtos’);
return ’<h1>Listagem de produtos com Laravel</h1>’;
}
}
Todososvaloresdosprodutosdobancodedadosserãoretornadosem
um array,quechamamosde $produtos.Vamosgarantirqueissoestáfun-
cionando?Podemosmudarométodo listapara concatenaronomeedes-
criçãodecadaumdosprodutosnastringderesposta.Ocódigoficaráassim:
<?php namespace estoque\Http\Controllers;
use Illuminate\Support\Facades\DB;
class ProdutoController extends Controller {
public function lista(){
$html = ’<h1>Listagem de produtos com Laravel</h1>’;
$html .= ’<ul>’;
$produtos = DB::select(’select * from produtos’);
foreach ($produtos as $p) {
$html .= ’<li> Nome: ’. $p->nome .’,
Descrição: ’. $p->descricao .’</li>’;
}
29

## Página 41

3.5. Parasabermais:Environment CasadoCódigo
$html .= ’</ul>’;
return $html;
}
}
Achouocódigofeio?Entãosomosdois!Masnãosepreocupecomisso,
logoeleserámelhorado,onossoobjetivoagoraégarantirqueaconexãocom
obancodedadosfoiestabelecidacorretamente.Comojátemosalgunspro-
dutoscadastradospelo dump,aoacessar http://localhost:8000/produtoso
resultadodeveráserparecidocom:
Fig.3.6:Listadeprodutoscomregistrosdobanco.
Excelente,comquasenenhumaconfiguraç ãojáconseguimosnosconec-
tareexecutarconsultasnobancodedados!
3.5 P ara saber mais: E nvironment
Vocêprovavelmentepercebeuqueadicionamosasconfiguraçõesdebancode
dadoscomosegundoparâmetrodeummétodo env,diretamentenoarquivo
de database.php.
’database’ => env(’DB_DATABASE’, ’estoque_laravel’),
’username’ => env(’DB_USERNAME’, ’root’),
’password’ => env(’DB_PASSWORD’, ’’),
30

## Página 42

CasadoCódigo Capítulo3. MVCeconexãocombancodedados
Masquandooprojetoestiverpronto,nãovamosquererusaressesdados
emprodução.Porumaquestãodeseguran ça,éimportantíssimoqueobanco
deproduçãotenhaumasenha,equeelafiqueprotegida. Alémdisso,não
queremosqueosdesenvolvedoresusemobancodedadosdeproduç ãopara
fazeremseustestesfuturos.Éaíqueentraométodo env.
OLaravelpossuiumrecursoconhecidocomo Environment,quenospos-
sibilitadefinirumconjuntodeconfiguraçõesdepodemmudardeacordocom
oambientedeexecuç ão,comoocasodobancodedados.
Vejaqueseuprojetojápossuiumarquivo .env.example,presenteno
diretórioraiz.Dentrodelevocêencontrará,entreoutrasop ções,aslinhas:
DB_HOST=localhost
DB_DATABASE=homestead
DB_USERNAME=homestead
DB_PASSWORD=secret
Ométodo env,utilizadonoarquivo database.php,primeiroprocura
pelaconfiguraçãodefinidanoarquivode environmente,casonãoencontre,
utilizaosegundovalorquepassamos.Emoutraspalavras,sequisermosqueo
Laravelpasseautilizarasconfiguraçõesdeproduç ãoemvezdosvaloresfixos
passadosparaoarquivodatabase,tudooqueprecisamosfazerécriarum
arquivo .envcomessasconfigurações. Sevocêestiverutilizandoaversão
maisnovadoLaravel,elejáexistirá.Bastaadicionaroconteúdo:
DB_HOST=meuprojeto.com.br
DB_DATABASE=estoque_producao
DB_USERNAME=production
DB_PASSWORD=uma_senha_super_hiper_secreta
Mascuidado.Essearquivoteráinformaçõesimportantesdeseuambiente
deprodução,comoasenhadobancodedados.Ébastanterecomendadoque
vocênãodeixeessearquivonoprojeto ou commitnorepositório,casoesteja
utilizandoalgumaferramentadecontroledeversãocomoogit. Sequiser,
vocêpodevermaisdetalhessobreessafuncionalidadeem:
http://laravel.com/docs/configuration#environment-configuration
31

## Página 43

3.6. Aondechegamoseparaondequeremosir CasadoCódigo
3.6 A onde chegamos e para onde queremos ir
Comumpoucodeteoriaeprática,osignificadodopadrãoMVCcome çaa
fazersentido.Comovimos,emvezdedeixartodasasresponsabilidadesno
arquivoderotas,cadacomportamentopodeficarmuitobem encapsuladoem
seudevidocontroller.Asvantagenssãoinúmeras,maspramimasprincipais
são:
•Legibilidade:poisemvezdeterváriasfun çõesanônimaseinúmeras
linhasdecódigoemummesmoarquivo,tudoficamuitobemdistri-
buído.Cadacomportamentoemseudevidolugar,emclasseseméto-
doscomnomesbemdefinidos.
•Manutenibilidade:poissetudoestábemorganizadoeencapsulado,
nãoprecisaremosmexeremumarquivocom1500linhassempreque
umproblemaaparecer. Alistagemdeprodutosparoudefuncionar?
Seiquetenhoqueiraummétododo ProdutoController. Não
consigo adicionar usuários? Sei que tenho que verificar na classe
UsuarioController.
Viusó? Issonadamaisédoquebomusodaorientaç ãoaobjetos,que
cadavezmaisfazparteeinfluenciaoPHPeseusframeworks.
Masespera,nossocódigoaindanãoobedeceoprincípiodas3camadas
doMVC,porenquantotodootrabalhoestásendofeitonacamadacontroller!
Issonãoébom,vamosresolver?
32

## Página 44

Capítulo4
Camadademodelo,migrationse
seeds
Atéentãousamosum dumpdobancodedadosparaimportaratabelapro-
dutosealgunsdadosprontos,mas,aocriarumnovoprojeto,nemsempre
teremosessasinformaçõesprontas,nãoé? Nestecapítuloveremoscomoo
Laravelpodeajudarnessetrabalho,criandotodasessasinformaçõesdozero,
semtermosquenospreocuparemacessarobancodedadoseexecutaresses
create tablese insertsnamão.
4.1 O modelo Produto
Nossoprimeiropassoserácriarumaclassede modeloque represente nossa
tabela de produtosdobancodedados.Algobemsimples,como:

## Página 45

4.1. OmodeloProduto CasadoCódigo
<?php namespace estoque;
use Illuminate\Database\Eloquent\Model;
class Produto extends Model {
}
Vejaquenossaclasse Produtoprecisaherdarde Model,masnãose
preocupecomissoporenquanto,embreveentenderemosomotivoeganhos
dessaheran ça.
Masespera,achatrabalhosodigitaressaslinhaspracriaraclassenamão?
Quetaldeixaro Artisanfazerissopravocê?Issomesmo,o Artisanfazmuito
maisdoquesubiroservidor,eletemumasériederecursosqueexploraremos
nodecorrerdolivro.Umdeleséo make:model,quecriarátodaaestruturada
classedemodeloparavocê.Reparecomoésimples:
php artisan make:model Produto
Apósexecutaressecomando,aclasseserácriadaautomaticamente:
Fig.4.1:ComandodoArtisanparacriaç ãodemodelos.
Tudopronto,procurepelaclasse Produtodentrodapasta appdeseu
projeto,elaestaráassim:
<?php namespace estoque;
use Illuminate\Database\Eloquent\Model;
34

## Página 46

CasadoCódigo Capítulo4. Camadademodelo,migrationseseeds
class Produto extends Model {
//
}
Legal,nãoé?AténissooLaravelnosajuda.Ocomando php artisan
make:modeléopcional,claro,masmuitoútilemnossodiaadia. Vocêsó
precisapassaronomedaclasseetodoocódigopadrãoserácriadoparavocê,
assimemnenhummomentoprecisaremosnospreocuparemlembrardeher-
darde Model,adicionaro importe namespacedosnossosmodelos.
Apartirdeagora,aclasse Produtorepresentaráatabela produtosque
serácriadanobancodedados. Masemquallugarissofoiconfigurado? A
respostaé:emnenhum.Quandonãodefinimosexplicitamente,oframework
assumequeatabelateráonomedaclassecomletraminúsculaenoplural.
Nessecaso,aclasse Produtoserávinculadaàtabela produtos.
Massevocêpreferir,oumesmoprecisar,tambémépossívelconfigurar
issoexplicitamente.Bastaadicionaremnossomodeloumapropriedadecom
visibilidade protected,chamada table:
<?php namespace estoque;
use Illuminate\Database\Eloquent\Model;
class Produto extends Model {
protected $table = ’produtos’;
}
4.2 T rabalhando com migrations
Se você estiver utilizando a versão 5.0 do Laravel, além da
classe Produto, um arquivo de migração (migration) chamado
2015_05_25_151007_create_produto_table foi criado. A partir
daversão5.1,elenãoécriadoautomaticamente;logo,vocêprecisaráexecutar
ocomandocomoargumento -m:
php artisan make:model Produto -m
35

## Página 47

4.2. Trabalhandocommigrations CasadoCódigo
EssearquivoseráoresponsávelporensinaraoLaravelcomocriar,atua-
lizarourecuperaroestadoanteriordoesquemadeseubancodedados. Mi-
grations,oumigrações,trabalhamcomoumcontroledeversãodoseubanco
dedados.Vejaque,inclusive,onomedoarquivodemigraç ãocome çacom
adataemqueelafoicriada,poisassimoLaravelsaberáexatamenteaordem
emqueelasdevemserexecutadas.
Ao abrir esse arquivo de migração, que por padrão será cri-
ado na pasta database/migrations, veremos que uma classe
CreateProdutosTablefoicriadacomoseguinteconteúdo:
<?php
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;
class CreateProdutosTable extends Migration {
/**
* Run the migrations.
*
* @return void
*/
public function up()
{
Schema::create(’produtos’, function(Blueprint $table)
{
$table->increments(’id’);
$table->timestamps();
});
}
/**
* Reverse the migrations.
*
* @return void
*/
public function down()
{
36

## Página 48

CasadoCódigo Capítulo4. Camadademodelo,migrationseseeds
Schema::drop(’produtos’);
}
}
Essaclasse,queherdade Migration,terádoismétodosimportantíssi-
mos. Oprimeiro( up)ensinacomocriaratabelaproduto,enquantoose-
gundo( down)mostracomodesfazê-la,ouseja,fazerum rollback.
Porém,repareque,nométodo up,apenaso ide timestampdatabela
sãodefinidos. Queremosque,alémdisso,umprodutotenha nome, valor,
descricaoe quantidade,portantoadicionaremosessasasinformaçõesaseguir:
public function up()
{
Schema::create(’produtos’, function(Blueprint $table)
{
$table->increments(’id’);
$table->string(’nome’);
$table->decimal(’valor’, 5, 2);
$table->string(’descricao’);
$table->integer(’quantidade’);
$table->timestamps();
});
}
Utilizamosométodo stringparaoscamposdetexto, integerpara
aquantidadee decimalparaovalordoproduto. Existemdiversasoutras
opções,como dateparadatas, timeparahora,entreoutros.Vocêpodever
umarelaçãocompletadosmétodosdesse builderem:
http://laravel.com/docs/schema#adding-columns
Comisso,nossamigraç ãoestápronta,ométodo upfornecetodasas
informaçõesnecessáriasparaqueoLaravelsaibacriaratabelaprodutos,eo
método downensinaaoframeworkcomodesfazeressaalteraç ão,quenesse
casoseráapagandoatabela:
public function down()
{
Schema::drop(’produtos’);
}
37

## Página 49

4.3. Apagandoatabelaprodutos CasadoCódigo
4.3 A pagando a tabela produtos
Agoraquejátemosumamigraç ãoparafazeressetrabalho,vamosapagara
tabeladeprodutosjáexistenteemnossobancodedados. Paraisso,basta
acessaro MySQLeexecutarainstruç ão:
DROP TABLE produtos;
Tudopronto. Acessaralistagemdeprodutospelonavegadoragorare-
sultariaemumerro,claro. Paraqueocódigovolteafuncionarprecisamos
executaramigraç ãodecriaç ãodatabela.Mascomo?
4.4 E xecutando migrações
Executaruma migrationéumatarefaextremamentesimples. Ocomando
php artisan migrate équemfarátodootrabalho. Aoexecutá-lo,te-
remoscomoresultadoalgocomo:
Migration table created successfully.
Migrated: 2014_10_12_000000_create_users_table
Migrated: 2014_10_12_100000_create_password_resets_table
Migrated: 2015_05_25_151007_create_produtos_table
Vejaque,alémdenossamigraç ãodeprodutos,umamigraç ãodecriaç ão
deusuárioseresetdesenhafoiexecutada. Essasmigraçõesforamcriadas
automaticamentejuntocomoprojeto,paraafuncionalidadedeautenticaç ão
queveremosmaisàfrente.
Vamosconferiroresultado? Bastaacessarobancodedadosdoprojeto
econferiraestruturadatabelaquefoicriada.Podemosfazerissocomoco-
mando descdo MySQL.
mysql> desc produtos;
Oresultadoserá:
38

## Página 50

CasadoCódigo Capítulo4. Camadademodelo,migrationseseeds
Fig.4.2:Estruturadatabelaprodutosnobancodedados.
Excelente,játemosatabelaprodutoscomtudoqueprecisamos.
E quanto ao rollback?
Eventualmentesurgiráanecessidadededesfazerumamigraç ão,seja
porumerrodedigitaç ãoemalgumdeseuscampos,adicionaralguma
informaçãooualgodotipo. Sevocêacaboudeexecutarocomando
migrateeviuquealgumacoisanãosaiucomoesperado,bastaexecutar
um php artisan migrate:rollback queaultimamigraç ãoserá
desfeita.Legal,nãoé?Mascuidado.Muitasvezesserámaisinteressante
criarumanovamigraç ãocomasmudan ças,emvezdesairdesfazendoas
últimasmigraçõesexecutadas.Lembre-seque,casoalgumainformaç ão
játenhasidoinseridanatabela,aofazer rollbackelaseráperdida.
Vocêpodecriarquantasmigraçõesquisercomocomando:
php artisan make:migration NOME_DA_MIGRATION
4.5 I nserindo dados na tabela produtos
Ocódigovoltaráafuncionar,porém,aoacessaralistagemdeprodutosno-
vamentepelonavegador,nenhumdadoseráexibido. Éoesperado,afinal,
apagamosatabeladeprodutosanteriorecriamosumanova.
39

## Página 51

4.5. Inserindodadosnatabelaprodutos CasadoCódigo
Embreveimplementaremosafun çãodeadicionarnovosprodutos,mas
enquantoissopodemosinseriralgunsprodutosmanualmentenobancode
dados. Umaformasimplesdefazerissoseriaacessandoo MySQLeexecu-
tandodiretamenteos inserts,masveremosumaformaaindamaisinteressante
eautomatizada,comumnovorecursodoLaravelchamado Seed.
Aideiaésimples,um seederéumaclassequepopulaseubancodeda-
doscomalgumasinformaçõesiniciais normalmenteinformaçõesdetestes.
Todaamágicaacontecedentrodeumaclassechamada DatabaseSeeder,
presentenodiretório database/seeds.Quandofizemosumnovoprojeto,
essaclassefoicriadacomoseguinteconteúdo:
<?php
use Illuminate\Database\Seeder;
use Illuminate\Database\Eloquent\Model;
class DatabaseSeeder extends Seeder {
/**
* Run the database seeds.
*
* @return void
*/
public function run()
{
Model::unguard();
//$this->call(’UserTableSeeder’);
}
}
Notequeháumalinhacomentadacomoexemplodecomoexecutarum
seeder,comauxíliodométodo call.
Criando o ProdutoTableSeeder
Vamos agora criar umseeder que deverá inserir alguns dados na
tabela produtos. A princípio o código pode parecer estranho, mas é
40

## Página 52

CasadoCódigo Capítulo4. Camadademodelo,migrationseseeds
verdadeiramente simples. Assim como o DatabaseSeeder, nosso
ProdutoTableSeederdeveherdardaclasse Seedereimplementarseu
método run,comoaseguir:
class ProdutoTableSeeder extends Seeder {
public function run()
{
// código vai aqui
}
}
Nadademais,nãoé? Comoporpadrãoo DatabaseSeedernãovem
com namespace,éumapráticamuitocomumdefinirmosos seedersdentrode
ummesmoarquivo.Portanto,ocódigoficaráassim:
<?php
use Illuminate\Database\Seeder;
use Illuminate\Database\Eloquent\Model;
class DatabaseSeeder extends Seeder {
/**
* Run the database seeds.
*
* @return void
*/
public function run()
{
Model::unguard();
//$this->call(’UserTableSeeder’);
}
}
class ProdutoTableSeeder extends Seeder {
public function run()
41

## Página 53

4.5. Inserindodadosnatabelaprodutos CasadoCódigo
{
// código vai aqui
}
}
Ótimo,agorasófaltaadicionarmosalgunsdados!Assimcomousamoso
DB:selectparafazerum selectnobancodedados,podemosusarum
DB:insertparafazerumainser ção.Ocódigoficaráassim:
class ProdutoTableSeeder extends Seeder {
public function run()
{
DB::insert(’insert into produtos
(nome, quantidade, valor, descricao)
values (?,?,?,?)’,
array(’Geladeira’, 2, 5900.00,
’Side by Side com gelo na porta’));
DB::insert(’insert into produtos
(nome, quantidade, valor, descricao)
values (?,?,?,?)’,
array(’Fogão’, 5, 950.00,
’Painel automático e forno elétrico’));
DB::insert(’insert into produtos
(nome, quantidade, valor, descricao)
values (?,?,?,?)’,
array(’Microondas’, 1, 1520.00,
’Manda SMS quando termina de esquentar’));
}
}
Nãosepreocupeementendero DB:insertporenquanto,voltaremos
afalarsobreessemétodomuitoembreve.Oqueimportanessemomentoé
que,emvezdeexecutarmos3insertsnobancodedadosmanualmente,dei-
xamosessecódigoisoladoemumaclasseresponsávelporfazeressetrabalho
paranós.Oganhoéque,emqualquerambiente,podemosexecutaresse seed
42

## Página 54

CasadoCódigo Capítulo4. Camadademodelo,migrationseseeds
parainseriralgunsdadosnatabeladeprodutossemprequequisermos.Legal,
nãoé?Sófaltamdoisdetalhesparaqueocódigofiquecompleto.Oprimeiro
éadicionaro importdaclasse DB,assimcomofizemosnocontrollerdepro-
dutos:
use Illuminate\Support\Facades\DB;
Ooutrodetalheseráadicionarachamadado ProdutoTableSeeder
dentrodométodo rundaclasse DatabaseSeeder. Ocódigocompleto
ficaráassim:
<?php
use Illuminate\Database\Seeder;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Support\Facades\DB;
class DatabaseSeeder extends Seeder {
/**
* Run the database seeds.
*
* @return void
*/
public function run()
{
Model::unguard();
$this->call(’ProdutoTableSeeder’);
}
}
class ProdutoTableSeeder extends Seeder {
public function run()
{
DB::insert(’insert into produtos
(nome, quantidade, valor, descricao)
43

## Página 55

4.5. Inserindodadosnatabelaprodutos CasadoCódigo
values (?,?,?,?)’,
array(’Geladeira’, 2, 5900.00,
’Side by Side com gelo na porta’));
DB::insert(’insert into produtos
(nome, quantidade, valor, descricao)
values (?,?,?,?)’,
array(’Fogão’, 5, 950.00,
’Painel automático e forno elétrico’));
DB::insert(’insert into produtos
(nome, quantidade, valor, descricao)
values (?,?,?,?)’,
array(’Microondas’, 1, 1520.00,
’Manda SMS quando termina de esquentar’));
}
}
Excelente.Vamostestar?Podemosutilizarocomando db:seeddo Ar-
tisansemprequequisermosexecutaro DatabaseSeeder.Bastaacessaro
terminaleexecutar:
php artisan db:seed
Tudopronto!Amensagem Seeded: ProdutoTableSeeder seráim-
pressaeosprodutosestarãosalvosnobancodedados. Acessealistagem
novamenteparaconferir.
44

## Página 56

Capítulo5
TrabalhandocomaView
Sabemosquenossocontrollerestácommuitasresponsabilidades,maspor
ondecome çaramelhorá-lo?Atualmente,ocódigoestáassim:
<?php namespace estoque\Http\Controllers;
use Illuminate\Support\Facades\DB;
class ProdutoController extends Controller {
public function lista(){
$html = ’<h1>Listagem de produtos com Laravel</h1>’;
$html .= ’<ul>’;

## Página 57

5.1. Cadacoisaemseulugar:camadaView CasadoCódigo
$produtos = DB ::select(’select * from produtos’);
foreach ($produtos as $p) {
$html .= ’<li> Nome: ’. $p->nome .’,
Descrição: ’. $p->descricao .’</li>’;
}
$html .= ’</ul>’;
return $html;
}
}
Issonãoélegalporumainfinidadedemotivos,porexemplo,comofaría-
mosparaestilizaresseHTML?Eseeuquisesseadicionarumaimagem,uma
tabela,oheader,títuloetc.,tudoissoficamesmodentrodocódigodomeu
controller?
5.1 C ada coisa em seu lugar: camada View
EmvezderetornarumHTML,ocontrollerdeveriadelegaressetrabalhopara
acamadade view,queéaespecialistadoMVCnesseassunto. Amudan ça
serásimples,bastacriarumarquivoPHPcomtodaessalógicadevisualiza-
ção.Podemoschamá-lode listagem.php,eéimportantequeeleestejano
diretório resources/views.
46

## Página 58

CasadoCódigo Capítulo5. TrabalhandocomaView
Fig.5.1:Arquivo/estoque/resources/views/listagem.php
Nessearquivopodemosfazeralgomuitoparecidocomoqueestamos
fazendonocontroller,um foreachemtodososprodutos,mostrandoseu
nome,descrição,eagoraqueestamosnolugarcerto,tambémpodemosexibir
osoutroscampos,quesãoovaloreaquantidade.Emvezdeumalista,po-
demosusarumatabelaparaorganizarumpoucomelhorosdados.Ocódigo
poderáficarparecidocom:
<html>
<body>
<h1>Listagem de produtos</h1>
<table>
<?php foreach ($produtos as $p): ?>
<tr>
<td><? = $p->nome ?> </td>
<td><? = $p->valor ?> </td>
<td><? = $p->descricao ?> </td>
<td><? = $p->quantidade ?> </td>
</tr>
<?php endforeach ?>
</table>
47

## Página 59

5.1. Cadacoisaemseulugar:camadaView CasadoCódigo
</body>
</html>
Agoraquetemosoarquivopronto,sóprecisamosensinaraocontroller
que,emvezdeescreveroHTMLtodo,eledevesimplesmentedelegarotra-
balhoparaessanossaview.Mascomofazerisso?
Vamosporpartes,antesdemaisnada,vamostirartodoaquelecódigo
HTMLdométodo lista.Eleficarassim:
class ProdutoController extends Controller {
public function lista(){
$produtos = DB::select(’select * from produtos’);
return // o que retornar aqui?
}
}
Ufa,bemmelhor,nãoacha? Tiramostodaalógicadevisualizaç ãode
nossocontroller,jáquetemosumacamadaprópriaparafazeressetrabalho,
a view.Opróximopassoéensinaraocontrollerque,apósfazerseutrabalho,
eledeverenderizaroHTMLdaview listagem.phpqueacabamosdecriar.
Parafazerisso,bastamudaroretornodométodopara view(‘listagem’),
comoaseguir:
class ProdutoController extends Controller {
public function lista(){
$produtos = DB::select(’select * from produtos’);
return view(’listagem’);
}
}
Essemétodorecebecomoparâmetroonomedapáginaquevocêquer
exibir,semaextensão,eparautilizá-lovocênãoprecisafazernenhum import,
jáqueissoéfeitopelaclasse Controllerqueherdamos.
48

## Página 60

CasadoCódigo Capítulo5. TrabalhandocomaView
Vamosversetudoestáfuncionando?Bastaacessar http://localhost:8000/
produtosnovamente.Diferentedoesperado,oresultadoserá:
Fig.5.2:Páginadelistagemcommensagemdeerro.
Ops,algumacoisadeuerrado,mascomodescobrir? Amensagemdo
navegadornãonosdizmuito.
5.2 C onsultando os arquivos de log do fra-
mework
Semprequevocêreceberumamensagemcomoessa,dizendoquealguma
coisadeuerradoemseucódigo,vocêpodeedeveconsultarosarquivosde
logdasuaaplicaç ãoparaterumadescriç ãomaisdetalhadasobreoqueestá
acontecendo.Essesarquivosficamnodiretório /storage/logs/esãono-
meadospordata.
49

## Página 61

5.2. Consultandoosarquivosdelogdoframework CasadoCódigo
Fig.5.3:Arquivodelogdaaplicaç ãonadataatual.
Aoabrirologdadataehoraatual,podemosverlogonoiníciodoarquivo
aseguintemensagemdeerro:
[2015-02-25 22:07:50] production.ERROR:
exception ’ErrorException’ with message
’Undefined variable: produtos’ in
/Users/Turini/Desktop/estoque/resources
/views/listagem.php:9
Vejaamensagem: Undefined variable: produtos.Faztodosen-
tido,nãoé?Afinal,secriamosavariável produtosnocontroller,nãopode-
mosacessá-lanaview,queéumoutroarquivo.
Háaindaumaformamaisinteressantedeconsultaros errorsdanossa
aplicaçãoquandoestamosemambientededesenvolvimento,semprecisara
todoomomentoprocuraramensagemnosarquivosdelog.Éfácil,bastacriar
umarquivochamado .envdentrodapastadoprojeto,edentrodelecolocar
asinstruções:
APP_DEBUG=true
50

## Página 62

CasadoCódigo Capítulo5. TrabalhandocomaView
Oseuarquivopodeficarassim:
Fig.5.4:Arquivo.envcomdebugativado.
Comisso,estamosinformandoaoLaravelquequeremosdepurarasmen-
sagensdeerro,oqueébastanterecomendadoquandoestamosdesenvolvendo
aaplicação.Façaaalteraçãoeacesseapáginanovamenteparaveroresultado:
Fig.5.5:Listagemcomerroemmododebug.
Excelente!Assimficamuitomaisfácilidentificaroqueaconteceudeer-
rado,nãoé?
51

## Página 63

5.3. Incluindoparâmetrosnaview CasadoCódigo
5.3 I ncluindo parâmetros na view
Oquefaltoufoi,dealgumaforma,mandaresse arraydeprodutosparaa
view.Poderíamos,sim,criaroarraydiretamentenoarquivo listagem.php
daview,masnãoestaríamosrespeitandoadivisãoderesponsabilidadesdo
MVC.Aviewéresponsávelpelalógicadevisualizaç ão,nãopeloacessoao
bancodedadosnemnadadessetipo.
Umaformamuitomaisinteressantedefazerissoé,noretornodocontrol-
ler,ensinaraoLaravelquequeremosdeixaressavariável produtosacessível
pelaviewcomauxiliodométodo with:
$produtos = DB::select(’select * from produtos’);
view(’listagem’)->with(’produtos’, $produtos);
Vejaquepassamosparaométodo withumachaveevalor,ouseja,a
formacomoeleseráacessadona view(produtos,nessecaso)eovalorasso-
ciadoaele.Ocódigocompletoficaassim:
<?php namespace estoque\Http\Controllers;
use Illuminate\Support\Facades\DB;
use estoque\Produto;
class ProdutoController extends Controller {
public function lista(){
$produtos = DB::select(’select * from produtos’);
return view(’listagem’)->with(’produtos’, $produtos);
}
}
Jápodemostestar.Acessandoalistagemnovamenteteremoscomoresul-
tado:
52

## Página 64

CasadoCódigo Capítulo5. TrabalhandocomaView
Fig.5.6:Listagemdeprodutos.
Pronto,tudocontinuafuncionandoeagoranossocódigoestámuitomais
bemorganizado. Ocontrollerfazseutrabalhoeaofinaldelegaaresponsa-
bilidadedeapresentaçãodoresultadoparaaview,queéacamadaquecuida
disso.Bemjusto,nãoé?
5.4 A lguns detalhes e curiosidades
Essemétodo view,queusamosnoretornodonossocontroller,éum helper
methodparasimplificaresseprocessodetrabalharcomviews.Sevocêjáviu
algumcódigocomasversõesanterioresdoLaravel,vaiselembrarquepara
fazeromesmotrabalhotínhamosqueescrever:
View::make(’listagem’)->with(’produtos’, $produtos);
Nofimdascontas,oqueaconteceéque,aochamarométodo view,sem
passarnenhumparâmetro,elevairetornarumaimplementaç ãodocontrato
ViewdefinidopeloLaravel.Chamandoométodocomparâmetro,eledelegará
achamadaparaométodo make,assimcomoerafeitoanteriormente sóque
comumasintaxeumpoucomaisenxutaeagradável.
Incluindo parâmetros com magic methods
Umacuriosidadeéque,emvezdeescrever:
53

## Página 65

5.4. Algunsdetalhesecuriosidades CasadoCódigo
view(’listagem’)->with(’produtos’, $produtos);
Vocêpodechamarummétodo withProdutos:
view(’listagem’)->withProdutos($produtos);
Façaaalteraç ãoparatestar,oresultadoseráomesmo!Comoissoépos-
sível?
Naverdade,essemétodo“nãoexiste”. Emnenhummomentoosdesen-
volvedoresescreveramummétodo withProdutosdentroda view,mas
simum magic methodquefazessetrabalhodinamicamente.
Emoutraspalavras,sevocêchamou withAlgumaCoisa,eleusaráo
algumaCoisacomochavedoparâmetrodisponibilizadonaview.
Passando um array de dados para a view
Existemdiversasoutrasformasdepassarosdadosparaaview,alémdo
método with. Umadasmaisconhecidaseutilizadasépassandoumarray
comosegundoparâmetrodométodo view.Emvezdefazer:
view(’listagem’)->with(’produtos’, $produtos);
Vocêfariaalgocomo:
return view(’listagem’, [’produtos’ => $produtos]);
Ouextraindooarrayparaumavariável:
$data = [’produtos’ => $produtos];
return view(’listagem’, $data);
Ouaindacriandooarrayeadicionandocadaitemmanualmente:
$data = [];
$data[’produtos’] = $produtos;
return view(’listagem’, $data);
Oquevaimudaréasintaxe,masoefeitoseráomesmo.Vocêpodeesco-
lheraformaquepreferir.
54

## Página 66

CasadoCódigo Capítulo5. TrabalhandocomaView
Mais alguns métodos: exists e file
Outropontoéquevocêpodeverificaraexistênciadeumaviewcomo
método exists:
if (view()->exists(’listagem’))
{
return view(’listagem’);
}
Oumesmousarométodo fileparageraraviewapartirdeumcami-
nho/diretóriodiferente:
view()->file(’/caminho/para/sua/view’);
Legal,nãoé? Sequiserconhecerumpoucomaissobreaview,eureco-
mendoquedêumaboaolhadaemsuadocumentaç ão.Olinké:
http://laravel.com/docs/views
5.5 M elhorando a aparência da nossa listagem
AgoraquenossoHTMLestánolugarcerto,queachademelhorarumpouco
ovisualdalistagem? OLaraveljátrazumarquivochamado app.css
comalgunsestilosprontos,paraajudá-loapoupartempocomessetraba-
lhotambém. EssearquivousainternamenteoconhecidoBootstrap(http:
//getbootstrap.com)paraoestilo,Glyphicons(http://glyphicons.com/)para
osíconesemuitomais.
55

## Página 67

5.5. Melhorandoaaparênciadanossalistagem CasadoCódigo
Não encontrou esse arquivo de CSS?
Nãodeixedeverificarseoarquivo app.cssestápresentenodiretó-
rio /public/cssdoseuprojeto.Senãoestiver,significaquevocêestá
utilizandoLaravelnaversão5.1oumaior.Desdeo5.1,porumadecisão
internadosdesenvolvedoresdoframework,esseealgunsoutrosarquivos
foramdeixadoscomoopcionais.Paraadicioná-losemseuprojeto,basta
instalaropacote scafold:https://github.com/bestmomo/scafold.
Sepreferir, vocêtambémpodecopiarosarquivosdoprojetoque
desenvolvemosduranteesselivro,norepositório: https://github.com/
Turini/estoque-laravel.
Paracome çarausaresseestilo,bastaadicionaro headnoseuHTMLe
o linkcomocaminhodoarquivo,algocomo:
<html>
<head>
<link href="/css/app.css" rel="stylesheet">
<title>Controle de estoque</title>
</head>
<body>
<!-- continuação do seu html aqui -->
Notequejáaproveitamosparacolocarumtítulonapáginatambém.
Aoacessaralistagemvocêjádeveperceberalgumadiferen ça,maspor
enquanto,sónafonte:
56

## Página 68

CasadoCódigo Capítulo5. TrabalhandocomaView
Fig.5.7:Listagemdeprodutoscomcssetítulo.
Aindaqueremosestilizaratabela,mascomo?Ébemsimples,bastaadici-
onaraclasse tablequevocêjávaiteralgumresultado.OHTMLdatabela
deveficarassim:
<table class="table">
<?php foreach ($produtos as $p): ?>
<tr>
<!-- código omitido -->
</tr>
<?php endforeach ?>
</table>
Essasimplesmudan çajádeixanossalistagemcomumvisualbemmais
agradável:
57

## Página 69

5.5. Melhorandoaaparênciadanossalistagem CasadoCódigo
Fig.5.8:Utilizandoclassesdobootstrapnatabela.
Alémdaclasse table,tambémpodemosusar:
•table-stripedparazebraraslinhas
•table-borderedparaadicionarbordas
•table-hoverparaefeitodehover
Hádiversosoutros,quevocêpodeencontrarnadocumentaç ãodoboots-
trap:
http://getbootstrap.com/css/#tables
Vamosusaralgunsdessesestilos?Bastaadicionarasnovasclassesnata-
bela:
<table class="table table-striped table-bordered table-hover">
<!-- restante do html omitido -->
Vocêpodeusarqualqueroutroestiloquepreferir.
Alémdisso, paradesgrudaratabelaeotítulodasbordasdapágina,
podemos envolvê-las em umadivcom a classecontainer. O arquivo
listagem.phpcompletopodeficarassim:
58

## Página 70

CasadoCódigo Capítulo5. TrabalhandocomaView
<html>
<head>
<link href="/css/app.css" rel="stylesheet">
<title>Controle de estoque</title>
</head>
<body>
<div class="container">
<h1>Listagem de produtos</h1>
<table class="table table-striped
table-bordered table-hover">
<?php foreach ($produtos as $p): ?>
<tr>
<td><? = $p->nome ?> </td>
<td><? = $p->valor ?> </td>
<td><? = $p->descricao ?> </td>
<td><? = $p->quantidade ?> </td>
</tr>
<?php endforeach ?>
</table>
</div>
</body>
</html>
Oresultadofinalserá:
59

## Página 71

5.6. Aondechegamoseparaondequeremosir CasadoCódigo
Fig.5.9:Aparênciafinaldalistagemdeprodutos.
5.6 A onde chegamos e para onde queremos ir
Nestecapítulodemosumgrandepasso,quefoisepararalógicadeapresenta-
çãodasregrasdenegóciodocontroller.Vimosqueosganhossãomuitos,já
queagoracadacoisaestáemseuefetivolugar.
Alémdisso,conhecemoso helper method viewevimossobreasdiferen-
tesvariaçõesparainclusãodeparâmetrosutilizando,ounão,ométodo with.
Prontoparadarmaisalgunspassos?
60

## Página 72

Capítulo6
ParâmetrosdarequesteURL
Agoraquetemosnossocódigoumpoucomaisorganizado,comalógicade
acessoaobancono controllerseparadadalógicadeapresentaç ãona view,
podemosadicionarumlinkemcadaprodutodatabelaparaquesejapossível
visualizarseusdetalhesemumanovatela.
6.1 E xibindo detalhes do produto
Amudan çanoHTMLdoarquivo listagem.phpserápequena,sóprecisa-
mosadicionarumanovacolunacomumlink:
<h1>Listagem de produtos</h1>
<table class="table ...">
<?php foreach ($produtos as $p): ?>
<tr>
<td><? = $p->nome ?> </td>

## Página 73

6.1. Exibindodetalhesdoproduto CasadoCódigo
<!-- outras colunas omitidas -->
<td>
<a href="/produtos/mostra>">
Visualizar
</a>
</td>
</tr>
<?php endforeach ?>
</table>
Fig.6.1:Listagemcomlinkdevisualizardetalhes.
Ou,paradeixaraaparênciaumpoucomaisinteressante,podemosusar
umíconedelupanolugardessetexto.Comoestamosusando bootstrap,que
jávemcomoframework,sóprecisamosadicionarum spancomaclassedo
íconequequeremosutilizar.Vejacomoésimples:
<a href="/produtos/mostra">
<span class="glyphicon glyphicon-search"></span>
</a>
Pronto,comissonossalistagemficouassim:
62

## Página 74

CasadoCódigo Capítulo6. ParâmetrosdarequesteURL
Fig.6.2:Listagemcomíconedelupanolink.
Criando uma nova rota
VejaqueolinkjáapontaparaaURL /produtos/mostra,queainda
nãoexisteemnossosistema.Vamoscriá-la?Sóprecisamosacessaroarquivo
routes.phpe,damesmaformacomofizemosparaalistagem,vincularessa
URLaummétododenossocontroller.Ocódigoficaráassim:
Route::get(’/produtos/mostra’, ’ProdutoController@mostra’);
Agora,no ProdutoController,criamosométodo mostra:
public function mostra(){
// retorna uma view com os detalhes
}
Vocêjádeveimaginarqualopróximopasso,nãoé? Queremosretor-
narumaviewcomosdadosdoproduto,portanto,vamoscriarumnovoar-
quivochamado detalhes.php,porenquantoembranco,dentrodapasta
/resources/views/.
Emnossocontroller,precisamosadicionaroretornodométodo mostra,
quedeverenderizaressanovaviewdedetalhesdoproduto:
63

## Página 75

6.1. Exibindodetalhesdoproduto CasadoCódigo
public function mostra(){
return view(’detalhes’);
}
Atéaquinadanovo,certo?Masagoraentraremosemumpontointeres-
sante.Aview,nestecaso detalhes.php,precisadasinformaçõesdopro-
dutoclicadoparaexibi-lasemseuHTML.Algomuitoparecidocomoque
fizemosnalistagem,porémemvezdefazerum forEachnalistadeprodu-
tos,teremossóum:
<h1>Detalhes do produto: <? = $p->nome ?> </h1>
<ul>
<li>
<b>Valor:</b> R$ <? = $p->valor ?>
</li>
<li>
<b>Descrição:</b> <? = $p->descricao ?>
</li>
<li>
<b>Quantidade em estoque:</b> <? = $p->quantidade ?>
</li>
</ul>
Vejaqueutilizeium uldoHTMLpraexibirasinformaçõesemformato
delista,masfiqueàvontadeparamontaroHTMLdaformaquepreferir.
Utilizandoamesmaestruturadanossaviewdelistagem,incluindo header
com css,títuloetc.,nossoarquivo detalhes.phpcompletopodeficarassim:
<html>
<head>
<link href="/css/app.css" rel="stylesheet">
<title>Controle de estoque</title>
</head>
<body>
<div class="container">
<h1>Detalhes do produto: <? = $p->nome ?> </h1>
<ul>
64

## Página 76

CasadoCódigo Capítulo6. ParâmetrosdarequesteURL
<li>
<b>Valor:</b> R$ <? = $p->valor ?>
</li>
<li>
<b>Descrição:</b> <? = $p->descricao ?>
</li>
<li>
<b>Quantidade em estoque:</b> <? = $p->quantidade ?>
</li>
</ul>
</div>
</body>
</html>
Agora,emnossocontroller,precisaremosdeixaravariável $pacessívelna
view.Nãotemerro,afinal,jáfizemosissonalistagemtambém!Sóprecisamos
buscaroelementodobancodedadosedepoisusarométodo withpara
disponibilizá-lono detalhes.php.Algocomo:
public function mostra(){
$resposta = // busca do banco
return view(’detalhes’)->with(’p’, $resposta);
}
Abuscaseráum selectnormal,quepodeserfeitocomo DB:selectque
jáconhecemos,masdiferentedequandoqueremoslistartodososelementos,
agoraprecisaremospassaro iddoprodutocomoparâmetro.Eledeveficar
assim:
$id = 1; // precisamos pegar o id de alguma forma
$resposta =
DB::select(’select * from produtos where id = ?’,[$id]);
Porenquanto,estamospassandoonúmero1como idfixo,logoresolve-
remosisso. Vejaqueusamosumsinaldeinterrogaç ãoparamostrarolocal
ondeoparâmetropassadonosegundoargumentodométodo select(que
éumarray)deveseraplicado.
65

## Página 77

6.1. Exibindodetalhesdoproduto CasadoCódigo
Não v amos focar no SQL... agora
NãosepreocupeementenderafundooSQLesintaxedo DB:select
agora,poisteremosumcapítulodedicadoaissoetambémveremosuma
formabemmaisinteressantedefazeressetipodeconsultasemnospre-
ocuparmostantoementenderessesdetalhes.
Outrainformaçãoimportanteéqueométodo selectsempreretorna
um array,quenestecasopode:
•ter 1 elemento,casosejaencontrado;
•ser vazio,casocontrário.
Precisamosportantoverificarseo arrayderespostaévazio,mostrando
umamensagemdeerro,oucasocontrárioincluiroelementodaprimeira
posiçãonaview.Valelembrarqueaprimeiraposiç ãodeumarrayéoíndice
zero,portantoocódigoficaassim:
public function mostra(){
$id = 1; // precisamos pegar o id de alguma forma
$resposta =
DB::select(’select * from produtos where id = ?’, [$id]);
if(empty($resposta)) {
return "Esse produto não existe";
}
return view(’detalhes’)->with(’p’, $resposta[0]);
}
Vamostestar? Bastaclicarnalupadedetalhesdequalquerprodutoda
listagem,oresultadodeveráserparecidocom:
66

## Página 78

CasadoCódigo Capítulo6. ParâmetrosdarequesteURL
Fig.6.3:Páginadedetalhes,porémsemprecomomesmoproduto.
Excelente, jásabemosquenossocontrollereviewestãofuncionando
comoesperado,oSQLfoiexecutado,oelementocom id1listadoeoHTML
foiexibidocorretamente.Masclaro,independentedoprodutoqueeuclicar,
sempreestamosmostrandoosdadosdoprodutocom id1,quenomeucaso
éa Geladeira.Comoresolver?
6.2 E nviando parâmetros na request
ComosaberexatamentequaloiddoprodutoquefoiclicadonoHTML?Uma
formabemtradicionaldefazerissoseriapassandoo iddoprodutocomoum
parâmetronarequisição,paraissobastariamudarolinkdalistagemcomoa
seguir:
<a href="/produtos/mostra?id= <? = $p->id ?> ">
<span class="glyphicon glyphicon-search"></span>
</a>
ReparequelogoapósaURLadicionamosum ?id=<?= $p->id ?>,ou
seja,estamospassandoumparâmetronarequisiç ãochamado id,comovalor
doiddoproduto. Fazendoaalteraç ão,vocêconsegueverificarnocódigo-
fontedalistagemqueosvaloressãosubstituídoseoslinksficamassim:
67

## Página 79

6.3. Recuperandoparâmetrosdarequest CasadoCódigo
Fig.6.4:Código-fontedalistagemdeprodutos.
6.3 R ecuperando parâmetros da request
Agora que o parâmetroidestá sendo enviado na requisição, podemos
recuperarseurespectivovaloremnossocontrollercomusodainterface
Request.Porsinal,essetipodeinterfaceestáticaéconhecidacomo facade.
Elasnosoferecemumaformasimplesdeacessaralgumasdasclassesfunda-
mentaisdoframework.Sequiser,vocêpodelermaissobreessesfacadesem:
http://laravel.com/docs/facades
Ainterface Requesttemmétodosquenosauxiliamcomessetrabalho,
comoo input,emquevocêpassaachave(name)doparâmetroquefoi
enviadonarequisiçãoeeleretornaovalor,ou nullcasonãosejaencontrado.
Portanto,podemosfazeralgocomo:
68

## Página 80

CasadoCódigo Capítulo6. ParâmetrosdarequesteURL
$id = Request::input(’id’);
Simples,nãoé?Vocêaindapodepassarumvalordefault,casooparâme-
tronãosejaencontrado.Umexemploseria:
$id = Request::input(’id’, ’0’);
Agorao $idteráovalorpassado,ouzero,casonenhumvalorde id
tenhasidoenviadonarequisiç ão.Vamosfazeressaalteraç ão?Nossométodo
mostrapodeficarassim:
public function mostra(){
$id = Request::input(’id’, ’0’);
$resposta =
DB::select(’select * from produtos where id = ?’, [$id]);
if(empty($resposta)) {
return "Esse produto não existe";
}
return view(’detalhes’)->with(’p’, $resposta[0]);
}
Valelembrarque,comoestamosemum namespacediferente,temos
queimportaro Requestnoiníciodenossocontroller,assimcomofizemos
comainterface DB:
<?php namespace estoque\Http\Controllers;
use Illuminate\Support\Facades\DB;
use Request;
class ProdutoController extends Controller {
// ...
Tudopronto,podemosvoltarparaonavegadoreacessarolinkdedetalhes
novamenteque,destavez,osdetalhesdoprodutocorretoserãoexibidos:
69

## Página 81

6.3. Recuperandoparâmetrosdarequest CasadoCódigo
Fig.6.5:Páginadedetalhescomparâmetroid.
Vejaquedessavezeuselecioneiofogão,quetemid2,eseusdadosforam
exibidosconformeesperado.Tambémpodemostestarcomum idquenão
existe,mudandoofinaldaURLpra10,porexemplo:
Fig.6.6:Páginadedetalhescomerrodeprodutoinexistente.
Excelente,amensagemdeerrodonosso iffoiexibidacomoplanejado.
70

## Página 82

CasadoCódigo Capítulo6. ParâmetrosdarequesteURL
6.4 C onhecendo um pouco mais da Request
Vimoscomoésimplesrecuperarosparâmetrosdarequisiç ãocomométodo
input,passandoounãoumvalordefault.Masalémdele,a Requesttem
umavariedadebemgrandedemétodosquenosajudamemtrabalhoscomo
esse.Porexemplo,quersaberseexisteumparâmetroespecíficonarequisi-
ção?Quetalfazer:
if (Request::has(’id’))
{
// faz alguma coisa
}
Háaindaométodo all,queretornaumarraycomtodososparâmetros
darequisição,osmétodos onlye except,comquevocêpoderestringir
quaisparâmetrosquerlistar.
// lista todos os params
$input = Request::all();
// apenas nome e id
$input = Request::only(’nome’, ’id’);
// todos os params, menos o id
$input = Request::except(’id’);
Hátambémmétodoscomourl,queretornaaURLdarequestatual,ou
o pathqueretornaaURI.Porexemplo,emumarequisiç ãoparaométodo
mostra,aofazer:
$url = Request::url();
Ovalorda $urlseria http://localhost:8000/produtos/mostra,masjáno
casodo path:
$uri = Request::path();
Ovalorda $uriseria produtos/mostra.
71

## Página 83

6.5. URLsmaissemânticas CasadoCódigo
Vamosusarmaisalgunsdessesmétodosnodecorrerdoscapítulos,mas
sedesdejáquiserconhecerumpoucomaisedominaraspossibilidadesda
interface Request,vocêpodedarumaolhadanasuadocumentaç ãoem:
http://laravel.com/docs/requests
6.5 URLs mais semânticas
Nossaestratégiaatualdeexibiroprodutojáresolveoproblema,masháuma
alternativabastanteelegantequeéadotadaemsituaçõescomoanossa,onde
queremosexibirdetalhesdeumrecursoespecíficodenossoprojeto.Aideia
éque,emvezdepassaroparâmetropela request,dessaforma:
/produtos/mostra?id=2
vocêuseo idcomopartedesuarota,tendoumaURLmaissemântica:
/produtos/mostra/2
Essasduasalternativassãoconhecidascomoparâmetrodebusca(query
param)eparâmetroderota(path param),respectivamente.Normalmentea
segundaestratégiaéutilizadaquandooparâmetroéobrigatório,comoéo
nossocaso,maspodedependerbastantedogostododesenvolvedor.
Quetalaplicarmosessaalteraç ãoemnossocódigo? Nãovaidarmuito
trabalho.Podemoscome çarpelolink,comodecostume.Noarquivodelis-
tagem,emvezdefazer:
<a href="/produtos/mostra?id= <? = $p->id ?> ">
<span class="glyphicon glyphicon-search"></span>
</a>
Vamosmudarpara:
<a href="/produtos/mostra/<? = $p->id ?> ">
<span class="glyphicon glyphicon-search"></span>
</a>
Vejaquesótiramoso ?id=eadicionamosumabarranolugar.Simples,
nãoé?Masaalteraç ãovaiserumpoucomaioremnossoarquivoderotas,o
routes.php.Atualmente,arotaestáassim:
72

## Página 84

CasadoCódigo Capítulo6. ParâmetrosdarequesteURL
Route::get(’/produtos/mostra’, ’ProdutoController@mostra’);
Mas,naverdade,agoraqueremosalgocomo:
Route::get(’/produtos/mostra/1’, ’ProdutoController@mostra’);
Bem,jásabeoproblema,nãoé? Oidnãopodeserfixo,senãoaURI
sempreseria /produtos/mostra/1. Oidprecisaserumavariável! Veja
comoissoéfeito:
Route::get(’/produtos/mostra/{id}’, ’ProdutoController@mostra’);
Ésóisso,bastaenvolvermosonomedoparâmetroemumpardechaves
epronto!Arotajáestáfeita.Eagora,oquefalta?Vamostestarparaverse
estátudook?Bastaabriralistagemeclicarnoíconededetalhesdequalquer
produto.
Fig.6.7:Produtonãoencontrado,mesmocomidcorreto.
Ops,oprodutonãoexiste!Issoestáacontecendocomtodososprodutos,
oquefizemosdeerrado?
6.6 R ecuperando parâmetros da URL
O problema está no método do controller, que atualmente usa o
Request:inputpararecuperarovalordo id:
public function mostra(){
73

## Página 85

6.6. RecuperandoparâmetrosdaURL CasadoCódigo
$id = Request::input(’id’, ’0’);
$resposta =
DB::select(’select * from produtos where id = ?’, [$id]);
if(empty($resposta)) {
return "Esse produto não existe";
}
return view(’detalhes’)->with(’p’, $resposta[0]);
}
Comovocêjádeveestarimaginando,ométodo inputnãobuscaparâ-
metrosdaURL,comoéocasodonosso idagora. Nolugardisso,experi-
mentemudarpara:
$id = Request::route(’id’);
Agorasim,oresultadoseráoesperado!
Fig.6.8:Detalhesdoprodutocompathparam.
Masespera,equantoaovalordefault?Quandoestávamosusandoomé-
todo input,nossocódigoestavaassim:
$id = Request::input(’id’, ’0’);
74

## Página 86

CasadoCódigo Capítulo6. ParâmetrosdarequesteURL
Porquenãofizemosomesmocomo route? Arespostaésimples: o
{id}darotaagoraéobrigatório!Senãopassar,nãoentranométodoeponto-
final.Sevocêquiserqueoiddofinaldaurlsejaopcional,vocêprecisarádeixar
issoexplícitonomomentoderegistrarsuarota.
Route::get(’/produtos/mostra/{id?}’, ’ProdutoController@mostra’);
Reparequeháuma ?apósoidindicandoqueeleéopcional.Mas,claro,
emnossocasonãoqueremosisso.Oidsempreprecisaráserpassado.
Issonãoétudo,oLaravelnosofereceumaformaaindamaislegaldere-
cuperarparâmetrosdaURL.Quervercomo?Bastaadicionarumargumento
com o mesmo nome do parâmetronaassinaturadoseumétodo,elevaiser
populadocomoumpassedemágica.Vejacomoficaométododocontroller:
public function mostra($id){
$resposta =
DB::select(’select * from produtos where id = ?’, [$id]);
if(empty($resposta)) {
return "Esse produto não existe";
}
return view(’detalhes’)->with(’p’, $resposta[0]);
}
Notequeemnenhummomentoprecisamosusara Request, ofra-
meworkfazessetrabalhopornós. Abraapáginanovamenteparatestar,o
resultadoseráomesmo:
75

## Página 87

6.7. Algunscuidadosnecessários CasadoCódigo
Fig.6.9:Páginadedetalhesdoproduto.
6.7 A lguns cuidados necessários
QuandoestamosusandoparâmetrosnaURL,sempreprecisamosnosatentar
aalgunsdetalhes.Porexemplo,emalgummomentofalamosqueo idpre-
cisariaserumnúmero?Não.Issosignificaqueeuconsigoacessarométodo
mostrapelaseguinteURL:
http://localhost:8000/produtos/mostra/teste
Claramenteissonãodeveriaacontecer. Pornossasorte,aúnicacon-
sequênciaaquiseráveramensagemdequeoprodutonãofoiencontrado.
Masexistemproblemaspiores,comoambiguidadeentrerotas.
Emnossocaso,issoseriaumpoucodifícil,masimaginequeparasimpli-
ficaroptássemosporremovero /mostradenossaURL.Issocausariasérios
problemas,poisasseguintesURLsseriamequivalentes:
• http://localhost:8000/produtos/1
• http://localhost:8000/produtos/adiciona
Jáqueo {id}podeserqualquercoisa,inclusiveumtexto,elepodeser
apalavra adiciona.Emoutraspalavras,dependendodaordememqueeu
registrarasrotas,podeacontecerdeeuacessar /produtos/adicionaea
aplicaçãomeresponderqueesseprodutonãoexiste...Ops!
76

## Página 88

CasadoCódigo Capítulo6. ParâmetrosdarequesteURL
Nessecaso, precisaríamosdealgumaformaensinaraoLaravelqueo
{id}darotasempreseráumnúmero. Issopodeserfeitocomauxiliodo
método where,comonoexemplo:
Route::get(
’/produtos/mostra/{id}’,
’ProdutoController@mostra’
)
->where(’id’, ’[0-9]+’);
Observequeestamospassandoparaométodo whereonomedoparâme-
troeumaexpressãoregular(regex )como patternquepodeserseguido.Faç a
aalteraçãoetenteacessaraURL http://localhost:8000/produtos/mostra/teste
novamente.Oresultadodessavezseráuma NotFoundHttpException.
Fig.6.10:NotFoundHttpExceptionnaURLcomparamnãonumérico.
Justo,nãoé?Afinal,essaURLrealmentenãoexiste.Repareque,passando
umnúmeroválido,tudocontinuafuncionando.
77

## Página 90

Capítulo7
Viewsmaisflexíveisepoderosas
Umdosproblemasdenossocódigoatualéqueexistemuitarepetiç ãoemnos-
sasviews.Veja,porexemplo,comoestánossoarquivode listagem.php:
<html>
<head>
<link href="/css/app.css" rel="stylesheet">
<title>Controle de estoque</title>
</head>
<body>
<div class="container">
<h1>Listagem de produtos</h1>
<table class="table table-striped ...">
<!-- conteúdo omitido -->

## Página 91

CasadoCódigo
</div>
</body>
</html>
Agorapercebaasemelhan çacomoHTMLdoarquivo detalhes.php:
<html>
<head>
<link href="/css/app.css" rel="stylesheet">
<title>Controle de estoque</title>
</head>
<body>
<div class="container">
<h1>Detalhes do produto: <? = $p->nome ?> </h1>
<!-- conteúdo omitido -->
</div>
</body>
</html>
Oconteúdoda divprincipalédiferente,afinal,cadapáginatemsuasre-
graseobjetivosespecíficos,mastodoorestoestáigual! Comisso,nodiaa
diasequeremoscriarumanovapágina,sempensarduasvezesacabamosco-
piandoecolandoalgumaqueexiste,mudandoapenasomiolo.Quemnunca
fezisso?
Oproblemadessaabordageméque,horaououtra,vocêpodequerermu-
darocabe çalho,menu,ouqualqueroutroelementoquefoicopiadoecolado
emquasetodasassuaspáginas.Eagora?Replicoamudan çanasminhas200
viewsmanualmente?Nãopareceumasoluç ãoideal,nãoé?
NestecapítuloveremoscomooLaravelpodenosajudarnessetrabalho,
tornandonossasviewsmaisflexíveis,evitandorepetiçõeseaindaganhando
poderososrecursosquenosajudamnasdiferentesnecessidadesdonossoco-
tidiano.
80

## Página 92

CasadoCódigo Capítulo7. Viewsmaisflexíveisepoderosas
7 .1 B lade,a template engine do Laravel
Seoproblemaestivesseacontecendonocódigodenossocontrollerouem
nossasregrasdenegócio,bastariaextrairocódigorepetidopraumarquivo
ouclasseepronto,poderíamosreutilizá-lasempre.Quetalsefossepossível
fazeromesmonaview,extraindotodaessaestruturaprincipalemumúnico
arquivoereutilizá-losemprequequiséssemos?Poisbem,issonãosóépos-
sívelcomotambém muito recomendado. Dessaforma,quandoquisermos
adicionaralgumlink,mudaroselementosoufazerqualqueralteraç ãonessa
parteemcomum,mudamosemumúnicolugar,etodoorestoéatualizado.
Oganhoemmanutenibilidadeéenorme.
Quemnosajudacomessetrabalhoéo Blade,a template enginedoLa-
ravel. Quervercomoésimples? Pararesolveresseproblemaderepetiç ão,
bastacriarumnovoarquivocomocódigoemcomum,queseránosso layout
principal.
Umfatorimportanteéquetodoarquivodobladeprecisarteraexten-
são .blade.php,portanto,vamoschamá-lode principal.blade.php,
e lembre-se de que, como é umaview, precisa estar no diretório
/resources/views.
81

## Página 93

7.1. Blade,atemplateenginedoLaravel CasadoCódigo
Fig.7.1:Layoutdobladedentrodapasta/resources/views.
Dentrodessearquivo,vamoscolocartodooHTMLemcomum,eutilizar
amarcação @yieldcomonomedase çãoquedeverásersobrescritapelas
outrasviews.Aideiaésimples,suasviews“herdam”desselayoutprincipal,e
sobrescrevemasse çõesneledefinidas:
82

## Página 94

CasadoCódigo Capítulo7. Viewsmaisflexíveisepoderosas
Fig.7.2:Layoutprincipalcomse çãodeconteúdo.
Ocódigodoarquivo principal.blade.phppodeficarassim:
<html>
<head>
<link href="/css/app.css" rel="stylesheet">
<title>Controle de estoque</title>
</head>
<body>
<div class="container">
@yield(’conteudo’)
</div>
</body>
</html>
Nadamuitodiferente,nãoé? TemtodooHTMLemcomum,eamar-
cação @yield(‘conteudo’)paradelimitarondeoconteúdodasoutras
viewsdeveserinserido.Vamostestar?Oprimeiropassoserámudaraexten-
sãodoarquivo detalhes.phppara detalhes.blade.php.
83

## Página 95

7.1. Blade,atemplateenginedoLaravel CasadoCódigo
Fig.7.3:Arquivodedetalhescomextensãodoblade.
Feito isso, podemos tirar todo o código que já existe no layout
principal.blade.php,edeixarapenasomioloqueestavadentroda div
comclasse container.Oarquivovaificarapenascomesteconteúdo:
<h1>Detalhes do produto: <? = $p->nome ?> </h1>
<ul>
<li>
<b>Valor:</b> R$ <? = $p->valor ?>
</li>
<li>
<b>Descrição:</b> <? = $p->descricao ?>
</li>
<li>
<b>Quantidade em estoque:</b> <? = $p->quantidade ?>
</li>
</ul>
Ótimo!Masaindaprecisamosdizerqueessearquivodeveutilizarolayout
principal,doarquivo principal.blade.php.Paraisso,bastaadicionara
marcação @extendscomonomedolayoutqueeledeveherdar(nestecaso:
principal,queéonomedoarquivosemaextensão).
84

## Página 96

CasadoCódigo Capítulo7. Viewsmaisflexíveisepoderosas
@extends(’principal’)
<!-- restante do html aqui -->
Tambéméprecisocolocartodooconteúdorestantedonossoarquivode
detalhesdentrodeuma @section,comonomequefoidefinidono @yield
dolayoutprincipal,quenestecasoé conteudo:
@extends(’principal’)
@section(’conteudo’)
<h1>Detalhes do produto: <? = $p->nome ?> </h1>
<ul>
<li>
<b>Valor:</b> R$ <? = $p->valor ?>
</li>
<li>
<b>Descrição:</b> <? = $p->descricao ?>
</li>
<li>
<b>Quantidade em estoque:</b> <? = $p->quantidade ?>
</li>
</ul>
@stop
Vejaqueusamosum @stopparamarcarofimda section.Issoéne-
cessáriopois,emalgunsmomentos,podemosquerersobrescrevermaisde
uma sectiondolayoutprincipal.
85

## Página 97

7.1. Blade,atemplateenginedoLaravel CasadoCódigo
Fig.7.4:Visãogeraldahierarquiadeviews.
Vamosverseapósamudan çatudocontinuafuncionando?Bastaacessar
apáginadedetalhesdequalquerproduto,porexemplo:
http://localhost:8000/produtos/mostra/1
Fig.7.5:Páginadedetalhesagoracomblade.
Vejaque,comoesperado,apáginacontinuafuncionandonormalmente.
Sequiser,cliquecomobotãodireitonapáginaeselecioneaop ção view page
source.ReparequeoHTMLcontinuaomesmo!
86

## Página 98

CasadoCódigo Capítulo7. Viewsmaisflexíveisepoderosas
Fig.7.6:CódigoHTMLdapáginadedetalhesrenderizadoapósamigraç ão
parablade.
Legal,nãoé?Maso bladenosoferecebemmaisqueisso!Temosmuito
maisoqueexplorar;vamosverasformasdeexibirovalordenossasvariáveis.
7 .2 V ariáveis com blade
Atualmenteestamosusandoamarcaç ãodoPHPpuroparaimprimirosva-
loresdoproduto.Quandofazemos:
<li>
<b>Valor:</b> R$ <? = $p->valor ?>
</li>
87

## Página 99

7.2. Variáveiscomblade CasadoCódigo
Nãoháproblemanissoe,sequiser,vocêaindapodecontinuarexibindo
dessaforma. Massequiser eeurecomendo,vocêtambémpodefazerda
formadoblade,envolvendoavariávelemchavesduplascomoaseguir:
<li>
<b>Valor:</b> R$ {{ $p->valor }}>
</li>
Amudan çaésimpleseoresultadoseráomesmo,masasintaxe,emminha
opinião,éumpoucomaisagradável. Entretanto,oganhovaialémdeuma
sintaxemelhor,ouumcaractereamenos.Vocêganhabastanteflexibilidade
ealgunsrecursosextras,comoo or,paradefinirumvalor defaultcasoa
variávelnãoestejapopulada.Umexemploseria:
{{$p->descricao or ’nenhuma descrição informada’}}
Legal,nãoé?Vamosconhecerdiversosoutrosrecursosnodecorrerdeste
capítuloelivro,masporenquanto,jápodemosfazeramudan çanorestante
doarquivo,quedeveficarassim:
@extends(’principal’)
@section(’conteudo’)
<h1>Detalhes do produto: {{$p->nome}} </h1>
<ul>
<li>
<b>Valor:</b> R$ {{$p->valor}}
</li>
<li>
<b>Descrição:</b> {{$p->descricao}}
</li>
<li>
<b>Quantidade em estoque:</b> {{$p->quantidade}}
</li>
</ul>
@stop
88

## Página 100

CasadoCódigo Capítulo7. Viewsmaisflexíveisepoderosas
7 .3 M igrando a listagem para Blade
Vamosfazeramesmaalteraç ãonoarquivo listagem.php?Ospassosserão
osmesmos,come çandoporrenomearoarquivo,queagoradevesechamar
listagem.blade.php.Alémdisso,jápodemostirartodoocódigoquejá
estádefinidonolayoutprincipaleadicionaro @extendse @section.A
listagemdeveficarassim:
@extends(’principal’)
@section(’conteudo’)
<h1>Listagem de produtos</h1>
<table class="table table-striped table-bordered table-hover">
<?php foreach ($produtos as $p): ?>
<tr>
<td><? = $p->nome ?> </td>
<td><? = $p->valor ?> </td>
<td><? = $p->descricao ?> </td>
<td><? = $p->quantidade ?> </td>
<td>
<a href="/produtos/mostra/<? = $p->id ?> ">
<span class="glyphicon glyphicon-search"></span>
</a>
</td>
</tr>
<?php endforeach ?>
</table>
@stop
Legal,nãoé?Oarquivojáficaumpoucomaislimpo.Jápodemostambém
mudaraformacomoestamosexibindonossasvariáveis,utilizandoaschaves
duplasdoblade.Ocorpodatabelaficaráassim:
<tr>
<td>{{ $p->nome }} </td>
<td>{{ $p->valor }} </td>
<td>{{ $p->descricao }} </td>
89

## Página 101

7.4. Loopingsemaisloopings CasadoCódigo
<td>{{ $p->quantidade }} </td>
<td>
<a href="/produtos/mostra/{{$p->id}}>">
<span class="glyphicon glyphicon-search"></span>
</a>
</td>
</tr>
7 .4 L oopings e mais loopings
Obladetambémnosofereceumamaneirabastanteinteressantedeenxugar
asintaxedonosso foreach,nalistagemdeprodutos.Vejaqueatualmente
estamosfazendocomPHPpuro,ouseja,utilizandoatag <?php ?>. Isso
funciona,evocêpodecontinuarfazendoassimsepreferir,claro,masquetal
tirartodaessaverbosidadeeadicionarumsimples @antesdesseoperador?
Emoutraspalavras,emvezdefazer:
<?php foreach ($produtos as $p): ?>
<!-- codigo omitido -->
<?php endforeach ?>
Vocêpodemudarpara:
@foreach ($produtos as $p)
<!-- codigo omitido -->
@endforeach
Isso melhora bastante a legibilidade do código. Agora o arquivo
listagem.blade.phpcompletodeveestarparecidocom:
@extends(’principal’)
@section(’conteudo’)
<h1>Listagem de produtos</h1>
<table class="table table-striped table-bordered table-hover">
@foreach ($produtos as $p)
<tr>
<td> {{$p->nome}} </td>
90

## Página 102

CasadoCódigo Capítulo7. Viewsmaisflexíveisepoderosas
<td> {{$p->valor}} </td>
<td> {{$p->descricao}} </td>
<td> {{$p->quantidade}} </td>
<td>
<a href="/produtos/mostra/{{$p->id}}>">
<span class="glyphicon glyphicon-search"></span>
</a>
</td>
</tr>
@endforeach
</table>
@stop
Outros tipos de looping
Alémdo foreach,tambémpodemosfazeromesmocomo fortradi-
cional:
@for ($i = 0; $i < 10; $i++)
O indice atual é {{ $i }}
@endfor
Ouaindacomum while:
@while (true)
Entrando em looping infinito!
@endwhile
Haaindaumavariaç ãobastanteinteressante,chamada forelse. Sea
listaforvazia,eleexecutaocódigodoblocomarcadocom @empty:
@forelse($produtos as $p)
<li>{{ $p->nome }}</li>
@empty
<p>Não tem nenhum produto!</p>
@endforelse
Legal,nãoé?Mascomoestamosfazendoo foreachnomiolodeuma
tabela,nãoseriamuitointeressante.Nolugardisso,podemosusarum if!
91

## Página 103

7.5. Adicionandocondiçõesnaview CasadoCódigo
7 .5 A dicionando condições na view
Podemosfazerum ifverificandosealistadeprodutosestávazia,eseestiver,
mostrarumamensagemdequenãoexistenenhumprodutocadastrado.Em
PHPpuro,ocódigoficariaassim:
<?php if(empty($produtos)) { ?>
<div class="alert alert-danger">
Você não tem nenhum produto cadastrado.
</div>
<?php } else { ?>
<h1>Listagem de produtos</h1>
<table>
<? foreach ($produtos as $p) { ?>
?>
<!-- continuação do código -->
<?php } ?> <!-- fechando o foreach -->
<?php } ?> <!-- fechando o else -->
Umpoucoconfusoedifícildeler.Quetalcomblade?
@if(empty($produtos))
<div class="alert alert-danger">
Você não tem nenhum produto cadastrado.
</div>
@else
<h1>Listagem de produtos</h1>
<table>
@foreach ($produtos as $p)
<!-- continuação do código -->
@endforeach
92

## Página 104

CasadoCódigo Capítulo7. Viewsmaisflexíveisepoderosas
@endif
A ausência das chaves e tags do PHP ajuda bastante, nosso có-
digo fica mais simples e legível. Vamos fazer a alteração? O arquivo
listage.blade.phpcompletopodeficarassim:
@extends(’principal’)
@section(’conteudo’)
@if(empty($produtos))
<div>Você não tem nenhum produto cadastrado.</div>
@else
<h1>Listagem de produtos</h1>
<table class="table table-striped table-bordered table-hover">
@foreach ($produtos as $p)
<tr>
<td> {{$p->nome}} </td>
<td> {{$p->valor}} </td>
<td> {{$p->descricao}} </td>
<td> {{$p->quantidade}} </td>
<td>
<a href="/produtos/mostra/{{$p->id}}>">
<span class="glyphicon glyphicon-search"></span>
</a>
</td>
</tr>
@endforeach
</table>
@endif
@stop
Vamostestar?Paranãoterqueapagarosprodutosdobanco,vamosrou-
barumpouco,incluindoumarrayvazionométodo listadonossocon-
troller:
93

## Página 105

7.5. Adicionandocondiçõesnaview CasadoCódigo
class ProdutoController extends Controller {
public function lista(){
// busca os produtos do banco
return view(’listagem’)->with(’produtos’, array());
}
// continuação do código omitido
Comisso,aoacessaralistagem,oresultadoserá:
Fig.7.7:Listagemdeprodutoscommensagemdelistavazia.
Excelente,tudoestáfuncionandocomoesperamos!Agoraquetestamos,
nãoseesque çadevoltarométodo listaaonormal,passandooarrayde
$produtosnolugardeumarrayvazio.
Outros formas de condicionar
Alémdo @ife @else, vocêtambémpodeusar @elseifsou
mesmoo @unless,quefazacondiç ãoinversa.Porexemplo,nocasoa
seguir,ovalorcondicionadosempreseráexibido:
@unless (1 == 2)
Esse texto sempre será exibido!
@endunless
94

## Página 106

CasadoCódigo Capítulo7. Viewsmaisflexíveisepoderosas
7 .6 M arcando produtos em falta no estoque
Queremosagorapintardevermelhoascolunasdatabelaquecontêmprodu-
toscomquantidademenorouiguala1.Essamarcaç ãovisualvainosajudar
aperceberquandoumprodutoestáemfaltaemnossoestoque.
Pracoloriralinha,podemosadicionaraclasse danger,dobootstrap,
nos trsdosprodutosemfalta.Apenasparaveroefeitodaalteraç ão,vamos
adicionaraclasseemtodasascolunas:
<table class="table table-striped ...">
@foreach ($produtos as $p)
<tr class="danger">
<!-- código omitido -->
</tr>
@endforeach
Atualizeapáginadalistagemparaveradiferen ça,elaagoradeveestar
parecidacom:
Fig.7.8:Listagemcomtodososprodutosmarcadosdevermelho.
Ótimo,agorasófaltacondicionarquaisosprodutosquedevemficarpin-
tadosdevermelho.Claro,um @ifresolveria,masficariabemfeioeverboso.
Emvezdisso,podemosfazerumacondiç ãoparecidacom:
95

## Página 107

7.6. Marcandoprodutosemfaltanoestoque CasadoCódigo
{{ $p->quantidade <= 1 ? ’danger’ : ’’}}
Esseéotãoconhecidoternárioque,comovocêjádeveterpercebido,tem
aseguinteestrutura:
{{ condicao ? ’valor_se_true’ : ’valor_se_false’}}
Ouseja,seacondiç ãobooleanaforverdadeira(true),oprimeirovalor
serádevolvido.Casocontrário,retornaráosegundovalor.Éimportantesa-
berqueessenãoéumrecursoexclusivodoblade,claro,emPHPpurovocê
tambémpodefazer:
<?php $p->quantidade <= 1 ? ’danger’ : ’’ ?>
Oquemudoufoiatag,assimcomonosdemaisexemplos,masnessecaso,
usandoobladenãoprecisamosadicionarnenhum @paraqueissofuncione,
bastacolocaroternáriodentrodaschavesduplasepronto. Vamostestar?
Bastaadicionaressacondiç ãodentroda classdo tr. Atabelavaificar
assim:
<table class="table table-striped ...">
@foreach ($produtos as $p)
<tr class="{{$p->quantidade<=1 ? ’danger’ : ’’ }}">
<!-- código omitido -->
</tr>
@endforeach
</table>
Prontoparatestar?Ésóacessaralistagemnovamente!Nomeucaso,ela
ficaráassim:
96

## Página 108

CasadoCódigo Capítulo7. Viewsmaisflexíveisepoderosas
Fig.7.9:Listagemdeprodutoscomverificaç ãodequantidadeemestoque.
Tambémpodemosadicionarumalegendaparadeixaressainformaç ão
maisintuitiva.Vamoscolocarum spanlogodepoisdo @endif,nofinalda
tabela:
<h4>
<span class="label label-danger pull-right">
Um ou menos itens no estoque
</span>
</h4>
Vejaqueelejátemalgumasclassesdobootstrapparaestilizá-lo. Com
essaalteração,oarquivo listagem.blade.phpcompletodeveficarassim:
@extends(’principal’)
@section(’conteudo’)
@if(empty($produtos))
<div class="alert alert-danger">
Você não tem nenhum produto cadastrado.
</div>
@else
97

## Página 109

7.6. Marcandoprodutosemfaltanoestoque CasadoCódigo
<h1>Listagem de produtos</h1>
<table class="table table-striped table-bordered table-hover">
@foreach ($produtos as $p)
<tr class="{{$p->quantidade<=1 ? ’danger’ : ’’ }}">
<td> {{$p->nome}} </td>
<td> {{$p->valor}} </td>
<td> {{$p->descricao}} </td>
<td> {{$p->quantidade}} </td>
<td>
<a href="/produtos/mostra/{{$p->id}}>">
<span class="glyphicon glyphicon-search"></span>
</a>
</td>
</tr>
@endforeach
</table>
@endif
<h4>
<span class="label label-danger pull-right">
Um ou menos itens no estoque
</span>
</h4>
@stop
Acessealistagemnovamenteparaveroresultado!Eladeveestarparecida
com:
98

## Página 110

CasadoCódigo Capítulo7. Viewsmaisflexíveisepoderosas
Fig.7.10:Aparênciafinaldalistagemcomlegenda.
7 .7 O rganizando nossas views
Conformenossosistemavaicrescendo,maisemaisviewsdevemaparecer
eprecisamosorganizá-lasdealgumaforma. Émuitocomumsepararesses
arquivosporcontroller,ouqualquerestruturaquefaciliteseutrabalhoetam-
bémotrabalhodesuaequipe.
Um exemplo de separação por controller seria, se temos um
ProdutoController, criar um diretório chamadoproduto e colo-
carneletodasas viewsrelacionadas. Omesmoparausuáriosequalquer
outroelementoquevenhaaapareceremnossaaplicaç ão.
Vamos criar uma nova pasta chamada produto, dentro de
resources/views,emoverparaelaosarquivos listagem.blade.php
e detalhes.blade.php.Seuprojetodeveficarassim:
99

## Página 111

7.7. Organizandonossasviews CasadoCódigo
Fig.7.11:Pastaprodutocomarquivosdelistagemedetalhes.
Alémdisso,vamoscriarumanovapastachamada layout,tambémem
resources/views,paramoveroarquivo principal.blade.php:
100

## Página 112

CasadoCódigo Capítulo7. Viewsmaisflexíveisepoderosas
Fig.7.12:Pastalayoutcomarquivoprincipal.
Mas,agoraquemudamosisso,tenteacessarqualquerpáginadasuaapli-
cação.Oresultado,talvezjáesperado,seráumerro!
Fig.7.13:Exceptiondearquivonãoencontrado.
Amensagemjádáumapista: View listagem not found.Agoraquemu-
damosaviewparaumsubdiretório,precisamosalteraroretornodosmétodos
101

## Página 113

7.7. Organizandonossasviews CasadoCódigo
donossocontroller.Atualmentefazemosalgocomo:
return view(’listagem’);
Emvezdisso,precisamosensinaraoLaravelqueaviewestádentroda
pasta produto:
return view(’produto/listagem’);
Issojáfunciona,maséaindamaiscomumfazermosdestaforma:
return view(’produto.listagem’);
Vejaqueusamosumpontonolugardabarra.Oresultadoseráomesmo,
vocêpodeescolheroquepreferir.Nossocontrollerdeveficarassim:
class ProdutoController extends Controller {
public function lista(){
// código omitido
return view(’produto.listagem’)->with(’produtos’, $produtos);
}
public function mostra($id){
// código omitido
return view(’produto.detalhes’)->with(’p’, $produto);
}
Vamostestar?Acessamosapáginanovamentee...ops!
102

## Página 114

CasadoCódigo Capítulo7. Viewsmaisflexíveisepoderosas
Fig.7.14:Exceptiondearquivonãoencontrado.
O arquivo principal.blade.php não foi encontrado nas vi-
ews, também precisamos mudar o lugar onde usamos o@extends!
Agora, nolugarde @extends(‘principal’), precisamosmudarpara
@extends(‘layout.principal’).Aalteraç ãodeveserfeitanosarqui-
vos detalhes.blade.phpe listagem.blade.php:
@extends(’layout.principal’)
@section(’conteudo’)
<!-- restante do conteúdo omitido -->
Ótimo,comissonossaaplicaç ãovoltaafuncionarcomoesperado.
7 .8 E stilizando o template principal
Como nossas views seguem um template padrão, definido no
principal.blade.php, agora fica muito mais fácil evoluir e estilizar
odesigndanossaaplicaç ãoweb.Podemosadicionarumheadercomonome
doprojeto,links,footercommensagemdedireitosautoraisetc.
Vejacomoésimples.Comoolayoutestáisolado,sóprecisamosaplicar
asalteraçõesno principal.blade.phpeelaserápropagadaemtodasas
páginas.Umexemplodelayoutseria:
103

## Página 115

7.8. Estilizandootemplateprincipal CasadoCódigo
<html>
<head>
<link href="/css/app.css" rel="stylesheet">
<link href="/css/custom.css" rel="stylesheet">
<title>Controle de estoque</title>
</head>
<body>
<div class="container">
<nav class="navbar navbar-default">
<div class="container-fluid">
<div class="navbar-header">
<a class="navbar-brand" href="/produtos">
Estoque Laravel
</a>
</div>
<ul class="nav navbar-nav navbar-right">
<li><a href="/produtos">Listagem</a></li>
</ul>
</div>
</nav>
@yield(’conteudo’)
<footer class="footer">
<p>© Livro de Laravel da Casa do Código.</p>
</footer>
</div>
</body>
</html>
Reparequeestamosimportandoumarquivo custom.css,queainda
nãoexiste.Sequiser,vocêpodecriaroarquivodentrode /public/css/,
comoconteúdoaseguir:
104

## Página 116

CasadoCódigo Capítulo7. Viewsmaisflexíveisepoderosas
nav.navbar.navbar-default{
background-color: #337ab7;
border-color: #2e6da4;
margin-top: 10px;
}
nav.navbar.navbar-default a {
color: white;
}
li p.navbar-text, a.navbar-brand {
color: white!important ;
font-weight: bolder;
}
footer.footer {
background-color: #337ab7;
border-color: #2e6da4;
margin-top: 55px ;
color: white;
border-radius: 5px;
}
footer.footer p {
padding: 10px;
}
Comesseestilo,alistagemvaificarparecidacom:
105

## Página 117

7.8. Estilizandootemplateprincipal CasadoCódigo
Fig.7.15:Aparênciafinaldalistagem.
Eaviewdedetalhesdeveficarassim:
Fig.7.16:Aparênciafinaldaviewdedetalhes.
Legal,nãoé? Mudamosumúnicoarquivoeoestilofoipropagadoem
106

## Página 118

CasadoCódigo Capítulo7. Viewsmaisflexíveisepoderosas
todos. Claro,fiqueàvontadeparaestilizaroHTMLdaformaquepreferir,
vocêpodeedeveirsemprealémdoquevemosaquinolivro.
107

## Página 120

Capítulo8
RequestemétodosHTTP
8.1 C riando formulário de novos produtos
Jásomoscapazesdevisualizarumalistacomtodososprodutoseosdetalhes
deumprodutoespecífico,masaindanãotemosumafun çãodeadicionar
novosprodutosemestoque.Vamosimplementá-la?
Podemoscome çarpelarota,noarquivo routes.php. Vamosregis-
trar uma URI/produtos/novoapontando para o métodonovo, do
ProdutoController.Elapodeficarassim:
Route::get(’/produtos/novo’, ’ProdutoController@novo’);
Valelembrarque,antesdeadicionarumprodutonobancodedados,pre-
cisamosabrirumapáginacomformulárioparaqueousuáriopossapreencher
osdados,portantoéissooqueométodo novofará.Eleretornaráumaview
chamada formulario,queserácriadadentrodapasta produto:

## Página 121

8.1. Criandoformuláriodenovosprodutos CasadoCódigo
public function novo(){
return view(’produto.formulario’);
}
Para fechar esse passo inicial, precisamos criar o arquivo
formulario.blade.php dentro de /resources/view/produtos/.
Comoqueremosqueeleuseolayoutpadrão,noiníciodoarquivodeclaramos
queeleherdadolayoutprincipaledeclaramosa sectiondeconteúdo,
assimcomofizemoscomosdemaisarquivos.Jávamosadicionarum form
também.Oarquivodeveficarassim:
@extends(’templates.principal’)
@section(’conteudo’)
<h1>Novo produto</h1>
<form>
<label>Nome</label>
<input/>
<label>Descricao</label>
<input/>
<label>Valor</label>
<input/>
<label>Quantidade</label>
<input type="number"/>
<button type="submit">Submit</button>
</form>
@stop
Vamostestarparagarantirquetudofuncionouatéaqui?Sóprecisamos
acessaraURL http://localhost:8000/produtos/novo.Oresultadoserá:
110

## Página 122

CasadoCódigo Capítulo8. RequestemétodosHTTP
Fig.8.1:FormuláriosemestilosdeCSS.
Oformulárioestáumpoucoestranho,comas labelse inputstodosba-
gunçadosemumamesmalinha.Jáqueestamosusandobootstrap,podemos
usarumdeseusmodelosdeformuláriosquepodeserencontradoemsua
documentação:
http://getbootstrap.com/css/#forms
Fazendoaalteração,oHTMLpoderáficarassim:
@extends(’templates.principal’)
@section(’conteudo’)
<h1>Novo produto</h1>
<form>
<div class="form-group">
<label>Nome</label>
<input class="form-control">
</div>
<div class="form-group">
<label>Descricao</label>
<input class="form-control">
111

## Página 123

8.1. Criandoformuláriodenovosprodutos CasadoCódigo
</div>
<div class="form-group">
<label>Valor</label>
<input class="form-control">
</div>
<div class="form-group">
<label>Quantidade</label>
<input type="number" class="form-control">
</div>
<button type="submit" class="btn
btn-primary btn-block">Submit</button>
</form>
@stop
Vamosveroresultado?
Fig.8.2:FormulárioscomestilosCSSdobootstrap.
112

## Página 124

CasadoCódigo Capítulo8. RequestemétodosHTTP
Excelente! Agoraquetemosumanovapágina,podemosadicionarum
novolinknocabe çalhodoarquivo principal.blade.php.OHTMLcom
onovolinkficaráassim:
<ul class="nav navbar-nav navbar-right">
<li><a href="/produtos">Listagem</a></li>
<li><a href="/produtos/novo">Novo</a></li>
</ul>
Comissoboapartedotrabalhoestápronto,masagoraprecisamosim-
plementarafun çãoqueefetivamenteadicionaráumnovoprodutoaobanco.
8.2 C riando o método adiciona
Como de costume, podemos começar pelo mapeamento desse método,
que deve ser feito noroutes.php. Podemos registrar uma nova rota
/produtos/adiciona, que apontará para o métodoadiciona do
ProdutoController.Ocódigoficaráassim:
Route::get(’/produtos/adiciona’, ’ProdutoController@adiciona’);
Agoraquejátemosarota,precisamoscriaressenovométodonocontrol-
ler.Suaassinaturaficarádestaforma:
public function adiciona(){
// deve adicionar os produtos no banco
}
Eagora,qualopróximopasso?AntesmesmodepensarnoSQLquedeve
serexecutadonobancodedados,ounaviewquedeveserretornada,preci-
samospegarosparâmetrosdigitadosnoformuláriodealgumamaneira!Os
passosnecessáriosparaométodo adicionaserão:
public function adiciona(){
// pegar dados do formulario
// salvar no banco de dados
// retornar alguma view
}
113

## Página 125

8.2. Criandoométodoadiciona CasadoCódigo
Jávimosqueéaclasse Requestquemcuidadessetrabalho,depegaros
parâmetrosdarequisição.Portantopodemosfazeralgocomo:
$nome = Request::input(’o_que_passar_aqui_?’);
Eisaquestão. Quandoestávamosbuscandooparâmetroenviadopelo
linkdevisualizar,sabíamosqueachaveera id,poiselaeraenviadapelaURL
dessaforma:
/produtos/mostra?id=1
Vejaqueestamosdeixandoexplícitoqueoparâmetrosechama id,eque
elerecebeovalor1.Comoagoratemosumformulário,enãoumlink,precisa-
remosadicionarum nameemcada inputdoformulárioparaquesejapossível
recuperarsuasinformaçõespelocontroller.OHTMLcompletoficaráassim:
@extends(’templates.principal’)
@section(’conteudo’)
<h1>Novo produto</h1>
<form action="/produtos/adiciona">
<div class="form-group">
<label>Nome</label>
<input name="nome" class="form-control"/>
</div>
<div class="form-group">
<label>Descricao</label>
<input name="descricao" class="form-control"/>
</div>
<div class="form-group">
<label>Valor</label>
<input name="valor" class="form-control"/>
</div>
<div class="form-group">
<label>Quantidade</label>
<input type="number" name="quantidade" class="form-control"/>
</div>
114

## Página 126

CasadoCódigo Capítulo8. RequestemétodosHTTP
<button type="submit"
class="btn btn-primary btn-block">Submit</button>
</form>
@stop
Comisso,emnossocontroller,podemosrecuperarcadaumdosvalores:
public function adiciona(){
$nome = Request::input(’nome’);
$descricao = Request::input(’descricao’);
$valor = Request::input(’valor’);
$quantidade = Request::input(’quantidade’);
// salvar no banco de dados
// retornar alguma view
}
Outras alternativ as
Podemossimutilizarométodo allda Requestparapegartodos
osvaloresdeumaúnicavezemum array,ouaindaométodo only
deixandoexplícitoquaisparâmetrosqueremosbuscar:
$all = Request::all();
$only = Request::only(’nome’, ’valor’, ’...’);
Masparadeixarbemexplícito,egarantiraordemdosdados,poren-
quantofaremosdessaforma.Voltaremosafalarsobreessemétodopara
melhoraresteeoutrospontosqueserãodetalhadosmaisàfrente.
Ótimo,comissojátemoscadaumdosvaloresdigitadosnoformulário.
Vamostestar?Podemosmudarométodo adicionapararetornaressesva-
lores:
public function adiciona(){
115

## Página 127

8.2. Criandoométodoadiciona CasadoCódigo
$nome = Request::input(’nome’);
$descricao = Request::input(’descricao’);
$valor = Request::input(’valor’);
$quantidade = Request::input(’quantidade’);
return implode( ’, ’, array($nome,
$descricao, $valor, $quantidade));
}
O implodefarácomquecadaumdosvaloressejaimpressoseparado
porvírgula.Agorasófaltaumdetalhe,precisamosadicionara actiondo
formulário,paraqueeleenvieparaométodo adiciona:
<form action="/produtos/adiciona">
<!-- restante do html omitido -->
Vamostestar?Bastaabriroformuláriononavegadorepreencheroscam-
poscomalgumvalordeteste:
116

## Página 128

CasadoCódigo Capítulo8. RequestemétodosHTTP
Fig.8.3:Formuláriopreenchidocomvaloresdeteste.
Aoclicarnobotão Adicionar,asaídaserá:
Fig.8.4:Mensagemcominformaçõesdoprodutoadicionado.
117

## Página 129

8.3. InserindoosprodutosnoBD CasadoCódigo
8.3 I nserindo os produtos no BD
Boapartedotrabalhoestápronta,masaindaprecisamospersistiroproduto
nobancodedados. Porenquanto,faremosissocomafun ção insertda
interface DB,quejáusamosnométodo lista.Ocódigodeadicionarficará
parecidocom:
DB::insert(’insert into produtos
(nome, quantidade, valor, descricao) values (?,?,?,?)’,
array($nome, $valor, $descricao, $quantidade));
Vejaque,assimcomofizemosno selectdométodo mostra,utilizamos
uma ?nolugardosvaloresepassamosum arraynaordememqueesses
elementosdevemsersubstituídos.Nãotemmuitosegredo,massevocênão
estámuitoacostumadocomSQLpodeseassustarumpouco.Muitoembreve
veremoscomooLaravelnosajudanestetrabalho.
8.4 R etornando uma view de confirmação
Agoraquejáestamospersistindo,podemosretornaruma viewcomamen-
sagemdeconfirmaç ão,dizendoqueoprodutofoiadicionadocomsucesso.
Podemoschamá-lade adicionado.blade.php.
@extends(’templates.principal’)
@section(’conteudo’)
O produto foi adicionado com sucesso!
@stop
Vale lembrar que essa view será criada dentro de
/resources/views/produto, assim como as demais, portanto, no
retornodocontrollerfaremos produto.adicionado:
public function adiciona(){
$nome = Request::input(’nome’);
118

## Página 130

CasadoCódigo Capítulo8. RequestemétodosHTTP
$valor = Request::input(’valor’);
$descricao = Request::input(’descricao’);
$quantidade = Request::input(’quantidade’);
DB::insert(’insert into produtos
(nome, quantidade, valor, descricao) values (?,?,?,?)’,
array($nome, $valor, $descricao, $quantidade));
return view(’produto.adicionado’);
}
Jápodemosfazerumnovoteste,garantindoqueamensagemseráexibida
equeoprodutoserápersistidonobanco.
Fig.8.5:Adicionandoumnovoproduto.
Aosubmeteroformulário,recebemososeguinteresultado:
119

## Página 131

8.4. Retornandoumaviewdeconfirmaç ão CasadoCódigo
Fig.8.6:Mensagemdeprodutoadicionadoemtextopuro.
Tudofuncionoucomoesperado,masaindaassimalgunsdetalhespodem
sermelhorados.Serialegal,porexemplo,exibironomedoprodutoquefoi
adicionado,nãoé? Issoébemsimples,bastaincluiroparâmetropelocon-
troller,comométodo withquejávimos.Ométodo adicionacompleto
ficarácomooseguinte:
public function adiciona(){
$nome = Request::input(’nome’);
$valor = Request::input(’valor’);
$descricao = Request::input(’descricao’);
$quantidade = Request::input(’quantidade’);
DB::insert(’insert into produtos
(nome, quantidade, valor, descricao) values (?,?,?,?)’,
array($nome, $valor, $descricao, $quantidade));
return view(’produto.adicionado’)->with(’nome’, $nome);
}
Naview,exibimoso $nomeincluído:
@extends(’templates.principal’)
120

## Página 132

CasadoCódigo Capítulo8. RequestemétodosHTTP
@section(’conteudo’)
O produto {{$nome}} foi adicionado com sucesso!
@stop
Alémdisso,podemosadicionaruma divcomasclassesdobootstrappara
deixaramensagemcomumaaparênciaumpoucomaisamigável.Umaalter-
nativaseria:
@extends(’templates.principal’)
@section(’conteudo’)
<div class="alert alert-success">
<strong>Sucesso!</strong> O produto {{$nome}} foi adicionado.
</div>
@stop
Agorasim,oresultadoserá:
Fig.8.7:Mensagemdeprodutoadicionadocomestilosdobootstrap.
Vamosacessartambémalistagem,paragarantirqueoprodutofoipersis-
tidonobancodedadoscomodeveria.
121

## Página 133

8.4. Retornandoumaviewdeconfirmaç ão CasadoCódigo
Fig.8.8:Listagemjácomnovoprodutoadicionado.
Perfeito,deutudocerto!
122

## Página 134

CasadoCódigo Capítulo8. RequestemétodosHTTP
Query Builder
Emvezdeutilizaro DB:insertcomofizemos,temoscomoalter-
nativaumrecursoconhecidocomo query builder.Elenosofereceuma
interfacefluente,queébastanteconvenienteparanãonospreocuparmos
tantocomoSQL.Aadiç ãodeprodutospoderiaficarassim:
DB::table(’produtos’)->insert(
[’nome’ => $nome,
’valor’ => $valor,
’descricao’ => $descricao,
’quantidade’ => $quantidade
]
);
Legal,nãoé?Sevocêseinteressar,podevermaisdaspossibilidades
emhttp://laravel.com/docs/4.0/queries. Embreveveremosumaforma
aindamaissimplesdefazeressetrabalho,comusodo Eloquent.
8.5 U tilizando os métodos do HTTP
Ocadastrodeprodutosestáfuncionandobem,eleéadicionadoaobanco,
umapáginadeconfirmaçãobonitaéexibida,tudoparececorreto.Sóquehá
umpontomuitoimportantequeprecisasercorrigido.
Vejaque,aoadicionarumproduto,todososparâmetrosdarequisiç ão
estãosendoenviadospelaURL:
http://localhost:8000/produtos
/adiciona?nome=Frigobar
&descricao=Com+controle+de+temperatura
&valor=1200.00&quantidade=2
Issoaconteceporque,porpadrão,ométodoHTTPutilizadono formdo
HTMLéo GET.Masnemsemprequeremosdeixartudovisíveldessaforma,
imagineporexemploseessefosseumformuláriodelogin,aURLficariaas-
sim:
123

## Página 135

8.5. UtilizandoosmétodosdoHTTP CasadoCódigo
http://localhost:8000
/login?usuario=Rodrigo
&senha=mamae+querida
Umcaos!Alémdisso,existeumlimiteparaotamanhodaURL,ouseja,se
fosseumformuláriomuitogrande,oupequenocommuitotexto,correríamos
oriscodeperderinformaçõesseesseconteúdoultrapassasseesselimite.
Emvezdeenviarpor GET,podemosmodificaroformulárioparautilizar
umoutrométodoHTTP,o POST.Dessaforma,osdadosnãoficarãomais
visíveisnaURL,tudoserápassadodentrodocorpodoprotocoloHTTP.
AURLficaráhttp://localhost:8000/produtos/adiciona,semosdadosvi-
síveis,independentedaquantidadedeparâmetrosenviados.Émuitoimpor-
tantelembrarqueissonãoéumamedidadeseguran ça,afinalosdadosainda
podemserconsultadospelonavegadordousuário. Oganhodessaaborda-
geméqueocorpodo POSTémuitomaiorqueaURIdo GET,eevitamos
deixarosdadossempretãoexpostos.
Tudooqueprecisamosfazerparaqueosdadossejamenviadosvia POST
no formdenovodeprodutoéadicionaroatributo method="post",como
aseguir:
<h1>Novo produto</h1>
<form action="/produtos/adiciona" method="post">
<div class="form-group">
<label>Nome</label>
<input name="nome" class="form-control"/>
</div>
<!-- continuação do html -->
Mas,comessaalteraç ão,nossoformulárioparadefuncionar!Tenteadi-
cionarumnovoprodutoparaveroresultado.
124

## Página 136

CasadoCódigo Capítulo8. RequestemétodosHTTP
Fig.8.9:MethodNotAllowedHttpExceptionaosubmeteroformulário.
Recebemosuma MethodNotAllowedHttpException,masoqueisso
significa? Oqueaconteceéquenomomentodemapearumarotaparao
método adiciona,fizemos:
Route::get(’/produtos/adiciona’, ’ProdutoController@adiciona’);
Repareque,comoutilizamosométodo get,definimosexplicitamente
queapenasrequisiçõesdessetiposerãoaceitas.Éjusto.Comoresolver?Uma
possibilidadeseriautilizandoométodo any,ouseja,liberandoqualquertipo
derequisiçãoparaessaURL.Masnãoéissoquequeremos,nãoé?Queremos
enviarosdadospor POST;portanto,utilizaremosométodo post:
Route::post(’/produtos/adiciona’, ’ProdutoController@adiciona’);
125

## Página 137

8.5. UtilizandoosmétodosdoHTTP CasadoCódigo
Para saber mais: O método match
Alémde get, poste any,ainterface Routeaindanosofereceum
métodochamado match,quenospermitepassarum arrayespecifi-
candoexatamentequaismétodosHTTPdevemseraceitos.Umexemplo
seria:
Route::match(array(’GET’, ’POST’),
’/produtos/adiciona’,
’ProdutoController@adiciona’);
Nestecaso,requisiçõesdetipo GETou POSTseriamaceitas.
Vamostestar? Ésóabriroformulárionovamentenonavegador,preen-
cheroscamposeclicaremadicionar.Paranossasurpresa,ounão,aindanão
funcionará.Masdestavezoerroseráoutro:
Fig.8.10:TokenMismatchExceptionaosubmeteroformulário.
Recebemosum TokenMismatchException,queacontecesempreque
enviamosumarequisiçãodotipo POSTsemmandarumparâmetrochamado
_token.Masporqueissoénecessário?Porpadrão,oLaraveltemumme-
canismodeprote çãocontra CSRF(Cross-site request forgery,oufalsificaç ão
desolicitaçãoentresites). Esseéumtipodeataque,bastanteconhecidono
126

## Página 138

CasadoCódigo Capítulo8. RequestemétodosHTTP
mundoweb,quetiraproveitodarelaç ãodeconfian çaentreseuusuáriolegí-
timoeumaplicativoweb.Vocêpodelerumpoucomaissobreeleaqui:
http://pt.wikipedia.org/wiki/Cross-site_request_forgery
A solução é simples, o Laravel tem umhelper method chamado
csrf_token()quenosretornaessetoken. Sóprecisamosadicionarum
novo input,quepodeedeveficarescondido,portantoserá type="hidden".
Alémdisso,o namedesseinputprecisaser _token,queéesperadopelasre-
quisiçõesdessetipo.O inputficaráassim:
<input type="hidden"
name="_token" value="{{{ csrf_token() }}}" />
Ocódigononosso formulario.blade.phpcompletofica:
@extends(’layout.principal’)
@section(’conteudo’)
<h1>Novo produto</h1>
<form action="/produtos/adiciona" method="post">
<input type="hidden"
name="_token" value="{{{ csrf_token() }}}" />
<div class="form-group">
<label>Nome</label>
<input name="nome" class="form-control"/>
</div>
<div class="form-group">
<label>Descricao</label>
<input name="descricao" class="form-control"/>
</div>
<div class="form-group">
<label>Valor</label>
<input name="valor" class="form-control"/>
</div>
<div class="form-group">
<label>Quantidade</label>
127

## Página 139

8.6. MaismétodosHTTPequandoutilizá-los CasadoCódigo
<input type="number"
name="quantidade" class="form-control"/>
</div>
<button type="submit"
class="btn btn-primary btn-block">Adicionar</button>
</form>
@stop
Agorasim,vamostestar?
Fig.8.11:Formulárioenviadocomsucesso.
Sucesso!
8.6 M ais métodos HTTP e quando utilizá-los
Mas,afinal,quandodevemosusarcadamétodoHTTP?Émuitocomumuti-
lizarmosométodo GETparalistagensouvisualizaç ãodealgumdenossos
recursos,sempreemoperaçõesque não modificam os valores do sistema.
O POSTdeveserutilizadoparaadiç ãodeinformaçõesaumrecusoexis-
tenteou adição de um novo recurso,comoestamosfazendoagoracomos
produtos.
Alémdisso,existemoutrosverboscomoo PUTe DELETE,quesãoutili-
zadosparaatualizaç ãoeremo ção,respectivamente.
128

## Página 140

Capítulo9
Osdiferentestiposderesposta
Oproblemadaabordagemqueutilizamosaoadicionarumnovoprodutoé
que,normalmente,nãoqueremosirparaumatelaqueapenasmostrauma
mensagem.Sepensarmosbem,aview adicionado.blade.phpnãotem
muitautilidade. Amensagemqueelaexibe,sim,émuitoválida,masisso
podeserfeitodediversasoutrasformas,semanecessidadedeumaviewin-
termediaria.
9.1 R edirecionando para outras lógicas
Umaalternativabastanteutilizadaseriaencaminharousuárioparaapágina
delistagemapósaadiç ãodeumnovoproduto.Podemosaindaexibiramen-
sagemdequeoprodutofoiadicionadocomsucessonapróprialistagem,
comoédecostume.Masoqueprecisaríamosalteraremnossocódigo?
Emvezderetornaraview adicionada,comoestamosfazendo,po-

## Página 141

9.1. Redirecionandoparaoutraslógicas CasadoCódigo
demosmodificarofinaldométodo adicionaparaqueeleretorneaview
listagem.
public function adiciona(){
$nome = Request::input(’nome’);
$valor = Request::input(’valor’);
$descricao = Request::input(’descricao’);
$quantidade = Request::input(’quantidade’);
DB::insert(’insert into produtos
(nome, quantidade, valor, descricao) values (?,?,?,?)’,
array($nome, $valor, $descricao, $quantidade));
return view(’produtos.listagem’);
}
Mas isso não seria o suficiente, afinal, a listagem precisa da variável
$produtoscomtodososregistrosdessatabelanobancodedadosparafun-
cionar.Emoutraspalavras,comessaalteraç ão,aviewdelistagemseráexibida
corretamente,porémelasempreestarávazia.
Fig.9.1:Listagemdeprodutosvazia.
Bem,nãoéoqueesperávamos!Masasoluç ãoébemsimples,bastalistar
osprodutosepassaravariávelparaview,porexemplo:
130

## Página 142

CasadoCódigo Capítulo9. Osdiferentestiposderesposta
public function adiciona(){
$nome = Request::input(’nome’);
$valor = Request::input(’valor’);
$descricao = Request::input(’descricao’);
$quantidade = Request::input(’quantidade’);
DB::insert(’insert into produtos
(nome, quantidade, valor, descricao) values (?,?,?,?)’,
array($nome, $valor, $descricao, $quantidade));
$produtos = DB::select(’select * from produtos’);
return view(’produtos.listagem’)->with(’produtos’, $produtos);
}
Agorasim,tudovaifuncionarcomoesperado! Mascalma,ofinaldo
nossométodo adicionaficouidênticoaométodo lista:
public function lista(){
$produtos = DB::select(’select * from produtos’);
return view(’produtos.listagem’)->with(’produtos’, $produtos);
}
Sabemosqueissonãoélegal,afinal,estamosduplicandocódigo. Do
pontodevistadaorientaç ãoaobjetos,issoéumproblemabemgrande,já
quenãoestamosseguindoseuprincípiobásicodereutilizarcomportamen-
tos.Seométodo listajáfazessetrabalho,nãoqueremoscopiarseucódigo,
massimdelegaressaresponsabilidadeparaele.
Amudan çanométodo adicionaserámínima,masmuitovaliosa.Em
vezdefazero selectnobancoeretornaraviewdelistagem,simplesmente
redirecionamosofluxoparaaURI /produtos,queseráatendidapelomé-
todo lista. Assimcomoo view,háum helper methodquenosajudaa
fazerredirecionamentoscomoesse:
return redirect(’/produtos’);
Simples,nãoé? Podemosedevemosredirecionarofluxodarequisiç ão
paraoutraslógicassemprequenecessário.Ométodo adicionacompleto
ficaráassim:
131

## Página 143

9.2. Maseamensagemdeconfirmaç ão? CasadoCódigo
public function adiciona(){
$nome = Request::input(’nome’);
$valor = Request::input(’valor’);
$descricao = Request::input(’descricao’);
$quantidade = Request::input(’quantidade’);
DB::insert(’insert into produtos
(nome, quantidade, valor, descricao) values (?,?,?,?)’,
array($nome, $valor, $descricao, $quantidade));
return redirect(’/produtos’);
}
Aindahámuitooquemelhorar,masessaalteraç ãojáfoiumpassoparao
caminhocerto.Testeparagarantirquetudoestáfuncionandocomoesperado,
apósadicionarumnovoproduto,ateladelistagemdeveserexibida.
9.2 M as e a mensagem de confirmação?
Oúnicoproblemadessaalteraçãoéqueagoranãotemosmaisumamensagem
bonitacomofeedbackdequeoprocessofoiconcluídocomsucesso,masisso
ésimples,podemosmovera divdapágina adicionado.blade.phppara
ofinaldalistagem:
@extends(’layout.principal’)
@section(’conteudo’)
@if(empty($produtos))
<div class="alert alert-danger">
Você não tem nenhum produto cadastrado.
</div>
@else
<h1>Listagem de produtos</h1>
<table class="table table-striped ...">
@foreach ($produtos as $p)
132

## Página 144

CasadoCódigo Capítulo9. Osdiferentestiposderesposta
<!-- conteúdo omitido -->
@endforeach
</table>
@endif
<h4>
<span class="label label-danger pull-right">
Um ou menos itens no estoque
</span>
</h4>
<div class="alert alert-success">
<strong>Sucesso!</strong>
O produto {{ $nome }} foi adicionado.
</div>
@stop
Vamostestar?Adicionamosumnovoproduto,masvejaoresultado:
Fig.9.2:Exceptiondevariávelnomenãodefinida.
Umaexception!O Undefined variable: nome,ouvariável nome
nãodefinidaembomportuguês,aconteceuporque,quandofizemoso redi-
rect,osdadosdarequisiç ãoanteriorforamperdidos. Issoénatural,claro,
afinaloesperadoéqueosdadosdeumarequisiç ãomorramjuntocomele,
133

## Página 145

9.3. Recuperandovaloresdarequisiçãoanterior CasadoCódigo
mascomoresolver?Háalgumasalternativas,umadasquaisseriaincluiropa-
râmetromanualmentenanovarequisiç ãofeitapelo redirect,maseseforem
vários?Dariaumbomtrabalho!
9.3 R ecuperando v alores da requisição ante-
rior
PornossasorteoLaravelnosofereceumaformabemsimplesderecuperar
osvaloresdarequisiç ãoanterior,jáqueéumanecessidadecomumemcasos
comoesse.Observecomoésimples:
public function adiciona(){
$nome = Request::input(’nome’);
<!-- código omitido -->
return redirect(’/produtos’)->withInput();
}
Ésóisso,bastachamarométodo withInputdepoisdo redirecte
pronto,todososparâmetrosserãomantidos.Masháumaquestão.Naview,
emvezdeacessaroparâmetrodaformatradicional,utilizamosummétodo
auxiliarchamado old.Portanto,ocódigodofinaldalistagemdeveráficar
assim:
<div class="alert alert-success">
<strong>Sucesso!</strong>
O produto {{ old(’nome’) }} foi adicionado.
</div>
Paramiméumaabordagembemjusta,poisdessaformaficaexplícitoque
estamosexibindoumvalordarequisiç ãoanterior.Vamostestar?Tentamos
adicionarumnovoprodutoesucesso,amensagemfoiexibida:
134

## Página 146

CasadoCódigo Capítulo9. Osdiferentestiposderesposta
Fig.9.3:Listagemcommensagemdeprodutoadicionadocomsucesso.
Masvamosfazerumnovoteste,abrindoalistagemsemquenenhumpro-
dutotenhasidoadicionado.Ops,amensagemestálá!
135

## Página 147

9.4. Escolhendoquaisvaloresmanter CasadoCódigo
Fig.9.4:Mensagemdesucessosemnomedeproduto.
Vejaqueaúnicadiferen çaéqueonomeficouembranco,jáquenenhum
produtofoiadicionado.Masasoluç ãoébemsimples,sóprecisamosgarantir
queamensagemseráexibida apenas seovalordonomeestiverpresentena
requisiçãoanterior.Umsimples ifresolveoproblema:
@if(old(’nome’))
<div class="alert alert-success">
<strong>Sucesso!</strong>
O produto {{ old(’nome’) }} foi adicionado.
</div>
@endif
9.4 E scolhendo quais v alores manter
Oproblemadeusaro withInputdessaformaéquetodososparâmetrossão
mantidos,masissoédesnecessário,jáqueestamosusandoapenaso nome.
136

## Página 148

CasadoCódigo Capítulo9. Osdiferentestiposderesposta
Paraevitarqueissoaconte ça,vocêpodedefinirexplicitamentequaisparâme-
trosdevemsermantidos:
return redirect(’/produtos’)
->withInput(Request::only(’nome’));
Legal,nãoé?Omesmovaleparaosoutrosmétodosda Request,como
porexemploo except.Nocasoaseguir,todososparâmetrosexcetoasenha
serãomantidosnapróximarequisiç ão.
return redirect(’/usuarios’)
->withInput(Request::except(’senha’));
9.5 O utros tipos de redirect
Alémdecomofizemos,existemdiversaspossibilidadesinteressantesparao
método redirect.Umadelas,queporsinaleurecomendobastante,ére-
direcionarparaumaaç ãodocontrollerenãoumaURI.
Redirecionando para uma action
Quervercomoésimples?Comoométodo adicionaquerredirecionar
paraométodo lista,daclasse ProdutoController,emvezdeusaro
redirect(‘/produtos’),ouseja,comaURI,elepodefazer:
return redirect()
->action(’ProdutoController@lista’)
->withInput(Request::only(’nome’));
Assimeleestádizendo explicitamente qual o método que quer redi-
recionar,independentedesuaURI.Sedecidirmosnofuturomudararota
dessemétodo,precisaríamoslembrardemudartodososlugaresquefaziam
redirect.Jáquandofazemosdessaforma,apontandoparauma action
específica,tudocontinuafuncionado.
Claro,sealguémmudaronomedométodoo redirecttambémvai
parardefuncionar,masessetipodemudan çaacontececomumafrequência
bemmenordoqueamudan çadeURI.
137

## Página 149

9.6. Parasabermais:rotasnomeadas CasadoCódigo
Masofereceressapossibilidadeapenasparao redirectnãoajuda-
riamuito,pois,todososlinksquebrariamseumarotafossealterada! Ima-
gine que em vez de/produtosa URI da listagem fosse alterada para
/produtos/lista.Oqueacontecequandovocêclicarnolinkdelistagem
domenu?Quebra!
Éjusto,afinal,elevaicontinuarapontandoparaaURIanteriorjáque
estamosdeixandoissofixo(ou hardcoded,comoécomumentechamado)em
nossoHTML.Repareno navbardolayout principal.blade.php:
<ul class="nav navbar-nav navbar-right">
<li><a href="/produtos">Listagem</a></li>
<li><a href="/produtos/novo">Novo</a></li>
</ul>
9.6 P ara saber mais: rotas nomeadas
OLaravelaindaofereceumaoutraalternativaparao redirect.Emvezde
redirecionarparauma URIou action,épossíveldefinirumnomeparasuas
rotas,aodeclará-lasnoarquivo routes.php.Umexemploseria:
Route::get(’/produtos’, [
’as’ => ’apelido’,
’uses’ => ’ProdutoController@lista’
]);
Esserecursoéconhecidocomo named route.Umavezquetenhamosde-
finidoumapelidoparaarota,podemospassarafazeros redirectsdaseguinte
forma:
return redirect()->route(’apelido’);
Linkando para ações
EmvezdelinkarparaumaURI,ésempremaisinteressantelinkarpara
umaaçãodocontroller,assimcomofizemosno redirect. Amudançaserá
simples,bastachamarométodoauxiliar actiondedentrodaschavesduplas
doblade.Oslinksdevemficarassim:
138

## Página 150

CasadoCódigo Capítulo9. Osdiferentestiposderesposta
<ul class="nav navbar-nav navbar-right">
<li>
<a href="{{action(’ProdutoController@lista’)}}">
Listagem
</a>
</li>
<li>
<a href="{{action(’ProdutoController@novo’)}}">
Novo
</a>
</li>
</ul>
Façaaalteraç ãoecliquenoslinksparatestar,oresultadoseráomesmo!
Sevocêclicarcomobotãodireitononavegadoreescolheraop ção view page
source,veráqueocódigo-fontedoHTMLgeradocontinuaráigual:
139

## Página 151

9.7. Outrostiposderesposta CasadoCódigo
Fig.9.5:CódigoHTMLdalistagem,comoslinksapósusodoaction.
9.7 O utros tipos de resposta
Alémderetornarumaview,ouredirecionarparaoutralógica,existemmo-
mentos em que queremos enviar outros tipos de resposta, por exemplo
quandoestamostrabalhandocomserviçosoucomunicaç ãoentresistemas.
UmformatobemcomumemuitoutilizadoatualmenteéoJSON,epor
essemotivoeleéoformatopadrãoderespostadoLaravel. Vocêemalgum
momentojáexperimentouretornarumobjetoouvariávelemvezdeuma
view?Senãofez,comcertezavaigostardetestar.
Podemoscriarumnovométodono ProdutoControllerchamado
listaJson,quepodefazeroseguinte:
140

## Página 152

CasadoCódigo Capítulo9. Osdiferentestiposderesposta
public function listaJson(){
$produtos = DB::select(’select * from produtos’);
return $produtos;
}
Nãoseesque çadequeacadanovométodoumarotadevesercriadano
routes.php,paraqueelefiqueacessívelpelonavegador.
Route::get(’/produtos/json’, ’ProdutoController@listaJson’);
Excelente,agoraquejátemosométodoeeleestádevidamentemapeado,
podemosacessarsuaURLpelonavegador:
Fig.9.6:ListadeprodutosemformatoJSON.
Oresultadoforamtodososprodutos serializadosemformato json.Bem
simples,nãofoi?Mastambémpodemosfazerissoexplicitamente.Emvezde
retornaralistadeprodutos,poderíamosfazer:
public function listaJson(){
$produtos = DB::select(’select * from produtos’);
return response()->json($produtos);
}
Executandononavegador,oresultadoseráomesmo!
141

## Página 153

9.7. Outrostiposderesposta CasadoCódigo
Fig.9.7:ListadeprodutosemformatoJSON.
Claro,nocasodeoJSONretornaroobjetooulistadeobjetosdiretamente
seriamuitomaissimples,masalémdométodo jsonexistemdiversosoutros
quepodemsermuitoúteisemnossodiaadia.Umexemploseria:
return response()
->download($caminhoParaUmArquivo);
Acessarummétodocomesseretornoresultarianodownloaddoarquivo
presentenocaminhoespecificado.Muitosimpleseprático,nãoacha?
142

## Página 154

Capítulo10
EloquentORM
Nossaaplicaçãoestácadavezmaiscompleta,porémosmétodosdocontroller
estãoficandomaiscomplexos,commuitaslinhasdecódigo,eexigemum
certoconhecimentodeSQL.Vejaométodo adiciona,porexemplo:
public function adiciona(){
$nome = Request::input(’nome’);
$valor = Request::input(’valor’);
$descricao = Request::input(’descricao’);
$quantidade = Request::input(’quantidade’);
DB::insert(’insert into produtos
(nome, quantidade, valor, descricao) values (?,?,?,?)’,
array($nome, $valor, $descricao, $quantidade));

## Página 155

10.1. Conheçaasoluç ão:ORM CasadoCódigo
return redirect()
->action(’ProdutoController@lista’)
->withInput(Request::only(’nome’));
}
Aordememqueosparâmetrossãopassadosparaométodo insert
éimportantíssima!Umerropodecausarumaconfusãoemnossobancode
dados.Alémdisso,sevocênãoestáacostumadocomSQL,deveestarachando
bastantecomplicado,nãoé?
NestecapítuloveremoscomooLaravel,comajudadeoutroframework,
podenosauxiliarnessesproblemas. Ométodo adiciona,porexemplo,
terminarácom2linhas,muitomaislegívelefácildemanter.
10.1 C onheça a solução: ORM
Sabemosqueoproblemadessaabordageméqueestamosnospreocupando
muitocominstruçõesSQL,ocódigoficaverbosoeexigeumconhecimento
maiorsobreoutroparadigmacomoqual,namaiorpartedotempo,nãoque-
remosficarnospreocupando.
Háumaformabemmaissimpleseinteressantedefazeressaeoutrasope-
raçõesnobancodedados,semtermosquenospreocupartantocomSQLe
detalhesdomundorelacionaldosbancosdedados.IntegradoaoLaravelte-
mosoutroframework,conhecidocomo Eloquent ORM.Elecuidadeencap-
sularboapartedacomplexidadedomundorelacional,permitindoacessoaos
nossosdadosdeumaformabemeleganteefluente.
144

## Página 156

CasadoCódigo Capítulo10. EloquentORM
Frameworks ORM
PormaisqueoPHPjásimplifiquemuitoesseprocesso,aindaassim
gastamosumaboapartedonossodesenvolvimentocom queriesSQLe
nospreocupandocomdetalhesdeseuparadigma.Quertrocardebanco?
Nemsempreissoseráfácil. Apesardopadrão,muitacoisamudade
acordocomofabricante.Háaindaodesafiodepensardeduasmaneiras
diferentes,jáqueoparadigmarelacionalébemdiferentedaorientaç ãoa
objetos.
Essassãoalgumasdasmuitasrazõesquemotivaramosframeworks
ORM(Object Relational Mapping),quecomoopróprionomeindica,
fazemomapeamentodosnossosobjetosparaomundorelacionaldos
bancosdedados.Vocêvaiperceberqueessaabstraç ãoébastanteconve-
niente,porissoétãobem-vindaemlinguagenscomooPHP,Java,C# e
outras.
10.2 T udo mais simples com Eloquent
Quervercomoéfácilcome çarausaroEloquent?Emvezdesairescrevendo
SQLs,sóprecisamosusaraclassede modeloquecriamosanteriormentepara
representarnossatabeladeprodutos.
Vejaque,assimcomoqualquerclassedemodelodoEloquent,aclasse
Produtoherdade Model. Todaclassequeherdade Modelganhauma
sériedemétodosquenosauxiliaafazeroperaçõesnobancodedados. O
primeirométodoqueusaremosseráo all,queretornatodososregistrosda
tabela.
Vejacomoestamosfazendoissonométodo listaatualmente:
public function lista(){
$produtos = DB::select(’select * from produtos’);
return view(’produtos.listagem’)->with(’produtos’, $produtos);
}
Nolugardisso,commétodo all,ocódigoficaráassim:
145

## Página 157

10.2. TudomaissimplescomEloquent CasadoCódigo
public function lista(){
$produtos = Produto::all();
return view(’produtos.listagem’)->with(’produtos’, $produtos);
}
Oresultadoseráomesmo,sóqueagoranãoexistenenhuminstruç ão
SQLnessemétodo. Resolvemosoproblemacomumasimpleschamadade
método.Vamostestar?
Fig.10.1:ExceptiondeclasseProdutonãoencontrada.
Ops,precisamosimportaraclasse Produto!
<?php namespace estoque\Http\Controllers;
use Illuminate\Support\Facades\DB;
use estoque\Produto;
use Request;
class ProdutoController extends Controller {
// restante do código escondido
Agorasim,vamosabriralistagemnovamente:
146

## Página 158

CasadoCódigo Capítulo10. EloquentORM
Fig.10.2:Listagemdeprodutos.
Sucesso, tudofuncionando. Podemosfazeromesmocomométodo
listaJson,queatualmenteestáassim:
public function listaJson(){
$produtos = DB::select(’select * from produtos’);
return response()->json($produtos);
}
Agora,comométodo all,elepodeficarassim:
public function listaJson(){
$produtos = Produto::all();
return response()->json($produtos);
}
10.3 B uscando pelo ID com Eloquent
OutropontoemquepodemostirarproveitodoEloquenténabuscadepro-
dutospelo id,comoéfeitonométodo mostra:
147

## Página 159

10.3. BuscandopeloIDcomEloquent CasadoCódigo
public function mostra($id){
$resposta =
DB::select(’select * from produtos where id = ?’, [$id]);
if(empty($resposta)) {
return "Esse produto não existe";
}
return view(’produto.detalhes’)->with(’p’, $resposta[0]);
}
Paraissofuncionarfoinecessáriopassarmosumarraycomosparâmetros
prométodo select,quealémdissoretornaumarray.Muitotrabalhoso,não
é?Quetaltrocartodoessetrabalhoporumsimples find($id)?
public function mostra($id){
$produto = Produto::find($id);
if(empty($produto)) {
return "Esse produto não existe";
}
return view(’produto.detalhes’)->with(’p’, $produto);
}
Comissotemosumcódigomaissimples,legíveleexpressivo. Nãose
esqueçadetestar:
Fig.10.3:Detalhesdoproduto.
148

## Página 160

CasadoCódigo Capítulo10. EloquentORM
10.4 M igrando a inserção de produtos
Ométodo adicionaéumdosmaisproblemáticos,ecomisso,oganhoserá
aindamaior.Lembracomoeleestá?Dêumaboaolhada,essecódigotodovai
sumirembreve!
public function adiciona(){
$nome = Request::input(’nome’);
$valor = Request::input(’valor’);
$descricao = Request::input(’descricao’);
$quantidade = Request::input(’quantidade’);
DB::insert(’insert into produtos
(nome, quantidade, valor, descricao) values (?,?,?,?)’,
array($nome, $valor, $descricao, $quantidade));
return redirect()
->action(’ProdutoController@lista’)
->withInput(Request::only(’nome’));
}
Vamosmelhorá-loaospoucos,acome çar,tirandoesseSQLdaí:
public function adiciona(){
$produto = new Produto();
$produto->nome = Request::input(’nome’);
$produto->valor = Request::input(’valor’);
$produto->descricao = Request::input(’descricao’);
$produto->quantidade = Request::input(’quantidade’);
$produto->save();
return redirect()
->action(’ProdutoController@lista’)
->withInput(Request::only(’nome’));
}
Adiferen çaéqueagorainstanciamosumproduto,populamososvalores
darequisiçãoe,emvezdeexecutarumSQL,simplesmentechamamosomé-
149

## Página 161

10.4. Migrandoainserçãodeprodutos CasadoCódigo
todo save.Bemmelhor,masaindatemmuitocódigoaí,nãoé?Podemos
reduziraindamais:
public function adiciona(){
$params = Request::all();
$produto = new Produto($params);
$produto->save();
return redirect()
->action(’ProdutoController@lista’)
->withInput(Request::only(’nome’));
}
Notequeestamospassandooarraycomosparâmetrosdarequisiç ãono
construtordomodelo nessecaso Produto.Issoémuitocomumnomundo
PHPedeoutraslinguagens,maspodeserumpoucoperigoso. Porisso,ao
tentaradicionarumprodutoapósessaalteraç ão,oresultadoserá:
Fig.10.4:MassAssignmentExceptionaotentaradicionar.
Recebemosum MassAssignmentException,masoqueissosignifica?
::Mass-assignment
Sendo assim, sempre que quisermos fazer a atribuição dessa forma,
via mass-assignable, paranosproteger, precisamosadicionarumapropri-
edadechamada $fillableemnossomodeloespecificandoexatamente
150

## Página 162

CasadoCódigo Capítulo10. EloquentORM
quais atributos podem ser populados, caso contrário receberemos uma
MassAssignmentException.Nocasodoproduto,serãoonome,descri-
ção,valorequantidade:
protected $fillable = array(’nome’,
’descricao’, ’valor’, ’quantidade’);
Aclassecompletadeveficarassim:
<?php namespace estoque;
use Illuminate\Database\Eloquent\Model;
class Produto extends Model {
protected $table = ’produtos’;
public $timestamps = false;
protected $fillable = array(’nome’,
’descricao’, ’valor’, ’quantidade’);
}
Tudopronto,agoraaadiç ãovoltaráafuncionarcomoesperado.
151

## Página 163

10.4. Migrandoainserçãodeprodutos CasadoCódigo
Uma outra opção: guarded
Alémdo $fillable,vocêtambémpodedeclararumatributocha-
mado $guarded,quefazjustamenteopapelinverso.Eleéumaespécie
de black-listdosvalorescujaatribuiç ãovocênãoquerpermitirvia mass-
assignment.Umbomcasodeusoparao $guardedseriaimpedirqueo
usuárioaltereo iddeseumodelo.Vejacomoésimples:
<?php namespace estoque;
use Illuminate\Database\Eloquent\Model;
class Produto extends Model {
protected $table = ’produtos’;
public $timestamps = false;
protected $fillable = array(’nome’,
’descricao’, ’valor’, ’quantidade’);
protected $guarded = [’id’];
}
Ocódigoficoubemmaissimples,nãoé?
public function adiciona(){
$params = Request::all();
$produto = new Produto($params);
$produto->save();
return redirect()
->action(’ProdutoController@lista’)
->withInput(Request::only(’nome’));
}
152

## Página 164

CasadoCódigo Capítulo10. EloquentORM
Mas,apesardejáestarsimples,podemosenxugá-loaindamais.Emvez
decriarumanovainstânciadeproduto,podemosutilizarum factory method
chamado create:
$params = Request::all();
Produto::create($params);
Nemprecisamoschamarométodo save!Legal,nãoé?Agoraqueestá
maissimples,podemosdeclararocódigoemumúnico statement:
Produto::create(Request::all());
Vejacomonossocódigofinalficoumaisenxuto:
public function adiciona(){
Produto::create(Request::all());
return redirect()
->action(’ProdutoController@lista’)
->withInput(Request::only(’nome’));
}
10.5 F unção de remover produtos
Paradeixarnossaaplicaç ãoaindamaiscompletaedebônusconhecerum
novométododoEloquent,quetalcriarmosumanovafun çãoderemover
produtos?Ofundamentalnósjásabemosmuitobem,criamosumanovarota
no routes.php:
Route::get(’/produtos/remove/{id}’, ’ProdutoController@remove’);
Noteque,assimcomonométodo mostra,estamospassandoo idcomo
path param,sendoassimpodemosrecebê-locomoargumentonométodo
remove,quevamoscriarno ProdutoController:
public function remove($id){
// ...
}
153

## Página 165

10.5. Funçãoderemoverprodutos CasadoCódigo
Assimcomoasoutrasoperações,deletarumprodutocomEloquentébem
simples.Sóprecisamosbuscaromodeloquedeveserexcluídoechamarseu
método delete:
public function remove($id){
$produto = Produto::find($id);
$produto->delete();
}
Excelente,eaofinal,podemosredirecionarparaalistagem:
public function remove($id){
$produto = Produto::find($id);
$produto->delete();
return redirect()
->action(’ProdutoController@lista’);
}
Quasetudopronto,sóprecisamosadicionarumnovolinknatabelada
view listagem.blade.php.Eleficarámuitoparecidocomolinkdeexibir
detalhesdoproduto,mudandoapenasseuíconeea actionqueseráchamada:
<table class="table table-striped ...">
@foreach ($produtos as $p)
<!-- código escondido -->
<td>
<a href="{{action(’ProdutoController@remove’, $p->id)}}">
<span class="glyphicon glyphicon-trash"></span>
</a>
</td>
</tr>
@endforeach
</table>
Vamosveroresultado?Aorecarregarapáginadelistagemdeprodutos
nonavegador,onovoíconecomlinkestarádisponível:
154

## Página 166

CasadoCódigo Capítulo10. EloquentORM
Fig.10.5:Listagemcomiconederemover.
Tenteexcluirumprodutoparatestar!
10.6 C ódigo final do ProdutoC ontroller
Apósessasériedemudan çascomaintroduç ãodoEloquent,ocódigodo
nossocontrollerdeprodutosficouassim:
<?php namespace estoque\Http\Controllers;
use estoque\Produto;
use Request;
use estoque\Http\Requests\ProdutosRequest;
class ProdutoController extends Controller {
public function lista(){
$produtos = Produto::all();
return view(’produto.listagem’)
->with(’produtos’, $produtos);
}
public function mostra($id){
$produto = Produto::find($id);
155

## Página 167

10.6. CódigofinaldoProdutoController CasadoCódigo
if(empty($produto)) {
return "Esse produto não existe";
}
return view(’produto.detalhes’)
->with(’p’, $produto);
}
public function novo(){
return view(’produto.formulario’);
}
public function adiciona(){
Produto::create(Request::all());
return redirect()
->action(’ProdutoController@lista’)
->withInput(Request::only(’nome’));
}
public function listaJson(){
$produtos = Produto::all();
return response()->json($produtos);
}
public function remove($id){
$produto = Produto::find($id);
$produto->delete();
return redirect()
->action(’ProdutoController@lista’);
}
}
Maissimples,nãoacha?OEloquentabstraiboapartedacomplexidade
desetrabalharcominstruçõesdobancodedados. Antesdeseguir,quetal
darumaolhadanadocumentaç ãodesseframework?Comcertezavocêen-
contrarámuitacoisalegalporlá.
http://laravel.com/docs/eloquent
156

## Página 168

CasadoCódigo Capítulo10. EloquentORM
Desafio
Quetaltentarimplementarafun çãodealterarprodutosporconta
própria? Esseéomomentoemquevocêperceberáserealmenteestá
afiadonoLaravel. OmétododealterareseuformulárioHTMLserão
muitoparecidoscomodeadicionar,comadiferen çadequevocêpreci-
sarápassaro iddoprodutocomoparâmetro.Ficoucomalgumadúvida?
Nãodeixedemandarume-mailnalistadolivro.
157

## Página 170

Capítulo11
Validandoosdadosdeentrada
Apesardeestarmaissimplesejáfazerboapartedeseutrabalhomuitobem,
ométodo adicionaaindapecaemumpontomuitoimportante.Osdados
deentradanãosãovalidados,permitindoquequalquerinformaç ãosejaper-
sistidanobanco.Vejaporexemplooqueacontecequandoadicionamosum
produtosemnenhumcampopreenchido:

## Página 171

CasadoCódigo
Fig.11.1:Produtoembrancoadicionadonalistagem.
Oprocessofoiconcluídosemquenenhumerrofosseapresentado,ouseja,
umregistrovaziofoiadicionadonobancoepontofinal.Enãoésóisso,tente
porexemploadicionarumprodutocomvalorequantidadenegativa:
Fig.11.2:Produtocomvalorequantidadenegativa.
160

## Página 172

CasadoCódigo Capítulo11. Validandoosdadosdeentrada
Funciona,masnãodeveria.Semprequeestamosadicionandorecursosno
bancodedadosprecisamostomaressecuidado,devalidarosvalorespassados
pelousuáriodeacordocomanossaregradenegócio.Emalgunscasos,passar
umvalornegativoserátotalmenteválido,masnãoéonosso.Omesmopara
asdemaisregras.Mascomovalidarcadavalorquefoipassado?
Claro,um ifjáresolveriaoproblema:
public function adiciona(){
$valor = Request::input(’valor’);
if(floatval($valor) < 0) {
// volta para o formulário com uma mensagem de erro
}
// faz o restante do trabalho
}
Masquantosdesseseriamnecessáriosparavalidarumformuláriode30
campos? Penseemcomoficariaométodo adiciona,cheioderegrasde
validaçãoespalhadasnosdiversos ifs.Umpesadelodemanuten ção.
11.1 V alidação com Laravel
Seéumanecessidadedemuitos,comcertezaoLaraveltemalgoparanos
ajudar. Esseéoespíritodesseedosoutrosframeworkstambém,facilitara
vidadequemdesenvolveeoferecerrecursosessenciaisparanossosprojetos.
Existem diversas formas de fazer validação dos dados, e o
Validator:makeéumadelas.Comelevocêpodefazeralgocomo:
$validator = Validator::make(
[’nome’ => Request::input(’nome’)],
[’nome’ => ’required|min:5’]
);
Reparequepassamosdoisarrays,umcomosvaloreseoutrocomasregras
devalidação.Nesseexemplo,onomeseráobrigatório(required )eprecisará
161

## Página 173

11.1. ValidaçãocomLaravel CasadoCódigo
ternomínimo5caracteres.Vocêpodevertodasasregrasdevalidaçõesexis-
tentesnestelink:
http://laravel.com/docs/validation#available-validation-rules
Agora,voltandoaoexemplo,ométodo makeretornaum $validator
quetemumasériedemétodosfundamentaisparaessetrabalho.Porexem-
plo,setiverumerrodevalidaç ão,precisovoltarparaoformulário,certo?
Podemosverificarissocomométodo fails:
if ($validator->fails())
{
return redirect()
->action(’ProdutoController@novo’);
}
Simples!Ocódigodométodo adicionacompletoficaráassim:
public function adiciona(){
$validator = Validator::make(
[’nome’ => Request::input(’nome’)],
[’nome’ => ’required|min:5’]
);
if ($validator->fails())
{
return redirect()
->action(’ProdutoController@novo’);
}
Produto::create(Request::all());
return redirect()
->action(’ProdutoController@lista’)
->withInput(Request::only(’nome’));
}
Paratestar,podemosabrirapáginadeadiç ãodeprodutoseclicarem
adicionar,sempreenchernadanocampo nome.Vejaqueeleretornarápara
oformulário,sempersistiroprodutonobancodedados.
162

## Página 174

CasadoCódigo Capítulo11. Validandoosdadosdeentrada
Fig.11.3:Retornouaoformulário,porémsemexibirumamensagem.
Oproblemaéquedessaformaousuárionãosabeoquefezdeerrado,
precisamosmostrarumamensagemdefeedbackparaele! O Validator
tambémtemummétodoquenosajudacomisso,repare:
$messages = $validator->messages();
Ométodo messagesnosretornaumarraycomtodasasmensagensde
validação.Poderíamos,porexemplo,devolveressalistadeerrosparaaview.
Mas,antesdenospreocuparmoscomisso,existemoutrosdetalhesquepre-
cisamosatacar.
Ograndeproblemadessaabordageméque,normalmente,queremosvali-
darmaisdeumcampo.Vejaqueapenascomavalidaç ãodo nomeométodo
adicionajáficouenorme,imaginequandoadicionarmosregrasprades-
crição,valor,quantidadeeoutroscamposquepodemviraexistir. Vaificar
enorme!
163

## Página 175

11.1. ValidaçãocomLaravel CasadoCódigo
public function adiciona(){
$validator = Validator::make(
[
’nome’ => Request::input(’nome’),
’descricao’ => Request::input(’descricao’),
’valor’ => Request::input(’valor’),
’quantidade’ => Request::input(’quantidade’)
],
[
’nome’ => ’required|min:5’
’descricao’ => ’required|max:255’,
’valor’ => ’required|numeric’,
’quantidade’ => ’required|numeric’
]
);
if ($validator->fails())
{
return redirect()
->action(’ProdutoController@novo’);
}
Produto::create(Request::all());
return redirect()
->action(’ProdutoController@lista’)
->withInput(Request::only(’nome’));
}
Issoporquenossoprodutosótem4propriedades,imaginesetivesse30!
Seriaumcaos.Utilizaro Validatordessaformaémuitosimples,mascos-
tumaserrecomendadoapenasparacasossimpleseisolados.Nosdemaisca-
sos,recomenda-seacriaç ãodeumanovaclasse,especialistaporaplicaressas
regrasdevalidaç ão.
164

## Página 176

CasadoCódigo Capítulo11. Validandoosdadosdeentrada
11.2 V alidando com Form Requests
Esse tipo de classe especial, cuja responsabilidade é validar os dados
do formulário enviados pela requisição, é conhecida pelo Laravel como
Form Requests. Éumaclassenormal,quevocêcriadentrododiretório
app/Http/Requestse deve herdar da classeRequestpresente neste
mesmodiretório.
Masemvezdecriaraclassenamão,adicionarosimports,namespacee
todosessesdetalhes,podemosdeixartodoessetrabalhoparao Artisan.Veja
comoésimples:
php artisan make:request ProdutosRequest
Muitoparecidocomquandoestamoscriandoumnovomodelo,masem
vezde make:model,faremosum make:request.Vamostestar?Ésódi-
gitaressecomandonoterminal,dentrodapastadonossoprojeto:
Fig.11.4:CriandoumformrequestcomArtisan.
Amensagem request created successfully deveserexibidaepronto,
já podemos procurar pelo arquivo ProdutosRequest dentro de
app/Http/Requests.
165

## Página 177

11.2. ValidandocomFormRequests CasadoCódigo
Fig.11.5:ProdutosRequestcriadonapastaapp/Http/Requests.
Chamamosàclassede ProdutosRequestporqueéumapráticacomum
utilizaressesufixo Request,masnãoéobrigatório. Vocêpodeescolher
onomequepreferir. Nogeral,avantagemdeseguiressaconven çãoéque
apenasaoleronomedaclassevocêjásabedoquesetrata,éum form request
deprodutos!
Aclassefoicriadacomaseguinteestrutura:
<?php namespace estoque\Http\Requests;
use estoque\Http\Requests\Request;
class ProdutosRequest extends Request {
/**
* Determine if the user is authorized
* to make this request.
166

## Página 178

CasadoCódigo Capítulo11. Validandoosdadosdeentrada
*
* @return bool
*/
public function authorize()
{
return false;
}
/**
* Get the validation rules that apply
* to the request.
*
* @return array
*/
public function rules()
{
return [
//
];
}
}
Parecebemassustador,umbichodesetecabe ças!Masnofim,vocêper-
ceberáqueelaébemsimples. Temosdoismétodos,oprimeiro,chamado
authorize,éutilizadoparainformarseousuáriopodeounãofazeressa
requisição.
Eleéexecutadoantesmesmodavalidaç ão,portantoseodeixarmoscomo
false,ninguémvaiconseguiradicionarprodutos.Normalmentenessemé-
todopodemosverificarseousuáriotempermissões,fazerconsultasnobanco
dedadosetc.,masemnossocaso,semprequeremosexecutá-lo,portanto
bastamudarseuvalorpara true.
public function authorize()
{
return true;
}
Jánooutrométodo,o rules,retornamosumarraycomasregrasde
167

## Página 179

11.2. ValidandocomFormRequests CasadoCódigo
validação,assimcomoestávamosfazendonométodo makedo Validator.
Emnossocaso,será:
public function rules()
{
return [
’nome’ => ’required|max:100’,
’descricao’ => ’required|max:255’,
’valor’ => ’required|numeric’
];
}
Comisso,ocódigocompletodaclasse ProdutosRequestficaráassim:
<?php namespace estoque\Http\Requests;
use estoque\Http\Requests\Request;
class ProdutosRequest extends Request {
/**
* Determine if the user is authorized
* to make this request.
*
* @return bool
*/
public function authorize()
{
return true;
}
/**
* Get the validation rules that apply
* to the request.
*
* @return array
*/
public function rules()
{
return [
168

## Página 180

CasadoCódigo Capítulo11. Validandoosdadosdeentrada
’nome’ => ’required|max:100’,
’descricao’ => ’required|max:255’,
’valor’ => ’required|numeric’
];
}
}
11.3 U sando Form Request ao adicionar
Agoraquetemosaclasseespecialistaemfazerotrabalho,podemostirartoda
acomplexidadedasregrasdevalidaç ãodedentrodométododocontroller.
Elevoltaráaficarassim:
public function adiciona(){
Produto::create(Request::all());
return redirect()
->action(’ProdutoController@lista’)
->withInput(Request::only(’nome’));
}
MasdealgumaformaprecisamosensinaraoLaravelquequeremosapli-
carasregrasdevalidaç ãodo form requestaoexecutaressemétodoe,para
fazerisso,bastaadicionaro ProdutosRequestcomoumargumentodo
método adiciona:
public function adiciona(ProdutosRequest $request){
Produto::create(Request::all());
return redirect()
->action(’ProdutoController@lista’)
->withInput(Request::only(’nome’));
}
Alémdisso,emvezdeutilizaro Request:all()parapegarosparâ-
metrosdarequisição,usaremosopróprio form request.Vejaqueamudan ça
serámínima:
169

## Página 181

11.3. UsandoFormRequestaoadicionar CasadoCódigo
Produto::create($request->all());
Ocódigodométodo adicionaficaráassim:
public function adiciona(ProdutosRequest $request){
Produto::create($request->all());
return redirect()
->action(’ProdutoController@lista’)
->withInput(Request::only(’nome’));
}
Vale lembrar que precisamos adicionar o import da classe
ProdutosRequestnoiníciodonosso ProdutoController:
<?php namespace estoque\Http\Controllers;
use estoque\Produto;
use Request;
use estoque\Http\Requests\ProdutosRequest;
class ProdutoController extends Controller {
// restante do código
Vamostestar?Abrimosoformulárionovamenteetentamosadicionarum
produtosempreenchernenhumdado.Oresultadoserá:
170

## Página 182

CasadoCódigo Capítulo11. Validandoosdadosdeentrada
Fig.11.6:Formuláriodeadiçãosemmensagemdevalidaç ão.
Semprecisarconfigurarnada,automaticamentenossarequisiç ãofoire-
direcionadadevoltaparaoformulário! Claro,sevocêquiserirpraoutro
lugar,bastariaadicionarum ifcomométodo failsassimcomofizemos
anteriormente,masporpadrão,o form requestjáredirecionadevoltapara
apáginaquefezarequisiç ão.Legal,nãoé?Assimevitamosescreveraquele
ifchato.
Masaindanãoestáperfeito,afinal,cadêamensagemdevalidaç ão? O
usuárioprecisadeumfeedbackparasaberoquefezdeerrado. Agorasim
podemosatacaresserequisito.
11.4 E xibindo errors de v alidação
Exibiroserroséumanecessidadecomum,eclaroqueoLaraveljápensou
emumaformadenosajudarnisso. Vocênãoprecisasempreadicionaras
mensagensmanualmente,depoisdecadaerrodevalidaç ão.Issoéfeitoauto-
171

## Página 183

11.4. Exibindoerrorsdevalidação CasadoCódigo
maticamente.
Umavariávelchamada errorsestarádisponívelnaviewapósumou
maiserrosdevalidaç ão.Elatemdiversosmétodos,porexemploo all,que
retornaumarraycomtodasasmensagens. Paratestar,adicioneaseguinte
instruçãoantesdoseuformuláriodeadicionarprodutos:
@foreach($errors->all() as $error)
{{ $error }}
@endforeach
Agorabastatentaradicionarumprodutovazionovamente:
Fig.11.7:Formulárioscomerrosdevalidaç ão.
.
Excelente!Asmensagensdevalidaç ãoforamexibidasassimcomoespe-
rado,masaindamuitofeio,semnenhumaformataç ãoetudonamesmalinha.
Podemosadicionaralgunsestilosdobootstrapparadeixaraaparênciame-
lhor:
<div class="alert alert-danger">
<ul>
172

## Página 184

CasadoCódigo Capítulo11. Validandoosdadosdeentrada
@foreach ($errors->all() as $error)
<li>{{ $error }}</li>
@endforeach
</ul>
</div>
Oresultadoestábemmelhor!
Fig.11.8:Formuláriocomerrosdevalidaç ão.
Sófaltaumúltimodetalhe,quepodeserpercebidoaorecarregaraview
doformulário:
173

## Página 185

11.4. Exibindoerrorsdevalidação CasadoCódigo
Fig.11.9:Divdeerrossemprepresente.
Nãoqueremosexibira divdeerrosquandonãoexistenenhumerrode
validação.Umsimples ifjáresolveráesseproblema:
@if (count($errors) > 0)
<div class="alert alert-danger">
<ul>
@foreach ($errors->all() as $error)
<li>{{ $error }}</li>
@endforeach
</ul>
</div>
@endif
Perfeito!Ocódigofinaldoarquivo formulario.blade.phpdeveficar
assim:
@extends(’layout.principal’)
@section(’conteudo’)
174

## Página 186

CasadoCódigo Capítulo11. Validandoosdadosdeentrada
<h1>Novo produto</h1>
@if (count($errors) > 0)
<div class="alert alert-danger">
<ul>
@foreach ($errors->all() as $error)
<li>{{ $error }}</li>
@endforeach
</ul>
</div>
@endif
<form action="/produtos/adiciona" method="post">
<input type="hidden"
name="_token" value="{{{ csrf_token() }}}" />
<div class="form-group">
<label>Nome</label>
<input name="nome" class="form-control"/>
</div>
<div class="form-group">
<label>Descricao</label>
<input name="descricao" class="form-control"/>
</div>
<div class="form-group">
<label>Valor</label>
<input name="valor" class="form-control"/>
</div>
<div class="form-group">
<label>Quantidade</label>
<input type="number"
name="quantidade" class="form-control"/>
</div>
<button type="submit" class="btn btn-primary
btn-block">Adicionar</button>
</form>
175

## Página 187

11.5. Customizandoasmensagens CasadoCódigo
@stop
11.5 C ustomizando as mensagens
Outropontoimportantíssimorelacionadoàsmensagensdevalidaç ãoéafle-
xibilidadedecustomizá-lasdeacordocomnossavontadeounecessidade.Por
exemplo,eseemvezdemostrar The nome field is requiredeuquisermostrar
umoutrotexto,oumesmoumamensagememportuguês,ondedevoalterar?
Existemdiversasformasdefazerissoe, jáqueestamosusando form
requests, adicionar um novo método chamadomessages é uma de-
las. Quervercomoésimples? Vamoscriaressemétododentrodaclasse
ProdutosRequest. Eledeveretornarumarraycomachaveevalorque
deveseralterado.Porexemplo,sequisermosmudaramensagemde required
elepodeficarassim:
public function messages()
{
return [
’required’ => ’The nome field can not be empty.’,
];
}
Vejaqueamudan çafoimínima,antesera is required(éobrigatório)e
agoramudamospara can not be empty(nãopodeservazio).Claro,sequiser,
tambémpoderiausarumamensagememportuguês.Vamostestar?Ésóabrir
oformulárionovamenteetentaradicionarumnovoprodutosemnenhuma
informaçãopreenchida.
176

## Página 188

CasadoCódigo Capítulo11. Validandoosdadosdeentrada
Fig.11.10:Palavra‘nome’sempreaparecendonamensagemdevalidação.
Ops,aconteceualgoinesperado.Anovamensagemfoiexibidacomsu-
cesso,masagoraficoucomocampo nomefixo.Tenteadicionarumproduto
semdescrição,porexemplo,amensagemaindaestarácomotexto nomeno
lugarde descricao.Comocorrigir?
Emvezdeutilizarovalor nome,experimentemudarpara :attribute
comoaseguir:
public function messages()
{
return [
’required’ => ’The :attribute field can not be empty.’,
];
}
Essavariávelespecialserásubstituídapelovalordocampoqueestásendo
validado.Querver?Tentamosacessarumprodutoembranconovamenteeo
177

## Página 189

11.6. Customizandomensagensdeumcampoespecífico CasadoCódigo
resultadofoi:
Fig.11.11:Mensagemcorreta,comusodo attribute.
Agorasim,osvalores nome, descricaoe valorforamexibidoscor-
retamente.
11.6 C ustomizando mensagens de um campo es-
pecífico
Aoalteraramensagemde required,dentrodaclasse ProdutosRequest,
estamosaplicandoissoparatodososcamposobrigatóriosdesseformulário.
Mashámomentosemquequeremoscustomizaramensagemapenasparaum
campo,comoo nome. Parafazerisso,bastaadicionaroprefixo nome.na
chavedamensagem:
178

## Página 190

CasadoCódigo Capítulo11. Validandoosdadosdeentrada
public function messages()
{
return [
’nome.required’ => ’The :attribute field can not be empty.’,
];
}
Agoraessaregraseráaplicadaapenasparaonome!
Fig.11.12:Mensagemdevalidaç ãodonomecustomizada.
Masaindatemumaquestão,quepodeounãoserumproblema.Eseeu
quiseraplicaressaregraparatodososcamposde nomedaaplicação? Da
formacomofizemos,serianecessáriorepetirocódigoemcada form request
quetivermos.Nolugardisso,sevocêquiseraplicaraalteraç ãoparaaaplica-
179

## Página 191

11.7. Boaprática:experiênciadeuso CasadoCódigo
çãotoda,vocêpodeadicionaramensagemnoarray customdefinidodentro
do validation.phpdapasta resources/lang/en.Elejáestaráassim:
’custom’ => [
’attribute-name’ => [
’rule-name’ => ’custom-message’,
],
],
Issojánosdáumadicadeseuuso.Paraocamponome,porexemplo,o
arrayficariaassim:
’custom’ => [
’nome’ => [
’required’ => ’The :attribute field can not be empty.’,
],
],
Legal,nãoé?Claro,existemdiversasoutrasformasdesevalidarecusto-
mizarasmensagensdoformulário.Sequiser,vocêpodelerumpoucomais
sobrevalidaçãonessapáginadadocumentaç ãodoframework:
http://laravel.com/docs/validation
11.7 B oa prática: experiência de uso
Oproblemadonossocódigoatualéque,apóssubmeteroformuláriocomer-
rosdevalidaç ão,ousuárioseráredirecionadoparaoformulárionovamente,
porémperderátodososdadosquedigitou!
Quandotemospoucoscamposissopodeatépassardespercebido,mas
imaginecomoseriaruimterquedigitarnovamentetodososvaloresdeum
formulárioenormetodavezquepreencherumcampoerrado.
Asoluçãoparaissoésimplesemuitíssimorecomendada. Tudooque
precisamosfazerparamanterosdadosdarequisiç ãoanterior quedeuum
errodevalidaçãopreenchidoséadicionarométodo oldnoatributo value
dosnossos inputs.Umexemploseria:
<input name="nome" value="{{ old(’nome’) }}" />
180

## Página 192

CasadoCódigo Capítulo11. Validandoosdadosdeentrada
Faremos o mesmo com cada um dos inputs do arquivo
formulario.blade.php.Aofinal,nossoHTMLpodeficarassim:
@extends(’layout.principal’)
@section(’conteudo’)
<h1>Novo produto</h1>
@if (count($errors) > 0)
<div class="alert alert-danger">
<ul>
@foreach ($errors->all() as $error)
<li>{{ $error }}</li>
@endforeach
</ul>
</div>
@endif
<form action="/produtos/adiciona" method="post">
<input type="hidden"
name="_token" value="{{{ csrf_token() }}}" />
<div class="form-group">
<label>Nome</label>
<input name="nome"
class="form-control" value="{{ old(’nome’) }}" />
</div>
<div class="form-group">
<label>Descricao</label>
<input name="descricao" class="form-control"
value="{{ old(’descricao’) }}"/>
</div>
<div class="form-group">
<label>Valor</label>
<input name="valor" class="form-control"
value="{{ old(’valor’) }}"/>
</div>
181

## Página 193

11.7. Boaprática:experiênciadeuso CasadoCódigo
<div class="form-group">
<label>Quantidade</label>
<input type="number" name="quantidade"
class="form-control" value="{{ old(’quantidade’) }}"/>
</div>
<button type="submit" class="btn
btn-primary btn-block">Adicionar</button>
</form>
@stop
182

## Página 194

Capítulo12
Autenticaçãoeseguran ça
Umpontofundamentalqueaindanãoexploramosnolivroéquantoàau-
tenticaçãoeseguran çadenossaaplicaç ão.Daformaqueestá,qualquerum
visualiza,criaouapagaprodutos,masnemsemprepodemospermitirque
issoaconte ça. VeremosnessecapítulocomooLaravelnosajudacomesse
trabalho,comusodeseusfamosos middlewaresemecanismode Auth.
12.1 T ela de login e autenticação
Agrandeverdadeéquetudoestápronto,emumaaplicaç ãorealvocêprova-
velmenteprecisarámudarumououtrodetalhe,masboapartedocódigoserá
totalmentereutilizadaemseusprojetos.
Paratestar,precisaremosvoltaraquelaslinhasqueapagamosdoarquivo
routes.phpnoprimeirocapítulo. Nãosepreocupesenãolembrar,oim-
portanteésaberquequandovocêcriaumaaplicaç ãooseguinteconteúdojá

## Página 195

12.1. Teladelogineautenticação CasadoCódigo
vemregistradonosarquivoderotas:
Route::get(’home’, ’HomeController@index’);
Route::controllers([
’auth’ => ’Auth\AuthController’,
’password’ => ’Auth\PasswordController’,
]);
Copienovamenteparalá.Seu routes.phppodeficarassim:
Route::get(’/produtos’, ’ProdutoController@lista’);
// outras rotas omitidas
Route::get(’home’, ’HomeController@index’);
Route::controllers([
’auth’ => ’Auth\AuthController’,
’password’ => ’Auth\PasswordController’,
]);
Ótimo!Vejaqueháumarota /homeapontandoparaométodo index
do HomeController,quetambémdevetersidocriadoautomaticamente
comoprojeto.Casoesse controllernãoexistaemseuprojeto,vocêpode
criá-lomanualmentecomoseguinteconteúdo:
<?php namespace estoque\Http\Controllers;
class HomeController extends Controller {
public function __construct()
{
$this->middleware(’auth’);
}
public function index()
{
return view(’home’);
}
}
184

## Página 196

CasadoCódigo Capítulo12. Autenticaçãoeseguran ça
Nãosepreocupeementenderoconstrutordessaclasse,pelomenospor
enquanto. Embreveseuusoficarábemclaro. Alémdisso,vejaqueomé-
todo indexretornauma viewchamada home.Crietambémessearquivo,
chamado home.blade.php,comoseguinteconteúdo:
@extends(’app’)
@section(’content’)
<div class="container">
<div class="row">
<div class="col-md-10 col-md-offset-1">
<div class="panel panel-default">
<div class="panel-heading">Home</div>
<div class="panel-body">
You are logged in!
</div>
</div>
</div>
</div>
</div>
@endsection
Vamosveroquetemládentro?Ésóacessar: http://localhost:8000/home.
Talvezparagrandesurpresa,oresultadoaotentaracessaressaURLserá
umredirecionamentoparaateladelogin. Issomesmo,essatelajáexistee,
porsinal,tudoqueexistenelajáfunciona!
185

## Página 197

12.1. Teladelogineautenticação CasadoCódigo
Fig.12.1:Viewcomformuláriodelogin.
Vejaque,alémdoformuláriodelogin,elaofereceumaop çãodereset
desenhaeregistrodenovosusuários. Vamostestar? Comonãotemosne-
nhumusuáriocadastrado,podemoscriarumnovoregistroclicandonaop ção
Registerdocantodireitodomenu.
186

## Página 198

CasadoCódigo Capítulo12. Autenticaçãoeseguran ça
Fig.12.2:Formulárioderegistrodeusuários.
Preenchaoformulárioecliquenobotãodesubmitparaveroresultado.
Ousuárioserácriado,evocêseráredirecionadoparaatela /home,quees-
tavaprotegidaporlogin.Logoveremosessapartedeseguran ça,comolimitar
acessoaosrecursosdaaplicaç ãoetudomais,masporenquanto,vamosentrar
umpoucomaisafundonessafuncionalidadedelogin.
187

## Página 199

12.2. Entendendoologindaaplicação CasadoCódigo
Fig.12.3:ViewpadrãodaURL/home.
Reparequeonomedeseuusuárioestarádisponívelnomenuprincipale,
aoserclicado,exibiráaop çãodelogout.Masondetudoissoestádefinido?
Comofoicriado?Comomodificar?
12.2 E ntendendo o login da aplicação
Vouresponderessasperguntasporpartes,ok?Primeirovamosentenderonde
essas viewsforamdefinidasealgunsdetalhesdesuaimplementaç ão.
188

## Página 200

CasadoCódigo Capítulo12. Autenticaçãoeseguran ça
Fig.12.4:Diretóriocomarquivosdeautenticaç ão.
Vejaqueapasta resources/views/authmantémtodasaspáginasre-
lacionadasaessalógicadeautenticaç ão.Podemossimapagartudoerecriar
todasasviews,formulários,validaçãoetc.Masenopróximoprojeto?Apaga-
mosefazemostudodenovo?Vaisertudomuitoparecido.Valelembrarque
agrandesacadadoframeworkéessa,ofereceroqueexisteemcomumentre
todososprojetos,pravocêgastarseutemponoquerealmenteimporta.
Vocêpodeedeveeditar,adicionarnovoscamposefazerqualqueradap-
taçãoquefornecessáriodeacordocomasnecessidadesdoseuprojeto,mas
comcertezaissoserámaisfácilagoraquetudojáestápronto.
Vejaqueapágina home.blade.phpébemsimples,temapenasumpai-
nelquemostraamensagemdequeousuárioestálogado:
@extends(’app’)
@section(’content’)
<div class="container">
<div class="row">
<div class="col-md-10 col-md-offset-1">
<div class="panel panel-default">
<div class="panel-heading">Home</div>
189

## Página 201

12.2. Entendendoologindaaplicação CasadoCódigo
<div class="panel-body">
You are logged in!
</div>
</div>
</div>
</div>
</div>
@endsection
Umdetalhequequeroquevejamnessearquivoéqueeleherdade app,
queéolayoutprincipalquejávemprontonoLaravel.Essaéacerejadobolo,
olugarondeomecanismodeautenticaç ãodoframeworkcome çaaaparecer.
Abraoarquivo app.blade.phpevejaqueeleémuitoparecidocomnosso
layoutprincipal,o principal.blade.php. Agrandediferen çaestáno
navbar,quefazum ifverificandoseousuárioestálogadoounão:
<ul class="nav navbar-nav navbar-right">
@if (Auth::guest())
<li><a href="/auth/login">Login</a></li>
<li><a href="/auth/register">Register</a></li>
@else
<li class="dropdown">
<a href="#" class="dropdown-toggle"
data-toggle="dropdown" role="button"
aria-expanded="false">
{{ Auth::user()->name }}
<span class="caret"></span>
</a>
<ul class="dropdown-menu" role="menu">
<li><a href="/auth/logout">Logout</a></li>
</ul>
</li>
@endif
</ul>
HádoispontosimportantíssimosnessetrechodeHTMLe,emambos,a
interface Authfoiutilizada. Essainterface(facade)équemnosajudacom
boapartedotrabalhodeautenticaç ão.Vamosentendercomoelafunciona?
190

## Página 202

CasadoCódigo Capítulo12. Autenticaçãoeseguran ça
Vejaqueno ifométodo guest(convidado)éverificado.Essemétodo,
comovocêjádeveimaginar,determinaseousuáriojáestálogadonaapli-
cação.Eleébastanteútilemdiferentescamadasdonossoprojeto:Naview,
paradeterminarseonomedousuáriooulinkdelogindeveserexibido,no
controllerouqualquercamadaintermediáriadeautorizaç ãoparaverificarse
ousuáriopodeounãoacessaroconteúdoetc.
Outrométodointeressanteutilizadoporessaviewéo user,queretorna
umainstânciadousuáriologadonaaplicaç ão.Reparequeeleéutilizadopara
exibironomedonossousuárionoseguintetrechodocódigo:
{{ Auth::user()->name }}
Legal!Masequantoaocódigodeautenticaç ãoemsi,usadoparalogarou
deslogarumusuário?Bem,emvezdeapenasficarnateoria,quetalcriarmos
onossoprópriosistemadeloginsópordiversão?Ocódigoserámaissimples
doqueparece.
12.3 C riando uma lógica de autenticação
Paracome çar,podemoscriarumnovocontrollerondeficarátodaessalógica
deautenticação.Vamoschamá-lode LoginControllere,lembrando,ele
deveráficardentrode app/Http/Controllers.Antesdecriaroarquivo
edigitartudo,quetaldessavezusaro artisan?Assimcomofizemospra
criaromodelo,tambémpodemosusarocomando make:controller.
php artisan make:controller LoginController --plain
Esse --plainquepassamoscomoargumentosignificaquenãoquere-
mosqueelecrienenhummétodo.Deveserumcontrollerembranco.Sem
essaop ção,eleadicionaráumasériedemétodoscomunsparaasoperações
básicasdeadicionar,listar,removeretc.Ofamoso CRUD.
191

## Página 203

12.3. Criandoumalógicadeautenticação CasadoCódigo
Fig.12.5:CriandocontrollercomArtisan.
Oresultadoseráumamensagemdesucessoepronto,podemosabriro
arquivo LoginControllerquejáestaráassim:
<?php namespace estoque\Http\Controllers;
use estoque\Http\Requests;
use estoque\Http\Controllers\Controller;
use Illuminate\Http\Request;
class LoginController extends Controller {
//
}
Vamosagoracriarumnovométodo,chamado login:
public function login()
{
// código vai aqui
}
Emumcasotradicionalcriaríamostambémummétodoqueenviapara
aviewdeformulário,quefariaum POSTcomosdadosparaessaaç ãode
login,mascomoestamosapenastestandoenãoqueremosreinventararoda
,passaremosousuárioesenhadiretopelaURL.
Noarquivoderotas, vamosensinaraoLaravelqueaoacessaraURI
/loginnossométododelogindeveráserchamado:
Route::get(’/login’, ’LoginController@login’);
192

## Página 204

CasadoCódigo Capítulo12. Autenticaçãoeseguran ça
Quasetudopronto,jápodemoscome çarocódigodeautenticaç ão. No
método login,queremospegaro emaile password,verificarseeleé
validoe,emcasodesucesso,retornarumamensagemcomonomedousuário
logado;casocontrário,umerro.Emresumo,ocódigoficaráassim:
public function login()
{
$credenciais = Request::only(’email’, ’password’);
if( /*credenciais são válidas*/ ) {
return "Usuário NOME logado com sucesso";
}
return "As credencias não são válidas";
}
Mascomosaberseousuárioexisteemnossobancodedados?Podería-
mossimescreverumSQLqueprocuraousuáriopore-mailesenha,maso
Authjácuidadessetrabalhoparanãotermosquenospreocuparnemcom
isso. Quervercomoésimples? Bastapassaro arraycome-mailesenha
paraseumétodo attempt:
public function login()
{
$credenciais = Request::only(’email’, ’password’);
if(Auth::attempt($credenciais)) {
return "Usuário NOME logado com sucesso";
}
return "As credencias não são válidas";
}
Alémdee-mailesenha,vocêpodepassarqualquerinformaç ãoválidado
usuáriocomoparâmetronoarraydecredenciais.
Valelembrarqueparausaro Authdentrodocontrollerprecisaremos
fazero import.Aclasse LoginControllercompletadeveficarassim:
193

## Página 205

12.3. Criandoumalógicadeautenticação CasadoCódigo
<?php namespace estoque\Http\Controllers;
use estoque\Http\Requests;
use estoque\Http\Controllers\Controller;
use Auth;
use Request;
class LoginController extends Controller {
public function login()
{
$credenciais = Request::only(’email’, ’password’);
if(Auth::attempt($credenciais)) {
return "Usuário NOME logado com sucesso";
}
return "As credencias não são válidas";
}
}
Vamostestar? Primeirotenteacessaralógicadelogincomumusuário
inválido. Umexemploseria:http://localhost:8000/login?email=teste@teste.
com.br&password=123456
Fig.12.6:Mensagemdecredenciasinválidas.
A mensagemAs credencias não são válidas foi exibida como espe-
rado. Experimenteagorapassarologinesenhaquevocêregistrouante-
194

## Página 206

CasadoCódigo Capítulo12. Autenticaçãoeseguran ça
riormente. Emmeucaso,será: http://localhost:8000/login?email=rodrigo.
turini@caelum.com.br&password=123456
Fig.12.7:Mensagemdesucesso,porémcomapalavra‘nome’fixo.
Sucesso!Masnolugarde NOME,queremosmostraronomedousuário
autenticado.Lembracomosefaz?Ésóutilizarométodo usereacessara
propriedadequevocêquiser.Ocódigoficarádeseguinteforma:
if(Auth::attempt($credenciais)) {
return "Usuário ".
Auth::user()->name
." logado com sucesso";
}
Agorasim,aoacessaraURLnovamenteoresultadoserá:
Fig.12.8:Mensagemdeconfirmaç ãodelogin.
Hámaisummontederecursosinteressantesno Auth.Porexemplo,se
vocêquiserusarafunção“lembrarasenha”nasuaaplicação,vocêpodepassar
195

## Página 207

12.3. Criandoumalógicadeautenticação CasadoCódigo
um booleancomosegundoargumentoparaométodo attempt.Ousuário
vaificarautenticadoportempoindefinidoouatéalguémmanualmentefazer
o logout.
if(Auth::attempt($credenciais, true)) {
//...
}
Porsinal,fazero logouttambémébemsimples!Repare:
Auth::logout();
Háaindaumasériedemétodosquepodemecomcertezaserãoúteis.
Algunsdelessão:
// verifica apenas se as credenciais são
// válidas, sem necessariamente se logar
Auth::validate($credentials);
// para logar um usuário de determinado id
Auth::loginUsingId(7);
// para ver se o usuário está logado
Auth::check();
// ou então, verificar o próprio usuário
Auth::user();
Legal,nãoé?Masvalelembrardequeapartedeautenticaç ãojáestátoda
pronta,dificilmentevamosusartodosessesmétodos.
AgoraquejáconhecemosumpoucodecomooLaravelcuidadaauten-
ticação,vamosentraremoutropontomuitoimportante:aautorizaç ão.Não
bastaestarlogado,énecessárioestabeleceroqueousuáriopodeounãoaces-
sar.
Sequiser,aproveiteparaexplorarumpoucomaisantesdeprosseguir.Que
talmudarotemplatedaspáginasdeautenticaç ãoparausaro principal?
Alémdisso,vocêpodeadicionaro ifnesselayoutparaverificarseousuário
estálogadoounão,mostrandoonomeouoslinksdeloginassimcomoo
196

## Página 208

CasadoCódigo Capítulo12. Autenticaçãoeseguran ça
app.blade.phpfaz.Fiqueàvontadeparafazeressaseoutrasalteraçõesno
sistema,éumaexcelenteoportunidadepararelembraralgunsrecursosque
vimosatéaqui.
12.4 A utorização com Middlew ares
Aquestãodologinfoiexplorada,sabemosqueissojáestápronto,masmesmo
semestaremlogadososusuáriosdanossaaplicaç ãoaindaconseguemvisu-
alizar,adicionareexcluirprodutos. Nãoqueremosqueissoaconte ça,esses
devemserprivilégiosexclusivosparaquemestáautenticado.
Noiníciodocapítulo,quandoacessamosaURI /homepelaprimeira
vez,fomosredirecionadosparaumateladelogin. Issoaconteceuporque,
dealgumaforma,foiconfiguradoqueparaacessaressalógicaeranecessário
estarautenticadonoprojeto.Queremosomesmo,masondeconfigurar?
Poderíamosfazerissodediversasformas. Umexemploseriavalidando
noprópriométodo,comonoexemploaseguirdométodo remove:
public function remove($id){
if (Auth:guest())
{
return redirect(’/auth/login’);
}
$produto = Produto::find($id);
$produto->delete();
return redirect()->action(’ProdutoController@lista’);
}
Vejaqueumsimples ifresolveoproblema.Aotentarremoverumpro-
dutosemestarlogado,ousuárioseráredirecionadoparaateladelogin. É
exatamenteoqueprecisamos!Porém,imaginesóaquantidadedevezesque
vamosprecisarrepetiresse if?Muitas.Equantomaiorforoprojeto,mas
ifsrepetidos.Seriainviável.
Éaíqueentrao Middleware. Elefuncionacomoumfiltro,poronde
passamtodasasrequisiçõesHTTPantesdechegaremnossoscontrollers.
Onomepodeparecerintimidador,masnãohánadademuitocomplicado.
Querver?Antesdesairusandoos Middlewaresexistentes,vamoscriarnossa
própriaregradeautenticaç ão.
197

## Página 209

12.4. AutorizaçãocomMiddlewares CasadoCódigo
Em vez de criar a classe manualmente, podemos usar o comando
make:middlewaredoArtisanparafazeressetrabalhopornós.Vejacomo
ésimples:
php artisan make:middleware AutorizacaoMiddleware
Fig.12.9:Middlewaredeautorizaç ão[[
Agorabastaabriroarquivo AutorizacaoMiddlewaredentrododi-
retório app/Http/Middlewareeaseguinteestruturaestarápronta:
<?php namespace estoque\Http\Middleware;
use Closure;
class AutorizacaoMiddleware {
/**
* Handle an incoming request.
*
* @param \Illuminate\Http\Request $request
* @param \Closure $next
* @return mixed
*/
public function handle($request, Closure $next)
{
return $next($request);
}
}
198

## Página 210

CasadoCódigo Capítulo12. Autenticaçãoeseguran ça
Todootrabalhoacontecenessemétodochamado handle,queéexe-
cutadosemprequeumanovarequisiç ãoéfeitaemnossaaplicaç ão. Repare
queelerecebecomoargumentoa $requestcomosdadosdarequisiç ão
atualetambémuma Closurechamada $next.Essesegundoargumento
éoresponsávelpordeterminarounãosenossocontrollerseráchamado.Se
ométodo handlenãoretornar $next($request)daformaqueestá,a
aplicaçãoficaráparadanesseponto.
Deformaprática,podemosfazeralgocomo:
public function handle($request, Closure $next)
{
if(/* não pode acessar */) {
return redirect(’/auth/login’);
}
return $next($request);
}
Vejaque,nessecaso,quandoousuárionãotiveracessoaumadetermi-
nadalógicaouURI,redirecionamosparaapáginadeautenticaç ão.Casocon-
trário,retornamoso $next($request)quecontinuarácomaexecuçãodo
nossocódigonormalmente.
Simples,nãoé? Masoquecolocarnesse if? Arespostaé: depende
danossanecessidade. Vocêpodefazerdesdeconsultasnobancodedados
paraverificaroprivilégiodousuárioedeacordocomelepermitiroacesso
ounão,atéumsimples Auth:guestparaverificarseousuárioestálogado,
queéjustamenteoqueprecisamosnestemomento.
Ocódigoficaráassim:
public function handle($request, Closure $next)
{
if(\Auth::guest()) {
return redirect(’/auth/login’);
}
return $next($request);
}
Excelente,masagoraqueo middlewareestácriado,todasasrequisições
vãopassarporele? Nóssomosquemdecidimos. Sequisermosfazerisso,
199

## Página 211

12.4. AutorizaçãocomMiddlewares CasadoCódigo
bastariaadicionaronomedessanossaclassenoatributo $middlewarede
umaclassechamada Kernel,presentenodiretório app/Http.
Aoabriressaclasse,elaestaráparecidacom:
<?php namespace estoque\Http;
class Kernel extends HttpKernel {
/**
* The application’s global HTTP middleware stack.
*
* @var array
*/
protected $middleware = [
// outros registros omitidos
’Illuminate\Session\Middleware\StartSession’,
’Illuminate\View\Middleware\ShareErrorsFromSession’,
’estoque\Http\Middleware\VerifyCsrfToken’,
’estoque\Http\Middleware\AutorizacaoMiddleware’,
];
/**
* The application’s route middleware.
*
* @var array
*/
protected $routeMiddleware = [
’auth’ => ’estoque\Http\Middleware\Authenticate’,
’auth.basic’ => ’Illuminate\Auth\Middleware
\AuthenticateWithBasicAuth’,
’guest’ => ’estoque\Http\Middleware
\RedirectIfAuthenticated’,
];
}
Observequeessaclassepossuidoisarrays,chamados $middlewaree
$routeMiddleware.Oprimeiroéutilizadosemprequequisermosqueum
middlewaresejaexecutado em todas as requisições.Bastariaadicionarnossa
classenessearrayepronto,masissoseriaumgrandeproblema.
200

## Página 212

CasadoCódigo Capítulo12. Autenticaçãoeseguran ça
Onossocódigosempreverificaseousuárioestálogadoe,casonãoes-
teja,redirecionaparaateladelogin. Como toda requisi ção passarápelo
middleware,elenovamenteverificaráseestálogado,eredirecionaráoutravez
paraateladelogin.Ocódigoentraráem loopingderedirect.
Fig.12.10:Páginaemredirectloop.
Eagora?Asoluç ãoésimples,bastariaadicionarumacondiç ãono ifque
verifiquequea requestacessadanãoéade auth/login:
public function handle($request, Closure $next)
{
if(!$request->is(’auth/login’) && \Auth::guest()) {
return redirect(’/auth/login’);
}
return $next($request);
}
Excelente,problemado loopresolvido.Façaasalteraçõesparatestar,ao
acessarqualquerURLenquantoestiverdeslogado,vocêseráredirecionado
paraateladelogin.
201

## Página 213

12.5. Registrandoomiddlewarepararotasespecíficas CasadoCódigo
12.5 R egistrando o middlew are para rotas espe-
cíficas
Imagineagoraquequeremosbloquearapenasalgumasrotas,comoadeadi-
cionareremoverproduto,masasdemaisdevemserliberadas.Ousuárionão
precisaráestarlogadoparaacessaralistagem,porexemplo.
DamesmaformacomofizemoscomaURIdelogin,podemosiradicio-
nandocondiçõesparaliberaraspáginasdelistagem,detalhesdoprodutoou
qualqueroutraquequisermos,masoproblemadessasoluç ãoéqueatodo
momentoqueumanovapáginaquenãodeveserbloqueadaforcriada,pre-
cisaremoslembrardeadicionarumanovacondiç ãono middleware. Além
disso,ocódigoficariabemfeito,cheiode ifsoucomumúnico ifenorme!
Nolugardisso,oLaravelnosofereceapossibilidadedeativarum mid-
dlewarepararotasespecíficas.Lembraqueaclasse Kerneltinhadoisarrays,
o middlewareeo $routeMiddleware?Poisbem,essesegundoatributo
servejustamenteparaisso.
Vamosremovernossaclassedoarray middlewaree, emvezdisso,
adicioná-laao $routeMiddlewarecomoaseguir:
protected $routeMiddleware = [
’auth’ => ’estoque\Http\Middleware
\Authenticate’,
’auth.basic’ => ’Illuminate\Auth\Middleware
\AuthenticateWithBasicAuth’,
’guest’ => ’estoque\Http\Middleware
\RedirectIfAuthenticated’,
’nosso-middleware’ => ’estoque\Http
\Middleware\AutorizacaoMiddleware’,
];
Veja que já existem outrosmiddlewaresregistrados nesse array tam-
bém, logo falaremos sobre eles. O importante agora é perceber
que nesse caso associamos a chave nosso-middleware ao nosso
AutorizacaoMiddleware.
202

## Página 214

CasadoCódigo Capítulo12. Autenticaçãoeseguran ça
Associando middlewares com a rota
Agoraquejáestáregistrado,precisamosassociaro nosso-middleware
àsrotasquedevemserfiltradas.Existemdiversasformasdefazerisso,euma
delasépeloarquivo routes.php.
Route::get(’/produtos/remove/{id}’, [
’middleware’ => ’nosso-middleware’,
’uses’ => ’ProdutoController@remove’
]);
Oproblemadessaabordageméquealémdepoluirbastanteonossoar-
quivoderotas,aindanosobrigaarepetiressaslinhasdo middlewareemcada
umadelas.
Associando middlewares ao controller
Emvezdisso,podemospartirparaumcaminhobemmaisinteressante,
queéregistraro middlewarenoconstrutordonossocontroller.Vejacomoé
simples:
<?php namespace estoque\Http\Controllers;
use estoque\Produto;
use Request;
use estoque\Http\Requests\ProdutosRequest;
class ProdutoController extends Controller {
public function __construct()
{
$this->middleware(’nosso-middleware’);
}
// restante do código omitido
}
Masaindanãoéoquequeremos,poisissofarácomquetodososmétodos
docontrollerpassempelofiltrodo middleware,ouseja,aotentaracessara
listagemnovamenteseremosredirecionadosparaateladelogin.
203

## Página 215

12.5. Registrandoomiddlewarepararotasespecíficas CasadoCódigo
Paraevitarisso,podemospassarcomosegundoargumentoapenasosmé-
todosemquequeremosaplicaresse middleware:
public function __construct()
{
$this->middleware(’nosso-middleware’,
[’only’ => [’adiciona’, ’remove’]]);
}
Nestecaso,apenasométodo adicionae removeserãofiltrados,to-
dososdemaisfuncionarãonormalmentemesmosemousuárioestarlogado.
Alémdo only,vocêtambémpodeutilizarachave exceptparadizerquais
métodosnãodevemserfiltrados.
Vamostestarasalterações? Primeiroacessandoalistagemdeprodutos.
Tudodevefuncionar:
Fig.12.11:Listagemdeprodutos.
Agoratenteremoverumdosprodutos:
204

## Página 216

CasadoCódigo Capítulo12. Autenticaçãoeseguran ça
Fig.12.12:Páginadelogin.
Sucesso!Fomosredirecionadosparaateladelogin.
12.6 U tilizando o middlew are padrão
Vimoscomocriareregistrarnossopróprio middleware,afinal,éumrecurso
importantíssimo.Mas,narealidade,paraumcasosimplescomoesseocódigo
todojáestápronto,portantonãoprecisaríamosdessetrabalhotodo.
Experimentemudaroconstrutordocontrollerparaqueutilizeum mid-
dlewarechamado auth:
<?php namespace estoque\Http\Controllers;
use estoque\Produto;
use Request;
use estoque\Http\Requests\ProdutosRequest;
class ProdutoController extends Controller {
public function __construct()
{
$this->middleware(’auth’,
205

## Página 217

12.6. Utilizandoomiddlewarepadrão CasadoCódigo
[’only’ => [ ’adiciona’, ’remove’]]);
}
// restante do código omitido
}
Oefeitoseráomesmo.Legal,nãoé?OLaravelnosentregademãobeijada
todaapartedeautenticaç ãoeautorizaç ão.
206

## Página 218

Capítulo13
MaisprodutividadecomArtisan
Duranteolivro,vimosumrecursomuitoatrativodoLaravel,o Artisan.
Essaferramentadelinhadecomandonostornaaindamaisprodutivos,pois
cuidadeboapartedocódigode boilerplate.Aocriarumnovomodelo,por
exemplo,precisamoslembrardeadicionaro namespace,dizerqueeleherda
de Model,adicionaroimportparaa superclasseetc.Muitotrabalho,nãoé?E
ésempreamesmacoisa,sómudaonomedaclasse.Éaíqueo Artisanentra,
umsimplescomandoepronto,todaessarotinaseráfeitaparanós.
Masaferramentanãoparaporaí. Alémdecriarmodelos,controllers,
formrequests,entreoutros,elatambémnosoferecediversosrecursoscomo
o serve,utilizadopararodaraaplicaç ãonoservidordedesenvolvimentodo
Laravel.Muitoconveniente!O Artisanéumverdadeirocintodeutilidades
doprogramadorprodutivo.

## Página 219

13.1. Comolembrardetodososcomandos? CasadoCódigo
13.1 C omo lembrar de todos os comandos?
Éfundamentalteremmentequequantomaiscomandosvocêconhecer,mais
proveitovocêvaitirardaferramenta.Mas,levandoemconsideraç ãoqueexis-
temdiversos,comoseriapossíveldecorartodos? Arespostaésimples:não
decore!Oúnicocomandodequevocêprecisaselembraréo list,quere-
tornaumalistacomtodasasop çõesdisponíveis.Sabendolereinterpretara
saídadessecomando,vocêconsegueusarqualqueroutro.
Vamospôrasmãosnamassa?Abraoterminale,dedentrodapastade
seuprojeto,executeocomando:
php artisan list
Fig.13.1:ListagemdecomandosdoArtisan.
Umalistanemumpoucopequenadecomandosdisponíveisseráexibida.
Aquivaiumresumosobreosprincipaisdelesetambémalgunsexemplosprá-
ticos.Vocêpodeedeveirtestandotodososcomandosquequiserconhecer
melhor.
•down:colocaaaplicaç ãoemmododemanuten ção.Paratestar,expe-
rimenterodar php artisan down eacessarqualquerURLdasua
aplicação.Oresultadoseráparecidocom:
208

## Página 220

CasadoCódigo Capítulo13. MaisprodutividadecomArtisan
Fig.13.2:Aplicaçãodomododemanuten ção.
•up:tiraaaplicaç ãodomododemanuten ção.Sevocêfezotesteante-
rior,bastarodar php artisan up paraquetudovolteaonormal.
Fig.13.3:Comandosdowneuppeloterminal.
•help:exibeinformaçõesdeajudaparaumcomando.Porexemplo,se
euquerosabercomoocomando php artisan list funciona,basta
digitar php artisan help list.Ospossíveisargumentos,op ções
ealgunsexemplosserãoexibidoscomoaseguir:
209

## Página 221

13.1. Comolembrardetodososcomandos? CasadoCódigo
Fig.13.4:Informaçõesdeajudadocomandolist.
•tinker:interagecomsuaaplicaç ão.Essecomandoémuitoútilepode-
roso.Épossívelexecutarquerysnobancodedados,utilizarqualquer
classedoprojetoetc.
210

## Página 222

CasadoCódigo Capítulo13. MaisprodutividadecomArtisan
Fig.13.5:AcessandodadosdobancopeloArtisanTinker.
•list:listatodososcomandos.
•optimize:otimizaaperformancedoframework.
•serve:sobeoservidordedesenvolvimentodoPHP.
•app:name:adicionaonamespacedaaplicaç ão.
Oscomandosaseguir,queinclusivejáutilizamos,têmcomopropósitoa
criaçãodeclasses.
•make:console:criaumnovocomandodoArtisan.
•make:controller:criaumnovocontroller.
•make:middleware:criaumnovomiddleware.
•make:model:criaumnovomodelodoEloquent.
211

## Página 223

13.1. Comolembrardetodososcomandos? CasadoCódigo
•make:request:criaumnovoformrequest.
Háaindaopçõesinteressantesparacontroledecacheeotimizações.
•cache:clear:limpaocachedaaplicaç ão.
•config:cache:criaumarquivodecachedeixandoaconsultadeconfi-
guraçõesmaisrápida.
•config:clear:removeoarquivodecachedeconfigurações.
Porfim,algunsquenosajudamcomrotas:
•route:cache:criaumarquivodecacheparadeixaroregistroderotas
maisrápido.
•route:clear:removeoarquivodecachederotas.
•route:list: listatodasasrotasregistradas. Estecomandoéespecial-
menteútil!Experimenteexecutar php artisan route:list para
veroresultado.AlémdeexibirasURIs,osmétodosHTTP,actionse
middlewareassociadosaelesserãodetalhados.
Essessãoapenasalgunsdosmuitoscomandosexistentes,aproveitepara
explorartodasessasfuncionalidades.Conhecerrecursosqueosframeworks
nosofereceméumgrandediferencial,poistornanossodiaadiamuitomais
produtivoedivertido.
212

## Página 224

Capítulo14
Ospróximospassos
Existemdiversasformasparavocêcontinuarseusestudos. Eurecomendo
fortementequevocêexercitetodososcódigosescritosnoscapítulosdesse
livro,quepodemserencontradosnorepositório:
https://github.com/Turini/estoque-laravel
Paracriarumaintimidadeaindamaiorcomoframework,experimente
passearporsuadocumentaç ãoetestarcenáriosalémdosaquisugeridos.Co-
loqueamãonamassa.Apartirdeagora,descobrirnovosrecursos,utilizar
novosframeworksetc.passaaserseutrabalhododiaadia.
Bonsestudos!