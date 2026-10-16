---
name: laws-of-ux
description: "Psychology-based design principles, cognitive heuristics, diagnostic decision trees, and usability laws (Jon Yablonski, Laws of UX 2nd ed. O'Reilly 2024). Guides UI design, accessibility, progressive disclosure, touch targets, and UX audits."
metadata:
  version: 2.0.0
upstream_source: https://github.com/keysjoao/laws-of-ux-skills
last_updated: 2026-10-10
---

# Laws of UX — Cognitive & Psychological Design System

Apply cognitive psychology and behavioral science to interface design. Grounded in Jon Yablonski's *Laws of UX* (O'Reilly 2024), Gestalt visual perception, and empirical human-computer interaction studies.

---

## 🧭 Diagnostic Decision Tree: Which Laws Apply?

Run this decision flow whenever designing or reviewing a screen:

```text
START: What are you designing or reviewing?
│
├─ 1. Navigation & Information Architecture
│  ├─ Confusing hierarchy? ────────────── Jakob's Law (use familiar mental models)
│  ├─ Too many menu items? ────────────── Hick's Law (reduce choices to 5-7 max)
│  └─ Hard to scan? ───────────────────── Miller's Law (chunk into visual groups)
│
├─ 2. Interactive Elements (Buttons, Forms, Targets)
│  ├─ Targets too small/tight? ────────── Fitts's Law (min 44x44px CSS / 48x48dp)
│  ├─ Form validation rigid/annoying? ─── Postel's Law (accept variable inputs)
│  ├─ Too many form fields? ───────────── Hick's Law + Tesler's Law (progressive disclosure)
│  └─ Primary CTA doesn't stand out? ──── Von Restorff Effect (isolated high-contrast)
│
├─ 3. Performance, Loading & Feedback
│  ├─ Slow response / no loading state? ─ Doherty Threshold (feedback < 400ms)
│  ├─ Users abandoning mid-flow? ──────── Peak-End Rule (celebrate completion, cushion errors)
│  └─ Complex steep learning curve? ───── Tesler's Law (system absorbs complexity)
│
└─ 4. Visual Design & Layout
   ├─ Monotonous, flat layout? ────────── Von Restorff (create intentional visual hierarchy)
   ├─ Interface feels "clunky"? ───────── Aesthetic-Usability Effect (50ms visual polish)
   └─ Wall of unstructured text? ──────── Miller's Law + Gestalt Proximity
```

---

## 📏 Core UX Laws & Engineering Thresholds

| Lei | Princípio Central | Threshold Numérico | Aplicação Prática no Código |
| :--- | :--- | :--- | :--- |
| **Fitts's Law** | Tempo até o alvo = $f(\text{distância}, \text{tamanho})$ | **44x44px** (Apple) / **48x48dp** (Material) / **8dp** espaçamento | Touch targets mínimos; botões principais em zonas de fácil alcance; labels com `htmlFor` clicáveis. |
| **Hick's Law** | Tempo de decisão aumenta com número e complexidade | **3 a 5 opções** por grupo | Menus enxutos; Progressive Disclosure (mostrar o avançado sob demanda); destacar opção recomendada. |
| **Miller's Law** | Memória de trabalho retém $\sim 4$ blocos ativos | **4 a 7 chunks** visuais | Agrupar formulários em seções (`Dados`, `Endereço`, `Pagamento`); formatar telefones/CPFs com máscaras legíveis. |
| **Doherty Threshold** | Produtividade decola com resposta $< 400\text{ms}$ | **$< 100\text{ms}$** (instantâneo), **$< 400\text{ms}$** (transição), **$> 1\text{s}$** (skeleton/progress) | Feedback tátil/visual imediato; Skeleton screens para carregamento; Optimistic UI em mutações. |
| **Jakob's Law** | Usuários esperam que seu app funcione como outros | **100% familiaridade** em padrões universais | Carrinho no topo direito, logo volta para home, busca visível, ícones canônicos. |
| **Von Restorff** | O item que destoa visualmente é o mais lembrado | **Apenas 1 CTA primário** de destaque por viewport | Botão primário com cor de ação e contraste $\ge 4.5:1$ (WCAG); ações secundárias em estilo ghost/outline. |
| **Postel's Law** | Aceite entradas flexíveis, produza saídas confiáveis | **Tolerância total** de formatos | Aceitar telefones com/sem traço, converter maiúsculas/minúsculas, mensagens de erro humanas e orientativas. |
| **Peak-End Rule** | A experiência é julgada pelo pico e pelo desfecho | **Final memorável** em 100% dos fluxos | Telas de sucesso com feedback positivo (ex: confete, check verde claro); tratativa cordial de erro 404/vazio. |
| **Tesler's Law** | A complexidade não é eliminada, apenas transferida | **Transferir para o sistema** | Autopreenchimento de CEP, seleção inteligente de defaults, mantendo override manual para power-users. |
| **Aesthetic-Usability**| Interfaces polidas são percebidas como mais fáceis | **50ms** para formar a 1ª impressão | Tipografia equilibrada, sombras suaves, microinterações fluidas e paleta de cores consistente. |

---

## 💻 Padrões de Código para Frontend

### 1. Touch Targets & Espaçamento (Fitts's Law)
```css
/* Botões e alvos interativos */
.btn, .nav-item, [role="button"] {
  min-height: 44px;
  min-width: 44px;
  padding: 12px 16px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

/* Espaçamento mínimo entre alvos adjacentes */
.action-group > * + * {
  margin-left: 8px; /* Previne mis-clicks */
}

/* Labels expandem a área de clique */
label {
  cursor: pointer;
  display: inline-block;
  padding: 4px 0;
}
```

### 2. Progressive Disclosure (Hick's Law + Tesler's Law)
```tsx
// Nível 1: Visão inicial limpa (redução de decisões)
// Nível 2: Expandido sob demanda
function SettingsSection() {
  const [showAdvanced, setShowAdvanced] = useState(false);
  return (
    <div className="space-y-4">
      <BasicPreferences />
      <button 
        type="button" 
        onClick={() => setShowAdvanced(!showAdvanced)}
        className="text-sm font-medium text-blue-600 hover:underline"
      >
        {showAdvanced ? "▲ Menos opções" : "▼ Opções avançadas"}
      </button>
      {showAdvanced && <AdvancedSettings />}
    </div>
  );
}
```

### 3. Estados de Resposta (Doherty Threshold)
```tsx
// Feedback instantâneo com Skeleton Screen
function DataCard({ isLoading, data }) {
  if (isLoading) {
    return <div className="animate-pulse bg-gray-200 dark:bg-gray-800 rounded-lg h-32 w-full" />;
  }
  return <div className="rounded-lg p-4 bg-white dark:bg-gray-900 border">{data.content}</div>;
}
```

---

## ✅ Pre-Ship UX Audit Checklist

Antes de aprovar ou entregar qualquer tela, execute este checklist:

- [ ] **Alvos de Toque (Fitts):** Todos os botões, links e inputs têm pelo menos 44x44px de área clicável com 8px de espaçamento?
- [ ] **Redução de Escolhas (Hick):** A tela apresenta no máximo 3–5 opções primárias simultâneas?
- [ ] **Agrupamento (Miller):** Formulários e dados densos estão divididos em seções visuais claras (*chunks*)?
- [ ] **Feedback Rápido (Doherty):** Ações de clique têm feedback visual em $<400\text{ms}$ e skeletons para carregamento?
- [ ] **Entradas Flexíveis (Postel):** Formulários aceitam dados com espaços/pontuação sem travar o usuário?
- [ ] **Hierarquia Visual (Von Restorff):** Existe apenas UM botão de ação primária destacado por viewport?
- [ ] **Familiaridade (Jakob):** A navegação e ícones seguem convenções já familiares ao usuário?
- [ ] **Desfecho Positivo (Peak-End):** O fluxo termina com uma confirmação clara e amigável de sucesso?
