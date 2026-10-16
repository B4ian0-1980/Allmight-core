---json
{
  "id": "documentacao_dsa",
  "title": "Documentação DSA — Estruturas de Dados e Algoritmos",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "**Fonte:** [W3Schools DSA](https://www.w3schools.com/dsa/index.php) · Referências clássicas (CLRS, etc.) **Versão:** Conceitual (exemplos em Python/JS)",
  "gatilhos": [
    "algoritmos",
    "dados",
    "documentacao",
    "dsa",
    "estruturas",
    "linguagens",
    "php"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação DSA — Estruturas de Dados e Algoritmos?",
    "Quais as boas praticas de php?"
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
  "dono": "stack-php",
  "prioridade": 2
}
---

# Documentação DSA — Estruturas de Dados e Algoritmos

> **Fonte:** [W3Schools DSA](https://www.w3schools.com/dsa/index.php) · Referências clássicas (CLRS, etc.)
> **Versão:** Conceitual (exemplos em Python/JS)
> **Atualizado:** 2026-02-14

---

## Sumário

1. [Complexidade (Big O)](#complexidade-big-o)
2. [Arrays e Listas Ligadas](#arrays-e-listas-ligadas)
3. [Pilhas e Filas](#pilhas-e-filas)
4. [Árvores](#árvores)
5. [Tabelas Hash](#tabelas-hash)
6. [Grafos](#grafos)
7. [Ordenação](#algoritmos-de-ordenação)
8. [Busca](#algoritmos-de-busca)
9. [Programação Dinâmica](#programação-dinâmica)
10. [Algoritmos Gulosos e Backtracking](#gulosos-e-backtracking)

---

## Complexidade (Big O)

| Notação | Nome | Exemplo |
|---|---|---|
| O(1) | Constante | Acesso por índice |
| O(log n) | Logarítmica | Busca binária |
| O(n) | Linear | Busca linear |
| O(n log n) | Log-linear | Merge Sort, Heap Sort |
| O(n²) | Quadrática | Bubble Sort, Selection Sort |
| O(2ⁿ) | Exponencial | Subsets, Fibonacci (recursivo) |
| O(n!) | Fatorial | Permutações |

### Regras Práticas

- **Drop constantes:** O(2n) → O(n)
- **Drop termos menores:** O(n² + n) → O(n²)
- **Loops aninhados:** O(n) × O(n) = O(n²)
- **Loops sequenciais:** O(n) + O(n) = O(n)

---

## Arrays e Listas Ligadas

### Array Dinâmico

```python
# Complexidade
# Acesso: O(1)  |  Inserção final: O(1) amortizado
# Inserção meio: O(n)  |  Busca: O(n)  |  Remoção: O(n)

arr = [10, 20, 30, 40, 50]
arr.append(60)       # O(1)
arr.insert(2, 25)    # O(n) — desloca elementos
arr.pop()            # O(1) — remove último
arr.pop(0)           # O(n) — desloca tudo
```

### Lista Ligada (Linked List)

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):       # O(1)
        node = Node(data)
        node.next = self.head
        self.head = node

    def append(self, data):        # O(n)
        node = Node(data)
        if not self.head:
            self.head = node; return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node

    def delete(self, data):        # O(n)
        if self.head and self.head.data == data:
            self.head = self.head.next; return
        curr = self.head
        while curr.next:
            if curr.next.data == data:
                curr.next = curr.next.next; return
            curr = curr.next

    def search(self, data):        # O(n)
        curr = self.head
        while curr:
            if curr.data == data: return True
            curr = curr.next
        return False
```

---

## Pilhas e Filas

### Stack (LIFO)

```python
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):  self.items.append(item)     # O(1)
    def pop(self):          return self.items.pop()      # O(1)
    def peek(self):         return self.items[-1]        # O(1)
    def is_empty(self):     return len(self.items) == 0
    def size(self):         return len(self.items)

# Uso: undo/redo, parsing expressões, DFS
```

### Queue (FIFO)

```python
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    def enqueue(self, item): self.items.append(item)    # O(1)
    def dequeue(self):       return self.items.popleft() # O(1)
    def peek(self):          return self.items[0]
    def is_empty(self):      return len(self.items) == 0

# Priority Queue
import heapq
pq = []
heapq.heappush(pq, (1, "urgente"))   # (prioridade, dado)
heapq.heappush(pq, (3, "normal"))
item = heapq.heappop(pq)              # (1, "urgente")
```

---

## Árvores

### Árvore Binária de Busca (BST)

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):              # O(log n) médio
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if not node: return TreeNode(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        return node

    def search(self, val):              # O(log n) médio
        return self._search(self.root, val)

    def _search(self, node, val):
        if not node: return False
        if val == node.val: return True
        if val < node.val: return self._search(node.left, val)
        return self._search(node.right, val)

# Traversals
def inorder(node):     # Esquerda → Raiz → Direita (ordenado!)
    if node:
        inorder(node.left)
        print(node.val)
        inorder(node.right)

def preorder(node):    # Raiz → Esquerda → Direita
    if node:
        print(node.val)
        preorder(node.left)
        preorder(node.right)

def postorder(node):   # Esquerda → Direita → Raiz
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.val)

def bfs(root):         # Largura (level-order)
    if not root: return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
```

### Heap (Min-Heap)

```python
# Array: parent = i//2, left = 2*i, right = 2*i+1
# Min-Heap: pai ≤ filhos | Max-Heap: pai ≥ filhos
# Inserção: O(log n) | Remoção raiz: O(log n) | Consulta mín/máx: O(1)

import heapq
nums = [5, 3, 8, 1, 9]
heapq.heapify(nums)          # Transforma em min-heap O(n)
heapq.heappush(nums, 2)      # Inserir
menor = heapq.heappop(nums)  # Remove menor
top3 = heapq.nsmallest(3, nums)
bottom3 = heapq.nlargest(3, nums)
```

---

## Tabelas Hash

```python
# dict do Python = hash table
# Inserção: O(1) médio | Busca: O(1) médio | Remoção: O(1) médio
# Pior caso (colisões): O(n)

# Implementação simplificada
class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value); return
        self.table[idx].append((key, value))

    def get(self, key):
        idx = self._hash(key)
        for k, v in self.table[idx]:
            if k == key: return v
        raise KeyError(key)

# Uso: caches, contagem, deduplicação, lookup O(1)
```

---

## Grafos

```python
from collections import defaultdict, deque

class Graph:
    def __init__(self, directed=False):
        self.adj = defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v, weight=1):
        self.adj[u].append((v, weight))
        if not self.directed:
            self.adj[v].append((u, weight))

    # BFS — Busca em Largura O(V+E)
    def bfs(self, start):
        visited = {start}
        queue = deque([start])
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor, _ in self.adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order

    # DFS — Busca em Profundidade O(V+E)
    def dfs(self, start, visited=None):
        if visited is None: visited = set()
        visited.add(start)
        result = [start]
        for neighbor, _ in self.adj[start]:
            if neighbor not in visited:
                result.extend(self.dfs(neighbor, visited))
        return result

    # Dijkstra — Caminho mais curto O((V+E) log V)
    def dijkstra(self, start):
        import heapq
        dist = {start: 0}
        pq = [(0, start)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist.get(u, float('inf')): continue
            for v, w in self.adj[u]:
                nd = d + w
                if nd < dist.get(v, float('inf')):
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        return dist
```

---

## Algoritmos de Ordenação

| Algoritmo | Melhor | Médio | Pior | Espaço | Estável |
|---|---|---|---|---|---|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | ❌ |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | ❌ |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(k) | ✅ |

```python
# Merge Sort O(n log n)
def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    return result + left[i:] + right[j:]

# Quick Sort O(n log n) médio
def quick_sort(arr):
    if len(arr) <= 1: return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)
```

---

## Algoritmos de Busca

```python
# Busca Linear O(n)
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target: return i
    return -1

# Busca Binária O(log n) — array ORDENADO
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: lo = mid + 1
        else: hi = mid - 1
    return -1
```

---

## Programação Dinâmica

```python
# Fibonacci — O(n) com memoization
def fib(n, memo={}):
    if n <= 1: return n
    if n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

# Knapsack 0/1 — O(n*W)
def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0] * (W+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for w in range(W+1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][W]

# LCS (Longest Common Subsequence) — O(m*n)
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

# Padrão DP:
# 1. Definir subproblemas
# 2. Encontrar relação de recorrência
# 3. Base case
# 4. Bottom-up (tabela) ou top-down (memoization)
```

---

## Gulosos e Backtracking

### Algoritmo Guloso

```python
# Problema do troco — escolha local ótima
def troco_guloso(valor, moedas=[100, 50, 25, 10, 5, 1]):
    resultado = {}
    for moeda in sorted(moedas, reverse=True):
        if valor >= moeda:
            resultado[moeda] = valor // moeda
            valor %= moeda
    return resultado

# Interval Scheduling — máximo de intervalos sem sobreposição
def max_intervalos(intervalos):
    intervalos.sort(key=lambda x: x[1])  # Ordena por fim
    count = 0
    last_end = float('-inf')
    for start, end in intervalos:
        if start >= last_end:
            count += 1
            last_end = end
    return count
```

### Backtracking

```python
# N-Queens
def solve_queens(n):
    solutions = []
    def backtrack(row, cols, diag1, diag2, board):
        if row == n:
            solutions.append([r[:] for r in board]); return
        for col in range(n):
            if col in cols or (row-col) in diag1 or (row+col) in diag2:
                continue
            board[row][col] = 'Q'
            backtrack(row+1, cols|{col}, diag1|{row-col}, diag2|{row+col}, board)
            board[row][col] = '.'
    board = [['.']*n for _ in range(n)]
    backtrack(0, set(), set(), set(), board)
    return solutions
```

---

*Fonte: [W3Schools DSA](https://www.w3schools.com/dsa/) · Cormen et al. "Introduction to Algorithms" (CLRS)*
