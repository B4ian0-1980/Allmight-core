#!/usr/bin/env python3
"""
Safety Gate — Antigravity Command Interceptor & Execution Guard
================================================================
Interprets stdin tool calls and inspects CommandLine against dangerous patterns
covering Unix, Windows PowerShell/CMD, Git, Cloud CLI, and Database operations.

Usage (Hook):
    python .agent/scripts/safety_gate.py < input.json
"""

import sys
import json
import re


DANGEROUS_PATTERNS = [
    # Unix Destructive
    (r"\brm\s+-(?:rf|fr)\b", "Exclusão recursiva forçada Unix (rm -rf)"),
    (r"\bmkfs\b", "Formatação de sistema de arquivos (mkfs)"),
    (r"\bdd\s+if=", "Sobrescrita direta de blocos (dd if=)"),

    # Windows / PowerShell Destructive
    (r"\bremove-item\b.*-(?:recurse|force).*", "Exclusão recursiva forçada PowerShell (Remove-Item)"),
    (r"\brd\s+/(?:s\s+/q|q\s+/s)\b", "Remoção de diretório recursivo CMD (rd /s /q)"),
    (r"\bdel\s+/(?:f\s+/s\s+/q|s\s+/q|q\s+/s)\b", "Exclusão forçada em lote CMD (del /f /s /q)"),
    (r"\bformat-volume\b", "Formatação de volume de disco (Format-Volume)"),
    (r"\bstop-computer\b", "Desligamento forçado de máquina (Stop-Computer)"),
    (r"\brestart-computer\b", "Reinicialização de máquina (Restart-Computer)"),
    (r"\bshutdown\s+/[srf]\b", "Desligamento / reinicialização CMD (shutdown)"),

    # Git Destructive
    (r"\bgit\s+push\b.*(?:\s+-f\b|\s+--force\b)", "Sobrescrita forçada de repositório remoto (git push --force)"),
    (r"\bgit\s+reset\s+--hard\b", "Descarte irreversível de alterações locais (git reset --hard)"),
    (r"\bgit\s+clean\s+-[a-zA-Z]*f[a-zA-Z]*\b", "Exclusão forçada de arquivos não rastreados (git clean -f)"),

    # Kubernetes & Containers
    (r"\bkubectl\s+delete\b", "Exclusão de recurso Kubernetes (kubectl delete)"),
    (r"\bhelm\s+uninstall\b", "Desinstalação de release Helm (helm uninstall)"),

    # Cloud Providers Destructive
    (r"\bgcloud\s+projects\s+delete\b", "Exclusão de projeto Google Cloud (gcloud projects delete)"),
    (r"\bgcloud\b.*(?:\s+delete\b)", "Exclusão de recurso GCP (gcloud delete)"),
    (r"\baws\s+s3\s+rb\b.*--force", "Exclusão forçada de bucket AWS S3"),
    (r"\baws\s+s3\s+rm\b.*--recursive", "Exclusão recursiva de bucket AWS S3"),
    (r"\baws\b.*(?:\s+delete-[a-zA-Z0-9\-]+)", "Exclusão de recurso AWS CLI"),
    (r"\baz\s+group\s+delete\b", "Exclusão de Resource Group Azure (az group delete)"),
    (r"\baz\b.*(?:\s+delete\b)", "Exclusão de recurso Azure CLI (az delete)"),

    # Database Destructive Operations
    (r"\bdrop\s+(?:table|database|schema|view)\b", "Comando destrutivo DDL (DROP TABLE/DATABASE)"),
    (r"\btruncate\s+(?:table\s+)?", "Esvaziamento de tabela (TRUNCATE TABLE)"),
    (r"\bdelete\s+from\s+[a-zA-Z0-9_.]+\s*(?:;\s*$|$)", "DELETE em tabela sem cláusula WHERE"),
]


def check_command(cmd: str):
    """Inspects command line string against regex rules."""
    norm_cmd = cmd.strip().lower()
    norm_cmd = re.sub(r'\s+', ' ', norm_cmd)

    for pattern, description in DANGEROUS_PATTERNS:
        if re.search(pattern, norm_cmd, re.IGNORECASE):
            return {
                "decision": "ask",
                "reason": f"Comando potencialmente destrutivo detectado: {description}. Requer confirmação humana explícita."
            }

    return {"decision": "allow"}


def main():
    try:
        if sys.stdin.isatty():
            # If run directly for testing without stdin pipe
            print(json.dumps({"decision": "allow"}))
            return

        input_data = json.load(sys.stdin)
        tool_call = input_data.get("toolCall", {})
        args = tool_call.get("args", {})
        cmd = args.get("CommandLine", "")

        result = check_command(cmd)
        print(json.dumps(result, ensure_ascii=False))

    except Exception:
        # Fallback to allow if parsing fails, so we don't break the agent pipeline
        print(json.dumps({"decision": "allow"}))


if __name__ == "__main__":
    main()
