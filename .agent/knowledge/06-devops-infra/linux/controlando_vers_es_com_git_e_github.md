---json
{
  "id": "controlando_vers_es_com_git_e_github",
  "title": "Controlando versões com Git e Github",
  "categoria": "06-devops-infra",
  "subcategoria": "linux",
  "resumo": "**Arquivo Original:** `Controlando versões com Git e Github.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "com",
    "controlando",
    "devops",
    "git",
    "github",
    "infra",
    "linux",
    "vers"
  ],
  "perguntas_tipo": [
    "Como utilizar Controlando versões com Git e Github?",
    "Quais as boas praticas de linux?"
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
  "dono": "stack-linux",
  "prioridade": 2
}
---

# Controlando versões com Git e Github

> **Arquivo Original:** `Controlando versões com Git e Github.pdf`
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
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 3

E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 4

E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 5

CasadoCódigo Sumário
Sumário
1 Introdução 1
1.1 Mantendoohistóricodocódigo. . . . . . . . . . . . . . . . . 1
1.2 Trabalhandoemequipe. . . . . . . . . . . . . . . . . . . . . . 2
1.3 Sistemasdecontroledeversão . . . . . . . . . . . . . . . . . . 2
1.4 ControledeversãorápidoeconfiávelcomGit. . . . . . . . . 3
1.5 HospedandocódigonoGitHub . . . . . . . . . . . . . . . . . 3
1.6 Oprocessodeescritadesselivro. . . . . . . . . . . . . . . . . 4
2 Tourprático 5
2.1 InstalandoeconfigurandooGit . . . . . . . . . . . . . . . . . 5
2.2 Criandoumarquivotextoparaversionarmos . . . . . . . . . 7
2.3 VersionandoseucódigocomGit . . . . . . . . . . . . . . . . 8
2.4 CompartilhandoseucódigoatravésdoGitHub . . . . . . . . 12
3 Trabalhandocomrepositóriolocal 19
3.1 Criandoumrepositóriolocal. . . . . . . . . . . . . . . . . . . 20
3.2 Rastreandoarquivos. . . . . . . . . . . . . . . . . . . . . . . . 22
3.3 Gravandoarquivosnorepositório. . . . . . . . . . . . . . . . 29
3.4 Verificandoohistóricodoseurepositório . . . . . . . . . . . 36
3.5 Verificandomudan çasnosarquivosrastreados . . . . . . . . 39
3.6 Removendoarquivosdorepositório. . . . . . . . . . . . . . . 47
3.7 Renomeandoemovendoarquivos. . . . . . . . . . . . . . . . 49
3.8 Desfazendomudan ças . . . . . . . . . . . . . . . . . . . . . . 52
i
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 6

Sumário CasadoCódigo
4 Trabalhandocomrepositórioremoto 61
4.1 Repositórioremoto . . . . . . . . . . . . . . . . . . . . . . . . 62
4.2 Adicionandoorepositórioremoto . . . . . . . . . . . . . . . 63
4.3 Enviandocommitsparaorepositórioremoto . . . . . . . . . 65
4.4 Clonandoorepositórioremoto . . . . . . . . . . . . . . . . . 66
4.5 Sincronizandoorepositóriolocal . . . . . . . . . . . . . . . . 67
4.6 ProtocolossuportadospeloGit . . . . . . . . . . . . . . . . . 68
5 HospedandoorepositórionoGitHub 71
5.1 Servi çosdehospedagemdeprojetos . . . . . . . . . . . . . . 72
5.2 GitHub:aredesocialdosdesenvolvedores . . . . . . . . . . . 72
5.3 Encontrandoprojetosevisualizandoocódigo-fonte . . . . . 74
5.4 CriandoumusuárionoGitHub . . . . . . . . . . . . . . . . . 80
5.5 Criandoorepositóriodoprojeto . . . . . . . . . . . . . . . . 83
5.6 EnviandooscommitsdoprojetoparaoGitHub. . . . . . . . 85
5.7 ClonandoorepositóriohospedadonoGitHub . . . . . . . . 86
5.8 Colaborandocomprojetosopensource . . . . . . . . . . . . 87
6 Organizandootrabalhocombranches 93
6.1 Abranchmaster . . . . . . . . . . . . . . . . . . . . . . . . . . 94
6.2 Criandoumabranch . . . . . . . . . . . . . . . . . . . . . . . 96
6.3 Trocandodebranch . . . . . . . . . . . . . . . . . . . . . . . . 98
6.4 Deletandoumabranch . . . . . . . . . . . . . . . . . . . . . . 100
6.5 Comitandocódigoemumanovabranch . . . . . . . . . . . . 101
6.6 Voltandoparaomasterefazendoumaaltera ção . . . . . . . 103
6.7 Mesclandoaltera ções . . . . . . . . . . . . . . . . . . . . . . . 105
7 Trabalhandoemequipecombranchesremotas 113
7.1 Branchesremotas . . . . . . . . . . . . . . . . . . . . . . . . . 114
7.2 Compartilhandobranches . . . . . . . . . . . . . . . . . . . . 116
7.3 Obtendonovasbranchesremotasemoutrosrepositórios . . 118
7.4 Enviandocommitsparaorepositóriocentral . . . . . . . . . 121
7.5 Obtendocommitsdeumabranchremota . . . . . . . . . . . 123
7.6 Mesclandobranchesremotaselocais . . . . . . . . . . . . . . 127
7.7 Deletandobranchesremotas . . . . . . . . . . . . . . . . . . . 133
ii
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 7

CasadoCódigo Sumário
8 Controlandoversõesdocódigocomtags 137
8.1 Criando,listandoedeletandotags. . . . . . . . . . . . . . . . 138
8.2 Maisinforma çõescomtagsanotadas . . . . . . . . . . . . . . 139
8.3 Compartilhandotagscomasuaequipe. . . . . . . . . . . . . 140
9 Lidandocomconflitos 143
9.1 Mesclandomudan çasemummesmoarquivosemconflitos. 144
9.2 Conflitosapósummergecommudan çasemummesmoar-
quivo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146
9.3 Resolvendoconflitosapósumrebase . . . . . . . . . . . . . . 150
9.4 Usandoumaferramentapararesolverconflitos . . . . . . . . 152
10 ManeirasdetrabalharcomGit 157
10.1 Utilizandosóabranchmastercomumrepositóriocentral . 159
10.2 Utilizandobranchesporfuncionalidadecomumrepositório
central. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 162
10.3 Utilizandobranchesporetapadedesenvolvimentocomum
repositóriocentral . . . . . . . . . . . . . . . . . . . . . . . . . 167
10.4 ColaborandocomprojetosopensourcecomForkePullRequest173
10.5 OrganizandoprojetosopensourcegigantescoscomDitador
eTenentes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 175
11 ApêndiceGitHubnoWindows 179
11.1 InstalandooGitHubforWindows. . . . . . . . . . . . . . . . 180
11.2 Criandoumnovorepositório . . . . . . . . . . . . . . . . . . 186
11.3 Efetuandocommitsnorepositório . . . . . . . . . . . . . . . 188
11.4 Detalhandooscommits. . . . . . . . . . . . . . . . . . . . . . 190
11.5 EnviandoorepositórioparaoGitHub . . . . . . . . . . . . . 193
11.6 Trabalhandocombranches. . . . . . . . . . . . . . . . . . . . 195
Versão:17.5.7
iii
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 8

E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 9

Capítulo1
Introdução
1.1 Mantendo o histórico do código
Vidadeprogramadornãoéfácil.Hásempreumapressãoporentregasrápidas
denovasfuncionalidades.Mas,apesardapressa,énecessárioprestaraten ção
noqueestamosfazendo,mesmoseaaltera çãoforpequena. Aomexermos
emumcódigoexistenteéimportantetomarmoscuidadoparanãoquebraro
quejáfunciona.
Porisso,queremosmexeromínimopossívelnocódigo. Temosmedo
deremovercódigoobsoleto,nãoutilizadoouatémesmocomentado,mesmo
quemantê-lojánemfaçasentido.Nãoéincomumnomercadovermoscódigo
funcionalacompanhadodecentenasdelinhasdecódigocomentado.
Semdúvida,éinteressantemanterohistóricodocódigodosprojetos,
paraentendermoscomochegamosatéali. Masmanteressehistóricojunto
aocódigoatual,comodecorrerdotempo,deixanossosprojetosconfusos,
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 10

1.2. Trabalhandoemequipe CasadoCódigo
poluídoscomtrechosecomentáriosquepoderiamserexcluídossemafetaro
funcionamentodosistema.
Seriabomsehouvesseumamaneiradenavegarmospelocódigodopas-
sado,comouma máquina do tempoparacódigo...
1.2 Trabalhando em equipe
Mas,mesmoquetivéssemosessamáquinadotempo,temosoutroproblema:
muitoraramentetrabalhamossozinhos.
Construirumsistemaemequipeéumgrandedesafio.Nossocódigotem
queseintegrardemaneiratransparenteesememendascomocódigodetodos
osoutrosmembrosdanossaequipe.
Comopodemosdetectarqueestamosalterandoomesmocódigoqueum
colega?Comomesclarasaltera çõesquefizemoscomademaisaltera çõesda
equipe? Ecomoidentificarconflitosentreessasaltera ções? Fazerissoma-
nualmente,comcadernetasouplanilhasemuitaconversa,parecetrabalhoso
demaisebastantesuscetívelaerroseesquecimentos.
Seriabomquetivéssemosum robô de integraçãodecódigo,quefizesse
todoessetrabalhoautomaticamente...
1.3 Sistemas de controle de versão
Existemferramentasquefuncionamcomo máquinas do tempoe robôs de inte-
graçãoparaoseucódigo.Elasnospermitemacompanharasaltera çõesdesde
asversõesmaisantigas.Tambémépossíveldetectaremesclaraltera çõesnos
mesmosarquivos,alémdeidentificarconflitos,tudodemaneiraautomática.
Essasferramentassãochamadasde sistemasdecontroledeversão .
Nessetipodeferramenta,háum repositórioquenospermiteobterqual-
querversãojáexistentedocódigo.Semprequequisermoscontrolarasversões
dealgumarquivo,temosqueinformarquequeremosrastreá-lonorepositó-
rio. Acadamudançaquedesejamosefetivar,devemosarmazenarasaltera-
çõesnesserepositório.
Alteraçõesnosmesmosarquivossãomescladasdemaneiraautomática
semprequepossível. Jápossíveisconflitossãoidentificadosacadavezque
obtemosasmudan çasdosnossoscolegasdetime.
2
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 11

CasadoCódigo Capítulo1. Introdução
Desdeadécadade1990,existeessetipodeferramenta.Algunsexemplos
desistemasdecontroledeversãomaisantigossãoCVS,ClearCase,Source-
SafeeSVN(queaindaébastanteusadonasempresas).
Emmeadosdadécadade2000,surgiramsistemasdecontroledeversão
maismodernos,maisrápidoseconfiáveis,comoMercurial,Bazaare,éclaro,
Git.
1.4 Controle de versão rápido e confiável com
Git
OGitéumsistemadecontroledeversãoque,pelasuaestruturainterna,é
umamáquinadotempoextremamenterápidaeéumrobôdeintegra çãobem
competente.
Foicriadoem2005porLinusTorvalds,omesmocriadordoLinux,que
estavadescontentecomoBitKeeper,osistemadecontroledeversãoutilizado
nodesenvolvimentodo kerneldoLinux.
Hojeemdia,alémdo kerneldoLinux,aferramentaéutilizadaemdiver-
sosoutrosprojetosdecódigoaberto.OGittambémébastanteutilizadoem
empresasemtodoomundo,inclusivenoBrasil.
Atualmente,conhecerbemcomoutilizaroGitéumahabilidadeimpor-
tanteparaumacarreirabem-sucedidanodesenvolvimentodesoftware.
1.5 Hospedando código no GitHub
Em2008,foicriadooGitHub,umaaplica çãoWebquepossibilitaahospeda-
gemderepositóriosGit,alémdeservircomoumaredesocialparaprogra-
madores.
Diversos projetos de código aberto importantes são hospedados no
GitHubcomojQuery,Node.js,RubyOnRails,Jenkins,Spring,JUnitemuitos
outros.
3
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 12

1.6. Oprocessodeescritadesselivro CasadoCódigo
1.6 O processo de escrita desse livro
Autiliza çãodoGitnãoérestritaapenasaodesenvolvimentodesoftware,mui-
tosadministradoresderede,porexemplo,utilizamoGitparamanterohis-
tóricodeevolu çãodearquivosdeconfigura çõesemservidores.
Acreditem,atémesmoaescritadesselivrofoifeitautilizandooGit!
Nãoapenasesse,mastodososlivrosdaeditora CasadoCódigo utili-
zamoGitcomoferramentadecontroledeversão,paramanterohistóricode
evoluçãodoscapítulos.OGitHubtambéméutilizadoparahospedagemdos
repositóriosdoslivros.
4
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 13

Capítulo2
Tourprático
Nestecapítulo,faremosum tourbempráticosobrecomousaroGitparaver-
sionarnossosprojetos. Nãosepreocupecomosignificadodoscomandos.
Nodecorrerdolivro,todososcomandosusadosaquiserãoexplicadoscom
profundidade.
2.1 Instalando e configurando o Git
AntesdeutilizarmosoGit,éfundamentalinstalá-lo.EscolhaaseguiroSis-
temaOperacionalapropriadoemãosàobra!
InstalandonoWindows
AcesseaseguinteURL,fa çaodownloadeinstaleaúltimaversãodispo-
nível:http://msysgit.github.io/
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 14

2.1. InstalandoeconfigurandooGit CasadoCódigo
Ainstala çãoébastantesimples.Escolhaasop çõespadrão.
Serãoinstaladosalgunsprogramas,sendoomaisimportanteoGitBash,
quepermitequeoGitsejaexecutadopelalinhadecomandonoWindows.
DêduplocliquenoíconedoGitBasheseráabertoumterminal,como
seguinte promptnalinhadecomando:
$
Essepromptseráseuamigoapartirdeagora.Nãotenhamedo!Sempre
quefalarmosdeterminal,estaremosfalandodoGitBash.
InstalandonoMac
BaixeaúltimaversãodoinstaladorgráficodoGitparaMacOSXapartir
dolink:https://code.google.com/p/git-osx-installer/downloads
Abraumterminaleprepare-separautilizaroGit!
InstalandonoLinux
ParainstalaroGitnoUbuntu,ouemumaoutradistribui çãobaseadaem
Debian,executeemumterminal:
$ sudo apt-get install git
NoFedora,utilize:
$ sudo yum install git
Para as demais distribuições do Linux, veja o comando em: http://
git-scm.com/download/linux
Configuraçõesbásicas
ÉimportantenosidentificarmosparaoGit,informandonossonomee
e-mail.Emumterminal,executeoscomandosaseguir:
$ git config --global user.name "Fulano da Silva"
$ git config --global user.email fulanodasilva.git@gmail.com
Claro,utilizeseunomeee-mail !
6
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 15

CasadoCódigo Capítulo2. Tourprático
A linha de comando
AmaneiramaiscomumdeusarGitépelalinhadecomando,acessível
atravésdeumterminal.Éojeitoqueamaiorpartedosbonsprofissionais
domercadoutilizaoGiteseránossaescolhanesselivro.
GitHub forWindows
AmaioriadosusuáriosdoWindowsnãotemohábitodeutilizaro
promptdecomandos,eperfereinstalaralgumaaplica çãovisualparatra-
balharcomoGit.
Umadestasaplica çõeséo GitHubforWindows , emostraremos
comoutilizá-lanocapítulo11.
2.2 Criando um arquivo texto para versionar -
mos
AntesdeutilizarmosoGit,vamoscriarnasua pastapessoal,umdiretório
chamado citacoescomumarquivo filmes.txt.
Dentrodoarquivo filmes.txt,coloqueoseguinteconteúdo:
"Não há certezas, apenas oportunidades." (V de Vingança)
"Diga ’olá’ para meu pequeno amigo!" (Scarface)
7
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 16

2.3. VersionandoseucódigocomGit CasadoCódigo
Pasta pessoal
Apastapessoal( ou home directory,eminglês)éolocaldosarquivos
deusuáriocomodocumentos,fotos,músicasetc.
Sevocênãosouberondeéapastapessoal,digiteoseguintecomando
emumterminal:
$ echo ~
NoWindowsVista,7ou8,seráalgocomo C:\Users\Fulano\ou,
noGitBash, /c/Users/Fulano/.
NoWindows2000,XPou2003,seráalgocomo C:\Documents
and Settings\Fulano\ ou, no Git Bash,/c/Documents and
Settings/Fulano.
NoLinux,será /home/fulanoenoMacOSX /Users/Fulano.
2.3 Versionando seu código com Git
Criandoumrepositório
Abraumterminaleváatéodiretório citacoes.
$ cd ~/citacoes
ParatransformarodiretórioatualemumrepositóriodoGit,bastaexe-
cutarocomando git init:
$ git init
Deveráaparecerumamensagemsemelhanteàseguinte:
Initialized empty Git repository in /home/fulano/citacoes/.git/
Pronto,oprojetojáéumrepositórioGitvazio.
Observequefoicriadaumapastaocultacomonome .git.
8
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 17

CasadoCódigo Capítulo2. Tourprático
Rastreandooarquivo
Maseoarquivo filmes.txt?Seráquejáestáversionado?
Podemosverasitua çãodosarquivosnorepositórioGitcomocomando:
git status
Asaídadeveráseralgocomo:
# On branch master
#
# Initial commit
#
# Untracked files:
# (use "git add <file>..." to include in what will be
committed)
#
# filmes.txt
nothing added to commit but untracked files present (use
"git add" to track)
Observeamensagemanterior: elaindicaqueoarquivo filmes.txt
aindanãofoirastreadopeloGit.
Paraqueoarquivosejarastreado,devemosexecutaroseguintecomando:
git add filmes.txt
Agora, seexecutarmos git status novamente, teremosaseguinte
saída:
# On branch master
#
# Initial commit
#
# Changes to be committed:
# (use "git rm --cached <file>..." to unstage)
#
# new file: filmes.txt
#
9
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 18

2.3. VersionandoseucódigocomGit CasadoCódigo
Gravandooarquivonorepositório
Oresultadoanteriormostraqueoconteúdodoarquivo filmes.txtjá
estásendorastreadopeloGit,masaindanãofoigravado(ou comitado,em
umalinguagemmaistécnica)norepositório.
Paragravarmosasmudan çasnorepositório, devemosexecutaroco-
mando:
git commit -m "Arquivo inicial de citacoes"
Observequefoiinvocadoocomando git commit,comaop ção -m
parainformaramensagemdocommit.
Deveteraparecidoalgocomoaseguintemensagem:
[master (root-commit) 3bc8267] Arquivo inicial de citacoes
1 file changed, 2 insertions(+)
create mode 100644 filmes.txt
Seexecutarmos git status novamente,teremos:
# On branch master
nothing to commit, working directory clean
Alterandooarquivo
Insiramaisumalinhanoarquivo filmes.txt,comoconteúdo:
"Hasta la vista, baby." (Exterminador do Futuro 2)
Depoisdisso,seexecutarmos git status novamente,podemosobser-
varqueháumanovamudan çaparaserrastreada:
# On branch master
# Changes not staged for commit:
# (use "git add <file>..." to update what will be committed)
# (use "git checkout -- <file>..." to discard changes in
working directory)
#
# modified: filmes.txt
#
no changes added to commit (use "git add" and/or
"git commit -a")
10
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 19

CasadoCódigo Capítulo2. Tourprático
Rastreandoegravandoasaltera çõesnorepositório
Pararastrearmosamodifica ção,devemosexecutarocomando git add
novamente:
git add filmes.txt
Comamodifica çãorastreada,podemosgravá-lanorepositório,como
comando git commit:
git commit -m "Inserindo nova citacao"
Devemosterumarespostaparecidacom:
[master 67f8a28] Inserindo nova citacao
1 file changed, 1 insertion(+)
Verificandoalteraçõesrealizadas
Paraverificarohistóricodasaltera çõesgravadasnorepositório,podemos
executarocomando git log:
$ git log
Asaídaseráparecidacom:
commit 67f8a287ddd13021e85355694f0c42f0b4f8f6ff
Author: Fulano da Silva <fulanodasilva.git@gmail.com>
Date: Fri Apr 11 21:23:34 2014 -0300
Inserindo nova citacao
commit 3bc8267d18d209bb38781aba69c29000d1e831cb
Author: Fulano da Silva <fulanodasilva.git@gmail.com>
Date: Fri Apr 11 21:21:38 2014 -0300
Arquivo inicial de citacoes
Pronto! Temos um repositório criado com as alterações no arquivo
filmes.txtdevidamentegravadas.Maseagora?
11
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 20

2.4. CompartilhandoseucódigoatravésdoGitHub CasadoCódigo
2.4 Compartilhando seu código através do
GitHub
Para que o mundo possa descobrir nosso incrível projeto, temos que
compartilhá-lonainternet. Paraisso,utilizaremosumaaplica çãowebcha-
madaGitHub.
CriandoumacontanoGitHub
OprimeiropassoécriarumacontanoGitHub.Paraprojetosdecódigo
aberto,nãohácustonenhum! Comumnavegador,acesse: https://github.
com/
Preenchaseunome,e-maileescolhaumasenha.
Figura2.1:CriandocontanoGitHub
Então,selecioneoplanoapropriadoefinalizeocadastro,clicandoem
Finish Signup.
12
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 21

CasadoCódigo Capítulo2. Tourprático
Figura2.2:SelecionandoplanonoGitHub
Senecessário,verifiqueoe-mail.
CriandoumrepositórionoGitHub
Agorapodemoscriarumrepositórioremoto,queficarádisponívelpara
todosdainternet. Paraisso,cliquenobotão New Repositoryapósacessar:
https://github.com/
13
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 22

2.4. CompartilhandoseucódigoatravésdoGitHub CasadoCódigo
Figura2.3:NovorepositórionoGitHub
No Repository name,devemospreencheronomedorepositórioremoto.
Nonossocaso,vamospreenchercom“citacoes”. Deixeorepositóriocomo
Public,paraquequalquerpessoaconsigaveroseucódigo.Asdemaisop ções
podemficarcomosvalorespadrão. Finalmente,devemosclicarem Create
repository.
Figura2.4:CriandorepositórionoGitHub
Pronto,jáfoicriadoumrepositóriovaziolánoGitHub.
14
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 23

CasadoCódigo Capítulo2. Tourprático
ApontandoseuprojetoparaoGitHub
Devemosagoraapontarorepositóriodanossamáquinaparaorepositó-
riodoGitHub.
Emumterminal,certifique-sedeestarnodiretório citacoes,quetem
orepositóriolocal:
$ cd ~/citacoes
Então,executeocomando git remote,conformeoquesegue:
$ git remote add origin https://github.com/fulanodasilva/
citacoes.git
Nãodeixede alterar fulanodasilvaparao seuusuáriodoGitHub.
Nãodeveaparecernenhumamensagem.
Comocomandoanterior,apontamosonome originparaorepositório
ládoGitHub.
Enviandoasaltera çõesparaoGitHub
Comorepositórioremotoconfigurado,podemosenviarnossasmudan-
çasparaoGitHube,porconsequência,paratodoomundo.
Paraisso,bastaexecutarocomando git push,daseguinteforma:
$ git push origin master
Comocomandoanterior,enviamosasaltera çõesparaorepositóriore-
motoconfiguradocomonome origin.
ForneçaseuusuárioesenhadoGitHubquandosolicitado.Deveráapa-
receralgosemelhanteàseguintesaída:
Username for ’https://github.com’: fulanodasilva
Password for ’https://fulanodasilva@github.com’:
Counting objects: 6, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (4/4), done.
Writing objects: 100% (6/6), 609 bytes | 0 bytes/s, done.
Total 6 (delta 1), reused 0 (delta 0)
To https://github.com/fulanodasilva/citacoes.git
* [new branch] master -> master
15
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 24

2.4. CompartilhandoseucódigoatravésdoGitHub CasadoCódigo
Vá até a página do seu projeto no GitHub: https://github.com/
fulanodasilva/citacoes
Figura2.5:PáginadoprojetonoGitHub
Observequeoarquivoquevocêenvioujáestádisponívelparaqualquer
pessoadainternet.Aviseseuprimo,suavizinha,todomundo!
É possível ver todas as alterações no projeto até agora (no caso, fo-
ramduas),atravésdoendere ço: https://github.com/fulanodasilva/citacoes/
commits/master
Figura2.6:Listandoaltera çõesgravadasnoGitHub
Seclicarmosnaúltimaaltera ção,porexemplo,épossívelverasmudan ças
queforamfeitas.Fascinante,não?
16
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 25

CasadoCódigo Capítulo2. Tourprático
Figura2.7:Detalhandoumaaltera çãogravadanoGitHub
ObtendoprojetodoGitHub
ComoprojetonoGitHub,qualquerumpodeacessarocódigoevero
histórico,mesmosemumaconta. SeapessoativercadastradanoGitHub,
serápossívelbaixarocódigo.
Vamossimularisso,baixandoocódigoemoutrodiretóriodoseucom-
putador.
Nasuapastapessoal,crieumdiretóriochamado projetos_git.Então,
oacessepeloterminal:
$ cd ~/projetos_git
ParaobterocódigodoprojetoládoGitHub,executeocomando git
cloneconformeoseguinte:
git clone https://github.com/fulanodasilva/citacoes.git
Nãoesque çadealterar fulanodasilvaparaoseuusuáriodoGitHub.
Deveráapareceralgocomo:
Cloning into ’citacoes’...
remote: Counting objects: 6, done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 6 (delta 1), reused 6 (delta 1)
Unpacking objects: 100% (6/6), done.
Checking connectivity... done
17
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 26

2.4. CompartilhandoseucódigoatravésdoGitHub CasadoCódigo
Observenodiretório projetos_gitquefoicriadoumsubdiretório
chamado citacoes.Dentrodessesubdiretórioháoarquivo filmes.txt,
comexatamenteomesmoconteúdoládoGitHub.
Hátambémumdiretórioocultochamado .git,revelandoquetemos
umacópiadorepositóriooriginal.
Váatéosubdiretório citacoes,executandoocomando:
$ cd citacoes
Podemosexecutarocomando git log nessenovorepositório:
$ git log
Teremosamesmasaídadeantes:
commit 67f8a287ddd13021e85355694f0c42f0b4f8f6ff
Author: Fulano da Silva <fulanodasilva.git@gmail.com>
Date: Fri Apr 11 21:23:34 2014 -0300
Inserindo nova citacao
commit 3bc8267d18d209bb38781aba69c29000d1e831cb
Author: Fulano da Silva <fulanodasilva.git@gmail.com>
Date: Fri Apr 11 21:21:38 2014 -0300
Arquivo inicial de citacoes
Sevocêtiveroutrocomputador,fa çao clonenele. Nãoseesque çade
instalaroGit,seguindoospassosdoiníciodestecapítulo.
Git eGitHub são a mesma coisa?
Não.Gitéosistemadecontroledeversões,comoqualinteragimos
nalinhadecomando.JáoGitHubéumaredesocialparaprogramadores
quedisponibilizarepositóriosGitacessíveisremotamente. OGitHubé
muitoutilizadoparaprojetosopensourcequepossuemvárioscolabora-
doresdomundotodo.Maisadianteaprofundaremosemambos.
18
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 27

Capítulo3
Trabalhandocomrepositório
local
AempresaMóveisEcológicosnoscontratouparafazerapáginadaempresa
naweb.Conversamoscomodonodaempresa,discutimossobreoconteúdo
básicoecriamosumHTMLsimples.
Apresentamosoresultadoenossoclientepediuparacolocarmosapágina
noar.Logoofizemos:diversãoelucro!
Porém,adiretoraderela çõespúblicasdaempresanãogostoudotexto.
Pediuparaalterarmosparaumtextobemmaiorecommaiscarade press
release.Fizemosasaltera çõesepublicamos.
Depoisdealgumtempo,odonodaempresanotouositemodificadoenos
contatouparavoltarmoscomaversãoanterior.Acontecequeesquecemosde
fazer backupdoarquivo.Atétentamosusarumrecuperadordearquivosou
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 28

3.1. Criandoumrepositóriolocal CasadoCódigo
lembraroconteúdodecabe ça,masnãotivemossucesso.Eagora?
Commuitarelutância,entramosemcontatocomodonodaempresape-
dindoqueotextofosseditonovamenteportelefone. Depoisdealgunsmi-
nutosdexingamentosedequaseperdermosocontrato,conseguimosotexto
maisumavez.
Poxavida...Devíamostermantidootextoantigocomentadonapágina...
Mascomtantasmudan ças,empoucotempoteríamosmaiscomentáriosdo
quecódigodefato.
SetivéssemosutilizadoumsistemadecontroledeversãocomooGit,te-
ríamosumamáquinadotempoparaonossocódigo.Aí,nossavidaseriamais
fácil.
3.1 Criando um repositório local
Vamos dizer que, na nossa pasta pessoal, temos um diretório chamado
moveis,comoarquivo index.htmlcontendooseguinteconteúdo:
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<meta name="description" content="Móveis ecológicos">
<meta name="keywords" content="moveis ecologicos">
</head>
<body>
<h1>Móveis Ecológicos S. A.</h1>
<ul>
<li>Móveis de garrafas PET</li>
<li>Móveis de latinhas de alumínio</li>
<li>Móveis de papelão</li>
</ul>
</body>
</html>
Antesdetudo,vamosentrarnodiretório moveis,comocomando cd
~/moveis.
ParacriarumrepositórioGitnessediretório,bastaexecutarmos:
20
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 29

CasadoCódigo Capítulo3. Trabalhandocomrepositóriolocal
$ git init
Teremosasaída:
Initialized empty Git repository in /home/fulano/moveis/.git/
Amensagemanteriorindicaquetransformamosodiretório moveisem
umrepositórioGit.
Selistarmososarquivosdodiretório moveiscomocomando ls -lha,
teremosumarespostasemelhanteaoquesegue:
total 36K
drwxr-xr-x 3 fulano fulano 4,0K Abr 15 21:30 .
drwx------ 58 fulano fulano 16K Abr 15 21:28 ..
drwxr-xr-x 7 fulano fulano 4,0K Abr 15 21:30 .git
-rw-r--r-- 1 fulano fulano 405 Abr 15 21:28 index.html
Observemquefoicriadoumsubdiretórioocultochamado .gitnapasta
moveis. EssesubdiretórioéumrepositóriodoGitcompleto,queconterá
todoohistóricodealtera çõesdosarquivos,entreoutrascoisas.
Podemosexecutar git init moveis sequisermoscriarumdire-
tóriovazioquejáéumrepositórioGit,ouseja,quejápossuio .git.
Nocasodetermosoutrossubdiretórioscomo jsparaarmazenarcódigo
Javascripte cssparaarmazenararquivosCSS,todasasinforma çõesdesses
arquivosserãoarmazenadasnomesmo .git.
SeporalgummotivoquisermosparardeusaroGit,bastaremoveresse
únicodiretório .git.
Bastaocomando git init paracriarumrepositóriocomGit,que
jácrialocalmenteumrepositóriocompleto.Issoébemmaissimplesque
diversosoutrossistemasdecontroledeversão,comooSVN,quepreci-
savamdaconfigura çãodeumservidor.
21
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 30

3.2. Rastreandoarquivos CasadoCódigo
3.2 Rastreando arquivos
Paraverificarmosoestadoatualdonossorepositório,devemosexecutaro
comando:
$ git status
Deveaparecerumarespostaparecidacom:
# On branch master
#
# Initial commit
#
# Untracked files:
# (use "git add <file>..." to include in what will be
committed)
#
# index.html
nothing added to commit but untracked files present (use
"git add" to track)
Notequeoarquivo index.htmlaindanãoestásendorastreado(está
em Untracked files).
ParainformaraoGitqueoarquivo index.htmldeveserrastreado,uti-
lizamosocomando:
$ git add index.html
Pronto! AgoraoGitsabequeessearquivoéimportanteeasmudan ças
devemserrastreadas.
Seexecutarmosnovamente git status,teremosaseguintesaída:
# On branch master
#
# Initial commit
#
# Changes to be committed:
# (use "git rm --cached <file>..." to unstage)
#
# new file: index.html
#
22
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 31

CasadoCódigo Capítulo3. Trabalhandocomrepositóriolocal
ObservequeoGitagorapassouarastrearoarquivo index.htmleestá
prontoparagravaressearquivonorepositório( Changes to be committed).
Rastreandováriosarquivos
Vamos dizer que criamos um arquivoestilos.css no diretório
moveis,comoseguinteconteúdo:
h1 {
font-family: sans-serif;
}
li {
font-family: monospace;
}
Também criamos um subdiretório imagens com um arquivo
logo.png,comumaimagemsemelhantea:http://goo.gl/6nganu
Seexecutarmos git status,teremos:
# On branch master
#
# Initial commit
#
# Changes to be committed:
# (use "git rm --cached <file>..." to unstage)
#
# new file: index.html
#
# Untracked files:
# (use "git add <file>..." to include in what will be
committed)
#
# estilos.css
# imagens/
Observequeoarquivo estilos.csseodiretório imagensaindanão
estãosendorastreados( Untracked files).
Sequisermosrastreartodosessesarquivos,seráqueteremosqueexecutar
git add umporum?
23
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 32

3.2. Rastreandoarquivos CasadoCódigo
Naverdade,não! Podemosrastreartodosessesarquivosdeumavezsó
comocomando:
$ git add .
O pontodocomandoanteriorrepresentatodososarquivosnãorastreados
dodiretórioatualetambémdetodososseussubdiretórios.
Agora,aoexecutarmos git status,veremosquetodososarquivos
estãosendorastreados:
# On branch master
#
# Initial commit
#
# Changes to be committed:
# (use "git rm --cached <file>..." to unstage)
#
# new file: estilos.css
# new file: imagens/logo.png
# new file: index.html
#
Se quiséssemos ter rastreado apenas os arquivos do subdiretório
imagens,porexemplo,poderíamosterexecutadoocomando git add
imagens.
Aáreadestage
QuandoinformamosparaoGitquequeremosrastrearumarquivo,exe-
cutando git add pelaprimeiravez,oGitcolocaessearquivoemumaárea
especialdorepositório,chamadade stage.
Umavezqueumarquivoestánaáreadestage,todasasmudan çasnesse
arquivopassamaserexaminadas.
Odiretórioquecontémnossosarquivoséchamadodediretóriode
trabalhoou working directory,eminglês.
24
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 33

CasadoCódigo Capítulo3. Trabalhandocomrepositóriolocal
Vamosmodificaroarquivo index.html,inserindoumareferênciaao
CSScriadoanteriormente:
<!-- início do arquivo ... -->
<head>
<!-- tags meta ... -->
<link rel="stylesheet" href="estilos.css">
</head>
<!-- restante do arquivo ... -->
Asaídado git status será:
# On branch master
#
# Initial commit
#
# Changes to be committed:
# (use "git rm --cached <file>..." to unstage)
#
# new file: estilos.css
# new file: imagens/logo.png
# new file: index.html
#
# Changes not staged for commit:
# (use "git add <file>..." to update what will be committed)
# (use "git checkout -- <file>..." to discard changes in
working directory)
#
# modified: index.html
#
Notequeo index.htmlcontinuaaparecendocomoumnovoarquivo
rastreado( new fileem Changes to be committed),indicandoqueeleestásendo
rastreadoeprontoparasergravado.
Masobservequeoarquivo index.htmlaparecemaisumavez,sob
Changes not staged for commit,comomodificado( modified).
Issoaconteceporque,umavezqueumarquivopassaaserrastreadopelo
Git,depoisdecolocá-lonaáreadestagecomocomando git add,cada
25
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 34

3.2. Rastreandoarquivos CasadoCódigo
mudançanessearquivoérastreadaetambémdevesercolocadanaáreade
stage.
Para colocarmos as últimas mudanças que fizemos no arquivo
index.htmlnaáreadestage,devemosexecutarnovamente:
$ git add index.html
Depoisdisso,aoexecutarmos git status,teremos:
# On branch master
#
# Initial commit
#
# Changes to be committed:
# (use "git rm --cached <file>..." to unstage)
#
# new file: estilos.css
# new file: imagens/logo.png
# new file: index.html
#
Agora,tantooarquivooriginalcomoasúltimasmudan çasestãoprontas
paraseremgravadasnorepositório.
Umarepresenta çãográficadastransi çõesentreodiretóriodetrabalhoe
aáreadestageseria:
Figura3.1:Rastreandoarquivosemudan çascomGit
26
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 35

CasadoCódigo Capítulo3. Trabalhandocomrepositóriolocal
Ignorandoarquivos
Suponhaquetemosumarquivo todo.txtquemantemos,duranteo
desenvolvimento,comalistadastarefasdodia.Suponhatambémquetemos
umsubdiretóriochamado tmp,comalgunsarquivostemporáriosgeradosao
manipularmosimagens.NãofazsentidomanterohistóricodeambosnoGit.
Seexecutarmos git status,oarquivo todo.txteosubdiretório
tmpserãomostradoscomoarquivosaindanãorastreados:
# On branch master
#
# Initial commit
#
# Changes to be committed:
# (use "git rm --cached <file>..." to unstage)
#
# new file: estilos.css
# new file: imagens/logo.png
# new file: index.html
#
# Untracked files:
# (use "git add <file>..." to include in what will be
committed)
#
# tmp/
# todo.txt
Seráqueteremossemprequelembrardeevitaro git add dessesar-
quivos?Seforassim,nãopoderemosmaisutilizar git add . ,jáqueesse
comandorastreiatodososarquivos.
Pararesolverisso,oGittemummecanismoquepermiteignorarmosar-
quivos.Bastacriarmosumarquivochamado .gitignorenodiretórioprin-
cipaldonossoprojeto,comosnomesdosarquivosquequeremosignorar.
Nonossocaso,devemoscriarumarquivochamado .gitignoreno
diretório moveis,comoseguinteconteúdo:
todo.txt
tmp/
27
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 36

3.2. Rastreandoarquivos CasadoCódigo
Dessamaneira,oarquivo todo.txteosubdiretório tmpnãoserão
mostradosaoexecutarmosocomando git status:
# On branch master
#
# Initial commit
#
# Changes to be committed:
# (use "git rm --cached <file>..." to unstage)
#
# new file: estilos.css
# new file: imagens/logo.png
# new file: index.html
#
# Untracked files:
# (use "git add <file>..." to include in what will be
committed)
#
# .gitignore
Observe,porém,queoarquivo .gitignoreapareceucomonãorastre-
ado.Éimportantequeessearquivosejarastreado,porqueevoluirájuntocom
orepositório.Porisso,aocriaro .gitignore,nãoesque çadeadicioná-lo
àáreadestagecomocomando:
$ git add .gitignore
Sequiséssemosignorartodososarquivoscomaextensão .log,por
exemplo, colocaríamos *.logno .gitignore. Sequiséssemosigno-
rartodososarquivos .bmpdosubdiretório imagens,deveríamosinserir
imagens/*.bmp.
28
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 37

CasadoCódigo Capítulo3. Trabalhandocomrepositóriolocal
Naprática,quetipodearquivossãocolocadosno .gitignore?De-
pendedatecnologiautilizadanoprojeto.
EmprojetosJava,arquivos .class, .jare .warsãoexemplos
dearquivosquedevemserignorados.ParaprojetosRuby,ignoraríamos
arquivos .gemeodiretório pkg. JáparaprojetosPython,arquivos
.egg.
HáumprojetonoGitHubcomexemplosdearquivos .gitignore
paradiversaslinguagensdeprograma çãoetecnologias: https://github.
com/github/gitignore
3.3 Grav ando arquivos no repositório
Osarquivosealtera çõesqueforamcolocadosnaáreadestageatravésdoco-
mando git add aindanãoforamgravadosnorepositório.Aoinvocarmos
o git status,podemosnotarqueessesarquivosestãoprontosparaserem
gravados( Changes to be committed):
# On branch master
#
# Initial commit
#
# Changes to be committed:
# (use "git rm --cached <file>..." to unstage)
#
# new file: .gitignore
# new file: estilos.css
# new file: imagens/logo.png
# new file: index.html
#
Paragravaressesarquivosealtera çõesdefinitivamentenorepositório,de-
vemosutilizarocomando git commit:
$ git commit -m "Commit inicial"
Observequepassamosumamensagemquedescreveasaltera çõesefetu-
adas,atravésdaop ção -m.Senãopassássemosessaop ção,seriaabertoum
29
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 38

3.3. Gravandoarquivosnorepositório CasadoCódigo
editordetextoparainformarmosamensagem.
Nonossocaso,utilizamosamensagem“Commitinicial”. Éimportante
queasmensagensdescrevamdemaneirasucintaasaltera çõesqueforamefe-
tuadas.
Depoisdeexecutadoessecomando,deveráapareceralgocomo:
[master (root-commit) 4a4fdf7] Commit inicial
4 files changed, 26 insertions(+)
create mode 100644 .gitignore
create mode 100644 estilos.css
create mode 100644 imagens/logo.png
create mode 100644 index.html
Noteque,naprimeiralinhadasaídaapresentada,éexibidoumcódigo
logoantesdamensagem( 4a4fdf7,nocaso). Essecódigoservecomoum
identificadordocommit.Naverdade,foramexibidosapenasosprimeiros7
dígitosdessecódigo,quecontém40caracteresaotodo.
Maisespecificamente,essecódigoéumnúmerodeverifica çãodein-
tegridadededados( checksum)criadoapartirdoconteúdodoarquivo
utilizandoafun çãode hashSHA-1. PorutilizarSHA-1,érepresentado
porumnúmerohexadecimalde40dígitos.
Se verificarmos agora o estado do repositório com o comandogit
status,teremos:
# On branch master
nothing to commit, working directory clean
Observequeonãohánadamaisasercomitado.
Otermo commitécomumemqualquersistemacontroladordeversão
esignificagravarnovosarquivosealtera çõesemarquivosexistentesem
umrepositório.Emportuguês,ostermos comitarou comitadosãobem
corriqueiros,apesardenãoexistiremnosdicionários.
30
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 39

CasadoCódigo Capítulo3. Trabalhandocomrepositóriolocal
Rastreandoecomitandomudan çasdeumasóvez
Percebemos que havíamos esquecido de colocar o título na página
index.html.Vamosalteraroarquivo:
<!-- início do arquivo ... -->
<head>
<!-- tags meta e link ... -->
<title>Móveis Ecológicos</title>
</head>
<!-- restante do arquivo ... -->
Alémdisso, vamosdiminuirotamanhodapáginaparaficarmelhor
em dispositivos com telas pequenas. Para isso, alteraremos o arquivo
estilos.css:
body {
width: 50%;
margin: auto;
}
/* resto do css */
Seexecutarmos git status,teremos:
# On branch master
# Changes not staged for commit:
# (use "git add <file>..." to update what will be committed)
# (use "git checkout -- <file>..." to discard changes in
working directory)
#
# modified: estilos.css
# modified: index.html
#
no changes added to commit (use "git add" and/or
"git commit -a")
Notequeosarquivosaparecemcomomodificados,masaáreadestage
aindanãocontémasmudan çasefetuadas( Changes not staged for commit).
Poderíamos efetuar ogit add dessas mudanças seguido do git
commit. Porém,épossívelrastrearasmudan çasecomitá-lasdeumavez
comaop ção -a:
31
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 40

3.3. Gravandoarquivosnorepositório CasadoCódigo
$ git commit -a -m "Inserindo titulo e diminuindo tamanho da
pagina"
Teremoscomorespostadocomandoanterioralgocomo:
[master ccff92c] Inserindo titulo e diminuindo tamanho da pagina
2 files changed, 5 insertions(+)
Aop ção -adocomando git commit jáefetuaorastreamentodasmu-
danças,adicionando-asàáreadestage. Poderíamosjuntarasop ções -ae
-mutilizando -amdaseguintemaneira: git commit -am "Inserindo
titulo..."
Nesseponto,asaídadocomando git status indicaráquenãohámais
nadaasercomitado:
# On branch master
nothing to commit, working directory clean
Novosarquivosprecisamdegitadd
Nossoclientepediuquecolocássemosumamensagemnapáginaqueé
trocadaautomaticamentedetemposemtempos.
Parafazerisso,criamosumarquivochamado principal.js,como
seguinteconteúdo:
var banners =
["Os melhores do Brasil!", "Qualidade e preço baixo!"];
var bannerAtual = 0;
function trocaBanner() {
bannerAtual = (bannerAtual + 1) % 2;
document.querySelector(’h2#mensagem’).textContent =
banners[bannerAtual];
}
setInterval(trocaBanner, 2000);
Precisamos também adicionar o script anterior à nossa página
index.html,alémdeumatag h2quevaiconteramensagem:
32
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 41

CasadoCódigo Capítulo3. Trabalhandocomrepositóriolocal
<!-- início do arquivo ... -->
<head>
<!-- tags meta, link e title ... -->
<script src="principal.js"></script>
</head>
<body>
<!-- tag h1 ... -->
<h2 id="mensagem"></h2>
<!-- restante do arquivo ... -->
Aoexecutarmosocomando git status,teremosasaída:
# On branch master
# Changes not staged for commit:
# (use "git add <file>..." to update what will be committed)
# (use "git checkout -- <file>..." to discard changes in working
directory)
#
# modified: index.html
#
# Untracked files:
# (use "git add <file>..." to include in what will be
committed)
#
# principal.js
no changes added to commit (use "git add" and/or
"git commit -a")
Observequeémostradaamodifica çãonoarquivo index.htmletam-
bémonovoarquivo principal.js.
Vamosexecutarocomandopararastrearecomitarosarquivosdeuma
vezsó:
git commit -am "Script de troca de banner"
Nasaída,teremos:
[master bb229c6] Script de troca de banner
1 file changed, 2 insertions(+)
33
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 42

3.3. Gravandoarquivosnorepositório CasadoCódigo
Qualseráarespostado git status?Será:
# On branch master
# Untracked files:
# (use "git add <file>..." to include in what will be
committed)
#
# principal.js
nothing added to commit but untracked files present (use
"git add" to track)
Observequeo git commit comaop ção -aadicionounostageape-
nasasmudan çasdoarquivoquejáestavasendorastreado.Onovoarquivo,
principal.js,nãopassouaserrastreado.
Semprequetivermosumarquivonovo,temosqueutilizarocomando
git add,paraqueoGitpassearastreá-lo.Sóentãopoderemoscomitá-lo.
Vamoslá:
$ git add principal.js
Apósexecutarmoso git status,teremos:
# On branch master
# Changes to be committed:
# (use "git reset HEAD <file>..." to unstage)
#
# new file: principal.js
#
Agorapodemoscomitaroarquivo principal.js:
$ git commit -m "Inserindo arquivo principal.js"
Teremosumasaídaparecidacom:
[master 842d2cf] Inserindo arquivo principal.js
1 file changed, 10 insertions(+)
create mode 100644 principal.js
Aoexecutarmosocomando git status,teremos:
34
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 43

CasadoCódigo Capítulo3. Trabalhandocomrepositóriolocal
# On branch master
nothing to commit, working directory clean
Agorasim! Tantoaaltera çãoem index.htmlcomoonovoarquivo
principal.jsestarãocomitadosnorepositório.
Aovisualizarmosgraficamenteastransi çõesentreodiretóriodetrabalho,
aáreadestageeorepositóriopropriamentedito,teríamosalgocomo:
Figura3.2:Gravandoarquivosemudan çascomGit
Parasabermais:paraqueserveaáreadestage?
OGit,aocontráriodamaioriadossistemasdecontroledeversão,possui
umasepara çãoentrerastrearasmudan ças,adicionando-asnaáreadestage
comocomando git add,egravarasmudan çasnorepositório,comoco-
mando git commit.
Masseráqueessasepara çãoéútil?Ésim!
Vamosdizerqueestamosdesenvolvendoumsistemaquetemummó-
dulodeestoqueeumdevendas.Aodesenvolverumanovafuncionalidade,
modificamosquatroarquivos,sendoquedoissãodeestoqueedoissãode
vendas.
Poderíamos,primeiramente,gravarasaltera çõesfeitasnosdoisarquivos
deestoque,adicionandoapenasessesdoisàstageecomitando-oscomuma
mensagembemdescritiva.Depois,faríamoso git add e git commit dos
arquivosdevendas,tambémcomumamensagembemdescritiva.
35
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 44

3.4. Verificandoohistóricodoseurepositório CasadoCódigo
Ouseja,essasepara çãoentrerastrearegravarpermitequeasmudan-
çasquefizemosnocódigosejamagrupadasdemaneiralógica.Dessaforma,
podemosmontarcommitsmenores,quefarãomaissentidoposterioraore-
visarmosohistóricodoprojetoeajudarãoaomesclarmosnossasmudan ças
comasdosoutrosmembrosdonossotime.
3.4 Verificando o histórico do seu repositório
Paraverificarohistóricodasmudan çasgravadasnorepositório,ouseja,os
commitsefetuados,devemosutilizarocomando:
$ git log
Apósexecutarocomandoanterior,teremosaseguintesaída:
commit 842d2cfc43418109e8f1bbd8ff8b91813f05373c
Author: Fulano da Silva <fulanodasilva.git@gmail.com>
Date: Wed Apr 30 14:32:38 2014 -0300
Inserindo arquivo principal.js
commit bb229c6f5bf64f210fa5acb21e52286456e27ac8
Author: Fulano da Silva <fulanodasilva.git@gmail.com>
Date: Wed Apr 30 14:24:06 2014 -0300
Script de troca de banner
commit ccff92c4036e50b573ad0a661a32416942da2c76
Author: Fulano da Silva <fulanodasilva.git@gmail.com>
Date: Wed Apr 30 14:02:26 2014 -0300
Inserindo titulo e diminuindo tamanho da pagina
commit 4a4fdf77dc2e9e59c4b6a82523ab32dfc81859fc
Author: Fulano da Silva <fulanodasilva.git@gmail.com>
Date: Tue Apr 29 12:47:36 2014 -0300
Commit inicial
36
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 45

CasadoCódigo Capítulo3. Trabalhandocomrepositóriolocal
Observequeforamlistadasasmensagensdetodososcommits,juntoao
códigocorrespondente,autoredata/horaemqueforamefetuados.
Sequisermosmostrarapenasosdoisúltimoscommitsdevemosutilizara
opção -n:
$ git log -n 2
Apósexecutarocomandoanterior,teremosaseguintesaída:
commit 842d2cfc43418109e8f1bbd8ff8b91813f05373c
Author: Fulano da Silva <fulanodasilva.git@gmail.com>
Date: Wed Apr 30 14:32:38 2014 -0300
Inserindo arquivo principal.js
commit bb229c6f5bf64f210fa5acb21e52286456e27ac8
Author: Fulano da Silva <fulanodasilva.git@gmail.com>
Date: Wed Apr 30 14:24:06 2014 -0300
Script de troca de banner
Sequisermosumresumobemconcisodoscommitsdonossoprojeto,
podemosutilizaraop ção --oneline:
$ git log --oneline
Seráapresentadoalgosemelhantea:
842d2cf Inserindo arquivo principal.js
bb229c6 Script de troca de banner
ccff92c Inserindo titulo e diminuindo tamanho da pagina
4a4fdf7 Commit inicial
Podemosmostrarumresumodosarquivosalterados,comonúmerode
linhasadicionadaseremovidas,atravésdaop ção --stat.
$ git log --stat
Asaídaseráalgocomo:
37
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 46

3.4. Verificandoohistóricodoseurepositório CasadoCódigo
commit 842d2cfc43418109e8f1bbd8ff8b91813f05373c
Author: Fulano da Silva <fulanodasilva.git@gmail.com>
Date: Wed Apr 30 14:32:38 2014 -0300
Inserindo arquivo principal.js
principal.js | 10 ++++++++++
1 file changed, 10 insertions(+)
commit bb229c6f5bf64f210fa5acb21e52286456e27ac8
Author: Fulano da Silva <fulanodasilva.git@gmail.com>
Date: Wed Apr 30 14:24:06 2014 -0300
Script de troca de banner
index.html | 2 ++
1 file changed, 2 insertions(+)
commit ccff92c4036e50b573ad0a661a32416942da2c76
Author: Fulano da Silva <fulanodasilva.git@gmail.com>
Date: Wed Apr 30 14:02:26 2014 -0300
Inserindo titulo e diminuindo tamanho da pagina
:
Podemosobservarqueforammostradososarquivosmodificadoseonú-
merodeinser ções.
Notetambémqueoúltimocaracterefoiumdoispontos( :).Aoapertar-
mosatecla Enter,serãomostradososresultadosrestantes.
estilos.css | 4 ++++
index.html | 1 +
2 files changed, 5 insertions(+)
commit 4a4fdf77dc2e9e59c4b6a82523ab32dfc81859fc
Author: Fulano da Silva <fulanodasilva.git@gmail.com>
Date: Tue Apr 29 12:47:36 2014 -0300
Commit inicial
38
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 47

CasadoCódigo Capítulo3. Trabalhandocomrepositóriolocal
.gitignore | 3 +++
estilos.css | 6 ++++++
imagens/logo.png | Bin 0 -> 15128 bytes
index.html | 20 ++++++++++++++++++++
4 files changed, 29 insertions(+)
(END)
Parasairmosdoresultadosdo git log,devemosapertaratecla q.
Podemostambémcombinarasváriasopçõesdocomando git log.Por
exemplo,paramostrarumresumodasaltera çõesdosúltimosdoiscommits:
$ git log -n 2 --oneline --stat
Teremosaseguintesaída:
842d2cf Inserindo arquivo principal.js
principal.js | 10 ++++++++++
1 file changed, 10 insertions(+)
bb229c6 Script de troca de banner
index.html | 2 ++
1 file changed, 2 insertions(+)
Qualadiferen çaentreoscomandos git status eo git log?
O git status exibearquivosqueestãoforadaáreadestage,pron-
tosparaseremadicionados,earquivosqueestãodentrodaáreadestage,
prontosparaseremcomitados.
Jáo git log exibeohistóricodasmudan çasefetivamentegravadas
emumrepositório.Ouseja,oscommitsefetuados.
3.5 Verificando mudanças nos arquivos rastre -
ados
Percebemosum bugnonossocódigo:aoabrirmosapágina,nãoémostrado
nenhum banner. Paracorrigir,devemosinvocarafun ção trocaBanner
no evento onload da página, fazendo a seguinte mudança no arquivo
index.html:
39
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 48

3.5. Verificandomudançasnosarquivosrastreados CasadoCódigo
<!-- início do arquivo ... -->
<body onload="trocaBanner();">
<!-- restante do arquivo ... -->
Depoisdefazeressaaltera ção,aoinvocarmos git status,teremos:
# On branch master
# Changes not staged for commit:
# (use "git add <file>..." to update what will be committed)
# (use "git checkout -- <file>..." to discard changes in working
directory)
#
# modified: index.html
#
no changes added to commit (use "git add" and/or
"git commit -a")
Tudoconformeoesperado. Éinformadoqueoarquivo index.html
sofreuumamodifica ção.
Verificandomudançasaindanãorastreadas
Sequisermosrevisaramodifica çãoefetuada,verificandoasdiferen çasen-
treoarquivoalteradoeoquefoicomitadoanteriormente,podemosusaro
comando:
$ git diff
Serámostradoalgocomo:
diff --git a/index.html b/index.html
index b1115c7..4786946 100644
--- a/index.html
+++ b/index.html
@@ -8,7 +8,7 @@
<title>Móveis Ecológicos</title>
<script src="principal.js"></script>
</head>
- <body>
+ <body onload="trocaBanner();">
40
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 49

CasadoCódigo Capítulo3. Trabalhandocomrepositóriolocal
<h1>Móveis Ecológicos S. A.</h1>
<h2 id="mensagem"></h2>
Observequefoimostradaexatamenteamudan çaquefizemosanterior-
mente:atrocade <body>por <body onload="trocaBanner();">.
Quandotivermosaltera çõesaindanãorastreadasemmaisdeumarquivo
equisermosverificaroquemudamosemumarquivoespecífico,bastapas-
sarmosonomedessearquivocomoparâmetro.Porexemplo,paraverificar-
mosasmudan çasapenasnoarquivo index.html,faríamos: git diff
index.html.
O git diff nãopoderáserutilizadoparaarquivosnovos,queainda
nãoestãosendorastreadospeloGit(ouseja,queaindanãotiveramo
primeiro git add executado).
Verificandomudançasrastreadas
Vamosadicionarasmudan çasquefizemosàáreadestagecomocomando
git add index.html .
Seexecutarmos git diff novamente, nãoserámostradanenhuma
saída.Ocomando git diff,quandousadosemparâmetros,mostraadi-
ferençaentreosarquivosnodiretóriodetrabalhoeaáreadestage.Portanto,
serveapenasparaexibirasmudan çasaindanãorastreadas.
Épossívelmostrarasdiferen çasentreosarquivosnaáreadestageea
últimaversãoquefoicomitadautilizandoaop ção --staged:
$ git diff --staged
Seráexibidaumasaídaexatamenteigualàanterior,jáqueaaltera çãoape-
naspassouparaaáreadestagemascontinuaamesma:
diff --git a/index.html b/index.html
index b1115c7..4786946 100644
--- a/index.html
+++ b/index.html
@@ -8,7 +8,7 @@
41
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 50

3.5. Verificandomudançasnosarquivosrastreados CasadoCódigo
<title>Móveis Ecológicos</title>
<script src="principal.js"></script>
</head>
- <body>
+ <body onload="trocaBanner();">
<h1>Móveis Ecológicos S. A.</h1>
<h2 id="mensagem"></h2>
Antesdaversão1.6.1doGit,sóhaviaaop ção --cached,quetemo
mesmoefeitodaop ção --staged.
Verificando mudanças rastreadas e não rastreadas ao mesmo
tempo
Vamosdiminuirotempodetrocado bannerparaumsegundoalterando
oarquivo principal.js:
//inicio do arquivo...
setInterval(trocaBanner, 1000);
Nesse ponto, temos duas alterações. Uma delas foi no arquivo
index.htmlquejáestánaáreadestage.Tambémtemosumaaltera çãono
arquivo principal.jsaindanãorastreada.Issopodeserverificadocom
ocomando git status:
# On branch master
# Changes to be committed:
# (use "git reset HEAD <file>..." to unstage)
#
# modified: index.html
#
# Changes not staged for commit:
# (use "git add <file>..." to update what will be committed)
# (use "git checkout -- <file>..." to discard changes in working
directory)
#
# modified: principal.js
#
42
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 51

CasadoCódigo Capítulo3. Trabalhandocomrepositóriolocal
Seexecutarmosocomando git diff,veremosapenasaaltera çãono
arquivo principal.js:
diff --git a/principal.js b/principal.js
index 5d114bd..696870a 100644
--- a/principal.js
+++ b/principal.js
@@ -6,5 +6,5 @@ function trocaBanner() {
document.querySelector(’h2#mensagem’).textContent =
banners[bannerAtual];
}
-setInterval(trocaBanner, 2000);
+setInterval(trocaBanner, 1000);
Jáaoexecutarmosocomando git diff --staged ,veremosapenasa
alteraçãonoarquivo index.html,quejáverificamosanteriormente.
Seráqueépossívelexibirtantoasaltera çõesforadaáreade stagecomoas
dedentro?
Sim! Paraisso,precisamosdescobrirocódigodoúltimocommit. Po-
demosfazerissocomocomando git log -n 1 --oneline .Teremosa
saída:
842d2cf Inserindo arquivo principal.js
Comocódigodoúltimocommitemmãos,agorapodemosmostraras
alteraçõesdentroeforadastageutilizandoocomando:
$ git diff 842d2cf
Serãoexibidasambasasaltera ções:
diff --git a/index.html b/index.html
index b1115c7..4786946 100644
--- a/index.html
+++ b/index.html
@@ -8,7 +8,7 @@
<title>Móveis Ecológicos</title>
<script src="principal.js"></script>
43
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 52

3.5. Verificandomudançasnosarquivosrastreados CasadoCódigo
</head>
- <body>
+ <body onload="trocaBanner();">
<h1>Móveis Ecológicos S. A.</h1>
<h2 id="mensagem"></h2>
diff --git a/principal.js b/principal.js
index 643ad98..696870a 100644
--- a/principal.js
+++ b/principal.js
@@ -6,5 +6,5 @@ function trocaBanner() {
document.querySelector(’h2#mensagem’).textContent =
banners[bannerAtual];
}
-setInterval(trocaBanner, 2000);
+setInterval(trocaBanner, 1000);
:
Comooresultadoéextenso,serámostradoocaracteredoispontos( :).
Parairmosparaospróximosresultadosdevemospressionaratecla Enter.
Parasairmos,devemosapertaratecla q.
Nonossocaso,teríamosamesmasaídaanterior,quemostraasalte-
raçõesdentroeforadostage,utilizandoocomando git diff HEAD .
Issoaconteceporque,nonossocaso, HEADestáapontadoparaoúl-
timocommitefetuado.
Porém,nãoésempreassim,jáqueo HEADpodeapontarparacom-
mitsanteriores.
Verificandomudançasjácomitadas
Vamos comitar nossas modificações em index.html com o co-
mando git commit -m "Banner ao abrir pagina" . Seráexibido
algocomo:
[master 2d04ca8] Banner ao abrir a pagina
1 file changed, 1 insertion(+), 1 deletion(-)
44
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 53

CasadoCódigo Capítulo3. Trabalhandocomrepositóriolocal
Também precisamos comitar as alterações em principal.js, que
aindanãoestánaáreadestage. Paraisso,utilizaremosaop ção -a: git
commit -am "Diminuindo intervalo de troca de banner" .Te-
remosnasaídaalgocomo:
[master 8aa07bd] Diminuindo intervalo de troca de banner
1 file changed, 1 insertion(+), 1 deletion(-)
Então,vamosmostrarostrêsúltimoscommitsdemaneiraconcisaatravés
docomando git log -n 3 --oneline .Asaídaserásemelhantea:
8aa07bd Diminuindo intervalo de troca de banner
2d04ca8 Banner ao abrir a pagina
842d2cf Inserindo arquivo principal.js
Agoranãotemosnenhumaaltera çãonãocomitada.Ufa!
Podemosusarocomando git diff paraverificarasdiferen çasentre
doiscommitsespecíficos.Paracompararoquefoialteradononossoúltimo
commitemrela çãoaosdoisanteriores,devemosutilizaro git diff pas-
sandooscódigosdessescommits:
$ git diff 842d2cf..8aa07bd
Observequepassamosocódigodoscommitsseparadosporponto-ponto
( ..).Podemoslerocomadoanteriorcomo:“mostreasmudan çasefetuadas
apartirdocommit842d2cfatéocommit8aa07bd”.
Arespostadessecomandomostraráasaltera çõesqueacabamosdegravar
norepositório:
diff --git a/index.html b/index.html
index b1115c7..4786946 100644
--- a/index.html
+++ b/index.html
@@ -8,7 +8,7 @@
<title>Móveis Ecológicos</title>
<script src="principal.js"></script>
</head>
- <body>
+ <body onload="trocaBanner();">
45
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 54

3.5. Verificandomudançasnosarquivosrastreados CasadoCódigo
<h1>Móveis Ecológicos S. A.</h1>
<h2 id="mensagem"></h2>
diff --git a/principal.js b/principal.js
index 5d114bd..696870a 100644
--- a/principal.js
+++ b/principal.js
@@ -6,5 +6,5 @@ function trocaBanner() {
document.querySelector(’h2#mensagem’).textContent =
banners[bannerAtual];
}
-setInterval(trocaBanner, 2000);
+setInterval(trocaBanner, 1000);
:
Poderíamosobteramesmasaídaatravésdocomando:
$ git diff 8aa07bd~2
Ocomandoanteriorexibeasmudan çasnosarquivosdocommitdecó-
digo 8aa07bdemrela çãoaosdoiscommitsfeitosimediatamenteantes.O
númerodepoisdo ~indicaquantoscommitsanterioresdevemserconside-
radosnacompara ção.Nonossocaso,foramdois.
Apesardeapresentaremamesmasaídanonossocaso,osparâmetros
842d2cf..8aa07bde 8aa07bd ~ 2nãosãoexatamenteequivalentes.
Sehouvessealgumamodifica çãoaindanãocomitada,foraoudentroda
áreadestage,aslinhasalteradastambémseriammostradasnarespostado
comando git diff 8aa07bd ~ 2 .
Jáocomando git diff 842d2cf..8aa07bd nãoexibemodifica ções
aindanãocomitadas,masapenasasmudan çasqueaconteceramentreosdois
commitsespecificados.
Ocomando git status listaosarquivosmodificadoseoconteúdo
daáreadestage.Jáocomando git diff mostradetalhadamentequais
foramessasmodifica ções,alémdepermitirverificarmudan çasentredois
commits.
46
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 55

CasadoCódigo Capítulo3. Trabalhandocomrepositóriolocal
3.6 Removendo arquivos do repositório
Vamosdizerquecriamosumarquivo produtos.htmlcomoseguintecon-
teúdo:
<html>
<body>
<ul>
<li>Móveis de garrafas PET</li>
<li>Móveis de latinhas de alumínio</li>
<li>Móveis de papelão</li>
</ul>
</body>
</html>
Então,informamosaoGitquequeremosrastreá-lo,atravésdocomando
git add produtos.html . Depois,gravamosoconteúdodoarquivono
repositóriocomocomando git commit -m "Página de produtos" .
Mas acabamos percebendo que replicamos o conteúdo do ar-
quivo index.html e, por isso, gostaríamos de remover o arquivo
produtos.html.
Porém,nãobastadeletarmoso produtos.html. Precisamosdeletá-
loeadicionaradele çãonastage,parasóentãoefetuarmosumcommitno
repositório.
Aremo çãodoarquivoeadi çãonastagepodemserrealizadasdeumavez
sóatravésdocomando:
$ git rm produtos.html
Depoisdocomandoanterior,oarquivo produtos.htmlnãoexistirá
mais.Seexecutarmos git status,teremos:
# On branch master
# Changes to be committed:
# (use "git reset HEAD <file>..." to unstage)
#
# deleted: produtos.html
#
47
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 56

3.6. Removendoarquivosdorepositório CasadoCódigo
Observequeadele çãode produtos.htmljáestánaáreadestage,
prontaparasercomitadacomocomando git commit -m "Removendo
página de produtos" .
Sejátivéssemosremovidooarquivo produtos.html,aoexecutarmos
git rm produtos.html ,adele çãodoarquivoseriacolocadanaáreade
stage.
Umaoutramaneiradeadicionaradele çãodeumarquivoàáreadestage
seriaexecutarocomando git add. Porém,essecomandonãopermiteo
usoemarquivosremovidos,anãoserquesejautilizadaaop ção --all.
Adicionandoaremo çãodearquivosaonossográfico,teríamos:
Figura3.3:RemovendoarquivoscomGit
48
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 57

CasadoCódigo Capítulo3. Trabalhandocomrepositóriolocal
Umdetalheimportanteésaberque,apesardeoarquivotersidore-
movido,seuconteúdoficagravadonohistóricodorepositório. Dessa
maneira,épossívelobtermosqualquerarquivoquejáexistiuemnosso
repositório.
Porém,sepordescuidocomitarmosalgumarquivograndeedepois
deletá-lo,nossorepositórionãodiminuirádetamanho,jáqueohistórico
serámantido.Maisadiante,veremoscomolimparnossorepositório,ex-
purgandoarquivosgrandes,utilizandoferramentasapropriadas.
3.7 Renomeando e movendo arquivos
Renomeandoarquivos
Paramanteropadrãodenomenclatura,resolvemosmodificaronomedoar-
quivo estilos.csspara principal.css.
Parafazerisso,teríamosquecriaronovoarquivo,copiarseuconteúdo,
removeroarquivoantigo,adicionandotantoonovoarquivocomoadele ção
doarquivoantigonaáreade stage.
Bastantetrabalho,não?Aindabemqueessetrabalhotodopodeserpou-
padocomocomando:
$ git mv estilos.css principal.css
Seexecutarmosocomando git status,teremos:
# On branch master
# Changes to be committed:
# (use "git reset HEAD <file>..." to unstage)
#
# renamed: estilos.css -> principal.css
#
Podemosobservarqueoarquivoaparececomorenomeadonaáreade
stageeprontoparasercomitado. E,claro,seobservarmosnodiretóriodo
nossorepositório,oarquivofoirealmenterenomeado.
49
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 58

3.7. Renomeandoemovendoarquivos CasadoCódigo
Éinteressantesaberque,setivéssemosrenomeadooarquivodamaneira
maistrabalhosa,oGitiriadetectaronossoobjetivo,depoisquetivéssemos
efetuadostodososcomandosnecessários.IssoaconteceporqueoGitrastreia
oconteúdodosarquivos,nãoapenasonome.
Antesdecontinuarmos,precisamosatualizaronomedoarquivoCSSem
index.html:
<!-- início do arquivo ... -->
<head>
<!-- tags meta ... -->
<link rel="stylesheet" href="principal.css">
<!-- tags title e script ... -->
</head>
<!-- restante do arquivo ... -->
Feitasasaltera ções,podemosgravá-lasnorepositóriocomocomando
git commit -am "Renomeando CSS" .Nasaída,deveaparecer:
[master 27ffd5e] Renomeando CSS
2 files changed, 1 insertion(+), 1 deletion(-)
rename estilos.css => principal.css (100%)
Pronto!Arquivorenomeado!
Movendoarquivos
Esequisermosmoveroarquivo principal.jsparaumsubdiretório
chamado js?
Primeiramente,devemoscriarodiretório js.
Depois,deveríamoscriarumarquivo principal.jsdentrodessenovo
diretório,copiarosconteúdosdoarquivoanterioreadicionaronovodiretó-
rioàáreadestage.Feitoisso,precisaríamosremoveroarquivoatual,adicio-
nandoaremo çãoàstage.Sóentãopoderíamoscomitarasaltera ções.
Todoessetrabalhotambémpodeserpoupadopelocomando git mv:
$ git mv principal.js js/principal.js
Atenção:éimportantequeodiretório jsjátenhasidocriado!
Seexecutarmosocomando git status,teremos:
50
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 59

CasadoCódigo Capítulo3. Trabalhandocomrepositóriolocal
# On branch master
# Changes to be committed:
# (use "git reset HEAD <file>..." to unstage)
#
# renamed: principal.js -> js/principal.js
#
Notequeoarquivo principal.jsfoidescritocomorenomeadoparao
novoarquivo,queestádentrodosubdiretório js.ParaoGit,nãohádiferen ça
entreumarquivomovidoourenomeado.Nofimdascontas,aqueleconteúdo
(oqueéefetivamenterastreado)mudoudelocal.
Vamosatualizaroarquivo index.htmlparaapontarparaalocaliza ção
corretadoarquivo principal.js:
<!-- início do arquivo ... -->
<head>
<!-- tags meta, link e title ... -->
<script src="js/principal.js"></script>
</head>
<!-- restante do arquivo ... -->
Então, comitar as alterações com git commit -am "Movendo
principal.js".Nasaída,deveaparecer:
[master 3dd877f] Movendo principal.js
2 files changed, 1 insertion(+), 1 deletion(-)
rename principal.js => js/principal.js (100%)
Pronto!Arquivomovido!
Incluindoamovimenta çãodearquivosnanossavisualiza ção,ficaríamos
com:
51
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 60

3.8. Desfazendomudanças CasadoCódigo
Figura3.4:RenomeandoemovendoarquivoscomGit
3.8 Desfazendo mudanças
Desfazendomudan çasnãorastreadas
VamosdizerqueodonodaempresaMóveisS.A.ligoudemadrugadadepois
detomarumaseoutras,pedindoparacolocarmosnapáginaprincipal,um
textoumtantopeculiar.
Paraatendê-lo,editamosoarquivo index.html,colocandooseguinte
conteúdonofimdoarquivo:
<!-- inicio do arquivo -->
<p>Móveis baratos pra c*&%$#@!</p>
</body>
</html>
Fizemosaaltera çãosemmuitaconvic ção.Porisso,nãoaadicionamosna
áreadestage.Arespostadeum git status seria:
52
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 61

CasadoCódigo Capítulo3. Trabalhandocomrepositóriolocal
# On branch master
# Changes not staged for commit:
# (use "git add <file>..." to update what will be committed)
# (use "git checkout -- <file>..." to discard changes in working
directory)
#
# modified: index.html
#
no changes added to commit (use "git add" and/or
"git commit -a")
Logodemanhã,odonodaempresaligaarrependido,pedindoparades-
fazermosasaltera ções.
Comopodemosfazerdemaneirafácil?
Devemosexecutaroseguintecomando:
$ git checkout -- index.html
Ocomando git checkout desfazasaltera çõesaindanãorastreadas,
ouseja,queaindanãoestãonaáreadestage,voltandoaoconteúdoanterior
doarquivo.
Apósum git status teríamos:
# On branch master
nothing to commit, working directory clean
Aoverificarmosoconteúdodoarquivo index.html,podemosconsta-
tarqueanossamudan çafoidesfeitaeoarquivoficoucomoconteúdoorigi-
nal,conformeoúltimocommit.
Casohajaalgumamudan çajárastreadanoarquivo,dentrodaáreade
stage,aoexecutarmosocomando git checkout,apenasasaltera ções
indesejadas,foradastage,serãodesfeitas.Asmudan çasquejáestavam
nastagepermanecerão. Serãodesfeitasapenasasaltera ções,queainda
nãotinhamsidorastreadas.
53
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 62

3.8. Desfazendomudanças CasadoCódigo
Eseapagarmosalgumarquivosemquerer?Medo!Desespero!
Vamosdizerqueapagamosoarquivo index.html.
Aoexecutarmosocomando git status,teríamos:
# On branch master
# Changes not staged for commit:
# (use "git add/rm <file>..."to update what will be committed)
# (use "git checkout -- <file>..." to discard changes in working
directory)
#
# deleted: index.html
#
no changes added to commit (use "git add" and/or
"git commit -a")
Quempoderánosajudar?OGit,éclaro.
Podemosutilizarocomando git checkout pararecuperararquivos
removidosacidentalmente:
$ git checkout -- index.html
Pronto!Arquivorecuperado!
Desfazendomudan çasjárastreadas
Esejátivermosrastreadoumamudan çaindesejadanoarquivo?Como
voltaratrás?
Vamos dizer que fizemos a seguinte modificação no fim do arquivo
index.html:
<!-- inicio do arquivo -->
<p>Móveis baratos pra p&%$#!</p>
</body>
</html>
Logodepois,colocamosamudan çanaáreadestagecomocomando git
add index.html.Aoexecutarmoso git status,teríamos:
54
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 63

CasadoCódigo Capítulo3. Trabalhandocomrepositóriolocal
# On branch master
# Changes to be committed:
# (use "git reset HEAD <file>..." to unstage)
#
# modified: index.html
#
Sequisermosapenasremoverdaáreadestageamudan çaefetuadanoar-
quivo index.html,preservandooarquivomodificado,devemosexecutar:
$ git reset -- index.html
Quandoutilizadodessamaneira,apenasinformandoumarquivoquetem
mudançasnaáreadestage,ocomando git reset retiraoarquivodastage
maspreservatudooquefoimodificadonessearquivo.
Aoverificarmosoarquivo index.html,veremosqueasaltera çõesque
fizemosanteriormenteestarãointocadas.
Depoisdeexecutarmosocomando git status,veremosqueasmu-
dançasaparecemforadaáreadestage( Changes not staged for commit):
# On branch master
# Changes not staged for commit:
# (use "git add <file>..." to update what will be committed)
# (use "git checkout -- <file>..." to discard changes in working
directory)
#
# modified: index.html
#
no changes added to commit (use "git add" and/or
"git commit -a")
Seinvocarmosocomando git reset semnenhumparâmetro,se-
rãoretiradostodososarquivosdaáreadestage.Asaltera çõesefetuadas
nessesarquivosserãopreservadas.
Nocasodequerermosdescartartodasasmudan çasnosarquivosaoin-
vocarmos git reset,devemosutilizaraop ção --hard.
55
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 64

3.8. Desfazendomudanças CasadoCódigo
Háumdetalheimportante:aop ção --hardretiratodososarquivosda
áreadestageedesfaztodasasaltera çõesnessesarquivos.Nofimdascontas,
orepositórioficaexatamentenoestadoqueestavanoúltimocommit.
Paratestarmos,vamoscolocarasmudan çasnoarquivo index.html
novamentenaáreadestageexecutando git add index.html .
Então,vamosexecutarocomando:
$ git reset --hard
Deveapareceralgocomo:
HEAD is now at 3dd877f Movendo principal.js
Todososarquivosforamretiradosdaáreadestageetodasasaltera ções
nessesarquivosforamdesfeitas. Podemosconfirmarissoexecutandooco-
mando git status novamente:
# On branch master
nothing to commit, working directory clean
Ouseja,depoisdo git reset --hard ,orepositóriovoltouaficarexa-
tamentecomoestavanoúltimocommit.Nenhumarquivoestarámodificado
eaáreadestageestarávazia.
Desfazendomudan çasjácomitadas
Agora,esejátivermoscomitadoalgumasmodifica çõesequisermosvol-
taratrás?
Por exemplo, se tivermos feito as seguintes mudanças no arquivo
index.html:
<!-- inicio do arquivo -->
<p>Móveis baratos pra b&%$#!</p>
</body>
</html>
Depois,comitamosasaltera ções:
$ git commit -am "Adicionando texto peculiar"
56
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 65

CasadoCódigo Capítulo3. Trabalhandocomrepositóriolocal
Nasaída,teríamosalgocomo:
[master 172691b] Adicionando texto peculiar
1 file changed, 1 insertion(+)
Sequisermosvoltaratrás,desfazendoasaltera çõesnorepositório,pode-
mosutilizarocomando:
$ git revert --no-edit 172691b
Nessecomando,ocódigo 172691brepresentaoúltimocommitefetu-
ado.Seomitirmosaop ção --no-edit,seráabertoumeditordetextopara
editarmosamensagemdonovocommit.
Emvezdepassarocódigodoúltimocommitcomoparâmetroparao
git revert,poderíamosterutilizado HEADque,nonossocaso,aponta
paraoúltimocommit.
Apósexecutaro git revert,teríamoscomorespostaalgoparecido
com:
[master 9274519] Revert "Adicionando texto peculiar"
1 file changed, 1 deletion(-)
Aoverificarmosoarquivo index.htmlveremosqueasaltera çõesdo
últimocommitforamdesfeitas,retornandoàversãoanterior.
Seobservarmosnovamenteohistóricodecommitsdonossorepositório,
comocomando git log -n 2 --oneline ,teremos:
9274519 Revert "Adicionando texto peculiar"
172691b Adicionando texto peculiar
Notequeocomando git revert efetuouumnovocommitcomaver-
sãoanteriordosarquivos.Foiutilizadaamensagem Revertseguidadamen-
sagemdocommitanterior(noexemplo, Revert “ Adicionando texto peculiar”).
57
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 66

3.8. Desfazendomudanças CasadoCódigo
Nocasodepassarmosumcódigodecommitantigo,apenasasaltera-
çõesfeitasnaquelecommitserãodesfeitas.Issoéalgobastantepoderoso!
Imaginequevocêdescubraqueum bugveiodeumaaltera çãodede-
terminadocommitemumconjuntodearquivos.Apenascomum git
revertépossíveldesfazerasaltera çõesqueinseriramo bug.
Porisso,valereiterarquecommitspequenosebemmontadossão
importantesparapodermosutilizarorealpoderdoGit.
Umaoutraformadedesfazeraltera çõesjácomitadaséutilizandooco-
mando git reset seguidodaop ção --hardedeumcódigodecommit.
Sequisermosvoltaraocommitanterioràsaltera çõespeculiaressolicita-
daspelonossocliente,devemosexecutar:
$ git reset --hard 3dd877f
Teríamoscomorespostaalgosimilara:
HEAD is now at 3dd877f Movendo principal.js
Seobservamososarquivos,asúltimasaltera çõesforamdesfeitas.
No histórico do repositório, exibido ao executarmos git log
--oneline,oscommitsdescartadosnãoaparecem:
3dd877f Movendo principal.js
27ffd5e Renomeando CSS
3234100 Removendo página de produtos
65727bb Página de produtos
8aa07bd Diminuindo intervalo de troca de banner
2d04ca8 Banner ao abrir a pagina
842d2cf Inserindo arquivo principal.js
bb229c6 Script de troca de banner
ccff92c Inserindo titulo e diminuindo tamanho da pagina
4a4fdf7 Commit inicial
Aoutilizarmosocomando git reset damaneiraanterior,comaop ção
--hardeumcódigodecommit,ohistóricodorepositórioéreescrito.
58
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 67

CasadoCódigo Capítulo3. Trabalhandocomrepositóriolocal
Porém,éimportantemantermostodasasaltera çõesgravadasnorepositó-
rio,mesmoqueindesejadas.Afinaldecontas,estamosutilizandoumsistema
decontroledeversõesjustamenteparaterumhistóricofieldaevolu çãodo
códigodenossosprojetos.
Porisso,nasrarasocasiõesemqueénecessáriodesfazercommits, reco-
mendamosquesejautilizadoocomando git revert.
Atualizandonossavisualiza çãográficadoqueaprendemos,agoracom
comandosparadesfazermodifica ções,temos:
Figura3.5:Desfazendomudan çascomGit
59
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 68

E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 69

Capítulo4
Trabalhandocomrepositório
remoto
Nossoprojetojápossuiváriosarquivos,etambémalgunscommitsquefi-
zemosparaguardarohistóricodasmodifica çõesrealizadas.Entretanto,to-
dososcommitsestãoregistradosapenaslocalmente,ouseja,unicamenteno
nossocomputador.
Sealgumdianossocomputadorapresentaralgumproblematécnico,e
deixardefuncionar,ouatémesmoseeleforroubado,teríamosumsériopro-
blema,poisjuntocomeleperderíamostambémnossorepositórioeoprojeto.
Podemosadotarumaestratégiaderealizar backupssemanalmentedo
nossorepositório,ouatémesmodiariamente,paraqueassimsempretenha-
mosumacópiadeseguran ça.
Entretanto,essaestratégiaderealiza çãodebackupsédesaconselhadapor
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 70

4.1. Repositórioremoto CasadoCódigo
sertrabalhosaesujeitaafalhas,jáquepodemosnosesquecerderealizaro
backupemalgumdia.
Alémdisso,manterorepositórioapenaslocalmentenostrazoutraques-
tão:comofazerparatrabalharemequipe,comváriosdesenvolvedoresalte-
randoosarquivosdoprojetoeregistrandoessasaltera çõescomcommits?
Certamenteficarcompactandoeenviandoorepositórioparaosoutros
membrosdaequipe,acadanovocommit,nãopareceserumaideiamuito
boa.
4.1 Repositório remoto
Paraevitarosproblemascitadosanteriormentedevemostrabalharcomum
repositórioremoto,quenadamaisédoqueum repositório Gitcriadoem
outrocomputador,chamadode servidor.
Seosdesenvolvedoresdaequipetrabalhamnamesmaempresa,todoseles
vãoestarconectadospelarede. Sendoassim,paracriarmosumrepositório
remoto,devemosprimeiramenteutilizaralgumcomputadordaempresaque
estejaconectadonarede,ecriarorepositórioGitdoprojetonestecomputa-
dor,quepassaráaseroservidorcentraldoprojeto.
Criandoumrepositórioremoto
Acria çãodorepositórioremotoéfeitacomocomando git init,da
mesmamaneiraquefizemosparacriarorepositóriolocal,entretantodeve-
mospassaroparâmetro --bareaocomando:
$ git init --bare moveis-ecologicos.git
Aoexecutarocomando,seráapresentadaumamensagemcomo:
Initialized empty Git repository
in /opt/repositorios/moveis-ecologicos.git/
Oparâmetro --bareserveparaqueoGitnãocrieum working tree(dire-
tóriodetrabalho),impedindoquecommitssejamefetuadosdiretamenteno
servidor.Nonossocasofazsentido,jáqueoscommitsserãorealizadospelos
62
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 71

CasadoCódigo Capítulo4. Trabalhandocomrepositórioremoto
desenvolvedores,localmente,emseuscomputadores,edepoisessescommits
serãoenviadosearmazenadosnorepositórioremoto,localizadonoservidor.
Ao executar o comando git init --bare
moveis-ecologicos.git, o Git criará um novo diretório chamado
moveis-ecologicos.gitcomaseguinteestrutura:
Figura4.1:EstruturadediretóriosdorepositórioGit
Lembre-sede nuncamexernessesarquivosediretórios,poiselesrepre-
sentamorepositórioGitedevemsermanipuladosapenaspeloGit.
4.2 Adicionando o repositório remoto
Agoraqueorepositórioremotojáfoicriadonoservidor,épossívelenviaros
commitsefetuadosnonossorepositóriolocalparaorepositórioremoto.Mas
antesdissoprecisamos,dealgumamaneira,indicaraoGitondeestálocali-
zadoorepositórioremoto.
ParaensinaraoGitondeseencontraonossorepositórioremoto,devemos
utilizarocomando git remote add ,noqualinformamoso endereçodo
repositórioremoto.
Supondo que o nosso servidor esteja na rede com o endereço IP
192.168.10.99,eorepositórioremotodonossoprojetotenhasidocriado
nodiretório /opt/repositorios/moveis-ecologicos.git,paraadi-
cionarmosorepositórioremotodevemosexecutarocomando git remote
adddaseguintemaneira:
63
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 72

4.2. Adicionandoorepositórioremoto CasadoCódigo
$ git remote add servidor
file://192.168.10.99/opt/repositorios/moveis-ecologicos.git
Aoexecutarocomando git remote add devemosinformaro name
(nome)dorepositórioremotoesua url(endereço).
Noexemploanterior,o namedorepositórioadicionadofoi servidorea
urlfoifile://192.168.10.99/opt/repositorios/moveis-ecologicos.git.
Épossíveladicionarmaisdeumrepositórioremoto,desdequecadaum
tenhaseu namedistinto.Istopodeserútilseprecisarmosenviaroscommits
paramaisdeumservidor.
Listandoosrepositóriosremotos
Paralistarosrepositóriosremotosqueforamadicionadosdevemosutili-
zarocomando git remote:
$ git remote
servidor
Masreparequeéexibidoapenaso namedosrepositóriosremotos.Para
quetambémsejaexibidaa urldevemosadicionaroparâmetro -vaoco-
mando:
$ git remote -v
servidor file://192.168.10.99/opt/repositorios/
moveis-ecologicos.git (fetch)
servidor file://192.168.10.99/opt/repositorios/
moveis-ecologicos.git (push)
Observequeorepositórioremotofoilistadoduasvezes. Issoacontece
poisoGitpermitequetenhamosduas URLsdistintasparaomesmoreposi-
tórioremoto,sendoumaparaleitura( fetch)eoutraparaescrita( push).Isto
podeserútilseprecisarmosutilizarprotocolosdistintosparaleituraeescrita.
Alterandoeremovendoosrepositóriosremotos
Épossívelalteraro namedeumrepositórioremotoutilizandoocomando
git remote rename :
64
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 73

CasadoCódigo Capítulo4. Trabalhandocomrepositórioremoto
$ git remote rename servidor outronome
$ git remote
outronome
O que aconteceria se alguém alterasse o endereço IP do servidor de
192.168.10.99para 192.168.10.110? Teríamosumproblema,pois
nossorepositórioremotoestariaapontandoparaoendere çoantigo. Deve-
mosnessecasoalterara urldorepositórioremoto,eistoéfeitocomoutro
comando,o git remote set-url ,passandocomoparâmetroo namedo
repositórioremotoeanova url:
$ git remote -v
servidor file://192.168.10.99/opt/repositorios/
moveis-ecologicos.git (fetch)
servidor file://192.168.10.99/opt/repositorios/
moveis-ecologicos.git (push)
$ git remote set-url servidor
file://192.168.10.110/opt/repositorios/moveis-ecologicos.git
$ git remote -v
servidor file://192.168.10.110/opt/repositorios/
moveis-ecologicos.git (fetch)
servidor file://192.168.10.110/opt/repositorios/
moveis-ecologicos.git (push)
4.3 Enviando commits para o repositório re -
moto
Agoraquejáadicionamosorepositórioremoto,podemos,enfim,enviaros
commitsparaoservidor.
Paraenviaroscommitslocais,queaindanãoexistemnoservidor,de-
vemosutilizarocomando git push,informandoo namedorepositório
remoto,nonossocaso servidor,seguidode master:
$ git push servidor master
Seráexibidaumamensagemcomo:
65
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 74

4.4. Clonandoorepositórioremoto CasadoCódigo
Counting objects: 3, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (2/2), 227 bytes | 0 bytes/s, done.
Total 2 (delta 1), reused 0 (delta 0)
To file://192.168.10.99/opt/repositorios/moveis-ecologicos.git/
e573bbb..8a2481d master -> master
Pronto!Agoraoscommitsjáforamenviadosparaoservidor.
Apalavra masterqueutilizamosnocomandoanterioréonome
da branchprincipaldonossorepositório. Estudaremosbranchescom
profundidademaisadiante.
4.4 Clonando o repositório remoto
Nossoprojetocontinuaacrescerenãoparamdechegarmaispedidosdefun-
cionalidades.Tivemosquecontratarmaisumdesenvolvedorparaaequipe,
eelejáestáprontoparacome çaradesenvolverasnovasfuncionalidadesdo
sistema,masparaissovaiprecisar,primeiramente,obterumacópiadorepo-
sitóriocomtodososarquivosecommits.
ParaobtermosumacópiadeumrepositórioGit,devemosutilizaroco-
mando git clone informandoaURLdorepositórioaserclonado:
$ git clone file://192.168.10.99/opt/repositorios/
moveis-ecologicos.git
Seráexibidaumamensagemcomo:
Cloning into ’projeto’...
remote: Counting objects: 8, done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 8 (delta 1), reused 0 (delta 0)
Receiving objects: 100% (8/8), 618.32 KiB | 0 bytes/s, done.
Resolving deltas: 100% (1/1), done.
Checking connectivity... done.
66
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 75

CasadoCódigo Capítulo4. Trabalhandocomrepositórioremoto
Aoexecutarocomandoanterior, oGitcriaráumdiretóriochamado
moveis-ecologicos,queseráumacópialocaldorepositórioremoto,con-
tendotodososarquivoseohistóricodoscommitsrealizados.
Porpadrão,oGitcriaráumdiretóriocomomesmonomedorepositório,
etambémjáadicionaráumrepositórioremotocomoname origin,que
apontaparaaURLclonada.
4.5 Sincronizando o repositório local
Apósclonarorepositóriodoprojeto,onovodesenvolvedorfinalizouuma
dasnovasfuncionalidades,realizandoalgunscommitsparaisso,einclusive
jáenvioutaiscommitsparaoservidor.
Sendoassim,paraquepossamosvisualizarasaltera çõesecommitsrea-
lizadospelonovodesenvolvedor,devemos sincronizaronossorepositório
localcomoservidor, puxandoosnovoscommitsparaonossorepositório
local.
Asincroniza çãodorepositóriolocalcomoservidoréfeitacomousodo
comando git pull,ondedevemosinformaro namedorepositórioremoto
quequeremossincronizar,eo nomedabranchlocalaseratualizada:
$ git pull servidor master
Seráexibidaumamensagemcomo:
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 2 (delta 1), reused 0 (delta 0)
Unpacking objects: 100% (2/2), done.
From file://192.168.10.99/opt/repositorios/moveis-ecologicos
* branch master -> FETCH_HEAD
8a2481d..61131f4 master -> servidor/master
Updating 8a2481d..61131f4
Fast-forward
promocoes.html | 0
1 file changed, 0 insertions(+), 0 deletions(-)
create mode 100644 promocoes.html
67
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 76

4.6. ProtocolossuportadospeloGit CasadoCódigo
Agoranossorepositóriolocalestáatualizado,ejáépossívelvisualizaras
alteraçõesecommitsefetuadospelonovodesenvolvedor.
Repositório centralizado ou distribuído
OGitéumsistemadecontroledeversãodistribuído,eporissonão
dependedeumservidorcentral,diferentementedoCVSeSVN.Con-
formevistonocapítuloanterior,podemostrabalharapenascomorepo-
sitóriolocal.
Entretanto,conformevistonestecapítulo,épossíveltrabalharcomo
Gitdemaneiracentralizada,ondeumservidorseráorepositóriocentral,
recebendooscommitsdetodososdesenvolvedores,eestes,porsuavez,
sincronizandoseusrepositórioslocaiscomoservidor,frequentemente,
paraobterosnovoscommits.Estaéamaneiramaiscomumdeutiliza ção
doGit.
4.6 P rotocolos suportados pelo Git
QuandoadicionamosouclonamosumrepositórioGit,devemosinformara
urldorepositório,queutilizaalgumprotocoloparacomunica çãoetransfe-
rênciadedados.
OGitsuportaquatroprotocolosparacomunica çãoetransferênciadeda-
dos:
• Local
• SSH
• Git
• HTTP/HTTPS
Protocololocal
Oprotocololocalfoioutilizadonestecapítulo. Elepodeserutilizado
quandoorepositórioremotoestiverlocalizadonomesmocomputadorem
68
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 77

CasadoCódigo Capítulo4. Trabalhandocomrepositórioremoto
queseencontraorepositóriolocal,ouemoutrocomputadorqueestejaco-
nectadonamesmarede.
Autiliza çãodoprotocololocaléfeitacomousodoprefixo file://na
URLdorepositórioaserclonado:
$ git clone file:///opt/repositorios/moveis-ecologicos.git
Épossívelomitiroprefixo file://naURL,bastandoapenasinformar
ocaminhodorepositório:
$ git clone /opt/repositorios/moveis-ecologicos.git
Asvantagensdautiliza çãodoprotocololocalsãoasuasimplicidade,eo
usodaspermissõesexistentesdeacessoaarquivosediretórios. Jáumadas
desvantagenséadificuldadedeconfigura çãoparaacessoexternoàrede.
ProtocoloSSH
OprotocoloSSHé,provavelmente,omaisutilizado,porserrápido,se-
guro,simplesdeconfigurareporsuportartantoaleituraquantoaescritade
dados.
O uso do protocolo SSH é feito com a URL seguindo o padrão
usuario@servidor:/caminho/repositorio.git.Porexemplo:
$ git clone root@192.168.10.99:/opt/repositorios/
moveis-ecologicos.git
ProtocoloGit
OGitpossuiumprotocolopróprio,queésimilaraoSSH,massemome-
canismodeautentica ção.Porcontadisso,eleacabasendomaisrápido;entre-
tantonãoéseguro,eseuusoéapenasparaleitura.
ParaclonarumrepositórioutilizandooprotocoloGit,aURLdevepossuir
oprefixo git://:
$ git clone git://192.168.10.99/opt/repositorios/
moveis-ecologicos.git
69
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 78

4.6. ProtocolossuportadospeloGit CasadoCódigo
ProtocoloHTTP/HTTPS
O Git também suporta o protocolo HTTP, que é bastante utilizado
quandoestamostrabalhandoemempresasquepossuemumcontrolerígido
deseguran ça,eaporta22,utilizadapeloprotocoloSSH,ébloqueada.
ParaclonarumrepositórioutilizandooprotocoloHTTP,aURLdevepos-
suiroprefixo http://:
$ git clone http://192.168.10.99/opt/repositorios/
moveis-ecologicos.git
TambémépossívelutilizaroprotocoloHTTPS,queadicionaumaca-
madadeseguran çasobreoHTTP,comautiliza çãodoprotocoloSSL/TLS:
$ git clone https://192.168.10.99/opt/repositorios/
moveis-ecologicos.git
70
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 79

Capítulo5
Hospedandoorepositóriono
GitHub
Nocapítuloanterior,vimoscomoutilizarumrepositórioremoto,paraque
tenhamosfacilidadeaotrabalharemequipenoprojeto. Agora,sempreque
umnovomembrodaequipefortrabalharnoprojeto,eledeveprimeiramente
clonarorepositório,efetuarasaltera çõesnecessárias,comitartaisaltera ções,
eentãoenviaroscommitsparaorepositórioremoto.
Assimsendo,vimosqueautiliza çãodeumrepositórioremotonosajuda
aterumamelhororganiza çãoparatrabalharemequipeemumprojeto,além
detambémfuncionarcomobackup.
Entretanto,comoorepositórioremotoestálocalizadoemumservidor
daempresa,ficamoslimitadosaefetuarasincroniza çãoapenasdentrodela,
poisprecisaremosestarconectadosàredelocalparaconseguirmosacessaro
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 80

5.1. Serviçosdehospedagemdeprojetos CasadoCódigo
servidor.
Sealgumdiaumdesenvolvedorprecisarsincronizarasaltera çõescomo
repositórioremotodeforadaempresa,porexemplodecasa,issonãovaiser
possível,poiselenãovaiestarconectadoàredelocal.
Atéépossívelacessararedelocaldaempresaexternamente,maspara
issoseránecessárioconfigurarumaVPN(Virtual Private Network),ouliberar
acessoexternoaoservidorviaSSH,oquepodeseralgocomplicadodese
fazer,alémdetambémpoderserproibidoporalgumasempresas,devidoa
políticasdeseguran ça.
Oidealseriaqueorepositórioremotoestivesseacessívelpelainternet,
poisassimpoderíamosacessá-lodequalquerlugardomundo,bastandoape-
nasestarmosconectadosàinternet.
5.1 Serviços de hospedagem de projetos
Existemalgunsservi çosparahospedagemdeprojetosnainternet,queper-
mitemautiliza çãodeferramentasdecontroledeversão.Aideiaéquevocê
possahospedarseusprojetos,juntamentecomosrepositórios,nainternet,e
assimserápossívelacessá-losdequalquerlugardomundo.
Dentreosprincipaisservi çosquesuportamoGit,estão:
• GitHub
• Bitbucket
• GoogleCode
5.2 GitHub: a rede social dos desenvolvedores
Criadoem2008porTomPreston-Werner,ChrisWanstrathePJHyett,com
oobjetivodesimplificarocompartilhamentodeprojetos,oGitHubéhojeo
maiorservi çodehospedagemderepositóriosdeprojetos,contendo,atual-
mente,maisde3milhõesdeusuáriosemaisde12milhõesderepositórios.
72
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 81

CasadoCódigo Capítulo5. HospedandoorepositórionoGitHub
Figura5.1:LogotipodoGitHub
Éoprincipalservi çoutilizadopelosdesenvolvedoresqueutilizamoGit.
VáriosprojetosimportantesestãohospedadosnoGitHub,dentreeles:
• jQuery
• RubyonRails
• Node.js
• Django
• Bootstrap
OGitHubétambémumaferramentacolaborativa,poisnospermitein-
teragirnosrepositórios,pormeiodealgumasfuncionalidadescomo:
• IssueTracker:paracriaçãoegestãodebugsemilestonesdoprojeto;
• PullRequests:paraqueoutrosusuáriospossamenviarseuscommits
comaltera çõesnoprojeto,oucommitscomcorre çõesdebugs;
• CommitComments:paraqueosusuáriospossamcomentarediscutir
sobreasmodifica çõesnocódigo,deumdeterminadocommit.
Alémdisso,noGitHubépossívelcriar organizações,edentrodelascriar
equipes,paraqueentãosejapossívelvinculardeterminadosusuáriosadeter-
minadasequipes,bemcomovincularasequipesaosrepositóriosemqueelas
73
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 82

5.3. Encontrandoprojetosevisualizandoocódigo-fonte CasadoCódigo
vãotrabalhar.Issoémuitoútilparaempresasquepossuemmuitosprojetose
muitoscolaboradores,poispermiteumamelhororganiza ção.
Porcontadessasfuncionalidadeseporpermitirumamaiorcolabora ção
nosrepositórios,oGitHubéconsideradopormuitoscomoumaespéciede
redesocial paradesenvolvedores.
5.3 Encontrando projetos e visualizando o
código-fonte
VamosacessarositedoGitHubevisualizarocódigo-fontedealgumprojeto
opensource.Paraisso,bastaabrirumnavegadoreacessaroendere ço:http:
//github.com
Figura5.2:PáginainicialdoGitHub
EssaéapáginainicialdoGitHub,nelapodemosefetuarlogin,cadastrar
umnovousuário,fazerbuscaseacessaralgunslinksinteressantes.
Notopodapáginaexisteumcampodetexto,usadoparapesquisarpor
repositóriosouusuários.Vamospesquisarpelorepositóriodo jQuery,uma
famosabibliotecadeJavaScript,bastandoparaissodigitarapalavra jquery
nocampodetextoeapertaratecla Enter.
74
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 83

CasadoCódigo Capítulo5. HospedandoorepositórionoGitHub
Figura5.3:Campoparapesquisarporrepositórios
Apósrealizarapesquisa,seráapresentadaumapáginacomoresultado,
listandotodososrepositóriosquepossuamnonomeounadescri çãoapalavra
jquery.
Figura5.4:Páginacomoresultadodapesquisa
Vamosselecionaroprimeiroresultado,quenocasoéoprojeto jQuery
queestamosbuscando.
Figura5.5:LinkparaorepositóriodojQuery
75
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 84

5.3. Encontrandoprojetosevisualizandoocódigo-fonte CasadoCódigo
NapáginadorepositóriodojQueryépossívelnavegarpelocódigo-fonte,
visualizaradescri çãodoprojeto,oscommits,osusuáriosquecontribuem
paraoprojeto,eatémesmobaixarorepositóriocompactadoemumarquivo
zip.
Figura5.6:PáginadorepositóriodojQuery
Visualizandooscommitsdoprojeto
Vamosagoravisualizarosúltimoscommitsrealizadosnoprojeto. Para
isso,bastaclicarnolink commits:
Figura5.7:LinkparaapáginadecommitsdojQuery
Seráapresentadaumapáginalistandoosúltimoscommitsefetuadosno
76
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 85

CasadoCódigo Capítulo5. HospedandoorepositórionoGitHub
projeto,ondetambémépossívelnavegarporcommitsmaisantigos.Visuali-
zarestapáginaseriacomoexecutarocomando git log norepositório.
Figura5.8:PáginadecommitsdojQuery
Aoclicaremalgumdoscommits,seráapresentadaumapáginadedeta-
lhamento,ondepodemosvisualizarasaltera çõesefetuadas,similaraquando
executamosocomando git diff:
77
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 86

5.3. Encontrandoprojetosevisualizandoocódigo-fonte CasadoCódigo
Figura5.9:Páginadedetalhamentodecommit
Visualizandoocódigo-fontedoprojeto
Devoltaàpáginaprincipaldorepositório, agoravamosnavegarpelo
código-fonte. Jánapáginaprincipaldorepositórioépossívelvisualizaros
arquivosediretóriosdoprojeto.Vamosnavegarpelodiretório src:
78
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 87

CasadoCódigo Capítulo5. HospedandoorepositórionoGitHub
Figura5.10:Diretóriosdorepositório
Serãoexibidostodososarquivosesubdiretóriosexistentes,epodemos
detalharalgumdeles,porexemplooarquivo ajax.js:
79
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 88

5.4. CriandoumusuárionoGitHub CasadoCódigo
Figura5.11:Detalhamentodeumdosarquivosdorepositório
Alémdeserexibidotodoocódigo-fontedoarquivo,nessapáginatam-
bémépossívelvisualizartodososusuáriosquejáefetuaramcommitscom
modificaçõesnestearquivo.
5.4 Criando um usuário no GitHub
Parapodercome çarausaroGitHubecriarosnossosrepositórios,devemos
primeiramentecadastrarumnovousuárionosite.
Atenção! Casovocêjátenhacriadoumusuárioanteriormente,nocapí-
tulo2vocêpodeseguirparaapróximase ção.
Acria çãodeumnovousuárionoGitHubdeveserfeitanapáginainicial
dosite:http://github.com
80
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 89

CasadoCódigo Capítulo5. HospedandoorepositórionoGitHub
Figura5.12:Páginadecria çãodenovousuário
Devemosinformarumnomedeusuário,oe-maileumasenha.Casojá
existaumoutrousuáriocadastradocomomesmonomedeusuárioe/oue-
mailinformado,oGitHubnosmostraráumalertaindicandotalsitua ção,e
sópermitiráquecontinuemosocadastroapósaaltera çãodessa(s)informa-
ção(ões).
Apósinformarosdadoseclicarnobotão SignupforGitHub ,seremos
redirecionadosparaumapáginadeboas-vindas,ondedevemosescolherqual
oplanoasercontratado.
81
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 90

5.4. CriandoumusuárionoGitHub CasadoCódigo
Figura5.13:Páginadeboas-vindaseescolhadoplanodecontrata ção
Planosdecontrata çãooferecidospeloGitHub
OGitHubpossuialgunsplanosquepodemoscontratar,sendoumgra-
tuito,eosoutroscomcustosmensais.
NoplanogratuitodoGitHub,ousuárionãotemnenhumcusto,entre-
tantoelesomentepoderácriarrepositóriospúblicos,ouseja,qualquerpes-
soapoderáencontrarseusrepositórioseinclusiveteracessoaocódigo-fonte.
Esteplanoéidealparausuáriosquequeremcriare/oucolaborarcomprojetos
opensource.
Masmuitasempresaspossuemprojetosquesãorestritos,enãopodem
terocódigo-fonteacessívelaqualquerpessoa.Nestecaso,aempresadeverá
contrataralgumdosplanospagosoferecidospeloGitHub.
Adiferen çaentreosplanospagosestánaquantidadederepositóriospri-
82
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 91

CasadoCódigo Capítulo5. HospedandoorepositórionoGitHub
vadosquepoderãosercriados.Noplanomaisbarato,queatualmentecusta
$7pormês,épossívelcriaraté5repositóriosprivados,enquantoquenoplano
maiscaro,queatualmentecusta $50pormês,essaquantidadederepositórios
privadossobepara50.
Apósescolheroplanoquemaisseadequeàsnossasnecessidades,deve-
mosfinalizarocadastroclicandonobotão Finishsignup ,eseremosredire-
cionadosparaapáginaquemostraosrepositóriosdonossousuárioeoutras
informações.Essapáginaéconhecidacomo Dashboard.
Figura5.14:Páginadedashboard
OGitHubenviaráume-maildeconfirma çãodecadastro,comumlink
paravalida çãoeativa ção. Éimportanteacessarmosesselink,poisassimo
e-mailserávalidadoeassociadoaonossousuário,ealémdisso,todasasno-
tificaçõesdoGitHubserãoenviadasapenasao(s)e-mail(s)cadastrado(s).
5.5 Criando o repositório do projeto
Agoraquetemosumusuáriocadastrado,jáépossívelcriarorepositóriodo
projeto.
ParacriarumnovorepositórionoGitHub,devemosacessaraURLhttp:
//github.com/newouclicarnobotão Newrepository existentenapágina
principal.
83
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 92

5.5. Criandoorepositóriodoprojeto CasadoCódigo
Figura5.15:Páginadecria çãodenovorepositório
Nesta página devemos preencher o nome do repositório no campo
Repository name,e,opcionalmente,preencherumadescri çãonocampo
Description. Apósisso,bastaclicarnobotão Create repository,e
seremosredirecionadosparaapáginaprincipaldorepositório,ondeserão
exibidasasinforma çõesdecomoadicionarorepositórioremoto,parapoder-
mossincronizaroscommitsdonossorepositóriolocal.
84
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 93

CasadoCódigo Capítulo5. HospedandoorepositórionoGitHub
Figura5.16:Páginadonovorepositório
Agorabastaadicionarmosorepositórioremoto,comocomando git
remote add,conformeexibidonapáginadorepositório:
$ git remote add origin
https://github.com/fulanodasilva/moveis-ecologicos.git
5.6 Enviando os commits do projeto para o
GitHub
Comorepositórioremotoadicionado,podemosfinalmenteenviaroscom-
mitsparaoGitHub.
Oenviodoscommitséfeitodamesmamaneiraquevimosnocapítulo
anterior,ouseja,utilizandoocomando git push:
$ git push origin master
Comoutilizamosoprotocolo httpsaoadicionarorepositórioremoto,
semprequeformossincronizarnossorepositóriolocal,oGitnossolicitaráo
usuárioesenhacadastradosnoGitHub.
85
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 94

5.7. ClonandoorepositóriohospedadonoGitHub CasadoCódigo
ApósoGitenviaroscommitsparaorepositórioremoto,seráexibidauma
mensagemcomo:
Counting objects: 8, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (6/6), done.
Writing objects: 100% (8/8), 15.78 KiB | 0 bytes/s, done.
Total 8 (delta 0), reused 0 (delta 0)
To https://github.com/fulanodasilva/moveis-ecologicos.git
* [new branch] master -> master
Seatualizarmosapáginadonossorepositório,veremosqueosarquivos
eoscommitsforamenviadoscomsucesso:
Figura5.17:Páginadorepositórioatualizadacomosarquivosecommits
5.7 Clonando o repositório hospedado no
GitHub
AgoraqueonossorepositórioremotoestáhospedadonoGitHub,osdesen-
volvedoresdaequipepoderãosincronizarseusrepositórioslocaisdequalquer
lugardomundo,nãoficandomaisrestritosasincronizarapenasquandoco-
nectadosnaredelocaldaempresa.
86
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 95

CasadoCódigo Capítulo5. HospedandoorepositórionoGitHub
Paraqueumnovodesenvolvedorobtenhaumacópiadorepositório,ele
agoradeveráclonarorepositórioremotolocalizadonoGitHub:
$ git clone https://github.com/fulanodasilva/
moveis-ecologicos.git
5.8 Colaborando com projetos open source
Conformecitadoanteriormente,existemmilharesdeprojetoshospedadosno
GitHub,sendoquemuitosdestessão opensource,ouseja,significaquequal-
querdesenvolvedorpodecolaborarcommelhoriasecorre çõesdebugs.Mas
comofazerparacolaborarcomtaisprojetos?
Vamossuporquequeremoscolaborarcomalgumprojetoopensource,
porexemplo,o VRaptor,umframeworkMVCparadesenvolvedoresJava.
Figura5.18:PáginadorepositóriodoVRaptor
Primeiramentevamosprecisarclonarorepositório,paratermosacesso
aocódigo-fonte,eentãoefetuarasmelhoriasdesejadas:
$ git clone https://github.com/caelum/vraptor4.git
87
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 96

5.8. Colaborandocomprojetosopensource CasadoCódigo
Pronto! Játemosumacópiadorepositóriocomtodososarquivosdo
projeto.Agorabastaefetuarasmelhoriasdesejadas,registrandoasaltera ções
realizadascomcommits.
Maslembre-sedequeoscommitsrealizadosexistemapenasnonosso
repositóriolocal,precisamosagoraenviá-losparaorepositórioremotodo
projeto,noGitHub,comocomando git push:
$ git push origin master
Entretanto,aexecu çãodocomandoanteriorfalha,gerandoaseguinte
mensagemdeerro:
remote: Permission to caelum/vraptor4.git denied to
fulanodasilva.
fatal: unable to access ’https://github.com/caelum/
vraptor4.git/’:
The requested URL returned error: 403
Oproblemaéqueousuário fulanodasilvanãotempermissãopara
enviarcommitsparaorepositóriodoVRaptor,poisesserepositórionãoper-
tenceaele,massimaousuário caelum.
Pararesolveresseproblema,ousuário caelumpoderiaacessarapágina
deconfigura çõesdorepositórioVRaptornoGitHub,eadicionarousuário
fulanodasilvacomocolaborador.
Masessaabordagemdeveserutilizadaapenasparaadicionarosusuários
quefazempartedaequipededesenvolvimentodoprojeto,ouseja,apenasos
desenvolvedoresquetrabalhamefetivamentenoprojeto.Dessaforma,acaba
sendoinviávelterqueadicionarumnovousuáriocomocolaboradortodavez
queumnovodesenvolvedorquisercolaborarcomoprojeto.
Alémdisso,apartirdomomentoemqueadicionamosumusuáriocomo
colaborador,elepassaaterpermissãodeenviarcommitsparaorepositório
semrestri ções,oquepodeserarriscado,poisnãoháumaavalia çãoprévia
dasaltera çõesqueforamrealizadas.
88
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 97

CasadoCódigo Capítulo5. HospedandoorepositórionoGitHub
Pullrequests
Asolu çãodoGitHubparaacolabora çãocomprojetosopensource,foi
umafuncionalidadechamadade pullrequests.
Primeiramente,devemosacessarapáginadoprojetoquequeremoscola-
borarnoGitHub,nonossocasohttp://github.com/caelum/vraptor4,eclicar
nobotão Fork:
Figura5.19:BotãoparafazeroforkdoVRaptor
Aoclicarnobotão Fork,oGitHubcriaráumacópiadorepositóriodo
VRaptornonossousuáriodoGitHub:
Figura5.20:PáginadorepositóriodoVRaptorpertencenteaonossousuário
ReparequeagoraonossousuáriodoGitHubpossuiumrepositóriocha-
mado vraptor4,ouseja,esserepositórioéa nossaversãodoprojeto.
Opróximopassoéclonarorepositórioapartirdo nossousuáriodo
GitHub,enãodousuário caelum,poisassimconseguiremosrealizaro push
doscommitslocaisparaonossorepositórionoGitHub:
$ git clone https://github.com/fulanodasilva/vraptor4.git
89
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 98

5.8. Colaborandocomprojetosopensource CasadoCódigo
Agora,apósrealizarasaltera çõesecommitsnoprojeto,conseguiremos
realizaro pushnormalmente,poisorepositórioremotonoGitHubpertence
aonossousuário.
Entretanto,oscommitsforamenviadosapenasparao nossorepositório
noGitHub.
Paraqueoscommitssejamintegradosaorepositóriooriginaldoprojeto,
nocasoorepositório vraptor4dousuário caelum,devemosenviarum
PullRequest paraousuário caelum,solicitandoquesejafeitoum pulldos
nossoscommits.
Paracriarum Pull Request devemosacessarapáginadonossorepo-
sitórionoGitHub,clicarnolink PullRequests,eemseguidaclicarnobotão
Newpullrequest :
Figura5.21:PáginacomlinkparagerenciarPullrequests
Figura5.22:PáginacombotãoparacriarumnovoPullrequest
Seremosredirecionadosparaapáginadecria çãodopullrequest,naqual
serãolistadososcommitsealtera çõesrealizados.Paraconfirmaracria çãodo
pullrequest,bastaclicarnobotão Create pull request :
90
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 99

CasadoCódigo Capítulo5. HospedandoorepositórionoGitHub
Figura5.23:Páginacombotãoparaconfirmaracria çãodopullrequest
Apóscriarmoso pull request,ousuário caelumreceberáumanoti-
ficaçãodoGitHub,epoderáefetuaro pulldosnossoscommits,integrando-
osaorepositóriooriginaldoprojeto.Claro,issoapósumaanálisedasaltera-
çõesefetuadasemnossoscommits.
Pronto!Esseéoprocessoutilizadopelosdesenvolvedoresquecolaboram
comprojetosopensourcehospedadosnoGitHub.
91
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 100

E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 101

Capítulo6
Organizandootrabalhocom
branches
Nossoclientenãoestásatisfeitocomo designdapágina. Convenhamos,a
páginaquecriamosnãoestádasmaisbonitasdomundo:
Figura6.1:Designdapáginadeixaadesejar
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 102

6.1. Abranchmaster CasadoCódigo
Sabemosumpouquinhosobredesign,masprecisamosdealgumassema-
nasfocadasnamelhoriadovisual.
Mastemosumproblema: nossoclientecontinuapedindoparaalterar-
mosoconteúdodapágina,váriasvezesporsemana.Alémdisso,temosque
corrigir bugscomoerrosdeportuguês,linksincorretosetc. Esabemosque
todasessasasmudan çastêmqueserpublicadasdeimediato.
Sepublicarmosositeenquantoonovodesignestásendodesenvolvido,
teremosumapáginapelametade.Eprecisamosdetempoparaexperimentar
algumaspossibilidades.Eagora?
Trabalhandoemparalelocombranches
Amaioriadossistemasdecontroledeversãopermitetrabalhoempara-
leloatravésdebranches.Uma branchéumalinhaindependentededesenvol-
vimentoemquepodemoscomitarnovasversõesdocódigosemafetaroutras
branches.
Emmuitossistemasdecontroledeversão,utilizarbrancheséalgobas-
tantelentoetrabalhoso.Porém,aestruturainternadoGitpermitelidarmos
combranchesdemaneiramuitorápidaeleve.
6.1 A branch master
Vamosnoscertificardequeestamosnonossorepositório moveis,execu-
tando cd ~/moveis emumterminal.
Paralistarasbranchesdonossorepositório, devemosexecutaroco-
mando:
$ git branch
Teremoscomoresposta:
* master
Peraí!Foimostradaumabranchchamada master,mesmosemtermos
criadosnenhumabranch...IssoocorreuporqueoGitpossuiporpadrãouma
branchprincipalchamada master.Todososnossoscommitsatéagoraocor-
reramnessabranchprincipal.
94
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 103

CasadoCódigo Capítulo6. Organizandootrabalhocombranches
Observequeabranch mastertemumasterisco(*)nafrente.Issoindica
queéabranchatual,emqueestamostrabalhando.
NoGit,todabranchébasicamenteumapontadorparaumcommit. A
cadanovocommitquefazemos,abranchémovidaautomaticamente,pas-
sandoaapontarparaessenovocommit. Porisso, porpadrão, abranch
masterapontaparaoúltimocommitquefizemos.
Sequisermoslistarasbranchesexistentesnonossorepositóriocomos
commitsassociados, poderíamosutilizaraop ção -vdocomando git
branch:
$ git branch -v
Aresposta,nonossocaso,seria:
* master b92285b Revert "Adicionando texto peculiar"
Antesdecontinuarmos,éimportantesabermosumadasinforma çõesque
umcommitarmazena,ocommitpai,queéoquefoiefetuadoanteriormente.
Naverdade,umcommitpodeterváriospais,oqueveremosadiante.
Podemosobservaroscommitscomseusrespectivospaisexecutandoo
comando git log comaop ção --parents.
Jáparaverificarmosocommitparaoquala masterestáapontando,
passamosaop ção --decorateparaocomando git log.
Juntando as opções, podemos executar git log --oneline
--decorate --parents para exibir o histórico resumido do nosso
repositóriocomocommitparaoquala masterestáapontadoeoscommits
paidecadacommit.Teríamosumasaídaparecidacom:
b92285b a5b9fce (HEAD, master) Revert "Adicionando texto
peculiar"
a5b9fce 2259f55 Adicionando texto peculiar
2259f55 d211fac Movendo principal.js
d211fac 515da0a Renomeando CSS
515da0a e9ca4c6 Removendo página de produtos
e9ca4c6 793e567 Página de produtos
793e567 0f2b749 Diminuindo intervalo de troca de banner
0f2b749 7e1c195 Banner ao abrir pagina
95
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 104

6.2. Criandoumabranch CasadoCódigo
7e1c195 9a20490 Inserindo arquivo principal.js
9a20490 83b60c3 Script de troca de banner
83b60c3 1a02a4f Inserindo titulo e diminuindo tamanho da pagina
1a02a4f Commit inicial
Observequearespostadocomandoanteriorapresentatrêscolunas: o
códigodocommit,ocódigodopaieamensagemdocommit. Porexem-
plo,podemosverqueopaidocommit d211fac(“RenomeandoCSS”)foio
commit 515da0a(“Removendopáginadeprodutos”).
Notetambémquenossoprimeirocommit,odecódigo 1a02a4f,possui
apenasduascolunas,indicandoqueessecommitnãopossuiumpai.
Alémdisso,podemosverqueabranch masterapontaparaoúltimo
commit,decódigo b92285b.Nãosepreocupecomo HEAD,jáqueveremos
aseguirseusignificado.
Umavisualiza çãodonossohistóricodecommitsdabranch masterse-
ria:
Figura6.2:Abranchmaster
6.2 Criando uma branch
Paracriarmosumabranchchamada designparatrabalharmosnamelhoria
dodesignbastaexecutarmos:
$ git branch design
Nãoseráexibidanenhumaresposta.
Selistarmosasbranchescomocomando git branch,teremos:
96
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 105

CasadoCódigo Capítulo6. Organizandootrabalhocombranches
design
* master
Agoratemosduasbranches!
Notequeabranchatualcontinuasendoa master,queestádestacada
comumasterisco(*). Ocomando git branch apenascriaumanova
branch,masnãomudaparaabranchcriada.
Anovabranchqueacabamosdecriar( design)apontaparaomesmo
commitqueabranchqueestávamosanteriormente( master).Podemosve-
rificarissocomocomando git branch -v :
design b92285b Revert "Adicionando texto peculiar"
* master b92285b Revert "Adicionando texto peculiar"
MasondeoGitguardaainforma çãodequaléabranchatual? Aíque
entrao HEAD,queéumapontadorespecialqueindicaqualéabranchna
qualestamostrabalhando.
Visualizandoonossorepositóriologoapósacria çãodabranch design,
teríamos:
Figura6.3:AbranchdesigneoHEAD
97
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 106

6.3. Trocandodebranch CasadoCódigo
6.3 Trocando de branch
Jácriamosnossabranch designmasaindaestamosna master.Paratro-
carmosparaabranchrecentementecriada,devemosexecutar:
$ git checkout design
Deveaparecercomoresposta:
Switched to branch ’design’
Depoisdeexecutarocomandoanterior,o HEADpassaaapontarparaa
novabranch design.
Seexecutarmosocomando git branch -v ,teremos:
* design b92285b Revert "Adicionando texto peculiar"
master b92285b Revert "Adicionando texto peculiar"
Observequeoasterisco(*)queindicaabranchatualfoimudadaparaa
branch design. Ambasasbranchescontinuamapontandoparaomesmo
commit.
Visualizandooestadodonossorepositório,teríamos:
Figura6.4:HEADapontandoparadesign
98
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 107

CasadoCódigo Capítulo6. Organizandootrabalhocombranches
Conformevimosnocapítulo3,ocomando git checkout,alémde
trocarabranchatual,tambémpodeserusadoparadescartarmudan ças
deumarquivoqueaindanãoestãonaáreadestage.Paradescartarmos
asmudan çasdoarquivo index.html,porexemplo,devemosexecutar
git checkout -- index.html .
Naverdade,aop ção --nãoéestritamentenecessária.Porém,éuma
boaprática,jáqueserveparainformarquesetratadeumarquivo.Dessa
maneira,ajudaaevitarproblemascasoumabranchtenhaomesmonome
dealgumarquivo.
Criandoejátrocandoparaumanovabranch
Nossoclientepediuquenóscome çássemosaconstruirumalojaonline
paravendadosmóveis.Seriaalgodemorado,delongoprazo.Porisso,cons-
truiríamosalojaonlineumanovabranch,chamada loja.
Criarumabranch lojacom git branch sóparadepoismudarpara
anovabranchcom git checkout éalgotedioso.
Seriainteressantejácriarmosemudarmosparaanovabranch lojade
umasóvez.Podemosfazerissopassandoaop ção -bparaocomando git
checkout:
$ git checkout -b loja
Asaídaapresentadaseria:
Switched to a new branch ’loja’
Selistarmosasbranchescom git branch -v ,teríamos:
design b92285b Revert "Adicionando texto peculiar"
* loja b92285b Revert "Adicionando texto peculiar"
master b92285b Revert "Adicionando texto peculiar"
Notequeoasterisco(*)estánabranch loja,indicandoqueessaéa
branchatual. Ea lojafoicriadaapontandoparaocommit b92285b,o
mesmodasoutrasbranches.
99
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 108

6.4. Deletandoumabranch CasadoCódigo
6.4 D eletando uma branch
Masnãotemostempoparacriarumalojaonline...Temosquenosfocarnas
nossastarefasatuais.
Comonãovamosusarabranch lojaporumbomtempo,seriabom
removê-la.Assim,evitamosconfusõesedesperdíciononossorepositório.
Nãoépossívelremoverumabranchenquantoestivermosnela.Porisso,
devemosirparaoutrabranch.Parairparaabranch master,devemosexe-
cutar git checkout master .
Paradeletarumabranch,devemosutilizaraop ção -ddocomando git
branch:
$ git branch -d loja
Deveaparecerumamensagemcomoaseguir:
Deleted branch loja (was b92285b).
Abranch lojafoideletada.Nossorepositórioestálimpoecristalino!
Sejátivéssemosfeitoalgumcommitnabranch loja,aoexecutarmos
git branch -d loja teríamoscomoresposta:
error: The branch ’loja’ is not fully merged.
If you are sure you want to delete it, run ’git branch -D loja’.
Nãoépossíveldeletarcomaop ção -dumabranchquepossuicommits
aindanãoaplicadosemoutrasbranches(veremoscomomesclarbranches
maisadiante).
Pararemovermosabranch lojasetivermosfeitoalgumcommit,deve-
mosutilizaraop ção -D:
$ git branch -D loja
Teríamosnasaída:
Deleted branch loja (was b92285b).
Agorasim!Oscommitsdabranch lojaseriamdescartadoseabranch
seriaremovida.
100
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 109

CasadoCódigo Capítulo6. Organizandootrabalhocombranches
6.5 Comitando código em uma nov a branch
Decidimosutilizarumaferramentaparaauxiliarnamelhoriadodesign: o
Bootstrap.
Aprimeiracoisaécertificar-nosqueestamosnabranch design,execu-
tando git checkout design .
Depoisdisso,vamosalteraro index.html,trocandonossoCSSfeio
peloCSSdoBootstrapecolocandooatributo classemalgumastags:
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<meta name="description" content="Móveis ecológicos">
<meta name="keywords" content="moveis ecologicos">
<link rel="stylesheet"
href="http://netdna.bootstrapcdn.com/bootstrap/3.1.1/
css/bootstrap.min.css">
<title>Móveis Ecológicos</title>
<script src="js/principal.js"></script>
</head>
<body onload="trocaBanner();">
<div class="container">
<div class="jumbotron">
<h1>Móveis Ecológicos S. A.</h1>
<h2 id="mensagem"></h2>
<ul class="list-group">
<li class="list-group-item">
Móveis de garrafas PET
</li>
<li class="list-group-item">
Móveis de latinhas de alumínio
</li>
<li class="list-group-item">
Móveis de papelão
</li>
</ul>
</div>
</div>
101
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 110

6.5. Comitandocódigoemumanovabranch CasadoCódigo
</body>
</html>
Apenascomessaspequenasaltera ções,embelezamosumbocadonossa
página:
Figura6.5:Páginaembelezada
TambémvamosremoveronossoCSSantigo,paranãoficarmoscomcó-
digoobsoleto,executandoocomando git rm principal.css .
Agora,vamosadicionaràáreadestageasaltera çõesecomitá-lascomo
comando git commit -am "Adicionando Bootstrap" .
Nasaída,seráimpresso:
[design 8f53065] Adicionando Bootstrap
2 files changed, 23 insertions(+), 19 deletions(-)
delete mode 100644 principal.css
Observenotextoanteriorquefoiexibidoonomedabranch design,em
queestamoscomitando.
Ao executarmos o comando git log -n 3 --oneline
--decorate --parents,teríamos:
8f53065 b92285b (HEAD, design) Adicionando Bootstrap
b92285b a5b9fce (master) Revert "Adicionando texto peculiar"
a5b9fce 2259f55 Adicionando texto peculiar
102
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 111

CasadoCódigo Capítulo6. Organizandootrabalhocombranches
Notequeabranch masteraindacontinuaapontandoparaocommitde
código b92285b(Revert“Adicionandotextopeculiar”).
Jáabranch designpassouaapontarparaonovocommit,decódigo
8f53065(AdicionandoBootstrap). Observetambémqueo HEADaponta
paraomesmocommit.
Umgráficorepresentandoonossocommitnabranch designseria:
Figura6.6:Commitnabranchdesign
6.6 Voltando para o master e fazendo uma al -
teração
Aindanãoacabamosdeembelezaranossapágina,masnossoclientenosligou
pedindoquemodificássemosostextosdobanner.Epediuquepublicássemos
urgentementeasaltera ções!
Aprimeiracoisaquedevemosfazerévoltarparaabranch master,exe-
cutandoocomando git checkout master .
Visualizandooestadodonossorepositórionesseponto,teríamos:
103
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 112

6.6. Voltandoparaomasterefazendoumaaltera ção CasadoCódigo
Figura6.7:Voltandoàbranchmaster
Agoraqueestamosnabranch master,vamosalterarostextosdobanner
noarquivo principal.js:
var banners = ["Do lixo ao luxo!","Reaproveitar é aproveitar!"];
//restante do arquivo
Em seguida, vamos comitar nossas alterações com o comandogit
commit -am "Alterando textos do banner" .Teríamosnasaída:
[master 2223859] Alterando textos do banner
1 file changed, 1 insertion(+), 1 deletion(-)
Nesseponto,nossorepositórioestariaparecidocom:
104
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 113

CasadoCódigo Capítulo6. Organizandootrabalhocombranches
Figura6.8:Novocommitnamaster
Notequeabranch masterestáapontandoparaocommit 2223859que
acabamosderealizar.Jáabranch designcontinuaapontandoparaomesmo
commitqueestavaanteriormente.
Poderíamosentãopublicarcomrapidezosnovosbannerssemasmodi-
ficaçõesdedesign,queaindanãoforamaprovadas.
6.7 Mesclando alterações
Mostramosonovodesignparaonossoclienteeelegostoubastante. Pediu
paracolocarmosnoaroquetemosagora.Eomaisrápidopossível!
Temosduasaltera ções:osnovostextosdobanner,queestãonabranch
master,eoembelezamentodapágina,queestánabranch design.
Porisso,precisamosmesclarasaltera çõesquefizemosnabranch design
comasquefizemosna master.Identificaroquemudou,copiandoecolando
namãoéumtrabalhorazoável,comaltachancedeinserirmosumerro.Ainda
bemqueoGitvainosajudarafazerisso!
105
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 114

6.7. Mesclandoalterações CasadoCódigo
Verificandobranchesaindanãomescladas
Considerandoqueestamosnabranch master, podemosverificaras
branchesaindanãomescladascomaop ção --no-mergeddocomando git
branch:
$ git branch --no-merged
Teríamosaseguintesaída:
design
Issoindicaquehámudan çasaindanãomescladasnabranch design.
Ocomando git branch tambémtemaop ção --merged.Seexecu-
tássemosgit branch --merged ,teríamos:
* master
Mesclandoaltera çõescommerge
Parajuntarmostodasasaltera çõesquefizemosnabranch designcom
asdabranch master,mesclandoasduas,podemosutilizarocomando:
$ git merge design -m "Mesclando com a branch design"
Seráexibidaumarespostasemelhanteàseguinte:
Removing principal.css
Merge made by the ’recursive’ strategy.
index.html | 31 +++++++++++++++++++++++--------
principal.css | 11 -----------
2 files changed, 23 insertions(+), 19 deletions(-)
delete mode 100644 principal.css
Pronto! Mudan ças mescladas! Ao executarmos o comandogit
branch --no-merged, nãoteríamosnenhumaresposta, indicandoque
nãohánenhumabranchnãomesclada.
Noteque,depoisdomerge,oarquivo principal.cssfoiremovidoe
asaltera çõesquetínhamosrealizadoem index.htmlforamtrazidaspara
106
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 115

CasadoCódigo Capítulo6. Organizandootrabalhocombranches
anossabranchatual,a master.Observetambémqueostextosdobanner
quemodificamoscontinuamlá.
Senãotivéssemosinformadoumamensagematravésdaop ção -m,seria
abertoumeditordetexto.
Éimportantesaberque,quandoéefetuadoummerge,écriadoumnovo
commitcomasaltera çõesqueestamosmesclandoecomamensagemque
informamos.
Podemosverificaressenovocommitdemergeexecutandoocomando
git log -n 4 --oneline --decorate --parents . Teríamos na
saída:
e6b2f35 2223859 8f53065 (HEAD, master) Mesclando com a branch
design
2223859 b92285b Alterando textos do banner
8f53065 b92285b (design) Adicionando Bootstrap
b92285b a5b9fce Revert "Adicionando texto peculiar"
Observequeabranch mastereo HEADapontamparaocommitde
merge,queéoúltimocommitrealizado,equetemocódigo e6b2f35ea
mensagemquehavíamosinformado.
Jáabranch designcontinuaapontandoparaomesmocommitquees-
tavaanteriormente.
Éimportantenotarqueocommitdemerge( e6b2f35)temdoiscommits
pai: ocommit 2223859,demensagem“Alterandotextosdobanner”,eo
commit 8f53065,demensagem“AdicionandoBootstrap”.
Visualizandooestadodonossorepositóriodepoisdomergedabranch
designnabranch master,teríamos:
107
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 116

6.7. Mesclandoalterações CasadoCódigo
Figura6.9:Mergededesignnamaster
Háumasituaçãoemqueum git merge nãoirágerarumcommit
demerge:quandoabranchdedestinonãotevenenhumcommitamais
desdequeabranchasermescladafoicriada.
Nonossocaso,senãotivéssemosfeitoocommit 2223859(Alte-
randotextosdobanner)nabranch master,omergecomabranch
designseriabasicamenteapontara masterparaondea design
aponta:ocommit 8f53065(AdicionandoBootstrap).
Essetipodemergeéchamadode fast-forward.
Épossívelevitarousodefast-forward,for çandoacria çãodeumcom-
mitdemerge,utilizandoaop ção --no-ffdocomando git merge.
Mesclandoaltera çõescomrebase
Àmedidaqueumaaplica çãovaisendodesenvolvida,énaturalisolarmos
partesdotrabalhoembranches.Equandoalgoestiverpronto,seráfeitoum
mergedocódigoe,porisso,teremosumnovocommitdemerge.
Paraprojetoscommuitasbranchesemuitosmerges,ohistóricodorepo-
sitórioficarárepletodecommitsdemerge.Issopodetornarbastantetraba-
108
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 117

CasadoCódigo Capítulo6. Organizandootrabalhocombranches
lhosastarefascomorevisãodecódigo.
Háumamaneira alternativademesclarasaltera çõesdeduasbranches
quesimplificaohistóricodoprojeto.Considerandoqueestamosnabranch
master,emvezdeutilizar git merge,épossívelutilizar:
$ git rebase design
Nasaída,deveapareceralgocomo:
First, rewinding head to replay your work on top of it...
Applying: Alterando textos do banner
Pronto!Outramaneiradetermosasmudan çasmescladas!Arespostado
comando git branch --no-merged seriavazia,jáquenãohánenhuma
branchnãomesclada.
Asmensagensanterioresinformamqueorepositóriofoirebobinadoe
nossotrabalhorefeito.
Nonossocaso,orepositóriovoltouaoestadoqueestavaaocriarmosa
branch designapartirda master.
Depoisdisso,foiaplicadoocommitquefizemosnabranch design.
Finalmente,foiaplicadoonossoúltimocommitna master,asaltera ções
notextodosbanners.
Aoverificarmosohistóricodonossorepositóriocomocomando git
log -n 3 --oneline --decorate --parents ,teríamos:
c05c05a 8f53065 (HEAD, master) Alterando textos do banner
8f53065 b92285b (design) Adicionando Bootstrap
b92285b a5b9fce Revert "Adicionando texto peculiar"
Abranch designcontinuaapontandoparaocommitqueestavaanteri-
ormente.
Jáabranch masterteveseuhistóricorefeito:foicriadoum novocommit
comasaltera çõesnotextodosbanners,comcódigo c05c05a.
Observequeopaidonovocommit c05c05a(Alterandotextosdoban-
ner)éocommit 8f53065(AdicionandoBootstrap),quetínhamosfeitona
branchdesign.
109
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 118

6.7. Mesclandoalterações CasadoCódigo
Percebaquenãohouvecommitdemerge. Ohistóricodecommitsfoi
linearizado.
Colocandooestadodonossorepositórioapósorebaseemumgráfico,
teríamos:
Figura6.10:Rebasededesignnamaster
Nocasodeumfast-forwardbastaapontarabranchdedestinoparao
commitmaisnovodabranchsendomesclada.
Nonossocaso,senãotivéssemosnenhumnovocommitnabranch
master,amesclagemseriafeitaapontandoa masterparaomesmo
commitparaoquala designaponta.Dessaforma,orebasenãopreci-
sariareescreverohistóricodecommits.
Porisso,o git merge eo git rebase têmomesmoefeitoquando
háumfast-forward.
Mantendoohistóricodamasterintactoapósumrebase
Evitaraomáximoaltera çõesnohistóricoda masteréumapráticabas-
tanteadotadaporusuáriosdoGit.
Porém, nosso rebase anterior acabou deixando obsoleto o commit
2223859 (Alterando textos do banner), substituindo-o pelo commit
c05c05a,quetemomesmoconteúdo.
110
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 119

CasadoCódigo Capítulo6. Organizandootrabalhocombranches
Poderíamosterfeitoaintegra çãodasbranches mastere designcom
rebasedemaneiraadeixar masterintactasetivéssemosfeitonossotrabalho
deumamaneiraligeiramentediferente.
Primeiramente,teríamosquepassarparaabranch designcomoco-
mando git checkout design .
Então,faríamosorebasedabranch masterna designcomocomando
git rebase master .
Apósorebase,ocommit 8f53065(AdicionandoBootstrap)dabranch
designfoisubstituído,digamos,pelocommitdecódigo e887c10.
Visualizandograficamentenossorepositórionessemomento,teríamos:
Figura6.11:Rebasedemasternadesign
Écomoserefizéssemosocommitbasedabranch design,ocommitda
branch masterqueéancestraldocommitquefizemosem design(ede
todosquevirão).
Antesdorebase,ocommitbaseeraodecódigo b92285b(Revert“Adi-
cionandotextopeculiar”).
Depoisqueorebasefoiexecutado,ocommitbasepassouaseroúltimo
commitda master,decódigo 2223859(Alterandotextosdobanner).
Onome rebasevemdaideiaderefazerocommitbasedeumabranch.
111
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 120

6.7. Mesclandoalterações CasadoCódigo
Paraisso,oGitprecisacriarnovoscommits,mudandoosancestraisdecom-
mitsanteriores.
Comabasedabranch designrefeita,épossívelfazerummergedotipo
fast-forwardda designnabranch master. Paratal,deveríamosirpara
a masterexecutando git checkout master .Então,faríamosum git
merge design.Ográficodorepositórioficariaparecidocom:
Figura6.12:Mergefast-forwarddedesignnamaster,apósorebase
Parasabermais:Qualusar?Ummergeouumrebase?
Utilizarmergemantémumregistrofieldoqueocorreucomonossore-
positório,masoscommitsdemergecomplicamtarefascomonavegarpelo
códigoantigoerevisarcódigonovo.
Jáorebasesimplificaohistórico,masperdemosinforma çãosobrenosso
repositórioealgunscommitssãoreescritos. Nocasodeconflitos,ascoisas
podemficarespecialmentecomplicadas.
Nãoháumarespostasimplessobreamaneiraidealdemesclarmosalte-
raçõescomGit.Cadasolu çãotemseusprósecontras.
Aotrabalharmoscombranchesremotas,nossopróximoassunto,surgem
novasquestões.
112
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 121

Capítulo7
Trabalhandoemequipecom
branchesremotas
Nadiaadia,dificilmentetrabalhamossozinhos.Nocapítulo4vimoscomo
trabalharcomrepositóriosremotosenocapítulo5vimoscomoutilizaro
GitHub,oquenospermitetrabalharemequipedemaneiraconsistente.
Trabalharcombranches,quevimosnocapítulo6,tambéméumaboa
maneiradeorganizarotrabalhoemequipe. Masquandotrabalhamoscom
repositóriosremotos,surgemnovaspreocupa ções.
Lembrandodosrepositóriosremotos
Nonossorepositóriolocal moveis,temosoremote originqueaponta
paraoGitHub,oquepodemosverificarcomocomando git remote -v :
origin git@github.com:fulanodasilva/moveis-ecologicos.git
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 122

7.1. Branchesremotas CasadoCódigo
(fetch)
origin git@github.com:fulanodasilva/moveis-ecologicos.git
(push)
Oremote originestáapontandoparaumrepositórioládoGitHub,que
tambémtemsuabranch master.Precisamosdeumamaneiraderecebere
enviarcommitsparaabranch masterdoGitHub.
7.1 Branches remotas
NoGit,temos branchesremotas queapontamparabranchesqueestãonos
repositóriosremotosconfigurados.
Paradiferenciá-lasdasbrancheslocais,onomedeumabranchremota
éonomedoremoteseguidodonomedabranch. Nonossocaso,abranch
masterládoGitHubtemonomede origin/master,jáqueoremote
originapontaparaoGitHub.
Aocontráriodebrancheslocais,quesãomovidasacadacommit,bran-
chesremotassósãomovidasaofazermosopera çõesqueenvolvamcomu-
nicaçãoderedecomo git push, git pull etambémocomando git
fetch,queveremosmaisadiante.Portanto,umabranchremotarepresenta
asitua çãodaúltimavezquehouvecomunica çãocomorepositórioremoto.
Podemoslistarasbranchesremotaspassandoaop ção -rparaocomando
git branch:
$ git branch -r
Teremosnasaída:
origin/master
Sequisermosmostrartantoasbrancheslocaiscomoasremotas,po-
demosutilizarocomando git branch -a .
Paravermosparaquaiscommitsasbranchesremotasestãoapontando,
podemosutilizarocomandoanteriorcomaop ção -v:
114
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 123

CasadoCódigo Capítulo7. Trabalhandoemequipecombranchesremotas
$ git branch -r -v
Teremos:
origin/master b92285b Revert "Adicionando texto peculiar"
Observequeabranch origin/masterestáapontandoocommitde
código b92285b(Revert“Adicionandotextopeculiar”).
Considerandoquefizemosomergedabranch mastercomabranch
designnorepositóriolocalnocapítulo6,aoexecutarmosocomando git
log -n 4 --oneline --decorate --parents ,teríamos:
e6b2f35 2223859 8f53065 (HEAD, master) Mesclando com a branch
design
2223859 b92285b Alterando textos do banner
8f53065 b92285b (design) Adicionando Bootstrap
b92285b a5b9fce (origin/master) Revert "Adicionando texto
peculiar"
Observequeabranch origin/masterapontaparaumcommitanterior
àsbranches mastere origindorepositóriolocal.
ExibindográficoscomorepositórioládoGitHubeorepositóriolocal,
cadaumcomsuasbranches,ficaríamoscomalgoparecidocom:
Figura7.1:OrepositóriodoGitHubnãocontémabranchdesign,apenasasua
master
115
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 124

7.2. Compartilhandobranches CasadoCódigo
Figura7.2:Repositóriolocaltemasbrancheslocaismasteredesignearemota
origin/master
Nofimdascontas,tantoabranch masterládoGitHubcomoanossa
branch origin/masterapontamparaocommitdecódigo b92285b(Re-
vert“Adicionandotextopeculiar”).
7.2 Compartilhando branches
Abranch designaindanãoexistelánoGitHub.Paracompartilhá-ladeve-
mosinformarosnomesdoremoteedabranchparaocomando git push:
$ git push origin design
Deveráaparecerumarespostaparecidacom:
Counting objects: 5, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 669 bytes | 0 bytes/s, done.
Total 3 (delta 1), reused 0 (delta 0)
To git@github.com:fulanodasilva/moveis-ecologicos.git
* [new branch] design -> design
Ocomandoanteriorenviaparaoremote originoscommitsdabranch
design.
116
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 125

CasadoCódigo Capítulo7. Trabalhandoemequipecombranchesremotas
Depoisdisso,podemosverabranch designnapáginadonossoprojeto
noGitHub.
Tambémpodemosverumgráficodasbranchesdorepositóriona
URLhttps://github.com/fulanodasilva/moveis-ecologicos/network(não
esqueçadetrocar fulanodasilvapeloseuusuário.)
Nessemomento,selistarmosasbranchesremotaselocaiscomocomando
git branch -a -v ,teríamos:
design 8f53065 Adicionando Bootstrap
* master e6b2f35 Mesclando com a branch design
remotes/origin/design 8f53065 Adicionando Bootstrap
remotes/origin/master b92285b Revert "Adicionando texto
peculiar"
Observequetemosasbrancheslocais mastere designeasbranches
remotas origin/mastere origin/design.
Comoacabamosdefazero git push dabranch origin/design,essa
branchremotaeabranchlocal designestãoapontandoparaocommitde
código 8f53065(AdicionandoBootstrap).
Jáabranchlocal masterearemota origin/masterestãoapontando
paracommitsdiferentes.
ColocandooestadoatualdosnossosrepositórioslocaledoGitHubem
gráficos,teríamos:
117
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 126

7.3. Obtendonovasbranchesremotasemoutrosrepositórios CasadoCódigo
Figura7.3:BranchdesignnoGitHub
Figura7.4:Branchremotaorigin/designnorepositóriomoveis
7.3 Obtendo nov as branches remotas em outros
repositórios
Parasimularumoutromembrodonossotime,vamosbaixarorepositório
emumaoutrapasta.
Primeiramente,devemosvoltarànossapastapessoal,executando cd ~.
118
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 127

CasadoCódigo Capítulo7. Trabalhandoemequipecombranchesremotas
Então, vamos clonar o repositório em um diretório
chamado outro, executando o comando git clone
git@github.com:fulanodasilva/moveis-ecologicos.git
outro.
Depoisdeclonarorepositório,éimportanteentrarnodiretório,como
comando cd outro.
Selistarmosasbrancheslocaiseremotascomocomando git branch
-a -v,teremos:
* master b92285b Revert "Adicionando texto
peculiar"
remotes/origin/design 8f53065 Adicionando Bootstrap
remotes/origin/master b92285b Revert "Adicionando texto
peculiar"
Notequetemosabranchlocal mastereasremotas origin/master
e origin/design.
Porém,nãotemosaindaumabranchlocal design.Seprecisarmostra-
balharnessabranchnonovorepositório outro,precisamosexecutarose-
guintecomando:
$ git checkout -b design origin/design
Ocomandoapresentaránasaídaalgocomo:
Branch design set up to track remote branch design from origin
by rebasing.
Switched to a new branch ’design’
Comocomandoanterior,fizemosum git checkout deumanova
branchlocalchamada designapartirdabranchremota origin/design.
Agoraestamosprontosparatrabalharnodesigndaaplica ção,sequiser-
mos.
Brancheslocaiscriadasapartirdebranchesremotassãochamadasde
tracking branches.
Seexecutarmos git branch -a -v novamente,teremos:
119
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 128

7.3. Obtendonovasbranchesremotasemoutrosrepositórios CasadoCódigo
* design 8f53065 Adicionando Bootstrap
master b92285b Revert "Adicionando texto
peculiar"
remotes/origin/design 8f53065 Adicionando Bootstrap
remotes/origin/master b92285b Revert "Adicionando texto
peculiar"
Umaoutramaneira,maissucinta,decriarumatrackingbranchéuti-
lizaraop ção -tdocomando git checkout.
No nosso caso, faríamosgit checkout -t origin/design .
Seriacriadalocalmenteatrackingbranch designrelacionadacoma
branchremota origin/design.
Depoisdecriadaatrackingbranch designnorepositório outro,os
repositóriosmoveiseodoGitHubestariaminalterados.
Sevisualizarmosorepositório outro,teríamos:
Figura7.5:Trackingbranchdesignnorepositóriooutro
120
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 129

CasadoCódigo Capítulo7. Trabalhandoemequipecombranchesremotas
7.4 Enviando commits para o repositório cen -
tral
Vamosvoltarparanossodiretório moveis, executandoocomando cd
~/moveis.
Nossorepositório moveisestádoiscommitsnafrentedabranchremota
origin/master.
Podemosverificarissoexecutando git status:
On branch master
Your branch is ahead of ’origin/master’ by 2 commits.
(use "git push" to publish your local commits)
nothing to commit, working directory clean
Seexecutarmos, git log -n 4 --oneline --decorate ,teremos:
e6b2f35 (HEAD, master) Mesclando com a branch design
2223859 Alterando textos do banner
8f53065 (origin/design, design) Adicionando Bootstrap
b92285b (origin/master) Revert "Adicionando texto peculiar"
Então,paraenviarasaltera çõesnabranch masterparaorepositório
remoto,devemosfazer:
$ git push origin master
Teremoscomorespostaalgocomo:
Counting objects: 10, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (5/5), done.
Writing objects: 100% (6/6), 670 bytes | 0 bytes/s, done.
Total 6 (delta 3), reused 0 (delta 0)
To git@github.com:fulanodasilva/moveis-ecologicos.git
b92285b..e6b2f35 master -> master
Depoisdisso,abranch masterea origin/masterestarãoapontando
paraocommitdemerge e6b2f35(Mesclandocomabranchdesign). É
possívelnoscertificarmosdisso,executando git log -n 4 --oneline
--decoratenovamente.Teríamos:
121
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 130

7.4. Enviandocommitsparaorepositóriocentral CasadoCódigo
e6b2f35 (HEAD, origin/master, master) Mesclando com a branch
design
2223859 Alterando textos do banner
8f53065 (origin/design, design) Adicionando Bootstrap
b92285b Revert "Adicionando texto peculiar"
Jánorepositório outro,abranch masteraindacontinuaapontando
paraocommit b92285b(Revert“Adicionandotextopeculiar”)eabranch
designcontinuaapontandoparaocommit 8f53065(AdicionandoBoots-
trap).
Orepositório outronãosofreualtera ções.Jáumavisualiza çãodoesta-
dosdorepositórios moveisedoGitHubseria:
Figura7.6:CommitsdemoveisforamrecebidospelorepositóriodoGitHub
122
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 131

CasadoCódigo Capítulo7. Trabalhandoemequipecombranchesremotas
Figura7.7:Branchorigin/masterfoiatualizadanorepositóriomoveis
7.5 Obtendo commits de uma branch remota
Umnovocommit
Digamosqueoutrodesenvolvedordanossaequipeestejatrabalhandoem
umapáginaquelistamóveisfeitosapartirdegarrafasPET.Todotrabalho
estásendofeitodiretamentenabranch master.
Parasimularesseoutrodesenvolvedor, vamosutilizarnossorepositó-
rio outro. Retornaremosaesserepositório,executandoocomando cd
~/outro.
Então,vamosnoscertificarqueestamosnabranch master,executando
git checkout master .
Feitoisso,vamoscriarumarquivo moveis_pet.htmlcomoseguinte
conteúdo:
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<meta name="description"
content="Móveis ecológicos PET">
123
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 132

7.5. Obtendocommitsdeumabranchremota CasadoCódigo
<meta name="keywords" content="moveis ecologicos pet">
<link rel="stylesheet" href="principal.css">
<title>Móveis Ecológicos de garrafas PET</title>
</head>
<body>
<h1>Móveis Ecológicos S. A.</h1>
<h2>Móveis de Garrafas PET</h2>
<p>Funcionais, baratos e amigos do meio ambiente.</p>
<ul>
<li>Sofás</li>
<li>Racks</li>
<li>Cadeiras</li>
<li>Mesas</li>
</ul>
</body>
</html>
Comoarquivo moveis_pet.htmlcriado,vamosrastreá-locom git
add moveis_pet.html egravá-lonorepositóriocom git commit -m
"Adicionando página sobre móveis PET" .
Semostramosohistóricodorepositórionessepontocom git log -n
2 --oneline --decorate ,teríamos:
e1b10ff (HEAD, master) Adicionando página sobre móveis PET
b92285b (origin/master) Revert "Adicionando texto peculiar"
Reparequeabranch origin/masterdorepositório outroestáno
commit b92285b(Revert“Adicionandotextopeculiar”),apesardabranch
masterládoGitHubestaralgunscommitsnafrente,nocommit e6b2f35
(Mesclandocomabranchdesign).
Orepositório moveiseodoGitHubcontinuaramiguais.Jásevisuali-
zarmosoestadodorepositório outroapósocommit,teríamos:
124
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 133

CasadoCódigo Capítulo7. Trabalhandoemequipecombranchesremotas
Figura7.8:Branchmasterdorepositóriooutroapontandoparaonovocom-
mit
Trazendocommitsdeumrepositórioremotocomfetch
Paraobtermososcommitsdabranchremota origin/masternonosso
repositório outro,podemosexecutarocomando:
$ git fetch origin
Teremoscomorespostaalgocomo:
remote: Counting objects: 6, done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 6 (delta 1), reused 0 (delta 0)
Unpacking objects: 100% (6/6), done.
From github.com:fulanodasilva/moveis-ecologicos
b92285b..e6b2f35 master -> origin/master
Comocomando git fetch,trazemososcommitsdeumabranchre-
motaqueaindanãoestavampresenteslocalmente.
Nonossocaso,obtemososcommits 2223859(Alterandotextosdoban-
ner)e e6b2f35(Mesclandocomabranchdesign)queestavamlánoGitHub
masaindanãoestavamnabranch origin/master.
125
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 134

7.5. Obtendocommitsdeumabranchremota CasadoCódigo
Porém,osnovoscommitsdabranchremota origin/masteraindanão
foramaplicadosnabranchlocal master,oquepodemosconstatarexecu-
tandoocomando git branch -a -v :
design 8f53065 Adicionando Bootstrap
* master e1b10ff Adicionando página sobre móveis
PET
remotes/origin/design 8f53065 Adicionando Bootstrap
remotes/origin/master e6b2f35 Mesclando com a branch design
Observequeabranch masteraindacontinuaapontandoparaocom-
mit e1b10ff(AdicionandopáginasobremóveisPET).Éimportantenotar
queosnovoscommits ainda não foram aplicadosapósexecutarmoso git
fetch.
Depoisdeobteroscommitsdabranch origin/master,ográficodo
repositório outroficaria:
Figura7.9:Commitsremotosobtidosnabranchorigin/masterdeoutro
126
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 135

CasadoCódigo Capítulo7. Trabalhandoemequipecombranchesremotas
7.6 Mesclando branches remotas e locais
Mesclandobranchesremotaselocaiscommerge
No repositório outro, temos alguns commits na branch remota
origin/masterqueaindanãoforamaplicadosnabranch master.
Comofazerparamesclarasduasbranches?Seráquemesclarumabranch
remotaaumalocalprecisadealgumcomandoespecial?
Não!BastausarmosumadasduasmaneirasdemesclarbranchesnoGit:
ummergeouumrebase.
Seescolhermosfazerummergeeestivermosnabranch master,basta
executarmos:
$ git merge origin/master -m "Mesclando origin/master em master"
Senãoinformarmosumamensagemparaocommitdemerge,será
abertoumeditordetexto.
Nasaída,teríamos:
Removing principal.css
Merge made by the ’recursive’ strategy.
index.html | 29 +++++++++++++++++++++--------
js/principal.js | 2 +-
principal.css | 11 -----------
3 files changed, 22 insertions(+), 20 deletions(-)
delete mode 100644 principal.css
Pronto! JátemosasmudançasládoGitHubaplicadasnabranchlocal
masterdorepositório outro.
Se executarmos git log -n 6 --oneline --decorate
--parents,teremos:
550e27d e1b10ff e6b2f35 (HEAD, master) Mesclando origin/master
em master
e1b10ff b92285b Adicionando página sobre móveis PET
127
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 136

7.6. Mesclandobranchesremotaselocais CasadoCódigo
e6b2f35 2223859 8f53065 (origin/master) Mesclando com a branch
design
2223859 b92285b Alterando textos do banner
8f53065 b92285b (origin/design, design) Adicionando Bootstrap
b92285b a5b9fce Revert "Adicionando texto peculiar"
Senãohouvessenenhumnovocommitnabranchlocal masterdo
repositório outro,a masterteriaum fast-forward,sendosimples-
mentemovidaparaapontarparaomesmocommitdabranchremota
origin/master.
Nenhumaaltera çãoteriaacontecidonorepositório moveisedoGitHub.
Agora,umgráficodohistóricoanteriordorepositório outroseria:
Figura7.10:Mergedeorigin/masternabranchmasterdorepositóriooutro
Mesclandobranchesremotaselocaiscomrebase
Aalternativaaomergeseriaumrebasedabranch origin/masterna
128
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 137

CasadoCódigo Capítulo7. Trabalhandoemequipecombranchesremotas
branch master.Paraisso,devemosexecutar:
$ git rebase origin/master
Teríamoscomoresposta:
First, rewinding head to replay your work on top of it...
Applying: Adicionando página sobre móveis PET
Asmudan çasládoGitHubforamaplicadasnabranchlocal masterdo
repositório outro,masnãohouvecommitdemerge.
Ohistóricodorepositóriofoilinearizado,oquepodemosobservarexe-
cutando git log -n 5 --oneline --decorate --parents :
0f8d4b3 e6b2f35 (HEAD, master) Adicionando página sobre móveis
PET
e6b2f35 2223859 8f53065 (origin/master) Mesclando com a branch
design
2223859 b92285b Alterando textos do banner
8f53065 b92285b (origin/design, design) Adicionando Bootstrap
b92285b a5b9fce Revert "Adicionando texto peculiar"
Observequeocommitcommensagem“Adicionandopáginasobremó-
veisPET”foirefeito,ficandocomocódigo 0f8d4b3,apósseremaplicados
oscommitsde origin/master.
Emgeral,nãoqueremosalterarohistóricodecommitsdabranchlo-
cal master.Masémaisimportanteaindaevitarmudan çasnoscommits
dabranchremota origin/master,queécompartilhadaportodosos
membrosdanossaequipe.
Uma alternativa bastante utilizada é não comitar diretamente na
branchlocal master,masemumaoutrabranchlocalespecíficapara
a funcionalidade sendo desenvolvida. Então, faríamos o rebase da
origin/masternessaoutrabranchlocal,queteriaseuhistóricomo-
dificado.Dessaforma,a masterficariaintacta.
Aofinaldafuncionalidade,abranchlocaldafuncionalidadeteriaum
mergefeitonabranchlocal master.
129
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 138

7.6. Mesclandobranchesremotaselocais CasadoCódigo
Orepositório moveiseodoGitHubnãosofrerammudan ças.Visuali-
zandoasitua çãodorepositório outro,teríamos:
Figura7.11:Rebasedeorigin/masternabranchmasterdorepositóriooutro
Obtendocommitsemesclandodeumavezcompull
Paraobtermosemesclarmososnovoscommitsdeumabranchremota
comumabranchlocalpoderíamosterusadoumcomandosó:
$ git pull
Seráabertoumeditordetextoparaquesejainformadaamensagemdo
commitdemerge.
Nasaída,teremosalgocomo:
remote: Counting objects: 6, done.
remote: Compressing objects: 100% (5/5), done.
Unpacking objects: 100% (6/6), done.
remote: Total 6 (delta 1), reused 0 (delta 0)
From github.com:fulanodasilva/moveis-ecologicos
b92285b..e6b2f35 master -> origin/master
Removing principal.css
Merge made by the ’recursive’ strategy.
index.html | 29 +++++++++++++++++++++--------
js/principal.js | 2 +-
130
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 139

CasadoCódigo Capítulo7. Trabalhandoemequipecombranchesremotas
principal.css | 11 -----------
3 files changed, 22 insertions(+), 20 deletions(-)
delete mode 100644 principal.css
Ocomandoanteriorvaiteromesmoefeitodeum git fetch origin
seguidodeum git merge origin/master .
Sedesejássemosqueo git pull tivesseumefeitoparecidocom git
fetch origin seguidodeum git rebase origin/master ,podería-
mosterpassadoaop ção --rebase:
$ git pull --rebase
Teríamoscomoresposta:
remote: Counting objects: 6, done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 6 (delta 1), reused 0 (delta 0)
Unpacking objects: 100% (6/6), done.
From github.com:fulanodasilva/moveis-ecologicos
b92285b..e6b2f35 master -> origin/master
First, rewinding head to replay your work on top of it...
Applying: Adicionando página sobre móveis PET
Parasabermais:Qualusar?Umpullouumpull --rebase?
Usar git pull ou git pull --rebase aomesclarcommudan ças
remotaséumaquestãoparecidacomadesedevemosusar git merge ou
git rebase paramesclagenslocais.
Ocomando git pull,nãopassadeum git fetch seguidodeum
git merge.Porisso,temosasmesmasvantagensedesvantagensdomerge,
masagoraconsiderandorepositóriosremotos. Comovantagem,temosum
registrofieldoqueaconteceuemcadarepositóriodanossaequipe,comos
commitsexatos.Mas,comodesvantagem,osvárioscommitsdemergecom-
plicamoentendimentodohistóricodoprojeto,afetandotarefascomonave-
garporcódigoantigoerevisarcódigonovo.Emtimesgrandes,umhistórico
complicadopodetornarotrabalhobastantedesafiador.
Nafiguraaseguir,háumpequenotrechodohistóricodeumprojetoreal
emqueumdosautorestrabalharam,comdetalhesomitidos.Ficaclaraacon-
fusãoocasionadapeloscommitsdemerge:
131
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 140

7.6. Mesclandobranchesremotaselocais CasadoCódigo
Figura7.12:Commitsdemergeemumprojetoreal
Jáocomando git pull --rebase éum git fetch seguidodeum
git rebase. Ohistóricoélinearizado,simplificandonossotrabalho. Po-
rém,acadarebasealgunscommitssãoreescritose,nofimdascontas,estamos
perdendoinforma çõessobrenossorepositório.Quandoacontecemconflitos,
corrigi-lospodeserbastantecomplicado.
Orebasepodeserespecialmenteproblemáticoseacabarmosmudando
umcommitjácompartilhadocomoutrosmembrosdanossaequipe.Nossos
colegaspodemsofrernahoradeobteroscommitsmodificados,jáqueoGit
podeseperder.
Nãopareceumaboasolu çãousarsempreomergeousempreorebase.
Ummeiotermoparecealgomaissensato!
Nossasugestãoéaseguinte:
• Utilizarumgit pull --rebase paraobtermudan çasremotas.É
umapráticaseguraporquenossosnovoscommitslocaisaindanãofo-
ramcompartilhados,ouseja,outrosmembrosnemsabemdaexistência
dessescommits.Porisso,alterá-losnãotrazgrandesproblemas.
• Aotrabalharmosemumanovafuncionalidadeutilizandoumabranch,
marcamossuaentregafazendoummerge. Assim,conseguimoster
umaboaideiadequandoafuncionalidadecome çouaserdesenvolvida
equandofoireintegradaàbranch master.
132
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 141

CasadoCódigo Capítulo7. Trabalhandoemequipecombranchesremotas
• Seestivermostrabalhandosozinhosnanovafuncionalidade,podemos
fazerrebasesperiódicosda masternanossabranchparaobtercódigo
novo,porémdeixandoohistóricodabranchbemlimpo.
• Éinteressantefazeropushdanossabranchsolitáriaemumrepositório
remoto,parabackup. Maséimportanteevitarquealguémfa çachec-
kout.
Uma discussão detalhada pode ser encontrada em: http://blog.
sourcetreeapp.com/2012/08/21/merge-or-rebase/
7.7 Deletando branches remotas
Vamosdizerquenossoclientesolicitouquefizéssemosumapáginadeconta-
tosquepermiteaousuáriodositeenviodemensagens.
Paraimplementaressasolicita ção,trabalharemosemumanovabranch
chamada contato.Paracriá-laejácome çaratrabalharnela,executamoso
comando git checkout -b contato .Teríamoscomoresposta:
Switched to a new branch ’contato’
Então,vamosiniciarodesenvolvimentocriandoumarquivocomonome
contato.htmlecomoseguintecódigo:
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<title>Entre em contato conosco</title>
</head>
<body>
<h1>Fale com a gente.</h1>
<p>Dúvidas, sugestões ou choramingos</p>
<form>
<label for="nome">Nome</label>
<input id="nome">
<label for="email">Email</label>
<input id="email">
133
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 142

7.7. Deletandobranchesremotas CasadoCódigo
<label for="mensagem">Mensagem</label>
<textarea id="mensagem"></textarea>
<input type="submit" value="Enviar">
</form>
</body>
</html>
Vamosrastrearnossonovoarquivocom git add contato.html e
comitá-locom git commit -m "Iniciando página de contato" .
Massurgiuumanovademandaurgente! Temosqueparardetrabalhar
napáginadecontato.Alguémdonossotimedissequeiriadarseguimento.
Porisso, resolvemoscompartilharnossabranchexecutando: git push
origin contato.
Pronto,abranch contatofoipublicadaetemumacópialánoGitHub.
Aoexecutarmosocomando git branch -a -v ,teríamos:
* contato 3523c62 Iniciando página de contato
design 8f53065 Adicionando Bootstrap
master 0f8d4b3 Adicionando página sobre móveis
PET
remotes/origin/contato 3523c62 Iniciando página de contato
remotes/origin/design 8f53065 Adicionando Bootstrap
remotes/origin/master 0f8d4b3 Adicionando página sobre móveis
PET
Masnossocliente,queéumpoucoindeciso,voltouatrásequissimplificar
oprojeto,parandoodesenvolvimentodapáginadecontatoedeixandoapenas
oe-mailnapáginaprincipal.
Devidoaessamudan çanosrequisitos,resolvemosremovernossabranch
contatomudandoparaabranch masterdonossorepositórioeexecu-
tandoocomando git branch -D contato .
Mas quando executamos o comando anterior, removemos apenas a
branchlocal contato.LánoGitHub,abranch contatocontinuaintacta.
Eanossabranchremota origin/contato,queapontaparaabranchcor-
respondentedoGitHub,tambémcontinuanonossorepositório.
Podemosconstatarissoexecutandonovamenteocomando git branch
-a -v:
134
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 143

CasadoCódigo Capítulo7. Trabalhandoemequipecombranchesremotas
design 8f53065 Adicionando Bootstrap
* master 0f8d4b3 Adicionando página sobre móveis
PET
remotes/origin/contato 3523c62 Iniciando página de contato
remotes/origin/design 8f53065 Adicionando Bootstrap
remotes/origin/master 0f8d4b3 Adicionando página sobre móveis
PET
Pararemovermosdefinitivamenteabranchremota origin/contatoe
abranch contatoládoGitHub,devemosexecutar:
$ git push origin :contato
Teríamosnasaída:
To git@github.com:fulanodasilva/moveis-ecologicos.git
- [deleted] contato
Pronto!SeolharmosnoGitHub,abranch contatonãoaparecemais!
Nocasodabranchládoservidorterumnomediferentedabranch
local,aodeletá-ladevemosutilizaronomedabranchdoservidor.
Por exemplo, se a branch do servidor fosse
contato_do_servidor, deveríamos executargit push origin
:contato_do_servidor.
135
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 144

E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 145

Capítulo8
Controlandoversõesdocódigo
comtags
Mostramosonovodesignparaonossoclienteefoiumsucesso!Nossocliente
pediuquecolocássemosnoaranovaversão,omaisrápidopossível.
Aoliberarmosessanovaversãodositeparaimplanta çãoemprodu ção,é
umaboapráticatirarmosuma fotodocódigonessemomento.Sehouveral-
gumerro,saberemosexatamenteocódigoqueestásendousadoemprodu ção
eserámaisfácilcaçaraorigemdafalha.
Emsistemasdecontroledeversão,essasfotosdeumdeterminadoins-
tantedeumrepositóriosãochamadasde tags.
NoGit,umatagésimplesmenteumapontadorfixoparaumcommites-
pecífico. Aocontráriodebranches,esseapontadornãoavan çacomnovos
commits.
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 146

8.1. Criando,listandoedeletandotags CasadoCódigo
Emgeral,criamostagscomnomescomo v1.0, v1.1, v2.0eassim
pordiante.Cadaequipedevedefiniroseupadrão.
Osnomespermitidosparatagsebranchestêmalgumasrestri ções:
nãopodemconteralgunscaracteresespeciaiscomo ~, ^e :,alémde
sequênciasdecaracterescomo ..e @{.
Os detalhes podem ser obtidos em: http://git-scm.com/docs/
git-check-ref-format.html
8.1 Criando, listando e deletando tags
Paracriarmosumatag v1.0noGit,devemosexecutarocomando:
$ git tag v1.0
Ográficodonossorepositóriolocal outrodepoisdocomandoanterior
ficariaparecidocom:
Figura8.1:Novatagnorepositóriooutro
Sequisermoslistarastagsdonossorepositório,bastaexecutarmos:
$ git tag
Teríamoscomoresposta:
138
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 147

CasadoCódigo Capítulo8. Controlandoversõesdocódigocomtags
v1.0
Severificarmosohistóricodorepositóriocomocomando git log -n
5 --oneline --decorate ,veremos:
0f8d4b3 (HEAD, tag: v1.0, master) Adicionando página sobre
móveis PET
e6b2f35 (origin/master) Mesclando com a branch design
2223859 Alterando textos do banner
8f53065 (origin/design, design) Adicionando Bootstrap
b92285b Revert "Adicionando texto peculiar"
Observequeocommit 0f8d4b3possuiatag v1.0.
Podemoscriarumatagparaumcommitpassado.Sequisermoscriaruma
tagchamada bannersparaocommit 2223859(Alterandotextosdoban-
ner),devemosexecutar:
$ git tag banners 2223859
Imaginequetenhamoserradoonomedeumatag.Porexemplo,criamos
atag verssao1comocomando git tag verssao1 .Podemosdeletá-la
comocomando:
$ git tag -d verssao1
Nasaída,teremos:
Deleted tag ’verssao1’ (was 0f8d4b3)
8.2 Mais informações com tags anotadas
Astagsqueacabamosdecriarsãochamadasdetagsleves,porquenãopassam
deumsimplesapontadorfixoparaumcommit.
Sedesejarmosmantermaisinforma çõescomoquandoumatagfoicriada,
quemacriou,alémdetermosumamensagemdescritiva,devemoscriar tags
anotadas.
Paracriarmosumataganotada,bastausarmosaop ção -adocomando
git tag einformarumamensagemcomaop ção -m:
139
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 148

8.3. Compartilhandotagscomasuaequipe CasadoCódigo
$ git tag -a v1.1 -m "Liberando versão urgente"
Senãoinformarmosumamensagemaoutilizarmosaop ção -ado
comando git tag,seráabertoumeditordetexto.
Podemosexibirasinforma çõesdeumataganotadacomocomando:
$ git show -s v1.1
Teríamoscomorespostadetalhessobreacria çãodataganotada,alémde
informaçõessobreocommitparaoqualatagaponta:
tag v1.1
Tagger: Fulano da Silva <fulanodasilva.git@gmail.com>
Date: Sun Jun 22 13:49:13 2014 -0300
Liberando versão urgente
commit 0f8d4b3f1a5ee4594e72ab1f49786b3a31ab20bb
Author: Fulano da Silva <fulanodasilva.git@gmail.com>
Date: Fri Jun 13 17:14:16 2014 -0300
Adicionando página sobre móveis PET
Ocomando git show nãoserveapenasparaexibirinforma çõesde
tags.
Épossívelutilizá-loparainspecionarcommitseoutrosdetalhesin-
ternosdoGit.
8.3 Compartilhando tags com a sua equipe
Astagscriadascomocomando git tag,anotadasounão,ficamdisponíveis
apenasnorepositóriolocal.
Quandoestamostrabalhandoemequipe,emgeralqueremoscomparti-
lharastagsquecriamoscomnossoscolegas,enviando-asparaorepositório
doservidor.Nonossocaso,enviaríamosastagsquecriamosparaoGitHub.
140
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 149

CasadoCódigo Capítulo8. Controlandoversõesdocódigocomtags
Paracompartilhartags,fazemosdemaneiraparecidacomoquefizemos
combranches,utilizandoocomando git push. Paracompartilharatag
v1.0,devemosexecutarocomando:
$ git push origin v1.0
Seráexibidoalgocomo:
Counting objects: 13, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (8/8), done.
Writing objects: 100% (9/9), 1.20 KiB | 0 bytes/s, done.
Total 9 (delta 4), reused 0 (delta 0)
To git@github.com:fulanodasilva/moveis.git
* [new tag] v1.0 -> v1.0
Pronto!Atag v1.0foienviadaparaorepositórioremoto origin.Nos-
soscolegasdeequipepoderãoobteressatagquandoexecutaremocomando
git pull.
Masaindatemosoutrastagsparacompartilhar:astags bannerse v1.1.
Executarocomando git push paracadatagéalgobastantetedioso.
Sequisermosenviartodasasnovastagsdorepositóriolocalparaum
repositórioremotopodemosutilizarocomando git push comaop ção
--tags:
$ git push origin --tags
Nasaída,teremos:
Counting objects: 1, done.
Writing objects: 100% (1/1), 181 bytes | 0 bytes/s, done.
Total 1 (delta 0), reused 0 (delta 0)
To git@github.com:fulanodasilva/moveis.git
* [new tag] banners -> banners
* [new tag] v1.1 -> v1.1
SeolharmosnoGitHub,veremosquenossastagsestãolá!
141
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 150

E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 151

Capítulo9
Lidandocomconflitos
Aomesclarmosmudan çasentreduasbrancheslocaisnocapítulo6eentre
umabranchlocaleumaremotanocapítulo7,oGitsoubefazeressamescla-
gemautomaticamente,semqualquerproblema.
Comparadocomoutrossistemasdecontrolesdeversão,oGitéespecial-
mentebomaojuntarmudan çasdeduasbranchesdiferentes.
Noscapítulosanteriores,fizemosmudan çasemarquivosdiferentes,oque
oGitresolvecomfacilidade. Atémudan çasemummesmoarquivopodem
serresolvidas.
MasmesmooGitnãoconseguefazermilagres!
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 152

9.1. Mesclandomudançasemummesmoarquivosemconflitos CasadoCódigo
9.1 Mesclando mudanças em um mesmo arquivo
sem conflitos
Nossoclienteligoudesesperadodizendoquedescobriuumerroimportante
nosite:estavafaltandooacrônimo“S.A.”notítulodapágina.
Precisandoatendê-locomurgência,fizemosaseguintemodifica çãona
branch master,noarquivo index.html:
<!-- início do arquivo ... -->
<head>
<!-- tags meta e link ... -->
<title>Móveis Ecológicos S. A.</title>
<!-- tag script -->
</head>
<!-- restante do arquivo ... -->
Comaaltera çãofeita,comitamosoarquivo index.htmlcomoco-
mando git commit -am "Corrigindo título da página" . Obti-
vemosnasaída:
[master 1963258] Corrigindo título da página
1 file changed, 1 insertion(+), 1 deletion(-)
OutracoisaquenossoclientenosinformouéqueapáginadaMóveis
EcológicosS.A.estavasendocopiadaporoutrasempresasdoramo.
Sugerimosalgumassolu çõesparaminimizaroproblemamasnossocli-
entedecidiuporumamaneirasimples:colocarumrodapénapáginacomo
símbolode copyright.Masorodapéteriaqueserbonito,“orodapémaisbelo
detodosostempos”,segundonossocliente.
Parapodermostrabalharcomcalmaembuscadorodapéperfeito,pas-
sandoatrabalharnabranch designdepoisdeexecutarocomando git
checkout design.
Depoisdealgumesfor çochegamosaumdesignutilizandoclassesdofra-
meworkCSSBootstrap. Modificamosoarquivo index.htmlconformea
seguir:
<!-- inicio do arquivo -->
<p class="text-muted text-right">
144
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 153

CasadoCódigo Capítulo9. Lidandocomconflitos
&copy; Copyright Móveis Ecológicos S. A.
</p>
<div>
</body>
</html>
Então,adicionamosamudan çaeagravamosnorepositóriocomoco-
mando git commit -am "Adicionando rodapé com copyright" .
Nasaída,foimostrado:
[design 0e2d613] Adicionando rodapé com copyright
1 file changed, 3 insertions(+)
Listandoohistóricodosúltimosdoiscommitscomocomando git log
-n 2 --oneline --decorate --all ,teríamos:
0e2d613 (HEAD, design) Adicionando rodapé com copyright
1963258 (master) Corrigindo título da página
Ocommitdecódigo 0e2d613(Adicionandorodapécomcopyright)
aindanãofoimescladona master.
Vamos voltar para a branchmaster executando o comandogit
checkout master.
Agora, vamosfazeromergedabranch designna mastercomo
comando git merge design -m "Merge de design na master" .
Teremoscomoresposta:
Auto-merging index.html
Merge made by the ’recursive’ strategy.
index.html | 3 +++
1 file changed, 3 insertions(+)
Seobservarmosoconteúdodoarquivo index.html,oconteúdoestá
deacordocomasúltimasaltera ções: otítulodapáginafoiatualizadoefoi
inseridoumrodapécominforma çõesdecopyright.
OGitconseguiufazeromergeautomático,mesclandosemproblemas
alteraçõesnoarquivo index.htmldasbranches designe master.Isso
aconteceuporquealteramosoarquivoem áreasdistintas.
145
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 154

9.2. Conflitosapósummergecommudan çasemummesmoarquivo CasadoCódigo
Setivéssemosfeitoum git rebase design paramesclarasalte-
raçõesdabranch designna master,tambémnãoteríamosnenhum
conflito.
Nocasodasaltera çõesseremfeitasemumabranchremota,podería-
mosutilizarum git pull ouum git pull --rebase semnenhum
conflito.
9.2 Conflitos após um merge com mudanças em
um mesmo arquivo
Deixamosnossoclientesatisfeito.Ecomasatisfa çãosurgiramnovasideias!
Umadascoisasquenossoclientepediufoicolocarumtextobastantecri-
ativonotopodapágina.Esolicitouqueamudan çafosseurgente!
Porisso,nabranch master,editamosoarquivo index.htmlinserindo
logoabaixodatag h2oseguinteparágrafo:
<!-- inicio do arquivo até tag h2-->
<p>Do lixo ao luxo, um resgate do descartado e uma transformação
em algo funcional. Reaproveitar é aproveitar. Coisas descartadas
são nossa carta na manga. Erodido, mas único.</p>
<!-- ul e restante do arquivo -->
Na branch master, comitamos as alterações no index.html
executando o comando git commit -am "Adicionando texto
criativo".Temoscomoresposta:
[master d2f3597] Adicionando texto criativo
1 file changed, 3 insertions(+)
Outropedidodonossoclientefoimelhorarodesigndobanner,dema-
neiraadestacá-los.
Paratrabalharnessademanda,mudamosparaabranch designexecu-
tandoocomando git checkout design .
Pesquisamos um pouco e resolvemos utilizar um recurso do Boots-
trapparaembelezarobanner. Nabranch design, editamosoarquivo
index.html,inserindoasseguintesclassesCSSnatag h2:
146
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 155

CasadoCódigo Capítulo9. Lidandocomconflitos
<!-- inicio do arquivo até tag h1-->
<h2 id="mensagem" class="alert alert-info"></h2>
<!-- ul e restante do arquivo -->
Depoisdisso,nabranch design,comitamosasaltera çõesnoarquivo
index.htmlexecutandoocomando git commit -am "Melhorando
design do banner" .Nasaída,tivemos:
[design fa528a5] Melhorando design do banner
1 file changed, 1 insertion(+), 1 deletion(-)
Aindanabranch design,aoexibirmosohistóricodosúltimosdois
commits do repositório com o comandogit log -n 2 --oneline
--decorate --all,teríamos:
fa528a5 (HEAD, design) Melhorando design do banner
d2f3597 (master) Adicionando texto criativo
Notequeocommitdecódigo fa528a5(Melhorandodesigndobanner)
aindanãotevesuasaltera çõesaplicadasnabranch master.
Executandoocomando git checkout master ,voltamosatrabalhar
nabranch master.
Paramesclarmosoúltimocommitdabranch designna master,exe-
cutamosocomando git merge design -m "Merge de design na
master".Nasaída,teremos:
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Automatic merge failed;fix conflicts and then commit the result.
Observeamensagemanterior: foiindicadoquehouveumconflitono
arquivo index.htmlequeomergeautomáticofalhou.
Seabrirmosoarquivo index.htmlveremosumconteúdoestranho:
<!-- inicio do arquivo arquivo até h1 -->
<<<<<<< HEAD
<h2 id="mensagem"></h2>
<p>Do lixo ao luxo, um resgate do descartado e uma transformação
147
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 156

9.2. Conflitosapósummergecommudan çasemummesmoarquivo CasadoCódigo
em algo funcional. Reaproveitar é aproveitar. Coisas descartadas
são nossa carta na manga. Erodido, mas único.</p>
=======
<h2 id="mensagem" class="alert alert-info"></h2>
>>>>>>> design
<!-- ul e restante do arquivo -->
Mesmosendomuitobomparafazeromergeautomático,dessavezoGit
nãoconseguiumesclaroarquivo index.htmldemaneiraclaraporquefo-
ramfeitasaltera çõesna mesmaregiãodoarquivo .
Deformacautelosa,oGitmarcouumconflitocomoscaracteres <, =e
>.
Entreostextos <<<<<<< HEAD e =======estãoasaltera çõesquefize-
mosnabranch master,queéabranchatual,paraqualo HEADestáapon-
tando.
Jáentre =======e >>>>>>> design,estãoasaltera çõesquefizemos
nabranch design.
Aoexecutarmos git status,teremos:
On branch master
Your branch is ahead of ’origin/master’ by 5 commits.
(use "git push" to publish your local commits)
You have unmerged paths.
(fix conflicts and run "git commit")
Unmerged paths:
(use "git add <file>..." to mark resolution)
both modified: index.html
no changes added to commit (use "git add" and/or
"git commit -a")
Notequeoarquivo index.htmlaparececomonãomesclado,como both
modifiedsob Unmerged paths(nomesnãomuitointuitivos).
Agorateremosquerealizaromergemanualmente.Nessecaso,asolu ção
éfácil.Vamoseditaroarquivo index.htmldaseguintemaneira:
148
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 157

CasadoCódigo Capítulo9. Lidandocomconflitos
<!-- inicio do arquivo arquivo até h1 -->
<h2 id="mensagem" class="alert alert-info"></h2>
<p>Do lixo ao luxo, um resgate do descartado e uma transformação
em algo funcional. Reaproveitar é aproveitar. Coisas descartadas
são nossa carta na manga. Erodido, mas único.</p>
<!-- ul e restante do arquivo -->
Mesmodepoisdeeditaroarquivo,removendoasmarca çõesdeconflito
emesclandomanualmenteasaltera ções,aindateremosamesmarespostade
antesaoexecutarmos git status.
ParainformarmosparaoGitqueresolvemosoconflitonoarquivo,temos
queadicioná-loàáreadestageexecutando git add index.html .
Agora,aoexecutarmos git status,teremos:
On branch master
Your branch is ahead of ’origin/master’ by 5 commits.
(use "git push" to publish your local commits)
All conflicts fixed but you are still merging.
(use "git commit" to conclude merge)
Changes to be committed:
modified: index.html
Reparequeoarquivo index.htmlaparececomomodificadoeestá
prontoparasercomitado.
Depois disso, falta comitarmos as mudanças com o comandogit
commit -am "Resolvendo conflitos após merge de design" .
Comoresposta,veremos:
[master d364c56] Resolvendo conflitos após merge de design
Pronto!Conflitoresolvido.Finalmenteomergefoifinalizado.
Nossapáginaficoucomumvisualbemrazoável:
149
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 158

9.3. Resolvendoconflitosapósumrebase CasadoCódigo
Figura9.1:Páginaembelezada
9.3 Resolvendo conflitos após um rebase
Esetivéssemosutilizadoumrebaseparamesclarasúltimasmudan çasda
branch designna master?
Devemosunirocommit fa528a5(Melhorandodesigndobanner)da
branch designcomocommit d2f3597(Adicionandotextocriativo)da
branch master.Masambosalteramotopodoarquivo index.html,oque
geraumconflito.
Considerandoqueestamosnabranch master,apósexecutarocomando
git rebase design ,veríamos:
First, rewinding head to replay your work on top of it...
Applying: Alterando textos do banner
Applying: Adicionando página sobre móveis PET
Applying: Corrigindo título da página
Applying: Adicionando texto criativo
Using index info to reconstruct a base tree...
M index.html
Falling back to patching base and 3-way merge...
150
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 159

CasadoCódigo Capítulo9. Lidandocomconflitos
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Failed to merge in the changes.
Patch failed at 0004 Adicionando texto criativo
The copy of the patch that failed is found in:
/home/fulanodasilva/moveis/.git/rebase-apply/patch
When you have resolved this problem, run "git rebase
--continue".
If you prefer to skip this patch, run "git rebase --skip"
instead.
To check out the original branch and stop rebasing, run
"git rebase --abort".
Observequequeapareceumconflitonoarquivo index.html.
Aoexecutarmosocomando git status,teríamos:
rebase in progress; onto fa528a5
You are currently rebasing branch ’master’ on ’fa528a5’.
(fix conflicts and then run "git rebase --continue")
(use "git rebase --skip" to skip this patch)
(use "git rebase --abort" to check out the original branch)
Unmerged paths:
(use "git reset HEAD <file>..." to unstage)
(use "git add <file>..." to mark resolution)
both modified: index.html
no changes added to commit (use "git add" and/or "git commit -a")
Demaneirasemelhanteaoqueaconteceuapósoconflitonomerge,oar-
quivo index.htmlapareceem Unmerged pathscomo both modified.Apesar
dadescri çãopoucointuitiva,issoindicaqueháumconflitonessearquivo.
Aoabrirmosoarquivo index.htmlveremosasmesmasmarca çõesde
conflitocomostextos <<<<<<< HEAD, =======e >>>>>>> design.
Devemosmesclaroarquivo index.htmlmanualmente,removendoas
marcaçõesdeconflito,conformefizemosanteriormente.
151
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 160

9.4. Usandoumaferramentapararesolverconflitos CasadoCódigo
Para marcar a resolução do conflito, devemos executargit add
index.html.
Depoisdisso,aoexecutar git status,teríamos:
rebase in progress; onto fa528a5
You are currently rebasing branch ’master’ on ’fa528a5’.
(all conflicts fixed: run "git rebase --continue")
Changes to be committed:
(use "git reset HEAD <file>..." to unstage)
modified: index.html
Parafinalizarorebase,teríamosqueexecutarainda:
$ git rebase --continue
Pronto!Finalmentefinalizamosnossorebaseconflitante!Ufa!
Sequiséssemosabortarorebase,voltandoàsitua çãoantesdatenta-
tivademesclagem,poderíamosexecutar git rebase --abort .
Tambémpoderíamossimplesmenteignorarocommitquegerouo
conflito, pulando-o, executandogit rebase --skip . Essaop ção
temqueserusadacomcuidado. Sófazsentidoquandoexatamentea
mesmaaltera çãofoifeitanabranchsendomesclada.
9.4 Usando uma ferramenta para resolver con -
flitos
Oconflitoqueacabamosderesolverfoibemfácil.Visualizaroarquivopara
decidircomomesclarasdiferentesversõesnãodemandougrandeesfor ço.
Porém,algumasvezestemosconflitosbemdesafiadores,emqueédifícil
visualizarcadatrechoconflitantedoarquivo.
Alémdisso,podemosterváriosarquivoscomconflitoparaseremsoluci-
onados.
152
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 161

CasadoCódigo Capítulo9. Lidandocomconflitos
Experiêncianocódigoqueestásendodesenvolvidoecalmasãofunda-
mentaisparanãoinserirmoserrosaoresolverconflitos.
Masutilizarumaferramentaapropriadapodeauxiliarnarapidezdere-
soluçãodeconflitos.
ComGit,podemosinvocarumaferramentaderesolu çãodeconflitoscom
ocomando:
$ git mergetool
Seriamexibidasmensagensparecidascom:
This message is displayed because ’merge.tool’ is not
configured.
See ’git mergetool --tool-help’ or ’git help config’ for more
details. ’git mergetool’ will now attempt to use one of the
following tools: meld opendiff kdiff3 tkdiff xxdiff
tortoisemerge gvimdiff diffuse diffmerge ecmerge p4merge araxis
bc3 codecompare emerge vimdiff
Merging:
index.html
Normal merge conflict for ’index.html’:
{local}: modified file
{remote}: modified file
Hit return to start merge resolution tool (meld):
Leiacomaten çãoamensagemanterior.ReparequeoGitlistoualgumas
ferramentaspararesolu çãodeconflitoscomo Meld(http://meldmerge.org),
bemsimpleseefetivaquefuncionaemWindows,MacOSeLinux,Tortoi-
seMerge(http://tortoisesvn.net/TortoiseMerge.html),bastanteutilizadamas
sóparaWindows,entreoutras.
Algumadasferramentaslistadasanteriormenteseráprocuradaeinvo-
cada.
Namensagemanterior,foiindicadaaferramentaMeld.Pressionandoa
tecla Enter,aferramentaéaberta:
153
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 162

9.4. Usandoumaferramentapararesolverconflitos CasadoCódigo
Figura9.2:Meld,ferramentaderesolu çãodeconflitos
Paradefinirumaferramentapadrãopararesolu çãodeconflitospo-
demosutilizaraconfigura ção merge.tool.
Porexemplo,parasempreutilizaroMeld,poderíamosexecutar git
config --global merge.tool meld .Ocomando melddevees-
tarnoPATHdosistemaoperacional.
NoMeld,oarquivo index.htmlfoiabertoàesquerdacomoconteúdo
da master,àdireitacomoconteúdodabranch designenocentrocom
oconteúdoanterioràsduasmodifica çõesconflitantes.Devemoseditaroar-
quivodocentro
DepoisderesolvidooconflitousandooMeldesalvaroarquivo,seexe-
cutarmos git status,teremos:
On branch master
Your branch is ahead of ’origin/master’ by 5 commits.
(use "git push" to publish your local commits)
All conflicts fixed but you are still merging.
154
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 163

CasadoCódigo Capítulo9. Lidandocomconflitos
(use "git commit" to conclude merge)
Changes to be committed:
modified: index.html
Untracked files:
(use "git add <file>..." to include in what will be committed)
index.html.orig
Note que o arquivoindex.html está entre as mudanças prontas
paraseremcomitadas. Alémdisso,foicriadoumnovoarquivochamado
index.html.origcomoconteúdooriginal,antesdoconflitoserresolvido.
Oarquivo index.html.origpodeserapagado.
Podemos, então, comitar o arquivoindex.html agora sem con-
flitos, executando git commit -am "Resolvendo conflitos após
merge de design" .Nasaída,teremos:
[master b0418dc] Resolvendo conflitos após merge de design
155
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 164

E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 165

Capítulo10
ManeirasdetrabalharcomGit
Nocapítulo3,vimoscomotrabalharcomumrepositóriolocaldoGit,criando
uma“máquinadotempo”paraonossocódigo.
Jánocapítulo4,vimoscomoutilizarrepositóriosremotosparacompar-
tilharnossocódigocomosoutrosmembrosdanossaequipe,alémdemanter
umbackupdorepositório.
Enocapítulo5,utilizamosoGithubparatornarnossorepositórioremoto
acessíveldequalquerlugarquetenhaacessoàinternet.
Depois,noscapítulos6e7,utilizamosbrancheslocaiseremotaspara
trabalharemparaleloemdiferentesfuncionalidadesdemaneiraorganizada.
Estudamostambém,nocapítulo8,comomarcarasversõesdenossasen-
tregasatravésdetags.
Nocapítulo9aprendemoscomolidarcomconflitosqueacontecemao
mesclarbranches.
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 166

CasadoCódigo
Mascomousartudoissoqueaprendemosnoseuprojeto?Qualamelhor
maneiratrabalharcomoGitnoseucaso?
Modelosdedistribui çãoderepositóriosedebranches
OGitéumsistemadecontroledeversãodistribuído.Temoslocalmente
umacópiacompletadorepositório,quepodemoscompartilharremotamente.
Alémdisso,podemosapontarparamaisdeumrepositórioremoto.
Porisso,umadasdecisõesqueprecisamosfazeréo modelodedistribui-
çãoderepositórios aseradotado,definindocomoorganizarosrepositórios
remotos.Osmodelosmaisutilizadossão:
• Apenasumrepositórioremoto,central,paraondeosrepositórioslocais
apontam;
• Cadadesenvolvedortemseufork,umrepositórioremotoqueéuma
cópiadoprojeto,utilizandoumrepositóriocentralparaintegra ção;
• Umahierarquiaderepositóriosparaintegração.
Aocontráriodeoutrossistemasdecontroledeversão,criarbranchesno
Gitéalgomuitoleveerápido.Alémdisso,oGitémuitobomemfazermes-
clagensautomáticas,oqueencorajaousodebranches.
Portanto,outracoisaqueprecisamosdecidiréo modelodebranches a
serutilizadononossoprojeto.Algunsdosmodelosmaiscomunssão:
• Utilizarapenasabranchmaster;
• Terumabranchparacadanovafuncionalidade,deixandoa master
paracódigoprontoparaserentregue;
• Teralgumasbranchesporetapadedesenvolvimento,comoumabranch
delongoprazoparacódigoaindaemconstru çãoeumadecurtoprazo
paracorre çõesdebugsurgentes.
ExistemváriosfluxosdetrabalhopossíveisaosetrabalharcomGit.Va-
mosestudarosmaiscomuns.
158
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 167

CasadoCódigo Capítulo10. ManeirasdetrabalharcomGit
10.1 Utilizando só a branch master com um re -
positório central
Umdosfluxosdetrabalhomaissimpleséutilizarapenasumrepositóriocen-
tralhospedado,porexemplo,noGithub,comitandotudodiretamentena
branchlocal master.
Paraenviaroscommitslocais,cadadesenvolvedorfazumpushparaore-
positóriocentral.Porisso,todososmembrosdaequipedevemterpermissões
depush.
Figura10.1:Repositóriocentralsócommaster
Considerandoquetemosumrepositórioparaonossoprojetoconfigu-
radonoGithub,aprimeiracoisaseriafazer:
$ git clone https://github.com/empresa/projeto.git
Apósoclone,temosumacópialocalcompletadorepositório.
Podemos, então, criar novos arquivos ou editar arquivos existentes.
Quandoestivermossatisfeitoscomocódigo,podemosadicionarasaltera-
çõesàáreadestageedepoiscomitá-lasna master,utilizandocomandos
como:
$ git add .
$ git commit -m "Otimizando consulta a clientes"
159
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 168

10.1. Utilizandosóabranchmastercomumrepositóriocentral CasadoCódigo
Depoisdealgunscommits,podemoscompartilharnossotrabalhocoma
equipe:
$ git push origin master
Depoisdetermospublicadoosnovoscommits,osoutrosdesenvolvedo-
respodemobtê-losexecutando:
$ git pull --rebase origin master
Encorajamosousodeum git pull --rebase aoobtermudan ças
remotasporquesimplificaohistóricodorepositório,evitandocommits
demerge.
Seocorreralgumconflitonomomentoemqueobtemososnovoscom-
mits,devemosresolverosproblemaseditandoosarquivosapropriadospara
entãoexecutar:
$ git add .
$ git rebase --continue
Quandoestivermosprontosparafazerumaentrega,podemosmarcá-la
criandoumatage,depois,enviandoessatagparaorepositóriocentral:
$ git tag v1.0
$ git push origin --tags
Quandoutilizar?
Paraequipespequenasounaado çãodoGit.
Quandotrabalhamosemequipespequenas,comaté5desenvolvedores,
quantomaissimplesofluxodetrabalho,melhor.Comoaequipeépequena,
muitoprovavelmenteoprojetoserápequenoeteremoscontrolenoritmodas
entregas,nãoprecisandodeumfluxomaispoderoso(ecomplexo).
Essefluxoéparecidocomamaneiracomosãocomumenteutilizadossis-
temasdecontroledeversãocentralizados,comooSubversion.Porisso,para
160
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 169

CasadoCódigo Capítulo10. ManeirasdetrabalharcomGit
equipesqueestãoiniciandocomoGit,éofluxodemaisfácilado ção.Aequipe
podefocaremaprenderoscomandosbásicosdoGit,utilizadosparalidarcom
umrepositóriolocal,paradepoispartirparafluxosmaisavan çados.
Vantagens
• Asimplicidadedessefluxopermiteumaado çãomaistranquilapara
quemestácomeçandoautilizarofluxo.Tambémhámenoscomplica-
çãoparaequipesreduzidas.
• Émaisfácildeadotarintegraçãocontínua,umapráticabastanteco-
mumemprojetosqueusammetodologiaságeis. Nessaprática,ocó-
digodeveserintegradofrequentemente,disparando buildsetestesau-
tomatizadosedetectandoerrosdeintegra çãoomaisrápidopossível.
Nessefluxo,comotodaaltera çãoécomitadanabranch master,todo
códigocompartilhadodepoisdeumpushseráintegradona master
dorepositóriocentral.Acadanovopush,obuildeostestesautoma-
tizadospodemserdisparadosutilizandoessecódigointegrado.Além
disso,possíveisconflitossãodetectadosacadapull.
Desvantagens
• Aocorrigirdefeitosurgentes,podeserqueocódigodenovasfuncio-
nalidadesaindaemdesenvolvimentojátenhasidocompartilhadona
branch masterdorepositóriocentral.Comessefluxo,ficadifícilse-
pararocódigodacorre çãododefeitodocódigodasnovasfuncionali-
dades,oquepodegerarmaisdefeitoseinsatisfa çãonosclientes.
• Comotudoécomitadonabranchmaster,asentregassãofeitascom
todoocódigoqueestánorepositórionomomentodaentrega.Nãoé
possívelentregarsópartedasfuncionalidadesqueforamcompartilha-
dascomorepositóriocentral.
• Háanecessidadedepermissãodepushparatodososmembrosda
equipenorepositóriocentral,jáqueháapenasumrepositórioremoto.
161
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 170

10.2. Utilizandobranchesporfuncionalidadecomumrepositóriocentral CasadoCódigo
Paraprojetosopensource,éalgoinviável.Paraprojetoseequipesmuito
grandes,podetambémserumproblema.
10.2 Utilizando branches por funcionalidade
com um repositório central
Podemosutilizarbranchesparaisolarocódigodenovasfuncionalidadesou
alteraçõesemfuncionalidadesexistentes.Abranch masterpassaasertra-
tadademaneiraespecial,ficandoestáveldurantetodoodesenvolvimento
doprojeto.Sóquandoafuncionalidadeestiverpronta,éfeitoummergeda
branchdafuncionalidadena master.
Seforprecisorealizarumacorre çãourgente,podeserutilizadaabranch
masterdiretamente.Paracorre çõesoualtera çõesmaisdemoradas,podem
sercriadasbranchesparasegregaroscommitsdacorre ção.
Essamaneiradetrabalhartambéméchamadade feature branching
ou topic branching.
Figura10.2:Repositóriocentralcombranchesporfuncionalidade
Vamosdizerquetemosumrepositóriolocalclonadoapartirdeumrepo-
sitóriodoGithub,comofizemosanteriormente,comocomando git clone
https://github.com/empresa/projeto.git.
Afuncionalidadeaserdesenvolvidaéacria çãodepedidosdenossaloja
162
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 171

CasadoCódigo Capítulo10. ManeirasdetrabalharcomGit
online.Antesdecome çar,vamoscriarapartirda masterumabranchcha-
mada pedidos,jámudandopraessanovabranch:
$ git checkout -b pedidos
Jánabranch pedidos,podemoscome çaratrabalharnafuncionalidade,
criandonovosarquivosealterandoarquivosexistentes. Emseguida,pode-
mosefetuarcommitscomoscomandosquejáconhecemos:
$ git add .
$ git commit -m "Tela inicial de pedidos"
Depoisdealgunscommits,mesmosemtermosterminadoafunciona-
lidadedepedidos,podemoscompartilharocódigoquefizemosenviando-o
paraorepositóriocentral.Bastaexecutar:
$ git push origin pedidos
Comocódigonorepositóriocentral,temosumbackupdocódigoeou-
trosmembrosdanossaequipepodemobtê-loparacolaborarnodesenvol-
vimentodafuncionalidade. Tudoissosemafetaraestabilidadedabranch
master.
Orestantedanossaequipe,parapodertrabalharnafuncionalidade,pre-
cisaobterasúltimasaltera çõesdorepositóriocentrale,emseguida,criaruma
cópialocaldabranch pedidos.Paraisso,deve-seexecutar:
$ git fetch origin
$ git checkout -t origin/pedidos
Nóseoutrosmembrosdaequipepodemosfazercommitse,quandoapro-
priado,compartilharocódigopormeiodorepositóriocentralatravésdoco-
mando:
$ git push origin pedidos
Para obtermos o novo código da funcionalidade, ainda na branch
pedidos,devemosfazer:
$ git pull --rebase origin pedidos
163
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 172

10.2. Utilizandobranchesporfuncionalidadecomumrepositóriocentral CasadoCódigo
Nocasodeconflitosapósopullcomrebase,devemosmesclarosarquivos
manualmenteeexecutar:
$ git add .
$ git rebase --continue
Abranch pedidosdorepositóriocentralteráocódigoqueintegraas
mudançasdetodososmembrosdaequipe.Testadoreseoutrosinteressados
podemutilizarocódigodabranch pedidosparaverificaroandamentodas
atividadesedetectarproblemas. Revisaraqualidadedocódigo,porexem-
plo,ficamaisfácilporqueasmudan çasrelacionadasàfuncionalidadeficam
isoladas.
Casohajaalgumaaltera çãofeitadiretamentena master,comoumacor-
reçãodeumdefeitourgente,éimportanteobtê-lanorepositóriolocal.Para
isso,continuandonabranch pedidos,devemosexecutar:
$ git pull --rebase origin master
O comando anterior obtém as mudanças da branch remota
origin/masterejáfazorebasenabranchatual,queéa pedidos.
Seriaequivalenteàsequênciadecomandos:
$ git checkout master
$ git pull origin master
$ git checkout pedidos
$ git rebase master
Adiferen çaéque,nessaúltimasequência,abranchlocal master
ficariaatualizadacomasúltimasmudan çasda origin/master.
Quandoaequipeestiversatisfeitacomafuncionalidadeecomocódigo,
algumdosdesenvolvedorespodefazeromergenabranch master.
Antes,éimportantenoscertificarmosdequeabranch mastercontém
asúltimasmodificaçõesdorepositóriocentral.Podemosutilizarumpullsem
rebase,paradeixarmosa masterintacta.Étranquilofazeropullsemrebase
164
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 173

CasadoCódigo Capítulo10. ManeirasdetrabalharcomGit
nessecasoporque,muitoprovavelmente,seráfeitoummergedoestilofast-
forward,jáquenãoécomumfazermoscommitsdiretamentena master.
Nabranch pedidos,devemosexecutaroscomandos:
$ git checkout master
$ git pull origin master
$ git merge pedidos
Hácasosemqueaequipetemmuitosmembrose/outemproblemas
nacomunica ção. Emvezdomerge,talvezsejamelhorfazerum git
pull origin pedidos (aindanabranch master). Tambémseria
realizadoummerge,mascompossíveisaltera çõesdeúltimahora.
Nocasodeconflitosnomergedabranchdafuncionalidade,devemosre-
solverosconflitosmanualmenteparadepoisexecutar:
$ git add .
$ git commit -m "Resolvendo conflitos no merge de pedidos"
Depoisderealizadoomergedabranch pedidoscomabranchlocal
master,podemoscompartilharocódigoexecutando:
$ git push origin master
Nomomentoadequado,podemosliberarumanovaversãodosistema,
marcando a entrega com uma tag através do comandogit tag v1.0
e compartilhando a tag criada com o comando$ git push origin
--tags.
Senãoquisermosentregaralgumafuncionalidadenanovaversãodosis-
tema,bastanãofazermosomergedabranchdafuncionalidadenabranch
master.
165
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 174

10.2. Utilizandobranchesporfuncionalidadecomumrepositóriocentral CasadoCódigo
Quandoutilizar?
Emprojetosumpoucomaiores,principalmentesejátiveremalgumas
entregasfeitas.ÉimportantequeaequipetenhafamiliaridadenousodoGit.
Paraprojetosquejáestãoatodovapor,commelhoriasecorre çõesque
precisamserfeitasdeimediato,isolarcódigoqueaindaestásendodesenvol-
vimentoéalgoimportante.Comousodeumabranchparacadafunciona-
lidade,podemosorganizarodesenvolvimentodasnovasfuncionalidadesde
maneiraanãoafetardemandasurgentes.
Paraqueessafluxosejausadocomfluência,éprecisoqueosdesenvolve-
doresjáestejamconfortáveiscomousobásicodoGit.
Vantagens
• Podemosisolarcódigomaisestávelnabranchmaster,facilitandoa
realizaçãodemelhoriasecorre çõesimediatas.
• Revisõesdaqualidadedonovocódigoqueimplementaumafunciona-
lidadepodemserfeitasanalisandooscommitsdabranchdafunciona-
lidade.
• Podeserentregueapenaspartedasfuncionalidadesqueestãosendo
desenvolvidas,possibilitandomudan çasmaistranquilasnaestratégia
denegóciodonossocliente.
Desvantagens
• ComoaequipeprecisadominaroGitrazoavelmentebem,ousodesse
fluxonoiníciodaado çãodoGitficadificultado.
• Comotrabalhamoscomumrepositóriocentral,aindaháanecessidade
depermissãodepushparatodososmembrosdaequipe.Porisso,esse
fluxopodeserproblemáticoparagrandesequipesetorna-seinviável
paraprojetosopensource.
• Ocódigodeumafuncionalidadesóéefetivamenteintegradocomou-
trasmudan çasnomomentodomergefinalcomabranch master.
166
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 175

CasadoCódigo Capítulo10. ManeirasdetrabalharcomGit
Comoutrasfuncionalidadesemdesenvolvimento,possíveisconflitos
entreocódigodasfuncionalidadessóserãodescobertostardiamente,
aomesclarmostodasasbranches.
• Realizarintegraçãocontínua,descobrindoproblemasnocódigoenas
funcionalidadesrapidamente, ficamaisdifícil. Agrandevantagem
dessefluxo,queéadeisolarcódigodasfuncionalidades,torna-seapior
desvantagemsobaóticadeintegra çãocontínua.Porisso,especialistas
emintegra çãocontínuanãorecomendamousodebranchesporfun-
cionalidade,favorecendooisolamentodasfuncionalidadescomuma
arquiteturamaismodular,utilizandoabstra çõesparagrandesaltera-
çõesnocódigo( branch by abstraction)econfigura çõesparadesabilitar
funcionalidadesnovas( feature toggles).
10.3 Utilizando branches por etapa de desen -
volvimento com um repositório central
Aocomitarmosumnovocódigoemumabranchseparadaparaumafuncio-
nalidadeespecífica,mantemosabranchlocal masterestável,mascorremos
oriscodeadiardemaisaintegra çãoentreoscódigosdasnovasfuncionalida-
des.Essademorapodelevaradefeitosquedeixariamnossosclientesinsatis-
feitos.
Paraevitaraintegra çãotardiadasfuncionalidades,poderíamosteruma
branch para código ainda em desenvolvimento,chamada desenv.Seriauma
branchdelongoprazo,queexistiriaenquantooprojetoestiversendodesen-
volvido.Abranch masterteriacódigojáprontopraserentregue.Jáabranch
desenvteriacódigoparaapróximaentrega.Quandotivermosumpontoes-
távelnonovocódigo,faríamosummergeda desenvna master.
Podemoscontinuarutilizando branches por funcionalidade mas,agora,
criando-asapartirdabranch desenv. Periodicamente,poderíamosefe-
tuarummergeprecocedasbranchesdasfuncionalidades,mesmoantesde
ocódigoestartotalmentefinalizado.Assim,evitaríamosaintegra çãotardiae
deixaríamosdeafetarabranch master.
Seriainteressantetermos branches de release,paracomitarmoscódigore-
ferenteaumadeterminadaentrega,comocorre çõesdeúltimahoradepe-
167
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 176

10.3. Utilizandobranchesporetapadedesenvolvimentocomumrepositóriocentral CasadoCódigo
quenosbugsdescobertoslogoantesdeliberarumaversão. Teriamnomes
como release1.1ou release2.0eseriamcriadasapartirda desenv.
Tambémpoderiamsercomitadosnessasbranchesdereleasecódigosneces-
sáriosparaprepararumaentrega,comoarquivosdeversãoe release notes.
Seriambranchesdecurtoprazo,quepoderiamserdeletadasquandonãofize-
remmaissentido.Oscommitsdascorre çõesfeitasnessasbranchesderelease
precisariamseraplicadosna masterena desenv,atravésdeummerge.
Parabugsurgentes,queafetamversõesemprodu ção,poderíamoscriar
uma branch de hotfix.Seestivermoscomaversão 1.0emprodu çãoeaconte-
cerumdefeitoquepodesercorrigidodemaneiraimediata,poderíamoscriar
abranch hotfix-1.0.1apartirda master.Acorre çãoseriafeitanessa
novabranche,quandofinalizada,faríamosummergenabranch master.
Tambéméimportanteefetuarmosummergenabranch desenv,paraobter-
mosacorre çãododefeito.Umabranchdehotfixédecurtoprazoe,depois
defeitoomerge,podemosapagá-la.
Figura10.3:Repositóriocentralcombranchesporetapadedesenvolvimento
Comonosfluxosdetrabalhoanteriores,cadadesenvolvedordevefazer
oclonedorepositóriocentralexecutando,porexemplo, git clone https:
168
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 177

CasadoCódigo Capítulo10. ManeirasdetrabalharcomGit
//github.com/empresa/projeto.git.
Logonoiníciodoprojeto,ouemalgumoutromomentoapropriado,po-
demoscriarumabranchlocalchamada desenv,apartirda master,para
comitarmoscódigoaindaemdesenvolvimento. Tambéméimportanteque
essabranchexistanorepositóriocentral.Paraisso,umdosdesenvolvedores
deveexecutar:
$ git branch desenv
$ git push origin desenv
Para começarem a trabalhar na branchdesenv, os desenvolvedo-
res precisam criar uma branch local que aponta para a branch remota
origin/desenvdorepositóriocentral.Paraisso,devemexecutar:
$ git fetch origin
$ git checkout -t origin/desenv
Paratrabalharmosemumanovafuncionalidade,porexemplodeesto-
que,podemoscriarumabranchparaessafuncionalidadeapartirdabranch
desenv,executando:
$ git checkout -b estoque desenv
Podemosefetuaralgunscommitse,depois,compartilharabranchcoma
nossaequipe,atravésdocomando git push origin estoque .
No momento adequado, devemos fazer o merge da funcionalidade
estoquenabranch desenv,integrando-acomasoutrasfuncionalidades
quejáforammescladascom desenv. Porém,antesdomerge,éimpor-
tanteobtermosasúltimasmudan çasem desenvfeitaspelosoutrosmem-
brosdanossaequipeatravésdeumpullde origin/desenv. Depoisdo
merge,podemoscompartilharabranch desenvquejáteráosúltimoscom-
mitsda estoque.Parafazerissotudo,considerandoqueestamosnabranch
estoque,devemosexecutar:
$ git pull origin desenv
$ git checkout desenv
$ git merge estoque
$ git push origin desenv
169
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 178

10.3. Utilizandobranchesporetapadedesenvolvimentocomumrepositóriocentral CasadoCódigo
Podemosrepetiroscomandosanterioressemprequequisermosintegrar
abranchdafuncionalidade estoquecomabranch desenv. Aotermi-
narmosafuncionalidade,devemosfazerumúltimomergeem desenv.Se
quisermos,podemosdeletarnossabranchlocal estoquecomocomando
git branch -d estoque .
Quandoestivermossatisfeitoscomasfuncionalidadesqueforammescla-
dasnabranch desenv,podemoscriarumabranchparaapróximarelease
comumnomecomo release-1.0apartirda desenv.Paraisso,devemos
executar:
$ git checkout -b release-1.0 desenv
Nabranch release-1.0podemoscomitar,porexemplo,umarquivo
listandoasnovasfuncionalidades(oreleasenotes),modificararquivospara
prepararaentrega.Alémdisso,podemoscomitarcorre çõesdepequenosbugs
quedescobrirmosantesdeliberaranovaversão. Enquantoisso,outrosde-
senvolvedorespodemcome çaratrabalharnasfuncionalidadesdapróxima
entrega,comitandonabranch desenv.
Parafecharmosanovaversão,devemosfazeromergedanossabranch
release-1.0nabranch master.Paraisso,devemosexecutaroscoman-
dos:
$ git checkout master
$ git merge release-1.0
$ git push origin master
Tambéméimportante,aindanabranch master,marcamosanovaver-
sãocomumatag:
$ git tag v1.0
$ git push origin --tags
Setivermoscomitadocorre çõesdebugsnabranch release-1.0,éim-
portanteaplicarmosocódigocorrigidonabranch desenv,atravésdeum
merge.Paraisso,devemosexecutar:
$ git checkout desenv
$ git merge release-1.0
$ git push origin desenv
170
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 179

CasadoCódigo Capítulo10. ManeirasdetrabalharcomGit
Sequisermos,podemosdeletarabranchlocal release-1.0atravésdo
comando git branch -d release-1.0 .
Casoaconte çaumbugemprodu çãoquedevesercorrigidoimediata-
mente,podemoscriarumabranchparatrabalharmosnacorre ção.Seaversão
atualfora 1.0,poderíamoschamá-lade hotfix-1.0.1.Jáqueabranch
mastercontémocódigodaúltimaversãoliberadaparaprodu ção,devemos
criaranovabranchdecorre çãoapartirdamaster.Paracriá-la,devemosexe-
cutar:
$ git checkout -b hotfix-1.0.1 master
Depoisdedescobrimosacausadodefeitoetermoscomitadoocódigo
com a correção, podemos fazer o merge da branchhotfix-1.0.1na
branch master.Então,devemosexecutar:
$ git checkout master
$ git merge hotfix-1.0.1
$ git tag 1.0.1
Não podemos esquecer de aplicar a correção do defeito na branch
desenv,quecontémocódigoqueestásendodesenvolvido.Podemosfazer
issoexecutando:
$ git checkout desenv
$ git merge hotfix-1.0.1
Feitos os merges da branchhotfix-1.0.1nas branches master
e desenv podemos apagá-la com o comando git branch -d
hotfix-1.0.1.
Quandoutilizar?
Emprojetoscomplexos,quejátêmváriasentregasecomdiversasnovas
funcionalidadesemdesenvolvimento.Aequipejádeveterumbomdomínio
doGit.
Essefluxoqueusabranchesporetapadedesenvolvimentodeixaotra-
balhobastanteorganizado. Abranchdedesenvolvimentoservecomouma
branchdeintegra çãoparaasdiferentesbranchesdefuncionalidade. Jáa
171
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 180

10.3. Utilizandobranchesporetapadedesenvolvimentocomumrepositóriocentral CasadoCódigo
branch masternãoéafetadapelodiaadia,ficandobastanteestávelporque
sótemnovocódigonosmomentosdeentregaecorre çõesurgentes.Ajustes
finosecódigoparaprepararaentregatemseulugar,nasbranchesderelease.
Bugsurgentespodemsercorrigidosnasbranchesdehotfix.
Devidoàcomplexidadenousodasvariadasbranches, paratrabalhar
dessamaneira,odomíniodosconceitosdoGitpelosmembrosdaequipeé
bastanteimportante.
Umfluxoparecidocomesseéchamadoporalgunsde Gitflow,masnão
éumfluxo“oficial”,apesardoapelido.FoidescritoporVincentDriessenem
2010,emseublog:http://nvie.com/posts/a-successful-git-branching-model/
Vantagens
• Abranchmasterficabemestável,podendoserutilizadaatéparadis-
pararimplanta çõesautomáticasdosoftware.
• Conseguimosdescobrirconflitosouerrosentrecódigosdasnovasfun-
cionalidadesmaiscedosemesclarmosasbranchesdasfuncionalidades
nabranch desenvperiodicamente.
• Comoutilizamosbranchesporfuncionalidade,revisõesdocódigodas
funcionalidadesãofáceisdefazer.
• Podemosentregarapenaspartedasfuncionalidades,bastandodeixar
ocódigoisoladonabranchdafuncionalidadequenãoentraránanova
versão. Porém,sefizermosintegra çõesperiódicasem desenv,isso
podeserumdesafio.
• Correçõesurgentestêmumlugardefinidonessefluxo:asbranchesde
hotfix.
• Trabalhorelacionadocomapreparaçãodeumanovaversãoeajustes
finosantesdalibera çãopodemserfeitosemumabranchderelease.
172
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 181

CasadoCódigo Capítulo10. ManeirasdetrabalharcomGit
Desvantagens
• AequipeprecisadeumbomdomíniodoGit.
• Éumfluxocomplexo.Porisso,émelhorutilizaressefluxoemprojetos
grandese/ouquandooprojetoestáatodovapor.Aí,aorganiza çãodo
trabalhocompensaacomplexidade.
• Todososmembrosdanossaequipeprecisamdepermissãodepushno
repositóriocentral,inviabilizandoousoemprojetosopensourceeem
equipesgrandes.
• Mesmocomabranchdesenv,queservecomoumabranchdeinte-
gração,sóintegraremosefetivamenteocódigonosmomentosemque
fizermosomergedasbranchesdasfuncionalidadesna desenv. Por
isso,especialistasemintegra çãocontínuaaindacriticamousodesse
fluxo,argumentandoqueessaintegra çãoaindaéfeitatardedemais.Se
essefluxoforutilizadosembranchesporfuncionalidade,asitua çãoé
melhorada,masperderíamosasvantagensdeisolarmosocódigodas
funcionalidadesemdesenvolvimento.
10.4 Colaborando com projetos open source
com Fork ePullRequest
Utilizarumrepositóriocentraléalgobastantecomumparaprojetosinternos
deempresas.Jáparaprojetosopensourceprecisamosdeumamaneiramais
flexível,quenãonecessitedepermissõesdepushparaasdezenasoucentenas
decolaboresdonossoprojeto.
ServiçoscomooGithubpermitemqueumcolaboradorfa çaforksdeum
projeto,criandoumacópiapúblicadorepositório.Essacópiaficapublicada
naweb,servindocomoorepositórioremotodocolaborador.Assim,oscola-
boradorespodemcomitarmudan çasemsuascópiasdoprojeto,semprecisar
depermissõesdepushparaoprojetooriginal.
Ocolaboradorpodecriarumrepositóriolocalqueapontaparaoseure-
positórioremoto.Depoisdecomitaralgumasmodifica ções,podeserfeitoo
173
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 182

10.4. ColaborandocomprojetosopensourcecomForkePullRequest CasadoCódigo
pushparasuacópiadoprojeto.Sedesejar,podeatéliberaracessodepushao
seurepositórioremotoparaoutraspessoascolaboraremnasuacópia.
Quandoocolaboradorestiversatisfeitocomseucódigo,épossívelenviar
umpullrequestparaoprojetoprincipal.Omantenedordoprojeto,apessoa
responsávelpelorepositóriooriginal,poderevisaracópiapúblicadocolabo-
radoresugerirmelhoriasnocódigo.
Quandoomantenedorestiversatisfeito,épossívelaceitaropullrequest,
aplicandoasmudan çasnorepositóriooriginal.
Éinteressantequeocolaboradorfa çaseuscommitsemumabranchde
funcionalidade,separadada master. Dessamaneira,nahoradeaplicaro
pullrequest,omantenedordoprojetooriginalteriaoscommitsdocolabora-
doremumabranchseparada,podendocomitarmelhorias.Tambémépossí-
velutilizarbranchesporetapadedesenvolvimentoparaprojetosopensource
maiores.
Figura10.4:ForkePullRequest
Quandoutilizar?
Emprojetosopensourcedepequenooumédioporte.
Paraprojetoopensourcemuitograndes,commilharesdecolaboradores,
onúmerodepullrequestsseriatãograndequetornariainviávelousodesse
fluxo.
174
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 183

CasadoCódigo Capítulo10. ManeirasdetrabalharcomGit
Tambémépossívelutilizaressemodeloemprojetosdeempresas,nocaso
deprojetosquetenhamcolaboradoresexternose/ounãoconfiáveis.
Vantagens
• Nãoénecessáriodarpermissõesdepushparatodososcolaboradores
doprojeto.
• Éumbommodeloparaprojetosopensourcedepequenooumédio
porte.
Desvantagens
• Aintegraçãodasmudan çasdosforkséfeitademaneirabemtardia.
Possíveisconflitose/ouerrosseriamdescobertosapenasnahorade
aplicarmosopullrequest.
• Comosóháumrepositóriooriginalcom,provavelmenteapenasum
mantenedor,onúmerodepullrequestspoderiairacumulando. Para
projetosopensourcemuitograndesénecessáriaumaoutraabordagem.
10.5 Organizando projetos open source gigan -
tescos com Ditador eTenentes
ParaprojetosopensourcecomookerneldoLinux,quetemmilhõesdelinhas
decódigoemilharesdecolaboradores,utilizarofluxodetrabalhoanterior
torna-seinviável.
Onúmerodepullrequestscriadosseriaenorme.Comapenasumman-
tenedor,seriaimpossíveldarvazãoàscolabora ções.
Paraessetipodeprojeto,omantenedordoprojetooriginalpodeficar
comoumditadorbenevolente,quetemaúltimapalavrasobreocódigodo
projetomasqueaceitassugestões.NocasodoLinux,oditadoréLinusTor-
valds.
Oditadorelegeriacolaboradoresquesemostraramcompetentesnopas-
sadoparamanterrepositóriospúblicoscomcópiasdoprojeto.Essascópias,
175
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 184

10.5. OrganizandoprojetosopensourcegigantescoscomDitadoreTenentes CasadoCódigo
emgeral,teriamumfocoemalgummóduloespecíficodoprojeto.Oseleitos
peloditadorserviriamcomotenentes,recebendopullrequestsdosmilhares
deoutroscolaboradoreserevisandoocódigo,filtrandoapenasascolabora-
çõesrealmenteboas.
Umnovocolaboradorteriadeescolherumdosrepositóriosdostenentes
parafazerseuforkdoprojeto,provavelmenteconsiderandoomóduloemque
quercolaborar.Depoisdefeitosseuscommits,fariaopushparaseureposi-
tório. Então,poderiafazerumpullrequestparaseutenente,quefariauma
revisãoedariaumfeedback.
Quandoapropriado,otenentefariapullrequestsparaorepositóriodo
ditador,sinalizandoumpacoteinteressantedemudan ças.
Naverdade, okerneldoLinuxnãoutilizapullrequestsenemo
Github. NoGithub,háumacópiasóparaleituradorepositórioorigi-
nal.
Oscommitssãoenviadosdoscolaboradoresparaostenentesedos
tenentesparaoditadorLinuspore-mail.
Éusadoocomando git format-patch paracriarumarquivo
.patchcomumconjuntodecommits. Ospatchessãoenviadospor
e-mailcomocomando git send-mail. Então,deveserutilizadoo
comando git am paraaplicaroscommitsrecebidospore-mail.
Éinteressanteutilizarbranchesporfuncionalidadeeporetapadedesen-
volvimentoaoutilizaressefluxodetrabalho.
176
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 185

CasadoCódigo Capítulo10. ManeirasdetrabalharcomGit
Figura10.5:DitadoreTenentes
Quandoutilizar?
Paraprojetosopensourcegrandes,commilharesdecolaboradores.
Vantagens
• Assimcomonofluxoanterior,nãosãonecessáriaspermissõesdepush
paraorepositóriooriginal,doditador,nemdostenentes.
• Éumfluxoquefuncionabememprojetosopensourcedegrandeporte.
Desvantagens
• Éumfluxodetrabalhoextremamentecomplicado,querequermuita
familiaridadecomoGit.
• Aintegraçãoéfeitademaneiratardia,sóquandoforaplicadoopull
request(ouospatchesrecebidospore-mail).
177
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 186

E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 187

Capítulo11
Apêndice GitHubnoWindows
Conformevistonoscapítulosanteriores,nestelivroutilizamosoGitvialinha
decomando,pelo Terminal,nocasodoLinuxeMac,oupelo GitBash,no
casodoWindows.
Emborasejapossívelfazertudovialinhadecomando,muitosusuáriosdo
Git,principalmenteosqueutilizamoWindowsenãotêmohábitodeacessar
opromptdecomandos,nãogostamdessaabordagem,preferindoutilizá-lo
comoauxíliodealgumaaplica çãovisual.
Existemalgumasaplica çõesvisuaisparaoGitnoWindows,dentreelaso
GitHubforWindows,criadapelopessoaldoGitHub.
NestecapítuloveremoscomoinstalareutilizaroGitHubforWindows.
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 188

11.1. InstalandooGitHubforWindows CasadoCódigo
11.1 Instalando o GitHub forWindows
Primeiramentedevemosbaixaraaplica ção,oquefazemosacessandoosite
http://windows.github.comeclicandonobotão DownloadGitHubforWin-
dows:
Figura11.1:PáginadoGitHubforWindowscomobotãoparadownload
Versões suportadas
OGitHubforWindowsfuncionaapenasnoWindowsVista,Win-
dows7eWindows8.
Apósodownloaddoarquivo,devemosexecutá-lodandoum duplo
clique,eseráexibidaateladeinstala ção:
180
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 189

CasadoCódigo Capítulo11. Apêndice GitHubnoWindows
Figura11.2:Teladeinstala ção
Apósainstala çãoserconcluídaveremosumatelaondedevemosinformar
nossousuárioesenhacadastradosnoGitHub,eclicarnobotão Login:
181
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 190

11.1. InstalandooGitHubforWindows CasadoCódigo
Figura11.3:TelaondeinformamososdadosdelogindoGitHub
Napróximateladevemosinformaro NomeeoE-maildonossousuário
Giteclicarnobotão continue.Essepassoéequivalenteaexecutaroscoman-
dos git config --global user.name e git config --global
user.email.
182
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 191

CasadoCódigo Capítulo11. Apêndice GitHubnoWindows
Figura11.4:Teladeconfigura çãodosdadosdousuárioGit
Porfim,veremosatelaondeserãolistadososrepositóriosGitencontra-
dosemnossocomputador,sehouver,ouumamensageminformandoquenão
foramencontradosrepositórios. Nonossocasoclicaremosnobotão Skip,
poisvamosadicionarosrepositóriosposteriormente.
183
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 192

11.1. InstalandooGitHubforWindows CasadoCódigo
Figura11.5:TelalistandoosrepositóriosGit
Apósclicarnobotão Skip,seremosdirecionadosparaatelaprincipalda
aplicação,conhecidacomo Dashboard:
184
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 193

CasadoCódigo Capítulo11. Apêndice GitHubnoWindows
Figura11.6:Teladedashboard
Nestepontojátemosaaplica çãoinstalada,eseverificarmosa Área de
Trabalhoveremosqueforamadicionadosdoisnovosatalhos,sendoum
chamadoGitHub,queserveparaexecutaroGitHubforWindows,eoutro
chamadoGitShell,paraexecutaroGitviapromptdecomando:
185
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 194

11.2. Criandoumnovorepositório CasadoCódigo
Figura11.7:Áreadetrabalhocomosnovosatalhos
O GitHub for Windows também criará um novo diretório chamado
GitHub,localizadonapasta Documentosdousuário. Esseéodiretório
padrãoondeosnovosrepositóriosserãocriados.
11.2 Criando um novo repositório
AgoraquejátemosoGitHubforWindowsinstaladoeconfigurado,podemos
criarumnovorepositórioGit.Paraisto,bastaclicarnobotão +localizadona
telaprincipaldaaplica ção:
186
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 195

CasadoCódigo Capítulo11. Apêndice GitHubnoWindows
Figura11.8:Teladecria çãodenovorepositório
Devemospreencheronomedorepositórionocampo Name,enocampo
Local path escolherodiretórioondeorepositóriodeverásercriado,ou
deixarpreenchidocomodiretóriopadrão.
Notequehátambémumcampochamado Gitignore,ondepodemoses-
colheralinguagemdeprograma çãoutilizadanoprojeto,dentreasop ções
disponíveis,ecomistooarquivo .gitignoreserácriadoautomaticamente.
Apóspreencheroscampos,devemosclicarnobotão Createrepository,
aguardaracria çãodorepositórioeentãoveremosatelaDashboardlistando
onovorepositório:
187
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 196

11.3. Efetuandocommitsnorepositório CasadoCódigo
Figura11.9:Teladashboardcomonovorepositório
Reparequeatelaagoraestádivididaemtrêscolunas,ondenaprimeira
sãolistadososrepositóriosGit,nasegundaoscommitsdorepositóriojunta-
mentecomumformulárioparaefetuarumnovocommit,enaúltimacoluna
sãoexibidososarquivosdorepositório.
11.3 Efetuando commits no repositório
Vamosagoracriarumnovoarquivonorepositórioeemseguidaefetuarum
commit.Paraisso,acesseodiretóriodorepositórioecrieumnovoarquivo
chamado teste.htmlcomoseguinteconteúdo:
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<title>GitHub for Windows</title>
</head>
<body>
<h1>Bem vindo!</h1>
</body>
188
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 197

CasadoCódigo Capítulo11. Apêndice GitHubnoWindows
</html>
AgoraaovoltarparaoGitHubforWindowsveremosonovoarquivo
sendolistado:
Figura11.10:Teladashboardlistandoonovoarquivo
Paraefetuarocommitdoarquivo,bastadigitaramensagemdocommit
nocampo Summarye,opcionalmente,preencherumadescri çãomaisdeta-
lhadadocommitnocampo Description,eentãoefetuarocommitclicando
nobotão committomaster:
189
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 198

11.4. Detalhandooscommits CasadoCódigo
Figura11.11:Efetuandooprimeirocommit
Reparequenalistagemdosarquivosépossívelselecionarquaisdosar-
quivosserãocomitados.
11.4 Detalhando os commits
Vamosefetuarumnovocommitnorepositório. Paraisso,altereoarquivo
teste.htmladicionandooseguinteconteúdo:
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<title>GitHub for Windows</title>
</head>
<body>
<h1>Bem vindo!</h1>
<p>Alteracao qualquer</p>
</body>
</html>
Eapósistoregistreaaltera çãocomumnovocommit:
190
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 199

CasadoCódigo Capítulo11. Apêndice GitHubnoWindows
Figura11.12:Registrandoonovocommit
Apósefetuarocommitreparequeomesmoéexibidonalistagemdecom-
mits,ondeéexibidaamensagem,oautoreadataemquecadacommitfoi
realizado.
Aoclicaremalgumdoscommitsveremosasaltera çõesrealizadasnaquele
commitemespecífico:
Figura11.13:Detalhamentodasmodifica çõesrealizadasnocommit
191
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 200

11.4. Detalhandooscommits CasadoCódigo
Épossívelreverteralgumdoscommitsfacilmente,bastandoparaissocli-
carnocommit,enateladedetalhamentodocommitclicarnobotão revert:
Figura11.14:Botãoparareverterocommit
Apósclicarnobotãorevertumnovocommitseráefetuadoautomatica-
mente,desfazendoasaltera çõesdocommitselecionado:
192
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 201

CasadoCódigo Capítulo11. Apêndice GitHubnoWindows
Figura11.15:Teladetalhandoocommitderevert
11.5 Enviando o repositório para o GitHub
OGitHubforWindowspossuiintegra çãocomoGitHub,enospermitecom
istooenviodonossorepositóriolocalparaoGitHub.
ParaenviarorepositórioparaoGitHubbastaclicarnobotão Publish
Repository:
Figura11.16:BotãoparaenviarorepositórioparaoGitHub
Aoclicarnobotãoseráexibidaumatelaondepodemospreencheruma
descriçãodetalhadadorepositório, eescolherseorepositóriodeveráser
193
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 202

11.5. EnviandoorepositórioparaoGitHub CasadoCódigo
privado,casonossousuáriotenhacadastroemalgumdosplanospagosdo
GitHub.
Apóspreencherasinforma çõesbastaclicarnobotão Publishmoveis-
windowsenossorepositórioseráenviadoparaoGitHub:
Figura11.17:TelacomdetalhesdorepositórioaserenviadoparaoGitHub
SeacessarmosapáginadonossousuárionoGitHub,veremosqueore-
positóriofoienviadocorretamente:
194
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 203

CasadoCódigo Capítulo11. Apêndice GitHubnoWindows
Figura11.18:TeladonovorepositórionoGitHub
Agorasemprequeprecisarmossincronizarnossasaltera çõeslocaiscom
orepositórioremotonoGitHub,bastaclicarmosnobotão Sync:
Figura11.19:BotãoparasincronizarorepositóriolocalcomoGitHub
11.6 Trabalhando com branches
Tambémépossíveltrabalharcom branchesnoGitHubforWindows.Na
telaprincipalexisteumbotaoondepodemosgerenciarasbranchesdorepo-
sitório:
195
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 204

11.6. Trabalhandocombranches CasadoCódigo
Figura11.20:Botãoparagerenciarasbranches
Vamoscriarumanovabranchchamada testes,clicandonobotãocitado
anteriormente,digitandoonome testesnocampodetextodatela,econfir-
marclicandonobotão Createtestes:
Figura11.21:Teladecria çãodanovabranch
Apósanovabranchsercriadaelajáéselecionada,eseclicarmosnova-
mentenobotãoparagerenciarasbranches,veremosqueagoratemosduas
branchesnorepositório:
196
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 205

CasadoCódigo Capítulo11. Apêndice GitHubnoWindows
Figura11.22:Telalistandoasbranchesdorepositório
Vamosalterarnovamenteoarquivo teste.htmleemseguidaefetuar
umnovocommit,masdestavezocommitdeveráserrealizadonabranch
testes.
Altereoarquivo teste.htmladicionandooseguinteconteúdo:
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<title>GitHub for Windows</title>
</head>
<body>
<h1>Bem vindo!</h1>
<p>TESTE!</p>
<h2>Trabalhando com branches</h2>
</body>
</html>
Eentãoregistreaaltera çãocomumnovocommit,certificando-seantes
queabranch testesestáselecionada:
197
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 206

11.6. Trabalhandocombranches CasadoCódigo
Figura11.23:Telaparaefetuaronovocommit
Reparequeapósefetuarocommitomesmoéexibidonalistagemdecom-
mitsdabranch testes:
Figura11.24:Telalistandooscommitsdabranchtestes
Masaomudarmosparaabranch masterocommitseráescondido,uma
vezqueelefoiefetuadoapenasnabranch testes:
198
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 207

CasadoCódigo Capítulo11. Apêndice GitHubnoWindows
Figura11.25:Telalistandooscommitsdabranchmaster
Efetuandoomergedoscommits
NoGitHubforWindowstambémépossívelefetuarmerges,paramesclar
asaltera çõesdeduasbranchesdistintas.
Vamosefetuaromergedabranch testesnabranch master.Paraisso,
devemosclicarnobotãodegerenciarasbranches,enatelaqueseráaberta
clicarnobotão Manage:
Figura11.26:TelacombotãoManage
Aoclicarnestebotãoveremosateladegerenciamentodasbranchesdo
repositório,naqualserãolistadastodasasbranchesexistentes,enapartein-
199
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 208

11.6. Trabalhandocombranches CasadoCódigo
feriorexistemdoiscamposutilizadosparafazeromerge:
Figura11.27:Teladegerenciamentodebranches
Pararealizaromergedevemosarrastaresoltarasbranchesdesejadasnos
camposcitadosanteriormente,sendoquenonossocasoabranch testes
deveserarrastadaparao primeirocampo ea masterparao segundo
campo,poisqueremosfazeromergedabranch testesnabranch master:
200
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 209

CasadoCódigo Capítulo11. Apêndice GitHubnoWindows
Figura11.28:Camposparasele çãodasbranches
Apósarrastarasbranchesparaoscamposdevemosclicarnobotão Merge
paraconfirmaraopera ção,eumamensagemseráexibidaaofinaldoprocesso.
Agora se voltarmos para a tela principal e mudarmos para a branch
master,veremosqueocommitefetuadonabranch testeseráexibidona
listagem,confirmandoassimqueomergefoiefetuadocomsucesso.
201
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 210

ÍndiceRemissivo CasadoCódigo
ÍndiceRemissivo
.gitignore,27
Branch,94
Branchremota,114
Branches por etapa de desenvolvi-
mento,167
Branchesporfuncionalidade,162
Configuraçõesbásicas,6
Conflito,143
Ditador/Tenentes,175
Featurebranches,162
fork,89
Fork/PullRequest,173
Git,3
gitadd,9,22
gitbranch,94
gitbranch-r,114
gitcheckout,52,98
gitclone,17,66
gitcommit,10,29
gitdiff,39
gitfetch,123
gitinit,8,20
gitlog,11,36
gitmerge,106
gitmergetool,152
gitmv,49
gitpull,67,130
gitpull–rebase,130
gitpush,15,65
gitrebase,108
gitrebase–continue,150
gitremote,15,64
gitremoteadd,63
gitremoteremove,64
gitremoterename,64
gitremoteset-url,64
gitreset,54
gitrevert,56
gitrm,47
gitstatus,9,22
gittag,138
GitHub,12,72
GitHubforWindows,179
Instalação,5
OpenSource,173,175
Protocolos,68
pullrequest,89
Repositórioremoto,62
202
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com

## Página 211

CasadoCódigo ÍndiceRemissivo
serviçosdehospedagemdeprojetos,
72
SistemasdeControledeVersão,2
Stage,24
Topicbranches,162
203
E-book gerado especialmente para Patryck Peterson Costa Gratão - kyroscoolg@gmail.com