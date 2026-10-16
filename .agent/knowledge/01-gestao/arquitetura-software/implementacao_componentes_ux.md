---json
{
  "id": "implementacao_componentes_ux",
  "title": "💻 Implementação de Componentes UX - Guia de Referência",
  "categoria": "01-gestao",
  "subcategoria": "arquitetura-software",
  "resumo": "Guia tecnico e referencias sobre 💻 Implementação de Componentes UX - Guia de Referência.",
  "gatilhos": [
    "arquitetura",
    "componentes",
    "gestao",
    "guia",
    "implementacao",
    "software"
  ],
  "perguntas_tipo": [
    "Como utilizar 💻 Implementação de Componentes UX - Guia de Referência?",
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

# 💻 Implementação de Componentes UX - Guia de Referência

**Data:** [DATA_ATUAL]
**Versão:** 1.0
**Status:** Código de Referência para Componentes Base
**Contexto:** React + Tailwind CSS + TypeScript

---

## 🎯 Visão Geral

Este guia fornece a implementação de referência para três componentes de UX essenciais para substituir interações de Select/Dropdown:
1. **ButtonGroup** (Seleção de Texto)
2. **ColorButton** (Seleção de Status/Cor)
3. **IconButtonGroup** (Seleção de Tipo/Ação)

O código é agnóstico de domínio e pode ser usado em qualquer projeto React moderno.

---

## 🏗️ Estrutura Recomendada

```
resources/js/
├── components/
│   ├── ui/
│   │   ├── ButtonGroup.tsx
│   │   ├── ColorButton.tsx
│   │   ├── IconButtonGroup.tsx
│   │   └── index.ts
│   └── ...
├── types/
│   └── index.d.ts
└── utils/
    └── cn.ts
```

---

## 💻 Código dos Componentes

### 1. Utilitário (cn.ts)

Essencial para combinar classes Tailwind condicionalmente.

```typescript
// resources/js/utils/cn.ts
import { type ClassValue, clsx } from 'clsx';
import { twMerge } from 'tailwind-merge';

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
```

### 2. ButtonGroup.tsx

Componente versátil para seleções de texto.

```typescript
import React from 'react';
import { cn } from '@/utils/cn';

interface ButtonGroupProps {
  options: { value: string; label: string; icon?: React.ReactNode }[];
  value: string | string[];
  onChange: (value: any) => void;
  multiple?: boolean;
  className?: string;
  size?: 'sm' | 'md' | 'lg';
}

export const ButtonGroup = ({
  options,
  value,
  onChange,
  multiple = false,
  className,
  size = 'md'
}: ButtonGroupProps) => {
  const isSelected = (val: string) => 
    multiple ? (value as string[]).includes(val) : value === val;

  const handleClick = (val: string) => {
    if (multiple) {
      const current = (value as string[]) || [];
      const newValue = current.includes(val)
        ? current.filter(v => v !== val)
        : [...current, val];
      onChange(newValue);
    } else {
      onChange(val);
    }
  };

  const sizeResult = {
    sm: 'px-3 py-1.5 text-xs',
    md: 'px-4 py-2 text-sm',
    lg: 'px-6 py-3 text-base',
  };

  return (
    <div className={cn("flex flex-wrap gap-2", className)}>
      {options.map((opt) => (
        <button
          key={opt.value}
          type="button"
          onClick={() => handleClick(opt.value)}
          className={cn(
            "rounded-lg border font-medium transition-all",
            sizeResult[size],
            isSelected(opt.value)
              ? "bg-blue-600 text-white border-blue-600 shadow-md"
              : "bg-white text-gray-700 border-gray-300 hover:bg-gray-50"
          )}
        >
          {opt.icon && <span className="mr-2">{opt.icon}</span>}
          {opt.label}
        </button>
      ))}
    </div>
  );
};
```

### 3. ColorButton.tsx

Para status, prioridades e categorias coloridas.

```typescript
import React from 'react';
import { cn } from '@/utils/cn';

interface ColorButtonProps {
  value: string;
  color: string; // Tailwind class (bg-red-500) ou Hex
  label?: string;
  selected?: boolean;
  onClick: () => void;
  className?: string;
}

export const ColorButton = ({
  value,
  color,
  label,
  selected,
  onClick,
  className
}: ColorButtonProps) => {
  const isHex = color.startsWith('#');
  
  return (
    <button
      type="button"
      onClick={onClick}
      className={cn(
        "flex items-center justify-center rounded-lg border-2 transition-all p-4",
        selected 
          ? "border-gray-900 shadow-lg scale-105" 
          : "border-transparent hover:brightness-90",
        !isHex && color, // Se for classe tailwind
        className
      )}
      style={isHex ? { backgroundColor: color } : undefined}
      aria-label={label || value}
      title={label || value}
    >
      {label && <span className="text-white font-bold text-shadow-sm">{label}</span>}
    </button>
  );
};
```

---

## 🔗 Exemplo de Integração (Genérico)

Abaixo um exemplo de formulário de "Configuração de Produto" que utiliza os componentes.

```typescript
// pages/Product/Create.tsx
import React from 'react';
import { useForm } from '@inertiajs/react';
import { ButtonGroup } from '@/components/ui/ButtonGroup';
import { ColorButton } from '@/components/ui/ColorButton';

export default function CreateProduct() {
  const { data, setData, post } = useForm({
    category: 'electronics',
    tags: [],
    status: 'draft',
    priority: 'normal'
  });

  return (
    <form onSubmit={(e) => { e.preventDefault(); post('/products'); }}>
      
      {/* 1. Seleção Simples (ButtonGroup) */}
      <div className="mb-6">
        <label className="block mb-2 font-bold">Categoria</label>
        <ButtonGroup
          value={data.category}
          onChange={(val) => setData('category', val)}
          options={[
            { value: 'electronics', label: 'Eletrônicos' },
            { value: 'furniture', label: 'Móveis' },
            { value: 'clothing', label: 'Roupas' }
          ]}
        />
      </div>

      {/* 2. Seleção Múltipla (ButtonGroup Multiple) */}
      <div className="mb-6">
        <label className="block mb-2 font-bold">Tags</label>
        <ButtonGroup
          multiple
          value={data.tags}
          onChange={(val) => setData('tags', val)}
          options={[
            { value: 'new', label: 'Lançamento' },
            { value: 'promo', label: 'Promoção' },
            { value: 'limited', label: 'Limitado' }
          ]}
        />
      </div>

      {/* 3. Seleção Visual (ColorButton) */}
      <div className="mb-6">
        <label className="block mb-2 font-bold">Status</label>
        <div className="flex gap-4">
          <ColorButton
            value="active"
            label="Ativo"
            color="#10B981" // Verde
            selected={data.status === 'active'}
            onClick={() => setData('status', 'active')}
          />
          <ColorButton
            value="draft"
            label="Rascunho"
            color="#F59E0B" // Amarelo
            selected={data.status === 'draft'}
            onClick={() => setData('status', 'draft')}
          />
          <ColorButton
            value="archived"
            label="Arquivado"
            color="#6B7280" // Cinza
            selected={data.status === 'archived'}
            onClick={() => setData('status', 'archived')}
          />
        </div>
      </div>

      <button type="submit" className="btn-primary">Salvar Produto</button>
    </form>
  );
}
```

---

## 📊 Checklist de Validação

- [ ] Componentes renderizam sem erros de TS.
- [ ] Utilitário `cn` (tailwind-merge) instalado.
- [ ] Acessibilidade (Tab/Enter) testada.
- [ ] Responsividade em mobile verificada.
