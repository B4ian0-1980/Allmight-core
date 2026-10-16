---json
{
  "id": "documentacao-fastapi",
  "title": "FastAPI — Guia Completo",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "Guia tecnico e referencias sobre FastAPI — Guia Completo.",
  "gatilhos": [
    "completo",
    "documentacao",
    "fastapi",
    "guia",
    "linguagens",
    "php"
  ],
  "perguntas_tipo": [
    "Como utilizar FastAPI — Guia Completo?",
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

# FastAPI — Guia Completo

**Fonte:** [fastapi.tiangolo.com/tutorial](https://fastapi.tiangolo.com/tutorial/) · [reference](https://fastapi.tiangolo.com/reference/) · [deployment](https://fastapi.tiangolo.com/deployment/)  
**Versão:** FastAPI 0.100+  
**Categoria:** Backend · API Framework Python  
**Última Atualização do Conteúdo:** 2026-02-14  
**Último Acesso às Fontes:** 2026-02-14

---

## 1. O que é FastAPI?

FastAPI é um **framework moderno para APIs Python**, baseado em type hints. O mais rápido em Python (Starlette + Pydantic). Gera documentação Swagger/OpenAPI automaticamente.

---

## 2. Instalação

```bash
pip install "fastapi[standard]"

# Rodar
fastapi dev main.py        # Desenvolvimento (hot reload)
fastapi run main.py        # Produção
```

---

## 3. Hello World

```python
from fastapi import FastAPI

app = FastAPI(title="Minha API", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

Docs automáticas: `http://localhost:8000/docs` (Swagger) · `/redoc` (ReDoc)

---

## 4. Path & Query Parameters

```python
from fastapi import Query, Path
from typing import Optional

@app.get("/users/{user_id}")
async def get_user(user_id: int = Path(..., gt=0)):
    return {"user_id": user_id}

@app.get("/users")
async def list_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=100),
    search: Optional[str] = None,
):
    return {"skip": skip, "limit": limit}
```

---

## 5. Request Body (Pydantic)

```python
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=6)
    role: str = Field(default="viewer")

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str
    created_at: datetime
    model_config = {"from_attributes": True}

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None

@app.post("/users", response_model=UserResponse, status_code=201)
async def create_user(user: UserCreate):
    db_user = save_to_db(user)
    return db_user

@app.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UserUpdate):
    data = user.model_dump(exclude_unset=True)
    return update_in_db(user_id, data)
```

---

## 6. CRUD Completo

```python
from fastapi import HTTPException

@app.post("/users", status_code=201)
async def create_user(user: UserCreate):
    db_user = {"id": next_id, **user.model_dump()}
    return db_user

@app.get("/users")
async def list_users(skip: int = 0, limit: int = 10):
    return list(fake_db.values())[skip:skip + limit]

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="Não encontrado")
    return fake_db[user_id]

@app.delete("/users/{user_id}", status_code=204)
async def delete_user(user_id: int):
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="Não encontrado")
    del fake_db[user_id]
```

---

## 7. Dependency Injection

```python
from fastapi import Depends, Header

async def get_db():
    db = Database()
    try:
        yield db
    finally:
        db.close()

async def get_current_user(token: str = Header(..., alias="Authorization")):
    user = decode_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Token inválido")
    return user

@app.get("/profile")
async def profile(user = Depends(get_current_user), db = Depends(get_db)):
    return {"user": user.name}
```

---

## 8. Middleware e CORS

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_timing(request, call_next):
    import time
    start = time.time()
    response = await call_next(request)
    response.headers["X-Process-Time"] = f"{time.time() - start:.3f}"
    return response
```

---

## 9. Router (Módulos)

```python
# routers/users.py
from fastapi import APIRouter
router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
async def list_users(): return []

# main.py
from routers import users
app.include_router(users.router)
```

---

## 10. Deploy

```bash
# Dev
fastapi dev main.py

# Produção
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4

# Docker
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 11. Django vs FastAPI

| Aspecto | Django | FastAPI |
|---|---|---|
| **Tipo** | Full framework (MTV) | API framework (ASGI) |
| **ORM** | Django ORM nativo | SQLAlchemy / Tortoise |
| **Validação** | Forms / DRF Serializers | Pydantic (nativo) |
| **Async** | Parcial | Nativo |
| **Admin** | Admin nativo | Sem admin nativo |
| **Docs API** | Via DRF | Swagger automático |
| **Performance** | Moderada | Muito alta |
| **Quando usar** | Apps completas | APIs / Microserviços |

---

*Fontes: [fastapi.tiangolo.com/tutorial](https://fastapi.tiangolo.com/tutorial/) · [reference](https://fastapi.tiangolo.com/reference/) · [deployment](https://fastapi.tiangolo.com/deployment/) — Acessado em 2026-02-14*
