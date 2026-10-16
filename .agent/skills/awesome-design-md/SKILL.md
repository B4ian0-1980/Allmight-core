---
name: awesome-design-md
description: "Curated collection and specification guide for DESIGN.md design system documents (Google Stitch standard). Contains analyzed design tokens, colors, typography, component rules, and visual guidelines from 73+ top tech products (Claude, Vercel, Linear, Cursor, Stripe, Mistral, Raycast)."
---

# Awesome DESIGN.md — Design System Standard for AI Agents

**awesome-design-md** is a comprehensive guide and repository of **`DESIGN.md`** specifications based on the **Google Stitch** standard. It enables AI coding agents (Claude Code, Antigravity, Cursor, Lovable) to generate visually stunning, brand-consistent interfaces without Figma exports or complex JSON schemas.

- **Upstream Repository:** [https://github.com/voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
- **Official Portal & Catalog:** [https://getdesign.md/](https://getdesign.md/)
- **Standard Spec:** [Google Stitch DESIGN.md](https://stitch.withgoogle.com/docs/design-md/overview/)

---

## 🎨 What is a `DESIGN.md`?

`DESIGN.md` is a plain-text design system document written in Markdown that AI agents read before writing UI code:

| File | Read By | Role in Project |
| :--- | :--- | :--- |
| `AGENTS.md` / `RULES.md` | Coding Agents | Architectural guidelines, coding rules, workflows |
| `DESIGN.md` | Design & Frontend Agents | Visual tokens, palettes, typography, spacing, component feel |

Drop a `DESIGN.md` into your project root, and the agent instantly understands the visual language and constraints.

---

## 📚 73+ Analyzed Brand Design Languages

The repository extracts complete design systems from industry-leading developer tools and platforms:

### 1. AI & LLM Platforms
- **Claude (Anthropic):** Warm terracotta accent (`#D97757`), clean editorial typography, paper-like backgrounds, restrained card styling.
- **Vercel:** Void-black canvas (`#000`), Geist Sans/Mono, crisp 1px borders (`#333`), monochromatic precision, zero rounded pills.
- **Cursor:** AI-native IDE aesthetic, sleek dark chrome, subtle gradient borders, syntax-tailored glow effects.
- **Mistral AI:** French minimalist layout, clean retro typography, orange/amber accents, high-contrast monospace blocks.
- **Replicate:** Code-first white/dark canvas, brutalist clean borders, monospace status badges, raw utility aesthetics.
- **xAI:** Stark monochrome, futuristic minimalism, hyper-condensed typography.

### 2. Developer Tools & Dashboards
- **Linear:** Fast keyboard-first aesthetic, smoky dark backgrounds (`#0F1015`), subtle purple/cyan micro-borders, refined hover transitions.
- **Stripe:** World-class gradient meshes, subtle multi-layered shadows, precision typography, executive finance polish.
- **Raycast:** Sleek macOS dark chrome, neon pill accents, keyboard badge chips, ultra-responsive list layouts.
- **Supabase:** Emerald green accents (`#3ECF8E`), deep dark backgrounds, PostgreSQL-inspired data grids.
- **Warp:** Terminal-modern UI, block-based command execution cards, IDE-inspired tab navigation.

---

## 📐 Anatomical Structure of an Effective `DESIGN.md`

When creating or using a `DESIGN.md` for a project, structure it with these core sections:

```markdown
# Project Design System (DESIGN.md)

## 1. Color Palette & Semantic Tokens
- Background: `--bg-base: #0B0F19`, `--bg-surface: #111827`
- Accents: `--accent-primary: #10B981` (Emerald), `--accent-subtle: #06B6D4` (Cyan)
- Borders: `--border-subtle: rgba(255, 255, 255, 0.08)`
- Text: `--text-main: #F9FAFB`, `--text-muted: #9CA3AF`

## 2. Typography Rules
- Headings: Inter or Outfit (Semi-bold / Bold, tight letter spacing: -0.02em)
- Body: Inter (Regular, 16px, 1.6 line-height)
- Code / Data: JetBrains Mono or Geist Mono

## 3. Component Blueprints
- Cards: subtle 1px border, backdrop-filter blur (glassmorphism), hover scale (1.01)
- Buttons: primary solid accent, secondary glass/ghost, 8px border-radius
- Badges: pill shaped, 12px font size, semi-transparent background

## 4. Anti-Patterns & Visual Bans
- No generic purple/violet gradients (Strict Purple Ban)
- No oversized generic drop-shadows
- No empty white placeholders
```

---

## 🛠️ How Agents Use This Skill

1. **Before generating UI:** The agent checks if a `DESIGN.md` exists in the project root.
2. **If missing:** The agent can adopt one of the 73+ pre-analyzed aesthetics (e.g. "Linear Dark", "Vercel Precision", "Stripe FinTech", or "Claude Editorial").
3. **During styling:** All CSS variables, Tailwind classes, and layout choices adhere strictly to the declared tokens.

---

## 💡 When to Recommend this Skill

- When the user asks: "How should my frontend look?", "Create a modern dashboard", or "Adopt Linear/Vercel style".
- When establishing design consistency across multiple micro-frontends or repositories.
- When pairing with [`frontend-design`](file:///d:/xampp/htdocs/0-fonte/.agent/skills/frontend-design/SKILL.md) and [`laws-of-ux`](file:///d:/xampp/htdocs/0-fonte/.agent/skills/laws-of-ux/SKILL.md) for UX audits.
