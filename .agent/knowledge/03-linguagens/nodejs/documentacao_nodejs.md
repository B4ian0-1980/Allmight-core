---json
{
  "id": "documentacao_nodejs",
  "title": "Node.js — Guia Completo",
  "categoria": "03-linguagens",
  "subcategoria": "nodejs",
  "resumo": "Guia tecnico e referencias sobre Node.js — Guia Completo.",
  "gatilhos": [
    "completo",
    "documentacao",
    "guia",
    "linguagens",
    "node",
    "nodejs"
  ],
  "perguntas_tipo": [
    "Como utilizar Node.js — Guia Completo?",
    "Quais as boas praticas de nodejs?"
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
  "dono": "stack-nodejs",
  "prioridade": 2
}
---

# Node.js — Guia Completo

**Fonte:** [nodejs.org](https://nodejs.org/docs/latest/api/) | **Versão:** 20+ LTS  
**Categoria:** Runtime JavaScript Server-Side  
**Uso:** Backend APIs, Server Actions (Next.js), Scripts, CLI Tools

---

## 1. O que é Node.js?

Node.js é um **runtime JavaScript** que roda fora do browser, usando o motor V8 do Chrome. Permite criar servidores web, APIs, scripts de automação e ferramentas de linha de comando.

```bash
# Verificar versão
node --version

# Executar arquivo
node app.js

# REPL interativo
node
```

---

## 2. Módulos Essenciais (Built-in)

### `fs` — Sistema de Arquivos
```javascript
import { readFile, writeFile, readdir, mkdir, unlink, stat } from 'fs/promises'
import { existsSync } from 'fs'

// Ler arquivo
const conteudo = await readFile('dados.json', 'utf-8')
const dados = JSON.parse(conteudo)

// Escrever arquivo
await writeFile('saida.json', JSON.stringify(dados, null, 2))

// Verificar se existe (síncrono — OK para verificações simples)
if (existsSync('./config.json')) {
  console.log('Arquivo existe')
}

// Listar diretório
const arquivos = await readdir('./src', { withFileTypes: true })
arquivos.forEach(item => {
  console.log(item.isDirectory() ? `📂 ${item.name}` : `📄 ${item.name}`)
})

// Criar pasta
await mkdir('./output', { recursive: true })

// Deletar arquivo
await unlink('./temp.txt')

// Info do arquivo
const info = await stat('./app.js')
console.log(`Tamanho: ${info.size} bytes`)
console.log(`Modificado: ${info.mtime}`)
```

### `path` — Manipulação de Caminhos
```javascript
import path from 'path'

path.join('/users', 'joao', 'docs')        // → /users/joao/docs
path.resolve('src', 'app.js')              // → /caminho/absoluto/src/app.js
path.basename('/src/app.js')               // → app.js
path.extname('foto.png')                   // → .png
path.dirname('/src/app.js')                // → /src
path.parse('/src/app.js')
// { root: '/', dir: '/src', base: 'app.js', ext: '.js', name: 'app' }

// __dirname e __filename em ESM
import { fileURLToPath } from 'url'
const __filename = fileURLToPath(import.meta.url)
const __dirname = path.dirname(__filename)
```

### `http` / `https` — Servidor Web
```javascript
import http from 'http'

const server = http.createServer((req, res) => {
  const { method, url } = req

  if (method === 'GET' && url === '/') {
    res.writeHead(200, { 'Content-Type': 'application/json' })
    res.end(JSON.stringify({ message: 'Hello Node.js!' }))
  }
  else if (method === 'GET' && url === '/users') {
    res.writeHead(200, { 'Content-Type': 'application/json' })
    res.end(JSON.stringify([{ id: 1, name: 'João' }]))
  }
  else {
    res.writeHead(404)
    res.end('Not Found')
  }
})

server.listen(3000, () => {
  console.log('🚀 Servidor rodando em http://localhost:3000')
})
```

### `crypto` — Criptografia e Hash
```javascript
import crypto from 'crypto'

// Hash MD5
const md5 = crypto.createHash('md5').update('texto').digest('hex')

// Hash SHA256
const sha256 = crypto.createHash('sha256').update('senha123').digest('hex')

// UUID v4
const uuid = crypto.randomUUID()

// Token aleatório
const token = crypto.randomBytes(32).toString('hex')

// HMAC (para assinaturas)
const hmac = crypto.createHmac('sha256', 'segredo')
  .update('dados')
  .digest('hex')

// Bcrypt-like com scrypt
const salt = crypto.randomBytes(16).toString('hex')
const hash = crypto.scryptSync('senha123', salt, 64).toString('hex')
```

### `events` — Event Emitter
```javascript
import { EventEmitter } from 'events'

class OrderService extends EventEmitter {
  createOrder(order) {
    // Lógica de criação...
    this.emit('orderCreated', order)
    return order
  }
}

const service = new OrderService()

service.on('orderCreated', (order) => {
  console.log(`📧 Email enviado para: ${order.email}`)
})

service.on('orderCreated', (order) => {
  console.log(`📊 Log: Pedido ${order.id} criado`)
})

service.createOrder({ id: 1, email: 'joao@email.com' })
```

### `child_process` — Executar Comandos
```javascript
import { exec, execSync, spawn } from 'child_process'

// Síncrono (bloqueia — use com cuidado)
const output = execSync('git status', { encoding: 'utf-8' })

// Assíncrono com callback
exec('ls -la', (error, stdout, stderr) => {
  if (error) console.error(error)
  console.log(stdout)
})

// Spawn (para processos longos, streaming)
const child = spawn('npm', ['install'], { stdio: 'inherit' })
child.on('close', (code) => console.log(`Exit code: ${code}`))
```

### `os` — Informações do Sistema
```javascript
import os from 'os'

os.platform()     // 'win32', 'linux', 'darwin'
os.arch()         // 'x64', 'arm64'
os.cpus().length  // Número de cores
os.totalmem()     // RAM total em bytes
os.freemem()      // RAM livre em bytes
os.homedir()      // Diretório do usuário
os.tmpdir()       // Diretório temp
os.hostname()     // Nome do computador
os.uptime()       // Uptime em segundos
```

### `url` — Parse de URLs
```javascript
const myUrl = new URL('https://api.exemplo.com/users?page=2&limit=10')

myUrl.hostname        // 'api.exemplo.com'
myUrl.pathname        // '/users'
myUrl.searchParams.get('page')   // '2'
myUrl.searchParams.get('limit')  // '10'

// Construir URL
const url = new URL('/api/users', 'https://meusite.com')
url.searchParams.set('page', '1')
url.toString()  // 'https://meusite.com/api/users?page=1'
```

### `process` — Processo Atual
```javascript
// Variáveis de ambiente
process.env.NODE_ENV      // 'development' ou 'production'
process.env.DATABASE_URL  // Variável do .env

// Argumentos da linha de comando
process.argv              // ['node', 'script.js', '--port', '3000']

// Diretório de trabalho
process.cwd()             // '/home/user/projeto'

// Sair do processo
process.exit(0)           // Sucesso
process.exit(1)           // Erro

// Eventos
process.on('uncaughtException', (err) => {
  console.error('Erro não tratado:', err)
  process.exit(1)
})

process.on('SIGINT', () => {
  console.log('Encerrando...')
  process.exit(0)
})

// Memória
const mem = process.memoryUsage()
console.log(`Heap: ${Math.round(mem.heapUsed / 1024 / 1024)} MB`)
```

### `stream` — Streams (Processar Dados em Pedaços)
```javascript
import { createReadStream, createWriteStream } from 'fs'
import { pipeline } from 'stream/promises'
import { createGzip } from 'zlib'

// Ler arquivo grande em chunks
const readStream = createReadStream('arquivo-grande.csv', 'utf-8')
readStream.on('data', (chunk) => {
  console.log(`Recebido ${chunk.length} bytes`)
})

// Copiar e comprimir arquivo
await pipeline(
  createReadStream('input.txt'),
  createGzip(),
  createWriteStream('input.txt.gz')
)

// Pipe simples (copiar)
createReadStream('origem.txt')
  .pipe(createWriteStream('destino.txt'))
```

### `timers` e `setTimeout/setInterval`
```javascript
// Delay com Promise
const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms))
await delay(2000) // Espera 2 segundos

// Interval
const timer = setInterval(() => {
  console.log('Tick...')
}, 1000)

// Parar após 5 segundos
setTimeout(() => clearInterval(timer), 5000)
```

---

## 3. Fetch API (Nativo desde Node 18)

```javascript
// GET
const res = await fetch('https://jsonplaceholder.typicode.com/users')
const users = await res.json()

// POST
const res = await fetch('https://api.exemplo.com/users', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name: 'João', email: 'joao@email.com' }),
})
const newUser = await res.json()

// Com timeout
const controller = new AbortController()
const timeout = setTimeout(() => controller.abort(), 5000)

const res = await fetch('https://api.lenta.com/dados', {
  signal: controller.signal,
})
clearTimeout(timeout)
```

---

## 4. ESModules vs CommonJS

### ESModules (RECOMENDADO para projetos novos)
```json
// package.json
{ "type": "module" }
```
```javascript
import express from 'express'
import { readFile } from 'fs/promises'
export default function handler() { }
export const config = { port: 3000 }
```

### CommonJS (Legado — ainda muito usado)
```javascript
const express = require('express')
const { readFile } = require('fs/promises')
module.exports = function handler() { }
module.exports.config = { port: 3000 }
```

---

## 5. Express.js — Framework Web Minimalista

```bash
npm install express
```

### Servidor básico
```javascript
import express from 'express'

const app = express()

// Middleware para JSON
app.use(express.json())

// Rotas
app.get('/api/users', async (req, res) => {
  const users = await getUsers()
  res.json(users)
})

app.get('/api/users/:id', async (req, res) => {
  const user = await getUserById(req.params.id)
  if (!user) return res.status(404).json({ error: 'Not found' })
  res.json(user)
})

app.post('/api/users', async (req, res) => {
  const { name, email } = req.body
  if (!name || !email) {
    return res.status(400).json({ error: 'Nome e email obrigatórios' })
  }
  const user = await createUser({ name, email })
  res.status(201).json(user)
})

app.put('/api/users/:id', async (req, res) => {
  const user = await updateUser(req.params.id, req.body)
  res.json(user)
})

app.delete('/api/users/:id', async (req, res) => {
  await deleteUser(req.params.id)
  res.status(204).end()
})

// Iniciar
app.listen(3000, () => {
  console.log('🚀 API rodando em http://localhost:3000')
})
```

### Middlewares
```javascript
// Logger
app.use((req, res, next) => {
  console.log(`${req.method} ${req.url}`)
  next()
})

// CORS
import cors from 'cors'
app.use(cors({ origin: 'http://localhost:3001' }))

// Auth middleware
function authMiddleware(req, res, next) {
  const token = req.headers.authorization?.split(' ')[1]
  if (!token) return res.status(401).json({ error: 'Token necessário' })

  try {
    req.user = verifyToken(token)
    next()
  } catch {
    res.status(403).json({ error: 'Token inválido' })
  }
}

// Usar em rotas específicas
app.get('/api/dashboard', authMiddleware, (req, res) => {
  res.json({ user: req.user })
})

// Error handler (SEMPRE no final)
app.use((err, req, res, next) => {
  console.error(err.stack)
  res.status(500).json({ error: 'Erro interno' })
})
```

### Organização por Rotas
```javascript
// routes/users.js
import { Router } from 'express'
const router = Router()

router.get('/', getAll)
router.get('/:id', getById)
router.post('/', create)
router.put('/:id', update)
router.delete('/:id', remove)

export default router

// app.js
import usersRouter from './routes/users.js'
app.use('/api/users', usersRouter)
```

---

## 6. Variáveis de Ambiente

```bash
# .env
PORT=3000
DATABASE_URL=mysql://root:senha@localhost:3306/meudb
JWT_SECRET=minha-chave-secreta
NODE_ENV=development
```

```bash
npm install dotenv
```

```javascript
import 'dotenv/config'

const port = process.env.PORT || 3000
const dbUrl = process.env.DATABASE_URL
```

---

## 7. npm — Gerenciador de Pacotes

### Comandos essenciais
```bash
# Inicializar projeto
npm init -y

# Instalar pacote
npm install express           # Dependência
npm install -D typescript     # DevDependency
npm install -g nodemon        # Global

# Remover
npm uninstall express

# Scripts
npm run dev                   # Executa script "dev"
npm start                     # Executa script "start"
npm test                      # Executa script "test"

# Atualizar
npm outdated                  # Ver desatualizados
npm update                    # Atualizar todos

# Limpar cache
npm cache clean --force
```

### `package.json` típico
```json
{
  "name": "minha-api",
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "nodemon src/app.js",
    "start": "node src/app.js",
    "build": "tsc",
    "test": "jest"
  },
  "dependencies": {
    "express": "^4.18.0",
    "@prisma/client": "^6.0.0"
  },
  "devDependencies": {
    "nodemon": "^3.0.0",
    "typescript": "^5.0.0"
  }
}
```

---

## 8. Async/Await e Promises

```javascript
// Promise básica
function fetchData(url) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (url) resolve({ data: 'resultado' })
      else reject(new Error('URL inválida'))
    }, 1000)
  })
}

// Async/Await
async function main() {
  try {
    const result = await fetchData('/api/users')
    console.log(result)
  } catch (error) {
    console.error('Erro:', error.message)
  }
}

// Promise.all (paralelo)
const [users, posts, stats] = await Promise.all([
  fetch('/api/users').then(r => r.json()),
  fetch('/api/posts').then(r => r.json()),
  fetch('/api/stats').then(r => r.json()),
])

// Promise.allSettled (não falha se um falhar)
const results = await Promise.allSettled([
  fetch('/api/endpoint1'),
  fetch('/api/endpoint2'),  // pode falhar
  fetch('/api/endpoint3'),
])
results.forEach(r => {
  if (r.status === 'fulfilled') console.log(r.value)
  if (r.status === 'rejected') console.error(r.reason)
})
```

---

## 9. Error Handling

```javascript
// Classe de erro customizada
class AppError extends Error {
  constructor(message, statusCode = 500) {
    super(message)
    this.statusCode = statusCode
    this.name = 'AppError'
  }
}

class NotFoundError extends AppError {
  constructor(resource) {
    super(`${resource} não encontrado`, 404)
  }
}

class ValidationError extends AppError {
  constructor(message) {
    super(message, 400)
  }
}

// Uso
async function getUser(id) {
  const user = await prisma.user.findUnique({ where: { id } })
  if (!user) throw new NotFoundError('Usuário')
  return user
}

// Express error handler
app.use((err, req, res, next) => {
  if (err instanceof AppError) {
    return res.status(err.statusCode).json({ error: err.message })
  }
  console.error(err)
  res.status(500).json({ error: 'Erro interno do servidor' })
})
```

---

## 10. Dicas de Performance

1. **Sempre use `async/await`** — Nunca bloqueie o event loop
2. **Use `Promise.all`** para requests paralelos
3. **Streams** para arquivos grandes (>10MB)
4. **Connection pooling** para bancos de dados
5. **`cluster` module** para usar múltiplos cores:

```javascript
import cluster from 'cluster'
import os from 'os'

if (cluster.isPrimary) {
  const numCPUs = os.cpus().length
  for (let i = 0; i < numCPUs; i++) {
    cluster.fork()
  }
} else {
  // Worker — inicia o servidor
  app.listen(3000)
}
```

---

## 11. Segurança em Produção (Hardening)

Para proteger sua API Node.js/Express em produção, use estas ferramentas **obrigatórias**:

### Helmet (Headers de Segurança)
Protege contra ataques comuns configurando headers HTTP (como X-XSS-Protection, HSTS).
```bash
npm install helmet
```
```javascript
import helmet from 'helmet'
app.use(helmet())
```

### Rate Limiting (Anti-DDoS / Brute Force)
Limita o número de requisições por IP.
```bash
npm install express-rate-limit
```
```javascript
import rateLimit from 'express-rate-limit'

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutos
  max: 100, // limite de 100 requisições por IP
  message: 'Muitas requisições deste IP, tente novamente em 15 minutos'
})

app.use(limiter)
```

### Validação de Entrada (Zod / Joi)
Nunca confie nos dados do usuário (`req.body`).
```bash
npm install zod
```
```javascript
import { z } from 'zod'

const userSchema = z.object({
  email: z.string().email(),
  senha: z.string().min(8)
})

app.post('/login', (req, res) => {
  const result = userSchema.safeParse(req.body)
  if (!result.success) {
    return res.status(400).json(result.error)
  }
  // ... processar login
})
```

---

*Fonte: [nodejs.org/docs/latest/api](https://nodejs.org/docs/latest/api/) — Consultado em 2026-02-14*
