import os
import re

def find_broken_links(root_dir):
    pattern = re.compile(r'\[.*?\]\((.*?)\)')
    broken = []
    
    for dirpath, _, filenames in os.walk(root_dir):
        for f in filenames:
            if not f.endswith('.md'): continue
            path = os.path.join(dirpath, f)
            try:
                with open(path, 'r', encoding='utf-8', errors='replace') as file:
                    content = file.read()
                    
                for match in pattern.findall(content):
                    link = match.split('#')[0] # remove fragment
                    if not link or link.startswith('http') or link.startswith('mailto:'): continue
                    if link.startswith('@'): continue # skip mentions
                    
                    target = os.path.normpath(os.path.join(dirpath, link))
                    if not os.path.exists(target):
                        broken.append((path, link))
            except Exception as e:
                pass
                    
    for path, link in broken:
        print(f"BROKEN: {path} -> {link}")
    
    print(f"Total broken: {len(broken)}")

find_broken_links('.agent')
