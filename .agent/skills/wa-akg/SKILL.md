---
name: wa-akg
description: "Professional multi-session WhatsApp Gateway, Dashboard, and Automation System powered by Next.js 15, Baileys (@whiskeysockets/baileys), and Prisma ORM. Provides 109+ REST API endpoints, webhooks, auto-replies, and scheduled broadcasts."
---

# WA-AKG WhatsApp Gateway & Automation Guide

**WA-AKG** is a multi-session WhatsApp API Gateway, Web Dashboard, and Automation Engine built with **Next.js 15**, **Baileys WebSocket engine** (`@whiskeysockets/baileys`), and **Prisma ORM**. It turns WhatsApp numbers into programmable RESTful APIs with bi-directional webhooks.

- **Upstream Repository:** [https://github.com/mrifqidaffaaditya/WA-AKG](https://github.com/mrifqidaffaaditya/WA-AKG)
- **Tech Stack:** Next.js 15, TypeScript, Tailwind CSS, Radix UI, Prisma ORM, Baileys

---

## 🚀 Core Capabilities

1. **Multi-Session Management:**
   - Run multiple WhatsApp accounts simultaneously.
   - Connect via dynamic QR Code scan or Phone Number Pairing Code.
2. **REST API Gateway (109+ Endpoints):**
   - Direct messaging: text, image, video, audio, document, sticker, location, contacts.
   - Group management: create, invite, promote, demote, leave, kick.
   - Status & Stories: send WhatsApp stories programmatically.
3. **Automations & Anti-Ban:**
   - **Smart Auto-Reply:** keyword trigger with context filters (Private / Group / Both).
   - **Safe Broadcast:** randomized anti-ban delay (10s–30s) across recipient batches.
   - **Task Scheduler:** schedule future messages with media attachments.
4. **Real-Time Webhooks:**
   - Dispatches `message.received`, `connection.update`, `messages.upsert`, and group events to external URLs/CRMs.
5. **Interactive Dashboard & OpenAPI:**
   - Built-in Swagger UI documentation (`/docs`).
   - Web GUI for managing active sessions, chat logs, and auto-reply rules.

---

## 📦 Architecture & Data Flow

```mermaid
graph LR
    Agent[Agent / App / CRM] -->|REST API| WA_AKG[WA-AKG Gateway (Next.js + Baileys)]
    WA_AKG -->|Prisma| DB[(SQLite / MySQL / Postgres)]
    WA_AKG -->|WebSocket| WAServer[[WhatsApp Network]]
    WAServer -.->|Incoming Event| WA_AKG
    WA_AKG -.->|HTTP Webhook| WebhookEndpoint[Webhook Receiver / Agent]
```

---

## 🛠️ On-Demand Installation Guide (When Ready to Deploy)

When you decide to install and start the service:

### 1. Clone & Dependencies
```bash
git clone https://github.com/mrifqidaffaaditya/WA-AKG.git wa-akg
cd wa-akg
npm install
```

### 2. Environment Configuration (`.env`)
Create a `.env` file in the project root:
```env
# Server Port
PORT=3000

# Database (SQLite recommended for zero-config local run)
DATABASE_URL="file:./prisma/dev.db"
# Or MySQL (e.g. XAMPP):
# DATABASE_URL="mysql://root:@localhost:3306/wa_akg"

# NextAuth / App Secrets
NEXTAUTH_URL="http://localhost:3000"
NEXTAUTH_SECRET="your-ultra-secure-random-secret-key-32-chars"

# Optional integrations
REMOVE_BG_API_KEY=""
```

### 3. Database Initialization
```bash
npx prisma db push
npx prisma generate
```

### 4. Setup Initial Admin & Run
```bash
# Create admin user
node scripts/setup-admin.js

# Start development server
npm run dev

# Or build & start production server
npm run build
npm run start
```

---

## 📡 Essential REST API Endpoints

All authenticated requests require `Authorization: Bearer <API_KEY>` or session tokens.

### 1. Create / Start Session
* `POST /api/sessions/create`
* **Body:** `{"sessionId": "bot-marketing"}`
* **Response:** Returns session metadata and QR Code string/data URL.

### 2. Send Text Message
* `POST /api/messages/send-text`
```json
{
  "sessionId": "bot-marketing",
  "to": "5511999999999",
  "text": "Hello! Message dispatched via WA-AKG Gateway."
}
```

### 3. Send Media (Image / Document)
* `POST /api/messages/send-media`
```json
{
  "sessionId": "bot-marketing",
  "to": "5511999999999",
  "mediaUrl": "https://example.com/report.pdf",
  "mediaType": "document",
  "fileName": "Relatorio_Mensal.pdf",
  "caption": "Segue o relatório mensal solicitado."
}
```

### 4. Webhook Receiver Format
Incoming events forwarded to your configured webhook URL:
```json
{
  "event": "message.received",
  "sessionId": "bot-marketing",
  "timestamp": "2026-10-11T17:40:00.000Z",
  "data": {
    "from": "5511988888888@s.whatsapp.net",
    "senderName": "Cliente",
    "text": "Preciso de suporte",
    "isGroup": false
  }
}
```

---

## 💡 When to Recommend this Skill

- When the user asks to integrate WhatsApp notifications, bots, or customer service into local web projects.
- When an agent needs to dispatch alerts, reports, or OTP codes directly to WhatsApp numbers.
- When building a multi-tenant or multi-account WhatsApp broadcast and customer support dashboard.
