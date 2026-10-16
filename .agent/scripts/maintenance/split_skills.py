import os

MAX_LINES = 250

for root, _, files in os.walk(r'd:\xampp\htdocs\0-fonte\.agent\skills'):
    if 'SKILL.md' in files:
        path = os.path.join(root, 'SKILL.md')
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            
        if len(lines) > MAX_LINES:
            # Find a safe split point (H2 or H3 after line 120)
            split_idx = -1
            for i in range(120, len(lines)):
                if lines[i].startswith('## ') or lines[i].startswith('### '):
                    split_idx = i
                    break
            
            if split_idx != -1 and len(lines) - split_idx > 50:
                print(f"Splitting {path} at line {split_idx}")
                
                # Create references dir
                ref_dir = os.path.join(root, 'references')
                os.makedirs(ref_dir, exist_ok=True)
                
                ref_path = os.path.join(ref_dir, 'reference.md')
                
                # Write reference.md
                with open(ref_path, 'w', encoding='utf-8') as rf:
                    rf.writelines(lines[split_idx:])
                    
                # Write new SKILL.md
                new_skill_content = lines[:split_idx]
                new_skill_content.append('\n---\n\n## 📚 Deep Reference (Progressive Disclosure)\n\n')
                new_skill_content.append('> ⚠️ **CONTEXT OPTIMIZATION:** The detailed methodology, edge cases, attack vectors, and advanced configurations for this skill are stored externally to save tokens.\n\n')
                new_skill_content.append('To access the full technical reference, you MUST use your iew_file tool to read:\n\n')
                new_skill_content.append(f'{ref_path}\n')
                
                with open(path, 'w', encoding='utf-8') as sf:
                    sf.writelines(new_skill_content)
