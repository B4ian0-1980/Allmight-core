---json
{
  "id": "documentacao-react-native",
  "title": "Documentação React Native — Guia Completo",
  "categoria": "04-frameworks",
  "subcategoria": "react",
  "resumo": "**Fonte:** [reactnative.dev](https://reactnative.dev/docs/getting-started) **Versão:** 0.73+ (Expo 50)",
  "gatilhos": [
    "completo",
    "documentacao",
    "frameworks",
    "guia",
    "native",
    "react"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação React Native — Guia Completo?",
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

# Documentação React Native — Guia Completo

> **Fonte:** [reactnative.dev](https://reactnative.dev/docs/getting-started)
> **Versão:** 0.73+ (Expo 50)
> **Atualizado:** 2026-02-14

---

## Sumário

1. [O que é React Native?](#o-que-é-react-native)
2. [Expo vs CLI Nativo](#expo-vs-cli-nativo)
3. [Componentes Core](#componentes-core)
4. [Estilização e Flexbox](#estilização-e-flexbox)
5. [Navegação](#navegação)
6. [Listas (FlatList)](#listas-flatlist)
7. [Acesso a Hardware](#acesso-a-hardware)

---

## O que é React Native?

Permite criar aplicativos nativos reais para Android e iOS usando React. Diferente de frameworks híbridos (Ionic/Cordova) que usam WebView, o React Native renderiza **Views Nativas** da plataforma.

A lógica é JavaScript/TypeScript, mas a UI é 100% nativa.

---

## Expo vs CLI Nativo

Para 99% dos projetos novos (e recomendações oficiais), use **Expo**.

- **Expo:** Setup zero, roda no celular via QR Code, bibliotecas pré-configuradas (Câmera, GPS, Notificações).
- **React Native CLI:** Controle total de código nativo (Java/Obj-C). Necessário apenas se você precisar linkar bibliotecas nativas muito específicas e não suportadas pelo Expo.

### Criando Projeto Expo

```bash
npx create-expo-app meu-app
cd meu-app
npx expo start
```

---

## Componentes Core

No React Native, **não existem tags HTML** (`<div>`, `<p>`, `<span>`). Usamos componentes nativos:

| HTML | React Native | Descrição |
|---|---|---|
| `<div>` | `<View>` | Container flexbox padrão |
| `<p>`, `<h1>` | `<Text>` | Único lugar onde texto pode existir |
| `<img`> | `<Image>` | Imagens locais ou rede |
| `<button>` | `<Button>`, `<Pressable>` | Botões |
| `<input>` | `<TextInput>` | Entrada de dados |
| `<ul>` | `<FlatList>` | Listas performáticas |
| `overflow: scroll` | `<ScrollView>` | Conteúdo rolável |

```jsx
import { View, Text, Image, Button, StyleSheet } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Olá Mobile!</Text>
      <Image 
        source={{ uri: 'https://logo.com/img.png' }} 
        style={styles.logo} 
      />
      <Button title="Clique aqui" onPress={() => alert('Oi!')} />
    </View>
  );
}
```

---

## Estilização e Flexbox

React Native usa um subset do CSS no JavaScript (`StyleSheet`). **Flexbox é o padrão** e a direção padrão é `column` (diferente da web que é `row`).

```javascript
const styles = StyleSheet.create({
  container: {
    flex: 1, // Ocupa toda a tela
    backgroundColor: '#fff',
    alignItems: 'center', // Centraliza horizontalmente (coluna)
    justifyContent: 'center', // Centraliza verticalmente
    padding: 20
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 10
  }
});
```

---

## Navegação

Usa-se **React Navigation** (padrão da comunidade) ou **Expo Router** (baseado em arquivos, similar ao Next.js).

### Exemplo (Expo Router / File-based)
Estrutura de pastas em `app/`:

- `app/index.js` → Home Screen
- `app/details.js` → Details Screen
- `app/_layout.js` → Configuração global (Stack/Tabs)

**Links:**
```jsx
import { Link } from 'expo-router';

<Link href="/details">Ir para Detalhes</Link>
```

### Exemplo (React Navigation - Stack)
```jsx
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

const Stack = createNativeStackNavigator();

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="Details" component={DetailsScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
```

---

## Listas (FlatList)

**NUNCA** use `map` dentro de uma `<ScrollView>` para listas longas. Use `<FlatList>` para renderizar apenas os itens visíveis na tela (virtualização).

```jsx
import { FlatList, Text, View } from 'react-native';

const DATA = Array.from({ length: 100 }).map((_, i) => ({ id: i, title: `Item ${i}` }));

export default function Lista() {
  return (
    <FlatList
      data={DATA}
      keyExtractor={item => item.id.toString()}
      renderItem={({ item }) => (
        <View style={{ padding: 20, borderBottomWidth: 1 }}>
          <Text>{item.title}</Text>
        </View>
      )}
    />
  );
}
```

---

## Acesso a Hardware (Expo SDK)

O Expo fornece hooks fáceis para hardware.

```bash
npx expo install expo-camera expo-location
```

```jsx
// Geolocalização
import * as Location from 'expo-location';

const [location, setLocation] = useState(null);

useEffect(() => {
  (async () => {
    let { status } = await Location.requestForegroundPermissionsAsync();
    if (status !== 'granted') return;

    let loc = await Location.getCurrentPositionAsync({});
    setLocation(loc);
  })();
}, []);
```

---

*Fonte: [reactnative.dev](https://reactnative.dev) · [docs.expo.dev](https://docs.expo.dev/)*
