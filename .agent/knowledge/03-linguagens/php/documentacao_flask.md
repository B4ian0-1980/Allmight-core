---json
{
  "id": "documentacao_flask",
  "title": "Documentação Flask (Guia Rápido & Oficial)",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "Guia tecnico e referencias sobre Documentação Flask (Guia Rápido & Oficial).",
  "gatilhos": [
    "documentacao",
    "flask",
    "guia",
    "linguagens",
    "oficial",
    "php"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação Flask (Guia Rápido & Oficial)?",
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

# Documentação Flask (Guia Rápido & Oficial)

**Fonte:** [https://flask.palletsprojects.com/en/stable/](https://flask.palletsprojects.com/en/stable/)

---

## 1. Instalação

### Ambientes Virtuais
É recomendado usar um ambiente virtual para gerenciar dependências.

```bash
# Windows
py -3 -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
. .venv/bin/activate
```

### Instalar Flask
Com o ambiente ativado:

```bash
pip install Flask
```

---

## 2. Aplicação Mínima

Crie um arquivo `hello.py`:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

Para rodar:

```bash
flask --app hello run
# Ou com debug ativado (recarrega ao salvar):
flask --app hello run --debug
```

Disponível em: `http://127.0.0.1:5000`

---

## 3. Roteamento (Routing)

### Rotas Básicas
Use o decorator `@app.route()` para ligar funções a URLs.

```python
@app.route('/')
def index():
    return 'Página Inicial'

@app.route('/hello')
def hello():
    return 'Olá Mundo'
```

### Variáveis na URL
Você pode capturar partes da URL como variáveis.

```python
from markupsafe import escape

@app.route('/user/<username>')
def show_user_profile(username):
    # escape previne injeção de código
    return f'Usuário: {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # post_id será um inteiro
    return f'Post ID: {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # captura tudo após a barra, incluindo barras
    return f'Subpath: {escape(subpath)}'
```

**Conversores disponíveis:** `string` (padrão), `int`, `float`, `path`, `uuid`.

### Métodos HTTP
Por padrão, rotas só aceitam GET. Use `methods` para aceitar outros.

```python
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
```

Ou use os atalhos:
```python
@app.get('/login')
def login_get(): ...

@app.post('/login')
def login_post(): ...
```

### Construindo URLs
Use `url_for()` para gerar URLs para suas funções. Isso é mais seguro que hardcoded strings.

```python
from flask import url_for

with app.test_request_context():
    print(url_for('index'))  # Saída: /
    print(url_for('login'))  # Saída: /login
    print(url_for('login', next='/'))  # Saída: /login?next=/
    print(url_for('profile', username='John Doe'))  # Saída: /user/John%20Doe
```

---

## 4. Arquivos Estáticos

Crie uma pasta chamada `static` na raiz do projeto.
Acesse usando o endpoint especial `'static'`.

```python
url_for('static', filename='style.css')
```
Isso gerará a URL para `root/static/style.css`.

---

## 5. Renderizando Templates

Flask usa **Jinja2** como motor de templates.
Crie uma pasta `templates` na raiz.

**Estrutura:**
```
/app.py
/templates
    /hello.html
```

**app.py:**
```python
from flask import render_template

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)
```

**templates/hello.html:**
```html
<!doctype html>
<title>Hello from Flask</title>
{% if person %}
  <h1>Hello {{ person }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %}
```

---

## 6. Acessando Dados da Requisição

Use o objeto global `request`.

```python
from flask import request

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        # Acessar dados de formulário
        username = request.form['username']
        password = request.form['password']
        if valid_login(username, password):
            return log_the_user_in(username)
        else:
            error = 'Invalid username/password'
    
    # Acessar parâmetros de URL (?key=value)
    search = request.args.get('q', '')

    return render_template('login.html', error=error)
```

---

## 7. Estrutura de Projeto Recomendada

À medida que o projeto cresce, não mantenha tudo em um arquivo. Use pacotes.

```text
/nome-projeto
├── .venv/
├── pyproject.toml       # Dependências e config
├── flaskr/              # Seu código python
│   ├── __init__.py      # Inicializa a app factory
│   ├── db.py
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   └── static/
└── tests/
    ├── conftest.py
    └── data.sql
```
