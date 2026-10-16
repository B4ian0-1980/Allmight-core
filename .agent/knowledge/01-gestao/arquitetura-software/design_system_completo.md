---json
{
  "id": "design_system_completo",
  "title": "🎨 Design System Template - Base SDLC",
  "categoria": "01-gestao",
  "subcategoria": "arquitetura-software",
  "resumo": "Guia tecnico e referencias sobre 🎨 Design System Template - Base SDLC.",
  "gatilhos": [
    "arquitetura",
    "base",
    "completo",
    "design",
    "gestao",
    "sdlc",
    "software",
    "system"
  ],
  "perguntas_tipo": [
    "Como utilizar 🎨 Design System Template - Base SDLC?",
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

# 🎨 Design System Template - Base SDLC

**Data:** [DATA_ATUAL]
**Versão:** 1.0
**Status:** Template Base (Agnóstico)
**Contexto:** Base Estrutura, Tailwind CSS + shadcn/ui

---

## 📝 Classificação de Tarefa

**Tipo:** 🏗️ **Arquitetura** - Decisão estrutural e de design de sistema
**Modo:** 🏗️ **Modo Arquiteto** - Decisões de alto nível sobre design visual e tokens

---

## 🎯 Decisão Técnica

**O que será feito:**
Estabelecer um Design System base com tokens de design (cores, tipografia, espaçamentos, bordas, sombras, animações) para garantir consistência visual e acessibilidade.

**Abordagem:**
Design System baseado em:
- **Tailwind CSS** como framework de estilização.
- **shadcn/ui** como biblioteca de componentes base.
- **Tokens de design** estruturados e documentados.
- **Variáveis CSS** para valores reutilizáveis e suporte a temas (dark/light).

---

## 💡 Justificativa

1. **Consistência Visual:** Garante que todos os componentes sigam os mesmos padrões.
2. **Acessibilidade:** Tokens de cor verificados para WCAG 2.1 AA.
3. **Manutenibilidade:** Centralizar tokens facilita mudanças globais (theming).
4. **Produtividade:** Reduz decisões de micro-design durante o desenvolvimento.

---

## 📋 Índice

1. [Visão Geral](#visão-geral)
2. [Tokens de Design](#tokens-de-design)
3. [Cores](#cores)
4. [Tipografia](#tipografia)
5. [Espaçamentos](#espaçamentos)
6. [Componentes Visuais](#componentes-visuais)
7. [Animações](#animações)
8. [Responsividade](#responsividade)
9. [Acessibilidade](#acessibilidade)

---

## 🎯 Visão Geral

### Objetivo

Fornecer uma fundação visual sólida para qualquer sistema, garantindo:
- ✅ **Consistência**
- ✅ **Acessibilidade**
- ✅ **Responsividade**
- ✅ **Escalabilidade**

### Princípios de Design

1. **Clareza:** Informações importantes em destaque.
2. **Consistência:** Padrões repetíveis reduzem a carga cognitiva.
3. **Feedback:** O sistema deve sempre informar o status das ações.
4. **Hierarquia:** Tamanho e contraste guiam a atenção do usuário.

---

## 🎨 Tokens de Design

Os tokens são as "partículas atômicas" do design, armazenando valores de design system em variáveis agnósticas de contexto.

---

## 🎨 Cores

### Paleta Semântica (Status & Feedback)

Cores com significado funcional devem ser usadas de forma consistente.

```typescript
const semanticColors = {
  primary: {
    hex: '#3B82F6', // Blue-500
    tailwind: 'blue-500',
    uso: 'Ação Principal, Links, Foco',
  },
  secondary: {
    hex: '#6B7280', // Gray-500
    tailwind: 'gray-500',
    uso: 'Ações Secundárias, Texto de Apoio',
  },
  success: {
    hex: '#10B981', // Emerald-500
    tailwind: 'emerald-500',
    uso: 'Sucesso, Concluído, Seguro, Positivo',
  },
  warning: {
    hex: '#F59E0B', // Amber-500
    tailwind: 'amber-500',
    uso: 'Atenção, Pendente, Alerta',
  },
  danger: {
    hex: '#DC2626', // Red-600
    tailwind: 'red-600',
    uso: 'Erro, Perigo, Apagar, Crítico',
  },
  info: {
    hex: '#0EA5E9', // Sky-500
    tailwind: 'sky-500',
    uso: 'Informação, Ajuda, Status Neutro',
  },
};
```

### Paleta Neutra (Estrutura)

Usada para textos, fundos e bordas.

```typescript
const neutralColors = {
  white: '#FFFFFF',    // Fundo de cards, modal
  gray50: '#F9FAFB',   // Fundo de página (subtle)
  gray100: '#F3F4F6',  // Fundo secundário
  gray200: '#E5E7EB',  // Bordas, divisores
  gray300: '#D1D5DB',  // Bordas input, disabled
  gray400: '#9CA3AF',  // Ícones inativos
  gray500: '#6B7280',  // Texto secundário
  gray600: '#4B5563',  // Texto corpo suave
  gray700: '#374151',  // Texto corpo principal
  gray800: '#1F2937',  // Títulos secundários
  gray900: '#111827',  // Títulos principais
  black: '#000000',    // Overlay
};
```

---

## 📝 Tipografia

Utilizamos uma escala tipográfica modular para garantir hierarquia clara.

### Família de Fontes
- **Sans (Principal):** Inter, system-ui, sans-serif.
- **Mono (Código/Dados):** JetBrains Mono, monospace.

### Escala de Tamanhos
```typescript
const fontSize = {
  xs: '0.75rem',    // 12px - Legendas, badges
  sm: '0.875rem',   // 14px - Texto secundário, inputs
  base: '1rem',     // 16px - Texto corpo padrão
  lg: '1.125rem',   // 18px - Títulos de seção pequenos
  xl: '1.25rem',    // 20px - Títulos de cards
  '2xl': '1.5rem',  // 24px - Títulos de página
  '3xl': '1.875rem', // 30px - Destaques
};
```

### Pesos
- **Regular (400):** Corpo de texto.
- **Medium (500):** Botões, labels, destaques suaves.
- **Semibold (600):** Títulos, ênfases fortes.
- **Bold (700):** Títulos principais (usar com moderação).

---

## 📏 Espaçamentos

Baseado em uma escala de 4px (1 rem = 16px).

```typescript
const spacing = {
  1: '0.25rem',  // 4px  - Micro-espaçamentos
  2: '0.5rem',   // 8px  - Espaço interno de componentes pequenos
  3: '0.75rem',  // 12px - Espaço interno padrão
  4: '1rem',     // 16px - Margem padrão entre elementos
  6: '1.5rem',   // 24px - Separação de seções internas
  8: '2rem',     // 32px - Separação de seções maiores
  12: '3rem',    // 48px - Margens de layout
};
```

---

## 🎭 Componentes Visuais

### Bordas (Radius)
```typescript
const radius = {
  sm: '0.125rem',   // 2px
  md: '0.375rem',   // 6px - Padrão (Inputs, Buttons)
  lg: '0.5rem',     // 8px - Cards, Modais
  full: '9999px',   // Badges, Avatars, Pills
};
```

### Sombras (Elevation)
```typescript
const shadows = {
  sm: '0 1px 2px 0 rgba(0, 0, 0, 0.05)',                  // Botões
  md: '0 4px 6px -1px rgba(0, 0, 0, 0.1)',                // Dropdowns, Cards Hover
  lg: '0 10px 15px -3px rgba(0, 0, 0, 0.1)',              // Modais, Toasts
};
```

---

## 🎬 Animações

Transições suaves para micro-interações melhoram a percepção de qualidade.

```css
.transition-base {
  transition-property: all;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 200ms;
}
```

---

## 📱 Responsividade

Grid fluida e breakpoints padrão.

```typescript
const breakpoints = {
  sm: '640px',   // Mobile Landscape
  md: '768px',   // Tablet Portrait
  lg: '1024px',  // Tablet Landscape / Laptop
  xl: '1280px',  // Desktop
  '2xl': '1536px' // Large Screens
};
```

---

## ♿ Acessibilidade

**Diretrizes Obrigatórias:**
1. **Contraste:** Mínimo de 4.5:1 para texto normal e 3:1 para texto grande/ícones.
2. **Foco:** Indicadores visíveis de foco (outline/ring) para navegação por teclado.
3. **Área de Toque:** Mínimo de 44x44px para interações touch.
4. **Semântica:** Uso correto de tags HTML e atributos ARIA.

---

## ⚙️ Configuração Tailwind (Exemplo)

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: { DEFAULT: '#3B82F6', foreground: '#FFFFFF' },
        secondary: { DEFAULT: '#6B7280', foreground: '#FFFFFF' },
        success: { DEFAULT: '#10B981', foreground: '#FFFFFF' },
        warning: { DEFAULT: '#F59E0B', foreground: '#FFFFFF' },
        danger: { DEFAULT: '#DC2626', foreground: '#FFFFFF' },
      },
      borderRadius: {
        lg: `var(--radius)`,
        md: `calc(var(--radius) - 2px)`,
        sm: `calc(var(--radius) - 4px)`,
      },
    },
  },
}
```
