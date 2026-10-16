---json
{
  "id": "python_-_escreva_seus_primeiros_programas",
  "title": "Python - Escreva seus primeiros programas",
  "categoria": "03-linguagens",
  "subcategoria": "python",
  "resumo": "**Arquivo Original:** `Python - Escreva seus primeiros programas.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "escreva",
    "linguagens",
    "primeiros",
    "programas",
    "python",
    "seus"
  ],
  "perguntas_tipo": [
    "Como utilizar Python - Escreva seus primeiros programas?",
    "Quais as boas praticas de python?"
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
  "dono": "stack-python",
  "prioridade": 2
}
---

# Python - Escreva seus primeiros programas

> **Arquivo Original:** `Python - Escreva seus primeiros programas.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 1

62598


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
E-book gerado especialmente para 


## Página 3

E-book gerado especialmente para 


## Página 4

E-book gerado especialmente para 


## Página 5

CasadoCódigo
Prefácio
Pythonéumalinguagemdeprograma çãoquevemsendoempregadanacons-
truçãodesolu çõesparaosmaisdiversosfinseducacionais,comerciaisecien-
tíficos eplataformas web,desktope,maisrecentemente,móvel.Éumalin-
guagemdefácilaprendizado,expressiva,concisaemuitoprodutiva;porisso,
suaadoçãotemcrescidobastantenosúltimosanospelosmaisvariadosperfis
deprofissionaisnomeiocientíficoeacadêmico,tantoparadesenvolvimento
deferramentasquantoparaensinodealgoritmoseintrodu çãoàprograma-
ção.
Éumalinguagemdeusogratuitoedecódigo-fonteaberto,compatível
comosprincipaissistemasoperacionais,como:Linux,OSX,Windows,BSDs
etc.Elacontacomumavastabibliotecapadrãoedocumenta çãoquepossibi-
litamquemuitascoisassejamfeitassemdependênciasadicionais.
Apesardesersimplesdeaprender,Pythonéumalinguagembastante
poderosaeflexível. Essacombina çãoresultaemumricoecossistemaque
melhoraaprodutividadedosdesenvolvedores.Issotudotornaadecisãode
aprenderPythonimportantíssima,poismuitoshorizontesabrem-sequando
sedominaumalinguagemcomecossistematãopoderosoquantoodela.
Sevocêestálendoestelivro,possivelmenteseinteressouporPythonem
algummomento. Então,esperoqueelepossacontribuir,dealgumaforma,
comoseuaprendizado.Olivroapresentaalinguagemdeumaformacontex-
tualizadae,porisso,aolongodele,vamoscriarumaplicativoparaanalisar
dadospúblicosdoGovernoFederal.Aideiaéapresentarmotiva çõespráticas,
paradepoisdemonstrarosrecursosdalinguagemquenospermitemtratara
motivaçãoinicial.
Estelivroestádivididoemduaspartes.Aprimeirafocanosaspectosfun-
i
E-book gerado especialmente para 


## Página 6

CasadoCódigo
damentaisdePython,muitosdosquaisjásãoconhecidosporquemjátem
experiênciacomoutraslinguagensdeprograma ção.Jánasegunda,passare-
mosaolharcaracterísticasmaisespecíficasdalinguagemque,emborapossam
nãoserexclusivas,sãomarcantesedevemsertratadascommaiscuidado.
PorquePython3?
Oanode2014foiumanochavenaado çãodePython3,porgrandeparte
dacomunidade.Muitosprojetosrelevantesforamportadosoulan çaramver-
sõescompatíveisnesseano. Afamília3.4temmaioraceita çãoqueasante-
rioresdaversão3e,inclusive,foiadotadacomoversãopadrãoemalguns
sistemasoperacionais. Python3nuncachamoutantaaten çãocomoagora,
entãonadamaisjustoqueumlivrootenhacomoassuntobase.
Nossoobjetivoéapresentarosrecursosbásicosdalinguagem,ideiase
conceitoscentraisconstruindoumaplicativosimplesdeleituraemanipula-
çãodedados.
Olivroéconceitualepráticoaomesmotempo,paraqueoaprendizado
sejamaisprofundosemserchatoedifícildeentender.Livrosextremamente
práticospodem,muitasvezes,pularconceitoseideiascentraisdoassunto
abordado,aopontoquetextosapenasconceituaispodemficarcansativose
teóricosdemais.
Assim, opropósitoéfazercomquevocêentendamelhorouniverso
Python,aomesmotempoemqueaprendeausarnapráticaosprincipaisre-
cursosdalinguagem.
Público-alvo
Esteéumlivroparainiciantesemprograma çãooudesenvolvedoresavan-
çadoscompoucaexperiênciaemPython.Sevocêforuminiciante,leia-ocom
calmaparanãoacumulardúvidasaolongodoaprendizado. Emtermosde
complexidade,amaioriadosexemplosébemsimplesefocaempassarpara
oleitorcomousarosrecursosdisponíveisdamelhorforma.Emtermoscon-
ceituais,todasasexplica çõesbuscamsercompletasparanãoexigirconsulta
afontesexternas.
Casovocêjátenhaalgumaexperiênciaemprograma ção,masnãoco-
nheçaPython,olivrocontribuiparaquevocêrapidamentedescubracomo
ii
E-book gerado especialmente para 


## Página 7

CasadoCódigo
implementarnessalinguagemcoisasquesãocomunsemoutras.Alémdisso,
oscapítulosabordamaspectosbemespecíficos,comexplica çõesconceituais
eexemplospráticos.
AquiexplicocomoascoisasfuncionamnouniversoPythoneapresento
umpoucodavisão pythônicaparaoleitor.Atémesmoaspartesmaistriviais
podemconter insightsimportantessobreocomportamentodalinguagemou
decisõesdedesignadotadas.
Ospeda çosdecódigoapresentadosserãoautocontidosepermitirãoao
leitormodificareobterresultadosdiferentes.Todososcódigossãoexplica-
dos,muitasvezeslinhaalinha,paraquevocêentendaclaramenteoobjetivo
eafun çãodecadaparte.
Caso tenha alguma dúvida ou sugestão, procure a comuni-
dade do livro para tirar dúvidas. Ela está disponível em livro-
python3@googlegroups.com.Vocêserámuitobem-vindo!
Oscódigos-fontedosexemplosutilizadosaolongodolivropodem
serencontradosem: https://github.com/felipecruz/exemplos
Sobreoautor
FelipeCruzédesenvolvedordesoftwarehá10anos.Trabalhounomer-
cadocorporativoedestartupserecentementeatuacomoCientistadeDados,
áreaondereencontrousuapaixãopelaconstru çãodesoftware. Mestrando
emComputaçãopelaPUC-Rio,tambémestudaAprendizadodeMáquinase
atualmentebuscanovasformasderesolveroproblemadarecomenda çãoeo
aprendizadonãosupervisionadodeatributos.
Pythonistahá6anos,palestranteeparticipantedediversasPythonBrasil,
semprebuscoucompartilharconhecimentoeaprendercadavezmaissobrea
linguagemeoecossistemaaolongodessesanos.
iii
E-book gerado especialmente para 


## Página 8

CasadoCódigo
Agradecimentos
Agradeço, primeiramente, àminhafamíliapeloapoioepaciênciaao
longodotempodecria çãodolivro. Emespecial,paraminhasfilhasMaya
eLiz,minhaesposaFernanda,mãeeirmãsIlka,IlkaeIeda.
Tambémagradeçomuitopelaconfian çaepaciênciadaequipeCasado
Códigoaolongodestaárduajornada.Emdiversosmomentos,nãoconsegui
produziroqueeraesperadomasmesmoassimsemprepudecontarcoma
paciênciaeapoiodetodos.
Porfim,agrade çoatodosquetrabalharamcomigo,emespecialparaos
diversosamigosquefiznouniversoPython.
iv
E-book gerado especialmente para 


## Página 9

CasadoCódigo
Agradecimentos
Erratas
Essecapítuloédedicadoaoscontribuidoresdolivro:
• SandroDutra-Errata-Seção2.2
• FranciscoAndré-Errata-Seção3.1
• AndréFrança-Errata-Se ção4.1
v
E-book gerado especialmente para 


## Página 10

E-book gerado especialmente para 


## Página 11

CasadoCódigo Sumário
Sumário
SeusprimeirospassoscomoPython 1
1 IniciandocomPython 3
1.1 AlinguagemPython . . . . . . . . . . . . . . . . . . . . . . . . 3
1.2 DePython2paraPython3 . . . . . . . . . . . . . . . . . . . . 6
1.3 Diversosinterpretadoresemesmalinguagem . . . . . . . . . 7
1.4 Preparandooambiente . . . . . . . . . . . . . . . . . . . . . . 8
1.5 Primeiropasso:abraointerpretador . . . . . . . . . . . . . . 8
1.6 Primeirasexplora ções. . . . . . . . . . . . . . . . . . . . . . . 9
1.7 Próximospassos . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2 AprendendoPythonnaprática:númerosestrings 11
2.1 Números . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.2 ComomanipulartextoemPython . . . . . . . . . . . . . . . 16
2.3 Criandoemanipulandotexto:strings . . . . . . . . . . . . . . 16
2.4 ComoPythonrepresentastringsinternamente? . . . . . . . . 21
2.5 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
3 Manipulaçõesbásicas 25
3.1 Umacalculadora:oexemplorevisadomaiscomum . . . . . 25
3.2 Pegandodadosnoterminal . . . . . . . . . . . . . . . . . . . . 26
3.3 Comparações:maior,menor,igualeoutras . . . . . . . . . . 27
3.4 Condicionais:if,elif&else . . . . . . . . . . . . . . . . . . . . 28
3.5 Operadoreslógicos . . . . . . . . . . . . . . . . . . . . . . . . 31
vii
E-book gerado especialmente para 


## Página 12

Sumário CasadoCódigo
3.6 Loopscomwhile . . . . . . . . . . . . . . . . . . . . . . . . . . 31
3.7 Primeiraestruturadedados:lista . . . . . . . . . . . . . . . . 32
3.8 Looppythônicocomforelistas . . . . . . . . . . . . . . . . . 34
3.9 Percorrendointervalosdezeroaténcomrange() . . . . . . . 35
3.10 Enumerandocoleçõescomforefun çãoenumerate. . . . . . 36
3.11 Declarandofunções:comandodef . . . . . . . . . . . . . . . 37
3.12 Valorespadronizadosdeargumentos . . . . . . . . . . . . . . 37
3.13 Parâmetrosnomeados. . . . . . . . . . . . . . . . . . . . . . . 38
3.14 Recebendoumnúmeroarbitráriodeargumentos:packing&
unpacking. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
3.15 Usandocódigojápronto:importandomódulos . . . . . . . . 41
3.16 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
4 Primeiroprograma:downloaddedadosdaCopa2014 43
4.1 Criandoumafun çãoparadownloadnaweb . . . . . . . . . . 43
4.2 Primeiroprogramacompleto . . . . . . . . . . . . . . . . . . . 45
4.3 Definindofun çõesmain . . . . . . . . . . . . . . . . . . . . . 45
4.4 Realizandoodownload . . . . . . . . . . . . . . . . . . . . . . 48
4.5 Maisdobásico:extraindoarquivosdedadosemetadados . . 49
4.6 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
5 Estruturasdedados 53
5.1 Montandoummodeloconceitualusandoestruturasdedados 53
5.2 Dicionários:fundaçãodalinguagem . . . . . . . . . . . . . . 55
5.3 Montandoodicionáriodemetadados . . . . . . . . . . . . . 56
5.4 Adicionandoeremovendoelementosemumalista . . . . . . 58
5.5 Iterandodicionários:vendovaloresechaves . . . . . . . . . . 60
5.6 Tuplas:sequênciasimutáveis . . . . . . . . . . . . . . . . . . . 62
5.7 Explorandoosdadosquecoletamos . . . . . . . . . . . . . . . 63
5.8 Exemplofinalusandoestruturasdedadosparaexploraros
metadados . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
5.9 Estruturasdedadossãoimportantes? . . . . . . . . . . . . . . 70
5.10 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
viii
E-book gerado especialmente para 


## Página 13

CasadoCódigo Sumário
6 Classeseobjetospythônicos 71
6.1 Expressandoodomínioemclasses . . . . . . . . . . . . . . . 72
6.2 Definindoclasses:primeiropasso . . . . . . . . . . . . . . . . 72
6.3 Criandoobjetos:métodosconstrutores . . . . . . . . . . . . . 74
6.4 Classesdocumentadas:docstrings . . . . . . . . . . . . . . . . 76
6.5 Métodos:adicionandocomportamentosaoobjeto . . . . . . 78
6.6 HerançasimplesemPython . . . . . . . . . . . . . . . . . . . 81
6.7 Atributosdeclasses:compartilhadosentretodasinstâncias . 86
6.8 Métodosestáticosedeclasse:usandomaisasclasses . . . . . 87
6.9 Encapsulamentopythônicocomafun çãoproperty. . . . . . 90
6.10 Herançamúltipla:herdandodeváriasclasses . . . . . . . . . 92
6.11 OqueéDuckTyping? . . . . . . . . . . . . . . . . . . . . . . . 94
6.12 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
7 Tratandoerroseexce ções:tornandoocódigomaisrobusto 97
7.1 Escreveuerrado?Errosdesintaxe . . . . . . . . . . . . . . . . 97
7.2 Comotornarocódigomaisrobusto? . . . . . . . . . . . . . . 98
7.3 Tratandováriaspossíveisexce çõesemummesmobloco . . . 100
7.4 ExceçõesePython3.3+ . . . . . . . . . . . . . . . . . . . . . . 102
7.5 Executandocódigosenenhumaexce çãoforlevantada . . . . 104
7.6 Açõesdelimpeza . . . . . . . . . . . . . . . . . . . . . . . . . . 104
7.7 Comandoraise:levantandoexce ções . . . . . . . . . . . . . . 105
7.8 ExemplodeumtratamentodeerrosmaisrobustoemPython 107
7.9 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
8 TestesemPython:umapráticasaudável 111
8.1 CriandooprimeiroTestCase . . . . . . . . . . . . . . . . . . . 112
8.2 Rodandoumarquivocomtestes . . . . . . . . . . . . . . . . . 114
8.3 APIdelinhadecomandoparatestes . . . . . . . . . . . . . . 117
8.4 APIdabibliotecaunittest . . . . . . . . . . . . . . . . . . . . . 119
8.5 CustomizandosaídaparaHTML . . . . . . . . . . . . . . . . 120
8.6 ImplementandoumTestRunnercustomizado . . . . . . . . . 121
ix
E-book gerado especialmente para 


## Página 14

Sumário CasadoCódigo
8.7 Testandoerros:quandoocódigojogaexce ções . . . . . . . . 125
8.8 Inicializaçãoefinaliza ção:setUpetearDown . . . . . . . . . 128
8.9 Açõesdelimpezanostestesunitários:cleanupactions . . . . 130
8.10 Mocks/Stubs:outraabordagemdetestesunitários . . . . . . 132
8.11 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
9 Módulosepacotes:organizandoedistribuindocódigo 139
9.1 MódulosemPython:primeiropasso . . . . . . . . . . . . . . 141
9.2 Oqueacontecequandoimportamosummódulo? . . . . . . 146
9.3 Pacotes:agrupandomódulos . . . . . . . . . . . . . . . . . . . 148
9.4 Definindonomesparaexporta çãoeescopodeexporta ção . 149
9.5 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151
MundoPython–Alémdosrecursosfundamentais 153
10 Trabalhandocomarquivos 155
10.1 Importandodadosparaastabelas . . . . . . . . . . . . . . . . 155
10.2 Lendoarquivos. . . . . . . . . . . . . . . . . . . . . . . . . . . 157
10.3 Fechandoarquivos. . . . . . . . . . . . . . . . . . . . . . . . . 159
10.4 Abrindoarquivoscomocomandowith . . . . . . . . . . . . 160
10.5 Escrevendoemarquivos . . . . . . . . . . . . . . . . . . . . . 161
10.6 Navegaçãoavan çadacomseek() . . . . . . . . . . . . . . . . . 162
10.7 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163
11 Umpasseioporalgunstiposdefinidosnabibliotecapadrão 165
11.1 Dinheiroedecimaiscomprecisãoarbitrária . . . . . . . . . . 166
11.2 Datasetempo:módulodatetime . . . . . . . . . . . . . . . . 169
11.3 Conjuntossemrepetição:set(). . . . . . . . . . . . . . . . . . 175
11.4 Tuplasnomeadas:tuplasqueparecemobjetoscomatributos 179
11.5 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 180
x
E-book gerado especialmente para 


## Página 15

CasadoCódigo Sumário
12 Conceitosepadrõesdalinguagem 183
12.1 Iteráveiseporqueocomandoforfunciona? . . . . . . . . . . 184
12.2 Objetoschamáveis:callables() . . . . . . . . . . . . . . . . . . 185
12.3 Protocolosabstratos: comocomportamentospadronizados
funcionam . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187
12.4 ClosuresemPython . . . . . . . . . . . . . . . . . . . . . . . . 188
12.5 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189
13 Elementoscomsintaxeespecífica 191
13.1 Listcomprehensions. . . . . . . . . . . . . . . . . . . . . . . . 191
13.2 Dictscomprehensions. . . . . . . . . . . . . . . . . . . . . . . 194
13.3 Decoradoresdefunção:@decorators . . . . . . . . . . . . . . 196
13.4 Funçõesanônimas:lambdas . . . . . . . . . . . . . . . . . . . 202
13.5 Funçõesgeradoras . . . . . . . . . . . . . . . . . . . . . . . . . 203
13.6 Palavrareservadanonlocal . . . . . . . . . . . . . . . . . . . . 206
13.7 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208
14 Explorandoaflexibilidadedomodelodeobjetos 211
14.1 Construtures:criandoobjetos . . . . . . . . . . . . . . . . . . 212
14.2 Representaçãotextualdeobjetos:fun çãoprint(),str()erepr() 214
14.3 Comparandoigualdadedeobjetos . . . . . . . . . . . . . . . 216
14.4 Outrostiposdecompara çõesbinárias . . . . . . . . . . . . . 218
14.5 Dicionáriointernodeatributos . . . . . . . . . . . . . . . . . 219
14.6 Interceptandooacessoaatributos . . . . . . . . . . . . . . . . 222
14.7 Protocolosemétodosespeciais . . . . . . . . . . . . . . . . . 225
14.8 Protocolodecontainer . . . . . . . . . . . . . . . . . . . . . . 226
14.9 Protocolodecontainerscomtamanhodefinido . . . . . . . . 227
14.10Protocolodeiteráveiseiteradores . . . . . . . . . . . . . . . . 228
14.11 Protocolodesequências. . . . . . . . . . . . . . . . . . . . . . 230
14.12 Protocolodemapas . . . . . . . . . . . . . . . . . . . . . . . . 232
14.13 Protocolosnuméricos . . . . . . . . . . . . . . . . . . . . . . . 233
14.14Oquemaisversobreclassesemodelodeobjetos? . . . . . . 235
14.15 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 235
xi
E-book gerado especialmente para 


## Página 16

Sumário CasadoCódigo
15 Consideraçõesfinais 237
15.1 Nuncapare!. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 237
15.2 Aprenditudo? . . . . . . . . . . . . . . . . . . . . . . . . . . . 237
15.3 ComunidadePython . . . . . . . . . . . . . . . . . . . . . . . 239
15.4 Paraondeir? . . . . . . . . . . . . . . . . . . . . . . . . . . . . 240
ÍndiceRemissivo 241
Bibliografia 244
Versão:18.9.26
xii
E-book gerado especialmente para 


## Página 17

ParteI
Seusprimeirospassoscomo
Python
Aolongodolivro,vamosdesenvolverumaplicativoquerealizaumpro-
cessorelativamentecomplexoparaconseguirextrairinforma çãodosdados
públicosdoGovernoFederal. Basicamente,elefazumdownloaddainter-
net,abreoarquivotrazidoefazalgumasconsultasnoconteúdo. Paraque
diversasbuscaspossamserfeitas,eletambémcriaumaabstra çãoemcima
dosdados,comosefosseumpequenobancodedados. Pormeiodetodaa
motivaçãopráticaparaosaspectosapresentadosnesseaplicativo,demons-
traremosdiversosrecursosdalinguagemPython:cria çãodefun ções,usode
loops,tratamentodeerro,cria çãodeclasseseoutros.
Nestaprimeiraparte,vamosabordarosaspectosmaisbásicosdePython,
quegeralmenteexistememoutraslinguagens,emostrarquenãoexistemli-
mitesnoresultadoounoimpactodosnossosprogramas,mesmocomobá-
sico.
Eaí?Estápreparadoparacome çar?
E-book gerado especialmente para 


## Página 18

E-book gerado especialmente para 


## Página 19

Capítulo1
IniciandocomPython
1.1 Alinguagem Python
Pythonéumalinguageminterpretadadealtonívelequesuportamúltiplos
paradigmasdeprograma ção:imperativo,orientadoaobjetosefuncional.É
umalinguagemcomtipagemdinâmicaeforte,escopoléxicoegerenciamento
automáticodememória. Possuialgumasestruturasdedadosembutidasna
sintaxe–comotuplas,listasedicionários–queaumentammuitoaexpres-
sividadedocódigo.Alémdetudoisso,Pythonpossui baterias inclusas,uma
expressãoqueserefereaumavastabibliotecapadrãocomdiversosutilitários
poderosos.
AsintaxebásicadePythonébemsimplesepodeseraprendidarapida-
mente.Commaisprática,elementosmaiscomplexos–comocomprehensions,
lambdas, packinge unpackingdeargumentos–vãopassandoafazerpartedo
diaadiadoprogramador.Estalinguagemtemumacaracterísticanãomuito
E-book gerado especialmente para 


## Página 20

1.1. AlinguagemPython CasadoCódigo
comum,queéousodaindenta çãocomoformadedefini çãodeblocosdecó-
digo.AcomunidadePythonprezamuitopelalegibilidadedocódigoepossui
doiselementosquerefor çamaindamaisessaquestão: PEP-8e The Zen of
Python.
OPEP-8[ 9]éumguiadeestilosdecódigoPythonqueéamplamente
empregadoeexistemdiversasferramentasparachecá-loautomaticamente.
OThe Zen of Python[8]éumpequenotextoquefalamuitosobreoestilode
programaçãoemPython.
Apesardeserumalinguageminterpretada,existeumprocessodecompi-
laçãotransparentequetransformaocódigotextoembytecode,que,porsua
vez,éinterpretadoporuma virtual machine(VM).Aimplementa çãopadrão
dalinguagemPythonéchamadadeCPythone,apesardeexistiremoutras
implementaçõesdaespecifica ção,énestaquevamosfocar,porqueéaque
hojeimplementaaversão3.x,queseráabasedestelivro.
TheZenofPython
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren’t special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one – and preferably only one – obvious way to do it.
Although that way may not be obvious at first unless you’re Dutch.
Now is better than never.
Although never is often better than right now.
If the implementation is hard to explain, it’s a bad idea.
4
E-book gerado especialmente para 


## Página 21

CasadoCódigo Capítulo1. IniciandocomPython
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea – let’s do more of those!
Tradução
Bonitoémelhorquefeio.
Explícitoémelhorqueimplícito.
Simplesémelhorquecomplexo.
Complexoémelhorquecomplicado.
Linearémelhorqueaninhado.
Esparsoémelhorquedenso.
Legibilidadeconta.
Casosespeciaisnãosãoespeciaisosuficienteparaquebrarregras.
Emborapraticidadeprevale çasobrepureza.
Errosnuncadevemsersilenciados.
Anãoserexplicitamente.
Diantedeumaambiguidade,nãocaianaarmadilhadochute.
Deveexistirum–epreferencialmenteum–jeitoóbviodesefazer
algo.
Emborapossanãopareceróbvioanãoserquevocêsejaholandês.
Agoraémelhorquenunca.
Emboranuncanormalmentesejamelhorqueexatamente agora.
Seaimplementa çãoédifícildeexplicar,elaéumamáideia.
Seaimplementa çãoéfácildeexplicar,talvezsejaumaboaideia.
Namespacessãoumagrandeideia–vamosusá-losmais!
PEP-8
ÉimportanteleraPEPpelomenosumavez,poisháváriosdetalhesin-
teressantes. Certospontossãoconsideradosindispensáveisporquasetoda
comunidade.Eisalgunstópicosimportantesquevaledestacar:
• Use4espaçosparaindenta ção;
• NuncamistureTabseespa ços;
5
E-book gerado especialmente para 


## Página 22

1.2. DePython2paraPython3 CasadoCódigo
• Tamanhomáximodelinhaé79caracteres;
•lower_case_with_underscoreparanomesdevariáveis;
•CamelCaseparaclasses.
Oguiatemmaisitenssobreindenta ção,espa çamento,sugestõesdecomo
usar importsemuitomais. AgrandemaioriadosprogramadoresPython
acabaadotandograndepartedaPEP-8[ 9]noseudiaadia. Porisso,asua
leituraéfortementerecomendada. VocêencontraaPEP-8disponívelem
http://www.python.org/dev/peps/pep-0008/.
1.2 DePython 2 paraPython 3
Duranteolivro,abordaremosaversão3doPython. Noentanto,épreciso
saberqueexistemalgumasdiferen çasimportantesentreelaeaversão2.Uma
delaséadefini çãode stringsede unicodes.EmPython2,stringsebytessão
um(eomesmo)tipo,enquantounicodeéumoutro.JánoPython3,strings
sãounicodeseosbytessãooutrotipo.
Sevocênãofazideiadoquesejamunicodes,aquivaiumabreveexplica-
ção:emidiomascomooportuguês,temosletrasquepodemseracompanha-
dasdeacentos(porexemplo, é).Tradicionalmente,essescaracteresnãotêm
representaçãodiretanatabelaASCII.Quandoumcaractereestánessatabela,
elenormalmentepodeserrepresentadocomapenas1bytedememória.Em
outroscasos,comoemoutrosidiomas,algunscaracteresprecisamdemais
de1byteparaseremrepresentados. Criou-se,então,umpadrãochamado
unicode[2],noqualforamdefinidos code points–emumasimplificação,po-
demosentendercomonúmeros–paradiversoscaracteresdeváriaslínguase
paraalgunsoutrostiposespeciaisdecaracteres.
Depoisdapadroniza ção,apareceramos codecs,queconvertemos code
pointsemsequênciasdebytes,jáque,quandosetratadeunicodes,nãotemos
maisarela çãode1caracterepara1byte.OcodecmaisfamosoéoUTF-8[ 14],
criadocomobjetivodeteramelhorcompatibilidadepossívelcomopadrão
ASCII.
NoPython2,comojádito,otipostringéomesmoqueotipobyteeum
objetounicodedeveserconvertidoparastringusandoumcodeccomoUTF-
6
E-book gerado especialmente para 


## Página 23

CasadoCódigo Capítulo1. IniciandocomPython
8. NoPython3,ouseja,nonossocaso,asstringssãounicodesporpadrão.
Quandoénecessárioobteroconjuntodebytesqueaformam,éprecisocon-
vertercomumcodec.Issoserávistocomumpoucomaisdedetalhesmaisà
frente.
EmPython3existeapenasumtipo intquesecomportabasicamente
comootipo longdoPython2.Talmudan çageralmentenãoépercebidana
migraçãodeumaversãoparaoutra.
Alémdisso,usaremosummódulonovocomfun çõesdeestatística,cha-
mado statistics.OutranovidadedoPython3éomódulo asyncio,que
tratadeI/Oassíncrono.Entretanto,suaaplica çãoexigemaisconhecimento
préviodoleitorarespeitodeI/O,loopdeeventos,programa çãoassíncrona
eoutrosassuntosmaisavan çadosqueestãoforadoescopodestelivro.Mas,
mesmoassim,essemódulomerecemen çãopelasuaimportância.
Nogeral,muitosconsideramquealinguagemficoumaisconsistente.Ou-
trasdiferençasserãoexemplificadascomcódigosaolongodolivro.Naprá-
tica,paraquemestáiniciandocomPython,elasnãoserãotãoimportantese
sóserãodestacadasquandopertinente.
1.3 Diversos interpretadores e mesma lingua -
gem
Pythonpossuidiversasimplementa ções. Aquivamosfocarnaimplemen-
taçãoquepodemoschamardereferência, CPython. Essaimplementaçãoé
feitaemCeé,delonge,amaisamplamenteutilizada.Outraimplementa ção
muitofamosaepoderosaéchamada PyPy,uminterpretadorPythonescrito
emPython,quecontacomumpoderoso JIT Compiler(Just-in-time compiler),
quemelhoraodesempenhodemuitosprogramasejáéusadoemprodu ção
poralgumasempresas.Éumprojetobemcomplexoeousado,masquevem
mostrandobonsresultadoseumcrescimentoemsuaado ção,assimcomo
umaparticipaçãomaiorporpartedacomunidade.
Aindatemos Jython,aimplementa çãodePythonemJava,queémais
usadaporprojetosemJavaquequeremoferecerumalinguagemmaissimples
paraalgumastarefas,emumcontextodeexecu çãodeumamáquinavirtual
Java.Seguindoummodelosemelhante,temoso IronPython,queéaimple-
7
E-book gerado especialmente para 


## Página 24

1.4. Preparandooambiente CasadoCódigo
mentaçãodePythonparaaplataforma.NET.
1.4 Preparando o ambiente
Oiníciodetudoéosite http://python.org.Osprincipaislinksrelacionados
àprogramação,documenta çãoedownloadsestãolá.Adocumenta çãoéboa
ebem-organizada,ecobrediversosaspectoscomoinstala ção,bibliotecapa-
drão,distribui çãoetc.
SevocêusaWindows, conseguefazerodownloaddoarquivo .msi
einstalarfacilmente. Jáainstala çãopadrãodamaioriadasdistribui ções
OSX/LinuxinstalaPythoncomopadrão,entretantonemsempreseráaver-
são3. Casonãoseja,existemdoiscaminhos:instalarcomomecanismode
pacotesdosistema(porexemplo, apt-getnoUbuntu,ou brewnoOSX);
oucompilardocódigo-fonteeinstalar.
Paramaioresdetalhes,existebastantematerialnainternetcomexplica-
çõesmaisdetalhadasparaoutrasplataformasetambémcomocompilarapar-
tirdocódigo-fonte.
1.5 Primeiro passo: abra o interpretador
Oprimeiropassoéinvocarointerpretador,executando python,geralmente
usandoumconsole.OqueabreéumconsolePythoninterativo,noqualpode-
mosescrevercódigoseverosresultadosimediatamente.Existeumcabe çalho
quedizqualéaversãoe,logodepois,oponteirodoconsoleinterativo.
Oconsoleinterativofacilitamuitooprocessodeaprendizagem,porque
permitequetrechosdecódigosejamexecutadosemumciclodeavalia çãode
expressõescontínuo.
$ python
Python 3.4.1 ( default, Aug 24 2014, 21:32:40 )
[ GCC 4.2.1 Compatible Apple LLVM 5.1 ( clang-503.0.40 )] on darwin
Type "help" , "copyright" , "credits" or "license" for more
information.
>>>
8
E-book gerado especialmente para 


## Página 25

CasadoCódigo Capítulo1. IniciandocomPython
Invocando o interpretador
Em algumas instalações, o interpretador pode estar no arquivo
python3.3emvezde python.
1.6 Primeiras explorações
Dentrodoconsoleinterativo,asexpressõesjápodemseravaliadas,fun ções
invocadasemódulosimportados,exatamentecomoemumprogramanor-
mal.
>>> 1
1
>>> 3 / 2
1.5
>>> print ( "Hello World" )
"Hello World"
Apósconfirmarocomandocomo Enter,oresultadoéexibidologo
abaixo.
Notequeoconsoleservemaisparaexplora çãodoqueparaelabora-
çãodeprogramas. Paraexecutarprogramas, bastautilizarmos python
nome_do_programa.py. Aextensão .pyénormalmenteusadaparaos
programasemPython. Inicialmente,vamosconsiderarquenossosprogra-
massempreestãonomesmoarquivoatéfalarmossobremódulos.
1.7 Próximos passos
Comoemtodoaprendizadodeumalinguagemdeprograma ção,oprimeiro
passoéinstalarocompiladorouinterpretador.DepoisdeinstalaroPython
3.3,3.4ousuperior,jápodemosabriroconsoleinterativoeiniciarasprimeiras
explorações.
Esse processo de exploração do console interativo acaba tornando-se
partedodiaadiadoprogramadorPython. Oconsoleéumaformamuito
rápida de testar trechos de código e consultar documentação. Além do
9
E-book gerado especialmente para 


## Página 26

1.7. Próximospassos CasadoCódigo
consolepadrão, existemmuitosoutroscommaisrecursos, como Ipython
(http://ipython.org/)e bpython(http://bpython-interpreter.org/).Oprojeto
Ipythonéamplamenteutilizadoesuainstala çãoésugerida. Elepossuidi-
versosrecursos,incluindo auto completedeobjetosnopróprioconsole,entre
outrascoisas.
Esse console interativo também possui uma ferramenta de
ajuda/documentação que pode ser usada chamando help() dentro
doconsole.Nopróximocapítulo,vamoscome çaroestudodamanipula ção
dostiposbásicosdePython. Dessaforma,daremosumpassoimportante
paraoaprendizadodasualinguagemedecomousá-la.
Emborasejacomumabriromodointerativomúltiplasvezesduranteode-
senvolvimento,softwareemPythonnãoéfeitonesseconsole.Maisàfrente,
veremoscomocriarpacotesedistribuirsoftwareescritoemPython,eusare-
mosomodointerativoparaestudoeprototipa ção.
Naspróximasetapas,vamosfalarumpoucomaisdecaracterísticasgerais
dalinguagemeiniciaraparteprática.
10
E-book gerado especialmente para 


## Página 27

Capítulo2
AprendendoPythonnaprática:
númerosestrings
Na prática, todos os programas vão manipular textos ou números. Por
isso,precisamossabertrabalharcomessestiposfundamentais.Nouniverso
Python,ostermosqueusaremossão númerose strings. Manipulá-losére-
lativamentesimplesatéparanãoprogramadores.Primeiro,vamosconhecer
osconceitosbásicos,paradepoisexploraralgunsexemploseexplicarmais
detalhesdosseuscomportamentos.
2.1 Números
Emprogramasdecomputador,quasesemprevamosmanipularnúmeros.Um
dosprimeirospassosparaaprenderumalinguagemdeprograma çãoésa-
E-book gerado especialmente para 


## Página 28

2.1. Números CasadoCódigo
bercomooperarseusnúmeros. Cadalinguagemdisponibiliza,porpadrão,
algunstiposdenúmerosembutidosqueestãopresentesemsuasintaxe;há
outrosemmódulospodemserimportadosesãomanipuladospormeiode
objetoseAPIs.
Python 3 possui três tipos de números embutidos:int, floate
complex.
Inteirossãovirtualmenteilimitados[ 3]epodemcresceratéolimiteda
memória.Outrotipomuitoconhecidodenúmeroséopontoflutuante,cha-
madode float. EmPython,nointerpretadorpadrãoCPython,os floats
sãoimplementadosusandootipo doubledoC[ 13].Entretanto,emoutros
interpretadores–comoJython–,issoéfeitopormeiodotipoflutuantede
precisãodupladaplataformaabaixo,nocasoaJVM.
Osnúmeroscomplexostambémestãoembutidosnalinguagem,massua
aplicaçãonãoétãocomumnodiaadia.Elestêmaparteimagináriaeareal,
sendoquecadaumadelaséum float.Osnúmeroscomplexos,porexem-
plo,dãorespostacomoaraizquadradadeumnúmeronegativoesãousados
emdomínioscomoengenhariaelétrica,estatísticaetc.
Númerosinteirossãoescritosnormalmentecomoemsuaformaliteral
(porexemplo, 100)etambémpodemsergeradosusandoafun ção int()
comoem int(‘1’),noqualgeramosonúmerointeiro 1apartirdeuma
string. Númerosdepontoflutuantetêmocaractere .–comoem 2.5
–,parasepararascasasdecimais. Tambémpodemsergeradospelafun ção
float()–comoemfloat(1)ou float(‘2.5’)–,esãoaceitasnafun-
ção float()asstrings nane infcomprefixosopcionais +e -–porexem-
plo, float(‘+nan’).Osnúmeroscomplexostêmosufixo jou J,como
em 1+2J.Paraacessara partereal ea parteimaginária,use 1+2j.real
ou 1+2j.imag.
FormasliteraisdeescreverosnúmerosbásicosemPython:
>>> 1 #int
1
>>> 1.0 #float
1.0
>>> 1. #também float
1.0
12
E-book gerado especialmente para 


## Página 29

CasadoCódigo Capítulo2. AprendendoPythonnaprática:númerosestrings
>>> 1+2j #complex
1+2j
Gerandoosnúmerospormeiodasfun çõesembutidas:
>>> int ( 1.0 )
1
>>> int ( '9' )
9
>>> float ( 1 )
1.0
>>> float ( '9.2' )
9.2
>>> float ( '-inf' )
-inf
>>> float ( '+inf' )
inf
>>> float ( 'nan' )
nan
>>> complex ( 1 , 2 )
(1+2j)
Ints e longs unificados no Python 3
DiferentedoPython2,noqualexistem2tiposdeinteiros, inte
long,oPython3contém apenaso int,quesecomportacomoo long
doPython2.Anteriormente,uminteiropoderiatornar-seumlongose
ultrapassasseolimitede sys.maxint. APEP-237[7]foiresponsável
poressaunifica ção.
Aseguir,algunsexemplosdenúmerosemanipula çõessimplesquevocê
podefazerparatestarseuambiente:
>>> 3 + 2
5
>>> 3 + 4.2
7.2
13
E-book gerado especialmente para 


## Página 30

2.1. Números CasadoCódigo
>>> 4 / 2
2.0
>>> 5 / 2
2.5
>>> 5 // 2
2
>>> complex ( 1 , 2 ) + 2
(3+2j)
>>> complex ( 2 , 0 ) + 0+1j
(2+1j)
>>> 2 + 0+1j
(2+1j)
Algunsoperadorespodemsernovos,comoo //.Vamosestudá-losem
seguida!
Operadoresaritméticos
OconjuntobasedeoperadoresaritméticoscomnúmerosemPythoné:
x + y (adição), x - y (subtração), x / y (divisãoempontoflutuante), x
// y (divisãodescartandopartefracionária), x * y,(multiplicação), x %
y(resto), -x(negação)e x ** y(potência).
>>> 1 + 2
3
>>> 3 - 1
2
>>> 10 / 2
5.0
>>> 10 // 3
3
>>> 10 * 2 + 1
21
>>> 10 % 3
1
>>> -3
-3
>>> 2 ** 8
256
14
E-book gerado especialmente para 


## Página 31

CasadoCódigo Capítulo2. AprendendoPythonnaprática:númerosestrings
Operadoresdebits
Oconjuntobasedeoperadorescombitsé: x | y (ou), x ^y (ouexclu-
sivo), x & y (e), x << y (xcomybitsdeslocadosàesquerda), x >> y (x
comybitsdeslocadosàdireita)e ~x(inversoembits).
>>> 1 | 0
1
>>> 1 | 5
5
>>> 1 ^ 5
4
>>> 4 & 1
0
>>> 1 << 2
4
>>> 4 >> 2
1
>>> ~4
-5
Operaçõesmisturandotiposdiferenteseasregrasdecoer ção
ComoPythonéumalinguagemdinâmica,muitosprogramaspodemope-
rarnúmerosdetiposdiferentesemumamesmaopera ção.Podemosdefinir
ovalordeumimpostocomum floateaplicaraumvalorinteiro.Vejao
exemplo:
>>> 100 * 1.3 # preço mais 30%
130.0
Paraisso,existeumapolíticadecoer çãodenúmerosquedefinequalo
tiporesultantedeumaopera çãoquemisturatiposdiferentesdenúmeros.
Seoperarmosum inteum float, vamostercomoresultadoum
float. Seoperarmosum intou floatcomum complex,vamoster
comoresultadoum complex.
Explorandoasopera çõesporcontaprópria:
>>> type ( 1 + 2.0 )
<class 'float'>
15
E-book gerado especialmente para 


## Página 32

2.2. ComomanipulartextoemPython CasadoCódigo
>>> type ( 1 + 2 J)
<class 'complex'>
>>> type ( 1.0 + 2 J)
<class 'complex'>
>>> type ( 1.0 + 1.0 )
<class 'float'>
Função type ()
Afunção type(obj),comapenasumparâmetro,retornaotipo(ou
classe)deumobjeto. Nadúvida,use-aedescubraotipodeumobjeto
referenciadoporumavariável. Pararealizartestesemcondicionais,é
recomendadoousodafun ção isinstace(obj, class).Parameras
verificaçõesemexplora çõesnosterminais,use type()quandotiver
dúvidasobreotipodeumavariável.
2.2 Como manipular texto em Python
Astringéumtipo(ouclasse)fundamentalemmuitaslinguagens. Nasde
altonível,suamanipula çãogeralmenteéfácil.Pythonpossuimuitasconve-
niênciasnamanipulaçãodestringsquevamosentendermelhordaquipara
afrente.Alémdemanipular,vamosentendercomoPython3representain-
ternamenteequaisasimplica çõespráticasdasuaimplementa çãoatualde
strings.
DiferentedelinguagenscomoC,nãoexisteotipo char,queéumtipo
inteiro,de1byte,usadoprarepresentarvaloresdatabelaASCII.EmPython,
existemapenasstrings,mesmoquecontenhamapenasumcaractereousejam
vazias.Portanto,podemosinterpretarqueelassãosequênciasdecaracteres
detamanho0atéomáximosuportado.
2.3 Criando e manipulando texto : strings
Pythontemformasmuitoconvenientesdedeclararstringsedeformatá-las.
Vamosveralgunsexemplos:
16
E-book gerado especialmente para 


## Página 33

CasadoCódigo Capítulo2. AprendendoPythonnaprática:númerosestrings
# coding: utf-8
"Copa 2014"
'Copa do mundo 2014'
'''2014 - Copa do mundo
'''
"copa 'padrão fifa'"
'copa "padrão fifa"'
Osformatosprincipaissãocom ‘e ",sendoqueaousarum,ooutro
podeserusadointernamentecomonosdoisúltimosexemplos.Outraop ção
sãoas multiline strings,comtrêsaspassimplesoutrêsaspasduplas. Elaé
muitoempregadaemformata çõesdesaídasdeconsole.Vejanocódigo:
# coding: utf-8
print ( """\
Uso: consulta_base [OPCOES]
-h Exibe saída de ajuda
-U url Url do dataset
""" )
Oquegeraráaseguintesaída:
Uso: consulta_base [ OPCOES ]
-h Exibe saída de ajuda
-U url Url do dataset
Reparena \noiníciodastringqueescapao \ndaquebradelinha.
Asstringsliteraisseparadasapenasporespa çoserãoimplicitamentecon-
vertidasemumaúnicastringliteral.
( "Copa" "2014" ) == "Copa2014"
Épossívelquebrarstringslongasquenãosão multilineapenasaoquebrar
alinha,depreferênciaindentando-as.
17
E-book gerado especialmente para 


## Página 34

2.3. Criandoemanipulandotexto:strings CasadoCódigo
input ( 'Em qual cidade o legado da Copa foi mais relevante '
'para a populacao?' )
Prefixo de literal unicode
Ao ler código Python, certamente você ainda encontrará muitas
stringscomoprefixo u,porexemplo u"minha string". Essasin-
taxesurgiunaversão2paradizerqueumastringestáescritaemuni-
code.Jánaversão3.3,asintaxe u"minha string" passounovamente
aseraceita,parafacilitaraportabilidadedeprogramasescritosnaver-
são2,nosquaisosliteraisunicodedevemterobrigatoriamenteoprefixo,
comoem u’string’.Anteriormente,nasversões3.0até3.2,asstrings
comprefixo ueramumerrodesintaxe.
Stringéumasequência
Emstringspodemosacessaroselementos code pointsusandoumíndice
eanota ção variavel[ index ] . Oíndicevariade0atéotamanhoda
stringmenos1.Seelefornegativo,acontageménaordeminversa.Oquadro
aseguirilustramelhor:
.
+---+---+---+---+---+---+
| P | y | t | h | o | n |
+---+---+---+---+---+---+
0 1 2 3 4 5 6
-6 -5 -4 -3 -2 -1
EmPython,otermo sequênciatemumsignificadoespecial.Paraqueum
objetosejauma sequência,comoumastring,eledeveatenderalgunsrequisi-
tos.Aseguir,veremosaaplica çãodealgunsconceitosde sequênciaemstrings
Python.Trêsdassuasmanipulaçõesfundamentaissão:sabertamanho,aces-
sarumitemporposi çãoeacessartrechosporposi ções.
Parasaberotamanho,usamos len(string). Paraacessoporíndice,
utilizamos variavel[indice],ouparaacessodetrechos,a slice notation,
comoem minha_str[1:2]naprática:
18
E-book gerado especialmente para 


## Página 35

CasadoCódigo Capítulo2. AprendendoPythonnaprática:númerosestrings
>>> st = "maracana"
>>> st[ 0 ]
'm'
>>> st[ 1 : 4 ]
'ara'
>>> st[ 2 :]
'racana'
>>> st[: 3 ]
'mar'
>>> len (st)
8
Porserumasequência,alémdoacessoporíndicese slices,podemosexe-
cutaroutrasopera çõescomo: x in y ,sexestáemy; x not in y ,sex
nãoestáemy; x + t ,concatenaçãodexcomy;e x * y,yrepeti çõesdex.
>>> "m" in "maracana"
True
>>> "x" not in "maracana"
True
>>> "m" + "aracana"
'maracana'
>>> "a" * 3
'aaa'
Imutabilidade:novasstringscriadasapartirdeoutrasstrings
Asstringssãosequênciasimutáveisdecodepoints[ 10].Issosignificaque
elastêmseuvalordefinidonacria çãoequeasnovassempresãocriadasa
partirdasopera çõescomelas.Setentarmosmudarovalordeumaposi ção
oupedaçodeumastring,vamosreceberumerro:
>>> minha_str = "livro python 3"
>>> minha_str[ 13 ] = "2"
Traceback (most recent call last):
File "<stdin>" , line 1 , in <module>
TypeError : 'str' object does not support item assignment
Algumasformaspossíveis:
19
E-book gerado especialmente para 


## Página 36

2.3. Criandoemanipulandotexto:strings CasadoCódigo
>>> minha_str = "livro python 3"
>>> minha_str = minha_str[ 0 : 13 ] + "2"
>>> minha_str
'livro python 2'
>>> minha_str = "livro python 3"
>>> minha_str = minha_str . replace( "3" , "2" )
>>> minha_str
'livro python 2'
Principaismétodos
Temos a documentação de todos os métodos de strings da biblio-
tecapadrãodisponívelem http://docs.python.org/3.3/library/stdtypes.html#
string-methods. Alguns muito comuns são: capitalize, count,
endswith, join, split, startswithe replace.
>>> "maracana" . capitalize()
'Maracana'
>>> "maracana" . count( "a" )
4
>>> "maracana" . startswith( "m" )
True
>>> "maracana" . endswith( "z" )
False
>>> "copa de 2014" . split( " " )
['copa', 'de', '2014']
>>> " " . join([ "Copa" , "de" , "2014" ])
'Copa de 2014'
>>> "copa de 2014" . replace( "2014" , "2018" )
'copa de 2018'
Interpolaçãodestring
Em Python, podemos interpolar strings usando% ou a função
.format().
20
E-book gerado especialmente para 


## Página 37

CasadoCódigo Capítulo2. AprendendoPythonnaprática:númerosestrings
Python também implementa o formato printf de impres-
são, documentado em http://docs.python.org/3/library/stdtypes.
html#printf-style-string-formatting, assim como um formato pró-
prio, documentado em http://docs.python.org/3/library/string.html#
formatstrings.
>>> "%d dias para copa" % ( 100 )
'100 dias para copa'
>>> "{} dias para copa" . format( 100 )
'100 dias para copa'
>>> "{dias} dias para copa" . format(dias =100 )
'100 dias para copa'
Podemosconfigurarespa çamentosealinhamentos,daseguinteforma:
>>> '{:<60}' . format( 'alinhado à esquerda, ocupando 60 posições' )
'alinhado à esquerda, ocupando 60 posições '
>>> '{:>60}' . format( 'alinhado à direita, ocupando 60 posições' )
' alinhado à direita, ocupando 60 posições'
>>> '{:^60}' . format( 'centralizado, ocupando 60 posições' )
' centralizado, ocupando 60 posições '
>>> '{:.^60}' . format( 'centralizando ao alterar caractere
de espaçamento')
'......centralizando ao alterar caracter de espaçamento.......'
2.4 Como Python representa strings interna -
mente?
NoPython3,todasasstringssãorepresenta çõesemunicodecodepoints[ 10].
Elaspodemtercaracterescomacentos(porexemplo, "é")ouqualqueroutro
unicodeválido,comocaracteresdojaponês.
Aquestãoéquemuitoscaracteres,inclusivedalínguaportuguesa,não
podemserrepresentadosemapenas1byte. Então,foinecessáriaumadife-
renciaçãoentreosobjetosqueutilizamumbyteporletra,queseriamapenas
asletrasecaracteresdatabelaASCII,eosobjetosqueusamcaracteresque
necessitamdemaisde1bytepareseremrepresentados.
21
E-book gerado especialmente para 


## Página 38

2.5. Conclusão CasadoCódigo
NoPython2,umastringéumasequênciadebytes,logonãopodemre-
presentarunicodesanãoserqueestessejamconvertidosparabytescomum
codec.Aconteceque,nessaversão,muitasvezesumaconversãoimplícitaera
feitausandoUTF-8,estringsebytessãoomesmoobjeto,enquantounicode
éoutro.EnoPython3,stringseunicodessãoamesmacoisa( string)eos
bytesumoutroobjeto.
Assim,noPython2,astring "é"éimplicitamenteconvertidaparasua
representaçãoembytes,usandoUTF-8. Nessecaso,oseutamanhoseria
len("é") == 2 . Porém,noPython3.3,amesmastringteriatamanho1,
porqueelacontémapenasumcodepointerepresentaissosemanticamente.
Logo,otamanhoseria len("é") == 1 .
Issopoderiarepresentarumaperdadeespa çoseoscaracteresASCII–os
queconseguemserrepresentadosem1byte–tivessemqueocupar2bytesem
memória.Felizmente,aPEP-393( Flexible String Representation[6])fazcom
quePython3representeoscodepointsdemaneiraeficienteemmemória.
Emalgumassitua çõesespecíficaspodesernecessárioconverterexplici-
tamentestrings[10]parabytes.Issodeve-seaofatodequeumunicodepode
serconvertidoparabytespormeiodediversoscodecs,sendoosmaisfamo-
sosoUTF-8eoUTF-16.Omesmounicodetorna-seumasequênciadebytes
diferente,dependendodocodecusadonaconversão.
Existeumagrandediscussãosobreessamudan çadarepresenta çãoem
codepointsdasstrings,masnãovamosentraremdetalhesnestelivro. Na
visãodoautor,acomunidadeaindaestádigerindoosefeitosdessamudan ça.
Entre2013e2014,muitacoisafoiportadaparaPython3.3,masaado çãoainda
nãoéemlargaescala,emborasejabemrelevante.
2.5 Conclusão
Nestecapítulo,vimososaspectosfundamentaisdenúmerosestrings(texto)
emPythonealgumasdesuascaracterísticas.Aprendemosaescrevê-losem
suaformaliteralouusandofun çõesauxiliaresparagerá-losapartirdeoutros
dados,comogerarinteirosouflutuantesapartirdestrings.
Vimostambémumpoucosobredetalhesdaimplementa çãodestrings
emPythoneasdiferen çasqueesseobjetosofreunamigra çãodafamília2
22
E-book gerado especialmente para 


## Página 39

CasadoCódigo Capítulo2. AprendendoPythonnaprática:númerosestrings
paraa3,eaprendemosalgunsexemplosdemétodosdestringsdisponíveisna
bibliotecapadrão.
Aolongodolivro,exploraremosamanipula çãodenúmerosestringsno
contextodeumaplicativoquevamosdesenvolver.Nopróximocapítulo,va-
mosaprendermaisferramentasquenosajudarãoaestruturarnossosprogra-
mas,como:condicionais,cole çõeseloops.
23
E-book gerado especialmente para 


## Página 40

E-book gerado especialmente para 


## Página 41

Capítulo3
Manipulaçõesbásicas
Asmanipulaçõesbásicassãoasmanipula çõesaritméticassimpleseasope-
raçõescomobjetosefun ções,comodeclara çõesechamadas.Parapassaros
conceitosiniciaisdemanipula çõesaritméticas,vamosverumapequenacal-
culadoraaseguir.
3.1 Uma calculadora: o exemplo revisado mais
comum
Nossoprimeiroprogramavaiaplicarumataxa floatsobreumvalorqual-
quer int. Seessamesmataxaforutilizadaemdiversaspartesdeumpro-
grama,fazsentidoguardarovaloremumavariável.Seataxamudar,basta
trocarovalordeclaradodavariáveleorestodoprogramapermaneceigual.
Reparequeaindanãovimoscomocriarvariáveis.Conceitualmente,essata-
E-book gerado especialmente para 


## Página 42

3.2. Pegandodadosnoterminal CasadoCódigo
refachama-se atribuição.EmPython,umaatribui çãosefaz variavel =
expressão.Vamosverexemplosreais:
>>> imposto = 0.27
>>> salario = 5000
>>> print (salario - (salario * imposto))
3650.0
Nesseexemplo, salarioéum int,e impostoéum float.Repare
queoresultadoéum float,comovimosnasregrasdecoer ção.
Podemosaplicarformata çãodestringseexpressõesparatermosumre-
sultadomaisatraente:
>>> imposto = 0.27
>>> salario = 3000
>>> print ( "Valor real: {0}" . format(salario -
(salario * imposto)))
Valor real: 2190.0
3.2 Pegando dados no terminal
EmPython3,usamosafun ção input([prompt])paracapturarum input
dousuário.Comesserecurso,podemosperguntaraousuárioqualovalordo
impostocujosaláriorealeledesejacalcular.
Input no Python 2 e3
Na versão 2, a função para capturar a entrada do usuário é
raw_input([prompt]), enquanto input([prompt]) avalia ex-
pressões.
Nonossoprimeiroprograma,vamosusarasfun ções: print(),para
imprimirnatelaofeedback; input(),parapegaraentradadousuário;e
int()e float(),paraconverteroinputde stringpara inte float,
respectivamente.
26
E-book gerado especialmente para 


## Página 43

CasadoCódigo Capítulo3. Manipulaçõesbásicas
Coloque o código a seguir em um arquivo e salve-o como
salario_real.py. Em seguida, execute-o no console python
salario_real.py.
salario = int ( input ( 'Salario? ' ))
imposto = float ( input ( 'Imposto em % (ex: 27.5)? ' ))
print ( "Valor real: {0}" . format(salario - (salario *
(imposto * 0.01 ))))
EssepequenoprogramamostramuitosobrePython:nãotemtiposexplí-
citos,nãoprecisaobrigatoriamentedeumafun ção main–emborasejauma
boapráticateruma–emanipulatiposdiferentesemumaopera çãoaritmé-
tica. Baseando-senesseexemplo,vamosevoluirnossopequenoprograma
introduzindocondicionaiseloops.
3.3 Comparações : maior, menor , igual e outras
EmPython,existem8operadoresdecompara ção.Nesteiníciodolivro,seis
delesserãomuitoimportantes,tendoelesumasemânticasimplesemuito
semelhanteàdeoutraslinguagens.
Osoperadoressão:
•<–menorque;
•<=–menorouigualque;
•>–maiorque;
•>=–maiorouigual;
•==–igual;
•!=–nãoigual.
Ocomportamentodosoperadoresébemintuitivoesegueessalógica
apresentada.Vejaalgunsexemplos:
27
E-book gerado especialmente para 


## Página 44

3.4. Condicionais:if,elif&else CasadoCódigo
>>> 1 >= 1
True
>>> 2 < 1
False
>>> 9 == 9
True
>>> 9 != 8
True
>>> 2 <= 3
True
Objetosdetiposdistintosnuncasãoconsideradosiguais,excetonúmeros.
Osnúmeros,porsuavez,podemsercomparadosentresi,excetopelonúmero
complexo,que,quandocomparadoaoutrotipodenúmero,geraumerrodo
tipo TypeError.Novamente,vamosverexemplos:
>>> 1 == 1.0
True
>>> 10 > 1j
Traceback (most recent call last):
File "<stdin>" , line 1 , in <module>
TypeError : unorderable types: int() > complex()
Instânciasdeclassespodemsercomparadas,masveremosissomaisà
frente. Porenquanto,queremosfazercompara çõescomtiposbásicospara
suprirasnossasnecessidadesiniciais.
3.4 Condicionais: if, elif & else
SeconsiderarmosquegrandepartedaspessoasnoBrasilpagaamesmacota
deimpostos,podemosdizerqueexisteumvalorpadrãoeusá-loseousuário
nãosouberinformarquantopaga. Paraisso,precisamosaplicarum ife
saberseeledeixouoinputvazio. Casotenhadeixado,utilizaremosovalor
padrãodataxa. Casooinputnãoestejavazio,vamosusá-locomovalorda
taxadeimpostodigitadapelousuário.
salario = int ( input ( 'Salario? ' ))
imposto = input ( 'Imposto em % (ex: 27.5)? ' )
28
E-book gerado especialmente para 


## Página 45

CasadoCódigo Capítulo3. Manipulaçõesbásicas
if imposto == '' :
imposto = 27.5
else :
imposto = float (imposto)
print ( "Valor real: {0}" . format(salario - (salario *
(imposto * 0.01 ))))
Afunção input()retornaumastringvaziaseousuárioteclar Enter
semnenhumaentrada.Portanto, impostoteráumvaloriguala ""(string
vazia)eoprimeiroblocoseráexecutado,enquantooblocodo elsenãoserá.
Comandoif
Nateoria,um iféumcomandoqueavaliauma expressãoeescolheum
blocoparaserexecutado,deacordocomoresultadodessaavalia ção.Aex-
pressão,nessecaso,é imposto == " ,tendoumavariávelsendocomparada
comooperadordeigualdade ==comumvalorliteraldeumastringvazia.
Semanticamente,umastringvaziaemumbloco ifequivalea False,assim
comoumalistavazia. Poderíamosmudarotestedo ifanteriorparaalgo
comoocódigoaseguir:
salario = int ( input ( 'Salario? ' ))
imposto = input ( 'Imposto em % (ex: 27.5)? ' )
if not imposto:
imposto = 27.5
else :
imposto = float (imposto)
print ( "Valor real: {0}" . format(salario - (salario *
(imposto * 0.01 ))))
Asexpressõespodemconteroperadoresexplicitamentebooleanosou
não.Comofalamos,emumcomando ifumaexpressãodelistavaziaécon-
sideradocomo False.Noexemploanterior,aexpressão not imposto na
verdadeéomesmoque not "" equeéinterpretadacomoumbooleano,
nocaso, True,jáquenocomando ifumastringvaziaéconsideradocomo
False.
29
E-book gerado especialmente para 


## Página 46

3.4. Condicionais:if,elif&else CasadoCódigo
Indentaçãodosblocosdecódigo
AquiumaoutracaracterísticamarcantedePythonficamuitoclara:ade-
finiçãodoslimitesdoinícioefimdosblocos if, elife elsesãofeitascom
indentação.Semprequeandamos4espa çosparaadireita,seguindoaPEP-
8[9],estamosdefinindoumnovobloco. Jáquandovoltamosos4espa ços,
significaqueaqueleblocoterminou.
Assimcomoemoutraslinguagens,tambémtemosdefinidososoutros
elementoscomo: elife else. O elifavaliaumaoutraexpressãoeé
executadocasoestasejaavaliadacomoverdadeira.Nocasodenenhumaex-
pressãode ifou elifserverdadeira,oblocodo elseéexecutado,se
existir.Reparequeocorpodosblocosdascondicionaisencontra-se4espa-
çosdepoisdocantoesquerdo.
imposto = float ( input ( "Imposto: " ))
if imposto < 10 :
print ( "Medio" )
elif imposto < 27.5 :
print ( "Alto" )
else :
print ( "Muito alto" )
Expressãoif
Tambémexistemasexpressõescondicionais if,chamadosdeoperadores
ternários.Porseremumaexpressão,elestêmumvalorassociadoepodemser
atribuídosavariáveis,diferentedocomando if,quenãotemnenhumvalor
associado.
Vejaoexemplo:
>>> imposto = 0.3
>>> "Alto" if imposto > 0.27 else "Baixo"
'Alto'
>>> imposto = 0.10
>>> "Alto" if imposto > 0.27 else "Baixo"
'Baixo'
>>> valor_imposto = "Alto" if imposto > 0.27 else "Baixo"
>>> valor_imposto
'Baixo'
30
E-book gerado especialmente para 


## Página 47

CasadoCódigo Capítulo3. Manipulaçõesbásicas
3.5 Operadores lógicos
Igualaoutraslinguagens,aquitambémtemosoutrasopera çõesbooleanas
quepodemserusadasnasexpressõesavaliadasemum ifouatémesmoem
atribuições.Elassão: and, ore not.Ouseja,sãoosoperadoreslógicos e,
ouenegação,respectivamente,comfuncionamentomuitosemelhanteaode
outraslinguagens,comoCouJava.
Ambos ande orsãooperadorescomcurtocircuito.Nocasodo and,a
segundaexpressãosóéavaliadacasoaprimeiraseja Truee,nocasodo or,
asegundasóéavaliadacasoaprimeiraseja False.
Oexemploanteriorpoderiasermelhoradocomessesoperadores:
imposto = float ( input ( "Imposto: " ))
if imposto < 10. :
print ( "Baixo" )
elif imposto >= 10. and imposto <= 27. :
print ( "Médio" )
elif imposto > 27. and imposto < 100 :
print ( "Alto" )
else :
print ( "Imposto inválido" )
3.6 Loops com while
Em muitas linguagens, quando vamos implementar loops, usamos o co-
mando while.O whileemPythontambémavaliaumaexpressãoeexecuta
umblocoatéqueestasejaavaliadacomofalsa,tenhaumachamada break
oulevanteumaexce çãosemtratamento.
Vamospermitirquenossoprogramacalculeparaummesmosaláriodi-
versosvalorescomimpostodescontado,utilizandoocomando while.No
primeiroexemplo,vamossaircomaavalia çãodaexpressãoretornandofalso.
salario = int ( input ( 'Salario? ' ))
imposto = 27.
while imposto > 0. :
imposto = input ( 'Imposto ou (0) para sair: ' )
if not imposto:
31
E-book gerado especialmente para 


## Página 48

3.7. Primeiraestruturadedados:lista CasadoCódigo
imposto = 27.
else :
imposto = float (imposto)
print ( "Valor real: {0}" . format(salario - (salario *
(imposto * 0.01 ))))
Olooppodeserinterrompidosemexecu çãodepartedoblococomum
comando break,comopodemosvernoexemploaseguir:
salario = int ( input ( 'Salario? ' ))
imposto = 27.
while imposto > 0 :
imposto = input ( 'Imposto ou (s) para sair: ' )
if not imposto:
imposto = 27.
elif imposto == 's' :
break
else :
imposto = float (imposto)
print ( "Valor real: {0}" . format(salario - (salario *
imposto * 0.01 )))
O whileémuitousadoquandonãosesabepreviamentequandooloop
deveterminar. Porém,emmuitoscasos,queremospercorrercole çõesde
elementos. Obviamente,podemosrealizaressaopera çãocomocomando
while,masemPythonexisteumaformamelhordesefazerisso.
Primeiro,vamosterumpequenocontatocomessascole çõese,depois,
veremoscomorealizamosessetipodeopera çãodepercorrertodoselementos
deumacole ção.
3.7 Primeira estrutura de dados : lista
EmPython,asintaxedalistaémuitoenxuta: [].Ositenssãoseparadospor
,(vírgula),comoem [1, 2, 3] . Listasnãoprecisamterelementosdo
mesmotipo,comoemlinguagensestaticamentetipadas,epodemmisturar
livrementetiposdiferentes,emboranãosejaalgocomum.Algunsexemplos
dedeclaraçõesdelistas:
32
E-book gerado especialmente para 


## Página 49

CasadoCódigo Capítulo3. Manipulaçõesbásicas
>>> [ 1 , 2 , 3 , 4 , 5 ]
[1, 2, 3, 4, 5]
>>> [ "salario" , "imposto" ]
['salario', 'imposto']
>>> [ 1 , "salario" ]
[1, 'salario']
>>> [[ 1 , 2 , 3 ], "salario" , 10 ]
[[1, 2, 3], 'salario', 10]
Listatambéméuma sequênciaemPython,ouseja,podemosperguntar
seutamanhoeacessarelementosporíndiceoutrechos( slices).
Parasaberotamanho,usamos len(lista).Jáparaacessarporíndice,
usamos lista[indice]eportrechos,utilizamosa slice notation,comoem
lista[1:2].Exemplos:
>>> lista = [ 'impostos' , 'salarios' , 'altos' , 'baixos' ]
>>> lista[ 0 ]
'impostos'
>>> lista[ -1 ]
'baixos'
>>> lista[ 2 : 4 ]
['altos', 'baixos']
Listassãomutáveis,logo,podemosrealizaratribui çõesemíndices,ouem
trechos:
>>> lista = [ 'impostos' , 'salarios' , 'altos' , 'baixos' ]
>>> lista[ 2 ] = "Altos"
>>> lista[ 3 ] = "Baixos"
>>> lista
['impostos', 'salarios', 'Altos', 'Baixos']
>>> lista[ 0 : 2 ] = [ "Impostos" , "Salarios" ]
>>> lista
['Impostos', 'Salarios', 'Altos', 'Baixos']
Ifselistas
EmPython,o ifavalialistasvaziascomofalso,eissoémuitoempregado
naprática.Portanto,acostume-se.Vejaumexemploaseguir:
33
E-book gerado especialmente para 


## Página 50

3.8. Looppythônicocomforelistas CasadoCódigo
lista = []
if lista:
print ( "Nunca sou executado" )
else :
print ( "Sempre sou executado" )
3.8 Loop pythônico com for e listas
Percorrerelementosdeumacole çãoéalgoquetodoprogramadorprecisa.
Porém,nemtodasaslinguagenspossuemumaformasimplificadapararea-
lizaressatarefa.Naprograma çãoimperativacomPython,ocomando foré
capazdetornaressatarefatrivial.Dadoonomedeumavariáveleumalista,
o forérealizadodaseguinteforma:
>>> impostos = [ 'MEI' , 'Simples' ]
>>> for imposto in impostos:
... print (imposto)
...
MEI
Simples
Comandoforemdetalhe
O forfaz,paracadaelementodalista,umaatribui çãodoelementocor-
renteàvariáveldefinidanocomando,eexecutaoblocodecódigoassociado
aessavariáveldisponível. Assimcomoo while,eletambémpodeserpa-
radoporum breakouporumaexce çãonãotratada.Umoutrorecursoque
tambémécompatívelcomo whileéapalavrareservada continue.Esse
comandofazcomqueaexecu çãodoblocovádiretoparaapróximaitera ção.
Vejaoexemploparaficarmaisclaro:
>>> impostos = [ 'MEI' , 'Simples' ]
>>> for imposto in impostos:
... if imposto . startswith( "S" ):
... continue
... print (imposto)
...
MEI
34
E-book gerado especialmente para 


## Página 51

CasadoCódigo Capítulo3. Manipulaçõesbásicas
Paraavançarcomo for,vamosanalisaropróximoproblema.Sequiser-
mosimprimirosnúmerosde0até10,poderíamoster:
>>> lista = [ 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]
>>> for i in lista:
... print (i)
...
0
1
2
3
4
5
6
7
8
9
Masesequiséssemosimprimirosnúmerosde0até100?Certamentenão
temosquecriarmanualmenteumalistacomesseselementos.Vamosvermais
elementosquecombinamcomo for.
3.9 Percorrendo interv alos de zero até n com
range ()
Atéomomento,nãovimoscomopercorrerintervalosdezeroatéNcomo
noclássico for(i = 0; i < n; i++) ,queexisteemC,Java,JavaScript
eemmuitasoutraslinguagens.Vamosparaoexemplo:
>>> for i in range ( 5 ):
... print (i)
...
0
1
2
3
4
Vejacomoécuriosooresultadodaavalia çãode range(5):
35
E-book gerado especialmente para 


## Página 52

3.10. Enumerandocoleçõescomforefun çãoenumerate CasadoCódigo
>>> range ( 5 )
range(0, 5)
EmPython3,umobjetoretornadopor range()écompatívelcomo
for,porémnãoéumalista. Esseobjetodotipo rangeéumquechama-
mosdeiterável,definidopelaPEP-234[ 5]. Ouseja,conseguimosdeleum
iteradorqueacadachamadaretornaumvalordiferente,atéqueumaexce ção
StopIterationsejalevantadaeo forterminado.Maisàfrente,aprende-
remosacriarnossosobjetositeráveisquepoderãoserutilizadosjuntocomo
for.
Range no Python 2
NoPython2,afun ção range()retornaumalista,oquetambém
émuitointuitivo,masimplicaemumalistadetamanhoNsercons-
truídaparaserretornada.SeovalorNformuitogrande(porexemplo,
1.000.000),podemserocupados,aproximadamente,31.074MBdeme-
mória.
JánoPython3,afun ção rangeretornaumobjetoiterávelque,por
suavez,retornacadaumdoselementosquefariampartedalista,um
decadavez. Dessaforma,nãoprecisaríamosdeumalistagrandeem
memóriaparaexecutarum forsobre range(1000000).
3.10 Enumerando coleções com for e função
enumerate
Muitasvezes,queremosenumerarelementosdeumacole ção.Ouseja,além
doelemento, queremososeuíndice. Comocomando foreafun ção
enumerate,issotorna-setrivial:
>>> impostos = [ 'MEI' , 'Simples' ]
>>> for i, imposto in enumerate (impostos):
... print (i, imposto)
...
0 MEI
1 Simples
36
E-book gerado especialmente para 


## Página 53

CasadoCódigo Capítulo3. Manipulaçõesbásicas
Ocomando forfuncionacomqualquerobjetodotipo sequência,como
listas,stringsoucomobjetositeráveis,queveremosnasequência.
3.11 Declarando funções : comando def
EmPython,fun çõessãoobjetosdeprimeiraclasse( first class objects),por-
tanto,podemserpassadascomoparâmetros,atribuídasavariáveis,retornar
outrasfunçõese,atémesmo,terematributospróprios.Nestaparteinicialdo
livro,apenasaprenderemosadeclararechamarfun ções. Exploraremosas
outrascaracterísticasmaisàfrente.Agora,oquevamosversãovaria çõesna
declaraçãoechamadadefun ções.
Declaraçõesdefun çãosãofeitasusandoocomando def:
def sum (a, b):
return a + b
c = sum ( 1 , 3 )
Nodiaadia,duasoutrascaracterísticassãomuitocomunsnamanipula-
çãodefun çõeseestãorelacionadasàdeclara çãoechamada.
3.12 Valores padronizados de argumentos
FunçõesemPythonpodemtervalorespadrãoparaseusargumentos. No
nossoexemplo,poderíamoster:
def salario_descontado_imposto (salario, imposto =27. ):
return salario - (salario * imposto * 0.01 )
Essevalorpadrãorefletediretamentenachamada:
>>> salario_descontado_imposto( 5000 )
3650.0
Vejaque,portermosumvalorpadrãoparaumargumento,nãoobriga-
mosousuárioainformarumvalor.Issoévaliosoparaquemescreveafun ção
eparaquemausa.Então,semprequehouverumvalorpadrão,use-o.
37
E-book gerado especialmente para 


## Página 54

3.13. Parâmetrosnomeados CasadoCódigo
Umdetalhemuitoimportanteéqueovalorpadrãodoargumentoéavali-
adonahoradaavaliaçãodadeclaraçãodafun ção,e nãonahoradachamada.
Nãoseesque çadessacaracterística!
3.13 Parâmetros nomeados
EmPython,outracaracterísticadachamadadefun çãosãoosparâmetrosno-
meados.Aprincípio,elessãousadosparamudarosvaloresdosargumentos
comvalorpadrão.
>>> salario_descontado_imposto( 5000 , imposto =0.10 )
4500.0
3.14 Recebendo um número arbitrário de argu -
mentos : packing & unpacking
UmaoutracaracterísticamuitointeressanteemPythonéquepodemoster
funçõesquerecebemnúmerosarbitráriosdeargumentos,posicionaisouno-
meados.Essacaracterísticainfluenciatantonachamadadafun çãoquantono
recebimentodosparâmetros.
Comosuaaplica çãovariamuito,vamosverumexemploparailustrarme-
lhor.
Afunção date(year, month, day) domódulo datetimerecebe
trêsparâmetros.Emalgumasitua ção,poderíamoster,emumatupla,osva-
lores (2014, 10, 1) vindosdealgumaoutrapartedocódigo.Daforma
comoaprendemosatéagora,teríamosquechamá-ladaseguinteforma:
>>> from datetime import date
>>> d = ( 2013 , 3 , 15 )
>>> date(d[ 0 ], d[ 1 ], d[ 2 ])
datetime.date(2013, 3, 15)
Packing
Felizmente,como packing,conseguimostornaressecasomenosverboso
emaiselegante.Alógicaéquesetemosumalistaoutuplacomosvaloresque
38
E-book gerado especialmente para 


## Página 55

CasadoCódigo Capítulo3. Manipulaçõesbásicas
estãonamesmaordemdosparâmetrosqueafun çãorecebe,podemosusaro
packing.
Vejaoexemplo:
>>> from datetime import date
>>> d = ( 2013 , 3 , 15 )
>>> date( * d)
datetime.date(2013, 3, 15)
Oqueaconteceuaquiéquese dateesperaosparâmetros year, month,
dayetemosumalistaoutuplacomosvaloresquecasamessaordem,po-
demosusarasintaxedo *tuplaparasinalizarqueacole çãodevetersuas
posiçõescasadascomparâmetrosrecebidos.
Casoo packingsejasinalizado,masacole çãotenhamaiselementosque
osparâmetrosdafun ção,vamosreceberum TypeError.
O packingtambémvaleparaosparâmetrosnomeados. Muitasvezesé
comumqueosparâmetrosestejamjádisponíveisemumdicionário.Semo
packing,teríamosalgocomo:
>>> def new_user (active = False , admin = False ):
>>> print (active)
>>> print (admin)
>>>
>>> config = { "active" : False ,
>>> "admin" : True }
>>>
>>> new_user(config . get( 'active' ), config . get( 'admin' ))
False
True
Novamente,queremosalgomaisenxutoeelegante.Podemosusaro pac-
kingcomosparâmetrosnomeados:
>>> def new_user (active = False , admin = False ):
>>> print (active)
>>> print (admin)
>>>
>>> config = { "active" : False ,
39
E-book gerado especialmente para 


## Página 56

3.14. Recebendoumnúmeroarbitráriodeargumentos:packing&unpacking CasadoCódigo
>>> "admin" : True }
>>>
>>> new_user( ** config)
False
True
Nessecaso,asintaxeé **dicionário. Ointerpretadorautomatica-
mentecasaositensdodicionáriocomosparâmetrosnomeadosdafun ção
new_user.
Unpackingdosargumentos
O unpackingéoprocessoqueéexecutadodentrodafun ção,enãona
chamada.Podemosusarasintaxe *argsou **kwargscomoargumentos
parao unpackingdosparâmetrosposicionaisounomeados.
>>> def unpacking_experiment ( * args):
... arg1 = args[ 0 ]
... arg2 = args[ 1 ]
... others = args[ 2 :]
... print (arg1)
... print (arg2)
... print (others)
...
>>> unpacking_experiment( 1 , 2 , 3 , 4 , 5 , 6 )
1
2
( 3 , 4 , 5 , 6 )
Comoaassinaturadafun çãousa *args,dopontodevistadochamador
(ou caller),elapodereceberumnúmeroarbitráriodeparâmetros,comono
exemploanterior.
Omesmoaplica-seaosparâmetrosnomeados.Seusarmos **kwargs,o
chamadorpodepassarquaisquerparâmetrosnomeadosquepodemacessar
kwargscomoumdicionárioeobterosvalores.Vejaoexemplo:
>>> def unpacking_experiment ( ** kwargs):
... print (kwargs)
...
40
E-book gerado especialmente para 


## Página 57

CasadoCódigo Capítulo3. Manipulaçõesbásicas
>>> unpacking_experiment(named = "Test" , other = "Other" )
{ 'other' : 'Other' , 'named' : 'Test' }
Essesrecursossãomuitopoderososepodemajudaremsitua çõesespecí-
ficas,masnãosãotãoincomuns.Nocapítulo 8,teremosumempregorealdo
packing.
3.15 Usando código já pronto : importando mó -
dulos
Umaoutramanipula çãobásicaéaimporta çãodemódulos. Porenquanto,
vamosaprenderapenascomoimportareusarosmódulos. Maisàfrente,
aprenderemoscomocriarosnossosmódulos.
APEP-8[ 9]temrecomenda çõessobrecomoestruturarocódigodeim-
portação,comousarordemalfabética,porexemplo.Nestemomentodolivro,
omaisimportanteé como importare como usarocódigoimportado.
Ocomando importpodeimportarmódulosouobjetos(classesefun-
ções)paraoescopodeexecu çãodocódigoqueoexecuta.Quandofazemos
isso,incluímosonomeusadonaimporta çãonalistadenomesdisponíveis.
Vejaoexemplo:
import math
print (math . sqrt( 9 ))
Nesseexemplo,importamosomódulo math.Logo,nocontextodeexe-
cuçãodocódigo,onome mathéareferênciaparaomódulo.Atépodemos
atribuirumvalorpara math,entretantoperderíamosareferênciaparaomó-
dulo.Vejaoexemplo:
import math
math = 10
print (math . sqrt( 9 ))
Traceback (most recent call last):
File "03_09_error.py" , line 3 , in < module >
print (math . sqrt( 9 ))
AttributeError : 'int' object has no attribute 'sqrt'
41
E-book gerado especialmente para 


## Página 58

3.16. Conclusão CasadoCódigo
Épossívelcriarum aliasparaummóduloouumobjetoimportado,se
quisermosusaroutronome.Vejaoexemplo:
import math as matematica
print (matematica . sqrt( 9 ))
Umoutrocasodeusoéimportarapenasumobjetoespecíficodeummó-
dulo. Tambéméumapráticamuitocomum. Nessecaso,utilizamosoco-
mando from/import,sinalizandono fromomódulo,edepoisdo import,
informamosqueobjetoqueremosimportar.Vejaoexemplo:
from unittest import TestCase
from unittest import mock
Podemosusarorecursodo aliascomo from/importtambém:
>>> from math import log2 as l2
>>> print (l2( 1024 ))
10.0
Agora,fechamosasmanipula çõesbásicasdeimporta ção,quejánosper-
mitemusarmódulosdeterceirosoudaprópriabibliotecapadrão.
3.16 Conclusão
Nestecapítulo,aprendemossobrecondicionaisusandoocomando if,como
declararlistasdeobjetosPythoncomoscolchetes []edoistiposdecoman-
dosdeloop, whilee for.Vimostambémcomopodemosinterromperesses
loopscomexce çõesouusandoocomando break,ecomopodemosutilizar
loopscomobjetositeráveis,porexemplonocasodoobjetoretornadopela
função range().
Descobrimoscomocombinar fore range()paragerarumloopde
inteirosemsequência,porexemplo for(i = 0; i < n; i++) ,obásico
dousodemódulosfoicobertocomocomando importealgumasvaria-
çõesforamexplicadas. Tambémaprendemosumpoucosobreousobásico
defunçõesealgumasdesuascaracterísticas,como packinge unpacking. A
partirdeagora,vamoscriarumasériedepequenosprogramasparamotivar
econtextualizarmelhorosrecursosdalinguagemPython.
42
E-book gerado especialmente para 


## Página 59

Capítulo4
Primeiroprograma:downloadde
dadosdaCopa2014
4.1 Criando uma função para download na web
Onossoprimeiroprogramaconsistebasicamenteemduasfun çõesdedown-
loaddedados.Umadelaslevaemcontaqueoservidorrespondeotamanho
dabasecujodownloadqueremosfazer,eaoutratrataquandooservidornão
informaotamanho. EssedownloadéfeitoviaprotocoloHTTP,usandore-
cursosdaprópriabibliotecapadrão.
Comosabemosqueexistemessasduassitua ções,podemosiniciarimagi-
nandoumafun çãoquetratacadacasoedepoiscombiná-las.Assim,teremos
umprogramaquefuncionaemqualquerumdoscasosdescritos.
E-book gerado especialmente para 


## Página 60

4.1. Criandoumafunçãoparadownloadnaweb CasadoCódigo
Downloaddearquivodetamanhoconhecido
Vamosconsiderarqueoservidornosinformouotamanhoembytesdo
arquivododownloadnocabe çalhodarequisi ção.Vamosverocódigo,para
entãodiscutirosdetalhes.
BUFF_SIZE = 1024
def download_length (response, output, length):
times = length / BUFF_SIZE
if length % BUFF_SIZE > 0 :
times += 1
for time in range (times):
output . write(response . read(BUFF_SIZE))
print ( "Downloaded %d" % (((time * BUFF_SIZE) / length) *100 ))
O responserepresentaumarespostadoservidor,sendodelaquelere-
mososbytesdoarquivodedownload.Comosabemosotamanho,consegui-
mossaberquantasopera çõesde response.read()vamosterquerealizar
paralertudo.Paracadaleitura,realizamosum output.write()dosbytes
lidosemumarquivo.
Nesseexemplo,exploramostodososconceitosbásicosqueforamintro-
duzidosatéaqui:definiçãodefun ção,atribuiçãodevariáveis,opera çõesarit-
méticas,chamadasdefunções,formata çãodestringseumloopcom range.
Agora,vamosveraoutrafun çãodedownloade,emseguida,afun ção
quedisparaumadelas,paracriaronossoprimeiroprogramacompleto.
Criandooutrafun çãoparadownloadnaweb
Comoditoanteriormente,àsvezesoservidornãorespondeotamanho
embytesdoarquivoquequeremos.Nessescasos,realizamosleiturasatéque
algumanãoretornenenhumbyte.Basicamente,trocamosoloopcom for
e range()porumloopcom while,vistoquenãoconseguimossaberde
antemãoquandoterminar. Quandoaleituranãoretornanada,ocomando
breakinterrompeo while.
def download (response, output):
total_downloaded = 0
while True :
44
E-book gerado especialmente para 


## Página 61

CasadoCódigo Capítulo4. Primeiroprograma:downloaddedadosdaCopa2014
data = response . read(BUFF_SIZE)
total_downloaded += len (data)
if not data:
break
output . write(data)
print ( 'Downloaded {bytes}' . format( bytes = total_downloaded))
Agoraquejáconhecemosasduasfun ções,veremosafun çãoqueescolhe
chamarumadasduas.
4.2 Primeiro programa completo
Oqueinicialmentefoiomitido:importa çõesdemóduloseafun ção main,
queseráchamadaquandooprogramaforexecutado.Emmuitaslinguagens,
oiníciodosarquivoscontémtudooqueéimportadodeoutrosmódulos.
# coding: utf-8
import io
import sys
import urllib.request as request
Intuitivamente,ficamuitoclaraaimporta çãodosmódulos ioe sys.A
últimalinhaéum importcomalteraçãono namespacelocal:estamosimpor-
tando urllib.requestecolocandononomelocal request.Seaparte
as request fosseomitida,parausaroobjeto request,teríamosquees-
crever urllib.requesttodasasvezes.Aquiadecisãoésempredeacordo
comocontexto.Algumasvezes,queremosexplicitartodososmomentosem
queestamosusandoumafun çãoouobjetoqueédeoutromódulo,eoutras
queremoslimparocódigodequalquerinforma çãoredundante.Aescolhaé
sua!
Agora, vamosoficialmenteaprenderoqueseriaemPythonafun ção
maindeoutraslinguagens,comoCouJava.
4.3 Definindo funções main
EmPython,quandochamamosointerpretadorpassandoumarquivo .py
comoparâmetro,opadrãoéquetodasaslinhasdoarquivosejamavalia-
45
E-book gerado especialmente para 


## Página 62

4.3. Definindofunçõesmain CasadoCódigo
das/executadas. Odetalheéquetodocódigodeescopoglobalemummó-
dulotambémseráexecutadoquandoforimportado. Oproblema,então,é:
comosabemosseummódulofoiaquelepassadocomoparâmetronalinha
decomando?
Bastatestarovalordeumavariávelglobal.Seotestedo ifaseguirfor
verdadeiro,éporqueessemódulo(queestáfazendoesseteste)foiochamado
pelalinhadecomando.Ébemcomumalgocomo:
def main ():
print ( "Olá" )
if __name__ == "__main__" :
main()
Nesseexemplo, mainsóéexecutadaquandoessemóduloéoutilizadona
linhadecomando.Quandoeleéimportado,afun ção mainnãoéexecutada.
Voltandoaonossoexemplo,nossa main:
def main ():
response = request . urlopen(sys . argv[ 1 ])
out_file = io . FileIO( "saida.zip" , mode = "w" )
content_length = response . getheader( 'Content-Length' )
if content_length:
length = int (content_length)
download_length(response, out_file, length)
else :
download(response, out_file)
response . close()
out_file . close()
print ( "Finished" )
if __name__ == "__main__" :
main()
Oquetemosagoraéum scriptquefazodownloaddeumarquivo ZIP.De
acordocomarespostadoservidor,eleoptaporumadeterminadaestratégia
paradownloaddoarquivo.
46
E-book gerado especialmente para 


## Página 63

CasadoCódigo Capítulo4. Primeiroprograma:downloaddedadosdaCopa2014
Utilizamosafun çãodabibliotecapadrão urllib.request.urlopen,
aclasse io.FileIOparaescrevermosoarquivobináriodesaída,umco-
mando ifealgumaschamadasdefun ções.Asfun çõescontêmum while,
um forealgumasoutrasopera çõesjámencionadas. Notequecomesses
poucosconceitosjáconseguimosconstruirumprogramaquerealizaumata-
refacompleta.
Vejaonossoprimeiroprograma,quefazodownloaddosarquivosde
dadosqueusaremosdaquiemdiante:
# coding: utf-8
import io
import sys
import urllib.request as request
BUFF_SIZE = 1024
def download_length (response, output, length):
times = length // BUFF_SIZE
if length % BUFF_SIZE > 0 :
times += 1
for time in range (times):
output . write(response . read(BUFF_SIZE))
print ( "Downloaded %d" % (((time * BUFF_SIZE) / length) *100 ))
def download (response, output):
total_downloaded = 0
while True :
data = response . read(BUFF_SIZE)
total_downloaded += len (data)
if not data:
break
out_file . write(data)
print ( 'Downloaded {bytes}' . format( bytes = total_downloaded))
47
E-book gerado especialmente para 


## Página 64

4.4. Realizandoodownload CasadoCódigo
def main ():
response = request . urlopen(sys . argv[ 1 ])
out_file = io . FileIO( "saida.zip" , mode = "w" )
content_length = response . getheader( 'Content-Length' )
if content_length:
length = int (content_length)
download_length(response, out_file, length)
else :
download(response, out_file)
response . close()
out_file . close()
print ( "Finished" )
if __name__ == "__main__" :
main()
4.4 Realizando o download
Parafacilitar,criamosumarquivobaseadonosdadosoriginais,mascomal-
gumassimplificações(semtodasastabelas)esemalgunsdados“sujos”que
poderiamtrazerproblemasaorodarosexemplos.
Todososexemplosfuncionarãoperfeitamentecomonossoconjuntode
arquivos.Comosdadosoriginais,algunsexemplospodemprecisardealte-
rações,especialmentedetratamentodeerro. AURLdosnossosarquivosé
http://livropython.com.br/dados.zip.
Todososexemplosdolivrovãofuncionarcomanossaversãodosar-
quivosdedados,jáqueosarquivosoriginaispodemterproblemasdeforma-
taçãodifíceisdecontornar.
Sevocêquiserosdadosoriginais,vocêconsegueencontrá-lonopróprio
sitedoPortaldaTransparência[ 1]. Sevocêconcluirtodasasetapasdoli-
vro,podeaventurar-secomosdadosoriginais,queserãoumanovafontede
desafios,umavezquediversosproblemaspoderãoserencontradosaotentar
explorarosdadosoriginais.
48
E-book gerado especialmente para 


## Página 65

CasadoCódigo Capítulo4. Primeiroprograma:downloaddedadosdaCopa2014
Paraobteronossoarquivodedadosusandoonossoprograma,crieum
arquivochamado download_dados_copa.pycomocódigo-fonteanterior
eexecutealinhadecomando:
$ python download_dados_copa.py
http://livropython.com.br/dados.zip
Agora,naraizdoprojetotemosoarquivo saida.zip,quefoiescrito
pelonossoprogramaapartirdarespostadarequisi ção.
Essatarefaépartedeumaaplica çãomaior,queautomatizaoprocessode
extraçãodosdadosdabasededadosdosgastoscomacopade2014nabase
doPortaldaTransparência[1].
Repareque,mesmonesseprogramarelativamentecomplexo,usamosso-
menteconceitosexibibosatéagora.
Vamoscontinuarcomasoutrasetapasdesteprocesso.
4.5 Mais do básico: extraindo arquivos de da -
dos e metadados
Antesdeseguirmosparaopróximotópico,vamosnosexercitarumpouco
maiscomoquevimosatéagora:fun ções,variáveis,condicionais,loops,con-
diçõesdeparadaeousodealgunsobjetosimportadosdeoutrosmódulosda
bibliotecapadrão.
Emvezdeutilizarumprogramapadrãoparaextrairoconteúdodoar-
quivo ZIPbaixado, vamos criar um novo programa que usa o módulo
zipfileparaessatarefa.
Notequefaremosumtratamentodeerrobemsimplescasooarquivopas-
sadocomoparâmetronãoexista.Novamente,veremosapenasousodecon-
ceitosquejáexibidospelomenosumavez,mesmoquesemmuitosdetalhes:
# coding: utf-8
import os
import zipfile
import sys
49
E-book gerado especialmente para 


## Página 66

4.5. Maisdobásico:extraindoarquivosdedadosemetadados CasadoCódigo
def main (path):
if not os . path . exists(path):
print ( "Arquivo {} não existe" . format(path))
sys . exit( -1 )
else :
zfile = zipfile . ZipFile(path)
zfile . extractall()
print ( "Arquivos extraídos" )
if __name__ == "__main__" :
main(sys . argv[ 1 ])
Vamosveroscript extrai_zip.pyinteiroeanalisarcadaparteindivi-
dualmente.Inicialmente,vemosadeclara çãodo encoding–éumaboaprática
sempretere,sevocêusatextocomacentosnasuadocumenta ção,éobriga-
tóriodefinirquasesempre utf-8.
Importamosapenas3módulos: sys, ose zipfile. Comomódulo
sys,pegamosoargumentodalinhadecomando–nessecaso,ocaminho
doarquivobaixado–etambémpodemosencerraraexecu çãodonossopro-
gramacom sys.exit(return_code). Usamosocódigoderetorno -1
porqueoarquivopassadonãoexiste.Paratestaraexistênciadoarquivo,usa-
mos os.path.exists(path).Essafun çãoretorna Truecasoocaminho
passadoexista,e Falsecasonão.
Existindo,vamosusaromódulo zipfileparacriarumobjetodaclasse
ZipFilequepossuiométodo extractall. Esteextraitodooconteúdo
doarquivo zipparaodiretóriodetrabalho.
Compoucaslinhas,ealgunsconceitoseconstrutosiniciais,criamosdois
programas: umdelesfazodownloaddeumarquivo zipdeumservidor
HTTPeooutroextraioconteúdodoarquivoparaodiretóriocorrente,para
queospróximosprogramaspossamusá-lo.
50
E-book gerado especialmente para 


## Página 67

CasadoCódigo Capítulo4. Primeiroprograma:downloaddedadosdaCopa2014
4.6 C onclusão
Assim,terminamosaprimeirapartedonossoprocesso.Vejanovamenteque
utilizamosapenasfun çõesestrings,importamosalgunsmóduloseexecuta-
mosalgunscomandos. Ouseja,tudooquevimos,mesmoquesuperficial-
mente,atéagora.
Éclaroquemuitacoisapoderiaserfeitadeoutraforma,masaideiadesses
scriptsiniciaiséseromaissimplespossível.
Nospróximoscapítulos,falaremosmaisdeestruturasdedadosecomo
vamosusá-lasparaalcançarnossoobjetivomaior.
51
E-book gerado especialmente para 


## Página 68

E-book gerado especialmente para 


## Página 69

Capítulo5
Estruturasdedados
5.1 Montando um modelo conceitual usando es -
truturas de dados
Oobjetivodonossoprogramaérealizarconsultasempartedosdadosdos
gastospúblicosdaCopa2014. Osarquivosdisponibilizadosdividem-seem
doistipos:metadadosedados.Os dadossãocomosefossemaslinhasdeum
bancodedados,enquantoos metadadosseriamadefini çãodascolunasde
umatabeladeumbancodedados,ouseja,nadamaissãodoqueadescri ção
dosdados.Vamosutilizarosmetadadoscomosuportepararealizarconsultas
nosdados.
Depoisdasetapasanteriores,agoratemosumapastaquecontémumar-
quivodemetadadosparacadaentidadedomodelodedados,eoutrapasta
comosdadosemsi. Oquequeremoséquenossoprogramasejacapazde
E-book gerado especialmente para 


## Página 70

5.1. Montandoummodeloconceitualusandoestruturasdedados CasadoCódigo
abrirtodosessesarquivoseinterpretaroconteúdodeformaadequada.Va-
mosveroconteúdodeumdosarquivosdemetadados:
IdInstituicao bigint Identificador da instituição-PK.
IdTipoInstituicao bigint Identificador do tipo de instituição ...
NomInstituicao varchar Nome da instituição.
NumCnpj varchar Número do CNPJ.
Existem3“colunas”nessearquivo: onomedocampo(porexemplo,
IdInstituicao),otipodocampo(porexemplo, bigint),eadescri ção.
Cadalinhadessearquivorefere-seaumainforma çãodeumalinhanoarquivo
dedados.Nesseexemplo,portanto,podemosesperarqueoarquivodedados
daentidade Instituição tenha4valoresseparadospelocaractere ;(pontoe
vírgula).
Vejaumtrechodoarquivodedados Instituicao.csv:
1;1;"Caixa Econômica Federal";"00360305000104"
2;1;"BNDES";"33657248000189"
8;3;"GOVERNO DO ESTADO DE MINAS GERAIS";"96313723000117"
12;5;"GOVERNO DO DISTRITO FEDERAL";"00394692000108"
105;6;"Concessionário";"72036339000159"
106;1;"BNB";"07237373000120"
107;2;"INFRAERO";"00352294000110"
Assimcomodescritonoarquivodemetadadosde Instituição,cadalinha
contém4informaçõessobreaentidadeàqualoarquivofazreferência. O
nossoprogramaconseguirálerosarquivosde4tiposdistintosdeentidades
e,posteriormente,cruzardadosparapermitirconsultasmaiscompletasein-
teressantes.
Parainiciaresseprocesso,primeiroprecisamosdeumaformadeencon-
trarosmetadadosdeumaentidadedadaa stringcomoseunome.Para
isso,usaremosum Dicionário. Essedicionáriodemetadados,queserácri-
adoapartirdaleituradosarquivos,seráumdospontoscentraisdonosso
aplicativo.
54
E-book gerado especialmente para 


## Página 71

CasadoCódigo Capítulo5. Estruturasdedados
5.2 Dicionários: fundação da linguagem
O dicionário,tambémmuitoconhecidocomo mapaou array associativo,é
umconceitoabstratodeestruturadedados[ 12],noqualtemosNentradas
associadasaumaoumaischavesporentrada.EmPython,ofamoso dict
éumadasestruturasdedadosmaisutilizadas.Inclusive,muitosrecursosda
próprialinguagemtêmimplementaçõesqueusamdicionários.
Nos dicts,aschavesdevemserimutáveiseosvalorespodemserqual-
querobjeto. Eleéinstanciadousandoasintaxe {},ouafun ção dict().
Vejaunsexemplos:
entidades = {
'Instituicao' : []
}
Tambémpodemosusar:
entidades = dict (Instituicao = [])
Ouseja,háduasformasderealizaramesmatarefa:usandoasintaxeli-
teral,ouusandoafun ção dict(). Tambémpodemosadicionaritensao
dicionárioapóscriado,comonoexemploaseguir:
entidades = dict ()
entidades[ "Instituicao" ] = []
Damesmamaneiraquepodemosatribuirvaloresparachaves,podemos
tambémremoverosvaloresusandoocomando del,noelementoqueque-
remosremoverdodicionário.
>>> entidades = dict ()
>>> entidades[ 'Empreendimento' ] = "EntidadeEmpreendimento"
>>> print (entidades)
{'Empreendimento': 'EntidadeEmpreendimento'}
>>> del entidades[ 'Empreendimento' ]
>>> print (entidades[ 'Empreendimento' ])
Traceback (most recent call last):
File "<stdin>" , line 1 , in <module>
KeyError : 'Empreendimento'
55
E-book gerado especialmente para 


## Página 72

5.3. Montandoodicionáriodemetadados CasadoCódigo
Oquequeremosagoraécriarumdicionário,noqualaschavessãoos
nomesdasentidadeseosvaloressejamlistas.Essaslistascontêmoscampos
comnome,tipoedescri çãoquecompõedecadaatributodaentidade. No
finaldessaetapa,queremosteralgoparecidocomoobjetoaseguir:
entidades = {
'Instituicao' : [
( 'IdInstituicao' , 'bigint' ,
'Identificador da instituição-PK' ),
( 'IdTipoInstituicao' , 'bigint' ,
'Id do tipo de instituição' ),
( 'NomInstituicao' , 'varchar' , 'Nome da instituição' ),
( 'NumCnpj' , 'varchar' , 'Número do CNPJ' )
]
}
Oquetemoséumdicionáriocomchavesdotipo stringevaloresdo
tipo list.Aslistas,porsuavez,sãodotipo tupleecontêm3elementos
cada. Paracadaumdosarquivosdemetadados,teremosumaentradano
dicionárioentidadescomalistadeatributosqueaquelaentidadecontém.
Aseguir,vamosvercomomontaressedicionário,quetempapelimportante
nosexemplosquevirãoaseguirnolivro.
5.3 Montando o dicionário de metadados
Estácomdúvidassobrecomomontaressedicionário?Nãosepreocupe.
Sevocêcriouerodouosdoisprogramascompletosquepassamosaté
então,oquevocêtemdisponívelagorasão2pastas. Umadessaschama-se
meta-dataecontém4arquivostextocomosmetadadosquenosinteres-
sam.
Sevocêquiser,tambémpodemosobterosdadosqueserãousadosapartir
daquiporaqueleendere çocomosarquivosdolivro, http://livropython.com.
br/dados.zip. Bastadescompactaroarquivo ZIPemumdiretórioerodar
todososexemplosnessediretório.
Poderíamos,simplesmente,criaremcódigoodicionárioquecontémas
mesmasinformaçõesqueessesarquivos.Comoissopodeserumpoucotra-
balhoso,vamoscriarumnovoprogramaquelistaosarquivosdessapasta,
56
E-book gerado especialmente para 


## Página 73

CasadoCódigo Capítulo5. Estruturasdedados
abreumdecadavezemontaaslistasdeatributos,baseando-senoconteúdo
dosarquivos.
Noparágrafoanterior,listamostrêstarefas.Vamosverexemplossepara-
dosdecomorealizarcadaumadelasedepoiscriarumnovoprograma.
Listandoarquivosdeumapasta
Paralistararquivosdeumapasta,podemosusarafun ção listdir()
domódulo os.Elaretornaumalistadearquivos,portanto,podeserusada
comocomando for.Vejaoexemplo:
>>> import os
>>> for meta_file in os . listdir( 'data/meta-data' ):
... print (meta_file)
...
Empreendimento.txt
ExecucaoFinanceira.txt
Instituicao.txt
Licitacao.txt
Agoraquelistamososarquivos, precisamosextrairaextensão .txt
paraobteronomedasentidadescomquevamostrabalhar. Vimosafun-
ção split()doobjeto string,quepodeserusadaparaessatarefa. Ela
tambémretornaumalista,logo,parapegaraprimeiraparte,usamosoin-
dexador filename.split(‘.’)[0]parapegaroelementonaposi ção 0.
Vejaoexemplo:
>>> def extract_entity_name (filename):
... return filename . split( '.' )[ 0 ]
...
>>> extract_entity_name( 'Licitacao.txt' )
'Licitacao'
Nessecódigo,obtemosonomedaentidadepormeiodonomedoar-
quivotextoassociado. Porexemplo, Licitacao.txttransforma-seem
Licitacao.Osnomesserãoaschavesdodicionárioeosvaloresserãouma
listadetuplas(queveremoslogoaseguir)quedescrevemoscamposdaenti-
dade.
57
E-book gerado especialmente para 


## Página 74

5.4. Adicionandoeremovendoelementosemumalista CasadoCódigo
5.4 Adicionando e removendo elementos em
uma lista
Comoquevimos,jápoderíamoscriarumdicionáriocomaschaves,massem
alistadeatributosquequeremos. Comoosarquivosdemetadadossãopa-
dronizados,podemoscriarumprogramaquefuncioneparatodosquesigam
ospadrõesdefinidos.
Noiníciodocapítulo,vimosqueoconteúdodeumarquivodemetadados
podeseralgocomo:
IdInstituicao bigint Identificador da instituição-PK.
IdTipoInstituicao bigint Identificador do tipo de instituição ...
NomInstituicao varchar Nome da instituição.
NumCnpj varchar Número do CNPJ.
Cadalinhatem3elementosseparadospelocaractere \t( tab).Vamos
vercomopoderiaserumafun ção,querecebeumcaminhoparaumarquivo
demetadadoseretornaumalistadetuplas,comodesejamos.Paraadicionar
umatuplanalistadeatributos,usaremosométodo append().Ométodo
appendadicionaumnovoelementonofinaldalista.
>>> def read_meta_data (path):
... data = open (path, "rt" )
... meta_data = []
... for line in data:
... line_data = line . split( '\t' )
... meta_data . append((line_data[ 0 ],
... line_data[ 1 ],
... line_data[ 2 ]))
... data . close()
... return meta_data
...
>>> read_meta_data( 'data/meta-data/Instituicao.txt' )
[('IdInstituicao', 'bigint', 'Identificador da instituição-PK.'),
('IdTipoInstituicao', 'bigint', 'Identificador do tipo de
instituição associada à instituição.'), ('NomInstituicao',
'varchar', 'Nome da instituição.'), ('NumCnpj', 'varchar',
'Número do CNPJ.')]
58
E-book gerado especialmente para 


## Página 75

CasadoCódigo Capítulo5. Estruturasdedados
Poderíamosterusadotambémométodo insert(i, o),emque ié
aposiçãoondequeremosadicionarumobjeto,e oéoobjetoquequeremos
adicionar.
Pararemoverobjetos, poderíamosusarosmétodos remove(obj)e
pop(i). Ométodo remove(obj)remove objdalista,jáo pop([i])
removeoelementonaposi ção ieoretorna. Se inãoforespecificado,o
últimoelementoéremovidoeretornado.
Outrasoperaçõesdelistassão:
•reverse()–inverteraordemdoselementos;
•sort()–ordenarporvalor;
•extend(lista)–concatenarcomoutralista;
•index(elemento)–descobriraposiçãodeumelemento;
•clear()–apagartodososelementosdalista.
Vejaalgunsexemplosdeuso:
>>> lista = [ 1 , 2 , 3 , 4 , 5 ]
>>> lista . append( 6 )
>>> lista
[1, 2, 3, 4, 5, 6]
>>> lista . insert( 0 , -1 )
>>> lista
[-1, 1, 2, 3, 4, 5, 6]
>>> lista . remove( 6 )
>>> lista
[-1, 1, 2, 3, 4, 5]
>>> lista . pop( 0 )
-1
>>> lista
[1, 2, 3, 4, 5]
>>> lista . reverse()
>>> lista
[5, 4, 3, 2, 1]
>>> lista . sort()
59
E-book gerado especialmente para 


## Página 76

5.5. Iterandodicionários:vendovaloresechaves CasadoCódigo
>>> lista
[1, 2, 3, 4, 5]
>>> lista . index( 5 )
4
>>> lista_b = [ 6 , 7 , 8 ]
>>> lista . extend(lista_b)
>>> lista
[1, 2, 3, 4, 5, 6, 7, 8]
>>> lista . clear()
>>> lista
[]
5.5 Iterando dicionários: vendo v alores e cha-
ves
Em Python, temos uma forma simples de iterar pela duplachave
-> valor de um dicionário. Podemos usar for key, value in
data.items(): ... e,acadaexecu çãodoblocodo for,teremosem key
oobjetochaveeem valueoobjetovalordaquelaentrada.Issoaconteceno
finaldoprograma:
import os
def extract_name (name):
return name . split( "." )[ 0 ]
def read_lines (filename):
_file = open (os . path . join( "data/meta-data" , filename), "rt" )
data = _file . read() . split( "\n" )
_file . close()
return data
def read_metadata (filename):
metadata = []
for column in read_lines(filename):
60
E-book gerado especialmente para 


## Página 77

CasadoCódigo Capítulo5. Estruturasdedados
if column:
values = column . split( '\t' )
nome = values[ 0 ]
tipo = values[ 1 ]
desc = values[ 2 ]
metadata . append((nome, tipo, desc))
return metadata
def main ():
meta = {}
for meta_data_file in os . listdir( "data/meta-data" ):
table_name = extract_name(meta_data_file)
meta[table_name] = read_metadata(meta_data_file)
for key, val in meta . items():
print ( "Entidade {}" . format(key))
print ( "Attributes: " )
for col in val:
print ( " {}: {}" . format(col[ 1 ], col[ 0 ]))
if __name__ == "__main__" :
main()
Nesseprograma,achaveésempreuma stringquecorrespondeao
nomedaentidade,eovaloréalistadeatributos. Comoosatributosestão
emumalista,sabemosquepodemosusá-lanocomando fore,assim,per-
corrercadaatributo.
Primeiro,listamososarquivosdapastademeta-dados.Paracadanome
dearquivo,extraímosonomedaentidade.Depois,abrimoscadaumdosar-
quivosdemetadadoseretiramosasinforma çõesdaslinhasdoarquivo.Cada
linhatemainforma çãodeumatributo(oucoluna)daentidade(outabela)
comnome,tipoedescri ção.
Nofinal,iteramosumdicionáriocomocomando for,eescrevemosna
saídaonomedaentidadeeosdetalhesdosatributos.Vejaumapartedasaída
quevocêveráaoexecutaressecódigo:
61
E-book gerado especialmente para 


## Página 78

5.6. Tuplas:sequênciasimutáveis CasadoCódigo
Entidade Instituicao
Atributos:
bigint: IdInstituicao
bigint: IdTipoInstituicao
varchar: NomInstituicao
varchar: NumCnpj
5.6 Tuplas: sequências imutáveis
Noexemploanterior,cadaentidadeérepresentadaporumalistadetuplas.As
tuplas,umavezcriadas,nãopodemsermudadas:sãoimutáveis. Nonosso
caso,cadatuplaarespeitodeumacolunasempreterá3elementos: nome,
tipoedescri ção. Alémdisso,inicialmente,nãovamosconsiderartrocasde
metadados,atéporqueosdadosjáestãoprontosenãovãomudar.
Tuplastambémsãoamplamenteusadasnaimplementa çãoderecursosda
linguagemPython.Alémdeseremusadascomocole çõesimutáveis,também
sãomuitoutilizadascomoagrupadoresdeelementosheterogêneos,comoo
structdeC.
Assimcomolistasedicionários,tuplassãosequências.Então,podemos
acessarelementospeloíndice,saberseutamanhoeseumelementoestáden-
trodelaounão.Vamosveralgunsexemplos:
>>> meta_dado = ( 'IdTipoAlerta' , 'bigint' ,
'Identificador do tipo alerta-PK.')
>>> 'IdTipoAlerta' in meta_dado
True
>>> len (meta_dado)
3
>>> meta_dado[ 0 ]
'IdTipoAlerta'
>>> impostos[ 0 ] = 'OutroValor'
Traceback (most recent call last):
File "<stdin>" , line 1 , in <module>
TypeError : 'tuple' object does not support item assignment
Agora,jácompreendemosoempregodo Dicionárioeda Tuplanonosso
programa.Opróximoobjetivoédetectarrelacionamentosautomaticamente,
analisandoosmetadadosquerepresentamos.
62
E-book gerado especialmente para 


## Página 79

CasadoCódigo Capítulo5. Estruturasdedados
5.7 Explorando os dados que coletamos
Nessemomento,oquetemos,precisamente,éumdicionáriodelistasdetu-
plas. Apesardeparecercomplexo,onossomodeloébemsimples. Vamos
aprendermaisalgunsmétodosparaexploraranossaestruturaeconhecer
melhoroquemontamos.
Primeiro,vamosdescobrirqueentidadescompõemessabasededados.
Umaformasimplesdeverissoseriaadaptarnossopenúltimocódigopara
imprimirsomenteonomedasentidades:
import os
def main ():
meta = {}
for meta_data_file in os . listdir( "data/meta-data" ):
table_name = meta_data_file . split( '.' )[ 0 ]
print (table_name)
if __name__ == "__main__" :
main()
Easaídaseria:
Empreendimento
ExecucaoFinanceira
Instituicao
Licitacao
Comojásabemosasentidadeseosatributos,podemosbuscarporrela-
çõesentreentidadesautomaticamente.Nocontextodosnossosdados,uma
relaçãoéquandoexiste,emalgumaentidade,umatributoqueapontapara
umelementodeoutraentidade.
Sabemosquecadaentidadetemumatributoidentificador.Portanto,va-
mosprocuraremcadaentidadeumatributoidentificadordeoutraentidade.
Quandoacharmosalgum,encontramosumarela ção.
Openúltimoexemplocriaumdicionáriodeentidades,noqualosvalores
sãolistasdetuplas.Oprimeiroelementodecadalistaéachaveidentificadora
daentidade.
63
E-book gerado especialmente para 


## Página 80

5.7. Explorandoosdadosquecoletamos CasadoCódigo
Paradescobrirasrela ções,primeirotemosqueacharaschavesidentifi-
cadorasdecadaentidade. Vamos,então,criarumdicionárioqueaschaves
sãoas stringsquerepresentamosnomes,eosvaloressãoonomedaen-
tidade. Vamoschamá-lodedicionárioidentificador para nome da
entidade.
Comele,poderemosverificarseoseunomeestánodicionário,acada
atributoencontradoparaumaentidade.Seestiver,significaqueessaentidade,
cujosatributossãooqueestamositerando,temumareferênciaparaoutra.A
entidadeéovalordodicionáriodeidentificadorparanomedaentidade.
import os
def extract_name (name):
return name . split( "." )[ 0 ]
def read_lines (filename):
_file = open (os . path . join( "data/meta-data" , filename), "rt" )
data = _file . read() . split( "\n" )
_file . close()
return data
def read_metadata (filename):
metadata = []
for column in read_lines(filename):
if column:
values = column . split( '\t' )
nome = values[ 0 ]
tipo = values[ 1 ]
desc = values[ 2 ]
metadata . append((nome, tipo, desc))
return metadata
def main ():
# dicionário nome entidade -> atributos
64
E-book gerado especialmente para 


## Página 81

CasadoCódigo Capítulo5. Estruturasdedados
meta = {}
# dicionário identificador -> nome entidade
keys = {}
for meta_data_file in os . listdir( "data/meta-data" ):
table_name = extract_name(meta_data_file)
attributes = read_metadata(meta_data_file)
identifier = attributes[ 0 ][ 0 ]
meta[table_name] = attributes
keys[identifier] = table_name
for key, val in meta . items():
for col in val:
if col[ 0 ] in keys:
if not col[ 0 ] == meta[key][ 0 ][ 0 ]:
print ( "Entiade {} -> {}" . format(key, col[ 0 ]))
if __name__ == "__main__" :
main()
Nofinaldoprogramaanterior,iteramostodososatributosdetodasasen-
tidades.Quandoumatributodeumaentidadequalquertemomesmonome
deumidentificadordeoutraentidade,nósencontramosumareferência.Essa
referênciaémuitosemelhanteaoconceitodechaveestrangeiradeumSGBD
(SistemadeGerenciamentodeBancodeDados,doinglês Data Base Mana-
gement System).Umacolunadessetiponospermiteliga çõesentredadosde
entidadesdistintas.Comoonossoobjetivomaioréexplorarosdados,damos
umpassoàfrentecomessafuncionalidade.
Sevocêrodaroprogramaanterior,deveráver:
Entiade ExecucaoFinanceira aponta para IdEmpreendimento
Entiade ExecucaoFinanceira aponta para IdLicitacao
Entiade Empreendimento aponta para IdInstituicao
Entiade Licitacao aponta para IdEmpreendimento
Issosignificaquepodemosmontarummodeloconceitualdonossope-
65
E-book gerado especialmente para 


## Página 82

5.8. Exemplofinalusandoestruturasdedadosparaexplorarosmetadados CasadoCódigo
quenouniversodedados.
Resultadofinaldousodasestruturasdedados
Aofinaldesseprograma,usamostodasas3fundamentaisestruturasde
dadosPython:tuplas,listasedicionários.Cadaumadelasserviuaumpropó-
sitoespecífico:osdicionáriosforamusadosparaobtermosobjetosdenosso
interessequandoempossedeumachave;alistafoiusadanacria çãodalista
deatributosdeumaentidade;eastuplasforamusadaspararepresentaras3
informaçõesdeumatributo(nome,tipoedescri ção).
Reparequeaindaestamosusandorecursosbemfundamentaisdalingua-
gem. Basicamente,nossoprogramamaiscomplexo,atéomomento,lêum
arquivo,iterasuaslinhas,aplicaalgumastransforma çõesnosdadosemonta
umconjuntodeestruturasdedadosquenospermitemobservarinforma ções
sobreosmetadados.
Comessasestruturasemmãos,podemos:
• Listarasentidades;
• Verosatributosdasentidades;
• Identificarrelacionamentosentreentidades.
Vamoscriarumexemplointerativoparaexplorarosmetadados.
5.8 Exemplo final usando estruturas de dados
para explorar os metadados
Aqui,vamosunirboapartedoquevimosatéagora:
• Stringsenúmeros;
• Definiçãodefun çãoechamadasafun ções;
• Loopscomfor;
• Estruturasdedados.
66
E-book gerado especialmente para 


## Página 83

CasadoCódigo Capítulo5. Estruturasdedados
import os
def extract_name (name):
return name . split( "." )[ 0 ]
def read_lines (filename):
_file = open (os . path . join( "data/meta-data" , filename), "rt" )
data = _file . read() . split( "\n" )
_file . close()
return data
def read_metadata (filename):
metadata = []
for column in read_lines(filename):
if column:
metadata . append( tuple (column . split( '\t' )[: 3 ]))
return metadata
def prompt ():
print ( "\nO que deseja ver?" )
print ( "(l) Listar entidades" )
print ( "(d) Exibir atributos de uma entidade" )
print ( "(r) Exibir referências de uma entidade" )
print ( "(s) Sair do programa" )
return input ( '' )
def main ():
# dicionário nome entidade -> atributos
meta = {}
# dicionário identificador -> nome entidade
keys = {}
# dicionário de relacionamentos
67
E-book gerado especialmente para 


## Página 84

5.8. Exemplofinalusandoestruturasdedadosparaexplorarosmetadados CasadoCódigo
relationships = {}
for meta_data_file in os . listdir( "data/meta-data" ):
table_name = extract_name(meta_data_file)
attributes = read_metadata(meta_data_file)
identifier = attributes[ 0 ][ 0 ]
meta[table_name] = attributes
keys[identifier] = table_name
for key, val in meta . items():
for col in val:
if col[ 0 ] in keys:
if not col[ 0 ] == meta[key][ 0 ][ 0 ]:
relationships[key] = keys[col[ 0 ]]
opcao = prompt()
while opcao != 's' :
if opcao == 'l' :
for entity_name in meta . keys():
print (entity_name)
elif opcao == 'd' :
entity_name = input ( 'Nome da entidade: ' )
for col in meta[entity_name]:
print (col)
elif opcao == 'r' :
entity_name = input ( 'Nome da entidade: ' )
other_entity = relationships[entity_name]
print (other_entity)
else :
print ( "Inexistente\n" )
opcao = prompt()
if __name__ == "__main__" :
main()
Esseprogramanosdáapossibilidadedeexplorarosmetadadosdeforma
interativa. Oquequeremosdaquiparaafrenteéusarosmetadadospara
68
E-book gerado especialmente para 


## Página 85

CasadoCódigo Capítulo5. Estruturasdedados
explorarosdadosemsi.
Umanovidadenessecódigoapresentadofoiousodométodo keys()
dodicionário.EmPython,podemositerarumdicionáriode3formas:
• Porchaveevalor,usandofor key, val in my_dict.items() ;
• Porchaves,usandofor key in my_dict.keys() ;
• Porvalores,usandofor val in my_dict.values() .
Vejaalgunsexemplos:
>>> meu_dict = { 'Empreendimento' : [( 'IdEmpreendimento' , 'biging' ,
... '...' )], 'Licitacao' : [( 'IdLicitacao' , 'bigint' ,
... '...' )]}
>>> for (name, attributes) in meu_dict . items():
... print ( "Nome {} com {} atributo(s)" . format(name,
len(attributes)))
...
Nome Licitacao com 1 atributo(s)
Nome Empreendimento com 1 atributo(s)
>>> for name in meu_dict . keys():
... print (name)
...
Licitacao
Empreendimento
>>> for attributes in meu_dict . values():
... print (attributes)
...
[('IdLicitacao', 'bigint', '...')]
[('IdEmpreendimento', 'biging', '...')]
Umadeficiênciadocódigoquecriamosatéagoraéqueosconceitospre-
sentesnasexplica çõesnãotêmumarepresenta çãodiretanocódigo.Nouni-
versodaprograma ção,existemdiversosparadigmas,como Orientação a Ob-
jetose Funcional,queinfluenciariamamelhororganizarocódigoquetemos
atéentão,ourepensaralgumasdenossassolu çõesatéomomento. Python,
comomencionadonoiníciodestelivro,éumalinguagem multiparadigma,
ouseja,vocêconsegueexplorarrecursosdeváriosparadigmasnela.
69
E-book gerado especialmente para 


## Página 86

5.9. Estruturasdedadossãoimportantes? CasadoCódigo
Nasequência,exploraremosumpoucodoparadigmada Orientação a
ObjetosparaexplicaromecanismodeclasseseobjetosemPython. Vamos
criarclassesquefa çamsentidoparaonossoaplicativo,paramelhoraraim-
plementação,isolaralgumascoisasdemais baixo nívelecriarumacamadade
abstraçãoquepermitiráquevocêfaçamaiscoisasnoprojeto.
5.9 Estruturas de dados são importantes?
Certamente!
UmdostemasmaisimportantesnaCiênciadaComputa çãosãoases-
truturasdedados.Elasoferecemmeioseficientesderealizarmostarefasem
conjuntosdedados.Estecapítulofoiumaintrodu çãoas3estruturasdedados
maiscomunsemPython.
5.10 Conclusão
Nestecapítulo,apresentamosoquesãotuplasedicionários. Juntocomas
listas,sãoasprincipaisestruturasdedadosdalinguagem.Nodiaadia,vamos
utilizá-lassempre.Mostramosumpoucodamotiva çãodeusarasestruturas,
dadasascaracterísticasindividuaisdecadauma.
Vimoscomoutilizarumacombina çãodeestruturaspararepresentaras
informaçõesquequeremosemnossoprograma.Paraaprendertodososde-
talhes,arecomenda çãooficialéolugarmaisadequado.
Adocumentaçãocompletadessasestruturasencontra-seem https://docs.
python.org/3/tutorial/datastructures.html.
Nopróximocapítulo,evoluiremosodesigninternodonossoaplicativo,
seguindoummodeloorientadoaobjetos.
70
E-book gerado especialmente para 


## Página 87

Capítulo6
Classeseobjetospythônicos
Játemosumprogramaque,apartirdosnossosdados,montaumaestrutura
querepresentatodasasentidadeserelacionamentosdeumapartedasinfor-
maçõesdabasededadosdoPortaldaTransparência[ 1]. Oqueaindanão
temoséumaformadeconsultarosdados.
Paraisso,vamosrealizarduastarefas:umaégarantirqueosdadosnos
arquivosdedadossejamcompatíveiscomaestruturadefinidanoarquivode
metadados;eaoutraécriaroscomponentesquevãocomporaconsultade
dados.
Oquequeremosrealizaré apenasumapequenaparte doqueumbanco
dedadosfaz,osfamosos SGBDs.Vamosmodelarobjetosquemapeiemcon-
ceitosdeumbancodedadosparaunidadesdecódigo.Omodelode Orien-
tação a Objetos éumparadigmamuitofortenacomunidadePython.Ainda
quenãosejaseuparadigmapreferido,éimportanteentendercomoPython
permiteaplicá-lo.
E-book gerado especialmente para 


## Página 88

6.1. Expressandoodomínioemclasses CasadoCódigo
6.1 Expressando o domínio em classes
Quandofalamosem domínio,estamosfalandodosconceitosquenossopro-
gramaopera. Osdadosquevamosexplorarsãodadosdegastospúblicos,
maspoderiamsersobrequalqueroutrotipodedadotabulado.Seguindoesse
raciocínio,vemosqueodomíniodonossoprogramasão dados tabulados.
Comumaclasse,podemosexpressaroconceitode tabelaejuntaraela
todososatributosecomportamentosesperados. Classesservemtantopara
organizaçãodecódigoquantoformadeexpressarumconceitododomínio.
Nessecaso,vamosjuntarosdadoseosmetadadosemumacoisaúnicaque
permitaavalida çãoeleituradosdados.
Oqueonossoprogramafazatéagoraconsisteem3funcionalidades:fazer
odownloaddabasededados;extrairoarquivobaixadoelerosmetadados;
montararelaçãodedependênciasentreasentidadespresentes.Odownloade
aextraçãodosdadoscontinuarãodamesmaforma.Porém,tudorelacionado
aosdadosemetadadosseráfeitoporobjetosquevamoscriarapartirdeagora.
Aideiaécriarumminibancodedadosemmemóriaquepermitainserir
linhas,validandoosdados,deacordocomasdefini çõesdosmetadados,e
permitaconsultascomfiltros.Essatarefapodeparecercomplicada,mas,aos
poucos,vamosconstruindocomponentesquetornarãoissopossível,deuma
formabemelegantee pythônica.
Agora,vamospassaramodelaronossodomíniocomclasseseentender
comoPythonnospermiteisso.
6.2 Definindo classes: primeiro passo
Python,assimcomoC #ouJava,possuiclasses,mascadaumadessaslingua-
genstempeculiaridadesemsuasimplementa ções.
Umaclassepermiteque estadoe comportamentofaçampartedamesma
unidadedecódigo. Quandofalamosem estado,falamosdos atributosde
umaclasse;jáquandofalamosem comportamento,falamosdeseus métodos.
Quandocriamosumaclasse,eladeveterumobjetivobemclaroesuainter-
facetemdesercoerentecomoqueelarepresentaedisponibiliza.
Paratermosumminibancodedadosemmemória,precisamosdealguma
formademanipulartabelasdedados.Onossoprimeiroobjetivoédeclarar
72
E-book gerado especialmente para 


## Página 89

CasadoCódigo Capítulo6. Classeseobjetospythônicos
umaclasseedefinirvaloresparaalgunsatributos. Nocasodanossaclasse
DataTable,osatributosiniciaisserão: name(string), columns(lista)e
data(lista). Essesatributossãoexatamenteosquetemosnosarquivosde
metadados,eosdadoscome çamvazios.Cadaentidadedabasededadosterá
umainstânciade DataTableassociada.
Emtermosdesintaxe,definirumaclasseemPythonéextremamentefácil.
Vamosvercomodefinirumaclassesemnada,instanciareaplicarafun ção
type()paraveroresultado:
>>> class DataTable :
... pass
...
>>> table = DataTable()
>>> type (table)
<class '__main__.DataTable'>
Oquevemosé <class ‘__main__.DataTable’>. Issoacontece
poisestamosrodandoemumconsolee,nessecaso,omódulocorrenteé
__main__. Agoratemosaclasse DataTable. Umacaracterísticainteres-
santeéque,emPython,asinstânciasdasclassespodemsermodificadasem
tempodeexecu ção. Umexemplodissoéquepodemosadicionaratributos
emtempodeexecu ção.Vejaoexemplo:
>>> class DataTable :
... pass
...
>>> table = DataTable()
>>> table . name = 'Alerta'
>>> table . columns = [ 'IdProjeto' , 'DescProjeto' ]
>>> table . data = []
Oproblemadessecódigoéquenãogarantimosquetodasasinstâncias
de DataTabletenhamosatributos namee column.Issoprecisaserfeito
dealgumaforma.Comomuitasvezesqueremoscriarobjetosjácomdeter-
minadasconfiguraçõesiniciais,émelhorterissodeumaformapadronizada.
Existeumaformapadronizadadedefinirosatributosdeumobjeto,geral-
mente,nométodo construtor.Aseguir,veremoscomocriá-lo.
73
E-book gerado especialmente para 


## Página 90

6.3. Criandoobjetos:métodosconstrutores CasadoCódigo
6.3 Criando objetos: métodos construtores
EmPython,algunsnomesdemétodosestãoreservadosparaousodapró-
prialinguagem. Umdessesmétodoséoquerepresentao construtor,sendo
seunome __init__().Outracaracterísticaéque,pelo The Zen of Python,
explícitoémelhorqueimplícito.Logo,oprimeiroparâmetrodoconstrutor
–assimcomoemtodosmétodosdeinstância–ésempreaprópriainstância.
Nonossocaso,éaqueestásendocriada.Por convenção,esseargumentotem
onomede self.Vejanoexemploadefini çãodeduasclasses:
class DataTable :
def __init__ ( self , name):
self . _name = name
self . _columns = []
self . _data = []
class Column :
def __init__ ( self , name, kind, description):
self . _name = name
self . _kind = kind
self . _description = description
Noteque,emnenhummomento,usamospalavrascomo publicou
private,nemdeclaramospreviamentequaisseriamosatributosdaclasse.
Quando uma classe é criada, todos os atributos serão inicializa-
dos conforme o código do construtor. Na prática, quando executamos
DataTable("Empreendimento"), a função __init__() da classe
DataTableéexecutadapassandoosparâmetrosdachamada.Assim,garan-
timosquetodasinstânciasde DataTablee Columntenhamosatributosde
queprecisamos.
Encapsulamentosemprivateoualgosemelhante
Emboraoencapsulamentonãopossaserfor çado–usandoalgocomoa
palavrareservada private,emJava–,elepodeserimplementadocom get-
ters, setterseatémesmocomo decorator @property.Umaconven çãomuito
respeitadaérepresentaratributosqueseriamprivadoscomumcaractere _
(underline)antes,comoem self._data.
74
E-book gerado especialmente para 


## Página 91

CasadoCódigo Capítulo6. Classeseobjetospythônicos
Dessaforma,sequiséssemosexporoconteúdode _data,poderíamos
terum getter:
>>> class DataTable :
... def __init__ ( self , name):
... self . _name = name
... self . _columns = []
... self . _data = []
... def getData ( self ):
... return self . _data
...
>>>
>>> table = DataTable( "TabelaTeste" )
>>> print (table . getData())
[]
Noexemploanterior,teríamosqueusar getData()paraacessaroatri-
buto _data.
Oupoderíamosusarum decorator:
>>> class DataTable :
... def __init__ ( self , name):
... self . _name = name
... self . _columns = []
... self . _data = []
... @property
... def data ( self ):
... return self . _data
...
>>> table = DataTable( "TabelaTeste" )
>>> print (table . data)
[]
Avantagemdo decorator @propertyéquepoderíamosacessaroatri-
butousandoapenas data,comose DataTabletivesseumatributocom
essenome.
75
E-book gerado especialmente para 


## Página 92

6.4. Classesdocumentadas:docstrings CasadoCódigo
6.4 C lasses documentadas : docstrings
Alémdocódigodaclasse,eladeveterpreferencialmentealgumadocumenta-
ção.Assimcomoemoutraslinguagens,adocumenta çãopodeserexpressada
juntoaocódigo.MasPython,porsuavez,tambémdisponibilizaadocumen-
taçãoemtempodeexecu ção.
Quandocriamosumaclasse,éimportanteexpressarquaisosatributose
paraqueservem,efalardosmétodoseoquemaisfornecessárioparaqueos
usuáriosdoseucódigoausem.
Umaótimaformadefazerissoécom docstrings.Essasstringssetornam
oatributo __doc__dasclasses.Vejaoexemplo:
class DataTable :
"""Representa uma Tabela de dados.
Essa classe representa uma tabela de dados do portal
da transparência. Deve ser capaz de validar linhas
inseridas de acordo com as colunas que possui. As
linhas inseridas ficam registradas dentro dela.
Attributes:
name: Nome da tabela
columns: [Lista de colunas]
data: [Lista de dados]
"""
def __init__ ( self , name):
"""Construtor
Args:
name: Nome da Tabela
"""
self . _name = name
self . _columns = []
self . data = []
class Column :
"""Representa uma coluna em um DataTable
76
E-book gerado especialmente para 


## Página 93

CasadoCódigo Capítulo6. Classeseobjetospythônicos
Essa classe contém as informações de uma coluna
e deve validar um dado de acordo com o tipo de
dado configurado no construtor.
Attributes:
name: Nome da Coluna
king: Tipo do Dado (varchar, bigint, numeric)
description: Descrição da coluna
"""
def __init__ ( self , name, kind, description = "" ):
"""Construtor
Args:
name: Nome da Coluna
kind: Tipo do dado (varchar, bigint, numeric)
description: Descrição da coluna
"""
self . _name = name
self . _kind = kind
self . _description = description
Salvenoarquivo domain.pyedepoisrodeocódigoaseguir,noconsole
Python:
>>> from domain import *
>>> print (DataTable . __doc__)
Representa uma Tabela de dados.
Essa classe representa uma tabela de dados do portal
da transparência. Deve ser capaz de validar linhas
inseridas de acordo com as colunas que possui. As
linhas inseridas ficam registradas dentro dela.
Attributes:
name: Nome da tabela
columns: [Lista de colunas]
data: [Lista de dados]
>>> print (Column . __init__ . __doc__)
77
E-book gerado especialmente para 


## Página 94

6.5. Métodos:adicionandocomportamentosaoobjeto CasadoCódigo
Construtor
Args:
name: Nome da Coluna
kind: Tipo do dado (varchar, bigint, numeric)
description: Descrição da coluna
Agoraquetemosumaclassecommétodo construtoreumaexplica çãoda
suaexistência,mesmoquesejainicial,podemosseguiradicionandocompor-
tamentosnela.
6.5 Métodos: adicionando comportamentos ao
objeto
Vamosadicionarummétodoànossaclasse:
class DataTable :
def __init__ ( self , name):
self . _name = name
self . _columns = []
self . _data = []
def add_column ( self , name, kind, description):
column = Column(name, kind, description)
self . _columns . append(column)
return column
Ométodo add_columnadicionaumainstânciade Columnemuma
lista, em DataTable. Conceitualmente, podemos pensar que uma ta-
belatemumacole çãodecolunas,eessacole çãoérepresentadapelalista
self._columns.
Deformasemelhante,poderíamosterummétodo add_references()
para adicionar quais tabelas são apontadas pela instância, e
add_referenced() onde adicionamos as tabelas que referenciam a
própriainstância.Paraguardaressasinforma ções,precisamosdedoisnovos
atributosem DataTable: _references,quesãoquaistabelaselaaponta;
e _referenced,quesãoastabelasqueapontamparaela.
78
E-book gerado especialmente para 


## Página 95

CasadoCódigo Capítulo6. Classeseobjetospythônicos
Comasinforma çõesquesabemosextrair,jápodemosdizerquaistabelas
existemequemapontaparaquem,especificandoascolunasdessasreferên-
cias.Oquenãotemoséumaclassequerepresenteessano çãode relaciona-
mento.
Esse relacionamentoexistequandotemosumacolunadeumatabelaque
éumachaveprimáriadeoutra.Oquedeterminaumrelacionamentoé:uma
coluna(ondeeleexiste),umatabeladeondesaieumatabelaaondeelechega.
Juntoaisso,vamostambémdarumnomeparaesserelacionamento.
Algumas docstringsserãoomitidasporconveniência.Vamosadicionara
classe Relationship:
class Relationship :
"""Classe que representa um relacionamento entre DataTables
Essa classe tem todas as informações que identificam um
relacionamento entre tabelas. Em qual coluna ele existe,
de onde vem e pra onde vai.
"""
def __init__ ( self , name, _from, to, on):
"""Construtor
Args:
name: Nome
from: Tabela de onde sai
to: Tabela pra onde vai
on: instância de coluna onde existe
"""
self . _name = name
self . _from = _from
self . _to = to
self . _on = on
class DataTable :
def __init__ ( self , name):
self . _name = name
self . _columns = []
self . _references = []
self . _referenced = []
79
E-book gerado especialmente para 


## Página 96

6.5. Métodos:adicionandocomportamentosaoobjeto CasadoCódigo
self . _data = []
def add_column ( self , name, kind, description = "" ):
column = Column(name, kind, description = description)
self . _columns . append(column)
return column
def add_references ( self , name, to, on):
"""Cria uma referencia dessa tabela para uma outra tabela
Args:
name: nome da relação
to: instância da tabela apontada
on: instância coluna em que existe a relação
"""
relationship = Relationship(name, self , to, on)
self . _references . append(relationship)
def add_referenced ( self , name, by, on):
"""Cria uma referência para outra tabela que aponta para
essa.
Args:
name: nome da relação
by: instância da tabela que aponta para essa
on: instância coluna em que existe a relação
"""
relationship = Relationship(name, by, self , on)
self . _referenced . append(relationship)
Agoratemos4métodosnaclasse DataTable:oconstrutoretrêsmé-
todosde domínio.Doisdessesmétodossãomuitosemelhantes,entãovamos
refatorarumpoucomais.
Coloqueocódigoanterior,destecapítulo,noarquivo domain.py.Em
umoutroarquivo,oumesmonoterminal,vocêpodeusaressasclasses.Veja
ocódigoaseguir:
>>> from domain import DataTable
>>> table_empreedimento = DataTable( "Empreendimento" )
80
E-book gerado especialmente para 


## Página 97

CasadoCódigo Capítulo6. Classeseobjetospythônicos
>>> col_id = table_empreedimento . add_column( 'IdEmpreendimento' ,
'bigint')
>>> col_aditivo = table_empreedimento . add_column( 'IdAditivo' ,
'bigint')
>>> col_alerta = table_empreedimento . add_column( 'IdAlerta' ,
'bigint')
>>> table_aditivo = DataTable( "Aditivo" )
>>> col_id = table_aditivo . add_column( 'IdAditivo' , 'bigint' )
>>> col_emp_id =
table_empreedimento.add_column('IdEmpreendimento', 'bigint')
>>> table_empreedimento . add_references( "IdAditivo" ,
table_aditivo, col_aditivo)
>>> table_aditivo . add_referenced( "IdEmpreendimento" ,
table_empreedimento, col_emp_id)
Onossocódigoagorarepresenta2tabelas,e Empreendimentoreferen-
ciaeéreferenciadapor Aditivo.Oquefaltounoexemploéque,nahoraem
quenossoprogramaestiverlendoosmetadados,eleprecisadetectarautoma-
ticamenteosrelacionamentos.Paraisso,precisamosdarumpassoadiante.
Aospoucos,nossomodelodeclassesganhamaiscomportamentos,mas
aindaestamosumpoucolongedeteralgomaiscompleto. Vamosresolver
umproblemadecadavez.Opróximoéidentificarosrelacionamentospro-
curandopelaschavesprimárias.
Nosarquivosdemetadados,umdostiposdecolunatemotipo PK.Isso
representaqueaquelacolunaéachaveprimária( primary key)databelacor-
respondente.Semprequeachamosumacolunacomnomeigualaodealguma
chaveprimáriaéporqueachamosumareferênciaentreastabelas.Logo,po-
demospensarnachaveprimáriacomoumtipoespecialdecoluna.
6.6 H erança simples em Python
Podemosdizerqueum relacionamento,nosnossosdados,existequandouma
colunadeumatabelaéachaveprimáriadeoutra.Acoluna IdAlertana
tabela Empreendimentodizque Empreendimentoreferencia Alerta.
Essacolunaéchaveprimáriaem Alerta. Partedanossalógicaé:sempre
queacharmosumachaveprimária,elaseráguardadaemumdicionáriopelo
81
E-book gerado especialmente para 


## Página 98

6.6. HerançasimplesemPython CasadoCódigo
nome,eaoiterarmosporoutras,consultaremosessedicionário.Casoexista
umachaveprimária,éporquetemosumarela ção.
Comherança,conseguimoscriarumnovotipo, PrimaryKeyqueherda
de Column,mantendoosseusatributosemodificandoovalorde _is_pk.
class PrimaryKey (Column):
def __init__ ( self , table, name, kind, description = None ):
super () . __init__(name, kind, description = description)
self . _is_pk = True
Areferênciadasuperclasseficanamesmalinhadonomedaclasse,en-
treparênteses.Alémdisso,reparequefoiutilizadaafun ção super()para
acessaroconstrutordasuperclasse.Podemosimplementarummétodonovo
em Columneusareminstânciasde PrimaryKey.
class Column :
def __init__ ( self , name, kind, description = "" ):
self . _name = name
self . _kind = kind
self . _description = description
self . _is_pk = False
def __str__ ( self ):
_str = "Col: {} : {} {}" . format( self . _name,
self . _kind,
self . _description)
return _str
class PrimaryKey (Column):
def __init__ ( self , table, name, kind, description = "" ):
super () . __init__(name, kind, description = description)
self . _is_pk = True
Novamente,salvenoarquivo domain.pye,noterminal,executeosse-
guintescomandos:
>>> from domain import *
>>> table = DataTable( "Empreendimento" )
>>> print (Column( 'IdEmpreendimento' , 'bigint' ))
82
E-book gerado especialmente para 


## Página 99

CasadoCódigo Capítulo6. Classeseobjetospythônicos
Col: IdEmpreendimento : bigint
>>> print (PrimaryKey(table, 'IdEmpreendimento' , 'bigint' ))
Col: IdEmpreendimento : bigint
Aqui,vemosqueométodoespecial __str__()foiimplementadoeher-
dadopelainstânciade PrimaryKey.Essemétodotambéméumdosméto-
dosespeciaisetemafun çãosemelhanteao toString()doJava,porexem-
plo,retornandoumarepresenta çãodoobjetoemformade String.
Essemétodopodesersobrescritoem PrimaryKey.Bastadeclará-lonela
mesma:
class PrimaryKey (Column):
def __init__ ( self , table, name, kind, description = "" ):
super () . __init__(name, kind, description = description)
self . _is_pk = True
def __str__ ( self ):
_str = "Col: {} : {} {}" . format( self . _name,
self . _kind,
self . _description)
return "{} - {}" . format( 'PK' , _str)
class Column :
def __init__ ( self , name, kind, description = "" ):
self . _name = name
self . _kind = kind
self . _description = description
self . _is_pk = False
def __str__ ( self ):
_str = "Col: {} : {} {}" . format( self . _name,
self . _kind,
self . _description)
return _str
Novamente,salveem domain.py.Executeevejaoresultado:
>>> from domain import *
>>> table = DataTable( "Empreendimento" )
83
E-book gerado especialmente para 


## Página 100

6.6. HerançasimplesemPython CasadoCódigo
>>> print (Column( 'IdEmpreendimento' , 'bigint' ))
Col: IdEmpreendimento : bigint
>>> print (PrimaryKey(table, 'IdEmpreendimento' , 'bigint' ))
PK - Col: IdEmpreendimento : bigint
O que ficou ruim é que a classeDataTable não implementa
__str__(),masissopodeserfacilmenteresolvidodepois.
Verificandoseumobjetoéinstânciadeumaclasse
Umdosobjetivosdoprogramaégarantirqueosdadossejamvalidados
antesdomodelosermontadoemmemória.Paraisso,podemoscolocaruma
funçãodevalida çãonaclasse Columneusá-laemoutraspartesdocódigo,
provavelmenteondeasinforma çõesdosarquivossãolidas.
Para implementar a valida ção, vamos usar a fun ção
isinstance(value, type) e uma classe chamadaDecimal. Fe-
lizmente,ostiposdefinidosnabasedoCopaTransparente(dadosdoPortal
da Transparência [1]) podem ser mapeados diretamente para tipos em
Python. Issopermitequealgumasverifica çõessejamfeitascomafun ção
embutida isinstance(value, type).Nonossocódigo,o ‘bigint’é
mapeadoparauminteiro, ‘numeric’para Decimale ‘varchar’para
strings.
from decimal import Decimal
class Column :
def __init__ ( self , name, kind, description = "" ):
self . _name = name
self . _kind = kind
self . _description = description
def __str__ ( self ):
return "Col: {} : {} {}" . format( self . _name,
self . _kind,
self . _description)
def validate ( self , data):
if self . _kind == 'bigint' :
84
E-book gerado especialmente para 


## Página 101

CasadoCódigo Capítulo6. Classeseobjetospythônicos
if isinstance (data, int ):
return True
return False
elif self . _kind == 'varchar' :
if isinstance (data, str ):
return True
return False
elif self . _kind == 'numeric' :
try :
val = Decimal(data)
except :
return False
return True
Vamostestarafun ção validate()noconsole:
>>> from domain import *
>>>
>>> c1 = Column( "IdEmpreendimento" , "bigint" )
>>> c1 . validate( 100 )
True
>>> not c1 . validate( 10.1 )
True
>>> not c1 . validate( "Texto" )
True
>>> c1 = Column( "DescEmpreendimento" , "varchar" )
>>> c1 . validate( "Contrato" )
True
>>> not c1 . validate( 10.1 )
True
>>> not c1 . validate( 10 )
True
>>> c1 = Column( "ValTotalPrevisto" , "numeric" )
>>> c1 . validate( 10.1 )
True
>>> c1 . validate( 10 )
True
>>> not c1 . validate( "Texto" )
True
85
E-book gerado especialmente para 


## Página 102

6.7. Atributosdeclasses:compartilhadosentretodasinstâncias CasadoCódigo
Oquevemosnoresultadoéqueovalor 100éum ‘bigint’válido,
10.1éum ‘numeric’válidoe ‘Contrato’éum ‘varchar’válido.
Todasasoutrassitua çõesnãosãoválidaseoretornoéinvertidopelo not,
imprimindo True.
Comessemétodo,todavezqueumalinhadoarquivodedadosforlida,
poderemosvalidaroseuconteúdocomasregrasdascolunasquecriamos
comosmetadados.Seumalinhativertodasinforma çõesválidas,elapoderá
serinseridanalistadedadosdatabela.
6.7 Atributos de classes : compartilhados en -
tre todas instâncias
Comoemoutraslinguagens,osatributosdeclassesãocompartilhadosentre
todasasinstânciasdeumaclasse. Amudan çadesejadaétornarométodo
deinstância validate()ummétodoestáticooudeclasse–quesãomuito
semelhantes.Aprimeiraetapaparafazerissoésabercomocriarumatributo
declasse.
Vejaoexemplo:
class Column :
def _validate ( self , kind, data):
if kind == 'bigint' :
if isinstance (data, int ):
return True
return False
elif kind == 'varchar' :
if isinstance (data, str ):
return True
return False
elif kind == 'numeric' :
try :
val = Decimal(data)
except :
return False
return True
validate = _validate
86
E-book gerado especialmente para 


## Página 103

CasadoCódigo Capítulo6. Classeseobjetospythônicos
Naúltimalinha,declaramosumatributodeclassechamado validatee
atribuímosaeleométodo _validate.Oproblemaéqueissonãofunciona
dessaforma.Vejaasexecu çõesaseguir:
>>> class Column :
... def _validate ( self , kind, data):
... if kind == 'bigint' :
... if isinstance (data, int ):
... return True
... return False
... elif kind == 'varchar' :
... if isinstance (data, str ):
... return True
... return False
... elif kind == 'numeric' :
... try :
... val = Decimal(data)
... except :
... return False
... return True
... validate = _validate
...
>>> Column . validate( 'bigint' , 10 )
Traceback (most recent call last):
File "<stdin>" , line 1 , in <module>
TypeError : _validate() missing 1 required positional argument:
'data'
Comovimos,paramétodosdeinstância,oprimeiroparâmetroéapró-
priainstânciasendoreferenciada.Nonossocaso,nãoexisteinstância,jáque
declaramosumatributodeclasseevamosreferenciá-lopelaclasse. Vamos
vercomofazerfuncionarocódigoanterior.
6.8 Métodos estáticos e de classe: usando mais
as classes
Podemostransformarométododevalida çãoemummétodoestático. Em
Python, osmétodosestáticosdeclassessãoosquepodemserchamados
87
E-book gerado especialmente para 


## Página 104

6.8. Métodosestáticosedeclasse:usandomaisasclasses CasadoCódigo
usandoumareferênciaparaumaclasse Column.validate(),ouinstância
col_instance.validate().Omaiscomuméusarareferênciadaclasse.
Adiferençaentreométodoestáticoeodeclasseéque,neste,oprimeiro
argumentoéainstânciadaclasse. Comononossocasonãoprecisamosda
instânciadaclasse,usamosummétodoestático. Emambos,oparâmetro
selfdosmétodosdeinstâncianãoépassado.
Para definir um método estático, usamos uma função chamada
staticmethod(),querecebecomoargumentoummétodo.Edeclaramos
oresultadodachamadade staticmethodcomoumatributodeclasse,da
nossaclasse.
from decimal import Decimal
class Column :
def __init__ ( self , name, kind, description = "" ):
self . _name = name
self . _kind = kind
self . _description = description
def _validate (kind, data):
if kind == 'bigint' :
if isinstance (data, int ):
return True
return False
elif kind == 'varchar' :
if isinstance (data, str ):
return True
return False
elif kind == 'numeric' :
try :
val = Decimal(data)
except :
return False
return True
validate = staticmethod (_validate)
Osegredoaquiéque _validate,agora,nãofoideclaradocomaassi-
88
E-book gerado especialmente para 


## Página 105

CasadoCódigo Capítulo6. Classeseobjetospythônicos
naturademétododeinstância,quelevaemconsidera çãoque selfésempre
oprimeiroargumento.Oquequeremoséummétodogenérico,quenãopre-
cisedeumainstânciacriadaeque,dadootipoeovalor,retornafalsoou
verdadeiro,seovalorforcorretoparaotipo.
Paraqueessafun çãopossaseracessadapelareferênciadaclasse Column,
precisamosinformarqueométodo _validateéestáticoequeéacessadono
nome validate,comousamosnadeclara çãodaúltimalinhadoexemplo.
Novamente,atualizeoarquivo domain.pyeexecutenoconsolePython:
>>> Column.validate('bigint', 100)
True
>>> Column.validate('numeric', 10.1)
True
>>> Column.validate('varchar', 'Texto')
True
Paratransformaremmétododeclasse,usamosafun ção classmethod.
Adiferençapara staticmethodéque,em classmethod,oprimeiroar-
gumentodaassinaturaéaprópriaclasse Column.Vejaemcódigo:
class Column :
def _validate (cls, kind, data):
if kind == 'bigint' :
if isinstance (data, int ):
return True
return False
elif kind == 'varchar' :
if isinstance (data, str ):
return True
return False
elif kind == 'numeric' :
try :
val = Decimal(data)
except :
return False
return True
validate = classmethod (_validate)
89
E-book gerado especialmente para 


## Página 106

6.9. Encapsulamentopythônicocomafun çãoproperty CasadoCódigo
Compoucaslinhas,conseguimosaplicaressemodelodeobjetosinicial
nonossoprograma.
Umdetalheimportanteéqueoquefoifeitonestase çãopoderiaserfeito
deformamaiselegantecomumrecursoquenãovimos,chamado decorator
(oudecorador).Paranãoterqueexplicarsobredecoradoresnestepontodo
livro,optamosportrabalharcom classmethod()e staticmethod()
comofunções.
6.9 E ncapsulamento pythônico com a função
property
Umtópicoqueaindanãocobrimoséencapsulamento pythônico. Paraisso,
vamosaprenderausarafun ção property.
Inicialmente,vamosimaginarumencapsulamentodaleiturausandoum
getter. Nocasodanossaclasse DataTable,nãoqueremosqueousuário
acesseonomepelareferênciade _name.Oprimeiropasso,portanto,écriar
um gettere,depois,usarafun ção propertyparaassociá-loàchamadade
umatributo.Vejaoexemploparaentendermelhor:
class DataTable :
def __init__ ( self , name):
self . _name = name
self . _columns = []
self . _references = []
self . _referenced = []
self . _data = []
def _get_name ( self ):
print ( "Getter executado!" )
return self . _name
name = property (_get_name)
Coloqueessamodifica çãonaclasse DataTableerodenoconsole:
>>> table = DataTable( "Empreendimento" )
>>> table . name
90
E-book gerado especialmente para 


## Página 107

CasadoCódigo Capítulo6. Classeseobjetospythônicos
Setter executado!
'Empreendimento'
Oqueaconteceufoique,quandoexecutamos table.name,ométodo
_get_name()–quefoiconfiguradocomogetternafunção property–foi
chamado.Omesmoprincípiopodeserusadoparao settere deleter.
class DataTable :
def __init__ ( self , name):
self . _name = name
self . _columns = []
self . _references = []
self . _referenced = []
self . _data = []
def _get_name ( self ):
print ( "Getter executado!" )
return self . _name
def _set_name ( self , _name):
print ( "Setter executado!" )
self . _name = _name
def _del_name ( self ):
print ( "Deletter executado!" )
raise AttributeError ( "Não pode deletar esse atributo" )
name = property (_get_name, _set_name, _del_name)
Repare aqui que, na documentação, consta exatamente que a função
property recebe nessa ordem:getter, setter e deleter. Agora salve em
domain.pyeexecutenoconsolePython:
>>> table = DataTable( "Empreendimento" )
>>> table . name
Getter executado!
'Empreendimento'
>>> table . name = 'Alerta'
Setter executado!
91
E-book gerado especialmente para 


## Página 108

6.10. Herançamúltipla:herdandodeváriasclasses CasadoCódigo
>>> del table . name
Deletter executado!
Traceback (most recent call last):
File "<stdin>" , line 1 , in <module>
File "<stdin>" , line 16 , in _del_name
AttributeError : Não pode deletar esse atributo
Aatribuiçãodevalorpara table.nametambémfoifeitapormeiodo
método _set_name(),ondepoderíamostercolocadoumavalida ção,por
exemplo.Omesmoaconteceparao deleter,queexecuta _del_name()por
baixo.
Agora,podemoscriarclassescomencapsulamento pythônico.
6.10 Herança múltipla : herdando de v árias
classes
Nestapartedolivro,voucobrirumassuntobemsuperficialmente,semem-
pregoprático,poisfazpartedocontextoqueestamosestudandodeclasses.
Maisàfrente,vamosusá-locomumobjetivoprático.
Pythonsuportaumaformadeheran çamúltipla.Superficialmente,oque
importaéaordemdebuscadosmétodos.Vamosverumexemploediscuti-lo:
92
E-book gerado especialmente para 


## Página 109

CasadoCódigo Capítulo6. Classeseobjetospythônicos
Fig.6.1:Heran çamúltipla
class A :
def run ( self ):
return "A"
class B :
def run ( self ):
return "B"
class C (A, B):
pass
a = A()
b = B()
c = C()
assert "A" == c . run()
Ocomportamentoesperadoéprimeirobuscar run()nadefiniçãode C.
Comonãoexiste,ointerpretadorprocuranassuperclassesdaesquerdapara
adireita,nadefini çãodaheran ça. Comisso,quandofalamos C(A, B),a
93
E-book gerado especialmente para 


## Página 110

6.11. OqueéDuckTyping? CasadoCódigo
procurade run()éfeitaem Aeemsuperclassesde A,ecasonãoexista,em
Besuperclassesde B.
Nonossocaso, c.run()retorna "A",jáqueométodofoiencontrado
em Aantesdeserem B.
Essaordemdebuscademétodosécomumentechamadade Method Re-
solution Order(MRO).Podemosatéacessá-laviaumatributoespecial:
>>> class A :
... def run ( self ):
... return "A"
>>> class B :
... def run ( self ):
... return "B"
>>> class C (A, B):
... pass
>>> C . __mro__
(__main__.C, __main__.A, __main__.B, builtins.object)
O output nos diz a ordem: C, A, B e, no final, o próprio
builtins.objectdequaltodasasclassesherdam.
6.11 Oque éDuckTyping?
Essetermo, DuckTypingéumaexpressãoquediz:tudoquepodefazer“quack”
éumpato;porisso, ducktyping(emumatradu çãolivre,“atipagemdopato”).
Secolocarmosessalógicaemumcontextodeobjetos,otermorefere-seao
fatodequeumobjetoemPythonpodesecomportarcomosefosseumoutro
objetoqualquer,desdequetenhadeterminadasemelhan ça.
EmPython,quandopassamosumobjetocomoparâmetrodeumafun ção
oumétodo,nãoháchecagemdetipo,poisnãoexistemtiposexplícitosna
assinatura,logo,qualquerobjetopodeserpassado.
Sedentrodométodoacessamosoatributo nome,qualquerobjetoque
tenhaesseatributoserácompatívelcomessecódigo.Paramétodoséamesma
coisa:seummétodoqualquerforchamado,qualquerobjetoquetenhaum
métodocommesmonomeemesmonúmerodeparâmetrospoderáserusado.
Esseéosignificadopráticodo ducktyping.Vamosexemplificar:
94
E-book gerado especialmente para 


## Página 111

CasadoCódigo Capítulo6. Classeseobjetospythônicos
>>> from domain import *
>>> table = DataTable( "Empreendimento" )
>>>
>>> class DuckType :
... pass
...
>>> duck = DuckType()
>>> duck . name = "quak"
>>>
>>> def print_name (table):
... print (table . name)
...
>>> print_name(table)
Empreendimento
>>> print_name(duck)
quak
A função print_name(tabela) serve tanto para instâncias de
DataTablequantoparaqualqueroutraquetenhaoatributo name. Esse
casopodesersimplesdemais,masemoutroscontextos,o ducktypingémuito
empregado. Seporumladoémuitoprático,poroutro,seuusoindiscrimi-
nadopodelevaratémesmoabugsnocódigo.
Dequalquerforma,éumacaracterísticarelevantedouniversodelingua-
gensdinâmicas,inclusivePython.
6.12 Conclusão
Nestecapítulo,exploramososaspectosbásicosdeclasseseobjetosemPython.
Descobrimoscomodeclararclasses, quepodemosadicionaratributosem
tempodeexecu ção,comosãodefinidososmétodosdedomínio,construtores
eofamoso __str__(). Alémdisso,exploramosherançasimplesemúlti-
pla,métodosestáticosedeclasse,atributosdeclasseeencapsulamentocom
afunção property.
Aideianãoeraexplicartudo,maspelomenosumaparteinicial,permi-
tindo,assim,queonossopróximopassosejacriarcódigoPythondequali-
dadeparaomundoreal.
95
E-book gerado especialmente para 


## Página 112

E-book gerado especialmente para 


## Página 113

Capítulo7
Tratandoerroseexce ções:
tornandoocódigomaisrobusto
7.1 Escreveu errado? Erros de sintaxe
EmPython,existemdoistiposprincipaisdeerros: oserrosdesintaxeeas
exceções.
Parautilizarosrecursosdeumalinguagemdeprograma ção,devemos
aprendersuasintaxe. Sevocêtentouexecutarosexemplosdolivro,talvez
tenhavistoumerrodesintaxeemalgummomento.Essetipodeerroimpede
aexecuçãodeumprograma,aopassoqueasexce çõesaparecememgrande
maioriadurantesuaexecu ção.
Vejaoqueacontecequandoexecutamosumcódigocomerrodesintaxe:
>>> print ( 'Erro de sintaxe)
E-book gerado especialmente para 


## Página 114

7.2. Comotornarocódigomaisrobusto? CasadoCódigo
File "<stdin>" , line 1
print ( 'Erro de sintaxe)
^
SyntaxError : EOL while scanning string literal
Noexemploanterior,ganhamosum SyntaxError,poisnãofechamos
corretamentea stringquequeremosimprimirnatela.
Agora,observeesteoutroexemplo:
>>> print ( 1/0 )
Traceback (most recent call last):
File "<stdin>" , line 1 , in <module>
ZeroDivisionError : division by zero
Aqui,vemosumaexce çãosendolevantadaemtempodeexecu ção.
Qualosignificadodaexce ção?
Aexceçãorepresentaumaanomaliaouumasitua çãoqueprecisasertra-
tadaespecificamente.
Oserrosdesintaxe,especificamenteosquenãopodemser tratados,de-
vemsercorrigidosparaqueumprogramapossaserexecutado.Umprograma
comessetipodeerronãopodesercompiladopara bytecodeparaserexecu-
tado.
Mesmocomasintaxecorreta,algunserrospodemacontecercomopro-
gramarodando.Imagine,porexemplo,tentarlerumarquivoquenãoexiste.
EmlinguagenscomoC,muitasbibliotecasretornam-1quandoocorrem
erros,mas,emoutras,existeumaformaespecialdesetratá-los,aschamadas
exceções.Python,assimcomoJavaeRuby,temsuporteparaessetratamento
deexceções,geralmenteintroduzindoumcomando. NocasodePython,é
umcomandocomposto( compound statement)queusaaspalavrasreserva-
das try/exceptparacriarblocosdecódigoquecontêmalternativaspara
quandoasexce çõesocorrem.
7.2 Como tornar o código mais robusto?
Usandooexemploanterior,comopodemoscontornarumaexce çãogerada
quandotentamoslerumarquivoquenãoexiste?Nessecaso,vamosapenas
98
E-book gerado especialmente para 


## Página 115

CasadoCódigo Capítulo7. Tratandoerroseexceções:tornandoocódigomaisrobusto
apresentarumamensagemmaisamigável.Vejaocódigoaseguir:
import zipfile
banco_zip = zipfile . ZipFile( "saida.zip" )
banco_zip . extractall(path = "banco" )
banco_zip . close()
Aqui,contamoscomaexistênciadoarquivo saida.zip.Casoelenão
exista,umamensagemseráexibida:
FileNotFoundError: [Errno 2 ] No such file or directory :
'saida.zip'
Esseéumerrofacilmentetratável,usandoocomando try/except.Na
prática,ocomando try/exceptéquempermiteotratamentodeexce ções
emPython.Vejaoexemplo:
import zipfile
try :
banco_zip = zipfile . ZipFile( "saida.zip" )
banco_zip . extractall(path = "banco" )
banco_zip . close()
except FileNotFoundError:
print ( "Arquivo inexistente" )
Quandotrabalhamoscomarquivos,váriasexce çõespodemserlevanta-
das. Nabibliotecapadrão,temosumahierarquiadeexce çõesquesãopa-
dronizadasequenospermitemtrataroserrosemníveismaisespecíficosou
genéricos.Vamosverumapartedaárvoredeexce ções:
+-- OSError
| +-- BlockingIOError
| +-- ChildProcessError
| +-- ConnectionError
| | +-- BrokenPipeError
| | +-- ConnectionAbortedError
| | +-- ConnectionRefusedError
| | +-- ConnectionResetError
99
E-book gerado especialmente para 


## Página 116

7.3. Tratandováriaspossíveisexceçõesemummesmobloco CasadoCódigo
| +-- FileExistsError
| +-- FileNotFoundError
| +-- InterruptedError
| +-- IsADirectoryError
| +-- NotADirectoryError
| +-- PermissionError
| +-- ProcessLookupError
| +-- TimeoutError
Vendoessaárvore,querepresentaumahierarquiadeexce ções,consegui-
mosobservar,porexemplo,que OSErroréoquechamamosde pai/mãede
todasasoutrasexce ções.Sequisermostrataroserrosdeumaformagenérica,
podemosusar OSErrornapartedo except.
Paratratarumerromaisespecificamente,comoumarquivoinexistente,
usamos FileNotFoundErrornobloco except.Repareque,seutilizar-
mos OSError,vamostratarerrosdetodasasexce ções filhas.Quandousa-
mos FileNotFoundError,quenãopossuifilhas,vamostratarapenaseste
casoespecífico.
7.3 Tratando v árias possíveis exceções em um
mesmo bloco
Emmuitoscasos,onúmerodeexce çõesqueumaúnicalinhadecódigopode
gerarpodesersuperiora1.Porisso,énormalterblocosquetratamdiversas
exceçõessimultaneamente.
Vamosverumexemplonoqualtratamos,separadamente,maisdeuma
exceção:
import zipfile
try :
banco_zip = zipfile . ZipFile( "saida.zip" )
banco_zip . extractall(path = "banco" )
banco_zip . close()
except FileNotFoundError:
print ( "Arquivo inexistente" )
100
E-book gerado especialmente para 


## Página 117

CasadoCódigo Capítulo7. Tratandoerroseexceções:tornandoocódigomaisrobusto
except PermissionError as pme:
print ( "Erro de permissao" )
Seolharmosparaaárvoredeexce ções,veremosqueambassãofilhasde
OSErrore,porisso,poderíamosterumtratamentoúnicoparaambas.
Oqueficoufaltandoéque,apesardetornaramensagemdeerromais
amigável,nãoestamosinformandoqualoarquivoquetentamosusar,oque
gerouoerro.
Vamosverumasolu çãoquetemumapequenavaria çãonasintaxe,adi-
cionandoum aliasparaainstânciadaexce çãousandoapalavrareservada
as:
import zipfile
try :
banco_zip = zipfile . ZipFile( "saidax.zip" )
banco_zip . extractall(path = "banco" )
banco_zip . close()
except OSError as ose:
print ( "Algum problema ao ler o arquivo {}"
. format(ose . filename))
É muito importante entender que todas exceções que são filhas de
OSErrorserãotratadasaqui. Todaselaspossuemoatributo filename,
portanto,essecódigofuncionaráemtodososcasosondeoerroéfilhode
OSError.
Emcasodedúvida,procureconhecermelhorosignificadodasexce ções
paratomarboasdecisõesquantoaotratamentogenérico,enãotratarcasos
demaissemquerer.Nãoexistefórmulacerta,logo,useobomsensonahora
dedecidiremqueníveldeespecificidadechegar.
Outravariaçãoseriausarasintaxecomtuplas:
import zipfile
try :
banco_zip = zipfile . ZipFile( "saida.zip" )
banco_zip . extractall(path = "banco" )
101
E-book gerado especialmente para 


## Página 118

7.4. ExceçõesePython3.3+ CasadoCódigo
banco_zip . close()
except (FileNotFoundError, PermissionError):
print ( "Algum problema ao ler o arquivo" )
7.4 Exceções e Python 3.3+
Apartirdoramo 3.3,umareorganiza çãonahierarquiadeexce çõesfoifeita.
Issovisoufacilitarotratamentodecasosespecíficoseremoveralgumasin-
consistênciasnalinguagem.
Ahierarquiacompletaestádescritanasequência.
BaseException
+-- SystemExit
+-- KeyboardInterrupt
+-- GeneratorExit
+-- Exception
+-- StopIteration
+-- ArithmeticError
| +-- FloatingPointError
| +-- OverflowError
| +-- ZeroDivisionError
+-- AssertionError
+-- AttributeError
+-- BufferError
+-- EOFError
+-- ImportError
+-- LookupError
| +-- IndexError
| +-- KeyError
+-- MemoryError
+-- NameError
| +-- UnboundLocalError
+-- OSError
| +-- BlockingIOError
| +-- ChildProcessError
| +-- ConnectionError
| | +-- BrokenPipeError
| | +-- ConnectionAbortedError
102
E-book gerado especialmente para 


## Página 119

CasadoCódigo Capítulo7. Tratandoerroseexceções:tornandoocódigomaisrobusto
| | +-- ConnectionRefusedError
| | +-- ConnectionResetError
| +-- FileExistsError
| +-- FileNotFoundError
| +-- InterruptedError
| +-- IsADirectoryError
| +-- NotADirectoryError
| +-- PermissionError
| +-- ProcessLookupError
| +-- TimeoutError
+-- ReferenceError
+-- RuntimeError
| +-- NotImplementedError
+-- SyntaxError
| +-- IndentationError
| +-- TabError
+-- SystemError
+-- TypeError
+-- ValueError
| +-- UnicodeError
| +-- UnicodeDecodeError
| +-- UnicodeEncodeError
| +-- UnicodeTranslateError
+-- Warning
+-- DeprecationWarning
+-- PendingDeprecationWarning
+-- RuntimeWarning
+-- SyntaxWarning
+-- UserWarning
+-- FutureWarning
+-- ImportWarning
+-- UnicodeWarning
+-- BytesWarning
+-- ResourceWarning
Em Python, toda exceção deve derivar em algum nível de
BaseException. As exce ções definidas pelo usuário, as chamadas
user-defined exceptionsgeralmentederivamde Exceptionousubclasses
comoaprópria OSError. EspecialmenteapartirdoPython3.3,parteda
103
E-book gerado especialmente para 


## Página 120

7.5. Executandocódigosenenhumaexce çãoforlevantada CasadoCódigo
hierarquiafoirefatoradaediversoserrosdemaisaltonívelforamcriados,
permitindocódigosmaisclarosquantoaotratamentodeerroimplementado.
7.5 Executando código se nenhuma exceção for
lev antada
Sepegarmososexemplosanteriores,podemosobservarque,seumadasduas
primeiraslinhaslevantarumerro,nãoconseguiremossaberexatamenteonde
foiqueeleaconteceu,anãoserqueolhemostodoo traceback.Podemosdizer
queométodo extractallsóvaiserexecutadocasoainstancia çãodaclasse
ZipFilenãodênenhumerro.Dessaforma,poderemosexpressar:
import zipfile
try :
banco_zip = zipfile . ZipFile( "saida.zip" )
except (FileNotFoundError, PermissionError):
print ( "Algum problema ao ler o arquivo" )
else :
banco_zip . extractall(path = "banco" )
Obloco elsegarantiuque extractallsejaexecutadosomentecasoa
operaçãoanterior–deaberturadoarquivo–nãolevanteumaexceção.Aqui,
expressamosqueométodo extractalldependedeumarquivoválido
aberto,quevemdachamadaaoconstrutor ZipFile.
Éclaroque,dentrodobloco else,achamadadométodotambémpode
gerarumerro. Oimportanteésempreterconsciênciaaodecidirmossobre
aimplementaçãodotratamentodeerros.Muitasvezesoempregodo else
podetornarocódigomaisclaro.
7.6 Ações de limpeza
Quandotrabalhamoscomcódigosquepodemgerarexce ções,muitasvezes
estamosmanipulando recursosabertosanteriormente(conexãocombanco
dedados,porexemplo),equeremosgarantirqueelessejamfinalizados(ou
fechados)independentedaocorrência,enãodealgumaexce ção. Paraisso,
104
E-book gerado especialmente para 


## Página 121

CasadoCódigo Capítulo7. Tratandoerroseexceções:tornandoocódigomaisrobusto
temosapalavrareservada finallyparadefinirumblocoquesempreserá
executado,permitindoqueessetipodecódigochameosmétodosdefinali-
zaçãoelibera çãocorretamente.
As ações de limpeza(clean-up actions)serãoexecutadas sempre,indepen-
dentedeteremocorridoerrosounão.Seguindoalógicadonossoexemplo,
poderíamosterumcódigosemelhanteaoaseguir:
import zipfile
banco_zip = None
try :
banco_zip = zipfile . ZipFile( "saida.zip" )
banco_zip . extractall(path = "banco" )
except PermissionError:
print ( "Algum problema ao extrair o arquivo" )
finally :
banco_zip . close()
Assim,garantimosque banco_zip.close()sempresejaexecutado,
nãodeixandoarquivosabertosnonossoprograma.
7.7 Comando raise : lev antando exceções
Nodomíniodanossaaplica ção,existem3tiposdedados,cadaumrepre-
sentadonosarquivosdemetadados, como: ‘bigint’, ‘varchar’e
‘numeric’.Qualquervaloréconsideradoinválido,alémdessestrês.
Essarestriçãodenegóciopodeserrepresentadapormeiodolan çamento
deumaexce ção,justamentequandoovalorforinválido. Essemétodoserá
privadonanossaAPI,masseráutilizadopordiversosoutrosmétodosque
recebemotipododadoeprecisamvalidarseestácorreto.Quandoqueremos
levantarumaexce ção,usamosocomando raisee,emseguida,passamos
umainstânciaouumaclassedeumaexce ção.Vejaoexemplo:
def validate_kind (kind):
if not kind in ( 'bigint' , 'numeric' , 'varchar' ):
raise Exception ( "Tipo inválido" )
105
E-book gerado especialmente para 


## Página 122

7.7. Comandoraise:levantandoexceções CasadoCódigo
Semprequeumainforma çãodetipoforlidadosarquivosdemetadados,
podemosexecutaressafun çãonovaloreverificarseeleévalido,diantedas
restriçõesdocódigo. Nonossoexemplo,usamosaprópria Exceptionda
bibliotecapadrão,maspoderíamosterusadouma user-defined exception.
Omaisimportanteéqueaexce çãolevantadasejacoerentecomasitua ção.
Vejaumavaria çãodocódigoreferenciandoumaclassedeexce çãodefi-
nidaporusuário:
class InvalidDataTypeException ( Exception ):
pass
def validate_kind (kind):
if not kind in ( 'bigint' , 'numeric' , 'varchar' ):
raise InvalidDataTypeException
Levantandoumamesmaexce çãotratada
Emalgunscasos,onossocódigoquerapenasterconhecimentodeque
umaexceçãofoilevantada,porém,quercontinuarpropagando-aparaocó-
digocliente.Outroexemplosãofiltrosdeaplica çõesweb,logandoexce ções,
masnãoescondendodorestodocódigo.
Vejaocódigoaseguir:
class InvalidDataTypeException ( Exception ):
pass
def validate_kind (kind):
if not kind in ( 'bigint' , 'numeric' , 'varchar' ):
raise InvalidDataTypeException
try :
validate_kind( 'invalid type' )
except Exception as e:
print ( "Peguei o erro mas vou repassa-lo" )
raise e
Nessecaso,ocódigoquechamaotrechoanteriorcontinuarecebendoa
exceçãolevantadapelafun ção validate_kind.Essetipodecódigoémuito
106
E-book gerado especialmente para 


## Página 123

CasadoCódigo Capítulo7. Tratandoerroseexceções:tornandoocódigomaisrobusto
comumquandoqueremosapenassaberqueumdeterminadoerroaconteceu,
masnãoqueremosafetarofluxodoprogramacomumtratamentomaises-
pecífico.
7.8 Exemplo de um tratamento de erros mais ro -
busto em Python
Conhecendomelhoromecanismodetratamentodeexce çõesemPython,po-
deríamosterescritoafun ção main()emnossoprimeiroprogramadocapí-
tulo4,daseguinteforma:
# coding: utf-8
import io
import sys
import urllib.request as request
BUFF_SIZE = 1024
def download_length (response, output, length):
times = length // BUFF_SIZE
if length % BUFF_SIZE > 0 :
times += 1
for time in range (times):
output . write(response . read(BUFF_SIZE))
print ( "Downloaded %d" % (((time * BUFF_SIZE) / length) *100 ))
def download (response, output):
total_downloaded = 0
while True :
data = response . read(BUFF_SIZE)
total_downloaded += len (data)
if not data:
break
out_file . write(data)
print ( 'Downloaded {bytes}' . format( bytes = total_downloaded))
107
E-book gerado especialmente para 


## Página 124

7.9. Conclusão CasadoCódigo
def main ():
response = request . urlopen(sys . argv[ 1 ])
out_file = io . FileIO( "saida.zip" , mode = "w" )
content_length = response . getheader( 'Content-Length' )
try :
if content_length:
length = int (content_length)
download_length(response, out_file, length)
else :
download(response, out_file)
except Exception as e:
print ( "Erro durante o download do arquivo {}"
. format(sys . argv[ 1 ]))
finally :
out_file . close()
response . close()
print ( "Fim" )
Agrandediferen çadessaversãoparaaversãosemtratamentodeerrosé
queumamensagemamigáveléescritanasaídapadrão,casoocorraalguma
exceçãonafun çãodedownloadexecutadaenenhumrecursosejamantido
aberto,mesmoemsitua çãodeexce ção.Comacláusula finally,garanti-
mosqueosdoisrecursosabertossejamfechados,independentedaocorrência
deerrosounão.
7.9 Conclusão
Omecanismodeexce çõesemPythonnãoétãodiferentedeoutraslingua-
gens,easintaxetambémébemfamiliar,decertaforma.Basicamente,temos
ocomando/bloco try/exceptcomcláusulasopcionais elsee finally.
Aexistênciadeumahierarquiatambémécomumemoutraslinguagense
nãoémuitodiferenteemPython. Tambémnãoexistenenhumaexigência
emtempodecompila çãoouexecu çãoquandotratamosdeterminadasexce-
ções. Vimoscomolevantarexce çõeseatémesmocomorepassá-lasaoutro
108
E-book gerado especialmente para 


## Página 125

CasadoCódigo Capítulo7. Tratandoerroseexceções:tornandoocódigomaisrobusto
código.
Agora, já podemos criar tratamentos de erro elaborados e, por con-
sequência,programasmaisrobustos. Éimportantesaberempregaroque
existecorretamente. Aolongodolivro,outrosexemplosmostrarãotrata-
mentodeexce ções,eexplicaremosamotiva çãoparaaimplementa ção.
Nopróximocapítulo,vamosver classes. Pythontemumbomsuporte
paraotrabalhocomclasseseobjetos,oparadigmaOrienta çãoaObjetos.Po-
rém,porcaracterísticasdalinguagem,acabamostendomuitosdetalhesque
precisamserabordadoscomcalmaparamelhorcompreensão.
109
E-book gerado especialmente para 


## Página 126

E-book gerado especialmente para 


## Página 127

Capítulo8
TestesemPython:umaprática
saudável
Emminhaopinião,aprenderacriarostesteslogocedocontribuiparaque
odesenvolvedorcrieaculturadeescrevercódigocomtestes,depreferência,
sempre.
Pythonpossuiumecossistemamuitoricodeferramentasdeteste.Para
começar,omódulodetestes unittestjáestánabibliotecapadrão,inclusive
comummódulode mockingem unittest.mock.Ouseja,sevocêtemo
interpretadorinstalado,játemtudonecessárioparaescrevercódigosdeteste.
Dopoucocódigoqueacumulamosatéagora,temosalgunstestesunitá-
riosbemsimplesaseremfeitoseoutrosquevãoexigirmockseoutrosrecur-
sos.Vamosanalisarcasoacaso.
Aideiadestecapítuloépassarobásicodopacote unittest,queédistri-
E-book gerado especialmente para 


## Página 128

8.1. CriandooprimeiroTestCase CasadoCódigo
buídonabibliotecapadrão.Porterumecossistemadetestesrico,elepermite
testesatémesmosemousodessepacote. Outrapráticacomuméusar T est
Runnersparapouparotrabalhodeconfigurarprogramaticamenteassuítese
testesquerodarão.
Nestecapítulo,vamosvercomocriarcódigodetestes,comorodá-lose
algunsoutrosdetalhesrelacionados.
8.1 Criando o primeiro TestCase
Omódulo unittesttemodesigninspiradono Junit,ferramentatradi-
cionaldetestesemJava.Oprimeiropassoparafazermosumtestedaforma
maistradicionalécriarumaclassequeherdade unittest.TestCase.
Vamoscriarumcasodetestesparaaclasse Columndonossoaplica-
tivo. Essaclassepossuiummétodoconstrutoreumdedomínio,chamado
validate().Faremosotestenasequência.
RelembrandoaclasseColumn
Umaspectomuitoimportantenonossoaplicativoéa consistência.Que-
remosqueosdadoslidosestejamemconformidadecomassuasdescri ções.
Seumatributotemtipo bigint,entãodeveaceitarapenasvaloresinteiros.
Esseaspectonosmotivaacriaronossoprimeiroteste.
Onossoprimeiroalvoseráaclasse Column,que,alémdeguardaros
atributos,éresponsávelporvalidarostipossuportadospelonossoprograma.
Osparâmetrossãoonomedotipoeumvalor.Seovalorforcompatívelcom
otipo,afun çãoretorna True. Porexemplo:ointeiro 1000écompatível
comotipo ‘bigint’,masnãocom ‘varchar’.
Vejaocódigo:
import decimal
import unittest
class Column :
def __init__ ( self , name, kind, description = "" ):
self . _name = name
self . _kind = kind
112
E-book gerado especialmente para 


## Página 129

CasadoCódigo Capítulo8. TestesemPython:umapráticasaudável
self . _description = description
@staticmethod
def validate (kind, data):
if kind == 'bigint' :
if isinstance (data, int ):
return True
return False
elif kind == 'varchar' :
if isinstance (data, str ):
return True
return False
elif kind == 'numeric' :
try :
val = decimal . Decimal(data)
except :
return False
return True
Agora,temosquecriartestesparagarantirqueocomportamentoespe-
radoaconteça.Aqui,separeiotestedafun ção validate()emtrêspartes,
mastambémpoderíamosterapenasumafun çãodeteste.Vejaocódigo:
import decimal
import unittest
class Column :
def __init__ ( self , name, kind, description = "" ):
self . _name = name
self . _kind = kind
self . _description = description
@staticmethod
def validate (kind, data):
if kind == 'bigint' :
if isinstance (data, int ):
return True
return False
elif kind == 'varchar' :
113
E-book gerado especialmente para 


## Página 130

8.2. Rodandoumarquivocomtestes CasadoCódigo
if isinstance (data, str ):
return True
return False
elif kind == 'numeric' :
try :
val = decimal . Decimal(data)
except :
return False
return True
class ColumnTest (unittest . TestCase):
def test_validate_bigint ( self ):
self . assertTrue(Column . validate( 'bigint' , 100 ))
self . assertTrue( not Column . validate( 'bigint' , 10.1 ))
self . assertTrue( not Column . validate( 'bigint' , 'Texto' ))
def test_validate_numeric ( self ):
self . assertTrue(Column . validate( 'numeric' , 10.1 ))
self . assertTrue(Column . validate( 'numeric' , 100 ))
self . assertTrue( not Column . validate( 'numeric' , 'Texto' ))
def test_validate_varchar ( self ):
self . assertTrue(Column . validate( 'varchar' , 'Texto' ))
self . assertTrue( not Column . validate( 'varchar' , 100 ))
self . assertTrue( not Column . validate( 'varchar' , 10.1 ))
if __name__ == "__main__" :
unittest . main()
Primeiro,criamosumaclassedetestechamada casodeteste (testcase).
Essaclassedeveherdarobrigatoriamentede unittest.TestCase.Depois,
chamamosafun ção main()domódulo unittest.
Aseguir,veremoscomoinvocaromecanismodetestes.
8.2 Rodando um arquivo com testes
Porenquanto, porconveniência, vamoscolocarnomesmoarquivoocó-
digo da classeColumne o testeColumnTest. Salve o arquivo como
114
E-book gerado especialmente para 


## Página 131

CasadoCódigo Capítulo8. TestesemPython:umapráticasaudável
test_column.py.Rode-o:
$ python test_column.py
...
-----------------------------------------------------------------
Ran 3 tests in 0.001s
OK
Todosostestesrodamcomsucesso.Vamosentendertudooqueaconte-
ceupararodá-los,analisandoostrechosdecódigoseparadamente.
Testedechamandanalinhadecomando
Ocódigoaseguir,queficanofinaldoarquivo test_column.py,éver-
dadeiro,ouseja, __name__éigualàstring "__main__”,portantoacha-
mada unittest.main()éfeita.
Afunção main()domódulo unittestprocuranoprópriomódulo
__main__–oquefoichamado–porclassesqueherdamde TestCasee
executaostestes.Outrasclassesdetestesimportadasporessearquivotam-
bémseriamexecutadas.
Vejaocódigoquefazoquefoidescritologoaseguir:
>>> if __name__ == "__main__" :
... unittest . main()
Códigodoteste
Aoutraparterelevanteéadefini çãodo testcasequeéencontradoeexe-
cutado.
# coding: utf-8
from domain import Column
class ColumnTest (unittest . TestCase):
def test_validate_bigint ( self ):
self . assertTrue(Column . validate( 'bigint' , 100 ))
self . assertTrue( not Column . validate( 'bigint' , 10.1 ))
115
E-book gerado especialmente para 


## Página 132

8.2. Rodandoumarquivocomtestes CasadoCódigo
self . assertTrue( not Column . validate( 'bigint' , 'Texto' ))
def test_validate_numeric ( self ):
self . assertTrue(Column . validate( 'numeric' , 10.1 ))
self . assertTrue(Column . validate( 'numeric' , 100 ))
self . assertTrue( not Column . validate( 'numeric' , 'Texto' ))
def test_validate_varchar ( self ):
self . assertTrue(Column . validate( 'varchar' , 'Texto' ))
self . assertTrue( not Column . validate( 'varchar' , 100 ))
self . assertTrue( not Column . validate( 'varchar' , 10.1 ))
Aqui,doisdetalhessãoimportantes:apenasmétodoscomprefixo test_
serãoexecutadopelomecanismodetestes,eelestêmdeestaremclassesque
herdamde TestCase.Cadamétodoencontradoqueatendeessesrequisi-
toséexecutadocomoumteste. Nonosso testcase,temos3métodosqueos
atendeme,porisso,nasaídaéinformadoque3testesrodaramcomsucesso.
AAPIdetestesficanaprópriainstância– self–docasodetesteeéela
quepossuiosmétodosdeasser ção.Asserçãoéonomedadoàverifica çãode
valores,quegeraumerronostestecasosejafalsa.
Aseguir,vocêpodeveralgunsdosmétodosqueestãodisponíveis. Os
maisbásicossão:
self . assertEqual(a, b) # a == b
self . assertNotEqual(a, b) # a != b
self . assertTrue(x) # bool(x) is True
self . assertFalse(x) # bool(x) is False
self . assertIs(a, b) # a is b
self . assertIsNot(a, b) # a is not b
self . assertIsNone(x) # x is None
self . assertIsNotNone(x) # x is not None
self . assertIn(a, b) # a in b
self . assertNotIn(a, b) # a not in b
self . assertIsInstance(a, b) # isinstance(a, b)
self . assertNotIsInstance(a, b) # not isinstance(a, b)
116
E-book gerado especialmente para 


## Página 133

CasadoCódigo Capítulo8. TestesemPython:umapráticasaudável
8.3 API de linha de comando para testes
Noexemploanterior,consideramosqueachamada unittest.main()ini-
ciaoprocessoderodartestes.Porém,existeumalimita çãomuitoruimnessa
formadeinicia ção:paraostestesrodarem,temosquepassaronomedoar-
quivonalinhadecomandoparaqueelessejamexecutados.
Esequiséssemosrodartestesdeváriosmódulos?
Felizmente,temosumaAPIdelinhadecomandoquepermitequeostes-
tessejamdescobertoseexecutados.EssaAPIaindapossuiumasériedepa-
râmetrosqueatendemaváriasnecessidades.
Para simular aunittest.main(), você precisa apenas informar o
nomedomódulo.Lembre-sedequequalquer TestCasedeclaradoouim-
portadonomóduloespecificadorodará. Nonossocaso,temosapenasum
casodetestecomtrêsmétodos.
$ python -m unittest test_column -v
test_validate_bigint (test_column.ColumnTest) ... ok
test_validate_numeric (test_column.ColumnTest) ... ok
test_validate_varchar (test_column.ColumnTest) ... ok
-----------------------------------------------------------------
Ran 3 tests in 0.000s
OK
Você pode especificar um caso de teste, como
test_column.ColumnTest, ou um método de um caso de teste, por
exemplo test_column.ColumnTest.test_validate_bigint.Vejao
exemplodosegundocaso:
$ python -m unittest
test_column.ColumnTest.test_validate_bigint -v
test_validate_bigint (test_column.ColumnTest) ... ok
-----------------------------------------------------------------
Ran 1 tests in 0.000s
OK
117
E-book gerado especialmente para 


## Página 134

8.3. APIdelinhadecomandoparatestes CasadoCódigo
Épossívelespecificarváriosmódulosdeumavez,apenaslistando-osse-
paradosporespa ço:
$ python -m unittest test_column test_data_table -v
test_add_relationship (test_data_table.DataTableTest) ... ok
test_add_reverse_relationship (test_data_table.DataTableTest)
... ok
test_validate_bigint (test_column.ColumnTest) ... ok
test_validate_numeric (test_column.ColumnTest) ... ok
test_validate_varchar (test_column.ColumnTest) ... ok
-----------------------------------------------------------------
Ran 5 tests in 0.001s
OK
Épossívelrodarocomando python -m unittest semmaisparâ-
metros,etodosostestesrodarem. Porém,naconfigura çãopadrão,existe
arestri çãodequeosarquivosdetestestenhamoprefixo test_, como
test_column.py.Vocêpodealteraressepadrãopassandoumparâmetro
paraosubcomando discover.Vejaoexemploquefuncionariacomoar-
quivoseelefosserenomeadopara column_test.py:
$ python -m unittest discover -p '*_test.py'
...
-----------------------------------------------------------------
Ran 3 tests in 0.000s
OK
Diantedessasop ções,talvezumbompontodepartidasejaadotaracon-
vençãopadrão:usaroprefixo test_echamarocomandosemparâmetros,
como python -m unittest .Destaforma,opróprio unittestprocu-
raráosmódulosdetesteeoscasosdetestesdefinidos,erodarátodoseles,
semexigirnenhumcódigo,alémdasclassesdecasodetestes.
Apesardemuitoflexível,controlarasconfigura çõespelalinhadeco-
mandonemsempreéoquequeremos. Emalgunscasos,queremosusaras
118
E-book gerado especialmente para 


## Página 135

CasadoCódigo Capítulo8. TestesemPython:umapráticasaudável
configuraçõesprogramáticasparamodificaraexecu çãodeetapasdessepro-
cessodeexecu çãodostestes. Umexemploclássicoéalteraroformatoda
saída.
8.4 API da biblioteca unittest
Algumascustomizaçõesnomecanismodetestesnãopodemserfeitaspela
linhadecomando.Porisso,o unittesttambémpossuitodaumaAPIpro-
gramáticaparaconfiguraçãoeexecu çãodomecanismodetestes.
Pelalinhadecomandonãoficatãoclaro,mastemosduasetapasbem
definidasnesseprocesso:descoberta/carregamentodostesteseexecu ção.
A descoberta/carregamento (discovery/ loading) é a etapa na
qualostestessãodescobertosecarregadospelo TestLoader. Oprin-
cipal objetivo dessa classe é ajudar com a criação das suítes de testes
unittest.suite.TestSuite. Podemoscriarumasuítecarregandodi-
retodeummódulodetestes.Vejaoexemplo:
import unittest
import test_column
suite = unittest . TestLoader() . loadTestsFromModule(test_column)
unittest . TextTestRunner(verbosity =2 ) . run(suite)
O método discover(start_dir, pattern=’test *.py’,
top_level_dir=None)procuraostestesemmódulos,buscando-osem
umdiretórioiniciale,recursivamente,naspastasdentrodele. Eletambém
retornaumasuítedetestes.
import unittest
suite = unittest . TestLoader() . discover( '.' )
unittest . TextTestRunner(verbosity =2 ) . run(suite)
Naetapadeexecu çãodostestes,oexecutor(ou Runner)precisadeum
objetodotiposuítedetestespararodar. Nonossoexemplo,escolhemosa
implementação TextTestRunnerpararodaranossasuíte.
119
E-book gerado especialmente para 


## Página 136

8.5. CustomizandosaídaparaHTML CasadoCódigo
>>> import unittest
>>> suite = unittest . TestLoader()
. loadTestsFromModule(test_column)
>>> unittest . TextTestRunner(verbosity =2 ) . run(suite)
test_validate_bigint (test_column . ColumnTest) ... ok
test_validate_numeric (test_column . ColumnTest) ... ok
test_validate_varchar (test_column . ColumnTest) ... ok
-----------------------------------------------------------------
Ran 3 tests in 0.001 s
OK
< unittest . runner . TextTestResult run =5 errors =0 failures =0>
TudooqueéfeitopelalinhadecomandopodeserfeitopormeiodaAPI,
manipulandoasclassesde loaderse runners.
Agrandediferen çaéqueagorapodemossubstituirasimplementa çõesda
bibliotecapadrãoporimplementa çõescustomizadas,econtrolaraindamais
omecanismo.
8.5 Customizando saída para HTML
Comojásabemosconfiguraromecanismodetestespararodardeacordo
comnossanecessidade,vamoscustomizá-loumpoucomaisparaexemplifi-
carcomopodemosempregaressafacilidade.
Emminhaopinião,afacilidadedecustomiza çãodomecanismodetestes
éumpontomuitofortedalinguagem. Emalgunscasos,podemosquerer
exportaroresultadodasuítedetestesparaalgumoutroprograma. Asaída
padrão,mesmotendoumaboapadroniza ção,nãoéflexívelcomoosformatos
JSON,ouatémesmo HTML.
Emvezdegerarum outputtexto,geraremosumcódigoHTMLque
poderáserabertononavegador. Paraisso,precisamosimplementarnossos
próprios runnerse TestResults.
Comovimos,o runneréoresponsávelporexibiroresultadodostestes
paraousuário.Oquefizemosfoiimplementarum runnerqueimprimeum
htmlcomoresultadodostestesemvezdasaídapadrão.Tambémprecisamos
120
E-book gerado especialmente para 


## Página 137

CasadoCódigo Capítulo8. TestesemPython:umapráticasaudável
deumaoutraclasseauxiliar HTMLResultquenospermiteexibir,nasaída,
maisinformaçõessobreostestesquenãofalharamougeraramerro.
Vamosnovamenteanalisarcadaparteseparadamentenasequência.
8.6 Implementando um TestRunner customi -
zado
Afun çãodo Runneréconfigurarum TestResulteexecutarostes-
tes,passandoo TestResultcomoparâmetro. Aexecu çãodostestesé
feitapormeiodachamada run()noobjeto test, queéumainstân-
ciade TestSuitedentrodométodotambémchamado run(),sóque
agora,do HTMLTestRunner.Essaexecu çãoinvocarádiversosmétodosno
TestResultparanotificarsobreostestescomsucesso,errosefalhas.
ParageraroHTML,iteramosnalista result.infos
import unittest
HTML = '''\
<html>
<head>
<title>unittest output</title>
</head>
<body>
<table>
{}
</table>
</body>
</html>'''
OK_TD = '<tr><td style="color: green;">{}</td></tr>'
ERR_TD = '<tr><td style="color: red;">{}</td></tr>'
class HTMLTestResult (unittest . TestResult):
def __init__ ( self , runner):
unittest . TestResult . __init__( self )
self . runner = runner
self . infos = []
121
E-book gerado especialmente para 


## Página 138

8.6. ImplementandoumTestRunnercustomizado CasadoCódigo
self . current = {}
def newTest ( self ):
self . infos . append( self . current)
self . current = {}
def startTest ( self , test):
self . current[ 'id' ] = test . id()
def addSuccess ( self , test):
self . current[ 'result' ] = 'ok'
self . newTest()
def addError ( self , test, err):
self . current[ 'result' ] = 'error'
self . newTest()
def addFailure ( self , test, err):
self . current[ 'result' ] = 'fail'
self . newTest()
def addSkip ( self , test, err):
self . current[ 'result' ] = 'skipped'
self . current[ 'reason' ] = err
self . newTest()
class HTMLTestRunner :
def run ( self , test):
result = HTMLTestResult( self )
test . run(result)
table = ''
for item in result . infos:
if item[ 'result' ] == 'ok' :
table += OK_TD . format(item[ 'id' ])
else :
table += ERR_TD . format(item[ 'id' ])
print (HTML . format(table))
return result
122
E-book gerado especialmente para 


## Página 139

CasadoCódigo Capítulo8. TestesemPython:umapráticasaudável
if __name__ == "__main__" :
suite = unittest . TestLoader() . discover( '.' )
HTMLTestRunner() . run(suite)
Onosso TestResult,chamadode HTMLTestResult,implementaal-
gunsmétodosqueserãochamadosnesseobjeto,deformaqueelesejaores-
ponsávelemguardarosresultadosdostestes.Essesmétodoscompõemum
protocolodenotificaçãodosresultados.Paraonossoexemplo,escolhemosos
métodos startTest(test), addSuccess(test), addError(test),
addFailure(test)e addSkip(test).Alémdisso,usamosalgumasva-
riáveisdeinstânciaeummétodoauxiliarparaimplementaressatarefa.
O newTestéummétodoauxiliarquefoicriadoparapegaroúltimoteste
modificadoecolocaremumalista,queseráusadapelonosso runner.Omé-
todo startTest(test)éexecutadoumpoucoantesdeoteste–contido
noparâmetro test–serexecutado.Nessemomento,pegamosoidentifica-
dordotesteeguardamosnodicionário current.
Ospróximos4métodossãochamadosparanotificaroresultadodaexe-
cuçãodoteste. Cadafun çãoestáassociadaaumevento,nocaso: sucesso,
erro,falhaoupulodoteste.Elestambémcolocamoresultadonodicionário
currentechamam newTestparaqueessetestesejaadicionadonalistade
resultadoseoespa çoparaopróximotestesejaaberto.
class HTMLTestResult (unittest . TestResult):
def __init__ ( self , runner):
unittest . TestResult . __init__( self )
self . runner = runner
self . infos = []
self . current = {}
def newTest ( self ):
self . infos . append( self . current)
self . current = {}
def startTest ( self , test):
self . current[ 'id' ] = test . id()
123
E-book gerado especialmente para 


## Página 140

8.6. ImplementandoumTestRunnercustomizado CasadoCódigo
def addSuccess ( self , test):
self . current[ 'result' ] = 'ok'
self . newTest()
def addError ( self , test, err):
self . current[ 'result' ] = 'error'
self . newTest()
def addFailure ( self , test, err):
self . current[ 'result' ] = 'fail'
self . newTest()
def addSkip ( self , test, err):
self . current[ 'result' ] = 'skipped'
self . current[ 'reason' ] = err
self . newTest()
if __name__ == "__main__" :
suite = unittest . TestLoader() . discover( '.' )
HTMLTestRunner() . run(suite)
Agora,usamosométodo discover()dasuíteparadescobrirostestes
nodiretóriocorrente,eaexecutamoscomnosso HTMLTestRunner.Asaída
éumcódigoHTML,emtexto,comoresultadodostestes.
<html>
<head>
<title> unittest output </title>
</head>
<body>
<table>
<tr>
<td style= "color: green;" >
test_domain.ColumnTest.test_validate_as_static_method
</td>
</tr>
</table>
</body>
</html>
124
E-book gerado especialmente para 


## Página 141

CasadoCódigo Capítulo8. TestesemPython:umapráticasaudável
Umasaídaemhtmlrenderizado:
Fig.8.1:Saídahtml
Esseexemplofoifeitoparademonstrarumpoucomaisdaflexibilidade
domecanismodetesteseparaexplorarumpoucomaisaAPIprogramática
dopacote unittest.Aseguir,vamosfocaremcomocriarocódigoque,de
fato,vaifazerostestesnoseuprogramaoubiblioteca.
8.7 Testando erros : quando o código joga exce-
ções
Muitasvezes,temosummétodooufun çãoquepodejogarumaexce çãoem
determinadoscasos. Umafunçãoretornaumresultadocasoosparâmetros
estejamcorretos,eumerrocasoosparâmetrosnãosejamválidos.Oidealé
queambososcasossejamtestados.
Sevoltarmosànossaaplica ção,naclasse DataTablepodemosverqueo
método add_column(name, kind) podejogarumaexce çãocaso kind
sejainválido.Vamosrefatoraressemétodoparaqueelejogueaexce çãocaso
kindnãosejaumtipoconhecido.Depoisvamoscriarotesteparaométodo
add_column().Nocódigoaseguir,omitimososmétodosquenãosãousa-
dosnoteste.
from domain import Column
class DataTable :
def add_column ( self , name, kind, description = "" ):
self . _validate_kind(kind)
column = Column(name, kind, description = description)
self . _columns . append(column)
return column
125
E-book gerado especialmente para 


## Página 142

8.7. Testandoerros:quandoocódigojogaexce ções CasadoCódigo
def _validate_kind ( self , kind):
if not kind in ( 'bigint' , 'numeric' , 'varchar' ):
raise Exception ( "Tipo inválido" )
Agora,temosdoiscasosparatestar: umquando kindéumdostipos
suportados,eoutroquandonãofor.Vamosverostestes:
from domain import Column
class DataTable :
def add_column ( self , name, kind, description = "" ):
self . _validate_kind(kind)
column = Column(name, kind, description = description)
self . _columns . append(column)
return column
def _validate_kind ( self , kind):
if not kind in ( 'bigint' , 'numeric' , 'varchar' ):
raise Exception ( "Tipo inválido" )
class DataTableTest (unittest . TestCase):
def test_add_column ( self ):
self . assertEqual( 0 , len ( self . table . _columns))
self . table . add_column( 'BId' , 'bigint' )
self . assertEqual( 1 , len ( self . table . _columns))
self . table . add_column( 'value' , 'numeric' )
self . assertEqual( 2 , len ( self . table . _columns))
self . table . add_column( 'desc' , 'varchar' )
self . assertEqual( 3 , len ( self . table . _columns))
def test_add_column_invalid_type ( self ):
a_table = DataTable( 'A' )
self . assertRaises( Exception ,
a_table . add_column, ( 'col' , 'invalid' ))
O assertRaises precisa receber o método que será
126
E-book gerado especialmente para 


## Página 143

CasadoCódigo Capítulo8. TestesemPython:umapráticasaudável
testado e seus argumentos. Aqui, internamente, dentro de
assertRaises(), temos a aplicação prática do conceito depac-
king, pois o terceiro argumento de assertRaises será usado na
chamada do método table.add_column. Vamos ter algo como
table.add_column(*(‘col’, ‘invalid’)) sendo executado,
que, no fundo, é o mesmo quetable.add_relationship(‘col’,
‘invalid’).
Outra forma de testar que esse erro é levantado é usando um bloco
try/exceptcombinadocomafun ção fail()do TestCase. Vejao
exemploedepoisaexplica ção,aseguir:
class DataTableTest (unittest . TestCase):
def test_add_column_invalid_type_fail ( self ):
a_table = DataTable( 'A' )
error = False
try :
a_table . add_column( 'col' , 'invalid' )
except :
error = True
if not error:
self . fail( "Chamada não gerou erro, mas deveria" )
Como o métodoadd_column levanta um erro, pois está com os
parâmetros inválidos, a variávelerror passa a ser True, e a linha
self.fail(msg)nãoéexecutada.Seoparâmetroforválido,ométodonão
levantaerro,eavariável errorficacomvalor False,executando,assim,a
chamadaaométodo fail(msg).Esteéoobjetivodesseteste:queremoster
certezadequeachamadagerouumerro.
Achamadafazcomqueotestefalheeexibaamensagempassadacomo
parâmetro.Éumaoutraformadetestarsitua çõesemqueerrosdeveriamser
levantados.
Aindaexisteoutramaneira,queveremosmaisàfrente,poisintroduzum
comandoaindanãotrabalhado.
127
E-book gerado especialmente para 


## Página 144

8.8. Inicializaçãoefinaliza ção:setUpetearDown CasadoCódigo
8.8 Inicialização e finalização : setUp e tear-
Down
Umprincípioimportanteemtesteséodeisolamento. Deveexistirumiso-
lamentoentreosambientesdeteste,emcadamétododeteste. Ouseja,as
mudançasdeambiente–comocria çãodevariáveis,altera çõesemobjetos
importadoseoutras–nãodevemservistasporoutrométododetesteque
nãosejaoqualasrealizou.
Poroutrolado,écomumquemuitostestesprecisemdeumavariáveldo
objetoquepossivelmenteestásendotestado,quesempreéiniciadaemum
estadoinicialigual.Peloprincípiodoisolamento,seumtestemodificaovalor
dessavariável,elanãopoderiaestarmodificadanoiníciodopróximoteste.
Vejaoexemplodedoistestesqueusamumainicializa çãoidênticadeob-
jeto:
class DataTableTest (unittest . TestCase):
def test_add_column ( self ):
table = DataTable( 'A' )
assertEqual( 0 , len ( self . table . _columns))
table . add_column( 'BId' , 'bigint' )
assertEqual( 1 , len ( self . table . _columns))
table . add_column( 'value' , 'numeric' )
assertEqual( 2 , len ( self . table . _columns))
table . add_column( 'desc' , 'varchar' )
assertEqual( 3 , len ( self . table . _columns))
def test_add_column_invalid_type ( self ):
table = DataTable( 'A' )
assertRaises( Exception ,
self . table . add_column, ( 'col' , 'invalid' ))
Repareque,noexemploanterior,primeiramentetodosostestesprecisam
deum DataTablenomesmoestadoinicial.Aqui,respeitamosoisolamento,
jáqueoambientedecadatestetemsuavariávelcriadanoseuinício,masse
128
E-book gerado especialmente para 


## Página 145

CasadoCódigo Capítulo8. TestesemPython:umapráticasaudável
tivéssemosmaismétodosdetestes,teríamosmaislinhasiguais. Vamosver
comopodemosmelhorarissoaseguir.
Osmétodos setUpe tearDownsãoexecutados,respectivamente,antes
edepoisdecadatesterodar.Comeles,podemosreaproveitarcódigodeinici-
alizaçãoefinaliza çãoqueserãorodadosparacadamétododeteste.Agrande
vantagemqueelesnosdãoéquepodemoscriarumcódigoúnicodeinici-
alizaçãoefinaliza çãoparacadamétododeteste. Issonospermitetantoter
oisolamentoquantoaelimina çãodecódigoduplicado. Vejaaseguircomo
podemosmelhoraroexemploanterior:
class DataTableTest (unittest . TestCase):
def setUp ( self ):
self . table = DataTable( 'A' )
def test_add_column ( self ):
self . assertEqual( 0 , len ( self . table . _columns))
self . table . add_column( 'BId' , 'bigint' )
self . assertEqual( 1 , len ( self . table . _columns))
self . table . add_column( 'value' , 'numeric' )
self . assertEqual( 2 , len ( self . table . _columns))
self . table . add_column( 'desc' , 'varchar' )
self . assertEqual( 3 , len ( self . table . _columns))
def test_add_column_invalid_type ( self ):
self . assertRaises( Exception ,
self . table . add_column, ( 'col' , 'invalid' ))
Emvezdecriarumainstânciadentrodetodososmétodos,usamosuma
criadanométodo setUp,quesempreestánomesmoestadoantesdaexecu-
çãodecadamétodo.Foiexatamenteoquefizemosnoexemploanterior.
Ométodo tearDown()éexecutadoapóscadamétododeteste. Uma
açãomuitocomuméfechararquivosouconexõescombancodedados,mas
váriasoutrastarefaspodemserexecutadasnele. Nofinaldascontas,para
cadamétododetesteexecutado,temosumasequênciacomo: setup(),
129
E-book gerado especialmente para 


## Página 146

8.9. Açõesdelimpezanostestesunitários:cleanupactions CasadoCódigo
test_minha_funcao(), tearDown().Éimportantequeesseprotocolo
sejausadosemprequandoforvantajoso,tantoparaoisolamentoquantopara
adiminuiçãodecódigorepetido.
ExceçõesnométodosetUp()
Umdetalheimportanteéque,seporacasoométodo setUp()levantar
algumerronãotratado,ométodo tearDown()não seráexecutado. Isso
podenostrazerproblemas!
Imaginequevocêtemumteste(deintegra ção)queabreconexãocom
duasfontesdedados.Poderíamoscolocarno setUp()acriaçãodosobjetos
quenosdãoacessoaessesrecursos. Oproblemaéqueabrimosoprimeiro
recursocomsucesso,mas,senahoradeabrirmososegundo,ocódigolevan-
tarumaexce ção,elenãoseráexecutadocasoafinaliza çãodosrecursosesteja
no tearDown().
Vocêpoderiaresolverissocomumbloco try/except,porém,existe
umaformamaisadequadadetrataressassitua ções.Felizmente,háumama-
neiraderodaralgumafun ção,mesmoqueométodo setUplevanteerros
nãotratados.
8.9 Ações de limpeza nos testes unitários : cle-
anup actions
Nestapartedolivro,ofocoestámaisemmostrarofuncionamentodoque
discutiraaplica ção.Umamotiva çãofoidadaanteriormente,naqualtemosa
hipótesedequeumrecursoquedeveriaserfinalizadono tearDown()acaba
nãoosendo,poispodeterocorridoumerronãotratadono setUp().
Paraqueissonãosejaumproblema,podemosconfigurara çõesdelim-
peza( cleanup actions),queserãoexecutadasmesmoqueumerrotenhasido
levantadono setUp()ouno tearDown().
Vejaoexemploaseguir:
import unittest
class DataTableTest (unittest . TestCase):
130
E-book gerado especialmente para 


## Página 147

CasadoCódigo Capítulo8. TestesemPython:umapráticasaudável
def setUp ( self ):
self . out_file = open ()
def test_add_column ( self ):
pass
def tearDown ( self ):
print ( "tearDown" )
Esseexemplonuncaexecutaráométodo tearDown(),porqueacha-
madaàfun ção open()levantaumerro.Nessasitua ção, tearDown()não
roda. Assim,precisamosadicionarumaa çãodelimpeza. Essasa çõesserão
executadassempredepoisdo tearDown(),mesmoqueelenãorode.Vejao
exemploatualizado:
import unittest
class DataTableTest (unittest . TestCase):
def setUp ( self ):
self . addCleanup( self . my_cleanup, ( 'cleanup executado' ))
self . out_file = open ()
def my_cleanup ( self , msg):
print (msg)
def test_add_column ( self ):
pass
def tearDown ( self ):
print ( "Nunca executado" )
Rodenalinhadecomandoevejaoresultado:
$ python -m unittest -v 08_10_cleanup.py
cleanup executado
E
=================================================================
ERROR: test_add_column (08_10_cleanup.DataTableTest)
-----------------------------------------------------------------
131
E-book gerado especialmente para 


## Página 148

8.10. Mocks/Stubs:outraabordagemdetestesunitários CasadoCódigo
Traceback (most recent call last):
File
"/Users/felipecruz/Projects/livros/exemplos/08_10_cleanup.py",
line 6, in setUp
self.out_file = open()
TypeError: Required argument 'file' (pos 1) not found
-----------------------------------------------------------------
Ran 1 test in 0.001s
FAILED (errors=1)
Vemosqueastring cleanup executado éimpressanatela.Issopor-
queométodo my_cleanup()foiexecutado,jáquefoiregistradocomouma
cleanup actionnachamada self.addCleanup(),passandocomoparâme-
troainstânciadométododelimpeza self.my_cleanupequalparâmetro
my_cleanupseráchamado.
Reparequeoerrocontinuasendoexibido.Casoelesejaajustado,nossa
açãodelimpezaaindaseráexecutada.Omaiscomumnessesmétodoséfe-
chararquivos, file descriptors,conexõescombancoseoutrosrecursosque
precisam,explicitamente,serfechadosouliberados.
8.10 Mocks/Stubs: outra abordagem de testes
unitários
Atéomomento,focamosemtodososnossostestesemcódigo,quepodemos
chamarde código de domínio.Ocódigodedomínioéondeestãoasregrasque
compõemodomíniononossoprograma,que,nocaso,sãodados. Porém,
temosumpoucodecódigode infraestrutura,ondefizemosumdownload
deumservidorremotoedepoisextraímosoconteúdodoarquivoemuma
pastalocal. Essapartedocódigoéumpoucomaisdelicadadetestar,pois
dependemos,porexemplo,deumaconexãodeinternetpararealizarumteste
completodedownloaddeumarquivodeumservidorremoto.
Nonossocódigodeinfraestruturatemosumafun çãoque,daformacomo
foifeita,sópoderiasertestadacomumteste funcional.Essafun çãoprecisa
deumobjeto responsequetemarespostadoservidorHTTP,comocon-
132
E-book gerado especialmente para 


## Página 149

CasadoCódigo Capítulo8. TestesemPython:umapráticasaudável
teúdodoarquivocujodownloadqueremosfazer.Sefossecriadoumobjetode
responseexplicitamentenocasodeteste,eelefossepassadoparaafun ção
download_length(),estaríamoscriandoum teste funcionalqueexecuta
emtotalidadeafuncionalidade,queérealizarodownloaddeumarquivo.
Mas,emalgunscasos,queremostestarcódigosemumambientefunci-
onal(semconexãocominternet,porexemplo)edeforma isolada.Existem
algumasalternativasparaotestefuncional. Veremosumadelasondemo-
dificamosocomportamentodealgunsobjetosduranteostestes. Comisso,
vamosisolarocódigotestadodesuasdependências. Nofinal,teremosum
testeunitário.
Paraqueissofiquemaisclaro,vamosanalisaranossafun çãodedownload
epensarsobrequallógicaqueremostestarnoseucódigo.
Alógicamaisimportantedocódigodedownloadéaquantidadedeve-
zesqueelechamaosmétodos read()e write(). Seonúmerodevezes
emqueessesmétodossãochamadosforcorreto,afun çãofazodownload
corretamente.
Secriamos mocksparaosobjetos responsee output,podemosve-
rificarquantasvezesosmétodosforamchamadosecomquaisparâmetros.
Com mocks,criaremosobjetosquesecomportamcomoqueremos,edepois
poderemosfazerperguntasaelesparatestarseforamchamadosdaforma
esperada.Assim,podemostestarafun ção download_lengthsemterque
criarumobjetorealde responseesemdependerdeumaconexãocoma
internet.
MocksversusStubs
Tecnicamente, mockse stubssãodiferentes. Quandoqueremosapenas
fazercomquedeterminadosobjetostenhamcomportamentospreestabeleci-
dos,oqueprecisamossãode stubs.Os mockstambémpodemtercomporta-
mentospreestabelecidos,maselestambémtêmexpectativasaseremcumpri-
das.
Quandocriamosum mocketrocamosumadependênciadocódigoaser
testadoporele,queremosdepoisverificarseessecomponente mockadofoi
chamadodemaneiraadequada.Destaforma,quandoocriamos,énecessário
configuraressasexpectativasnele,poisaverifica çãodelasfarápartedonosso
133
E-book gerado especialmente para 


## Página 150

8.10. Mocks/Stubs:outraabordagemdetestesunitários CasadoCódigo
teste.Sevocêusarum mock,masnãoconfigurarnemverificarnenhumaex-
pectativa,vocêestará,naverdade,usandoum stub.Ambossãocomuns,mas
nonossocaso,vamosfocarumpoucomaisnos mocks.
No Python 3.3, o projetomock foi integrado dentro do módulo
unittest. Logo,temosquasetudooqueprecisamosjánabibliotecapa-
drão.
Vejaoexemploaseguir:
import unittest
from unittest import mock
BUFF_SIZE = 1024
def download_length (response, output, length):
times = length / BUFF_SIZE
if length % BUFF_SIZE > 0 :
times += 1
for time in range ( int (times)):
output . write(response . read(BUFF_SIZE))
print ( "Downloaded %d" % (((time * BUFF_SIZE) / length)
*100 ))
class DownloadTest (unittest . TestCase):
def test_download_with_known_length ( self ):
response = mock . MagicMock()
response . read = mock . MagicMock(side_effect = [ 'Data' ] *2 )
output = mock . MagicMock()
download_length(response, output, 1025 )
calls = [mock . call(BUFF_SIZE),
mock . call(BUFF_SIZE)]
response . read . assert_has_calls(calls)
calls = [mock . call( 'Data' ),
mock . call( 'Data' )]
output . write . assert_has_calls(calls)
134
E-book gerado especialmente para 


## Página 151

CasadoCódigo Capítulo8. TestesemPython:umapráticasaudável
Podemos ver que existem duas etapas bem claras: configuração dos
mockse, depoisdoteste, asasser ções. Naconfigura çãodo mockpara
response,primeirocriamosum MagicMocke,depois,outro MagicMock
paraométodosobreoqualqueremossaberquantasvezesfoichamado.
O mockdométodo read()podereceberosvaloresqueachamadaaele
retornará.Nonossocaso,cadachamadaretornaráastring ‘Data’,portanto,
oparâmetro side_effectspodeserumalistacomovalorrepetido,como
em [’Data’, ‘Data’] ou [’Data’]*2.
Paraocasodoobjeto output,queremostambémsaberquantasvezese
comquaisargumentosométodo writefoichamado.Comonãotemosque
configurarnenhumefeitocolateral( side effect),bastacriamosum mockpara
oobjeto output.
Depoisdeafun çãoserexecutadacomos mocks,conseguimospergun-
taraelessobreosmétodosqueforamexecutados. Comoqueremosverifi-
caronúmerodevezesemqueosmétodosforamexecutados,usamosomé-
todo assert_has_calls(calls)do mock.Nessecaso, callsseráuma
listade mock.call(arg). Repareque mock.call(arg)recebeumar-
gumentoquedeveseraquelecomqueo mockinicialfoichamado.
Porexemplo,vamosverapenasumtrecho:
response = mock . MagicMock()
response . read = mock . MagicMock(side_effect = [ 'Data' ] *2 )
download_length(response, output, 1025 )
calls = [mock . call(BUFF_SIZE),
mock . call(BUFF_SIZE)]
response . read . assert_has_calls(calls)
Essetrechoverificase response.read()foichamadoduasvezescom
oargumento BUFF_SIZE.Se callstivessemaisumelemento,ouoargu-
mentofossediferentedopassadoparao mock,otestegerariaumerro.
Outrodetalhe:oqueépassadopara output.write()éoqueéretor-
nadopelo mockde response.read(). Nessecaso,específicamosquais
valoresretornarãoacadachamada.
135
E-book gerado especialmente para 


## Página 152

8.10. Mocks/Stubs:outraabordagemdetestesunitários CasadoCódigo
Amesmalógicavaleparaaasser çãono mockde output.write().
Queremosverificarseelefoichamadoduasvezes,comoparâmetro ‘Data’
emcadauma.
Outrafunçãodedownload
Nafunçãoquenãorecebeotamanho,acondi çãoqueterminaaleitura
éumretornode reponse.read()comumastringvazia. Podemosusar
novamenteoatributo side_effectparaajudarcomoteste.Vejaoexemplo
aseguir:
import unittest
from unittest import mock
BUFF_SIZE = 1024
def download (response, output):
total_downloaded = 0
while True :
data = response . read(BUFF_SIZE)
total_downloaded += len (data)
if not data:
break
output . write(data)
print ( 'Downloaded {bytes}' . format( bytes = total_downloaded))
class DownloadTest (unittest . TestCase):
def test_download_with_no_length ( self ):
response = mock . MagicMock()
response . read = mock . MagicMock(
side_effect = [ 'data' , 'more data' , '' ])
output = mock . MagicMock()
output . write = mock . MagicMock()
download(response, output)
calls = [mock . call(BUFF_SIZE),
136
E-book gerado especialmente para 


## Página 153

CasadoCódigo Capítulo8. TestesemPython:umapráticasaudável
mock . call(BUFF_SIZE),
mock . call(BUFF_SIZE)]
response . read . assert_has_calls(calls)
calls = [mock . call( 'data' ),
mock . call( 'more data' )]
output . write . assert_has_calls(calls)
Aqui, read()éexecutadotrêsvezes,retornandoumastringvaziana
terceiravezefazendocomqueo whileterminenocomando break.Desta
forma, write()échamadoduasvezescomosparâmetros ‘data’e ‘more
data’.
Testar com mocks é uma técnica muito interessante em alguns ca-
sos,comodasnossasfun çõesdedownload. Felizmente,tudooquepre-
cisamos está disponível na biblioteca padrão, no módulounittest e
unittest.mock.
8.11 Conclusão
Neste capítulo, aprendemos como criar casos de teste – herdando de
TestCase–,vimosumpoucodesuaAPI,comorodá-lospormeiodaAPI
delinhadecomandoecomoconfigurarprogramaticamenteanossasuíte
detestes,alémdeumexemplodeumacustomiza çãoqueaAPIdopacote
unittestpermite.
Tambémforamvistosexemplosdetestesquedevemgerarerros,testes
com mocksusandoaprópriabibliotecapadrãoeosmétodosdociclodevida
deumcasodeteste: setUp()e tearDown(). Porúltimo,aprendemos
comocriara çõesdelimpezausandoaprópriaAPIdo unittest,aousar
addCleanup().
Nopróximocapítulo,vamosveroúltimoconceitofundamentalparatra-
balharcomPython,quesãoosmódulos. Nossocontatocommódulosaté
agorafoisomentecomo usuário,ouseja,importandomóduloseseusobjetos,
eusando-os.Agora,queremosaprenderacriarmóduloseentendermelhor
comofuncionaoseumecanismonoPython3.
137
E-book gerado especialmente para 


## Página 154

E-book gerado especialmente para 


## Página 155

Capítulo9
Módulosepacotes:organizando
edistribuindocódigo
Oúltimoassuntodessaprimeirapartedolivroé módulos. Atéaqui,oque
vimos sobre módulos foi apenas como importá-los e exemplos de como
importá-losdabibliotecapadrão.
Agora,vamosvercomocriarmódulosecomoutilizarosquecriamos.
Comesserecurso,poderemoscompornossoprogramaemdiversosmódu-
los.Amodulariza çãoéumdosprincípiosbásicosdouniversodedesenvol-
vimentodesoftware.
Comojáfalamosemtestes,ficaclaroque,atéentão,temosdois tiposde
código:domínioetestes.Énaturalecomumterummóduloparacadaum
dessestipos.Tambémécomum,masnemsemprenecessário,existirummó-
dulodetestesparacadamódulodedomínio.
E-book gerado especialmente para 


## Página 156

CasadoCódigo
Onossodomínioésimples:tabelasdedados,colunaserelacionamentos.
Naprática,temosquatroclassesdedomínio.Comosãopoucas,vamoscolo-
cartodasnomódulo domain.py.Alémdeste,teremosummódulodetestes
chamado test_domain.py,ondecolocaremosostestesquefizemos.
Emprojetosmaiores,podemosperceberestilosdemodulariza ção,como
maioroumenornúmerodemódulos. Algunsdesenvolvedorespensamem
termosdegruposmaisgeneralistas,enquantooutrosvãomodularizarseu
programasobumaperspectivamaisespecialista.
Agora,vamosolharparaamodulariza çãodeformaprática.
Exemplosreais
Umdosprincipaismotivosdamodulariza çãochama-se reúso.
Dasbibliotecasdisponíveisjuntoaointerpretador,afamosabibliotecapa-
drão(ou standard library),nósimportamosmóduloseobjetosdosmódulos
parautilizá-losemnossosprogramas.Nessescasos,usamososcomandosde
import.Percebaqueacabamosdereusarcódigojápronto.Certamente,você
encontrarámódulosúteisnabibliotecapadrãoeemdiversosoutrosprojetos
decódigoaberto.
Tambémexistemcasosnosquaiscriamosmóduloscomdeterminados
nomeseferramentasqueimportameinteragemcomoquecriamosnes-
sesmódulos.Issoémuitocomumemframeworksdedesenvolvimentoweb.
Aqui,nãoexploraremosexplicitamenteoreúso,masvamosusufruirdofato
dequeumframeworkpodeimportarummódulonossoeusá-lo.
Vamosentendercomomódulossãocriadoseimportados,paraquesua
utilizaçãosejafeitadeformaadequadaemambososcasos.
Criandomódulos:arquivos.py
Quandocriamosoarquivo domain.pynocapítuloanterior,criamosum
módulo.Todoarquivo .pyquecontémcódigoválidoeestáno pathdebusca
demódulospodesercarregado.
140
E-book gerado especialmente para 


## Página 157

CasadoCódigo Capítulo9. Módulosepacotes:organizandoedistribuindocódigo
Caminho (path) de busca de módulos
EmPython,quandoimportamosummódulo,ointerpretadorper-
correumasériedecaminhos–oschamados paths–,paraprocurara
implementaçãodomóduloimportado. Porpadrão,odiretóriodetra-
balho,deondeointerpretadorfoichamado,estánessalista. Porisso,
quandocriamosumarquivo meu_modulo.py,seabrimosointerpre-
tadornomesmodiretóriodele,podemosexecutarcomsucesso import
meu_moduloeutilizaroseucódigo.
Como esse arquivo está na raiz do diretório de trabalho, podemos
importá-lousandoocomando importno pathdebuscapadrão. Ocon-
teúdodomódulo domaincontémasquatroclassesquedefinimosnocapí-
tulo8: DataTable, Column, PrimaryKeye Relationship.
Vejaoexemplo:
>>> import domain
>>> table = domain . DataTable( "Empreendimento" )
>>> table
< domain . DataTable object at 0x10c7f7fd0>
Nocapítulo3aprendemosausaressecomando.Aúnicadiferen çaagora
équeestamosimportandodonossopróprioarquivo domain.py.
Outramelhoriaquepodemosfazeréreunirtodosostestesnoarquivo
test_domain.py. Oprefixo test_fazcomqueobuscadordetestesdo
unittestconsigaacharessemódulodetesteseexecutaroscasosdetestes
queencontrar,dentrodele.
9.1 Módulos em Python : primeiro passo
Semprequecriamosumarquivo *.py,criamosummódulo.Estepodeser
importadousandoocomando import nome_modulo. Semprequeum
novocódigoforcriado,devemosavaliarseeleprecisadeummódulonovo
ounão.Casoprecise,bastacriarumnovoarquivo *.py.
141
E-book gerado especialmente para 


## Página 158

9.1. MódulosemPython:primeiropasso CasadoCódigo
Revisandoomodelodeclasseseseustestes
Agoravamosaproveitarerevisarosarquivosdetrabalho: domain.pye
test_domain.py.
Removios docstringsdasclassesdedomínioparanãoocuparmuitoes-
paço.
Arquivo domain.py:
import decimal
class Column :
def __init__ ( self , name, kind, description = "" ):
self . _name = name
self . _kind = kind
self . _description = description
self . _is_pk = False
def __str__ ( self ):
_str = "Col: {} : {} {}" . format( self . _name,
self . _kind,
self . _description)
if self . _is_pk:
_str = "({}) {}" . format( "PK" , _str)
return _str
@staticmethod
def validate (kind, data):
if kind == 'bigint' :
if isinstance (data, int ):
return True
return False
elif kind == 'varchar' :
if isinstance (data, str ):
return True
return False
elif kind == 'numeric' :
try :
val = decimal . Decimal(data)
except :
142
E-book gerado especialmente para 


## Página 159

CasadoCódigo Capítulo9. Módulosepacotes:organizandoedistribuindocódigo
return False
return True
class PrimaryKey (Column):
def __init__ ( self , table, name, kind, description = None ):
super () . __init__(name, kind, description = description)
self . _is_pk = True
class Relationship :
def __init__ ( self , name, _from, to, on):
self . _name = name
self . _from = _from
self . _to = to
self . _on = on
class DataTable :
def __init__ ( self , name):
self . _name = name
self . _columns = []
self . _references = []
self . _referenced = []
self . _data = []
def _get_name ( self ):
return self . _name
def _set_name ( self , _name):
self . _name = _name
def _del_name ( self ):
raise AttributeError ( "Não pode deletar esse atributo" )
name = property (_get_name, _set_name, _del_name)
references = property ( lambda self : self . _references)
referenced = property ( lambda self : self . _referenced)
143
E-book gerado especialmente para 


## Página 160

9.1. MódulosemPython:primeiropasso CasadoCódigo
def add_column ( self , name, kind, description = "" ):
self . _validate_kind(kind)
column = Column(name, kind, description = description)
self . _columns . append(column)
return column
def _validate_kind ( self , kind):
if not kind in ( 'bigint' , 'numeric' , 'varchar' ):
raise Exception ( "Tipo inválido" )
def add_references ( self , name, to, on):
relationship = Relationship(name, self , to, on)
self . _references . append(relationship)
def add_referenced ( self , name, by, on):
relationship = Relationship(name, by, self , on)
self . _referenced . append(relationship)
Nonossoaplicativo, omódulo domaincontémasclassesdodomí-
niodanossaaplica ção. Emumprojetocomdiversosmódulos,geralmente
existeummódulodetestesparacadaum,comprefixo test_(porexemplo,
test_domain.py).
Vejaocódigofeitoatéentãode test_domain.py:
import unittest
from domain import DataTable
class DataTableTest2 (unittest . TestCase):
def setUp ( self ):
self . table = DataTable( 'A' )
def test_add_column ( self ):
self . assertEqual( 0 , len ( self . table . _columns))
self . table . add_column( 'BId' , 'bigint' )
self . assertEqual( 1 , len ( self . table . _columns))
self . table . add_column( 'value' , 'numeric' )
144
E-book gerado especialmente para 


## Página 161

CasadoCódigo Capítulo9. Módulosepacotes:organizandoedistribuindocódigo
self . assertEqual( 2 , len ( self . table . _columns))
self . table . add_column( 'desc' , 'varchar' )
self . assertEqual( 3 , len ( self . table . _columns))
def test_add_column_invalid_type ( self ):
self . assertRaises( Exception , self . table . add_column,
( 'col' , 'invalid' ))
def test_add_column_invalid_type_fail ( self ):
a_table = DataTable( 'A' )
error = False
try :
a_table . add_column( 'col' , 'invalid' )
except :
error = True
if not error:
self . fail( "Chamada não gerou erro mas deveria" )
def test_add_relationship ( self ):
a_table = DataTable( 'A' )
col = a_table . add_column( 'BId' , 'bigint' )
b_table = DataTable( 'B' )
b_table . add_column( 'BId' , 'bigint' )
a_table . add_references( 'B' , b_table, col)
self . assertEqual( 1 , len (a_table . references))
self . assertEqual( 0 , len (a_table . referenced))
def test_add_reverse_relationship ( self ):
a_table = DataTable( 'A' )
col = a_table . add_column( 'BId' , 'bigint' )
b_table = DataTable( 'B' )
col = b_table . add_column( 'BId' , 'bigint' )
b_table . add_referenced( 'A' , a_table, col)
self . assertEqual( 1 , len (b_table . referenced))
145
E-book gerado especialmente para 


## Página 162

9.2. Oqueacontecequandoimportamosummódulo? CasadoCódigo
self . assertEqual( 0 , len (b_table . references))
9.2 O que acontece quando importamos um mó -
dulo?
Quandoomóduloéimportado,todososcomandosnelesãoexecutados.As
definiçõesdeclassesefun çõesficamemumatabeladesímbolosdopróprio
móduloimportado,evitandoconflitoscomdefini çõesdeoutrosmódulos.
Essemódulo domainpossuiquatroclasses. Quandoeleéimportado,
essesquatroobjetosserãoacessíveisdealgumaforma. Oquenosinteressa
nelesãoasclassesqueestedefine.Existemváriasformasdeacessá-las.Vamos
vercomousaressemóduloquecriamosetambémasvaria ções.
Importaçãosimples
Aformamaissimplesdeimportaréusarocomando import,passando
apenaso(s)nome(s)do(s)módulo(s).
>>> import domain
Agora,nocódigoqueimportou,avariável(ounome) domainrepresenta
omóduloenosdáacessoàsclasses.
>>> import domain
>>> table = domain . DataTable( "Empreendimento" )
Umacaracterísticaqueficaexplícitaéousodocódigodomóduloim-
portado,jáquesempretemosqueusaro“prefixo”domain.antesdeutilizar
algumadefiniçãodomódulo.
Navariaçãocomváriosnomes,elessãoseparadosporvírgula:
import os, sys
Importaçãocompostacomnomes
Aimporta çãocompostanadamaiséqueocomandode importcom
duasinformações: onomedomódulo eonomedadefini ção. Asintaxeé
from nome_modulo import nome_definicao .
146
E-book gerado especialmente para 


## Página 163

CasadoCódigo Capítulo9. Módulosepacotes:organizandoedistribuindocódigo
>>> from domain import DataTable
>>> DataTable
< class ' domain. DataTable '>
Onomedadefini çãopodeserum wildcard( *)queimporta todosos
nomesdomódulo.Nemsemprequeremosimportartudo,masissopodeser
convenienteemexplora çõesnoconsole.
>>> from domain import *
>>> table = DataTable( "Empreendimento" )
>>> col = Column( "IdEmpreendimento" , 'bigint' )
Aqui,tambémpodemossepararasdefini çõesporvírgula:
>>> from domain import DataTable, Column
>>> table = DataTable( "Empreendimento" )
>>> col = Column( "IdEmpreendimento" , 'bigint' )
Emalgunscasos,quandoimportamosalgumasdefini çõeseosnomes
ocupammuitoespa ço,exigindoumaquebradelinha,podemosusarasin-
taxecomtuplas:
>>> from domain import (DataTable, Column, PrimaryKey,
... Relationship)
Modificandonomesimportadoslocalmente
Podesernecessário,ouapenasconveniente,queonomedadefini ção(ou
domódulo)quequeremosimportarsejadiferentenomóduloqueestáim-
portando.Issoépossívelusandoasvaria çõescomapalavrareservada as.
>>> from domain import DataTable as Table
>>> table = Table( "Empreendimento" )
Vejadoisexemplosnoprópriocódigodoaplicativo:
>>> import unittest.mock as mock
>>> import urllib.request as request
Aqui,nãoexistemregrasdecertoouerrado.Maslembrandoo The Zen
of Python,vistonocapítulo 1: explícito é melhor que implícito,emuitacoisa
implícitapodegerarconfusão. Nessecaso,oobjetivoédeixarexplícitoque
umcódigoimportadoestásendousado.
147
E-book gerado especialmente para 


## Página 164

9.3. Pacotes:agrupandomódulos CasadoCódigo
9.3 Pacotes: agrupando módulos
Projetosmaiscomplexosnãosãoorganizadosapenasemmódulos.Quando
aquantidadedemódulosaumenta,aumentatambémanecessidadedecolo-
carmosalgunsempastas,quereúnemmódulosdeumdeterminadotipo.
Nonossoprojeto,temosocódigodeinfraestrutura(download,extra ção
de zip,leituradearquivos)edomínio( DataTable, Columnetc.).Nosso
próximopassoagoraéorganizarnossaaplica çãoempacotes.
Primeiro,vamoscriarumpacotenonívelraiz.Nele,colocaremosomó-
dulo domaineosubpacote commands. Nessesubpacote,colocaremosos
módulosquecompõeasetapasdetratamentodosdados,dodownloadea
geraçãodonossomodelodetabelas.
Aestruturaficariasemelhanteàseguinte:
| copa_transparente
+ | __init__.py
| domain.py
| commands/
| +| __init__.py
| read_meta.py
| download_data.py
| extract_data.py
Para que o interpretador reconheça pastas como pacotes, ele pre-
cisa encontrar o arquivo__init__.py, mesmo que vazio, dentro da
pasta. Agora, podemos chamar o nosso projeto de pacote. O pacote
copa_transparente.
Issofazcomque import domain nãofuncionemais.Deagoraemdi-
ante,nossocódigoestáacessívelcomoprefixo copa_transparente. O
códigoanterioragoradeveserescritodaseguinteforma:
from copa_transparente.domain import DataTable
Apesardeinicialmenteparecerquetemosumtrabalhoamais,nahorade
importar,osarquivos __init__.pyservemparaquesejafeitoocontrole
finodequaisnomessãoexportadosquandoopacoteforcarregado.
148
E-book gerado especialmente para 


## Página 165

CasadoCódigo Capítulo9. Módulosepacotes:organizandoedistribuindocódigo
Se executarmos import copa_transparente, o arquivo
__init__.py na raiz do diretório copa_transparente será exe-
cutado. Todasasdefiniçõesdessemóduloeasimportadasporeleficarão
disponíveisparaocódigocliente.Entretanto,issonemsempreéoqueque-
remos. Nonossoaplicativo,porenquanto,aúnicaclassequeédeinteresse
aousuáriofinalé DataTable. Todasasoutrasdevemserescondidasdo
usuário,paradiminuiracomplexidadedamanipula çãodoprojeto.
9.4 D efinindo nomes para exportação e escopo
de exportação
Emalgunsprojetos,nãoqueremosexporparaousuárioasepara çãoconcei-
tualinternadonossocódigo.Paracontornarisso,podemoscontrolarquais
nomesserãoexportadosporummódulo,mesmoqueestesnãoestejamori-
ginalmentedeclaradosnele. Ointeressantedissoéquedeixamosacritério
dousuárioaescolhadecomoimportaroqueelequer:fazendoreferênciaao
caminhointeiro,ouapenasimportandoonome.
Porexemplo,nonossoprojeto,nãoqueremosqueousuárioconhe çao
módulo domain,masqueremosqueeleuseaclasse DataTablequeestá
em copa_transparente.domain.Naprática,queremostrocaristo:
>>> from copa_transparente.domain import DataTable
Poristo:
>>> from copa_transparente import DataTable
Essetipodedecisãofazpartedo designdaAPI.Nonossocaso,comonão
expusemosmuitosobjetos,émaispráticocolocartodosdebaixodeumúnico
nome–nocaso,copa_transparente–emvezdeobrigarousuárioafazer
diversos importsdesubmódulosdistintos.
Semprequeummóduloéimportado,avariável __all__éprocurada
dentrodele.Casoexista,elaquedefiniráquaissãoosnomesexportadospelo
módulo.Casonãoexista, todasasdefiniçõesencontradasnomóduloquenão
começamcom _serãoexportadas.
149
E-book gerado especialmente para 


## Página 166

9.4. Definindonomesparaexportaçãoeescopodeexporta ção CasadoCódigo
Nonossocaso,oprimeiroexemploédecomoexportarapenasumnome,
semdefiniravariável __all__.Noarquivo __init__.py,dentrodapasta
copa_transparente,podemosteroseguintecódigo:
>>> from domain import DataTable
Repare que aqui estamos no __init__.py, dentro da pasta
copa_transparente, e não como código de usuário. Portanto, não
precisamos do “prefixo”copa_transparente. Esse código anterior
permitequetenhamos,nonossocódigocliente:
>>> from copa_transparente import DataTable
O que aconteceu aqui é que, quando foi feito oimport de
copa_transparente,oconteúdode copa_transparente.__init__
foiexecutado,eonome DataTablefoiimportadodomódulo domaine
automaticamenteexportadopelosclientesde copa_transparente. Isso
porquetudoqueestádefinidono __init__.pydeummóduloéexpor-
tado,porpadrão.
Emalgunsmomentosdeprojetosmaiscomplexos,queremos(oupre-
cisamos)importardiversasclassesno __init__.py,masnãoqueremos
expô-lasparaosclientesdomódulo.Éaíqueentraavariável __all__.py.
Usando-a,poderíamosfazernoarquivo __init__.py(naraizdapasta
copa_transparente),daseguinteforma:
from domain import *
__all__ = [ 'DataTable' ]
Oefeitopráticoéidênticoparaonossoexemplo.Adiferen çaéque,no
primeirocaso,nãotemosacesso,porexemplo,àclasse Columnnoescopo
domódulo __init__.Jánosegundoexemplo,temos Columnnoescopo
domódulo __init__eacessoatodasasclassesdefinidasem domain,e
optamosporexportarapenas DataTable.
150
E-book gerado especialmente para 


## Página 167

CasadoCódigo Capítulo9. Módulosepacotes:organizandoedistribuindocódigo
9.5 Conclusão
Nestecapítulo,vimoscomocriarnossosmódulosealgunsexemplospráticos
decomoutilizaromecanismodemódulos,tantodopontodevistadeumau-
tordeumabibliotecaquantopelodeumusuário.Vimostambémoconceito
depacote,ecomopacotesemódulosrelacionam-se. Porúltimo,aprende-
moscomousarasvaria çõesdocomandode importecomocustomizarque
nomessãoexportadospornossosmódulos.
Deumaformageral,oquevimosaquicobre90%dousodiáriodemó-
dulos,tantocomocriadoresdemódulosepacotesassimcomousuáriosde
módulosdeterceiros.
Aseguir,vamosaprenderamanipulararquivos,parapermitiraleiturade
dadosquepopularáomodelodeobjetosquecriamos.
151
E-book gerado especialmente para 


## Página 168

E-book gerado especialmente para 


## Página 169

ParteII
MundoPython–Alémdos
recursosfundamentais
NaparteI,vimosalgunselementosbásicosdeumalinguagemdeprogra-
maçãoecomoelesfuncionamemPython.
Oqueiniciaremosagoraéaexplora çãodediversosaspectos,alémdos
recursosfundamentais. Vamosvercomotrabalharcomarquivos–jáque
nossoprogramavailerarquivosdedados–,ealgumasclassesdetiposde
dadoscomodecimais,dataseconjuntos,queestãodisponíveisnalinguagem.
Alémdisso,tambémapresentareinovoselementosdesintaxe,aspectosmais
avançadosdomodelodeobjetoseoutrascoisasquefazempartedalinguagem
emerecemestarnolivro.
E-book gerado especialmente para 


## Página 170

E-book gerado especialmente para 


## Página 171

Capítulo10
Trabalhandocomarquivos
Nestecapítulo,aprenderemosamanipulararquivos,paraentãopodermosler
osarquivosdedadosdabasequeestamosusandoparapopularnossomodelo
deobjetos,desenvolvidonocapítulo 7.
10.1 Importando dados para as tabelas
Atéomomento,criamosalgumasclassesqueserãoabasedonossoaplicativo,
maselasaindanãoestãonospermitindomuitascoisas.Oquequeremosagora
écomeçaralerosarquivosdedadoseacriarasinstânciasdessastabelas,
usandoosdadosdasbasesdasquaispodemosfazerdownload.Depoisqueas
tabelasforamcriadaseosdadosdosarquivoslidos,oobjetivoéusá-laspara
realizarconsultasnosdados.
Paralerarquivos,temosafun ção builtin(embutida),chamada open(),
queabreumarquivoeretornaumobjetodotipoarquivo.NoPython3,exis-
E-book gerado especialmente para 


## Página 172

10.1. Importandodadosparaastabelas CasadoCódigo
temtrêstiposdearquivos:binários,bináriosbufferizadosedetexto. Oar-
quivoquevamosleréumarquivotexto. Vamoscome çarcomoexemplo
maissimplespossíveleaproveitarparaverquetipotemumobjetoarquivo
quandoabertocomosparâmetrospadrão:
>>> data = open ( 'data/data/ExecucaoFinanceira.csv' , 'r' )
>>> data
<_io.TextIOWrapper name='ExecucaoFinanceira.csv'
mode='r' encoding='UTF-8'>
>>> data . close()
Ocódigoanteriorpassacomoparâmetroocaminhoe ‘r’queéomodo,
nocaso readouleitura,queserveparaabriroarquivoparaleituradosdados.
Quandomencionamosobjetodotipoarquivo,aideiaéque,independentede
seutipo,suainterfacesejaigualparatodos. MesmoquePythonnãotenha
interfacescomoJava,osobjetosaindapodemseguirdeterminadaspadroni-
zaçõesdemétodos,ouatémesmoherdardeclassesabstratas.
A assinatura completa da função é: open(file, mode=’r’,
buffering=-1, encoding=None, errors=None, newline=None,
closefd=True, opener=None). Os modos informam se o arquivo é
textooubinário,eparaquaisopera çõesseráaberto(leitura,escritaetc.).
Vejaalistademodosaseguir:
'r' open for reading (default)
'w' open for writing, truncating the file first
'x' open for exclusive creation, failing if the file already
exists
'a' open for writing, appending to the end of the file if it
exists
'b' binary mode
't' text mode (default)
'+' open a disk file for updating (reading and writing)
Valelembrarqueosmodospodemsercombinados,sepertinente,como
em: wb,sendoescritabinária( write binary);ou rt,comoleituratexto( read
text).
Oparâmetro bufferingpermitealgumasop ções: -1éovalorpadrão,
quesignificausarasconfigura çõesdosistema; 0paranãousarbuffer(so-
156
E-book gerado especialmente para 


## Página 173

CasadoCódigo Capítulo10. Trabalhandocomarquivos
mentenomodobinário); 1parausarumbufferporlinhas(válidosomente
emarquivotexto);e,emvalores>1,otamanhodobufferpassaaserovalor
passadocomoparâmetro.
Oparâmetro encodingpodeserastringcomonomedoformato,como
"utf-8".
Os outros parâmetros são muito específicos e podem ser consul-
tados na documentação oficial, em https://docs.python.org/3/library/
functions.html#open.
Voltando ao exemplo, veja que o objeto retornado é do tipo
TextIOWrapper. Essa classe é uma implementação de arquivos de
texto, que, alémdeterasfunçõescomunsatodotipodeobjetodotipo
arquivo, tem também funções específicas que só podem ser usadas para
arquivosabertosemmodotexto.
Ostiposdearquivodetextotrabalhamcomstringsemvezdebytes,como
nosarquivosbinários. Nocapítulo2,vimosquenoPython3todasstrings
sãounicodee,portanto,quandoescritasemarquivoouenviadaspelarede,
devemserconvertidasparabytesatravésdeum encoder.Nostiposdearquivo
detexto,mecanismosinternosjáfazemaconversãodestringsparabytes(e
vice-versa).
Comoqueremosolharparaostiposdearquivodeformamaisgenérica,
vamosnosconcentrarnosmétodosemcomumatodosostiposdearquivo,e
veraseguirdoisdosmaisimportantes: read()e write().
10.2 Lendo arquivos
Afunçãoparalerdadosé read().Quandoainvocamossemparâmetros,
todooconteúdodoarquivoélidoeretornado.Seoarquivoformuitogrande,
oseuprogramapodeconsumirmuitamemória.Umaalternativaéespecificar
aquantidadedebytesaserlida,como read(4096).Vamosveroexemplo:
>>> data = open ( 'ExecucaoFinanceira.csv' , 'r' )
>>> data . read( 19 )
157
E-book gerado especialmente para 


## Página 174

10.2. Lendoarquivos CasadoCódigo
'1;2;132;CONSTRUTORA'
>>> data . close()
Ocódigoexibiuos19primeirosbytesdoarquivodeexecu çõesfinancei-
ras.Comoestamostrabalhandocomarquivosdetextoqueseguemoformato
CSV,geralmenteasquebrasdelinha "\n"delimitamofinaldeumainforma-
ção.Porexemplo,nocasodeumarquivodedados copa_transparente
[1],cadalinhasignificaumregistronaquelatabela. Logo,umalinhanoar-
quivo ExecucaoFinanceira.csvcontémainformaçãodeumaExecu ção
Financeira.
Existeumaformamelhordeler,linhaalinha,umarquivodetexto,que
veremosnasequência.
Iterandonaslinhas
Nonossoaplicativo,comotodososarquivostêmmenosde10Mb,pode-
moslê-losdeumavezsó,apenaschamando read(),semparâmetroalgum.
Emnossocaso,estamoslidandocomumCSV,entãoqueremoslerlinhaali-
nha.EmPython,podemosusarométodo readline()ouiteraraslinhas
doarquivo,usandoocomando fornopróprioobjetodotipoarquivo.Veja
oexemplo:
data = open ( 'data/data/ExecucaoFinanceira.csv' , 'r' )
for line in data:
print (line)
data . close()
Ométodo readline()estádisponívelapenasparaarquivosdetexto.
Aiteraçãousandoocomando fortambémfuncionaemarquivosbinários,
mascontinuaráfazendoaquebrapelocaractere "\n".
Sequisermostodasaslinhasemumalistadestrings,emquecadaitem
dalistaéumalinhadoarquivo,podemosusarafun ção readlines(). A
desvantageméque,novamente,emarquivosgrandes,podesercriadauma
listamuitograndeemmemória.Deve-seanalisarcasoacasoseénecessário
tertudoemmemóriasimultaneamente,ouseteracessoapenasaumalinha
porvezjáatendeànecessidade.
158
E-book gerado especialmente para 


## Página 175

CasadoCódigo Capítulo10. Trabalhandocomarquivos
Paraverumexemplodafun ção readlines(),vamosvermaisumtipo
dearquivodetextoqueémuitocomum: StringIO.Um StringIOéum
streamdetextoemmemória,queimplementaocontratodaAPIdemanipu-
laçãodearquivosdetexto. Émuitoútilquandoqueremosusarumcódigo
queesperaumobjetodotipoarquivoenóspodemospassarumobjetocom-
patível,masquepordentrotemumastringqueé,naverdade,oconteúdodo
arquivo.
>>> import io
>>> data = io . StringIO( "a\nb\nc" )
>>> lines = data . readlines()
>>> print (lines)
['a\n', 'b\n', 'c']
>>> data . close()
>>> data . closed
True
Paraocódigo, dataéumarquivoepodeserusadocomoarquivoem
códigosqueesperamumtipoarquivotexto.
Comoesperado,afun ção readlinesretornouumalistacomcadalinha
doarquivo.Reparequeaslinhasquetêmocaractere "\n"vêmcomelena
string,easlinhasquenãotêm(nocaso,apenasaúltima),vêmsem.
Iterar versus ler todas as linhas
Avantagemdeiterarnaslinhaséqueemnenhummomentopreci-
samosteremmemóriaumespa çograndeosuficienteparacabertodo
oconteúdo.Paraarquivosmuitograndes,issopodefazerumaboadife-
rença.
Emalgumasitua ções,podeserdesejávelteroconteúdotodoemme-
mória.Então,cadasitua çãodeveseravaliadaseparadamente.
10.3 Fechando arquivos
Programas“bemcomportados”fechamosarquivosabertosaofinaldesua
execução. Nosnossosexemplos,fizemosissousandoométodo close().
159
E-book gerado especialmente para 


## Página 176

10.4. Abrindoarquivoscomocomandowith CasadoCódigo
Todosostiposdearquivoimplementamométodo close(),atémesmo
StringIO,quenãotemumarquivorealabertoeque,depoisdométodo
close()chamado,seuconteúdonãopodesermaislido.Nessescasos,acha-
madaaométodo read(),emumarquivofechado,geraum ValueError.
Podemosverificarseumobjetodotipoarquivoestáfechadousandoa
propriedade closed.Vejaoexemploqueilustraoquefalamos:
>>> import io
>>> data = io . StringIO( "a\nb\nc" )
>>> lines = data . readlines()
>>> print (lines)
['a\n', 'b\n', 'c']
>>> data . close()
>>> data . closed
True
>>> data . read()
Traceback (most recent call last):
File "<stdin>" , line 1 , in <module>
ValueError : I/O operation on closed file
10.4 Abrindo arquivos com o comando with
EmPython,existeumaforma pythônicadesetrabalharcomarquivosusando
ocomando with.EssecomandointroduzidopelaPEP-343[ 4]temoobjetivo
desimplificarousorepetidodecomandos try/finallyemalgumassitua-
ções.Conceitualmente,temosumgerenciadordecontexto,queéumaclasse
decujociclodevidadoismétodosfazem. Pormeiodessesmétodos,con-
seguimosexecutarcódigoemmomentoscomoentradaesaídadeumbloco
com with.
Comessecomando,nãoprecisamosnospreocuparemfecharexplicita-
menteoarquivo,jáqueoprópriogerenciadordecontextoseráchamadono
finaldobloco with,echamaráométodo close()doarquivoemquestão.
Vamosusá-lononossoprimeiroexemplo:
with open ( 'data/data/ExecucaoFinanceira.csv' , 'r' ) as data:
content = data . read()
print (content)
160
E-book gerado especialmente para 


## Página 177

CasadoCódigo Capítulo10. Trabalhandocomarquivos
Nesseexemplo,oobjetoretornadopelafun ção open()écompatível
comoprotocolodegerenciadordecontexto.Portanto,quandoobloco with
termina,oarquivoretornadopor open(‘ExecucaoFinanceira.csv’,
‘r’)éfechado.Algumasbibliotecasdeacessoabancodedadosusamesse
comandoparadelimitarconexõesabertas,ouatémesmotransa çõesemban-
cosdedados.
Sejuntarmosocomando withcomleituradearquivolinhaalinhae split
destrings,jáconseguimosobtertodososvaloresdeexecu çõesfinanceirasda
basededadosdacopa.Vejaoexemplo:
with open ( 'data/data/ExecucaoFinanceira.csv' , 'r' ) as data:
for line in data:
print (line . split( ';' )[ 5 ])
Veremosnasaídavaloresdeexecu çõesfinanceirasatéqueumerroseja
exibidoquandoumalinhamalformadaforencontrada. Porenquantoisso
nãoéumproblemajáqueofocoésobreabrirumarquivo,lerlinhaalinhae
deixarqueopróprioambienteseencarreguedefecha-loaofinaldouso.
10.5 Escrevendo em arquivos
Nonossoprimeiroprograma,nocapítulo 4,vimosumexemplodeescritaem
arquivonocódigoquefazodownloaddoarquivodabasededados.Aescrita
noarquivosedeubasicamenteemduaslinhasdocódigo.Vamosanalisar:
>>> out_file = io . FileIO(file_path, mode = "w" )
Vejaocódigoanteriorusandoafun ção open():
>>> out_file = open (file_path, mode = "wb" ) # modo write binary
Agora,aschamadasdafun ção write():
>>> out_file . write(bytes_to_write)
Porsetratardeumarquivo ZIP–quetemconteúdobinário–,usamosa
classe FileIOquetrabalhacombytesemvezdestrings.Porém,poderíamos
usarafun ção open(),sinalizandoarquivobinário,exatamentecomono
161
E-book gerado especialmente para 


## Página 178

10.6. Navegaçãoavan çadacomseek() CasadoCódigo
exemploanterior.Alémdisso,abrimosoarquivocommodo w,queéomodo
deescrita( write),equepermitequeafun ção write()sejachamada. O
códigocompletonãofaznadaalémdelerdadosdarespostadoservidore
escreveremumarquivolocal.
Seestivéssemostrabalhandocomarquivostexto,aúnicadiferen çaseria
ométodo write(),queestariaesperandoumastring(enãobytes),como
nonossoexemplo.Émuitoimportanteescolherotipocorretodependendo
doarquivoqueserálido,pois,casocontrário,ascoisaspodemnãofuncionar
comoesperado.
10.6 Navegação av ançada com seek ()
Umafunçãobasedearquivoséa seek().Essafun çãoémuitosemelhanteà
fseek()dalinguagemC.Comela,vocêpodecolocaroponteirodoarquivo
nolugarquedesejar.Issoémuitoútilquandoqueremosleromesmotrecho
deumarquivodiversasvezes.
Vejaoexemplo:
>>> data = open ( 'ExecucaoFinanceira.csv' , 'r' )
>>> data . read( 5 )
'1;2;1'
>>> data . read( 5 )
'32;CO'
>>> data . read( 5 )
'NSTRU'
>>> data . read( 5 )
'TORA '
>>> data . seek( 0 )
0
>>> data . read( 20 )
'1;2;132;CONSTRUTORA '
Repareque,acadachamadade read(),oponteirodoarquivoéatua-
lizadoeanovaleituraéiniciadaemumaoutraregião. Pormeiodousoda
função fseek(),foipossívelretornaraoiníciodoarquivopararealizara
leitura.
162
E-book gerado especialmente para 


## Página 179

CasadoCódigo Capítulo10. Trabalhandocomarquivos
10.7 Conclusão
Nestecapítulo,vimoscomoabrirefechararquivos,ecomousarocomando
withparaqueelessejamfechadosautomaticamente. Depoisaprendemos
algumasformasdeseobterosdadosdosarquivos,sejalendoumaquantidade
específicadebytes,iterandolinhaalinhacomoloop for,ouatémesmo
pegandoumalistacomtodasaslinhasdoarquivo.
Alémdisso,vimostambémcomousarosmodosdeabertura,interferindo
nosobjetosretornados,equaisopera çõespodemosrealizarneles. Porfim,
aprendemoscomoescreveremarquivoseemquaisdetalhesdevemosficar
atentos. Aseguir,veremosmaisrecursosdisponíveisnabibliotecapadrão,
masquenãoestãoembutidosnalinguagemeprecisamosimportá-los.
163
E-book gerado especialmente para 


## Página 180

E-book gerado especialmente para 


## Página 181

Capítulo11
Umpasseioporalgunstipos
definidosnabibliotecapadrão
Atéagora,vimosalgunsdostiposquepodemserchamados básicos,quesão:
inteiros,flutuantesestrings. Ostiposquechamamosdebásicossãoosque
nãonecessitamdenenhumcomandode importejáestãodisponíveisno
contextodeexecu ção. Essestipostambémsãochamadosde builtins,pois
estãoembutidosnapróprialinguagemepodemserusadossemquenenhum
módulosejaimportado.
Tambémvimosasestruturasdedados fundamentais,quesãotuplas,lis-
tasedicionários.Podemoschamá-lasdefundamentais,porquetodalingua-
geméimplementadausando-ascomobase.
Nomundoreal,emalgumassitua ções,precisamosdeoutrosrecursos
comoumtipomaisespecializado,ouumaestruturadedadosquenãosejam
E-book gerado especialmente para 


## Página 182

11.1. Dinheiroedecimaiscomprecisãoarbitrária CasadoCódigo
asfundamentais,pararesolvermosnossosproblemascommaiseficiência.
EmPython,existemmuitosrecursosqueestãodisponíveisnabiblioteca
padrão,masquenãoestãoembutidosnalinguagem. Issosignificaquepo-
demosusá-losapenasimportandodeondequerqueseja.Nocasodonosso
aplicativo,queremosumtipoquenospermitatrabalharcomvaloresfinancei-
rosequesuportemopera çõesaritméticascomprecisãoarbitrária.Emmui-
taslinguagens,essetipoéchamado,informalmente,deDecimal,comopor
exemploemPython,noqualtemosotipo Decimal,ouemJava,ondeexiste
o java.math.BigDecimal.
11.1 Dinheiro e decimais com precisão arbitrá-
ria
Quandoestamosrealizandocálculosfinanceiros,mesmoquesimples,pre-
cisamosdenúmeroscomprecisãoarbitrária. Quandousamosflutuantes
(floats)pararepresentarvaloresfracionários–como1.25–,dependendoda
operaçãoquefizermos,oresultadodosarredondamentospodecausarmuita
surpresa.Vejaosexemplosaseguir:
>>> 0.1 + 0.1 + 0.1
0.30000000000000004
>>> 0.1 + 0.1 + 0.1 - 0.3
5.551115123125783e-17
>>> Decimal( '0.1' ) + Decimal( '0.1' ) + Decimal( '0.1' ) -
Decimal('0.3')
Decimal('0.0')
>>> Decimal( '0.1' ) + Decimal( '0.1' ) + Decimal( '0.1' ) -
Decimal('0.3')
Decimal('0.0')
Acontecequeosflutuantessãoumaformaderepresentar aproximaçõesde
númerosreaisparaumgrandeintervalodenúmeros.Paratermosessaflexi-
bilidadedesuportarintervalosrealmentegrandes,suaprecisãoéumpouco
sacrificada. Emmuitosdomínios,essaperdadeprecisãonãoafetaoresul-
tadodoprograma,então,escolherumdosdoiséumaquestãodedesigndo
projeto.
166
E-book gerado especialmente para 


## Página 183

CasadoCódigo Capítulo11. Umpasseioporalgunstiposdefinidosnabibliotecapadrão
Nonossoprograma,vamostrabalharcomvaloresquerepresentamquan-
tiasemdinheiro. Nanossamoeda,temosduascasasdecimais,equeremos
precisãototalearredondamentoscoerentescomascontasfinanceiras.Para
essetipodetarefa,usamosotipo Decimaldomódulo decimal.
Tudooqueprecisamosfazeréconverterosvaloresfinanceirosdestring
para Decimal,parapoderrealizarascontasquenosinteressam.
Vamosvoltarnoexemplodocapítuloanterioreutilizaro Decimal,para
quesejapossívelsomartodososvalorescomaprecisãoquequeremos.
# coding: utf-8
from decimal import Decimal
total = Decimal( '0' )
with open ( 'data/data/ExecucaoFinanceira.csv' , 'r' ) as data:
for line in data:
try :
info = line . split( ';' )
str_value = info[ 5 ] # o valor está na 5a posição
total += Decimal(str_value)
except Exception as e:
print ( 'error {}' . format(line))
print ( "Total gasto: {}" . format(total))
Oresultadocomputadofoide:
Total gasto: 22583122032.97
Nocódigoanterior,criamososdecimaisapartirdestrings,eosmanipu-
lamosdeformaidênticaaoquefazemoscominteirosouflutuantes.Elestêm
algumasfunçõesmatemáticasdisponíveise,demaneirageral,sãointercam-
biáveiscomostiposprimitivos.
MaisdetalhesemDecimals
Umerromuitocomuméemrela çãoàinicializa çãodosdecimais,mais
especificamentenotipoquepassamosnoconstrutor. Oconstrutoraceita
167
E-book gerado especialmente para 


## Página 184

11.1. Dinheiroedecimaiscomprecisãoarbitrária CasadoCódigo
strings,inteiros,floatsetuplas.Vamosveralgunscasosqueexpressamme-
lhoresseserrosquepodemsercometidos.
>>> from decimal import Decimal
>>> Decimal( '0.1' ) + Decimal( '0.1' )
Decimal('0.2')
>>> Decimal( 0.1 ) + Decimal( 0.1 )
Decimal('0.2000000000000000111022302463')
>>> Decimal( 0.1 ) + Decimal( 0.1 ) ==
Decimal('0.1') + Decimal('0.1')
False
Comomencionado,os floatssãoaproximações.Logo,quandopassamos
paraumconstrutordotipodecimal,elecaptaaaproxima ção,enãoonúmero
representadopeloliteral 0.1.
Épossívelconfiguraraprecisãonasopera ções,paraqueaúltimaigual-
dadedoexemploanteriorsejaverdadeira.Fazemosissoconfigurandoapre-
cisãonocontextodosdecimais.Vejaoexemploaseguir:
>>> from decimal import Decimal
>>> from decimal import Decimal, getcontext
>>> getcontext() . prec = 1
>>> Decimal( 0.1 ) + Decimal( 0.1 ) ==
Decimal('0.1') + Decimal('0.1')
True
Seapreci çãoexigidaédeapenasumacasadecimal,então,aigualdade
anteriortemdeserverdadeira.
Tambémsãoaceitosvaloresstringquerepresentamumvalorquenãoseja
umnúmero( Not a Number),zeronegativoouinfinitos.Vejaosexemplosa
seguir:
>>> Decimal( 'NaN' )
Decimal('NaN')
>>> Decimal( 'Infinity' )
Decimal('Infinity')
>>> Decimal( '-Infinity' )
Decimal('-Infinity')
>>> Decimal( '-0' )
Decimal('-0')
168
E-book gerado especialmente para 


## Página 185

CasadoCódigo Capítulo11. Umpasseioporalgunstiposdefinidosnabibliotecapadrão
Impedindousodedecimaiscomcertostipos
Aúltimacaracterísticaquevamosvernosdecimaisécomousaroseu
mecanismodearmadilhas( traps). Comumaarmadilha,podemossolicitar
queumaexce çãosejalevantadacasoumdecimalsejausadoemumaopera ção
deconstrução,oucompara çãocomumoutrovalorquenãoéumdecimal.
>>> c = getcontext()
>>> from decimal import FloatOperation
>>> c . traps[FloatOperation] = True
>>> Decimal( '1.10' ) < 1.25
Traceback (most recent call last):
File "<stdin>" , line 1 , in <module>
decimal.FloatOperation : [<class 'decimal.FloatOperation'>]
Podemosusaressemecanismoparaemitir,emtempodeexecu ção,uma
exceçãoquandoumaopera çãoenvolvendoumdecimaleumobjetodeoutro
tipo,quenãodecimal,forexecutada.
Nonossoaplicativo,oqueprecisamoséapenasdotipo Decimal,para
realizaralgumasopera çõesaritméticas.Éimportantetratarerrosquepossam
sergeradosnachamadadoconstrutor,eentenderqualmotivooslevoua
acontecer,paratomaramelhordecisãosobreotratamentodessasitua ção.
11.2 Datas e tempo: módulo datetime
Agoraquesabemoscomotratarcorretamenteosvaloresfinanceiros,pode-
moscriarconsultasmaisinteressantes,usandodatascomoreferência. Por
exemplo,podemossaberquaisexecu çõesfinanceirasforamassinadasapar-
tirdedeterminadadata,ouemumintervaloespecíficodetempo.
EmPython,amanipula çãodedatasfazumasepara çãosimplesdeiní-
cio: trabalharcomdatasehora,trabalharsomentecomdata,outrabalhar
somentecomhora(ouhorário). Emcadacaso,umaclasseespecíficadeve
serimportada,quepodeser: date, datetimeou time,todasdopacote
datetime.
Vamossuporquenossoobjetivosejaverasexecu çõesfinanceirasassi-
nadasentreduasdatas.Precisamostransformaroinputdetextoemobjetos
169
E-book gerado especialmente para 


## Página 186

11.2. Datasetempo:módulodatetime CasadoCódigo
dedata,ecompará-losaosobjetoscriadosarbitrariamente,porexemplo.A
seguir,vejaumprogramaquecalculaototalassinadoentre2009e2010.
# coding: utf-8
from decimal import Decimal
from datetime import date
total = Decimal( '0' )
start_date = date( 2009 , 1 , 1 )
end_date = date( 2010 , 1 , 1 )
def get_value (info):
try :
signature_str_date = info[ 7 ]
year = int (signature_str_date . split( '/' )[ 2 ])
month = int (signature_str_date . split( '/' )[ 1 ])
day = int (signature_str_date . split( '/' )[ 0 ])
signature_date = date(year, month, day)
if signature_date > start_date and signature_date <
end_date:
str_value = info[ 5 ]
value = Decimal(str_value)
return value
except Exception as e:
print (e)
pass
return Decimal( '0' )
with open ( 'data/data/ExecucaoFinanceira.csv' , 'r' ) as data:
for line in data:
total += get_value(line . split( ';' ))
print ( "Total gasto com assinaturas entre {} e {} : {}"
. format(start_date, end_date, total))
Primeiro, usamos o construtor dedate com a seguinte assinatura:
date(year, month, day) . Comele,criamosasdatasdereferência. Já
170
E-book gerado especialmente para 


## Página 187

CasadoCódigo Capítulo11. Umpasseioporalgunstiposdefinidosnabibliotecapadrão
asdatasdasexecu çõescriamosapartirdasdatasemtexto,decadalinhado
arquivo.
Nofinal,realizamosacompara çãocomooperador >,quepermitecom-
paraçãodevaloresdedata,dataehora,ehora.Todasascompara çõesestão
disponíveisparaosobjetosdedata,desdequesejamcompatíveisentresi.
Oobjeto dateéomaissimplesdetodosecontaapenascomtrêsatri-
butos:ano,mêsedia.Naprática,amaioriadosprogramasacabausandoo
objeto datetime,queémaiscompletoetemmaisfuncionalidades,alémde
poderserusadomesmoqueasinforma çõesdehoranãosejamespecificadas.
Osobjetos datetimetambémpodemsercriadosdeumaformaseme-
lhanteaoobjeto date.Vejanoexemplo:
>>> from datetime import datetime
>>> dt = datetime( 2014 , 1 , 1 )
>>> dt
datetime.datetime(2014, 1, 1, 0, 0)
Ou,podemsercriadoscomespecifica çãodehora:
>>> from datetime import datetime
>>> dt = datetime( 2014 , 1 , 1 , 8 , 30 )
>>> dt18 = datetime( 2014 , 1 , 1 , 18 , 30 )
>>> dt8 = datetime( 2014 , 1 , 1 , 8 , 30 )
>>> dt18 > dt8
True
Naprática,quandoqueremosconverterdatas,apartirdetexto,emobje-
tosdotipo dateou datetime,usamosométodo strptime()doobjeto
datetime.Essapequenamudan çaajudaaapagaralgumaslinhasdecódigo.
Vejaoexemploaseguir:
>>> from datetime import datetime
>>> datetime . strptime( '01/01/2014' , '%d/%m/%Y' )
datetime.datetime(2014, 1, 1, 0, 0)
Da mesma forma, a operação inversa pode ser feita com o método
strftime(),comonoexemploseguinte:
171
E-book gerado especialmente para 


## Página 188

11.2. Datasetempo:módulodatetime CasadoCódigo
>>> from datetime import datetime
>>> dt = datetime( 2014 , 1 , 1 , 19 , 15 )
>>> dt . strftime( '%Y-%d-%m %H:%M' )
'2014-01-01 19:15'
Alistacomasop çõesdeconfigura çõesdeformatosdedata,usadas
por strptimee strftime,estáemhttps://docs.python.org/3/library/
datetime.html#strftime-and-strptime-behavior.
Outraoperaçãocomuméaaritméticacomdatas.Muitasvezes,queremos
somardias,oumeses,ouqualqueroutraunidadecompatívelaumadata.Em
outrassituações,queremossaberadiferen çaemdiasoumeses,ouatémesmo
horasentreduasdatasoudoishorários. Todasessasopera çõespodemser
realizadascomosoperadoresaritméticos,porémcomodetalhedequeelas
retornemouusemobjetosdotipo timedelta. Oobjeto timedeltare-
presentaumadiferen çaentreduasdatas,oudata/hora.
Nonossoaplicativo,podemoslistarquantosegastouemexecu çõesfinan-
ceiras,cujotempodevigênciafoimenorque11dias:
from decimal import Decimal
from datetime import datetime
total = Decimal( '0' )
start_date = datetime( 2014 , 1 , 1 )
def get_value (info):
try :
start_str_date = info[ 8 ]
end_str_date = info[ 9 ]
start_date =
datetime . strptime(start_str_date, '%d/%m/%Y' )
end_date = datetime . strptime(end_str_date, '%d/%m/%Y' )
date_diff = end_date - start_date
if date_diff . days < 10 :
str_value = info[ 5 ]
value = Decimal(str_value)
172
E-book gerado especialmente para 


## Página 189

CasadoCódigo Capítulo11. Umpasseioporalgunstiposdefinidosnabibliotecapadrão
return value
except Exception as e:
print (info)
pass
return Decimal( '0' )
with open ( 'data/data/ExecucaoFinanceira.csv' , 'r' ) as data:
for line in data:
total += get_value(line . strip() . split( ';' ))
print ( "Total gasto com contrados de menos de 11 dias {}"
. format(total))
Vamosexaminarmelhoresseobjetoqueestánavariável date_diff.
>>> from datetime import datetime
>>> start_date = datetime . strptime( '01/01/2014' , '%d/%m/%Y' )
>>> end_date = datetime . strptime( '10/01/2014' , '%d/%m/%Y' )
>>> diff = end_date - start_date
>>> type (diff)
<class 'datetime.timedelta'>
>>> diff . days
9
>>> diff . total_seconds() / 60 / 60 / 24 # segundos/minutos/dias
9.0
Omódulo datetimepossuiumaclassechamada timedelta. Essa
classerepresentajustamenteumadiferen çaentredatasouhoras. Quando
realizamosoperaçõesaritméticascomdatas,oobjetoretornadoédessetipo.
Comele,podemospegaradiferen çaemnúmerodedias,ouatémesmoem
segundostotais. Omesmotipodeopera ção,subtra ção,tambémpodeser
feitocomhoras.Vejanoexemplo:
>>> start_time = datetime . strptime( '18:00' , '%H:%M' )
>>> end_time = datetime . strptime( '21:30' , '%H:%M' )
>>> diff = end_time - start_time
>>> diff . seconds / 60 / 60
3.5
173
E-book gerado especialmente para 


## Página 190

11.2. Datasetempo:módulodatetime CasadoCódigo
Vemosqueadiferen çaentre 21:30e 18:00éde3horasemeia.Tam-
bémpodemosverovaloremsegundos,pormeiodoatributo seconds
daclasse timedelta. Umdetalheimportanteénãoconfundirométodo
total_seconds()–quepegaototaldesegundosentreduasdatasquais-
quer–,comoatributo seconds–queserefereapenasàpartedashoras.
Umaoutrafacilidadedaclasse timedeltaéqueelatambémpodeser
facilmenteconstruídaàmão,paraquesejasomadaaumadata,retornando
umanovadata.Vejaumexemplobásicoprimeiro:
>>> birthday = datetime( 2014 , 1 , 1 )
>>> next_birthday = birthday + timedelta(days =365 )
>>> next_birthday
datetime.datetime(2015, 1, 1, 0, 0)
Noexemploprático,podemostirarumaconsultabeminteressante: a
quantidadedeexecu çõesfinanceirasassinadasemcadaano. Paraisso,cri-
amosdatascomadatainicialdecadaano,somamos365diaseficamoscom
duasdatas.Depois,filtramosasexecu çõesfinanceirasassinadasnesseinter-
valoecontamosaquantidadeencontrada.Vejaque,nesseexemplo,usamos
quasetudooquefoivisto: datetime, timedelta,operaçãodecompara-
çãoeopera çãoaritmética.
from decimal import Decimal
from datetime import datetime, timedelta
totals = { 2010 : 0 , 2011 : 0 , 2012 : 0 , 2013 : 0 , 2014 : 0 , 2015 : 0 }
def check_signature_interval (info, year_start_date,
year_end_date):
try :
start_str_date = info[ 8 ]
end_str_date = info[ 9 ]
start_date = datetime . strptime(start_str_date,
'%d/%m/%Y' )
end_date = datetime . strptime(end_str_date, '%d/%m/%Y' )
if start_date > year_start_date and start_date <
year_end_date:
174
E-book gerado especialmente para 


## Página 191

CasadoCódigo Capítulo11. Umpasseioporalgunstiposdefinidosnabibliotecapadrão
return 1
except Exception as e:
pass
return 0
for year in totals . keys():
start_date = datetime(year, 1 , 1 )
end_date = start_date + timedelta(days =365 )
with open ( 'data/data/ExecucaoFinanceira.csv' , 'r' ) as data:
for line in data:
totals[year] += check_signature_interval(
line . strip() . split( ';' ), start_date, end_date)
for year, signed in totals . items():
print ( "{} execuções assinadas em {}" . format(signed, year))
Asaída:
35 execuções assinadas em 2010
91 execuções assinadas em 2011
253 execuções assinadas em 2012
4468 execuções assinadas em 2013
506 execuções assinadas em 2014
0 execuções assinadas em 2015
Alémdisso,temosasfun çõesdeobteradata/horaeadataatual,sendo,
respectivamente, o métodonow() da classe datetime, e o método
today()daclasse date.Vejaoexemplo:
>>> from datetime import datetime, date
>>> datetime . now()
datetime.datetime(2014, 8, 18, 23, 25, 3, 297527)
>>> date . today()
datetime.date(2014, 8, 18)
11.3 Conjuntos sem repetição : set()
Outraestruturadedadosmuitoutilizadaéoconjunto,que,emPython,éa
estrutura set.
175
E-book gerado especialmente para 


## Página 192

11.3. Conjuntossemrepetição:set() CasadoCódigo
Essaestruturanãopermiteelementosduplicadosenemasseguranenhum
tipodeordementreelementos,nemíndices.Portanto,nãoéumasequência
comoumalista. Esseobjetopermitequealgumasopera çõesdaTeoriados
Conjuntos[11]–comointerseção,união,diferen ça,diferençasimétrica,teste
depresençadeelementoouelementos–sejamrealizadasemumconjunto,
ouconjuntos.
Nonossoprograma,podemoscriarconjuntosdeempresasassociadosa
execuçõesfinanceirasdevalores,emalgumintervaloarbitrário,edepoiscon-
sultaronúmerodistintodeempresasemcadagrupo.Porexemplo,podemos
criarumconjuntocomasempresasassociadasaexecu çõessuperioresa1bi-
lhão,500milhões,100milhões,10milhões,1milhãoemenos.
Vamoscontinuarcomnossoexemplo:
# coding: utf-8
from decimal import Decimal
def get_id_and_value (info, lower):
value = Decimal(info[ 5 ])
if value > lower:
return info[ 2 ], value
return None , Decimal( 0 )
all_companies = set ()
intervals = [(Decimal( '1000000000' ), set ()),
(Decimal( '500000000' ), set ()),
(Decimal( '100000000' ), set ()),
(Decimal( '10000000' ), set ()),
(Decimal( '1000000' ), set ()),
(Decimal( '100000' ), set ()),
(Decimal( '10000' ), set ()),
(Decimal( '1000' ), set ())]
for lower, companies in intervals:
data = open ( 'data/data/ExecucaoFinanceira.csv' , 'r' )
for line in data:
company_id, contract_value = get_id_and_value(
line . strip() . split( ';' ), lower)
176
E-book gerado especialmente para 


## Página 193

CasadoCódigo Capítulo11. Umpasseioporalgunstiposdefinidosnabibliotecapadrão
if company_id and not company_id in all_companies:
companies . add(company_id)
all_companies . add(company_id)
data . close()
for lower, companies in intervals:
print ( "{} empresas receberam mais de {}" . format(
len (companies), lower))
print ( "{} empresas no total" . format( len (all_companies)))
Leiacomcalmaparaentenderasdiversasideiasempregadasnessepe-
quenoprograma.
Primeiro,criamosumconjuntoondecolocaremososidentificadoresde
todasasempresas. Comele,vamosverificarqueumaempresaquerecebeu
1milhãonãosejacontadanovamentequandoovalordetesteforumvalor
menor,como10mil.
Depois,criamosumalistadetuplas,naqualcadaumatemumvalorde
comparaçãoeumconjuntoondecolocaremososidentificadoresencontrados.
Oloopsimplesmentevarretodososregistroscomumvalormínimocor-
rente,eincluinoconjuntooidentificadordaempresaquerecebeumaisque
ovalormínimocorrente.Semumconjunto,teríamosumalistacomrepeti-
ções,jáqueumamesmaempresapodeterrecebidomaisdeumaexecu ção
financeira.Porém,felizmente,temosumaformaelegantedeeliminararepe-
tiçãosemterdeintroduzirmanualmenteummecanismodeelimina çãode
repetições.
Aestruturadeconjuntonãoselimitaapenasaeliminarrepeti çõeseaim-
plementaralgumasopera çõesmatemáticasdeconjuntos.Vejaalgunsexem-
plosaseguir:
>>> set ([ 1 , 2 , 3 , 4 , 5 ]) & set ([ 2 , 4 ])
{2, 4}
>>>
>>> set ([ 1 , 2 , 3 , 4 , 5 ]) | set ([ 6 , 7 ])
{1, 2, 3, 4, 5, 6, 7}
>>>
>>> set ([ 1 , 2 , 3 , 4 , 5 ]) . isdisjoint( set ([ 6 , 7 ]))
True
177
E-book gerado especialmente para 


## Página 194

11.3. Conjuntossemrepetição:set() CasadoCódigo
>>>
>>> set ([ 1 , 2 , 3 , 4 , 5 ]) > set ([ 2 , 4 ])
True
>>>
>>> set ([ 1 , 2 ]) < set ([ 1 , 2 , 3 , 4 , 5 ])
True
>>>
>>> set ([ 1 , 2 , 3 ]) - set ([ 1 , 3 ])
{2}
>>>
>>> set ([ 1 , 2 , 3 ]) ^ set ([ 2 , 3 ])
{1}
Asoperaçõessão:
•&–interseção;
•|–união;
•original.isdisjoint(other)–seoconjuntootherédisjunto
doconjunto original;
•set1 > set2 –seset2ésubconjuntode set1;
•set1 < set2 –seset1ésubconjuntode set2;
•-–diferençaentreconjuntos;
•^–diferençasimétricaqueretornaoselementosqueestãoemapenas
umdosconjuntos.
Valelembrarque,noPython3.x–posteriormenteportadoparaafamília
2.7–,existeasintaxeliteraldeconjuntos,queécomosefosseumalistaou
umatupla,mascomchaves(comoem {2, 4, 6} ,oconjuntocomosnú-
meros2,4e6).Asintaxeliteraldeconjuntossuportaatémesmooformato
de comprehension,queveremosmaisàfrenteequeserádetalhadomelhor
quandovermosrecursosmaisavan çadosdalinguagem,nocapítulo 13.
178
E-book gerado especialmente para 


## Página 195

CasadoCódigo Capítulo11. Umpasseioporalgunstiposdefinidosnabibliotecapadrão
11.4 Tuplas nomeadas: tuplas que parecem obje-
tos com atributos
Muitaslinguagensnãopossuemtuplase,paraquemestátendocontatocom
elaspelaprimeiravez,elaspodemparecermenosúteisdoquerealmentesão.
Umdosseususoscomunséalgosemelhantea structdoC,sepensarmos
nelacomoum containerdeoutrosobjetos.
Oproblemaaparenteéqueastuplas“comuns”exigemacessovianotação
deíndice:
>>> execucao = ( '1' , '2' , '132' , '-1' , '76' ,
... '696648486.09' , '0' , '19/03/2010' ,
... '23/03/2010' , '05/10/2013' )
>>> value = execucao[ 5 ]
>>> value
'696648486.09'
Astuplasnomeadassãosubclassesdastuplas,quepareceminstânciasde
classesdeusuário,masnãosão.Internamente,tuplasnomeadaseclassesde
usuáriosãomuitodiferentes. Oqueasfazsepareceremcomasclassesde
usuárioéquepodemosdefinirumnome,eumnomeparacadaatributoque
queremosdefinirnatuplanomeada.
Avantagemdatuplanomeadasobreumainstânciadeumaclasseéque
atuplaéumobjetomenor,emtermosdeespa çoemmemória. Seconside-
rarmosumaquantidadegrandedeobjetos,podesermaisvantajosotê-los
representadosemtuplasnomeadasdoqueeminstânciasdeclasses“regula-
res”.
Éclaroquepodemosusartuplasnormaissempre,porém,afacilidadede
acessaratributosnasintaxe,semelhanteaoacessodeatributosdeumains-
tânciadeclasse,émuitoconveniente.
Vejacomopoderíamosutilizá-la:
from collections import namedtuple
ExecucaoFianceira = namedtuple('ExecucaoFianceira',
['IdExecucaoFinanceira',
'IdEmpreendimento',
179
E-book gerado especialmente para 


## Página 196

11.5. Conclusão CasadoCódigo
'IdInstituicaoContratado',
'IdPessoaFisicaContratado',
'IdLicitacao',
'ValContrato',
'ValTotal',
'DatAssinatura',
'DatInicioVigencia',
'DatFinalVigencia'])
execucao = ExecucaoFianceira(
'1',
'2',
'132',
'-1',
'76',
'696648486.09',
'0',
'19/03/2010',
'23/03/2010',
'05/10/2013'
)
print(execucao.ValContrato)
print(execucao)
Nacriaçãoda namedtuple,primeirodefinimosseunomee,depois,em
umalista,definimososnomesdosseusatributos.Maistarde,podemoscriar
instânciasdessatuplanomeadaereferenciarosatributospelosseuspróprios
nomesemvezdesuaposi ção.
11.5 Conclusão
Nestecapítulo,vimosdecimais,datas,data/hora,hora,conjuntosetuplasno-
meadas.Pythonpossuimaistiposespeciaisdisponíveis,porémestesacabam
sendoosmaiscomuns.Vimoscomoelespodemnosajudarcomproblemas
dodiaadiaeamelhorar.Namaioriadoscasos,ésempremelhorprocurarse
jánãoexistealgoqueprecisamos,poisusarasimplementa çõesoficiaispode
nospoupardemaisuma“reinvençãodaroda”.
180
E-book gerado especialmente para 


## Página 197

CasadoCódigo Capítulo11. Umpasseioporalgunstiposdefinidosnabibliotecapadrão
Sevocêquiservermaisalgumtipoespecialexplicadoaquinapróxima
edição,entreemcontatopelosite http://livropython.com.br/. Valetambém
lembrardanossalistadediscussão,emlivro-python3@googlegroups.com.
Nopróximocapítulo,veremosalgunsconceitosepadrõesadotadosna
linguagem,comoobjetositeráveis,closureseoutros.
181
E-book gerado especialmente para 


## Página 198

E-book gerado especialmente para 


## Página 199

Capítulo12
Conceitosepadrõesda
linguagem
ExistemalgunsconceitosepadrõesnouniversoPythonquesãomuitoco-
munsdeseremusadosoucitadosemdocumenta ções,tutoriaiseoutrosma-
teriais.Atéentão,focamosnosaspectosmaisbásicosefundamentaisdalin-
guagem.
Agora,vamosveralgunsconceitosumpoucomaisavan çadosequeex-
plicamdeterminadoscomportamentosoufuncionalidadesdalinguagem.A
terminologiatambéméimportante,poistornaacomunica çãocomoutros
pythonistasmaisfácil,jáquemuitosestão(ouestarão)familiarizadoscom
algumascoisasqueveremosagora.
E-book gerado especialmente para 


## Página 200

12.1. Iteráveiseporqueocomandoforfunciona? CasadoCódigo
12.1 Iteráveis e por que o comando for funci -
ona?
Jávimoscomorealizarloopsemcole ções–comolistasoudicionários–,
usandoocomando for,mas,nomaterialdolivro,nãofoiexplicadopor
qualrazãoelefunciona. Essecomandopodeserusadocomdiversostipos
deobjetos,desdequeelessejam iteráveis.Diversosobjetosdalinguagemsão
iteráveis,comolistas,strings,tuplasetc. Essacaracterísticafoiincorporada
pelaPEP-234[5],queintroduziuoconceitodeinterfacedeitera ção.
Masoquesignificaumobjetoseriterável?Paraqueissoserve?
Iteráveléqualquerconjunto–sejalista,dicionáriooutupla–,quepode
terseuselementosvisitadosumaum,emumaordemqualquer.
Naprática,umagrandevantageméquepodemosplugarqualquerob-
jetodentrodo for,inclusiveosquenóscriamos,desdequeotornemosum
iterável. Umobjeto,paraserconsideradoiterável,temdeimplementar
ométodo __iter__(). Geralmente,aimplementaçãoretornaumobjeto
chamadodeiterador( iteratoreminglês),que,casoimplementeambososmé-
todos __iter__()e __next__(),podeserplugadonocomando for.
Podemospensarqueumobjetoquerepresentaumaconsulta,ouuma
query,podeserumiterável.Mas,comoconseguimosisso?
Paratal,vamoscriarumobjetoiterávelquelê,registroaregistro,oar-
quivodedadosenuncacriaumobjetocomtodoselesemmemória,simulta-
neamente.Seesseobjetoforumiterador,podemosusá-lonocomando for.
Vamosvercomoesseobjetoseria:
# coding: utf-8
from decimal import Decimal
total = Decimal( '0' )
def dec (element, index):
try :
return Decimal(element[index])
except :
return Decimal( '0' )
184
E-book gerado especialmente para 


## Página 201

CasadoCódigo Capítulo12. Conceitosepadrõesdalinguagem
class QueryFile ():
def __init__ ( self , filename):
self . _file = open (filename, "r" )
def __iter__ ( self ):
return self
def __next__ ( self ):
data = self . _file . readline()
if not data:
self . _file . close()
raise StopIteration
return data . split( ';' )
query = QueryFile( 'data/data/ExecucaoFinanceira.csv' )
total = sum (dec(element, 5 ) for element in query)
print ( "Total gasto: {}" . format(total))
Reparequeeliminamoscompletamenteousodelistas.Oobjetodotipo
QueryFileéoobjeto iteradorqueusamosparapercorrertodososregistros
doarquivodedados.Elequemantémareferênciaparaoarquivoaberto,que,
porsuavez,mantématualizadooponteirodaspróximasleiturasdedados
eavança,linhaalinha,usandoafun ção readline(),quelêapenasuma
linhaquandoéchamada.
Outrodetalheimportanteéqueofinaldopercursoésinalizadocomage-
raçãode StopIteration.Podemosdizerquenossaclasse QueryFileim-
plementaoprotocolode iteráveis(iterator protocol),portanto,podeserusada
comocomando for.
12.2 Objetos chamáveis: callables()
UmoutrotermoextremamenteutilizadonouniversoPythoné callable.Um
objetoquepodeserinvocadocomasintaxedechamada,usandoparênteses,
éum callable.Osmaioresexemplosdecallablessãoasfun çõeseosmétodos.
185
E-book gerado especialmente para 


## Página 202

12.2. Objetoschamáveis:callables() CasadoCódigo
Ométodoconstrutor,porexemplo,funciona,poisemPythonasclassessão
callables,eoatodechamaroconstrutorpelaclassedisparaachamadado
método __init__(),definidoporela.
Ograndedetalheéqueépossíveltornarqualquerclasseumcallable.
Bastaqueestaimplementeométodoespecial __call__().Podemosmo-
dificaroexemploanterior,fornecendoumainterfacedeconsultapormeio
dasintaxedechamada,semutilizarummétodo,massim,ummecanismode
chamada.
Vejaoexemplo:
# coding: utf-8
from decimal import Decimal
class QueryFile ():
def __init__ ( self , filename):
self . _file = open (filename, "r" )
def __iter__ ( self ):
return self
def __next__ ( self ):
data = self . _file . readline() . split( ';' )
if not data or len (data) == 1 :
self . _file . close()
raise StopIteration
returned_el = []
for position in self . positions:
if len (data) >= position:
returned_el . append(data[position])
return returned_el
def __call__ ( self , * args):
self . positions = args
return self
186
E-book gerado especialmente para 


## Página 203

CasadoCódigo Capítulo12. Conceitosepadrõesdalinguagem
query = QueryFile( 'data/data/ExecucaoFinanceira.csv' )
for data in query( 5 , 7 ):
print ( "Execucao no valor de {} assinada {}" . format(
data[ 0 ], data[ 1 ]))
Repareque,nachamadaà query(),passamososíndicesdosatributos
quequeremosver. Comainforma çãodosmetadados,podemostrocá-los
parareceberasstringsqueidentificamoscampos,comodescritonoarquivo
demetadados.
12.3 Protocolos abstratos : como comporta -
mentos padronizados funcionam
Osprotocolosabstratossãoumaoutracaracterísticamuitoimportantedalin-
guagemPython.Essesprotocolosdefinemconjuntosdecomportamentosque
padronizamousodealgunsobjetos. Oexemplomaiscomumequejáfoi
mencionadonolivroéoprotocolode sequência.
Seanalisarmos,ousodelistasestringsémuitosemelhanteemmuitos
aspectos.Emambas,podemosacessarelementosporumíndiceou slice,testar
apresençadeumelementonelaseperguntarotamanho.Vejaosexemplosa
seguir,pararelembrar:
>>> st = "gastos publicos"
>>> len (st)
15
>>> st[ 0 ]
'g'
>>> st[ -1 ]
's'
>>> "g" in st
True
>>> gastos = [ 1000.0 , 2000.0 , 3000.0 ]
>>> gastos[ 0 ]
1000.0
>>> gastos[ -1 ]
3000.0
187
E-book gerado especialmente para 


## Página 204

12.4. ClosuresemPython CasadoCódigo
>>> 1000.0 in gastos
True
Mesmo sendo objetos completamente diferentes, sua manipulação é
igualparaessasopera ções. Issoporqueambosimplementamoprotocolo
de sequência. Atémesmoocomportamentodosobjetositeráveisédefi-
nidoporumprotocoloabstrato,queexigeaimplementa çãodosmétodos
__iter__()e __next__().
Osdicionáriosimplementamoprotocoloabstratodemapas(eminglês,
mapping).Osmapastambémpermitemaperguntapeloseutamanho,ope-
didodeumvalordadaumachaveeaitera çãonatuplachave/valor. Érela-
tivamentecomumencontrarmosmateriaisnainternetqueafirmamquetal
objetoé “dict-like
.Issosignificaquepodemosmanipulá-loequeelenãoénecessariamente
umdicionário–comosefosseum–,jáqueprovavelmenteimplementao
protocoloabstratodemapas.
Veremosmaisconcretamenteosprotocolosabstratosnocapítulo 14.
12.4 Closures em Python
EmPython,temosescopoléxicoe funções de primeira classe.Comessesele-
mentos,podemosusarumatécnicachamadade closure.
Atécnicaconsisteemretornarumafun çãoqueuseinternamentevariá-
veis(ounomes)dafun çãoqueadefine.
Imaginequequeremosumafun çãoqueretorne True,casoumvalorseja
maiorque 100000.
Poderíamosescrevê-ladaseguinteforma:
>>> def greater_100K (val):
... return val > 100000
...
>>>
>>> greater_100K( 99999 )
False
>>> greater_100K( 99999 + 2 )
True
188
E-book gerado especialmente para 


## Página 205

CasadoCódigo Capítulo12. Conceitosepadrõesdalinguagem
O problema do código anterior é que ele está amarrado ao número
100000,dentrodafun çãodocódigo.Com closures,podemoscriaralgomais
eleganteeflexível,quepermitaqueasfun çõessejamcriadasemtempode
execução,deacordocomosvaloresescolhidos.Vejaoexemplo:
>>> def greater (fixed_val):
... def _greater (val):
... return val > fixed_val
... return _greater
...
>>> greater_100K = greater( 100000 )
>>> greater_100K( 99999 )
False
>>> greater_100K( 99999 + 2 )
True
Essetipode“técnica”émuitocomumemprogramaçãofuncionaleem
Python,jáqueestaéumalinguagemmultiparadigma,oquetornaissopos-
sível.
MesmonãosendoalgoexclusivodePython,pessoasqueconhecemou-
traslinguagenspodemnuncatertidocontatocomclosures. Éimportante
saberoquesãoecomousá-lasemPython.
12.5 Conclusão
Oobjetivodestecapítulofoitransmitirumapartedaterminologia,quese
manifestaemcaracterísticasdalinguagem,técnicasdeprograma ção,padrões
deprojetoedeoutrasformas.
UmalinguagemdemuitoaltonívelcomoPythonpode,emumprimeiro
olhar,tornartudotãosimplesqueosdetalhespassamsemseremnotados.
Emumsegundomomento,algunsdesenvolvedoressequestionarãomaisso-
brecomoascoisasfuncionam.Nestasegundapartedolivro,continuaremos
vendoaspectosdaimplementa çãoedesigndalinguagem,oqueelespermi-
temecomousá-los.
189
E-book gerado especialmente para 


## Página 206

E-book gerado especialmente para 


## Página 207

Capítulo13
Elementoscomsintaxeespecífica
Agora,veremosalgunselementosespecíficosdelinguagem,quetalveznão
sejamexclusivos,mascertamentesãomarcantesnouniversoPython.Vamos
mudarumpoucoaabordagemdolivro.Emvezdeiniciarasexplica çõescom
asmotivaçõespráticas,vamosvergradativamenteonovoelementoapresen-
tadoe,aofinaldecadase ção,umexemploaplicadoaocontextodonosso
programa.
13.1 List comprehensions
Umavaria çãonasintaxequecausacertaestranheza,principalmentepara
quemvemdelinguagenscomsintaxesmaistradicionais–comoCouJava–,
éalist comprehension.Umatarefamuitocomumemprogramasécriarlistasa
partirdeoutraslistas,oudentrodeloops.Issopodeserfeitocomocomando
forquejávimos,masa list comprehensionforneceumaformamaiselegante,
E-book gerado especialmente para 


## Página 208

13.1. Listcomprehensions CasadoCódigo
emmuitoscasos,desefazeromesmo.Noiníciodolivro,usamosocomando
forparaimprimirosnúmerosde0até4:
>>> for i in range ( 5 ):
... print (i)
...
0
1
2
3
4
Essecódigopodeserfacilmenteadaptadoparaqueumalistacomosnú-
merosimpressossejacriada:
>>> numbers = []
>>> for i in range ( 5 ):
... numbers . append(i)
...
>>> numbers
[0, 1, 2, 3, 4]
Asintaxede list comprehensionmisturaumasintaxededeclara çãodelista
comocomando fordentrodela.
>>> numbers = [i for i in range ( 5 )]
>>> numbers
[0, 1, 2, 3, 4]
Aqui,vemosqueoblocoqueseriaexecutadoparacadavalorde ivirou
umaexpressão,queéretornadaonúmerodevezesqueaexpressãodo for
–nocaso,range(5)–retornarumelemento. Dessaforma,conseguimos
criaressalistadenúmeroscomapenasumalinha.Alémdisso,oselementos
retornadospodemsermanipulados,eatécondicionaispodemsercolocadas
nomeio:
>>> numbers_times_2 = [i *2 for i in range ( 5 )]
>>> numbers_times_2
[0, 2, 4, 6, 8]
192
E-book gerado especialmente para 


## Página 209

CasadoCódigo Capítulo13. Elementoscomsintaxeespecífica
>>> evens = [i for i in range ( 5 ) if i % 2 == 0 ]
>>> evens
[0, 2, 4]
Indomaisalém,damesmaformaquepodemosaninharcomandos for,
podemosaninhar list comprehensions. Vejaoexemplousandoocomando
for,semasintaxenova:
>>> nested = []
>>> for i in range ( 2 ):
... for j in range ( 3 ):
... nested . append((i, j))
...
>>> nested
[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]
Agora,omesmocódigousando list comprehension:
>>> nested = [(i, j) for i in range ( 2 ) for j in range ( 3 )]
>>> nested
[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]
Noprimeiroexemplodocapítulo 12(seção12.1),criamosumcódigoque
somaovalordetodasasexecu çõesfinanceiras.Podemostornaraquelecódigo
maiselegantecomoempregode list comprehensions.
# coding: utf-8
from decimal import Decimal
total = Decimal( '0' )
def dec (element, index):
try :
return Decimal(element[index])
except :
return Decimal( '0' )
with open ( 'data/data/ExecucaoFinanceira.csv' , 'r' ) as data:
splited_data = [line . split( ';' ) for line in data]
193
E-book gerado especialmente para 


## Página 210

13.2. Dictscomprehensions CasadoCódigo
total = sum ([dec(element, 5 ) for element in splited_data])
print ( "Total gasto: {}" . format(total))
Aplicamos list comprehensionsduasvezes. Aprimeirafoiparamontar
umalistadelistas. Avariável splited_dataéumalistaderegistrosdo
arquivodeexecu çõesfinanceiras,ecadaelementodestaéumalistacomos
valoresdescritosnoarquivodemetadadosparatabela.
Seficouumpoucoconfuso,vejacomodeveficaraestruturadoobjeto
splited_data:
splited_data = [
[ 1 , 'DOC001' , ... , 'Decimal(' 12345.00 ')' ],
[ 2 , 'DOC002' , ... , 'Decimal(' 12345.00 ')' ],
[ 3 , 'DOC003' , ... , 'Decimal(' 12345.00 ')' ],
[ 4 , 'DOC004' , ... , 'Decimal(' 12345.00 ')' ]
]
Notequeconstruímos,comapenasumalinha,umalistadelistas.Dessa
estrutura,nósmontamosumaoutralista,apenascomacolunadeíndice5,
queéacolunacomovalorquequeremos.
A função sum() recebe algo como [Decimal(‘123.00’),
Decimal(‘321.00’)], e soma todos os elementos. O detalhe im-
portante é que, a partir do arquivo, montamos uma lista com todos os
dados, cujotamanhoestáamarradoaonúmeroderegistros. Ouseja, se
temos100milelementos,vamosterumalistacom100milelementos,todos
simultaneamenteemmemória.
Talvezissonãosejaumproblemaemumprogramaquecalculaasoma
elogotermina,porém,emprocessosdelongadura çãoecomváriosclientes,
comoemsistemasweb,nãoqueremosficarcriandolistasgigantescasname-
mória.Nase ção13.5,sobre funções geradoras,veremoscomocontornaressa
situação.
13.2 Dicts comprehensions
Deformaanálogaà list comprehensions,a dict comprehensionfuncionada
mesmaforma,porémoresultadoéumdicionário.Noexemplo,vamosvera
194
E-book gerado especialmente para 


## Página 211

CasadoCódigo Capítulo13. Elementoscomsintaxeespecífica
função zip(),queébemcomumemprogramasPythonparacriardicioná-
riosapartirdelistas.
Imagine que queremos que cada resultado seja um dicionário, em
queachaveéonomedoatributoeovaloréoprópriovalordesseatri-
buto. Porexemplo, podemosterumobjetocomo {‘NumDocumento’:
‘2014NE800370’, ‘ValContrato’: ‘Decimal(‘13499.20’)’} .
Vejaoexemploaseguir:
# coding: utf-8
from decimal import Decimal
total = Decimal( '0' )
schema = ( 'NumDocumento' , 'ValContrato' )
def dec (element, index):
try :
return Decimal(element[index])
except :
return Decimal( '0' )
with open ( 'ExecucaoFinanceira.csv' , 'r' ) as data_file:
splited_data = [line . split( ';' ) for line in data_file]
data = [(element[ 2 ], dec(element, 12 )) for element in
splited_data if len (element) > 2 ]
result = [{key:value for key, value in zip (schema, element)}
for element in data]
for info_dict in result:
print ( "{}" . format(info_dict))
Reparequeoselementosde resultsãoosdicionárioscriadoscoma dict
comprehension.Afun ção zip()tambémnosajudou,permitindoqueatupla
schema,comacole çãodeatributos,ealistadedadosquequeremossejam
iteradassimultaneamente,demodoquesejapossívelcriarumdicionárioque
junteessasduaslistas.Oresultadodesseprogramaseriaalgocomo:
...
{'NumDocumento': '"2014NE800934"',
195
E-book gerado especialmente para 


## Página 212

13.3. Decoradoresdefunção:@decorators CasadoCódigo
'ValContrato': Decimal('445.10')}
{'NumDocumento': '"2014NE800316"',
'ValContrato': Decimal('368.62')}
{'NumDocumento': '"2014NE801005"',
'ValContrato': Decimal('38950.00')}
{'NumDocumento': '"2014NE800317"',
'ValContrato': Decimal('95.89')}
{'NumDocumento': '"2014NE800318"',
'ValContrato': Decimal('222.16')}
...
Talveza dict comprehensionnãosejatãocomumquantosuaversãoem
lista,masseuempregoérelativamentecomume,quandousadanasitua ção
maisadequada,podedeixarocódigomaiseleganteesucinto.
13.3 Decoradores de função :@ decorators
Nocapítulo3,vimosque,emPython,asfun çõessãoobjetoscomotodosos
outros,comumentechamadasde first class objects. Porisso,podemoscriar
funçõesquerecebemoutrascomoparâmetro,eretornamfun çõestambém.
Especialmente,essacombina çãodereceberumafun çãoeretornaroutraé
umadasformascomoum decoratorpodeserimplementado.
Naprática,o decoratoréummecanismodesintaxequechamaumafun-
ção,passandooutracomoparâmetro,ouchamaoconstrutordeumaclasse,
passandoumafun çãocomoparâmetro.Pensandoemaltonível,um decorator
éumainformaçãodeclarativasobreumafun çãoemquestão.Elenospermite
adicionarcomportamentosextrasafun çõesexistentes,deformadeclarativa.
Issoéumrecursoquepertenceàmetaprograma ção.
Exemplopráticodousodeumdecorator
Vimos um uso prático no capítulo 7, quando usamos o decorator
@property.Essedecoradoréumencapsuladordoacessoaatributosdeum
objeto,istoé,elepermitequesejamdefinidasfun çõesqueserãochamadasno
casodetrêsoperaçõescomobjetos:
• Acesso,comoemtable.name;
196
E-book gerado especialmente para 


## Página 213

CasadoCódigo Capítulo13. Elementoscomsintaxeespecífica
• Atribuição,comoem table.data = [] (vejaquevalequalquertipo
deatribuiçãoválida);
• Remoção,comoem del table.data.
EmPython,nãoexistemvariáveisprivadas,masexisteaconven çãode
seusarum underscore( _)antesdonomedasvariáveis,parapassaressesig-
nificado. Paraquetodoorestodoprogramanãouseessavariávelprivada
diretamente,podemosdefinirumapropriedadequearepresenta. Paraela,
podemosassociarfun çõesqueserãoexecutadasnostrêseventosdescritos
anteriormente.Vamosverumexemplomuitosimples:
>>> class Column:
... def __init__(self, name):
... self._name = name
... @property
... def name(self):
... return self._name
... def other_name(self):
... return self._name
...
>>> col = Column('Name')
>>> col.other_name
<bound method Column.other_name of <__main__.Column object at
0x1053a6588>>
>>> col.name
'Name'
Oobjetivododecorator @propertyécriarumatributoartificialcha-
mado name,querepresentaoacessodeleituraàvariável _name. Repare
queaimplementa çãode nameede other_namesãoiguais,mascomo
other_namenãoestácomodecorator @property,areferênciaparaela,
semousodasintaxedechamadadefun çãocom (),fazcomqueumains-
tânciadométodosejaretornadaemvezdeométodoserinvocado. Como
decorator @property,areferênciaa col.nameinvocaométodo namee,
porisso,oretornoéovalorde _name.
Deformasemelhante,podemosdefinirumencapsuladorparaatribui ção
devalores,paraumatributodeumobjeto.Porexemplo,quandocriamosuma
197
E-book gerado especialmente para 


## Página 214

13.3. Decoradoresdefunção:@decorators CasadoCódigo
coluna,nãoqueremosqueovalordoseunomemudeemtempodeexecu ção.
Paraisso,devemosimpedirquenovosvaloressejamatribuídos.Issopodeser
feitocomum setter.Vejaoexemplo:
>>> class Column:
... def __init__(self, name):
... self._name = name
... @property
... def name(self):
... return self._name
... @name.setter
... def name(self, value):
... raise Exception("Nome não pode mudar")
... @name.deleter
... def name(self):
... pass
...
>>>
>>> col = Column('Name')
>>> col.name = 'New Name'
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File "<stdin>", line 9, in name
Exception: Nome não pode mudar
Nodiaadia,podemosverdecoradoresqueexploramapenasofatode
seremchamadosquandoafun çãoéchamada,masnãoalteramoresultado
dachamadaoriginal,eoutrosqueofazem,oualteramaprópriachamada
original.
Aseguir,vamosveremdetalhescomoomecanismofunciona,paraque
fiquemmaisclarostodososrecursosdisponíveisqueganhamosaoutilizar
decorators.
Comofuncionaumdecorator?
EmPython, podemosimplementarum decoratordeduasformas. A
formamaiscomumédefinindo-ocomoumafun ção;aoutra–menosco-
mum,porémigualmentepoderosa–éusandoumaclassecommétodoses-
198
E-book gerado especialmente para 


## Página 215

CasadoCódigo Capítulo13. Elementoscomsintaxeespecífica
peciais. Primeiro,vamosveremmaisdetalhesaprimeiraforma,edepois
veremosasegunda.
Antesdepensarnodecorator,penseemumafun çãoquerecebeumafun-
çãocomoparâmetro.
>>> def uma_funcao ():
... print ( "uma_funcao" )
...
>>> def outra_funcao (func):
... print ( "outra_funcao" )
... func()
...
>>> outra_funcao(uma_funcao)
outra_funcao
uma_funcao
Comovimosnase ção3.11,asfun çõessãoobjetosdeprimeiraclasse,por-
tantopodemserpassadascomoparâmetrosparaoutrasfun ções.Atéaí,ne-
nhumanovidade.
Essacaracterísticatambémpermitequeumafun çãosejaretornadapor
outra.Vejaoexemplo:
>>> def uma_funcao_com_args(param):
... print("uma_funcao param {}".format(param))
...
>>> def outra_funcao(func, *args):
... print("Irei chamar {}".format(func.__name__))
... return func(*args)
...
>>> outra_funcao(uma_funcao_com_args, [1, 2, 3])
Irei chamar uma_funcao_com_args
uma_funcao param [1, 2, 3]
Reparequeusamos outra_funcao()apenasparaescreverqualfun ção
vamoschamar.Vejaque,comotemosorecursodo packing,conseguimosusar
esserecursoparaumcasogenéricocomo:
>>> outra_funcao( sum , [ 1 , 2 , 3 ])
Irei chamar sum
199
E-book gerado especialmente para 


## Página 216

13.3. Decoradoresdefunção:@decorators CasadoCódigo
6
>>> outra_funcao( max , [ 1 , 2 , 3 ])
Irei chamar max
3
Alémdeconseguirexecutarumcódigoarbitrário(nocaso,apenasum
print),conseguimosexecutarafun çãopassadacomoparâmetro,comores-
tantedosparâmetros.
Afunçãodosdecoradoreséadicionar,deformadeclarativa,umcompor-
tamentoextraaumafun ção.Essafacilidadeémuitoútileelegante.
Oexemplorealqueveremoslogoaseguirmostraum decoratorqueim-
primenasaídapadrãoonomedafun çãochamadaeosargumentospassados
paraela.Todafun çãoqueestivercomessenossodecoradorganharáessenovo
comportamento.
Esseseriaoexemplomaisbásicodeumdecorator.Vejaoexemplo:
def trace_call (func):
def inner ( * args, ** kwargs):
print ( "Function executed: {} args: {}" . format(
func . __name__, args))
func( * args, ** kwargs)
return inner
@trace_call
def add (x, y):
return x + y
add( 5 , 1 )
Geraasaída:
Function executed: add args: (5, 1)
Primeiro,vejaque trace_call()éafun çãodecoradora. Afun ção
quechamamosdeoriginal,nesseexemplo,é add(),eafun çãoretornadaé
inner().
Agora,vamosentendertodososdetalhes.Afun ção trace_calléum
decoratorquefoiimplementadocomofun ção.Dentrodela,definimosuma
200
E-book gerado especialmente para 


## Página 217

CasadoCódigo Capítulo13. Elementoscomsintaxeespecífica
outrafunção,chamada inner,que,quandochamada,imprimeumainfor-
maçãonatelaechamaafun çãooriginal add(),representadapelavariável
func,comosparâmetrosoriginais.
Alémdisso,afun çãodecoradora trace_calltemderetornarumare-
ferênciapara inner. Assim,quandochamamos add(),internamentea
funçãochamadaé trace_call(),querecebeafun ção add()comoparâ-
metroeretorna inner.Estaexecutaumatarefaqualquere,depois,executa
add().
Dessaforma,todafun çãodecoradacom @trace_call,antesdeserexe-
cutada,temseunomeeseusargumentosimpressos.
Quandodefinimosumdecorator,podemosinclusiveadicionarparâme-
trosnachamadaoriginal,mudarparâmetros,ouqualqueroutracoisaqueseja
compatível.Omaiorpontodeaten çãoéqueosdecoratorsprecisamterum
objetivobemdefinidoerealmentetornaroprogramamaisreusáveleclaro.
Paraimplementarum decoratorusandoumaclasse,vocêdevecriaruma
classequeimplementaométodoespecial __call__(). Vejaodecorador
trace_callreimplementadocomoclasse:
class trace_call :
def __init__ ( self , f):
self . f = f
def __call__ ( self , * args, ** kwargs):
print ( "Function executed: {} args: {}" . format(
self . f . __name__, args))
self . f( * args, ** kwargs)
@trace_call
def add (a, b):
return a + b
add( 1 , 3 )
Esseprogramageraasaída:
Function executed: add args: (1, 3)
201
E-book gerado especialmente para 


## Página 218

13.4. Funçõesanônimas:lambdas CasadoCódigo
13.4 Funções anônimas : lambdas
Asfunçõesanônimassãoempregadas,geralmente,quandoumadeterminada
funçãoforusadasomenteumavez,oupoucasvezes.Aideiadefun çãoanô-
nimaéamplamentedifundidanaslinguagensfuncionais.Python,comolin-
guagemmultiparadigma,temasuaversão,quesãochamadasde lambdas.
EmPython,oslambdasnãopodemcontercomandos( statements),de-
coradoresenemmúltiplaslinhas,maspodemconterváriasexpressões.Um
empregopráticomuitocomuméseuusocomafun çãodabibliotecapadrão,
filter().
Aassinaturacompletaé filter(function, iterable),quechama
afunçãopassadaparacadaelementoe,quandoestaretorna True,afun ção
filterretornaesseelemento.
Nonossoaplicativo,podemospassarumlambdacomocritériodeum
filtro,queselecionavaloresmaioresqueumdeterminadonúmero:
# coding: utf-8
from decimal import Decimal
total = Decimal( '0' )
_100M = Decimal( '100000000' )
def dec (element, index):
try :
return Decimal(element[index])
except :
return Decimal( '0' )
with open ( 'ExecucaoFinanceira.csv' , 'r' ) as data:
splited_data = [line . split( ';' ) for line in data]
values = [dec(element, 12 ) for element in splited_data]
total = sum (values)
values_100M = filter ( lambda x: x > _100M, values)
total_gt_100M = sum (values_100M)
percent = lambda x, y: (x / y) * Decimal( '100' )
print ( "Total gasto: {}" . format(total))
202
E-book gerado especialmente para 


## Página 219

CasadoCódigo Capítulo13. Elementoscomsintaxeespecífica
print ( "Apenas contratos com mais de 100MI: {}" . format(
total_gt_100M))
print ( "Representam {:.2f}% do total" . format(percent(
total_gt_100M, total)))
Noexemploanterior,empregamoslambdasduasvezes: primeiro,pas-
sandoumafun çãoanônimaparafun ção filter,paraselecionarapenasva-
loresmaioresque100milhões;depois,atribuímosumlambdaaumavariável
–oqueéválido–,eafunçãodeixadeseranônima.
Issonãoéumproblema,eérelativamentecomumencontraratribui ções
defunçõesanônimasavariáveis,quandoessasfun çõesnãofazemnenhuma
declaraçãoouexecutamalgumcomandodentrodela.
Jáhouvetentativasdealteraralgumascoisasemlambdas,comoapossibi-
lidadedeusarváriaslinhasnasuadefini ção,masatéagoratodasfracassaram.
13.5 Funções geradoras
Umacaracterísticamuitorelevantenalinguageméaexistênciadefun ções
geradoras. Essetipodefun çãoespecialpermitealgoquepodeserimple-
mentadocomlistas,oucomumiterador,masemambososcasosexistem
problemas.
Imaginequequeremossomarototaldeexecu çõesfinanceiras,daforma
comofizemos,aplicandoafun ção sum(),emumalistamontadacomuma
list comprehension. Quandoalistaformuitogrande–como,porexemplo,
commaisde1milhãodeelementos–,jádevemospensarduasvezesseque-
remoscriarumobjetodessetamanhoemmemória.
Nocasodeumiterador,temosumpequenoproblema:énecessárioum
poucodecodifica çãoparacriá-lo.Felizmente,apróprialinguagemjápossui
umaformanaturalparatermosalgoquefuncionacomoumiterador,masque
nãoexigeacria çãodecole çõesemmemória.
Naprática,afun çãogeradorapermitequeelaretorneumelementoe,
quandoforchamadanovamente,consigarestauraroestadodeexecu çãoan-
terioreretornarumnovoelemento.Vejaoexemploquecomparaumafun ção
quegeraosnúmerosde1a10,usandoumalista,eumexemplocomumafun-
çãogeradora.
203
E-book gerado especialmente para 


## Página 220

13.5. Funçõesgeradoras CasadoCódigo
>>> def get_list ():
... numbers = []
... for i in range ( 10 ):
... numbers . append(i)
... return numbers
...
>>> for number in get_list():
... print (number)
...
0
1
2
3
4
5
6
7
8
9
>>> def get_generator ():
... for i in range ( 10 ):
... yield i
...
>>> for number in get_generator():
... print (number)
...
0
1
2
3
4
5
6
7
8
9
Semprequeusamosapalavrareservada yield,estamoscriandouma
funçãogeradora.Noexemplo,ficaclaroqueelaécapazdomesmoefeitoque
204
E-book gerado especialmente para 


## Página 221

CasadoCódigo Capítulo13. Elementoscomsintaxeespecífica
afunçãoquecriaumalista,porémelanãousaumalista.Afun çãogeradora
“gera”umvalortodavezqueé“chamada”e,aqui,usamosaspas,poisnãoé
umachamadacomum.Porpadrão,asfun çõesgeradoraspodemseriteradas
nocomando for,quejásabecomoobterosnovosvaloresgeradosporela.
Nonossoprogramaissoémuitoútil,pois,parapercorrermostodosos
dadosdosarquivos,nãoprecisamoscriarnenhumalistacomelesemmemó-
ria.Bastacriarmosumafun çãoque,acadalinha,geraumvalorparaafun ção
chamadora.
Vamosverumcódigoemespecíficoeexplicá-lologoemseguida:
>>> my_generator = get_generator()
>>> my_generator
<generator object get_generator at 0x1034d6120>
Repareque my_generatoréumobjetodotipo generator.Issosig-
nificaqueéumafun çãogeradora. Vamostentarobteroprimeirovalor,no
caso0(zero).
>>> my_generator()
Traceback (most recent call last):
File "<stdin>" , line 1 , in <module>
TypeError : 'generator' object is not callable
Uma função geradora não é chamável (callable), portanto te-
mos esse erro. Para obter os valores gerados, usamos a função
next(generator_function). Esta é que faz com que a função ge-
radorasejaexecutada,gereumelementoetenhaseuestadopreservado,até
queoutrachamadacom next()sejafeita.Vejaoexemplo:
>>> my_generator = get_generator()
>>> next (my_generator)
0
>>> next (my_generator)
1
>>> next (my_generator)
2
>>> next (my_generator)
3
205
E-book gerado especialmente para 


## Página 222

13.6. Palavrareservadanonlocal CasadoCódigo
>>> next (my_generator)
4
>>> next (my_generator)
5
... # outras execuções
>>> next (my_generator)
9
>>> next (my_generator)
Traceback (most recent call last):
File "<stdin>" , line 1 , in <module>
StopIteration
Repare que, quando os elementos terminam, temos uma
StopIteration, que é justamente a exceção que temos que levantar
noiteradorquandonãohouvermaiselementospararetornar.Issoporqueas
funçõesgeradorassãoiteráveis( iterables).
Naprática,asfunçõesgeradorassãomuitousadasporqueresolvemopro-
blemadecriarobjetosquepodemocuparmuitoespa ço,deumaformabem
simples,usandoapenasumapalavrareservada.
Alémdisso,existemasexpressõesgeradores(eminglês, generator expres-
sions),quetêmsintaxesemelhanteàs list comprehensions,masnãocriamlistas
emmemória.
>>> sum (x for x in [ 10 ] *10 )
100
13.6 Palavra reserv ada nonlocal
Quandofalamosde closuresnocapítulo12(seção12.4),vimosqueumafun ção
poderetornaroutra,eafun çãoretornadapodeusarvariáveisdoescopoda
funçãoqueadefine.Vejaoutroexemplo:
>>> def make_counter (count):
... def counter ():
... return count
... return counter
...
>>> count = make_counter( 0 )
206
E-book gerado especialmente para 


## Página 223

CasadoCódigo Capítulo13. Elementoscomsintaxeespecífica
>>> count()
0
>>> count()
0
>>> count()
0
Aqui,afun çãointernausaumavariávelnoescopodaqueadefine. Se
vocêrodaressecódigo,verácomoresultado3zeros.
Masoquequeremosémodificarovalordocontadoracadachamada
dafunção count().Nessecaso,podemostentaralterarovalorde count
dentrodafun çãointerna.Vejaoexemploeoresultadoaseguir:
>>> def make_counter (count):
... def counter ():
... count += 1
... return count
... return counter
...
>>> count = make_counter( 0 )
>>> count()
Traceback (most recent call last):
File "<stdin>" , line 1 , in <module>
File "<stdin>" , line 3 , in counter
UnboundLocalError : local variable 'count' referenced before
assignment
Arazãodissoé,apesardepodermosler,nãopodemosalterarovalorde
countdentrode counter(). ComaPEP-3104[ 15],foiintroduzidoum
mecanismoformalparatornarissopossível.Apalavrareservada nonlocal
informaqueestamosusandoumavariável(ounome),definidaemumescopo
imediatoexterno.Comoseuuso,torna-sepossívelalterarovalorde count,
paratermosumcontadordeverdade.
Vejaoexemplo:
>>> def make_counter (count):
... def counter ():
... nonlocal count
207
E-book gerado especialmente para 


## Página 224

13.7. Conclusão CasadoCódigo
... count += 1
... return count
... return counter
...
>>> count = make_counter( 0 )
>>> count()
1
>>> count()
2
>>> count()
3
Nasversõesanteriores,conseguíamosalgosemelhanteaousarobjetos
mutáveis,comoumalista. Elespodemseralteradossemousodapalavra
nonlocal.Vejaoexemplo:
>>> def make_counter ():
... acc = []
... def counter (val):
... acc . append(val)
... return acc
... return counter
...
>>> count = make_counter()
>>> count( 1 )
[ 1 ]
>>> count( 2 )
[ 1 , 2 ]
>>> count( 3 )
[ 1 , 2 , 3 ]
Nofundo,aPEP-3104buscoudarmaisclarezaàlinguagem,oferecendo
umamaneiraexplícitaeabrangentedeusarmosorecursodealterarvariáveis
definidasemescoposexternos.
13.7 Conclusão
Nestecapítulo,vimosdiversosrecursosqueutilizamumasintaxeespecífica.
Alémdisso,vimosopropósitodecadaumdelesealgumasno çõesdecomo
208
E-book gerado especialmente para 


## Página 225

CasadoCódigo Capítulo13. Elementoscomsintaxeespecífica
utilizá-losnoseudiaadia. Essesrecursossãoextremamentecomunsem
códigosPythonqueencontraremosporaí.Logo,éimportantedominá-lose,
principalmente,aplicá-losquandoforamelhorop ção.
Maisàfrente,veremosalgunsassuntosmaisavan çadosdeclasses,eexpli-
caremosdiversosfatoresquenãoforammostradosnoprimeiromaterialde
classes.VamosvercomoomodelodeobjetosPythonintegra-secomalguns
aspectosdasintaxedalinguagem.
209
E-book gerado especialmente para 


## Página 226

E-book gerado especialmente para 


## Página 227

Capítulo14
Explorandoaflexibilidadedo
modelodeobjetos
OmodelodeclassesdePythonésimples,porémmuitoflexível.Nestecapí-
tulo,vamosalémdoqueaprendemosnocapítulo 7,paraaprenderoutrastare-
fasigualmenteimportantesquandoestamosdefinindoclassesparaosnossos
programas.Aofinaldocapítulo,saberemoscomocriarclasses,comtodosos
comportamentosmaiscomunsimplementados,everquaissãoecomoeles
funcionam.
Vamosvertambémalgunsmétodosespeciaisemecanismosimportantes
nosistemadeobjetosPython. Aofinal,jáestaremosaptosparaexplorare
obtermaisfacilidadesdosistemadeobjetos.
E-book gerado especialmente para 


## Página 228

14.1. Construtures:criandoobjetos CasadoCódigo
14.1 Construtures : criando objetos
Naprimeiraapresenta çãodeclasses,nocapítulo 7,vimosque,paradefinir
ométodoconstrutor,bastaimplementarométodo __init__()nanossa
classe.Essemétodoespecialéchamadoquandofazemosumainvoca çãono
objetodaclasse.Aausênciadeconstrutorfazcomque,automaticamente,a
classetenhaumconstrutorsemparâmetros.
>>> class DataTable :
... pass
...
>>> table = DataTable()
Casosejadefinidoumconstrutorquerecebeumparâmetro,jánãoémais
possívelinstanciarsempassá-lo:
>>> class DataTable :
... def __init__ ( self , name):
... self . _name = name
...
>>> table = DataTable( 'ExecucaoFinanceira' )
>>> table = DataTable()
Traceback (most recent call last):
File "<stdin>" , line 1 , in <module>
TypeError : __init__() missing 1 required positional argument:
'name'
EmPython,casosejamdeclaradosmaisdeummétodoconstrutor,oúl-
timoaserdeclaradoacabasendooquevale.Vejaoexemplo:
>>> class DataTable :
... def __init__ ( self , name):
... self . _name = name
... def __init__ ( self , data):
... self . _data = data
...
>>> t = DataTable( 'ExecucaoFinanceira' )
>>> t . _name
Traceback (most recent call last):
212
E-book gerado especialmente para 


## Página 229

CasadoCódigo Capítulo14. Explorandoaflexibilidadedomodelodeobjetos
File "<stdin>" , line 1 , in <module>
AttributeError : 'DataTable' object has no attribute '_name'
>>> t . _data
'ExecucaoFinanceira'
EmJava,existeapossibilidadedetermosdiversosconstrutorescomas-
sinaturasdiferentes.Entretanto,emPython,geralmenteissoseresolvecom
apenasumconstrutoreparâmetroscomvalorpadronizado.Vejaoexemplo
aseguir:
>>> class DataTable :
... def __init__ ( self , name, data = []):
... self . _name = name
... self . _data = data
...
>>> t = DataTable( 'ExecucaoFinanceira' )
>>> t . _data
[]
>>> t = DataTable( 'ExecucaoFinanceira' ,
data=['linha1', 'linha2'])
>>> t . _data
['linha1', 'linha2']
>>> t . _name
'ExecucaoFinanceira'
Reparequeoferecemosduasformasdecriarumobjeto DataTable,mas
usandoapenasumconstrutoreumparâmetrocomvalorpadronizado.
Oúltimodetalheemrela çãoaométodoconstrutoréquandoprecisamos
invocaroconstrutordasuperclassenoconstrutordasubclasse.Vamoslem-
brardaclasse PrimaryKey,queherdade Column.
class PrimaryKey (Column):
def __init__ ( self , table, name, kind, description = "" ):
Column . __init__( self , name, kind,
description = description)
self . _is_pk = True
Achamadaaoconstrutordasuperclassetemumdetalhemuitoimpor-
tante: elachamaométodo __init__diretonasuperclasse,epassaasua
instânciasubclasse,comoprimeiroargumentodoconstrutordasuperclasse.
213
E-book gerado especialmente para 


## Página 230

14.2. Representaçãotextualdeobjetos:fun çãoprint(),str()erepr() CasadoCódigo
>>> class Column :
... def __init__ ( self , name, kind, description = "" ):
... print ( type ( self ))
...
>>> class PrimaryKey (Column):
... def __init__ ( self , table, name, kind, description = "" ):
... Column . __init__( self , name, kind,
description=description)
... self . _is_pk = True
...
... def get_name ( self ):
... return self . _name
...
>>> pk = PrimaryKey( None , 'PK' , 'int' )
<class '__main__.PrimaryKey'>
Reparequeotipoimpressoé PrimaryKey.Issoporquepassamosuma
instânciade PrimaryKey,diretamenteparaoparâmetro selfdocons-
trutordasuperclasse(nocaso, Column). Essapassageméfeitapelalinha
Column.__init__().
Oúltimodetalheéqueconstrutoresnãopodemretornarexplicitamente
nenhum valor. Caso retorne, você ganhará umTypeError, com uma
mensagem semelhante a TypeError: __init__() should return
None, not ... .
14.2 Representação textual de objetos : função
print(), str() e repr()
Outrafuncionalidadecomum(eesperadaemlinguagenscomsuporteàOri-
entaçãoaObjetos)écomodefinirarepresenta çãotextualdeumaclasse.Mui-
tasvezesqueremosimprimir,noconsole,oconteúdodeumaclassedeuma
formaestruturada,semterqueficarimprimindotodososseusatributos,um
aum.
Sevoltarmosàsclassesdefinidasanteriormente,nocapítulo 7,eusarmos
umainstânciadelasnafun ção print(),veremosumarepresenta çãopadro-
nizadaque,muitasvezes,nãoéoquequeremosver.Vamosreverumcódigo
214
E-book gerado especialmente para 


## Página 231

CasadoCódigo Capítulo14. Explorandoaflexibilidadedomodelodeobjetos
simplificadodessecapítulo:
>>> class DataTable :
... def __init__ ( self , name):
... self . _name = name
...
>>> table = DataTable( "ExecucaoFinanceira" )
>>> print (table)
<__main__.DataTable object at 0x109277860>
Vejaqueoresultadodachamadadafun çãoretornaumtextogenérico.
Eleexibeomódulo __main__–porquefoidefinidonoconsole–,onome
daclasseeumarepresenta çãodoendere çoondeoobjetoseencontra.
Assimcomoemoutraslinguagens–comoJavaouC++–, épossível
customizararepresenta çãoemtextodenossasclasses. Emcadalinguagem
issoéfeitodeumaformaespecíficae,emPython,fazemosissoimplemen-
tandoumdedois(ouosdois)possíveismétodosespeciais: __str__()ou
__repr__().
Vamosverumexemplousando __str__():
class DataTable:
def __init__(self, name):
self._name = name
def __str__(self):
return "Tabela {}".format(self._name)
>>> table = DataTable( "ExecucaoFinanceira" )
>>> print (table)
Tabela ExecucaoFinanceira
>>> table
<__main__.DataTable object at 0x109277b00>
>>> str (table)
'Tabela ExecucaoFinanceira'
Deformasemelhante,podemosdefinirométodo __repr__():
>>> class DataTable :
... def __init__ ( self , name):
... self . _name = name
215
E-book gerado especialmente para 


## Página 232

14.3. Comparandoigualdadedeobjetos CasadoCódigo
... def __repr__ ( self ):
... return "Tabela {}" . format( self . _name)
...
>>> table = DataTable( "ExecucaoFinanceira" )
>>> print (table)
Tabela ExecucaoFinanceira
>>> table
Tabela ExecucaoFinanceira
>>> str (table)
'Tabela ExecucaoFinanceira'
ReprversusStr
Adocumentaçãodefinequearepresenta çãoretornadapelométodoes-
pecial __str__()éumarepresentação“informal”,usadaapenasquandoo
objetoépassadocomoparâmetroparaafun ção str(object),ouquando
passadoparaafun ção print().Repareque,noprimeiroexemplo,nase-
gundaexibiçãodoobjetocontinuamosvendosuarepresenta çãogenérica.
Ométodo __repr__()deveretornarumarepresenta ção“formal”,que
deveidealmentepermitirqueoobjetosejarecriadoapartirdasuarepresen-
taçãoemtexto.Seoobjetonãoimplementar __str__(),masimplementar
__repr__(),eleseráusadoquandoumarepresenta ção“informal”forsoli-
citada.Noconsole,quandoaentradaforapenasonomedeumavariável,a
suarepresentação“oficial”échamada,eométodo__repr__()éinvocado.
Essedetalhede __str__() versus __repr__()jáfoimuitodiscutido
nainternet.Oqueimportaéquesejausadooqueformaisconvenientepara
oseuprograma.
14.3 Comparando igualdade de objetos
Outra operação comum com objetos é a comparação de igualdade. Em
Python,comotudoéumobjeto,secompararmosasinstânciasdasclasses
quecriamosatéomomento,oresultadoserásempre False,poisnenhuma
delasimplementaométodoespecialdecompara ção. Issoocorreporqueo
mecanismodecompara çãopadrãocomparaosidentificadoresdosobjetos,
quesãoúnicosparacadainstância,mesmoqueelascontenhamexatamente
216
E-book gerado especialmente para 


## Página 233

CasadoCódigo Capítulo14. Explorandoaflexibilidadedomodelodeobjetos
osmesmosvalores.
Comoeupoderiasaberseduastabelassãoamesma?
Paratermosumacompara çãodeigualdadequeleveemconsidera ção
osvaloresdosatributosdoobjeto,temosqueimplementarométodoespe-
cial __eq__().Esteémuitosemelhanteaométodo equals()deJava,ou
Equals()deC #.
Suaassinaturadeveterumparâmetro,queéoobjetocomoqualains-
tânciaestásendocomparada. Dentrodessemétodo,podemos,então,fazer
umacomparaçãodeatributosquesejacompatívelcomnossodomínio.Por
exemplo,nonossoaplicativo,tabelascommesmonomesãoiguais.
Vejaoexemplo semaimplementaçãoométodo __eq__():
>>> class DataTable :
... def __init__ ( self , name):
... self . _name = name
...
>>> t1 = DataTable( "ExecucaoFinanceira" )
>>> t2 = DataTable( "ExecucaoFinanceira" )
>>> t1 == t2
False
>>> id (t1)
4510145448
>>> id (t2)
4510145392
Reparequeoresultadodacompara çãofoi False,porque,emborate-
nhammesmonome,sãoinstânciascomidentificadoresdiferentes.Quando
realizamosumacompara çãodeigualdadesemométodo __eq__()defi-
nido,osidentificadoressãocomparados.
Vamosagoraaoexemploemqueométodo __eq__()éimplementado:
>>> class DataTable :
... def __init__ ( self , name):
... self . _name = name
... @property
... def name ( self ):
... return self . _name
217
E-book gerado especialmente para 


## Página 234

14.4. Outrostiposdecomparaçõesbinárias CasadoCódigo
... def __eq__ ( self , other):
... return self . name == other . name
...
>>> t1 = DataTable( "ExecucaoFinanceira" )
>>> t2 = DataTable( "ExecucaoFinanceira" )
>>> t1 == t2
True
>>> id (t1)
4510145952
>>> id (t2)
4510146008
Agora,mesmotendoidentificadoresdiferentes,acompara çãoretornou
True.Internamente,acompara ção t1 == t2 invocaométodo __eq__()
em t1,passando t2comoparâmetro.
Sabendodisso,bastacolocaralógicadecompara çãodentrodessemé-
todo. Nonossocaso,astabelasquetêmomesmonomesãoiguais. Éclaro
que,dentrodessemétodo,vocêdevefazerascompara çõesqueforemneces-
sárias,paraqueseudomínioestejabemrepresentadonocódigo.
Método cmp() removido na versão 3.x
Emmuitasversõesdafamília2,acompara çãoerafeitapormeiodo
métodoespecial __cmp__.Oprotocoloqueessemétododeveriaobede-
cerimplicavaem“forçar”umaordemartificialemobjetosque,seman-
ticamente,podemnãoterrela çãodeordem. Oproblemaéque,pelo
protocolo,ouumémaiorqueooutro,ouelessãoiguaiseficaimpossível
representaraausênciadeordem,semdizerqueelessãoiguais.
Maistarde,issofoiconsideradoruim.Então,foidecididoqueseriam
criadosummétodoporoperadordecompara ção,como ==, >eoutros.
Naversão3.xtemoso __eq__()eoutrosqueveremosnasequência.
14.4 Outros tipos de comparações binárias
Já sabemos que a comparação com var1 == var2 invoca o método
__eq__()em var1,passandocomoparâmetro var2. Eissovalepara
218
E-book gerado especialmente para 


## Página 235

CasadoCódigo Capítulo14. Explorandoaflexibilidadedomodelodeobjetos
outrasoperaçõestambém.Paracompactarainforma ção,vamosveratabela
aseguir,quemapeiaosmétodosespeciaisaoscomparadores:
object.__lt__(self, other) | x < y
object.__le__(self, other) | x <= y
object.__ne__(self, other) | x != y
object.__gt__(self, other) | x > y
object.__ge__(self, other) | x >= y
Paracadamétodoimplementado,ganhamosaop çãodeusaraexpressão
correspondente. Dessaforma,seimplementarmos __lt__(),poderemos
usar var1 < var2 .Vamosverumexemplo:
>>> class TesteLT :
... def __init__ ( self , n):
... self . n = n
... def __lt__ ( self , other):
... return self . n < other . n
...
>>> TesteLT( 3 ) < TesteLT( 4 )
True
>>> TesteLT( 4 ) < TesteLT( 3 )
False
Esseexemploilustrabemoempregode __lt__().Nãoéextremamente
comumimplementaralgumdessesmétodos,porém,éimportantesaberque
elesexistemecomofuncionam.
14.5 Dicionário interno de atributos
Comojámencionadonoiníciodolivro,Pythonimplementaváriasdesuas
funcionalidadesusandosuasestruturasdedados. A priori,todososobje-
tostêmseusatributosguardadosemumdicionáriointerno, chamadode
__dict__.Esseobjetoéchamadodedicionáriointernodeatributos.
>>> class DataTable :
... def __init__ ( self , name, data = []):
... self . _name = name
219
E-book gerado especialmente para 


## Página 236

14.5. Dicionáriointernodeatributos CasadoCódigo
... self . _data = data
... def add_row ( self , row):
... self . _data . append(row)
...
>>> t = DataTable( 'ExecucaoFinanceira' )
>>> t . __dict__
{'_data': [], '_name': 'ExecucaoFinanceira'}
Repareque t.__dict__éumdicionárionormal,cujaschaves/valores
são,respectivamente,nomeevalordosatributosdainstânciacriada.Sevocê
sentiufaltadosatributosreferentesaosmétodos,vejaoexemploaseguir:
>>> DataTable . __dict__ . keys()
dict_keys(['__module__', '__dict__', '__doc__', '__init__',
'__weakref__', 'add_row'])
Reparequeosmétodosestãodefinidosnoobjetodaclasse,enãonasins-
tâncias.Porisso,osdicionários t.__dict__e DataTable.__dict__são
diferentes.
Esserecursoémuitopoderoso,maséapenasparacasosmuitoespecíficos.
Frameworksouferramentasquefazemalgumtipode patchingdocódigo,em
algunscasos,ofazematravésdamanipula çãodiretadodicionáriointernode
atributos.Issopodeserfeitopormeiodealgumasfun çõesembutidas,como:
setattr(), getattr()e hasattr().
Vejaoexemplodousode setattr():
>>> class DataTable :
... pass
...
>>> t = DataTable()
>>> setattr (t, 'name' , 'ExecucaoFinanceira' )
>>> t . name
'ExecucaoFinanceira'
Note que definimos um atributo na instância, ao usarmos a função
setattr(object, attribute_name, value) . Essencialmente,tería-
mosomesmoresultadocom t.name = ‘ExecucaoFinanceira’ ,masa
220
E-book gerado especialmente para 


## Página 237

CasadoCódigo Capítulo14. Explorandoaflexibilidadedomodelodeobjetos
vantagemde setattr()équepodemospassarumastringarbitrária,como
nomedoatributo.
A operação de obter o valor do atributo, geralmente feita
com objeto.atributo, pode também ser feita com a função
getattr(object, attribute_name).Vejaoexemploaseguir:
>>> class DataTable :
... pass
...
>>> t = DataTable()
>>> setattr (t, 'name' , 'ExecucaoFinanceira' )
>>> t . name
'ExecucaoFinanceira'
>>> getattr (t, 'name' )
'ExecucaoFinanceira'
Essencialmente, t.nameéomesmoque getattr(t, ‘name’). A
diferençaéque,nosegundocaso,tambémpodemospassarumastringarbi-
trária.
Por último, vemos o métodohasattr(obj, attribute_name),
que responde se determinado objeto tem algum atributo com o nome
attribute_name.
>>> class DataTable :
... def __init__ ( self , name, data = []):
... self . name = name
... self . _data = data
... def add_row ( self , row):
... self . _data . append(row)
...
>>> t = DataTable( 'ExecucaoFinanceira' )
>>> hasattr (t, 'name' )
True
>>> hasattr (t, '_data' )
True
Essa flexibilidade é muito interessante, mas, assim como no caso do
ducktyping,valesemprepensarbemseexisteanecessidaderealdeseusar
essesrecursos.
221
E-book gerado especialmente para 


## Página 238

14.6. Interceptandooacessoaatributos CasadoCódigo
14.6 Interceptando o acesso a atributos
Pormeiodemétodosespeciais, podemostambémdefinirumaformade
acessocustomizadoaosatributosdeumobjeto.Aideiaéinterceptaracha-
madaqueacessaumatributo,paraexecutarumcódigoarbitrário.
EmPython, quandousamosumaexpressãocomo table.name, no
fundo,estamosrealizando getattr(table, ‘name’),ouseja,queremos
acessaroatributo namedoobjeto table.Porpadrão,esseacessoéfeitono
dicionáriointernodeatributos,quevimosanteriormente.
Emalgunscasos,podeserinteressantepodermodificarcomoessabusca
deatributoéfeita.Umcasofamosodessanecessidadeéemmodelosdeplu-
gins,noqualosatributossóaparecememtempodeexecu ção,eficaimpossí-
velcriartodososmétodos/atributos,semsaberpreviamentequaisoscódigos
oclientepodequererusar.
Tambémexisteumpadrãoquepodeexplorarbemessacaracterística,que
éo Proxy.Neste,temosumobjetoquerepresentaoutroe,decertaforma,é
uma“camada”entreoclienteeoobjetoqueestáatrásdoproxy. Algumas
coisasdeprograma çãoorientadaaaspectostambémpodemserrealizadas
comaimplementa çãodessesmétodos.
Vejaumexemplo:
>>> class Proxy :
... def __init__ ( self , obj):
... self . obj = obj
...
... def __getattr__ ( self , name):
... print ( "Acesso ao atributo {}" . format(name))
... if hasattr ( self . obj, name):
... return getattr ( self . obj, name)
... else :
... raise Exception ( "Atributo desconhecido" )
...
>>> class DataTabte :
... def __init__ ( self , name):
... self . name = name
...
>>> class Query :
222
E-book gerado especialmente para 


## Página 239

CasadoCódigo Capítulo14. Explorandoaflexibilidadedomodelodeobjetos
... def __init__ ( self , attributes):
... self . attributes = attributes
...
>>> table_proxy = Proxy(DataTable( 'ExecucaoFinanceira' ))
>>> query_proxy = Proxy(Query([ 'id' , 'valor' ]))
>>> table_proxy . __dict__
{'obj': <__main__.DataTable object at 0x100a48e48>}
>>> query_proxy . __dict__
{'obj': <__main__.Query object at 0x100a48c88>}
>>> print (table_proxy . name)
Acesso ao atributo name
ExecucaoFinanceira
>>> print (query_proxy . attributes)
Acesso ao atributo attributes
['id', 'valor']
Pormeiodaimplementa çãodométodo __getattr__(),conseguimos
fazercomqueousodeumainstânciadonosso Proxysejamuitosemelhante
aousodopróprioobjetoencapsuladodentrodele. Reparequeosatributos
queacessamosnãoexistemnosdicionáriosinternosdoproxy,mas,quando
usamos,acessamososatributos,eoproxybuscanoobjetoencapsuladoere-
torna.
Deformasemelhante,temosométodo __setattr__(),queéacionado
quandoatribuímosumvaloraumatributodeumobjeto,comoporexem-
plo: table.nome = "ExecucaoFinanceira" .Issotemomesmoresul-
tadoque setattr(obj, "nome", "ExecucaoFinanceira") .Vamos
verumexemploilustrandoseuuso:
>>> table = DataTable()
>>> table . name = "ExecucaoFinanceira"
>>>
>>> table . name
'ExecucaoFinanceira'
>>> class DataTable :
... pass
...
>>> table = DataTable()
>>> table . name = "ExecucaoFinanceira"
223
E-book gerado especialmente para 


## Página 240

14.6. Interceptandooacessoaatributos CasadoCódigo
>>>
>>> class DataTable :
... def __setattr__ ( self , name, value):
... raise Exception ( "Classe de leitura apenas" )
...
>>> table = DataTable()
>>> table . name = "ExecucaoFinanceira"
Traceback (most recent call last):
File "<stdin>" , line 1 , in <module>
File "<stdin>" , line 3 , in __setattr__
Exception : Classe de leitura apenas
Nocasodo __setattr__()edo __getattr__(),elessãoexecutados
quandonãoexistedefini çãoparaoatributoemquestão.Porexemplo,quando
acessamosumatributoquenãofoidefinido,tantoparaobterseuvalorquanto
umaatribuição,umdosmétodosseráexecutado.
Caso você precise que os métodos sejam executados em todos aces-
sosaatributos, vocêpodedefinirosmétodos __getattribute__()e
__setattribute__().Vejaumexemploqueilustrabemisso:
>>> class DataTable :
... def __init__ ( self , name):
... self . _name = name
... def __getattr__ ( self , attr_name):
... print ( "Attributo não definido '{}' acessado" . format(
attr_name))
... if attr_name == "data" :
... return []
... raise AttributeError ( "Atributo '{}' não existe"
.format(attr_name))
... def __getattribute__ ( self , attr_name):
... print ( "Attributo {} acessado" . format(attr_name))
... return object . __getattribute__( self , attr_name)
...
>>> t = DataTable( "ExecucaoFinanceira" )
>>> t . _name
Attributo _name acessado
'ExecucaoFinanceira'
>>> t . data
224
E-book gerado especialmente para 


## Página 241

CasadoCódigo Capítulo14. Explorandoaflexibilidadedomodelodeobjetos
Attributo data acessado
Attributo não definido 'data' acessado
[]
>>> t . cols
Attributo cols acessado
Attributo não definido 'cols' acessado
Traceback (most recent call last):
File "<stdin>" , line 1 , in <module>
File "<stdin>" , line 8 , in __getattr__
AttributeError : Atributo 'cols' não existe
Ao tentarmos acessar o atributo_name, quando ele existe, ape-
nas __getattribute__() é acessado. Ele repassa a execução para
__getattribute__()daclasse object,quevaibuscaroatributonodi-
cionáriointernodanossaclasse.
Ao acessarmos o atributodata, quando ele não existe, primeiro
o __getattribute__ é acessado. A implementação do método
__getattribute__(),porsuavez,repassaaexecu çãoparaaimplemen-
taçãodessemesmométodo,sóquenaclasse object.
Aimplementaçãode __getattribute__()em objectprocurao
atributopelonomenodicionáriointerno.Comoelenãofoidefinido,omé-
todo __getattr__()échamado.Dentrodeste,retornamosumalistava-
zia, casoonomedoatributoseja ‘data’, ougeramosumaexce çãode
AttributeError. Estaénormalmenteusadanessetipodesitua ção,efoi
ilustradaquandotentamosacessaroatributo colsdoobjeto.
14.7 Protocolos e métodos especiais
Comovimosnocapítulo12,Pythontemprotocolos,usadosparadefinircom-
portamentospadronizados,paradeterminadostiposdeobjetos.Paraimple-
mentarumprotocolo,umconjuntoespecíficodemétodosespeciaisdeveser
realizado.
Diversasestruturasdedadosseguemprotocolos,assimcomonúmeros
tambémtêmseusprotocolos.Osprotocolos,inclusive,influenciamnatermi-
nologiausadapelacomunidade.Dapróximavezquevocêouviralgocomo
“esseobjetoéumiterável”ou“essafunçãofuncionacomqualquerobjetocom-
225
E-book gerado especialmente para 


## Página 242

14.8. Protocolodecontainer CasadoCódigo
patívelcomumasequência”,jásaberáqueessasfrasessereferemaprotocolos
etêmdefiniçãoformal.
Dopontodevistadeumautordebiblioteca,osprotocolospodemseruma
formadecriarAPIsmaisintegradasaosrecursosdalinguagem.Issopermite
umusomais“leve”emenosorientado,emchamadasdemétodosemobjetos.
Umexemplocompletoéoprotocolodesequências.Jácomentamossobre
eleanteriormenteem[ ?],masnãovimosexplicitamentequemétodosfazem
partedele.
Umasequênciaéumobjetoque:respondeseumoutroobjetopertencea
ele,respondeaoseutamanho,retornaumobjetoporíndiceeéiterável.Esse
protocoloécompostodeoutrosprotocolosmenores,eoscomportamentos
maiscomplexosacabamemergindodauniãodecomportamentosmenores
definidos.
Falandoemprotocolosmaisbásicos,vamosverosmaisfundamentaisdas
estruturasdedados,emPython.
14.8 Protocolo de container
Umcontainer,emPython,temdeimplementarapenasumcomportamento:
responderseumelementoqualquerfazparteounãodocontainer.Ficafácil
verquelistas,tuplas,dicionários,stringseoutrasestruturassãocontainers.
Ométodoespecialé __contains__().
>>> class TenhoTudo :
... def __contains__ ( self , obj):
... return True
...
>>> tem_tudo = TenhoTudo()
>>> 1 in tem_tudo
True
>>> "qualquercoisa" in tem_tudo
True
>>> [] in tem_tudo
True
Comovocêpodever,sempreretornamos True. Logo,ooperador in
sempreretornaráessevalorquandousadoemumobjeto TemTudo.
226
E-book gerado especialmente para 


## Página 243

CasadoCódigo Capítulo14. Explorandoaflexibilidadedomodelodeobjetos
Nocontextodonossoaplicativo,essemétodopoderiaserusadoparares-
pondersedeterminadoobjetoencontra-seemdeterminadacolunadeinfor-
mação.
Porexemplo,seumatabelacontémumadeterminadachave,ocontainer
responde True:
>>> table = DataTable( "ExecucaoFinanceira" ,
"execucaoFinanceira.csv")
>>> 1 in table
True
Veja que, por meio da implementação de __contains__(), nosso
DataTablepoderespondersedeterminadachaveprimáriaestáentreseus
elementos.Apesardeserumexemplosimples,seconstruirmosumaAPIque
implementadiversosprotocolos,elaacabatornando-sebemamigávelaouso
ebemintegradaaorestodalinguagem.
14.9 Protocolo de containers com tamanho de -
finido
Onomerealdoprotocoloquevamosveragoraéo sized protocol,também
chamadode“containercomtamanhodefinido”.Esseprotocolotambémtem
apenasummétodo,o __len__().Bastaoobjetosempresaberrespondero
seutamanho,quepodeserconsideradoum sized.
Eletambémpodeserimplementadonanossa DataTablepararespon-
der,naverdade,otamanhodelinhasdeinforma çãoqueelacontém.Vejaum
exemploilustrativo:
>>> class DataTable :
... def __init__ ( self , name, filename):
... self . _name = name
... with open (filename) as data:
... self . _data = data . readlines()
... @property
... def name ( self ):
... return self . _name
... def __len__ ( self ):
227
E-book gerado especialmente para 


## Página 244

14.10. Protocolodeiteráveiseiteradores CasadoCódigo
... return len ( self . _data)
...
>>> table = DataTable( "ExecucaoFinanceira" ,
"execucaoFinanceira.csv")
>>> len (table)
5375
Novamente,usamosoprotocoloanossofavor,paratornaraAPIum
poucomenoscomplexa,poisnãoexigimosqueousuáriosaibaqualatributo
contémosdadosparachamar len()eobteronúmeroderegistros.
14.10 Protocolo de iteráveis e iteradores
Outroprotocolofundamentalemuitoimportanteéodeobjetositeráveis.
Todoobjetoqueoimplementapodeserusadonocomando foreem com-
prehensions.Quandoinformamosqueumobjetoéiterável,significaquepo-
demospercorrerosseuselementosdeformasequencial.
Nonossoexemplo,podemostornarum DataTableiterável,eosele-
mentositeradosseriamosseusregistros.Parasercompatívelcomessepro-
tocolo,aúnicaexigênciaéqueométodo __iter__()sejaimplementadoe
retorneumobjetoiterador.Oobjetoiteradoréoobjetoquerepresenta,em
si,ofluxodedados.
O objetoiterador, por sua vez, tem de implementar o método
__next__(),quedeveretornaropróximoelementodopercorrimento. É
dentrode __next__()quesecontrolaaordememqueosobjetossãore-
tornados.
Emmuitoscasos,oobjetoiteráveltambéméumiteradordelemesmo.
Porisso,écomumqueelesimplementem __iter__()e __next__().
Vamostornarnossoobjetoiteráveleiterador:
>>> class DataTable :
... def __init__ ( self , name, filename):
... self . _name = name
... self . _c = 0
... with open (filename) as data:
... self . _data = data . readlines()
228
E-book gerado especialmente para 


## Página 245

CasadoCódigo Capítulo14. Explorandoaflexibilidadedomodelodeobjetos
... @property
... def name ( self ):
... return self . _name
... def __len__ ( self ):
... return len ( self . _data)
... def __iter__ ( self ):
... return self
... def __next__ ( self ):
... try :
... element = self . _data[ self . _c]
... except IndexError as ie:
... self . _c = 0
... raise StopIteration
... self . _c += 1
... return element
...
>>> table = DataTable( "ExecucaoFinanceira" ,
"execucaoFinanceira.csv")
>>> for line in table:
... print (line)
...
37145;354;11982;xxxxxxxxxxxxxxxxxxx;
14332.00;0;25/07/2013;25/07/2013;31/12/2013
37147;354;11831;xxxxxxxxxxxxxxxxxxx;
832.88;0;26/07/2013;26/07/2013;31/12/2013
37148;360;12581;xxxxxxxxxxxxxxxxxxx;
590.60;0;04/06/2014;04/06/2014;14/06/2014
37149;354;12899;xxxxxxxxxxxxxxxxxxx;
1200.00;0;26/07/2013;26/07/2013;31/12/2013
Vejaque,noexemplo,implementamosambososmétodos.Dessaforma,
podemosusaroobjeto DataTablediretonocomando for,maisumavez,
integrandomelhornossaAPIcomalinguagem.
Aimplementaçãoébemsimples:basicamente,mantemosumíndicedo
elementocorrenteaserretornado,nocaso,avariável“privada”_c.Afun ção
__next__()sempreretornaoelementodalista _data,apontadoporesse
229
E-book gerado especialmente para 


## Página 246

14.11. Protocolodesequências CasadoCódigo
índice.Quandochegamosaofinal,levantamos StopIterationparasina-
lizarqueoloopiniciadoterminou.Nessemomento,reiniciamosocontador
para0,paraqueoobjetopossaserpercorridodoinícioemumapróximavez.
14.11 Protocolo de sequências
Seimplementarmosostrêsprotocolosanterioresemaisummétodo,vamos
atenderaoprotocolode sequência.
Nofimdascontas,paraserumasequência,oobjetodeveserumcontai-
nercomtamanhodefinido,iterávelequeécapazderetornarumelemento,
dadoumíndice. Esseúltimocomportamentosedápormeiodométodo
__getitem__().
Emsequências,essemétododevereceberuminteiroou slice object.Qual-
queroutrotipodeveserinterpretadocomoerro,preferencialmentegerando
um TypeError.Seoargumentoforuminteiro,deveserretornadooobjeto
queocupaaposi çãorepresentadapelointeiro.Seforum slice object,devem
serretornadososelementoscorrespondentesaesse slice.
Nonossocaso,aimplementa çãode __getitem__()simplesmentere-
tornaoobjetodasualistainternaderegistros.
>>> class DataTable :
... def __init__ ( self , name, filename):
... self . _name = name
... self . _c = 0
... with open (filename) as data:
... self . _data = data . readlines()
... @property
... def name ( self ):
... return self . _name
... def __len__ ( self ):
... return len ( self . _data)
... def __iter__ ( self ):
... return self
... def __next__ ( self ):
... try :
... element = self . _data[ self . _c]
... except IndexError as ie:
230
E-book gerado especialmente para 


## Página 247

CasadoCódigo Capítulo14. Explorandoaflexibilidadedomodelodeobjetos
... self . _c = 0
... raise StopIteration
... self . _c += 1
... return element
... def __getitem__ ( self , i):
... if isinstance (i, int ) or isinstance (i, slice ):
... return self . _data[i]
... raise TypeError ( "Invalid index/slice object '{}'"
.format(str(i)))
...
>>> table = DataTable( "ExecucaoFinanceira" ,
"execucaoFinanceira.csv")
>>> print (table[ 0 ])
1;2;132;CONSTRUTORA ANDRADE GUTIERREZ S/A.;696648486.09;0;
19/03/2010;23/03/2010;05/10/2013
>>> print (table[ 1 : 3 ])
['2;3;357;MENDES JUNIOR TRADING E ENGENHARIA S. A.;
342060007.96;0;
20/04/2010;20/04/2010;03/06/2013\n',
'5;6;136;Arena das Dunas Concess\xc3\xa3o e Eventos S.A.;
400000000.00;0;31/10/2011;31/10/2011;31/10/2031\n']
>>> print (table[ '1' ])
Traceback (most recent call last):
File "<stdin>" , line 1 , in <module>
File "<stdin>" , line 25 , in __getitem__
TypeError : Invalid index/slice object '1'
Tudoquefizemosfoirepassaroobjetorecebidoparaalistainternade
registros.Comoessalistaéumasequência,elaécompatívelcomosobjetos
dotipointeiroou slice. Casooobjetopassadonãosejanenhumdosdois,
levantamosumerrodotipo TypeError.
Comaimplementa çãodosmétodos __contains__(), __len__(),
__iter__(), __next__()e __getitem__(),tornamosonossoobjeto
DataTablecompatívelcomoprotocolodesequência.Qualquerfun çãoque
esperaumobjetocompatívelcomesseprotocolopodereceberumobjeto
dessetipo. Alémdisso,integramosonossoobjetoadiversoscomandosda
linguagem,comoooperadorbinário in,ocomandodeloop for,afun ção
len()easintaxedeacessoaelementos objeto[indice].
231
E-book gerado especialmente para 


## Página 248

14.12. Protocolodemapas CasadoCódigo
Alémde sequence,temosadefini çãodeuma mutable sequence,quedeve
implementarmétodosquepermitemamudan çadeelementos.Paraseruma
sequênciamutável,oobjetodeveserumasequênciaeimplementar,pelome-
nos,osmétodos __setitem__(), __delitem__()e insert.
Ométodo __setitem__()implementaocomportamentodaatribui-
çãoemumaposi ção,e __delitem__()ocomportamentodeapagarum
valordeumaposi ção.Vejaosexemplos:
>>> lista = [ 1 , 2 , 3 , 4 , 5 ]
>>> lista[ 2 ] = 10
>>> lista
[1, 2, 10, 4, 5]
>>> del lista[ 1 ]
>>> lista
[1, 10, 4, 5]
>>> lista . insert( 0 , -1 )
>>> lista
[-1, 1, 10, 4, 5]
Existe uma implementa ção de sequência mutável
collections.abc.MutableSequence, que tem alguns métodos
concretos que se utilizam dos métodos fundamentais descritos anterior-
mente.Sesuaclasseherdarde MutableSequence,vocêganhaosmétodos
adicionais: append(), reverse(), extend(), pop(), remove(),e
__iadd__()(veremosessemétodoemdetalhesnase ção14.13).
Algunsobjetossãoapenassequências,comotuplasestrings.Jálistaéum
objetoqueésequênciamutável.
14.12 Protocolo de mapas
Outroprotocolofundamentaléodemapas( Mapping).Asfun çõesquede-
vemserimplementadassão __getitem__(), __iter__()e __len__(),
alémdosprotocolosdecontainer,containercomtamanhodefinido( Sized)
edeiteráveis.
Oobjetomaisfamosoqueimplementaesseprotocoloéodicionário(
dict).Existetambémomapamutável( MutableMapping),quenecessita
232
E-book gerado especialmente para 


## Página 249

CasadoCódigo Capítulo14. Explorandoaflexibilidadedomodelodeobjetos
dosmétodos __setitem__()e __delitem__(),alémdosmétodosne-
cessáriosem Mapping.
Geralmente, quandoqueremoscustomizaressesmétodos, aprincípio
partimos das classes abstratas do módulocollections.abc (https://
docs.python.org/3/library/collections.abc.html),especificamente Mapping
e MutableMapping.
Mesmo que pareça confuso, os métodos __setitem__(),
__getitem__() e __contains__() são válidos tanto parasequên-
ciasquantopara mapas.Adiferen çaémuitoimportante!
Nas sequências,osobjetossãoindexadosporinteiros( int)e,emalguns
casos,podemreceber slice objectscomoparâmetro(se ção14.11).Nocasodos
mapas,osobjetospassados,comoem valor = objeto[’atributo’] ,
podemserstringsouqualquerobjetoimutávelqueimplementeoprotocolo
Hashable,comostrings,númerosouatémesmotuplas.
14.13 Protocolos numéricos
Alémdosmétodosespeciaisvistos,existemváriosoutros,comdestaquepara
osquesãousadosquandoopera çõesnuméricassãoexecutadas.Expressões
–comoa + b ou a >> b –tambémdisparammétodosespeciais.
A referência completa e oficial de métodos está disponí-
vel em https://docs.python.org/3/reference/datamodel.html #
emulating-numeric-types.
No mundo real, encontramos o uso dos métodos especiais numéri-
cos onde o objeto em questão representa um número – por exemplo, a
classe Decimal, vista no capítulo 11. Isso nos permite manipular es-
sesobjetosemexpressõesnuméricas,comonocódigo Decimal("1") +
Decimal("2.5"),queresultaem Decimal("3.5").
EmumalinguagemcomoJava,quenãopossuiessetipoderecurso, sem-
pretemosdeinvocarummétodo–comoemBigDecimal result = new
BigDecimal(1).add(new BigDecimal(2.5)); –,jáquealinguagem
233
E-book gerado especialmente para 


## Página 250

14.13. Protocolosnuméricos CasadoCódigo
nãosuportaexpressõesnuméricascomobjetos,masapenascomtipospri-
mitivosecomosrespectivosobjetosassociadosaeles(classe Integerou
Long,porexemplo).
Emalgunscasosmaisexóticos,autoresdeprojetosdãooutrassemân-
ticasaosmétodosespeciaisnuméricos,paracriarAPIsmaisexpressivas.No
casodonossoaplicativo,podemoscriarumasintaxeexóticapararealizaruma
consultanosdados.Vejaoexemplo:
>>> class DataTable :
... def __init__ ( self , name, filename):
... self . _name = name
... with open (filename) as data:
... self . _data = data . readlines()
... @property
... def name ( self ):
... return self . _name
... def __len__ ( self ):
... return len ( self . _data)
...
>>> class Select :
... def __init__ ( self ):
... self . _c = 0
... def __lshift__ ( self , table):
... self . table = table
... return self
... def __iter__ ( self ):
... return self
... def __next__ ( self ):
... try :
... element = self . table . _data[ self . _c]
... except IndexError as ie:
... self . _c = 0
... raise StopIteration
... self . _c += 1
... return element
...
>>> select = Select()
>>> table = DataTable( "ExecucaoFinanceira" ,
... "../data/data/execucaoFinanceira.csv" )
234
E-book gerado especialmente para 


## Página 251

CasadoCódigo Capítulo14. Explorandoaflexibilidadedomodelodeobjetos
>>>
>>> for line in select << table:
... print (line)
Reparequefoipossívelusaraexpressão select << table ,pormeio
daimplementaçãode __lshift__().Esseexemplofoicriadomaispelofim
ilustrativodoqueprático.Entretanto,aindaassim,algunsprojetosqueexis-
temporaífazemousodessetipoderecurso,algoquepodesermaiscriativo
eútil.Omaisimportanteéconheceromecanismo,nãosódosmétodosespe-
ciaisnuméricos,masdetodosemgeral.Podemosesbarrarcomelesmuitas
vezes.
14.14 O que mais ver sobre classes e modelo de
objetos?
Aindaexistemoutrosassuntossobreclasses;porseremmaisavan çados,não
fazempartedoescopodestelivro,portantoficaporcontadoleitorseaprofun-
darneles.UmbomdesenvolvedorPythondeveconhecertambémométodo
especial __new__(),responsávelpelacriaçãodeumanovainstânciadeum
objeto,diferentede __init__(),quedeveserresponsávelpelainicializa-
ção.
Oatributoespecial __slots__tambémpodeserútilquandoestivermos
manipulandoumagrandequantidadedeobjetos,poispermitequemenos
memóriasejaocupadapelasinstânciasdeles.
Outroassuntorelevantesãoasmetaclasses,quedãoaindamaispodere
flexibilidadeparametaprograma ção,emPython.
14.15 Conclusão
Aexistênciadosprotocolospermitequenossosobjetosseintegremmelhor
aosrecursosjádisponíveisnativamentenalinguagemounabibliotecapa-
drão.Comeles,podemosmanipularobjetoscriadospornós,comconstru-
çõeseexpressõesdalinguagem,fugindoumpoucodeAPIstotalmenteim-
plementadascommétodos(comonocasodeJava,emversõesumpoucomais
antigas).
235
E-book gerado especialmente para 


## Página 252

14.15. Conclusão CasadoCódigo
Aflexibilidadeoferecidapelapossibilidadedeimplementarmosprotoco-
los(quandoconveniente),tornaomodelodeobjetosPythonmuitopoderoso
eaomesmotemposimples. Éimportantesemprerelembrarquerecursos
dessetipodevemserusadosquandorealmentefornecessário.
Osrecursosexplicadosaquisãousadosporalgunsprojetosepodemos
esbarrarcomelesnonossodiaadia.Mesmoque,emalgunscasos,aaplica ção
nãosejatãoampla,éimportantesabercomoascoisasfuncionam,poisisso
permitemelhorusoeentendimentodosrecursosdisponíveis.
236
E-book gerado especialmente para 


## Página 253

Capítulo15
Consideraçõesfinais
15.1 Nunca pare!
EstelivronãoéumguiacompletosobrePythonenuncapretendeuser.Veja-o
comoumpontodepartida.
OuniversoPythonémuitoricoealinguagem,semsombradedúvidas,
émuitoprodutiva.Tenhaemmentequeummaiordomíniorefleteemuma
produtividadeaindamaior.Éclaroquetodoaprendizadoégradual.
Nestelivro,tenteiselecionaralgunstópicosquejáapresentamvárioste-
masrecorrentes, principalmentequandofalamoseminiciantes, tantoem
Pythonquantoemprograma çãoemgeral.
15.2 Aprendi tudo?
Claroquenão!:)
E-book gerado especialmente para 


## Página 254

15.2. Aprenditudo? CasadoCódigo
Aprimeiradicaéqueprograma ção,independentedalinguagem,exige
estudoeprática.Algumaspessoasoptamporselan çarnapráticacommenos
estudo,eoutrasfazemaocontrário.Dequalquerforma,éimportantealter-
narasduascoisas.Criepequenosprojetose,preferencialmente,termine-os,
mesmoqueelestenhamumobjetivobemlimitado.
Tenteabsorverbemapartedateoria,antesdeirparaassuntosmaisavan-
çados,paranãoacumularlacunasdeconhecimento. ParticipedeDOJOS,
casotenhadisponibilidade–senãosouberoqueé,fa çaumapesquisana
internet!Nãotenhapressa,masestabele çametasetentecumpri-las.
Vamosdefinirdoistiposprincipaisdeusuários,comosimplifica çãodo
mundoreal,paravocêentendercomoolivropodeajudá-lo.Vejacomqual
delesvocêseidentificahoje,paraentãovercomoolivroatendeàssuasne-
cessidades.
Usuáriosdelinguagem
Umusuáriodeumalinguagemavêcomoumaferramentapararesolver
seusproblemas.Hoje,temosdiversosusuáriosdePythonqueresolvempro-
blemas,incrivelmentecomplexos,usandoPython,masnãonecessariamente
são expertsdalinguagem.
Pythontemcrescidomuito,poisérelativamentefácildesetornarum
usuáriodalinguagem.Assim,elatorna-seprodutivacomcertarapidez.
Umusuário,geralmente,fazmuitousodecódigodeterceiroseusaos
aspectosmaisfundamentaisdalinguagemnoseudiaadia. Oseufocode
trabalhosãoseusproblemas,enãoalinguagememsi.
DesenvolvedorPython
Esseoutro“tipo”éalguémcominteresseemlinguagensdeprogramação
ounoecossistemaPython(incluindooutrosinterpretadoreseprojetosmais
avançados),ouqueapenasquerentenderprecisamentetodososmecanismos
easpectosdalinguagem.
Diversosprojetos–comodebuggerseferramentasdetestes–usamin-
tensivamenteconhecimentosbemespecíficosdalinguagem. Émuitodifícil
serumbomdesenvolvedordealgunstiposdeferramentassementenderseus
detalhesinternosealgumasmotiva çõesparadecisõessobreoseudesign.
238
E-book gerado especialmente para 


## Página 255

CasadoCódigo Capítulo15. Consideraçõesfinais
Mas,eaí?
SevocêquerserumusuáriodePython,estelivroéumótimopontode
partida.Todososassuntosforamabordadoscomexemplosetodoselespo-
derão(edeverão)serdiscutidosnainternet.Novosexemplosserãocriados
emaisconteúdotambém! UmdospontosmaisfortesdePythonéque,sa-
bendoapenasobásicoeconhecendoasferramentascertas,muitosproblemas
podemserresolvidosouestudados.
SevocêdesejaserumdesenvolvedorPython,olivroseráumlivrointro-
dutório.Algunsassuntosedetalhesquenãosãomuitocomunsemmateriais
pelainternetforamexplicados,comotambémumpoucodeteoria.Quando
vimosprotocolosabstratosemétodosespeciais,aimportânciamaiorerapas-
saraoleitoraterminologiaeopropósito,comopontodepartidaparaleitu-
rasmaisprofundas,masnãotínhamoscomoobjetivocobririndividualmente
cadaumdeles.
Existemaindacaracterísticascomoaexpressão yield from,alguns
módulosimportantes(como os, sys, asyncio),detalhesarespeitode
ASTs,bytecode,máquinavirtualeserializa ção,quesãomuitorelevantesno
universoPython,porémexigemmaiscuidadoseinforma çõesparaquepos-
samserpassados.
Algunsdostópicosquesãoconsideradosavan çadospodemserestudados
emmaterialnainterneteemoutroslivrosmaisavan çados,comoo Fluent
Python,escritoporLucianoRamalho,famosopythonistabrasileiro.
15.3 Comunidade Python
AcomunidadePythonémuitodiversificada.AquinoBrasiltemosiniciantes,
expertsemuitosdesenvolvedoresdeoutraslinguagensque,dealgumaforma,
seconectamcomacomunidadePython.Alémdisso,existeumintercâmbio
comomeiocientífico,jáquePythonéumalinguagemextremamentepopular
quandosefalaemcomputa çãocientífica.Issotudotornaacomunidadebra-
sileiradePythonextremamenterica,quecontribuicomoamadurecimento
daspessoasqueseenvolvemcomelaefetivamente.
239
E-book gerado especialmente para 


## Página 256

15.4. Paraondeir? CasadoCódigo
Umlivrotambémcriaumacomunidade. Todososexemplospode-
rãoserdiscutidoseincrementados,pormeiodacolabora çãodequem
querqueseja. Temosumfórum: livro-python3@googlegroups.come
umrepositórioGitHuboficial,comosexemplos,paraquetodospossam
colaborarcomolivrodealgumaforma: https://github.com/felipecruz/
exemplos.
15.4 Para onde ir?
Primeiro,vocêdeveseperguntarquaissãoseusobjetivoshoje.Qualsuamo-
tivaçãoparaaprenderPython?Éasuaprimeiralinguagem?Vocêjádesen-
volve,masquerumaoutraop çãocomolinguagem?Vocêsebeneficiariano
seutrabalho(oupesquisa)sesoubesseprogramar?
Paracadapergunta,háumaouváriasrespostas.Paraprogramadoresini-
ciantes,muitotreinoénecessário. Mantenhaumadisciplinaemdesenvol-
verecriartestesquandoforimportante,edesenvolvaalgoritmosconhecidos,
como quicksort, mergesort,buscaemlarguraeváriosoutros,parafixarasope-
raçõeselementaresnalinguagem.Pesquiseevejacomodesenvolvedoresmais
experientesorganizamseusprojetos,criamtestes,equaisferramentasusam
paraaumentaraqualidadeouprodutividade.
Casovocêjádesenvolva,foque-seemaprendercomoresolverproblemas
comunsemPython,depreferênciadaforma pythônica.Crieumprojetocom
scriptdeinstala çãoetestes,eestudecomofazerissodamelhorforma.Pes-
quiseferramentaseframeworksparairmontandoseukitdeferramentas.
Conversecomoutraspessoas! Massempretenhaemmenteosseusobjeti-
vosenãoosesque ça! Combomfoco,oingressonouniversoPythonpode
serbemrápidoeprodutivoparaquemjáédesenvolvedor.
Sevocênãotrabalhacomtecnologia,masestábuscandoconhecimento
sobreprogramação,saibaquemuitosexcelentesdesenvolvedoressãoauto-
didatas,equevocêtambémpodeserumdeles. Talvezsejainteressantedi-
recionaroestudodalinguagemsemprecomumganchopararesolverum
problemadoseucotidiano.
UmestatísticopodeusarPythoncomoumaferramentapoderosapara
240
E-book gerado especialmente para 


## Página 257

CasadoCódigo Capítulo15. Consideraçõesfinais
análises,assimcomoumeconomistapodeobtergrandeêxitonoseudiaadia
usandoscriptssimples,mesmosemseaprofundarmaisnalinguagem.
Emtodososcasos,Pythonéapenasumaferramentaquepodeajudá-loa
realizardiversostiposdetarefa.Dequalquermodo,podemosconsiderarque
algumaspartesdalinguagemsãoimportantes,nãoimportaqualsejaoseu
caso.
Umresumodedicas:
1) Estudeepratique!
2) Procureajuda,masnãosejapregui çoso.
3) Nãotenteaprendertudodeumasóvez,mastambémnãofiqueparado.
4) ParticipedeDOJOS,eventosdePython.
5) VáaumaPythonBrasil!Temtodoano!
6) SejaummembrodaAssocia çãoBrasileiradePython.
7) Participedecomunidadespresenciaisevirtuais.
8) Ajudepessoascommenosconhecimento,sepuder!
Obrigado!
241
E-book gerado especialmente para 


## Página 258

E-book gerado especialmente para 


## Página 259

CasadoCódigo ReferênciasBibliográficas
ReferênciasBibliográficas
[1] GovernoBrasileiro. Portaldatransparência-copa2014. http://www.
portaldatransparencia.gov.br/copa2014.
[2] UnicodeConsortium.Unicode.http://www.unicode.org/.
[3] PythonDocumentation.Pythonunlimitedintegers.http://docs.python.
org/3/library/stdtypes.html#numeric-types-int-float-complex.
[4] NickCoghlanGuidovanRossum. Newimporthooks. http://legacy.
python.org/dev/peps/pep-0343/,2005.
[5] GuidovanRossumKa-PingYee.Pep-234-iterators.http://www.python.
org/dev/peps/pep-0234/,2001.
[6] MartinVLöwis.Pep-393.http://www.python.org/dev/peps/pep-0393/,
2010.
[7] GuidovanRossumMosheZadka. Unifyinglongintegersandintegers.
http://www.python.org/dev/peps/pep-0237/,2001.
[8] Tim Peters.The zen of python. http://www.python.org/dev/peps/
pep-0020/,2004.
[9] Guido van Rossum. Pep-8. http://www.python.org/dev/peps/
pep-0008/,2001.
[10] Wikipedia.Codepoints.http://en.wikipedia.org/wiki/Code_point.
[11] Wikipedia. Teoriadosconjuntos. http://pt.wikipedia.org/wiki/Teoria_
dos_conjuntos.
243
E-book gerado especialmente para 


## Página 260

ReferênciasBibliográficas CasadoCódigo
[12] Wikpedia. Associative arrays. http://en.wikipedia.org/wiki/
Associative_array.
[13] Wikpedia. Ieee floating point. http://en.wikipedia.org/wiki/IEEE_
754-2008.
[14] Wikpedia.Utf-8.https://en.wikipedia.org/wiki/UTF-8.
[15] Ka-PingYee.Accesstonamesinouterscopes. https://www.python.org/
dev/peps/pep-3104/,2006.
244
E-book gerado especialmente para 
