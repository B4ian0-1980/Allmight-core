---json
{
  "id": "documentacao_jest",
  "title": "Jest — Guia Completo de Testes JavaScript/TypeScript",
  "categoria": "04-frameworks",
  "subcategoria": "react",
  "resumo": "Guia tecnico e referencias sobre Jest — Guia Completo de Testes JavaScript/TypeScript.",
  "gatilhos": [
    "completo",
    "documentacao",
    "frameworks",
    "guia",
    "javascript",
    "jest",
    "react",
    "testes"
  ],
  "perguntas_tipo": [
    "Como utilizar Jest — Guia Completo de Testes JavaScript/TypeScript?",
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

# Jest — Guia Completo de Testes JavaScript/TypeScript

**Fonte:** [jestjs.io](https://jestjs.io/) · [Docs](https://jestjs.io/docs/getting-started) · [API](https://jestjs.io/docs/api)  
**Versão:** Jest 29+  
**Categoria:** Testes · Frontend/Backend · JavaScript/TypeScript  
**Última Atualização do Conteúdo:** 2026-02-14  
**Último Acesso às Fontes:** 2026-02-14

---

## 1. O que é Jest?

Jest é o **framework de testes JavaScript** mantido pelo Meta. É o padrão em projetos React, Next.js, Node.js e TypeScript. Zero configuração na maioria dos casos.

---

## 2. Instalação

```bash
# npm
npm install --save-dev jest

# Com TypeScript
npm install --save-dev jest @types/jest ts-jest

# Criar config
npx jest --init
```

### `package.json`
```json
{
  "scripts": {
    "test": "jest",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage"
  }
}
```

### `jest.config.js` (TypeScript)
```javascript
module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'node',
  roots: ['<rootDir>/src'],
  testMatch: ['**/*.test.ts', '**/*.spec.ts'],
  collectCoverageFrom: ['src/**/*.ts', '!src/**/*.d.ts'],
}
```

---

## 3. Estrutura de Testes

```
src/
├── services/
│   ├── user.service.ts
│   └── user.service.test.ts    ← Junto do código
├── utils/
│   ├── helpers.ts
│   └── helpers.test.ts
└── __tests__/                  ← Ou em pasta separada
    └── api.test.ts
```

---

## 4. Anatomia de um Teste

```javascript
// sum.js
function sum(a, b) {
  return a + b
}
module.exports = sum

// sum.test.js
const sum = require('./sum')

describe('sum()', () => {
  test('soma 1 + 2 = 3', () => {
    expect(sum(1, 2)).toBe(3)
  })

  test('soma números negativos', () => {
    expect(sum(-1, -2)).toBe(-3)
  })

  test('soma com zero', () => {
    expect(sum(5, 0)).toBe(5)
  })
})
```

---

## 5. Matchers (Verificações)

### Igualdade
```javascript
expect(2 + 2).toBe(4)                    // Igualdade estrita (===)
expect({ name: 'João' }).toEqual({ name: 'João' })  // Deep equal (objetos)
expect(result).not.toBe(0)               // Negação
```

### Verdadeiro/Falso
```javascript
expect(null).toBeNull()
expect(undefined).toBeUndefined()
expect(value).toBeDefined()
expect(true).toBeTruthy()
expect(0).toBeFalsy()
```

### Números
```javascript
expect(value).toBeGreaterThan(3)
expect(value).toBeGreaterThanOrEqual(3.5)
expect(value).toBeLessThan(5)
expect(0.1 + 0.2).toBeCloseTo(0.3)      // Float comparison
```

### Strings
```javascript
expect('hello world').toMatch(/world/)
expect('hello world').toContain('world')
expect(errorMsg).toMatch('not found')
```

### Arrays e Iteráveis
```javascript
expect(['admin', 'user', 'editor']).toContain('admin')
expect(users).toHaveLength(3)
expect(new Set([1, 2, 3])).toContain(2)
```

### Objetos
```javascript
expect(user).toHaveProperty('name')
expect(user).toHaveProperty('address.city', 'São Paulo')
expect(response).toMatchObject({
  status: 200,
  data: { success: true }
})
```

### Exceções
```javascript
expect(() => {
  throw new Error('falha')
}).toThrow()

expect(() => dividir(10, 0)).toThrow('Division by zero')
expect(() => dividir(10, 0)).toThrow(DivisionError)
```

---

## 6. Setup e Teardown

```javascript
describe('UserService', () => {
  let db

  // Antes de TODOS os testes do describe
  beforeAll(async () => {
    db = await connectDatabase()
  })

  // Depois de TODOS os testes do describe
  afterAll(async () => {
    await db.close()
  })

  // Antes de CADA teste
  beforeEach(async () => {
    await db.clear()
    await db.seed()
  })

  // Depois de CADA teste
  afterEach(() => {
    jest.restoreAllMocks()
  })

  test('lista usuarios', async () => {
    const users = await UserService.getAll()
    expect(users).toHaveLength(3)
  })
})
```

---

## 7. Testes Assíncronos

```javascript
// Async/Await (RECOMENDADO)
test('busca usuário por id', async () => {
  const user = await fetchUser(1)
  expect(user.name).toBe('João')
})

// Promises
test('busca dados', () => {
  return fetchData().then(data => {
    expect(data).toBeDefined()
  })
})

// Rejeição
test('falha quando id inválido', async () => {
  await expect(fetchUser(-1)).rejects.toThrow('ID inválido')
})

// Resolve
test('resolve com dados', async () => {
  await expect(fetchUser(1)).resolves.toEqual({ id: 1, name: 'João' })
})
```

---

## 8. Mocks

### Mock de função
```javascript
test('callback é chamado', () => {
  const callback = jest.fn()

  executeWithCallback(callback)

  expect(callback).toHaveBeenCalled()
  expect(callback).toHaveBeenCalledTimes(1)
  expect(callback).toHaveBeenCalledWith('arg1', 'arg2')
})
```

### Mock de retorno
```javascript
const mockFn = jest.fn()
  .mockReturnValue(42)                 // Retorna sempre 42
  .mockReturnValueOnce(10)             // Retorna 10 na primeira chamada
  .mockResolvedValue({ id: 1 })        // Promise.resolve
  .mockRejectedValue(new Error('!'))   // Promise.reject
```

### Mock de módulo
```javascript
// Mock inteiro
jest.mock('./api')
const api = require('./api')

api.fetchUsers.mockResolvedValue([
  { id: 1, name: 'João' }
])

test('lista usuarios', async () => {
  const users = await api.fetchUsers()
  expect(users).toHaveLength(1)
})

// Mock parcial (mantém implementação real das outras funções)
jest.mock('./utils', () => ({
  ...jest.requireActual('./utils'),
  generateId: jest.fn().mockReturnValue('mock-id-123'),
}))
```

### Spy (observar sem alterar)
```javascript
const spy = jest.spyOn(Math, 'random').mockReturnValue(0.5)

const result = getRandomItem(['a', 'b', 'c'])

expect(spy).toHaveBeenCalled()
expect(result).toBe('b')

spy.mockRestore()  // Restaurar original
```

### Mock de Timer
```javascript
jest.useFakeTimers()

test('executa após delay', () => {
  const callback = jest.fn()

  setTimeout(callback, 1000)

  expect(callback).not.toHaveBeenCalled()

  jest.advanceTimersByTime(1000)

  expect(callback).toHaveBeenCalledTimes(1)
})
```

---

## 9. Snapshot Testing

```javascript
// Cria snapshot na primeira vez, compara nas seguintes
test('componente renderiza corretamente', () => {
  const tree = renderer.create(<Button label="Click" />).toJSON()
  expect(tree).toMatchSnapshot()
})

// Atualizar snapshots
// npx jest --updateSnapshot
```

---

## 10. Testes com Next.js / React

```bash
npm install --save-dev @testing-library/react @testing-library/jest-dom
```

```javascript
import { render, screen, fireEvent } from '@testing-library/react'
import '@testing-library/jest-dom'
import LoginForm from './LoginForm'

describe('LoginForm', () => {
  test('renderiza campos de email e senha', () => {
    render(<LoginForm />)

    expect(screen.getByLabelText('Email')).toBeInTheDocument()
    expect(screen.getByLabelText('Senha')).toBeInTheDocument()
    expect(screen.getByRole('button', { name: 'Entrar' })).toBeInTheDocument()
  })

  test('mostra erro com email inválido', async () => {
    render(<LoginForm />)

    fireEvent.change(screen.getByLabelText('Email'), {
      target: { value: 'invalido' },
    })
    fireEvent.click(screen.getByRole('button', { name: 'Entrar' }))

    expect(await screen.findByText('Email inválido')).toBeInTheDocument()
  })
})
```

---

## 11. Comandos

```bash
# Rodar todos
npx jest

# Rodar um arquivo
npx jest user.test.js

# Rodar testes que combinam com padrão
npx jest --testPathPattern="api"

# Watch mode (re-roda ao salvar)
npx jest --watch

# Coverage
npx jest --coverage

# Verbose
npx jest --verbose

# Parar no primeiro erro
npx jest --bail

# Rodar apenas testes alterados (com git)
npx jest --onlyChanged

# Atualizar snapshots
npx jest --updateSnapshot
```

---

## 12. Boas Práticas

1. **Arquivo de teste junto do código:** `user.service.ts` → `user.service.test.ts`
2. **Descreva o comportamento:** `describe('quando o usuário não está logado')`
3. **Use `beforeEach` para limpar estado**
4. **Restaure mocks:** `jest.restoreAllMocks()` no `afterEach`
5. **Evite testes frágeis:** Teste comportamento, não implementação
6. **Use matchers semânticos:** `toHaveBeenCalledWith()` > `toBe()`

---

*Fontes: [jestjs.io/docs](https://jestjs.io/docs/getting-started) · [jestjs.io/docs/api](https://jestjs.io/docs/api) — Acessado em 2026-02-14*
