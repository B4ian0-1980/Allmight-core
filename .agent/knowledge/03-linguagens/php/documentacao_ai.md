---json
{
  "id": "documentacao_ai",
  "title": "Documentação AI & Generative AI — Guia Completo",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "**Fonte:** [W3Schools AI](https://www.w3schools.com/ai/default.asp) · [W3Schools Gen AI](https://www.w3schools.com/gen_ai/index.php) **Versão:** Conceitual + Prática (Python)",
  "gatilhos": [
    "completo",
    "documentacao",
    "generative",
    "guia",
    "linguagens",
    "php"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação AI & Generative AI — Guia Completo?",
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

# Documentação AI & Generative AI — Guia Completo

> **Fonte:** [W3Schools AI](https://www.w3schools.com/ai/default.asp) · [W3Schools Gen AI](https://www.w3schools.com/gen_ai/index.php)
> **Versão:** Conceitual + Prática (Python)
> **Atualizado:** 2026-02-14

---

## Sumário

1. [Conceitos Fundamentais](#conceitos-fundamentais)
2. [Machine Learning](#machine-learning)
3. [Deep Learning](#deep-learning)
4. [NLP e Visão Computacional](#nlp-e-visão-computacional)
5. [Generative AI e LLMs](#generative-ai-e-llms)
6. [Prompt Engineering](#prompt-engineering)
7. [Ferramentas](#ferramentas)

---

## Conceitos Fundamentais

### Tipos de IA

| Tipo | Descrição | Exemplo |
|---|---|---|
| **ANI** (Narrow) | Especializada em uma tarefa | ChatGPT, filtro de spam |
| **AGI** (General) | Inteligência humana geral | Teórico |
| **ASI** (Super) | Supera inteligência humana | Teórico |

### Mapa da IA

```
IA (Inteligência Artificial)
├── Machine Learning (supervisionado, não-supervisionado, reforço)
│   └── Deep Learning (redes neurais profundas)
│       ├── CNN (visão computacional)
│       ├── RNN/LSTM (sequências)
│       └── Transformers (NLP, geração)
├── NLP (processamento de linguagem natural)
├── Visão Computacional
└── Generative AI (LLMs, difusão, GANs)
```

---

## Machine Learning

### Aprendizado Supervisionado

```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
modelo = RandomForestClassifier(n_estimators=100)
modelo.fit(X_train, y_train)
print(f"Acurácia: {accuracy_score(y_test, modelo.predict(X_test)):.2%}")
```

### Algoritmos Comuns

| Algoritmo | Tipo | Uso |
|---|---|---|
| Regressão Linear/Logística | Reg./Classif. | Previsão, classif. binária |
| Decision Tree / Random Forest | Ambos | Regras de decisão, ensemble |
| SVM | Classificação | Margens de separação |
| KNN | Ambos | Vizinhos mais próximos |
| K-Means | Clustering | Agrupamento |
| XGBoost/LightGBM | Ambos | Gradient boosting (competições) |

### Métricas

| Métrica | Quando Usar |
|---|---|
| **Accuracy** | Classes balanceadas |
| **Precision** | Minimizar falsos positivos |
| **Recall** | Minimizar falsos negativos |
| **F1-Score** | Balanço precision/recall |
| **AUC-ROC** | Classificação binária |
| **MAE/RMSE** | Regressão |

---

## Deep Learning

### Rede Neural com PyTorch

```python
import torch
import torch.nn as nn

class MLP(nn.Module):
    def __init__(self, input_size, hidden, output):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_size, hidden), nn.ReLU(), nn.Dropout(0.3),
            nn.Linear(hidden, hidden), nn.ReLU(),
            nn.Linear(hidden, output)
        )
    def forward(self, x): return self.net(x)

model = MLP(784, 256, 10)
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
criterion = nn.CrossEntropyLoss()
```

### Funções de Ativação

| Função | Uso |
|---|---|
| ReLU | Default para hidden layers |
| Sigmoid | Saída binária |
| Softmax | Classificação multiclasse |
| GELU | Transformers |

### Arquiteturas

| Tipo | Uso | Modelo |
|---|---|---|
| **CNN** | Imagens | ResNet, EfficientNet, YOLO |
| **RNN/LSTM** | Sequências | Séries temporais, texto |
| **Transformer** | NLP, multimodal | BERT, GPT, T5 |
| **GAN** | Geração | StyleGAN, Pix2Pix |
| **Diffusion** | Geração de imagens | Stable Diffusion, DALL-E |

---

## NLP e Visão Computacional

### NLP com Hugging Face

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis")
resultado = classifier("Esse produto é excelente!")
# [{'label': 'POSITIVE', 'score': 0.9998}]

summarizer = pipeline("summarization")
translator = pipeline("translation_en_to_pt")
generator = pipeline("text-generation", model="gpt2")
qa = pipeline("question-answering")
```

### Visão Computacional — Tarefas

| Tarefa | Descrição | Modelo |
|---|---|---|
| Classificação | Classe da imagem | ResNet, EfficientNet |
| Detecção | Objetos + bounding boxes | YOLO, Faster R-CNN |
| Segmentação | Classificação por pixel | U-Net, Mask R-CNN |
| OCR | Texto em imagem | Tesseract, EasyOCR |

---

## Generative AI e LLMs

### Modelos Principais

| Modelo | Empresa | Destaque |
|---|---|---|
| GPT-4o / o3 | OpenAI | Raciocínio, código, multimodal |
| Claude 3.5 | Anthropic | Contexto longo, segurança |
| Gemini 2.0 | Google | Integração Google, multimodal |
| LLaMA 3 | Meta | Open-source, fine-tuning |
| Mistral | Mistral AI | Eficiente, MoE |

### API OpenAI

```python
from openai import OpenAI
client = OpenAI(api_key="sk-...")

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Você é um assistente útil."},
        {"role": "user", "content": "Explique ML em 3 frases."}
    ],
    temperature=0.7
)
print(response.choices[0].message.content)
```

### RAG (Retrieval-Augmented Generation)

```
1. Indexar documentos → Embeddings → Vector DB (Pinecone, ChromaDB)
2. Query → Embedding → Busca similaridade → Top-K documentos
3. Documentos + Query → LLM → Resposta fundamentada
```

---

## Prompt Engineering

| Técnica | Descrição |
|---|---|
| **Zero-shot** | Instrução direta sem exemplos |
| **Few-shot** | 2-5 exemplos antes da pergunta |
| **Chain-of-Thought** | "Pense passo a passo" |
| **Role prompting** | "Você é um especialista em..." |
| **ReAct** | Reasoning + Acting |

### Boas Práticas

- ✅ Seja específico e claro
- ✅ Forneça contexto relevante
- ✅ Defina formato de saída (JSON, tabela)
- ✅ Use delimitadores (```, ---)
- ❌ Prompts vagos ou ambíguos
- ❌ Confiar cegamente na saída

---

## Ferramentas

| Ferramenta | Uso |
|---|---|
| **scikit-learn** | ML clássico |
| **PyTorch** | Deep learning (pesquisa) |
| **TensorFlow/Keras** | Deep learning (produção) |
| **Hugging Face** | NLP, modelos pré-treinados |
| **LangChain** | Apps com LLMs, RAG, agents |
| **OpenCV** | Visão computacional |
| **spaCy** | NLP (produção, NER) |
| **MLflow** | MLOps, tracking |
| **Weights & Biases** | Experiment tracking |

---

*Fonte: [W3Schools AI](https://www.w3schools.com/ai/) · [W3Schools Gen AI](https://www.w3schools.com/gen_ai/)*
