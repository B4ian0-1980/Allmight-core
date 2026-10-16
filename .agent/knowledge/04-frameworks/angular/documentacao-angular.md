---json
{
  "id": "documentacao-angular",
  "title": "Angular — Guia Completo",
  "categoria": "04-frameworks",
  "subcategoria": "angular",
  "resumo": "Guia tecnico e referencias sobre Angular — Guia Completo.",
  "gatilhos": [
    "angular",
    "completo",
    "documentacao",
    "frameworks",
    "guia"
  ],
  "perguntas_tipo": [
    "Como utilizar Angular — Guia Completo?",
    "Quais as boas praticas de angular?"
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
  "dono": "stack-angular",
  "prioridade": 2
}
---

# Angular — Guia Completo

**Fonte:** [angular.dev/overview](https://angular.dev/overview) · [angular.dev/ai](https://angular.dev/ai/develop-with-ai)  
**Versão:** Angular 17+ (Standalone, Signals)  
**Categoria:** Frontend · Framework Full  
**Última Atualização do Conteúdo:** 2026-02-14  
**Último Acesso às Fontes:** 2026-02-14

---

## 1. O que é Angular?

Angular é um **framework frontend completo** mantido pelo Google. Inclui Router, Forms, HTTP Client, RxJS, DI, e testing integrados. Usa TypeScript obrigatório.

---

## 2. Criando Projeto

```bash
npm install -g @angular/cli
ng new meu-app --standalone --style=scss --routing
cd meu-app
ng serve       # http://localhost:4200
```

---

## 3. Componentes Standalone

```typescript
import { Component, Input, Output, EventEmitter, signal, computed } from '@angular/core'
import { CommonModule } from '@angular/common'

@Component({
  selector: 'app-user-card',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div class="card" [class.active]="isActive()">
      <h3>{{ name }}</h3>
      <p>Cliques: {{ count() }}</p>
      <button (click)="increment()">+1</button>
      @if (isActive()) {
        <span class="badge">Ativo</span>
      }
    </div>
  `,
})
export class UserCardComponent {
  @Input({ required: true }) name!: string
  @Output() onDelete = new EventEmitter<string>()

  count = signal(0)
  isActive = computed(() => this.count() > 0)

  increment() { this.count.update(c => c + 1) }
}
```

---

## 4. Signals (Reatividade Moderna)

```typescript
import { signal, computed, effect } from '@angular/core'

const count = signal(0)
count()                    // Ler
count.set(5)               // Definir
count.update(c => c + 1)   // Atualizar

const doubled = computed(() => count() * 2)

effect(() => {
  console.log(`Count: ${count()}, Doubled: ${doubled()}`)
})
```

---

## 5. Template Syntax (Angular 17+)

```html
<!-- Property binding -->
<img [src]="imageUrl" />
<button [disabled]="isLoading">Enviar</button>

<!-- Event binding -->
<button (click)="handleClick()">Click</button>
<form (ngSubmit)="onSubmit()">

<!-- Two-way binding -->
<input [(ngModel)]="name" />

<!-- New Control Flow -->
@if (users.length > 0) {
  <ul>
    @for (user of users; track user.id) {
      <li>{{ user.name }}</li>
    }
  </ul>
} @else {
  <p>Nenhum usuário</p>
}

@switch (status) {
  @case ('loading') { <spinner /> }
  @case ('error') { <p>Erro!</p> }
  @default { <data-display /> }
}

@defer (on viewport) {
  <heavy-component />
} @placeholder {
  <p>Carregando...</p>
}
```

---

## 6. Services e Dependency Injection

```typescript
import { Injectable, inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'

@Injectable({ providedIn: 'root' })
export class UserService {
  private http = inject(HttpClient)

  getAll() { return this.http.get<User[]>('/api/users') }
  getById(id: string) { return this.http.get<User>(`/api/users/${id}`) }
  create(user: Partial<User>) { return this.http.post<User>('/api/users', user) }
  delete(id: string) { return this.http.delete<void>(`/api/users/${id}`) }
}

// No componente
export class UserListComponent {
  private userService = inject(UserService)
  users = signal<User[]>([])

  ngOnInit() {
    this.userService.getAll().subscribe(data => this.users.set(data))
  }
}
```

---

## 7. Routing

```typescript
import { Routes } from '@angular/router'

export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'login', loadComponent: () => import('./login.component').then(c => c.LoginComponent) },
  { path: 'dashboard', loadComponent: () => import('./dashboard.component').then(c => c.DashboardComponent), canActivate: [authGuard] },
  { path: 'user/:id', loadComponent: () => import('./user.component').then(c => c.UserComponent) },
  { path: '**', redirectTo: '' },
]
```

---

## 8. Reactive Forms

```typescript
import { ReactiveFormsModule, FormBuilder, Validators } from '@angular/forms'

@Component({
  standalone: true,
  imports: [ReactiveFormsModule],
  template: `
    <form [formGroup]="form" (ngSubmit)="submit()">
      <input formControlName="email" />
      <input formControlName="password" type="password" />
      <button [disabled]="form.invalid">Entrar</button>
    </form>
  `
})
export class LoginComponent {
  private fb = inject(FormBuilder)
  form = this.fb.group({
    email: ['', [Validators.required, Validators.email]],
    password: ['', [Validators.required, Validators.minLength(6)]],
  })

  submit() { if (this.form.valid) console.log(this.form.value) }
}
```

---

## 9. Segurança Empresarial

### Prevenção XSS
O Angular escapa automaticamente dados no template.
**Evite (ou use com cuidado):** `innerHTML` ou `DomSanitizer.bypassSecurityTrustHtml`.

### Route Guards (Proteção de Acesso)
```typescript
import { inject } from '@angular/core'
import { Router } from '@angular/router'
import { AuthService } from './auth.service'

export const authGuard = () => {
  const auth = inject(AuthService)
  const router = inject(Router)
  
  if (auth.isLoggedIn()) return true
  return router.parseUrl('/login')
}
```

### HTTP Interceptors (JWT & CSRF)
Anexe tokens automaticamente e trate erros 401:
```typescript
import { HttpInterceptorFn } from '@angular/common/http'

export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const token = localStorage.getItem('token')
  const authReq = token ? req.clone({ setHeaders: { Authorization: `Bearer ${token}` } }) : req
  return next(authReq)
}

// Em app.config.ts
provideHttpClient(withInterceptors([authInterceptor]))
```

---

## 10. CLI Commands

```bash
ng new app-name            # Criar projeto
ng serve                   # Dev server (4200)
ng generate component Name # Criar componente
ng generate service Name   # Criar service
ng build                   # Build production
ng test                    # Testes (Karma)
ng update                  # Atualizar Angular
```

---

## 10. Angular vs React vs Vue

| Aspecto | Angular | React | Vue |
|---|---|---|---|
| **Tipo** | Framework completo | Biblioteca | Framework progressivo |
| **Linguagem** | TypeScript (obrigatório) | JSX/TSX | SFC (.vue) |
| **State** | Signals | useState | ref/reactive |
| **Routing** | Incluso | React Router | Vue Router |
| **Forms** | Incluso (Reactive) | Manual | v-model |
| **HTTP** | HttpClient incluso | fetch/axios | fetch/axios |
| **DI** | Nativo | Context/Props | provide/inject |

---

*Fontes: [angular.dev](https://angular.dev/overview) · [angular.dev/ai](https://angular.dev/ai/develop-with-ai) — Acessado em 2026-02-14*
