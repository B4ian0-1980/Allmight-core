---json
{
  "id": "python_para_desenvolvedores_2ed",
  "title": "Python para Desenvolvedores",
  "categoria": "03-linguagens",
  "subcategoria": "python",
  "resumo": "**Arquivo Original:** `python_para_desenvolvedores_2ed.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "2ed",
    "desenvolvedores",
    "linguagens",
    "para",
    "python"
  ],
  "perguntas_tipo": [
    "Como utilizar Python para Desenvolvedores?",
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

# Python para Desenvolvedores

> **Arquivo Original:** `python_para_desenvolvedores_2ed.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 2

Licença
Este trabalho está licenciado sob uma Licença Creative Commons Atribuição-
Uso Não-Comercial-Compartilhamento pela mesma Licença 2.5 Brasil. Para  
ver uma cópia desta licença, visite http://creativecommons.org/licenses/by-nc-
sa/2.5/br/ ou envie uma carta para Creative Commons, 171 Second Street,  
Suite 300, San Francisco, California 94105, USA.
Site oficial
A edição mais recente está disponível no formato PDF em:
http://ark4n.wordpress.com/python/
Capa
Imagem utilizada na capa (Steampython):
http://ark4n.deviantart.com/art/Steampython-150806118


## Página 3

Luiz Eduardo Borges
Python para Desenvolvedores
2ª edição
Rio de Janeiro
Edição do Autor
2010

## Página 4

Python para Desenvolvedores / Luiz Eduardo Borges
Rio de Janeiro, Edição do Autor, 2010
ISBN 978-85-909451-1-6

## Página 5

Agradecimentos
Gostaria de agradecer a minha esposa e aos meus pais, pela paciência que  
tiveram durante o processo de criação desta obra.
Além deles, também gostaria de agradecer a todos que apoiaram e ajudaram  
a divulgar o livro.
Sobre o autor
Luiz Eduardo Borges é engenheiro e analista de sistemas, com pós-graduação  
em  Computação  Gráfica  pela  Universidade  do  Estado  do  Rio  de  Janeiro  
(UERJ).  Atua  a  quase  duas  décadas  na  área  de  informática,  sob  diversas 
formas.

## Página 6

Sumário
Parte I 10
Prefácio da primeira edição 11
Prefácio da segunda edição 12
Introdução 13
Características 13
Histórico 14
Versões 14
Executando programas 14
Tipagem dinâmica 15
Compilação e interpretação 16
Modo interativo 17
Ferramentas 18
Cultura 20
Sintaxe 22
Blocos 23
Objetos 25
Controle de fluxo 26
Laços 28
For 28
While 29
Tipos 31
Números 32
Texto 34
Listas 40
Tuplas 42
Outros tipos de sequências 44
Dicionários 45
Verdadeiro, falso e nulo 49
Operadores booleanos 50
Funções 52
Documentação 58
Exercícios I 60
Parte II 61
Módulos 62
Escopo de nomes 66
Pacotes 68
Biblioteca padrão 69

## Página 7

Matemática 69
Arquivos e I/O 72
Sistemas de arquivo 74
Arquivos temporários 75
Arquivos compactados 76
Arquivos de dados 77
Sistema operacional 78
Tempo 80
Expressões regulares 83
Bibliotecas de terceiros 85
Exceções 87
Introspecção 90
Inspect 91
Exercícios II 93
Parte III 94
Geradores 95
Programação funcional 97
Lambda 97
Mapeamento 98
Filtragem 99
Redução 100
Transposição 102
List Comprehension 103
Generator Expression 104
Exercícios III 105
Parte IV 106
Decoradores 107
Classes 109
Classes abertas 114
Herança simples 117
Herança múltipla 120
Propriedades 124
Sobrecarga de operadores 127
Coleções 128
Metaclasses 134
Classes base abstratas 136
Decoradores de classe 139
Testes automatizados 141
Exercícios IV 145
Parte V 146

## Página 8

Threads 147
Persistência 151
Serialização 151
ZODB 152
YAML 154
JSON 157
XML 158
DOM 160
SAX 161
ElementTree 162
Banco de dados 165
DBI 166
MySQL 166
SQLite 167
Firebird 169
PostgreSQL 170
Mapeamento objeto-relacional 177
Web 180
CherryPy 181
CherryTemplate 181
Cliente Web 184
MVC 185
Exercícios V 195
Parte VI 196
Processamento numérico 197
NumPy 197
Arranjos 197
Matrizes 200
SciPy 202
Matplotlib 204
Interface Gráfica 211
Arquitetura 211
PyGTK 213
wxPython 225
PyQt 232
Computação Gráfica 238
Matrizes versus vetores 238
Processamento de imagem 241
SVG 247
SVGFig 249

## Página 9

Imagens em três dimensões 252
VPython 254
PyOpenGL 260
Processamento distribuído 268
Objetos distribuídos 271
Performance 274
Empacotamento e distribuição 283
Exercícios VI 287
Apêndices 288
Integração com aplicativos 289
Blender 290
Game engine 299
GIMP 303
Inkscape 307
BrOffice.org 312
Integração com outras linguagens 317
Bibliotecas compartilhadas 317
Python -> C 319
C -> Python 321
Integração com .NET 323
Respostas dos exercícios I 329
Respostas dos exercícios II 333
Respostas dos exercícios III 340
Respostas dos exercícios IV 343
Respostas dos exercícios V 350
Respostas dos exercícios VI 354
Índice remissivo 357

## Página 10

10 Parte I
Parte I
Esta  parte  trata  de  conceitos  básicos  sobre  a  linguagem  de  programação  
Python,  incluindo  sintaxe,  tipos,  estruturas  de  controle,  funções  e  
documentação.
Conteúdo:
▪ Prefácio da primeira edição  .
▪ Prefácio da segunda edição  .
▪ Introdução  .
▪ Sintaxe  .
▪ Controle de fluxo  .
▪ Laços  .
▪ Tipos  .
▪ Funções  .
▪ Documentação  .
▪ Exercícios I  .

## Página 11

Prefácio da primeira edição 11
Prefácio da primeira edição
As linguagens dinâmicas eram vistas no passado apenas como linguagens  
script, usadas para automatizar pequenas tarefas, porém, com o passar do  
tempo,  elas  cresceram,  amadureceram  e  conquistaram  seu  espaço  no  
mercado,  a  ponto  de  chamar  a  atenção  dos  grandes  fornecedores  de  
tecnologia.
Vários  fatores  contribuíram  para  esta  mudança,  tais  como  a  internet,  o  
software de código aberto e as metodologias ágeis de desenvolvimento.
A internet viabilizou o compartilhamento de informações de uma forma sem  
precedentes na história, que tornou possível o crescimento do software de  
código  aberto.  As  linguagens  dinâmicas  geralmente  são  código  aberto  e  
compartilham  as  mesmas  funcionalidades  e  em  alguns  casos,  os  mesmos  
objetivos.
A  produtividade  e  expressividade  das  linguagens  dinâmicas  se  encaixam 
perfeitamente com as metodologias ágeis, que nasceram do desenvolvimento  
de software de código aberto e defendem um enfoque mais pragmático no  
processo de criação e manutenção de software do que as metodologias mais  
tradicionais.
Entre  as  linguagens  dinâmicas,  o  Python  se  destaca  como  uma  das  mais 
populares e poderosas. Existe uma comunidade movimentada de usuários da  
linguagem no mundo, o que se reflete em listas ativas de discussão e muitas  
ferramentas disponíveis em código aberto.
Aprender uma nova linguagem de programação significa aprender a pensar  
de  outra  forma.  E  aprender  uma  linguagem  dinâmica  representa  uma  
mudança de paradigma ainda mais forte para aquelas pessoas que passaram  
anos desenvolvendo em linguagens estáticas.

## Página 12

12 Prefácio da segunda edição
Prefácio da segunda edição
Revisada e ampliada, esta edição traz algumas novidades, como a inclusão de  
vários  recursos  interessantes  que  foram  incorporados  na  versão  2.6  do  
Python.
Vários assuntos já abordados na edição anterior foram expandidos, incluindo: 
orientação  a  objetos,  rotinas  matemáticas,  interface  gráfica,  computação  
gráfica, acesso a bancos de dados  e integração com aplicativos de código  
aberto.
Além disso, a formatação passou por algumas mudanças, visando facilitar a  
leitura em monitores e a impressão.
Entretanto, a maior parte das mudanças vieram com a revisão do texto, que  
agora se tornou compatível com a nova ortografia, tarefa facilitada pelo uso  
do BrOffice.org e suas ferramentas. Várias partes do texto foram ampliadas,  
capítulos  mudaram  de  ordem,  novos  exemplos  e  diagramas  foram  
acrescentados,  com  o  objetivo  de  melhorar  o  encadeamento  dos  assuntos 
abordados.

## Página 13

Introdução 13
Introdução
Python1 é  uma  linguagem  de  altíssimo  nível  (em  inglês,  Very  High  Level  
Language)  orientada  a objeto,  de  tipagem  dinâmica e  forte,  interpretada  e  
interativa.
Características
O Python possui uma sintaxe clara e concisa, que favorece a legibilidade do  
código fonte, tornando a linguagem mais produtiva.
A linguagem inclui diversas estruturas de alto nível (listas, dicionários, data /  
hora, complexos e outras) e uma vasta coleção de módulos prontos para uso,  
além de frameworks de terceiros que podem ser adicionados. Também possui  
recursos encontrados em outras linguagens modernas, tais como: geradores,  
introspecção, persistência, metaclasses e unidades de teste. Multiparadigma,  
a linguagem suporta programação modular e funcional, além da orientação a  
objetos.  Mesmo  os  tipos  básicos  no  Python  são  objetos.  A  linguagem  é  
interpretada  através  de  bytecode pela  máquina virtual  Python,  tornando  o  
código portável. Com isso é possível compilar aplicações em uma plataforma  
e rodar em outros sistemas ou executar direto do código fonte.
Python  é  um  software  de  código  aberto  (com  licença  compatível  com  a  
General  Public  License  (GPL),  porém  menos  restritiva,  permitindo  que  o  
Python  seja  inclusive  incorporado  em  produtos  proprietários).  A  
especificação da linguagem é mantida pela Python Software Foundation2 (PSF).
Além  de  ser  utilizado  como  linguagem  principal  no  desenvolvimento  de  
sistemas,  o  Python  também  é  muito  utilizado  como  linguagem  script em  
vários  softwares,  permitindo  automatizar  tarefas  e  adicionar  novas  
funcionalidades,  entre  eles:  BrOffice.org,  PostgreSQL,  Blender,  GIMP e  
Inkscape.
É possível integrar o Python a outras linguagens, como a Linguagem C e  
Fortran. Em termos gerais, a linguagem apresenta muitas similaridades com  
1 Página oficial: http://www.python.org/.
2 Endereço na internet da PSF: http://www.python.org/psf/.

## Página 14

14 Introdução
outras linguagens dinâmicas, como Perl e Ruby.
Histórico
A  linguagem  foi  criada  em  1990  por  Guido  van  Rossum,  no  Instituto  
Nacional de Pesquisa para Matemática e Ciência da Computação da Holanda  
(CWI) e tinha originalmente foco em usuários como físicos e engenheiros. O  
Python  foi  concebido  a  partir  de  outra  linguagem  existente  na  época,  
chamada ABC.
Hoje, a linguagem é bem aceita na industria por empresas de alta tecnologia,  
tais como:
▪ Google (aplicações Web).
▪ Yahoo (aplicações Web).
▪ Microsoft (IronPython: Python para .NET).
▪ Nokia (disponível para as linhas recentes de celulares e PDAs).
▪ Disney (animações 3D).
Versões
A implementação oficial do Python é mantida pela PSF e escrita em C, e por  
isso, é também conhecida como CPython. A versão estável mais recente está  
disponível para download no endereço:
http://www.python.org/download/
Para  a  plataforma  Windows,  basta  executar  o  instalador.  Para  outras  
plataformas, como em sistemas Linux, geralmente o Python já faz parte do  
sistema, porém em alguns casos pode ser necessário compilar e instalar o  
interpretador a partir dos arquivos fonte.
Existem também implementações de Python para .NET (IronPython), JVM  
(Jython) e em Python (PyPy).
Executando programas
Exemplo de programa em Python:

## Página 15

Introdução 15
# Uma lista de instrumentos musicais
instrumentos = ['Baixo', 'Bateria', 'Guitarra']
# Para cada nome na lista de instrumentos
for instrumento in instrumentos:
    # mostre o nome do instrumento musical
    print instrumento
Saída:
Baixo
Bateria
Guitarra
No exemplo, “instrumentos” é uma lista contendo os itens “Baixo”, “Bateria”  
e “Guitarra”. Já “instrumento” é um nome que corresponde a cada um dos  
itens da lista, conforme o laço é executado.
Os arquivos fonte são identificados geralmente pela extensão “.py” e podem  
ser executados diretamente pelo interpretador:
python apl.py
Assim o programa “apl.py” será executado. No Windows, as extensões de  
arquivo  “.py”,  “.pyw”,  “.pyc”  e  “.pyo”  são  associadas  ao  Python  
automaticamente  durante  a  instalação,  então  é  só  clicar  no  arquivo  para  
executar. Os arquivos “.pyw” são executados com uma versão alternativa do  
interpretador que não abre a janela de console.
Tipagem dinâmica
Python utiliza tipagem dinâmica, o que significa que o tipo de uma variável é  
inferido pelo interpretador em tempo de execução (isto é conhecido como  
Duck  Typing ).  No  momento  em  que  uma  variável  é  criada  através  de  
atribuição, o interpretador define um tipo para a variável, com as operações  
que podem ser aplicadas.
O caractere “#” indica que o 
resto da linha é um comentário.
O caractere “#” indica que o 
resto da linha é um comentário.

## Página 16

16 Introdução
A tipagem do Python é forte, ou seja, o interpretador verifica se as operações  
são válidas e não faz coerções automáticas entre  tipos incompatíveis 3. Para  
realizar  a  operação  entre  tipos não  compatíveis,  é  necessário  converter  
explicitamente o tipo da variável ou variáveis antes da operação.
Compilação e interpretação
O código fonte é traduzido  pelo Python para  bytecode, que é um formato  
binário com instruções para o interpretador. O  bytecode é multiplataforma e  
pode ser distribuído e executado sem fonte original.
Por padrão, o interpretador compila o código e armazena o bytecode em disco, 
para que a próxima vez que o executar, não precise compilar novamente o  
programa, reduzindo o tempo de carga na execução. Se os arquivos fontes  
forem  alterados,  o  interpretador  se  encarregará  de  regerar  o  bytecode 
automaticamente, mesmo utilizando o shell interativo. Quando um programa  
ou  um  módulo  é  evocado,  o  interpretador  realiza  a  análise  do  código,  
converte para símbolos, compila (se não houver bytecode atualizado em disco) 
3 Em  Python,  coerções  são  realizadas  automaticamente  apenas  entre  tipos  que  são  
claramente relacionados, como inteiro e inteiro longo.
Código fonte 
(.py)
 Símbolos
 Árvore sintática
Bytecode
(.pyc / .pyo)
 Binários
Instaladores
Interpretador

## Página 17

Introdução 17
e executa na máquina virtual Python.
O bytecode é armazenado em arquivos com extensão “.pyc” (bytecode normal) 
ou  “.pyo” ( bytecode otimizado).  O  bytecode também  pode  ser  empacotado  
junto com o interpretador em um executável, para facilitar a distribuição da  
aplicação, eliminando a necessidade de instalar Python em cada computador.
Modo interativo
O interpretador Python pode ser usado de forma interativa, na qual as linhas  
de código são digitadas em um  prompt (linha de comando) semelhante ao  
shell do sistema operacional.
Para evocar o modo interativo basta executar o interpretador (se ele estiver no 
path):
python
Ele  estará  pronto  para  receber  comandos  após  o  surgimento  do  sinal  de 
espera “>>>” na tela:
Python 2.6.4 (r264:75706, Nov  3 2009, 13:20:47)
[GCC 4.4.1] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
No Windows, o modo interativo está disponível também através do ícone  
“Python (command line)”.
O  modo  interativo  é  uma  característica  diferencial  da  linguagem,  pois  é  
possível testar e modificar trechos de código antes da inclusão do código em  
programas, fazer extração e conversão de dados ou mesmo analisar o estado  
dos objetos que estão em memória, entre outras possibilidades.
Além do modo interativo tradicional do Python, existem outros programas  
que funcionam como alternativas, com interfaces mais sofisticadas (como o  

## Página 18

18 Introdução
PyCrust4):
Ferramentas
Existem muitas ferramentas de desenvolvimento para Python, como  IDEs, 
editores e shells (que aproveitam da capacidade interativa do Python).
Integrated Development Environments  (IDEs) são pacotes de software integram  
várias ferramentas de desenvolvimento em um ambiente consistente, com o  
objetivo  de  aumentar  a  produtividade  do  desenvolvedor.  Geralmente,  as  
IDEs  incluem  recursos  como  syntax  highlight  (código  fonte  colorizado  
conforme a sintaxe da linguagem), navegadores de código, shell integrado e  
code completion  (o editor apresenta durante a digitação formas possíveis de  
completar o texto que ele consegue identificar).
Entre as IDEs que suportam Python, encontram-se:
▪ PyScripter5.
▪ SPE6 (Stani's Python Editor).
4 PyCrust faz parte do projeto wxPython (http://www.wxpython.org/).
5 Disponível em http://code.google.com/p/pyscripter/.
6 Endereço: http://pythonide.blogspot.com/.


## Página 19

Introdução 19
▪ Eric7.
▪ PyDev8 (plug-in para a IDE Eclipse).
Existem também editores de texto especializados em código de programação,  
que possuem funcionalidades como colorização de sintaxe, exportação para  
outros formatos e conversão de codificação de texto.
Esses editores suportam diversas linguagens de programação, dentre elas o  
Python:
▪ SciTE9.
▪ Notepad++10.
Shell é o nome dado aos ambientes interativos para execução de comandos,  
que  podem  ser  usados  para  testar  pequenas  porções  de  código  e  para  
atividades  como  data  crunching (extração  de  informações  de  interesse  de  
massas de dados e a subsequente tradução para outros formatos).
Além do próprio Shell padrão do Python, existem os outros disponíveis:
7 Site: http://eric-ide.python-projects.org/.
8 Disponível em http://pydev.org/.
9 Site: http://www.scintilla.org/SciTE.html.
10 Download de fontes e binários em: http://notepad-plus.sourceforge.net/br/site.htm.


## Página 20

20 Introdução
▪ PyCrust (gráfico).
▪ Ipython (texto).
Os empacotadores são utilitários que são usados para construir executáveis  
que englobam o bytecode, o interpretador e outras dependências, permitindo  
que o aplicativo rode em máquinas sem Python instalado, o que facilita a  
distribuição de programas.
Entre empacotadores feitos para Python, estão disponíveis:
▪ Py2exe (apenas para Windows).
▪ cx_Freeze (portável).
Frameworks são coleções de componentes de software (bibliotecas, utilitários e  
outros) que foram projetados para serem utilizados por outros sistemas.
Alguns frameworks disponíveis mais conhecidos:
▪ Web: Django, TurboGears, Zope e web2py.
▪ Interface gráfica: wxPython, PyGTK e PyQt.
▪ Processamento cientifico: NumPy e SciPy.
▪ Processamento de imagens: PIL.
▪ 2D: Matplotlib e SVGFig.
▪ 3D: Visual Python, PyOpenGL e Python Ogre.
▪ Mapeamento objeto-relacional: SQLAlchemy e SQLObject.
Cultura
O  nome  Python  foi  tirado  por  Guido  van  Rossum  do  programa  da  TV  
britânica  Monty  Python  Flying  Circus ,  e  existem  várias  referências  na  
documentação da linguagem ao programa, como, por exemplo, o repositório  
oficial de pacotes do Python se chamava Cheese Shop, que era o nome de um  
dos  quadros  do  programa.  Atualmente,  o  nome  do  repositório  é  Python 
Package Index11 (PYPI).
A  comunidade  de  usuários  de  Python  criou  algumas  expressões  para  se  
referir aos assuntos relacionados à linguagem. Neste jargão, o termo Pythonic 
é usado para indicar que algo é compatível com as premissas de projeto do  
Python, e Unpythonic significa o oposto. Já o usuário da linguagem é chamado 
11 Endereço: http://pypi.python.org/pypi.

## Página 21

Introdução 21
de Pythonist.
As metas do projeto foram resumidas por Tim Peters em um texto chamado  
Zen of Python, que está disponível no próprio Python através do comando:
import this
O texto enfatiza a postura pragmática do Benevolent Dictator for Life  (BDFL),  
como Guido é conhecido na comunidade Python.
Propostas  para  melhoria  da  linguagem  são  chamadas  de  PEPs  ( Python 
Enhancement  Proposals ),  que  também  servem  de  referência  para  novos  
recursos a serem implementados na linguagem.
Além do site oficial, outras boas fontes de informação sobre a linguagem são:  
PythonBrasil12,  o  site da  comunidade  Python  no  Brasil,  com  bastante  
informação  em  português,  e  Python  Cookbook 13,  site  que  armazena  
“receitas”: pequenas porções de código para realizar tarefas específicas.
12 Endereço: http://www.python.org.br/.
13 Endereço: http://aspn.activestate.com/ASPN/Python/Cookbook/.

## Página 22

22 Sintaxe
Sintaxe
Um programa feito em Python é constituído de linhas, que podem continuar  
nas linhas seguintes, pelo uso do caractere de barra invertida (\) ao final da  
linha ou parênteses,  colchetes ou chaves, em expressões  que utilizam tais  
caracteres.
O caractere # marca o inicio de comentário. Qualquer texto depois do # será  
ignorado até o fim da linha , com exceção dos comentários funcionais.
Comentários funcionais são usados para:
▪ alterar a codificação do arquivo fonte do programa acrescentando um  
comentário  com o  texto  “#-*- coding:  <encoding> -*#-” no inicio  do  
arquivo, no qual <encoding> é a codificação do arquivo (geralmente  
latin1 ou  utf-8).  Alterar  a  codificação  é  necessário  para  suportar  
caracteres que não fazem parte da linguagem inglesa, no código fonte  
do programa.
▪ definir o interpretador que será utilizado para rodar o programa em  
sistemas  UNIX,  através  de  um  comentário  começando  com  “#!”  no 
inicio  do  arquivo,  que  indica  o  caminho  para  o  interpretador  
(geralmente  a  linha  de  comentário  será  algo  como  “#!/usr/bin/env  
python”).
Exemplo de comentários funcionais:
#!/usr/bin/env python
# -*- coding: latin1 -*-
# Uma linha de código que mostra o resultado de 7 vezes 3
print 7 * 3
Saída:
21
Exemplos de linhas quebradas:

## Página 23

Sintaxe 23
# -*- coding: latin1 -*-
# Uma linha quebrada por contra-barra
a = 7 * 3 + \
5 / 2
# Uma lista (quebrada por vírgula)
b = ['a', 'b', 'c',
'd', 'e']
# Uma chamada de função (quebrada por vírgula)
c = range(1,
11)
# imprime todos na tela
print a, b, c
Saída:
23 ['a', 'b', 'c', 'd', 'e'] [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
O  comando  print insere  espaços  entre  as  expressões  que  forem  recebidas  
como parâmetro e um caractere de nova linha no final, a não ser que ele  
receba uma vírgula no fim da lista parâmetros.
Blocos
Em Python, os blocos de código são delimitados pelo uso de endentação, que  
deve ser constante no bloco de código, porém é considerada uma boa prática  
manter  a  consistência  no  projeto  todo  e  evitar  a  mistura  tabulações  e  
espaços14.
A linha anterior ao bloco sempre termina com dois pontos (:) e representa  
uma estrutura de controle da linguagem ou uma declaração de uma nova  
estrutura (uma função, por exemplo).
14 A recomendação oficial de estilo de codificação ( http://www.python.org/dev/peps/pep-
0008/) é usar quatro espaços para endentação e esta convenção é amplamente aceita  
pelos desenvolvedores.

## Página 24

24 Sintaxe
Exemplo:
# Para i na lista 234, 654, 378, 798:
for i in [234, 654, 378, 798]:
    # Se o resto dividindo por 3 for igual a zero:
    if i % 3 == 0:
        # Imprime...
        print i, '/ 3 =', i / 3
Saída:
234 / 3 = 78
654 / 3 = 218
378 / 3 = 126
798 / 3 = 266
O operador “%” calcula o módulo (resto da divisão).
Programa
Instruções
Enquanto condição:
 Dois pontos obrigatórios
Se condição:
Instruções
Senão:
Instruções
Instruções
Inicio de um bloco
Fim dos dois blocos
Outro bloco
Fim do programa
Instruções
 Inicio do programa

## Página 25

Sintaxe 25
Objetos
Python é uma linguagem orientada a objeto, sendo assim as estruturas de  
dados possuem atributos (os dados em si) e métodos (rotinas associadas aos  
dados). Tanto os atributos quanto os métodos são acessados usando ponto (.).
Para mostrar um atributo:
print objeto.atributo
Para executar um método:
objeto.metodo(argumentos)
Mesmo um método sem argumentos precisa de parênteses:
objeto.metodo()
O ponto também é  usado para  acessar estruturas  de  módulos que  foram  
importados pelo programa.

## Página 26

26 Controle de fluxo
Controle de fluxo
É muito comum em um programa que certos conjuntos de instruções sejam  
executados de forma condicional, em casos como validar entradas de dados,  
por exemplo.
Sintaxe:
if <condição>:
    <bloco de código>
elif <condição>:
    <bloco de código>
elif <condição>:
    <bloco de código>
else:
    <bloco de código>
Na qual:
▪ <condição>: sentença que possa ser avaliada como verdadeira ou falsa.
▪ <bloco de código>: sequência de linhas de comando.
▪ As clausulas elif e else são opcionais e podem existir vários elifs para o  
mesmo if, porém apenas um else ao final.
▪ Parênteses só são necessários para evitar ambiguidades.
Exemplo:
temp = int(raw_input('Entre com a temperatura: '))
if temp < 0:
    print 'Congelando...'
elif 0 <= temp <= 20:
    print 'Frio'
elif 21 <= temp <= 25:
    print 'Normal'
elif 26 <= temp <= 35:
    print 'Quente'
else:
    print 'Muito quente!'
Exemplo de saída:

## Página 27

Controle de fluxo 27
Entre com a temperatura: 23
Normal
Na  qual  “Entre  com  a  temperatura:”  é  a  mensagem  indicando  que  o  
programa  espera pela digitação , “23” é a entrada digitada e “Normal” é a  
resposta do programa.
Se o bloco de código for composto de apenas uma linha, ele pode ser escrito  
após os dois pontos:
if temp < 0: print 'Congelando...'
A partir da versão 2.5, o Python suporta a expressão:
<variável> = <valor 1> if <condição> else <valor 2>
Na qual <variável> receberá <valor 1> se <condição> for verdadeira e <valor  
2> caso contrário.

## Página 28

28 Laços
Laços
Laços ( loops) são estruturas de repetição, geralmente usados para processar  
coleções de dados, tais como linhas de um arquivo ou registros de um banco  
de dados, que precisam ser processados por um mesmo bloco de código.
For
É a estrutura de repetição mais usada no Python. A instrução aceita não só  
sequências  estáticas,  mas  também  sequências  geradas  por  iteradores.  
Iteradores são estruturas que permitem iterações, ou seja, acesso aos itens de  
uma coleção de elementos, de forma sequencial.
Durante a execução de um laço for, a referência aponta para um elemento da  
sequência. A cada iteração, a referência é atualizada, para que o bloco de  
código do for processe o elemento correspondente.
A clausula break interrompe o laço e continue passa para a próxima iteração. O 
código dentro do else é executado ao final do laço, a não ser que o laço tenha  
sido interrompido por break.
Lista
x aponta para 1.
1
2
3
4
5
6
...
x
Primeira
iteração
A referência
foi atualizada.
Lista
1
2
3
4
5
6
...
x
Segunda
iteração
x é apenas uma
referência.
x aponta para 2.

## Página 29

Laços 29
Sintaxe:
for <referência> in <sequência>:
    <bloco de código>
    continue
    break
else:
    <bloco de código>
Exemplo:
# Soma de 0 a 99
s = 0
for x in range(1, 100):
    s = s + x
print s
Saída:
4950
A função  range(m, n, p) , é muito útil em laços, pois retorna uma lista de  
inteiros, começando em  m e menores que  n, em passos de comprimento  p, 
que podem ser usados como sequência para o laço.
While
Executa um bloco de código atendendo a uma condição.
Sintaxe:
while <condição>:
    <bloco de código>
    continue
    break
else:
    <bloco de código>

## Página 30

30 Laços
O bloco de código dentro do laço  while é repetido enquanto a condição do  
laço estiver sendo avaliada como verdadeira.
Exemplo:
# Soma de 0 a 99
s = 0
x = 1
while x < 100:
    s = s + x
    x = x + 1
print s
O laço while é adequado quando não há como determinar quantas iterações  
vão ocorrer e não há uma sequência a seguir.

## Página 31

Tipos 31
Tipos
Variáveis  no  interpretador  Python  são  criadas  através  da  atribuição  e  
destruídas pelo coletor de lixo ( garbage colector ), quando não existem mais  
referências a elas.
Os  nomes  das  variáveis  devem  começar  com  letra  (sem  acentuação)  ou  
sublinhado (_) e seguido por letras (sem acentuação), dígitos ou sublinhados  
(_), sendo que maiúsculas e minúsculas são consideradas diferentes.
Existem vários tipos simples de dados pré-definidos no Python, tais como:
▪ Números (inteiros, reais, complexos, ... ).
▪ Texto.
Além disso, existem tipos que funcionam como coleções. Os principais são:
▪ Lista.
▪ Tupla.
▪ Dicionário.
Os tipos no Python podem ser:
▪ Mutáveis: permitem que os conteúdos das variáveis sejam alterados.
▪ Imutáveis:  não  permitem  que  os  conteúdos  das  variáveis  sejam  
alterados.
Em Python, os nomes de variáveis são referências, que podem ser alteradas  
em tempos de execução.
Os tipos e rotinas mais comuns estão implementados na forma de builtins, ou 
seja, eles estão sempre disponíveis em tempo de execução, sem a necessidade  
de importar nenhuma biblioteca.

## Página 32

32 Tipos
Números
Python oferece alguns tipos numéricos na forma de builtins:
▪ Inteiro (int): i = 1
▪ Real de ponto flutuante (float): f = 3.14
▪ Complexo (complex): c = 3 + 4j
Além  dos  números  inteiros  convencionais,  existem  também  os  inteiros  
longos, que tem dimensão arbitrária e são limitados pela memória disponível. 
As conversões entre inteiro e longo são realizadas de forma automática. A  
função  builtin int() pode ser usada para converter outros tipos para inteiro,  
incluindo mudanças de base.
Exemplo:
# -*- coding: latin1 -*-
# Convertendo de real para inteiro
print 'int(3.14) =', int(3.14)
# Convertendo de inteiro para real
print 'float(5) =', float(5)
# Calculo entre inteiro e real resulta em real
print '5.0 / 2 + 3 = ', 5.0 / 2 + 3
# Inteiros em outra base
print "int('20', 8) =", int('20', 8) # base 8
print "int('20', 16) =", int('20', 16) # base 16
# Operações com números complexos
c = 3 + 4j
print 'c =', c
print 'Parte real:', c.real
print 'Parte imaginária:', c.imag
print 'Conjugado:', c.conjugate()
Saída:
int(3.14) = 3

## Página 33

Tipos 33
float(5) = 5.0
5.0 / 2 + 3 =  5.5
int('20', 8) = 16
int('20', 16) = 32
c = (3+4j)
Parte real: 3.0
Parte imaginária: 4.0
Conjugado: (3-4j)
Os números reais também podem ser representados em notação cientifica,  
por exemplo: 1.2e22.
O Python tem uma série de operadores definidos para manipular números,  
através  de  cálculos  aritméticos,  operações  lógicas  (que  testam  se  uma  
determina condição é verdadeira ou falsa) ou processamento bit-a-bit (em  
que os números são tratados na forma binária).
Operações aritméticas:
▪ Soma (+).
▪ Diferença (-).
▪ Multiplicação (*).
▪ Divisão  (/):  entre  dois  inteiros  funciona  igual  à  divisão  inteira.  Em  
outros casos, o resultado é real.
▪ Divisão inteira (//): o resultado é truncado para o inteiro imediatamente 
inferior, mesmo quando aplicado em números reais, porém neste caso  
o resultado será real também.
▪ Módulo (%): retorna o resto da divisão.
▪ Potência (**): pode ser usada para calcular a raiz, através de expoentes  
fracionários (exemplo: 100 ** 0.5).
▪ Positivo (+).
▪ Negativo (-).
Operações lógicas:
▪ Menor (<).
▪ Maior (>).
▪ Menor ou igual (<=).
▪ Maior ou igual (>=).
▪ Igual (==).

## Página 34

34 Tipos
▪ Diferente (!=).
Operações bit-a-bit:
▪ Deslocamento para esquerda (<<).
▪ Deslocamento para direita (>>).
▪ E bit-a-bit (&).
▪ Ou bit-a-bit (|).
▪ Ou exclusivo bit-a-bit (^).
▪ Inversão (~).
Durante  as  operações,  os  números  serão  convertidos  de  forma  adequada  
(exemplo: (1.5+4j) + 3 resulta em 4.5+4j).
Além dos operadores,  também existem algumas funções  builtin para lidar  
com tipos numéricos: abs(), que retorna o valor absoluto do número, oct(), que 
converte para octal,  hex(), que converte para hexadecimal,  pow(), que eleva  
um  número  por  outro  e  round(),  que  retorna  um  número  real  com  o  
arredondamento especificado.
Texto
As strings no Python são buitins para armazenar texto. Como são  imutáveis, 
não é possível adicionar, remover ou mesmo modificar algum caractere de  
uma  string. Para realizar essas operações, o Python precisa criar um nova  
string.
Tipos:
▪ String padrão: s = 'Led Zeppelin'
▪ String unicode: u = u'Björk'
A string padrão pode ser convertida para unicode através da função unicode().
A inicialização de strings pode ser:
▪ Com aspas simples ou duplas.
▪ Em várias linhas consecutivas, desde que seja entre três aspas simples  
ou duplas.
▪ Sem expansão de caracteres (exemplo: s = r'\n', em que s conterá os  

## Página 35

Tipos 35
caracteres “\” e “n”).
Operações com strings:
# -*- coding: latin1 -*-
s = 'Camel'
# Concatenação
print 'The ' + s + ' run away!'
# Interpolação
print 'tamanho de %s => %d' % (s, len(s))
# String tratada como sequência
for ch in s: print ch
# Strings são objetos
if s.startswith('C'): print s.upper()
# o que acontecerá?
print 3 * s
# 3 * s é consistente com s + s + s
Operador “%” é usado para fazer interpolação de  strings. A interpolação é  
mais eficiente no uso de memória do que a concatenação convencional.
Símbolos usados na interpolação:
▪ %s: string.
▪ %d: inteiro.
▪ %o: octal.
▪ %x: hexacimal.
▪ %f: real.
▪ %e: real exponencial.
▪ %%: sinal de percentagem.
Os  símbolos  podem  ser  usados  para  apresentar  números  em  diversos  
formatos.
Exemplo:

## Página 36

36 Tipos
# -*- coding: latin1 -*-
# Zeros a esquerda
print 'Agora são %02d:%02d.' % (16, 30)
# Real (número após o ponto controla as casas decimais)
print 'Percentagem: %.1f%%, Exponencial:%.2e' % (5.333, 0.00314)
# Octal e hexadecimal
print 'Decimal: %d, Octal: %o, Hexadecimal: %x' % (10, 10, 10)
Saída:
Agora são 16:30.
Percentagem: 5.3%, Exponencial:3.14e-03
Decimal: 10, Octal: 12, Hexadecimal: a
A partir da versão 2.6, está disponível outra forma de interpolação além do  
operador “%”, o método de string e a função chamados format().
Exemplos:
# -*- coding: latin1 -*-
musicos = [('Page', 'guitarrista', 'Led Zeppelin'),
('Fripp', 'guitarrista', 'King Crimson')]
# Parâmetros identificados pela ordem
msg = '{0} é {1} do {2}'
for nome, funcao, banda in musicos:
    print(msg.format(nome, funcao, banda))
# Parâmetros identificados pelo nome
msg = '{saudacao}, são {hora:02d}:{minuto:02d}'
print msg.format(saudacao='Bom dia', hora=7, minuto=30)
# Função builtin format()
print 'Pi =', format(3.14159, '.3e')
Saída:

## Página 37

Tipos 37
Page é guitarrista do Led Zeppelin
Fripp é guitarrista do King Crimson
Bom dia, são 07:30
Pi = 3.142e+00
A função format() pode ser usada para formatar apenas um dado de cada vez.
Fatias (slices) de strings podem ser obtidas colocando índices entre colchetes  
após a string.
Os índices no Python:
▪ Começam em zero.
▪ Contam a partir do fim se forem negativos.
▪ Podem ser definidos como trechos, na forma [inicio:fim + 1:intervalo].  
Se não for definido o inicio, será considerado como zero.  Se não for  
definido o fim + 1, será considerado o tamanho do objeto. O intervalo  
(entre os caracteres), se não for definido, será 1.
É possível inverter strings usando um intervalo negativo:
Fatiando strings
String s
P
 y
 t
 h
 o
 n
0
 1
 2
 3
 4
 5
s[0]
Caracteres
Posições
s[:2]
 s[2:]
 s[-1]
P
 Py
 thon
 n
Expressões
Fatias

## Página 38

38 Tipos
print 'Python'[::-1]
# Mostra: nohtyP
Várias funções para tratar com texto estão implementadas no módulo string.
# -*- coding: latin1 -*-
# importando o módulo string
import string
# O alfabeto
a = string.ascii_letters
# Rodando o alfabeto um caractere para a esquerda
b = a[1:] + a[0]
# A função maketrans() cria uma tabela de tradução
# entre os caracteres das duas strings que ela
# recebeu como parâmetro.
# Os caracteres ausentes nas tabelas serão
# copiados para a saída.
tab = string.maketrans(a, b)
# A mensagem...
msg = '''Esse texto será traduzido..
Vai ficar bem estranho.
'''
# A função translate() usa a tabela de tradução
# criada pela maketrans() para traduzir uma string
print string.translate(msg, tab)
Saída:
Fttf ufyup tfsá usbevAjep..
Wbj gjdbs cfn ftusboip.
O módulo também implementa um tipo chamado Template, que é um modelo 
de  string que  pode  ser  preenchido  através  de  um  dicionário.  Os  
identificadores são inciados por cifrão ($) e podem ser cercados por chaves,  
para evitar confusões.

## Página 39

Tipos 39
Exemplo:
# -*- coding: latin1 -*-
# importando o módulo string
import string
# Cria uma string template
st = string.Template('$aviso aconteceu em $quando')
# Preenche o modelo com um dicionário
s = st.substitute({'aviso': 'Falta de eletricidade',
    'quando': '03 de Abril de 2002'})
# Mostra:
# Falta de eletricidade aconteceu em 03 de Abril de 2002
print s
É possível usar  strings mutáveis no Python, através do módulo  UserString, 
que define o tipo MutableString:
# -*- coding: latin1 -*-
# importando o módulo UserString
import UserString
s = UserString.MutableString('Python')
s[0] = 'p'
print s # mostra "python"
Strings mutáveis são menos eficientes do que strings imutáveis, pois são mais  
complexas (em termos de estrutura), o que se reflete em maior consumo de  
recursos (CPU e memória).
As strings unicode podem convertidas para strings convencionais através do  
método decode() e o caminho inverso pode ser feito pelo método encode().
Exemplo:
# -*- coding: latin1 -*-

## Página 40

40 Tipos
# String unicode
u = u'Hüsker Dü'
# Convertendo para str
s = u.encode('latin1')
print s, '=>', type(s)
# String str
s = 'Hüsker Dü'
u = s.decode('latin1')
print repr(u), '=>', type(u)
Saída:
Hüsker Dü => <type 'str'>
u'H\xfcsker D\xfc' => <type 'unicode'>
Para usar os dois métodos, é necessário passar como argumento a codificação  
compatível, as mais utilizadas com a língua portuguesa são “latin1” e “utf8”.
Listas
Listas são coleções heterogêneas de objetos, que podem ser de qualquer tipo,  
inclusive outras listas.
As  listas  no  Python  são  mutáveis,  podendo  ser  alteradas  a  qualquer  
momento.  Listas podem ser fatiadas da mesma forma que as  strings, mas  
como as listas são mutáveis, é possível fazer atribuições a itens da lista.
Sintaxe:
lista = [a, b, ..., z]
Operações comuns com listas:
# -*- coding: latin1 -*-

## Página 41

Tipos 41
# Uma nova lista: Brit Progs dos anos 70
progs = ['Yes', 'Genesis', 'Pink Floyd', 'ELP']
# Varrendo a lista inteira
for prog in progs:
    print prog
# Trocando o último elemento
progs[-1] = 'King Crimson'
# Incluindo
progs.append('Camel')
# Removendo
progs.remove('Pink Floyd')
# Ordena a lista
progs.sort()
# Inverte a lista
progs.reverse()
# Imprime numerado
for i, prog in enumerate(progs):
    print i + 1, '=>', prog
# Imprime do segundo item em diante
print progs[1:]
Saída:
Yes
Genesis
Pink Floyd
ELP
1 => Yes
2 => King Crimson
3 => Genesis
4 => Camel
['King Crimson', 'Genesis', 'Camel']
A função enumerate() retorna uma tupla de dois elementos a cada iteração: um 
número sequencial e um item da sequência correspondente.

## Página 42

42 Tipos
A lista possui o método pop() que facilita a implementação de filas e pilhas:
# -*- coding: latin1 -*-
lista = ['A', 'B', 'C']
print 'lista:', lista
# A lista vazia é avaliada como falsa
while lista:
    
    # Em filas, o primeiro item é o primeiro a sair
    # pop(0) remove e retorna o primeiro item
    print 'Saiu', lista.pop(0), ', faltam', len(lista)
# Mais itens na lista
lista += ['D', 'E', 'F']
print 'lista:', lista
while lista:
    # Em pilhas, o primeiro item é o último a sair
    # pop() remove e retorna o último item
    print 'Saiu', lista.pop(), ', faltam', len(lista)
Saída:
lista: ['A', 'B', 'C']
Saiu A , faltam 2
Saiu B , faltam 1
Saiu C , faltam 0
lista: ['D', 'E', 'F']
Saiu F , faltam 2
Saiu E , faltam 1
Saiu D , faltam 0
As operações de ordenação (sort) e inversão (reverse) são realizadas na própria 
lista, sendo assim, não geram novas listas.
Tuplas
Semelhantes as listas, porém são imutáveis: não se pode acrescentar, apagar  
ou fazer atribuições aos itens.

## Página 43

Tipos 43
Sintaxe:
tupla = (a, b, ..., z)
Os parênteses são opcionais.
Particularidade: tupla com apenas um elemento é representada como:
t1 = (1,)
Os elementos de uma tupla podem ser referenciados da mesma forma que os  
elementos de uma lista:
primeiro_elemento = tupla[0]
Listas podem ser convertidas em tuplas:
tupla = tuple(lista)
E tuplas podem ser convertidas em listas:
lista = list(tupla)
Embora a tupla possa conter elementos mutáveis, esses elementos não podem 
sofrer atribuição, pois isto modificaria a referência ao objeto.
Exemplo (usando o modo interativo):
>>> t = ([1, 2], 4)
>>> t[0].append(3)
>>> t
([1, 2, 3], 4)
>>> t[0] = [1, 2, 3]

## Página 44

44 Tipos
Traceback (most recent call last):
  File "<input>", line 1, in ?
TypeError: object does not support item assignment
>>>
As tuplas são mais eficientes do que as listas convencionais, pois consomem  
menos  recursos  computacionais  (memória),  por  serem  estruturas  mais  
simples, tal como as strings imutáveis em relação às strings mutáveis.
Outros tipos de sequências
O Python provê entre os builtins também:
▪ set: sequência mutável unívoca (sem repetições) não ordenada.
▪ frozenset: sequência imutável unívoca não ordenada.
Os  dois  tipos  implementam  operações  de  conjuntos,  tais  como:  união,  
interseção e diferença.
Exemplo:
# -*- coding: latin1 -*-
# Conjuntos de dados
s1 = set(range(3))
s2 = set(range(10, 7, -1))
s3 = set(range(2, 10, 2))
# Exibe os dados
print 's1:', s1, '\ns2:', s2, '\ns3:', s3
# União
s1s2 = s1.union(s2)
print 'União de s1 e s2:', s1s2
# Diferença
print 'Diferença com s3:', s1s2.difference(s3)
# Interseção
print 'Interseção com s3:', s1s2.intersection(s3)
# Testa se um set inclui outro
if s1.issuperset([1, 2]):

## Página 45

Tipos 45
    print 's1 inclui 1 e 2'
# Testa se não existe elementos em comum
if s1.isdisjoint(s2):
    print 's1 e s2 não tem elementos em comum'
Saída:
s1: set([0, 1, 2]) 
s2: set([8, 9, 10]) 
s3: set([8, 2, 4, 6])
União de s1 e s2: set([0, 1, 2, 8, 9, 10])
Diferença com s3: set([0, 1, 10, 9])
Interseção com s3: set([8, 2])
s1 inclui 1 e 2
s1 e s2 não tem elementos em comum
Quando uma lista é convertida para set, as repetições são descartadas.
Na versão 2.6, também está disponível um tipo  builtin de lista mutável de  
caracteres, chamado bytearray.
Dicionários
Um dicionário é uma lista de associações compostas por uma chave única e  
estruturas correspondentes. Dicionários são mutáveis, tais como as listas.
A chave precisa ser de um tipo imutável, geralmente são usadas strings, mas 
também podem ser  tuplas ou tipos numéricos. Já os itens dos dicionários  
podem ser tanto mutáveis quanto imutáveis.  O dicionário do Python não  
fornece garantia de que as chaves estarão ordenadas.
Sintaxe:
dicionario = {'a': a, 'b': b, ..., 'z': z}
Estrutura:

## Página 46

46 Tipos
Exemplo de dicionário:
dic = {'nome': 'Shirley Manson', 'banda': 'Garbage'}
Acessando elementos:
print dic['nome']
Adicionando elementos:
dic['album'] = 'Version 2.0'
Apagando um elemento do dicionário:
del dic['album']
Obtendo os itens, chaves e valores:
Chaves
Fractal
{'Fractal': 'IFS', 'Palheta': 'Verde', 'Limites': (640, 480), (0, 0): (42, 35)}
Valores
IFS
Palheta
 Verde
Limites
 (640, 480)
(0, 0)
 (42, 35)
Elementos 
imutáveis
Objetos 
quaisquer

## Página 47

Tipos 47
itens = dic.items()
chaves = dic.keys()
valores = dic.values()
Exemplos com dicionários:
# Progs e seus albuns
progs = {'Yes': ['Close To The Edge', 'Fragile'],
    'Genesis': ['Foxtrot', 'The Nursery Crime'],
    'ELP': ['Brain Salad Surgery']}
# Mais progs
progs['King Crimson'] = ['Red', 'Discipline']
# items() retorna uma lista de
# tuplas com a chave e o valor
for prog, albuns in progs.items():
    print prog, '=>', albuns
# Se tiver 'ELP', deleta
if progs.has_key('ELP'):
    del progs['ELP']
Saída:
Yes => ['Close To The Edge', 'Fragile']
ELP => ['Brain Salad Surgery']
Genesis => ['Foxtrot', 'The Nursery Crime']
King Crimson => ['Red', 'Discipline']
Exemplo de matriz esparsa:
# -*- coding: latin1 -*-
# Matriz esparsa implementada
# com dicionário
# Matriz esparsa é uma estrutura
# que só armazena os valores que
# existem na matriz

## Página 48

48 Tipos
dim = 6, 12
mat = {}
# Tuplas são imutáveis
# Cada tupla representa
# uma posição na matriz
mat[3, 7] = 3
mat[4, 6] = 5
mat[6, 3] = 7
mat[5, 4] = 6
mat[2, 9] = 4
mat[1, 0] = 9
for lin in range(dim[0]):
    for col in range(dim[1]):
        # Método get(chave, valor)
        # retorna o valor da chave
        # no dicionário ou se a chave
        # não existir, retorna o
        # segundo argumento
        print mat.get((lin, col), 0),
    print
Saída:
0 0 0 0 0 0 0 0 0 0 0 0
9 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 4 0 0
0 0 0 0 0 0 0 3 0 0 0 0
0 0 0 0 0 0 5 0 0 0 0 0
0 0 0 0 6 0 0 0 0 0 0 0
Gerando a matriz esparsa:
# -*- coding: latin1 -*-
# Matriz em forma de string
matriz = '''0 0 0 0 0 0 0 0 0 0 0 0
9 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 4 0 0
0 0 0 0 0 0 0 3 0 0 0 0
0 0 0 0 0 0 5 0 0 0 0 0

## Página 49

Tipos 49
0 0 0 0 6 0 0 0 0 0 0 0'''
mat = {}
# Quebra a matriz em linhas
for lin, linha in enumerate(matriz.splitlines()):
    # Quebra a linha em colunas
    for col, coluna in enumerate(linha.split()):
        coluna = int(coluna)
        # Coloca a coluna no resultado,
        # se for diferente de zero
        if coluna:
            mat[lin, col] = coluna
print mat
# Some um nas dimensões pois a contagem começa em zero
print 'Tamanho da matriz completa:', (lin + 1) * (col + 1)
print 'Tamanho da matriz esparsa:', len(mat)
Saída:
{(5, 4): 6, (3, 7): 3, (1, 0): 9, (4, 6): 5, (2, 9): 4}
Tamanho da matriz completa: 72
Tamanho da matriz esparsa: 5
A matriz esparsa é uma boa solução de processamento para estruturas em  
que a maioria dos itens permanecem vazios, como planilhas, por exemplo.
Verdadeiro, falso e nulo
Em Python, o tipo booleano (bool) é uma especialização do tipo inteiro (int). O 
verdadeiro é chamado True e é igual a 1, enquanto o falso é chamado False e é 
igual a zero.
Os seguintes valores são considerados falsos:
▪ False (falso).
▪ None (nulo).
▪ 0 (zero).
▪ '' (string vazia).

## Página 50

50 Tipos
▪ [] (lista vazia).
▪ () (tupla vazia).
▪ {} (dicionário vazio).
▪ Outras estruturas com o tamanho igual a zero.
São considerados verdadeiros todos os outros objetos fora dessa lista.
O objeto  None, que é do tipo  NoneType,  do Python representa  o nulo e é  
avaliado como falso pelo interpretador.
Operadores booleanos
Com operadores lógicos é possível construir condições mais complexas para  
controlar desvios condicionais e laços.
Os operadores booleanos no Python são: and, or, not, is e in.
▪ and:  retorna  um  valor  verdadeiro  se  e  somente  se  receber  duas  
expressões que forem verdadeiras.
▪ or: retorna um valor falso se e somente se receber duas expressões que  
forem falsas.
▪ not: retorna falso se receber uma expressão verdadeira e vice-versa.
▪ is: retorna verdadeiro se receber duas referências ao mesmo objeto e  
falso em caso contrário.
▪ in: retorna verdadeiro se receber um item e uma lista e o item ocorrer  
uma ou mais vezes na lista e falso em caso contrário.
O calculo do valor resultante na operação and ocorre da seguinte forma: se a  
primeira  expressão  for  verdadeira,  o  resultado  será  a  segunda  expressão, 
senão será a primeira. Já para o operador or, se a primeira expressão for falsa,  
o resultado será a segunda expressão, senão será a primeira. Para os outros  
operadores, o retorno será do tipo bool (True ou False).
Exemplos:
print 0 and 3 # Mostra 0
print 2 and 3 # Mostra 3
print 0 or 3 # Mostra 3

## Página 51

Tipos 51
print 2 or 3 # Mostra 2
print not 0 # Mostra True
print not 2 # Mostra False
print 2 in (2, 3) # Mostra True
print 2 is 3 # Mostra False
Além  dos  operadores  booleanos,  existem  as  funções  all(),  que  retorna  
verdadeiro  quando  todos  os  itens  forem  verdadeiros  na  sequência  usada  
como parâmetro, e any(), que retorna verdadeiro se algum item o for.

## Página 52

52 Funções
Funções
Funções são blocos de código identificados por um nome, que podem receber  
parâmetros pré-determinados.
No Python, as funções:
▪ Podem retornar ou não objetos.
▪ Aceitam Doc Strings.
▪ Aceitam  parâmetros  opcionais  (com  defaults).  Se  não  for  passado  o 
parâmetro será igual ao default definido na função.
▪ Aceitam que os parâmetros sejam passados com nome. Neste caso, a  
ordem em que os parâmetros foram passados não importa.
▪ Tem  namespace próprio  (escopo  local),  e  por  isso  podem  ofuscar  
definições de escopo global.
▪ Podem ter suas propriedades alteradas (geralmente por decoradores).
Doc Strings são strings que estão associadas a uma estrutura do Python. Nas  
funções, as Doc Strings são colocadas dentro do corpo da função, geralmente  
no começo. O objetivo das Doc Strings é servir de documentação para aquela  
estrutura.
Sintaxe:
def func(parametro1, parametro2=padrao):
    """Doc String
    """
    <bloco de código>
    return valor
Os parâmetros com default devem ficar após os que não tem default.
Exemplo (fatorial com recursão):
# Fatorial implementado de forma recursiva
def fatorial(num):

## Página 53

Funções 53
    if num <= 1:
        return 1
    else:
        return(num * fatorial(num – 1))
# Testando fatorial()
print fatorial(5)
Saída:
120
Exemplo (fatorial sem recursão):
def fatorial(n):
    n = n if n > 1 else 1
    j = 1
    for i in range(1, n + 1):
        j = j * i
    return j
# Testando...
for i in range(1, 6):
    print i, '->', fatorial(i)
Saída:
1 -> 1
2 -> 2
3 -> 6
4 -> 24
5 -> 120
Exemplo (série de Fibonacci com recursão):
def fib(n):
    """Fibonacci:
    fib(n) = fib(n - 1) + fib(n - 2) se n > 1

## Página 54

54 Funções
    fib(n) = 1 se n <= 1
    """
    if n > 1:
        return fib(n - 1) + fib(n - 2)
    else:
        return 1
# Mostrar Fibonacci de 1 a 5
for i in [1, 2, 3, 4, 5]:
    print i, '=>', fib(i)
Exemplo (série de Fibonacci sem recursão):
def fib(n):
    """Fibonacci:
    fib(n) = fib(n - 1) + fib(n - 2) se n > 1
    fib(n) = 1 se n <= 1
    """
    
    # Dois primeiros valores
    l = [1, 1]
    
    # Calculando os outros
    for i in range(2, n + 1):
        l.append(l[i -1] + l[i - 2])
        
    return l[n]
# Mostrar Fibonacci de 1 a 5
for i in [1, 2, 3, 4, 5]:
    print i, '=>', fib(i)
Saída:
1 => 1
2 => 2
3 => 3
4 => 5
5 => 8
Exemplo (conversão de RGB):

## Página 55

Funções 55
# -*- coding: latin1 -*-
def rgb_html(r=0, g=0, b=0):
    """Converte R, G, B em #RRGGBB"""
    return '#%02x%02x%02x' % (r, g, b)
def html_rgb(color='#000000'):
    """Converte #RRGGBB em R, G, B"""
    if color.startswith('#'): color = color[1:]
    r = int(color[:2], 16)
    g = int(color[2:4], 16)
    b = int(color[4:], 16)
    return r, g, b # Uma sequência
print rgb_html(200, 200, 255)
print rgb_html(b=200, g=200, r=255) # O que houve?
print html_rgb('#c8c8ff')
Saída:
#c8c8ff
#ffc8c8
(200, 200, 255)
Observações:
▪ Os  argumentos  com  padrão  devem  vir  por  último,  depois  dos  
argumentos sem padrão.
▪ O valor do padrão para um parâmetro é calculado quando a função é  
definida.
▪ Os argumentos passados sem identificador são recebidos pela função  
na forma de uma lista.
▪ Os argumentos passados com identificador são recebidos pela função  
na forma de um dicionário.
▪ Os  parâmetros  passados  com  identificador  na  chamada  da  função  
devem vir no fim da lista de parâmetros.
Exemplo de como receber todos parâmetros:

## Página 56

56 Funções
# -*- coding: latin1 -*-
# *args - argumentos sem nome (lista)
# **kargs - argumentos com nome (dicionário)
def func(*args, **kargs):
    print args
    print kargs
func('peso', 10, unidade='k')
Saída:
('peso', 10)
{'unidade': 'k'}
No  exemplo,  kargs receberá  os  argumentos  nomeados  e  args receberá  os  
outros.
O interpretador tem definidas algumas funções builtin, incluindo sorted(), que 
ordena sequências, e  cmp(), que faz comparações entre dois argumentos e  
retorna -1 se o primeiro elemento for maior , 0 (zero) se forem iguais ou 1 se o  
último  for  maior.  Essa  função  é  usada  pela  rotina  de  ordenação,  um  
comportamento que pode ser modificado.
Exemplo:
# -*- coding: latin1 -*-
dados = [(4, 3), (5, 1), (7, 2), (9, 0)]
# Comparando pelo último elemento
def _cmp(x, y):
    return cmp(x[-1], y[-1])
print 'Lista:', dados
# Ordena usando _cmp()
print 'Ordenada:', sorted(dados, _cmp)

## Página 57

Funções 57
Saída:
Lista: [(4, 3), (5, 1), (7, 2), (9, 0)]
Ordenada: [(9, 0), (5, 1), (7, 2), (4, 3)]
O  Python  também  possui  como  builtin a  função  eval(),  que  avalia  código 
(fonte ou objeto) retornando o valor.
Exemplo:
print eval('12. / 2 + 3.3')
Saída:
9.3
Com isso é possível montar código para ser passado para o interpretador  
durante  a  execução  de  um  programa.  Esse  recurso  deve  ser  usado  com  
cuidado, pois código montados a partir de entradas do sistema abrir brechas  
de segurança.

## Página 58

58 Documentação
Documentação
PyDOC é a ferramenta de documentação 15 do Python. Ela pode ser utilizada  
tanto para acessar a documentação dos módulos que acompanham o Python,  
quanto a documentação dos módulos de terceiros.
No  Windows,  acesse  o  ícone  “Module  Docs”  para  a  documentação  da  
biblioteca padrão e “Python Manuals” para consultar o tutorial, referências e  
outros documentos mais extensos.
Para utilizar o PyDOC no Linux:
pydoc ./modulo.py
Para exibir a documentação de “modulo.py” no diretório atual.
No Linux, a documentação das bibliotecas pode ser vista através do browser 
usando o comando:
pydoc -p 8000
No endereço http://localhost:8000/.
Para rodar a versão gráfica do PyDOC execute:
pydoc -g
O PyDOC utiliza as Doc Strings dos módulos para gerar a documentação.
Além  disso,  é  possível  ainda  consultar  a  documentação  no  próprio  
interpretador, através da função help().
Exemplo:
15 A documentação do Python também está disponível em: http://www.python.org/doc/.

## Página 59

Documentação 59
help(list)
Mostra a documentação para a lista do Python.

## Página 60

60 Exercícios I
Exercícios I
1. Implementar duas funções:
▪ Uma que converta temperatura em graus Celsius para Fahrenheit.
▪ Outra que converta temperatura em graus Fahrenheit para Celsius.
Lembrando que:
2. Implementar uma função que retorne verdadeiro se o número for primo  
(falso caso contrário). Testar de 1 a 100.
3. Implementar uma função que receba uma lista de listas de comprimentos  
quaisquer e retorne uma lista de uma dimensão.
4. Implementar uma função que receba um dicionário e retorne a soma, a  
média e a variação dos valores.
5. Escreva uma função que:
▪ Receba uma frase como parâmetro.
▪ Retorne uma nova frase com cada palavra com as letras invertidas.
6. Crie uma função que:
▪ Receba uma lista de tuplas (dados), um inteiro (chave, zero por padrão  
igual) e um booleano (reverso, falso por padrão).
▪ Retorne dados ordenados pelo item indicado pela chave e em ordem  
decrescente se reverso for verdadeiro.
F = 9
5⋅C 32

## Página 61

Parte II 61
Parte II
Esta parte trata de módulos e pacotes, destacando alguns dos mais relevantes  
que  estão  presentes  na  biblioteca  padrão  da  linguagem,  instalação  de  
bibliotecas de terceiros, exceções e introspecção.
Conteúdo:
▪ Módulos  .
▪ Escopo de nomes  .
▪ Pacotes  .
▪ Biblioteca padrão  .
▪ Bibliotecas de terceiros  .
▪ Exceções  .
▪ Introspecção  .
▪ Exercícios II  .

## Página 62

62 Módulos
Módulos
Para o Python, módulos são arquivos fonte que podem importados para um  
programa.  Podem  conter  qualquer  estrutura  do  Python  e  são  executados  
quando importados16. Eles são compilados quando importados pela primeira  
vez e armazenados em arquivo (com extensão  “.pyc” ou “.pyo” ), possuem  
namespace próprio e aceitam  Doc Strings . São objetos  Singleton (é carregada  
somente uma instância em memória, que fica disponível de forma global para  
o programa).
Os  módulos são  localizados  pelo  interpretador  através  da  lista  de  pastas  
PYTHONPATH (sys.path),  que  normalmente  inclui  a  pasta  corrente  em  
primeiro lugar.
Os módulos são carregados através da instrução import. Desta forma, ao usar  
alguma  estrutura  do  módulo,  é  necessário  identificar  o  módulo.  Isto  é  
chamado de importação absoluta.
16 Caso seja necessário executar de novo o módulo durante a execução da aplicação, ele terá 
que carregado outra vez através da função reload().
__main__
Função
sys.path
sys.exit()
Módulo principal em execução.
sys
path
exit
Módulo sys (import sys)
path é uma lista.
exit é uma função.
Função definida em __main__.
Chamando exit de sys.

## Página 63

Módulos 63
import os
print os.name
Também possível importar módulos de forma relativa:
from os import name
print name
O caractere  “*” pode  ser  usado  para importar  tudo  que  está  definido no  
módulo:
from os import *
print name
Por evitar problemas, como a ofuscação de variáveis, a importação absoluta é  
considerada  uma  prática  de  programação  melhor  do  que  a  importação  
relativa.
Exemplo de módulo:
# -*- coding: latin1 -*-
# Arquivo calc.py
# Função definida no módulo
def media(lista):
    return float(sum(lista)) / len(lista)
Exemplo de uso do módulo:
# -*- coding: latin1 -*-
# Importa o módulo calc
import calc
l = [23, 54, 31, 77, 12, 34]

## Página 64

64 Módulos
# Chamada a função definida em calc
print calc.media(l)
Saída:
38.5
O  módulo  principal  de  um  programa  tem  a  variável  __name__ igual  à  
“__main__”, então é possível testar se o módulo é o principal usando:
if __name__ == "__main__":
    # Aqui o código só será executado
    # se este for o módulo principal
    # e não quando ele for importado por outro programa
Com isso é fácil transformar um programa em um módulo.
Outro exemplo de módulo:
# -*- coding: latin1 -*-
"""
modutils => rotinas utilitárias para módulos
"""
import os.path
import sys
import glob
def find(txt):
    """encontra módulos que tem o nome
    contendo o parâmetro
    """
    resp = []
    for path in sys.path:
        mods = glob.glob('%s/*.py' % path)
        for mod in mods:

## Página 65

Módulos 65
            if txt in os.path.basename(mod):
                resp.append(mod)
    return resp
Exemplo de uso do módulo:
from os.path import getsize, getmtime
from time import localtime, asctime
import modutils
mods = modutils.find('xml')
for mod in mods:
    tm = asctime(localtime(getmtime(mod)))
    kb = getsize(mod) / 1024
    print '%s: (%d kbytes, %s)' % (mod, kb, tm)
Exemplo de saída:
c:\python26\lib\xmllib.py: (34 kbytes, Wed Sep 30 00:35:56 2009)
c:\python26\lib\xmlrpclib.py: (48 kbytes, Mon Sep 08 09:58:32 2008)
Dividir programas em módulos facilita o reaproveitamento e localização de  
falhas no código.

## Página 66

66 Escopo de nomes
Escopo de nomes
O escopo de nomes em Python é mantido através de  Namespaces, que são  
dicionários que relacionam os nomes dos objetos (referências) e os objetos em  
si.
Normalmente, os nomes estão definidos em dois dicionários, que podem ser  
consultados  através  das  funções  locals() e  globals().  Estes  dicionários  são  
atualizados dinamicamente em tempo de execução17.
Variáveis globais podem ser ofuscadas por variáveis locais (pois o escopo  
local é consultado antes do escopo global). Para evitar isso, é preciso declarar  
a variável como global no escopo local.
Exemplo:
17 Embora  os  dicionários  retornados  por  locals() e  globals() possam  ser  alterados  
diretamente, isso deve ser evitado, pois pode ter efeitos indesejáveis.
Módulo
Função
Var_1
Var_2
Var_3
Var_3
Var_4
Estas são variáveis globais.
Estas são variáveis locais.
Var_3 foi ofuscada, pois foi 
(re)definida no escopo local.
Um namespace é um escopo de 
definição de estruturas.

## Página 67

Escopo de nomes 67
def somalista(lista):
    """
    Soma listas de listas, recursivamente
    Coloca o resultado como global
    """
    global soma
    
    for item in lista:
        if type(item) is list: # Se o tipo do item for lista
            somalista(item)
        else:
            soma += item
soma = 0
somalista([[1, 2], [3, 4, 5], 6])
print soma # 21
Usar  variáveis  globais  não  é  considerada  uma  boa  prática  de  
desenvolvimento,  pois tornam mais  difícil  entender  o  sistema,  portanto  é  
melhor evitar seu uso. E ofuscar variáveis também.

## Página 68

68 Pacotes
Pacotes
Pacotes ( packages) são pastas que são identificadas pelo interpretador  pela  
presença de um arquivo com o nome “__init__.py”. Os pacotes funcionam  
como coleções para organizar módulos de forma hierárquica.
É possível importar todos os  módulos do pacote usando a declaração  from 
nome_do_pacote import *.
O arquivo “__init__.py” pode estar vazio ou conter código de inicialização do  
pacote ou definir uma variável chamada  __all__, uma lista de módulos do  
pacote serão importados quando for usado “*”. Sem o arquivo, o Python não  
identifica a pasta como um pacote válido.
componentes
display.py
lcd
oled
Esta pasta é um pacote.
sensor.py
termico
Identifica a pasta como pacote.
componentes.sensor.
componentes.sensor.termico.
componentes.display.crt.
componentes.display.oled.
__init__.py
crt
componentes.display.lcd.
componentes.display.

## Página 69

Biblioteca padrão 69
Biblioteca padrão
É comum dizer que o Python vem com “baterias inclusas”, em referência a  
vasta biblioteca de módulos e pacotes que é distribuída com o interpretador.
Alguns módulos importantes da biblioteca padrão:
▪ Matemática: math, cmath, decimal e random.
▪ Sistema: os, glob, shutils e subprocess.
▪ Threads: threading.
▪ Persistência: pickle e cPickle.
▪ XML: xml.dom, xml.sax e elementTree (a partir da versão 2.5).
▪ Configuração: ConfigParser e optparse.
▪ Tempo: time e datetime.
▪ Outros: sys, logging, traceback, types e timeit.
Matemática
Além dos tipos numéricos builtins do interpretador, na biblioteca padrão do  
Python  existem  vários  módulos  dedicados  a  implementar  outros  tipos  e  
operações matemáticas.
O  módulo  math define  funções  logarítmicas,  de  exponenciação,  
trigonométricas,  hiperbólicas  e  conversões  angulares,  entre  outras.  Já  o  
módulo  cmath, implementa  funções  similares,  porém  feitas  para  processar  
números complexos.
Exemplo:
# -*- coding: latin1 -*-
# Módulo para matemática
import math
# Módulo para matemática (de complexos)
import cmath
# Complexos
for cpx in [3j, 1.5 + 1j, -2 - 2j]:

## Página 70

70 Biblioteca padrão
    # Conversão para coordenadas polares
    plr = cmath.polar(cpx)
    print 'Complexo:', cpx
    print 'Forma polar:', plr, '(em radianos)'
    print 'Amplitude:', abs(cpx)
    print 'Ângulo:', math.degrees(plr[1]), '(graus)'
Saída:
Complexo: 3j
Forma polar: (3.0, 1.5707963267948966) (em radianos)
Amplitude: 3.0
Ângulo: 90.0 (graus)
Complexo:  (1.5+1j)
Forma polar: (1.8027756377319948, 0.5880026035475675) (em radianos)
Amplitude: 1.80277563773
Ângulo: 33.690067526 (graus)
Complexo:  (-2-2j)
Forma polar: (2.8284271247461903, -2.3561944901923448) (em radianos)
Amplitude: 2.82842712475
Ângulo: -135.0 (graus)
O módulo random traz funções para a geração de números aleatórios.
Exemplos:
# -*- coding: latin1 -*-
import random
import string
# Escolha uma letra
print random.choice(string.ascii_uppercase)
# Escolha um número de 1 a 10
print random.randrange(1, 11)
# Escolha um float no intervalo de 0 a 1
print random.random()
Saída:

## Página 71

Biblioteca padrão 71
I
4
0.680752701112
Na biblioteca padrão ainda existe o módulo  decimal, que define operações  
com números reais com precisão fixa.
Exemplo:
t = 5.
for i in range(50):
    t = t - 0.1
print 'Float:', t
t = Decimal('5.')
for i in range(50):
    t = t - Decimal('0.1')
print 'Decimal:', t
Saída:
Float: 1.02695629778e-15
Decimal: 0.0
Com  este  módulo,  é  possível  reduzir  a  introdução  de  erros  de  
arredondamento originados da aritmética de ponto flutuante.
Na  versão  2.6,  também  está  disponível  o  módulo  fractions,  que  trata  de  
números racionais.
Exemplo:
# -*- coding: latin1 -*-
from fractions import Fraction

## Página 72

72 Biblioteca padrão
# Três frações
f1 = Fraction('-2/3')
f2 = Fraction(3, 4)
f3 = Fraction('.25')
print "Fraction('-2/3') =", f1
print "Fraction('3, 4') =", f2
print "Fraction('.25') =", f3
# Soma
print f1, '+', f2, '=', f1 + f2
print f2, '+', f3, '=', f2 + f3
Saída:
Fraction('-2/3') = -2/3
Fraction('3, 4') = 3/4
Fraction('.25') = 1/4
-2/3 + 3/4 = 1/12
3/4 + 1/4 = 1
As frações podem ser inicializadas de várias formas: como  string, como um  
par de inteiros ou como um número real. O módulo também possui uma  
função chamada gcd(), que calcula o maior divisor comum (MDC) entre dois  
inteiros.
Arquivos e I/O
Os  arquivos  no  Python  são  representados  por  objetos  do  tipo  file18,  que 
oferecem métodos para diversas operações de arquivos. Arquivos podem ser 
abertos para leitura ('r', que é o  default), gravação ('w') ou adição ('a'), em  
modo texto ou binário('b').
Em Python:
▪ sys.stdin representa a entrada padrão.
▪ sys.stdout representa a saída padrão.
▪ sys.stderr representa a saída de erro padrão.
A entrada,  saída  e erro  padrões  são tratados  pelo Python como arquivos  
18 A referência open aponta para file.

## Página 73

Biblioteca padrão 73
abertos. A entrada em modo de leitura e os outros em modo de gravação.
Exemplo de escrita:
import sys
# Criando um objeto do tipo file
temp = open('temp.txt', 'w')
# Escrevendo no arquivo
for i in range(100):
    temp.write('%03d\n' % i)
# Fechando
temp.close()
temp = open('temp.txt')
# Escrevendo no terminal
for x in temp:
    # Escrever em sys.stdout envia
    # o texto para a saída padrão
    sys.stdout.write(x)
temp.close()
A cada iteração no segundo laço, o objeto retorna uma linha do arquivo de  
cada vez.
Exemplo de leitura:
import sys
import os.path
# raw_input() retorna a string digitada
fn = raw_input('Nome do arquivo: ').strip()
if not os.path.exists(fn):
    print 'Tente outra vez...'
    sys.exit()
# Numerando as linhas
for i, s in enumerate(open(fn)):

## Página 74

74 Biblioteca padrão
    print i + 1, s,
É possível ler todas as linhas com o método readlines():
# Imprime uma lista contendo linhas do arquivo
print open('temp.txt').readlines()
Os objetos do tipo arquivo também possuem um método seek(), que permite  
ir para qualquer posição no arquivo.
Na  versão  2.6,  está  disponível  o  módulo  io,  que  implementa  de  forma  
separada as operações de arquivo e as rotinas de manipulação de texto.
Sistemas de arquivo
Os sistemas operacionais modernos armazenam os arquivos em estruturas  
hierárquicas chamadas sistemas de arquivo (file systems).
Várias  funcionalidades  relacionadas  a  sistemas  de  arquivo  estão  
implementadas no módulo os.path, tais como:
▪ os.path.basename(): retorna o componente final de um caminho.
▪ os.path.dirname(): retorna um caminho sem o componente final.
▪ os.path.exists():  retorna  True se  o  caminho  existe  ou  False em  caso  
contrário.
▪ os.path.getsize(): retorna o tamanho do arquivo em bytes.
O glob é outro módulo relacionado ao sistema de arquivo:
import os.path
import glob
# Mostra uma lista de nomes de arquivos
# e seus respectivos tamanhos
for arq in sorted(glob.glob('*.py')):
    print arq, os.path.getsize(arq)
A função glob.glob() retorna uma lista com os nomes de arquivo que atendem  

## Página 75

Biblioteca padrão 75
ao critério passado como parâmetro, de forma semelhante ao comando “ls”  
disponível nos sistemas UNIX.
Arquivos temporários
O módulo os implementa algumas funções para facilitar a criação de arquivos 
temporários, liberando o desenvolvedor de algumas preocupações, tais como:
▪ Evitar colisões com nomes de arquivos que estão em uso.
▪ Identificar a área apropriada do sistema de arquivos para temporários  
(que varia conforme o sistema operacional).
▪ Expor a aplicação a riscos (a área de temporários é utilizada por outros  
processos).
Exemplo:
# -*- coding: latin1 -*-
import os
texto = 'Teste'
# cria um arquivo temporário
temp = os.tmpfile()
# Escreve no arquivo temporário
temp.write('Teste')
# Volta para o inicio do arquivo
temp.seek(0)
# Mostra o conteúdo do arquivo
print temp.read()
# Fecha o arquivo
temp.close()
Saída:
Teste
Existe também a função tempnam(), que retorna um nome válido para arquivo 
temporário, incluindo um caminho que respeite as convenções do sistema  

## Página 76

76 Biblioteca padrão
operacional. Porém, fica por conta do desenvolvedor garantir que a rotina  
seja usada de forma a não comprometer a segurança da aplicação.
Arquivos compactados
O Python possui módulos para trabalhar com vários formatos de arquivos  
compactados.
Exemplo de gravação de um arquivo “.zip”:
# -*- coding: latin1 -*-
"""
Gravando texto em um arquivo compactado
"""
import zipfile
texto = """
***************************************
Esse é o texto que será compactado e...
... guardado dentro de um arquivo zip.
***************************************
"""
# Cria um zip novo
zip = zipfile.ZipFile('arq.zip', 'w',
    zipfile.ZIP_DEFLATED)
# Escreve uma string no zip como se fosse um arquivo
zip.writestr('texto.txt', texto)
# Fecha o zip
zip.close()
Exemplo de leitura:
# -*- coding: latin1 -*-
"""
Lendo um arquivo compactado
"""
import zipfile

## Página 77

Biblioteca padrão 77
# Abre o arquivo zip para leitura
zip = zipfile.ZipFile('arq.zip')
# Pega a lista dos arquivos compactados
arqs = zip.namelist()
for arq in arqs:
    # Mostra o nome do arquivo
    print 'Arquivo:', arq
    # Pegando as informações do arquivo
    zipinfo = zip.getinfo(arq)
    print 'Tamanho original:', zipinfo.file_size
    print 'Tamanho comprimido:', zipinfo.compress_size
    # Mostra o conteúdo do arquivo
    print zip.read(arq)
Saída:
Arquivo: texto.txt
Tamanho original: 160
Tamanho comprimido: 82
***************************************
Esse é o texto que será compactado e...
... guardado dentro de um arquivo zip.
***************************************
O Python também provê módulos para os formatos gzip, bzip2 e tar, que são  
bastante utilizados em ambientes UNIX.
Arquivos de dados
Na biblioteca padrão, o Python também fornece um módulo para simplificar  
o processamento de arquivos no formato CSV (Comma Separated Values).
No formato CSV, os dados são armazenados em forma de texto, separados  
por vírgula, um registro por linha.
Exemplo de escrita:

## Página 78

78 Biblioteca padrão
import csv
# Dados
dt = (('temperatura', 15.0, 'C', '10:40', '2006-12-31'),
    ('peso', 42.5, 'kg', '10:45', '2006-12-31'))
# A rotina de escrita recebe um objeto do tipo file
out = csv.writer(file('dt.csv', 'w'))
# Escrevendo as tuplas no arquivo
out.writerows(dt)
Arquivo de saída:
temperatura,15.0,C,10:40,2006-12-31
peso,42.5,kg,10:45,2006-12-31
Exemplo de leitura:
import csv
# A rotina de leitura recebe um objeto arquivo
dt = csv.reader(file('dt.csv'))
# Para cada registro do arquivo, imprima
for reg in dt:
    print reg
Saída:
['temperatura', '15.0', 'C', '10:40', '2006-12-31']
['peso', '42.5', 'kg', '10:45', '2006-12-31']
O formato CSV é aceito pela maioria das planilhas e sistemas de banco de  
dados para importação e exportação de informações.
Sistema operacional
Além  do  sistema  de  arquivos,  os  módulos  da  biblioteca  padrão  também  
fornecem acesso a outros serviços providos pelo sistema operacional.

## Página 79

Biblioteca padrão 79
Exemplo:
# -*- coding: utf-8 -*-
import os
import sys
import platform
def uid():
    """
    uid() -> retorna a identificação do usuário
    corrente ou None se não for possível identificar
    """
    # Variáveis de ambiente para cada
    # sistema operacional
    us = {'Windows': 'USERNAME',
        'Linux': 'USER'}
    u = us.get(platform.system())
    return os.environ.get(u)
print 'Usuário:', uid()
print 'plataforma:', platform.platform()
print 'Diretório corrente:', os.path.abspath(os.curdir)
exep, exef = os.path.split(sys.executable)
print 'Executável:', exef
print 'Diretório do executável:', exep
Saída:
Usuário: l
plataforma: Linux-2.6.31-16-generic-x86_64-with-Ubuntu-9.10-karmic
Diretório corrente: /home/l
Executável: python
Diretório do executável: /usr/bin
Exemplo de execução de processo:
# -*- coding: latin1 -*-

## Página 80

80 Biblioteca padrão
import sys
from subprocess import Popen, PIPE
# ping
cmd = 'ping -c 1 '
# No Windows
if sys.platform == 'win32':
    cmd = 'ping -n 1 '
# Local só para testar
host = '127.0.0.1'
# Comunicação com outro processo,
# um pipe com o stdout do comando
py = Popen(cmd + host, stdout=PIPE)
# Mostra a saída do comando
print py.stdout.read()
O módulo subprocess provê uma forma genérica de execução de processos, na  
função Popen(), que permite a comunicação com o processo através pipes do  
sistema operacional.
Tempo
O Python possui dois módulos para lidar com tempo:
▪ time: implementa funções que permitem utilizar o tempo gerado pelo  
sistema.
▪ datetime: implementa tipos de alto nível para realizar operações de data  
e hora.
Exemplo com time:
# -*- coding: latin-1 -*-
import time
# localtime() Retorna a data e hora local no formato
# de uma estrutura chamada struct_time, que é uma
# coleção com os itens: ano, mês, dia, hora, minuto,
# segundo, dia da semana, dia do ano e horário de verão
print time.localtime()

## Página 81

Biblioteca padrão 81
# asctime() retorna a data e hora como string, conforme
# a configuração do sistema operacional
print time.asctime()
# time() retorna o tempo do sistema em segundos
ts1 = time.time()
# gmtime() converte segundos para struct_time
tt1 = time.gmtime(ts1)
print ts1, '->', tt1
# Somando uma hora
tt2 = time.gmtime(ts1 + 3600.)
# mktime() converte struct_time para segundos
ts2 = time.mktime(tt2)
print ts2, '->', tt2
# clock() retorma o tempo desde quando o programa
# iniciou, em segundos
print 'O programa levou', time.clock(), \
    'segundos até agora...'
# Contando os segundos...
for i in xrange(5):
    # sleep() espera durante o número de segundos
    # especificados como parâmetro
    time.sleep(1)
    print i + 1, 'segundo(s)'
Saída:
time.struct_time(tm_year=2010,  tm_mon=1,  tm_mday=16,  tm_hour=18,  
tm_min=7, tm_sec=59, tm_wday=5, tm_yday=16, tm_isdst=1)
Sat Jan 16 18:07:59 2010
1263672479.6  ->  time.struct_time(tm_year=2010,  tm_mon=1,  
tm_mday=16,  tm_hour=20,  tm_min=7,  tm_sec=59,  tm_wday=5,  
tm_yday=16, tm_isdst=0)
1263686879.0  ->  time.struct_time(tm_year=2010,  tm_mon=1,  
tm_mday=16,  tm_hour=21,  tm_min=7,  tm_sec=59,  tm_wday=5,  
tm_yday=16, tm_isdst=0)
O programa levou 1.46666685291e-06 segundos até agora...
1 segundo(s)

## Página 82

82 Biblioteca padrão
2 segundo(s)
3 segundo(s)
4 segundo(s)
5 segundo(s)
Em datetime, estão definidos quatro tipos para representar o tempo:
▪ datetime: data e hora.
▪ date: apenas data.
▪ time: apenas hora.
▪ timedelta: diferença entre tempos.
Exemplo:
# -*- coding: latin-1 -*-
import datetime
# datetime() recebe como parâmetros:
# ano, mês, dia, hora, minuto, segundo
# e retorna um objeto do tipo datetime
dt = datetime.datetime(2020, 12, 31, 23, 59, 59)
# Objetos date e time podem ser criados
# a partir de um objeto datetime
data = dt.date()
hora = dt.time()
# Quanto tempo falta para 31/12/2020
dd = dt - dt.today()
print 'Data:', data
print 'Hora:', hora
print 'Quanto tempo falta para 31/12/2020:', \
    str(dd).replace('days', 'dias')
Saída:
Data: 2020-12-31
Hora: 23:59:59
Quanto tempo falta para 31/12/2020: 4616 dias, 13:22:58.857000

## Página 83

Biblioteca padrão 83
Os objetos dos tipos date e datetime retornam datas em formato ISO.
Expressões regulares
Expressão regular é uma maneira de identificar padrões em sequências de  
caracteres.  No  Python,  o  módulo  re  provê  um  analisador  sintático  que  
permite o uso de tais expressões. Os padrões definidos através de caracteres  
que tem significado especial para o analisador.
Principais caracteres:
▪ Ponto (.): Em modo padrão, significa qualquer caractere, menos o de  
nova linha.
▪ Circunflexo (^): Em modo padrão, significa inicio da string.
▪ Cifrão ($): Em modo padrão, significa fim da string.
▪ Contra-barra (\): Caractere de escape, permite usar caracteres especiais  
como se fossem comuns.
▪ Colchetes ([]): Qualquer caractere dos listados entre os colchetes.
▪ Asterisco (*): Zero ou mais ocorrências da expressão anterior.
▪ Mais (+): Uma ou mais ocorrências da expressão anterior.
▪ Interrogação (?): Zero ou uma ocorrência da expressão anterior.
▪ Chaves ({n}): n ocorrências da expressão anterior.
▪ Barra vertical (|): “ou” lógico.
▪ Parenteses (()): Delimitam um grupo de expressões.
▪ \d: Dígito. Equivale a [0-9].
▪ \D: Não dígito. Equivale a [^0-9].
▪ \s: Qualquer caractere de espaçamento ([ \t\n\r\f\v]).
▪ \S: Qualquer caractere que não seja de espaçamento.([^ \t\n\r\f\v]).
▪ \w: Caractere alfanumérico ou sublinhado ([a-zA-Z0-9_]).
▪ \W: Caractere que não seja alfanumérico ou sublinhado ([^a-zA-Z0-
9_]).
Exemplos:
# -*- coding: latin1 -*-
import re
# Compilando a expressão regular

## Página 84

84 Biblioteca padrão
# Usando compile() a expressão regular fica compilada
# e pode ser usada mais de uma vez
rex = re.compile('\w+')
# Encontra todas as ocorrências que atendam a expressão
bandas = 'Yes, Genesis & Camel'
print bandas, '->', rex.findall(bandas)
# Identifica as ocorrências de Björk (e suas variações)
bjork = re.compile('[Bb]j[öo]rk')
for m in ('Björk', 'björk', 'Biork', 'Bjork', 'bjork'):
    # match() localiza ocorrências no inicio da string
    # para localizar em qualquer parte da string, use search()
    print m, '->', bool(bjork.match(m))
# Substituindo texto
texto = 'A próxima faixa é Stairway to Heaven'
print texto, '->', re. sub('[Ss]tairway [Tt]o [Hh]eaven',
    'The Rover', texto)
# Dividindo texto
bandas = 'Tool, Porcupine Tree e NIN'
print bandas, '->', re.split(',?\s+e?\s+', bandas)
Saída:
Yes, Genesis & Camel -> ['Yes', 'Genesis', 'Camel']
Björk -> True
björk -> True
Biork -> False
Bjork -> True
bjork -> True
A próxima faixa é Stairway to Heaven -> A próxima faixa é The Rover
Tool, Porcupine Tree e NIN -> ['Tool, Porcupine Tree', 'NIN']
O comportamento das funções desse módulo pode ser alterado por opções,  
para tratar as strings como unicode, por exemplo.

## Página 85

Bibliotecas de terceiros 85
Bibliotecas de terceiros
Existem  muitas  bibliotecas  escritas  por  terceiros  disponíveis  para  Python, 
compostas  por  pacotes  ou  módulos,  que  implementam  diversos  recursos  
além da biblioteca padrão.
Geralmente, as bibliotecas são distribuídas das seguintes formas:
▪ Pacotes distutils.
▪ Pacotes para gerenciadores de pacotes do Sistema Operacional.
▪ Instaladores.
▪ Python Eggs.
Os pacotes usando o módulo  distutils, que é distribuído com o Python,  são  
muito  populares.  Os  pacotes  são  distribuídos  em  arquivos  compactados  
(geralmente  “.tar.gz”,  “.tar.bz2”  ou  “.zip”).  Para  instalar,  é  necessário  
descompactar o arquivo, entrar na pasta que foi descompactada e por fim  
executar o comando:
python setup.py install
Que o pacote será instalado na pasta “site-packages” no Python.
Gerenciadores de pacotes do Sistema Operacional, geralmente trabalham com 
formatos próprios de pacote, como “.deb” (Debian Linux) ou “.rpm” (RedHat  
Linux). A forma de instalar os pacotes depende do gerenciador utilizado. A  
grande vantagem é que o gerenciador de pacotes cuida das dependências e  
atualizações.
Programas  instaladores  são  nada  mais  que  executáveis  que  instalam  a  
biblioteca.  Geralmente  são  usados  em  ambiente  Windows  e  podem  ser  
desinstalados pelo Painel de Controle.
Python  Egg é  um  formato  de  pacote  (com  a  extensão  “.egg”)  que  é  
administrado pelo easy_install, utilitário que faz parte do projeto setuptools 19. 
Semelhante a algumas ferramentas encontradas em outras linguagens, como  
19 Fontes e documentação em: http://peak.telecommunity.com/DevCenter/setuptools/.

## Página 86

86 Bibliotecas de terceiros
o Ruby Gems, aos poucos está se tornando o padrão de fato para distribuição  
de bibliotecas em Python.
O programa  procura  pela  versão  mais  nova  do  pacote  no PYPI 20 ( Python 
Package Index ), repositório de pacotes Python, e também procura instalar as  
dependências que forem necessárias.
Pacotes Python Eggs podem ser instalados pelo comando:
easy_install nome_do_pacote
O script easy_install é instalado na pasta “scripts” do Python.
20 Endereço: http://pypi.python.org/pypi.

## Página 87

Exceções 87
Exceções
Quando ocorre uma falha no programa (como uma divisão por zero, por  
exemplo) em tempo de execução, uma exceção é gerada. Se a exceção não for  
tratada, ela será propagada através das chamadas de função até o módulo  
principal do programa, interrompendo a execução.
print 1/0
Traceback (most recent call last):
  File "<input>", line 1, in ?
ZeroDivisionError: integer division or modulo by zero
A instrução try permite o tratamento de exceções no Python. Se ocorrer uma  
exceção em um bloco marcado com try, é possível tratar a exceção através da  
instrução except. Podem existir vários blocos except para o mesmo bloco try.
try:
    print 1/0
except ZeroDivisionError:
    print 'Erro ao tentar dividir por zero.'
Saída:
Erro ao tentar dividir por zero.
Se except recebe o nome da exceção, só esta será tratada. Se não for passada  
nenhuma exceção como parâmetro, todas serão tratadas.
Exemplo:
import traceback
# Tente receber o nome do arquivo
try:
    fn = raw_input('Nome do arquivo: ').strip()

## Página 88

88 Exceções
    # Numerando as linhas
    for i, s in enumerate(file(fn)):
        print i + 1, s,
# Se ocorrer um erro
except:
    # Mostre na tela
    trace = traceback.format_exc()
    # E salve num arquivo
    print 'Aconteceu um erro:\n', trace
    file('trace.log', 'a').write(trace)
    # Encerre o programa
    raise SystemExit
O módulo traceback oferece funções para manipular as mensagens de erro. A  
função format_exc retorna a saída da última exceção formatada em uma string.
O tratamento de  exceções pode possuir um bloco  else, que será executado  
quando não ocorrer nenhuma exceção e um bloco finally, será executado de  
qualquer  forma,  tendo  ocorrido  uma  exceção  ou  não 21.  Novos  tipos  de  
exceções podem ser definidos através de herança a partir da classe Exception.
A partir da versão 2.6, está disponível a instrução with, que pode substituir a  
combinação try / finally em várias situações. Com with, podemos definir um  
objeto que será usado durante a execução do bloco. O objeto precisa suportar  
o  protocolo  de  gerenciamento  de  contexto,  o  que  significa  que  ele  deve  
possuir um método  __enter__(), que é executado no inicio do bloco, e outro  
chamado __exit__(), que é evocado ao final do bloco.
Exemplo:
# -*- coding: latin-1 -*-
21 A declaração finally pode ser usada para liberar recursos que foram usados no bloco try, 
tais como conexões de banco de dados ou arquivos abertos.

## Página 89

Exceções 89
import random
# Cria um arquivo com 25 números randômicos
with file('temp.txt', 'w') as temp:
    for y in range(5):
        for x in range(5):
            # "print >> " grava a saída do comando no arquivo indicado
            print >> temp, '%.2f' % random.random(),
        print >> temp
# Exibe o conteúdo do arquivo
with file('temp.txt') as temp:
    for i in temp:
        print i,
# Fora dos blocos, o arquivo está fechado
# Isso gera uma exceção ValueError: I/O operation on closed file
print >> temp
Exemplo de saída:
0.61 0.09 0.91 0.94 0.11
0.41 0.01 0.88 0.61 0.91
0.49 0.54 0.29 0.72 0.42
0.44 0.75 0.47 0.62 0.73
0.13 0.66 0.87 0.60 0.35
Traceback (most recent call last):
  File "wt01.py", line 15, in <module>
    print >> temp
ValueError: I/O operation on closed file
Como o arquivo foi fechado ao final do bloco, a tentativa de gravação gera  
uma exceção.

## Página 90

90 Introspecção
Introspecção
Introspecção ou  reflexão é capacidade do software de identificar e relatar  
suas  próprias  estruturas  internas,  tais  como  tipos,  escopo  de  variáveis,  
métodos e atributos.
Funções nativas do interpretador para introspecção:
Função Retorno
type(objeto) O tipo (classe) do objeto
id(objeto) O identificador do objeto
locals() O dicionário de variáveis locais
globals() O dicionário de variáveis globais
vars(objeto) O dicionário de símbolos do objeto
len(objeto) O tamanho do objeto
dir(objeto) A lista de estruturas do objeto
help(objeto) As Doc Strings do objeto
repr(objeto) A representação do objeto
isinstance(objeto, classe) Verdadeiro se objeto deriva da classe
issubclass(subclasse, classe) Verdadeiro se subclasse herda classe
O  identificador  do  objeto  é  um  número  inteiro  único  que  é  usado  pelo  
interpretador para identificar internamente os objetos.
Exemplo:
# -*- coding: latin1 -*-
# Colhendo algumas informações
# dos objetos globais no programa
from types import ModuleType
def info(n_obj):
    # Cria uma referência ao objeto
    obj = globals()[n_obj]

## Página 91

Introspecção 91
    # Mostra informações sobre o objeto
    print 'Nome do objeto:', n_obj
    print 'Identificador:', id(obj)
    print 'Tipo:', type(obj)
    print 'Representação:', repr(obj)
    # Se for um módulo
    if isinstance(obj, ModuleType):
        print 'itens:'
        for item in dir(obj):
            print item
    print
# Mostrando as informações
for n_obj in dir():
    info(n_obj)
O Python também tem um módulo chamado types, que tem as definições dos  
tipos básicos do interpretador.
Exemplo:
# -*- coding: latin-1 -*-
import types
s = ''
if isinstance(s, types.StringType):
    print 's é uma string.'
Através da introspecção, é possível determinar os campos de uma tabela de  
banco de dados, por exemplo.
Inspect
O  módulo  inspect provê  um  conjunto  de  funções  de  alto  nível  para  
introspecção que  permitem  investigar  tipos  ,  itens  de  coleções,  classes,  
funções, código fonte e a pilha de execução do interpretador.
Exemplo:

## Página 92

92 Introspecção
# -*- coding: latin1 -*-
import os.path
# inspect: módulo de introspecção "amigável"
import inspect
print 'Objeto:', inspect.getmodule(os.path)
print 'Classe?', inspect.isclass(str)
# Lista todas as funções que existem em "os.path"
print 'Membros:',
for name, struct in inspect.getmembers(os.path):
    if inspect.isfunction(struct):
        print name, 
Saída:
Objeto: <module 'ntpath' from 'c:\python26\lib\ntpath.pyc'>
Classe? True
Membros:  abspath  basename  commonprefix  dirname  exists  expanduser  
expandvars  getatime  getctime  getmtime  getsize  isabs  isdir  isfile  islink  
ismount  join  lexists  normcase  normpath  realpath  relpath  split  splitdrive  
splitext splitunc walk
As funções que trabalham com a pilha do interpretador devem ser usadas  
com  cuidado,  pois  é  possível  criar  referências  cíclicas  (uma  variável  que  
aponta para o item da pilha que tem a própria variável).  A existência de  
referências a itens da pilha retarda a destruição dos itens pelo coletor de lixo  
do interpretador.

## Página 93

Exercícios II 93
Exercícios II
1.  Implementar  um  programa  que  receba  um  nome  de  arquivo  e  gere  
estatísticas  sobre  o  arquivo  (número  de  caracteres,  número  de  linhas  e  
número de palavras)
2. Implementar um módulo com duas funções:
▪ matrix_sum(*matrices), que retorna a matriz soma de matrizes de duas  
dimensões.
▪ camel_case(s), que converte nomes para CamelCase.
3. Implementar uma função que leia um arquivo e retorne uma lista de tuplas  
com os dados (o separador de campo do arquivo é vírgula), eliminando as  
linhas  vazias.  Caso  ocorra  algum  problema,  imprima  uma  mensagem  de  
aviso e encerre o programa.
4. Implementar um módulo com duas funções:
▪ split(fn, n) , que quebra o arquivo fn em partes de n  bytes e salva com  
nomes sequenciais (se fn = arq.txt, então arq_001.txt, arq_002.txt, ... )
▪ join(fn, fnlist) que junte os arquivos da lista fnlist em um arquivo só fn.
5. Crie um script que:
▪ Compare a lista de arquivos em duas pastas distintas.
▪ Mostre os nomes dos arquivos que tem conteúdos diferentes e/ou que  
existem em apenas uma das pastas.
6. Faça um script que:
▪ Leia um arquivo texto.
▪ Conte as ocorrências de cada palavra.
▪ Mostre os resultados ordenados pelo número de ocorrências.

## Página 94

94 Parte III
Parte III
Esta parte é dividida em dois assuntos: geradores, uma tecnologia cada vez  
mais presente na linguagem, e programação funcional.
Conteúdo:
▪ Geradores  .
▪ Programação funcional  .
▪ Exercícios III  .

## Página 95

Geradores 95
Geradores
As funções geralmente seguem o fluxo convencional de processar, retornar  
valores e encerrar. Geradores funcionam de forma similar, porém lembram o  
estado do processamento entre as chamadas, permanecendo em memória e  
retornando o próximo item esperado quando ativados.
Os  geradores  apresentam  várias  vantagens  em  relação  às  funções  
convencionais:
▪ Lazy  Evaluation:  geradores  só  são  processados  quando  é  realmente  
necessário, sendo assim, economizam recursos de processamento.
▪ Reduzem a necessidade da criação de listas.
▪ Permitem trabalhar com sequências ilimitadas de elementos.
Geradores geralmente  são  evocados  através  de  um  laço  for.  A  sintaxe  é  
semelhante a da função tradicional, só que a instrução yield substitui o return. 
A nova cada iteração, yield retorna o próximo valor.
Exemplo:
# -*- coding: latin-1 -*-
def gen_pares():
    """
    Gera números pares infinitamente...
    """
    i = 0
    while True:
        i += 2
        yield i
# Mostra cada número e passa para o próximo
for n in gen_pares():
    print n
Outro exemplo:

## Página 96

96 Geradores
# -*- coding: latin-1 -*-
import os
# Encontra arquivos recursivamente
def find(path='.'):
    for item in os.listdir(path):
        fn = os.path.normpath(os.path.join(path, item))
        if os.path.isdir(fn):
            for f in find(fn):
                yield f
        else:
            yield fn
# A cada iteração, o gerador devolve
# um novo nome de arquivo
for fn in find('c:/temp'):
    print fn
Existem vários geradores  que fazem parte  da própria linguagem,  como o  
builtin xrange()22.  Além  disso,  n o  módulo  itertools,  estão  definidos  vários  
geradores úteis.
Para converter a saída do gerador em uma lista:
lista = list(gerador())
Assim, todos os itens serão gerados de uma vez.
22 O gerador xrange() pode substituir a função range() na maioria dos casos e a sintaxe é a  
mesma, com a vantagem de economizar memória.

## Página 97

Programação funcional 97
Programação funcional
Programação funcional  é um paradigma que trata a computação como uma  
avaliação  de  funções  matemáticas.  Tais  funções  podem  ser  aplicadas  em  
sequências  de  dados  (geralmente  listas).  São  exemplos  de  linguagens  
funcionais:  LISP,  Scheme  e  Haskell  (esta  última  influenciou  o  projeto  do 
Python de forma marcante).
As operações básicas do paradigma funcional são implementadas no Python  
pelas funções builtin map(), filter(), reduce() e zip().
Lambda
No Python, lambda é uma função anônima composta apenas por expressões.  
As funções  lambda podem ter apenas uma linha, e podem ser atribuídas a  
uma variável. Funções lambda são muito usadas em programação funcional.
Sintaxe:
lambda <lista de variáveis>: <expressões >
Exemplo:
# Amplitude de um vetor 3D
amp = lambda x, y, z: (x ** 2 + y ** 2 + z ** 2) ** .5
print amp(1, 1, 1)
print amp(3, 4, 5)
Saída:
1.73205080757
7.07106781187
Funções  lambda consomem menos recursos computacionais que as funções  
convencionais, porém são mais limitados.

## Página 98

98 Programação funcional
Mapeamento
O mapeamento  consiste  em aplicar  uma função  a todos  os itens  de  uma  
sequência,  gerando  outra  lista  contendo  os  resultados  e  com  o  mesmo  
tamanho da lista inicial.
No Python, o mapeamento é implementado pela função map().
Exemplos:
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# log na base 10
from math import log10
print map(log10, nums)
# Dividindo por 3
print map(lambda x: x / 3, nums)
A função map() sempre retorna uma lista.
Lista
1
2
3
4
5
6
7
Lista
1
4
9
16
25
36
49
Função
x**2

## Página 99

Programação funcional 99
Filtragem
Na filtragem, uma função é aplicada em todos os itens de uma sequência, se a  
função retornar um valor que seja avaliado como verdadeiro, o item original  
fará parte da sequência resultante.
No Python, a filtragem é implementada pela função filter().
Exemplo:
# Selecionando apenas os ímpares
print filter(lambda x: x % 2, nums)
A  função  filter() aceita  também  funções  lambda,  além  de  funções  
convencionais.
Lista
 Lista
1
3
5
7
Função
x % 2
Falso
Falso
Falso
1
2
3
4
5
6
7

## Página 100

100 Programação funcional
Redução
Redução significa aplicar uma função que recebe dois parâmetros, nos dois  
primeiros elementos de uma sequência, aplicar novamente a função usando  
como parâmetros o resultado do primeiro par e o terceiro elemento, seguindo  
assim até o final da sequência. O resultado final da redução é apenas um  
elemento.
Exemplos de redução, que é implementada no Python pela função reduce():
# -*- coding: latin1 -*-
nums = range(100)
# Soma com reduce (pode concatenar strings)
print reduce(lambda x, y: x + y, nums)
# Soma mais simples, mas só para números
print sum(nums)
Saída:
Lista
 Resultado
1
3
6
10
15
21
28
Função
x + y
1
2
3
4
5
6
7

## Página 101

Programação funcional 101
4950
4950
A função reduce() pode ser usada para calcular fatorial:
# Calcula o fatorial de n
def fat(n):
    return reduce(lambda x, y: x * y, range(1, n))
print fat(6)
Saída:
120
A partir da versão 2.6, o módulo  math traz uma função que calcula fatorial  
chamada factorial().

## Página 102

102 Programação funcional
Transposição
Transposição é construir uma série de sequências a partir de outra série de  
sequências, aonde a primeira nova sequência contém o primeiro elemento de  
cada  sequência  original,  a  segunda  nova  sequência  contém  o  segundo  
elemento  de   cada  sequência  original,  até  que  alguma  das  sequências  
originais acabe.
Exemplo de transposição, que é implementada no Python pela função zip():
# Uma lista com ('a', 1), ('b', 2), ...
from string import ascii_lowercase
print zip(ascii_lowercase, range(1, 100))
# Transposta de uma matriz
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print zip(*matriz)
A função zip() sempre retorna uma lista de tuplas.
Listas
1
2
3
4
5
6
Listas
1
4
2
5
3
6
Função

## Página 103

Programação funcional 103
List Comprehension
Em computação,  List Comprehension  é uma construção que equivale a uma  
notação matemática do tipo:
Ou seja, S é o conjunto formado por x ao quadrado para todo x no conjunto  
dos números naturais, se x for maior ou igual a 20.
Sintaxe:
lista = [ <expressão> for <referência> in <sequência> if <condição> ]
Exemplo:
# -*- coding: latin1 -*-
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# Eleve os ímpares ao quadrado
print [ x**2 for x in nums if x % 2 ]
Saída:
[1, 9, 25, 49, 81, 121]
List Comprehension é mais eficiente do que usar as funções map() e filter() tanto 
em termos de uso de processador quanto em consumo de memória.
S={x2
∀ xem ℕ , x20}

## Página 104

104 Programação funcional
Generator Expression
Generator Expression é uma expressão que se assemelha ao List Comprehension, 
porém funciona como um gerador.
Exemplo:
# -*- coding: latin1 -*-
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# Eleve os ímpares ao quadrado
gen = ( x**2 for x in nums if x % 2 )
# Mostra os resultados
for num in gen:
    print num
Outro exemplo:
# Uma lista de tuplas (artista, faixa):
instrumentais = [('King Crimson', 'Fracture'),
    ('Metallica','Call of Ktulu'),
    ('Yes', 'Mood for a Day'),
    ('Pink Floyd', 'One of This Days'),
    ('Rush', 'YYZ')]
# Filtra e ordena apenas as faixas de artistas anteriores a letra N
print sorted(faixa[-1] + ' / ' + faixa[0]
    for faixa in instrumentais if
    faixa[0].upper() < 'N')
Saída:
['Call of Ktulu / Metallica', 'Fracture / King Crimson']
Generator  Expression  usa  menos  recursos  do  que  o  List  Comprehension  
equivalente,  pois  os  itens  são  gerados  um  de  cada  vez,  apenas  quando  
necessário, economizando principalmente memória.

## Página 105

Exercícios III 105
Exercícios III
1. Implementar um gerador de números primos.
2. Implementar o gerador de números primos como uma expressão (dica: use  
o módulo itertools).
3. Implementar um gerador que produza tuplas com as cores do padrão RGB  
(R, G e B variam de 0 a 255) usando xrange() e uma função que produza uma  
lista com as tuplas RGB usando range(). Compare a performance.
4. Implementar um gerador que leia um arquivo e retorne uma lista de tuplas  
com os dados (o separador de campo do arquivo é vírgula), eliminando as  
linhas  vazias.  Caso  ocorra  algum  problema,  imprima  uma  mensagem  de  
aviso e encerre o programa.

## Página 106

106 Parte IV
Parte IV
Esta parte se concentra principalmente na orientação a objetos,  e também  
aborda decoradores e testes automatizados.
Conteúdo:
▪ Decoradores  .
▪ Classes  .
▪ Herança simples  .
▪ Herança múltipla  .
▪ Propriedades  .
▪ Sobrecarga de operadores  .
▪ Metaclasses  .
▪ Decoradores de classe  .
▪ Testes automatizados  .
▪ Exercícios IV  .

## Página 107

Decoradores 107
Decoradores
Decoradores ( decorators) são funções que são aplicadas em outras funções e  
retornam  funções modificadas.  Decoradores tanto  podem  ser  usados  para  
criar  ou  alterar  características  das  funções  (que  são  objetos)  quanto  para  
“envolver” as funções, acrescentando uma camada em torno delas com novas  
funcionalidades.
A partir do Python 2.4, o caractere “@” pode ser usado para automatizar o  
processo de aplicação do decorador:
def decorator(f):
   f.decorated = True
   return f
@decorator
def func(arg):
   return arg
Com isso, foi criado um atributo novo na função, que pode ser usado depois,  
Função
Original
Função
Modificada
def func(arg):
   return arg
def decorator(f):
   f.decorated = True
   return f
func = decorator(func)
Decorador
O decorador foi aplicado.

## Página 108

108 Decoradores
quando a função for executada.
Exemplo:
# -*- coding: latin1 -*-
# Função decoradora
def dumpargs(f):
    # Função que envolverá a outra
    def func(*args):
        # Mostra os argumentos passados para a função
        print args
        # Retorna o resultado da função original
        return f(*args)
    # Retorna a função modificada
    return func
@dumpargs
def multiply(*nums):
    m = 1
    for n in nums:
        m = m * n
    return m
print multiply(1, 2, 3)
Saída:
(1, 2, 3)
6
A saída apresenta os parâmetros que a função decorada recebeu.

## Página 109

Classes 109
Classes
Objetos são abstrações computacionais que representam entidades, com  suas  
qualidades (atributos) e ações (métodos) que estas podem realizar. A classe é  
a estrutura básica do paradigma de orientação a objetos, que representa o tipo 
do objeto, um modelo a partir do qual os objetos serão criados.
Por exemplo, a classe  Canino descreve as características e ações dos caninos  
em geral, enquanto o objeto Bandit representa um canino em particular.
Os atributos são estruturas de dados que armazenam informações sobre o  
objeto e os métodos são funções associadas ao objeto, que descrevem como o  
objeto se comporta.
No  Python,  novos  objetos são  criados  a  partir  das  classes através  de  
atribuição.  O  objeto  é  uma  instância  da  classe,  que  possui  características  
próprias.  Quando  um  novo  objeto  é  criado,  o  construtor da  classe  é  
executado.  Em  Python,  o  construtor  é  um  método  especial,  chamado  
__new__(). Após a chamada ao construtor, o método  __init__() é chamado  
Canino
Peso, Altura, 
idade, Raça
Correr, Atacar, 
Comer, Latir
Suas 
características.
O que ele pode 
fazer.
Bandit
Peso, Altura, 
idade, Raça
Correr, Atacar, 
Comer, Latir
A classe 
representa 
qualquer canino.
O objeto 
representa um 
canino.
Bandit = Canino()

## Página 110

110 Classes
para inicializar a nova instância.
Um objeto continua existindo na memória enquanto existir pelo menos uma  
referência a ele. O interpretador Python possui um recurso chamado coletor  
de lixo ( Garbage Collector ) que limpa da memória  objetos sem referências 23. 
Quando o objeto é apagado, o método especial __done__() é evocado. Funções 
ligadas ao coletor de lixo podem ser encontradas no módulo gc.
Em Python:
▪ Quase tudo é objeto, mesmo os tipos básicos, como números inteiros.
▪ Tipos e classes são unificados.
▪ Os operadores são na verdade chamadas para métodos especiais.
▪ As classes são abertas (menos para os tipos builtins).
Métodos especiais são identificados por nomes no padrão __metodo__() (dois 
sublinhados  no  início  e  no  final  do  nome)  e  definem  como  os  objetos 
derivados  da  classe  se  comportarão  em  situações  particulares,  como  em  
sobrecarga de operadores.
23 Para apagar uma referência a um objeto, use o comando  del. Se todas as referências  
forem apagadas, o Garbage Collector apagará o objeto.
Classe
Métodos de 
classe
Atributos de 
classe
Métodos 
estáticos
Objeto
Métodos de 
classe
Atributos de 
classe
Métodos 
estáticos
Métodos 
dinâmicos
Atributos de 
objeto
Objeto = Classe()
O construtor é executado neste 
momento.

## Página 111

Classes 111
No Python, existem dois tipos de classes, chamadas  old style  e  new style . As  
classes new  style são  derivadas  da  classe  object e  podem  utilizar  recursos  
novos das  classes do Python, como  properties e  metaclasses. As  properties são  
atributos calculados em tempo de execução através de métodos, enquanto as  
metaclasses são  classes que geram  classes, com isso permitem personalizar o  
comportamento das classes. As classes old style são uma herança das versões  
antigas  do  Python,  mantidas  para  garantir  compatibilidade  com  código  
legado.
Sintaxe:
# -*- coding: latin1 -*-
class Classe(supcl1, supcl2):
    """
    Isto é uma classe
    """
    clsvar = []
    def __init__(self, args):
        """
        Inicializador da classe
        """
        <bloco de código>
    def __done__(self):
        """
        Destrutor da classe
        """
        <bloco de código>
    def metodo(self, params):
        """
        Método de objeto
        """
        <bloco de código>
    @classmethod
    def cls_metodo(cls, params):
        """
        Método de classe
        """

## Página 112

112 Classes
        <bloco de código>
    @staticmethod
    def est_metodo(params):
        """
        Método estático
        """
        <bloco de código>
obj = Classe()
obj.metodo()
Classe.cls_metodo()
Classe.est_metodo()
Métodos  de  objeto podem  usar  atributos  e  outros  métodos  do  objeto.  A  
variável self, que representa o objeto e também precisa ser passado de forma  
explícita. O nome self é uma convenção, assim como cls, podendo ser trocado  
por outro nome qualquer, porém é considerada como boa prática manter o  
nome.
Métodos de classe podem usar apenas atributos e outros métodos de classe. O 
argumento  cls representa a classe em si, precisa ser passado explicitamente  
como primeiro parâmetro do método.
Métodos estáticos são aqueles que não tem ligação com atributos do objeto ou 
da classe. Funcionam como as funções comuns.
Exemplo de classe:
# -*- coding: latin1 -*-
class Cell(object):
    """
    Classe para células de planilha
    """
    def __init__(self, formula='""', format='%s'):
        """

## Página 113

Classes 113
        Inicializa a célula
        """
        self.formula = formula
        self.format = format
    def __repr__(self):
        """
        Retorna a representação em string da célula
        """
        return self.format % eval(self.formula)
print Cell('123**2')
print Cell('23*2+2')
print Cell('abs(-1.45 / 0.3)', '%2.3f')
Saída:
15129
48
4.833
O método  __repr__() é usado internamente pelo comando  print para obter  
uma representação do objeto em forma de texto.
Em Python, não existem variáveis e métodos privados (que só podem ser  
acessados a partir do próprio objeto). Ao invés disso, é usada uma convenção, 
usar um nome que comece com sublinhado (_), deve ser considerado parte da  
implementação  interna  do  objeto  e  sujeito  a  mudanças  sem  aviso  prévio. 
Além  disso,  a  linguagem  oferece  uma  funcionalidade  chamada  Name 
Mangling,  que  acrescenta  na  frente  de  nomes  que  iniciam  com  dois  
sublinhados (__), um sublinhado e o nome da classe.
Exemplo:
# -*- coding: latin1 -*-

## Página 114

114 Classes
class Calc:
    def __init__(self, formula, **vars):
        self.formula = formula
        self.vars = vars
        self.__recalc()
    
    def __recalc(self):
        self.__res = eval(self.formula, self.vars)
    def __repr__(self):
        self.__recalc()
        return str(self.__res)
formula = '2*x + 3*y + z**2'
calc = Calc(formula, x=2, y=3, z=1)
print 'fórmula:', calc.formula
print 'x =', calc.vars['x'],'-> calc =', calc
calc.vars['x'] = 4
print 'x =', calc.vars['x'],'-> calc =', calc
print dir(calc)
Saída:
fórmula: 2*x + 3*y + z**2
x = 2 -> calc = 14
x = 4 -> calc = 18
['_Calc__recalc', '_Calc__res', '__doc__', '__init__', '__module__', '__repr__', 
'formula', 'vars']
O  método  __recalc() aparece  como  _Calc__recalc() e  o  atributo  __res como  
_Calc__res para fora do objeto.
Classes abertas
No Python, as classes que não são builtins podem ser alteradas em tempo de  
execução, devido a natureza dinâmica da linguagem. É possível acrescentar  

## Página 115

Classes 115
métodos  e  atributos  novos,  por  exemplo.  A  mesma  lógica  se  aplica  aos  
objetos.
Exemplo de como acrescentar um novo método:
# -*- coding: latin1 -*-
class User(object):
    """Uma classe bem simples.
    """
    def __init__(self, name):
        """Inicializa a classe, atribuindo um nome
        """
        self.name = name
# Um novo método para a classe
def set_password(self, password):
    """Troca a senha
    """
    self.password = password
print 'Classe original:', dir(User)
# O novo método é inserido na classe
User.set_password = set_password
print 'Classe modificada:', dir(User)
user = User('guest')
user.set_password('guest')
print 'Objeto:', dir(user)
print 'Senha:', user.password
Saída:
Classe  original:  ['__class__',  '__delattr__',  '__dict__',  '__doc__',  
'__getattribute__',  '__hash__',  '__init__',  '__module__',  '__new__',  
'__reduce__',  '__reduce_ex__',  '__repr__',  '__setattr__',  '__str__',  
'__weakref__']
Classe  modificada:  ['__class__',  '__delattr__',  '__dict__',  '__doc__',  
'__getattribute__',  '__hash__',  '__init__',  '__module__',  '__new__',  
'__reduce__',  '__reduce_ex__',  '__repr__',  '__setattr__',  '__str__',  
'__weakref__', 'set_password']

## Página 116

116 Classes
Objeto: ['__class__', '__delattr__', '__dict__', '__doc__', '__getattribute__',  
'__hash__',  '__init__',  '__module__',  '__new__',  '__reduce__',  
'__reduce_ex__', '__repr__', '__setattr__', '__str__', '__weakref__', 'name',  
'password', 'set_password']
Senha: guest
A classe modificada passou a ter um novo método: set_password().

## Página 117

Herança simples 117
Herança simples
Herança é um mecanismo que a orientação a objeto provê, com objetivo de  
facilitar  o  reaproveitamento  de  código.  A  ideia  é  que  as  classes sejam  
construídas formando uma hierarquia.
A nova classe pode implementar novos métodos e atributos e herdar métodos 
e  atributos  da  classe  antiga  (que  também  pode  ter  herdado  de  classes  
anteriores),  porém  estes  métodos  e atributos  podem substituídos  na nova  
classe.
A forma comum de herança é chamada de herança simples, na qual a nova  
classe é derivada de apenas uma classe já existente, porém é possível criar  
várias classes derivadas, criando uma hierarquia de classes.
Para localizar os métodos e atributos, a hierarquia é seguida de baixo para  
cima, de forma similar a busca nos namespaces local e global.
Carnívoro
Peso, Altura, 
idade
Correr, Atacar, 
Comer
Canino
Peso, Altura, 
idade, Raça
Correr, Atacar, 
Comer, Latir
Suas 
características
O que ele pode 
fazer
Bandit
Peso, Altura, 
idade, Raça
Correr, Atacar, 
Comer, Latir
Classe para  
carnívoros.
Objeto para um 
canino.
Classe para 
caninos.

## Página 118

118 Herança simples
Exemplo de herança simples:
class Pendrive(object):
    def __init__(self, tamanho, interface='2.0'):
        self.tamanho = tamanho
        self.interface = interface
class MP3Player(Pendrive):
    def __init__(self, tamanho, interface='2.0', turner=False):
        self.turner = turner
        Pendrive.__init__(self, tamanho, interface)
mp3 = MP3Player(1024)
print '%s\n%s\n%s' % (mp3.tamanho, mp3.interface, mp3.turner)
Saída:
A classe MP3Player é derivada
da classe Pendrive.
A classe MP3Player é derivada
da classe Pendrive.
Classe Antiga
Métodos
Atributos
Classe Nova
Métodos
antigos
Métodos 
redefinidos
Métodos
novos
Atributos
antigos
Atributos 
redefinidos
Atributos
novos
class Nova(Antiga):
Redefinição e/ou criação de 
métodos e/ou atributos.

## Página 119

Herança simples 119
1024
2.0
False
A classe MP3Player herda de Pendrive o tamanho e a interface.

## Página 120

120 Herança múltipla
Herança múltipla
Na  herança  múltipla,  a  nova  classe  deriva  de  duas  ou  mais  classes já  
existentes.
Exemplo:
# -*- coding: latin1 -*-
class Terrestre(object):
    """
    Classe de veículos terrestres
    """
    se_move_em_terra = True
    def __init__(self, velocidade=100):
        """
        Inicializa o objeto
        """
        self.velocidade_em_terra = velocidade
class Aquatico(object):
    """
    Classe de veículos aquaticos
    """
    se_move_na_agua = True
    def __init__(self, velocidade=5):
        """
        Inicializa o objeto
        """
        self.velocidade_agua = velocidade
class Carro(Terrestre):
    """
    Classe de carros
    """
    rodas = 4
    def __init__(self, velocidade=120, pistoes=4):
        """
A classe Carro deriva de Terrestre .A classe Carro deriva de Terrestre .

## Página 121

Herança múltipla 121
        Inicializa o objeto
        """
        self.pistoes = pistoes
        Terrestre.__init__(self, velocidade=velocidade)
class Barco(Aquatico):
    """
    Classe de barcos
    """
    def __init__(self, velocidade=6, helices=1):
        """
        Inicializa o objeto
        """
        self.helices = helices
        Aquatico.__init__(self, velocidade=velocidade)
class Anfibio(Carro, Barco):
    """
    Classe de anfíbios
    """
    def __init__(self, velocidade_em_terra=80,
        velocidade_na_agua=4, pistoes=6, helices=2):
        """
        Inicializa o objeto
        """
        # É preciso evocar o __init__ de cada classe pai
        Carro.__init__(self, velocidade=velocidade_em_terra,
            pistoes=pistoes)
        Barco.__init__(self, velocidade=velocidade_na_agua,
            helices=helices)
novo_anfibio = Anfibio()
for atr in dir(novo_anfibio):
    # Se não for método especial:
    if not atr.startswith('__'):
        print atr, '=', getattr(novo_anfibio, atr)
Saída:
helices = 2
A classe Anfibio é derivada
de Carro e Barco.
A classe Anfibio é derivada
de Carro e Barco.
A classe Barco deriva de Aquatico.A classe Barco deriva de Aquatico.

## Página 122

122 Herança múltipla
pistoes = 6
rodas = 4
se_move_em_terra = True
se_move_na_agua = True
velocidade_agua = 4
velocidade_em_terra = 80
A diferença mais significativa em relação à herança simples é a ordem de  
resolução de métodos (em inglês, Method Resolution Order- MRO).
Nas classes old style, a resolução começa pela classe mais a esquerda e desce  
até o fim da hierarquia e depois passa para o ramo a direita.
Já nas classes new style, a resolução é feita a partir da esquerda, descendo até  
encontrar a classe em comum entre os caminhos dentro hierarquia. Quando é  
encontrada uma classe em comum, a procura passa para o caminho à direita.  
Ao esgotar os caminhos, o algoritmo prossegue para a classe em comum e  
repete o processo.
Na hierarquia de classes do exemplo, a MRO para a classe dos anfíbios será:
A
1
0
3
2
 4
5
Ordem de 
resolução
B
 C
D
 E
F
A
1
0
4
2
 5
3
B
 C
D
 E
F
Old 
style
New 
style

## Página 123

Herança múltipla 123
[<class '__main__.Anfibio'>,
<class '__main__.Carro'>,
<class '__main__.Terrestre'>,
<class '__main__.Barco'>,
<class '__main__.Aquatico'>,
<type 'object'>]
A herança múltipla é um recurso que gera muita controvérsia, pois seu uso  
pode tornar o projeto confuso e obscuro.

## Página 124

124 Propriedades
Propriedades
Propriedades (properties) são atributos calculados em tempo de execução. As  
propriedades são criadas através da função / decorador property.
O uso de propriedades permite:
▪ Validar a entrada do atributo.
▪ Criar atributos apenas de leitura.
▪ Simplificar o uso da classe24.
▪ Mudar  de  um  atributo  convencional  para  uma  propriedade  sem  a  
necessidade de alterar as aplicações que utilizam a classe.
Exemplo de código sem propriedades:
# get_*, set_*...
class Projetil(object):
    def __init__(self, alcance, tempo):
        self.alcance = alcance
        self.tempo = tempo
    def get_velocidade(self):
        return self.alcance / self.tempo
moab = Projetil(alcance=10000, tempo=60)
print moab.get_velocidade()
Saída:
166
Exemplo de propriedade através de decorador:
24 As propriedades disfarçam as funções get() e set() dos atributos.

## Página 125

Propriedades 125
# -*- coding: latin1 -*-
# Exemplo de property de leitura
class Projetil(object):
    def __init__(self, alcance, tempo):
        self.alcance = alcance
        self.tempo = tempo
    @property
    def velocidade(self):
        return self.alcance / self.tempo
moab = Projetil(alcance=10000, tempo=60)
# A velocidade é calculada
print moab.velocidade
Saída:
166
Exemplo de propriedade através de chamada de função:
# Property de leitura e escrita
class Projetil(object):
    def __init__(self, alcance, tempo):
        self.alcance = alcance
        self.tempo = tempo
    # Calcula a velocidade
    def getv(self):
        return self.alcance / self.tempo

## Página 126

126 Propriedades
    # Calcula o tempo
    def setv(self, v):
        self.tempo = self.alcance / v
    # Define a propriedade
    velocidade = property(getv, setv)
moab = Projetil(alcance=10000, tempo=60)
print moab.velocidade
# Muda a velocidade
moab.velocidade = 350
print moab.tempo
Saída:
166
28
Propriedades  são  particularmente  interessantes  para  quem  desenvolve  
bibliotecas para serem usadas por outras pessoas.

## Página 127

Sobrecarga de operadores 127
Sobrecarga de operadores
No  Python,  o  comportamento  dos  operadores  é  definido  por  métodos  
especiais, porém tais métodos só podem ser alterados nas classes abertas. Por 
convenção, os métodos especiais têm nomes que começam e terminam com  
“__”.
Lista de operadores e os métodos correspondentes:
Operador Método Operação
+ __add__ adição
- __sub__ subtração
* __mul__ multiplicação
/ __div__ divisão
// __floordiv__ divisão inteira
% __mod__ módulo
** __pow__ potência
+ __pos__ positivo
- __neg__ negativo
< __lt__ menor que
> __gt__ maior que
<= __le__ menor ou igual a
>= __ge__ maior ou igual a
== __eq__ Igual a
!= __ne__ diferente de
<< __lshift__ deslocamento para 
esquerda
>> __rshift__ deslocamento para 
direita
& __and__ e bit-a-bit
| __or__ ou bit-a-bit
^ __xor__ ou exclusivo bit-a-bit
~ __inv__ inversão
Exemplo:

## Página 128

128 Sobrecarga de operadores
# A classe String deriva de str
class String(str):
    def __sub__(self, s):
            return self.replace(s, '')
s1 = String('The Lamb Lies Down On Broadway')
s2 = 'Down '
print '"%s" - "%s" = "%s"' % (s1, s2, s1 - s2)
Saída:
"The  Lamb  Lies  Down  On  Broadway"  -  "Down  "  =  "The  Lamb  Lies  On  
Broadway"
Observações:
▪ A subtração definida no código não é comutativa (da mesma forma que 
a adição em strings também não é)
▪ A  classe  str não  é  aberta,  portanto  não  é  possível  alterar  o  
comportamento da  string padrão do Python. Porém a classe  String é  
aberta.
▪ A redefinição de operadores conhecidos pode dificultar a leitura do  
código.
Coleções
Além de métodos especiais para objetos escalares, existem também métodos  
especiais para lidar com objetos que funcionam como coleções (da mesma  
forma que as listas e os dicionários), possibilitando o acesso aos itens que  
fazem parte da coleção.
Exemplo:
# -*- coding: latin1 -*-

## Página 129

Sobrecarga de operadores 129
class Mat(object):
    """
    Matriz esparsa
    """
    def __init__(self):
        """
        Inicia a matriz
        """
        self.itens = []
        self.default = 0
    def __getitem__(self, xy):
        """
        Retorna o item para X e Y ou default caso contrário
        """
        i = self.index(xy)
        if i is None:
            return self.default
        return self.itens[i][-1]
    def __setitem__(self, xy, data=0):
        """
        Cria novo item na matriz
        """
        i = self.index(xy)
        if not i is None:
            self.itens.pop(i)
        self.itens.append((xy, data))
    def __delitem__(self, xy):
        """
        Remove um item da matriz
        """
        i = self.index(xy)
        if i is None:
            return self.default
        return self.itens.pop(i)
    def __getslice__(self, x1, x2):
        """

## Página 130

130 Sobrecarga de operadores
        Seleciona linhas da matriz
        """
        r = []
        for x in xrange(x1, x2 + 1):
            r.append(self.row(x))
        return r
    def index(self, xy):
        i = 0
        for item in self.itens:
            if xy == item[0]:
                return i
            i += 1
        else:
            return None
    def dim(self):
        """
        Retorna as dimensões atuais da matriz
        """
        x = y = 0
        for xy, data in self.itens:
            if xy[0] > x: x = xy[0]
            if xy[1] > y: y = xy[1]
        return x, y
    def keys(self):
        """
        Retorna as coordenadas preenchidas
        """
        return [xy for xy, data in self.itens]
    def values(self):
        """
        Retorna os valores preenchidos
        """
        return [data for xy, data in self.itens]
    def row(self, x):
        """

## Página 131

Sobrecarga de operadores 131
        Retorna a linha especificada
        """
        X, Y = self.dim()
        r = []
        for y in xrange(1, Y + 1):
            r.append(self[x,y])
        return r
    def col(self, y):
        """
        Retorna a coluna especificada
        """
        X, Y = self.dim()
        r = []
        for x in xrange(1, X + 1):
            r.append(self[x,y])
        return r
    def sum(self):
        """
        Calcula o somatório
        """
        return sum(self.values())
    def avg(self):
        """
        Calcula a média
        """
        X, Y = self.dim()
        return self.sum() / (X * Y)
    def __repr__(self):
        """
        Retorna uma representação do objeto como texto
        """
        r = 'Dim: %s\n' % repr(self.dim())
        X, Y = self.dim()
        for x in xrange(1, X + 1):
            for y in xrange(1, Y + 1):
                r += ' %s = %3.1f' % (repr((x, y)),

## Página 132

132 Sobrecarga de operadores
                    float(self.__getitem__((x, y))))
            r += '\n'
        return r
if __name__ == '__main__':
    mat = Mat()
    print '2 itens preenchidos:'
    mat[1, 2] = 3.14
    mat[3, 4] = 4.5
    print mat
    print 'Troca e remoção:'
    del mat[3, 4]
    mat[1, 2] = 5.4
    print mat
    print 'Preenchendo a 3ª coluna:'
    for i in xrange(1, 4):
        mat[i + 1, 3] = i
    print mat
    print '3ª coluna:', mat.col(3)
    print 'Fatia com 2ª a 3ª linha', mat[2:3]
    print 'Somatório:', mat.sum(), 'Média', mat.avg()
Saída:
2 itens preenchidos:
Dim: (3, 4)
 (1, 1) = 0.0 (1, 2) = 3.1 (1, 3) = 0.0 (1, 4) = 0.0
 (2, 1) = 0.0 (2, 2) = 0.0 (2, 3) = 0.0 (2, 4) = 0.0
 (3, 1) = 0.0 (3, 2) = 0.0 (3, 3) = 0.0 (3, 4) = 4.5
Troca e remoção:
Dim: (1, 2)
 (1, 1) = 0.0 (1, 2) = 5.4
Preenchendo a 3ª coluna:
Dim: (4, 3)
 (1, 1) = 0.0 (1, 2) = 5.4 (1, 3) = 0.0
 (2, 1) = 0.0 (2, 2) = 0.0 (2, 3) = 1.0
 (3, 1) = 0.0 (3, 2) = 0.0 (3, 3) = 2.0
 (4, 1) = 0.0 (4, 2) = 0.0 (4, 3) = 3.0

## Página 133

Sobrecarga de operadores 133
3ª coluna: [0, 1, 2, 3]
Fatia com 2ª a 3ª linha [[0, 0, 1], [0, 0, 2]]
Somatório: 11.4 Média 0.95
A matriz esparsa cresce ou diminui conforme os índices dos elementos.

## Página 134

134 Metaclasses
Metaclasses
Em uma linguagem orientada a objeto aonde (quase) tudo são objetos e todo  
o objeto tem uma classe, é natural que as classes também sejam tratadas como 
objetos.
Metaclasse  é  uma  classe  cujas  as  instâncias  são  classes,  sendo  assim,  a  
metaclasse define o comportamento das  classes derivadas a partir dela. Em  
Python, a classe  type é uma metaclasse e pode ser usada para criar novas  
metaclasses.
Exemplo de metaclasse criada a partir de type:
# -*- coding: latin1 -*-
class Singleton(type):
    """
    Metaclasse Singleton
    """
    def __init__(cls, name, bases, dic):
        type.__init__(cls, name, bases, dic)
        # Retorna o próprio objeto na cópia
        def __copy__(self):
            return self
        # Retorna o próprio objeto na cópia recursiva
        def __deepcopy__(self, memo=None):
            return self
        cls.__copy__ = __copy__
        cls.__deepcopy__ = __deepcopy__
    def __call__(cls, *args, **kwargs):
        # Chamada que cria novos objetos,
        # aqui retorna sempre o mesmo
        try:
            return cls.__instance

## Página 135

Metaclasses 135
        # Se __instance não existir, então crie...
        except AttributeError:
            # A função super() pesquisa na MRO
            # a partir de Singleton
            cls.__instance = super(Singleton,
                cls).__call__(*args, **kwargs)
            return cls.__instance
import MySQLdb
class Con(object):
    """
    Classe de conexão única
    """
    # Define a metaclasse desta classe
    __metaclass__ = Singleton
    def __init__(self):
        # Cria uma conexão e um cursor
        con = MySQLdb.connect(user='root')
        self.db = con.cursor()
        # Sempre será usado o mesmo
        # objeto de cursor
class Log(object):
    """
    Classe de log
    """
    # Define a metaclasse desta classe
    __metaclass__ = Singleton
    def __init__(self):
        # Abre o arquivo de log para escrita
        self.log = file('msg.log', 'w')
        # Sempre será usado o mesmo
        # objeto de arquivo
    def write(self, msg):

## Página 136

136 Metaclasses
        print msg
        # Acrescenta as mensagens no arquivo
        self.log.write(str(msg) + '\n')
# Conexão 1
con1 = Con()
Log().write('con1 id = %d' % id(con1))
con1.db.execute('show processlist')
Log().write(con1.db.fetchall())
# Conexão 2
con2 = Con()
Log().write('con2 id = %d' % id(con2))
con2.db.execute('show processlist')
Log().write(con2.db.fetchall())
import copy
# Conexão 3
con3 = copy.copy(con1)
Log().write('con3 id = %d' % id(con3))
con3.db.execute('show processlist')
Log().write(con2.db.fetchall())
Saída e conteúdo do arquivo “msg.log”:
con1 id = 10321264
((20L, 'root', 'localhost:1125', None, 'Query', 0L, None, 'show processlist'),)
con2 id = 10321264
((20L, 'root', 'localhost:1125', None, 'Query', 0L, None, 'show processlist'),)
con3 id = 10321264
((20L, 'root', 'localhost:1125', None, 'Query', 0L, None, 'show processlist'),)
Com isso, todas as referências apontam para o mesmo objeto, e o recurso (a  
conexão de banco de dados) é reaproveitado.
Classes base abstratas
A partir da versão 2.6, o Python passou a suportar Abstract Base Classes , que 
são  metaclasses  que  permitem  forçar  a  implementação  de  determinados  
métodos e atributos das classes e subclasses derivadas.

## Página 137

Metaclasses 137
O módulo abc define a metaclasse ABCMeta e os decoradores abstractmethod e 
abstractproperty que identificam os métodos e propriedades que devem ser  
implementadas.
# -*- coding: latin1 -*-
from abc import ABCMeta, abstractmethod
class Nave(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def mover(self, x0, x1, v):
        # Sem implementação
        pass
class Zeppelin(Nave):
    def mover(self, x0, x1, v):
        """
        A partir da posição inicial e final e da velocidade
        calcula o tempo da viagem
        """
        d = x1 - x0
        t = v * d
        return t
class Hovercraft(Nave):
    # Esta classe não implementa o método mover()
    pass
z = Zeppelin()
# Objeto que não implementa o método abstrato
# Isso causa uma exceção TypeError
h = Hovercraft()
Saída:

## Página 138

138 Metaclasses
Traceback (most recent call last):
  File "ab01.py", line 38, in <module>
    h = Hovercraft()
TypeError: Can't instantiate abstract class Hovercraft with abstract methods  
mover
A avaliação da existência dos métodos abstratos ocorre durante o processo de  
criação  de  objetos  a  partir  da  classe,  porém  esta  não  leva  em  conta  os  
parâmetros dos métodos.

## Página 139

Decoradores de classe 139
Decoradores de classe
A partir da versão 2.6, os decoradores podem ser aplicados em classes.
Exemplo:
# -*- coding: latin1 -*-
import time
def logger(cls):
    """
    Função decoradora de classes
    """
    class Logged(cls):
        """
        Classe derivada que mostra os parâmetros de inicialização
        """
        def __init__(self, *args, **kargs):
            print 'Hora:', time.asctime()
            print 'Classe:', repr(cls)
            print 'args:', args
            print 'kargs:', kargs
            
            # Executa a inicialização da classe antiga
            cls.__init__(self, *args, **kargs)
    # Retorna a nova classe
    return Logged
@logger
class Musica(object):
    def __init__(self, nome, artista, album):
        self.nome = nome
        self.artista = artista
        self.album = album
m = Musica('Hand of Doom', 'Black Sabbath', album='Paranoid')

## Página 140

140 Decoradores de classe
Saída:
Hora: Mon Jan 04 23:59:14 2010
Classe: <class '__main__.Musica'>
args: ('Hand of Doom', 'Black Sabbath')
kargs: {'album': 'Paranoid'}
Com isso, o decorador mudou o comportamento da classe.

## Página 141

Testes automatizados 141
Testes automatizados
A atividade de testar software é uma tarefa repetitiva, demorada e tediosa.  
Por isso, surgiram várias ferramentas para automatizar testes. Existem dois  
módulos  para  testes  automatizados que  acompanham  o  Python:  doctest e  
unittest.
O  módulo  doctest usa  as  Doc  Strings que  estão  presentes  no  código  para  
definir os testes do código. A função  testmod() do  doctest procura por um  
trecho de texto seja semelhante a uma sessão interativa de Python, executa a  
mesma sequência de comandos, analisa a saída e faz um relatório dos testes  
que falharam, com os erros encontrados.
Exemplo:
"""
fib.py
Implementa Fibonacci.
"""
def fib(n):
    """Fibonacci:
    Se n <= 1, fib(n) = 1
    Se n > 1, fib(n) = fib(n - 1) + fib(n - 2)
    
    Exemplos de uso:
    
    >>> fib(0)
    1
    >>> fib(1)
    1
    >>> fib(10)
    89
    >>> [ fib(x) for x in xrange(10) ]
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    >>> fib('')
    Traceback (most recent call last):
      File "<input>", line 1, in ?
      File "<input>", line 19, in fib
    TypeError
    >>> 
Testes definidos para o doctest.Testes definidos para o doctest.

## Página 142

142 Testes automatizados
    """
    if not type(n) is int:
        raise TypeError
    if n > 1:
        return fib(n - 1) + fib(n - 2)
    else:
        return 1
def _doctest():
    """
    Evoca o doctest.
    """
    import doctest
    doctest.testmod()
if __name__ == "__main__":
    _doctest()
Se todos os testes forem bem sucedidos, não haverá relatório dos testes.
Exemplo  de  relatório  de  erros  dos  testes  (a  Doc  String  foi  alterada  de  
propósito para gerar um erro):
*************************************************************
File "fib.py", line 18, in __main__.fib
Failed example:
    fib(10)
Expected:
    89
Got:
    100
*************************************************************
1 items had failures:
   1 of   5 in __main__.fib
***Test Failed*** 1 failures.
Usando o módulo unittest, os testes são criados através de uma subclasse da  
classe  unittest.TestCase. Os testes são definidos como métodos da subclasse.  
Os métodos precisam ter seus nomes iniciando com “test” para que sejam  
identificados como rotinas de teste.
Os testes serão executados se este módulo 
for evocado diretamente pelo Python.
Os testes serão executados se este módulo 
for evocado diretamente pelo Python.

## Página 143

Testes automatizados 143
Os métodos de teste devem evocar ao terminar um dos métodos:
▪ assert_: verifica se uma condição é atingida.
▪ assertEqual: verifica se o resultado é igual ao parâmetro passado.
▪ AssertRaises: verifica se a exceção é a esperada.
Se houver  um método chamado s etUp, este  será executado  antes de cada  
teste,  assim  é  possível  reinicializar  variáveis  e  garantir  que  um  teste  não 
prejudique  o  outro.  O  final  dos  testes,  o  unittest gera  o  relatório  com  os  
resultados encontrados.
Exemplo:
"""
fibtest.py
Usa unittest para testar fib.py.
"""
import fib
import unittest
class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)
    def test0(self):
        self.assertEqual(fib.fib(0), 1)
    def test1(self):
        self.assertEqual(fib.fib(1), 1)
    def test10(self):
        self.assertEqual(fib.fib(10), 89)
    def testseq(self):
        fibs = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        
        for x, y in zip(fibs, [ fib.fib(x) for x in self.seq ]):
            self.assert_(x is y)
    def testtype(self):
Métodos que definem os testes.Métodos que definem os testes.

## Página 144

144 Testes automatizados
        self.assertRaises(TypeError, fib.fib, '')
if __name__ == '__main__':
    
    unittest.main()
Saída:
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s
OK
Exemplo de relatório com erros:
..F..
================================================
======================
FAIL: test10 (__main__.TestSequenceFunctions)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "unittest1.py", line 22, in test10
    self.assertEqual(fib.fib(10), 89)
AssertionError: 100 != 89
----------------------------------------------------------------------
Ran 5 tests in 0.000s
FAILED (failures=1)
No relatório, o terceiro teste falhou, pois “fib.fib(10)” retornou 100 ao invés de 
89, como seria o esperado.
O  unittest oferece  uma  solução  muito  semelhante  a  bibliotecas  de  testes  
implementadas em outras linguagens, enquanto o  doctest é mais simples de  
usar e se integra  bem com a documentação (as sessões do  doctest podem  
servir como exemplos de uso).

## Página 145

Exercícios IV 145
Exercícios IV
1. Crie uma classe que modele um quadrado, com um atributo lado e os  
métodos: mudar valor do lado, retornar valor do lado e calcular área.
2. Crie uma classe derivada de lista com um método retorne os elementos da  
lista sem repetição.
3. Implemente uma classe Carro com as seguintes propriedades:
▪ Um veículo tem um certo consumo de combustível (medidos em km /  
litro) e uma certa quantidade de combustível no tanque.
▪ O consumo é especificado no construtor e o nível de combustível inicial 
é 0.
▪ Forneça um método mover(km) que receba a distância em quilômetros e  
reduza o nível de combustível no tanque de gasolina.
▪ Forneça  um  método  gasolina(),  que  retorna  o  nível  atual  de  
combustível.
▪ Forneça um método abastecer(litros), para abastecer o tanque.
4. Implementar uma classe Vetor:
▪ Com coordenadas x, y e z.
▪ Que suporte soma, subtração, produto escalar e produto vetorial.
▪ Que calcule o módulo (valor absoluto) do vetor.
5. Implemente um módulo com:
▪ Uma classe Ponto, com coordenadas x, y e z.
▪ Uma classe Linha, com dois pontos A e B, e que calcule o comprimento  
da linha.
▪ Uma  classe  Triangulo,  com  dois  pontos  A,  B  e  C,  que  calcule  o  
comprimento dos lados e a área.

## Página 146

146 Parte V
Parte V
Esta parte cobre diversas tecnologias que os aplicativos hoje tem a disposição:  
principalmente para lidar com armazenamento e troca de informações: acesso 
a banco de dados, persistência, XML e Web. Além desses tópicos, temos o uso  
de threads e a arquitetura MVC.
Conteúdo:
▪ Threads  .
▪ Persistência  .
▪ XML  .
▪ Banco de dados  .
▪ Web  .
▪ MVC  .
▪ Exercícios V  .

## Página 147

Threads 147
Threads
Uma thread é uma linha de execução que compartilha sua área de memória  
com outras linhas, ao contrário do processo tradicional, que possui apenas  
uma linha com área de memória própria.
O  uso  de  threads oferece  algumas  vantagens  em  relação  aos  processos  
convencionais:
▪ Consomem menos recursos de máquina.
▪ Podem ser criadas e destruídas mais rapidamente.
▪ Podem ser chaveadas mais rapidamente.
▪ Podem se comunicar com outras threads de forma mais fácil.
É comum utilizar threads para:
▪ Processamento paralelo, em casos como atender várias conexões em  
processos servidores.
▪ Executar  operações  de  I/O  assíncronas,  por  exemplo:  enquanto  o  
usuário  continua  interagindo  com  a  interface  enquanto  a  aplicação  
envia um documento para a impressora.
Processo
Thread 1
Thread 2
Thread 3
Thread 1
Tempo
Thread 4

## Página 148

148 Threads
▪ Operações de I/O em paralelo.
Em Python, o módulo da biblioteca padrão  threading provê classes de alto  
nível de abstração e usa o módulo thread, que implementa as rotinas de baixo  
nível e geralmente não é usado diretamente.
Exemplo com o módulo threading:
# -*- coding: latin1 -*-
"""
Exemplo de uso de threads
"""
import os
import time
import threading
class Monitor(threading.Thread):
    """
    Classe de monitoramento usando threads
    """
    def __init__(self, ip):
        """
        Construtor da thread
        """
        # Atributos para a thread
        self.ip = ip
        self.status = None
        # Inicializador da classe Thread
        threading.Thread.__init__(self)
    def run(self):
        """
        Código que será executado pela thread
        """
        # Execute o ping
        ping = os.popen('ping -n 1 %s' % self.ip).read()
        if 'Esgotado' in ping:
            self.status = False
        else:
            self.status = True

## Página 149

Threads 149
if __name__ == '__main__':
    # Crie uma lista com um objeto de thread para cada IP
    monitores = []
    for i in range(1, 11):
        ip = '10.10.10.%d' % i
        monitores.append(Monitor(ip))
    # Execute as Threads
    for monitor in monitores:
        monitor.start()
    # A thread principal continua enquanto
    # as outras threads executam o ping
    # para os endereços da lista
    # Verifique a cada segundo
    # se as threads acabaram
    ping = True
    while ping:
        ping = False
        for monitor in monitores:
            if monitor.status == None:
                ping = True
                break
            
        time.sleep(1)
    # Imprima os resultados no final
    for monitor in monitores:
        if monitor.status:
            print '%s no ar' % monitor.ip
        else:
            print '%s fora do ar' % monitor.ip
Saída:
10.10.10.1 no ar
10.10.10.2 no ar
10.10.10.3 no ar

## Página 150

150 Threads
10.10.10.4 fora do ar
10.10.10.5 no ar
10.10.10.6 fora do ar
10.10.10.7 no ar
10.10.10.8 no ar
10.10.10.9 no ar
10.10.10.10 no ar
É importante observar que, quando o processo morre, todas as suas  threads 
terminam.
Na  versão  2.6,  está  disponível  também  o  módulo  multiprocessing,  que  
implementa classes para a criação de processos e a comunicação entre eles.

## Página 151

Persistência 151
Persistência
Persistência pode  ser  definida  como  a  manutenção  do  estado  de  uma  
estrutura de dados entre execuções de uma aplicação. A persistência libera o  
desenvolvedor de escrever código explicitamente para armazenar e recuperar  
estruturas  de  dados  em  arquivos  e  ajuda  a  manter  o  foco  na  lógica  da  
aplicação.
Serialização
A forma mais simples e direta de persistência é chamada de serialização25 e 
consiste em gravar em disco uma imagem ( dump) do objeto, que pode ser  
recarregada (load) posteriormente. No Python, a serialização é implementada  
de várias formas, sendo que a mais comum é através do módulo chamado  
pickle.
Exemplo de serialização:
▪ O  programa  tenta  recuperar  o  dicionário  setup usando  o  objeto  do  
arquivo “setup.pkl”.
▪ Se conseguir, imprime o dicionário.
▪ Se não conseguir, cria um setup default e salva em “setup.pkl”.
import pickle
try:
    setup = pickle.load(file('setup.pkl'))
    print setup
except:
    setup = {'timeout': 10,
        'server': '10.0.0.1',
        'port': 80
        }
    pickle.dump(setup, file('setup.pkl', 'w'))
Na primeira execução, ele cria o arquivo. Nas posteriores, a saída é:
25 Em inglês, serialization ou marshalling.

## Página 152

152 Persistência
{'port': 80, 'timeout': 10, 'server': '10.0.0.1'}
Entre  os  módulos  da  biblioteca  padrão  estão  disponíveis  outros  módulos 
persistência, tais como:
▪ cPickle: versão mais eficiente de pickle, porém não pode ter subclasses.
▪ shelve:  fornece  uma  classe  de  objetos  persistentes  similares  ao  
dicionário.
Existem  frameworks em  Python  de  terceiros  que  oferecem  formas  de  
persistência com recursos mais avançados, como o ZODB.
Todas essas formas de  persistência armazenam dados em formas binárias,  
que não são diretamente legíveis por seres humanos.
Para armazenar dados em forma de texto, existem módulos para Python para  
ler e gravar estruturas de dados em formatos:
▪ JSON26 (JavaScript Object Notation).
▪ YAML27 (YAML Ain't a Markup Language).
▪ XML28 (Extensible Markup Language).
ZODB
Zope Object Database  ( ZODB) é um  banco de dados  orientado a objeto que  
oferece uma forma de persistência quase transparente para aplicações escritas 
em Python e foi projetado para ter pouco impacto no código da aplicação.
ZODB suporta transações, controle de versão de objetos e pode ser conectado  
a  outros  backends através  do  Zope  Enterprise  Objects  (ZEO),  permitindo  
inclusive  a  criação  de  aplicações  distribuídas  em  diversas  máquinas  
conectadas por rede.
O  ZODB é  um  componente  integrante  do  Zope 29,  que  é  um  servidor  de 
26 Página do formato em: http://www.json.org/.
27 Página do formato em: http://yaml.org/.
28 Página do formato em: http://www.w3.org/XML/.
29 Documentação  e  pacotes  de  instalação  do  Zope  e  produtos  ligados  a  ele  em  
http://www.zope.org/.

## Página 153

Persistência 153
aplicações desenvolvido em Python, muito usado em  Content Management  
Systems (CMS).
Componentes do ZODB:
▪ Database: permite que a aplicação faça conexões (interfaces para acesso  
aos objetos).
▪ Transaction: interface que permite tornar as alterações permanentes.
▪ Persistence : fornece a classe base Persistent.
▪ Storage: gerencia a representação persistente em disco.
▪ ZEO:  compartilhamento  de  objeto  entre  diferentes  processos  e  
máquinas.
Exemplo de uso do ZODB:
# -*- coding: latin1 -*-
from ZODB import FileStorage, DB
import transaction
# Definindo o armazenamento do banco
Aplicação 
persistente
ZODB
ZODB: Zope Object Database
Database
 Transaction
Persistence
Storage
ZEO

## Página 154

154 Persistência
storage = FileStorage.FileStorage('people.fs')
db = DB(storage)
# Conectando
conn = db.open()
# Referência para a raiz da árvore
root = conn.root()
# Um registro persistente
root['singer'] = 'Kate Bush'
# Efetuando a alteração
transaction.commit()
print root['singer'] # Kate Bush
# Mudando um item
root['singer'] = 'Tori Amos'
print root['singer'] # Tori Amos
# Abortando...
transaction.abort()
# O item voltou ao que era antes da transação
print root['singer'] # Kate Bush
O ZODB tem algumas limitações que devem ser levadas em conta durante o  
projeto da aplicação:
▪ Os objetos precisam ser “serializáveis” para serem armazenados.
▪ Objetos mutáveis requerem cuidados especiais.
Objetos  “serializáveis”  são  aqueles  objetos  que  podem  ser  convertidos  e  
recuperados pelo  Pickle. Entres os objetos que não podem ser processados  
pelo  Pickle,  estão  aqueles  implementados  em  módulos  escritos  em C,  por  
exemplo.
YAML
YAML é um formato de  serialização de dados para texto que representa os  
dados como combinações de listas, dicionários e valores escalares. Tem como  
principal característica ser legível por humanos.

## Página 155

Persistência 155
O projeto do YAML foi muito influenciado pela sintaxe do Python e outras  
linguagens  dinâmicas.  Entre  outras  estruturas,  a especificação 30 do YAML  
define que:
▪ Os blocos são marcados por endentação.
▪ Listas são delimitadas por colchetes ou indicadas por traço.
▪ Chaves de dicionário são seguidas de dois pontos.
Listas podem ser representadas assim:
- Azul
- Branco
- Vermelho
Ou:
[azul, branco, vermelho]
Dicionários são representados como:
cor: Branco
nome: Bandit
raca: Labrador
PyYAML31 é um módulo de rotinas para gerar e processar YAML no Python.
Exemplo de conversão para YAML:
import yaml
progs = {'Inglaterra':
            {'Yes': ['Close To The Edge', 'Fragile'],
            'Genesis': ['Foxtrot', 'The Nursery Crime'],
            'King Crimson': ['Red', 'Discipline']},
        'Alemanha':
            {'Kraftwerk': ['Radioactivity', 'Trans Europe Express']}
30 Disponível em: http://yaml.org/spec/1.2/.
31 Documentação e fontes em: http://pyyaml.org/wiki/PyYAML.

## Página 156

156 Persistência
        }
print yaml.dump(progs)
Saída:
Alemanha:
  Kraftwerk: [Radioactivity, Trans Europe Express]
Inglaterra:
  Genesis: [Foxtrot, The Nursery Crime]
  King Crimson: [Red, Discipline]
  'Yes': [Close To The Edge, Fragile]
Exemplo de leitura de YAML. Arquivo de entrada “prefs.yaml”:
- musica: rock
- cachorro:
   cor: Branco
   nome: Bandit
   raca: Labrador
- outros:
   instrumento: baixo
   linguagem: [python, ruby]
   comida: carne
Código em Python:
import pprint
import yaml
# yaml.load() pode receber um arquivo aberto
# como argumento
yml = yaml.load(file('prefs.yaml'))
# pprint.pprint() mostra a estrutura de dados
# de uma forma mais organizada do que
# o print convencional
pprint.pprint(yml)
Saída:

## Página 157

Persistência 157
[{'musica': 'rock'},
 {'cachorro': {'cor': 'Branco', 'nome': 'Bandit', 'raca': 'Labrador'}},
 {'outros': {'comida': 'carne',
             'instrumento': 'baixo',
             'linguagem': ['python', 'ruby']}}]
YAML é muito prático para ser usado em arquivos de configuração e outros  
casos onde os dados podem ser manipulados diretamente por pessoas.
JSON
A partir versão 2.6, foi incorporado a biblioteca do Python um módulo de  
suporte  ao  JSON ( JavaScript  Object  Notation).  O  formato  apresenta  muitas 
similaridades com o YAML e tem o mesmo propósito.
Exemplo:
import json
desktop = {'arquitetura': 'pc', 'cpus': 2, 'hds': [520, 270]}
print json.dumps(desktop)
Saída:
{"hds": [520, 270], "arquitetura": "pc", "cpus": 2}
O JSON usa a sintaxe do JavaScript para representar os dados e é suportado  
em várias linguagens.

## Página 158

158 XML
XML
XML32 ( eXtensible Markup Language ) é uma especificação, desenvolvida pelo  
World Wide Web Consortium33 (W3C), para uma representação de dados em que o  
metadado é armazenado junto com os dados através de marcadores (tags).
Em  termos  estruturais,  um  documento  XML representa  uma  hierarquia  
formada de elementos, que podem ter ou não atributos ou subelementos.
Características principais:
▪ É legível por software.
▪ Pode ser integrada com outras linguagens.
▪ Conteúdo e formato são entidades distintas.
▪ Marcadores podem ser criados sem limitação.
▪ Permite a criação de arquivos para validação de estrutura.
No exemplo, o elemento “Cachorro” possui três atributos: nome, raça e cor. O  
elemento Lobo tem dois subelementos (“Cachorro” e “Coiote”) e não possui  
32 Página oficial em http://www.w3.org/XML/.
33 Endereço na Internet: http://www.w3.org/.
Canino
Raposa
Cachorro
Lobo
Coiote
Nome: Bandit
Raça: Labrador
Cor: Branco
Atributos
Elementos
Raiz
Árvore de elementos

## Página 159

XML 159
atributos.
Em XML, o cachorro é representado por:
<Cachorro cor="Branco" nome="Bandit" raca="Labrador" />
E o lobo por:
<Lobo>    </Lobo>
Existem  vários  módulos  disponíveis  para  Python  com  suporte  ao  XML, 
inclusive na biblioteca que acompanha o interpretador.
Entre as APIs mais usados, destacam-se:
▪ DOM.
▪ SAX.
▪ ElementTree.
Cachorro
Nome: Bandit
Raça: Labrador
Cor: Branco
Atributos
Tag
Elemento
Lobo
<Cachorro cor="Branco" 
nome="Bandit" raca="Labrador" />
<Lobo>...</Lobo>

## Página 160

160 XML
DOM
Document Object Model  (DOM) é um modelo de objeto para representação de  
XML, independente de plataforma e linguagem. O  DOM foi projetado para  
permitir navegação não linear e modificações arbitrárias. Por isso, o  DOM 
exige que o documento XML (ou pelo menos parte dele) esteja carregado na  
memória.
Exemplo:
# -*- coding: latin1 -*-
# importa a implementação minidom
import xml.dom.minidom
# Cria o documento
doc = xml.dom.minidom.Document()
# Para ler um documento que já existe
# doc = xml.dom.minidom.parse('caninos.xml')
# Cria os elementos
root = doc.createElement('Canino')
lobo = doc.createElement('Lobo')
raposa = doc.createElement('Raposa')
coiote = doc.createElement('Coiote')
cachorro = doc.createElement('Cachorro')
# Cria os atributos
cachorro.setAttribute('nome', 'Bandit')
cachorro.setAttribute('raca', 'Labrador')
cachorro.setAttribute('cor', 'Branco')
# Cria a estrutura
doc.appendChild(root)
root.appendChild(lobo)
root.appendChild(raposa)
lobo.appendChild(coiote)
lobo.appendChild(cachorro)
# Para acrescentar texto ao elemento
# tex = doc.createTextNode('Melhor amigo do homem...')
# cachorro.appendChild(tex)
# Mostra o XML formatado

## Página 161

XML 161
print doc.toprettyxml()
Saída:
<?xml version="1.0" ?>
<Canino>
    <Lobo>
        <Coiote/>
        <Cachorro cor="Branco" nome="Bandit" raca="Labrador"/>
    </Lobo>
    <Raposa/>
</Canino>
O módulo minidom é uma implementação do DOM mais simples e que requer 
menos memória.
SAX
Simple API for  XML ( SAX) é uma API de análise sintática serial para  XML. 
SAX permite  apenas  a  leitura  serial  do  documento  XML.  SAX consome  
menos memória que o DOM, porém tem menos recursos.
Exemplo:
# -*- coding: latin1 -*-
import xml.sax
# A classe processa a árvore XML
class Handler(xml.sax.handler.ContentHandler):
    def __init__(self):
        xml.sax.handler.ContentHandler.__init__(self)
        self.prefixo = ''
    # É chamado quando uma novo tag é encontrada
    def startElement(self, tag, attr):
        self.prefixo += '  '

## Página 162

162 XML
        print self.prefixo + 'Elemento:', tag
        for item in attr.items():
            print self.prefixo + '- %s: %s' % item
    # É chamado quando texto é encontrado
    def characters(self, txt):
        if txt.strip():
            print self.prefixo + 'txt:', txt
    # É chamado quando o fim de uma tag é encontrada
    def endElement(self, name):
        self.prefixo = self.prefixo[:-2]
parser = xml.sax.make_parser()
parser.setContentHandler(Handler())
parser.parse('caninos.xml')
Saída:
  Elemento: Canino
    Elemento: Lobo
      Elemento: Coiote
      Elemento: Cachorro
      - cor: Branco
      - raca: Labrador
      - nome: Bandit
    Elemento: Raposa
Com o SAX não é necessário trazer o documento inteiro para a memória.
ElementTree
ElementTree é o mais “pythônico” dos três, representando uma estrutura XML 
como uma árvore de elementos, que são tratados de forma semelhante às  
listas, e nos quais os atributos são chaves, similar aos dicionários.
Exemplo de geração de XML com ElementTree:
from xml.etree.ElementTree import Element, ElementTree

## Página 163

XML 163
root = Element('Canino')
lobo = Element('Lobo')
raposa = Element('Raposa')
coiote = Element('Coiote')
cachorro = Element('Cachorro', nome='Bandit',
    raca='Labrador', cor='Branco')
root.append(lobo)
root.append(raposa)
lobo.append(coiote)
lobo.append(cachorro)
ElementTree(root).write('caninos.xml')
Arquivo XML de saída:
<Canino>
    <Lobo>
        <Coiote />
        <Cachorro cor="Branco" nome="Bandit" raca="Labrador" />
    </Lobo>
    <Raposa />
</Canino>
Exemplo de leitura do arquivo XML:
from xml.etree.ElementTree import ElementTree
tree = ElementTree(file='caninos.xml')
root = tree.getroot()
# Lista os elementos abaixo do root
print root.getchildren()
# Encontra o lobo
lobo = root.find('Lobo')
# Encontra o cachorro
cachorro = lobo.find('Cachorro')
print cachorro.tag, cachorro.attrib
# Remove a raposa

## Página 164

164 XML
root.remove(root.find('Raposa'))
print root.getchildren()
Saída:
[<Element Lobo at ab3a58>, <Element Raposa at ab3b70>]
Cachorro {'cor': 'Branco', 'raca': 'Labrador', 'nome': 'Bandit'}
[<Element Lobo at ab3a58>]
O XML é muito útil por facilitar a interoperabilidade entre sistemas, mesmo  
que estes sejam desenvolvidos em tecnologias diferentes.

## Página 165

Banco de dados 165
Banco de dados
Sistemas Gerenciadores de  Banco de Dados  (SGBDs) são reconhecidos por  
prover uma forma de acesso consistente e confiável para informações.
A maioria dos  SGDB atuais são baseados no modelo relacional, no qual as  
informações são representadas na forma de tabelas. Geralmente, estas tabelas  
podem ser consultadas através de uma linguagem especializada para isso,  
chamada SQL (Structured Query Language).
Geralmente, os SGBDs utilizam a arquitetura cliente-servidor. Os aplicativos  
usam  a  API  cliente  para  poder  se  comunicar  com  o  servidor,  que  é  o  
responsável por receber  as consultas dos clientes,  interpretar  as sentenças  
SQL e recuperar os dados com um tempo de resposta adequado.
Para fazer isso, o servidor precisa realizar uma série de outras tarefas, tais  
como: verificar credenciais, controlar o acesso, gerenciar conexões de rede,  
manter a integridade dos dados, otimizar as consultas e resolver questões de  
concorrência.
Servidor
Processo
Arquivos
Arquivos
Arquivos
Cliente
API Cliente
Aplicativo
Rede
Processo

## Página 166

166 Banco de dados
No Python, a integração com SGBDs é feita na maioria dos casos através de  
um módulo  DBI., que usa a API cliente para se comunicar com o banco de  
dados.
DBI
Database Interface  ( DBI) é uma especificação que descreve como deve ser o  
comportamento de um módulo de acesso a sistemas de banco de dados.
A DBI define que o módulo deve ter uma função connect(), retorna objetos de  
conexão. A partir do do objeto conexão, é possível obter um objeto cursor,  
que permite a execução de sentenças  SQL e a recuperação dos dados (uma  
lista de tuplas com os resultados, por default).
MySQL
O MySQL é um SGBD cliente-servidor reconhecido pelo bom desempenho e é 
bastante usado como backend para aplicações Web.
Interpretador
DBI
Programa
As consultas são sentenças SQL 
e as respostas são listas de 
tuplas ou dicionários.
SGBD
O módulo DBI (Database 
Interface) é um driver especifico 
para o SGBD.

## Página 167

Banco de dados 167
Exemplo de acesso através de DBI com MySQL34:
# -*- coding: utf-8 -*-
import MySQLdb
# Cria uma conexão
con = MySQLdb.connect(db='test', user='root', passwd='')
# Cria um cursor
cur = con.cursor()
# Executa um comando SQL
cur.execute('show databases')
# Recupera o resultado
recordset = cur.fetchall()
# Mostra o resultado
for record in recordset:
    print record
# Fecha a conexão
con.close()
Saída:
('information_schema',)
('mysql',)
('test',)
O resultado é composto por uma lista de tuplas com as databases disponíveis 
no servidor.
SQLite
A partir da versão 2.5, o Python passou a incorporar em sua distribuição um  
módulo DBI para acessar o SQLite35.
34 Binários,  fontes  e  documentação  podem  ser  encontrados  em:  
http://sourceforge.net/projects/mysql-python.
35 Documentação, fontes e binários podem ser encontrados em: http://www.sqlite.org/.

## Página 168

168 Banco de dados
SQLite é uma biblioteca Open Source escrita em linguagem C, que implementa 
um interpretador  SQL, e provê funcionalidades de  banco de dados , usando  
arquivos,  sem  a  necessidade  de  um  processo  servidor  separado  ou  de  
configuração manual.
Exemplo:
# -*- coding: utf-8 -*-
import sqlite3
# Cria uma conexão e um cursor
con = sqlite3.connect('emails.db')
cur = con.cursor()
# Cria uma tabela
sql = 'create table emails '\
    '(id integer primary key, '\
    'nome varchar(100), '\
    'email varchar(100))'
cur.execute(sql)
# sentença SQL para inserir registros
sql = 'insert into emails values (null, ?, ?)'
# Dados
recset = [('jane doe', 'jane@nowhere.org'),
    ('rock', 'rock@hardplace.com')]
# Insere os registros
for rec in recset:
    cur.execute(sql, rec)
# Confirma a transação
con.commit()
# Seleciona todos os registros
cur.execute('select * from emails')
# Recupera os resultados
recset = cur.fetchall()
# Mostra
for rec in recset:
    print '%d: %s(%s)' % rec

## Página 169

Banco de dados 169
# Fecha a conexão
con.close()
A  vantagem  mais  significativa  de  usar  o  SQLite  é  a  praticidade,  
principalmente no uso em aplicativos locais para  desktops, aonde usar um  
SGBD convencional seria desnecessário e complicado de manter.
Firebird
Firebird36 é  um  SGBD  cliente-servidor  leve,  porém  com  muitos  recursos.  
Programas em Python podem se comunicar com ele através do  driver DBI  
KInterbasDB37.
Exemplo:
# -*- coding: latin1 -*-
import kinterbasdb
#Para criar a base
# isql -u sysdba -p xXxXxXx
# create database '\temp\cds.fdb';
#
# conecta o Firebird
con = kinterbasdb.connect(dsn='localhost:/temp/cds.fdb',
    user='sysdba', password='xXxXxXx')
# Cria um objeto cursor
cur = con.cursor()
sql = "create table cds("\
"nome varchar(20),"\
"artista varchar(20),"\
"ano integer,"\
"faixas integer,"\
"primary key(nome, artista, ano));"
# Cria uma tabela
36 Disponível em: http://www.firebirdsql.org/.
37 Última versão: http://www.firebirdsql.org/index.php?op=devel&sub=python.

## Página 170

170 Banco de dados
cur.execute(sql)
# Grava as modificações
con.commit()
dados = [
    ('IV', 'Led Zeppelin', 1971, 8),
    ('Zenyattà Mondatta', 'The Police', 1980, 11),
    ('OK Computer', 'Radiohead', 1997, 12),
    ('In Absentia', 'Porcupine Tree', 2002, 12),
  ]
# Insere os registros e faz a interpolação
insert = "insert into cds"\
"(nome, artista, ano, faixas) values (?, ?, ?, ?)"
cur.executemany(insert, dados)
con.commit()
# Consulta os registros
cur.execute("select * from cds order by ano")
# Recupera os resuldados
for reg in cur.fetchall():
        # Formata e imprime
        print ' - '.join(str(i) for i in reg)
Saída:
IV - Led Zeppelin - 1971 – 8
Zenyattà Mondatta - The Police - 1980 – 11
OK Computer - Radiohead - 1997 – 12
In Absentia - Porcupine Tree - 2002 - 12
Como  o  Firebird não  requer  muita  potência  e  nem  muito  esforço  para  
administração,  ele  pode  ser  usado  tanto  como  servidor,  quanto  ser  
empacotado junto com um aplicativo desktop.
PostgreSQL
Para  sistemas  que  demandam  recursos  mais  sofisticados  do  SGBD,  o  
PostgreSQL38 é a solução Open Source mais completa disponível. O software  
38 Site  oficial  em  http://www.postgresql.org/ e  site  da  comunidade  brasileira  em  
http://www.postgresql.org.br/.

## Página 171

Banco de dados 171
segue a arquitetura cliente-servidor e é distribuído sob a licença BSD.
Entre os recursos oferecidos pelo PostgreSQL, destacam-se:
▪ Suporte a consultas complexas.
▪ Transações.
▪ Controle de concorrência multi-versão.
▪ Tipos de objetos definidos pelo usuário.
▪ Herança.
▪ Views.
▪ Stored Procedures.
▪ Triggers.
▪ Full text search.
Existem vários módulos que provêm acesso ao  PostgreSQL para o Python,  
como o PygreSQL39 e o Psycopg40.
O  PygreSQL  oferece  duas  interfaces  distintas  para  acesso  a  servidores  
PostgreSQL:
▪ pgdb: módulo compatível com DBI.
▪ pg: módulo mais antigo, incompatível com DBI.
Exemplo com pgdb:
# -*- coding: latin1 -*-
import pgdb
# Para bancos de dados locais (via Unix Domain Sockets)
#con = pgdb.connect(database='music')
# Via TCP/IP
con = pgdb.connect(host='tao', database='music', user='pg', 
password='#@!$%&')
cur = con.cursor()
# Cria uma tabela
sql = 'create table tracks '\
39 Site oficial: http://www.pygresql.org/.
40 Fontes e documentação em http://initd.org/.

## Página 172

172 Banco de dados
   '(id serial primary key, '\
   'track varchar(100), '\
   'band varchar(100))'
cur.execute(sql)
# A interpolação usa uma notação semelhante a do Python
sql = 'insert into tracks values (default, %s, %s)'
# Dados
recset = [('Kashmir', 'Led Zeppelin'),
   ('Starless', 'King Crimson')]
# Insere os registros
for rec in recset:
   cur.execute(sql, rec)
con.commit()
# Recupera os registros
cur.execute('select * from tracks')
# Recupera os resultados
recset = cur.fetchall()
# Mostra
for rec in recset:
   print rec
con.close()
Saída:
[1, 'Kashmir', 'Led Zeppelin']
[2, 'Starless', 'King Crimson']
Exemplo com pg:
import pg
# Para bancos de dados locais (via Unix Domain Sockets)
#con = pg.connect('music')
# Via TCP/IP
con = pg.connect(host='tao', dbname='music', user='pg', passwd='#@!$
%&')

## Página 173

Banco de dados 173
# Realiza uma consulta no banco
qry = con.query('select * from tracks')
# Pega a lista de campos
flds = qry.listfields()
# Mostra os resultados
for rec in qry.dictresult():
   for fld in flds:
       print '%s: %s' % (fld, rec[fld])
   print
con.close()
Saída:
id: 1
track: Kashmir
band: Led Zeppelin
id: 2
track: Starless
band: King Crimson
Exemplo usando o Psycopg:
import psycopg2
# Para bancos de dados locais (via Unix Domain Sockets)
#con = psycopg2.connect(database='music')
# Via TCP/IP
con = psycopg2.connect(host='tao', database='music',
   user='pg', password='#@!$%&')
cur = con.cursor()
sql = 'insert into tracks values (default, %s, %s)'
recset = [('Siberian Khatru', 'Yes'),
   ("Supper's Ready", 'Genesis')]
for rec in recset:
   cur.execute(sql, rec)
con.commit()

## Página 174

174 Banco de dados
cur.execute('select * from tracks')
recset = cur.fetchall()
for rec in recset:
   print rec
con.close()
Saída:
(1, 'Kashmir', 'Led Zeppelin')
(2, 'Starless', 'King Crimson')
(3, 'Siberian Khatru', 'Yes')
(4, "Supper's Ready", 'Genesis')
Como o módulo segue fielmente a especificação DBI, o código é praticamente  
igual  ao  exemplo  usando  o  módulo  pg.  O  Psycopg  foi  projetado  com  o  
objetivo  de  suportar  aplicações  mais  pesadas,  com  muitas  inserções  e  
atualizações.
Também é possível escrever funções para  PostgreSQL usando Python. Para  
que  isso  seja  possível,  é  preciso  habilitar  o  suporte  ao  Python  no  banco, 
através do utilitário de linha de comando pelo administrador:
createlang plpythonu <banco>
As linguagens que podem usadas pelo PostgreSQL são chamadas Procedural  
Languages (PL) e o sufixo “u” significa untrusted.
Os tipos dos parâmetros e do retorno da função devem ser definidos durante  
a criação da função no PostgreSQL.
Exemplo de função:
create function pformat(band text, track text)
  returns text
as $$

## Página 175

Banco de dados 175
  return '%s - %s' % (band, track)
$$ language plpythonu;
O código em Python foi marcado em verde.
Saída da função (através do psql):
music=> select pformat(track, band) from tracks;
         pformat         
-------------------------
 Kashmir - Led Zeppelin
 Starless - King Crimson
 Yes - Siberian Khatru
 Genesis - Supper's Ready
(4 registros)
O ambiente de execução de Python no  PostgreSQL provê o módulo plpy  
(importado automaticamente) que é uma abstração para o acesso aos recursos  
do SGBD.
Exemplo com plpy:
create function inibands()
  returns setof text
as $$
  bands = plpy.execute('select distinct band from tracks order by 1')
  return [''.join(filter(lambda c: c == c.upper(), list(band['band']))) for band  
in bands]
$$ language plpythonu;
Saída da função (através do utilitário psql):
music=> select inibands();
 inibands 
----------
 KC
 LZ
 Y
 G

## Página 176

176 Banco de dados
(4 registros)
Funções escritas em Python podem ser utilizadas tanto em Stored Procedures 
quanto Triggers no PostgreSQL.
Existem vários projetos  que ampliam os recursos  do PostgreSQL,  como o  
PostGis41,  que  provê  suporte  a  informações  espaciais,  usadas  em  GIS  
(Geographic Information Systems).
41 Site: http://postgis.refractions.net/.

## Página 177

Banco de dados 177
Mapeamento objeto-relacional
Object-Relational  Mapper ( ORM)  é  uma  camada  que  se  posiciona  entre  o  
código com a lógica da aplicação e o módulo DBI, com o objetivo de reduzir  
as dificuldades geradas pelas diferenças entre a representação de objetos (da  
linguagem) e a representação relacional (do banco de dados).
Com o uso de um ORM:
▪ A aplicação se torna independente do SGDB.
▪ O desenvolvedor não precisa usar SQL diretamente.
▪ A  lógica  para  gerenciamento  das  conexões  é  realizada  de  forma  
transparente pelo ORM.
Exemplo de ORM (com SQLAlchemy42):
# -*- coding: latin1 -*-
# Testado com SQLAlchemy 0.5.7
42 Documentação e fontes podem encontrados em: http://www.sqlalchemy.org/.
As consultas são métodos e as 
respostas são objetos.
SGBD
O módulo ORM desacopla a 
aplicação do SGBD.
Interpretador
ORM
Programa
DBI

## Página 178

178 Banco de dados
from sqlalchemy import *
# URL => driver://username:password@host:port/database
# No SQLite:
#   sqlite:// (memória)
#   sqlite:///arquivo (arquivo em disco)
db = create_engine('sqlite:///progs.db')
# Torna acessível os metadados
metadata = MetaData(db)
# Ecoa o que SQLAlchemy está fazendo
metadata.bind.echo = True
# Tabela Prog
prog_table = Table('progs', metadata,
    Column('prog_id', Integer, primary_key=True),
    Column('name', String(80)))
# Cria a tabela
prog_table.create()
# Carrega a definição da tabela
prog_table = Table('progs', metadata, autoload=True)
# Insere dados
i = prog_table.insert()
i.execute({'name': 'Yes'}, {'name': 'Genesis'},
    {'name': 'Pink Floyd'}, {'name': 'King Crimson'})
# Seleciona
s = prog_table.select()
r = s.execute()
for row in r.fetchall():
    print row
Saída:
2010-01-16 08:17:15,163 INFO sqlalchemy.engine.base.Engine.0x...af50 
CREATE TABLE progs (
prog_id INTEGER NOT NULL, 
name VARCHAR(80), 
PRIMARY KEY (prog_id)
)

## Página 179

Banco de dados 179
2010-01-16 08:17:15,163 INFO sqlalchemy.engine.base.Engine.0x...af50 ()
2010-01-16  08:17:15,272  INFO  sqlalchemy.engine.base.Engine.0x...af50  
COMMIT
2010-01-16  08:17:15,272  INFO  sqlalchemy.engine.base.Engine.0x...af50  
INSERT INTO progs (name) VALUES (?)
2010-01-16  08:17:15,272  INFO  sqlalchemy.engine.base.Engine.0x...af50  
[['Yes'], ['Genesis'], ['Pink Floyd'], ['King Crimson']]
2010-01-16  08:17:15,272  INFO  sqlalchemy.engine.base.Engine.0x...af50  
COMMIT
2010-01-16  08:17:15,365  INFO  sqlalchemy.engine.base.Engine.0x...af50  
SELECT progs.prog_id, progs.name 
FROM progs
2010-01-16 08:17:15,365 INFO sqlalchemy.engine.base.Engine.0x...af50 []
(1, u'Yes')
(2, u'Genesis')
(3, u'Pink Floyd')
(4, u'King Crimson')
Além  dos  SQLAlchemy,  também  existem  disponíveis  para  Python  o  
SQLObject43 e ORMs que integram frameworks maiores, como o Django.
43 Documentação e fontes disponíveis em: http://www.sqlobject.org/.

## Página 180

180 Web
Web
Uma  aplicação  Web é  uma  aplicação  cliente-servidor  aonde  o  cliente  é  o  
browser (como o Mozilla Firefox) e o protocolo utilizado para a comunicação  
com o servidor é chamado Hypertext Transfer Protocol (HTTP), tecnologias que 
servem de base para a World Wide Web (WWW), as páginas de hipertexto que  
fazem parte da internet . Tais páginas seguem as convenções da linguagem  
HyperText Markup Language44 (HTML).
As aplicações  Web geram as páginas HTML dinamicamente, atendendo as  
requisições enviadas pelo  browser. Se construídas da forma adequada, estas  
aplicações  podem  ser  acessadas  em  vários  ambientes  diferentes,  de  
computadores pessoais, até PDAs e celulares.
Existem muitos  frameworks para facilitar o desenvolvimento  de aplicativos  
Web em Python, entre eles, o CherryPy e o CherryTemplate.
44 Especificações em: http://www.w3.org/MarkUp/.
Servidor
Requisição GET
ou POST
Browser
HTTPd
Resposta
A Web dinâmica é uma forma de 
execução remota.
url?param=arg => url(param=arg)

## Página 181

Web 181
CherryPy
CherryPy45 é  um  framework para  aplicações  Web que  publica  objetos,  
convertendo URLs em chamadas para os métodos dos objetos publicados.  
Com o CherryPy, o programa passa a se comportar como um servidor Web, 
respondendo a requisições GET e POST.
Exemplo com CherryPy:
import cherrypy
class Root(object):
    @cherrypy.expose
    def index(self):
        return 'Hello World!'
cherrypy.quickstart(Root())
O decorador @expose indica quais métodos são publicados via Web. O retorno 
do método é uma string, que é enviada para o browser.
O endereço padrão do servidor é “http://localhost:8080/”.
CherryTemplate
CherryTemplate46 é  um  módulo  de  processamento  de  modelos  ( templates) 
para Python. Era parte integrante do CherryPy, mas hoje é distribuído como  
um pacote separado.
Marcadores disponíveis no CherryTemplate:
▪ py-eval: avalia uma expressão em Python e insere o resultado (que deve  
ser uma string) no texto.
45 Documentação e fontes podem ser encontrados em: http://www.cherrypy.org/.
46 Documentação  e  fontes  podem  ser  encontrados  em:  http://cherrytemplate.python-
hosting.com/.

## Página 182

182 Web
Exemplo:
Somatório de 1 a 10 é <py-eval="str(sum(range(1, 11)))">
▪ py-exec: executa uma linha de código Python.
Exemplo:
<py-exec="import platform">
O sistema é <py-eval="platform.platform()">
▪ py-code: executa um bloco de código Python.
Exemplo:
<py-code="
import platform
sistema = platform.platform()
">
<py-eval="sistema">
▪ py-if / py-else: funciona como o par if / else em Python.
Exemplo:
<py-if="1 > 10">
    Algo errado...
</py-if><py-else>
    Correto!
</py-else>
▪ py-for: funciona como o laço for em Python.
Exemplo:
<py-for="x in range(1, 11)">

## Página 183

Web 183
    <py-eval="str(x)"> ** 2 = <py-eval="str(x ** 2)"><br>
</py-for>
▪ py-include: inclui um arquivo externo no template.
Exemplo:
<py-include="header.html">
Corpo da página...
<py-include="footer.html">
Além de usar uma string como template, é possível guardar o template em um 
arquivo:
renderTemplate(file='index.html')
Exemplo com CherryTemplate:
from cherrytemplate import renderTemplate
progs = ['Yes', 'Genesis', 'King Crimson']
template = '<html>\n<body>\n'\
'<py-for="prog in progs">'\
'    <py-eval="prog"><br>\n'\
'</py-for>'\
'</body>\n</html>\n'
print renderTemplate(template)
Saída HTML:
<html>
<body>
    Yes<br>
    Genesis<br>
    King Crimson<br>
</body>

## Página 184

184 Web
</html>
As  saídas  geradas  pelo  CherryTemplate  podem  ser  publicadas  pelo  
CherryPy.
Cliente Web
O Python também pode funcionar do lado cliente, através do módulo urllib.
Exemplo:
# -*- coding: latin1 -*-
import urllib
# Abre a URL e fornece um objeto semelhante
# a um arquivo convencional
url = urllib.urlopen('http://ark4n.wordpress.com/')
# Lê a página
html = url.read()
#html = '<a href="http://www.gnu.org/">'
found = html.find('href=', 0)
# find retorna -1 se não encontra
while found >= 0:
    # O fim do link (quando as aspas acabam)
    end = html.find(html[found + 5], found + 6) + 1
    # Mostra o link
    print html[found:end]
    # Passa para o próximo link
    found = html.find('href=', found + 1)
Outra solução cliente é o Twisted Web 47, que é parte do projeto Twisted 48, um 
framework orientado  a eventos  voltado  para  protocolos  de  rede,  incluindo  
HTTP, SSH, IRC, IMAP e outros.
47 Endereço: http://twistedmatrix.com/trac/wiki/TwistedWeb.
48 Endereço: http://twistedmatrix.com/trac/.

## Página 185

MVC 185
MVC
Model-view-controller ( MVC)  é  uma  arquitetura  de  software  que  divide  a  
aplicação em três partes distintas: o modelo de dados da aplicação, a interface  
com o usuário e a lógica de controle.
O objetivo é obter um baixo acoplamento entre as três partes de forma que  
uma alteração em uma parte tenha pouco (ou nenhum) impacto nas outras  
partes.
A criação da aplicação dependente da definição de três componentes:
▪ Modelo (model): encapsula os dados da aplicação e a lógica de domínio.
▪ Visão (view): recupera dados do modelo e apresenta ao usuário.
▪ Controlador  ( controller):  recebe  e  reage  a  possíveis  eventos,  como  
interações com o usuário e requisita alterações no modelo e na visão.
Embora  a  arquitetura  não  determine  formalmente  a  presença  de  um  
componente de persistência, fica implícito que este faz parte do componente  
modelo.
Controller
MVC: Model View Controller
Model
View
Recupera dados e 
apresenta ao 
usuário.
Encapsula os dados 
da aplicação e a 
lógica de domínio.
Recebe e reage a 
eventos.

## Página 186

186 MVC
O uso mais comum para o modelo  MVC é em aplicações  Web baseadas em  
bancos de dados, que implementam as operações básicas chamadas CRUD  
(Create, Read, Update and Delete).
Existem  vários  frameworks  para  aumentar  a  produtividade  na  criação  de  
aplicativos seguindo o MVC, com recursos como:
▪ Scripts que automatizam as tarefas mais comuns de desenvolvimento.
▪ Geração automática de código.
▪ Uso de ORM.
▪ Uso de CSS49 (Cascade Style Sheets).
▪ Uso de AJAX (Asynchronous Javascript And XML).
▪ Modelos de aplicações.
▪ Uso  de  introspecção  para  obter  informações  sobre  as  estruturas  de  
dados  e  gerar  formulários  com  campos  com  as  características  
correspondentes.
▪ Diversas  opções  pré-configuradas  com  defaults adequados  para  a  
maioria das aplicações.
Uma  das  maiores  vantagens  oferecidas  pelo  MVC  é  que,  ao  separar  a  
apresentação da lógica de aplicação, se torna mais fácil dividir as tarefas de  
desenvolvimento e de design da interface em uma equipe.
Exemplo:
# -*- coding: utf-8 -*-
"""
Web com operações CRUD
"""
# CherryPy
import cherrypy
# CherryTemplate
import cherrytemplate
# SQLAlchemy
import sqlalchemy as sql
49 Especificação em: http://www.w3.org/Style/CSS/.

## Página 187

MVC 187
# Conecta ao bando
db = sql.create_engine('sqlite:///zoo.db')
# Acesso aos metadados
metadata = sql.MetaData(db)
try:
    # Carrega metadados da tabela
    zoo = sql.Table('zoo', metadata, autoload=True)
except:
    # Define a estrutura da tabela zoo
    zoo = sql.Table('zoo', metadata,
        sql.Column('id', sql.Integer, primary_key=True),
        sql.Column('nome', sql.String(100),
            unique=True, nullable=False),
        sql.Column('quantidade', sql.Integer, default=1),
        sql.Column('obs', sql.String(200), default='')
    )
    # Cria a tabela
    zoo.create()
# Os nomes das colunas
colunas = [col for col in zoo.columns.keys()]
colunas.remove('id')
class Root(object):
    """Raiz do site"""
    @cherrypy.expose
    def index(self, **args):
        """
        Lista os registros
        """
        msg = ''
        op = args.get('op')
        ident = int(args.get('ident', 0))
        novo = {}
        for coluna in colunas:
            novo[coluna] = args.get(coluna)
        if op == 'rem':

## Página 188

188 MVC
            # Remove dados
            rem = zoo.delete(zoo.c.id==ident)
            rem.execute()
            msg = 'registro removido.'
        elif op == 'add':
            novo = {}
            for coluna in colunas:
                novo[coluna] = args[coluna]
            try:
                # Insere dados
                ins = zoo.insert()
                ins.execute(novo)
                msg = 'registro adicionado.'
            except sql.exceptions.IntegrityError:
                msg = 'registro existe.'
        elif op == 'mod':
            novo = {}
            for coluna in colunas:
                novo[coluna] = args[coluna]
            try:
                # Modifica dados
                mod = zoo.update(zoo.c.id==ident)
                mod.execute(novo)
                msg = 'registro modificado.'
            except sql.exceptions.IntegrityError:
                msg = 'registro existe.'
        # Seleciona dados
        sel = zoo.select(order_by=zoo.c.nome)
        rec = sel.execute()
        # Gera a página principal a partir do modelo "index.html"
        return cherrytemplate.renderTemplate(file='index.html',
            outputEncoding='utf-8')
    @cherrypy.expose

## Página 189

MVC 189
    def add(self):
        """
        Cadastra novos registros
        """
        # Gera a página de registro novo a partir do modelo "add.html"
        return cherrytemplate.renderTemplate(file='add.html',
            outputEncoding='utf-8')
    @cherrypy.expose
    def rem(self, ident):
        """
        Confirma a remoção de registros
        """
        # Seleciona o registro
        sel = zoo.select(zoo.c.id==ident)
        rec = sel.execute()
        res = rec.fetchone()
        # Gera a página de confirmar exclusão a partir do modelo "rem.html"
        return cherrytemplate.renderTemplate(file='rem.html',
            outputEncoding='utf-8')
    @cherrypy.expose
    def mod(self, ident):
        """
        Modifica registros
        """
        # Seleciona o registro
        sel = zoo.select(zoo.c.id==ident)
        rec = sel.execute()
        res = rec.fetchone()
        # Gera a página de alteração de registro a partir do modelo "mod.html"
        return cherrytemplate.renderTemplate(file='mod.html',
            outputEncoding='utf-8')
# Inicia o servidor na porta 8080
cherrypy.quickstart(Root())
Modelo “index.html” (página principal):

## Página 190

190 MVC
<py-include="header.html">
<table>
<tr>
<th></th>
<py-for="coluna in colunas">
    <th><py-eval="coluna"></th>
</py-for>
<th></th>
<th></th>
</tr>
<py-for="i, campos in enumerate(rec.fetchall())">
    <tr>
    <th><py-eval="unicode(i + 1)"></th>
    <py-for="coluna in colunas">
        <td><py-eval="unicode(campos[coluna])"></td>
    </py-for>
    <td>
    <a href="/mod?ident=<py-
eval="unicode(campos['id'])">">modificar</a>
    </td><td>
    <a href="/rem?ident=<py-eval="unicode(campos['id'])">">remover</a>
    </td>
    </tr>
</py-for>
</table>
<br />
<form action="/add" method="post">
    <input type="submit" value=" adicionar " />
</form>
<p>
<py-eval="msg">
</p>
<py-include="footer.html">
Modelo “add.html” (página de formulário para novos registros):
<py-include="header.html">
<form action="/?op=add" method="post">
    <table>
    <py-for="coluna in colunas">
        <tr><td>
        <py-eval="coluna">
        </td><td>
        <input type="text" size="30" name="<py-eval="coluna">" />
        </td></tr>

## Página 191

MVC 191
    </py-for>
    </table>
<br />
<input type="submit" value=" salvar " />
</form>
<br />
[ <a href="/">voltar</a> ]
<py-include="footer.html">
Modelo “mod.html” (página de formulário para alteração de registros):
<py-include="header.html">
<form action="/?op=mod&ident=<py-eval="unicode(res['id'])">" 
method="post">
    <table border="0">
    <py-for="coluna in colunas">
        <tr><th>
        <py-eval="coluna">
        </th><td>
        <input type="text" size="30" name="<py-eval="coluna">"
        value="<py-eval="unicode(res[coluna])">" />
        </td></tr>
    </py-for>
    </table>
<br />
<input type="submit" value=" salvar " />
</form>
<br />
[ <a href="/">voltar</a> ]
<py-include="footer.html">
Modelo  “rem.html”  (página  que  pede  confirmação  para  remoção  de  
registros):
<py-include="header.html">
<table border="1">
<tr>
<py-for="coluna in colunas">
    <th><py-eval="coluna"></th>
</py-for>
</tr>
<tr>
<py-for="coluna in colunas">

## Página 192

192 MVC
    <td><py-eval="unicode(res[coluna])"></td>
</py-for>
</tr>
</table>
<br />
<form action="/?op=rem&ident=<py-eval="unicode(res['id'])">" 
method="post">
    <input type="submit" value=" remover " />
</form>
<br />
[ <a href="/">voltar</a> ]
<py-include="footer.html">
Modelo “header.html” (cabeçalho comum a todos os modelos):
<html>
<head>
 <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
<title>Zoo</title>
<style type="text/css">
<!--
body {
    margin: 10;
    padding: 10;
    font: 80% Verdana, Lucida, sans-serif;
    color: #333366;
}
h1 {
    margin: 0;
    padding: 0;
    font: 200% Lucida, Verdana, sans-serif;
}
a {
    color: #436976;
    text-decoration: none;
}
a:hover {
    background: #c4cded;
    text-decoration: underline;
}
table {
    margin: 1em 0em 1em 0em;
    border-collapse: collapse;
    border-left: 1px solid #858ba1;
    border-bottom: 1px solid #858ba1;

## Página 193

MVC 193
    font: 90% Verdana, Lucida, sans-serif;
}
table th {
    padding: 0em 1em 0em 1em;
    border-top: 1px solid #858ba1;
    border-bottom: 1px solid #858ba1;
    border-right: 1px solid #858ba1;
    background: #c4cded;
    font-weight: normal;
}
table td {
    padding: 0em 1em 0em 1em;
    border-top: 1px solid #858ba1;
    border-right: 1px solid #858ba1;
    text-align: center;
}
form {
    margin: 0;
    border: none;
}
input {
    border: 1px solid #858ba1;
    background-color: #c4cded;
    vertical-align: middle;
}
-->
</style>
</head>
<body>
<h1>Zoo</h1>
<br />
Modelo “footer.html” (rodapé comum a todos os modelos):
</body>
</html>
Página principal:

## Página 194

194 MVC
O  framework  MVC mais  conhecido  é  o  Ruby  On  Rails,  que  ajudou  a  
popularizar o MVC entre os desenvolvedores.
Especificamente desenvolvidos em Python, existem os  frameworks Django 50, 
TurboGears51 e web2py52, entre outros.
50 Página oficial em: http://www.djangoproject.com/.
51 Página oficial em: http://turbogears.org/.
52 Página oficial em: http://www.web2py.com/.


## Página 195

Exercícios V 195
Exercícios V
1. Implementar uma classe  Animal com os atributos: nome, espécie, gênero,  
peso, altura e idade. O objeto derivado desta classe deverá salvar seu estado  
em arquivo com um método chamado “salvar” e recarregar o estado em um  
método chamado “desfazer”.
2. Implementar uma função que formate uma lista de tuplas como tabela  
HTML.
3.  Implementar  uma  aplicação  Web com  uma  saudação  dependente  do  
horário (exemplos: “Bom dia, são 09:00.”, “Boa tarde, são 13:00.” e “Boa noite,  
são 23:00.”).
4. Implementar uma aplicação Web com um formulário que receba expressões 
Python e retorne a expressão com seu resultado.

## Página 196

196 Parte VI
Parte VI
Esta parte apresenta algumas funcionalidades dos pacotes NumPy, SciPy e  
Matplolib,  e também  de  conhecidos  toolkits para  interfaces  gráficas.  Além  
disso,  uma  breve  introdução  a  computação  gráfica  e  processamento  
distribuído. E por fim, observações sobre performance no Python e formas de  
empacotar e distribuir aplicativos.
Conteúdo:
▪ Processamento numérico  .
▪ Interface gráfica  .
▪ Computação gráfica  .
▪ Processamento de imagem  .
▪ SVG  .
▪ Imagens em três dimensões  .
▪ Processamento distribuído  .
▪ Performance  .
▪ Empacotamento e distribuição  .
▪ Exercícios VI  .

## Página 197

Processamento numérico 197
Processamento numérico
No Python, além dos recursos matemáticos que fazem parte da distribuição  
padrão, o processamento numérico pode ser feito através do NumPy e outros  
pacotes que foram construídos a partir dele.
NumPy
NumPy53 é um pacote que inclui:
▪ Classe array.
▪ Classe matrix.
▪ Várias funções auxiliares.
Arranjos
A  classe  array implementa  um  arranjo  homogêneo  mutável  com  número  
arbitrário de elementos, semelhante à lista comum do Python, porém mais  
poderosa.
Exemplos:
import numpy
# Criando arranjos
print 'Arranjo criado a partir de uma lista:'
a = numpy.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
print a
# [0 1 2 3 4 5 6 7 8]
print 'Arranjo criado a partir de um intervalo:'
z = numpy.arange(0., 4.5, .5)
print z
# [ 0.   0.5  1.   1.5  2.   2.5  3.   3.5  4. ]
print 'Arranjo de 1s 2x3:'
y = numpy.ones((2, 3))
53 Fontes, binários e documentação podem ser encontrados em: http://numpy.scipy.org/.

## Página 198

198 Processamento numérico
print y
# [[ 1.  1.  1.]
#  [ 1.  1.  1.]]
print 'Arranjos podem gerar novos arranjos:'
# numpy.round() é uma função do numpy
# semelhante ao builtin round(), porém aceita
# arranjos como parâmetro
cos = numpy.round(numpy.cos(z), 1)
print cos
# [ 1.   0.9  0.5  0.1 -0.4 -0.8 -1.  -0.9 -0.7]
print 'Multiplicando cada elemento por um escalar:'
print 5 * z
# [  0.    2.5   5.    7.5  10.   12.5  15.   17.5  20. ]
print 'Somando arranjos elemento por elemento:'
print z + cos
# [ 1.   1.4  1.5  1.6  1.6  1.7  2.   2.6  3.3]
print 'Redimensionando o arranjo:'
z.shape = 3, 3
print z
# [[ 0.   0.5  1. ]
#  [ 1.5  2.   2.5]
#  [ 3.   3.5  4. ]]
print 'Arranjo transposto:'
print z.transpose()
# [[ 0.   1.5  3. ]
#  [ 0.5  2.   3.5]
#  [ 1.   2.5  4. ]]
print '"Achata" o arranjo:'
print z.flatten()
# [ 0.   0.5  1.   1.5  2.   2.5  3.   3.5  4. ]
print 'O acesso aos elementos funciona como nas listas:'
print z[1]
# [ 1.5  2.   2.5]
print 'Caso especial, diferente da lista:'
print z[1, 1]
# 2.0

## Página 199

Processamento numérico 199
# Dados sobre o arranjo
print 'Formato do arranjo:'
print z.shape
# (3, 3)
print 'Quantidade de eixos:'
print z.ndim
# 2
print 'Tipo dos dados:'
print z.dtype
# float64
Saída completa:
Arranjo criado a partir de uma lista:
[0 1 2 3 4 5 6 7 8]
Arranjo criado a partir de um intervalo:
[ 0.   0.5  1.   1.5  2.   2.5  3.   3.5  4. ]
Arranjo de 1s 2x3:
[[ 1.  1.  1.]
 [ 1.  1.  1.]]
Arranjos podem gerar novos arranjos:
[ 1.   0.9  0.5  0.1 -0.4 -0.8 -1.  -0.9 -0.7]
Multiplicando cada elemento por um escalar:
[  0.    2.5   5.    7.5  10.   12.5  15.   17.5  20. ]
Somando arranjos elemento por elemento:
[ 1.   1.4  1.5  1.6  1.6  1.7  2.   2.6  3.3]
Redimensionando o arranjo:
[[ 0.   0.5  1. ]
 [ 1.5  2.   2.5]
 [ 3.   3.5  4. ]]
Arranjo transposto:
[[ 0.   1.5  3. ]
 [ 0.5  2.   3.5]
 [ 1.   2.5  4. ]]
"Achata" o arranjo:
[ 0.   0.5  1.   1.5  2.   2.5  3.   3.5  4. ]
O acesso aos elementos funciona como nas listas:
[ 1.5  2.   2.5]
Caso especial, diferente da lista:
2.0
Formato do arranjo:

## Página 200

200 Processamento numérico
(3, 3)
Quantidade de eixos:
2
Tipo dos dados:
float64
Ao contrário  da lista,  os arranjos  sempre são homogêneos,  ou seja,  todos  
elementos são do mesmo tipo.
Matrizes
A classe matrix implementa operações de matrizes.
Exemplos:
import numpy
print 'Criando uma matriz a partir de uma lista:'
l = [[3,4,5], [6, 7, 8], [9, 0, 1]]
Z = numpy.matrix(l)
print Z
# [[3 4 5]
#  [6 7 8]
#  [9 0 1]]
print 'Transposta da matriz:'
print Z.T
# [[3 6 9]
#  [4 7 0]
#  [5 8 1]]
print 'Inversa da matriz:'
print Z.I
# [[-0.23333333  0.13333333  0.1       ]
#  [-2.2         1.4        -0.2       ]
#  [ 2.1        -1.2         0.1       ]]
# Criando outra matriz
R = numpy.matrix([[3, 2, 1]])
print 'Multiplicando matrizes:'
print R * Z
# [[30 26 32]]

## Página 201

Processamento numérico 201
print 'Resolvendo um sistema linear:'
print numpy.linalg.solve(Z, numpy.array([0, 1, 2]))
# [ 0.33333333  1.         -1.        ]
Saída:
Criando uma matriz a partir de uma lista:
[[3 4 5]
 [6 7 8]
 [9 0 1]]
Transposta da matriz:
[[3 6 9]
 [4 7 0]
 [5 8 1]]
Inversa da matriz:
[[-0.23333333  0.13333333  0.1       ]
 [-2.2         1.4        -0.2       ]
 [ 2.1        -1.2         0.1       ]]
Multiplicando matrizes:
[[30 26 32]]
Resolvendo um sistema linear:
[ 0.33333333  1.         -1.        ]
O módulo  numpy.linalg também implementa  funções de  decomposição de  
matrizes:
from numpy import *
# Matriz 3x3
A = array([(9, 4, 2), (5, 3, 1), (2, 0, 7)])
print 'Matriz A:'
print A
# Decompondo usando QR
Q, R = linalg.qr(A)
# Resultados
print 'Matriz Q:'
print Q
print 'Matriz R:'
print R

## Página 202

202 Processamento numérico
# Produto
print 'Q . R:'
print int0(dot(Q, R))
Saída:
Matriz A:
[[9 4 2]
 [5 3 1]
 [2 0 7]]
Matriz Q:
[[-0.85811633  0.14841033 -0.49153915]
 [-0.47673129 -0.58583024  0.65538554]
 [-0.19069252  0.79672913  0.57346234]]
Matriz R:
[[-10.48808848  -4.86265921  -3.52781158]
 [  0.          -1.16384941   5.28809431]
 [  0.           0.           3.68654364]]
Q . R:
[[9 4 2]
 [5 3 1]
 [2 0 7]]
O NumPy serve de base para diversos outros projetos de código aberto, como  
o Matplolib e o SciPy, que complementam o Numpy de várias formas.
SciPy
SciPy54 é  um  pacote  que  expande  o  NumPy com  outras  funcionalidades  
voltadas para a área cientifica.
Entre os módulos que fazem parte do pacote, temos:
▪ linalg: funções de álgebra linear.
▪ fftpack: transformada de Fourier.
▪ integrate: funções de integração.
▪ interpolate: funções de interpolação.
▪ optimize: funções de optimização.
▪ signal: processamento de sinais.
54 Página oficial em: http://www.scipy.org/.

## Página 203

Processamento numérico 203
▪ special: funções especiais (Airy, Bessel, etc).
Exemplo:
# -*- coding: latin1 -*-
from numpy import arange, cos, sin
# Duas funções do SciPy para processamento de sinais
from scipy.signal import cspline1d, cspline1d_eval
# Duas funções do Matplotlib para gerar um gráfico
from pylab import plot, show
x0 = arange(20) # X original
y0 = cos(x0) * sin(x0 / 2) # Y a partir de X
dx = x0[1]-x0[0] # Diferença original
x1 = arange(-1, 21, 0.1)
# Coeficientes para arranjo de 1 dimensão
cj = cspline1d(y0)
# Avalia o Spline para um novo conjunto de pontos
y1 = cspline1d_eval(cj, x1, dx=dx,x0=x0[0])
plot(x1, y1, '-g', x0, y0, '^y') # Desenha
show() # Mostra o gráfico
Saída:


## Página 204

204 Processamento numérico
Além do SciPy, existe também o ScientificPython 55, que é outro pacote que  
implementa rotinas para uso cientifico.
Matplotlib
Existem vários pacotes de terceiros para a geração de gráficos disponíveis  
para Python, sendo que o mais popular deles é o Pylab / Matplotlib56.
O pacote tem dois módulos principais:
▪ matplotlib: módulo que oferece uma abstração orientada a objetos aos  
recursos do pacote.
▪ pylab: módulo que oferece uma coleção de comandos que se assemelha  
ao Matlab, e é mais adequado para o uso interativo.
Exemplo:
from pylab import *
ent = arange(0., 20.1, .1)
# Calcula os cossenos da entrada
sai = cos(ent)
# Plota a curva
plot(ent, sai)
# Texto para o eixo X
xlabel('entrada')
# Texto para o eixo Y
ylabel('cosseno')
# Texto no topo da figura
title('Cossenos')
# Ativa a grade
grid(True)
# Apresenta a figura resultante na tela
55 Fontes e binários disponíveis em: http://sourcesup.cru.fr/projects/scientific-py/.
56 Fontes,  binários  e  documentação  podem  ser  encontrados  em:  
http://matplotlib.sourceforge.net/.

## Página 205

Processamento numérico 205
show()
Saída:
Outro exemplo:
from pylab import *
# Dados
ent1 = arange(0., 7., .1)
sai1 = cos(ent1)
sai2 = sin(ent1)
dif = sai2 - sai1
# Divide a figura em 2 linhas e 1 coluna,
# e seleciona a parte superior
subplot(211)
# Plota a curva
# Primeira curva: ent1, sai1, 'bo:'
# Segunda curva: ent1, sai2, 'g^-'
plot(ent1, sai1, 'bo:', ent1, sai2, 'g^-')
# Cria uma legenda
legend(['Cossenos', 'Senos'])
# Seleciona a parte inferior
subplot(212)


## Página 206

206 Processamento numérico
# Desenha barras
# Eixo X: arange(len(dif)) + .5
# Eixo Y: dif
# Largura das barras: .5
# Cor: #ccbbaa
bar(arange(len(dif)) + .5, dif, .5, color='#ccbbaa')
# Salva a figura
savefig('graf.png')
Saída:
O pacote tem funções para gerar gráficos de barra, linha, dispersão, pizza e  
polar, entre outros.
Exemplo usando matplotlib:
# -*- coding: latin1 -*-
import os
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
def pie(filename, labels, values):
    """
    Gera um diagrama de Pizza e salva em arquivo.
    """


## Página 207

Processamento numérico 207
    # Use a biblioteca Anti-Grain Geometry
    matplotlib.use('Agg')
    # Cores personalizadas
    colors = ['seagreen', 'lightslategray', 'lavender',
        'khaki', 'burlywood', 'cornflowerblue']
    # Altera as opções padrão
    matplotlib.rc('patch', edgecolor='#406785',
        linewidth=1, antialiased=True)
    # Altera as dimensões da imagem
    matplotlib.rc('figure', figsize=(8., 7.))
    # Inicializa a figura
    fig = Figure()
    fig.clear()
    axes = fig.add_subplot(111)
    if values:
        # Diagrama
        chart = axes.pie(values, colors=colors, autopct='%2.0f%%')
        # Legenda
        pie_legend = axes.legend(labels)
        pie_legend.pad = 0.3
        # Altera o tamanho da fonte
        for i in xrange(len(chart[0])):
            chart[-1][i].set_fontsize(12)
            pie_legend.texts[0].set_fontsize(10)
    else:
        # Mensagem de erro
        # Desliga o diagrama
        axes.set_axis_off()
        # Mostra a mensagem
        axes.text(0.5, 0.5, 'Sem dados',
            horizontalalignment='center',
            verticalalignment='center',
            fontsize=32, color='#6f7c8c')
    # Salva a figura
    canvas = FigureCanvasAgg(fig)
    canvas.print_figure(filename, dpi=600)
if __name__ == '__main__':

## Página 208

208 Processamento numérico
    # Testes
    pie('fig1.png', [], [])
    pie('fig2.png', ['A', 'B', 'C', 'D', 'E'],
        [6.7, 5.6, 4.5, 3.4, 2.3])
Saída:
Existem  add ons  para o Matplotlib, que expandem a biblioteca com novas  
funcionalidades, como é o caso do Basemap.
Exemplo com Basemap:
from mpl_toolkits.basemap import Basemap
from matplotlib import pyplot
from numpy import arange
# Cria um mapa usando Basemap
mapa = Basemap(projection='robin', lat_0=-20, lon_0=-50,
    resolution='l', area_thresh=1e3)
    
# desenha a costa dos continentes
mapa.drawcoastlines(color='#777799')
# Desenha as fronteiras
mapa.drawcountries(color='#ccccee')
# Pinta os continentes
mapa.fillcontinents(color='#ddddcc')
# Desenha os meridianos


## Página 209

Processamento numérico 209
mapa.drawmeridians(arange(0, 360, 30), color='#ccccee')
# Desenha os paralelos
mapa.drawparallels(arange(-180, 180, 30), color='#ccccee')
# Desenha os limites do mapa
mapa.drawmapboundary()
# Salva a imagem
pyplot.savefig('mapa1.png', dpi=150)
Saída:
Outro exemplo:
from mpl_toolkits.basemap import Basemap
from matplotlib import pyplot
mapa = Basemap(projection='ortho', lat_0=10, lon_0=-10,
    resolution='l', area_thresh=1e3)
# Preenche o mapa com relevo
mapa.bluemarble()
mapa.drawmapboundary()
lxy = (('Rio\nde\nJaneiro', -43.11, -22.54),
    ('Londres', 0.07, 50.30))
# Transposta
lxy = zip(*lxy)
# Converte as coordenadas
x, y = mapa(lxy[1], lxy[2])
lxy = lxy[0], x, y
# Marca no mapa
mapa.plot(x, y, 'w^')


## Página 210

210 Processamento numérico
# Escreve os nomes
for l, x, y in zip(*lxy):
    pyplot.text(x+2e5, y-6e5, l,
        color='#eeeecc')
pyplot.savefig('mapa2.png', dpi=150)
Saída:
Para  processamento  de  informações  georreferenciadas  de  forma  mais  
sofisticada, existe o projeto MapServer 57, um servidor de aplicação voltado  
para  GIS  (Geographic  Information  System)  que  suporta  diversas  linguagens, 
inclusive Python.
Além  de  módulos  de  terceiros,  também  é  possível  usar  a  planilha  do  
BrOffice.org58 para gerar  gráficos com o Python,  através  da API chamada  
Python-UNO Bridge59.
57 Site oficial em http://mapserver.org/.
58 Disponível em: http://www.broffice.org/.
59 Mais informações em: http://udk.openoffice.org/python/python-bridge.html.


## Página 211

Interface Gráfica 211
Interface Gráfica
As  Interfaces  Gráficas  com  Usuário  (GUI,  Graphic  User  Interface )  se  
popularizaram  no  ambiente  desktop,  devido  à  facilidade  de  uso  e  a  
produtividade. Existem hoje muitas bibliotecas disponíveis para a construção  
de aplicações GUI, tais como: GTK+, QT, TK e wxWidgets.
Arquitetura
Interfaces gráficas geralmente utilizam a metáfora do desktop, um espaço em  
duas dimensões, é que ocupado por janelas retangulares, que representam  
aplicativos, propriedades ou documentos.
As janelas podem conter diversos tipos de controles (objetos utilizados para  
interagir com o usuário ou para apresentar informações) e containers (objetos 
que servem de repositório para coleções de outros objetos).
Na maior parte do tempo, a interface gráfica espera por eventos e responde  
de acordo.  Os eventos podem ser resultado da interação do usuário, como  
cliques e arrastar de mouse ou digitação, ou ainda de eventos de sistema,  
Janela
Containers
 Controles

## Página 212

212 Interface Gráfica
como  o  relógio  da  máquina.  A  reação  a  um  evento  qualquer  é  definida  
através de funções callback (funções que são passadas como argumento para  
outras rotinas).
Controles mais usados:
▪ Rótulo (label): retângulo que exibe texto.
▪ Caixa de texto (text box): área de edição de texto.
▪ Botão (button): área que pode ser ativada interativamente.
▪ Botão de rádio ( radio button ): tipo especial de botão, com o qual são  
formados grupos aonde apenas um pode ser apertado de cada vez.
▪ Botão  de  verificação  ( check  button):  botão  que  pode  ser  marcado  e  
desmarcado.
▪ Barras  de  rolagem  (scroll  bars):  controles  deslizantes  horizontais  ou  
verticais, usados para intervalos de valores numéricos.
▪ Botão giratório ( spin button): caixa de texto com dois botões com setas  
ao lado que incrementam e decrementam o número na caixa.
▪ Barra  de  status  ( status  bar ):  barra  para  exibição  de  mensagens,  
geralmente na parte inferior da janela.
▪ Imagem (image): área para exibição de imagens.
Controles podem ter aceleradores (teclas de atalho) associados a eles.
Containers mais usados:
▪ Barra  de  menu  (menu  bar):  sistema  de  menus,  geralmente  na  parte 
superior da janela.
▪ Fixo (fixed): os objetos permanecem fixos nas mesmas posições.
▪ Tabela  ( table):  coleção  de  compartimentos  para  fixar  os  objetos,  
distribuídos em linhas e colunas.
▪ Caixa horizontal ( horizontal box ): semelhante à tabela, porém apenas  
com uma linha.
▪ Caixa vertical  ( vertical box ):  semelhante à tabela, porém apenas com  
uma coluna.
▪ Caderno ( notebook): várias áreas que podem ser visualizadas uma de  
cada vez  quando selecionadas através  de abas, geralmente  na parte  
superior.
▪ Barra de ferramentas ( tool bar): área com botões para acesso rápido aos  
principais recursos do aplicativo.

## Página 213

Interface Gráfica 213
Para lidar com eventos de tempo, as interfaces gráficas implementam um  
recurso chamado temporizador ( timer) que evoca a função callback depois de  
um certo tempo programado.
PyGTK
O GTK+60 (GIMP Toolkit) é uma biblioteca Open Source escrita em linguagem  
C. Originalmente concebida para ser usada pelo GIMP 61, é compatível com as  
plataformas mais utilizadas atualmente e rica em recursos, entre eles, um  
construtor de interfaces chamado Glade.
Interface do Glade:
O  GTK+ é  usado  pelo  GNOME 62 (ambiente  desktop  Open  Source )  e  por  
diversos aplicativos, como os portes do Mozilla Firefox e do BrOffice.org para  
60 A página internet do projeto reside em: http://www.gtk.org/. e os binários para Windows 
estão disponíveis em: http://gladewin32.sourceforge.net/. A versão para desenvolvedores 
instala o Glade.
61 Endereço oficial do projeto: http://www.gimp.org/.
62 Documentação e fontes em: http://www.gnome.org/.


## Página 214

214 Interface Gráfica
sistemas  UNIX.  O  GTK+ pode  ser  usado  no  Python  através  do  pacote  
PyGTK63. Os portes das bibliotecas para Windows podem ser encontrados  
em:
▪ PyGTK: http://ftp.gnome.org/pub/gnome/binaries/win32/pygtk/
▪ PyGObject: http://ftp.gnome.org/pub/gnome/binaries/win32/pygobject/
▪ PyCairo: http://ftp.gnome.org/pub/gnome/binaries/win32/pycairo/
Embora  seja  possível  criar  interfaces  inteiramente  usando  código,  é  mais  
produtivo construir a interface em um software apropriado. O  Glade gera  
arquivos XML com extensão “.glade”, que podem ser lidos por programas  
que usam GTK+, automatizando o processo de criar interfaces gráficas.
Roteiro básico para construir uma interface:
No Glade:
▪ Crie uma janela usando algum dos modelos disponíveis em “Níveis  
Superiores”.
▪ Crie containers para armazenar os controles.
▪ Crie os controles.
▪ Crie os manipuladores para os sinais necessários.
▪ Salve o arquivo com a extensão “.glade”.
No Python:
▪ Importe os pacotes necessários.
▪ Use o GTK para interpretar o arquivo XML do Glade.
▪ Crie rotinas para serem usadas como funções callback.
▪ Associe  as  rotinas  com  os  manipuladores  correspondes  que  foram  
criados no Glade, através do método signal_autoconnect().
▪ Ative o laço para processar eventos com gtk.main().
Exemplo (relógio):
No Glade:
▪ Clique em “janela” em “Níveis Superiores”.
▪ Nas propriedades da janela:
• Mude “Nome” para “main” em “Geral”.
63 A página na internet do PyGTK é http://www.pygtk.org/.

## Página 215

Interface Gráfica 215
• Mude “Redimensionável” para “Sim”.
• Mude “Posição da janela” para “Centralizar”.
• Mude “Visível” para “Sim” em “Comum”.
• Mude o manipulador para “on_main_destroy” do sinal “destroy”  
de “GtkObject” em “Sinais”.
▪ Clique em “Caixa vertical” em “Containers”, depois clique dentro da  
janela e escolha o número de itens igual a 3.
▪ Clique em “Barra de menu” em “Containers”, depois clique dentro do  
espaço vazio superior e delete os itens “Editar” e “Ver”.
▪ Clique em “Barra de status”  em “Controle e Exibição” e depois clique  
dentro do espaço vazio inferior.
▪ Mude o nome da barra de status para “sts_data” em “Geral”.
▪ Clique em “Rótulo” em “Controle e Exibição” e depois clique dentro  
do espaço vazio central.
▪ Nas propriedades do rótulo, mude “Nome” para “lbl_hora” e “Rótulo”  
para  vazio  em  “Geral”,  “Solicitação  de  largura”  para  “300”  e  
“Solicitação de altura” para “150” em “Comum”.
▪ No “Inspetor” (lista em forma de árvore com todos itens), delete:
• “imagemenuitem1”.
• “imagemenuitem2”.
• “imagemenuitem3”.
• “imagemenuitem4”.
• “separatormenuitem1”.
▪ No “Inspetor”:
• localize “imagemenuitem5” e mude o manipulador em “Sinais” do  
sinal  “activate”  para  “on_imagemenuitem5_activate”  de  
“GtkMenuItem”.
• localize “imagemenuitem10” e mude o manipulador em “Sinais” do  
sinal  “activate”  para  “on_imagemenuitem10_activate”  de  
“GtkMenuItem”.
▪ Salve o arquivo como “relogio.glade”.
Janela principal do relógio:

## Página 216

216 Interface Gráfica
Código em Python:
# -*- coding: latin1 -*-
"""
Um relógio com GTK.
"""
import datetime
# GTK e outros módulos associados
import gtk
import gtk.glade
import gobject
import pango
class Relogio(object):
    """
    Implementa a janela principal do programa.
    """
    def __init__(self):
        """
        Inicializa a classe.
        """
        # Carrega a interface
        self.tree = gtk.glade.XML('relogio.glade', 'main')
        # Liga os eventos
        callbacks = {
            'on_main_destroy': self.on_main_destroy,
            'on_imagemenuitem5_activate': self.on_main_destroy,
            'on_imagemenuitem10_activate': self.on_imagemenuitem10_activate


## Página 217

Interface Gráfica 217
            }
        self.tree.signal_autoconnect(callbacks)
        # Coloca um título na janela
        self.tree.get_widget('main').set_title('Relógio')
        # O rótulo que reberá a hora
        self.hora = self.tree.get_widget('lbl_hora')
        # A barra de status que reberá a data
        self.data = self.tree.get_widget('sts_data')
        print dir(self.data)
        # Muda a fonte do rótulo
        self.hora.modify_font(pango.FontDescription('verdana 28'))
        # Um temporizador para manter a hora atualizada
        self.timer = gobject.timeout_add(1000, self.on_timer)
    def on_imagemenuitem10_activate(self, widget):
        """
        Cria a janela de "Sobre".
        """
        # Caixa de dialogo
        dialog = gtk.MessageDialog(parent=self.tree.get_widget('main'),
            flags=gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
            type=gtk.MESSAGE_OTHER, buttons=gtk.BUTTONS_OK,
            message_format='Primeiro exemplo usando GTK.')
        dialog.set_title('Sobre')
        dialog.set_position(gtk.WIN_POS_CENTER_ALWAYS)
        # Exibe a caixa
        dialog.run()
        dialog.destroy()
        return
    def on_timer(self):
        """
        Rotina para o temporizador.
        """
        # Pega a hora do sistema
        hora = datetime.datetime.now().time().isoformat().split('.')[0]

## Página 218

218 Interface Gráfica
        # Muda o texto do rótulo
        self.hora.set_text(hora)
        # Pega a data do sistema em formato ISO
        data = datetime.datetime.now().date().isoformat()
        data = 'Data: ' + '/'.join(data.split('-')[::-1])
        # Coloca a data na barra de status
        self.data.push(0, data)
        # Verdadeiro faz com que o temporizador rode de novo
        return True
    def on_main_destroy(self, widget):
        """
        Termina o programa.
        """
        raise SystemExit
if __name__ == "__main__":
    # Inicia a GUI
    relogio = Relogio()
    gtk.main()
Arquivo “relogio.glade”:
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE glade-interface SYSTEM "glade-2.0.dtd">
<!--Generated with glade3 3.4.3 on Sat May 03 14:06:18 2008 -->
<glade-interface>
  <widget class="GtkWindow" id="main">
    <property name="visible">True</property>
    <property name="resizable">False</property>
    <property name="window_position">GTK_WIN_POS_CENTER</property>
    <signal name="destroy" handler="on_main_destroy"/>
    <child>
      <widget class="GtkVBox" id="vbox1">
        <property name="visible">True</property>
        <child>
          <widget class="GtkMenuBar" id="menubar1">
            <property name="visible">True</property>
            <child>

## Página 219

Interface Gráfica 219
              <widget class="GtkMenuItem" id="menuitem1">
                <property name="visible">True</property>
                <property name="label" translatable="yes">_Arquivo</property>
                <property name="use_underline">True</property>
                <child>
                  <widget class="GtkMenu" id="menu1">
                    <property name="visible">True</property>
                    <child>
                      <widget class="GtkImageMenuItem" id="imagemenuitem5">
                        <property name="visible">True</property>
                        <property name="label" translatable="yes">gtk-
quit</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                        <signal name="activate" 
handler="on_imagemenuitem5_activate"/>
                      </widget>
                    </child>
                  </widget>
                </child>
              </widget>
            </child>
            <child>
              <widget class="GtkMenuItem" id="menuitem4">
                <property name="visible">True</property>
                <property name="label" translatable="yes">Aj_uda</property>
                <property name="use_underline">True</property>
                <child>
                  <widget class="GtkMenu" id="menu3">
                    <property name="visible">True</property>
                    <child>
                      <widget class="GtkImageMenuItem" 
id="imagemenuitem10">
                        <property name="visible">True</property>
                        <property name="label" translatable="yes">gtk-
about</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                        <signal name="activate" 
handler="on_imagemenuitem10_activate"/>
                      </widget>
                    </child>
                  </widget>
                </child>
              </widget>
            </child>
          </widget>

## Página 220

220 Interface Gráfica
          <packing>
            <property name="expand">False</property>
          </packing>
        </child>
        <child>
          <widget class="GtkLabel" id="lbl_hora">
            <property name="width_request">300</property>
            <property name="height_request">150</property>
            <property name="visible">True</property>
            <property name="xpad">5</property>
            <property name="ypad">5</property>
          </widget>
          <packing>
            <property name="position">1</property>
          </packing>
        </child>
        <child>
          <widget class="GtkStatusbar" id="sts_data">
            <property name="visible">True</property>
            <property name="spacing">2</property>
          </widget>
          <packing>
            <property name="expand">False</property>
            <property name="position">2</property>
          </packing>
        </child>
      </widget>
    </child>
  </widget>
</glade-interface>
Exemplo (rodando programas):
No Glade:
▪ Crie  uma  janela  com  o  nome  “main”  com  o  manipulador  
“on_main_destroy” para o sinal “destroy”.
▪ Crie um container fixo para receber os controles.
▪ Crie  uma  caixa  de  texto  chamada  “ntr_cmd”.  Esta  caixa  receberá  
comandos para serem executados.
▪ Crie um botão de verificação chamado “chk_shell”, com o texto “Janela  
de texto”. Se o botão estiver marcado, o comando será executado em  
uma janela de texto.
▪ Crie  um  botão  chamado  “btn_rodar”  com  o  manipulador  

## Página 221

Interface Gráfica 221
“on_btn_fechar_clicked”  para  o  sinal  “clicked”.  Quando  clicado,  o  
comando da caixa de texto é executado.
▪ Crie  um  botão  chamado  “btn_fechar”  com  o  manipulador  
“on_btn_fechar_clicked”  para  o  sinal  “clicked”.  Quando  clicado,  o  
programa termina.
Janela principal:
Código em Python:
# -*- coding: utf-8 -*-
"""
Rodando programas com GTK.
"""
import subprocess
import gtk
import gtk.glade
import gobject
import pango
class Exec(object):
    """
    Janela principal.
    """
    def __init__(self):
        """
        Inicializa a classe.
        """
        # Carrega a interface
        self.tree = gtk.glade.XML('cmd.glade', 'main')
        # Liga os eventos


## Página 222

222 Interface Gráfica
        callbacks = {
            'on_main_destroy': self.on_main_destroy,
            'on_btn_fechar_clicked': self.on_main_destroy,
            'on_btn_rodar_clicked': self.on_btn_rodar_clicked
            }
        self.tree.signal_autoconnect(callbacks)
    def on_btn_rodar_clicked(self, widget):
        """
        Roda o comando.
        """
        ntr_cmd = self.tree.get_widget('ntr_cmd')
        chk_shell = self.tree.get_widget('chk_shell')
        cmd = ntr_cmd.get_text()
        if cmd:
            # chk_shell.state será 1 se chk_shell estiver marcado
            if chk_shell.state:
                cmd = 'cmd start cmd /c ' + cmd
            subprocess.Popen(args=cmd)
        else:
            # Caixa de dialogo
            dialog = gtk.MessageDialog(parent=self.tree.get_widget('main'),
                flags=gtk.DIALOG_MODAL |
                gtk.DIALOG_DESTROY_WITH_PARENT,
                type=gtk.MESSAGE_OTHER, buttons=gtk.BUTTONS_OK,
                message_format='Digite um comando.')
            dialog.set_title('Mensagem')
            dialog.set_position(gtk.WIN_POS_CENTER_ALWAYS)
            # Exibe a caixa
            dialog.run()
            dialog.destroy()
        return True
    def on_main_destroy(self, widget):
        """
        Termina o programa.
        """
        raise SystemExit

## Página 223

Interface Gráfica 223
if __name__ == "__main__":
    # Inicia a GUI
    exe = Exec()
    gtk.main()
O arquivo “cmd.glade”:
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE glade-interface SYSTEM "glade-2.0.dtd">
<!--Generated with glade3 3.4.3 on Tue May 27 23:44:03 2008 -->
<glade-interface>
  <widget class="GtkWindow" id="main">
    <property name="width_request">380</property>
    <property name="height_request">100</property>
    <property name="visible">True</property>
    <property name="title" translatable="yes">Entre  com  um  
comando...</property>
    <property name="resizable">False</property>
    <property name="modal">True</property>
    <property name="window_position">GTK_WIN_POS_CENTER</property>
    <signal name="destroy" handler="on_main_destroy"/>
    <child>
      <widget class="GtkFixed" id="fixed1">
        <property name="width_request">380</property>
        <property name="height_request">100</property>
        <property name="visible">True</property>
        <child>
          <widget class="GtkButton" id="btn_rodar">
            <property name="width_request">100</property>
            <property name="height_request">29</property>
            <property name="visible">True</property>
            <property name="can_focus">True</property>
            <property name="receives_default">True</property>
            <property name="label" translatable="yes">_Rodar</property>
            <property name="use_underline">True</property>
            <property name="response_id">0</property>
            <signal name="clicked" handler="on_btn_rodar_clicked"/>
          </widget>
          <packing>
            <property name="x">167</property>
            <property name="y">61</property>
          </packing>
        </child>

## Página 224

224 Interface Gráfica
        <child>
          <widget class="GtkButton" id="btn_fechar">
            <property name="width_request">100</property>
            <property name="height_request">29</property>
            <property name="visible">True</property>
            <property name="can_focus">True</property>
            <property name="receives_default">True</property>
            <property name="label" translatable="yes">_Fechar</property>
            <property name="use_underline">True</property>
            <property name="response_id">0</property>
            <signal name="clicked" handler="on_btn_fechar_clicked"/>
          </widget>
          <packing>
            <property name="x">272</property>
            <property name="y">61</property>
          </packing>
        </child>
        <child>
          <widget class="GtkEntry" id="ntr_cmd">
            <property name="width_request">365</property>
            <property name="height_request">29</property>
            <property name="visible">True</property>
            <property name="can_focus">True</property>
          </widget>
          <packing>
            <property name="x">9</property>
            <property name="y">14</property>
          </packing>
        </child>
        <child>
          <widget class="GtkCheckButton" id="chk_shell">
            <property name="width_request">136</property>
            <property name="height_request">29</property>
            <property name="visible">True</property>
            <property name="can_focus">True</property>
            <property name="label" translatable="yes">_Janela  de 
texto</property>
            <property name="use_underline">True</property>
            <property name="response_id">0</property>
            <property name="draw_indicator">True</property>
          </widget>
          <packing>
            <property name="x">11</property>
            <property name="y">59</property>
          </packing>
        </child>
      </widget>

## Página 225

Interface Gráfica 225
    </child>
  </widget>
</glade-interface>
Além do Glade, também existe o Gaspacho 64, outro construtor de interfaces  
que também gera arquivos XML no padrão do Glade.
wxPython
O pacote  wxPython65 é basicamente um  wrapper para o  toolkit (conjunto de  
ferramentas  e  bibliotecas)  wxWidgets,  desenvolvido  em  C++.  Principais  
características:
▪ Multi-plataforma.
▪ Look & feel (aparência e comportamento) nativo, ou seja, coerente com o  
ambiente em que está sendo executado.
▪ Grande coleção de componentes prontos.
▪ Comunidade bastante ativa.
O forma geral de funcionamento é similar ao GTK+: o  framework controla a  
interação com o usuário através de um laço que detecta eventos e ativa as  
rotinas correspondentes.
A  maneira  mais  usual  de  implementar  uma  interface  gráfica  através  do  
wxPython consiste em:
▪ Importar o pacote wx.
▪ Criar  uma  classe  de  janela  através  de  herança.  Na  inicialização  da  
classe podem ser definidos controles e  containers que fazem parte da  
janela  e  as  associações  entre  os  eventos  com  as  funções  callback 
correspondentes, que geralmente são métodos da própria classe.
▪ Criar um objeto “aplicação” usando a classe App do wxPython.
▪ Criar um objeto a partir da classe de janela.
▪ Iniciar o loop de tratamento de eventos da aplicação.
Exemplo (caixa de texto):
64 Disponível em: http://gazpacho.sicem.biz/.
65 Fontes, binários e documentação estão disponíveis em http://www.wxpython.org/.

## Página 226

226 Interface Gráfica
# -*- coding: latin1 -*-
# importa wxPython
import wx
class Main(wx.Frame):
    """
    Classe que define a janela principal do programa.
    """
    def __init__(self, parent, id, title):
        """
        Inicializa a classe.
        """
        # Define a janela usando o __init__ da classe mãe
        wx.Frame.__init__(self, parent, id, title, size=(600, 400))
        # Cria uma caixa de texto
        self.text = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        # Pega o fonte do programa (decodificado para latin1)
        font = file(__file__, 'rb').read().decode('latin1')
        
        # Carrega o fonte do programa na caixa de texto
        self.text.SetLabel(font)
        # Mostra a janela
        self.Show(True)
if __name__ == '__main__':
    # Cria um objeto "aplicação" do wxPython
    app = wx.App()
    # Cria um objeto "janela" a partir da classe
    frame = Main(None, wx.ID_ANY, 'Fonte')
    # Inicia o loop de tratamento de eventos
    app.MainLoop()
Janela do exemplo:

## Página 227

Interface Gráfica 227
Exemplo (temporizador):
# -*- coding: latin1 -*-
import wx
import time
class Main(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(150, 80))
        clock = time.asctime().split()[3]
        # Cria um rótulo de texto
        self.control = wx.StaticText(self, label=clock)
        # Muda a fonte
        self.control.SetFont(wx.Font(22, wx.SWISS, wx.NORMAL, wx.BOLD))
        # Cria um timer
        TIMER_ID = 100
        self.timer = wx.Timer(self, TIMER_ID)
        # Inicia o timer
        self.timer.Start(1000)


## Página 228

228 Interface Gráfica
        # Associa os métodos com os eventos
        wx.EVT_TIMER(self, TIMER_ID, self.on_timer)
        wx.EVT_CLOSE(self, self.on_close)
        self.Show(True)
    def on_timer(self, event):
        
        # Atualiza o relógio
        clock = time.asctime().split()[3]
        self.control.SetLabel(clock)
    def on_close(self, event):
        
        # Para o timer
        self.timer.Stop()
        self.Destroy()
app = wx.App()
Main(None, wx.ID_ANY, 'Relógio')
app.MainLoop()
Interface:
Exemplo (barra de menus):
# -*- coding: latin1 -*-
import wx
# Identificadores para as opções do menu
ID_FILE_OPEN = wx.NewId()
ID_FILE_SAVE = wx.NewId()
ID_FILE_EXIT =  wx.NewId()
ID_HELP_ABOUT =  wx.NewId()
class Main(wx.Frame):
    def __init__(self, parent, id, title):


## Página 229

Interface Gráfica 229
        wx.Frame.__init__(self, parent, id, title)
        # Cria o menu arquivo
        filemenu = wx.Menu()
        # Cria as opções
        filemenu.Append(ID_FILE_OPEN, 'Abrir arquivo...')
        filemenu.Append(ID_FILE_SAVE, 'Salvar')
        filemenu.AppendSeparator()
        filemenu.Append(ID_FILE_EXIT, 'Sair')
        # Cria o menu ajuda
        helpmenu =  wx.Menu()
        helpmenu.Append(ID_HELP_ABOUT, 'Sobre...')
        # Cria o menu
        menubar =  wx.MenuBar()
        menubar.Append(filemenu, 'Arquivo')
        menubar.Append(helpmenu, 'Ajuda')
        self.SetMenuBar(menubar)
        # Associa métodos aos eventos de menu
        wx.EVT_MENU(self, ID_FILE_OPEN, self.on_open)
        wx.EVT_MENU(self, ID_FILE_SAVE, self.on_save)
        wx.EVT_MENU(self, ID_FILE_EXIT, self.on_exit)
        wx.EVT_MENU(self, ID_HELP_ABOUT, self.about)
        # Cria uma caixa de texto
        self.control = wx.TextCtrl(self, 1,
            style=wx.TE_MULTILINE)
        self.fn = ''
    def on_open(self, evt):
        # Abre uma caixa de dialogo escolher arquivo
        dialog = wx.FileDialog(None, style=wx.OPEN)
        d = dialog.ShowModal()
        if d == wx.ID_OK:
            # Pega o arquivo escolhido
            self.fn = dialog.GetPath()
            # Muda o título da janela
            self.SetTitle(self.fn)
            # Carrega o texto na caixa de texto
            self.control.SetLabel(file(self.fn, 'rb').read())

## Página 230

230 Interface Gráfica
        dialog.Destroy()
    def on_save(self, evt):
        # Salva o texto na caixa de texto
        if self.fn:
            file(self.fn, 'wb').write(self.control.GetLabel())
    def on_exit(self, evt):
        # Fecha a janela principal
        self.Close(True)
    def about(self, evt):
        dlg = wx.MessageDialog(self,
            'Exemplo wxPython', 'Sobre...',
            wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
app = wx.App()
frame = Main(None , wx.ID_ANY, 'Isto é quase um editor...')
frame.Show(True)
app.MainLoop()
Janela principal:
Exemplo (caixa de mensagem):
# -*- coding: latin1 -*-


## Página 231

Interface Gráfica 231
import wx
class Main(wx.Frame):
    
    def __init__(self, parent, id, title):
        # Cria janela
        wx.Frame.__init__(self, parent, id, title, size=(300, 150))
        self.Centre()
        self.Show(True)
        # Cria um texto estático
        self.text = wx.StaticText(self, label='Entre com uma expressão:',
            pos=(10, 10))
        # Cria uma caixa de edição de texto
        self.edit = wx.TextCtrl(self, size=(250, -1), pos=(10, 30))
        # Cria um botão
        self.button = wx.Button(self, label='ok', pos=(10, 60))
        # Conecta um método ao botão
        self.button.Bind(wx.EVT_BUTTON, self.on_button)
    def on_button(self, event):
        # Pega o valor da caixa de texto
        txt = self.edit.GetValue()
        
        # Tenta resolver e apresentar a expressão
        try:
            wx.MessageBox(txt + ' = ' + str(eval(txt)), 'Resultado')
        
        # Se algo inesperado ocorrer
        except:
            wx.MessageBox('Expressão inválida', 'Erro')
app = wx.App()
Main(None, -1, 'Teste de MessageBox')
app.MainLoop()
Janela principal e caixa de mensagem:

## Página 232

232 Interface Gráfica
O wxPython oferece uma variedade enorme de controles prontos, que ser no  
programa de demonstração que é distribuído junto com a documentação e os  
exemplos.
PyQt
Qt66 é um toolkit desenvolvido em C++ e é utilizado por diversos programas,  
incluindo o ambiente de desktop gráfico KDE e seus aplicativos. Embora o Qt  
seja  mais  usado  para  a  criação  de  aplicativos  GUI,  ele  também  inclui  
bibliotecas  com  outras  funcionalidades,  como  acesso  a  banco  de  dados,  
comunicação de rede e controle de threads, entre outras. PyQt 67 é um binding 
que permite o uso do Qt no Python, disponível sob a licença GPL.
A  Qt  na  versão  4  possui  dois  módulos  principais,  chamados  QtGui,  que 
define as rotinas de interface, e QtCore, que define estruturas essenciais para o 
funcionamento do toolkit, como, por exemplo, os sinais (eventos).
Exemplo:
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore
class Main(QtGui.QWidget):
    """
    Janela principal
    """
66 Site oficial: http://qt.nokia.com/.
67 Site oficial: http://www.riverbankcomputing.co.uk/software/pyqt/intro.


## Página 233

Interface Gráfica 233
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        # Muda a geometria da janela
        self.setGeometry(200, 200, 200, 100)
        # Muda o título
        self.setWindowTitle('Teste')
        # Cria um botão
        quit = QtGui.QPushButton('Fechar', self)
        quit.setGeometry(10, 10, 60, 35)
        # Conecta o sinal gerado pelo botão com a função
        # que encerra o programa
        self.connect(quit, QtCore.SIGNAL('clicked()'),
            QtGui.qApp, QtCore.SLOT('quit()'))
# Cria um objeto "aplicação Qt", que trata os eventos
app = QtGui.QApplication(sys.argv)
# Cria a janela principal
qb = Main()
qb.show()
# Inicia a "aplicação Qt"
sys.exit(app.exec_())
Janela principal:
Um  dos  maiores  atrativos  do  PyQt  é  o  GUI  Builder (ferramenta  para  a  
construção  de interfaces)  Qt Designer.  Os arquivos  XML gerados  pelo Qt  
Designer (com a extensão .ui) podem ser convertidos em módulos Python  
através do utilitário pyuic.


## Página 234

234 Interface Gráfica
Para gerar o módulo Python a partir do arquivo criado no Qt Designer:
pyuic dialog.ui -o dialog.py
No qual “dialog.ui” é o arquivo de interface e “dialog.py” é o módulo.
Exemplo de arquivo gerado pelo Qt Designer (dialog.ui):
<ui version="4.0" >
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog" >
  <property name="geometry" >
   <rect>
    <x>0</x>
    <y>0</y>
    <width>116</width>
    <height>108</height>
   </rect>
  </property>
  <property name="windowTitle" >


## Página 235

Interface Gráfica 235
   <string>Dialog</string>
  </property>
  <widget class="QPushButton" name="msg" >
   <property name="geometry" >
    <rect>
     <x>20</x>
     <y>20</y>
     <width>75</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text" >
    <string>Mensagem</string>
   </property>
  </widget>
  <widget class="QPushButton" name="fim" >
   <property name="geometry" >
    <rect>
     <x>20</x>
     <y>60</y>
     <width>75</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text" >
    <string>Fechar</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections>
  <connection>
   <sender>fim</sender>
   <signal>clicked()</signal>
   <receiver>Dialog</receiver>
   <slot>close()</slot>
   <hints>
    <hint type="sourcelabel" >
     <x>57</x>
     <y>71</y>
    </hint>
    <hint type="destinationlabel" >
     <x>57</x>
     <y>53</y>
    </hint>
   </hints>
  </connection>

## Página 236

236 Interface Gráfica
 </connections>
</ui>
O  arquivo  de  interface  define  uma  janela,  da  classe  QDialog,  chamada  
“Dialog”, com dois botões, da classe QPushButton, chamados “msg” e “fim”.
Exemplo usando o módulo criado pelo Qt Designer:
# -*- coding: utf-8 -*-
import sys
import time
from PyQt4 import QtCore, QtGui
# Módulo gerado pelo pyuic
from dialog import Ui_Dialog
class Main(QtGui.QMainWindow):
    """
    Janela principal
    """
    def __init__(self, parent=None):
        """
        Inicialização da janela
        """
        QtGui.QWidget.__init__(self, parent)
        # Cria um objeto a partir da interface gerada pelo pyuic
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # Conecta o método ao botão que foi definido através do Qt Designer
        self.connect(self.ui.msg, QtCore.SIGNAL('clicked()'),
            self.show_msg)
    def show_msg(self):
        """
        Método que evoca a caixa de mensagem
        """
        reply = QtGui.QMessageBox.question(self, 'Messagem',
            'Hora: ' + time.asctime().split()[3],
            QtGui.QMessageBox.Ok)

## Página 237

Interface Gráfica 237
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Main()
    myapp.show()
    sys.exit(app.exec_())
Janela principal e caixa de mensagem:
Também  está  disponível  um  binding LGPL  similar  ao  PyQt,  chamado  
PySide68.
Outras  funcionalidades  associadas  a  interface  gráfica  podem  ser  obtidas  
usando  outros  módulos,  como  o  pySystray 69,  que  implementa  a  
funcionalidade que permite que o aplicativo use a bandeja de sistema no  
Windows.
68 Site oficial: http://www.pyside.org/.
69 Endereço na internet: http://datavibe.net/~essiene/pysystray/.


## Página 238

238 Computação Gráfica
Computação Gráfica
A Computação Gráfica (CG) é a área da Ciência da Computação que estuda a  
geração,  representação  e  manipulação  de  conteúdo  visual  em  sistemas  
computacionais e tem aplicação em várias áreas do conhecimento humano.
Simulações, por exemplo, são sistemas que empregam cálculos matemáticos  
para imitar um ou mais aspectos de um fenômeno ou processo que existe no  
mundo real. Simulações permitem entender melhor como o experimento real  
funciona e verificar cenários alternativos com outras condições.
No caso dos jogos, que na verdade são uma forma de simulação interativa  
que  faz  uso  de  recursos  visuais  para  aumentar  a  sensação  de  realismo,  
conhecida como imersão, e com isso, enriquecer a experiência do jogador.
Outra aplicação é a visualização, como dizia um antigo ditado popular: "uma  
imagem  vale  por  mil  palavas",  e  isso  é  mais  verdadeiro  ainda  quando  é 
necessário  interpretar  grandes  quantidades  de  dados,  como  acontece  em  
diversas atividades cientificas, médicas e de engenharia.
Áreas como geografia, cartografia e geologia demandam por GIS ( Geographic  
Information Systems / Sistemas de Informações Geográficas), que representam  
topologias e dados associados, tais como altura, umidade e outros.
A  engenharia  e  atividades  afins  usam  ferramentas  CAD  (Computer  Aided  
Design /  Projeto  Assistido  por  Computador)  para  facilitar  a  criação  de  
desenhos técnicos para componentes ou peças de maquinaria.
Além  disso,  várias  formas  de  arte  se  beneficiam  da  CG,  como  o  cinema, 
principalmente para a criação de efeitos especiais. A CG também permitiu o  
surgimento novas formas de arte, que usam um ambiente digital como mídia,  
como por exemplo a animação em três dimensões (3D).
Matrizes versus vetores
É muito comum representar uma informação visual em forma bidimensional  
(2D), seja em fotos, gráficos impressos ou em uma tela de LCD. Existem duas  

## Página 239

Computação Gráfica 239
formas  para  a  representação  de  imagens  bidimensionais  amplamente  
utilizadas, cada qual com suas vantagens e desvantagens.
A primeira é matricial, também conhecida como mapa de  bits ( bitmap) ou  
raster, na qual a imagem é representada como uma matriz bidimensional de  
pontos  com  informações  sobre  cor,  chamados  de  elementos  de  imagem  
(picture  element ,  geralmente  abreviado  como  pixel).  Esta  forma  requer  
algoritmos  sofisticados  para  ser  manipulada  e  armazenada,  devido  ao  
volume de dados, e a complexidade das operações, como interpolar valores  
durante um redimensionamento, por exemplo.
A segunda forma de representação são as imagens vetoriais, que são descritas 
através  de  entidades  matemáticas  que  compõem  a  geometria  da  imagem  
(linhas, polígonos, texto e outros). Esta forma é menos exigente em termos de  
recursos  computacionais  e  não  apresenta  problemas  associados  a  
redimensionamento, porém não permite muitas operações que o mapa de bits 
viabiliza.
Entre outras formas de representação, é interessante destacar os fractais, em  
que as imagens são geradas através de algoritmos que são aplicados de forma  
(102, 153, 102)
A imagem é 
composta por pixels 
com uma cor 
associada.
Geralmente as cores 
são representadas 
em RGB (Red, Green 
e Blue).
(102, 153, 153)
(102, 153, 204)
(51, 102, 153)

## Página 240

240 Computação Gráfica
recursiva.
Estas formas de representação levaram ao surgimento de vários formatos de  
arquivo para armazenamento de imagens, inclusive abertos,  como o PNG  
(Portable Network  Graphics ), que suporta  imagens  raster, com transparência  
inclusive, e o SVG (Scalable Vectorial Graphics ), para imagens vetoriais, mapas  
de bits e até animações. Ambos são homologados pelo W3C ( World Wide Web  
Consortium).
Existem hoje várias bibliotecas voltadas para CG disponíveis para Python,  
que estão em estado avançado de maturidade.
Mapa de bits
 Vetorial

## Página 241

Processamento de imagem 241
Processamento de imagem
Python Imaging Library 70 (PIL) é uma biblioteca de processamento de imagens  
matriciais para Python.
PIL possui módulos que implementam:
▪ Ferramentas para cortar, redimensionar e mesclar imagens.
▪ Algoritmos de conversão, que suportam diversos formatos.
▪ Filtros, tais como suavizar, borrar e detectar bordas.
▪ Ajustes, incluindo brilho e contraste.
▪ Operações com paletas de cores.
▪ Desenhos simples em 2D.
▪ Rotinas  para  tratamento  de  imagens:  equalização,  auto-contraste,  
deformar, inverter e outras.
Exemplo de tratamento de imagem:
# -*- coding: latin-1 -*-
"""
Cria miniaturas suavizadas para cada
JPEG na pasta corrente
"""
import glob
# Módulo principal do PIL
import Image
# Módulo de filtros
import ImageFilter
# Para cada arquivo JPEG
for fn in glob.glob("*.jpg"):
    # Retorna o nome do arquivo sem extensão
    f = glob.os.path.splitext(fn)[0]
    print 'Processando:', fn
    imagem = Image.open(fn)
70 Documentação,  fontes  e  binários  disponíveis  em:  
http://www.pythonware.com/products/pil/.

## Página 242

242 Processamento de imagem
    # Cria thumbnail (miniatura) da imagem
    # de tamanho 256x256 usando antialiasing
    imagem.thumbnail((256, 256), Image.ANTIALIAS)
    # Filtro suaviza a imagem
    imagem = imagem.filter(ImageFilter.SMOOTH)
    # Salva como arquivo PNG
    imagem.save(f + '.png', 'PNG')
Exemplo de desenho:
# -*- coding: latin-1 -*-
"""
Cria uma imagem com vários gradientes de cores
"""
import Image
# Módulo de desenho
import ImageDraw
# Largura e altura
l, a = 512, 512
# Cria uma imagem nova com fundo branco
imagem = Image.new('RGBA', (l, a), 'white')
# O objeto desenho age sobre o objeto imagem
desenho = ImageDraw.Draw(imagem)
# Calcula a largura da faixa de cor
faixa = l / 256
# Desenha um gradiente de cor
for i in xrange(0, l):
    # Calcula a cor da linha
    rgb = (0.25 * i / faixa, 0.5 * i / faixa, i / faixa)
    cor = '#%02x%02x%02x' % rgb
    # Desenha uma linha colorida
    # Primeiro argumento é uma tupla com
    # as coordenadas de inicio e fim da linha

## Página 243

Processamento de imagem 243
    desenho.line((0, i, l, i), fill=cor)
# Copia e cola recortes invertidos do gradiente
for i in xrange(l, l / 2, -l / 10):
    # Tamanho do recorte
    area = (l - i, a - i, i, i)
    # Copia e inverte
    flip = Image.FLIP_TOP_BOTTOM
    recorte = imagem.crop(area).transpose(flip)
    # Cola de volta na imagem original
    imagem.paste(recorte, area)
# Salva como arquivo PNG
imagem.save('desenho.png', 'PNG')
Arquivo de saída “desenho.png”:
É possível calcular os dados da imagem com o NumPy e usar o PIL para  
gerar a imagem real.
Exemplo com modulação de amplitude de onda:
# -*- coding: latin1 -*-
"""
Criando uma imagem usando NumPy
"""


## Página 244

244 Processamento de imagem
import numpy
import Image
def coords(xy, tam):
    """
    coords(xy, tam) => x, y
    Transforma as coordenadas normalizadas
    para o centro da imagem de tamanho "tam"
    """
    X, Y = tam
    x = int((1. + xy[0]) * (X - 1.) / 2.)
    y = int((1. + xy[1]) * (Y - 1.) / 2.)
    return x, y
if __name__ == '__main__':
    # Dimensões
    tam = 900, 600
    # Cria um arranjo apenas com zeros
    # com as dimensões transpostas
    # "tam[::-1]" é o reverso de "tam" e 
    # "(3,)" é uma tupla para representar "(R, G, B)"
    imag = numpy.zeros(tam[::-1] + (3,), numpy.uint8)
    # Preenche de branco
    imag.fill(255)
    # Dados do eixo X
    xs = numpy.arange(-1., 1., 0.00005)
    # Onda moduladora
    # Valor médio, amplitude e freqüência
    vmed = 0.6
    amp = 0.4
    fm = 2.
    mod = vmed + amp * numpy.cos(fm * numpy.pi * xs)
    # Frequência da portadora
    fc = 8.
    # Número de curvas internas
    ci = 32.
    # Contador
    i = 0
    # Gera um conjunto de curvas

## Página 245

Processamento de imagem 245
    for delta_y in numpy.arange(1. / ci, 1. + 1. / ci,
        1. / ci):
        # Dados do eixo Y
        ys = mod * delta_y * numpy.sin(fc * numpy.pi * xs)
        # Pares x, y
        xys = zip(xs, ys)
        # Desenha a portadora e as curvas internas
        # Para cada ponto na lista
        for xy in xys:
            # Coordenadas invertidas
            x, y = coords(xy, tam)[::-1]
            # Aplica cor a xy
            imag[x, y] = (250 - 100 * delta_y,
                150 - 100 * delta_y,
                50 + 100 * delta_y)
            i += 1
    for x, y in zip(xs, mod):
        # Desenha as envoltórias
        imag[coords((x, y), tam)[::-1]] = (0, 0, 0)
        imag[coords((x, -y), tam)[::-1]] = (0, 0, 0)
        # Bordas superior e inferior
        imag[coords((x, 1.), tam)[::-1]] = (0, 0, 0)
        imag[coords((x, -1.), tam)[::-1]] = (0, 0, 0)
        i += 4
    for y in xs:
        # Bordas laterais
        imag[coords((1., y), tam)[::-1]] = (0, 0, 0)
        imag[coords((-1., y), tam)[::-1]] = (0, 0, 0)
        i += 2
    print i, 'pontos calculados'
    # Cria a imagem a partir do arranjo
    imagem = Image.fromarray(imag, 'RGB')
    imagem.save('curvas.png', 'PNG')
Arquivo de saída “curvas.png”:

## Página 246

246 Processamento de imagem
Observações:
▪ A biblioteca trabalha com o conceito de bandas, que são camadas que  
compõem a imagem. Cada imagem pode ter várias bandas, mas todas  
devem ter as mesmas dimensões e profundidade.
▪ A origem do sistema de coordenadas é no canto superior esquerdo.
Além do PIL, também possível usar o ImageMagick 71 com Python. Com uma  
proposta diferente, ImageMagick é um conjunto de utilitários para processar  
imagens  raster, feito basicamente para uso através de linha de comando ou  
através de linguagens de programação.
71 Site oficial: http://www.imagemagick.org/.


## Página 247

SVG 247
SVG
SVG72 ( Scalable Vector Graphics ) é um formato aberto, baseado no XML, que  
descreve imagens vetoriais, na forma de estruturas compostas por instruções  
de alto nível que representam primitivas geométricas. O formato foi proposto  
pelo W3C ( World Wide Web Consortium ), a entidade que define os padrões  
vigentes na Internet, como o HTML e o próprio XML.
Arquivos  SVG podem  armazenar  vários  tipos  de  informações  vetoriais,  
incluindo polígonos básicos, que são representados por linhas que delimitam  
uma  área  fechada,  tais  como  retângulos,  elipses  e  outras  formas  simples. 
Além  disso,  ele  também  suporta  caminhos  ( paths),  que  são  figuras,  com  
preenchimento  ou  não,  compostas  por  linhas  e/ou  curvas  definidas  por  
pontos,  que  são  codificados  através  de  comandos  de  um  caractere  (“L”  
significa “Line To”, por exemplo) e um par de coordenadas X e Y, o que gera  
um código muito compacto.
Texto unicode pode ser incluído em um arquivo SVG, com efeitos visuais, e a  
72 Página oficial: http://www.w3.org/Graphics/SVG/.
Imagem gerada a partir 
das instruções que 
descrevem os objetos.
Arquivo SVG 
original.

## Página 248

248 SVG
especificação  inclui  tratamento  de  texto  bidirecional,  vertical  e  seguindo  
caminhos curvos. O texto pode ser formatadas com fontes de texto externas,  
mas para amenizar o problema do texto não ser apresentado corretamente em 
sistemas diferentes, existe uma fonte interna, que está sempre disponível.
As figuras geométricas, caminhos e texto podem ser usados como contornos,  
internos ou externos, que pode usar três tipos de preenchimento:
▪ Cores sólidas, que podem ser opacas ou com transparência.
▪ Gradientes, que podem ser lineares ou radiais.
▪ Padrões, que são imagens bitmap ou vetoriais que se repetem ao longo  
do objeto.
Tantos os gradientes quantos os padrões podem ser animados.
O  SVG também permite que o autor inclua metadados com informações a  
respeito da imagem, tais como título, descrição e outros, com o objetivo de  
facilitar a catalogação, indexação e recuperação dos arquivos.
Todos os componentes de um arquivo SVG pode ser lidos e alterados usando  
scripts  da  mesma  forma  que  o  HTML,  tendo  como  padrão  a  linguagem  
ECMAScript. A especificação também prevê tratamento de eventos de mouse  
e teclado, o que, junto com  hyperlinks, permite adicionar interatividade aos  
gráficos.
O  formato  também  suporta  animação  através  do  ECMAScript,  que  pode 
transformar  os  elementos  da  imagem  e  temporizar  o  movimento.  Isso  
também poder ser feito através de recursos próprios do SVG, usando tags.
Para o  SVG, filtros são conjuntos de operações gráficas que são aplicadas a  
um determinado gráfico vetorial, para produzir uma imagem matricial com o 
resultado.  Tais  operações  gráficas  são  chamadas  primitivas  de  filtro,  que  
geralmente realizam uma forma de processamento de imagem, como, por  
exemplo,  o  efeito  Gaussian  Blur ,  e  por  isso,  geram  um  bitmap com  
transparência (padrão RGBA) como saída, que é regerado se necessário. O  
resultado  de  uma  primitiva  pode  ser  usado  como  entrada  para  outra  
primitiva, permitindo a concatenação de várias para gerar o efeito desejado.

## Página 249

SVG 249
SVGFig
Os arquivos  SVG podem manipulados através de bibliotecas XML, como o  
ElementTree, mas é mais produtivo usar componentes que já projetados com  
essa  finalidade.  O  SVGFig é  um  módulo  para  SVG com  muitos  recursos  
prontos.  O  módulo  permite  tanto  usar  as primitivas  de  desenho  do  SVG 
diretamente, como também rotinas próprias de alto nível.
Exemplo (usando primitivas do SVG):
# -*- coding: latin1 -*-
# Importa SVGFig
from svgfig import *
cores = ['#dddddd', '#306090', '#609030', '#906030']
# Um retângulo usando SVG
# x, y  -> posição do canto superior esquerdo
# width, height -> tamanho
# fill -> cor do preenchimento
# opacity -> opacidade (1.0 = 100%)
# stroke_width -> largura da linha (em pontos)
q1 = SVG('rect', x=0, y=0, width=100, height=100,
    fill=cores[0],  opacity='1.0', stroke_width='0.2pt')
# Primeiro círculo
# cx, cy -> posição do centro
# r -> raio
c1 = SVG('circle', cx=35, cy=65, r=30,
    fill=cores[1],  opacity='0.5', stroke_width='0.2pt')
# Segundo círculo
c2 = SVG('circle', cx=65, cy=65, r=30,
    fill=cores[2],  opacity='0.5', stroke_width='0.2pt')
# Terceiro círculo
c3 = SVG('circle', cx=50, cy=35, r=30,
    fill=cores[3],  opacity='0.5', stroke_width='0.2pt')
# Criando um grupo com as figuras
g = SVG('g', q1, c1, c2, c3)
# Salvando
g.save("tmp.svg")

## Página 250

250 SVG
Saída (arquivo SVG):
<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC  "-//W3C//DTD  SVG 1.1//EN"  
"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg style="stroke-linejoin:round;  stroke:black;  stroke-width:0.5pt;  text-
anchor:middle;  fill:none"  xmlns="http://www.w3.org/2000/svg" font-
family="Helvetica, Arial, FreeSans, Sans, sans, sans-serif"  height="400px" 
width="400px" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" 
viewBox="0 0 100 100">
<g>
<rect opacity="1.0" height="100" width="100" y="0" x="0" stroke-
width="0.2pt" fill="#dddddd" />
<circle opacity="0.5" stroke-width="0.2pt" cy="65" cx="35" r="30" 
fill="#306090" />
<circle opacity="0.5" stroke-width="0.2pt" cy="65" cx="65" r="30" 
fill="#609030" />
<circle opacity="0.5" stroke-width="0.2pt" cy="35" cx="50" r="30" 
fill="#906030" />
</g>
</svg>
Saída (gráfico):


## Página 251

SVG 251
Exemplo (com rotinas do SVGFig):
# -*- coding: latin1 -*-
from math import sin, cos, pi
from svgfig import *
# Cria uma curva para t = seno(2t) / 2 + cosseno(3t)
# de -2Pi a 2 Pi, da cor #ccbbaa
curva = Curve('t, 0.5 * sin(2*t) + cos(3*t)',
    -2*pi, 2*pi, stroke='#ccbbaa')
# Gera um gráfico com eixos
# X (-2Pi a 2Pi) e Y (-2 a 2) com a curva
grafico = Plot(-2*pi, 2*pi, -2, 2, curva)
# Cria um objeto SVG
svg = grafico.SVG()
# Salva em um arquivo
svg.save("tmp.svg")
Saída (gráfico):
O  SVGFig tem várias  primitivas  de desenho  implementadas  na forma de  
funções, incluindo caminhos (Path()), linhas (Line()) e texto (Text()).


## Página 252

252 Imagens em três dimensões
Imagens em três dimensões
Os  formatos  matricial e  vetorial  representam  imagens  bidimensionais  no  
computador de forma adequada para a maior parte das aplicações. Porém,  
elas são limitadas em vários aspectos, principalmente para simulações, pois  
mundo que vivemos tem três dimensões (3D).
Uma cena 3D é composta por objetos, que representam sólidos, fontes de luz  
e  câmeras.  Os  objetos  sólidos  geralmente  são  representados  por  malhas  
(meshes), que são conjunto de pontos (vértices). Estes possuem coordenadas x,  
y  e  z.  Os  pontos  são  interligados  por  linhas  (arestas)  que  formam  as  
superfícies  (faces)  dos  objetos.  Conjuntos  de  linhas  que  representam  as  
malhas são chamados de estruturas de arame (wireframes).
Objetos  podem  usar  um  ou  mais  materiais  e  estes  podem  ter  várias  
características, tais como cor, transparência e sombreamento, que é a forma  
como o material responde a iluminação da cena. Além disso, o material pode  
ter uma ou mais texturas associadas.
Objetos
CâmeraFonte de luz

## Página 253

Imagens em três dimensões 253
Texturas  são  compostas  por  imagens  de  duas  dimensões  que  podem  ser  
usadas nos materiais aplicados as superfícies dos objetos, alterando várias  
propriedades,  tais  como  reflexão,  transparência  e  enrugamento  (bump)  da 
superfície.
Em uma cena 3D, os objetos podem modificados através de transformações,  
tais como translação (mover de uma posição para outra), rotação (girar em  
torno de um eixo) e redimensionamento (mudar de tamanho em uma ou mais 
dimensões).
Para renderizar, ou seja, gerar a imagem final, é necessário fazer uma série de  
cálculos complexos para aplicar iluminação e perspectiva aos objetos da cena.  
Entre os algoritmos usados para renderização, um dos mais conhecidos é o  
chamado  raytrace, no qual os raios de luz são calculados da câmera até as  
fontes de luz. Com isso, são evitados cálculos desnecessários dos raios que  
não chegam até a câmera.
Um dos usos mais populares da tecnologia 3D é em animações. A técnica  
mais comum de animação em 3D é chamada de keyframe. Nela, o objeto a ser  
animado  é  posicionado  em  locais  diferentes  em  momentos  chave  da  
animação, e o software se encarrega de calcular os quadros intermediários.
Muitos aplicativos 3D utilizam bibliotecas que implementam a especificação  
OpenGL ( Open  Graphics  Library ),  que  define  uma  API  independente  de  
plataforma e de linguagem, para a manipulação de gráficos 3D, permitindo a  
Estrutura de arame Sólido Imagem final

## Página 254

254 Imagens em três dimensões
renderização em tempo real acelerada por  hardware. Sua característica mais  
marcante é a performance. Mesa 3D73 é a implementação livre mais conhecida 
e está amplamente disponível em distribuições de Linux e BSD.
VPython
VPython74 é um pacote que permite criar e animar modelos simples em três  
dimensões. Seu objetivo é facilitar a criação rápida de simulações e protótipos  
que não requerem soluções complexas.
O VPython provê iluminação, controle de câmera e tratamento de eventos de  
mouse  (rotação  e  zoom)  automaticamente.  Os  objetos  podem  ser  criados  
interativamente no interpretador, que a janela 3D do VPython é atualizada de 
acordo.
Exemplo:
# -*- coding: latin-1 -*-
"""
Hexaedro
"""
# VPython
import visual
# Coordenadas para os vértices e arestas
coords = (-3, 3)
# Cor do vértice
cor1 = (0.9, 0.9, 1.0)
# Cor da aresta
cor2 = (0.5, 0.5, 0.6)
# Desenha esferas nos vértices
for x in coords:
    for y in coords:
        for z in coords:
            # pos é a posição do centro da esfera
            visual.sphere(pos=(x, y, z), color=cor1)
73 Página oficial: http://www.mesa3d.org/.
74 Documentação, fontes e binários para instalação em: http://www.vpython.org/.

## Página 255

Imagens em três dimensões 255
# Desenha os cilindros das arestas
for x in coords:
    for z in coords:
        # pos é a posição do centro da base do cilindro
        # radius é o raio da base do cilindro
        # axis é o eixo do cilindro
        visual.cylinder(pos=(x, 3, z), color=cor2,
            radius=0.25, axis=(0, -6, 0))
    for y in coords:
        visual.cylinder(pos=(x, y, 3), color=cor2,
            radius=0.25, axis=(0, 0, -6))
for y in coords:
    for z in coords:
        visual.cylinder(pos=(3, y, z), color=cor2,
            radius=0.25, axis=(-6, 0, 0))
Janela 3D:
Os objetos 3D do  VPython podem ser agrupados em quadros ( frames), que  
podem ser movidos e rotacionados.
É possível animar os objetos 3D usando laços. Para controlar a velocidade da  
animação, o VPython provê a função rate(), que pausa animação pelo inverso  
do argumento em segundos.


## Página 256

256 Imagens em três dimensões
Exemplo de quadro e animação:
# -*- coding: latin-1 -*-
"""
Octaedro animado
"""
from visual import *
# Cores
azul = (0.25, 0.25, 0.50)
verde = (0.25, 0.50, 0.25)
# Eixo de rotação
eixo = (0, 1, 0)
# Cria um frame alinhado com o eixo de rotação
fr = frame(axis=eixo)
# O fundo da caixa
box(pos=(0, -0.5, 0), color=azul,
    size=(10.0, 0.5, 8.0))
# O bordas da caixa
box(pos=(0, -0.5, 4.0), color=azul,
    size=(11.0, 1.0, 1.0))
box(pos=(0, -0.5, -4.0), color=azul,
    size=(11.0, 1.0, 1.0))
box(pos=(5.0, -0.5, 0), color=azul,
    size=(1.0, 1.0, 8.0))
box(pos=(-5.0, -0.5, 0), color=azul,
    size=(1.0, 1.0, 8.0))
# O pião
py1 = pyramid(frame=fr, pos=(1, 0, 0), color=verde,
    axis=(1, 0, 0))
py2 = pyramid(frame=fr, pos=(1, 0, 0), color=verde,
    axis=(-1, 0, 0))
# O pião anda no plano y = 0
delta_x = 0.01
delta_z = 0.01
print fr.axis

## Página 257

Imagens em três dimensões 257
while True:
    # Inverte o sentido em x
    if abs(fr.x) > 4.2:
        delta_x = -delta_x
    # Inverte o sentido em z
    if abs(fr.z) > 3.1:
        delta_z = -delta_z
    fr.x += delta_x
    fr.z += delta_z
    # Rotaciona em Pi / 100 no eixo
    fr.rotate(angle=pi / 100, axis=eixo)
    # Espere 1 / 100 segundos
    rate(250)
Janela 3D:
O pacote inclui também um módulo de plotagem de gráficos, chamado graph.
Exemplo:
# -*- coding: latin1 -*-


## Página 258

258 Imagens em três dimensões
# Módulo para plotagem de gráficos
from visual.graph import *
# Gráfico de linha simples
g1 = gcurve(color=(.8, .6, .3))
# Gráfico de barras
g2 = gvbars(delta=0.02, color=(.6, .4, .6))
# Limites do eixo X do gráfico
for x in arange(0., 10.1, .1):
    # plot() recebe X e Y
    # Plotando a curva
    g1.plot(pos=(x, 3 * sin(x) + cos(5 * x)))
    # Plotando as barras
    g2.plot(pos=(x, tan(x) * sin(4 * x)))
Janela de saída:
Na versão 5, o VPython passou a incluir recursos como materiais prontos  
(como madeira, por exemplo) e controle de opacidade.
Exemplo:


## Página 259

Imagens em três dimensões 259
# -*- coding: latin1 -*-
from visual import *
# Define posição inicial da câmera
scene.forward = (-0.1, -0.1, -0.1)
# Limpa a iluminação
scene.lights = []
# Define a iluminação ambiente
scene.ambient = (.1, .1, .2)
# Uma caixa de madeira
box(material=materials.wood)
# Uma esfera de material semi-transparente
sphere(radius=.2, pos=(-1, -0.3, 1), color=(.4, .5, .4),
    material=materials.rough, opacity=.5)
# Uma textura xadrez
x = 2 * (2 * (1, 0), 2 * (0, 1))
# Define a textura nova
mat = materials.texture(data=x, interpolate=False,
    mapping='rectangular')
# Caixa com a nova textura
box(axis=(0, 1, 0), size=(4, 4, 4), pos=(0, -3, 0), material=mat)
# A lâmpada é um frame composto por uma esfera e uma fonte de luz
c = (1., .9, .8)
lamp = frame(pos=(0, 1, 0))
# Define uma fonte de luz
local_light(frame=lamp, pos=(2, 1, 0), color=c)
# Define uma esfera com material emissor
sphere(frame=lamp, radius=0.1, pos=(2, 1, 0),
            color=c, material=materials.emissive)
while True:
    # Anima a lâmpada, rotacionando em torno do eixo Y
    lamp.rotate(axis=(0, 1, 0), angle=.1)
    rate(10)
Janela de saída:

## Página 260

260 Imagens em três dimensões
O  VPython tem  várias  limitações.  Ele  não  provê  formas  de  criar  e/ou  
manipular materiais ou texturas mais complexas, nem formas avançadas de  
iluminação  ou  detecção  de  colisões.  Para  cenas  mais  sofisticadas,  existem 
outras soluções, como o Python Ogre 75 e o  Blender, que é um aplicativo de  
modelagem 3D que usa Python como linguagem script.
PyOpenGL
As  bibliotecas  OpenGL76 implementam  uma  API  de  baixo  nível  para  
manipulação de imagens 3D, permitindo o acesso aos recursos disponíveis no  
hardware de vídeo, e também torna o código independente da plataforma,  
pois emula por software as funcionalidades que não estiverem disponíveis no  
equipamento.  Entre  esses  recursos  temos:  primitivas  (linhas  e  polígonos),  
mapeamento de texturas, operações de transformação e iluminação.
A OpenGL funciona em um contexto, que tem seu estado alterado através das 
funções definidas na especificação. Este estado é mantido até que sofra uma  
nova alteração.
Complementando a biblioteca principal, a  OpenGL Utility  Library  (GLU)  é  
uma biblioteca com funções de alto nível, enquanto a OpenGL Utility Toolkit  
(GLUT) define rotinas independentes de plataforma para gerenciamento de  
janelas, entrada e contexto.
A  GLUT  é  orientada  a  eventos,  aos  quais  é  possível  se  associar  funções  
75 Disponível em: http://python-ogre.org/.
76 Documentação em http://www.opengl.org/.


## Página 261

Imagens em três dimensões 261
callback, que executam as chamadas  OpenGL. A biblioteca tem uma rotina  
que monitora os eventos e evoca as funções quando necessário.
PyOpenGL77 é um pacote que permite que programas em Python utilizem as  
bibliotecas OpenGL, GLU e GLUT.
Exemplo:
# -*- coding: latin1 -*-
from sys import argv
from OpenGL.GL import *
from OpenGL.GLUT import *
def display():
    """
    Função callback que desenha na janela
    """
    
    # glClear limpa a janela com valores pré-determinados
    # GL_COLOR_BUFFER_BIT define que o buffer aceita escrita de cores
    # GL_DEPTH_BUFFER_BIT define que o buffer de profundidade será usado
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    rgba = [.8, .6, .4, .9]
    # glMaterial especifica os parâmetros do material que serão
    # usados no modelo de iluminação da cena (no formato RGBA)
    # GL_FRONT define que a face afetada pela função é a frontal
    # GL_AMBIENT especifica que o parâmetro é a reflexão de ambiente
    glMaterialfv(GL_FRONT, GL_AMBIENT, rgba)
    # GL_DIFFUSE especifica que o parâmetro é a reflexão difusa do material
    glMaterialfv(GL_FRONT, GL_DIFFUSE, rgba)
    # GL_SPECULAR especifica que o parâmetro é a reflexão especular
    glMaterialfv(GL_FRONT, GL_SPECULAR, rgba)
    # GL_EMISSION especifica que o parâmetro é a emissão do material
    # glMaterialfv(GL_FRONT, GL_EMISSION, rgba)
    # GL_SHININESS especifica o expoente usado pela reflexão especular
    glMaterialfv(GL_FRONT, GL_SHININESS, 120)
77 Página oficial do projeto: http://pyopengl.sourceforge.net/.

## Página 262

262 Imagens em três dimensões
    # Desenha uma esfera sólida, com raio 0.5 e 128 divisões
    # na horizontal e na vertical
    glutSolidSphere(0.5, 128, 128)
    # Força a execução dos comandos da OpenGL
    glFlush()
#  Inicializa a biblioteca GLUT
glutInit(argv)
# glutInitDisplayMode configura o modo de exibição
# GLUT_SINGLE define o buffer como simples
# (também pode ser duplo, com GLUT_DOUBLE)
# GLUT_RGB seleciona o modo RGB
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
# Cria a janela principal
glutCreateWindow('Esfera')
# Configura a função callback que desenha na janela atual
glutDisplayFunc(display)
# Limpa a janela com a cor especificada
glClearColor(.25, .15, .1, 1.)
# Muda a matriz corrente para GL_PROJECTION
glMatrixMode(GL_PROJECTION)
# Carrega uma matriz identidade na matriz corrente
glLoadIdentity()
# Configurando os parâmetros para as fontes de luz
# GL_DIFFUSE define o parâmetro usado a luz difusa (no formato RGBA)
glLightfv(GL_LIGHT0, GL_DIFFUSE, [1., 1., 1., 1.])
# Os três parâmetros definem a posição da fonte luminosa
# O quarto define se a fonte é direcional (0) ou posicional (1)
glLightfv(GL_LIGHT0, GL_POSITION, [-5., 5., -5., 1.])
# Aplica os parâmetros de iluminação
glEnable(GL_LIGHTING)
# Inclui a fonte de luz 0 no calculo da iluminação
glEnable(GL_LIGHT0)
# Inicia o laço de eventos da GLUT
glutMainLoop()

## Página 263

Imagens em três dimensões 263
Saída:
A biblioteca também oferece rotinas para fazer transformações, o que permite  
animar os objetos da cena.
Exemplo:
# -*- coding: latin1 -*-
from sys import argv
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
# Ângulo de rotação do objeto
ar = 0.
# Variação da rotação
dr = 1.
def resize(x, y):
    """
    Função callback que é evocada quando
    a janela muda de tamanho
    """


## Página 264

264 Imagens em três dimensões
    # Limpa a vista
    glViewport(0, 0, x, y)
    # Seleciona a matriz de projeção
    glMatrixMode(GL_PROJECTION)
    # Limpa a matriz de projeção
    glLoadIdentity()
    
    # Calcula o aspecto da perspectiva
    gluPerspective(45., float(x)/float(y), 0.1, 100.0)
    
    # Seleciona a matriz de visualização
    glMatrixMode(GL_MODELVIEW)
def draw():
    """
    Função que desenha os objetos
    """
    global ar, dr
    # Limpa a janela e o buffer de profundidade
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # Limpa a matriz de visualização
    glLoadIdentity()
    # Move o objeto (translação)
    # Parâmetros: x, y e z (deslocamento)
    glTranslatef(-0.5, -0.5, -4.)
    # Rotação (em graus)
    # Parâmetros: graus, x, y e z (eixo)
    glRotatef(ar, 1.0 , 1.0, 1.0)
    # Mudança de escala
    # Parâmetros: x, y e z (tamanho)
    glScalef(ar  / 1000, ar / 1000, ar / 1000)
    for i in xrange(0, 360, 10):
        # Rotação das faces do objeto
        glRotatef(10, 1.0 , 1.0, 1.0)
        # Inicia a criação de uma face retangular
        glBegin(GL_QUADS)

## Página 265

Imagens em três dimensões 265
        # Define a cor que será usada para desenhar (R, G, B)
        glColor3f(.7, .5, .1)
        # Cria um vértice da face
        glVertex3f(0., 0., 0.)
        glColor3f(.7, .3, .1)
        glVertex3f(1., 0., 0.)
        glColor3f(.5, .1, .1)
        glVertex3f(1., 1., 0.)
        glColor3f(.7, .3, .1)
        glVertex3f(0., 1., 0.)
        # Termina a face
        glEnd()
    # Inverte a variação
    if ar > 1000: dr = -1
    if ar < 1: dr = 1
    ar  = ar + dr
    #  Troca o buffer, exibindo o que acabou de ser usado
    glutSwapBuffers()
def keyboard(*args):
    """
    Função callback para tratar eventos de teclado
    """
    # Testa se a tecla ESC foi apertada
    if args[0] == '\33': 
        raise SystemExit
if __name__ == '__main__':
    # Inicializa a GLUT
    glutInit(argv)
    # Seleciona o modo de exibição
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    # Configura a resolução da janela do GLUT de 640 x 480
    glutInitWindowSize(640, 480)
    # Cria a janela do GLUT
    window = glutCreateWindow('Transformações')
    # Configura a função callback que desenha na janela atual

## Página 266

266 Imagens em três dimensões
    glutDisplayFunc(draw)
    # Para exibir em tela cheia
    #glutFullScreen()
    # Registra a função para tratar redesenhar a janela quando
    # não há nada a fazer
    glutIdleFunc(draw)
    # Registra a função para redesenhar a janela quando
    # ela for redimensionada
    glutReshapeFunc(resize)
    # Registra a função para tratar eventos de teclado
    glutKeyboardFunc(keyboard)
    # Inicialização da janela
    # Limpa a imagem (fundo preto)
    glClearColor(0., 0., 0., 0.)
    # Limpa o buffer de profundidade
    glClearDepth(1.)
    
    # Configura o tipo do teste de profundidade
    glDepthFunc(GL_LESS)
    # Ativa o teste de profundidade
    glEnable(GL_DEPTH_TEST)
    # Configura o sombreamento suave
    glShadeModel(GL_SMOOTH)
    # Seleciona a matriz de projeção
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45., 640. / 480., .1, 100.)
    # Seleciona a matriz de visualização
    glMatrixMode(GL_MODELVIEW)
    # Inicia o laço de eventos da GLUT
    glutMainLoop()
Janela de saída:

## Página 267

Imagens em três dimensões 267
A OpenGL pode ser integrada com toolkits gráficos, como wxWidgets e Qt, ao 
invés  de  usar  a  GLUT,  e  com  isso,  ser  incorporada  em  aplicações  GUI  
convencionais.
Uma  das  principais  referências  sobre  OpenGL  é  o  livro  “OpenGL  
Programming Guide”, também conhecido como “Red Book”78.
78 Versão online disponível em http://www.glprogramming.com/red/.


## Página 268

268 Processamento distribuído
Processamento distribuído
Geralmente  a  solução  para  problemas  que  requerem  muita  potência  
computacional  é  a  utilização  de  máquinas  mais  poderosas,  porém  esta  
solução é limitada em termos de escalabilidade. Uma alternativa é dividir os  
processos da aplicação entre várias máquinas que se comunicam através de  
uma rede, formando um cluster ou um grid.
A diferença básica entre cluster e grid é que o primeiro tem como premissa de  
projeto  ser  um ambiente controlado,  homogêneo e previsível,  enquanto o  
segundo é geralmente heterogêneo, não controlado e imprevisível. Um cluster 
é um ambiente planejado especificamente para processamento distribuído,  
com máquinas dedicadas em um lugar adequado. Um grid se caracteriza pelo 
uso de estações de trabalho que podem estar em qualquer lugar.
Os modelos mais comuns de cluster:
▪ computacional.
▪ de recursos.
▪ de aplicação ou híbrido.
Híbrido
A
 B
C
 D
Computacional
A
 B
C
 D
O servidor faz o 
escalonamento das tarefas 
para as estações.
Qualquer máquina pode 
atuar como cliente e 
servidor.

## Página 269

Processamento distribuído 269
O modelo computacional tem como objetivo usar processadores e memória  
dos  equipamentos  envolvidos  para  obter  mais potência computacional.  A  
implementação  geralmente  utiliza  um  sistema  escalonador  de  filas  
(metascheduler), que realiza o agendamento das tarefas a serem processadas  
pelos nós (máquinas que compõem o modelo), com isso a operação tende a  
ser  contínua,  com  interação  reduzida  com  os  usuários.  Um  exemplo  
conhecido é o SETI@home79.
O cluster de recursos é usado para armazenar informações em um grupo de  
computadores, tanto para obter mais performance de recuperação de dados  
quanto para expandir a capacidade de armazenamento. Este modelo pode ser  
usado para prover infra-estrutura para aplicações ou para atender requisições 
feitas de forma interativa por usuários. Entre os serviços que podem operar  
desta forma estão os Sistemas Gerenciadores  de Banco de Dados (SGBD),  
como o MySQL Cluster80.
O modelo híbrido é uma aplicação projetada especificamente para funcionar  
79 Página do projeto em: http://setiathome.berkeley.edu/.
80 Endereço na internet: http://www.mysql.com/products/database/cluster/.
Clientes
Recursos
A
 B
C
 D
Clientes fazem requisições 
ao cluster...
... e qualquer máquina do 
cluster pode atuar como 
servidor.
E
 F
G
 H

## Página 270

270 Processamento distribuído
em  várias  máquinas  ao  mesmo  tempo.  Ao  invés  de  prover  recursos  
diretamente, a aplicação utiliza os equipamentos para suportar suas próprias  
funcionalidades.  Com  isso,  a  infra-estrutura  é  utilizada  de  forma  quase  
transparente pelos usuários que usam a aplicação interativamente. Todos os  
nós  rodam  o  aplicativo  e  podem  operar  como  servidores  e  clientes.  O  
exemplo  mais  comum  de  arquitetura  híbrida  são  os  sistemas  de  
compartilhamento de arquivos ( file sharing ) que usam comunicação  Peer To  
Peer (P2P).
Independente do modelo utilizado. sistemas distribuídos devem atender a  
quatro requisitos básicos:
▪ Comunicação: as máquinas envolvidas devem se comunicar de forma a  
permitir a troca de informações entre elas.
▪ Metadados: os dados sobre o processamento precisam ser mantidos de  
forma adequada.
▪ Controle: os processos devem ser gerenciados e monitorados.
▪ Segurança:  o  sigilo,  integridade  e  disponibilidade  devem  estar  
protegidos.
Existem diversas tecnologias voltadas para o desenvolvimento de aplicações  
distribuídas, tais como: XML-RPC81, Web Services, objetos distribuídos, MPI e 
outras.
81 Especificação em http://www.xmlrpc.com/.

## Página 271

Processamento distribuído 271
Objetos distribuídos
A  premissa  básica  da  tecnologia  de  objetos  distribuídos é  tornar  objetos  
disponíveis  para  que  seus  métodos  possam  ser  evocados  remotamente  a  
partir  de  outras  máquinas  ou  mesmo  por  outros  processos  na  mesma  
máquina, usando a pilha de protocolos de rede TCP/IP para isso.
Existem  diversas  soluções  para  estes  casos,  porém  utilizar  objetos 
distribuídos oferece  várias  vantagens  em  relação  a  outras  soluções  que  
implementam funcionalidades semelhantes, tal como o protocolo XML-RPC:
▪ Simplicidade para implementação.
▪ Oculta as camadas de comunicação.
▪ Suporte  a  estruturas  de  dados  nativas  (contanto  que  sejam  
serializáveis).
▪ Boa performance.
▪ Maturidade da solução.
PYthon Remote Objects  ( PYRO82) é um framework para aplicações distribuídas  
82 Documentação e fontes disponíveis em: http://pyro.sourceforge.net/.
Rede
Cliente
Interpretador
Programa
Framework
Servidor
Interpretador
Objeto
Framework

## Página 272

272 Processamento distribuído
que permite  publicar objetos  via TCP/IP. Na máquina servidora,  o  PYRO 
publica o objeto, cuidando de detalhes como: protocolo, controle de sessão,  
autenticação, controle de concorrência e outros.
Exemplo de servidor:
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Pyro.core
# A classe Pyro.core.ObjBase define
# o comportamento dos objetos distribuídos
class Dist(Pyro.core.ObjBase):
    def calc(self, n):
        return n**n
if __name__ == '__main__':
    # Inicia a thread do servidor
    Pyro.core.initServer()
    # Cria o servidor
    daemon = Pyro.core.Daemon()
    # Publica o objeto
    uri = daemon.connect(Dist(),'dist')
    # Coloca o servidor em estado operacional
    daemon.requestLoop()
Na máquina cliente, o programa usa o PYRO para evocar rotinas do servidor  
e recebe os resultados, da mesma forma que um método de um objeto local.
Exemplo de cliente:
# -*- coding: utf-8 -*-
import Pyro.core

## Página 273

Processamento distribuído 273
# Cria um objeto local para acessar o objeto remoto
proxy = Pyro.core.getProxyForURI('PYROLOC://127.0.0.1/dist')
# Evoca um método do objeto remoto
print proxy.calc(1000)
Os métodos publicados através do PYRO não podem ser identificados por  
introspecção pelo cliente.
Embora o PYRO resolva problemas de concorrência de comunicação com os  
clientes que estão acessando o mesmo servidor (cada conexão roda em uma  
thread separada), fica por conta do desenvolvedor (ou de outros  frameworks 
que a aplicação utilize) resolver questões de concorrência por outros recursos,  
como arquivos ou conexões de banco de dados 83, por exemplo. É possível  
autenticar as conexões através da criação de objetos da classe  Validator, que  
podem verificar credenciais, endereços IP e outros itens.
83 Problemas de concorrência de conexões de banco de dados podem ser tratados de forma  
transparente com a utilização de ORMs que implementam esta funcionalidade ou pelo  
pacote DBUtils ( http://www.webwareforpython.org/DBUtils), que faz parte do projeto  
Webware for Python (http://www.webwareforpython.org/).

## Página 274

274 Performance
Performance
O Python provê algumas ferramentas para avaliar  performance e localizar  
gargalos na aplicação. Entre estas ferramentas estão os módulos  cProfile e  
timeit.
O módulo cProfile84 faz uma análise detalhada de performance, incluindo as  
chamadas de função, retornos de função e exceções.
Exemplo:
# -*- coding: latin1 -*-
import cProfile
def rgb1():
    """
    Função usando range()
    """
    rgbs = []
    for r in range(256):
        for g in range(256):
            for b in range(256):
                rgbs.append('#%02x%02x%02x' % (r, g, b))
    return rgbs
def rgb2():
    """
    Função usando xrange()
    """
    rgbs = []
    for r in xrange(256):
        for g in xrange(256):
            for b in xrange(256):
                rgbs.append('#%02x%02x%02x' % (r, g, b))
    return rgbs
def rgb3():
    """
    Gerador usando xrange()
    """
84 O módulo  cProfile (disponível no Python 2.5 em diante) é uma versão otimizada do  
módulo profile, que tem a mesma funcionalidade.

## Página 275

Performance 275
    for r in xrange(256):
        for g in xrange(256):
            for b in xrange(256):
                yield '#%02x%02x%02x' % (r, g, b)
def rgb4():
    """
    Função usando uma lista várias vezes
    """
    rgbs = []
    ints = range(256)
    for r in ints:
        for g in ints:
            for b in ints:
                rgbs.append('#%02x%02x%02x' % (r, g, b))
    return rgbs
def rgb5():
    """
    Gerador usando apenas uma lista
    """
    for i in range(256 ** 3):
        yield '#%06x' % i
def rgb6():
    """
    Gerador usando xrange() uma vez
    """
    for i in xrange(256 ** 3):
        yield '#%06x' % i
# Benchmarks
print 'rgb1:'
cProfile.run('rgb1()')
print 'rgb2:'
cProfile.run('rgb2()')
print 'rgb3:'
cProfile.run('list(rgb3())')
print 'rgb4:'
cProfile.run('rgb4()')
print 'rgb5:'
cProfile.run('list(rgb5())')

## Página 276

276 Performance
print 'rgb6:'
cProfile.run('list(rgb6())')
Saída:
rgb1:
         16843012 function calls in 54.197 CPU seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.633    0.633   54.197   54.197 <string>:1(<module>)
        1   49.203   49.203   53.564   53.564 rgbs.py:5(rgb1)
 16777216    4.176    0.000    4.176    0.000 {method 'append' of 'list'  
objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of  
'_lsprof.Profiler' objects}
    65793    0.186    0.000    0.186    0.000 {range}
rgb2:
         16777219 function calls in 53.640 CPU seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.624    0.624   53.640   53.640 <string>:1(<module>)
        1   49.010   49.010   53.016   53.016 rgbs.py:16(rgb2)
 16777216    4.006    0.000    4.006    0.000 {method 'append' of 'list'  
objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of  
'_lsprof.Profiler' objects}
rgb3:
         16777219 function calls in 52.317 CPU seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    6.251    6.251   52.317   52.317 <string>:1(<module>)
 16777217   46.066    0.000   46.066    0.000 rgbs.py:27(rgb3)
        1    0.000    0.000    0.000    0.000 {method 'disable' of  
'_lsprof.Profiler' objects}

## Página 277

Performance 277
rgb4:
         16777220 function calls in 53.618 CPU seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.624    0.624   53.618   53.618 <string>:1(<module>)
        1   48.952   48.952   52.994   52.994 rgbs.py:36(rgb4)
 16777216    4.042    0.000    4.042    0.000 {method 'append' of 'list'  
objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of  
'_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {range}
rgb5:
         16777220 function calls in 32.209 CPU seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    6.110    6.110   32.209   32.209 <string>:1(<module>)
 16777217   25.636    0.000   26.099    0.000 rgbs.py:48(rgb5)
        1    0.000    0.000    0.000    0.000 {method 'disable' of  
'_lsprof.Profiler' objects}
        1    0.463    0.463    0.463    0.463 {range}
rgb6:
         16777219 function calls in 30.431 CPU seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    6.066    6.066   30.431   30.431 <string>:1(<module>)
 16777217   24.365    0.000   24.365    0.000 rgbs.py:55(rgb6)
        1    0.000    0.000    0.000    0.000 {method 'disable' of  
'_lsprof.Profiler' objects}
O relatório do cProfile mostra no inicio as duas informações mais importantes: 
o tempo de CPU consumido em segundos e a quantidade de chamadas de  
função. As outras linhas mostram os detalhes por função, incluindo o tempo  
total e por chamada.

## Página 278

278 Performance
As cinco rotinas do exemplo têm a mesma funcionalidade: geram uma escala  
de cores RGB. Porém, o tempo de execução é diferente.
Comparando os resultados:
Rotina Tipo Tempo Laços x/range()
rgb1() Função 54.197 3 range()
rgb2() Função 53.640 3 xrange()
rgb3() Gerador 52.317 3 xrange()
rgb4() Função 53.618 3 range()
rgb5() Gerador 32.209 1 range()
rgb6() Gerador 30.431 1 xrange()
Fatores observados que pesaram no desempenho:
▪ A complexidade do algoritmo.
▪ Geradores  apresentaram  melhores  resultados  do  que  as  funções  
tradicionais.
▪ O gerador  xrange() apresentou uma performance ligeiramente melhor  
do que a função range().
O gerador rgb6(), que usa apenas um laço e xrange(), é bem mais eficiente que  
as outras rotinas.
Outro exemplo:
# -*- coding: latin1 -*-
import cProfile
def fib1(n):
    """
    Fibonacci calculado de forma recursiva.
    """
    if n > 1:
        return fib1(n - 1) + fib1(n - 2)
    else:
        return 1
def fib2(n):

## Página 279

Performance 279
    """
    Fibonacci calculado por um loop.
    """
    if n > 1:
        # O dicionário guarda os resultados
        fibs = {0:1, 1:1}
        for i in xrange(2, n + 1):
            fibs[i] = fibs[i - 1] + fibs[i - 2]
        return fibs[n]
    else:
        return 1
print 'fib1'
cProfile.run('[fib1(x) for x in xrange(1, 31)]')
print 'fib2'
cProfile.run('[fib2(x) for x in xrange(1, 31)]')
Saída:
fib1
         7049124 function calls (32 primitive calls) in 21.844 CPU seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   21.844   21.844 <string>:1(<module>)
7049122/30   21.844    0.000   21.844    0.728 fibs.py:4(fib1)
        1    0.000    0.000    0.000    0.000 {method 'disable' of  
'_lsprof.Profiler' objects}
fib2
         32 function calls in 0.001 CPU seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
       30    0.001    0.000    0.001    0.000 fibs.py:13(fib2)
        1    0.000    0.000    0.000    0.000 {method 'disable' of  
'_lsprof.Profiler' objects}
A performance do cálculo da série de Fibonacci usando um laço que preenche 

## Página 280

280 Performance
um dicionário é muito mais eficiente do que a versão usando recursão, que  
faz muitas chamadas de função.
O módulo timeit serve para fazer benchmark de pequenos trechos de código 85. 
O  módulo  foi  projetado  para  evitar  as  falhas  mais  comuns  que  afetam  
programas usados para fazer benchmarks.
Exemplo:
import timeit
# Lista dos quadrados de 1 a 1000
cod = '''s = []
for i in xrange(1, 1001):
    s.append(i ** 2)
'''
print timeit.Timer(cod).timeit()
# Com Generator Expression
cod = 'list(x ** 2 for x in xrange(1, 1001))'
print timeit.Timer(cod).timeit()
# Com List Comprehesion
cod = '[x ** 2 for x in xrange(1, 1001)]'
print timeit.Timer(cod).timeit()
Saída:
559.372637987
406.465490103
326.330293894
O List Comprehension é mais eficiente do que o laço tradicional.
Outra forma de melhorar a performance de uma aplicação é usando o Psyco, 
que é uma espécie de  Just In Compiler  (JIT). Durante a execução, ele tenta  
otimizar o código da aplicação e, por isso, o módulo deve ser importado antes 
do código a ser otimizado (o inicio do módulo principal da aplicação é um  
85 O módulo cProfile não é apropriado para avaliar pequenos trechos de código. O módulo  
timeit é mais adequado pois executa o código várias vezes durante a avaliação.
O código é passado para o 
benchmark como uma string.
O código é passado para o 
benchmark como uma string.

## Página 281

Performance 281
lugar adequado).
Exemplo (com o último trecho de código avaliado no exemplo anterior):
import psyco
# Tente otimizar tudo
psyco.full()
import timeit
# Lista dos quadrados de 1 a 1000
cod = '[x ** 2 for x in xrange(1, 1001)]'
print timeit.Timer(cod).timeit()
Saída:
127.678481102
O código foi executado mais de duas vezes mais rápido do que antes. Para  
isso, foi necessário apenas acrescentar duas linhas de código.
Porém, o Psyco deve ser usado com alguns cuidados, pois em alguns casos ele  
pode não conseguir otimizar ou até piorar a performance86. As funções map() 
e filter() devem ser evitadas e módulos escritos em C, como o re (expressões 
regulares) devem ser marcados com a função cannotcompile() para que o Psyco 
os ignore. O módulo fornece formas de otimizar apenas determinadas partes  
do código da aplicação, tal como a função profile(), que só otimiza as partes  
mais pesadas do aplicativo, e uma função log() que analisa a aplicação, para  
contornar estas situações.
Algumas dicas sobre otimização:
▪ Mantenha o código simples.
▪ Otimize apenas o código aonde a performance da aplicação é realmente 
crítica.
86 Existem  algumas  funções  em  que  o  Psyco  tem  o  efeito  de  reduzir  a  velocidade  do 
programa, pois o próprio Psyco consome CPU também. Além disso, o Psyco também faz 
com que a aplicação consuma mais memória.

## Página 282

282 Performance
▪ Use ferramentas para identificar os gargalos no código.
▪ Evite funções recursivas.
▪ Use os recursos nativos da linguagem. As listas e dicionários do Python 
são muito otimizados.
▪ Use List Comprehensions ao invés de laços para processar listas usando  
expressões simples.
▪ Evite funções dentro de laços. Funções podem receber e devolver listas.
▪ Use geradores ao invés de funções para grandes sequências de dados.

## Página 283

Empacotamento e distribuição 283
Empacotamento e distribuição
Geralmente é bem mais simples distribuir aplicações na forma de binário, em  
que basta rodar um executável para iniciar a aplicação, do que instalar todas  
as dependências necessárias em cada máquina em que se deseja executar a  
aplicação.
Existem  vários  softwares  que  permitem  gerar  executáveis  a  partir  de  um 
programa feito em Python, como o Py2exe87 e cx_Freeze88.
O  Py2exe só  funciona  na  plataforma  Windows,  porém  possui  muitos  
recursos, podendo gerar executáveis com interface de texto, gráficos, serviços  
(programas que rodam sem intervenção do usuário, de forma semelhante aos  
daemons nos sistemas UNIX) e servidores COM (arquitetura de componentes  
da Microsoft).
87 Documentação,  fontes  e  binários  de  instalação  podem  ser  encontrados  em:  
http://www.py2exe.org/.
88 Documentação,  fontes  e  binários  de  instalação  para  várias  plataformas  podem  ser  
encontrados em: http://starship.python.net/crew/atuining/cx_Freeze/.
Fontes
(*.py)
Bytecode
(*.pyc / *.pyo)
 Binários
Interpretador e
 dependências
Compilação
 Empacotamento
Instalador
Binários

## Página 284

284 Empacotamento e distribuição
O  cx_Freeze é portável, podendo rodar em ambientes UNIX, porém é bem  
menos versátil que o Py2exe.
Para usar o  Py2exe, é preciso criar um  script, que normalmente se chama  
“setup.py”, que diz ao Py2exe o que é necessário para gerar o executável.
Exemplo de “setup.py”:
# -*- coding: latin1 -*-
"""
Exemplo de uso do py2exe
"""
from distutils.core import setup
import py2exe
setup(name = 'SIM - Sistema Interativo de Música',
    service = ['simservice'],
    console = ['sim.py', 'simimport.py'],
    windows = ['simgtk.py'],
    options = {'py2exe': {
        'optimize': 2,
        'includes': ['atk', 'gobject', 'gtk','gtk.glade',
        'pango', 'cairo', 'pangocairo']
    }},
    data_files=[('',['janela.glade', 'sim.ico'])],
    description = 'Primeira Versão...',
    version = '1.0')
No exemplo, temos um sistema que é composto por dois utilitários de linha  
comando, um aplicativo com interface gráfica e um serviço. O aplicativo com  
GUI depende do GTK+ para funcionar e foi desenvolvido usando Glade.
Entre os parâmetros do Py2exe, os mais usuais são:
▪ name: nome da aplicação.
▪ service: lista de serviços.
▪ console: lista de programas com interface de texto.
▪ windows: lista de programas com interface gráfica.
▪ options['py2exe']: dicionário com opções que alteram o comportamento  
do Py2exe:
• optimize: 0 (otimização desativada,  bytecode padrão), 1 (otimização  

## Página 285

Empacotamento e distribuição 285
ativada,  equivale  ao  parâmetro  “-O”  do  interpretador)  ou  2  
(otimização  com  remoção  de  Doc  Strings  ativada,  equivale  ao  
parâmetro “-OO” do interpretador).
• includes: lista de módulos que serão incluídos como dependências.  
Geralmente, o  Py2exe detecta as dependências sem necessidade de  
usar esta opção.
• data_files: outros arquivos que fazem parte da aplicação, tais como  
imagens, ícones e arquivos de configuração.
• description: comentário.
• version: versão da aplicação, como string.
Para gerar o executável, o comando é:
python setup.py py2exe
O Py2exe criará duas pastas:
▪ build: arquivos temporários.
▪ dist: arquivos para distribuição.
Entre  os  arquivos  para  distribuição,  “w9xpopen.exe”  é  necessário  apenas  
para as versões  antigas  do  Windows  (95 e 98)  e pode  ser removido  sem  
problemas em versões mais recentes.
Pela  linha  de  comando  também  é  possível  passar  algumas  opções  
interessantes,  como o parâmetro “-b1”, para gerar  menos arquivos para a  
distribuição.
O cx_Freeze é um utilitário de linha de comando.
FreezePython -OO -c sim.py
A opção “-c” faz com que o bytecode seja comprimido no formato zip.
FreezePython -OO --include-modules=atk,cairo,pango,pangocairo simgtk.py

## Página 286

286 Empacotamento e distribuição
A opção “--include-modules”, permite passar uma lista de módulos que serão 
incluídos na distribuição.
Tanto o Py2exe quanto o cx_Freeze não são compiladores. O que eles fazem é  
empacotar os bytecodes da aplicação, suas dependências e o interpretador em  
(pelo  menos)  um  arquivo  executável  (e  arquivos  auxiliares)  que  não  
dependem do ambiente em que foram gerados. Com isso, a distribuição do  
aplicativo  se  torna  bem  mais  simples.  Entretanto,  não  há  ganho  de  
performance  em  gerar  executáveis,  exceto  pela  carga  da  aplicação  para  a 
memória em alguns casos.
Eles também não geram programas de instalação. Para isso, é necessário o  
uso de um software específico. Os instaladores são gerados por aplicativos  
que se encarregam de automatizar tarefas comuns do processo de instalação.  
São exemplos de softwares dessa categoria: Inno Setup89 e NSIS90.
89 Documentação  e  binários  de  instalação  disponíveis  em:  
http://www.jrsoftware.org/isinfo.php.
90 Endereço do projeto: http://nsis.sourceforge.net/Main_Page.

## Página 287

Exercícios VI 287
Exercícios VI
1. Implementar um módulo com uma função  tribonacci(n) que retorne uma  
lista de  n números de Tribonacci, aonde  n é o parâmetro da função. Faça  
testes da função caso o módulo seja executado como principal.
2. Implementar:
▪ um servidor que publique um objeto distribuído e este evoque a função 
tribonacci.
▪ um cliente que use o objeto distribuído para calcular a sequência de  
Tribonacci.

## Página 288

288 Apêndices
Apêndices
Esta  parte  se  concentra  em  outras  tecnologias  que  tem  convivem  com  o  
Python de diversas formas. E ao final, as respostas dos exercícios propostos  
nas partes anteriores.
Conteúdo:
▪ Integração com aplicativos  .
▪ Blender  .
▪ GIMP  .
▪ Inkscape  .
▪ BrOffice.org  .
▪ Integração com outras linguagens  .
▪ Integração com .NET  .
▪ Respostas dos exercícios I  .
▪ Respostas dos exercícios II  .
▪ Respostas dos exercícios III  .
▪ Respostas dos exercícios IV  .
▪ Respostas dos exercícios V  .
▪ Respostas dos exercícios VI  .

## Página 289

Integração com aplicativos 289
Integração com aplicativos
Python pode ser usado como linguagem  script em vários aplicativos para  
automatizar tarefas e adicionar novas funcionalidades, ou para oferecer seus  
recursos  para  outro  programa,  através  de  uma  API ou  protocolo.  Muitos  
desses pacotes de software são Open Source, como o BrOffice.org e o Blender,  
por exemplo.
Muitas  vezes  isso  é  possível  porque  esses  programas  adotaram  uma  
arquitetura de plugins, na qual existe uma infraestrutura genérica que permite 
que componentes externos sejam ligados aos aplicativos.
Na maioria dos casos, isso é viabilizado mediante o uso de uma API que é  
disponibilizada pelo software, que é vista pelo Python como um módulo ou  
um pacote, que apenas precisa estar no PYTHONPATH para que possa ser  
utilizado.  Com  isso,  o  programa  pode  fazer  chamadas  as  rotinas  do  
aplicativo, para utilizar seus recursos e se comunicar.
Em outros casos, como o Inkscape, o programa em Python funciona como um 
filtro, recebendo e enviando informações para o aplicativo através de entrada  
(stdin) e saída (stdout) padrões.

## Página 290

290 Blender
Blender
Blender91 é um software de modelagem 3D de código aberto, capaz de gerar  
animações  e  também  funciona  como  Game  Engine  (infraestrutura  
especializada para criação de jogos para computador). Além disso, o software 
possui  um  renderizador  interno  e  pode  ser  integrado  a  renderizadores  
externos,  como  os  projetos,  também  de  código  aberto,  Yafaray 92 e  
LuxRender93.
No Blender, uma cena é composta por objetos, que precisam ser fixados em  
posições e conectados a cena. Se o objeto não estiver conectado a cena, ele  
será  eliminado  ao  fim  do  processamento.  Para  cada  sólido,  é  possível  
configurar vários materiais, que podem ter zero ou mais texturas.
A cena padrão do Blender é composta por três objetos: uma câmera, uma  
91 Documentação, fontes e binários podem ser encontrados em: http://www.blender.org/.
92 Página do projeto: http://www.yafaray.org/.
93 Site oficial: http://www.luxrender.net/.


## Página 291

Blender 291
lâmpada e um cubo (representado como mesh). A escala no Blender é medida  
em BUs (Blender Units).
Com Python é possível acessar todas essas estruturas do Blender através de  
módulos, incluindo:
▪ Blender: permite abrir arquivos, salvar e outras funções correlatas.
▪ Object: operações com objetos 3D.
▪ Materials: manipulação de materiais.
▪ Textures: manipulação de texturas.
▪ World: manipulação do ambiente da cena.
▪ Draw: rotinas de interface com o usuário.
▪ Nmesh: manipulação de malhas.
▪ BGL: acesso direto as funções do OpenGL.
A  API  do  Blender  oferece  várias  texturas  procedurais  e  uma  coleção  de  
sólidos  primitivos  prontos,  que  podem  ser  criados  e  alterados  através  de 
código.
Exemplo de código para a criação de uma cena:
# -*- coding: latin1 -*-
import math
import Blender
# Pega a cena atual
cena = Blender.Scene.GetCurrent()
# Elementos da cena "default"
camera = Blender.Object.Get()[0]
cubo = Blender.Object.Get()[1]
lamp = Blender.Object.Get()[2]
# Move a câmera
camera.setLocation(8., -8., 4.)
camera.setEuler(math.radians(70), 0.,
    math.radians(45))
# Muda a lente
camera.data.lens = 30

## Página 292

292 Blender
# Remove da cena o objeto "default"
cena.objects.unlink(cubo)
# Altera a intensidade da luz
lamp.data.energy = 1.2
# Muda o tipo para "Sun"
lamp.data.type = 1
# Aumenta o número de samples
lamp.data.raySamplesX = 16
lamp.data.raySamplesY = 16
# E a cor
lamp.data.col = 1., .9, .8
# Cria outra fonte de luz
lamp1 = Blender.Lamp.New('Lamp')
lamp1.energy = 0.5
lamp1.col = .9, 1., 1.
_lamp1 = Blender.Object.New('Lamp')
# Muda o lugar da fonte (default = 0.0, 0.0, 0.0)
_lamp1.setLocation(6., -6., 6.)
# "Prende" a fonte de luz na cena
_lamp1.link(lamp1)
cena.objects.link(_lamp1)
# Cria um material
material1 = Blender.Material.New('newMat1')
material1.rgbCol = [.38, .33, .28]
material1.setAlpha(1.)
# Cria uma textura
textura1 = Blender.Texture.Get()[0]
textura1.setType('Clouds')
textura1.noiseType = 'soft'
textura1.noiseBasis = Blender.Texture.Noise['VORONOICRACKLE']
# Coloca no material
material1.setTexture(0, textura1)
mtex1 = material1.getTextures()[0]
mtex1.col = .26, .22, .18
mtex1.mtNor = 1
mtex1.neg = True
mtex1.texco = Blender.Texture.TexCo['GLOB']

## Página 293

Blender 293
material1.mode += Blender.Material.Modes['RAYMIRROR']
material1.rayMirr = 0.2
material1.glossMir = 0.8
# Cria o piso
mesh = Blender.Mesh.Primitives.Plane(40.)
piso = cena.objects.new(mesh,'Mesh')
piso.setLocation(0., 0., .05)
# Rotaciona o piso
piso.setEuler(0., 0., math.radians(45))
# Coloca o material no piso
piso.setMaterials([material1])
piso.colbits = 1
# Cria outro material
material2 = Blender.Material.New('newMat2')
material2.rgbCol = [.77, .78, .79]
material2.setAlpha(1.)
material2.mode += Blender.Material.Modes['RAYMIRROR']
material2.rayMirr = 0.6
material2.glossMir = 0.4
# Coloca textura no outro material
material2.setTexture(0, textura1)
mtex2 = material2.getTextures()[0]
mtex2.col = .3, .3, .4
mtex2.mtNor = 1
mtex2.neg = True
mtex2.texco = Blender.Texture.TexCo['GLOB']
mat = [material2]
# Cria objetos na cena
def objeto(local, tam, mat, prim=Blender.Mesh.Primitives.Cube):
    mesh = prim()
    obj = cena.objects.new(mesh, 'Mesh')
    obj.setLocation(*local)
    obj.size = tam
    obj.setMaterials(mat)
    obj.colbits = 1
    return obj
def coluna(x=0., y=0., z=0., mat=mat):
    # Cilindro

## Página 294

294 Blender
    prim = Blender.Mesh.Primitives.Cylinder
    # Topo
    local = x, y, 2.5 + z
    tam = .25, .25, .1
    objeto(local, tam, mat)
    # Base
    local = x, y, 0. + z
    objeto(local, tam, mat)
    # Corpo
    for k in xrange(10):
        local = x, y, .25 * k + z
        tam = .2 - k / 200., .2 - k / 200., .25
        objeto(local, tam, mat, prim)
# Cria colunas no fundo
for i in xrange(16):
    # Primeira fileira
    coluna(i - 8., 8)
    # Segunda fileira
    coluna(-8., i - 8.)
    # Aqueduto
    local = -8., i - 8., 3.
    tam = .5, .5, .5
    objeto(local, tam, mat)
    local = i - 8., 8., 3.
    objeto(local, tam, mat)
z = .25
# Cria colunas em cima do piso
for i in (-3, 3):
    for j in range(-2, 3):
        # Fileiras X
        coluna(i, j, z)
        # Fileiras Y
        coluna(j, i, z)
    # Cantos

## Página 295

Blender 295
    for j in (-3, 3):
        coluna(i, j, z)
# Cria escada
for i in xrange(8):
    local = 0., 0., i / 32. - .25
    tam = 3.3 + (8. - i) / 8., 3.3 + (8. - i) / 8., .25
    objeto(local, tam, mat)
# Cria teto
for i in xrange(35):
    local = 0., 0., 2.9 + i / 60.
    tam = 3.5 - i / 200., 3.5 * ( 1. - i / 35.), .1
    objeto(local, tam, mat)
# Pega o "mundo"
world = Blender.World.Get()[0]
# Modo "blend" no fundo
world.skytype = 1
# Atualiza a cena
cena.update()
Saída (renderizada):
Exemplo com interface:


## Página 296

296 Blender
# -*- coding: latin1 -*-
from math import *
from Blender.Draw import *
from Blender import BGL, Window, Mesh, Scene
class Buttons:
    """
    Classe com para armazenar os botões para que
    os valores possam ser usados por outras rotinas
    sem usar variáveis globais
    """
    # Equação
    formula = Create('cos(x) - sin(3*x)')
    # Variação
    delta = Create(.1)
def interface():
    """
    Função que desenha a interface
    """
    # Pega o tamanho da janela
    x, y = Window.GetAreaSize()
    # Desenha caixa de texto
    # Parâmetros: rótulo, evento, x, y, largura, altura, valor inicial,
    # tamanho máximo do texto, tooltip
    Buttons.formula = String('Fórmula: ', 0, 10, y - 30, 300, 20,
        Buttons.formula.val, 300, 'Entre com uma expressão Python')
    # Desenha caixa de número
    # Parâmetros: rótulo, evento, x, y, largura, altura, valor inicial,
    # mínimo, máximo, tooltip
    Buttons.delta = Number('Delta: ', 0, 10, y - 60, 300, 20,
        Buttons.delta.val, .01, 1., 'Entre com a variação')
    # Desenha os botões
    # Parâmetros: texto do botão, evento, x, y, largura, altura, tooltip
    PushButton('Ok', 1, 10, y - 90, 100, 20, 'Aplica as mudanças')
    PushButton('Fim', 2, 10, y - 120, 100, 20, 'Termina o programa')
    # Comandos OpenGL através da BGL
    BGL.glClearColor(.7, .7, .6, 1)
    BGL.glClear(BGL.GL_COLOR_BUFFER_BIT)
def events(evt, val):

## Página 297

Blender 297
    """
    Função que responde a eventos diversos,
    menos os gerados por botões
    """
    # Os eventos das teclas estão definidas em Draw
    if evt == ESCKEY:
        # Termina o programa
        Exit()
def buttons(evt):
    """
    Função que responde a eventos dos botões
    """
    if  evt == 2:
        Exit()
    elif evt == 1:
        gen3d()
def gen3d():
        # Cena 3D
        cena = Scene.GetCurrent()
        x = y = z = 0
        while x < 2 * pi:
            # Calcula os valores de z
            z = eval(Buttons.formula.val)
            # Cria uma esfera de 16 segmentos, 16 anéis e 0.1 BU de raio
            s = Mesh.Primitives.UVsphere(16, 16, .1)
            esfera = cena.objects.new(s, 'Mesh')
            
            # Transfere a esfera para o local calculado
            esfera.setLocation(x, y, z)
            # Próximo x
            x += Buttons.delta.val
            
        # Atualiza a cena
        cena.update()
if __name__ == '__main__':

## Página 298

298 Blender
    # Registra as funções callback
    Register(interface, events, buttons)
Interface:
Saída:
Exemplo de criação de malha:
# -*- coding: latin1 -*-
from Blender import NMesh, Redraw
# Cria uma nova malha
mesh = NMesh.New()
# Um dicionário para armazenar os vértices
# conforme a posição
vertices = {}
for X in xrange(3):


## Página 299

Blender 299
    for Y in range(3):
        # Uma face é determinada pelos vértices que fazem parte dela
        face = []
        coords = [(X + 0, Y + 0), (X + 0, Y + 1),
            (X + 1, Y+ 1), (X + 1, Y + 0)]
        # Vértices da face
        for x, y in coords:
            vertices[(x, y)] = vertices.get((x, y), NMesh.Vert(x, y, 0))
            face.append(vertices[(x, y)])
        # Adiciona um objeto "face" na lista de faces da malha
        mesh.faces.append(NMesh.Face(face))
# Adiciona os vértices na malha
for vertice in vertices.values():
    mesh.verts.append(vertice)
# Carrega a malha na cena
NMesh.PutRaw(mesh, 'chess', True)
Redraw()
Saída:
Para executar código em Python no ambiente do  Blender, basta carregar o  
programa na janela de editor de texto do Blender e usar a opção de execução  
no menu.
Game engine
Game  engine  é  um  software  que  facilita  a  criação  de  jogos,  simulando  
determinados aspectos da realidade, de forma a possibilitar a interação com  


## Página 300

300 Blender
objetos  em  tempo  real.  Para  isso,  ele  deve  implementar  várias  
funcionalidades que são comuns em jogos, como por exemplo a capacidade  
de simulação física. O objetivo principal do uso de  game engine s  é centrar o  
foco da criação do jogo no conteúdo, ou seja, mapas (níveis), personagens,  
objetos, diálogos, trilha sonora e cenas. É comum que vários jogos usem o  
mesmo engine, reduzindo assim, o esforço de desenvolvimento.
Um dos principais recursos fornecidos por  game engine s é a capacidade de  
renderizar  cenas  em  2D  ou  3D  em  tempo  real,  geralmente  usando  uma  
biblioteca gráfica, como o OpenGL, permitindo animações e efeitos especiais.  
O componente especializado para esta função é conhecido como render engine.
Além  disso,  a  simulação  física  também  é  essencial  para  um  jogo,  para  
representar  de  forma  adequada  os  movimentos  dos  personagens  sendo  
influenciados pela gravidade, inércia, atrito, detecção de colisões e outros. O  
componente que realiza esses cálculos é chamado Physics Engine.
Outra funcionalidade importante é a lógica, que é como o jogo determina o  
comportamento do ambiente e dos personagens. Em muitos casos, o  game 
engine suporta uma ou mais linguagens para descreve-la.
Os  game  engine s podem  incluir  outros  recursos  importantes  para  
determinados  tipos  de  jogos,  como  conectividade.  No  caso  de  MMOG  
(Massively  Multiplayer  Online  Games ),  que  são  muito  complexos,  a  
infraestrutura de software é mais conhecida como middleware.
A popularização dos game engines aconteceu durante a década de 90, graças a  
Id Software, que desenvolveu os jogos que definiram o gênero chamado FPS  
(First Person Shooter), jogos de ação em primeira pessoa. Esses títulos tiveram  
seus  engines licenciados  para  outras  empresas,  que  criaram  outros  jogos  
desenvolvendo o conteúdo do jogo. Em paralelo, os processadores de vídeo  
foram incorporando suporte as funções gráficas cada vez mais sofisticadas, o  
que facilitou a evolução dos engines. A Id também liberou os game engines das 
séries DOOM e Quake em GPL.
Além de entretenimento,  outras  áreas podem se beneficiar desses  engines. 
Chamadas  genericamente  de  serious  games ,  aplicações  nas  áreas  de  

## Página 301

Blender 301
treinamento,  arquitetura,  engenharia,  medicina  e  marketing  estão  se  
popularizando aos poucos.
O Blender inclui um game engine genérico, que permite a criação de jogos 3D,  
usando o próprio aplicativo para criação de conteúdo e Python para as partes  
com lógica mais complexa.
O Blender  Game Engine  ( BGE) usa como  physics engine  o projeto, também  
Open Source, chamado Bullet94. Com ele, é possível simular o comportamento  
de  corpos  rígidos  (como  peças  de  maquinaria),  macios  (como  tecidos),  
estáticos (fixos) e intangíveis (que não são afetados por colisões).
O render engine  do Blender suporta GLSL ( OpenGL Shading Language ), o que  
permite que ele utilize recursos avançados disponíveis nos processadores de  
vídeo mais recentes.
Já a lógica é definida no BGE através de Logic Bricks, que segue um modelo  
baseado em eventos. Eventos são associados a um objeto da cena e podem ser  
gerados  por  periféricos  de  entrada  (como  teclado  e  mouse),  pelo  sistema 
(tempo),  pelo  próprio  BGE (colisões,  por  exemplo)  ou  por  mensagens  
enviadas por outros objetos. Quando um ou mais eventos são detectados, o  
BGE toma uma decisão e reage de acordo.
Existem três tipos de bricks:
94 Site oficial: http://www.bulletphysics.org/.
Quadro 160 Quadro 230 Quadro 300
Blender + Bullet

## Página 302

302 Blender
▪ Sensores (sensors), que detectam os eventos.
▪ Controladores  ( controllers),  que  relacionam  os  sensores  com  os  
ativadores adequados.
▪ Ativadores (actuators), que ativam as reações.
No painel  Logic, as associações entre os  bricks pode ser definida de forma  
interativa. O BGE tem diversos ativadores prontos, para realizar tarefas como  
encerrar a execução ou mudar a velocidade do objeto.
O  BGE pode evocar código em Python para responder aos eventos, através  
do controlador “Python”. Quando uma função em Python é executada, ela  
recebe como argumento o controlador que realizou a chamada, com isso é  
possível identificar e modificar o objeto (onwer) que possui o controlador.
Exemplo (módulo com função para teleporte):
# -*- coding: latin1 -*-
# Módulo de interface com o Game Engine
import GameLogic
def teleport(cont):
    # obtêm o dono do controller
    own = cont.owner
    # obtêm a cena
    scene = GameLogic.getCurrentScene()
    
    # obtêm o destino
    dest = scene.getObjectList()['OBr_portal']
    
    # obtêm as coordenadas do destino
    x, y, z = dest.getPosition()
    
    # move a câmera para 1 BU acima do destino
    own.setPosition([x, y, z + 1])
Essa função muda a posição do objeto, para um BU a cima do objeto chamado 
“r_portal”, independente do lugar na cena em que estiver localizado.

## Página 303

GIMP 303
GIMP
GIMP95 ( GNU Image Manipulation Program ) é um software de código aberto  
bastante conhecido, que implementa várias ferramentas para processamento  
e edição de imagens  raster (com alguns recursos vetoriais,  para lidar com  
texto, por exemplo), além de algoritmos de conversão para diversos formatos.  
Permite a manipulação de imagens compostas de múltiplas camadas e possui  
uma  arquitetura  baseada  em  plugins que  permite  implementar  novas  
funcionalidades.
Originalmente,  os  plugins eram  criados  na  linguagem  funcional  Scheme,  
porém  hoje  é  possível  usar  Python  também,  através  de  uma  extensão  
chamada Gimp-Python96.
Um plugin feito em Python deve seguir os seguintes passos:
▪ Importar  gimpfu:  o  módulo  gimpfu  define  as  funções  e  tipos  
necessários para o Python possa se comunicar com o GIMP.
▪ Definir  função  de  processamento:  a  função  que  será  utilizada  para  
processar a imagem, usando a API do GIMP.
▪ Registrar  a  função:  a  função  register() cadastra  a  função  de  
processamento na  Procedural Database  (PDB), permitindo que o  GIMP 
conheça as informações necessárias para executar o plugin.
▪ Executar main(): rotina principal da API.
A função de processamento terá realizar alguns passos para poder interagir  
corretamente com o GIMP:
▪ Receber variáveis: a função recebe como argumentos a imagem ( image), 
a camada corrente em edição ( drawable) e outros que forem definidos  
no registro da função. Os outros parâmetros serão obtidos através de  
uma caixa de dialogo apresentada ao usuário antes da execução.
▪ Iniciar  transação:  inicio  da  transação  através  da  função  
pdb.gimp_image_undo_group_start().  A  transação  pode  ser  desfeita  
posteriormente através de undo.
▪ Processar imagem: altera a imagem ou a camada através das funções  
definidas na API.
95 Site oficial: http://www.gimp.org/ .
96 Documentação disponível em: http://www.gimp.org/docs/python/index.html.

## Página 304

304 GIMP
▪ Terminar  transação:  encerra  a  transação  através  da  função  
pdb.gimp_image_undo_group_end().
Com isso, o processamento realizado pelo  plugin terá um comportamento  
conforme  com  outras  funcionalidades  presentes  no  software,  incluindo  a  
capacidade de ter a operação desfeita (undo).
Exemplo:
# -*- coding: latin1 -*-
# Importa a interface para o GIMP
from gimpfu import *
def stonify(img, drawable, fracture=135, picture=135):
    """"""
    # Inicia a transação para UNDO
    pdb.gimp_image_undo_group_start(img)
    
    # Cria uma camada de lava
    pdb.script_fu_lava(img, drawable, 10, 10, 7,
    'German flag smooth', 1, 1, 0)
    lava = img.layers[0]
    w, h = img.width, img.height
    
    # Cria uma camada de ruído
    rock = gimp.Layer(img, 'Rock', w, h, RGB_IMAGE,
    100, MULTIPLY_MODE)
    pdb.gimp_image_add_layer(img, rock, 0)
    pdb.plug_in_solid_noise(img, rock, 0, 0, 0, 1, 4, 4)
    
    # Aplica relevo nas camadas
    pdb.plug_in_bump_map(img, rock, lava,
    fracture, 45, 15, 0, 0, 0, 0, 1, 0, 0)
    pdb.plug_in_bump_map(img, rock, drawable,
    picture, 45, 30, 0, 0, 0, 0, 1, 0, 0)
    lava.visible = 0
    
    # Combina as camadas da imagem em uma só
    img.flatten()
    pdb.gimp_brightness_contrast (img.layers[0], 30, 10)
    
    # Termina a transação
    pdb.gimp_image_undo_group_end(img)

## Página 305

GIMP 305
# Registra a função na PDB
register(
    # Identificação
    'Stonify',
    '"Stonify" the image...',
    '"Stonify" the image with some noise',
    'Luiz Eduardo Borges',
    'Luiz Eduardo Borges',
    '2008-2010',
    # Localização no menu
    '<Image>/Filters/Render/Stonify...',
    # Modos suportados (todos) 
    '*',
    # Parâmetros
    [
        (PF_INT, 'fracture', 'Fracture power', 135),
        (PF_INT, 'picture', 'Picture power', 135)
    ],
    # Resultados
    [],
    stonify)
# Executa o plugin
main()
Janela de opções:
Exemplo dos passos para a geração da imagem:


## Página 306

306 GIMP
O GIMP também permite que os plugins sejam executados através de linha de  
comando, usando os parâmetros “--no-interface --batch”.
O script precisa estar numa pasta em que o GIMP possa encontra-lo. Para o  
GIMP 2.6, a pasta de plugins do usuário fica em .gimp-2.6/plug-ins abaixo do  
diretório home do usuário. Além disso, a extensão requer que PyGTK e suas  
dependências estejam instaladas.
Relevo
 Relevo
Ruído
Lava
Combina

## Página 307

Inkscape 307
Inkscape
O  editor  de  imagens  vetoriais  Inkscape97 permite  o  uso  do  Python  como  
linguagem script, para a criação de extensões. O aplicativo utiliza o SVG como 
formato nativo e implementa vários recursos previstos no padrão.
As extensões para o Inkscape servem principalmente para a implementação  
de filtros e efeitos. Enquanto outros aplicativos (como o Blender) apresentam  
uma  API  na  forma  de  módulos  para  o  interpretador,  o  Inkscape passa  
argumentos pela linha de comando e transfere informações pela entrada e  
saída  padrão  do  sistema  operacional,  de  forma  similar  aos  utilitários  de  
tratamento de texto encontrados em sistemas UNIX. Com isso, a extensão tem 
acesso apenas aos elementos que fazem parte do documento, e não a interface 
gráfica do aplicativo. Qualquer interação com o usuário durante a execução  
fica por conta da extensão.
A criação e manipulação das estruturas de dados é feita usando XML, como  
prevê a especificação do formato SVG, permitindo com isso o uso de módulos 
como o ElementTree.
Para simplificar o processo, o Inkscape provê o módulo chamado inkex, que 
define estruturas básicas para extensões. Com esse módulo, novas extensões  
podem ser criadas por herança a partir de uma classe chamada Effect.
Exemplo (randomtext.py):
#! /usr/bin/env python
# -*- coding: latin1 -*-
import random
import inkex
import simplestyle
class RandomText(inkex.Effect):
    """
    Repete um texto aleatoriamente dentro de uma área.
97 Site oficial: http://www.inkscape.org/.

## Página 308

308 Inkscape
    """
    def __init__(self):
        # Evoca a inicialização da superclasse
        inkex.Effect.__init__(self)
        # Adiciona um parâmetro para ser recebido do Inkscape
        self.OptionParser.add_option('-t', '--texto',
            action = 'store', type = 'string',
            dest = 'texto', default = 'Python',
            help = 'Texto para ser randomizado')
        self.OptionParser.add_option('-q', '--quantidade',
            action='store', type='int',
            dest='quantidade', default=20,
            help='Quantidade de vezes que o texto irá aparecer')
        self.OptionParser.add_option('-l', '--largura',
            action='store', type='int',
            dest='largura', default=1000,
            help='Largura da área')
        self.OptionParser.add_option('-c', '--altura',
            action='store', type='int',
            dest='altura', default=1000,
            help='Altura da área')
    def effect(self):
        # Pega as variáveis que foram passadas como
        # opções de linha de comando pelo Inkscape
        texto = self.options.texto
        quantidade = self.options.quantidade
        largura = self.options.largura
        altura = self.options.altura
        # Raiz do SVG
        svg = self.document.getroot()
        # Altura e largura do documento
        doc_largura  = inkex.unittouu(svg.attrib['width'])
        doc_altura = inkex.unittouu(svg.attrib['height'])
        # Cria uma camada no documento
        camada = inkex.etree.SubElement(svg, 'g')
        camada.set(inkex.addNS('label', 'inkscape'), 'randomtext')
        camada.set(inkex.addNS('groupmode', 'inkscape'), 'camada')

## Página 309

Inkscape 309
        for i in xrange(quantidade):
            # Cria um elemento para o texto
            xmltexto = inkex.etree.Element(inkex.addNS('text','svg'))
            xmltexto.text = texto
            # Posiciona o elemento no documento
            x = random.randint(0, largura) + (doc_largura -  largura) / 2
            xmltexto.set('x', str(x))
            y = random.randint(0, altura) + (doc_altura -  altura) / 2
            xmltexto.set('y', str(y))
            # Centraliza na vertical e na horizontal
            # e muda a cor de preenchimento usando CSS
            c = random.randint(100, 255)
            style = {'text-align' : 'center',
                'text-anchor': 'middle',
                'fill': '#%02x%02x%02x' % (c, c  - 30, c - 60)}
            xmltexto.set('style', simplestyle.formatStyle(style))
            # Coloca o texto na camada
            camada.append(xmltexto)
if __name__ == '__main__':
    rt = RandomText()
    rt.affect()
Para que o Inkscape reconheça a nova extensão, é necessário criar um arquivo 
XML  com  a  configuração,  que  informa  ao  aplicativo  os  módulos  e  os  
parâmetros usados pela extensão, incluindo os tipos, limites e valores padrão 
desses parâmetros, para que ele possa interagir com o usuário através de uma 
caixa  de  dialogo  antes  da  execução  para  obter  os  valores  desejados.  Os  
parâmetros são passados como argumentos na linha de comando quando o  
script é executado.
Arquivo de configuração (randomtext.inx):
<?xml version="1.0" encoding="UTF-8"?>
<inkscape-extension 
xmlns="http://www.inkscape.org/namespace/inkscape/extension">

## Página 310

310 Inkscape
    <_name>RandomText</_name>
      <id>org.ekips.filter.randomtext</id>
    <dependency type="executable" 
location="extensions">randomtext.py</dependency>
    <dependency type="executable" 
location="extensions">inkex.py</dependency>
    <param name="texto" type="string" _gui-text="Texto">Python</param>
    <param name="quantidade" type="int" min="1" max="500" _gui-
text="Quantidade">20</param>
    <param name="largura" type="int" min="1" max="10000" _gui-
text="Largura">1000</param>
    <param name="altura" type="int" min="1" max="10000" _gui-
text="Altura">1000</param>
    <effect>
    <object-type>all</object-type>
        <effects-menu>
            <submenu _name="Render"/>
        </effects-menu>
    </effect>
    <script>
        <command reldir="extensions" 
interpreter="python">randomtext.py</command>
    </script>
</inkscape-extension>
Janela com os parâmetros da extensão:
Exemplo de saída (quantidade igual a 100, largura igual a 600 e altura igual a  
200):


## Página 311

Inkscape 311
Tanto o programa quanto o arquivo de configuração precisam ficar na pasta  
de extensões (share\extensions, dentro da pasta de instalação, para a versão  
Windows) para que sejam encontrados pelo aplicativo e o nome do arquivo  
de configuração precisa ter extensão “.inx”.


## Página 312

312 BrOffice.org
BrOffice.org
BrOffice.org98 é um conhecido pacote de automação de escritórios de código  
aberto, que inclui editor de textos, planilha e outros aplicativos. Além disso, o  
BrOffice.org também suporta Python (entre outras linguagens):
▪ Como linguagem de macro, permitindo a automatização de tarefas.
▪ Para a construção de extensões (add ons).
▪ Em um serviço para atender conexões, através de uma API chamada  
UNO (Universal Network Objects).
Exemplo de macro:
# -*- coding: latin1 -*-
# A macro deve ser executada a partir do
# BrOffice.org Calc
def plan():
    """
    Preenche uma planilha
    """
    # Obtêm o documento para o contexto de script
    doc = XSCRIPTCONTEXT.getDocument()
    # A primeira planilha do documento
    sheet = doc.getSheets().getByIndex(0)
    col = lin = 0
    a = ord('A')
    # Cria uma linha com os títulos para as colunas
    for titulo in ('Jan', 'Fev', 'Mar', 'Total'):
        col += 1
        sheet.getCellByPosition(col, lin).setString(titulo)
        # E coloca uma fórmula com somatório na última linha
        coluna = chr(a + col)
        formula = '=SUM(%s2:%s6)' % (coluna, coluna)
        sheet.getCellByPosition(col, lin + 6).setFormula(formula)
98 Disponível em: http://www.broffice.org/.

## Página 313

BrOffice.org 313
    for lin in xrange(1, 6):
        # Numera as linhas
        sheet.getCellByPosition(0, lin).setValue(lin)
        # Coloca somatórios no fim de cada linha
        formula = '=SUM(B%d:D%d)' % (lin + 1, lin + 1)
        sheet.getCellByPosition(4, lin).setFormula(formula)
        
        # Preenche os dados
        for col in (1, 2, 3):
            sheet.getCellByPosition(col, lin).setFormula('=10*RAND()')
            # Substitui a fórmula pelo valor
            val = sheet.getCellByPosition(col, lin).getValue()
            sheet.getCellByPosition(col, lin).setValue(val)
    return None
Saída:
Para que o BrOffice.org possa identificar o script escrito em Python como um  
arquivo de macro, ele precisa estar na pasta para scripts em Python, que no  
Windows  fica  em  “Basis\share\Scripts\python”,  dentro  da  pasta  de  
instalação do BrOffice.org.


## Página 314

314 BrOffice.org
Exemplo de geração de relatório em PDF através do editor de texto (Writer),  
através da Python UNO Bridge:
# -*- coding: latin1 -*-
# Para iniciar o BrOffice.org como servidor:
# swriter.exe -headless
#   "-accept=pipe,name=py;urp;StarOffice.ServiceManager"
import os
import uno
from com.sun.star.beans import PropertyValue
# Dados...
mus = [('Artista', 'Faixa'),
    ('King Crimson', 'Starless'), ('Yes', 'Siberian Khatru'),
    ('Led Zeppellin', 'No Quarter'), ('Genesis', 'Supper\'s Ready')]
# Obtêm o número e o tamanho dos registros
rows = len(mus)
cols = len(mus[0])
# Inicio do "Boiler Plate"...
# Contexto de componente local
loc = uno.getComponentContext()
# Para resolver URLs
res = loc.ServiceManager.createInstanceWithContext(
    'com.sun.star.bridge.UnoUrlResolver', loc)
# Contexto para a URL
con = res.resolve('uno:pipe,name=py;urp;StarOffice.ComponentContext')
# Documento corrente
desktop = con.ServiceManager.createInstanceWithContext(
    'com.sun.star.frame.Desktop', con)
# Fim do "Boiler Plate"...
# Cria um documento novo no Writer
doc = desktop.loadComponentFromURL('private:factory/swriter',
    '_blank', 0, ())
# Cursor de texto

## Página 315

BrOffice.org 315
cursor = doc.Text.createTextCursor()
# Muda as propriedades do texto
cursor.setPropertyValue('CharFontName', 'Verdana')
cursor.setPropertyValue('CharHeight', 20)
cursor.setPropertyValue('CharWeight', 180)
# Insere o texto no documento
doc.Text.insertString(cursor, 'Músicas favoritas\n', 0)
# Cria tabela
tab = doc.createInstance('com.sun.star.text.TextTable')
tab.initialize(rows, cols)
doc.Text.insertTextContent(cursor, tab, 0)
# Preenche a tabela
for row in xrange(rows):
    for col in xrange(cols):
        cel = chr(ord('A') + col) + str(row + 1)
        tab.getCellByName(cel).setString(mus[row][col])
# Propriedades para exportar o documento
props = []
p = PropertyValue()
p.Name = 'Overwrite'
p.Value = True # Sobrescreve o documento anterior
props.append(p)
p = PropertyValue()
p.Name = 'FilterName'
p.Value = 'writer_pdf_Export' # Writer para PDF
props.append(p)
# URL de destino, no qual o arquivo PDF será salvo
url = uno.systemPathToFileUrl(os.path.abspath('musicas.pdf'))
# Salva o documento como PDF
doc.storeToURL(url, tuple(props))
# Fecha o documento
doc.close(True)
Saída (arquivo PDF):

## Página 316

316 BrOffice.org
A API do BrOffice.org é bastante completa e simplifica várias atividades que  
são lugar comum em programas para ambiente desktop.


## Página 317

Integração com outras linguagens 317
Integração com outras linguagens
Existe hoje muito código legado desenvolvido em diversas linguagens que  
pode ser aproveitado pelo Python, através de várias formas de integração.
Uma  forma  genérica  de  fazer  isso  é  gerar  uma  biblioteca  compartilhada  
(shared library) através do compilador da outra linguagem e fazer chamadas a  
funções que estão definidas na biblioteca.
Como a implementação original do Python é usando Linguagem C, é possível 
integrar Python e C nos dois sentidos:
▪ Python -> C (Python faz chamadas a um módulo compilado em C).
▪ C -> Python (C evoca o interpretador Python em modo embedded).
Também é possível integrar o Python com Fortran usando o utilitário f2py,  
que faz parte do projeto NumPy.
Bibliotecas compartilhadas
A partir da versão 2.5, o Python incorporou o módulo ctypes, que implementa 
tipos compatíveis com os tipos usados pela linguagem C e permite evocar  
funções de bibliotecas compartilhadas.
O módulo provê várias formas de evocar funções. Funções que seguem a  
convenção  de  chamada  stdcall,  como  a  API  do  Windows,  podem  ser  
acessadas  através  da  classe  windll.  Dynamic-link  library  (DLL)  é  a  
implementação de bibliotecas compartilhadas que são usadas no Windows.
Exemplo com windll:
# -*- coding: latin1 -*-
import ctypes
# Evocando a caixa de mensagens do Windows
# Os argumentos são: janela pai, mensagem,
# título da janela e o tipo da janela.
# A função retorna um inteiro, que

## Página 318

318 Integração com outras linguagens
# corresponde a que botão foi pressionado
i = ctypes.windll.user32.MessageBoxA(None,
    'Teste de DLL!', 'Mensagem', 0)
# O resultado indica qual botão foi clicado
print i
Para funções que seguem a convenção de chamada cdecl, usada pela maioria  
dos compiladores C, existe a classe cdll. Para as passagens de argumentos por  
referência é preciso criar uma variável que funciona como um  buffer para  
receber os resultados. Isso é necessário para receber strings, por exemplo.
Exemplo com cdll e buffer:
# -*- coding: latin1 -*-
import ctypes
# msvcrt é a biblioteca com a maioria das funções
# padrões da linguagens C no Windows
# O Windows coloca automaticamente
# a extensão do arquivo
clib = ctypes.cdll.msvcrt
# Cria um buffer para receber o resultado
# a referência para o buffer será passada para
# a função, que preenche o buffer com o resultado
s = ctypes.c_buffer('\000', 40)
# sscanf() é uma função que extrai valores
# de uma string conforme uma mascara
clib.sscanf('Testando sscanf!\n',
    'Testando %s!\n', s)
# Mostra o resultado
print s.value
É possível também evocar funções de bibliotecas compartilhadas no Linux:
# -*- coding: latin1 -*-

## Página 319

Integração com outras linguagens 319
import ctypes
# Carrega a biblioteca padrão C no Linux
# A extensão do arquivo precisa passada
# para a função LoadLibrary()
clib = ctypes.cdll.LoadLibrary("libc.so.6")
# Cria um buffer para receber o resultado
s = ctypes.c_buffer('\000', 40)
# Evoca a função sprintf
clib.sprintf(s, 'Testando %s\n', 'sprintf!')
# Mostra o resultado
print s.value
Através de bibliotecas compartilhadas é possível usar código desenvolvido  
em outras linguagens de uma maneira simples.
Python -> C
O módulo  escrito  em  C  deve  utilizar  as estruturas  do  Python (que  estão  
definidas na API de interface) para se comunicar com o interpretador Python.
Exemplo:
// Arquivo: mymodule.c
// Python.h define as estruturas do Python em C
#include <Python.h>
// No Python, mesmo os erros sao objetos
static PyObject *MyModuleError;
// Chamando a funcao "system" em C
static PyObject *
mymodule_system(PyObject *self, PyObject *args)
{
  const char *command;
  int sts;
  // "PyArg_ParseTuple" desempacota a tupla de parametros
  // "s" significa que ele deve identificar uma string

## Página 320

320 Integração com outras linguagens
  if (!PyArg_ParseTuple(args, "s", &command))
    // retornando NULL gera uma excessao
    // caso falte parametros
    return NULL;
  // chamando "system":
  sts = system(command);
  // "Py_BuildValue" gera objetos que o Python conhece
  // "i" significa inteiro
  return Py_BuildValue("i", sts);
}
// Tabela que o Python consulta para resolver
// os metodos do modulo e pode ser usado
// tambem para gerar a documentacao
// por instrospeccao: dir(), help(),...
static PyMethodDef MyModuleMethods[] = {
  {"system", mymodule_system, METH_VARARGS,
  "Executa comandos externos."},
  // Fim da tabela:
  {NULL, NULL, 0, NULL}
};
// inicializacao do modulo:
PyMODINIT_FUNC
initmymodule(void)
{
  // O modulo tambem e' um objeto
  PyObject *m;
  // "Py_InitModule" precisa do nome do modulo e da
  // tabela de metodos
  m = Py_InitModule("mymodule", MyModuleMethods);
  // Erros...
  MyModuleError = PyErr_NewException("mymodule.error",
    NULL, NULL);
  // "Py_INCREF" incrementa o numero de referencias do objeto
  Py_INCREF(MyModuleError);
  // "PyModule_AddObject" adiciona um objeto ao modulo
  PyModule_AddObject(m, "error", MyModuleError);
}
Ao  invés  de  compilar  o  módulo  manualmente,  use  o  Python  para  

## Página 321

Integração com outras linguagens 321
automatizar o processo. Primeiro, crie o script:
# Arquivo: setup.py
from distutils.core import setup, Extension
mymodule = Extension('mymodule', sources = ['mymodule.c'])
setup(name = 'MyPackage', version = '1.0',
    description = 'My Package',
    ext_modules = [mymodule])
E para compilar:
python setup.py build
O binário compilado será gerado dentro da pasta “build”. O módulo pode ser  
usado como qualquer outro módulo no Python (através de import).
C -> Python
O inverso  também é possível.  Um programa escrito em C pode evocar o  
interpretador Python seguindo três passos:
▪ Inicializar o interpretador.
▪ Interagir (que pode ser feito de diversas formas).
▪ Finalizar o interpretador.
Exemplo:
// Arquivo: py_call.c
// Python.h com as definicoes para
// interagir com o interpretador
#include <Python.h>
int main()
{
  // Inicializa interpretador Python
  Py_Initialize();
  // Executando codigo Python

## Página 322

322 Integração com outras linguagens
  PyRun_SimpleString("import os\n"
    "for f in os.listdir('.'):\n"
    "  if os.path.isfile(f):\n"
    "    print f, ':', os.path.getsize(f)\n");
  // Finaliza interpretador Python
  Py_Finalize();
  return 0;
}
Para compilar, é preciso passar a localização das headers e libraries do Python  
para o compilador C:
gcc -I/usr/include/python2.5 \
  -L/usr/lib/python2.5/config \
  -lpython2.5 -opy_call py_call.c
Observações:
▪ Esta API faz parte do CPython (porte do Python escrito em C).
▪ Existem ferramentas para automatizar o processo para gerar interfaces  
para sistemas maiores: SWIG, Boost.Python e SIP.

## Página 323

Integração com .NET 323
Integração com .NET
IronPython99 é a implementação do interpretador Python na linguagem C#.  
Embora  o  projeto  tenha  como  objetivo  a  compatibilidade  com  CPython,  
existem algumas diferenças entre elas. A principal vantagem do IronPython 
em  relação  ao  CPython  é  a  integração  com  componentes  baseados  no  
framework .NET.
O .NET é uma infra-estrutura de software criada pela Microsoft para a criação 
e execução de aplicações. A parte principal do .NET é o  Common Language  
Runtime (CLR),  que  provê  uma  série  recursos  aos  programas,  como  
gerenciamento  de  memória  para  as  aplicações.  Além  disso,  há  um  vasto  
conjunto de bibliotecas de componentes prontos para uso. As instruções das  
linguagens  de  programação  são  traduzidas  para  intermediate  language (IL)  
reconhecida pelo CLR, permitindo que várias linguagens sejam usadas.
Dentro  dos  recursos  disponíveis  no  framework,  existe  o  Dynamic Language  
99 Fontes, binários, exemplos, documentação e outras informações podem ser encontrados  
em: http://www.codeplex.com/Wiki/View.aspx?ProjectName=IronPython.
Fontes
Python
 Símbolos
 Árvore sintática
CLR
Compilação
Objetos 
IronPython
Gerador IL

## Página 324

324 Integração com .NET
Runtime  (DLR),  que  implementa  os  serviços  necessários  para  linguagens  
dinâmicas. O IronPython faz uso desses serviços.
Para evocar o modo interativo do IronPython:
ipy
Para executar um programa:
ipy prog.py
As bibliotecas do CPython podem ser usadas dentro do  IronPython, desde  
que as versões sejam compatíveis.
Exemplo:
import sys
# Acrescenta o caminho no PYTHONPATH
sys.path.append(r'c:\python25\lib')
import os
print os.listdir('.')
Exemplo usando um componente .NET:
from System.Diagnostics import Process
Process.Start('http://www.w3c.org/')
A função Start irá evocar o browser para abrir a URL.
Os objetos .NET podem ser usados ao invés dos builtins do Python:
import System
from System.Collections import  Hashtable
hash = Hashtable()

## Página 325

Integração com .NET 325
hash['baixo'] = '4 cordas'
hash['guitarra'] = '6 cordas'
for item in hash:
    print item.Key, '=>', item.Value
A classe Hashtable tem funcionalidade semelhante ao dicionário do Python.
Integração com outros componentes .NET adicionais, como o Windows Forms, 
que implementa a interface gráfica, é feita através do módulo  clr. Após a  
importação do módulo, o IronPython passa a usar os tipos do .NET, ao invés  
da biblioteca padrão do Python.
Exemplo com Windows Forms:
# -*- coding: utf-8 -*-
import clr
# Adiciona referências para esses componentes
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
# Importa os componentes
from System.Windows.Forms import *
from System.Drawing import *
# Cria uma janela
frm = Form(Width=200, Height=200)
# Coloca título na janela
frm.Text = 'Mini calculadora Python'
# Cria texto
lbl = Label(Text='Entre com a expressão:',
    Left=20, Top=20, Width=140)
# Adiciona a janela
frm.Controls.Add(lbl)
# Cria caixa de texto
txt = TextBox(Left=20, Top=60, Width=140)
# Adiciona a janela
frm.Controls.Add(txt)

## Página 326

326 Integração com .NET
# Função para o botão
def on_btn_click(*args):
    
    try:
        r = repr(eval(txt.Text))
        MessageBox.Show(txt.Text + '=' + r, 'Resultado')
    except:
        MessageBox.Show('Não foi possível avaliar: ' + \
            txt.Text, 'Erro')
# Cria botão
btn = Button(Text='Calcular!', Left=20, Top=100, Width=60)
btn.Click += on_btn_click
# Adiciona a janela
frm.Controls.Add(btn)
# Mostra a janela
frm.Show()
# Aplicação entra no loop de eventos,
# esperando pela interação do usuário
Application.Run(frm)
Interface do programa:
O mais comum é usar herança para especializar a classe de janela, em uma  
solução  mais  orientada  a  objetos,  encapsulando  o  código  da  criação  e  


## Página 327

Integração com .NET 327
manipulação dos controles. A segunda versão do programa usa herança e  
inclui um componente de layout: FlowLayoutPanel.
# -*- coding: utf-8 -*-
"""
Mini calculadora Python
"""
import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
from System.Windows.Forms import *
from System.Drawing import *
class Janela(Form):
    """
    Janela principal
    """
    def __init__(self):
        """
        Inicializa a janela
        """
        
        self.Width=200
        self.Height=200
        self.Text = 'Mini calculadora Python'
        self.lbl = Label(Text='Entre com a expressão:')
        self.txt = TextBox()
        self.btn = Button(Text='Calcular!')
        self.btn.Click += self.on_btn_click
        # Layout automático para os controles
        self.panel = FlowLayoutPanel(Dock = DockStyle.Fill)
        self.panel.Controls.Add(self.lbl)
        self.panel.Controls.Add(self.txt)
        self.panel.Controls.Add(self.btn)
        self.Controls.Add(self.panel)
        self.Show()
        Application.Run(self)

## Página 328

328 Integração com .NET
    def on_btn_click(self, *args):
        """
        Acontece quando o botão é pressionado
        """
        
        try:
            r = repr(eval(self.txt.Text))
            MessageBox.Show(self.txt.Text + ' = ' + r, 'Resultado')
        except:
            MessageBox.Show('Não foi possível avaliar: ' + \
                self.txt.Text, 'Erro')
if __name__ == '__main__':
    janela = Janela()
O IronPython pode ser usado com o Mono 100, que uma implementação Open 
Source da  especificação  do  .NET.  O  Mono  apresenta  a  vantagem  de  ser  
portável,  suportando  outras  plataformas  além  do  Windows,  porém  não  
implementa todos os componentes do .NET (como o Windows Forms). Existe 
também uma IDE para o IronPython, chamada IronPython Studio101.
100Endereço do projeto: http://www.mono-project.com/Main_Page.
101Disponível em: http://www.codeplex.com/IronPythonStudio.

## Página 329

Respostas dos exercícios I 329
Respostas dos exercícios I
1. Implementar duas funções:
▪ Uma que converta temperatura em graus Celsius para Fahrenheit.
▪ Outra que converta temperatura em graus Fahrenheit para Celsius.
Lembrando que:
Solução:
def celsius_fahrenheit(c=0):
    # round(n, d) => arredonda n em d casas decimais
    return round(9. * c / 5. + 32., 2)
def fahrenheit_celsius(f=0):
    
    return round(5. * (f - 32.) / 9., 2)
# Testes
print celsius_fahrenheit(123.0)
print fahrenheit_celsius(253.4)
2. Implementar uma função que retorne verdadeiro se o número for primo  
(falso caso contrário). Testar de 1 a 100.
Solução:
# -*- coding: latin1 -*-
# Testa se o número é primo
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
F = 9
5⋅C 32

## Página 330

330 Respostas dos exercícios I
        if not n % i:
            return False
    else:
        return True
# Para x de 1 a 100
for x in range(1, 101):
    if is_prime(x):
        print x
3. Implementar uma função que receba uma lista de listas de comprimentos  
quaisquer e retorne uma lista de uma dimensão.
Solução:
def flatten(it):
    """
    "Achata" listas...
    """
    # Se for uma lista
    if isinstance(it, list):
        ls = []
        # Para cada item da lista
        for item in it:
            # Evoca flatten() recursivamente
            ls = ls + flatten(item)
        return ls
    else:
        return [it]
# Teste
l = [[1, [2]], [3, 4], [[5, 6], 7]]
print flatten(l)
# imprime: [1, 2, 3, 4, 5, 6, 7]
4. Implementar uma função que receba um dicionário e retorne a soma, a  
média e a variação dos valores.
Solução:

## Página 331

Respostas dos exercícios I 331
# -*- coding: latin1 -*-
def stat(dic):
    # Soma
    s = sum(dic.values())
    # Média
    med = s / len(dic.values())
    # Variação
    var = max(dic.values()) - min(dic.values())
    return s, med, var
5. Escreva uma função que:
▪ Receba uma frase como parâmetro.
▪ Retorne uma nova frase com cada palavra com as letras invertidas.
Solução:
def reverse1(t):
    """
    Usando um loop convencional.
    """
    r = t.split()
    for i in xrange(len(r)):
        r[i] = r[i][::-1]
    return ' '.join(r)
def reverse2(t):
    """
    Usando Generator Expression.
    """
    return ' '.join(s[::-1] for s in t.split())
# Testes
f = 'The quick brown fox jumps over the lazy dog'
print reverse1(f)
print reverse2(f)
# mostra: "ehT kciuq nworb xof spmuj revo eht yzal god"

## Página 332

332 Respostas dos exercícios I
6. Crie uma função que:
▪ Receba uma lista de tuplas (dados), um inteiro (chave, zero por padrão  
igual) e um booleano (reverso, falso por padrão).
▪ Retorne dados ordenados pelo item indicado pela chave e em ordem  
decrescente se reverso for verdadeiro.
Solução:
def ord_tab(dados, chave=0, reverso=False):
    # Rotina para comparar as tuplas em sort()
    def _ord(x, y):
        return x[chave] - y[chave]
    dados.sort(_ord, reverse=reverso)
    return dados
# Testes
t = [(1, 2, 0), (3, 1, 5), (0, 3, 3)]
print ord_tab(t)
print ord_tab(t, 1)
print ord_tab(t, 2)
# Mostra:
# [(0, 3, 3), (1, 2, 0), (3, 1, 5)]
# [(3, 1, 5), (1, 2, 0), (0, 3, 3)]
# [(1, 2, 0), (0, 3, 3), (3, 1, 5)]

## Página 333

Respostas dos exercícios II 333
Respostas dos exercícios II
1.  Implementar  um  programa  que  receba  um  nome  de  arquivo  e  gere  
estatísticas  sobre  o  arquivo  (número  de  caracteres,  número  de  linhas  e  
número de palavras)
Solução 1:
(Economizando memória)
# -*- coding: latin1 -*-
filename = raw_input('Nome do arquivo: ')
in_file = file(filename)
c, w, l = 0, 0, 0
# Para cada linha do arquivo
for line in in_file:
    # Soma 1 ao número de linhas
    l += 1
    # Soma o tamanho da linha ao número de caracteres
    c += len(line)
    # Soma a quantidade de palavra
    w += len(line.split())
in_file.close()
print 'Bytes: %d, palavras: %d, linhas: %s' % (c, w, l)
Solução 2:
(Economizando código)
# -*- coding: latin1 -*-
filename = raw_input('Nome do arquivo: ')

## Página 334

334 Respostas dos exercícios II
# Lê o arquivo inteiro para uma string
chars = file(filename).read()
c = len(chars)
w = len(chars.split())
# Soma o número de caracteres de nova linha
l = chars.count('\n')
print 'Bytes: %d, palavras: %d, linhas: %s' % (c, w, l)
2. Implementar um módulo com duas funções:
▪ matrix_sum(*matrices), que retorna a matriz soma de matrizes de duas  
dimensões.
▪ camel_case(s), que converte nomes para CamelCase.
Solução:
# -*- coding: latin1 -*-
def matrix_sum(*matrices):
    """
    Soma matrizes de duas dimensões.
    """
    # Pegue a primeira matriz
    mat = matrices[0]
    # Para cada matriz da segunda em diante
    for matrix in matrices[1:]:
        # Para cada linha da matriz
        for x, row in enumerate(matrix):
            # Para cada elemento da linha
            for y, col in enumerate(row):
                # Some na matriz de resposta
                mat[x][y] += col
    return mat
def camel_case(s):
    """

## Página 335

Respostas dos exercícios II 335
    Formata strings DestaForma.
    """
    return ''.join(s.title().split())
if __name__ == '__main__':
    # Testes
    print matrix_sum([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    print camel_case('close to the edge')
3. Implementar uma função que leia um arquivo e retorne uma lista de tuplas  
com os dados (o separador de campo do arquivo é vírgula), eliminando as  
linhas  vazias.  Caso  ocorra  algum  problema,  imprima  uma  mensagem  de  
aviso e encerre o programa.
Script para gerar os dados de teste:
# -*- coding: latin1 -*-
# Importa o módulo para gerar
# números randômicos
import random
# Abre o arquivo
csv = file('test.csv', 'w')
for i in xrange(100):
    r = []
    for i in xrange(10):
        # random.randrange() escolhe números
        # dentro de um intervalo. A sintaxe
        # é a mesma da função range()
        r.append('%04d' %random.randrange(1000))
    csv.write(','.join(r) + '\n')
# Fecha o arquivo
csv.close()
Solução:

## Página 336

336 Respostas dos exercícios II
# -*- coding: latin1 -*-
def load_csv(fn):
    try:
        # Lê todas as linhas do arquivo
        lines = file(fn).readlines()
        new_lines = []
        for line in lines:
            new_line = line.strip()
            # Se houver caracteres na linha
            if new_line:
                # Quebra nas vírgulas, converte para tupla e
                # acrescenta na saída
                new_lines.append(tuple(new_line.split(',')))
        return new_lines
    # Tratamento de exceção
    except:
        print 'Ocorreu um erro ao ler o arquivo', fn
        raise SystemExit
4. Implementar um módulo com duas funções:
▪ split(fn, n) , que quebra o arquivo fn em partes de n  bytes e salva com  
nomes sequenciais (se fn = arq.txt, então arq_001.txt, arq_002.txt, ... )
▪ join(fn, fnlist) que junte os arquivos da lista fnlist em um arquivo só fn.
Solução:
# -*- coding: latin1 -*-
"""
breaker.py
"""
# Quebra o arquivo em fatias de n bytes
def split(fn, n):

## Página 337

Respostas dos exercícios II 337
    bytes = list(file(fn, 'rb').read())
    name, ext = fn.split('.')
    num = 1
    while bytes:
        out = ''.join(bytes[:n])
        del bytes[:n]
        newfn = '%s_%3d.%s' % (name, num, ext)
        file(newfn, 'wb').write(out)
        num += 1
# Junta as fatias em um arquivo
def join(fn, fnlist):
    out = ''
    for f in fnlist:
        out += file(f, 'rb').read()
    file(fn, 'wb').write(out)
if __name__ == '__main__':
    # Teste
    import glob
    split('breaker.py', 20)
    join('breaker2.py', sorted(glob.glob('breaker_*.py')))
5. Crie um script que:
▪ Compare a lista de arquivos em duas pastas distintas.
▪ Mostre os nomes dos arquivos que tem conteúdos diferentes e/ou que  
existem em apenas uma das pastas.
Solução:
# -*- coding: latin1 -*-
import os
# Nomes das pastas
pst1 = 'teste1'
pst2 = 'teste2'
# Lista o conteúdo das pastas
lst1 = os.listdir(pst1)

## Página 338

338 Respostas dos exercícios II
lst2 = os.listdir(pst2)
for fl in lst1:
    
    if fl in lst2:
        # Lê os arquivos e compara:
        if file(os.path.join(pst1, fl)).read() <> \
            file(os.path.join(pst2, fl)).read():
            print fl, 'diferente'
    # O arquivo não está na segunda pasta
    else:
        print fl, 'apenas em', pst1
for fl in lst2:
    # O arquivo não está na primeira pasta
    if not fl in lst1:
        print fl, 'apenas em', pst2
6. Faça um script que:
▪ Leia um arquivo texto.
▪ Conte as ocorrências de cada palavra.
▪ Mostre os resultados ordenados pelo número de ocorrências.
Solução:
# -*- coding: latin1 -*-
import string
# Lê o arquivo
texto = file('note.txt').read()
texto_limpo = ''
# Limpa o texto
for car in texto:
   if not car in string.punctuation:
       texto_limpo += car
# Separa as palavras
palavras = texto_limpo.split()

## Página 339

Respostas dos exercícios II 339
# Conta
resp = {}
for palavra in palavras:
   resp[palavra] = resp.get(palavra, 0) + 1
saida = resp.items()
# Ordena
def cmp(x, y):
   return x[-1] - y[-1]
saida.sort(cmp=cmp, reverse=True)
# Imprime
for k, v in saida:
   print k, '=>', v

## Página 340

340 Respostas dos exercícios III
Respostas dos exercícios III
1. Implementar um gerador de números primos.
Solução:
# -*- coding: latin1 -*-
# Verifica se o número é primo
def is_prime(n):
    if n < 2:
        return False
    for i in xrange(2, n):
        if not n % i:
            return False
    else:
        return True
# Gerador de números primos
def prime_gen():
    i = 1
    while True:
        if is_prime(i): yield i
        i += 1
# Teste: 100 primeiros primos
prime_iter = prime_gen()
for i in range(100):
    print prime_iter.next()
2. Implementar o gerador de números primos como uma expressão (dica: use  
o módulo itertools).
Solução:
# -*- coding: latin1 -*-

## Página 341

Respostas dos exercícios III 341
from itertools import count
# Verifica se o número é primo
def is_prime(n):
    if n < 2:
        return False
    for i in xrange(2, n):
        if not n % i:
            return False
    else:
        return True
# Generator Expression
primes = (i for i in count() if is_prime(i))
# Teste: 100 primeiros primos
for i in range(100):
    print primes.next()
3. Implementar um gerador que produza tuplas com as cores do padrão RGB  
(R, G e B variam de 0 a 255) usando xrange() e uma função que produza uma  
lista com as tuplas RGB usando range(). Compare a performance.
Solução:
# -*- coding: latin1 -*-
def rgb_lst():
    rgb = []
    for r in range(256):
        for g in range(256):
            for b in range(256):
                rgb.append((r, g, b))
    return rgb
def rgb_gen():
    for r in xrange(256):
        for g in xrange(256):
            for b in xrange(256):

## Página 342

342 Respostas dos exercícios III
                yield (r, g, b)
import time
tt = time.time()
l = rgb_lst()
print time.time() - tt
tt = time.time()
for color in rgb_gen(): pass
print time.time() - tt
4. Implementar um gerador que leia um arquivo e retorne uma lista de tuplas  
com os dados (o separador de campo do arquivo é vírgula), eliminando as  
linhas  vazias.  Caso  ocorra  algum  problema,  imprima  uma  mensagem  de  
aviso e encerre o programa.
Solução:
# -*- coding: latin1 -*-
def load_csv(fn):
    try:
        for line in file(fn):
            new_line = line.strip()
            if new_line:
                yield tuple(new_line.split(','))
    except:
        print 'Ocorreu um erro ao ler o arquivo', fn
        raise SystemExit
# Teste
for line in load_csv('teste.csv'):
    print line

## Página 343

Respostas dos exercícios IV 343
Respostas dos exercícios IV
1. Crie uma classe que modele um quadrado, com um atributo lado e os  
métodos: mudar valor do lado, retornar valor do lado e calcular área.
Solução:
# -*- coding: latin1 -*-
class Square(object):
    """
    Classe que modela um quadrado.
    """
    def __init__(self, side=1):
        self.side = side
    def get_side(self):
        return self.side
    
    def set_side(self, side):
        self.side = side
    
    def get_area(self):
        # A área é o quadrado do lado
        return self.side ** 2
# Testes
square = Square(2)
square.set_side(3)
print square.get_area()
2. Crie uma classe derivada de lista com um método retorne os elementos da  
lista sem repetição.
Solução:
# -*- coding: latin1 -*-

## Página 344

344 Respostas dos exercícios IV
class List(list):
    def unique(self):
        """
        Retorna a lista sem repetições.
        """
        res = []
        for item in self:
            if item not in res:
                res.append(item)
        return res
# Teste
l = List([1, 1, 2, 2, 2, 3, 3])
print l.unique()
3. Implemente uma classe Carro com as seguintes propriedades:
▪ Um veículo tem um certo consumo de combustível (medidos em km /  
litro) e uma certa quantidade de combustível no tanque.
▪ O consumo é especificado no construtor e o nível de combustível inicial 
é 0.
▪ Forneça um método mover(km) que receba a distância em quilômetros e  
reduza o nível de combustível no tanque de gasolina.
▪ Forneça  um  método  gasolina(),  que  retorna  o  nível  atual  de  
combustível.
▪ Forneça um método abastecer(litros), para abastecer o tanque.
Solução:
# -*- coding: latin1 -*-
class Carro(object):
    """
    Classe que calcula o consumo de um carro.
    """

## Página 345

Respostas dos exercícios IV 345
    tanque = 0
    def __init__(self, consumo):
        self.consumo = consumo
    def mover(self, km):
        gasto = self.consumo * km
        if self.tanque > gasto:
            self.tanque = self.tanque - gasto
        else:
            self.tanque = 0
    def abastecer(self, litros):
        self.tanque = self.tanque + litros
    def gasolina(self):
        return self.tanque
# Teste
carro = Carro(consumo=5)
carro.abastecer(litros=220)
carro.mover(km=20)
print carro.gasolina()
4. Implementar uma classe Vetor:
▪ Com coordenadas x, y e z.
▪ Que suporte soma, subtração, produto escalar e produto vetorial.
▪ Que calcule o módulo (valor absoluto) do vetor.
Solução:
# -*- coding: latin1 -*-
import math
class Vetor(object):

## Página 346

346 Respostas dos exercícios IV
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    def __repr__(self):
        return 'Vetor(x=%.1f, y=%.1f, z=%.1f)' % (self.x, self.y, self.z)
        
    def __add__(self, v):
        x = self.x + v.x
        y = self.y + v.y
        z = self.z + v.z
        return Vetor(x, y, z)
    def __sub__(self, v):
        x = self.x - v.x
        y = self.y - v.y
        z = self.z - v.z
        return Vetor(x, y, z)
    def __abs__(self):
        tmp = self.x ** 2 + self.y ** 2 + self.z ** 2
        return math.sqrt(tmp)
    def __mul__(self, v):
        if isinstance(v, Vetor):
            x = self.y * v.z - v.y * self.z
            y = self.z * v.x - v.z * self.x
            z = self.x * v.y - v.x * self.y
        else:
            x = self.x * float(v)
            y = self.y * float(v)
            z = self.z * float(v)
        return Vetor(x, y, z)
vetor = Vetor(1, 2, 3)
print abs(vetor)
print Vetor(4.5, 5, 6) + vetor
print Vetor(4.5, 5, 6) - vetor
print Vetor(4.5, 5, 6) * vetor

## Página 347

Respostas dos exercícios IV 347
print Vetor(4.5, 5, 6) * 5
5. Implemente um módulo com:
▪ Uma classe Ponto, com coordenadas x, y e z.
▪ Uma classe Linha, com dois pontos A e B, e que calcule o comprimento  
da linha.
▪ Uma  classe  Triangulo,  com  dois  pontos  A,  B  e  C,  que  calcule  o  
comprimento dos lados e a área.
Solução:
class Ponto(object):
    def __init__(self, x, y, z):
        # Coordenadas
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        
    def __repr__(self):
        
        return '(%2.1f, %2.1f, %2.1f)' % \
        (self.x, self.y, self.z)
class Linha(object):
    
    def __init__(self, a, b):
        # Pontos
        self.a = a
        self.b = b
    def comp(self):
        x = self.b.x - self.a.x
        y = self.b.y - self.a.y
        z = self.b.z - self.a.z
        
        return round((x ** 2 + y ** 2 + z ** 2)\
            ** .5, 1)
    def __repr__(self):

## Página 348

348 Respostas dos exercícios IV
        
        return '%s => %s' % \
        (self.a, self.b)
class Triangulo(object):
    def __init__(self, a, b, c):
        # Vertices
        self.a = a
        self.b = b
        self.c = c
        # Lados
        self.ab = Linha(a, b)
        self.bc = Linha(b, c)
        self.ca = Linha(c, a)
    def area(self):
        # Comprimento dos lados
        ab = self.ab.comp()
        bc = self.bc.comp()
        ca = self.ca.comp()
        # Semiperimetro
        p = (ab + bc + ca) / 2.
        # Teorema de Heron
        return round((p * (p - ab) * (p - bc) \
            * (p - ca)) ** .5, 1)
    def __repr__(self):
        return '%s => %s => %s)' % \
        (self.a, self.b, self.c)
# Testes
a = Ponto(2, 3, 1)
b = Ponto(5, 1, 4)
c = Ponto(4, 2, 5)
l = Linha(a, b)
t = Triangulo(a, b, c)
print 'Ponto A:', a
print 'Ponto B:', b
print 'Ponto C:', c

## Página 349

Respostas dos exercícios IV 349
print 'Linha:', l
print 'Comprimento:', l.comp()
print 'Triangulo:', t
print 'Area:', t.area()
# Mostra:
# Ponto A: (2.0, 3.0, 1.0)
# Ponto B: (5.0, 1.0, 4.0)
# Ponto C: (4.0, 2.0, 5.0)
# Linha: (2.0, 3.0, 1.0) => (5.0, 1.0, 4.0)
# Comprimento: 4.7
# Triangulo: (2.0, 3.0, 1.0) => (5.0, 1.0, 4.0) => (4.0, 2.0, 5.0))
# Area: 3.9

## Página 350

350 Respostas dos exercícios V
Respostas dos exercícios V
1. Implementar uma classe  Animal com os atributos: nome, espécie, gênero,  
peso, altura e idade. O objeto derivado desta classe deverá salvar seu estado  
em arquivo com um método chamado “salvar” e recarregar o estado em um  
método chamado “desfazer”.
Solução:
# -*- coding: latin1 -*-
import pickle
class Animal(object):
    """
    Classe que representa um animal.
    """
    attrs = ['nome', 'especie', 'genero', 'peso', 'altura', 'idade']
    def __init__(self, **args):
        # Crie os atributos no objeto a partir da lista
        # Os atributos tem None como valor default
        for attr in self.attrs:
            setattr(self, attr, args.get(attr, None))
    
    def __repr__(self):
        dic_attrs = {}
        for attr in self.attrs:
            dic_attrs[attr] = getattr(self, attr)
        return 'Animal: %s' % str(dic_attrs)
    def salvar(self):
        """
        Salva os dados do animal.
        """
        dic_attrs = {}
        for attr in self.attrs:
            dic_attrs[attr] = getattr(self, attr)
        pickle.dump(dic_attrs, file('a.pkl', 'w'))

## Página 351

Respostas dos exercícios V 351
    def desfazer(self):
        """
        Restaura os últimos dados salvos.
        """
        attrs = pickle.load(file('a.pkl'))
        for attr in attrs:
            setattr(self, attr, attrs[attr])
# Teste
gato = Animal(nome='Tinker', especie='Gato', genero='m',
    peso=6, altura=0.30, idade=4)
gato.salvar()
gato.idade = 5
print gato
gato.desfazer()
print gato
2. Implementar uma função que formate uma lista de tuplas como tabela  
HTML.
Solução:
# -*- coding: latin1 -*-
# O módulo StringIO implementa uma classe
# de strings que se comportam como arquivos
import StringIO
def table_format(dataset):
    """
    Classe que representa um animal.
    """
    out = StringIO.StringIO()
    out.write('<table>')
    for row in dataset:
        out.write('<tr>')
        for col in row:
            out.write('<td>%s</td>' % col)

## Página 352

352 Respostas dos exercícios V
        out.write('</tr>')
    out.write('</table>')
    out.seek(0)
    return out.read()
3.  Implementar  uma  aplicação  Web com  uma  saudação  dependente  do  
horário (exemplos: “Bom dia, são 09:00.”, “Boa tarde, são 13:00.” e “Boa noite,  
são 23:00.”).
Solução:
# -*- coding: latin1 -*-
import time
import cherrypy
class Root(object):
    """
    Raiz do site.
    """
    @cherrypy.expose
    def index(self):
        """
        Exibe a saudação conforme o horário do sistema.
        """
        # Lê a hora do sistema
        hour = '%02d:%02d' % time.localtime()[3:5]
        if '06:00' < hour <= '12:00':
            salute = 'Bom dia'
        elif '12:00' < hour <= '18:00':
            salute = 'Boa tarde'
        else:
            salute = 'Boa noite'
        # Retorna a mensagem para o browser
        return '%s, são %s.' % (salute, hour)
cherrypy.quickstart(Root())

## Página 353

Respostas dos exercícios V 353
4. Implementar uma aplicação Web com um formulário que receba expressões 
Python e retorne a expressão com seu resultado.
Solução:
# -*- coding: latin1 -*-
import traceback
import cherrypy
class Root(object):
    # Modelo para a página HTML
    template = '''
    <html><body>
    <form action="/">
    <input type="text" name="exp" value="%s" />
    <input type="submit" value="enviar">
    <pre>%s</pre>
    </body></html>'''
    @cherrypy.expose
    def index(self, exp=''):
        out = ''
        if exp:
            # Tente avaliar a expressão
            try:
                out = eval(exp)
            # Se der errado, mostre a mensagem do erro
            except:
                out = traceback.format_exc()
        return self.template % (exp, out)
cherrypy.quickstart(Root())

## Página 354

354 Respostas dos exercícios VI
Respostas dos exercícios VI
1. Implementar um módulo com uma função  tribonacci(n) que retorne uma  
lista de  n números de Tribonacci, aonde  n é o parâmetro da função. Faça  
testes da função caso o módulo seja executado como principal.
Solução:
# -*- coding: latin1 -*-
def tribonacci(n):
    """
    Retorna uma lista com n elementos de Tribonacci.
    
    >>> t = [1, 1, 2, 4, 7, 13, 24, 44, 81, 149, \
    274, 504, 927, 1705, 3136, 5768, 10609, 19513, \
    35890, 66012, 121415, 223317]
    >>> t == tribonacci(22)
    True
    >>> tribonacci('22')
    Traceback (most recent call last):
      File "pyro_server.py", line 26, in <module>
        print Dist().tribonacci('22')
      File "pyro_server.py", line 14, in tribonacci
        raise TypeError
    TypeError
    """
    if type(n) is not int:
        raise TypeError
    # Os 3 primeiros elementos da sequência
    t = [1, 1, 2]
    if n < 4:
        return t[:n]
    for i in range(3, n):
        
        # Soma os 3 elementos finais
        t.append(sum(t[-3:]))
        
    return t
def _doctest():

## Página 355

Respostas dos exercícios VI 355
    """
    Evoca o doctest.
    """
    
    import doctest
    doctest.testmod()
if __name__ == "__main__":
    _doctest()
2. Implementar:
▪ um servidor que publique um objeto distribuído e este evoque a função 
tribonacci.
▪ um cliente que use o objeto distribuído para calcular a sequência de  
Tribonacci.
Solução:
Servidor:
# -*- coding: latin1 -*-
import Pyro.core
# Importa o módulo com a função
import trib
class Dist(Pyro.core.ObjBase):
    @staticmethod
    def tribonacci(n):
        return trib.tribonacci(n)
if __name__ == '__main__':
    # Define a porta TCP/IP usada pelo Pyro
    Pyro.config.PYRO_PORT = 8888
    
    # Define o limite de cliente ao mesmo tempo
    Pyro.config.PYRO_MAXCONNECTIONS = 2000
    

## Página 356

356 Respostas dos exercícios VI
    Pyro.core.initServer()
    
    # norange=1 faz com que o Pyro sempre use a mesma porta
    daemon = Pyro.core.Daemon(norange = 1)
    # Define o limite de tempo
    daemon.setTimeout(300)
    uri = daemon.connect(Dist(),'dist')
    daemon.requestLoop()
Cliente:
# -*- coding: latin1 -*-
import Pyro.core
# URL com a porta
url = 'PYROLOC://127.0.0.1:8888/dist'
proxy = Pyro.core.getProxyForURI(url)
# Teste com até dez elementos
for i in range(10):
    print i + 1, '=>', proxy.tribonacci(i + 1)
Saída:
Pyro Client Initialized. Using Pyro V3.7
1 => [1]
2 => [1, 1]
3 => [1, 1, 2]
4 => [1, 1, 2, 4]
5 => [1, 1, 2, 4, 7]
6 => [1, 1, 2, 4, 7, 13]
7 => [1, 1, 2, 4, 7, 13, 24]
8 => [1, 1, 2, 4, 7, 13, 24, 44]
9 => [1, 1, 2, 4, 7, 13, 24, 44, 81]
10 => [1, 1, 2, 4, 7, 13, 24, 44, 81, 149]

## Página 357

Índice remissivo 357
Índice remissivo
Abstract Base Classes............................................................................................ 136
Arquivos................................................................................................................... 72
Arranjos.................................................................................................................. 197
Banco de dados........................................................................... 152, 165p., 168, 177
BGE...................................................................................................................... 301p.
Bibliotecas compartilhadas.................................................................................. 317
Bibliotecas de terceiros........................................................................................... 85
Blender........................................................................................... 13, 260, 290p., 299
BrOffice.org......................................................................... 13, 210, 289, 312pp., 316
Bytecode................................................................................................................ 16p.
CherryPy......................................................................................................... 181, 186
CherryTemplate..................................................................................... 181, 183, 186
Classes................................................................ 109pp., 114, 117, 120, 122, 127, 134
Comentários funcionais.......................................................................................... 22
Controle de fluxo..................................................................................................... 26
CPython.................................................................................................................... 14
DBI............................................................................................................... 166p., 177
Decoradores........................................................................................................... 107
Decoradores de classe........................................................................................... 139
Dicionários......................................................................................................... 45, 47
Doc Strings...................................................................................... 52, 58, 62, 90, 141
DOM.................................................................................................................. 159pp.
Duck Typing............................................................................................................ 15
ElementTree........................................................................................... 159, 162, 163
Empacotamento..................................................................................................... 283
Exceções................................................................................................................ 87p.
False.......................................................................................................................... 49
Ferramentas.............................................................................................................. 18
Firebird................................................................................................................ 169p.
Funções............................................................................................................... 38, 52
Game Engine............................................................................................ 290, 299pp.
Generator Expression............................................................................................ 104
Geradores................................................................................................................. 95
GIMP...................................................................................................... 13, 303p., 306
Glade............................................................................................................ 213p., 220

## Página 358

358 Índice remissivo
GTK+............................................................................................................ 211, 213p.
Herança........................................................................................................... 117, 120
Herança múltipla................................................................................................... 120
Histórico................................................................................................................... 14
IDE......................................................................................................................... 18p.
Inkscape.............................................................................................. 13, 289, 307pp.
Integração com .NET............................................................................................. 323
Interface gráfica..................................................................................................... 211
Introspecção.......................................................................................................... 90p.
IronPython................................................................................................ 323pp., 328
JSON................................................................................................................ 152, 157
Laços......................................................................................................................... 28
Lambda..................................................................................................................... 97
Lazy Evaluation....................................................................................................... 95
List Comprehension........................................................................................... 103p.
Listas................................................................................................................... 40, 43
Mapeamento objeto-relacional............................................................................ 177
Matplotlib............................................................................................................... 204
Matrizes.................................................................................................................. 200
Metaclasses..................................................................................................... 111, 134
Métodos de classe.................................................................................................. 112
Métodos de objeto................................................................................................. 112
Métodos estáticos.................................................................................................. 112
Modo interativo....................................................................................................... 17
Módulos................................................................................................. 62p., 68p., 85
MVC............................................................................................................. 185p., 194
MySQL................................................................................................................ 166p.
Name Mangling..................................................................................................... 113
Namespace......................................................................................................... 62, 66
None...................................................................................................................... 49p.
Números................................................................................................................... 32
NumPy............................................................................................................ 197, 202
Objetos......................................................................................................... 109p., 134
Objetos distribuídos.............................................................................................. 271
OpenGL............................................................................................. 253, 260pp., 267
Operadores booleanos............................................................................................ 50
ORM................................................................................................................ 177, 186

## Página 359

Índice remissivo 359
Performance...................................................................................... 271, 274, 279pp.
Perl............................................................................................................................ 14
Persistência................................................................................................. 151p., 185
Physics engine.................................................................................................... 300p.
PIL........................................................................................................................... 241
PostgreSQL...................................................................................... 13, 170p., 174pp.
Processamento de imagem................................................................................... 241
Processamento distribuído................................................................................... 268
Programação funcional........................................................................................... 97
Propriedades.......................................................................................................... 124
Psyco.................................................................................................................... 280p.
Py2exe............................................................................................................... 283pp.
PyDOC...................................................................................................................... 58
PyOpenGL.......................................................................................................... 260p.
PYRO................................................................................................................. 271pp.
Pythonic.................................................................................................................... 20
PYTHONPATH....................................................................................................... 62
Reflexão.................................................................................................................... 90
Ruby.......................................................................................................................... 14
SAX.............................................................................................................. 159, 161p.
Serialização..................................................................................................... 151, 154
SGDB............................................................................................................... 165, 177
Shell..................................................................................................................... 16pp.
Sintaxe................................................................................... 22, 26, 29, 40, 43, 45, 52
Sobrecarga de operadores............................................................................ 110, 127
SQL............................................................................................................ 165pp., 177
SQLite.......................................................................................................... 167p., 178
Strings...................................................................................... 34p., 37pp., 45, 52, 58
SVG................................................................................................. 240, 247pp., 307p.
SVGFig............................................................................................................ 249, 251
Tempo....................................................................................................................... 80
Testes automatizados............................................................................................ 141
Threads............................................................................................................. 147pp.
Tipagem dinâmica............................................................................................. 13, 15
Tipos.......................................................................................................................... 16
Imutáveis.................................................................................................. 31, 34, 42
Mutáveis.......................................................................................... 31, 39p., 43, 45

## Página 360

360 Índice remissivo
True........................................................................................................................... 49
Tuplas.................................................................................................................. 42pp.
Unpythonic.............................................................................................................. 20
Versões...................................................................................................................... 14
VPython....................................................................................................... 254p., 260
Web...................................................................................................... 158, 180p., 186
WxPython............................................................................................ 225p., 230, 232
XML................................................................................................... 152, 158pp., 186
YAML........................................................................................................ 152, 154pp.
ZODB................................................................................................................ 152pp.