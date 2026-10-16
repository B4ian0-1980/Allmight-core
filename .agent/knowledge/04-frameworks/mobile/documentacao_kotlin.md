---json
{
  "id": "documentacao_kotlin",
  "title": "Documentação Kotlin — Guia Completo",
  "categoria": "04-frameworks",
  "subcategoria": "mobile",
  "resumo": "**Fonte:** [W3Schools Kotlin](https://www.w3schools.com/kotlin/index.php) · [Kotlin Docs](https://kotlinlang.org/docs/) **Versão:** Kotlin 2.0+",
  "gatilhos": [
    "completo",
    "documentacao",
    "frameworks",
    "guia",
    "kotlin",
    "mobile"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação Kotlin — Guia Completo?",
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

# Documentação Kotlin — Guia Completo

> **Fonte:** [W3Schools Kotlin](https://www.w3schools.com/kotlin/index.php) · [Kotlin Docs](https://kotlinlang.org/docs/)
> **Versão:** Kotlin 2.0+
> **Atualizado:** 2026-02-14

---

## Sumário

1. [Fundamentos](#fundamentos)
2. [Tipos e Null Safety](#tipos-e-null-safety)
3. [Controle de Fluxo](#controle-de-fluxo)
4. [Funções](#funções)
5. [OOP — Classes](#oop--classes)
6. [Coleções](#coleções)
7. [Coroutines](#coroutines)
8. [Kotlin para Android](#kotlin-para-android)

---

## Fundamentos

```kotlin
fun main() {
    println("Hello, World!")
}
```

### Variáveis

```kotlin
val nome = "Maria"       // Imutável (preferir)
var idade = 30           // Mutável
val PI: Double = 3.14159 // Tipo explícito

// String templates
println("Nome: $nome, Idade: $idade")
println("Maiúsculo: ${nome.uppercase()}")

// Multiline
val texto = """
    |Primeira linha
    |Segunda linha
""".trimMargin()
```

---

## Tipos e Null Safety

```kotlin
// Tipos básicos: Int, Long, Double, Float, Boolean, Char, String, Byte, Short

// Null safety (nullable com ?)
var email: String? = null

// Safe call
val len = email?.length           // null se email é null

// Elvis operator
val len = email?.length ?: 0      // 0 se null

// Not-null assertion (cuidado!)
val len = email!!.length          // Lança NPE se null

// Smart cast
if (email != null) {
    println(email.length)  // Já é String (não String?)
}

// let (executar se não-null)
email?.let { e ->
    println("Email: $e")
}

// Casting seguro
val numero = valor as? Int  // null se falhar
```

---

## Controle de Fluxo

```kotlin
// if (é expressão)
val max = if (a > b) a else b

// when (switch turbinado)
val resultado = when (nota) {
    in 9..10 -> "A"
    in 7..8 -> "B"
    in 5..6 -> "C"
    else -> "D"
}

when {
    idade < 12 -> "Criança"
    idade < 18 -> "Adolescente"
    else -> "Adulto"
}

// for
for (i in 1..10) { }           // 1 a 10
for (i in 0 until 10) { }     // 0 a 9
for (i in 10 downTo 0 step 2) { }
for ((index, value) in lista.withIndex()) { }

// while
while (condicao) { }
do { } while (condicao)
```

---

## Funções

```kotlin
// Básica
fun somar(a: Int, b: Int): Int {
    return a + b
}

// Single-expression
fun somar(a: Int, b: Int) = a + b

// Default params
fun saudar(nome: String, saudacao: String = "Olá") = "$saudacao, $nome!"

// Named arguments
saudar(nome = "Ana", saudacao = "Oi")

// Varargs
fun soma(vararg nums: Int) = nums.sum()

// Extension functions
fun String.isEmail(): Boolean = this.contains("@") && this.contains(".")
"teste@mail.com".isEmail()  // true

// Higher-order functions
fun operar(a: Int, b: Int, operacao: (Int, Int) -> Int): Int {
    return operacao(a, b)
}
operar(5, 3) { x, y -> x + y }

// Lambda
val quadrado: (Int) -> Int = { it * it }
val filtrado = lista.filter { it > 5 }

// Scope functions
pessoa.apply {
    nome = "Ana"
    idade = 25
}
pessoa.let { println(it.nome) }
pessoa.also { log(it) }
val resultado = with(pessoa) { "$nome, $idade anos" }
val endereco = pessoa.run { buscarEndereco(id) }
```

---

## OOP — Classes

```kotlin
// Classe
class Pessoa(
    val nome: String,              // Propriedade no construtor
    var idade: Int,
    val email: String = ""
) {
    // Bloco init
    init { require(idade >= 0) { "Idade inválida" } }

    // Propriedade secundária
    val adulto: Boolean get() = idade >= 18

    // Construtor secundário
    constructor(nome: String) : this(nome, 0)

    override fun toString() = "$nome, $idade anos"
}

// Data class (equals, hashCode, toString, copy automáticos)
data class Produto(val nome: String, val preco: Double)
val p1 = Produto("Item", 10.0)
val p2 = p1.copy(preco = 15.0)
val (nome, preco) = p1  // Destructuring

// Sealed class/interface (hierarquia fechada)
sealed class Resultado {
    data class Sucesso(val dados: String) : Resultado()
    data class Erro(val mensagem: String) : Resultado()
    data object Carregando : Resultado()
}

fun processar(r: Resultado) = when (r) {
    is Resultado.Sucesso -> "OK: ${r.dados}"
    is Resultado.Erro -> "Falha: ${r.mensagem}"
    Resultado.Carregando -> "Aguarde..."
}

// Object (singleton)
object Database {
    fun connect() { /* ... */ }
}

// Companion object (static equivalente)
class Util {
    companion object {
        fun create(): Util = Util()
    }
}
val u = Util.create()

// Enum
enum class Cor(val hex: String) {
    VERMELHO("#FF0000"),
    VERDE("#00FF00"),
    AZUL("#0000FF");

    fun rgb() = hex.removePrefix("#")
}

// Interface
interface Clicavel {
    fun onClick()
    fun onLongClick() { /* default */ }
}
```

---

## Coleções

```kotlin
// Imutáveis (preferir)
val lista = listOf(1, 2, 3)
val set = setOf("a", "b", "c")
val mapa = mapOf("a" to 1, "b" to 2)

// Mutáveis
val mutavel = mutableListOf(1, 2, 3)
mutavel.add(4)
mutavel.removeAt(0)

// Transformações
val nums = listOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
nums.filter { it % 2 == 0 }           // [2, 4, 6, 8, 10]
nums.map { it * 2 }                    // [2, 4, 6, ...]
nums.flatMap { listOf(it, it * 10) }
nums.groupBy { if (it % 2 == 0) "par" else "ímpar" }
nums.sortedDescending()
nums.take(3)                           // [1, 2, 3]
nums.drop(7)                           // [8, 9, 10]
nums.chunked(3)                        // [[1,2,3],[4,5,6],[7,8,9],[10]]
nums.any { it > 5 }                    // true
nums.all { it > 0 }                    // true
nums.none { it < 0 }                   // true
nums.count { it > 5 }                  // 5
nums.sumOf { it }                      // 55
nums.fold(0) { acc, n -> acc + n }
nums.associateBy { it.toString() }     // Map<String, Int>

// Sequences (lazy — para grandes coleções)
nums.asSequence()
    .filter { it > 3 }
    .map { it * 2 }
    .take(3)
    .toList()
```

---

## Coroutines

```kotlin
import kotlinx.coroutines.*

// Básico
fun main() = runBlocking {
    launch {
        delay(1000)
        println("Mundo!")
    }
    println("Olá,")
}

// async/await
suspend fun fetchData(url: String): String { /* ... */ }

val resultado = coroutineScope {
    val d1 = async { fetchData("url1") }
    val d2 = async { fetchData("url2") }
    "${d1.await()} + ${d2.await()}"
}

// Flow (stream reativo)
fun numeros(): Flow<Int> = flow {
    for (i in 1..5) {
        delay(100)
        emit(i)
    }
}
numeros()
    .filter { it % 2 == 0 }
    .map { it * 10 }
    .collect { println(it) }
```

---

## Kotlin para Android

```kotlin
// Activity básica (Jetpack Compose)
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MeuApp()
        }
    }
}

@Composable
fun MeuApp() {
    var count by remember { mutableIntStateOf(0) }
    Column(modifier = Modifier.padding(16.dp)) {
        Text("Contagem: $count", style = MaterialTheme.typography.headlineMedium)
        Button(onClick = { count++ }) {
            Text("Incrementar")
        }
    }
}

// ViewModel
class MainViewModel : ViewModel() {
    private val _dados = MutableStateFlow<List<String>>(emptyList())
    val dados: StateFlow<List<String>> = _dados.asStateFlow()

    fun carregar() {
        viewModelScope.launch {
            _dados.value = repository.fetchDados()
        }
    }
}
```

---

*Fonte: [W3Schools Kotlin](https://www.w3schools.com/kotlin/) · [Kotlin Docs](https://kotlinlang.org/docs/)*
