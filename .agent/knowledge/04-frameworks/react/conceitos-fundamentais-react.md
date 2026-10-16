---json
{
  "id": "conceitos-fundamentais-react",
  "title": "📚 Conceitos Fundamentais React - Extraídos de Fontes Clássicas",
  "categoria": "04-frameworks",
  "subcategoria": "react",
  "resumo": "Guia tecnico e referencias sobre 📚 Conceitos Fundamentais React - Extraídos de Fontes Clássicas.",
  "gatilhos": [
    "conceitos",
    "fontes",
    "frameworks",
    "fundamentais",
    "react"
  ],
  "perguntas_tipo": [
    "Como utilizar 📚 Conceitos Fundamentais React - Extraídos de Fontes Clássicas?",
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

# 📚 Conceitos Fundamentais React - Extraídos de Fontes Clássicas

**Data:** 2025-01-27  
**Versão:** 1.0  
**Status:** Referência de Conceitos Fundamentais  
**Contexto:** Sistema SESAU Eventos - React 19 + TypeScript + Inertia 2

---

## 📝 Classificação de Tarefa

**Tipo:** 📚 **Documentação** - Conceitos fundamentais extraídos e adaptados  
**Modo:** 🏗️ **Modo Arquiteto** - Consolidação de conhecimento

---

## 🎯 Decisão Técnica

**O que será feito:**
Extrair conceitos fundamentais úteis dos livros React desatualizados (2015-2018), adaptá-los para React 19 (hooks ao invés de classes), e consolidar em um único documento de referência.

**Abordagem:**
- **Extrair:** Conceitos fundamentais que ainda são válidos
- **Adaptar:** Converter padrões antigos (classes) para padrões modernos (hooks)
- **Consolidar:** Um único documento de referência
- **Excluir:** Arquivos desatualizados após extração

---

## 💡 Justificativa

**Por que essa abordagem:**
1. **Preservar Conhecimento:** Conceitos fundamentais ainda são válidos
2. **Modernizar:** Adaptar para React 19 (hooks)
3. **Limpar:** Remover arquivos desatualizados que podem confundir
4. **Consolidar:** Um único documento de referência

**Alternativas Consideradas:**
1. **Manter livros antigos** - ❌ Rejeitada: podem confundir com padrões desatualizados
2. **Excluir sem extrair** - ❌ Rejeitada: perderia conhecimento útil

**Trade-offs:**
- ✅ **Ganhos:** Conhecimento preservado e modernizado, estrutura limpa
- ⚠️ **Custos:** Tempo para extrair e adaptar
- ✅ **ROI:** Alto - conhecimento útil preservado sem confusão

---

## 📊 Análise de Impacto

### O que muda no sistema?
- **Documentação:** Novo documento com conceitos fundamentais
- **Estrutura:** Arquivos desatualizados removidos
- **Clareza:** Apenas referências atualizadas mantidas

### Riscos Identificados
1. **Risco de Perda de Informação:** Algum conceito útil pode ser perdido
   - **Mitigação:** Extrair cuidadosamente, focar em conceitos fundamentais

### Custos
- **Tempo:** Extração e adaptação de conceitos

### Breaking Changes
- ❌ **Nenhum:** Apenas reorganização de documentação

---

## ✅ Critérios de Aceite

### Validação
- ✅ Conceitos fundamentais extraídos
- ✅ Padrões adaptados para React 19 (hooks)
- ✅ Documento consolidado criado
- ✅ Arquivos desatualizados excluídos

### Casos Cobertos
- ✅ Conceitos fundamentais (JSX, Props, State)
- ✅ Gerenciamento de estado
- ✅ Performance e otimizações
- ✅ Organização de código
- ✅ Arquitetura de componentes

---

## 📚 Conceitos Fundamentais Extraídos e Adaptados

### 1. JSX - JavaScript XML

**Conceito Fundamental (válido desde sempre):**

JSX é uma extensão de sintaxe do JavaScript que permite escrever código similar a HTML dentro do JavaScript.

**Exemplo Moderno (React 19 com Hooks):**

```typescript
// Componente funcional com JSX
export function Welcome({ name }: { name: string }) {
    return <h1>Olá, {name}!</h1>;
}

// JSX permite expressões JavaScript
export function UserInfo({ user }: { user: User }) {
    return (
        <div>
            <p>Nome: {user.name}</p>
            <p>Idade: {user.age}</p>
            {user.isActive && <span className="badge">Ativo</span>}
        </div>
    );
}
```

**Regras Importantes:**
- ✅ Use `className` ao invés de `class`
- ✅ Use `htmlFor` ao invés de `for`
- ✅ Componentes devem começar com letra maiúscula
- ✅ Elementos HTML devem começar com letra minúscula

---

### 2. Props - Propriedades

**Conceito Fundamental (válido desde sempre):**

Props são dados passados de um componente pai para um componente filho. Props são imutáveis (read-only).

**Exemplo Moderno (React 19 com TypeScript):**

```typescript
// Definindo props com TypeScript
interface ButtonProps {
    label: string;
    onClick: () => void;
    variant?: 'primary' | 'secondary';
    disabled?: boolean;
}

export function Button({ label, onClick, variant = 'primary', disabled = false }: ButtonProps) {
    return (
        <button
            onClick={onClick}
            disabled={disabled}
            className={`btn btn-${variant}`}
        >
            {label}
        </button>
    );
}

// Uso
<Button 
    label="Salvar" 
    onClick={handleSave} 
    variant="primary" 
/>
```

**Princípios:**
- ✅ Props são imutáveis (não modifique props dentro do componente)
- ✅ Props fluem de cima para baixo (unidirecional)
- ✅ Use TypeScript para type safety

---

### 3. State - Estado

**Conceito Fundamental (válido desde sempre):**

State é o estado interno de um componente. Quando state muda, o componente re-renderiza.

**Exemplo Moderno (React 19 com Hooks):**

```typescript
// Estado local com useState
import { useState } from 'react';

export function Counter() {
    const [count, setCount] = useState<number>(0);

    return (
        <div>
            <p>Contador: {count}</p>
            <button onClick={() => setCount(count + 1)}>
                Incrementar
            </button>
        </div>
    );
}

// Estado com objeto
export function Form() {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
    });

    const handleChange = (field: string, value: string) => {
        setFormData(prev => ({
            ...prev,
            [field]: value,
        }));
    };

    return (
        <form>
            <input
                value={formData.name}
                onChange={(e) => handleChange('name', e.target.value)}
            />
            <input
                value={formData.email}
                onChange={(e) => handleChange('email', e.target.value)}
            />
        </form>
    );
}
```

**Princípios:**
- ✅ State é privado ao componente
- ✅ State deve ser atualizado com funções setter
- ✅ Use função atualizadora quando depender do valor anterior
- ✅ Evite mutar state diretamente

---

### 4. Gerenciamento de Estado

**Conceito Fundamental (ainda válido):**

Em aplicações React, o gerenciamento de estado pode ser um desafio. Existem diferentes estratégias:

#### Estado Local (useState)

```typescript
// Para estado simples e local
const [value, setValue] = useState('');
```

#### Estado Compartilhado (Context API)

```typescript
// Para estado compartilhado entre componentes
const ThemeContext = createContext();

export function ThemeProvider({ children }) {
    const [theme, setTheme] = useState('light');
    
    return (
        <ThemeContext.Provider value={{ theme, setTheme }}>
            {children}
        </ThemeContext.Provider>
    );
}
```

#### Estado Global (Redux/Zustand - se necessário)

```typescript
// Use apenas se estado local e Context não forem suficientes
// Redux para aplicações muito complexas
// Zustand para casos intermediários
```

**Princípios:**
- ✅ Comece com estado local (useState)
- ✅ Use Context API para estado compartilhado
- ✅ Considere Redux/Zustand apenas se necessário
- ✅ Evite "prop drilling" (passar props por muitos níveis)

---

### 5. Performance e Otimizações

**Conceitos Fundamentais (ainda válidos):**

#### Memoização com React.memo

```typescript
// Memoizar componente para evitar re-renders desnecessários
import { memo } from 'react';

interface PacienteCardProps {
    paciente: Paciente;
    onSelect: (id: string) => void;
}

export const PacienteCard = memo<PacienteCardProps>(({ paciente, onSelect }) => {
    return (
        <div onClick={() => onSelect(paciente.id)}>
            {paciente.nome_completo}
        </div>
    );
}, (prevProps, nextProps) => {
    // Comparação customizada (opcional)
    return prevProps.paciente.id === nextProps.paciente.id;
});
```

#### useMemo para Cálculos Pesados

```typescript
// Memoizar cálculos pesados
const pacientesFiltrados = useMemo(() => {
    return pacientes
        .filter(p => p.triagem === filtroTriagem)
        .sort((a, b) => a.nome_completo.localeCompare(b.nome_completo));
}, [pacientes, filtroTriagem]);
```

#### useCallback para Funções

```typescript
// Memoizar funções para evitar recriação
const handleClick = useCallback((id: string) => {
    setSelectedId(id);
}, []); // Função estável, não recria a cada render
```

**Princípios:**
- ✅ Use memoização apenas quando necessário (não otimize prematuramente)
- ✅ Meça performance antes de otimizar
- ✅ React.memo para componentes pesados
- ✅ useMemo para cálculos pesados
- ✅ useCallback para funções passadas como props

---

### 6. Organização de Código

**Conceitos Fundamentais (ainda válidos):**

#### Estrutura de Pastas

```
resources/js/
├── components/
│   ├── ui/              # Componentes UI reutilizáveis
│   ├── layout/          # Componentes de layout
│   └── features/        # Componentes específicos de features
├── hooks/               # Custom hooks
├── contexts/            # Context providers
├── types/               # TypeScript types
├── utils/               # Funções utilitárias
└── pages/               # Páginas (Inertia)
```

#### Separação de Responsabilidades

```typescript
// ✅ BOM: Componente focado em UI
export function PacienteList({ pacientes }: { pacientes: Paciente[] }) {
    return (
        <ul>
            {pacientes.map(p => (
                <li key={p.id}>{p.nome_completo}</li>
            ))}
        </ul>
    );
}

// ✅ BOM: Lógica em custom hook
function usePacientes() {
    const [pacientes, setPacientes] = useState<Paciente[]>([]);
    // Lógica de busca, filtros, etc.
    return { pacientes, /* ... */ };
}

// ✅ BOM: Componente usa hook
export function PacientePage() {
    const { pacientes } = usePacientes();
    return <PacienteList pacientes={pacientes} />;
}
```

**Princípios:**
- ✅ Um componente = uma responsabilidade
- ✅ Extraia lógica para custom hooks
- ✅ Separe UI de lógica de negócio
- ✅ Organize por feature quando aplicável

---

### 7. Fluxo de Dados Unidirecional

**Conceito Fundamental (válido desde sempre):**

React usa fluxo de dados unidirecional: dados fluem de componentes pais para filhos através de props.

```typescript
// ✅ CORRETO: Dados fluem para baixo
function App() {
    const [count, setCount] = useState(0);
    
    return (
        <div>
            <Counter count={count} />
            <Button onClick={() => setCount(count + 1)} />
        </div>
    );
}

// ✅ CORRETO: Eventos fluem para cima
function Button({ onClick }: { onClick: () => void }) {
    return <button onClick={onClick}>Incrementar</button>;
}
```

**Princípios:**
- ✅ Props fluem para baixo (pai → filho)
- ✅ Eventos fluem para cima (filho → pai via callbacks)
- ✅ Estado deve estar no componente mais próximo que precisa dele

---

### 8. Componentes Puros

**Conceito Fundamental (válido desde sempre):**

Componentes devem ser "puros" - mesma entrada, mesma saída, sem efeitos colaterais.

```typescript
// ✅ PURO: Sempre retorna o mesmo resultado para as mesmas props
export function Welcome({ name }: { name: string }) {
    return <h1>Olá, {name}!</h1>;
}

// ❌ IMPURO: Tem efeito colateral
export function BadComponent({ name }: { name: string }) {
    document.title = `Olá, ${name}!`; // Efeito colateral!
    return <h1>Olá, {name}!</h1>;
}

// ✅ CORRETO: Use useEffect para efeitos colaterais
export function GoodComponent({ name }: { name: string }) {
    useEffect(() => {
        document.title = `Olá, ${name}!`;
    }, [name]);
    
    return <h1>Olá, {name}!</h1>;
}
```

**Princípios:**
- ✅ Componentes devem ser puros (sem efeitos colaterais no render)
- ✅ Use useEffect para efeitos colaterais
- ✅ Mesma entrada = mesma saída

---

### 9. Composição vs Herança

**Conceito Fundamental (válido desde sempre):**

React favorece composição ao invés de herança.

```typescript
// ✅ BOM: Composição
function Card({ children }: { children: React.ReactNode }) {
    return <div className="card">{children}</div>;
}

function CardHeader({ children }: { children: React.ReactNode }) {
    return <div className="card-header">{children}</div>;
}

function CardBody({ children }: { children: React.ReactNode }) {
    return <div className="card-body">{children}</div>;
}

// Uso
<Card>
    <CardHeader>Título</CardHeader>
    <CardBody>Conteúdo</CardBody>
</Card>

// ❌ EVITAR: Herança
// Não use extends em componentes React
```

**Princípios:**
- ✅ Use composição (children, props)
- ✅ Evite herança de componentes
- ✅ Crie componentes pequenos e reutilizáveis

---

### 10. Keys em Listas

**Conceito Fundamental (válido desde sempre):**

Sempre forneça uma `key` única ao renderizar listas.

```typescript
// ✅ CORRETO: Key única e estável
{pacientes.map(paciente => (
    <PacienteCard key={paciente.id} paciente={paciente} />
))}

// ❌ ERRADO: Sem key
{pacientes.map(paciente => (
    <PacienteCard paciente={paciente} />
))}

// ❌ ERRADO: Key com índice (se lista pode mudar ordem)
{pacientes.map((paciente, index) => (
    <PacienteCard key={index} paciente={paciente} />
))}
```

**Princípios:**
- ✅ Sempre use key em listas
- ✅ Key deve ser única e estável
- ✅ Evite usar índice como key (exceto em listas estáticas)

---

### 11. Conditional Rendering

**Conceito Fundamental (válido desde sempre):**

Renderize condicionalmente usando operadores JavaScript.

```typescript
// ✅ CORRETO: Conditional rendering
function UserProfile({ user }: { user: User | null }) {
    if (!user) {
        return <div>Carregando...</div>;
    }

    return (
        <div>
            <h1>{user.name}</h1>
            {user.isAdmin && <AdminPanel />}
            {user.hasNotifications ? (
                <NotificationBadge count={user.notificationCount} />
            ) : (
                <span>Sem notificações</span>
            )}
        </div>
    );
}
```

**Padrões:**
- ✅ `{condition && <Component />}` - Render se verdadeiro
- ✅ `{condition ? <A /> : <B />}` - Ternário
- ✅ `{condition ? <A /> : null}` - Render ou nada
- ✅ Early return para casos extremos

---

### 12. Event Handling

**Conceito Fundamental (válido desde sempre):**

React usa SyntheticEvents, uma camada sobre eventos nativos do browser.

```typescript
// ✅ CORRETO: Event handlers
function Form() {
    const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault(); // Previne comportamento padrão
        // Lógica de submit
    };

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const value = e.target.value;
        // Atualizar state
    };

    return (
        <form onSubmit={handleSubmit}>
            <input onChange={handleChange} />
        </form>
    );
}
```

**Princípios:**
- ✅ Use SyntheticEvents do React
- ✅ Previne comportamento padrão com `e.preventDefault()`
- ✅ Type events com TypeScript
- ✅ Passe funções, não resultados de funções

---

## 🔄 Migração de Conceitos Antigos para Modernos

### Classes → Hooks

**Antigo (Classes - 2015-2018):**
```javascript
class Counter extends Component {
    constructor(props) {
        super(props);
        this.state = { count: 0 };
    }

    componentDidMount() {
        // Lógica após montagem
    }

    render() {
        return <div>{this.state.count}</div>;
    }
}
```

**Moderno (Hooks - React 19):**
```typescript
function Counter() {
    const [count, setCount] = useState(0);

    useEffect(() => {
        // Lógica após montagem
    }, []);

    return <div>{count}</div>;
}
```

### Lifecycle Methods → useEffect

**Antigo:**
- `componentDidMount()` → `useEffect(() => {}, [])`
- `componentDidUpdate()` → `useEffect(() => {}, [deps])`
- `componentWillUnmount()` → `useEffect(() => { return () => {} }, [])`

**Moderno:**
```typescript
// Equivalente a componentDidMount
useEffect(() => {
    // Código aqui
}, []); // Array vazio = executa apenas uma vez

// Equivalente a componentDidUpdate
useEffect(() => {
    // Código aqui
}, [dependency]); // Executa quando dependency muda

// Equivalente a componentWillUnmount
useEffect(() => {
    return () => {
        // Cleanup aqui
    };
}, []);
```

---

## 📋 Checklist de Conceitos Fundamentais

### Ao Criar Componente
- [ ] Componente é funcional (não classe)
- [ ] Props tipadas com TypeScript
- [ ] Componente é puro (sem efeitos colaterais no render)
- [ ] Usa hooks para estado e efeitos

### Ao Gerenciar Estado
- [ ] Estado local com useState quando possível
- [ ] Context API para estado compartilhado
- [ ] Redux/Zustand apenas se necessário
- [ ] Evita prop drilling

### Ao Otimizar Performance
- [ ] Usa React.memo quando necessário
- [ ] Usa useMemo para cálculos pesados
- [ ] Usa useCallback para funções
- [ ] Não otimiza prematuramente

### Ao Renderizar Listas
- [ ] Sempre fornece key única
- [ ] Key é estável (não índice, exceto listas estáticas)
- [ ] Usa map() corretamente

---

## 🔍 Reflexão sobre Escalabilidade e Manutenibilidade

### Escalabilidade
Conceitos fundamentais bem compreendidos permitem criar código escalável. Padrões como composição, fluxo unidirecional e organização clara facilitam crescimento.

**Considerações futuras:**
- Manter conceitos fundamentais atualizados
- Adaptar padrões conforme React evolui
- Documentar mudanças importantes

### Manutenibilidade
Código baseado em conceitos fundamentais sólidos é mais fácil de manter. Padrões claros facilitam entendimento e modificação.

**Melhorias sugeridas:**
- Revisar periodicamente conceitos fundamentais
- Atualizar quando React introduz novos padrões
- Manter exemplos práticos atualizados

---

## 📚 Fontes

**Conceitos extraídos de:**
- "The Road to learn React" (Robin Wieruch, 2018) - Conceitos fundamentais
- "React - Guia do Iniciante" (2015) - Conceitos básicos

**Adaptados para:**
- React 19.3.0 (hooks, TypeScript, padrões modernos)

**Referência Principal:**
- `PADROES_REACT19.md` - Padrões completos e atualizados

---

**Última Atualização:** 2025-01-27  
**Status:** Conceitos fundamentais extraídos e adaptados para React 19

