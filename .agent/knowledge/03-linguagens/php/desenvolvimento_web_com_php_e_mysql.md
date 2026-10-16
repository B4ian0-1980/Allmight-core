---json
{
  "id": "desenvolvimento_web_com_php_e_mysql",
  "title": "Desenvolvimento web com PHP e MySQL",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "**Arquivo Original:** `Desenvolvimento web com PHP e MySQL.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "com",
    "desenvolvimento",
    "linguagens",
    "mysql",
    "php",
    "web"
  ],
  "perguntas_tipo": [
    "Como utilizar Desenvolvimento web com PHP e MySQL?",
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

# Desenvolvimento web com PHP e MySQL

> **Arquivo Original:** `Desenvolvimento web com PHP e MySQL.pdf`
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
Avidanãoéumasequênciadeacontecimentosaleatórios.Muitacoisatevequeacon-
teceremumacertaordemparaqueestelivrofossepossível,desdeumalongínqua
oportunidadedefazeroprimeirocursodeinformática,passandoporcursotécnico,
faculdade,gruposdeestudo,palestras,atéachancedetrabalharcompessoasque
mefizeramevoluir. Porissoagrade çoaDeusportermedadoasferramentaseo
discernimentonecessáriosparaencontraroscaminhosquemetrouxeramatéeste
livro.
Estelivronãoseriaumarealidadesemoapoiodaminhaamadaesposa Cássia
Luz.Quandoeufaleiparaeladaoportunidadedeescreverumlivro,eladisse você
temqueescreverumlivro! eissomemotivoubastanteaencararessatarefatão
difícil. Obrigado,Cassinha! (Eobrigadotambémpelaideiadailustraç ãodacapa,
ficoudemais!)
Agradeçotambémaosmeuspais,SilvanaeEvaldo,meusirmãos,JennereAn-
tonioPaulo,eàsra.Creuzaeaosr.Mário,tiosdaCássia,quemedesculparampor
nãocompareceraosalmo çosejantaresemfamíliaporqueestavaescrevendosómais
umpedaçodolivro.
Naverdade,eusemprequisescreverumlivrosobreprogramaç ãoeatécheguei
começaralgunsrascunhos,masacabeideixandotodosdelado. Atéqueumdiao
CaioRibeiroPereira,queestavaterminandoseulivrodeNode.js,meperguntouse
eunãoqueriaescreverumlivrodePythonemeapresentouaoPauloSilveirada
Caelum/CasadoCódigo.Depoisdissotrocamosalgunse-mailsecomeceiaescrever
estelivrodePHPeMySQL,finalmentecolocandono“papel”oquepenseiemfazer
pormuitotempo.Obrigado,Caio!Eobrigado,Paulo!
AgradeçotambémaosmeusalunosdaUnimontequepacientementeaguarda-
ramosquaseseismesesdeescritadestelivro.Nãofaleiparavocêsqueeuterminaria
logo?
Obrigadotambémaopessoalqueleualgunsrascunhosemedeuideiasdoque
i

## Página 6

CasadoCódigo
poderiaserabordado.
NãopossoesquecerdopessoaldoGCCSDquefoibastanteincentivadorquando
euaindadavapassospequenosemTI.
ii

## Página 7

CasadoCódigo
Sobreoautor
EvaldoJuniorBentotrabalhacomTIdesde2004. Édesenvolvedorwebcomfoco
emboaspráticasepadrõesdedesenvolvimentoutilizandoPHPcomosuaprincipal
linguagemdesde2008.Éprofessoruniversitário,ministrandodisciplinasrelaciona-
dasadesenvolvimentodesoftwareetambémpalestranteemeventosrelacionadosa
softwarelivreedesenvolvimentodesoftware. Possuiformaç ãoemProcessamento
deDadospelaFatecePósGraduaç ãoemGestãoEstratégicadeTI.Mantémumblog
sobredesenvolvimentoetecnologiaem http://evaldojunior.com.br/blog/eprojetos
opensourcenoGitHubem https://github.com/InFog.
iii

## Página 9

CasadoCódigo
Prefácio
MuitagentequepensaemWeblembralogodeHTML,CSSeJavaScript. Claro,
sãoaslinguagensfundamentaisdosnavegadores. Maselassócontammetadeda
história.Muitacoisaprecisaacontecerdooutroladodaconexão,nosservidores.E,
sevocêquerprogramarseriamentenaWeb,vaiprecisardominarumalinguagemde
programaçãoquerodenoservidor.
Nessecenário,oPHPéamelhorescolhasevocêquerevoluirsuaspáginases-
táticasHTMLparapáginasdinâmicasesistemascomplexos.Hámuitasop çõesde
linguagensdeprogramaçãoedebancosdedados,masaduplaPHPeMySQLédas
maisimportantesnomercadoWebatual,comaplicaçõesemsitesdeconteúdo,co-
mércioeletrônicoeatésistemasgrandescomoFacebook.
Esselivroéobrigatórioparaquemquercome çarcomPHPeMySQL.OEvaldo
éumexcelenteautorcomgrandeexperiência,econseguiuchegaremumlivrofácil
delereacompanhar,comumaescritadinâmicaevibrante.Segueomodelodelivros
objetivosdaCasadoCódigoefarávocêentrarnessemercadorapidamenteecom
bastanteconhecimento.
Umaboaleitura,bonsestudosebem-vindoaoimensoeimportantemundodo
PHP.
SérgioLopes
—InstrutoredesenvolvedornaCaelum,autordolivro“AWebMobile”também
daeditoraCasadoCódigo
http://sergiolopes.org
v

## Página 11

CasadoCódigo Sumário
Sumário
1 Introdução 1
1.1 Ganhandoaweb2.0compáginasdinâmicas . . . . . . . . . . . . . . 1
1.2 Onavegadoreaexibiç ãodepáginaswebestáticas . . . . . . . . . . . 2
1.3 Ecomofuncionaumapáginadinâmica? . . . . . . . . . . . . . . . . . 2
1.4 EondeentraoPHPeoMySQL? . . . . . . . . . . . . . . . . . . . . . . 3
1.5 Mas,porqueescolherPHPeMySQL? . . . . . . . . . . . . . . . . . . 3
1.6 Oquevouprecisarparaacompanharestelivro? . . . . . . . . . . . . . 3
1.7 Sobreestelivro . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
2 OprimeiroprogramaemPHP 7
2.1 InstalandooPHP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.2 PHPnoLinux . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.3 Evamosaoprimeiroprograma! . . . . . . . . . . . . . . . . . . . . . . 14
2.4 Aminhapáginaestámostrandoahoraerrada! . . . . . . . . . . . . . 15
2.5 Resumo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
2.6 Desafios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
3 ConstruindoumcalendáriocomPHP 19
3.1 Definindonossocalendário . . . . . . . . . . . . . . . . . . . . . . . . 19
3.2 Come çandoocalendário . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3.3 Usandofun ções . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
3.4 Entendendoeseentendendocomoserros . . . . . . . . . . . . . . . . 26
3.5 MeuPHPnãomostrouoserros! . . . . . . . . . . . . . . . . . . . . . . 27
3.6 Finalizandoocalendário . . . . . . . . . . . . . . . . . . . . . . . . . . 28
3.7 Resumo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
3.8 Desafios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
vii

## Página 12

Sumário CasadoCódigo
4 Entradadedadoscomformulário 31
4.1 Definindoalistadetarefas . . . . . . . . . . . . . . . . . . . . . . . . . 31
4.2 Oformuláriodecadastrodetarefas . . . . . . . . . . . . . . . . . . . . 32
4.3 Entradadedados . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
4.4 PegandoosdadosdaURL . . . . . . . . . . . . . . . . . . . . . . . . . 34
4.5 SessõesnoPHP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
4.6 Resumo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
4.7 Desafios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
5 Tratamentodediferentescamposdeformulários 43
5.1 Organizandoocódigoemarquivosseparados . . . . . . . . . . . . . . 44
5.2 Adicionandomaisinformaçõesàstarefas . . . . . . . . . . . . . . . . 46
5.3 Conclusãodocapítuloedousodesessões . . . . . . . . . . . . . . . . 50
5.4 Resumo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
5.5 Desafios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
6 Acessandoeusandoumbancodedados 53
6.1 ObancodedadosMySQL . . . . . . . . . . . . . . . . . . . . . . . . . 54
6.2 InstalandooMySQL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
6.3 PHPMyAdmin,administrandoobancodedados . . . . . . . . . . . . 55
6.4 Criandoobancodedados . . . . . . . . . . . . . . . . . . . . . . . . . 57
6.5 Criandoatabela . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
6.6 Cadastrandoelendoosdadosdeumatabela . . . . . . . . . . . . . . 61
6.7 FiltrandoosresultadosdoSELECT . . . . . . . . . . . . . . . . . . . . 62
6.8 Resumo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
6.9 Desafios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
7 IntegrandoPHPcomMySQL 65
7.1 PHPeMySQL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
7.2 ConectandoaoMySQL . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
7.3 Buscandodadosnobanco . . . . . . . . . . . . . . . . . . . . . . . . . 68
7.4 Cadastrandoastarefasnobanco . . . . . . . . . . . . . . . . . . . . . . 72
7.5 Cadastrandooprazodasatividades . . . . . . . . . . . . . . . . . . . . 77
7.6 Marcandoumatarefacomoconcluída . . . . . . . . . . . . . . . . . . 81
7.7 Resumo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84
7.8 Desafios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84
viii

## Página 13

CasadoCódigo Sumário
8 Edi çãoeremo çãoderegistros 85
8.1 Ediçãodetarefas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
8.2 Remo çãodetarefas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
8.3 Evitandooproblemacomaatualizaç ãodepágina . . . . . . . . . . .100
8.4 Resumo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
8.5 Desafios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
9 Validaçãodeformulários 103
9.1 Validaçãonalistadetarefas . . . . . . . . . . . . . . . . . . . . . . . . 103
9.2 EntradadedadosusandoPOST . . . . . . . . . . . . . . . . . . . . . . 104
9.3 Validandoonomedatarefa . . . . . . . . . . . . . . . . . . . . . . . . 106
9.4 Adicionandooavisodeerro . . . . . . . . . . . . . . . . . . . . . . . . 110
9.5 Validandoadatadigitada . . . . . . . . . . . . . . . . . . . . . . . . . . 114
9.6 Expressõesregulares . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
9.7 Validandooformuláriodeediç ãodetarefas . . . . . . . . . . . . . . . 121
9.8 Resumo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
9.9 Desafios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
10 Uploaddearquivos 127
10.1 Anexosparaalistadetarefas . . . . . . . . . . . . . . . . . . . . . . . . 127
10.2 Mudançasnobancodedados . . . . . . . . . . . . . . . . . . . . . . . 128
10.3 Páginacomosdetalhesdastarefas . . . . . . . . . . . . . . . . . . . . 130
10.4 Oformulárioparacadastraranexos . . . . . . . . . . . . . . . . . . . . 132
10.5 RecebendoarquivospeloPHP . . . . . . . . . . . . . . . . . . . . . . . 134
10.6 Gravandoosdadosdoanexonobancodados . . . . . . . . . . . . . . 138
10.7 Exibindoosanexos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139
10.8 Resumo. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
10.9 Desafios. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
11 Lembretesdetarefaspore-mail 143
11.1 Definindooe-maildeaviso . . . . . . . . . . . . . . . . . . . . . . . . 143
11.2 Unificandoaconfiguraçãodaaplicaç ãocomconstantes . . . . . . . . 145
11.3 Adicionandoaop çãodeavisopore-mail . . . . . . . . . . . . . . . . . 147
11.4 Afunçãoenviar_email() . . . . . . . . . . . . . . . . . . . . . . . . . . 149
11.5 Escrevendoocorpodoe-mailusandoumarquivocomotemplate . . 151
ix

## Página 14

Sumário CasadoCódigo
11.6 Instalandoumabibliotecaparaenviare-mails . . . . . . . . . . . . . . 154
11.7 Finalizandoafun çãoenviar_email() . . . . . . . . . . . . . . . . . . . 155
11.8 Resumo. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 160
11.9 Desafios. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 160
12 HospedagemdeaplicaçõesPHP 161
12.1 Suaaplicaçãoparaomundo! . . . . . . . . . . . . . . . . . . . . . . . . 161
12.2 Escolhendoumservidorparahospedagem . . . . . . . . . . . . . . . 162
12.3 HospedagemcomaHostinger . . . . . . . . . . . . . . . . . . . . . . . 162
12.4 CriaçãodacontanaHostinger . . . . . . . . . . . . . . . . . . . . . . . 163
12.5 ConfigurandoaaplicaçãoparaaHostinger . . . . . . . . . . . . . . . 170
12.6 EnviandoaaplicaçãoparaaHostinger . . . . . . . . . . . . . . . . . . 170
12.7 HospedagemnoJelasticdaLocaweb . . . . . . . . . . . . . . . . . . . 173
12.8 CriaçãodacontanoJelasticdaLocaweb . . . . . . . . . . . . . . . . . 173
12.9 ConfigurandoaaplicaçãoparaoJelastic . . . . . . . . . . . . . . . . . 179
12.10 EnviandoaaplicaçãoparaoJelastic . . . . . . . . . . . . . . . . . . . . 180
12.11 Resumo. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 182
12.12 Desafios. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 182
13 Programandocomorientaçãoaobjetos 183
13.1 AclasseTarefas. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 184
13.2 Buscandotarefasdentrodaclasse . . . . . . . . . . . . . . . . . . . . . 185
13.3 Buscandoapenasumatarefadentrodaclasse . . . . . . . . . . . . . . 187
13.4 Gravandoeeditandotarefasdentrodaclasse . . . . . . . . . . . . . . 189
13.5 UsandooMySQLiorientadoaobjetos . . . . . . . . . . . . . . . . . . 191
13.6 Avançandoemorientaçãoaobjetos . . . . . . . . . . . . . . . . . . . . 195
13.7 MVCeFrameworks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 195
13.8 Resumo. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 197
13.9 Desafios. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 197
14 Proteçãoeajustes 199
14.1 Protegendo-secontraSQLInjection . . . . . . . . . . . . . . . . . . . .200
14.2 Exibindocamposcomaspas . . . . . . . . . . . . . . . . . . . . . . . . 201
14.3 Resumo. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .202
14.4 Desafios. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .202
x

## Página 15

CasadoCódigo Sumário
15 Aoinfinito...Ealém! 203
15.1 Ondepossobuscarmaisinformações? . . . . . . . . . . . . . . . . . . 203
xi

## Página 17

Capítulo1
Introdução
1.1 Ganhando a web 2.0 com páginas dinâmicas
Imagineainternetnaqualvocêpodeapenasconsumirconteúdos,comosefosseum
jornal,umarevista,ouainda,umprogramanatelevisão. Chato,né? Masquando
seaprendeaslinguagensdaweb,comoHTMLeCSS,éissoqueseaprende,pois
usandoapenasHTMLpodemosmontarsitesquesãocomorevistaseservemapenas
paraleitura,sempermitirinteraç ãocomosinternautas.
Osegredodafamosa web2.0 éacapacidadedeinteraç ãoentreaspessoaseos
serviçosonline.Mas,paraqueestainteraç ãosejapossível,énecessárioqueossites
sejamcapazesdereceberinformaçõesdosinternautasetambémdeexibirconteúdos
personalizadosparacadaumoudemudarseuconteúdoautomaticamente,semque
odesenvolvedorprecisecriarumnovoHTMLparaisso.
Estesdoistiposdesitessãochamadosdeestáticoedinâmico,respectivamente.

## Página 18

1.2. Onavegadoreaexibiçãodepáginaswebestáticas CasadoCódigo
1.2 O navegador e a exibição de páginas web estáti-
cas
Vocêjáparouparapensaremtudooqueacontecequandovocêdigitaumendere ço
emseunavegadorweb?Ahistóriatodaémaisoumenosassim:
• Onavegadorvaiatéoservidorquerespondenoendereçosolicitadoepedea
páginasolicitada.
• Oservidorverificaseoendereçoexisteeseapáginatambémexisteemseu
sistemadearquivoseentãoretornaoarquivoparaonavegador.
• ApósreceberoarquivoHTML,onavegadorcomeçaotrabalhoderenderiza-
ção,paraexibirapáginaparaousuário. Énestemomentoqueonavegador
tambémrequisitaarquivosdeestilos(css),imagenseoutrosarquivosneces-
sáriosparaaexibiçãodapágina.
Quandosedesenvolvepáginasestáticas,esteébasicamentetodooprocessone-
cessárioparaqueonavegadorexibaapáginaparaousuário.Chamamosde estáticas
aspáginaswebquenãomudamseuconteúdo,mesmoemumanovarequisiç ãoao
servidor.
1.3 E como funciona uma página dinâmica?
Oprocessoparapáginasdinâmicasémuitoparecidocomodaspáginasestáticas.
Adiferen çaéqueapáginaseráprocessadanoservidorantesdeserenviadapara
ousuário. Esteprocessamentonoservidoréusadoparaalterardinamicamenteo
conteúdodeumapágina,sejaeleHTML,CSS,imagensououtrosformatos.
Pense,porexemplo,emumsitedeumjornal.Emgeral,estetipodesitecontém
algumasáreasdestinadasàsnotíciasdedestaque,outrasáreasparanotíciasgerais
eaindaoutrasáreasparaoutrosfins.Quandoonavegadorsolicitaapáginaparao
servidor,eleirámontaroconteúdoantesdeenviarparaonavegador.Esteconteúdo
podeserconseguidodealgumasfontes,masamaiscomuméumbancodedados,
onde,nestecaso,asnotíciasficamarmazenadasparaseremexibidasnaspáginas
quandonecessário.
2

## Página 19

CasadoCódigo Capítulo1. Introdução
1.4 E onde entra o PHP e oMySQL?
PHPéumaferramentaquepossibilitaopré-processamentodepáginasHTML.
Dessaforma,PHPconseguealteraroconteúdodeumapágina,antesdeenviá-la
paraonavegador.Alémdisso,PHPtambémpermitecapturarentradasdedadosdo
usuário,comoformulárioseoutrasformasdeinteraç ão.
JáoMySQLéobancodedadosnoqualguardamosinformaçõesemestruturas
noestilodetabelas,sendoquecadalinhadatabelaéumnovoregistro.Éembancos
comooMySQLqueossitesdenotícias,redessociaisetc.,guardamsuasinformações
paraquedepoissejamrecuperadaseexibidasnaspáginas.
AduplaPHPeMySQLseconhecehámuitosanosetrabalhabememequipe.
1.5 Mas, por que escolherPHP eMySQL?
Háalgunsdias,aofinaldeumaaulanafaculdade,umalunoveioatémimeper-
guntouporqueasempresasescolhemPHPeMySQLparadesenvolverseussitese
atémesmoseussistemas.ElemedissequeexistemlinguagenssuperioresaoPHPe
bancosquesãotidoscomomelhoresqueoMySQL.
Responderaestaquestãonãoéfácil,poisexistemdiversosmotivosparaescolher
estaouaquelatecnologia.NocasodaduplaPHPeMySQL,algunsmotivossão:
• PHPnasceuparaawebesuaintegraçãocomservidoreswebésimples.
• PHPtemumacurvadeaprendizadosuave,comparadaaoutraslinguagens.
• PHPeMySQLsãotecnologiaslivres.
• ÉfácilencontrarserviçosdehospedagemqueoferecemPHPeMySQL.
• ServiçosdehospedagemPHPeMySQLsãomaisbaratosqueserviçosseme-
lhantesparaoutrastecnologias.
• MySQLéleveerápido,mesmoparaquantidadesrazoavelmentegrandesde
dados.
1.6 O que vou precisar para acompanhar este livro?
Paradesenvolversoftwaresãonecessáriasalgumasferramentas.Nestelivro,fareiuso
eindicareiapenasferramentasemsoftwarelivre,masvocêpodeusarferramentas
3

## Página 20

1.7. Sobreestelivro CasadoCódigo
quejáconheceecomasquaissesintaconfortável,apenassecertificandodefazeras
devidasadaptaçõesquandonecessário.
NogeraltudooqueseránecessárioéumcomputadorcomoambienteWEBcom
PHPeMySQL,umbomeditordetextoseumnavegadorWEBparatestaraspáginas
queserãocriadas.
Umadicaimportanteparaquembuscaaprenderumanovalinguagemdepro-
gramação,oumesmoaprimeiralinguagemdeprogramaç ão,éreservartempopara
estudarepraticarbastante.Sevocêconseguirsepararumcertotempopordiaere-
almentesededicaràleituraepráticadosexercíciospropostos,rapidamentevocêse
sentirámaisconfortávelcomPHPecomoambienteWEB,oquevailhedarcon-
ceitosgeraisparadesenvolvimentodepáginasdinâmicasatémesmousandooutras
linguagens.
Ouseja,umdosrequisitosparaoestudoserámesmootempoe,quantomais
tempovocêconseguirdedicaraosestudos,maisconseguiráabsorvernovosconhe-
cimentosemaisrápidoconseguirádesenvolversuasaplicações.
1.7 Sobre este livro
Aideiacentraldestelivroéofereceraoportunidadedeoleitorcome çaradesen-
volversuasprimeiraspáginasdinâmicasutilizandoalinguagemPHPassociadaao
bancodedadosMySQL.Estelivroapresentaumaexperiênciadeaprendizadoque
pode(edeve)seraplicadanãosomenteaoPHP,mastambémaquaisqueroutras
tecnologiasparadesenvolvimentodeaplicações,sejamelaswebounão.Duranteos
capítulos,osexemplossãoconstruídosaospoucosealgunserrossãoencorajados,
alémdehaveralgumasreescritasemelhoriasemcódigosquejáfuncionam—mas
quepodemsofrerpornãoutilizaremtécnicasquesimplificamalógicaegarantem
maiorfacilidadeparafuturasalterações.
EstelivronãoéumguiadereferênciaparaPHPeMySQLe,assimsendo,não
apresentalistasdefun çõesebibliotecasdisponíveisparaestastecnologias. Ofoco
aquiérealmenteumprocessodeaprendizado,atravésdaconstruç ãogradualdeapli-
caçõeseassimilaç ãodosconceitos.
Estudantesdecursosrelacionadosadesenvolvimentodesistemas,curiososestu-
dandoprogramaçãoparawebehobistaspodemsebeneficiargrandementedocon-
teúdodestelivro.Porém,desenvolvedoresmaisavan çadosquedesejamapenasum
guiadereferênciaparatiraraqueladúvidasobreumafun çãoououtradalinguagem
podemnãoencontrarbenefíciosnestaspáginas.
4

## Página 21

CasadoCódigo Capítulo1. Introdução
WebdesignerscomexperiênciaemHTMLeCSSquedesejamaprenderadesen-
volverparabackendtambémpodemsebeneficiarbastantedoconteúdodestelivro.
Mesmosendofocadonoiniciante,estelivrobuscatrazerconteúdoatualizado
comaspráticasmaisrecentesdoPHPeseuambiente.
Sempre que estiver com alguma dúvida, não deixe de perguntar na lista
de discussão do livro. Ela está em https://groups.google.com/forum/#!forum/
phpemysqlcasadocodigo.
OsexemplosdecódigousadosnestelivropodemserbaixadosnoGitHubem
https://github.com/InFog/phpmysql
Agora,acomode-senacadeiraebonsestudos!
5

## Página 23

Capítulo2
OprimeiroprogramaemPHP
ChegouomomentodeescreveronossoprimeiroprogramaemPHP!Paraisso,é
necessárioteroPHPealgumasoutrasferramentasinstaladasnonossocomputador.
Aindanãoéhoradesepreocuparcomtodasasferramentas,poisprecisamos
realmenteapenasdoPHP.Mesmoassimiremosinstalarumpacotãocompratica-
mentetudooqueprecisaremosduranteolivro.Apenasnãosepreocupecomessas
ferramentasagora,tudobem?
2.1 Instalando o PHP
Umaótimaop çãoparainstalaroPHPéoXAMPP.Estepacotecontémtudooqueé
precisoparacome çaraprogramaremPHP.Parainstalar,acesseositedoXAMPPe
cliquenaop ção XAMPP para Windows,vejanaimagem:

## Página 24

2.1. InstalandooPHP CasadoCódigo
Figura2.1:SitedoXAMPPcomlinkparaoXAMPPparaWindows
Ah,ositedoXAMPPéesteaqui:http://www.apachefriends.org/pt_br/xampp.
html.
Napróximapágina,cliquenolink XAMPPlogoabaixodotítulo Download:
8

## Página 25

CasadoCódigo Capítulo2. OprimeiroprogramaemPHP
Figura2.2:Op çãoparaDownloaddoXAMPPparaWindows
Agoracliquenolink Instalador,vocêserádirecionadoparaapáginade
download.Oarquivotemcercade100MB,aproveiteparatomarumcaféenquanto
baixa:
9

## Página 26

2.1. InstalandooPHP CasadoCódigo
Figura2.3:DownloaddoinstaladordoXAMPPparaWindows
Apósfinalizarodownload,abraoinstaladoreusetodasasop çõespadrão,apenas
clicandoem Próximoou Nextatéfinalizarainstalação.
Depoisdeinstalar,cliqueem Finalizarou Finish,deixandoaop çãode
abriropaineldoXAMPPmarcada:
10

## Página 27

CasadoCódigo Capítulo2. OprimeiroprogramaemPHP
Figura2.4:Finalizandooainstalaç ãodoXAMPP
Nopainelqueabrir,cliquenobotão startapenasdoserviçochamado Apache:
Figura2.5:PaineldoXAMPP,useaop çãodeiniciaroApache
OApacheéoservidorwebqueseráresponsávelporentregaraspáginasquando
onavegadorsolicitar.
PodeserquesejanecessárioliberaroApacheno firewalldoWindows:
11

## Página 28

2.2. PHPnoLinux CasadoCódigo
Figura2.6:LiberaroApachenoFirewalldoWindows
OXAMPPseráinstaladonapasta C:\xampp\.
2.2 PHP noLinux
SevocêusaLinux,useogerenciadordepacotesdasuadistribuiç ãofavoritapara
instalaroPHP.Ébemfácilusaro apt-getnoDebianenoUbuntuouo yumnos
derivadosdoFedora. ApenasprocurepelospacotesdoPHPedoApacheefaç aa
instalação.
PHP noDebian/Ubuntu
ParainstalaroPHPnoDebian/Ubuntu,useocomandoabaixo.Isso
iráinstalaroPHP,ApacheeoMySQLedeixartudoprontoparausar.
sudo aptitute install php5 php5-mysql apache2
libapache2-mod-php5 mysql-server
12

## Página 29

CasadoCódigo Capítulo2. OprimeiroprogramaemPHP
PHP noMacOSX
UsuáriosdoMacOSXtambémpodemusaroXAMPP,apáginapara
download fica emhttp://www.apachefriends.org/en/xampp-macosx.
html
BaixeopacoteDMGesigaasinstruçõesdeinstalaç ão.
Apósainstalação,abraseunavegadoreacesseoendere çolocalhost.Vocêdeverá
verumapáginadeboasvindasdoXAMPP,ouumapáginadizendoqueoApache
estáfuncionando:
Figura2.7:HomepagedoXAMPPinstaladolocalmente
O que é o localhost?
Acabamosdeacessaroendere çolocalhostatravésdonavegador.Este
éoendereçolocaldocomputador—elecorrespondesempreaopróprio
computador.ApósinstalaroXAMPP,umservidorwebtambémestará
instaladonocomputador,porissoserápossívelacessá-loatravésdona-
vegador.
13

## Página 30

2.3. Evamosaoprimeiroprograma! CasadoCódigo
2.3 E v amos ao primeiro programa!
Certo,comoXAMPPinstalado,éhoradeescreveroprimeiroprogramaemPHP!
Abraumeditordetextosedigiteoseguintecódigo:
<?php
echo "Hoje é dia " . date('d/m/Y');
Agora,salveoarquivocomo C:\xampp\htdocs\programa.phpeacesse
atravésdonavegadoroendere ço localhost/programa.php,vocêdeveráver
umapáginaassim:
Hoje é dia 26/05/2013
Onde salv ar os arquivos no Linux e no MacOSX?
Se você usa Debian ou Ubuntu, a pasta para salvar o arquivo é
/var/www. Lembre-sededarpermissãoparaseuusuáriocriararqui-
vosnestapasta.
UsuáriosdoMacOSXqueinstalaramoXAMPPdevemsalvaros
arquivosem /Applications/XAMPP/htdocs/.
O que é a pasta htdocs do XAMPP?
EstapastaéaraizdoservidorApache.Éapartirdelaquepodemos
acessarnossosarquivosdentrodoApache. Porexemplo,umarquivo
chamado pagina.phpdentrodapasta htdocspoderáseracessado
atravésdoendereço localhost/pagina.php.
Agora,sevocêcriarumapastanovadentrodehtdocs,porexemplo,
apasta siteedentrodelaumarquivo pagina.php,oacessoseráfeito
atravésdoendereço localhost/site/pagina.php.
Éclaroqueadataexibidanoseunavegadorserádiferente,poiselaserágerada
automaticamentepeloPHP.Vamosalterarumpoucoestecódigo,paraenxergarmos
melhorasmudan çasacontecendo.Altereoarquivo programa.php,colocandoo
códigoaseguir:
14

## Página 31

CasadoCódigo Capítulo2. OprimeiroprogramaemPHP
<?php
echo "Hoje é dia " . date('d/m/Y');
echo " agora são " . date('H:i:s');
Atualizeapáginanonavegador,paraissouseaop çãoderecarregarouaperteo
botão F5.Percebeuoqueaconteceu?Agoraeletambémexibeahora,osminutos
eossegundosdahoradarequisiç ão.Experimenteatualizarapáginaalgumasvezes,
vejaqueacadarequisiç ãoosdadosserãoalterados.Esevocênãoatualizarmaiso
navegador?Oqueacontece?
NADA!
Issomesmo,nadaacontecerá. Mas,nãoeraparaelecontinuaratualizandoa
hora?
Requisição , processamento e entrega
Oqueaconteceéoseguinte:Quandoonavegadorpedeumapágina
nova,ouatualizaumasendoexibida,aconteceuma requisição.OApa-
cherecebeestarequisiç ãoepedeparaoPHPfazero processamento.É
nestahoraqueoPHPpreencheosdadospegandoadataeahoradocom-
putador.Depoisdeprocessartudo,oPHPdevolvetudoparaoApache,
queentregaparaonavegador.
Onavegador,então,exibeosdadosjáprocessados,eéporissoquea
páginanãomudamaisseumanovarequisiç ãonãoforfeita.
Alias,vocêsabiaquePHPsignifica PHP Hypertext Preprocessor?Ou,
emportuguês: PHPPré-processadordeHipertexto,sendoquehiper-
textoéoHTML.Legal,né?
2.4 A minha página está mostrando a hora errada!
Asuapáginapoderámostrarahoraerrada,poisoPHPdoXAMPPvemconfigurado
comoahoradeoutropaís.Paracorrigirisso,bastaeditaroarquivodeconfiguraç ão
doPHPdentrodainstalaç ãodoXAMPP.Oarquivoéo php.inie,noXAMPP,ele
ficaem c:\xampp\php\php.ini.Nestearquivoprocurepelalinhaquecome ça
com date.timezone =.Naminhaconfiguraç ãoeleveioassim:
date.timezone = Europe/Berlin
15

## Página 32

2.5. Resumo CasadoCódigo
VejaqueeleestácomohoráriodeBerlim!Bastaalterarparaumhoráriobrasi-
leiro.Nomeucaso,ficouassim:
date.timezone = America/Sao_Paulo
SevocênãoestivernohoráriodeSãoPaulo(Brasília),vocêpoderápesquisaro
seutimezonenalistadetimezonesdaAméricaqueficanesteendere ço:http://php.
net/manual/en/timezones.america.php.
Usuários de Debian/Ubuntu vão encontrar o arquivo php.ini em
/etc/php5/apache2/php.ini.
Apósalteraresalvaroarquivo,seránecessárioreiniciaroApache.Useopainel
doXAMPPparaparareiniciarnovamenteoApache.SevocêusaDebian/Ubuntu,
useocomando sudo service apache2 restart.
Qual editor de textos devo usar?
ATENÇÃO:NãoutilizeeditorescomooWordouoWriter,poisestes
editoresgravamváriasinformaçõesalémdotextonosarquivos.
Existemdiversoseditoresdetextoquepodemserusadosparaedi-
tarseuscódigosemPHP.NoWindows,omaissimplesdeleséobloco
denotas,masexistemoutrasop ções. Aminharecomendaç ãoéo No-
tepad++umótimoeditordetextosquepermiteescreveremdiversas
linguagens,inclusivePHPeHTML.Sevocêaindanãousaumeditorde
textosparaseuscódigos,ouestácome çandoagora,eurecomendousar
oNotepad++.
ParabaixaroNotepad++acesse http://notepad-plus-plus.org/ecli-
que na opção Downloads. Na próxima página, clique no link
Notepad++ Installer.Oinstaladorésimples,bastausarasop ções
padrão.
SevocêusaLinux,recomendooGeditouoKate.
2.5 Resumo
Oquefizemosatéagoraébemsimples,masjánosdáalgumasinformaçõesimpor-
tantessobreoPHP.Primeiro,vocêdeveterpercebidoqueumprogramaemPHP
começacom <?php.Éestepequenotrechoquediz apartirdaqui,oPHPdeverá
processaroscódigos.
16

## Página 33

CasadoCódigo Capítulo2. OprimeiroprogramaemPHP
Outracoisaquepodemosperceberéqueainstruç ão echoéusadaparaimpri-
mirinformaçõesparaonavegador.
Estearquivotambémnosmostraque,assimcomoemoutraslinguagens,em
PHPumalinhadeinstruçõesterminacom ;(pontoevírgula).
Umúltimoaprendizadodestearquivoéafun ção date(),querecebeumfor-
matodedataparaformataradataatualdocomputador.Usamosalgumasop çõesde
formataçãocomo Yparaexibiroanocomquatrodígitose Hparaexibirahorano
formato24horas.
2.6 Desafios
Aofinaldecadacapítulocolocareialgunsdesafioscomoformadepraticaroque
foivistoatéaquelemomentoeatéfor çarumpoucomais.Dessaforma,vocêpode
pesquisarmaissobrePHPeresolvernovosproblemas.
Agoraquejáconseguimosexibiradataeahora,tentefazerosdesafiosabaixo:
• Nafunção date(),experimentemudaro Ypara y.Oqueacontece?
• Vocêconsegueexibirahoranoformatode12horas,amepm?
• Esevocêtivessequeexibirodiadasemana?Comofaria?
• Exibaquantosdiasfaltamparaopróximosábado. Porexemplo,sehojefor
quarta,entãofaltam3diasparasábado.
• Exibatambémonomedomêsatual.
17

## Página 35

Capítulo3
Construindoumcalendáriocom
PHP
Ok,nossoprimeiroprogramaapenasexibiaadataeahoradoprocessamentoreali-
zadopeloPHP.Agoravamoscriarumapáginaqueexibeumcalendário.
Nestecapítulo,conheceremosmaissobreoPHP.Leiacomaten ção,faç aeaté
refaçaosexercícios. Éfundamentalparacompreendermelhoralgumaspartesdo
PHP,entãofiquedeolhonasnovidadesqueserãoapresentadas.
3.1 Definindo nosso calendário
Nossapáginaexibiráumcalendário,usaremostabelasHTMLqueserãomontadas
peloPHPacadanovarequisiç ão,dessaformateremossempreocalendáriogerado
peloPHP,semterquecriarapáginamanualmente.
ComoestãoseusconhecimentosHTML?Horadedesenferrujarepraticar,mas
usaremosPHPparaescreverumapartedonossoHTML.

## Página 36

3.2. Começandoocalendário CasadoCódigo
Aofinaldesdecapítulo,vocêterádesenvolvidoumprogramaPHPquevaigerar
umcalendárioparecidocomoabaixo:
Figura3.1:Exemplodecomoficaráocalendário
PercebaqueocalendárioéapenasumatabelaHTML.Aliás,reparetambémque
vocêpoderáadicionarestatabelaemoutrosprogramasemPHPquevocêestejade-
senvolvendo!Issoébemlegal,seuprimeirocomponentePHP.
Vamosemfrente. Nestecapítulovocêtambémaprenderánovoscomandose
conceitosdoPHP.
3.2 Começando o calendário
Vamoscomeçardefinindoaprimeirapartedocalendário,crieumnovoarquivocha-
mado calendario.phpesalveem c:\xampp\htdocs.Lembre-sequeumar-
quivosalvonestapastapoderáseracessadousandoo localhostatravésdonave-
gador.
Poisbem,vamosaocódigo:
<table border="1">
<tr>
<th>Dom</th>
<th>Seg</th>
<th>Ter</th>
<th>Qua</th>
<th>Qui</th>
<th>Sex</th>
<th>Sáb</th>
20

## Página 37

CasadoCódigo Capítulo3. ConstruindoumcalendáriocomPHP
</tr>
</table>
Pronto,bemsimples. Acesseoendere ço localhost/calendario.phpe
vocêveráumasaídaparecidacomesta:
Figura3.2:Cabe çalhodocalendário
Mas,esperaumpouco.IssoéHTML!NãoiríamosescreverPHP?Esteémaisum
atributointeressantedoPHP: PodemosescreverHTMLdentrodearquivosPHP.
Vejaesteoutroexemplodeintegraç ãodeHTMLePHP:
<h1><?php echo "Título dentro do H1"; ?> </h1>
Percebaqueoconteúdodatag h1éTítulodentrodoH1 eesteconteúdofoi
adicionadousandoo echodoPHP.NotetambémqueiniciamosoPHPcom <?php,
assimcomodaoutravez,masdestaveztambémfechamosoPHPcom ?>.Apóso
?>,podemosvoltaracolocarHTML.
PodemosiniciarefecharoPHPdiversasvezesdentrodeumaestruturaHTML,
masdevemosnomearoarquivocomo .php.Tentefazeresteexemplo,emumnovo
arquivochamado hoje.php:
<html>
<head>
<title>Dia <?php echo date('d'); ?> </title>
</head>
<body>
<h1>Estamos em <?php echo date('Y'); ?> </h1>
<p>
Agora são <?php echo date('H'); ?> horas e
<?php echo date('i'); ?> minutos.
</p>
</body>
<html>
21

## Página 38

3.3. Usandofunções CasadoCódigo
3.3 Usando funções
Bem,voltandoaoassuntodocalendário,vamosadicionarumafun çãoaoarquivo
calendario.phpparadesenharumanovalinhanatabela.Umalinhadeveconter
setecolunas,paraossetediasdasemana:
<?php
function linha()
{
echo "
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
";
}
?>
<table>
...
</table>
Adicionamosafun çãoantesdatabela.Agoravamosadicionaraslinhas:
<table border="1">
<tr>
<th>Dom</th>
<th>Seg</th>
<th>Ter</th>
<th>Qua</th>
<th>Qui</th>
<th>Sex</th>
<th>Sáb</th>
</tr>
<?php linha(); ?>
<?php linha(); ?>
<?php linha(); ?>
22

## Página 39

CasadoCódigo Capítulo3. ConstruindoumcalendáriocomPHP
<?php linha(); ?>
<?php linha(); ?>
</table>
Adicionamoscincochamadasàfun ção linha(),assim,quandoacessarmos
localhost/calendario.phpserárenderizadaumatabelaparecidacomesta:
Figura3.3:Calendárioaindasemosdias
Agoravamosadicionarumanovafun çãoparadesenharocalendário.Estafun-
çãoseráchamadade calendario()edeveráseradicionadalogoapósafun ção
linha:
<?php
function linha()
{
...
}
function calendario()
{
$dia = 1;
$semana = array();
while ($dia <= 31) {
array_push($semana, $dia);
if (count($semana) == 7) {
linha($semana);
$semana = array();
}
$dia++;
}
23

## Página 40

3.3. Usandofunções CasadoCódigo
}
?>
Aquitemosbastantecoisanova.Pelaprimeiravezestamosusandovariáveisno
PHP.Reparequeasvariáveissemprecome çamcomumcifrão( $).Estaéumaregra
doPHP:elassempreiniciamcomcifrãoseguidodeumaletraouum underline.
Sendoassim,asvariáveis $dia, $semana, $pessoae $_nomesãoválidasparao
PHP,masas $1, $-nomee $!nomesãoinválidas.
NestetrechotambémestamosusandoumtipodedadosdoPHPchamadode
array.
Reparounousodainstruç ão while? Viuqueestainstruç ãoépraticamente
igualao whiledelinguagenscomo C?Outrainstruç ãobemparecidaéo if,que
verificaseumacondiç ãoéverdadeira.
Paradesenharocalendário,iniciamosnodiaprimeiroeusamoso whilepara
fazerumlaçoqueserepetiráatéodia31. Oarray $semanaéusadoparacolocar
osdiasdasemanaegarantimosqueelenãoterámaisquesetediasusandoo if.A
função array_push()adicionamaisumvaloremnossoarrayedentrodo ifo
arrayéreiniciado.
Ah,umanovafun çãoapresentadafoia count().Seufuncionamentoéfácilde
deduzir,certo?Elacontaaquantidadedeitensdonossoarray $semana.
Masreparequeanossafun ção linha()foichamadacomumparâmetro,queé
umarraycomosdiasdasemana.Então,precisamosalterarafun ção linha()para
receberestearrayeexibirseusvalores.Altereafun ção linha()paraficarcomo
esta:
<?php
function linha($semana)
{
echo "
<tr>
<td>{$semana[0]}</td>
<td>{$semana[1]}</td>
<td>{$semana[2]}</td>
<td>{$semana[3]}</td>
<td>{$semana[4]}</td>
<td>{$semana[5]}</td>
<td>{$semana[6]}</td>
</tr>
24

## Página 41

CasadoCódigo Capítulo3. ConstruindoumcalendáriocomPHP
";
}
Vejaqueagoraelarecebeumparâmetrochamado $semanaeoconteúdode
$semanaéexibidousandooscolchetesparaacessarcadaumdositens. Atenção:
Umarrayiniciaseusitensnonúmerozero!Porisso,exibimosdozeroaoseis.
Agoraprecisamosfazermaisumaalteraç ãoparaexibirocalendárioquetemos
atéagora.Natabela,retireaquelascincochamadasparaafun ção linha()etroque
porumachamadaparaafun ção calendario():
<table border="1">
<tr>
<th>Dom</th>
<th>Seg</th>
<th>Ter</th>
<th>Qua</th>
<th>Qui</th>
<th>Sex</th>
<th>Sáb</th>
</tr>
<?php calendario(); ?>
</table>
Agora,acesse localhost/calendario.php,ouatualizeapágina,casojáes-
tejaaberta,evocêveráumresultadoparecidocomeste:
Figura3.4:Calendário,massemtodososdiasdomês
Jáestáparecidocomumcalendário!Maseleestáexibindoapenasatéodia28!
Issoestáacontecendoporestarmosverificandoseonúmerodeitensnavariável
25

## Página 42

3.4. Entendendoeseentendendocomoserros CasadoCódigo
$semanaéiguala7. Oproblemaéqueestenúmeronãovaichegarasete,jáque
de28para31sãoapenas3diasdediferen ça.
3.4 Entendendo e se entendendo com os erros
Umapossívelsoluçãoseriachamarafun ção linha()apósolaço whilepassando
oarray semanacommenosdias.Altereseucódigoparafazerestachamada:
<?php
function calendario()
{
$dia = 1;
$semana = array();
while ($dia <= 31) {
array_push($semana, $dia);
if (count($semana) == 7) {
linha($semana);
$semana = array();
}
$dia++;
}
linha($semana);
}
?>
Atualizeapágina.Vejaqueosdiasestãosendoexibidos,maspercebaaquanti-
dadedeerrosqueapareceram!
26

## Página 43

CasadoCódigo Capítulo3. ConstruindoumcalendáriocomPHP
Figura3.5:Calendáriocompleto,mascomalgunserros
Vejaqueoerroinformadoé Undefined offset: 3.Issoquerdizerqueele
estátentandoacessaroíndice3noarray $semanaenãoestáencontrando.Omesmo
acontececomosíndices4,5e6,porissoessemontedeerrosapareceu.
A importância das mensagens de erro
Écomumqueprogramadoresnovatosignoremasmensagensdeerro
dalinguagem.Issoéumproblema,poisquandoalgumafalhaacontece,
alinguagemfazomelhorpossívelparaindicaroqueaconteceu.Quando
toparcomumerronoPHP,tenteleramensagemecompreenderoque
houve.Emgeral,eledizalinhadoerroeexplicabemoproblema.
3.5 MeuPHP não mostrou os erros!
Podeacontecerdevocênãoenxergaroserrosgerados,poisseuPHPpodeestarcon-
figuradoparanãoexibiroserros. Estaéumaconfiguraç ãodoPHP,assimcomo
aqueladotimezonequefizemosnoexemplodoiníciodolivro.Parafazercomque
oPHPexibaoserros,alterenoarquivo php.inialinha:
27

## Página 44

3.6. Finalizandoocalendário CasadoCódigo
display_errors = Off
Para
display_errors = On
3.6 Finalizando o calendário
Vamosmudarumpoucooscriptparanãogerarerroseparaexibircorretamenteo
nossocalendário.Altereapenasafun ção linha()paratestarseosíndicesexistem
antesdeexibi-los.Paraisso,vamosusarumlaço for,queébemparecidocomo
fordeoutraslinguagens.Dentrodolaço,vamosusarafun ção issetqueverifica
seumavariávelexisteouseumíndiceemumarrayfoidefinido. Ocódigodeverá
ficarassim:
<?php
function linha($semana)
{
echo "<tr>";
for ($i = 0; $i <= 6; $i++) {
if (isset($semana[$i])) {
echo "<td>{$semana[$i]}</td>";
} else {
echo "<td></td>";
}
}
echo "</tr>";
}
Agora,executenovamenteoarquivo calendario.phpevocêteráumresul-
tadobemparecidocomeste:
28

## Página 45

CasadoCódigo Capítulo3. ConstruindoumcalendáriocomPHP
Figura3.6:Calendáriofinal,semerrosecomtodososdias
3.7 Resumo
Nestecapítuloforamintroduzidasalgumascaracterísticasefuncionalidadesinte-
ressantesdoPHP,comoaop çãodeusarHTMLePHPnomesmoarquivo,eouso
defun çõesparacentralizarblocosquepodemserrepetidosnofluxodoprograma.
Tambémforamtratadososlaços forewhile,alémdousodacondicional ifeda
função isset()queverificaseumavariávelfoidefinida.
3.8 Desafios
Prontoparaalgunsdesafios?Sugirocopiarocalendárioatualparafazerostestese
desafiospropostos.
• Façaumapáginaqueexibaahoraeafrase“Bomdia”,“Boatarde”ou“Boa
noite”,deacordocomahora.Useacondicionalifeafun ção date().
• Façacomqueocalendárioexibaodiaatualemnegrito,usandoafun ção
date().
• Exibaosdomingosemvermelhoeossábadosemnegrito.
• Façaocalendáriocome çaremumdiaquenãosejaumdomingo.
• Eumcalendáriodoanotodo?Seráqueémuitocomplexo?
29

## Página 47

Capítulo4
Entradadedadoscomformulário
Nocapítuloanterior,foramapresentadasváriasfuncionalidadesdoPHPetambém
suasintaxeparablocoselaçosutilizadosemdiversaslinguagens.Agoravamosaum
novoprojeto:aconstruç ãodeumalistadetarefas.
4.1 Definindo a lista de tarefas
Nossoprojetoserácompostoporapenasalgumaspáginas,comoalistadetarefas
eumformulárioparaadicioná-laseeditá-las.Duranteesteprojetoseránecessário
receberdadosdousuário,nocaso,asdescriçõesdastarefas.Émuitoprovávelque
vocêjátenhausadositesquepedemalgumtipodeinformaç ão,oumesmosistemas
onlinenosquaisénecessáriocadastrarváriostiposdedados.Poiséexatamenteisso
oquefaremos—exibiremosumformulárioperguntandoalgumasinformaçõespara
ousuárioequandoeleinserirasinformações,iremostratá-las.

## Página 48

4.2. Oformuláriodecadastrodetarefas CasadoCódigo
4.2 O formulário de cadastro de tarefas
TrabalharcomwebexigeconhecimentosemHTML.Equandodigoconhecimentos
emHTML,estoudizendorealmenteconhecerHTMLenãotermedodecriarpági-
nasusandoapenasumeditordetextosparaescreverseuHTML.Sevocêjáconhece
umpouco(oubastante)dewebeusaeditoresnosquaisvocêpraticamentedese-
nhaapágina,comooDreamweaveresimilares,eurecomendoqueutilizeapenas
umeditordetextoparareproduzirosexercíciosdestelivro.Assimficamaisfácilde
entenderoqueestáacontecendoeporqueacontecedestaoudaquelamaneira.
Vamosaoformulárioparaocadastrodastarefas.Crieumapastanovachamada
tarefasdentrodapastado htdocsdoXAMPP(ouondeestiverasuainstalaç ão
doApache).Nestapasta,crieumarquivochamado tarefas.php.Nestearquivo
vamoscriaroformulárioparaastarefas.
Inicieoarquivocomoseguinteconteúdobásico:
<html>
<head>
<title>Gerenciador de Tarefas</title>
</head>
<body>
<h1>Gerenciador de Tarefas</h1>
<!-- Aqui irá o restante do código -->
</body>
</html>
Nossoprojetoirácomeçarsimplesedepoisadicionaremosmaisfuncionalidades
conformeanecessidade.Porisso,vamoscome çarpelomaisimportante,onomeda
tarefaaserrealizada.Esteéocódigoquedefineonossoformulário:
<form>
<fieldset>
<legend>Nova tarefa</legend>
<label>
Tarefa:
<input type="text" name="nome" />
</label>
<input type="submit" value="Cadastrar" />
</fieldset>
</form>
32

## Página 49

CasadoCódigo Capítulo4. Entradadedadoscomformulário
NãotenhamedodedigitarocódigoHTML,lembre-sedetreinarbastante,as-
simficanasuamemóriamuscular. Adicioneocódigodoformuláriologoapóso
comentárionoHTMLquedizquealiiráorestantedocódigo.
Agoraacesseestanovapáginanoendere ço:
http://localhost/tarefas/tarefas.php
Seuformuláriovaificarbemparecidocomeste:
Figura4.1:Formulárioinicialparaocadastrodetarefas
4.3 Entrada de dados
Certo,agoratemosumformuláriosendoexibido,mas,comoseráqueoPHPcon-
seguepegarosdadosquesãoinformadosnosformulários?Vamosfazerumexpe-
rimento:nonomedatarefa,digite EstudarPHP ecliquenobotão Cadastrar.O
queaconteceu? Aparentemente,nada,masotextosumiudacaixadetexto. Eou-
tracoisamuitointeressantetambémaconteceu,oendere çodonossoscriptmudou!
Sim,reparequeagoraexisteumainterrogaç ãonoendere ço,seguidaporumtexto
quetemmuitoanosdizer.Vejacomoficouoendere ço:
http://localhost/tarefas/tarefas.php?nome=Estudar+PHP
Dáparatirarmosalgumasconclusõesaqui,certo? Onomedo inputnofor-
mulárioénomeenesteendere çotemosumtrecho nome=,ouseja,oquedigitamos
nocampofoi enviadoatravésdoendereço,atravésdaURL(vouchamaroendere ço
deURLdaquiparafrente).
Naprimeiravezquechamamosapágina,seuendere çonãotinhaotrechocom
onomedatarefa,masquandodigitamosonomeeenviamos,estetrechopassoua
aparecerdepoisdosímbolodeinterrogaç ão( ?).Ouseja,umformulárioservepara
enviarmososdadosparaalgumlugar.
33

## Página 50

4.4. PegandoosdadosdaURL CasadoCódigo
Entrada de dados na web
Sevocêjáprogramoualgumsoftwareparadesktopouscriptsparaa
linhadecomando,jádeveterlidadocomentradadedadosdousuário.
Nestetipodesoftware,emgeralbastapararoprocessamentoepedir
paraousuárioinformarumvalor,eentãoseguiremfrenteusandoovalor
fornecido.
Naweb,ascoisassãoumpoucodiferentes.OPHPnãopodeserpa-
radoparaperguntaralgoparaousuário,entãoosdadosjádevemexistir
paraoPHPquandooscriptcome çararodar. Confuso? Naverdadeé
sóumamaneiradiferentedeencararaentradadedados. Vejaanossa
URL,porexemplo,elatemotrecho nome=Estudar+PHP.Estetrecho
serveparainserirumainformaç ãoparaoPHP,nocaso,onomedata-
refa.Sendoassim,quandooscript tarefa.phpcomeçaraexecutar,ele
játeráestainformação.
Porisso,nawebdevemossemprepensarnaentradadedadosusando
osformuláriosqueirãoenviarosdadosparaa próximapágina.
Porenquanto,anossapróximapáginaéamesmapágina,masvere-
moscomomudarissomaisadiante.
Legal,jásabemosqueonomedatarefafoienviadoatravésdaURL.Agoraa
questãoé:ComopegaressedadodentrodoPHP?
4.4 Pegando os dados da URL
PHPnasceuparaawebesedámuitobemcomela.Porisso,emPHPésupersimples
pegarosdadosfornecidospelousuárioatravésdeformulárioseURLs.EmPHPexis-
temalgumasvariáveischamadasde superglobais,issosignificaqueestasvariáveis
existememtodososescoposdeseusprogramasPHP.Ouseja,vocêpodeacessá-las
dentrodefun ções,dentrodela ços,dentrodeclasses...Enfim,emqualquerlugardo
seucódigoelasestarãodisponíveis.
Nonossocaso,vamosusarasuperglobal $_GET.Lembradosarraysqueforam
usadosparafazerocalendário? $_GETtambéméumarrayeomaisinteressanteé
queoPHPpegaoqueestánaURLecolocaem $_GETparausarmos!Vamosfazer
umtesteexibindoonomedigitadologoapósonossoformulário. Paraisso,após
34

## Página 51

CasadoCódigo Capítulo4. Entradadedadoscomformulário
ofechamentodoformulário,ouseja,depoisdatag </form>,adicioneoseguinte
código:
...
</form>
<?php
if (isset($_GET[ 'nome'])) {
echo "Nome informado: " . $_GET['nome'];
}
?>
...
Asreticênciassãoapenasilustrativas,claro!Alias,deagoraemdiantevoucolo-
carreticênciasváriasvezesparailustrartrechosquedeverãoserincluídosdentrode
códigosjáexistentes.
Nestetrechoestamosusandoafun ção isset()queverificaseumavariável
existe,ou,nestecaso,seoíndice nomeexistenoarray $_GET.Casooíndiceexista,
vamosexibi-lousandoo echo.
EmPHP,assimcomoemoutraslinguagens,énecessáriodefinirumavariável
antesdetentarusá-la.Afun ção isset()éinteressanteparanosajudaraverificar
seumavariávelexiste,ounestecaso,umíndiceemumarray,pois isset()nãoirá
gerarumerro,dizendoqueavariávelnãoexiste.
Atualizesuapágina,em http://localhost/tarefas/tarefas.php,mantendoaURL
comonome,oudigitenoformulárionovamenteeenvieosdados.Suapáginadeverá
ficarassim:
 Figura4.2:Exibindoosdadosusando $_GET
35

## Página 52

4.4. PegandoosdadosdaURL CasadoCódigo
Legal,agoraquesabemospegarovalorquefoipassadoatravésdaURLusando
$_GET,podemosguardarestevaloremum arrayqueseráanossalistadetarefas.
Paraisso,troqueocódigoqueacabamosdefazerparaexibironomeinfor-
mado por um que pegue o valor em$_GETe guarde em um array chamado
$lista_tarefas:
...
</form>
<?php
$lista_tarefas = array();
if (isset($_GET[ 'nome'])) {
$lista_tarefas[] = $_GET['nome'];
}
?>
...
Estecódigoébemsimples,apenasverificamosseexisteoíndice nomedentro
de $_GETecasoexista,criamosumnovoíndiceem $lista_tarefasusandoa
sintaxedecolchetesvazios.
Agoraénecessárioexibiralistadetarefas. Aindanomesmoarquivo,antesda
tag </body>vamosadicionarumatabelaHTMLparalistarasatividades.Dentro
destatabelausaremoso foreachparapegarcadaumadastarefasqueestánoarray
$lista_tarefaseexibircomolinhasdatabela:
...
<table>
<tr>
<th>Tarefas</th>
</tr>
<?php foreach ($lista_tarefas as $tarefa) : ?>
<tr>
<td><?php echo $tarefa; ?> </td>
</tr>
<?php endforeach; ?>
</table>
36

## Página 53

CasadoCódigo Capítulo4. Entradadedadoscomformulário
</body>
...
Repassandoocódigo,foicriadaumatabelacomapenasumacoluna,naqualo
cabeçalhoéapalavra Tarefaseaslinhasserãoosnomesdastarefas.
AquiexisteumlaçonovodoPHP.Jávimoso while—agoraapresentoo
foreach.Estelaçoserveparapassarportodososíndicesdeumarray,atribuindo
cadaíndiceaumavariávelqueescolhemos,nocaso,avariável $tarefa.
Umaoutranovidadeaquiéquenãoforamusadasaschavesparacriaroblocodo
foreach,assimcomoforamusadaschavesparaoblocodo while.Naverdade,o
foreachtambémpodeserusadocomaschaves,semproblemas,masestaforma,
usandodoispontosparaabriroblocoeapalavra endforeachficamaislegívelem
templatesHTML.Lembre-sequeonossocódigocom whileestavaapenasdentro
deumgrandecódigoPHP,nestecasoestamoscolocandopequenospedaçosdePHP
dentrodoHTML.Sendoassim,ficamaislegívelfazerousodestasintaxe. Como
exemplo,vejacomoficaomesmoblocousandoaschaves:
<?php foreach ($lista_tarefas as $tarefa) { ?>
<tr>
<td><?php echo $tarefa; ?> </td>
</tr>
<?php } ?>
Nãoparecetermuitadiferen çaemumtrechopequenodesses, masperceba
que <?php } ?>éumalinhabemgenérica,quepodeestarfechandoum if,um
while,um foreachoumesmoumafun çãoeoutrosblocosPHP,enquanto <?php
endforeach; ?>émaisexpressivo. Porisso,recomendousarestaforma. Alias,
vocêpodeexperimentaroutrosblocoscomestasintaxe,comoo ife endif, while
e endwhilee fore endfor.MasprefiraestasintaxeparaostemplatesHTML,
deixandoasintaxedechavesparaosarquivoseblocosquecontenhamapenasPHP.
Bem,voltandoaoassuntodalistadetarefas,aoenviarumnomedetarefa,asua
páginadeveráficarassim:
37

## Página 54

4.4. PegandoosdadosdaURL CasadoCódigo
Figura4.3:Listadetarefascomumatarefa
Comoestamosdeixandotudonamesmapágina,ficafáciladicionarumanova
tarefa,entãovamosadicionarumanovatarefausandooformulárioqueestáantes
databela,noendere çohttp://localhost/tarefas/tarefas.php.Aquieudigitei Estudar
HTMLeuseiobotãocadastrareoresultadofoieste:
Figura4.4:Listadetarefascomumatarefa
Apenasatarefanovaélistada!Ondeestáatarefaantiga?
Por que a primeira tarefa sumiu?
PHPtrabalhaprincipalmentecomwebenestecasooqueacontece
acadanovarequisiç ãoquefazemos,sejapedindoumapágina,sejaen-
viandodados,équeoPHPinterpretatudodenovoedevolveapenas
HTMLparaonavegador.Ouseja,elenãolembradoqueaconteceuna
últimarequisiçãofeita!
Acadanovarequisiç ãooPHPprocessatudodenovoenãoguardaasvariáveis
paraoutrosacessos.Issoéumproblemaparaanossaaplicaç ão,jáqueprecisamos
38

## Página 55

CasadoCódigo Capítulo4. Entradadedadoscomformulário
manteralistadasnossastarefas.Mascalma,nemtudoestáperdido!OPHPtemum
recursoquenosauxiliaráasolucionarisso.
4.5 Sessões no PHP
Orecursoquenosauxiliaráamanterosdadosentreasrequisiçõessãoassessões.
Umasessãoserveparamantermosumavariávelespecialqueiráexistiremtodasas
nossasrequisições.Lembradasuperglobal $_GET?Assessõessãotãofáceisdeusar
quantoa $_GET,bastausarasuperglobal $_SESSION.Agrandediferen çaéque
usamosa $_GETmaisparalerinformaçõeseusaremosa $_SESSIONparaescrever
elerinformações.
Ousoda $_SESSIONexigesóumesfor çoadicional,queéchamarafun ção
session_start()nocome çodonossoprograma. Paraisso,vamosadicionara
funçãoantesdaaberturadoHTML:
<?php session_start(); ?>
<html>
...
Depoisdisso,precisamosalterarousodalista $lista_tarefasparapegar
osdadosde $_SESSION,casoessesdadosexistam.Vamosmudaro ifqueveri-
ficaseexistemdadosem $_GETevamosadicionarumnovo ifapósacriaç ãodo
array $lista_tarefasparapreenchê-locomosdadosda $_SESSION,quando
necessário:
<?php
...
if (isset($_GET['nome'])) {
$_SESSION['lista_tarefas'][] = $_GET['nome'];
}
$lista_tarefas = array();
if (isset($_SESSION['lista_tarefas'])) {
$lista_tarefas = $_SESSION['lista_tarefas'];
}
...
?>
Agora,aocadastraralgumastarefas,oPHPirámanterosdadosentreasrequi-
sições!Vejacomoasualistadeveficar:
39

## Página 56

4.5. SessõesnoPHP CasadoCódigo
Figura4.5:Alistadetarefasusando $_SESSIONparamanterosdados
Legal!Temosumalistadetarefasjábemfuncional!Claroqueagoraprecisamos
demaisfuncionalidades,comoeditareexcluirumatarefa,masjáconseguimospegar
váriosconceitosdaprogramaçãoparawebusandoPHP.
Agoradáatéparabrincarumpoucocomovisualdaaplicaç ãousandoumas
linhasdeCSS.Omeuficouassim:
Figura4.6:AlistausandoumpoucodeCSS
Se quiser pegar este CSS, basta baixar aqui:https://gist.github.com/InFog/
6860949
Agorafaçaduasexperiências:abraoutronavegadoreacesseoendere çodalista
detarefasem http://localhost/tarefas/tarefas.php,oqueacontece?Astarefasapare-
cem?Não?Maselasnãoestãonasessão?
40

## Página 57

CasadoCódigo Capítulo4. Entradadedadoscomformulário
Como funcionam as sessões?
Secolocamososdadosnasessão,porqueelesnãoaparecemquando
usamosoutronavegador?
ParaoPHPsaberqualusuárioéodonodeumasessão,eleguarda
algumasinformaçõesnos Cookiesdonavegador.Naverdade,ainfor-
maçãomaisimportanteficaemumcookiechamado PHPSESSID,que
guardaumcódigoúnicodeidentificaç ãodasessãodaqueleusuárioque
estáacessandoaaplicaçãoPHP.
NóstambémpodemosusarosCookiesparaguardarinformaçõesque
serãomantidasentreasrequisições.Paraisso,bastausarumaoutrasuper
globaldoPHPchamada $_COOKIE.Estasuperglobaltambéméum
array,assimcomoa $_SESSION.
Aoutraexperiênciaéatualizarapáginaapóscadastrarumatarefa. Faç aisso
usandoF5ououtraop çãodeatualizaç ãodonavegador.Oqueacontece?Aúltima
tarefacadastradaserepete!Econtinuaserepetindoapósasatualizaçõesdapágina!
Veremosmaisparafrentecomoresolverestesdoisproblemas.
4.6 R esumo
Nestecapítuloiniciamosodesenvolvimentodeumalistadetarefas.Elaaindaébem
simplesecontémpoucosdados,masjáestamostrabalhandocomformulárioseen-
tradadedadosnawebutilizandoasuperglobal $_GETdoPHPetambémestamos
manipulandoassessõesutilizadoasuperglobal $_SESSION.
SuperglobaissãovariáveisdoPHPqueestãodisponíveisemqualquerpontoda
aplicação.Nocasodassuperglobais $_GETe $_SESSION,osvaloressãoguardados
emarrays.
Importante: sempre que quiser usar sessões será necessário usar a função
session_start(),semissoasessãosimplesmentenãofunciona.Ficaadica:D
4.7 Desafios
Muitobem,éhoradealgunsdesafios:
• Usandoosmesmosconceitosquevimosatéagora,monteumalistadecontatos
naqualdevemsercadastradosonome,otelefoneeoe-maildecadacontato.
41

## Página 58

4.7. Desafios CasadoCódigo
Continueusandoassessõesparamanterosdados.
• Crieumacópiadoprojetoatéagora(poisvamoscontinuarnospróximosca-
pítulos)ealtereparausarasuperglobal $_COOKIEemvezdeusarassessões.
ParaadicionarumCookieuseafun ção setcookie()querecebeonome
docookieeumtextocomseuvalor.Parapegarumcookiejádefinidousea
superglobal $_COOKIE.
• Depoisdealteraraaplicaçãoparausarcookiesnolugardesessões,tenteabrir
oscookiesnasop çõesdonavegadorevejaseseusdadosaparecemlá.
42

## Página 59

Capítulo5
Tratamentodediferentescamposde
formulários
Nocapítuloanterior,construímosabaseparaanossalistadetarefas.Agoravamos
adicionarmaisinformaçõesefuncionalidadesaoprojeto.
Antesdecome çaraadicionarmaisinformaçõesefuncionalidadepodemosparar
paraanalisarumpouconossocenárioatualeentãodecidirsepodemoscontinuar
comelecomoestáousepodemosfazeralgoparamelhorar.
Estapodeserumaetapaimportantenodesenvolvimentodeumaaplicaç ão,pois
podetornarotrabalhoàfrentemaissimplesoumaiscomplicado.Àsvezesémelhor
alterarabasedaaplicaç ãoparapoderevoluirdeformamaiseficientedoqueinsistir
emumcódigonãomuitobom.Nãosepreocupesenãoconseguirfazerissologono
começo,poisaexperiênciatambémajudabastantenestetipodedecisão.

## Página 60

5.1. Organizandoocódigoemarquivosseparados CasadoCódigo
5.1 Organizando o código em arquivos separados
Oquetemosatéomomentoéumalistadetarefasquetemapenasonomedata-
refaesópermiteadicionarnovastarefas.Tudoissofoifeitoemapenasumarquivo
quecontémumpoucodeHTMLeumpoucodePHP.Podemoscontinuarcomesta
estrutura,mascomotempooarquivovaicrescerepodeficarcomplicadodelere
entenderumarquivomuitograndeedivididoemmaisdeumalinguagem.Porisso,
aquientraumadecisãoimportante,vamossepararnossaaplicaç ãoemdoisarqui-
vos,umdelesfaráoprocessamentodeentradadedadosemanipulaç ãodasessãoe
ooutroiráexibiroformuláriodecadastrodetarefasealistadastarefascadastradas.
Nãoadicionaremoscódigonovo,vamosapenassepararocódigoatualemdois
arquivos—umarquivoseráo tarefas.phpcomesteconteúdo:
<?php
session_start();
if (isset($_GET[ 'nome'])) {
$_SESSION['lista_tarefas'][] = $_GET['nome'];
}
if (isset($_SESSION['lista_tarefas'])) {
$lista_tarefas = $_SESSION['lista_tarefas'];
} else {
$lista_tarefas = array();
}
include "template.php";
PercebaqueapenasjuntamosostrechosdePHPqueantesestavamseparados
emapenasumarquivoquecontémsomentecódigoPHP.Outrodetalheimportante
nestearquivoéousodainstruç ão include,queserveparaincluiroconteúdo
deoutroarquivonofluxoatual. Olegaldo includeéqueeleadicionaooutro
arquivoetodasasvariáveisefun çõesdoarquivoatualcontinuamvalendonoarquivo
incluído,porissopodemos,nestecaso,incluirumarquivocomapenasotemplate
doformuláriodecadastrodetarefasealistadetarefaseaindapodemoscontinuar
usandoavariável $lista_tarefasquefoidefinidanoarquivo tarefas.phpe
quecontémumarraycomastarefascadastradas.
Oarquivocomotemplatedevesechamar template.phppoisesteéoarquivo
queestamosincluindousandoo includenoarquivo tarefas.php.Vejacomo
ficaoarquivo template.php:
44

## Página 61

CasadoCódigo Capítulo5. Tratamentodediferentescamposdeformulários
<html>
<head>
<meta charset="utf-8" />
<title>Gerenciador de Tarefas</title>
<link rel="stylesheet" href="tarefas.css" type="text/css" />
</head>
<body>
<h1>Gerenciador de Tarefas</h1>
<form>
<fieldset>
<legend>Nova tarefa</legend>
<label>
Tarefa:
<input type="text" name="nome" />
</label>
<input type="submit" value="Cadastrar" />
</fieldset>
</form>
<table>
<tr>
<th>Tarefas</th>
</tr>
<?php foreach ($lista_tarefas as $tarefa) : ?>
<tr>
<td><?php echo $tarefa; ?> </td>
</tr>
<?php endforeach; ?>
</table>
</body>
</html>
Agoratemosapenaso foreachqueéumcódigoPHP,orestanteéapenas
HTML.Agoraficamaissimplesdeparaadicionarealterarasfuncionalidades,pois
osarquivosestãomenorese,oqueémaisimportante,estãocomsuasresponsabili-
dadesseparadas.
45

## Página 62

5.2. Adicionandomaisinformaçõesàstarefas CasadoCódigo
Devo separar meus projetos em v ários arquivos sem-
pre?
Estaéumaperguntadifícilearespostaéumpoucovaga:Depende.
Tudodependedotamanhoquesuaaplicaç ãoteráedoquantovocê
julgarquevaleapenainvestirumtemposeparandoosasresponsabilida-
desentreosarquivos.Nogeral,valebastanteapenafazerestaseparaç ão.
Vejaquenonossocasooprogramaaindaestábempequenoemesmo
assimaseparaçãodearquivosjámelhoroubastantenoentendimentodas
partes.
Nogeralnãoestamosperdendotempoquandoparamosparaorgani-
zarmelhorumprojeto.Essetempoinvestidoagorapodesetornaruma
grandeeconomiadetemponasfuturasmanuten çõesdocódigo.
5.2 Adicionando mais informações às tarefas
Paraquenossosistemadecontroledetarefasfiquemaisprático,vamosadicionar
algumasinformaçõesparamelhordescrevereorganizarastarefas.
Porenquantojátemosumtítuloparaatarefa,agoravamosadicionarumades-
crição,umprazoparaconclusão,umníveldeprioridadeeumaconfirmaç ãodeque
atarefajáestáconcluída.Paraisso,vamosadicionarosnovoscamposnoformulário
HTML:
...
<label>
Descrição (Opcional):
<textarea name="descricao"></textarea>
</label>
<label>
Prazo (Opcional):
<input type="text" name="prazo" />
</label>
<fieldset>
<legend>Prioridade:</legend>
<label>
<input type="radio" name="prioridade" value="baixa" checked />
46

## Página 63

CasadoCódigo Capítulo5. Tratamentodediferentescamposdeformulários
Baixa
<input type="radio" name="prioridade" value="media" />
Média
<input type="radio" name="prioridade" value="alta" />
Alta
</label>
</fieldset>
<label>
Tarefa concluída:
<input type="checkbox" name="concluida" value="sim" />
</label>
<input type="submit" value="Cadastrar" />
...
SevocêusaroCSSdosexemplos,seuformuláriodeveráficarparecidocomeste:
Figura5.1:Formuláriocompletoparaocadastrodetarefas
47

## Página 64

5.2. Adicionandomaisinformaçõesàstarefas CasadoCódigo
Olegaléquesóprecisamosalteraroarquivo template.php, enquantoo
tarefas.phpcontinuouomesmo.Osistemacontinuafuncionandoeapenasig-
noraosdadosadicionaisenviados.
Agoravamosalterartambémo tarefas.phpparapegarasnovasinformações.
Vamosusarocampocomonomedatarefacomoabaseparasabersedevemos
cadastrarumanovatarefa,jáqueonomedatarefaéaúnicainformaç ãoessencial
paranós.
Paraisso,vamosalteraraquele iflogoapóso session_start()etambém
seuconteúdo.Éclaroqueelevaificarmaior,poisagorasãovárioscamposquepre-
cisamospegardoformulárioenviado:
<?php
session_start();
if (isset($_GET['nome']) && $_GET['nome'] != '') {
$tarefa = array();
$tarefa['nome'] = $_GET['nome'];
if (isset($_GET['descricao'])) {
$tarefa['descricao'] = $_GET['descricao'];
} else {
$tarefa['descricao'] = '';
}
if (isset($_GET['prazo'])) {
$tarefa['prazo'] = $_GET['prazo'];
} else {
$tarefa['prazo'] = '';
}
$tarefa['prioridade'] = $_GET['prioridade'];
if (isset($_GET['concluida'])) {
$tarefa['concluida'] = $_GET['concluida'];
} else {
$tarefa['concluida'] = '';
}
48

## Página 65

CasadoCódigo Capítulo5. Tratamentodediferentescamposdeformulários
$_SESSION['lista_tarefas'][] = $tarefa;
}
...
Reparequeusamossempreafun ção isset()parasaberseosíndicesde $_GET
existem.Issoénecessáriopoisonavegadornãoenviaoscamposembranco,nemos
camposdesmarcados.
Agoraésóalteraratabelaparaexibirtodososdados:
<table>
<tr>
<th>Tarefa</th>
<th>Descricao</th>
<th>Prazo</th>
<th>Prioridade</th>
<th>Concluída</th>
</tr>
<?php foreach ($lista_tarefas as $tarefa) : ?>
<tr>
<td><?php echo $tarefa['nome']; ?> </td>
<td><?php echo $tarefa['descricao']; ?> </td>
<td><?php echo $tarefa['prazo']; ?> </td>
<td><?php echo $tarefa['prioridade']; ?> </td>
<td><?php echo $tarefa['concluida']; ?> </td>
</tr>
<?php endforeach; ?>
</table>
Acesseoformulárioecadastrealgumastarefas.Vejacomoficouaminhapágina
comduastarefascadastradas:
49

## Página 66

5.3. Conclusãodocapítuloedousodesessões CasadoCódigo
Figura5.2:Formulárioepáginacomnovoscamposparaocadastrodetarefas
5.3 Conclusão do capítulo e do uso de sessões
Nestemomentotemosumsistemadegerenciamentodetarefasjábeminteressante.
DuranteodesenvolvimentoatéaquijáforamusadasfuncionalidadesdoPHPpara
manterasessãoeparaincluirarquivoscomtrechosdecódigo.Gra çasaestasepara-
çãoemarquivosonossoprojetoficoumaislegíveleseparamosasresponsabilidades
decadaarquivo,umparatratarosdadoseoutroparaexibiroformulárioealistade
tarefas.
Nestaquestãodeseparaç ãodearquivospoderíamosiralém,separandoumar-
quivoparaoformulárioeoutroparaalistadetarefas.Masissoficaparavocêtestar
edecidirsevaificarmaisorganizadoousevaiseparardemaisasresponsabilidades.
Porenquanto,nossaaplicaç ãopermiteapenasaadiç ãodastarefasefunciona
apenasenquantoonavegadorestáaberto,poisquandotrocamosdenavegador,ou
quandoreiniciamosonavegadoratual,asessãoseperdeecomissoperdemosas
atividadescadastradas. Issoquerdizerqueassessõessãoruins? Não! Issoquer
dizerapenasqueelasnãoservemparaonossoproblemaatual,queéguardaralista
detarefaseacessardeoutronavegadorsemperderosdados.Masemcenáriosonde
énecessário,porexemplo,guardarologindousuário,umasessãoéideal.
50

## Página 67

CasadoCódigo Capítulo5. Tratamentodediferentescamposdeformulários
5.4 Resumo
Nestecapítuloadicionamosnovoscamposaoformuláriodastarefasetratamosestes
camposatravésdoPHP.Umpontobemimportantefoiaseparaç ãodoprograma
emmaisdeumarquivo,sendoquecadauméresponsávelporumapartedogeral,
tornando-semenoremaissimplesparamanter.
Nospróximoscapítulosvamospassaraguardarosdadosemumbancodedados.
5.5 Desafios
Agora,maisalgunsdesafiosparatreinareevoluir:
• Continuealistadecontatosqueestánosdesafiosdocapítuloanterior.Além
donome,dotelefoneedoe-maildecadacontato,adicioneumcampopara
descrição,umparaadatadenascimentoeumcheckboxparadizerseocontato
éfavoritoounão.
• Separeasresponsabilidadesdalistadecontatos,mantendoumarquivopara
cada,assimcomofizemosnalistadeafazeres.
51

## Página 69

Capítulo6
Acessandoeusandoumbancode
dados
Nosúltimoscapítulosconstruímosumalistadetarefasquefuncionamuitobem
quandousamosapenasumnavegadoremantemosasessãosempreaberta. Paraa
nossaaplicaçãoestenãoéocenárioideal,porissoénecessárioguardarnossosdados
emumlocalmaisadequado,deondevamosconseguirrecuperá-lossemprequene-
cessário,mesmoestandoemoutronavegadoroufechandoonavegadoreabrindo-o
novamente.
Épararesolverestetipodeproblemaqueentraobancodedadose,nonosso
caso,ofamosoMySQL.
Comonossaaplicaç ãojátemumaestruturabacanaejáfuncionabemusando
assessões,oqueprecisamosfazerétrocarousodassessõespelousodobancode
dados.Porisso,vamoscome çarporcriarobancodedados,definindoquaisdados
queremosguardarefaremoscomqueoPHPseconecteaobancoparapoderinserir
erecuperaressesdados.

## Página 70

6.1. ObancodedadosMySQL CasadoCódigo
Amanipulaçãodobancodedadoséfeitacomautilizaç ãodeoutralinguagem,
aSQL,quenospermiteexecutarcomandosparainserir,pesquisareremoverdados,
fazerrelatóriosetc.NestelivroveremosapenasumbásicosobreaSQL,focandomais
noscomandosnecessáriosparaodesenvolvimentodosprojetos.Sevocêaindanão
temfamiliaridadecomSQL,recomendoquetambéminvistaumtempoestudando
estalinguagem,poisvocêpoderáusarSQLparatrabalharcomdiversosbancosde
dadosalémdoMySQL,integrandocomváriasoutraslinguagensdeprogramaç ão
alémdoPHP.
6.1 O banco de dadosMySQL
MySQLéumsoftwarelivreparabancodedados.Issosignificaquevocêpodeusaro
MySQLemseusprojetoseaindapodecontribuircomodesenvolvimentodopróprio
MySQL,seassimdesejarounecessitar.
OMySQLébastanteusadoemaplicaçõeswebporsuaversatilidadeeporser
suportadoemdiversasplataformasediferenteslinguagens.
Porpadrão,oMySQLnãotemumainterfacegráficaparaadministraç ãoeuti-
lização,masépossívelencontrardiversasferramentasquefazemestetipodetraba-
lho,sendoqueumadasmaisconhecidaséoMySQLWorkbench.Nãousaremoso
MySQLWorkbench,masvocêpodepesquisarmaissobreestesoftwareeusá-lopara
administrarseusbancosMySQL.
6.2 Instalando o MySQL
ComojáfizemosainstalaçãodoXAMPP,oMySQLveiojunto.Então,sóprecisamos
usaroPainelnoXAMPPparainiciaroserviço. Fiquesempredeolhoparaverse
nãoénecessárioliberaroserviçodoMySQLnofirewall.
MySQL noLinux
ParaquemusaLinux,maisespecificamenteosderivadosdoDebian
edoUbuntu,bastainstalaroMySQLcomoseguintecomando:
sudo apt-get install mysql-server
UsuáriosdeMacOSXqueinstalaramoXAMPPpoderãoiniciaro
MySQLusandoopaineldoXAMPP.
54

## Página 71

CasadoCódigo Capítulo6. Acessandoeusandoumbancodedados
6.3 PHPMyAdmin, administrando o banco de dados
AinstalaçãodoXAMPPcontémumaferramentamuitointeressanteparaagestãode
bancosMySQL,oPHPMyAdmin.EstaéumaferramentaescritaemPHPusadapara
gerenciaroMySQL,comop çõesparacriarnovosbancos,usuários,tabelas,inserir,
pesquisareremoverregistrosetc.
Instalação do PHPMyAdmin
SevocêoptoupeloXAMPP,oPHPMyAdminjáveminstaladoe
prontoparausar.Casoasuainstalaç ãonãosejacomoXAMPP,ouou-
trospacotesnesteestilo,vocêtambémpoderábaixaroPHPMyAdmin
emseusiteoficial: http://www.phpmyadmin.net/
CasovocêuseUbuntu,DebianououtrasdistrosLinux,procurepelo
pacotedoPHPMyAdmin.NoDebian/Ubuntubastausaroaptparafazer
ainstalação:
apt-get install phpmyadmin
SevocêoptoupeloXAMPP,seránecessárioiniciaroserviçodoMySQLpara
poderacessaroPHPMyAdmin. Paraisso,acesseopaineldoXAMPPecliquena
opção StartnoserviçoMySQL:
Figura6.1:PaineldoXAMPP,cliqueemStartnoserviçoMySQL
55

## Página 72

6.3. PHPMyAdmin,administrandoobancodedados CasadoCódigo
Lembre-sedequepodesernecessárioautorizaroserviçonofirewalldoWin-
dows.Seesteforocaso,eleiráabrirumajanelapedindoautorizaç ão.
ParaacessarPHPMyAdminutilizeoendere çohttp://localhost/phpmyadmin.
Vocêpoderáverumapáginaparecidacomesta:
Figura6.2:PáginadelogindoPHPMyAdmin
NestapáginavocêpodeescolheroidiomaparausaroPHPMyAdmin. Acesse
seuPHPMyAdminusandoousuário rooteasenha root.
Atenção! O XAMPP pode entrar direto na página de administração do
PHPMyAdmin,sempedirumasenha!Issoénormalemalgumasversõesdele.
Apósacessarvocêveráumapáginacomoesta:
56

## Página 73

CasadoCódigo Capítulo6. Acessandoeusandoumbancodedados
Figura6.3:PáginainicialdoPHPMyAdmin
6.4 C riando o banco de dados
Vamoscriarumnovobancodedados.Sevocêescolheuoidiomaportuguêsnapá-
ginadelogin,selecioneaop ção Bancos de dados.Napróximapáginadigiteo
nomedobancodedados,queserá tarefas,nacaixadeentrada Criarbancodeda-
dos.Naop ção Colação,ou Collation,selecioneaop ção utf8_general_ci.
Figura6.4:FormulárioparacriarumnovobancodedadosnoMySQL
Agora,bastaclicarnobotão Criareonovobancodeveaparecernomenuà
esquerda:
57

## Página 74

6.5. Criandoatabela CasadoCódigo
Figura6.5:Vejaobanco‘tarefas’nalistadosbancos
Clicandononome,seremosinformadosdequeobancoaindanãopossuitabelas.
6.5 Criando a tabela
Nossoprojetoéumgerenciadordetarefas,entãovamosprecisarapenasdeuma
tabelacomoscamposnecessáriosparaguardarosdadosquejátemosnosarraysde
tarefasdentroda $_SESSION.Nossatabeladeveráficarassim:
58

## Página 75

CasadoCódigo Capítulo6. Acessandoeusandoumbancodedados
Figura6.6:Modelagemdatabelatarefas
Reparequeatabelaémuitoparecidacomosarraysquearmazenamastarefas,
asdiferen çassãopequenas,comoocampo ideoscampos nome,quefoidefinido
comaté20caracteres,e prioridadequeéumnúmerointeiro.
Ocampo idseráumaidentificaçãoúnicadasnossastarefaseseráumnúmero
crescente.Dessaformateremosatarefa1,2,3eassimpordiante,semnuncarepetiro
número.Issoéimportanteparaidentificarmosastarefasenãomisturarmosquando
precisarmosfazerreferênciaaumatarefa.Imaginequeusássemosocampo nome
paraisso,fatalmenteteríamosduastarefascomomesmonome,eissoatrapalharia
nahoradesaberqualéqual.
Ocampo nomeagoratemumlimitedeaté20caracteres.Issoéalgocomumem
bancosdedados.Jáquenãoprecisamosdenomesmuitograndesparaastarefas,20
caracteresdevemsersuficientes.
Ocampo prioridadeéumnúmerocomapenasumalgarismo.Vamosusar
destaformapoisficamaissimplesguardarnobancoasprioridades1,2e3,emvezde
baixa,médiaealta.Issotambémébastantecomumembancosdedados,poisreduz
oespaçoutilizadoeficafácildecontrolarnaaplicaç ão.
Existemduasmaneirasdecriaratabela,aprimeiraéexecutandodiretamente
ocódigoSQLasegundaéusandoainterfacedoPHPMyAdmin. Voumostrara
primeiraop çãopoisexigemenospassose,acredite,émaissimplesdepoisquese
aprendeumpoucodeSQL.
UsandooPHPMyAdmineestandocomobanco tarefasselecionado,clique
naaba SQLevocêveráumapáginacomumcampoparadigitarcomandosSQL.A
páginaéparecidacomesta:
59

## Página 76

6.5. Criandoatabela CasadoCódigo
Figura6.7:CampoparadigitarcomandosSQL
Ocódigoparaacriaç ãodatabelaéeste:
CREATE TABLE tarefas (
id INTEGER AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(20) NOT NULL,
descricao TEXT,
prazo DATE,
prioridade INTEGER(1),
concluida BOOLEAN
);
Digiteestecódigonocampoecliquenobotão executar.Comisso,atabela
serácriadaejáconseguiremosmanipularseusdados.
60

## Página 77

CasadoCódigo Capítulo6. Acessandoeusandoumbancodedados
6.6 C adastrando e lendo os dados de uma tabela
Comatabelapronta,podemostreinarumpoucomaisdeSQLantesdefazerain-
tegraçãocomoPHP.VamosusarSQLparaadicionardadosnatabela.Ocomando
usadoparainserirosdadosemumatabelaéo INSERTeneledevemosinformar
quaissãooscamposquequeremospreenchereseusvalores.
SemprequequisermosexecutarcódigosSQLusandooPHPMyAdmin,basta
acessarmosobancoeusaraaba SQL.Agoravejaumexemploparainserirosdados
deumatarefanatabela tarefas:
INSERT INTO tarefas
(nome, descricao, prioridade)
VALUES
('Estudar PHP', 'Continuar meus estudos de PHP e MySQL ', 1)
Apósinserirosdados,useobotão Executar.
Reparenaestruturadocomando:nósestamosdizendoparaoMySQLquaisos
camposquequeremospreencher,quenãosãotodososcamposdatabela. Neste
caso,oscamposquenãopreenchermos,serãovazios.Aten ção,émuitoimportante
manteramesmasequênciadoscamposinformadoseseusvalores.Vejaqueestamos
colocandoamesmasequênciade nome,descricaoeprioridadenalistadecampos
etambémnalistadevalores.
Agora,vamosselecionarosdadosdatabela.Ocomandoparaselecionarosdados
éo SELECT.Coloqueocomandonacaixadetextonaaba SQL:
SELECT * FROM tarefas
ComissooPHPMyAdminiráparaumanovapáginacomoresultadodapes-
quisa,parecidacomapróximaimagem:
Figura6.8:ResultadodoSELECT
Nocomando SELECTnósinformamosquaiscamposqueremos,nocaso,useio
asterisco,quesignifica todososcampos,mastambémpodemosindicaroscampos
quequeremos.Faç ao SELECTabaixoparabuscarapenasdoiscamposdatabela:
61

## Página 78

6.7. FiltrandoosresultadosdoSELECT CasadoCódigo
SELECT nome, prioridade FROM tarefas
Agoraoresultadoserácomapenasoscampos nomee prioridade.
Adicionemaisalgumastarefasnatabela,usandoocomando INSERTquevimos
hápouco. Eucadastreiquatrotarefas. Omeu SELECT,comoscampos nome,
descricaoe prioridadetrouxeesteresultado:
Figura6.9:ResultadodoSELECTcommaislinhas
Umacuriosidadeinteressanteéque SQLnãoteobrigaaescreveroscomandos
dalinguagem,como SELECT, INSERTetc.,usandocaixaalta,maséinteressante
manterestepadrãopoissimplificaaleitura. VejaquenosnossoscódigosSQLaté
aquiexistemcomandoscomoo FROMeo VALUES,queeunãonecessariamentedisse
paraqueservem,mascomoelesestãoemcaixaalta,vocêconseguiuleroscomandos
ededuziroqueédalinguagemeoquesãonossosdados.Então,mantenhaseuSQL
comaspalavrasdalinguagememcaixaalta,vaifacilitarparavocêeparaoutras
pessoasleremseucódigoeentenderoqueelefaz.
6.7 Filtrando os resultados do SELECT
Usandoo SELECTpodemosfiltrarosresultadosdabusca,porexemplo,sequiser-
mosexibirastarefascomaprioridade1,faremosoSQLassim:
SELECT nome, descricao, prioridade FROM tarefas
WHERE prioridade = 1
Oresultadodeveseralgosimilaraisso:
Figura6.10:ResultadodoSELECTfiltrandocomaprioridade1
62

## Página 79

CasadoCódigo Capítulo6. Acessandoeusandoumbancodedados
Tambémpodemosfiltrarporumtextoqueestejadentrodeoutrotexto,paraisso
usamosainstruç ão LIKEdoSQL:
SELECT nome, descricao, prioridade FROM tarefas
WHERE nome LIKE '%php%'
O LIKEaceitaousodaquelessinaisdeporcentagem. Elesservemparadizer
algocomo:
Procureporqualquercoisa,seguidodephp,seguidodequalquercoisa
Então,seanossapesquisafosseassim:
SELECT nome, descricao, prioridade FROM tarefas
WHERE nome LIKE 'php'
Elanãoteriaresultados. Consegueentenderomotivo? Sepensarumpouco
ficasimples.Nestecaso,elepesquisaresultadosnosquaisocampo nomesejaigual
a php,semtextosantesoudepois.Tambémpodemosusaraporcentagemapenas
antesouapenasdepoisdeumtexto.
Nopróximocapítulovamosfazeraconexãodanossaaplicaç ãoPHPcomobanco
MySQL.
6.8 R esumo
NestecapítulousamosalinguagemSQLparamanipulardadosemumbancodeda-
dosMySQL.OMySQLpodeserinstaladoàparte,oujuntocomopacotedoXAMPP.
UsamostambémoPHPMyAdmincomoferramentaparaacessarobancoatravésdo
navegador.
Paramanipularobancodedadosusamosainstruç ão CREATE TABLEparacriar
umatabela, INSERT INTOparacadastrardadosemumatabela, SELECTparabus-
carosdadosdatabelaetambémfiltramososresultadosdo SELECTusando WHERE
e LIKE.
6.9 D esafios
Horadealgunsdesafios,dessavezvoltadosparabancosdedadoseparaalinguagem
SQL:
• Façamaistestescomo SELECT,o WHEREeo LIKEusandoobanco tarefas.
63

## Página 80

6.9. Desafios CasadoCódigo
• Crieumbancochamadocontatosparaguardarosdadosdoscontatosdo
desafioiniciadonosdesafiosanteriores.Qualtabelaseránecessáriaparaeste
banco?Quaiscamposserãonecessáriosparacadastrarosdadosquejáestão
sendocapturadospeloformulário?Nãoseesque çadedeixarumcampo id
paraguardarachavequeidentificaráumcontatocomoúnico,assimcomofoi
feitoparaastarefas.
• Crieumbancochamadoestacionamentoparacadastrarosveículosesta-
cionados.Nestebancocrieumatabelachamada veiculoscomoscampos
id, placa, marca, modelo, hora_entradae hora_saida. Decida
ostiposdedadosquedevemserusadosparacadacampo. Cadastrealguns
veículosetentefazerpesquisas,comobuscartodososveículosdeumamarca.
64

## Página 81

Capítulo7
IntegrandoPHPcomMySQL
Nocapítuloanterior,criamosobancodedadoseumatabelaparaguardarosregis-
trosdenossastarefas.Alémdisso,inserimosalgumastarefasnobancoeusamosas
buscasdalinguagemSQLparaselecionarastarefasnobancoefiltrarpelonomee
pelaprioridade.Nestecapítulo,iremosfinalmenteconectaroPHPaoMySQL!Como
játemosaaplicaçãopronta,masusandosessões,eobancopronto,nossatarefaserá
menoscomplexa,poisteremosquealterarapenasalgumaspartesdaaplicaç ão.
7.1 PHPeMySQL
PHPeMySQLjásãovelhosamigos.Ébemcomumencontraraplicaçõesquefazem
usodestastecnologiasemconjunto.Desdepequenossitespessoais,atégrandessis-
temasdegestãoelojasvirtuais,awebestárepletadecasosdesucessodestaparceria.
Oquetornaestaparceriatãoforteeestáveléumacombinaç ãodefatores,como
ofatodeoMySQLserumbancofácildeaprender,leveerápido,oPHPserfácil
eflexíveleambospossuíremlicen çaspermissivasparausopessoal,comercialeem
projetosdesoftwarelivre.

## Página 82

7.2. ConectandoaoMySQL CasadoCódigo
PHPtornasimplesousodoMySQLatravésdefun çõesqueconectam,executam
códigoSQLetrazemosresultadosparaaaplicaç ão.Eéexatamenteissoquefaremos
agora!
7.2 Conectando ao MySQL
Primeiro,vamosfazerapartemaissimples,queéconectaraobancoebuscaros
dadosqueestãocadastradosnele.
OprimeiropassopararealizaraconexãocomoMySQLécriarumusuáriono
MySQLparaqueoPHPpossaseautenticar. Esteéumpassoimportanteeajuda
amanterobancodedadosmaisseguro. Écomoaqueleusuárioesenhaquevocê
precisadigitarquandoligaocomputador,ouquandovaiacessarseue-mailouainda
oseuperfilemumaredesocial.
ParacriarousuárionoMySQL,acesseoPHPMyAdmineselecioneobanco
tarefase,estandonele,useaop ção Privilégiosnomenusuperior.Napágina
queabrir,cliquenaop ção Adicionar usuário—umajanelaabrirápedindoos
dadosdonovousuário.Eupreenchioscamposconformeaimagemaseguir:
Figura7.1:CriaçãodeusuárionoMySQL
Nocamponovousuárioinformei sistematarefa,nasenhadigitei sistemaecon-
firmei,depoiscliqueinobotão Adicionar usuário.
66

## Página 83

CasadoCódigo Capítulo7. IntegrandoPHPcomMySQL
Apósaadiç ãodousuário,teremosumusuáriochamado sistematarefacoma
senhasistema.EstessãoosvaloresqueinformaremosaoPHP.
Agoravamoscriarumnovoarquivoparafazeraconexãocomobanco.Eleserá
gravadonamesmapastadosarquivosdalistadetarefa,ousejaapasta tarefas,e
seunomeserá banco.php:
<?php
$bdServidor = '127.0.0.1';
$bdUsuario = 'sistematarefa';
$bdSenha = 'sistema';
$bdBanco = 'tarefas';
$conexao = mysqli_connect($bdServidor, $bdUsuario, $bdSenha, $bdBanco);
if (mysqli_connect_errno($conexao)) {
echo "Problemas para conectar no banco. Verifique os dados!";
die();
}
Noarquivo,estamoscriandoquatrovariáveisqueguardamoendere çodoservi-
dorMySQL(queéanossamáquina),onomedeusuário,asenhadeacessoeonome
dobancoquequeremosacessar.Élegalmanterestesdadosemvariáveis,poissefor
necessárioalterar,alteramosapenasacriaç ãodavariável,semterqueprocuraronde
elaestásendousada.
Reparequenocódigodoarquivo banco.phpexistemapenasduasfun çõesque
nãousamosatéagora.Afun ção mysqli_connect()recebeosdadosdeconexão
comobancoeabreaconexão. Estaconexãoéguardadanavariável $conexaoe
vamosprecisardestavariávelsemprequeformosinteragircomobanco. Aoutra
funçãoéa mysqli_connect_errno()quepegaumaconexãoeverificasehouve
errosdeconexão.Nestecaso,afun çãoestádentrodeum if,paraverificarsehouve
errosounão. Ah,temmaisumafun çãonovaali,afun ção die(),quefazoque
onomediz:elamataoprogramaalimesmo,semlerocódigoqueexistemaispara
frente.
67

## Página 84

7.3. Buscandodadosnobanco CasadoCódigo
Sempre ouvi falar de mysql_connect()
TalvezvocêjátenhavistoalgumtextosobrePHPeMySQLemquea
funçãodeconexãoeraa mysql_connect().Estafun çãoexiste,assim
comováriasoutrasfun çõesquecome çamcom mysql_,maselasserão
removidasdoPHPembreve.Porisso,oidealéusarsempreanovaeme-
lhoradaversãodabibliotecaMySQLdoPHP,aMySQLi.Nogeral,basta
adicionaraletra inosnomesdefun çãoMySQLeumparâmetroaqui
ouali,quetudofuncionabem,masexistemalgumasdiferen çasentre
asbibliotecas.Então,adicaé: sempreuseaversãonovadabiblioteca
MySQLparaPHP.Sempre.
Vamosfazerumapequenaexperiênciacomaconexãoaobanco. Acesseoar-
quivobanco.phpdiretamentepelonavegador,noendere ço:http://localhost/tarefas/
banco.php.Vocêdeveráverapenasumapáginaembranco,oqueébom,significa
queaconexãofuncionou.Agora,experimentemudarocampodesenhadaconexão
paraumasenhaincorretaeacesseoarquivonovamente.Vocêveráafrase Problemas
paraconectarnobanco.Verifiqueosdados! .Ouseja,nossocódigodeconexãoestá
funcionaletambémexibeerroscasonãoconsigaconectar.
O erro de conexão aparece sempre, mesmo com os dados
corretos
Vocêpoderápassarpeloproblemadoerrodeconexãodevezem
quando.Casoissoaconte ça,verifiqueseoservidordoMySQLestáativo
nopaineldecontroledoXAMPP,ouemoutraferramentaquevocêuse
paragerenciaroMySQL.Umaoutraformadeverificarseobancoestá
funcionandonormalmenteéacessandooPHPMyAdmin.Seeletambém
nãoconseguirconectar,obancopoderáestarmesmodesligado.
7.3 Buscando dados no banco
Apróximaalteraç ãoquefaremosemnossoprogramaéfazercomqueelebusqueas
tarefascadastradasnobancodedadosenãomaisnasessão.Paraisso,abraoarquivo
tarefas.phpeacheotrechoqueverificaseasessãoexisteparacolocarnalistade
tarefas,oucriaumalistavazia,casoasessãonãoexista.Otrechoéeste:
68

## Página 85

CasadoCódigo Capítulo7. IntegrandoPHPcomMySQL
<?php
...
if (isset($_SESSION[ 'lista_tarefas'])) {
$lista_tarefas = $_SESSION['lista_tarefas '];
} else {
$lista_tarefas = array();
}
...
Estetrechoseráeliminado! Nolugardele,ficaráapenasumanovalinhaque
chamaumafun çãoqueretornaráastarefascadastradasnobanco:
<?php
...
$lista_tarefas = buscar_tarefas($conexao);
Éclaroqueafun ção buscar_tarefas()aindanãoexiste,porissoiremos
criá-ladentrodoarquivo banco.php. Então, abriremosnovamenteoarquivo
banco.phpenofinaldelevamoscolocaranovafun ção.Masantesdeescrevê-la,
precisamosplanejarumpoucooseufuncionamento.
Afun ção buscar_tarefas()deveráusarumaconexãocomobancopara
executarcomandosSQLquebusquemalistadetarefas.Apósbuscarastarefas,ela
deverácriarumarraycomosdadosdastarefaseentãodeveráretornaressesdados.
Certo,planejandoassimficamaissimplesalcan çarnossoobjetivo.Comojáte-
mosumavariávelcomaconexãocomoMySQL,poderemosusá-la.Vamosaocódigo
dafun ção:
<?php
...
function buscar_tarefas($conexao)
{
$sqlBusca = 'SELECT * FROM tarefas';
$resultado = mysqli_query($conexao, $sqlBusca );
$tarefas = array();
69

## Página 86

7.3. Buscandodadosnobanco CasadoCódigo
while ($tarefa = mysqli_fetch_assoc($resultado )) {
$tarefas[] = $tarefa;
}
return $tarefas;
}
Nestafun çãofoicriadaumavariávelcomocomandoSQLqueirábuscaros
dadosnobanco,nocasoocomando SELECT * FROM tarefas.Logodepois,a
função mysqli_query()usaavariávelcomaconexãoeavariávelcomocomando
parairaobanco,executarocomandoetrazeroresultado.Esteresultadoficaarma-
zenadonavariável $resultado.Nasequência,écriadaavariável $tarefas,que
éapenasumarrayvazio. Opróximoblocoéo while,queéexecutadoatéquea
função mysqli_fetch_assoc()tenhapassadoportodasaslinhasdoresultado,
sendoquecadalinhadoresultadoéarmazenadanavariável $tarefa,nosingular,
paradiferenciardoarray $tarefas. Eentãotemos,finalmente,o returnque
devolveosdadosparaquemchamouafun ção.
Agorapodemosatualizarapágina tarefas.phpeveroresultado. Acesseo
endereçohttp://localhost/tarefas/tarefas.phpevejaoqueacontece.Umerro!Elediz
queafun ção buscar_tarefas()nãoexiste!Masnósacabamosdeescrevê-la.
Analisandooproblemaéfácilidentificarqueoarquivo tarefas.phptemum
includeapenasnofinalparaoarquivo template.php.Comoelenãosabedaexis-
tênciadoarquivo banco.php,elegeraoerro.Vamoscorrigiroproblemaadicio-
nandoumincludeparaoarquivo banco.php.Estenovo includeseráadicionado
nocome çodoarquivo,logoapósafun ção session_start():
<?php
session_start();
include "banco.php";
...
Agorasim,atualizeapáginaevocêveráqueelaexibeosdadoscadastradosno
banco!Vejacomoficouaminha:
70

## Página 87

CasadoCódigo Capítulo7. IntegrandoPHPcomMySQL
Figura7.2:Listandoastarefascadastradasnobancodedados
A importância de uma boa estrutura
Vejacomoconseguimosalteraranossalistadetarefasparapegaros
dadosdobancocomapenasalgumasalteraçõespontuais.
Issofoipossívelpoisanossaaplicaç ãotemumaestruturaquefavorece
essetipodealteraç ãoeatémesmoumcrescimentomaissaudável.
Veja a geração da lista de tarefas, por exemplo. Se estivéssemos
usandoasuperglobal $_SESSIONdiretamentelá,aalteraçãoseriamais
complicadaenoscustariamaistempo,alémdepodergerarmaiserros.
Mas,comoestamosusandoumarraychamado $lista_tarefas,bas-
toualteraraformacomoestearrayégerado. Reparequenemmesmo
precisamostocarnoarquivo template.php.
Nãosepreocupesevocênãoconseguircriarestruturasassimlogono
começodoseuaprendizado.Maslembre-sedesempreestudaremelho-
rarseuscódigosdepoisde“finalizar”,poisumsoftwaredificilmentevai
ficar“pronto”.
71

## Página 88

7.4. Cadastrandoastarefasnobanco CasadoCódigo
7.4 Cadastrando as tarefas no banco
Bem,agoraquejáestamosbuscandoastarefasnobanco,échegadaahoradecadas-
trarmosmaistarefasusandoonossoformulário.Seráqueaquitambémserápossível
fazerpequenasalteraçõesparatermososdadossendoenviadosparaobanco,nolu-
gardeusarsessões?Analisandoocódigonoarquivo tarefas.php,conseguimos
verquealinharesponsávelporcolocaratarefanasessãoéesta:
<?php
...
$_SESSION['lista_tarefas'][] = $tarefa;
...
Essalinhacolocanasessãoavariável $tarefa,queéumarraycomosdados
datarefa.Estearrayéexatamenteoqueprecisamosparaenviarnossastarefasparao
bancodedados!Assimcomofizemoscomotrechoquebuscavaastarefasnasessão,
vamostrocarestalinhaporumachamadaaumanovafun çãoqueirágravarosdados
nobanco.Troquealinhaqueacabamosdeverporesta:
<?php
...
gravar_tarefa($conexão, $tarefa);
...
Afun ção gravar_tarefa()receberáaconexãoquejátemos,navariável
$conexao, etambémanossatarefa, queestánoarray $tarefa. Masafun-
ção gravar_tarefa()nãoexiste,entãoprecisamosadicioná-la. Faremosisso
noarquivo banco.php,poiseleestácomorestantedocódigoresponsávelpela
comunicaçãocomobancoMySQL.Nofinaldoarquivoiremosadicionarafun ção
gravar_tarefa():
<?php
...
function gravar_tarefa($conexao, $tarefa)
{
$sqlGravar = "
72

## Página 89

CasadoCódigo Capítulo7. IntegrandoPHPcomMySQL
INSERT INTO tarefas
(nome, descricao, prioridade)
VALUES
(
'{$tarefa['nome']}',
'{$tarefa['descricao']}',
{$tarefa['prioridade']}
)
";
mysqli_query($conexao, $sqlGravar);
}
VejaqueestecódigofazoquefizemoslánoPHPMyAdmin,adiferen çaéqueele
colocaasvariáveisdoPHPparapreencherocódigoSQL.Nãoseesque çadecolocar
asvariáveisPHPdentrodaschavesquandoestivercolocandooconteúdodasvariá-
veisdentrodeoutrasstrings. Uma stringéumasequênciadecaracteres,ouseja,
asnossasvariáveiscomtextossãovariáveiscomstrings.Nãodeixederepararque
abrimosastring $sqlGravarnalinhaondeelaédeclaradaeafechamosnalinha
depoisdocódigoSQL.
Nestafun çãotambémfizemosousodafun ção mysqli_query(),poiselaé
bemversátil,servindoparabuscardadosetambémparagravardados.Naverdade
afun ção mysqli_query()serveparaexecutarcódigoSQL,entãoeladevolveda-
dosquandofizermos,porexemplo,um SELECT,ouapenasinseredadosquando
executadosumINSERT.
Bem,aaplicaçãojáestáquaseokparafuncionarusandoobanco.Masaindaéne-
cessáriaumaalteração!Onossoformuláriotemocampoparaadefiniraprioridade
datarefaeestecampoestácomosvalores baixa,mediaealta,masatabela tarefas
nobancodedadosnãoestápreparadaparaestesvalores,poisdecidimosusarnúme-
rosparadefinirasprioridades.Sendoassim,altereoformulárioparaqueosvalores
dasprioridadesfiquemcomo 1,2e3,respectivamente,lembrandoqueoformulário
estánoarquivo template.php:
...
<legend>Prioridade:</legend>
<label>
<input type="radio" name="prioridade" value="1" checked /> Baixa
<input type="radio" name="prioridade" value="2" /> Média
73

## Página 90

7.4. Cadastrandoastarefasnobanco CasadoCódigo
<input type="radio" name="prioridade" value="3" /> Alta
</label>
...
Muitobem,agoraacesseapáginaem http://localhost/tarefas/tarefas.phpetente
cadastrarumatarefa.Eucadastreiumanovaeaminhalistaficouassim:
Figura7.3:Cadastrandoumanovatarefaatravésdoformulário
Agora,precisamosexibircorretamenteasprioridadesnalistadetarefas,pois1,2
e3devemserusadosapenasnobancoeaaplicaç ãodeveexibirsemprecomo baixa,
médiaealta.
A linha que precisamos alterar é a que exibe a prioridade no arquivo
template.php:
...
<td><?php echo $tarefa[ 'prioridade']; ?> </td>
...
Adicionaralguns ifspodemresolveronossoproblema,masvãodeixarnosso
templatemaisdifícildeserlido.Vejacomoficaseadicionarmosalogicanecessária
paraexibirosnomesdasprioridadesdiretamentenotemplate:
<td><?php
if ($tarefa['prioridade'] == 1) { echo 'Baixa'; }
if ($tarefa['prioridade'] == 2) { echo 'Média'; }
if ($tarefa['prioridade'] == 3) { echo 'Alta'; }
?> </td>
Nãoestáassimtãoruim,masvejacomoestaoutramaneiraficabemmaislegível
efácildeentender:
74

## Página 91

CasadoCódigo Capítulo7. IntegrandoPHPcomMySQL
<td><?php echo traduz_prioridade($tarefa[ 'prioridade']); ?> </td>
Bem mais simples, não? Claro que neste caso é necessário criar a função
traduz_prioridade()ecolocarnelaos ifs,masagrandequestãoaquiéqueo
arquivo template.phpficamaissimpleseenxuto,muitomaisfácildeentender.
Pegueoarquivo banco.phpcomoexemplo:neleexistemasfun çõesquecri-
amosparalidarcomobancodedados.Graç asaissoorestantedanossaaplicaç ão
precisaapenaschamaressasfun çõesenãosepreocuparemescreverSQLparaexe-
cutarnobanco.
Vamoscriarumnovoarquivochamado ajudantes.php.Eleiráconterfun-
çõesquenosajudarãoempequenastarefas,comoestecasodetraduzirocódigoda
prioridadeparaonomedela.Oconteúdodoarquivo ajudantes.phpseráapenas
afun ção traduz_prioridade(),porenquanto,poislogomaisiremoscolocar
maisfun çõesnestearquivo:
<?php
function traduz_prioridade($codigo)
{
$prioridade = '';
switch ($codigo) {
case 1:
$prioridade = 'Baixa';
break;
case 2:
$prioridade = 'Média';
break;
case 3:
$prioridade = 'Alta';
break;
}
return $prioridade;
}
Reparequenafun ção traduz_prioridade()utilizamosumanovainstruç ão
doPHP,aswitch/case.Estainstruç ãoserveparaoscasosemqueumavariávelpode
terdiversosvaloresecadavalorsignificaumfluxodiferenteparaoprograma.Você
deveestarpensandoqueomesmoresultadopoderiaserobtidousandoalguns ifs,e
vocêestácerto.Mastenteescreverestafun çãousadoapenas ifeelse,vocêveráque
75

## Página 92

7.4. Cadastrandoastarefasnobanco CasadoCódigo
elaficarámaioremaiscomplexadeseentender.Nocasodo switch/caseasop ções
ficammaisclarasedefácillocalizaç ão.
Masoswitch/casenãopodeserusadoemcasosnosquaisprecisamoscomparar
seumvalorémaioroumenorqueoutro.Usando ifpodemoscolocarumacondiç ão
como“$variavel < 10”,algoimpossívelnocase,quesóaceitavaloresfixos.É
comoseno ifsósepudesseusar“$variavel == 10”.
Comafun ção traduz_prioridade()pronta,precisamosdizerparaanossa
aplicaçãoqueelaexiste.Paraisso,noarquivo tarefas.php,vamosadicionarmais
umainstruçãoinclude,logoabaixodainclusãodoarquivo banco.php:
<?php
session_start();
include "banco.php";
include "ajudantes.php";
...
Atualizeapáginaevocêdeveráverasprioridadescomosnomesenãomaiscom
oscódigos.
Ajudantes?
ÉbemcomumencontraremaplicaçõesPHP,oudeoutraslinguagens,
arquivos,pacotes,módulosetc.,comonomede helpers,quesignifica
exatamenteajudantes.
Emgeral,estesarquivoscontêmpequenostrechosdecódigoparaau-
xiliaremtarefasrecorrentes,comononossocasodeexibirotipodepri-
oridadeouaformataç ãodedatas,queveremosaindanestecapítulo.
Você também pode agrupar os ajudantes para determi-
nadas tarefas em arquivos separados. Alguns exemplos se-
riam ajudantes para desenhar tabelas em um arquivo chamado
ajudantes_tabelas.php ou um para criar formulários em um
arquivo ajudantes_formularios.php.Tudovaidependerdassuas
necessidadeseorganizaç ãodocódigo.
76

## Página 93

CasadoCódigo Capítulo7. IntegrandoPHPcomMySQL
7.5 Cadastrando o prazo das atividades
Atéomomento,estamosgravandonobancoapenasonome,adescriç ãoeapriori-
dadedastarefas.Vamosagoraincluiroprazo.
Esteéumcampoquevaidarumpoucomaisdetrabalho,poisnoBrasilnós
usamosadatanoformatoDIA/MÊS/ANO,masparaoMySQLoformatodadataé
ANO-MÊS-DIA.Porissovamosprecisardedoistradutores:umparapegaradata
quedigitarmosetraduzirparaoformatodoMySQLeoutroparapegaradatado
MySQLetraduzirparaexibirnalistadetarefas.
Emprogramaçãosempreexistemdiversasmaneirasdeseresolverumproblema.
Nestecasonãoédiferente,poispodemostransformarasdatasusandodiversastéc-
nicasdiferentes. Atécnicaquefaremospodenãoseramelhorouamaiselegante,
masvairesolveronossoproblemaeficarábemsimplesdeentender.
Vamosanalisarmelhoroproblema.Nosdoisformatosdedatatemososmesmos
valores,masemposiçõesdiferenteseusandoseparadoresdiferentes. Então,oque
precisamosfazeréarrumarumaformadesepararosvaloresereconstruirastring
colocandocadavaloremsuaposiç ãousandoosseparadoresesperados,quepodem
serbarrasoutraços.
Vamos começar pela tradução da data digitada no formulário, no formato
DIA/MÊS/ANOparaoformatodoMySQL.Aestratégiaaquiserásepararosvalores
paramontarastringcomonovoformato.Paraisso,vamosusarumafun çãobem
interessantedoPHP,a explode(),quedivideumastringempartes,deacordocom
algumseparadorinformado.Oretornodafun ção explode()éumarraycomas
partesdastring,vejaumexemplo:
<?php
$texto_original = "Frodo;Sam;Merry;Pippin";
$hobbits = explode(";", $texto_original);
foreach ($hobbits as $hobbit) {
echo $hobbit . "<br />";
}
Avariável$texto_originalcontémosnomesdosquatrohobbitsseparados
porpontoevírgula. Afun ção explode()recebedoisparâmetros,sendoqueo
primeiroéoseparadorquedesejamoseosegundoéotextoquedesejamosseparar.
Oresultadoéum arraynoqualcadaiteméumdospedaçosapósaseparaç ão.
77

## Página 94

7.5. Cadastrandooprazodasatividades CasadoCódigo
Nocasodatraduç ãodoprazoparaasnossastarefas,vamoscriarumafun ção
chamada traduz_data_para_banco()noarquivo ajudantes.php.Estafun-
çãoirásepararosvaloresdedia,mêseanoeiráretornarumastringcomoformato
corretoparaoMySQL.Vejacomoelafica:
<?php
function traduz_data_para_banco($data)
{
if ($data == "") {
return "";
}
$dados = explode("/", $data);
$data_mysql = "{$dados[2]}-{$dados[1]}-{$dados[0]}";
return $data_mysql;
}
...
Quandoseparamosastringdadata,temosumarrayemqueoíndicezeroéodia,
oíndice1éomêseoíndice2éoano.Bastaconstruirumanovastringcomosdados
nasposiçõescorretaseseparandocomotraço,assimtemosoformatoesperadopelo
MySQL.
Outrodetalheéque,antesdetentartraduziradata,verificamosseelaestávazia,
jáqueéumcampoopcional.Casoestejavazia,retornamosumastringvazia,assim
oMySQLirágravarumadatatambémvazia.
Agoraprecisamosalterarotrechoondemontamosoarraycomosdadosenvia-
dosparausaranovafun ção,lánoarquivo tarefas.php:
<?php
...
if (isset($_GET['prazo'])) {
$tarefa['prazo'] = traduz_data_para_banco($_GET['prazo']);
} else {
$tarefa['prazo'] = '';
}
78

## Página 95

CasadoCódigo Capítulo7. IntegrandoPHPcomMySQL
...
Certo,játemosafun çãoetambémjáestamostraduzindooprazoquefordi-
gitadonoformulário. Sófaltaalterarafun ção gravar_tarefa()noarquivo
banco.phpparatambémgravaroprazo. Paraissoénecessáriomudaracria ção
docódigoSQL.Umanotaimportanteéqueadataprecisaserformatadacomouma
stringparaoMySQL,ouseja,elaprecisaestarentreaspas.Vejacomodeveráficaro
código:
<?php
...
function gravar_tarefa($conexao, $tarefa)
{
$sqlGravar = "
INSERT INTO tarefas
(nome, descricao, prioridade, prazo)
VALUES
(
'{$tarefa['nome']}',
'{$tarefa['descricao']}',
{$tarefa['prioridade']},
'{$tarefa['prazo']}'
)
";
mysqli_query($conexao, $sqlGravar);
}
...
Pronto,todasaspontasligadas.Experimentecadastrarumatarefacomumprazo
evejacomofica.Aminhalistaficouassim:
79

## Página 96

7.5. Cadastrandooprazodasatividades CasadoCódigo
Figura7.4:OprazodaatividadeestánoformatodoMySQL
Quaseperfeito,não? Agoraprecisamostraduziradatadevoltaparaonosso
formatobrasileiroparaexibirnalistadetarefas.Seguindoumalógicabemparecida,
vamoscriarumafun ção traduz_data_para_exibir(),quetambémestaráno
arquivo ajudantes.php:
<?php
...
function traduz_data_para_exibir($data)
{
if ($data == "" OR $data == "0000-00-00") {
return "";
}
$dados = explode("-", $data);
$data_exibir = "{$dados[2]}/{$dados[1]}/{$dados[0]}";
return $data_exibir;
}
...
Reparenasdiferen çasentreafun çãoquetraduzparaobancoeaquetraduz
paraexibição. Estamosseparandoastringusandoseparadoresdiferentesedepois
montamosnovamentetambémcomseparadoresdiferentes. Umaoutradiferen ça
na traduz_data_para_exibir()équeo iflogonocome çofazduasverifi-
cações,poisadatanobancopodeestarembrancooupodeestarcomoumastring
“0000-00-00”.Parafazerestaverificaçãoutilizamosainstruç ão OR,colocandouma
condiçãodecadalado,assimoPHPiráverificarseumadascondições,ouasduas,
sãoverdadeiras.
Atualizeasualistadetarefasevejaoresultado,agoracomadatacorreta:
80

## Página 97

CasadoCódigo Capítulo7. IntegrandoPHPcomMySQL
Figura7.5:OprazodaatividadecomoformatocorretousadonoBrasil
7.6 Marcando uma tarefa como concluída
Doscamposquetemosnoformulário,oúnicoqueaindanãoestamosgravandono
bancoéocampoqueindicaqueseatarefaestáconcluída.Nocheckboxdoformu-
láriocolocamosovalorcomo sim,masnobancoprecisamosdonúmerozeropara
tarefasnãoconcluídasedonúmero1paratarefasconcluídas.Porisso,vamosmudar
ocheckboxparaovalor 1,noarquivo template.php:
<label>
Tarefa concluída:
<input type="checkbox" name="concluida" value="1" />
</label>
Agora,vamosalteraraparteondeestedadoéadicionadonoarray $tarefa,
noarquivo tarefas.php:
<?php
...
if (isset($_GET['concluida'])) {
$tarefa['concluida'] = 1;
} else {
$tarefa['concluida'] = 0;
}
...
Repareque,apósverificarseodadoestádefinidonasuperglobal $_GET,ovalor
estásendodefinidocomo1,oucomo0quandonãoestiverdefinido.Estaverificaç ão
éassimpoisquandoumcheckboxnãoémarcado,elenãoéenviadopelonavegador
juntocomoformulário.Porisso,bastaverificarseeleestáounãodefinidousando
o isset().
81

## Página 98

7.6. Marcandoumatarefacomoconcluída CasadoCódigo
Agora, é necessário alterar a função gravar_tarefa() para gerar o
código SQL incluindo o campoconcluida. Vale lembrar que a função
gravar_tarefa()estánoarquivo banco.php:
<?php
...
function gravar_tarefa($conexao, $tarefa)
{
$sqlGravar = "
INSERT INTO tarefas
(nome, descricao, prioridade, prazo, concluida)
VALUES
(
'{$tarefa['nome']}',
'{$tarefa['descricao']}',
{$tarefa['prioridade']},
'{$tarefa['prazo']}',
{$tarefa['concluida']}
)
";
}
...
Reparequeocampofoiadicionadonalistadecamposeovalornalistadevalores.
Comoocampoéumnúmero,nãoprecisamosusaraspasdestavez.
Cadastreumaatividadeevejaoresultado:
Figura7.6:Mostrandoatarefacomoconcluída,masmostra‘1’nolugarde‘Sim’
Bem,aindanãoestábomparaousuário,poisagoraelevaiexibironúmero1
paratarefasconcluídaseonúmero0paraatividadesnãoconcluídas.
82

## Página 99

CasadoCódigo Capítulo7. IntegrandoPHPcomMySQL
Vamos adicionar mais uma função para traduzir conteúdos do banco
para apresentação. No arquivo ajudantes.php criaremos a função
traduz_concluida(), que retornaSim ou Não de acordo com o campo
detarefaconcluídanobanco:
<?php
...
function traduz_concluida($concluida)
{
if ($concluida == 1) {
return 'Sim';
}
return 'Não';
}
Precisamosalteraroarquivo template.phpparausaranovafun çãoparaexi-
birostatusdeconclusãodastarefas:
...
<td><?php echo traduz_concluida($tarefa['concluida']); ?> </td>
...
Atualizeapágina,oucadastreumanovatarefaevocêveráalistacomaspalavras
SimeNãonacolunaConcluída:
Figura7.7:ListaexibindoostatusdeconclusãocomoSimeNão
Nestemomento,temosumalistadetarefasfuncional,masaindanãopodemos
editarastarefaseteremosproblemasedigitarmosdatasincorretas,nomesmuito
grandesouseatualizarmosapáginaassimqueadicionarmosumatarefa. Nopró-
ximocapítulo,vamoslidarcomalgunsdestesproblemasevamospraticamentecon-
cluirnossaaplicaçãodegestãodetarefas.
83

## Página 100

7.7. Resumo CasadoCódigo
7.7 Resumo
Nestecapítuloalteramosanossaaplicaç ãoparatrabalharcomobancodedadosno
lugardassessões. Experimente,nestemomento,fecharoseunavegadoreabri-lo
novamente,ouentãoacessealistadetarefasemumnavegadordiferente. Perceba
queasatividadesestãolá! Ouseja,nãodependemosmaisdousodassessõespara
quenossaaplicaçãoguardeosdados.
Estecapítulotambémreforçouoconceitodaseparaç ãoderesponsabilidadesem
diferentesarquivosetambémmostrouoconceitodosarquivoscomfun çõesajudan-
tes,quetambémsãoconhecidosnomundodaprogramaç ãocomo helpers.
TambémfizemosatraduçãodedatasnoformatousadonoBrasilparaoformato
esperadopeloMySQLevice-versa.
7.8 Desafios
Horadetreinarfazendomaisalgunsdesafios:
• Continuealistadecontatosdosdesafiosanteriores,masagorapassandoa
guardarosdadosemumbancodedados.Utilizetodososconceitosvistosaté
aqui,comoaseparaç ãoemarquivos,ousodeajudanteseousodasfun ções
mysqli_doPHPparalidarcomoMySQL.
• Crieaaplicaçãoparatrabalharcomobancodedados estacionamento,criado
nosdesafiosdocapítuloanterior.Maisumavez,utilizetodososconceitosque
vimosatéaqui.
84

## Página 101

Capítulo8
Ediçãoeremo çãoderegistros
Nossalistadetarefasfuncionaapenasparainclusãodetarefaseaindanãovalidaas
informaçõesfornecidaspelousuário.Nestecapítulo,vamosadicionarmaisfuncio-
nalidadesparaeditareremovertarefasecomissodeixaraaplicaç ãopraticamente
prontaparaserusadanodiaadia.
8.1 Edição de tarefas
Paraeditarnossastarefas,precisamosdeumaformadeidentificarmosumatarefa
comoúnica. Usaronomeouoprazonãoéumaboaideia,poistarefaspodemse
repetir,porissovamosusarocampo iddatabela tarefasnobancodedados.
Estecampojáfoifeitoparaestasituaç ão,emqueprecisamosidentificarumregistro
comoúnico.Comoestecampoédotipoautonumeraç ão,cadatarefateráseupróprio
número,semserepetir.
Vamosalteraralistadetarefasparaincluirumanovacoluna Opções.Estanova
colunairáconterlinksparaediç ãoeremo çãodetarefas.Aprimeiraop çãoqueadi-

## Página 102

8.1. Ediçãodetarefas CasadoCódigo
cionaremoséadeediç ãodastarefas. Paraisso,editeoarquivo template.php,
adicionandoalinhaquecriaacoluna Opções ealinhaquecriaolinkparaediç ão:
...
<tr>
<th>Tarefa</th>
<th>Descricao</th>
<th>Prazo</th>
<th>Prioridade</th>
<th>Concluída</th>
<th>Opções</th> <!-- A nova coluna Opções -->
</tr>
<?php foreach ($lista_tarefas as $tarefa) : ?>
<tr>
<td>
<?php echo $tarefa['nome']; ?>
</td>
<td>
<?php echo $tarefa['descricao']; ?>
</td>
<td>
<?php echo traduz_data_para_exibir($tarefa['prazo']); ?>
</td>
<td>
<?php echo traduz_prioridade($tarefa['prioridade']); ?>
</td>
<td>
<?php echo traduz_concluida($tarefa['concluida']); ?>
</td>
<td> <!-- O campo com os links para editar e remover -->
<a href="editar.php?id=<?php echo $tarefa['id']; ?> ">
Editar
</a>
</td>
</tr>
<?php endforeach; ?>
...
AdicioneicomentáriosnoHTMLanteriorparaficarmaissimplesidentificar
quaissãoasnovasadições.Vejaaconstru çãodolinkparaaediç ãodastarefas.Ele
86

## Página 103

CasadoCódigo Capítulo8. Ediçãoeremo çãoderegistros
iránoslevarparaumarquivoPHPchamado editar.phpeestáinformandoum
parâmetroqueéo id. EsteidépreenchidopeloPHPpegandooidcadastradono
bancodedados.
Agoratemosumadecisãoimportanteasertomada:podemoscriarumanovapá-
gina,comumnovoformulário,paraaediç ãodastarefas,oquevaisermaissimples;
oupodemosreaproveitaroformulárioquejáexiste,oqueseráumpoucomenos
simples—masvaifacilitarbastanteasfuturasalteraçõesemnossaaplicaç ão,pois
nãoseránecessárioalterardoisformulários.
Vamosseguirocaminhodoreaproveitamentoeusarapenasumformuláriopara
fazeraadiçãoeaediç ãodastarefas.Paraisso,seránecessárioalteraronossoformu-
lárioparaqueelesaibalidarcomasduassituações.Masantes,vamosfazermaisuma
separaçãoemnossaaplicaç ão.Atualmenteoarquivo template.phpéresponsável
porexibiroformulárioparacadastrarumaatividadeetambématabelacomalista
deatividades.Issofuncionabemparaasituaç ãoatual,jáquenãotemosaindaaedi-
çãodetarefas,masnãoiráfuncionarbemparaaediç ão,poisoidealéqueaediç ão
nãoexibaalistadetarefas,masapenasoformulário.
Por isso, vamos melhorar um pouco o projeto atual separando o ar-
quivo template.php em dois, um para o formulário, que irá se chamar
formulario.php (sem acento) e outro para a tabela, que vamos chamar de
tabela.php.Valelembrarque,depoisdestaalteraç ão,oarquivo template.php
aindaexistirá,mascomumanovaestrutura.
Esteéoarquivo formulario.php:
<form>
<fieldset>
<legend>Nova tarefa</legend>
<label>
Tarefa:
<input type="text" name="nome" />
</label>
<label>
Descrição (Opcional):
<textarea name="descricao"></textarea>
</label>
<label>
Prazo (Opcional):
<input type="text" name="prazo" />
</label>
87

## Página 104

8.1. Ediçãodetarefas CasadoCódigo
<fieldset>
<legend>Prioridade:</legend>
<input type="radio" name="prioridade" value="1" checked />
Baixa
<input type="radio" name="prioridade" value="2" />
Média
<input type="radio" name="prioridade" value="3" />
Alta
</fieldset>
<label>
Tarefa concluída:
<input type="checkbox" name="concluida" value="1" />
</label>
<input type="submit" value="Cadastrar" />
</fieldset>
</form>
Eoarquivo tabela.phpvaificarassim:
<table>
<tr>
<th>Tarefa</th>
<th>Descricao</th>
<th>Prazo</th>
<th>Prioridade</th>
<th>Concluída</th>
<th>Opções</th>
</tr>
<?php foreach ($lista_tarefas as $tarefa) : ?>
<tr>
<td>
<?php echo $tarefa['nome']; ?>
</td>
<td>
<?php echo $tarefa['descricao']; ?>
</td>
<td>
<?php echo traduz_data_para_exibir($tarefa['prazo']); ?>
</td>
<td>
<?php echo traduz_prioridade($tarefa['prioridade']); ?>
</td>
88

## Página 105

CasadoCódigo Capítulo8. Ediçãoeremo çãoderegistros
<td>
<?php echo traduz_concluida($tarefa['concluida']); ?>
</td>
<td>
<a href="editar.php?id=<?php echo $tarefa['id']; ?> ">
Editar
</a>
</td>
</tr>
<?php endforeach; ?>
</table>
Onovoarquivo template.phpficarábemmenor,jáquenãoterámaisalógica
doformulárioedatabela.Masagoraeleteráumanovalógicaqueiráverificarsea
tabeladeveaparecer.
Paraissovamosutilizarumavariáveldecontrole $exibir_tabela,quedeverá
seriniciadacomovalor falselogonocome çodoarquivo tarefas.php. Veja
primeirocomodeveficaroarquivo template.php:
<html>
<head>
<meta charset="utf-8" />
<title>Gerenciador de Tarefas</title>
<link rel="stylesheet" href="tarefas.css" type="text/css" />
</head>
<body>
<h1>Gerenciador de Tarefas</h1>
<?php include('formulario.php'); ?>
<?php if ($exibir_tabela) : ?>
<?php include('tabela.php'); ?>
<?php endif; ?>
</body>
</html>
Gostoudestasintaxedo if?Emvezdeabrirchavesparaosblocos,eucoloquei
osdoispontosparaabriroblocodo ifefecheioblococomainstruç ãoendif.Esta
sintaxeébemlegalparatemplates,poisdeixamaisclarooqueestásendofechado.
Lembre-sedequepodemosfazerissocomo while,usando endwhile,foreendfor,
89

## Página 106

8.1. Ediçãodetarefas CasadoCódigo
foreacheendforeach.Useestasintaxeparatemplates—ficamelhorparaentender
ocódigodepois.Oseufuturoeuagradecerá,etambémopessoaldasuaequipe.
Agora precisamos definir a variável de controle dentro do arquivo
tarefas.php:
<?php
...
include "banco.php";
include "ajudantes.php";
$exibir_tabela = false;
...
Sevocêatualizarapáginanestemomento,veráapenasoseutítuloeoformulário,
poisacabamosdedefinircomo falseaexibiçãodatabela.
Anossaideiaénãoexibiralistadetarefasapenasquandoestivermoseditando
umatarefa.Jáqueanossalógicaéexibiralistasempreenãoexibiremapenasum
caso,entãoficamaissimplessedeixarmosavariável $exibir_tabelacomotrue,
emvezde false:
<?php
...
include "banco.php";
include "ajudantes.php";
$exibir_tabela = true;
...
Nãotenhamedodemudaralógicadosseusprogramasdevezemquando,sefor
paradeixarmaissimplesefácildeentender.Tenteevitaraomáximoasíndromedo
Gollumeficarchamandoseucódigodemeuprecioso.=)
Agoravamoscuidardaquelenovoarquivo,paraondeolinkdeediç ãodastarefas
nosleva,oarquivo editar.php.Estearquivoserámuitoparecidocomoarquivo
tarefas.php,mascomdiferen çasessenciais,comoavariável $exibir_tabela
comovalor falseeanãonecessidadedeusarafun ção buscar_tarefas(),jáque
nãoexibiremosastarefas.Claroqueseránecessárioiraobancodedadosparapegar
90

## Página 107

CasadoCódigo Capítulo8. Ediçãoeremo çãoderegistros
osdadosdatarefaquequeremoseditar,porissovamosusarumafun çãonova,a
buscar_tarefa().Vejaqueonomeébemparecidocomaoutrafun ção,mudando
apenasqueanovafun çãobuscaapenasumatarefa.Éporissoqueseunomeestáno
singulareoseuresultadoseráatribuídoàvariável $tarefa.
Umaoutradiferen çaimportantenoarquivo editar.phpéqueeledeverápegar
tambémocódigodeidentificaç ãodasnossastarefas,queéocampo id.
Vejacomodeveráficaronossoarquivo editar.php.
<?php
session_start();
include "banco.php";
include "ajudantes.php";
$exibir_tabela = false;
if (isset($_GET['nome']) && $_GET['nome'] != '') {
$tarefa = array();
$tarefa['id'] = $_GET['id'];
$tarefa['nome'] = $_GET['nome'];
if (isset($_GET['descricao'])) {
$tarefa['descricao'] = $_GET['descricao'];
} else {
$tarefa['descricao'] = '';
}
if (isset($_GET['prazo'])) {
$tarefa['prazo'] = traduz_data_para_banco($_GET['prazo']);
} else {
$tarefa['prazo'] = '';
}
$tarefa['prioridade'] = $_GET['prioridade'];
if (isset($_GET['concluida'])) {
$tarefa['concluida'] = 1;
} else {
91

## Página 108

8.1. Ediçãodetarefas CasadoCódigo
$tarefa['concluida'] = 0;
}
editar_tarefa($conexao, $tarefa);
}
$tarefa = buscar_tarefa($conexao, $_GET['id']);
include "template.php";
Vejaqueeleépraticamenteumacópiadoarquivo tarefas.php,mascom
algumasalteraçõesfundamentais.
Precisamoscriaranovafun ção buscar_tarefa().Eladeveráficarjuntocom
asdemaisfun çõesquelidamcombancodedadosnoarquivo banco.php:
<?php
...
function buscar_tarefa($conexao, $id) {
$sqlBusca = 'SELECT * FROM tarefas WHERE id = ' . $id;
$resultado = mysqli_query($conexao, $sqlBusca);
return mysqli_fetch_assoc($resultado);
}
...
Reparequesempreutilizaremosocampo iddatabela tarefasparanosrefe-
renciarmosaumatarefacomoúnica.Issoéumpadrãoparaosbancosdedadose,
emgeral,paradiversaslinguagens.
Agoravamosalteraroarquivo formulario.phpparaqueelejávenhacomos
dadosdatarefapreenchidos,demodoqueousuáriopossafazeraediç ão.
Vamosprimeiroadicionarocampo idnoformulário,assimeleseráenviado
juntocomorestantedoscamposquandoousuáriopedirparasalvaraediç ãodas
tarefas.Estecamponãoprecisaserexibidoparaousuário,poisnãoexisteanecessi-
dadedeediç ãodele,entãovamosusarumcampodotipo hidden:
<form>
<input type="hidden" name="id"
value="<?php echo $tarefa['id']; ?> " />
<fieldset>
92

## Página 109

CasadoCódigo Capítulo8. Ediçãoeremo çãoderegistros
...
Norestantedoscampos,vamospreencherosvaloresusandooatributo value
ouoconteúdodoelementoquandofortexto,quenestecasosãooscampos tarefa,
descricaoe prazo. Voucolocarapenasoscamposnocódigoaseguir, mas
lembre-sedequeelesestãoseparadoseexistemaiscódigoentreeles:
<input type="text" name="nome"
value="<?php echo $tarefa[ 'nome']; ?> " />
<textarea name="descricao">
<?php echo $tarefa[ 'descricao']; ?>
</textarea>
<input type="text" name="prazo"
value="<?php
echo traduz_data_para_exibir($tarefa['prazo']);
?> " />
Lembradafun ção traduz_data_para_exibir()? Olhasócomoelaestá
sendoútilmaisumavez,agoraparaexibiradatanoformatocorretoparaediç ão.
Opreenchimentodoscampos prioridadee concluidaéumpoucodife-
rente,jáqueprecisamosdoatributo checkedparamarcarocampo:
...
<input type="radio" name="prioridade" value="1"
<?php echo ($tarefa['prioridade'] == 1)
? 'checked'
: '';
?> /> Baixa
<input type="radio" name="prioridade" value="2"
<?php echo ($tarefa['prioridade'] == 2)
? 'checked'
: '';
?> /> Média
<input type="radio" name="prioridade" value="3"
<?php echo ($tarefa['prioridade'] == 3)
? 'checked'
93

## Página 110

8.1. Ediçãodetarefas CasadoCódigo
: '';
?> /> Alta
<!-- Agora o campo de concluída -->
<input type="checkbox" name="concluida" value="1"
<?php echo ($tarefa[ 'concluida'] == 1)
? 'checked'
: '';
?> />
Nãoseassustecomestetrecho!AquiestamosusandooternáriodoPHP,queé
tipoum if,mascomumasintaxereduzida.Oternáriofuncionaassim:vocêcoloca
umacondicionalelogodepoisumaop çãoparaacondicionalverdadeirae,emse-
guida,umaop çãoparaacondicionalfalsa. Nocome çopareceestranho,maslogo
sepercebequeestaformadeusarcondicionaispodesermuitoútilemalgunscasos.
Vejaumexemplocomum ifnormal,igualaoquejávimosatéagora:
<?php
$idade = $_GET['idade'];
if ($idade >= 18) {
echo "Bem vindo!";
} else {
echo "Entrada proibida!";
}
Agora,vejaomesmoexemplo,usandoternário:
<?php
$idade = $_GET['idade'];
echo ($idade > 18) ? "Bem vindo!" : "Entrada proibida!";
Bemmaissimples,certo? Agoratodaacondi çãocabeemapenasumalinhae
ficabemfácildeleresemummontedecódigoparaapenasum echo.
Umapequenamudan çaquepodemosfazeréalterartambémotextodobotão
submitnofinaldoformulário,queatualmenteé Cadastrar. Aideiaéexibir
Atualizarquandoestivermoseditandoumatarefa.Nestecasooternáriotambém
serábastanteútil:
94

## Página 111

CasadoCódigo Capítulo8. Ediçãoeremo çãoderegistros
...
<input type="submit" value="
<?php echo ($tarefa[ 'id'] > 0) ? 'Atualizar' : 'Cadastrar'; ?>
" />
...
Muitobem,nestemomentooformuláriodeediç ãojáestáexibindoosdados
dastarefas.Masaindanãoescrevemosafun ção editar_tarefa().Estafun ção
receberáumarraycomosdadosdatarefaeentãofaráaatualiza çãodoregistrono
bancousandoainstruç ão UPDATEdaSQL.Vejaumexemplodainstruç ão UPDATE:
UPDATE tabela SET
campo1 = 'valor',
campo2 = 123
WHERE id = 1
Maisumavezvalelembrarquenossasfun çõesquelidamcomobancodeda-
dossãoapenasgeradoraseexecutorasdeSQL,porissoéimportantesededicara
aprenderSQLtantoquantoaoaprendizadodePHP.;-)
Vejacomodeveráficarafun ção editar_tarefa():
<?php
...
function editar_tarefa($conexao, $tarefa)
{
$sql = "
UPDATE tarefas SET
nome = '{$tarefa['nome']}',
descricao = '{$tarefa['descricao']}',
prioridade = { $tarefa['prioridade']},
prazo = '{$tarefa['prazo']}',
concluida = {$tarefa['concluida']}
WHERE id = {$tarefa[ 'id']}
";
mysqli_query($conexao, $sqlEditar);
}
...
95

## Página 112

8.1. Ediçãodetarefas CasadoCódigo
Comestafun çãopronta,jápodemoseditarastarefas. Massevocêacessaro
arquivo tarefas.phpnestemomento,vocêverádiversoserrosnapágina,maisou
menosconformeaimagemaseguir:
Figura8.1:Diversoserrosnoformulário
Nossa!Quantoserros!Masseanalisarmosmelhorveremosquenaverdadeto-
dososerrossãoreferentesàmesmavariável $tarefa.Esteerroestáacontecendo
porquemudamosoformulárioparapreencherosdadosdeumatarefasendoedi-
tada.Jáquetomamosadecisãodeusarapenasumarquivoparaoformulário,agora
teremosqueadaptaroformulárioparaocadastrodenovastarefas,queantesjáfun-
cionavacorretamente.
Nestecaso,acorre çãodoproblemaésimples:bastafornecermosumatarefaem
brancoparaoformuláriodecadastrodetarefas,assimelesempreteráumavariá-
vel $tarefaparaexibir,evitandooserrosdevariávelnãodefinida. Noarquivo
tarefas.phpadicionaremosestanova $tarefaembranco,queseráumarray.
Vamosadicionarestavariávellogoantesdo includedo template.php:
<?php
...
$tarefa = array(
'id' => 0,
'nome' => '',
96

## Página 113

CasadoCódigo Capítulo8. Ediçãoeremo çãoderegistros
'descricao' => '',
'prazo' => '',
'prioridade' => 1,
'concluida' => ''
);
include "template.php";
...
Comoestamosfornecendoumatarefaembranco,oformulárionãogeramais
erros. Então,vamoseditarumatarefa! Acesseoendere çohttp://localhost/tarefas/
tarefas.phpecliquenolink Editar. Vocêdeveráverapenasoformuláriopreen-
chidocomosdadosdatarefa,massemalistadetarefasembaixo:
Figura8.2:Nossoformulárioparaediç ãodetarefas
Agorapodemoseditarnossastarefas,umavezquejátemosoformulário. O
arquivo editar.phpjátrataosdadosetambémjáestamosenviandoatarefapara
afun ção editar_tarefa()queusaocomando UPDATEdoMySQLparaatualizar
osdados.
Masalgoaindanãoestálegal.Percebaque,apóssalvarumatarefa,continuamos
napáginadeedição.Estaéumaboahoraparaapresentarumanovaop ção:os redi-
recionamentos.Aideiaaquiéquebrarofluxodaaplicaç ãologoapósaexecuç ãoda
97

## Página 114

8.2. Remoçãodetarefas CasadoCódigo
função editar_tarefa(),paraqueousuáriosejaencaminhadonovamentepara
apáginainicial—ouseja,alistadetarefas,lánoarquivo tarefas.php.OPHP
emsinãopossuiumaferramentaderedirecionamento,poisissoéfeitopeloHTTP,
atravésdeinformaçõesparaonavegador.Aquieuvoumostrarumaformasimples
defazeresteredirecionamento,maslembre-sedemaistardepararparaestudarum
poucomaissobreoprotocoloHTTP,ok?
Parafazeroredirecionamento,precisamosfalarparaonavegadorqueeledeveir
paraumlocaldiferentedolocalatual.Issoéfeitoatravésdecabe çalhosHTTP,neste
casoocabe çalhoqueprecisamoséo Location.OPHPusaafun ção header()
paramandaressescabe çalhosparaonavegador. Vejacomoficaousodafun ção
header()pararedirecionarmosnossosusuáriosdevoltapara tarefas.phpapós
aatualizaçãodeumatarefacomafun ção editar_tarefa():
<?php
...
editar_tarefa($conexao, $tarefa);
header('Location: tarefas.php');
die();
...
Logoapósafun ção header(),foiadicionadaafun ção die(),queencerra
oprocessodoPHPimediatamente.Achamadadafun ção die()vaievitarqueo
restantedoarquivo editar.phpsejaexecutadodeformadesnecessária,jáqueo
queprecisamosapósaediç ãodeumatarefaéapenasoredirecionamentoparaalista
detarefas.
Comisso,temosalistadetarefasjáfuncionalparacadastroetambémparaedi-
çãodetarefas!Masagoraprecisamosdeunsajustesimportantes,comoapossibili-
dadederemovertarefasetambémavalidaç ãodoformulário,paraevitarmos,por
exemplo,ocadastrodetarefasembranco.
8.2 Remoção de tarefas
Aremo çãodastarefasserábemmaissimplesqueaediç ão,poisdessaveznãoprecisa-
mospegardadosnobanco,preencherformulárioetc.Agoratudooqueprecisamos
édonúmerodatarefapararemover,ouseja,seu idnobancodedados.
98

## Página 115

CasadoCódigo Capítulo8. Ediçãoeremo çãoderegistros
Vamoscomeçaradicionandoolink Removernanossalistadetarefas.Estelink
ficarájuntodolink Editar,nacoluna Opçõesdatabela,entãovamoseditaro
arquivo tabela.phpparafazeraadiç ãodonovolink:
...
<td>
<a href="editar.php?id=<?php echo $tarefa[ 'id']; ?> ">
Editar
</a>
<a href="remover.php?id=<?php echo $tarefa[ 'id']; ?> ">
Remover
</a>
</td>
...
Percebaqueolinkderemo çãoémuitoparecidocomolinkdeediç ãoquejá
conhecemos.Afinal,pararemoverumatarefatambémvamosprecisardoseu idno
bancodedados,masoendere çoapontaparaoarquivo remover.php,queainda
nãoexiste.
Onossoarquivo remover.phptambémdeveráutilizaroarquivo banco.php
paraacessarobancoetambémdeveráredirecionarousuárioapósaremo çãoda
tarefa,assimcomofizemosnaediç ão.Estearquivoserábemmenorqueosdemais,
porqueprecisafazermenostrabalhodoquealistaeaediç ão:
<?php
include "banco.php";
remover_tarefa($conexao, $_GET[ 'id']);
header('Location: tarefas.php');
Epronto,esteéoarquivo remover.phpemtodooseuesplendor.Sim,apenas
isso!Éclaroqueaindaprecisamoscriarafun ção remover_tarefa()lánoarquivo
banco.php,masalógicadaremo çãoébasicamenteesta.
Noarquivo banco.php,vamosadicionarafun ção remover_tarefa().Esta
funçãoiráutilizarocomando DELETEdalinguagem SQL,quetemasintaxecon-
formeesteexemplo:
99

## Página 116

8.3. Evitandooproblemacomaatualizaç ãodepágina CasadoCódigo
DELETE FROM tarefas WHERE id = 123
Esteexemploremoveriaoregistrodatabela tarefascomoid123.Mastambém
podemosfazeralgoassimcomSQL:
DELETE FROM tarefas WHERE concluida = 1
Estecomandoremoveriadatabela tarefastodososregistrosondeocampo
concluidafosseiguala1,ouseja,nossastarefasconcluídas.
Masvamosvoltaràfun ção remover_tarefa()noarquivo banco.php:
<?php
...
function remover_tarefa($conexao, $id)
{
$sqlRemover = "DELETE FROM tarefas WHERE id = {$id}";
mysqli_query($conexao, $sqlRemover);
}
Com a função remover_tarefa()pronta, já podemos usar o novo link
Removernalistadetarefaspararemovermostarefas.Faç aumteste,deucerto?Se
sim,vamosemfrente!Casotenhaalgumproblema,reviseseucódigoatéaquieleia
asmensagensdeerroqueoPHPinforma,assimficamaisfácilderesolverproblemas.
8.3 Evitando o problema com a atualização de pá-
gina
Aindatemosumpequenoproblemacomanossalistadetarefas!Nãoacredita?Então
façaoseguinte:adicioneumatarefa,adicionou?Agoraatualizeapáginausandoo
F5ouobotãodeatualizardoseunavegador.Viuoqueacontece?Elerepeteoúltimo
cadastrofeito!Vejacomoficouaminhalista:
100

## Página 117

CasadoCódigo Capítulo8. Ediçãoeremo çãoderegistros
Figura8.3:Tarefasrepetidasapósatualizarapáginadepoisdeumagravaç ão
Esseproblemaacontecepois,quandoatualizamosapágina,onavegadormanda
osdadosnovamenteparaoPHP.ComooPHPrecebeudados,eleacabadisparando
todaarotinadegravaç ãodenovastarefas.
Paraevitarmosesteproblema,vamosusarotruquequeaprendemoscomaspá-
ginasdeediç ãoederemo çãoevamosredirecionarousuáriodevoltaparaalistade
tarefasapósagravaç ãodeumatarefa.Paraisso,vamosusarafun ção headerlogo
apósafun ção gravar_tarefanoarquivo tarefas.php:
<?php
...
gravar_tarefa($conexao, $tarefa);
header('Location: tarefas.php');
die();
...
Afun ção die()aquitemomesmopropósitodoarquivo editar.php,para
encerraroPHPlogoapósenviarocabe çalhoderedirecionamentoparaonavegador.
Façaumtesteagoraeapósagravaç ãovocêveráoformulárioealistadetarefas
normalmente,eaindapoderáatualizarapáginasemoproblemadeduplicaç ãoda
últimatarefacadastrada.
8.4 Resumo
Atéestemomentojávimosbastantecoisa.Saímosdozeroejátemosumambiente
PHPeMySQLcomanossaprimeiraaplicaç ão:umgerenciadordetarefas!
Neste capítulo fizemos a edição das tarefas e também sua remoção. Além
disso,corrigimosalgunscomportamentosusandoo Redirect,atravésdafun ção
101

## Página 118

8.5. Desafios CasadoCódigo
header()doPHP.
Nestecapítulotambémforamutilizadososcomandos UPDATEe DELETEda
linguagemSQL.
Nopróximocapítulofaremosavalidaç ãodosdadosenviadospelousuário,assim
evitamosproblemascomodatasinválidas.
8.5 Desafios
Existemdiversasformasdemelhoraroquejáfizemosatéaqui.Experimentedesen-
volverfuncionalidadescomo:
• UmbotãodeCancelarquandoestivereditandoumatarefa.
• Umbotãoparaduplicarumatarefa.
• Otimizar o código para ter menos repetição. Veja que os arquivos
tarefas.phpe editar.phpsãomuitoparecidos. Vocêconseguepensar
emmaneirasdereutilizarpartesdeles?Quetalumarquivonovocomasbases
paraeles?
• Quetalumaopçãoparaapagartodasastarefasconcluídas?
• Vocêconseguepensaremumamaneiradeusarapenasumarquivoparaexibir
astarefas,editar,salvarumanova,deletaretc.? Assimnãoserianecessário
termososarquivos editar.phpe remover.php.
Alémdestesdesafiosparaalistadetarefas,continueosoutrosdesafiosdoscapí-
tulosanteriores:
• Adicioneumaopçãoparaeditareoutrapararemoveroscontatosdalistade
contatos.
• Adicioneumaopçãoparalistarapenasoscontatosfavoritos.
• Adicioneopçõespararemoverosdadosdosveículoscadastradosnobancode
dadosdoestacionamento.
• Façaumaop çãonodesafiodoestacionamentoparamostrarosveículosque
entraramnoestacionamentoemumadeterminadadata.
102

## Página 119

Capítulo9
Validaçãodeformulários
Umproblemacomumempraticamentequalquersoftwarequetenhaquelidarcom
dadosfornecidosporumusuárioéavalidaç ão.Sabequandovocêpreencheumfor-
mulárioemumsite(ouumsoftwaredesktop,ouumappparasmartphoneetc.)e,
logoapósenviarosdados,oformulárioéexibidonovamentecomseusdadosemais
algunsalertasdecamposquesãoobrigatóriosouqueforampreenchidosincorre-
tamente?Poisentão,esteéumcenárioondeaconteceualgumtipodevalidaç ãode
entradadedados.
9.1 Validação na lista de tarefas
Nossalistadetarefastemumcampoobrigatório,queéonomedatarefaeumcampo
quepodegerarerrossepreenchidoincorretamente,queéocampodeprazo,onde
usamosumadata.
Atualmenteestamosusandoocampodenomedatarefaparadecidirsevamos
gravaratarefaounão. Issoéumpoucoruim,poissealguémpreencherosdados

## Página 120

9.2. EntradadedadosusandoPOST CasadoCódigo
datarefa,menosonome,eenviar,iráperderoquefoidigitadoeatarefanãoserá
gravada.
Podemoscome çarvalidandoessaentrada,parasaberseoformuláriofoienviado
independentementedocampodenomedatarefaserpreenchidoounão.
Mas,antesdefazerestavalidaç ão,vamospegarumpedaçodestecapítulopara
falardaentradadedados.
9.2 Entrada de dados usando POST
Atéestemomentoestamosusandoasuperglobal $_GETdoPHPparapegaros
dadosenviadospelousuárionoformulárioetambémnaspáginasdeediç ãoede
remoçãoparapegaro iddatarefaquequeremoseditarouremover.
Vocêjádeveterusadodiversosformuláriosemsiteseoutrasaplicaçõesonline
epercebidoqueosdadosdigitadosemumformulárionãoficamexpostosnoen-
dereço,assimcomonossoformuláriodetarefasestáfazendo.Existembasicamente
duasformasdeenviardadosusandoumformulário,umadelaséusandooGETea
outraéusandooPOST.
UsandooPOST,osdadosdoformulárionãoficammaisnoendere çodapágina
dedestino,oquepodetornaraaplicaç ãomaissegura.Imagineumformulárioque
enviaumasenhaeelaficaexpostanaURLdedestino.Nadabom,né?
Certo,mascomopodemostrocarousodoGETnosformuláriosdanossalistade
tarefasparaoPOST?Oprimeiropassoéalteraroformulárioparaqueuseométodo
POSTeparaissoénecessárioadicionaroatributo methodcomovalor POSTno
elementoform.Estasalteraçõesdevemserfeitasnoarquivo formulario.php:
<form method="POST">
<input type="hidden" name="id" value="<?php echo $tarefa['id']; ?> "/>
...
Comisso,oformuláriopassaaenviarosdadosusandooPOST.Opadrãodos
navegadoreséenviarusandoGET,porissoessemétodoerausadoquandonãotí-
nhamosinformadoexplicitamentequalusar.
Agoratambéménecessárioalterartodaapartequepegaosdadosdoformulário
paracadastrarnobanco,poisestamosusandoasuperglobal $_GET.Estaalteraç ão
serábemsimples,jáqueoPHPcuidadaentradaviaPOSTtambém.Então,tudoo
104

## Página 121

CasadoCódigo Capítulo9. Validaçãodeformulários
quetemosquefazerétrocar $_GETpor $_POSTnoscamposrelacionadosaoformu-
lário.Essasalteraçõesdevemserfeitasnosarquivo tarefas.phpe editar.php
Vejacomoficaaalteraç ãonoarquivo tarefas.php:
<?php
...
if (isset($_POST['nome']) && $_POST['nome'] != '') {
$tarefa = array();
$tarefa['nome'] = $_POST['nome'];
if (isset($_POST['descricao'])) {
$tarefa['descricao'] = $_POST['descricao'];
} else {
$tarefa['descricao'] = '';
}
if (isset($_POST['prazo'])) {
$tarefa['prazo'] = traduz_data_para_banco($_POST['prazo']);
} else {
$tarefa['prazo'] = '';
}
$tarefa['prioridade'] = $_POST['prioridade'];
if (isset($_POST['concluida'])) {
$tarefa['concluida'] = 1;
} else {
$tarefa['concluida'] = 0;
}
gravar_tarefa($conexao, $tarefa);
...
Asalteraçõesnoarquivo editar.phptambémsãosimples:
<?php
...
if (isset($_POST['nome']) && $_POST['nome'] != '') {
105

## Página 122

9.3. Validandoonomedatarefa CasadoCódigo
$tarefa = array();
$tarefa['id'] = $_POST['id'];
$tarefa['nome'] = $_POST['nome'];
if (isset($_POST['descricao'])) {
$tarefa['descricao'] = $_POST['descricao'];
} else {
$tarefa['descricao'] = '';
}
if (isset($_POST['prazo'])) {
$tarefa['prazo'] = traduz_data_para_banco($_POST['prazo']);
} else {
$tarefa['prazo'] = '';
}
$tarefa['prioridade'] = $_POST['prioridade'];
if (isset($_POST['concluida'])) {
$tarefa['concluida'] = 1;
} else {
$tarefa['concluida'] = 0;
}
editar_tarefa($conexao, $tarefa);
...
OusodoPOSTtambéméimportanteparaformuláriosqueenviamarquivos,
masveremosissoumpoucomaisparafrente.
9.3 Validando o nome da tarefa
Vamosàvalidaçãodonossoprimeirocampo,queseráocampocomonomedatarefa
asercadastrada.Hojejáexisteumaespéciedevalidaç ãoqueverificaseonomeda
tarefafoidigitadoounãoeentãodecideseirácadastraratarefanobanco.Essetipo
dedecisãovaisempredependerdeocampocomonomedatarefatersidodigitado
pelousuário.Issopodetrazerproblemas,poisousuáriopodeterdigitadoorestante
106

## Página 123

CasadoCódigo Capítulo9. Validaçãodeformulários
doscampos,masterseesquecidodonomedatarefaenestecasoelevaiperdertudo
oquedigitounorestantedoscampos.
Vamostratarprimeirodavalidaç ãonapáginadecadastro,ouseja,noarquivo
tarefas.php.Vamoscome çaralterandoalinhaqueverificasetemqueentrarou
nãonoprocessodegravaç ãodenovastarefas,poiselaverificaapenasseoíndice
nomeexisteem $_POSTenãonecessariamenteseexistemmaiscoisasno $_POST.
Estaéalinha:
<?php
...
if (isset($_POST[ 'nome']) && $_POST['nome'] != '') {
...
Estalinhaserásubstituídaporesta:
<?php
...
if (tem_post()) {
...
Afun ção tem_post()aindanãoexiste,entãovamosadicioná-lanoarquivo
ajudantes.php:
<?php
...
function tem_post()
{
if (count($_POST) > 0) {
return true;
}
return false;
}
Vejaqueafun ção tem_post()fazumacontagemdonúmerodeíndicesexis-
tentesem $_POSTeretornatruequandoestenúmeroformaiorquezero,queéuma
situaçãoqueiráacontecerapenassealgumainformaç ãoforenviadavia POST.
107

## Página 124

9.3. Validandoonomedatarefa CasadoCódigo
Certo,agoraoprocessodegravaç ãoiniciasetiverdadosno POST,independente
deocampo nometersidoenviado. Issoébom,poisvamosvalidarestecampoe
repreencherosdadosnoformulário,casoavalidaç ãonãopasse.
Vamoscriarumanovavariáveldecontrolechamada $tem_errosetambém
umarrayparaguardaroserrosemcadacampochamado $erros_validacao,
amboslogoacimado ifqueverificasetem POST:
<?php
...
$exibir_tabela = true;
$tem_erros = false;
$erros_validacao = array();
if (tem_post()) {
...
Nocaso, $tem_errosjácomeçacomofalse,eseráalteradaparatrueconforme
asvalidaçõesacontecerem. Oarray $erros_validacaotambémreceberáseus
valoresconformeasvalidaçõesacontecerem.
Paravalidarocampocomonomedatarefaprecisamosapenasverificarseele
nãoestávazio.Paraissovamosalteraralinhaquepegaonomedatarefanoarquivo
tarefas.php:
<?php
...
$tarefa['nome'] = $_POST['nome'];
...
Esta linha está logo após oif que acabamos de alterar para usar a função
tem_post().Nolugardestalinha,faremosumaverificaç ãoparecidacomaverifi-
caçãoquejáexisteparaosdemaiscampos,comadiferen çadequeagoraprecisamos
preencheroarraycomoserrosealteraravariável $tem_errosparatruecasoo
nomedatarefaestejavazio:
<?php
...
108

## Página 125

CasadoCódigo Capítulo9. Validaçãodeformulários
if (isset($_POST[ 'nome']) && strlen($_POST['nome']) > 0) {
$tarefa['nome'] = $_POST['nome'];
} else {
$tem_erros = true;
$erros_validacao['nome'] = 'O nome da tarefa é obrigatório! ';
}
...
Amaiornovidadenestetrechoéousodafun ção strlen()quecontaota-
manhodeumtexto.Oqueestamosfazendoéverificarseonomeestáno POSTe
seacontagemdecaracteresémaiorquezero. Reparequeo elseestácriandoum
índicenomenoarray $erros_validacaocomumafraseindicandooerroque
aconteceu.Alémdisso,tambémaproveitamosomesmo elseparaalteraravariável
$tem_errosparatrue.
Agoraquetemosumavariávelquedizsealgumerroaconteceu,podemosusá-la
paradecidirsevamosounãofazeragravaç ãodatarefa.Comojátemosumafun ção
quefazagravaç ão,podemoscolocarachamadadestafun çãodentrodeum if:
<?php
...
if (! $tem_erros) {
gravar_tarefa($conexao, $tarefa);
header('Location: tarefas.php');
die();
}
...
Vejaqueusamosaexclamaç ãoparanegarovalorde $tem_erros,entãoesta
condiçãopodeserlidacomo“senãotemerros”. Casoalgumerroexista,afun ção
função gravar_tarefa()nãoseráchamadaeoarquivo tarefas.phpconti-
nuaráaserexecutado,jáqueousuárionãoseráredirecionadoparaalistadetarefas.
Sevocêtentarincluirumatarefavazianestemomento,vocêsimplesmentevoltará
aoformulário,massemavisosdeerro.
109

## Página 126

9.4. Adicionandooavisodeerro CasadoCódigo
9.4 A dicionando o aviso de erro
Paraadicionaroavisodeerrovamosalteraroarquivo formulario.php,mais
especificamente,vamosalterarapartequecriaocampoparaonomedatarefa:
...
<label>
Tarefa:
<input type="text" name="nome"
value="<?php echo $tarefa[ 'nome']; ?> " />
</label>
...
Asvariáveis$tem_errose $erros_validacaoserãousadasparadecidirse
oerroseráexibidoeparapegarovalorerro.Altereotrechodentrodatag label
paraficarassim:
...
<label>
Tarefa:
<?php if ($tem_erros && isset($erros_validacao[ 'nome'])) : ?>
<span class="erro">
<?php echo $erros_validacao['nome']; ?>
</span>
<?php endif; ?>
<input type="text" name="nome"
value="<?php echo $tarefa['nome']; ?> " />
</label>
...
Estamos usando duas condições dentro doif, uma para verificar se
$tem_erroséverdadeiraeoutraparaverificarseoíndice nomeexistedentro
doarray $erros_validacao. Estaverificaçãodoíndiceénecessáriapoislogo
maisfaremosavalidaç ãodosoutroscampos, entãopodeserque, porexemplo,
$tem_errossejatruemasqueoerronãosejanocampo nome.
Oerrofoiexibidodentrodeumelemento spancomaclasseerro,assimpodemos
usarCSSparaestilizarafrasedeerro.Nomeucaso,eudeixeiafraseemvermelho.
SevocêusaroCSSdosexemplos,teráomesmoresultado.
110

## Página 127

CasadoCódigo Capítulo9. Validaçãodeformulários
Façaumanovatentativadecadastrosemdigitaronomedatarefaevocêdeverá
veroformulárionovamente,comoerrosendoexibido:
Figura9.1:Exibiçãodoerrononomedatarefa
Masaindatemosumproblema.Seexperimentarmoscadastrarumatarefaape-
nascomumadescriç ão,voltaremosparaapáginadoformulário,massemosdados
dadescrição.Esteéumpontoimportantedavalidaç ão,poisquandovalidamosum
formulárioeinformamosparaousuárioqueexistealgumcampofaltando,nãopo-
demosapagarorestantedasinformaçõesjáfornecidas.Quemnuncapassouporum
formulárioqueapagouosdadosporcontadeapenasumcampoesquecido?Ébem
chato,não?
Parapreenchernovamenteoscamposquejáforamenviadosvamosfazerusodo
array $tarefaqueégeradoantesdeincluirmosoarquivo template.php,láno
finaldoarquivo tarefas.php:
<?php
...
$tarefa = array(
'id' => 0,
'nome' => '',
'descricao' => '',
'prazo' => '',
111

## Página 128

9.4. Adicionandooavisodeerro CasadoCódigo
'prioridade' => 1,
'concluida' => ''
);
...
Estearrayégeradocomdadosembranco,entãoprecisamosverificarseexistem
dadosenviadosatravésdo POSTparaquesejamusadosnolugardosvaloremem
branco.Lembradoternário?Aquieleserábemútil:
<?php
...
$tarefa = array(
'id' => 0,
'nome' => (isset($_POST[ 'nome'])) ?
$_POST['nome'] : '',
'descricao' => (isset($_POST['descricao'])) ?
$_POST['descricao'] : '',
'prazo' => (isset($_POST['prazo'])) ?
traduz_data_para_banco($_POST['prazo']) : '',
'prioridade' => (isset($_POST['prioridade'])) ?
$_POST['prioridade'] : 1,
'concluida' => (isset($_POST['concluida'])) ?
$_POST['concluida'] : ''
);
...
Deixeioternárioemduaslinhasemcadaumdoscamposparafacilitaraleitura
aquinolivro,maselepoderiaficaremapenasumalinhanocódigo.
Percebaqueemcadaumdoscamposéverificadoseexisteumvalorno POSTe
entãoestevaloréusado.Casonãoexista,usamosumvalorpadrãoembranco.
Ocampoquefogeumpoucodosdemaiséo prazo. Neleestamosusandoa
função traduz_data_para_banco(). Mas,esperaumpouco,naverdadenão
estamosenviandoestadataparaobanco!Então,porqueusarestafun ção?
Vamosanalisaracriaç ãodocampodoprazo,lánoarquivo formulario.php:
112

## Página 129

CasadoCódigo Capítulo9. Validaçãodeformulários
<label>
Prazo (Opcional):
<input type="text" name="prazo"
value="<?php echo traduz_data_para_exibir($tarefa['prazo ']); ?> "
/>
</label>
Vejaquenacriaç ãodocamponoformulárioestamosusandosempreafun-
ção traduz_data_para_exibir(),queesperaumtextovazio,ouumadatano
formatoANO-MÊS-DIA,masadataqueentramosnoformulárioestánoformato
DIA/MÊS/ANO.Paraevitarerrosnaformataç ãodadata,vamosmontaroarraycom
oformatoesperadopelonossoformulário.
Agora,preenchaoscamposdoformulário,menosonomedaatividadeetente
fazeragravaç ão. Vocêveránovamenteoformulário,comoerrodevalidaç ãodo
nome,assimcomodaoutravez,masagoraosdemaiscamposjáestarãopreenchidos
comosdadosinformados:
Figura9.2:Exibiç ãodeerrononome,mascomoformuláriopreenchido
Sepreenchermostambémonomedatarefa,elaserágravadanormalmente. O
próximopassoévalidaroprazo,poisosdemaiscampossãoopcionaisenãoprecisam
devalidaçãodedadoscorretos.
113

## Página 130

9.5. Validandoadatadigitada CasadoCódigo
9.5 Validando a data digitada
Oprazoéumcampoopcional,masexisteoproblemadeousuárioentrardatas
inválidas,comoum31defevereirooumesmotextosquenãoestejamnoformato
DIA/MÊS/ANOqueestamosesperando.
Vamosfocarnavalidaç ãodoformatoprimeiro,depoisiremosparaavalidaç ão
dedatasqueexistem.
Vamosdefinirentãoqualseráoformatodedataaceitaemnossaaplicaç ão. O
diapoderáterumoudoisdígitoseomêstambém,masoanodeverátersempre
quatrodígitos.Vejaalgunsexemplosdedatasqueserãoconsideradasválidaseoutras
inválidastambém:
# Datas válidas
03/07/2012
3/07/2012
03/7/2012
3/7/2012
# Datas inválidas
003/7/2012
3/007/12
3/7/12
03/07/12
03/07
Certo,tendodefinidoosformatosqueserãoaceitospelaaplicaç ãopodemosfazer
avalidação.
Agora,comofaremosisso?Jásabemosquepodemosexplodirumastringusando
umseparadoretransformá-laemumarray.Aípoderíamoscontaroscaracteresde
cadaitemdoarrayparasaberseadataestánoformatoesperado.Issocomcerteza
vaidarumtrabalhãoenãoserámuitoprático.Vejamaisoumenoscomoficariaa
validaçãodestaforma:
<?php
function validar_data($data)
{
$partes = explode('/', $data);
if (count($partes) != 3) {
return false;
114

## Página 131

CasadoCódigo Capítulo9. Validaçãodeformulários
}
$dia = $partes[0];
$mes = $partes[1];
$ano = $partes[2];
if (strlen($dia) < 1 OR strlen($dia) > 2) {
return false;
}
if (strlen($mes) < 1 OR strlen($mes) > 2) {
return false;
}
if (strlen($ano) != 4) {
return false;
}
return true;
}
Nadaprático,né?ImaginevalidaroformatodeumCPFassim,ouumCEP,ou
umCNPJ,ouumcódigodebarrasdeumboletobancário...Enfim,deveexistiralgo
queverificacertospadrõesemumtextoedizseessetextoestánopadrão.
9.6 E xpressões regulares
Esteéumtópicomuitointeressantequemereceumlivrosóparaele,masvamoscom
calma,voumostrarapenasobásiconecessárioparavalidarmosoprazodasnossas
atividadesedeixarasugestãoparaquevocêseaprofundenoassunto,poisrealmente
valeapena.
Expressõesregularesnospermitempesquisartextosdentrodeoutrostextose
verificarsedeterminadostextosseguemumpadrãopredefinido.Usandoexpressões
regularespodemosfazercoisascomoavalidaç ãodoformatoquequeremosparaa
nossadatadoprazodeumaformamuitomaissimplesdoqueaformamanualque
vimosanteriormente.
Usarexpressõesregularesparavalidaroformatodanossadataéalgomaisou
menosassim:
Verifique se o texto começa com um ou dois dígitos, seguido de uma barra, seguido
115

## Página 132

9.6. Expressõesregulares CasadoCódigo
por mais um ou dois dígitos, seguido por mais uma barra e por último uma sequência
de quatro dígitos.
Esteformatoquedeveserencontradoéchamadode padrão eumpadrãoque
valida,porexemplo,apenasumnúmeroéeste:
[0-9]
Issosignificaqualquernúmerode0até9,ouseja,todososdígitosdosistema
decimal. Entãoparavalidardoisnúmerosseguidospoderíamosusarumpadrão
comooseguinte:
[0-9][0-9]
Bastarepetiropadrão,assimteríamosumavalidaç ãoparadoisnúmerossegui-
dos.Masimaginequeprecisássemosvalidar10númerosseguidos,escreveropadrão
10vezesnãoépráticoecomcertezairiadificultarmuitooentendimentodocódigo.
Porisso,existemtambémquantificadoresparaasexpressõesregulares:
[0-9]{10}
Issoquerdizer10vezesumnúmero.Mas,alémdepodercolocarumaquantidade
fixaderepetiçõesdopadrão,podemoscolocarintervalos:
[0-9]{3,5}
Issosignificaumpadrãodetrêsacinconúmeros.Comissopodemosvoltarao
padrãoparavalidaroprazodasatividades:
[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{4}
Lerestaexpressãoregularésimples:“umoudoisnúmeros,barra,umoudois
números,barra,quatronúmeros”. Percebaqueexistembarrasinvertidasantesdas
barras,issoénecessáriopara“escapar”asbarras,ouseja,estamosdizendoparaa
expressãoregularqueelenãodevetratarabarracomoumcaractereespecial.
Agorapodemosmelhorarumpoucoaexpressão,poistemosqueverificarseeste
éoúnicotextodigitadonocampodoprazo.Porisso,precisamosadicionarosca-
racteresquesignificamocome çoeofimdotextoemumpadrão,quesãorespecti-
vamenteoacentocircunflexoeocifrão:
^[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{4}$
116

## Página 133

CasadoCódigo Capítulo9. Validaçãodeformulários
Ufa,expressãoregularjámontadaeprontaparausar.Aliás,umadicalegalaquié
usarosite regexpalparatestarsuasexpressõesregulares: http://regexpal.com/.Este
foiositequeeuuseiparaconstruiretestaranossaexpressãoregular:
Figura9.3:Regexpalsendousadoparatestaravalidaç ãodadata
Certo,jásabemosumbasicãodeexpressõesregulares,agoraprecisamosaplicar
avalidaçãodentrodoPHP.Paraissovamosusarafun ção preg_match(),que
recebeumpadrãoeumtextoparaverificarseotextocasacomopadrão. Vamos
criarumanovafun ção validar_data()noarquivo ajudantes.php:
<?php
...
function validar_data($data)
{
$padrao = '/^[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{4}$/';
$resultado = preg_match($padrao, $data);
return $resultado;
}
...
Ei!Estepadrãoestádiferentedoquefizemos!Calma!Elatemapenasumabarra
nocome çoeoutranofinal,poisesteéumpadrãousadoemalgumaslinguagens,
inclusivenalinguagemPerl,queédeondeoPHPherdaalgumascoisas.
Agoraquejátemosafun çãoparavalidaroprazo,vamosadicioná-lanoarquivo
tarefas.php,jáaproveitandoparacolocaroerrodevalidaç ão:
<?php
...
117

## Página 134

9.6. Expressõesregulares CasadoCódigo
if (isset($_POST[ 'prazo']) && strlen($_POST['prazo']) > 0) {
if (validar_data($_POST['prazo'])) {
$tarefa['prazo'] = traduz_data_para_banco($_POST['prazo']);
} else {
$tem_erros = true;
$erros_validacao['prazo'] = 'O prazo não é uma data válida! ';
}
} else {
$tarefa['prazo'] = '';
}
...
Vejaqueénecessárioprimeiroverificarseexistealgumtextonocampoprazo,
paradepoisusarafun ção validar_data(),poisesteéumcampoopcional.
Precisamosalterartambémoarquivo formulario.phpparaexibiroerrode
validaçãodoprazo:
<?php
...
<label>
Prazo (Opcional):
<?php if ($tem_erros && isset($erros_validacao['prazo'])) : ?>
<span class="erro">
<?php echo $erros_validacao['prazo']; ?>
</span>
<?php endif; ?>
<input type="text" name="prazo" value=
"<?php echo traduz_data_para_exibir($tarefa['prazo']); ?> "
/>
</label>
...
Agorajápodemostentarcadastrarumatarefacomoprazoincorreto,comopor
exemplo“12/12/12":
118

## Página 135

CasadoCódigo Capítulo9. Validaçãodeformulários
Figura9.4:Errodevalidaç ãodoprazo
Massedigitarmosalgocomo“amanhã”noprazo,ouumadatacomo“12/12”,sere-
mosagraciadoscomvárioserros,poisasfun ções traduz_data_para_exibir()
e traduz_data_para_banco(),usadasparamontaroarray &tarefaepara
exibiroformulárioesperamdatascomtrêspartesseparadasportraçosoubarras.
Porisso,vamosadicionarumapequenamodificaç ãonestasduasfun çõesparaque
retornemadatadaformacomoareceberam,casoelanãotenhatrêspartesseparadas
porbarras.Valelembrarqueasfun çõesestãonoarquivo ajudantes.php:
<?php
...
function traduz_data_para_banco($data)
{
if ($data == "") {
return "";
}
$dados = explode("/", $data);
119

## Página 136

9.6. Expressõesregulares CasadoCódigo
if (count($dados) != 3) {
return $data;
}
$data_mysql = "{$dados[2]}-{$dados[1]}-{$dados[0]}";
return $data_mysql;
}
function traduz_data_para_exibir($data)
{
if ($data == "" OR $data == "0000-00-00") {
return "";
}
$dados = explode("-", $data);
if (count($dados) != 3) {
return $data;
}
$data_exibir = "{$dados[2]}/{$dados[1]}/{$dados[0]}";
return $data_exibir;
}
...
Vejaqueapenasadicioneium ifparaverificarseaquantidadedepartesdadata,
apósousodafun ção explode(),éigualatrês.
Agorasim,podemosusaralistadetarefascomavalidaç ãodadataesemoserros
emcasodedatasemformatosincorretos.
Mas... Bem,aindatemosumpequenoproblema,avalidaç ãodoprazoapenas
verificaseoformatodeentradadadataestácorreto,semconsiderarseadataexiste
ounão. Dessemodo,podemosdigitardatascomo“99/99/9999”quenãoteremos
umerrodevalidaç ão,mesmoqueestadatanãoexista.
Validarseumadataéválidaéumaatividadebemchatinha.Sério,alémdeofato
decadamêsterumacertaquantidadededias,aindatemososmaravilhososanos
bissextos,nosquaisfevereirotem29dias.
120

## Página 137

CasadoCódigo Capítulo9. Validaçãodeformulários
AindabemquePHPpossuiafun ção checkdate()queverificaseumadataé
válida.Então,vamosusá-ladentrodanossafun ção validar_data():
<?php
...
function validar_data($data)
{
$padrao = '/^[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{4}$/';
$resultado = preg_match($padrao, $data);
if (! $resultado) {
return false;
}
$dados = explode('/', $data);
$dia = $dados[0];
$mes = $dados[1];
$ano = $dados[2];
$resultado = checkdate($mes, $dia, $ano);
return $resultado;
}
...
Afun ção checkdate()recebetrêsparâmetros,sendooprimeiroomês,o
segundoodiaeoterceirooano.Estafun çãoretorna trueapenasquandoosdados
informadosformaremumadataválida.Experimentecadastrarumaatividadepara
odia30defevereiro,oupara31deabril,oupara32dedezembroevocêsempre
receberáoerrodevalidaç ãodizendoqueadataéinválida.
Nestemomentotemosavalidaç ãofuncionalparaaadiç ãodenovastarefas!
9.7 Validando o formulário de edição de tarefas
Comocadastrodetarefasjáfuncionalevalidando,podemosagoraalteraraediç ão
detarefasparaqueavalidaç ãotambémfuncione.Noarquivo editar.phpadicione
121

## Página 138

9.7. Validandooformuláriodeediçãodetarefas CasadoCódigo
avariáveldecontrole $tem_errose $erros_validacaologoapósavariável
$exibir_tabela:
<?php
...
$exibir_tabela = false;
$tem_erros = false;
$erros_validacao = array();
...
Alteretambémoifqueverificaseexisteosdadosforamenviadosviapost,que
atualmenteusaocampocomonomedatarefa,pelanossafun ção tem_post():
<?php
...
$exibir_tabela = false;
$tem_erros = false;
$erros_validacao = array();
if (tem_post()) {
...
Opróximopassoéalterarotrechoquepegaonomedatarefaparaquefaç aa
validaçãoepreenchaoarraydeerrossenecessário:
<?php
...
if (isset($_POST[ 'nome']) && strlen($_POST['nome']) > 0) {
$tarefa['nome'] = $_POST['nome'];
} else {
$tem_erros = true;
$erros_validacao['nome'] = 'O nome da tarefa é obrigatório! ';
}
...
Etambémdevemosalteraradefiniç ãodocampoprazo,validandocomafun ção
validar_data():
122

## Página 139

CasadoCódigo Capítulo9. Validaçãodeformulários
<?php
...
if (isset($_POST[ 'prazo']) && strlen($_POST['prazo']) > 0) {
if (validar_data($_POST['prazo'])) {
$tarefa['prazo'] = traduz_data_para_banco($_POST['prazo']);
} else {
$tem_erros = true;
$erros_validacao['prazo'] = 'O prazo não é uma data válida! ';
}
}
...
E no final do bloco doif precisamos alterar a chamada da função
editar_tarefa()parausaravariável $tem_erros:
<?php
...
if (! $tem_erros) {
editar_tarefa($conexao, $tarefa);
header('Location: tarefas.php');
die();
}
...
Estetrechotodoficamesmomuitoparecidocomoarquivo tarefas.php,com
apenasalgunspontosdiferentes,masimportantes.
Sevocêtentareditarumatarefanestemomento,jáveráavalida çãofuncionando,
masorepreenchimentodoscamposnãoestaráfuncionandocorretamente.Osvalo-
resexibidosemcasodeerroserãoexatamenteosmesmosqueestãocadastradosno
banco,ouseja,atarefaatual.
Vamosacertaresteproblemaverificandoseexistemdadosno POSTlogoapós
a chamada da função buscar_tarefa() que está bem no final do arquivo
editar.php. Os dados que esta função retorna são armazenados na variável
$tarefa,queéumarraycomosdadosdatarefa. Então,oqueprecisamosfazer
ésubstituirosvaloresrecuperadosdobancopelosqueestãono POST.Vaificaraté
parecidocomapartedavalidaç ão,comadiferen çadequenãoseránecessáriovali-
dar:
123

## Página 140

9.8. Resumo CasadoCódigo
<?php
...
$tarefa = buscar_tarefa($conexao, $_GET['id']);
$tarefa['nome'] = (isset($_POST['nome'])) ?
$_POST['nome'] : $tarefa['nome'];
$tarefa['descricao'] = (isset($_POST['descricao'])) ?
$_POST['descricao'] : $tarefa['descricao'];
$tarefa['prazo'] = (isset($_POST['prazo'])) ?
$_POST['prazo'] : $tarefa['prazo'];
$tarefa['prioridade'] = (isset($_POST['prioridade'])) ?
$_POST['prioridade'] : $tarefa['prioridade'];
$tarefa['concluida'] = (isset($_POST['concluida'])) ?
$_POST['concluida'] : $tarefa['concluida'];
...
Olhaonossoamigoternáriodandoascarasnovamente.Vejaquenestaparteo
quefazemoséaverificaç ãodocampono POSTe,quandoestenãoéencontrado,
usamosovalorpadrãoquejáestánoarray $tarefa.
Nãoprecisamosmaisdealteraçõesparaqueavalidaç ãofuncionetambémna
ediçãodastarefas,poisoformuláriojáestápreparadoparaexibiroserrosquando
necessário.Então,játemosaadiçãoeaediç ãodeatividadesfuncionalecomvalida-
ção.
9.8 R esumo
Ufa,estefoiumcapítuloetantoheim?Parafazeravalidaç ãodeapenasdoiscampos
passamosporalgunstópicosbeminteressantes,comoasfamosasexpressõesregula-
resetambémavalida çãodedatas.Nãofoinecessárioalterarprofundamentenossa
aplicação,somentealgunspontoschaveparaalógicaetambémaexibiç ãodoserros
noformulário.
Paraorepreenchimentodoscamposemcasodeerrosdevalidaç ãousamosos
dadosdoPOST,aproveitandoarequisiç ãoatual.Existemtécnicasdevalidaç ãoque
124

## Página 141

CasadoCódigo Capítulo9. Validaçãodeformulários
guardamosdadosnasessãoeredirecionamousuárioparaumapáginadeerros.
VocêpodeexperimentaroutrastécnicaseatémesmobibliotecasPHPespecializadas
emformuláriosevalidação,massaberofuncionamentofundamentaléimportante,
porissorecomendotreinarmaisvalidaçõesdestaformaquefizemos.
9.9 D esafios
Pensouqueiriaficarsemdesafios?Aquiestãomaisalgunsparapraticar:
• Façaumformulárioquepe çaumCEPevalideovalordigitadousandoopa-
drãoXXXXX-XXX,ouseja,cinconúmeros,umtraçoemaistrêsnúmeros.
• Façaumformulárioquepe çaumCPFevalideseovalorfoidigitadonofor-
matocorreto:XXX.XXX.XXX-XX(Xsãoosnúmeros).Useexpressõesregu-
laresaqui.
• Adicionevalidaçãoparaalistadecontatosquejáestásendofeitanosdesafios
háalgunscapítulos.Tentevalidaraentradadonome,quedeveserobrigatório,
dotelefone,usandooformato“(00)0000-0000”,doe-mailetambémdadata
denascimento.
• Adicionevalidaçãotambémparaoprojetodoestacionamento.Asplacasdos
veículosdevemseguiropadrão“AAA-0000”,ouseja,trêsletrasequatronú-
meros.
125

## Página 143

Capítulo10
Uploaddearquivos
Umatarefabemcomumemaplicaçõeswebéouploaddearquivos.Vezououtranós
acabamosenviandofotos,documentoseoutrostiposdearquivosparasiteseoutras
aplicaçõesweb. Oprocessodeenviodearquivosébemparecidocomoenviode
dadosemformulários,comadiferen çadequeescolhemososarquivosemnossos
computadoresemvezdedigitarouselecionarosdadosemformulários.
Nestecapítulo,veremoscomoenviararquivosparaquesejamtratadospeloPHP
earmazenadosnosistemadearquivos,comreferênciascadastradasnobancode
dados.
10.1 Anexos para a lista de tarefas
Nossalistadetarefasagoratambémteráanexos.Imaginequeousuárioqueiraca-
dastrarumatarefacomo imprimirorelatório equeira,éclaro,anexarorelatórioà
tarefa.
Oarmazenamentodearquivospodeserfeitodealgumasmaneirasdiferentese

## Página 144

10.2. Mudançasnobancodedados CasadoCódigo
utilizaremosumatécnicaquemisturaousodobancodedadoscomosistemade
arquivos.
Antesdecolocaramãonamassaprecisamosdefinircomoseráessesistemade
anexos:
• Teremosumapáginacomosdetalhesdatarefa,ondeestaráoformuláriopara
adicionarosanexos.
• Umatarefapoderáterumoumaisanexos.
• Permitiremosanexarapenasarquivoszipou pdf.
• Ousuáriopoderáremoveroanexo,semremoveratarefa.
Uau,temosumpoucodetrabalhopelafrente,masoresultadoserábeminte-
ressante. Vamoscomeçaralterandoobancodedados,depoisvamosadicionara
páginacomosdetalhesdastarefaseoformulárioparaadicionaranexose,porúl-
timo,faremosotratamentodoenviodosarquivoselistagemdosarquivosnapágina
dedetalhesdatarefa.
10.2 Mudanças no banco de dados
Nossobancodedadosatualpossuiapenasatabela tarefas,entãoprecisamosfa-
zeralteraçõesparaquesejapossívelguardarosdadosrelacionadosaosanexos. Se
adicionarmosumnovocampochamado,porexemplo, anexoàtabela tarefas,
poderemosadicionarapenasumanexoportarefa,masdefinimosqueumatarefa
poderáterváriosanexos,entãoestasoluç ãonãonosatenderá.
Sendoassim,teremosqueadicionarmaisumatabelaemnossobancoparaguar-
darexclusivamenteosanexos. Estanovatabeladeveráguardarumareferênciaàs
tarefasparaquesepossaassociá-lasaseusanexos.Vejacomoficaodiagramapara
anovatabela anexosesuaassociaç ãocomatabela tarefas:
128

## Página 145

CasadoCódigo Capítulo10. Uploaddearquivos
Figura10.1:Diagramadobancocomatabelaanexos
Atabela anexosteráseupróprioidparaidentificaçãodosanexoscomoúnicos
etambémumcampo tarefa_idqueiráguardarumareferênciaaocampo idda
tabela tarefas.
Oscampos idemcadaumadastabelassãochamadosde chavesprimárias,pois
reconhecemcadaregistrocomoúnico.Jáocampo tarefa_idnatabela anexos
guardaumareferênciaaumregistroúnicoemoutratabela,porissoeleéchamado
dechaveestrangeira.
Alémdissoanovatabelatambémterádoiscamposparaguardarmosonomedo
arquivosemsuaextensãoeasualocalizaç ãonosistemadearquivos.
Esseprocessodeseparaç ãodetabelaseusodechavesprimáriasechavesestran-
geirasfazparteda normalizaçãodebancosdedados.Eurecomendoquevocêleia
maisarespeitoparaevitarproblemascomunsdeduplicaç ãodedadoseatémesmo
perdadeinformaçõesrelacionaisembancosdedados.
ParacriaranovatabelaacesseoPHPMyAdminesigaumprocessoparecidocom
oqueusamosparacriaratabeladastarefas,masdessavezocódigoSQLnecessário
paracriaratabela anexoséoseguinte:
CREATE TABLE anexos (
id INTEGER AUTO_INCREMENT PRIMARY KEY,
tarefa_id INTEGER NOT NULL,
nome VARCHAR(255) NOT NULL,
arquivo VARCHAR(255) NOT NULL
);
ApósexecutarestecódigooPHPMyAdmindeveráexibirasduastabelasno
banco tarefas:
129

## Página 146

10.3. Páginacomosdetalhesdastarefas CasadoCódigo
Figura10.2:Astabelasnobancotarefas
10.3 Página com os detalhes das tarefas
Comobancodedadosjáprontoparareceberosanexosdastarefas,vamosparaa
próximaetapa,queéacriaç ãodeumapáginaqueiráexibirosdadosdeumatarefa
eumformulárioparacadastraranexos.
Anossanovapáginaficaránoendere çohttp://localhost/tarefas/tarefa.php?id=
N,ondeNseráoiddatarefaquequeremosexibir.Esteendere çoestaráemumlink
queiremosadicionaragoranalistadetarefas,usandoonomedatarefa.Noarquivo
tabela.phpalterealinhaqueexibeonome,adicionandoolink:
<td>
<a href="tarefa.php?id=<?php echo $tarefa['id']; ?> ">
<?php echo $tarefa['nome']; ?>
</a>
</td>
Estelinkapontaparaoarquivo tarefa.php,queaindanãoexiste. Nosso
próximopassoéacriaç ãodesdearquivo,queteráumaestruturasemelhanteao
tarefas.php,masdeverámostrarapenasumatarefaporvez:
<?php
include "banco.php";
include "ajudantes.php";
$tem_erros = false;
$erros_validacao = array();
if (tem_post()) {
// upload dos anexos
130

## Página 147

CasadoCódigo Capítulo10. Uploaddearquivos
}
$tarefa = buscar_tarefa($conexao, $_GET['id']);
include "template_tarefa.php";
Percebaquejátemostodasasfun çõesqueestãosendousadasnestearquivo.Por
enquanto,vamosdeixarapartedouploadapenascomumcomentárioevamoscriar
oarquivo template_tarefa.php,queestásendoincluídonaúltimalinha:
<html>
<head>
<meta charset="utf-8" />
<title>Gerenciador de Tarefas</title>
<link rel="stylesheet" href="tarefas.css" type="text/css" />
</head>
<body>
<h1>Tarefa: <?php echo $tarefa['nome']; ?> </h1>
<p>
<a href="tarefas.php">Voltar para a lista de tarefas</a>.
</p>
<p>
<strong>Concluída:</strong>
<?php echo traduz_concluida($tarefa['concluida']); ?>
</p>
<p>
<strong>Descrição:</strong>
<?php echo nl2br($tarefa['descricao']); ?>
</p>
<p>
<strong>Prazo:</strong>
<?php echo traduz_data_para_exibir($tarefa['prazo']); ?>
</p>
<p>
<strong>Prioridade:</strong>
<?php echo traduz_prioridade($tarefa['prioridade']); ?>
</p>
<h2>Anexos</h2>
<!-- lista de anexos -->
131

## Página 148

10.4. Oformulárioparacadastraranexos CasadoCódigo
<!-- formulário para um novo anexo -->
</body>
</html>
Estearquivoserveparaexibirosdadosdatarefa,alistadeanexosdecadauma
etambémoformulárioparaadiç ãodenovosanexos.Deixeiostrechoscomalista
deanexosecomoformuláriodeanexosembranco,poisvamospreencherestes
trechosmaisparafrente.Acessealistadetarefasecliquenolinknonomedatarefa
paraacessarapáginacomosseusdetalhes. Vocêdeveráverumapáginaparecida
comesta:
Figura10.3:Páginacomosdetalhesdatarefa
10.4 O formulário para cadastrar anexos
Aindanoarquivo template_tarefa.phpvamoscriaroformulárioparaoenvio
deanexos.Esteformulárioserábemsimpleseteráapenasumcampoparaasele ção
doarquivo,umcampocomo iddatarefaeobotãodeenvio:
...
<!-- formulário para um novo anexo -->
<form action="" method="post" enctype="multipart/form-data">
132

## Página 149

CasadoCódigo Capítulo10. Uploaddearquivos
<fieldset>
<legend>Novo anexo</legend>
<input type="hidden"
name="tarefa_id" value=" <?php echo $tarefa[ 'id']; ?> " />
<label>
<?php if ($tem_erros && isset($erros_validacao[ 'anexo'])):?>
<span class="erro">
<?php echo $erros_validacao['anexo']; ?>
</span>
<?php endif; ?>
<input type="file" name="anexo" />
</label>
<input type="submit" value="Cadastrar" />
</fieldset>
</form>
...
Comojátemosaexperiênciadoformuláriodecadastrodetarefas,jápodemos
deixaroformuláriodecadastrodeanexosprontoparaexibirerrosdevalidaç ão,
mesmosemterfeitoavalidaç ãoainda.
Agora,reparenasdiferen çasdoformuláriodecadastrodeanexosparaoformu-
láriodecadastrodetarefas.Atag <form>doformuláriodecadastrodeanexostem
apropriedade enctype="multipart/form-data",queserveparaindicarpara
onavegadorquenossoformulárioiráfazeroenviodearquivos.Outradiferen çaé
o inputdoanexo,quetemapropriedade type="file,queserveparaindicar
queestecampodeveráserpreenchidocomumarquivoescolhidonocomputador
dousuário.Vejacomoficaesteformulárionapáginacomosdetalhesdatarefa:
133

## Página 150

10.5. RecebendoarquivospeloPHP CasadoCódigo
Figura10.4:Formparaenviodeanexos
10.5 Recebendo arquivos peloPHP
Apósadicionaroformulário,vamosalteraroarquivo tarefa.phpparaqueele
possareceberoarquivo. Faremosavalidaç ãoegravaç ãodoanexonaquele ifque
verificaseexistemdadosnopost.Aestruturaquedevemosconstruiriráverificarse
oarquivofoienviado,depoisiráverificarseoarquivoédotipopdfouzip,afinal,
estesforamosarquivosquedecidimosaceitar. Ésóentãoquefaráagravaç ãodo
nomedoarquivonobancodedados.Estetrechodecódigodeveráficarassim:
<?php
...
if (tem_post()) {
// upload dos anexos
$tarefa_id = $_POST['tarefa_id'];
if (! isset($_FILES['anexo'])) {
$tem_erros = true;
$erros_validacao['anexo'] =
'Você deve selecionar um arquivo para anexar';
} else {
if (tratar_anexo($_FILES['anexo'])) {
$anexo = array();
$anexo['tarefa_id'] = $tarefa_id;
$anexo['nome'] = $_FILES['anexo']['name'];
$anexo['arquivo'] = $_FILES['anexo']['name'];
} else {
$tem_erros = true;
$erros_validacao['anexo'] =
'Envie apenas anexos nos formatos zip ou pdf';
}
}
134

## Página 151

CasadoCódigo Capítulo10. Uploaddearquivos
if (! $tem_erros) {
gravar_anexo($conexao, $anexo);
}
}
...
Percebaqueestaestruturaébemparecidacomagravaç ãodetarefas,asdiferen-
çasestãonousodasduasnovasfun ções: tratar_anexo()e gravar_anexo().
Afun ção tratar_anexo()seráresponsávelporverificarseoanexoestánofor-
matocorretoetambémporcopiá-loparaapastaondeserãoarmazenados.Jáafun-
ção gravar_anexo()seráresponsávelporcadastraroanexonobancodedados,
nomesmoestilodafun ção gravar_tarefa().
Nafun ção tratar_anexo()teremosqueverificarseoarquivoédotipocor-
reto,ouseja,pdfouzipe,quandootipoforcorreto,vamosguardaroarquivoem
umapasta.
Guardar arquivos em pastas? E o banco de dados?
Podeparecerestranho,masnãovamosusarobancodedadospara
guardarosanexosdosusuários.
Oquevamosguardarnobancodedadoséapenasonomedoarquivo,
assimteremosumareferênciaparaacessarcadaarquivoquandoneces-
sário.
Jáosarquivosserãoarmazenadosemumdiretório,umapasta,no
servidor,assimcomoguardamosarquivosemnossoscomputadores.
Estaéumamaneirasimpleseeficienteparalidarcomouploadear-
mazenamentodearquivos.Elamantémobancodedadosmenor,apenas
comosnomesdosarquivosedeixaosarquivosparaosistemadearqui-
vosdosistemaoperacional.Fazsentido,né?
Vejacomodeveráficarafun ção tratar_anexo(),queseráadicionadano
arquivo ajudantes.php:
<?php
...
135

## Página 152

10.5. RecebendoarquivospeloPHP CasadoCódigo
function tratar_anexo($anexo) {
$padrao = '/^.+(\.pdf|\.zip)$/';
$resultado = preg_match($padrao, $anexo['name']);
if (! $resultado) {
return false;
}
move_uploaded_file($anexo['tmp_name'],
"anexos/{$anexo['name']}");
return true;
}
...
Aformaqueestamosusandoparaverificarseoarquivoédotipocorretoéatravés
daextensão. Eaquitemosmaisumusoimportanteparaasexpressõesregulares.
Destavez,estamosusandooponto,queéumaespéciedecuringadasexpressões
regulareseserveparacasarcomqualquercoisa.Logoapósoponto,temososinalde
mais,queindicaqueoponto,ouseja,qualquercoisa,devecasarpelomenosumavez
epodecasardiversasvezes.Estetrecho .+jáserveparacasarqualquertexto,mas
nonossocasoqueremosapenasosarquivosqueterminemcom .pdfou .zip,por
isso,precisamosadicionarostrechos \.pdfe \.zip.Percebaquenestestrechos
queremosqueaexpressãocaseopontoliteral.Paratanto,usamosabarrainvertida
antesdele,parafazero escapedoponto,poisissosignificaalgocomo“ei,expressão
regular,aquieuqueroumpontomesmo,nãoqualquercoisa,comoéopadrãodo
ponto”.
Aindatemmaisumdetalheimportantenestaexpressãoregular,queéousodo
ou,poisprecisamosqueoarquivoseja zipou pdf.Issoéfeitousandoosparênteses
eopipe(barravertical),assim: (isso|aquilo),estaexpressãocasariaaspalavras isso
ouaquilo.
Nãofaleiqueasexpressõesregularesmerecemumlivrosóparaelas?
Muitobem,apóscasaraexpressãoregular,movemosoarquivotemporáriopara
oseudestinofinal.
136

## Página 153

CasadoCódigo Capítulo10. Uploaddearquivos
Arquivo temporário? O que tem no $_FILES?
QuandoenviamosumarquivoatravésdeumformulárioparaoPHP,
elecriaasuperglobal $_FILES,simnomesmoestilodassuperglo-
bais $_GETe $_POST.Cadacampodotipo fileécolocadoem
umarraydentrode $_FILES,porissoconseguimoschamarafun ção
tratar_anexo()passandooíndice anexo,queéonomedocampo
doanexononossoformulário.
Cadaíndicedo $_FILESéumarrayquecontémosseguintesíndices:
•name:nomedoarquivo;
•type:otipomimedoarquivo;
•tmp_name:onomeondeoarquivofoisalvotemporariamente;
•error:umnúmeroquerepresentaumerronoupload.Zerosigni-
ficaqueestátudocerto;
•8size:Otamanhodoarquivo.
Oarquivoenviadoparaoservidorégravadoemumnometemporá-
rio,porissoprecisamospegá-loecopiarparaseudestinofinal.Vejaque
afun ção tratar_anexo()estámovendooarquivotemporáriopara
umapastachamada anexos,queaindanãoexiste.
Para mover o arquivo para sua localização final usamos a função
move_uploaded_file(), que faz o que seu nome diz, verificando se o ar-
quivodeorigemrealmentefoienviadoparaoPHPatravésdeumformuláriona
requisiçãoatual.
137

## Página 154

10.6. Gravandoosdadosdoanexonobancodados CasadoCódigo
A pasta de uploads
Estamosenviandoosarquivosparaumapastachamada anexos
usandoafun ção move_uploaded_file()e,paraqueissofuncione,
elaprecisaexistir. Então,crieumapastachamada anexosnamesma
pastaondeestáoarquivo tarefas.php,ousejaa tarefas.
ATENÇÃO:UsuáriosdesistemasGNU/LinuxeMacOSX(ououtros
baseadosemUnix)deverãodarpermissãodeescritaparaoApacheno
diretóriodeupload.Um chmod 777 anexos/resolve,masvocêtam-
bémpodemudarogrupodestediretórioedarpermissãoparaoservidor
web.
Afun ção tratar_anexo()retorna trueou false.Casoseja true,cria-
mosumarraynovochamado $anexoeguardamosneleosdadosdoupload;sefor
falsegeramosumerroqueseráexibidonoformulário.
10.6 Grav ando os dados do anexo no banco dados
Estandotudocertocomoupload,vamosparaagravaç ãodosdadosnobancousando
afun ção gravar_anexo(),queficaránoarquivo banco.php:
<?php
...
function gravar_anexo($conexao, $anexo)
{
$sqlGravar = "INSERT INTO anexos
(tarefa_id, nome, arquivo)
VALUES
(
{$anexo['tarefa_id']},
'{$anexo['nome']}',
'{$anexo['arquivo']}'
)
";
mysqli_query($conexao, $sqlGravar);
}
138

## Página 155

CasadoCódigo Capítulo10. Uploaddearquivos
...
Semmuitossegredos,certo? Amaiordiferen çaparaagravaç ãodosdadosde
umatarefaestánocampo tarefa_id,queguardaumareferênciaàtarefaàqual
esteanexopertence. Comojáfaleianteriormentenestecapítulo,issofazparteda
normalizaçãodebancosdedadosevaleumestudoadicionalsobreoassunto.
10.7 Exibindo os anexos
Agoraprecisamosbuscarosanexosnobancoparapoderfazerumalistanapá-
ginacomosdetalhesdatarefa. Paraissovamosusarumafun çãonovachamada
buscar_anexos(),quereceberá,comosempre,aconexãoetambémo iddatarefa.
Adicioneachamadadestafun çãonofinaldoarquivo tarefa.php,logoabaixoda
linhaquebuscaosdadosdatarefa:
<?php
...
$tarefa = buscar_tarefa($conexao, $_GET['id']);
$anexos = buscar_anexos($conexao, $_GET['id']);
include "template_tarefa.php";
...
Jáafunção buscar_anexos()deveráseradicionadanoarquivo banco.php:
<?php
...
function buscar_anexos($conexao, $tarefa_id)
{
$sql = "SELECT * FROM anexos WHERE tarefa_id = {$tarefa_id}";
$resultado = mysqli_query($conexao, $sql);
$anexos = array();
while ($anexo = mysqli_fetch_assoc($resultado)) {
$anexos[] = $anexo;
}
139

## Página 156

10.7. Exibindoosanexos CasadoCódigo
return $anexos;
}
...
Quasesemdiferen çasparaafun ção buscar_tarefas(),né? Basicamente,
mudasóocódigoSQLqueestamosusando.VejaqueaconsultaSQLfiltraapenasas
tarefasquecontenhamocampo tarefa_idcomovalordatarefaquequeremos
exibir.Comoocampo tarefa_idéumachaveemoutratabela,atabela tarefas,
elaéchamadadechaveestrangeira.Ops,jáfaleisobreisso,masébomrefor çar.:)
Para exibir os anexos, precisamos adicionar uma tabela no arquivo
template_tarefa.php, logo abaixo do H2 que diz “Anexos” e acima do
formulárioparacadastrarumanexo. Paracriaratabelavamosusaravariável
$anexosquecontémoresultadodafun ção buscar_anexos():
...
<h2>Anexos</h2>
<!-- lista de anexos -->
<?php if (count($anexos) > 0) : ?>
<table>
<tr>
<th>Arquivo</th>
<th>Opções</th>
</tr>
<?php foreach ($anexos as $anexo) : ?>
<tr>
<td><?php echo $anexo['nome']; ?> </td>
<td>
<a href="anexos/ <?php echo $anexo['arquivo']; ?> ">
Download
</a>
</td>
</tr>
<?php endforeach; ?>
</table>
<?php else : ?>
140

## Página 157

CasadoCódigo Capítulo10. Uploaddearquivos
<p>Não há anexos para esta tarefa.</p>
<?php endif; ?>
<!-- formulário para um novo anexo -->
...
Vejaqueestamosverificandosealistadeanexostemalgumíndiceantesdetentar
exibiralista.Cadaitemdalistatemumelemento aquefazumlinkparaodownload
doarquivo.Aquinãotemsegredos,éumlinknormalqueapontaoarquivoguardado
napasta anexos.
Experimentefazerouploaddoarquivo,suapáginadedetalhesdatarefadeverá
ficarparecidacomesta:
Figura10.5:Páginacomosdetalhesdatarefa,alistadeanexoseoformuláriopara
cadastrarnovosanexos
141

## Página 158

10.8. Resumo CasadoCódigo
10.8 Resumo
NestecapítulotratamosdouploaddearquivosusandoPHP.Osuploadssãocoloca-
dosdentrodasuperglobal _FILES.Alémdissocriamosumanovatabelanobanco
eusamosmaisumpoucodeexpressõesregularesparavalidarotipodearquivoen-
viado.
10.9 Desafios
Depoisdetrabalharduronoenviodearquivosparaastarefas,vamosparamaisal-
gunsdesafios!
• Nalistadecontatos(sim,aqueladosdesafiosanteriores):1)adicioneumapá-
ginaparaexibirosdetalhesdecadacontato;2)adicioneouploaddefotos
paraalistadecontatos. Lembre-sedevalidarseoarquivoéumaimagem,
como jpg, pngetc.;3)adicioneafotodocontatonapáginadedetalhes.
• Noprojetodoestacionamento,adicioneumaopçãoparauploaddafotodo
carronomomentoemqueentrouenomomentoemquesaiudoestaciona-
mento.Issoéumagarantiaqueosclientespediram,poisalgunsdisseramque
seusveículosforamamassadosdentrodoestacionamento.
142

## Página 159

Capítulo11
Lembretesdetarefaspore-mail
Ébemcomumquediversostiposdeaplicaçõeswebenvieme-mailsparaosusuários
comalgumtipodeinformaç ãoetambémlembretes.Porissovamosadicionaruma
opçãoemnossalistadetarefasparaenviare-mailscomlembretesdastarefas.
Estenãoseráotipodelembretequeéenviadoautomaticamentenodiadefinido
comoprazoparaatarefa.Oquefaremoséaadiç ãodeumcheckbox Enviarlembrete
nosformuláriosdecriaçãoeediç ãodetarefase,quandoestaop çãoestivermarcada,
vamosenviaroe-mailparaumendere çodee-mailquedeixaremoscadastradono
código.
OPHPpossuialgumasop çõespadrãoparaenviodee-mails,masdestavezva-
mosusarumabibliotecaadicionalquefacilitaránossotrabalho.
11.1 Definindo o e-mail de aviso
Oe-maildeavisoseráumHTMLsimplescomosdadosdatarefa.Aideiaémandar
pore-mailumapáginabemparecidacomapáginadedetalhese,quandonecessário,

## Página 160

11.1. Definindooe-maildeaviso CasadoCódigo
adicionartambémosanexosdatarefaaoe-mail.Eéaquiqueabibliotecadeenvio
dee-mailsserábastanteútil!
Ocorpodonossoe-mailficaráemumnovoarquivoquevamoschamarde
template_email.php.Estearquivodeveráficarjuntocomosdemaisdentrodo
diretório tarefas,eseuconteúdoseráapenaseste:
<h1>Tarefa: <?php echo $tarefa['nome']; ?> </h1>
<p>
<strong>Concluída:</strong>
<?php echo traduz_concluida($tarefa['concluida']); ?>
</p>
<p>
<strong>Descrição:</strong>
<?php echo nl2br($tarefa['descricao']); ?>
</p>
<p>
<strong>Prazo:</strong>
<?php echo traduz_data_para_exibir($tarefa['prazo']); ?>
</p>
<p>
<strong>Prioridade:</strong>
<?php echo traduz_prioridade($tarefa['prioridade']); ?>
</p>
<?php if (count($anexos) > 0) : ?>
<p><strong>Atenção!</strong> Esta tarefa contém anexos!</p>
<?php endif; ?>
Reparequeestetemplateparaoe-mailébemparecidocomapáginadedetalhes
datarefa,aquelaquetemoformulárioparaadicionaranexos. Adiferen çaéque
aquinãoprecisamosexibirolinkparavoltarparaalistadetarefasetambémnão
precisamosexibirosanexos,apenasumainformaç ãodequeexistemanexosparaa
tarefa.
Agoravamosdeixaressearquivoguardadoumpoucoevamosajustaroutros
pontosdaaplicação.Certo,euseiqueéchatoescrevercódigoenãoverofunciona-
mento,masacheimelhorjádeixarmosestearquivoprontoagora,paranãoatrapalhar
oraciocíniomaisparafrente.
144

## Página 161

CasadoCódigo Capítulo11. Lembretesdetarefaspore-mail
11.2 Unificando a configuração da aplicação com
constantes
Atéagoranossaaplica çãonãotemmuitositensconfiguráveis,naverdadetemosape-
nasosdadosdeconexãocomobancodedados.Mas,apartirdeagora,teremosuma
configuraçãoparadefiniroendere çodee-mailparaondeose-mailsdeavisoserão
enviados.
Tudobem,aindasãopoucasinformações,mas,acredite,émelhorcome çara
organizaçãoaindapequeno,poisfacilitaocrescimento.
Muitobem,vamoscriarentãoumnovoarquivoparamanterasconfigurações
danossaaplicaç ão.Eleseráo config.phpedeverásercolocadocomosdemais
arquivosnapasta tarefas.Inicialmente,eledeveráconterosdadosdeconexãoao
bancoetambémoe-maildeavisodastarefas.Vejacomodeveráficarseuconteúdo:
<?php
// Conexão ao banco de dados (MySQL)
define("BD_SERVIDOR", "127.0.0.1");
define("BD_USUARIO", "sistematarefa");
define("BD_SENHA", "sistema");
define("BD_BANCO", "tarefas");
// E-mail para notificação
define("EMAIL_NOTIFICACAO", "meuemail@meudominio.com.br");
Nestearquivoestamosusandoafun ção define()queserveparadefinir cons-
tantesnoPHP.Afun ção define()recebeonomedaconstanteeoseuvalor.Uma
constanteéumidentificadorparaumvalorquenãoseráalteradoduranteaexecuç ão
daaplicação.
Ficafácilentenderasconstantesquandojáconhecemosbemasvariáveis,que
sãoidentificadoresparavaloresquepodemmudar,porissotêmonomede variáveis.
Paraexibirasconstantesusamosapenasseusnomes,semocifrãonafrente,como
asvariáveis.Vejaumexemplo:
<?php
$linguagem = "PHP";
define("BANCO", "MySQL");
echo "Eu uso {$linguagem} com o banco " . BANCO;
// Exibe: Eu uso PHP com o banco MySQL
145

## Página 162

11.2. Unificandoaconfiguraçãodaaplicaç ãocomconstantes CasadoCódigo
Reparequeestoudeixandoasconstantessempreemcaixaalta,ouseja,todasas
letrasemmaiúsculo.Issonãoéobrigatório,maséumpadrãoqueopessoaldoPHP
segue,poisdestamaneiraficafácildeidentificarondeelasestãoemumcódigo.
Nonossoarquivo banco.phpdefinimosquatrovariáveisparaguardarosdados
deacessoaobancodedados.Masessesvaloresnãodeverãomudarduranteousoda
aplicação,porissoelespoderiamficaremconstantes.Agora,porexemplo,avariável
$tarefarecebenovosdadosequepodemseralterados,porissonãopodeseruma
constante.Aliás,asconstantesnãopodemserdefinidascomo arrays!Apenasvalores
comonúmerosestrings.
Vamosentãoalteraroarquivo banco.phpparausarnossasnovasconstantes
paraacomunicaç ãocomobanco. Apagueadefiniç ãodasvariáveiscomosdados
deacessoaobancoemudeachamadadafun ção mysqli_connect()parausaras
constantes:
<?php
$conexao = mysqli_connect(BD_SERVIDOR, BD_USUARIO, BD_SENHA, BD_BANCO);
...
Vejacomoumarápidaolhadanocódigojánosrevelaqueestamosusandocons-
tantes,graçasaousodacaixaalta.
Sevocêtentaracessarsuaaplicaç ãoagora,vaiencontraralgunserrosdizendo
queosidentificadoresusadosnãoforamdefinidos,poisaindanãoadicionamoso
novoarquivo config.phpnaaplicação.
Nossaaplicaçãotemdiversospontosdeentrada,quesãoosarquivosqueesta-
moschamandodiretamentepeloendere çononavegador.Oarquivo tarefas.php,
porexemplo, éumpontodeentrada, poiseleéchamadopelonavegador. Jáo
template.phpéincluídoporoutrosarquivos,entãonãoéumpontodeentrada.
Precisamosalterartodosospontosdeentradaparaincluiroarquivodeconfigu-
ração. Então, adicionealinhaaseguirnoiníciodosarquivos tarefas.php,
tarefa.php, editar.phpe remover.php:
<?php
include "config.php"; // Esta é a nova linha
include "banco.php";
...
146

## Página 163

CasadoCódigo Capítulo11. Lembretesdetarefaspore-mail
Lembre-sequeoarquivo banco.phpdependedasconstantesdefinidasnoar-
quivo config.php,entãoestedeveserincluídoprimeiro.
11.3 Adicionando a opção de aviso por e-mail
Ousuárioprecisainformarquequerreceberpore-mailumlembretedatarefa,por
issoprecisamosalteraroformulário,adicionandoumcheckboxcomaop çãodeen-
viodoe-mail.
Vamosalteraroarquivo formulario.phpparaadicionaranovaop çãologo
abaixodaop çãodetarefaconcluída:
...
<label>
Tarefa concluída:
<input type="checkbox" name="concluida" value="1"
<?php echo ($tarefa[ 'concluida'] == 1) ? 'checked' : ''; ?>
/>
</label>
<label>
Lembrete por e-mail:
<input type="checkbox" name="lembrete" value="1" />
</label>
...
VejaqueéapenasumcheckboxHTMLcomonome lembreteeovalor 1.
Estecamposeráverificadoduranteagravaç ãoeduranteaediç ãodeumatarefae,
casosejanecessário,oe-mailcomoavisoserádisparado.
Vamos fazer a alteração primeiro na gravação de novas tarefas, que fica
no arquivo tarefas.php. O envio do e-mail será feito usando a função
enviar_email(),queaindanãoexiste. Essafun çãoreceberácomoparâmetros
apenasosdadosdatarefaeosdadosdosanexos,sendoquenemsempreumatarefa
teráanexos,entãooparâmetrodosanexosseráopcional.Opcional?Calma,veremos
issologomais.
Anossaprimeiraalteraç ãoseránagravaç ãodatarefa,entãonãoprecisaremos
enviarosdadosdosanexos,poisnossaaplicaç ãosópermiteadicionaranexosna
páginadedetalhesdatarefa.
147

## Página 164

11.3. Adicionandoaopçãodeavisopore-mail CasadoCódigo
Noarquivo tarefas.php,logoapósagravaç ãodatarefausandoafun ção
gravar_tarefa(),adicioneum ifqueverificaqueaop çãodelembretefoimar-
cadaeentãochamaafun ção enviar_email():
<?php
...
if (! $tem_erros) {
gravar_tarefa($conexao, $tarefa);
if (isset($_POST['lembrete']) && $_POST['lembrete'] == '1') {
enviar_email($tarefa);
}
header('Location: tarefas.php');
die();
}
...
Vejaqueafun ção enviar_email()estásendochamadacomapenasumpa-
râmetro,quesãoosdadosdatarefa.
Agora,alteretambémoarquivo editar.php.Essaalteraçãoserábemparecida
comaanterior,masaquiprecisamosmandartambémosdadosdosanexos.Então,
ficaassim:
<?php
...
if (! $tem_erros) {
editar_tarefa($conexao, $tarefa);
if (isset($_POST['lembrete']) && $_POST['lembrete'] == '1') {
$anexos = buscar_anexos($conexao, $tarefa['id']);
enviar_email($tarefa, $anexos);
}
header('Location: tarefas.php');
die();
}
148

## Página 165

CasadoCódigo Capítulo11. Lembretesdetarefaspore-mail
...
Comojátemosalógicaparapegarosanexosdentrodeumafun ção,bastachamá-
laepegarseuresultadoparatermososanexos.
Agoraquejápreparamosaaplicaç ãoparaenviarose-mails,vamosfinalmente
paraafun ção enviar_email()!
11.4 Afunção enviar_email()
Antesdeescreverafun çãoparaenviare-mails,vamospensarnoqueénecessário
fazerparaenviarume-mailusandoumsistemacomooGMailoutroswebmails.
Voucolocaraquiopassoapassodoqueénecessárioparaenviarume-mail:
• Acessarosistemadee-mails;
• Fazeraautenticaçãocomusuárioesenha;
• Usaraopçãoparaescreverume-mail;
• Digitaroe-maildodestinatário;
• Digitaroassuntodoe-mail;
• Escreverocorpodoe-mail;
• Adicionarosanexosquandonecessário;
• Usaraopçãodeenviaroe-mail.
Nossa!Umatarefatãosimplescomoenviarume-mailvirouumaatividadedi-
vididaemoitopassos!Então,paraenviarume-mailusandoPHPdeveseralgobem
parecido.Sendoassimvamoscriarafun çãoparaenviarose-mailsusandoummonte
decomentários,quevãonosguiarparaaimplementaç ãodocódigo. Noarquivo
ajudantes.php,adicioneafun ção enviar_email():
<?php
...
function enviar_email($tarefa, $anexos)
{
149

## Página 166

11.4. Afunçãoenviar_email() CasadoCódigo
// Acessar o sistema de e-mails;
// Fazer a autenticação com usuário e senha;
// Usar a opção para escrever um e-mail;
// Digitar o e-mail do destinatário;
// Digitar o assunto do e-mail;
// Escrever o corpo do e-mail;
// Adicionar os anexos quando necessário;
// Usar a opção de enviar o e-mail.
}
Agorajátemosumaespéciedemapaqueiránosguiar. Mas,antesdeseguir
omapaefazerafun çãorealmentemandare-mails, reparenosparâmetrosque
estafun çãopodereceber. Vejaquetemosumavariável $tarefaeumavariável
$anexos.Oproblemaquecome çaanosperturbarésaberqueapósagravaç ãoda
tarefaestamoschamandoessafun çãocomapenasumparâmetro,enquantoquena
ediçãoestamospassandoosdois.Issocertamentevaigerarumerro,poisprecisamos
fornecerosparâmetrosobrigatóriosdeumafun ção.
Parâmetros de funções
Emgeralasfun çõesrecebemparâmetrosefazemalgumtipodetra-
balhorepetitivocomeles.Masalgumasvezespodemosprecisardefun-
çõesquepodemreceberumcertoparâmetrooupodemteralgumtipo
devalorpadrãoparaum.
Esteéexatamenteonossocasonafun ção enviar_email(),pois
oquerealmenteseránecessáriosempresãoosdadosdastarefas,afinal
nãopodemosenviarume-mailsemisso.Jáosanexosserãoopcionais,já
quepodemosmuitobemtertarefassemanexos.
Parafazercomqueumparâmetrosejaopcionalemumafun çãoPHP
bastaatribuirumvalorlogoapósadeclaraç ãodoparâmetronafun ção:
function pular_linha($c = '<br />') { echo $c; }
Afun ção pular_linha()porpadrãopulaumalinhanoHTML
usandoatag <br/>,maspoderíamostrocarocomportamentopadrão
chamandoafun çãoefalandoparapularlinhaemumarquivotxtusando
ocaractere\n:
pular_linha("\n");
150

## Página 167

CasadoCódigo Capítulo11. Lembretesdetarefaspore-mail
Comoalistadeanexoséumarray,podemosalteraradeclaraç ãodafun ção
enviar_email()paraterumalistadeanexosvaziaporpadrão:
<?php
...
function enviar_email($tarefa, $anexos = array())
{
...
}
...
Agoravamosvoltaràlistadepassosparaenviaroe-mail. Praticamentealista
dependedealgumtipodecomunicaç ãocomosistemadee-mails,menosoitem
escreverocorpodoe-mail,eatéjátemosoarquivo template_email.phpcom
otemplate.Então,vamoscome çarporesteitem.
11.5 Escrevendo o corpo do e-mail usando um ar-
quivo com o template
Paracolocarotextodocorpodoe-mailefetivamentedentrodoe-mail,precisamos
usaralgumaformadeleroarquivo template_email.php,colocandooseucon-
teúdojáprocessado(comosvaloresdasvariáveisetc.) dentrodeumavariável. É
algumacoisaparecidacomisso:
<?php
...
function enviar_email($tarefa, $anexos = array())
{
$corpo = include "template_email.php";
}
Oarquivo template_email.phpprecisadasvariáveis $tarefae anexos,
quejáestãosendorecebidaspelafun ção.Aideiaaquiéqueavariável $corpofique
comoHTMLresultantedoprocessamentodoarquivo template_email.php.
Infelizmente esse código não irá funcionar e o conteúdo do arquivo
template_email.phpseráenviadoparaonavegador.
151

## Página 168

11.5. Escrevendoocorpodoe-mailusandoumarquivocomotemplate CasadoCódigo
Para resolver este problema vamos separar essa lógica de ler o arquivo
template_email.phpemumanovafun ção,poisassimvaificarmaissimplesler
eentenderefun ção enviar_email():
<?php
...
function enviar_email($tarefa, $anexos = array())
{
$corpo = preparar_corpo_email($tarefa, $anexos);
...
}
function preparar_corpo_email($tarefa, $anexos)
{
// Aqui vamos pegar o conteúdo processado do template_email.php
}
Agoraqueseparamosalógicaparaprepararocorpodoe-mail,vamospensarem
comoissodeveserfeito.Onossomaiorproblemaéque,seincluirmosumarquivo
comHTMLusandoo include,seuconteúdoseráenviadoparaonavegador,então
temosquefazerumpassoapassodessaforma:
• FalarparaoPHPquenãoéparaenviaroprocessamentoparaonavegador;
• Incluiroarquivotemplate_email.php;
• Guardaroconteúdodoarquivoemumavariável;
• FalarparaoPHPqueelepodevoltaramandarconteúdosparaonavegador.
Estamoscheiosdelistasdescrevendoosprocedimentosnestecapítulo,heim?
Maséporumaboarazão,jáqueissoajudaapensarprimeironalógicaedepoisna
implementaçãousandoPHP.
Parafazerafun ção preparar_corpo_email()vamosusaralgumasfun ções
doPHPquefazemexatamenteoquefoidescritonalistaanterior. Essasfun ções
impedemoPHPdeenviarconteúdosparaonavegadorenospermitempegaresses
conteúdoseguardaremvariáveis.Vejacomoficasimplesaimplementaç ão:
152

## Página 169

CasadoCódigo Capítulo11. Lembretesdetarefaspore-mail
<?php
...
function preparar_corpo_email($tarefa, $anexos)
{
// Aqui vamos pegar o conteúdo processado do template_email.php
// Falar para o PHP que não é para enviar o processamento para o
// navegador:
ob_start();
// Incluir o arquivo template_email.php:
include "template_email.php";
// Guardar o conteúdo do arquivo em uma variável;
$corpo = ob_get_contents();
// Falar para o PHP que ele pode voltar a mandar conteúdos para o
// navegador.
ob_end_clean();
return $corpo;
}
Eudeixeioscomentáriosdepropósito,poiselessãoamesmalistadepassosque
fizemosparamontaralógica.Depoisvocêpodeapagá-los.
Nafun ção preparar_corpo_email(),usamosafun ção ob_start(),que
colocaumaespéciedecancelanofluxoqueoPHPenviaparaonavegador.Depois
fizemosainclusãodoarquivo template_email.php,aquelequefizemosláno
começodestecapítulo,usandoainstruç ãoinclude.Aívemumapartebemmágica
emqueusamosafun ção ob_get_contents(),quefazalgocomopegartodo
mundoqueestavaesperandoacancelaabrirparapassareretornaessevalorparaa
variável$corpo. Porúltimo,usamosafun ção ob_end_clean()parafinalizar
oprocesso,queétiporeabriracancelaedeixarosnovosdadospassaremparao
navegador.
Complicado?Sim,umpouquinho,masésótreinarparadominaressatécnica.
Senãofosseporestatécnicateríamosquefazeralgocomoumavariáveldetextocom
todooHTMLnecessárioeasvariáveis.
153

## Página 170

11.6. Instalandoumabibliotecaparaenviare-mails CasadoCódigo
11.6 Instalando uma biblioteca para enviar e-mails
Nossafun ção enviar_email()játemocorpodoe-mail,masaindatemvários
passosqueelanãofazequeserãofeitoscomaajudadeumabibliotecaparae-mails.
Existemváriasbibliotecasparaenviodee-mailsusandoPHP,inclusivealgumas
opçõesembutidasnoPHP.Aideiadeusarumabibliotecaadicionalnestelivroé
mostrarcomoissopodeserfeito,alémdesupriralgunspontosqueseriambemtra-
balhososdefazercomasop çõespadrão,comoanexararquivos.
AbibliotecaescolhidaéaPHPMailer.Parabaixá-laacesse https://github.com/
PHPMailer/PHPMailerecliquenobotão Download ZIP,conformeaimagema
seguir:
Figura11.1:BaixandooPHPMailernoGitHub.Aop çãoestánocantoinferiordireito
Apósbaixar,crieumnovodiretório,umapastachamada bibliotecas,den-
trodapasta tarefas,edescompacteoconteúdodozipdentrodela. Apósdes-
compactarvocêveráumanovapastachamada PHPMailer-master.Renomeie-a
paraapenas PHPMailer.Depoisderenomearvocêvaificarcomumaestruturade
pastasassim:
tarefas > bibliotecas > PHPMailer
Valelembrarquenossoprojetoestádentrodapasta tarefas.
154

## Página 171

CasadoCódigo Capítulo11. Lembretesdetarefaspore-mail
Agorapodemosvoltarparaafun ção enviar_email().
11.7 Finalizando a função enviar_email()
Parafinalizarafun ção enviar_email(),precisamosusarabibliotecaPHPMailer.
Veremosagoraalgumaslinhasdecódigoumpoucodiferentesdoquejávimosaté
aqui,poisabibliotecaPHPMailerusaumnegóciochamado ProgramaçãoOrien-
tadaàObjetos.
Deformasimplificadapodemospensarqueum objetoéumaestruturaquepode
terváriasvariáveisdentrodela,assimcomoosarrays,etambémpodeterfun ções
dentrodela,queservemparamanipularsuasvariáveis.
Lembradalistadepassosnecessáriosparaseenviarume-mail? Vamosagora
preencherestalistausandoasop çõesdaPHPMailer.Voucolocarocódigopassoa
passo,depoisjuntamostudonafun ção.
OprimeiropassoéincluiraPHPMailer:
<?php
...
include "bibliotecas/PHPMailer/PHPMailerAutoload.php" ;
Ospróximospassossãooacessoaosistemadee-mails,aautenticaç ãoeaop ção
deescreverumnovoe-mail:
<?php
...
// Acessar o sistema de e-mails;
// Fazer a autenticação com usuário e senha;
// Usar a opção para escrever um e-mail;
$email = new PHPMailer(); // Esta é a criação do objeto
$email->isSMTP();
$email->Host = "smtp.gmail.com";
$email->Port = 587;
$email->SMTPSecure = 'tls';
$email->SMTPAuth = true;
$email->Username = "meuemail@gmail.com";
155

## Página 172

11.7. Finalizandoafunçãoenviar_email() CasadoCódigo
$email->Password = "minhasenha";
$email->setFrom("meuemail@gmail.com", "Avisador de Tarefas");
Neste último trecho, bastante coisa aconteceu! Primeiro, criamos oobjeto
$emailusandoaclasse PHPMailer.Nãosepreocupecomissoainda,apenasen-
tendaquenoobjeto $emailtemvariáveisefun çõesembutidas.Acessamosestas
variáveisefunçõesusandoaseta,queéosinaldemenosseguidoporumsinalde
maior: ->.Identificamosoqueévariáveleoqueéfun çãousandoosparêntesesnas
funções.
Comoeuqueroenviaroe-mailusandooGMail,preciseidizerqueotipode
conexãoé SMTP,oendere çodoservidoré smtp.gmail.com,aportaparaconexão
éa 587equeeletemqueusaracriptografia tls. Alémdisso,tambémfaleique
énecessárioautenticarnoSMTPusandoousuário(Username)esenha(Password)
informados.Porúltimo,eucoloqueio Fromdoe-mail,paradizerdeondeoe-mail
partiu.
O próximo passo é o destinatário usando a nossa constante
EMAIL_NOTIFICACAO:
<?php
...
// Digitar o e-mail do destinatário;
$email->addAddress(EMAIL_NOTIFICACAO);
Agoratemoassuntodoe-mail:
<?php
...
// Digitar o assunto do e-mail;
$email->Subject = "Aviso de tarefa: {$tarefa['nome ']}";
Temtambémocorpodoe-mail,quevamosenviarusandoHTMLparadeixar
formatado:
<?php
...
// Escrever o corpo do e-mail;
$corpo = preparar_corpo_email($tarefa, $anexos);
$email->msgHTML($corpo);
156

## Página 173

CasadoCódigo Capítulo11. Lembretesdetarefaspore-mail
Osanexos,quandoexistirem,sãoospróximos:
<?php
...
// Adicionar os anexos quando necessário;
foreach ($anexos as $anexo) {
$email->addAttachment("anexos/{$anexo['arquivo']}");
}
Vejaqueo foreachfoiusadoparaosanexos. Casooarray $anexosesteja
vazio,elesimplesmentenãoentranolaço.
Agorasófaltaaop çãodeenviaroe-mail!Vejacomofica:
<?php
...
// Usar a opção de enviar o e-mail.
$email->send();
Ufa!Esseétodoocódigonecessárioparaenviaroe-mail!Sepensarbem,étipo
opassoapassoparaenviarume-mail,apenascodificamosemPHP.Vejacomofica
afun ção enviar_email()completaesemoscomentários:
<?php
function enviar_email($tarefa, $anexos = array())
{
include "bibliotecas/PHPMailer/PHPMailerAutoload.php";
$corpo = preparar_corpo_email($tarefa, $anexos);
$email = new PHPMailer();
$email->isSMTP();
$email->Host = "smtp.gmail.com";
$email->Port = 587;
$email->SMTPSecure = 'tls';
$email->SMTPAuth = true;
$email->Username = "meuemail@email.com";
$email->Password = "minhasenha";
$email->setFrom("meuemail@email.com", "Avisador de Tarefas");
157

## Página 174

11.7. Finalizandoafunçãoenviar_email() CasadoCódigo
$email->addAddress(EMAIL_NOTIFICACAO);
$email->Subject = "Aviso de tarefa: {$tarefa[ 'nome']}";
$email->msgHTML($corpo);
foreach ($anexos as $anexo) {
$email->addAttachment("anexos/{$anexo['arquivo']}");
}
$email->send();
}
Adiferen çaéqueeucoloqueiousodafun ção preparar_corpo_email()
logonocome ço.
Agorajápodemosusaraop çãodeavisarpore-mail!Euediteiumatarefaque
temanexosemarqueiaop çãoparaavisar:
Figura11.2:Editandoumatarefaemarcandoaop çãodelembrete
Evejasócomooe-mailchegouparamim:
158

## Página 175

CasadoCódigo Capítulo11. Lembretesdetarefaspore-mail
Figura11.3:E-maildeavisonoGMail,comanexo
OusodaPHPMailerfacilitabastanteotrabalhoparaenviodee-mails,poisreduz
praticamenteaopassoapassoseguidoparaenviarumusandoumwebmail,sem
maiorescomplicações.
Não uso o GMail
O pessoal do PHPMailer tem alguns exemplos de como fazer a
partedaconexãousandooutrosservidoresalémdoGMail. Parasa-
bermaisacesse https://github.com/PHPMailer/PHPMailer/tree/master/
examples
Dica importante!
Eviteusaroseue-mailpessoalparaenviare-mailsemumaaplicaç ão
comoanossa,poisseuusuárioesenhaficamexpostosnocódigo.
Façaumacontadee-mailparaisso,ousevocêestiverdesenvolvendo
algonaempresaondetrabalha,vejacomoseuadministradorderedes
eservidorescomodeveseraautenticaç ãoparamandare-mails(ouse
realmenteprecisaautenticar).
159

## Página 176

11.8. Resumo CasadoCódigo
11.8 Resumo
Estecapítulocome çoucomumaideiasimples:mandare-mailscomlembretesdas
tarefas. Vimoscomoinstalareusarumabibliotecacomorientaç ãoaobjetospara
enviodee-mails,trabalhamoscomconstantesecomafun ção define()paracen-
tralizaraconfiguraç ãodaaplicaç ão. Alémdisso,usamososcontrolesdesaídado
PHPcomasfun ções ob_start(), ob_get_contents()e ob_end_clean()
paraconseguirfazerainclusãodeumtemplatecomoresultadoemumavariável.
11.9 Desafios
Éclaroqueestecapítulotambémtemalgunsdesafios.
• Terquatropontosdeentradadificultouumpoucoaadiçãodoarquivodecon-
figuração.Façaumacópiadoprojetoatéaquiepenseemumaformademanter
apenasumpontodeentradaqueconsigatratartodososcasos.
• Oarquivodeconfiguraçãotemapenasoe-maildedestino. Adicionecons-
tantesparaconfigurarodoremetente,ousuárioeasenhaparaautenticar,eo
nomequeapareceno“from”.
• Nalistadecontatos,adicioneaopçãodemandarosdadosdeumcontatopara
umendere çodee-mail.
• Aindanalistadecontato,adicioneafotodocontatocomoanexodoe-mail.
• Maisumparaalistadecontatos:centralizeasconfiguraçõesusandoconstan-
tesemumarquivoseparado.
• Nosistemadoestacionamento,adicioneaopçãodemandarosdadosdeuma
estadiaparaume-mail,mandandotambémasfotosdoveículo.
Emtodososdesafios,procureusaratécnicadelerotemplatedoe-mailusando
asfun ções ob_start()etc.
160

## Página 177

Capítulo12
HospedagemdeaplicaçõesPHP
Desenvolveraplicaçõeswebpodeserbastantedivertidoeútil,poispodemosdesen-
volverferramentasquesolucionamproblemasquetemosemnossodiaadia,como
foiocasodonossosistemadetarefasdesenvolvidoduranteoscapítulosdestelivro.
Oproblemaéqueatéestemomentoficamospresosanossoscomputadores,poisnos-
sasaplicaçõesfuncionamapenasneles.Quandoacessamosumsite,umblogouou-
traaplicaçãoweb,estamosacessandoalgoquefoidesenvolvidoassimcomoanossa
aplicação,masqueestálocalizadoemumservidornainternet.Quandocolocamos
nossaaplicaçãoemumservidornainternet,chamamosissode hospedagem.
Quandonossaaplicaç ãoestáemhospedadaemumservidor,elapodeseraces-
sadaapartirdequalquercomputadortambémconectadoàinternet,ouatémesmo
detabletsesmartphones!
12.1 Sua aplicação para o mundo!
Bem,naverdadeaindanãoéparaomundo,éapenasparavocê,masvocêpoderá
acessarestandoemqualquerlugar,bastandoestarconectadoàinternet.Digoqueé

## Página 178

12.2. Escolhendoumservidorparahospedagem CasadoCódigo
apenasparavocêpoisnossalistadetarefasnãotemseparaç ãoporusuários,então
serveparaapenasumusuário.
Paracolocarmosnossaaplicaç ãoonlineprecisamosencontrarumservidorpara
hospedagemquesuportenossasnecessidades.Depoisteremosqueconfigurarcomo
seráofuncionamentodaaplicaç ãonoservidoreentãopoderemosenviarnossos
arquivosparalá.
12.2 Escolhendo um servidor para hospedagem
Parapublicarumaaplicaç ãonawebprecisamosutilizarumservidorquetenhasu-
porteàstecnologiasqueestamosusando.NonossocasoéoPHPeoMySQL.Existem
diversasop çõesparahospedaraplicaçõesPHPeMySQL,desdeempresasqueofe-
recemoserviçogratuitamente(maspodemadicionaralgumtipodepropaganda),
atéopçõesparaquemquergerenciaroservidor,instalarasferramentasnecessárias
emantertudofuncionando.
Nonossocaso,precisamosdostiposmaisbásicos,poisestamosusandoapenas
paraaprendizadoenãoteremosumgrandevolumedeacesso. Mastambéméin-
teressanteconhecermosumaop çãomaisavan çada,porissovoudemonstrardois
serviçosdehospedagem,ummaissimplesegrátiseoutrocommaisrecursosque
ofereceumperíodográtisparaexperimentar.
OsserviçosdehospedagemdemonstradosserãoahospedagemdaHostingere
oJelasticdaLocaweb:
• Hostingerhttp://www.hostinger.com.br/
• JelasticdaLocawebhttp://www.locaweb.com.br/produtos/jelastic-cloud.html
12.3 Hospedagem com a Hostinger
AhospedagemcomaHostingersegueumpadrãodeacessovia FTPeusodeum
paineldeconfiguraçãobastanteusadoemdiversosservidoresqueéo CPanel.
OacessoviaFTPébastanteutilizadopoiselecriaumaconexãoqueexibeosar-
quivosremotoseseusarquivoslocaisdeumamaneiraqueficasimplesparacopiarde
umparaooutro.FTPsignifica File Transfer Protocol,ouProtocoloparaTransmissão
deArquivos.
OCPaneléumaferramentaparaadministraç ãodeservidoresvianavegador.
Estaferramentapossuidiversasop çõesdeconfiguraç ãoeébastantesimplesdeuti-
lizar,porissoéumaop çãocomumnúmerobemgrandedeusuários.
162

## Página 179

CasadoCódigo Capítulo12. HospedagemdeaplicaçõesPHP
12.4 Criação da conta na Hostinger
Paracriaracontaparahospedagemdeumaaplicaç ãonaHostingeracesseoendere ço
http://www.hostinger.com.br/evocêveráumatelaparecidacomesta:
Figura12.1:SitedaHostinger
Umformuláriodecadastroseráapresentado. Preenchaosdadosecliqueno
botão Criar conta:
163

## Página 180

12.4. CriaçãodacontanaHostinger CasadoCódigo
Figura12.2:CadastronaHostinger
Apróximatela,apósocadastro,pedeparaquevocêverifiqueoseue-maile
cliquenolinkdeativaç ão:
164

## Página 181

CasadoCódigo Capítulo12. HospedagemdeaplicaçõesPHP
Figura12.3:Pedidodeconfirmaç ãodocadastropore-mail
Apósclicarnolinkquechegoupore-mail,vocêserádirecionadoparaumapá-
ginaparaselecionarumplanodehospedagem.Aop ção Gratuitovaiservirbem
paratesteseatéparapequenossites:
165

## Página 182

12.4. CriaçãodacontanaHostinger CasadoCódigo
Figura12.4:Escolhaaop çãoGratuitoparaostestes
Napróximapágina,vocêdevecriarumanovaconta.Euescolhiumsubdomínio
gratuitoeaconselhoestaop çãoparaostestes:
Figura12.5:Escolhaumsubdomínioouumdomínio
166

## Página 183

CasadoCódigo Capítulo12. HospedagemdeaplicaçõesPHP
Elepodedemorarumpoucoparaativaracontaeespalharonovoendere çopela
internet(propagaroDNS).Entãovocêveráestapáginaquandoterminarocadastro
daconta:
Figura12.6:Aguardandoapropagaç ãodoDNS
Euaguardeiuns5minutoseatualizeiapágina,eacontajáestavaativa:
Figura12.7:Comoéumsubdomínio,ativoubemrápido
Estávendoobotão Painel de Controlenatelaanterior? Vamosprecisar
delelogomais.
Efinalmenteteremosacontacriadaeatéoendere çojáfuncionando! Aquieu
crieiumsubdomínionoendere ço tarefasphp.zz.mu.Aoacessá-lotemosapá-
ginapadrãodaHostinger:
167

## Página 184

12.4. CriaçãodacontanaHostinger CasadoCódigo
Figura12.8:PáginapadrãodaHostinger
Voltandonapáginadascontas,cliquenobotão Painel de Controle. Ele
exibirádiversosblocoscomáreasdiferentesdaadministraç ão.Navegueatéobloco
intitulado Avançadoecliquenaop ção Bases de Dados MySQL:
Figura12.9:Useaop çãoBasesdeDadosMySQL
168

## Página 185

CasadoCódigo Capítulo12. HospedagemdeaplicaçõesPHP
Nesta página será exibido um bloco chamadoCriar Novo Banco de
Dados e Usuário MySQL.Elejácolocaumprefixoparaonomedobancodeda-
dosedousuário,entãocoloqueonomedobancoeousuário,depoisasenhapara
acessoeconfirme:
Figura12.10:CriandoumnovobancoeumusuárioMySQL
Apáginaseráatualizadaeumblococomosdadosdeacessoseráexibido:
Figura12.11:OsdadosdeacessoaoMySQL
Guardeessesdados,poisaaplicaç ãovaiprecisardeles.
Agoradevemosvoltaraopainel Avançadoeusaraop ção PHPMyAdmin,que
éomesmoPHPMyAdminqueusamosemnossoambientelocal. Elevaipediro
usuárioesenha,entãocoloqueousuárioquevocêacaboudecriareteráacessoao
PHPMyAdmin.Agorasigaospassosparacriaç ãodastabelasdoscapítulos 6e10.
Játemososervidorprontoparareceberaaplicaç ão,entãoprecisamosdeixara
aplicaçãoprontaparaoservidor.
169

## Página 186

12.5. ConfigurandoaaplicaçãoparaaHostinger CasadoCódigo
12.5 Configurando a aplicação para a Hostinger
Agoraprecisamosalteraraaplicaç ãoparaquefuncionenoservidor. Naverdade
nãoétantotrabalho,éapenasaconfiguraç ãodeacessoaobancodedados.Altereo
arquivo config.phpecoloqueosdadosdeacesso:
<?php
define("BD_SERVIDOR", "mysql.hostinger.com.br");
define("BD_USUARIO", "seu_usuario");
define("BD_SENHA", "sua_senha");
define("BD_BANCO", "seu_banco_taref");
Nãoesque çadeconferirosdadosdeacesso!
Agorapodemos,finalmente,enviaraaplicaç ãoparaoservidorusandooFTP.
12.6 Enviando a aplicação para a Hostinger
ParaenviarosarquivosusandoFTPvocêvaiprecisardeumsoftwareclienteFTP.
Existemdiversasop ções,maseurecomendooFileZilla,quepodeserobtidoem
https://filezilla-project.org/:
170

## Página 187

CasadoCódigo Capítulo12. HospedagemdeaplicaçõesPHP
Figura12.12:SitedoFileZilla
Useaop ção Download FileZilla Clientenapáginadedownloadescolha
aop çãoparaoseusistemaoperacional.Sigaospassosdainstalaç ãousandoasop ções
padrão.
FileZilla noLinux
Procurenogerenciadordepacotesdasuadistribuiç ãopeloFileZilla.
UsuáriosdeDebian/Ubuntupodeminstalarusandooapt:
sudo apt-get install filezilla
AntesdeabriroFileZillaprecisamosdosdadosdeacessoFTP.Paraconsegui-
los,váaoCPaneldaHostingereprocurepelobloco Arquivose,nele,cliquena
opção Acesso FTP:
171

## Página 188

12.6. EnviandoaaplicaçãoparaaHostinger CasadoCódigo
Figura12.13:Useaop çãoAcessoFTP
VocêveráapáginadeacessoFTP:
Figura12.14:DadosdeacessoviaFTP
Énecessáriousaraop ção Mudar senha de contaparaescolherumasenha
deacesso.
AgoraabraoFileZillaecoloqueosdadosdeacessoFTPexibidospeloCPanelda
Hostinger:
172

## Página 189

CasadoCódigo Capítulo12. HospedagemdeaplicaçõesPHP
Figura12.15:PreenchendoosdadosdeacessoFTPnoFileZilla
Apóspreencherosdadoscliqueem Conexão rápida. OFileZillatemdois
paineis,umàesquerdacomosseusarquivoslocaiseumàdireitacomosarquivos
noservidor.NocasodaHostingerseráexibidoumúnicoarquivo default.php.
Agorapodemosnavegaratéapastaondeestãonossosarquivoslocais,eentãobasta
clicarearrastá-losparaopainelcomosarquivosdoservidor.OFileZillairáiniciar
atransmissão,equandoterminarosarquivosserãoexibidosnoservidortambém.
Apósfinalizaratransmissãodosarquivospodemosacessarosistemadetarefas
jáhospedado.Omeuficouhospedadoem http://tarefasphp.zz.mu/tarefas.php.
12.7 Hospedagem no Jelastic daLocaweb
OJelasticéumserviçobeminteressantedaLocawebpoisnospermiteconfigurar
aplicaçõesemcaminhosdiferentes,terbancosdedadosseparadosepacotescomas
diferentesversõesdaaplicaç ão,hospedagemdeoutrastecnologiasalémdoPHPe
MySQL,configuraçãodoPHPedoMySQLetc.
OJelasticéumpoucomaiscomplexodoqueaHostinger,maséumaop ção
interessanteparaquemdesejatermaiscontrolesobreasop çõesdoservidor.
12.8 Criação da conta no Jelastic daLocaweb
Paracriarumacontaehospedarumaaplicaç ãonoJelasticacesseoendere çohttp:
//www.locaweb.com.br/produtos/jelastic-cloud.htmlevocêveráumapáginacomo
esta:
173

## Página 190

12.8. CriaçãodacontanoJelasticdaLocaweb CasadoCódigo
Figura12.16:SitedoJelasticdaLocaweb
Preenchaoseue-mailecliqueem quero experimentar.Apósoprocessa-
mento,vocêveráamensagemdesucessonacriaç ãodaconta:
Figura12.17:Sucessonacriaç ãodaconta
Verifiquesuacaixadeentradaevocêdeveráterrecebidoume-mailcomoen-
dereçoeosdadosdeacessoparaconfiguraç ãodoambientedehospedagem:
174

## Página 191

CasadoCódigo Capítulo12. HospedagemdeaplicaçõesPHP
Figura12.18:E-maildeboasvindasdoJelastic
Cliquenolinkdoe-mailouacesseoendere çohttps://app.jelasticlw.com.br/e
informeologinesenhaquerecebeunoe-mail:
175

## Página 192

12.8. CriaçãodacontanoJelasticdaLocaweb CasadoCódigo
Figura12.19:TeladelogindoJelastic
Nestatela,vocêserárecebidopeloassistentedoJelastic:
Figura12.20:OassistentedoJelastic
Paraaprimeirautilizaç ão,eurecomendoseguirasinstruçõesdoassistente:basta
clicarem Vamos começareentãoclicarnaop ção Criar ambientequeficaem
cima,àesquerda:
176

## Página 193

CasadoCódigo Capítulo12. HospedagemdeaplicaçõesPHP
Figura12.21:Op çãoparacriarumnovoambiente
Nestapróximatelatemosaop çãodehospedarumaaplicaç ãoJavaouPHP:
Figura12.22:Sele çãodastecnologiaspararodaraaplicaç ão
Selecione PHPnaabasuperior, ApacheparaoservidorHTTPe MySQLparao
bancodedados.Aproveiteescolheroendere çodaaplicaç ãoecliqueem Criar.
Agoraésóaguardarenquantoaaplicaç ãoécriada:
Figura12.23:Aguardeacriaç ãodoambiente
177

## Página 194

12.8. CriaçãodacontanoJelasticdaLocaweb CasadoCódigo
Eassimqueterminar,oassistenteinformaqueoambientefoicriado:
Figura12.24:Sucessonacriaç ãodoambienteparahospedagem
Verifiquemaisumavezasuacaixadeentradaevocêdeveráverume-mailcom
osdadosdeacessoaoambiente:
Figura12.25:Endere çodeacessoàaplicaç ãohospedada
Vocêtambémdeveráterrecebidoume-mailcomaindicaçãodequeoambiente
doMySQLfoicriadoeseusdadosdeacesso:
178

## Página 195

CasadoCódigo Capítulo12. HospedagemdeaplicaçõesPHP
Figura12.26:DadosdeacessoaoMySQL
Agora é necessário acessar o endereço do banco de dados. Lá tem um
PHPMyAdmin.InformeseususuárioesenhaeuseoPHPMyAdminparacriarum
novobancochamado tarefasecrieastabelascriadasnoscapítulos 6e10aquido
livro.
12.9 Configurando a aplicação para o Jelastic
Apósacriaç ãodastabelas,editeoarquivo config.phpdaaplicaçãoecoloqueos
dadosdeacessoaoMySQLdoJelastic:
<?php
define("BD_SERVIDOR", "seu-mysql.jelasticlw.com.br");
define("BD_USUARIO", "seu_usuario");
define("BD_SENHA", "sua_senha");
define("BD_BANCO", "tarefas");
Feitoisso,crieumpacote zipdasuaaplicação.Issopodeserfeitoclicandocom
obotãodireitonapasta tarefaseusandoaop çãodecriarumarquivo zip.Este
passoéimportantepoisnoJelasticestaéamaneirapadrãodeenviaraaplicaç ão.
179

## Página 196

12.10. EnviandoaaplicaçãoparaoJelastic CasadoCódigo
12.10 Enviando a aplicação para o Jelastic
Apósfazeropacote zipvolteaopaineldoJelasticecliquenaop çãoUploadque
estánaabaGerenciadordeInstalação:
Figura12.27:Op çãodeUploaddaaplicaç ão
Napróximajanelaselecioneopacote zipquevocêcriouedêumadescriç ão
paraestaversãodopacote:
Figura12.28:Selecioneozipedêumadescriç ãoparaopacote
Umbomnomeajudaaidentificaropacotequandovocêtivermaisdeumaversão
cadastrada.
Opróximopassoéusaraop çãodeenviaropacoteparaproduç ãousandooícone
queestánalistacomosnomesdospacotes:
180

## Página 197

CasadoCódigo Capítulo12. HospedagemdeaplicaçõesPHP
Figura12.29:Selecioneoambienteparaenviaraaplicaç ão
Vocêseráquestionadosobreondefazerainstalaçãodopacote.Deixaembranco
parainstalarnaraizdoendere çoecliqueem instalar:
Figura12.30:Deixeembrancoparainstalarnaraizdoendere ço
Agoraaguardeenquantoaaplicaç ãoéimplantada:
Figura12.31:Aguardeaimplantaç ão
Apósaconclusãovocêpodeclicarnoíconeparairparaoendere çodaaplicação:
181

## Página 198

12.11. Resumo CasadoCódigo
Figura12.32:Aplicaçãoinstalada,bastaacessar!
Nomeucasoaaplicaç ãoficouem http://tarefasphp.jelasticlw.com.br/tarefas.
php.Aoacessarasua,nãoseesque çadecolocaronomedoarquivo tarefas.php
noendere ço.
Eéisso,suaaplicaç ãoestaráinstaladanoJelastic.
12.11 Resumo
Nestecapítuloforamapresentadasduasmaneirasdehospedagemdeaplica çõesPHP:
umausandooFTPeCPaneldaHostinger,quetambémsãousadospordiversosou-
trosservidores,eoutrausandooJelasticdaLocawebquetemop çõesbeminteres-
santesparaconfiguraçãodoservidor.
12.12 Desafios
Achouquenãoteríamosdesafiosnestecapítulo?Aquiestãoeles!
• Façaahospedagemdaaplicaç ãodoscontatosnaHostinger.
• Façaahospedagemdaaplicaç ãodoestacionamentonoJelastic.
• ProcuremaisumaopçãodehospedagemPHPeMySQLefaç aahospedagem
dosistemadetarefas.
182

## Página 199

Capítulo13
Programandocomorientaçãoa
objetos
Nocapítulodeenviodee-mailsusamosabibliotecaPHPMaileratravésdacriaç ão
deum objetonavariável$email.Esteobjetoeracompostopordiversasvariáveis
efun ções,tudoembutidoemapenasumavariável,quasecomoumarray,coma
diferençadequeumarraynãotemfun ções,apenasíndicescomvalores.
Estaéumaformabeminteressantedesedesenvolveraplicações,poispodemos
pensarnãoapenasnofluxodaaplicaç ão,mastambémnaslógicasdecadapartese-
paradamente.AbibliotecaPHPMaileréinteressanteporqueelanãotemaslógicas
necessáriasparaonossogerenciamentodetarefas,tudooqueelafazéoenviode
e-mails,esepreocupaapenascomisso.
Umexemplointeressantedoquepodevirarcódigoorientadoaobjetoséonosso
registrodetarefas,jáquetodasasregraselógicasparamanipularocadastrodeta-
refasestãoespalhadaspelaaplica çãoemdiversasfun çõesecondicionais,enquanto
poderiamestarreunidasemumaespéciede pacotequeseriaoresponsávelpelas

## Página 200

13.1. AclasseTarefas CasadoCódigo
regrasrelacionadasàstarefas.
Estepacoterecebeonomede classeeumaclassepodegerarostais objetos.
OlhandonovamenteparaousodabibliotecaPHPMailer,vejacomofoicriadoo
objeto $email:
<?php
...
$email = new PHPMailer();
...
Nestecaso PHPMaileréaclasseeusamosooperador newparacriarumnovo
objetodessaclasse.
Podemosfazeromesmocriando,porexemplo,umaclasse Tarefasquecon-
teriatodasaslógicasresponsáveisportrabalharcomobanco,salvaranexoseaté
mesmousara PHPMailerparaenviare-mails.
13.1 AclasseTarefas
Vamosentãoàcriaç ãodanossaclasse Tarefas.Aideiaéqueestaclassecontenha
todaalógicadastarefas,portantoelavainosajudarafazerumalimpezanoarquivo
banco.phpetambémnoarquivo ajudantes.php,poistudovaiestardentrodela.
Vamoscomeçarpelapartemaissimples,queéiraobancobuscarastarefasjáca-
dastradas.Paraisso,vamoscriarumdiretóriochamado classesedentrodeleum
arquivochamado Tarefas.php(issomesmo,comainicialemcaixaalta).Dentro
dessearquivo,coloqueoesbo çodaclasse Tarefas:
<?php
// Arquivo: classes/Tarefas.php
class Tarefas
{
public $conexao;
public $tarefas = array();
public function __construct($nova_conexao)
{
184

## Página 201

CasadoCódigo Capítulo13. Programandocomorientaçãoaobjetos
$this->conexao = $nova_conexao;
}
}
Analisandoocódigoparaaclasse Tarefaspodemosperceberalgunsitensinte-
ressantes,comoasvariáveis $conexaoe $tarefas.Aliás,apartirdeagoravamos
usaronome atributosparaessasvariáveisquesãomembrosdeumaclasse.
Umatributoéumvalorquedefinealgoemumaclasse.Paraficarmaisfácilde
entender,imaginequeseestivéssemoscriandoumaclasse Gatoteríamososatribu-
tospeso,cordopelo,tamanhodasgarrasetc. Atributossãoasqualidadesdeuma
classe.
LánaclassePHPMailertambémvimosalgunsatributoscomoHost,PorteUser-
name.
Outroitemquechamaaaten çãoéafun ção _ _construct().Estaéumafun-
çãoqueéexecutadasemprequeumnovoobjetoécriadousandoooperador new.
Nestecaso _ _construct()recebecomoparâmetroumaconexãodoMySQLe
guardanoatributo $conexaodanossaclasse. Aliás,paraacessaraqueleatributo
$conexaodaclasse,usamoso $thisqueéumnomeparaacessarosobjetoscria-
dosapartirdestaclasse.
Ejáquejádemosonomede atributoàsvariáveisdeumaclasse,vamostambém
usaronomecorretodasfun çõesdeumaclasse,queé método.
Voltandoàclasse Gatoosmétodosseriamalgocomo andar(), miar()e
dormir().
13.2 Buscando tarefas dentro da classe
Agora vamos transformar a função buscar_tarefas() que está no arquivo
banco.phpemum métododaclasseTarefas. Paraissopodemosrecortarafun-
çãodoarquivo banco.phpecolarlogodepoisdométodo _ _construct()da
classeTarefa:
<?php
...
public function __construct()
{
...
}
185

## Página 202

13.2. Buscandotarefasdentrodaclasse CasadoCódigo
public function buscar_tarefas()
{
$sqlBusca = 'SELECT * FROM tarefas';
$resultado = mysqli_query($this->conexao, $sqlBusca);
$this->tarefas = array();
while ($tarefa = mysqli_fetch_assoc($resultado)) {
$this->tarefas[] = $tarefa;
}
}
Pequenasalteraçõesforamfeitasnométodo buscar_tarefas().Vejaqueele
nãorecebemaisaconexãoMySQL,poisestaconexãojáéinformadanahoradecriar
umnovoobjeto.Avariável $tarefasvirouoatributo $this->tarefasenãoé
maisretornadanofinal,poisjáficadentrodoatributo $this->tarefas.
Comojátemosumafun çãotransportadaparaaclasse,vamosalteraraaplicaç ão
paraqueuseaclasseemvezdaantigafun ção.Noarquivo tarefas.phpadicione
um includeparaoarquivodaclasse,nãodeixandodecolocarocaminhodele
dentrodapasta classes:
<?php
include "config.php";
include "banco.php";
include "ajudantes.php";
include "classes/Tarefas.php";
...
Logoabaixodo includejápodemoscriarumobjeto $tarefasusandoa
classe Tarefas:
<?php
...
$tarefas = new Tarefas($conexao);
Perceba que estamos passando a variável$conexaona criação do objeto.
Quandocriamosumobjetonovo,oPHProdaométodo _ _construct()que
186

## Página 203

CasadoCódigo Capítulo13. Programandocomorientaçãoaobjetos
nestecasorecebeaconexãoeacolocanoatributo $this->conexao.Porissonão
precisamosmaisficarpassandoaconexãoparaométodo buscar_tarefas(),já
queeleusaoatributodoobjeto.
Agora, no final do arquivotarefas.php faça a chamada do método
buscar_tarefas().Issovaipreencheroatributo tarefasdaclassecomasta-
refasqueestãonobanco:
<?php
...
$tarefas->buscar_tarefas();
include "template.php";
Enoarquivo tabela.php,ondeéexibidaalistadetarefas,altereousoda
variável$lista_tarefaspeloatributo $tarefasdoobjeto $tarefas:
...
</tr>
<?php foreach ($tarefas->tarefas as $tarefa) : ?>
<tr>
...
Agorajápodemosacessaraaplicaç ãonovamenteetudodeveráestarfuncional.
Visualmente,nadamudou,masagoratemosumaclasseparacentralizarasregras
paraastarefas.
13.3 Buscando apenas uma tarefa dentro da classe
Vamosmoverafun ção buscar_tarefa()paraummétododaclasse Tarefas.
Para isso, recorte essa função do arquivobanco.phpe cole dentro da classe
Tarefas,logoabaixodométodo buscar_tarefas():
<?php
class Tarefas
{
...
187

## Página 204

13.3. Buscandoapenasumatarefadentrodaclasse CasadoCódigo
public function buscar_tarefas()
{
...
}
function buscar_tarefa($id)
{
$sqlBusca = 'SELECT * FROM tarefas WHERE id = ' . $id;
$resultado = mysqli_query($this->conexao, $sqlBusca);
$this->tarefa = mysqli_fetch_assoc($resultado);
}
}
Vejaqueasmudan çasparaestemétodotambémsãopequenas,poisestamos
usandoaconexãoqueestánoatributo $this->conexaoeoresultadoestásendo
guardadonoatributo $this->tarefa.Aliás,oatributo $this->tarefaainda
nãoexiste,entãovamosadicioná-lologoapósoatributo $this->tarefas:
<?php
class Tarefas
{
public $tarefas = array();
public $tarefa;
public $conexao;
...
}
Agorapodemosalteraroarquivo editar.phpparausaraclasse Tarefa
e o método buscar_tarefa(). Para isso devemos incluir o arquivo
classes/Tarefas.phpecriaroobjeto $tarefaslogonoiníciodoarquivo
editar.php:
<?php
include "config.php";
include "banco.php";
include "ajudantes.php";
include "classes/Tarefas.php";
188

## Página 205

CasadoCódigo Capítulo13. Programandocomorientaçãoaobjetos
$tarefas = new Tarefas($conexao);
...
Enofinaldoarquivotrocamosousodafun ção buscar_tarefa()pelomé-
todocomomesmonome:
<?php
...
$tarefas->buscar_tarefa($_GET['id']);
$tarefa = $tarefas->tarefa;
$tarefa['nome'] = (isset($_POST['nome'])) ?
$_POST['nome'] : $tarefa['nome'];
...
Comisso,aaplicaç ãojávoltaafuncionarcommaisumafun çãotransformada
emmétododaclasse Tarefas.
13.4 Grav ando e editando tarefas dentro da classe
Vamosmovertambémagravaç ãodenovastarefaseaediç ãodetarefasparaden-
trodaclasseTarefas. Aquifaremosbasicamenteosmesmospassosjáfeitospara
mover a busca de tarefas para dentro da classe. Comece movendo as funções
gravar_tarefa()e editar_tarefa()paramétodosdaclasse,depoisremova
oparâmetro $conexaoe,porúltimo,troqueousodavariável $conexaopelo
atributo $this->conexao.Ométodo gravar_tarefa()ficaassim:
<?php
// Arquivo classes/Tarefas.php
...
class Tarefas
{
...
public function gravar_tarefa($tarefa)
{
$sqlGravar = "
INSERT INTO tarefas
189

## Página 206

13.4. Gravandoeeditandotarefasdentrodaclasse CasadoCódigo
(nome, descricao, prioridade, prazo, concluida)
VALUES
(
'{$tarefa['nome']}',
'{$tarefa['descricao']}',
{$tarefa['prioridade']},
'{$tarefa['prazo']}',
{$tarefa['concluida']}
)
";
mysqli_query($this->conexao, $sqlGravar);
}
...
Eométodo editar_tarefa()ficaassim:
<?php
// Arquivo classes/Tarefas.php
...
class Tarefas
{
...
public function editar_tarefa($tarefa)
{
$sqlEditar = "
UPDATE tarefas SET
nome = '{$tarefa['nome']}',
descricao = '{$tarefa['descricao']}',
prioridade = {$tarefa['prioridade']},
prazo = '{$tarefa['prazo']}',
concluida = {$tarefa['concluida']}
WHERE id = {$tarefa[ 'id']}
";
mysqli_query($this->conexao, $sqlEditar);
}
...
190

## Página 207

CasadoCódigo Capítulo13. Programandocomorientaçãoaobjetos
Depois, basta alterar o uso das fun ções gravar_tarefa() e
editar_tarefa()pelosmétodosdemesmonome.Noarquivo tarefas.php:
<?php
...
if (! $tem_erros) {
$tarefas->gravar_tarefa($tarefa);
if (isset($_POST['lembrete']) && $_POST['lembrete'] == '1') {
...
Enoarquivo editar.php:
<?php
...
if (! $tem_erros) {
$tarefas->editar_tarefa($tarefa);
if (isset($_POST['lembrete']) && $_POST['lembrete'] == '1') {
...
Com isso, temos mais duas funções transformadas em métodos. Perceba
que o arquivo banco.php está esvaziando e agora tem apenas a conexao
comoMySQLemaistrêsfun ções( buscar_anexos(), gravar_anexo()e
remover_tarefa()). Dessaforma,estamosmovendotodaalógicarelacionada
àstarefasparaaclasse Tarefaseissoémuitobom,porqueficafácildeencontrar
asregrasemaisorganizado.
13.5 Usando o MySQLi orientado a objetos
Atéagorausamosdiversasfun ções mysqli_eumacoisaqueincomodaumpouco
éterqueficarpassandoavariávelcomaconexãoparacadafun çãoqueprecisamos
usar.Seriabemmaisinteressanteseaprópriaconexãotivessemaneirasderealizar
oscomandosSQL,certo?
Porissoo MySQLipossuiumaformaorientadaaobjetosdetrabalharqueébem
interessanteenãoédifícildeaplicarnanossaaplicaç ão.
191

## Página 208

13.5. UsandooMySQLiorientadoaobjetos CasadoCódigo
Lembradafun ção mysqli_connect()usadanoarquivo banco.php? Ela
retornaaconexãoqueusamosemtodasasoutrasfun ções mysqli_atéagora.Esta
linhapodesersubstituídapelacriaç ãodeumobjetodaclasse mysqlieesteobjeto
possuiosmétodosnecessáriosparatrabalharmoscomobancodedados.
Paracriaroobjeto,precisamosdooperador newevamosusaraclasse mysqli.
Então,noarquivo banco.phptroquealinhaquecriaavariável $conexaopela
criaçãodoobjeto $mysqli:
<?php
$mysqli = new mysqli(BD_SERVIDOR, BD_USUARIO, BD_SENHA, BD_BANCO);
if ($mysql->connect_errno) {
echo "Problemas para conectar no banco. Verifique os dados!";
die();
}
...
Percebaqueaverificaç ãodoerrodeconexãojáéfeitausandoumatributodo
objeto $mysqlienãomaisafun ção mysqli_connect_errno().
Agora,altereoslocaisquecriamumobjetodaclasse Tarefasparareceberem
oobjeto $mysqli. Issoacontecenosarquivos tarefas.php, editar.phpe
tarefa.php.
Vejacomoficanoarquivo tarefas.php:
<?php
...
$tarefas = new Tarefas($mysqli);
...
Éclaroqueissovairefletirnosnossosmétodosdaclasse Tarefasqueusamas
funções mysqli_.Então,paraacertaraclasse Tarefasvamoscome çarmudando
oatributo $conexaopara mysqli:
<?php
class Tarefas
{
192

## Página 209

CasadoCódigo Capítulo13. Programandocomorientaçãoaobjetos
public $tarefas = array();
public $tarefa;
public $mysqli;
...
Alteretambémoconstrutordaclasse Tarefasparausaroobjeto $mysqli:
<?php
...
public function __construct($novo_mysqli)
{
$this->mysqli = $novo_mysqli;
}
...
E por fim, precisamos apenas trocar o uso da função mysqli_query()
pelo método query() do objeto $mysqli. Veja como fica o método
buscar_tarefa(),porexemplo:
<?php
...
function buscar_tarefa($id)
{
$sqlBusca = 'SELECT * FROM tarefas WHERE id = ' . $id;
$resultado = $this->mysqli->query($sqlBusca);
$this->tarefa = mysqli_fetch_assoc($resultado);
}
Agora o resultado é obtido usando$this->mysqli->query(), pois o
mysqliéumobjetoqueéumatributodaclasse Tarefas. Percebaquenãomu-
damosousodafun ção mysqli_fetch_assoc(),jáqueelacontinuarecebendo
umresultadodométodo $mysqli->query().
Altere os outros métodos da classe Tarefas para usar o método
this->mysqli->query()nolugardafun ção mysqli_query().
Antes de executar a aplicação também é necessário alterar as funções
remover_tarefa(), gravar_anexo()e buscar_anexos()queestãonoar-
quivo banco.phpequeaindanãotransformamosemmétodosdaclasse Tarefas.
193

## Página 210

13.5. UsandooMySQLiorientadoaobjetos CasadoCódigo
Nocaso,estasfun çõesaindarecebemcomoparâmetroaconexão,masagoravãore-
ceberoobjeto $mysqli.Vejacomoficaafun ção remover_tarefa():
<?php
function remover_tarefa($mysqli, $id)
{
$sqlRemover = "DELETE FROM tarefas WHERE id = {$id}";
$mysqli->query($sqlRemover);
}
Nestafun çãomudamosoparâmetropara $mysqlieremovemosafun ção
mysqli_query(),trocandoseuusopelométodo $mysqli->query().
Jáasfunções gravar_anexo()e buscar_anexos()ficamassim:
<?php
function gravar_anexo($mysqli, $anexo)
{
$sqlGravar = "INSERT INTO ... ";
$mysqli->query($sqlGravar);
}
function buscar_anexos($mysqli, $tarefa_id)
{
$sqlBusca = "SELECT * FROM anexos WHERE tarefa_id = {$tarefa_id}";
$resultado = $mysqli->query($sqlBusca);
...
}
Deixeiemdestaqueapenasaslinhasmaisimportantesequesofreramasmu-
dançasparausaroobjeto $mysqli. Orestantedasfun çõesfuncionadamesma
maneiraqueantes.
Estas funções são usadas nos arquivostarefas.php, editar.php e
remover.php. Então devemos alterar suas chamadas para passar o objeto
$mysqlinolugardavariável $conexao. Noarquivo remover.phpousoda
função remover_tarefa()ficaassim:
194

## Página 211

CasadoCódigo Capítulo13. Programandocomorientaçãoaobjetos
<?php
include "config.php";
include "banco.php";
remover_tarefa($mysqli, $_GET[ 'id']);
header('Location: tarefas.php');
Após alterar também as chamadas das funções gravar_anexo() e
buscar_anexos()aaplicaçãojápoderáserexecutadanormalmente.
OusodabibliotecaMySQLicomoumobjetoéinteressantepoisdeixaquasetudo
dentrodeumúnicoobjeto,emvezdeusarváriasfun ções,alémdenãosernecessário
ficarpassandoavariávelcomaconexãoparacadafun çãoqueéchamada.
13.6 Av ançando em orientação a objetos
Orientaçãoaobjetosémuitomaisdoqueopoucoquemostreinestelivro.Aideia
aquifoifazerapenasumaintroduç ãoparaincentivaroleitorapesquisarmaissobre
oassunto.
Trabalharcomorientaç ãoaobjetoscostumaseropesadelodemuitosinician-
tesemprogramaç ão,masdepoisqueseentendemosconceitosdeclasses,objetos
edecomunicaç ãoentreosobjetosepadrõesdedesenvolvimentocomoosfamosos
designpatterns,percebe-seaimportânciadesdetipodedesenvolvimentodecódigo.
Osmaisavan çadosemdesenvolvimentoorientadoaobjetospodemterencon-
tradodiversospontosdemelhorianocódigodaclasseTarefas,comoofatodeela
serumaespéciedeentidade,umrepositórioeumacole çãoaomesmotempo.Mas
nãofiquemimpacientes!Estafoiapenasumamaneirademostrarcomoaorientaç ão
aobjetospodeserútilnacentralizaç ãoeorganizaç ãodecódigo.Alistadee-mails
desdelivropodeedeveserusadaparaapresentarimplementaçõesdiferentesemais
avançadas.
13.7 MVCeFrameworks
Umconceitoimportantequeinfelizmentenãocoubenestelivroéo MVC,queéum
padrãoparadesenvolvimentodesoftwarequeseparaaaplicaç ãoembasicamentetrês
camadasdistintas,sendoquecadaumaéresponsávelporumafun ção.Nestelivro
195

## Página 212

13.7. MVCeFrameworks CasadoCódigo
nãousamosestritamenteoMVC,masosexemplosforamfeitosdeformaamanter
asresponsabilidadesseparadasemcadaarquivo. Vejaqueoarquivo banco.php
semprefoioresponsávelpeloacessoaobanco,atéaclasse Tarefasaparecer.Os
arquivos tarefas.php, editar.phpe remover.phpforamosresponsáveispor
receberasrequisiçõesdonavegadoreentãodecidiroquefazer. Etambémtemos
algunsarquivosquecontêmbastanteHTMLeservemparamontarostemplatesda
aplicação.
NoMVCexistemtrêscamadas: Model,VieweController.
AcamadaModeléaresponsávelpelasregrasdenegócioe,emgeral,peloacesso
aobancodedadosououtrasfontesdedados.Podemosmeioquefazerumaassoci-
açãodaModelcomnossoarquivo banco.phpoucomaclasse Tarefas.
Acamada Controlleréresponsávelporreceberasrequisiçõesedecidiroque
deveserfeitocomelas. Emgeral,o controllerusaas modelsparaobteregravar
dados,eenviainformaçõesparaqueas viewsexibamdadosparaquemsolicitou.
JáacamadaViewéresponsávelporinteragircomosusuáriosexibindoaspági-
nas(as viewstambémpodemconversarcomoutrossistemasatravésdelinguagens
comoXMLeJSON).
ExistemferramentasqueimplementamoMVCefacilitameuniformizamotra-
balhodosdesenvolvedores.Estasferramentassãoos frameworks.
Emgeralum frameworkjávemcomdiversasdiretrizesparadesenvolvimento,
comoondecolocarumcontroller,comofazerumaview,uniformiza çãodeacessoaos
diversosbancosdedados,ajudantesparaenviodee-mails,valida çãodeformulários,
camadasdeseguran çaetc.
Existemdiversos frameworksparaPHP,cadaumcomseufocoeseupúblico.
Ficaaquiumalistacomalguns frameworksPHP:
• CodeIgniter—leve,rápidoefácildeaprender.Bomparaaplicaçõesmenores.
• Laravel—umadasestrelasdomundoPHPatualmente. Usadoparaapro-
duçãodeprojetospequenosegrandes. Suabibliotecadebancodedadosé
bastanteelogiada.
• CakePHP—umdosmaisconhecidoseutilizadosdepequenasagrandesapli-
cações.
• ZendFramework—frameworkoficialdaZend,cheioderecursoseumdos
preferidosdasempresasparagrandesaplicações.
196

## Página 213

CasadoCódigo Capítulo13. Programandocomorientaçãoaobjetos
• Symfony—umdosmaisrobustos,bastanteusadoparagrandesaplicações.
Experimenteconhecerdoisoutrês frameworks.Tentefazeraaplicaç ãodasta-
refasemcadaumdelesevejacomoelestratamoacessoaobanco,comofazemo
uploaddearquivosetc.
Ésemprebomconheceralguns frameworksparapoderescolhernahoradecriar
umanovaaplicação,alémdeaprendercomosdetalhesdecadaum.
13.8 Resumo
Nestecapítulofoiapresentadaumapequenaintroduç ãoàprogramaç ãoorientadaa
objetos. Conseguimoscriarumaclasse Tarefasquepassouaservirdecentrali-
zadoraparaostrechosdecódigoresponsávelporlidarcomastarefasnobancode
dados.Tambémalteramosautilizaç ãodoMySQLiparasuaformaorientadaaobje-
tosecentralizamosoacessoaobanconoobjeto $mysqliemvezdeusardiversas
funções.
Orientaçãoaobjetoséumtópicobastanteextensoevaleapenaentendermais
profundamente,poisgrandepartedossoftwaresPHP(edeoutraslinguagens)autili-
zamparacriarsistemasgrandesoupequenosdeformamaisorganizadaefacilitando
amanuten ção.
Também foi feita uma pequena introdução a conceitos comoMVCefra-
meworks,quetambémsãotópicosquerendemboashorasdeestudoecalorosas
discussõesentredesenvolvedores.
13.9 Desafios
Agoramaisalgunsdesafios,dessavezparatreinarorientaç ãoaobjetos.
• Transforme as funções buscar_anexos(), gravar_anexo() e
remover_tarefa()emmétodosdaclasse Tarefas.
• Movaavalidaçãodosformuláriosdecriaçãoeediç ãodetarefasparadentroda
classe Tarefas.Esteémaiscomplexo,poisvocêdeveretornarasmensagens
deerro,casonecessário.
• CrieumaclasseContatosetransformeasfun çõesdemanipulaç ãodobanco
dedadosemmétodosdestaclassenoprojetodoscontatos.
197

## Página 214

13.9. Desafios CasadoCódigo
• NoprojetodoestacionamentocrieumaclasseVeiculosqueseráresponsá-
velpormanipularosdadosdosveículosnobancodedados.
• Escolhaumdosframeworkslistadosetenterecriaraaplicaç ãodastarefas
nele.Umadicaéfazeraaplicaç ãodeexemploqueemgeralexistenomanual
decasaframework.Quasesempreestaaplicaç ãodeexemploéumblog,oque
envolvediversosrecursos.
198

## Página 215

Capítulo14
Proteçãoeajustes
Esteéumcapítulobônusquenãopoderiaficardeforadestelivro.
Existemdiversasformasdeataquesasiteseaplicaçõeswebe,quandocolocamos
nossocódigoonline,corremosoriscodereceberalgumtipodeataqueparaquebrara
segurançadenossasaplicaçõeseroubarinformações—oumesmoparatransformar
nossasaplicaçõesemrobôsqueenviamspamououtrostiposdeameaç asvirtuais.
Umdostiposmaiscomunsdeataqueéa SQLInjection,comaqualoatacante
consegueburlaroacessoaobancodedadosdaaplicaç ãoe,emgeral,consegueapagar
todososdados.
Nossaaplicaçãodastarefasestávulnerávelaestetipodeataque,poisumusuário
poderiadigitarumpoucodeSQLemalgunsdecampos.Experimentecadastraruma
tarefachamada Assistir 'Star Wars'evocêveráqueelanãoserácadastrada.
IssoacontecepoismontamosocódigoSQLusandooapóstrofoparadelimitar
nossoscamposdetextoe,quandocolocamosmaisumapóstrofononomedatarefa,
ocódigoSQLégeradoincorretamente.Issoéruim,certo?

## Página 216

14.1. Protegendo-secontraSQLInjection CasadoCódigo
14.1 Protegendo-se contra SQLI njection
Paraprotegernossaaplicaç ãoprecisamosescaparoscaracteresquepodemserusa-
dosparacomporcódigoSQL,comoéocasodeaspaseapóstrofos.
Para escapar esses caracteres, devemos usar a fun ção
mysqli_real_escape_string() ou o método escape_string() da
classemysqli.
Vejacomoficaométodo gravar_tarefa()daclasse Tarefas,noarquivo
classes/Tarefas.php:
<?php
class Tarefas
{
...
public function gravar_tarefa($tarefa)
{
$nome = $this->mysqli->escape_string($tarefa['nome']);
$descricao = $this->mysqli->escape_string($tarefa['descricao']);
$prazo = $this->mysqli->escape_string($tarefa['prazo']);
$sqlGravar = "
INSERT INTO tarefas
(nome, descricao, prioridade, prazo, concluida)
VALUES
(
'{$nome}',
'{$descricao}',
{$tarefa['prioridade']},
'{$prazo}',
{$tarefa['concluida']}
)
";
$this->mysqli->query($sqlGravar);
}
...
Percebaqueosdadosquecontêmtextosforamcolocadosemvariáveisquesão
200

## Página 217

CasadoCódigo Capítulo14. Proteçãoeajustes
osretornosdométodo $mysql->escape_string().
Escaparumtextoéalgomaisoumenosassim:
Otextoeraisso Assistir 'Star Wars'evirouisso Assistir \'Star
Wars\'.Dessaforma,oMySQLtrataoapóstrofocomoumapóstrofomesmoenão
comoumdelimitadordecamposdetexto.
14.2 Exibindo campos com aspas
Agoraquejáestamosfazendooescapedenossoscamposdetextoparaobanco,um
novoproblemaaparece.Experimenteadicionarumatarefachamada Assistir“Star
Wars”evocêveráqueocadastroacontecenormalmente.
Agoratenteeditarestatarefaevocêveráqueocamponomeapareceapenascom
otextoAssistir.IssoestáacontecendopelofatodeoHTMLgeradoserassim:
<input type="text" name="nome" value="Assistir "Star Wars"" />
Vejaqueasaspasantesdapalavra Starestãofinalizandooatributo valueda
tag input,porissoorestantedotextonãoaparecedentrodocampo.
Pararesolveresteproblema,precisamostransformarasaspasemcaractereses-
peciaisdeaspasqueoHTMLentende. Issonãoéamesmacoisaqueoescapede
strings,massegueumaideiasemelhanteparanãodeixarquetemplatesHTMLque-
brem.
Arepresenta çãodeaspasparaHTMLéotexto &quot;eemPHPexisteuma
funçãoquetraduztodososcaracteresespeciaisdoHTMLemsuasrepresentações
HTML.Estafun çãoéa htmlspecialchars().Vejacomoficaparaexibirmoscor-
retamenteonomedastarefasnoformulárioqueestánoarquivo formulario.php:
<input type="text" name="nome" value="<?php
echo htmlspecialchars($tarefa['nome']);
?> " />
Apósestaalteraç ão,ocódigoHTMLdocamposerágeradoassim:
<input type="text" name="nome" value="Assistir &quot;Star Wars&quot;" />
Vejaqueasaspasforamalteradaspara $quot;.
201

## Página 218

14.3. Resumo CasadoCódigo
14.3 Resumo
Estefoiumcapítulopequenomasextremamenteimportante!Nele,foramexibidos
doisconceitosmuitoimportantesdodesenvolvimentoweb,sendoumdelesaprote-
çãocontra SQLInjection eooutro,otratamentodageraç ãodeHTMLparaevitar
quebrasdecamposetemplates.
AlémdoSQLInjection,existemoutrostiposdeataquescomo XSSeCSRFe
estestópicosmerecemumestudomaisaprofundado.
Umadicalegaléque,emgeral,os frameworkstratamdestestópicos,entãoeste
émaisummotivoparapesquisarmaissobreeles.
14.4 Desafios
Eaquiestãomaisalgunsdesafios!
• FaçaotratamentocontraSQLInjectionemtodaaaplicaç ãodastarefas.
• Façaotratamentodaexibiç ãodoscamposdetextodaaplicaç ãodastarefas.
• FaçaotratamentocontraSQLInjectioneotratamentodaexibiç ãodoscampos
detextodaaplicaç ãodoscontatosetambémdoestacionamento.
202

## Página 219

Capítulo15
Aoinfinito...Ealém!
Eaquichegamosaofimdesdelivro,masnãoaofimdosestudos!
Paraaprenderadirigirautomóveisénecessáriopraticarporváriashoras. O
mesmoéválidoparaquemqueraprenderatocaruminstrumentomusicaloupara
quemquerdominaralgumtipodearteoutecnologia.
Éclaroquecomprogramaç ãonãoédiferente.Parasetornarumbomprogra-
madorénecessáriopraticar.Equantomaissepratica,maisseaprende.
Inventenovosproblemaspararesolver,poisassimvocêsetornaoprimeirousuá-
riodesuasaplicações.Crieumorganizadordetarefas,umgestorparaasuacole ção
delivros,umaagendadigital,umclonedoTwitteretc. Oimportanteécontinuar
praticando.
15.1 Onde posso buscar mais informações?
Ainternetébemvastaeasvezesécomplicadoacharbonsconteúdos,porissodeixo
aquialgumassugestõesdeondebuscarajudaeprocurarinformações.

## Página 220

15.1. Ondepossobuscarmaisinformações? CasadoCódigo
ParasabermaissobreosrecursosdoPHPvisiteadocumentaç ãooficialemhttp:
//php.net/docs.php.Temtambémaversãoemportuguêsaquihttp://www.php.net/
manual/pt_BR/index.php.
Umsitequetemmuitainformaç ãoimportantesobreasmelhorespráticaspara
PHPéo http://www.phptherightway.com/. Existetambémumaversãoemportu-
guêsaquihttp://br.phptherightway.com/.
Participedalistadediscussãodolivro.Lávocêpodetirarsuasdúvidas,ajudar
quemestápassandoporproblemasdiferenteseaindaconhecerpessoasinteressadas
nomesmoassunto,oquepodeturbinarseuaprendizado.Alistaestánesteendere ço:
https://groups.google.com/forum/#!forum/phpemysqlcasadocodigo
UmaboaideiaéparticipartambémdecomunidadesmaiorescomooGUJ–
http://www.guj.com.br.Látempessoasconversandosobreváriaslinguagensetec-
nologiaseépossívelaprendermuitoparticipandodesdetipodegrupo.
FiquedeolhonositedaCasadoCódigo– http://www.casadocodigo.com.br–
parasaberdosúltimoslan çamentos.
Valelembrarquevocêpodebaixartodososexemplosusadosnolivro.Elesestão
noGitHubem https://github.com/InFog/phpmysql
Bonsestudosesucesso!
204