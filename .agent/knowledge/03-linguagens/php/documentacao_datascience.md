---json
{
  "id": "documentacao_datascience",
  "title": "Documentação Data Science — Guia Completo",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "**Fonte:** [W3Schools Data Science](https://www.w3schools.com/datascience/default.asp) · Referências diversas **Versão:** Conceitual + Prática (Python)",
  "gatilhos": [
    "completo",
    "data",
    "datascience",
    "documentacao",
    "guia",
    "linguagens",
    "php",
    "science"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação Data Science — Guia Completo?",
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

# Documentação Data Science — Guia Completo

> **Fonte:** [W3Schools Data Science](https://www.w3schools.com/datascience/default.asp) · Referências diversas
> **Versão:** Conceitual + Prática (Python)
> **Atualizado:** 2026-02-14

---

## Sumário

1. [Fundamentos](#fundamentos)
2. [NumPy](#numpy)
3. [Pandas](#pandas)
4. [Visualização (Matplotlib/Seaborn)](#visualização)
5. [Estatística](#estatística)
6. [Pré-processamento](#pré-processamento)
7. [Machine Learning Aplicado](#machine-learning-aplicado)
8. [Pipeline Completo](#pipeline-completo)

---

## Fundamentos

### Ciclo de Data Science

```
1. Definir problema / questão de negócio
2. Coletar dados (APIs, DBs, web scraping, CSVs)
3. Limpar e preparar (missing values, outliers, tipos)
4. Explorar (EDA — análise exploratória)
5. Modelar (ML, estatística)
6. Avaliar (métricas, validação cruzada)
7. Comunicar (visualizações, relatórios, dashboards)
8. Deploy (API, dashboard, automação)
```

### Ambiente

```bash
pip install numpy pandas matplotlib seaborn scikit-learn jupyter
jupyter notebook
```

---

## NumPy

```python
import numpy as np

# Criar arrays
a = np.array([1, 2, 3, 4, 5])
zeros = np.zeros((3, 4))
ones = np.ones((2, 3))
seq = np.arange(0, 10, 0.5)
linear = np.linspace(0, 1, 100)
rand = np.random.randn(3, 3)        # Normal
rand_int = np.random.randint(0, 100, size=(5, 5))

# Shape e reshape
a.shape                               # (5,)
m = a.reshape(5, 1)                   # Coluna
m = np.arange(12).reshape(3, 4)       # 3x4

# Operações vetorizadas
a * 2                                  # [2, 4, 6, 8, 10]
a ** 2                                 # [1, 4, 9, 16, 25]
np.sqrt(a)
np.log(a)
np.dot(m1, m2)                         # Produto matricial
m1 @ m2                                # Equivalente

# Estatística
np.mean(a); np.median(a); np.std(a)
np.min(a); np.max(a); np.sum(a)
np.percentile(a, 75)
np.corrcoef(x, y)

# Indexação avançada
a[a > 3]                              # Filtro booleano
m[0, :]                               # Primeira linha
m[:, 1]                               # Segunda coluna
m[1:3, 0:2]                           # Submatriz

# Broadcasting
a = np.array([1, 2, 3])
b = np.array([[10], [20], [30]])
a + b  # 3x3 automaticamente
```

---

## Pandas

```python
import pandas as pd

# Criar DataFrame
df = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carlos', 'Diana'],
    'idade': [25, 30, 22, 28],
    'salario': [3000, 5000, 3500, 4500],
    'dept': ['TI', 'RH', 'TI', 'RH']
})

# Ler dados
df = pd.read_csv('dados.csv')
df = pd.read_excel('dados.xlsx')
df = pd.read_json('dados.json')
df = pd.read_sql('SELECT * FROM tabela', conn)

# Exploração
df.head(5); df.tail(5)
df.shape                    # (linhas, colunas)
df.info()                   # Tipos e nulos
df.describe()               # Estatísticas
df.dtypes
df.columns
df.nunique()                # Valores únicos
df['col'].value_counts()

# Seleção
df['nome']                  # Coluna (Series)
df[['nome', 'idade']]      # Múltiplas colunas
df.loc[0]                   # Linha por label
df.iloc[0:3]                # Linhas por posição
df.loc[df['idade'] > 25]   # Filtro

# Filtros avançados
df.query('idade > 25 and dept == "TI"')
df[df['nome'].str.contains('an', case=False)]

# Manipulação
df['bonus'] = df['salario'] * 0.1        # Nova coluna
df['faixa'] = pd.cut(df['idade'], bins=[0, 25, 35, 100], labels=['Jovem', 'Adulto', 'Senior'])
df.rename(columns={'nome': 'funcionario'}, inplace=True)
df.drop(columns=['bonus'], inplace=True)
df.sort_values('salario', ascending=False)

# Agrupamento
df.groupby('dept').agg({
    'salario': ['mean', 'sum', 'count'],
    'idade': 'mean'
}).round(2)

# Missing values
df.isnull().sum()
df.dropna()                             # Remover linhas
df.fillna(0)                            # Preencher com valor
df['col'].fillna(df['col'].median())    # Preencher com mediana

# Merge / Join
pd.merge(df1, df2, on='id', how='left')
pd.concat([df1, df2], axis=0)           # Empilhar

# Pivot
df.pivot_table(values='salario', index='dept', aggfunc='mean')

# Salvar
df.to_csv('saida.csv', index=False)
df.to_excel('saida.xlsx', index=False)
```

---

## Visualização

```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

# Linha
plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='o', label='Vendas')
plt.xlabel('Mês'); plt.ylabel('Valor')
plt.title('Vendas Mensais'); plt.legend()
plt.savefig('grafico.png', dpi=300, bbox_inches='tight')
plt.show()

# Barras
sns.barplot(data=df, x='dept', y='salario', hue='dept', palette='Set2')

# Histograma
sns.histplot(df['salario'], bins=20, kde=True, color='coral')

# Scatter
sns.scatterplot(data=df, x='idade', y='salario', hue='dept', size='bonus')

# Heatmap (correlação)
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f')

# Boxplot
sns.boxplot(data=df, x='dept', y='salario')

# Pairplot
sns.pairplot(df, hue='dept')

# Subplots
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
sns.histplot(df['idade'], ax=axes[0])
sns.histplot(df['salario'], ax=axes[1])
sns.countplot(data=df, x='dept', ax=axes[2])
plt.tight_layout()
```

---

## Estatística

```python
from scipy import stats

# Descritiva
df['salario'].mean()
df['salario'].median()
df['salario'].std()
df['salario'].quantile([0.25, 0.5, 0.75])
df['salario'].skew()     # Assimetria
df['salario'].kurtosis() # Curtose

# Correlação
df[['idade', 'salario']].corr()
r, p_value = stats.pearsonr(df['idade'], df['salario'])

# Teste t (duas amostras)
t_stat, p_val = stats.ttest_ind(grupo_a, grupo_b)
if p_val < 0.05:
    print("Diferença estatisticamente significativa")

# Qui-quadrado (variáveis categóricas)
tabela = pd.crosstab(df['dept'], df['satisfacao'])
chi2, p, dof, expected = stats.chi2_contingency(tabela)

# Distribuição normal
x = np.linspace(-4, 4, 100)
y = stats.norm.pdf(x, loc=0, scale=1)  # Curva normal
```

---

## Pré-processamento

```python
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split

# Encoding categórico
le = LabelEncoder()
df['dept_encoded'] = le.fit_transform(df['dept'])

# One-hot encoding
df_encoded = pd.get_dummies(df, columns=['dept'], drop_first=True)

# Normalização / Padronização
scaler = StandardScaler()
df[['idade', 'salario']] = scaler.fit_transform(df[['idade', 'salario']])

# Outliers (IQR)
Q1 = df['salario'].quantile(0.25)
Q3 = df['salario'].quantile(0.75)
IQR = Q3 - Q1
filtro = (df['salario'] >= Q1 - 1.5*IQR) & (df['salario'] <= Q3 + 1.5*IQR)
df_limpo = df[filtro]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
```

---

## Machine Learning Aplicado

```python
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingRegressor
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score

# Regressão
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(f"R²: {r2_score(y_test, y_pred):.3f}")
print(f"RMSE: {mean_squared_error(y_test, y_pred, squared=False):.3f}")

# Classificação
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
print(f"Acurácia: {accuracy_score(y_test, clf.predict(X_test)):.2%}")

# Validação cruzada
scores = cross_val_score(clf, X, y, cv=5, scoring='accuracy')
print(f"CV Acurácia: {scores.mean():.2%} ± {scores.std():.2%}")

# Feature importance
importances = pd.Series(clf.feature_importances_, index=feature_names)
importances.nlargest(10).plot(kind='barh')
```

---

## Pipeline Completo

```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

# Pipeline de pré-processamento + modelo
num_features = ['idade', 'salario', 'experiencia']
cat_features = ['dept', 'cargo']

preprocessor = ColumnTransformer([
    ('num', Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ]), num_features),
    ('cat', Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OneHotEncoder(handle_unknown='ignore'))
    ]), cat_features)
])

pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=200))
])

pipeline.fit(X_train, y_train)
score = pipeline.score(X_test, y_test)
print(f"Pipeline accuracy: {score:.2%}")
```

---

*Fonte: [W3Schools Data Science](https://www.w3schools.com/datascience/) · Documentação oficial NumPy, Pandas, scikit-learn*
