---json
{
  "id": "referencia-flask-restful",
  "title": "⚡ Referência: Flask RESTful (Class-Based)",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "Guia tecnico e referencias sobre ⚡ Referência: Flask RESTful (Class-Based).",
  "gatilhos": [
    "class-based",
    "flask",
    "linguagens",
    "php",
    "referencia",
    "restful"
  ],
  "perguntas_tipo": [
    "Como utilizar ⚡ Referência: Flask RESTful (Class-Based)?",
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

# ⚡ Referência: Flask RESTful (Class-Based)

Guia baseado no tutorial de Dennis Ivy. Foca no uso da extensão `flask-restful` para criar APIs mais organizadas usando Classes.

---

## 📦 Instalação
```bash
pip install flask-restful
```

## 🏗️ Estrutura Básica (app.py)

Ao invés de `@app.route`, usamos `api.add_resource`.

```python
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Recurso (Class-Based View)
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

# Rotas
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
```

---

## 🛠️ CRUD com Classes

A lógica é separada por verbo HTTP (`get`, `post`, `put`, `delete`) dentro da classe.

```python
class Item(Resource):
    # GET (Read)
    def get(self, pk):
        # Lógica para buscar item pelo ID (pk)
        return {'id': pk, 'name': 'Exemplo'}

    # PUT (Update)
    def put(self, pk):
        data = request.json
        # Lógica de update
        return {'id': pk, 'name': data['name']}

    # DELETE (Delete)
    def delete(self, pk):
        # Lógica de delete
        return {'message': 'Deletado'}

# Registrando rota com parâmetro
api.add_resource(Item, '/item/<int:pk>')
```

---

## 📤 Response Marshaling (Serialização)

Transforma objetos do banco (SQLAlchemy) em JSON automaticamente.

```python
from flask_restful import fields, marshal_with

# 1. Definir o Schema
task_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'is_active': fields.Boolean,
}

class Items(Resource):
    # 2. Decorar o método
    @marshal_with(task_fields)
    def get(self):
        # Retorna objetos do banco, o Flask-RESTful converte p/ JSON
        return Task.query.all() 
```

---

## 🆚 Flask Puro vs Flask RESTful

| Feature | Flask Puro (`@app.route`) | Flask RESTful (`Resource`) |
| :--- | :--- | :--- |
| **Organização** | Funções soltas. | Classes agrupam métodos HTTP. |
| **Rotas** | Decorator em cima da função. | `api.add_resource` centralizado. |
| **Retorno** | Precisa de `jsonify()`. | Retorna dicionários/objetos direto. |
| **Uso** | Projetos simples/médios. | APIs maiores/Padronizadas. |
