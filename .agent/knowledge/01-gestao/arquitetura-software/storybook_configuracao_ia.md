---json
{
  "id": "storybook_configuracao_ia",
  "title": "📚 Configuração do Storybook - Guia para IA",
  "categoria": "01-gestao",
  "subcategoria": "arquitetura-software",
  "resumo": "Guia tecnico e referencias sobre 📚 Configuração do Storybook - Guia para IA.",
  "gatilhos": [
    "arquitetura",
    "configuracao",
    "gestao",
    "guia",
    "para",
    "software",
    "storybook"
  ],
  "perguntas_tipo": [
    "Como utilizar 📚 Configuração do Storybook - Guia para IA?",
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

# 📚 Configuração do Storybook - Guia para IA

**Data:** [DATA_ATUAL]
**Versão:** 1.0
**Status:** Guia de Ferramenta (Opcional)
**Contexto:** Projetos React Genéricos

---

## 🎯 Objetivo

Configurar o Storybook para documentação visual isolada de componentes, permitindo que IAs e desenvolvedores validem estados visuais (hover, focus, disabled) sem depender da aplicação principal.

---

## 🚀 Instalação Rápida

```bash
# Inicializar Storybook em projeto existente
npx storybook@latest init
```

Isso detectará automaticamente o framework (Vite, Next.js, CRA) e instalará as dependências corretas.

---

## 📂 Estrutura de Pastas Recomendada

```
.storybook/
├── main.ts          # Configuração de addons e builders
├── preview.ts       # Configuração de decorators e globals
└── manager.ts       # Configuração de tema do Storybook

stories/             # (Opcional) Stories centralizadas
├── Button.stories.tsx
├── Input.stories.tsx
└── ...

# OU (Recomendado) Co-located junto com componentes
resources/js/components/ui/
├── Button.tsx
└── Button.stories.tsx
```

---

## 💻 Exemplo de Story Genérica

**Arquivo:** `Button.stories.tsx`

```typescript
import type { Meta, StoryObj } from '@storybook/react';
import { Button } from './Button';

const meta: Meta<typeof Button> = {
  title: 'UI/Button', // Categoria/Componente
  component: Button,
  tags: ['autodocs'], // Gera documentação automática
  argTypes: {
    variant: {
      control: 'select',
      options: ['primary', 'secondary', 'danger'],
    },
    size: {
      control: 'radio',
      options: ['sm', 'md', 'lg'],
    },
    disabled: { control: 'boolean' },
  },
};

export default meta;
type Story = StoryObj<typeof meta>;

// Story Principal
export const Primary: Story = {
  args: {
    variant: 'primary',
    children: 'Salvar Alterações',
  },
};

// Variação de Erro
export const Danger: Story = {
  args: {
    variant: 'danger',
    children: 'Excluir Item',
  },
};

// Estado Desabilitado
export const Disabled: Story = {
  args: {
    children: 'Carregando...',
    disabled: true,
  },
};
```

---

## ⚙️ Configuração para Tailwind CSS

Para que os estilos do Tailwind funcionem no Storybook, importe o CSS global no `preview.ts`.

**Arquivo:** `.storybook/preview.ts`

```typescript
import type { Preview } from '@storybook/react';
import '../resources/css/app.css'; // Ajuste o caminho conforme seu projeto

const preview: Preview = {
  parameters: {
    actions: { argTypesRegex: '^on[A-Z].*' },
    controls: {
      matchers: {
        color: /(background|color)$/i,
        date: /Date$/,
      },
    },
  },
};

export default preview;
```

---

## ✅ Checklist de Integração

- [ ] Storybook inicializa sem erros (`npm run storybook`).
- [ ] Estilos globais (Tailwind) estão carregando.
- [ ] Controles interativos (Knobs) funcionam.
- [ ] Acessibilidade (módulo a11y) está ativo.

---

## 💡 Dica para IAs

Ao gerar componentes novos, **sempre crie a story correspondente** se o Storybook estiver configurado. Isso serve como "teste visual" e documentação viva do que foi implementado.
