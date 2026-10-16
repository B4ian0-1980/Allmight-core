#!/usr/bin/env python3
"""
Claudex — Plan Cross-Examiner
==============================
Analyzes an architecture/implementation plan against the 3 Claudex lenses:
1. Senior Engineer (Complexity, YAGNI, Redundancy)
2. Security & Data Integrity (Secrets, Auth, Validation)
3. Ops & SRE (Rollback, Telemetry, Failure modes)
"""

import sys
import re
from pathlib import Path

if sys.stdout:
    sys.stdout.reconfigure(encoding="utf-8")

def analyze_plan(file_path: Path):
    if not file_path.exists():
        print(f"❌ Arquivo não encontrado: {file_path}")
        sys.exit(1)

    content = file_path.read_text(encoding="utf-8", errors="ignore")
    lines = content.splitlines()

    print(f"⚔️ Iniciando Sabatina Claudex: {file_path.name}")
    print(f"📊 Volume: {len(lines)} linhas | {len(content)} caracteres\n")

    # Lens 1: Senior Engineer Checks
    print("--- [Rodada 1] Engenheiro Sênior (Simplicidade & Arquitetura) ---")
    overkill_terms = ["microservices", "kafka", "event sourcing", "blockchain", "multithread"]
    overkill_found = [t for t in overkill_terms if t in content.lower()]
    if overkill_found:
        print(f"  ⚠️ Alerta de Complexidade: detectados termos que podem indicar over-engineering: {overkill_found}")
    else:
        print("  ✅ Complexidade arquitetural controlada. Nenhum sinal óbvio de over-engineering.")

    has_testing = any(t in content.lower() for t in ["test", "teste", "pytest", "unit", "e2e", "mock"])
    if has_testing:
        print("  ✅ Cobertura de testes e estratégia de validação identificada.")
    else:
        print("  ❌ CRÍTICA R1: O plano não menciona estratégia de testes ou critérios de aceitação.")

    # Lens 2: Security Checks
    print("\n--- [Rodada 2] Segurança & Integridade de Dados ---")
    has_secrets_handling = any(s in content.lower() for s in ["env", "secret", "token", "auth", "jwt", "sanitiz"])
    if has_secrets_handling:
        print("  ✅ Menção a autenticação, variáveis ou sanitização de entrada.")
    else:
        print("  ⚠️ ALERTA R2: O plano não especifica tratamento de dados sensíveis ou autenticação.")

    # Lens 3: Ops & SRE Checks
    print("\n--- [Rodada 3] Confiabilidade, DevOps & SRE ---")
    has_rollback = any(r in content.lower() for r in ["rollback", "fallback", "migra", "backup", "log"])
    if has_rollback:
        print("  ✅ Resiliência operacional ou estratégia de mitigação mencionada.")
    else:
        print("  ❌ CRÍTICA R3: Ausência de plano de reversão (rollback) ou monitoramento pós-deploy.")

    print("\n🏆 Resumo Claudex concluído. Aplique as correções necessárias para convergir.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python plan_cross_examiner.py <caminho_do_plano.md>")
        sys.exit(1)
    analyze_plan(Path(sys.argv[1]))
