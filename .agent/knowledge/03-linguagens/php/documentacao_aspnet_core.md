---json
{
  "id": "documentacao_aspnet_core",
  "title": "Documentação ASP.NET Core — Guia Completo",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "**Fonte:** [learn.microsoft.com](https://learn.microsoft.com/aspnet/core) **Versão:** .NET 8 / 9",
  "gatilhos": [
    "asp",
    "aspnet",
    "completo",
    "core",
    "documentacao",
    "guia",
    "linguagens",
    "net"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação ASP.NET Core — Guia Completo?",
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

# Documentação ASP.NET Core — Guia Completo

> **Fonte:** [learn.microsoft.com](https://learn.microsoft.com/aspnet/core)
> **Versão:** .NET 8 / 9
> **Atualizado:** 2026-02-14

---

## Sumário

1. [O que é ASP.NET Core?](#o-que-é-aspnet-core)
2. [Criando uma API (Minimal API)](#criando-uma-api-minimal-api)
3. [Estrutura do Projeto](#estrutura-do-projeto)
4. [Injeção de Dependência (DI)](#injeção-de-dependência-di)
5. [Controller-based API (Tradicional)](#controller-based-api)
6. [Entity Framework Core (EF Core)](#entity-framework-core)
7. [Autenticação e JWT](#autenticação-e-jwt)

---

## O que é ASP.NET Core?

ASP.NET Core é o framework web open-source e cross-platform da Microsoft para construir aplicações modernas conectadas à Internet, como APIs, microservices e Web Apps. É conhecido por sua performance exepcional.

---

## Criando uma API (Minimal API)

Desde o .NET 6, podemos criar APIs completas em um único arquivo `Program.cs` com pouquíssimas linhas.

```csharp
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => "Hello World!");

app.MapGet("/users/{id}", (int id) => 
    new { Id = id, Name = "User " + id });

app.MapPost("/users", (User user) => 
    Results.Created($"/users/{user.Id}", user));

app.Run();

record User(int Id, string Name);
```

---

## Estrutura do Projeto

- **Program.cs**: Ponto de entrada. Configura serviços (DI) e pipeline de requisição (Middleware).
- **appsettings.json**: Configurações (Strings de conexão, chaves de API).
- **Controllers/**: (Opcional) Define endpoints da API.
- **Models/DTOs**: Classes de dados.

### Middleware Pipeline
A ordem importa!

```csharp
var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();
app.UseAuthentication(); // 1. Quem é você?
app.UseAuthorization();  // 2. Você pode entrar?

app.MapControllers();

app.Run();
```

---

## Injeção de Dependência (DI)

ASP.NET Core tem DI nativa. Registramos serviços no `Program.cs`.

### Ciclos de Vida
1. **Transient**: Novo a cada injeção (Leve, stateless).
2. **Scoped**: Novo a cada requisição HTTP (Bancos de dados, User context).
3. **Singleton**: Único para toda a aplicação (Cache, Configurações globais).

```csharp
// Program.cs
builder.Services.AddTransient<IEmailService, EmailService>();
builder.Services.AddScoped<IUserRepository, UserRepository>();
builder.Services.AddSingleton<ICache, MemoryCache>();

// Uso (no construtor)
public class UserController(IUserRepository repo) : ControllerBase
{
    // C# 12 Primary Constructor
}
```

---

## Controller-based API

A abordagem clássica, recomendada para APIs grandes e organizadas.

```csharp
[ApiController]
[Route("api/[controller]")]
public class ProductsController : ControllerBase
{
    private readonly IProductService _service;

    public ProductsController(IProductService service)
    {
        _service = service;
    }

    [HttpGet]
    public ActionResult<List<Product>> GetAll()
    {
        return Ok(_service.GetProducts());
    }

    [HttpGet("{id}")]
    public ActionResult<Product> Get(int id)
    {
        var product = _service.GetById(id);
        if (product == null) return NotFound();
        return Ok(product);
    }
}
```

---

## Entity Framework Core (EF Core)

ORM oficial. Mapeia classes C# para tabelas SQL.

### Modelo
```csharp
public class Todo
{
    public int Id { get; set; }
    public string Title { get; set; }
    public bool IsComplete { get; set; }
}
```

### DbContext
```csharp
public class AppDbContext : DbContext
{
    public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) { }
    
    public DbSet<Todo> Todos { get; set; }
}
```

### Registro e Uso
```csharp
// Program.cs
builder.Services.AddDbContext<AppDbContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("Default")));

// Endpoint
app.MapGet("/todos", async (AppDbContext db) => 
    await db.Todos.ToListAsync());
```

---

## Autenticação e JWT

Proteger APIs com JSON Web Tokens.

1. **Pacote:** `Microsoft.AspNetCore.Authentication.JwtBearer`
2. **Configuração:**

```csharp
builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(options =>
    {
        options.TokenValidationParameters = new TokenValidationParameters
        {
            ValidateIssuer = true,
            ValidateAudience = true,
            ValidateLifetime = true,
            ValidateIssuerSigningKey = true,
            ValidIssuer = "meuApp",
            ValidAudience = "meuApp",
            IssuerSigningKey = new SymmetricSecurityKey(
                Encoding.UTF8.GetBytes("chave-super-secreta-32-chars"))
        };
    });
```

3. **Uso:**

```csharp
app.MapGet("/segredo", () => "Dados sensíveis")
   .RequireAuthorization();
```

---

*Fonte: [learn.microsoft.com/aspnet/core](https://learn.microsoft.com/aspnet/core)*
