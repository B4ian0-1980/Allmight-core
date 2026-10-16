---json
{
  "id": "documentacao-django",
  "title": "Django 6.0 — Guia Completo",
  "categoria": "03-linguagens",
  "subcategoria": "python",
  "resumo": "Guia tecnico e referencias sobre Django 6.0 — Guia Completo.",
  "gatilhos": [
    "completo",
    "django",
    "documentacao",
    "guia",
    "linguagens",
    "python"
  ],
  "perguntas_tipo": [
    "Como utilizar Django 6.0 — Guia Completo?",
    "Quais as boas praticas de python?"
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
  "dono": "stack-python",
  "prioridade": 2
}
---

# Django 6.0 — Guia Completo

**Fonte:** [docs.djangoproject.com/en/6.0](https://docs.djangoproject.com/en/6.0/)  
**Versão:** Django 6.0  
**Categoria:** Backend · Framework Python  
**Última Atualização do Conteúdo:** 2026-02-14  
**Último Acesso às Fontes:** 2026-02-14

---

## 1. O que é Django?

Django é o **framework web Python de alto nível** que segue o padrão MTV (Model-Template-View). "Baterias incluídas": ORM, Admin, Auth, Forms, Templates, Middleware, e muito mais.

---

## 2. Instalação e Projeto

```bash
pip install django
django-admin startproject myproject .
python manage.py startapp core
python manage.py runserver   # http://127.0.0.1:8000
```

### Estrutura
```
myproject/
├── manage.py
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── core/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── serializers.py
│   ├── templates/core/
│   └── tests.py
└── requirements.txt
```

---

## 3. Models (ORM)

```python
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    role = models.CharField(max_length=20, choices=[
        ('admin', 'Admin'), ('editor', 'Editor'), ('viewer', 'Viewer'),
    ], default='viewer')

    class Meta:
        ordering = ['-date_joined']

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField('Tag', blank=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [models.Index(fields=['slug']), models.Index(fields=['-created_at'])]
```

### Migrations
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

---

## 4. QuerySets

```python
# Buscar
User.objects.all()
User.objects.filter(role='admin')
User.objects.exclude(is_active=False)
User.objects.get(pk=1)

# Filtros avançados
Post.objects.filter(
    title__icontains='django',
    created_at__year=2026,
    author__role='admin',
    tags__name__in=['python', 'web'],
)

# Q objects (OR)
from django.db.models import Count, Avg, Q
Post.objects.filter(Q(title__icontains='django') | Q(content__icontains='django'))

# Agregar
User.objects.annotate(post_count=Count('posts'))
Post.objects.aggregate(avg_len=Avg('content'))

# CRUD
user = User.objects.create(username='joao', email='joao@email.com')
Post.objects.filter(pk=1).update(published=True)
Post.objects.filter(published=False).delete()

# Otimizar
Post.objects.select_related('author')       # FK (JOIN)
Post.objects.prefetch_related('tags')       # M2M (2 queries)
```

---

## 5. Views

```python
# Function-based
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

def user_list(request):
    users = User.objects.filter(is_active=True).values('id', 'username', 'email')
    return JsonResponse(list(users), safe=False)

# Class-based
from django.views.generic import ListView

class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(published=True)
    template_name = 'core/post_list.html'
    paginate_by = 10
```

---

## 6. URLs

```python
# myproject/urls.py
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
]

# core/urls.py
urlpatterns = [
    path('users/', views.user_list, name='user-list'),
    path('users/<int:pk>/', views.user_detail, name='user-detail'),
    path('posts/', views.PostListView.as_view(), name='post-list'),
]
```

---

## 7. Django REST Framework

```python
# serializers.py
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'content', 'author', 'author_name', 'published']

# views.py
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related('author')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        post = self.get_object()
        post.published = True
        post.save()
        return Response({'status': 'published'})
```

---

## 8. Admin

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published', 'created_at']
    list_filter = ['published', 'author__role']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
```

---

## 9. Segurança Empresarial (Hardening)

Para sistemas críticos ("Extremamente Seguros"), o Django oferece ferramentas nativas que devem ser ativadas:

### Configurações de Produção (`settings.py`)
```python
# Habilitar proteção contra ataques de navegador
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Forçar HTTPS
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# HSTS (Strict Transport Security)
SECURE_HSTS_SECONDS = 31536000  # 1 ano
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
```

### Proteção de Dados
1.  **Host Validations:** `ALLOWED_HOSTS` deve ter apenas o domínio de produção.
2.  **Senha Forte:** Use validadores de senha:
    ```python
    AUTH_PASSWORD_VALIDATORS = [
        {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
        {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 'OPTIONS': {'min_length': 12}},
        {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
        {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
    ]
    ```
3.  **2FA (Autenticação de Dois Fatores):** Use `django-otp` ou `django-two-factor-auth`.

### CSP (Content Security Policy)
Use `django-csp` para prevenir XSS avançado:
```python
CSP_DEFAULT_SRC = ("'self'", "cdn.exemplo.com")
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'")
```

---

## 10. Comandos

```bash
python manage.py runserver           # Dev server
python manage.py makemigrations      # Criar migrations
python manage.py migrate             # Aplicar
python manage.py createsuperuser     # Criar admin
python manage.py shell               # Shell interativo
python manage.py test                # Testes
python manage.py collectstatic       # Estáticos
```

---

*Fontes: [docs.djangoproject.com/en/6.0](https://docs.djangoproject.com/en/6.0/) — Acessado em 2026-02-14*
