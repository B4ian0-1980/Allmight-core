---json
{
  "id": "documentacao_bootstrap",
  "title": "Documentação Bootstrap — Guia Completo",
  "categoria": "04-frameworks",
  "subcategoria": "react",
  "resumo": "**Fonte:** [W3Schools Bootstrap](https://www.w3schools.com/bootstrap/bootstrap_ver.asp) · [Bootstrap Docs](https://getbootstrap.com/docs/) **Versão:** Bootstrap 5.3+",
  "gatilhos": [
    "bootstrap",
    "completo",
    "documentacao",
    "frameworks",
    "guia",
    "react"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação Bootstrap — Guia Completo?",
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

# Documentação Bootstrap — Guia Completo

> **Fonte:** [W3Schools Bootstrap](https://www.w3schools.com/bootstrap/bootstrap_ver.asp) · [Bootstrap Docs](https://getbootstrap.com/docs/)
> **Versão:** Bootstrap 5.3+
> **Atualizado:** 2026-02-14

---

## Sumário

1. [Instalação](#instalação)
2. [Grid System](#grid-system)
3. [Tipografia](#tipografia)
4. [Componentes](#componentes)
5. [Formulários](#formulários)
6. [Utilitários](#utilitários)
7. [JavaScript Components](#javascript-components)

---

## Instalação

```html
<!-- CSS -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

<!-- JS (Bundle inclui Popper) -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

<!-- Icons -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">

<!-- Template base -->
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="bootstrap.min.css" rel="stylesheet">
    <title>App</title>
</head>
<body>
    <div class="container">...</div>
    <script src="bootstrap.bundle.min.js"></script>
</body>
</html>
```

---

## Grid System

```html
<!-- Container -->
<div class="container">    <!-- max-width responsivo -->
<div class="container-fluid"> <!-- 100% width -->
<div class="container-lg">    <!-- 100% até lg, depois max-width -->

<!-- Grid 12 colunas -->
<div class="row">
    <div class="col-12 col-md-6 col-lg-4">1/3 em desktop</div>
    <div class="col-12 col-md-6 col-lg-4">1/3 em desktop</div>
    <div class="col-12 col-md-12 col-lg-4">1/3 em desktop</div>
</div>

<!-- Auto-sizing -->
<div class="row">
    <div class="col">Igual</div>
    <div class="col">Igual</div>
    <div class="col">Igual</div>
</div>

<!-- Offset e Order -->
<div class="col-md-6 offset-md-3">Centralizado</div>
<div class="col order-2">Segundo</div>
<div class="col order-1">Primeiro</div>

<!-- Gap -->
<div class="row g-3">         <!-- Gap 3 (1rem) -->
<div class="row gx-4 gy-2">  <!-- Gap X e Y separados -->
```

### Breakpoints

| Breakpoint | Classe | Width |
|---|---|---|
| Extra small | `.col-` | < 576px |
| Small | `.col-sm-` | ≥ 576px |
| Medium | `.col-md-` | ≥ 768px |
| Large | `.col-lg-` | ≥ 992px |
| Extra large | `.col-xl-` | ≥ 1200px |
| XXL | `.col-xxl-` | ≥ 1400px |

---

## Tipografia

```html
<!-- Títulos -->
<h1 class="display-1">Display 1</h1>
<p class="lead">Parágrafo de destaque</p>
<p class="text-muted">Texto suave</p>
<small class="text-body-secondary">Secundário</small>

<!-- Alinhamento -->
<p class="text-start text-md-center text-lg-end">Responsivo</p>

<!-- Cores de texto -->
<p class="text-primary">Primary</p>
<p class="text-success">Success</p>
<p class="text-danger">Danger</p>
<p class="text-warning">Warning</p>
<p class="text-info">Info</p>

<!-- Background -->
<div class="bg-primary text-white p-3">Primary</div>
<div class="bg-dark text-white p-3">Dark</div>
<div class="bg-body-tertiary p-3">Tertiary</div>
```

---

## Componentes

```html
<!-- Botões -->
<button class="btn btn-primary">Primary</button>
<button class="btn btn-outline-secondary">Outline</button>
<button class="btn btn-lg btn-success">Large</button>
<button class="btn btn-sm btn-danger">Small</button>

<!-- Cards -->
<div class="card" style="width: 18rem;">
    <img src="img.jpg" class="card-img-top" alt="...">
    <div class="card-body">
        <h5 class="card-title">Título</h5>
        <p class="card-text">Descrição</p>
        <a href="#" class="btn btn-primary">Ação</a>
    </div>
</div>

<!-- Navbar -->
<nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
        <a class="navbar-brand" href="#">Logo</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#nav">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="nav">
            <ul class="navbar-nav me-auto">
                <li class="nav-item"><a class="nav-link active" href="#">Home</a></li>
                <li class="nav-item"><a class="nav-link" href="#">Sobre</a></li>
            </ul>
        </div>
    </div>
</nav>

<!-- Alert -->
<div class="alert alert-success alert-dismissible fade show">
    Sucesso!
    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
</div>

<!-- Badge -->
<span class="badge bg-primary">Novo</span>
<span class="badge rounded-pill bg-danger">99+</span>

<!-- List Group -->
<ul class="list-group">
    <li class="list-group-item active">Ativo</li>
    <li class="list-group-item">Item 2</li>
</ul>

<!-- Breadcrumb -->
<nav aria-label="breadcrumb">
    <ol class="breadcrumb">
        <li class="breadcrumb-item"><a href="#">Home</a></li>
        <li class="breadcrumb-item active">Página</li>
    </ol>
</nav>

<!-- Table -->
<table class="table table-striped table-hover table-bordered">
    <thead class="table-dark">
        <tr><th>#</th><th>Nome</th><th>Email</th></tr>
    </thead>
    <tbody>
        <tr><td>1</td><td>Ana</td><td>ana@mail.com</td></tr>
    </tbody>
</table>

<!-- Spinner -->
<div class="spinner-border text-primary" role="status">
    <span class="visually-hidden">Carregando...</span>
</div>

<!-- Progress -->
<div class="progress">
    <div class="progress-bar bg-success" style="width: 75%">75%</div>
</div>
```

---

## Formulários

```html
<form>
    <!-- Input com label flutuante -->
    <div class="form-floating mb-3">
        <input type="email" class="form-control" id="email" placeholder="Email">
        <label for="email">Email</label>
    </div>

    <!-- Select -->
    <select class="form-select mb-3">
        <option selected>Selecione...</option>
        <option value="1">Opção 1</option>
    </select>

    <!-- Textarea -->
    <div class="mb-3">
        <textarea class="form-control" rows="3" placeholder="Mensagem"></textarea>
    </div>

    <!-- Checkbox e Radio -->
    <div class="form-check">
        <input class="form-check-input" type="checkbox" id="termos">
        <label class="form-check-label" for="termos">Aceito</label>
    </div>

    <!-- Switch -->
    <div class="form-check form-switch">
        <input class="form-check-input" type="checkbox" id="notif">
        <label class="form-check-label" for="notif">Notificações</label>
    </div>

    <!-- Input Group -->
    <div class="input-group mb-3">
        <span class="input-group-text">R$</span>
        <input type="number" class="form-control" placeholder="Valor">
    </div>

    <!-- Validação -->
    <div class="mb-3">
        <input type="text" class="form-control is-invalid" required>
        <div class="invalid-feedback">Campo obrigatório.</div>
    </div>

    <button type="submit" class="btn btn-primary">Enviar</button>
</form>
```

---

## Utilitários

```html
<!-- Spacing: m(argin)/p(adding) + t/b/s/e/x/y + 0-5 -->
<div class="mt-3 mb-5 px-4 py-2">Espaçamento</div>
<div class="mx-auto" style="width: 200px;">Centralizado</div>

<!-- Display -->
<div class="d-none d-md-block">Oculto em mobile</div>
<div class="d-flex justify-content-between align-items-center">Flex</div>
<div class="d-flex flex-column flex-md-row gap-3">Responsivo</div>

<!-- Sizing -->
<div class="w-50">50% largura</div>
<div class="h-100">100% altura</div>
<div class="vw-100 vh-100">Full viewport</div>

<!-- Border -->
<div class="border border-primary rounded-3">Borda</div>
<div class="border-0 rounded-circle">Sem borda, circular</div>

<!-- Shadow -->
<div class="shadow-sm">Sombra pequena</div>
<div class="shadow">Sombra normal</div>
<div class="shadow-lg">Sombra grande</div>

<!-- Position -->
<div class="position-relative">
    <div class="position-absolute top-0 end-0">Canto superior direito</div>
</div>
<div class="sticky-top">Fixo no topo ao rolar</div>

<!-- Opacity -->
<div class="opacity-75">75% opacidade</div>

<!-- Overflow -->
<div class="overflow-auto" style="height: 200px;">Scroll se necessário</div>
```

---

## JavaScript Components

```html
<!-- Modal -->
<button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#meuModal">Abrir</button>
<div class="modal fade" id="meuModal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Título</h5>
                <button class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">Conteúdo</div>
            <div class="modal-footer">
                <button class="btn btn-secondary" data-bs-dismiss="modal">Fechar</button>
                <button class="btn btn-primary">Salvar</button>
            </div>
        </div>
    </div>
</div>

<!-- Tooltip -->
<button data-bs-toggle="tooltip" title="Dica">Hover</button>
<script>
    new bootstrap.Tooltip(document.querySelector('[data-bs-toggle="tooltip"]'));
</script>

<!-- Accordion -->
<div class="accordion" id="faq">
    <div class="accordion-item">
        <h2 class="accordion-header">
            <button class="accordion-button" data-bs-toggle="collapse" data-bs-target="#q1">Pergunta 1</button>
        </h2>
        <div id="q1" class="accordion-collapse collapse show" data-bs-parent="#faq">
            <div class="accordion-body">Resposta 1</div>
        </div>
    </div>
</div>

<!-- Toast -->
<div class="toast" role="alert">
    <div class="toast-header">
        <strong class="me-auto">Notificação</strong>
        <button class="btn-close" data-bs-dismiss="toast"></button>
    </div>
    <div class="toast-body">Mensagem aqui</div>
</div>

<!-- Carousel -->
<div id="carrossel" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-inner">
        <div class="carousel-item active"><img src="1.jpg" class="d-block w-100"></div>
        <div class="carousel-item"><img src="2.jpg" class="d-block w-100"></div>
    </div>
    <button class="carousel-control-prev" data-bs-target="#carrossel" data-bs-slide="prev">
        <span class="carousel-control-prev-icon"></span>
    </button>
    <button class="carousel-control-next" data-bs-target="#carrossel" data-bs-slide="next">
        <span class="carousel-control-next-icon"></span>
    </button>
</div>
```

---

*Fonte: [W3Schools Bootstrap](https://www.w3schools.com/bootstrap/) · [Bootstrap 5 Docs](https://getbootstrap.com/docs/)*
