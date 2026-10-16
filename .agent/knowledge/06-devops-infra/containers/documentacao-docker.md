---json
{
  "id": "documentacao-docker",
  "title": "Docker — Guia Completo",
  "categoria": "06-devops-infra",
  "subcategoria": "containers",
  "resumo": "Guia tecnico e referencias sobre Docker — Guia Completo.",
  "gatilhos": [
    "completo",
    "containers",
    "devops",
    "docker",
    "documentacao",
    "guia",
    "infra"
  ],
  "perguntas_tipo": [
    "Como utilizar Docker — Guia Completo?",
    "Quais as boas praticas de containers?"
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
  "dono": "stack-containers",
  "prioridade": 2
}
---

# Docker — Guia Completo

**Fonte:** [docs.docker.com](https://docs.docker.com/) | **Versão:** 24+  
**Categoria:** Containerização & DevOps  
**Uso:** Ambiente de desenvolvimento, deploy, CI/CD

---

## 1. O que é Docker?

Docker **empacota** sua aplicação e todas as dependências em um **container** — uma unidade isolada e portátil que roda igual em qualquer lugar (dev, staging, produção).

```
┌─────────────────────────────┐
│         Seu Computador      │
│  ┌────────┐  ┌────────┐    │
│  │ Container│ │Container│   │
│  │ PHP 8.3 │ │ Node 20│    │
│  │ Laravel │ │ Next.js│    │
│  │ Apache  │ │ :3000  │    │
│  └────┬────┘ └───┬────┘    │
│       └─────┬────┘         │
│        Docker Engine        │
│         (Linux Kernel)      │
└─────────────────────────────┘
```

---

## 2. Instalação

### Docker Desktop (Windows/Mac)
Baixe em [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/)

### Docker Engine (Linux/Servidor)
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install docker.io docker-compose-v2
sudo systemctl enable docker
sudo usermod -aG docker $USER  # Roda sem sudo

# Verificar
docker --version
docker compose version
```

---

## 3. Comandos Essenciais

### Containers
```bash
# Rodar container
docker run -d --name meu-app -p 3000:3000 node:20-alpine
#             └─ nome    └─ porta host:container └─ imagem

# Listar containers
docker ps               # Rodando
docker ps -a             # Todos (incluindo parados)

# Parar / Iniciar / Reiniciar
docker stop meu-app
docker start meu-app
docker restart meu-app

# Remover
docker rm meu-app        # Remove container
docker rm -f meu-app     # Forçar (mesmo rodando)

# Logs
docker logs meu-app
docker logs -f meu-app   # Follow (tempo real)
docker logs --tail 50 meu-app  # Últimas 50 linhas

# Entrar no container
docker exec -it meu-app bash
docker exec -it meu-app sh     # Alpine não tem bash

# Rodar comando dentro do container
docker exec meu-app ls /app
docker exec meu-app npm test
```

### Imagens
```bash
# Listar imagens locais
docker images

# Baixar imagem
docker pull php:8.3-fpm
docker pull node:20-alpine
docker pull mysql:8.0

# Construir imagem
docker build -t minha-app:1.0 .
docker build -f Dockerfile.prod -t minha-app:prod .

# Remover imagem
docker rmi node:20-alpine

# Limpar imagens/containers não usados
docker system prune -a       # ⚠️ Remove TUDO não usado
docker image prune            # Só imagens sem container
docker container prune        # Só containers parados
```

### Volumes (Persistência)
```bash
# Criar volume
docker volume create dados-db

# Usar volume
docker run -d -v dados-db:/var/lib/mysql mysql:8.0

# Bind mount (pasta local → container)
docker run -d -v $(pwd)/src:/app/src node:20

# Listar / Remover
docker volume ls
docker volume rm dados-db
```

---

## 4. Dockerfile — Construir Imagens

### Node.js / Next.js
```dockerfile
# Dockerfile
FROM node:20-alpine AS base

WORKDIR /app

# Instalar dependências
COPY package*.json ./
RUN npm ci

# Copiar código
COPY . .

# Build
RUN npm run build

# Produção
FROM node:20-alpine AS runner
WORKDIR /app

COPY --from=base /app/.next/standalone ./
COPY --from=base /app/.next/static ./.next/static
COPY --from=base /app/public ./public

EXPOSE 3000
ENV NODE_ENV=production

CMD ["node", "server.js"]
```

### PHP / Laravel
```dockerfile
FROM php:8.3-fpm

# Extensões PHP
RUN docker-php-ext-install pdo pdo_mysql bcmath

# Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

WORKDIR /var/www/html

# Dependências
COPY composer.json composer.lock ./
RUN composer install --no-dev --optimize-autoloader

# Código
COPY . .

# Permissões
RUN chown -R www-data:www-data storage bootstrap/cache

EXPOSE 9000
CMD ["php-fpm"]
```

### Python / Django / FastAPI
```dockerfile
FROM python:3.12-slim

WORKDIR /app

# Dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Código
COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Boas Práticas para Dockerfile
```dockerfile
# ✅ Use imagens Alpine (menores)
FROM node:20-alpine          # ~50MB vs ~350MB

# ✅ Multi-stage builds (imagem final menor)
FROM node:20-alpine AS builder
RUN npm run build

FROM node:20-alpine AS runner
COPY --from=builder /app/dist ./dist

# ✅ .dockerignore (não copiar lixo)
# Crie .dockerignore:
# node_modules
# .git
# .env
# dist

# ✅ Copie package.json antes do código (cache de dependências)
COPY package*.json ./
RUN npm ci
COPY . .

# ❌ Evite rodar como root
RUN addgroup -S app && adduser -S app -G app
USER app
```

---

## 5. Docker Compose — Múltiplos Containers

### `docker-compose.yml` — Stack Completa
```yaml
# docker-compose.yml
version: "3.8"

services:
  # ======== BANCO DE DADOS ========
  db:
    image: mysql:8.0
    container_name: app-db
    restart: unless-stopped
    environment:
      MYSQL_ROOT_PASSWORD: root_secret
      MYSQL_DATABASE: meu_banco
      MYSQL_USER: app_user
      MYSQL_PASSWORD: app_secret
    ports:
      - "3306:3306"
    volumes:
      - db-data:/var/lib/mysql
      - ./docker/mysql/init.sql:/docker-entrypoint-initdb.d/init.sql
    networks:
      - app-network

  # ======== BACKEND PHP/LARAVEL ========
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: app-backend
    restart: unless-stopped
    volumes:
      - ./backend:/var/www/html
    environment:
      DB_HOST: db
      DB_PORT: 3306
      DB_DATABASE: meu_banco
      DB_USERNAME: app_user
      DB_PASSWORD: app_secret
    depends_on:
      - db
    networks:
      - app-network

  # ======== WEBSERVER NGINX ========
  nginx:
    image: nginx:alpine
    container_name: app-nginx
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./backend:/var/www/html
      - ./docker/nginx/default.conf:/etc/nginx/conf.d/default.conf
    depends_on:
      - backend
    networks:
      - app-network

  # ======== FRONTEND NEXT.JS ========
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    container_name: app-frontend
    restart: unless-stopped
    ports:
      - "3000:3000"
    volumes:
      - ./frontend:/app
      - /app/node_modules  # Não montar node_modules local
    environment:
      NEXT_PUBLIC_API_URL: http://localhost/api
    depends_on:
      - backend
    networks:
      - app-network

  # ======== REDIS (CACHE/FILAS) ========
  redis:
    image: redis:7-alpine
    container_name: app-redis
    restart: unless-stopped
    ports:
      - "6379:6379"
    volumes:
      - redis-data:/data
    networks:
      - app-network

  # ======== PHPMYADMIN (DEV) ========
  phpmyadmin:
    image: phpmyadmin:5
    container_name: app-phpmyadmin
    restart: unless-stopped
    ports:
      - "8080:80"
    environment:
      PMA_HOST: db
      PMA_USER: root
      PMA_PASSWORD: root_secret
    depends_on:
      - db
    networks:
      - app-network
    profiles:
      - dev  # Só sobe com: docker compose --profile dev up

volumes:
  db-data:
  redis-data:

networks:
  app-network:
    driver: bridge
```

### Comandos Docker Compose
```bash
# Subir tudo
docker compose up -d

# Subir com rebuild
docker compose up -d --build

# Subir com profile dev
docker compose --profile dev up -d

# Ver logs
docker compose logs -f
docker compose logs -f backend

# Parar tudo
docker compose down

# Parar e remover volumes (⚠️ dados do banco!)
docker compose down -v

# Executar comando em um serviço
docker compose exec backend php artisan migrate
docker compose exec frontend npm run build
docker compose exec db mysql -u root -p

# Ver status
docker compose ps
```

---

## 6. Nginx Config para Laravel + Next.js

```nginx
# docker/nginx/default.conf
server {
    listen 80;
    server_name localhost;

    # Frontend Next.js
    location / {
        proxy_pass http://frontend:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
    }

    # Backend Laravel API
    location /api {
        root /var/www/html/public;
        try_files $uri $uri/ /index.php?$query_string;

        location ~ \.php$ {
            fastcgi_pass backend:9000;
            fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
            include fastcgi_params;
        }
    }
}
```

---

## 7. `.dockerignore`

```dockerignore
# Dependências
node_modules
vendor

# Ambiente
.env
.env.local
.env.*.local

# Git
.git
.gitignore

# Build/Cache
dist
.next
storage/framework/cache
storage/logs

# IDE
.vscode
.idea

# Docker
docker-compose*.yml
Dockerfile*

# OS
.DS_Store
Thumbs.db
```

---

## 8. Receitas Rápidas

### MySQL rápido para desenvolvimento
```bash
docker run -d --name mysql-dev \
  -e MYSQL_ROOT_PASSWORD=root \
  -e MYSQL_DATABASE=meu_banco \
  -p 3306:3306 \
  -v mysql-data:/var/lib/mysql \
  mysql:8.0
```

### PostgreSQL rápido
```bash
docker run -d --name postgres-dev \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=admin \
  -e POSTGRES_DB=meu_banco \
  -p 5432:5432 \
  -v pg-data:/var/lib/postgresql/data \
  postgres:16-alpine
```

### Redis rápido
```bash
docker run -d --name redis-dev \
  -p 6379:6379 \
  redis:7-alpine
```

### Backup do banco via Docker
```bash
# MySQL dump
docker exec mysql-dev mysqldump -u root -proot meu_banco > backup.sql

# PostgreSQL dump
docker exec postgres-dev pg_dump -U admin meu_banco > backup.sql

# Restaurar
docker exec -i mysql-dev mysql -u root -proot meu_banco < backup.sql
```

---

## 9. Cheatsheet

| Ação | Comando |
|---|---|
| Rodar container | `docker run -d -p 3000:3000 imagem` |
| Listar containers | `docker ps` |
| Parar container | `docker stop nome` |
| Remover container | `docker rm nome` |
| Ver logs | `docker logs -f nome` |
| Entrar no container | `docker exec -it nome bash` |
| Construir imagem | `docker build -t nome:tag .` |
| Listar imagens | `docker images` |
| Compose up | `docker compose up -d` |
| Compose down | `docker compose down` |
| Compose logs | `docker compose logs -f` |
| Limpar tudo | `docker system prune -a` |

---

*Fonte: [docs.docker.com](https://docs.docker.com/) — Consultado em 2026-02-14*
