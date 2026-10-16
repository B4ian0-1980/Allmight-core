---json
{
  "id": "documentacao_jquery",
  "title": "Documentação jQuery — Guia Completo",
  "categoria": "04-frameworks",
  "subcategoria": "react",
  "resumo": "**Fonte:** [W3Schools jQuery](https://www.w3schools.com/jquery/default.asp) · [jQuery API](https://api.jquery.com/) **Versão:** jQuery 3.7+",
  "gatilhos": [
    "completo",
    "documentacao",
    "frameworks",
    "guia",
    "jquery",
    "react"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação jQuery — Guia Completo?",
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

# Documentação jQuery — Guia Completo

> **Fonte:** [W3Schools jQuery](https://www.w3schools.com/jquery/default.asp) · [jQuery API](https://api.jquery.com/)
> **Versão:** jQuery 3.7+
> **Atualizado:** 2026-02-14

---

## Sumário

1. [Fundamentos](#fundamentos)
2. [Seletores](#seletores)
3. [Manipulação do DOM](#manipulação-do-dom)
4. [Eventos](#eventos)
5. [Efeitos e Animações](#efeitos-e-animações)
6. [AJAX](#ajax)
7. [Traversing](#traversing)

---

## Fundamentos

```html
<!-- CDN -->
<script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>

<script>
// Document ready
$(document).ready(function() {
    // Código aqui
});

// Short form
$(function() {
    // Código aqui
});
</script>
```

---

## Seletores

```javascript
// Básicos
$("p")                  // Todos os <p>
$(".classe")            // Classe
$("#id")                // ID
$("div, p, span")       // Múltiplos
$("ul li")              // Descendentes
$("ul > li")            // Filhos diretos

// Filtros
$("tr:even")            // Linhas pares
$("tr:odd")             // Linhas ímpares
$("li:first")           // Primeiro
$("li:last")            // Último
$("li:eq(2)")           // Índice 2
$("li:gt(2)")           // Índice > 2
$("p:contains('texto')") // Contém texto
$(":input")             // Todos inputs
$(":checked")           // Checkboxes marcados
$(":visible")           // Elementos visíveis
$(":hidden")            // Elementos ocultos

// Atributo
$("a[href]")            // <a> com href
$("a[target='_blank']") // Valor específico
$("input[name^='user']") // Começa com
$("input[name$='name']") // Termina com
```

---

## Manipulação do DOM

```javascript
// Conteúdo
$("p").text()                   // Get texto
$("p").text("Novo texto")      // Set texto
$("div").html()                 // Get HTML
$("div").html("<b>Bold</b>")   // Set HTML
$("input").val()                // Get valor
$("input").val("novo")         // Set valor

// Atributos
$("a").attr("href")            // Get atributo
$("a").attr("href", "url")    // Set atributo
$("a").removeAttr("title")    // Remover
$("input").prop("checked")     // Propriedade booleana

// Classes
$("p").addClass("destaque")
$("p").removeClass("destaque")
$("p").toggleClass("ativo")
$("p").hasClass("destaque")    // boolean

// CSS
$("p").css("color")                    // Get
$("p").css("color", "red")           // Set
$("p").css({"color": "red", "font-size": "16px"}) // Múltiplos

// Inserir elementos
$("ul").append("<li>Novo item</li>")     // No final
$("ul").prepend("<li>Primeiro</li>")     // No início
$("p").after("<hr>")                      // Depois
$("p").before("<h2>Título</h2>")         // Antes
$("<div>", {class: "card", text: "Novo"}).appendTo("body")

// Remover
$("p").remove()         // Remove elemento
$("div").empty()        // Remove conteúdo
$("p").detach()         // Remove mas mantém dados

// Dimensões
$("div").width()
$("div").height()
$("div").outerWidth(true)  // Inclui margin
```

---

## Eventos

```javascript
// Click
$("button").click(function() {
    $(this).toggleClass("ativo");
});

// On (recomendado — suporta delegação)
$("ul").on("click", "li", function() {
    $(this).remove();
});

// Eventos comuns
$("input").focus(function() { });
$("input").blur(function() { });
$("input").change(function() { });
$("input").keyup(function(e) {
    if (e.key === "Enter") { /* ... */ }
});
$("form").submit(function(e) {
    e.preventDefault();
});
$("div").hover(
    function() { /* mouseenter */ },
    function() { /* mouseleave */ }
);

// Desligar evento
$("button").off("click");

// Trigger
$("button").trigger("click");

// One (executa uma vez)
$("button").one("click", function() { });
```

---

## Efeitos e Animações

```javascript
// Show/Hide
$("div").hide(400)
$("div").show(400)
$("div").toggle(400)

// Fade
$("div").fadeIn(400)
$("div").fadeOut(400)
$("div").fadeToggle(400)
$("div").fadeTo(400, 0.5)  // Opacidade

// Slide
$("div").slideDown(400)
$("div").slideUp(400)
$("div").slideToggle(400)

// Animate
$("div").animate({
    left: "250px",
    opacity: 0.5,
    fontSize: "24px"
}, 800, function() {
    // Callback ao concluir
});

// Encadear
$("div").slideUp(300).slideDown(300).fadeOut(500);

// Stop
$("div").stop()    // Para animação atual
$("div").stop(true, true)  // Para todas, vai para o final
```

---

## AJAX

```javascript
// $.ajax (completo)
$.ajax({
    url: "/api/dados",
    method: "GET",
    dataType: "json",
    headers: {"Authorization": "Bearer token"},
    success: function(data) {
        console.log(data);
    },
    error: function(xhr, status, error) {
        console.error(error);
    },
    complete: function() {
        console.log("Finalizado");
    }
});

// $.get (atalho)
$.get("/api/users", function(data) {
    console.log(data);
});

// $.post (atalho)
$.post("/api/users", {nome: "Ana", email: "ana@mail.com"}, function(res) {
    console.log(res);
});

// $.getJSON
$.getJSON("/api/dados.json", function(data) {
    $.each(data, function(i, item) {
        $("ul").append("<li>" + item.nome + "</li>");
    });
});

// Load (HTML em elemento)
$("#conteudo").load("/pagina.html #secao");

// Formulário via AJAX
$("form").submit(function(e) {
    e.preventDefault();
    $.ajax({
        url: $(this).attr("action"),
        method: "POST",
        data: $(this).serialize(),
        success: function(res) { alert("Enviado!"); }
    });
});
```

---

## Traversing

```javascript
// Ancestrais
$("li").parent()          // Pai direto
$("li").parents("ul")     // Ancestrais
$("li").closest("div")    // Ancestral mais próximo

// Descendentes
$("div").children()        // Filhos diretos
$("div").find("span")     // Todos descendentes

// Irmãos
$("li").siblings()
$("li").next()
$("li").prev()
$("li").nextAll()
$("li").prevAll()

// Filtrar
$("li").first()
$("li").last()
$("li").eq(2)
$("li").filter(".ativo")
$("li").not(".ativo")
$("li").has("ul")

// Each
$("li").each(function(index) {
    console.log(index + ": " + $(this).text());
});
```

---

*Fonte: [W3Schools jQuery](https://www.w3schools.com/jquery/) · [jQuery API](https://api.jquery.com/)*
