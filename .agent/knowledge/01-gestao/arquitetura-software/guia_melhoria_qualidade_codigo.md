---json
{
  "id": "guia_melhoria_qualidade_codigo",
  "title": "📚 Guia de Melhoria de Qualidade de Código - Sugestões de Documentação",
  "categoria": "01-gestao",
  "subcategoria": "arquitetura-software",
  "resumo": "Guia tecnico e referencias sobre 📚 Guia de Melhoria de Qualidade de Código - Sugestões de Documentação.",
  "gatilhos": [
    "arquitetura",
    "codigo",
    "gestao",
    "guia",
    "melhoria",
    "qualidade",
    "software"
  ],
  "perguntas_tipo": [
    "Como utilizar 📚 Guia de Melhoria de Qualidade de Código - Sugestões de Documentação?",
    "Quais as boas praticas de arquitetura-software?"
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
  "dono": "stack-arquitetura-software",
  "prioridade": 2
}
---

# 📚 Guia de Melhoria de Qualidade de Código - Sugestões de Documentação

**Data:** 2025-01-27  
**Versão:** 1.0  
**Status:** Sugestões para Melhorar Qualidade  
**Contexto:** Sistema Novo, Desenvolvimento por IA (Cursor IDE)

---

## 🎯 Objetivo

Este documento lista **documentações adicionais** que você pode trazer para melhorar significativamente a qualidade do código gerado pela IA. Cada sugestão inclui:
- **O que é**
- **Por que melhora a qualidade**
- **O que trazer** (exemplos, padrões, guias)
- **Prioridade** (Alta, Média, Baixa)

---

## ⭐ ALTA PRIORIDADE - Impacto Imediato na Qualidade

### 1. 📐 Padrões de Código e Convenções

**O que é:**
Documentação detalhada sobre convenções de nomenclatura, formatação, estrutura de arquivos e padrões de código específicos do projeto.

**Por que melhora:**
- ✅ IA segue padrões consistentes automaticamente
- ✅ Código mais legível e manutenível
- ✅ Menos decisões ad-hoc durante desenvolvimento
- ✅ Reduz necessidade de refatoração

**O que trazer:**
- **Convenções de Nomenclatura:**
  - Classes: `PascalCase` ou `camelCase`?
  - Métodos: `camelCase` ou `snake_case`?
  - Constantes: `UPPER_SNAKE_CASE`?
  - Arquivos: `kebab-case` ou `PascalCase`?
  - Variáveis: `camelCase` ou `snake_case`?
  
- **Estrutura de Arquivos:**
  - Como organizar controllers?
  - Como organizar models?
  - Como organizar services?
  - Onde colocar helpers/utils?
  
- **Formatação:**
  - Tamanho de linha (80, 100, 120 caracteres)?
  - Indentação (tabs ou espaços, quantos)?
  - Quebra de linha (LF, CRLF)?
  - Aspas (simples ou duplas)?

**Exemplo do que trazer:**
```markdown
# Padrões de Nomenclatura

## PHP/Laravel
- Classes: PascalCase (ex: `PacienteController`)
- Métodos: camelCase (ex: `criarPaciente`)
- Variáveis: camelCase (ex: `$nomeCompleto`)
- Constantes: UPPER_SNAKE_CASE (ex: `STATUS_AGUARDANDO`)

## JavaScript/React
- Componentes: PascalCase (ex: `ButtonGroup`)
- Funções: camelCase (ex: `handleClick`)
- Variáveis: camelCase (ex: `nomeCompleto`)
- Constantes: UPPER_SNAKE_CASE (ex: `API_BASE_URL`)
```

**Prioridade:** ⭐⭐⭐ **ALTA** - Impacto imediato em consistência

---

### 2. 🏗️ Arquitetura de Pastas e Organização

**O que é:**
Estrutura detalhada de pastas do projeto, onde cada tipo de arquivo deve ficar, e como organizar código por domínio/feature.

**Por que melhora:**
- ✅ IA sabe exatamente onde criar arquivos
- ✅ Estrutura consistente desde o início
- ✅ Fácil navegação e manutenção
- ✅ Reduz confusão sobre onde colocar código

**O que trazer:**
- **Estrutura de Pastas Completa:**
  ```
  app/
    ├── Http/
    │   ├── Controllers/
    │   │   ├── Api/
    │   │   └── Web/
    │   ├── Requests/
    │   └── Resources/
    ├── Models/
    ├── Services/
    ├── Repositories/
    └── ...
  ```
  
- **Regras de Organização:**
  - Quando usar Services vs Controllers?
  - Quando criar Repositories?
  - Como organizar por feature vs por tipo?
  - Onde colocar helpers compartilhados?

**Exemplo do que trazer:**
```markdown
# Estrutura de Pastas

## Laravel Backend
app/
  Http/
    Controllers/
      Api/          # API REST
      Web/          # Web controllers
    Requests/       # Form Requests (validação)
    Resources/      # API Resources (transformação)
  Models/          # Eloquent Models
  Services/        # Lógica de negócio
  Repositories/    # Abstração de dados
  Events/          # Eventos
  Listeners/       # Listeners de eventos
```

**Prioridade:** ⭐⭐⭐ **ALTA** - Fundamental para organização

---

### 3. 🔒 Padrões de Segurança Específicos

**O que é:**
Guia detalhado de práticas de segurança específicas do projeto, além das gerais (LGPD, HIPAA).

**Por que melhora:**
- ✅ IA implementa segurança corretamente desde o início
- ✅ Reduz vulnerabilidades
- ✅ Compliance garantido
- ✅ Menos revisões de segurança

**O que trazer:**
- **Validação de Dados:**
  - Quais campos são obrigatórios?
  - Quais validações específicas (CPF, CNS, CEP)?
  - Como sanitizar dados?
  
- **Autenticação e Autorização:**
  - Como implementar autenticação?
  - Como verificar permissões?
  - Padrões de tokens/sessões?
  
- **Proteção de Dados Sensíveis:**
  - Como criptografar dados?
  - Como mascarar dados em logs?
  - Como proteger APIs?

**Exemplo do que trazer:**
```markdown
# Padrões de Segurança

## Validação
- Sempre validar no backend (nunca confiar no frontend)
- Usar Form Requests do Laravel
- Validar CPF: 11 dígitos, algoritmo de validação
- Validar CNS: 15 dígitos, algoritmo específico

## Sanitização
- Sanitizar HTML (prevenir XSS)
- Escapar SQL (usar Eloquent, nunca raw queries)
- Validar tipos de arquivo upload

## Autenticação
- Usar Laravel Sanctum para API
- Tokens expiram em 24h
- Refresh tokens para renovação
```

**Prioridade:** ⭐⭐⭐ **ALTA** - Crítico para segurança

---

## ⭐⭐ MÉDIA PRIORIDADE - Melhora Qualidade Gradualmente

### 4. 🧪 Padrões de Testes Detalhados

**O que é:**
Guia específico de como escrever testes, estrutura de testes, e exemplos práticos.

**Por que melhora:**
- ✅ IA escreve testes consistentes
- ✅ Cobertura adequada desde o início
- ✅ Testes mais úteis e manuteníveis
- ✅ Reduz bugs em produção

**O que trazer:**
- **Estrutura de Testes:**
  - Como organizar testes (unit, feature, e2e)?
  - Onde colocar fixtures/factories?
  - Como nomear arquivos de teste?
  
- **Padrões de Testes:**
  - Como estruturar um teste (Arrange-Act-Assert)?
  - Quais casos testar sempre?
  - Como testar exceções?
  - Como testar integrações?

- **Exemplos Práticos:**
  - Exemplo de teste de Controller
  - Exemplo de teste de Service
  - Exemplo de teste de Model
  - Exemplo de teste de API

**Exemplo do que trazer:**
```markdown
# Padrões de Testes

## Estrutura de Teste (AAA)
```php
public function test_criar_paciente_com_dados_validos()
{
    // Arrange
    $dados = PacienteFactory::make();
    
    // Act
    $paciente = $this->service->criar($dados);
    
    // Assert
    $this->assertDatabaseHas('pacientes', ['nome' => $dados['nome']]);
    $this->assertEquals('verde', $paciente->triagem);
}
```

## Casos Sempre Testar
- Dados válidos
- Dados inválidos
- Campos obrigatórios faltando
- Valores fora do range
- Permissões/autenticação
```

**Prioridade:** ⭐⭐ **MÉDIA** - Melhora qualidade, mas não bloqueia desenvolvimento

---

### 5. 📡 Padrões de API REST

**O que é:**
Convenções específicas de como estruturar APIs REST, formatos de resposta, códigos HTTP, e tratamento de erros.

**Por que melhora:**
- ✅ APIs consistentes e previsíveis
- ✅ Melhor experiência para frontend
- ✅ Fácil integração
- ✅ Documentação automática

**O que trazer:**
- **Estrutura de Endpoints:**
  - Convenções de URLs (singular/plural)?
  - Versão de API (v1, v2)?
  - Nested resources?
  
- **Formato de Resposta:**
  - Estrutura padrão de sucesso
  - Estrutura padrão de erro
  - Paginação
  - Metadados
  
- **Códigos HTTP:**
  - Quando usar 200, 201, 204?
  - Quando usar 400, 401, 403, 404?
  - Quando usar 500?

**Exemplo do que trazer:**
```markdown
# Padrões de API REST

## Estrutura de Endpoint
GET    /api/v1/pacientes          # Listar
POST   /api/v1/pacientes          # Criar
GET    /api/v1/pacientes/{id}     # Buscar
PUT    /api/v1/pacientes/{id}     # Atualizar
DELETE /api/v1/pacientes/{id}     # Deletar

## Formato de Resposta (Sucesso)
{
  "data": { ... },
  "meta": { "timestamp": "..." }
}

## Formato de Resposta (Erro)
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Dados inválidos",
    "details": { ... }
  }
}
```

**Prioridade:** ⭐⭐ **MÉDIA** - Importante para APIs consistentes

---

### 6. 🗄️ Padrões de Banco de Dados

**O que é:**
Convenções de nomenclatura de tabelas, colunas, índices, migrations, e relacionamentos.

**Por que melhora:**
- ✅ Schema consistente
- ✅ Migrations bem estruturadas
- ✅ Relacionamentos claros
- ✅ Performance otimizada

**O que trazer:**
- **Nomenclatura:**
  - Tabelas: singular ou plural?
  - Colunas: snake_case?
  - Foreign keys: `{tabela}_id`?
  - Índices: como nomear?
  
- **Migrations:**
  - Como estruturar migrations?
  - Como fazer rollback seguro?
  - Quando usar seeds?
  
- **Relacionamentos:**
  - Convenções de foreign keys
  - Quando usar soft deletes?
  - Padrões de timestamps?

**Exemplo do que trazer:**
```markdown
# Padrões de Banco de Dados

## Nomenclatura
- Tabelas: plural, snake_case (ex: `pacientes`, `atendimentos`)
- Colunas: snake_case (ex: `nome_completo`, `data_nascimento`)
- Foreign keys: `{tabela}_id` (ex: `paciente_id`, `medico_id`)
- Índices: `idx_{tabela}_{coluna}` (ex: `idx_pacientes_cpf`)

## Migrations
- Sempre criar down() method
- Usar transactions quando possível
- Adicionar índices para foreign keys
- Adicionar timestamps (created_at, updated_at)
```

**Prioridade:** ⭐⭐ **MÉDIA** - Importante para consistência de dados

---

## ⭐ BAIXA PRIORIDADE - Nice to Have

### 7. 📝 Padrões de Documentação de Código

**O que é:**
Como documentar código, quais comentários adicionar, formato de JSDoc/PHPDoc.

**Por que melhora:**
- ✅ Código mais legível
- ✅ Documentação automática
- ✅ Melhor para manutenção

**O que trazer:**
- Formato de PHPDoc para PHP
- Formato de JSDoc para JavaScript
- Quando comentar vs quando não comentar
- Exemplos de documentação

**Prioridade:** ⭐ **BAIXA** - Já temos JSDoc nos componentes UX

---

### 8. 🚀 Padrões de Performance

**O que é:**
Guia de otimizações específicas, quando usar cache, como otimizar queries.

**Por que melhora:**
- ✅ Performance desde o início
- ✅ Menos problemas de performance depois

**O que trazer:**
- Quando usar eager loading
- Como evitar N+1 queries
- Quando usar cache
- Otimizações de frontend

**Prioridade:** ⭐ **BAIXA** - Pode ser adicionado depois

---

### 9. 📦 Padrões de Dependências

**O que é:**
Quais bibliotecas usar, quando adicionar dependências, como gerenciar versões.

**Por que melhora:**
- ✅ Dependências consistentes
- ✅ Menos conflitos
- ✅ Melhor manutenibilidade

**O que trazer:**
- Lista de dependências aprovadas
- Quando adicionar nova dependência
- Como gerenciar versões

**Prioridade:** ⭐ **BAIXA** - Pode ser definido conforme necessário

---

## 📋 Checklist de Documentação Recomendada

### ⭐⭐⭐ Alta Prioridade (Implementar Primeiro)
- [ ] **Padrões de Código e Convenções** - Nomenclatura, formatação, estrutura
- [ ] **Arquitetura de Pastas** - Onde colocar cada tipo de arquivo
- [ ] **Padrões de Segurança** - Validação, autenticação, proteção de dados

### ⭐⭐ Média Prioridade (Implementar Depois)
- [ ] **Padrões de Testes** - Estrutura, exemplos, casos de teste
- [ ] **Padrões de API REST** - Endpoints, respostas, códigos HTTP
- [ ] **Padrões de Banco de Dados** - Nomenclatura, migrations, relacionamentos

### ⭐ Baixa Prioridade (Nice to Have)
- [ ] **Padrões de Documentação** - PHPDoc, JSDoc, comentários
- [ ] **Padrões de Performance** - Otimizações, cache, queries
- [ ] **Padrões de Dependências** - Bibliotecas, versões, gerenciamento

---

## 🎯 Como Usar Este Guia

### Para Você (Usuário)

1. **Revise as sugestões de Alta Prioridade**
   - Essas têm maior impacto na qualidade
   - Comece por aqui se tempo é limitado

2. **Traga exemplos do seu projeto anterior**
   - Se você tem código de outro projeto que funciona bem
   - Padrões que você já usa e gosta
   - Estruturas que funcionaram bem

3. **Traga guias de referência**
   - PSR standards (PHP)
   - Airbnb Style Guide (JavaScript)
   - Laravel best practices
   - React best practices

4. **Traga exemplos de código**
   - Exemplos de "código bom"
   - Exemplos de "código ruim" (para evitar)
   - Padrões que você quer seguir

### Para a IA

A IA usará esta documentação para:
- ✅ Seguir padrões consistentes automaticamente
- ✅ Criar código que segue convenções do projeto
- ✅ Reduzir necessidade de refatoração
- ✅ Melhorar qualidade desde o início

---

## 📚 Fontes de Documentação Úteis

### Padrões PHP/Laravel
- **✅ PADROES_CODIGO_LARAVEL.md** - Guia completo de padrões (criado)
- **✅ LARAVEL_BEST_PRACTICES.md** - Boas práticas da comunidade (criado)
- **✅ Laravel 12/laravel-12.x.md** - Documentação completa (convertido do PDF)
- **PSR Standards:** https://www.php-fig.org/psr/
- **Laravel Docs:** https://laravel.com/docs

### Padrões JavaScript/React
- **Airbnb JavaScript Style Guide:** https://github.com/airbnb/javascript
- **React Best Practices:** Documentação oficial
- **TypeScript Style Guide:** Documentação oficial

### Padrões de API
- **REST API Design:** https://restfulapi.net/
- **JSON API Specification:** https://jsonapi.org/
- **OpenAPI Specification:** https://swagger.io/specification/

### Padrões de Testes
- **PHPUnit Best Practices:** Documentação oficial
- **Testing Library Best Practices:** Documentação oficial
- **Playwright Best Practices:** Documentação oficial

---

## ✅ Próximos Passos

1. **Revise este documento** e identifique o que é mais importante para seu projeto
2. **Traga documentação** das áreas de Alta Prioridade primeiro
3. **Compartilhe exemplos** de código que você quer seguir
4. **A IA criará documentos específicos** baseados no que você trouxer

---

**Última Atualização:** 2025-01-27  
**Status:** Guia de Referência - Aguardando Documentação Adicional

