---json
{
  "id": "rspec_crie_especifica__es_execut_veis_em_ruby_1",
  "title": "RSpec Crie especificações executáveis em Ruby",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "**Arquivo Original:** `RSpec Crie especificações executáveis em Ruby.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "crie",
    "especifica",
    "execut",
    "linguagens",
    "php",
    "rspec",
    "ruby",
    "veis"
  ],
  "perguntas_tipo": [
    "Como utilizar RSpec Crie especificações executáveis em Ruby?",
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

# RSpec Crie especificações executáveis em Ruby

> **Arquivo Original:** `RSpec Crie especificações executáveis em Ruby.pdf`
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
Agradecimentos
MuitoobrigadoàminhaMãeeaomeuPai,MariaNilzaeJoséMauro,porme
apoiarememtudoeestaremsempreaomeulado.
ComoolivronãopoderiaexistirsemoRuby,obrigadoaoMatzeaoRuby
Coreteamporcriarumalinguagemorientadaaobjetostãodivertidaeex-
pressiva.EaoDavidHeinemeierHanssonetodooRailsteamporcriarum
frameworkwebquetornaonossotrabalhomuitomaisdivertido.Eatodosos
criadores,mantenedoresecontribuidoresdasferramentasqueveremosaqui
comoWebMock,VCRefactory_girl.
ObrigadoatodosdaCasadoCódigoporacreditaremnoprojetoeaju-
darematorná-lorealidade.EspecialmenteaoAdrianoeàVivian,porterem
quelidardiretamentecomomeuexcelenteconhecimentodeportuguês.
ObrigadoàHE:labsportudooquetenhoaprendidoeproduzido.Obri-
gadoaoRafaelLimaeaoSylvestreMergulhão,donosdaHE:labs,porapoia-
remomeuprojetodolivroetorná-loumaparceriacomaHE:labs.
ObrigadoaoCayoMedeiros(Yogodoshi),porsempremedarexcelentes
dicasemqualquernovoprojetoqueinicioouiniciamosjuntos.
ObrigadoàJéssica,minhanamoradaefuturaesposa.=)Pormeaturarhá
maisde6anosesempreestaraomeuladomeapoiandonasminhasdecisões
efazendoaminhavidamuitomaisfeliz!
i

## Página 5

CasadoCódigo
SobreoAutor
MauroGeorgeatualmenteédesenvolvedordesoftwarenaHE:labs,ondetra-
balhacomRubyeAgilenoseudiaadia.Commaisdeseisanosdeexperi-
ênciacomdesenvolvimentoweb,temcontribuídoemdiversosprojetosopen
source,incluindooshoulda-matchers,játendofeitoumapequenacontri-
buiçãonoRails. Épalestranteeapaixonadoporvídeogamedesdesempre,
tambémesóciodoEstouJogando.
iii

## Página 7

CasadoCódigo
AHE:labs
AHE:labsfazprodutoswebfantásticosdesdeaideiaaolan çamento. Isso
incluiaplicativos,e-commerce,sistemascorporativos,aplicativosemcloud
equalquertipodesoftwareparainternet. UtilizandodeDesign Thinking,
LeanStartupeDesenvolvimentoÁgilparatransformarasuaideiaemum
produtoreal. Possuiumaequipemultidisciplinarcompostaporprograma-
dores,analistas,designersehackers.Paraconhecerumpoucomais,acesse:
http://helabs.com.br.
v

## Página 9

CasadoCódigo
Introdução
Sejabem-vindo! ORubytemumexcelenteambientedetestescomferra-
mentascomoMiniTest,RSpeceCucumber. Masoquepodemosmelhorar
nonossoTDDdodiaadia?Qualopróximopasso?Alémdepadrõesecon-
vençõesbemdefinidasquepodemosseguir,temosdiversasferramentasque
ajudamenquantoescrevemosnossostestes.Trabalhandoemdiversostimese
emprojetosopensource,pudenotarquecertostesteseramescritosdeforma
complicada,sempadrões,apenas happy pathseramtestados,projetoscom
baixacoberturadetestes,faltadeconhecimentodebibliotecasqueajudariam
noprocessodetesteetc.
Edesteseoutrosproblemassurgiuaideiadolivro: mostrartécnicase
ferramentasquetendemamelhoraronossoprocessodeescrevertestes.
Sendoassimoobjetivodolivroéquevocêsaiadaqui:
• escrevendomelhorosseustestes,seguindoconvençõeseboaspráticas
queserãoabordadas;
• esteja equipado com uma coleção de ferramentas e técnicas para
quandoenfrentarproblemasduranteoprocessodeTDD.
EuvouaprenderaescrevertestesemRuby?
OlivronãoéumaintroduçãoaoRSpecouTDD.Assume-sequeoleitor
tenhaconhecimentodoRSpecouqualqueroutrabibliotecadetestesemRuby
equeestejahabituadoaoprocessodeTDD.
vii

## Página 10

CasadoCódigo
UtilizooMinitest/Test::Unit,estelivroserveparamim?
Sim. UtilizamosoRSpecnosexemplos,masmuitasdastécnicasefer-
ramentaspodemserutilizadasindependentedaferramentadetestes.Lem-
brandoquetambémpassamosporcaracterísticasexclusivasdoRSpec.
Sobreaabordagem
UtilizamosnamaiorpartedotempoTDDenquantoestamosescrevendo
osexemplos,come çandopelotesteeseguindoparaaimplementaç ão.
Propositalmente,utilizamosumdomíniodaaplicaçãosimples,dadoque
onossofocoaquiénapartedostestes.
UtilizamosumaaplicaçãoemRubyonRails,dadoqueamaioriadosini-
ciantescomeçapeloRailsparasódepoisaprenderRuby. Sendoassim,os
maisexperientesnãoterãodificuldadedeacompanharosexemplosmesmo
quenuncatenhamtrabalhadocomRails,bemcomoosiniciantesqueestão
acostumadosapenascomoambientedoRails.
Osexemplosdecódigopodemserencontradosem https://github.com/
maurogeorge/rspecbf-exemplos.
Todoocódigoéescritoemportuguês,devidoaofatodeolivroserem
português.Noentanto,recomendoquesevocênãoescreveoseucódigoem
inglêsprocurefazê-lonopróximoprojeto,afinalosprojetosopensourcepos-
suemseucódigoedocumentaçãoescritosoriginalmenteeminglês.Alémdo
mais,ébemprovávelquevocêvenhaatrabalharcomalguémdeoutropaíse
queestapessoatenhaumagrandechancedenãofalaronossoportuguês.
viii

## Página 11

CasadoCódigo Sumário
Sumário
1 ObomevelhoRSpec 1
1.1 Bah,masporquetestar? . . . . . . . . . . . . . . . . . . . . . 1
1.2 Meuprimeiroteste,agoracomRSpec . . . . . . . . . . . . . . 5
1.3 OtaldoRSpec . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
1.4 Asintaxedeexpectativa . . . . . . . . . . . . . . . . . . . . . . 6
1.5 Descrevendobemoseuteste . . . . . . . . . . . . . . . . . . . 10
1.6 Nãotesteapenaso happy path . . . . . . . . . . . . . . . . . . 11
1.7 Definindoosujeito . . . . . . . . . . . . . . . . . . . . . . . . 12
1.8 Nodiaadianãoseesque çade... . . . . . . . . . . . . . . . . 15
1.9 Conclusão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
2 Testesqueacessamrede...WTF!?! 19
2.1 Introdução . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
2.2 ConsumindoumaAPI . . . . . . . . . . . . . . . . . . . . . . 20
2.3 WebMockaoresgate . . . . . . . . . . . . . . . . . . . . . . . . 24
2.4 UtilizandoocURL . . . . . . . . . . . . . . . . . . . . . . . . . 26
2.5 Maseuqueroautomatizarisso... . . . . . . . . . . . . . . . . . 28
2.6 VCR???Éovideocassetedequemeupaifala? . . . . . . . . . 29
2.7 UtilizandooVCR . . . . . . . . . . . . . . . . . . . . . . . . . 29
2.8 DadossensíveisnoVCR . . . . . . . . . . . . . . . . . . . . . 35
2.9 URIsnãodeterminísticas . . . . . . . . . . . . . . . . . . . . . 38
2.10 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
ix

## Página 12

Sumário CasadoCódigo
3 Fixturessãotãochatas!Conhe çaafactory_girl 45
3.1 Introdução . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
3.2 Instalação . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
3.3 Criandonossaprimeirafactory . . . . . . . . . . . . . . . . . 47
3.4 Utilizandoafactory . . . . . . . . . . . . . . . . . . . . . . . . 47
3.5 Factoriesnostestes . . . . . . . . . . . . . . . . . . . . . . . . 48
3.6 SendoDRY . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
3.7 Atributosdinâmicosnasfactories . . . . . . . . . . . . . . . . 55
3.8 Associações. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
3.9 Bah,massófuncionacomActiveRecord? . . . . . . . . . . . 65
3.10 Conhecendoasestratégias . . . . . . . . . . . . . . . . . . . . 67
3.11 Equandoasfactoriesnãosãomaisválidas? . . . . . . . . . . 70
3.12 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72
4 Precisamosir...devoltaparaofuturo 73
4.1 Introdução . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
4.2 Congelandootempocomtimecop . . . . . . . . . . . . . . . 75
4.3 Removendorepetição . . . . . . . . . . . . . . . . . . . . . . . 78
4.4 Rails4.1eoActiveSupport::Testing::TimeHelpers . . . . . . . 81
4.5 Conclusão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
5 Seráquetesteitudo? 83
5.1 Introdução . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
5.2 Ofalso100% . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
5.3 Meuobjetivoéter100%decoberturadetestes? . . . . . . . . 89
5.4 Masevocêsenhorautor,quantofazdecoberturadetestes? . 91
5.5 Conclusão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92
6 Copiarecolarnãoéumaop ção! 95
6.1 Introdução . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
6.2 Osharedexample . . . . . . . . . . . . . . . . . . . . . . . . . 96
6.3 CriandoumMatcher . . . . . . . . . . . . . . . . . . . . . . . 99
6.4 Oshoulda-matchers . . . . . . . . . . . . . . . . . . . . . . . . 103
6.5 Matchersdeterceiros . . . . . . . . . . . . . . . . . . . . . . . 108
6.6 Conclusão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
x

## Página 13

CasadoCódigo Sumário
7 Otaldosmocksestubs 111
7.1 Conhecendoostub . . . . . . . . . . . . . . . . . . . . . . . . 111
7.2 Osdublês . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
7.3 Expectativasemmensagens . . . . . . . . . . . . . . . . . . . 119
7.4 Matchersdeargumentos . . . . . . . . . . . . . . . . . . . . . 124
7.5 Umpoucomaissobrestubs,dublêsemessageexpectations . 126
7.6 Mockarounãomockar? . . . . . . . . . . . . . . . . . . . . . 129
7.7 Conclusão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129
8 Nãodebugamoscomputs,certo? 131
8.1 Porummelhorconsole . . . . . . . . . . . . . . . . . . . . . . 132
8.2 ConhecendooPry . . . . . . . . . . . . . . . . . . . . . . . . . 133
8.3 Conclusão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138
9 Conclusão 139
Bibliografia 141
xi

## Página 15

Capítulo1
ObomevelhoRSpec
1.1 Bah, mas por que testar?
Sevocêaindanãosabequaisasvantagensdetertestesautomatizadosnoseu
sistema,vamosaumahistorinha.
MauroeRodrigotrabalhamemumprojetoquepossuiumcadastrode
produtoqueéfeitoemtrêspassos. Hoje,ocadastrodeprodutofunciona
muitobem,noentantoéprecisoadicionarumnovopassoentreosegundo
eoterceiro.MauroeRodrigocome çamacriarestenovopasso,masopro-
cessoébastanterepetitivoepassivoaerro,dadoquedepoisqueousuário
atingeumpassonãopodevoltar.Sendoassim,acadalinhaalteradaeacada
tentativadeimplementaralgo,elesdevempassarportodooprocessopara
sódepoisconseguirtestar. Alémdofeedbacklento,acadavezquealteram
umpassorecebemumerroinesperadonateladevidoàfaltadeparâmetrode
ummétodoouumobjetoquenãofoiinstanciadoegera NoMethodError:

## Página 16

1.1. Bah,masporquetestar? CasadoCódigo
undefined method 'metodo'for nil:NilClassparatodoolado.
Senossosheróiscontinuaremassim,nãoobterãosucessonestajornada.
Éumahistóriabemcomumdeumtimedepessoasquenãoutilizatestesuni-
tários.Vamosvercomoestestestespodemnosajudar:
•Feedbackconstante:acadavezquerodamosnossostestes,sabemos
seumafuncionalidadeestáfuncionandoounãoemsegundos.
•Fácilmanutenção:casoalgoestejaerrado,otestequebrará,sendoas-
simodesenvolvedortemtotalconfian çadealteraralgo.
•Reduzbugs: comotestamoscadaumdosnossosmétodosunitaria-
mente,temoscasosdepontasgarantindoquecadaumadaspartesdo
softwaresecomportecomodevido.
•Melhordesign:assimcomotemosconfian çadeadicionarcoisanova,
tambémtemostotalconfiançaderefatoraroquejáfoifeito.
•Documentação:cadatesteéumaespecificaç ãodecomoummétodo
ouumapartedosistemafunciona,ficandodisponíveleatualizadopara
todosdotime.
•Divertido:alémdetodasasvantagens,escrevertestesésemprediver-
tido.
AcomunidadeRubyémuitofocadaemtestes,projetosopensourcecomo
o rails, devise, cancanetc.,quepossuemseustestesautomatizados.Na
realidadeaexce çãosãoprojetosquenãopossuemtestes.
Então,semdesculpas:vamosescrevernossoprimeiroteste.
Meuprimeiroteste
ORubyjápossuinasuabibliotecapadrãoseuframeworkdetestescha-
madode Test::Unit,noentanto,apartirdoRuby2.1.0érecomendadoo
usodoMiniTestparaquandoestamoscriandoumprojetonovo.OMinitest
tambémjáfazpartedabibliotecapadrãodoRuby.
Emaplicaçõesrailstemosdefinidoo ActiveSupport::TestCase,
queéaclassedetestesquedevemosherdarparadefinirmosnossostestes.
2

## Página 17

CasadoCódigo Capítulo1. ObomevelhoRSpec
O ActiveSupport::TestCase herda de
MiniTest::Unit::TestCase, sendo assim, quando estamos tes-
tando uma app rails sem definir qual o nosso framework de testes, por
padrãoestamosutilizandooMinitest.Emversõesmaisantigaserausadoo
Test::Unit.
Chegaparanósaseguintemissão:Vamoscriarumappquesimulauma
batalhaentrepokémons. Noentanto,primeirotemosquepreenchernossa
basededadoscomospokémons.Paraissocriamosonossomodel Pokemon.
Vamosescreverumtesteparaomodel Pokemonquepossuiummé-
todo #nome_completo. Elesimplesmenteretornaovalordo nomeedo
id_nacionalquecadapokémonpossuidefinido,masprimeirovamosao
teste.
Iniciamos nosso teste primeiro criando um arquivo em
test/models/pokemon_test.rb, no qual incluímos o arquivo
test_helper.rb. Em seguida, criamos uma classe com o nome
do nosso model acrescido deTest, o PokemonTest que herda de
ActiveSupport::TestCase.Comomínimodefinido,vamosagoracriar
otesteparaonossométodo.Paraisso,definimosummétodocomoprefixo
testqueindicaaominitestqueaqueleéumteste. Nométodoprefixado
por test criamos uma instância de pokémon e utilizamos do método
assert_equal para realizarmos o teste. Como primeiro parâmetro,
passamosovalorqueesperamoscomoretornoenosegundo,ométodoque
estamostestando.
require ’test_helper’
class PokemonTest < ActiveSupport::TestCase
def test_exibe_o_nome_e_o_id_nacional
pokemon = Pokemon.new(nome: ’Charizard’, id_nacional: 6)
assert_equal ’Charizard - 6’, pokemon.nome_completo
end
end
Definido o nosso teste, vamos executá-lo com $ rake test
test/models/pokemon_test.rb. Como ainda não implementa-
3

## Página 18

1.1. Bah,masporquetestar? CasadoCódigo
mosestemétodo,nossotesteiráfalhar. Vamosagoraimplementá-lopara
fazeronossotestepassar.
Paraissocriamosométodo Pokemon#nome_completoeinterpolamos
osvalores nomee id_nacional.
class Pokemon < ActiveRecord::Base
def nome_completo
"#{nome} - #{ id_nacional}"
end
end
Aoexecutarmosotestenovamente,elepassa.Opróximopassoseriare-
fatorarmosonossométodo,mascomoelefazpoucacoisa,nãotemosoque
refatorar.EsteéochamadoTDD(Desenvolvimentoguiadoatestes),quecon-
sisteemseguirmosospassosdeprimeiroescreveroteste,depoisescrevero
mínimodecódigoparaotestepassare,porúltimo,refatorarmos.
Orailsdefineométodo test,quenospermitepassarmosumastring
eumblocoe,automaticamente,égeradoométodocomoprefixo testcomo
fizemosanteriormente. Paraalteramosonossotesteanteriorparautilizar
ométodo test,removemosadefiniçãodemétodo,utilizamoso teste
passamosaeleumastringemvezdeumnomeseparadopor_(underline)e
umblococomonossoteste.
test ’exibe o nome e o id nacional’ do
pokemon = Pokemon.new(nome: ’Charizard’, id_nacional: 6)
assert_equal ’Charizard - 6’, pokemon.nome_completo
end
Émelhorutilizarométodo testpoiselenosgeramaislegibilidade.
Legal!MasporqueoRSpec?
DevidoaofatodeoRSpecincentivartestesmaislegíveisporcontade
suasintaxe.NacomunidadeRubytemososquepreferemtestarutilizandoo
Minitest/ Test::Unit[1]eosquepreferemoRSpec[7].Independentedo
frameworkqueescolher,omaisimportanteéqueestamostestando.Vamos
emfrenteeveremoscomopodemosfazeromesmotesteutilizandooRSpec.
4

## Página 19

CasadoCódigo Capítulo1. ObomevelhoRSpec
1.2 Meu primeiro teste, agora com RSpec
Instalando
AdicionamosaonossoGemfile.
group :development, :test do
gem ’rspec-rails’
end
Emseguida,rodamos $ bundle install. Éimportantequeagem
estejanosgrupos developmente test.
Finalizadoobundle,rodamos $ rails generate rspec:install
paragerarodiretório spec/egerarosarquivosdeconfiguraçãodoRSpec.
Oteste
Vamos escrever o mesmo teste que fizemos para o
Pokemon#nome_completo, no entanto, agora utilizando o RSpec.
Criamosonossoarquivodetesteem spec/models/pokemon_spec.rb,
noqualincluímoso spec_helper.rb. Iniciamosdizendoqualaclasse
queestamostestando,passandoparaométodo describeanossaclasse
Pokemon,alémdeumbloco,queéondedefiniremostodososnossostestes.
Definimosonossoprimeirotesteutilizandoométodo it,querecebeuma
stringcomonomedonossotesteeumbloco,queéondeeleérealizado.
Parafazermosaasser çãodonossoteste,utilizamosométodo shouldqueo
RSpeccriaemnossoobjetos,eemseguidapassamosparao matcher eq,que
definequenossaasser çãodeveserigualaovalorpassadoao eq.
it ’exibe o nome e o id nacional’ do
pokemon = Pokemon.new(nome: ’Charizard’, id_nacional: 6)
pokemon.nome_completo.should eq(’Charizard - 6’ )
end
Atéomomento,elenãodiferemuitodoMinitest,aindamaisseutilizar-
mosométodo testqueorailsnosfornece.Masnãosepreocupe:veremos
aindanestecapítuloalgumasdicasdecomomelhoraralegibilidadedenossos
testesutilizandotodoopoderdoRSpec.
5

## Página 20

1.3. OtaldoRSpec CasadoCódigo
1.3 O tal doRSpec
Comoprimeiroreleaseem18demaiode2007,oRSpectembastantehistó-
riaediversoscolaboradores.Quaseatingindoasuaversão3.0estável,muita
coisaaconteceucomomudan çadesintaxeeosurgimentodeumpadrãode
boaspráticascriadopelacomunidade.Sendoassim,muitosexemplosdecó-
digosempostsmaisantigospodemestarusandoasintaxeantiga,alémdenão
seguirasboaspráticas.Vamosdarumaolhadanessaspráticasparaassimuti-
lizarmossempreomelhorqueoRSpectemanosoferecer.
1.4 A sintaxe de expectativ a
Pormuitotempo,oRSpecutilizoudoquechamamosdesintaxe should,
comoacabamosdever.
it ’exibe o nome e o id nacional’ do
pokemon = Pokemon.new(nome: ’Charizard’, id_nacional: 6)
pokemon.nome_completo.should eq(’Charizard - 6’)
end
ApartirdoRSpec2.11foiincluídaasintaxe expect. Parautilizá-la,sim-
plesmentepassamosonossoobjetoparaométodo expecte,emseguida,
utilizamosométodo to.Vamosalteraronossotesteparausá-la.
it ’exibe o nome e o id nacional’ do
pokemon = Pokemon.new(nome: ’Charizard’, id_nacional: 6)
expect(pokemon.nome_completo).to eq(’Charizard - 6’)
end
Émaisverbosoqueaclássicasintaxe should,quetentavaserbempró-
ximaaumafraseeminglês.
Umdosprincipaismotivosdestamudan çadesintaxefoidevidoàsuaim-
plementaçãoqueutilizava monkey patchno Kernel.Sesuaclasseherdade
outraquenãoincluiomódulo Kernel,como BasicObject,vocêreceberá
umerro NoMethodErrorseestiverutilizandoasintaxe should.
6

## Página 21

CasadoCódigo Capítulo1. ObomevelhoRSpec
MonkeyPatch
NoRuby,asclassessãoabertas,oquenapráticaquerdizerquepo-
demosmudarocomportamentodeumaclasseaqualquermomentodu-
ranteaexecuçãodoprograma. Podemosalterar,adicionareremover
métodos.Vamosaumexemplo.
NoRubynãotemosummétodoquesimplesmentesomatodosos
valoresdoarrayeretornauminteiro. Podemosfazerissoutilizandoo
inject,entãovamoscriaronossométodo Array#somaquesomato-
dososvaloresdeumarray.
Paraissosimplesmentedefinimosummétodonanossaclasse Array
eneleutilizamoso injectparafazerasoma.
class Array
def soma
self.inject(0, :+)
end
end
Agoraquedefinimosométodo,podemosutilizá-locomofazemos
comqualquermétododoarraydiretamente.
[].soma
[1, 2, 3].soma
Noprimeiro,teremosoretorno0enosegundo,6comooesperado.
Avantagemdousodomonkeypatchéquepodemoscriarnovosmé-
todosparaoutrasclassesdenossosistemaàsquaisnãotemosacesso,
comonocasoaspadrõesdoRubyouinternasdegems.Inclusiveorails
temoActiveSupportquedefinediversasextensõesparaclassesruby,por
exemplo,ométodo #sumégeradopeloActiveSupportaoarray.
Fiqueatentoparanãoquerersaircriandométodosparaasclasses
ruby,poisvocêpodeestarsobrescrevendoummétodoqueexiste,ou
aindaumquejáfoicriadoviamonkeypatchporumagemcomooActive
Support.Utilizesabiamenteomonkeypatch.
7

## Página 22

1.4. Asintaxedeexpectativa CasadoCódigo
Ocenáriosópioraquandoestamosutilizando delegate,queincluial-
gunsdosmétodosdo Kernel.Sendoassim,seo rspec-expectations
forcarregadoantesdo delegate,tudoiráfuncionarcorretamente,masse
o delegateforcarregadoprimeiro,receberemosoerro.
Paraasintaxede shouldfuncionar,elateriaqueserdefinidoemtodos
osobjetosdosistema,masoRSpecnãopossuitodososobjetosdosistemae
tambémnãoconseguegarantirqueissoocorrerásempre.
Sevocê,assimcomoeu,nuncarecebeunenhumerrodevidoaisso,sorte
nossa! Estanovasintaxenosajudaacontinuarassim,comoRSpecfuncio-
nandosemgerarproblemasenquantoescrevemosnossostestes.
Vocêdeveselembrardo expect,queaceitavaapenasumblococomo
parâmetro,comoocasoaseguir.
it ’cria um novo pokemon’ do
expect do
criador_pokemon.criar
end.to change{ Pokemon.count }.by(1)
end
Comanovasintaxe,o expectfoiunificado.Utilizamo-lopassandoape-
nasumparâmetrooupassandoumbloco,comonoexemploanterior.
Apegadinhadosujeitoimplícito
Quandoestamosutilizandomatchersdeumalinha,podeficarmeiover-
bosoousodasintaxede expect,poisteremosquepassaro subjectparao
expectobrigatoriamentedaseguintemaneira:
it { expect(subject).to be_a(ActiveRecord::Base) }
Comopodever,nãoficoumuitolegal,poisumadasvantagensdoteste
deumalinhaépodermosusardiretamenteomatchersemprecisardefinir
osujeito. Éaíquevemapegadinha: mesmoquandoestamosutilizandoa
sintaxede expect,oRSpecnosdeixautilizaro should.
it { should be_a(ActiveRecord::Base) }
8

## Página 23

CasadoCódigo Capítulo1. ObomevelhoRSpec
Sendoassim,quandotemososujeitoimplícitopodemoscontinuaruti-
lizandoo should. Issoocorrepoiso should,quandousadonosujeito
implícito,nãodependedo monkey patchno Kernel.
ApartirdoRSpec3,alémdo shouldpodemosutilizarumanovasintaxe,
o is_expected.to.
it { is_expected.to be_a(ActiveRecord::Base) }
O is_expected.to possui a sua contraparte, o
is_expected.to_not. Dessa forma, em projetos novos utilizando o
RSpec3prefiraousodo is_expected.to.
Voucome çarumprojetonovo:qualsintaxeusar?
Iniciaremosumprojetoagora. UtilizaremosoRSpecmaisrecente,2.xx
(assumindoqueaindanãotenhamosoRSpec3estável).Definimoscomtodo
otimequeiremosusaranovasintaxe,parasersuaveanossatransiç ãopara
oRSpec3.
Noentanto,come çamosaperceberdiversos shouldduranteocódigo,
afinalotimeaindaestáacostumadoautilizá-loeacabaeventualmenteesque-
cendodeusaro expect. Assimnossostestesficamsempadrãonenhum,
unscomumasintaxeoutroscomoutra.
Para resolver o problema, podemos dizer para o RSpec que quere-
mos utilizar apenas a nova sintaxe. Para isso, adicionamos ao nosso
spec_helper.rbaconfiguração expect_withedefinimosapenasasin-
taxe expect,passandooseguintebloco:
RSpec.configure do |config|
# ...
config.expect_with :rspec do |c|
c.syntax = :expect
end
end
Destemodo,quandovocêmesmooualguémdotimetentarutilizara
sintaxedo should,receberáum NoMethodErrordadoqueoRSpecnão
faráomonkey patchparaadicionaro should.Assim,todootimeutilizará
apenasanovasintaxe.
9

## Página 24

1.5. Descrevendobemoseuteste CasadoCódigo
1.5 Descrevendo bem o seu teste
Devemossempreserclarosnonossoteste,deixandoexplícitooqueestamos
testando.Sendoassim,mensagensdetestessoltasesemcontextonãosãouma
boaprática.Vamosvoltaraotestedométodo Pokemon#nome_completo.
it ’exibe o nome e o id nacional’ do
pokemon = Pokemon.new(nome: ’Charizard’, id_nacional: 6)
expect(pokemon.nome_completo).to eq(’Charizard - 6’)
end
Nossotestepassa.Noentanto,imagineumarquivocomdezenasdetestes
evocêquersaberondeestáotestedo nome_completo.Ficacomplicadode
achar,dadoquenãohánenhumareferênciaaistononomedoteste. Pode-
mosmelhoraranossaleituradefinindoonomedométodo,comumbloco
describe.
describe ’#nome_completo’ do
it ’exibe o nome e o id nacional’ do
pokemon = Pokemon.new(nome: ’Charizard’, id_nacional: 6)
expect(pokemon.nome_completo).to eq(’Charizard - 6’)
end
end
Observequechamamosonossodescribede #nome_completo.Utiliza-
mosatralha(#)paranosreferenciarmosamétodosdeinstânciaeutilizamos
oponto(.) paranosreferenciarmosamétodosdeclasse,assimcomodiza
convençãodadocumentaçãodoRuby.Dessamaneira,ficamuitomaisfácil
deseentenderoqueestáacontecendoemcadaumdostestes.
Debônus,aoutilizarmosoformatodedocumentaç ãodoRSpec,temos
umasaídabemlegaledescritiva.
Pokemon
#nome_completo
exibe o nome e o id nacional
Parautilizarmosoformatodedocumentação,simplesmentepassamoso
parâmetro --format ddaseguintemaneiraaoRSpec: rspec --format
d.
10

## Página 25

CasadoCódigo Capítulo1. ObomevelhoRSpec
1.6 Não teste apenas o happy path
Nonossoexemploanterior,testamosapenaso happy path,ocaminhomais
comumdetodos.Assumimosquetodosospokémonsterãodefinidoso nome
eo id_nacional,masequandoumpokémonnãopossuirestesvalores?
Devemostestarestescasostambém.
Paraisso,criamosumnovopokémonsemdefinirnenhumdosvalorese
esperamosqueométodonosretorne nil.
describe ’#nome_completo’ do
it ’exibe o nome e o id nacional’ do
pokemon = Pokemon.new(nome: ’Charizard’, id_nacional: 6)
pokemon_2 = Pokemon.new
expect(pokemon.nome_completo).to eq(’Charizard - 6’)
expect(pokemon_2.nome_completo).to be_nil
end
end
Parafazermosonossotestepassar,simplesmenteverificamosantesseo
pokémonpossuitaisvalores.
def nome_completo
"#{nome} - #{ id_nacional}" if nome && id_nacional
end
Observe,noentanto,queestamosfazendo2asser çõesdentrodomesmo
teste,temos2 expectnomesmo it.Éumaboapráticadefinirmosapenas
umaasserçãoporteste.Parafazermosisso,alteramosonossotesteem2:um
quetestaopokémonquepossuitodososvaloreseoutroquetestaopokémon
quenãopossuitaisvalores.
describe ’#nome_completo’ do
it ’exibe o nome e o id nacional quando possui os valores’ do
pokemon = Pokemon.new(nome: ’Charizard’, id_nacional: 6)
expect(pokemon.nome_completo).to eq(’Charizard - 6’)
end
it ’é nil quando não possui o nome e o id nacional’ do
pokemon = Pokemon.new
11

## Página 26

1.7. Definindoosujeito CasadoCódigo
expect(pokemon.nome_completo).to be_nil
end
end
Contextosparaamelhordescri ção
Nonossotestede Pokemon#nome_completo,vemossurgiraneces-
sidadedousodecontexto. Observequeapósoquerealmenteéesperado
seguimoscomapalavra“quando”.Umbommododesaberseprecisamosde
umcontextoéquandovemostestesquepossuem“se”(seousuárioestálo-
gado),“com”(comumusuárioválido)e“quando”.Poiscadaumdestestem
asuacontraparte,como,nonossoexemplo,oquepossuiosvaloreseoque
nãopossuiosvalores.
Simplesmenterefatoramosmovendoapartedocontextoparaumbloco
contextmantendoonossotestedaseguintemaneira:
describe ’#nome_completo’ do
context ’quando possui nome e o id nacional’ do
it ’exibe o nome e o id nacional’ do
# ...
end
end
context ’quando não possui o nome e o id nacional’ do
it ’é nil’ do
# ...
end
end
end
Assimficaclaroparatodosdotimequeométodo #nome_completose
comportadiferentebaseadonoqueédefinidonomodel Pokemon.
1.7 Definindo o sujeito
Noexemploanterior,estamoscriandooobjetoasertestadodentrodopró-
prioteste,noentantoécomumoscontextosteremdiversostestes.Podemos
12

## Página 27

CasadoCódigo Capítulo1. ObomevelhoRSpec
resolverissocomumavariáveldeinstânciacomonossoobjetoasertestado,
simplesmentecriando @pokemondentrodeumbloco before.
context ’quando possui nome e o id nacional’ do
before do
@pokemon = Pokemon.new(nome: ’Charizard’, id_nacional: 6)
end
it ’exibe o nome e o id nacional’ do
expect(@pokemon.nome_completo).to eq(’Charizard - 6’)
end
end
SevocêutilizaoRSpecháalgumtempojádeveterfeitoalgoassim,outer
vistoestepadrão.Noentanto,podemosfazermelhorutilizandoo let.
Removemosobloco beforeeutilizamosumbloco let,passandoo
nomedoobjetoquequeremoscomoumsímbolo nonossocaso pokemon.
context ’quando possui nome e o id nacional’ do
let(:pokemon) do
Pokemon.new(nome: ’Charizard’, id_nacional: 6)
end
it ’exibe o nome e o id nacional’ do
expect(pokemon.nome_completo).to eq(’Charizard - 6’)
end
end
Observequeagoratemosdisponívelométodo pokemon,quefoicriado
pelo let,enãomaisavariáveldeinstância @pokemon.
Alémdisso,estamosutilizandoa DSLdoRSpecparaoqueelafoicriada.
Temosavantagemdo letser lazy loaded,ouseja,eleécriadonaprimeira
vezqueéchamadoecacheadoatéofinaldotestequeestásendorodado.
Seelenãoforusadoporalgumteste,elenemécriado,diferentedequando
utilizamoso before.
Emcasosemqueprecisamosgarantirqueoobjetosejacriadoantesdo
nossoteste,utilizamoso let!,quefuncionacomoo let,comadiferen ça
dequeeleécriadoantesdoteste,enãoquandoéchamadocomoo let.
13

## Página 28

1.7. Definindoosujeito CasadoCódigo
Issonãoquerdizerqueo beforenãotenhaseuuso. Utilize-opara
quandoprecisarcriarocenáriodoseuteste,masnãoprecisardainstância
denenhumdosobjetosgerados.Como,porexemplo,criar11pokémonspara
testarumapaginação podemoscriartodoselesdentrodeumbloco before
etestarapenasaquantidadedospokémonsretornados.
Otaldosubject
Nousodopadrãodobloco before,umaoutrapráticaquesurgiufoio
usodo @itparadefiniroobjetoasertestado.
context ’quando possui nome e o id nacional’ do
before do
@it = Pokemon.new(nome: ’Charizard’, id_nacional: 6)
end
it ’exibe o nome e o id nacional’ do
expect(@it.nome_completo).to eq(’Charizard - 6’ )
end
end
Afinal,obloco before,alémdedefiniroobjetoasertestado,podeestar
gerandotambémoutrosobjetosparamontarocenáriodoteste. Podemos
alteraronossoexemploparautilizaro subject,simplesmentetrocandoo
nosso letpor subjectereferenciando-nosa subjectduranteonosso
teste.
context ’quando possui nome e o id nacional’ do
subject do
Pokemon.new(nome: ’Charizard’, id_nacional: 6)
end
it ’exibe o nome e o id nacional’ do
expect(subject.nome_completo).to eq(’Charizard - 6’)
end
end
Assimcomoo let,o subjecttambémélazy loaded. Vocêpodees-
tarseperguntandoqualavantagemdeseusaro subjectemvezdo let.
14

## Página 29

CasadoCódigo Capítulo1. ObomevelhoRSpec
UmadasgrandesvirtudesdoRSpecéalegibilidade.Imaginequetenhamos
mais2 letscompondoonossocenário.Àprimeiravista,nãosabemosde
antemãoqualobjetoestásendotestado,temosqueolharnoteste.Utilizando
o subjectsabemosqueaqueleéosujeitodonossoteste.
Seaindapreferirmosutilizaro pokemondiretamente,podemospassar
umparâmetroparao subjectdefinindoonomedosubjectdaseguinte
maneira:
context ’quando possui nome e o id nacional’ do
subject(:pokemon) do
Pokemon.new(nome: ’Charizard’, id_nacional: 6)
end
it ’exibe o nome e o id nacional’ do
expect(pokemon.nome_completo).to eq(’Charizard - 6’)
end
end
Avantagemnestecasoéque,nomeiodediversos let,sabemosexata-
mentequalonossosujeito.
Comotudoemprogramação,nãohárespostacorretaouapenasumca-
minhoaseseguir.HáumaparceladacomunidadeRubyqueapoiaousoda
DSL[6]eoutraqueprefereousodemétodosRuby[2].Utilizecadaumadas
abordagenseescolhaqualseguir,baseadonocontextodoseuprojeto.Afinal,
seoprojetojáexisteeestamosseguindocomumpadrão,émelhormantê-lo
doqueinserirumaabordagemdiferente.Utilizenovosprojetosparaexperi-
mentaropadrãodiferentedoqueohabitual,esenãogostar.simplesmente
mude.
1.8 No dia a dia não se esqueça de ...
utilizarsempreosmatchers
Observeque,nonossoexemploparatestarseonomecompletodopokémon
era nil,utilizamosomatcher be_nil.
15

## Página 30

1.8. Nodiaadianãoseesque çade... CasadoCódigo
it ’é nil’ do
expect(subject.nome_completo).to be_nil
end
Poderíamosterutilizadoomatcher eqpassandoovalor nildaseguinte
maneira:
it ’é nil’ do
expect(subject.nome_completo).to eq(nil)
end
Noentanto,éumaboapráticasempreutilizarmosos matchersqueoRS-
pecnosofereceporquestõesdelegibilidade.
Valelembrarqueaoutilizarmosasintaxe expectnãopodemosutilizaro
==,dadoqueestasintaxenãoaceitaosoperadoresdiretamente.Resolvemos
issosimplesmentecomomatcher eq,quepossuiomesmocomportamento.
Sendoassim, semprequepossívelutilizeosmatchersdoRSpec. Po-
demos ter uma lista dos matchers em:https://www.relishapp.com/rspec/
rspec-expectations/docs/built-in-matchers.
nãouseo should
Umapráticaqueeracomumdacomunidadeeraadetodosostestesini-
ciaremcom should(“deveria”eminglês).
it ’should have the name and the national_id’ do
expect(pokemon.full_name).to eq(’Charizard - 6’)
end
Nonossoteste,temosemsuadescriç ãoalgocomo“deveteronameeo
national_id”.Omelhormododedefinirmosistoéutilizandoaterceirapessoa
dopresente,alterandode shouldpara does,daseguintemaneira:
it ’does have the name and the national_id’ do
expect(pokemon.full_name).to eq(’Charizard - 6’)
end
Seestácome çandoumnovoprojeto, maspercebequevocêeotime
aindaestãocolocandoo should,mesmoqueinconscientemente,utilizeagem
16

## Página 31

CasadoCódigo Capítulo1. ObomevelhoRSpec
should_not(https://github.com/should-not/should_not),quefazasspecs
queiniciaremcom shouldfalharem.Seocasoéumprojetoantigo,podemos
utilizardagem should_clean(https://github.com/siyelo/should_clean),
quefazexatamenteoquefizemosnonossoexemplo.
utilizeum coding style
Definacomoseutimequal coding styleutilizar,poisassimpoderãoevitar
quecadatesteestejadefinidodeumamaneiradiferente. Utilizesempreos
mesmosespaços,mesmaquebradelinhaetc.Umasimplesconven çãodequal
codingstyleseguirajudaatodosnotime,jáqueosparticipantessesentem
sempreemcasa,enãoestranhamcomocadatestefoifeito.Comumcoding
stylebemdefinidoeasdicasquevimosnestecapítulo,ficamuitomaisfácilo
usodoRSpecparatodosdotime.
OBetterSpecs[6]nosrecomendaseguirocodingstyledefinidonasuíte
detestesdomongoid(https://github.com/mongoid/mongoid). Podemos
utilizá-looudefiniralgoapartirdele,desdequetodosdotimeconcordem
emutilizaromesmocodingstyle.
ComooRSpectambéméRuby,recomendosempreficardeolhono Ruby
Style Guide (https://github.com/bbatsov/ruby-style-guide)eno Rails Style
Guide(https://github.com/bbatsov/rails-style-guide),quepossuembastan-
tesdicaslegaisdecomodefiniroseucódigo.
Duranteolivro,seguimosocodingstyledoBetterSpecscomalgumas
pequenasalteraçõesparaseadequaraoprocessodeimpressão.
1.9 Conclusão
Adiversãoapenascome çou,Vamosrelembraroquevimosnestecomecinho
dolivro.
• Vimosasvantagensdeescrevertestesautomatizados;
• CriamosnossoprimeirotesteutilizandooMinitest;
• CriamosnossoprimeirotesteutilizandooRSpec;
• UtilizamosasintaxeexpectdoRSpec;
17

## Página 32

1.9. Conclusão CasadoCódigo
• Vimosquepodemosutilizaroshouldquandoestamoscomosujeito
implícito;
• Vimosdicasdecomoescrevermelhorosnossostestes;
• Nãotestamosapenasohappy path;
• Utilizamoslete subjectparadefinirmosocenáriodenossostestes;
• Vimosdicasparausarmosnonossodiaadia.
Continueaí,quenopróximocapítuloveremosquetestesqueacessama
redesãoumproblema. Veremoscomopodemoscontorná-losutilizandoo
WebMockeautomatizandooprocessocomousodo VCR.
18

## Página 33

Capítulo2
Testesqueacessamrede...
WTF!?!
2.1 Introdução
HojeemdiaécomumtermosqueutilizardiversasAPIs,comoTwitter,Fa-
cebooketc. Temosque,porexemplo,obtertodososamigosdeumusuário
doFacebook,maseparatestarisso?Acessararededuranteostestesnosdá
muitosproblemas:
•Testeslentos:seacadaumdostestestivermosqueacessararede,o
processoficarálento,ecomoreflexonossocomportamentoserácome-
çaranãoquererescrevertestes,paranãoaumentarotempodefunci-
onamentodasuítedetestes.

## Página 34

2.2. ConsumindoumaAPI CasadoCódigo
•Testesquebradi ços: tambémchamadosdefalsospositivos, seriam
aquelesqueemalgunsmomentospassameemoutrosnão. Afinal,
comoestamosdependentesderede,podemosficarseminternetoua
APIpodenãoresponder,assimotesteàsvezespassa,àsvezesnão.
•Nãopodertestarsemrede:quandoestamosemumvooouemlugares
afastadosdosgrandescentros,podehavermomentossemconexãoà
internet. Seriamuitobompoderrodarnossasuítedetestesmesmo
seminternet,masseestivermosacessandoredenãoconseguiremos.
Nãoqueremosnenhumdestesproblemasnanossasuíte.Vamosvercomo
podemosresolverisso.
2.2 Consumindo uma API
Temosonossomodel Pokemon,noentanto,nãoqueremosficarcriando
cadaumdospokémonsmanualmente. Parasalvarosdadossobretodosos
pokémonsiremosutilizaraAPIpúblicadosite http://pokeapi.co/.
Sabemosquecadapokémonpossuium id_nacionalemnossaAPI.
Destemodo,pelo id_nacionaldopokémonconseguimospegarsuasde-
maisinformações.Vamosimplementarissoemnossarailsapp.
OCriadorPokemon
Parainiciar,criaremosumaclassequerecebeum id_nacionalecria
umpokémonutilizandoasinformaçõesvindasdaAPI.Vamosprimeiroao
teste:
describe CriadorPokemon do
describe ’#criar’ do
let(:criador_pokemon) do
CriadorPokemon.new(6)
end
it ’cria um novo pokemon’ do
20

## Página 35

CasadoCódigo Capítulo2. Testesqueacessamrede...WTF!?!
expect do
criador_pokemon.criar
end.to change{ Pokemon.count }.by(1)
end
end
end
Começamosfazendoapenasotesteparaverificarseumpokémonfoicri-
ado.Vamosagoraaocódigoparafazê-lopassar.
class CriadorPokemon
def initialize(id_nacional)
end
def criar
Pokemon.create
end
end
Comosepodever,nãoestamosconsumindoaAPIainda,afinaltestamos
apenassecriamosumpokémoneestetestepassou. Agoravamosavan çar
maisumpoucoesalvaronomedestepokémon.Vamosaoteste.
describe ’pokemon criado’ do
before do
criador_pokemon.criar
end
subject do
Pokemon.last
end
it ’possui o nome correto’ do
expect(subject.nome).to eq(’Charizard’)
end
end
21

## Página 36

2.2. ConsumindoumaAPI CasadoCódigo
Nossotestedizqueonomedonossopokémondeveser Charizard,dado
queestamospassandoparaeleo id_nacional6.Agoravamosimplemen-
tarocódigoparageraronomedopokémon.
Vamos primeiro criar o initializer, no qual atribuímos
id_nacionala @id_nacional. Olegaléquecriamosum reader
parapodermosusarapenas id_nacionalemnossocódigo, emvezde
@id_nacionale,comodefinimosoreadercomoprivado,nãoserápossível
acessar id_nacionalpublicamente. Isso,paranós,éoideal,dadoque
oúnicoobjetivodestaclasseésalvarumpokémon. Sefôssemosexpora
interface CriadorPokemon#id_nacionalpublicamente, teríamos que
escreverumtesteparaisto.
class CriadorPokemon
def initialize(id_nacional)
@id_nacional = id_nacional
end
private
attr_reader :id_nacional
end
Vamoscriarummétodoprivado endpoint. Aúnicacoisaqueele
fazécriarumobjeto URIinterpolandooendpointdaAPIcomonosso
id_nacional.Comovamosutilizaro Net::HTTP,éumaboadefinirmos
umobjeto URIparanãoprecisarmospassarduasstringsparaométodo get.
Assimseguimosumaabordagemmaisorientadaaobjetopoistemosumob-
jetoquerepresentaumaURIenãoumastring.Edebônusganhamosdiversos
métodoscomo #hostname, #pathequalqueroutroqueo URInosofere-
cer.
def endpoint
URI("http://pokeapi.co/api/v1/pokemon/#{id_nacional}/")
end
Agorasimvamosao cria_info. Primeiro,usamoso Net::HTTP
parafazeranossarequisiç ãoGETeassimconseguimosainformaç ãodo
22

## Página 37

CasadoCódigo Capítulo2. Testesqueacessamrede...WTF!?!
nossopokémon.Emseguida,parseamosarespostadarequisiç ãoutilizando
o JSON.parseesalvamosistoem @info.
private
attr_reader :id_nacional, :info
def cria_info
resposta = Net::HTTP.get(endpoint)
@info = JSON.parse(resposta)
end
NossarespostaéumJSONcomoalgoassim:
{
"attack": 84,
"defense": 78,
"moves": [
{
"learn_type": "machine",
"name": "Dragon-tail",
"resource_uri": "/api/v1/move/525/"
},
],
"name": "Charizard",
"national_id": 6,
}
Removidiversasinformações,poisistoéosuficienteparaonossopro-
pósito.Casoqueiravisualizartodasasinformações,bastaacessaroendpoint
http://pokeapi.co/api/v1/pokemon/6/.
Criamos o métodonome, que nada mais é do que um reader do
info['name'].
def nome
info[’name’]
end
Alteramosnossoinitializerparacriarainformaç ãodopokémon.
23

## Página 38

2.3. WebMockaoresgate CasadoCódigo
def initialize(id_nacional)
@id_nacional = id_nacional
cria_info
end
Finalizamosalterandoocreateparasalvaropokémoncomonamecor-
reto.
def criar
Pokemon.create(nome: nome)
end
Nossostestesagoraestãoverde,todosostestespassam,noentantoesta-
mosenfrentandotodososproblemasmencionadosnocome çodocapítulo.
2.3 WebMock ao resgate
O WebMockéumabibliotecaquenospermitefazerstubeasser çõesdere-
quisiçõesHTTP,exatamenteoqueprecisamospararesolveronossoatual
problema.
Instalação
Simplesmenteadicionamosaonosso Gemfileaseguintelinhaeroda-
mos bundle.
gem ’webmock’
Emseguida,adicionamosao spec_helper.rbalinha.
require ’webmock/rspec’
Forjandoumarequisi çãoHTTP
Antesdecontinuarmos,vamosrodarosnossostestes.WTF?!Masagora
elesquebram,deixandoaseguintemensagem:
WebMock::NetConnectNotAllowedError:
Real HTTP connections are disabled.
Unregistered request:
...
24

## Página 39

CasadoCódigo Capítulo2. Testesqueacessamrede...WTF!?!
EsteéoWebMocknosavisandoqueestamostentandofazerumarequisi-
çãoHTTPenocorpodamensagemdoerroeleaindanosensinaacorrigi-lo
utilizandoométodo stub_request.
UmadasfuncionalidadesdoWebMockégarantirquenenhumarequi-
siçãoHTTPsejafeitaemnossostestes,ouseja,elenosalertasobreaqueles
problemasquevimosnocome çoenosdáumadicadecomoresolvê-losuti-
lizandooWebMock.
Nonossocaso,nãoéimportantequaisosparâmetrosqueestamospas-
sandonoheader,dadoqueaAPInãoseimportacomisso.Oquequeremos
forjaréapenasoretornodaAPI.VamosseguiradicadoWebMockeutilizaro
stub_request.Antesdosnossostestesdecreate,adicionamosachamada
ao stub_request.
describe ’#criar’ do
before do
stub_request(:get, ’http://pokeapi.co/api/v1/pokemon/6/’)
.to_return(status: 200, body: ’’, headers: {})
end
# ...
end
Agoraestamosforjandoaresposta. Todarequisiç ão GETfeitaàURL
http://pokeapi.co/api/v1/pokemon/6/teráomesmovalorretornado.Vamos
rodarotesteeverseestáverde. Aindaestamoscomerros,masdestavez
temososeguinte:
TypeError:
no implicit conversion of nil into String
Muitobom,agoraoerroénonossocódigoenãodevidoaoacessoà
rede. Verificando,conseguimosdescobrirqueesseerroocorrenométodo
cria_infoexatamenteem JSON.parse(resposta),poisnesteponto
forjamosarequisição,ousejaovalordaresposta. Mascomodefinimoso
bodycomovazio,o JSON.parsenãoconseguefazeroparsede nilere-
torna TypeError.
25

## Página 40

2.4. UtilizandoocURL CasadoCódigo
Vamosarrumaranossarespostaedarumvalorao body.Paraisso,aces-
samoshttp://pokeapi.co/api/v1/pokemon/6/,salvamosapenasoqueinteressa
paraanossaAPI,epassamosistoparaoWebMock.
describe ’#criar’ do
before do
body = ’{’ \
’ "name": "Charizard"’ \
’}’
stub_request(:get, ’http://pokeapi.co/api/v1/pokemon/6/’)
.to_return(status: 200, body: body, headers: {})
end
# ...
end
Rodamosostestes,tudoestáverdeenossostestes,passando.
Forjandolikeapro
Noexemploanterior,conseguimosforjaranossarequisiç ãoeagoranão
estamosmaisenfrentandoosproblemasdetalhadosnoiníciodase ção. No
entanto,enfrentamososseguintesproblemas:
•Processofactívelaerro: secontinuarmoscriandonossasrespostas,es-
tamossujeitosaeventualmenteescreveralgoerrado,como,porexem-
plo,definirumvalorqueseriaumastringcomointeiro.Issopodenos
levaraproblemasinesperados.
•Respostaincompleta: noexemploanterior,forjamosapenasoscam-
posqueestamosusandonomomento.Ouseja,seprecisarmosdeno-
voscampos,teremosqueacessaraAPImaisumavezmanualmente
paraobtermososdadoseadicioná-losaonossoteste.
2.4 Utilizando o cURL
OcURLéumutilitáriodelinhadecomandoparatransferênciadedadosque
entendeváriosprotocolos. Ouseja,podemosacessarumaURLviacURLe
26

## Página 41

CasadoCódigo Capítulo2. Testesqueacessamrede...WTF!?!
obtersuaresposta.Porpadrão,elejáveminstaladonoUbuntuenoMacOS
X.
Instalando o cURL noWindows
AcesseapáginadedownloaddocURLem http://curl.haxx.se/dlwiz/
1)Selecioneotipodepacote:curlexecutable
2) Selecioneosistemaoperacional:Windows/Win32ouWin64
3)Selecioneo flavour:Generic
4) Selecioneaversão:Unspecified
5)Façaodownload:simplesmenteclicandonobotãodedownload
Extraiaoarquivozipqueacaboudebaixaremova-oparao windir
(porpadrãoC:\WINDOWS).Abraopromptdecomandoeexecute
$ curl --version,vocêreceberáaversãodocURLinstalada.
PodemosutilizarocURLdaseguintemaneiranoterminal.
$ curl http://pokeapi.co/api/v1/pokemon/6/
EleexibiráobodydarespostaHTTPdiretonoseuterminal. Sevocê
manjaumpoucomaisdeLinux,sabequepodemosredirecionarooutputdo
terminalparaumarquivoutilizandoo >e,parafacilitaranossavidamais
ainda,o WebMockaceitaumarquivocomoresposta. Vamosalterarnossa
specparautilizarumarespostavindadocURL.
Primeiro, criamos um arquivo de fixture em
spec/fixtures/services/criador_pokemon/resposta.txt,
queiráarmazenaranossaresposta. Depois, salvamosnossarespostado
servidorutilizandoocURLdaseguintemaneira:
$ curl -is http://pokeapi.co/api/v1/pokemon/6/ > \
spec/fixtures/services/criador_pokemon/resposta.txt
27

## Página 42

2.5. Maseuqueroautomatizarisso... CasadoCódigo
Aopção iquepassamosparaocURLdizparaeleincluiroscabe çalhos
naresposta.Dadoqueo WebmockentendearespostadocURL,nãoteremos
queforjarocorponemoscabe çalhosdaresposta.
Jáaopção séparautilizarmosomodosilencioso,ouseja,nãorecebere-
mosooutputdiretonoterminal.
Agoraquetemosanossarespostasalva,temosquealterarnossotestepara
utilizarestearquivo.
describe ’#criar’ do
before do
caminho_arquivo =
’spec/fixtures/services/criador_pokemon/resposta.txt’
arquivo_resposta = File.new(caminho_arquivo)
stub_request(:get, ’http://pokeapi.co/api/v1/pokemon/6/’)
.to_return(arquivo_resposta)
end
# ...
end
Rodamosnossostestesecontinuatudoverde,comoesperado. Sepor
algummotivoarespostadaAPImudar,simplesmenterodamosocURLpara
atualizarmosanossaresposta.
2.5 Mas eu quero automatizar isso ...
VimosquecomoWebmockresolvemososproblemasrelacionadosaousode
redeemnossostestes. AprendemosquepodemosusarocURLparaforjar
melhornossasrequisiçõesaoutilizarmoso WebMock.
Talvezvocêtenhasesentidoinclinadoacriarumhelper,quelheajudea
automatizaresteprocessodeutilizaçãodocURLemconjuntocomoWeb-
Mock. Sesim,émelhorpararporaí,afinaljátemosoVCR,queveremos
adiante—umagemquefazousodoWebMockagilizandooprocessoda
criaçãodasfixtures,alémdeoutrascoisaslegais.
28

## Página 43

CasadoCódigo Capítulo2. Testesqueacessamrede...WTF!?!
2.6 VCR???É o videocassete de que meu pai fala?
Sevocêviveunosanos80e90comcertezaselembrarádovideocassete,o
ancestraldoDVDedoBlu-ray.Daépocaemqueaúnicacoisaquesetinha
aoalugarumfilmeeraoprópriofilme,emquesetinhaquerebobinarafitaao
entregarnalocadoraparanãopagarmulta,daépocaemqueaindaexistiam
locadoras.
OVCRqueiremosutilizaréumabibliotecarubyqueutilizabibliotecasde
stubderequisiçõesHTTP,comoWebMock,paracriarasfixtures,aquicha-
madasdecassetes.Assim,automatizamosoprocessodecriaç ãodasfixtures.
Instalação
Simplesmente,adicionamosaonosso Gemfileaseguintelinhaeroda-
mos bundle:
gem ’vcr’
Emseguida,criamosumarquivoem spec/support/vcr.rbcomo
seguinteconteúdo.
VCR.configure do |c|
c.cassette_library_dir = ’spec/fixtures/vcr_cassettes’
c.hook_into :webmock
end
Aconfiguração cassette_library_dirquefazemoséparadefinir
ondearmazenaremosnossoscassetes.Emseguida,definimoso hook_into,
quedizqualseráabibliotecadestubqueusaremos,edefinimosoWebMock.
2.7 Utilizando oVCR
RemovendooWebMock
AntesdeiniciarmosousodoVCR,devemosremoveroWebMockdenosso
teste.
Primeiro,removemosanossafixture:
29

## Página 44

2.7. UtilizandooVCR CasadoCódigo
$ rm spec/fixtures/services/criador_pokemon/resposta.txt
Eremovemosachamadado stub_requestnonossoteste:
describe CriadorPokemon do
describe ’#criar’ do
let(:criador_pokemon) do
CriadorPokemon.new(6)
end
# ...
end
end
Vamosagorarodarnossostesteseveroqueacontece.Recebemoscomo
respostaalgocomo:
Failure/Error: CriadorPokemon.new(6)
VCR::Errors::UnhandledHTTPRequestError:
==============================================================
An HTTP request has been made that VCR does not know how
to handle:
GET http://pokeapi.co/api/v1/pokemon/6/
There is currently no cassette in use. There are a few ways
you can configure VCR to handle this request:
...
Omitiorestantedotextoparafocarmosnoqueinteressaaquiparanós.
AssimcomooWebMock,elenosnotificaaotentarmosacessarredeemnos-
sosteste.
30

## Página 45

CasadoCódigo Capítulo2. Testesqueacessamrede...WTF!?!
AplicandooVCR
AgoraqueremovemosoWebMock,vamosaplicaroVCR.OVCRutiliza
deumasintaxediferentedoWebMock:eleaceitaumblococomoparâmetro
etodooacessoàredequehouverdentrodoblocoésalvoemumarquivo
defixture,tantoarequisiçãocomoaresposta. Nossotesteficadaseguinte
maneira:
describe ’#criar’ do
let(:criador_pokemon) do
CriadorPokemon.new(6)
end
it ’cria um novo pokemon’ do
expect do
VCR.use_cassette(’CriadorPokemon/criar’) do
criador_pokemon.criar
end
end.to change{ Pokemon.count }.by(1)
end
describe ’pokemon criado’ do
before do
VCR.use_cassette(’CriadorPokemon/criar’) do
criador_pokemon.criar
end
end
# ...
end
end
Utilizamosométodo VCR.use_cassetteparadefiniranossafixture
utilizandooVCR,epassamos2parâmetros:oprimeiroéonomedoarquivo
defixturesquequeremos;osegundo,umblococomaaç ãoqueacessarede
emnossoteste—nonossocaso,achamadaao criador_pokemon.criar.
OVCRsalvaasfixturesutilizandooformato YAML,salvandooarquivo
nocaminhoquedefinimosnanossaconfiguraç ãoemconjuntocomoque
31

## Página 46

2.7. UtilizandooVCR CasadoCódigo
definimosno VCR.use_cassette.
Sendo assim, após rodarmos os nossos testes, teremos um novo
arquivo criado. Este é criado apenas na primeira requisição; nas
demais já utilizamos o arquivo de fixture. O arquivo é salvo em
spec/fixtures/vcr_cassettes/CriadorPokemon/criar.yml,
comalgocomo:
---
http_interactions:
- request:
method: get
uri: http://pokeapi.co/api/v1/pokemon/6/
body:
encoding: US-ASCII
string: ’’
headers:
...
response:
status:
code: 200
message: OK
headers:
...
body:
encoding: UTF-8
...
Omitiboapartedo YAML,masotrechoapresentadoéinteressantepara
vermosqueelesalvaarequisiçãoearespostanomesmoarquivo,utilizando
oformato YAML.
Comosepodever,reduzimosbastanteonossotrabalho.Agoranãopreci-
samosmaiscriaroarquivomanualmente,jáquedelegamosistoparaoVCR,
eeleaindanosavisaquandoesquecemosdealgumtestequeporumacaso
estejaacessandorede.NestecasosimplesmenteadicionamosoVCReore-
solvemos.
32

## Página 47

CasadoCódigo Capítulo2. Testesqueacessamrede...WTF!?!
Blocks,blockseverywhere
AsintaxequeestamosutilizandoatéomomentoéapadrãodoVCR.O
problemaéqueelapodeparecerbastanteverbosaeconfusa,principalmente
quandoestáemconjuntocomosblocosdoRSpec.Comononossoexemplo:
it ’cria um novo pokemon’ do
expect do
VCR.use_cassette(’CriadorPokemon/criar’) do
criador_pokemon.criar
end
end.to change{ Pokemon.count }.by(1)
end
Acabamoscomtrêsblocosaninhados:odoteste,odomatcherdoRSpec
eodoVCR.
ConheçaometadadodoRSpec
ComooRubyéumalinguagemqueprezaporlegibilidade,podemoscon-
figuraroVCRparautilizarometadadodoRSpec.
Primeiro, alteramos o nosso config do VCR em
spec/support/vcr.rb:
VCR.configure do |c|
# ...
c.configure_rspec_metadata!
end
TambémalteramosoRSpecparatratarsímboloscomosepossuíssemo
valor true,modificandoo spec/spec_helper.rb:
RSpec.configure do |config|
# ...
config.treat_symbols_as_metadata_keys_with_true_values = true
end
Agoravamosalterarnossotesteparausaranovasintaxe.
33

## Página 48

2.7. UtilizandooVCR CasadoCódigo
describe CriadorPokemon do
describe ’#criar’, :vcr do
# ...
end
end
Removemos todos os blocos do nosso código e adici-
onamos apenas o símbolo :vcr na descrição do nosso
método create. Se não configurássemos o RSpec com o
treat_symbols_as_metadata_keys_with_true_values, tería-
mosquedefinirovalorde :vcrdaseguintemaneira: vcr: true.
Rodeostestesevejaquetudocontinuapassando.Sóqueagoracomme-
nosblocos,eumasintaxemaiselegante.
Cassetes,Casseteseverywhere
Apósrodarostestes,verificarmosquefoicriado1arquivodefixturepara
cadabloco it,cadateste.Ouseja,paracadateste,pelomenos1vezfoiaces-
sadaaredeecriadaumafixture. Oproblemaésealterarmosonossoteste,
mudandooendpointporexemplo. Teríamosquerecriartodasestasfixtu-
ressecontinuássemosseguindoestaabordagem.Dadoquesempreestamos
fazendoamesmarequisição,oidealseriadefinirmos1arquivodefixtureape-
nas,comoquandoestávamosutilizandooblocodoVCR.
Pararesolverisso,primeiroapagamostodasasfixturesnovascriadas.Em
seguida,alteramosonossoteste.
describe CriadorPokemon do
describe ’#criar’, vcr:
{ cassette_name: ’CriadorPokemon/criar’ } do
# ...
end
end
Simplesmentepassamosumparamêtro cassette_nameparaoVCR,
34

## Página 49

CasadoCódigo Capítulo2. Testesqueacessamrede...WTF!?!
demodoque,emtodosostestesdaquelebloco,eleusaráomesmocassete
queéoquequeremosnestecaso. Mashaverácasosemqueusaremosum
cassetediferenteporcontexto,porexemplo.
Nanossahipótese,apontamosparaomesmocassetequejáhavíamoscri-
ado,noentanto,senãohouvessenenhumcasseteparaarequisiç ão,eleseria
criadonoprimeirotesteeutilizadonosseguintes.
2.8 Dados sensíveis noVCR
ObserveocassetegeradopeloVCR,especificamentenapartederequisiç ão.
---
http_interactions:
- request:
method: get
uri: http://pokeapi.co/api/v1/pokemon/6/
body:
encoding: US-ASCII
string: ’’
headers:
Accept-Encoding:
- gzip;q=1.0,deflate;q=0.6,identity;q=0.3
Accept:
- ’*/*’
User-Agent:
- Ruby
Host:
- pokeapi.co
Perceba que todos os dados que passamos comouri, body e os
headerssãosalvosnestearquivo.
EnquantoestamoslidandocomprojetosprivadoseAPIspúblicas,não
precisamosnospreocuparcomovazamentodainformação,dadoqueelaestá
limitadaaumnúmerodepessoas.
Noentanto,vamosinverterasituaç ão:eseestivermostrabalhandoem
umprojetoopensourcequetenhaqueacessarumaAPIprivada?Acessara
redenãoéumaop çãoduranteostestes,mastambémnãoserialegalmanter-
mosnossascredenciaisdisponíveisparaqualquerumnogithub.
35

## Página 50

2.8. DadossensíveisnoVCR CasadoCódigo
Filtrandodadossensíveis
Vamosmudarumpoucoagoraonossocenário. DadoqueanossaAPI
anteriorépublica,vamosagorautilizarumaAPIprivada,aAPIdomoip(http:
//moip.com.br).
OmoippossuiumaAPIparaoseuchamadocheckouttransparente.
Vamosabstrairdetalhesefocarapenasnoquenosinteressa: devemosre-
alizarumPOSTparaaseguinteURI https://MOIP_TOKEN:MOIP_KEY@
desenvolvedor.moip.com.br/sandbox/ws/alpha/EnviarInstrucao/Unica.
O checkout transparente do moip
Emdiversosserviçosdeintermediadordepagamento,PagSeguroe
PayPal,porexemplo,temosumfluxomaisoumenosassim.
1) Osprodutossãoadicionadosaocarrinhonoe-commerce;
2) Aoclicarmosemcomprarsomosdirecionadosaointermediadordo
pagamento;
3) Finalizando o pagamento, retornamos ao e-commerce com uma
mensagemdesucesso.
Ocheckouttransparenteremoveosegundopasso. Nósnãosomos
direcionadosaointermediadordepagamento,todooprocessoéfeito
dentrodopróprioe-commerce.
Deste modo, utilizamos um intermediador de pagamento, mas o
usuáriofinalnãotemestapercep ção,ficandooprocessotransparente
paraele.
Percebaqueoendpointdomoipnecessitaquepassemosonossomoip
tokenenossamoipkeyemcadaumadasrequisições.Ecomovimos,oVCR
irásalvaressesdadosnafixture.
Pararesolverisso,primeirotemosquedizeraoVCRquaisdadossãocon-
sideradossensíveis.Issoéfeitocomumaconfiguraçãodaseguintemaneira:
36

## Página 51

CasadoCódigo Capítulo2. Testesqueacessamrede...WTF!?!
VCR.configure do |c|
# ...
c.filter_sensitive_data(’<MOIP_KEY>’) { ’my_key’ }
c.filter_sensitive_data(’<MOIP_TOKEN>’) { ’my_token’ }
end
Destaforma,semprequeoVCRencontrar my_key,elesubstituiráno
cassetepara <MOIP_KEY>.
Comistoconfigurado,todososnossoscassetesqueusarem my_keye
my_tokenserãosubstituídos.Anossarequisiçãoaoendpointdomoipseria
salvaassim:
---
http_interactions:
- request:
method: post
uri: https://<MOIP_DEV_KEY>:<MOIP_DEV_TOKEN>@desenvolvedor \
.moip.com.br/sandbox/ws/alpha/EnviarInstrucao/Unica
Agoranossoscassetesnãopossuemmaisnenhumainformaç ãodomoip
tokenekeyreais. Noentanto,seolharmoscomaten ção,estainformação
nãoseencontramaisnoscassetese,noentanto,elaaindaédisponívelna
configuraçãodoVCR.
Pararemovermosporcompletoovalorhardcodeddemoiptokenekey
denossoprojeto,podemosutilizaro dotenv,quenospermitecriarvariáveis
deambientenoescopodanossaaplicaç ão.
37

## Página 52

2.9. URIsnãodeterminísticas CasadoCódigo
dotenv
Armazenarasconfiguraçõesdaappemvariáveisdeambienteéum
dosprincípiosdo twelve-factor app(http://12factor.net).Qualquerconfi-
guraçãoquemudedependendodoambiente(development,staging,pro-
ductionetc.)deveserarmazenadaemumavariáveldeambientecomo:
• Dadosdebancodedados,Memcachedetc.
• DadosdeserviçosexternoscomoAmazonS3ouFacebook.
O dotenvcarregaasvariáveisdefinidasnoarquivo .envnaraiz
desuaappetornadisponívelovalordasvariáveisnaconstante ENV,
facilitandooprocessodesedefinirvariáveisdeambienteapenasparao
escopodoprojeto.
Criadasasvariáveisdeambiente,simplesmentealteramosnossaconfigu-
raçãopara:
VCR.configure do |c|
# ...
c.filter_sensitive_data(’<MOIP_KEY>’) { ENV[’MOIP_KEY’] }
c.filter_sensitive_data(’<MOIP_TOKEN>’) { ENV[’MOIP_TOKEN’] }
end
Eadefinimosnormalmentenonossoarquivo .envcomosolicitadopelo
dotenv.Valelembrarquenãoadicionamosestearquivoaorepositório,as-
simgarantimosqueapenasnóstemostaiscredenciais. Nãoseesque çade
deixarclaronoseuprojetoopensourceque,paraousocorreto,deve-secriar
umarquivo .envepreenchertaisvariáveis.
2.9 URIs não determinísticas
Nosexemplosanteriores, sempreestávamosacessandoamesmaURIem
nossoteste,masemalgunsmomentospodemosnãotertotalcontroledisto.
38

## Página 53

CasadoCódigo Capítulo2. Testesqueacessamrede...WTF!?!
Imagineaseguintesituação: estamosutilizandooPaperclip(Gemde
uploaddearquivos)edizemosparaeleque,nonossomodelJogo,éobri-
gatórioocampo capa,queéumaimagemdoPaperclip.Vamosaele.
class Jogo < ActiveRecord::Base
# ...
validates :capa, attachment_presence: true
has_attached_file :capa,
storage: :s3,
bucket: ENV[’AMAZON_S3_BUCKET’],
path: "jogos/capas/:id.:style.:extension",
s3_credentials: {
access_key_id: ENV[’AMAZON_ACCESS_KEY_ID’],
secret_access_key: ENV[’AMAZON_SECRET_ACCESS_KEY’]
}
end
ConfiguramosoPaperclipparamandarnossasimagensparaaAmazon
S3,edefinimosumcaminhodosarquivossalvos. Utilizamosoiddonosso
modelparageramosaimagem.
Aprincípionãoteremosproblemasnenhum,anãosersechegarmosa
umaaçãoemquenãopossamosdefinirovalorde iddomodelJogodean-
temão.Umdestescasoséumasimplesactionde createemumcontroller
deumaapprails.
Actioncreate
Vamosagorafazerumasimplesactiondecreateparaonossomodelgame.
class JogosController < ApplicationController
# ...
def create
@game = current_user.jogos.build(params[:jogo])
if @game.save
39

## Página 54

2.9. URIsnãodeterminísticas CasadoCódigo
redirect_to new_jogo_path
else
render ’new’
end
end
end
Trata-sedeumasimplesactioncomumemdiversasapprailsporaí.Va-
mosdarumaolhadanostestes.
describe JogosController do
describe "POST ’create’" do
context ’com sucesso’ do
let(:params) do
{
’game’ => {
’name’ => ’Zelda’,
’platform’ => ’wii’,
’capa’ => fixture_file_upload(’/lorempixel.png’)
}
}
end
it ’cria um novo jogo’ do
expect do
post :create, params
end.to change(Jogo , :count).by(1)
end
end
end
end
Éumtestebemcomumemdiversasrailsappstambém. Masatenteao
detalhedequeutilizamoso fixture_file_upload,queéumhelperque
nosajudaaenviararquivosemnossostestesdecontroller.
Aorodarmosostestes,deparamo-noscomamensagemdoVCRdizendo
40

## Página 55

CasadoCódigo Capítulo2. Testesqueacessamrede...WTF!?!
queestamosfazendoumarequisiçãoequeelenãosabecomotratar. Neste
caso,quemestáfazendoarequisiçãoéoPaperclipparaenviarnossaimagem
paraaAmazonS3.Comofizemosanteriormente,adicionamosoVCR.
describe JogosController do
describe "POST ’create’", :vcr do
# ...
end
Rodamosotestenovamenteeestátudoverde.Noentanto,agoravema
pegadinha:rodeostestesnovamente.Uou!Recebemosamensagemdeerro
novamentedoVCR,masagorajátemosoblocodoVCReumafixturecriada!
Oquepodeestarerrado?
Requestmatching
OVCRutilizaasrequisiçõesparafazerummatchesaberqualresposta
retornar. Porpadrão,utiliza-seoverboHTTPeaURI,sendoassim,seseu
testefizerrequisiçõesdiferentesacadavezquerodar,oVCRretornaráum
erroinformandoquenãosabelidarcomisso.
Vamosentenderemquemomentoestamosfazendoestarequisiç ãodife-
rente. OlhandonovamenteparaonossosetupdoPaperclip,deparamo-nos
comaconfiguraçãodo path:
path: "jogos/capas/:id.:style.:extension"
Comoestamostestandoumaactiondecreate,onosso idédinâmico:
acadavezquerodamosostesteségeradoum iddiferentee,comocon-
sequência,aURIqueoPaperclipacessaparaenviaroarquivoparaaAmazon
S3tambémédiferente,dadoqueépassadoeste path.
AbrindoocassetedoVCR,vemosaURIdorequestalgocomo https://
myproject-development.s3.amazonaws.com/jogos/capas/2.original.png.
Aorodarmosotestenovamente,o2do 2.original.pngpodenãoser
mas2,massimqualqueridgeradopelobancodedados.
41

## Página 56

2.9. URIsnãodeterminísticas CasadoCódigo
Resolvendooproblema
ProcurandonadocumentaçãodoVCR,podemosnosdepararcomo
mododegravação :new_episodes.Noentanto,elenãoresolvenossopro-
blema:umavezquearequisiçãonãodeumatch,eleadicionaumnovocassete
nomesmoarquivo,ouseja,nonossocaso,seriacomosenãoestivéssemos
usandodoVCR.Cadavezquerodássemosostestesseriaconsideradaum
novoepisódio.
Um método que quase resolve o nosso problema é o
VCR.request_matchers.uri_without_param. Contudo, ele fun-
cionasomentecomparâmetrospassadosviaquerystring.
Poderíamosresolverissocriandoummatchercustomizado. Maspara
estecasoemespecíficoseriaesfor çodemaissemnecessidade,afinalsabemos
queoPaperclipfuncionaeébemtestado.Queremosapenasqueelenãoque-
brenossotestedecontrollerequenãotenhamosquetestaroPaperclipnova-
mente.
ParaissoalteramosonovoVCRparaqueo bodysejausadonomacthing
derequisição.
describe JogosController do
describe "POST ’create’",
vcr: { match_requests_on: [:body] } do
# ...
end
Destemodo,nãoestamosnosimportandocomométodoHTTPeaURI
darequisição.Apenasestamosenviandoomesmo bodysempre,ouseja,a
imagem.
Assimconseguimosfazercomquenossostestescontinuempassando,e
nãoprecisamostestarnovamenteoPaperclipnotestedocontroller.Somente
precisamosverificarqueelenãonosgeraproblemasdevidoaURIsnãode-
terminísticas.
ValelembrarquesefosseumcódigonossoqueestivesseacessandoaURI
nãodeterminística,enãooPaperclip,fariasentidoutilizarmosummatcher
customizado,dadoqueestaríamostestandoarequisição.
42

## Página 57

CasadoCódigo Capítulo2. Testesqueacessamrede...WTF!?!
2.10 Conclusão
Nestecapítulovimosdiversasdicasetécnicasquenosajudamquandoesta-
mosescrevendotestesqueacessamrede,entreelas:
• Testesqueacessamredepodemserumgrandeproblema;
• Construímosumasimplesclassequeacessaahttp://pokeapi.co/;
• UtilizamosoWebMockparaforjaranossarespostaHTTP;
• Forjamos nossa resposta HTTP de uma melhor maneira usando o
cURLemconjuntocomoWebMock;
• AutomatizamosoprocessodeforjarrespostasHTTPutilizandooVCR;
• ConfiguramosoVCRparaintegrar-seaoRSpecutilizandoometadado
doRSpec;
• Diminuímosonúmerodefixturesgeradasaoutilizarmosometadado
doRSpec;
• VimoscomofiltrardadossensíveisdafixturedoVCR;
• AprendemosautilizaroVCRemURIsnãodeterminísticas,comoao
enviarumarquivoparaaAmazonS3.
Nopróximocapítuloveremoscomopodemosnoslivrardasfixturesde
umaapprailsutilizandoa factory_girl.Sejáutilizaafactory_girlnãosepreo-
cupepoishaverábastantecoisalegalcomoutilizá-laparaobjetosquenãosão
ActiveRecordetestesparaela.
43

## Página 59

Capítulo3
Fixturessãotãochatas!Conhe ça
afactory_girl
3.1 Introdução
Seemalgummomentojátrabalhamosemalgumarailsapp,utilizamosfix-
turesoufactoriesparatestar. Sevocêjáaconhece,podecontinuarlendo,
porquetembastanteconteúdolegal,mesmopraquemjáusaafactory_girl
nodiaadia!Senuncausouafactory_girl,vouconvencê-loagora!=)
Provavelmentetemalgumafixtureassimnoseucódigo.
charizard:
nome: Charizard
id_nacional: 6
ataque: 89

## Página 60

3.2. Instalação CasadoCódigo
Eumcódigoqueautilizadaseguintemaneira.
describe ’#nome_completo’ do
it ’exibe o nome e o id nacional’ do
pokemon = pokemons(:charizard)
expect(pokemon.nome_completo).to eq(’Charizard - 6’)
end
end
Oproblemadestaabordageméque,nonossoteste,nãoficaclaroquais
sãoosvaloresdefinidosparaoobjetopokémon.Qualéoataquedestepoké-
mon?Qualoseuid_nacional?Paradescobrirmostudoisso,temosqueabriro
nossoarquivodefixtureevertaisinformações,ouseja,afixtureéumaforma
de Mystery Guestdevidoàsuadefiniçãoeestádistantedocontextoemque
estamosutilizando.
ClaroquepodemostrocarafixturealiparausardiretamenteoActive
Recordcom Pokemon.create;destemodoteremosadefiniç ãojuntoao
contexto. Masestaabordagemnãoénemumpoucoprática,poisaoadici-
onarmosumnovocampocomvalidaç ãonomodel Pokemon,teremosque
iratrásdediversaschamadasa Pokemon.createparacorrigiroserrosde
validaçãoqueserãolan çadose,porconsequência,fazemnossostestesque-
brarem.Alémdisso,estaríamosdefinindodiversoscamposquenãotêmnada
avercomocontextoqueestamostestandoapenasparaavalidaç ãodoActive
Recordpassar.
Comonemtudosãofloresasfactoriessãolentas,devidoasempreestarem
persistindonobancodedados,masganhamemlegibilidadeeflexibilidade.
Nãosepreocupe,veremosalgumasdicasdecomoevitarestalentidãoneste
capítulo.
Temosestasduasvertentesnacomunidade:osqueusamfactory_girl[7]e
osqueusamfixtures[4].Leiaestecapítulo,comeceumnovoprojetoeutilize
factories,façaasuaprópriaexperiência.
3.2 Instalação
Simplesmenteadicionamosagemaonosso Gemfilee,emseguida,rodamos
bundle.
46

## Página 61

CasadoCódigo Capítulo3. Fixturessãotãochatas!Conhe çaafactory_girl
group :development, :test do
gem ’factory_girl_rails’
end
Se não estivermos utilizando Rails, podemos adicionar a gem
factory_girlnolugarde factory_girl_rails.
Eucostumoutilizara factory_girlnoambientededevelopmente
testpoisassimconsigousarasfactoriesnoconsoledeumaapprails.
3.3 Criando nossa primeira factory
Para nossa primeira factory, criamos um arquivo em
spec/factories/usuarios.rb, iniciamos com o bloco
FactoryGirl.define e, depois, chamamos o método factory,
querecebeumblococomadefiniç ãodanossafactory.Criamosumafactory
de usuario,queémapeadoparaonossomodel Usuario.
FactoryGirl.define do
factory :usuario do
nome ’Mauro’
email ’mauro@helabs.com.br’
end
end
A factory_girl carrega automaticamente as factories em
spec/factories.rb e spec/factories/*.rb. Como boa prá-
tica,criamosumarquivodefactoryparacadamodel–nonossocasoaqui,o
usuarios.rb.
Umaboapráticaparaquandoestamosdefinindoumafactoryédefinir
apenasosatributosquesãonecessáriosaomodel,ouseja,aquelesquesão
obrigatóriosdevidoàvalidaçãodoActiveRecord.Veremoscomocriarfac-
toriesmaisespecificasadiante.
3.4 Utilizando a factory
Definimosanossafactorynoexemploanterior. Vamosbrincarcomela
umpoucodiretopeloconsole,depreferênciaemmodosandbox.Paraisso,
47

## Página 62

3.5. Factoriesnostestes CasadoCódigo
rails c --sandbox. Assim,todososregistrosqueinserirmosnobanco
dedadosserãoapagadosaosairmosdoconsole.
Paracriarnossaprimeirafactoryusamos.
FactoryGirl.create(:usuario)
Comoretorno,teremosumobjetoActiveRecordquefoisalvononosso
bancodedados,utilizandoosvaloresquedefinimosnanossafactorynase ção
anteriorcomobloco FactoryGirl.define.
Utilizando FactoryGirl.create(:usuario),novamenterecebere-
mosumerrodevalidação,dadoquenonossomodelédefinidoqueocampo
emaildeveserúnico. Agoraéquevemumadasvantagensdafactoryem
relaçãoàfixture:podemosalteraranossafactorysemanecessidadedecriar
umanova.Fazemosdaseguintemaneira:
FactoryGirl.create(:usuarios, email: ’mauro@helabs.com.br’)
O registro foi criado com sucesso. A factory_girl nos deixa passar
comoparâmetrocadaumdoscamposdefinidosnoActiveRecord. Pode-
mosalteraranossafactorysemanecessidadedecriarmosoutrafactoryno
spec/factories/usuarios.rb.
3.5 Factories nos testes
Noexemploanterior,vimoscomoutilizara FactoryGirlnoconsolepara
apenasconhecermosseucomportamento. Oseuusorealénoambientede
testes.Vamosaele.
Umasimplesactionshow
Vamossuporquetemosumaaction show,queexibeoconteúdodeum
artigo. Umpossíveltesteseriaverificarmosseavariável @artigofoiatri-
buídacorretamenteparaanossaview.Paraisso,criaremosumainstânciade
Artigoutilizandoafactory_girlenossotestesimplesmenteverificasefoi
passadoparaaviewo @artigo,pelométodo assigns.
Vejaoteste.
48

## Página 63

CasadoCódigo Capítulo3. Fixturessãotãochatas!Conhe çaafactory_girl
describe "GET ’show’" do
let!(:artigo) do
FactoryGirl.create(:artigo)
end
before do
get :show, id : artigo
end
it ’assigns a artigo’ do
expect(assigns(:artigo)).to eq(artigo)
end
end
Vamosagoraaocontroller.
class ArtigosController < ApplicationController
def show
@artigo = Artigo.find(params[:id])
end
end
Rodamosotesteeagoraeleestápassando. SeguindooTDD(verme-
lho,verdeerefatorar),estamosnomomentoderefatorar.Nonossocontrol-
ler,nãotemmuitooquefazer,estábemlegalparaomomento. Maspode-
mosmelhoraronossoteste,maisespecificamente,omodocomousamosa
FactoryGirl.
ConfigurandoaFactoryGirl
No nosso exemplo anterior, utilizamos
FactoryGirl.create(:artigo). Para usar a nossa factory de
Artigo, no entanto, é bastante verboso ter que sempre se referir à
classe FactoryGirlquandoqueremoscriarumafactory.
Porisso,afactory_girlnosofereceaop çãodeusarmosapenas create
emnossostestes. Bastaadicionarmosaonosso spec_helper.rbose-
guinte:
49

## Página 64

3.5. Factoriesnostestes CasadoCódigo
RSpec.configure do |config|
# ...
config.include FactoryGirl::Syntax::Methods
end
Assimpodemosalterarnosso let!queusaafactorypara:
let!(:artigo) do
create(:artigo)
end
Agoratemosumaversãobemmenosverbosanousodenossafactory.
Umasimplesactioncreate
Emumtestedecontrollerdaactiondecreatedeumarailsappqualquer,
provavelmenteteremosumtrechocomoaseguir.
describe "POST ’create’" do
let(:params) do
{
artigo: {
titulo: ’Meu título’,
conteudo: ’Conteúdo do artigo’
}
}
end
it ’create a new artigo’ do
expect do
artigo :create, params
end.to change(Artigo, :count).by(1)
end
end
Adeclaraçãode paramsestábemgrandinha,dadoquetemosquemon-
tarohashcomosatributos.Nestecaso,passamosapenasdoisatributos,mas
emummodelmaiorasituaçãosópioraria.
50

## Página 65

CasadoCódigo Capítulo3. Fixturessãotãochatas!Conhe çaafactory_girl
Comoestamosutilizandoafactory_girljádefinimosestesvaloresem
nossafactory,dadoquesãoosobrigatórios.Noentanto,o createnosre-
tornaumobjetoActiveRecordecriaumregistronobanco,enãoéissoque
queremos. Queremosapenasosvaloresquepassamosparaafactory,para
issoutilizamosométodo attributes_for.Vamosalteraronosso let.
let(:params) do
{ artigo: attributes_for(:artigo) }
end
O attributes_fornosretornaumhashcomovalordefinidoem
nossafactorye,assimcomoo create,podemosalterarosvaloresaoinvocá-
lo,passandoumhashopcional.
attributes_for(:artigo, titulo: ’Novo título’)
Utilizandoo attributes_for,nossotestedecontrollerficabemmais
enxuto.
describe "POST ’create’" do
let(:params) do
{ artigo: attributes_for(:artigo) }
end
it ’create a new artigo’ do
expect do
artigo :create, params
end.to change(Artigo, :count).by(1)
end
end
3.6 SendoDRY
Herança
Atéomomento,criamosapenasumafactoryparacadamodel,masécomum
definirmosmaisfactoriesparafacilitaronossousoenãoprecisarficarpas-
sandosempreosmesmosparâmetros.
51

## Página 66

3.6. SendoDRY CasadoCódigo
Vamosagoradefinirduasfactoriespara Artigo. Umadeumartigo
aprovadoeoutraparaumartigonãoaprovado. Aoutilizarmosumbloco
factorydentrodeoutro,definimosumafactoryqueherdaosvaloresda
factorypai.
factory :artigo do
titulo ’Diversas dicas do RSpec’
conteudo ’Contenteúdo de Diversas dicas do RSpec’
factory :artigo_aprovado do
aprovado true
end
factory :artigo_nao_aprovado do
aprovado false
end
end
Aochamarmos FactoryGirl.create(:artigo_aprovado),esta
terátodososvaloresdefinidosnafactory artigomaisosdefinidosem
artigo_aprovado.
Vejaumexemploaoutilizarmos FactoryGirl.create(:artigo_aprovado).
#<Artigo:0x000001090c8668> {
:id => 9,
:titulo => "Diversas dicas do RSpec",
:conteudo => "Contenteúdo de Diversas dicas do RSpec",
:created_at => Thu, 16 Jan 2014 21:05:18 UTC +00:00,
:updated_at => Thu, 16 Jan 2014 21:05:18 UTC +00:00,
:aprovado => true
}
Se usarmos apenasFactoryGirl.create(:artigo), o valor de
aprovadoseránil.
Esteéumbommododemantermosaboapráticadedefinirapenasosva-
loresobrigatóriosquandodeclaramosafactorybase,enasfactoriesdefinidas
viaherançapassamososvaloresnãoobrigatórios.
52

## Página 67

CasadoCódigo Capítulo3. Fixturessãotãochatas!Conhe çaafactory_girl
Sendomelhor,utilizandotraits
Herançaémuitolegal!Noentanto,imaginequetenhamosumafactory
comumtítulotodoemcaixaaltaquesejaaprovadaeumaoutrafactorynão
aprovada.Alémdisso,temosquemanteraversãoquejáfuncionacomotitulo
domodoqueestá.
factory :artigo do
titulo ’Diversas dicas do RSpec’
conteudo ’Contenteúdo de Diversas dicas do RSpec’
factory :artigo_aprovado do
aprovado true
end
factory :artigo_nao_aprovado do
aprovado false
end
factory :artigo_aprovado_titulo_maiusculo do
titulo ’DIVERSAS DICAS DO RSPEC’
aprovado true
end
factory :artigo_nao_aprovado_titulo_maiusculo do
titulo ’DIVERSAS DICAS DO RSPEC’
aprovado false
end
end
Comosepodever,come çamosacriarmuitarepetição,ocampo titulo
e aprovadoforamduplicadoscomomesmovalor.
Vamosrefatoraragoraparausarmostraits.Traits,assimcomoaodecla-
rarmosafactory,tambémrecebeumbloco.Destaforma,vamosremoveras
declaraçõesdasoutrasfactories:deixamosapenasafactory artigoecria-
mosumatraitparacadaumadasnossasnecessidades.
factory :artigo do
titulo ’Diversas dicas do RSpec’
53

## Página 68

3.6. SendoDRY CasadoCódigo
conteudo ’Contenteúdo de Diversas dicas do RSpec’
trait :aprovado do
aprovado true
end
trait :nao_aprovado do
aprovado false
end
trait :titulo_maiusculo do
titulo ’DIVERSAS DICAS DO RSPEC’
end
end
Vamosagoravercomoutilizaratraitparacriarmosanossafactoryantiga
artigo_aprovado_titulo_maiusculo. Paraisso,passamosapenasos
símboloscomosnomesdastraits.
FactoryGirl.create(:artigo, :aprovado, :titulo_maiusculo)
Valelembrarqueaindapodemospassarumhashopcionalsequisermos
alterarqualquerumdosparâmetros.
FactoryGirl.create(:artigo, :aprovado, :titulo_maiusculo,
conteudo: ’Novo conteúdo’)
Nonossoexemplo,passamosapenasumparâmetro,noentanto,épossível
passarquantosforemnecessários.
Agora não temos mais repetição de nenhum campo. Se não gos-
tar muito de ter que sempre ficar passando a trait, e preferir chamar
artigo_aprovado_titulo_maiusculo,épossívelfazeristo,masdesta
vezsemrepetição.
factory :artigo do
titulo ’Diversas dicas do RSpec’
conteudo ’Contenteúdo de Diversas dicas do RSpec’
trait :aprovado do
54

## Página 69

CasadoCódigo Capítulo3. Fixturessãotãochatas!Conhe çaafactory_girl
aprovado true
end
trait :nao_aprovado do
aprovado false
end
trait :titulo_maiusculo do
titulo ’TITLE’
end
factory :artigo_aprovado_titulo_maiusculo,
traits: [:aprovado, :titulo_maiusculo]
end
E utilizamos a factory como fizemos anteriormente,
FactoryGirl.create(:artigo_aprovado_titulo_maiusculo).
3.7 Atributos dinâmicos nas factories
Atéomomento,definimosemnossasfactoriesosatributosmanualmente,
masserialegalsepudéssemosbrincarumpoucoutilizandoatributosmais
dinâmicos,afinalestamosprogramando.
LazyAttributes
Podemospassarumblocoparaosatributosdasfactoriesquandoquere-
mosqueestesvaloressejamavaliadosacadavezqueumainstânciaécriada.
factory :artigo do
titulo ’Diversas dicas do RSpec’
conteudo ’Contenteúdo de Diversas dicas do RSpec’
created_at { 2.days.ago }
end
Alteramosovalorde created_atparachamar 2.days.ago,demodo
que,semprequeumregistroforcriado,teráovalorde created_atadata
de2diasatrás.
55

## Página 70

3.7. Atributosdinâmicosnasfactories CasadoCódigo
DependentAttributes
Vamos alterar nossa factory de artigo para definirmos o valor de
conteudo dinamicamente, exibindo informações dotitulo e do
aprovado.Paraisso,passamosumbloco,afinalseráumatributolazy.Den-
trodesteblocotemosacessoaosoutrosatributosdomodel.
factory :artigo do
titulo ’Diversas dicas do RSpec’
conteudo
{ "Conteudo do artigo #{titulo}. Approved: #{aprovado}" }
end
Observequealteramosonosso conteudoparaterumvalormaisre-
levante,exibindoo tituloeovalorde aprovado. Podeparecermeio
desnecessáriodeclararconteudocomumvalormaisdescritivo,mastodoo
valordeseterum conteudodinâmicoévistoquandoestamosdebugando,
afinal,temosmaisinformaçõesúteisdoobjetodeumamaneirafácildeser
lida.
Sequences
Atéomomento,onossocampo tituloéomesmoparatodasasfac-
tories. Vamosalterarparaestevalortambémserdinâmico,masagoranão
baseadoemoutroscampose,sim,emumasequênciadevalores.
Primeirodefinimosum sequence,passandoumsymbolcomonomedo
campoquequeremosutilizar,epassamosumblocoparageraresteconteúdo
docampo titulo. Nadefiniçãodenossafactory,simplesmenteusamos
titulo,queutilizaovalorgeradopelasequence.
FactoryGirl.define do
sequence :titulo do |n|
"Diversas dicas do RSpec #{n}"
end
factory :artigo do
titulo
56

## Página 71

CasadoCódigo Capítulo3. Fixturessãotãochatas!Conhe çaafactory_girl
conteudo
{ "Conteudo do artigo #{titulo}. Approved: #{aprovado}" }
end
end
Destemodo,nossasfactoriesgeradasterãoostítulos:“Diversasdicasdo
RSpec1”,“DiversasdicasdoRSpec2”,“DiversasdicasdoRSpec3”etc.
Inlinesequence
Comoestamosutilizandoapenasovalorde sequenceparaafactory
deartigo,podemosdefinirestevalorinline,como sequencediretamente
dentrodoblocode factory.
factory :artigo do
sequence(:titulo) { |n| "Diversas dicas do RSpec #{n}" }
conteudo
{ "Conteudo do artigo #{titulo}. Approved: #{aprovado}" }
end
Destemodo,economizamosalgumaslinhaseficamaisclarooqueestá
acontecendo.
Podemosalterarovalorinicialsimplesmentepassandooprimeirovalor
parao sequence,daseguintemaneira:
factory :artigo do
sequence(:titulo, 125) { |n| "Diversas dicas do RSpec #{n}" }
conteudo
{ "Conteudo do artigo #{titulo}. Approved: #{aprovado}" }
end
Assim,nossasfactoriesgeradasterãoostítulos:“DiversasdicasdoRSpec
125”,“DiversasdicasdoRSpec126”,“DiversasdicasdoRSpec127”etc.
Épossívelpassarqualquerobjetoqueimplementeométodo #nextassim
podemospassarumastring.
factory :artigo do
sequence(:titulo, ’a’) { |n| "Diversas dicas do RSpec #{n}" }
conteudo
57

## Página 72

3.8. Associações CasadoCódigo
{ "Conteudo do artigo #{titulo}. Approved: #{aprovado}" }
end
Comovocêdeveimaginar,osnossostítulosserãogeradoscomo:“Diver-
sasdicasdoRSpeca”,“DiversasdicasdoRSpecb”,“DiversasdicasdoRSpec
c”etc.
3.8 Associações
NomundoRails,ébemcomumtermosqueusarasassociaçõesdoActive
Record,paraligarmosumaentidadeàoutra.Vamosvercomopodemoscriar
estasassociaçõesutilizandoasfactories.Primeiro,nossafactoryde Usuario.
factory :usuario do
nome ’Mauro’
email { "#{nome}@helabs.com.br" }
end
Agora, nossafactoryde Artigo. Onossorelacionamentoédeum
Artigoquepertencea( belongs_to)um Usuarioeum Usuariotem
vários(has_many) Artigos.
factory :artigo do
titulo ’Diversas dicas do RSpec’
conteudo { "Conteudo do #{titulo}" }
trait :aprovado do
aprovado true
end
factory :artigo_aprovado, traits: [:aprovado]
end
Criandoaassociaç ãodiretamente
Podemoscriaraassociaçãonomomentoemqueestamosutilizandoa
nossafactory,daseguintemaneira:
usuario = FactoryGirl.create(:usuario)
FactoryGirl.create(:artigo, usuario: usuario)
58

## Página 73

CasadoCódigo Capítulo3. Fixturessãotãochatas!Conhe çaafactory_girl
Primeiro,criamosumainstânciade Usuarioepassamosparafactoryde
Artigo,noatributo usuario,umobjeto Usuario.Dessaforma,aasso-
ciaçãoécriadaautomaticamenteeconseguimoscriarumusuárioquepossui
umartigocriado.
Definindoaassociação
Dadoquetodo Artigoéescritoporumusuário,nãoserialegaltermos
emnossafactoryum Artigosemusuário,senão,semprequefôssemosuti-
lizarafactoryde Artigo,teríamosqueficarcriandoumusuárioepassar
explicitamentecomofizemosnoexemploanterior.Seriamelhorsedefinísse-
mosissonanossafactorydiretamente.Éoquefazemossimplesmentedecla-
randoabaixode conteudoo usuario.Nãopassamosnenhumvalorpara
usuario,mascomoexisteumafactorycomestenome,afactory_girlcriaa
associaçãoautomaticamente.
factory :artigo do
titulo ’Diversas dicas do RSpec’
conteudo { "Conteudo do #{titulo}" }
usuario
trait :aprovado do
aprovado true
end
factory :artigo_aprovado, traits: [:aprovado]
end
Comisso,afactory_girlirácriarsempreumusuárioassociadoaumar-
tigo,quandoutilizarmosafactorydeartigo.
Definindoafactorynaassociaç ão
Nossaassociaçãoentre Usuarioe Artigoaindanãoestálegal,afinal
nãotemosousuáriodoartigomaissimoautordoartigo.Vamosalterarnosso
modeldeformaquereflitaisso.
class Artigo < ActiveRecord::Base
59

## Página 74

3.8. Associações CasadoCódigo
belongs_to :autor, class_name: ’Usuario’
end
Valelembrarqueparaissofuncionardevemosteracoluna autor_id
naclasse Artigo,porissorenomeamosanossacoluna usuario_idpara
autor_id.
Agoraquetemosaassociaçãodeque Artigopertenceaum Usuario,
seelafornomeada autornossafactoryquebrará.
Vamos definir a associação na nossa factory trocando a chamada de
usuariopara association,passandoonomedaassociaç ãoequalfac-
toryqueremosdefinirparaatal.
factory :artigo do
titulo ’Diversas dicas do RSpec’
conteudo { "Conteudo do #{titulo}" }
association :autor, factory: :usuario
trait :aprovado do
aprovado true
end
factory :artigo_aprovado, traits: [:aprovado]
end
Podemosalterarafactorydeusuáriopassandoosparâmetrosadicionais
daseguintemaneira:
association :autor, factory: :usuarios, nome: ’Mauro George’
Aliases
Noexemploanterior,utilizamosométodo associationparadefinira
factorydaassociação. Nãopodemosnosreferenciara autordiretamente,
dadoquenossafactoryestádeclaradacomo usuario.
Podemosdeclararumaliasparanossafactoryde Usuario,assimpo-
deremosutilizar autordiretamente.Paraisso,simplesmentepassamosum
arrayparaachave aliases.
60

## Página 75

CasadoCódigo Capítulo3. Fixturessãotãochatas!Conhe çaafactory_girl
factory :usuario, aliases: [:autor] do
nome ’Mauro’
email { "#{nome}@helabs.com.br" }
end
Dessa forma, além de podermos utilizar a factory
como FactoryGirl.create(:usuario), é possível usar
FactoryGirl.create(:autor).
Podemosalteraranossafactorydeartigoparautilizarafactorydeautor
diretamente,quenadamaisédoqueumaliasdafactorydeusuário.
factory :artigo do
titulo ’Diversas dicas do RSpec’
conteudo { "Conteudo do #{titulo}" }
autor
trait :aprovado do
aprovado true
end
factory :artigo_aprovado, traits: [:aprovado]
end
Definindoumaassociaçãohas_many
No exemplo anterior, definimos na factory uma associação
belongs_to, onde dizemos que umArtigo pertence a Usuario.
Vamosagoradefinirumaassociaç ão has_many,paraum Usuarioque
temváriosArtigos.
Nossaprimeiratentativaprovavelmenteseriadefiniro artigodireta-
mente.
factory :usuario, aliases: [:autor] do
nome ’Mauro’
email { "#{nome}@helabs.com.br" }
artigo
end
61

## Página 76

3.8. Associações CasadoCódigo
Ao tentarmos rodar o código usando
FactoryGirl.create(:autor), recebemos o seguinte erro do Ac-
tive Record: NoMethodError: undefined method 'artigo='for
#<Usuario:0x000001090012e8>'. Afinal, o nosso modelUsuario
nãoimplementa artigo=,esim artigos=,dadoquetemos has_many
:artigos.
Nãoadiantatentarmostrocar artigopara artigos,poisnãoobtere-
mossucesso. Issoporqueafactory_girltentaráencontrarumatraitcomo
nomedeartigosemvezdecriaraassociaç ão.
Conseguimoscriaraassociaçãodiretamentecomofizemosnoexemplo
anterior,utilizando:
autor = FactoryGirl.create(:autor)
FactoryGirl.create(:artigo, autor: autor)
Mascomodefinimosumaassociaçãohas_manydiretamentenafactory?
Conhecendooscallbacks
AssimcomooActiveRecord,afactory_girltambémpossuioscallbacks.
Utilizaremosocallback after(:create)pararesolveronossoproblema
econseguircriarumaassociação has_manynadefiniçãodenossafactory.
Definimosprimeiroumatrait,apenasporquenãoqueremosquetodosos
usuáriostenhamumartigocriado,jáquenãoéumdadoobrigatório.Lembra
daboapráticané?
Nanossatrait,chamamosocallback after(:create),querecebeum
bloco,ecomoprimeiroargumentoelenospassaainstânciadafactorycri-
ada.Então,simplesmentepassamosonosso Usuarioparaacriaçãodeum
artigo.Domesmomodoquefizemosaoutilizarafactorydiretamente,agora
conseguimosfazerissonadefiniçãodafactory.
factory :usuario, aliases: [:autor] do
nome ’Mauro’
email { "#{nome}@helabs.com.br" }
trait :com_artigo do
after(:create) do |usuario|
62

## Página 77

CasadoCódigo Capítulo3. Fixturessãotãochatas!Conhe çaafactory_girl
create(:artigo, autor: usuario)
end
end
end
Oproblemaéquetodoautorteráapenasumartigocriado.Seriabomse
conseguíssemosaumentarestenúmero.
Ocreate_list
Seprecisássemoscriarumacole çãodeartigos,provavelmenteutilizaría-
mos #times.
3.times { FactoryGirl.create(:artigo) }
Noentanto,afactory_girlnosdáométodo create_list.Assim,po-
demostrocarousodo timespara:
FactoryGirl.create_list(:artigo, 3)
Ficoufácilalterarnossafactoryparacriarcadaautorcompelomenos3
artigos.
factory :usuario, aliases: [:autor] do
nome ’Mauro’
email { "#{nome}@helabs.com.br" }
trait :com_artigo do
after(:create) do |usuario|
create_list(:artigo, 3, autor: usuario)
end
end
end
Agorasim,todosautorestêm3artigos.É...masesequisermosumautor
com4artigos? #comofas?
63

## Página 78

3.8. Associações CasadoCódigo
OláTransientAttributes
Afactory_girlnosdáaop çãodedefinirmosatributosquenãoestãoem
nossomodel.Paraisso,utilizamosumbloconométodo ignoree,seutili-
zarmosestesatributosemconjuntocomocallback,conseguiremosdefinira
quantidadedeartigosquequeremoscriardinamicamente.
Paraisso,passamosparaobloco ignoreonosso transient attribute,o
total_de_artigosedefinimosovalor3. Passamosparaonossobloco
do after(:create)umnovoparâmetro,o evaluator,quearmazena
todososvaloresdafactory,inclusiveosignorados.Assim,passamosovalor
de total_de_artigosparao create_list.
factory :usuario, aliases: [:autor] do
nome ’Mauro’
email { "#{nome}@helabs.com.br" }
trait :com_artigo do
ignore do
total_de_artigos 3
end
after(:create) do |usuario, evaluator|
create_list(:artigo, evaluator.total_de_artigos,
autor: usuario)
end
end
end
Podemosagoracriarusuárioscomaquantidadedeartigosquedesejar-
mosdaseguintemaneira:
FactoryGirl.create(:usuarios, :com_artigo, total_de_artigos: 10)
Seomitirmosoparâmetro total_de_artigos,eleserácriadocomo
valorpadrão,quedefinimoscomo3.
FactoryGirl.create(:usuarios, :com_artigo)
64

## Página 79

CasadoCódigo Capítulo3. Fixturessãotãochatas!Conhe çaafactory_girl
3.9 Bah, mas só funciona com ActiveRecord?
Curtiubastanteafactory_girleagoraquerusarfactoryparagerarconteúdo
quenormalmenteérepetido,né?Vamosfazerissoentão.
Quandotrabalhamoscomahttp://pokeapi.co,vimosqueelaretornaum
JSON.DiversoscolaboradoresdonossosistemaestãoacessandoesteJSON,
entãoserámuitocomumvermosemdiversostestesalgocomooseguintepara
declararamesmastring,oualteraralgunscamposemdiversoslugares:
json = %({"national_id": 6, "name": "Charizard", "attack":84,
"defense":78})
Porpadrão,afactory_girléparadefiniçãodeobjetosActiveRecord.Va-
mosvercomofazemosparaafactory_girltrabalharcomoutrosobjetos.
Vamosprimeirodefiniraspropriedadesdequeprecisamos:
factory :pokeapi do
id_nacional 6
nome ’Charizard’
ataque 84
defesa 78
end
Ao tentarmos executar esta factory diretamente, receberemos
NameError: uninitialized constant Pokeapi, porque a fac-
tory_girlestátentandocriarumainstânciade Pokeapie,comonãoexiste
estemodel,oerroélan çado.
NossoJSONnadamaisédoqueumastringruby,entãovamosdizeristo
àfactory_girlparaverseajuda.
factory :pokeapi, class: String do
id_nacional 6
nome ’Charizard’
ataque 84
defesa 78
end
Novamente,aoexecutarmosafactory_girl,recebemoserro,masagora
oerroé NoMethodError: undefined method 'id_nacional='for
65

## Página 80

3.9. Bah,massófuncionacomActiveRecord? CasadoCódigo
"":String. Issoporqueafactory_girlestátentandopassarcadaumdos
atributos à classe como faz com o Active Record, mas não é assim que
instanciamosumastring! Vamosalterarnovamentenossafactory,, agora
paraterum initializercustomizado. Paraissoutilizaremosométodo
initialize_with,querecebeumbloco,dentrodoqualinstanciamosa
nossaclasseString.Paracriaranossaclasse,primeirocriamosumhashcom
cadaumdosatributosdefinidosnafactorye,emseguida,passamosestehash
parao JSON.generate,quetransformaohashemumJSONretornando
umastring.Adicionamostodososnossosatributosnobloco ignore,pois
usaremososnossosatributosno initialize_with,enãonastringdire-
tamente.
factory :pokeapi, class: String do
ignore do
# ...
end
initialize_with do
info = { national_id: id_nacional, name: nome,
attack: ataque, defense: defesa }
JSON.generate(info)
end
end
Vamosagorautilizarnossafactorye...recebemosoutroerro!Caramba!
Estouachandoqueissonãovaifuncionar=/
Agora o erro foi NoMethodError: undefined method
'save!'for #<String:0x00000108b28eb0>, ou seja, a factory_girl
aindapensaqueestamosusandoocomportamentodeumobjetoActive
Recordetentachamar save!emnossastring.
Para resolvermos isso, simplesmente utilizamos o método
skip_create,quedefinequenossafactorynãochamaráo save!.
factory :pokeapi, class: String do
skip_create
ignore do
66

## Página 81

CasadoCódigo Capítulo3. Fixturessãotãochatas!Conhe çaafactory_girl
# ...
end
# ...
end
Agorasimnossafactoryestáfuncionando!EretornandoonossoJSON.
Utilizamosafactorycomoqualqueroutra.
FactoryGirl.create(:pokeapi)
Podemospassarqualquerumdosparâmetroscomofizemosanterior-
mente.
FactoryGirl.create(:pokeapi, nome: ’Bulbasaur’)
Agoraquenossafactoryestáfuncionandopodemosfazertudodelegal
quejávimosutilizandoafactory_girlcomotraits.
3.10 Conhecendo as estratégias
Atéomomento,utilizamosduasestratégias,mesmosemsaberqueesseerao
nomedelas. Foramo createeo attributes_for. Ocreatesalvao
objetonobancodedadoseo attributes_fornosretornaumhashcomo
vimosanteriormente.
Écomumutilizarmossempreo create,masrealmentesemprepreci-
samosdosdadospersistidosnobancodedados? Vamoscriarummétodo
#nome_completoparaonossomodel Pokemon.Primeiro,vamosaoteste.
Verificamosqueométodo #nome_completoéonomedopokémonseguido
doseu nacional_idseparadoporumtraço.
describe ’#nome_completo’ do
let(:pokemon) do
create(:pokemon)
end
subject do
67

## Página 82

3.10. Conhecendoasestratégias CasadoCódigo
pokemon.nome_completo
end
it ’exibe o nome e o id nacional’ do
expect(subject).to eq(’Charizard - 6’)
end
end
Vamos agora fazer este teste passar, criando o método
#nome_completo,quesimplesmenteconcatenao nomeeo id_nacional.
class Pokemon < ActiveRecord::Base
def nome_completo
"#{nome} - #{id_nacional}"
end
end
Nossotestepassa,noentanto,estamoscriandoumregistronobancode
dadostodavezqueotesteérodado,eissoélento.Vamosvercomopodemos
melhorar.
Conhecendoobuild
Uma das estratégias da factory_girl é obuild. Diferentemente do
create,obuildapenascriaoobjetoActiveRecordnãoopersistindono
bancodedados.Vamosverumexemplo.
pokemon = FactoryGirl.build(:pokemon)
Podemosversenossoobjetoestásalvoounãosimplesmenteusandoo
métodopersisted?doActiveRecord.
pokemon.persisted?
Nonossocaso,éretornado false. Podemospensarqueo buildda
factory_girlseriaomesmoqueutilizarmoso newdoActiveRecord,passando
osatributosdefinidosnafactory.
Podemosrefatorarnossotesteparausaro buildsimplesmentealterando
onosso let.
68

## Página 83

CasadoCódigo Capítulo3. Fixturessãotãochatas!Conhe çaafactory_girl
let(:pokemon) do
build(:pokemon)
end
Nossostestescontinuampassando,dadoqueelesnãotêmdependência
nenhumacomobancodedados,apenascomosatributosdefinidosemnosso
objeto.
build_stubbed,oirmãomaispoderosodobuild
Uma outra estratégia disponibilizada pela factory_girl é o
build_stubbed. Diferente do build, não estamos criando um ob-
jeto Active Record real, mas sim fazendo stub de seus métodos. Em
consequência,estaestratégiaéamaisrápidadetodas.Vamosaumexemplo.
pokemon = FactoryGirl.build_stubbed(:pokemon)
Diferentementedo build,nossoobjetoagecomoestivessepersistido,
porisso,aousarmos pokemon.persisted?,nossoresultadoserá true.
Nosso objeto somente age como se estivesse persistido, pois se fizermos
um Pokemon.countantesedepoisdousodo build_stubbedobtere-
mosomesmovalor,mesmoqueexplicitamentesalvemosnossoobjetocom
#save!. Como build,realmenteoobjetoésalvonobancodedadosse
usarmos #save!.
Comonossotestenãodependediretamentedobancodedados,podemos
alterá-loparautilizaro build_stubbed.
let(:pokemon) do
build_stubbed(:pokemon)
end
Ocódigonormalmentedevedependermenosdoseuestadoemrelaç ão
aobancodedadosedependermaisdoseuestadoemrelaç ãoaoutrosobjetos.
Sendoassimanãoserqueestejamostestandométodosquefaç amconsultas
nobancodedados,éumaboapedidautilizaro build_stubbed.
69

## Página 84

3.11. Equandoasfactoriesnãosãomaisválidas? CasadoCódigo
3.11 Equando as factories não são mais v álidas?
Vimosnoiníciodocapítuloqueéumaboapráticadefinirmosapenasosatri-
butosquesãoobrigatóriosdevidoàvalidaç ãodoActiveRecord. Maséco-
mum,nonossodesenvolvimento,termosqueadicionarnovoscamposdevido
anovasvalidaçõesdonossomodel.
Vamossuporqueagoraonossomodel Pokemonganhouumnovocampo
ataqueeesteéobrigatório.Vamosàvalidação.
class Pokemon < ActiveRecord::Base
validates :ataque, presence: true
end
AgoraaotentarmosrodarnossafactorydePokémonreceberemosose-
guinteerrodoActiveRecord:
ActiveRecord::RecordInvalid:
Validation failed: Attack can’t be blank
Imagineagoraissonasuasuítedetesteseumaboabasedelasutilizando
afactorydepokémon.Teremosdiversostestesquebrados.
Paraevitarisso,criamostestesparaasnossasfactoriesdaseguintema-
neira:primeirocriamosumarquivoem spec/factories_spec.rbeuti-
lizamosométodo FactoryGirl.factoriesparaobtertodasasfactories
declaradas.Emseguida,iteramossobrecadaumadestasfactoriescriandoum
testeparacadauma,dinamicamente. Everificamosseafactoryrespondea
valid?antesdefazermosaasser ção,poisnemtodasasfactoriesherdamde
ActiveRecord::Base,comovimoscomafactory pokeapi.
describe ’FactoryGirl’ do
FactoryGirl.factories.map(&:name).each do |factory_nome|
it "factory #{factory_nome} is valid" do
factory = build(factory_nome)
if factory.respond_to?(:valid?)
expect(factory).to be_valid
end
70

## Página 85

CasadoCódigo Capítulo3. Fixturessãotãochatas!Conhe çaafactory_girl
end
end
end
Agoratemostestesparaasfactories,noentanto,nossasuíterodaasspecs
emordemaleatória.Sendoassim,nossasspecsdasfactoriesficaramperdidas
nomeiodetodasasoutrasspecsecontinuaremoscomummontedespecs
quebradas.Podemosrodarapenasaspecdasfactoriesparaverseoproblema
élá,masépossívelautomatizarisso,rodandoasspecsdasfactoriesantesda
nossasuíte.Paratanto,adicionamososeguintecódigoanosso Rakefile:
if defined?(RSpec)
desc ’Run factory specs.’
RSpec::Core::RakeTask.new(:factory_specs) do |t|
t.pattern = ’./spec/factories_spec.rb’
end
end
task spec: :factory_specs
Quesimplesmenterodaasspecsdasfactoriesantesderodarasdemais
specse,casoalgumaspecdefactoryquebre,eleneminiciaosdemaistestes.É
exatamenteoqueprecisamos:assim,seumadenossasfactoriesquebrar,não
ficaremosassustadosaoverumaboapartedenossasuítedetestequebrando.
Conhecendoolint
Aprendemosanteriormentecomotestarnossasfactories. Noentanto,é
chatoterqueficarcopiandoistoparatodososprojetosemqueiremostraba-
lhar.Eseautomatizarmosisto?Afinal,éumpadrão.Foipensandonissoque
opessoalquetrabalhanofactory_girlcriouo FactoryGirl.lint.Elefaz
exatamenteoquefizemosmanualmente:rodanossasspecsdefactoriesantes
dasspecsdoapp.
Parautilizarolint,adicionamosumbloco before(:suite)emnosso
spec_helper.rb,chamandoo FactoryGirl.lint.
RSpec.configure do |config|
# ...
71

## Página 86

3.12. Conclusão CasadoCódigo
config.before(:suite) do
FactoryGirl.lint
end
end
Agoratemosomesmoresultado,noentanto,deumamaneiramaisenxuta
eportávelentrediversosprojetos.
3.12 Conclusão
Esperoquetenhagostadodafactory_girledetodasastécnicasquevimos
aqui.Comcertezaissoajudarámuitoquandoestiverescrevendoosseustes-
tes.Nestecapítulo:
• Vimosasvantagensedesvantagensdousodefactorysobrefixtures;
• Definimoseutilizamosnossaprimeirafactory;
• Utilizamosnossafactorynostestes;
• Configuramosofactory_girlparasermenosverbosoduranteostestes;
• Utilizamosherançaetraitparanãonosrepetirmosaodeclararmosas
nossasfactories;
• Utilizamosatributosdinâmicosnasfactories;
• Criamosassociaçõesbásicasentrefactories;
• Definimosumaassociaçãocomplexautilizandocallback, trait, cre-
ate_listetransientattributes;
• Utilizamosafactory_girlparagerarumobjetoquenãoéActiveRecord;
• Conhecemosasdiversasestratégiasqueafactory_girlpossui;
• Aprendemostestarasnossasfactoriesparaevitarmossurpresasdesa-
gradáveis.
Continueporaíquenopróximocapítuloviajaremosnotempoutilizando
otimecop.Veremosporquedevemostomarcuidadocomtestesquedepen-
damdedataecomopodemosutilizarotimecopparanosajudar.
72

## Página 87

Capítulo4
Precisamosir...devoltaparao
futuro
4.1 Introdução
Nossoappdebatalhaspokémonsestáevoluindo. Temosqueimplementar
umanovafuncionalidadequeéselecionartodosospokémonsqueforamse-
lecionadosnodiaanterior. Utilizaremosestesdadosparaexibiremalgum
momentonosistema.
Vamos primeiro ao nosso teste. Criaremos um método
Pokemon.escolhidos_ontem. Primeiro, definimos o nosso cenário,
queconsistede3pokémons:umquefoiescolhidohoje,umquefoiescolhido
ontemeumquefoiescolhidoantesdeontem.Paraisso,definiremosovalor
de Pokemon#escolhido_emutilizando Time.zone.local.

## Página 88

4.1. Introdução CasadoCódigo
describe ’.escolhidos_ontem’ do
let!(:pokemon_escolhido_hoje) do
create(:pokemon,
escolhido_em: Time.zone.local(2015, 1, 8, 1))
end
let!(:pokemon_escolhido_ontem) do
create(:pokemon,
escolhido_em: Time.zone.local(2015, 1, 2, 23, 59, 59))
end
let!(:pokemon_escolhido_antes_de_ontem) do
create(:pokemon,
escolhido_em: Time.zone.local(2014, 1, 2))
end
end
Tendodefinidoonossocenário,vamosdefiniragoraosujeitodonosso
testeeoprimeiroteste,dequeo Pokemon.escolhidos_ontemdevere-
tornarospokémonsqueforamescolhidosnodiaanterior.
subject do
Pokemon.escolhidos_ontem
end
it ’tem o pokemon escolhido ontem’ do
expect(subject).
to include(pokemon_escolhido_ontem)
end
Rodam
osonossotesteeelequebra,dadoqueaindanãodefinimoso
nossométodo.Vamoscriá-loagora.
Comonecessitamosdeummétododeclassequeretorneumacole çãode
pokémons,podemosutilizaro scopedoActiveRecord.Criamosumescopo
chamado escolhidos_ontemquefazum whereretornandoospokémons
criadosentremeia-noitedodiaanterioremeia-noitedehoje,ouseja,ontem.
class Pokemon < ActiveRecord::Base
74

## Página 89

CasadoCódigo Capítulo4. Precisamosir...devoltaparaofuturo
scope :escolhidos_ontem, -> do
where(escolhido_em:
1.day.ago.midnight..Time.zone.now.midnight)
end
end
Rodamos novamente nosso teste e agora ele passa. Vamos implementar 
agora os testes dos pokémons que ele não deve incluir, que são os que foram 
escolhidos hoje e os que foram escolhidos antes de ontem.
it ’não tem o pokemon hoje’ do
expect(subject).to_not include(pokemon_escolhido_hoje)
end
it ’não tem o pokemon escolhido antes de ontem’ do
expect(subject).
to_not include(pokemon_escolhido_antes_de_ontem)
end
Rodamos nossa suíte novamente e todos os testes continuam verdes. Ter-
minamos nosso trabalho por hoje, no entanto, na manhã do dia seguinte ao 
rodar os testes novamente recebemos erros nos testes que antes passavam!
Mas por quê? Se observarmos, nos nossos testes definimos  o dia de hoje como 
1/02/2015
, e o utilizamos no pokemon_escolhido_hoje. Durante 
todo aquele dia nossa suíte de testes funcionará mas, em qualquer outro 
dia, ela quebrará, dado que não estaremos mas no dia 2/02/2015.
4.2 Congelando o tempo com timecop
A gem timecop nos dá exatamente os poderes de que necessitamos, de parar
otempo em
 um momento especifico. Se conseguíssemos manter o tempo 
sempre no dia 2/02/2015, nossos testes sempre passariam, dado que 
naquele dia eles passavam.
Instalação
Vamosins
talarotimecopsimplesmenteadicionando-oaonossoGemfile:
75

## Página 90

4.2. Congelandootempocomtimecop CasadoCódigo
gem ’timecop’
Efinalizamosrodando bundle.
Congela
ndootempo
Agoraquetemosotimecopinstalado,vamosaosnossostestes.Otimecop
nosforneceométodo Timecop.freezeparapararmosotempo.Passamos
comoprimeiroparâmetroolugardotempoquequeremosparareumbloco
comocontextodoquedeveserparadonotempo.
it ’tem o pokemon escolhido ontem’ do
Timecop.freeze(
Time.zone.local(2015, 1, 2, 12)) do
expect(subject).to include(pokemon_escolhido_ontem)
end
end
Agora to
do código que é executado dentro do bloco do
Timecop.freeze é interpretado como se a data fosse 7/03/2014 às
12:00:00. Fizemosnoprimeiroteste,mastemosqueaplicarotimecopaos
demaistestestambém.
it ’não tem o pokemon hoje’ do
Timecop.freeze(
Time.zone.local(2015, 2, 2, 12)) do
expect(subject).to_not include(pokemon_escolhido_hoje)
end
end
it ’não tem o pokemon escolhido
antes de ontem’ do
Timecop.freeze(
Time.zone.local(2015, 3, 3, 12)) do
expect(subject).
to_not include(pokemon_escolhido_antes_de_ontem)
end
end
Observeq
ueestamosrepetindodiversasvezesadefiniç ãodehojecom
o Time.zone.local(2015,
 3, 3, 12) e está sendo um valor mágico, 
afinal, não sabemos o que esta data quer dizer a não ser que analisemos o 
contexto todo, lendo os demais testes.
Podemosmelhorarissodefinindoo hoje,utilizandoo let.
76

## Página 91

CasadoCódigo Capítulo4. Precisamosir...devoltaparaofuturo
let(:hoje) do
Time.zone.local(2014, 3, 3, 12)
end
Em seguida, alteramos todos os nossos testes que usam o timecop para 
utilizarem o valor definido no let.
it ’tem o pokemon escolhido ontem’ do
Timecop.freeze(hoje) do
expect(subject).to include(pokemon_escolhido_ontem)
end
end
Dado que o timecop nos dá o poder de parar o tempo, é uma boa prática 
definirmos o nosso “hoje” sempre no passado, pois assim evitamos qualquer 
surpresa de os testes passarem no dia e começarem a falhar depois de um 
tempo. Para facilitar nosso trabalho, alteramos apenas o ano de 2014 para 
2010 do nosso hoje.
let(:hoje) do
Time.zone.local(2000, 3, 3, 12)
end
Por que tantos lets?
Vamos olhar para nosso teste. Perceba que temos definido to do o nosso 
cenário dos testes em diversos let antes de qualquer um deles. No entanto, 
vamos analisar o nosso primeiro teste.
it ’tem o pokemon escolhido ontem’ do
Timecop.freeze(hoje) do
expect(subject)
.to include(pokemon_escolhido_ontem)
end
end
Perce
ba que em nenhum momento estamos uti-
lizando o pokemon_escolhido_ontem e o
pokemon_escolhido_antes_de_ontem, mas apenas o
pokemon_escolhido_ontem. Então, por que declaramos todos eles
77

## Página 92

4.3. Removendorepetição CasadoCódigo
antes? Normalmente por não fazermos TDD, pois, no nosso exemplo,
criamostodososcenáriosparasódepoisiniciarmosostestes.
Aparentementenãofazmalnenhum,correto? Errado! Lembraquando
falamosquefactoriessãolentas 3.1? Fazendoestetipodeabordagemajuda
atorna
rumtestelento,afinalestamoscriandoobjetosnobancodedados
quenãosãonemusadosnoteste. Issotambémdeixaostestesfrágeis,pois
estamoscriandoumcenáriograndequeédifícildesemanteremtestesque
testamordenação,porexemplo.
Vamosa
lterá-loparadefinirapenasosdadosquesãousadosporeles.Para
isso,removemoso letecriamosonossoobjetoapenasdentrodoblocodo
teste,queéondeeleéutilizadosomente.
it ’tem o pokemon escolhido ontem’ do
pokemon_escolhido_ontem = create(:pokemon
,
escolhido_em: Time.zone.local(2010, 3, 3, 23, 59, 59)) 
Timecop.freeze(hoje) do
expect(subject).to include(pokemon_escolhido_ontem)
end
end
Agoranos
sosobjetossãocriadosapenasquandonecessários. Porisso,
ésemprebomfazermosoTDD,esepercebermosumarepetiç ão,extraímos
paraum let,
comofoiocasodo hoje.Emmuitosdoscasosépossíveluti-
lizaro letparadefinir
ocenário,apenasdeixeissosurgir.Quandoperceber
quemuitodosseustestesestãodeclarandoomesmoobjeto,movaparaum
letmasnãoiniciegerandotodoocenário.
4.3 Removendo repetição
Olhandoparanossostestes,vemossempreachamadaa Timecop.freeze
emtodoseles. Otimecopnosdáapossibilidadedeutilizarmosumasin-
taxesemanecessidadedeumbloco. Paraisso, vamosdefinirumbloco
before, dado que todo o nosso contexto depende da data, com a cha-
madaa Timecop.freeze, e
umbloco after, emqueutilizaremoso
Timecop.returnquevolt
aotempoparaonossohojereal.
78

## Página 93

CasadoCódigo Capítulo4. Precisamosir...devoltaparaofuturo
before do
hoje = Time.zone.local(2010, 3, 3, 12)
Timecop.freeze(hoje)
end
after do
Timecop.return
end
Perceba que movemos a definição do hoje para dentro do before, já 
que não iremos utilizá-lo em mais de um lugar. Para finalizar, removemos o 
Timecop.freeze dos nossos testes.
it ’tem o pokemon escolhido ontem’ do
pokemon_escolhido_ontem = create(:pokemon
,
escolhido_em: Time.zone.local(2010, 2, 3, 23, 59, 59)) 
expect(subject).to include(pokemon_escolhido_ontem)
end
Agora removemos a repetição dos testes. No entanto, temos que lem-
brar que sempre que utilizamos o timecop sem o bloco temos que usar o 
Timecop.return pois se não, o tempo não é retornado para o hoje atual. 
Como os testes são rodados em ordem aleatória, o tempo continuará o de-
finido no timecop mesmo em testes que não o  estão utilizando, o  que pode 
gerar testes quebradiços que q uebram aleatoriamente. O pior é que é muito 
difícil de se identificar o problema, visto que nenhuma exce ção é lançada.  
Com alguns seeds os testes passarão e com outros não.
describe ’.outro_metodo’ do
it ’faz alguma
coisa’ do
puts Time.zone.now
end
end
Nesse exemplo, removemos o bloco after, para testes apenas. Em algum 
momento, o valor de Time.zone.now pode ser 2000-03-03 12:00:00 
-0300, o valor que foi definido pelo timecop em outro contexto de testes, ou
79

## Página 94

4.3. Removendorepetição CasadoCódigo
ovalorreal.Sendoassim,cabeanósdesenvolvedoresficarmosatentosaouso
decadaumadenossasferramentasparanãogerarmosproblemasparatodo
otimeporumsimplesdescuido.
Ordem aleatória nos testes
Umaboapráticaésemprerodarmosostestesemordemaleatória.
Issoporquetestesqueestejamdependendodeoutrossãoumproblema,
poisnãosabemosondeestádefinidatodasuaestrutura,demodoque
nãoficaclarooqueestásendotestado,enemépráticodesealteraralgo,
dadoqueumaalteraçãopodefazeroutrostestesquebrarem.
Porpadrão,aoutilizarmosogeradordorspec-rails,eleadicionaa
seguintelinhano spec_helper.rb:
config.order = "random"
Eladefinequenossostestesserãoexecutadosemordemaleatória.
Sendoassim,éumaboaverificaremprojetosmaisantigosseelespos-
suemestalinhaeadicioná-lacasoaindanãotiver.
ORSpecnospermitedefinirsuasconfiguraçõesutilizandoumar-
quivo .rspecnaraizdoprojeto,ounonossodiretório home.Podemos
definirnonossohomeparasemprerodarostestesemordemaleatória,o
quenosajudaaencontrarproblemas,jáquepodemosesquecerdefazer
averificaçãoemprojetosantigos.Nestearquivosimplesmenteadiciona-
mos:
--order random
Seencontrarmosqualquerproblemaaorodarmosostestes,podemos
fazerusodo seedgeradoparadebugutilizando rspec spec --seed
182,simplesmentetrocandoo182pelovalorgeradopeloRSpec.
Aindapodemosdefinirotimecopparaoperarno safe mode, emque
éaceitoapenasasintaxedebloco. Paraisso, simplesmenteadicionamos
Timecop.safe_mode = trueaonosso spec_helper.rb.
80

## Página 95

CasadoCódigo Capítulo4. Precisamosir...devoltaparaofuturo
4.4 Rails 4.1 e o ActiveSup-
port::Testing::T ime
Helpers
A part
ir do Rails 4.1, foi criado o módulo
ActiveSupport::Testing::TimeHelpers, que nos oferece méto-
dosparavi
ajarmosnotempoassimcomocomotimecop.
ComoestamosutilizandooRSpec,primeirotemosqueincluiromódulo.
Paraisso,utilizamoso spec_helper.rb.
RSpec.configure do |config|
# ...
config
.include ActiveSupport:
:Testing::TimeHelpers
end
C
omomóduloinseridosimplesmentetrocamosde Timecop.freeze
para travel_toede Timecop.returnpara travel_back,emantemos
omesmocom
portamentodotimecop.Noentanto,agoranãohánecessidade
deumagemextra.
before do
hoje = Time.
zone.local(2010, 3, 3, 12)
travel_to(hoje)
end
after do
travel_back
end
Assim como o Timecop.freeze, o travel_to também aceita um 
bloco, de forma que não é necessário usar o travel_back. No entanto, não 
se esqueça de sempre usar o travel_back se não estiver usando um bloco, 
como no nosso exemplo, para evitarmos o problema de testes quebradiços 
que vimos anteriormente.
Mas e o timecop ainda faz sentido? Sim! Em projetos que não são Rails 
ou que não utilizem o ActiveSupport. A dica é: se tiver em uma app Rails, ou 
se seu projeto tiver o ActiveSupport, utilize o travel_to; nos demais casos 
utilize o timecop.
81

## Página 96

4.5. Conclusão CasadoCódigo
4.5 Conclusão
Esperoquetenhacurtidonossaviagemnotempo! Agoratemosemnosso
arsenalmaisumaferramentaquenosajudaalidarcomtestesquedependam
dedata.Nestecapítulo:
• Vimosquedevemostercuidadoaolidarmoscomtestesquedependam
dedatas;
• Congelamosotempoutilizandootimecop;
• Removemosrepetiçãodenossocódigoutilizandoo let;
• Vimosquetantosletspodemserumsinaldequefizemosalgode
errado;
• Utilizamosotimecopsemasintaxedebloco;
• Aprendemosquesempredevemosvoltaraotempoatualquandoutili-
zamosotimecopsemobloco;
• ConhecemosoActiveSupport::Testing::TimeHelpers,que
éumaalternativaaotimecopparaquandoestamosemumambiente
RailsouquepossuaoActiveSupport.
Agoraquevoltamosdanossaviagemnotempo,continueaíquenopró-
ximocapítuloconheceremosoSimpleCov,umaferramentaquenospermite
mediroquefoitestadoemnossocódigo,everemossedevemosounãoter
100%donossocódigocobertoportestes.
82

## Página 97

Capítulo5
Seráquetesteitudo?
5.1 Introdução
Duranteonossodiaadia,estamosfazendoTDDenquantoescrevemosnos-
soscódigos,noentanto,ficaumadúvida:seráquetesteitudo?Seráquetestei
todasaspossibilidades? Anteriormentevimos 1.6quenãodevemostestar
apenaso happy pathmascomosaberoquetestamoseoquenãotestamos?
ConhecendooSimpleCov
OSimpleCovéumaferramentadecoberturadecódigoemRubyque
analisaquaislinhasdocódigoforamtestadasequaisnão,enosretornaum
HTMLcomoresultadogerado.
InstalamosoSimpleCovadicionandoaonossoGemfilenogrupodetes-
tes.

## Página 98

5.1. Introdução CasadoCódigo
gem ’simplecov’, require: false
Parafinalizar,incluímosoSimpleCovno spec_helper.rbeoinicia-
moscom SimpleCov.start.Valelembrarqueestas linhasdoSimpleCov
devemseraprimeiracoisadonosso spec_helper.rb.Elasdevemser
inseridasantesdequalquercódigodaaplicaç ãoserincluído.
require ’simplecov’
SimpleCov.start ’rails’
Nonossoexemplo,passamosparao SimpleCov.starto 'rails',
dadoqueestamosemumaapprails.Destemodo,eleutilizaoprofiledoRails
queagrupaosnossostestesdecontrollers,modelsetc.
Agoraaoexecutarmosnossostesteségeradaumasaídafalandoquala
nossacoberturadetestesatualmente.Algocomo:
Coverage report generated for RSpec to /meuprojeto/coverage.
5 / 5 LOC (100.0%) covered.
ÉgeradoumarquivoHTMLcomdetalhesem coverage/index.html
e,comoboaprática,ignorenogitapastacoverage.
Figura5.1:HTMLgeradopeloSimpleCov
84

## Página 99

CasadoCódigo Capítulo5. Seráquetesteitudo?
Figura5.2:DetalhedeumúnicoarquivonoSimpleCov
Porpadrão,oSimpleCovérodadotodasasvezesqueumtesteéexecu-
tado,sempreexibindoesteoutputduranteonossoTDD,oqueébastante
chato,afinalnãoestamospreocupadoscomissoenquantoescrevemosnos-
sostestes.Paraisso,podemosdefinirqueoSimpleCovseráexecutadoapenas
seumavariáveldeambienteestiverdefinida,vamoschamá-lade
coverage
ecolocarocódigodoSimpleCovdentrodeum if.
if ENV[’coverage’] == ’on’
require ’simplecov’
SimpleCov.start ’rails’ do
minimum_coverage 100
end
end
Destemodo,aorodarmosnossostestes,nãoteremosasaídadoSim-
pleCovapenassedefinirmosissoexplicitamenteutilizando $coverage=on
rspec spec.
5.2 O falso100%
NoRuby,utilizamosbastantemacros,aquelescomoo scopeeo validates
do Active Record. No entanto, estes macros são avaliados enquanto a
classesimplesmenteéincluídanoambientedetestes.Vamospegaronosso
escopo declarado no capítulo4 e adicionar uma validação em
nome e
id_nacional.
85

## Página 100

5.2. Ofalso100% CasadoCódigo
class Pokemon < ActiveRecord::Base
validates :nome, :id_nacional, presence: true
scope :escolhidos_ontem, -> do
where(escolhido_em:
1.day.ago.midnight..Time.zone.now.midnight)
end
end
Rodamosnossotestee,aoverificarmos,vemosqueestácom100%deco-
bertura,issodevidoaousodosmacros.Porisso,sempredevemosteraten ção
aoadicionarmosnovocódigoenãotestarmos.
Aprendendocomoserros
Vimosqueosmacrospodemnosdarumafalsaconfian çadequetudofoi
testado,masnãoapenasosmacros,osnossostestesmesmospodemnosdar
essaimpressão.
Nocapítulo 1.6falamossobreaimportânciadenãotestarmosapenaso
happy path,noentanto,mesmotestandodiversoscenáriospodeserquenão
consigamospreveralgo.Imaginequeestánavegandonoseuappe,emalgum
momento,sedeparacomumpokémonsemnomenatela,ouseja,algumcaso
debordaquenãotestamos.Oquepodemosfazeréutilizarumaferramentade
debug,entenderereplicaroproblema,nonavegadormesmo. Quandoestá
claroqualonossoproblema,criamosumtestederegressão,umtesteque
recebeosmesmosparâmetrosdoproblema,contudo,oseuresultadodeve
seroesperadoenãooerro.
Vamospegaronossoexemploládequandofalamosdo happy path.
def nome_completo
"#{nome} - #{id_nacional}"
end
Como vimos, pode ser que um pokémon esteja com onome e o
id_nacionalvazios.Aonosdepararmoscomumpokémondesseemnossa
tela,teremosexibidosimplesmenteum - (traçocomespaçosnoinicioe
nofinal),oquenãoénemdelongeoquequeremos.Umaabordagemrápida
86

## Página 101

CasadoCódigo Capítulo5. Seráquetesteitudo?
porémerrôneaseriasimplesmenteadicionaro ifaliparaeleretornar nil
esertratadocorretamentenacamadadeapresentaç ão.
def nome_completo
"#{nome} - #{ id_nacional}" if nome && id_nacional
end
Noentanto,porqueissoéerrado?Porquenãofoiescritonenhumteste,
ofamosotestederegressão,afinalmudamosocomportamentodealgoenão
testamos.Assimoutrapessoadotimepodevirduranteumrefactoringesim-
plesmenteremovero ifaorodarostestestodospassaram,assimoproblema
foiinseridonovamentenosistema.
Otestederegressãonadamaisédoqueumtestecomooutroqualquer.O
mesmotesteescritonocapítulo 1.6podeserconsideradoumtestederegres-
são,seelefoicriadodiantedestascondições.
context ’quando não possui o nome e o id nacional’ do
subject do
Pokemon.new
end
it ’é nil’ do
expect(subject.nome_completo).to be_nil
end
end
Comoregraésemprebomadicionarumalinha,um ifouoquefor
escreverumteste,issoseestivermudandoocomportamentodoobjeto. Se
forapenasumrefactoringnãoénecessário,amenosqueextraiacódigopara
umanovaclasse.
Nãotesteassociaç ões,validaç õesouescoposdoActiveRecord
CertavezocriadordoRailsfezumpostsobretestesemqueeleincluía
7coisasanãosefazerenquantoseestárealizandotestes[3].Umadelasera
exatamenteisto:nãotestarassociações,validaçõesouescopos.Masseráque
issoéumacoisarealmenteboaasefazer?
87

## Página 102

5.2. Ofalso100% CasadoCódigo
Osdefensoresdestamaneiraderealizarostestesdefendemqueestecom-
portamentoétestadopeloRails,oqueécorreto.Noentanto,oRailsnãotesta
queeuchameiadeclaraç ãodeumaassociaçãoouvalidação,porexemplo.
Assim,semeumodelo Pokemondefinirasseguintesvalidações:
class Pokemon < ActiveRecord::Base
validates :name, :id_nacional, presence: true
end
Eeuasremover,nenhumtestemeuquebrará! Acabamosdeveromal
queissopodetrazer.
Algunsdefendemquetaisvalidaçõesouassociaçõesdevemsertestadas
emtestesdecontrolleroudeintegração.Testesdeintegraçãosãolentos,epor
issonãosãocriadosmuitoscasosdeusocomodetestesunitários.Enoseu
testedecontroller,vocêrealmentevaificartestandocadaumdestesparâme-
tros?Ouvaitestarapenascomumcontextoválidoouuminválido?Estetipo
deabordagemficapioraindaaofalarmosdeassociaçõesouescopos.
Associaçõeshas_many,porexemplo,podemdefinirumaop çãocha-
mada dependent.Sendoassim,aotestarodeletardeumusuárionocon-
trollervocêvaitestartambémquefoideletadoseusartigos?Emumsimples
blog,estalógicaésimples.Agoraaumenteaquantidadederelacionamentos
queummodeloemumsistemademédio/grandeportepossui.Senestecaso
fizerostestesnocontroller,jáémelhordoqueassumirqueétestadopelo
Rails.
Escopossofremdomesmoproblemadeassociaç ão,definemumcom-
portamentoquepodesercomplexo. Imagineoexemploqueutilizamosem
4.Seráquenonossocontrollerteríamosescritodiversoscasosdepontaou
apenasumsimplestesteparaoescopo? Provavelmenteapenasumsimples
caso,o happy path.
Umadasvantagensdeescrevermosestestestesdiretamentenomodelé
quesealteramosalgonele,otestedomodelquebraráenãootestedocon-
troller,oquefacilitanahoradeveroquefoiquebrado.
Comosempre,nadaemsoftwareéabsoluto: temososquenãotestam
estescomportamentos[3]unitariamente,assimcomoosquetestam. Estes
88

## Página 103

CasadoCódigo Capítulo5. Seráquetesteitudo?
atécriaramumagemparaajudararealizaralgunsdestestestesqueveremos
maisàfrente. Oimportanteaquiétestar,oquenãopodeéassumirquetal
comportamentojáétestadopeloRails.
5.3 Meu objetivo é ter100% de cobertura de tes-
tes?
Assimcomotemosescolasdiferentesnomodocomoserealizarostestes,o
mesmoocorrequandooassuntoécoberturadetestes.NopostdoDHH[3],
umadesuaspráticaséquenãodevemosfocaremobter100%decobertura
detestes.NaoutrapontatemosUncleBob[5]queacreditaquecadalinhade
códigoquevocêescrevedevesertestada.
Oimportanteéotimevervaloraoescreverostestes. Nãoadiantaum
gerenteoualguémassimimporestapráticaaotime.Comovimos,podemos
terofalso100%,ecasootimenãoestejamotivadoarealizarostestes,ébem
provávelqueescrevamtestesbemruinsparasimplesmenteagradaraferra-
mentadecoberturadetestes.Porisso,éimportanteotimedefinirqualserá
estacobertura,eadicionaraferramenta.
Mesmoumprojetoquetenha100%decoberturadetestespodeterbugs,
pois,comovimos,podeserumcasodefalso100%.Noentanto,seotimeestá
escrevendotestesporquevêvalor,enãoparaagradaraferramenta,ébem
provávelqueaquantidadedebugssejareduzida.Contudo,lembre-sedeque
noprojetoquenãopossuiestes100%decoberturaachancedeterbugssão
maiores.
Umganhoaoseterumaaltataxadecoberturadetestesénahoraem
queiremosrealizarrefatorações,afinaltemosaconfian çadequepodemos
removerummétodo,alterarseucomportamento,extrairclassesetc.Aorea-
lizarmosummovimentoerradodurantearefatoraç ão,algumtestequebrará
enosalertaráparaoproblema,demodoquetemostotalconfian çaaofazer
mudançasparamelhoraronossocódigo.Emprojetoscomumataxadeco-
berturamenor,provavelmenteninguémiráalteraraquelemétododomodel
quenãopossuitestesunitários.Seforalterá-lo,émelhorescrevertestesuni-
táriosparaeleparasódepoisfazerarefatoraç ão.Assimgarantimosquenão
quebramosseucomportamento.
89

## Página 104

5.3. Meuobjetivoéter100%decoberturadetestes? CasadoCódigo
Outrobenefíciodeumaaltataxadecoberturadetesteséqueelanosajuda
aencontrarcódigoquenãoémaisutilizadoe,noentanto,aindaestáali.Nor-
malmente,quandoestamosfazendorefatoraçõesmovendométodosdeum
ladoparaoutro,definindoalgunscomoprivadoseremovendooutros,ébem
provávelquetenhaalgoaliquenãoémaisutilizado. Com100%decober-
turadetestes,conseguimosterissofacilmenteexposto,dadoquepodemos
ternonossoprocessodeintegraç ãoestaverificaçãode100%decoberturae
sómandarcódigoparaorepositóriocentralseocódigoatingirtalnível.
Assim,quandofôssemosintegrarnossocódigo,averificaç ãodecobertura
detestesfalhariae,aoverificarmosoporquê,encontraríamosummétodo
privadoquenãoémaisutilizado,esimplesmenteoremoveríamos.
Umdospontosquepodepesarnahoradesedefinirumametadecober-
turadecódigoéocusto,afinal,agoraénecessáriocadadesenvolvedorescre-
vermaisparaentregaramesmafuncionalidade. NomesmopostdoDHH,
elecitaumtrechodoKentBeck.Emumatraduç ãolivre:
“Sou pago para o código que funciona, não para testes, por isso a minha
filosofia é testar o mínimo possível para chegar a um determinado nível de
confiança (eu suspeito que este nível de confiança é alto em comparação com
os padrões da indústria, mas poderia ser apenas arrogância). Se eu não
costumo fazer um tipo de erro (como definir as variáveis erradas em um
construtor), eu não o testo. ”
–KentBeck
QuemsoueuparadiscordardoKentBeck?=)
Masumdetalheaquiéquandoelefala“Seeunãocostumofazerumtipo
deerro”.Normalmente,nãoestamostrabalhandosozinhos,masemconjunto,
emtimesmultidisciplinaresecomcódigocoletivo. Sendoassim,umnovo
membrodotimecommenosexperiênciapodecometerumerroquepara
vocêsejatrivial,eassiminserirumbugnosistemaquepodeserpegosomente
noambientedeprodução.
Porisso,acreditoqueostestesnãosãopagosnasprimeirassemanas,mas
simcomopassardotempo.Afinal,comopassardotempoocódigotende
acrescereficarmaiscomplexo. Emumambienteondenãosepossuiuma
90

## Página 105

CasadoCódigo Capítulo5. Seráquetesteitudo?
grandecoberturadetestes,come çaráaficarconfusosabersealgumaaltera-
çãoteráumimpactonegativonosistemaounão,seumnovobugseráin-
seridoounão.Comumaboacoberturadetestes,temosmaiorconfian çaao
lidarcomocódigo,oquenosajudanamantenabilidadedoprojeto.Ostestes
funcionamcomoumremédio:podemosirtomando-oempequenasdosese
constantemente,ouesperarestarmosemumestadobemruimdesaúdepara
sóassimprocurarummédico.Sabemosmuitobemqueosegundocasotem
umadorbemmaior.
5.4 Mas e você senhor autor, quanto faz de co-
bertura de testes?
Comojádeveimaginarpelooqueacaboudeler,simeusouumdosdefenso-
resdecoberturadecódigo.Eédefinidonoprocessodeintegraç ãoque,senão
tiver100%decobertura,ocódigonãoéintegrado.Agoravamosaosdetalhes.
Primeirodetudo,nãopenseemcoberturadetestesenquantofazoseu
desenvolvimentocomTDD.Depreferência,definaqueoSimpleCovsejaexe-
cutadopordemanda,demodoque,enquantorodaseustestesduranteode-
senvolvimento,ooutputdeleneméexibido,comovimosanteriormente.Adi-
cioneaoseuprocessodeintegraç ãoestaverificaçãodequeseocódigonão
estivercom100%decoberturadetesteselenãoseráenviado.Podeserqueno
começotenhaalgumadificuldade,mascomotempoveráqueterámenosde
100%decoberturaapenasquandoestáfazendoum spike,oudevidoacódigo
mortoquepodeserremovido.
Oimportanteécriarmosohábitodefazerissononossodiaadia,assim
comofazemosoteste: adicionarmaiscoisanonossojogo,queagoradeve
serconseguir100%decobertura.DesdequevimparaoRubysempreescrevo
testes,inclusivefoiumdosmotivosparaeuvirparatrabalharcomRuby.Com
todooecossistemadacomunidadeRuby,temosdiversasferramentasquenos
ajudamaatingirestameta,comoasquevimoseasqueaindavamosver.
Emprojetosnovos,definanoseufluxodeintegraç ãoaverificaçãodeco-
berturade100%comofaladoanteriormente,assimajudaráacriarohábito.
Emprojetosquejápossuemumahistória,adicioneaoprocessodeintegraç ão
averificação,noentanto,comovalordacoberturadetestesdoprojeto,evá
91

## Página 106

5.5. Conclusão CasadoCódigo
adicionandotestesnasáreasqueaindanãopossuem.Emumprojetoqueestá
com80%decobertura,adicionequetodoocódigodeveterestemínimopara
serintegrado.Comotempo,estataxavaiaumentar.Aumentenovamenteo
mínimodecoberturadoprojetoparaeleserintegrado,eemummomentoé
possívelchegaraos100%.
Realmenterecomendoquetenhamos100%decoberturadetestes,dado
quetemosdiversosbenefíciosqueameuversuperamosproblemasrelatados.
Jumpup
Falamosmuitodoprocessodeintegraç ão,contudo,nenhumaferra-
mentafoicitada. Issoporquevocêpodeestáfazendointegraçãoassín-
cronautilizandooTravisCI,porexemplo,ouaindafazendointegraç ão
síncrona.
Casoestejarealizandointegraçãosíncrona,recomendoousodagem
Jumpup,quefazestaverificaçãodecoberturadetestesesóenviacódigo
paraorepositóriocentralseesteatingir100%.
https://github.com/Helabs/jumpup
5.5 Conclusão
Vimosdiversasopiniõesqueacomunidadepossuiquandooassuntoécober-
turadetestes,vamosagoraaoresumo.
• ConhecemosoSimpleCov;
• UtilizamosoSimpleCovpordemanda;
• Aprendemosquepodemosterumfalso100%decoberturadecódigo;
• Passamosportestesderegressão;
• Vimosofamoso“nãotesteassociações,validaçõesouescopos”doAc-
tiveRecord;
• Falamossobreo100%decoberturadetestes;
92

## Página 107

CasadoCódigo Capítulo5. Seráquetesteitudo?
• Finalizamosvendocomoeupessoalmentelidocomo100%decober-
turadetestes.
Testesdevalidaçõesdemodeldeumapprailstendemaacabarficando
bemrepetitivosentrediversosmodels.Nopróximocapítuloveremoscomo
podemosremoverestarepetiçãocome çandoporum shared examplee,em
seguida,ummatcher,conhecendoalgunsmatchersdeterceirosquepodem
nosajudarnestastarefas.
93

## Página 109

Capítulo6
Copiarecolarnãoéumaop ção!
6.1 Introdução
Vamosadicionarvalidaçãoaonossomodel Pokemon,poisatéomomentoele
podesersalvocomtodososvalores nilenãoéoquequeremos.Paraisso,
vamoscomeçarpeloteste,criandoumcasoquedevedarerroaoestarcom
ovalordenomevazio. InstanciamosumPokémonechamamosométodo
valid?,querodatodasasvalidaçõesdeummodel.Depoisdasvalidações
executadas,verificamosnoarray errorsseanossachave nomepossuial-
gumerro.
describe ’validações’ do
describe ’#nome’ do
it ’possui erro quando está vazio’ do

## Página 110

6.2. Osharedexample CasadoCódigo
pokemon = Pokemon.new
pokemon.valid?
expect(pokemon.errors[:nome]).
to include(’não pode ficar em branco’)
end
end
end
Rodamosonossotesteeelequebra.Vamosagoraaomodelimplementar
anossavalidação.
class Pokemon < ActiveRecord::Base
validates :nome, presence: true
end
Executamosnovamenteonossoteste,noentantoagoraelepassa. Va-
mostestaragoraqueaopassarmosumnomeparaonossopokémon,elenão
possuamaisnenhumerro. Novamente,instanciamosumpokémon,agora
definindooseunome,everificamosoarray errorsapósexecutarmoso
valid?.Destavezesperamosqueelepossuaumarrayvazio.
it ’não possui erro quando está preenchido’ do
pokemon = Pokemon.new(nome: ’Charizard’)
pokemon.valid?
expect(pokemon.errors[:nome]).to be_empty
end
Assimfinalizamosavalidaçãodepresen çadocamponomenonossomo-
del Pokemon.Agoratemosquevalidarocampo id_nacional,semfalarde
outroscamposemoutrasentidadesdonossosistemaquepossuemamesma
validaçãodepresen ça. Sabemosquecopiarecolarotestealiseriaumpro-
blema,poisteríamosdiversostestesduplicadosportodoosistema.
6.2 O shared example
ORSpecpossuios shared examplesquenosajudaexatamentenoquepreci-
samos:criartestesreutilizáveis.
96

## Página 111

CasadoCódigo Capítulo6. Copiarecolarnãoéumaop ção!
Vamos primeiro mover os nossos testes do modelPokemon re-
ferentes à validação do nome para um arquivo separado. Por con-
venção, os shared examples são armazenados emspec/support/ e
possuem o prefixo shared_examples_for_. Criaremos o nosso
spec/support/shared_examples_for_validacao.rb. Para criar-
mosumsharedexample,utilizaremosométodo shared_examples,quere-
cebecomoprimeiroparâmetroonomedonossosharedexampleeumbloco
comoconteúdodoexemplocompartilhado.
shared_examples ’valida presenca de string’ do
describe ’#nome’ do
it ’possui erro quando está vazio’ do
pokemon = Pokemon.new
pokemon.valid?
expect(pokemon.errors[:nome]).
to include(’não pode ficar em branco’)
end
# ...
end
end
Criamos o nosso shared exemple comovalida presenca de
stringparafocarmosapenasnavalidaçãodepresen çadecamposdotipo
stringnomomento. Agoraquetemosnossosharedexamplecriado,deve-
mosutilizá-lononossomodel.Paraissoutilizamoso include_examples
passandoonomedosharedexample.
describe ’validações’ do
include_examples ’valida presenca de string’
end
Rodamosnossostestesevemosqueosexemploscontinuampassando.
Semprequetiversharedexamplesequiserrodarestestestes,executetodo
oarquivodetestesenãoapenasumúnicoteste.Issoporqueossharedexam-
97

## Página 112

6.2. Osharedexample CasadoCódigo
plessófuncionamaoexecutarmosoarquivotodo.Nodiaadia,essaéuma
boadicaparasemanteremmente.
Masaindaassim,olhandonovamenteparaonossosharedexample,ve-
mosqueeleaindanãoresolvenossoproblemadeduplicaç ão,dadoqueele
apenasfuncionacomomodel Pokemoneoatributonome.Vamosagoraver
comofazerissodeumamaneiradinâmica.
Sharedexamplesdinâmicos
Osharedexampleaceitaparâmetros,sendoassim,temosquepassarcomo
parâmetroaclasseeumsímbolocomonomedocampodomodelcujapre-
sençaqueremostestar. Alteramosonossosharedexampleparaagorautili-
zaroatributoquefoipassadoporparâmetro.Alémdisso,instanciamosuma
classedeacordocomaquefoipassadaporparâmetroeassimrealizamos
nossavalidaçãodepresen ça.
shared_examples ’valida presenca de string’ do |klass, attr|
describe "#{attr}" do
it ’possui erro quando está vazio’ do
instancia = klass.new
instancia.valid?
expect(instancia.errors[attr]).
to include(’não pode ficar em branco’)
end
end
end
Agoraquefizemosonossoprimeirotesteserdinâmico,vamosfazera
mesmacoisanosegundo.Criamosumhashdinamicamente,definindoova-
lordoatributopassadocomoCharizard. Depoisdeexecutarmosasvalida-
çõesdanossaclasse,verificamosseoatributopassadonãopossuinenhum
erro.
it ’não possui erro quando está preenchido’ do
params = {}
params[attr] = ’Charizard’
98

## Página 113

CasadoCódigo Capítulo6. Copiarecolarnãoéumaop ção!
instancia = klass.new(params)
instancia.valid?
expect(instancia.errors[attr]).to be_empty
end
Agoraquedefinimosonossosharedexampledeumamaneiradinâmica
temosquealteraronossotesteparapassarosparâmetroscorretos.Simples-
mentepassamosanossaclasse Pokemoneumsímbolo :nome,queéovalor
quequeremostestar.
describe ’validações’ do
include_examples ’valida presenca de string’, Pokemon, :nome
end
Nossosharedexampleagorapodeserusadoemoutroscamposdomodel
Pokemon,assimcomoemoutrasentidadesquenecessitemdevalidaç ãode
presençaemumcampostring.
Poderíamosiralémealteraronossoexemploparaelefuncionarbaseado
nocampodefinidoeopreenchimentodovalorsejafeitoautomático,inde-
pendentedeserumastring.Deixoissocomoumexercícioparavocê,leitor.
Comodefinimosadescriçãodonossotestedinamicamente,aindaconti-
nuamoscomumoutputexcelentequandorodamosostestescomoformato
dedocumentação.
Pokemon
validações
nome
possui erro quando está vazio
não possui erro quando está preenchido
6.3 Criando um Matcher
AoinstalarmosoRSpec,játemosumacole çãodematcherspadrões,quesão
definidosnagem rspec-expectations,umadepêndenciadoRSpec.O
rspec-expectationséquemdefineosmatchersqueestamosacostuma-
dosautilizarcomo eq, includeeassimpordiante. Alémdosmatchers
99

## Página 114

6.3. CriandoumMatcher CasadoCódigo
padrões,oRSpecnosdáapossibilidadedecriarmosonossoprópriomat-
cher,entãovamosmoveronossosharedexampleparaummatcher.
Antesdeiniciarmosocódigo,vamosdefinirainterfacedonossomatcher.
Nomatcher eq,pegamosoresultadoecomparamoscomoesperado.
it ’soma dois inteiros’ do
expect(soma(2,2)).to eq(4)
end
Nonossocaso,eunãoqueroterqueexecutaravalidaç ão.Nolugardisso,
passaremosapenasaclassequeserátestada. Ecomonomatchereuquero
passarapenasoatributo,nossainterfacetemqueserusadaassim:
it { expect(Pokemon).to valida_presenca_de_string(:nome) }
Agoraquejátemosumainterfacedefinida,vamoscriaronossomatcher.
Paraisso,come çamoscomo RSpec::Matchers.defineepassamospara
elecomoprimeiroparâmetroonomedonossomatcher.Emseguida,passa-
mosumblocoecomoparâmetrodeleovalorqueseráavaliadonomatcher.
Temosqueimplementaro matchquetambémrecebeumblococujo
parâmetroéoquefoipassadoparao expect,nocasoo sujeito.Éaqui
quedefinimosseacondiçãofoiválidaounãoretornando trueou false.
RSpec::Matchers.define :valida_presenca_de_string do |attr|
match do |sujeito|
end
end
Comobásicopronto,agoratemosquemoveranossalógicadoshared
exampleparacá. Paraissocriamosummétodo verifica_vazio?que
possuioconteúdobemparecidodonossosharedexamplenoteste“ possui
erro quando está vazio”,excetoqueagoraeleéummétodoequenão
fazemosasserçãonenhumadentrodele.Eledeveapenasretornar trueou
false.
match do |sujeito|
verifica_vazio?(sujeito, attr)
100

## Página 115

CasadoCódigo Capítulo6. Copiarecolarnãoéumaop ção!
end
def verifica_vazio?(sujeito, attr)
instancia = sujeito.new
instancia.valid?
instancia.errors[attr].include?(’não pode ficar em branco’)
end
Implementamosaprimeirapartedonossoteste,masnãopodemoses-
quecerdooutro.Movemo-loparacáe,igualaoanterior,retornamosapenas
oresultado,semnenhumaasser ção.Finalizadosambososmétodos,chama-
mosumseguidodooutrodentrodomatch,utilizandoo &&.
match do |sujeito|
verifica_vazio?(sujeito, attr) &&
verifica_preenchido?(sujeito, attr)
end
def verifica_preenchido?(sujeito, attr)
params = {}
params[attr] = ’Charizard’
instancia = sujeito.new(params)
instancia.valid?
instancia.errors[attr].empty?
end
Assim,finalizamosaestruturadonossomatcherepodemosutilizá-lo
conformedefinimosaassinatura.
it { expect( Pokemon).to valida_presenca_de_string(:nome) }
Porumamelhordescri ção
Nomomento,serodarmosnossotesteeelefalharteremosumamensa-
gemgeradapelopróprioRSpec.
expected Pokemon(id: integer, id_nacional: integer, nome: string,
ataque: integer, defesa: integer, created_at: datetime,
updated_at: datetime) to valida presenca de string :nome
101

## Página 116

6.3. CriandoumMatcher CasadoCódigo
Nãoestámuitoclarooproblema,jáqueelemostroutodososcamposda
classe,alémdeexibirumsímbolononomedoatributo.Podemosmelhorar
estasaídautilizandoométodo failure_message,querecebeumbloco
emquepassamosonossosujeitoemostramosumamensagemcustomizada.
failure_message do |sujeito|
"esperava-se que #{sujeito} tivesse validação em #{attr}"
end
Agoraquedefinimoso failure_message,teremosaseguintesaídaem
casodefalha.
esperava-se que Pokemon tivesse validação de presença em nome
Umacoisalegalparaselembraraocriarummatcheréqueelefunciona
tambémemcasodenegação,aoutilizarmoso to_not,oquenosdábastante
flexibilidade.Matcherstambémgerambastanteexpressividadeemnossocó-
digo.
Assimcomoutilizamosonossomatchercomo #to,haverácasosem
quequeremosutilizá-locomo to_not,porém,ficariaestranhaasaídaseti-
véssemosamesmamensagemquedefinimosno failure_message,afinal
estamosfazendooopostoagora.
Para definirmos a mensagem para quando estivermos utilizando o
to_not,temosométodo failure_message_when_negatedquefun-
cionaexatamentecomo failure_message,ondeapenasdefinimosuma
mensagemquefaçasentidoemcasodenegação.
failure_message_when_negated do |sujeito|
"esperava-se que #{sujeito} não tivesse validação em #{attr}"
end
Umadasvantagensdetermosmatchersbemespecíficosépodermosusar
omatchersemanecessidadedeescrevermosumamensagemparao it,dado
queoprópriomatcherjádizocomportamentoesperado.
Issonãoquerdizerquenãodevemosutilizardo itcomumamensagem,
narealidadedevemossempredefinirumaboamensagemquedeixeclaroo
comportamentotestado.Utilizamosomatcherdeumalinhaapenasquando
102

## Página 117

CasadoCódigo Capítulo6. Copiarecolarnãoéumaop ção!
estedefineclaramenteocomportamentotestadoepossuaumaboasaídano
formatodedocumentação.
ORSpecdefineumadescriçãoautomaticamentequandocriamosonosso
matcher,maspodemosmelhorarestasaída. Paraissoutilizamosométodo
descriptionepassamosparaeleapenasanossamensagemquequeremos
exibir.
description do
"valida presença do #{attr}"
end
Assim,finalizamosonossoprópriomatcher.
Agoraquecriamosnossomatcher,nãoquerdizerqueonossoshared
examplenãofaçasentido,dependedodesenvolvedordecidirqualusar.Um
bomcaminhoéseperguntarseaquelaextraç ãoqueestásendofeitaseráuti-
lizadaemmaisdeumaentidade,porexemplo,seéalgorealmentegenérico.
Mascomoregra,podemosseguirutilizandoosharedexampleeextrairpara
ummatcherapenasquandosentirmosnecessidade.
Umavezqueaprendemoscomocriarnossosprópriosmatchers,écomum
querermosencapsulardiversosdelesemumagemparafacilitarnossotraba-
lhoeaindacontribuircomacomunidade...mascalmaae!
Játemosdiversascoleçõesdematchersencapsuladasemgemsemantidas
pelacomunidade. Antesdecriarumnovo,émelhorverseoquevocêestá
pensandofazerjánãoexiste.Mesmosenãoexistirummatcher,émaisfácil
criá-loemumdestesprojetosdoquecriarumnovoprojetodozero.
6.4 O shoulda-matchers
Oshoulda-matchersfoiextraidodoshoulda,queéumametagemqueécom-
postadoshoulda-contextedoshoulda-matchers.Oshoulda-contextéutili-
zadoparaescrevertestesmaislegíveisno Test::Unit.Comestaextração,
podemosutilizarapenasosmatchers,queéoquerealmentenosinteressa.
Osmatchercriadospeloshoulda-matcherssãoparatestarmosfuncionalida-
descomunsdoRails.
Parainstalarmososhoulda-matchers,simplesmenteoadicionamosao
Gemfilenogrupodetesteserodamos $ bundle.
103

## Página 118

6.4. Oshoulda-matchers CasadoCódigo
group :test do
gem ’shoulda-matchers’
end
Vamosagoravalidaronossomodel Pokemon,quedevepossuirvalidação
depresençanoscampos nomee id_nacional. Paraisso,utilizaremoso
matcher validate_presence_of,querecebecomoparâmetroonomeda
colunadobancocujapresen çaestamosvalidando.
describe ’validações’ do
it { should validate_presence_of(:nome) }
end
Assim como o nosso matcher que criamos, o shoulda-matchers pos-
suiumaboadescriçãoepodemosoutilizarsemanecessidadededefinir
umadescriçãoaoteste. Diferentedomatcherquecriamosanteriormente,
o validate_presence_offuncionacomtodosostiposdedados,então
vamosvalidarqueanossacoluna id_nacionaldeveserpreenchidatam-
bém.
it { should validate_presence_of(:nome) }
it { should validate_presence_of(:id_nacional) }
Eparanossostestespassarem,simplesmenteadicionamosavalidaç ãode
presençanomodel.
class Pokemon < ActiveRecord::Base
validates :nome, :id_nacional, presence: true
end
Esteéapenasumcome çodoqueoshoulda-matchersécapaz. Vamos
continuaravalidaçãodonossomodelparavermosmaisdosseuspoderes.
104

## Página 119

CasadoCódigo Capítulo6. Copiarecolarnãoéumaop ção!
Matcherscomsuperpoderes
Nosso campo id_nacional não deve aceitar qualquer valor, ele
deve aceitar apenas valores inteiros e maiores que 0. Vamos pri-
meiro testar que ele aceita apenas numeros, para isso utilizamos o
validate_numericality_of
it { should validate_numericality_of(:id_nacional) }
Eparafazerotestepassarapenasadicionamosvalidaç ãodevaloresnu-
méricosutilizandooparâmetro numericality.
class Pokemon < ActiveRecord::Base
validates :nome, :id_nacional, presence: true
validates :id_nacional, numericality: true
end
Agoratemosquegarantirqueaceitamosapenasvaloresinteirosenão
qualquervalor. Oshoulda-matchersnosdáapossibilidadedeutilizarmé-
todos encadeados e ele já possui um método que podemos passar para
o matcher para garantir que aceitamos apenas valores inteiros o método
only_integer.
it { should validate_numericality_of(:id_nacional).only_integer}
Nonossomodel,paraotestepassar,simplesmenteadicionamosumhash
passandoaop çãodeapenasinteiro.
validates :id_nacional, numericality: { only_integer: true }
Parafinalizaravalidaçãodonosso id_nacional,temosquegaran-
tir que todo o valor seja acima de zero. Como você já deve imaginar,
podemosencadearmaisummétodoaliqueresolveonossoproblema, o
is_greater_than,querecebecomoparâmetroovalorqueomodeldeve
aceitaracimadeste.
it { should validate_numericality_of(:id_nacional).only_integer
.is_greater_than(0) }
105

## Página 120

6.4. Oshoulda-matchers CasadoCódigo
Eparaonossotestevoltarapassar,simplesmenteadicionamosachave
greater_thannonossomodel.
class Pokemon < ActiveRecord::Base
validates :nome, :id_nacional, presence: true
validates :id_nacional, numericality: {
only_integer: true, greater_than: 0 }
end
Comosepodever,temosumasintaxebemflexívelpararealizarosnossos
testes.ÉbomsemprefazermosoTDDmesmoquandoutilizamososmatchers
comofizemosanteriormente,poiscomousodematcherspodemosquerer
“agilizar”ascoisas,masvimosquemesmocomousodematchersépossível
fazermosTDD.
Parafinalizar,vamosorganizarosnossostestesseparandoporcontexto
cadaumadasvalidaçõesdoscampos.
describe ’validações’ do
it { should validate_presence_of(:nome) }
describe ’id_nacional’ do
it { should validate_presence_of(:id_nacional) }
it { should validate_numericality_of(:id_nacional).
only_integer.is_greater_than(0) }
end
end
Definindoosujeitonosmatchers
Nossomodel Pokemondeveexigirapresen çadocampoataque,noen-
tantoapenasquandoovalordacolunaaprovadofor true,ouseja,temos
umavalidaçãocondicional.Istoporquenãoqueremosqueumpokémonseja
aprovadoporenganoquandonãopossuiovalordoseuataque.
Utilizaroshoulda-matcherscomosujeitoimplícitocomofizemosanteri-
ormentenãoresolveránossoproblema.Teremoscomosujeitoumpokémon
106

## Página 121

CasadoCódigo Capítulo6. Copiarecolarnãoéumaop ção!
comtodososcampos nil,mastemosquedefinironossosujeitoedefiniro
valordacolunaaprovado.
Paraisso,iniciaremoscriandoumcontextodequandoopokémonestá
aprovadoe,nessecontexto,eledevevalidarapresen çadonome.
describe ’ataque’ do
context ’quando está aprovado’ do
subject do
Pokemon.new(aprovado: true )
end
it { should validate_presence_of(:ataque) }
end
end
Parafazeronossotestepassar,simplesmenteadicionamosavalidaç ãode
presençanonossomodel.
validates :ataque, presence: true
Testamosocasodequandoopokémonestáaprovado,agoratemosque
testarquandoelenãoestáaprovado.Paraisso,criamosumcontextoetesta-
mosquenãotemosvalidaçãodepresen çacasoopokémonnãotenhadefinido
oaprovadopara true.
describe ’ataque’ do
# ...
context ’quando não está aprovado’ do
subject do
Pokemon.new
end
it { should_not validate_presence_of(:ataque) }
end
end
107

## Página 122

6.5. Matchersdeterceiros CasadoCódigo
Aorodarmosnossoteste,elequebra,comooesperado. Paraelepassar,
simplesmentepassamosaop ção :ifcomovalor aprovado?,dadoqueo
ActiveRecordimplementaparanósestemétodoqueverificaseovalorestá
preenchidoounão.
validates :ataque, presence: true, if: :aprovado?
Assim,finalizamosanossaintroduçãoaoshoulda-matchers.Ecomose
podeveragoraficoubemmaisfácildetestaravalidaç ãodepresen çado
camponome,equeaidadeérealmenteuminteiropositivoemummodel
Usuario,queécasocomumemmuitasaplicações.
Ficaadicaparaconsultaradocumentaçãodoshoulda-mathcersparaver
osdemaismatchersdisponíveis. Masapenasparadeixarumgostinhode
queromais,látemosmatchersparatestarassociaçõesdoActiveRecord,di-
versosmatchersdevalidação,alémdosdecontrollerparatestarrenderização
delayouts,templatesematchersderotas. Semprequeestivertestandoalgo
comum,nãoseesque çadedarumaolhadanoshoulda-matchersparaverifi-
carsejánãoexisteummatcherparaoqueestátestando.
https://github.com/thoughtbot/shoulda-matchers
6.5 Matchers de terceiros
Oshoulda-matchersnãoéaúnicacole çãodematchers,temoscole çõesde
matchersparadiversostestescomunsquenossaaplicaç ãopossater.Vamos
apenasconheceralgunsdeles,dadoquetodosfuncionambemparecidocomo
oshoulda-matchers.Ficacomoexercícioutilizá-losnosprojetosemquefizer
sentido.
•email-spec:comoonomejádiz,ajuda-nosatestarose-mailsdoActi-
onMailerhttps://github.com/bmabey/email-spec.
•rspec-sidekiq:paraquandoestamosutilizandooSidekiq(ferramenta
de background job)https://github.com/philostler/rspec-sidekiq.
•mongoid-rspec:assimcomooshoulda-matchersnosdádiversosmat-
chersdoActiveRecord,omongoid-rspecnosoferecematcherspara
108

## Página 123

CasadoCódigo Capítulo6. Copiarecolarnãoéumaop ção!
quandoestamosutilizandooMongoid https://github.com/evansagge/
mongoid-rspec.
Estessãoapenasalguns.Quandoverqueestátestandoumacoisaqueé
bemcomumerepetitiva,valeapenaprocurarparaversenãoéalgoquejá
possuiumagemquefacilitaráonossotrabalho.
Alémdasgemsquesãocole çõesdematchers,temosgemsquejápossuem
osseusmatchers,comoéocasodoPaperclip. Porisso,ésemprebomlera
documentaçãodagemqueestamosusandoparanãoperdemosestasdicas.
Nenhummatchervairesolvertodososnossosproblemas.Aindateremos
quefazeronossoTDD.Opapeldomatcheréapenasnosfacilitaremtestes
repetitivos.Sendoassim,seaindanãosesentirconfortávelaorealizarTDD,
continuefazendooTDDparasódepoisutilizarestesmatchersdeterceiros,
dadoquebastantecoisaétestadaaoutilizarmososmatchers.
6.6 C onclusão
Vimosdiversasmaneirasdeevitarrepetiçãonosnossostestes:
• Extraímosnossostestesrepetidosparaumsharedexample;
• Utilizamossharedexamplesdinâmicos;
• Criamosonossoprópriomatcher;
• Melhoramosassaídasdonossomatcher;
• Conhecemososhoulda-matchers;
• Fomosapresentadosamaisalgunsmatchersdeterceiros.
Comopodemostestarvaloresnãodeterminísticos?Comofazerumteste
deumaclassequeutilizaoutraqueaindanemexiste? Ficaporaíqueno
próximocapítuloveremosbastantecoisalegalnousodemocksestubsque
nosajudamresolverestesproblemas.
109

## Página 125

Capítulo 7
O tal dos mocks e stubs
Nosso model Pokemon agora precisa retornar um valor para quando um 
ataque é crítico. Como estamos apenas no começo do projeto, o valor do 
nosso ataque crítico deve ser um valor aleatório entre 60 e 80. Mas como 
podemos testar algo que não possui um valor não determinístico? Afinal, em 
um momento o valor retornado pode ser 66 e no outro 75.
7.1 Conhecendo o stub
O RSpec já possui no seu core uma biblioteca de mocks, o rspec-mocks, que 
é exatamente o que precisamos quando queremos forjar a chamada de algum 
método.
Ant
esderealizarmosnossoprimeirousodostub,vamosprimeirodefinir
oRSpecparautilizarapenasasintaxede expectativaquandoestivermos

## Página 126

7.1. Conhecendoostub CasadoCódigo
fazendonossosmocks.Paraisso,utilizamosaconfiguraç ão mock_withno
nosso spec_helper.rb.
RSpec.configure do |config|
# ...
config.mock_with :rspec do |mocks|
mocks.syntax = :expect
end
end
ComoRSpecdevidamenteconfigurado,vamosaonossoprimeiroteste
utilizandostub,quenospermiteforjarachamadadealgummétodo.
Utilizandoostub
Vamoscomeçarotestedonossométodo Pokemon#ataque_critico.
Paraisso,criamosumcontextochamado #ataque_criticoedentrodele
criamosotestedovaloraleatório,testandoapenasqueovalordeveserigual
a75.
describe ’#ataque_critico’ do
it ’é um valor aleatório’ do
pokemon = Pokemon.new
expect(pokemon.ataque_critico).to eq(75)
end
end
Vamosagoraimplementaronossométodo ataque_critico.NoRuby
podemosutilizaraclasse Randomeseumétododeclasse rand,querecebe
umrangeenosretornaumvaloraleatóriodentrodaquelerange.Sendoassim,
podemospassarumrangeentre60e80,quenossoproblemaestáresolvido.
class Pokemon < ActiveRecord::Base
def ataque_critico
Random.rand(60..80)
end
end
112

## Página 127

CasadoCódigo Capítulo7. Otaldosmocksestubs
Vamosrodarostestes. Comoédeseesperar,ostestesquebram. Em
algummomentoelevaipassar,mastambémquebraráemmuitos,devidoà
dinâmicado Random. Nãopodemosterestetipodecomportamentoem
nossasuítedetestes,portanto,vamosagorautilizarostubpararesolvero
nossoproblema.
Oquequeremosagoraéforjarachamadadonossoobjetocolaborador,
o Random,eseumétodo .rand.Paraisso,utilizamoso allow,querecebe
aclasseouobjetoemqueiremosfazerostub. Emseguida,passamospara
ométodo receiveométodoquequeremosforjare,parafinalizar,ovalor
retornadoporestemétodocomousodo and_return.
it ’é um valor aleatório’ do
allow(Random).to receive(:rand).and_return(75)
pokemon = Pokemon.new
expect(pokemon.ataque_critico).to eq(75)
end
Agorasemprequerodarmosnossotesteovalorde Random.randserá
de75enossotestesemprepassará.
Asserçãodosparâmetros
Nossotestepassa,noentanto,seformoslánomodel Pokemonealterar-
mos Random.randparanãorecebernenhumparâmetroououtroparâme-
troqualquer,onossotestecontinuarápassando,oquenãoéoesperado.
Ao utilizarmos stub, temos a opção de chamar o método encadeado
with,quenospermitefazerumaasser çãonosparâmetrosquesãoesperados,
osqueométododevereceber.Paraisso,simplesmentepassamososparâme-
troscorretosdepoisdousodo receivecomo with.
it ’é um valor aleatório’ do
allow(random).to receive(:rand).with(60..80).and_return(75)
pokemon = pokemon.new
expect(pokemon.ataque_critico).to eq(75)
end
Agora se formos ao nosso model e alterarmos a chamada ao
Random.rand,otestefalhará,dadoqueachamadamudou.
113

## Página 128

7.2. Osdublês CasadoCódigo
WTF!Eunãotesteinada
Calmaaí!Oconceitodestubmuitasvezesnosdáasensaç ãodequenão
testamosnada,afinalestamosforjandoachamadadeummétodo.Massabe
quemtambémsãoforjadoresquevimosaqui?OWebMock,queforjachama-
dasHTTP,oTimecop,queforjaotempo,eo build_stubbeddoFactory-
Girl,queforjaumobjetoActiveRecord.Observequetodoselesforjamcola-
boradoresdenossosistema,nuncadevemosforjaroobjetotestado.Noteque
narealidadenãoforjamosonossométodo Pokemon#ataque_critico,
queéonossométodotestado,esimoseucolaboradorqueéo Random.rand.
Vamosagoraàsdicasdequandoutilizarstub.
• Quandooresultadodeumdosseuscolaboradoresnãoédeterminís-
tico;
• Apenasemcolaboradores,nuncanoobjeto(osujeito),doseuteste;
• Quandoocolaboradorfazumaoperaçãolenta,comoacessarumaAPI.
7.2 Os dublês
Temosemnossasmãosagoraatarefadecriarum Cardparaospokémons,
paraosusuáriosequalqueroutraentidadedonossosistema,desdequeela
implementeométodo to_presenter. Noentanto,aindanãofoiimple-
mentadonenhumdestesmétodos to_presenteremnenhumadessasen-
tidades,entãocomopodemostestarseonossocolaboradoraindanãoexiste?
Paraestescasos,existemosdublêsdoRSpec.
Ocontratoentreo CardPresentereocolaboradoréqueocolaborador
deveimplementarométodo to_presenterqueretorneumhashcoma
chavesendooatributoquequerexibirnocardeovalordohashcomoovalor
paraaqueleatributo.
Vamos começar criando o nosso teste para o método
CardPresenter#show. Iniciamos instanciando umCardPresenter
passando um objeto e fazemos a nossa expectativa de que ao chamar o
método#showdevemosterumparágrafoparacadaatributo.
114

## Página 129

CasadoCódigo Capítulo7. Otaldosmocksestubs
describe ’#show’ do
it ’retorna um paragrafo por chave’ do
card_presenter = CardPresenter.new(objeto)
expect(card_presenter.show).
to eq(%{<p>nome: Mauro</p><p>idade: 24</p>})
end
end
Agoravamoscriaronossodublê,o objeto.Paraisso,utilizamosomé-
todo doubleepassamosparaeleumadescrição.Éimportantepassarades-
criçãopoisissonosajudanasaídadonossoteste.
it ’retorna um paragrafo por chave’ do
objeto = double(’Um objeto’)
card_presenter = CardPresenter.new(objeto)
expect(card_presenter.show).
to eq(%{<p>nome: Mauro</p><p>idade: 24</p>})
end
Neste momento já estamos passando o nosso dublê para o
CardPresenter, porém o nosso dublê não implementa o método
to_presenter. Lembra dos stubs? Então vamos agora criar um stub
paraonossodublê,utilizandoo allow,mascomadiferen çadequeagora
estamospassandoumobjeto,onossodublê,enãoumaclassecomofizemos
anteriormente.
it ’retorna um paragrafo por chave’ do
objeto = double(’Um objeto’)
to_presenter = { nome: ’Mauro’, idade: 24 }
allow(objeto).to receive(:to_presenter).
and_return(to_presenter)
card_presenter = CardPresenter.new(objeto)
expect(card_presenter.show).
to eq(%{<p>nome: Mauro</p><p>idade: 24</p>})
end
Agoratemosonossocenáriomontado. Temosocolaborador,queéo
objeto,eonossosujeito,o CardPresenter,queconseguefazersuaas-
serção.Vamosagoraescreveranossaclasse CardPresenter.Começamos
115

## Página 130

7.2. Osdublês CasadoCódigo
criandouminitializerquecriaum @objeto. Definimostambémoacesso
aesteobjetoparaapenasleituradentrodo CardPresenterutilizandoo
attr_reader.
class CardPresenter
def initialize(objeto)
@objeto = objeto
end
private
attr_reader :objeto
end
Eparafinalizar,criamosométodo CardPresenter#showquesimples-
menteiteraemcadaumdosvaloresdohashdo to_presenteremontaum
parágrafo.
def show
retorno = ’’
objeto.to_presenter.each do |atributo, valor|
retorno += "<p>#{atributo}: #{valor}</p>"
end
retorno
end
Aorodarmosonossotestenestemomento,elepassará. Issoporqueo
nossodublêimplementaométodo to_presenterretornandoumhash.
Comovimos,umdublêéumobjetoquesimulaoutrosobjetosequepode
terseucomportamentoalteradodeformacontroladacomousodestub.
Parafinalizaronossoteste,vamosapenasfazerumrefatoraç ãoparadei-
xarmaisclaroopapeldecadaum.Movemosonossocolaboradorparaum
let,definimosonossosujeitoutilizandoo subject,utilizamosobloco
beforeparafazermosonossostube,parafinalizar,fazemosonossoteste.
describe ’#show’ do
116

## Página 131

CasadoCódigo Capítulo7. Otaldosmocksestubs
let(:objeto) do
double(’Um objeto’)
end
subject(:card_presenter) do
CardPresenter.new(objeto)
end
before do
to_presenter = { nome: ’Mauro’, idade: 24 }
allow(objeto).to receive(:to_presenter).
and_return(to_presenter)
end
it ’retorna um paragrafo por chave’ do
expect(card_presenter.show).
to eq(%{<p>nome: Mauro</p><p>idade: 24</p>})
end
end
Comopodever,ficamaisclarooqueestáacontecendo,issodevidoàex-
pressividadequeoRSpecnosfornececomsuaDSL.
Ossuperdublês
Nossotestefunciona,noentanto,nadagarantequeelefuncionacomo
Pokemon,dadoqueutilizamosumdublêcomoobjeto.Porém,podemosuti-
lizaro instance_double,quecriaumdublêutilizandoumainstânciade
umobjetocomobase.
Parafazermosoisso,criaremosumnovocontextoe,nadefiniç ãodo
nossoobjeto,utilizamos instance_double.
context ’Pokemon’ do
let(:objeto) do
instance_double(Pokemon)
end
it ’retorna um paragrafo por chave’ do
117

## Página 132

7.2. Osdublês CasadoCódigo
expect(card_presenter.show).
to eq(%{<p>nome: Mauro</p><p>idade: 24</p>})
end
end
Aorodarmosonossoteste,elequebra,dadoqueonossomodel Pokemon
nãoimplementaométodo #to_presenter. Parafazermosonossoteste
passar,simplesmentecriamosométodo #to_presentervazio.
class Pokemon < ActiveRecord::Base
# ...
def to_presenter
end
end
Agoraonossotestepassa.Issoporqueestamosfazendoumstubnoob-
jeto,nonossobloco beforeemquedefinimosonomeeidade. Nãofaz
sentidoopokémonterosmeusdados,masvamosdeixareleassimporen-
quanto.
Além do instance_double, o RSpec também implementa o
object_double,quenospermitepassarumainstânciadeumobjeto.
object_double(Pokemon.new(nome: ’Charizard’))
O object_doubleéútilparaquandoprecisamosterumestadodefi-
nidoemnossoobjeto,comonoexemploanterioremquepassamosonome.
Dublêsemumalinha
Quandonossosdublêsdevemretornarumsimplesvalornachamadade
ummétodo,podemosfazerostubdiretonodublêsemanecessidadedo
allowedo and_return.
Vamosalterarostubdonossopokémonpararetornarumhashcomo
nomedopokémondefinido. Paraisso,passamosumhashcomovalorque
desejamosdefinir,nonossocasoumhashcomachave nome.
context ’Pokemon’ do
118

## Página 133

CasadoCódigo Capítulo7. Otaldosmocksestubs
let(:objeto) do
instance_double(Pokemon, to_presenter: {nome: ’Charizard’})
end
it ’retorna um paragrafo por chave’ do
expect(card_presenter.show).to eq(%{<p>nome: Charizard</p>})
end
end
Valelembrarquequandotivermoso Pokemon#to_presenterére-
comendadoremovermosousododublêedostubeusarumainstânciado
Pokemon,issoporqueagoraonossocolaboradorjáfoicriado.
Resumindoosdublês
Vamosagoraaoresumodedublês.
• Utilizequandooseucolaboradoraindanãofoiimplementado;
• Utilizeparadescobrirsuainterface. Nocomeçoditamosqueiríamos
criaro #to_presenter,noentantoelepoderiatersaídodonosso
TDDsimplesmentepassandoocolaboradore,emseguida,pensaría-
mosemumnomeparaométodo;
• Utilize sempre que possível os super dublês como o
instance_double e o object_double, dado que assim ga-
rantimosqueométodopelomenosfoicriadonocolaborador;
• Removaodublêtrocando-oporumainstânciadocolaborador,quando
ocolaboradorforcriadoeimplementarosmétodosnecessários.
7.3 Expectativ as em mensagens
Jáfizemosanossaclasse CriadorPokemonque,comooseunomediz,é
responsávelporcriarosnossospokémons.Vamosagoracriarumesbo çodo
nosso AtualizadorPokemon. Paraisso,criamosum initializeque
recebeumpokémoneummétodo update!,responsávelporatualizaro
119

## Página 134

7.3. Expectativasemmensagens CasadoCódigo
pokémon.Nãoentraremosemdetalhedeimplementaçãodessaclasse,maso
quemétodo update!devefazeré:
• AcessaraAPIemhttp://pokeapi.co/api/v1/pokemon/6emque6éoid
nacionaldopokémonqueforpassadoparaoobjetonasuacriaç ão;
• Pegartodasasinformaçõesdopokémoneatualizaroquefoipassado
comoparâmetronoinitialize.
Ficaoexercíciodeimplementarestaclasse. Parasimularalentidãodo
acessoaredecolocaremosapenasum sleepparaométodo update!ser
lentoeeledurar10segundospararealizaraoperaç ão.
class AtualizadorPokemon
def initialize(pokemon)
@pokemon = pokemon
end
def update!
sleep 10
end
private
attr_reader :pokemon
end
Com isso temos a nossa classeAtualizadorPokemon. Queremos
quesejapossívelousuáriosimplesmenteclicaremumbotãoeatualizar
o pokémon. Como estamos em uma app rails, vamos criar uma action
pokemons#update. Vamoscomeçaronossotestedestaaction. Paraisso,
criamosumcontextoesimplesmentechamamosanossaactionpassandoum
pokémonjácriado.
describe "PUT ’update’" do
let!(:pokemon) do
120

## Página 135

CasadoCódigo Capítulo7. Otaldosmocksestubs
Pokemon.create!
end
it ’atualiza o Pokemon’ do
put :update, id: pokemon
end
end
end
Aindanãofizemosnenhumaasser ção,ouseja,nãotestamosnada.Como
oqueélentono AtualizadorPokemonéoacessoàrede,vimosquepode-
mosutilizaroVCR 2.6.Masvamosdiferenciarumpoucoeutilizaras message
expectations.
Paraisso,utilizamosométodo expect,emquepassamosanossaclasse
AtualizadorPokemon,eo receive,quedizqualmétodoeladevereceber,
nocasoo new.
it ’atualiza o Pokemon’ do
expect(AtualizadorPokemon).to receive(:new)
put :update, id: pokemon
end
Rodamosonossotesteeelequebra.Paraofazermospassar,chamamoso
nosso AtualizadorPokemoncomoéesperadononossoteste.
class PokemonsController < ApplicationController
def update
AtualizadorPokemon.new
redirect_to pokemons_path
end
end
Rodamosnovamente,enossotestepassa. Noentanto,testamosapenas
queeleinstanciouo AtualizadorPokemon. Nãotestamosaindaqueele
recebeuoobjetocorreto,nemquechamouométodo update!.
Vamoscontinuareagoratestarqueelerecebeoobjetocorreto,onosso
pokémonqueestáno let,queépassadoparaocontroller. Paraissouti-
lizamosométodo with,quenosdápossibilidadededefinirosparâmetros
esperados.
121

## Página 136

7.3. Expectativasemmensagens CasadoCódigo
it ’atualiza o Pokemon’ do
expect(AtualizadorPokemon).to receive(:new).with(pokemon)
put :update, id: pokemon
end
Rodamosnossotestee,nomomento,eleestáquebrado.Vamosaocon-
trollerparaarrumar.Paraisso,passamosanossainstânciadepokémonpara
o AtualizadorPokemon.
def update
pokemon = Pokemon.find(params[:id])
AtualizadorPokemon.new(pokemon)
redirect_to pokemons_path
end
Nossostestesagorapassameestamoscadavezmaispróximosdefinalizá-
los.Faltaagoratestarmosqueo AtualizadorPokemonrecebeuométodo
update!.
Paratestarmosque AtualizadorPokemonrecebeuumoutrométodo,
teremosqueutilizarosnossosdublês. Primeiro, definimosumdublêdo
AtualizadorPokemone,emseguida,utilizamoso and_returnaofinali-
zaranossachamadado new,garantindoqueoretornosejaonossodublê.
it ’atualiza o Pokemon’ do
atualizador_pokemon = double(AtualizadorPokemon)
expect(AtualizadorPokemon).to receive(:new).with(pokemon)
.and_return(atualizador_pokemon)
put :update, id: pokemon
end
Agoratemosocontroledoretornodo new,queéonossodublê.Faze-
mosmaisumaexpectativa,agoranonossodublê,verificandoseelerecebeu
ométodocorreto, update!.
it ’atualiza o Pokemon’ do
atualizador_pokemon = double(AtualizadorPokemon)
expect(AtualizadorPokemon).to receive(:new).with(pokemon)
.and_return(atualizador_pokemon)
expect(atualizador_pokemon).to receive(:update!)
122

## Página 137

CasadoCódigo Capítulo7. Otaldosmocksestubs
put :update, id: pokemon
end
Nossoteste,comoesperado,estáquebrado. Parafazê-lopassar,chama-
mosométodo update!nonosso AtualizadorPokemon.
def update
pokemon = Pokemon.find(params[:id])
AtualizadorPokemon.new(pokemon).update!
redirect_to pokemons_path
end
Agorasimnossotesteestácompleto.Estamostestandoqueaclasseéins-
tanciada,querecebeosparâmetroscorretosechamaométodocorreto.Ace-
rejanotopodobolo:vamostrocaronosso doublepor instance_double
paragarantirqueaclassedequeestamosfazendoasser çãoaquirealmenteim-
plementaométodoqueestamostestando.
it ’atualiza o Pokemon’ do
atualizador_pokemon = instance_double(AtualizadorPokemon)
expect(AtualizadorPokemon).to receive(:new).with(pokemon)
.and_return(atualizador_pokemon)
expect(atualizador_pokemon).to receive(:update!)
put :update, id: pokemon
end
Percebaque,quandoestamostestandocom message expectations,nossa
estruturadetestesmuda: emvezdopadrão setup,exercício,verificaçãoe
teardown,temoso setup,verificação,exercícioe teardown. Tenhaissoem
menteparaquandorealizartestesquefazemexpectativasemmensagens.
Resumindoasmessageexpectations
Vamosagoraaoresumodas message expectations.
• Utilizeparaverificarachamadacorretadeumcolaborador;
• Alémdetestarachamadaaométodo,testeseusargumentos;
• Testeunitariamenteoseucolaborador.
123

## Página 138

7.4. Matchersdeargumentos CasadoCódigo
7.4 Matchers de argumentos
Nosnossosexemplosanteriores,utilizamosométodo withque,alémde
recebervaloresexplícitos,eleaceitaalgunsmatchers.Vamosdarumaolhada
neles.
Quandooqueimportaéapresenç a
Temosumcolaboradordonossosistema,o FacebookPost,quefaz
umapostagemnofacebookutilizandoométodo criar.Elejápossuiuma
mensagempadrão,entãononossotestequeremosapenasqueocolabora-
dorsejaexecutadosemnenhumparâmetro.Paraisso,utilizamosomatcher
no_args.
expect(FacebookPost).to receive(:criar).with(no_args)
Emoutrocontexto, queremosqueeletenharecebidoumamensagem
qualquercomoparâmetroeparaissoutilizamosomatcher anything.
expect(FacebookPost).to receive(:criar).with(anything)
Eparaquandooparâmetropodeestarpresenteounão, utilizamoso
any_args.
expect(FacebookPost).to receive(:criar).with(any_args)
Assimnossotestepassasehouverparâmetroounão.
Comexpressãoregular
No FacebookPost,temosquegarantirquesempretenhamosmencio-
nadootermo“pokémon”namensagem.Paraisso,utilizaremosumaexpres-
sãoregular.
expect(FacebookPost).to receive(:criar).with(/pokémon/)
Comopodever,aexpressãoregularéescritadomesmomodoquefaze-
mosemRubysemanecessidadedeummatcherespecífico.
124

## Página 139

CasadoCódigo Capítulo7. Otaldosmocksestubs
Quandooparamêtroéumhash
No AtualizadorPokemon,esperamosqueonossopokémonatualize
oseuataq
ue.Então,podemostestarqueelerecebeo update_attributes
comoseunovoataque. Paranãopassarmosohashcompleto,utilizamoso
hash_including,quenospermitedefinirapenasumapartedohash.
expect(pokemon).to receive(:update_attributes)
.
with(hash_including(ataque:
 12))
Noentanto,nãoqueremosqueelemudeonomedonossopokémon.Para
tal,utilizamoso hash_not_including,quenospermitedefinirapartedo
hashque
nãoqueremospresente.
expect(pokemon).to receive(:update_attributes)
.with(hash_not_including(:nome))
Ambososm
atchersnospermitemdefinirapenasachaveouchaveevalor,
oquenosdábastanteversatilidade.
Quandooquenosimportaéaclasse
Utilizandonosso CardPresenter,estamosesperandoquenaexibição
depokémo
nselerecebaapenasumainstânciadepokémon,nãoimportaqual
pokémon.Paraescreverestetesteutilizamosomatcher instance_of.
expect(subject).to receive(:new)
.with(instance_of(Pokemon))
Quandonãonosimportaoobjetoexato,massimqueestesejaapenas
umainstânciadeumadadaclasse,utilizamosomatcher instance_of.
No entan
to, na exibição do treinador pokémon utilizamos o
CardPresenter para exibir, além dos pokémon, o card dos usuá-
rios. Então, temos que verificar se o parâmetro recebido é um objeto
ActiveRecord::Base,eparaissoutilizamoso kind_of.
expect(subject).to receive(:new)
.
with(kind_of(ActiveRecord::Base))
125

## Página 140

7.5. Umpoucomaissobrestubs,dublêsemessageexpectations CasadoCódigo
Agora nosso objeto pode não ser mais um que herda de
ActiveRecord::Base,entãotemosquegarantirque CardPresenter
receba um objeto que implemente o métodoto_presenter, não nos
importadequalclasseeleseja.Paraissoutilizamoso duck_type.
expect(subject).to receive(:new).with(duck_type(:to_presenter))
Alémdosmatchersquevimos,temosaindao boolean,quegaranteque
oparâmetroétrueou false.Eo array_including,quefuncionacomo
o hash_includingrecebendoosvaloresdeumarray.
Outra funcionalidade legal no uso do with é que é possível
passarmos mais de um argumento, assim podemos passar matchers
junto de valores explícitos como, por exemplo,with(anything, 12,
duck_type(:save)).
7.5 Um pouco mais sobre stubs, dublês e message
expectations
Vamosagoraaalgumasdicasparaquandoestamosutilizandoosstubs,dublês
emessageexpectations.
Encadeamentodemétodos
Os escopos do Active Record nos fornecem uma interface fluente,
de modo que podemos fazerPokemon.aprovados.recem_criados
com o que aprendemos até aqui. Se precisássemos fazer um stub do
recem_criados,nestachamadateríamosquedefinirantesoretornode
aprovadoscomumdublê,assimcomofizemosnonossoexemplodeexpec-
tativademensagens 7.3.
Paraquandotemosquefazerstubdeumachamadaamétodosconsecu-
tivos,podemosutilizaro receive_message_chain. Paraissosimples-
mentepassamososnomesdosmétodosdosquaisestamosfazendoostub.
allow(Pokemon).
to receive_message_chain(:aprovados, :recem_criados).
and_return([])
126

## Página 141

CasadoCódigo Capítulo7. Otaldosmocksestubs
Comopodever,estachamadaamétodosencadeadosnãolevaemcon-
sideraçãoosparâmetros. Seforimportantenoseutestequeosparâmetros
sejamcorretos,utilizeomesmoconceitoquefizemosnaexpectativademen-
sagenscomousodeumdublê.
Alémdefuncionarcomo allowparacriarmosumstub,funcionacom
o expectparafazermosumaasser ção.
Quandoascoisasdãoerrado
EmumaAPItemosumateladehistórico,eparamontá-loéutilizadoo
User Agentenviadonoheader. AAPIcontinuafuncionandosemoheader;
eleénecessárioapenasparavermosestatísticasdeuso.Vamosfazerumteste
paraenviaroUserAgent.
Vamoscomeçarcomonossotestefazendoumaexpectativadequeo
Net::HTTPrecebeosparâmetroscorretosnoheader.
it ’envia o user agent’ do
expect(Net::HTTP).to receive(:get).with(anything,
{ ’User-Agent’ => ’RSpec’ })
acessa_api
end
Ao rodarmos nosso teste, recebemos o seguinte erro:undefined
method 'strip'for nil:NilClass. Nossométodoatualqueacessaa
APIpossuioseguintecódigo.
resposta = Net::HTTP.get(endpoint, { ’User-Agent’ => ’RSpec’ })
resposta.strip
Comopodever,depoisdepegarmosaresposta,estamosutilizandoo
strippararemoverespaçosindesejáveis.
O nosso erro undefined method 'strip'for nil:NilClass
ocorrepois,quandoestamosutilizandostuboufazendoexpectativanasmen-
sagens,ométodonuncaéchamado,eelesempreretorna nileestenãoim-
plementaométodo strip.
No nosso exemplo podemos resolver simplesmente retornando uma
stringvazia.
127

## Página 142

7.5. Umpoucomaissobrestubs,dublêsemessageexpectations CasadoCódigo
expect(Net::HTTP).to receive(:get).with(anything,
{ ’User-Agent’ => ’RSpec’ }).and_return(’’)
Issoresolveonossoproblema,masalémdo strip,anossarespostapode
estarchamandodiversosmétodosealgunspodemnãoserimplementados
pelastring.
Pararesolverpodemosretornarumdublêparaanossaresposta.
resposta = double(’resposta HTTP’)
expect(Net::HTTP).to receive(:get).with(anything,
{ ’User-Agent’ => ’RSpec’ }).and_return(resposta)
Noentanto,agoraestamosrecebendooutroerro: Double "resposta
HTTP"received unexpected message :strip with (no args),
ouseja,onossodublênãoimplementao strip.Podemosfazerostubdeste
edeNoutrosmétodos,porémseriaumprocessomuitochatoedeixariao
setupdonossotestebemcomplexo.Nesteteste,nãonosimportamoscomas
demaischamadasdosmétodosem resposta,estessãotestadosemoutros
testes. Oúnicoobjetivoquetemosaquiétestarseoheaderfoienviado
corretamente.Entãopodemosdizerqueonossodublêéum null object,isto
é,elerespondeaqualquermétodo.
resposta = double(’resposta HTTP’).as_null_object
expect(Net::HTTP).to receive(:get).with(anything,
{ ’User-Agent’ => ’RSpec’ }).and_return(resposta)
Agoranossostestespassam. Parafinalizar, podemosutilizaraindao
and_call_original,querealizaachamadadométodoretornandooseu
valor.Assimpodemosremoverousododublê.
expect(Net::HTTP).to receive(:get).with(anything,
{ ’User-Agent’ => ’RSpec’ }).and_call_original
Valelembrarqueagoraestamosfazendoarequisiç ãoHTTP,entãoébom
utilizarmosoVCRnestecaso.
Adicaé:iniciecomumsimplesvalorcomoretorno,ecasoencontrepro-
blemasutilizedodublêcomo null object;casoométodotestadonãosejacus-
tosodeserexecutado,utilizeo and_call_original.
128

## Página 143

CasadoCódigo Capítulo7. Otaldosmocksestubs
7.6 Mockar ou não mockar?
Comopodemosver,ousode message expectations,dublêsestubaumentao
nossoacoplamento,dadoqueseaassinaturadeummétodomudar,porexem-
plo,teremosquealterarostestesparaesteagorarefletirestanovachamada.
Outropontoquetemosquelevaremconsideraç ãoaoutilizarmosestes
recursoséquandoestácomplicadodefazeronossocenário,comoquando
estamoscriandodiversosdublêsefazendostubdediversosmétodos.Temos
queespecificarapenasonecessárioparaonossoexemplopassare,seainda
assimissoformuitacoisa,provavelmentenossaclasse/métodoestáfazendo
coisademaiseclamandoporumrefactoring.
Lembre-sedequeémaiscomplicadoparauminicianteentendertestes
utilizandodemocksdoqueaabordagemclássica,entãopensenoseutime
antesdecome çarautilizarestaabordagem.Vejasetodosestãoconfortáveis
eutilize-aapenasquandofornecessária.
Temosestasduasescolas:aclássicaeademocks.Pessoalmente,euuti-
lizoaabordagemclássicacomumpouquinhodemock.Utilizomocksbasi-
camentequandoalgumcolaboradormeu,criadopormim,necessitaserexe-
cutado,como,nonossoexemplo,o AtualizadorPokemonem message ex-
pectations.Issoporqueaabordagemclássicamedámaiorconfian ça.
7.7 Conclusão
• Conhecemosostubparaforjaroretornodenossosmétodos;
• Vimosquedevemosforjarapenasnosnossoscolaboradores;
• Utilizamososdublêsquandoaindanãotínhamosonossocolaborador
criado;
• Conhecemosossuperdublêsquenosdãoumamaiorconfiança;
• Fizemosasserçãonachamadademétodosutilizandoas message expec-
tations;
• Conhecemosdiversosmatchersdeargumentos;
129

## Página 144

7.7. Conclusão CasadoCódigo
• Utilizamosoencadeamentodemétodos;
• Vimosqueàsvezesosmockspodemsairdotrilho;
• Discutimosumpoucosobreestaabordagemaoserealizarostestes.
Fiqueporaí,quenopróximocapítuloveremosquetemosmodosdefazer
debugalémdo putsecomomelhoraranossaexperiênciaenquantoestamos
nonossoconsole. Éumcapítulobemcurtinhoemaistranquilo. Elenãoé
100%relacionadocomtestes,masquemnuncaescreveuum putsprafazer
debugnostestes?
130

## Página 145

Capítulo8
Nãodebugamoscomputs,certo?
Quantasvezesjánosdeparamoscomalgoassimnomeiodenossocódigo:
puts ’oi’
Podeserumoi,umpalavrão,qualquerpalavra,ouaindaumavariáveldo
nossocódigo. Normalmentefazemosissoquandoqueremossabersenosso
códigopassouporumdeterminadométodooucondiç ão,eaindaquando
queremossaberovalordeumavariávelemtalmomentodeexecuç ão.Mas
seráquenãotemosummodomelhordefazerisso?
Comovocêjápode,perceberestamosfalandodedebug.Dadoquepassa-
mos60%donossotempofazendodebug,ébomdarmosumaaten çãoaissoe
termosumaformamaisprofessionaldoqueo puts.Pessoalmente,quando
estoutestandoalgoquedependedeumagemquenuncauseiouumaapique
desconheço,façomeutesteenquantovoudebugandoofuncionamentodetal
api.

## Página 146

8.1. Porummelhorconsole CasadoCódigo
8.1 Por um melhor console
Antesdefalarmossobredebug,vamosantesdarumupgradeemcomoo
nossoconsoleexibeasinformações,oquevainosajudarmuitonodebug.
NoRuby,écomumutilizarmosbastanteonossoconsole,sejaparaini-
ciarmosoRails,rodartestes,excutarmos rake tasksetc.Tambémutilizamos
oconsoledopróprioRailsparadarmosumaolhadanosnossosobjetoscom
um rails c. Noentanto,vamosdarumaolhadaemcomoéexibidoum
objetop
aranósnoconsoledoRails.Paraisso,vamossimplesmentedaruma
olhadaemumainstânciadeumpokémonqualquer.
1.1
.0 :001 > pokemon
=> #<Pokemon id: 1, id_nacional: nil, nome: nil,
ataque: nil, defesa: nil, created_at: "2015-04-04 22:11:22", 
updated_at: "2015-04-04 21:11:23">
Comosepodever,aexibiçãoébemconfusa:sãoexibidostodososcam-
posemapenasumalinha(nonossoexemplo,aquebradelinhaéparase
adequaraolivro)enãotemoscoresparanosajudar.Sejáestáconfusocom
umsimplesobjeto,imagineemummodelocommaiscampos!
OAwesomePrint
OAwesomePrintéumagemquenosajudanatarefadeexibirnossosob-
jetosRubycommelhorformatação.Parainstalar,simplesmenteadicionamos
aonossogemfileo awesome_printeexecutamos $ bundle install.
group :development, :test do
# ...
gem ’awesome_print’
end
Parafinalizarejátermosaexibiç ãodoAwesomePrintporpadrãono
nossoirb
,criamosumarquivo .irbrcnonossohomecomoseguintecon-
teúdo:
require "awesome_print"
AwesomePrint.irb!
132

## Página 147

CasadoCódigo Capítulo8. Nãodebugamoscomputs,certo?
Vamosvoltarparaonossoconsoleagoraeexibiromesmoobjeto.
1.1.0 :001 > pokemon
#<Pokemon:0x000001049cf8d8> {
:id => 1,
:id_nacional => nil,
:nome => nil,
:ataque => nil,
:defesa => nil,
:created_at => Mon, 04 Apr 2015 22:11:22 BRT 
-03:00, :updated_at => Mon, 04 Apr 2015 22:11:23 BRT -03:00
}
Comosepodever,agoraestábemmaisclaroovalordecadaumdosatri-
butosdonossomodelo,alémdetermoscoresquefacilitamemuitoonosso
entendimento.
8.2 Conhecendo o Pry
OPrynãoéapenasumdebug,massimumdebugbombado.Porhora,vamos
começarapenasoinstalando.Paraisso,adicionamoso pry-railsnonosso
Gemfile,quenosforneceossuperpoderesdopryemumconsolerailse
executa
mos $ bundle install.
group :development, :test do
# ...
gem ’pry-rails’
end
Nãoquerem
osperderanossaformataçãodoAwesomePrinte,paraisso,
criamosumarquivo .pryrcnonossodiretóriohomeeadicionamosasse-
guinteslinhas:
require "awesome_print"
AwesomePrint.pry!
Assim,temosoAwesomePrintintegradodiretocomopry.Masvamos
agoradarumaolhadanestepry.
133

## Página 148

8.2. ConhecendooPry CasadoCódigo
Documentaçãoaoseualcance
Quandocriamosonosso CriadorPokemon,utilizamoso Net::HTTP,
mascomopodemossaberquaissãoosmétodos,qualéassinaturadestesmé-
todosetc.?PodemosconseguirestainformaçãoacessandoaAPIdoRubypelo
browser,massejáconseguíssemostodasestasinformaçõesdiretopelocon-
sole?Paraisso,oPrynosofereceocomando lsquelistatodososmétodos
deumaclasseouobjeto.
ls Net::HTTP
Comoresposta,teremososmétodos,atributosedemaisinformaçõesda
classe.Vejaumtrechodaresposta.
#<Class:Net::HTTP>#methods:
Proxy get_print
default_port get_response
get http_default_port
Comosepodever,anossaclasse Net::HTTPimplementaométodoget,
queébemprovavelseroqueprecisamosquandoqueremosfazerumare-
quisição get.Entãoagoravamoslerasuadocumentaç ãoparasabercomo
utilizá-lo,issoaindadentrodoconsole,pormeiodocomando ?
? Net::HTTP#get
Quenosfornececomorespostaamesmadocumentaç ãoqueteríamosao
acessaraAPIdoRuby.Vamosaumpequenotrecho:
From: /path/ruby-2.1.0/lib/ruby/2.1.0/net/http.rb @ line 1089:
Owner: Net::HTTP
Visibility: public
Signature: get(path, initheader=?, dest=?, &block)
Number of lines: 37
Retrieves data from path on the connected-to host which may be an
absolute path String or a URI to extract the path from.
Ocomando ?tambémpodeseracessadoatravésdo show-doc.Como
sepodever,émuitoutil,poisnãoprecisamossairdonossoterminalpara
acessaradocumentação.
134

## Página 149

CasadoCódigo Capítulo8. Nãodebugamoscomputs,certo?
Podemos ainda ir além e ver a implementação de um dado método ou 
classe. Para isso, utilizamos o comando $.
$ Net::HTTP#get
Isso nos retorna à implementação do método get da classe Net::HTTP. 
Vamos a um trecho.
From: /path/ruby-2.1.0/lib/ruby/2.1.0/net/http.rb @ line 1122: 
Owner: Net::HTTP
Visibility: public
Number of lines: 8
def get(path, initheader = {}, dest = nil, &block)
# :yield: +body_segment+
O comando $ também pode ser acessado através do comando 
show-source.
Conseguimos acessar bastante documentação diretamente do nosso con-
sole sem a necessidade de sairmos do terminal, o que facilita em muito o nosso 
desenvolvimento.
Para finalizarmos a nossa sessão do Pry podemos utilizar um < Ctrl> + 
d ou com
 o comando exit.
Utilizando o Pry em tempo de execução
Agora vamos ver o que para mim  é a melhor funcionalidade do Pry, que 
a possibilidade de utilizar o Pry em tempo de execução. Vamos alterar o 
CriadorPokemon e c
hamar o Pry com o binding.pry.
def cria_info
binding.pry
resposta = Ne
t::HTTP.get(endpoint)
@info = JSON
.parse(resposta)
end
Agoravamosrodaronossoteste.Deparamo-noscomaseguintemensa-
gemnoconsole:
135

## Página 150

8.2. ConhecendooPry CasadoCódigo
From: /path/criador_pokemon.rb @ line 21
CriadorPokemon#cria_info:
20: def cria_info
=> 21: binding.pry
22: resposta = Net::HTTP.get(endpoint)
23: @info = JSON.parse(resposta)
24: end
[1] pry(#<CriadorPokemon>)>
Percebaquequandootesteatingeométodo cria_infoeleseráparado
enoslevaráaoconsoledoPry.Ok,maseaí?TemosumconsoleRubyentão
podemosrodardiversoscomandosquedesejamos,inclusiveosdopróprio
Pryquevimosanteriormente.
Observequenoconsoleéexibidoocontextoemqueestamos.Nonosso
caso,éo CriadorPokemon.Seutilizamoso lseosdemaiscomandosque
oPrynosfornece,veremososmétodosevariáveisdoobjetoatual,ousejado
nosso CriadorPokemon.
Comoestamosemumambientededebug,vamosrodaralinha22e23,
podemoscopiarecolar...éissonãoélegalné?Então,paranãoprecisarfazer
isso,oPrynosforneceocomando play -l,queaceitacomoparêmetroum
númeroou range.Vamospassarumrangede22a23.
play -l 22..23
Assimexecutamosas2linhasumaseguidadaoutra. Comoresultado
seráexibidoohashgeradopelo JSON.parse. Agoraeuqueroverovalor
davariável...équalonomedavariável?ParanosajudarcomissooPrynos
forneceométodo whereamiquenosretornaparaopontoondedefinimos
onosso binding.pry.
Agoraqueestamosdevoltaedescobrimosqueonomedavariávelquear-
mazenamosovalordo JSON.parsefoi @info,vamosdarumaolhadanela.
Podemossimplesmentechama-ládiretamentecom @info,masvamosfazer
diferente:vamostrocaronossocontexto. Paraisso,utilizamosocomando
cdseguidodavariávelqueentraremos,nonossocaso @info.
136

## Página 151

CasadoCódigo Capítulo8. Nãodebugamoscomputs,certo?
cd @info
Seobservarmosnoconsole,veremosqueonossocontextomudouagora
para #<Hash>):1emvezdo #<CriadorPokemon>.Ecomovocêjádeve
imaginar,agorapodemosacessaroscomandosdoPrynonossocontextoas-
simcomoqualquermétododoHash,comoporexemplo keys,semane-
cessidadedechamaroobjeto,afinalagoraestamosnocontextodopróprio
objeto.
Paravoltarmosparaonossocontextopai,simplesmenteexecutamoso
comando cd ...
Aultimasaídaquetivemosnoconsole,foiachamadadométodo keys.
Podemosacessaraúltimasaídaatravésdavariável _,podemospassá-lacomo
parâmetroeexecutarqualquermétodo,porexemplo _[0].
Atéaquijádigitamosdiversoscomandosetivemosváriassaídas.Todas
essasentradasesaídaspodemseracessadasnasváriaveis _in_e _out_,
respectivamente. Alémdisso,podemosutilizardocomando <Ctrl> + r
pararealizarumabuscaenquantocome çamosdigitarumcomando.
Eunãomencioneiaqui,masquandoestiverrealizandoosseustestesverá
queoPrynosfornecebastantescoresenquantoestamosutilizandoseusco-
mandos.
Eupessoalmenteutilizomuitoautocomplete.Sevocêtambémcurte,no
Prytemosautocompletesimplesmentedigitando <tab>.
Comosepodever,ousodoPryajudamuitononossoprocessodede-
senvolvimento.Particularmente,euoutilizoatéquandoescrevomeustestes,
poisconsigoterumambientecontrolado,comapenasocenáriodomeuteste,
diferentedeeuabrirumconsolequeterámuitomaisdadoseelespodemnão
estarcomosvaloresdefinidosdequeeupreciso.
Oecossistema
Alémdo pry-railsqueutilizamosaqui,oPrytemtodoumecossis-
temadegemsqueajudamnesseprocessodedebug,vamosaalgumadelas.
•pry-rescue: abreoPrysemprequeumaexcessãoélan çada,https://
github.com/ConradIrwin/pry-rescue.
137

## Página 152

8.3. Conclusão CasadoCódigo
•pry-stack_explorer: permitenavegarpelo stack,https://github.com/
pry/pry-stack_explorer.
•pry-debugger: adiciona mais comandos de debug ao Pry e a
possibilidade de adicionar breakpoints,https://github.com/nixme/
pry-debugger.
•pry-plus: coleçãodeferramentasparaaumentarospoderesdoPry,
https://github.com/rking/pry-plus.
•jazz_hands:outracoleçãodeferramentasqueincluiopry-railseAwe-
somePrint,https://github.com/nixme/jazz_hands.
Antesdeadicionarestasdemaisgems,experimenteprimeiroapenascom
oPryeaoAwesomePrinte,depois,váadicionandooqueacharlegalaoseu
repertório,assimterámaisconhecimentosobrecadaumadasferramentas.
8.3 Conclusão
• VimosquepodemosmelhoraronossoconsoleutilizandooAwesome
Print;
• AcessamosadocumentaçãodiretodoconsolecomousodoPry;
• UtilizamosoPryemtempodeexecução;
• FomosapresentadosaoecossistemadoPry.
138

## Página 153

Capítulo9
Conclusão
Esperoquetenhaaproveitadoanossaaventura,aprendidoformasmelhores
deseescrevertesteseconhecidonovasferramentasetécnicasparaajudarno
processodeTDD.
Enquantoestoulendoumlivrocostumotraç aroparalelodequecada
capítuloécomosefosseumafasedoMegamane,quandofinalizoumcapítulo,
derroteiochefedafaseeganheiseuspodereseagorapossousarestenovo
podercomobementender. Esperoquetenhaderrotadotodososchefese
ganhandonovospoderesvocêtambém.
Gostariadeouvirseufeedback,entãonãodeixedemecontatarparaques-
tões,comentários,sugestõeseparainformarqualquererroqueencontrar.
Meue-mailémauro@helabs.com.br.
Segostoudoconteúdodolivro,euoconvidoparavisitaromeublogsobre
desenvolvimentodesoftwareem http://groselhas.maurogeorge.com.br.

## Página 154

CasadoCódigo
Obrigadoporchegaratéaquie happy hacking.
140

## Página 155

CasadoCódigo ReferênciasBibliográficas
ReferênciasBibliográficas
[1] PeterCooper. Dhhoffendedbyrspec,saystest::unitisjustgreat. http:
//www.rubyinside.com/dhh-offended-by-rspec-debate-4610.html,2011.
[2] JoeFerris.Let’snot.http://robots.thoughtbot.com/lets-not,2012.
[3] DavidHeinemeierHansson.Testinglikethetsa. http://signalvnoise.com/
posts/3159-testing-like-the-tsa,2012.
[4] SteveKlabnik. Whyidon’tlikefactory_girl.http://blog.steveklabnik.
com/posts/2012-07-14-why-i-don-t-like-factory_girl,2012.
[5] Robert C. Martin. Am i suggesting 100 https://twitter.com/
unclebobmartin/status/55954057327677440,2011.
[6] Andrea Reginato. Better specs rspec guidelines with ruby .http:
//betterspecs.org/,2012.
[7] JoshSteiner. Howwetestrailsapplications. http://robots.thoughtbot.
com/how-we-test-rails-applications,2014.
141