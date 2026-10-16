---json
{
  "id": "documentacao_symfony",
  "title": "Documentação: Symfony",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "**Linguagem:** PHP 8+ **Tipo:** Framework MVC Full-Stack",
  "gatilhos": [
    "documentacao",
    "linguagens",
    "php",
    "symfony"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação: Symfony?",
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

# Documentação: Symfony

> **Linguagem:** PHP 8+
> **Tipo:** Framework MVC Full-Stack
> **Site Oficial:** [symfony.com](https://symfony.com)

## O que é?
Symfony é um framework PHP de alto desempenho, robusto e flexível, utilizado para construir aplicações web complexas e microsserviços. Ele também é uma biblioteca de componentes reutilizáveis (como HttpFoundation, Console, Routing) que são usados por outros projetos famosos (como Laravel e Drupal).

## Arquitetura
O Symfony adota o padrão MVC e é fortemente orientado a injeção de dependência e serviços.

### Estrutura de Diretórios
*   `config/`: Configurações de rotas, serviços e pacotes.
*   `src/`: Código fonte PHP (Controllers, Entities, Services).
*   `templates/`: Arquivos Twig.
*   `public/`: Ponto de entrada (index.php) e assets.

## Instalação (Symfony CLI)
A maneira recomendada é usar o binário oficial.

```bash
# Baixar CLI
curl -sS https://get.symfony.com/cli/installer | bash

# Criar projeto Web completo
symfony new meu_projeto --webapp

# Rodar servidor local
symfony server:start
```

## Conceitos Chave

### 1. Rotas e Controllers
As rotas são definidas via atributos (PHP 8) ou YAML.

```php
// src/Controller/BlogController.php
namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

class BlogController extends AbstractController
{
    #[Route('/blog', name: 'blog_list')]
    public function list(): Response
    {
        return $this->render('blog/list.html.twig', [
            'category' => 'Technology',
        ]);
    }
}
```

### 2. Twig (Templates)
Motor de template seguro e poderoso.

```twig
{# templates/blog/list.html.twig #}
<h1>Blog de {{ category }}</h1>
<ul>
    {% for post in posts %}
        <li>{{ post.title }}</li>
    {% endfor %}
</ul>
```

### 3. Entidades e Doctrine (ORM)
O Symfony usa o Doctrine para mapeamento de banco de dados.

```bash
# Criar entidade
php bin/console make:entity Product

# Gerar migration
php bin/console make:migration

# Aplicar no banco
php bin/console doctrine:migrations:migrate
```

## Componentes
O Symfony é modular. Você pode instalar pacotes conforme a necessidade:
*   `symfony/mailer`: Envio de emails.
*   `symfony/security-bundle`: Autenticação e autorização.
*   `symfony/form`: Criação e validação de formulários.

## Referências
*   [Documentação Oficial](https://symfony.com/doc/current/index.html)
*   [SymfonyCasts (Tutoriais)](https://symfonycasts.com/)
