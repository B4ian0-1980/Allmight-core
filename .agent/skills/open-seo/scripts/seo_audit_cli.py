#!/usr/bin/env python3
"""
OpenSEO — Technical SEO Audit CLI
=================================
Performs instant technical SEO analysis on local HTML files or live URLs:
- Title tag presence & length (50-60 chars)
- Meta description presence & length (120-160 chars)
- Single H1 heading verification
- Canonical tag & OpenGraph tags
- Image alt attribute coverage
"""

import sys
import re
import urllib.request
from pathlib import Path

if sys.stdout:
    sys.stdout.reconfigure(encoding="utf-8")

def fetch_content(target: str) -> str:
    if target.startswith("http://") or target.startswith("https://"):
        req = urllib.request.Request(target, headers={"User-Agent": "OpenSEO-Auditor/1.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.read().decode("utf-8", errors="replace")
    else:
        p = Path(target)
        if not p.exists():
            print(f"❌ Arquivo não encontrado: {target}")
            sys.exit(1)
        return p.read_text(encoding="utf-8", errors="ignore")

def audit_seo(target: str):
    print(f"🔍 Executando Auditoria OpenSEO em: {target}")
    html = fetch_content(target)

    # 1. Title tag
    title_match = re.search(r"<title[^>]*>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    if title_match:
        title = title_match.group(1).strip()
        t_len = len(title)
        status = "✅" if 30 <= t_len <= 65 else "⚠️"
        print(f"  {status} Title: \"{title}\" ({t_len} caracteres - ideal: 50-60)")
    else:
        print("  ❌ Title tag AUSENTE no documento!")

    # 2. Meta description
    meta_desc = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', html, re.IGNORECASE)
    if not meta_desc:
        meta_desc = re.search(r'<meta[^>]*content=["\']([^"\']*)["\'][^>]*name=["\']description["\']', html, re.IGNORECASE)

    if meta_desc:
        desc = meta_desc.group(1).strip()
        d_len = len(desc)
        status = "✅" if 110 <= d_len <= 165 else "⚠️"
        print(f"  {status} Meta Description: \"{desc[:60]}...\" ({d_len} caracteres - ideal: 120-160)")
    else:
        print("  ❌ Meta description AUSENTE!")

    # 3. H1 Headings
    h1_matches = re.findall(r"<h1[^>]*>(.*?)</h1>", html, re.IGNORECASE | re.DOTALL)
    if len(h1_matches) == 1:
        print(f"  ✅ H1 único identificado: \"{re.sub(r'<[^>]+>', '', h1_matches[0]).strip()}\"")
    elif len(h1_matches) == 0:
        print("  ❌ Nenhum <h1> encontrado na página!")
    else:
        print(f"  ⚠️ Múltiplos <h1> detectados ({len(h1_matches)} encontrados). Ideal é exatamente 1.")

    # 4. Canonical
    canonical = re.search(r'<link[^>]*rel=["\']canonical["\'][^>]*href=["\']([^"\']*)["\']', html, re.IGNORECASE)
    if canonical:
        print(f"  ✅ Tag Canonical: {canonical.group(1)}")
    else:
        print("  ⚠️ Tag Canonical ausente (recomendada para evitar duplicação).")

    # 5. OpenGraph
    has_og = "og:title" in html or "og:description" in html
    print(f"  {'✅' if has_og else '⚠️'} OpenGraph (Social Tags): {'Presentes' if has_og else 'Ausentes'}")

    # 6. Images Alt
    images = re.findall(r"<img[^>]*>", html, re.IGNORECASE)
    if images:
        missing_alt = [img for img in images if 'alt=' not in img.lower()]
        if not missing_alt:
            print(f"  ✅ Todas as {len(images)} imagens possuem atributo alt.")
        else:
            print(f"  ⚠️ {len(missing_alt)} de {len(images)} imagens NÃO possuem atributo alt.")

    print("\n🏁 Auditoria OpenSEO finalizada.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python seo_audit_cli.py <url_ou_arquivo.html>")
        sys.exit(1)
    audit_seo(sys.argv[1])
