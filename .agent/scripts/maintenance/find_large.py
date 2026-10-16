import os

for root, _, files in os.walk(r'd:\xampp\htdocs\0-fonte\.agent\skills'):
    for file in files:
        if file == 'SKILL.md':
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
                if len(lines) > 250:
                    print(f"{path}: {len(lines)} lines")
