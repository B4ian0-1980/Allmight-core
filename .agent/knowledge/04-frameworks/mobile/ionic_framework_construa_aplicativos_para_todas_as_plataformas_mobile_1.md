---json
{
  "id": "ionic_framework_construa_aplicativos_para_todas_as_plataformas_mobile_1",
  "title": "Ionic Framework Construa aplicativos para todas as plataformas mobile",
  "categoria": "04-frameworks",
  "subcategoria": "mobile",
  "resumo": "**Arquivo Original:** `Ionic Framework Construa aplicativos para todas as plataformas mobile.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "aplicativos",
    "construa",
    "framework",
    "frameworks",
    "ionic",
    "mobile",
    "para",
    "plataformas"
  ],
  "perguntas_tipo": [
    "Como utilizar Ionic Framework Construa aplicativos para todas as plataformas mobile?",
    "Quais as boas praticas de mobile?"
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
  "dono": "stack-mobile",
  "prioridade": 2
}
---

# Ionic Framework Construa aplicativos para todas as plataformas mobile

> **Arquivo Original:** `Ionic Framework Construa aplicativos para todas as plataformas mobile.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 1

	


## Página 2

Table	of	Contents	
ISBN	
Agradecimentos	
O	autor	
Prefácio	
1.	Introdução	
1.1	Instalações	
1.2	Conclusão	
2.	Iniciando	nossa	aplicação	
2.1	Command	Line	Interface	e	seus	comandos	básicos	
2.2	Criando	os	artefatos	
2.3	Testando	a	aplicação	
2.4	Estrutura	de	pastas	
2.5	Adicionando	a	plataforma	Android	
2.6	Compilando	e	instalando	o	aplicativo	
2.7	Metendo	a	mão	na	massa	
2.8	Conclusão	
2.9	Para	saber	mais	
3.	Conhecendo	os	nossos	arquivos	
3.1	Um	pouco	de	MVC	
3.2	Separando	o	joio	do	trigo	
3.3	O	cardápio	e	o	MVC	
3.4	Conclusão	

## Página 3

3.5	Para	saber	mais	
4.	Completando	o	menu	
4.1	Estados	
4.2	Conclusão	
4.3	Para	saber	mais	
5.	Detalhando	os	itens	
5.1	O	protótipo	
5.2	Camada	de	serviços	
5.3	Criando	os	arquivos	
5.4	Ordem	na	casa	
5.5	Criando	a	tela	genérica	
5.6	Passando	um	parâmetro	
5.7	Recuperando	o	parâmetro	
5.8	Criando	o	serviço	de	detalhamento	
5.9	Detalhando	o	item	
5.10	Conclusão	
5.11	Para	saber	mais	
6.	Fazendo	pedidos	
6.1	Os	requisitos	do	aplicativo	
6.2	Uma	forma	de	guardar	nossa	sessão	
6.3	Hora	de	injetar	o	value	
6.4	Guardando	os	pedidos	
6.5	Conclusão	
6.6	Para	saber	mais	
7.	A	bandeja	

## Página 4

7.1	Elementos	do	modal	
7.2	Vamos	ter	retrabalho	
7.3	Editar	os	itens	da	bandeja	
7.4	A	função	de	confirmar	edição	
7.5	Exclusão	de	itens	
7.6	Confirmando	os	pedidos	
7.7	Conclusão	
7.8	Para	saber	mais	
8.	A	conta	
8.1	Construção	do	template	
8.2	Vamos	dividir	a	conta	
8.3	Pagar	ou	pedir?	
8.4	Conclusão	
8.5	Para	saber	mais	
9.	Usando	a	câmera	
9.1	Instalação	do	plugin	
9.2	Construção	de	artefatos	
9.3	A	câmera	
9.4	Conclusão	
9.5	Para	saber	mais	
10.	Recursos	
10.1	O	Firebase	
10.2	Consumindo	serviços	
10.3	O	cardápio	modificado	
10.4	ionicList	

## Página 5

10.5	O	ionicActionSheet	
10.6	Dialog	do	ngCordova	
10.7	Conclusão	
10.8	Para	saber	mais	

## Página 6

Sumário	
	
ISBN		
Agradecimentos		
O	autor		
Prefácio		
1.	Introdução		
2.	Iniciando	nossa	aplicação		
3.	Conhecendo	os	nossos	arquivos		
4.	Completando	o	menu		
5.	Detalhando	os	itens		
6.	Fazendo	pedidos		
7.	A	bandeja		
8.	A	conta		
9.	Usando	a	câmera		
10.	Recursos		
 

## Página 7

ISBN	
Impresso	e	PDF:	978‐85‐5519‐288‐3	
EPUB:	978‐85‐5519‐289‐0	
MOBI:	978‐85‐5519‐290‐6	
Você	pode	discutir	sobre	este	livro	no	Fórum	da	Casa	do	Código:	
http://forum.casadocodigo.com.br/.	
Caso	você	deseje	submeter	alguma	errata	ou	sugestão,	acesse:	
http://erratas.casadocodigo.com.br.	
 

## Página 8

Agradecimentos	
A 	r e a l i z a ç ã o 	d e s t e 	p r o j e t o 	t o r n o u ‐ s e 	p o s s í v e l 	e 	r e a l 	c o m 	o 	a p o io	 e	 confiança	 de	 algumas	
pessoas.	Faço	questão	de	deixar	aqui	o	meu	agradecimento	a	elas.	
Em	primeiro	lugar,	quero	agradecer	ao	Adriano	Almeida	pela	oportunidade	e	confiança	na	
minha	obra.	À	Vivian	Matsui	que	foi	fundamental	para	aprender	e	continuar	aprendendo	os	
macetes	de	uma	boa	escrita.	
Agradeço	 à	 minha	 família	 pela	 paciência	 e	 compreensão	 incondicional,	 principalmente	 à	
minha	 filha	 Letícia	 por	 ter	 "cedido"	 o	 tempo	 em	 que	 poderíamos	estarmos	 juntos,	 como	
também	seu	colo	para	descanso	e	relaxamento	em	momentos	de	estresse.		
Este	 parágrafo	 não	 é	 um	 simples	 agradecimento,	 mas	 um	 intenso	 a gradecimento	 e	
dedicação	à	memória	de	meus	pais,	principalmente	minha	mãe,	fal ecida	no	mesmo	ano	de	
publicação,	por	ter	deixado	o	legado	de	uma	boa	educação	e	ter	 me	apoiado	e	incentivado	a	
estudar	TI	para	seguir	a	profissão	onde	me	sinto	realizado	e	feliz.	
 

## Página 9

O	autor	
	
Figura	‐1.1:	Adrian	Gois	
	
Em	 1995	 recebi	 de	 presente	 de	minha	 querida	 e	 saudosa	 mãe	 meu	 primeiro	 computador	
com	 o	 SO	 Windows	 95:	 um	ITAUTEC	e q u i p a d o 	c o m 	u m 	p r o c e s sa d o r 	Pentium	q u e 	f e z 	m e	
apaixonar	à	primeira	vista	pela	tecnologia.	A	partir	daí,	comec ei	a	ingressar	no	mundo	da	
internet	desde	já,	pesquisando	como	programar	aquela	máquina.		
Fiz	assim	meus	primeiros	programas	na	linguagem	 Clipper	e,	logo	em	seguida,	comecei	a	
estudar	 HTML	e 	JavaScript .	 Depois	 disto,	 nunca	 mais	 deixei	 de	 lado	 o	 fascínio	 por	
computadores.	 Assim	 me	 tornei	 bacharel	 em	 Ciência	 da	 Computação 	p e l a 	
UNIFACS/Salvador‐BA,	 fundei	 a	 empresa	 ABG	 TI	 SOLUTIONS	
(http://www.abgsolucoes.com.br),	 onde	 obtive	 experiência	 em	 Desenvolvimento	 de	
Sistemas	 em	 grandes	 empresas	 multinacionais,	 passando	 por	 lingu agens	 como	 Java,	
JavaScript,	C,	C++,	Delphi,	entre	outras	que	permeiam	o	mundo	do	desenvolvimento.	
Hoje	 lidero	 uma	 equipe	 de	 TI	 em	 uma	 fábrica	 de	 software	 com	 arquiteturas	 diversas,	
passando	 por	 .NET	 até	 Microsoft	 SharePoint,	 com	 contratos	 em	 empresas	 de	 grande	 e	
médio	 porte.	 Desenvolvo	 projetos	 de	 aplicativos	 híbridos,	 utilizando	 a	 tecnologia	 deste	
livro.	
 


## Página 10

Prefácio	
Já	 parou	 para	 imaginar,	 enquanto	 você	 lê	 esta	 pequena	 frase,	 quantos	smartphones	e s t ã o 	
sendo	 utilizados	 no	 mundo?	 Pois	 bem!	 Segundo	 a	TeleGeography,	 em	 2015	 tínhamos	 7,1	
b i l h õ e s 	d e 	c h i p s 	a t i v o s 	n o 	m u n d o , 	o u 	s e j a , 	q u a s e 	a 	q u a n t i d a d e 	de	 habitantes	 do	 globo	
terrestre.	 Com	 isso,	 podemos	 inferir	 sobre	 o	 grande	 potencial	 d e	 mercado	 que	 é	 o	 de	
smartphones	e	telefonia.		
Com	 a	 invenção	 dos	 smartphones,	 surgiram	 tanto	 grandes	 como	 descartáveis	 ideias	 de	
aplicativos.	 No	 início,	 tudo	 era	 muito	 restrito	 ao	 desenvolvimento	 destas	 ideias	 em	 uma	
plataforma	e,	a	partir	de	seu	sucesso	ou	não,	a	migração	do	cód igo	para	outras	plataformas,	
principalmente	na	dupla	iOS	versus	Android.	
Por	 conta	 disto,	 surgiram	 os	 frameworks	 para	 compilação	 híbrida	 de	 aplicativos	 sendo	
desenvolvidos	em	uma	única	linguagem.	Hoje,	sabe‐se	que	isso	é	 possível	com	a	mesclagem	
de	HTML,	JavaScript	e	CSS,	basicamente.	
Dentro	 destes	 frameworks, 	o 	f o c o 	d e s t a 	o b r a 	é 	Ionic	 framework. 	N e l e 	é 	p o s s í v e l 	u t i l i z a r 	
componentes	 responsivos	 e	 atrativos	 para	 o	 desenvolvimento	 dos	 a p l i c a t i v o s , 	c o m 	a 	
p o s s i b i l i d a d e 	d e 	c o m p i l a ç ã o 	e 	f á c i l 	i n s t a l a ç ã o 	n a s 	m a i s 	d i v e r s as	 plataformas	 –	 seja	
Windows	Phone,	Android,	iOS,	BlackBerry	etc.	
O	livro	é	dividido	em	10	capítulos,	nos	quais	inicialmente	é	ex planado	sobre	a	instalação	e	
preparação	 do	 ambiente	 de	 desenvolvimento	 e,	 em	 seguida,	 um	 cap ítulo	 dedicado	 a	
explicar	os	comandos	básicos	do	framework.	Posteriormente,	vamos	evoluindo	na	criação	e	
entendimento	dos	artefatos	do	ap licativo	e,	a	cada	novo	capítul o,	temos	novas	inserções	de	
componentes.		
Ao	final,	dedico	dois	capítulos	a	recursos	extras,	como	utiliza ção	da	câmera	do	dispositivo,	
consumo	de	serviços	do	firebase	do	Google,	entre	outros	recursos	avançados.		
Esta	leitura	levará	você	em	uma	viagem	ao	mundo	do	desenvolvime nto	de	aplicativos,	sem	
s e 	p r e o c u p a r 	c o m 	a 	p l a t a f o r m a 	n a t i v a 	à 	q u a l 	e l e 	s e r á 	d e s t i n a d o ,	 tornando	 as	 coisas	 mais	
fáceis	para	manutenção	e	evolução.	
Público‐alvo	
E s t e 	l i v r o 	é 	d i r e c i o n a d o 	a o s 	d e s e n v o l v e d o r e s 	q u e 	j á 	t e n h a m , 	p e lo	 menos,	 uma	 base	 em	
JavaScript,	HTML5	e	CSS.	No	decorrer	do	livro,	mesmo	o	leitor	não	tendo	experiência	com	as	
tecnologias	que	permeiam	o	 Ionic,	como	AngularJS	e	Cordova/Phonegap,	pretendo	fazê‐lo	
alcançar	um	nível	de	conhecimento	básico	sobre	todas	elas.		
É	aconselhável	também	uma	base	de	conhecimento	em	lógica	de	pro gramação,	para	que	se	
evolua	 no	 desenvolvimento	 de	 um	 Caso	 de	 uso	q u e 	u t i l i z a r e m o s 	c o m o 	e x e m p l o 	p a r a 	o s 	

## Página 11

c a p í t u l o s . 	S e n d o 	a s s i m , 	s e 	j á 	p r o g r a m o u 	n e s s a 	t r í a d e 	( H T M L , 	J S 	e	 CSS)	 e	 quer	 iniciar	 no	
mundo	de	aplicativos	com	o	Ionic	Framework,	não	se	preocupe,	você	está	no	lugar	certo.	
Código‐fonte	
Durante	a	leitura	deste	livro,	desenvolveremos	um	aplicativo	denominado	Cardápio	Móvel	
e	seu	código	fonte	pode	ser	clonado	através	do	link:	
https://github.com/adriangois/codigo‐livro‐ionicframework.	
 

## Página 12

CAPÍTULO	1	
Introdução	
Com	o	nascimento	dos	dispositivos	inteligentes,	surgiu	uma	grande	quantidade	de	Sistemas	
Operacionais.	 Com	 isso,	 surgia	 também	 a	 dificuldade	 em	 padroniz a r 	u m a 	l i n h a 	d e 	
desenvolvimento	de	aplicações	que	fossem	portáveis	ou	multiplataforma.		
O	Java	ME,	lançado	em	1999,	foi	a	plataforma	criada	da	subdivisão	do	Java	2	(Java	1.2).	Com	
o	objetivo	de	integrar	dispositivos	limitados	em	termo	de	 hardware,	 veio	 como	 promessa	
da	já	citada	padronização,	visto	que	todos	os	aplicativos	rodar iam	em	uma	Máquina	Virtual	
(VM	–	Virtual	Machine),	 não	 importando	 em	 qual	 sistema/dispositivo	 estaria	 hospedado.	
Tudo	isso	provido	pela	portabilidade	da	tão	crescente	tecnologia	Java.	
Com	 o	 passar	 do	 tempo,	 em	 junho	 de	 2007,	 a	 Apple	 Inc	 viria	 a	 anunciar	 o	 primeiro	
SmartPhone	 com	 seu	 iOS	 como	 Sistema	 Operacional	 Móvel.	 Consequentemente,	o	 grupo	
Google	criou	o	Sistema	Operacional	Android	para	dispositivos,	baseado	no	núcleo	do	Linux.	
Além	destes,	outros	nasceram	no	mesmo	contexto,	como	por	exemplo,	Windows	Phone	e	o	
Blackberry.		
Com	 essa	 variedade	 de	 Sistemas	 Operacionais	 em	 uso	 no	 mundo,	 o	 leitor	 deve	 estar	
imaginando	 a	 dificuldade	 de	 agilizar	 o	 processo	 de	 desenvolvimento	 e	 compilação	 dos	
aplicativos,	 a	 fim	 de	 torná‐los	 portáveis	 para	 as	 distintas	 pla taformas,	 sem	 que	 fosse	
necessário	reprogramar	na	linguagem	de	programação	nativa	de	cada	dispositivo.		
Uma	luz	no	fim	do	túnel	veio	com	o	surgimento	do	HTML5,	em	que	se	criou	uma	segunda	
camada,	 que	 seria	 o	 intermediário	 entre	 a	 linguagem	 do	 sistema	 n a t i v o 	( i O S , 	A n d r o i d , 	
Windows	Phone,	BlackBerry	etc.)	e	a	aplicação,	construída	basic amente	em	HTML5,	CSS3	e	
JavaScript.	Esta	camada	seria	responsável	pela	compilação	final 	do	aplicativo,	provendo	à	
camada	view	(JavaScripts,	CSS	e	HTML)	os	recursos	da	plataforma	nativa	(di spositivo	para	
o	qual	estará	sendo	compilado).		
Surgiu	também	o	PhoneGap	com	o	propósito	de	facilitar	a	vida	de 	muitos	desenvolvedores,	
disponibilizando	 acesso	 aos	 diversos	 hardwares	 (câmeras,	 GPS,	 acelerômetros)	 nos	
variados	dispositivos	móveis.	Ou	seja,	tudo	o	que	estaria	dispo nível	somente	via	linguagem	
nativa	agora	é	possível	acessar	por	meio	de	chamadas	na	linguagem	JavaScript.		
A	imagem	a	seguir	ilustra	como	funciona,	na	prática,	o	PhoneGap .	Nele,	a	entrada	é	de	um	
conjunto	de	artefatos	na	tríade	já	citada	(HTML,	CSS	e	JavaScri pt),	passando	por	um	 build	
que	gera	no	final	o	aplicativo	na	plataforma	escolhida.	

## Página 13

	
Figura	1.1:	Processo	de	build	do	PhoneGap	
A p e s a r 	d e 	o 	P h o n e G a p 	n ã o 	s e r 	o 	p r i n c i p a l 	f o c o 	d o 	l i v r o , 	à 	m e d i da	 que	 formos	
implementando	 nosso	 caso	 de	 uso	 (um	 aplicativo	 de	 Cardápio	 Móvel	 que	 explicaremos	
mais	à	frente),	nos	familiarizaremos	com	ele	utilizando	alguns	de	seus	plugins.	
Dentro	de	todo	este	contexto	e	aprimorando	mais	o	processo	de	desenvolvimento,	em	2013	
nasceu	o	 Ionic	Framework,	mesclando	outros	frameworks	já	existentes,	como	o	PhoneGap	
citado	 anteriormente	 e	 AngularJS.	 O	 Ionic	 é	 um	 open	 source	 SDK	q u e 	u s a 	u m 	c o n c e i t o 	
chamado	 native‐feeling	 mobile	 apps,	 o	 que	 quer	 dizer	 desenvolvimento	 de	 aplicativos	
móveis	com	tecnologias	web	como,	HTML,	CSS	e	JavaScript.		
O	foco	do	framework	é	o	front	view	dos	aplicativos,	ou	seja,	ele	fornece	componentes	para	o	
desenvolvimento	da	interface	dos 	aplicativos,	não	sendo	um	substituto	do	PhoneGap	(que	
f o c a 	n o 	a c e s s o 	a o s 	r e c u r s o s ) , 	p o r 	e x e m p l o . 	N a 	p r á t i c a , 	o 	Ionic	n o s 	f o r n e c e 	u m a 	g a m a 	d e 	
componentes	para	serem	utilizados	na	 view,	fazendo	o	controle	através	do	 AngularJS	e,	por	
fim,	é	compilado	através	do	PhoneGap .	Esta	é	a	junção	de	vários	frameworks	para	um	fim	
específico.	
N o 	p r o g r e s s o 	d e 	n o s s a 	l e i t u r a , 	v a m o s 	v e r 	q u e , 	p a r a 	e s t e n d e r 	a 	capacidade	 do	 aplicativo,	
usaremos	o	Cordova/Phonegap,	que	possibilita	o	acesso	aos	recur sos	do	hardware,	através	
da	 instalação	 de	plugins.	 Com	 isto,	 nos	 preocupamos	 em	 construir,	 planejar	 e	 executar	 as	
tarefas	 por	 camadas,	 separando	views,	 controllers	e 	models . 	I s t o 	é 	p o s s í v e l 	p o r 	c a u s a 	d a 	
integração	do	Ionic	com	o	AngularJS.	
Veremos	através	dos	capítulos	a	construção	de	uma	aplicação	de	 exemplo,	a	que	daremos	o	
nome	 de	 Cardápio	 Móvel,	 em	 que	 o	 leitor	 participará	 do	 planejamento	 (através	 de	


## Página 14

protótipos),	 construção,	 teste	 e	 implantação.	 Veremos	 também	 o	aplicativo	 consumindo	
serviços,	através	de	simulações	de	 webservices	e,	no	final,	não	mais	uma	simulação,	mas	o	
c o n s u m o 	d e 	u m 	s e r v i ç o 	n a 	n u v e m 	a t r a v é s 	d o 	firebase	 que	 será	 explicado	 no	 capítulo	
Recursos.	
A	 aplicação	 será	 baseada	 na	 seguinte	 situação:	 construiremos	 um 	 aplicativo	 que	 nos	
f o r n e ç a 	u m a 	l i s t a 	d e 	p r o d u t o s , 	c o m 	d e s c r i ç ã o , 	f o t o 	e 	p r e ç o 	d e l e . 	E s t a 	a p l i c a ç ã o 	s e r i a 	u m a 	
forma	de	o	proprietário	de	um	restaurante	disponibilizar,	através	de	um	serviço	hospedado	
na	nuvem,	os	produtos	para	os	seus	cardápios.		
Além	 disto,	 o	 aplicativo	 deve	 permitir	 que	 os	 usuários	 façam	 pedidos,	 colocando‐os	 na	
b a n d e j a , 	s i m i l a r 	a 	u m 	carrinho	 de	 compras	m u i t o 	u t i l i z a d o 	n o s 	e‐commerces.	 Ao	
confirmar	 a	 bandeja,	 o	 pedido	 será	 enviado	 para	 o	 setor	 respons á v e l 	q u e 	a t e n d e r á 	o 	
consumidor.	O	usuário	também	terá	a	possibilidade	de	pagar	a	co nta	parcial	ou	total,	e/ou	
pedi‐la	que	seja	encerrada	e	entregue	na	mesa.	
Nas	 interfaces	 da	 aplicação,	 serão	 apresentados	 alguns	 componentes	 CSS	 do	 framework,	
bem	como	sua	extensão	AngujarJS,	que	fornece	uma	rica	bibliotec a	de	JavaScript	para	que	
toda	a	mágica	funcione.	
A	 cada	 nova	 funcionalidade,	 apresentaremos	 um	 protótipo	 do	 que	se	 deseja	 alcançar	 ao	
f i n a l 	d a 	c o n s t r u ç ã o . 	I s t o 	f a c i l i t a r á 	a 	c o m p r e e n s ã o 	d a 	l e i t u r a 	do	 capítulo,	 e	 se	 consagrará	
q u a n d o 	p u s e r m o s 	e m 	p r á t i c a 	o 	c o n h e c i m e n t o 	a d q u i r i d o , 	c h e g a n d o 	assim	 ao	 produto	
planejado.	
O	H TM L 5	c h ego u 	e,	ao 	q u e	p arec e ,	c h ego u 	p ara	f ic ar 	c o m o 	grande 	padronizador,	sendo	a	
linguagem	de	interfaces.	Assim,	ele	deixa	os	recursos	mais	complexos	e	que	estejam	fora	do	
c o n t e x t o 	d e 	U I 	( I n t e r f a c e 	d e 	U s u á r i o ) , 	p a r a 	o u t r a s 	t e c n o l o g i a s 	e	 padrões.	 Vamos	 explorar	
e s t e 	r e c u r s o 	a o 	m á x i m o 	e 	n o s 	f a m i l i a r i z a r , 	p o i s , 	p o r 	s e r 	o 	f u t uro	 (alguns	 já	 o	 consideram	
presente),	vamos	nos	preparar	agora.	
Através	 dessa	 sopa	 de	 frameworks	 ( Ionic,	 AngularJS	 e	 Phonegap/Cordova)	 é	 possível	
construir	um	aplicativo	portável	e	funcional,	não	se	preocupand o	com	a	sua	linguagem	de	
programação	nativa,	mas	sim	em	desenvolver	o	visual	e	a	lógica	 numa	linguagem	simples	e	
universal	na	linguagem	da	web,	o	HTML.	
P a r a 	e n t e n d e r 	m e l h o r 	c o m o 	s u r g i u 	a 	i d e i a 	d e 	s e 	m e s c l a r 	t u d o 	e m 	um	 framework,	 criar	
aplicações	 rápidas	 e	 ter	 a	 facilidade	 de	 compilar	 para	 as	 variadas	 plataformas	 existentes,	
utilizando	HTML5,	JavaScript	e	CSS3,	basicamente,	vamos	meter	a	mão	na	massa	e	instalar	
as	ferramentas	necessárias	para	iniciarmos	nossa	aplicação	de	exemplo.	
Nos	 concentraremos	 em	 uma	 instal a ç ã o 	a m b i e n t e 	W i n d o w s 	+ 	A n d r o i d.	 Isso	 não	
impede	que	o	leitor	possa	trabalhar	em	outro	ambiente	e	gerar	a 	aplicações	para	iOS,	
Windows	Phone	ou	qualquer	outro	 de	sua	preferência,	visto	que	e ste	é	exatamente	o	
propósito	do	Ionic	Framework.	

## Página 15

1.1	Instalações	
	
Para	 iniciarmos	 o	 desenvolvimento	 de	 nossa	 aplicação	 de	 exemplo,	 devemos	 dispor	 das	
seguintes	ferramentas:	
 Ionic	Framework	CLI	(até	a	edição	deste	livro,	a	versão	mais	no va	era	a	1.3	ou	
Beta	2,	mas	vamos	trabalhar	com	o	1.3);	
 Java	Development	Kit	‐	JDK	(7	ou	superior);	
 Android	SDK;	
 NodeJS	(até	a	edição	deste	livro,	a	versão	mais	nova	era	a	4.4.4);	
 Sublime	Text	(até	a	edição	deste	livro,	a	versão	mais	nova	era	a	3).	
	
Vamos	lá?!		
	
1. Comece	 baixando	 a	 JDK	 no	 site	 da	 Oracle,	 em	
http://www.oracle.com/technetwork/java/javase/downloads/jdk8‐downloads‐
2133151.html. 	R e c o m e n d a m o s 	q u e 	b a i x e 	a 	v e r s ã o 	m a i s 	n o v a . 	A t é 	a 	e d i ç ã o 	d e s t e	
livro	era	a	8u102.	
2. T u d o 	p r o n t o 	p a r a 	o 	A n d r o i d 	S D K ? 	F a ç a 	o 	d o w n l o a d 	e 	i n s t a l e 	e m 	
https://developer.android.com/studio/index.html.	
3. Agora	 vamos	 ao	 NodeJS,	 em	 https://nodejs.org/en/download/.	 Instale	 e	 vamos	
partir	para	nossas	dependências.	
4. Depois	de	instalado	o 	NodeJS,	abra	a	linha	de	comando	do	Window s,	do	Linux	ou	
d o 	M a c 	O S , 	e 	i n s t a l e 	o 	C o r d o v a 	e 	o 	I o n i c , 	c o m 	o 	s e g u i n t e 	c o m a n do:	 npm install -g 
cordova ionic.	
	 	

## Página 16

1.2	Conclusão	
Se	 tudo	 ocorreu	 bem,	 já	 estamos	 preparados	 para	 criarmos	 nossa	primeira	 aplicação.	 No	
próximo	 capítulo,	 aprenderemos	 mais	 sobre	 a	 linha	 de	 comando	 do 	 Ionic	e , 	
consequentemente,	 sobre	 o	 comando	 para	 gerar	 uma	 aplicação	 que	servirá	 de	 base	 em	
todo	o	nosso	livro.	Vamos	à	diversão!	
	
Para	saber	mais	
	
1. Sobre	as	instalações	do	JDK	e	Android	SDK,	acesse	
http://www.oracle.com/technetwork/pt/java/javase/downloads/index.html.	E	
para	o	Developer	Android	em	https://developer.android.com.	
2. Você	 encontra	 um	 guia	 completo	 para	 instalação	 destas	 dependênc ias	 em	
http://cordova.apache.org/docs/en/5.1.1/guide/platforms/android/index.html.	
3. AngularJS	–	https://angularjs.org.	
4. Phonegap	–	http://phonegap.com.	
5. Ionic	Framework	–	http://ionicframework.com.	
 

## Página 17

CAPÍTULO	2	
Iniciando	nossa	aplicação	
Para	fins	didáticos,	vamos	conhecer	os	principais	componentes	d o	framework	e	aplicá‐los	
n a 	p r á t i c a . 	P o r t a n t o , 	p e n s a r e m o s 	e m 	u m 	c a s o 	d e 	u s o 	q u e 	v a m o s 	c onstruir	 e	 evoluir	 ao	
longo	 dos	 capítulos.	 Ao	 final	 deste	 livro,	 teremos	 um	 aplicativ o	 que	 nos	 fornecerá	 um	
cardápio	de	um	determinado	estabelecimento,	com	os	seguintes	requisitos:	
1. Permitirá	 a	 listagem	 e	 o	 detalhamento	 de	 cada	 produto	 existente,	 assim	 como	
fazer	o	pedido	determinando	sua	quantidade.	
2. Fazer	 pedidos	 através	 desta	 lista g e m 	e 	p e r m i t i r 	c o n f i r m a r 	o u 	e d i t a r 	o 	p e d i d o ; 	
tudo	isto	similar	a	um	carrinho	de	compras	de	um	e‐commerce.	
3. Pagar	e/ou	pedir	a	conta	de	forma	parcial	ou	total.	
Neste	capítulo,	conheceremos	os	comandos	básicos	do	CLI	( Command	Line	Interface),	que	é	
a	linha	de	comando	do	framework. 	Começaremos	executando	o	coman do	responsável	pela	
criação	de	toda	a	estrutura	do	nosso	caso	de	uso.		
Posteriormente,	 executaremos	 a	 aplicação	 no	 browser	p a r a 	o s 	t e s t e s 	e , 	e m 	s e g u i d a , 	
adicionaremos	uma	plataforma	(em	nosso	caso	Android),	fazendo	o 	build	e	deploy 	em	um	
dispositivo	móvel	real.	
O	 protótipo	 inicial	 deste	 aplicativo	 está	 ilustrado	 na	 figura	 a 	s e g u i r , 	n a 	q u a l 	s e 	d e s e j a 	
construir	toda	estrutura	e	navegação	através	do	menu	lateral.	
	
Figura	2.1:	Protótipo	deste	capítulo	–	Construção	da	estrutura	do	Cardápio	Móvel	
	
Preparado	para	uma	viagem	sem	volta?	Vamos	à	prática	do	framework.	

## Página 18

2.1	Command	Line	Interface	e	seus	comandos	básicos	
O	 Ionic	CLI	é 	a 	f e r r a m e n t a 	d o 	f r a m e w o r k 	q u e 	p e r m i t e 	e x e c u t a r 	u m a 	b o a 	q u a n tidade	 de	
comandos.	Vamos	nos	concentrar	em	alguns	deles,	nos	que	usaremos	com	mais	frequência.	
Ao	decorrer	do	livro,	aprenderemos	mais	sobre	estes	comandos.	
O	Ionic	facilita	o	processo	de	criação	inicial	do	desenvolvimen to,	passando	pelos	testes	em	
browser,	 sem	 a	 necessidade	 de	 instalar	 o	 aplicativo	 em	 um	 dispositivo.	 Isso	 exceto	 em	
casos	extremos,	como	a	utilização	de	APIs	para	os	recursos	da	plataforma	em	questão.		
Para	a	construção	dos	códigos,	usaremos	o	editor	de	texto	 Sublime	Text	3,	mas	nada	impede	
que	o	leitor	utilize	qualquer	outra	ferramenta	de	edição	de	sua	preferência.	Existe	um	leque	
de	 opções	 de	 editores	 que	 deixarei	 como	 dica	 na	 seção	Links	 úteis	‐ 	Editores,	 no	 final	
deste	capítulo.	Espero	que	o	leitor	se	sinta	à	vontade	para	esc olher	o	que	mais	lhe	satisfaz.	
E s s a 	é 	u m a 	d a s 	v a n t a g e n s 	d o 	d e s e n v o l v i m e n t o 	h í b r i d o , 	e m 	q u e 	o 	desenvolvedor	 não	 fica	
atrelado	a	uma	IDE	de	cada	linguagem	nativa.	
Com	o	Ionic	instalado,	abriremos	a	linha	de	comando	e	digitarem os	ionic.	Isto	nos	dará	uma	
lista	de	comandos	que	o	framework	suporta,	como	mostra	a	seguinte	figura:	
	
Figura	2.2:	Alguns	comandos	do	CLI	
O b s e r v e 	q u e 	a 	f i g u r a 	n ã o 	i l u s t r a 	t o d o s 	o s 	c o m a n d o s , 	m a s 	a p e n a s 	o s 	q u e 	a c h a m o s 	
relevantes	 para	 iniciarmos	 os	 tr abalhos.	 Mas	 não	 se	 preocupe,	 a o	 longo	 do	 livro,	
quando	necessário,	utilizaremos	outros	comandos,	explicando	detalhadamente.	


## Página 19

O	 framework	 contém	 alguns	templates	j á 	p r o n t o s , 	e m 	q u e 	é 	g e r a d o 	t o d o 	a r t e f a t o 	a p e n a s 	
com	 um	 comando.	 Se,	 por	 exemplo,	 você	 desejar	 construir	 um	 apli cativo	 com	 tabs	d e 	
navegação,	poderia	gerá‐lo	com	o	seguinte	comando:	ionic start [nome_de_sua_aplicação] tabs.		
V e j a 	a 	s e g u i r 	t r ê s 	t e m p l a t e s 	b á s i c o s 	q u e 	p o d e m 	s e r 	ú t e i s 	e m 	m u itas	 aplicações,	 como	
também	podem	ser	customizados	pelo	desenvolvedor.	
	
Figura	2.3:	3	templates	prontos	que	são	gerados	pelo	framework	com	o	comando	ionic	start	
	
Os	comandos	para	geração	desses	templates	são,	respectivamente:	
	
1. ionic start [nome_aplicação] blank:	um	template	sem	menu,	sem	rodapé	ou	cabeçalho;	
2. ionic start [nome_aplicação] tabs:	um	template	com	rodapé	e	cabeçalho	com	um	título;	
3. ionic start [nome_aplicação] sidemenu:	um	template	com	um	menu	lateral	e	cabeçalho	com	
um	título.	
Simples,	não	é?!	
2.2	Criando	os	artefatos	
E m 	n o s s o 	c a s o , 	p a r a 	c r i a r m o s 	o s 	a r t e f a t o s 	d a 	a p l i c a ç ã o 	d e 	e x e m p l o 	d e s t e 	l i v r o , 	v a m o s 	
executar	 o	 comando	ionic start cardapio-movel sidemenu.	E s t e 	c o m a n d o 	c r i a 	u m a 	p a s t a 	c h a m a d a 	
cardapio-movel	no	diretório	que	você	estiver	executando.		
O	 sidemenu	n o 	c o m a n d o 	f a r á 	o 	f r a m e w o r k 	c o n s t r u i r 	u m 	a p l i c a t i v o 	c o m 	u m 	m e nu	 lateral,	
conforme	 ilustrado	 no	 protótipo.	 Após	 a	 execução	 deste	 comando,	n a v e g u e 	s o b r e 	a 	p a s t a 	
criada	para	ir	se	familiarizando	com	os	artefatos	criados.	


## Página 20

2.3	Testando	a	aplicação	
Prontinho!	Agora	que	foram	gerados	os	artefatos,	na	mesma	pasta	execute	o	comando	 ionic 
serve. 	C o m 	e l e , 	s u a 	a p l i c a ç ã o 	j á 	e s t a r á 	s e n d o 	e x e c u t a d a 	e m 	s e u 	n a v e gador	 padrão,	 no	
endereço	http://localhost:8100/.		
Teste	e	navegue	sobre	o	menu.	Brinque	um	pouco	e	conheça	sua	nova	aplicação.		
Caso	queira	executar	em	um	navegador	específico,	que	não	seja	o	padrão,	o	comando	é:	 ionic 
serve --w [nome_do_navegador].	 Por	 exemplo,	 no	 Google	 Chrome,	 você	 pode	 utilizar	 ionic serve --w 
chrome. 	S u g i r o 	q u e 	u s e 	e s t e 	browser	e 	a b r a ‐ o 	e m 	m o d o 	d e s e n v o l v e d o r 	(Ctrl + Shift + i),	 em	
seguida	utilize	o	Toggle device mode,	simulando	um	dispositivo,	clicando	no	ícone	a	seguir:	
	
Figura	2.4:	Estrutura	de	pastas	
Com	isto,	você	será	capaz	de	ter	uma	visualização	bem	próxima	de	como	o	aplicativo	ficará	
quando	for	instalado	no	dispositivo	móvel.	
Muito	bem!	Você	já	está	com	a	estrutura	da	sua	aplicação	montad a	e	testada.	Agora	vamos	
conhecer	um	pouco	do	que	foi	gerado	por	trás	deste	comando	tão	poderoso.	
2.4	Estrutura	de	pastas	
A	estrutura	de	suas	pastas	deve	ter	sido	gerada	como	ilustra	a	seguinte	figura:	


## Página 21

	
Figura	2.5:	Estrutura	de	pastas	
	
Por	 enquanto,	 vamos	 nos	 concentra r 	e m 	d o i s 	a r q u i v o s 	p r i n c i p a i s 	que	 estão	 no	 diretório	
raiz:	 package.json e config xml .	 O	 package.json	é 	o 	a r q u i v o 	npm	( https://npmjs.org),	 onde	 são	
configuradas	 as	 dependências	 do	 seu	 projeto,	 suas	 versões,	 entr e	 outras	 informações	
referentes	a	elas.	
O	 config.xml	 diz	 respeito	 às	 configurações	 do	 aplicativo,	 bem	 como	 orientação	 de	 tela	
(horizontal,	 vertical	 ou	 ambas),	 nome	 do	 aplicativo,	 resources,	 versão	 e	 permissões.	 Este	
arquivo	 é	 a	 base	 para	 o	 AndroidManifest xml, 	n o 	c a s o 	d e 	o 	b u i l d 	s e r 	f e i t o 	e m 	A n d r o i d , 	p o r 	
exemplo.	
N ã o 	v a m o s 	m e x e r 	n e s s e s 	a r q u i v o s 	p o r 	e n q u a n t o . 	M a s 	é 	d e 	s u m a 	i m portância	 o	
conhecimento	da	existência	deles ,	assim	como	também	é	importante	entender	a	estrutura	
das	pastas	geradas:	
	
1. www:	contém	os	templates	em	HTML,	arquivos	JavaScript,	CSS	e	imagens,	ou	seja,	
praticamente	onde	você	vai	trabalhar.	
2. plugins:	 contém	 os	 plugins	 que	 foram	 gerados	 e	 serão	 configurados	 ao	 longo	 do	
desenvolvimento.	


## Página 22

3. scss:	 uma	 sintaxe	 para	 o	 CSS,	 para	 quem	 quer	 implementar	 nessa	 estr utura.	
Vamos	trabalhar	apenas	com	CSS.	
4. hooks:	não	nos	aprofundaremos	no	entendimento	deste	diretório,	pois	 não	vamos	
usá‐lo.	Basta	apenas	saber	que	ele	é	gerado	para	customizações	de	comandos	do	
Cordova.	
Com	 nossa	 estrutura	 montada	 e	 apl icação	 rodando,	 vamos	 adiciona r 	a o 	p r o j e t o 	u m a 	
plataforma.	 Como	 havia	 dito	 no	 início	 deste	 livro,	 o	 nosso	build	s e r á 	p a r a 	a 	p l a t a f o r m a 	
Android,	 portanto,	 a	 partir	 de	 agora,	 todos	 os	 comandos	 serão	 executados	 em	 ambiente	
Windows	e	a	geração	do	aplicativo	será	baseada	no	Android.		
Isto	não	impede	que	o	leitor	opte	por	outra	plataforma,	caso	sinta‐se	à	vontade.	Faça	à	sua	
maneira.	
2.5	Adicionando	a	plataforma	Android	
Depois	de	construída	a	aplicação,	é	preciso	adicionar	a	platafo rma	que	se	deseja	compilar.	
Como	executaremos	o	aplicativo	n a	plataforma	Android,	vamos	apr ender	a	gerar	um	 .apk,	e	
em	seguida	fazer	um	deploy	em	algum	dispositivo	desta	plataforma.		
Para	isto,	devemos	rodar	o	seguinte	comando:	ionic platform add android.		
Rode	e	observe	o	que	acontece.	A	seguir,	explicaremos	com	mais	detalhes.	
Nova	estrutura	de	pastas	
Se	tudo	correr	bem,	sua	estrutura	ganhou	uma	nova	pasta	 (platforms/android).	Caso	você	tenha	
executado	 o	 comando	ionic platform add ios, 	d a 	m e s m a 	f o r m a 	o 	f r a m e w o r k 	c r i a r á 	a 	p l a t a f o r m a 	
iOS	(platforms/ios).	
	
Figura	2.6:	Pasta	adicionada	para	a	plataforma	Android	


## Página 23

	
À	medida	que	formos	avançando,	teremos	mais	conhecimentos	sobre 	esta	estrutura	e	seus	
respectivos	arquivos.	Explicaremos	cada	um	deles	de	forma	clara	e	técnica.	
2.6	Compilando	e	instalando	o	aplicativo	
Agora	 que	 criamos	 e	 adicionamos	 uma	 plataforma	 ao	 aplicativo,	 vamos	 testá‐lo	 em	 uma	
plataforma	 móvel.	 O	 Ionic,	 como	 já	 foi	 citado	 neste	 livro,	 é	 totalmente	 compatível	 com	 o	
Phonegap/Cordova.	 No	 processo	 de	 compilar	 para	 nossa	 plataforma 	A n d r o i d , 	o 	
Phonegap/Cordova	 gera	 toda	 a	 estrutura	 de	 classes	 em	 Java,	 configurações	
(AndroidManifest xml),	ícones,	e	todos	os	recursos	necessários	para	que	nossa	aplic ação	execute	
como	esperado.	
Por	padrão,	os	dispositivos	com	Android	não	estão	habilitados	p ara	executar	um	ambiente	
de	desenvolvimento.	Entretanto,	não	há	motivo	para	se	preocupar ,	pois	esta	é	uma	tarefa	
muito	fácil	e	vamos	lhe	instruir	em	relação	a	isto.		
Executaremos	em	um	celular	Motorola	G3,	com	a	versão	do	Android 	6.0,	mas	isto	não	
impede	 de	ser	 instalado	 e	 executado	 em	 outro	 dispositivo.	 Esta	informação	 é	 apenas	
para	fins	didáticos,	já	que	seguiremos	alguns	comandos	para	preparação	do	ambiente	
no	 dispositivo.	 O	 Android	 segue	 sempre	 este	 padrão	 de	 desbloque io	 de	 ambiente	
desenvolvedor.	
Para	isto,	é	necessário	seguir	os	passos:	
	
1. Abra	a	configuração	do	sistema	em	Configurar;	
2. Vá	até	o	último	item	Sobre o telefone	e	clique;	
3. Desça	 até	 Número da versão	e 	c l i q u e 	3 	v e z e s , 	a t é 	a p a r e c e r 	a 	s e g u i n t e 	m e n s a g e m : 	
Faltam	 4	 etapas	 para	 você	 se	 tornar	 um	 desenvolvedor.	 Continue	 clicando	 até	
aparecer:	Agora	você	é	um	desenvolvedor.	
Pronto!	 Agora	 você	 já	 deve	 visualizar	 a	 opção	 Configurar > Programador	 no	 seu	 dispositivo.	
Conecte	 um	 cabo	 USB	 no	 computador	 e	 em	 seu	 dispositivo,	 e	 vamos	 configurar	 algumas	
opções	de	desenvolvimento.	
	
	

## Página 24

1. Se	a	opção	Programador	estiver	como	Desativado,	passe	para	Ativado;	
2. Selecione	Permanecer ativa	para	que	a	sua	tela	não	blo queie	enquanto	estiver	com	o	
cabo	USB	plugado;	
3. Mais	 abaixo,	 encontre	 a	 opção	 Depuração USB	e 	d e i x e 	h a b i l i t a d a . 	S e 	a p a r e c e r 	a 	
mensagem	pedindo	permissão	de	depuração,	clique	em	OK.	
A	seguir,	uma	ilustração	desta	configuração:	
	
Figura	2.7:	Configuração	de	desenvolvedor	
	
Agora	 a	 festa	 vai	 começar.	 Você	 só	 precisa	 executar	 um	 comando	p a r a 	q u e 	s e u 	a p l i c a t i v o 	
seja	compilado	e	instalado.	Abra	a	linha	de	comando	e	execute	ionic run.		
Durante	 a	 execução	 deste	 comando,	 pode	 aparecer	 uma	 confirmação	d e 	d e p u r a ç ã o 	
USB	 com	 a	 seguinte	 mensagem:	A	impressão	digital	da	chave	RSA	deste	computador	é:	
[aqui	a	chave	RSA].	Selecione	a	opção	Sempre permitir a partir deste computador	e	clique	em	OK.	
Se	 tudo	 correr	 bem,	 você	 terá	 ao	 final	 o	 aplicativo	 rodando	 em	 seu	 dispositivo	 como	
ilustrado	na	figura	a	seguir.	Teste,	brinque	e	avalie.	
	


## Página 25

	
Figura	2.8:	Layout	inicial	no	dispositivo	
	
	
Vamos	deixá‐lo	parecido	com	nosso	protótipo?	
2.7	Metendo	a	mão	na	massa	
Agora	 vamos	 conhecer	 um	 pouco	 nosso	 arquivo	app.js	q u e 	f i c a 	e m 	/cardapio-movel/www/js.	 Ele	 é	
responsável	pela	criação,	registro	e	recuperação	de	módulos	do	AngularJS.		
Não	 se	 preocupe	 em	 entender	 a	 fundo	 todos	 os	 conceitos	 deste	 arquivo	 neste	 momento,	
pois,	 à	 medida	 que	 formos	 avançando	 em	 nosso	 caso	 de	 uso,	 aprofundaremos	 cada	 vez	
mais.	O	que	o	leitor	deve	entender	neste	momento	é	que	neste	ar quivo	estarão	as	rotas	de	
nossa	aplicação,	configurações	para	estas	rotas	e	inicialização	da	aplicação.	
Como	nosso	intuito	é	"enxugar"	este	layout	inicial,	criado	pelo	próprio	framework,	para	que	
fique	bem	próximo	ao	nosso	protótipo,	vamos	direto	ao	ponto.		


## Página 26

Toda	aplicação	tem	um	ponto	de	partida,	ou	seja,	no	 start	o	app	será	direcionado	para	onde	
o	 desenvolvedor	 configurou	 como	tela	 de	 início.	 No	 nosso	 caso,	e s t á 	s e n d o 	u m a 	l i s t a 	d e 	
músicas,	a	/templates/playlists.html.		
Isto	 foi	 gerado	 na	 configuração	 do	 módulo	 do	 Ionic,	 chamado	 $urlRouterProvider	q u e 	f a z 	a 	
chamada	à	função	otherwise([rota]),	direcionando	para	esta	interface	como	padrão.	Veja	a	seguir	
a	linha	que	vamos	modificar:	
    $urlRouterProvider.otherwise('/app/playlists'); 
Esta	linha	está	simplesmente	informando	ao	framework	que	sua	pá gina	inicial	é	a	/app/playlist.	
O	leitor	pode	estranhar	a	forma	de	referenciar	a	página	aqui.	N a	verdade,	o	 $urlRouterProvider	
não	referencia	a	página	diretamente,	mas	sim	um	$stateProvider	pré‐configurado.		
Preste	atenção	no	trecho	do	código	a	seguir,	que	se	encontra	no 	app.js.	Observe	que	existem	
dois	 estados	 ( state)	 configurando	 url,	 menu,	 template	e 	 controller.	 O	 nome	 destes	 estados	 são	
app.browse	e	app.playlist,	que	foram	passados	como	primeiro	parâmetro	em	sua	configuração.	
$stateProvider 
... 
.state('app.browse',  
{ 
    url: '/browse', 
        views: { 
            'menuContent': { 
                templateUrl: 'templates/browse.html' 
            } 
        } 
}) 
.state('app.playlists',  
{ 
    url: '/playlists', 
        views: { 
            'menuContent': { 
                templateUrl: 'templates/playlists.html', 
                controller: 'PlaylistsCtrl' 
            } 
        } 
}) 
... 
Agora	ficou	fácil,	não	é?!	Vamos	modificar	no	 $urlRouterProvider	para	que	inicie	nossa	aplicação,	
chamando	o	estado	app.browse	em	vez	de	app.playlists.	Para	isto,	deixe	a	linha	do	$urlRouterProvider	da	
seguinte	forma:	
    $urlRouterProvider.otherwise('/app/browse'); 

## Página 27

Observe	 que	 o	 nome	 do	 estado	 é	 app.browse,	 mas	 a	 forma	 de	 passar	 esse	 parâmetro	 ao	
$urlRouterProvider.otherwise	é 	e m 	f o r m a t o 	URL.	 Portanto,	 substituímos	 o	 .	 (ponto)	 por	 uma	 /	
(barra).	A	partir	de	agora,	assimile	esta	regrinha	básica	para	 chamadas	dos	estados.	Vamos	
precisar	dela	no	decorrer	do	desenvolvimento.	
	
Figura	2.9:	Direcionando	para	página	inicial	browse	
	
Quase	tudo	parecido	com	nosso	protótipo,	conforme	imagem	anterior.	Agora	vamos	apenas	
a j u s t a r 	o s 	t e x t o s 	p a r a 	q u e 	t u d o 	f i q u e 	c o n f o r m e 	p l a n e j a m o s . 	A f i nal,	 você	 não	 quer	
desapontar	o	pessoal	de	design	que	lhe	ofereceu	o	protótipo	da	tela,	não	é	mesmo?!	
Primeiro,	 construiremos	 dois	 estilos	 no	 nosso	 arquivo	 CSS	 que	 s e	 encontra	 em	
/www/css/style.css, 	c o m 	a 	f i n a l i d a d e 	d e 	c e n t r a l i z a r 	o s 	t e x t o s 	q u e 	c o n s t i t u e m 	a 	p rimeira	 tela.	
Abra	este	arquivo	e	vamos	editá‐lo	da	seguinte	forma:	
.txt-centralizado{ 
    text-align: center; 
}.txt-espaco{ 
    margin: 70px 0 70px 0 !important; 
} 
Agora	 é	 o	 momento	 de	 modificar	 o	 arquivo	/www/templates/browse.html,	 alterando	 o	 título	 para	
Cardápio Móvel	 e	 inserindo	 nossos	 dois	 labels	 (Bem-vindo ao Cardápio Móvel	e 	 Acesse as funcionalidades pelo 
menu lateral).	


## Página 28

O 	t í t u l o 	d e s t e 	e s t a d o 	d e v e 	s e r 	a l t e r a d o 	d i r e t a m e n t e 	n a 	t a g 	d o 	framework	 ion-view.	 Depois	
removeremos	 a	 tag	<h1>Browse</h1>	 e	 substituímos	 por	 duas	 com	 as	 classes	 do	 arquivo	 de	
estilo	que	construímos	anteriormente.	Nosso	código	no	arquivo	ficará	assim:	
 <ion-view view-title="Cardápio Móvel"> 
  <ion-content> 
    <h2 class="txt-centralizado txt-espaco">Bem-vindo ao Cardápio Móvel</h2> 
    <h4 class="txt-centralizado">Acesse as funcionalidades pelo menu lateral</h4> 
  </ion-content> 
</ion-view> 
Q u a s e 	t u d o 	p r o n t o ! 	S ó 	p r e c i s a m o s 	c e n t r a l i z a r 	o 	t í t u l o . 	P a r a 	i s to,	 deveremos	 alterar	 uma	
configuração	do	framework	através	de	uma	função	chamada	da	API	 $ionicConfigProvider.	Após	o	
carregamento	da	aplicação,	o	framework	passa	pelo	ciclo	de	conf igurações	por	esta	função:	
angular module('starter', ['ionic', 'starter.controllers']).config(function($stateProvider, $urlRouterProvider)).	
Injetaremos	a	nossa	API	nesta	função	e	informaremos	a	posição	d o	título.	Feito	isto,	nosso	
código	ficará	como	a	seguir:	
... 
.config(function($stateProvider, $urlRouterProvider,$ionicConfigProvider) { 
  $ionicConfigProvider navBar.alignTitle('center'); 
... 
S u g i r o 	q u e 	v á 	s e 	f a m i l i a r i z a n d o 	c o m 	o 	t e r m o 	injetar, 	p o i s 	s e r á 	b a s t a n t e 	u s a d o 	n o 	
decorrer	 do	 livro,	 já	 que	 é	 a	 base	 da	 utilização	 dos	 módulos	 do	A n g u l a r J S 	e m 	n o s s o 	
framework.	Injetar	refere‐se	à	injeção	de	dependências	feita	pelo	framework	por	m eio	
da	 passagem	 de	 parâmetro,	 como	 está	 sendo	 feito	 com	 o	$ionicConfigProvider	n o 	c ó d i g o 	
anterior.	
2.8	Conclusão	
Neste	 capítulo,	 aprendemos	 alguns	 comandos	 básicos	 do	 framework	q u e 	s ã o 	e s s e n c i a i s 	
para	a	construção	de	uma	aplicação	básica,	bem	como	adição	de	p lataformas,	compilação	e	
empacotamento	 para	 posterior	 instalação	 em	 seus	 respectivos	 dispositivos.	 Aprendemos	
t a m b é m 	a 	c o n f i g u r a r 	a l g u n s 	m ó d u l o s 	e , 	c o m 	i s t o , 	d i r e c i o n a r 	a 	a plicação	 para	 um	
estado/template	 inicial	 e	 posicionar	 o	 título	 dos	 templates	 atr a v é s 	d a 	A P I 	d o 	m ó d u l o 	
$ionicConfigProvider.	

## Página 29

No	próximo	capítulo,	aprenderemos	mais	sobre	os	arquivos	gerado s,	principalmente	sobre	
os	 controllers	 no	 arquivo	 www/js/controllers.js.	 Organizaremos	 estes	 controllers	 para	 que	 a	
aplicação	fique	mais	modularizada	e,	consequentemente,	facilite	eventuais	manutenções.	
2.9	Para	saber	mais	
	
1. API	$ionicConfigProvider	–	
http://ionicframework.com/docs/api/provider/$ionicConfigProvider/.	
2. AngularUI	Router	–	https://github.com/angular‐ui/ui‐router.	
	
	
Links	úteis	–	Editores	
	
1. Sublime	Text	–	https://www.sublimetext.com	
2. Atom	–	https://atom.io	
3. Brackets	–	http://brackets.io	
4. Visual	Code	Studio	–	https://code.visualstudio.com	
 

## Página 30

CAPÍTULO	3	
Conhecendo	os	nossos	arquivos	
E s t e 	c a p í t u l o 	v a i 	d e s c r e v e r 	u m 	p o u c o 	s o b r e 	o s 	a r q u i v o s 	q u e 	s e r ão	 utilizados	 para	 a	
implementação	das	funcionalidades	do	nosso	aplicativo.	
Teremos	 um	 conhecimento	 mais	 abrangente	 do	 que	 são	 controllers	e 	s u a s 	
responsabilidades	 no	 front‐view	d a 	a p l i c a ç ã o , 	a s 	r o t a s 	c r i a d a s 	p a r a 	a 	t r a n s i ç ã o 	e n t r e 	a s 	
telas	do	aplicativo,	a	separação	dos	artefatos	em	pastas	organi zadas	e	instalações	de	novos	
plugins.	
A o 	f i n a l , 	o 	l e i t o r 	e s t a r á 	m a i s 	a p t o 	p a r a 	a d i c i o n a r 	a s 	f u n c i o n a lidades	 do	 aplicativo,	
consumindo	 retornos	 de	 serviços	 (em	 nosso	 caso,	 será	 um	 JSON	 simulando	 serviços)	 e	
executando	tarefas	como	transições	entre	telas,	preenchimento	d e	campos	e	validações	de	
formulários,	bem	como	alguns 	componentes	próprios	do	 framework	para	serem	aplicados	
na	marcação	HTML.	
3.1	Um	pouco	de	MVC	
Uma	aplicação	 web	é	constituída	basicamente	de	alguma	linguagem	de	programação,	 seja	
no	 back‐end	o u 	front‐end,	 e	 uma	 representação	 desses	 dados.	 A	 representação,	 em	 seu	
estado	 final,	 sempre	 será	 um	 HTML	 padrão,	 interpretado	 por	 todo s	 os	 browsers	 do	
mercado.	
Com	 o	 surgimento	 dessas	 aplicações	 (World	Wide	Web)	 e	 a	 necessidade	 de	 se	 separar	 o	
código	do	negócio	(Java,	.Net,	PHP,	JavaScript)	da	representaçã o	visual	(HTML),	surgiu	um	
padrão	 de	 arquitetura	 de	 software	 que	 separa	 a	 aplicação	 em	 3	 camadas	 (Model,	 View	e 	
Controller),	o	qual	foi	abreviado	para	MVC.		
O	 AngularJS	 é	 um	 framework	 que	 segue	 este	 conceito	 ( Model‐View‐Controllers,	 em	
português	 Modelo‐Visão‐Controles).	 Com	 ele,	 é	 possível	 manipular	 a	 DOM	 do	 HTML5	 por	
meio	dos	 controllers,	utilizando	um	evento	denominado	 Data	Binding.	Este	é	exatamente	a	
forma	de	atualizar	a	Visão	(View)	toda	vez	que	o	modelo	(Model) 	é	alterado,	e	vice‐versa.	
Esta	interação	é	feita	através	do	controller	de	cada	aplicação.		
		

## Página 31

Em	resumo,	o	papel	de	cada	camada	em	nosso	framework	será	descrito	a	seguir:	
	
1. View	ou	Visão:	o	HTML,	ou	seja,	cada	tela	do	aplicativo	que	será	escrita	nes ta	
linguagem;	
2. Controller	 ou	 Controle:	 JavaScripts	 responsáveis	 por	 receber	 solicitações,	
através	de	funções,	e	delegar	estas	chamadas	a	um	serviço	remot o	ou	executar	
alguma	regra	ou	ação,	como	por	exemplo,	uma	inserção	no	banco	d e	dados	local	
(SQLite);		
3. Model	ou	Modelo:	responsável	por	fazer	a	ponte	entre	o	HTML	e	o	 controller,	
executando	 o	 Data	 binding,	 ou	 seja,	 a	 atualização	 constante	 entre	 estas	 duas	
camadas.	O	modelo	em	AngularJS	é	um	objeto	cuja	referência	é	o	$scope.		
Não	se	preocupe,	pois,	na	prática,	vamos	explanar	melhor	esta	arquitetura	através	de	nosso	
caso	de	uso,	onde	estes	conceitos	(MVC)	serão	aplicados.		
A	figura	a	seguir	ilustra	bem	o	que	é	o	Data	Binding	do	AngularJS:	
	
Figura	3.1:	Data	Binding	do	AngularJS	


## Página 32

	
Vemos	que	a	 view	é	a	camada	logo	abaixo	do	 template	(em	nosso	caso,	um	arquivo	HTML).	
N a 	v e r d a d e , 	d e v e ‐ s e 	e n t e n d e r 	q u e 	a 	view	é 	d e 	f a t o 	o 	n o s s o 	a r q u i v o 	H T M L , 	q u e 	s o f r e 	
a t u a l i z a ç õ e s 	c o n t í n u a s 	d o 	M o d e l o , 	f a z e n d o 	t a m b é m 	o 	c a m i n h o 	c o n trário,	 atualizando	 o	
modelo	da	aplicação	através	de	formulários,	inputs,	ações	de	bo tões	e	tudo	mais	que	seja	
capaz	de	enviar	através	do	HTML.		
A 	s e g u i r , 	v e j a 	u m 	e x e m p l o 	d e 	m a r c a ç ã o 	H T M L 	c o m 	A n g u l a r J S , 	e m 	q ue	 se	 percebe	 um	
modelo	 chamado	yourName. 	E s t e 	r e c e b e 	n o 	c o n t r o l l e r 	u m 	v a l o r 	e 	a t u a l i z a 	a u t o m a t i c a m e n t e	
na	view	em	<h1> Hello {{yourName}} </h1>:	
	
Figura	3.2:	AngularJS	
	
Na	figura	a	seguir,	o	leitor	tem	uma	visão	do	conceito	de	MVC	a plicado	ao	AngujarJS,	onde	
as	 views	( H T M L , 	C S S ) 	i n t e r a g e m 	c o m 	o s 	u s u á r i o s 	e 	s e 	r e s p o n s a b i l i z a m 	p o r	a t u a l i z a r 	o 	
modelo	 ou	 o	 controller,	 através	 de	 chamadas	JavaScript.	 Observe	 o	 AngularJS	 fazendo	 o	
meio	 dos	 caminhos	 entre	 o	 modelo	 e	 a	 view.	 Além	 disto,	 percebe‐se	 também	 que	 a	
responsabilidade	de	uma	chamada	externa,	um	webservice	por	exemplo,	é	do	controller.	
	


## Página 33

	
Figura	3.3:	MVC	
	
	
O	Ionic	v1,	por	padrão,	cria	apenas	um	 controller	por	aplicação.	Porém,	isso	não	nos	impede	
de	separar	em	arquivos	diferentes	para	um	melhor	entendimento	e	manutenção.	
Nosso	 aplicativo	 possui,	 na	 pasta	www/js,	 dois	 arquivos:	app.js	e 	 controllers.js.	 Vamos	 focar	 no	
controllers.js,	visto	que	já	explicamos	o	app.js	no	capítulo	anterior.	
Vamos	organizar	as	coisas?	
		


## Página 34

3.2	Separando	o	joio	do	trigo	
V a m o s 	c r i a r 	u m 	c o n t r o l l e r 	n o 	n o s s o 	a p l i c a t i v o 	p a r a 	c a d a 	f u n c i o nalidade.	 Para	 isto,	
começaremos	 modificando	 o	 nome	 da	 chamada	 de	 nossa	 primeira	 funcionalidade	 (Listar	
Produtos).	Abra	o	arquivo	www/templates/menu html	e	localize	a	seguinte	linha	de	código:	
... 
<ion-list> 
    <ion-item menu-close ng-click="login()"> 
      Login 
    </ion-item> 
    <ion-item menu-close href="#/app/search"> 
      Search 
    </ion-item> 
    <ion-item menu-close href="#/app/browse"> 
      Browse 
    </ion-item> 
    <ion-item menu-close href="#/app/playlists"> 
      Playlists 
    </ion-item> 
</ion-list> 
... 
Observe	 que	 a	 transição	 entre	 as	 telas	 do	 aplicativo,	 pelo	 menu,	 são	 feitas	 conforme	 a	
marcação	<ion-item menu-close href="[chamada]">.	Em	nosso	aplicativo,	o	cardápio	ficará	dividido	em	
4 	c a t e g o r i a s 	( b e b i d a s , 	p e t i s c o s , 	s u c o s 	e 	c o n t a ) . 	P o r t a n t o , 	v a m os	 construir	 todas	 as	
configurações	deste	menu	para	chamar	cada	tela	referente	à	sua	respectiva	funcionalidade.	
Desta	maneira,	nosso	arquivo	de	menu	ficará	como	a	seguir:	
... 
<ion-item menu-close href="#/app/bebidas"> 
    Bebidas 
</ion-item> 
<ion-item menu-close href="#/app/petiscos"> 
    Petiscos 
</ion-item> 
<ion-item menu-close href="#/app/sucos"> 
    Sucos 
</ion-item> 
<ion-item menu-close href="#/app/conta"> 
    Conta 
</ion-item> 

## Página 35

Perceba	que	ainda	temos	um	trabalho	de	tradução	para	fazer.	O	t ítulo	do	menu	está	como	
left	e	deveremos	substituí‐lo	por	"Menu".	Para	isto,	abra	o	arquivo 	www/templates/menu html,	para	
editar	a	seguinte	linha:	
... 
<ion-side-menu side="left"> 
    <ion-header-bar class="bar-stable"> 
      <h1 class="title">Left</h1> 
    </ion-header-bar> 
... 
Ela	ficará	assim:	
... 
<ion-side-menu side="left"> 
    <ion-header-bar class="bar-stable"> 
      <h1 class="title">Menu</h1> 
    </ion-header-bar> 
... 
Com	estas	modificações,	temos	um	menu	seguindo	a	nossa	ideia	de	cardápio.	Veja	a	seguir:	
	
Figura	3.4:	MVC	
	
Agora	que	temos	um	menu,	vamos	dar	a	ele	mais	vida,	ou	seja,	to rná‐lo	funcional.	Para	isto,	
teremos	que	configurá‐lo	para	chamar	nossas	telas	que	conterão	nossos	produtos.		
Eles	 poderão	 ser	 carregados	 através	 de	 um	webservice.	 Porém,	 como	 nosso	 foco	 não	 será	
explanar	sobre	a	criação	destes	serviços,	faremos	isto	em	forma	de	mocks ,	ou	seja,	objetos	


## Página 36

simulados	de	forma	controlada,	para	que	tenhamos	uma	ideia	mais	concreta	dessas	listas.	
Será	uma	simulação	de	um	retorno	dos	webservices	em	formato	de	JSON.	
Webservices	s ã o 	c o m p o n e n t e s 	q u e 	p e r m i t e m 	q u e 	a s 	a p l i c a ç õ e s , 	m e s m o 	c o m 	
tecnologias	 diferentes,	 se	 comun iquem	 através	 de	 uma	 rede	 por	 padrões	
predeterminados	entre	as	duas	partes:	consumidor	(aplicação	que	consome	o	serviço)	
e	o	provedor	(aplicação	que	fornece	o	serviço).		
Vamos	começar	a	brincar?!	
3.3	O	cardápio	e	o	MVC	
Faremos	agora	todo	o	processo	de	chamada	de	uma	tela	do	nosso	aplicativo	utilizando	toda	
a	técnica	de	MVC.	Nesta	seção,	o	leitor	vai	entender	como	tudo	 isto	funciona	de	uma	forma	
bem	prática.	
Nosso	 primeiro	 passo	 será	 criar	 um	 estado	 no	 nosso	 arquivo	 www/js/app.js,	 onde	 estará	
configurada	 a	 chamada	 para	 nossa	 view	 www/templates/bebidas html. 	E s t a 	s e r á 	c o n t r o l a d a 	p o r 	
nosso	controller	www/js/bebidas-controller.js	e	terá	como	modelo	nosso	objeto	$scope.		
Observe	 que	 usamos	 de	 propósito	 a	 sopa	 de	 letrinhas	 MVC	 para	 fr i s a r 	q u e 	n o s s o 	
framework	é	baseado	neste	modelo,	como	já	foi	citado	em	nossa	introdução.	
A	view	
Para	criarmos	nossa	 view,	que	nada	mais	é	do	que	um	arquivo	HTML,	e	representar	nossa	
tela	no	aplicativo,	deveremos	construir	a	listagem	de	bebidas	d o	nosso	cardápio.	Para	isto,	
crie	um	arquivo	www/templates/bebidas.html.	Em	seu	conteúdo,	coloque	o	seguinte	código:	
<ion-view title="Bebidas"> 
    <ion-content> 
        <ion-list> 
             <ion-item ng-repeat="bebida in bebidas" href="#/app/bebida/{{bebida.id}}"> 
                {{bebida nome}} - R$ {{bebida.preco}} 
              </ion-item> 
        </ion-list> 
    </ion-content> 
</ion-view> 
P e r c e b a 	q u e 	o 	H T M L 	c o n t é m 	c o m p o n e n t e s 	o u 	m a r c a ç õ e s 	q u e 	s ã o 	p r ó prias	 do	framework	
(Ionic),	 como	 <ion-view,	 <ion-content>,	 <ion-list>	e 	 <ion-item>.	 Estes	 componentes	 fazem	 toda	 a	
diferença	 quando	 renderizadas	 no	 browser	d o s 	d i s p o s i t i v o s , 	c o n s t r u i n d o 	u m a 	i n t e r f a c e 	
elegante.		

## Página 37

Mais	adiante,	veremos	em	que	formatos	esta	marcação	ficará	e	ex plicaremos	melhor	cada	
um	deles	com	seus	respectivos	atributos	e	diretivas	( ng-repeat,	title	etc).	Para	isto,	vamos	criar	
nossa	rota	para	esta	view	e	nosso	controller	responsável	por	ela.	
O	Controller	
Nosso	controller	será	o	JavaScript	que	proverá	a	troca	( data	binding)	de	informação	entre	a	
camada	 view	( H T M L ) 	e 	o 	model	( m o d e l o ) . 	P o r t a n t o , 	v a m o s 	c r i a r 	o 	s e g u i n t e 	a r q u i v o : 	
www/js/bebidas-controller.js.		
Com	 o	 arquivo	 salvo,	 construiremos	 um	controller	que	será	composto	de	uma	codificação	
simples:	
app.controller('BebidasCtrl', function($scope){ 
    //Mock de bebidas 
    $scope.bebidas = [ 
    {'nome': 'Vinho Tinto Brasil', 'id' : 01, 'preco' : '40,00'}, 
    {'nome': 'Cerveja Especial', 'id' : 02, 'preco' : '23,00'}, 
    {'nome': 'Wisky 18 anos', 'id' : 03, 'preco' : '200,00'} 
    ] 
 
}); 
O	 que	 temos	 nesse	 código	 é	 a	 definição	 do	controller	 para	 ser	 referenciado	 pelo	 objeto	
BebidasCtrl.	Observe	 isto	 no	 primeiro	 parâmetro	 passado	 para	 a	 função	app.controller().	 Ele	 será	
carregado	 quando	 for	 chamada	 a	 view	 correspondente	 e	 executará	 a	 construção	 de	 um	
array	de	bebidas	com	3	objetos.		
O b s e r v e 	q u e 	e s t e 	a r r a y 	f o i 	a t r i b u í d o 	a 	u m 	o b j e t o 	r e f e r e n c i a d o 	por	 $scope.	 Preste	 atenção	
neste	objeto	e	não	se	preocupe,	na	seção	seguinte	falaremos	dele.		
Note	 também	 o	 comentário	 acima	 do	 array	 de	 bebidas,	 que	 informa	q u e 	i s t o 	é 	u m 	m o c k 	
(//Mock de bebidas),	ou	seja,	um	objeto	que	simulará	uma	chamada	a	um	web	service.		
Objetos	mock	são	simulações	de	objetos,	criados	para	testar	aplicações,	quando	não	há	
a 	p o s s i b i l i d a d e 	d e 	o b t ê ‐ l o s 	d e 	u m 	a m b i e n t e 	r e a l . 	E m 	n o s s o 	c a s o , 	c o m o 	f o g e 	d o 	
c o n t e x t o 	c r i a r 	u m a 	a p l i c a ç ã o 	q u e 	p r o v e r á 	u m 	webservice	 para	 consumirmos	 no	
aplicativo,	simularemos	todos	os	serviços	através	dos	mocks.	
O	model	
L e m b r a 	d e 	q u a n d o 	p e d i 	p a r a 	o 	l e i t o r 	o b s e r v a r 	o 	o b j e t o 	$scope	 na	 seção	 anterior?	 Agora	
vamos	aprender	mais	sobre	ele.	

## Página 38

Esta	 referência	 está	 diretamente	 ligada	 ao	model	d o 	M V C . 	O 	A n g u l a r J S 	u s a ‐ o 	j u s t a m e n t e 	
para	fazer	aquela	 atualização	contínua,	ilustrada	na	figura	sobre	o	 data	binding.	Através	
deste	objeto,	o	HTML	www/templates/bebidas.html	é	capaz	de	interagir	e	exibir	a	lista	em:	
<ion-item ng-repeat="bebida in bebidas" href="#/app/bebida/{{bebida.id}}"> 
     {{bebida nome}} - R$ {{bebida.preco}} 
</ion-item> 
Note	que,	na	 view,	não	foi	preciso	referenciar	o	objeto	( $scope),	porém,	no	 controller,	isso	é	
necessário.	Agora	vamos	configurar	a	chamada	para	a	tela	desta	funcionalidade.		
As	rotas	
T o d a 	c o n f i g u r a ç ã o 	d e 	t e l a 	n o 	n o s s o 	a p l i c a t i v o 	é 	t r a t a d a 	c o m o 	u m 	e s t a d o 	(state).	 Para	 que	
nossa	 tela	 de	 bebidas	 seja	 apresentada	 ao	 clicar	 no	 menu,	 devere m o s 	c r i a r 	u m a 	r o t a 	e m 	
nosso	 arquivo	www/js/app.js.	 A	 seguir,	 veja	 um	 exemplo	 de	 nosso	state	 para	 o	 template	 que	
criamos	no	item	anterior	deste	capítulo:	
  .state('app.bebidas' , { 
      url : '/bebidas', 
      views: { 
        'menuContent' : { 
            templateUrl : 'templates/bebidas html', 
            controller : 'BebidasCtrl'          
        } 
      } 
  }) 
Crie	este	estado	entre	.state('app')	e	.state('app.search').		
A	 ordem	 não	 afeta	 o	 funcionamento,	 mas	 para	 que	 façamos	 tudo	 no	m e s m o 	p a d r ã o , 	
esta	é	apenas	uma	sugestão	de	organização.	
Prontinho,	 vamos	 explicar	 nosso	 state.	 Simplesmente,	 dissemos	 que,	 ao	 invocar	 a	 URL	
/app/bebidas	( U R L 	n o 	state),	 estamos	 dizendo	 que	 devemos	 carregar	 a	view	templates/bebidas html	e , 	
juntamente	com	ela,	o	controller	www/js/bebidas-controller.js.	
Execute	 a	 aplicação	 com	 comando	ionic serve	 em	 seu	 CLI,	 demonstrado	 no	 capítulo	 anterior.	
Então,	clique	no	menu	 Bebidas	e	observe	tudo	acontecendo.	A	tela	a	seguir	deve	ser	exibida	
em	seu	browser:	

## Página 39

	
Figura	3.5:	Tela	Bebidas	
	
Não	 foi	 fácil?	 Neste	 momento,	 você	 deve	 estar	 ansioso	 para	 instalar	 o	 aplicativo	 em	 um	
celular	(ou	qualquer	outro	dispositivo	móvel),	e	observar	como	 estão	ficando	os	trabalhos	
até	aqui.	Pois	bem!	Vá	em	frente.	Execute	o	comando	já	citado	n o	capítulo	anterior	através	
do	CLI,	ionic run,	e	curta	seu	funcionamento.	
3.4	Conclusão	
Neste	 capítulo,	 foi	 explanado	 uma	 visão	 geral	 sobre	 MVC,	mocks	 e	 toda	 a	 estrutura	 que	 o	
Ionic	Framework	cria	para	que	seja	possível	a	construção	de	aplicativos	nesta	 arquitetura.	
Vimos	 que	 através	 de	 estados	 ( .state) 	n o 	a r q u i v o 	d e 	c o n f i g u r a ç ã o 	www/js/app.js,	 é	 possível	
montar	uma	transição	de	tela,	configurando	o	 controller	responsável	por	ela,	como	também	
carregar	seu	template	ou	view	(HTML).	
N o 	p r ó x i m o 	c a p í t u l o , 	c o n c l u i r e m o s 	n o s s o 	m e n u , 	c h a m a n d o 	t o d a s 	a s	 funcionalidades	 de	
nosso	 aplicativo.	 Também	 aprenderemos	 um	 pouco	 mais	 sobre	 os	 componentes	 do	
framework.	Veremos	que	existem	formas	mui to	simples	de	apresentar	listas ,	botões,	inputs	
e	labels.		
	
	


## Página 40

3.5	Para	saber	mais	
	
1. SQLite	–	http://ngcordova.com/docs/plugins/sqlite;	
2. Mock	–	https://pt.wikipedia.org/wiki/Objeto Mock ;	
3. Data	Binding	–	https://angularjs.org/	
 

## Página 41

CAPÍTULO	4	
Completando	o	menu	
Neste	 capítulo,	 concluiremos	 o	 m enu	 principal	 para	 chamar	 as	 telas	 de	 listagem	 dos	
produtos	contidos	no	cardápio.	Todo	conceito	aprendido	até	aqui 	servirá	como	base	para	o	
melhor	entendimento	do	framework ,	principalmente	no	que	diz	respeito	às	configurações	
dos	states	e	construções	dos	controllers	e	views.	
4.1	Estados	
C o m o 	v i m o s 	n o 	c a p í t u l o 	a n t e r i o r , 	t o d a 	" m á g i c a " 	d e 	t r a n s i ç ã o 	d e 	funcionalidades	 é	 feita	
através	da	configuração	de	um	estado	( .state),	também	chamado	de	rotas.	Isso	acontece	no	
arquivo	www/js/app.js,	onde	é	necessário	informar	o	template,	controller	e	construir	as	tags	que	
vão	renderizar	nossa	listagem	fornecida	pelos	mocks.		
Se	acaso	tentarmos	executar	qualquer	outra	parte	do	cardápio	–	através	do	menu	–	que	não	
seja	 "bebidas",	 o	 aplicativo	 não	 direcionará	 para	 as	 telas	 correspondentes	 pelo	 seguinte	
motivo	óbvio:	ainda	não	construímos	os	artefatos	e	configurações	necessárias	para	que	isto	
aconteça.		
Por	isso,	não	se	desespere!	Preparado	para	construir	todas	as	c hamadas	do	menu	principal	
da	aplicação?	Então,	vamos	lá!	
Abra	o	arquivo	www/js/app.js	e	adicione	um	novo	estado	(petiscos)	logo	abaixo	da	nossa	última	
configuração	.state('app.bebidas'...:	
... 
 
.state('app.petiscos', { 
      url: '/petiscos', 
      views : { 
        'menuContent' : { 
            templateUrl : 'templates/petiscos html', 
            controller : 'PetiscosCtrl' 
        } 
} 
 
... 
Criado	o	estado	 app.petiscos,	se	tentarmos	abrir	esta	tela	no	aplicativo,	teremos	um	erro	4 04	
do	protocolo	HTTP,	ou	seja,	não	será	encontrado	o	HTML	referente	e	mapeado	em	templateUrl.	
A	seguir,	veja	o	erro	que	pode	ser	verificado	no	console	do	navegador:	

## Página 42

	
Figura	4.1:	'Erro	404'	
	
Vamos	então	construir	nossa	tela	de	petiscos?	
É	 muito	 simples,	 pois	 é	 bastante	 parecida	 com	 a	 de	 bebidas	 que	 criamos	 no	 capítulo	
anterior.	Vamos	fazer	apenas	as	alterações	necessárias.		
Comece	criando	o	seguinte	arquivo	 www/templates/petiscos html	e,	em	seguida,	faremos	a	seguinte	
codificação:	
<ion-view title="Petiscos"> 
    <ion-content> 
        <ion-list> 
             <ion-item ng-repeat="petisco in petiscos" href="#/app/petisco/{{petisco.id}}"> 
                {{petisco nome}} - R$ {{petisco.preco}} 
              </ion-item> 
        </ion-list> 
    </ion-content> 
</ion-view> 
V e j a 	q u e 	h o u v e 	p o u c a s 	m u d a n ç a s 	e m 	r e l a ç ã o 	a o 	a r q u i v o 	www/templates/bebidas html.	 Só	
modificamos	o	título	da	tela,	o	nome	do	array	em	 <ion-item ng-repeat...,	e	a	referência	para	cada	
objeto	deste	array	(petisco).	
T e n t e 	a b r i r 	e s t a 	t e l a 	d o 	a p l i c a t i v o 	e 	o b s e r v e 	a 	s a í d a 	d e 	l o g 	n o	 console	 do	 seu	 navegador.	
V o c ê 	v a i 	v e r i f i c a r 	q u e 	a l g o 	e s t á 	f a l t a n d o . 	C o n s e g u e 	i d e n t i f i c a r	 qual	 arquivo	 deixou	 de	 ser	
carregado	pelo	aplicativo?		
	


## Página 43

	
Figura	4.2:	Erro	de	controller	
	
Simplesmente	referenciamos	o	nosso	 controller	no	estado	com	a	variável	 PetiscosCtrl,	porém,	
não	criamos	e	nem	carregamos	este	arquivo	no	nosso	aplicativo.	 Precisamos	criá‐lo	e,	em	
seguida,	construir	nosso	mock,	já	discutido	no	capítulo	anterior	–	ou	seja,	uma	simulação	de	
um	objeto	que	poderia	ser	o	consumo	de	um	serviço	que	estaria	na	nuvem,	por	exemplo.	
O	mock	(objeto)	de	petiscos	teria	como	atributos	um	nome,	um	identifi cador	e	o	seu	preço.	
Exibiremos	o	nome	e	preço	na	tela	principal,	em	forma	de	 grid,	e	usaremos	o	identificador	
para	carregar	os	detalhes	de	cada	petisco.		
Com	isto,	vamos	simular	que,	em	um	banco	de	dados,	temos	uma	ta bela,	com	os	petiscos	e	
seus	 atributos:	 id,	 nome,	 imagens,	 descrição	 e	 preço.	 Como	 estamos	 sempre	 falando	 em	
consumo	de	serviços,	vamos	imaginar	um	webservice	no	lugar	desta	tabela.	
Inicialmente,	 vamos	 construir	 o	 mock	s i m p l e s 	e 	e v o l u i r m o s 	a o s 	p o u c o s 	p a r a 	m e l h o r 	
entendimento.	Construindo	nosso	 controller,	nosso	arquivo	petiscos-controller.js	em	www/js/	ficará	
da	seguinte	forma:	
app.controller('PetiscosCtrl', function($scope){ 
 
    $scope.petiscos = [ 
    {'nome': 'Filé ao molho madeira', 'id' : 01, 'preco' : '60,00'}, 
    {'nome': 'Camarão ao alho', 'id' : 02, 'preco' : '21,00'}, 
    {'nome': 'Lagosta assada', 'id' : 03, 'preco' : '100,00'} 
    ] 
 
}); 


## Página 44

Mas	isto	basta?	Não!	Ainda	temos	de	referenciar	este	 JavaScript	no	nosso	HTML	principal,	
ou	seja,	no	index html.	Faça	a	inclusão	da	seguinte	tag:	
... 
<script src="js/petiscos-controller.js"></script> 
... 
Agora	 sim	 será	 possível	 carregar	 nossa	 tela	 de	 petiscos.	 Peça	 uma	 cerveja	 especial	 e,	 de	
preferência,	 para	 acompanhar	 um	camarão	 ao	 alho,	 pois	 o	 preço	 está	 bastante	 atrativo.	
Bom	apetite!	
	
Figura	4.3:	Nova	tela	–	Petiscos	
	
Deixaremos	 para	 o	 leitor	 a	 responsabilidade	 de	 criar	 a	 tela	 de	sucos	 do	 aplicativo.	 Siga	 o	
mesmo	 raciocínio	 e	 construa	 esta	 funcionalidade	 antes	 de	 prosseg u i r 	c o m 	a 	l e i t u r a . 	I s t o 	
reforçará	 o	 aprendizado	 e,	 quando	 perceber,	 já	 estará	 construin do	 estados,	 views	e 	
controllers	de	forma	automática.		
		


## Página 45

	
4.2	Conclusão	
Até	aqui,	configuramos	todo	 menu	do	aplicativo,	exceto	 Conta.	Este	deixaremos	para	o	final	
do	livro.	
No	próximo	capítulo,	vamos	permitir	que	o	usuário	navegue	melho r	no	cardápio,	clicando	
em	cada	item	em	que	terá	uma	breve	descrição	e	uma	foto,	além	de	disponibilizar	um	botão	
p a r a 	e f e t u a r 	o 	p e d i d o . 	C o m o 	e s t a 	d e m a n d a , 	a c r e s c e n t a r e m o s 	n o v o s 	a t r i b u t o s 	n o s 	mocks	
para	representar	o	detalhamento	do	item.	
4.3	Para	saber	mais	
	
1. Controllers	em	AngularJS	–	https://docs.angularjs.org/guide/controller	
 

## Página 46

CAPÍTULO	5	
Detalhando	os	itens	
Neste	capítulo,	vamos	construir	novas	telas	para	o	aplicativo,	 onde	será	possível	visualizar	
detalhes	 sobre	 cada	 item	 do	 cardápio,	 como	 imagem,	 descrição,	 al é m 	d e 	s e r 	p e r m i t i d o 	
efetuar	 pedidos.	 Para	 isto,	 vamos	 pôr	 em	 prática	 um	 conceito	 mu ito	 utilizado	 em	
desenvolvimento	 de	softwares	 que	 é	 o	 reaproveitamento.	 Perceba	 que	 a	 tela	 de	 detalhes	
será	igual	para	todos	os	itens,	por	isto,	vamos	planejar	uma	tela	que	seja	reutilizada.	
5.1	O	protótipo	
Pensando	em	uma	tela	genérica	para	nosso	aplicativo,	chegaremos 	a	al go	par e cido	com 	o	
protótipo	da	figura	a	seguir:	
	
	
Figura	5.1:	Protótipo	
	


## Página 47

Observe	que	carregaremos	de	cada	item	um	título,	uma	imagem,	um a	breve	descrição	e	seu	
valor	(preço).	Caso	o	usuário	opte	por	efetuar	o	pedido,	o	apli cativo	direcionará	para	uma	
página	 (ou	 modal)	 de	 confirmação,	 onde	 ele	 poderá	 desistir,	 ou	informar	 a	 quantidade	 e	
confirmar.		
Quantas	cervejas	você	pedirá	com	a	turma	do	trabalho	sexta‐feir a	à	noite?	Acho	que	o	input	
de	quantidade	veio	a	calhar	neste	momento,	não	é	mesmo?!	
Agora	que	temos	uma	ideia,	vamos	colocá‐la	em	prática.	Pense	ta mbém	sobre	um	serviço	
que	seja	reaproveitado	para	que	não	fiquemos	duplicando	os	 mocks	em	cada	tela.	A	seguir,	
vamos	 aprender	 a	 organizar	 estes	mocks,	 simulando	 melhor	 uma	 chamada	 a	 um	 serviço.	
Para	isso,	faremos	uma	outra	camada	na	nossa	aplicação.	
5.2	Camada	de	serviços	
Já	vimos	como	criar	arquivos	JavaScript	que	têm	a	função	de	controllers.	Da	mesma	forma,	o	
Ionic	p e r m i t e 	c r i a r 	s e r v i ç o s 	( n ã o 	c o n f u n d a 	c o m 	w e b s e r v i c e s ) 	q u e 	s ã o 	scripts	 reutilizáveis	
dentro	 de	 uma	 aplicação.	 Isto	 elimina	 a	 replicação	 de	 código	 e	centraliza	 funcionalidades	
em	camadas,	como	demonstra	a	figura	a	seguir.	
	
Figura	5.2:	Camadas	
	
	


## Página 48

I s t o 	i l u s t r a 	q u e 	o s 	controllers	 passarão	 agora	 a	 fazer	 chamadas	 aos	services	q u e , 	p o r 	s u a 	
vez,	consomem	 webservices	fora	da	aplicação.	Na	prática,	em	nosso	app,	isto	não	ocorrerá ,	
pois	vamos	apenas	simular	o	consumo	destes	serviços	através	dos	mocks.	
Entretanto,	 se	 houvesse	 a	 necessidade	 de	 se	 implementar	webservices,	 estes	 estariam	 em	
algum	 servidor	 na	 nuvem.	 E	 nossos	 scripts	 (serviços),	 dentro	 da	 aplicação,	 seriam	 os	
responsáveis	por	consumi‐los.	
5.3	Criando	os	arquivos	
S e 	v o c ê 	f o s s e 	p e n s a r 	n a 	a r q u i t e t u r a 	d a 	s e ç ã o 	a n t e r i o r , 	f a r i a 	u m 	a r q u i v o 	(service)	 que	
centralizasse	 todas	 as	 chamadas	 aos	 webservices,	 ou	 vários	 arquivos,	 um	 para	 cada	
funcionalidade?	 Depende,	 não	 é	 mesmo?	 Mas,	 depende	 de	 quê?	 Do	 quão	 complexa	 será	 a	
aplicação.		
E m 	n o s s o 	c a s o , 	f a r e m o s 	a p e n a s 	u m 	a r q u i v o , 	p o i s 	é 	u m 	a p l i c a t i v o 	s i m p l e s , 	p e q u e n o 	e 	d e 	
fácil	 manutenção.	 Mas,	 se	 por	 acaso	 você	 estivesse	 trabalhando	e m 	u m a 	a p l i c a ç ã o 	m a i o r , 	
em	que	o	escopo	fosse	uma	infinidade	de	funcionalidades,	a	melh or	opção	seria	dividir	em	
vários	 services,	 pois	 faria	 jus	 à	 máxima	 da	 Ciência	 da	 Computação:	 dividir	 para	
conquistar.	Esta	seria	a	melhor	solução.	
Portanto,	 vamos	 iniciar	 criando	 o	 arquivo	 da	 camada	 de	 services. 	C r i e 	p a r a 	i s t o 	a 	p a s t a 	
www/js/services.	Preste	atenção	que	criamos	uma	pasta	para	organizar	nossos	 services,	porém	
teremos	na	aplicação	apenas	um	arquivo.	Sugeri	no	plural	apenas	com	o	propósito	didático	
para	 demonstrar	 que	 tudo	 pode	 ser	 organizado	 por	 pastas.	 Na	 seç ão	 seguinte,	 vamos	
organizar	da	mesma	forma	todos	os	nossos	controllers.	
A g o r a 	v a m o s 	c r i a r 	n o s s o 	a r q u i v o 	c u j o 	n o m e 	s e r á 	cardapio-services.js,	 dentro	 de	 nossa	 pasta	
www/js/services,	 que	 ainda	não	 será	funcional,	 pois	 não	vai	 dispor	 de	nenhum	 código.	 Apenas	
vamos	criá‐lo	para	usar	como	piloto	de	nosso	propósito.	Ele	ficará	da	seguinte	forma:	
app.service('CardapioServices', function(){ 
 
}); 
Observe	que	estamos	dando	a	este	objeto	a	referência	 CardapioServices,	que	usaremos	logo	em	
seguida	em	nossos	controllers.		
Criado	 o	 arquivo,	 precisamos	 injetar.	 Lembra‐se	 deste	 termo	 qua n d o 	s u g e r i 	q u e 	s e 	
familiarizasse	com	ele,	lá	no	capítulo	 Iniciando	nossa	aplicação?	Pois	é!	Vamos	agora	injetar	
nosso	 service	n o 	controller,	 abrindo	 nosso	 arquivo	 www/js/petiscos-controller.js	 e	 inserindo	 a	
referência	do	service	dentro	da	function.	Ela	ficará	da	seguinte	forma:	

## Página 49

app.controller('PetiscosCtrl', function($scope, CardapioServices){ 
... 
Agora	tente	chamar	a	tela	de	petiscos	no	menu	do	aplicativo	e	observe	o	log	no	console	do	
navegador.	A	seguir,	veja	o	que	deve	ter	acontecido	com	seu	aplicativo:	
	
Figura	5.3:	Erro	de	injeção	
	
O	que	o	 Ionic	está	nos	informando	é	que	você	injetou	 CardapioServices	em	PetiscosCtrl,	ou	seja,	em	
n o s s o 	c o n t r o l l e r , 	p o r é m 	e l e 	a i n d a 	é 	d e s c o n h e c i d o . 	S a b e 	o 	p o r q u ê	 disto?	 Simplesmente	
precisamos	importar	o	arquivo	JavaScript	em	nosso	index.html.	Vamos	lá?!	
Abra	o	arquivo	principal	index html	e	insira	abaixo	da	declaração	do	service	de	nosso	cardápio.	
    <script src="js/services/cardapio-services.js"></script> 
Prontinho!	 Agora	 o	 erro	 não	 ocorrerá	 mais,	 porém,	 ainda	 precisa mos	 simular	 os	
webservices	e 	i n v o c á ‐ l o s 	n o s 	controllers.	 Para	 isto,	 crie	 todos	 os	mocks	q u e 	u s a r e m o s 	e m 	
www/js/services/cardapio-services.js. 	L e m b r e ‐ s e 	d e 	q u e 	t o d o s 	o s 	n o s s o s 	i t e n s 	t ê m 	c o m o 	a t r i b u t o s 	o 	
nome,	um	identificador	(id)	e	seu	preço.	Para	isto,	criamos	os	 mocks	em	formato	de	array ,	
como	no	código	a	seguir:	
app.service('CardapioServices', function(){ 
    //Mock Bebidas 
    var bebidas = [ 


## Página 50

        {'nome':'Vinho Tinto Brasil','id':01,'preco':'40,00'}, 
        {'nome':'Cerveja Especial','id':02,'preco':'23,00'}, 
        {'nome':'Wisky 18 anos','id':03,'preco':'200,00'} 
    ]; 
    //Mock Petiscos 
    var petiscos = [ 
        {'nome':'Filé ao molho madeira','id':01,'preco':'60,00'}, 
        {'nome':'Camarão ao alho','id':02,'preco':'21,00'}, 
        {'nome':'Lagosta assada','id':03,'preco':'100,00'} 
    ]; 
 
    //Mock Sucos 
    var sucos = [ 
        {'nome':'Cajá','id':01,'preco':'3,00'}, 
        {'nome':'Açaí','id':02,'preco':'4,00'}, 
        {'nome':'Cacau','id':03,'preco':'5,00'} 
    ]; 
 
    this.getPetiscos = function(){ 
        return petiscos; 
    } 
 
    this.getBebidas = function(){ 
        return bebidas; 
    } 
 
    this.getSucos = function(){ 
        return sucos; 
    } 
 
}); 
Observe	 que	 transferimos	 todos	 os	mocks	 para	nosso	service	e 	c r i a m o s 	c h a m a d a s 	à s 	s u a s	
funções	 pelo	 modificador	 this.	 Desta	 forma,	 não	 precisamos	 mais	 destes	 mocks	n o s 	
controllers,	 ficando	 assim	 mais	 p róximo	 de	 uma	 aplicação	 real,	 na	 qual	 invocaremos	
sempre	os	webservices	através	desta	última	camada.	
Para	que	tudo	fique	em	seu	lugar,	vamos	modificar	o	 controller	petiscos-controller.js,	removendo	
o	mock	de	petiscos	e	chamando‐o	por	meio	do	 service.	Observe	como	ficará	nosso	arquivo	
final:	
app.controller('PetiscosCtrl', function($scope, CardapioServices){ 
    $scope.petiscos = CardapioServices.getPetiscos(); 
}); 

## Página 51

Deixo	aqui	mais	um	desafio	ao	leitor	de	transferir	as	chamadas	 ao	serviço	correspondente	
p a r a 	o 	c o n t r o l l e r 	d e 	b e b i d a s 	e 	s u c o s . 	N o 	f i n a l , 	p e ç a 	u m 	s u c o 	d e	 cacau,	 pois	 precisamos	
refrescar	um	pouco	nossa	mente	para	organizar	nossa	aplicação	na	próxima	seção.	
5.4	Ordem	na	casa	
A n t e r i o r m e n t e , 	c r i a m o s 	a 	p a s t a 	www/js/services, 	o n d e 	o r g a n i z a m o s 	n o s s o 	a r q u i v o 	d a 	c a m a d a 	
d e 	s e r v i ç o . 	S e g u i n d o 	o 	m e s m o 	r a c i o c í n i o , 	v a m o s 	o r g a n i z a r 	n o s s a 	camada	 de	 controller.	
Fazendo	isto,	você	estará	facilitando	a	manutenção,	permitindo	 ao	desenvolvedor	a	rápida	
localização	dos	arquivos	referentes	a	cada	camada	e	funcionalidade.	
Para	 isto,	 crie	 a	 pasta	controllers	e m 	www/js,	 e	 transfira	 para	 ela	 os	 arquivos	controllers.js,	bebidas-
controller.js,	petiscos-controller.js	e	sucos-controller.js.	Mas	isto	não	basta;	lembre‐se	de	nossa	importação	
de	scripts	no	arquivo	index html,	onde	esta	aponta	para	www/js.	Veja	a	seguir:	
... 
<!-- your app's js --> 
    <script src="js/app.js"></script> 
    <script src="js/controllers.js"></script> 
 
    <script src="js/bebidas-controller.js"></script> 
    <script src="js/petiscos-controller.js"></script> 
    <script src="js/sucos-controller.js"></script> 
    <script src="js/detalhar-controller.js"></script> 
... 
Modifique‐o	 para	 que	 referencie	 os	 arquivos	 na	 nova	 pasta	 criada,	 ficando	 da	 seguinte	
forma:	
... 
<!-- your app's js --> 
    <script src="js/app.js"></script> 
    <script src="js/controllers/controllers.js"></script>     
    <script src="js/controllers/bebidas-controller.js"></script> 
    <script src="js/controllers/petiscos-controller.js"></script> 
    <script src="js/controllers/sucos-controller.js"></script> 
 
    <script src="js/services/cardapio-services.js"></script> 
... 
Observe	que	transferimos	também	um	arquivo	que	ainda	nem	altera mos,	o	controllers.js.	Este	
controller	é 	o 	r e s p o n s á v e l 	p o r 	c a r r e g a r 	t o d o s 	o s 	o u t r o s 	controllers, 	p o i s 	é 	e l e 	q u e m 	
instancia	 a	 variável	app	u s a d a 	p o r 	t o d o s 	o s 	o u t r o s 	a r q u i v o s , 	i n c l u s i v e 	o s 	services.	 Por	 isto,	
este	é	o	primeiro	controller	a	ser	carregado	no	arquivo	index html.	

## Página 52

Se	esta	sequência	for	alterada,	o	aplicativo	não	funcionará,	porque	o	HTML	é	carregado	
sequencialmente	de	cima	para	baixo.	
Depois	de	transferido	para	a	nova	estrutura	de	pastas,	abra	o	a rquivo	controllers.js	e	edite‐o,	
deletando	 tudo	 o	 que	 há	 nele,	 deixando	 apenas	 a	 função	 de	 carre gamento	 dos	 outros	
controllers.	Isso	porque	usaremos	para	isto	a	variável	 app,	que	está	sendo	instanciada	nele,	
pegando	a	referência	de	angular.module(),	isto	é,	o	módulo	principal	do	AngularJS.	
var app = angular.module('starter.controllers', []); 
 
app.controller('AppCtrl', function($scope, $ionicModal, $timeout) { 
    //Nenhuma function 
}); 
Muito	 bem!	 Tudo	 organizado	 agora ,	 vamos	 fazer	 o	 detalhamento	 de 	 cada	 item,	 como	
planejado	no	início	deste	capítulo.	
5.5	Criando	a	tela	genérica	
Até	 aqui,	 só	 vimos	 um	 protótipo	 de	 nossa	 tela	 de	 detalhes	 dos	 itens.	 Vamos	 construir	
utilizando	 os	 componentes	 CSS	 do	 Ionic, 	d e 	f o r m a 	q u e 	f i q u e 	b e m 	p r ó x i m a 	a o 	n o s s o 	
protótipo.	O	pessoal	de	design	vai	adorar	saber	que	você	foi	fiel	ao	protótipo.	
Crie	o	seguinte	arquivo	na	sua	pasta	 www/templates/detalhe-item html.	Nele	insira	o	seguinte	código	
e	vamos	analisá‐lo:	
<ion-view> 
  <ion-content> 
      <div class="card"> 
          <div class="item"> 
              <p>Titulo do Item</p> 
              <img  
            src="http://www.abgsolucoes.com.br/publico/noimage.png"  
            width="100%"> 
              <p>Descrição:</p> 
              <div class="item item-text-wrap"> 
                  <p> 
                  Aqui, alguma descrição. 
                  </p> 
              </div> 
              <p>Preço: R$ XX,XX</p> 
          </div> 
    </div> 

## Página 53

    <div class="item"> 
    <div class="bar bar-footer"> 
            <button class="button  icon-right ion-checkmark button-positive button-full"> 
            Pedir 
         </button> 
      </div> 
      </div> 
  </ion-content> 
</ion-view> 
Calma!	Não	se	desespere!	Vamos	tentar	entender	ao	máximo	o	que	 está	acontecendo	nesta	
tela.	
Vejamos	o	resultado	deste	código	e,	logo	em	seguida,	a	explicação	da	view.	
	
Figura	5.4:	Pagina	de	detalhes	
	
	


## Página 54

	
Lembra	da	nossa	introdução,	onde	há	uma	explanação	que	o	 Ionic	é	o	framework	focado	no	
front	view	da	ap l ic aç ão . 	Po is	b em ,	aq u i	fic ará	b em 	c l aro 	q u e	u sam os	m u itos	componentes	
prontos	em	CSS,	facilitando	assim	a	vida	do	desenvolvedor	de	ap licativos.	Vamos	explicar	o	
código	anterior	e	entender	cada	componente	nele.	
No	 início,	 temos	 uma	 div card.	 Os	 cards	 são	 retângulos	 com	 sombreamentos	 bastante	
utilizados	 em	 aplicativos.	 Eles	dão	 destaque	 para	 diversos	 conteúdos,	 sejam	 estes	 textos,	
imagens,	botões	ou	forms.	
Em	nossa	tela,	observe	que	o	título	do	item,	a	imagem,	a	descri ção	e	o	preço	encontram‐se	
dentro	do	nosso	 card,	e	isto	dá	uma	aparência	agradável	ao	aplicativo,	além	de	dest acar	o	
conteúdo,	separando‐o	do	botão	de	ação	Pedir.	
Observe	 que	 cada	 parte	 do	 conteúdo	 foi	 separado	 pelas	 marcações	<div>,	 com	 a	 classe	 de	
estilo	 item.	 Este	 dá	 o	 destaque	 tracejando	 cada	 elemento,	 como	 os	 traços	 a baixo	 de	
"Descrição"	e	acima	de	"Preço".	
Por	fim,	o	botão	Pedir	que	contém	5	classes.	Na	sequência,	temos	a	classe	button	informando	ao	
framework	q u e 	i s t o 	é 	u m 	b o t ã o , 	c o m 	u m 	í c o n e 	p o s i c i o n a d o 	à 	d i r e i t a 	(icon-right)	 e	 com	
símbolo	de	um	check	(ion-checkmark).		
Existem	 muitos	 ícones	 já	 prontos	 para	 serem	 utilizados	 no	 Ionic.	 Estes	 podem	 ser	
encontrados	em	http://ionicons.com.	
A	 classe	button-positive	c o n f i g u r a 	a p e n a s 	a 	c o r 	d o 	b o t ã o 	p a r a 	a z u l 	e , 	l o g o 	e m 	s e g u i d a , 	temos	
uma	 classe	 chamada	 button-full. 	E s t a 	d e t e r m i n a 	q u e 	o 	b o t ã o 	s e j a 	d a 	l a r g u r a 	d a 	t e l a 	d o 	
dispositivo,	ajustando	ao	máximo.	Sem	esta	classe,	o	botão	se	ajustaria	apenas	ao	label.	
Por	fim,	este	botão	está	dentro	de	uma	 <div>	que	determina	o	rodapé	da	tela	em	forma	de	
barra	(bar e bar-footer).	
F á c i l , 	n ã o 	é ? ! 	M a s 	é 	p r e c i s o 	d e c o r a r 	t o d a s 	e s t a s 	c l a s s e s ? 	N ã o ! 	S e m p r e 	q u e 	f o r 	p r e c i s o , 	
podemos	 consultar	 os	 componentes	 do	 Ionic	e m 	
http://ionicframework.com/docs/components/.	
5.6	Passando	um	parâmetro	
Já	imaginou	como	faremos	para	transitar	da	tela	principal	de	ca da	seção	do	cardápio	para	o	
detalhamento	 dos	 itens?	 Lembre‐se	 de	 que	 cada	 item	 tem	 um	 ident ificador	 e,	
anteriormente,	citamos	que	usaremos	dois	 webservices	neste	contexto:	um	para	carregar	a	

## Página 55

lista	de	itens,	e	outro	para	o	seu	detalhamento.	Portanto,	poderemos	imaginar	que,	ao	clicar	
em	um	item,	enviaremos	o	seu	id	para	que	o	serviço	retorne	os	seus	detalhes.	
Vamos	 ver	agora	 como	 passar	 parâmetros	 entre	as	 telas	 e	 recuperá‐los	 nas	 transições	 de	
nosso	 aplicativo.	 Para	 isto,	 precisamos	 construir	 um	 controller	e m 	 www/js/controllers,	 e	
configurá‐lo	no	www/js/app.js,	mapeando	sua	rota	através	de	um	estado	(.state).	
Portanto,	 crie	 um	 arquivo	 e	 dê	 a	 ele	 o	 nome	 detalhar-controller.js,	 salvando‐o	 na	 pasta	
www/js/controllers.	Em	seguida,	dê	a	ele	uma	referência	denominada	'DetalharCtrl'.	
app.controller('DetalharCtrl', function($scope){ 
 
}) 
Lembre‐se	 de	 que	 esta	 referência	 será	 utilizada	 em	 nosso	 arquivo	 de	 configuração,	 onde	
criaremos	o	estado	para	a	transição	entre	a	tela	principal	e	os 	itens	que	serão	detalhados.	
Para	isto,	no	arquivo	 www/app.js,	logo	abaixo	do	último	estado	que	configuramos	( app.petiscos),	
crie	um	estado	que	terá	como	diferencial	a	passagem	de	parâmetr o	na	URL.	Veja	como	ele	
ficará:	
... 
.state('app.detalhar', { 
      url: '/detalhar/:itemID', 
      views : { 
        'menuContent' : { 
            templateUrl : 'templates/detalhe-item html', 
            controller : 'DetalharCtrl' 
        } 
      } 
  }) 
... 
Observe	que,	na	URL,	fizemos	a	passagem	do	parâmetro	 id	do	item.	Este	será	utilizado	para	
carregar	o	detalhamento	dele,	independente	de	qual	seja.	Assim,	permitirá	que	a	nossa	tela,	
de	fato,	torne‐se	genérica,	isto	é,	seja	reaproveitada	em	todos	os	itens	disponíveis.		
A l t e r e 	o 	a r q u i v o 	www/templates/petiscos.html	 para	 que	 chame	 a	 URL	 passando	 o	 parâmetro	id	d o 	
item.	 Para	 isto,	 modifique	 o	 atributo	href	d a 	l i s t a 	p a r a 	q u e 	p a s s e 	o 	i d e n t i f i c a d o r 	d e 	c a d a 	
objeto	carregado	na	grid.	
... 
<ion-item  
    ng-repeat="petisco in petiscos"  
        href="#/app/detalhar/{{petisco.id}}"> 
... 

## Página 56

Agora	tente	clicar	nos	petiscos	para	ver	a	tela	sendo	executada .	Se	tudo	ocorreu	bem,	você	
visualizará	a	tela	genérica	em	todos	eles.	Apesar	de	já	estar	p assando	o	parâmetro	na	URL,	
como	 pode	 ser	 observado	 no	 campo	 de	 endereço	 do	 seu	 browser,	 nada	 está	 sendo	 feito	
com	ele.	Na	seção	seguinte,	vamos	aprender	a	recuperar	este	parâmetro	e	carregar	apenas	
o	detalhamento	do	item	referente	a	ele.	
5.7	Recuperando	o	parâmetro	
Como	já	foi	explanado	na	seção	anterior,	precisamos	recuperar	o	parâmetro	itemID	na	tela	de	
detalhamento,	para	que	possamos	consumir	o	serviço	que	retorna	 estes	detalhes.	Para	isto,	
o	Ionic	Framework	utiliza	o	objeto	$stateParams.	Você	precisa	apenas	injetar	este	objeto	em	seu	
controller	para	que	possa	utilizá‐lo.	Vamos	fazer	uma	experiência	baseada	nisto?		
Crie	um	objeto	item	dentro	do	controle	DetalharCtrl,	recupere	o	itemID	e	atribua	a	este	objeto.	Em	
seguida,	na	tela	genérica	de	detalhamento	de	itens,	exiba	este	 valor.	Para	isto,	nosso	código	
deverá	ficar	da	seguinte	forma:	
app.controller('DetalharCtrl', function($scope, $stateParams){ 
    $scope.item = {}; 
    $scope.item.id = $stateParams.itemID;  
}) 
Agora	você	tem	um	problema	para	resolver.	Depois	de	ter	passado 	o	parâmetro	para	tela	
seguinte	e	recuperá‐lo	dentro	de	seu	 controller,	como	você	conseguirá	exibi‐lo	na	sua	 view?	
Você	se	lembra	do	data	binding	citado	em	nossa	explicação	sobre	AngularJS?	Pois	bem,	esta	
é	a	grande	mágica	ou	magia,	como	queira	chamá‐la,	do	nosso	 framework.	Constantemente,	
toda	atualização	feita	no	controller	é	exibida	na	view.		
Faça	esta	experiência	e	veja	na	prática	o	id	sendo	exibido,	o	que	significa	que	foi	recuperado	
do	evento	 click	da	tela	anterior.	Para	exibi‐lo,	basta	inserir	em	sua	 view	uma	referência	ao	
objeto	item,	desta	maneira:	{{item.id}}.	
5.8	Criando	o	serviço	de	detalhamento	
Construiremos	 nesta	 seção	 um	 simulador	 de	 webservice,	 que	 retornará	 os	 atributos	 de	
detalhes	dos	itens	do	cardápio	para	que	sejam	exibidos	na	tela	 genérica.	Para	isto,	vamos	
imaginar	 que	 cada	 item	 deve	 conter	 um	 título,	 uma	 imagem,	 uma	 descrição	 e	 um	 preço.	
T u d o 	i s s o 	f o i 	e s b o ç a d o 	n a 	t e l a 	d o 	p r o t ó t i p o 	d o 	d e t a l h a m e n t o 	d o 	item,	 exibida	 neste	
capítulo.		

## Página 57

Agora	 que	 conhecemos	 todos	 os	 atributos	 do	 nosso	 objeto,	 vamos	codificá‐lo	 para	 que	 o	
serviço	retorne‐os,	simulando	um	acesso	ao	banco	de	dados	e	faz endo	uma	consulta	pelo	id	
de	cada	item.	
Como	você	pode	observar,	nosso	parâmetro	de	passagem	é	o	 id,	portanto,	deve	estar	claro	
que	 nosso	 webservice	 receberá	 o	 identificador	 do	 item.	 Com	 este	 parâmetro,	 o	 serviç o	
consultará	um	array	de	itens,	onde	deverá	comparar	cada	identif icador	e	retornar	o	objeto	
referente	a	ele.		
Esta	não	é	a	melhor	forma	de	se	localizar	um	objeto	em	uma	apli cação,	mas	estamos	
simulando	 com	 mocks,	 e	 não	 com	 bancos	 de	 dados	 reais.	 Se	 fosse	 dessa	 forma,	
e s t a r í a m o s 	p a s s a n d o 	p a r a 	o 	s e r v i ç o 	o 	id	 do	 item	 e	 este	 retornaria	 o	 item	 referente,	
a t r a v é s 	d e 	u m a 	c o n s u l t a 	a o 	b a n c o 	c o m 	u m 	SELECT.	 Em	 nosso	 caso,	 simularemos	
percorrendo	a	lista	dos	mocks	até	encontrar	o	item	desejado.		
Para	 isto,	 vamos	 utilizar	 o	 mesmo	 arquivo	 que	 criamos	 os	 serviços,	 ou	 seja,	 nosso	
CardapioServices	q u e 	s e 	e n c o n t r a 	n a 	p a s t a 	www/js/services.	 Considerando	 que	 cada	 item	 será	
comparado	 pelo	 id,	 vamos	 modificar	 nossos	 arrays	 de	 itens	 para	 que	 eles	 tenham	 u m	
identificador	único,	simulando	assim	uma	tabela	de	itens	em	um	 banco	de	dados	real.	Para	
isto,	 vamos	 alterar	 todos	 os	ids	 a	 partir	 dos	petiscos,	 onde	 receberá	 os	ids	3 , 	4 , 	5 	e 	a s s i m 	
sucessivamente.		
Além	 disto,	 devemos	 acrescentar	 a	 imagem	 e	 descrição	 de	 cada	 item.	 Neste	 livro,	
alteraremos	apenas	o	cardápio	de 	bebidas,	deixando	a	cargo	do	leitor	fazer	a	alteração	dos	
demais	itens,	a	título	de	exercício	e	prática.	
Com	isto,	nosso	serviço	passará	a	ter	o	seguinte	conteúdo:		
    //Mock Bebidas 
var bebidas = [ 
    {'nome':'Vinho Tinto Brasil','id':1,'preco':'40,00',  
    'imagem':'img/garrafas.png','descricao':'Vinho tinto seco, da região Sul do país.'}, 
    {'nome': 'Cerveja Especial','id':2,'preco':'23,00',  
    'imagem':'img/cerveja.png','descricao':'Cerveja elaborada artesanalmente com um toque frutado.'}, 
    {'nome':'Wisky 18 anos','id':3,'preco':'200,00', 
    'imagem':'img/wisky.png','descricao':'Wisky de fabricação Russa.'} 
]; 
//Mock Petiscos 
var petiscos = [ 
    {'nome': 'Filé ao molho madeira','id' : 4,'preco' : '60,00'}, 
    {'nome': 'Camarão ao alho', 'id' : 5, 'preco' : '21,00'}, 
    {'nome': 'Lagosta assada', 'id' : 6, 'preco' : '100,00'} 
]; 
 

## Página 58

//Mock Sucos 
. 
. 
. 
O	que	modificamos?	Como	foi	descrito,	alteramos	os	ids,	a	partir	do	array	de	pestiscos,	para	
que	tenham	um	identificador	único.	Já	no	array	de	bebidas,	adic ionamos	uma	descrição	e	
um	caminho	para	uma	imagem	que	deve	estar	na	pasta	img.		
C a s o 	o 	l e i t o r 	p r e f i r a , 	p o d e 	b a i x a r 	n o s s a 	i m a g e m 	c l o n a n d o 	o 	s e g uinte	 repositório:	
https://github.com/adriangois/livro‐ionicframework.	Todo	nosso	código	estará	disponível	
neste	repositório	e	poderá	ser	baixado	pelo	leitor.	
Mas	o	que	falta?	Um	método	que	recebe	um	 id	e	retorne	o	item	referente.	Para	isto,	vamos	
criar	a	seguinte	função	JavaScript:	
this.getDetalheItem = function(id, callback){ 
 
        bebidas.forEach(function(bebida){ 
            if(bebida.id == id){ 
                callback(bebida); 
            } 
        }); 
 
        petiscos forEach(function(petisco){ 
            if(petisco.id == id){ 
                callback(petisco); 
            } 
        }); 
 
        sucos forEach(function(suco){ 
            if(suco.id == id){ 
                callback(suco); 
            } 
        }); 
    } 
 
    callback = function(item){ 
        return item; 
    } 
Observe	 que	 percorremos	 todas	 as	 listas	 do	 cardápio,	 através	 da 	f u n ç ã o 	forEach	d o 	
JavaScript.	 Assim	que	encontramos	um	item	 com	o	identificador	igual	ao	qu e	foi	passado,	
retornaremos	através	de	uma	função	de	callback.		

## Página 59

Não	 se	 desespere!	Callback	é 	u m a 	f u n ç ã o 	e m 	JavaScript, 	e m 	q u e 	o 	i n t e r p r e t a d o r 	e x e c u t a 	
assim	que	finaliza	todo	processamento	da	função	principal.	Ou	s eja,	por	ser	uma	linguagem	
assíncrona,	 o	 JavaScript	 executaria	 os	 3	 forEachs 	e m 	p a r a l e l o , 	e 	n o s s o 	r e t o r n o 	n ã o 	s e r i a 	
satisfatório.	 Fizemos	 isto	 para	 que,	 ao	 final	 do	 processamento,	 seja	 chamada	 a	 função	
retornando	nosso	item.	
5.9	Detalhando	o	item	
Q u a s e 	t u d o 	p r o n t o , 	r e s t a m ‐ n o s 	d o i s 	d e t a l h e s 	p a r a 	q u e 	n o s s o 	s e r v i ç o 	s e j a 	c h a m a d o 	e 	o s 	
itens	sejam	exibidos:	
a)	 Modificar	 nosso	 controller	 de	 detalhamento	 (DetalharCtrl)	 para	 injetarmos	 CardapioServices.	
Também	 executaremos	 a	 chamada	 ao	 serviço	 getDetalheItem,	 passando	 o	 id	e 	u m a 	f u n ç ã o 	
(citada	acima)	de	callback,	recebendo	um	item:	
app.controller('DetalharCtrl',  
    function($scope, $stateParams, CardapioServices){ 
    $scope.item = {}; 
    CardapioServices.getDetalheItem($stateParams.itemID,  
        function(item){ 
            $scope.item = item; 
        }); 
}) 
b)	Modificar	nossa	view	(detalhe-item html)	para	que	ela	receba	os	atributos	do	objeto	passado:	
<ion-view> 
  <ion-content> 
      <div class="card"> 
          <div class="item"> 
              <h1>{{item.nome}}</h1> 
              <!-- <img src="http://www.abgsolucoes.com.br/publico/noimage.png" width="100%"> --> 
        <div class="card"> 
          <img class="centralizar-imagem margem-imagem" src="{{item.imagem}}" width="60%"> 
        </div> 
              <p>Descrição:</p> 
              <div class="item item-text-wrap"> 
                  <p> 
                  {{item.descricao}} 
                  </p> 
              </div> 
              <p>Preço: R$ {{item.preco}}</p> 
          </div> 
    </div> 

## Página 60

    <div class="item"> 
    <div class="bar bar-footer"> 
            <button class="button icon-right ion-checkmark button-positive button-full">Pedir</button> 
      </div> 
      </div> 
  </ion-content> 
</ion-view> 
Customizamos	 duas	 classes	 no	 CSS	 da	 aplicação	 em	www/css/style.css:	 centralizar-imagem	e 	margem-
imagem.	Elas	foram	criadas	para	centralizar	a	imagem	do	item	e	inseri r	uma	margem	abaixo	
para	organização	dos	elementos	na	tela.	Vejamos	a	seguir	o	código	CSS:	
.centralizar-imagem{ 
    margin-left: 20%; 
} 
 
margem-imagem{ 
    padding:1em; 
} 
A	partir	daqui,	vamos	utilizar	muito	essas	classes,	principalmente	a	margem-imagem.		
Feito	 isto,	 façamos	 um	 teste	 clicando	 no	 cardápio	 de	 bebidas	 e,	e m 	s e g u i d a , 	d e t a l h a n d o 	
cada	um	dos	3	itens	listados	nele.	Veja	o	resultado	na	figura:	

## Página 61

	
Figura	5.5:	Detalhamento	de	item	
	
		


## Página 62

5.10	Conclusão	
Neste	capítulo,	vimos	como	passar	parâmetros	de	uma	tela	para	o utra	e	criar	serviços.	Com	
isto,	aprendemos	a	detalhar	todos	os	itens	utilizando	uma	premi ssa	muito	importante	em	
programação:	 reaproveitamento.	 Criamos	 apenas	 uma	 tela	 genérica ,	 e	 nela	 detalhamos	
todos	os	itens,	independente	de	qual	cardápio	ele	faça	parte.	
N o 	p r ó x i m o 	c a p í t u l o , 	v a m o s 	c r i a r 	n o s s a 	l i s t a 	d e 	p e d i d o s 	e 	e n v i ar	 para	 o	 serviço,	
adicionando	todos	os	valores	em	uma	conta.	
5.11	Para	saber	mais	
	
1. Cards	–	http://ionicframework.com/docs/components/#cards	
2. Listas	–	http://ionicframework.com/docs/api/directive/ionList	
 

## Página 63

CAPÍTULO	6	
Fazendo	pedidos	
Neste	 capítulo,	 vamos	 dar	 vida	 ao	 botão	Pedir	 da	 tela	 de	 detalhes	 do	 item,	 para	 que	 assim	
possamos	simular	um	carrinho	de	compras	dos	sistemas	de	 e‐commerce.	O	fluxo	funciona	
da	seguinte	maneira:	o	cliente	faz	o	pedido,	informando	a	quant idade	e	ele	será	adicionado	
à	bandeja	do	sistema.	Será	possível	adicionar	vários	itens	à	ba ndeja	antes	de	confirmar	os	
pedidos.		
Ao	 clicar	 na	 bandeja,	 após	 estes	 pedidos,	 o	 cliente	 poderá	 edit ar	 ou	 confirmá‐los.	 Ao	
confirmar	a	lista	de	pedidos,	es tes	serão	enviados	ao	setor	res ponsável	pelo	atendimento	e	
a	lista	retornará	vazia,	mas	adicionando	os	pedidos	na	conta	do	usuário.	
6.1	Os	requisitos	do	aplicativo	
Vamos	 raciocinar	 como	 funcionaria	 um	 cardápio	 eletrônico	 em	 sua	f o r m a 	d e 	e f e t u a r 	o s 	
pedidos.	 Omitiremos	 a	 funcionalidade	 de	 logar,	 pois	 somente	 ass im	 seria	 possível	
identificar	 a	 mesa	 que	 estará	 fazendo	 as	 solicitações,	 através	d o 	a p l i c a t i v o . 	I m a g i n e 	q u e 	
nosso	cardápio	já	terá	um	identificador	guardado	em	sua	sessão	(logado).		
Agora	vamos	avaliar	como	um	usuário	faria	seu	pedido	a	um	garçom	humano	após	verificar	
as	informações	do	cardápio.	Este	provavelmente	o	chamaria	e	ped iria	um	item	de	cada	vez	
e	com	sua	quantidade.	Por	exemplo:	 "Garçom!	Por	favor,	traga‐me	duas	cervejas	especiais	e	
um	filé	ao	molho	madeira".	 Ao	 final,	 o	 garçom	 encerra,	 confirmando	 o	 pedido	 e	 emitindo	
uma	anotação	ao	setor	responsável	por	despachá‐los.	
Em	nosso	caso,	vamos	imaginar	que,	ao	clicar	no	botão	 Pedir	do	detalhamento	de	cada	item,	
um	 modal	 para	 informar	 a	 quantidade	 se	 abrirá	 e,	 ao	 confirmar,	 ele	 entrará	 em	 nosso	
"carrinho	de	compras".	Para	confirmar	os	pedidos,	será	preciso	 clicar	no	"carrinho"	e,	em	
seguida,	enviar	todos	os	pedidos	para	o	servidor.		
T u d o 	i s t o 	j á 	f o i 	d e s e n h a d o 	e m 	n o s s o 	p r o t ó t i p o 	n o 	c a p í t u l o 	a n t e rior.	 Precisamos	 apenas	
definir	como	se	comportará	nosso	"carrinho".	Por	uma	decisão	co erente,	a	partir	de	agora,	
chamaremos	de	bandeja	e	ela	estará	posicionada	no	lado	superior	direito.	Veja	a	seguir	um	
protótipo	desta	função.	
	
	
	

## Página 64

	
Figura	6.1:	Bandeja	
	
Observe	que,	simulando	uma	bandeja,	o	ícone	no	canto	superior	d ireito	sugere	que	temos	
pedidos	e,	ao	clicar	neste	ícone,	a	tela	será	direcionada	para	 uma	listagem	das	solicitações.	
O	 próximo	 passo	 do	 fluxo	 é	 a	 confirmação	 do	 pedido	 para	 que	 sejam	 enviados	 ao	 setor	
responsável	(servidor)	e	limpeza	da	bandeja,	retornando	para	a	tela	inicial	do	aplicativo.	
Agora	 que	 temos	 os	 requisitos	 da 	 funcionalidade,	 vamos	 implementar.	 A	 proposta	 é	
continuarmos	 fiéis	 ao	 protótipo	 que	 o	 pessoal	 do	 design	n o s 	p a s s o u . 	E l e s 	v ã o 	a d o r a r 	e 	
agradecer.		
6.2	Uma	forma	de	guardar	nossa	sessão	
P a r a 	q u e 	n o s s o 	a p l i c a t i v o 	s i m u l e 	q u e 	o 	u s u á r i o 	s e 	e n c o n t r a 	l o g a d o 	c o m 	u m 	i d e n t i f i c a d o r 	
ú n i c o , 	v a m o s 	m a n t e r 	u m 	n ú m e r o 	q u e 	s e r á 	u s a d o 	p a r a 	l o c a l i z a r 	a 	mesa	 do	 pedido	 e	 uma	
lista	 que	 será	 nossa	 variável	 para	 guardar	 nossa	 bandeja.	 Para	isto,	 precisamos	 entender	
um	novo	conceito	em	AngularJS:	os	values.		


## Página 65

Toda	aplicação	web	construída	em	AngularJS	é	formada	por	objeto s	que	colaboram	entre	si	
para	 executar	 as	 funcionalidades .	 Estes	 objetos	 são	 criados	 e	 c onectados	 através	 do	
conceito	já	citado:	injeção	dos	serviços.		
O	AngularJS	dispõe	de	um	serviço	chamado	 Value	Recipe.	Vamos	utilizar	este	serviço	para	
guardar	os	valores	em	diversos	lugares	de	nosso	aplicativo.	Fazendo	analogia	com	qualquer	
linguagem	de	programação,	é	como	se	guardássemos	um	objeto	em	uma	variável	global	e,	
quando	necessário,	recuperássemos	estes	valores.		
Para	esta	finalidade,	usaremos	o	 value	para	guardar	nosso	identificador	da	mesa.	A	seguir,	
criamos	um	script	chamado	www/js/services/sessao.js.	
angular module('starter.controllers').value('Sessao',{ 
    mesaID: "123", 
    bandeja: [] 
}); 
Observe	 que,	 no	 lugar	 do	 controller	o u 	service ,	 instanciamos	 um	 value.	 Isto	 diz	 ao	
framework	q u e 	e s t e 	script	n a d a 	m a i s 	é 	d o 	q u e 	u m 	contêiner	 usado	 para	 guardar	 algumas	
constantes	 e	 variáveis.	 Agora	 é	 só	 importá‐lo	 no	 index.html	e 	e l e 	e s t a r á 	p r o n t o 	p a r a 	s e r 	
injetado	nos	controllers	da	aplicação.	Vamos	fazer	isto?	
... 
 
 <!-- Cabeçalho do index html --> 
 <script src="js/services/sessao.js"></script> 
 </head> 
... 
Prontinho!	Agora	você	já	pode	injetar	dentro	de	qualquer	 controller	ou	service.	Mas	qual	o	
mais	indicado	para	isto?	Veremos	a	seguir.	
6.3	Hora	de	injetar	o	value	
J á 	q u e 	c o n s t r u í m o s 	u m a 	s i m u l a ç ã o 	d a 	s e s s ã o 	e m 	n o s s a 	a p l i c a ç ã o , 	podemos	 analisar	 que,	
para	a	utilização	desses	valores	(mesa	e	bandeja),	devemos	deixá‐los	guardados	em	algum	
controller	que	esteja	o	tempo	todo	instanciado.	Queremos	dizer	com	isto	que,	dependendo	
da	configuração	de	sua	aplicação,	cada	vez	que	você	chama	uma	n ova	tela,	o	 controller	da	
tela	anterior	sai	da	memória	e	entra	o	novo	em	seu	lugar,	e	assim	sucessivamente.	
E	agora?!	Onde	guardarei	minha	sessão	já	que	isto	acontece?		
Vamos	 recapitular	 a	 seguinte	 estrutura	 de	 nossa	 pasta	 www/templates:	 temos	 nela	 alguns	
HTMLs	(como	por	exemplo,	 bebidas html	e	detalhe-item html)	e	nossa	aplicação	tem	um	layout	com	

## Página 66

um	menu	lateral.	Este	menu	é	mantido	pelo	menu html,	ou	seja,	este	é	o	template	onde	todas	as	
páginas	citadas	são	inseridas.		
S e g u i n d o 	a 	l i n h a 	d e s t e 	r a c i o c í n i o , 	v a m o s 	a o 	a r q u i v o 	www/js/app.js	e 	v e j a m o s 	o 	q u e 	e l e 	d i z 	
sobre	meu	menu html.	
... 
$stateProvider 
    .state('app', { 
    url: '/app', 
    abstract: true, 
    templateUrl: 'templates/menu html', 
    controller: 'AppCtrl' 
  }) 
... 
Observe	no	código	que	o	 controller	do	menu	é	o	 AppCtrl.	Com	isto,	conclui‐se	que	ele	sempre	
estará	 em	 memória	 durante	 a	 execução	 da	 nossa	 aplicação.	 Isso	 porque,	 mesmo	 quando	
você	carrega	telas	diferentes	em	sua	aplicação,	o	menu	lateral	estará	lá.	
A s s i m , 	i n j e t a r e m o s 	o 	script	 value,	 configurado	 anteriormente,	 em	 nosso	 controller.	 Para	
isto,	basta	declarar,	em	nosso	 www/js/controllers/controllers.js,	um	parâmetro	na	 function	chamado	
Sessao,	ou	seja,	a	instância	de	nosso	script	value.		
Além	 disto,	 devemos	 declarar	 uma	 variável	 de	 escopo	 ($scope) 	p a r a 	a 	b a n d e j a 	d e 	n o s s o 	
cardápio.	Portanto,	nosso	código	ficará	como	a	seguir:	
var app = angular.module('starter.controllers', []); 
 
app.controller('AppCtrl', function($scope, Sessao, $ionicModal, $timeout) { 
    $scope.bandeja = Sessao.bandeja; 
}); 
Observe	 que	 injetamos	 'Sessao'	b a s e a d o 	n o 	n o m e 	q u e 	v o c ê 	d e u 	à 	i n s t â n c i a 	d o 	Value	
Recipe.	Isto	é,	o	nome	que	o	AngularJS	disponibiliza	para	ser	injetad o	nos	controllers	e	
services	é	o	mesmo	que	você	declara	na	assinatura	do	objeto	'.value([nome_da_instância])'.	
Q u a s e 	t u d o 	p r o n t o , 	v a m o s 	a g o r a 	o b e d e c e r 	a o 	p e s s o a l 	d e 	d e s i g n 	q ue	 construiu	 nosso	
protótipo	e	inserir	um	ícone	com	um	contador	de	produtos,	que	t ambém	servirá	de	link	de	
direcionamento	para	a	listagem	de	pedidos	em	nossa	bandeja.		
Para	isto,	usaremos	dois	componentes	fornecidos	pelo	 framework:	um	botão	decorado	com	
um	ícone,	e	um	elemento	chamado	 badge,	que	nada	mais	é	do	que	um	contador	destacado	
de	vermelho	no	topo	da	aplicação.	

## Página 67

A 	s e g u i r , 	v e j a 	a 	m o d i f i c a ç ã o 	d e 	n o s s o 	www/templates/menu html	 com	 o	 código	 devidamente	
comentado:	
<ion-side-menus enable-menu-with-back-views="false"> 
  <ion-side-menu-content> 
    <ion-nav-bar class="bar-stable"> 
      <ion-nav-back-button> 
      </ion-nav-back-button> 
      <ion-nav-buttons side="left"> 
        <button class="button button-icon button-clear ion-navicon" menu-toggle="left"> 
        </button> 
      </ion-nav-buttons> 
 
      <!-- Modificação da posição do badge. A melhor prática diz que este trecho deve estar no arquivo style.css, 
      mas para efeito didático, colocamos dentro do html. --> 
      <style> 
        .button .badge { 
          top: -36px; 
        } 
      </style> 
      <ion-nav-buttons side="right"> 
        <!-- Botão que direcionará para a listagem de pedidos. --> 
        <button class="button button-icon button-clear ion-information-circled"> 
          <!-- Bagde com número de pedidos --> 
          <span ng-show="true" class="badge badge-assertive">{{bandeja.length}}</span> 
        </button>   
      </ion-nav-buttons> 
    </ion-nav-bar> 
    <ion-nav-view name="menuContent"></ion-nav-view> 
  </ion-side-menu-content> 
... 
P r e s t e 	a t e n ç ã o 	n o s 	c o m e n t á r i o s , 	o n d e 	c r i a m o s 	u m 	b o t ã o 	c o m 	a 	c l asse	 button-icon	e 	 ion-
information-circled.	Estes	componentes	criam	um	botão	com	o	ícone	de	um	círculo.	D entro	deste,	
foi	inserida	a	tag	 <span>	do	HTML	com	as	classes	 badge	e	 badge-assertive	(na	cor	vermelha)	para	
informar	o	número	de	pedidos.		
Não	 deixe	 de	 observar	 também	 que	 a	 quantidade	 está	 sendo	 constr u í d a 	a t r a v é s 	d o 	
tamanho	(length)	do	array	 bandeja	e	executando	o	 data‐binding	do	AngularJS	 {{bandeja.length}}.	O	
resultado	disto	pode	ser	visto	na	seguinte	figura.	
	
	

## Página 68

	
Figura	6.2:	Badge	da	bandeja	
	
6.4	Guardando	os	pedidos	
Bom	trabalho	até	aqui!	Construímos	nosso	layout	e	já	temos	onde 	guardar	nossos	pedidos.	
Agora	precisamos	construir	uma	função	que	executaremos	quando	o 	cliente	selecionar	um	
item	do	menu	e	clicar	no	botão	 Pedir.	Além	disto,	ele	deve	informar	a	quantidade	para	que	
seja	calculado	o	valor	real	em	sua	conta,	e	os	itens	sejam	fornecidos	de	forma	correta.	
Lembra	 da	 tela	 de	 detalhamento	 de	 pedidos	 que	 foi	 planejada	 com 	o 	p r o t ó t i p o 	e 	
posteriormente	 construída?	 Pois	 bem!	 No	 capítulo	 anterior,	 apre ndemos	 como	 passar	
p a r â m e t r o s 	e n t r e 	a s 	t e l a s , 	c o n s t r u í m o s 	n o s s a 	t e l a 	g e n é r i c a 	d e 	detalhes	 dos	 itens	 através	
deste	parâmetro,	mas	deixamos	de	lado	a	ação	do	botão	Pedir.		
Não	tem	problema!	Vamos	construir	aqui	esta	ação	baseada	no	pro tótipo	que	nos	emitirá	
um	 modal	 para	 informar	 a	 quantidade	 e	 confirmar	 o	 pedido.	 Posteriormente,	 assim	 que	
confirmado	 o	 pedido,	 ele	 será	 inserido	 na	 bandeja	 e	 terá	 um	 comportamento	 similar	 ao	
c a r r i n h o 	d e 	c o m p r a s 	d e 	q u a l q u e r 	s i s t e m a 	d e 	e‐commerce,	 conforme	 já	 comparamos	
anteriormente	neste	capítulo.	
Agora	vamos	lembrar	de	uma	máxima	que	escutamos	desde	pequenos: 	"tenho	uma	boa	e	
u m a 	m á 	n o t í c i a 	p a r a 	v o c ê . 	Q u a l 	v o c ê 	q u e r 	l e r 	p r i m e i r o ? " . 	N ã o 	f ugindo	 à	 regra,	 o	 leitor	
provavelmente	 pensou:	 "A	 má	 primeiro,	 por	 favor!".	 Pois	 bem!	 Vamos	 seguir	 nesta	
sequência.	
A 	m á 	é 	q u e 	o 	Ionic	n ã o 	o f e r e c e 	n a t i v a m e n t e 	u m 	c o m p o n e n t e 	q u e 	p r e c i s a m o s 	u s a r : 	o 	
number	 picker. 	E s t e 	t e m 	a 	c a r a c t e r í s t i c a 	d e 	u m 	input	 de	 números	 através	 de	 botões	
incrementando/decrementando	 estes	 valores,	 conforme	 visto	 em	 no sso	 protótipo.	 Ao	
menos	em	sua	versão	1,	o	framework	não	nos	dá	isso	prontinho	para	utilizar.	
	
Figura	6.3:	Number	Picker	
	


## Página 69

	
Agora	vamos	ler	a	boa:	utilizaremos	um	componente	de	terceiros, 	instalando‐o	através	do	
comando	 bower.	 Para	 entendermos	 o	 que	 é	 este	 comando,	 precisamos	 relembrar	 d a	
instalação	 de	 nosso	 ambiente	 no	 primeiro	 capítulo,	 onde	 usamos	 o	 comando	 npm install -g 
cordova ionic.	
Tanto	 o	 bower	( https://bower.io/)	 quanto	 o	 npm	( https://www.npmjs.com/)	 são	
gerenciadores	de	pacotes	JavaScript,	em	que	você	pode	reutilizar,	compartilhar	e	encontrar	
componentes	 de	 outros	 desenvolvedores.	 É	 uma	 espécie	 de	 reposit ó r i o . 	P a r a 	q u e 	v o c ê 	
possa	utilizar	o	 bower,	será	necessário	instalá‐lo	pelo	 npm	com	o	seguinte	comando	 npm install -g 
bower.	Após	a	instalação,	execute	também:	
bower install angular-number-picker --save 
Viu?!	 Além	 da	 boa	 e	 da	 má	 notícia,	 existe	 uma	 outra:	 a	 excelente ! 	O 	c o m p o n e n t e 	s e r á 	
instalado	com	apenas	um	comando.		
Observe	a	instalação	e,	quando	finalizar,	o	seu	componente	estará	prontinho	para	ser	usado	
em	 www/lib/angular-number-picker.	 Agora	 vamos	 importá‐lo	 em	 nosso	 projeto	 no	 arquivo	
www/index html.	Para	isto,	insira	o	código	do	script	no	index html,	como	tem	feito	até	aqui:	
... 
 <script type="text/javascript" src="lib/angular-number-picker/dist/angular-number-picker min.js"></script> 
... 
Chegou	a	vez	de	injetarmos	este	componente	em	 www/js/app.js,	para	que	ele	seja	utilizado	em	
toda	aplicação.	Com	isto,	o	módulo	ficará	com	os	seguintes	parâmetros:	
angular module('starter',  
    ['ionic',  
        'starter.controllers', 
            'ngNumberPicker']) 
... 
A g o r a 	q u e 	v o c ê 	j á 	t e m 	n o ç ã o 	d o 	q u e 	v a i 	c o n s t r u i r , 	s u g i r o 	q u e 	v olte	 ao	 arquivo	
www/templates/detalhe-item htmle	localize	nosso	botão	 Pedir.	Observe	que	ele	está	lá,	sem	vida,	sem	
ação.	Vamos	dar	a	ele	vida	e	ação,	pois	cor	ele	já	tem.		
Precisamos	construir	um	modal	que	ficará	escondidinho	(hide)	até	o	momento	que	o	usuário	
clicar	 em	 Pedir,	 conforme	 visto	 no	 protótipo	 do	 capítulo	 anterior.	 Para	 isto,	 adicione	 o	
seguinte	código	antes	do	botão:	
<ion-view> 
  <ion-content> 
  <!-- Modal --> 

## Página 70

    <script id="my-modal html" type="text/ng-template"> 
      <ion-modal-view> 
        <ion-content> 
        <div class="card"> 
          <div class="item txt-centralizado"> 
            <p>Informe a quantidade</p> 
            <p>e confirme este pedido.</p> 
            <br /> 
            <h2>{{item nome}}</h2> 
            <p><h-number value="input.quant" min="1" max="100" step="1"></h-number></p> 
          </div> 
          <div class="margem-imagem"></div> 
        </div> 
         <div class="bar bar-footer"> 
          <div class="button-bar"> 
           <button class="button icon-right ion-checkmark button-positive"  ng-click="pedir()">Pedir</button> 
           <button class="button icon-right ion-checkmark button-assertive"  ng-click="fechaModal()">Cancelar</button> 
          </div> 
        </div> 
        </ion-content> 
      </ion-modal-view> 
    </script> 
    <!-- Fim/Modal --> 
    ... 
Observe	que,	mesmo	antes	de	construirmos	as	funções	para	fechar 	o	modal	e	confirmar	o	
pedido	 ‐	 fechaModal()	e 	 pedir()	‐ , 	j á 	e s t a m o s 	p r e v e n d o 	e 	c o l o c a n d o ‐ a s 	n o 	ng-click	 dos	 botões.	
Analise	 o	 código	 e	 verifique	 também	 que	 criamos	 uma	 div	c o m 	a 	class	 button-bar,	 na	 qual	
teremos	o	seguinte	efeito:	
	
Figura	6.4:	Button	bar	
	
Criamos	 assim	 uma	 barra	 com	 dois	 botões	 alinhados.	 A	 class	 button-assertive	e 	 button-positive	
determinam	as	cores	dos	botões.		
Analisando	mais	o	código,	note	q ue	reutilizamos	uma	classe	cria da	no	início	de	nosso	livro	
(a	txt-centralizado)	para	centralizar	o	conteúdo	de	nosso	modal	na	 divque	encapsula	o	texto	e	o	
number	picker.	Além	disto,	veja	o	uso	do	componente	que	baixamos	com	o	 bower.	O	<h-number>	
recebe	 um	value	 que	 deve	 estar	 declarado	 em	 nosso	controller. 	V a m o s 	v e r 	e s t e 	v a l o r 	m a i s 	
adiante	quando	o	codificarmos.		


## Página 71

Refrescando	 nossa	 memória,	 lembre‐se	 de	 que	 o	controller	d e s t e 	template	é 	o 	DetalharCtrl,	
declarado	no	arquivo	 www/js/detalhar-controller.js.	Abra‐o,	pois	é	nele	que	vamos	atuar	a	partir	de	
agora.	
Vamos	 construir	 uma	 função	 para	 fazer	 a	 chamada	 através	 de	 noss o	 botão.	 Para	 isto,	
adicionaremos	as	seguintes	funções	de	nosso	modal:	
... 
$scope.input = {}; 
$scope.input.quant = 0; 
 
$ionicModal fromTemplateUrl('my-modal.html', { 
        scope: $scope, 
        animation: 'slide-in-up' 
    }).then(function(m){ 
        $scope modal = m; 
    }); 
 
    $scope.abreModal = function(){ 
        $scope modal.show();         
    } 
 
    $scope fechaModal = function(){ 
        $scope modal hide();         
    } 
... 
Agora	 observe	 que	 estamos	 usando 	u m 	o b j e t o 	c o m o 	r e f e r ê n c i a 	p a r a 	o 	n o s s o 	m o d a l : 	
$ionicModal.	Nele	inserimos	o	template	construído	em	 www/templates/detalhe-item html,	e	informamos	
parâmetros	como	animação	( animation)	abrindo	a	variável	de	escopo	( $scope)	do	AngularJS	
a	partir	do	topo	da	aplicação.		
Além	 disto,	 abriremos	 o	 modal	 através	 de	 $scope modal.show()	 e	 fecharemos	 através	 de	
$scope modal hide().	 Mas	 lembre‐se:	 para	 que	 tudo	 seja	 executado	 corretamente,	 precisaremos	
ter	o	objeto	$ionicModal	também	corretamente	inserido	no	contexto.		
Vamos	 fazer	 agora	 um	 exercício	 de	 memória?	 Qual	 recurso	 nos	 per mite	 inserir	 este	
componente	 no	 contexto	 da	 aplicação?	 Claro!	 Através	 da	 injeção.	E u 	s a b i a 	q u e 	v o c ê 	s e 	
lembraria.	Também	tenho	certeza	de	que	você	se	antecipou	e	a	as sinatura	de	seu	controller	
ficou	assim:	
... 
app.controller('DetalharCtrl',  
    function($scope,  
                $stateParams,  
                    CardapioServices,  

## Página 72

                        Sessao, 
                            $ionicModal){ 
... 
Observe	também	o	início	do	código	onde	declaramos	o	$scope.input.quant	para	que	seja	utilizado	
pelo	componente	<h-number>,	por	meio	do	parâmetro	 value="input.quant".	Desta	forma,	estaremos	
guardando	o	valor	para	inserir	em	nossa	bandeja.	
Tudo	pronto,	faça	um	teste	e	verá	que	o	modal	abrirá,	porém	o	b otão	Pedir	não	confirmará	
ainda	o	pedido.	O	botão	de	cancelar	fechará	o	modal	e	o	usuário	voltará	à	tela	do	produto.	
Vamos	 então	 construir	 nossa	 função	 para	 adicionar	 o	 pedido	 na	 b andeja.	 Para	 isto,	
p r e c i s a m o s 	f a z e r 	u m a 	f u n ç ã o 	q u e 	a d i c i o n e 	o 	i t e m 	e m 	u m a 	l i s t a 	c om	 2	 parâmetros	
importantes:	o	objeto	item	e	a	quantidade	deste	item.	
Após	este	processo,	o	pedido	deve	ser	inserido	na	bandeja	e	o	m odal	deverá	ser	fechado,	
retornando	à	tela	anterior.	Vamos	ver	como	ficará	esta	função	no	www/js/detalhar-controller.js?	
... 
$scope.inserirPedido = function(){ 
    Sessao.bandeja.push({item: $scope.item, quantidade : $scope.input.quant}); 
    $scope modal hide(); 
    $scope.input.quant = 1; 
} 
Verifique	 no	 código	 a	 utilização	 da	 função	 push	d o 	J a v a S c r i p t 	q u e 	i n s e r e 	o 	i t e m 	e 	a 	
quantidade	que	está	no	 $scope.	Colocamos	a	quantidade	com	um	valor	inicial	igual	a	1,	pois	
assim	ficará	quando	voltarmos	a	abrir	este	modal.	Faça	isto	tam bém	na	função	 fechaModal(),	
pois	 impede	 do	 usuário	 aumentar	 a	 quantidade	 e	 desistir	 no	 meio	 do	 processo,	 assim	
cancelando,	e	retornar	com	o	valor	guardado.	
Bem!	Tudo	prontinho,	agora	é	só	testar	e	observar	que	o	seu	aplicativo	já	está	inserindo	o	
item	na	bandeja,	pois	o	ícone	já	incrementa	a	quantidade	no	topo	da	aplicação,	como	ilustra	
a	figura	a	seguir:	

## Página 73

	
Figura	6.5:	Bandeja	incrementando	
	
		


## Página 74

	
6.5	Conclusão	
A q u i 	v i m o s 	c o m o 	c r i a r 	u m 	m o d a l 	p a r a 	i n s e r i r 	u m 	o b j e t o 	e m 	u m 	a r ray	 JavaScript,	
aproveitando	 o	 valor	 (quantidade)	 informado	 nele,	 e	 com	 isto	 gu ardá‐lo	 na	 sessão	 do	
aplicativo.	 Vimos	 também	 como	 instalar	 um	 componente	 de	 terceir o s 	a t r a v é s 	d o 	
gerenciador	de	pacotes	JavaScript	bower	e	como	usá‐lo.		
No	 próximo	 capítulo,	 aprenderemos	 a	 gerenciar	 os	 pedidos	 da	 ban deja,	 excluindo,	
alterando	quantidades	e	visualizando	seus	valores.		
6.6	Para	saber	mais	
	
1. Bower	–	https://bower.io	
2. Npm	–	https://www.npmjs.com	
3. Angular	Number	Picker	–	
https://github.com/leftstick/angular‐number‐picker	
 

## Página 75

CAPÍTULO	7	
A	bandeja	
Neste	 capítulo,	 vamos	 planejar	 e	 implementar	 a	 visualização	 da	 bandeja	 com	 a	
possibilidade	 de	 editar	 os	 itens	 e	 também	 confirmar	 o	 pedido	 para	 que	 seja	 enviado	 ao	
setor	responsável	por	receber	e	encaminhar	ao	garçom.	
V i m o s 	n o 	c a p í t u l o 	a n t e r i o r 	q u e 	a 	b a n d e j a 	é 	s i m i l a r 	a o 	c a r r i n h o 	d e 	c o m p r a s 	d o s 	e‐
commerces.	 Portanto,	 o	 processo	 consiste	 em	 inserir	 pedidos	 dentro	 deste	c a r r i n h o , 	e m 	
nosso	 caso	 na	 bandeja,	 e	 posteriormente	 ser	 possível	 visualizar	e 	e d i t a r 	a s 	q u a n t i d a d e s 	
destes	itens.	
P a r a 	i s t o , 	v a m o s 	i m a g i n a r 	u m a 	t e l a 	c o m 	u m a 	l i s t a 	o n d e 	t e r e m o s 	a	 quantidade	 pedida,	 o	
item	e	um	valor	‐	produto	da	multiplicação	da	quantidade	pelo	p reço.	Usaremos	um	novo	
modal	que	abrirá	com	o	toque	no	botão	que	representará	nossa	ba ndeja,	no	topo	superior	
direito	 do	 aplicativo.	 Nele	 implementaremos	 ações	 para	 a	 lista	 de	 itens.	 Vamos	 ao	
trabalho?!	
7.1	Elementos	do	modal	
Como	já	vimos	no	capítulo	anterior,	precisamos	"esconder"	o	mod al	em	algum	template	e	
mostrá‐lo	 assim	 que	 o	 usuário	 executar	 determinada	 função	 respon s á v e l 	p o r 	a b r i ‐ l o . 	O 	
modal	 também	 será	 um	 template,	 ou	 seja,	 um	 template	 escondido	 ( inserido)	 em	 um	
template.	Parece	confuso?!		
Na	prática,	veremos	como	isto	funciona.	Existem	várias	formas	d e	construí‐lo,	inclusive	em	
arquivos	separados	para	melhor	r eaproveitamento.	Porém,	em	nosso	caso,	faremos	dentro	
do	 www/templates/menu.html, 	p o i s 	e s t e 	m o d a l 	s e r á 	m u i t o 	e s p e c í f i c o , 	e 	p r o v a v e l m e n t e 	n ã o 	s eria	
reutilizado	 em	 nossa	 aplicação.	 Até	 porque,	 dentro	 do	 template	 d e 	m e n u , 	e l e 	e s t a r á 	
disponível	para	abertura	em	qualquer	cenário.	Basta	tocar	no	bo tão	da	bandeja	quando	ele	
tiver	um	pedido	ou	mais.	
Pensando	 no	 protótipo	 da	 bandeja 	a p r e s e n t a d o 	n o 	c a p í t u l o 	a n t e r ior,	 teríamos	 este	
presentinho	do	pessoal	do	design:	

## Página 76

	
Figura	7.1:	Protótipo	
	
	


## Página 77

Observe	a	lista	na	qual	cada	ele mento	tem	uma	quantidade,	que	foi	determinada	no	modal	
aberto	 pela	 ação	Pedir.	 Lembra‐se	 dela?	 Ao	 efetuar	 um	pedido,	 o	 usuário	 informa	 quantos	
itens	devem	conter	nele	através	de	um	 number	picker.	Além	disto,	a	lista	traz	um	título	do	
item	e	o	valor	deste	pedido,	ou	seja,	uma	multiplicação	do	preço	do	item	com	a	quantidade.	
L o g o 	a b a i x o , 	t e r e m o s 	4 	b o t õ e s 	p a r a 	a s 	a ç õ e s : 	Enviar	a 	b a n d e j a 	p a r a 	e f e t u a r 	o 	p e d i d o , 	
Alterar	 o	 pedido	 selecionado,	 Excluir	 um	 item	 selecionado	 da	 bandeja	 sem	 efetuar	 o	
pedido	 e	 Voltar	 fechando	 o	 modal	 e	 permanecendo	 os	 pedidos	 na	 bandeja.	 Mas	 com o	
faremos	isto	na	prática	utilizando	o	Ionic?	No	papel,	está	fácil,	não	é,	pessoal	do	design?	
A p r o v e i t a n d o 	p a r a 	f i l o s o f a r 	u m 	p o u c o , 	t o d o 	a p r e n d i z a d o 	t e m 	s u a 	origem	 na	 ignorância.	
Não	sabemos	ainda	como	construir	este	modal,	mas	pode	ter	certe za	de	que,	ao	final	deste	
c a p í t u l o , 	v o c ê 	v a i 	o l h a r 	p a r a 	t r á s 	e 	p e n s a r 	q u e 	v a l e u 	a 	p e n a . 	A	 partir	 daí,	 a	 ignorância	
passou	 a	 ser	 aprendizado,	 e	 isto	 provavelmente	 vai	 acrescentar	 muito	 em	 sua	 vida	
profissional.	
Para	 início	 de	 conversa,	 vamos	 aos	 nossos	 componentes	 prontos	 e,	 como	 diria	 meu	 avô,	
"mastigados"	 do	 framework.	 O	 arquivo	 www/templates/menu.html,	 a	 partir	 da	 tag	 </ion-side-menu>,	
ficará	assim:	
<!-- Modal --> 
    <script id="bandeja html" type="text/ng-template"> 
      <ion-modal-view> 
        <ion-content> 
        <div class="card"> 
          <div class="item txt-centralizado"> 
          <!-- Colunas --> 
            <div class="row"> 
                <div class="col"> 
                  Quantidade 
                </div> 
                <div class="col"> 
                  Item 
                </div> 
                <div class="col"> 
                  Valor 
                </div> 
            </div> 
            <!-- Loop em Lista --> 
            <ion-list ng-repeat="it in bandeja"> 
              <!-- Radio --> 
              <ion-radio> 
                 <div class="row"> 
                  <div class="col"> 
                    {{it.quantidade}} 

## Página 78

                  </div> 
                  <div class="col"> 
                    {{it.item nome}} 
                  </div> 
                  <div class="col"> 
                    {{it.valor}} 
                  </div> 
                  </div> 
              </ion-radio> 
            </ion-list> 
            <br /> 
          </div> 
          <div class="margem-imagem"></div> 
        </div> 
        <div class="bar bar-footer"> 
          <div class="button-bar"> 
           <button class="button  button-positive"><i class="ion-ios-checkmark-outline"></i></button> 
           <button class="button  button-dark"><i class="ion-edit"></i></button> 
           <button class="button"><i class="ion-ios-trash-outline"></i></button> 
           <button class="button  button-assertive"  ng-click="fechaModal()"><i class="ion-ios-undo-outline"></i></button> 
          </div> 
        </div> 
        </ion-content> 
      </ion-modal-view> 
    </script> 
    <!-- Fim/Modal --> 
Não	 se	 desespere!	 Como	 já	 foi	 dito,	 estes	 componentes	 foram	 fei tos	 para	 você,	
desenvolvedor	de	aplicativos,	utilizar	à	vontade.	Basta	entendê ‐los	e,	por	isso,	agora	vamos	
explicar.		
O	 modal	 contém	 uma	 lista	 que	 será	 exibida	 com	 o	 componente	<ion-list>.	 O	loop	 na	 lista	 é	
feito	através	do	atributo	 ng-repeat	deste	componente.	Observe	que	fizemos	um	loop 	em	bandeja	
que	 estará	 definido	 no	controller,	 atribuindo	 cada	 elemento	 deste	array	 em	 uma	 variável	
chamada	 it.	 De	 cada	 elemento,	 daremos	 um	 print	a t r a v é s 	d a s 	c h a v e s 	d u p l a s 	({{}}),	 que	
vimos	em	capítulos	anteriores,	o	qual	utiliza	o	 data‐binding	do	AngularJS	para	sincronizar	
as	atualizações	desta	variável.	
Temos	também	um	componente	novo	nesta	iteração	e	acima	dela,	que	são	as	colunas	de	um	
grid.	Observe	a	seguir	como	se	comportam	essas	grids	responsivas	no	Ionic.	
	

## Página 79

	
Figura	7.2:	Sistema	de	Grids	
	
Não	 vamos	 nos	 aprofundar	 em	 grids	 do	 framework,	 mas	 o	 importante	 é	 saber	 que	 elas	
e x i s t e m . 	A 	f o r m a 	m a i s 	s i m p l e s 	d e 	o r g a n i z a r 	c o n t e ú d o s 	c o m 	e l a 	é 	construindo	 uma	 linha	
com	a	class css row	e	inserir	colunas	com	a	class css col.		
Para	 aprofundar	 mais	 sobre	 as	 grids,	 a	 documentação	 do	 framework	é 	v a s t a , 	e m 	
https://ionicframework.com/docs/components/#grid.	 Por	 enquanto,	 vamos	 focar	 apenas	
nesta	forma	simples	de	organizar	os	componentes.	


## Página 80

U m 	o u t r o 	c o m p o n e n t e 	n o v o 	é 	o 	radio button	e 	e l e 	f o i 	d e c l a r a d o 	e m 	<ion-radio>. 	C a d a 	l i n h a 	d o 	
objeto	bandeja	estará	envolvida	em	um	 radio,	ou	seja,	uma	seleção	única.	Isto	foi	planejado	por	
causa	 da	 funcionalidade	 de	 editar	 o	 item	 pedido,	 alterando	 sua	 quantidade.	 O	 usuário	
selecionará	um	item	para	edição	e	acionará	o	botão	 Alterar	para	que	seja	possível	efetuar,	de	
fato,	a	edição	do	item	selecionado.	
O	 último	 elemento	 novo	 em	 nossa	 codificação	 é	 o	 <i>,	 dentro	 de	 cada	 tag	 <button>.	 Ela	
determina	que	o	botão	tenha	uma	imagem,	e	não	um	label	como	de	 praxe.	A	imagem	será	
declarada	 por	 cada	class.	 São	 elas:	ion-ios-checkmark-outline, ion-edit, ion-ios-trash-outline e ion-ios-undo-outline.	
O	 próprio	 framework	d i s p o n i b i l i z a 	u m a 	g r a n d e 	q u a n t i d a d e 	d e 	í c o n e s 	q u e 	p o d e m 	s e r 	
pesquisados	e	utilizados,	em	http://ionicons.com.	
B e m ! 	A t é 	a q u i , 	s ó 	v i m o s 	c o m o 	c r i a r 	n o s s o 	m o d a l , 	m a s 	a i n d a 	n ã o 	o	 chamamos	 em	 botão	
algum,	 entretanto	 já	 sabemos	 onde	 vamos	 executar	 esta	 ação,	 não	é 	m e s m o ? ! 	P a r a 	i s t o , 	
vamos	criar	uma	função	JavaScript	em	nosso	www/js/controllers.js.		
Lembre‐se	 de	 que	 este	controller	 contém	 um	 objeto	 simulando	 nossa	 sessão,	 usado	 para	
guardar	os	itens	pedidos	em	nossa	bandeja	( Sessao.bandeja).	Abaixo	dele,	vamos	inserir	nosso	
código	para	declarar,	abrir	e	fechar	o	modal	do	arquivo	www/templates/menu html.	
... 
$ionicModal fromTemplateUrl('bandeja.html', { 
        scope: $scope, 
        animation: 'slide-in-up' 
    }).then(function(m){ 
        $scope modal = m; 
    }); 
 
    $scope.abreModal = function(){ 
        $scope modal.show();         
    } 
 
    $scope fechaModal = function(){ 
        $scope modal hide();     
    } 
... 
Observe	 que	 o	 template	 do	 modal	 é	 o	 bandeja html,	 o	 mesmo	 declarado	 na	 tag	 <script 
id="bandeja html" type="text/ng-template"> 	d o 	 www/templates/menu html.	 Pronto!	 Agora	 só	 precisamos	
colocar	a	ação	de	exibi‐lo.	
Vale	lembrar	que	o	ícone	representante	da	bandeja	está	envolvid o	por	um	botão,	até	então	
sem	ação.	É	justamente	nele	que	faremos	a	ação	de	abrir	o	modal,	através	da	diretiva	ng-click,	
já	vista	antes.		

## Página 81

Ainda	assim,	vamos	explicar	melhor	o	que	são	essas	diretivas.	E las	são	extensões	do	HTML,	
providas	pelo	 framework	AngularJS.	Elas	permitem	que	tenhamos	novos	comportamentos,	
ou	 seja,	 o	 desenvolvedor	 poderá	 construir	 suas	 diretivas	 ou	 utilizar	 as	 já	 existentes	 do	
AngularJS.	Veja	a	seguir	o	ícone	da	bandeja	sendo	envolvido	por	um	<button>:	
... 
    <!-- Botão que direcionará para a listagem de pedidos. --> 
    <button class="button button-icon button-clear ion-information-circled"> 
      <!-- Bagde com número de pedidos --> 
      <span ng-show="true" class="badge badge-assertive">{{bandeja.length}}</span> 
    </button> 
... 
Nele	é	possível	observar	duas	ca racterísticas	do	AngularJS:	uma 	diretiva	ng-show	e	um	 data‐
binding	através	do	 {{bandeja.length}}.	O	 data‐binding	estará	sendo	atualizado	constantemente,	
de	 acordo	 com	 a	 quantidade	 de	 itens	 inseridos	 no	array bandeja.	 Inicialmente,	 estará	 com	 0	
( z e r o ) 	e 	s e r á 	i n c r e m e n t a d o 	d e 	a c o r d o 	c o m 	a 	a ç ã o 	d o 	u s u á r i o 	a o 	inserir	 ou	 remover	 itens	
(decrementando).	
Agora	 vamos	 usar	 a	 diretiva	ng-click,	 que	 tem	 o	 comportamento	 parecido	 com	 o	 nativo	 do	
onclick	 do	 HTML.	 Daremos	 a	 ela	 a	 função	 para	 abrir	 o	 modal	 toda	 vez	 que	 for	clicada.	 Esta	
função	já	foi	criada	anteriormente	neste	capítulo.	Lembra‐se	dela?	
... 
$scope.abreModal = function(){ 
        $scope modal.show();         
    } 
... 
E n f i m , 	n o s s o 	b o t ã o 	p a s s a r á 	a 	t e r 	u m a 	d i r e t i v a 	ng-click,	 chamando	 esta	 função	 da	 seguinte	
forma:	
... 
 
    <!-- Botão que direcionará para a listagem de pedidos. --> 
    <button class="button button-icon button-clear ion-information-circled" ng-click="abreModal()"> 
    <!-- Bagde com número de pedidos --> 
 
... 
Clique	e	observe	o	comportamento.	Consegue	prever	um	problema	a qui?	Quando	a	"Equipe	
de	Testes"	começarem	a	testar	seu	aplicativo,	eles	vão	devolver 	um	 bug	e	você	não	terá	o	
d i r e i t o 	d e 	f i c a r 	b r a v o 	c o m 	e l e s . 	O 	m o d a l 	a b r e , 	m e s m o 	s e m 	e x i s t ir	 pedido	 na	 bandeja.	 A	
parte	boa	desse	 bug	é	que	você	resolverá	em	1	minuto	e	poderá	ir	para	a	copa	tomar 	um	
café	quentinho	enquanto	relaxa	um	pouco.	Vamos	à	solução?	

## Página 82

... 
$scope.abreModal = function(){ 
        //Testa se existe pelo menos um item na bandeja. 
        if($scope.bandeja.length > 0) 
            $scope modal.show();         
} 
... 
S i m p l e s m e n t e 	i s t o ! 	A o 	e x e c u t a r 	a 	f u n ç ã o , 	v a m o s 	t e s t a r 	s e 	e x i s t e	 pelo	 menos	 um	 pedido	
inserido	 na	 bandeja	 através	 do	 tamanho	 do	 array.	 Se	 não	 existe,	a 	f u n ç ã o 	n ã o 	e x e c u t a r á 	
nada.	Caso	contrário,	a	bandeja	será	aberta	através	da	função	show	do	modal.		
Com	 esta	 mesma	 lógica	 e	 linha	 de	 raciocínio,	 poderemos	 construir 	u m 	o u t r o 	m o d a l 	o u 	
apenas	um	aviso	na	tela	do	aplicativo	informando	que	não	há	ite m	na	bandeja.	Mas	isso	fica	
a	critério	do	leitor.	Não	faremos	esta	funcionalidade	neste	livro	pelo	simples	motivo	de	que	
vamos	apenas	replicar	códigos	já	vistos.	
A o 	e x e c u t a r 	a 	f u n ç ã o 	e 	a b r i r 	o 	m o d a l , 	v o c ê 	p o d e r á 	o b s e r v a r 	q u e 	só	 estamos	 exibindo	 a	
quantidade	de	item	que	foi	informada	no	componente	 number	picker	e	a	descrição	do	item.	
Precisamos	 calcular	 o	 valor	 total	 de	 cada	 pedido,	 multiplicando	a 	q u a n t i d a d e 	p e l o 	p r e ç o . 	
Entretanto,	temos	um	problema	em	nosso	planejamento	inicial.		
Ao	 pensarmos	 em	 nosso	mock	c r i a d o 	n o 	s e r v i ç o 	d e 	d e t a l h a m e n t o 	d o s 	i t e n s 	n o 	c a p í t u l o 	
Detalhando	os	itens,	 esquecemos	 de	 um	 pequeno	 detalh e , 	m a s 	s a i b a m 	q u e 	f o i 	p r o p o s i tal.	
Utilizamos	para	o	preço	do	item	um	valor	do	tipo	 VARCHAR,	ou	string,	como	quiser	chamar	o	
nosso	valor	alfanumérico.	Isto	aconteceu	porque	pensamos	mais	n a	forma	como	este	valor	
seria	apresentado	em	tela	do	que	representado	em	um	banco	de	dados,	por	exemplo.		
Com	 isto,	 o	 JavaScript,	 que	 é	 uma	 linguagem	 de	 programação	 não	 tipada,	 faz	 a	 variável	
a s s u m i r 	u m 	v a l o r 	d o 	t i p o 	string,	 o	 que	 torna	 impossível	 multiplicá‐lo	 por	 um	 número	 do	
tipo	number.	Para	saber	mais	sobre	tipos	em	JavaScript,	consulte	a	seção	 Para	saber	mais	no	
final	deste	capítulo.		
Entretanto,	o	que	acontece	aqui	é	que	determinamos	o	preço	do	i tem	através	de	aspas.	Isto	
faz	 com	 que	 o	 JavaScript	 interprete	 em	 tempo	 de	 execução	 que	 nossa	 variável	 é	 do	 tipo	
string.	
7.2	Vamos	ter	retrabalho	
Tendo	o	problema	em	vista,	assumindo	nosso	erro	de	planejamento 	com	nosso	Gerente	de	
Projetos,	vamos	corrigir	o	serviço	para	que	nos	retorne	o	valor	em	form ato	numérico.	Para	
isto,	altere‐os	da	seguinte	forma,	no	arquivo	www/js/cardapio-services.js:	

## Página 83

... 
    //Mock Bebidas 
    var bebidas = [ 
        {'nome': 'Vinho Tinto Brasil', 'id' : 1, 'preco' : 40.00, 
            'imagem' : 'img/garrafas.png', 'descricao':'Vinho tinto seco, da região Sul do país.'}, 
        {'nome': 'Cerveja Especial', 'id' : 2, 'preco' : 23.00, 
            'imagem' : 'img/cerveja.png', 'descricao':'Cerveja elaborada artesanalmente com um toque frutado.'}, 
        {'nome': 'Whisky 18 anos', 'id' : 3, 'preco' : 200.00, 
        'imagem' : 'img/whisky.png', 'descricao':'Whisky de fabricação Russa.' } 
    ]; 
... 
Retiramos	a	vírgula	do	preço	e	também	as	aspas.	Agora	a	linguag em	JavaScript	assume	que	
este	valor	é	um	number,	e	assim	você	poderá	multiplicá‐lo	com	qualquer	número.	Veja	q ue	só	
fizemos	a	correção	no	 array	de	bebidas,	ficando	a	critério	do	leitor	a	correção	nos	outros 	
itens.		
Agora	é	hora	do	cálculo	do	valor	total.	Vamos	lá?	Voltando	ao	a rquivo	www/js/detalhar-controller.js,	
na	função	inserirPedido()	criada	no	capítulo	Fazendo	pedidos,	vamos	fazer	o	cálculo	na	linha	que	
adiciona	o	item	no	array	através	da	função	push()	do	JavaScript.		
... 
Sessao.bandeja.push({item: $scope.item, quantidade : $scope.input.quant, valor: $scope.input.quant*$scope.item.preco}); 
... 
Todo	 desenvolvimento	 de	 sistemas	 está	 inserido	 em	 um	 perigo	 temido	 pelos	 analistas	 e	
gestores:	o	retrabalho	causado	por	um	impacto	em	alguma	falha	n a	fase	de	planejamento.	
Com	 o	 nosso	 aplicativo,	 aconteceu	 exatamente	 isto.	 Corrigimos	 u m	 problema,	 mas	
inserimos	 outros,	 pois	 esperávam o s 	q u e 	o 	p r e ç o 	d o 	p r o d u t o 	c h e g asse,	 quando	
consultássemos	o	serviço,	no	formato	"redondinho"	para	exibição	em	tela.	
Entretanto,	de	acordo	com	a	necessidade,	vimos	que	é	preciso	um 	retorno	numérico	e	cru	
para	 que	 sejam	 efetuadas	 operações	 matemáticas	 nele.	 Além	 disto,	 o	 preço	 deve	
representar	o	tipo	de	dados	que	ele	realmente	é:	number.	
O 	p r o b l e m a 	q u e 	i n s e r i m o s 	é 	v i s í v e l 	q u a n d o 	s e 	d i r e c i o n a 	p a r a 	q u alquer	 tela	 que	 exibe	 o	
preço	 do	 produto.	 Este	 estará	 no	 seguinte	 formato:	 R$	 99.999,	 ou	 seja,	 com	 um	 ponto	
representando	um	valor	double	em	vez	do	formato	de	nossa	moeda,	o	Real,	com	a	vírgula.		
C a l m a ! 	N ã o 	s e 	d e s e s p e r e , 	p o i s 	o 	p e s s o a l 	q u e 	d e s e n v o l v e u 	o 	J a v a S c r i p t 	p e n s o u 	n i s s o 	e 	
resolveu	de	uma	forma	bem	discreta	e	eficiente	este	problema.	B asta	transformar	o	valor,	
e m 	t o d a s 	a s 	t e l a s 	e m 	q u e 	s e 	q u e r 	r e p r e s e n t a r 	o 	p r e ç o , 	a t r a v é s 	de	 uma	 string	c o m 	
parâmetros	que	determinam	a	moeda.		

## Página 84

Vamos	 aqui	 lhe	 apresentar	 a	 função	toLocalString()	d o 	J a v a S c r i p t 	e , 	s e 	q u i s e r 	s e 	a p r o f u n d a r 	
n e l a , 	v e j a 	a 	s e ç ã o 	Para	 saber	 mais	 onde	 encontrará	 a	 especificação	 desta	 função	 e	 os	
códigos	que	podem	ser	usados	para	outras	moedas.		
Vamos	 fazer	 a	 transformação	 com	e s t a 	f u n ç ã o 	p a r a 	a 	m o e d a 	R e a l 	brasileira	 e,	 a	 seguir,	
explicaremos	o	que	foi	utilizado	para	isto.	Em	nosso	arquivo	 www/templates/bebidas html,	fizemos	
o	seguinte:	
... 
<ion-item ng-repeat="bebida in bebidas" href="#/app/detalhar/{{bebida.id}}"> 
     {{bebida nome}} - {{bebida.preco.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL'})}} 
</ion-item> 
... 
V e j a 	q u e 	u t i l i z a m o s 	c o m o 	p a r â m e t r o 	d a 	f u n ç ã o 	toLocaleString()	o 	pt-BR,	 determinando	 que	 o	
local	 é	 aqui,	 em	 nosso	 país.	 Em	 seguida,	 enviamos	 um	 objeto	 info r m a n d o 	q u a l 	o 	e s t i l o 	
(moeda)	 e	 finalmente	 o	 formato	 dela	 (BRL).	 Experimente	 colocar	E U R 	n o 	l u g a r 	d e 	B R L 	e 	
observe	que	o	formato	será	alterado	para	Euro.		
Agora	volte	para	realidade	e	aceite	o	Real	como	moeda.	Lembre‐s e	de	fazer	isto	em	todos	
os	lugares	que	representam	valores	no	aplicativo:	tela	de	bebidas,	petiscos	e	sucos,	e	modal	
da	bandeja.	
Tudo	pronto,	tente	efetuar	alguns	pedidos	e	abrir	a	bandeja	para	visualizar	os	itens	pedidos	
com	o	cálculo	efetuado.	
7.3	Editar	os	itens	da	bandeja	
Para	editar,	daremos	ao	usuário	apenas	a	ação	de	informar	uma	n ova	quantidade	ao	item.	
I s t o 	é 	b e m 	s i m i l a r 	à 	s u a 	i n s e r ç ã o , 	e m 	q u e 	o 	u s u á r i o 	s e l e c i o n a 	um	 item	 no	 cardápio	 e	
informa	a	quantidade	que	ele	deseja.	Tendo	em	vista	isto,	vamos	começar	por	esta	função	
colocando‐a	no	ícone	Editar.	
	
Figura	7.3:	Ícone	Editar	
	
Construiremos	logo	todo	JavaScript	envolvido	no	www/js/controller.js.	É	muito	simples!	Para	isto,	
basta	 adicionar	 uma	 ação	 de	 abrir	 um	 modal	 com	 um	number	picker, 	s i m i l a r 	a o 	q u e 	f o i 	
construído	anteriormente,	quando	se	efetua	um	pedido.	Vamos	dar	a	este	 template	o	nome	
de	modal-edicao html.	Nosso	arquivo	ficará	assim:	


## Página 85

... 
    $scope.input = {}; 
    $scope.input.quant = 1; 
    $scope.data = {}; 
 
    $ionicModal fromTemplateUrl('modal-edicao.html', { 
        scope: $scope, 
        animation: 'slide-in-up' 
    }).then(function(m){ 
        $scope modalNumber = m; 
    }); 
 
    $scope.cancelarEdicao = function(){ 
        $scope modalNumber.hide(); 
        $scope.input.quant = 1; 
    } 
 
    $scope.editarItem = function(){ 
        $scope.input.quant = Sessao.bandeja[$scope.data.item].quantidade; 
        $scope modalNumber.show(); 
    } 
 
    $scope.confirmarEdicao = function(){ 
        //Para fazer 
    } 
... 
Observe	que	ele	será	bem	parecido	com	o	modal	de	pedir	item	do	 capítulo	anterior,	porém	
demos	 a	 ele	 um	 nome	 diferente	 em	 sua	 referência,	modalNumber, 	p a r a 	q u e 	n ã o 	s e 	c o n f u n d a 	
com	 um	 modal	 da	 bandeja	 já	 construído	 neste	controller.	 Poucas	 são	 as	 novidades	 neste	
código:	 uma	 função	 de	 cancelar,	 na	 qual	 simplesmente	 fecha‐se	 o	m o d a l ; 	e 	n o s s a 	f u n ç ã o 	
editarItem,	 que	 receberá	 um	 item	 do	radio button	s el ec io n a d o . 	P a r a 	i s t o , 	d e c i d i m o s 	p e g a r 	o 	i t e m 	
no	array	pelo	seu	index,	da	seguinte	forma:	
Sessao.bandeja[INDEX] 
Jogaremos	 o	 valor	 da	 quantidade	 do	 item	 na	 variável	input.quant	d e c l a r a d a 	c o m o 	m o d e l o 	d o 	
number	picker,	e	depois	exibiremos	o	modal	( modalNumber.show())	com	este	valor,	dando	assim	
a	opção	do	usuário	incrementar	ou	decrementar	a	quantidade	do	p edido.	Logo	em	seguida,	
construímos	 uma	 função	 vazia	 ( confirmarEdicao()),	 em	 que	 faremos	 futuramente	 a	 ação	 de	
confirmar	a	alteraçao,	ao	atualizar	os	dados	da	lista.		
Por	enquanto,	deixe‐a	em	 stand‐by	e	vamos	ver	como	passar	o	item	selecionado	para	que	
seja	possível	recuperá‐lo,	e	assi m	editá‐lo.	Preste	bastante	atenção	à	variável	 $scope.data	que	
foi	declarada	no	início,	e	usada	na	função	editarItem()	para	recuperar	o	item	do	array.		

## Página 86

Agora	vamos	ao	código	que	deve	ser	alterado	em	nossa	lista	impl ementada	por	 radio buttons,	
em	www/templates/menu html.	Lembra‐se	deles?	Pois	vamos	lhe	mostrar	a	mágica:	
... 
<ion-list ng-repeat="it in bandeja" > 
              <ion-radio  ng-value="bandeja.indexOf(it)" 
                          ng-model="data.item"> 
... 
Veja	que	usamos	as	diretivas	do	AngularJS,	sendo	que	já	explica mos	algumas	neste	mesmo	
capítulo:	ng-value	receberá	um	valor.	Esta	será	a	indexação	do	 array	JavaScript	utilizado	para	
inserir	os	itens.		
Lembre‐se	 de	 que,	 em	 JavaScript,	 o	 array	 é	 inicialmente	 indexado	 pelo	 valor	 0	 (zero),	
portanto,	 o	index	d o s 	i t e n s 	s e g u e 	a 	s e g u i n t e 	o r d e m : 	0 , 	1 , 	2 , 	3 	e 	a s s i m 	s u c e s s i v amente.	 A	
função	usada	para	isto	é	a	indexOf()	da	própria	linguagem.	Passa‐se	o	item	como	parâmetro,	e	
assim	é	retornado	o	index	que	será	atribuído	à	diretiva	ng-value,	como	já	foi	dito.	
A	 diretiva	ng-model	 será	 nosso	data‐biding	 para	 o	 item,	 ou	 seja,	 através	 dela	 será	 possível	
recuperar	 o	 valor	 que	 foi	 selecionado	 no	radio button	a o 	c l i c a r 	n o 	b o t ã o 	q u e 	c o n t é m 	a 	a ç ã o 	
editarItem().	Tudo	prontinho	pelo	lado	view	e	pelo	lado	controller.	
Agora	 vamos	 construir	 nosso	 modal	 ainda	 em	www/templates/menu html,	 cujo	 nome	 será	modal-
edicao html.	Abaixo	do	nosso	último	modal,	insira	um	template	como	a	seguir:	
... 
<!-- Modal Edição --> 
<script id="modal-edicao html" type="text/ng-template"> 
  <ion-modal-view> 
    <ion-content> 
    <div class="card"> 
      <div class="item txt-centralizado"> 
        <p>Informe a quantidade</p> 
        <p>e confirme este pedido.</p> 
        <br /> 
        <h2>{{item nome}}</h2> 
        <p><h-number value="input.quant" min="1" max="100" step="1"></h-number></p> 
      </div> 
      <div class="margem-imagem"></div> 
    </div> 
    <div class="bar bar-footer"> 
      <div class="button-bar"> 
       <button class="button icon-right ion-checkmark button-positive"  ng-click="confirmarEdicao()">Confirmar</button> 
       <button class="button icon-right ion-checkmark button-assertive"  ng-click="cancelarEdicao()">Cancelar</button> 
      </div> 
    </div> 

## Página 87

    </ion-content> 
  </ion-modal-view> 
</script> 
<!-- Fim/Modal --> 
... 
S e m 	n e n h u m 	s e g r e d o 	o u 	n o v i d a d e , 	e s t e 	m o d a l 	é 	p r a t i c a m e n t e 	i g u a l	a o 	d o 	p e d i d o . 	
Alteramos	 apenas	 os	 nomes	 das	 funções	 para	 a	 diretiva	ng-click	d o 	b o t õ e s : 	confirmarEdicao() e 
cancelarEdicao().	Execute	o	aplicativo,	insira	um	pedido,	abra	a	bandeja	selecionando	o	pedido	e	
clique	 no	 botão	 de	 edição.	 Se	 tudo	 correr	 bem,	 só	 precisamos	 construir	 a	 ação	 do	 botão	
Confirmar.	
7.4	A	função	de	confirmar	edição	
Tudo	o	que	queremos	agora	é	recuperar	o	objeto	inserido	no	 array,	e	em	seguida	alterar	a	
quantidade,	 fazendo	 um	 novo	 cálcu l o 	d o 	v a l o r 	e 	m u l t i p l i c a n d o 	o 	preço	 pela	 quantidade.	
Para	 isto,	 vamos	 voltar	 ao	 www/js/controller.js	e 	i m p l e m e n t a r 	a 	f u n ç ã o , 	a t é 	e n t ã o , 	v a z i a : 	
confirmarEdicao().	
... 
$scope.confirmarEdicao = function(){ 
    Sessao.bandeja[$scope.data.item].quantidade = $scope.input.quant; 
    Sessao.bandeja[$scope.data.item].valor =  $scope.input.quant * Sessao.bandeja[$scope.data.item].item.preco; 
    $scope modalNumber hide(); 
} 
... 
Viu	 que	 não	 há	 segredo?	 Apenas	 recuperamos	 o	 item	 selecionado	 c om	 $scope.data.item	e 	
fizemos	as	devidas	operações.	Primeiro	inserimos	a	nova	quantidade	informada,	e	depois	
pegamos	 o	 preço	 do	 item	 e	 multiplicamos	 pela	 nova	 quantidade.	 Após	 isto,	 fechamos	 o	
modal	e	assim	voltamos	à	tela	anterior.		
Observe	a	mágica	do	 data	biding	explicado	neste	livro	onde	o	próprio	AngularJS	é	capaz	de	
atualizar	 tudo,	 sem	 que	 haja	 a	 necessidade	 de	 se	 dar	 um	refresh,	 ou	 recuperar	 os	 novos	
valores.	Tudo	é	feito	de	forma	transparente	e	contínua.	
Opa!	O	pessoal	do	teste	falou	que	existe	um	bug	em	nossa	aplica ção.	Eles	disseram	que	
s e 	e n t r a r 	n a 	t e l a 	p a r a 	e d i ç ã o 	e 	c l i c a r 	n o 	b o t ã o 	Editar,	 sem	 selecionar	 algum	 item,	
aparecerá	uma	exceção	no	browser	com	a	seguinte	mensagem:	
	

## Página 88

Figura	7.4:	Sem	selecionar	
	
Ok!	Isso	parece	uma	exceção	nos	informando	que	não	há	uma	propriedade	quantidade.	Ela	
está	indefinida.	Vamos	tentar	contornar	isto	obrigando	um	item	 a	ser	selecionado	por	
padrão,	sempre	que	o	modal	da	ba ndeja	for	aberto.	Vamos	eleger	 o	item	com	 index	0	
(zero).	 Basta,	 para	 isso,	 declarar	 nossa	 variável	 antes	 do	 modal	 bandeja.	 Na	 ação	 de	
abertura,	 diremos	 a	 ele	 que	 o	$scope.data.item	é 	i g u a l 	a 	z e r o . 	V e j a m o s 	c o m o 	f i c a r á 	n o s s a 	
alteração:	
... 
    //Declaração da variável antes de ser utilizada 
    $scope.data = {}; 
    $ionicModal fromTemplateUrl('bandeja.html', { 
        scope: $scope, 
        animation: 'slide-in-up' 
    }).then(function(m){ 
        //Selecionar por padrão o zero 
        $scope.data.item = 0; 
        $scope modal = m; 
    }); 
... 
Agora	 tudo	 estará	 tranquilo	 com	 o	 pessoal	 de	 testes.	 Espero	 que	n o s 	d ê 	u m 	d e s c o n t o 	n a 	
n o s s a 	p r ó x i m a 	f u n c i o n a l i d a d e . 	V a m o s 	c o n s t r u i r 	a 	e x c l u s ã o 	d o s 	i tens	 e	 aguardarmos	
ansiosos	que	tudo	termine	sem	bugs.	
7.5	Exclusão	de	itens	
P a r a 	e x c l u i r 	i t e n s 	d a 	l i s t a , 	v a m o s 	i m p l e m e n t a r 	u m a 	f u n ç ã o 	q u e 	atenderá	 ao	 botão	 com	
ícone	 de	 lixeira	 da	 bandeja.	 Pensando	 em	 um	 aplicativo	 profissi onal,	 mais	 detalhado,	


## Página 89

teríamos	 de	 planejar	 uma	 tela	 de	c o n f i r m a ç ã o 	a p ó s 	o 	c l i q u e 	d e 	exclusão.	 Isto	 poderia	 ser	
feito	com	um	novo	modal.		
F a r e m o s 	d e 	u m a 	o u t r a 	f o r m a 	q u a n d o 	c h e g a r m o s 	n o 	c a p í t u l o 	Recursos,	 onde	 usaremos	
alguns	recursos	que	o	 Cordova	nos	oferece	através	da	instalação	de	 plugins.	Por	enquanto,	
vamos	 abstrair	 uma	 confirmação,	 partindo	 do	 pressuposto	 que,	 ao 	c l i c a r 	n o 	e x c l u i r , 	o 	
usuário	saiba	realmente	o	que	está	fazendo.		
Utilizaremos	apenas	a	função	JavaScript	 splice(pos,num).	Ela	é	responsável	por	remover	um	ou	
mais	 itens	 em	 um	array.	 O	 parâmetro	pos	 determina	 a	 posição	 em	 que	 se	 deve	 iniciar	 a	
r e m o ç ã o , 	e 	o 	num	d e t e r m i n a 	o 	n ú m e r o 	d e 	e l e m e n t o s 	a 	p a r t i r 	d a q u e l a 	p o s i ç ã o . 	E m 	nosso	
caso,	removeremos	apenas	o	item	selecionado	pelo	radio button.		
I s t o 	l e m b r a 	a l g o ? 	S i m ! 	I s s o 	m e s m o ! 	T e m o s 	a 	p o s i ç ã o 	d o 	i t e m 	n o 	array	a t r a v é s 	d o 	
$scope.data.item	de	nosso	 www/js/controllers.js.	Então	passaremos	apenas	o	valor	fixo	1	(um)	para	o	
segundo	parâmetro.	Vamos	lá?	
... 
$scope removerItem = function(){ 
    Sessao.bandeja.splice($scope.data.item,1); 
} 
... 
O	código	dispensa	comentários,	não	é	mesmo?!	Apenas	usamos	o	 splice(pos, num)	explicado	no	
array	da	bandeja,	removendo	apenas	o	item	que	estará	selecionado	pel a	diretiva	ng-model	do	
radio button.	Agora	vamos	chamar	esta	função	no	botão	do	modal	a	seguir:	
	
Figura	7.5:	Botão	Excluir	
	
O	código	em	www/templates/menu html	ficará	da	seguinte	forma:	
... 
<button class="button" ng-click="removerItem()><i class="ion-ios-trash-outline"></i></button> 
... 
A c h o 	q u e 	o 	p e s s o a l 	d o 	t e s t e 	n ã o 	e n c o n t r a r á 	n e n h u m 	bug	d e s s a 	v e z . 	E x e c u t e 	o s 	s e u s 	
próprios	testes.	


## Página 90

7.6	Confirmando	os	pedidos	
Já	 sabemos	 como	 alterar	 nossa	 bandeja,	 excluindo	 itens	 ou	 atualizando	 as	 quantidades,	
agora	vamos	aprender	a	confirmar.	Para	isto,	precisamos	planeja r	como	foi	feito	tudo	até	
aqui.	 O	 planejamento	 faz	 parte	 de	 qualquer	 processo	 de	 desenvol vimento	 de	 software.	
Mesmo	que	você	não	o	coloque	no	papel,	de	alguma	forma,	o	plane jamento	estará	implícito	
em	sua	cabeça.		
Neste	 caso,	 vamos	 planejar	 implicitamente	 que,	 ao	 clicar	 no	 botão	 confirmar,	 os	 pedidos	
sejam	enviados	para	um	"serviço".	Como	não	temos	um	serviço	de	 fato,	até	agora	o	artifício	
que	utilizamos	para	simular	isto	foram	os	mocks.	Lembra‐se	deles?!	
Mas	os	mocks	são	valores	fixos	e,	em	nosso	caso,	deverá	ser	uma	variável	dinâmica	parecida	
com	 nossa	 bandeja.	 Vamos	 guardá‐la	 também	 em	 toda	 aplicação,	 en q u a n t o 	e l a 	e s t i v e r 	
aberta,	pois	simularemos	que	nela	estará	o	histórico	de	pedidos	do	cliente.	
P a r a 	i n i c i a r m o s , 	v a m o s 	a p r o v e i t a r 	o 	o b j e t o 	t i p o 	value	 Sessao,	 criado	 no	 capítulo	 Fazendo	
pedidos,	 em	 www/js/services/sessao.js, 	e 	c o l o c a r 	e s t a 	v a r i á v e l . 	D a r e m o s 	o 	n o m e 	d e 	historicoPedidos	
para	este	array.	
angular module('starter.controllers').value('Sessao',{ 
    mesaID: "123", 
    bandeja: [], 
    historicoPedidos: [] 
}); 
Agora	 que	 temos	 um	 array	 mantido	 na	 sessão,	 toda	 vez	 que	 confirmarmos	 a	 bandeja,	
vamos	 adicionar	 todos	 os	 itens	 neste	array	e 	l i m p á ‐ l o s 	d a 	b a n d e j a . 	P o r t a n t o , 	a 	a ç ã o 	d e 	
transferência	desses	arrays	é	muito	simples.	
Até	 aqui,	 já	 falei	 em	 algumas	 funções	 para	 trabalhar	 com	array	e m 	J a v a S c r i p t . 	E l a s 	s ã o 	
muito	úteis	e	vale	a	pena	dar	uma	olhada	em	todas	que	se	encont ram	disponíveis	na	sessão	
Para	saber	mais.		
Utilizaremos	mais	uma:	Array.concat(array).	Esta	função	simplesmente	concatena	um	array	que	é	
passado	como	parâmetro	e	retorna	 um	novo	com	todos	os	elementos .	Como	nosso	objetivo	
é	 justamente	 copiar	 todos	 os	 pedidos	 da	 bandeja	 e	 jogá‐los	 em	 ou t r o 	o b j e t o 	d e 	s e s s ã o , 	
então	ela	será	muito	útil.		
Manteremos	 assim	 o	 estado	 antigo	 deste	array	e 	c r i a r e m o s 	s e m p r e 	u m 	n o v o 	c o m 	i t e n s 	
adicionados	 no	 final	 dele.	 Feito	 isto,	 deveremos	 limpar	 e	 fecha r	 nossa	 bandeja.	 Para	 a	
l i m p e z a 	d e 	n o s s a 	l i s t a , 	u s a r e m o s 	a 	f u n ç ã o 	j á 	c o n h e c i d a 	splice.	 Vamos	 à	 codificação	 no	
www/js/controllers.js.	
... 
$scope historicoPedidos = Sessao.historicoPedidos; 

## Página 91

$scope.pedir = function(){ 
    Sessao historicoPedidos = Sessao historicoPedidos.concat(Sessao.bandeja); 
    Sessao.bandeja.splice(0,Sessao.bandeja.length); 
    $scope historicoPedidos = Sessao.historicoPedidos; 
    $scope modal hide(); 
} 
... 
Analisando	o	código,	o	leitor	pode	verificar	a	junção	dos	arrays	em	 concat	e	seu	retorno	para	
a	variável	historicoPedidos.	Logo	abaixo,	limpamos	o	array	com	o	splice	começando	pelo	primeiro	
elemento	 (0)	 e	 finalizando	 em	 seu	 tamanho	 total	 ( Sessao.bandeja.length).	 Em	 seguida,	
atualizamos	a	variável	 $scope historicoPedidos	com	o	novo	array	para	que	tenhamos	a	referência	
atualizada.	Por	fim,	fechamos	a	bandeja	com	o	hide	do	modal.	Fácil,	não	é	mesmo?!	
7.7	Conclusão	
E s p e r o 	q u e 	t e n h a m o s 	c h e g a d o 	a t é 	a q u i 	c o m 	u m a 	b o a 	b a g a g e m 	d e 	u t ilização	 do	 Ionic	
framework, 	o n d e 	h á 	v á r i a s 	t e c n o l o g i a s 	e n v o l v i d a s 	q u e , 	j u n t a s , 	f o r m a m 	u m 	paradigma	
inovador	 de	 desenvolvimento	 de	 aplicativos:	 os	 Apps	 híbridos.	 Vimos	 um	 pouco	 de	 cada	
coisa	como,	JavaScript,	AngularJS,	CSS,	HTML,	Cordova	etc.	
N o 	p r ó x i m o 	c a p í t u l o , 	v a m o s 	a p r e n d e r 	a 	s i m u l a r 	n o s s o 	p e d i d o 	d e 	conta,	 fazendo	 a	
recuperação	dela,	e	dando	a	possi bilidade	de	o	cliente	pedir	que	seja	finalizada	ou	pagá‐la.	
Não	 desista,	 estamos	 chegando	 ao	 final	 do	 livro	 e	 sairemos	 dele	 com	 um	 conhecimento	
imensurável.		
A o 	f i n a l , 	d e 	c o r t e s i a , 	d e m o n s t r arei	 em	 um	 capítulo	 especial	 e	 fora	 do	 contexto	 de	 nosso	
c a s o 	d e 	u s o 	c o m o 	u t i l i z a r 	u m 	r e c u r s o 	m a i s 	a v a n ç a d o : 	a 	c â m e r a . 	Além	 disto,	 teremos	
também	um	capítulo	dedicado	a	recursos	avançados	fornecidos	pelo	framework.	
7.8	Para	saber	mais	
	
1. Grids	–	https://ionicframework.com/docs/components/#grid	
2. Ícones	–	http://ionicons.com	
3. Typeof	JavaScript	–	
https://developer.mozilla.org/en‐
US/docs/Web/JavaScript/Reference/Operators/typeof	

## Página 92

4. toLocaleString()	–	
https://developer.mozilla.org/pt‐
BR/docs/Web/JavaScript/Reference/Global_Objects/Number/toLocaleString	
5. Currency	ISO	–	https://www.currency‐iso.org/en/home/tables/table‐a1.html	
6. Operações	com	array	em	JavaScript	–		
https://www.w3schools.com/jsref/jsref obj array.asp 	
 

## Página 93

CAPÍTULO	8	
A	conta	
Neste	 capítulo,	 consideraremos	 que	 o	 usuário	 precisa	 encerrar	 su a 	c o n t a 	e 	p a g á ‐ l a 	c o m 	
u m a 	i n t e g r a ç ã o 	v i a 	c a r t ã o 	d e 	c r é d i t o . 	V i s t o 	q u e 	o s 	g a r ç o n s 	d e m oram	 para	 trazer	 a	 conta	
h o j e 	e m 	d i a , 	i s s o 	p o d e 	s e r 	u m a 	b o a 	i d e i a , 	n ã o ? 	P o r t a n t o , 	v a m o s 	tentar	 simular	 esta	
integração?	
P a r a 	i s t o , 	v a m o s 	p l a n e j a r 	t o d o 	f l u x o 	d e 	t e l a , 	c o m o 	t e m o s 	f e i t o 	até	 aqui.	 Pediremos	 ao	
pessoal	do	design	para	que	nos	apresentem	uma	tela	e	veremos	o	 que	será	possível	fazer	
por	eles.	
8.1	Construção	do	template	
A v a l i a n d o 	o s 	r e q u i s i t o s , 	p o d e m o s 	a f i r m a r 	q u e 	o 	l a y o u t 	d e s t a 	t e la	 será	 bastante	 similar	 à	
lista	 da	 bandeja.	 Conversamos	 com	 o	 pessoal	 de	 design	 e	 Analistas	 de	 Requisitos,	 e	 eles	
c h e g a r a m 	a 	u m a 	c o n c l u s ã o : 	" V a m o s 	c o n s t r u i r 	u m 	r a s c u n h o 	e 	e n v i a r	 para	 vocês	
d e s e n v o l v e r e m " . 	A s s i m 	q u e 	r e c e b e m o s , 	t i v e m o s 	u m a 	s u r p r e s a . 	N ã o 	é	 que	 estávamos	
certos?	Realmente	vamos	aproveitar	muita	coisa	de	lá.	
	
Figura	8.1:	Protótipo	da	conta	


## Página 94

Analisando	a	primeira	tela	(no	protótipo,	a	segunda	da	esquerda	para	direita),	verificamos	
que	 existe	 sim	 uma	 similaridade	com	 a	 bandeja,	 mas	 com	 algumas	particularidades:	 um	
cálculo	da	conta	a	pagar,	um	divisor	por	pessoas	e	uma	barra	de 	botões	logo	abaixo	para	a	
opção	de	Pagar	ou	Fechar	a	conta.		
Observe	 as	 setas	 para	 entender	 os	 dois	 fluxos	 que	 vamos	 simular. 	N o 	c e n á r i o 	e m 	q u e 	o 	
usuário	 clicar	 no	 botão	 de	 pagar,	 direcionaremos	 para	 uma	 tela	 de	 preenchimento	 dos	
dados	referentes	ao	pagamento.	S e	o	usuário	resolver	apenas	fec har	a	conta,	a	tela	será	de	
a g r a d e c i m e n t o , 	s u p o n d o 	q u e 	o 	p e d i d o 	f o i 	e n v i a d o 	a o 	c a i x a 	p a r a 	que	 o	 garçom	 conduza	 a	
nota	até	a	mesa.		
M u n i d o 	d e s s a s 	i n f o r m a ç õ e s , 	v a m o s 	i m p l e m e n t a r 	p r i m e i r o 	a 	t e l a 	i nicial.	 Para	 isto,	 basta	
aproveitar	 um	 pouco	 o	 código	 do	 modal	 da	 bandeja	 e	 ir	 adaptando.	 Mas	 antes,	 vamos	
r e l e m b r a r 	d o 	q u e 	f i z e m o s 	n o s 	c a p í t u l o s 	Conhecendo	 os	 nossos	 arquivos	e 	Completando 	 o	
menu,	onde	fizemos	os	menus,	mas	deixamos	de	lado	a	tela	de	conta.	 Vamos	construir	isto	
no	www/js/app.js.	
... 
  .state('app.conta', { 
      url: '/conta', 
      views: { 
        'menuContent': { 
          templateUrl: 'templates/conta.html', 
          controller : 'ContaCtrl' 
        } 
      } 
 
  }); 
  ... 
Portanto,	nosso	último	 state	será	o	da	conta,	em	que	configuramos	o	controller 	ContaCtrl	e	o	
template	www/templates/conta html. 	S e m 	n e n h u m a 	n o v i d a d e , 	m a p e a m o s 	a 	t e l a 	d a 	c o n t a 	p a r a 	s e r 	
representada	pela	URL	#/app/conta/.	Em	nosso	www/templates/menu.html,	podemos	fazer	assim:	
... 
<ion-list> 
    <ion-item menu-close href="#/app/bebidas"> 
      Bebidas 
    </ion-item> 
    <ion-item menu-close href="#/app/petiscos"> 
      Petiscos 
    </ion-item> 
    <ion-item menu-close href="#/app/sucos"> 
      Sucos 
    </ion-item> 

## Página 95

    <ion-item menu-close href="#/app/conta"> 
      Conta 
    </ion-item> 
</ion-list> 
... 
J á	q u e	dec laram o s	o 	template	e	o	controller , 	s ó 	no s 	res t a	c o ns tru í‐ l o s . 	Vam o s 	p rim eiro 	a o 	
template.	 Basta	 reaproveitar	 o	 modal	 da	 bandeja	 que	 se	 encontra	e m 	www/templates/menu html.	
Removendo	 as	 tags	 <script>	e 	 <ion-modal-view>,	 e	 inserindo	 <ion-view>,	 você	 não	 estará	 mais	
colocando	 um	 template	 dentro	 de	 um	 arquivo	 que	 contém	 outros	 templates	‐ 	v i s t o 	n o 	
capítulo	anterior.		
Vo c ê	tam b ém 	não 	u s ará	m ais 	a	tel a	em 	fo rm a	d e	m o d al , 	c o m 	to d as 	funções	JavaScript	de	
c o m a n d o s 	( f e c h a r 	e 	a b r i r ) , 	a l é m 	d e 	t e r 	d e 	d e c l a r a r 	o 	o b j e t o 	q u e	 representa	 o	 modal	 com	
$ionicModal fromTemplateUrl().	Vamos	criar	um	template	único	em	um	HTML,	e	pronto.	Portanto, 	
como	nossa	tela	não	será	mais	um	modal,	vamos	inserir	o	código	na	tag	<ion-view>.	O	restante	
será	a	mesma	coisa	(por	enquanto)	e	ficará	assim:	
<ion-view title="Conta"> 
    <ion-content> 
        <div class="card"> 
          <div class="item txt-centralizado"> 
            <div class="row"> 
                <div class="col"> 
                  Quantidade 
                </div> 
                <div class="col"> 
                  Item 
                </div> 
                <div class="col"> 
                  Valor 
                </div> 
            </div> 
 
            <ion-list ng-repeat="it in historicoPedidos" > 
              <ion-radio  ng-value="historicoPedidos.indexOf(it)"  
                          ng-model="data.item"> 
                 <div class="row"> 
                  <div class="col"> 
                   {{it.quantidade}}  
                  </div> 
                  <div class="col"> 
                    {{it.item nome}} 
                  </div> 
                  <div class="col"> 

## Página 96

                    {{it.valor.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL'})}} 
                  </div> 
                 </div> 
              </ion-radio> 
            </ion-list> 
            <br /> 
          </div> 
          <div class="margem-imagem"></div> 
        </div> 
        <div class="bar bar-footer"> 
          <div class="button-bar"> 
           <button class="button  button-positive"  ng-click="pedir()"><i class=" ion-ios-checkmark-outline"></i></button> 
           <button class="button  button-dark"  ng-click="editarItem()"><i class="ion-edit"></i></button> 
           <button class="button" ng-click="removerItem()"><i class="ion-ios-trash-outline"></i></button> 
           <button class="button  button-assertive"  ng-click="fechaModal()"><i class="ion-ios-undo-outline"></i></button> 
          </div> 
        </div> 
    </ion-content> 
</ion-view> 
Desta	forma,	nada	muda	em	relação	à	bandeja,	mas	não	é	exatamente	isto	que	o	pessoal	de	
design	pediu,	não	é	mesmo?	Precisamos	adaptar	algumas	mudanças.		
Observe	que,	com	nosso	copiar	e	colar,	não	estamos	omitindo	o	a prendizado.	Estamos	
fazendo	isto	em	códigos	que	já	foram	explicados	anteriormente	e,	a	partir	deles,	vamos	
evoluir	em	algo	que	ainda	não	conhecemos.		
Mesmo	com	a	repetição	desses	códi gos,	seria	interessante	você	c omeçar	a	construir	as	
views	inserindo	os	componentes	um	a	um,	sem	utilizar	o	recurso	de	co piar/colar.	Isso	
ajudará	a	fixar	o	nome	dos	componentes	e	o	aprendizado.	
Primeiramente,	vamos	adaptar	os	botões	do	rodapé.	Não	precisamo s	de	tantos,	mas	apenas	
dois,	e	com	um	texto	em	vez	de	ícones.	Vamos	ao	código:	
... 
 <div class="bar bar-footer"> 
  <div class="button-bar"> 
   <button  class="button button-positive">Pagar</button> 
   <button  class="button button-assertive">Fechar</i></button> 
  </div> 
</div> 
... 

## Página 97

Veja	que	excluímos	dois	botões	e	alteramos	os	dois	que	sobraram :	retiramos	a	 tag	<i>	que	
representava	os	ícones	para	dar	lugar	ao	texto	que	aparecerá	no 	botão.	Analisando‐os,	dá	
para	 concluir	 que	 são	 botões	 sem	 ação,	 portanto,	 inúteis.	 Precisamos	 entregar	 para	 eles	
funções	 que	 vão	 agregar	 valor	 à	 nossa	 funcionalidade.	 Para	 isto , 	m a i s 	à 	f r e n t e , 	
construiremos	as	funções	de	pagar	e	fechar	a	conta.		
Por	enquanto,	vamos	deixar	um	pouco	de	lado	as	funções	JavaScript	e	nos	preocupar	com	o	
formato	do	template,	fazendo	com	que	ele	reflita	a	aparência	do 	nosso	protótipo.	Para	isto	
vamos	 construir	 um	 controller, 	p o i s 	p r e c i s a m o s 	c h a m a r 	a 	t e l a 	e 	v e r 	c o m o 	e s t á 	f i c a n d o . 	
Além	disto,	este	controller	será	usado	nas	operações	da	conta.	
app.controller('ContaCtrl', function($scope){ 
}); 
Agora	inclua	dois	itens	à	bandeja,	confirme	os	pedidos	e	depois 	clique	em	conta	no	menu.	
Vejamos	o	resultado:	
	
Figura	8.2:	Conta	sem	ajustes	
	
Ops!	Algo	estranho	aconteceu	nesta	tela.	A	conta	não	deve	permi tir	a	opção	de	selecionar	
um	item,	pois	não	vamos	editá‐lo.	Sugiro	que	retire	o	 radio	button,	deixando	apenas	a	lista	
de	itens	desta	forma:	
... 
<ion-list ng-repeat="it in historicoPedidos" > 
    <div class="row"> 


## Página 98

        <div class="col"> 
            {{it.quantidade}}  
        </div> 
        <div class="col"> 
            {{it.item nome}} 
        </div> 
        <div class="col"> 
            {{it.valor.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL'})}} 
        </div> 
    </div> 
... 
Agora	 precisamos	 acrescentar	 os	 campos	 novos:	 total,	 opcional	 e 	 subtotal.	 Além	 disto,	
c o l o c a r e m o s 	u m a 	c a l c u l a d o r a 	p a r a 	d i v i d i r 	a 	c o n t a 	e n t r e 	a 	q u a n t idade	 de	 pessoas	
informadas	em	um	 input.	Em	nossa	 view,	usaremos	novamente	 grids	para	organizar	estes	
campos,	seguindo	a	imagem	do	protótipo.	
... 
 
<div class="row"> 
    <h2>Total:</h2> 
</div> 
<div class="row"> 
    Opcional(10%): 
</div> 
<div class="row"> 
    <h2>Subtotal:</h2> 
</div> 
<br /> 
<div class="row"> 
    Informe abaixo a quantidade de pessoas 
</div> 
<div class="row"> 
    <div class="col item item-input col-25">   
        <input type="number" /> 
    </div> 
    <div class="col"> 
        <p><h2>Valor por pessoa:</h2></p> 
    </div> 
</div> 
<div class="margem-imagem"></div> 
<!-- Abaixo fechar o card e insere a barra de botões --> 
... 

## Página 99

Por	enquanto,	temos	nossa	tela	seguindo	o	protótipo,	mas	sem	mu ita	função	além	de	listar	
todos	os	pedidos	que	foram	confirmados	através	da	bandeja.	Pegu e	agora	uma	boa	xícara	
de	café	e	vamos	avaliar	como	faremos	todos	os	cálculos	que	essa	tela	precisa.	
O	 primeiro	 é	 total,	 que	 representa	 a	 soma	 de	 todos	 os	 pedidos.	 Em	 seguida,	 devemos	
c a l c u l a r 	1 0 % 	s o b r e 	e s t e 	t o t a l 	e , 	p o r 	f i m , 	s o m a r 	e s t e 	p e r c e n t u a l 	c o m 	o 	t o t a l 	p a r a 	f o r n e c e r 	
um	valor	ao	usuário.		
E s t e s 	c á l c u l o s 	s ã o 	b á s i c o s 	e 	p a d r ã o 	e m 	c o n t a s 	d e 	q u a l q u e r 	e s t a belecimento.	 Vamos	
construir	uma	função	responsável	por	executar	esta	regra	de	neg ócio	de	forma	assíncrona,	
porém	rápida,	assim	que	entrarmos	na	tela.		
Teremos	de	fazer	uma	função	que	execute	um	loop	no	array	de	pedidos,	some	todos	os	seus	
valores	e	guarde	em	uma	variável.	A	partir	dela,	poderemos	fazer	os	outros	cálculos.	
... 
    $scope.conta = {}; 
    $scope.calcularConta = function(){ 
        $scope.conta.total = 0; 
        $scope historicoPedidos.forEach(function(v){ 
            $scope.conta.total = $scope.conta.total + v.valor; 
        }) 
        $scope.conta.porcentagem = $scope.conta.total * 10/100; 
        $scope.conta.subtotal = $scope.conta.porcentagem + $scope.conta.total; 
    } 
Analise	 com	 atenção	 este	 código.	 Veja	 que,	 antes	 da	 função,	 dec laramos	 um	 objeto	
$scope.conta.	Ele	servirá	de	base	para	inserirmos	os	atributos	 total,	percentual	e	subtotal.	Logo	abaixo	
vem	 a	 função	 propriamente	 dita,	 que	 chamaremos	 toda	 vez	 que	 a	 t e l a 	d e 	c o n t a 	f o r 	
executada.	
Você	deve	estar	curioso	para	saber	onde	a	chamaremos,	não	é	mes mo?	Explicaremos	mais	
tarde,	 por	 enquanto	 vamos	 pensar	 apenas	 neste	 código.	Veja	 que,	na	 chamada,	 faremos	 o	
loop	na	lista	de	itens,	somando	o	valor	de	todos	os	pedidos	e	guard ando	na	propriedade	do	
objeto	$scope.conta.total.		
Para	isto,	antes,	devemos	zerar	este	total,	visto	que	esta	função	está	no	 controller	principal	
e	 nunca	 perderá	 seu	 estado.	 Abaixo	 do	loop,	 temos	 de	 fato	 o	 cálculo	 do	 percentual	 e	 o	
subtotal.	 Dessa	 forma,	 vamos	 fazer	 o	 data‐binding	n a 	t e l a 	e m 	www/templates/conta html,	 da	
seguinte	forma:	
... 
<div class="row"> 
    <h2>Total: {{conta.total}}</h2> 
</div> 
<div class="row"> 

## Página 100

    Opcional(10%): {{conta.porcentagem}} 
</div> 
<div class="row"> 
    <h2>Subtotal: {{conta.subtotal}}</h2> 
</div> 
... 
Mas	e	agora?	Onde	chamaremos	nossa	função?		
C a l m a ! 	V a m o s 	a o 	www/templates/menu html	 para	 utilizar	 um	 conhecimento	 já	 adquirido	 neste	
livro.	 O	 famigerado	 conceito	 de	 diretiva	 do	 AngularJS.	 No	 menu	da	 conta,	 devemos	 ter	 o	
componente	<ion-item menu-close>	com	o	seguinte	formato:	
... 
<ion-item menu-close href="#/app/conta"  
        ng-click="calcularConta()"> 
    Conta 
</ion-item> 
... 
Vejo	 no	 código	 que,	 através	 da	 diretiva	ng-click,	 chamamos	 a	 função	calcularConta()	 de	 nosso	
controller.	Isso	é	totalmente	diferente	dos	outros	itens	de	menu.	O	que	f izemos	foi	apenas	
executar	uma	função	JavaScript	–	antes	de	abrir	nossa	tela	–,	r esponsável	por	executar	os	
c á l c u l o s 	d a 	c o n t a . 	S i m p l e s 	a s s i m ! 	A g o r a 	t u d o 	e s t á 	m u i t o 	b e m 	f e i t o 	e 	e s p e r a n d o 	v o c ê 	
executar	alguns	testes.	
Eu	sei	que	você	leu	este	livro	até	aqui	e	chegou	a	este	ponto	s abendo	muitos	conceitos	de	
uma	 variedade	 de	 plataformas,	 frameworks	 e	 linguagem	 de	 program ação.	 Disso	 tudo,	
vimos	uma	característica	muito	legal	do	JavaScript,	que	é	a	forma	de	representar	a	moeda.		
Eu	 também	 sei	 que	 você	 deve	 estar	 achando	 estranho	 que	 não	 colocamos	 isto	 nos	 novos	
campos	inseridos.	Não	se	preocupe!	Foi	tudo	proposital,	meu	caro!	Deixamos	isto	para	você	
praticar.	 Faça	 bom	 uso	 da	 função	 .toLocaleString('pt-BR', { style: 'currency', currency: 'BRL'}) 	 para	
representar	nossa	moeda	brasileira,	e	agora	sim	tudo	ficará	muito	bem	ajustado.	
8.2	Vamos	dividir	a	conta	
S a b e 	a q u e l a 	h o r a 	e m 	q u e 	u m 	a m i g o 	d i z 	q u e 	e s t á 	i n d o 	e m b o r a 	e 	p e de	 uma	 conta	 parcial?	
Após	este	evento,	o	restante	vai	saindo	na	sequência,	mas	sempr e	pedindo	a	conta	parcial.	
Agora	é	a	hora	de	ver	quanto	ficará	para	cada	um,	já	que	todos	 beberam	e	quem	não	bebeu	
segue	a	máxima:	"Sentou,	sorriu.	A	conta	dividiu!".	Para	facili tar	a	vida	do	pessoal,	vamos	
implementar	 a	 calculadora	 na	 qual	 será	 possível	 digitar	 apenas	 uma	 informação:	
quantidade	de	pessoas	que	pagarão	a	conta.	

## Página 101

Depois	 de	 todos	 os	 cálculos	 feitos	 na	 função	 anterior,	 fazer	 um	c á l c u l o 	d e 	d i v i s ã o 	f i c o u 	
simples.	Vamos	fazer	um	data‐binding	da	quantidade	de	pessoas,	e	assim	calcular	o	valor	da	
divisão	na	própria	view	(www/templates/conta html).		
... 
<div class="row"> 
    <div class="col item item-input col-25">   
        <input type="number" ng-model="conta.quantidadePessoa"/> 
    </div> 
    <div class="col"> 
        <p><h2>Valor por pessoa: {{(conta.subtotal / conta.quantidadePessoa) 
            .toLocaleString('pt-BR', { style: 'currency', currency: 'BRL'})}}</h2></p> 
    </div> 
</div> 
... 
Observe	a	diretiva	ng-model	do	input	e	veja	que	ela	faz	o	papel	do	 data‐binding	já	explicado.	O	
valor	 é	 atualizado	 constantemente	 e,	 na	 mesma	 view, 	p e g a m o s 	e s t e 	v a l o r 	e 	d i v i d i m o s 	
através	 da	 operação	 entre	 4	 chaves	 ({{}}).	 Observe	 que,	 depois	 da	 divisão,	 utilizamos	 a	
função	 do	 JavaScript	 para	 formatar	 novamente	 em	 nossa	 moeda	Real,	 com	 dois	 dígitos	
decimais	após	a	vírgula.	
8.3	Pagar	ou	pedir?	
Q u a n d o 	o 	u s u á r i o 	e n t r a r 	n a 	f u n c i o n a l i d a d e 	d e 	c o n t a , 	c o n f o r m e 	o 	protótipo,	 ele	 terá	 de	
escolher	entre	pagar	através	dos	dados	do	cartão	de	crédito,	ou	efetuar	o	pedido	de	fechar	
a	 conta.	 Estas	 duas	 ações	 serão	 executadas	 através	 dos	 dois	 botões,	 já	 inseridos	 na	 tela.	
Para	isto,	precisamos	construir	dois	modais	que	representarão	e stas	duas	funcionalidades	
e	chamar	de	acordo	com	a	ação	escolhida.		
Pensando	 dessa	 forma,	 vamos	 inserir	 os	 dois	 modais	 no	 mesmo	 template,	
www/templates/conta.html,	 como	 já	 fizemos	 com	 a	 bandeja.	 A	 inserção	 destes	 modais	 serão	p e l a 	
tag	<script type="text/ng-template">,	não	esquecendo	que	cada	um	terá	um	id.		
Vamos	dividir	o	fonte	em	duas	partes	para	não	ficar	muito	longo .	Portanto,	vamos	ao	fonte	
do	modal	que	representará	o	pedido	de	fechar	a	conta.	
... 
<script id="modal-fechar-conta.html" type="text/ng-template"> 
  <ion-modal-view> 
    <ion-content> 
      <div class="card"> 
            <br /> 
            <div class="row"> 

## Página 102

              <div class="col col-offset-25"> 
                <h1>Obrigado!</h1> 
              </div> 
            </div> 
            <div class="margem-imagem"></div> 
            <div class="txt-centralizado">Em breve o garçon levará sua conta!</div> 
            <div class="margem-imagem"></div> 
            <div class="row"> 
              <div class="col-offset-33"> 
                Total: {{conta.total.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL'})}} 
              </div> 
            </div> 
            <div class="row"> 
              <div class="col-offset-33"> 
                Opcional(10%): {{conta.porcentagem.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL'})}} 
              </div> 
            </div> 
            <div class="row"> 
              <div class="col-offset-33"> 
                Subtotal: {{conta.subtotal.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL'})}} 
              </div> 
            </div> 
            <br /> 
          <div class="row"> 
            <div class="col col-offset-33"> 
              <button type="button" class="button button-positive button-block">Voltar</button> 
            </div> 
            <div class="col"></div> 
          </div> 
      </div> 
    </ion-content> 
  </ion-modal-view> 
</script> 
... 
O	 código	 contém	 poucas	 novidades,	 mas	 algo	 novo	 poderá	 lhe	 cham a r 	a 	a t e n ç ã o . 	
Organizamos	os	elementos	com	grids	através	das	classes	row	e	tag.	Existe	no	framework	uma	
classe	usada	para	deslocar	uma	coluna	dentro	de	um	 grid.	Essa	classe	é	a	 col-offset-xx,	em	que	
x	é	o	percentual	que	queremos	deslocar.		
A	 seguir,	 veremos	 uma	 tabela	 com	 os	 percentuais	 de	 deslocamento 	 e	 suas	 respectivas	
classes:	
	
	

## Página 104

	
Figura	8.4:	Botão	deslocado	
	
V e j a 	q u e 	o 	b o t ã o 	d e 	f a t o 	p r e e n c h e u 	t o d a 	c o l u n a 	a 	p a r t i r 	d o 	col- offset-33,	 porém	 como	 não	
encontrou	 nenhuma	 coluna	 à	 direita 	d e l e , 	e l e 	e x t r a p o l o u 	e 	o 	e f eito	 não	 ficou	 satisfatório	
para	 nosso	 design. 	B u s c a n d o 	u m a 	s o l u ç ã o 	i n t e l i g e n t e , 	p e n s a m o s 	e m 	u m a 	c o l u n a 	fake	à 	
direita	 deste	 botão.	 Dessa	 forma,	 cria‐se	 a	 seguinte	tag	 <div class="col"></div>,	 que	 determina	
que	existe	uma	coluna,	mas	sem	nenhum	elemento	nela.	
C o m 	t u d o 	p r o n t o 	p a r a 	a b r i r 	o 	m o d a l , 	s ó 	n o s 	r e s t a 	d e c l a r á ‐ l o 	n o 	JavaScript	 do	controller	
www/js/conta-controller.js.	Também	precisaremos	chamar	a	função	de	abrir	no	botão	 Fechar	da	tela	
de	conta,	e	a	função	de	fechar	no	botão	Voltar	do	modal.	O	código	da	declaração	ficará	assim:	
... 
$ionicModal fromTemplateUrl('modal-fechar-conta html', { 
    scope: $scope, 
    animation: 'slide-in-up' 
}).then(function(modal){ 
    $scope modalFecharConta = modal; 
}); 
... 


## Página 105

Tudo	muito	parecido	por	enquanto,	não	é	mesmo?	Observe	que	declaramos	o	modal	que	foi	
construído	 na	 tag	 <script>	c o m 	id	i g u a l 	a 	modal-fechar-conta html,	 e	 demos	 a	 ele	 o	 nome	 de	
modalFecharConta	que	ficará	no	objeto	$scope.	Agora	vamos	fazer	algo	diferente.		
L e m b r a 	d e 	q u a n d o 	c o n s t r u í m o s 	a 	b a n d e j a 	e , 	a l é m 	d e 	d e c l a r a r 	o 	m odal,	 construímos	
também	duas	funções:	 fechaModal()	e	 abreModal()?	Esse	código	muitas	vezes	faz	apenas	o	papel	
de	encapsular	as	funções	hide()	e	show(),	que	já	estão	prontas	no	framework.	Inteligentemente,	
vamos	 apenas	 chamá‐las	 nas	 diretivas	 ng-click	 de	 nossos	 botões	 em	 vez	 de	 sair	 por	 aí	
escrevendo	códigos	para	fechar	e	abrir	modais,	espalhados	por	todas	as	classes.	
Se	você	sentir	a	necessidade	de	criar	alguma	regra	de	negócio,	 validação	ou	até	mesmo	
carregar	 alguma	 informação	 antes	 dos	 eventos	 de	 abrir	 e/ou	 fech ar	 os	 modais,	
aconselho	que	construa	sua	função	dentro	do	controller.	
No	botão	Fechar,	colocamos:	
... 
 <!-- Botões para fechar a conta -->  
<div class="bar bar-footer"> 
  <div class="button-bar"> 
     <button class="button button-positive">Pagar</button> 
     <button class="button button-assertive"   
             ng-click="modalFecharConta.show()">Fechar</i> 
     </button> 
  </div> 
</div> 
... 
E	no	botão	de	voltar	do	modal:	
... 
<div class="row"> 
<div class="col col-offset-33"> 
    <button   type="button"  
            class="button button-positive button-block"  
            ng-click="modalFecharConta hide()"> 
         Voltar 
    </button> 
</div> 
<div class="col"></div> 
</div> 
... 

## Página 106

A g o r a 	s i m ! 	N o s s o 	m o d a l 	j á 	p o d e 	s e r 	t e s t a d o . 	A d i c i o n e 	a l g u n s 	i t ens	 na	 bandeja,	 depois	
confirme	os	pedidos	e	veja	a	simulação	ocorrer	como	planejamos.	Estamos	simulando	que	
o	 serviço	 estará	 guardando	 todos	 os	 itens	 confirmados	 e,	 ao	 final,	 nós	 teremos	 todo	 o	
histórico	de	pedidos	na	memória,	em	um	caso	real,	em	algum	webservice	na	nuvem.	
Então,	vamos	construir	o	nosso	outro	modal,	o	que	terá	a	função 	de	pagar	a	conta.	Este	nos	
dará	os	fundamentos	necessários	para	a	criação	de	 forms	e	o	leitor	conhecerá	a	facilidade	
que	o	framework	nos	fornece	para	este	componente.	
Antes	de	começarmos,	lembre‐se	d e	que	tudo	será	montado	em	mais 	um	modal.	Portanto,	
vamos	 iniciar	 declarando‐o	 em	 www/js/conta-controller.js, 	e n t r e t a n t o 	c o m 	o u t r o 	n o m e 	p a r a 	o 	
template:	modal-pagar.conta-html.	
... 
$ionicModal fromTemplateUrl('modal-pagar-conta.html', { 
    scope: $scope, 
    animation: 'slide-in-up' 
}).then(function(modal){ 
    $scope modalPagarConta = modal; 
}); 
... 
Feito	 isto,	 vamos	 construir	 o	 mo dal	 dentro	 do	 mesmo	 arquivo	 da	 conta.	 Em	
www/templates/modal-pagar-conta html,	declararemos	a	tag	<script>	com	a	seguinte	estrutura:	
... 
 <!-- Modal pagar conta --> 
<script id="modal-pagar-conta html" type="text/ng-template"> 
  <ion-modal-view> 
    <ion-content> 
      <div class="card"> 
            <div class="margem-imagem"></div> 
            <div class="row"> 
              <div class="col-offset-25"><h3>Dados do cartão</h3></div> 
            </div> 
            <div class="row"> 
              <div class="col-offset-33"> 
                Total: {{conta.total.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL'})}} 
              </div> 
            </div> 
            <div class="row"> 
              <div class="col-offset-33"> 
                Opcional(10%): {{conta.porcentagem.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL'})}} 
              </div> 
            </div> 

## Página 107

            <div class="row"> 
              <div class="col-offset-33"> 
                Subtotal: {{conta.subtotal.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL'})}} 
              </div> 
            </div> 
            <br /> 
          <div class="row"> 
            <div class="col col-offset-33"> 
              <button type="button" class="button button-positive button-block" ng-
click="modalPagarConta hide()">Voltar</button> 
            </div> 
            <div class="col"></div> 
          </div> 
      </div> 
    </ion-content> 
  </ion-modal-view> 
</script> 
... 
Por	enquanto,	este	modal	apresenta	apenas	os	valores:	total,	op cional	e	subtotal	e	o	botão	
Voltar.	Fizemos	isto	para	reaproveitar	um	pouco	do	código	do	modal	anterior,	acrescentamos	
um	offset	de	coluna	para	o	título	de	25%,	mas	ainda	precisamos	ajustar	no	nosso	protótipo.	
Vamos	começar	inserindo	um	Pagar	ao	lado	do	Voltar.	Para	isto,	vamos	retirar	a	classe	 col-offset-
33,	pois	não	há	mais	a	necessidade	de	deslocar	uma	coluna	com	33% .	O	que	organizará	os	
botões	aqui	serão	duas	colunas,	lado	a	lado.		
P o d e r í a m o s 	u t i l i z a r 	u m a 	b a r r a 	d e 	r o d a p é 	c o m 	o s 	b o t õ e s 	c o m o 	f o i 	feito	 na	 primeira	
t e l a . 	F i z e m o s 	d e s t a 	f o r m a 	a p e n a s 	c o m 	o 	i n t u i t o 	d e 	a p r e n d e r 	n o v os	 conceitos	 de	
organização	dos	elementos.	
Veja	como	ficará	o	código	dos	botões	a	seguir:	
... 
<div class="row"> 
    <div class="col"> 
      <button type="button" class="button button-positive button-block">Pagar</button> 
    </div> 
    <div class="col"> 
      <button type="button" class="button button-positive button-block" ng-click="modalPagarConta hide()">Voltar</button> 
    </div> 
</div> 
... 

## Página 108

Simples,	não	é	mesmo?!	Uma	linha	( row)	e	duas	colunas	na	mesma	linha	contendo	cada	uma	
um	 botão.	 Por	 enquanto,	 o	Pagar	 está	 sem	 ação,	 mas	 daqui	 a	 pouco	 veremos	 o	 que	 vamos	
fazer	com	ele.	Por	agora,	apenas	vamos	focar	em	construir	o	form	com	seus	inputs.		
No	Ionic,	existem	várias	classes	para	os	formulários.	Existe	uma	documentação	ampla	sobre	
inputs	c o m 	labels	 ao	 lado,	 encapsulados,	placeholders,	 ícones,	 entre	 outras	 características	
que	 podemos	 dar	 aos	 elementos	 do 	f o r m u l á r i o . 	N e s t e 	l i v r o , 	t r a t aremos	 apenas	 dos	
principais,	mas	se	o	leitor	quiser	se	aprofundar,	poderá	consul tar	a	seção	 Para	saber	mais	
ao	final	deste	capítulo.	
O	input	no	HTML	tem	um	atributo	chamado	 placeholder	que	nada	mais	é	do	que	uma	descrição	
curta	 sobre	 o	 dado	 esperado	 naquele	 campo.	 Por	 exemplo,	 o	 código	 <input placeholder="Nome 
Completo">	se	apresentaria	da	seguinte	forma:	
	
Figura	8.5:	Placeholder	
	
Vamos	 distribuir	 nossos	inputs	 em	 nosso	form	c o m 	o s 	labels	e m 	f o r m a t o 	d e 	placeholder.	
Além	disto,	ficaria	mais	interessante	se,	ao	preencher	os	dados ,	o	texto	animasse	e	subisse	
ao	topo	do	campo.	Normalmente,	por	padrão	do	 placeholder,	este	 label	sumiria.	Todo	este	
desejo	 pode	 ser	 construído	 com	 facilidade	 através	 do	Floating	Labels	d o 	Ionic.	 A	 seguir,	
veremos	como	ficará	nosso	código	e,	em	seguida,	uma	explanação	mais	detalhada.	
... 
<div class="list"> 
  <label class="item item-input item-floating-label"> 
    <span class="input-label">Nome no Cartão</span> 
    <input type="text" placeholder="Nome no Cartão"> 
  </label> 
  <label class="item item-input item-floating-label"> 
    <span class="input-label">Número do Cartão</span> 
    <input type="number" placeholder="Número do Cartão"> 
  </label> 
  <label class="item item-input item-floating-label"> 
    <span class="input-label">Código de Segurança</span> 
    <input type="number" placeholder="Código de Segurança"> 
  </label> 
  <label class="item item-input item-floating-label"> 
    <span class="input-label">CPF</span> 
    <input type="number" placeholder="CPF"> 
  </label> 


## Página 109

  <label class="item item-input item-floating-label"> 
    <span class="input-label">Valor a pagar</span> 
    <input type="number" placeholder="Valor a pagar"> 
  </label> 
</div> 
... 
Cada	campo	é	composto	por	um	 label,	um	spane	um	input.	Todos	eles	encapsulados	em	uma	 div	
com	a	classe	list.	Os	labels	são	configurados	com	as	classes	 item,	item-input	e	item-floating-label.	Vamos	
explicar	cada	uma	dela:	
	
1. Classe	list:	é	a	forma	simples	de	exibir	uma	lista.	Esta	é	a	forma	mais	com um	de	
exibir	conteúdos	como	texto	simples,	botões,	imagens,	inputs	e	rádios.	
2. Classe	 item:	r e p r e s e n t a 	u m 	n o v o 	i t e m 	n a 	l i s t a , 	c o m o 	s e 	f o s s e 	u m a 	n o v a 	l i n h a,	
traçando	assim	uma	borda	para	separá‐los.	
3. Classe	item-input:	configura	o	item	para	ter	uma	aparência	de	input.	
4. Classe	item-floating-label:	responsável	por	informar	ao	 framework	que	este	item	é	um	
Floating	 Label,	 citado	 anteriormente,	 causando	 assim	 o	 efeito	 de	 "flutuar"	 o	
placeholder	para	cima	do	input.	Observe	a	seguir	uma	ilustração	deste	efeito.	
Figura	8.6:	Efeito	Floating	Label	
	
	


## Página 110

N ã o 	s e r á 	o 	f o c o 	d e s t e 	l i v r o 	t r a t a r 	d e 	e x c e ç õ e s 	o u 	v a l i d a ç õ e s 	d e	 dados.	 Portanto,	 vamos	
considerar	que	o	usuário	vai	preencher	todos	os	dados	e	de	form a	correta.	Mas	fica	a	dica	
p a r a 	q u e 	v o c ê 	p e s q u i s e 	s o b r e 	validações	de	campos	em	AngularJS,	 e	 tente	 fazer	 o	 caso	 de	
uso	de	uma	forma	mais	elab orada.	Consulte	a	seção	 Para	saber	mais	deste	c apítulo	para	
ver	uma	referência	do	W3schools	sobre	isto.	
Já	temos	nosso	form	com	uma	boa	aparência,	agora	nos	resta	fazer	um	último	ajuste:	aquele	
campo	 no	 protótipo	 do	 início	 deste	 capítulo	 chamado	Restante,	 onde	 deverá	 ser	 um	data‐
binding	segu indo 	u m a	regr a	q u e	terá	c o m o 	b ase	o 	c am p o 	Valor.	Na	prática,	isto	quer	dizer	
que,	se	uma	pessoa	na	mesa	paga	a	parte	a	ele	destinada,	o	rest ante	vai	ser	exibido	neste	
campo	até	que	a	conta	seja	totalmente	paga.		
Para	isto,	vamos	inserir	primeiro	na	diretiva	 ng-model	do	campo	 Valor	a	variável	para	guardá‐
lo:	
... 
<label class="item item-input item-floating-label"> 
    <span class="input-label">Valor a pagar</span> 
    <input type="number" placeholder="Valor a pagar" ng-model="conta.valorPagar"> 
</label> 
... 
Em	seguida,	inserimos	a	operação	no	campo	Restante	da	seguinte	forma:	
... 
 <div class="row"> 
  <div class="col-offset-33"> 
    Restante: {{(conta.subtotal - conta.valorPagar).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL'})}} 
  </div> 
</div> 
... 
Tudo	pronto,	vamos	apenas	simular	que	a	conta	foi	paga.	Quando	 o	usuário	clicar	no	botão,	
devemos	inserir	um	novo	item	no	histórico	de	pedidos.	Este	novo 	item	será	o	pagamento	e	
terá	u m 	val o r	nega tivo ,	p ara	q u e,	ao 	gera r	u m a	no va	c o nta,	o 	valor	deste	pagamento	seja	
subtraído	do	total.	
Para	 isto,	 vamos	 inserir	 a	 codificação	 de	 adicionar	 um	 novo	 item	 à	 lista	 de	 pedidos	 em	
www/js/conta-controller.js.		
... 
$scope.pagar = function(){ 
    var valor = -$scope.conta.valorPagar; 
    Sessao 
        historicoPedidos 

## Página 111

            .push({item: { nome : "Pagamento"}, quantidade : 1, valor: valor}); 
    $scope modalPagarConta hide(); 
} 
... 
Não	devemos	esquecer	da	injeção	do	objeto	Sessao	no	controller:		
app.controller('ContaCtrl', function($scope, $ionicModal, Sessao){... 
Inserimos	assim	um	valor	negativo	e	demos	 o	nome	de	 Pagamento.	Através	do	 push	do	array,	
adicionamos	este	novo	item	à	lista	historicoPedidos,	e	depois	fechamos	o	modal.	
Agora	chamaremos	essa	função	através	do	botão	Pagar	e	sua	diretiva	ng-click.		
... 
<div class="col"> 
    <button type="button"  
            class="button button-positive button-block"  
            ng-click="pagar()"> 
        Pagar 
    </button> 
</div> 
... 
D e p o i s 	d e 	t u d o 	i m p l e m e n t a d o , 	c h e g o u 	a 	h o r a 	d e 	t e s t a r 	o 	f l u x o 	d a	 aplicação.	 Faça	 um	
pedido,	confirme‐o	depois	de	ser	inserido	na	bandeja	e	acesse	a	conta	para	pagar	parcial	ou	
totalmente,	como	também	efetuar	o	pedido	através	do	botão	 Fechar.	Se	tudo	ocorreu	bem	até	
aqui,	seu	aplicativo	está	pronto	e	nosso	caso	de	uso	chegou	ao	fim.	
8.4	Conclusão	
Neste	capítulo,	encerramos	nosso	caso	de	uso.	Ele	foi	implement ado	através	do	framework	
para	aplicações	híbridas:	 Ionic	versão	1.	Conhecemos	alguns	conceitos	básicos	sobre	toda	
tecnologia	 envolvida	 no	 framework, 	s e u s 	c o n c e i t o s 	e 	p e ç a s 	c h a v e s , 	a l é m 	d e 	u t i l i z a r m o s 	
muitos	componentes	CSS	que	o	próprio	Ionic	fornece.		
Temos	mais	dois	capítulos	pela	frente,	em	que	vou	explanar	o	us o	da	câmera	do	dispositivo	
através	da	instalação	do	plugin	do	 ngCordova	(capítulo	Usando	a	câmera),	e	falarei	de	mais	
alguns	recursos	que	poderemos	explorar	em	nossos	aplicativos	(capítulo	Recursos).		
E s p e r o 	q u e 	t e n h a 	g o s t a d o 	d o 	q u e 	v i u 	a t é 	a g o r a , 	e 	s e g u i r e m o s 	n e ssa	 viagem	 até	 o	 último	
capítulo.	

## Página 112

8.5	Para	saber	mais	
	
1. Forms	–	https://ionicframework.com/docs/components/#forms	
2. Lists	–	https://ionicframework.com/docs/components/#list	
3. Validações	AngularJS	–		
https://www.w3schools.com/angular/angular validation.asp	
 

## Página 113

CAPÍTULO	9	
Usando	a	câmera	
Neste	capítulo,	vamos	aprender	a	utilizar	um	dos	recursos	mais	 explorados	do	dispositivo:	
a 	c â m e r a . 	P a r a 	i s t o , 	v a m o s 	e s q u e c e r 	u m 	p o u c o 	o 	browser	 em	 relação	 aos	 testes	 da	
aplicação,	 pois	 o	 plugin	r e q u e r 	u m 	d i s p o s i t i v o 	r e a l , 	o u 	u m 	e m u l a d o r , 	p a r a 	e x e c u t a r 	a 	
aplicação	corretamente	utilizando	a	câmera.		
Portanto,	o	recurso	escolhido	para	testarmos	será	um	dispositivo	móvel:	de	preferência	um	
celular	ou	um	tablet	com	 Android.	Retornando	ao	capítulo	 Iniciando	nossa	aplicação,	vimos	
que	é	preciso	plugar	um	dispositivo	na	porta	USB,	e	assim	executar	o	comando	 run	para	que	
o	framework	faça	o	build	da	aplicação	e	instale	(no	dispositivo).		
9.1	Instalação	do	plugin	
Com	 a	 ascensão	 do	AngularJS	e 	d o 	Cordova, 	s u r g i u 	u m a 	c o l e ç ã o 	d e 	plugins	 para	 rodar	 na	
junção	 destas	 duas	 plataformas.	 Todos	 eles	 estão	 no	 site	 ngCordova,	 em	
http://ngcordova.com,	e	até	a	escrita	deste	livro	possuía	mais	de	70	plugins.		
O	 que	 estes	plugins	f a z e m 	é 	a p e n a s 	t r a z e r 	p a r a 	a 	l i n g u a g e m 	J a v a S c r i p t 	a 	p o s s i b i l i dade	 de	
utilizar	as	APIs	do	dispositivo,	como	câmeras,	GPS,	 filesystem,	touch	id,	entre	outros.	Tudo	
isto	sendo	implementado	em	poucas	linhas	de	código.		
Para	começar	a	usar	estes	recursos,	você	deve	instalar	o	 plugin	da	câmera	no	diretório	da	
a p l i c a ç ã o . 	A s s i m , 	u s e 	o 	c o m a n d o 	cordova plugin add cordova-plugin-camera.	 Ele	 faz	 parte	 dos	plugins	
disponíveis	em	ngCordova,	portanto,	precisamos	deste	recurso	também	instalado	em	nossa	
aplicação.		
O	 comando	 utilizado	 para	 isto	 é	 o	bower install ngCordova,	 ou	 seja,	 através	 do	 repositório	bower	
instalamos	 o	 ngCordova.	 Por	 fim,	 vamos	 importá‐lo	 na	 aplicação	 através	 do	 arquivo	
www/index html:	
... 
    <script src="lib/ngCordova/dist/ng-cordova.js"></scrip> 
    <script src="cordova.js"></script> 
... 
Certifique‐se	de	que	o	 cordova.js	esteja	importado	também	em	sua	aplicação,	conforme	linha	
de	código	anterior.	O	ngCordova	depende	desta	API	para	funcionar.	

## Página 114

C o m o 	n o s s o 	c a s o 	d e 	u s o 	d o 	C a r d á p i o 	M ó v e l 	f o i 	c o n c l u í d o 	n o 	c a p í tulo	 anterior,	
consideramos	 que	 o	 leitor	 já	 está	apto	 a	 construir	 uma	 aplicação	 nova,	 ou	 utilizar	 os	
conceitos	aprendidos	neste	capítulo,	reaproveitando	a	mesma	estrutura	do	aplicativo	
construído.		
9.2	Construção	de	artefatos	
Até	 aqui,	 nosso	 livro	 foi	 baseado	 em	 um	 caso	 de	 uso.	 Todas	 as	 f uncionalidades	 foram	
baseadas	em	dois	artefatos	principais:	a	tela	(view)	e	o	controller.	Nesta	funcionalidade,	não	
será	 diferente.	 Precisamos	 criar	 estes	 dois	 arquivos	 e	 construir	 a	 funcionalidade	 baseada	
neles.		
Através	do	arquivo	 www/js/app.js,	onde	configuramos	todos	os	 states	da	aplicação,	você	deve	
configurar	a	chamada	para	nossa	tela	que	será	baseada	no	seguinte	protótipo:	
	
Figura	9.1:	Protótipo	câmera	
	
	


## Página 115

Ufa!	 O	 pessoal	 do	design	 pegou	 leve	 dessa	 vez.	 O	 que	 precisamos	 é	 de	 apenas	 um	 ícone	
dentro	de	um	botão?	Estamos	até	desconfiados	deles,	não	é	mesmo?		
B o m ! 	E n t ã o , 	v a m o s 	l á . 	P a r a 	q u e 	o 	í c o n e 	f i q u e 	d e n t r o 	d e 	u m 	b o t ã o 	t ã o 	g r a n d e 	a s s i m , 	
precisamos	criá‐lo	maior.	Isto	só	é	possível	através	da	manipul ação	via	CSS.	Para	tal,	vamos	
criar	o	estilo	desta	tela	em	nosso	www/css/style.css,	que	refletirá	a	nossa	necessidade.	
... 
.bt-camera { 
    min-height: 200px; 
    max-height: 200px; 
    min-width: 80%; 
    max-width: 80%; 
} 
... 
Feito	isto,	estamos	construindo	uma	classe	que	determina	um	tamanho	mínimo	para	altura	
(min-height,	max-height)	 e	 largura	 (min-width,	max-width) . 	E s s a 	s e r á 	a 	b a s e 	d e 	n o s s o 	b o t ã o 	q u e 	t e r á 	
como	ícone	a	câmera	ilustrada	no	protótipo.		
Para	 isto,	 devemos	 construir	 um	 arquivo	 que	 chamaremos	 de	www/templates/camera html	e 	u m 	
estado	que	nos	levará	a	um	controle	 www/js/camera-controller.js.	Aqui	não	importa	como	o	leitor	
vai	 construir	 estes	 artefatos.	 Se	 forem	 feitos	 no	 projeto	 do	 Cardápio	 Móvel,	 lembre‐se	 de	
que	deverá	fazer	um	novo	 estado,	depois	um	novo	menu	e	chamar	a	 view	associada	a	um	
controller.		
Se	você	leu	o	livro	até	aqui,	não	terá	dificuldade	em	entender	 isto.	Caso	decida	fazer	tudo	
em	uma	nova	aplicação,	a	regra	será	basicamente	a	mesma.	Portan to,	vamos	aos	artefatos	
controller	e	view,	respectivamente.	
//Controller 
app.controller("CameraCtrl", function(){ 
}); 
<!-- View --> 
<ion-view title="Camera"> 
    <ion-content> 
        <div class="row"> 
            <div class="col col-offset-20"> 
                <button class="button bt-camera ion-camera"> 
                </button></div> 
        </div> 
    </ion-content> 
</ion-view> 

## Página 117

As	opções	devem	ser	passadas	em	formato	JSON,	ou	seja,	um	objeto	neste	formato.	Um	JSON	
nada	 mais	 é	 que	 um	 JavaScript	 Object	 Notation	 (Notação	 de	 Objetos	 JavaScript).	 Esta	
definição	dispensa	explicação,	basta	o	leitor	entender	que	os	o bjetos	JavaScript	podem	ser	
representados	de	várias	formas,	inclusive	como	JSON.	Verifique	no	exemplo	a	seguir:	
 var opcoes = { 
      quality: 50, 
      destinationType: Camera.DestinationType.DATA_URL, 
      sourceType: Camera.PictureSourceType.CAMERA, 
      allowEdit: true, 
      encodingType: Camera.EncodingType.JPEG, 
      popoverOptions: CameraPopoverOptions, 
      saveToPhotoAlbum: false, 
      correctOrientation:true 
    }; 
Todo	JSON	é	formatado	entre	chaves,	com	seus	parâmetros	definid os	no	seguinte	formato:	
[chave] : [valor]	e 	s e p a r a d o s 	p o r 	v í r g u l a . 	S a b e n d o 	d i s t o , 	v a m o s 	e m 	s e g u i d a 	u t i l izar	 estes	
parâmetros.	Ao	clicar	no	ícone	da	câmera	de	nosso	exemplo,	o	ap licativo	abrirá	a	opção	de	
tirar	 uma	 foto	 (sourceType)	 e	 a	 guardará	 em	 formato	 JPEG	encodingType,	 permitindo	 a	 edição	
após	execução	(allowEdit).		
Depois	 disto,	 exibiremos	 a	 foto	 que	 foi	 tirada	 e	 guardada	 em	 um	f o r m a t o 	base64.	 Este	
formato	 foi	 configurado	 com	 o	 parâmetro	 destinationType, 	a t r i b u i n d o 	o 	v a l o r 	
Camera.DestinationType.DATA_URL.	 Caso	 você	 prefira	 guardar	 em	 um	 arquivo,	 poderá	 utilizar	 a	
seguinte	 opção:	 destinationType: Camera.DestinationType.FILE_URI. 	P a r a 	q u e 	a 	e x i b i ç ã o 	s e j a 	p o s s í v e l , 	
vamos	inserir	uma	div	ao	html.	Veja	a	seguir	a	codificação	de	nossa	view:	
<ion-view title="Camera"> 
    <ion-content> 
        <div class="row"> 
            <div class="col col-offset-20"><button ng-click="tirarFoto()" class="button bt-camera ion-
camera" id="btCamera"><img id="minhaImagem" ></button></div> 
        </div> 
    </ion-content> 
</ion-view> 
Analisando	 melhor,	 podemos	 verificar	 a	 alteração	 do	 botão,	 em	 q u e 	e s t e 	r e c e b e 	u m a 	
diretiva	 ng-click=tirarFoto()	 e,	 logo	 em	 seguida,	 a	div	 que	 receberá	 a	 imagem.	 Portanto,	 vamos	
preparar	nosso	controller	com	o	seguinte	código:	
app.controller("CameraCtrl", function($scope){ 
 
    var options = { 
      quality: 50, 
      destinationType: Camera.DestinationType.DATA_URL, 

## Página 118

      sourceType: Camera.PictureSourceType.CAMERA, 
      allowEdit: true, 
      encodingType: Camera.EncodingType.JPEG, 
      popoverOptions: CameraPopoverOptions, 
      saveToPhotoAlbum: false, 
      correctOrientation:true 
    }; 
 
 
    $scope.tirarFoto = function(){ 
        $cordovaCamera 
            .getPicture(options) 
                .then(function(imageData) { 
        var image = document.getElementById('minhaImagem'); 
        image.src = "data:image/jpeg;base64," + imageData; 
 
        }, function(err) { 
          // error 
        }); 
    } 
}); 
Observe	 que	 usamos	 uma	 variável	 options	 onde	 informamos	 os	 principais	 parâmetros	
a p r e s e n t a d o s 	n a 	t a b e l a 	d o 	i n í c i o 	d e s t a 	s e ç ã o . 	A p ó s 	i s t o , 	c o n s t ruímos	 uma	 função	 que	
executará	 a	 chamada	 à	 câmera,	 passando	 os	 parâmetros	 e	 recebend o	 o	 resultado	 no	
callback	da	função	chamada	de	then.	
Este	callback	recebe,	através	de	uma	função,	a	imagem	capturada	na	câmera,	que	neste	caso	
estará	 em	 um	 formato	base64.	 Com	 o	 resultado	 neste	 retorno,	 vamos	 disponibilizá‐lo	 na	div	
que	 referenciamos	 através	 do	 document.getElementById('minhaImagem'). 	S e 	e x e c u t a r m o s 	e s t a 	
funcionalidade	no	browser,	encontraremos	o	seguinte	erro:	
	
Figura	9.2:	Erro	sem	câmera	
	


## Página 119

Isto	significa	que	chegamos	ao	nosso	limite	de	testes	de	aplica ções	através	do	 browser,	ou	
seja,	 o	 aplicativo	 está	 tentando	 encontrar	 um	 recurso	 que	 não	 existe	 no	 navegador.	 Para	
isto,	precisamos	utilizar	um	simulador,	ou	debugar	nossa	aplicação	em	um	dispositivo	real.		
E s t e 	c o m a n d o 	f o i 	e x p l a n a d o 	n o 	c a p í t u l o 	Iniciando	nossa	aplicação	e , 	c a s o 	o 	l e i t o r 	n ã o 	s e 	
lembre,	 poderemos	refrescar	sua	memória.	O	comando	é	o	 ionic run [plataforma],	e	a	plataforma	
pode	 ser	 Android,	 iOS	 etc.,	 dependendo	 de	 qual	 o	 desenvolvedor	 esteja	 utilizando	 e	
plugado	via	USB	em	seu	computador.		
Antes	de	executar	o	comando,	pre cisamos	injetar	o	recurso	em	no ssa	aplicação	e	em	nosso	
controller.	Abra	o	arquivo	www/js/app.js	e	injete	o	ngCordova	no	módulo	da	aplicação	assim:	
... 
angular module('starter', ['ionic', 'starter.controllers','ngNumberPicker', 'ngCordova']) 
... 
Agora	 a	 assinatura	 do	 nosso	controller	 receberá	 a	 injeção	 do	plugin	a t r a v é s 	d o 	s e g u i n t e 	
objeto:	
app.controller("CameraCtrl", function($cordovaCamera, $scope){ 
... 
Feito	isto,	você	já	pode	testar	a	câmera	e	ver	o	funcionamento	 deste	plugin.	Se	tudo	ocorreu	
bem	 até	 aqui,	 você	 verá	 a	 câmera	 ser	 chamada	 através	 do	 botão	 e, 	a o 	t i r a r 	u m a 	f o t o , 	o 	
a p l i c a t i v o 	p e r m i t i r á 	a 	s u a 	e d i ç ã o . 	P o s t e r i o r m e n t e , 	q u a n d o 	c o n f irmada,	 será	 exibida	 na	div	
que	incluímos	em	nossa	view.	
9.4	Conclusão	
E s t e 	c a p í t u l o 	f o i 	u m a 	i n t r o d u ç ã o 	à 	a d i ç ã o 	d e 	u m 	d o s 	m u i t o s 	plugins	 disponíveis	 no	
repositório	 ngCordova, 	e 	s e r v e 	c o m o 	b a s e 	p a r a 	o 	l e itor	 entender	 como	 é	 feita	 uma	
chamada	 a	 um	 recurso	 através	 desta	 instalação.	 Os	 demais	plugins	t r a b a l h a m 	d e 	f o r m a 	
similar,	e	basta	uma	ligeira	consulta	na	documentação	do	recurs o	para	entender	como	será	
feita	a	chamada	às	suas	funções.	
9.5	Para	saber	mais	
	
1. ngCordova	–	http://ngcordova.com	
2. Câmera	–	http://ngcordova.com/docs/plugins/camera	
 

## Página 120

CAPÍTULO	10	
Recursos	
Estamos	 chegando	 ao	 final	 de	 nosso	 livro,	 e	 este	 último	 capítul o	 será	 utilizado	 para	
fazermos	 uma	 miscelânea	 de	 recursos	 do	 Ionic	 Framework.	 Vamos	 consumir	 dados	
alocados	 na	 nuvem,	 e	 também	 uma	 lista	 mais	 avançada	 do	 que	 a	 vi sta	 no	 capítulo	 A	
bandeja.	 Conheceremos	 o	$ionicActionSheet,	 uma	 espécie	 de	 painel	 de	 opções	 que	 abre	 com	
efeito	slide‐up,	através	do	evento	click	de	um	botão.		
Faça	bom	proveito	destes	recursos	e	espero	que,	com	eles,	o	lei tor	tenha	uma	melhor	visão	
e	 possa	 ampliar	 assim	 seus	 conhecimentos,	 utilizando‐os	 em	 suas	a p l i c a ç õ e s . 	I n c l u s i v e , 	
você	poderá	fazer	melhorias	no	caso	de	uso	do	Cardápio	Móvel,	construído	neste	livro.	
10.1	O	Firebase	
Para	consumir	serviços	de	uma	base	de	dados	na	 web,	vamos	utilizar	o	 firebase	do	Google.	
E s te	rec u rs o 	é	u m a	b as e	q u e	s e	enc o ntra	n a	nu vem 	e	te m 	c o mo 	d iferencial	o	conceito	de	
real	time.	Isto	é,	tudo	o	que	for	atualizado	no	banco	de	dados	será	propagado	em	tempo	real	
para	sua	aplicação.		
Por	 exemplo,	 se	 a	 aplicação	 executar	 uma	 leitura	 de	 um	 registro	n o 	firebase	e 	d e 	a l g u m a 	
forma	estiver	"escutando"	este	registro,	quando	ele	for	alterado	por	outra	aplicação,	o	valor	
será	 atualizado	 sem	 necessidade	 de	 um	 novo	 ciclo	 de	 consulta	 ao	 banco	 de	 dados.	 Para	
visualizar	melhor	este	conceito,	imagine	um	 chat	onde	vários	usuários	enviam	mensagem	
d e 	f o r m a 	a s s í n c r o n a . 	A s s i m 	q u e 	u m 	u s u á r i o 	g r a v a 	n o 	b a n c o 	u m a 	m ensagem,	 todos	 as	
aplicações	que	estão	conectadas	no	firebase	receberão	a	atualização.		
Na	 verdade,	 o	 firebase	e n v i a 	a 	a t u a l i z a ç ã o 	n o 	s e n t i d o 	i n v e r s o 	d o 	q u e 	a c o n t e c e 	e m 	u m a 	
aplicação	 convencional.	 É	 uma	 espécie	 de	listener, 	e m 	q u e 	a 	a p l i c a ç ã o 	f i c a 	a g u a r d a n d o 	– 	
sem	precisar	fazer	consulta	–	qualquer	alteração	no	banco	de	dados.	
Obviamente	não	vamos	nos	aprofundar	na	criação	de	uma	base	no	 firebase,	pois	este	não	é	
o	foco	deste	capítulo,	no	entant o,	vou	disponibilizar	uma	base	 pronta	para	ser	consumida.	
Se	quiser	saber	mais	sobre	o	 firebase,	sugiro	que	consulta	a	seção	 Para	saber	mais.	Estamos	
prontos?!	
10.2	Consumindo	serviços	

## Página 121

Antes	 de	 tudo,	 precisamos	 instalar	 o	client	d o 	firebase,	 através	 do	bower. 	E m 	n o s s o 	c a s o , 	
devemos	 utilizar	 um	 suporte	 oficial	 do	AngularJS	 para	 executar	 as	 funções	 deste	 recurso.	
Vamos	ao	comando	para	instalação?!	
bower install angularfire --save 
Se	 você	 observar,	 serão	 instalados	 dois	 plugins	 em	 sua	 aplicação	 com	 este	 comando:	 o	
Angularfire	p r o p r i a m e n t e 	d i t o 	e 	a s 	A P I s 	d o 	firebase	 no	 diretório	lib	 de	 sua	 aplicação.	
Precisamos	 agora	 importá‐los	 em	 nosso	www/index html,	 para	 que	 seja	 possível	 injetar	 estes	
artefatos	na	aplicação.	Veja	a	seguir	o	resultado	da	instalação	e	a	importação	na	aplicação,	
respectivamente:	
	
Figura	10.1:	Conclusão	da	instalação	
	
... 
    <!-- Importação no arquivo www/index html --> 
    <script src="lib/angularfire/dist/angularfire.js"></script> 
    <script src="lib/firebase/firebase.js"></script> 
... 
Após	 a	 importação,	 vamos	 consumir	 três	 listas	 que	 estão	 disponí veis	 em	 https://livro-
ionic firebase.com.	Se	você	tentar	acessar	esta	 URL,	não	conseguirá,	ainda	que	faça	login	em	sua	
conta	Google.	Entretanto,	poderá	ler	o	banco	de	dados	que	está	na	seguinte	estrutura:	
	
Figura	10.2:	Lista	no	firebase	
	


## Página 122

Esta	imagem	o	faz	recordar	de	alguma	coisa?	Se	você	fez	o	dever 	de	casa	e	leu	o	livro	até	
a q u i , 	e s t a r á 	s e 	p e r g u n t a n d o : 	" S e r á 	q u e 	e u 	p o s s o 	c o n s u m i r 	e s t e s 	serviços	 para	 o	 meu	
cardápio	 e	 eliminar	 os	mocks	q u e 	c r i e i ? 	D e s s a 	f o r m a , 	e s t a r e i 	c o n s t r u i n d o 	u m 	a p l i c a t i v o 	
mais	próximo	da	realidade".	A	resposta	é:	você	não	só	pode,	como	deve!		
Vamos	entender	como	tudo	funcionará	com	o	firebase	e,	em	seguida,	você	poderá	transferir	
todo	conceito	para	o	cardápio	móvel.		
Com	tudo	pronto,	vamos	inicializar	o	firebase 	em	nossa	aplicação	pelo	arquivo	 www/js/app.js.	
E s t e 	é 	o 	m ó d u l o 	starter	 da	 aplicação,	 ou	 seja,	 é	 a	 localização	 global	 para	 criar,	 registrar	 e	
recuperar	 módulos	 do	 AngularJS.	 Portanto,	 vamos	 registrar	 (ou	 inicializar)	 as	
configurações	firebase,	dentro	da	função	run()	e	$ionicPlatform ready().	
... 
run(function($ionicPlatform) { 
  $ionicPlatform.ready(function() { 
    // Hide the accessory bar by default (remove this to show the accessory bar above the keyboard 
    // for form inputs) 
 
    // Initialize Firebase 
    var config = { 
        apiKey: "AIzaSyAV6AVt9iTDoa5Rla_xbrNO7EDjcRzSrmA", 
        authDomain: "livro-ionic firebaseapp.com", 
        databaseURL: "https://livro-ionic.firebaseio.com" 
    }; 
    firebase.initializeApp(config); 
... 
Observe	que	estas	configurações	são	específicas	do	banco	de	dad os	que	foi	disponibilizado	
para	o	leitor	deste	livro.	Portanto,	tudo	pode	mudar	de	acordo	 com	o	banco	que	você	criar.	
Temos	 aí	 uma	 chave	apiKey	 (que	 nada	 mais	 é	 do	 que	 um	 identificador	 dentro	 da	 base	 de	
dados)	e,	em	seguida,	o	domínio	e	a	URL.		
Depois,	 inicializamos	 de	 fato	 o	 banco	 com	 a	 chamada	 a	 initializeApp,	 passando	 como	
parâmetro	 as	 configurações.	 Feito	 isto,	 já	 podemos	 utilizar	 o	 firebase	 dentro	 de	 nossa	
aplicação	para	consultar,	setar	e	escutar	valores	na	nuvem.	Por ém,	em	nosso	caso,	o	leitor	
só	terá	a	permissão	para	consulta.	Utilize	um	controller	com	a	seguinte	chamada:	
var ref = firebase.database() 
                ref("/bebidas") 
                    .once("value",function(valor){ 
        console.log(valor.val()); 
}); 
Chame	este	 controller	e	observe	o	console	no	 browser.	Você	vai	observar	que	estão	sendo	
retornados	os	três	valores	do	array	das	bebidas,	similar	à	figura	a	seguir:	

## Página 123

	
Figura	10.3:	Objetos	retornados	
	
Entendendo	o	código,	temos	na	primeira	linha	uma	variável	que	g uardará	a	referência	do	
banco,	de	acordo	com	as	configurações	que	fizemos	ao	inicializa r	a	aplicação	( database()).	Em	
seguida,	demos	ao	database()	a	referência	que	queremos	dentro	do	banco:	/bebidas.		
Chamamos	 assim	 a	 função	once()	c o m 	o 	p a r â m e t r o 	value, 	i n f o r m a n d o 	q u e 	q u e r e m o s 	" t i r a r 	
u m a 	f o t o " , 	o u 	s e j a , 	p e g a r 	o s 	d a d o s 	u m a 	s ó 	v e z 	n o 	firebase. 	I s t o 	s i g n i f i c a 	q u e 	o 	a p l i c a t i v o 	
busca	na	nuvem	a	lista	de	bebidas	e,	mesmo	que	ela	seja	atualiz ada,	nada	acontecerá	mais	
nesta	lista	local	até	que	se	faça	uma	nova	consulta.		
Isto	entra	em	contradição	com	o	que	foi	dito	sobre	o	firebase	no	início	deste	capítulo,	não	é?	
S i m ! 	M a s , 	c o m o 	e s t a m o s 	f a z e n d o 	u m a 	f u n c i o n a l i d a d e 	s o m e n t e 	d e 	c onsulta,	 resolvemos	
fazer	desta	forma.	Caso	o	leitor	queira	aprender	mais	sobre	as	 atualizações	citadas,	poderá	
se	 aprofundar	 na	 documentação	 do	 link	 disponível	 na	 seção	 Para	 saber	 mais	s o b r e 	o 	
firebase.		
A g o r a 	v a m o s 	e n t e n d e r 	o 	q u e 	a 	f u n ç ã o 	d e 	callback	 faz.	 Ela	 simplesmente	 recebe	 um	 valor	
que	 é	 acessível	 através	 da	 função	val(). 	P o r 	f i m , 	a 	f u n ç ã o 	console()	d o 	J a v a S c r i p t 	i m p r i m e 	o s 	
o b j e t o s 	r e c e b i d o s . 	T e s t e 	e 	o b s e r v e 	a 	l i s t a 	s e n d o 	r e t o r n a d a . 	F e i t o 	i s t o , 	b r i n q u e 	u m 	p o u c o 	
com	 as	 listas,	 modificando	 apenas	 a	 referência	 ( ref)	 com	 seus	 respectivos	 parâmetros:	
"/petiscos"	e	"/sucos".	
10.3	O	cardápio	modificado	
Agora	que	você	já	sabe	como	chamar	um	serviço	na	nuvem	utilizan do	o	 firebase,	podemos	
modificar	nosso	caso	de	uso	para	que,	em	vez	de	utilizar	 mocks,	passe	a	consumir	serviços,	
de	fato.	
Para	executar	estas	chamadas	no	Cardápio	Móvel,	precisamos	apenas	modificar	o	controller	
para	o	seguinte	código:	


## Página 124

app.controller('BebidasCtrl', function($scope, Sessao, CardapioServices,$firebaseObject,$ionicLoading){ 
$ionicLoading.show({ 
    template: 'Carregando...' 
}).then(function(){ 
    $scope.bebidas  = []; 
}); 
 
var ref = firebase.database() ref("/petiscos").once("value",function(valor){ 
    $ionicLoading hide().then(function(){ 
       $scope.bebidas = valor.val(); 
    }); 
}); 
 
}); 
Ops!	Algo	novo	aconteceu	aqui.	Veja	que	injetamos	o	 $ionicLoading.	Este	objeto	é	uma	tela	de	
espera	 do	Ionic	q u e 	é 	b a s t a n t e 	u t i l i z a d a 	p a r a 	c o n s u m o 	d e 	s e r v i ç o s 	e 	p r o c e s s a m entos.	 Ele	
contém	duas	funções	básicas:	show()	e	hide().	
A	 primeira	 exibe	 o	 template	 que	 for	 determinado	 pelo	 desenvolvedor.	 Em	 nosso	 caso,	
apenas	exibiremos	a	mensagem	"Carregando..."	e	inicializamos	a	 variável	$scope.bebidas	vazia.	
Após	 executar	 o	 once()	d o 	 firebase, 	n o t e 	q u e 	f e c h a m o s 	a 	t e l a 	d e 	e s p e r a 	c o m 	o 	hide()	e 	
referenciamos	 em	 $scope.bebidas	 o	 valor	 que	 foi	 recuperado.	 Assim	 exibiremos	 na	 view	d e 	
nossa	aplicação.		
Portanto,	o	$ionicLoading	é	um	excelente	componente	para	consultas	assíncronas	pelo	 Ionic.	A	
estratégia	é	simples:		
	
1. Fazer	uma	consulta	no	webservice;	
2. Abrir	a	tela	de	espera	com	o	$ionicLoading;	
3. E n q u a n t o 	o 	s e r v i ç o 	n ã o 	é 	r e t o r n a d o 	a t r a v é s 	d a 	promise	 once(), 	a 	t e l a 	e x i b i r á 	a 	
mensagem	de	"Carregando...";	
4. Ao	retornar,	dentro	da	promise,	fechamos	a	tela	de	espera	 $ionicLoading	e	exibimos	
os	dados.	
PROMISE,	segundo	o	site	da	 Mozzila	Foundation,	é	uma	promessa	em	JavaScript,	ou	seja,	
um	 objeto	 usado	 para	 processamento	 assíncrono.	 Ele	 representa	 um	 valor	 que	 pode	
estar	 disponível	 agora,	 no	 futur o	 ou	 nunca.	 Se	 quiser	 saber	 mais	 sobre	 promise,	
consulte	https://developer.mozilla.org/pt‐BR/docs/Web/JavaScript/Reference.	

## Página 125

A g o r a 	q u e 	v o c ê 	e n t e n d e u 	c o m o 	c o n s u m i r 	a s 	l i s t a s 	n a 	n u v e m , 	d e i x arei	 a	 seu	 critério	 a	
modificação	 dos	 outros	 itens,	 eliminando	 assim	 os	 mocks	 construídos	 em	
www/js/services/cardapio-services.js.	
10.4	ionicList	
Vamos	agora	nos	aprofundar	mais	nas	listas	do	 Ionic.	Este	componente	é	bastante	utilizado	
em	aplicações	nas	quais	há	necessidade	de	exibir	muitos	elementos	em	um	grid.	Para	isto,	o	
framework	nos	oferece	o	componente	 $ionicList	com	muitas	possibilidades	de	manipulações	
dos	elementos	na	lista.		
Lembra	da	nossa	bandeja,	na	qual	 tínhamos	a	possibilidade	de	ed ição	e	exclusão	dos	itens?	
Pois	bem!	Poderíamos	ter	feito	tudo	muito	mais	elegante	se	tivé ssemos	iniciado	o	livro	de	
trás	para	a	frente,	porém,	deixei	isto	por	último	para	que	você 	aprendesse	o	"algo	a	mais"	
do	framework.		
Sim!	Reinventamos	a	roda	quando	c onstruímos	botões	para	edição	 e	remoção	dos	itens	da	
lista.	 Além	 disto,	 o	 pessoal	 de	design	n ã o 	i m a g i n o u 	q u e 	n o s s o s 	c o m p o n e n t e s 	f a r i a m 	b o a 	
parte	deste	trabalho.	Agora	vamos	de	fato	usar	a	"roda"	mais	elegante.	O	problema	disto	é	
convencer	os	designers	a	reconstruir	o	comportamento	desta	lista.	
Vamos	fazer	como	na	seção	anterior,	em	que	construímos	um	exemp lo	e,	a	partir	daí,	fica	a	
critério	 do	 leitor	 transferir	 o	 conceito	 para	 o	 Cardápio	 Móvel.	 Consumiremos	 o	 mesmo	
serviço	disponível	em	 https://livro-ionic.firebaseio.com	para	demonstração	desta	lista.	Utilizaremos	
para	isto	a	lista	bebidas.	
O	controller	conterá	agora	o	seguinte	trecho	de	código:	
... 
$scope.data = { 
    showDelete: false 
}; 
$scope.onItemDelete = function(item) { 
    $scope.bebidas.splice($scope.bebidas.indexOf(item), 1); 
}; 
... 
O	que	fizemos	foi	declarar	um	objeto	que	receberá	o	estado	inic ial	false.	Ele	será	explicado	e	
melhor	 entendido	 quando	 construirmos	 a	 view.	 Em	 seguida,	 temos	 uma	 função	 que	
receberá	um	item	para	ser	excluído	pelo	 splice(index, quant),	já	explicada	no	capítulo	 A	bandeja.	
Feito	isto,	vamos	partir	para	a	view:		
... 
<div class="buttons"> 

## Página 126

   <button class="button button-icon icon ion-ios-minus-outline" 
      ng-click="data.showDelete = !data.showDelete"></button> 
</div> 
<ion-list  show-delete="data.showDelete"> 
    <ion-item ng-repeat="bebida in bebidas" href="#/app/detalhar/{{bebida.id}}"> 
        <ion-delete-button class="ion-minus-circled"  
                 ng-click="onItemDelete(bebida)"> 
            </ion-delete-button> 
        {{bebida nome}} - {{bebida.preco.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL'})}} 
     </ion-item> 
</ion-list> 
... 
N e l a 	é 	p o s s í v e l 	o b s e r v a r 	u m 	b o t ã o 	p a r a 	e x i b i r 	a 	l i s t a 	c o m 	i t e n s	 removíveis,	 ou	 seja,	 este	
botão	ficará	no	topo	da	página,	antes	da	lista.	Ele	tem	como	 data‐binding	o	data.showDelete	que	
declaramos	no	controller,	lembra?		
Veja	que,	ao	clicar	neste	botão	com	a	diretiva	 ng-click,	o	estado	da	variável	 showDelete	receberá	
a	negação	do	valor	atual.	Ou	seja,	se	for	true	se	tornará	false,	e	vice‐versa.		
Logo	abaixo,	a	lista	recebe	duas	novidades:	show-delete	e	<ion-delete-button>.	O	show-delete	configura	a	
lista	para	abrir	os	botões	de	 delete	construídos	com	o	 <ion-delete-button>,	dentro	de	cada	item.	
Nele	 está	 configurada	 a	 exibição	 do	 ícone	 com	 o	 sinal	 de	 menos	(-)	 que	 executará	 uma	
função,	construída	no	controller,	passando	assim	a	bebida	como	parâmetro.		
Na	figura	a	seguir,	é	possível	ver	exemplo	desta	ação	sendo	exe cutada.	À	esquerda,	o	botão	
de	m eno s	a inda	n ão 	fo i	c l ic ado 	e,	à	dire ita,	te m o s	o 	resu ltado 	do	clique	neste	botão.	Faça	
um	teste	e	aproveite	para	modificar	o	Cardápio	Móvel	(na	bandeja	do	capítulo	A	bandeja).		
	
Figura	10.4:	Lista	turbinada	
	
	


## Página 127

10.5	O	ionicActionSheet	
O	 Action	Sheet	s e r á 	n o s s o 	ú l t i m o 	r e c u r s o 	a 	s e r 	d e m o n s t r a d o . 	E l e 	é 	a p e n a s 	u m 	painel	 de	
opções	que	rola	de	baixo	para	cima	( slide‐up),	sem	tomar	a	tela	por	completo.	Com	certeza,	
muitos	já	se	depararam	com	este	componente	em	aplicativos	que	c ompartilham	algum	tipo	
de	conteúdo.	
A o 	c l i c a r 	n o 	r e c u r s o 	a 	s e r 	c o m p a r t i l h a d o , 	e s t e 	e x i b e 	u m a 	Action	 Sheet	 para	 escolha	 do	
aplicativo.	Veja	a	seguir	seu	formato:	
	
Figura	10.5:	Action	Sheet	
	
A	figura	nos	diz	que	este	 Action	Sheet	foi	criado	para	modificar	um	álbum,	sendo	possível 	
executar	as	seguintes	ações:	Compartilhar,	Mover	ou	Excluir.		
Vamos	incrementar	em	nossa	lista	um	botão	de	compartilhar.	O	co mportamento	seguirá	o	
seguinte	fluxo:	
	
1. Ao 	desl izar 	o 	dedo 	so bre	u m 	item 	da	direi ta	p ara	a	esq u erda,	se rá	e xib ido 	u m	
botão	Compartilhar;	
2. Ao	clicar	neste	botão,	abrirá	nosso	Action	Sheet	com	dois	botões:	WhatsApp,	E-mail.		
Para	isto,	execute	na	lista	construída	anteriormente	a	seguinte	modificação:	
... 
<ion-list  show-delete="data.showDelete"> 
    <ion-item ng-repeat="bebida in bebidas" href="#/app/detalhar/{{bebida.id}}"> 
        <ion-delete-button class="ion-minus-circled"  
                 ng-click="onItemDelete(bebida)"> 
        </ion-delete-button> 


## Página 128

        <ion-option-button class="button-calm" ng-click="abrirActionSheet()">Compartilhar</ion-option-button> 
        {{bebida nome}} - {{bebida.preco.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL'})}} 
     </ion-item> 
</ion-list> 
... 
Perceba	 que	 só	 colocamos	 um	 botão	 a	 mais:	 o	 <ion-option-button>	 com	 a	 diretiva	 ng-click	
chamando	a	função	abrirActionSheet(),	que	construiremos	no	controller	logo	a	seguir:	
... 
$scope.abrirActionSheet = function(){ 
    $ionicActionSheet.show({ 
     buttons: [ 
       { text: 'Whatsapp' }, 
       { text: 'Email' } 
     ], 
     buttonClicked: function(index) { 
       return true; 
     } 
    }); 
  } 
... 
Não	 se	 esqueça	 de	 injetar	 o	 $ionicActionSheet	e m 	s e u 	controller.	 O	 que	 fizemos	 foi	 apenas	
configurar	 o	 nosso	 componente	 com	 dois	 botões	 (buttons):	 um	 WhatsApp	 e	 outro	 E‐mail.	 A	
função	 buttonClicked	 é	 executada	 toda	 vez	 que	 algum	 botão,	 de	 fato,	 é	 acionado.	 Aqui	 você	
poderia	fazer	sua	regra	de	negócio,	sabendo	em	qual	botão	o	usu ário	clicou	através	do	 index	
que	é	passado	como	parâmetro.		
Tudo	pronto	para	teste.	Fica	aqui	o	desafio	para	você	colocar	u m	botão	ao	deslizar	o	dedo	
sobre	um	item,	onde	o	mesmo	substitua	a	função	de	Editar	do	cap ítulo	A	bandeja,	para	que	
os	itens	da	lista	de	bandeja	sofram	esta	ação.	Boa	sorte!	
10.6	Dialog	do	ngCordova	
Em	nosso	 caso	de	uso	do	cardápio,	fizemos	uma	bandeja,	na	qual	o	usuário	adiciona	vários	
itens	 antes	 de	 confirmar	 estes	 pedidos,	 permitindo	 que	 se	 volte	 várias	 vezes	 e	 edite	 ou	
r e m o v a 	e s t e s 	i t e n s . 	A o 	f a z e r 	a 	f u n c i o n a l i d a d e 	d e 	r e m o v e r 	n o 	c a pítulo	 Fazendo	 pedidos,	
deixamos	de	lado	o	modal	de	confirmação,	ou	seja,	o	usuário	dev eria	clicar	em	remover	um	
item.	 Mas	 antes	 de	 executar	 a	 função,	 o	 aplicativo	 abrirá	 uma	 tela	 de	 confirmação	 desta	
ação.		

## Página 129

Esta	 função	 pode	 ser	 construída	 através	 da	 adição	 do	plugin	 dialog	 do	 ngCordova,	 com	 o	
seguinte	 comando:	 cordova plugin add cordova-plugin-dialogs.	 Feito	 isto,	 é	 preciso	 refazer	 a	 função	
removerItem()	do	www\js\controllers.js.		
Primeiro	precisamos	injetar	o	plugin	recentemente	instalado	dentro	do	controller:	
app.controller('AppCtrl', function($scope, Sessao,  
                $ionicModal, $cordovaDialogs) {... 
Agora	 é	 só	 inserir	 um	dialog	 na	 função	 que	 está	 sendo	 chamada	 pelo	 botão	 de	 remoção.	
Este	dialog	deverá	conter	dois	botões	(Cancelar	e	OK)	mais	uma	mensagem	de	confirmação.	
Ao	clicar	em	OK,	o	dialog	deverá	efetuar	um	teste	para	executar	a	remoção	que	estava	sendo	
feita	antes,	ou	ignorar	fechando	o	 dialog	se	acaso	o	usuário	escolher	o	botão	 Cancelar.	Veja	o	
código	a	seguir:	
... 
//Remoção 
$scope removerItem = function(){ 
    $cordovaDialogs.confirm('Deseja realmente remover este item?',  
        'Remoção', ['Cancelar','OK']) 
        .then(function(buttonIndex) { 
            'Cancelar' = 0, 'OK' = 1 
            var btnIndex = buttonIndex; 
            if( btnIndex == 1){ 
                Sessao.bandeja.splice($scope.data.item,1); 
             } 
}); 
... 
A n a l i s a n d o 	o 	c ó d i g o , 	v e m o s 	q u e 	o 	$cordovaDialogs.confirm()	 contém	 3	 parâmetros:	 uma	
mensagem,	 um	 título	 e	 um	array	 de	 botões,	 respectivamente.	 Ao	 clicar	 em	 um	 botão,	 a	
promise	then()	pega	a	referência	do	botão	(ou	seja,	seu	index)	e	testa.	Se	for	igual	a	1,	a	função	
executa	a	remoção	do	item	da	ban deja.	Ao	contrário,	se	o	usuári o	clicar	em	cancelar	(index = 
0),	nada	acontecerá,	exceto	o	fechamento	do	dialog.	
10.7	Conclusão	
Bem,	 caros	 colegas,	 chegamos	 ao	 final	 deste	 livro!	 Espero	 ter	 c ontribuído	 para	 a	
disseminação	do	conhecimento,	alg o	muito	importante	na	área	de	 tecnologia.	Ao	longo	dos	
c a p í t u l o s , 	a p r e n d e m o s 	u m 	p o u c o 	d e 	c a d a 	c o i s a . 	É 	o 	q u e 	c h a m a m o s 	de	 overview	d o 	
framework.		
Através	desta	leitura,	aprendemos	desde	a	criação	do	ambiente	e 	criação	de	nova	aplicação	
até	 a	 utilização	 de	 recursos	 do	 dispositivo.	 Com	 isto,	 passamos 	 pela	 maioria	 dos	

## Página 130

componentes	 usados	 em	 um	 aplicativo	 através	 do	 Ionic	 Framework,	 deixando	 assim	
algumas	dicas	para	que	o	leitor	tenha	uma	experiência	mais	apro fundada	através	da	leitura	
da	sua	documentação	oficial.	
Somente	a	partir	disto,	o	leitor	poderá	agregar	mais	conhecimento	e	experiência	com	esta	
ferramenta	 poderosa	 que	 é	 o	Ionic	Framework.	 Toda	 sua	 documentação	 está	 disponível	 e	
citada	 em	 cada	 seção	Para	 saber	 mais	 dos	 capítulos.	 Portanto,	 é	 importante	 a	 consulta	
sempre	que	necessário.	
Participe	 também	 das	 comunidades	 referentes	 ao	 assunto	 e	 tire	 d úvidas	 com	
desenvolvedores	 mais	 experientes .	 O	 meu	 desejo	 é	 que	 você	 tenha 	t i d o 	u m 	ó t i m o 	
a p r e n d i z a d o 	c o m 	e s t e 	l i v r o 	e 	q u e 	d ê 	c o n t i n u i d a d e 	s e 	a p r o f u n d a n do 	n a 	b u s c a 	d e 	n o v o s 	
conhecimentos	sobre	o	framework,	já	que	ele	disponibiliza	uma	infinidade	de	componentes	
que	não	foram	explorados	aqui.	
10.8	Para	saber	mais	
	
1. Angularfire	–	https://github.com/firebase/angularfire	
2. Documentação	do	Firebase	–	https://firebase.google.com/docs	
3. Action	Sheet	–		
http://ionicframework.com/docs/v1/api/service/$ionicActionSheet	