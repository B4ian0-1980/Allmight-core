---json
{
  "id": "padroes-react19",
  "title": "⚛️ Padrões React 19 - Guia Completo",
  "categoria": "04-frameworks",
  "subcategoria": "react",
  "resumo": "Guia tecnico e referencias sobre ⚛️ Padrões React 19 - Guia Completo.",
  "gatilhos": [
    "completo",
    "frameworks",
    "guia",
    "padroes",
    "react",
    "react19"
  ],
  "perguntas_tipo": [
    "Como utilizar ⚛️ Padrões React 19 - Guia Completo?",
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

# ⚛️ Padrões React 19 - Guia Completo

**Data:** 2025-01-27  
**Versão:** 1.0  
**Status:** Referência Completa para Desenvolvimento por IA  
**Contexto:** Sistema SESAU Eventos - React 19 + TypeScript + Inertia 2

---

## 📝 Classificação de Tarefa

**Tipo:** 🏗️ **Arquitetura** - Padrões e convenções React 19  
**Modo:** 🏗️ **Modo Arquiteto** - Decisões sobre padrões React

---

## 🎯 Decisão Técnica

**O que será feito:**
Documentar padrões, hooks, e práticas recomendadas do React 19 para garantir código consistente, performático e manutenível.

**Abordagem:**
- **React 19:** Padrões mais recentes
- **TypeScript:** Type safety
- **Hooks:** Custom hooks e hooks nativos
- **Performance:** Memoização e otimizações
- **Estrutura:** Organização de código

---

## 💡 Justificativa

**Por que essa abordagem:**
1. **React 19:** Versão mais recente, melhor performance
2. **TypeScript:** Type safety reduz bugs
3. **Hooks:** Padrão moderno, mais simples
4. **Performance:** Otimizações garantem UX fluida
5. **Estrutura:** Organização facilita manutenção

**Alternativas Consideradas:**
1. **React com classes** - ❌ Rejeitada: padrão antigo, mais verboso
2. **JavaScript puro** - ❌ Rejeitada: TypeScript oferece type safety

**Trade-offs:**
- ✅ **Ganhos:** Código moderno, type-safe, performático
- ⚠️ **Custos:** Curva de aprendizado TypeScript (mas vale a pena)
- ✅ **ROI:** Muito alto - código mais seguro e manutenível

---

## 📊 Análise de Impacto

### O que muda no sistema?
- **Padrões:** Padrões React 19 estabelecidos
- **Estrutura:** Organização de componentes definida
- **Performance:** Otimizações aplicadas
- **Type Safety:** TypeScript em todos os componentes

### Riscos Identificados
1. **Risco de Performance:** Componentes podem ser lentos
   - **Mitigação:** Memoização, lazy loading
2. **Risco de Bugs:** Type errors podem ocorrer
   - **Mitigação:** TypeScript, validação

### Custos
- **Desenvolvimento:** Tempo para seguir padrões
- **Manutenção:** Manter padrões atualizados

### Breaking Changes
- ❌ **Nenhum:** Padrões não alteram código existente

---

## ✅ Critérios de Aceite

### Validação
- ✅ Padrões React 19 documentados
- ✅ Exemplos práticos fornecidos
- ✅ Estrutura de projeto definida
- ✅ Performance otimizada

### Casos Cobertos
- ✅ Componentes funcionais
- ✅ Hooks (nativos e customizados)
- ✅ Context API
- ✅ TypeScript
- ✅ Performance
- ✅ Testes

---

## 🏗️ Estrutura de Projeto React

### Organização de Pastas

```
resources/js/
├── components/
│   ├── ui/              # Componentes UI reutilizáveis
│   │   ├── ButtonGroup.tsx
│   │   ├── ColorButton.tsx
│   │   └── IconButtonGroup.tsx
│   ├── layout/          # Componentes de layout
│   │   ├── Header.tsx
│   │   ├── Footer.tsx
│   │   └── Sidebar.tsx
│   └── features/        # Componentes específicos de features
│       ├── pacientes/
│       └── atendimentos/
├── hooks/               # Custom hooks
│   ├── usePaciente.ts
│   ├── useTheme.ts
│   └── useDebounce.ts
├── contexts/            # Context providers
│   ├── ThemeContext.tsx
│   └── AuthContext.tsx
├── types/               # TypeScript types
│   ├── components.ts
│   ├── paciente.ts
│   └── atendimento.ts
├── utils/               # Funções utilitárias
│   ├── cn.ts
│   ├── format.ts
│   └── validation.ts
├── pages/               # Páginas (Inertia)
│   ├── Pacientes/
│   │   ├── Index.tsx
│   │   └── Create.tsx
│   └── Atendimentos/
└── app.tsx              # Entry point
```

---

## 🎣 Hooks Nativos

### useState

```typescript
import { useState } from 'react';

// Estado simples
const [nome, setNome] = useState<string>('');

// Estado com valor inicial
const [idade, setIdade] = useState<number>(0);

// Estado com objeto
const [paciente, setPaciente] = useState<Paciente | null>(null);

// Atualização funcional (quando depende do valor anterior)
const [contador, setContador] = useState(0);
setContador(prev => prev + 1);
```

### useEffect

```typescript
import { useEffect, useState } from 'react';

// Executar após render
useEffect(() => {
    // Código aqui
}, []); // Array vazio = executa apenas uma vez

// Com dependências
useEffect(() => {
    fetchData();
}, [id]); // Executa quando 'id' muda

// Cleanup
useEffect(() => {
    const timer = setInterval(() => {
        // ...
    }, 1000);

    return () => {
        clearInterval(timer); // Cleanup
    };
}, []);
```

### useCallback

```typescript
import { useCallback, useState } from 'react';

// Memoizar função
const handleClick = useCallback((id: string) => {
    // Lógica
}, []); // Dependências

// Com dependências
const handleSubmit = useCallback((data: FormData) => {
    submitData(data);
}, [submitData]); // Re-cria se submitData mudar
```

### useMemo

```typescript
import { useMemo } from 'react';

// Memoizar cálculo pesado
const pacientesFiltrados = useMemo(() => {
    return pacientes.filter(p => p.triagem === 'vermelho');
}, [pacientes]); // Recalcula apenas se pacientes mudar

// Memoizar objeto
const config = useMemo(() => ({
    theme: 'light',
    locale: 'pt-BR',
}), []); // Cria apenas uma vez
```

### useContext

```typescript
import { useContext } from 'react';
import { ThemeContext } from '@/contexts/ThemeContext';

const Component = () => {
    const { theme, toggleTheme } = useContext(ThemeContext);
    
    return <div className={theme}>...</div>;
};
```

---

## 🎨 Custom Hooks

### Hook para Data Fetching

```typescript
// hooks/usePacientes.ts
import { useState, useEffect } from 'react';
import { router } from '@inertiajs/react';

interface Paciente {
    id: string;
    nome_completo: string;
    triagem: string;
}

interface UsePacientesReturn {
    pacientes: Paciente[];
    isLoading: boolean;
    error: Error | null;
    refetch: () => void;
}

export function usePacientes(filtros?: { triagem?: string }): UsePacientesReturn {
    const [pacientes, setPacientes] = useState<Paciente[]>([]);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState<Error | null>(null);

    const fetchPacientes = useCallback(async () => {
        setIsLoading(true);
        setError(null);

        try {
            router.get('/api/pacientes', filtros || {}, {
                preserveState: true,
                onSuccess: (page) => {
                    setPacientes(page.props.pacientes);
                    setIsLoading(false);
                },
                onError: (errors) => {
                    setError(new Error('Erro ao carregar pacientes'));
                    setIsLoading(false);
                },
            });
        } catch (err) {
            setError(err as Error);
            setIsLoading(false);
        }
    }, [filtros]);

    useEffect(() => {
        fetchPacientes();
    }, [fetchPacientes]);

    return {
        pacientes,
        isLoading,
        error,
        refetch: fetchPacientes,
    };
}
```

### Hook para Theme

```typescript
// hooks/useTheme.ts
import { useContext } from 'react';
import { ThemeContext } from '@/contexts/ThemeContext';

export function useTheme() {
    const context = useContext(ThemeContext);
    
    if (!context) {
        throw new Error('useTheme must be used within ThemeProvider');
    }
    
    return context;
}
```

### Hook para Debounce

```typescript
// hooks/useDebounce.ts
import { useState, useEffect } from 'react';

export function useDebounce<T>(value: T, delay: number = 500): T {
    const [debouncedValue, setDebouncedValue] = useState<T>(value);

    useEffect(() => {
        const timer = setTimeout(() => {
            setDebouncedValue(value);
        }, delay);

        return () => {
            clearTimeout(timer);
        };
    }, [value, delay]);

    return debouncedValue;
}

// Uso
const [searchTerm, setSearchTerm] = useState('');
const debouncedSearch = useDebounce(searchTerm, 300);

useEffect(() => {
    if (debouncedSearch) {
        // Buscar...
    }
}, [debouncedSearch]);
```

---

## 🎭 Context API

### Criando Context

```typescript
// contexts/ThemeContext.tsx
import { createContext, useState, ReactNode } from 'react';

interface ThemeContextType {
    theme: 'light' | 'dark';
    toggleTheme: () => void;
}

const ThemeContext = createContext<ThemeContextType | undefined>(undefined);

export function ThemeProvider({ children }: { children: ReactNode }) {
    const [theme, setTheme] = useState<'light' | 'dark'>('light');

    const toggleTheme = () => {
        setTheme(prev => prev === 'light' ? 'dark' : 'light');
    };

    return (
        <ThemeContext.Provider value={{ theme, toggleTheme }}>
            {children}
        </ThemeContext.Provider>
    );
}

export { ThemeContext };
```

### Usando Context

```typescript
// Component usando Context
import { useTheme } from '@/hooks/useTheme';

export function Header() {
    const { theme, toggleTheme } = useTheme();

    return (
        <header className={theme === 'dark' ? 'bg-gray-900' : 'bg-white'}>
            <button onClick={toggleTheme}>
                {theme === 'light' ? '🌙' : '☀️'}
            </button>
        </header>
    );
}
```

---

## 📘 TypeScript com React

### Tipos de Componentes

```typescript
// Componente funcional com props tipadas
interface ButtonProps {
    label: string;
    onClick: () => void;
    disabled?: boolean;
    variant?: 'primary' | 'secondary';
}

export function Button({ label, onClick, disabled = false, variant = 'primary' }: ButtonProps) {
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
```

### Tipos de Estado

```typescript
// Estado tipado
interface Paciente {
    id: string;
    nome_completo: string;
    triagem: 'vermelho' | 'amarelo' | 'verde' | 'azul';
}

const [paciente, setPaciente] = useState<Paciente | null>(null);
```

### Tipos de Eventos

```typescript
// Event handlers tipados
const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setValue(e.target.value);
};

const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    // ...
};

const handleClick = (e: React.MouseEvent<HTMLButtonElement>) => {
    // ...
};
```

---

## ⚡ Performance

### React.memo

```typescript
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

### useMemo para Cálculos Pesados

```typescript
const pacientesFiltrados = useMemo(() => {
    return pacientes
        .filter(p => p.triagem === filtroTriagem)
        .sort((a, b) => a.nome_completo.localeCompare(b.nome_completo));
}, [pacientes, filtroTriagem]);
```

### useCallback para Funções

```typescript
const handleClick = useCallback((id: string) => {
    setSelectedId(id);
}, []); // Função estável, não recria a cada render
```

### Lazy Loading

```typescript
import { lazy, Suspense } from 'react';

const PacienteList = lazy(() => import('@/components/PacienteList'));

function App() {
    return (
        <Suspense fallback={<div>Carregando...</div>}>
            <PacienteList />
        </Suspense>
    );
}
```

---

## 🧪 Testes

### Configuração Vitest

```typescript
// vitest.config.ts
import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';
import path from 'path';

export default defineConfig({
    plugins: [react()],
    test: {
        environment: 'jsdom',
        setupFiles: ['./tests/setup.ts'],
    },
    resolve: {
        alias: {
            '@': path.resolve(__dirname, './resources/js'),
        },
    },
});
```

### Teste de Componente

```typescript
// components/ui/__tests__/ButtonGroup.test.tsx
import { describe, it, expect } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { ButtonGroup } from '../ButtonGroup';

describe('ButtonGroup', () => {
    it('renderiza opções corretamente', () => {
        render(
            <ButtonGroup
                options={[
                    { value: 'op1', label: 'Opção 1' },
                    { value: 'op2', label: 'Opção 2' },
                ]}
                value=""
                onChange={() => {}}
            />
        );

        expect(screen.getByText('Opção 1')).toBeInTheDocument();
        expect(screen.getByText('Opção 2')).toBeInTheDocument();
    });

    it('chama onChange quando clicado', () => {
        const handleChange = vi.fn();
        render(
            <ButtonGroup
                options={[{ value: 'op1', label: 'Opção 1' }]}
                value=""
                onChange={handleChange}
            />
        );

        fireEvent.click(screen.getByText('Opção 1'));
        expect(handleChange).toHaveBeenCalledWith('op1');
    });
});
```

---

## 📋 Convenções de Nomenclatura

### Componentes
- ✅ **PascalCase:** `ButtonGroup.tsx`, `PacienteCard.tsx`
- ❌ ~~camelCase: `buttonGroup.tsx`~~
- ❌ ~~kebab-case: `button-group.tsx`~~

### Hooks
- ✅ **camelCase com prefixo `use`:** `usePaciente.ts`, `useTheme.ts`
- ❌ ~~PascalCase: `UsePaciente.ts`~~

### Types/Interfaces
- ✅ **PascalCase:** `Paciente`, `ButtonProps`
- ✅ **Interface:** `interface Paciente { ... }`
- ✅ **Type:** `type Status = 'aguardando' | 'em_atendimento'`

### Arquivos
- ✅ **Componentes:** `.tsx`
- ✅ **Hooks/Utils:** `.ts`
- ✅ **Types:** `.ts`

---

## 🎯 Padrões de Componentes

### Componente Funcional com TypeScript

```typescript
import { FC } from 'react';

interface Props {
    title: string;
    children: React.ReactNode;
}

export const Card: FC<Props> = ({ title, children }) => {
    return (
        <div className="card">
            <h2>{title}</h2>
            {children}
        </div>
    );
};
```

### Componente com Estado Local

```typescript
import { useState } from 'react';

export function SearchInput() {
    const [value, setValue] = useState('');

    return (
        <input
            type="text"
            value={value}
            onChange={(e) => setValue(e.target.value)}
            placeholder="Buscar..."
        />
    );
}
```

### Componente com Props Opcionais

```typescript
interface ButtonProps {
    label: string;
    onClick: () => void;
    variant?: 'primary' | 'secondary';
    size?: 'sm' | 'md' | 'lg';
    disabled?: boolean;
    icon?: React.ReactNode;
}

export function Button({
    label,
    onClick,
    variant = 'primary',
    size = 'md',
    disabled = false,
    icon,
}: ButtonProps) {
    return (
        <button
            onClick={onClick}
            disabled={disabled}
            className={`btn btn-${variant} btn-${size}`}
        >
            {icon && <span>{icon}</span>}
            {label}
        </button>
    );
}
```

---

## 🔍 Reflexão sobre Escalabilidade e Manutenibilidade

### Escalabilidade
Padrões React 19 bem definidos garantem que o código escale bem. Custom hooks permitem reutilização. Memoização garante performance mesmo com muitos componentes.

**Considerações futuras:**
- Adicionar padrões de code splitting conforme necessário
- Implementar lazy loading para rotas
- Considerar state management (Redux/Zustand) se necessário

### Manutenibilidade
Estrutura clara e padrões consistentes facilitam manutenção. TypeScript reduz bugs. Custom hooks encapsulam lógica reutilizável.

**Melhorias sugeridas:**
- Criar biblioteca de hooks compartilhados
- Documentar padrões de componentes
- Manter tipos TypeScript atualizados

---

**Última Atualização:** 2025-01-27  
**Baseado em:** `qi/Professional-React-v19.3.0-labs.md` + `qi/The Road to learn React.md`

