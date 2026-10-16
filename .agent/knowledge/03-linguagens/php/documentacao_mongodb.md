---json
{
  "id": "documentacao_mongodb",
  "title": "Documentação MongoDB — Guia Completo",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "**Fonte:** [W3Schools MongoDB](https://www.w3schools.com/mongodb/index.php) · [MongoDB Docs](https://www.mongodb.com/docs/manual/) **Versão:** MongoDB 7.x+",
  "gatilhos": [
    "completo",
    "documentacao",
    "guia",
    "linguagens",
    "mongodb",
    "php"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação MongoDB — Guia Completo?",
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

# Documentação MongoDB — Guia Completo

> **Fonte:** [W3Schools MongoDB](https://www.w3schools.com/mongodb/index.php) · [MongoDB Docs](https://www.mongodb.com/docs/manual/)
> **Versão:** MongoDB 7.x+
> **Atualizado:** 2026-02-14

---

## Sumário

1. [Fundamentos](#fundamentos)
2. [CRUD — Operações Básicas](#crud)
3. [Consultas e Filtros](#consultas-e-filtros)
4. [Aggregation Pipeline](#aggregation-pipeline)
5. [Índices](#índices)
6. [Schema Design](#schema-design)
7. [Mongoose (Node.js)](#mongoose)

---

## Fundamentos

```bash
# Docker
docker run -d --name mongo -p 27017:27017 mongo:7

# mongosh (shell)
mongosh
show dbs
use minhaBase
show collections
db.stats()
```

### Conceitos

| Relacional | MongoDB |
|---|---|
| Database | Database |
| Table | Collection |
| Row | Document (JSON/BSON) |
| Column | Field |
| JOIN | Embedded / $lookup |
| PRIMARY KEY | `_id` (automático) |

---

## CRUD

### Inserir

```javascript
// Um documento
db.usuarios.insertOne({
  nome: "Ana",
  email: "ana@mail.com",
  idade: 25,
  tags: ["dev", "frontend"],
  endereco: { cidade: "São Paulo", uf: "SP" }
})

// Múltiplos
db.usuarios.insertMany([
  { nome: "Bruno", idade: 30, ativo: true },
  { nome: "Carlos", idade: 22, ativo: false }
])
```

### Consultar

```javascript
// Todos
db.usuarios.find()

// Com filtro
db.usuarios.find({ idade: { $gte: 25 } })

// Um documento
db.usuarios.findOne({ email: "ana@mail.com" })

// Projeção (campos retornados)
db.usuarios.find({}, { nome: 1, email: 1, _id: 0 })

// Contagem
db.usuarios.countDocuments({ ativo: true })
```

### Atualizar

```javascript
// Um documento
db.usuarios.updateOne(
  { email: "ana@mail.com" },
  { $set: { idade: 26, ativo: true } }
)

// Múltiplos
db.usuarios.updateMany(
  { ativo: false },
  { $set: { ativo: true }, $currentDate: { atualizado: true } }
)

// Replace (substitui documento inteiro)
db.usuarios.replaceOne(
  { _id: ObjectId("...") },
  { nome: "Diana", idade: 28, ativo: true }
)

// Upsert (insere se não existir)
db.usuarios.updateOne(
  { email: "novo@mail.com" },
  { $set: { nome: "Novo", idade: 20 } },
  { upsert: true }
)
```

### Deletar

```javascript
db.usuarios.deleteOne({ email: "ana@mail.com" })
db.usuarios.deleteMany({ ativo: false })
db.usuarios.drop()  // Remove coleção inteira
```

---

## Consultas e Filtros

### Operadores de Comparação

```javascript
db.produtos.find({ preco: { $eq: 100 } })    // Igual
db.produtos.find({ preco: { $ne: 100 } })    // Diferente
db.produtos.find({ preco: { $gt: 50 } })     // Maior que
db.produtos.find({ preco: { $gte: 50 } })    // Maior ou igual
db.produtos.find({ preco: { $lt: 100 } })    // Menor que
db.produtos.find({ preco: { $lte: 100 } })   // Menor ou igual
db.produtos.find({ preco: { $in: [10, 20, 30] } })   // Em lista
db.produtos.find({ preco: { $nin: [10, 20] } })       // Não em lista
```

### Operadores Lógicos

```javascript
// AND (implícito)
db.produtos.find({ preco: { $gte: 50 }, categoria: "eletro" })

// OR
db.produtos.find({
  $or: [
    { preco: { $lt: 20 } },
    { categoria: "oferta" }
  ]
})

// NOT
db.produtos.find({ preco: { $not: { $gt: 100 } } })

// NOR
db.produtos.find({
  $nor: [{ ativo: false }, { estoque: 0 }]
})
```

### Operadores de Elemento e Array

```javascript
// Existe campo
db.usuarios.find({ telefone: { $exists: true } })

// Tipo
db.usuarios.find({ idade: { $type: "int" } })

// Regex
db.usuarios.find({ nome: { $regex: /^ana/i } })

// Array
db.pedidos.find({ tags: "urgente" })              // Contém
db.pedidos.find({ tags: { $all: ["urgente", "vip"] } })  // Contém todos
db.pedidos.find({ tags: { $size: 3 } })            // Tamanho exato
db.pedidos.find({ "itens.preco": { $gt: 100 } })  // Nested

// $elemMatch (elemento do array satisfaz múltiplas condições)
db.pedidos.find({
  itens: { $elemMatch: { produto: "X", qtd: { $gte: 5 } } }
})
```

### Sort, Limit, Skip

```javascript
db.produtos.find()
  .sort({ preco: -1 })      // Descendente
  .skip(10)                   // Pular 10
  .limit(5)                   // Retornar 5
```

---

## Aggregation Pipeline

```javascript
db.vendas.aggregate([
  // 1. Filtrar
  { $match: { status: "concluida", data: { $gte: ISODate("2026-01-01") } } },

  // 2. Agrupar
  { $group: {
    _id: "$vendedor",
    total: { $sum: "$valor" },
    qtd: { $count: {} },
    media: { $avg: "$valor" },
    maximo: { $max: "$valor" }
  }},

  // 3. Ordenar
  { $sort: { total: -1 } },

  // 4. Limitar
  { $limit: 10 },

  // 5. Projeção
  { $project: {
    vendedor: "$_id",
    total: { $round: ["$total", 2] },
    media: { $round: ["$media", 2] },
    _id: 0
  }}
])
```

### Stages Úteis

```javascript
// $lookup (JOIN)
{ $lookup: {
  from: "produtos",
  localField: "produto_id",
  foreignField: "_id",
  as: "produto_detalhes"
}}

// $unwind (expande array)
{ $unwind: "$itens" }

// $addFields
{ $addFields: { total: { $multiply: ["$preco", "$qtd"] } } }

// $bucket (histograma)
{ $bucket: {
  groupBy: "$idade",
  boundaries: [0, 18, 30, 50, 100],
  default: "Outros",
  output: { count: { $sum: 1 } }
}}

// $facet (múltiplos pipelines)
{ $facet: {
  porCategoria: [{ $group: { _id: "$cat", total: { $sum: 1 } } }],
  porPreco: [{ $bucket: { groupBy: "$preco", boundaries: [0, 50, 100, 500] } }]
}}
```

---

## Índices

```javascript
// Índice simples
db.usuarios.createIndex({ email: 1 })   // ASC

// Índice composto
db.pedidos.createIndex({ cliente_id: 1, data: -1 })

// Índice único
db.usuarios.createIndex({ cpf: 1 }, { unique: true })

// Índice de texto (full-text search)
db.artigos.createIndex({ titulo: "text", conteudo: "text" })
db.artigos.find({ $text: { $search: "mongodb guia" } })

// TTL (auto-deletar documentos)
db.sessoes.createIndex({ criadoEm: 1 }, { expireAfterSeconds: 3600 })

// Listar e remover
db.usuarios.getIndexes()
db.usuarios.dropIndex("email_1")

// Explain (análise de performance)
db.usuarios.find({ email: "ana@mail.com" }).explain("executionStats")
```

---

## Schema Design

### Embedded (desnormalizado — preferir para dados lidos juntos)

```javascript
// Pedido com itens embutidos
{
  _id: ObjectId("..."),
  cliente: { nome: "Ana", email: "ana@mail.com" },
  itens: [
    { produto: "Mouse", preco: 50, qtd: 2 },
    { produto: "Teclado", preco: 120, qtd: 1 }
  ],
  total: 220,
  data: ISODate("2026-02-14")
}
```

### Referenced (normalizado — para dados independentes)

```javascript
// Coleção: usuarios
{ _id: ObjectId("u1"), nome: "Ana" }

// Coleção: pedidos
{ _id: ObjectId("p1"), cliente_id: ObjectId("u1"), total: 220 }
```

### Regra Geral

| Situação | Padrão |
|---|---|
| Dados sempre lidos juntos | Embedded |
| Dados independentes/compartilhados | Referenced |
| Array pode crescer ilimitadamente | Referenced |
| Relação 1:1 ou 1:poucos | Embedded |
| Relação 1:muitos (milhares) | Referenced |

---

## Mongoose (Node.js)

```javascript
const mongoose = require('mongoose');

// Conexão
await mongoose.connect('mongodb://localhost:27017/minhaBase');

// Schema
const usuarioSchema = new mongoose.Schema({
  nome:   { type: String, required: true, trim: true },
  email:  { type: String, required: true, unique: true, lowercase: true },
  idade:  { type: Number, min: 0, max: 150 },
  ativo:  { type: Boolean, default: true },
  tags:   [String],
  endereco: {
    cidade: String,
    uf:     { type: String, maxlength: 2 }
  },
  criadoEm: { type: Date, default: Date.now }
});

// Métodos
usuarioSchema.methods.apresentar = function() {
  return `${this.nome}, ${this.idade} anos`;
};

// Statics
usuarioSchema.statics.buscarAtivos = function() {
  return this.find({ ativo: true });
};

// Virtual
usuarioSchema.virtual('adulto').get(function() {
  return this.idade >= 18;
});

// Model
const Usuario = mongoose.model('Usuario', usuarioSchema);

// CRUD
const user = await Usuario.create({ nome: "Ana", email: "ana@mail.com", idade: 25 });
const todos = await Usuario.find({ ativo: true }).sort({ nome: 1 }).limit(10);
await Usuario.findByIdAndUpdate(id, { $set: { idade: 26 } });
await Usuario.findByIdAndDelete(id);
```

---

*Fonte: [W3Schools MongoDB](https://www.w3schools.com/mongodb/) · [MongoDB Docs](https://www.mongodb.com/docs/manual/)*
