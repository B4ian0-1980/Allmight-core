---json
{
  "id": "documentacao_html_css",
  "title": "Documentação HTML5 + CSS3 — Guia Completo",
  "categoria": "04-frameworks",
  "subcategoria": "react",
  "resumo": "**Fonte:** [W3Schools HTML](https://www.w3schools.com/html/default.asp) · [W3Schools CSS](https://www.w3schools.com/css/default.asp) · [MDN Web Docs](https://developer.mozilla.org/) **Versão:** HTML5 / CSS3+",
  "gatilhos": [
    "completo",
    "css",
    "css3",
    "documentacao",
    "frameworks",
    "guia",
    "html",
    "html5"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação HTML5 + CSS3 — Guia Completo?",
    "Quais as boas praticas de react?"
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
  "dono": "stack-react",
  "prioridade": 2
}
---

# Documentação HTML5 + CSS3 — Guia Completo

> **Fonte:** [W3Schools HTML](https://www.w3schools.com/html/default.asp) · [W3Schools CSS](https://www.w3schools.com/css/default.asp) · [MDN Web Docs](https://developer.mozilla.org/)
> **Versão:** HTML5 / CSS3+
> **Atualizado:** 2026-02-14

---

## Sumário

1. [HTML Fundamentos](#html-fundamentos)
2. [Elementos e Semântica](#elementos-e-semântica)
3. [Formulários](#formulários)
4. [Mídia e Gráficos](#mídia-e-gráficos)
5. [APIs HTML5](#apis-html5)
6. [CSS Fundamentos](#css-fundamentos)
7. [Box Model e Layout](#box-model-e-layout)
8. [Flexbox](#flexbox)
9. [Grid](#grid)
10. [Responsividade](#responsividade)
11. [Animações e Transições](#animações-e-transições)
12. [CSS Avançado](#css-avançado)
13. [Boas Práticas](#boas-práticas)

---

## HTML Fundamentos

### Estrutura Base

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Descrição da página">
  <title>Minha Página</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>...</header>
  <main>...</main>
  <footer>...</footer>
  <script src="app.js"></script>
</body>
</html>
```

### Tags Essenciais

| Tag | Uso |
|---|---|
| `<h1>` a `<h6>` | Títulos (1 `<h1>` por página) |
| `<p>` | Parágrafos |
| `<a href="url">` | Links |
| `<img src="" alt="">` | Imagens (alt obrigatório) |
| `<ul>`, `<ol>`, `<li>` | Listas |
| `<div>` | Container genérico (block) |
| `<span>` | Container genérico (inline) |
| `<br>` | Quebra de linha |
| `<hr>` | Linha horizontal |
| `<strong>`, `<em>` | Negrito semântico, itálico semântico |

### Atributos Globais

| Atributo | Uso |
|---|---|
| `id` | Identificador único |
| `class` | Classes CSS |
| `style` | CSS inline |
| `title` | Tooltip |
| `data-*` | Dados customizados |
| `hidden` | Oculta o elemento |
| `tabindex` | Ordem de tabulação |
| `lang` | Idioma do conteúdo |

---

## Elementos e Semântica

### Elementos Semânticos HTML5

```html
<header>    <!-- Cabeçalho da página ou seção -->
<nav>       <!-- Navegação principal -->
<main>      <!-- Conteúdo principal (1 por página) -->
<article>   <!-- Conteúdo independente (blog post, notícia) -->
<section>   <!-- Seção temática do conteúdo -->
<aside>     <!-- Conteúdo lateral (sidebar) -->
<footer>    <!-- Rodapé -->
<figure>    <!-- Imagem com legenda -->
<figcaption><!-- Legenda da figure -->
<details>   <!-- Seção expansível -->
<summary>   <!-- Título do details -->
<mark>      <!-- Texto destacado -->
<time>      <!-- Data/hora semântica -->
```

### Tabelas

```html
<table>
  <caption>Título da Tabela</caption>
  <thead>
    <tr>
      <th>Coluna 1</th>
      <th>Coluna 2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Dado 1</td>
      <td>Dado 2</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td colspan="2">Rodapé</td>
    </tr>
  </tfoot>
</table>
```

---

## Formulários

```html
<form action="/api/submit" method="POST">
  <!-- Texto -->
  <label for="nome">Nome:</label>
  <input type="text" id="nome" name="nome" required placeholder="Seu nome">

  <!-- Email -->
  <input type="email" name="email" required>

  <!-- Senha -->
  <input type="password" name="senha" minlength="8">

  <!-- Número -->
  <input type="number" name="idade" min="0" max="120">

  <!-- Data -->
  <input type="date" name="nascimento">

  <!-- Telefone -->
  <input type="tel" name="tel" pattern="[0-9]{11}">

  <!-- URL -->
  <input type="url" name="site">

  <!-- Textarea -->
  <textarea name="bio" rows="4" cols="50" maxlength="500"></textarea>

  <!-- Select -->
  <select name="estado">
    <option value="">Selecione...</option>
    <optgroup label="Sudeste">
      <option value="SP">São Paulo</option>
      <option value="RJ">Rio de Janeiro</option>
    </optgroup>
  </select>

  <!-- Checkbox -->
  <input type="checkbox" id="termos" name="termos" required>
  <label for="termos">Aceito os termos</label>

  <!-- Radio -->
  <input type="radio" name="genero" value="M"> Masculino
  <input type="radio" name="genero" value="F"> Feminino

  <!-- File -->
  <input type="file" name="foto" accept="image/*" multiple>

  <!-- Range -->
  <input type="range" name="volume" min="0" max="100">

  <!-- Color -->
  <input type="color" name="cor" value="#ff0000">

  <!-- Hidden -->
  <input type="hidden" name="token" value="abc123">

  <!-- Submit -->
  <button type="submit">Enviar</button>
  <button type="reset">Limpar</button>
</form>
```

### Atributos de Validação

| Atributo | Função |
|---|---|
| `required` | Campo obrigatório |
| `minlength` / `maxlength` | Tamanho mín/máx de texto |
| `min` / `max` | Valores mín/máx numéricos |
| `pattern` | Regex de validação |
| `placeholder` | Texto de orientação |
| `autocomplete` | Sugestão automática |
| `autofocus` | Foco ao abrir a página |
| `disabled` | Desabilita o campo |
| `readonly` | Somente leitura |

---

## Mídia e Gráficos

```html
<!-- Imagem responsiva -->
<picture>
  <source media="(min-width: 800px)" srcset="grande.webp">
  <source media="(min-width: 400px)" srcset="medio.webp">
  <img src="pequeno.webp" alt="Descrição" loading="lazy">
</picture>

<!-- Vídeo -->
<video controls width="640" poster="thumb.jpg" preload="metadata">
  <source src="video.mp4" type="video/mp4">
  <source src="video.webm" type="video/webm">
  Seu navegador não suporta vídeo.
</video>

<!-- Áudio -->
<audio controls>
  <source src="audio.mp3" type="audio/mpeg">
  <source src="audio.ogg" type="audio/ogg">
</audio>

<!-- Canvas -->
<canvas id="myCanvas" width="400" height="300"></canvas>

<!-- SVG inline -->
<svg width="100" height="100">
  <circle cx="50" cy="50" r="40" fill="#3498db" />
</svg>

<!-- Iframe -->
<iframe src="https://example.com" width="600" height="400"
        loading="lazy" sandbox="allow-scripts"></iframe>
```

---

## APIs HTML5

```javascript
// Geolocation
navigator.geolocation.getCurrentPosition(pos => {
  console.log(pos.coords.latitude, pos.coords.longitude);
});

// LocalStorage / SessionStorage
localStorage.setItem('chave', 'valor');
const v = localStorage.getItem('chave');
localStorage.removeItem('chave');
localStorage.clear();

// Web Workers
const worker = new Worker('worker.js');
worker.postMessage('start');
worker.onmessage = e => console.log(e.data);

// Drag and Drop
element.draggable = true;
element.addEventListener('dragstart', e => e.dataTransfer.setData('text', e.target.id));
dropZone.addEventListener('drop', e => { /* ... */ });

// Fetch API
const res = await fetch('/api/data');
const data = await res.json();
```

---

## CSS Fundamentos

### Seletores

```css
/* Elemento */          p { }
/* Classe */            .card { }
/* ID */                #header { }
/* Descendente */       nav a { }
/* Filho direto */      ul > li { }
/* Irmão adjacente */   h2 + p { }
/* Irmão geral */       h2 ~ p { }
/* Atributo */          input[type="email"] { }
/* Pseudo-classe */     a:hover { }  a:nth-child(2n) { }
/* Pseudo-elemento */   p::first-line { }  p::before { content: "→"; }
/* Universal */         * { }
/* Agrupamento */       h1, h2, h3 { }
```

### Especificidade (precedência)

| Nível | Seletor | Peso |
|---|---|---|
| 1 | `!important` | ∞ |
| 2 | Inline `style=""` | 1000 |
| 3 | `#id` | 100 |
| 4 | `.class`, `[attr]`, `:pseudo` | 10 |
| 5 | `element`, `::pseudo` | 1 |
| 6 | `*` (universal) | 0 |

### Unidades

| Unidade | Tipo | Base |
|---|---|---|
| `px` | Absoluta | Pixel |
| `em` | Relativa | Font-size do pai |
| `rem` | Relativa | Font-size do root |
| `%` | Relativa | Dimensão do pai |
| `vw` / `vh` | Relativa | Viewport width/height |
| `vmin` / `vmax` | Relativa | Menor/maior viewport |
| `ch` | Relativa | Largura do "0" |
| `fr` | Fração | Grid fraction |

---

## Box Model e Layout

```css
/* Box Model */
.box {
  width: 300px;
  padding: 20px;           /* Espaço interno */
  border: 1px solid #ccc;  /* Borda */
  margin: 10px;            /* Espaço externo */
  box-sizing: border-box;  /* Width inclui padding+border */
}

/* Display */
display: block;       /* Ocupa toda a linha */
display: inline;      /* Ocupa só o conteúdo */
display: inline-block;/* Inline com width/height */
display: none;        /* Remove do fluxo */
display: flex;        /* Flex container */
display: grid;        /* Grid container */

/* Position */
position: static;     /* Padrão */
position: relative;   /* Relativo à posição original */
position: absolute;   /* Relativo ao ancestral posicionado */
position: fixed;      /* Relativo à viewport */
position: sticky;     /* Combina relative + fixed */

/* Float (legado — use Flexbox/Grid) */
float: left | right;
clear: both;
```

---

## Flexbox

```css
/* Container */
.flex-container {
  display: flex;
  flex-direction: row | column | row-reverse | column-reverse;
  justify-content: flex-start | center | flex-end | space-between | space-around | space-evenly;
  align-items: stretch | center | flex-start | flex-end | baseline;
  align-content: stretch | center | flex-start | flex-end | space-between;
  flex-wrap: nowrap | wrap | wrap-reverse;
  gap: 16px;
}

/* Items */
.flex-item {
  flex: 1;               /* flex-grow: 1, flex-shrink: 1, flex-basis: 0 */
  flex-grow: 2;          /* Proporção de crescimento */
  flex-shrink: 0;        /* Não encolhe */
  flex-basis: 200px;     /* Tamanho base */
  align-self: center;    /* Override do align-items */
  order: -1;             /* Reordenar */
}
```

### Padrões Úteis

```css
/* Centralizar perfeitamente */
.center { display: flex; justify-content: center; align-items: center; }

/* Navbar responsiva */
.nav { display: flex; justify-content: space-between; align-items: center; }

/* Card grid com wrap */
.cards { display: flex; flex-wrap: wrap; gap: 1rem; }
.card { flex: 1 1 300px; }
```

---

## Grid

```css
/* Container */
.grid-container {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;        /* 3 colunas */
  grid-template-columns: repeat(3, 1fr);      /* 3 colunas iguais */
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); /* Responsivo */
  grid-template-rows: auto 1fr auto;
  gap: 20px;
  row-gap: 10px;
  column-gap: 20px;
}

/* Áreas nomeadas */
.layout {
  grid-template-areas:
    "header header header"
    "sidebar main   aside"
    "footer footer footer";
}
.header  { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main    { grid-area: main; }

/* Items */
.item {
  grid-column: 1 / 3;    /* Ocupa colunas 1 e 2 */
  grid-row: 1 / span 2;  /* Ocupa 2 linhas */
}
```

---

## Responsividade

### Media Queries

```css
/* Mobile First */
.container { width: 100%; padding: 1rem; }

/* Tablet */
@media (min-width: 768px) {
  .container { max-width: 720px; margin: 0 auto; }
}

/* Desktop */
@media (min-width: 1024px) {
  .container { max-width: 960px; }
}

/* Wide */
@media (min-width: 1200px) {
  .container { max-width: 1140px; }
}

/* Orientação e preferências */
@media (orientation: landscape) { /* ... */ }
@media (prefers-color-scheme: dark) { /* ... */ }
@media (prefers-reduced-motion: reduce) { /* ... */ }
@media print { /* Estilos para impressão */ }
```

### Viewport Meta Tag

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

### Imagens Responsivas

```css
img { max-width: 100%; height: auto; }
```

---

## Animações e Transições

```css
/* Transições */
.btn {
  background: #3498db;
  transition: all 0.3s ease;
  /* transition: property duration timing-function delay */
}
.btn:hover {
  background: #2980b9;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

/* Animações */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to   { opacity: 1; transform: translateY(0); }
}

.card {
  animation: fadeIn 0.5s ease-out forwards;
  /* animation: name duration timing delay iteration direction fill */
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
.loader {
  animation: spin 1s linear infinite;
}

/* Transforms */
transform: translate(10px, 20px);
transform: scale(1.2);
transform: rotate(45deg);
transform: skew(10deg);
transform: perspective(500px) rotateY(30deg);
```

---

## CSS Avançado

### Variáveis CSS (Custom Properties)

```css
:root {
  --cor-primaria: #3498db;
  --cor-texto: #2c3e50;
  --font-body: 'Inter', sans-serif;
  --radius: 8px;
  --shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.btn {
  background: var(--cor-primaria);
  color: white;
  border-radius: var(--radius);
  font-family: var(--font-body);
}

/* Dark mode com variáveis */
@media (prefers-color-scheme: dark) {
  :root {
    --cor-texto: #ecf0f1;
    --bg: #1a1a2e;
  }
}
```

### Funções CSS

```css
/* calc() */
width: calc(100% - 2rem);
font-size: calc(1rem + 0.5vw);

/* clamp() — responsivo sem media queries */
font-size: clamp(1rem, 2.5vw, 2rem);
width: clamp(300px, 50%, 800px);

/* min() e max() */
width: min(90%, 1200px);
padding: max(1rem, 3vw);
```

### Pseudo-classes Modernas

```css
:is(h1, h2, h3) { color: navy; }      /* Agrupamento */
:where(h1, h2, h3) { margin: 0; }     /* Agrupamento (spec. 0) */
:not(.active) { opacity: 0.5; }       /* Negação */
:has(> img) { padding: 0; }           /* Pai que contém img */
:nth-child(3n+1) { color: red; }      /* Padrão n-ésimo */
:focus-visible { outline: 2px solid blue; } /* Foco por teclado */
```

### Container Queries (CSS 2023+)

```css
.card-container { container-type: inline-size; }

@container (min-width: 400px) {
  .card { display: flex; gap: 1rem; }
}
```

---

## Boas Práticas

### HTML
- Sempre declarar `<!DOCTYPE html>` e `lang="pt-BR"`
- 1 `<h1>` por página, hierarquia correta de títulos
- `alt` em todas as imagens
- Usar elementos semânticos em vez de `<div>` puro
- `loading="lazy"` em imagens abaixo do fold
- Validar com [validator.w3.org](https://validator.w3.org/)

### CSS
- Mobile-first approach
- `box-sizing: border-box` global
- Usar variáveis CSS para design tokens
- Preferir `rem` e `em` sobre `px`
- Usar Flexbox/Grid em vez de float
- BEM para nomenclatura: `.block__element--modifier`
- Evitar `!important`
- Usar `clamp()` para tipografia fluida

### Performance
- Minificar CSS em produção
- CSS crítico inline no `<head>`
- Preconnect a CDNs de fontes
- `preload` para recursos críticos

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preload" href="critical.css" as="style">
```

---

## 14. Segurança (Critical Hardening)

### Content Security Policy (CSP)
A **vacina contra XSS**. Define quais fontes o navegador pode carregar.
Adicione no `<head>`:

```html
<meta http-equiv="Content-Security-Policy" content="
  default-src 'self';
  script-src 'self' https://trusted.cdn.com;
  style-src 'self' 'unsafe-inline' https://fonts.googleapis.com;
  img-src 'self' data: https://images.com;
  font-src 'self' https://fonts.gstatic.com;
  object-src 'none';
  base-uri 'self';
">
```

### Prevenção XSS (Cross-Site Scripting)
1.  **Nunca** use `innerHTML` com dados de usuário.
2.  Use `textContent` ou `innerText`.
3.  Sanitize HTML se necessário (use bibliotecas como **DOMPurify**).

```javascript
// ❌ ERRADO
div.innerHTML = userInput; 

// ✅ CORRETO
div.textContent = userInput;

// ✅ CORRETO (Se precisar de HTML)
div.innerHTML = DOMPurify.sanitize(userInput);
```

### Subresource Integrity (SRI)
Garanta que scripts de CDN não foram alterados.
```html
<script src="https://code.jquery.com/jquery-3.7.1.min.js"
  integrity="sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo="
  crossorigin="anonymous"></script>
```

---

## 15. Cheatsheet Rápido

```css
/* === RESET MODERNO === */
*, *::before, *::after { box-sizing: border-box; margin: 0; }
html { font-size: 16px; scroll-behavior: smooth; }
img, video { max-width: 100%; display: block; }

/* === CONTAINER RESPONSIVO === */
.container {
  width: min(90%, 1200px);
  margin-inline: auto;
  padding-inline: 1rem;
}

/* === CENTRALIZAR === */
.center { display: grid; place-items: center; }

/* === TIPOGRAFIA FLUIDA === */
h1 { font-size: clamp(2rem, 5vw, 3.5rem); }
p  { font-size: clamp(1rem, 1.5vw, 1.125rem); }

/* === ASPECT RATIO === */
.video { aspect-ratio: 16 / 9; }

/* === TRUNCAR TEXTO === */
.truncate {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

/* === GLASS EFFECT === */
.glass {
  background: rgba(255,255,255,0.15);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255,255,255,0.2);
}
```

---

*Fonte: [W3Schools HTML](https://www.w3schools.com/html/) · [W3Schools CSS](https://www.w3schools.com/css/) · [MDN Web Docs](https://developer.mozilla.org/)*
