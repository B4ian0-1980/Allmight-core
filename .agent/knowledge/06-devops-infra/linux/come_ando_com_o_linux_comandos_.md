---json
{
  "id": "come_ando_com_o_linux_comandos_",
  "title": "Começando_com_o_Linux_Comandos,",
  "categoria": "06-devops-infra",
  "subcategoria": "linux",
  "resumo": "**Arquivo Original:** `Começando_com_o_Linux_Comandos,.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "ando",
    "com",
    "comandos",
    "come",
    "devops",
    "infra",
    "linux"
  ],
  "perguntas_tipo": [
    "Como utilizar Começando_com_o_Linux_Comandos,?",
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

# Começando_com_o_Linux_Comandos,

> **Arquivo Original:** `Começando_com_o_Linux_Comandos,.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 2

CasadoCódigo
Agradecimentos
DedicoestetrabalhoàminhaesposaMychelle,obrigadoporcompreenderaminha
ausênciaquandonecessárioepeloapoioemtodososmomentos.Aosmeuspaispelo
constanteapoioeincentivo.
AgradeçoaCasadoCódigopelaoportunidadedeescreveresselivro,especial-
menteaoPauloSilveirapelosensinamentoseopiniõesdemuitovalorsobreocon-
teúdoeorganizaçãodomesmo.
AgradecimentosespeciaisaosamigosFranciericAlvespormostrarocaminho
daspedraseFredPortelaporajudaratrilharessecaminho. Agrade çotambéma
todososamigosquemeajudaramdiretaouindiretamentenaconstruç ãodolivro.
Porfim,agrade çoaDeuspormaisestaoportunidade.
i

## Página 4

CasadoCódigo Sumário
Sumário
1 Introdução 1
1.1 Paraqueméestelivro . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2 OqueéLinux? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.3 PorqueoUbuntu? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.4 InstalaçãodoUbuntu . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.5 Navegandononovosistemaoperacional . . . . . . . . . . . . . . . . . 12
2 Mãonamassa:conhecendooShell 17
2.1 OqueéoShell? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
2.2 PrimeirocontatocomoShell . . . . . . . . . . . . . . . . . . . . . . . . 17
2.3 Trabalhandocomdiretórios . . . . . . . . . . . . . . . . . . . . . . . . 19
2.4 Trabalhandocomarquivos . . . . . . . . . . . . . . . . . . . . . . . . . 23
2.5 Pedindoajuda . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
2.6 Localizandoarquivosnosistema . . . . . . . . . . . . . . . . . . . . . . 30
2.7 Umpasseioforadoambientegráfico . . . . . . . . . . . . . . . . . . . 32
3 Manipulandoarquivos 33
3.1 OeditorVim . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
3.2 OeditorNano . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
3.3 TrabalhandocomoCat . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
3.4 Exibindooinícioeofimdearquivos . . . . . . . . . . . . . . . . . . . 44
4 Compactaçãoedescompactaç ãodearquivos 47
4.1 Conhecendootar . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
4.2 Conhecendoogzip/gunzip . . . . . . . . . . . . . . . . . . . . . . . . . 51
4.3 Conhecendoozip/unzip . . . . . . . . . . . . . . . . . . . . . . . . . . 51
iii

## Página 5

Sumário CasadoCódigo
5 Entendendoaestruturadediretórios 53
5.1 Aestruturadediretórios . . . . . . . . . . . . . . . . . . . . . . . . . . 53
5.2 Osdiretóriosopcionais . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
5.3 Osdiretórios/proce/sys . . . . . . . . . . . . . . . . . . . . . . . . . . 55
6 Administraçãodeusuários 57
6.1 Gerenciandousuários . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
6.2 Permissões . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
6.3 Atribuindopermissões . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
6.4 Criandogrupos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
6.5 Criandousuários. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
6.6 Alterandogrupos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
7 Instalandopacoteseaplicativos 71
7.1 Gerenciadordepacotes . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
7.2 GerenciandopacotescomAPT . . . . . . . . . . . . . . . . . . . . . . 76
8 Prática,instalandoApache,PHPeMySQL 81
8.1 InstalandooApache . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
8.2 Linkandoarquivos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84
8.3 InstalandoeconfigurandooMySQL . . . . . . . . . . . . . . . . . . . 85
8.4 InstalandoeconfigurandooPHP . . . . . . . . . . . . . . . . . . . . . 88
9 Entendendoprocessos 91
9.1 Oquesãoprocessos? . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91
9.2 Oprocessoinit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92
9.3 Aidentificaç ãodeprocessos . . . . . . . . . . . . . . . . . . . . . . . . 92
9.4 Verificandoprocessos . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
9.5 Oquesãosinaisdeprocessos? . . . . . . . . . . . . . . . . . . . . . . . 98
9.6 Processosesuasprioridades . . . . . . . . . . . . . . . . . . . . . . . . 101
10 IntroduçãoaShellScript 103
10.1 Oprimeiroscript . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
10.2 Executandooscript . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
10.3 Operaçõesbásicas. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
iv

## Página 6

CasadoCódigo Sumário
10.4 Estruturasdecontrole . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
10.5 Realizandoumbackupagendado . . . . . . . . . . . . . . . . . . . . . 108
10.6 Umsimplesscriptdebackup . . . . . . . . . . . . . . . . . . . . . . . . 111
10.7 Personalizandooseushell:PS1,PATHeoutros . . . . . . . . . . . . . 112
10.8 Alias. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
10.9 Arquivosdeconfiguração. . . . . . . . . . . . . . . . . . . . . . . . . . 115
11 Compilandoarquivosfonte 117
11.1 Aconfiguração . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
11.2 Compilandonaprática. . . . . . . . . . . . . . . . . . . . . . . . . . . 118
12 Oqueestudaralém? 123
12.1 SSH–SecureShell. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
12.2 Proteçãoporfirewall . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
12.3 UpstarteMonit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
12.4 Documentaçõesemportuguês. . . . . . . . . . . . . . . . . . . . . . . 128
12.5 Tirardúvidas. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129
v

## Página 8

Capítulo1
Introdução
“Não há conhecimento que não tenha valor. ”
–EdmundBurke
Raramenteutilizamosumsistemaoperacionaldiretamente.Oqueusamossão
programas,queutilizamrecursoscomoarquivos,internetememória,ambosprovi-
dospelosistemaoperacional.QuandovocêusaoInternetExplorereoWord,ambos
pedemaoscomponentesinternosdoWindows,queéoverdadeirosistema.
OWindowséumdosdiversossistemasoperacionais.OLinuxéoutrodeles.
OLinuxganhoumuitapopularidadeehojeencontra-seamplamentedifundido
nosservidoresdegrandessistemas.Instalarbancosdedadoseservidoresweb,além
degerenciá-los,éumatarefacomumerelativamentefácilemsistemasLinux.Du-
ranteesselivroaprenderemosatrabalharcomarquivos,configurarservidores,com-
pilarpacotes,criarscriptserealizartarefasdodiaadiaqueumadministradorcos-
tumafazer.
Amelhorformadepensarem Sistema Operacionaléimaginarumconjuntode
váriosprogramasunidos,aguardandoseremusados.Comessadefiniç ãoemmente

## Página 9

1.1. Paraqueméestelivro CasadoCódigo
podemosdizerquedistribuições LinuxcomoSlackware,Debian,Ubuntu,RedHat
eFedorasãoumaglomeradodeprogramaseconfiguraçõesespecíficas.Sãosabores
diferentesdoLinux.Hávantagensedesvantagensemcadaumadelas.
HátambémoAndroid,queadaptouokerneldoLinuxparacriarseupróprio
sistemaoperacionalfocadoemdispositivosmóveis.
1.1 Para quem é este livro
Estelivrotemoobjetivodeapresentarumaintroduç ãoao Linuxdeformabastante
práticaecomusodemuitosexemplos. Érecomendadoparainiciantesepodeser
umbomguiadeconsultasparausuárioscommaisexperiência.
Existeumalistadediscussõesaqui:
http://lista.infoslack.com
Sinta-seàvontadeparamandardúvidassobreolivro. Alémdisso,sugestões,
críticasecorre çõesserãobemvindas.
1.2 O que éLinux?
Linuxéo kernel,ocomponentecentral,ocoraç ãodosistema. Eleéresponsável
porconectarosprogramasaohardware.Penseno Linuxcomopartecentraldeum
Sistema Operacional.
ApenascomoKernelnãoteríamosmuitasop ções. Precisamosdeprogramas,
configurações,interfacegráficaedriversparatirarumproveitorealdessesistema
operacional.
Paraisso,utilizaremosadistribuiç ãodeLinuxconhecidacomoUbuntu.
http://www.ubuntu.com/
1.3 Por que oUbuntu?
Pensandoeminiciantes,escolhioUbuntuparausardurantetodoolivro,poiséum
Sistema Operacionalfácildeusar,instalareconfigurar,alémdepossuirumavasta
documentação.
Nósvamos,nessecapítulo,realizarainstalaç ãodoUbuntu.Masháoutrasop-
ções,nocasodevocêpreferirsótestá-lo.
IssoépossívelpoisasversõesparadownloaddoUbuntusão Live CDepossibilita
quevocêexecutetodoosistemaoperacionalseminstalarnada,tudoseráexecutado
diretamentenamemóriaRAM.
2

## Página 10

CasadoCódigo Capítulo1. Introdução
Outraop çãoéfazerusodemáquinasvirtuais,comoéocasodoVirtualBox
https://www.virtualbox.org/eVMware http://www.vmware.com/br/,eterumsis-
temaoperacionalvirtualizadodentrodeoutro.
Existeoutrasoluç ãomaiselegantequefazusotantodoVirtualBoxquantodo
VMwarenoseubackground,oVagrant http://www.vagrantup.com/.
1.4 Instalação do Ubuntu
OUbuntufoiprojetadoparaterumainstalaç ãorápidaemuitofácil.Duranteeste
processoelepodebaixardainternetalgumasatualizaçõesdosistemaepacotesde
linguagemparaoseuidioma.Dependendodavelocidadedasuaconexãootempo
dainstalaçãopodedemorarumpouco.
Apresentareiaformapadrãodeinstalaç ãodoUbuntusemconexãocomainter-
net,masvocêpodeoptarportestá-loantesdeinstalarexecutando-odiretodeum
CD/DVDoupendrive.
AseguirtemosateladeboasvindasdoinstaladordoUbuntu:
Figura1.1:Teladeboasvindas
3

## Página 11

1.4. InstalaçãodoUbuntu CasadoCódigo
Nessatelatemosaop çãodeescolhadoidioma—nocasoselecionei Português
do Brasil.Cliqueem Instalar o Ubuntuparacontinuarmosoprocessodeinstalaç ão.
AgoraoUbuntuiráverificaraquantidadedeespaçodisponívelemdisco. Ele
precisade,nomínimo,4.4GBparaprosseguirainstalaç ão.
Figura1.2:PreparandoparainstalaroUbuntu
Notequenãomarqueiasop çõesdebaixaratualizaçõesenquantoinstalaeins-
talarprogramasdeterceirospodefazerainstalaç ãodemorarumpoucoalémdo
previsto.
Vamosprosseguirescolhendoagoraotipodeinstalaç ão.
4

## Página 12

CasadoCódigo Capítulo1. Introdução
Figura1.3:Sele çãodetipodeinstalaç ão
Observeamensagemquediz Atualmentenãofoidetectadonenhumsistema
operacionalnestecomputador..Comonãotenhonadainstaladomarqueiaop ção
deapagarodiscoeinstalaroUbuntu.
Outrasop çõessãooferecidasquandojápossuímosumsistemainstalado,como
instalaroUbuntuaoladodoWindowsousubstituiroWindowscompletamentepelo
Ubuntu.
Nasequência,oinstaladorinformaquevaiapagarodiscointeiroeprosseguir:
5

## Página 13

1.4. InstalaçãodoUbuntu CasadoCódigo
Figura1.4:Discoqueseráusado
Duranteoprocesso,oinstaladordoUbuntusolicitaasualocalizaç ãoparasele-
çãodefusohorário.
6

## Página 14

CasadoCódigo Capítulo1. Introdução
Figura1.5:Sele çãodefusohorário
Emseguida,devemosescolherolayoutdonossoteclado.Porpadrão,oinstala-
dordoUbuntutentareconhecerotipodetecladoautomaticamente.
7

## Página 15

1.4. InstalaçãodoUbuntu CasadoCódigo
Figura1.6:Escolhadolayoutdoteclado
Antesdeconcluirainstalaç ão,osistemapedealgumasinformações:oseunome,
nomedocomputador,umnomedeusuárioesenha.
Existeaop ção Criptografar minha pasta pessoal,queinsereumapro-
teçãocomplementaraosseusarquivosarmazenadosnodisco.
8

## Página 16

CasadoCódigo Capítulo1. Introdução
Figura1.7:Informandoosdadosdousuário
Oprocessodefinalizaç ãopodelevaralgunsminutoseoinstaladoroferecenesse
tempoumguiailustradosobreoUbuntu.
9

## Página 17

1.4. InstalaçãodoUbuntu CasadoCódigo
Figura1.8:Processodeinstalaç ão
Aofinalizar,teremosamensageminformandoqueénecessárioreiniciarocom-
putador.Cliqueem Reiniciar agora.
10

## Página 18

CasadoCódigo Capítulo1. Introdução
Figura1.9:Finalizandoainstalaç ão
OsistemairáreiniciarocomputadorefinalmenteteremosoUbuntuprontopara
uso. Daquiprafrentetudooqueveremosnolivroseráexecutadonoterminalde
comandos.
11

## Página 19

1.5. Navegandononovosistemaoperacional CasadoCódigo
Figura1.10:Ubuntudesktop
1.5 Navegando no novo sistema operacional
Vamosexplorarumpoucoonovosistemaoperacional,abrindoalgunsprogramas:
12

## Página 20

CasadoCódigo Capítulo1. Introdução
Figura1.11:Algunsaplicativosabertos
Experimenteonovoambiente,abraalgunsaplicativoscomonoexemploante-
rior.
Observecomoéfamiliarcomoutrossistemasoperacionais,editordetexto,a
calculadora,ogerenciadordepastasearquivos,obrowser,configuraçõesderede
etc.
Porpadrão,oUbuntujáinstalaumasuítedeaplicativosdeescritóriogratuita:o
LibreOffice,quepossuicompatibilidadecomosarquivosformatadosnoMicrosoft
Office.Confira:
13

## Página 21

1.5. Navegandononovosistemaoperacional CasadoCódigo
Figura1.12:LibreOffice,equivalentesaoWordeExcel
Seestiverprocurandoumsemelhanteao notepaddoWindows,oUbuntupos-
suio Gedit:
14

## Página 22

CasadoCódigo Capítulo1. Introdução
Figura1.13:Gedit,equivalenteaonotepaddoWindows
Comelevocêpodecriarealterararquivos.Nesselivroveremosasformasmais
comunsdefazerisso,queseráatravésdeeditoresmenosvisuais,porémpoderosos.
Paraalterarasconfiguraçõesdesistemaepersonalizardeacordocomsuaspre-
ferências,porexemplo,ovisual,configuraçõesderede,teclado,mouse,dataemuito
mais,váem Configurações do sistema:
15

## Página 23

1.5. Navegandononovosistemaoperacional CasadoCódigo
Figura1.14:Configuraçõesdosistema
VocêpodenotarqueusamosoUbuntucomoumsistemaoperacionaltradicio-
nal,assimcomonossosamigoscostumamusaroWindows.
Apesardessafacilidade,focaremosolivronousoparadesenvolvedoreseadmi-
nistradoresdesistemas.Semdúvida,aferramentaprincipaléo shelldoLinux,que
veremosagora.
16

## Página 24

Capítulo2
Mãonamassa:conhecendooShell
Nestecapítuloveremosumpoucosobreo Shelldeformaprática,algunscomandos
denavegação,informação,buscaemanipulaç ãodearquivosediretórios.
2.1 O que é oShell?
O shelléainterfacedeacessoaosistemaoperacional,ondeépossívelinteragir
comosistemapormeiodecomandosdigitadosdoteclado. Elepodeseracessado
pelomodográficoediretamenteemmodotexto. Veremosdetalhessobreissono
decorrerdolivro.
2.2 Primeiro contato com o Shell
ApósinstalaroUbuntueabriroterminaldecomandos,vocêsedeparacomase-
guinteimagem:

## Página 25

2.2. PrimeirocontatocomoShell CasadoCódigo
Figura2.1:PrimeirocontatocomoShell
Masoquesignificaisso?
•ubuntuéonomedousuário;
•@servidoréonomedohost;
•~éaabreviaçãoparaapastadousuário;
•$indicaqueousuárionãopossuipoderesdeadministrador.
Agoraqueentendemososignificadodo promptqueaparece,vamostestaral-
gunscomandoseveroqueacontece.
daniel@casadocodigo:~$ pwd
/home/daniel
daniel@casadocodigo:~$ whoami
daniel
daniel@casadocodigo:~$ date
Thu Sep 26 21:30:07 UTC 2013
daniel@casadocodigo:~$
18

## Página 26

CasadoCódigo Capítulo2. Mãonamassa:conhecendooShell
Aoexecutarocomando pwd,oretornofoiexatamenteodiretórioqueestamos
atualmentechamandode current.
Ocomando whoamiexibeonomedousuárioatualqueestamosusandoeo
dateretornaadataatual.
Nãosepreocupeaindasobreospoderesdeadministrador sudo,veremosisso
maisadiante.
Semprequequisermosdigitaralgumcomandoquejátenhasidoexecutadoan-
tes,podemosfazerusodatecla direcional para cima ou direcional para
baixo.Issopossibilitanavegarmosporumalistadecomandosquejáforamexecu-
tados.
Existeaop çãodevermosessalistacompleta,graç asao history,quecriaum
históricomemorizandotudooquejádigitamosno shell:
daniel@casadocodigo:~$ history
1 pwd
2 whoami
3 date
4 clear
5 history
daniel@casadocodigo:~$
Outrarecomendaçãoparaumusomaisprodutivodo shelléutilizaratecla
tab,quepossuiafun çãodeautocompletar.
2.3 Trabalhando com diretórios
ParaconhecermaissobreoShell,vamosnavegarporalgunsdiretórioseexecutar
algunscomandosbásicosparatrabalharcomarquivos.Àmedidaqueformosnave-
gandonaestrutura Linuxentenderemoscomoeleéorganizado.
Antesdecontinuar,observeaestruturadediretóriosnoambientegráficodo
Ubuntu:
19

## Página 27

2.3. Trabalhandocomdiretórios CasadoCódigo
Figura2.2:Listagemdediretóriosnapastahome
Emalgunssistemasoperacionais,éutilizadootermo pasta(folder)emvezde
diretório(directory).
daniel@casadocodigo:~$ cd /
daniel@casadocodigo:/$
Aoexecutarocomando cd / estamosinformandoaoShellquequeremosna-
vegaratéodiretório /,maisconhecidocomoraiz(oudiretório root).Ainstruç ão
cdéoquepermiteanavegaç ãoentrediretórios.
Jáocomando lslistaosarquivosediretórios,nestecasonodiretórioraiz,que
éondeestamos.Façaoteste!
daniel@casadocodigo:/$ ls
bin home media Repos selinux usr
boot initrd.img mnt root srv vagrant
dev lib opt run sys var
etc lost+found proc sbin tmp vmlinuz
daniel@casadocodigo:/$
20

## Página 28

CasadoCódigo Capítulo2. Mãonamassa:conhecendooShell
Amesmalistagemnoambientegráfico:
Figura2.3:Listagemdodiretórioraiz
Nãosepreocupe,veremoscadaumdessesdiretóriosdalistagemdeformadeta-
lhadaemumcapítuloapropriado.
Suainstalaçãopodelistararquivosumpoucodiferentes,nãotemproblemaal-
gum.Elesvariamdeacordocominstalaç ão.
Percebaquealgumasvezes,apósdigitarmoscomandosoulistarmosconteúdo
dediretórios,ateladoterminalficarepletadepalavras.Parafazeralimpezadatela
usamosocomando clear.Testeocomandoevejaoresultado.Oatalho Ctrl +
ltemomesmoefeito.
Vamosretornaraonossodiretóriodeusuárioqueficaem /home/ubuntu,que
éconhecidopor home.Paraissovamosusaro cd.
Pararetornar,temosalgumasop çõesparacombinarcomocomando cd:
•~apontadiretoparaodiretório homedousuário(ou pasta do usuário);
•/home/ubuntuéocaminhoabsoluto;
21

## Página 29

2.3. Trabalhandocomdiretórios CasadoCódigo
•-últimodiretórioondeesteve.
Noexemploaseguirusaremoso cd - pararetornaraodiretório home:
daniel@casadocodigo:/$ ls
bin home media Repos selinux usr
boot initrd.img mnt root srv vagrant
dev lib opt run sys var
etc lost+found proc sbin tmp vmlinuz
daniel@casadocodigo:/$ cd -
/home/daniel
daniel@casadocodigo:~$
Testeasoutrascombinaçõeseseficarperdidoretorneimediatamenteaodiretó-
riohome,executando cd ~.
Agoraquevoltamosaonossodiretóriohome,vamoscriarumnovodiretório
usandoocomando mkdir.Chamaremosde aplicativos:
daniel@casadocodigo:~$ pwd
/home/daniel
daniel@casadocodigo:~$ mkdir aplicativos
daniel@casadocodigo:~$ ls
aplicativos
daniel@casadocodigo:~$
Agoraqueodiretóriofoicriado,vamosentraresairdeletestandomaisduas
novasformasdenavegaç ãousandoo cd,seguidodonomedodiretório:
daniel@casadocodigo:~$ ls
aplicativos
daniel@casadocodigo:~$ cd aplicativos/
daniel@casadocodigo:~/aplicativos$ cd ..
daniel@casadocodigo:~$
Observequenãopassamoso caminhoabsoluto parao cd,apenaso caminho
relativo,poisodiretórioemquequeremosentraré relativoaoqueestamosatual-
mente.
Alternativamente, você poderia sim ter utilizado o caminho abso-
luto, colocando todo o diretório, desde a raiz, no comando, fazendocd
/home/daniel/aplicativos.
Valelembrarqueodiretório danieldependedonomedeusuárioquevocê
criouduranteainstalaç ãodoUbuntu.
Paravoltar,usamoso cd .. quesignifica volte para o diretório anterior.
22

## Página 30

CasadoCódigo Capítulo2. Mãonamassa:conhecendooShell
2.4 Trabalhando com arquivos
Vamoscriarumarquivonodiretório homedonossousuárioe,emseguida,movê-lo
paradentrododiretórioquefoicriado,o aplicativos:
daniel@casadocodigo:~$ ls
aplicativos
daniel@casadocodigo:~$ touch meu_arquivo
daniel@casadocodigo:~$ ls
aplicativos meu_arquivo
daniel@casadocodigo:~$ mv meu_arquivo aplicativos/
daniel@casadocodigo:~$ ls
aplicativos
daniel@casadocodigo:~$ ls aplicativos/
meu_arquivo
daniel@casadocodigo:~$
Utilizando o comando touch, criamos um novo arquivo chamado
meu_arquivo. Em seguida usamos o comandomv, passando como parâme-
troonomedoarquivoeodestinoparamoveroarquivoquecriamos.Notequeao
movermosoarquivodelugarelenãoficamaisdisponívelondeestavaantes.
Nocasoanterioro meu_arquivofoimovidoparaodiretório aplicativos,
masesequisermosterumacópiadessearquivonapasta homedonossousuário?
Paraisso,existeocomando cp,quefazumacópiadoarquivomantendooori-
ginal.Elefuncionadeformaparecidacomo mv:
daniel@casadocodigo:~$ ls
aplicativos
daniel@casadocodigo:~$ cp aplicativos/meu_arquivo .
daniel@casadocodigo:~$ ls
aplicativos meu_arquivo
daniel@casadocodigo:~$ ls aplicativos/
meu_arquivo
daniel@casadocodigo:~$
Observe a legibilidade: estamos falando para o shell copiar o arquivo
meu_arquivoqueseencontraem aplicativosparaodiretórioatual,etudo
foifeitosemsairdapasta home. Omesmopoderiaserfeitodeoutraforma: cp
aplicativos/meu_arquivo /home/daniel,passandoocaminhoabsolutodo
diretóriodestinoparaacópia.
23

## Página 31

2.4. Trabalhandocomarquivos CasadoCódigo
Antesdeprosseguirvamosverumpoucosobrearquivosocultos. Umarquivo
ocultoéidentificadoporum "."noiníciodonome,porexemplo( .profile).
Arquivosocultosnãoaparecememlistagensnormaisdediretórios,paraissousamos
umparâmetronocomando ls, ls -a ou,noformatomaisdetalhado, ls -la.
NoUbuntuexisteumatalhoparaessecomando,o ll.
Vamoslistarosarquivosocultosdapasta home:
daniel@casadocodigo:~$ ls -a
. aplicativos .bash_logout meu_arquivo
.. .bash_history .bashrc .profile
daniel@casadocodigo:~$
Agoravamoslistarosarquivosocultosdeformamaisdetalhada:
daniel@casadocodigo:~$ ls -la
total 28
drwxr-xr-x 3 daniel daniel 4096 Sep 27 01:29 .
drwxr-xr-x 4 root root 4096 Sep 11 02:35 ..
drwxrwxr-x 2 daniel daniel 4096 Sep 27 01:28 aplicativos
-rw------- 1 daniel daniel 697 Sep 26 21:58 .bash_history
-rw-r--r-- 1 daniel daniel 220 Sep 11 02:35 .bash_logout
-rw-r--r-- 1 daniel daniel 3486 Sep 11 02:35 .bashrc
-rw-rw-r-- 1 daniel daniel 0 Sep 27 01:29 meu_arquivo
-rw-r--r-- 1 daniel daniel 675 Sep 11 02:35 .profile
daniel@casadocodigo:~$
Nãosepreocupecomtodasessasinformaçõesexibidasnalistagemdetalhada,
veremososignificadodecadaumaemcapítulosposteriores.Agoracontinuaremos
atrabalharcomarquivos.
Ocomando mvtambémservepararenomearumarquivo. Vamosrenomear
oarquivoquecriamos meu_arquivopara meu_arquivo.txt,adicionandoa
extensão .txt:
daniel@casadocodigo:~$ ls
aplicativos meu_arquivo
daniel@casadocodigo:~$ mv meu_arquivo meu_arquivo.txt
daniel@casadocodigo:~$ ls
aplicativos meu_arquivo.txt
daniel@casadocodigo:~$
24

## Página 32

CasadoCódigo Capítulo2. Mãonamassa:conhecendooShell
Nossoarquivoatualmenteestávazio.Vamosescreveralgumtextoneleeconhe-
cermaisumcomando,o echo.O echoéutilizadoparaexibirmensagensnatela
ouemumarquivo:
daniel@casadocodigo:~$ echo "Exibindo mensagem na tela"
Exibindo mensagem na tela
daniel@casadocodigo:~$
Agoravamosescreveralgononossoarquivocomo echo,masparaissoéne-
cessáriofazerusodoparâmetro >,confira:
daniel@casadocodigo:~$ echo Escrevendo no arquivo > meu_arquivo.txt
Notecomoélegível,ainstruç ãopodeserlidadaseguinteforma: escreva o texto
“Escrevendo no arquivo” em meu_arquivo.txt.
Agorapodemosverificarotextoquefoiinseridononossoarquivo,comoco-
mando cat:
daniel@casadocodigo:~$ ls
aplicativos meu_arquivo.txt
daniel@casadocodigo:~$ cat meu_arquivo.txt
Escrevendo no arquivo
daniel@casadocodigo:~$
O catfazpartedeumacole çãodecomandosparamanipulararquivos,veremos
maisdetalhessobreelenopróximocapítulo.
Éinteressantesaberinformaçõessobreotipodearquivo,paraissoexisteoco-
mando file:
daniel@casadocodigo:~$ ls
aplicativos meu_arquivo.txt
daniel@casadocodigo:~$ file meu_arquivo.txt
meu_arquivo.txt: ASCII text
daniel@casadocodigo:~$ file aplicativos/
aplicativos/: directory
daniel@casadocodigo:~$
Como filepodemosverqueonossoarquivoédotipo text,nota-setambém
queaoexecutaro fileemumdiretório,eleinformaotipo directory.Issoacontece
poisnoLinuxtudoéconsideradoumarquivo.
Agoraquejásabemoscriararquivos,emanipulardeformabásica,horadeapren-
deraremover.Usandoo rmpodemosdeletararquivosediretórios:
25

## Página 33

2.5. Pedindoajuda CasadoCódigo
daniel@casadocodigo:~$ ls
aplicativos meu_arquivo
daniel@casadocodigo:~$ rm meu_arquivo
daniel@casadocodigo:~$ ls
aplicativos
daniel@casadocodigo:~$ rm aplicativos/
rm: cannot remove `aplicativos/': Is a directory'`
daniel@casadocodigo:~$
Notequeconseguimosdeletaroarquivo meu_arquivo,porémaotentarremo-
verodiretório aplicativosrecebemosumamensagemdeerroinformandoque
nãofoipossível,poistrata-sedeumdiretório.
Ocomando rmdiréresponsávelporremoverdiretórios,massomentediretó-
riosvazios. Nonossocaso aplicativoscontémumacópiade meu_arquivo,
entãooquefazer?
Usandoo rm -r vamosconseguirremoverodiretório,o -réumaop çãodo
comando rmquefazeleremoverdiretóriosquetenhamconteúdodeformarecur-
siva:
daniel@casadocodigo:~$ ls
aplicativos
daniel@casadocodigo:~$ rm -r aplicativos/
daniel@casadocodigo:~$ ls
daniel@casadocodigo:~$
Obviamente,tenhamuitocuidadoaoutilizá-lo!
2.5 Pedindo ajuda
SemprequeprecisarmosdeajudanoLinux,podemosusaro helpoupodemos
incluiroparâmetro --help,queésuportadonamaioriadoscomandos.Vejamos
algunsexemplos:
daniel@casadocodigo:~$ help cd
cd: cd [-L|[-P [-e]]] [dir]
Change the shell working directory.
Aousarocomando help,estoupedindoajudaao shellparaquemeinforme
maisdetalhessobrecomousarumdeterminadocomando,nestecasoo cd.
Comofalei,outraformadeajudaéoparâmetro --help,quepodesercomple-
mentoparaamaioriadoscomandos.Vejacomoumexemplodeuso:
26

## Página 34

CasadoCódigo Capítulo2. Mãonamassa:conhecendooShell
daniel@casadocodigo:~$ ls --help
Usage: ls [OPTION]... [FILE]...
List information about the FILEs (the current directory by default).
Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.
NoLinuxadocumentaç ãopadrãoéchamadade man pages,elacontémajuda
paratodososcomandospadrões. Vamosaoteste,executeocomando man ls e
vejaoqueeleretorna:
daniel@casadocodigo:~$ man ls
Figura2.4:Exibindoadocumentaç ãodeajudadeumcomando
O manapresentatodosostópicosdomanuallinux,deformasemelhanteaum
manualimpressoeestápresenteemqualquerdistribuiç ãolinux.Oambienteapre-
sentadopelo manaceitacomandosparanavegaç ãoebuscanadocumentaç ão:
•hmostraaajudadocomandoman,vejaparamaisdetalhes;
•qsairdoman;
•/procuraporumtextonadocumentaç ãoapresentada;
•favançaumatela;
•bvoltaumatela.
27

## Página 35

2.5. Pedindoajuda CasadoCódigo
Testecadaumdoscomandoseverifiqueosresultados,tecle hparavertodasas
opçõesdo man:
Figura2.5:Verificandoasop çõesdoman
Tecle qparavoltaradocumentaç ãoqueestavaabertaefaç aumabuscapor
algumtextonadocumentaç ão,useocomando /:
28

## Página 36

CasadoCódigo Capítulo2. Mãonamassa:conhecendooShell
Figura2.6:Buscaportextonadocumentaç ão
Podemosobservarqueotextoquebuscamosfoiselecionadodestacandoacor
defundo:
Figura2.7:Resultadodabuscaportexto
Parasair,tecle q.
29

## Página 37

2.6. Localizandoarquivosnosistema CasadoCódigo
Claro,adocumentaç ãoétodaeminglêseestetipodetelapodenãosermuito
amigável. Nainternet,muitasvezesépossívelencontrarexemplosetutoriaismais
simplessobrecadacomando,atémesmoemportuguês!
Maséimportantevocêencararo manesuanavegaçãoestranha.Vocêveráque,
noLinux,muitoscomandostrabalhamdeformasimilar.
Obtendoadescri çãodecomandos
Éinteressantesaberquepodemosverificarumadescriç ãosimplesdeumco-
mando,paraissopodemosusaro whatis:
daniel@casadocodigo:~$ whatis ls
ls (1) - list directory contents
daniel@casadocodigo:~$ whatis man
man (1) - an interface to the on-line reference manuals
man (7) - macros to format man pages
daniel@casadocodigo:~$
2.6 L ocalizando arquivos no sistema
Veremosagoraumpoucosobreocomando find,eleserveparaprocurararqui-
vospelonomeeoutrascaracterísticascomodatademodificaç ão,tamanho,usuário
criadordoarquivoetc.
Asintaxedo findrecebealgunsparâmetros:
find [caminho] expressão [ação]
Indicamoso caminhoapartirdoqualeleiráprocurarosarquivos,a expressão
naqualpodemosdefiniroscritériosdebuscaea açãocomaqualinformamosoque
deveserfeitocomosarquivosqueatenderemaoscritériosdabusca.
Algunsdoscritériosdebuscadefinidosem expressão:
•-nameprocuraarquivospelonome;
•-userprocuraarquivospelonomedousuáriodonodoarquivo;
•-atimeprocuraarquivosqueforamacessadoshámaisdexdias,ondexéo
númerodedias.
30

## Página 38

CasadoCódigo Capítulo2. Mãonamassa:conhecendooShell
Parasabermaissobreo findleiasempreadocumentaç ão,useo man!
Vamospraticarumpoucobuscandoarquivoscomo find,paraissovamosco-
meçarlistandonatelatodososarquivosocultosquecontenhamapalavra bash:
daniel@casadocodigo:~$ find . -name \*.bash*
./.bash_history
./.bashrc
./.bash_logout
daniel@casadocodigo:~$
Percebaqueinformamosocaminho .(quesignifica aqui),aexpressão -name
\*.bash*,quequerdizer“busquepelonometodososarquivosquecontenhama
palavrabashnocorpodoseunome”,eaaç ão -printqueéopadrãoquandonão
especificamosdeformaexplícita. Nestecasoaaç ãofoiimprimiremtelaalistade
arquivosqueatendemaocritériodefinidonaexpressão.
Vamosfazermaisumabusca,destavezemoutrodiretóriodosistema:
daniel@casadocodigo:~$ find /etc/init -name net*
/etc/init/network-interface-container.conf
/etc/init/network-interface-security.conf
/etc/init/network-interface.conf
/etc/init/networking.conf
daniel@casadocodigo:~$
Nesse caso, informamos um caminho diferente para busca no sistema
/etc/initeespecificamosumanovaexpressão -name net *. O *usadoem
expressõeséomesmoquequalquercoisa;nesseexemplosignifica“busqueporar-
quivosquecomecemcomneteterminemcomqualquercoisa”.
Testeoutraformadebuscacomaexpressão -atime:
daniel@casadocodigo:~$ find . -atime +1
./.bash_logout
daniel@casadocodigo:~$
Noexemplo,o -atime +1 buscaporarquivosqueformamodificadoshámais
de1dia.Testeomesmocomandoinformando -1destaformaeleretornaráarquivos
modificadosamenosde1dia:
daniel@casadocodigo:~$ find . -atime -1
.
31

## Página 39

2.7. Umpasseioforadoambientegráfico CasadoCódigo
./.bash_history
./.bashrc
./.lesshst
daniel@casadocodigo:~$
Nãosepreocupeseoresultadonoseucomputadorfordiferente,issoénormal
poiseupossotereditadooutrosarquivoseporissoelespodemaparecernalistagem.
2.7 Um passeio fora do ambiente gráfico
AlémdoambientegráficonoLinux,existeainda6ambientesdelinhadecomando,
conhecidospelonomede TTY(TeleTYpe)ouaindaterminaisvirtuais.O TTYcor-
respondeaotipodosprimeirosterminaisusadosemcomputadores.
Parateracessoaessesambientes,usamosumacombinaç ãodasteclas Ctrl +
Alt + F sendoque Fcorrespondedasteclas F1a F6,a F7retornaaoambientegrá-
fico.
Façaumteste,pressioneacombinaç ãodeteclasnestaordem: Ctrl + Alt +
F1ou Ctrl + Alt + F2:
Figura2.8:TTY,ambientenativodelinhadecomando
EsteéoambientepadrãofornecidoemalgumasdistribuiçõesLinuxparaDesk-
toplogoapósainstalaç ão,comoéocasodo Slackwareetambéméopadrãoem
servidores.
Pararetornaraomodográficofaç a: Ctrl + Alt + F7.
Nopróximocapítulo,veremosmaissobreediç ãodearquivos.
32

## Página 40

Capítulo3
Manipulandoarquivos
Vamosaprendersobremanipulaç ãodearquivosnoShell.Nessecapítulo,conhece-
remosumpoucosobreoeditoresdetextonoterminalealgunscomandosdeleitura
dearquivos.
3.1 O editorVim
O ViéoeditorbásicodisponívelemgrandepartedasdistribuiçõesLinux. Atual-
menteesteeditoréoferecidocommaisrecursoserecebeonomede Vim(VIiMpro-
ved).O Viméumeditordeaspectosimples,porémbastanteflexível.Emseguida,
veremosobásicosobreele.
Paracome çarvamosaprendersobrecomoentraresairdoeditor. NoUbuntu
porpadrãoelejáveminstaladocomonomede vi:
daniel@casadocodigo:~$ vi

## Página 41

3.1. OeditorVim CasadoCódigo
Figura3.1:Telainicialdovim
Aoentrarno vi,eleéabertodiretonomodo visual. Paraeditarumarquivo,
usamososmodosde inserção, substituiçãoe deleção.Semprequeprecisamosvoltar
aomodo visual,usa-seatecla Esc.
Parasairdo viuseocomando :q:
Figura3.2:Saindodovim
34

## Página 42

CasadoCódigo Capítulo3. Manipulandoarquivos
Nasequênciaveremoscomoalternarparaomodode inserção,escreveremum
arquivo,voltarparao visual,salvaresairdoeditor:
Vamosabriro viinformandoonomedeumarquivoparaeditar:
daniel@casadocodigo:~$ vi vim_basico.txt
Aoabrirumnovoarquivo,o vinosexibeumatelalimpaesimples:
Figura3.3:Abrindonovoarquivonovim
Observenabasedoeditorasinformaçõeseonomedoarquivoqueabrimos.
Vamosalternarparaomodode inserção—paraissotecle i:
35

## Página 43

3.1. OeditorVim CasadoCódigo
Figura3.4:AlternandoparaomodoINSERT
Notequeeleinformaomodocorrente,nocasoINSERT.Nessemomentopode-
mosdigitarqualquercoisanonossoarquivo:
Figura3.5:Inserindotextonoarquivo
Agoraqueinserimosumtexto,vamossalvaronossoarquivo. Paraissoéne-
36

## Página 44

CasadoCódigo Capítulo3. Manipulandoarquivos
cessárioretornarparaomodo visualeemseguidapodemossalvarcomocomando
:w.
Tecle Escpararetornaraomodo visuale :wparasalvar:
Figura3.6:Salvandooarquivo
Agoraquesalvamosoarquivopodemossairdoeditorcom :q:
37

## Página 45

3.1. OeditorVim CasadoCódigo
Figura3.7:Saindodovimapóssalvaroarquivo
Verifiquequedepoisdesalvo,oarquivofoicriadononossodiretório home,não
foiprecisocriarumarquivoantes:
daniel@casadocodigo:~$ ls
vim_basico.txt
daniel@casadocodigo:~$
Podemosverificaroconteúdodoarquivocomo cat:
daniel@casadocodigo:~$ cat vim_basico.txt
Básico de Vim
Aprendendo o básico sobre o editor Vim
daniel@casadocodigo:~$
Novimpodemosnavegarpeloarquivousandoasteclasdirecionaisouasteclas
h, j, ke l:
•h,moveparaaesquerda;
•j,moveparabaixo(próximalinha);
•k,moveparacima(linhaanterior);
38

## Página 46

CasadoCódigo Capítulo3. Manipulandoarquivos
•l,moveparaadireita.
Maiscomandosquefacilitamamovimentaç ão:
•Gmoveparaaúltimalinhadoarquivo;
•ggmoveparaaprimeiralinhadoarquivo;
•0moveocursorparaoiníciodalinha;
•$moveocursorparaofinaldalinha.
Algunscomandosbásicosparaajudarnainser çãodetexto:
•iparainserirtextoantesdocursor;
•aparainserirtextodepoisdocursor;
•Aparainserirtextonofinaldeumalinhaondeseencontraocursor;
•oparaadicionarumalinhaabaixodalinhaatual;
•Oparaadicionarumalinhaacimadalinhaatual.
Temostambémcomandosparaalteraç ãoelocalizaç ãonomodo visual:
•xdeletaocaractereondeestáocursor;
•dddeletaalinhaatual;
•udesfazaúltimamodificaçãonoarquivo;
•yycopiaumalinha, pcolaoquefoicopiado;
•/palavrabuscapelapalavraoucaractereemtodooarquivo.
Avariedadedecomandosecombinaçõesparaesseeditorémuitogrande,tería-
mosumlivroapenassobreele.Porissoéinteressantetero vimbook,umguiaem
português,ótimoparaconsultas:
https://code.google.com/p/vimbook/
Sepreferirumscreencast,oFabioAkitadisponibilizougratuitamenteumvídeo
com1horadeduraç ãosobreovimparainiciantes:
http://blip.tv/akitaonrails/screencast-come-ando-com-vim-6075050
39

## Página 47

3.2. OeditorNano CasadoCódigo
3.2 O editorNano
O nanoémaisumaalternativaparaediç ãodetextosnoterminal,eestádisponível
emquasetodasasdistribuiçõeslinux,assimcomoo vim.
Onanoacabasendoumaboaescolhaparainiciantesporsermaisfácildeusare
possuirumainterfacebastanteintuitiva.
Vamosabriro nanoeconhecerumpoucosobreesseeditor:
Figura3.8:Telainicialdonano
Observandoomenuinferiordoeditor nanonotamosváriasfunções.Valelem-
brarque^éomesmoque Ctrl,sendoassim ^Gsignifica Ctrl + G.
Algunscomandosbásicosdo nano:
•^Gapresentaateladeajudasobremaiscomandosdoeditor;
•^Xsaidoeditor;seoarquivonãoestiversalvoserásolicitadoparasalvarantes
desair;
•^Osalvaumarquivo;
•^Wbuscaporumapalavradentrodoarquivo.
Vamosabriroarquivoquecriamoscomo vim,editaresalvarparaentenderna
práticacomofuncionao nano.
40

## Página 48

CasadoCódigo Capítulo3. Manipulandoarquivos
Comoeditoraberto.tecle ^R.Serásolicitadoonomedoarquivoquedesejamos
editar,nonossocaso vim_basico.txt:
Figura3.9:Abrindooarquivovim_basico.txtcomonano
Agoraquetemosoarquivoaberto,vamoseditar:
Figura3.10:Editandooarquivocomonano
Vamossalvarnossoarquivoeditadocomoatalho ^O.Serásolicitadoonomedo
arquivocasoqueiracriarumnovoarquivo:
41

## Página 49

3.3. TrabalhandocomoCat CasadoCódigo
Figura3.11:Salvandooarquivocomonano
Apóssalvaroarquivo,tecle ^Xparasairdoeditoreverifiquequeagoratemos
umnovoarquivocomonome nano_basico.txt:
daniel@casadocodigo:~$ nano
daniel@casadocodigo:~$ ls
nano_basico.txt vim_basico.txt
daniel@casadocodigo:~$
Comopodemosver,editartextoscomo nanoébemsimples.Aseguirveremos
algunscomandosquepodemajudarnaediç ãodearquivosdeformarápida.
3.3 Trabalhando com o Cat
Ocomando cat,quejávimosumpoucoanteriormente,énormalmenteutilizado
paraexibiroconteúdodearquivos,maselepossuirecursosparairalémdisso.
Paraconhecermosmelhoro cat,vamoscriarumarquivochamado agendae
inseriralgunsdadoscomonomeeperfilnoTwitter.Criaremosoarquivousandoo
próprio cat,comoparâmetro >.Destaforma,o catvailerosdadosdigitadosno
tecladoeinserirnoarquivoindicado.
Faça cat > agenda etecle Enter.Emseguidadigiteasinformações,enofinal
tecle Ctrl + d.Istovaiencerraradigitaç ãoesalvarosdadosnoarquivo agenda:
daniel@casadocodigo:~$ cat > agenda
Daniel Romero @infoslack
42

## Página 50

CasadoCódigo Capítulo3. Manipulandoarquivos
Paulo Silveira @paulo_caelum
Nando Vieira @fnando
Adriano Almeida @adrianoianoalmeida7
Vinicius Baggio @vinibaggio
^D
Paraconferir,exibaoconteúdodoarquivoeverifiquequeosdadosforamsalvos:
daniel@casadocodigo:~$ cat agenda
Daniel Romero @infoslack
Paulo Silveira @paulo_caelum
Nando Vieira @fnando
Adriano Almeida @adrianoalmeida7
Vinicius Baggio @vinibaggio
daniel@casadocodigo:~$
O catdisponibilizaop çõesparaexibir <TAB>noarquivo -t,ofimdaslinhas
deumarquivo,ouseja,ondedemos ENTER -e.Façaumtestecomasduasop ções:
daniel@casadocodigo:~$ cat -et agenda
Daniel Romero^I@infoslack$
Paulo Silveira^I@paulo_caelum$
Nando Vieira^I@fnando$
Adriano Almeida^I@adrianoalmeida7$
Vinicius Baggio^I@vinibaggio$
daniel@casadocodigo:~$
Notequeforamexibidoscaracteres ^,querepresentamo <TAB>,eo $,que
representaofimdalinhaou <ENTER>. Existetambémaop çãodeenumeraras
linhas -n:
daniel@casadocodigo:~$ cat -n agenda
1 Daniel Romeroero @infoslack
2 Paulo Silveira @paulo_caelum
3 Nando Vieira @fnando
4 Adriano Almeida @adrianoalmeida7
5 Vinicius Baggio @vinibaggio
daniel@casadocodigo:~$
Umusomuitointeressantedo catéparaconcatenararquivos.Elepodepegar
oconteúdodeváriosarquivoseredirecionarparaumoutro.Lembradoarquivoque
criamoscomo vim?Vamosusá-loparatestaresserecursodo cat,pegaremosos
43

## Página 51

3.4. Exibindooinícioeofimdearquivos CasadoCódigo
dadosdaagendaedoarquivocriadocomo vim,evamosconcatenaremumnovo
arquivo.
Antes,verifiqueoconteúdodecadaum:
daniel@casadocodigo:~$ cat vim_basico.txt
Básico de Vim
Aprendendo o básico sobre o editor Vim
daniel@casadocodigo:~$
daniel@casadocodigo:~$ cat agenda
Daniel Romero @infoslack
Paulo Silveira @paulo_caelum
Nando Vieira @fnando
Adriano Almeida @adrianoalmeida7
Vinicius Baggio @vinibaggio
daniel@casadocodigo:~$
Vamosàinstruçãodeconcatenaç ãodearquivos.Paraissofaç aoseguinte: cat
vim_basico.txt agenda > concatenando.txt:
daniel@casadocodigo:~$ cat vim_basico.txt agenda > concatenando.txt
daniel@casadocodigo:~$
Emseguida,verifiqueoconteúdodonovoarquivogeradopelo cat:
daniel@casadocodigo:~$ cat concatenando.txt
Básico de Vim
Aprendendo o básico sobre o editor Vim
Daniel Romero @infoslackslack
Paulo Silveira @paulo_caelum
Nando Vieira @fnando
Adriano Almeida @adrianoalmeida7
Vinicius Baggio @vinibaggio
daniel@casadocodigo:~$
3.4 Exibindo o início e o fim de arquivos
Éinteressantesabersobredoiscomandoscomafun çãodeexibiroconteúdodeum
arquivodo cat:sãoeleso heade tail.
44

## Página 52

CasadoCódigo Capítulo3. Manipulandoarquivos
O headmostraoiníciodosdadosemumarquivo.Porpadrãoeleexibeas10
primeiraslinhasdoarquivo,masutilizandoaop ção -npodemoslimitaronúmero
delinhas:
daniel@casadocodigo:~$ head -n 3 concatenando.txt
Básico de Vim
Aprendendo o básico sobre o editor Vim
daniel@casadocodigo:~$
Jáo tailmostraofinaldosdadosdoarquivoepossuiamesmaop çãopara
limitaraquantidadedelinhas, -n:
daniel@casadocodigo:~$ tail -n 5 concatenando.txt
Daniel Romero @infoslackslackack
Paulo Silveira @paulo_caelum
Nando Vieira @fnando
Adriano Almeida @fnandoadrianoalmeida7
Vinicius Baggio @vinibaggio
daniel@casadocodigo:~$
Lembre-sedesempreconsultaradocumentaç ãodoscomandoscomo man!
Nocapítuloaseguirveremoscomofazeracompreesãoedescompressãodear-
quivos.
45

## Página 54

Capítulo4
Compactaçãoedescompactaç ãode
arquivos
OLinuxporpadrãopossuiváriosutilitáriosdecompressãodearquivos.Compactar
arquivosediretórioséumaboapráticapararealizaç ãode backups. Nestecapítulo
veremosalgunscomandosdecompressão.
4.1 Conhecendo o tar
O taréexcelenteparaagruparváriosarquivosemapenasum. Isso,naprática,
evitaqueprecisemosfazerváriastransferênciasdearquivosentrecomputadores,en-
viandoapenasumúnicoarquivo.Issovaiaparecer muitonodecorrerdoseuusodo
Linux.Éimportanteconhecê-lobem.
Basicamenteexistemtrêstiposdearquivosquesãoutilizadoscomo .tar:
tar.gzou .tgze .tar.bz2.
Aoutilizarmoso .tar,elerealizaumacópiasemcompactaç ãodosarquivos

## Página 55

4.1. Conhecendootar CasadoCódigo
passadoscomoparâmetro,ousejaelejuntatodososarquivosemumúnicoarquivo
semcompactar.
Algumasop çõesdo tar:
•-ccriaumnovoarquivo.tareadicionaosarquivosaseremcompactados;
•-findicaqueodestinoéumarquivoemdisco;
•-vexibeonomedecadaarquivocompactado;
•-xextraiosarquivosagrupadosnoarquivo.tar.
Paramaisop ções,lembre-sedeusaro man!
Vamostestaro .tarnaprática,juntaremostodososnossosarquivosqueter-
minamem .txtemapenasum.Paraissousaremosasop ções -ce -f:
daniel@casadocodigo:~$ ls
agenda concatenando.txt nano_basico.txt vim_basico.txt
daniel@casadocodigo:~$ tar -cf backup.tar *.txt
daniel@casadocodigo:~$ ls
agenda backup.tar concatenando.txt nano_basico.txt vim_basico.txt
daniel@casadocodigo:~$
Notequefoicriadoumarquivochamado backup.tar,querepresentaaunião
detodososarquivoscomextensão .txt.
Vamosfazeroreversodestaunião,separandoosarquivosusandoasop ções -x,
-ve -f.Criaremosumnovodiretórioparamelhorvisualizar:
daniel@casadocodigo:~$ mkdir backup
daniel@casadocodigo:~$ mv backup.tar backup/
daniel@casadocodigo:~$ cd backup/
daniel@casadocodigo:~/backup$ ls
backup.tar
daniel@casadocodigo:~/backup$ tar xvf backup.tar
concatenando.txt
nano_basico.txt
vim_basico.txt
daniel@casadocodigo:~/backup$ ls
backup.tar concatenando.txt nano_basico.txt vim_basico.txt
daniel@casadocodigo:~/backup$
48

## Página 56

CasadoCódigo Capítulo4. Compactaçãoedescompactaç ãodearquivos
Oqueacabamosdefazerfoicriarumapastachamada backup,moveroarquivo
backup.tarparadentrodapastacriadaefazeroprocessoreversoparasepararos
arquivos.
Otipo.tar.gz
O .tar.gzconsisteemdoisprocessosdiferenteseinterligados,sendoquepri-
meiroelecriaumarquivo .tare,emseguida,compactautilizandooformato .gz.
Nestecaso,alémdegerarumúnicoarquivocomo .tar,eleserácompactado,re-
duzindoassimoseutamanho.
Aindadentrodapasta backup,vamostestaracriaç ãodonossoarquivodessa
vezcompactadocom .tar.gz:
daniel@casadocodigo:~/backup$ ls
backup.tar concatenando.txt nano_basico.txt vim_basico.txt
daniel@casadocodigo:~/backup$ tar zcvf backup.tar.gz *.txt
concatenando.txt
nano_basico.txt
vim_basico.txt
daniel@casadocodigo:~/backup$ ls
backup.tar concatenando.txt vim_basico.txt
backup.tar.gz nano_basico.txt
daniel@casadocodigo:~/backup$
Notequeagoratemoso backup.tar.gz,omesmoarquivounido .tar,mas
compactadocom .gz.Podemosverificarotamanhodosarquivoscomocomando
duparamelhorentenderorealefeitodacompactaç ão:
daniel@casadocodigo:~/backup$ du -h backup.tar backup.tar.gz
12K backup.tar
4.0K backup.tar.gz
daniel@casadocodigo:~/backup$
Vejaqueusandoo .tar.gzoarquivofoireduzidopara4kbytes!Paradescom-
pactararquivos .tar.gzusa-seasop ções zxvf:
daniel@casadocodigo:~/backup$ tar zxvf backup.tar.gz
concatenando.txt
nano_basico.txt
vim_basico.txt
daniel@casadocodigo:~/backup$
49

## Página 57

4.1. Conhecendootar CasadoCódigo
Otipo.tar.bz2
Como .tar.bz2ocorreomesmocasoquecomo .tar.gz:acompactaç ão
comoformato .bz2émaiseficientequeo .gz,porémémaislentanahorade
geraracópia.
Vamoscriarumarquivocompactadocom .tar.bz2utilizandoasop ções
jcvfeconferiradiferen çaentreostamanhoscomocomando du:
daniel@casadocodigo:~/backup$ tar jcvf backup.tar.bz2 *.txt
concatenando.txt
nano_basico.txt
vim_basico.txt
daniel@casadocodigo:~/backup$ ls
backup.tar backup.tar.gz nano_basico.txt
backup.tar.bz2 concatenando.txt vim_basico.txt
daniel@casadocodigo:~/backup$ du -h backup.tar*
12K backup.tar
4.0K backup.tar.bz2
4.0K backup.tar.gz
daniel@casadocodigo:~/bashackup$
Nãohouvediferen çaentreostamanhosnosformatos .gze .bz2,jáqueesta-
moscompactandopequenosarquivostexto.Porémépossívelnotaradiferen çaem
arquivosmaiores,porexemploumaimagem ISOdeum DVD.
Parafazeradescompactaç ãodeformatos .bz2usamosasop ções jxvf:
daniel@casadocodigo:~/backup$ tar jxvf backup.tar.bz2
concatenando.txt
nano_basico.txt
vim_basico.txt
daniel@casadocodigo:~/backup$
Podemosnotarque,semprequevamoscompactar,aop ção céutilizada;eao
realizaradescompactaç ãousamosaop ção x.Jáparaoformato .tar.gz,usamos
aop ção z,eaop ção jparaoformato .tar.bz2.
Podeparecerumpoucocomplicadomemorizartodasessasop çõesnoinicio,
mascomapráticaissoacabasetornandonatural.
50

## Página 58

CasadoCódigo Capítulo4. Compactaçãoedescompactaç ãodearquivos
4.2 Conhecendo o gzip/gunzip
EsteéoprogramadecompressãomaisutilizadonoLinux.O gzipgeraumarquivo
noformato .gz.Suaformadeusoparacompactarébastantesimples:
daniel@casadocodigo:~/backup$ gzip -c -r *.txt > backup.gz
daniel@casadocodigo:~/backup$ ls
backup.gz concatenando.txt nano_basico.txt vim_basico.txt
daniel@casadocodigo:~/backup$
Asop ções -ce -rrespectivamenteinformamquequeremoscriarumarquivo
ecompactar.Aoexecutarmosacompactaç ãodeváriosarquivosutilizandoo gzip,
osarquivosserãoconcatenadosemumsóeemseguidacomprimidosnoformato
.gz.
Paradescompactarusamoso gunzip,quepodeserutilizadocomasop ções -c
e -vparaexibiroconteúdoaserdescompactadoeinformaçõessobreonívelde
compactaçãodosarquivos:
daniel@casadocodigo:~/backup$ gunzip backup.gz
daniel@casadocodigo:~/backup$
Noexemplo, aoexecutaradescompactaç ãocom gunzip, onossoarquivo
backup.gzdeixarádeexistirpoisporpadrãoo gunzipextraioarquivocom-
primidonoformato .gzeexcluioarquivocompacto.
4.3 Conhecendo o zip/unzip
Ocomando zip,comoonomejásugere,criaumarquivocompactonoformato
.zip,enquantoo unzipfazotrabalhoinverso,descompactando.
Aformadeusoémuitosimples:
daniel@casadocodigo:~/backup$ zip backup.zip *.txt
adding: concatenando.txt (deflated 27%)
adding: nano_basico.txt (deflated 44%)
adding: vim_basico.txt (deflated 16%)
daniel@casadocodigo:~/backup$ ls
backup.zip concatenando.txt nano_basico.txt vim_basico.txt
daniel@casadocodigo:~/backup$
51

## Página 59

4.3. Conhecendoozip/unzip CasadoCódigo
Pacotes padrões em um Ubuntu
Tenteestecomandoagora.Háumagrandechancedevocênãocon-
seguirexecutá-lo.
Porquê?Porqueelenãoestáinstalado!OUbuntueasoutrasdistros
emgeraltrazemjáinstaladosumgrupograndedeaplicativos,masobvi-
amentenãotodos.OZipéumdeles.Embreve,veremoscomoprocurar
einstalarospacotesdoLinux.
Paradescompactar,useocomando unzip:
daniel@casadocodigo:~/backup$ unzip backup.zip
Archive: backup.zip
inflating: concatenando.txt
inflating: nano_basico.txt
inflating: vim_basico.txt
daniel@casadocodigo:~/backup$
Éimportantenãoconfundirocomando gzipcomo zipeo gunzipcomo
unzip!
52

## Página 60

Capítulo5
Entendendoaestruturade
diretórios
VamosconhecermaissobreaestruturadediretóriosLinuxeentenderoseufun-
cionamento.Aestruturadediretóriosarmazenaarquivosdeformahierárquica,de
maneiraqueousuárionãoprecisaconhecerosdetalhestécnicosdosistemadear-
mazenamento.Masparapodernavegareobterinformaçõeséprecisoentenderesta
estrutura.
5.1 Aestrutura de diretórios
Cadadiretóriodosistemapossuiarquivosquesãomantidosseguindoregrasdefini-
daspelaFHS(FilesystemHierarchyStandard).NoUbuntuaestruturadediretórios
segueopadrãoLSB(LinuxStandardBase),queporsuavezsegueaespecificaç ãodo
FHS.Essespadrõessãoimportantespoisajudamamanteracompatibilidadeentre
asvariaçõesdedistribuiçõesLinux.

## Página 61

5.1. Aestruturadediretórios CasadoCódigo
Comovimosnosprimeiroscapítulos,umdiretórioéumlocalondeguardamos
arquivosnosistema,tambémconhecidosporpastas.Vamosrelembraranossapri-
meiralistagemdediretórios,quepodeserchamadade árvore:
daniel@casadocodigo:~$ ls /
bin home media Repos selinux usr
boot initrd.img mnt root srv vagrant
dev lib opt run sys var
etc lost+found proc sbin tmp vmlinuz
daniel@casadocodigo:~$
Nestaestrutura,oFHSdeterminaqueobrigatoriamenteumadistribuiç ãoLinux
deveconter14diretórios.Veremoscadaumdeles.
Quandolistamos ls / estamosverificandooconteúdododiretório raiz. /é
umdiretório—podemosdizerqueéoprincipaldiretóriodosistema,poisneleficam
todososoutros.QuemvemdoWindowspodepensarno /comoo c:ounoícone
Meu Computador.Tododiretóriodentrodoraiz( /)échamadodesubdiretório.
Odiretório /binarmazenaarquivosexecutáveisbinários,quesãooscomandos
baseparaaexecuç ãodosistema,porexemploo lseo cd.Essediretórioépúblico,
ouseja,qualquerusuáriopodeusarosexecutáveisqueestãolá.
O /bootcontémarquivosdeinicializaçãodosistema,dentreosquaisestáoge-
renciadorde bootdosistema.Eleéumaplicativoquecarregaosistemaoperacional
duranteainicialização.
Odiretório /devmantémocaminhodosdispositivosinstaladosnosistema.
Todoohardwarereconhecidopelosistemaérepresentadoporumarquivonesse
diretório,porexemplo,discorígidoeplacadevídeo.
Em /etcficamosarquivosdeconfiguraç ãodosistema,scriptsdeinicializaç ão,
configuraçõespadrãoparausuáriosearquivosdeconfiguraç ãodeprogramasquesão
instalados.Veremosmuitoessediretórioquandoestivemosinstalandoaplicativos.
O /libcontémasbibliotecasemódulosdokernelquesãoessenciaisparao
funcionamentodosistema. Asbibliotecassãofun çõescompartilhadasquepodem
serusadasporváriosprogramas.
/mediaéodiretórioresponsávelpormanteros pontos de montagem,ouseja,
quandoinserimosumpendriveénestediretórioqueeleficarádisponíveltempora-
riamenteenquantousamos.
O /mntéutilizadopara montagem temporáriadesistemasdearquivos,istoé,
umhdoupendrive.Estediretóriopodeserusadodamesmaformaqueo /media.
54

## Página 62

CasadoCódigo Capítulo5. Entendendoaestruturadediretórios
Nodiretório /optéondenormalmenteinstalamosprogramasquenãofazem
parteoficialmentedadistribuiç ão.Porexemplo,o google chrome.
Em /sbinficamoscomandosutilizadosparainicializaç ão,reparaçãoerestau-
raçãodosistema.Éumdiretóriodecomandosessenciais,mascomadiferen çade
queapenasumusuáriopodeusar,o root. Veremosmaissobreesseusuáriono
próximocapítulo.
O /srvmantémdadosdeserviçosdisponíveispelosistemaepodeseracessado
deformageral(portodososusuários),porexemplo, web server.
No /tmpficamarmazenadosarquivostemporários,informaçõesquedevemser
mantidasatéofimdeumaoperaç ão,comoumdownloademandamentoouarquivos
decachedevídeosdoYoutube.
Em /usrsãomantidosprogramasquenãosãoessenciaisparaofuncionamento
dosistema.Programasinstaladospelousuário,comoeditores,programasgráficos,
gerenciadoresdejanelasssãoexemplosdisso.
Odiretório /varcontémarquivosdedadosvariáveis,ouseja,arquivosque
podemaumentardetamanho,comoarquivosdelog,arquivosdebancosdedadose
mensagensdee-mail.
5.2 Os diretórios opcionais
Osdiretórios /homee /rootsãoopcionais—elespodemexistirnosistemamas
nãoobrigatoriamentecomestesnomes,apesardeseremassimcomfrequência!
Odiretório /homearmazenaosdiretóriosearquivosdosusuárioscadastrados
nosistema,porexemplo /home/daniel.Elepoderiaserchamadoporoutronome
como /minha_pasta,porexemplo,eissonãoafetariaemnadaaestruturado
sistema.
Jáodiretório /rootéapastapessoaldosuperusuário root,sobreoqualve-
remosmaisdetalhesnocapítuloseguinte.
5.3 Os diretórios/proc e/sys
Odiretório /proccontémarquivostemporáriosdeprocessosemexecuç ãonosis-
tema.Emoutraspalavras,éumdiretóriovirtualusadopelokernel.Nelesãoman-
tidosconfiguraçõesatuaisdosistemaedadosestatísticos.Maisadianteveremosde-
talhessobreprocessos.
55

## Página 63

5.3. Osdiretórios/proce/sys CasadoCódigo
Assimcomoodiretório /proc,o /sysarmazenaquaseomesmoconteúdo
porémdeformamaisorganizadaparapodermosadministrar.
Ámedidaqueformosavan çando,vamosconferirnapráticaalgunsdosprinci-
paisdiretóriosvistosaqui.
56

## Página 64

Capítulo6
Administraçãodeusuários
OLinuxéumsistemamultiusuário,ouseja,quepodeserusadoporváriosusuários
simultaneamente,semqueuminterfiranasatividadesdooutro,nemconsigaalte-
rarseusarquivos. Umbomexemploparaentendermelhorseriaumservidorweb
compartilhado,baseadoemLinux,quehospedaalgunsmilharesdesites,cadaum
administradoporumusuáriodiferente.
Asrestriçõesimplementadasnosistemadepermissõessãomuitoeficientes.Esse
esquemadepermissõeséfundamentalparaofuncionamentodosistemaporcom-
pleto. Aspermissõesconsistememumconjuntodetrêsregras: leitura, escritae
execução. ÉgraçasaesseesquemadepermissõesquenãovemossistemasLinux
infectadospormalwaresouvírus.
Nestecapítulo,aprenderemossobregestãodeusuáriosevamosentenderdeta-
lhadamentecomofuncionamaspermissões.

## Página 65

6.1. Gerenciandousuários CasadoCódigo
6.1 Gerenciando usuários
Paraentendersobreocontroledeusuários,vamosdividirestase çãoemtrêscatego-
rias:
1) SuperUsuário(sudo)ouAdministrador;
2) UsuáriodeSistema;
3) UsuárioComum.
UsuárioAdministradoresudo
Nosistema,esseusuárioéchamadode root. Eleéresponsávelporcontrolar
todoosistemaenãopossuirestrições.Semprequeexecutamosalgumprogramaou
tarefaquenecessitedepoderesadministrativos,precisamosdo root,queéchamado
pormeiodocomando sudo.
Porexemplo,semprequeformosinstalarumprogramaouatualizartodoosis-
tema,usaremosocomando sudoparateraspermissõesde rooteconseguirefetuar
essastarefas.
Vejaoqueaconteceaotentarexecutarumatarefaqueprecisadaspermissõesdo
usuárioroot:
daniel@casadocodigo:~$ apt-get update
E: Could not open lock file
/var/lib/apt/lists/lock - open (13: Permission denied)
E: Unable to lock directory /var/lib/apt/lists/
E: Could not open lock file
/var/lib/dpkg/lock - open (13: Permission denied)
E: Unable to lock the administration directory
(/var/lib/dpkg/), are you root?
daniel@casadocodigo:~$
Podemosnotarváriasmensagensdealertainformandoqueapermissãopara
atarefafoinegadae,nofinal,eleperguntasesomosousuário root. Ocorreto
seriaexecutarcomocomando sudoparaqueonossousuáriosejatratadocomos
privilégiosdousuário root.
Vejaoqueaconteceaoexecutarmosamesmainstruç ãousandoocomando
sudo:
58

## Página 66

CasadoCódigo Capítulo6. Administraçãodeusuários
daniel@casadocodigo:~$ sudo apt-get update
[sudo] password for daniel:
Notequefoisolicitadaumasenhaparaonossousuário,queéamesmaque
cadastramosnoprocessodeinstalaç ão. Aoconfirmá-la, ocomando apt-get
updatefuncionaránormalmente,poisonossousuáriofazpartedomesmo grupo
dousuário root.Entenderemosmaisadiantesobre grupos de usuários.
Nãosepreocupeaindacomoexemplodocomando apt-get,veremosoque
elefaznopróximocapítulo.
Usuáriosdesistema
Sãousuáriosquenãonecessitamlogarnosistema–elesexistemparacontro-
larserviçosenormalmentenãopossuemsenhas. Umbomexemploéousuário
www-data,quepodeserusadoparaadministrarservidoreswebcomoApachee
Nginx.
Veremosmaissobreusuáriosdesistemanoscapítulossobreadministraç ãoeser-
viços.
Usuárioscomuns
Sãoascontascriadasparaoutilizadoresdosistema.Essencialmente,elespodem
executartarefasbásicascomocriareeditardocumentos,navegarnainternet,assistir
vídeosetc.Aconta danieléumexemplodeusuáriocomum,diferentedaconta
rootqueéutilizadaparaadministrarosistema.
6.2 Permissões
Nestase çãoabordaremososuficienteparatermosumareferênciasobrepermissões
dearquivoseusuários. Aspermissõessãoop çõesquepermitemumusuárioter
controledeacesso,leitura,gravaç ãoeexecuç ãodearquivos.
Existemtrêstiposdepermissões: r (leitura), w (escrita)e x (execução).
Arquivosdisponíveissomenteparaleiturapodemserabertoseterseuconteúdo
visualizado,assimcomopastascomomesmotipodepermissãopodemterosarqui-
voslistados.
Arquivosquepossuempermissãodeescritapodemseralterados–ousuário,
nestecaso,tempermissãoparaeditarumarquivoeatéapagar.Emdiretóriosépos-
sívelcriarumnovoarquivo.
59

## Página 67

6.2. Permissões CasadoCódigo
Apermissãodeexecuç ãodáapossibilidadedeexecutarumarquivocomoum
programa,porexemploum scriptdeinstalaçãodeumaplicativo.
Paralistaraspermissõesdeumarquivooudiretório,podemosusarocomando
ls,seguidodaop ção -l(longlisting).Assimteremosumalistagemdetalhadados
arquivos:
daniel@casadocodigo:~$ ls -l
total 20
-rw-rw-r-- 1 daniel daniel 136 Oct 2 00:49 agenda
drwxrwxr-x 2 daniel daniel 4096 Oct 2 18:49 backup
-rw-rw-r-- 1 daniel daniel 192 Oct 2 01:12 concatenando.txt
-rw-rw-r-- 1 daniel daniel 98 Sep 28 16:35 nano_basico.txt
-rw-rw-r-- 1 daniel daniel 56 Sep 28 01:50 vim_basico.txt
daniel@casadocodigo:~$
Nocome ço,issopodeparecergregoparanós.Écomumumapequenadificul-
dadeatéseacostumarcomtantasletrinhaseabreviações.Vamosentenderdetalha-
damenteosignificadodalistagemexibida:
•-:significa“desabilitado”oupermissãonegada;
•r:permissãodeleitura,apenaslêumarquivo;
•w:permissãodeescrita,podeescreveremarquivosediretórios;
•x:permissãoparaexecutarumarquivo.
Aaplicaçãodepermissõesaosarquivosestáligadaatrêsentidades,quesãoclas-
sesdeacessoaosarquivos:
•u:usuáriodonodoarquivo;
•g:grupoaqueoarquivopertence;
•o:outrosusuáriosquenãosejamodononemperten çamaogrupo.
Quandolistamoscom ls -l,os 10 primeiros caracteresindicamomododo
arquivo:
Figura6.1:Mododoarquivoestásublinhadoemvermelho
60

## Página 68

CasadoCódigo Capítulo6. Administraçãodeusuários
Oprimeirocaractereindicaseéumdiretório,linkouumarquivo.Osoutros 9
caracteres formam três grupos de três caracteres.
Oprimeirocaracteredecadagruporepresentaapermissãode leitura, r.Ose-
gundocaractererepresentaapermissãode escrita, w.Oterceirocaractererepresenta
apermissãode execução, x.Quandoocaractere - (hífen)éexibido,significaquea
permissãoestádesligada.
Paraentendermelhorosgruposvejaaimagemseguintedamesmalistagem:
Figura6.2:Ostrêsgrupos
Analisandocomcalmaépossívelperceberqueaspermissõesparao donodo
arquivosãodeleituraeescrita. Aspermissõesparao grupoaoqualoarquivo
pertencesãotambémdeleituraeescrita,easpermissõesde outrossãodeapenas
leitura.Observamosque danieléonomedodonodoarquivoetambéméonome
dogrupoaqualoarquivopertence.
Paraevitarconfusão,mudaremosonomedogrupomaisadiante.
Noambientegráficoépossívelverificaraspermissõesdeumarquivo:paraisso,
cliquecomobotãodireitodomousenoarquivo,depoisem propriedadese,em
seguida,naaba permissões:
61

## Página 69

6.3. Atribuindopermissões CasadoCódigo
Figura6.3:Permissõesdeumarquivonoambientegráfico
6.3 Atribuindo permissões
O chmodéocomandoparaatribuirpermissõesdearquivos.Basicamente,eleatua
diretamentenosníveis dono, grupoe outros.
Asintaxedeusodo chmodéaseguinte:
chmod [opções] modo arquivo
O modopodeserrepresentadoutilizandonotaç ãosimbólicaouoctal,veremos
asduasformas.Aseguir,umalistadasop çõesparaocomando:
•-c:listainformaçõessobreosarquivosmodificados;
•-f:ignoramensagensdeerro;
62

## Página 70

CasadoCódigo Capítulo6. Administraçãodeusuários
•-R:modorecursivo,alteraaspermissõesdetodososarquivosediretórios;
•-v:listadeformadetalhadaasalteraçõesdeatributo.
Antesdeprosseguiréimportanteentendermossobre bitsdeatributo!
Bitsdeatributo
Bits de atributosãoumcontroleadicionalàspermissõesdearquivos.Asentida-
des dono, grupoe outrostêmsuasconfiguraçõessetadaspelodonodoarquivo.Essas
configuraçõespodemserrepresentadastambémpelos bits de atributo,ouseja,assim
comoexistemtrêsentidades,tambémexistemtrêsbits de atributo,quepodemestar
ligadosoudesligados:
BitSetUIDpermitequeumarquivosejaexecutadodamesmaformaqueéexe-
cutadopelodono.
BitSetGIDpermitequeumarquivosejaexecutadocomosefossepartedogrupo
deseudono.Quandoumarquivoécriadoemumdiretórioquepossuiestebitativo,
eleécriadocomomesmogrupododiretório.
BitStickyativaumaprote çãoparaoarquivoenãopermitequeelesejaapagado,
anãoserpeloprópriodono.
Arepresentaçãosimbólicadestes bitsélidadaesquerdaparaadireitaatravésdas
siglas SST,ondeoprimeiro Srepresentao SetUID,osegundo Srepresentao SetGID
eo Trepresentao Sticky.Paraindicarseum bitestáativoouinativo,usa-se (1 ou +)
paraativoe (0 ou -)parainativo.
Osbitsdeprote çãodefinemprote çõesbásicasdeumarquivoque,comovimos
anteriormente,são: leitura, escritae execução.Ativarounãoestesbitséoquedefine
aspermissõesdequempoderátrabalharcomoarquivo,ouseja: editar, deletarou
executar.
Bitsdeprote çãosãodivididosemtrêsgruposdetrêsbits,sendoquecadagrupo
possuitrêsbitsecadabitrepresentaumapermissão.Ficouconfuso?Vamosveruma
representaçãoparaentendermelhor:
000000000 aspermissõesdecadaentidadesãorepresentadasporcadagrupo
detrêszerosesãolidassempredaesquerdaparaadireita.
Quandolistamosarquivoscomocomando ls -l,conseguimosvisualizaras
mesmaspermissõesdeoutramaneira: rwxrwxrwx.
63

## Página 71

6.3. Atribuindopermissões CasadoCódigo
Ostiposdenotaç ões
Agoraquejávimosoquesãoos bits de atributoede proteção,veremoscomo
converterentrenotaçõesbinária,simbólicaeoctal.
Juntandoosbitsdeatributoedeprote çãotemosumtotalde12bits,sendo3de
atributose9deprote ção. Vejaarepresentaçãobináriaesimbólica: 000000000
000ousstrwxrwxrwx.
Anotaçãooctalconvertecadagrupodetrêsbitsemumcaracterequevaide0a
7.
Grupos: Dono | Grupo | Outros
Simbólica: rwx r-x r--
Binária: 111 101 100
Octal: 7 5 4
Voltandoparao chmod,vamosàprática. Primeiro,comocomando ls -l,
vamoslistarasinformaçõessobrepermissãodoarquivo agenda:
daniel@casadocodigo:~$ ls -l agenda
-rw-rw-r-- 1 daniel daniel 136 Oct 2 00:49 agenda
daniel@casadocodigo:~$
Podemosnotarqueoarquivopossuipermissãodeleituraeescritaparaodono
egrupo,epermissãodeapenasleituraparaoutros.Fazendousodo chmodvamos
alteraraspermissõesdestearquivo:
daniel@casadocodigo:~$ chmod u=rw,g=rw,o=rw agenda
daniel@casadocodigo:~$ ls -l agenda
-rw-rw-rw- 1 daniel daniel 136 Oct 2 00:49 agenda
daniel@casadocodigo:~$
Oquefizemosfoimanteraspermissõesparadonoegrupoesetarumanova
permissãoparaoutros.Agoraonossoarquivopossuiapermissãodeleituraeescrita
para outros.
Lembre-sequeo urepresentaousuáriodono,o grepresentaogrupoeo ore-
presentaoutros.Amesmapermissãopoderiatersidoexecutadanaformaoctal:
daniel@casadocodigo:~$ chmod 666 agenda
daniel@casadocodigo:~$ ls -l agenda
-rw-rw-rw- 1 daniel daniel 136 Oct 2 00:49 agenda
daniel@casadocodigo:~$
64

## Página 72

CasadoCódigo Capítulo6. Administraçãodeusuários
Testeo chmodusandoaop ção -vevejaainformaç ãoqueeleretorna:
daniel@casadocodigo:~$ chmod -v 664 agenda
mode of `agenda` changed from 0666 (rw-rw-rw-) to 0664 (rw-rw-r--)
daniel@casadocodigo:~$
Retornamosapermissãoanteriorusandooformatooctal. Aop ção -vdo
chmodnosmostraduasnotaçõesm,demodoqueficafácilcomparareentendero
queestamosfazendo.
Analiseatabeladeconversãoentreasnotaçõesparaosbitsdeprote ção.Usare-
mosanotaç ãooctaldaquiprafrenteporsermaisconcisa:
Figura6.4:Notaçõesparaosbitsdeprote ção
6.4 C riando grupos
Agoraquejáentendemosumpoucosobreusuários,gruposepermissões,vamos
praticareconhecermaisalgunscomandos.
Sabemosqueumusuáriodevepertenceraumgrupoepodeseradicionadoaou-
trosgrupos.Paracriarumnovogrupo,usamosocomando addgroup–criaremos
umgrupochamado suporte:
daniel@casadocodigo:~$ sudo addgroup suporte
Adding group `suporte` (GID 1005) ...
Done.
daniel@casadocodigo:~$
65

## Página 73

6.5. Criandousuários CasadoCódigo
Noteque,aocriarogrupoautomaticamente,elerecebeoseunúmero GID.
6.5 Criando usuários
Paracriarusuários,existeocomando adduser,quepodetambémadicionarusuá-
riosemgruposeatécriarnovosgrupos.
adduser paulo iráadicionarousuáriopaulosolicitandoasinformaçõesadi-
cionaiscomo:nome,senha,grupo,pastahome...:
daniel@casadocodigo:~$ sudo adduser paulo
Adding user `paulo` ...
Adding new group `paulo` (1007) ...
Adding new user `paulo` (1003) with group `paulo` ...
Creating home directory `/home/paulo` ...
Copying files from `/etc/skel` ...
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
Changing the user information for paulo
Enter the new value, or press ENTER for the default
Full Name []:
Room Number []:
Work Phone []:
Home Phone []:
Other []:
Is the information correct? [Y/n] Y
Notetodasasop çõessolicitadasaocriarumnovousuário.Apóspreencherou
confirmarsomenteasqueacharnecessário,ousuário pauloserácriadonosistema:
daniel@casadocodigo:~$ id paulo
uid=1003(paulo) gid=1007(paulo) groups=1007(paulo)
daniel@casadocodigo:~$ ls /home/
daniel paulo
daniel@casadocodigo:~$
Utilizeocomando idsemprequequiserobterinformaçõessobreumusuário
dosistema.Eleiráretornar UID, GIDeosgruposaosquaisousuáriopertence.
Agoraquejácriamosumnovogrupoeumnovousuário,vamosadicionaro
usuáriopauloaogrupo suporte.Paraisso,utilizeocomando addgroupque,
66

## Página 74

CasadoCódigo Capítulo6. Administraçãodeusuários
alémdecriarumnovogrupocomovimosanteriormente,tambémpodeadicionar
usuáriosaoutrosgrupos:
daniel@casadocodigo:~$ sudo addgroup paulo suporte
Adding user `paulo` to group `suporte` ...
Adding user paulo to group suporte
Done.
daniel@casadocodigo:~$
Oretornodocomandojánosinformaqueousuário paulofoiadicionadoao
grupo suporte.Podemosverificarcomocomando groupsou id:
daniel@casadocodigo:~$ groups paulo
paulo : paulo suporte
daniel@casadocodigo:~$ id paulo
uid=1003(paulo) gid=1007(paulo) groups=1007(paulo),1005(suporte)
daniel@casadocodigo:~$
Umnovousuáriopodesercriadoedeimediatojápossuirumgrupodenossa
escolha. O adduserpoderiafazerissorecebendocomoargumentosonomedo
usuárioeonomedogrupo: adduser [usuário] [grupo]. Epararemover
usuárioegrupopoderíamosusarocomando deluser,quetemaseguintesintaxe:
deluser [usuário] [grupo].
6.6 A lterando grupos
Comovimosnoiniciodocapítulo,cadaarquivoediretóriopossuiumdonoeum
grupo.Tantoodonocomoogrupoaoqualumarquivooudiretóriopertencepodem
seralterados.Paraisso,usamososcomandos chowne chgrp.
Paratestá-los,vamosusaroarquivo agendaquecriamosanteriormente:
daniel@casadocodigo:~$ ls -l agenda
-rw-rw-r-- 1 daniel daniel 136 Oct 2 00:49 agenda
daniel@casadocodigo:~$
Odonodoarquivoéousuário daniel,assimcomoogrupoaoqualoarquivo
pertencetambémé daniel.Vamosalterarogrupoaqueoarquivopertencepara
suporte:
daniel@casadocodigo:~$ sudo chgrp suporte agenda
daniel@casadocodigo:~$ ls -l agenda
67

## Página 75

6.6. Alterandogrupos CasadoCódigo
-rw-rw-r-- 1 daniel suporte 136 Oct 2 00:49 agenda
daniel@casadocodigo:~$
Aoalterarogrupo,agoraestamosdandopermissãoparaqueusuáriosqueper-
tencemaogrupo suportepossamteracessoaoarquivo agenda,nestecasoo
usuáriopaulo.
Oqueaconteceriasealterássemosodonodoarquivo?Parafazerissoutilizamos
ocomando chown:
daniel@casadocodigo:~$ sudo chown paulo:suporte agenda
daniel@casadocodigo:~$ ls -l agenda
-rw-rw-r-- 1 paulo suporte 136 Oct 2 00:49 agenda
daniel@casadocodigo:~$
Agoraodonodoarquivoéousuário paulo.Passamoscomoargumentoonome
dogruposeparadopor :paraocomando chown.Estaéasintaxedocomandopara
alterarodonoeogrupo.Paravermaisop ções,consulteadocumentaç ão.
Agoraquemudamosodonoeogrupodoarquivo,seráqueonossousuárioainda
possuipermissãoparafazeralterações?Tenteeditaroarquivoevejaoqueacontece:
Figura6.5:Alertadoeditoraotentaralteraroarquivo
Recebemosumamensagemdealertadoeditorinformandoqueoarquivoestá
68

## Página 76

CasadoCódigo Capítulo6. Administraçãodeusuários
disponívelsomenteparaleituraparaonossousuário. Pararecuperaroacessoao
arquivo,altereodonoeogrupoparaoseuusuário:
daniel@casadocodigo:~$ sudo chown daniel:daniel agenda
daniel@casadocodigo:~$ ls -l agenda
-rw-rw-r-- 1 daniel daniel 136 Oct 21 01:16 agenda
daniel@casadocodigo:~$
Durantetodooprocesso,notequeo sudofoiutilizado,poiseleéquemtem
opoderdedelegartodasessasatribuiçõesnosistemaeescolherusuários,grupose
permissões.
Comaspermissõescorretas,podemosexecutaraplicaçõesquesódeterminados
usuáriospodem. Praexecutarprogramasinteressantes,vamosaprenderainstalá-
los!
69

## Página 78

Capítulo7
Instalandopacoteseaplicativos
CadadistribuiçãoLinuxpossuipacotesespecíficos.Vamosaprenderumpoucoso-
breeles,comoinstalá-loseremovê-losdosistema.
Primeiramente,vamosentenderoqueéumpacote.Umpacoteéumconjunto
dearquivosagrupadosparafacilitarainstalaç ãoedistribuiç ãodeumprograma.Ele
podeconter scriptsparalistagemechecagemdedependênciasparaconfiguraç ão
duranteoprocessodeinstalaç ãodeumaplicativo.
No Ubuntuospacotessãobaseadosem Debianetêmaextensão .deb.
7.1 Gerenciador de pacotes
Veremosagorasobregerenciamentodepacotesparainstalaç ão,atualizaçãoeremo-
çãodeaplicativos. Ogerenciadordepacotestrabalhainterpretandoanecessidade
decadapacoteparaqueelepossafuncionardeformacorreta.
Antesdeprosseguirmoscomnossoestudosobreshelleaprendersobregerenci-
amentodepacotesnoterminal,veremosumexemplopráticodeinstalaç ãodeum
aplicativonomodográfico.

## Página 79

7.1. Gerenciadordepacotes CasadoCódigo
Vamosinstalaro google chrome usandoainterfacegráficadegerenciamento
depacotes.Paraisso,faç aodownloaddopacote .debemhttp://www.google.com/
intl/pt-BR/chrome/:
Figura7.1:Downloaddopacote.debdogooglechrome
Depossedopacote,vamosàinstalaç ão.Cliquecomobotãodireitodomouse
emcimadopacoteeescolhaaop ção Abrir com Central de programas do Ubuntu:
72

## Página 80

CasadoCódigo Capítulo7. Instalandopacoteseaplicativos
Figura7.2:Instalandoopacoteusandoogerenciadorgráfico
Agora,bastaclicarem Instalareteremoso google chrome instaladoem
nossosistema:
73

## Página 81

7.1. Gerenciadordepacotes CasadoCódigo
Figura7.3:Efetivandoainstalaç ão
Ogerenciadorirásolicitarasenhadoseuusuário,queéamesmaquevocêcadas-
trouduranteoprocessodeinstalaç ão.Informeasenhaecliqueem Autenticar:
74

## Página 82

CasadoCódigo Capítulo7. Instalandopacoteseaplicativos
Figura7.4:Autenticaçãonecessáriaparainstalarpacotes
Aguardeatéoprocessodeinstalaç ãoserconcluído–ogerenciadorvaiinformar
queopacotefoiinstalado.Testeonovoaplicativoeverifiquequetudoocorreucom
sucesso:
75

## Página 83

7.2. GerenciandopacotescomAPT CasadoCódigo
Figura7.5:Testandoogooglechromeapósainstalaç ão
Agoraquejávimosumademonstraç ãodeinstalaç ãonoambientegráfico,volta-
remosparao shelleaprenderemossobreogerenciador apt.
7.2 Gerenciando pacotes com APT
Veremosaquiumpoucosobregerenciamentodepacotesnoterminalutilizando
aferramenta APT (Advanced Packaging T ool). Paraisso, usaremosocomando
apt-get,queéumainterfaceparaaferramenta APT.Assimcomoo apt-get,
existeoutrainterfaceparao APT,o aptitude.Masemnossosestudosusaremos
o apt-getparainstalar,atualizareremoveraplicativos.
Lembre-sedesempreverificaromanualdeumcomando.Faç ausoexcessivodo
man!
Antesdeprosseguir,vamosentenderalgumasop çõesdo apt-get:
•update:atualizaalistadepacotes;
•upgrade:atualizatodoosistema;
76

## Página 84

CasadoCódigo Capítulo7. Instalandopacoteseaplicativos
•install:instalaumnovoprograma;
•remove:desinstalaumprograma.
Paraentendermelhorcomofuncionao apt-get,vamosfazerainstalaç ão
do Java. OpacoteOracleJDKfoiremovidodorepositóriooficialdoUbuntude-
vidoànovalicen çado Java. Porcontadisso,usaremosumrepositórioalternativo
parainstalaropacotedoJava. Veremosmaisumaop çãodo apt-get,ondeadi-
cionamosumnovocanaldesoftwaresusandoaop ção add-apt-repository
ppa:xxxxxx/xxxx.Lembre-sedeutilizaro sudo:
daniel@casadocodigo:~$ sudo add-apt-repository ppa:webupd8team/java
O sudovaisolicitarsuasenha,informe-aparacontinuaretecle ENTERquando
forsolicitado:
daniel@casadocodigo:~$ sudo add-apt-repository ppa:webupd8team/java
[sudo] password for daniel:
You are about to add the following PPA to your system:
Oracle Java (JDK) Installer (automatically downloads and installs
Oracle JDK6 / JDK7 / JDK8). There are no actual Java files in this PPA.
More info: http://www.webupd8.org/2012/01/
install-oracle-java-jdk-7-in-ubuntu-via.html
Debian installation instructions:
http://www.webupd8.org/2012/06/
how-to-install-oracle-java-7-in-debian.html
More info: https://launchpad.net/~webupd8team/+archive/java
Press [ENTER] to continue or ctrl-c to cancel adding it
gpg: keyring `/tmp/tmpXshrbm/secring.gpg' created
gpg: keyring `/tmp/tmpXshrbm/pubring.gpg' created
gpg: requesting key EEA14886 from hkp server keyserver.ubuntu.com
gpg: /tmp/tmpXshrbm/trustdb.gpg: trustdb created
gpg: key EEA14886: public key "Launchpad VLC" imported
gpg: Total number processed: 1
gpg: imported: 1 (RSA: 1)
OK
Apósadicionaranovafontederepositório,énecessárioatualizaralistadepa-
cotes–usaremosaopção update:
77

## Página 85

7.2. GerenciandopacotescomAPT CasadoCódigo
daniel@casadocodigo:~$ sudo apt-get update
Depoisdeatualizaralistadepacotes,vamosfinalmenteinstalaro Java,usando
aop ção install:
daniel@casadocodigo:~$ sudo apt-get install oracle-java7-installer
Aorodarocomandoanterior,o APTvaiinformaroqueseráinstaladojunto
comasdependências. Quandoo APTperguntarsedesejacontinuar,tecle Ypara
informarquesim:
daniel@casadocodigo:~$ sudo apt-get install oracle-java7-installer
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following extra packages will be installed:
gsfonts gsfonts-x11 java-common
Suggested packages:
default-jre equivs binfmt-support visualvm ttf-baekmuk
ttf-unfonts ttf-unfonts-core ttf-kochi-gothic
ttf-sazanami-gothic ttf-kochi-mincho ttf-sazanami-mincho
ttf-arphic-uming firefox firefox-2 iceweasel mozilla-firefox
iceape-browser mozilla-browser epiphany-gecko
epiphany-webkit epiphany-browser galeon midbrowser
moblin-web-browser xulrunner xulrunner-1.9 konqueror
chromium-browser midori google-chrome
The following NEW packages will be installed:
gsfonts gsfonts-x11 java-common oracle-java7-installer
0 upgraded, 4 newly installed, 0 to remove and 18 not upgraded.
Need to get 3,462 kB of archives.
After this operation, 5,351 kB of additional disk space will be used.
Do you want to continue [Y/n]? Y
OinstaladordoJavavaiinformarsobreostermosdelicen çadeuso.Paraconti-
nuar,tecle Enter:
78

## Página 86

CasadoCódigo Capítulo7. Instalandopacoteseaplicativos
Figura7.6:Javainstaller
Emseguidaoinstaladorperguntasevocêaceitaostermosdeusodalicen ça.
Escolha Yesetecle Enterparacontinuarefinalizarainstalaç ão:
Figura7.7:Javainstallerlicen çadeuso
ParafinalizarvamosconferiraversãodoJavaquefoiinstalada.Execute java
-version:
79

## Página 87

7.2. GerenciandopacotescomAPT CasadoCódigo
daniel@casadocodigo:~$ java -version
java version "1.7.0_40"
Java(TM) SE Runtime Environment (build 1.7.0_40-b43)
Java HotSpot(TM) Client VM (build 24.0-b56, mixed mode)
daniel@casadocodigo:~$
Pronto!Instalaçãocomsucesso.
80

## Página 88

Capítulo8
Prática,instalandoApache,PHPe
MySQL
Nestecapítuloiremospraticartudooquevimosatéaqui,desdenavegaç ão,edição
dearquivosatéinstalaçãodepacotes.Conheceremosumpoucosobreconfiguraç ão
econtroledeserviçoseentenderemosmaissobreusuáriosegrupos.
Nossoobjetivoserádeinstalareconfiguraro web server Apache,alinguagemde
programação PHPeobancodedados MySQL.Faremosos3funcionaremconjunto.
Nãosepreocupecasovocênãoosconhe ça. Sãosoftwaresmuitoutilizadose
foramescolhidoscomoexemploparaquevocêentendabemomecanismodeinsta-
laçãodepacotes.
8.1 Instalando o Apache
Vamoscomeçarinstalandoprimeiroo Apache.Paraisso,antesprecisamosatualizar
anossalistadepacoteseinstalarumpacoteessencialparaoprocessodecompilaç ão

## Página 89

8.1. InstalandooApache CasadoCódigo
deoutrospacotes.
Eleéo build-essential,quepossui,porexemplo,compiladorparaalin-
guagemC(oGCC)eoutrasferramentas.
Atualizealistadepacotesdoseurepositório,fazendoocomandoquejáconhe-
cemos:
daniel@casadocodigo:~$ apt-get update
[sudo] password for daniel:
Informeasenhadoseuusuárioeprossigacomoprocessodeatualizaç ão. Em
seguida,podemosinstalaropacote build-essential:
daniel@casadocodigo:~$ sudo apt-get install build-essential
Agorainstaleopacote apache2.Serãolistadasasdependênciasqueserãoins-
taladasjuntoaopacote apache2–osistemadevesolicitaraconfirmaçãoparapros-
seguircomainstalaç ão.Faça:
daniel@casadocodigo:~$ sudo apt-get install apache2
Sempre que quiser obter informações sobre um pacote, utilize o comando
apt-cache,quepossuiaseguintesintaxe apt-cache show pacote.Faç aum
testecomopacote apache2:
daniel@casadocodigo:~$ sudo apt-cache show apache2
Podemosnotarqueforaminformadosmuitosdetalhessobreopacote,comolista
dedependências,versãoedescriç ão.
Seo Apachefoiinstaladocomsucesso,jádeveestarfuncionando.Faç aumteste
acessandopelobrowseroendere çohttp://localhostouhttp://127.0.0.1,evocêverá
umamensagemdo Apacheinformandoqueowebserverestáfuncionando:
82

## Página 90

CasadoCódigo Capítulo8. Prática,instalandoApache,PHPeMySQL
Figura8.1:Apacheinstaladoefuncionando
Agoraquetemosowebserver Apacheinstaladoefuncionando,podemosfazer
testesparaentendersobreserviços.Apósainstalaç ão,owebserverficadisponível
nosistemaemformadeserviço;sendoassim,usaremosocomando servicepara
verificarasop çõesdisponíveisparaoserviço apache2queinstalamos:
daniel@casadocodigo:~$ sudo service apache2
* Usage: /etc/init.d/apache2 {start|stop|graceful-stop|restart|reload|
force-reload|start-htcacheclean|stop-htcacheclean|status}
daniel@casadocodigo:~$
Notequeocomando serviceexecutaoscriptdeserviços apache2locali-
zadoem /etc/init.d/apache2,quepossuiasváriasop çõescomoiniciar,parar,
restartareoutras.
Testeo serviceparandooserviço apache2.Paraisso,execute:
daniel@casadocodigo:~$ sudo service apache2 stop
* Stopping web server apache2
apache2: Could not reliably determine the server's fully qualified domain
name, using 127.0.0.1 for ServerName
83

## Página 91

8.2. Linkandoarquivos CasadoCódigo
... waiting . [ OK ]
daniel@casadocodigo:~$
Foiinformadoqueooserviço apache2foiinterrompido.Váaobrowseredê
refreshparaverificarqueapágina It works! nãoestámaisacessível. Parainiciaro
serviçonovamente,faç a:
daniel@casadocodigo:~$ sudo service apache2 start
* Starting web server apache2
apache2: Could not reliably determine the server's fully qualified domain
name, using 127.0.0.1 for ServerName [ OK ]
daniel@casadocodigo:~$ ]
Usaremosbastanteocomando servicedaquiprafrente,lembre-sedepesqui-
sarsobreelecomo man.
Reiniciesuamáquinaevejaque,porpadrão,oserviçodoApacheéinicializado
automaticamente. Algunspacotes,comooApache,alémdeinstalarumserviço,
torna-oautoinicializável.
8.2 Linkando arquivos
Antesdeprosseguirfaremosumpequenodesvioparaverumpoucosobrelinkagem
dearquivos,ouseja,comofazerum link. Éalgoqueaparececomfrequênciano
Linux.
O apachefazbastanteusodelinkagemdearquivosemsuasconfigurações,
assim,agoratemosexemplosmaisricos.
Parafazerumlink,utilizamosocomando ln -s,quecriaumlinksimbólico
paraoarquivodeorigem–seuconteúdoéocaminhodoarquivo. Paraentender
melhor,observealistagemnasconfiguraçõesdo apache:
daniel@casadocodigo:/etc/apache2/sites-enabled$ ls -l
total 0
lrwxrwxrwx 1 root root 26 Oct 3 23:11 000-default ->
../sites-available/default
daniel@casadocodigo:/etc/apache2/sites-enabled$
Notequeoarquivo 000-defaultestáapontandoparaoarquivo default,
queficanodiretório sites-available. Vamoscriarumlinksimbólicoparao
defaultcomoutronome,paraissodevemosantesremoverolinkquejáexiste:
84

## Página 92

CasadoCódigo Capítulo8. Prática,instalandoApache,PHPeMySQL
daniel@casadocodigo:/etc/apache2/sites-enabled$ sudo rm 000-default
daniel@casadocodigo:/etc/apache2/sites-enabled$ sudo ln -s
../sites-available/default daniel-config
daniel@casadocodigo:/etc/apache2/sites-enabled$
daniel@casadocodigo:/etc/apache2/sites-enabled$ ls -l
total 0
lrwxrwxrwx 1 root root 26 Oct 20 21:23 daniel-config ->
../sites-available/default
daniel@casadocodigo:/etc/apache2/sites-enabled$
Éimportantesaberqueexistemdoistiposdeligaç ões:
•Hardlink:criaumarquivoigualcapazdecompartilharosdados;
•Linksimbólico:ésomenteumcaminhoparaoarquivooriginal.
Noexemploanterior, criamosumlinksimbólico. Semaop ção -snoco-
mando ln, teríamos criado um hard link. Agora qualquer alteração no link
daniel-configqueseencontranodiretório sites-enabledserárefletidano
arquivo default,queficaem sites-available.
OLinuxutilizabastanteorecursodelinkagemdearquivos,atémesmoparare-
presentarohardwareduranteoprocessodecomunicaç ãocomokernel. Listede
formadetalhadaodiretório /devparaveraquantidadede hard linkse links simbó-
licosutilizadospelosistema.
Agoraqueentendemosumpoucodesterecurso,vamosprosseguir!
8.3 Instalando e configurando o MySQL
Vamosprosseguirinstalandoeconfigurandoo MySQL.Eleéumsistemadegeren-
ciamentodebancodedadosrelacionalbastantepopular,muitousadoemconjunto
comaplicaçõesbemconhecidascomoo WordPress.
Oprimeiropassoéinstalaropacote mysql-server,eparaissofaç a:
daniel@casadocodigo:~$ sudo apt-get install mysql-server
Maisumavez,o apt-getvaiinformarospacotesextrasqueserãoinstalados
eototaldeespaçoemdiscoqueseráconsumidonainstalaç ão.Suaconfirmaç ãoé
necessáriaparacontinuar.
85

## Página 93

8.3. InstalandoeconfigurandooMySQL CasadoCódigo
Duranteoprocessodeinstalaç ãodo mysqlserásolicitadaadefiniçãodesenha
paraousuário root:
Figura8.2:Instalaç ãodoMySQL
Definaasenhadeusuário rootousimplesmentetecle Enterpoiséopcional,
jáquesetratadeumainstalaç ãoemsuamáquinalocal:
Figura8.3:DefiniçãodesenhaparaousuáriorootdoMySQL
86

## Página 94

CasadoCódigo Capítulo8. Prática,instalandoApache,PHPeMySQL
Apósainstalaç ão,verifiqueseoserviço mysqlestárodandoemseusistema.
Useocomando servicecomaop ção status:
daniel@casadocodigo:~$ sudo service mysql status
mysql start/running, process 11879
daniel@casadocodigo:~$
Notequeeleinformaqueoserviçoestárodando. Ainformaç ão process
11879exibidarefere-seaonúmerodoprocessodoserviçonosistema. Essenú-
merovaivariar,eseráprovavelmentediferentenasuamáquina. Nãosepreocupe,
entenderemossobreprocessosnopróximocapítulo.
Agoratesteo mysqlefetuandologinnoserviçocomousuário root:
daniel@casadocodigo:~$ sudo mysql -u root -p
Enter password:
O mysqlsolicitaráasenhade rootquefoidefinidanoprocessodeinstalaç ão.
Apósinformá-la,vocêveráumatelacomoaseguinte:
Figura8.4:ConectandoaoMySQLpeloshell
Listeosbancosdedadosdisponíveis:
mysql> show databases;
+--------------------+
87

## Página 95

8.4. InstalandoeconfigurandooPHP CasadoCódigo
| Database |
+--------------------+
| information_schema |
| mysql |
| performance_schema |
| test |
+--------------------+
4 rows in set (0.00 sec)
mysql>
Parasair,faça:
mysql> quit
Bye
daniel@casadocodigo:~$
Assimcomoo apache,o mysqltambéméumserviçoe,comotal,possuias
mesmasregrasdisponíveisno service. Issopossibilitaparar,iniciar,recarregar,
verostatus,igualfizemosno apache:
daniel@casadocodigo:~$ sudo service mysql stop
mysql stop/waiting
daniel@casadocodigo:~$ sudo service mysql status
mysql stop/waiting
daniel@casadocodigo:~$ sudo service mysql start
mysql start/running, process 12089
daniel@casadocodigo:~$ sudo service mysql status
mysql start/running, process 12089
daniel@casadocodigo:~$
8.4 Instalando e configurando o PHP
Vamosprosseguircomanossapráticainstalandoeconfigurandoo PHP.Instala-
remostrêspacotes, php5–pacotedalinguagem,php-pear–pacotecomclasses
baseparao phpeo php5-mysql–pacoteparacomunicaçãocomobancodedados
mysql.Parainstalarfaç a:
daniel@casadocodigo:~$ sudo apt-get install php5 php-pear php5-mysql
Agoraqueinstalamoso php,precisamosajustaroseuarquivodeconfiguraç ão
queestáem /etc/php5/apache2/php.ini.Vamospermitirmensagensdeerro
88

## Página 96

CasadoCódigo Capítulo8. Prática,instalandoApache,PHPeMySQL
maisdescritivaseativarlogs.Paraisso,vamoseditaro php.ini.Utilizeo vimou
nano:
daniel@casadocodigo:~$ sudo vim /etc/php5/apache2/php.ini
Comoarquivoaberto,busquepor error_reporting.No vim,faça:
/error_reporting =
Essainstruçãono vimirábuscarpelotexto error_reporting = noarquivo.
Apósencontrar,editealinhaefaç aaseguintealteraç ão:
De:
error_reporting = E_ALL & ~E_DEPRECATED
Para:
error_reporting = E_COMPILE_ERROR|E_RECOVERABLE_ERROR|E_ERROR|
E_CORE_ERROR
Destaforma,estamosalterandooformatodasmensagensdeerrodo phppara
seremmaisdescritivas.Agoravamosespecificaroarquivodelogsondeo phpdeverá
salvar:busqueno vimadiretiva error_log = edescomenteapagandoo ;no
iniciodalinha.Emseguida,insiraoseguintecaminho:
error_log = /var/log/php.log
Pronto,agoraoslogsdo phpirãosersalvosnoarquivo php.loglocalizadono
diretório /var/log.Salveoarquivo,saiadoeditoreno vimfaça: :wq.
Devoltaao shell,agoraquealteramosasconfiguraçõesdo phpprecisamos
recarregaro apacheparaqueeleentendaasnovasconfiguraçõessetadasno php.
Execute:
daniel@casadocodigo:~$ sudo service apache2 reload
Aop ção reloaddo apachevairecarregarosmóduloseasnovasconfigurações
semprecisarrestartaroserviçoporcompleto.
Agoraqueinstalamoseconfiguramoso php,éumaboaideiaverificarseestá
funcionandoperfeitamente.Paraisso,vamoscriarumscriptdetesteem phpecon-
ferirseestátudook.Crieumnovoarquivochamadode teste.phpem /var/www,
ecomo vimfaça:
89

## Página 97

8.4. InstalandoeconfigurandooPHP CasadoCódigo
daniel@casadocodigo:~$ sudo vim /var/www/teste.php
Insiranoarquivooseguintetrechodecódigo:
<?php
phpinfo();
?>
Salveoarquivoesaiadoeditorcom :wq;emseguidaconfiraoresultadono
browser,acessandohttp://localhost/teste.php.
Figura8.5:Testeparaverificarseophpfoiinstaladocorretamente
Querumdesafio? InstaleoWordPress. Existemváriasformasdefazerisso.
Talvezamaissimplesserábaixarosarquivosfontesdo http://www.wordpress.org
edescompactá-losemumdiretório.Apósisso,bastaconfiguraroApache,editando
seuarquivodeconfiguraç ão,paraqueessediretóriosejavisualizadoporum virtual
host.Sim,vocêterádeleralgumaspáginasdeinstruções,masvocêjápossuitodoo
conhecimentodeLinuxbásicoparatal!
Casoseinteresseporprogramaç ão,nãodeixedeconheceroslivrosdosmeus
outroscolegasdaCasadoCódigo,inclusivesobrePHP.
90

## Página 98

Capítulo9
Entendendoprocessos
VamosnosaprofundarumpoucomaisnoLinuxeconhecersobreoseubackground.
Veremoscomofuncionasuainicializaç ãoecomoosserviçossãogerenciados,mas
antesprecisamosentenderoquesãoprocessos.
9.1 O que são processos?
AdefiniçãodeprocessoapresentadaporTanenbaumnolivro SistemasOperacio-
nais-ProjetoeImplementaç ão:
A ideia-chave aqui é que um processo é um tipo de atividade. Ele tem um programa,
entrada, saída e um estado. Um único processador pode ser compartilhado entre vá-
rios processos, com algum algoritmo de agendamento sendo utilizado para determinar
quando parar de trabalhar em um processo e servir a um diferente.
Penseemumprocessocomoarepresentaç ãodeumprogramaemexecuç ãouti-
lizandoosrecursosdocomputadorpararealizaralgumatarefa.
Umprocessopossuiestadosquedefinemoseucomportamento,sãoeles:

## Página 99

9.2. Oprocessoinit CasadoCódigo
•execução:oprocessoestáativoutilizandoaCPUeoutrosrecursos;
•prontoou espera: oprocessoestátemporariamenteparadopermitindo
queoutroprocessoexecutenasuafrente;
•bloqueado:oprocessoestáparadoaguardandoaexecuç ãodealgumevento
paravoltaraoestadode execução.
Alémdepossuiressescomportamentos,umprocessoécapazdecriaroutros
processos. Quandoissoocorredizemosqueumprocessoépaidosoutroscriados
porele.
CadaprocessonoLinuxrecebeumnúmeroparasuaidentificaç ãoconhecido
por PID.Podemosvê-loscomocomando ps:
daniel@casadocodigo:~$ ps aux
USER PID %CPU %MEM VSZ RSS TTY STAT START TIME COMMAND
root 1 0.5 0.3 3516 1908 ? Ss 18:49 0:00 /sbin/init
root 2 0.0 0.0 0 0 ? S 18:49 0:00 [kthreadd]
root 3 0.0 0.0 0 0 ? S 18:49 0:00 [ksoftirq]
root 4 0.0 0.0 0 0 ? S 18:49 0:00 [kworker/]
root 5 0.1 0.0 0 0 ? S 18:49 0:00 [kworker/]
Certamente,noseucomputador,oresultadoserádiferente,apresentandooutros
processos,comoutrosids.
9.2 O processo init
QuandoinicializamosoLinux,oprimeiroprocessocriadoéo init,queéconhe-
cidocomoopaidetodososoutros.
Depoisdeinicializaroambientegráfico,quandoabrimosoterminal,umpro-
cessoécriadoparacontrolaroterminalemquestão. Deformasemelhante,para
cadaprogramaabertotambémserácriadoumprocessocorrespondente.O inité
responsávelporinicializartodoselesepossuiaidentificaç ãodenúmero1nosistema.
9.3 A identificação de processos
Comovimos,umprocessoéidentificadoporseu PID(ProcessIdentifier). Esse
númeroédadopelosistemaparacadaprocesso,cada PIDéúnico,entãovocênunca
verádoisoumaisprocessosfazendousodomesmo PID.
92

## Página 100

CasadoCódigo Capítulo9. Entendendoprocessos
Cadaprocessotambémpossuiumusuáriodono,dessaforma,osistemaveri-
ficaaspermissõesesabequalusuáriopodeexecutarumdeterminadoprocesso.A
identificaçãodedonoséfeitapelosnúmeros UIDe GID.
NoLinux,todousuáriopossuiumnúmerodeidentificaç ãodamesmaformaque
osprocessos.Essenúmeroéconhecidopor UID(UserIdentifier)eo GID(Group
Identifier).
9.4 Verificando processos
Verificaregerenciarprocessoséumatarefamuitoimportante,poisàsvezesprecisa-
mosinterromperumprocessoàfor çaouverificarquaisprocessosestãoconsumindo
maisrecursosnocomputador(CPU,memóriaetc).
Veremosalgunscomandosnovos.Vamoscome çarpelocomando ps,queserve
paralistarosprocessosemexecuç ãoeobterinformaçõescomo PIDe UID.
Executeo psparaobteralistadeprocessosdonossousuário:
daniel@casadocodigo:~$ ps
PID TTY TIME CMD
1788 pts/0 00:00:00 bash
1847 pts/0 00:00:00 ps
daniel@casadocodigo:~$
Nocaso,ousuário danielpossuiapenas2processosemexecuç ão:o bash,
queéoprocessodo shell,eopróprio ps,quefoioprocessocriadoaoexecutaro
comando ps.
Assimcomotodososcomandosquevimosatéagora,o pstambémpossuiop-
ções.Veremosalgumasdelas:
•a:listatodososprocessosexistentes;
•u:exibeonomedousuáriodonodoprocesso;
•x:listaosprocessosquenãopossuemrelaç ãocomoterminal;
•m:exibeaquantidadememóriaconsumidaporcadaprocesso.
Paramaisop ções man ps,acombinaç ãomaisusadaé ps aux –executeeveja
alistadeprocessosemexecuç ão:
93

## Página 101

9.4. Verificandoprocessos CasadoCódigo
daniel@casadocodigo:~$ ps aux
USER PID %CPU %MEM VSZ RSS TTY STAT START TIME COMMAND
root 1 0.0 0.3 3516 1908 ? Ss 18:49 0:00 /sbin/init
root 2 0.0 0.0 0 0 ? S 18:49 0:00 [kthreadd]
root 3 0.0 0.0 0 0 ? S 18:49 0:00 [ksoftirq]
root 5 0.0 0.0 0 0 ? S 18:49 0:00 [kworker/]
root 6 0.0 0.0 0 0 ? S 18:49 0:00 [migratio]
root 7 0.0 0.0 0 0 ? S 18:49 0:00 [watchdog]
root 8 0.0 0.0 0 0 ? S< 18:49 0:00 [cpuset]
root 9 0.0 0.0 0 0 ? S< 18:49 0:00 [khelper]
root 10 0.0 0.0 0 0 ? S 18:49 0:00 [kdevtmpf]
Notequepodemosverousuáriodonodecadaprocessonaprimeiracoluna
USER.Emseguidatemoso PIDdecadaprocesso,informaçõesdeconsumode CPU
ememória,outrasinformaçõescomodataehoradequandooprocessofoiiniciali-
zado,assimcomoonomedoprocesso.
Podemoscontartodososprocessosemexecuç ãofazendousodeumcomando
queaindanãotestamos:o wc.Basicamenteoqueelefazécontaraslinhasdeum
arquivooudoconteúdoqueforexibidonoterminal,paraissoutilizamosaop ção wc
-l.Parainformaraocomandoquequeremosapenasaquantidadedelinhas,oque
faremoséexecutaro ps aux emcombinaçãocomo wc -l,usandoo |(pipe),
queéumaformadeencadeamentodeprocessos:
daniel@casadocodigo:~$ ps aux | wc -l
82
daniel@casadocodigo:~$
Oqueo |fezfoiencadearaexecuç ãodocomando ps aux aocomando wc
-l.Assim,elepegouoresultadogeradodoprimeirocomandoepassouparaose-
gundo. Asaídado wcnosmostraquantosprocessosaotodotemosrodandoem
nossocomputador.
Outrocomandoqueaindanãovimoséo grep,queprocuraporumaexpressão
quepodeserumapalavraoufraseemumarquivo,ouaindapodefuncionarcomo
filtronasaídadecomandos. Vamosusá-loparafiltraralistadeprocessosgerada
com ps -A ebuscartodososprocessosdo apachequeestiverememexecuç ão.A
opção -Adocomando pséparaexibirtodososprocessosemexecuç ãomassem
detalhes.
daniel@casadocodigo:~$ ps -A | grep apache
1166 ? 00:00:00 apache2
94

## Página 102

CasadoCódigo Capítulo9. Entendendoprocessos
1184 ? 00:00:00 apache2
1185 ? 00:00:00 apache2
1186 ? 00:00:00 apache2
1187 ? 00:00:00 apache2
1188 ? 00:00:00 apache2
daniel@casadocodigo:~$
Foramretornadossomenteosprocessoscomnome apache,poiso greprea-
lizouumfiltroparaignorartodoorestoeexibiroqueprocurávamos.Experimente
executar ps -A paraverotamanhodalistadeprocessos.
Veremosagoraoutrocomandobastanteusadoparaverificarprocessos,o top,
queacompanhaosprocessosatualizandoasinformaçõesquaseemtemporeal.Exe-
cutenoterminalo topparavê-lofuncionando:
Figura9.1:Executandootop
Napartesuperior,logonasprimeiraslinhas,temosinformaçõessobreosistema,
comnúmerototaldeprocessos,usoda CPU,usodamemória.Emseguida,temos
alistadosprocessosexistentes.Paraobterajudasobreouso,tecle he,parasairdo
top,tecle q.Otoppossuimuitasop ções,vejaalgumasem man top.
Umaop çãointeressanteéacompanharosprocessosdeumdeterminadousuário
dosistema.Paraissousamosaop ção -ueonomedousuário:
95

## Página 103

9.4. Verificandoprocessos CasadoCódigo
daniel@casadocodigo:~$ top -u daniel
Figura9.2:Executandofiltronotop
Dessaforma,estamosexecutandoumfiltroparaexibirsomenteosprocessos
pertencentesaousuário daniel.
Umaoutraop çãoao topéo htop,quetemumainterfacemaisamigável.Ele
nãoveminstaladoporpadrão,entãovamosinstalarparaconhecê-lo:
daniel@casadocodigo:~$ sudo apt-get install htop
Apósainstalaç ão,execute htop:
96

## Página 104

CasadoCódigo Capítulo9. Entendendoprocessos
Figura9.3:Executandoohtop
Bemmelhor,nãoémesmo?
Agoraépossívelidentificarrapidamenteasinformações.OconsumodeCPUe
memóriaficoumaisamigável,enabarrainferiorexisteummenucomop ções.Por
exemplo,tecle F1paraobterajuda:
97

## Página 105

9.5. Oquesãosinaisdeprocessos? CasadoCódigo
Figura9.4:Obtendoajudanohtop
Navegueumpoucono htop,leiaadocumentaç ão,parasairtecle qou F10.
9.5 O que são sinais de processos?
NoLinuxossinaissãoumaformadecomunicaç ãousadapelosprocessosparaque
osistemaconsigainterferiremseufuncionamento. Naprática,aoreceberumsi-
nalcominstruções,umprocessointerpretaaaç ãoquefoiespecificadanosinalea
executa.
Algunsdossinaismaisconhecidoseusadosporprocessossão:
•KILL:sinalcomfun çãodeencerrarumprocesso;
•TERM:terminaoprocessoapóselefinalizarumatarefa;
•STOP:interrompeaexecuç ãodeumprocesso;
•CONT:ativaaexecuç ãodeumprocessoquefoiinterrompido.
Paraentendermelhorsobresinais,vamosverumpoucodocomando kill.Este
comandoéusadoparaoenviodesinaisaprocessos,suasintaxeésimplesedepende
apenasdo PIDdeumprocesso.
98

## Página 106

CasadoCódigo Capítulo9. Entendendoprocessos
Vamosinterromperaexecuç ãodo mysqlenviandoumsinalde STOPparao
seuprocesso.Precisamosprimeirodonúmero PIDdo mysql:
daniel@casadocodigo:~$ ps -A | grep mysql
1047 ? 00:00:00 mysqld
daniel@casadocodigo:~$
Agoraquetemosonúmero PIDdoprocessodo mysql,vamosenviarosinal
de STOPparaele,interrompendosuaexecuç ão:
daniel@casadocodigo:~$ sudo kill -STOP 1047
daniel@casadocodigo:~$
Paraentenderoquerealmenteocorreu,tenteconectaraoserviçodo mysql:
daniel@casadocodigo:~$ sudo mysql -u root -p
Enter password:
Nadavaiacontecer,ficaremosodiainteiroolhandoestatelapoisoprocessode
execuçãodo mysqlfoiinterrompido.Abraumnovoterminal,envieosinal CONT
paraativaraexecuç ãodoprocessoquefoiinterrompidoevejaoqueaconteceno
terminalondeestamostentandonosconectarao mysql:
daniel@casadocodigo:~$ sudo kill -CONT 1047
daniel@casadocodigo:~$
Aoexecutaroenviodosinal CONTparaoprocessointerrompidodo mysql,
vejaqueelevoltouafuncionarnormalmente.
Ocomando killtambémpodeserusadocomonúmerodosinalemvezdo
seunome,porexemplo, -9representaosinal KILL.Paraentendermelhoroqueo
sinal KILLfaz,abraoeditor vimemumterminaleemoutroterminalbusquepelo
PIDdoeditor.Emseguida,envieosinal -9paraoprocesso:
daniel@casadocodigo:~$ ps -A | grep vim
2488 pts/0 00:00:00 vim
daniel@casadocodigo:~$ sudo kill -9 2488
[1]+ Killed vim
daniel@casadocodigo:~$
Aoenviarosinal KILLparaoprocessodo vim,eleéencerrado.Recebemosuma
mensageminformandoqueoprocessofoi morto,ouseja,aexecuç ãodoaplicativo
foifinalizadaàfor ça.
99

## Página 107

9.5. Oquesãosinaisdeprocessos? CasadoCódigo
Outrocomandobastanteusadoéo killall,quandonãosabemoso PIDou
quandotemosváriosprocessosdomesmoaplicativocomvários PIDsemexecução,
porexemploo apache:
daniel@casadocodigo:~$ ps -A | grep apache
2548 ? 00:00:00 apache2
2553 ? 00:00:00 apache2
2554 ? 00:00:00 apache2
2555 ? 00:00:00 apache2
2556 ? 00:00:00 apache2
2557 ? 00:00:00 apache2
daniel@casadocodigo:~$
Notequetemosvários PIDse,porisso,enviarumsinaldecadavezparacada
PIDtorna-secomplicado.Nestecasousamoso killalleonomedoprocessoem
vezdo PID.Parainterromperaexecuç ãodoprocesso,faríamos:
daniel@casadocodigo:~$ sudo killall -STOP apache2
daniel@casadocodigo:~$
Verifiqueacessandooendere çohttp://localhostenotequeapáginainicialdo
apachenãoirácarregar.Envieosinal CONTpararetornaràexecuç ãonormaldo
processo:
daniel@casadocodigo:~$ sudo killall -CONT apache2
daniel@casadocodigo:~$
Leiamaissobreo killeo killallemsuasdocumentações–essescomandos
sãoimportantesebastanteutilizados.
Osestadosdeumprocesso
Basicamenteexistem4estadosparaumprocesso. Apóssuacriaç ão,oseues-
tadocorrenteé executável;quandoumprocessoestáaguardandoalgumaro-
tinaparaserexecutado,dizemosqueeleestádormindo–esseestadoéchamadode
dormente–;seumprocessoestácongeladoeporalgummotivonãopodeserexe-
cutado,dizemosqueseuestadoé parado;seumprocessoéconsiderado morto,ou
seja,foifinalizado,nãoestámaisemexecuç ãomasporalgummotivoaindaexiste,
dizemosqueseuestadoédeumprocesso zumbi.
100

## Página 108

CasadoCódigo Capítulo9. Entendendoprocessos
9.6 P rocessos e suas prioridades
Durantesuaexecução,umprocessopodeterprioridadeemrelaç ãoaosoutros.Para
entendermelhorcomofuncionamasprioridades,vamosveroconceitodegentileza.
Imagineumprocessoemexecuç ãosendogentil(oferecendoagentileza)dedei-
xarumprocessocomprioridademaiorpassarasuafrenteeserexecutadoantes.Os
processostrabalhamcomníveisdegentileza,quepodemserdefinidosatravésdo
comando niceeumnúmeroentre -19 e 19,quedeterminaoquãogentilum
processopodeser.Quantomaiorforonúmerodefinido,maisgentiloprocessoserá,
logoquantomenorforonúmero,maiorasuaprioridade.
Normalmentenãoprecisamosdeterminarasprioridadesdeumprocessopoiso
Linuxtrabalhadeformainteligenteparafazerisso.
Emalgunscasos,porexemplotarefasdebackup,setamosaprioridadeparaqueo
processonãoconsumadeformainesperadarecursosdocomputadorcomomemória
eCPU.Nessescasos,podemosusar2comandos:o niceeo renice.
Porenquanto,vamostestaro reniceealteraraprioridadedoprocessoqueestá
executandoo mysql:
daniel@casadocodigo:~$ ps -A | grep mysql
2340 ? 00:00:03 mysqld
daniel@casadocodigo:~$
Agoraquetemoso PIDdoprocessopodemosalterarsuaprioridade,paraisso
faça:
daniel@casadocodigo:~$ sudo renice -19 2340
2340 (process ID) old priority 0, new priority -19
daniel@casadocodigo:~$
Notequeocomandonosinformaaprioridadeantigaqueera0paraanovapri-
oridadequeé-19. Processoscomprioridade0sãointermediáriospoisestãobem
nomeiodosextremos.Aosetarmosaprioridade-19,estamosinformandoqueesse
processoépoucogentiletodososoutrosdeixá-lo-ãopassarnafrente.
Vamosalterarnovamentesetandoumanovaprioridadeetornandoesseprocesso
gentil:
daniel@casadocodigo:~$ sudo renice +15 2340
2340 (process ID) old priority -19, new priority 15
daniel@casadocodigo:~$
101

## Página 109

9.6. Processosesuasprioridades CasadoCódigo
Agoratemosumprocessogentildeprioridade15,queirápermitirqueoutros
passemàsuafrenteesejamexecutadosantes.Épossívelveraprioridadedospro-
cessosno htop:
Figura9.5:ColunaNImostraaprioridadedosprocessos
Note,nacoluna NI,todasasprioridadescom0eapenasumaop çãocomvalor
15queéadoprocessoquefoialterado.
102

## Página 110

Capítulo10
IntroduçãoaShellScript
Scriptéumprogramanãocompiladoqueéenviadoparaumprocessador. Emse-
guida,uminterpretadorlêseucódigoeotraduz,demodoqueoprocessadorentende
suasinstruções,queserãoexecutadasemseguida.
Shell Scriptéalinguagemdeprogramaç ãoutilizadapelo shell–nocasoo
shelléonossointerpretadorquevailerosnossosprogramasedizeraoprocessador
oquefazer.
Programasem Shell Scriptsãoescritosparatarefasadministrativaserepetitivas
noLinux.Aofazerisso,estamosautomatizandoprocedimentospormeiodescripts.
VeremosobásicodeShellScriptnestecapítuloe,aofinal,teremosumscript
simplesparaautomatizarumatarefadebackup.Alémdisso,conheceremosalguns
novoscomandosbastanteutilizados.
10.1 Oprimeiro script
Vamosverumexemplodeumprogramabemsimples:

## Página 111

10.2. Executandooscript CasadoCódigo
#!/bin/bash
# Nosso primeiro programa em Shell Script
mkdir ~/relatorio
ps aux > ~/relatorio/processos.txt
echo "Programa executado com sucesso!"
Nossoprimeiroprogramaéumscriptmuitosimples.Linhasquecome çamcom
#sãocomentáriosouseja,sãodesprezadasduranteaexecuç ãodoscript. Porém
aprimeiralinha,queatépareceumcomentário,énaverdadeumindicadorpara
informarqualprogramairáexecutaroscript.Nonossoexemplo,éoprograma bash
queestálocalizadoem /bin.
Basicamente,oqueoscriptestáfazendoécriarumapastachamada relatorio
nodiretório homedonossousuário.Emseguida,éexecutadoocomando ps aux
paralistartodososprocessosdetalhadamente.Asaídadessecomandoésalvadaem
umarquivochamado processos.txtdentrodapastaquefoicriada. Porfim,
oprogramaemiteumamensagemnoterminalinformandoquefoi "executado
com sucesso".
10.2 Executando o script
Paraexecutaronossoprimeiroprogramaéprecisoalteraraspermissõesdeforma
queotorneumexecutávelparatodososusuários:
daniel@casadocodigo:~$ ls -l primeiro_programa.sh
-rw-rw-r-- 1 daniel daniel 147 Oct 10 22:40 primeiro_programa.sh
daniel@casadocodigo:~$ chmod 777 primeiro_programa.sh
daniel@casadocodigo:~$ ls -l primeiro_programa.sh
-rwxrwxrwx 1 daniel daniel 147 Oct 10 22:40 primeiro_programa.sh
daniel@casadocodigo:~$
Agoraquealteramosapermissãodoarquivo primeiro_programa.sh,po-
demosexecutardaseguinteforma:
daniel@casadocodigo:~$ ./primeiro_programa.sh
Programa executado com sucesso!
daniel@casadocodigo:~$
Reparenousodo ./,jáqueoarquivoestánodiretóriocorrente.Sevocêtentar
executarsimplesmentefazendo primeiro_programa.sh,veráqueoshellnão
104

## Página 112

CasadoCódigo Capítulo10. IntroduçãoaShellScript
encontraráoarquivo.Veremos,maisàfrente,comomodificarocaminho( PATH)
deprocuradearquivosdeexecuç ão.
Noteamensagemexibidainformandoqueoprogramafoiexecutado.Podemos
agoraverificarseasinstruçõespassadasnoscriptrealmenteforamexecutadas.Pri-
meiroveremosseapasta relatoriofoicriadanodiretório homeeseoarquivo
processos.txtfoigerado:
daniel@casadocodigo:~$ ls -l ~/relatorio
-rw-rw-r-- 1 daniel daniel 6783 Oct 10 22:56 processos.txt
daniel@casadocodigo:~$
Verifiqueoconteúdodoarquivo processos.txtcomumdoscomandosque
jáaprendeu, cat, headou tail.Devesairalgoparecidocom:
daniel@casadocodigo:~$ head -n 3 relatorio/processos.txt
USER PID %CPU %MEM VSZ RSS TTY STAT START TIME COMMAND
root 1 0.0 0.3 3520 1900 ? Ss 22:34 0:00 /sbin/init
root 2 0.0 0.0 0 0 ? S 22:34 0:00 [kthreadd]
daniel@casadocodigo:~$
Esteéofuncionamentodeumscript: criamoscomqualquereditor,salvamos
preferencialmentecomaextensão .sh,alteramosapermissãoparaquesetorne
umexecutáveleporfim,rodamos.
Comovocêjádeveterpercebido,basicamenteosscriptspodemserinstruções
comoscomandosquevocêjáviuatéaqui.
10.3 Operações básicas
Comotodalinguagemdeprogramaç ão,ShellScripttambémtrabalhacomopera-
çõesnuméricas,variáveiseestruturasdecontrole.Vamosimplementarumexemplo
básicocontandoonúmerodelinhasdeumarquivo.Paraisso,crieumarquivocha-
mado conta_linhas.shcomoeditordesuaescolhaeinsiraoseguinteconteúdo:
#!/bin/bash
echo "Contando as linhas ..."
sleep 5
LINHAS=`cat ~/relatorio/processos.txt | wc -l `
echo "Existem $LINHAS no arquivo."
105

## Página 113

10.4. Estruturasdecontrole CasadoCódigo
Salveoarquivo conta_linhas.sh,altereapermissãoparaqueeletorne-se
executávelcom chmode,emseguida,executeoprogramacomainstruç ão ./:
daniel@casadocodigo:~$ chmod 777 conta_linhas.sh
daniel@casadocodigo:~$ ./conta_linhas.sh
Contando as linhas ...
Existem 81 no arquivo.
daniel@casadocodigo:~$
Oquefizemosdediferente?
Ainstrução sleep 5 realizaumacontagemde5segundosantesdeexecutaras
próximasinstruções–emoutraspalavraséumenfeite.
Emseguidacriamosumavariávelchamada LINHASeatribuímosaelaainstru-
çãoparaverificaroconteúdodoarquivo processos.txtcomocomando cat,e
emseguidacontaraquantidadedelinhasnoarquivo,fazendousodocomando wc
-l.Estaatribuiç ãofoifeitapormeiodosinal =.Porfim,éexibidaumamensagem
queinformaaquantidadedelinhasexistentesnoarquivo.
Estamensagempossuinoseucorpoachamadadavariávelquecriamos,epara
issoutilizamoso $.
10.4 Estruturas de controle
Emnossosexemplos,vimosscriptssemop çõesdecontrole,ouseja,nãoofereciam
escolhas,apenasinstruçõescomcomandosparaexecuç ão. Vamoscriarumpro-
gramasimplesparaverificareinformarseumarquivoexistenodiretório homedo
nossousuário.Paraisso,crieumarquivochamado verificador.sh:
#!/bin/bash
echo "Informe o nome do arquivo que deseja buscar:"
read ARQUIVO
CONSULTA=$(ls ~ | grep $ARQUIVO)
if [ -z $CONSULTA ]; then
echo "$ARQUIVO não foi encontrado!"
else
echo "Arquivo encontrado!"
fi
106

## Página 114

CasadoCódigo Capítulo10. IntroduçãoaShellScript
Altereoarquivodandopermissãodeexecuç ãoeemseguidarodeoscript.Teste
buscandoporarquivosexistentesenãoexistentes:
daniel@casadocodigo:~$ chmod 777 verificador.sh
daniel@casadocodigo:~$ ./verificador.sh
Informe o nome do arquivo que deseja buscar:
Daniel
Daniel não foi encontrado!
daniel@casadocodigo:~$ ./verificador.sh
Informe o nome do arquivo que deseja buscar:
agenda
Arquivo encontrado!
daniel@casadocodigo:~$
Notequeagoraonossoscriptficoumaisexperto,elesolicitaeaguardaqueuma
instruçãosejaexecutadapornós. Nestecaso,elesolicitaonomedoarquivoque
queremosverificarseexiste.Ainstruç ão readéresponsávelporleroquevamos
digitarnoterminalearmazenarparaoscriptcontinuarcomapróximainstruç ão.
Depoisdearmazenarapalavraqueestamosbuscandoemumavariável,oscript
executaumanovainstruç ão,listandooconteúdododiretório homeefiltrandocom
ocomando grepembuscadapalavraquefoiinformada.
Finalmenteentraaestruturadecontrole if,eoscriptverificaseanossains-
truçãoretorna nulocomoparâmetro -z.Seainstruç ãodeconsultafornula,será
exibidaamensageminformandoqueoarquivonãofoiencontrado,casocontrário,
seoarquivorealmenteexistir,eleseráencontradonabuscaeamensageminformará
quefoilocalizado.
NoLinux,muitosserviçospossuemscriptsdecontroleescritosemShellScript.
Listeoconteúdododiretório /etc/init.devejaalguns.Notequeo apacheeo
mysqlpossuemscriptsnestediretório.
Adiferen çasdalistagemparaosscriptsquefizemosaquinestecapítuloéapenas
afaltadaextensão .sh.Elanãoéobrigatóriaquandodefinimosnaprimeiralinha
doscriptoprogramaqueiráexecutá-lo.
Abracomumeditordesuaescolhaoarquivo /etc/init.d/apache2ouuti-
lizeocomando lessparaveroconteúdodoarquivo.Percebaquejánasprimeiras
linhasvemosalgumasinstruçõesqueacabamosdeaprender:
#!/bin/sh
### BEGIN INIT INFO
# Provides: apache2
107

## Página 115

10.5. Realizandoumbackupagendado CasadoCódigo
# Required-Start: $local_fs $remote_fs $network $syslog $named
# Required-Stop: $local_fs $remote_fs $network $syslog $named
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
# X-Interactive: true
# Short-Description: Start/stop apache2 web server
### END INIT INFO
set -e
SCRIPTNAME="${0##*/}"
SCRIPTNAME="${SCRIPTNAME##[KS][0-9][0-9]}"
if [ -n "$APACHE_CONFDIR" ] ; then
if ["${APACHE_CONFDIR##/etc/apache2-}" != "${APACHE_CONFDIR}"]; then
DIR_SUFFIX="${APACHE_CONFDIR##/etc/apache2-}"
else
DIR_SUFFIX=
fi...
Adeclaraçãodoprogramaqueexecutaráoscriptnaprimeiralinhanoexemplo
do apacheéo /bin/sh.Emseguida,temoscometáriosnocódigo,declaraç ãode
variáveiseinstruçõescondicionais.
Podeparecerdifícilàprimeiravista,maséumasériedecomandoscondicionais
deacordocomvariáveisearquivosdeconfiguraç ão.OApacheéumsistemacom-
plexo,háoutrosarquivosdescriptbemmaissimples.Procure-osentreosdiversos
serviçosjáinstaladosnoseuLinux!
OconhecimentodeShellScriptéessencialparaquempensaemadministrar
servidores.Paraconhecermaisdetalhesdestapoderosalinguagem,visite:
http://aurelio.net/shell/
TodoomaterialproduzidoporAurelioJargasémuitorecomendado. Paraco-
nhecermaissobreosoperadoreseinstruçõesdecontroleemshell,visite:
http://aurelio.net/shell/canivete/
10.5 Realizando um backup agendado
AntesdeprosseguirmoscomoShellScripteimplementarmosumscriptdebackup,
faremosumabrevepausaparaexplicarumpoucosobreagendamentodetarefas.
NoLinux,o crontabéresponsávelporagendartarefasparaseremexecuta-
dasemumperíododetempodeterminado. Eleégerenciadoporumserviçocha-
108

## Página 116

CasadoCódigo Capítulo10. IntroduçãoaShellScript
mado crond,queverificaaexistenciadeagendamentosquedevemserexecutados.
O crontabrealiza2tiposdeagendamentos,agendamentodosusuárioseagenda-
mentodosistema.
Ocomando crontabpodeeditar,listarecriarnovosagendamentosparausuá-
rios,vejaasop çõesem crontab --help.Paraverificarseexistemtarefasagen-
dadasparaumdeterminadousuáriofaç a:
daniel@casadocodigo:~$ crontab -u daniel -l
no crontab for daniel
daniel@casadocodigo:~$
Noexemploaindanãoexisteumatarefaagendadaparaousuário daniel.
O agendamento dos usuários é armazenado em
/var/spool/cron/crontabs. Já os agendamentos para o sistema ficam
em /etc,distribuídosemdiretóriosquepodemserorganizadosemagendamentos
porhora,dia,semanaemês:
daniel@casadocodigo:~$ ls -d /etc/cron.*
/etc/cron.d /etc/cron.hourly /etc/cron.weekly
/etc/cron.daily /etc/cron.monthly
daniel@casadocodigo:~$
Vamosdissecarofuncionamentodo crontabparaentendercadaparte.Para
isso,criaremosumexemplodeumatarefaagendadaparaonossousuário.Acada
minutoserálistadooconteúdodapasta homedonossousuário:
daniel@casadocodigo:~$ crontab -u daniel -e
no crontab for daniel - using an empty one
Select an editor. To change later, run 'select-editor'.
1. /bin/ed
2. /bin/nano <---- easiest
3. /usr/bin/vim.basic
4. /usr/bin/vim.tiny
Choose 1-4 [2]:
Aoexecutarocomando crontab -u daniel -e paracriarumanovatarefa
agendadaparaousuário daniel,o crontabperguntaqueeditorqueremosutili-
zar.Escolhaumdesuapreferência–noexemplo,utilizareio vim.Insiraesalveno
fimdonovoarquivogeradoainstruç ão:
109

## Página 117

10.5. Realizandoumbackupagendado CasadoCódigo
*/1 * * * * ls ~ >> ~/crontab.txt
Oqueainstruç ãofazélistaracadaminutooconteúdode homedousuário
danieleinserirooutputdalistagemnoarquivo crontab.txtqueserácriado
tambémem home. Noteousodo >>,quesignificaquesempreseráinseridoo
conteúdodalistagemsempreapósaúltimalinhadoarquivo crontab.txt.Mase
essemontede *?
Cada *representaumaconfiguraçãono crontab,queindica:
•minuto:vaide0a59;
•hora:vaide0a23;
•dia:vaide1a31;
•mês:vaide1a12;
•dia da semana:vaide0a7.
Alémdessasconfigurações,aindapodemosdefinirqualusuárioiráexecutara
tarefaagendada. Emseguida,definimosocomandoouinstruç ãoparaexecuç ão.
Aindaépossívelutilizarosoperadores , - / ,sendoquea (,)serveparaes-
pecificarumalistadevalores,o -serveparaespecificarintervalosdevalores,ea /
serveparapularvalores.
Sevocêimplementouoagendamentodeexemplo,jádevetersepassadomais
de1minuto,entãoverifiquenalistagemdapasta homedoseuusuárioseoarquivo
crontab.txtfoicriadoeseexisteinformaç ãonele:
daniel@casadocodigo:~$ ls cron*
crontab.txt
daniel@casadocodigo:~$ tail -n 3 crontab.txt
relatorio
verificador.sh
vim_basico.txt
daniel@casadocodigo:~$
Seoarquivoexisteecontémasinformaçõesdalistagemdapasta home,nosso
agendamentofuncionouperfeitamente!
Agora que entendemos como funciona o agendamento de tarefas com o
crontab,podemosprosseguireconstruirumscriptdebackupeimplementarnossa
soluçãoautomatizadadebackupagendado.
110

## Página 118

CasadoCódigo Capítulo10. IntroduçãoaShellScript
10.6 Um simples script de backup
Vamosimplementaragoraoscriptpararealizarobackupdodiretório homedo
nossousuário.Paraisso,usaremosocomando tareocomando date.O tarvai
gerarumacópiado homecompactada,o dateiráincrementarascópiasadicio-
nandoainformaçãododia,mês,ano,horaeminutoemqueobackupfoirealizado.
Primeirovamoscriarumapastachamada backupnodiretórioraiz (/)do
nossosistema:
daniel@casadocodigo:~$ sudo mkdir /backup
Crieumarquivochamado backup.sh.Useumeditordesuaescolhaeimple-
menteoseguintescript:
#!/bin/bash
# Script de backup /home/daniel
sudo tar czf /backup/$(date +%d%m%Y-%H%M)-home.tar.gz -C /home/daniel .
Estamosfazendoumacópiadapasta homedousuário danielecompactando
noformato tar.gz.Aocriaracópia,estamosadicionandoadataatualeahorano
momentodobackup. Paraverfuncionando,altereapermissãodoscriptparaque
elepossaserexecutado,emseguidarodeoprograma:
daniel@casadocodigo:~$ chmod 777 backup.sh
daniel@casadocodigo:~$ ./backup.sh
daniel@casadocodigo:~$
Masoqueaconteceu?Obackupfoifeito?Olheodiretório /backup:
daniel@casadocodigo:~$ ls -l /backup
total 12
-rw-r--r-- 1 root root 9935 Oct 13 23:32 13102013-2332-home.tar.gz
daniel@casadocodigo:~$
Onossobackupfoirealizadocomsucesso!Notequeonomedoarquivogerado
contémadataehoradacriaç ão 13102013-2332-home.tar.gz–paralerme-
lhor,imagineoseguinteformato: 13/10/2013-23:32 .Façaumtestecomo
comando dateevejasuasaídapadrão;emseguida,rodeomesmocomandocom
aformataçãoquepassamosnoscriptdebackup:
111

## Página 119

10.7. Personalizandooseushell:PS1,PATHeoutros CasadoCódigo
daniel@casadocodigo:~$ date
Sun Oct 13 23:38:09 UTC 2013
daniel@casadocodigo:~$ date +%d%m%Y-%H%M
13102013-2338
daniel@casadocodigo:~$
Agoraquetemosonossoscriptdebackup,podemoscriarumatarefa cronpara
queelesejaexecutadoacada5minutos,porexemplo.Vamoscriaroagendamento
nacontadonossousuário,paraissousaremoso crontab:
daniel@casadocodigo:~$ crontab -e -u daniel
Editeoarquivonaúltimalinhaealtereatarefaquecriamosanteriormentepara:
*/5 * * * * /home/daniel/backup.sh
Estamosinformandoao crontabparaexecutaronossoscript backup.sha
cada5minutos.
Sevocêquiserpraticarmais,vocêpodecriarumscriptquefazobackupdeum
determinadobancodedadosdoMySQL.Paraisso,utilizeocomando mysqldump,
queéinstaladojuntocomopacotedoMySQL.
10.7 Personalizando o seu shell:PS1,PATH e outros
O shellpodesertotalmentepersonalizado,podemosalteraropromptdeco-
mando,esquemadecores,automatizaç ãodeprocessosemuitomais.Veremosagora
obásicoparacustomizá-lo.
Umpoucosobrevariáveis
SendoShellScriptumalinguagemdeprogramaç ãoparaoambiente shell,
temosrecursosdalinguagemdisponíveisporpadrãoparapersonalizar.Lembradas
variáveisemShellScript?Elaspodemsercriadaseacessadasdiretamentenoconsole:
daniel@casadocodigo:~$ NOME="Daniel Romero"
daniel@casadocodigo:~$ echo $NOME
Daniel Romero
daniel@casadocodigo:~$
Comovocêviuanteriormente,emShellScript,aocriarumavariávelépossí-
velteracessoaoseuconteúdoarmazenadofazendousodooperador( $)–como
acabamosdever,issofuncionadiretamenteno shell.
112

## Página 120

CasadoCódigo Capítulo10. IntroduçãoaShellScript
Éimportantesaberqueexistemvariáveislocaiseglobais,sendoqueasvariáveis
locaissãorestritasaumescopodefinidoeasglobaisficamdisponíveisparatodoo
sistema. Estasúltimassãobastanteconhecidasporvariáveisdeambiente. Adife-
rençaentreelasestánacriaç ão:
VARIAVEL_LOCAL="valor"
export VARIAVEL_GLOBAL="valor"
Paradefinirumavariávellocal,sóprecisamosatribuirumvaloraonomedava-
riável. Paradefinirumavariáveldeambiente,énecessáriofazerusodocomando
exportantesdesuadefiniç ão.
Esteconceitodevariáveiséimportantepoiséatravésdelasquedefinimosaforma
comoo shelleoutrosaplicativosirãosecomportar.
Umexemplodevariávelglobaléa PS1,queéresponsávelporguardarascon-
figuraçõesdopromptdecomandos. Essasconfiguraçõesapresentamosdadosdo
computador,nomedeusuário,diretórios.Porexemplo,quandoestamosno shell
temososeguinte: daniel@casadocodigo:~$.Estainformaç ãoécriadaeman-
tidanavariável PS1,vamosveroqueestáarmazenadonela:
daniel@casadocodigo:~$ echo $PS1
\[\e]0;\u@\h: \w\a\]${debian_chroot:+($debian_chroot)}\u@\h:\w\$
daniel@casadocodigo:~$
Essescódigosarmazenadosem PS1équedefinemaformadoprompt.Podemos
alterarissoanossogosto,masantesvamosconhecermaisdetalhessobreo shell
paraemseguidamodificá-lo.
Umaoutravariáveldesistemamuitoimportanteéo PATH,quearmazenaos
caminhosabsolutosdearquivosbinários(executáveis)deaplicativos. Elespodem
serchamadossemanecessidadedeinformarmosocaminhocompleto.
daniel@casadocodigo:~$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games
daniel@casadocodigo:~$
Paramelhorentender,busqueocaminhoabsolutodo vim.Paraisso,utilizeo
comando whereis:
daniel@casadocodigo:~$ whereis vim
vim: /usr/bin/vim /usr/bin/vim.basic /usr/bin/vim.tiny
/etc/vim /usr/bin/X11/vim /usr/bin/X11/vim.basic
113

## Página 121

10.8. Alias CasadoCódigo
/usr/bin/X11/vim.tiny /usr/share/vim
/usr/share/man/man1/vim.1.gz
daniel@casadocodigo:~$
Comoo $PATHarmazenaotrajeto /usr/bin,nãoprecisamosinformaroca-
minhointeiroaoexecutaroaplicativo vim,queseria /usr/bin/vim.Istoserve
parapraticamentequasetodososaplicativos.Podemaparecercasosemquesejane-
cessárioalterarovalordavariável PATH,oquepodeserfeitoem /etc/profile
oudemaneiramaisorganizadaseparandoporscriptsem /etc/profile.d.
10.8 Alias
Outrorecursoqueusaremosbastanteéo alias,quecriaumapelidoparauma
determinadainstrução.Suasintaxeéparecidacomadefiniç ãodeumavariável.
Vamosveralistade aliasqueexistedefinidanosistema:
daniel@casadocodigo:~$ alias
alias egrep= 'egrep --color=auto'
alias fgrep= 'fgrep --color=auto'
alias grep= 'grep --color=auto'
alias l='ls -CF '
alias la='ls -A '
alias ll='ls -alF '
alias ls='ls --color=auto '
daniel@casadocodigo:~$
Percebaqueadeclaraç ãoéamesmadeumavariável,sendoqueocomando
aliaséutilizadoantes. Esterecursoébastanteútilparanãotermosquerepetir
comandosgrandesquerecebemparâmetros. Porexemplo,tomeocomando ls
--color=autoqueativaumesquemadecoresparaexibiroconteúdolistadode
formamaisagradável.Notequeo aliasparaocomando lsrecebecomoargu-
mentoocomando ls --color=auto,assim,semprequefizermosusodo ls,ele
jávaiexibirasaídaemcores.
Podemoscriaronossopróprio alias,porexemplo,paraocomando clear.
Emvezdedigitarmoso clearparalimparobufferdoterminal,podemosterum
apelidochamado cl.Paraisso,faç a:
daniel@casadocodigo:~$ alias cl='clear'
daniel@casadocodigo:~$
114

## Página 122

CasadoCódigo Capítulo10. IntroduçãoaShellScript
Agorapodemosexecutarocomando clearchamandopeloseuapelido cl.
Nesteexemplo,o clsóvaiexistirenquantoestasessãodo shellestiveraberta.
Veremosmaisadiantecomotornaresseapelidofixoassimcomoosdemaisexisten-
tes.
10.9 Arquivos de configuração
Quandonoslogamosnosistemaeabrimosum shell,esseshellédelogininterativo
eexecutaváriasinstruçõesdeconfiguraçõespara,porexemplo,customizaro bash
oudisponibilizarumnovo alias.
Porpadrão,aologarno shell,elevaileroarquivo /etc/profileeexecutá-
lo,aplicandoasconfiguraçõesparatodososusuáriosdosistema.Nasequência,após
lero /etc/profile,irábuscarporumdosseguintesarquivos,napasta homedo
usuário:
•~/.profile
•~/.bash_profile
•~/.login
•~/.bashrc
Casoumscriptsejaexecutadoenasuaprogramaç ãoelefaç ausodo bash,ele
iráapenasexecutaro ~/.bashrc,jáqueduranteessachamadanãosetratadeuma
shellefetuandoumaoperaçãodelogin.
Paraentendermelhor,vamoscriarum aliasedefini-loparasercarregadologo
quechamamosum shell.Noexemplo,vamossetarumnovo aliasapenaspara
ousuário daniel.Paraisso,precisamoseditaroarquivo .bashrcqueexistena
pasta homedonossousuário:
daniel@casadocodigo:~$ vim .bashrc
Observeasváriasconfiguraçõesnestearquivo,vamoseditá-loseguindoasua
organização. Existeumamarcaçãoespecíficaparainseriraliases,vamosinseriro
nosso aliasnessegrupo:
# some more ls aliases
alias ll='ls -alF '
115

## Página 123

10.9. Arquivosdeconfiguração CasadoCódigo
alias la= 'ls -A '
alias l= 'ls -CF '
alias cl= 'clear' # <--- Nosso novo alias
Salveoarquivoesaiadoeditor. Agoratesteoseunovoaliaseexecuteasua
chamada:
daniel@casadocodigo:~$ cl
The program 'cl' is currently not installed.
You can install it by typing:
sudo apt-get install cl-launch
daniel@casadocodigo:~$
Oqueaconteceu?Porquefalhou?Nóscriamoso aliasnoarquivocertopo-
rémaindanãoinformamosao shellqueeledeveleroscript .bashrceaplicar
anovaconfiguraç ão.Podemosresolverissode2formas,aprimeiraébemsimples:
encerreoterminaleabraumnovo.Asegundamaneiraémaisinteressante,nãopre-
cisamosencerraronossoterminal:paraaplicaranovaconfiguraç ãovamosutilizar
ocomando sourcequeiráinterpretaroscripteaplicaranovaconfiguraç ãona
sessão shellquejáestáaberta.Paraisso,faç a:
daniel@casadocodigo:~$ source .bashrc
daniel@casadocodigo:~$
Emseguida,rodeocomando clnovamenteevejaquetudofunciona.
Alémdo .bashrcnodiretório homedonossousuárioaindapodemosencon-
trarmais2arquivosdeconfiguraç ão:
daniel@casadocodigo:~$ ls .b*
.bash_history .bash_logout .bashrc
daniel@casadocodigo:~$
O .bash_historyarmazenatudooquefoidigitadono shell.Essearquivo
élidopelocomando historycomojávimosanteriormente.Jáo .bash_logout
executainstruçõeslogoquesaímosdo shell,porexemplo,aorodarocomando
exiteefetuarologout,essescriptseráexecutado.
116

## Página 124

Capítulo11
Compilandoarquivosfonte
Compilarourecompilarumsoftwareapartirdocódigofonteénecessáriosempre
queprecisamosalteraralgumaconfiguraç ãoespecíficaquenãoveiodisponívelna
suaversãopré-compilada,porexemplo,quandoinstalamosvia apt. Alémdisso,
acompilaçãoébastanteutilizadaparaaplicaratualizaçõesdeseguran çaehabilitar
novasfuncionalidadesnosoftware.
Nestecapítulo,veremosobásicodecompilaç ão.Vamosinstalaropacotedalin-
guagemdeprogramaç ão rubyfazendoalgumasalteraçõesduranteacompilaç ão,
eentendercomofuncionaesseprocesso.Algumasvezeselepodesermaiscompli-
cado,àsvezesmenos. Dependemuitodecomoosdesenvolvedoresprepararamo
pacote.
11.1 Aconfiguração
Semprequevamosinstalarumsoftwareapartirdoseucódigofonte,veremosum
arquivochamado configure.Eleé,naverdade,umaplicativoque,aoserexecu-

## Página 125

11.2. Compilandonaprática CasadoCódigo
tado,verificanosistemaseexistemtodasasdependênciasnecessáriasparacompilar
osoftwareemquestão.
Oaplicativo configuredisponibilizaaop ção help,queexibeumalistade
opçõesquepodeserutilizadanoprocessodecompilaç ão.Essasop çõesincluemas
funcionalidadesdosoftwarequepodemserhabilitadasounão.
Apósaexecuç ãodo configure,seforconcluídocomsucesso,eleirágeraro
arquivo Makefilequeveremosaseguir.
Oarquivo Makefileéresponsávelporautomatizaroprocessodecompilaç ão,
alémdefazeraverificaç ãoparatercertezadequenadafaltoueporfimàinstalaç ão
dosoftware.
11.2 Compilando na prática
Paracome çar,vamosfazerodownloaddocódigofontedo ruby.Paraisso,usaremos
umcomandoqueaindanãovimos,o wget.
O wgetéumaplicativo shellparaexecutartarefasdedownloadmuitopo-
derosoetemváriaspossibilidadesdeuso.Faç aodownloaddo rubyexecutandoo
comando:
daniel@casadocodigo:~$ wget -c \
> http://cache.ruby-lang.org/pub/ruby/2.0/ruby-2.0.0-p247.tar.gz
Aop ção -cdocomando wgetéparacontinuarodownloaddeondeparoucaso
elesejainterrompido.Ousoda \foiapenasparaformatarocomandonoterminal.
Após concluir o download, descompacte o arquivo para o diretório
/usr/local.Énelequeiremoscompilaro ruby:
daniel@casadocodigo:~$ sudo tar zxvf ruby-2.0.0-p247.tar.gz -C
/usr/local
Lembre-sedequeaop ção -Cdocomando tarserveparaindicarmosodire-
tóriodestinoaodescompactaroarquivo. Apósdescompactar,vamosaodiretório
ondeestáocódigofontedo ruby:
daniel@casadocodigo:~$ cd /usr/local/ruby-2.0.0-p247/
daniel@casadocodigo:/usr/local/ruby-2.0.0-p247$ ls
addr2line.c inits.c regexec.c
addr2line.h insns.def regint.h
array.c insns.inc regparse.c
118

## Página 126

CasadoCódigo Capítulo11. Compilandoarquivosfonte
bcc32 insns_info.inc regparse.h
benchmark internal.h regsyntax.c
bignum.c io.c revision.h
bin iseq.c ruby_atomic.h
bootstraptest iseq.h ruby.c
BSDL KNOWNBUGS.rb safe.c
ChangeLog known_errors.inc sample
class.c LEGAL signal.c
...
daniel@casadocodigo:/usr/local/ruby-2.0.0-p247$
Podemosverquenodiretóriodocódigofonteexistebastantecoisa!Aprimeira
coisaafazernessemomentoélerosarquivos READMEe INSTALL.Dependendo
dodesenvolvedordosoftware,elepodedisponibilizarapenasumdosarquivos–no
nossocaso,existeo READMEcominformaçõessobreosoftwareeprocedimentosde
instalação.
Prosseguindo,vamosaoaplicativo configureverasop çõesdecompilaç ão:
daniel@casadocodigo:/usr/local/ruby-2.0.0-p247$ ./configure --help
A quantidade de opções para o processo de compilação realmente é muito
grande. Escolheremosapenasalgumas: vamosdesabilitarainstalaç ãodosuporte
dalinguagem rubyparacomunicaçãocomalinguagem Cevamosdesabilitartam-
bémainstalaçãodadocumentaç ão rdocdalinguagem ruby:
daniel@casadocodigo:/usr/local/ruby-2.0.0-p247$ sudo ./configure \
> --disable-install-capi --disable-install-rdoc
Maisumavezestamosusando \apenasparaformataçãono shell.Ocomando
podeserinseridointeiroemumaúnicalinha.Asduasop çõesescolhidasparadesa-
bilitarnoexemplosãoapenasparailustrarousodoprocessodecompilaç ão.
Após rodar o aplicativoconfigure, receberemos a seguinte mensagem
nofinal: config.status: creating Makefile, indicandoqueoarquivo
Makefilefoicriado. Agorapodemosirparaapróximaetapaecompilarosoft-
ware:
daniel@casadocodigo:/usr/local/ruby-2.0.0-p247$ sudo make
Paracompilar,usamosocomando make,queirábasicamenteleroarquivo
Makefilecomasinstruçõesdecompilaç ãoeexecutarcadaetapa.Oprocessode
119

## Página 127

11.2. Compilandonaprática CasadoCódigo
compilaçãopodedemorarumpouco.Nesteexemploacompilaç ãopodelevarentre
1e3minutos,dependendodoseuhardware.
Apósconcluir,senãohouvenenhumamensagemdeerrogeradapelocomando
make,podemosfinalizarexecutandoainstalaç ão:
daniel@casadocodigo:/usr/local/ruby-2.0.0-p247$ sudo make install
Afun çãodo make install éessencialmentemoveralgunsarquivosqueforam
compiladosparaosseusdevidoslugarese,assim,efetivarainstalaç ão.Durantetodas
essasetapasforamgeradosalgunsarquivosbináriosqueservemdeauxíliodurante
acompilação. Agoraessesarquivospodemserremovidos,eparaissouseaop ção
cleandocomando make:
daniel@casadocodigo:/usr/local/ruby-2.0.0-p247$ sudo make clean
Retorneparaodiretório homedoseuusuárioetesteparaverseoaplicativofoi
instaladocomsucesso:
daniel@casadocodigo:/usr/local/ruby-2.0.0-p247$ cd
daniel@casadocodigo:~$ ruby -v
ruby 2.0.0p247 (2013-06-27 revision 41674) [i686-linux]
daniel@casadocodigo:~$
Executando ruby -v,sevocêrecebeuamensageminformandoaversãodo
rubyqueinstalamos,significaquetudofoiexecutadocorretamente.
Comoo rubypoderiaserinstaladorapidamentevia apt,podemosremover
anossainstalaç ãoexecutandoaop ção uninstalldocomando make.Paraisso
vamosvoltarparaodiretórioondeseencontraocódigofontedainstalaç ão:
daniel@casadocodigo:~$ cd -
/usr/local/ruby-2.0.0-p247
daniel@casadocodigo:/usr/local/ruby-2.0.0-p247$ sudo make uninstall
make: *** No rule to make target `uninstall`. Stop.
daniel@casadocodigo:/usr/local/ruby-2.0.0-p247$
Masoqueaconteceu?Nãofoipossíveldesinstalarpoisocriadordosoftwarenão
disponibilizouaop ção uninstallparao make.Masaindatemosduasformaspara
desinstalar.
Aprimeiraformaémaistrabalhosa,teríamosquelocalizarosdiretóriosondeo
rubyfoiinstaladonosistema.Poderíamosusarocomando whereis:
120

## Página 128

CasadoCódigo Capítulo11. Compilandoarquivosfonte
daniel@casadocodigo:/usr/local/ruby-2.0.0-p247$ whereis ruby
ruby: /usr/local/bin/ruby /usr/local/lib/ruby
daniel@casadocodigo:/usr/local/ruby-2.0.0-p247$
Esabendoagoraondeestãoosarquivosdainstalaç ãodo rubynosistema,te-
ríamosqueremovermanualmente,masissoémuitotrabalho. Podemosutilizaro
shellcommaissabedoriaeremovertudodeumavez.
Ao realizar a instalação, o make gerou um arquivo oculto chamado
.installed.list,noqualestáexatamenteaestruturadosdiretóriosearquivos
queforaminstaladosduranteoprocessodecompilaç ão:
daniel@casadocodigo:/usr/local/ruby-2.0.0-p247$ cat .installed.list
/usr/local/bin/
/usr/local/bin/ruby
/usr/local/lib/
/usr/local/lib/libruby-static.a
/usr/local/lib/ruby/2.0.0/i686-linux/
/usr/local/lib/ruby/2.0.0/i686-linux/rbconfig.rb
/usr/local/lib/pkgconfig/
/usr/local/lib/pkgconfig/ruby-2.0.pc
/usr/local/bin/testrb
/usr/local/bin/ri
...
Agoraquetemosalistadosarquivoscomosrespectivoscaminhosabsolutos
podemosmontarumainstruç ãodeumaúnicalinhapararemovertodosdosistema
–paraissousaremoso xargs. Basicamente,oqueo xargsfazécombinaro
parâmetroinicialcomosargumentosrecebidosdaentradapadrão,edessaforma
eleexecutaocomandoordenadoumaoumaisvezes.
Para remover os arquivos da instalaç ão que estão listados em
.installed.listusaremoso catparaler,o rmpararemovereo xargspara
fazê-lossecomunicarem:
daniel@casadocodigo:/usr/local/ruby-2.0.0-p247$ cat .installed.list |
xargs sudo rm
Nãosepreocupecomasmensagensdealertadestainstruç ãopoisestamosre-
movendoapenasosarquivosenãoosdiretórios.Testeagoraocomando ruby -v
evejaquenãoestámaisinstaladonosistema:
121

## Página 129

11.2. Compilandonaprática CasadoCódigo
daniel@casadocodigo:/usr/local/ruby-2.0.0-p247$ cd
daniel@casadocodigo:~$ ruby -v
bash: /usr/local/bin/ruby: No such file or directory
daniel@casadocodigo:~$
Lembre-sesempredelero READMEou INSTALLdosprogramasqueforinstalar
pelocódigofonte!
Jáestápreparadoparamaispacotes?Procureebaixeopacote nmap,queserve
paraescaneararedeparaseguran ça,etentecompilá-loeinstalá-lo,seguindopassos
análogosaosjávistosaqui.
122

## Página 130

Capítulo12
Oqueestudaralém?
AgoraquevocêjásefamiliarizoucomoLinux,estánahoradepartirembuscade
maisconhecimentoseavan çarnosestudos. Selecioneialgumasdicasinteressantes
paraquevocêprossigacomoaprendizado!
12.1 SSH–SecureShell
SSH(SecureShell)éumprotocoloqueestabeleceumcanaldecomunicaç ãoseguro
entredoiscomputadorespormeiodecriptografiaecodificaç ãodemensagensde
autenticação.O SSHébastanteutilizadoquandoqueremosestabelecerumaconexão
commáquinasremotaseexecutarcomandosemumservidorremoto,porexemplo.
Aformamaiscomumdeutilizaç ãoé: ssh username@servidor_ip.
$ ssh daniel@192.168.25.8
The authenticity of host '192.168.25.8 (192.168.25.8)'
can't be established.

## Página 131

12.1. SSH–SecureShell CasadoCódigo
ECDSA key fingerprint is
32:53:5d:95:d9:2b:c0:92:ab:1d:a4:87:95:a6:5a:e2.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '192.168.25.8' (ECDSA) to the list of known
hosts.
daniel@192.168.25.8's password:
Welcome to Ubuntu 12.04.3 LTS (GNU/Linux 3.2.0-23-generic-pae i686)
daniel@casadocodigo:~$
Noexemplo,estabeleciumaconexãoremotaemumamaquinavirtualpassando
onomedousuárioeipcomoargumentosdocomando ssh.Duranteaconexão,o
sshsolicitaasenhadousuárioparacompletaroacessoremoto.
Imagineaseguintesituação:vocêestáemseucomputadoreprecisaacessaroutro
computadorutilizando sshviainternet.Duranteoprocessodeloginvocêinformou
asuasenha,masnomeiodocaminhotinhaalguémobservandoosseuspassos:
Figura12.1:Acessosshinseguro
Naimagemanteriorépossívelnotarqueosdadosestãodesprotegidoseque
qualquerpessoaconseguecapturareentenderasinformaçõesquetrafegamentreo
computador A eo computador B,poisasinformaçõesnãoestãocriptografadas.
124

## Página 132

CasadoCódigo Capítulo12. Oqueestudaralém?
Utilizandocriptografia,osdadosquesaemdoseucomputadorseriamtransfor-
madosemalgototalmenteincompreensívelparaqualquerpessoaquenãofosseo
destinatário.
Podemosnotarqueaindaépossívelinterceptarasinformaçõesquetrafegamen-
treo computador A eo computador B masémuitodifícilentenderoconteúdo:
Figura12.2:Acessosshseguro
Notequeagoraonossohackernãoconseguiudecifrarasinformaçõestrocadas
entreoscomputadores Ae B,graçasàcriptografia.
O SSHutilizaumsistemadecriptografiaquerequer2chaves,umachaveéco-
nhecidapor chave pública quepodeserusadapeloremetenteparacriptografar
osdadosantesdeenviá-loseaoutraéconhecidapor chave privada queéusada
paradecodificaramensagemoriginal.
Para o nosso exemplo, vamos gerar um par de chaves e garantir o nosso
acessosegurovia SSH.Nolinux, o OpenSSHtrabalhacomdoistiposdecha-
ves: DSA (Digital Signature Algorithm) e RSA (Rivest, Shamir e
Adleman),aschavesdotipo DSAsãopadronizadaspelogovernodosEUAeo
OpenSSHsócriachavesDSAcomnomáximo1024bits. Issopodeserumpro-
blemapoisseriapossíveldecodificarumachaveDSAacurtoprazo,jáaschavesRSA
125

## Página 133

12.1. SSH–SecureShell CasadoCódigo
o OpenSSHpodegerarchavescomaté4096bitsouatémaiseissoastornainque-
bráveisnaatualidade.
Utilizaremosopadrãodo OpenSSHqueédechaves RSAde2048bits.Paragerar
aschavesusaremosoaplicativo ssh-keygen:
$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/daniel/.ssh/id_rsa):
O ssh-keygenvaiperguntarondedesejamossalvaraschavesqueserãocria-
das.Porpadrãoésalvonapasta .sshna homedonossousuário,entãonestaetapa,
apenastecle Enter.
Emseguidaserásolicitadaumasenhaeaconfirmaç ãodesenhaparaageraç ão
daschaves.Porcomodidadevamosdeixarembrancoeapenasteclar Enter:
$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/daniel/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/daniel/.ssh/id_rsa.
Your public key has been saved in /home/daniel/.ssh/id_rsa.pub.
The key fingerprint is:
ce:71:1f:c2:54:b4:e6:53:bf:59:72:64:d5:be:46:a7 daniel@localhost
The key 's randomart image is:
+--[ RSA 2048 ]----+
| .o o|
| . . o|
| . o ..o|
| o o . =o|
| S + + o.*|
| o o o oE=+|
| o . .o |
| |
| |
+-----------------+
Pronto,onossopardechavesfoigerado.Paraverificarbastalistaraschaves:
126

## Página 134

CasadoCódigo Capítulo12. Oqueestudaralém?
$ ls ~/.ssh
id_rsa id_rsa.pub
Aolistarosarquivosnodiretório .sshnapastahomedonossousuáriotemos
opardechavesgeradoonde id_rsaéachaveprivadae id_rsa.pubnossachave
pública.
Agoraquejápossuímosnossopardechavesoqueprecisamosfazerélevara
nossachavepúblicaparaodestinatárioedizerparaelequeiremosestabelecerco-
municaçãocomousodechaves. Paraissoutilizaremoso scp (secure copy)
umaplicativodecópiaseguradearquivosqueutilizaosshcomocanaldeenvio:
$ scp ~/.ssh/id_rsa.pub daniel@192.168.25.8:~/chave_publica
daniel@192.168.25.8's password:
Oquefizemosfoiinformarao scpoarquivoaserenviadoeodestino,sendo
queoesseéamesmainstruç ãoqueutilizamosparaumaconexãossh.
Apósenviarnossachavepública,precisamosentrareconfigurarnoservidorpara
queomesmopasseautilizaracomunicaç ãoporchavesno ssh:
$ ssh daniel@192.168.25.8
daniel@192.168.25.8's password:
Welcome to Ubuntu 12.04.3 LTS (GNU/Linux 3.2.0-23-generic-pae i686)
daniel@casadocodigo:~$
Agoraqueentramosnoservidornovamente,sóprecisamosconfigurarparaque
eleleianossachavepública:
daniel@casadocodigo:~$ cat chave-publica >> ~/.ssh/authorized_keys
Oarquivo authorized_keyséresponsávelporautorizarquempodeounão
manteracessoaoservidorvia ssh.Agorabastaverificarseo OpenSSHestáconfi-
guradoparaaceitarloginutilizandochaves:
daniel@casadocodigo:~$ sudo grep 'PubkeyAuthentication'
/etc/ssh/sshd_config
PubkeyAuthentication yes
daniel@casadocodigo:~$ exit
Nomeucasoaop çãoestáativa.Seasaídadocomandoretornar noemvezde
yes,abraoarquivo /etc/ssh/sshd_configealterepara yes.
Agoraépossívelmanteracessoseguroviasshsemanecessidadedeinformar
senha:
127

## Página 135

12.2. Proteçãoporfirewall CasadoCódigo
$ ssh daniel@192.168.25.8
daniel@casadocodigo:~$
Pormedidasdeseguran ça,nuncareveleoconteúdodasuachaveprivada.
Paramaisdetalhes,éinteressanteolharadocumentaç ãooficialdadistribuiç ão
Linuxqueestamosusando,nocasooUbuntu: https://help.ubuntu.com/community/
SSH
12.2 Proteção por firew all
O firewalltemporobjetivoaplicarumapolíticadeseguran çapormeiodere-
grasquecontrolamofluxodeentradaesaídadedadosemumaredeeprotegeros
computadores.
NoLinux,oaplicativode firewallmaisconhecidoéo iptablesqueébas-
tantepoderosoecomplexo.NoUbuntu,existeumaferramentaqueajudanaconfi-
guraçãodo firewallreduzindoacomplexidadedo iptables:UFW(Uncom-
plicatedFirewall) http://wiki.ubuntu-br.org/UFW
Em versões futuras no Kernel Linux, oiptables será substituído por
nftableshttp://netfilter.org/projects/nftables/parareduziracomplexidadedaes-
critaderegrasqueatualmenteháno iptables.
12.3 Upstart e Monit
Lembradosscriptsdeinicializaç ãodeserviços?O upstartéumasoluçãoótima
disponíveltambémnoUbuntu. Comeleépossívelcriarscriptsdeinicializaç ãoe
controledeserviçosdeformafácilemenosdolorosa: http://upstart.ubuntu.com/
index.html.
Jáo monitéumaplicativoparagerenciamentoemonitoramentodeprocessos,
aplicativos,arquivos,diretóriosetc.Elepodeexecutaraçõesplanejadaseébastante
indicadoparamonitorarservidores.Alémdisso,elepodetrabalhardeformapare-
cidacomo cron:http://mmonit.com/monit/.
12.4 Documentações em português
Sevocênãosesentirconfortávelcommaterialeminglês,existeumavastadocumen-
taçãosobreLinuxemportuguês.
128

## Página 136

CasadoCódigo Capítulo12. Oqueestudaralém?
Oguiafoca http://www.guiafoca.org/éumadocumentaçãobastantecompleta
separadaemníveisiniciante,intermediárioeavan çado.
12.5 Tirar dúvidas
Sevocêtiveralgumadúvidasobreestelivro,junte-seàlistaem:
http://lista.infoslack.com
Eenviesuapergunta!Eueosparticipantesdogrupotentaremosajudar.
MUITOOBRIGADO!
129

## Página 137

ÍndiceRemissivo CasadoCódigo
ÍndiceRemissivo
adduser,66
alias,114
apache,81
apt,76
backup,108
bash,113
bash_profile,115
caminho,22
cat,25,42
cd,20
chmod,62,104
clear,21
compactação,47
configure,119
cp,23
cron,108
date,19,111
delete,26
diretóriocorrente, 104
diretóriorelativo,22
diretórios,19,53
echo,25,105
etc,115
find,30
grep,94
grupos,61
gzip,51
head,45
help,26
history,19
home,21,55
if,106
initd,83,107
java,78
kernel,2
kill,99
killall,100
LibreOffice,13
ln,84
ls,20
make,119
man,27
mv,23
mysql,85
nano,40
pacotes,71
PATH,104,113
permissões, 59,104
php,88
130

## Página 138

CasadoCódigo ÍndiceRemissivo
profile,24,115
ps,92
PS1,113
pwd,19
raiz,20,54
read,106
rm,26
root,58
script,103
service,83
shell,17,103
sleep,105
source,113
sudo,58
tail,45
tar,47
terminal,32
top,95
touch,23
Ubuntu,2
usuários,58
variáveis,105
vi,33
vim,33
wget,118
whereis,120
whoami,19
zip,51
131