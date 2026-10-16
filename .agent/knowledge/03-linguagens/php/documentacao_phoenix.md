---json
{
  "id": "documentacao_phoenix",
  "title": "Documentação: Phoenix Framework",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "**Linguagem:** Elixir (Erlang VM / BEAM) **Tipo:** Framework Web de Alta Concorrência",
  "gatilhos": [
    "documentacao",
    "framework",
    "linguagens",
    "phoenix",
    "php"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação: Phoenix Framework?",
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

# Documentação: Phoenix Framework

> **Linguagem:** Elixir (Erlang VM / BEAM)
> **Tipo:** Framework Web de Alta Concorrência
> **Site Oficial:** [phoenixframework.org](https://www.phoenixframework.org)

## O que é?
Phoenix é um framework de desenvolvimento web escrito em Elixir que implementa o padrão MVC. Ele é famoso por permitir a criação de aplicações ricas e interativas em tempo real com facilidade, escalabilidade e performance extrema (milhões de conexões simultâneas).

## Principais Diferenciais
*   **Velocidade:** Respostas de microssegundos.
*   **Concorrência:** Baseado na BEAM (Erlang VM), lida com muitos usuários simultâneos sem "suar".
*   **LiveView:** Permite criar interfaces ricas e dinâmicas (como SPAs) renderizadas no servidor, sem escrever JavaScript complexo.
*   **Channels:** WebSockets fáceis para recursos de tempo real (chat, notificações).

## Instalação

Pré-requisitos: Elixir e Erlang instalados.

```bash
# Instalar o gerador Phoenix
mix archive.install hex phx_new

# Criar novo projeto
mix phx.new hello

# Iniciar o servidor
cd hello
mix phx.server
```

Acesse em `http://localhost:4000`.

## Estrutura (MVC+)
*   `lib/hello_web/controllers/`: Controladores.
*   `lib/hello_web/templates/`: Views (HTML com EEx/HEEx).
*   `lib/hello/`: Lógica de negócio e contextos (Contexts).

### Exemplo de LiveView
LiveView é o recurso "matador" do Phoenix.

```elixir
# lib/hello_web/live/thermostat_live.ex
defmodule HelloWeb.ThermostatLive do
  use HelloWeb, :live_view

  def render(assigns) do
    ~H"""
    Current temperature: <%= @temperature %>
    <button phx-click="inc">+</button>
    """
  end

  def mount(_params, _session, socket) do
    {:ok, assign(socket, temperature: 50)}
  end

  def handle_event("inc", _uri, socket) do
    {:noreply, update(socket, :temperature, &(&1 + 1))}
  end
end
```

## Ecto (Camada de Dados)
O Phoenix usa Ecto, que não é apenas um ORM, mas um wrapper de dados e query builder.

```elixir
# Schema
schema "users" do
  field :name, :string
  field :email, :string
  timestamps()
end
```

## Referências
*   [Guias Oficiais](https://hexdocs.pm/phoenix/overview.html)
*   [Elixir School](https://elixirschool.com/pt)
