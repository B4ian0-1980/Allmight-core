---json
{
  "id": "documentacao_knockout",
  "title": "Documentação: Knockout.js",
  "categoria": "04-frameworks",
  "subcategoria": "react",
  "resumo": "**Status:** Legado / Estável **Tipo:** Biblioteca MVVM (Model-View-ViewModel)",
  "gatilhos": [
    "documentacao",
    "frameworks",
    "knockout",
    "react"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação: Knockout.js?",
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

# Documentação: Knockout.js

> **Status:** Legado / Estável
> **Tipo:** Biblioteca MVVM (Model-View-ViewModel)
> **Site Oficial:** [knockoutjs.com](https://knockoutjs.com)

## O que é?
Knockout é uma biblioteca JavaScript que ajuda a criar interfaces de usuário ricas e responsivas com um modelo de dados subjacente limpo. Sempre que você tiver seções da UI que atualizam dinamicamente (ex: dependendo das ações do usuário ou de fontes de dados externas), o KO pode ajudar.

## Conceitos Chave

### 1. Observables
O coração do Knockout. São objetos JavaScript especiais que notificam assinantes sobre mudanças e detectam dependências automaticamente.

```javascript
var myViewModel = {
    personName: ko.observable('Bob'),
    personAge: ko.observable(123)
};
```

### 2. Declarative Bindings
A maneira como você conecta os dados ao HTML.

```html
The name is <span data-bind="text: personName"></span>
```

### 3. Dependency Tracking (Computed Observables)
Calcula valores baseados em outros observables e se atualiza automaticamente.

```javascript
function AppViewModel() {
    this.firstName = ko.observable('Bob');
    this.lastName = ko.observable('Smith');

    this.fullName = ko.computed(function() {
        return this.firstName() + " " + this.lastName();
    }, this);
}
```

### 4. Templating
Renderização de modelos complexos.

## Instalação
Ainda amplamente disponível via CDN:

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/knockout/3.5.1/knockout-latest.js"></script>
```

## Exemplo Completo

```html
<p>First name: <input data-bind="value: firstName" /></p>
<p>Last name: <input data-bind="value: lastName" /></p>
<h2>Hello, <span data-bind="text: fullName"> </span>!</h2>

<script>
    // ViewModel
    var ViewModel = function(first, last) {
        this.firstName = ko.observable(first);
        this.lastName = ko.observable(last);
        
        this.fullName = ko.pureComputed(function() {
            return this.firstName() + " " + this.lastName();
        }, this);
    };
 
    // Ativar Knockout
    ko.applyBindings(new ViewModel("Planet", "Earth"));
</script>
```

## Referências
*   [Tutoriais Interativos](http://learn.knockoutjs.com/)
*   [Documentação Completa](https://knockoutjs.com/documentation/introduction.html)
