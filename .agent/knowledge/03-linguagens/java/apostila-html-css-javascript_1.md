---json
{
  "id": "apostila-html-css-javascript_1",
  "title": "SOBRE ESTA APOSTILA",
  "categoria": "03-linguagens",
  "subcategoria": "java",
  "resumo": "12 + 13 14 * 3",
  "gatilhos": [
    "apostila",
    "css",
    "esta",
    "html",
    "java",
    "javascript",
    "linguagens",
    "sobre"
  ],
  "perguntas_tipo": [
    "Como utilizar SOBRE ESTA APOSTILA?",
    "Quais as boas praticas de java?"
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
  "dono": "stack-java",
  "prioridade": 2
}
---


--------------------------------------------------


--------------------------------------------------

Esta apostila da Caelum visa ensinar de uma maneira elegante, mostrando apenas o que é necessário e

quando é necessário, no momento certo, poupando o leitor de assuntos que não costumam ser de seu
interesse em determinadas fases do aprendizado.

A Caelum espera que você aproveite esse material. Todos os comentários, críticas e sugestões serão
muito bem-vindos.

Essa apostila é constantemente atualizada e disponibilizada no site da Caelum. Sempre consulte o
site para novas versões e, ao invés de anexar o PDF para enviar a um amigo, indique o site para que ele

possa sempre baixar as últimas versões. Você pode conferir o código de versão da apostila logo no ​nal
do índice.

Baixe sempre a versão mais nova em: www.caelum.com.br/apostilas

Esse material é parte integrante do treinamento Desenvolvimento Web com HTML, CSS e
JavaScript e distribuído gratuitamente exclusivamente pelo site da Caelum. Todos os direitos são

reservados à Caelum. A distribuição, cópia, revenda e utilização para ministrar treinamentos são
absolutamente vedadas. Para uso comercial deste material, por favor, consulte a Caelum previamente.

# SOBRE ESTA APOSTILA


--------------------------------------------------

**1**

**4**

**7**

**17**

**21**

**25**

**29**

**# Sumário**

**1 A estrutura dos arquivos de um projeto**

1.1 Web site ou aplicação Web?
1

1.2 Editores e IDEs
2

**2 Exercício: Baixando os arquivos do curso**

2.1 Objetivo
4

2.2 Passo a passo com código
5

**3 Introdução ao HTML**

3.1 Exibindo informações na Web
7

3.2 Sintaxe do HTML
12

3.3 Tags HTML
13

3.4 Imagens
14

3.5 Primeira página
15

**4 Exercício: Primeiros passos com HTML**

4.1 Objetivo
17

4.2 Passo a passo com código
18

**5 Estrutura de um documento HTML**

5.1 A tag <html>
21

5.2 A tag <head>
22

5.3 A tag <body>
22

5.4 A instrução DOCTYPE
23

**6 Exercício: A Especificação HTML**

6.1 Objetivo
25

6.2 Passo a passo com código
26

**7 Estilizando com CSS**

7.1 Sintaxe e inclusão de CSS
29

7.2 Propriedades tipográficas e fontes
32

Sumário
Caelum


--------------------------------------------------

**37**

**41**

**45**

**48**

**51**

**55**

**61**

**66**

**68**

**73**

**74**

7.3 Alinhamento e decoração de texto
33

7.4 Imagem de fundo
34

7.5 Bordas
34

7.6 Cores na Web
35

**8 Exercício: Mudando o visual da nossa página**

8.1 Objetivo
37

8.2 Passo a passo com código
38

**9 Espaçamentos e dimensões**

9.1 Dimensões
41

9.2 Espaçamentos
42

**10 Exercício: Trabalhando com tamanhos e espaçamento**

10.1 Objetivo
45

10.2 Passo a passo com código
46

**11 Listas HTML**

11.1 Listas de definição
48

11.2 Links no HTML
49

**12 Exercício: Usando links e listas**

12.1 Objetivo
51

12.2 Passo a passo com código
52

**13 Seletores mais específicos e herança**

13.1 Para saber mais: o valor inherit
59

**14 Exercício: Selecionando elementos mais específicos e herança**

14.1 Objetivo
61

14.2 Passo a passo com código
62

**15 Desacoplamento com classes**

**16 Exercício: Usando classes para evitar acoplamento de estilos**

16.1 Objetivo
68

16.2 Passo a passo com código
69

**17 Elementos estruturais e semântica dos elementos**

**18 Exercício: Semantica em primeiro lugar**

18.1 Objetivo
74

18.2 Passo a passo com código
75

Caelum
Sumário


--------------------------------------------------

**78**

**83**

**87**

**92**

**97**

**99**

**104**

**110**

**115**

**121**

**125**

**19 Conhecendo padrões de CSS**

19.1 Tipos de display
79

**20 Exercício: Treinando display e nomenclatura de classes**

20.1 Objetivo
83

20.2 Passo a passo com código
83

**21 Exercício: Um pouco sobre estilização com blocos**

21.1 Objetivo
87

21.2 Passo a passo com código
87

**22 Exercício: Modificadores**

22.1 Objetivo
92

22.2 Passo a passo com código
92

**23 Unidades relativas com EM e REM**

**24 Exercício: Medidas relativas em e rem**

24.1 Objetivo
99

24.2 Passo a passo com código
99

**25 Site mobile ou mesmo site?**

25.1 CSS media types
105

25.2 CSS3 media queries
106

25.3 Viewport
107

25.4 Responsive Web Design
108

25.5 Mobile-first
109

**26 Exercício: Responsividade com viewport e unidades relativas**

26.1 Objetivo
110

26.2 Passo a passo com código
110

**27 Exercício: Responsividade com `@media`**

27.1 Objetivo
115

27.2 Passo a passo com código
117

**28 O processo de desenvolvimento de uma tela**

28.1 Analisando o Layout
122

**29 Exercício: Estrutura da página principal e o cabeçalho**

29.1 Objetivo
125

29.2 Passo a passo com código
127

30.1 CSS Reset
132

Sumário
Caelum


--------------------------------------------------

**136**

**143**

**146**

**150**

**152**

**154**

**156**

**158**

**162**

**166**

**171**

**176**

30.2 Fontes Próprias
133

30.3 Modularizando Componentes com CSS Isolados
134

**30 Exercício: Começando a estilizar o `header` da home**

31.1 Objetivo
136

31.2 Passo a passo com código
140

**31 Progressive Enhancement**

32.1 Condições, opções, limitações e restrições
143

**32 Exercício: Progressive Enhancement**

33.1 Objetivo
146

33.2 Passo a passo com código
147

**33 Display Flex**

34.1 Flex Container
150

**34 Exercício: Novos Layouts com Flexbox**

35.1 Objetivo
152

35.2 Passo a passo com código
153

**35 Exercício: Novos Layouts com Flexbox B**

36.1 Objetivo
154

36.2 Passo a passo com código
154

**36 Responsividade e Fallback**

**37 Exercício: Responsividade e fallback**

38.1 Objetivo
158

38.2 Passo a passo com código
159

**38 Exercício: Desafio: crie o HTML do rodapé**

39.1 Objetivo
162

39.2 Passo a passo com código
163

**39 Exercício: Conteúdo Rodapé**

40.1 Objetivo
166

40.2 Passo a passo com código
167

**40 Exercício: Espaçando o conteúdo do rodapé - os detalhes nas entrelinhas e margens**

41.1 Objetivo
171

41.2 Passo a passo com código
172

**41 Exercício: O formulário de newsletter do rodapé**

Caelum
Sumário


--------------------------------------------------

**181**

**187**

**190**

**197**

**206**

**216**

**222**

**231**

**239**

**247**

**255**

42.1 Objetivo
176

42.2 Passo a passo com código
177

**42 Exercício: Embaralhando os itens do rodapé em telas maiores com Flexbox**

43.1 Objetivo
181

43.2 Passo a passo com código
182

**43 Exercício: Rodapé em telas grandes sem sobrescrever tudo o que veio antes**

44.1 Objetivo
187

44.2 Passo a passo com código
187

**44 Exercício: O componente container**

45.1 Objetivo
190

45.2 Passo a passo com código
190

**45 Display: grid**

46.1 grid-template-columns
202

46.2 grid-template-rows
202

**46 Exercício: Conteúdo principal - a vitrine de cursos**

47.1 Objetivo
206

47.2 Passo a passo com código
207

**47 Exercício: Conteúdo Principal**

48.1 Objetivo
216

48.2 Passo a passo com código
217

**48 Exercício: Conteúdo principal (opcional) - os planos**

49.1 Objetivo
222

49.2 Passo a passo com código
223

**49 Exercício: Conteúdo Principal - os benefícios**

50.1 Objetivo
231

50.2 Passo a passo com código
232

**50 Exercício: Conteúdo Principal (opcional) - chamada youtube**

51.1 Passo a passo com código
239

**51 Exercício: Conteúdo Principal - chamada dos aplicativos**

52.1 Objetivo
247

52.2 Passo a passo com código
248

**52 Bootstrap e frameworks de CSS**

53.1 Estilo e componentes base
255

Sumário
Caelum


--------------------------------------------------

**258**

**260**

**262**

**266**

**280**

**284**

**53 Exercício: Primeiros passos com Bootstrap**

54.1 Objetivo
258

54.2 Passo a passo com código
258

**54 Exercício: Customizando o Bootstrap (opicional)**

55.1 Objetivo
260

55.2 Passo a passo com código
260

**55 Exercício: A tabela de cursos**

56.1 Objetivo
262

56.2 Passo a passo com código
262

**56 Um pouquinho da história do JavaScript**

57.1 História
266

57.2 Características da linguagem
267

57.3 Console do navegador
267

57.4 Sintaxe básica
268

57.5 A tag script
270

57.6 JavaScript em arquivo externo
271

57.7 Mensagens no console
271

57.8 DOM: sua página no mundo JavaScript
272

57.9 querySelector
272

57.10 Elemento da página como variável
273

57.11 querySelectorAll
273

57.12 Alterações no DOM
274

57.13 Funções e os eventos do DOM
274

57.14 Funções Anônimas
275

57.15 Manipulando strings
276

57.16 Imutabilidade
276

57.17 Conversões
277

57.18 Manipulando números
277

57.19 Concatenações
277

**57 Exercício: Calculando total de horas e cursos com JavaScript**

58.1 Objetivo
280

58.2 Passo a passo com código
280

**58 Propriedades CSS**

59.1 Propriedade font
284

59.2 Propriedade text
284

Caelum
Sumário


--------------------------------------------------

59.3 Propriedade letter-spacing
284

59.4 Propriedade line-height
285

59.5 Propriedades de cor
285

59.6 Propriedade background
285

59.7 Propriedade border
285

59.8 Propriedade vertical-align
286

59.9 Propriedades width e height
286

59.10 Propriedade box-sizing
286

59.11 Propriedade overflow
287

Versão: 25.0.25

Sumário
Caelum


--------------------------------------------------

CAPÍTULO 1

Como todo tipo de projeto de software, existem algumas recomendações quanto à organização dos
arquivos de um site. Não há nenhum rigor técnico quanto a essa organização e, na maioria das vezes,

você vai adaptar as recomendações da maneira que for melhor para o seu projeto.

Como um site é um conjunto de páginas Web sobre um assunto, empresa, produto ou qualquer outra
coisa, é comum todos os arquivos de um site estarem dentro de uma só pasta e, assim como um livro, é
recomendado que exista uma "capa", uma página inicial que possa indicar para o visitante quais são as

outras páginas que fazem parte desse projeto e como ele pode acessá-las, como se fosse o **índice** do site.

Ter esse índice, não por coincidência, é uma convenção adotada pelos servidores de páginas Web. Se
desejamos que uma determinada pasta seja servida como um site e dentro dessa pasta existe um arquivo
chamado **index.html**, esse arquivo será a página inicial, ou seja o índice, a menos que alguma

configuração determine outra página para esse fim.

Dentro da pasta do site, no mesmo nível que o  index.html , é recomendado que sejam criadas mais

algumas pastas para manter separados os arquivos de imagens, as folhas de estilo e os scripts. Para
iniciar um projeto, teríamos uma estrutura de pastas como a demonstrada na imagem a seguir:

Muitas vezes, um site é servido por meio de uma aplicação Web e, nesses casos, a estrutura dos
arquivos depende de como a aplicação necessita dos recursos para funcionar corretamente. Porém, no
geral, as aplicações também seguem um padrão bem parecido com o que estamos adotando para o nosso

projeto.

Quando estamos começando no mundo do desenvolvimento Web, acabamos por conhecer muitos

termos novos, que por muitas vezes não são claros ou nos causam confusão. Vamos entender um pouco
mais agora, qual a diferença de um Web site e uma aplicação Web.

# A ESTRUTURA DOS ARQUIVOS DE UM
# PROJETO

## 1.1 WEB SITE OU APLICAÇÃO WEB?

1 A ESTRUTURA DOS ARQUIVOS DE UM PROJETO 
**1**


--------------------------------------------------

Podemos considerar um Web site uma coleção de páginas HTML estáticas, ou seja, que não
interagem com um banco de dados através de uma linguagem de servidor Web. Ou seja, aqui todo o
conteúdo do site está escrito diretamente no documento HTML, assim como as imagens e outras mídias.

Claro que, para qualquer página Web ser fornecida publicamente a mesma deve estar hospedada em um
simples servidor Web (hospedagem de sites).

Uma aplicação Web pode conter uma coleção de páginas, porém o conteúdo destas páginas é

montado dinamicamente, ou seja, é carregado através de solicitações (requisições) à um banco de dados,
que conterá armazenado os textos e indicação dos caminhos das imagens ou mídias que a página precisa

exibir. Porém um HTML não tem acesso direto à um banco de dados, e esta comunicação deve ser feita
por uma linguagem de programação de servidor Web. Esta aplicação escrita com uma linguagem de
servidor que tem o poder de acessar o banco de dados e montar a página HTML conforme o solicitado

pelo navegador. Estas solicitações podem ser feitas de várias maneiras, inclusive utilizando JavaScript.
Portanto uma aplicação Web é mais complexa porque precisa de uma linguagem de servidor para poder
intermediar as solicitações do navegador, um banco de dados, e muitas vezes (porém não

obrigatoriamente) exibir páginas HTML com estes conteúdos.

Exemplo de linguagens de servidor Web: Java EE, PHP, Python, Ruby on Rails, NodeJS etc...

Se você está gostando dessa apostila, certamente vai aproveitar os **cursos**
**online** que lançamos na plataforma **Alura**. Você estuda a qualquer momento

com a **qualidade** Caelum. Programação, Mobile, Design, Infra, Front-End e
Business, entre outros! Ex-estudante da Caelum tem 10% de desconto, siga o link!

Conheça a Alura Cursos Online.

Os editores de texto são programas de computador leves e ideais para escrever e editar as páginas de
um 
site, 
como 
*Visual *
*Studio *
*Code* 
(https://code.visualstudio.com/), 
*Sublime*
(https://www.sublimetext.com/), *Atom* (https://atom.io/) e *Notepad++* (https://notepad-plus-plus.org),

que possuem realce de sintaxe e outras ferramentas para facilitar o desenvolvimento de páginas.

**### Web site**

**### Aplicação Web**

**Agora é a melhor hora de aprender algo novo**

## 1.2 EDITORES E IDES

**2** 
1.2 EDITORES E IDES


--------------------------------------------------

Há também **IDE**s (*Integrated Development Environment*) que são editores mais robustos e trazem
mais facilidades para o desenvolvimento de aplicações Web, se integrando com outras funcionalidades.
São alguns deles: *WebStorm* (https://www.jetbrains.com/webstorm/) *Eclipse* (https://www.eclipse.org/) e

*Visual Studio* (https://visualstudio.microsoft.com).

1.2 EDITORES E IDES 
**3**


--------------------------------------------------

CAPÍTULO 2

Nesse curso criaremos um site com várias páginas e criaremos vários arquivos pra isso. Para sua

organização, recomendamos que crie uma pasta para colocar todos esses arquivos. Tome cuidado para
não criar essa pasta em um lugar muito escondido no seu computador e acabar esquecendo onde estão os
arquvios.

Nossa recomendação é que crie essa pasta com o nome **"projeto-musicdot"** na **"Área de**

**Trabalho"**. Assim, durante os exercícios, os seus arquivos estarão sempre acessíveis à um clique e você
não precisará ficar navegando pelas pastas do seu computador à procura dos seus arquivos. Se você
estiver confortável com seu computador e tiver algum nome e lugar favorito para criar essa pasta, fique

à vontade.

Antes de escrever qualquer código do projeto, você também já pode pegar todos os arquivos de
imagens e estilo do curso que estão prontos e copiar eles para a pasta **"projeto-musicdot"** que acabou
de criar.

Nas máquina da Caelum, vá para a **"Área de Trabalho"**, abra a pasta **"Arquivos do Curso"** e

procure pela pasta **"WD43"**. **Copie** todo o conteúdo dessa pasta **"WD43"** para a pasta **"projeto-**
**musicdot"** que você criou.

Se estiver no seu computador, faça o download dos arquivos no seguinte endereço:
https://www.caelum.com.br/download/caelum-arquivos-wd43.zip

# EXERCÍCIO: BAIXANDO OS ARQUIVOS
# DO CURSO

## 2.1 OBJETIVO

**4** 
2 EXERCÍCIO: BAIXANDO OS ARQUIVOS DO CURSO


--------------------------------------------------

Abrindo o projeto no Visual Studio Code:

Clique no menu **ARQUIVO > ABRIR PASTA** e escolha a pasta **"projeto-musicdot"** que
você criou na **"Área de Trabalho"**. Agora o *Visual Studio Code* vai ter acesso a todos os arquivos

do curso, e sempre que você criar novos arquivos pelo editor eles já vão ser criados dentro da pasta.

Confira na barra lateral da esquerda se todos os arquivos aparecem como na imagem abaixo:

Figura 2.1: Barra lateral do VS Code com os arquivos do curso

Conheça a **Casa do Código**, uma **nova** editora, com autores de destaque no
mercado, foco em **ebooks** (PDF, epub, mobi), preços **imbatíveis** e assuntos

**atuais**.
Com a curadoria da **Caelum** e excelentes autores, é uma abordagem **diferente**
para livros de tecnologia no Brasil.

Casa do Código, Livros de Tecnologia.

1. Há 43 arquivos a serem adicionados nas pastas css, img, js, textos e video. Note que esses arquivos
foram disponibilizados já prontos para você.

Os 43 arquivos devem ser adicionados na seguinte estrutura de pastas:

**Seus livros de tecnologia parecem do século passado?**

## 2.2 PASSO A PASSO COM CÓDIGO

2.2 PASSO A PASSO COM CÓDIGO 
**5**


--------------------------------------------------

 └─ pasta_raiz_do_projeto
    ├─ css
    │  ├─ bootstrap.css
    │  └─ reset.css
    ├─ img
    │  ├─ familia-tupfeln.jpg
    │  ├─ favicon.ico
    │  ├─ footer-icone-facebook.svg
    │  ├─ footer-icone-instagram.svg
    │  ├─ footer-icone-youtube.svg
    │  ├─ home-background-mobile.png
    │  ├─ home-background.png
    │  ├─ icone-android-logo.svg
    │  ├─ icone-apple-logo.svg
    │  ├─ icone-beneficios-didatica-cuidadosa.svg
    │  ├─ icone-beneficios-nenhuma-duvida.svg
    │  ├─ icone-beneficios-online.svg
    │  ├─ icone-beneficios-tudo-para-voce.svg
    │  ├─ icone-cordas.svg
    │  ├─ icone-teclado-piano.svg
    │  ├─ icone-youtube.svg
    │  ├─ icones-audio.svg
    │  ├─ icones-baixo.svg
    │  ├─ icones-bateria.svg
    │  ├─ icones-canto.svg
    │  ├─ icones-percussao.svg
    │  ├─ icones-sopro.svg
    │  ├─ icones-teoria.svg
    │  ├─ icones-violao-guitarra.svg
    │  ├─ logo.svg
    │  ├─ matriz-musicdot-antiga.jpg
    │  ├─ matriz-musicdot.png
    │  ├─ mockup-app.png
    │  ├─ musicdot-logo-light.svg
    │  ├─ planos-background-mobile.png
    │  ├─ planos-background.png
    │  ├─ play-button.svg
    │  ├─ simbolo-musidot-branco.svg
    │  ├─ simbolo-musidot-dark.svg
    │  ├─ video-principal-mobile.png
    │  ├─ video-principal.png
    │  ├─ videos-thumbnail-video1.png
    │  └─ videos-thumbnail-video2.png
    ├─ js
    │  └─ bootstrap.js
    ├─ textos
    │  └─ sobre.txt
    └─ video
       └─ video-promocional.mp4

**# novos arquivos do projeto**

**6** 
2.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

CAPÍTULO 3

*"Quanto mais nos elevamos, menores parecemos aos olhos daqueles que não sabem voar." -- Friedrich*

*Wilhelm Nietzsche*

A única linguagem que um navegador Web consegue interpretar para a exibição de conteúdo é o
HTML. Para iniciar a exploração do HTML, vamos imaginar o seguinte caso: o navegador realizou uma
requisição e recebeu como corpo da resposta o seguinte conteúdo:

 MusicDot

 Bem-vindo à MusicDot, seu portal de cursos de música online.

 Confira nossas promoções.
 Receba informações sobre nossos lançamentos por email.
 Navegue por todos nossos cursos disponíveis.
 Aprenda sem sair de casa.

Para conhecer o comportamento dos navegadores quanto ao conteúdo descrito antes, vamos
reproduzir esse conteúdo em um arquivo de texto comum, que pode ser criado com qualquer editor de

texto puro. Salve o arquivo como **index.html** e abra-o a partir do navegador à sua escolha.

# INTRODUÇÃO AO HTML

## 3.1 EXIBINDO INFORMAÇÕES NA WEB

3 INTRODUÇÃO AO HTML 
**7**


--------------------------------------------------

Parece que obtemos um resultado um pouco diferente do esperado, não? Apesar de ser capaz de
exibir texto puro em sua área principal, algumas regras devem ser seguidas caso desejemos que esse
texto seja exibido com alguma formatação, para facilitar a leitura pelo usuário final.

Uma nota de atenção é que a imagem acima foi tirada dos navegadores: **Microsoft Edge e**

**Microsoft Internet Explorer 11**. Veja o que acontece quando obtemos a mesma imagem porém com
navegadores mais atuais:

**8** 
3.1 EXIBINDO INFORMAÇÕES NA WEB


--------------------------------------------------

A imagem acima foi tirada nos navegadores: **Brave, Mozilla Firefox e Google Chrome**.

*Obs: existe a possibilidade de que mesmo nesses navegadores, se utilizada uma versão mais antiga,*
*pode ser que o texto seja mostrado igual na foto dos navegadores da Microsoft*.

Usando os resultados acima podemos concluir que os navegadores mais antigos e até mesmo o

**Microsoft Edge** por padrão:

Podem não exibir caracteres acentuados corretamente;

Mas até mesmo nos navegadores mais novos:

Não exibem quebras de linha.

Para que possamos exibir as informações desejadas com a formatação, é necessário que cada trecho
de texto tenha uma **marcação** indicando qual é o significado dele. Essa marcação também influencia a

maneira com que cada trecho do texto será exibido. A seguir é listado o texto com esta marcação
esperada pelo navegador:

*<!DOCTYPE html>*
<html>

 <head>
   <title>MusicDot</title>
   <meta charset="utf-8">
 </head>

3.1 EXIBINDO INFORMAÇÕES NA WEB 
**9**


--------------------------------------------------

 <body>
   <h1>MusicDot</h1>
   <h2>Bem-vindo à MusicDot, seu portal de cursos de música online.</h2>
   <ul>
     <li>Confira nossas promoções.</li>
     <li>Receba informações sobre nossos lançamentos por email.</li>
     <li>Navegue por todos nossos cursos disponíveis.</li>
     <li>Aprenda sem sair de casa.</li>
   </ul>
 </body>
</html>

O texto com as devidas marcações, comumente chamado de "código". Reproduza então o código

anterior em um novo arquivo de texto puro e salve-o como **index-2.html**. Não se preocupe com a
sintaxe, vamos conhecer detalhadamente cada característica destas marcações nos próximos capítulos.
Abra o arquivo no navegador.

**10** 
3.1 EXIBINDO INFORMAÇÕES NA WEB


--------------------------------------------------

Agora, uma página muito mais agradável e legível é exibida. Para isso, tivemos que adicionar as
marcações que são pertencentes ao HTML. Essas marcações são chamadas de **tags**, e elas basicamente
dão uma **representação** ao texto contido entre sua abertura e fechamento.

Apesar de estarem corretamente marcadas, as informações não apresentam pouco ou nenhum
atrativo estético e, nessa deficiência do HTML, reside o primeiro e maior desafio de pessoas que

desenvolvem para *front-end*.

3.1 EXIBINDO INFORMAÇÕES NA WEB 
**11**


--------------------------------------------------

O HTML (*Hypertext Markup Language*) ou linguagem de marcação de hipertexto foi desenvolvido
para suprir a necessidade exibição de documentos científicos fornecidos por uma rede de Internet. Para
termos uma comparação, é como se a Web fosse desenvolvida para exibir monografias redigidas e

formatadas pela Metodologia do Trabalho Científico da ABNT. Porém, com o tempo e a evolução da
Web e de seu potencial comercial, tornou-se necessária a exibição de informações com grande riqueza

de elementos gráficos e de interação.

Começaremos por partes, primeiro entenderemos como o HTML funciona, para depois aprendermos

estilos, elementos gráficos e interações.

Se você está gostando dessa apostila, certamente vai aproveitar os **cursos**

**online** que lançamos na plataforma **Alura**. Você estuda a qualquer momento
com a **qualidade** Caelum. Programação, Mobile, Design, Infra, Front-End e
Business, entre outros! Ex-estudante da Caelum tem 10% de desconto, siga o link!

Conheça a Alura Cursos Online.

O HTML é um conjunto de **tags** responsáveis pela marcação do conteúdo de uma página no
navegador. No código que vimos antes, as tags são os elementos a mais que escrevemos usando a

sintaxe  <nomedatag> . Diversas tags são disponibilizadas pela linguagem HTML e cada uma possui

uma funcionalidade específica.

No código de antes, vimos por exemplo o uso da tag  <h1> . Ela representa o título principal da

página.

 <h1>MusicDot</h1>

Note a sintaxe. Uma tag é definida com caracteres * < * e * > *, e seu nome (**h1** no caso). Muitas tags

possuem conteúdo, como o texto do título (*"MusicDot"*). Nesse caso, para determinar onde o conteúdo
acaba, usamos uma *tag de fechamento* com a barra antes do nome:  </h1> .

Algumas tags podem receber algum tipo de informação extra dentro de sua definição chamada de
**atributo**. São parâmetros usando a sintaxe de  atributo="valor" . Para definir uma imagem, por

exemplo, usamos a tag  <img>  e, para indicar o caminho que está essa imagem, usamos o atributo

**Agora é a melhor hora de aprender algo novo**

## 3.2 SINTAXE DO HTML

**12** 
3.2 SINTAXE DO HTML


--------------------------------------------------

src :

 <img src="../imagens/casa_de_praia.jpg">

Repare que a tag  img não possui conteúdo por si só, e sim ela carrega ali o conteúdo de um arquivo

externo (a imagem). Nesses casos, **não** é necessário usar uma tag de fechamento como antes no  h1 .

O HTML é composto de diversas tags, cada uma com sua função e significado. Desde 2013, com a
atualização da linguagem para o HTML 5, muitas novas tags foram adicionadas, que veremos ao longo

do curso.

Nesse momento, vamos focar em tags que representam **títulos**, **parágrafo** e **ênfase**.

Quando queremos indicar que um texto é um título em nossa página, utilizamos as tags de ***heading***
em sua marcação:

<h1>MusicDot</h1>
<h2>Bem-vindo à MusicDot, seu portal de cursos de música online.</h2>

As tags de *heading* são para exibir conteúdo de texto e contém 6 níveis, ou seja de  <h1> à  <h6> ,

seguindo uma ordem de importância, sendo  <h1> o título principal, o mais importante, e  <h6> o título

de menor importância.

Utilizamos, por exemplo, a tag  <h1> para o nome, título principal da página, e a tag  <h2>  como

subtítulo ou como título de seções dentro do documento.

*Obs: a tag ** <h1> **só pode ser utilizada uma vez em cada página porque não pode existir mais de um*

*conteúdo mais importante da página.*

A ordem de importância tem impacto nas ferramentas que processam HTML. As ferramentas de

indexação de conteúdo para buscas, como o Google, Bing ou Yahoo! levam em consideração essa ordem
e relevância. Os navegadores especiais para acessibilidade também interpretam o conteúdo dessas tags
de maneira a diferenciar seu conteúdo e facilitar a navegação do usuário pelo documento.

Quando exibimos qualquer texto em nossa página, é recomendado que ele seja sempre conteúdo de
alguma tag filha da tag  <body> . A marcação mais indicada para textos comuns é a tag de **parágrafo**:

<p>

 A MusicDot é a maior escola online de música em todo o mundo.
</p>

## 3.3 TAGS HTML

**### Títulos**

**### Parágrafos**

3.3 TAGS HTML 
**13**


--------------------------------------------------

Se você tiver vários parágrafos de texto, use várias dessas tags  <p> para separá-los:

<p>

 A MusicDot é a maior escola online de música em todo o mundo.
</p>
<p>

 Nossa matriz fica em Mafra, em Santa Catarina. De lá, saem  grande parte das gravações de nossos cu
rsos.
</p>

Quando queremos dar uma ênfase diferente a um trecho de texto, podemos utilizar as marcações de
ênfase. Podemos deixar um texto "mais forte" com a tag  <strong> ou deixar o texto com uma "ênfase

acentuada" com a tag  <em> . Do mesmo jeito que a tag  <strong>  deixa a tag "mais forte", temos

também a tag  <small> , que diminui o "peso" do texto.

Por padrão, os navegadores exibem o texto dentro da tag  <strong> em negrito e o texto dentro da

tag  <em> em itálico. Existem ainda as tags  <b> e  <i> , que atingem o mesmo resultado visualmente,

mas as tags  <strong>  e  <em>  são mais indicadas por definirem nossa intenção de significado ao

conteúdo, mais do que uma simples indicação visual. Vamos discutir melhor a questão do significado
das tags mais adiante.

<p>Aprenda de um jeito rápido e barato na <strong>MusicDot</strong>.</p>

A tag  <img>  indica para o navegador que uma imagem deve ser "renderizada"

(mostrada/desenhada) naquele lugar e necessita dois atributos preenchidos:  src  e  alt . O primeiro é

um atributo obrigatório para exibir a imagem e aponta para a sua localização (pode ser um local do seu
computador ou um endereço na Web), já o segundo é um texto alternativo que aparece caso a imagem

não possa ser carregada ou visualizada.

O atributo  alt não é obrigatório, porém é considerado um erro caso seja omitido, pois ele provê o

entendimento da imagem para pessoas com deficiência que necessitam o uso de leitores de tela para
acessar o computador, e também auxilia na indexação da imagem para motores de busca, como o
Google etc.

O HTML 5 introduziu duas novas tags específicas para imagem:  <figure>  e  <figcaption> . A

tag  <figure> define uma imagem em conjunto com a tag  <img> . Além disso, permite adicionar uma

legenda para a imagem por meio da tag  <figcaption> .

<figure>

 <img src="img/matriz-musicdot.png" alt="Foto da matriz da musicdot">
 <figcaption>Matriz da MusicDot</figcaption>
</figure>

**### Marcações de ênfase**

## 3.4 IMAGENS

**14** 
3.4 IMAGENS


--------------------------------------------------

Editoras tradicionais pouco ligam para ebooks e novas tecnologias. Não dominam

tecnicamente o assunto para revisar os livros a fundo. Não têm anos de

experiência em didáticas com cursos.

Conheça a **Casa do Código**, uma editora diferente, com curadoria da **Caelum** e

obsessão por livros de qualidade a preços justos.

Casa do Código, ebook com preço de ebook.

A primeira página que desenvolveremos para a *MusicDot* será a *Sobre*, que explica detalhes sobre a

empresa, apresenta fotos e a história.

Recebemos o design já pronto, assim como os textos. Nosso trabalho, como pessoas

desenvolvedoras de front-end, é codificar o HTML e CSS necessários para esse resultado.

**B****OA**** ****PRÁTICA**** - I****NDENTAÇÃO**

Uma prática sempre recomendada, ligada à limpeza e utilizada para facilitar a leitura do código,
é o uso correto de **recuos**, ou **indentação**, no HTML. Costumamos alinhar elementos "irmãos" na

mesma margem e adicionar alguns espaços ou um *tab* para elementos "filhos".

A maioria dos exercícios dessa apostila utiliza um padrão recomendado de recuos.

**B****OA**** ****PRÁTICA**** - C****OMENTÁRIOS**

Quando iniciamos nosso projeto, utilizamos poucas tags HTML. Mais tarde adicionaremos uma
quantidade razoável de elementos, o que pode gerar uma certa confusão. Para manter o código mais

legível, é recomendada a adição de comentários antes da abertura e após do fechamento de tags
estruturais (que conterão outras tags). Dessa maneira, nós podemos identificar claramente quando

um elemento está **dentro** dessa estrutura ou **depois** dela.

**Editora Casa do Código com livros de uma forma diferente**

## 3.5 PRIMEIRA PÁGINA

3.5 PRIMEIRA PÁGINA 
**15**


--------------------------------------------------

 <!-- início do cabeçalho -->
 <header>
   <p>Esse parágrafo está <strong>dentro</strong> do cabeçalho.</p>
 </header>
 <!-- fim do cabeçalho -->

 <p>Esse parágrafo está <strong>depois</strong> do cabeçalho.</p>

**16** 
3.5 PRIMEIRA PÁGINA


--------------------------------------------------

CAPÍTULO 4

Começaremos a fazer nossa primeira página do projeto. Escreveremos o conteúdo e marcaremos ele

com as *tags* do *HTML* para que nossa página tenha cada conteúdo diferenciado pela sua natureza. Nesse
começo, o resultado será que cada conteúdo marcado terá um visual diferente por padrão, por exemplo,
títulos aparecerão com um tamanho maior que o dos textos comuns.

Os conteúdos que aparecerão na página por enquanto serão:

A logo da MusicDot
O título principal da página: "Sobre a empresa"

Os textos sobre a empresa, em parágrafos

O subtítulo: "História"

Os textos sobre a história, em parágrafos
As figuras da empresa e da família. Lembrando que chamamos de figura o conjunto de uma foto e
uma legenda.

Todo o conteúdo de texto das páginas já está pronto na pasta **"textos"**. Essa pasta foi disponibilizada
juntamente com os arquivos do curso.

O resultado ao final do exercício será o seguinte:

# EXERCÍCIO: PRIMEIROS PASSOS COM
# HTML

## 4.1 OBJETIVO

4 EXERCÍCIO: PRIMEIROS PASSOS COM HTML 
**17**


--------------------------------------------------

Figura 4.1: Visual da página ao final do exercício

A **Alura** oferece centenas de **cursos online** em sua plataforma exclusiva de
ensino que favorece o aprendizado com a **qualidade** reconhecida da Caelum.

Você pode escolher um curso nas áreas de Programação, Front-end, Mobile,
Design & UX, Infra, Business, entre outras, com um plano que dá acesso a todos os cursos. Ex-

estudante da Caelum tem 10% de desconto neste link!

Conheça os cursos online Alura.

1. Crie o arquivo ** sobre.html **na pasta ** raíz do projeto **com o seguinte código:

**Já conhece os cursos online Alura?**

## 4.2 PASSO A PASSO COM CÓDIGO

**18** 
4.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

+<img src="img/logo.svg" alt="MusicDot">
+
+<h1> Sobre a empresa </h1>
+
+<p>
+  A MusicDot é a maior escola online de música em todo o mundo.
+  Fundada em 1932, possui estúdios em 124 países, sendo líder de mercado com mais de 90% de
+  participação em 118 deles.
+</p>
+
+<p>
+  Nossa matriz fica em Mafra, em Santa Catarina. De lá, saem grande parte das gravações de nosso
s cursos. Nossa matriz:

+</p>
+
+<figure>
+  <img src="img/matriz-musicdot.png" alt="Matriz da musicdot">
+  <figcaption> 
+      Matriz MusicDot 
+  </figcaption>
+</figure>
+
+<p>
+  Assine os cursos da MusicDot. Acesse nosso site ou entre em contato
+  se tiver dúvidas. Conheça também nossa história e nossos diferenciais.
+</p>
+
+<h2> História </h2>
+
+<figure>
+  <img src="img/familia-tupfeln.jpg" alt="Foto da família tüpfeln">
+  <figcaption>Família Tüpfeln</figcaption>
+</figure>
+
+<p>
+  A fundação em 1932 ocorreu no momento da descoberta econônica de cursos por stream online no i
nterior de Santa Catarina. A

+  família Tüpfeln, tradicional da região, investiu todas as suas economias nessa nova iniciativa
,

+  revolucionária para a época. A fundadora frau Dagmar Olaf Tüpfeln, dotada de particular visão
+  administrativa, guiou os negócios da empresa durante mais de 50 anos, muitos deles ao lado
+  de seu filho Ernst Noten Tüpfeln, atual CEO. O nome da empresa é inspirado no nome da família.
+</p>
+
+<p>
+  O crescimento da empresa foi praticamente instantâneo. Nos primeiros 5 anos, já atendia 18 paí
ses.

+  Bateu a marca de 100 países em apenas 15 anos de existência. Até hoje, já atendeu 2 bilhões
+  de usuários diferentes, em bilhões de diferentes pedidos.
+</p>
+
+<p>
+  O crescimento em número de funcionários é também assombroso. Hoje, é a maior empregadora do
+  Brasil, mas mesmo após apenas 5 anos de sua existência, já possuía 30 mil funcionários. Fora d
o

+  Brasil, há 240 mil funcionários, além dos 890 mil brasileiros nas instalações de Mafra e
+  nos escritórios em todo país.
+</p>
+
+<p>

**# sobre.html**

4.2 PASSO A PASSO COM CÓDIGO 
**19**


--------------------------------------------------

+  Dada a importância econômica da empresa para o Brasil, a família Tüpfeln já recebeu diversos p
rêmios,

+  homenagens e condecorações. Todos os presidentes do Brasil já visitaram as instalações da Musi
cDot, além de presidentes da União Européia, Ásia e o secretário-geral da ONU.

+</p>

**20** 
4.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

CAPÍTULO 5

Um documento HTML válido precisa seguir obrigatoriamente a estrutura composta pelas tags  <html> ,

<head>  e  <body>  e a instrução  <!DOCTYPE> . Esta estrutura está informada em uma documentação

que descreve todos os detalhes do HTML, no caso as tags e atributos, e como os navegadores devem
considerar e interpretar estas tags, esta documentação é chamada de "especificação do HTML", e através

do que está declarado nela que é possível entender se um documento HTML válido. Um documento
HTML inválido é carregado pelo navegador, porém em um "*modo de compatibilidade*", vamos entender

melhor sobre isto logo mais.

Abaixo, vamos conhecer em detalhes cada uma das tags estruturais obrigatórias:

Na estrutura do nosso documento, antes de começar a colocar o conteúdo, inserimos uma tag

<html> . Dentro dessa tag, é necessário declarar outras duas tags:  <head> e  <body> . Essas duas tags

são "irmãs", pois estão no mesmo nível hierárquico em relação à sua tag "mãe", que é  <html> .

 <html> <!-- mãe -->
   <head></head> <!-- filha -->
   <body></body> <!-- filha -->
 </html>

Querendo aprender ainda mais sobre? Esclarecer dúvidas dos exercícios? Ouvir
explicações detalhadas com um instrutor?
A Caelum oferece o **curso data** presencial nas cidades de São Paulo, Rio de

Janeiro e Brasília, além de turmas incompany.

Consulte as vantagens do curso *Desenvolvimento Web com HTML, CSS e*
*JavaScript*

# ESTRUTURA DE UM DOCUMENTO HTML

## 5.1 A TAG <HTML>

**Você pode também fazer o curso data dessa apostila na Caelum**

5 ESTRUTURA DE UM DOCUMENTO HTML 
**21**


--------------------------------------------------

A tag  <head>  contém informações sobre o documento HTML que são de interesse somente do

navegador e para outros serviços da web, e não para as pessoas que vão acessar nosso site. São
informações que não serão exibidas diretamente no navegador, também podemos considerar um local

onde informamos os metadados sobre a página.

A especificação do HTML obriga a presença da tag de conteúdo  <title>  dentro da  <head> ,

permitindo definir o título do documento, que poder ser visto na *barra de título* ou *aba* da janela do
navegador. Caso contrário, a página não será um documento HTML válido.

Outra configuração muito importante, principalmente em documentos HTML cujo conteúdo é
escrito em um idioma como o português, que contém caracteres "especiais" (acentos e cedilha), é a

codificação/conjunto de caracteres, chamada de **encoding** ou **charset**.

Podemos configurar qual codificação queremos utilizar em nosso documento por meio da
configuração de  charset na tag  <meta> . Um dos valores mais comuns usados hoje em dia é o **UTF-**

**8**, também chamado de **Unicode**. Há outras possibilidades, como o **latin1**, muito usado antigamente.

O **UTF-8** é a recomendação atual para encoding na Web por ser amplamente suportada em
navegadores e editores de código, além de ser compatível com praticamente todos os idiomas do mundo.
É o que usaremos no curso.

<html>

   <head>
     <meta charset="utf-8">
     <title>MusicDot</title>
   </head>
   <body>

   </body>
</html>

A tag  <body>  contém o corpo de um documento HTML, que é exibido pelo navegador em sua

janela, ou seja, todo o conteúdo visível do site. É necessário que o  <body>  tenha ao menos um

elemento "filho", ou seja, uma ou mais tags HTML dentro dele.

<html>

 <head>
   <meta charset="utf-8">
   <title>MusicDot</title>
 </head>
 <body>
   <h1>A MusicDot</h1>
 </body>
</html>

## 5.2 A TAG <HEAD>

## 5.3 A TAG <BODY>

**22** 
5.2 A TAG


--------------------------------------------------

Nesse exemplo, usamos a tag  <h1> , que indica o título principal da página.

O  DOCTYPE  não é uma tag HTML, mas uma instrução especial. Ela indica para o navegador qual

**versão do HTML** deve ser utilizada para exibir a página. Quando não colocamos essa instrução a
página é exibida numa espécie de "*modo de compatibilidade*" na qual algumas tags e estilizações não
funcionam 100% corretamente. Principalmente as tags e estilizações mais atuais (lançadas na versão 5

do HTML). Inclusive é possível ver a diferença na folha de estilos padrão que o navegador usa quando
não colocamos essa instrução.

A imagem da esquerda é a página **sem**  Doctype e a imagem da direita é a página **com**  Doctype .

Dá para ver que existe uma leve diferença entre as duas páginas, principalmente com relação aos
espaçamentos.

Utilizaremos  <!DOCTYPE html> , que indica para o navegador a utilização da versão mais recente

do HTML - a versão 5, atualmente*.

Há muitas possibilidades mais complicadas nessa parte de  DOCTYPE  que eram usados em versões

anteriores do HTML e do XHTML. Hoje em dia, nada disso é mais importante. O recomendado é
**sempre usar a última versão do HTML**, usando a declaração de  DOCTYPE simples:

 *<!DOCTYPE html>*

A declaração do DOCTYPE, pode ser escrita toda em maiúsculo ou toda em minúsculo ou com a

primeira letra maiúscula:  <!DOCTYPE HTML> ,  <!DOCTYPE html> ,  <!Doctype HTML> ,  <!Doctype

html> ,  <!doctype html> ,  <!doctype HTML> . O resultado será o mesmo para todos os casos.

## 5.4 A INSTRUÇÃO DOCTYPE

5.4 A INSTRUÇÃO DOCTYPE 
**23**


--------------------------------------------------

**Obs: desde maio de 2019 o desenvolvimento do HTML é mantido pelo W3C (World Wide Web*
*Consortium) **https://www.w3.org/**, WHATWG e comunidade de desenvolvedores, e sua especificação é*
*aberta no Github **https://github.com/whatwg/html**, e desde este movimento o HTML é considerado um*

*"padrão vivo" (living standard) onde sua versão a partir da 5 é atualizada continuamente*.

Conheça a **Casa do Código**, uma **nova** editora, com autores de destaque no

mercado, foco em **ebooks** (PDF, epub, mobi), preços **imbatíveis** e assuntos
**atuais**.
Com a curadoria da **Caelum** e excelentes autores, é uma abordagem **diferente**

para livros de tecnologia no Brasil.

Casa do Código, Livros de Tecnologia.

**Seus livros de tecnologia parecem do século passado?**

**24** 
5.4 A INSTRUÇÃO DOCTYPE


--------------------------------------------------

CAPÍTULO 6

Nesse momento a aba do navegador está exibindo o caminho e o nome do arquivo "sobre.html"

Figura 6.1: Aba do Firefox com a página "sobre" aberta

Nesse exercício mudaremos algumas informações da nossa página. A diferença é que essas

informações serão apenas para o navegador e não devem ser exibidas como conteúdo da página.

As informações que passaremos para o navegador são:

O texto que aparecerá na aba do navegador: **"MusicDot | Sobre a empresa"**

O ícone que aparecerá na aba do navegador: **"img/favicon.ico"**
Qual o "charset" que será usado para o conteúdo da aba e da página: **"utf-8"**

Qual o idioma principal da página: **"pt-BR"**

Qual a versão do HTML está sendo usada: **"a mais atual suportada pelo navegador"**

Ao final do exercício deve ser possível escrever e ler caractéres acentuados no conteúdo da página.

Ao final, também, a aba do navegador deve apresentar o texto e o ícone:

Figura 6.2: Aba do Firefox com a página "sobre" aberta

# EXERCÍCIO: A ESPECIFICAÇÃO HTML

## 6.1 OBJETIVO

6 EXERCÍCIO: A ESPECIFICAÇÃO HTML 
**25**


--------------------------------------------------

Se você está gostando dessa apostila, certamente vai aproveitar os **cursos**

**online** que lançamos na plataforma **Alura**. Você estuda a qualquer momento
com a **qualidade** Caelum. Programação, Mobile, Design, Infra, Front-End e
Business, entre outros! Ex-estudante da Caelum tem 10% de desconto, siga o link!

Conheça a Alura Cursos Online.

1. No arquivo ** sobre.html **na pasta ** raíz do projeto **faça as seguintes alterações:

-<̶i̶m̶g̶ s̶r̶c̶=̶"̶i̶m̶g̶/̶l̶o̶g̶o̶.̶s̶v̶g̶"̶ a̶l̶t̶=̶"̶M̶u̶s̶i̶c̶D̶o̶t̶"̶>
+*<!doctype html>*
+<html lang="pt-BR">
+  <head>
+    <meta charset="utf-8">
+    <title>
+      MusicDot | Sobre a empresa
+    </title>
+    <link href="img/favicon.ico" rel="icon">
+  </head>

-<̶h̶1̶>̶ S̶o̶b̶r̶e̶ a̶ e̶m̶p̶r̶e̶s̶a̶ </̶h̶1̶>
+  <body>

-<̶p̶>
+    <img src="img/logo.svg" alt="MusicDot">
+    
+    <h1> Sobre a empresa </h1>
+    
+    <p>
       A MusicDot é a maior escola online de música em todo o mundo.
       Fundada em 1932, possui estúdios em 124 países, sendo líder de mercado com mais de 90% de
       participação em 118 deles.
-</̶p̶>
+    </p>

-<̶p̶>
+    <p>
       Nossa matriz fica em Mafra, em Santa Catarina. De lá, saem grande parte das gravações de n
ossos cursos. Nossa matriz:

-</̶p̶>
+    </p>

-<̶f̶i̶g̶u̶r̶e̶>
+    <figure>

**Agora é a melhor hora de aprender algo novo**

## 6.2 PASSO A PASSO COM CÓDIGO

**# sobre.html**

**26** 
6.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

       <img src="img/matriz-musicdot.png" alt="Matriz da musicdot">
       <figcaption> 
           Matriz MusicDot 
       </figcaption>
-</̶f̶i̶g̶u̶r̶e̶>
+    </figure>

-<̶p̶>
+    <p>
       Assine os cursos da MusicDot. Acesse nosso site ou entre em contato
       se tiver dúvidas. Conheça também nossa história e nossos diferenciais.
-</̶p̶>
+    </p>

-<̶h̶2̶>̶ H̶i̶s̶t̶ó̶r̶i̶a̶ </̶h̶2̶>
+    <h2> História </h2>

-<̶f̶i̶g̶u̶r̶e̶>
+    <figure>
       <img src="img/familia-tupfeln.jpg" alt="Foto da família tüpfeln">
       <figcaption>Família Tüpfeln</figcaption>
-</̶f̶i̶g̶u̶r̶e̶>
+    </figure>

-<̶p̶>
+    <p>
       A fundação em 1932 ocorreu no momento da descoberta econônica de cursos por stream online 
no interior de Santa Catarina. A

       família Tüpfeln, tradicional da região, investiu todas as suas economias nessa nova inicia
tiva,

       revolucionária para a época. A fundadora frau Dagmar Olaf Tüpfeln, dotada de particular vi
são

       administrativa, guiou os negócios da empresa durante mais de 50 anos, muitos deles ao lado
       de seu filho Ernst Noten Tüpfeln, atual CEO. O nome da empresa é inspirado no nome da famí
lia.

-</̶p̶>
+    </p>

-<̶p̶>
+    <p>
       O crescimento da empresa foi praticamente instantâneo. Nos primeiros 5 anos, já atendia 18
países.
       Bateu a marca de 100 países em apenas 15 anos de existência. Até hoje, já atendeu 2 bilhõe
s

       de usuários diferentes, em bilhões de diferentes pedidos.
-</̶p̶>
+    </p>

-<̶p̶>
+    <p>
       O crescimento em número de funcionários é também assombroso. Hoje, é a maior empregadora d
o

       Brasil, mas mesmo após apenas 5 anos de sua existência, já possuía 30 mil funcionários. Fo
ra do

       Brasil, há 240 mil funcionários, além dos 890 mil brasileiros nas instalações de Mafra e
       nos escritórios em todo país.
-</̶p̶>
+    </p>

-<̶p̶>
+    <p>
       Dada a importância econômica da empresa para o Brasil, a família Tüpfeln já recebeu divers
os prêmios,

6.2 PASSO A PASSO COM CÓDIGO 
**27**


--------------------------------------------------

       homenagens e condecorações. Todos os presidentes do Brasil já visitaram as instalações da 
MusicDot, além de presidentes da União Européia, Ásia e o secretário-geral da ONU.

-</̶p̶>
+    </p>
+  
+  </body>
+</html>

**28** 
6.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

CAPÍTULO 7

Quando escrevemos o HTML, marcamos o conteúdo da página com tags que melhor representam o

significado daquele conteúdo. Quando abrimos a página no navegador é possível perceber que ele
mostra as informações com estilos diferentes.

Um h1, por exemplo, por padrão é apresentado em negrito numa fonte maior. Parágrafos de texto
são espaçados entre si, e assim por diante. Isso quer dizer que o navegador tem um *estilo padrão* para as
tags que usamos. Porém para fazer sites bonitos, ou com o visual próximo de uma dada identidade

visual (design), vamos precisar *personalizar a apresentação padrão dos elementos* da página.

Antigamente, isso era feito no próprio HTML. Caso houvesse a necessidade de um título ser
vermelho, era só fazer:

<h1><font color="red">MusicDot anos 90</font></h1>

Além da tag  <font> , várias outras tags de estilo existiam. Mas isso é passado. Hoje em dia **tags**

**HTML para estilo são má prática** e jamais devem ser usadas, são interpretadas apenas para o modo de
compatibilidade.

Em seu lugar, surgiu o **CSS** (*Cascading Style Sheet* ou folha de estilos em cascata), que é uma outra
linguagem, separada do HTML, com objetivo único de cuidar da estilização da página. A vantagem é

que o CSS é bem mais robusto que o HTML para estilização, como veremos. Mas, principalmente,
escrever formatação visual misturado com conteúdo de texto no HTML se mostrou algo impraticável. O
CSS resolve isso separando as coisas; regras de estilo não aparecem mais no HTML, apenas no CSS.

A sintaxe do CSS tem estrutura simples: é uma declaração de propriedades e valores separados por
um sinal de dois pontos ":", e cada propriedade é separada por um sinal de ponto e vírgula ";" da
seguinte maneira:

color: blue;
background-color: yellow;

O elemento que receber essas propriedades será exibido com o texto na cor azul e com o fundo
amarelo. Essas propriedades podem ser declaradas de três maneiras diferentes.

# ESTILIZANDO COM CSS

## 7.1 SINTAXE E INCLUSÃO DE CSS

7 ESTILIZANDO COM CSS 
**29**


--------------------------------------------------

A primeira delas é com o atributo  style no próprio elemento:

<p style="color: blue; background-color: yellow;">
O conteúdo desta tag será exibido em azul com fundo amarelo no navegador!
</p>

Mas tínhamos acabado de discutir que uma das grandes vantagens do CSS era manter as regras de
estilo fora do HTML. Usando esse atributo  style  não parece que fizemos isso. Justamente por isso

não se recomenda esse tipo de uso na prática, mas sim os que veremos a seguir.

A outra maneira de se utilizar o CSS é declarando suas propriedades dentro de uma tag  <style> .

Como estamos declarando as propriedades visuais de um elemento em outro lugar do nosso

documento, precisamos indicar de alguma maneira a qual elemento nos referimos. Fazemos isso
utilizando um **seletor CSS**. É basicamente uma forma de buscar certos elementos dentro da página que
receberão as regras visuais que queremos.

No exemplo a seguir, usaremos o seletor que pega todas as tags  p e altera sua cor e background:

*<!DOCTYPE html>*
<html>

 <head>
   <meta charset="utf-8">
   <title>Sobre a MusicDot</title>
   <style>
     p {
       color: blue;
       background-color: yellow;
     }
   </style>
 </head>
 <body>
   <p>
     O conteúdo desta tag será exibido em azul com fundo amarelo!
   </p>
   <p>
     <strong>Também</strong> será exibido em azul com fundo amarelo!
   </p>
 </body>
</html>

O código dentro da tag  <style>  indica que estamos alterando a cor e o fundo de todos os

elementos com tag  p . Dizemos que selecionamos esses elementos pelo nome de sua tag, e aplicamos

certas propriedades CSS apenas neles.

Revisando então a estrutura de uso do CSS:

seletor {

   propriedade: valor;

**### Atributo style**

**### A tag style**

**30** 
7.1 SINTAXE E INCLUSÃO DE CSS


--------------------------------------------------

}

Algumas propriedades contém "subpropriedades" que modificam uma parte específica daquela

propriedade que vamos trabalhar, sendo sua sintaxe:

seletor {

   propriedade-subpropriedade: valor;
}

No exemplo abaixo, em ambos os casos, trabalhamos com a propriedade  text , que estiliza a

aparência do texto do seletor informado. Podemos especificar quais propriedades específicas do texto
queremos modificar, no caso  text-align  o alinhamento do texto, e com  text-decoration 

colocamos o efeito de sublinhado.

p {

   text-align: center;
   text-decoration: underline;
}

A terceira maneira de declararmos os estilos do nosso documento é com um arquivo externo com a
extensão  .css . Para que seja possível declarar nosso CSS em um arquivo à parte, precisamos indicar

em nosso documento HTML uma ligação entre ele e a folha de estilo (arquivo com a extensão  .css ).

Além da melhor organização do projeto, a folha de estilo externa traz ainda as vantagens de manter
nosso HTML mais limpo e do reaproveitamento de uma mesma folha de estilos para diversos

documentos.

A indicação de uso de uma folha de estilos externa deve ser feita dentro da tag  <head>  de um

documento HTML:

*<!DOCTYPE html>*
<html>

 <head>
   <meta charset="utf-8">
   <title>MusicDot | Sobre a empresa</title>
   <!-- Inclusão do arquivo CSS -->
   <link rel="stylesheet" href="estilos.css">
 </head>
 <body>
   <p>
     O conteúdo desta tag será exibido em azul com fundo amarelo!
   </p>
   <p>
     <strong>Também</strong> será exibido em azul com fundo amarelo!
   </p>
 </body>
</html>

E dentro do arquivo  estilos.css colocamos apenas o conteúdo do CSS:

p {

**### Arquivo externo**

7.1 SINTAXE E INCLUSÃO DE CSS 
**31**


--------------------------------------------------

 color: blue;
 background-color: yellow;
}

Editoras tradicionais pouco ligam para ebooks e novas tecnologias. Não dominam
tecnicamente o assunto para revisar os livros a fundo. Não têm anos de
experiência em didáticas com cursos.
Conheça a **Casa do Código**, uma editora diferente, com curadoria da **Caelum** e
obsessão por livros de qualidade a preços justos.

Casa do Código, ebook com preço de ebook.

Da mesma maneira que alteramos cores, podemos alterar o texto. Podemos definir fontes com o uso

da propriedade  font-family .

A propriedade  font-family  pode receber seu valor com ou sem aspas dependendo da sua

composição, por exemplo, quando uma fonte tem o nome separado por *espaço*.

Por padrão, os navegadores mais conhecidos exibem texto em um tipo que conhecemos como
"serif". As fontes mais conhecidas (e comumente utilizadas como padrão) são "Times" e "Times New

Roman", dependendo do sistema operacional. Elas são chamadas de **fontes serifadas** pelos pequenos
ornamentos em suas terminações.

Podemos alterar a família de fontes que queremos utilizar em nosso documento para a família "sans-
serif" (sem serifas), que contém, por exemplo, as fontes "Arial" e "Helvetica". Podemos também

declarar que queremos utilizar uma família de fontes "monospace" como, por exemplo, a fonte
"Courier".

*Obs: Fontes monospace podem ser tanto com serifa ou sem serifa. Monospace quer dizer apenas*

*que todas as letras possuem o mesmo tamanho*

h1 {

 font-family: serif;
}

h2 {

 font-family: sans-serif;
}

**Editora Casa do Código com livros de uma forma diferente**

## 7.2 PROPRIEDADES TIPOGRÁFICAS E FONTES

**32** 
7.2 PROPRIEDADES TIPOGRÁFICAS E FONTES


--------------------------------------------------

p {

 font-family: monospace;
}

É possível, e muito comum, declararmos o nome de algumas fontes que gostaríamos de verificar se
existem no computador, permitindo que tenhamos um controle melhor da forma como nosso texto será
exibido.

Em nosso projeto, as fontes não têm ornamentos, vamos declarar essa propriedade para todo o

documento por meio do seu elemento  body :

body {

 font-family: "Helvetica", "Lucida Grande", sans-serif;
}

Nesse caso, o navegador verificará se a fonte "Helvetica" está disponível e a utilizará para exibir os
textos de todos os elementos do nosso documento que, por cascata, herdarão essa propriedade do

elemento  body .

Caso a fonte "Helvetica" não esteja disponível, o navegador verificará a disponibilidade da próxima

fonte declarada, no nosso exemplo a "Lucida Grande". Caso o navegador não encontre também essa
fonte, ele solicita qualquer fonte que pertença à família "sans-serif", declarada logo a seguir, e a utiliza
para exibir o texto, não importa qual seja ela.

Temos outras propriedades para manipular a fonte, como a propriedade  font-style , que define o

estilo da fonte que pode ser:  normal (normal na vertical),  italic (inclinada) e  oblique (oblíqua).

Já vimos uma série de propriedades e subpropriedades que determinam o tipo e estilo da fonte.
Vamos conhecer algumas maneiras de alterarmos as disposições dos textos.

No exemplo a seguir vamos mudar o alinhamento do texto com a propriedade  text-align .

p {

 text-align: right;
}

O exemplo determina que todos os parágrafos da nossa página tenham o texto alinhado para a
direita. Também é possível determinar que um elemento tenha seu conteúdo alinhado ao centro ao
definirmos o valor  center para a propriedade  text-align , ou então definir que o texto deve ocupar

toda a largura do elemento aumentando o espaçamento entre as palavras com o valor  justify . Por

padrão o texto é alinhado à esquerda, com o valor  left , porém é importante lembrar que essa

propriedade propaga-se em cascata.

É possível configurar também uma série de espaçamentos de texto com o CSS:

## 7.3 ALINHAMENTO E DECORAÇÃO DE TEXTO

7.3 ALINHAMENTO E DECORAÇÃO DE TEXTO 
**33**


--------------------------------------------------

p {

 line-height: 3px; /* tamanho da altura de cada linha */
 letter-spacing: 3px; /* tamanho do espaço entre cada letra */
 word-spacing: 5px; /* tamanho do espaço entre cada palavra */
 text-indent: 30px; /* tamanho da margem da primeira linha do texto */
}

A propriedade  background-image  permite indicar um arquivo de imagem para ser exibido ao

fundo do elemento. Por exemplo:

h1 {

 background-image: url(sobre-background.jpg);
}

Com essa declaração, o navegador vai requisitar um arquivo  sobre-background.jpg , que deve

estar na mesma pasta do arquivo CSS onde consta essa declaração. Mas podemos também passar um
endereço da web para pegar imagens remotamente:

body {

 background-image: url(https://i.imgur.com/uAhjMNd.jpg);
}

A **Alura** oferece centenas de **cursos online** em sua plataforma exclusiva de
ensino que favorece o aprendizado com a **qualidade** reconhecida da Caelum.

Você pode escolher um curso nas áreas de Programação, Front-end, Mobile,
Design & UX, Infra, Business, entre outras, com um plano que dá acesso a todos os cursos. Ex-

estudante da Caelum tem 10% de desconto neste link!

Conheça os cursos online Alura.

As propriedades do CSS para definirmos as **bordas** de um elemento nos apresentam uma série de
opções. Podemos, para cada borda de um elemento, determinar sua cor, seu estilo de exibição e sua

largura. Por exemplo:

body {

 border-color: red;
 border-style: solid;
 border-width: 1px;
}

## 7.4 IMAGEM DE FUNDO

**Já conhece os cursos online Alura?**

## 7.5 BORDAS

**34** 
7.4 IMAGEM DE FUNDO


--------------------------------------------------

A propriedade  border tem uma forma resumida para escrever os mesmos estilos que adicionamos

acima, mas de uma maneira mais simples:

body {

 border: 1px solid red;
}

Para que o efeito da cor sobre a borda surta efeito, é necessário que a propriedade  border-style 

tenha qualquer valor diferente do padrão  none .

Podemos também falar em qual dos lados do nosso elemento queremos a borda usando a
subpropriedade que indica lado:

h1 {

 border-top: 1px solid red; /* borda vermelha em cima */
 border-right: 1px solid red; /* borda vermelha à direita */
 border-bottom: 1px solid red; /* borda vermelha embaixo */
 border-left: 1px solid red; /* borda vermelha à esquerda */
}

Conseguimos fazer também comentários no CSS usando a seguinte sintaxe:

    /* deixando o fundo amarelo ouro */
    body {
        background-color: gold;
    }

Propriedades como  background-color ,  color ,  border-color , entre outras aceitam uma cor

como valor. Existem várias maneiras de definir cores quando utilizamos o CSS.

A primeira, mais simples, é usando o nome da cor:

h1 {

   color: red;
}

h2 {

   background-color: yellow;
}

O difícil é acertar a exata variação de cor que queremos no design e também cada navegador tem o
seu padrão de cor para os nomes de cores. A W3C obriga que todos os navegadores tenham pelo menos

140 nomes de cores padronizados, mas existem mais de 16 milhões de cores na web e seria
extremamente complicado nomear cada uma delas. Por isso, é bem incomum usarmos cores com seus

nomes. O mais comum é definir a cor com base em sua composição RGB.

RGB é o sistema de cor usado nos monitores, já que cada pixel nos monitores possuem 3 leds (um

## 7.6 CORES NA WEB

7.6 CORES NA WEB 
**35**


--------------------------------------------------

vermelho, um verde e um azul) e a combinação dessas 3 cores formam todas as outras 16 milhões de

cores que vemos nos monitores. Podemos escolher a intensidade de cada um desses três leds básicos,
numa escala de 0 a 255.

Um amarelo forte, por exemplo, tem 255 de Red, 255 de Green e 0 de Blue (255, 255, 0). Se quiser

um laranja, basta diminuir um pouco o verde (255, 200, 0). E assim por diante.

No CSS, podemos escrever as cores tendo como base sua composição RGB. Aliás, no CSS3 - que
veremos melhor depois - há até uma sintaxe bem simples pra isso:

h3 {

   color: rgb(255, 200, 0);
}

Essa sintaxe funciona nos browsers mais modernos e até alguns browsers super antigos mas não é a
mais comum na prática, por questões de compatibilidade. O mais comum é a **notação hexadecimal**.
Essa sintaxe tem suporte universal nos navegadores e é mais curta de escrever, apesar de ser mais

enigmática.

h3 {

   background-color: #f2eded;
}

No fundo, porém, as duas formas são baseadas no sistema RGB. Na notação hexadecimal (que

começa com **#**), temos 6 caracteres, os primeiros 2 indicam o canal Red, os dois seguintes, o Green, e os
dois últimos, Blue; ou seja, RGB. E usamos a matemática pra escrever menos, trocando a base numérica

de decimal para hexadecimal.

Na base hexadecimal, os algarismos vão de zero a quinze (ao invés do zero a nove da base decimal

comum). Para representar os algarismos de dez a quinze, usamos letras de A a F. Nessa sintaxe, portanto,
podemos utilizar números de 0-9 e letras de A-F.

Há uma conta por trás dessas conversões, mas seu editor de imagens deve ser capaz de fornecer

ambos os valores para você sem problemas. Um valor 255 vira FF na notação hexadecimal. A cor
**#f2eded**, por exemplo, é equivalente a **rgb(242, 237, 237)**, um cinza claro.

Vale aqui uma dica quanto ao uso de cores hexadecimais, toda vez que os caracteres presentes na
composição da base se repetirem, estes podem ser simplificados. Então um número em hexadecimal

**3366ff**, pode ser simplificado para **36f**.

*Obs: os 3 pares de números devem ser iguais entre si, ou seja, se tivermos um hexadecimal #33aabc*

*não podemos simplificar nada do código.*

**36** 
7.6 CORES NA WEB


--------------------------------------------------

CAPÍTULO 8

Começaremos a alterar o visual da nossa página para deixá-la mais agradável.

Primeiro precisamos criar nosso arquivo de estilo e importá-lo no nosso html. Dentro desse arquivo

utilizaremos os **seletores CSS** para escolher as tags/elementos que queremos estilizar e depois
aplicaremos as **propriedades do CSS**.

As mudanças de estilo serão:

Na página toda: trocar a família da fonte de toda a página

No título principal: alterar a cor da fonte para um cinza-escuro **"#3D3D3D"**
No título principal: colocar uma cor de fundo cinza-azulado **"#E1EDF2"**

Nos subtítulos: colocar uma borda na parte de baixo

Nas figuras: centralizar o conteúdo
Nas figuras: colocar uma cor de fundo chamada **"whitesmoke"**

Nas figuras: alterar a cor da fonte para um cinza-claro **"lightgrey"**

A página ficará assim:

# EXERCÍCIO: MUDANDO O VISUAL DA
# NOSSA PÁGINA

## 8.1 OBJETIVO

8 EXERCÍCIO: MUDANDO O VISUAL DA NOSSA PÁGINA 
**37**


--------------------------------------------------

Figura 8.1: Visual da página ao final do exercício

Querendo aprender ainda mais sobre? Esclarecer dúvidas dos exercícios? Ouvir
explicações detalhadas com um instrutor?
A Caelum oferece o **curso data** presencial nas cidades de São Paulo, Rio de
Janeiro e Brasília, além de turmas incompany.

Consulte as vantagens do curso *Desenvolvimento Web com HTML, CSS e*

*JavaScript*

1. Crie o arquivo ** sobre.css **na pasta ** css **com o seguinte código:

+body {
+  font-family: "Helvetica", "Lucida Grande", sans-serif;
+  color: #3D3D3D;
+}
+
+h1 {

**Você pode também fazer o curso data dessa apostila na Caelum**

## 8.2 PASSO A PASSO COM CÓDIGO

**# css/sobre.css**

**38** 
8.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

+  background-color: #E1EDF2;
+}
+
+h2 {
+  border-bottom: 2px solid black;
+}
+
+figure {
+  text-align: center;
+
+  background-color: whitesmoke;
+  border: 1px solid lightgrey;
+}

2. No arquivo ** sobre.html **na pasta ** raíz do projeto **faça as seguintes alterações:

 *<!doctype html>*
 <html lang="pt-BR">
   <head>
     <meta charset="utf-8">
     <title>
       MusicDot | Sobre a empresa
     </title>
     <link href="img/favicon.ico" rel="icon">
+    <link rel="stylesheet" href="css/sobre.css">
   </head>

   <body>

     <img src="img/logo.svg" alt="MusicDot">

     <h1> Sobre a empresa </h1>

     <p>
       A MusicDot é a maior escola online de música em todo o mundo.
       Fundada em 1932, possui estúdios em 124 países, sendo líder de mercado com mais de 90% de
       participação em 118 deles.
     </p>

     <p>
       Nossa matriz fica em Mafra, em Santa Catarina. De lá, saem grande parte das gravações de n
ossos cursos. Nossa matriz:

     </p>

     <figure>
       <img src="img/matriz-musicdot.png" alt="Matriz da musicdot">
       <figcaption> 
           Matriz MusicDot 
       </figcaption>
     </figure>

     <p>
       Assine os cursos da MusicDot. Acesse nosso site ou entre em contato
       se tiver dúvidas. Conheça também nossa história e nossos diferenciais.
     </p>

     <h2> História </h2>

     <figure>
       <img src="img/familia-tupfeln.jpg" alt="Foto da família tüpfeln">

**# sobre.html**

8.2 PASSO A PASSO COM CÓDIGO 
**39**


--------------------------------------------------

       <figcaption>Família Tüpfeln</figcaption>
     </figure>

     <p>
       A fundação em 1932 ocorreu no momento da descoberta econônica de cursos por stream online 
no interior de Santa Catarina. A

       família Tüpfeln, tradicional da região, investiu todas as suas economias nessa nova inicia
tiva,

       revolucionária para a época. A fundadora frau Dagmar Olaf Tüpfeln, dotada de particular vi
são

       administrativa, guiou os negócios da empresa durante mais de 50 anos, muitos deles ao lado
       de seu filho Ernst Noten Tüpfeln, atual CEO. O nome da empresa é inspirado no nome da famí
lia.

     </p>

     <p>
       O crescimento da empresa foi praticamente instantâneo. Nos primeiros 5 anos, já atendia 18
países.
       Bateu a marca de 100 países em apenas 15 anos de existência. Até hoje, já atendeu 2 bilhõe
s

       de usuários diferentes, em bilhões de diferentes pedidos.
     </p>

     <p>
       O crescimento em número de funcionários é também assombroso. Hoje, é a maior empregadora d
o

       Brasil, mas mesmo após apenas 5 anos de sua existência, já possuía 30 mil funcionários. Fo
ra do

       Brasil, há 240 mil funcionários, além dos 890 mil brasileiros nas instalações de Mafra e
       nos escritórios em todo país.
     </p>

     <p>
       Dada a importância econômica da empresa para o Brasil, a família Tüpfeln já recebeu divers
os prêmios,

       homenagens e condecorações. Todos os presidentes do Brasil já visitaram as instalações da 
MusicDot, além de presidentes da União Européia, Ásia e o secretário-geral da ONU.

     </p>

   </body>
 </html>

**40** 
8.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

CAPÍTULO 9

Temos algumas maneiras de trabalhar com dimensões e espaçamentos. Para espaçamento interno e

externo usamos respectivamente  padding e  margin , e para redimensionar elementos podemos usar as

propriedades de largura e altura ou  width e  height . Vamos ver mais a fundo essas propriedades.

É possível determinar as dimensões de um elemento, por exemplo:

p {

 background-color: red;
 height: 300px;
 width: 300px;
}

Todos os parágrafos do nosso HTML ocuparão 300 pixels de altura e de largura, com cor de fundo

vermelha.

Se usarmos o inspetor de elementos do navegador veremos que o restante do espaço ocupado pelo
elemento vira  margin 

Conheça a **Casa do Código**, uma **nova** editora, com autores de destaque no
mercado, foco em **ebooks** (PDF, epub, mobi), preços **imbatíveis** e assuntos
**atuais**.

Com a curadoria da **Caelum** e excelentes autores, é uma abordagem **diferente**
para livros de tecnologia no Brasil.

Casa do Código, Livros de Tecnologia.

# ESPAÇAMENTOS E DIMENSÕES

## 9.1 DIMENSÕES

**Seus livros de tecnologia parecem do século passado?**

9 ESPAÇAMENTOS E DIMENSÕES 
**41**


--------------------------------------------------

A propriedade **padding** é utilizada para definir um espaçamento interno em elementos (por
espaçamento interno queremos dizer a distância entre o limite do elemento, sua borda, e seu respectivo
conteúdo) e tem as subpropriedades listadas a seguir:

padding-top

padding-right

padding-bottom

padding-left

Essas propriedades aplicam uma distância entre o limite do elemento e seu conteúdo acima, à direita,

abaixo e à esquerda respectivamente. Essa ordem é importante para entendermos como funciona a
*shorthand property* (encurtamento) do padding.

Podemos definir todos os valores para as subpropriedades do padding em uma única propriedade,
chamada exatamente de  padding , e seu comportamento é descrito nos exemplos a seguir:

Se passado somente um valor para a propriedade  padding , esse mesmo valor é aplicado em todas

as direções.

p {

 padding: 10px;
}

Se passados dois valores, o primeiro será aplicado acima e abaixo (equivalente a passar o mesmo
valor para  padding-top  e  padding-bottom ) e o segundo será aplicado à direita e à esquerda

(equivalente ao mesmo valor para  padding-right e  padding-left ).

p {

 padding: 10px 15px;
}

Se passados três valores, o primeiro será aplicado acima (equivalente a  padding-top ), o segundo

será aplicado à direita e à esquerda (equivalente a passar o mesmo valor para  padding-right  e

padding-left ) e o terceiro valor será aplicado abaixo do elemento (equivalente a  padding-bottom ).

p {

 padding: 10px 20px 15px;
}

Se passados quatro valores, serão aplicados respectivamente a  padding-top ,  padding-right ,

padding-bottom  e  padding-left . Para facilitar a memorização dessa ordem, basta lembrar que os

valores são aplicados em **sentido horário**.

p {

## 9.2 ESPAÇAMENTOS

**### Padding**

**42** 
9.2 ESPAÇAMENTOS


--------------------------------------------------

 padding: 10px 20px 15px 5px;
}

Uma dica para omitir valores do padding:

Quando precisar omitir valores, sempre omita no sentido anti-horário começando a partir da
subpropriedade  -left .

Como os valores tem posicionamento fixo na hora de declarar os espaçamentos, o navegador
não sabe quando e qual valor deve ser omitido. Por exemplo:

Se tivermos um padding:

  h1 {
   padding: 10px 25px 10px 15px;
  }

O código não pode sofrer o encurtamento porque por mais que os valores de  top  e  bottom 

sejam iguais, os valores  right e  left não são e eles são os primeiros a serem omitidos. Veja o

que acontece quando vamos omitir o valor de  10px do bottom:

  h1 {
      padding: 10px 25px 15px;
  }

O navegador vai interpretar da seguinte maneira:

  h1 {
      padding: top right bottom; 
  }

Que no final vai ficar igual a:

  h1 {
      padding-top: 10px;
      padding-right: 25px;
      padding-bottom: 15px;
      padding-left: 25px;
  }

E esses valores não são os que nós colocamos no começo com  padding: 10px 25px 10px

15px; 

A propriedade  margin  é bem parecida com a propriedade  padding , exceto que ela adiciona

espaço após o limite do elemento, ou seja, é um espaçamento além do elemento em si (espaçamento
externo). Além das subpropriedades listadas a seguir, há a *shorthand property*  margin que se comporta

da mesma maneira que a *shorthand property* do  padding vista no tópico anterior.

**### Margin**

9.2 ESPAÇAMENTOS 
**43**


--------------------------------------------------

margin-top
margin-right

margin-bottom

margin-left

Há ainda uma maneira de permitir que o navegador defina qual será a dimensão da propriedade

padding  ou  margin  conforme o espaço disponível na tela: definimos o valor  auto  para os

espaçamentos que quisermos.

No exemplo a seguir, definimos que um elemento não tem nenhuma margem acima ou abaixo de seu

conteúdo e que o navegador define uma margem igual para ambos os lados de acordo com o espaço
disponível:

p {

 margin: 0 auto;
}

**44** 
9.2 ESPAÇAMENTOS


--------------------------------------------------

CAPÍTULO 10

Nesse exercício trabalharemos com os tamanhos das caixas, com o espaço vazio entre essas caixas e

com o espaço de respiro entre a caixa e seu conteúdo.

Em resumo, iremos:

diminuir a largura do conteúdo da página para **940px**

Para que o conteúdo não fique colado no canto da página, afaste ele dos cantos direito e esquerdo
da tela, até que fique centralizado.
criar um espaço de respiro interno de **10px** para o conteúdo do título principal

criar um espaço de respiro interno de **15px** para o conteúdo das figuras

afastar **30px** as figuras dos cantos da tela e das caixas que vêm antes e depois delas

dentro das figuras, afastar **10px** a legenda da imagem

A página ficará assim:

# EXERCÍCIO: TRABALHANDO COM
# TAMANHOS E ESPAÇAMENTO

## 10.1 OBJETIVO

10 EXERCÍCIO: TRABALHANDO COM TAMANHOS E ESPAÇAMENTO 
**45**


--------------------------------------------------

Figura 10.1: Visual da página ao final do exercício

Se você está gostando dessa apostila, certamente vai aproveitar os **cursos**
**online** que lançamos na plataforma **Alura**. Você estuda a qualquer momento

com a **qualidade** Caelum. Programação, Mobile, Design, Infra, Front-End e
Business, entre outros! Ex-estudante da Caelum tem 10% de desconto, siga o link!

Conheça a Alura Cursos Online.

1. No arquivo ** sobre.css **na pasta ** css **faça as seguintes alterações:

 body {
+  width: 940px;
+  margin-left: auto;
+  margin-right: auto;
+

**Agora é a melhor hora de aprender algo novo**

## 10.2 PASSO A PASSO COM CÓDIGO

**# css/sobre.css**

**46** 
10.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

   font-family: "Helvetica", "Lucida Grande", sans-serif;
   color: #3D3D3D;
 }

 h1 {
+  padding: 10px;
+
   background-color: #E1EDF2;
 }

 h2 {
   border-bottom: 2px solid black;
 }

 figure {
+  margin: 30px;
+  padding: 15px;
+  
   text-align: center;

   background-color: whitesmoke;
   border: 1px solid lightgrey;
 }
+
+figcaption {
+  margin-top: 10px;
+}

10.2 PASSO A PASSO COM CÓDIGO 
**47**


--------------------------------------------------

CAPÍTULO 11

Não são raros os casos em que queremos exibir uma listagem em nossas páginas. O HTML tem algumas

tags definidas para que possamos fazer isso de maneira correta. A lista mais comum é a lista não-
ordenada definida pela tag  <ul> (*unordered list*).

<ul>

 <li>Primeiro item da lista</li>
 <li>
   Segundo item da lista:
   <ul>
     <li>Primeiro item da lista aninhada</li>
     <li>Segundo item da lista aninhada</li>
   </ul>
 </li>
 <li>Terceiro item da lista</li>
</ul>

Note que, para cada item da lista não-ordenada, utilizamos uma marcação de item de lista  <li> 

(*list item*). No exemplo acima, utilizamos uma estrutura composta na qual o segundo item da lista
contém uma nova lista. A mesma tag de item de lista  <li>  é utilizada quando demarcamos uma lista

ordenada.

<ol>

 <li>Primeiro item da lista</li>
 <li>Segundo item da lista</li>
 <li>Terceiro item da lista</li>
 <li>Quarto item da lista</li>
 <li>Quinto item da lista</li>
</ol>

As listas ordenadas ( <ol> - *ordered list*) também podem ter sua estrutura composta por outras listas

ordenadas como no exemplo que temos para as listas não-ordenadas. Também é possível ter listas

ordenadas aninhadas em um item de uma lista não-ordenada e vice-versa.

Existe um terceiro tipo de lista que devemos utilizar para demarcar um glossário, quando listamos

termos e seus significados. Essa lista é a **lista de definição** (*definition list*).

<dl>

 <dt>HTML</dt>
 <dd>
   HTML é a linguagem de marcação de textos utilizada

# LISTAS HTML

## 11.1 LISTAS DE DEFINIÇÃO

**48** 
11 LISTAS HTML


--------------------------------------------------

   para exibir textos como páginas na Internet.
 </dd>
 <dt>Navegador</dt>
 <dd>
   Navegador é o software que requisita um documento HTML
   através do protocolo HTTP e exibe seu conteúdo em uma
   janela.
 </dd>
</dl>

Para estilizar o formato padrão das listas ordenadas e não-ordenadas, podemos utilizar a propriedade

list-style-type no CSS:

 ul {
   /* alterar para circulo antes de cada <li> da lista não-ordenada */
   list-style-type: circle;
 }

 ol {
   /* alterar para uma sequência alfabética antes de cada <li> da lista ordenada */
   list-style-type: upper-alpha;
 }

Também podemos usar a *shorthand property*  list-style: circle 

Editoras tradicionais pouco ligam para ebooks e novas tecnologias. Não dominam
tecnicamente o assunto para revisar os livros a fundo. Não têm anos de
experiência em didáticas com cursos.
Conheça a **Casa do Código**, uma editora diferente, com curadoria da **Caelum** e
obsessão por livros de qualidade a preços justos.

Casa do Código, ebook com preço de ebook.

Quando precisamos indicar que um trecho de texto se refere a um outro conteúdo, seja ele no mesmo

documento ou em outro endereço (por exemplo uma página na web), utilizamos a tag de âncora  <a> .

Existem três diferentes usos para as âncoras. Um deles é a definição de links:

<p>

**Editora Casa do Código com livros de uma forma diferente**

## 11.2 LINKS NO HTML

11.2 LINKS NO HTML 
**49**


--------------------------------------------------

 Visite o site da <a href="https://www.caelum.com.br">Caelum</a>.
</p>

Note que a âncora está demarcando apenas a palavra **Caelum** de todo o conteúdo do parágrafo

exemplificado. Isso significa que, ao clicarmos com o cursor do mouse na palavra **Caelum**, o navegador
redirecionará o usuário para o site da **Caelum**, indicado no atributo  href .

Podemos adicionar o atributo  target=""  para especificar onde que essa página irá carregar. Por

padrão a página irá abrir na mesma aba da página que tem o link, mas se quisermos que a página

abra em outra aba podemos colocar o valor  _blank dentro desse atributo:

<a href="https://www.caelum.com.br" target="_blank">

Outro uso para a tag de âncora é a demarcação de destinos para links dentro do próprio documento,
o que chamamos de ***bookmark***.

<p>Mais informações <a href="#info">aqui</a>.</p>
<p>Conteúdo da página...</p>

<h2 id="info">Mais informações sobre o assunto:</h2>
<p>Informações...</p>

De acordo com o exemplo acima, ao clicarmos sobre a palavra **aqui**, demarcada com um link, o

usuário será levado à porção da página onde o *bookmark* **info** é visível. *Bookmark* é o elemento que tem
o atributo  id .

É possível, com o uso de um link, levar o usuário a um *bookmark* presente em outra página.

<a href="http://www.caelum.com.br/curso/wd43/#contato">

 Entre em contato sobre o curso
</a>

O exemplo acima fará com que o usuário que clicar no link seja levado à porção da página indicada

no endereço, especificamente no ponto onde o *bookmark* **contato** seja visível.

O outro uso para a tag de âncora é a demarcação de destinos para links dentro do próprio site, mas
não na mesma página que estamos. Por exemplo, estamos na página **sobre.html** e queremos um link
para a página **index.html**.

<p>Acesse <a href="index.html">nossa loja</a>.</p>

**50** 
11.2 LINKS NO HTML


--------------------------------------------------

CAPÍTULO 12

Criaremos uma nova seção no final da página que listará todos os diferenciais da MusicDot. Os textos

de cada item dessa lista estão em **textos/sobre.txt**. Lembre-se que a ordem dos itens não é importante.

Agora que temos mais seções e bastante conteúdo, podemos melhorar a navegação e a experiência
das pessoa que acessarem essa página. Adicionaremos vários links úteis no conteúdo que já temos.

No segundo parágrafo da página adicione um link ao redor de "Mafra, em Santa Catarina" que
aponta para a localização ficticia da MusicDot no Google Maps: "http://maps.google.com.br/?

q=190,GabrielDequech,Mafra,SC".

No terceiro parágrafo da página, adicione os seguintes links:

"nosso site" apontando para a página principal do nosso site em "index.html"

"nossa história" apontando para a página sobre, porém tendo como alvo o subtítulo  <h2>

História </h2> 

"nossos diferenciais" apontando para a página sobre, porém tendo como alvo o subtítulo  <h2>

Diferenciais </h2> 

Figura 12.1: Links com destaque nos parágrafos do início da página

# EXERCÍCIO: USANDO LINKS E LISTAS

## 12.1 OBJETIVO

12 EXERCÍCIO: USANDO LINKS E LISTAS 
**51**


--------------------------------------------------

Figura 12.2: Lista de diferenciais no final da página

A **Alura** oferece centenas de **cursos online** em sua plataforma exclusiva de
ensino que favorece o aprendizado com a **qualidade** reconhecida da Caelum.
Você pode escolher um curso nas áreas de Programação, Front-end, Mobile,

Design & UX, Infra, Business, entre outras, com um plano que dá acesso a todos os cursos. Ex-
estudante da Caelum tem 10% de desconto neste link!

Conheça os cursos online Alura.

1. Crie o arquivo ** index.html **na pasta ** raíz do projeto **com o seguinte código:

+<h1> Página principal temporária da MusicDot </h1>

2. No arquivo ** sobre.html **na pasta ** raíz do projeto **faça as seguintes alterações:

 *<!doctype html>*

**Já conhece os cursos online Alura?**

## 12.2 PASSO A PASSO COM CÓDIGO

**# index.html**

**# sobre.html**

**52** 
12.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

 <html lang="pt-BR">
   <head>
     <meta charset="utf-8">
     <title>
       MusicDot | Sobre a empresa
     </title>
     <link href="img/favicon.ico" rel="icon">
     <link rel="stylesheet" href="css/sobre.css">
   </head>

   <body>

     <img src="img/logo.svg" alt="MusicDot">

     <h1> Sobre a empresa </h1>

     <p>
       A MusicDot é a maior escola online de música em todo o mundo.
       Fundada em 1932, possui estúdios em 124 países, sendo líder de mercado com mais de 90% de
       participação em 118 deles.
     </p>

     <p>
-      N̶o̶s̶s̶a̶ m̶a̶t̶r̶i̶z̶ f̶i̶c̶a̶ e̶m̶ M̶a̶f̶r̶a̶,̶ e̶m̶ S̶a̶n̶t̶a̶ C̶a̶t̶a̶r̶i̶n̶a̶.̶ D̶e̶ l̶á̶,̶ s̶a̶e̶m̶ g̶r̶a̶n̶d̶e̶ p̶a̶r̶t̶e̶ d̶a̶s̶ g̶r̶a̶v̶a̶ç̶õ̶e̶s̶ d̶e̶ n̶
o̶s̶s̶o̶s̶ c̶u̶r̶s̶o̶s̶.̶ N̶o̶s̶s̶a̶ m̶a̶t̶r̶i̶z̶:̶

+      Nossa matriz fica em <a href="https://maps.google.com.br/?q=190,GabrielDequech,Mafra,SC"> 
Mafra, em Santa Catarina </a>. De lá, saem grande parte das gravações de nossos cursos. Nossa matr
iz:

     </p>

     <figure>
       <img src="img/matriz-musicdot.png" alt="Matriz da musicdot">
       <figcaption>
           Matriz MusicDot 
       </figcaption>
     </figure>

     <p>
-      A̶s̶s̶i̶n̶e̶ o̶s̶ c̶u̶r̶s̶o̶s̶ d̶a̶ M̶u̶s̶i̶c̶D̶o̶t̶.̶ A̶c̶e̶s̶s̶e̶ n̶o̶s̶s̶o̶ s̶i̶t̶e̶ o̶u̶ e̶n̶t̶r̶e̶ e̶m̶ c̶o̶n̶t̶a̶t̶o̶
-      s̶e̶ t̶i̶v̶e̶r̶ d̶ú̶v̶i̶d̶a̶s̶.̶ C̶o̶n̶h̶e̶ç̶a̶ t̶a̶m̶b̶é̶m̶ n̶o̶s̶s̶a̶ h̶i̶s̶t̶ó̶r̶i̶a̶ e̶ n̶o̶s̶s̶o̶s̶ d̶i̶f̶e̶r̶e̶n̶c̶i̶a̶i̶s̶.̶
+      Assine os cursos da MusicDot. Acesse <a href="index.html"> nosso site </a> ou entre em con
tato

+      se tiver dúvidas. Conheça também <a href="#historia"> nossa história </a> e <a href="#dife
renciais"> nossos diferenciais </a>.

     </p>

-    <̶h̶2̶>̶ H̶i̶s̶t̶ó̶r̶i̶a̶ </̶h̶2̶>
+    <h2 id="historia"> História </h2>

     <figure>
       <img src="img/familia-tupfeln.jpg" alt="Foto da família tüpfeln">
       <figcaption>Família Tüpfeln</figcaption>
     </figure>

     <p>
       A fundação em 1932 ocorreu no momento da descoberta econônica de cursos por stream online 
no interior de Santa Catarina. A

       família Tüpfeln, tradicional da região, investiu todas as suas economias nessa nova inicia
tiva,

       revolucionária para a época. A fundadora frau Dagmar Olaf Tüpfeln, dotada de particular vi
são

       administrativa, guiou os negócios da empresa durante mais de 50 anos, muitos deles ao lado
       de seu filho Ernst Noten Tüpfeln, atual CEO. O nome da empresa é inspirado no nome da famí

12.2 PASSO A PASSO COM CÓDIGO 
**53**


--------------------------------------------------

lia.

     </p>

     <p>
       O crescimento da empresa foi praticamente instantâneo. Nos primeiros 5 anos, já atendia 18
países.
       Bateu a marca de 100 países em apenas 15 anos de existência. Até hoje, já atendeu 2 bilhõe
s

       de usuários diferentes, em bilhões de diferentes pedidos.
     </p>

     <p>
       O crescimento em número de funcionários é também assombroso. Hoje, é a maior empregadora d
o

       Brasil, mas mesmo após apenas 5 anos de sua existência, já possuía 30 mil funcionários. Fo
ra do

       Brasil, há 240 mil funcionários, além dos 890 mil brasileiros nas instalações de Mafra e
       nos escritórios em todo país.
     </p>

     <p>
       Dada a importância econômica da empresa para o Brasil, a família Tüpfeln já recebeu divers
os prêmios,

       homenagens e condecorações. Todos os presidentes do Brasil já visitaram as instalações da 
MusicDot, além de presidentes da União Européia, Ásia e o secretário-geral da ONU.

     </p>

+    <h2 id="diferenciais"> Diferenciais </h2>
+    <ul>
+      <li> Menor preço do mercado, garantido </li>
+      <li> Se você achar um serviço mais barato, leva 1 mês de graça </li>
+      <li> Pague em reais, dólares, euros, libras, dodgecoins, litecoins ou bitcoins </li>
+      <li> Todas as compras acompanham acesso à Alura </li>
+      <li> Maior escola de música online do mundo </li>
+      <li> Atendimento via telefone, email, chat, twitter, facebook, instagram, ICQ, WhatsApp, S
MS, carta, fax, sinal de fumaça e telegrama </li>

+      <li> Presente em 124 países </li>
+      <li> Mais de um milhão de funcionários em todo o mundo </li>
+    </ul>
   </body>
 </html>

**54** 
12.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

CAPÍTULO 13

Durante o curso veremos outros tipos de seletores. Por hora veremos um seletor que deixa nossa
estilização um pouco mais precisa do que fazemos agora.

Vamos com o exemplo a seguir:

**HTML:**

<img src="img/logo-musicdot" atl="Logo da MusicDot">

<figure>

   <img src="img/matriz-musicdot" alt="Foto da matriz da MusicDot">
   <figcaption>Matriz da MusicDot</figcaption>
</figure>

<figure>

   <img src="img/familia-tupfeln" alt="Foto da família Tupfeln">
   <figcaption>Família Tüpfeln</figcaption>
</figure>

**CSS:**

img {

   width: 300px;
}

No código acima estamos aplicando uma largura de  300px para todas as tags  <img> . Mas e se nós

só quisermos aplicar essa largura apenas para as imagens que estão nas figuras? É aí que entra o seletor

mais específico:

figure img {

   width: 300px;
}

Agora estamos aplicando a largura de  300px  apenas às imagens que são filhas de uma tag

<figure> .

Outra forma de selecionar elementos mais específicos é usando o atributo  id="" nos elementos que

queremos estilizar e depois fazer a chamada de seletor de  id :

**HTML:**

# SELETORES MAIS ESPECÍFICOS E
# HERANÇA

13 SELETORES MAIS ESPECÍFICOS E HERANÇA 
**55**


--------------------------------------------------

<img src="img/logo-musicdot" atl="Logo da MusicDot">

<figure>

   <img src="img/matriz-musicdot" alt="Foto da matriz da MusicDot" id="matriz-musicdot">
   <figcaption>Matriz da MusicDot</figcaption>
</figure>

<figure>

   <img src="img/familia-tupfeln" alt="Foto da família Tupfeln" id="familia-tupfeln">
   <figcaption>Família Tüpfeln</figcaption>
</figure>

**CSS:**

#matriz-musicdot {

   width: 300px;
}

#familia-tupfeln {

   width: 300px;
}

Só que não é recomendado o uso de  id para a estilização de elementos já que a idéia do atributo é

para fazer uma referência única na página como fizemos na parte dos links. Quando queremos estilizar
elementos específicos é melhor utilizar o atributo  class="" . O comportamento no CSS será idêntico

ao do atributo  id="" , mas  class foi feito para ser usado no CSS e no JavaScript.

Arrumando o exemplo anterior, usando classes:

**HTML:**

<img src="img/logo-musicdot" atl="Logo da MusicDot">

<figure>

   <img src="img/matriz-musicdot" alt="Foto da matriz da MusicDot" class="matriz-musicdot">
   <figcaption>Matriz da MusicDot</figcaption>
</figure>

<figure>

   <img src="img/familia-tupfeln" alt="Foto da família Tupfeln" class="familia-tupfeln">
   <figcaption>Família Tüpfeln</figcaption>
</figure>

**CSS:**

.matriz-musicdot {

   width: 300px;
}

.familia-tupfeln {

   width: 300px;
}

Existe uma coisa muito importante no CSS que precisamos tomar cuidado é o **grau de**

**especificidade de um seletor**. Isto é, a prioridade de interpretação de um seletor pelo navegador. Para

**### Grau de especificidade de um seletor**

**56** 
13 SELETORES MAIS ESPECÍFICOS E HERANÇA


--------------------------------------------------

entender estas regras de especificidade de um selector, ao criarmos um seletor de tag a sua pontuação se

torna **1**. Quando usamos um seletor de classe sua pontuação se torna **10**. Quando usamos um seletor de
id sua pontuação se torna **100**. Ao fim, o navegador soma a pontuação dos seletores aplicados à um

elemento, e as propriedades com o seletor de maior pontuação são as que valem.

<body>

   <p class="paragrafo" id="paragrafo-rosa">Texto</p>
</body>

p { /* Pontuação 1 */

   color: blue;
}

.paragrafo { /* Pontuação 10 */

   color: red;
}

#paragrafo-rosa { /* Pontuação 100 */

   color: pink;
}

No exemplo acima o parágrafo vai ficar com a cor rosa porque o seletor que tem a cor rosa é o

seletor de maior pontuação.

Quando elementos possuem a mesma pontuação quem prevalece é a propriedade do último seletor:

p { /* Pontuação 1 */

   color: blue;
}

p { /* Pontuação 1 */

   color: red;
}

No exemplo acima a cor do parágrafo será vermelha.

Podemos também somar os pontos para deixar nosso seletor mais forte:

body p { /* Seletor de tag + outro seletor de tag = 2 pontos */

   color: brown;
}

p { /* Pontuação 1 */

   color: blue;
}

No exemplo acima nós deixamos nosso seletor mais específico para os  <p>  que estão dentro de

uma tag <body> , portanto a cor do parágrafo será marrom.

Em resumo:

Quanto mais específico é o nosso seletor, maior sua pontuação no nível de especificidade do CSS.

Portanto devemos sempre trabalhar com uma baixa especificidade, para que não seja impossível
sobrescrever valores quando necessário em uma situação específica.

13 SELETORES MAIS ESPECÍFICOS E HERANÇA 
**57**


--------------------------------------------------

A cascata do CSS, significa justamente a possibilidade de elementos filhos herdarem características
de estilização de elementos superiores, estas definidas por suas propriedades, que podem ou não passar
aos seus descendentes seus valores.

Vamos ver o exemplo de código a seguir:

*<!DOCTYPE html>*
<html>
<head>

   <meta charset="UTF-8">
   <title>Um exemplo</title>
</head>
<body>

   <p>Uma breve explicação de algo com um <a href="https://google.com.br">link</a> para uma referênc
ia de outra página</p>

   <figure>
       <img src="img/foto" alt="Uma foto">
       <figcaption>Uma foto</figcaption>
   </figure>
</body>
</html>

Vamos mudar a família da fonte de toda a página. Uma maneira que podemos fazer é selecionar

todas as tags que contém text ( <p> ,  <a>  e  <figcaption> ) e colocar a família de fonte que

queremos:

p {

   font-family: 'Helvetica', sans-serif;
}

a {

   font-family: 'Helvetica', sans-serif;
}

figcaption {

   font-family: 'Helvetica', sans-serif;
}

Mas isso dá muito trabalho e estamos repetindo código. Ao invés de colocar essa propriedade em
cada um dos elementos textuais da nossa página, podemos colocar no elemento superior a estas tags,

neste caso é o elemento  <body> .

body {

   font-family: 'Helvetica', sans-serif;
}

No exemplo acima todos os elementos filhos da tag  <body>  vão receber a propriedade  font-

family:  e isso é o que nós chamamos de **herança**. Herança acontece quando elementos herdam

propriedades dos elementos acima deles (elementos pai).

*Obs: Para saber se uma propriedade deixa herança ou não, é possível consultar na sua*
*especificação ou no site MDN **https://developer.mozilla.org/**.*

**### Herança**

**58** 
13 SELETORES MAIS ESPECÍFICOS E HERANÇA


--------------------------------------------------

Imagine que temos a seguinte divisão com uma imagem:

<div>

   <img src="box-model.png" alt="box model">
</div>

div {

   border: 2px solid;
   border-color: red;
   width: 30px;
   height: 30px;
}

Queremos que a imagem preencha todo o espaço da  <div> , mas as propriedades  width  e

height  não são aplicadas em cascata, sendo assim, somos obrigados a definir o tamanho da imagem

manualmente:

img {

   width: 30px;
   height: 30px;
}

Esta não é uma solução sustentável, porque, caso alterarmos o tamanho da  <div> , teremos que

lembrar de alterar também o tamanho da imagem. Uma forma de resolver este problema é utilizando o
valor **inherit** para as propriedades  width e  height da imagem:

img {

   width: inherit;
   height: inherit;
}

O valor  inherit  indica para o elemento filho que ele deve utilizar o mesmo valor presente no

elemento pai, sendo assim, toda vez que o tamanho do elemento pai for alterado, automaticamente o
elemento filho herdará o novo valor, facilitando assim, a manutenção do código.

Lembre-se de que o  inherit também afeta propriedades que não são aplicadas em cascata.

## 13.1 PARA SABER MAIS: O VALOR INHERIT

13.1 PARA SABER MAIS: O VALOR INHERIT 
**59**


--------------------------------------------------

Querendo aprender ainda mais sobre? Esclarecer dúvidas dos exercícios? Ouvir

explicações detalhadas com um instrutor?

A Caelum oferece o **curso data** presencial nas cidades de São Paulo, Rio de
Janeiro e Brasília, além de turmas incompany.

Consulte as vantagens do curso *Desenvolvimento Web com HTML, CSS e*
*JavaScript*

**Você pode também fazer o curso data dessa apostila na Caelum**

**60** 
13.1 PARA SABER MAIS: O VALOR INHERIT


--------------------------------------------------

CAPÍTULO 14

No momento as figuras da página ocupam praticamente a largura da tela inteira. Nesse exercício,

diminuiremos a largura das duas tags  <figure>  da página. Além das larguras, também alteraremos a

disposição de cada figura na página. Cada uma terá uma largura e disposição diferentes.

A  <figure> da matriz deverá ter **550px** de largura e deve estar centralizada em relação à página. A

<figure>  da família devera ter **275px** de largura, deve ficar alinhada à direita e envolta pelos textos

que no HTML vêm abaixo dela.

Ao alterar a largura das tags  <figure> você notará que as tags  <img> dentro delas são maiores e

ultrapassam a caixa da figura:

Figura 14.1: A imagem da matriz é maior do que os 550px da <figure>

Para resolver isso podemos dizer que toda tag  <img>  dentro de uma tag  <figure>  deve ocupar

todo o espaço que definimos, mas não mais que isso.

O resultado final será assim:

# EXERCÍCIO: SELECIONANDO
# ELEMENTOS MAIS ESPECÍFICOS E
# HERANÇA

## 14.1 OBJETIVO

14 EXERCÍCIO: SELECIONANDO ELEMENTOS MAIS ESPECÍFICOS E HERANÇA 
**61**


--------------------------------------------------

Figura 14.2: Resultado final da figura da matriz

Figura 14.3: Resultado final da figura da família

Conheça a **Casa do Código**, uma **nova** editora, com autores de destaque no
mercado, foco em **ebooks** (PDF, epub, mobi), preços **imbatíveis** e assuntos
**atuais**.

Com a curadoria da **Caelum** e excelentes autores, é uma abordagem **diferente**
para livros de tecnologia no Brasil.

Casa do Código, Livros de Tecnologia.

1. No arquivo ** sobre.css **na pasta ** css **faça as seguintes alterações:

 body {
   width: 940px;
   margin-left: auto;

**Seus livros de tecnologia parecem do século passado?**

## 14.2 PASSO A PASSO COM CÓDIGO

**# css/sobre.css**

**62** 
14.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

   margin-right: auto;

   font-family: "Helvetica", "Lucida Grande", sans-serif;
   color: #3D3D3D;
 }

 h1 {
   padding: 10px;

   background-color: #E1EDF2;
 }

 h2 {
   border-bottom: 2px solid black;
 }

 figure {
   margin: 30px;
   padding: 15px;

   text-align: center;

   background-color: whitesmoke;
   border: 1px solid lightgrey;
 }

 figcaption {
   margin-top: 10px;
 }
+
+.matriz-musicdot {
+  width: 550px;
+  margin-left: auto;
+  margin-right: auto;
+}
+
+.familia-tupfeln {
+  width: 275px;
+  float: right;
+}
+
+figure img {
+  width: 100%;
+}

2. No arquivo ** sobre.html **na pasta ** raíz do projeto **faça as seguintes alterações:

 *<!doctype html>*
 <html lang="pt-BR">
   <head>
     <meta charset="utf-8">
     <title>
       MusicDot | Sobre a empresa
     </title>
     <link href="img/favicon.ico" rel="icon">
     <link rel="stylesheet" href="css/sobre.css">
   </head>

   <body>

**# sobre.html**

14.2 PASSO A PASSO COM CÓDIGO 
**63**


--------------------------------------------------

     <img src="img/logo.svg" alt="MusicDot">

     <h1> Sobre a empresa </h1>

     <p>
       A MusicDot é a maior escola online de música em todo o mundo.
       Fundada em 1932, possui estúdios em 124 países, sendo líder de mercado com mais de 90% de
       participação em 118 deles.
     </p>

     <p>
       Nossa matriz fica em <a href="https://maps.google.com.br/?q=190,GabrielDequech,Mafra,SC"> 
Mafra, em Santa Catarina </a>. De lá, saem grande parte das gravações de nossos cursos. Nossa matr
iz:

     </p>

-    <̶f̶i̶g̶u̶r̶e̶>
+    <figure class="matriz-musicdot">
       <img src="img/matriz-musicdot.png" alt="Matriz da musicdot">
       <figcaption>
           Matriz MusicDot 
       </figcaption>
     </figure>

     <p>
       Assine os cursos da MusicDot. Acesse <a href="index.html"> nosso site </a> ou entre em con
tato

       se tiver dúvidas. Conheça também <a href="#historia"> nossa história </a> e <a href="#dife
renciais"> nossos diferenciais </a>.

     </p>

     <h2 id="historia"> História </h2>

-    <̶f̶i̶g̶u̶r̶e̶>
+    <figure class="familia-tupfeln">
       <img src="img/familia-tupfeln.jpg" alt="Foto da família tüpfeln">
       <figcaption>Família Tüpfeln</figcaption>
     </figure>

     <p>
       A fundação em 1932 ocorreu no momento da descoberta econônica de cursos por stream online 
no interior de Santa Catarina. A

       família Tüpfeln, tradicional da região, investiu todas as suas economias nessa nova inicia
tiva,

       revolucionária para a época. A fundadora frau Dagmar Olaf Tüpfeln, dotada de particular vi
são

       administrativa, guiou os negócios da empresa durante mais de 50 anos, muitos deles ao lado
       de seu filho Ernst Noten Tüpfeln, atual CEO. O nome da empresa é inspirado no nome da famí
lia.

     </p>

     <p>
       O crescimento da empresa foi praticamente instantâneo. Nos primeiros 5 anos, já atendia 18
países.
       Bateu a marca de 100 países em apenas 15 anos de existência. Até hoje, já atendeu 2 bilhõe
s

       de usuários diferentes, em bilhões de diferentes pedidos.
     </p>

     <p>
       O crescimento em número de funcionários é também assombroso. Hoje, é a maior empregadora d
o

       Brasil, mas mesmo após apenas 5 anos de sua existência, já possuía 30 mil funcionários. Fo

**64** 
14.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

ra do

       Brasil, há 240 mil funcionários, além dos 890 mil brasileiros nas instalações de Mafra e
       nos escritórios em todo país.
     </p>

     <p>
       Dada a importância econômica da empresa para o Brasil, a família Tüpfeln já recebeu divers
os prêmios,

       homenagens e condecorações. Todos os presidentes do Brasil já visitaram as instalações da 
MusicDot, além de presidentes da União Européia, Ásia e o secretário-geral da ONU.

     </p>

     <h2 id="diferenciais"> Diferenciais </h2>
     <ul>
       <li> Menor preço do mercado, garantido </li>
       <li> Se você achar um serviço mais barato, leva 1 mês de graça </li>
       <li> Pague em reais, dólares, euros, libras, dodgecoins, litecoins ou bitcoins </li>
       <li> Todas as compras acompanham acesso à Alura </li>
       <li> Maior escola de música online do mundo </li>
       <li> Atendimento via telefone, email, chat, twitter, facebook, instagram, ICQ, WhatsApp, S
MS, carta, fax, sinal de fumaça e telegrama </li>

       <li> Presente em 124 países </li>
       <li> Mais de um milhão de funcionários em todo o mundo </li>
     </ul>
   </body>
 </html>

14.2 PASSO A PASSO COM CÓDIGO 
**65**


--------------------------------------------------

CAPÍTULO 15

Muitas vezes quando estamos declarando os estilos de uma página HTML, achamos mais fácil usar o

seletor de nome da tag ao invés de usar classes. Porém isto pode causar problemas imprevistos se não
usado com cautela. Vamos analisar o seguinte código para entender a situação:

**HTML:**

<h1>MusicDot</h1>

<h2>História</h2>
<p>Texto</p>

<h2>Diferenciais</h2>
<ul>

   <li>Diferencial 1</li>
   <li>Diferencial 2</li>
   <li>Diferencial 3</li>
</ul>

**CSS:**

h2 {

   font-size: 24px;
   font-weight: bold;
   border-bottom: 1px solid #000000;
}

No exemplo acima adicionamos estilo nas tags  <h2>  para ter um tamanho de fonte maior, uma

fonte mais grossa e uma borda abaixo para fazer o efeito de linha divisória. Até aqui tudo certo. Mas

agora vamos colocar um outro título na página chamada "Sobre a MusicDot" e esse título tem relevância
maior do que os dois outros títulos que temos (História e Diferenciais), portanto vamos ter que
modificar suas tags para uma de menos importância:

<h1>MusicDot</h1>

<h2>Sobre a MusicDot</h2>
<p>Introdução</p>

<!-- Mudamos para h3 pois queremos que tenham menos relevância que o título "Sobre a MusicDot" -->
<h3>História</h3>
<p>Texto</p>

<!-- Mudamos para h3 pois queremos que tenham menos relevância que o título "Sobre a MusicDot" -->
<h3>Diferenciais</h3>
<ul>

   <li>Diferencial 1</li>

# DESACOPLAMENTO COM CLASSES

**66** 
15 DESACOPLAMENTO COM CLASSES


--------------------------------------------------

   <li>Diferencial 2</li>
   <li>Diferencial 3</li>
</ul>

Agora com essa mudança da estrutura do HTML o nosso CSS está alterando um elemento que não é
o que nós inicialmente queríamos mudar. Vamos ter que fazer a mudança no CSS para usar as nossas
alterações no elemento certo.

Neste exemplo a solução é relativamente simples, porém imagine que temos seletores bem mais

complexos, com heranças etc... a mudança não seria tão simples. Por isso o ideal é declarar estilos com
classes ao invés de nomes de tags. Uma dica pra dar nome às classes é elas representarem o papel que
estas tags estão exercendo em conjunto com os estilos declarados, no nosso caso, estamos declarando

um conjunto de estilo para subtítulos.

Veja como fica o resultado do desacoplamento do conjunto de estilos do nome da tag, para ser agora
com classes:

**HTML:**

<h1>MusicDot</h1>

<h2>Sobre a MusicDot</h2>
<p>Introdução</p>

<!-- Adicionamos a classe subtitulo-->
<h3 class="subtitulo">História</h3>
<p>Texto</p>

<!-- Adicionamos a classe subtitulo-->
<h3 class="subtitulo">Diferenciais</h3>
<ul>

   <li>Diferencial 1</li>
   <li>Diferencial 2</li>
   <li>Diferencial 3</li>
</ul>

**CSS:**

.subtitulo {

   font-size: 24px;
   font-weight: bold;
   border-bottom: 1px solid #000000;
}

Usando classes, podemos alterar toda a estrutura HTML sem nos preocupar se estas alterações
afetarão a estilização que fizemos no começo.

15 DESACOPLAMENTO COM CLASSES 
**67**


--------------------------------------------------

CAPÍTULO 16

Adicionaremos uma nova seção com as informações de contato e começaremos colocando e estilizando

apenas o título dessa nova seção.

O novo título de contato é na verdade um subtítulo da página e por isso usaremos uma tag  <h2> .

Porém, o estilo desse  <h2>  deve ser o mesmo da tag  <h1>  que temos na página. O desafio aqui é

estilizar tanto o  <h1> Sobre a empresa </h1> quanto o  <h2> Contato </h2> sem repetir o código

CSS para cada um e sem depender do nome da tag que usamos.

Uma dica é que podemos usar os tipos de seletores que vimos anteriormente para desacoplar nosso

código CSS do HTML da página. Traduzindo, deixaremos de depender do nome das tags que
escolhemos e passaremos a selecionar ambas as tags no CSS de uma forma mais específica e
aplicaremos o mesmo estilo nas duas.

Para que esse estilo funcione, não poderemos mais estilizar todos os  <h2>  como fazemos agora.

Será preciso também alterar os estilos genéricos de todo  <h2>  para que estilizem apenas os subtítulos

<h2> História </h2> e  <h2> Diferenciais </h2> 

No final teremos o novo título aparecendo na página com o seguinte estilo:

Figura 16.1: Novo subtítulo "Contato" com mesmo estilo do título principal

# EXERCÍCIO: USANDO CLASSES PARA
# EVITAR ACOPLAMENTO DE ESTILOS

## 16.1 OBJETIVO

**68** 
16 EXERCÍCIO: USANDO CLASSES PARA EVITAR ACOPLAMENTO DE ESTILOS


--------------------------------------------------

Se você está gostando dessa apostila, certamente vai aproveitar os **cursos**

**online** que lançamos na plataforma **Alura**. Você estuda a qualquer momento
com a **qualidade** Caelum. Programação, Mobile, Design, Infra, Front-End e
Business, entre outros! Ex-estudante da Caelum tem 10% de desconto, siga o link!

Conheça a Alura Cursos Online.

1. No arquivo ** sobre.css **na pasta ** css **faça as seguintes alterações:

 body {
   width: 940px;
   margin-left: auto;
   margin-right: auto;

   font-family: "Helvetica", "Lucida Grande", sans-serif;
   color: #3D3D3D;
 }

-h̶1̶ {̶
+.titulo {
   padding: 10px;

+  font-size: 32px;
+
   background-color: #E1EDF2;
 }

-h̶2̶ {̶
+.subtitulo {
   border-bottom: 2px solid black;
 }

 figure {
   margin: 30px;
   padding: 15px;

   text-align: center;

   background-color: whitesmoke;
   border: 1px solid lightgrey;
 }

 figcaption {
   margin-top: 10px;

**Agora é a melhor hora de aprender algo novo**

## 16.2 PASSO A PASSO COM CÓDIGO

**# css/sobre.css**

16.2 PASSO A PASSO COM CÓDIGO 
**69**


--------------------------------------------------

 }

 .matriz-musicdot {
   width: 550px;
   margin-left: auto;
   margin-right: auto;
 }

 .familia-tupfeln {
   width: 275px;
   float: right;
 }

 figure img {
   width: 100%;
 }

2. No arquivo ** sobre.html **na pasta ** raíz do projeto **faça as seguintes alterações:

 *<!doctype html>*
 <html lang="pt-BR">
   <head>
     <meta charset="utf-8">
     <title>
       MusicDot | Sobre a empresa
     </title>
     <link href="img/favicon.ico" rel="icon">
     <link rel="stylesheet" href="css/sobre.css">
   </head>

   <body>

     <img src="img/logo.svg" alt="MusicDot">

-    <̶h̶1̶>̶ S̶o̶b̶r̶e̶ a̶ e̶m̶p̶r̶e̶s̶a̶ </̶h̶1̶>
+    <h1 class="titulo"> Sobre a empresa </h1>

     <p>
       A MusicDot é a maior escola online de música em todo o mundo.
       Fundada em 1932, possui estúdios em 124 países, sendo líder de mercado com mais de 90% de
       participação em 118 deles.
     </p>

     <p>
       Nossa matriz fica em <a href="https://maps.google.com.br/?q=190,GabrielDequech,Mafra,SC"> 
Mafra, em Santa Catarina </a>. De lá, saem grande parte das gravações de nossos cursos. Nossa matr
iz:

     </p>

     <figure class="matriz-musicdot">
       <img src="img/matriz-musicdot.png" alt="Matriz da musicdot">
       <figcaption>
           Matriz MusicDot 
       </figcaption>
     </figure>

     <p>
       Assine os cursos da MusicDot. Acesse <a href="index.html"> nosso site </a> ou entre em con
tato

       se tiver dúvidas. Conheça também <a href="#historia"> nossa história </a> e <a href="#dife

**# sobre.html**

**70** 
16.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

renciais"> nossos diferenciais </a>.

     </p>

-    <̶h̶2̶ i̶d̶=̶"̶h̶i̶s̶t̶o̶r̶i̶a̶"̶>̶ H̶i̶s̶t̶ó̶r̶i̶a̶ </̶h̶2̶>
+    <h2 id="historia" class="subtitulo"> História </h2>

     <figure class="familia-tupfeln">
       <img src="img/familia-tupfeln.jpg" alt="Foto da família tüpfeln">
       <figcaption>Família Tüpfeln</figcaption>
     </figure>

     <p>
       A fundação em 1932 ocorreu no momento da descoberta econônica de cursos por stream online 
no interior de Santa Catarina. A

       família Tüpfeln, tradicional da região, investiu todas as suas economias nessa nova inicia
tiva,

       revolucionária para a época. A fundadora frau Dagmar Olaf Tüpfeln, dotada de particular vi
são

       administrativa, guiou os negócios da empresa durante mais de 50 anos, muitos deles ao lado
       de seu filho Ernst Noten Tüpfeln, atual CEO. O nome da empresa é inspirado no nome da famí
lia.

     </p>

     <p>
       O crescimento da empresa foi praticamente instantâneo. Nos primeiros 5 anos, já atendia 18
países.
       Bateu a marca de 100 países em apenas 15 anos de existência. Até hoje, já atendeu 2 bilhõe
s

       de usuários diferentes, em bilhões de diferentes pedidos.
     </p>

     <p>
       O crescimento em número de funcionários é também assombroso. Hoje, é a maior empregadora d
o

       Brasil, mas mesmo após apenas 5 anos de sua existência, já possuía 30 mil funcionários. Fo
ra do

       Brasil, há 240 mil funcionários, além dos 890 mil brasileiros nas instalações de Mafra e
       nos escritórios em todo país.
     </p>

     <p>
       Dada a importância econômica da empresa para o Brasil, a família Tüpfeln já recebeu divers
os prêmios,

       homenagens e condecorações. Todos os presidentes do Brasil já visitaram as instalações da 
MusicDot, além de presidentes da União Européia, Ásia e o secretário-geral da ONU.

     </p>

-    <̶h̶2̶ i̶d̶=̶"̶d̶i̶f̶e̶r̶e̶n̶c̶i̶a̶i̶s̶"̶>̶ D̶i̶f̶e̶r̶e̶n̶c̶i̶a̶i̶s̶ </̶h̶2̶>
+    <h2 id="diferenciais" class="subtitulo"> Diferenciais </h2>
     <ul>
       <li> Menor preço do mercado, garantido </li>
       <li> Se você achar um serviço mais barato, leva 1 mês de graça </li>
       <li> Pague em reais, dólares, euros, libras, dodgecoins, litecoins ou bitcoins </li>
       <li> Todas as compras acompanham acesso à Alura </li>
       <li> Maior escola de música online do mundo </li>
       <li> Atendimento via telefone, email, chat, twitter, facebook, instagram, ICQ, WhatsApp, S
MS, carta, fax, sinal de fumaça e telegrama </li>

       <li> Presente em 124 países </li>
       <li> Mais de um milhão de funcionários em todo o mundo </li>
     </ul>
+    
+    <h2 class="titulo"> Contato </h2>
+

16.2 PASSO A PASSO COM CÓDIGO 
**71**


--------------------------------------------------

   </body>
 </html>

**72** 
16.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

CAPÍTULO 17

Vimos muitas tags para representar diversos elementos em nossa página HTML como, por exemplo,

<h1> para títulos,  <p>  para parágrafos,  <figure>  para figuras, etc. Nossa maior preocupação com

desenvolvimento de páginas deve ser conseguir representar tudo com tags que condizem com o seu

conteúdo. Veremos tags como, por exemplo,  <section> ,  <article> ,  <address> , entre outras, com

a intenção de representar com maior precisão o conteúdo que queremos mostrar. Estas tags são
chamadas também de elementos semânticos, ou seja, que conseguem passar uma informação com um
significado específico para o conteúdo interpretado pelo navegador, não depende apenas do texto dentro

da tag para se entender o que há naquela parte do site.

Um dos grandes motivos para nos preocuparmos com a semântica que usamos no site vem das
ferramentas de indexação de buscadores, que colocam os sites mais semânticos e estruturados como
prioridade nas respostas das buscas. A outra grande preocupação é com as ferramentas de acessibilidade,

que permitem que pessoas com deficiência, por exemplo pessoas cegas, consigam usar um site através
de softwares leitores de tela de maneira padronizada e sem problemas.

Uma coisa que precisamos lembrar é que devemos escolher as tags pelo o que elas representam e
não como elas são mostradas na tela do navegador. Estilização deve ficar no CSS e estrutura no HTML.

As únicas tags que são de propósito genérico e que são usadas apenas para facilitar a estilização no

CSS são as tags  <div>  e  <span> . Essas duas tags não representam nenhum conteúdo

necessariamente.  <div>  representa uma divisão de blocos e  <span>  uma marcação para texto (sem

quebrar a linha do texto).

# ELEMENTOS ESTRUTURAIS E
# SEMÂNTICA DOS ELEMENTOS

17 ELEMENTOS ESTRUTURAIS E SEMÂNTICA DOS ELEMENTOS 
**73**


--------------------------------------------------

CAPÍTULO 18

Agora continuaremos com o conteúdo da nova parte de "Contato" da página.

O resultado final com todos os estilos será o seguinte:

Figura 18.1: A seção de "Contato" pronta

Nesse exercício não se preocupe em deixar a página com o mesmo estilo acima. Antes de mais nada,
escreva o conteúdo da página e depois escolha as tags mais semânticas que você lembrar para cada parte
do conteúdo.

O rodapé deve conter as seguintes informações:

Uma seção com título "Correspondência" contendo:
- o horário para recebimento de correspondências
- um endereço para correspondência com:

   - Nome da empresa
   - Rua, núemro e andar
   - Bairro
   - Cidade - estado

Uma seção com título "Telefones" contendo:
- o horário para recebimento de ligações
- Telefone de Pessoa Física
- Telefone de Pessoa Jurídica

O conteúdo de texto está pronto em **"textos/sobre.txt"**

Ao final ainda não teremos os estilos como queremos, porém escolhendo as tags que trazem uma
semântica legal teremos o seguinte resultado:

# EXERCÍCIO: SEMANTICA EM PRIMEIRO
# LUGAR

## 18.1 OBJETIVO

**74** 
18 EXERCÍCIO: SEMANTICA EM PRIMEIRO LUGAR


--------------------------------------------------

Figura 18.2: A seção de "Contato" apenas com o estilo padrão das tags

Editoras tradicionais pouco ligam para ebooks e novas tecnologias. Não dominam
tecnicamente o assunto para revisar os livros a fundo. Não têm anos de
experiência em didáticas com cursos.
Conheça a **Casa do Código**, uma editora diferente, com curadoria da **Caelum** e
obsessão por livros de qualidade a preços justos.

Casa do Código, ebook com preço de ebook.

1. No arquivo ** sobre.html **na pasta ** raíz do projeto **faça as seguintes alterações:

 *<!doctype html>*
 <html lang="pt-BR">
   <head>
     <meta charset="utf-8">
     <title>
       MusicDot | Sobre a empresa
     </title>
     <link href="img/favicon.ico" rel="icon">
     <link rel="stylesheet" href="css/sobre.css">
   </head>

   <body>

**Editora Casa do Código com livros de uma forma diferente**

## 18.2 PASSO A PASSO COM CÓDIGO

**# sobre.html**

18.2 PASSO A PASSO COM CÓDIGO 
**75**


--------------------------------------------------

     <img src="img/logo.svg" alt="MusicDot">

     <h1 class="titulo"> Sobre a empresa </h1>

     <p>
       A MusicDot é a maior escola online de música em todo o mundo.
       Fundada em 1932, possui estúdios em 124 países, sendo líder de mercado com mais de 90% de
       participação em 118 deles.
     </p>

     <p>
       Nossa matriz fica em <a href="https://maps.google.com.br/?q=190,GabrielDequech,Mafra,SC"> 
Mafra, em Santa Catarina </a>. De lá, saem grande parte das gravações de nossos cursos. Nossa matr
iz:

     </p>

     <figure class="matriz-musicdot">
       <img src="img/matriz-musicdot.png" alt="Matriz da musicdot">
       <figcaption>
           Matriz MusicDot 
       </figcaption>
     </figure>

     <p>
       Assine os cursos da MusicDot. Acesse <a href="index.html"> nosso site </a> ou entre em con
tato

       se tiver dúvidas. Conheça também <a href="#historia"> nossa história </a> e <a href="#dife
renciais"> nossos diferenciais </a>.

     </p>

     <h2 id="historia" class="subtitulo"> História </h2>

     <figure class="familia-tupfeln">
       <img src="img/familia-tupfeln.jpg" alt="Foto da família tüpfeln">
       <figcaption>Família Tüpfeln</figcaption>
     </figure>

     <p>
       A fundação em 1932 ocorreu no momento da descoberta econônica de cursos por stream online 
no interior de Santa Catarina. A

       família Tüpfeln, tradicional da região, investiu todas as suas economias nessa nova inicia
tiva,

       revolucionária para a época. A fundadora frau Dagmar Olaf Tüpfeln, dotada de particular vi
são

       administrativa, guiou os negócios da empresa durante mais de 50 anos, muitos deles ao lado
       de seu filho Ernst Noten Tüpfeln, atual CEO. O nome da empresa é inspirado no nome da famí
lia.

     </p>

     <p>
       O crescimento da empresa foi praticamente instantâneo. Nos primeiros 5 anos, já atendia 18
países.
       Bateu a marca de 100 países em apenas 15 anos de existência. Até hoje, já atendeu 2 bilhõe
s

       de usuários diferentes, em bilhões de diferentes pedidos.
     </p>

     <p>
       O crescimento em número de funcionários é também assombroso. Hoje, é a maior empregadora d
o

       Brasil, mas mesmo após apenas 5 anos de sua existência, já possuía 30 mil funcionários. Fo
ra do

**76** 
18.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

       Brasil, há 240 mil funcionários, além dos 890 mil brasileiros nas instalações de Mafra e
       nos escritórios em todo país.
     </p>

     <p>
       Dada a importância econômica da empresa para o Brasil, a família Tüpfeln já recebeu divers
os prêmios,

       homenagens e condecorações. Todos os presidentes do Brasil já visitaram as instalações da 
MusicDot, além de presidentes da União Européia, Ásia e o secretário-geral da ONU.

     </p>

     <h2 id="diferenciais" class="subtitulo"> Diferenciais </h2>
     <ul>
       <li> Menor preço do mercado, garantido </li>
       <li> Se você achar um serviço mais barato, leva 1 mês de graça </li>
       <li> Pague em reais, dólares, euros, libras, dodgecoins, litecoins ou bitcoins </li>
       <li> Todas as compras acompanham acesso à Alura </li>
       <li> Maior escola de música online do mundo </li>
       <li> Atendimento via telefone, email, chat, twitter, facebook, instagram, ICQ, WhatsApp, S
MS, carta, fax, sinal de fumaça e telegrama </li>

       <li> Presente em 124 países </li>
       <li> Mais de um milhão de funcionários em todo o mundo </li>
     </ul>

     <h2 class="titulo"> Contato </h2>

+    <h3> Correspondência </h3>
+    <small> (todos os dias, das 9h às 18h) </small>
+
+    <address>
+        AOVS Sistemas de Informática S.A
+        <br>
+        Rua Vergueiro, 3185, 8º andar
+        <br>
+        Vila Mariana
+        <br>
+        São Paulo - SP
+    </address>
+
+    <h3> Telefones </h3>
+    <small> (segunda à sexta, das 9h às 18h) </small>
+    
+    <dl>
+      <dt> Pessoa Física: </dt>
+      <dd> <a href="tel://114118-3319"> (11) 4118-3319 </a> </dd>
+      
+      <dt> Pessoa Jurídica: </dt>
+      <dd> <a href="tel://114118-2172"> (11) 4118-2172 </a> </dd>
+    </dl>
+
   </body>
 </html>

18.2 PASSO A PASSO COM CÓDIGO 
**77**


--------------------------------------------------

CAPÍTULO 19

Vimos já o conceito de desacoplar estilos usando classes e os benefícios que isso nos traz, mas para cada

elemento que nós vamos estilizar precisamos pensar em um nome diferente e isso pode ficar muito
complicado sem um padrão para seguir.

Existem vários padrões de CSS mas durante o curso vamos usar um chamado ***BEMCSS***. A
vantagem de se usar ***BEMCSS*** para quem está começando com desenvolvimento HTML e CSS é que
ele é um padrão que foca bastante em estrutura e facilita bastante na hora planejar os nomes das classes.

**BEM** usa um conceito de  bloco__elemento--modificador  para nomear suas classes, sendo que

bloco  é o elemento html que representa uma divisão de conteúdo cuja sua existência já tenha um

sentido por si só,  elemento  representa uma parte semântica do  bloco  e  modificador  é uma

sinalização de *comportamento* ou *estilização*.

As divisões entre  bloco__elemento--modificador  são chamados de: double  snake__case  e

double  kebab--case . Quando queremos uma divisão como o *espaço* usamos ou  kebab-case ou

o  camelCase .  Kebab-case é o mais comum para HTML e CSS e  camelCase é mais comum em

JavaScript.

Vamos ver como que **BEM** funciona com o exemplo abaixo:

<!-- section representa um painel (por exemplo) de produtos. Mas não de qualquer produto, mas sim de 
produtos mais vendidos -->
<section class="produtos produtos--mais-vendidos"> 

   <!-- O h2 representa o título desse painel -->
   <h2 class="produtos__titulo">Produtos mais vendidos</h2>
   <ul class="produtos__lista">
       <!-- li representa o produto em sí -->
       <li class="produtos__produto">
           <figure>
               <img src="img/produto1.png" alt="Foto do Produto 1">
               <figcaption>Foto do produto 1</figcaption>
           </figure>
       </li>
       <!-- li representa o produto em sí, mas nesse caso também temos um produto destaque -->
       <li class="produtos__produto produtos__produto--destaque">
           <figure>
               <img src="img/produto-destaque.png" alt="Foto do Produto em Destaque">

# CONHECENDO PADRÕES DE CSS

**78** 
19 CONHECENDO PADRÕES DE CSS


--------------------------------------------------

               <figcaption>Foto do produto em destaque</figcaption>
           </figure>
       </li>
       <li class="produtos__produto">
           <figure>
               <img src="img/produto3.png" alt="Foto do Produto 3">
               <figcaption>Foto do produto 3</figcaption>
           </figure>
       </li>
       <li class="produtos__produto">
           <figure>
               <img src="img/produto4.png" alt="Foto do Produto 4">
               <figcaption>Foto do produto 4</figcaption>
           </figure>
       </li>
   </ul>
</section>

Da maneira que montamos a estrutura acima fica bem fácil saber o que estamos estilizando no CSS.
Veja a diferença:

section h2 { /* É o h2 da section que tem os produtos? E se precisar mudar minha estrutura para um h3
? */

   font-size: 40px;
   font-weight: 800;
}

.produtos__titulo { /* Agora aqui eu sei que vou estilizar o título do painel de produtos. Mesmo se m
udar para um h3 */

   font-size: 40px;
   font-weight: 800;
}

Existem 2 tipos de display que caracterizam a exibição padrão da maior parte dos elementos HTML:

display: block e  display: inline . A maneira mais fácil de ver a diferença entre eles é usando as

tags que possuem essas propriedades por padrão,  <p>  e  <a>  respectivamente, e colocar uma cor de

fundo.

**HTML:**

<p>Um parágrafo que é block</p>
<a>Um link que é inline</a>

**CSS:**

p {

   background-color: blue;   
}

a {

   background-color: red;
}

Veja o espaço que esses elementos realmente ocupam. A tag  <p>  ocupa toda a largura da página

## 19.1 TIPOS DE DISPLAY

19.1 TIPOS DE DISPLAY 
**79**


--------------------------------------------------

enquanto a tag  <a>  ocupa apenas o espaço necessário para mostrar o texto que colocamos. Vamos

colocar mais elementos no nosso exemplo acima.

**HTML:**

<p>Um parágrafo que é block</p>
<p>Mais um parágrafo que é block</p>
<a>Um link que é inline</a>
<a>Mais um link que é inline</a>

**CSS:**

p {

   background-color: blue;   
}

a {

   background-color: red;
}

Podemos observar que agora um parágrafo ficou um embaixo do outro e os links ficaram um do lado
do outro. Esses comportamentos são os esperados de elementos  block e  inline . Como um elemento

block ocupa toda a largura da tela não podemos colocar outro elemento do lado porque não há espaço.

Agora como no  inline  o elemento ocupa só o espaço necessário para mostrar nosso texto então

podemos colocar outros elementos que caibam naquele espaço. Bom, vamos então resolver o problema
de espaço da tag  <p> :

**HTML:**

<p>Um parágrafo que é block</p>
<p>Mais um parágrafo que é block</p>
<a>Um link que é inline</a>
<a>Mais um link que é inline</a>

**CSS:**

p {

   background-color: blue;
   width: 30%;  
}

a {

   background-color: red;
   width: 60%;
}

Bom, agora temos dois problemas. Mesmo com o espaço extra os parágrafos não ficaram um do lado
do outro e nossos links não tiveram alterações em suas larguras. Vamos usar o inspetor de elementos de

nosso navegador para ver o que está acontecendo com esses elementos.

Selecionando a tag  <p>  com nosso inspetor conseguimos ver que ela realmente está ocupando

30% do espaço da tela do navegador, mas agora tem alguma coisa a mais que não colocamos no CSS.

**80** 
19.1 TIPOS DE DISPLAY


--------------------------------------------------

**Margin**. Existe uma  margin ocupando o restante do espaço que era ocupado pela tag  <p> . Utilizando

a propriedade  margin-right: 0px;  não parece fazer efeito. Mas está tudo bem! Esse é o

comportamento esperado de um elemento  block .

Vamos ver agora o que aconteceu com nossos links. Nossos links parecem ter ignorado

completamente a propriedade de largura que colocamos. Mais uma vez, está tudo bem! Esse é o
comportamento padrão de um elemento  inline . Diferente de um elemento  block , um elemento

inline não recebe propriedades de tamanho ( width e  height ) e isso pode gerar alguns problemas

com estilização. Foi criado então o  display: inline-block  que permite usar o melhor dos dois

mundos. Vamos usar o exemplo acima novamente só que mudando o tipo de display do link:

**HTML:**

<p>Um parágrafo que é block</p>
<p>Mais um parágrafo que é block</p>
<a>Um link que é inline</a>
<a>Mais um link que é inline</a>

**CSS:**

p {

   background-color: blue;
   width: 30%;  
}

a {

   background-color: red;
   width: 60%;
   display: inline-block;
}

Perfeito! Agora nosso link recebeu o tamanho que colocamos e agora deixamos um  <a> debaixo do

outro. Se mudarmos o tamanho dessa tag  <a> para um tamanho de  40% , por exemplo, vemos que as

nossas tags  <a> ficam uma do lado da outra.

Em resumo então dos displays:

 display: block :

O elemento ocupa toda a largura disponível

Se diminuir o tamanho desse elemento o espaço restante será ocupado por uma  margin  não

removível

 display: inline :

Permite que outro elemento fique do seu lado caso haja espaço

O elemento ocupa apenas o espaço para mostrar seu conteúdo

Não recebe propriedades de tamanho

19.1 TIPOS DE DISPLAY 
**81**


--------------------------------------------------

 display: inline-block :

Permite que outro elemento fique do seu lado caso haja espaço

O elemento inicialmente ocupa apenas o espaço para mostrar seu conteúdo
Recebe propriedades de tamanho

O ideal é nunca limitar nossas opções quando vamos escolher uma propriedade. Se o único propósito

de mudarmos o  display  de um elemento é para deixá-lo um do lado do outro, vamos usar  inline-

block . Se por algum motivo houver necessidade de mudar o tamanho desse elemento, já estamos com o

display correto e não precisaremos mudá-lo de novo.

A **Alura** oferece centenas de **cursos online** em sua plataforma exclusiva de
ensino que favorece o aprendizado com a **qualidade** reconhecida da Caelum.
Você pode escolher um curso nas áreas de Programação, Front-end, Mobile,

Design & UX, Infra, Business, entre outras, com um plano que dá acesso a todos os cursos. Ex-
estudante da Caelum tem 10% de desconto neste link!

Conheça os cursos online Alura.

**### Quando devo usar **** inline ****###  ou **** inline-block ****### ?**

**Já conhece os cursos online Alura?**

**82** 
19.1 TIPOS DE DISPLAY


--------------------------------------------------

CAPÍTULO 20

Usando a nova nomenclatura e padrão de classes de CSS, coloque os devidos nomes nas tags que

colocamos no exercício anterior. Depois utilize essas classes novas para colocar os subtítulos do rodapé
na mesma linha que as tags  <small> . Em seguida arrume os espaçamentos das informações dentro do

rodapé.

Querendo aprender ainda mais sobre? Esclarecer dúvidas dos exercícios? Ouvir
explicações detalhadas com um instrutor?
A Caelum oferece o **curso data** presencial nas cidades de São Paulo, Rio de

Janeiro e Brasília, além de turmas incompany.

Consulte as vantagens do curso *Desenvolvimento Web com HTML, CSS e*

*JavaScript*

1. No arquivo ** sobre.css **na pasta ** css **faça as seguintes alterações:

 body {
   width: 940px;
   margin-left: auto;
   margin-right: auto;

   font-family: "Helvetica", "Lucida Grande", sans-serif;
   color: #3D3D3D;
 }

# EXERCÍCIO: TREINANDO DISPLAY E
# NOMENCLATURA DE CLASSES

## 20.1 OBJETIVO

**Você pode também fazer o curso data dessa apostila na Caelum**

## 20.2 PASSO A PASSO COM CÓDIGO

**# css/sobre.css**

20 EXERCÍCIO: TREINANDO DISPLAY E NOMENCLATURA DE CLASSES 
**83**


--------------------------------------------------

 .titulo {
   padding: 10px;

   font-size: 32px;

   background-color: #E1EDF2;
 }

 .subtitulo {
   border-bottom: 2px solid black;
 }

 figure {
   margin: 30px;
   padding: 15px;

   text-align: center;

   background-color: whitesmoke;
   border: 1px solid lightgrey;
 }

 figcaption {
   margin-top: 10px;
 }

 .matriz-musicdot {
   width: 550px;
   margin-left: auto;
   margin-right: auto;
 }

 .familia-tupfeln {
   width: 275px;
   float: right;
 }

 figure img {
   width: 100%;
 }
+
+.contato__subtitulo {
+  display: inline;
+}
+
+.contato__info {
+  margin: 16px 0 24px;
+  padding-left: 32px;
+}

2. No arquivo ** sobre.html **na pasta ** raíz do projeto **faça as seguintes alterações:

 *<!doctype html>*
 <html lang="pt-BR">
   <head>
     <meta charset="utf-8">
     <title>
       MusicDot | Sobre a empresa
     </title>

**# sobre.html**

**84** 
20.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

     <link href="img/favicon.ico" rel="icon">
     <link rel="stylesheet" href="css/sobre.css">
   </head>

   <body>

     <img src="img/logo.svg" alt="MusicDot">

     <h1 class="titulo"> Sobre a empresa </h1>

     <p>
       A MusicDot é a maior escola online de música em todo o mundo.
       Fundada em 1932, possui estúdios em 124 países, sendo líder de mercado com mais de 90% de
       participação em 118 deles.
     </p>

     <p>
       Nossa matriz fica em <a href="https://maps.google.com.br/?q=190,GabrielDequech,Mafra,SC"> 
Mafra, em Santa Catarina </a>. De lá, saem grande parte das gravações de nossos cursos. Nossa matr
iz:

     </p>

     <figure class="matriz-musicdot">
       <img src="img/matriz-musicdot.png" alt="Matriz da musicdot">
       <figcaption>
           Matriz MusicDot 
       </figcaption>
     </figure>

     <p>
       Assine os cursos da MusicDot. Acesse <a href="index.html"> nosso site </a> ou entre em con
tato

       se tiver dúvidas. Conheça também <a href="#historia"> nossa história </a> e <a href="#dife
renciais"> nossos diferenciais </a>.

     </p>

     <h2 id="historia" class="subtitulo"> História </h2>

     <figure class="familia-tupfeln">
       <img src="img/familia-tupfeln.jpg" alt="Foto da família tüpfeln">
       <figcaption>Família Tüpfeln</figcaption>
     </figure>

     <p>
       A fundação em 1932 ocorreu no momento da descoberta econônica de cursos por stream online 
no interior de Santa Catarina. A

       família Tüpfeln, tradicional da região, investiu todas as suas economias nessa nova inicia
tiva,

       revolucionária para a época. A fundadora frau Dagmar Olaf Tüpfeln, dotada de particular vi
são

       administrativa, guiou os negócios da empresa durante mais de 50 anos, muitos deles ao lado
       de seu filho Ernst Noten Tüpfeln, atual CEO. O nome da empresa é inspirado no nome da famí
lia.

     </p>

     <p>
       O crescimento da empresa foi praticamente instantâneo. Nos primeiros 5 anos, já atendia 18
países.
       Bateu a marca de 100 países em apenas 15 anos de existência. Até hoje, já atendeu 2 bilhõe
s

       de usuários diferentes, em bilhões de diferentes pedidos.
     </p>

20.2 PASSO A PASSO COM CÓDIGO 
**85**


--------------------------------------------------

     <p>
       O crescimento em número de funcionários é também assombroso. Hoje, é a maior empregadora d
o

       Brasil, mas mesmo após apenas 5 anos de sua existência, já possuía 30 mil funcionários. Fo
ra do

       Brasil, há 240 mil funcionários, além dos 890 mil brasileiros nas instalações de Mafra e
       nos escritórios em todo país.
     </p>

     <p>
       Dada a importância econômica da empresa para o Brasil, a família Tüpfeln já recebeu divers
os prêmios,

       homenagens e condecorações. Todos os presidentes do Brasil já visitaram as instalações da 
MusicDot, além de presidentes da União Européia, Ásia e o secretário-geral da ONU.

     </p>

     <h2 id="diferenciais" class="subtitulo"> Diferenciais </h2>
     <ul>
       <li> Menor preço do mercado, garantido </li>
       <li> Se você achar um serviço mais barato, leva 1 mês de graça </li>
       <li> Pague em reais, dólares, euros, libras, dodgecoins, litecoins ou bitcoins </li>
       <li> Todas as compras acompanham acesso à Alura </li>
       <li> Maior escola de música online do mundo </li>
       <li> Atendimento via telefone, email, chat, twitter, facebook, instagram, ICQ, WhatsApp, S
MS, carta, fax, sinal de fumaça e telegrama </li>

       <li> Presente em 124 países </li>
       <li> Mais de um milhão de funcionários em todo o mundo </li>
     </ul>

     <h2 class="titulo"> Contato </h2>

-    <̶h̶3̶>̶ C̶o̶r̶r̶e̶s̶p̶o̶n̶d̶ê̶n̶c̶i̶a̶ </̶h̶3̶>
+    <h3 class="contato__subtitulo"> Correspondência </h3>
     <small> (todos os dias, das 9h às 18h) </small>

-    <̶a̶d̶d̶r̶e̶s̶s̶>
+    <address class="contato__info">
         AOVS Sistemas de Informática S.A
         <br>
         Rua Vergueiro, 3185, 8º andar
         <br>
         Vila Mariana
         <br>
         São Paulo - SP
     </address>

-    <̶h̶3̶>̶ T̶e̶l̶e̶f̶o̶n̶e̶s̶ </̶h̶3̶>
+    <h3 class="contato__subtitulo"> Telefones </h3>
     <small> (segunda à sexta, das 9h às 18h) </small>

-    <̶d̶l̶>
+    <dl class="contato__info">
       <dt> Pessoa Física: </dt>
       <dd> <a href="tel://114118-3319"> (11) 4118-3319 </a> </dd>

       <dt> Pessoa Jurídica: </dt>
       <dd> <a href="tel://114118-2172"> (11) 4118-2172 </a> </dd>
     </dl>

   </body>
 </html>

**86** 
20.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

CAPÍTULO 21

Primeiro vamos criar as classes que serão utilizadas no CSS para estilizar as informações de telefones.

Precisamos deixar ambas as informações na mesma linha: Ex:  Pessoa Física: (11) 4118-3319 

Conheça a **Casa do Código**, uma **nova** editora, com autores de destaque no
mercado, foco em **ebooks** (PDF, epub, mobi), preços **imbatíveis** e assuntos

**atuais**.
Com a curadoria da **Caelum** e excelentes autores, é uma abordagem **diferente**
para livros de tecnologia no Brasil.

Casa do Código, Livros de Tecnologia.

1. No arquivo ** sobre.css **na pasta ** css **faça as seguintes alterações:

 body {
   width: 940px;
   margin-left: auto;
   margin-right: auto;

   font-family: "Helvetica", "Lucida Grande", sans-serif;
   color: #3D3D3D;
 }

 .titulo {
   padding: 10px;

# EXERCÍCIO: UM POUCO SOBRE
# ESTILIZAÇÃO COM BLOCOS

## 21.1 OBJETIVO

**Seus livros de tecnologia parecem do século passado?**

## 21.2 PASSO A PASSO COM CÓDIGO

**# css/sobre.css**

21 EXERCÍCIO: UM POUCO SOBRE ESTILIZAÇÃO COM BLOCOS 
**87**


--------------------------------------------------

   font-size: 32px;

   background-color: #E1EDF2;
 }

 .subtitulo {
   border-bottom: 2px solid black;
 }

 figure {
   margin: 30px;
   padding: 15px;

   text-align: center;

   background-color: whitesmoke;
   border: 1px solid lightgrey;
 }

 figcaption {
   margin-top: 10px;
 }

 .matriz-musicdot {
   width: 550px;
   margin-left: auto;
   margin-right: auto;
 }

 .familia-tupfeln {
   width: 275px;
   float: right;
 }

 figure img {
   width: 100%;
 }

 .contato__subtitulo {
   display: inline;
 }

 .contato__info {
   margin: 16px 0 24px;
   padding-left: 32px;
 }
+
+.contato__info-titulo,
+.contato__info-descricao {
+  display: inline;
+}
+
+.contato__info-descricao {
+  margin-left: 10px;
+}

2. No arquivo ** sobre.html **na pasta ** raíz do projeto **faça as seguintes alterações:

 *<!doctype html>*

**# sobre.html**

**88** 
21.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

 <html lang="pt-BR">
   <head>
     <meta charset="utf-8">
     <title>
       MusicDot | Sobre a empresa
     </title>
     <link href="img/favicon.ico" rel="icon">
     <link rel="stylesheet" href="css/sobre.css">
   </head>

   <body>

     <img src="img/logo.svg" alt="MusicDot">

     <h1 class="titulo"> Sobre a empresa </h1>

     <p>
       A MusicDot é a maior escola online de música em todo o mundo.
       Fundada em 1932, possui estúdios em 124 países, sendo líder de mercado com mais de 90% de
       participação em 118 deles.
     </p>

     <p>
       Nossa matriz fica em <a href="https://maps.google.com.br/?q=190,GabrielDequech,Mafra,SC"> 
Mafra, em Santa Catarina </a>. De lá, saem grande parte das gravações de nossos cursos. Nossa matr
iz:

     </p>

     <figure class="matriz-musicdot">
       <img src="img/matriz-musicdot.png" alt="Matriz da musicdot">
       <figcaption>
           Matriz MusicDot 
       </figcaption>
     </figure>

     <p>
       Assine os cursos da MusicDot. Acesse <a href="index.html"> nosso site </a> ou entre em con
tato

       se tiver dúvidas. Conheça também <a href="#historia"> nossa história </a> e <a href="#dife
renciais"> nossos diferenciais </a>.

     </p>

     <h2 id="historia" class="subtitulo"> História </h2>

     <figure class="familia-tupfeln">
       <img src="img/familia-tupfeln.jpg" alt="Foto da família tüpfeln">
       <figcaption>Família Tüpfeln</figcaption>
     </figure>

     <p>
       A fundação em 1932 ocorreu no momento da descoberta econônica de cursos por stream online 
no interior de Santa Catarina. A

       família Tüpfeln, tradicional da região, investiu todas as suas economias nessa nova inicia
tiva,

       revolucionária para a época. A fundadora frau Dagmar Olaf Tüpfeln, dotada de particular vi
são

       administrativa, guiou os negócios da empresa durante mais de 50 anos, muitos deles ao lado
       de seu filho Ernst Noten Tüpfeln, atual CEO. O nome da empresa é inspirado no nome da famí
lia.

     </p>

     <p>
       O crescimento da empresa foi praticamente instantâneo. Nos primeiros 5 anos, já atendia 18

21.2 PASSO A PASSO COM CÓDIGO 
**89**


--------------------------------------------------

países.
       Bateu a marca de 100 países em apenas 15 anos de existência. Até hoje, já atendeu 2 bilhõe
s

       de usuários diferentes, em bilhões de diferentes pedidos.
     </p>

     <p>
       O crescimento em número de funcionários é também assombroso. Hoje, é a maior empregadora d
o

       Brasil, mas mesmo após apenas 5 anos de sua existência, já possuía 30 mil funcionários. Fo
ra do

       Brasil, há 240 mil funcionários, além dos 890 mil brasileiros nas instalações de Mafra e
       nos escritórios em todo país.
     </p>

     <p>
       Dada a importância econômica da empresa para o Brasil, a família Tüpfeln já recebeu divers
os prêmios,

       homenagens e condecorações. Todos os presidentes do Brasil já visitaram as instalações da 
MusicDot, além de presidentes da União Européia, Ásia e o secretário-geral da ONU.

     </p>

     <h2 id="diferenciais" class="subtitulo"> Diferenciais </h2>
     <ul>
       <li> Menor preço do mercado, garantido </li>
       <li> Se você achar um serviço mais barato, leva 1 mês de graça </li>
       <li> Pague em reais, dólares, euros, libras, dodgecoins, litecoins ou bitcoins </li>
       <li> Todas as compras acompanham acesso à Alura </li>
       <li> Maior escola de música online do mundo </li>
       <li> Atendimento via telefone, email, chat, twitter, facebook, instagram, ICQ, WhatsApp, S
MS, carta, fax, sinal de fumaça e telegrama </li>

       <li> Presente em 124 países </li>
       <li> Mais de um milhão de funcionários em todo o mundo </li>
     </ul>

     <h2 class="titulo"> Contato </h2>

     <h3 class="contato__subtitulo"> Correspondência </h3>
     <small> (todos os dias, das 9h às 18h) </small>

     <address class="contato__info">
         AOVS Sistemas de Informática S.A
         <br>
         Rua Vergueiro, 3185, 8º andar
         <br>
         Vila Mariana
         <br>
         São Paulo - SP
     </address>

     <h3 class="contato__subtitulo"> Telefones </h3>
     <small> (segunda à sexta, das 9h às 18h) </small>

     <dl class="contato__info">
-      <̶d̶t̶>̶ P̶e̶s̶s̶o̶a̶ F̶í̶s̶i̶c̶a̶:̶ </̶d̶t̶>
-      <̶d̶d̶>̶ <̶a̶ h̶r̶e̶f̶=̶"̶t̶e̶l̶:̶/̶/̶1̶1̶4̶1̶1̶8̶-̶3̶3̶1̶9̶"̶>̶ (̶1̶1̶)̶ 4̶1̶1̶8̶-̶3̶3̶1̶9̶ </̶a̶>̶ </̶d̶d̶>
-    
-      <̶d̶t̶>̶ P̶e̶s̶s̶o̶a̶ J̶u̶r̶í̶d̶i̶c̶a̶:̶ </̶d̶t̶>
-      <̶d̶d̶>̶ <̶a̶ h̶r̶e̶f̶=̶"̶t̶e̶l̶:̶/̶/̶1̶1̶4̶1̶1̶8̶-̶2̶1̶7̶2̶"̶>̶ (̶1̶1̶)̶ 4̶1̶1̶8̶-̶2̶1̶7̶2̶ </̶a̶>̶ </̶d̶d̶>
+      <div>
+        <dt class="contato__info-titulo"> Pessoa Física: </dt>
+        <dd class="contato__info-descricao"> <a href="tel://114118-3319"> (11) 4118-3319 </a> </
dd>

**90** 
21.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

+      </div>
+    
+      <div>
+        <dt class="contato__info-titulo"> Pessoa Jurídica: </dt>
+        <dd class="contato__info-descricao"> <a href="tel://114118-2172"> (11) 4118-2172 </a> </
dd>

+      </div>
     </dl>

   </body>
 </html>

21.2 PASSO A PASSO COM CÓDIGO 
**91**


--------------------------------------------------

CAPÍTULO 22

Precisamos agora que os blocos que criamos no exercício passado fiquem um do lado do outro, mas

dessa vez precisamos que os conteúdos dos blocos sejam contidos no espaço do bloco. Também vamos
colocar um espaçamento entre os telefones e mudar o alinhamento vertical para deixar todo o conteúdo

no topo

Se você está gostando dessa apostila, certamente vai aproveitar os **cursos**
**online** que lançamos na plataforma **Alura**. Você estuda a qualquer momento

com a **qualidade** Caelum. Programação, Mobile, Design, Infra, Front-End e
Business, entre outros! Ex-estudante da Caelum tem 10% de desconto, siga o link!

Conheça a Alura Cursos Online.

1. No arquivo ** sobre.css **na pasta ** css **faça as seguintes alterações:

 body {
   width: 940px;
   margin-left: auto;
   margin-right: auto;

   font-family: "Helvetica", "Lucida Grande", sans-serif;
   color: #3D3D3D;
 }

 .titulo {
   padding: 10px;

   font-size: 32px;

# EXERCÍCIO: MODIFICADORES

## 22.1 OBJETIVO

**Agora é a melhor hora de aprender algo novo**

## 22.2 PASSO A PASSO COM CÓDIGO

**# css/sobre.css**

**92** 
22 EXERCÍCIO: MODIFICADORES


--------------------------------------------------

   background-color: #E1EDF2;
 }

 .subtitulo {
   border-bottom: 2px solid black;
 }

 figure {
   margin: 30px;
   padding: 15px;

   text-align: center;

   background-color: whitesmoke;
   border: 1px solid lightgrey;
 }

 figcaption {
   margin-top: 10px;
 }

 .matriz-musicdot {
   width: 550px;
   margin-left: auto;
   margin-right: auto;
 }

 .familia-tupfeln {
   width: 275px;
   float: right;
 }

 figure img {
   width: 100%;
 }

 .contato__subtitulo {
   display: inline;
 }

+.contato__secao {
+  display: inline-block;
+  vertical-align: top;
+  margin-left: 16px;
+}
+
+.contato__secao--telefone {
+  margin-left: 32px;
+}
+
 .contato__info {
   margin: 16px 0 24px;
   padding-left: 32px;
 }

 .contato__info-titulo,
 .contato__info-descricao {
   display: inline;
 }

 .contato__info-descricao {
   margin-left: 10px;

22.2 PASSO A PASSO COM CÓDIGO 
**93**


--------------------------------------------------

 }

2. No arquivo ** sobre.html **na pasta ** raíz do projeto **faça as seguintes alterações:

 *<!doctype html>*
 <html lang="pt-BR">
   <head>
     <meta charset="utf-8">
     <title>
       MusicDot | Sobre a empresa
     </title>
     <link href="img/favicon.ico" rel="icon">
     <link rel="stylesheet" href="css/sobre.css">
   </head>

   <body>

     <img src="img/logo.svg" alt="MusicDot">

     <h1 class="titulo"> Sobre a empresa </h1>

     <p>
       A MusicDot é a maior escola online de música em todo o mundo.
       Fundada em 1932, possui estúdios em 124 países, sendo líder de mercado com mais de 90% de
       participação em 118 deles.
     </p>

     <p>
       Nossa matriz fica em <a href="https://maps.google.com.br/?q=190,GabrielDequech,Mafra,SC"> 
Mafra, em Santa Catarina </a>. De lá, saem grande parte das gravações de nossos cursos. Nossa matr
iz:

     </p>

     <figure class="matriz-musicdot">
       <img src="img/matriz-musicdot.png" alt="Matriz da musicdot">
       <figcaption>
           Matriz MusicDot 
       </figcaption>
     </figure>

     <p>
       Assine os cursos da MusicDot. Acesse <a href="index.html"> nosso site </a> ou entre em con
tato

       se tiver dúvidas. Conheça também <a href="#historia"> nossa história </a> e <a href="#dife
renciais"> nossos diferenciais </a>.

     </p>

     <h2 id="historia" class="subtitulo"> História </h2>

     <figure class="familia-tupfeln">
       <img src="img/familia-tupfeln.jpg" alt="Foto da família tüpfeln">
       <figcaption>Família Tüpfeln</figcaption>
     </figure>

     <p>
       A fundação em 1932 ocorreu no momento da descoberta econônica de cursos por stream online 
no interior de Santa Catarina. A

       família Tüpfeln, tradicional da região, investiu todas as suas economias nessa nova inicia
tiva,

       revolucionária para a época. A fundadora frau Dagmar Olaf Tüpfeln, dotada de particular vi

**# sobre.html**

**94** 
22.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

são

       administrativa, guiou os negócios da empresa durante mais de 50 anos, muitos deles ao lado
       de seu filho Ernst Noten Tüpfeln, atual CEO. O nome da empresa é inspirado no nome da famí
lia.

     </p>

     <p>
       O crescimento da empresa foi praticamente instantâneo. Nos primeiros 5 anos, já atendia 18
países.
       Bateu a marca de 100 países em apenas 15 anos de existência. Até hoje, já atendeu 2 bilhõe
s

       de usuários diferentes, em bilhões de diferentes pedidos.
     </p>

     <p>
       O crescimento em número de funcionários é também assombroso. Hoje, é a maior empregadora d
o

       Brasil, mas mesmo após apenas 5 anos de sua existência, já possuía 30 mil funcionários. Fo
ra do

       Brasil, há 240 mil funcionários, além dos 890 mil brasileiros nas instalações de Mafra e
       nos escritórios em todo país.
     </p>

     <p>
       Dada a importância econômica da empresa para o Brasil, a família Tüpfeln já recebeu divers
os prêmios,

       homenagens e condecorações. Todos os presidentes do Brasil já visitaram as instalações da 
MusicDot, além de presidentes da União Européia, Ásia e o secretário-geral da ONU.

     </p>

     <h2 id="diferenciais" class="subtitulo"> Diferenciais </h2>
     <ul>
       <li> Menor preço do mercado, garantido </li>
       <li> Se você achar um serviço mais barato, leva 1 mês de graça </li>
       <li> Pague em reais, dólares, euros, libras, dodgecoins, litecoins ou bitcoins </li>
       <li> Todas as compras acompanham acesso à Alura </li>
       <li> Maior escola de música online do mundo </li>
       <li> Atendimento via telefone, email, chat, twitter, facebook, instagram, ICQ, WhatsApp, S
MS, carta, fax, sinal de fumaça e telegrama </li>

       <li> Presente em 124 países </li>
       <li> Mais de um milhão de funcionários em todo o mundo </li>
     </ul>

     <h2 class="titulo"> Contato </h2>

+    <div class="contato__secao">
       <h3 class="contato__subtitulo"> Correspondência </h3>
       <small> (todos os dias, das 9h às 18h) </small>

       <address class="contato__info">
           AOVS Sistemas de Informática S.A
           <br>
           Rua Vergueiro, 3185, 8º andar
           <br>
           Vila Mariana
           <br>
           São Paulo - SP
       </address>
+    </div>

+    <div class="contato__secao contato__secao--telefone">
       <h3 class="contato__subtitulo"> Telefones </h3>
       <small> (segunda à sexta, das 9h às 18h) </small>

22.2 PASSO A PASSO COM CÓDIGO 
**95**


--------------------------------------------------

       <dl class="contato__info">
         <div>
           <dt class="contato__info-titulo"> Pessoa Física: </dt>
           <dd class="contato__info-descricao"> <a href="tel://114118-3319"> (11) 4118-3319 </a> 
</dd>

         </div>

         <div>
           <dt class="contato__info-titulo"> Pessoa Jurídica: </dt>
           <dd class="contato__info-descricao"> <a href="tel://114118-2172"> (11) 4118-2172 </a> 
</dd>

         </div>
       </dl>
+    </div>

   </body>
 </html>

**96** 
22.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

CAPÍTULO 23

Já vimos em exercícios passados o uso da unidade de medida relativa com  % . Usamos essa medida

relativa quando queremos que um elemento use, por exemplo,  100% do espaço disponível.

**HTML:**

<div>

   <img src="img/flor.png" alt="Foto de uma flor">
</div>

**CSS:**

div {

   width: 400px;
}

No exemplo acima, dependendo do tamanho da imagem, a imagem pode ultrapassar o espaço que
definimos para a  <div>  ou pode ocupar um espaço menor. Se queremos que a imagem ocupe todo o

espaço da  <div> podemos usar a unidade relativa  % :

div {

   width: 400px;
}

img {

   width: 100%; /* Ocupe 100% do espaço disponível */
}

A grande vantagem de se usar  % é que não importa o tamanho que colocamos na  <div> , a  <img> 

sempre vai acompanhar o tamanho da sua tag mãe (a  <div> ).

**EM** e **REM** tem o mesmo conceito de  %  mas ao invés de serem baseadas no tamanho de um

elemento, essas medidas são baseadas em tamanho de fonte. **EM** usa o tamanho da fonte do elemento
pai e **REM** usa o tamanho da fonte do  <html> .

**HTML:**

*<!DOCTYPE html>*
<html>
<head>

   <meta charset="UTF-8">
   <title>Um exemplo</title>
</head>
<body>

# UNIDADES RELATIVAS COM EM E REM

23 UNIDADES RELATIVAS COM EM E REM 
**97**


--------------------------------------------------

   <div>
       <img src="img/foto" alt="Uma foto">
   </div>
</body>
</html>

**CSS:**

html {

   font-size: 10px;
}

div {

   font-size: 20px;
}

img {

   width: 10em; /* A largura será de 200px */
   height: 10rem; /* A altura será de 100px */
}

A vantagem de usar essas medidas é que se tivermos outros elementos usando essas medidas e
precisarmos mudar o tamanho de todos os elementos proporcionalmente, basta mudarmos em um lugar
só. Estas unidades de medida são ideais para quando o site precisa ser exibido em diferentes tamanhos

de telas, onde em cada tamanho de tela a fonte deve ser exibida em escalas de tamanhos diferentes e
proporcionais entre si.

**98** 
23 UNIDADES RELATIVAS COM EM E REM


--------------------------------------------------

CAPÍTULO 24

Agora vamos mudar o tamanho da fonte para 16px da página e também a distância entre uma linha e

outra para 1.5.

No rodapé vamos colocar um espaçamento interno 75% maior do que a fonte da página em cima e
embaixo e 0 nos lados. Vamos colocar uma fonte que seja 10% maior do que a fonte da página.

Na logo do rodapé vamos definir uma largura de 6 vezes o tamanho da fonte da página

No elemento que contém o copyright vamos deixá-lo na mesma linha que a imagem e colocar um
espaçamento à sua esquerda de 1em

Editoras tradicionais pouco ligam para ebooks e novas tecnologias. Não dominam
tecnicamente o assunto para revisar os livros a fundo. Não têm anos de
experiência em didáticas com cursos.
Conheça a **Casa do Código**, uma editora diferente, com curadoria da **Caelum** e
obsessão por livros de qualidade a preços justos.

Casa do Código, ebook com preço de ebook.

1. No arquivo ** sobre.css **na pasta ** css **faça as seguintes alterações:

 body {

# EXERCÍCIO: MEDIDAS RELATIVAS EM E
# REM

## 24.1 OBJETIVO

**Editora Casa do Código com livros de uma forma diferente**

## 24.2 PASSO A PASSO COM CÓDIGO

**# css/sobre.css**

24 EXERCÍCIO: MEDIDAS RELATIVAS EM E REM 
**99**


--------------------------------------------------

   width: 940px;
   margin-left: auto;
   margin-right: auto;

+  font-size: 16px;
+  line-height: 1.5;
   font-family: "Helvetica", "Lucida Grande", sans-serif;
   color: #3D3D3D;
 }

 .titulo {
   padding: 10px;

   font-size: 32px;

   background-color: #E1EDF2;
 }

 .subtitulo {
   border-bottom: 2px solid black;
 }

 figure {
   margin: 30px;
   padding: 15px;

   text-align: center;

   background-color: whitesmoke;
   border: 1px solid lightgrey;
 }

 figcaption {
   margin-top: 10px;
 }

 .matriz-musicdot {
   width: 550px;
   margin-left: auto;
   margin-right: auto;
 }

 .familia-tupfeln {
   width: 275px;
   float: right;
 }

 figure img {
   width: 100%;
 }

 .contato__subtitulo {
   display: inline;
 }

 .contato__secao {
   display: inline-block;
   vertical-align: top;
   margin-left: 16px;
 }

 .contato__secao--telefone {
   margin-left: 32px;

**100** 
24.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

 }

 .contato__info {
   margin: 16px 0 24px;
   padding-left: 32px;
 }

 .contato__info-titulo,
 .contato__info-descricao {
   display: inline;
 }

 .contato__info-descricao {
   margin-left: 10px;
 }
+
+.rodape {
+  padding: 1.75em 0;
+
+  font-size: 1.1rem;
+}
+
+.rodape__logo {
+  width: 6em;
+}
+
+.rodape__copyright {
+  display: inline;
+  margin-left: 1em;
+}

2. No arquivo ** sobre.html **na pasta ** raíz do projeto **faça as seguintes alterações:

 *<!doctype html>*
 <html lang="pt-BR">
   <head>
     <meta charset="utf-8">
     <title>
       MusicDot | Sobre a empresa
     </title>
     <link href="img/favicon.ico" rel="icon">
     <link rel="stylesheet" href="css/sobre.css">
   </head>

   <body>

     <img src="img/logo.svg" alt="MusicDot">

     <h1 class="titulo"> Sobre a empresa </h1>

     <p>
       A MusicDot é a maior escola online de música em todo o mundo.
       Fundada em 1932, possui estúdios em 124 países, sendo líder de mercado com mais de 90% de
       participação em 118 deles.
     </p>

     <p>
       Nossa matriz fica em <a href="https://maps.google.com.br/?q=190,GabrielDequech,Mafra,SC"> 
Mafra, em Santa Catarina </a>. De lá, saem grande parte das gravações de nossos cursos. Nossa matr
iz:

**# sobre.html**

24.2 PASSO A PASSO COM CÓDIGO 
**101**


--------------------------------------------------

     </p>

     <figure class="matriz-musicdot">
       <img src="img/matriz-musicdot.png" alt="Matriz da musicdot">
       <figcaption>
           Matriz MusicDot 
       </figcaption>
     </figure>

     <p>
       Assine os cursos da MusicDot. Acesse <a href="index.html"> nosso site </a> ou entre em con
tato

       se tiver dúvidas. Conheça também <a href="#historia"> nossa história </a> e <a href="#dife
renciais"> nossos diferenciais </a>.

     </p>

     <h2 id="historia" class="subtitulo"> História </h2>

     <figure class="familia-tupfeln">
       <img src="img/familia-tupfeln.jpg" alt="Foto da família tüpfeln">
       <figcaption>Família Tüpfeln</figcaption>
     </figure>

     <p>
       A fundação em 1932 ocorreu no momento da descoberta econônica de cursos por stream online 
no interior de Santa Catarina. A

       família Tüpfeln, tradicional da região, investiu todas as suas economias nessa nova inicia
tiva,

       revolucionária para a época. A fundadora frau Dagmar Olaf Tüpfeln, dotada de particular vi
são

       administrativa, guiou os negócios da empresa durante mais de 50 anos, muitos deles ao lado
       de seu filho Ernst Noten Tüpfeln, atual CEO. O nome da empresa é inspirado no nome da famí
lia.

     </p>

     <p>
       O crescimento da empresa foi praticamente instantâneo. Nos primeiros 5 anos, já atendia 18
países.
       Bateu a marca de 100 países em apenas 15 anos de existência. Até hoje, já atendeu 2 bilhõe
s

       de usuários diferentes, em bilhões de diferentes pedidos.
     </p>

     <p>
       O crescimento em número de funcionários é também assombroso. Hoje, é a maior empregadora d
o

       Brasil, mas mesmo após apenas 5 anos de sua existência, já possuía 30 mil funcionários. Fo
ra do

       Brasil, há 240 mil funcionários, além dos 890 mil brasileiros nas instalações de Mafra e
       nos escritórios em todo país.
     </p>

     <p>
       Dada a importância econômica da empresa para o Brasil, a família Tüpfeln já recebeu divers
os prêmios,

       homenagens e condecorações. Todos os presidentes do Brasil já visitaram as instalações da 
MusicDot, além de presidentes da União Européia, Ásia e o secretário-geral da ONU.

     </p>

     <h2 id="diferenciais" class="subtitulo"> Diferenciais </h2>
     <ul>
       <li> Menor preço do mercado, garantido </li>
       <li> Se você achar um serviço mais barato, leva 1 mês de graça </li>

**102** 
24.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

       <li> Pague em reais, dólares, euros, libras, dodgecoins, litecoins ou bitcoins </li>
       <li> Todas as compras acompanham acesso à Alura </li>
       <li> Maior escola de música online do mundo </li>
       <li> Atendimento via telefone, email, chat, twitter, facebook, instagram, ICQ, WhatsApp, S
MS, carta, fax, sinal de fumaça e telegrama </li>

       <li> Presente em 124 países </li>
       <li> Mais de um milhão de funcionários em todo o mundo </li>
     </ul>

     <h2 class="titulo"> Contato </h2>

     <div class="contato__secao">
       <h3 class="contato__subtitulo"> Correspondência </h3>
       <small> (todos os dias, das 9h às 18h) </small>

       <address class="contato__info">
           AOVS Sistemas de Informática S.A
           <br>
           Rua Vergueiro, 3185, 8º andar
           <br>
           Vila Mariana
           <br>
           São Paulo - SP
       </address>
     </div>

     <div class="contato__secao contato__secao--telefone">
       <h3 class="contato__subtitulo"> Telefones </h3>
       <small> (segunda à sexta, das 9h às 18h) </small>

       <dl class="contato__info">
         <div>
           <dt class="contato__info-titulo"> Pessoa Física: </dt>
           <dd class="contato__info-descricao"> <a href="tel://114118-3319"> (11) 4118-3319 </a> 
</dd>

         </div>

         <div>
           <dt class="contato__info-titulo"> Pessoa Jurídica: </dt>
           <dd class="contato__info-descricao"> <a href="tel://114118-2172"> (11) 4118-2172 </a> 
</dd>

         </div>
       </dl>
     </div>

+    <footer class="rodape">
+      <img src="img/logo.svg" alt="Logo da musicdot" class="rodape__logo">
+      <p class="rodape__copyright"> &copy; Copyright MusicDot </p>
+    </footer>
+
   </body>
 </html>

24.2 PASSO A PASSO COM CÓDIGO 
**103**


--------------------------------------------------

CAPÍTULO 25

O volume de usuários que acessam a internet por meio de dispositivos móveis cresceu

exponencialmente nos últimos anos. Usuários de iPhones, iPads e outros smartphones e tablets têm
demandas diferentes dos usuários Desktop. Redes nem sempre rápidas e acessibilidade em dispositivos
limitados e multitoque são as principais diferenças.

Como atender a esses usuários?

Para que suportemos usuários móveis, antes de tudo, precisamos tomar uma decisão: fazer um site
exclusivo - e diferente - focado em dispositivos móveis ou adaptar nosso site para funcionar em

qualquer dispositivo?

Vários sites na internet adotam a estratégia de ter um site diferente voltado para dispositivos móveis
usando um subdomínio diferente como "m." ou "mobile.", como https://m.kabum.com.br.

Essa abordagem é a que traz maior facilidade na hora de pensar nas capacidades de cada plataforma,
Desktop e mobile, permitindo que entreguemos uma experiência customizada e otimizada para cada

situação. Porém, há diversos problemas envolvidos:

Como atender adequadamente diversos dispositivos tão diferentes quanto um smartphone com tela
pequena e um tablet com tela mediana? E se ainda considerarmos as SmartTVs, ChromeCast,
AppleTV? Teríamos que montar um site específico para cada tipo de plataforma?

Muitas vezes esses sites mobile são versões limitadas dos sites de verdade e não apenas ajustes de
usabilidade para o dispositivo diferente. Isso frustra o usuário que, cada vez mais, usa dispositivos

móveis para completar as mesmas tarefas que antes fazia no Desktop.

Dar manutenção em um site já é bastante trabalhoso, imagine dar manutenção em dois.

Você terá conteúdos duplicados entre sites "diferentes", podendo prejudicar seu SEO se não for
feito com cuidado.

Terá que lidar com redirects entre URLs móveis e normais, dependendo do dispositivo. O usuário
pode receber de um amigo um link para uma página vista no site normal, mas se ele abrir esse

email no celular, terá que ver a versão mobile desse link, sendo redirecionado automaticamente. E a
mesma coisa no sentido contrário, ao mandar um link de volta para o Desktop.

# SITE MOBILE OU MESMO SITE?

**104** 
25 SITE MOBILE OU MESMO SITE?


--------------------------------------------------

Uma abordagem que costumas ser muito utilizada é a de ter um único site, acessível em todos os
dispositivos móveis. Adeptos da ideia da Web única (**One Web**) consideram que o melhor para o
usuário é ter o mesmo site do Desktop normal também acessível no mundo móvel. É o melhor para o

desenvolvedor também, que não precisará manter vários sites diferentes. E é o que garante a
compatibilidade com a maior gama de aparelhos diferentes.

Certamente, a ideia não é fazer o usuário móvel acessar a página exatamente da mesma maneira que
o usuário Desktop. Usando truques de CSS3 bem suportados no mercado, podemos usar a mesma base

de layout e marcação porém ajustando o design para cada tipo de dispositivo.

Hoje em dia não existe tanto essa crença de que o site precisa ser exatamente a mesma experiência

do que no Desktop. Podemos criar experiências exclusivas para cada tipo de dispositivo, mas é
importante que o usuário ainda consiga fazer as funções (por exemplo realizar uma compra).

**Como desenvolver um site exclusivo para Mobile?**

Do ponto de vista de código, é a abordagem mais simples: basta fazer sua página com design
mais enxuto e levando em conta que a tela será pequena (em geral, usa-se width de 100% para que
se adapte à pequenas variações de tamanhos de telas entre smartphones diferentes).

Uma dificuldade estará no servidor para detectar se o usuário está vindo de um dispositivo

móvel ou não, e redirecioná-lo para o lugar certo. Isso costuma envolver código no servidor que
detecte o navegador do usuário usando o User-Agent do navegador.

É uma boa prática também incluir um link para a versão normal do site caso o usuário não
queira a versão móvel.

Desde a época do CSS2, há uma preocupação com o suporte de regras de layout diferentes para cada
situação possível. Isso é feito usando os chamados *media types*, que podem ser declarados ao se invocar

um arquivo CSS:

<link rel="stylesheet" href="site.css" media="screen">
<link rel="stylesheet" href="print.css" media="print">
<link rel="stylesheet" href="handheld.css" media="handheld">

Outra forma de declarar os *media types* é separar as regras dentro do próprio arquivo CSS:

@media screen {

 body {
   background-color: blue;
   color: white;
 }

## 25.1 CSS MEDIA TYPES

25.1 CSS MEDIA TYPES 
**105**


--------------------------------------------------

}

@media print {

 body {
   background-color: white;
   color: black;
 }
}

O *media type screen* determina a visualização normal, na tela do Desktop. É muito comum também
termos um CSS com *media type print* com regras de impressão (por exemplo, retirar navegação,

formatar cores para serem mais adequadas para leitura em papel etc).

E havia também o *media type handheld*, voltado para dispositivos móveis. Com ele, conseguíamos
adaptar o site para os pequenos dispositivos como celulares WAP e palmtops.

O problema é que esse tipo *handheld* nasceu em uma época em que os celulares eram bem mais
simples do que hoje, e, portanto, costumavam ser usados para fazer páginas bem simples. Quando os

novos smartphones *touchscreen* começaram a surgir - em especial, o iPhone -, eles tinham capacidade
para abrir páginas completas e tão complexas quanto as do Desktop. Por isso, o iPhone e outros

celulares modernos ignoram as regras de *handheld* e se consideram, na verdade, *screen*.

Além disso, mesmo que *handheld* funcionasse nos smartphones, como trataríamos os diferentes

dispositivos de hoje em dia como tablets, televisões etc?

A solução veio com o CSS3 e seus *media queries*.

A **Alura** oferece centenas de **cursos online** em sua plataforma exclusiva de
ensino que favorece o aprendizado com a **qualidade** reconhecida da Caelum.

Você pode escolher um curso nas áreas de Programação, Front-end, Mobile,
Design & UX, Infra, Business, entre outras, com um plano que dá acesso a todos os cursos. Ex-

estudante da Caelum tem 10% de desconto neste link!

Conheça os cursos online Alura.

Todos os smartphones e navegadores modernos suportam uma nova forma de adaptar o CSS baseado
nas propriedades dos dispositivos, as **media queries** do CSS3.

**Já conhece os cursos online Alura?**

## 25.2 CSS3 MEDIA QUERIES

**106** 
25.2 CSS3 MEDIA QUERIES


--------------------------------------------------

Em vez de simplesmente falar que determinado CSS é para *handheld* em geral, nós podemos agora
indicar que determinadas regras do CSS devem ser vinculadas a propriedades do dispositivo como
tamanho da tela, orientação (landscape ou portrait) e até resolução em dpi.

<link rel="stylesheet" href="base.css" media="screen">
<link rel="stylesheet" href="mobile.css" media="(max-width: 480px)">

Outra forma de declarar os *media types* é separar as regras dentro do mesmo arquivo CSS:

@media screen {

 body {
   font-size: 16px;
 }
}

@media (max-width: 480px) {

 body {
   font-size: 12px;
 }
}

Repare como o atributo *media* agora pode receber expressões complexas. No caso, estamos
indicando que queremos que as telas com largura máxima de 480px tenham uma fonte de 12px.

Você pode testar isso apenas redimensionando seu próprio navegador Desktop para um tamanho
menor que 480px.

Mas, se você tentar rodar nosso exemplo anterior em um iPhone ou Android de verdade, verá que
ainda estamos vendo a versão Desktop da página. A regra do *max-width* parece ser ignorada!

Na verdade, a questão é que os smartphones modernos têm telas grandes e resoluções altas,
justamente para nos permitir ver sites complexos feitos para Desktop. A tela de um iPhone SE por

exemplo é 1280px por 720px. Celulares Android já chegam a 4K.

Ainda assim, a experiência desses celulares é bem diferente dos Desktops. 4K em uma tela de 4

polegadas é bem diferente de 4K em um notebook de 16 polegadas. A resolução muda. Celulares
costumam ter uma resolução em dpi bem maior que Desktops.

Como arrumar nossa página?

Os smartphones sabem que considerar a tela como 4K não ajudará o usuário a visualizar a página
otimizada para telas menores. Há então o conceito de *device-width* que, resumidamente, representa um

número em pixels que o fabricante do aparelho considera como mais próximo da sensação que o usuário
tem ao visualizar a tela.

Nos iPhones, por exemplo, o *device-width* é considerado como 370px, mesmo com a tela tendo uma
resolução bem mais alta.

## 25.3 VIEWPORT

25.3 VIEWPORT 
**107**


--------------------------------------------------

Por padrão, iPhones, Androids e afins costumam considerar o tamanho da tela visível, chamada de
*viewport* como grande o suficiente para comportar os sites Desktop normais. Por isso a nossa página foi
mostrada sem zoom como se estivéssemos no Desktop.

A Apple criou então uma solução que depois foi copiada pelos outros smartphones, que é configurar

o valor que julgarmos mais adequado para o *viewport*:

<meta name="viewport" content="width=370">

Isso faz com que a tela seja considerada com largura de 370px, fazendo com que nosso layout

mobile finalmente funcione e nossas *media queries* também.

Melhor ainda, podemos colocar o *viewport* com o valor  device-width  definido pelo fabricante,

dando mais flexibilidade com dispositivos diferentes com tamanhos diferentes:

<meta name="viewport" content="width=device-width">

Pequenas mudanças que fazemos usando  @media  tentando fazer a experiência do usuário em

diversos dispositivos mais atraente é o que o mercado chama de **Web Design Responsivo**. O termo

surgiu num famoso artigo de Ethan Marcotte e diz o seguinte:

São 3 os elementos de um design responsivo:

layout fluído usando medidas flexíveis, como porcentagens;
*media queries* para ajustes de design;

uso de imagens flexíveis.

A ideia do responsivo é que a página se **adapte a diferentes condições**, em especial a diferentes
resoluções. E, embora o uso de porcentagens exista há décadas na Web, foi a popularização das *media*
*queries* que permitiram layouts verdadeiramente adaptativos.

## 25.4 RESPONSIVE WEB DESIGN

**108** 
25.4 RESPONSIVE WEB DESIGN


--------------------------------------------------

Querendo aprender ainda mais sobre? Esclarecer dúvidas dos exercícios? Ouvir

explicações detalhadas com um instrutor?

A Caelum oferece o **curso data** presencial nas cidades de São Paulo, Rio de
Janeiro e Brasília, além de turmas incompany.

Consulte as vantagens do curso *Desenvolvimento Web com HTML, CSS e*
*JavaScript*

Nossos exercícios seguiram o processo que chamamos de *desktop-first*. Isso significa que tínhamos

nossa página montada para o layout Desktop e, num segundo momento, precisaremos codar a adaptação
a mobile.

Na prática, isso não é muito interessante porque precisamos **desfazer** algumas coisas do que
tínhamos feito no nosso layout para desktop: tiramos alguns posicionamentos e desfizemos diversos

ajustes na largura de elementos que já eram padrões deles.

É muito mais comum e recomendado o uso da prática inversa: o **Mobile-first**. Isto é, começar o

desenvolvimento pelo mobile e, depois, adicionar suporte a layouts desktop. No código, não há nenhum
segredo: vamos apenas usar mais *media queries* **min-width** ao invés de **max-width**, mais comum em

códigos desktop-first.

A grande mudança do mobile-first é que ela permite uma abordagem muito mais simples e evolutiva.

Inicia-se o desenvolvimento pela área mais simples e limitada, com mais restrições, o mobile. O uso da
tela pequena vai nos forçar a criar páginas mais simples, focadas e objetivas. Depois, a adaptação pra
Desktop com *media queries*, é apenas uma questão de readaptar o layout.

A abordagem desktop-first começa pelo ambiente mais livre e vai tentando cortar coisas quando
chega no mobile. Esse tipo de adaptação é, na prática, muito mais trabalhosa.

**Você pode também fazer o curso data dessa apostila na Caelum**

## 25.5 MOBILE-FIRST

25.5 MOBILE-FIRST 
**109**


--------------------------------------------------

CAPÍTULO 26

Modifique a largura do  body  para que ele utilize unidade de medida relativa de porcentagem, e

também coloque um tamanho máximo que o  body pode alcançar.

Deixe o  figure  ocupando máximo de espaço possível da página e também faça com que o

tamanho do figure seja todo o *box*.

Não esqueça de adicionar a meta tag  viewport 

Conheça a **Casa do Código**, uma **nova** editora, com autores de destaque no
mercado, foco em **ebooks** (PDF, epub, mobi), preços **imbatíveis** e assuntos
**atuais**.

Com a curadoria da **Caelum** e excelentes autores, é uma abordagem **diferente**
para livros de tecnologia no Brasil.

Casa do Código, Livros de Tecnologia.

1. No arquivo ** sobre.css **na pasta ** css **faça as seguintes alterações:

 body {
-  w̶i̶d̶t̶h̶:̶ 9̶4̶0̶p̶x̶;̶
+  width: 80%;
+  max-width: 940px;
   margin-left: auto;

# EXERCÍCIO: RESPONSIVIDADE COM
# VIEWPORT E UNIDADES RELATIVAS

## 26.1 OBJETIVO

**Seus livros de tecnologia parecem do século passado?**

## 26.2 PASSO A PASSO COM CÓDIGO

**# css/sobre.css**

**110** 
26 EXERCÍCIO: RESPONSIVIDADE COM VIEWPORT E UNIDADES RELATIVAS


--------------------------------------------------

   margin-right: auto;

   font-size: 16px;
   line-height: 1.5;
   font-family: "Helvetica", "Lucida Grande", sans-serif;
   color: #3D3D3D;
 }

 .titulo {
   padding: 10px;

   font-size: 32px;

   background-color: #E1EDF2;
 }

 .subtitulo {
   border-bottom: 2px solid black;
 }

 figure {
+  max-width: 100%;
+  box-sizing: border-box;
   margin: 30px;
   padding: 15px;

   text-align: center;

   background-color: whitesmoke;
   border: 1px solid lightgrey;
 }

 figcaption {
   margin-top: 10px;
 }

 .matriz-musicdot {
   width: 550px;
   margin-left: auto;
   margin-right: auto;
 }

 .familia-tupfeln {
   width: 275px;
   float: right;
 }

 figure img {
   width: 100%;
 }

 .contato__subtitulo {
   display: inline;
 }

 .contato__secao {
   display: inline-block;
   vertical-align: top;
   margin-left: 16px;
 }

 .contato__secao--telefone {
   margin-left: 32px;

26.2 PASSO A PASSO COM CÓDIGO 
**111**


--------------------------------------------------

 }

 .contato__info {
   margin: 16px 0 24px;
   padding-left: 32px;
 }

 .contato__info-titulo,
 .contato__info-descricao {
   display: inline;
 }

 .contato__info-descricao {
   margin-left: 10px;
 }

 .rodape {
   padding: 1.75em 0;

   font-size: 1.1rem;
 }

 .rodape__logo {
   width: 6em;
 }

 .rodape__copyright {
   display: inline;
   margin-left: 1em;
 }

2. No arquivo ** sobre.html **na pasta ** raíz do projeto **faça as seguintes alterações:

 *<!doctype html>*
 <html lang="pt-BR">
   <head>
     <meta charset="utf-8">
+    <meta name="viewport" content="width=device-width">
     <title>
       MusicDot | Sobre a empresa
     </title>
     <link href="img/favicon.ico" rel="icon">
     <link rel="stylesheet" href="css/sobre.css">
   </head>

   <body>

     <img src="img/logo.svg" alt="MusicDot">

     <h1 class="titulo"> Sobre a empresa </h1>

     <p>
       A MusicDot é a maior escola online de música em todo o mundo.
       Fundada em 1932, possui estúdios em 124 países, sendo líder de mercado com mais de 90% de
       participação em 118 deles.
     </p>

     <p>
       Nossa matriz fica em <a href="https://maps.google.com.br/?q=190,GabrielDequech,Mafra,SC"> 

**# sobre.html**

**112** 
26.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

Mafra, em Santa Catarina </a>. De lá, saem grande parte das gravações de nossos cursos. Nossa matr
iz:

     </p>

     <figure class="matriz-musicdot">
       <img src="img/matriz-musicdot.png" alt="Matriz da musicdot">
       <figcaption>
           Matriz MusicDot 
       </figcaption>
     </figure>

     <p>
       Assine os cursos da MusicDot. Acesse <a href="index.html"> nosso site </a> ou entre em con
tato

       se tiver dúvidas. Conheça também <a href="#historia"> nossa história </a> e <a href="#dife
renciais"> nossos diferenciais </a>.

     </p>

     <h2 id="historia" class="subtitulo"> História </h2>

     <figure class="familia-tupfeln">
       <img src="img/familia-tupfeln.jpg" alt="Foto da família tüpfeln">
       <figcaption>Família Tüpfeln</figcaption>
     </figure>

     <p>
       A fundação em 1932 ocorreu no momento da descoberta econônica de cursos por stream online 
no interior de Santa Catarina. A

       família Tüpfeln, tradicional da região, investiu todas as suas economias nessa nova inicia
tiva,

       revolucionária para a época. A fundadora frau Dagmar Olaf Tüpfeln, dotada de particular vi
são

       administrativa, guiou os negócios da empresa durante mais de 50 anos, muitos deles ao lado
       de seu filho Ernst Noten Tüpfeln, atual CEO. O nome da empresa é inspirado no nome da famí
lia.

     </p>

     <p>
       O crescimento da empresa foi praticamente instantâneo. Nos primeiros 5 anos, já atendia 18
países.
       Bateu a marca de 100 países em apenas 15 anos de existência. Até hoje, já atendeu 2 bilhõe
s

       de usuários diferentes, em bilhões de diferentes pedidos.
     </p>

     <p>
       O crescimento em número de funcionários é também assombroso. Hoje, é a maior empregadora d
o

       Brasil, mas mesmo após apenas 5 anos de sua existência, já possuía 30 mil funcionários. Fo
ra do

       Brasil, há 240 mil funcionários, além dos 890 mil brasileiros nas instalações de Mafra e
       nos escritórios em todo país.
     </p>

     <p>
       Dada a importância econômica da empresa para o Brasil, a família Tüpfeln já recebeu divers
os prêmios,

       homenagens e condecorações. Todos os presidentes do Brasil já visitaram as instalações da 
MusicDot, além de presidentes da União Européia, Ásia e o secretário-geral da ONU.

     </p>

     <h2 id="diferenciais" class="subtitulo"> Diferenciais </h2>
     <ul>

26.2 PASSO A PASSO COM CÓDIGO 
**113**


--------------------------------------------------

       <li> Menor preço do mercado, garantido </li>
       <li> Se você achar um serviço mais barato, leva 1 mês de graça </li>
       <li> Pague em reais, dólares, euros, libras, dodgecoins, litecoins ou bitcoins </li>
       <li> Todas as compras acompanham acesso à Alura </li>
       <li> Maior escola de música online do mundo </li>
       <li> Atendimento via telefone, email, chat, twitter, facebook, instagram, ICQ, WhatsApp, S
MS, carta, fax, sinal de fumaça e telegrama </li>

       <li> Presente em 124 países </li>
       <li> Mais de um milhão de funcionários em todo o mundo </li>
     </ul>

     <h2 class="titulo"> Contato </h2>

     <div class="contato__secao">
       <h3 class="contato__subtitulo"> Correspondência </h3>
       <small> (todos os dias, das 9h às 18h) </small>

       <address class="contato__info">
           AOVS Sistemas de Informática S.A
           <br>
           Rua Vergueiro, 3185, 8º andar
           <br>
           Vila Mariana
           <br>
           São Paulo - SP
       </address>
     </div>

     <div class="contato__secao contato__secao--telefone">
       <h3 class="contato__subtitulo"> Telefones </h3>
       <small> (segunda à sexta, das 9h às 18h) </small>

       <dl class="contato__info">
         <div>
           <dt class="contato__info-titulo"> Pessoa Física: </dt>
           <dd class="contato__info-descricao"> <a href="tel://114118-3319"> (11) 4118-3319 </a> 
</dd>

         </div>

         <div>
           <dt class="contato__info-titulo"> Pessoa Jurídica: </dt>
           <dd class="contato__info-descricao"> <a href="tel://114118-2172"> (11) 4118-2172 </a> 
</dd>

         </div>
       </dl>
     </div>

     <footer class="rodape">
       <img src="img/logo.svg" alt="Logo da musicdot" class="rodape__logo">
       <p class="rodape__copyright"> &copy; Copyright MusicDot </p>
     </footer>

   </body>
 </html>

**114** 
26.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

CAPÍTULO 27

Utilize as media queries para definir estilos diferenciados de acordo com o tamanho da tela.

As seções "Correspondência" e "Telefones" na parte de "contato" já não cabem mais uma do lado da
outra:

transforme as duas seções em blocos para que elas ocupem toda a largura disponível e não dividam
o espaço na horizontal entre sí.
adicione também um espaçamento à esquerda do tamanho de um caractér nessas mesmas seções.

Figura 27.1: Visual em telas de até 850px de largura

O texto que fica ao redor da imagem da família Tupfeln já não tem mais espaço para mais do que
duas palavras:

faça com que a  <figure>  da família deixe de flutuar para que os textos voltem a ficar apenas

embaixo da figura.

centralize a figura na horizontal, em relação à pagina.

# EXERCÍCIO: RESPONSIVIDADE COM
# `@MEDIA`

## 27.1 OBJETIVO

**Para telas de até 850px**

**Para telas de até 622px**

27 EXERCÍCIO: RESPONSIVIDADE COM `@MEDIA` 
**115**


--------------------------------------------------

Figura 27.2: Visual em telas de até 622px de largura

Os subtítulos dentro de "contato" não cabem mais na mesma linha junto com os horários:

Faça com que cada subtítulo desses vire um bloco, que ocupe a linha toda e faça a linha com os
horários ir para baixo.
As informação dentro de cada seção de "contato" já não cabem mais na tela:

substitua a margem à esquerda por uma borda de **1px** **cinza-claro** à esquerda.

coloque um espaçamento interno à esquerda de **5px**
deixe a fonte levemente menor ( 0.92em ) do que o tamanho da fonta da página

O conteúdo do rodapé já não cabe mais numa linha só:

deixe a fonte levemente menor do que a que a fonte da página ( 0.92em ).

Figura 27.3: Visual em telas de até 446px de largura

**Para telas de até 446px**

**116** 
27.1 OBJETIVO


--------------------------------------------------

Os números dos telefones estão no limite e quase já não cabem na mesma linha que sua descrição:

deixe os título da  <dl> dos telefones como bloco para que ocupem a linha toda

coloque um espaçamento à esquerda para dar a ideia de hierarquia entre título e número de telefone

Figura 27.4: Visual em telas de até 342px de largura

Se você está gostando dessa apostila, certamente vai aproveitar os **cursos**
**online** que lançamos na plataforma **Alura**. Você estuda a qualquer momento
com a **qualidade** Caelum. Programação, Mobile, Design, Infra, Front-End e

Business, entre outros! Ex-estudante da Caelum tem 10% de desconto, siga o link!

Conheça a Alura Cursos Online.

1. No arquivo ** sobre.css **na pasta ** css **faça as seguintes alterações:

**Para telas de até 342px**

**Agora é a melhor hora de aprender algo novo**

## 27.2 PASSO A PASSO COM CÓDIGO

27.2 PASSO A PASSO COM CÓDIGO 
**117**


--------------------------------------------------

 body {
   width: 80%;
   max-width: 940px;
   margin-left: auto;
   margin-right: auto;

   font-size: 16px;
   line-height: 1.5;
   font-family: "Helvetica", "Lucida Grande", sans-serif;
   color: #3D3D3D;
 }

 .titulo {
   padding: 10px;

   font-size: 32px;

   background-color: #E1EDF2;
 }

 .subtitulo {
   border-bottom: 2px solid black;
 }

 figure {
   max-width: 100%;
   box-sizing: border-box;
   margin: 30px;
   padding: 15px;

   text-align: center;

   background-color: whitesmoke;
   border: 1px solid lightgrey;
 }

 figcaption {
   margin-top: 10px;
 }

 .matriz-musicdot {
   width: 550px;
   margin-left: auto;
   margin-right: auto;
 }

 .familia-tupfeln {
   width: 275px;
   float: right;
 }

 figure img {
   width: 100%;
 }

 .contato__subtitulo {
   display: inline;
 }

 .contato__secao {

**# css/sobre.css**

**118** 
27.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

   display: inline-block;
   vertical-align: top;
   margin-left: 16px;
 }

 .contato__secao--telefone {
   margin-left: 32px;
 }

 .contato__info {
   margin: 16px 0 24px;
   padding-left: 32px;
 }

 .contato__info-titulo,
 .contato__info-descricao {
   display: inline;
 }

 .contato__info-descricao {
   margin-left: 10px;
 }

 .rodape {
   padding: 1.75em 0;

   font-size: 1.1rem;
 }

 .rodape__logo {
   width: 6em;
 }

 .rodape__copyright {
   display: inline;
   margin-left: 1em;
 }
+
+@media (max-width: 850px) {
+
+  .contato__secao {
+    display: block;
+    margin-left: 1em;
+  }
+
+}
+
+@media (max-width: 622px) {
+
+  .familia-tupfeln {
+    float: none;
+    margin: 0 auto;
+  }
+
+}
+
+@media (max-width: 446px) {
+
+  .contato__subtitulo {
+    display: block;
+    margin-bottom: 0;
+  }
+

27.2 PASSO A PASSO COM CÓDIGO 
**119**


--------------------------------------------------

+  .contato__info {
+    padding-left: 5px;
+    
+    font-size: .92em;
+
+    border-left: 2px solid lightgray;
+  }
+
+  .rodape {
+    font-size: .92em;
+  }
+
+}
+
+@media (max-width: 342px) {
+
+  .contato__info-descricao {
+    display: block;
+    margin-left: 1em;
+  }
+
+}

**120** 
27.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

CAPÍTULO 28

Existe hoje no mercado uma grande quantidade de empresas especializadas no desenvolvimento de sites
e aplicações web, bem como algumas empresas de desenvolvimento de software ou agências de

comunicação que têm pessoas capacitadas para executar esse tipo de projeto.

Quando detectada a necessidade do desenvolvimento de um site ou aplicação web, a empresa que
tem essa necessidade deve passar todas as informações relevantes ao projeto para a empresa que vai
executá-lo. A empresa responsável pelo seu desenvolvimento deve analisar muito bem essas

informações e utilizar pesquisas para complementar ou mesmo certificar-se da validade dessas
informações.

Um projeto de site ou aplicação web envolve muitas disciplinas em sua execução, pois são diversas
características a serem analisadas e diversas as possibilidades apresentadas pela plataforma. Por

exemplo, devemos conhecer muito bem as características do público alvo, pois ele define qual a melhor
abordagem para definir a navegação, tom linguístico e visual a ser adotado, entre outras. A afinidade do
público com a Internet e o dispositivo pode inclusive definir o tipo e a intensidade das inovações que

podem ser utilizadas.

Por isso, a primeira etapa do desenvolvimento do projeto fica a cargo da pessoa que cuida da
experiência de usuário (UX Designer) junto com uma pessoa de Design e alguém de conteúdo. Esse
grupo de pessoas analisa e endereça uma série de informações da característica humana do projeto,

definindo a quantidade, conteúdo, localização e estilização de cada informação.

Algumas das motivações e práticas de Experiência do Usuário são conteúdo do curso **Design de**
**Interação, Experiência do Usuário e Usabilidade**. O resultado do trabalho dessa equipe é uma série de
definições sobre a navegação (mapa do site) e um esboço de cada uma das visões, que são os layouts das

páginas, e visões parciais como, por exemplo, os diálogos de alerta e confirmação da aplicação. Por
essas visões serem esboços ainda, a parte de estilo do site fica mais genérica: são utilizadas fontes, cores
e imagens neutras, embora as informações escritas devam ser definidas nessa fase do projeto.

Esses esboços das visões são o que chamamos de **wireframes** e guiam o restante do processo de

design.

Com os wireframes em mãos, é hora de adicionar as imagens, cores, fontes, fundos, bordas e outras

# O PROCESSO DE DESENVOLVIMENTO
# DE UMA TELA

28 O PROCESSO DE DESENVOLVIMENTO DE UMA TELA 
**121**


--------------------------------------------------

características visuais. Esse trabalho é realizado pela mesma equipe acima, só que agora sem a pessoa de

conteúdo, que utilizam ferramentas gráficas como Adobe Photoshop, Adobe Illustrator, Figma, entre
outras. O resultado do trabalho dessa equipe é que chamamos de **layout**. Os layouts são imagens

estáticas já com o visual completo a ser implementado. Apesar de os navegadores serem capazes de
exibir imagens estáticas, exibir uma única imagem para o usuário final no navegador não é a forma ideal

de se publicar uma página.

Para que as informações sejam exibidas de forma correta e para possibilitar outras formas de uso e

interação com o conteúdo, é necessário que a equipe de **programação front-end** transforme essas
imagens em telas visíveis e, principalmente, utilizáveis pelos navegadores.

De todas as tecnologias disponíveis, a mais recomendada é certamente o HTML, pois é a linguagem
que o navegador entende. Todas as outras tecnologias citadas dependem do HTML para serem exibidas

corretamente no navegador e, ultimamente, o uso do HTML, em conjunto com o CSS e o JavaScript,
tem evoluído a ponto de podermos substituir algumas dessas outras tecnologias onde tínhamos mais
poder e controle em relação à exibição de gráficos, efeitos e interatividade.

Antes de digitar qualquer código, é necessária uma análise do layout. Com essa análise, definiremos
as principais áreas de nossas páginas. Note que há um cabeçalho (uma área que potencialmente se

repetirá em mais de uma página), um rodapé e um conteúdo principal. Seguindo o pensamento de
escrever o nosso código pensando em semântica em primeiro lugar, já podemos imaginar como que será
a estrutura no documento  html 

*<!DOCTYPE html>*
<html lang="pt-BR">
<head>

   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width">
   <title>MusicDot</title>
</head>
<body>

   <header>
       <!-- Conteúdo do header -->
   </header>
   <main>
       <!-- Conteúdo principal -->
   </main>
   <footer>
       <!-- Conteúdo do footer -->
   </footer>
</body>
</html>

Uma recomendação é a de começar a planejar o código sempre analizando de fora para dentro.

Portanto, depois de ver as 3 principais camadas ( <header> ,  <main>  e  <footer> ) vamos nos

aprofundar em uma delas. Vamos partir da ordem de declaração e nos aprofundar mais na tag

## 28.1 ANALISANDO O LAYOUT

**122** 
28.1 ANALISANDO O LAYOUT


--------------------------------------------------

<header> . Dentro de  header temos uma **logo** e 3 **links**. Sabemos já que a logo é uma **imagem**:

*<!DOCTYPE html>*
<html lang="pt-BR">
<head>

   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width">
   <title>MusicDot</title>
</head>
<body>

   <header>
       <!-- Conteúdo do header -->
       <img src="img/logo-musicdot.png" alt="Logo da MusicDot">
   </header>
   <main>
       <!-- Conteúdo principal -->
   </main>
   <footer>
       <!-- Conteúdo do footer -->
   </footer>
</body>
</html>

Agora com os links precisamos notar que são links que vão para outras páginas dentro do nosso
próprio site portanto esses 3 **links** fazem parte de uma **navegação** e que são 3 **links** em sequência.
Quando temos elementos iguais em sequência temos uma **lista**! Nesse nosso caso a ordem dos links não

importa:

*<!DOCTYPE html>*
<html lang="pt-BR">
<head>

   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width">
   <title>MusicDot</title>
</head>
<body>

   <header>
       <!-- Conteúdo do header -->
       <img src="img/logo-musicdot.png" alt="Logo da MusicDot">
       <nav>
           <ul>
               <li><a href="#">Contato</a></li>
               <li><a href="#">Entrar</a></li>
               <li><a href="#">Matricule-se</a></li>
           </ul>
       </nav>
   </header>
   <main>
       <!-- Conteúdo principal -->
   </main>
   <footer>
       <!-- Conteúdo do footer -->
   </footer>
</body>
</html>

O próximo passo seria fazer o aprofundamento de outra tag e assim por diante. Lembre-se de que

essa é apenas uma recomendação!

28.1 ANALISANDO O LAYOUT 
**123**


--------------------------------------------------

Editoras tradicionais pouco ligam para ebooks e novas tecnologias. Não dominam

tecnicamente o assunto para revisar os livros a fundo. Não têm anos de

experiência em didáticas com cursos.

Conheça a **Casa do Código**, uma editora diferente, com curadoria da **Caelum** e

obsessão por livros de qualidade a preços justos.

Casa do Código, ebook com preço de ebook.

**Editora Casa do Código com livros de uma forma diferente**

**124** 
28.1 ANALISANDO O LAYOUT


--------------------------------------------------

CAPÍTULO 29

Começaremos agora a página principal da MusicDot.

Edite o arquivo  index.html  que criamos anteriormente (se não criou antes, é só criar agora) e

coloque toda a estrutura básica de um arquivo *HTML* e também aproveite para criar toda a estrutura do

cabeçalho da home. No link de "Contato" do menu do cabeçalho, aponte para a parte de contato na
página  sobre.html .

Num celular o cabeçalho terá a seguite aparência:

Figura 29.1: Cabeçalho em telas pequenas

Não se preocupe em criar os nomes das classes e estilizar ainda. Sem estilos o resultado final será

próximon a esse:

# EXERCÍCIO: ESTRUTURA DA PÁGINA
# PRINCIPAL E O CABEÇALHO

## 29.1 OBJETIVO

29 EXERCÍCIO: ESTRUTURA DA PÁGINA PRINCIPAL E O CABEÇALHO 
**125**


--------------------------------------------------

Figura 29.2: O visual apenas com marcação semântica do cabeçalho

Nos próximos exercícios contruiremos um cabeçalho responsivo param vários tamanhos de tela:

Figura 29.3: Cabeçalho em telas pequenas

**126** 
29.1 OBJETIVO


--------------------------------------------------

Figura 29.4: Cabeçalho em telas médias

Figura 29.5: Cabeçalho em telas grandes

A **Alura** oferece centenas de **cursos online** em sua plataforma exclusiva de

ensino que favorece o aprendizado com a **qualidade** reconhecida da Caelum.
Você pode escolher um curso nas áreas de Programação, Front-end, Mobile,
Design & UX, Infra, Business, entre outras, com um plano que dá acesso a todos os cursos. Ex-

estudante da Caelum tem 10% de desconto neste link!

Conheça os cursos online Alura.

**Já conhece os cursos online Alura?**

## 29.2 PASSO A PASSO COM CÓDIGO

29.2 PASSO A PASSO COM CÓDIGO 
**127**


--------------------------------------------------

1. No arquivo ** index.html **na pasta ** raíz do projeto **faça as seguintes alterações:

-<̶h̶1̶>̶ P̶á̶g̶i̶n̶a̶ p̶r̶i̶n̶c̶i̶p̶a̶l̶ t̶e̶m̶p̶o̶r̶á̶r̶i̶a̶ d̶a̶ M̶u̶s̶i̶c̶D̶o̶t̶ </̶h̶1̶>
+*<!doctype html>*
+<html>
+  <head>
+    <meta charset="utf-8">
+    <meta name="viewport" content="width=device-width">
+    <title>Musicdot</title>
+    <link rel="icon" href="img/favicon.ico">
+  </head>
+  <body>
+
+    <header>
+      <a href="index.html">
+        <img src="img/musicdot-logo-light.svg" title="Ir para a página inicial da Musicdot" alt=
"Musicdot">

+      </a>
+      
+      <nav>
+        <ul>
+          <li> <a href="sobre.html#contato"> Contato </a> </li>
+          <li> <a href="#"> Entrar </a> </li>
+          <li> <a href="#"> Matricule-se </a> </li>
+        </ul>
+      </nav>
+    </header>
+
+    <main>
+      Conteúdo principal
+    </main>
+
+    <footer>
+      Rodapé
+    </footer>
+  </body>
+</html>

2. No arquivo ** sobre.html **na pasta ** raíz do projeto **faça as seguintes alterações:

 *<!doctype html>*
 <html lang="pt-BR">
   <head>
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width">
     <title>
       MusicDot | Sobre a empresa
     </title>
     <link href="img/favicon.ico" rel="icon">
     <link rel="stylesheet" href="css/sobre.css">
   </head>

   <body>

     <img src="img/logo.svg" alt="MusicDot">

**# index.html**

**# sobre.html**

**128** 
29.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

     <h1 class="titulo"> Sobre a empresa </h1>

     <p>
       A MusicDot é a maior escola online de música em todo o mundo.
       Fundada em 1932, possui estúdios em 124 países, sendo líder de mercado com mais de 90% de
       participação em 118 deles.
     </p>

     <p>
       Nossa matriz fica em <a href="https://maps.google.com.br/?q=190,GabrielDequech,Mafra,SC"> 
Mafra, em Santa Catarina </a>. De lá, saem grande parte das gravações de nossos cursos. Nossa matr
iz:

     </p>

     <figure class="matriz-musicdot">
       <img src="img/matriz-musicdot.png" alt="Matriz da musicdot">
       <figcaption>
           Matriz MusicDot 
       </figcaption>
     </figure>

     <p>
       Assine os cursos da MusicDot. Acesse <a href="index.html"> nosso site </a> ou entre em con
tato

       se tiver dúvidas. Conheça também <a href="#historia"> nossa história </a> e <a href="#dife
renciais"> nossos diferenciais </a>.

     </p>

     <h2 id="historia" class="subtitulo"> História </h2>

     <figure class="familia-tupfeln">
       <img src="img/familia-tupfeln.jpg" alt="Foto da família tüpfeln">
       <figcaption>Família Tüpfeln</figcaption>
     </figure>

     <p>
       A fundação em 1932 ocorreu no momento da descoberta econônica de cursos por stream online 
no interior de Santa Catarina. A

       família Tüpfeln, tradicional da região, investiu todas as suas economias nessa nova inicia
tiva,

       revolucionária para a época. A fundadora frau Dagmar Olaf Tüpfeln, dotada de particular vi
são

       administrativa, guiou os negócios da empresa durante mais de 50 anos, muitos deles ao lado
       de seu filho Ernst Noten Tüpfeln, atual CEO. O nome da empresa é inspirado no nome da famí
lia.

     </p>

     <p>
       O crescimento da empresa foi praticamente instantâneo. Nos primeiros 5 anos, já atendia 18
países.
       Bateu a marca de 100 países em apenas 15 anos de existência. Até hoje, já atendeu 2 bilhõe
s

       de usuários diferentes, em bilhões de diferentes pedidos.
     </p>

     <p>
       O crescimento em número de funcionários é também assombroso. Hoje, é a maior empregadora d
o

       Brasil, mas mesmo após apenas 5 anos de sua existência, já possuía 30 mil funcionários. Fo
ra do

       Brasil, há 240 mil funcionários, além dos 890 mil brasileiros nas instalações de Mafra e
       nos escritórios em todo país.
     </p>

29.2 PASSO A PASSO COM CÓDIGO 
**129**


--------------------------------------------------

     <p>
       Dada a importância econômica da empresa para o Brasil, a família Tüpfeln já recebeu divers
os prêmios,

       homenagens e condecorações. Todos os presidentes do Brasil já visitaram as instalações da 
MusicDot, além de presidentes da União Européia, Ásia e o secretário-geral da ONU.

     </p>

     <h2 id="diferenciais" class="subtitulo"> Diferenciais </h2>
     <ul>
       <li> Menor preço do mercado, garantido </li>
       <li> Se você achar um serviço mais barato, leva 1 mês de graça </li>
       <li> Pague em reais, dólares, euros, libras, dodgecoins, litecoins ou bitcoins </li>
       <li> Todas as compras acompanham acesso à Alura </li>
       <li> Maior escola de música online do mundo </li>
       <li> Atendimento via telefone, email, chat, twitter, facebook, instagram, ICQ, WhatsApp, S
MS, carta, fax, sinal de fumaça e telegrama </li>

       <li> Presente em 124 países </li>
       <li> Mais de um milhão de funcionários em todo o mundo </li>
     </ul>

     <h2 class="titulo"> Contato </h2>

     <div class="contato__secao">
       <h3 class="contato__subtitulo"> Correspondência </h3>
       <small> (todos os dias, das 9h às 18h) </small>

       <address class="contato__info">
           AOVS Sistemas de Informática S.A
           <br>
           Rua Vergueiro, 3185, 8º andar
           <br>
           Vila Mariana
           <br>
           São Paulo - SP
       </address>
     </div>

-    <̶d̶i̶v̶ c̶l̶a̶s̶s̶=̶"̶c̶o̶n̶t̶a̶t̶o̶_̶_̶s̶e̶c̶a̶o̶ c̶o̶n̶t̶a̶t̶o̶_̶_̶s̶e̶c̶a̶o̶-̶-̶t̶e̶l̶e̶f̶o̶n̶e̶"̶>
+    <div id="contato" class="contato__secao contato__secao--telefone">
       <h3 class="contato__subtitulo"> Telefones </h3>
       <small> (segunda à sexta, das 9h às 18h) </small>

       <dl class="contato__info">
         <div>
           <dt class="contato__info-titulo"> Pessoa Física: </dt>
           <dd class="contato__info-descricao"> <a href="tel://114118-3319"> (11) 4118-3319 </a> 
</dd>

         </div>

         <div>
           <dt class="contato__info-titulo"> Pessoa Jurídica: </dt>
           <dd class="contato__info-descricao"> <a href="tel://114118-2172"> (11) 4118-2172 </a> 
</dd>

         </div>
       </dl>
     </div>

     <footer class="rodape">
       <img src="img/logo.svg" alt="Logo da musicdot" class="rodape__logo">
       <p class="rodape__copyright"> &copy; Copyright MusicDot </p>
     </footer>

**130** 
29.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

   </body>
 </html>

29.2 PASSO A PASSO COM CÓDIGO 
**131**


--------------------------------------------------

CAPÍTULO 30

Quando não especificamos nenhum estilo para nossos elementos do HTML, o navegador utiliza uma
série de estilos padrão, que são diferentes em cada um dos navegadores. Em um momento mais

avançado dos nossos projetos, poderemos enfrentar problemas com coisas que não tínhamos previsto;
por exemplo, o espaçamento entre caracteres utilizado em determinado navegador pode fazer com que
um texto que, pela nossa definição deveria aparecer em 4 linhas, apareça com 5, quebrando todo o nosso

layout.

Para evitar esse tipo de interferência, alguns desenvolvedores e empresas criaram alguns estilos que
chamamos de **CSS Reset**. A intenção é setar (definir) um valor básico para todas as características do
CSS, sobrescrevendo totalmente os estilos padrão do navegador.

Desse jeito podemos começar a estilizar as nossas páginas a partir de um ponto que é o mesmo para

todos os casos, o que nos permite ter um resultado muito mais sólido em vários navegadores.

Existem algumas opções para resetar os valores do CSS. Algumas que merecem destaque hoje são as
seguintes:

**HTML5 Boilerplate**

O HTML5 Boilerplate é um projeto que pretende fornecer um excelente ponto de partida para quem
pretende desenvolver um novo projeto com HTML5. Uma série de técnicas para aumentar a
compatibilidade da nova tecnologia com navegadores um pouco mais antigos estão presentes e o código

é totalmente gratuito. Em seu arquivo "style.css", estão reunidas diversas técnicas de CSS Reset. Apesar
de consistentes, algumas dessas técnicas são um pouco complexas, mas é um ponto de partida que

podemos considerar.

https://html5boilerplate.com/

**YUI3 CSS Reset**

Criado pelos desenvolvedores front-end do Yahoo!, uma das referências na área, esse CSS Reset é

composto de 3 arquivos distintos. O primeiro deles, chamado de **Reset**, simplesmente muda todos os
valores possíveis para um valor padrão, onde até mesmo as tags  <h1>  e  <small>  passam a ser

# ESTILIZANDO O HEADER DA HOME

## 30.1 CSS RESET

**132** 
30.1 CSS RESET


--------------------------------------------------

exibidas com o mesmo tamanho. O segundo arquivo é chamado de **Base**, onde algumas margens e

dimensões dos elementos são padronizadas. O terceiro é chamado de **Font**, onde o tamanho dos tipos é
definido para que tenhamos um visual consistente inclusive em diversos dispositivos móveis.

**Eric Meyer CSS Reset**

Há 
também 
o 
famoso 
CSS 
Reset 
de 
Eric 
Meyer, 
que 
pode 
ser 
obtido 
em

http://meyerweb.com/eric/tools/css/reset/. É apenas um arquivo com tamanho bem reduzido.

Vale lembrar que o uso de cada **reset** varia conforme a necessidade. Alguns CSS Resets são mais
*agressivos* do que outros, e também é importante saber que eles podem ser modificados para suas
próprias necessidades. Existem pessoas que desenvolvem seus próprios CSS Resets e elas costumam

compartilhar seus códigos em certos fórums voltados para  HTML e  CSS .

Querendo aprender ainda mais sobre? Esclarecer dúvidas dos exercícios? Ouvir
explicações detalhadas com um instrutor?
A Caelum oferece o **curso data** presencial nas cidades de São Paulo, Rio de

Janeiro e Brasília, além de turmas incompany.

Consulte as vantagens do curso *Desenvolvimento Web com HTML, CSS e*

*JavaScript*

É comum que páginas na web tenham tipografias que combinem com a sua estética e linguagem
visual, também para a facilidade de leitura. Só que nem sempre os usuários possuem as fontes que
queremos usar em nossas páginas. Para isso precisamos decidir em como fazer para que nossos usuários

tenham acesso a essas fontes. Uma maneira super comum e fácil é usar o ***Google Fonts***. Basta entrar no
site https://fonts.google.com/, escolher uma tipografia e depois escolher como importar a fonte. A
primeira maneira de se importar a fonte do ***Google Fonts*** é usando a tag  <link>  e passar a referência

para o ***Google Fonts***. Não se preocupe que na hora de escolher uma fonte a própria Google dá o código

pronto para você utilizar:

<link href="https://fonts.googleapis.com/css?family=Roboto&display=swap" rel="stylesheet">

**Você pode também fazer o curso data dessa apostila na Caelum**

## 30.2 FONTES PRÓPRIAS

30.2 FONTES PRÓPRIAS 
**133**


--------------------------------------------------

O ideal é fazer essa importação antes de qualquer arquivo CSS para garantir que todos os arquivos

depois vão conseguir utilizar essa fonte.

A outra maneira de importar é fazendo um ***@import*** no próprio arquivo CSS que você vai usar a

fonte:

@import url('https://fonts.googleapis.com/css?family=Roboto&display=swap');

body {

   font-family: 'Roboto', sans-serif;
}

Outra maneira de importar fonte sem depender de serviços externos é importar o próprio arquivo de
fonte no arquivo CSS que essa fonte será utilizada usando o ***@font-face***:

@font-face {

 font-family: minhaFonte;
 src: url(fonts/minha-fonte-customizada.woff);
}

body {

   font-family: 'minhaFonte', sans-serif;
}

Uma observação extremamente importante quando utilizar fontes da web:

Antes de usar qualquer fonte verifique os direitos autorais dela e veja se é necessário permissão
ou compra da fonte. A vantagem de se usar o ***Google Fonts*** é que todas as fontes são abertas para

uso livre, mas no caso de outras fontes é bom verificar antes. O que não queremos é o uso indevido
de fontes.

Durante o desenvolvimento do projeto, principalmente na parte de planejamento, definimos diversas
seções que vão englobar os diversos conteúdos de nossa página que podem ou não se repetir em outras

páginas de nosso site. Podemos lidar com a situação de diversas maneiras:

A abordagem de criar um CSS geral com um CSS específico da página é bem conhecida e muito
utilizada no mercado. A idéia é criar um CSS que vai conter estilos que podem se repetir em diversas

páginas, como por exemplo, tipografia, cores, tamanhos e até alguns componentes, e depois criar um

## 30.3 MODULARIZANDO COMPONENTES COM CSS ISOLADOS

**### CSS Geral com CSS Específico da Página**

**134** 
30.3 MODULARIZANDO COMPONENTES COM CSS ISOLADOS


--------------------------------------------------

CSS que vai conter estilos específicos daquela página. Como tudo na vida, existem vantagens e
desvantagens dessa abordagem.

Vantagens:

Só é necessário a importação de um arquivo CSS para que a página já tenha um estilo padrão.
Como todas as classes de estilos estão em um lugar só, podemos escrever o  html já colocando

os nomes de classes que precisamos. Quase como um *framework*.

Desvantagens:

Todas as páginas terão de carregar um arquivo de estilos gigantesco independete se vão usar
todas as classes ou não, o que pode impactar performance.
Dependendo do tamanho do arquivo geral pode ser muito complexo encontrar seletores que
queremos usar.

Se por algum motivo queremos usar algo que era para ser exclusivo de uma página em outra
página, teremos de fazer a "portabilidade" para o arquivo geral o que pode bagunçar o arquivo
geral.

Manutenção pode ser complexo dependendo do tamanho do arquivo.

Essa abordagem também é bastante utilizada no mercado só que ela é mais utilizada em projetos
com o uso de frameworks (React, Angular) e pré processadores de CSS (SASS). Nessa abordagem cada

seção ou componente da página tem um CSS exclusivo.

Vantagens:

Como cada componente tem seu próprio CSS só é necessário importar os componentes que

precisamos usar em cada página, evitando importar estilos desnecessários.
Organização e manutenção fica menos complicada porque é mais claro saber exatamente qual
arquivo trabalhar.

Desvantagens:

Precisamos importar um arquivo CSS diferente para cada componente que queremos usar que

pode gerar linhas de imports gigantescas.

**### Um CSS Para Cada Componente Da Página**

30.3 MODULARIZANDO COMPONENTES COM CSS ISOLADOS 
**135**


--------------------------------------------------

CAPÍTULO 31

Nessa página seguiremos uma organização de arquivos CSS onde cada bloco do BEM terá seu próprio

arquivo CSS.

Iniciaremos os estilos em **cabecalho.css** alterando sua cor de fundo para um azul-escuro **"#2D5377"**
e a cor do conteúdo para branco **"#FFF"**.

Ao fazer isso, note que os links não mudam sua cor para branco e que há um espaçamento que não
colocamos entre a página e o cabeçalho:

# EXERCÍCIO: COMEÇANDO A ESTILIZAR
# O `HEADER` DA HOME

## 31.1 OBJETIVO

**136** 
30 EXERCÍCIO: COMEÇANDO A ESTILIZAR O `HEADER` DA HOME


--------------------------------------------------

Figura 31.1: Estilos estranhos no cabeçalho

31.1 OBJETIVO 
**137**


--------------------------------------------------

Para solucionar precisaremos adicionar um CSS que retire os estilos padrão do navegador.
Chamamos esse tipi de estilo de *reset*. O *reset* que usaremos está parcialmente pronto e está disponível
em https://meyerweb.com/eric/tools/css/reset/reset.css.

Adicionaremos mais alguns estilos nesse reset:

alteraremos a fonte padrão de todo texto na página pela fonte ** Montserrat **

todo texto na página por padrão terá a cor ** #2e4255 **

todo link terá a cor herdada da cor da fonte do seu parente

todo link terá a decoração de texto (e.g. underline) herdada de seu parente

Para que a fonte Montserrat funcione mesmo em computadores que não tenham ela instalada,
precisaremos baixar e criar essa família de fontes com CSS. Por enquanto, usaremos esse CSS pronto de

um 
serviço 
chamado 
Google 
Fonts, 
em: 
https://fonts.googleapis.com/css?
family=Montserrat:300,400,500,600,700,&display=block. Nesse endereço há um arquivo CSS com tudo
pronto, basta importá-lo como um arquivo CSS na página.

O resultado final será o seguinte:

**138** 
31.1 OBJETIVO


--------------------------------------------------

31.1 OBJETIVO 
**139**


--------------------------------------------------

Figura 31.2: Cabecalho com reset e estilos iniciais

Conheça a **Casa do Código**, uma **nova** editora, com autores de destaque no

mercado, foco em **ebooks** (PDF, epub, mobi), preços **imbatíveis** e assuntos
**atuais**.
Com a curadoria da **Caelum** e excelentes autores, é uma abordagem **diferente**

para livros de tecnologia no Brasil.

Casa do Código, Livros de Tecnologia.

1. Crie o arquivo ** cabecalho.css **na pasta ** css **com o seguinte código:

+.cabecalho {
+  background-color: #2D5377;
+  color: #fff;
+}

2. No arquivo ** index.html **na pasta ** raíz do projeto **faça as seguintes alterações:

 *<!doctype html>*
 <html>
   <head>
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width">
     <title>Musicdot</title>
     <link rel="icon" href="img/favicon.ico">
+    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:300,400,500,
600,700,&display=block">

+    <link rel="stylesheet" href="css/reset.css">
+    <link rel="stylesheet" href="css/cabecalho.css">
   </head>
   <body>

-    <̶h̶e̶a̶d̶e̶r̶>
+    <header class="cabecalho">
       <a href="index.html">
         <img src="img/musicdot-logo-light.svg" title="Ir para a página inicial da Musicdot" alt=
"Musicdot">

**Seus livros de tecnologia parecem do século passado?**

## 31.2 PASSO A PASSO COM CÓDIGO

**# css/cabecalho.css**

**# index.html**

**140** 
31.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

       </a>

       <nav>
         <ul>
           <li> <a href="sobre.html#contato"> Contato </a> </li>
           <li> <a href="#"> Entrar </a> </li>
           <li> <a href="#"> Matricule-se </a> </li>
         </ul>
       </nav>
     </header>

     <main>
       Conteúdo principal
     </main>

     <footer>
       Rodapé
     </footer>
   </body>
 </html>

3. No arquivo ** reset.css **na pasta ** css **faça as seguintes alterações:

 /* http://meyerweb.com/eric/tools/css/reset/ 
    v2.0 | 20110126
    License: none (public domain)
 */

 html, body, div, span, applet, object, iframe,
 h1, h2, h3, h4, h5, h6, p, blockquote, pre,
 a, abbr, acronym, address, big, cite, code,
 del, dfn, em, img, ins, kbd, q, s, samp,
 small, strike, strong, sub, sup, tt, var,
 b, u, i, center,
 dl, dt, dd, ol, ul, li,
 fieldset, form, label, legend,
 table, caption, tbody, tfoot, thead, tr, th, td,
 article, aside, canvas, details, embed, 
 figure, figcaption, footer, header, hgroup, 
 menu, nav, output, ruby, section, summary,
 time, mark, audio, video {
     margin: 0;
     padding: 0;
     border: 0;
     font-size: 100%;
     font: inherit;
     vertical-align: baseline;
 }
 /* HTML5 display-role reset for older browsers */
 article, aside, details, figcaption, figure, 
 footer, header, hgroup, menu, nav, section {
     display: block;
 }
 body {
     line-height: 1;
 }
 ol, ul {
     list-style: none;
 }
 blockquote, q {

**# css/reset.css**

31.2 PASSO A PASSO COM CÓDIGO 
**141**


--------------------------------------------------

     quotes: none;
 }
 blockquote:before, blockquote:after,
 q:before, q:after {
     content: '';
     content: none;
 }
 table {
     border-collapse: collapse;
     border-spacing: 0;
 }
+
+body {
+  font-family: 'Montserrat', sans-serif;
+  color: #2e4255;
+}
+
+a {
+  color: inherit;
+  text-decoration: inherit;
+}

**142** 
31.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

CAPÍTULO 32

Pessoas diferentes vão usar nosso site em dispositivos diferentes dos que nós usamos para desenvolver,

em lugares diferentes do que estamos e em condições muito diferentes das que nos desenvolvemos o
site.

Tamanho de tela.

Pessoas podem acessar nosso site de diversos dispositivos com tamanho de telas diferentes, por
exemplo, celulares, TVs, tablets, notebooks...

Ausência de mouse e teclado.

Nem todos os dispositivos do mundo suportam um mouse e um teclado.

Pointer menos preciso: *touchscreen*.

Geralmente na ausência de um mouse, o **toque** se torna o ponteiro do dispositivo.
Navegadores diferentes e navegadores em versões diferentes

Navegadores desatualizados suportam menos tecnologias que navegadores mais novos, e

diferentes navegadores mostram páginas de maneiras diferentes.
Tipos de conexões.

3G da TIM no túnel/metrô e TIM Fibra no Escritório da firma a 1 GB/s tem velocidades bem
diferentes que impactam como a página pode ser mostrada.
Pessoas com Deficiências.

Algumas pessoas podem ter dificuldades para acessar nosso site como problemas de visão:
cegueira, miopia, visão embaçada; motora: incapacidade de usar um mouse, controle motor com
limitações; audição: surdez.

Pessoas usando o site em situações diferentes.

No metrô ou ônibus lotado e pessoas sentadas no escritório da firma ou em casa.

O que isso significa pra quem está desenvolvendo o site: definir e garantir que o site seja acessível

nessas condições **definidas**. Como garantir isso? Testar em todas as situações e modificar o código
sempre que o teste numa dada situação falhe. Se não pensarmos e testarmos em dispositivos e casos de
uso em condições difrentes ou com limitações e restrições há grandes chances de que nosso site só fique

utilizável pra quem se enquadre no perfil testado. E se não der para testar em todas as situações? Como
tentar "reduzir" ou padronizar o esforço? Tentar seguir um fluxo de desenvolvimento (ou pensamento?)

# PROGRESSIVE ENHANCEMENT

## 32.1 CONDIÇÕES, OPÇÕES, LIMITAÇÕES E RESTRIÇÕES

31 PROGRESSIVE ENHANCEMENT 
**143**


--------------------------------------------------

que "automaticamente" inclua a maior parte das situações:

Em relação a espaço de tela: analogia da caixa de fósforo vs caixa de sapato. O que cabe numa
caixa de sapato cabe numa caixa de fósforo? e o contrário?

Devemos pensar e testar **primeiro** na base que é igual/mínima para todas as pessoas e depois

"melhorar"/ adicionar código para situações onde caibam essas melhorias. Uma ordem de
desenvovlimento, o porquê de cada passo e como testar:

1. Conteúdo. Conteúdo é o que todas as pessoas querem ver num site e começamos por ele.

2. Qual tipo de conteúdo a página vai ter? Como o conteúdo vai ser agrupado? Onde vai cada
conteúdo? Qual a quantidade de conteúdo em cada lugar?

3. Teste: revisão de conteúdo, ortografia e etc.

4. Semântica com HTML. Semântica é uma melhoria em cima do conteúdo sem nenhuma marcação.

5. Como se localizar entre 1000 linhas de conteúdo para marcar e dar manutenção nesse conteúdo?

6. Teste: a tag escolhida (ex:  <footer> ) melhora a localização do código e a legibilidade para quem

está desenvolvendo?
7. Como usar o site sem acesso ao visual dele? Muitas pessoas dependem só do conteúdo para navegar
no site. Essas pessoas usam **leitores de tela** que interpretam a página e deixam ela acessível e

navegável de uma maneira similar à forma que quem desenvolve o código se localiza no código
(pelas tags). Leitores de tela permitem que uma pessoa leia diretamente o conteúdo do  <footer> ao

invés de ler todo o conteúdo da página do início até o fim para chegar no conteúdo do  <footer> .

8. Teste: definir casos de uso, abrir e usar o site de acordo em um leitor de tela

9. Outro teste: programas que exibem a árvore de acessibilidade (ex: Dev Tools do Firefox)

10. CSS. Estilos farão o conteúdo ser exibido de uma maneira **melhor**. O foco ainda é o conteúdo, então
estilos são o terceiro passo, uma **melhoria**.

11. Um estilo deve melhorar e manter o conteúdo sempre acessível em qualquer situação.

12. Recomendamos começar limitando a largura e/ou a altura do viewport. Isso incentivará que CSS não
impeça o acesso ao conteúdo em telas menores e o conteúdo que está numa tela menor acaba sendo

acessível em telas maiores (por mais que as vezes seja feio). diversas versões de navegadores.
13. CSS sem limitação de tamanhos já é super responsivo! Quem pode deixar um site não responsivo é o
CSS de quem está desenvolvendo o site.

**144** 
32.1 CONDIÇÕES, OPÇÕES, LIMITAÇÕES E RESTRIÇÕES


--------------------------------------------------

Na hora de escolher qual código HTML e CSS escrever. A W3C, o Progressive Enhancement e os

navegadores desatualizados:

A tag que estou escolhendo é identificada pelos *User Agents* que vamos dar suporte? Se tag é

nova e não existe ainda naquela versão de navegador, o que acontece? Tags novas são
melhoria e em navegadores desatualizados viram  <div> . O conteúdo não vai deixar de ser

exibido.

Propriedades e valores novos do CSS (#rrggbbaa) em navegadores desatualizados são
desconsiderados e a tag segue em frente sendo exibida na página.

O site não vai parar de funcionar. Coisas antigas não deixam de existir ou de funcionar. A

W3C usa o **P****ROGRESSIVE**** E****NHANCEMENT** para atualizar o HTML, o CSS e outros padrões a
cada nova versão. Novas versões geralmente não mudam o que havia antes, melhoram.

WCAG: tamanho de fontes, contraste, legibilidade, etc

Se você está gostando dessa apostila, certamente vai aproveitar os **cursos**
**online** que lançamos na plataforma **Alura**. Você estuda a qualquer momento

com a **qualidade** Caelum. Programação, Mobile, Design, Infra, Front-End e
Business, entre outros! Ex-estudante da Caelum tem 10% de desconto, siga o link!

Conheça a Alura Cursos Online.

**Agora é a melhor hora de aprender algo novo**

32.1 CONDIÇÕES, OPÇÕES, LIMITAÇÕES E RESTRIÇÕES 
**145**


--------------------------------------------------

CAPÍTULO 33

Durante todo o curso aplicaremos um conceito chamado de Progressive Enhancement. O P.E. vai

permear todos os nossos códigos.

Nesse primeiro momento, o que é importante para nós:

Escolher uma marcação semântica que ajude quem está desenvolvendo o site a se guiar pelo

código, geralmente já ajuda na acessibilidade de leitores de tela.

Testar semântica em leitores de tela (NVDA) ou em ferramentas de acessibilidade (Dev tools do
Firefox).
Desenvolver com device-mode aberto no mobile. Telas menores primeiro: *mobile-first*

Ainda no device-mode deixar o modo de touch habilitado (escolher um celular como dispositivo)

Iniciaremos todo o estilo do cabeçalho com o *Device Mode* do navegador já configurado para uma
tela de celular. O resultado esperado é o seguinte:

Figura 33.1: Cabeçalho finalizado numa tela pequena

# EXERCÍCIO: PROGRESSIVE
# ENHANCEMENT

## 33.1 OBJETIVO

**146** 
32 EXERCÍCIO: PROGRESSIVE ENHANCEMENT


--------------------------------------------------

Para facilitar os cliques nos items do menu, para quem usa pointer com menor precisão (e.g.
toucshscreen), aumentaremos a área clicável de cada link do menu, colocando um espaçamento
interno de ** 1.86em 1.42em **.

Diminuiremos o tamanho da fonte no cabecalho, porém, ainda deixaremos o texto legível para
baixa visão:

deixar tudo com letras maiúsculas preservando a semântica do conteúdo

aumentar o espaçamento entre as letras

melhorar o contraste escurencendo a cor de fundo do menu com um cinza-escuro-transparente:

** #272B3A87 **

verifique o suporte do padrão de cores ** #rrggbbaa ** em https://caniuse.com/#search=rrggbbaa e

use uma alternativa caso ache necessário

Usar o layout padrão do CSS ao nosso favor, deixando tudo como está e alterando apenas o

alinhamento do conteúdo do cabeçalho

Editoras tradicionais pouco ligam para ebooks e novas tecnologias. Não dominam
tecnicamente o assunto para revisar os livros a fundo. Não têm anos de
experiência em didáticas com cursos.
Conheça a **Casa do Código**, uma editora diferente, com curadoria da **Caelum** e
obsessão por livros de qualidade a preços justos.

Casa do Código, ebook com preço de ebook.

1. No arquivo ** cabecalho.css **na pasta ** css **faça as seguintes alterações:

 .cabecalho {
-  b̶a̶c̶k̶g̶r̶o̶u̶n̶d̶-̶c̶o̶l̶o̶r̶:̶ #̶2̶D̶5̶3̶7̶7̶;̶
+  text-align: center;
+  font-size: 0.6rem;
+  font-weight: bold;
+  text-transform: uppercase;
+  letter-spacing: 0.23em;
+

**Editora Casa do Código com livros de uma forma diferente**

## 33.2 PASSO A PASSO COM CÓDIGO

**# css/cabecalho.css**

33.2 PASSO A PASSO COM CÓDIGO 
**147**


--------------------------------------------------

   color: #fff;
+  background-color: #2D5377;
+}
+
+.cabecalho__logo {
+  padding: 1.5em 0;
+  width: 14.5em;
+}
+
+.cabecalho__menu {
+  background-color: #272B3A87;
+}
+
+.cabecalho__item-menu {
+  display: inline-block;
+}
+
+.cabecalho__item-menu a {
+  display: inline-block;
+  padding: 1.86em 1.42em;
 }

2. No arquivo ** index.html **na pasta ** raíz do projeto **faça as seguintes alterações:

 *<!doctype html>*
 <html>
   <head>
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width">
     <title>Musicdot</title>
     <link rel="icon" href="img/favicon.ico">
     <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:300,400,500,
600,700,&display=block">

     <link rel="stylesheet" href="css/reset.css">
     <link rel="stylesheet" href="css/cabecalho.css">
   </head>
   <body>

     <header class="cabecalho">
       <a href="index.html">
-        <̶i̶m̶g̶ s̶r̶c̶=̶"̶i̶m̶g̶/̶m̶u̶s̶i̶c̶d̶o̶t̶-̶l̶o̶g̶o̶-̶l̶i̶g̶h̶t̶.̶s̶v̶g̶"̶ t̶i̶t̶l̶e̶=̶"̶I̶r̶ p̶a̶r̶a̶ a̶ p̶á̶g̶i̶n̶a̶ i̶n̶i̶c̶i̶a̶l̶ d̶a̶ M̶u̶s̶i̶c̶d̶o̶t̶"̶ a̶l̶t̶=
"̶M̶u̶s̶i̶c̶d̶o̶t̶"̶>

+        <img class="cabecalho__logo" src="img/musicdot-logo-light.svg" title="Ir para a página i
nicial da Musicdot" alt="Musicdot">

       </a>

       <nav>
-        <̶u̶l̶>
-          <̶l̶i̶>̶ <̶a̶ h̶r̶e̶f̶=̶"̶s̶o̶b̶r̶e̶.̶h̶t̶m̶l̶#̶c̶o̶n̶t̶a̶t̶o̶"̶>̶ C̶o̶n̶t̶a̶t̶o̶ </̶a̶>̶ </̶l̶i̶>
-          <̶l̶i̶>̶ <̶a̶ h̶r̶e̶f̶=̶"̶#̶"̶>̶ E̶n̶t̶r̶a̶r̶ </̶a̶>̶ </̶l̶i̶>
-          <̶l̶i̶>̶ <̶a̶ h̶r̶e̶f̶=̶"̶#̶"̶>̶ M̶a̶t̶r̶i̶c̶u̶l̶e̶-̶s̶e̶ </̶a̶>̶ </̶l̶i̶>
+        <ul class="cabecalho__menu">
+          <li class="cabecalho__item-menu"> <a href="sobre.html#contato"> Contato </a> </li>
+          <li class="cabecalho__item-menu"> <a href="#"> Entrar </a> </li>
+          <li class="cabecalho__item-menu"> <a href="#"> Matricule-se </a> </li>
         </ul>
       </nav>
     </header>

     <main>

**# index.html**

**148** 
33.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

       Conteúdo principal
     </main>

     <footer>
       Rodapé
     </footer>
   </body>
 </html>

33.2 PASSO A PASSO COM CÓDIGO 
**149**


--------------------------------------------------

CAPÍTULO 34

Vimos algumas maneiras de manipular posicionamento de elementos como 
 display:

inline/block/inline-block ,  margin:  e  text-align , mas todas essas maneiras são muito

"**rígidas**" na hora de distribuir elementos na página. Nós conseguimos posicionar com uma certa
precisão os elementos na tela, mas esse posicionamento é muito fixo no sentido de que se o *container* ou

a tela mudar de tamanho, os elementos não vão ter seu posicionamento adaptado. Tudo precisa ser
sempre milimetricamente calculado para que o restante dos elementos dispostos na tela não sejam

afetados pelas mudanças de dimensões.

Pensando nessa flexibilidade de posicionamento, as pessoas desenvolvedoras criaram um novo tipo

de  display : o  display: flex; .

O  display: flex funciona de uma maneira diferente dos outros displays. Quando colocamos essa

propriedade em um elemento, esse elemento se torna um ***flex container***, a partir daí podemos manipular
todos os elementos filhos desse ***flex container*** com propriedades novas. Essas propriedades devem ser
usadas no elemento que é um flex container.

Por padrão, quando aplicamos  display: flex  para um elemento, todos os filhos ficam um do

lado do outro como se estivessem sob o efeito de  display: inline .

 justify-content :

Essa prorpiedade ajusta horizontalmente os elementos filhos do **flex container**

**flex-start**: É o valor padrão. Os elementos ficam grudados um do lado do outro à esquerda do

flex container.

**flex-end**: Os elementos ficam grudados um do lado do outro à direita do flex container.

**center**: Os elementos ficam grudados um do lado do outro no meio do flex container.

# DISPLAY FLEX

## 34.1 FLEX CONTAINER

**### Propriedades de um Flex Container**

**150** 
33 DISPLAY FLEX


--------------------------------------------------

**space-between**: O primeiro elemento fica totalmente à esquerda do flex container e o último fica
totalmente à direita. O restante dos elementos ficam distribuídos com um espaçamento igual
entre eles.

**space-around**: Cada elemento fica com um espaçamento igual **em volta** dele mesmo. Isso quer
dizer que o primeiro elemento vai ter um espaçamento maior à direita do que à esquerda porque

vai somar com o espaçamento à esquerda do segundo elemento.
**space-evenly**: Corrige o "problema" do valor acima. Os elementos terão um espaçamento igual
em ambos os lados.

 align-items :

Essa propriedade ajusta verticalmente os elementos filhos do **flex container**

**stretch**: É o valor padrão. Os elementos se "esticam" para que todos fiquem com a mesma altura.

**flex-start**: Os elementos ficam todos alinhados com o topo do flex container.
**flex-end**: Os elementos ficam todos alinhados com a base do flex container.

**center**: Os elementos ficam todos alinhados com o meio do flex container.

**baseline**: Os elementos ficam alinhados com base do conteúdo textual de cada um deles.

 flex-wrap :

Essa propriedade trabalha com a "quebra de linha" dos elementos em linha.

**nowrap**: É o valor padrão. Os elementos vão ficar um do lado do outro mesmo que não exista

mais espaço horizontal.

**wrap**: Os elementos que não cabem mais no espaço lateral recebem uma quebra de linha, ou
seja, vão para a linha debaixo.
**wrap-reverse**: Os elementos que não cabem mais no espaço lateral recebem uma quebra de
linha acima, ou seja, vão para a linha de cima.

A **Alura** oferece centenas de **cursos online** em sua plataforma exclusiva de
ensino que favorece o aprendizado com a **qualidade** reconhecida da Caelum.

Você pode escolher um curso nas áreas de Programação, Front-end, Mobile,
Design & UX, Infra, Business, entre outras, com um plano que dá acesso a todos os cursos. Ex-
estudante da Caelum tem 10% de desconto neste link!

Conheça os cursos online Alura.

**Já conhece os cursos online Alura?**

34.1 FLEX CONTAINER 
**151**


--------------------------------------------------

CAPÍTULO 35

Com a nova ideia de layouts mais declarativos com Flexbox, faremos com que os itens do menu do

cabeçalho sejam distribuídos igualmente por toda largura do cabeçalho. As margem horizontal entre os
itens deixará de ser fixa:

Figura 35.1: Itens do menu igualmente espaçados na horizontal

Querendo aprender ainda mais sobre? Esclarecer dúvidas dos exercícios? Ouvir

explicações detalhadas com um instrutor?

A Caelum oferece o **curso data** presencial nas cidades de São Paulo, Rio de
Janeiro e Brasília, além de turmas incompany.

Consulte as vantagens do curso *Desenvolvimento Web com HTML, CSS e*
*JavaScript*

# EXERCÍCIO: NOVOS LAYOUTS COM
# FLEXBOX

## 35.1 OBJETIVO

**Você pode também fazer o curso data dessa apostila na Caelum**

**152** 
34 EXERCÍCIO: NOVOS LAYOUTS COM FLEXBOX


--------------------------------------------------

1. No arquivo ** cabecalho.css **na pasta ** css **faça as seguintes alterações:

 .cabecalho {
   text-align: center;
   font-size: 0.6rem;
   font-weight: bold;
   text-transform: uppercase;
   letter-spacing: 0.23em;

   color: #fff;
   background-color: #2D5377;
 }

 .cabecalho__logo {
   padding: 1.5em 0;
   width: 14.5em;
 }

 .cabecalho__menu {
+  display: flex;
+  justify-content: space-evenly;
+  flex-wrap: wrap;
+
   background-color: #272B3A87;
 }

 .cabecalho__item-menu {
   display: inline-block;
 }

 .cabecalho__item-menu a {
   display: inline-block;
   padding: 1.86em 1.42em;
 }

## 35.2 PASSO A PASSO COM CÓDIGO

**# css/cabecalho.css**

35.2 PASSO A PASSO COM CÓDIGO 
**153**


--------------------------------------------------

CAPÍTULO 36

Ainda com a nova ideia de layouts mais declarativos com Flexbox, faremos com que em telas com

larguras a partir de ** 640px ** o logo e o menu fiquem um do lado do outro com o máximo de espaço

possível entre eles. O logo ficaria o máximo possível para a direita e o menu o máximo possível para a
esquerda. Dizemos que eles ficarão justificados:

Figura 36.1: Logo e menu alinhados e justificados na horizontal

Querendo aprender ainda mais sobre? Esclarecer dúvidas dos exercícios? Ouvir
explicações detalhadas com um instrutor?
A Caelum oferece o **curso data** presencial nas cidades de São Paulo, Rio de
Janeiro e Brasília, além de turmas incompany.

Consulte as vantagens do curso *Desenvolvimento Web com HTML, CSS e*
*JavaScript*

1. No arquivo ** cabecalho.css **na pasta ** css **faça as seguintes alterações:

# EXERCÍCIO: NOVOS LAYOUTS COM
# FLEXBOX B

## 36.1 OBJETIVO

**Você pode também fazer o curso data dessa apostila na Caelum**

## 36.2 PASSO A PASSO COM CÓDIGO

**154** 
35 EXERCÍCIO: NOVOS LAYOUTS COM FLEXBOX B


--------------------------------------------------

 .cabecalho {
   text-align: center;
   font-size: 0.6rem;
   font-weight: bold;
   text-transform: uppercase;
   letter-spacing: 0.23em;

   color: #fff;
   background-color: #2D5377;
 }

 .cabecalho__logo {
   padding: 1.5em 0;
   width: 14.5em;
 }

 .cabecalho__menu {
   display: flex;
   justify-content: space-evenly;
   flex-wrap: wrap;

   background-color: #272B3A87;
 }

 .cabecalho__item-menu {
   display: inline-block;
 }

 .cabecalho__item-menu a {
   display: inline-block;
   padding: 1.86em 1.42em;
 }
+
+@media (min-width: 640px) {
+  .cabecalho {
+    padding: 0 5%;
+    display: flex;
+    justify-content: space-between;
+    align-items: center;
+  }
+
+  .cabecalho__logo {
+    padding: 2.5em 0;
+  }
+
+  .cabecalho__menu {
+    background-color: transparent; 
+  }
+}

**# css/cabecalho.css**

36.2 PASSO A PASSO COM CÓDIGO 
**155**


--------------------------------------------------

CAPÍTULO 37

Vamos acabar encontrando casos de incompatibilidade de propriedades CSS com os browsers que

usamos. Nem todas as pessoas atualizam seus browsers, seja por não saber atualizar, por uma feature
específica daquela versão, compatibilidade com o sistema operacional, etc... por conta disso, algumas
propriedades CSS que usamos não vão funcionar em todos os browsers. Vimos em capítulos anteriores

que o site caniuse.com mostra um gráfico falando sobre compatibilidade de propriedades CSS com
diversas versões de browsers, e a idéia de usar esse site é por conta das métricas que ele nos apresenta.
Uma dessas métricas é a quantidade de usuários utilizando versões diferentes de browsers. Vamos

montar nosso site pensando na maioria dos usuários (que costumam usar versões mais atualizadas de
browsers) mas não esquecendo das pequenas porcentagens que usam navegadores mais antigos (IE 10
por exemplo). Só que não podemos deixar de colocar novas propriedades e tags por conta da pequena

porcentagem de pessoas que usam navegadores muito antigos. O que fazemos então?

Vamos ver o exemplo baixo:

.meu-elemento {

   background-color: #f00;
}

No exemplo nós colocamos uma cor de fundo vermelha num elemento que possui a classe  meu-

elemento . Agora vamos observar o exemplo abaixo:

.meu-elemento {

   background-color: #f00;
   background-color: #0f0;
}

Agora o navegador vai ler primeiro a cor vermelha e depois vai substituir pela cor verde porque
estamos usando a mesma propriedade no mesmo elemento, ou seja, quem for declarado por último

ganha a preferência. Agora vamos ver mais um exemplo.

.meu-elemento {

   background-color: #f00;
   background-color: corlinda(10);
}

A função  corlinda() não é um CSS válido portanto o navegador vai ler a cor vermelha primeiro e

depois vai tentar ler a função, mas como essa função não existe o navegador vai ignorar a sobrescrita e

vai manter a cor de fundo vermelha.

# RESPONSIVIDADE E FALLBACK

**156** 
36 RESPONSIVIDADE E FALLBACK


--------------------------------------------------

Essa é a maneira mais ideal de manter compatibilidade com browsers mais antigos. Seguindo o
conceito de Progressive Enhancement, começamos a colocar nossas propriedades baseadas nos
navegadores mais antigos e depois vamos crescendo para propriedades mais novas de navegadores mais

novos, assim naturalmente vamos deixando nosso site responsivo e compatível com diversos
navegadores.

É importante ver que na hora de decidir qual propriedade antiga usar como "piso" da progressão,

essa propriedade faça sentido para a época que o site for criado.

Não vamos usar propriedades do *Internet Explorer 6* porque já é um navegador extremamente
velho e que não apresenta mais pacotes de segurança para o uso na internet. Mas podemos

considerar o *Internet Explorer 11* que ainda possui uma quantidade de usuários considerável.

36 RESPONSIVIDADE E FALLBACK 
**157**


--------------------------------------------------

CAPÍTULO 38

Em telas grandes e com alta resolução, o padding horizontal em porcentagem que colocamos no

cabeçalho pode não ser o suficiente e acabaremos com um cabeçalho largo demais:

Figura 38.1: Cabeçalho muito largo em telas com alta resolução

Para solucionar esse problema calcularemos um padding dinâmico, que garantirá que o conteúdo do
cabeçalho ocupará sempre no máximo ** 960px **, isso para qualquer tela maior que ** 1066px **.

Outro ponto que podemos melhorar é dando um destaque para o item "Matricule-se" do menu.
Deixaremos ele com o fundo vermelho ** #e93d50 **, com um espaçamento à esquerda de ** 1.42em ** e uma

borda redonda com raio de ** 6px **.

# EXERCÍCIO: RESPONSIVIDADE E
# FALLBACK

## 38.1 OBJETIVO

**158** 
37 EXERCÍCIO: RESPONSIVIDADE E FALLBACK


--------------------------------------------------

Figura 38.2: Resultado final em telas grandes

Conheça a **Casa do Código**, uma **nova** editora, com autores de destaque no
mercado, foco em **ebooks** (PDF, epub, mobi), preços **imbatíveis** e assuntos

**atuais**.
Com a curadoria da **Caelum** e excelentes autores, é uma abordagem **diferente**
para livros de tecnologia no Brasil.

Casa do Código, Livros de Tecnologia.

1. No arquivo ** cabecalho.css **na pasta ** css **faça as seguintes alterações:

 .cabecalho {
   text-align: center;
   font-size: 0.6rem;
   font-weight: bold;
   text-transform: uppercase;
   letter-spacing: 0.23em;

   color: #fff;
   background-color: #2D5377;
 }

 .cabecalho__logo {
   padding: 1.5em 0;

**Seus livros de tecnologia parecem do século passado?**

## 38.2 PASSO A PASSO COM CÓDIGO

**# css/cabecalho.css**

38.2 PASSO A PASSO COM CÓDIGO 
**159**


--------------------------------------------------

   width: 14.5em;
 }

 .cabecalho__menu {
   display: flex;
   justify-content: space-evenly;
   flex-wrap: wrap;

   background-color: #272B3A87;
 }

 .cabecalho__item-menu {
   display: inline-block;
 }

 .cabecalho__item-menu a {
   display: inline-block;
   padding: 1.86em 1.42em;
 }

 @media (min-width: 640px) {
   .cabecalho {
     padding: 0 5%;
     display: flex;
     justify-content: space-between;
     align-items: center;
   }

   .cabecalho__logo {
     padding: 2.5em 0;
   }

   .cabecalho__menu {
     background-color: transparent; 
   }
 }
+
+@media (min-width: 770px) {
+  .cabecalho__item-menu--matricular {
+    margin-left: 1.42em;
+
+    border-radius: 6px;
+    background-color: #e93d50;
+  }
+
+  .cabecalho__item-menu--matricular a {
+    padding: 1.8em 3.5em;
+  }
+}
+
+@media (min-width: 1066px) {
+  .cabecalho {
+    padding-left: calc((100% - 960px) / 2);
+    padding-right: calc((100% - 960px) / 2);
+  }
+}

2. No arquivo ** index.html **na pasta ** raíz do projeto **faça as seguintes alterações:

 *<!doctype html>*

**# index.html**

**160** 
38.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

 <html>
   <head>
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width">
     <title>Musicdot</title>
     <link rel="icon" href="img/favicon.ico">
     <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:300,400,500,
600,700,&display=block">

     <link rel="stylesheet" href="css/reset.css">
     <link rel="stylesheet" href="css/cabecalho.css">
   </head>
   <body>

     <header class="cabecalho">
       <a href="index.html">
         <img class="cabecalho__logo" src="img/musicdot-logo-light.svg" title="Ir para a página i
nicial da Musicdot" alt="Musicdot">

       </a>

       <nav>
         <ul class="cabecalho__menu">
           <li class="cabecalho__item-menu"> <a href="sobre.html#contato"> Contato </a> </li>
           <li class="cabecalho__item-menu"> <a href="#"> Entrar </a> </li>
-          <̶l̶i̶ c̶l̶a̶s̶s̶=̶"̶c̶a̶b̶e̶c̶a̶l̶h̶o̶_̶_̶i̶t̶e̶m̶-̶m̶e̶n̶u̶"̶>̶ <̶a̶ h̶r̶e̶f̶=̶"̶#̶"̶>̶ M̶a̶t̶r̶i̶c̶u̶l̶e̶-̶s̶e̶ </̶a̶>̶ </̶l̶i̶>
+          <li class="cabecalho__item-menu cabecalho__item-menu--matricular"> <a href="#"> Matric
ule-se </a> </li>

         </ul>
       </nav>
     </header>

     <main>
       Conteúdo principal
     </main>

     <footer>
       Rodapé
     </footer>
   </body>
 </html>

38.2 PASSO A PASSO COM CÓDIGO 
**161**


--------------------------------------------------

CAPÍTULO 39

Agora iremos para o final da página e começaremos a construir o rodapé da página principal. No celular

essa será aparência final dele:

Figura 39.1: O rodapé no celular, já estilizado

Nesse momento não se preocupe com o estilo e escolha as tags mais semânticas que conseguir se

# EXERCÍCIO: DESAFIO: CRIE O HTML DO
# RODAPÉ

## 39.1 OBJETIVO

**162** 
38 EXERCÍCIO: DESAFIO: CRIE O HTML DO RODAPÉ


--------------------------------------------------

lembrar para cada parte do conteúdo do rodapé, se tiver dúvidas sobre quais tags usar, sinta-se a vontade
para discutir com colegas da turma ou perguntar para quem estiver te dando o curso.

Figura 39.2: Resultado do rodapé sem estilos

Se você está gostando dessa apostila, certamente vai aproveitar os **cursos**
**online** que lançamos na plataforma **Alura**. Você estuda a qualquer momento
com a **qualidade** Caelum. Programação, Mobile, Design, Infra, Front-End e

Business, entre outros! Ex-estudante da Caelum tem 10% de desconto, siga o link!

Conheça a Alura Cursos Online.

**Agora é a melhor hora de aprender algo novo**

## 39.2 PASSO A PASSO COM CÓDIGO

39.2 PASSO A PASSO COM CÓDIGO 
**163**


--------------------------------------------------

1. No arquivo ** index.html **na pasta ** raíz do projeto **faça as seguintes alterações:

 *<!doctype html>*
 <html>
   <head>
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width">
     <title>Musicdot</title>
     <link rel="icon" href="img/favicon.ico">
     <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:300,400,500,
600,700,&display=block">

     <link rel="stylesheet" href="css/reset.css">
     <link rel="stylesheet" href="css/cabecalho.css">
   </head>
   <body>

     <header class="cabecalho">
       <a href="index.html">
         <img class="cabecalho__logo" src="img/musicdot-logo-light.svg" title="Ir para a página i
nicial da Musicdot" alt="Musicdot">

       </a>

       <nav>
         <ul class="cabecalho__menu">
           <li class="cabecalho__item-menu"> <a href="sobre.html#contato"> Contato </a> </li>
           <li class="cabecalho__item-menu"> <a href="#"> Entrar </a> </li>
           <li class="cabecalho__item-menu cabecalho__item-menu--matricular"> <a href="#"> Matric
ule-se </a> </li>

         </ul>
       </nav>
     </header>

     <main>
       Conteúdo principal
     </main>

     <footer>
-      R̶o̶d̶a̶p̶é̶
+      <section>
+        <img src="img/logo.svg" alt="Logo da MusicDot">
+
+        <p>
+          AOVS Sistemas de Informática S.A.
+          <br>
+          CNPJ 05.555.382/0001-33 
+          <br>
+          Rua Vergueiro - São Paulo/SP
+          <br>
+          Telefone (11) 4118-3319
+        </p>
+
+        <ul>
+          <li>
+            <a href="https://www.facebook.com/musicdotonline">
+              <img src="img/footer-icone-facebook.svg" alt="MusicDot no Facebook">
+            </a>
+          </li>
+          <li>
+            <a href="https://www.youtube.com/user/musicdotonline">

**# index.html**

**164** 
39.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

+              <img src="img/footer-icone-youtube.svg" alt="MusicDot no YouTube">
+            </a>
+          </li>
+          <li>
+            <a href="https://www.instagram.com/musicdotonline/">
+              <img src="img/footer-icone-instagram.svg" alt="Instagram">
+            </a>
+          </li>
+        </ul>
+      </section>
+
+      <section>
+        <h2> Cursos da MusicDot </h2>
+        <nav>
+          <ul>
+            <li><a href="#">Cursos de Teclado & Piano</a></li>
+            <li><a href="#">Cursos de Violão/Guitarra</a></li>
+            <li><a href="#">Cursos de Baixo</a></li>
+            <li><a href="#">Cursos de Bateria</a></li>
+            <li><a href="#">Cursos de Percussão</a></li>
+            <li><a href="#">Cursos de Canto</a></li>
+            <li><a href="#">Cursos de Áudio</a></li>
+            <li><a href="#">Cursos de Teoria</a></li>
+            <li><a href="#">Cursos de Sopro</a></li>
+            <li><a href="#">Cursos de Cordas</a></li>
+          </ul>
+        </nav>
+      </section>
+
+      <section>
+        <h2> MusicDot </h2>
+        <nav>
+          <ul>
+            <li><a href="#">Apostila</a></li>
+            <li><a href="#">E-book</a></li>
+            <li><a href="#">Login</a></li>
+            <li><a href="#">Matricule-se</a></li>
+            <li><a href="#">Perguntas frequentes</a></li>
+            <li><a href="#">Para Escolas</a></li>
+            <li><a href="#">Contato</a></li>
+          </ul>
+        </nav>
+      </section>
+
     </footer>
   </body>
 </html>

39.2 PASSO A PASSO COM CÓDIGO 
**165**


--------------------------------------------------

CAPÍTULO 40

Seguindo a risca a ideia do Progressive Enhancement, iniciaremos os estilos do rodapé pelo estilo do

conteúdo de texto e imagens.

Replicaremos o seguinte estilo do rodapé:

Figura 40.1: Estilo apenas do conteúdo, sem espaçamentos

# EXERCÍCIO: CONTEÚDO RODAPÉ

## 40.1 OBJETIVO

**166** 
39 EXERCÍCIO: CONTEÚDO RODAPÉ


--------------------------------------------------

Editoras tradicionais pouco ligam para ebooks e novas tecnologias. Não dominam

tecnicamente o assunto para revisar os livros a fundo. Não têm anos de

experiência em didáticas com cursos.

Conheça a **Casa do Código**, uma editora diferente, com curadoria da **Caelum** e

obsessão por livros de qualidade a preços justos.

Casa do Código, ebook com preço de ebook.

1. Crie o arquivo ** rodape.css **na pasta ** css **com o seguinte código:

+.rodape {
+  text-align: center;
+  font-size: 0.7rem;
+}
+
+.rodape__logo {
+  width: 11.25em;
+}
+
+.rodape__lista-midias-sociais {
+  display: flex;
+  justify-content: center;
+}
+
+.rodape__item-midias-sociais {
+  width: 2.62em;
+}
+
+.rodape__item-midias-sociais img {
+  width: 100%;
+}
+
+.rodape__titulo {
+  font-size: 1.45em;
+  font-weight: bold;
+  text-transform: uppercase;
+}
+
+.rodape_item-lista {  
+  font-weight: 500;
+}

**Editora Casa do Código com livros de uma forma diferente**

## 40.2 PASSO A PASSO COM CÓDIGO

**# css/rodape.css**

40.2 PASSO A PASSO COM CÓDIGO 
**167**


--------------------------------------------------

2. No arquivo ** index.html **na pasta ** raíz do projeto **faça as seguintes alterações:

 *<!doctype html>*
 <html>
   <head>
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width">
     <title>Musicdot</title>
     <link rel="icon" href="img/favicon.ico">
     <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:300,400,500,
600,700,&display=block">

     <link rel="stylesheet" href="css/reset.css">
     <link rel="stylesheet" href="css/cabecalho.css">
+    <link rel="stylesheet" href="css/rodape.css">
   </head>
   <body>

     <header class="cabecalho">
       <a href="index.html">
         <img class="cabecalho__logo" src="img/musicdot-logo-light.svg" title="Ir para a página i
nicial da Musicdot" alt="Musicdot">

       </a>

       <nav>
         <ul class="cabecalho__menu">
           <li class="cabecalho__item-menu"> <a href="sobre.html#contato"> Contato </a> </li>
           <li class="cabecalho__item-menu"> <a href="#"> Entrar </a> </li>
           <li class="cabecalho__item-menu cabecalho__item-menu--matricular"> <a href="#"> Matric
ule-se </a> </li>

         </ul>
       </nav>
     </header>

     <main>
       Conteúdo principal
     </main>

-    <̶f̶o̶o̶t̶e̶r̶>
+    <footer class="rodape">
       <section>
-        <̶i̶m̶g̶ s̶r̶c̶=̶"̶i̶m̶g̶/̶l̶o̶g̶o̶.̶s̶v̶g̶"̶ a̶l̶t̶=̶"̶L̶o̶g̶o̶ d̶a̶ M̶u̶s̶i̶c̶D̶o̶t̶"̶>
+        <img class="rodape__logo" src="img/logo.svg" alt="Logo da MusicDot">

         <p>
           AOVS Sistemas de Informática S.A.
           <br>
           CNPJ 05.555.382/0001-33 
           <br>
           Rua Vergueiro - São Paulo/SP
           <br>
           Telefone (11) 4118-3319
         </p>

-        <̶u̶l̶>
-          <̶l̶i̶>
+        <ul class="rodape__lista-midias-sociais">
+          <li class="rodape__item-midias-sociais">
             <a href="https://www.facebook.com/musicdotonline">
               <img src="img/footer-icone-facebook.svg" alt="MusicDot no Facebook">

**# index.html**

**168** 
40.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

             </a>
           </li>
-          <̶l̶i̶>
+          <li class="rodape__item-midias-sociais">
             <a href="https://www.youtube.com/user/musicdotonline">
               <img src="img/footer-icone-youtube.svg" alt="MusicDot no YouTube">
             </a>
           </li>
-          <̶l̶i̶>
+          <li class="rodape__item-midias-sociais">
             <a href="https://www.instagram.com/musicdotonline/">
               <img src="img/footer-icone-instagram.svg" alt="Instagram">
             </a>
           </li>
         </ul>
       </section>

       <section>
-        <̶h̶2̶>̶ C̶u̶r̶s̶o̶s̶ d̶a̶ M̶u̶s̶i̶c̶D̶o̶t̶ </̶h̶2̶>
+        <h2 class="rodape__titulo"> Cursos da MusicDot </h2>
         <nav>
           <ul>
-            <̶l̶i̶>̶<̶a̶ h̶r̶e̶f̶=̶"̶#̶"̶>̶C̶u̶r̶s̶o̶s̶ d̶e̶ T̶e̶c̶l̶a̶d̶o̶ &̶ P̶i̶a̶n̶o̶</̶a̶>̶</̶l̶i̶>
-            <̶l̶i̶>̶<̶a̶ h̶r̶e̶f̶=̶"̶#̶"̶>̶C̶u̶r̶s̶o̶s̶ d̶e̶ V̶i̶o̶l̶ã̶o̶/̶G̶u̶i̶t̶a̶r̶r̶a̶</̶a̶>̶</̶l̶i̶>
-            <̶l̶i̶>̶<̶a̶ h̶r̶e̶f̶=̶"̶#̶"̶>̶C̶u̶r̶s̶o̶s̶ d̶e̶ B̶a̶i̶x̶o̶</̶a̶>̶</̶l̶i̶>
-            <̶l̶i̶>̶<̶a̶ h̶r̶e̶f̶=̶"̶#̶"̶>̶C̶u̶r̶s̶o̶s̶ d̶e̶ B̶a̶t̶e̶r̶i̶a̶</̶a̶>̶</̶l̶i̶>
-            <̶l̶i̶>̶<̶a̶ h̶r̶e̶f̶=̶"̶#̶"̶>̶C̶u̶r̶s̶o̶s̶ d̶e̶ P̶e̶r̶c̶u̶s̶s̶ã̶o̶</̶a̶>̶</̶l̶i̶>
-            <̶l̶i̶>̶<̶a̶ h̶r̶e̶f̶=̶"̶#̶"̶>̶C̶u̶r̶s̶o̶s̶ d̶e̶ C̶a̶n̶t̶o̶</̶a̶>̶</̶l̶i̶>
-            <̶l̶i̶>̶<̶a̶ h̶r̶e̶f̶=̶"̶#̶"̶>̶C̶u̶r̶s̶o̶s̶ d̶e̶ Á̶u̶d̶i̶o̶</̶a̶>̶</̶l̶i̶>
-            <̶l̶i̶>̶<̶a̶ h̶r̶e̶f̶=̶"̶#̶"̶>̶C̶u̶r̶s̶o̶s̶ d̶e̶ T̶e̶o̶r̶i̶a̶</̶a̶>̶</̶l̶i̶>
-            <̶l̶i̶>̶<̶a̶ h̶r̶e̶f̶=̶"̶#̶"̶>̶C̶u̶r̶s̶o̶s̶ d̶e̶ S̶o̶p̶r̶o̶</̶a̶>̶</̶l̶i̶>
-            <̶l̶i̶>̶<̶a̶ h̶r̶e̶f̶=̶"̶#̶"̶>̶C̶u̶r̶s̶o̶s̶ d̶e̶ C̶o̶r̶d̶a̶s̶</̶a̶>̶</̶l̶i̶>
+            <li class="rodape_item-lista"><a href="#">Cursos de Teclado & Piano</a></li>
+            <li class="rodape_item-lista"><a href="#">Cursos de Violão/Guitarra</a></li>
+            <li class="rodape_item-lista"><a href="#">Cursos de Baixo</a></li>
+            <li class="rodape_item-lista"><a href="#">Cursos de Bateria</a></li>
+            <li class="rodape_item-lista"><a href="#">Cursos de Percussão</a></li>
+            <li class="rodape_item-lista"><a href="#">Cursos de Canto</a></li>
+            <li class="rodape_item-lista"><a href="#">Cursos de Áudio</a></li>
+            <li class="rodape_item-lista"><a href="#">Cursos de Teoria</a></li>
+            <li class="rodape_item-lista"><a href="#">Cursos de Sopro</a></li>
+            <li class="rodape_item-lista"><a href="#">Cursos de Cordas</a></li>
           </ul>
         </nav>
       </section>

       <section>
-        <̶h̶2̶>̶ M̶u̶s̶i̶c̶D̶o̶t̶ </̶h̶2̶>
+        <h2 class="rodape__titulo"> MusicDot </h2>
         <nav>
           <ul>
-            <̶l̶i̶>̶<̶a̶ h̶r̶e̶f̶=̶"̶#̶"̶>̶A̶p̶o̶s̶t̶i̶l̶a̶</̶a̶>̶</̶l̶i̶>
-            <̶l̶i̶>̶<̶a̶ h̶r̶e̶f̶=̶"̶#̶"̶>̶E̶-̶b̶o̶o̶k̶</̶a̶>̶</̶l̶i̶>
-            <̶l̶i̶>̶<̶a̶ h̶r̶e̶f̶=̶"̶#̶"̶>̶L̶o̶g̶i̶n̶</̶a̶>̶</̶l̶i̶>
-            <̶l̶i̶>̶<̶a̶ h̶r̶e̶f̶=̶"̶#̶"̶>̶M̶a̶t̶r̶i̶c̶u̶l̶e̶-̶s̶e̶</̶a̶>̶</̶l̶i̶>
-            <̶l̶i̶>̶<̶a̶ h̶r̶e̶f̶=̶"̶#̶"̶>̶P̶e̶r̶g̶u̶n̶t̶a̶s̶ f̶r̶e̶q̶u̶e̶n̶t̶e̶s̶</̶a̶>̶</̶l̶i̶>
-            <̶l̶i̶>̶<̶a̶ h̶r̶e̶f̶=̶"̶#̶"̶>̶P̶a̶r̶a̶ E̶s̶c̶o̶l̶a̶s̶</̶a̶>̶</̶l̶i̶>
-            <̶l̶i̶>̶<̶a̶ h̶r̶e̶f̶=̶"̶#̶"̶>̶C̶o̶n̶t̶a̶t̶o̶</̶a̶>̶</̶l̶i̶>
+            <li class="rodape_item-lista"><a href="#">Apostila</a></li>
+            <li class="rodape_item-lista"><a href="#">E-book</a></li>
+            <li class="rodape_item-lista"><a href="#">Login</a></li>
+            <li class="rodape_item-lista"><a href="#">Matricule-se</a></li>
+            <li class="rodape_item-lista"><a href="#">Perguntas frequentes</a></li>

40.2 PASSO A PASSO COM CÓDIGO 
**169**


--------------------------------------------------

+            <li class="rodape_item-lista"><a href="#">Para Escolas</a></li>
+            <li class="rodape_item-lista"><a href="#">Contato</a></li>
           </ul>
         </nav>
       </section>

     </footer>
   </body>
 </html>

**170** 
40.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

CAPÍTULO 41

Agora calcularemos e adicionaremos todos os espaçamentos para que o rodapé fique assim:

Figura 41.1: Rodapé mobile com espaçamentos

# EXERCÍCIO: ESPAÇANDO O CONTEÚDO
# DO RODAPÉ - OS DETALHES NAS
# ENTRELINHAS E MARGENS

## 41.1 OBJETIVO

40 EXERCÍCIO: ESPAÇANDO O CONTEÚDO DO RODAPÉ - OS DETALHES NAS ENTRELINHAS E MARGENS 
**171**


--------------------------------------------------

Para treinar, tente calcular os espaçamentos sem saber o tamanho exato deles, através da imagem
acima é possível estimar os tamanhos como uma proporção do tamanho da fonte dos textos.

A **Alura** oferece centenas de **cursos online** em sua plataforma exclusiva de
ensino que favorece o aprendizado com a **qualidade** reconhecida da Caelum.
Você pode escolher um curso nas áreas de Programação, Front-end, Mobile,

Design & UX, Infra, Business, entre outras, com um plano que dá acesso a todos os cursos. Ex-
estudante da Caelum tem 10% de desconto neste link!

Conheça os cursos online Alura.

1. No arquivo ** rodape.css **na pasta ** css **faça as seguintes alterações:

 .rodape {
+  padding: 2em 5%;
+
   text-align: center;
   font-size: 0.7rem;
 }

 .rodape__logo {
   width: 11.25em;
+  margin-bottom: 1em;
 }

 .rodape__lista-midias-sociais {
   display: flex;
   justify-content: center;
 }

+.rodape__infos-empresa {
+  line-height: 1.5;
+}
+
+.rodape__secao + .rodape__secao {
+  margin-top: 2em;
+}
+
+.rodape__lista-midias-sociais {
+  display: flex;
+  justify-content: center;
+  margin-top: 1em;

**Já conhece os cursos online Alura?**

## 41.2 PASSO A PASSO COM CÓDIGO

**# css/rodape.css**

**172** 
41.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

+}
+
 .rodape__item-midias-sociais {
   width: 2.62em;
+  margin: 0 .25em;
 }

 .rodape__item-midias-sociais img {
   width: 100%;
 }

 .rodape__titulo {
+  margin-bottom: 1em;
+
   font-size: 1.45em;
   font-weight: bold;
   text-transform: uppercase;
 }

 .rodape_item-lista {  
   font-weight: 500;
+  margin: 0.625em 0;
 }

2. No arquivo ** index.html **na pasta ** raíz do projeto **faça as seguintes alterações:

 *<!doctype html>*
 <html>
   <head>
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width">
     <title>Musicdot</title>
     <link rel="icon" href="img/favicon.ico">
     <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:300,400,500,
600,700,&display=block">

     <link rel="stylesheet" href="css/reset.css">
     <link rel="stylesheet" href="css/cabecalho.css">
     <link rel="stylesheet" href="css/rodape.css">
   </head>
   <body>

     <header class="cabecalho">
       <a href="index.html">
         <img class="cabecalho__logo" src="img/musicdot-logo-light.svg" title="Ir para a página i
nicial da Musicdot" alt="Musicdot">

       </a>

       <nav>
         <ul class="cabecalho__menu">
           <li class="cabecalho__item-menu"> <a href="sobre.html#contato"> Contato </a> </li>
           <li class="cabecalho__item-menu"> <a href="#"> Entrar </a> </li>
           <li class="cabecalho__item-menu cabecalho__item-menu--matricular"> <a href="#"> Matric
ule-se </a> </li>

         </ul>
       </nav>
     </header>

     <main>
       Conteúdo principal
     </main>

**# index.html**

41.2 PASSO A PASSO COM CÓDIGO 
**173**


--------------------------------------------------

     <footer class="rodape">
-      <̶s̶e̶c̶t̶i̶o̶n̶>
+      <section class="rodape__secao">
         <img class="rodape__logo" src="img/logo.svg" alt="Logo da MusicDot">

-        <̶p̶>
+        <p class="rodape__infos-empresa">
           AOVS Sistemas de Informática S.A.
           <br>
           CNPJ 05.555.382/0001-33 
           <br>
           Rua Vergueiro - São Paulo/SP
           <br>
           Telefone (11) 4118-3319
         </p>

         <ul class="rodape__lista-midias-sociais">
           <li class="rodape__item-midias-sociais">
             <a href="https://www.facebook.com/musicdotonline">
               <img src="img/footer-icone-facebook.svg" alt="MusicDot no Facebook">
             </a>
           </li>
           <li class="rodape__item-midias-sociais">
             <a href="https://www.youtube.com/user/musicdotonline">
               <img src="img/footer-icone-youtube.svg" alt="MusicDot no YouTube">
             </a>
           </li>
           <li class="rodape__item-midias-sociais">
             <a href="https://www.instagram.com/musicdotonline/">
               <img src="img/footer-icone-instagram.svg" alt="Instagram">
             </a>
           </li>
         </ul>
       </section>

-      <̶s̶e̶c̶t̶i̶o̶n̶>
+      <section class="rodape__secao">
         <h2 class="rodape__titulo"> Cursos da MusicDot </h2>
         <nav>
           <ul>
             <li class="rodape_item-lista"><a href="#">Cursos de Teclado & Piano</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Violão/Guitarra</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Baixo</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Bateria</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Percussão</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Canto</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Áudio</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Teoria</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Sopro</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Cordas</a></li>
           </ul>
         </nav>
       </section>

-      <̶s̶e̶c̶t̶i̶o̶n̶>
+      <section class="rodape__secao">
         <h2 class="rodape__titulo"> MusicDot </h2>
         <nav>
           <ul>
             <li class="rodape_item-lista"><a href="#">Apostila</a></li>
             <li class="rodape_item-lista"><a href="#">E-book</a></li>
             <li class="rodape_item-lista"><a href="#">Login</a></li>

**174** 
41.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

             <li class="rodape_item-lista"><a href="#">Matricule-se</a></li>
             <li class="rodape_item-lista"><a href="#">Perguntas frequentes</a></li>
             <li class="rodape_item-lista"><a href="#">Para Escolas</a></li>
             <li class="rodape_item-lista"><a href="#">Contato</a></li>
           </ul>
         </nav>
       </section>

     </footer>
   </body>
 </html>

41.2 PASSO A PASSO COM CÓDIGO 
**175**


--------------------------------------------------

CAPÍTULO 42

Agora, adicionaremos um formulário no final do conteúdo do rodapé:

Figura 42.1: O formulário de newsletter do rodapé

# EXERCÍCIO: O FORMULÁRIO DE
# NEWSLETTER DO RODAPÉ

## 42.1 OBJETIVO

**176** 
41 EXERCÍCIO: O FORMULÁRIO DE NEWSLETTER DO RODAPÉ


--------------------------------------------------

Ess formulário terá apenas um campo de e-mail.

Lembre-se que por mais que não haja um rótulo/texto explicativo visível para o campo de email, ele
deve estar presente no HTML por questões semânticas. O rótulo deve estar presente no HTML e deve
ser removido apenas no estilo CSS.

Querendo aprender ainda mais sobre? Esclarecer dúvidas dos exercícios? Ouvir
explicações detalhadas com um instrutor?
A Caelum oferece o **curso data** presencial nas cidades de São Paulo, Rio de
Janeiro e Brasília, além de turmas incompany.

Consulte as vantagens do curso *Desenvolvimento Web com HTML, CSS e*

*JavaScript*

1. Crie o arquivo ** form-newsletter.css **na pasta ** css **com o seguinte código:

+.form-newsletter {
+  display: flex;
+  width: 100%;
+  overflow: hidden;
+  box-sizing: border-box;
+
+  border-radius: 7px;
+  border: 2px solid #e93d50;
+  background-color: #e93d50;
+}
+
+.form-newsletter__label {
+  position:absolute;
+  left:-10000px;
+  width:1px;
+  height:1px;
+  overflow:hidden;
+}
+
+.form-newsletter__campo {
+  padding: .6rem .4rem;
+  flex-grow: 1;
+  border: none;
+}
+

**Você pode também fazer o curso data dessa apostila na Caelum**

## 42.2 PASSO A PASSO COM CÓDIGO

**# css/form-newsletter.css**

42.2 PASSO A PASSO COM CÓDIGO 
**177**


--------------------------------------------------

+.form-newsletter__botao {
+  flex-grow: 1;
+  border: none;
+  
+  text-transform: uppercase;
+  font-weight: 600;
+
+  background-color: #e93d50;
+  color: #fff;
+}

2. No arquivo ** index.html **na pasta ** raíz do projeto **faça as seguintes alterações:

 *<!doctype html>*
 <html>
   <head>
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width">
     <title>Musicdot</title>
     <link rel="icon" href="img/favicon.ico">
     <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:300,400,500,
600,700,&display=block">

     <link rel="stylesheet" href="css/reset.css">
     <link rel="stylesheet" href="css/cabecalho.css">
     <link rel="stylesheet" href="css/rodape.css">
+    <link rel="stylesheet" href="css/form-newsletter.css">
   </head>
   <body>

     <header class="cabecalho">
       <a href="index.html">
         <img class="cabecalho__logo" src="img/musicdot-logo-light.svg" title="Ir para a página i
nicial da Musicdot" alt="Musicdot">

       </a>

       <nav>
         <ul class="cabecalho__menu">
           <li class="cabecalho__item-menu"> <a href="sobre.html#contato"> Contato </a> </li>
           <li class="cabecalho__item-menu"> <a href="#"> Entrar </a> </li>
           <li class="cabecalho__item-menu cabecalho__item-menu--matricular"> <a href="#"> Matric
ule-se </a> </li>

         </ul>
       </nav>
     </header>

     <main>
       Conteúdo principal
     </main>

     <footer class="rodape">
       <section class="rodape__secao">
         <img class="rodape__logo" src="img/logo.svg" alt="Logo da MusicDot">

         <p class="rodape__infos-empresa">
           AOVS Sistemas de Informática S.A.
           <br>
           CNPJ 05.555.382/0001-33 
           <br>
           Rua Vergueiro - São Paulo/SP
           <br>

**# index.html**

**178** 
42.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

           Telefone (11) 4118-3319
         </p>

         <ul class="rodape__lista-midias-sociais">
           <li class="rodape__item-midias-sociais">
             <a href="https://www.facebook.com/musicdotonline">
               <img src="img/footer-icone-facebook.svg" alt="MusicDot no Facebook">
             </a>
           </li>
           <li class="rodape__item-midias-sociais">
             <a href="https://www.youtube.com/user/musicdotonline">
               <img src="img/footer-icone-youtube.svg" alt="MusicDot no YouTube">
             </a>
           </li>
           <li class="rodape__item-midias-sociais">
             <a href="https://www.instagram.com/musicdotonline/">
               <img src="img/footer-icone-instagram.svg" alt="Instagram">
             </a>
           </li>
         </ul>
       </section>

       <section class="rodape__secao">
         <h2 class="rodape__titulo"> Cursos da MusicDot </h2>
         <nav>
           <ul>
             <li class="rodape_item-lista"><a href="#">Cursos de Teclado & Piano</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Violão/Guitarra</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Baixo</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Bateria</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Percussão</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Canto</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Áudio</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Teoria</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Sopro</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Cordas</a></li>
           </ul>
         </nav>
       </section>

       <section class="rodape__secao">
         <h2 class="rodape__titulo"> MusicDot </h2>
         <nav>
           <ul>
             <li class="rodape_item-lista"><a href="#">Apostila</a></li>
             <li class="rodape_item-lista"><a href="#">E-book</a></li>
             <li class="rodape_item-lista"><a href="#">Login</a></li>
             <li class="rodape_item-lista"><a href="#">Matricule-se</a></li>
             <li class="rodape_item-lista"><a href="#">Perguntas frequentes</a></li>
             <li class="rodape_item-lista"><a href="#">Para Escolas</a></li>
             <li class="rodape_item-lista"><a href="#">Contato</a></li>
           </ul>
         </nav>
       </section>

+      <section class="rodape__secao">
+        <h2 class="rodape__titulo"> 
+          Receba novidades e lançamentos 
+        </h2>
+
+        <form action="#" method="get" class="form-newsletter">
+          <label for="form-newsletter__label" class="form-newsletter__label">
+            Seu email pessoal

42.2 PASSO A PASSO COM CÓDIGO 
**179**


--------------------------------------------------

+          </label>
+          <input id="email-newsletter" name="email-newsletter" type="email" class="form-newslett
er__campo">

+          <button type="submit" class="form-newsletter__botao">
+            OK
+          </button>
+        </form>
+      </section>
     </footer>
   </body>
 </html>

**180** 
42.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

CAPÍTULO 43

Agora, em telas a partir de ** 640px ** precisamos alterar a disposição e a ordem em que os elementos do

HTML aparecem na tela. Podemos fazer isso sem alterar o HTML, utilizando apenas o Flexbox.

O resultado final será o seguinte:

Figura 43.1: Itens no rodapé com ordem diferente

# EXERCÍCIO: EMBARALHANDO OS ITENS
# DO RODAPÉ EM TELAS MAIORES COM
# FLEXBOX

## 43.1 OBJETIVO

42 EXERCÍCIO: EMBARALHANDO OS ITENS DO RODAPÉ EM TELAS MAIORES COM FLEXBOX 
**181**


--------------------------------------------------

Conheça a **Casa do Código**, uma **nova** editora, com autores de destaque no

mercado, foco em **ebooks** (PDF, epub, mobi), preços **imbatíveis** e assuntos
**atuais**.
Com a curadoria da **Caelum** e excelentes autores, é uma abordagem **diferente**

para livros de tecnologia no Brasil.

Casa do Código, Livros de Tecnologia.

1. No arquivo ** rodape.css **na pasta ** css **faça as seguintes alterações:

 .rodape {
   padding: 2em 5%;

   text-align: center;
   font-size: 0.7rem;
 }

 .rodape__logo {
   width: 11.25em;
   margin-bottom: 1em;
 }

 .rodape__lista-midias-sociais {
   display: flex;
   justify-content: center;
 }

 .rodape__infos-empresa {
   line-height: 1.5;
 }

-.̶r̶o̶d̶a̶p̶e̶_̶_̶s̶e̶c̶a̶o̶ +̶ .̶r̶o̶d̶a̶p̶e̶_̶_̶s̶e̶c̶a̶o̶ {̶
-  m̶a̶r̶g̶i̶n̶-̶t̶o̶p̶:̶ 2̶e̶m̶;̶
-}̶
-
 .rodape__lista-midias-sociais {
   display: flex;
   justify-content: center;
   margin-top: 1em;
 }

 .rodape__item-midias-sociais {
   width: 2.62em;

**Seus livros de tecnologia parecem do século passado?**

## 43.2 PASSO A PASSO COM CÓDIGO

**# css/rodape.css**

**182** 
43.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

   margin: 0 .25em;
 }

 .rodape__item-midias-sociais img {
   width: 100%;
 }

 .rodape__titulo {
   margin-bottom: 1em;

   font-size: 1.45em;
   font-weight: bold;
   text-transform: uppercase;
 }

 .rodape_item-lista {  
   font-weight: 500;
   margin: 0.625em 0;
 }
+
+@media (max-width: 640px) {
+  .rodape__secao + .rodape__secao {
+    margin-top: 2em;
+  }  
+}
+
+@media(min-width: 640px) {
+  .rodape {
+    display: flex;
+    flex-wrap: wrap;
+    justify-content: space-between;
+
+    font-size: 1rem;
+  }
+
+  .rodape__secao--sobre,
+  .rodape__secao--cursos,
+  .rodape__secao--links,
+  .rodape__secao--newsletter {
+    width: 45%;
+  }
+
+  .rodape__secao--cursos {
+    order: 1;
+    margin: 0;
+  }
+
+  .rodape__secao--links {
+    order: 2;
+    margin: 0;
+  }
+
+  .rodape__secao--sobre {
+    order: 3;
+    margin-top: 2em;
+  }
+
+  .rodape__secao--newsletter {
+    order: 4;
+    margin-top: 2em;
+  }
+}

43.2 PASSO A PASSO COM CÓDIGO 
**183**


--------------------------------------------------

2. No arquivo ** index.html **na pasta ** raíz do projeto **faça as seguintes alterações:

 *<!doctype html>*
 <html>
   <head>
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width">
     <title>Musicdot</title>
     <link rel="icon" href="img/favicon.ico">
     <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:300,400,500,
600,700,&display=block">

     <link rel="stylesheet" href="css/reset.css">
     <link rel="stylesheet" href="css/cabecalho.css">
     <link rel="stylesheet" href="css/rodape.css">
     <link rel="stylesheet" href="css/form-newsletter.css">
   </head>
   <body>

     <header class="cabecalho">
       <a href="index.html">
         <img class="cabecalho__logo" src="img/musicdot-logo-light.svg" title="Ir para a página i
nicial da Musicdot" alt="Musicdot">

       </a>

       <nav>
         <ul class="cabecalho__menu">
           <li class="cabecalho__item-menu"> <a href="sobre.html#contato"> Contato </a> </li>
           <li class="cabecalho__item-menu"> <a href="#"> Entrar </a> </li>
           <li class="cabecalho__item-menu cabecalho__item-menu--matricular"> <a href="#"> Matric
ule-se </a> </li>

         </ul>
       </nav>
     </header>

     <main>
       Conteúdo principal
     </main>

     <footer class="rodape">
-      <̶s̶e̶c̶t̶i̶o̶n̶ c̶l̶a̶s̶s̶=̶"̶r̶o̶d̶a̶p̶e̶_̶_̶s̶e̶c̶a̶o̶"̶>
+      <section class="rodape__secao rodape__secao--sobre">
         <img class="rodape__logo" src="img/logo.svg" alt="Logo da MusicDot">

         <p class="rodape__infos-empresa">
           AOVS Sistemas de Informática S.A.
           <br>
           CNPJ 05.555.382/0001-33 
           <br>
           Rua Vergueiro - São Paulo/SP
           <br>
           Telefone (11) 4118-3319
         </p>

         <ul class="rodape__lista-midias-sociais">
           <li class="rodape__item-midias-sociais">
             <a href="https://www.facebook.com/musicdotonline">
               <img src="img/footer-icone-facebook.svg" alt="MusicDot no Facebook">
             </a>
           </li>

**# index.html**

**184** 
43.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

           <li class="rodape__item-midias-sociais">
             <a href="https://www.youtube.com/user/musicdotonline">
               <img src="img/footer-icone-youtube.svg" alt="MusicDot no YouTube">
             </a>
           </li>
           <li class="rodape__item-midias-sociais">
             <a href="https://www.instagram.com/musicdotonline/">
               <img src="img/footer-icone-instagram.svg" alt="Instagram">
             </a>
           </li>
         </ul>
       </section>

-      <̶s̶e̶c̶t̶i̶o̶n̶ c̶l̶a̶s̶s̶=̶"̶r̶o̶d̶a̶p̶e̶_̶_̶s̶e̶c̶a̶o̶"̶>
+      <section class="rodape__secao rodape__secao--cursos">
         <h2 class="rodape__titulo"> Cursos da MusicDot </h2>
         <nav>
           <ul>
             <li class="rodape_item-lista"><a href="#">Cursos de Teclado & Piano</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Violão/Guitarra</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Baixo</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Bateria</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Percussão</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Canto</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Áudio</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Teoria</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Sopro</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Cordas</a></li>
           </ul>
         </nav>
       </section>

-      <̶s̶e̶c̶t̶i̶o̶n̶ c̶l̶a̶s̶s̶=̶"̶r̶o̶d̶a̶p̶e̶_̶_̶s̶e̶c̶a̶o̶"̶>
+      <section class="rodape__secao rodape__secao--links">
         <h2 class="rodape__titulo"> MusicDot </h2>
         <nav>
           <ul>
             <li class="rodape_item-lista"><a href="#">Apostila</a></li>
             <li class="rodape_item-lista"><a href="#">E-book</a></li>
             <li class="rodape_item-lista"><a href="#">Login</a></li>
             <li class="rodape_item-lista"><a href="#">Matricule-se</a></li>
             <li class="rodape_item-lista"><a href="#">Perguntas frequentes</a></li>
             <li class="rodape_item-lista"><a href="#">Para Escolas</a></li>
             <li class="rodape_item-lista"><a href="#">Contato</a></li>
           </ul>
         </nav>
       </section>

-      <̶s̶e̶c̶t̶i̶o̶n̶ c̶l̶a̶s̶s̶=̶"̶r̶o̶d̶a̶p̶e̶_̶_̶s̶e̶c̶a̶o̶"̶>
+      <section class="rodape__secao rodape__secao--newsletter">
         <h2 class="rodape__titulo"> 
           Receba novidades e lançamentos 
         </h2>

         <form action="#" method="get" class="form-newsletter">
           <label for="form-newsletter__label" class="form-newsletter__label">
             Seu email pessoal
           </label>
           <input id="email-newsletter" name="email-newsletter" type="email" class="form-newslett
er__campo">

           <button type="submit" class="form-newsletter__botao">
             OK
           </button>

43.2 PASSO A PASSO COM CÓDIGO 
**185**


--------------------------------------------------

         </form>
       </section>
     </footer>
   </body>
 </html>

**186** 
43.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

CAPÍTULO 44

Agora inplementaremos o estilo do rodapé em telas maiores ainda, a partir de ** 1200px **:

Figura 44.1: O rodapé desktop

Note que a disposição dos elementos difere bastante do estilo anterior. Só para sobrescrever esse
estilo anterior precisaríamos escrever bastanta código. Para evitar isso, podemos limitar o estilo anterior
para funcionar apenas em telas a partir de ** 640px **até telas de ** 1200px **.

Se você está gostando dessa apostila, certamente vai aproveitar os **cursos**
**online** que lançamos na plataforma **Alura**. Você estuda a qualquer momento

com a **qualidade** Caelum. Programação, Mobile, Design, Infra, Front-End e
Business, entre outros! Ex-estudante da Caelum tem 10% de desconto, siga o link!

Conheça a Alura Cursos Online.

# EXERCÍCIO: RODAPÉ EM TELAS
# GRANDES SEM SOBRESCREVER TUDO O
# QUE VEIO ANTES

## 44.1 OBJETIVO

**Agora é a melhor hora de aprender algo novo**

## 44.2 PASSO A PASSO COM CÓDIGO

43 EXERCÍCIO: RODAPÉ EM TELAS GRANDES SEM SOBRESCREVER TUDO O QUE VEIO ANTES 
**187**


--------------------------------------------------

1. No arquivo ** rodape.css **na pasta ** css **faça as seguintes alterações:

 .rodape {
   padding: 2em 5%;

   text-align: center;
   font-size: 0.7rem;
 }

 .rodape__logo {
   width: 11.25em;
   margin-bottom: 1em;
 }

 .rodape__lista-midias-sociais {
   display: flex;
   justify-content: center;
 }

 .rodape__infos-empresa {
   line-height: 1.5;
 }

 .rodape__lista-midias-sociais {
   display: flex;
   justify-content: center;
   margin-top: 1em;
 }

 .rodape__item-midias-sociais {
   width: 2.62em;
   margin: 0 .25em;
 }

 .rodape__item-midias-sociais img {
   width: 100%;
 }

 .rodape__titulo {
   margin-bottom: 1em;

   font-size: 1.45em;
   font-weight: bold;
   text-transform: uppercase;
 }

 .rodape_item-lista {  
   font-weight: 500;
   margin: 0.625em 0;
 }

 @media (max-width: 640px) {
   .rodape__secao + .rodape__secao {
     margin-top: 2em;
   }  
 }

-@̶m̶e̶d̶i̶a̶(̶m̶i̶n̶-̶w̶i̶d̶t̶h̶:̶ 6̶4̶0̶p̶x̶)̶ {̶
+@media(min-width: 640px) and (max-width: 1200px) {

**# css/rodape.css**

**188** 
44.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

   .rodape {
     display: flex;
     flex-wrap: wrap;
     justify-content: space-between;

     font-size: 1rem;
   }

   .rodape__secao--sobre,
   .rodape__secao--cursos,
   .rodape__secao--links,
   .rodape__secao--newsletter {
     width: 45%;
   }

   .rodape__secao--cursos {
     order: 1;
     margin: 0;
   }

   .rodape__secao--links {
     order: 2;
     margin: 0;
   }

   .rodape__secao--sobre {
     order: 3;
     margin-top: 2em;
   }

   .rodape__secao--newsletter {
     order: 4;
     margin-top: 2em;
   }
 }
+
+@media(min-width: 1200px) {
+  .rodape {
+    display: flex;
+    justify-content: space-between;
+    font-size: 0.85rem;
+    
+    text-align: left;
+  }
+
+  .rodape__titulo {
+    font-size: 1em;
+  }
+
+  .rodape__lista-midias-sociais {
+    justify-content: left;
+  }
+
+  .rodape__secao {
+    margin-top: 0;
+  }
+
+  .rodape__secao + .rodape__secao {
+    margin-left: 2em;
+  }
+}

44.2 PASSO A PASSO COM CÓDIGO 
**189**


--------------------------------------------------

CAPÍTULO 45

Olhe para sua página no navegador e volte aqui.

Você notou algum estilo se repetindo e que vamos continuar repetindo no resto da página? Se sim,

como poderíamos deixar de repetir esse estilo?

Nesse exercício trataremos de um estilo repetido em específico: o espaçamento entre a página e o

conteúdo do cabeçalho e do rodpé.

Para deixar de escrever o mesmo estilo várias vezes. Criaremos um novo componente/bloco
chamado ** container ** que terá todos os estilos que criam esse espaçamento. Esse estilo será aplicado

tanto no cabeçalho quanto no rodapé e será escrito apenas uma vez no novo componente ** container **.

Nada deve mudar no visual da página. As mudanças serão apenas no código.

Editoras tradicionais pouco ligam para ebooks e novas tecnologias. Não dominam
tecnicamente o assunto para revisar os livros a fundo. Não têm anos de
experiência em didáticas com cursos.
Conheça a **Casa do Código**, uma editora diferente, com curadoria da **Caelum** e

obsessão por livros de qualidade a preços justos.

Casa do Código, ebook com preço de ebook.

1. No arquivo ** cabecalho.css **na pasta ** css **faça as seguintes alterações:

# EXERCÍCIO: O COMPONENTE
# CONTAINER

## 45.1 OBJETIVO

**Editora Casa do Código com livros de uma forma diferente**

## 45.2 PASSO A PASSO COM CÓDIGO

**190** 
44 EXERCÍCIO: O COMPONENTE CONTAINER


--------------------------------------------------

 .cabecalho {
   text-align: center;
   font-size: 0.6rem;
   font-weight: bold;
   text-transform: uppercase;
   letter-spacing: 0.23em;

   color: #fff;
   background-color: #2D5377;
 }

 .cabecalho__logo {
   padding: 1.5em 0;
   width: 14.5em;
 }

 .cabecalho__menu {
   display: flex;
   justify-content: space-evenly;
   flex-wrap: wrap;

   background-color: #272B3A87;
 }

 .cabecalho__item-menu {
   display: inline-block;
 }

 .cabecalho__item-menu a {
   display: inline-block;
   padding: 1.86em 1.42em;
 }

 @media (min-width: 640px) {
   .cabecalho {
-    p̶a̶d̶d̶i̶n̶g̶:̶ 0̶ 5̶%̶;̶
+    padding-top: 0;
+    padding-bottom: 0;
     display: flex;
     justify-content: space-between;
     align-items: center;
   }

   .cabecalho__logo {
     padding: 2.5em 0;
   }

   .cabecalho__menu {
     background-color: transparent; 
   }
 }

 @media (min-width: 770px) {
   .cabecalho__item-menu--matricular {
     margin-left: 1.42em;

     border-radius: 6px;
     background-color: #e93d50;
   }

**# css/cabecalho.css**

45.2 PASSO A PASSO COM CÓDIGO 
**191**


--------------------------------------------------

   .cabecalho__item-menu--matricular a {
     padding: 1.8em 3.5em;
   }
 }
-
-@̶m̶e̶d̶i̶a̶ (̶m̶i̶n̶-̶w̶i̶d̶t̶h̶:̶ 1̶0̶6̶6̶p̶x̶)̶ {̶
-  .̶c̶a̶b̶e̶c̶a̶l̶h̶o̶ {̶
-    p̶a̶d̶d̶i̶n̶g̶-̶l̶e̶f̶t̶:̶ c̶a̶l̶c̶(̶(̶1̶0̶0̶%̶ -̶ 9̶6̶0̶p̶x̶)̶ /̶ 2̶)̶;̶
-    p̶a̶d̶d̶i̶n̶g̶-̶r̶i̶g̶h̶t̶:̶ c̶a̶l̶c̶(̶(̶1̶0̶0̶%̶ -̶ 9̶6̶0̶p̶x̶)̶ /̶ 2̶)̶;̶
-  }̶
-}̶

2. Crie o arquivo ** container.css **na pasta ** css **com o seguinte código:

+.container {
+  padding-left: 5%;
+  padding-right: 5%;
+}
+
+@media (min-width: 1066px) {
+  .container {
+    padding-left: calc((100% - 960px) / 2);
+    padding-right: calc((100% - 960px) / 2);
+  }
+}
+
+@media (min-width: 1440px) {
+  .container {
+    padding-left: calc((100% - 1200px) / 2);
+    padding-right: calc((100% - 1200px) / 2);
+  }
+}

3. No arquivo ** rodape.css **na pasta ** css **faça as seguintes alterações:

 .rodape {
-  p̶a̶d̶d̶i̶n̶g̶:̶ 2̶e̶m̶ 5̶%̶;̶
+  padding-top: 2em;
+  padding-bottom: 2em;

   text-align: center;
   font-size: 0.7rem;
 }

 .rodape__logo {
   width: 11.25em;
   margin-bottom: 1em;
 }

 .rodape__lista-midias-sociais {
   display: flex;
   justify-content: center;
 }

 .rodape__infos-empresa {
   line-height: 1.5;

**# css/container.css**

**# css/rodape.css**

**192** 
45.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

 }

 .rodape__lista-midias-sociais {
   display: flex;
   justify-content: center;
   margin-top: 1em;
 }

 .rodape__item-midias-sociais {
   width: 2.62em;
   margin: 0 .25em;
 }

 .rodape__item-midias-sociais img {
   width: 100%;
 }

 .rodape__titulo {
   margin-bottom: 1em;

   font-size: 1.45em;
   font-weight: bold;
   text-transform: uppercase;
 }

 .rodape_item-lista {  
   font-weight: 500;
   margin: 0.625em 0;
 }

 @media (max-width: 640px) {
   .rodape__secao + .rodape__secao {
     margin-top: 2em;
   }  
 }

 @media(min-width: 640px) and (max-width: 1200px) {
   .rodape {
     display: flex;
     flex-wrap: wrap;
     justify-content: space-between;

     font-size: 1rem;
   }

   .rodape__secao--sobre,
   .rodape__secao--cursos,
   .rodape__secao--links,
   .rodape__secao--newsletter {
     width: 45%;
   }

   .rodape__secao--cursos {
     order: 1;
     margin: 0;
   }

   .rodape__secao--links {
     order: 2;
     margin: 0;
   }

   .rodape__secao--sobre {

45.2 PASSO A PASSO COM CÓDIGO 
**193**


--------------------------------------------------

     order: 3;
     margin-top: 2em;
   }

   .rodape__secao--newsletter {
     order: 4;
     margin-top: 2em;
   }
 }

 @media(min-width: 1200px) {
   .rodape {
     display: flex;
     justify-content: space-between;
     font-size: 0.85rem;

     text-align: left;
   }

   .rodape__titulo {
     font-size: 1em;
   }

   .rodape__lista-midias-sociais {
     justify-content: left;
   }

   .rodape__secao {
     margin-top: 0;
   }

   .rodape__secao + .rodape__secao {
     margin-left: 2em;
   }
 }

4. No arquivo ** index.html **na pasta ** raíz do projeto **faça as seguintes alterações:

 *<!doctype html>*
 <html>
   <head>
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width">
     <title>Musicdot</title>
     <link rel="icon" href="img/favicon.ico">
     <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:300,400,500,
600,700,&display=block">

     <link rel="stylesheet" href="css/reset.css">
+    <link rel="stylesheet" href="css/container.css">
     <link rel="stylesheet" href="css/cabecalho.css">
     <link rel="stylesheet" href="css/rodape.css">
     <link rel="stylesheet" href="css/form-newsletter.css">
   </head>
   <body>

-    <̶h̶e̶a̶d̶e̶r̶ c̶l̶a̶s̶s̶=̶"̶c̶a̶b̶e̶c̶a̶l̶h̶o̶"̶>
+    <header class="cabecalho container">
       <a href="index.html">
         <img class="cabecalho__logo" src="img/musicdot-logo-light.svg" title="Ir para a página i

**# index.html**

**194** 
45.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

nicial da Musicdot" alt="Musicdot">

       </a>

       <nav>
         <ul class="cabecalho__menu">
           <li class="cabecalho__item-menu"> <a href="sobre.html#contato"> Contato </a> </li>
           <li class="cabecalho__item-menu"> <a href="#"> Entrar </a> </li>
           <li class="cabecalho__item-menu cabecalho__item-menu--matricular"> <a href="#"> Matric
ule-se </a> </li>

         </ul>
       </nav>
     </header>

     <main>
       Conteúdo principal
     </main>

-    <̶f̶o̶o̶t̶e̶r̶ c̶l̶a̶s̶s̶=̶"̶r̶o̶d̶a̶p̶e̶"̶>
+    <footer class="rodape container">
       <section class="rodape__secao rodape__secao--sobre">
         <img class="rodape__logo" src="img/logo.svg" alt="Logo da MusicDot">

         <p class="rodape__infos-empresa">
           AOVS Sistemas de Informática S.A.
           <br>
           CNPJ 05.555.382/0001-33 
           <br>
           Rua Vergueiro - São Paulo/SP
           <br>
           Telefone (11) 4118-3319
         </p>

         <ul class="rodape__lista-midias-sociais">
           <li class="rodape__item-midias-sociais">
             <a href="https://www.facebook.com/musicdotonline">
               <img src="img/footer-icone-facebook.svg" alt="MusicDot no Facebook">
             </a>
           </li>
           <li class="rodape__item-midias-sociais">
             <a href="https://www.youtube.com/user/musicdotonline">
               <img src="img/footer-icone-youtube.svg" alt="MusicDot no YouTube">
             </a>
           </li>
           <li class="rodape__item-midias-sociais">
             <a href="https://www.instagram.com/musicdotonline/">
               <img src="img/footer-icone-instagram.svg" alt="Instagram">
             </a>
           </li>
         </ul>
       </section>

       <section class="rodape__secao rodape__secao--cursos">
         <h2 class="rodape__titulo"> Cursos da MusicDot </h2>
         <nav>
           <ul>
             <li class="rodape_item-lista"><a href="#">Cursos de Teclado & Piano</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Violão/Guitarra</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Baixo</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Bateria</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Percussão</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Canto</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Áudio</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Teoria</a></li>

45.2 PASSO A PASSO COM CÓDIGO 
**195**


--------------------------------------------------

             <li class="rodape_item-lista"><a href="#">Cursos de Sopro</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Cordas</a></li>
           </ul>
         </nav>
       </section>

       <section class="rodape__secao rodape__secao--links">
         <h2 class="rodape__titulo"> MusicDot </h2>
         <nav>
           <ul>
             <li class="rodape_item-lista"><a href="#">Apostila</a></li>
             <li class="rodape_item-lista"><a href="#">E-book</a></li>
             <li class="rodape_item-lista"><a href="#">Login</a></li>
             <li class="rodape_item-lista"><a href="#">Matricule-se</a></li>
             <li class="rodape_item-lista"><a href="#">Perguntas frequentes</a></li>
             <li class="rodape_item-lista"><a href="#">Para Escolas</a></li>
             <li class="rodape_item-lista"><a href="#">Contato</a></li>
           </ul>
         </nav>
       </section>

       <section class="rodape__secao rodape__secao--newsletter">
         <h2 class="rodape__titulo"> 
           Receba novidades e lançamentos 
         </h2>

         <form action="#" method="get" class="form-newsletter">
           <label for="form-newsletter__label" class="form-newsletter__label">
             Seu email pessoal
           </label>
           <input id="email-newsletter" name="email-newsletter" type="email" class="form-newslett
er__campo">

           <button type="submit" class="form-newsletter__botao">
             OK
           </button>
         </form>
       </section>
     </footer>
   </body>
 </html>

**196** 
45.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

CAPÍTULO 46

Mais uma propriedade de posicionamento de elementos! A propriedade  display: flex  já nos

proporcionou grandes vantagens em relação às maneiras que costumávamos manipular posicionamento

de elementos, só que encontramos uma certa complicação quando precisamos posicionar elementos de
forma *bidimensional*.  Flex  é uma ótima ferramenta para quando temos elementos que precisam ser

distribuídos de maneira igual e com uma direção bem definida.

*<!DOCTYPE html>*
<html lang="pt-BR">
<head>

   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width">
   <title>Exemplo</title>
   <link rel="stylesheet" href="style.css">
</head>
<body>

   <main class="flex-container">
       <div class="foto"></div>
       <div class="foto"></div>
       <div class="foto"></div>
       <div class="foto"></div>
       <div class="foto"></div>
       <div class="foto"></div>
       <div class="foto"></div>
       <div class="foto"></div>
   </main>
</body>
</html>

.flex-container {

   display: flex;
   flex-wrap: wrap;
   justify-content: space-evenly;
}

.foto {

   width: 200px;
   height: 200px;

   border-radius: 5px;

   box-shadow: 3px 3px 3px #000000aa;

   background-color: #ff002b;

   margin-bottom: 1rem;
}

# DISPLAY: GRID

45 DISPLAY: GRID 
**197**


--------------------------------------------------

No exemplo mostrado acima o  display: flex  funciona perfeitamente porque a distribuição é

unidirecional, mesmo que exista uma segunda linha por conta do  flex-wrap . Mas agora se vamos

fazer algo como:

 display: flex  por conta não consegue lidar o posicionamento *bidimensional*. Precisamos

modificar a estrutura para que os elementos *ocupem o espaço de uma linha*:

<main>

   <div class="flex-container"> <!-- Primeira linha que contém "apenas" o bloco verde e o container 
que guarda os elementos vermelhos-->

       <div class="foto foto-destaque-verde"></div> <!-- Bloco verde e primeiro elemento da linha -->

       <div class="flex-container foto-container"> <!-- Container que vai guardar o restante dos ele
entos vermelhos e segundo elemento da linha -->

           <div class="foto"></div>
           <div class="foto"></div>
           <div class="foto"></div>
           <div class="foto"></div>
       </div>
   </div>
</main>

.flex-container {

   display: flex;
   flex-wrap: wrap;
   justify-content: space-evenly;
}

.foto-container {

   width: 66%;
}

**198** 
45 DISPLAY: GRID


--------------------------------------------------

.foto {

   width: 200px;
   height: 200px;

   border-radius: 5px;

   box-shadow: 3px 3px 3px #000000aa;

   background-color: #ff002b;

   margin-bottom: 1rem;
}

.foto-destaque-verde {

   background-color: #24cc2d;

   height: 400px;
}

Vamos entender o que aconteceu. Como o  flex  só consegue trabalhar com uma direção, então

vamos criar a primeira linha contendo apenas dois elementos: o **bloco verde** e uma **caixa vazia**. Nessa
caixa vazia, vamos criar nossa segunda linha (deixar a caixa como um  flex container ) com os 4

blocos vermelhos dentro e vamos limitar o tamanho dessa caixa para que o espaço seja melhor dividido.
Já conseguimos perceber com esse exemplo simples que o código já começou a ficar muito complicado.

Imagine fazer layouts mais complexos usando essa técnica do  diplay: flex . Por conta dessa

dificuldade de fazer layouts com uma complexidade *bidimensional* que surgiu o  display: grid .

A idéia do  grid  é exatamente de não precisar mudar a estrutura do **HTML** e que toda a parte de

45 DISPLAY: GRID 
**199**


--------------------------------------------------

posicionamento de layout fique apenas no **CSS**.

Quando colocamos a propriedade  display: grid  em um elemento ele se transforma em um *grid*

*container* da mesma forma que um elemento se torna *flex container* quando recebe a propriedade

display: flex . Depois que definimos um *grid container* precisamos definir sua estrutura. Por padrão

um *grid container* coloca cada item em uma linha e todos eles ficam em uma coluna:

**200** 
45 DISPLAY: GRID


--------------------------------------------------

45 DISPLAY: GRID 
**201**


--------------------------------------------------

Para ver melhor as marcações de grid, use a ferramenta de desenvolvimento de seu navegador.

Nós sabemos que nós precisamos de 3 colunas e 2 linhas para conseguir o efeito que queremos.
Então vamos usar as propriedades de *grid container* que vão definir o número de colunas e o número de

linhas respectivamente:  grid-template-columns: e  grid-template-rows . A propriedade de  grid 

permite que nós usemos outra unidade de medida:  fr (que significa fraction/ fração).

Podemos colocar infinitos valores dentro dessa propriedade, mas cada valor dentro dessa
propriedade vai representar **uma** coluna. Queremos 3 colunas que ocupem igualmente o espaço da

página. Vamos usar a nova unidade de medida  fr .

.grid-container {

   display: grid;

   grid-template-columns: 1fr 1fr 1fr;
}

No código acima, quando escrevemos  1fr 1fr 1fr estamos dizendo que queremos **3** colunas que

ocupem 1 fração do espaço disponível, ou seja, cada coluna vai ter 1/3 do espaço disponível
lateralmente.

A **Alura** oferece centenas de **cursos online** em sua plataforma exclusiva de
ensino que favorece o aprendizado com a **qualidade** reconhecida da Caelum.

Você pode escolher um curso nas áreas de Programação, Front-end, Mobile,
Design & UX, Infra, Business, entre outras, com um plano que dá acesso a todos os cursos. Ex-
estudante da Caelum tem 10% de desconto neste link!

Conheça os cursos online Alura.

## 46.1 GRID-TEMPLATE-COLUMNS

**Já conhece os cursos online Alura?**

## 46.2 GRID-TEMPLATE-ROWS

**202** 
46.1 GRID-TEMPLATE-COLUMNS


--------------------------------------------------

A propriedade que cria as linhas funciona da mesma maneira que a propriedade que cria colunas.
Portanto se queremos duas linhas que ocupam o mesmo espaço:

.grid-container {

   display: grid;

   grid-template-columns: 1fr 1fr 1fr;
   grid-template-rows: 1fr 1fr;
}

Só que mesmo depois de ter colocado as duas linhas ainda assim os elementos não ficaram dispostos
corretamente. O elemento verde ainda ocupa apenas uma linha e não duas, então precisamos indicar para

o navegador:

.foto-destaque-verde {

   background-color: #24cc2d;

   grid-row: span 2;

   height: 400px;
}

A propriedade  grid-row  é usada apenas nos elementos filhos de um *grid container* e ela recebe

dois valores: linha de início e linha de término. No nosso exemplo usamos o valor  span  que diz que

queremos mesclar linhas e o  2 a quantidade de linhas que vamos mesclar. Quando usamos o  span  o

próximo valor vai ser a quantidade de linhas ou colunas que vamos mesclar, portanto não indicamos
qual linha é a linha de término. Quando não colocamos o valor de término o navegador coloca

automaticamente  span 1 que quer dizer "ocupe apenas 1 linha/coluna".

Agora sim nosso bloco verde está na posição correta em relação aos elementos vermelhos. Usado

grid nós não precisamos mudar a estrutura HTML para conseguir o efeito que queríamos no começo e

o código ficou muito mais simples de entender também.

Vamos dificultar um pouco nosso exemplo. Vamos trocar a posição do bloco verde para a direita.

Vamos usar a propriedade  grid-columns para dizer onde que queremos que nosso bloco verde comece

e termine, mas apenas colocar essa propriedade no bloco verde não vai ser o suficiênte, precisamos
colocar essa propriedade também nos blocos vermelhos e isso já começa a aumentar significativamente
a complexidade e dificuldade de manutenção.

Para melhorar essa capacidade de movimentação de elementos dentro do grid, foi criado uma

propriedade chamada *grid-template-areas*, que nomeia cada espaço do grid criado. Vamos pegar nosso
layout normal e tentar nomear baseado no que já temos:

.grid-container {

   display: grid;

   grid-template-columns: 1fr 1fr 1fr;
   grid-template-rows: 1fr 1fr;
   grid-template-areas:
       "verde vermelho vermelho"

46.2 GRID-TEMPLATE-ROWS 
**203**


--------------------------------------------------

       "verde vermelho vermelho";
}

Então no exemplo acima na primeira linha (o primeiro conjunto de aspas):  primeiro espaço:

bloco verde, segundo espaço: bloco vermelho, terceiro espaço: bloco vermelho ; segunda

linha (o segundo conjunto de aspas):  primeiro espaço: bloco verde, segundo espaço: bloco

vermelho, terceiro espaço: bloco vermelho . Agora só precisamos dizer quem é o bloco vermelho

e quem é o bloco verde:

.grid-container {

   display: grid;

   grid-template-columns: 1fr 1fr 1fr;
   grid-template-rows: 1fr 1fr;
   grid-template-areas:
       "verde vermelho vermelho"
       "verde vermelho vermelho";
}

.foto-destaque-verde {

   background-color: #24cc2d;

   /*
   grid-column: 4;
   grid-row: span 2;
   Esse código não é mais necessário por conta do grid-template-area
   */
   grid-area: verde;

   height: 400px;
}

Antes de colocar nome nos outros blocos, vamos nomear apenas o bloco verde e depois testar.

Podemos observar que os elementos continuaram na mesma posição. Agora vamos mudar a posição do
bloco verde:

.grid-container {

   display: grid;

   grid-template-columns: 1fr 1fr 1fr;
   grid-template-rows: 1fr 1fr;
   grid-template-areas:
       "vermelho vermelho verde"
       "vermelho vermelho verde";
}

.foto-destaque-verde {

   background-color: #24cc2d;

   /*
   grid-column: 4;
   grid-row: span 2;
   Esse código não é mais necessário por conta do grid-template-area
   */
   grid-area: verde;

   height: 400px;
}

**204** 
46.2 GRID-TEMPLATE-ROWS


--------------------------------------------------

Mesmo sem nomear os blocos vermelhos com a propriedade  grid-area  chegamos no nosso

objetivo. Neste caso só queremos mudar a posição do bloco verde e queremos que o restante se adapte
conforme necessário, então podemos trocar os valores de **vermelho** para apenas um ponto "**.**" .

.grid-container {

   display: grid;

   grid-template-columns: 1fr 1fr 1fr;
   grid-template-rows: 1fr 1fr;
   grid-template-areas:
       ". . verde"
       ". . verde";
}

.foto-destaque-verde {

   background-color: #24cc2d;

   /*
   grid-column: 4;
   grid-row: span 2;
   Esse código não é mais necessário por conta do grid-template-area
   */
   grid-area: verde;

   height: 400px;
}

Não podemos deixar espaços vazios que o browser não vai entender, precisamos deixar alguma

coisa para indicar o espaço do grid.

46.2 GRID-TEMPLATE-ROWS 
**205**


--------------------------------------------------

CAPÍTULO 47

Figura 47.1: Vitrine de cursos mobile

Figura 47.2: Vitrine de cursos telas médias

# EXERCÍCIO: CONTEÚDO PRINCIPAL - A
# VITRINE DE CURSOS

## 47.1 OBJETIVO

**206** 
46 EXERCÍCIO: CONTEÚDO PRINCIPAL - A VITRINE DE CURSOS


--------------------------------------------------

Figura 47.3: Vitrine de cursos desktop

Querendo aprender ainda mais sobre? Esclarecer dúvidas dos exercícios? Ouvir
explicações detalhadas com um instrutor?
A Caelum oferece o **curso data** presencial nas cidades de São Paulo, Rio de

Janeiro e Brasília, além de turmas incompany.

Consulte as vantagens do curso *Desenvolvimento Web com HTML, CSS e*

*JavaScript*

1. No arquivo ** cabecalho.css **na pasta ** css **faça as seguintes alterações:

 .cabecalho {
+  position: absolute;
+  top: 0;
+  width: 100%;
+  box-sizing: border-box;
+
   text-align: center;
   font-size: 0.6rem;
   font-weight: bold;
   text-transform: uppercase;
   letter-spacing: 0.23em;

   color: #fff;
-  b̶a̶c̶k̶g̶r̶o̶u̶n̶d̶-̶c̶o̶l̶o̶r̶:̶ #̶2̶D̶5̶3̶7̶7̶;̶
 }

 .cabecalho__logo {
   padding: 1.5em 0;
   width: 14.5em;
 }

**Você pode também fazer o curso data dessa apostila na Caelum**

## 47.2 PASSO A PASSO COM CÓDIGO

**# css/cabecalho.css**

47.2 PASSO A PASSO COM CÓDIGO 
**207**


--------------------------------------------------

 .cabecalho__menu {
   display: flex;
   justify-content: space-evenly;
   flex-wrap: wrap;

   background-color: #272B3A87;
 }

 .cabecalho__item-menu {
   display: inline-block;
 }

 .cabecalho__item-menu a {
   display: inline-block;
   padding: 1.86em 1.42em;
 }

 @media (min-width: 640px) {
   .cabecalho {
     padding-top: 0;
     padding-bottom: 0;
     display: flex;
     justify-content: space-between;
     align-items: center;
   }

   .cabecalho__logo {
     padding: 2.5em 0;
   }

   .cabecalho__menu {
     background-color: transparent; 
   }
 }

 @media (min-width: 770px) {
   .cabecalho__item-menu--matricular {
     margin-left: 1.42em;

     border-radius: 6px;
     background-color: #e93d50;
   }

   .cabecalho__item-menu--matricular a {
     padding: 1.8em 3.5em;
   }
 }

2. Crie o arquivo ** cursos.css **na pasta ** css **com o seguinte código:

+.--largura-maxima {
+    width: 100%;
+  }
+  
+  .--largura-grande {
+    width: 80%;
+  }
+  
+  .botao {
+    font-size: .8rem;

**# css/cursos.css**

**208** 
47.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

+    font-weight: 500;
+    letter-spacing: 2.9px;
+    text-transform: uppercase;
+    padding: 1rem 40px;
+    margin-top: .5rem;
+    margin-bottom: .5rem;
+    border-radius: 6px;
+    transition: .25s;
+  }
+  
+  .botao:hover {
+    transform: translate(0, .22rem);
+    transition: .25s;
+  }
+
+.cursos {
+    color: #fff;
+    text-align: center;
+    background-image: url(../img/home-background-mobile.png);
+    background-size: cover;
+    padding-top: 9.5rem;
+    display: flex;
+    flex-direction: column;
+    align-items: center;
+  }
+  
+  .cursos__chamada {
+    display: flex;
+    flex-direction: column;
+    align-items: center;
+  }
+  
+  .chamada__titulo {
+    color: #e93d50;
+    font-weight: 700;
+    font-size: 1.2rem;
+    margin-bottom: .3rem;
+  }
+  
+  .chamada__titulo--destaque {
+    color: #fff;
+  }
+  
+  .chamada p {
+    font-weight: 500;
+    line-height: 1.3;
+    margin: 1rem 0;
+  }
+  
+  .chamada__cursos__matricula {
+    color: #fff;
+    background-color: #e93d50;
+  }
+  
+  .cursos__lista {
+    font-size: .7rem;
+    font-weight: 600;
+    margin-top: 1rem;
+    margin-bottom: 1rem;
+    display: grid;
+    grid-template-columns: 7rem 7rem;
+    grid-template-rows: repeat(5, 4.5rem);
+    grid-gap: .5rem;

47.2 PASSO A PASSO COM CÓDIGO 
**209**


--------------------------------------------------

+    text-align: center;
+  }
+  
+  .cursos__lista li {
+    border: 1px solid #4286f4;
+    border-radius: 8px;
+    box-sizing: border-box;
+    display: flex;
+    justify-content: space-around;
+    align-items: center;
+    background-repeat: no-repeat;
+    background-size: 2rem 2rem;
+    background-position: top .6rem center;
+    padding-top: 2.5rem;
+    transition: .25s;
+  }
+  
+  .cursos__lista li:hover {
+    transform: translate(0, .22rem);
+    background-color: rgba(66, 134, 244, 0.337);
+    transition: .25s;
+  }
+  
+  .curso--tecladopiano {
+    background-image: url("../img/icone-teclado-piano.svg");
+  }
+  
+  .curso--violaoguitarra {
+    background-image: url("../img/icones-violao-guitarra.svg");
+  }
+  
+  .curso--baixo {
+    background-image: url("../img/icones-baixo.svg");
+  }
+  
+  .curso--bateria {
+    background-image: url("../img/icones-bateria.svg");
+  }
+  
+  .curso--percussao {
+    background-image: url("../img/icones-percussao.svg");
+  }
+  
+  .curso--canto {
+    background-image: url("../img/icones-canto.svg");
+  }
+  
+  .curso--audio {
+    background-image: url("../img/icones-audio.svg");
+  }
+  
+  .curso--teoria {
+    background-image: url("../img/icones-teoria.svg");
+  }
+  
+  .curso--sopro {
+    background-image: url("../img/icones-sopro.svg");
+  }
+  
+  .curso--cordas {
+    background-image: url("../img/icone-cordas.svg");
+  }
+  

**210** 
47.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

+  .cursos__lista img {
+    width: 2rem;
+    height: 2rem;
+    margin-bottom: 5px;
+  }
+
+  @media(min-width:768px) {
+    .cursos {
+        padding: 6rem 5% 0;
+        background-image: url(../img/home-background.png);
+      }
+    
+      .cursos__chamada {
+        width: 300px;
+        align-items: flex-start;
+        align-self: flex-start;
+        text-align: left;
+      }
+    
+      .chamada__titulo {
+        font-size: 2rem;
+      }
+    
+      .chamada__cursos__matricula {
+        display: none;
+      }
+    
+      .cursos__lista {
+        grid-template-columns: repeat(5, 7rem);
+        grid-template-rows: 5.5rem 5.5rem 5.5rem;
+        gap: .8rem;
+      }
+    
+      .cursos__lista li {
+        background-repeat: no-repeat;
+        background-size: 2rem 2rem;
+        background-position: top 1rem center;
+        padding-top: 2.5rem;
+      }
+    
+    .cursos__lista .curso--destaque {
+        order: -1;
+        grid-area: 1/1/span 3/3;
+        padding-top: 5.5rem;
+        background-size: 6rem 6rem;
+        background-position: top 3.6rem center;
+    }
+}
+
+@media(min-width:1200px) {
+    .cursos {
+        padding: 7rem 10% 0;
+      }
+    
+      .cursos__chamada {
+        width: 450px;
+      }
+    
+      .chamada__titulo {
+        font-size: 2.5rem;
+      }
+    
+      .cursos__lista {

47.2 PASSO A PASSO COM CÓDIGO 
**211**


--------------------------------------------------

+        grid-template-columns: repeat(6, 9.3rem);
+        grid-template-rows: 7.5rem 7.5rem;
+        margin-top: 1.5rem;
+        margin-bottom: 1.5rem;
+      }
+    
+      .cursos__lista li {
+        background-repeat: no-repeat;
+        background-size: 3rem 3rem;
+        background-position: top 1rem center;
+        padding-top: 2.5rem;
+      }
+    
+      .cursos__lista .curso--destaque {
+        order: -1;
+        grid-area: 1/1/span 2/2;
+        padding-top: 6rem;
+        background-size: 6rem 6rem;
+        background-position: top 3.6rem center;
+      }
+    
+      .cursos__lista .curso--destaque2 {
+        order: -1;
+        grid-area: 1/4/span 2/5;
+        padding-top: 6rem;
+        background-size: 6rem 6rem;
+        background-position: top 3.6rem center;
+      }
+    
+      .cursos__lista p {
+        font-size: .9rem;
+      }
+    
+    
+      .curso--destaque2 .imagem-destaque2 {
+        width: 6rem;
+        height: 6rem;
+        margin-bottom: .8rem;
+      }
+}
+
+@media(min-width:1440px) {
+    .cursos__lista {
+      grid-template-columns: repeat(6, 11rem);
+    }
+}
+
+@media(min-width:1600px) {
+    .cursos__lista {
+        grid-template-columns: repeat(6, 13rem);
+      }
+    
+      .cursos__lista img {
+        width: 3rem;
+        height: 3rem;
+        margin-bottom: 10px;
+      }
+}

3. No arquivo ** index.html **na pasta ** raíz do projeto **faça as seguintes alterações:

**# index.html**

**212** 
47.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

 *<!doctype html>*
 <html>
   <head>
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width">
     <title>Musicdot</title>
     <link rel="icon" href="img/favicon.ico">
     <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:300,400,500,
600,700,&display=block">

     <link rel="stylesheet" href="css/reset.css">
     <link rel="stylesheet" href="css/container.css">
     <link rel="stylesheet" href="css/cabecalho.css">
+    <link rel="stylesheet" href="css/cursos.css">
     <link rel="stylesheet" href="css/rodape.css">
     <link rel="stylesheet" href="css/form-newsletter.css">
   </head>
   <body>

     <header class="cabecalho container">
       <a href="index.html">
         <img class="cabecalho__logo" src="img/musicdot-logo-light.svg" title="Ir para a página i
nicial da Musicdot" alt="Musicdot">

       </a>

       <nav>
         <ul class="cabecalho__menu">
           <li class="cabecalho__item-menu"> <a href="sobre.html#contato"> Contato </a> </li>
           <li class="cabecalho__item-menu"> <a href="#"> Entrar </a> </li>
           <li class="cabecalho__item-menu cabecalho__item-menu--matricular"> <a href="#"> Matric
ule-se </a> </li>

         </ul>
       </nav>
     </header>

     <main>
-      C̶o̶n̶t̶e̶ú̶d̶o̶ p̶r̶i̶n̶c̶i̶p̶a̶l̶
+      <section class="cursos">
+        <article class="cursos__chamada --largura-grande">
+          <h1 class="chamada__titulo">Cursos online de <strong class="chamada__titulo--destaque">
música</strong></h1>

+          <p>Comece agora e aprenda sua primeira música em 10 minutos!</p>
+          <a href="cursos.html" class="chamada__cursos__matricula botao">Matricule-se</a>
+        </article>
+        <nav>
+            <ul class="cursos__lista">
+                <li class="curso--tecladopiano">
+                    <a href="#">Teclado & Piano</a>
+                </li>
+                <li class="curso--violaoguitarra">
+                    <a href="#">Violão & Guitarra</a>
+                </li>
+                <li class="curso--baixo">
+                    <a href="#">Baixo</a>
+                </li>
+                <li class="curso--bateria curso--destaque">
+                    <a href="#">Bateria</a>
+                </li>
+                <li class="curso--percussao">
+                    <a href="#">Percussão</a>
+                </li>
+                <li class="curso--canto curso--destaque2">
+                    <a href="#">Canto</a>
+                </li>

47.2 PASSO A PASSO COM CÓDIGO 
**213**


--------------------------------------------------

+                <li class="curso--audio">
+                    <a href="#">Áudio</a>
+                </li>
+                <li class="curso--teoria">
+                    <a href="#">Teoria</a>
+                </li>
+                <li class="curso--sopro">
+                    <a href="#">Sopro</a>
+                </li>
+                <li class="curso--cordas">
+                    <a href="#">Cordas</a>
+                </li>
+            </ul>
+        </nav>
+      </section>
     </main>

     <footer class="rodape container">
       <section class="rodape__secao rodape__secao--sobre">
         <img class="rodape__logo" src="img/logo.svg" alt="Logo da MusicDot">

         <p class="rodape__infos-empresa">
           AOVS Sistemas de Informática S.A.
           <br>
           CNPJ 05.555.382/0001-33 
           <br>
           Rua Vergueiro - São Paulo/SP
           <br>
           Telefone (11) 4118-3319
         </p>

         <ul class="rodape__lista-midias-sociais">
           <li class="rodape__item-midias-sociais">
             <a href="https://www.facebook.com/musicdotonline">
               <img src="img/footer-icone-facebook.svg" alt="MusicDot no Facebook">
             </a>
           </li>
           <li class="rodape__item-midias-sociais">
             <a href="https://www.youtube.com/user/musicdotonline">
               <img src="img/footer-icone-youtube.svg" alt="MusicDot no YouTube">
             </a>
           </li>
           <li class="rodape__item-midias-sociais">
             <a href="https://www.instagram.com/musicdotonline/">
               <img src="img/footer-icone-instagram.svg" alt="Instagram">
             </a>
           </li>
         </ul>
       </section>

       <section class="rodape__secao rodape__secao--cursos">
         <h2 class="rodape__titulo"> Cursos da MusicDot </h2>
         <nav>
           <ul>
             <li class="rodape_item-lista"><a href="#">Cursos de Teclado & Piano</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Violão/Guitarra</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Baixo</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Bateria</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Percussão</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Canto</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Áudio</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Teoria</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Sopro</a></li>

**214** 
47.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

             <li class="rodape_item-lista"><a href="#">Cursos de Cordas</a></li>
           </ul>
         </nav>
       </section>

       <section class="rodape__secao rodape__secao--links">
         <h2 class="rodape__titulo"> MusicDot </h2>
         <nav>
           <ul>
             <li class="rodape_item-lista"><a href="#">Apostila</a></li>
             <li class="rodape_item-lista"><a href="#">E-book</a></li>
             <li class="rodape_item-lista"><a href="#">Login</a></li>
             <li class="rodape_item-lista"><a href="#">Matricule-se</a></li>
             <li class="rodape_item-lista"><a href="#">Perguntas frequentes</a></li>
             <li class="rodape_item-lista"><a href="#">Para Escolas</a></li>
             <li class="rodape_item-lista"><a href="#">Contato</a></li>
           </ul>
         </nav>
       </section>

       <section class="rodape__secao rodape__secao--newsletter">
         <h2 class="rodape__titulo"> 
           Receba novidades e lançamentos 
         </h2>

         <form action="#" method="get" class="form-newsletter">
           <label for="form-newsletter__label" class="form-newsletter__label">
             Seu email pessoal
           </label>
           <input id="email-newsletter" name="email-newsletter" type="email" class="form-newslett
er__campo">

           <button type="submit" class="form-newsletter__botao">
             OK
           </button>
         </form>
       </section>
     </footer>
   </body>
 </html>

47.2 PASSO A PASSO COM CÓDIGO 
**215**


--------------------------------------------------

CAPÍTULO 48

Figura 48.1: Seção vídeo em telas pequenas

Figura 48.2: Seção vídeo em telas maiores

# EXERCÍCIO: CONTEÚDO PRINCIPAL

## 48.1 OBJETIVO

**216** 
47 EXERCÍCIO: CONTEÚDO PRINCIPAL


--------------------------------------------------

Conheça a **Casa do Código**, uma **nova** editora, com autores de destaque no

mercado, foco em **ebooks** (PDF, epub, mobi), preços **imbatíveis** e assuntos
**atuais**.
Com a curadoria da **Caelum** e excelentes autores, é uma abordagem **diferente**

para livros de tecnologia no Brasil.

Casa do Código, Livros de Tecnologia.

1. Crie o arquivo ** video.css **na pasta ** css **com o seguinte código:

+.video {
+    display: flex;
+    flex-direction: column;
+    align-items: center;
+    text-align: center;
+    color: #fff;
+    background-color: #2a3042;
+}
+
+.video--mobile {
+    width: 100%;
+    height: 8.9rem;
+}
+
+.video--desktop {
+    display: none;
+}
+
+.video__textos {
+    margin-top: 1rem;
+    margin-bottom: 1rem;
+    position: relative;
+    padding: 0 10%;
+    box-sizing: border-box;
+}
+
+.textos__titulo {
+    font-weight: 700;
+    font-size: 1.2rem;
+    margin-bottom: .3rem;
+    margin-bottom: .5rem;
+}
+

**Seus livros de tecnologia parecem do século passado?**

## 48.2 PASSO A PASSO COM CÓDIGO

**# css/video.css**

48.2 PASSO A PASSO COM CÓDIGO 
**217**


--------------------------------------------------

+.textos__titulo::first-line {
+    color: #e93d50;
+}
+
+@media(min-width:768px) {
+    .video--mobile {
+        display: none;
+    }
+    
+    .video--desktop {
+        display: block;
+        width: 100%;
+        height: 12.8rem;
+    }
+    
+    .textos__titulo {
+        font-size: 1.5rem;
+    }
+}
+
+@media(min-width:1200px) {
+    .video--desktop {
+        height: 19.8rem;
+    }
+    
+    .video__textos {
+        margin-top: 1.5rem;
+        margin-bottom: 1.5rem;
+    }
+    
+    .video__textos::before {
+        width: 5rem;
+        height: 5rem;
+    }
+    
+    .textos__titulo {
+        font-size: 1.9rem;
+    }
+}
+
+@media(min-width:1600px) {
+    .video--desktop {
+        height: 26.8rem;
+    }
+}

2. No arquivo ** index.html **na pasta ** raíz do projeto **faça as seguintes alterações:

 *<!doctype html>*
 <html>
   <head>
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width">
     <title>Musicdot</title>
     <link rel="icon" href="img/favicon.ico">
     <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:300,400,500,
600,700,&display=block">

     <link rel="stylesheet" href="css/reset.css">
     <link rel="stylesheet" href="css/container.css">
     <link rel="stylesheet" href="css/cabecalho.css">

**# index.html**

**218** 
48.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

     <link rel="stylesheet" href="css/cursos.css">
+    <link rel="stylesheet" href="css/video.css">
     <link rel="stylesheet" href="css/rodape.css">
     <link rel="stylesheet" href="css/form-newsletter.css">
   </head>
   <body>

     <header class="cabecalho container">
       <a href="index.html">
         <img class="cabecalho__logo" src="img/musicdot-logo-light.svg" title="Ir para a página i
nicial da Musicdot" alt="Musicdot">

       </a>

       <nav>
         <ul class="cabecalho__menu">
           <li class="cabecalho__item-menu"> <a href="sobre.html#contato"> Contato </a> </li>
           <li class="cabecalho__item-menu"> <a href="#"> Entrar </a> </li>
           <li class="cabecalho__item-menu cabecalho__item-menu--matricular"> <a href="#"> Matric
ule-se </a> </li>

         </ul>
       </nav>
     </header>

     <main>
       <section class="cursos">
         <article class="cursos__chamada --largura-grande">
           <h1 class="chamada__titulo">Cursos online de <strong class="chamada__titulo--destaque">
música</strong></h1>

           <p>Comece agora e aprenda sua primeira música em 10 minutos!</p>
           <a href="cursos.html" class="chamada__cursos__matricula botao">Matricule-se</a>
         </article>
         <nav>
             <ul class="cursos__lista">
                 <li class="curso--tecladopiano">
                     <a href="#">Teclado & Piano</a>
                 </li>
                 <li class="curso--violaoguitarra">
                     <a href="#">Violão & Guitarra</a>
                 </li>
                 <li class="curso--baixo">
                     <a href="#">Baixo</a>
                 </li>
                 <li class="curso--bateria curso--destaque">
                     <a href="#">Bateria</a>
                 </li>
                 <li class="curso--percussao">
                     <a href="#">Percussão</a>
                 </li>
                 <li class="curso--canto curso--destaque2">
                     <a href="#">Canto</a>
                 </li>
                 <li class="curso--audio">
                     <a href="#">Áudio</a>
                 </li>
                 <li class="curso--teoria">
                     <a href="#">Teoria</a>
                 </li>
                 <li class="curso--sopro">
                     <a href="#">Sopro</a>
                 </li>
                 <li class="curso--cordas">
                     <a href="#">Cordas</a>
                 </li>

48.2 PASSO A PASSO COM CÓDIGO 
**219**


--------------------------------------------------

             </ul>
         </nav>
       </section>
+      <section class="video">
+        <video  controls class="video--mobile" src="video/video-promocional.mp4" poster="img/vid
eo-principal-mobile.png"></video>

+        <video controls class="video--desktop" src="video/video-promocional.mp4" poster="img/vid
eo-principal.png"></video>

+        <article class="video__textos">
+          <h2 class="textos__titulo">Estude com os melhores professores</h2>
+          <p>Aprenda no seu ritmo, sem sair de casa</p>
+        </article>
+      </section>
     </main>

     <footer class="rodape container">
       <section class="rodape__secao rodape__secao--sobre">
         <img class="rodape__logo" src="img/logo.svg" alt="Logo da MusicDot">

         <p class="rodape__infos-empresa">
           AOVS Sistemas de Informática S.A.
           <br>
           CNPJ 05.555.382/0001-33 
           <br>
           Rua Vergueiro - São Paulo/SP
           <br>
           Telefone (11) 4118-3319
         </p>

         <ul class="rodape__lista-midias-sociais">
           <li class="rodape__item-midias-sociais">
             <a href="https://www.facebook.com/musicdotonline">
               <img src="img/footer-icone-facebook.svg" alt="MusicDot no Facebook">
             </a>
           </li>
           <li class="rodape__item-midias-sociais">
             <a href="https://www.youtube.com/user/musicdotonline">
               <img src="img/footer-icone-youtube.svg" alt="MusicDot no YouTube">
             </a>
           </li>
           <li class="rodape__item-midias-sociais">
             <a href="https://www.instagram.com/musicdotonline/">
               <img src="img/footer-icone-instagram.svg" alt="Instagram">
             </a>
           </li>
         </ul>
       </section>

       <section class="rodape__secao rodape__secao--cursos">
         <h2 class="rodape__titulo"> Cursos da MusicDot </h2>
         <nav>
           <ul>
             <li class="rodape_item-lista"><a href="#">Cursos de Teclado & Piano</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Violão/Guitarra</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Baixo</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Bateria</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Percussão</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Canto</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Áudio</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Teoria</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Sopro</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Cordas</a></li>
           </ul>

**220** 
48.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

         </nav>
       </section>

       <section class="rodape__secao rodape__secao--links">
         <h2 class="rodape__titulo"> MusicDot </h2>
         <nav>
           <ul>
             <li class="rodape_item-lista"><a href="#">Apostila</a></li>
             <li class="rodape_item-lista"><a href="#">E-book</a></li>
             <li class="rodape_item-lista"><a href="#">Login</a></li>
             <li class="rodape_item-lista"><a href="#">Matricule-se</a></li>
             <li class="rodape_item-lista"><a href="#">Perguntas frequentes</a></li>
             <li class="rodape_item-lista"><a href="#">Para Escolas</a></li>
             <li class="rodape_item-lista"><a href="#">Contato</a></li>
           </ul>
         </nav>
       </section>

       <section class="rodape__secao rodape__secao--newsletter">
         <h2 class="rodape__titulo"> 
           Receba novidades e lançamentos 
         </h2>

         <form action="#" method="get" class="form-newsletter">
           <label for="form-newsletter__label" class="form-newsletter__label">
             Seu email pessoal
           </label>
           <input id="email-newsletter" name="email-newsletter" type="email" class="form-newslett
er__campo">

           <button type="submit" class="form-newsletter__botao">
             OK
           </button>
         </form>
       </section>
     </footer>
   </body>
 </html>

48.2 PASSO A PASSO COM CÓDIGO 
**221**


--------------------------------------------------

CAPÍTULO 49

Figura 49.1: Planos telas menores

# EXERCÍCIO: CONTEÚDO PRINCIPAL
# (OPCIONAL) - OS PLANOS

## 49.1 OBJETIVO

**222** 
48 EXERCÍCIO: CONTEÚDO PRINCIPAL (OPCIONAL) - OS PLANOS


--------------------------------------------------

Figura 49.2: Planos telas maiores

Se você está gostando dessa apostila, certamente vai aproveitar os **cursos**
**online** que lançamos na plataforma **Alura**. Você estuda a qualquer momento

com a **qualidade** Caelum. Programação, Mobile, Design, Infra, Front-End e
Business, entre outros! Ex-estudante da Caelum tem 10% de desconto, siga o link!

Conheça a Alura Cursos Online.

1. Crie o arquivo ** planos.css **na pasta ** css **com o seguinte código:

+.planos {
+    background-image: url(../img/planos-background-mobile.png);
+    background-size: cover;
+    background-repeat: no-repeat;
+    text-align: center;
+    padding-top: 15px;
+    padding-bottom: 1.8rem;
+    display: grid;
+    justify-items: center;
+    position: relative;
+}
+
+.planos::before {
+    content: "";
+    width: 81%;
+    height: .1rem;
+    background-color: #e93d50;
+    position: absolute;
+    top: 0;
+    left: 50%;

**Agora é a melhor hora de aprender algo novo**

## 49.2 PASSO A PASSO COM CÓDIGO

**# css/planos.css**

49.2 PASSO A PASSO COM CÓDIGO 
**223**


--------------------------------------------------

+    transform: translate(-50%, 0);
+}
+
+.planos__titulo {
+    font-size: .85rem;
+    font-weight: 700;
+    margin-bottom: 2rem;
+}
+
+.planos__card {
+    background-color: #f76148;
+    border-radius: 8px;
+    margin-bottom: 1.3rem;
+    color: #fff;
+    padding: 4rem 1rem 1rem;
+    display: flex;
+    flex-direction: column;
+    align-items: center;
+    box-shadow: 0 0 .8rem .1rem rgba(0, 0, 0, .2);
+    background-repeat: no-repeat;
+    background-size: 1.7rem;
+    background-position: top 1.5rem center;
+}
+
+.card--anual {
+    background-image: url(../img/simbolo-musidot-branco.svg);
+}
+
+.card--semestral {
+    background-image: url(../img/simbolo-musidot-dark.svg);
+}
+
+.plano__titulo {
+    margin: 8px 0;
+}
+
+.planos__card p + p {
+    font-weight: 300;
+    margin-top: .2rem;
+    letter-spacing: 1.5px;
+}
+
+.plano__titulo, .plano__titulo + p {
+    font-size: 1rem;
+    font-weight: 500;
+}
+
+.valor--destaque {
+    font-size: 2rem;
+    font-weight: 700;
+}
+
+.planos__card span {
+    font-weight: 500;
+}
+
+.cards__botao {
+    color: #f76148;
+    text-transform: uppercase;
+    letter-spacing: 1.8px;
+    font-weight: 600;
+    border-radius: 8px;
+    margin-top: .8rem;

**224** 
49.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

+    padding: 1rem 2rem;
+    background-color: #fff;
+    box-shadow: 0 0 .8rem .1rem rgba(0, 0, 0, .2);
+}
+
+.card--anual {
+    position: relative;
+    z-index: 2;
+}
+
+.plano--destaque {
+    color: #f76148;
+    font-weight: 600;
+    text-transform: uppercase;
+    letter-spacing: 1.1px;
+    width: 8rem;
+    padding: .4rem 0 .8rem;
+    border-radius: 5px;
+    box-shadow: 0 0 .8rem .05rem rgba(0, 0, 0, .2);
+    background-color: #fff;
+    position: absolute;
+    transform: translate(-50%, -65%);
+    z-index: 1;
+}
+
+.card--anual p + p, .card--semestral p + p {
+    margin-bottom: 1rem;
+}
+
+.planos > p {
+    width: 250px;
+    font-size: .6rem;
+    font-weight: 600;
+    line-height: 18px;
+}
+
+.planos a {
+    font-weight: 700;
+}
+
+
+@media(min-width:768px) {
+    .planos {
+        grid-template-columns: 20rem 20rem;
+        grid-template-areas:
+        "header header"
+        "card1 card2" 
+        "footer footer";
+        gap: 1rem;
+        justify-content: center;
+        padding-bottom: 2rem;
+        background-image: url(../img/planos-background.png);
+        background-size: cover;
+    }
+    
+    .planos__titulo {
+        grid-area: header;
+    }
+    
+    .cards__planoanual {
+        grid-area: card2;
+    }
+    

49.2 PASSO A PASSO COM CÓDIGO 
**225**


--------------------------------------------------

+    .card--semestral {
+        grid-area: card1;
+    }
+    
+    .planos__pagamentos {
+        grid-column-end: span 2;
+    }
+    
+    .planos--maisassinado {
+        font-size: .8rem;
+    }
+    
+    .planos__card {
+        padding: 6rem 2rem 2rem;
+        justify-content: space-between;
+        background-size: 2.5rem;
+        background-position: top 2.5rem center;
+    }
+    
+    .planos__card img {
+        width: 2.5rem;
+    }
+    
+    .plano__titulo, .plano__titulo + p {
+        font-size: 1.4rem;
+        font-weight: 500;
+    }
+    
+    .valor--destaque {
+        font-size: 2.6rem;
+        font-weight: 700;
+    }
+    
+    .plano--destaque {
+        font-size: .6rem;
+    }
+    
+    .cards__botao {
+        font-size: 1.1rem;
+        transition: .25s;
+    }
+    
+    .planos > p {
+        font-size: .9rem;
+        font-weight: 600;
+        line-height: 18px;
+    }
+}
+
+@media(min-width:1200px) {
+    .planos__titulo {
+        font-size: 1.2rem;
+    }
+    
+    .plano--destaque {
+        font-size: .9rem;
+        width: 10rem;
+        transform: translate(-50%, -75%);
+    }
+    
+}

**226** 
49.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

2. No arquivo ** index.html **na pasta ** raíz do projeto **faça as seguintes alterações:

 *<!doctype html>*
 <html>
   <head>
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width">
     <title>Musicdot</title>
     <link rel="icon" href="img/favicon.ico">
     <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:300,400,500,
600,700,&display=block">

     <link rel="stylesheet" href="css/reset.css">
     <link rel="stylesheet" href="css/container.css">
     <link rel="stylesheet" href="css/cabecalho.css">
     <link rel="stylesheet" href="css/cursos.css">
     <link rel="stylesheet" href="css/video.css">
+    <link rel="stylesheet" href="css/planos.css">
     <link rel="stylesheet" href="css/rodape.css">
     <link rel="stylesheet" href="css/form-newsletter.css">
   </head>
   <body>

     <header class="cabecalho container">
       <a href="index.html">
         <img class="cabecalho__logo" src="img/musicdot-logo-light.svg" title="Ir para a página i
nicial da Musicdot" alt="Musicdot">

       </a>

       <nav>
         <ul class="cabecalho__menu">
           <li class="cabecalho__item-menu"> <a href="sobre.html#contato"> Contato </a> </li>
           <li class="cabecalho__item-menu"> <a href="#"> Entrar </a> </li>
           <li class="cabecalho__item-menu cabecalho__item-menu--matricular"> <a href="#"> Matric
ule-se </a> </li>

         </ul>
       </nav>
     </header>

     <main>
       <section class="cursos">
         <article class="cursos__chamada --largura-grande">
           <h1 class="chamada__titulo">Cursos online de <strong class="chamada__titulo--destaque">
música</strong></h1>

           <p>Comece agora e aprenda sua primeira música em 10 minutos!</p>
           <a href="cursos.html" class="chamada__cursos__matricula botao">Matricule-se</a>
         </article>
         <nav>
             <ul class="cursos__lista">
                 <li class="curso--tecladopiano">
                     <a href="#">Teclado & Piano</a>
                 </li>
                 <li class="curso--violaoguitarra">
                     <a href="#">Violão & Guitarra</a>
                 </li>
                 <li class="curso--baixo">
                     <a href="#">Baixo</a>
                 </li>
                 <li class="curso--bateria curso--destaque">
                     <a href="#">Bateria</a>

**# index.html**

49.2 PASSO A PASSO COM CÓDIGO 
**227**


--------------------------------------------------

                 </li>
                 <li class="curso--percussao">
                     <a href="#">Percussão</a>
                 </li>
                 <li class="curso--canto curso--destaque2">
                     <a href="#">Canto</a>
                 </li>
                 <li class="curso--audio">
                     <a href="#">Áudio</a>
                 </li>
                 <li class="curso--teoria">
                     <a href="#">Teoria</a>
                 </li>
                 <li class="curso--sopro">
                     <a href="#">Sopro</a>
                 </li>
                 <li class="curso--cordas">
                     <a href="#">Cordas</a>
                 </li>
             </ul>
         </nav>
       </section>
       <section class="video">
         <video  controls class="video--mobile" src="video/video-promocional.mp4" poster="img/vid
eo-principal-mobile.png"></video>

         <video controls class="video--desktop" src="video/video-promocional.mp4" poster="img/vid
eo-principal.png"></video>

         <article class="video__textos">
           <h2 class="textos__titulo">Estude com os melhores professores</h2>
           <p>Aprenda no seu ritmo, sem sair de casa</p>
         </article>
       </section>
+      <section class="planos"> 
+        <h2 class="planos__titulo">Acesso ilimitado a todos os cursos</h2>
+        <article class="cards__planoanual">
+          <span class="plano--destaque"> + Assinado</span>
+          <div class="planos__card card--anual">
+            <h3 class="plano__titulo">Plano Anual</h3>
+            <p>12x <span class="valor--destaque">R$ 50,00</span></p>
+            <p>Valor total de R$ 600,00</p>
+            <span>Acesso à Alura Língua</span>
+            <a href="cursos.html" class="cards__botao botao">Matricule-se</a>
+          </div>
+        </article>
+        <article class="planos__card card--semestral">
+          <h3 class="plano__titulo">Plano Semestral</h3>
+          <p>12x <span class="valor--destaque">R$ 60,00</span></p>
+          <p>Valor total de R$ 360,00</p>
+          <a href="cursos.html" class="cards__botao botao">Matricule-se</a>
+        </article>
+        <article class="planos__pagamentos">
+          <p>Pagamento seguro com PayPal</p>
+          <p>Oferecemos boleto à vista, <a href="#">basta entrar em contato</a></p>
+        </article>
+      </section>
     </main>

     <footer class="rodape container">
       <section class="rodape__secao rodape__secao--sobre">
         <img class="rodape__logo" src="img/logo.svg" alt="Logo da MusicDot">

         <p class="rodape__infos-empresa">
           AOVS Sistemas de Informática S.A.

**228** 
49.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

           <br>
           CNPJ 05.555.382/0001-33 
           <br>
           Rua Vergueiro - São Paulo/SP
           <br>
           Telefone (11) 4118-3319
         </p>

         <ul class="rodape__lista-midias-sociais">
           <li class="rodape__item-midias-sociais">
             <a href="https://www.facebook.com/musicdotonline">
               <img src="img/footer-icone-facebook.svg" alt="MusicDot no Facebook">
             </a>
           </li>
           <li class="rodape__item-midias-sociais">
             <a href="https://www.youtube.com/user/musicdotonline">
               <img src="img/footer-icone-youtube.svg" alt="MusicDot no YouTube">
             </a>
           </li>
           <li class="rodape__item-midias-sociais">
             <a href="https://www.instagram.com/musicdotonline/">
               <img src="img/footer-icone-instagram.svg" alt="Instagram">
             </a>
           </li>
         </ul>
       </section>

       <section class="rodape__secao rodape__secao--cursos">
         <h2 class="rodape__titulo"> Cursos da MusicDot </h2>
         <nav>
           <ul>
             <li class="rodape_item-lista"><a href="#">Cursos de Teclado & Piano</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Violão/Guitarra</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Baixo</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Bateria</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Percussão</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Canto</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Áudio</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Teoria</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Sopro</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Cordas</a></li>
           </ul>
         </nav>
       </section>

       <section class="rodape__secao rodape__secao--links">
         <h2 class="rodape__titulo"> MusicDot </h2>
         <nav>
           <ul>
             <li class="rodape_item-lista"><a href="#">Apostila</a></li>
             <li class="rodape_item-lista"><a href="#">E-book</a></li>
             <li class="rodape_item-lista"><a href="#">Login</a></li>
             <li class="rodape_item-lista"><a href="#">Matricule-se</a></li>
             <li class="rodape_item-lista"><a href="#">Perguntas frequentes</a></li>
             <li class="rodape_item-lista"><a href="#">Para Escolas</a></li>
             <li class="rodape_item-lista"><a href="#">Contato</a></li>
           </ul>
         </nav>
       </section>

       <section class="rodape__secao rodape__secao--newsletter">
         <h2 class="rodape__titulo"> 
           Receba novidades e lançamentos 

49.2 PASSO A PASSO COM CÓDIGO 
**229**


--------------------------------------------------

         </h2>

         <form action="#" method="get" class="form-newsletter">
           <label for="form-newsletter__label" class="form-newsletter__label">
             Seu email pessoal
           </label>
           <input id="email-newsletter" name="email-newsletter" type="email" class="form-newslett
er__campo">

           <button type="submit" class="form-newsletter__botao">
             OK
           </button>
         </form>
       </section>
     </footer>
   </body>
 </html>

**230** 
49.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

CAPÍTULO 50

Figura 50.1: Seção dos benefícios mobile

# EXERCÍCIO: CONTEÚDO PRINCIPAL - OS
# BENEFÍCIOS

## 50.1 OBJETIVO

49 EXERCÍCIO: CONTEÚDO PRINCIPAL - OS BENEFÍCIOS 
**231**


--------------------------------------------------

Figura 50.2: Seção dos benefícios telas maiores

Editoras tradicionais pouco ligam para ebooks e novas tecnologias. Não dominam

tecnicamente o assunto para revisar os livros a fundo. Não têm anos de

experiência em didáticas com cursos.

Conheça a **Casa do Código**, uma editora diferente, com curadoria da **Caelum** e

obsessão por livros de qualidade a preços justos.

Casa do Código, ebook com preço de ebook.

1. Crie o arquivo ** beneficios.css **na pasta ** css **com o seguinte código:

+.beneficios {
+    text-align: center;
+    margin-bottom: 2rem;
+    padding: 0 10%;
+    display: flex;
+    flex-direction: column;
+    align-items: center;
+}
+
+.beneficios__titulo {
+    font-size: 1rem;
+    font-weight: 700;
+}
+
+.beneficios__lista li {
+    padding-top: 5.5rem;

**Editora Casa do Código com livros de uma forma diferente**

## 50.2 PASSO A PASSO COM CÓDIGO

**# css/beneficios.css**

**232** 
50.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

+    background-repeat: no-repeat;
+    background-size: 4rem 4rem;
+    background-position: top 20px center;
+}
+
+.beneficio--paravoce {
+    background-image: url(../img/icone-beneficios-tudo-para-voce.svg);
+}
+
+.beneficio--duvidas {
+    background-image: url(../img/icone-beneficios-nenhuma-duvida.svg);
+}
+
+.beneficio--didatica {
+    background-image: url(../img/icone-beneficios-didatica-cuidadosa.svg);
+}
+
+.beneficio--online {
+    background-image: url(../img/icone-beneficios-online.svg);
+}
+
+.beneficio__titulo {
+    font-size: .8rem;
+    font-weight: 600;
+    margin-top: 1rem;
+    margin-bottom: .2rem;
+}
+
+.beneficio__texto {
+    line-height: 1rem;
+}
+
+@media(min-width:768px) {
+    .beneficios {
+        margin-bottom: 3.7rem;
+    }
+    
+    .beneficios__lista {
+        display: grid;
+        grid-template-columns: 17.5rem 17.5rem;
+        gap: 1rem;
+    }
+    
+    .beneficios__titulo {
+        margin-bottom: 1rem;
+    }
+    
+    .beneficio__titulo {
+        font-size: 1.1rem;
+    }
+    
+    .beneficio__texto {
+        font-size: .8rem;
+    }
+}
+
+@media(min-width:1200px) {
+    .beneficios__titulo {
+        font-size: 1.3rem;
+    }
+    
+    .beneficios__lista {
+        gap: 1.3rem;

50.2 PASSO A PASSO COM CÓDIGO 
**233**


--------------------------------------------------

+        grid-template-columns: 22.5rem 22.5rem;
+    }
+    
+    .beneficios__lista li {
+        padding-top: 7.25rem;
+        background-size: 6rem 6rem;
+    }
+    
+    .beneficio__titulo {
+        font-size: 1.2rem;
+        margin-bottom: .6rem;
+    }
+    
+    .beneficio__texto {
+        font-size: .9rem;
+        line-height: 1.2rem;
+    }
+}

2. No arquivo ** index.html **na pasta ** raíz do projeto **faça as seguintes alterações:

 *<!doctype html>*
 <html>
   <head>
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width">
     <title>Musicdot</title>
     <link rel="icon" href="img/favicon.ico">
     <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:300,400,500,
600,700,&display=block">

     <link rel="stylesheet" href="css/reset.css">
     <link rel="stylesheet" href="css/container.css">
     <link rel="stylesheet" href="css/cabecalho.css">
     <link rel="stylesheet" href="css/cursos.css">
     <link rel="stylesheet" href="css/video.css">
     <link rel="stylesheet" href="css/planos.css">
+    <link rel="stylesheet" href="css/beneficios.css">
     <link rel="stylesheet" href="css/rodape.css">
     <link rel="stylesheet" href="css/form-newsletter.css">
   </head>
   <body>

     <header class="cabecalho container">
       <a href="index.html">
         <img class="cabecalho__logo" src="img/musicdot-logo-light.svg" title="Ir para a página i
nicial da Musicdot" alt="Musicdot">

       </a>

       <nav>
         <ul class="cabecalho__menu">
           <li class="cabecalho__item-menu"> <a href="sobre.html#contato"> Contato </a> </li>
           <li class="cabecalho__item-menu"> <a href="#"> Entrar </a> </li>
           <li class="cabecalho__item-menu cabecalho__item-menu--matricular"> <a href="#"> Matric
ule-se </a> </li>

         </ul>
       </nav>
     </header>

     <main>
       <section class="cursos">

**# index.html**

**234** 
50.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

         <article class="cursos__chamada --largura-grande">
           <h1 class="chamada__titulo">Cursos online de <strong class="chamada__titulo--destaque">
música</strong></h1>

           <p>Comece agora e aprenda sua primeira música em 10 minutos!</p>
           <a href="cursos.html" class="chamada__cursos__matricula botao">Matricule-se</a>
         </article>
         <nav>
             <ul class="cursos__lista">
                 <li class="curso--tecladopiano">
                     <a href="#">Teclado & Piano</a>
                 </li>
                 <li class="curso--violaoguitarra">
                     <a href="#">Violão & Guitarra</a>
                 </li>
                 <li class="curso--baixo">
                     <a href="#">Baixo</a>
                 </li>
                 <li class="curso--bateria curso--destaque">
                     <a href="#">Bateria</a>
                 </li>
                 <li class="curso--percussao">
                     <a href="#">Percussão</a>
                 </li>
                 <li class="curso--canto curso--destaque2">
                     <a href="#">Canto</a>
                 </li>
                 <li class="curso--audio">
                     <a href="#">Áudio</a>
                 </li>
                 <li class="curso--teoria">
                     <a href="#">Teoria</a>
                 </li>
                 <li class="curso--sopro">
                     <a href="#">Sopro</a>
                 </li>
                 <li class="curso--cordas">
                     <a href="#">Cordas</a>
                 </li>
             </ul>
         </nav>
       </section>
       <section class="video">
         <video  controls class="video--mobile" src="video/video-promocional.mp4" poster="img/vid
eo-principal-mobile.png"></video>

         <video controls class="video--desktop" src="video/video-promocional.mp4" poster="img/vid
eo-principal.png"></video>

         <article class="video__textos">
           <h2 class="textos__titulo">Estude com os melhores professores</h2>
           <p>Aprenda no seu ritmo, sem sair de casa</p>
         </article>
       </section>
       <section class="planos"> 
         <h2 class="planos__titulo">Acesso ilimitado a todos os cursos</h2>
         <article class="cards__planoanual">
           <span class="plano--destaque"> + Assinado</span>
           <div class="planos__card card--anual">
             <h3 class="plano__titulo">Plano Anual</h3>
             <p>12x <span class="valor--destaque">R$ 50,00</span></p>
             <p>Valor total de R$ 600,00</p>
             <span>Acesso à Alura Língua</span>
             <a href="cursos.html" class="cards__botao botao">Matricule-se</a>
           </div>
         </article>

50.2 PASSO A PASSO COM CÓDIGO 
**235**


--------------------------------------------------

         <article class="planos__card card--semestral">
           <h3 class="plano__titulo">Plano Semestral</h3>
           <p>12x <span class="valor--destaque">R$ 60,00</span></p>
           <p>Valor total de R$ 360,00</p>
           <a href="cursos.html" class="cards__botao botao">Matricule-se</a>
         </article>
         <article class="planos__pagamentos">
           <p>Pagamento seguro com PayPal</p>
           <p>Oferecemos boleto à vista, <a href="#">basta entrar em contato</a></p>
         </article>
       </section>
+      <section class="beneficios">
+        <h2 class="beneficios__titulo">Porque estudar na Musicdot?</h2>
+        <ul class="beneficios__lista">
+          <li class="beneficio--paravoce">
+            <h3 class="beneficio__titulo">Tudo para você realmente aprender</h3>
+            <p class="beneficio__texto">Você acessa todo o conteúdo! São aulas, exercícios, play
backs, cifras, partituras e tira dúvidas. Estudem em qualquer lugar, qualquer dia, qualquer horári
o, ilimitado. Matricule-se já</p>

+          </li>
+          <li class="beneficio--duvidas">
+            <h3 class="beneficio__titulo">Nenhuma dúvida sem resposta</h3>
+            <p class="beneficio__texto">Dúvidas são importantes para o seu aprendizado, e as dif
iculdades são normais. Na MusicDot você estuda com todo o suporte necessário. Além de todo conteúd
o, você tira dúvidas.</p>

+          </li>
+          <li class="beneficio--didatica">
+            <h3 class="beneficio__titulo">Didática cuidadosa que te faz aprender</h3>
+            <p class="beneficio__texto">Saber tocar não quer dizer saber ensinar. Na MusicDot vo
cê encontra os dois! Nosso orgulho é justo o extremo cuidado didático que temo com as aulas. Inves
timos muito tempo.</p>

+          </li>
+          <li class="beneficio--online">
+            <h3 class="beneficio__titulo">Estudar online é a melhor opção</h3>
+            <p class="beneficio__texto">Aprender em DVD e revistinha de banca são coisas do pass
ado! Estudar com um professor particular é bom, mas quem é o seu professor? A MusicDot te oferece 
a melhor aula, a qualquer hora.</p>

+          </li>
+        </ul>
+      </section>
     </main>

     <footer class="rodape container">
       <section class="rodape__secao rodape__secao--sobre">
         <img class="rodape__logo" src="img/logo.svg" alt="Logo da MusicDot">

         <p class="rodape__infos-empresa">
           AOVS Sistemas de Informática S.A.
           <br>
           CNPJ 05.555.382/0001-33 
           <br>
           Rua Vergueiro - São Paulo/SP
           <br>
           Telefone (11) 4118-3319
         </p>

         <ul class="rodape__lista-midias-sociais">
           <li class="rodape__item-midias-sociais">
             <a href="https://www.facebook.com/musicdotonline">
               <img src="img/footer-icone-facebook.svg" alt="MusicDot no Facebook">
             </a>
           </li>
           <li class="rodape__item-midias-sociais">

**236** 
50.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

             <a href="https://www.youtube.com/user/musicdotonline">
               <img src="img/footer-icone-youtube.svg" alt="MusicDot no YouTube">
             </a>
           </li>
           <li class="rodape__item-midias-sociais">
             <a href="https://www.instagram.com/musicdotonline/">
               <img src="img/footer-icone-instagram.svg" alt="Instagram">
             </a>
           </li>
         </ul>
       </section>

       <section class="rodape__secao rodape__secao--cursos">
         <h2 class="rodape__titulo"> Cursos da MusicDot </h2>
         <nav>
           <ul>
             <li class="rodape_item-lista"><a href="#">Cursos de Teclado & Piano</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Violão/Guitarra</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Baixo</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Bateria</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Percussão</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Canto</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Áudio</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Teoria</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Sopro</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Cordas</a></li>
           </ul>
         </nav>
       </section>

       <section class="rodape__secao rodape__secao--links">
         <h2 class="rodape__titulo"> MusicDot </h2>
         <nav>
           <ul>
             <li class="rodape_item-lista"><a href="#">Apostila</a></li>
             <li class="rodape_item-lista"><a href="#">E-book</a></li>
             <li class="rodape_item-lista"><a href="#">Login</a></li>
             <li class="rodape_item-lista"><a href="#">Matricule-se</a></li>
             <li class="rodape_item-lista"><a href="#">Perguntas frequentes</a></li>
             <li class="rodape_item-lista"><a href="#">Para Escolas</a></li>
             <li class="rodape_item-lista"><a href="#">Contato</a></li>
           </ul>
         </nav>
       </section>

       <section class="rodape__secao rodape__secao--newsletter">
         <h2 class="rodape__titulo"> 
           Receba novidades e lançamentos 
         </h2>

         <form action="#" method="get" class="form-newsletter">
           <label for="form-newsletter__label" class="form-newsletter__label">
             Seu email pessoal
           </label>
           <input id="email-newsletter" name="email-newsletter" type="email" class="form-newslett
er__campo">

           <button type="submit" class="form-newsletter__botao">
             OK
           </button>
         </form>
       </section>
     </footer>
   </body>

50.2 PASSO A PASSO COM CÓDIGO 
**237**


--------------------------------------------------

 </html>

**238** 
50.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

CAPÍTULO 51

1. Crie o arquivo ** chamada-youtube.css **na pasta ** css **com o seguinte código:

+.chamada__youtube {
+    background-color: #2e4255;
+    display: grid;
+    justify-items: center;
+}
+
+.chamada__youtube__canal {
+    color: #fff;
+    display: flex;
+    flex-direction: column;
+    align-items: center;
+    text-align: center;
+    padding: 1.2rem 2rem .9rem;
+    position: relative;
+    box-sizing: border-box;
+}
+
+.icone--youtube::before {
+    content: "";
+    width: 3rem;
+    height: 3rem;
+    background-image: url(../img/icone-youtube.svg);
+    background-size: 100%;
+    background-repeat: no-repeat;
+    position: absolute;
+    top: 0;
+    left: 50%;
+    transform: translate(-50%, -50%);
+}
+
+.canal__titulo {
+    color: #e93d50;
+    font-size: 1rem;
+    font-weight: 700;
+    margin-top: .9rem;
+    margin-bottom: .1rem;
+    letter-spacing: .5px;
+}
+
+.canal__texto {

# EXERCÍCIO: CONTEÚDO PRINCIPAL
# (OPCIONAL) - CHAMADA YOUTUBE

## 51.1 PASSO A PASSO COM CÓDIGO

**# css/chamada-youtube.css**

50 EXERCÍCIO: CONTEÚDO PRINCIPAL (OPCIONAL) - CHAMADA YOUTUBE 
**239**


--------------------------------------------------

+    font-size: .6rem;
+    letter-spacing: .8px;
+    line-height: 12px;
+    margin-bottom: 1rem;
+}
+
+.canal__button {
+    color: #fff;
+    background-color: #e93d50;
+}
+
+.video__descricao {
+    width: 85%;
+}
+
+.descricao__titulo {
+    font-size: .9rem;
+    font-weight: 500;
+    line-height: 15px;
+    margin-bottom: .5rem;
+}
+
+.descricao__titulo::before {
+    content: "";
+    width: 3rem;
+    height: 3rem;
+    background-image: url(../img/play-button.svg);
+    background-size: 100%;
+    display: block;
+    margin: 1.2rem auto 1rem;
+}
+
+.chamada__youtube--video1 {
+    background-image: url(../img/videos-thumbnail-video1.png);
+}
+
+.chamada__youtube--video2 {
+    background-image: url(../img/videos-thumbnail-video2.png);
+}
+
+.chamada__youtube--video1, .chamada__youtube--video2 {
+    background-size: cover;
+    width: 100%;
+}
+
+@media(min-width:768px) {
+    .chamada__youtube {
+        grid-template-columns: 1fr 1fr;
+        grid-template-areas:
+        "chamada chamada"
+        "video1 video2";
+    }
+    
+    .youtube__informacao {
+        padding: 2rem 17%;
+        box-sizing: border-box;
+        grid-area: chamada;
+    }
+    
+    .--icone-youtube::before {
+        width: 5rem;
+        height: 5rem;
+    }

**240** 
51.1 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

+    .chamada__youtube--video1 {
+        grid-area: video1;
+    }
+    
+    .chamada__youtube--video2 {
+        grid-area: video2;
+    }
+    
+    .canal__titulo {
+        font-size: 1.5rem;
+    }
+    
+    .descricao__texto {
+        font-size: .8rem;
+    }
+}
+
+@media(min-width:1200px) {
+    .youtube__informacao {
+        padding: 4rem 20%;
+    }
+    
+    .icone--youtube::before {
+        width: 6rem;
+        height: 6rem;
+    }
+    
+    .canal__titulo {
+        font-size: 2rem;
+        margin-bottom: .4rem;
+    }
+    
+    .canal__texto {
+        font-size: 1rem;
+        line-height: 1rem;
+    }
+    
+    .video__descricao {
+        width: 75%;
+        text-align: left;
+    }
+    
+    .descricao__titulo {
+        font-size: 1.2rem;
+        line-height: 1.4rem;
+        margin-bottom: 1.5rem;
+    }
+    
+    .descricao__texto {
+        font-size: .9rem;
+    }
+}

2. No arquivo ** index.html **na pasta ** raíz do projeto **faça as seguintes alterações:

 *<!doctype html>*
 <html>
   <head>
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width">

**# index.html**

51.1 PASSO A PASSO COM CÓDIGO 
**241**


--------------------------------------------------

     <title>Musicdot</title>
     <link rel="icon" href="img/favicon.ico">
     <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:300,400,500,
600,700,&display=block">

     <link rel="stylesheet" href="css/reset.css">
     <link rel="stylesheet" href="css/container.css">
     <link rel="stylesheet" href="css/cabecalho.css">
     <link rel="stylesheet" href="css/cursos.css">
     <link rel="stylesheet" href="css/video.css">
     <link rel="stylesheet" href="css/planos.css">
     <link rel="stylesheet" href="css/beneficios.css">
+    <link rel="stylesheet" href="css/chamada-youtube.css">
     <link rel="stylesheet" href="css/rodape.css">
     <link rel="stylesheet" href="css/form-newsletter.css">
   </head>
   <body>

     <header class="cabecalho container">
       <a href="index.html">
         <img class="cabecalho__logo" src="img/musicdot-logo-light.svg" title="Ir para a página i
nicial da Musicdot" alt="Musicdot">

       </a>

       <nav>
         <ul class="cabecalho__menu">
           <li class="cabecalho__item-menu"> <a href="sobre.html#contato"> Contato </a> </li>
           <li class="cabecalho__item-menu"> <a href="#"> Entrar </a> </li>
           <li class="cabecalho__item-menu cabecalho__item-menu--matricular"> <a href="#"> Matric
ule-se </a> </li>

         </ul>
       </nav>
     </header>

     <main>
       <section class="cursos">
         <article class="cursos__chamada --largura-grande">
           <h1 class="chamada__titulo">Cursos online de <strong class="chamada__titulo--destaque">
música</strong></h1>

           <p>Comece agora e aprenda sua primeira música em 10 minutos!</p>
           <a href="cursos.html" class="chamada__cursos__matricula botao">Matricule-se</a>
         </article>
         <nav>
             <ul class="cursos__lista">
                 <li class="curso--tecladopiano">
                     <a href="#">Teclado & Piano</a>
                 </li>
                 <li class="curso--violaoguitarra">
                     <a href="#">Violão & Guitarra</a>
                 </li>
                 <li class="curso--baixo">
                     <a href="#">Baixo</a>
                 </li>
                 <li class="curso--bateria curso--destaque">
                     <a href="#">Bateria</a>
                 </li>
                 <li class="curso--percussao">
                     <a href="#">Percussão</a>
                 </li>
                 <li class="curso--canto curso--destaque2">
                     <a href="#">Canto</a>
                 </li>
                 <li class="curso--audio">
                     <a href="#">Áudio</a>

**242** 
51.1 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

                 </li>
                 <li class="curso--teoria">
                     <a href="#">Teoria</a>
                 </li>
                 <li class="curso--sopro">
                     <a href="#">Sopro</a>
                 </li>
                 <li class="curso--cordas">
                     <a href="#">Cordas</a>
                 </li>
             </ul>
         </nav>
       </section>
       <section class="video">
         <video  controls class="video--mobile" src="video/video-promocional.mp4" poster="img/vid
eo-principal-mobile.png"></video>

         <video controls class="video--desktop" src="video/video-promocional.mp4" poster="img/vid
eo-principal.png"></video>

         <article class="video__textos">
           <h2 class="textos__titulo">Estude com os melhores professores</h2>
           <p>Aprenda no seu ritmo, sem sair de casa</p>
         </article>
       </section>
       <section class="planos"> 
         <h2 class="planos__titulo">Acesso ilimitado a todos os cursos</h2>
         <article class="cards__planoanual">
           <span class="plano--destaque"> + Assinado</span>
           <div class="planos__card card--anual">
             <h3 class="plano__titulo">Plano Anual</h3>
             <p>12x <span class="valor--destaque">R$ 50,00</span></p>
             <p>Valor total de R$ 600,00</p>
             <span>Acesso à Alura Língua</span>
             <a href="cursos.html" class="cards__botao botao">Matricule-se</a>
           </div>
         </article>
         <article class="planos__card card--semestral">
           <h3 class="plano__titulo">Plano Semestral</h3>
           <p>12x <span class="valor--destaque">R$ 60,00</span></p>
           <p>Valor total de R$ 360,00</p>
           <a href="cursos.html" class="cards__botao botao">Matricule-se</a>
         </article>
         <article class="planos__pagamentos">
           <p>Pagamento seguro com PayPal</p>
           <p>Oferecemos boleto à vista, <a href="#">basta entrar em contato</a></p>
         </article>
       </section>
       <section class="beneficios">
         <h2 class="beneficios__titulo">Porque estudar na Musicdot?</h2>
         <ul class="beneficios__lista">
           <li class="beneficio--paravoce">
             <h3 class="beneficio__titulo">Tudo para você realmente aprender</h3>
             <p class="beneficio__texto">Você acessa todo o conteúdo! São aulas, exercícios, play
backs, cifras, partituras e tira dúvidas. Estudem em qualquer lugar, qualquer dia, qualquer horári
o, ilimitado. Matricule-se já</p>

           </li>
           <li class="beneficio--duvidas">
             <h3 class="beneficio__titulo">Nenhuma dúvida sem resposta</h3>
             <p class="beneficio__texto">Dúvidas são importantes para o seu aprendizado, e as dif
iculdades são normais. Na MusicDot você estuda com todo o suporte necessário. Além de todo conteúd
o, você tira dúvidas.</p>

           </li>
           <li class="beneficio--didatica">
             <h3 class="beneficio__titulo">Didática cuidadosa que te faz aprender</h3>

51.1 PASSO A PASSO COM CÓDIGO 
**243**


--------------------------------------------------

             <p class="beneficio__texto">Saber tocar não quer dizer saber ensinar. Na MusicDot vo
cê encontra os dois! Nosso orgulho é justo o extremo cuidado didático que temo com as aulas. Inves
timos muito tempo.</p>

           </li>
           <li class="beneficio--online">
             <h3 class="beneficio__titulo">Estudar online é a melhor opção</h3>
             <p class="beneficio__texto">Aprender em DVD e revistinha de banca são coisas do pass
ado! Estudar com um professor particular é bom, mas quem é o seu professor? A MusicDot te oferece 
a melhor aula, a qualquer hora.</p>

           </li>
         </ul>
       </section>
+      <section class="chamada__youtube">
+        <article class="chamada__youtube__canal youtube__informacao icone--youtube --largura-gra
nde">

+          <h2 class="canal__titulo">Nosso canal no YouTube</h2>
+          <p class="canal__texto">Cursos online de Teclado, Piano, Canto, Violão, Guitarra, Teor
ia Musical e mais!</p>

+          <a href="https://www.youtube.com/user/musicdotonline" class="canal__button botao">Ver 
Canal</a>

+        </article>
+        <article class="chamada__youtube__canal chamada__youtube--video1">
+          <a class="video__descricao" href="#">
+            <h2 class="descricao__titulo">Aula de Canto para Iniciantes (dicas básicas)</h2>
+            <p class="descricao__texto">Nessa aula a professora Anny Cee dá as primeiras dicas p
ara você começar o seu estudo do Canto.</p>

+          </a>
+        </article>
+        <article class="chamada__youtube__canal chamada__youtube--video2">
+          <a class="video__descricao" href="#">
+            <h2 class="descricao__titulo">Toque teclado em 10 minutos! (Aula de teclado para ini
ciantes)</h2>

+            <p class="descricao__texto">Essa é a primeira aula do curso de teclado da MusicDot. 
Aqui você aprenderá a nomear todas...</p>

+          </a>
+        </article>
+      </section>
     </main>

     <footer class="rodape container">
       <section class="rodape__secao rodape__secao--sobre">
         <img class="rodape__logo" src="img/logo.svg" alt="Logo da MusicDot">

         <p class="rodape__infos-empresa">
           AOVS Sistemas de Informática S.A.
           <br>
           CNPJ 05.555.382/0001-33 
           <br>
           Rua Vergueiro - São Paulo/SP
           <br>
           Telefone (11) 4118-3319
         </p>

         <ul class="rodape__lista-midias-sociais">
           <li class="rodape__item-midias-sociais">
             <a href="https://www.facebook.com/musicdotonline">
               <img src="img/footer-icone-facebook.svg" alt="MusicDot no Facebook">
             </a>
           </li>
           <li class="rodape__item-midias-sociais">
             <a href="https://www.youtube.com/user/musicdotonline">
               <img src="img/footer-icone-youtube.svg" alt="MusicDot no YouTube">
             </a>

**244** 
51.1 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

           </li>
           <li class="rodape__item-midias-sociais">
             <a href="https://www.instagram.com/musicdotonline/">
               <img src="img/footer-icone-instagram.svg" alt="Instagram">
             </a>
           </li>
         </ul>
       </section>

       <section class="rodape__secao rodape__secao--cursos">
         <h2 class="rodape__titulo"> Cursos da MusicDot </h2>
         <nav>
           <ul>
             <li class="rodape_item-lista"><a href="#">Cursos de Teclado & Piano</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Violão/Guitarra</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Baixo</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Bateria</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Percussão</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Canto</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Áudio</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Teoria</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Sopro</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Cordas</a></li>
           </ul>
         </nav>
       </section>

       <section class="rodape__secao rodape__secao--links">
         <h2 class="rodape__titulo"> MusicDot </h2>
         <nav>
           <ul>
             <li class="rodape_item-lista"><a href="#">Apostila</a></li>
             <li class="rodape_item-lista"><a href="#">E-book</a></li>
             <li class="rodape_item-lista"><a href="#">Login</a></li>
             <li class="rodape_item-lista"><a href="#">Matricule-se</a></li>
             <li class="rodape_item-lista"><a href="#">Perguntas frequentes</a></li>
             <li class="rodape_item-lista"><a href="#">Para Escolas</a></li>
             <li class="rodape_item-lista"><a href="#">Contato</a></li>
           </ul>
         </nav>
       </section>

       <section class="rodape__secao rodape__secao--newsletter">
         <h2 class="rodape__titulo"> 
           Receba novidades e lançamentos 
         </h2>

         <form action="#" method="get" class="form-newsletter">
           <label for="form-newsletter__label" class="form-newsletter__label">
             Seu email pessoal
           </label>
           <input id="email-newsletter" name="email-newsletter" type="email" class="form-newslett
er__campo">

           <button type="submit" class="form-newsletter__botao">
             OK
           </button>
         </form>
       </section>
     </footer>
   </body>
 </html>

51.1 PASSO A PASSO COM CÓDIGO 
**245**


--------------------------------------------------

A **Alura** oferece centenas de **cursos online** em sua plataforma exclusiva de

ensino que favorece o aprendizado com a **qualidade** reconhecida da Caelum.
Você pode escolher um curso nas áreas de Programação, Front-end, Mobile,
Design & UX, Infra, Business, entre outras, com um plano que dá acesso a todos os cursos. Ex-

estudante da Caelum tem 10% de desconto neste link!

Conheça os cursos online Alura.

**Já conhece os cursos online Alura?**

**246** 
51.1 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

CAPÍTULO 52

Figura 52.1: Chamada aplicativos mobile

Figura 52.2: Chamada aplicativos telas maiores

# EXERCÍCIO: CONTEÚDO PRINCIPAL -
# CHAMADA DOS APLICATIVOS

## 52.1 OBJETIVO

51 EXERCÍCIO: CONTEÚDO PRINCIPAL - CHAMADA DOS APLICATIVOS 
**247**


--------------------------------------------------

Querendo aprender ainda mais sobre? Esclarecer dúvidas dos exercícios? Ouvir

explicações detalhadas com um instrutor?

A Caelum oferece o **curso data** presencial nas cidades de São Paulo, Rio de
Janeiro e Brasília, além de turmas incompany.

Consulte as vantagens do curso *Desenvolvimento Web com HTML, CSS e*
*JavaScript*

1. Crie o arquivo ** chamada-app.css **na pasta ** css **com o seguinte código:

+.chamada__aplicativo {
+    color: #fff;
+    text-align: center;
+    background-color: #f76148;
+    padding: 2rem 7.5%;
+    display: grid;
+    grid-template-columns: 1fr 1fr;
+    grid-template-rows: auto;
+    justify-items: center;
+}
+
+.aplicativo__titulo {
+    font-size: 1.2rem;
+    font-weight: 700;
+    margin-bottom: .8rem;
+    line-height: 24px;
+    grid-column-end: span 2;
+}
+
+.aplicativo__texto {
+    line-height: 20px;
+    margin-bottom: 15px;
+    grid-column-end: span 2; 
+}
+
+.texto__destaque {
+    font-weight: 600;
+}
+
+.chamada__aplicativo__button--wrapper {
+    display: flex;
+    justify-content: space-evenly;
+}

**Você pode também fazer o curso data dessa apostila na Caelum**

## 52.2 PASSO A PASSO COM CÓDIGO

**# css/chamada-app.css**

**248** 
52.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

+
+.aplicativo__button {
+    color: #e93d50;
+    font-weight: 600;
+    letter-spacing: 1.6px;
+    text-transform: uppercase;
+    background-color: #fff;
+    border: none;
+    border-radius: 5px;
+    width: 5.9rem;
+    padding: 1rem 0 1rem 1rem;
+    box-sizing: border-box;
+    font-size: .5rem;
+    background-size: 1.2rem;
+    background-repeat: no-repeat;
+}
+
+.app__download--android {
+    background-image: url(../img/icone-android-logo.svg);
+    background-position: left .5rem center;
+    padding-left: 1.4rem;
+}
+
+.app__download--ios {
+    background-image: url(../img/icone-apple-logo.svg);
+    background-position: left 1rem top .4rem;
+}
+
+.aplicativo--icone {
+    width: 1.2rem;
+    height: 1.2rem;
+    margin-right: .2rem;
+    vertical-align: middle;
+}
+
+@media(min-width:768px) {
+    .chamada__aplicativo {
+        background-image: url(../img/mockup-app.png);
+        background-size: 12rem;
+        background-position: left 20% center;
+        background-repeat: no-repeat;
+        padding: 5rem 20%;
+        grid-template-columns: 1fr 9rem 9rem;
+        column-gap: 1rem;
+        grid-template-areas: 
+        ". titulo titulo"
+        ". texto texto"
+        ". android ios";
+    }
+    
+    .aplicativo__titulo {
+        font-size: 1.5rem;
+        line-height: 29px;
+        grid-area: titulo;
+    }
+    
+    .aplicativo__texto {
+        line-height: 28px;
+        grid-area: texto;
+    }
+    
+    .app__download--android {
+        grid-area: android;

52.2 PASSO A PASSO COM CÓDIGO 
**249**


--------------------------------------------------

+        justify-self: flex-end;
+    }
+    
+    .app__download--ios {
+        grid-area: ios;
+        justify-self: flex-start;
+    }
+}
+
+@media(min-width:1200px) {
+    .chamada__aplicativo {
+        grid-template-columns: 1fr 12rem 12rem;
+    }
+    
+    .aplicativo__titulo {
+        font-size: 1.8rem;
+    }
+    
+    .aplicativo__button {
+        width: 9.5rem;
+        font-size: .8rem;
+        background-size: 1.8rem;
+        padding: 1.5rem 0 1.5rem 1rem;
+    }
+    
+    .app__download--android {
+        background-position: left .7rem top .8rem;
+        padding-left: 1.4rem;
+    }
+    
+    .app__download--ios {
+        background-position: left 1.3rem top .6rem;
+    }
+}

2. No arquivo ** index.html **na pasta ** raíz do projeto **faça as seguintes alterações:

 *<!doctype html>*
 <html>
   <head>
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width">
     <title>Musicdot</title>
     <link rel="icon" href="img/favicon.ico">
     <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:300,400,500,
600,700,&display=block">

     <link rel="stylesheet" href="css/reset.css">
     <link rel="stylesheet" href="css/container.css">
     <link rel="stylesheet" href="css/cabecalho.css">
     <link rel="stylesheet" href="css/cursos.css">
     <link rel="stylesheet" href="css/video.css">
     <link rel="stylesheet" href="css/planos.css">
     <link rel="stylesheet" href="css/beneficios.css">
     <link rel="stylesheet" href="css/chamada-youtube.css">
+    <link rel="stylesheet" href="css/chamada-app.css">
     <link rel="stylesheet" href="css/rodape.css">
     <link rel="stylesheet" href="css/form-newsletter.css">
   </head>
   <body>

**# index.html**

**250** 
52.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

     <header class="cabecalho container">
       <a href="index.html">
         <img class="cabecalho__logo" src="img/musicdot-logo-light.svg" title="Ir para a página i
nicial da Musicdot" alt="Musicdot">

       </a>

       <nav>
         <ul class="cabecalho__menu">
           <li class="cabecalho__item-menu"> <a href="sobre.html#contato"> Contato </a> </li>
           <li class="cabecalho__item-menu"> <a href="#"> Entrar </a> </li>
           <li class="cabecalho__item-menu cabecalho__item-menu--matricular"> <a href="#"> Matric
ule-se </a> </li>

         </ul>
       </nav>
     </header>

     <main>
       <section class="cursos">
         <article class="cursos__chamada --largura-grande">
           <h1 class="chamada__titulo">Cursos online de <strong class="chamada__titulo--destaque">
música</strong></h1>

           <p>Comece agora e aprenda sua primeira música em 10 minutos!</p>
           <a href="cursos.html" class="chamada__cursos__matricula botao">Matricule-se</a>
         </article>
         <nav>
             <ul class="cursos__lista">
                 <li class="curso--tecladopiano">
                     <a href="#">Teclado & Piano</a>
                 </li>
                 <li class="curso--violaoguitarra">
                     <a href="#">Violão & Guitarra</a>
                 </li>
                 <li class="curso--baixo">
                     <a href="#">Baixo</a>
                 </li>
                 <li class="curso--bateria curso--destaque">
                     <a href="#">Bateria</a>
                 </li>
                 <li class="curso--percussao">
                     <a href="#">Percussão</a>
                 </li>
                 <li class="curso--canto curso--destaque2">
                     <a href="#">Canto</a>
                 </li>
                 <li class="curso--audio">
                     <a href="#">Áudio</a>
                 </li>
                 <li class="curso--teoria">
                     <a href="#">Teoria</a>
                 </li>
                 <li class="curso--sopro">
                     <a href="#">Sopro</a>
                 </li>
                 <li class="curso--cordas">
                     <a href="#">Cordas</a>
                 </li>
             </ul>
         </nav>
       </section>
       <section class="video">
         <video  controls class="video--mobile" src="video/video-promocional.mp4" poster="img/vid
eo-principal-mobile.png"></video>

         <video controls class="video--desktop" src="video/video-promocional.mp4" poster="img/vid

52.2 PASSO A PASSO COM CÓDIGO 
**251**


--------------------------------------------------

eo-principal.png"></video>

         <article class="video__textos">
           <h2 class="textos__titulo">Estude com os melhores professores</h2>
           <p>Aprenda no seu ritmo, sem sair de casa</p>
         </article>
       </section>
       <section class="planos"> 
         <h2 class="planos__titulo">Acesso ilimitado a todos os cursos</h2>
         <article class="cards__planoanual">
           <span class="plano--destaque"> + Assinado</span>
           <div class="planos__card card--anual">
             <h3 class="plano__titulo">Plano Anual</h3>
             <p>12x <span class="valor--destaque">R$ 50,00</span></p>
             <p>Valor total de R$ 600,00</p>
             <span>Acesso à Alura Língua</span>
             <a href="cursos.html" class="cards__botao botao">Matricule-se</a>
           </div>
         </article>
         <article class="planos__card card--semestral">
           <h3 class="plano__titulo">Plano Semestral</h3>
           <p>12x <span class="valor--destaque">R$ 60,00</span></p>
           <p>Valor total de R$ 360,00</p>
           <a href="cursos.html" class="cards__botao botao">Matricule-se</a>
         </article>
         <article class="planos__pagamentos">
           <p>Pagamento seguro com PayPal</p>
           <p>Oferecemos boleto à vista, <a href="#">basta entrar em contato</a></p>
         </article>
       </section>
       <section class="beneficios">
         <h2 class="beneficios__titulo">Porque estudar na Musicdot?</h2>
         <ul class="beneficios__lista">
           <li class="beneficio--paravoce">
             <h3 class="beneficio__titulo">Tudo para você realmente aprender</h3>
             <p class="beneficio__texto">Você acessa todo o conteúdo! São aulas, exercícios, play
backs, cifras, partituras e tira dúvidas. Estudem em qualquer lugar, qualquer dia, qualquer horári
o, ilimitado. Matricule-se já</p>

           </li>
           <li class="beneficio--duvidas">
             <h3 class="beneficio__titulo">Nenhuma dúvida sem resposta</h3>
             <p class="beneficio__texto">Dúvidas são importantes para o seu aprendizado, e as dif
iculdades são normais. Na MusicDot você estuda com todo o suporte necessário. Além de todo conteúd
o, você tira dúvidas.</p>

           </li>
           <li class="beneficio--didatica">
             <h3 class="beneficio__titulo">Didática cuidadosa que te faz aprender</h3>
             <p class="beneficio__texto">Saber tocar não quer dizer saber ensinar. Na MusicDot vo
cê encontra os dois! Nosso orgulho é justo o extremo cuidado didático que temo com as aulas. Inves
timos muito tempo.</p>

           </li>
           <li class="beneficio--online">
             <h3 class="beneficio__titulo">Estudar online é a melhor opção</h3>
             <p class="beneficio__texto">Aprender em DVD e revistinha de banca são coisas do pass
ado! Estudar com um professor particular é bom, mas quem é o seu professor? A MusicDot te oferece 
a melhor aula, a qualquer hora.</p>

           </li>
         </ul>
       </section>
       <section class="chamada__youtube">
         <article class="chamada__youtube__canal youtube__informacao icone--youtube --largura-gra
nde">

           <h2 class="canal__titulo">Nosso canal no YouTube</h2>
           <p class="canal__texto">Cursos online de Teclado, Piano, Canto, Violão, Guitarra, Teor

**252** 
52.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

ia Musical e mais!</p>

           <a href="https://www.youtube.com/user/musicdotonline" class="canal__button botao">Ver 
Canal</a>

         </article>
         <article class="chamada__youtube__canal chamada__youtube--video1">
           <a class="video__descricao" href="#">
             <h2 class="descricao__titulo">Aula de Canto para Iniciantes (dicas básicas)</h2>
             <p class="descricao__texto">Nessa aula a professora Anny Cee dá as primeiras dicas p
ara você começar o seu estudo do Canto.</p>

           </a>
         </article>
         <article class="chamada__youtube__canal chamada__youtube--video2">
           <a class="video__descricao" href="#">
             <h2 class="descricao__titulo">Toque teclado em 10 minutos! (Aula de teclado para ini
ciantes)</h2>

             <p class="descricao__texto">Essa é a primeira aula do curso de teclado da MusicDot. 
Aqui você aprenderá a nomear todas...</p>

           </a>
         </article>
       </section>
+      <section class="chamada__aplicativo">
+        <h2 class="aplicativo__titulo">Estude em qualquer lugar com o App</h2>
+        <p class="aplicativo__texto">Com o aplicativo da MusicDot você baixa as aulas para estud
ar offline e fazer os exercícios. Disponível para Android e iOS. Já é aluno? <strong class="texto-
destaque">Baixe já:</strong></p>

+        <a href="https://play.google.com/store/apps/details?id=br.com.musicdot&hl=en" class="apl
icativo__button app__download--android botao">Android</a>

+        <a href="https://apps.apple.com/br/app/musicdot/id1333842849" class="aplicativo__button 
app__download--ios botao">iOS</a>

+      </section>
     </main>

     <footer class="rodape container">
       <section class="rodape__secao rodape__secao--sobre">
         <img class="rodape__logo" src="img/logo.svg" alt="Logo da MusicDot">

         <p class="rodape__infos-empresa">
           AOVS Sistemas de Informática S.A.
           <br>
           CNPJ 05.555.382/0001-33 
           <br>
           Rua Vergueiro - São Paulo/SP
           <br>
           Telefone (11) 4118-3319
         </p>

         <ul class="rodape__lista-midias-sociais">
           <li class="rodape__item-midias-sociais">
             <a href="https://www.facebook.com/musicdotonline">
               <img src="img/footer-icone-facebook.svg" alt="MusicDot no Facebook">
             </a>
           </li>
           <li class="rodape__item-midias-sociais">
             <a href="https://www.youtube.com/user/musicdotonline">
               <img src="img/footer-icone-youtube.svg" alt="MusicDot no YouTube">
             </a>
           </li>
           <li class="rodape__item-midias-sociais">
             <a href="https://www.instagram.com/musicdotonline/">
               <img src="img/footer-icone-instagram.svg" alt="Instagram">
             </a>
           </li>
         </ul>

52.2 PASSO A PASSO COM CÓDIGO 
**253**


--------------------------------------------------

       </section>

       <section class="rodape__secao rodape__secao--cursos">
         <h2 class="rodape__titulo"> Cursos da MusicDot </h2>
         <nav>
           <ul>
             <li class="rodape_item-lista"><a href="#">Cursos de Teclado & Piano</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Violão/Guitarra</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Baixo</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Bateria</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Percussão</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Canto</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Áudio</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Teoria</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Sopro</a></li>
             <li class="rodape_item-lista"><a href="#">Cursos de Cordas</a></li>
           </ul>
         </nav>
       </section>

       <section class="rodape__secao rodape__secao--links">
         <h2 class="rodape__titulo"> MusicDot </h2>
         <nav>
           <ul>
             <li class="rodape_item-lista"><a href="#">Apostila</a></li>
             <li class="rodape_item-lista"><a href="#">E-book</a></li>
             <li class="rodape_item-lista"><a href="#">Login</a></li>
             <li class="rodape_item-lista"><a href="#">Matricule-se</a></li>
             <li class="rodape_item-lista"><a href="#">Perguntas frequentes</a></li>
             <li class="rodape_item-lista"><a href="#">Para Escolas</a></li>
             <li class="rodape_item-lista"><a href="#">Contato</a></li>
           </ul>
         </nav>
       </section>

       <section class="rodape__secao rodape__secao--newsletter">
         <h2 class="rodape__titulo"> 
           Receba novidades e lançamentos 
         </h2>

         <form action="#" method="get" class="form-newsletter">
           <label for="form-newsletter__label" class="form-newsletter__label">
             Seu email pessoal
           </label>
           <input id="email-newsletter" name="email-newsletter" type="email" class="form-newslett
er__campo">

           <button type="submit" class="form-newsletter__botao">
             OK
           </button>
         </form>
       </section>
     </footer>
   </body>
 </html>

**254** 
52.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

CAPÍTULO 53

Uma tendência em alta no mundo front-end é o uso de frameworks CSS com estilos base para nossa

página. Ao invés de começar todo projeto do zero, criando todo estilo na mão, existem frameworks que
já trazem toda uma base construída de onde partiremos nossa aplicação.

Existem muitas opções mas o **Bootstrap** talvez seja o de maior notoriedade. Ele foi criado pelo
pessoal do Twitter a partir de códigos que eles já usavam internamente. Foi liberado como opensource e
ganhou muitos adeptos. O projeto cresceu bastante em maturidade e importância no mercado a ponto de

se desvincular do Twitter e ser apenas o **Bootstrap**.

https://getbootstrap.com/

O Bootstrap traz uma série de recursos:

Reset CSS

Estilo visual base pra maioria das tags

Ícones

Grids prontos pra uso
Componentes CSS

Plugins JavaScript

Tudo responsivo e mobile-first

Para usar o Bootstrap, apenas incluímos seu CSS na página:

<link rel="stylesheet" href="css/bootstrap.css">

Só isso já nos traz uma série de benefícios. Um reset é aplicado, e nossas tags ganham estilo e

tipografia base. Isso quer dizer que podemos usar tags como um H1 ou um P agora e elas terão um estilo
característico do Bootstrap.

Além disso, ganhamos **muitas classes** com componentes adicionais que podemos aplicar na página.

São várias opções. Por exemplo, pra criar um título com uma frase de abertura em destaque, usamos o
Jumbotron:

<div class="jumbotron jumbotron-fluid">

   <div class="container">

# BOOTSTRAP E FRAMEWORKS DE CSS

## 53.1 ESTILO E COMPONENTES BASE

52 BOOTSTRAP E FRAMEWORKS DE CSS 
**255**


--------------------------------------------------

       <h1 class="display-4">Ótima escolha!</h1>
       <p class="lead">Obrigado por comprar na Mirror Fashion.</p>
   </div>
</div>

O Bootstrap utiliza a idéia de reaproveitamento de classes que vimos em capítulos anteriores para
estilizar páginas. No exemplo acima, para criar um componente do tipo *jumbotron* nós só precisamos
criar um elemento e chamar a classe que representa esse componente. Isso facilita muito na hora de criar

páginas do zero porque se a pessoa já está acostumada com a nomenclatura e conhece bem os
componentes do Bootstrap, já é possível escrever o HTML com os nomes de classes corretos. Então
reduz o tempo quase que pela metade na hora de desenvolver porque não precisamos mais focar tanto

em propriedades CSS e sim em estrutura. Na documentação do Bootstrap existem vários exemplos de
estruturas que podemos literalmente copiar e colar e alterar para o conteúdo que precisamos.

A recomendação para o uso do Bootstrap (principalmente para pessoas novas com o framework) é
deixar uma aba aberta do navegador com a documentação para conferir os componentes, estruturas
e ferramentas enquanto escreve a estrutura.

Podemos fazer nossa prórpria adaptação do CSS do Bootstrap. Basta sobrescrever as classes que
queremos usar em um arquivo separado e fazer o import depois do CSS do Bootstrap.

Alguns componentes do Bootstrap possuem interatividade com o usuário através de JavaScript,
então além de importar o arquivo CSS precisamos importar também o arquivo de javaScript. Só que

para o JavaScript do Bootstrap funcionar ele precisa de um outro framework chamado *JQuery*.

https://jquery.com/

A importação desses JavaScripts é feita logo antes do fechamento da tag  </body>  e o import do

*JQuery* deve vir antes do arquivo do Bootstrap:

...

   <script src="js/jquery.js"></script>
   <script src="js/bootstrap.js.js"></script>
</body>
</html>

**256** 
53.1 ESTILO E COMPONENTES BASE


--------------------------------------------------

Conheça a **Casa do Código**, uma **nova** editora, com autores de destaque no

mercado, foco em **ebooks** (PDF, epub, mobi), preços **imbatíveis** e assuntos
**atuais**.
Com a curadoria da **Caelum** e excelentes autores, é uma abordagem **diferente**

para livros de tecnologia no Brasil.

Casa do Código, Livros de Tecnologia.

**Seus livros de tecnologia parecem do século passado?**

53.1 ESTILO E COMPONENTES BASE 
**257**


--------------------------------------------------

CAPÍTULO 54

Para começar a usar o Bootstrap primeiro importe três arquivos importantes:

- bootstrap.css
- jquery.js
- bootstrap.js

Depois abra a documentação do Bootstrap e procure pela estrutura exemplo de um header.
Modifique para que o header contenha a logo da musicdot e que possua três links:

- Cursos
- Matrículas
- Email

Dentro da tag  <main> crie a estrutura de um Jumbotron e, assim como no header, modifique-o para

que fique com os textos certos. No título do Jumbotron: "Escolher cursos" e no parágrafo abaixo do

título: "Escolha os cursos que gostaria de se matricular". Para estilizar toda a página utilize as classes css
necessárias que estão na documentação do Bootstrap.

Se você está gostando dessa apostila, certamente vai aproveitar os **cursos**

**online** que lançamos na plataforma **Alura**. Você estuda a qualquer momento
com a **qualidade** Caelum. Programação, Mobile, Design, Infra, Front-End e
Business, entre outros! Ex-estudante da Caelum tem 10% de desconto, siga o link!

Conheça a Alura Cursos Online.

# EXERCÍCIO: PRIMEIROS PASSOS COM
# BOOTSTRAP

## 54.1 OBJETIVO

**Agora é a melhor hora de aprender algo novo**

## 54.2 PASSO A PASSO COM CÓDIGO

**258** 
53 EXERCÍCIO: PRIMEIROS PASSOS COM BOOTSTRAP


--------------------------------------------------

1. Crie o arquivo ** matricula.html **na pasta ** raíz do projeto **com o seguinte código:

+*<!DOCTYPE html>*
+<html>
+<head>
+    <title>Matriculas</title>
+    <meta charset="utf-8">
+    <meta name="viewport" content="width=device-width">
+    <link href="css/bootstrap.css" rel="stylesheet">
+    <link href="img/favicon.ico" rel="icon">
+</head>
+<body>
+    <header class="header">
+        <nav class="navbar navbar-expand-sm navbar-dark bg-dark">
+            <a class="navbar-brand" href="index.html"><img class="header-navbar-logo" src="img/m
usicdot-logo-light.svg" alt="Logo da Musicdot"></a>

+            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#na
vbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Tog
gle navigation">

+                <span class="navbar-toggler-icon"></span>
+            </button>
+            <div class="collapse navbar-collapse" id="navbarSupportedContent">
+                <ul class="navbar-nav mr-auto">
+                    <li class="nav-item active">
+                        <a class="nav-link" href="#">Cursos</a>
+                    </li>
+                    <li class="nav-item">
+                        <a class="nav-link" href="#">Matriculas</a>
+                    </li>
+                    <li class="nav-item">
+                        <a href="#" class="nav-link">Emails</a>
+                    </li>
+                </ul>
+            </div>
+        </nav>
+    </header>
+    <main class="container mb-4">
+        <div class="jumbotron bg-dark text-light mt-3">
+            <div class="container">
+                <h1>Escolher cursos</h1>
+                <p class="lead">Escolha os cursos que gostaria de se matricular</p>
+            </div>
+        </div>
+    </main>
+    <script src="js/jquery.js"></script>
+    <script src="js/bootstrap.js"></script>
+</body>
+</html>

**# matricula.html**

54.2 PASSO A PASSO COM CÓDIGO 
**259**


--------------------------------------------------

CAPÍTULO 55

Crie um novo arquivo css que irá conter as mudanças do peso da fonte do título do jumbotron para  600 

e a largura da imagem para  8rem  e um espaçamento externo à direta da imagem de  1rem . Não

esqueça de criar classes para esses elementos.

Editoras tradicionais pouco ligam para ebooks e novas tecnologias. Não dominam
tecnicamente o assunto para revisar os livros a fundo. Não têm anos de
experiência em didáticas com cursos.
Conheça a **Casa do Código**, uma editora diferente, com curadoria da **Caelum** e
obsessão por livros de qualidade a preços justos.

Casa do Código, ebook com preço de ebook.

1. Crie o arquivo ** matricula.css **na pasta ** css **com o seguinte código:

+.header-navbar-logo {
+    width: 8rem;
+    margin-right: 1rem;
+}
+
+.header-matricula h1 {
+    font-weight: 300;
+}

# EXERCÍCIO: CUSTOMIZANDO O
# BOOTSTRAP (OPICIONAL)

## 55.1 OBJETIVO

**Editora Casa do Código com livros de uma forma diferente**

## 55.2 PASSO A PASSO COM CÓDIGO

**# css/matricula.css**

**260** 
54 EXERCÍCIO: CUSTOMIZANDO O BOOTSTRAP (OPICIONAL)


--------------------------------------------------

2. No arquivo ** matricula.html **na pasta ** raíz do projeto **faça as seguintes alterações:

 *<!DOCTYPE html>*
 <html>
 <head>
     <title>Matriculas</title>
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width">
     <link href="css/bootstrap.css" rel="stylesheet">
+    <link href="css/matricula.css" rel="stylesheet">
     <link href="img/favicon.ico" rel="icon">
 </head>
 <body>
     <header class="header">
         <nav class="navbar navbar-expand-sm navbar-dark bg-dark">
             <a class="navbar-brand" href="index.html"><img class="header-navbar-logo" src="img/m
usicdot-logo-light.svg" alt="Logo da Musicdot"></a>

             <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#na
vbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Tog
gle navigation">

                 <span class="navbar-toggler-icon"></span>
             </button>
             <div class="collapse navbar-collapse" id="navbarSupportedContent">
                 <ul class="navbar-nav mr-auto">
                     <li class="nav-item active">
                         <a class="nav-link" href="#">Cursos</a>
                     </li>
                     <li class="nav-item">
                         <a class="nav-link" href="#">Matriculas</a>
                     </li>
                     <li class="nav-item">
                         <a href="#" class="nav-link">Emails</a>
                     </li>
                 </ul>
             </div>
         </nav>
     </header>
     <main class="container mb-4">
-        <̶d̶i̶v̶ c̶l̶a̶s̶s̶=̶"̶j̶u̶m̶b̶o̶t̶r̶o̶n̶ b̶g̶-̶d̶a̶r̶k̶ t̶e̶x̶t̶-̶l̶i̶g̶h̶t̶ m̶t̶-̶3̶"̶>
+        <div class="jumbotron bg-dark header-matricula text-light mt-3">
             <div class="container">
                 <h1>Escolher cursos</h1>
                 <p class="lead">Escolha os cursos que gostaria de se matricular</p>
             </div>
         </div>
     </main>
     <script src="js/jquery.js"></script>
     <script src="js/bootstrap.js"></script>
 </body>
 </html>

**# matricula.html**

55.2 PASSO A PASSO COM CÓDIGO 
**261**


--------------------------------------------------

CAPÍTULO 56

Construa a estrutura de uma tabela contendo 3 informações no cabeçalho:

- (espaço vazio)
- Nome do curso
- Tempo/Carga Horária

No corpo da tabela coloque na primeira coluna um  <input>  do tipo  checkbox  com o valor do

tempo/carga horária. Na segunda coluna coloque o nome de algum curso e na terceira coluna coloque o
valor em horas do tempo/carga horária.

Não esqueça de colocar as classes como na documentação do Bootstrap

A **Alura** oferece centenas de **cursos online** em sua plataforma exclusiva de
ensino que favorece o aprendizado com a **qualidade** reconhecida da Caelum.

Você pode escolher um curso nas áreas de Programação, Front-end, Mobile,
Design & UX, Infra, Business, entre outras, com um plano que dá acesso a todos os cursos. Ex-
estudante da Caelum tem 10% de desconto neste link!

Conheça os cursos online Alura.

1. No arquivo ** matricula.css **na pasta ** css **faça as seguintes alterações:

 .header-navbar-logo {
     width: 8rem;
     margin-right: 1rem;
 }

# EXERCÍCIO: A TABELA DE CURSOS

## 56.1 OBJETIVO

**Já conhece os cursos online Alura?**

## 56.2 PASSO A PASSO COM CÓDIGO

**# css/matricula.css**

**262** 
55 EXERCÍCIO: A TABELA DE CURSOS


--------------------------------------------------

 .header-matricula h1 {
     font-weight: 300;
 }
+
+.rounded-top {
+    overflow: hidden;
+}

2. No arquivo ** matricula.html **na pasta ** raíz do projeto **faça as seguintes alterações:

 *<!DOCTYPE html>*
 <html>
 <head>
     <title>Matriculas</title>
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width">
     <link href="css/bootstrap.css" rel="stylesheet">
     <link href="css/matricula.css" rel="stylesheet">
     <link href="img/favicon.ico" rel="icon">
 </head>
 <body>
     <header class="header">
         <nav class="navbar navbar-expand-sm navbar-dark bg-dark">
             <a class="navbar-brand" href="index.html"><img class="header-navbar-logo" src="img/m
usicdot-logo-light.svg" alt="Logo da Musicdot"></a>

             <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#na
vbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Tog
gle navigation">

                 <span class="navbar-toggler-icon"></span>
             </button>
             <div class="collapse navbar-collapse" id="navbarSupportedContent">
                 <ul class="navbar-nav mr-auto">
                     <li class="nav-item active">
                         <a class="nav-link" href="#">Cursos</a>
                     </li>
                     <li class="nav-item">
                         <a class="nav-link" href="#">Matriculas</a>
                     </li>
                     <li class="nav-item">
                         <a href="#" class="nav-link">Emails</a>
                     </li>
                 </ul>
             </div>
         </nav>
     </header>
     <main class="container mb-4">
         <div class="jumbotron bg-dark header-matricula text-light mt-3">
             <div class="container">
                 <h1>Escolher cursos</h1>
                 <p class="lead">Escolha os cursos que gostaria de se matricular</p>
             </div>
         </div>
+        <table class="table table-hover rounded-top">
+            <thead class="thead-dark">
+                <tr>
+                    <th scope="col"></th>
+                    <th scope="col">Curso</th>
+                    <th scope="col">Tempo</th>
+                </tr>

**# matricula.html**

56.2 PASSO A PASSO COM CÓDIGO 
**263**


--------------------------------------------------

+            </thead>
+            <tbody>
+                <tr>
+                    <td><input type="checkbox" name="curso" value="20"></td>
+                    <td>Curso de Violão</td>
+                    <td>20h</td>
+                </tr>
+                <tr>
+                    <td><input type="checkbox" name="curso" value="30"></td>
+                    <td>Curso de Bambolê</td>
+                    <td>30h</td>
+                </tr>
+                <tr>
+                    <td><input type="checkbox" name="curso" value="12"></td>
+                    <td>Curso de Java</td>
+                    <td>12h</td>
+                </tr>
+                <tr>
+                    <td><input type="checkbox" name="curso" value="20"></td>
+                    <td>Curso de Violão</td>
+                    <td>20h</td>
+                </tr>
+                <tr>
+                    <td><input type="checkbox" name="curso" value="30"></td>
+                    <td>Curso de Bambolê</td>
+                    <td>30h</td>
+                </tr>
+                <tr>
+                    <td><input type="checkbox" name="curso" value="12"></td>
+                    <td>Curso de Java</td>
+                    <td>12h</td>
+                </tr>
+                <tr>
+                    <td><input type="checkbox" name="curso" value="20"></td>
+                    <td>Curso de Violão</td>
+                    <td>20h</td>
+                </tr>
+                <tr>
+                    <td><input type="checkbox" name="curso" value="30"></td>
+                    <td>Curso de Bambolê</td>
+                    <td>30h</td>
+                </tr>
+                <tr>
+                    <td><input type="checkbox" name="curso" value="12"></td>
+                    <td>Curso de Java</td>
+                    <td>12h</td>
+                </tr>
+                <tr>
+                    <td><input type="checkbox" name="curso" value="20"></td>
+                    <td>Curso de Violão</td>
+                    <td>20h</td>
+                </tr>
+                <tr>
+                    <td><input type="checkbox" name="curso" value="30"></td>
+                    <td>Curso de Bambolê</td>
+                    <td>30h</td>
+                </tr>
+                <tr>
+                    <td><input type="checkbox" name="curso" value="12"></td>
+                    <td>Curso de Java</td>
+                    <td>12h</td>
+                </tr>
+                <tr class="bg-dark text-light">

**264** 
56.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

+                    <td>Total</td>
+                    <td class="js-total-de-cursos">0 curso(s)</td>
+                    <td class="js-total-de-horas">0h</td>
+                </tr>
+            </tbody>
+        </table>
+        <button type="button" class="btn btn-outline-dark btn-lg mb-4">Confirmar Matrícula</butt
on>

     </main>
     <script src="js/jquery.js"></script>
     <script src="js/bootstrap.js"></script>
 </body>
 </html>

56.2 PASSO A PASSO COM CÓDIGO 
**265**


--------------------------------------------------

CAPÍTULO 57

No início da *Internet* as páginas eram pouco ou nada interativas, eram documentos que apresentavam
seu conteúdo exatamente como foram criados para serem exibidos no navegador. Existiam algumas

tecnologias para a geração de páginas no lado do servidor, mas havia limitações no que diz respeito a
como o usuário consumia aquele conteúdo. Navegar através de *links* e enviar informações através de

formulários era basicamente tudo o que se podia fazer.

Visando o potencial da *Internet* para o público geral e a necessidade de haver uma interação maior
do usuário com as páginas, a Netscape, criadora do navegador mais popular do início dos anos 90, de
mesmo nome, criou o Livescript, uma linguagem simples que permitia a execução de *scripts* contidos

nas páginas dentro do próprio navegador.

Aproveitando o iminente sucesso do Java, que vinha conquistando cada vez mais espaço no mercado
de desenvolvimento de aplicações corporativas, a Netscape logo rebatizou o Livescript como JavaScript
num acordo com a Sun para alavancar o uso das duas. A então vice-líder dos navegadores, Microsoft,

adicionou ao Internet Explorer o suporte a *scripts* escritos em VBScript e criou sua própria versão de
JavaScript, o JScript.

JavaScript é a linguagem de programação mais popular no desenvolvimento Web. Suportada por

todos os navegadores, a linguagem é responsável por praticamente qualquer tipo de dinamismo que
queiramos em nossas páginas.

Se usarmos todo o poder que ela tem para oferecer, podemos chegar a resultados impressionantes.
Excelentes exemplos disso são aplicações Web complexas como Gmail, Google Maps e Google Docs.

# UM POUQUINHO DA HISTÓRIA DO
# JAVASCRIPT

## 57.1 HISTÓRIA

**266** 
56 UM POUQUINHO DA HISTÓRIA DO JAVASCRIPT


--------------------------------------------------

Querendo aprender ainda mais sobre? Esclarecer dúvidas dos exercícios? Ouvir

explicações detalhadas com um instrutor?

A Caelum oferece o **curso data** presencial nas cidades de São Paulo, Rio de
Janeiro e Brasília, além de turmas incompany.

Consulte as vantagens do curso *Desenvolvimento Web com HTML, CSS e*
*JavaScript*

O JavaScript, como o próprio nome sugere, é uma linguagem de *scripting*. Uma linguagem de

*scripting* é comumente definida como uma linguagem de programação que permite ao programador
controlar uma ou mais aplicações de terceiros. No caso do JavaScript, podemos controlar alguns
comportamentos dos navegadores através de trechos de código que são enviados na página HTML.

Outra característica comum nas linguagens de *scripting* é que normalmente elas são linguagens

**interpretadas**, ou seja, não dependem de compilação para serem executadas. Essa característica é
presente no JavaScript: o código é interpretado e executado conforme é lido pelo navegador, linha a
linha, assim como o HTML.

O JavaScript também possui **grande tolerância a erros**, uma vez que conversões automáticas são

realizadas durante operações. Como será visto no decorrer das explicações, nem sempre essas
conversões resultam em algo esperado, o que pode ser fonte de muitos bugs, caso não conheçamos bem
esse mecanismo.

O script do programador é enviado com o HTML para o navegador, mas como o navegador saberá
diferenciar o script de um código html? Para que essa diferenciação seja possível, é necessário envolver

o script dentro da tag  <script> .

Existem várias formas de executar códigos JavaScript em um página. Uma delas é executar códigos
no que chamamos de **Console**. A maioria dos navegadores desktop já vem com essa ferramenta

instalada. No Chrome, por exemplo, é possível chegar ao Console apertando **F12** e em seguida acessar a
aba "Console" ou por meio do atalho de teclado **Control + Shift + i**.

**Você pode também fazer o curso data dessa apostila na Caelum**

## 57.2 CARACTERÍSTICAS DA LINGUAGEM

## 57.3 CONSOLE DO NAVEGADOR

57.2 CARACTERÍSTICAS DA LINGUAGEM 
**267**


--------------------------------------------------

**D****EVELOPER**** T****OOLS**

O console faz parte de uma série de ferramentas embutidas nos navegadores especificamente
para nós que estamos desenvolvendo um site. Essa série de ferramentas é o que chamamos de

Developer Tools.

Figura 57.1: #

Podemos somar, subtrair, multiplicar e dividir como em qualquer linguagem:

Teste algumas contas digitando diretamente no console:

> 12 + 13

 25
> 14 * 3

 42
> 10 - 4

 6
> 25 / 5

 5
> 23 % 2

 1

Para armazenarmos um valor para uso posterior, podemos criar uma **variável**:

> var resultado = 102 / 17;
undefined

No exemplo acima, guardamos o resultado de  102 / 17  na variável  resultado . O resultado de

criar uma variável é sempre **undefined**. Para obter o valor que guardamos nela ou mudar o seu valor,
podemos fazer o seguinte:

> resultado
6

> resultado = resultado + 10

## 57.4 SINTAXE BÁSICA

**### Operadores**

**### Variáveis**

**268** 
57.4 SINTAXE BÁSICA


--------------------------------------------------

16

> resultado
16

Também podemos alterar o valor de uma variável usando as operações básicas com uma sintaxe bem
compacta:

> var idade = 10; // undefined
> idade += 10; // idade vale 20
> idade -= 5; // idade vale 15
> idade /= 3; // idade vale 5
> idade *= 10; // idade vale 50

Com esse tipo de dados é possível executar todas as operações que vimos anteriormente:

var pi = 3.14159;
var raio = 20;
var perimetro = 2 * pi * raio

Não são apenas números que podemos salvar numa variável. O JavaScript tem vários tipos de dados.
Uma string em JavaScript é utilizada para armazenar trechos de texto:

var empresa = "Caelum";

Para exibirmos o valor da variável empresa fora do console, podemos executar o seguinte comando:

alert(empresa);

O comando  alert  serve para criação de **popups** com algum **conteúdo de texto** que colocarmos

dentro dos parênteses. O que acontece com o seguinte código?

var numero = 30;
alert(numero)

O número 30 é exibido sem problemas dentro do **popup**. O que acontece é que qualquer variável
pode ser usada no  alert . O JavaScript não irá diferenciar o tipo de dados que está armazenado numa

variável, e se necessário, tentará converter o dado para o tipo desejado.

É possível omitir o ponto e vírgula no final de cada declaração. A omissão de ponto e vírgula

funciona no JavaScript devido ao mecanismo chamado *automatic semicolon insertion* (ASI).

**### Number**

**### String**

**### Automatic semicolon insertion (ASI)**

57.4 SINTAXE BÁSICA 
**269**


--------------------------------------------------

Conheça a **Casa do Código**, uma **nova** editora, com autores de destaque no

mercado, foco em **ebooks** (PDF, epub, mobi), preços **imbatíveis** e assuntos
**atuais**.
Com a curadoria da **Caelum** e excelentes autores, é uma abordagem **diferente**

para livros de tecnologia no Brasil.

Casa do Código, Livros de Tecnologia.

O console nos permite testar códigos diretamente no navegador. Porém, não podemos pedir aos

usuários do site que sempre abram o console, copiem um código e colem para ele ser executado.

Para inserirmos um código JavaScript em uma página, é necessário utilizar a tag  <script> :

<script>

 alert("Olá, Mundo!");
</script>

A tag  <script>  pode ser declarada dentro da tag  <head>  assim como na tag  <body> , mas

devemos ficar atentos, porque o código é lido imediatamente dentro do navegador. Veja a consequência
disso nos dois exemplos abaixo:

*<!DOCTYPE html>*
<html>

 <head>
   <meta charset="utf-8">
   <title>Aula de JS</title>
   <script>
      alert("Olá, Mundo!");
   </script>
 </head>
 <body>
   <h1>JavaScript</h1>
   <h2>Linguagem de programação</h2>
 </body>
</html>

Repare que, ao ser executado, o script trava o processamento da página. Imagine um script que
demore um pouco mais para ser executado ou que exija alguma interação do usuário como uma

confirmação. Não seria interessante carregar a página toda primeiro antes de sua execução por uma
questão de performance e experiência para o usuário?

**Seus livros de tecnologia parecem do século passado?**

## 57.5 A TAG SCRIPT

**270** 
57.5 A TAG SCRIPT


--------------------------------------------------

Para fazer isso, basta removermos o script do  <head> , colocando-o no final do  <body> :

*<!DOCTYPE html>*
<html>

 <head>
   <meta charset="utf-8">
   <title>Aula de JS</title>
 </head>
 <body>
   <h1>JavaScript</h1>
   <h2>Linguagem de Programação</h2>
   <script>
     alert("Olá, Mundo!");
   </script>
 </body>
</html>

Devemos sempre colocar o script antes de fecharmos a tag  </body> ? Na maioria esmagadora das

vezes sim.

Se o mesmo script for utilizado em outra página, como fazemos? Imagine ter que reescrever o script
toda vez que ele for necessário. Para não acontecer isso, é possível importar scripts dentro da página
utilizando também a tag  <script> :

<script type="text/javascript" src="js/hello.js"></script>

alert("Olá, Mundo!");

Com a separação do script em arquivo externo é possível reaproveitar alguma funcionalidade em

mais de uma página.

É comum querermos dar uma olhada no valor de alguma varíavel ou resultado de alguma operação
durante a execução do código. Nesses casos, poderíamos usar um *alert*. Porém, se esse conteúdo deveria

somente ser mostrado para o desenvolvedor, o console do navegador pode ser utilizado no lugar do alert
para imprimir essa mensagem:

var mensagem = "Olá mundo";
console.log(mensagem);

## 57.6 JAVASCRIPT EM ARQUIVO EXTERNO

## 57.7 MENSAGENS NO CONSOLE

57.6 JAVASCRIPT EM ARQUIVO EXTERNO 
**271**


--------------------------------------------------

**I****MPRESSÃO**** ****DE**** ****VARIÁVEIS**** ****DIRETAMENTE**** ****DO**** ****CONSOLE**

Quando 
você 
estiver 
com 
o 
console 
aberto, 
não 
é 
necessário 
chamar

 console.log(nomeDaVariavel) : você pode chamar o nome da variável diretamente que ela será

impressa no console.

Se você está gostando dessa apostila, certamente vai aproveitar os **cursos**
**online** que lançamos na plataforma **Alura**. Você estuda a qualquer momento

com a **qualidade** Caelum. Programação, Mobile, Design, Infra, Front-End e
Business, entre outros! Ex-estudante da Caelum tem 10% de desconto, siga o link!

Conheça a Alura Cursos Online.

Para permitir alterações na página, ao carregar o HTML da página, os navegadores carregam em

memória uma estrutura de dados que representa cada uma das nossas tags no JavaScript. Essa estrutura é
chamada de DOM (**D**ocument **O**bject **M**odel). Essa estrutura pode ser acessada através da variável
global  document .

O termo "documento" é frequentemente utilizado em referências à nossa página. No mundo front-
end, documento e página são sinônimos.

Antes de sair alterando nossa página, precisamos em primeiro lugar acessar no JavaScript o
elemento que queremos alterar. Como exemplo, vamos alterar o conteúdo de um título da página. Para
acessar ele:

document.querySelector("h1")

Esse comando usa os **seletores CSS** para encontrar os elementos na página. Usamos um seletor de
nome de tag mas poderíamos ter usado outros:

document.querySelector(".class")

**Agora é a melhor hora de aprender algo novo**

## 57.8 DOM: SUA PÁGINA NO MUNDO JAVASCRIPT

## 57.9 QUERYSELECTOR

**272** 
57.8 DOM: SUA PÁGINA NO MUNDO JAVASCRIPT


--------------------------------------------------

document.querySelector("#id")

Se você vai utilizar várias vezes um mesmo elemento da página, é possível salvar o resultado de
qualquer  querySelector numa variável:

var titulo = document.querySelector("h1")

Executando no console, você vai perceber que o elemento correspondente é selecionado. Podemos

então manipular seu conteúdo. Você pode ver o conteúdo textual dele com:

titulo.textContent

Essa propriedade, inclusive, pode receber valores e ser alterada:

titulo.textContent = "Novo título"

Editoras tradicionais pouco ligam para ebooks e novas tecnologias. Não dominam
tecnicamente o assunto para revisar os livros a fundo. Não têm anos de
experiência em didáticas com cursos.
Conheça a **Casa do Código**, uma editora diferente, com curadoria da **Caelum** e
obsessão por livros de qualidade a preços justos.

Casa do Código, ebook com preço de ebook.

As vezes você precisa selecionar vários elementos na página. Várias tags com a classe  .cartao por

exemplo. Se o retorno esperado é mais de um elemento, usamos  querySelectorAll que devolve uma

lista de elementos (*array*).

document.querySelectorAll(".cartao")

Podemos então acessar elementos nessa lista através da posição dele (começando em zero) e usando
o colchetes:

// primeiro cartão
document.querySelectorAll(".cartao")[0]

## 57.10 ELEMENTO DA PÁGINA COMO VARIÁVEL

**Editora Casa do Código com livros de uma forma diferente**

## 57.11 QUERYSELECTORALL

57.10 ELEMENTO DA PÁGINA COMO VARIÁVEL 
**273**


--------------------------------------------------

Ao alterarmos os elementos da página, o navegador sincroniza as mudanças e alteram a aplicação
em tempo real.

Apesar de ser interessante a possibilidade de alterar o documento todo por meio do JavaScript, é
muito comum que as alterações sejam feitas quando o usuário executa alguma ação, como por exemplo,

mudar o conteúdo de um botão ao clicar nele e não quando a página carrega. Porém, por padrão,
qualquer código colocado no  <script> , como fizemos anteriormente, é executado assim que o

navegador lê ele.

Para guardarmos um código para ser executado em algum outro momento, por exemplo, quando o
usuário clicar num botão, é necessário utilizar alguns recursos do JavaScript no navegador. Primeiro
vamos criar uma **função**:

function mostraAlerta() {

 alert("Funciona!");
}

Ao criarmos uma função, simplesmente guardamos o que estiver dentro da função, e esse código
guardado só será executado quando **chamarmos** a função, como no seguinte exemplo:

function mostraAlerta() {

 alert("Funciona!");
}

// fazendo uma chamada para a função mostraAlerta, que será executada nesse momento
mostraAlerta()

Para chamar a função **mostraAlerta** só precisamos utilizar o nome da função e logo depois abrir e
fechar parênteses.

Agora, para que essa nossa função seja chamada quando o usuário clicar no botão da nossa página,
precisamos do seguinte código:

function mostraAlerta() {

 alert("Funciona!");
}

// obtendo um elemento através de um seletor de ID
var botao = document.querySelector("#botaoEnviar");

botao.onclick = mostraAlerta;

Note que primeiramente foi necessário selecionar o botão e depois definir no  onclick  que o que

vai ser executado é a função  mostraAlerta . Essa receita será sempre a mesma para qualquer código

que tenha que ser executado após alguma ação do usuário em algum elemento. O que mudará sempre é

## 57.12 ALTERAÇÕES NO DOM

## 57.13 FUNÇÕES E OS EVENTOS DO DOM

**274** 
57.12 ALTERAÇÕES NO DOM


--------------------------------------------------

qual elemento você está selecionando, a qual evento você está reagindo e qual função será executada.

Existem diversos eventos que podem ser utilizados em diversos elementos para que a interação do
usuário dispare alguma função:

oninput: quando um elemento input tem seu valor modificado

onclick: quando ocorre um click com o mouse
ondblclick: quando ocorre dois clicks com o mouse

onmousemove: quando mexe o mouse

onmousedown: quando aperta o botão do mouse

onmouseup: quando solta o botão do mouse (útil com os dois acima para gerenciar drag'n'drop)
onkeypress: quando pressionar e soltar uma tecla

onkeydown: quando pressionar uma tecla

onkeyup: quando soltar uma tecla
onblur: quando um elemento perde foco

onfocus: quando um elemento ganha foco

onchange: quando um input, select ou textarea tem seu valor alterado

onload: quando a página é carregada
onunload: quando a página é fechada

onsubmit: disparado antes de submeter o formulário (útil para realizar validações)

Existem também uma série de outros eventos mais avançados que permitem a criação de interações
para drag-and-drop, e até mesmo a criação de eventos customizados.

A **Alura** oferece centenas de **cursos online** em sua plataforma exclusiva de
ensino que favorece o aprendizado com a **qualidade** reconhecida da Caelum.
Você pode escolher um curso nas áreas de Programação, Front-end, Mobile,

Design & UX, Infra, Business, entre outras, com um plano que dá acesso a todos os cursos. Ex-
estudante da Caelum tem 10% de desconto neste link!

Conheça os cursos online Alura.

**### Quais eventos existem**

**Já conhece os cursos online Alura?**

## 57.14 FUNÇÕES ANÔNIMAS

57.14 FUNÇÕES ANÔNIMAS 
**275**


--------------------------------------------------

No exercício anterior nós indicamos que a função mostraTamanho deveria ser executada no
momento em que o usuário inserir o tamanho do produto no  <input type="range"> . Note que não

estamos executando a função mostraTamanho, já que não colocamos os parênteses. Estamos apenas
indicando o nome da função que deve ser executada.

inputTamanho.oninput = mostraTamanho

function mostraTamanho(){

   outputTamanho.value = inputTamanho.value
}

Há algum outro lugar do código no qual precisamos chamar essa função? Não! Porém, é pra isso que

damos um nome à uma função, para que seja possível usá-la em mais de um ponto do código.

É muito comum que algumas funções tenham uma única referência no código. É o nosso caso com a
função  mostraTamanho . Nesses casos, o JavaScript permite que criemos a função no lugar onde antes

estávamos indicando seu nome.

inputTamanho.oninput = function() {

   outputTamanho.value = inputTamanho.value
}

Transformamos a função mostraTamanho em uma função sem nome, uma função anônima. Ela
continua sendo executada normalmente quando o usuário alterar o valor para o tamanho.

Uma variável que armazena um string faz muito mais que isso! Ela permite, por exemplo, consultar

o seu tamanho e realizar transformações em seu valor.

var empresa = "Caelum";

empresa.length; // tamanho da string

empresa.replace("lum","tano"); // retorna Caetano

A partir da variável  empresa , usamos o operador  ponto seguido da ação  replace .

**String é imutável**. Logo, no exemplo abaixo, se a variável  empresa for impressa após a chamada

da função  replace , o valor continuará sendo "Caelum". Para obter uma string modificada, é necessário

receber o retorno de cada função que manipula a string, pois uma nova string modificada é retornada:

var empresa = "Caelum";

// substitui a parte "lum" por "tano"
empresa.replace("lum","tano");
console.log(empresa); // imprime Caelum, não mudou!

## 57.15 MANIPULANDO STRINGS

## 57.16 IMUTABILIDADE

**276** 
57.15 MANIPULANDO STRINGS


--------------------------------------------------

empresa = empresa.replace("lum","tano");
console.log(empresa); // imprime Caetano, mudou!

Querendo aprender ainda mais sobre? Esclarecer dúvidas dos exercícios? Ouvir

explicações detalhadas com um instrutor?

A Caelum oferece o **curso data** presencial nas cidades de São Paulo, Rio de

Janeiro e Brasília, além de turmas incompany.

Consulte as vantagens do curso *Desenvolvimento Web com HTML, CSS e*

*JavaScript*

O JavaScript possui funções de conversão de string para number:

var textoInteiro = "10";
var inteiro = parseInt(textoInteiro);

var textoFloat = "10.22";
var float = parseFloat(textoFloat);

Number, assim como string, também é imutável. O exemplo abaixo altera o número de casas
decimais com a função  toFixed . Esta função retorna uma string, mas, para ela funcionar corretamente,

seu retorno precisa ser capturado:

var milNumber = 1000;
var milString = milNumber.toFixed(2); // recebe o retorno da função
console.log(milString); // imprime a string "1000.00"

É possível concatenar (juntar) tipos diferentes e o JavaScript se encarregará de realizar a conversão
entre os tipos, podendo resultar em algo não esperado.

var s1 = "Caelum";
var s2 = "Inovação";
console.log(s1 + s2); // imprime CaelumInovação

**Você pode também fazer o curso data dessa apostila na Caelum**

## 57.17 CONVERSÕES

## 57.18 MANIPULANDO NÚMEROS

## 57.19 CONCATENAÇÕES

**### String com String**

57.17 CONVERSÕES 
**277**


--------------------------------------------------

Como vimos, o JavaScript tentará ajudar realizando conversões quando tipos diferentes forem
envolvidos numa operação, mas é necessário estarmos atentos na maneira como ele as realiza:

var num1 = 2;
var num2 = 3;
var nome = "Caelum"

// O que ele imprimirá?

// Exemplo 1:
console.log(num1 + nome + num2); // imprime 2Caelum3

// Exemplo 2:
console.log(num1 + num2 + nome); // imprime 5Caelum

// Exemplo 3:
console.log(nome + num1 + num2); // imprime Caelum23

// Exemplo 4:
console.log(nome + (num1 + num2)); // imprime Caelum5

// Exemplo 5:
console.log(nome + num1 * num2); // imprime Caelum6
// A multiplicação tem precedência

**N****A****N**

Veja o código abaixo:

  console.log(10-"curso")

O resultado é  NaN  (not a number). Isto significa que todas operações matemáticas, exceto

subtração, que serão vistas mais a frente, só podem ser feitas com números. O valor  NaN  ainda

possui uma peculiaridade, definida em sua especificação:

var resultado = 10-"curso"; // retorna NaN
resultado == NaN; // false
NaN == NaN; // false

Não é possível comparar uma variável com  NaN , nem mesmo  NaN  com  NaN ! Para saber se

uma variável é  NaN , deve ser usada a função **isNaN**:

var resultado = 10-"curso";
isNaN(resultado); // true

**### String com outro tipo de dados**

**278** 
57.19 CONCATENAÇÕES


--------------------------------------------------

Conheça a **Casa do Código**, uma **nova** editora, com autores de destaque no

mercado, foco em **ebooks** (PDF, epub, mobi), preços **imbatíveis** e assuntos
**atuais**.
Com a curadoria da **Caelum** e excelentes autores, é uma abordagem **diferente**

para livros de tecnologia no Brasil.

Casa do Código, Livros de Tecnologia.

**Seus livros de tecnologia parecem do século passado?**

57.19 CONCATENAÇÕES 
**279**


--------------------------------------------------

CAPÍTULO 58

Primeiro precisamos criar as classes com o padrão visto em aula para indicar quem queremos manipular

com o JavaScript. Queremos manipular o contador de cursos, o total de horas e o botão que vai fazer a
matrícula do usuário nos cursos. Depois precisamos selecionar esses elementos no arquivo JS e guarda-
los em variáveis.

Agora devemos criar a função que vai cuidar da soma dos contadores e também de mostrar essa

soma nos respectivos contadores da tabela. Não esquecendo de chamar essa função toda vez que um
input é selecionado e a soma só pode acontecer quando o input estiver selecionado.

Se você está gostando dessa apostila, certamente vai aproveitar os **cursos**

**online** que lançamos na plataforma **Alura**. Você estuda a qualquer momento
com a **qualidade** Caelum. Programação, Mobile, Design, Infra, Front-End e

Business, entre outros! Ex-estudante da Caelum tem 10% de desconto, siga o link!

Conheça a Alura Cursos Online.

1. Crie o arquivo ** matricula.js **na pasta ** js **com o seguinte código:

+var $tdTotalCursos = document.querySelector('.js-total-de-cursos')
+var $tdTotalDeHoras = document.querySelector('.js-total-de-horas')
+var $buttonConfirmar = document.querySelector('.js-botao-matricula')
+

# EXERCÍCIO: CALCULANDO TOTAL DE
# HORAS E CURSOS COM JAVASCRIPT

## 58.1 OBJETIVO

**Agora é a melhor hora de aprender algo novo**

## 58.2 PASSO A PASSO COM CÓDIGO

**# js/matricula.js**

**280** 
57 EXERCÍCIO: CALCULANDO TOTAL DE HORAS E CURSOS COM JAVASCRIPT


--------------------------------------------------

+var totalHoras = 0
+var totalCursos = 0
+
+
+function adicionaCurso(checkbox){
+  
+  if(checkbox.checked){
+    totalCursos ++
+    totalHoras += parseInt(checkbox.value)
+  }
+  else {
+    totalCursos --
+    totalHoras -= parseInt(checkbox.value)
+  }
+  
+  $tdTotalDeHoras.textContent = totalHoras + 'h'
+  $tdTotalCursos.textContent = totalCursos + ' curso(s)'
+  
+}
+
+$buttonConfirmar.onclick = confirmaMatriculas
+
+function confirmaMatriculas() {
+  if(totalCursos === 0) {
+    alert('Nenhum curso selecionado')
+  } else {
+    alert('Matricula confirmada nos cursos!')
+    window.location.href = 'index.html'
+  }
+}

2. No arquivo ** matricula.html **na pasta ** raíz do projeto **faça as seguintes alterações:

 *<!DOCTYPE html>*
 <html>
 <head>
     <title>Matriculas</title>
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width">
     <link href="css/bootstrap.css" rel="stylesheet">
     <link href="css/matricula.css" rel="stylesheet">
     <link href="img/favicon.ico" rel="icon">
 </head>
 <body>
     <header class="header">
         <nav class="navbar navbar-expand-sm navbar-dark bg-dark">
             <a class="navbar-brand" href="index.html"><img class="header-navbar-logo" src="img/m
usicdot-logo-light.svg" alt="Logo da Musicdot"></a>

             <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#na
vbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Tog
gle navigation">

                 <span class="navbar-toggler-icon"></span>
             </button>
             <div class="collapse navbar-collapse" id="navbarSupportedContent">
                 <ul class="navbar-nav mr-auto">
                     <li class="nav-item active">
                         <a class="nav-link" href="#">Cursos</a>
                     </li>
                     <li class="nav-item">
                         <a class="nav-link" href="#">Matriculas</a>

**# matricula.html**

58.2 PASSO A PASSO COM CÓDIGO 
**281**


--------------------------------------------------

                     </li>
                     <li class="nav-item">
                         <a href="#" class="nav-link">Emails</a>
                     </li>
                 </ul>
             </div>
         </nav>
     </header>
     <main class="container mb-4">
         <div class="jumbotron bg-dark header-matricula text-light mt-3">
             <div class="container">
                 <h1>Escolher cursos</h1>
                 <p class="lead">Escolha os cursos que gostaria de se matricular</p>
             </div>
         </div>
         <table class="table table-hover rounded-top">
             <thead class="thead-dark">
                 <tr>
                     <th scope="col"></th>
                     <th scope="col">Curso</th>
                     <th scope="col">Tempo</th>
                 </tr>
             </thead>
             <tbody>
                 <tr>
-                    <̶t̶d̶>̶<̶i̶n̶p̶u̶t̶ t̶y̶p̶e̶=̶"̶c̶h̶e̶c̶k̶b̶o̶x̶"̶ n̶a̶m̶e̶=̶"̶c̶u̶r̶s̶o̶"̶ v̶a̶l̶u̶e̶=̶"̶2̶0̶"̶>̶</̶t̶d̶>
+                    <td><input onclick="adicionaCurso(this)" type="checkbox" name="curso" value=
"20"></td>

                     <td>Curso de Violão</td>
                     <td>20h</td>
                 </tr>
                 <tr>
-                    <̶t̶d̶>̶<̶i̶n̶p̶u̶t̶ t̶y̶p̶e̶=̶"̶c̶h̶e̶c̶k̶b̶o̶x̶"̶ n̶a̶m̶e̶=̶"̶c̶u̶r̶s̶o̶"̶ v̶a̶l̶u̶e̶=̶"̶3̶0̶"̶>̶</̶t̶d̶>
+                    <td><input onclick="adicionaCurso(this)" type="checkbox" name="curso" value=
"30"></td>

                     <td>Curso de Bambolê</td>
                     <td>30h</td>
                 </tr>
                 <tr>
-                    <̶t̶d̶>̶<̶i̶n̶p̶u̶t̶ t̶y̶p̶e̶=̶"̶c̶h̶e̶c̶k̶b̶o̶x̶"̶ n̶a̶m̶e̶=̶"̶c̶u̶r̶s̶o̶"̶ v̶a̶l̶u̶e̶=̶"̶1̶2̶"̶>̶</̶t̶d̶>
+                    <td><input onclick="adicionaCurso(this)" type="checkbox" name="curso" value=
"12"></td>

                     <td>Curso de Java</td>
                     <td>12h</td>
                 </tr>
                 <tr>
-                    <̶t̶d̶>̶<̶i̶n̶p̶u̶t̶ t̶y̶p̶e̶=̶"̶c̶h̶e̶c̶k̶b̶o̶x̶"̶ n̶a̶m̶e̶=̶"̶c̶u̶r̶s̶o̶"̶ v̶a̶l̶u̶e̶=̶"̶2̶0̶"̶>̶</̶t̶d̶>
+                    <td><input onclick="adicionaCurso(this)" type="checkbox" name="curso" value=
"20"></td>

                     <td>Curso de Violão</td>
                     <td>20h</td>
                 </tr>
                 <tr>
-                    <̶t̶d̶>̶<̶i̶n̶p̶u̶t̶ t̶y̶p̶e̶=̶"̶c̶h̶e̶c̶k̶b̶o̶x̶"̶ n̶a̶m̶e̶=̶"̶c̶u̶r̶s̶o̶"̶ v̶a̶l̶u̶e̶=̶"̶3̶0̶"̶>̶</̶t̶d̶>
+                    <td><input onclick="adicionaCurso(this)" type="checkbox" name="curso" value=
"30"></td>

                     <td>Curso de Bambolê</td>
                     <td>30h</td>
                 </tr>
                 <tr>
-                    <̶t̶d̶>̶<̶i̶n̶p̶u̶t̶ t̶y̶p̶e̶=̶"̶c̶h̶e̶c̶k̶b̶o̶x̶"̶ n̶a̶m̶e̶=̶"̶c̶u̶r̶s̶o̶"̶ v̶a̶l̶u̶e̶=̶"̶1̶2̶"̶>̶</̶t̶d̶>
+                    <td><input onclick="adicionaCurso(this)" type="checkbox" name="curso" value=
"12"></td>

**282** 
58.2 PASSO A PASSO COM CÓDIGO


--------------------------------------------------

                     <td>Curso de Java</td>
                     <td>12h</td>
                 </tr>
                 <tr>
-                    <̶t̶d̶>̶<̶i̶n̶p̶u̶t̶ t̶y̶p̶e̶=̶"̶c̶h̶e̶c̶k̶b̶o̶x̶"̶ n̶a̶m̶e̶=̶"̶c̶u̶r̶s̶o̶"̶ v̶a̶l̶u̶e̶=̶"̶2̶0̶"̶>̶</̶t̶d̶>
+                    <td><input onclick="adicionaCurso(this)" type="checkbox" name="curso" value=
"20"></td>

                     <td>Curso de Violão</td>
                     <td>20h</td>
                 </tr>
                 <tr>
-                    <̶t̶d̶>̶<̶i̶n̶p̶u̶t̶ t̶y̶p̶e̶=̶"̶c̶h̶e̶c̶k̶b̶o̶x̶"̶ n̶a̶m̶e̶=̶"̶c̶u̶r̶s̶o̶"̶ v̶a̶l̶u̶e̶=̶"̶3̶0̶"̶>̶</̶t̶d̶>
+                    <td><input onclick="adicionaCurso(this)" type="checkbox" name="curso" value=
"30"></td>

                     <td>Curso de Bambolê</td>
                     <td>30h</td>
                 </tr>
                 <tr>
-                    <̶t̶d̶>̶<̶i̶n̶p̶u̶t̶ t̶y̶p̶e̶=̶"̶c̶h̶e̶c̶k̶b̶o̶x̶"̶ n̶a̶m̶e̶=̶"̶c̶u̶r̶s̶o̶"̶ v̶a̶l̶u̶e̶=̶"̶1̶2̶"̶>̶</̶t̶d̶>
+                    <td><input onclick="adicionaCurso(this)" type="checkbox" name="curso" value=
"12"></td>

                     <td>Curso de Java</td>
                     <td>12h</td>
                 </tr>
                 <tr>
-                    <̶t̶d̶>̶<̶i̶n̶p̶u̶t̶ t̶y̶p̶e̶=̶"̶c̶h̶e̶c̶k̶b̶o̶x̶"̶ n̶a̶m̶e̶=̶"̶c̶u̶r̶s̶o̶"̶ v̶a̶l̶u̶e̶=̶"̶2̶0̶"̶>̶</̶t̶d̶>
+                    <td><input onclick="adicionaCurso(this)" type="checkbox" name="curso" value=
"20"></td>

                     <td>Curso de Violão</td>
                     <td>20h</td>
                 </tr>
                 <tr>
-                    <̶t̶d̶>̶<̶i̶n̶p̶u̶t̶ t̶y̶p̶e̶=̶"̶c̶h̶e̶c̶k̶b̶o̶x̶"̶ n̶a̶m̶e̶=̶"̶c̶u̶r̶s̶o̶"̶ v̶a̶l̶u̶e̶=̶"̶3̶0̶"̶>̶</̶t̶d̶>
+                    <td><input onclick="adicionaCurso(this)" type="checkbox" name="curso" value=
"30"></td>

                     <td>Curso de Bambolê</td>
                     <td>30h</td>
                 </tr>
                 <tr>
-                    <̶t̶d̶>̶<̶i̶n̶p̶u̶t̶ t̶y̶p̶e̶=̶"̶c̶h̶e̶c̶k̶b̶o̶x̶"̶ n̶a̶m̶e̶=̶"̶c̶u̶r̶s̶o̶"̶ v̶a̶l̶u̶e̶=̶"̶1̶2̶"̶>̶</̶t̶d̶>
+                    <td><input onclick="adicionaCurso(this)" type="checkbox" name="curso" value=
"12"></td>

                     <td>Curso de Java</td>
                     <td>12h</td>
                 </tr>
                 <tr class="bg-dark text-light">
                     <td>Total</td>
                     <td class="js-total-de-cursos">0 curso(s)</td>
                     <td class="js-total-de-horas">0h</td>
                 </tr>
             </tbody>
         </table>
-        <̶b̶u̶t̶t̶o̶n̶ t̶y̶p̶e̶=̶"̶b̶u̶t̶t̶o̶n̶"̶ c̶l̶a̶s̶s̶=̶"̶b̶t̶n̶ b̶t̶n̶-̶o̶u̶t̶l̶i̶n̶e̶-̶d̶a̶r̶k̶ b̶t̶n̶-̶l̶g̶ m̶b̶-̶4̶"̶>̶C̶o̶n̶f̶i̶r̶m̶a̶r̶ M̶a̶t̶r̶í̶c̶u̶l̶a̶</̶b̶u̶t̶t̶o
̶n̶>

+        <button type="button" class="js-botao-matricula btn btn-outline-dark btn-lg mb-4">Confir
mar Matrícula</button>

     </main>
     <script src="js/jquery.js"></script>
     <script src="js/bootstrap.js"></script>
+    <script src="js/matricula.js"></script>
 </body>
 </html>

58.2 PASSO A PASSO COM CÓDIGO 
**283**


--------------------------------------------------

CAPÍTULO 59

.elemento {

   font-size: * px, em, rem, pt, %*; /* Controla o tamanho da fonte */
   font-weight: *0 à 1000. Depende da fonte*; /* Controla o peso da fonte */
   font-style: *normal, italic, oblique*;
   font-family: *serif, sans-serif, monospace, custom*; /* Controla a família da fonte */
}

Editoras tradicionais pouco ligam para ebooks e novas tecnologias. Não dominam
tecnicamente o assunto para revisar os livros a fundo. Não têm anos de
experiência em didáticas com cursos.
Conheça a **Casa do Código**, uma editora diferente, com curadoria da **Caelum** e
obsessão por livros de qualidade a preços justos.

Casa do Código, ebook com preço de ebook.

.elemento {

   text-align: *left, center, right, justify; /* Controla o alinhamento do texto */
   text-transform: *capitalize, uppercase, lowercase, none*; /* Controla a capitalização do texto */
   text-indent: *px, em, rem, %*; /* Controla o tamanho da indentação que é colocado antes de uma li
nha de texto em um bloco */
}

.elemento {

   letter-spacing: *px, rem, em, %, pt*; /* Controla o espaçamento entre uma letra e outra de um blo
co de texto */
}

# PROPRIEDADES CSS

## 59.1 PROPRIEDADE FONT

**Editora Casa do Código com livros de uma forma diferente**

## 59.2 PROPRIEDADE TEXT

## 59.3 PROPRIEDADE LETTER-SPACING

**284** 
58 PROPRIEDADES CSS


--------------------------------------------------

.elemento {

   line-height: *pt, px, rem, em, sem unidade de medida*; /* Controla a altura das linhas de um conj
unto de texto */
}

A **Alura** oferece centenas de **cursos online** em sua plataforma exclusiva de

ensino que favorece o aprendizado com a **qualidade** reconhecida da Caelum.
Você pode escolher um curso nas áreas de Programação, Front-end, Mobile,
Design & UX, Infra, Business, entre outras, com um plano que dá acesso a todos os cursos. Ex-

estudante da Caelum tem 10% de desconto neste link!

Conheça os cursos online Alura.

.elemento {

   color: #ff00ff; /* Hexadecimal #RRGGBB */
   color: #f0f; /* Hexadecimal shorthand #RGB */
   color: rgb(255, 0, 255); /* Valor RGB de 0 a 255 rgb(R, G, B)*/
   color: #ff00ff00; /* Hexadecimal com opacidade (alpha) #RRGGBBAA */
   color: rgba(255, 0, 255, 0.0); /* Valor RGB com opacidade */
}

.elemento {

   background-color: *hexadecimal, nome, rgb, rgba*; /* Controla a cor de fundo */
   background-image: *url()*; /* Coloca uma imagem como plano de fundo */
   background-size: *x y, x/y, cover, contain, %, px, rem, em *; /* Controla o tamanho do plano de f
undo. Dois valores podem ser colocados, x e y ou apenas o valor de x que ele será adicionad/removido 
proporcionalmente em y */

   background-repeat: *repeat, no-repeat*; /* Controla se a imagem de fundo vai sofrer repetição*/
   background-position: *top right bottom left, top 10px, bottom 2rem right 2%*; /* Controla a posiç
ão do plano de fundo */
}

.elemento {

   border: *espessura* *estilo* *cor*; /* Coloca uma borda em todo elemento */
   border-top: *espessura* *estilo* *cor*; /* Coloca uma borda acima do elemento */
   border-right: *espessura* *estilo* *cor*; /* Coloca uma borda à direita do elemento */
   border-bottom: *espessura* *estilo* *cor*; /* Coloca uma borda abaixo do elemento */

## 59.4 PROPRIEDADE LINE-HEIGHT

**Já conhece os cursos online Alura?**

## 59.5 PROPRIEDADES DE COR

## 59.6 PROPRIEDADE BACKGROUND

## 59.7 PROPRIEDADE BORDER

59.4 PROPRIEDADE LINE-HEIGHT 
**285**


--------------------------------------------------

   border-left: *espessura* *estilo* *cor*; /* Coloca uma borda à esquerda do elemento */
}

Querendo aprender ainda mais sobre? Esclarecer dúvidas dos exercícios? Ouvir

explicações detalhadas com um instrutor?

A Caelum oferece o **curso data** presencial nas cidades de São Paulo, Rio de

Janeiro e Brasília, além de turmas incompany.

Consulte as vantagens do curso *Desenvolvimento Web com HTML, CSS e*

*JavaScript*

.elemento {

   vertical-align: *baseline, top, middle, bottom*; /* Alinha verticalmente elementos que são inline
ou inline-block */
}

.elemento {

   width: *px, rem, em, %*; /* Controla a largura do elemento */
   min-width: *px, rem, em, %*; /* Controla a largura mínima que um elemento pode ter */
   max-width: *px, rem, em, %*; /* Controla a largura máxima que um elemento pode ter */

   height: *px, rem, em, %*; /* Controla a altura do elemento */
   min-height: *px, rem, em, %*; /* Controla a altura mínima que um elemento pode ter */
   max-height: *px, rem, em, %*; /* Controla a altura máxima que um elemento pode ter */
}

.elemento {

   box-sizing: *border-box, content-box*; /* Define qual caixa do box-model será usada como referênc
ia para colocar propriedades de tamanho */
}

**Você pode também fazer o curso data dessa apostila na Caelum**

## 59.8 PROPRIEDADE VERTICAL-ALIGN

## 59.9 PROPRIEDADES WIDTH E HEIGHT

## 59.10 PROPRIEDADE BOX-SIZING

**286** 
59.8 PROPRIEDADE VERTICAL-ALIGN


--------------------------------------------------

Conheça a **Casa do Código**, uma **nova** editora, com autores de destaque no

mercado, foco em **ebooks** (PDF, epub, mobi), preços **imbatíveis** e assuntos
**atuais**.
Com a curadoria da **Caelum** e excelentes autores, é uma abordagem **diferente**

para livros de tecnologia no Brasil.

Casa do Código, Livros de Tecnologia.

.elemento {

   overflow: *visible, hidden, scroll, auto*; /* Controla o comportamento dos elementos internos que
"vazam"  do espaço definido pela tag mãe */
   overflow-x: *visible, hidden, scroll, auto*; /* Controla o comportamento dos elementos internos q
ue "vazam"  do espaço horizontal definido pela tag mãe */

   overflow-y: *visible, hidden, scroll, auto*; /* Controla o comportamento dos elementos internos q
ue "vazam"  do espaço vertial definido pela tag mãe */
}

**Seus livros de tecnologia parecem do século passado?**

## 59.11 PROPRIEDADE OVERFLOW

59.11 PROPRIEDADE OVERFLOW 
**287**

