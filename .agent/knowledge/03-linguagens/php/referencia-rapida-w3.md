---json
{
  "id": "referencia-rapida-w3",
  "title": "⚡ Referência Rápida Django (Baseado em W3Schools)",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "Guia tecnico e referencias sobre ⚡ Referência Rápida Django (Baseado em W3Schools).",
  "gatilhos": [
    "baseado",
    "django",
    "linguagens",
    "php",
    "rapida",
    "referencia",
    "w3schools"
  ],
  "perguntas_tipo": [
    "Como utilizar ⚡ Referência Rápida Django (Baseado em W3Schools)?",
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

# ⚡ Referência Rápida Django (Baseado em W3Schools)

Este arquivo é um resumo prático dos principais recursos e sintaxes do Django, organizado conforme o curso da W3Schools.

---

## 📂 Configuração de Templates
Para o Django encontrar seus HTMLs, configure o `settings.py`:

1.  Crie uma pasta `templates` na raiz (ao lado do `manage.py`).
2.  No `settings.py`, procure por `TEMPLATES` e adicione a pasta em `DIRS`:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # <--- ADICIONAR ISSO
        'APP_DIRS': True,
        # ...
    },
]
```

---

## 🏷️ Template Tags (Sintaxe Básica)
Use `{% %}` para lógica e `{{ }}` para variáveis.

| Tag | Descrição | Exemplo |
| :--- | :--- | :--- |
| `{% extends %}` | Herança de template (Sempre a primeira linha). | `{% extends "master.html" %}` |
| `{% block %}` | Define um bloco substituível. | `{% block content %}...{% endblock %}` |
| `{% include %}` | Importa outro template. | `{% include "menu.html" %}` |
| `{% for %}` | Loop em listas. | `{% for x in members %} {{ x.name }} {% endfor %}` |
| `{% if %}` | Condicional. | `{% if x > 100 %} Grante {% endif %}` |
| `{% csrf_token %}` | Proteção obrigatória em Forms (POST). | `<form>{% csrf_token %}...</form>` |
| `{% load static %}` | Carrega arquivos estáticos (CSS/JS). | `{% load static %}` |

---

## 🔍 Filtros Comuns
Modificam a exibição de variáveis. Use `|`.

| Filtro | O que faz | Exemplo |
| :--- | :--- | :--- |
| `upper` | Transforma em maiúsculo. | `{{ name|upper }}` |
| `lower` | Transforma em minúsculo. | `{{ name|lower }}` |
| `default` | Valor padrão se for vazio/None. | `{{ name|default:"Sem nome" }}` |
| `length` | Tamanho da lista/string. | `{{ lista|length }}` |
| `slice` | Corta a lista/string. | `{{ nome|slice:":3" }}` |
| `date` | Formata datas. | `{{ data|date:"D d M Y" }}` |

---

## 🔎 Field Lookups (Filtros de Banco)
Usados no `filter()`. Ex: `Member.objects.filter(firstname__startswith='L')`.

| Lookup | Descrição |
| :--- | :--- |
| `__exact` | Igualdade exata (Case sensitive). |
| `__iexact` | Igualdade (Case insensitive). |
| `__contains` | Contém texto (LIKE '%...%'). |
| `__startswith` | Começa com. |
| `__gt` / `__gte` | Maior que / Maior ou igual. |
| `__lt` / `__lte` | Menor que / Menor ou igual. |
| `__in` | Está dentro de uma lista de valores. |

---

## 📦 QuerySets (Métodos Principais)

```python
# Buscar tudo
Member.objects.all()

# Filtrar
Member.objects.filter(firstname='Emil')

# Buscar um único registro (Erro se não achar ou achar vários)
Member.objects.get(id=1)

# Ordenar
Member.objects.all().order_by('lastname')
Member.objects.all().order_by('-lastname') # Decrescente

# Primeiros 5
Member.objects.all()[:5]
```

---

## ☁️ Deploy (AWS Elastic Beanstalk)
O W3Schools oferece um guia específico para AWS. Passos macro:

1.  Criar conta AWS e RDS (PostgreSQL).
2.  Configurar arquivo `.ebextensions/django.config`:
    ```yaml
    option_settings:
      aws:elasticbeanstalk:container:python:
        WSGIPath: meuprojeto.wsgi:application
    ```
3.  Criar arquivo `.zip` do projeto (excluindo venv).
4.  Subir no console do Elastic Beanstalk.
