---json
{
  "id": "documentacao_mui",
  "title": "Documentação: Material UI (MUI)",
  "categoria": "04-frameworks",
  "subcategoria": "react",
  "resumo": "**Tipo:** Biblioteca de Componentes React (Material Design) **Site Oficial:** [mui.com](https://mui.com)",
  "gatilhos": [
    "documentacao",
    "frameworks",
    "material",
    "mui",
    "react"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação: Material UI (MUI)?",
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

# Documentação: Material UI (MUI)

> **Tipo:** Biblioteca de Componentes React (Material Design)
> **Site Oficial:** [mui.com](https://mui.com)
> **Versão Atual:** v5/v6

## O que é?
MUI (anteriormente Material-UI) é uma biblioteca robusta, personalizável e acessível de componentes React fundamentais, permitindo construir seu próprio Design System e desenvolver aplicações React mais rapidamente. Implementa os princípios do Material Design do Google.

## Instalação

```bash
# Com npm
npm install @mui/material @emotion/react @emotion/styled

# Ícones e fontes (Opcional mas recomendado)
npm install @mui/icons-material
```

Adicione ao `index.html` a fonte Roboto:
```html
<link
  rel="stylesheet"
  href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
/>
```

## Uso Básico

```jsx
import * as React from 'react';
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';

export default function BasicButtons() {
  return (
    <Stack spacing={2} direction="row">
      <Button variant="text">Text</Button>
      <Button variant="contained">Contained</Button>
      <Button variant="outlined">Outlined</Button>
    </Stack>
  );
}
```

## Componentes Principais
*   **Layout:** Box, Container, Grid, Stack.
*   **Inputs:** Button, Checkbox, TextField, Select, Slider, Switch.
*   **Data Display:** Avatar, Badge, Chip, Divider, List, Table, Typography, Icons.
*   **Feedback:** Alert, Backdrop, Dialog, Snackbar, Skeleton.
*   **Navigation:** Drawer, Menu, Stepper, Tabs.

## Customização (Theming)
MUI permite customizar todo o tema da aplicação.

```jsx
import { createTheme, ThemeProvider } from '@mui/material/styles';

const theme = createTheme({
  palette: {
    primary: {
      main: '#ff4400',
    },
    secondary: {
      main: '#0044ff',
    },
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <MeuComponente />
    </ThemeProvider>
  );
}
```

## sx prop
Para estilização rápida inline (similar a utility classes), use a prop `sx`:

```jsx
<Box sx={{ p: 2, border: '1px dashed grey', '&:hover': { opacity: 0.8 } }}>
  Container customizado
</Box>
```

## Referências
*   [Começando (Getting Started)](https://mui.com/material-ui/getting-started/)
*   [Componentes](https://mui.com/material-ui/all-components/)
*   [Templates Gratuitos](https://mui.com/material-ui/getting-started/templates/)
