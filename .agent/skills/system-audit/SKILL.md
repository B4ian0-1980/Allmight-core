---
name: system-audit
description: Comprehensive checklists and methodology for software system auditing, diagnostics, and verification. Based on universal auditing standards and security best practices.
---

# System Audit - Methodology & Checklists

This skill provides the structured checklists and diagnostic patterns used by the `auditor-specialist` and other agents to verify system integrity.

## 1. Stack & Structure Diagnostics

### 1.1 Identification Checklist
- [ ] **Language**: `package.json`, `composer.json`, `requirements.txt`, `pom.xml`.
- [ ] **Framework**: `react`, `vue`, `laravel`, `django`, `fastapi`, `next.js`.
- [ ] **Database**: `.env`, `docker-compose`, ORM config.
- [ ] **Architecture**: `MVC`, `Modular`, `Clean`, `Hexagonal`.

### 1.2 Structure Patterns
- **Backend**: `models/`, `controllers/`, `services/`, `repositories/`, `middlewares/`.
- **Frontend**: `components/`, `pages/`, `store/`, `hooks/`, `assets/`.

## 2. Security Audit (The "Zero-Trust" Checklist)

### 2.1 Authentication & Authz
- [ ] **Hashing**: Using Argon2id or BCrypt (cost >= 12)?
- [ ] **MFA**: Implemented for critical actions?
- [ ] **JWT**: Correct expiration and secret handling?
- [ ] **RBAC**: Access check in EVERY controller/endpoint?

### 2.2 OWASP Top 10 Verification
- **Injection**: Search for string concatenation in queries: `grep -r ".*'.*req\.body.*"`.
- **XSS**: Check for `innerHTML`, `v-html`, or dangerouslySetInnerHTML.
- **CSRF**: Check for CSRF tokens in forms and same-site cookies.
- **Broken Access**: Check if `userId` is taken from session, not from body/query (IDOR).

## 3. Performance & Quality

### 3.1 Backend Efficiency
- [ ] **N+1 Queries**: Look for loops with database calls inside.
- [ ] **Missing Indexes**: Check foreign keys and search fields in migration files.
- [ ] **Large Payloads**: Check for `SELECT *` in large tables.

### 3.2 Frontend Vitals
- [ ] **Bundle Size**: Look for large dependencies (moment, lodash without tree-shaking).
- [ ] **Lazy Loading**: Are routes and heavy components lazy-loaded?

## 4. Reporting Template

Use this format for audit reports:

```markdown
# 📊 SYSTEM AUDIT REPORT: [Project Name]

## 1. Executive Summary
- **Status**: [🔴 CRITICAL / 🟠 WARNING / 🟢 STABLE]
- **Vulnerabilities**: [Critical: N, High: N, Med: N, Low: N]
- **Main Findings**: [Brief summary]

## 2. Detailed Findings

### ✅ [Phase Name]
- **Found**: ...
- **Status**: ✅ OK

### ❌ [Phase Name]
- **Issue**: [Description]
- **Impact**: [High/Medium/Low]
- **File**: `[path]`
- **Fix**:
  ```[lang]
  [code]
  ```

## 3. Prioritized Remediation Plan
1. **P0 (Immediate)**: [Critical Security Fixes]
2. **P1 (Next 24h)**: [High Impact Issues]
3. **P2 (Maintenance)**: [Optimization & Docs]
```

## 5. Diagnostic Commands (Windows/Powershell)

- **Find hardcoded secrets**: `grep -r "key|password|secret|token" .`
- **Check for SQLi patterns**: `grep -r "execute.*$.*" .`
- **Map structure**: `tree /f /a | select -first 100`
