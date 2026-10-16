---json
{
  "id": "documentacao_ember",
  "title": "Documentação: Ember.js",
  "categoria": "04-frameworks",
  "subcategoria": "react",
  "resumo": "**Versão:** Release (Atual) **Tipo:** Framework Frontend (MVVM/Component-Based)",
  "gatilhos": [
    "documentacao",
    "ember",
    "frameworks",
    "react"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação: Ember.js?",
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

# Documentação: Ember.js

> **Versão:** Release (Atual)
> **Tipo:** Framework Frontend (MVVM/Component-Based)
> **Site Oficial:** [emberjs.com](https://emberjs.com)

## O que é?
O Ember.js é um framework JavaScript produtivo e opinativo para a construção de aplicações web ambiciosas. Ele fornece uma solução completa que inclui roteamento, gerenciamento de dados (EmberData) e um pipeline de build moderno (Ember CLI).

## Principais Características
*   **Convenção sobre Configuração:** O Ember toma muitas decisões triviais por você, permitindo foco na lógica de negócio.
*   **Ember CLI:** Ferramenta de linha de comando robusta para criar, desenvolver e testar aplicações.
*   **Roteamento:** Um router de primeira classe que respeita a URL como fonte da verdade.
*   **Estabilidade sem Estagnação:** Compromisso com retrocompatibilidade e migrações suaves.
*   **Glimmer Engine:** Motor de renderização rápido e eficiente.

## Instalação (Ember CLI)

Pré-requisitos: Node.js e npm.

```bash
# Instalar a CLI globalmente
npm install -g ember-cli

# Criar um novo projeto
ember new meu-app-incrivel

# Entrar no diretório
cd meu-app-incrivel

# Rodar o servidor de desenvolvimento
ember serve
```

Acesse em `http://localhost:4200`.

## Conceitos Fundamentais

### 1. Router e Rotas
O Router mapeia a URL para uma Rota (Route). A Rota é responsável por carregar o modelo (Model) de dados.

```javascript
// app/router.js
Router.map(function() {
  this.route('about');
  this.route('posts');
});
```

### 2. Componentes (Glimmer/Octane)
Componentes são os blocos de construção da UI.

```handlebars
{{!-- app/components/profile.hbs --}}
<div class="profile">
  <h2>{{@name}}</h2>
  <p>{{@bio}}</p>
</div>
```

```javascript
// app/components/profile.js
import Component from '@glimmer/component';
import { action } from '@ember/object';

export default class ProfileComponent extends Component {
  @action
  showDetails() {
    console.log('Detalhes...');
  }
}
```

### 3. Ember Data
Biblioteca padrão para gerenciamento de dados.

```javascript
// app/models/person.js
import Model, { attr } from '@ember-data/model';

export default class PersonModel extends Model {
  @attr('string') name;
  @attr('date') birthday;
}
```

## Ecossistema
*   **Ember Inspector:** Extensão de navegador para debugar a aplicação.
*   **Addons:** Milhares de pacotes prontos para uso (`ember install <nome-do-addon>`).
*   **Ember Composable Helpers:** Utilitários para templates.

## Referências
*   [Guides (Guia Oficial)](https://guides.emberjs.com/release/)
*   [API Reference](https://api.emberjs.com/)
*   [Ember Discord](https://discord.gg/emberjs)
