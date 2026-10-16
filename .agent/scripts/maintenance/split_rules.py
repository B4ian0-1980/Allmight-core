import os

with open(r'd:\xampp\htdocs\0-fonte\.agent\rules\GEMINI.md', 'r', encoding='utf-8') as f:
    content = f.read()

def extract_section(start_marker, end_marker=None):
    start_idx = content.find(start_marker)
    if start_idx == -1: return ""
    if end_marker:
        end_idx = content.find(end_marker, start_idx)
        if end_idx == -1: return content[start_idx:]
        return content[start_idx:end_idx].strip()
    return content[start_idx:].strip()

core_part = content[:content.find('## 📥 REQUEST CLASSIFIER')] + extract_section('### 🗺️ System Map Read', '### 🧹 Clean Code')

routing_part = "---\ntrigger: always_on\n---\n\n# Intelligent Routing Rules\n\n" + extract_section('## 📥 REQUEST CLASSIFIER', '## TIER 0: UNIVERSAL RULES')

standards_part = "---\ntrigger: always_on\n---\n\n# Universal Coding Standards\n\n" + extract_section('### 🧹 Clean Code', '## TIER 1: CODE RULES')

execution_part = "---\ntrigger: always_on\n---\n\n# Execution and Tooling Protocols\n\n" + extract_section('## TIER 1: CODE RULES')

with open(r'd:\xampp\htdocs\0-fonte\.agent\rules\GEMINI.md', 'w', encoding='utf-8') as f:
    f.write(core_part)

with open(r'd:\xampp\htdocs\0-fonte\.agent\rules\01_routing.md', 'w', encoding='utf-8') as f:
    f.write(routing_part)

with open(r'd:\xampp\htdocs\0-fonte\.agent\rules\02_coding_standards.md', 'w', encoding='utf-8') as f:
    f.write(standards_part)

with open(r'd:\xampp\htdocs\0-fonte\.agent\rules\03_execution_protocols.md', 'w', encoding='utf-8') as f:
    f.write(execution_part)

print("Modularization complete.")
