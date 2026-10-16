---json
{
  "id": "documentacao_sass",
  "title": "Documentação Sass/SCSS — Guia Completo",
  "categoria": "04-frameworks",
  "subcategoria": "react",
  "resumo": "**Fonte:** [W3Schools Sass](https://www.w3schools.com/sass/default.asp) · [Sass Docs](https://sass-lang.com/documentation/) **Versão:** Dart Sass 1.7+",
  "gatilhos": [
    "completo",
    "documentacao",
    "frameworks",
    "guia",
    "react",
    "sass",
    "scss"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação Sass/SCSS — Guia Completo?",
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

# Documentação Sass/SCSS — Guia Completo

> **Fonte:** [W3Schools Sass](https://www.w3schools.com/sass/default.asp) · [Sass Docs](https://sass-lang.com/documentation/)
> **Versão:** Dart Sass 1.7+
> **Atualizado:** 2026-02-14

---

## Sumário

1. [Instalação](#instalação)
2. [Variáveis](#variáveis)
3. [Nesting](#nesting)
4. [Partials e Import](#partials-e-import)
5. [Mixins](#mixins)
6. [Extend e Herança](#extend-e-herança)
7. [Funções e Operadores](#funções-e-operadores)
8. [Controle de Fluxo](#controle-de-fluxo)
9. [Módulos (@use e @forward)](#módulos)

---

## Instalação

```bash
npm install -g sass
sass input.scss output.css
sass --watch src/scss:dist/css
```

---

## Variáveis

```scss
// Variáveis com $
$cor-primaria: #3498db;
$cor-texto: #2c3e50;
$font-body: 'Inter', sans-serif;
$radius: 8px;
$spacing: 1rem;

// Maps
$breakpoints: (
  sm: 576px,
  md: 768px,
  lg: 992px,
  xl: 1200px
);

$cores: (
  primary: #3498db,
  success: #2ecc71,
  danger: #e74c3c,
  warning: #f39c12
);

// Acessar map
.btn { color: map-get($cores, primary); }

// Listas
$fontes: 'Inter', 'Helvetica', sans-serif;
$tamanhos: 12px 14px 16px 18px 24px;
font-size: nth($tamanhos, 3); // 16px
```

---

## Nesting

```scss
nav {
  background: $cor-primaria;

  ul {
    list-style: none;
    display: flex;
    gap: $spacing;
  }

  li {
    &:hover {    // & = seletor pai (nav li:hover)
      opacity: 0.8;
    }

    &.ativo {    // nav li.ativo
      font-weight: bold;
    }

    &::before {  // Pseudo-elemento
      content: "→";
    }
  }

  // BEM com nesting
  &__item {      // nav__item
    padding: 0.5rem;

    &--ativo {   // nav__item--ativo
      color: white;
    }
  }

  // Media queries aninhadas
  @media (max-width: 768px) {
    flex-direction: column;
  }
}
```

---

## Partials e Import

```scss
// Estrutura de arquivos:
// styles/
//   _variables.scss    (partial — começa com _)
//   _mixins.scss
//   _reset.scss
//   _components/
//     _buttons.scss
//     _cards.scss
//   main.scss

// main.scss
@use 'variables' as vars;   // Moderno (recomendado)
@use 'mixins';
@use 'reset';
@use 'components/buttons';
@use 'components/cards';

// Usar variáveis do módulo
.btn { color: vars.$cor-primaria; }
```

---

## Mixins

```scss
// Mixin simples
@mixin flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
}

.hero { @include flex-center; }

// Mixin com parâmetros
@mixin btn($bg, $color: white, $radius: 8px) {
  background: $bg;
  color: $color;
  border-radius: $radius;
  padding: 0.5rem 1rem;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;

  &:hover {
    opacity: 0.9;
    transform: translateY(-1px);
  }
}

.btn-primary { @include btn(#3498db); }
.btn-danger  { @include btn(#e74c3c, white, 4px); }

// Mixin com @content (slot)
@mixin responsive($breakpoint) {
  @if map-has-key($breakpoints, $breakpoint) {
    @media (min-width: map-get($breakpoints, $breakpoint)) {
      @content;
    }
  }
}

.container {
  width: 100%;
  @include responsive(md) { max-width: 720px; }
  @include responsive(lg) { max-width: 960px; }
}

// Mixin para pseudo-elementos
@mixin pseudo($pos: absolute, $content: '') {
  content: $content;
  position: $pos;
}

// Mixin para tipografia fluida
@mixin fluid-type($min-size, $max-size, $min-vw: 320px, $max-vw: 1200px) {
  font-size: clamp(#{$min-size}, calc(#{$min-size} + (#{strip-unit($max-size - $min-size)}) * ((100vw - #{$min-vw}) / #{strip-unit($max-vw - $min-vw)})), #{$max-size});
}
```

---

## Extend e Herança

```scss
// Placeholder (não gera CSS sozinho)
%card-base {
  border-radius: $radius;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.card { @extend %card-base; background: white; }
.card-dark { @extend %card-base; background: #1a1a2e; color: white; }

// Extend classe real
.mensagem {
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.sucesso { @extend .mensagem; border-color: green; color: green; }
.erro { @extend .mensagem; border-color: red; color: red; }
```

---

## Funções e Operadores

```scss
// Operadores
.container { width: 100% - 2rem; }
.col { width: (4 / 12) * 100%; }

// Funções built-in
$cor: #3498db;
lighten($cor, 20%)       // Clarear
darken($cor, 15%)        // Escurecer
adjust-hue($cor, 45deg)  // Girar matiz
saturate($cor, 20%)      // Saturar
desaturate($cor, 20%)    // Dessaturar
rgba($cor, 0.5)          // Adicionar alfa
mix($cor1, $cor2, 50%)   // Misturar

// Funções de string
str-length("hello")     // 5
to-upper-case("hello")  // "HELLO"
str-index("hello", "lo") // 4

// Funções numéricas
round(4.6)    // 5
ceil(4.1)     // 5
floor(4.9)    // 4
abs(-5)       // 5
min(10, 20)   // 10
max(10, 20)   // 20
percentage(0.5) // 50%

// Função customizada
@function rem($px, $base: 16) {
  @return ($px / $base) * 1rem;
}

h1 { font-size: rem(32); }  // 2rem
p  { font-size: rem(16); }  // 1rem

// Função para acessar cores
@function cor($nome) {
  @if map-has-key($cores, $nome) {
    @return map-get($cores, $nome);
  }
  @warn "Cor '#{$nome}' não encontrada.";
  @return null;
}

.btn { background: cor(primary); }
```

---

## Controle de Fluxo

```scss
// @if / @else
@mixin tema($modo) {
  @if $modo == dark {
    background: #1a1a2e;
    color: #ecf0f1;
  } @else if $modo == light {
    background: #ffffff;
    color: #2c3e50;
  } @else {
    @warn "Modo desconhecido: #{$modo}";
  }
}

// @each (iterar)
$tamanhos: (sm: 12px, md: 16px, lg: 24px, xl: 32px);

@each $nome, $size in $tamanhos {
  .text-#{$nome} { font-size: $size; }
}
// Gera: .text-sm, .text-md, .text-lg, .text-xl

@each $cor-nome, $cor-valor in $cores {
  .bg-#{$cor-nome} { background: $cor-valor; }
  .text-#{$cor-nome} { color: $cor-valor; }
}

// @for
@for $i from 1 through 12 {
  .col-#{$i} { width: percentage($i / 12); }
}

// @while
$cols: 12;
@while $cols > 0 {
  .flex-#{$cols} { flex: 0 0 percentage($cols / 12); }
  $cols: $cols - 1;
}
```

---

## Módulos

```scss
// _variables.scss
$cor-primaria: #3498db !default;  // Pode ser sobrescrito

// _mixins.scss
@use 'variables' as *;

@mixin theme-color($prop) {
  #{$prop}: $cor-primaria;
}

// main.scss — @use (moderno, substitui @import)
@use 'variables' as vars;      // Namespace
@use 'mixins';

.btn { color: vars.$cor-primaria; }
.card { @include mixins.theme-color(background); }

// Sobrescrever defaults
@use 'variables' with (
  $cor-primaria: #e74c3c
);

// @forward (re-exportar)
// _index.scss
@forward 'variables';
@forward 'mixins';
@forward 'functions';

// Então em main.scss:
@use 'index';
```

---

*Fonte: [W3Schools Sass](https://www.w3schools.com/sass/) · [Sass Documentation](https://sass-lang.com/documentation/)*
