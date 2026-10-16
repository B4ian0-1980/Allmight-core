---json
{
  "id": "documentacao_pytest",
  "title": "Pytest — Guia Completo de Testes Python",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "Guia tecnico e referencias sobre Pytest — Guia Completo de Testes Python.",
  "gatilhos": [
    "completo",
    "documentacao",
    "guia",
    "linguagens",
    "php",
    "pytest",
    "python",
    "testes"
  ],
  "perguntas_tipo": [
    "Como utilizar Pytest — Guia Completo de Testes Python?",
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

# Pytest — Guia Completo de Testes Python

**Fonte:** [docs.pytest.org](https://docs.pytest.org/) · [Contents](https://docs.pytest.org/en/stable/contents.html)  
**Versão:** Pytest 8+  
**Categoria:** Testes · Backend · Python  
**Última Atualização do Conteúdo:** 2026-02-14  
**Último Acesso às Fontes:** 2026-02-14

---

## 1. O que é Pytest?

Pytest é o **framework de testes padrão** para Python. Mais simples que unittest, com fixtures poderosas, parametrize e plugins. Usado em Django, FastAPI, Flask e scripts Python.

---

## 2. Instalação

```bash
pip install pytest
pip install pytest-cov          # Coverage
pip install pytest-asyncio      # Testes async
pip install pytest-django       # Django
pip install pytest-mock         # Mocking
```

---

## 3. Estrutura de Testes

```
projeto/
├── src/
│   ├── services/
│   │   └── user_service.py
│   └── utils/
│       └── helpers.py
├── tests/
│   ├── conftest.py             ← Fixtures compartilhadas
│   ├── unit/
│   │   ├── test_helpers.py
│   │   └── test_user_service.py
│   └── integration/
│       └── test_api.py
├── pytest.ini                  ← Configuração
└── requirements-dev.txt
```

### Configuração (`pytest.ini` ou `pyproject.toml`)
```ini
# pytest.ini
[pytest]
testpaths = tests
python_files = test_*.py
python_functions = test_*
addopts = -v --tb=short
```

```toml
# pyproject.toml
[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-v --tb=short"
```

---

## 4. Anatomia de um Teste

```python
# src/calculator.py
def soma(a, b):
    return a + b

def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero")
    return a / b


# tests/test_calculator.py
from src.calculator import soma, dividir
import pytest

def test_soma_basica():
    assert soma(2, 3) == 5

def test_soma_negativos():
    assert soma(-1, -2) == -3

def test_soma_zero():
    assert soma(5, 0) == 5

def test_dividir_normal():
    assert dividir(10, 2) == 5.0

def test_dividir_por_zero():
    with pytest.raises(ValueError, match="Divisão por zero"):
        dividir(10, 0)
```

---

## 5. Assertions

```python
# Igualdade
assert resultado == 5
assert resultado != 0
assert usuario.nome == "João"

# Verdadeiro/Falso
assert usuario.ativo is True
assert usuario.deletado is False
assert resultado is None
assert resultado is not None

# Tipos
assert isinstance(usuario, User)
assert type(resultado) is int

# Coleções
assert "admin" in roles
assert len(users) == 3
assert set(roles) == {"admin", "user"}

# Strings
assert "hello" in response.text
assert response.text.startswith("Error")

# Aproximação (floats)
assert resultado == pytest.approx(0.3, rel=1e-3)

# Exceções
with pytest.raises(ValueError):
    funcao_que_falha()

with pytest.raises(KeyError, match="chave_invalida"):
    dicionario["chave_invalida"]
```

---

## 6. Fixtures (Setup/Teardown)

```python
# tests/conftest.py — compartilhado entre TODOS os testes
import pytest
from src.database import Database
from src.models import User

@pytest.fixture
def db():
    """Conexão com banco de teste"""
    database = Database("sqlite:///:memory:")
    database.create_tables()
    yield database            # yield = teardown automático
    database.close()

@pytest.fixture
def sample_user():
    """Usuário de exemplo"""
    return User(
        name="João Silva",
        email="joao@email.com",
        role="admin"
    )

@pytest.fixture
def admin_user(db):
    """Usuário admin salvo no banco"""
    user = User(name="Admin", email="admin@test.com", role="admin")
    db.save(user)
    return user


# tests/test_user_service.py
def test_criar_usuario(db, sample_user):
    db.save(sample_user)
    found = db.find_by_email("joao@email.com")
    assert found is not None
    assert found.name == "João Silva"

def test_admin_tem_permissao(admin_user):
    assert admin_user.role == "admin"
    assert admin_user.has_permission("manage_users")
```

### Fixture Scopes
```python
@pytest.fixture(scope="function")   # Padrão: por teste
@pytest.fixture(scope="class")      # Por classe de teste
@pytest.fixture(scope="module")     # Por arquivo
@pytest.fixture(scope="session")    # Uma vez por execução inteira
def expensive_setup():
    return create_heavy_resource()
```

---

## 7. Parametrize (Data-Driven Tests)

```python
import pytest

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, -2, -3),
    (0, 0, 0),
    (100, -50, 50),
])
def test_soma(a, b, expected):
    assert soma(a, b) == expected

@pytest.mark.parametrize("email, valido", [
    ("user@email.com", True),
    ("user@", False),
    ("@email.com", False),
    ("user@email", False),
    ("user.name@domain.com.br", True),
])
def test_validar_email(email, valido):
    assert validar_email(email) == valido

# Múltiplos parâmetros combinados
@pytest.mark.parametrize("role", ["admin", "editor", "user"])
@pytest.mark.parametrize("active", [True, False])
def test_permissoes(role, active):
    user = User(role=role, active=active)
    # Testa 6 combinações (3 roles × 2 active)
```

---

## 8. Marks (Categorizar Testes)

```python
import pytest

@pytest.mark.slow
def test_processo_pesado():
    """Testa algo que demora"""
    pass

@pytest.mark.skip(reason="Feature ainda não implementada")
def test_feature_futura():
    pass

@pytest.mark.skipif(
    sys.platform == "win32",
    reason="Não roda no Windows"
)
def test_unix_only():
    pass

@pytest.mark.xfail(reason="Bug conhecida #123")
def test_bug_conhecida():
    """Espera-se que falhe"""
    assert funcao_bugada() == esperado
```

```bash
# Rodar apenas testes marcados como 'slow'
pytest -m slow

# Rodar tudo EXCETO slow
pytest -m "not slow"
```

---

## 9. Mocking

```python
from unittest.mock import patch, MagicMock
import pytest

# Mock com decorator
@patch('src.services.email.send_email')
def test_criar_usuario_envia_email(mock_send):
    mock_send.return_value = True

    user_service.create_user("joao@email.com")

    mock_send.assert_called_once_with(
        to="joao@email.com",
        subject="Bem-vindo!"
    )

# Mock com context manager
def test_api_externa():
    with patch('src.api.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"data": "ok"}

        result = fetch_external_data()

        assert result == {"data": "ok"}
        mock_get.assert_called_once()

# pytest-mock (mais limpo)
def test_com_mocker(mocker):
    mock_db = mocker.patch('src.services.database.save')
    mock_db.return_value = True

    result = create_item({"name": "Test"})

    assert result is True
    mock_db.assert_called_once()
```

---

## 10. Testes Async

```python
import pytest
import httpx

@pytest.mark.asyncio
async def test_api_async():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.example.com/users")

    assert response.status_code == 200
    assert len(response.json()) > 0
```

---

## 11. Testes Django

```python
# pytest.ini
[pytest]
DJANGO_SETTINGS_MODULE = myproject.settings
django_find_rootdir = true

# tests/test_views.py
import pytest
from django.test import Client

@pytest.mark.django_db
def test_home_page(client: Client):
    response = client.get("/")
    assert response.status_code == 200

@pytest.mark.django_db
def test_criar_usuario(client: Client):
    response = client.post("/api/users/", {
        "name": "João",
        "email": "joao@email.com"
    }, content_type="application/json")

    assert response.status_code == 201
```

---

## 12. Comandos

```bash
# Rodar todos
pytest

# Arquivo específico
pytest tests/test_calculator.py

# Função específica
pytest tests/test_calculator.py::test_soma_basica

# Classe específica
pytest tests/test_user.py::TestUserService

# Verbose
pytest -v

# Parar no primeiro erro
pytest -x

# Mostrar prints (stdout)
pytest -s

# Coverage
pytest --cov=src --cov-report=html

# Paralelismo (precisa pytest-xdist)
pytest -n auto

# Apenas testes que falharam da última vez
pytest --lf

# Testes novos/modificados primeiro
pytest --nf
```

---

## 13. Comparação PHPUnit vs Jest vs Pytest

| Aspecto | PHPUnit | Jest | Pytest |
|---|---|---|---|
| **Linguagem** | PHP | JavaScript/TS | Python |
| **Assertion** | `$this->assertEquals()` | `expect().toBe()` | `assert ==` |
| **Data provider** | `@dataProvider` | `test.each()` | `@pytest.mark.parametrize` |
| **Mock** | `createMock()` | `jest.fn()` | `unittest.mock.patch()` |
| **Setup** | `setUp()` | `beforeEach()` | `@pytest.fixture` |
| **Async** | N/A | `async test` | `@pytest.mark.asyncio` |
| **Coverage** | `--coverage-html` | `--coverage` | `--cov` |

---

*Fontes: [docs.pytest.org](https://docs.pytest.org/) · [unittest](https://docs.pytest.org/en/stable/how-to/unittest.html) — Acessado em 2026-02-14*
