---json
{
  "id": "documentacao_ionic",
  "title": "Documentação Ionic — Guia Completo",
  "categoria": "04-frameworks",
  "subcategoria": "mobile",
  "resumo": "**Fonte:** [ionicframework.com](https://ionicframework.com/docs) **Versão:** 7.x",
  "gatilhos": [
    "completo",
    "documentacao",
    "frameworks",
    "guia",
    "ionic",
    "mobile"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação Ionic — Guia Completo?",
    "Quais as boas praticas de mobile?"
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
  "dono": "stack-mobile",
  "prioridade": 2
}
---

# Documentação Ionic — Guia Completo

> **Fonte:** [ionicframework.com](https://ionicframework.com/docs)
> **Versão:** 7.x
> **Atualizado:** 2026-02-14

---

## Sumário

1. [O que é Ionic?](#o-que-é-ionic)
2. [Ionic vs React Native/Flutter](#ionic-vs-react-nativeflutter)
3. [Instalação](#instalação)
4. [Componentes de UI](#componentes-de-ui)
5. [Capacitor (Acesso Nativo)](#capacitor-acesso-nativo)
6. [Theming e CSS](#theming-e-css)

---

## O que é Ionic?

Ionic é um toolkit open-source para criar **mobile apps híbridos** de alta qualidade usando tecnologias web padrão (HTML, CSS e JavaScript).

A aplicação roda dentro de uma WebView nativa e tem acesso a recursos do dispositivo (Câmera, GPS) através de uma ponte (Capacitor ou Cordova). O Ionic fornece uma biblioteca gigante de **componentes visuais adaptativos** que parecem nativos tanto no iOS quanto no Android.

Pode ser usado com **Angular**, **React**, **Vue** ou Vanilla JS.

---

## Ionic vs React Native/Flutter

- **Ionic:** Você escreve HTML/CSS reais. Se você é dev web, já sabe 100%. A UI é simulada via Web Components (mas muito bem feita). Performance é "boa o suficiente" para 90% dos apps (LOB, CRUD).
- **React Native/Flutter:** Usam componentes nativos ou engine própria. Melhor performance para jogos ou animações pesadas. Curva de aprendizado maior.

---

## Instalação

```bash
# Instalar CLI
npm install -g @ionic/cli

# Criar app (escolha o framework: React, Angular, Vue)
ionic start meu-app tabs --type=react

# Rodar no navegador
cd meu-app
ionic serve
```

---

## Componentes de UI

O poder do Ionic está nos componentes pré-prontos.

### Estrutura da Página (`IonPage`)
Necessário para o roteamento e transições funcionarem corretamente.

```jsx
// Exemplo React
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent } from '@ionic/react';

const Home = () => (
  <IonPage>
    <IonHeader>
      <IonToolbar>
        <IonTitle>Home</IonTitle>
      </IonToolbar>
    </IonHeader>
    
    <IonContent class="ion-padding">
      <h1>Bem-vindo!</h1>
    </IonContent>
  </IonPage>
);
```

### Componentes Comuns
Todos começam com `ion-`.

- **Botões:** `<IonButton expand="block">Clique</IonButton>`
- **Listas:** `<IonList>`, `<IonItem>`, `<IonLabel>`
- **Cards:** `<IonCard>`
- **Modal:** `<IonModal>`
- **Abas:** `<IonTabs>`

Os componentes mudam o visual automaticamente dependendo da plataforma (Material Design no Android, Cupertino no iOS).

---

## Capacitor (Acesso Nativo)

Capacitor é o sucessor moderno do Cordova. É a camada que conecta seu JS ao código nativo.

```bash
npm install @capacitor/camera @capacitor/preferences
```

### Usando a Câmera
```javascript
import { Camera, CameraResultType } from '@capacitor/camera';

const tirarFoto = async () => {
  const image = await Camera.getPhoto({
    quality: 90,
    allowEditing: true,
    resultType: CameraResultType.Uri
  });

  console.log('Foto salva em:', image.webPath);
};
```

### Gerando Build Nativo
O Capacitor "sincroniza" seu build web para dentro das pastas `android` e `ios` nativas.

```bash
# Compilar projeto web
npm run build

# Copiar assets para pastas nativas
npx cap sync

# Abrir Android Studio ou Xcode
npx cap open android
```

---

## Theming e CSS

Ionic usa CSS Variables extensivamente. É muito fácil customizar temas.

`src/theme/variables.css`:
```css
:root {
  --ion-color-primary: #3880ff;
  --ion-color-secondary: #3dc2ff;
  --ion-color-danger: #eb445a;
}
```

Utilitários CSS também estão disponíveis (padding, margin, flexbox), similar ao Bootstrap ou Tailwind.

```html
<IonContent class="ion-padding ion-text-center">
  <p>Texto centralizado com padding</p>
</IonContent>
```

---

*Fonte: [ionicframework.com/docs](https://ionicframework.com/docs)*
