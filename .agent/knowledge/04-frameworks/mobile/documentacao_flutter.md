---json
{
  "id": "documentacao_flutter",
  "title": "Documentação Flutter — Guia Completo",
  "categoria": "04-frameworks",
  "subcategoria": "mobile",
  "resumo": "**Fonte:** [flutter.dev](https://docs.flutter.dev/) **Versão:** 3.19+ (Dart 3)",
  "gatilhos": [
    "completo",
    "documentacao",
    "flutter",
    "frameworks",
    "guia",
    "mobile"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação Flutter — Guia Completo?",
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

# Documentação Flutter — Guia Completo

> **Fonte:** [flutter.dev](https://docs.flutter.dev/)
> **Versão:** 3.19+ (Dart 3)
> **Atualizado:** 2026-02-14

---

## Sumário

1. [O que é Flutter?](#o-que-é-flutter)
2. [Linguagem Dart](#linguagem-dart)
3. [Widget Tree](#widget-tree)
4. [Stateless vs Stateful](#stateless-vs-stateful)
5. [Layouts Comuns](#layouts-comuns)
6. [Navegação](#navegação)
7. [Gerenciamento de Estado](#gerenciamento-de-estado)

---

## O que é Flutter?

Criado pelo Google, Flutter é um toolkit de UI para criar aplicações nativas compiladas para Mobile, Web e Desktop a partir de um único código base.

Diferente do React Native (que usa pontes para componentes nativos), o Flutter desenha cada pixel na tela usando a engine gráfica **Skia** (ou **Impeller** no iOS), garantindo 60/120 FPS consistentes e visual idêntico em todas as plataformas.

---

## Linguagem Dart

Flutter usa Dart, uma linguagem orientada a objetos, fortemente tipada e fácil de aprender (mistura de Java e JS).

```dart
void main() {
  print('Hello World');
  
  // Variáveis
  String nome = 'Fulano';
  int idade = 30;
  final data = DateTime.now(); // Runtime constant
  const pi = 3.14;             // Compile-time constant
  
  // Null Safety (Padrão)
  String? podeSerNulo;
  String naoNulo = 'Valor';
  
  // Funções (Arrow syntax)
  int somar(int a, int b) => a + b;
}

// Classes
class Pessoa {
  final String nome;
  
  // Construtor com parâmetros nomeados obrigatórios
  Pessoa({required this.nome});
}
```

---

## Widget Tree

Em Flutter, **TUDO é um Widget**. O layout, o botão, o padding, a animação, o alinhamento.

```dart
import 'package:flutter/material.dart';

void main() => runApp(MeuApp());

class MeuApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp( // Widget raiz (configurações gerais)
      home: Scaffold(   // Estrutura padrão (AppBar, Body, FAB)
        appBar: AppBar(title: Text('Meu App')),
        body: Center(
          child: Text('Olá Flutter!'),
        ),
        floatingActionButton: FloatingActionButton(
          onPressed: () {},
          child: Icon(Icons.add),
        ),
      ),
    );
  }
}
```

---

## Stateless vs Stateful

### Stateless Widget
Imutável. Depende apenas de configurações passadas no construtor. Se precisar mudar, o pai deve reconstruí-lo.
*(Ex: Ícone, Texto Estático)*

### Stateful Widget
Mantém estado interno que pode mudar durante a vida do widget. Usa `setState()` para reconstruir a UI.
*(Ex: Checkbox, Contador, Formulário)*

```dart
class Contador extends StatefulWidget {
  @override
  _ContadorState createState() => _ContadorState();
}

class _ContadorState extends State<Contador> {
  int _count = 0;

  void _increment() {
    setState(() {
      _count++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: _increment,
      child: Text('Contagem: $_count'),
    );
  }
}
```

---

## Layouts Comuns

O segredo do layout em Flutter é a composição (Rows e Columns dentro de Containers).

- **Column:** Alinha verticalmente.
- **Row:** Alinha horizontalmente.
- **Stack:** Empilha widgets um em cima do outro (eixo Z).
- **ListView:** Lista com scroll.
- **Container:** O <div> do Flutter. Padding, margem, cor, borda.
- **Expanded:** Faz o filho ocupar o espaço restante (Flex).

```dart
Row(
  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
  children: [
    Icon(Icons.star, color: Colors.blue),
    Icon(Icons.star, color: Colors.blue),
    Icon(Icons.star, color: Colors.blue),
  ],
)
```

---

## Navegação

### Navegação Simples (Push/Pop)
```dart
// Ir para nova tela
Navigator.push(
  context,
  MaterialPageRoute(builder: (context) => SegundaTela()),
);

// Voltar
Navigator.pop(context);
```

### Navegação Nomeada
Definida no `MaterialApp`.

```dart
MaterialApp(
  initialRoute: '/',
  routes: {
    '/': (context) => Home(),
    '/detalhes': (context) => Detalhes(),
  },
);

// Usando
Navigator.pushNamed(context, '/detalhes');
```

---

## Gerenciamento de Estado

Para apps complexos, `setState` não escala bem (prop drilling).

### Provider (Recomendado iniciantes)
Usa Injeção de Dependência na árvore de widgets.

```dart
// 1. Criar Model (ChangeNotifier)
class CounterModel extends ChangeNotifier {
  int count = 0;
  void increment() {
    count++;
    notifyListeners(); // Avisa quem ouve
  }
}

// 2. Prover na raiz
ChangeNotifierProvider(
  create: (context) => CounterModel(),
  child: MyApp(),
);

// 3. Consumir
Consumer<CounterModel>(
  builder: (context, model, child) => Text('${model.count}'),
);
```

Outras opções populares:
- **Riverpod:** Evolução do Provider (Stateless, Compile-safe).
- **Bloc / Cubit:** Separação estrita de lógica e UI (Eventos e Estados).

---

*Fonte: [flutter.dev/docs](https://docs.flutter.dev/)*
