import os
import re

files = []
for root, dirs, f in os.walk('.'):
    for file in f:
        if file.endswith('.css') or file.endswith('.html'):
            if 'node_modules' not in root and '.git' not in root:
                files.append(os.path.join(root, file))

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content

    # Background replacements
    content = content.replace('background-color: #07070B', 'background-color: var(--background)')
    content = content.replace('background-color: #0D0D1A', 'background-color: var(--background)')
    content = content.replace('content="#0D0D1A"', 'content="#010F29"')
    content = content.replace('content="#07070B"', 'content="#010F29"')
    
    # Pricing button replacement (from previous turn)
    content = content.replace('#8A0000', 'var(--btn-grad-2)')

    # Button gradient replacements
    content = re.sub(r'linear-gradient\([^)]*var\(--primary\)[^)]*var\(--accent\)[^)]*\)', 'linear-gradient(90deg, var(--btn-grad-1) 0%, var(--btn-grad-2) 100%)', content)
    content = re.sub(r'linear-gradient\([^)]*var\(--accent\)[^)]*var\(--primary\)[^)]*\)', 'linear-gradient(90deg, var(--btn-grad-2) 0%, var(--btn-grad-1) 100%)', content)

    # Some cards have border-color: #A30000 or rgba(163, 0, 0) (which is the red primary). We should map them to primary hover or border
    content = content.replace('#A30000', 'var(--primary-hover)')
    content = content.replace('rgba(163, 0, 0', 'rgba(130, 42, 238')

    # Replace manual inline style text colors if any (like the #FF0000 youtube icon, #0a66c2 linkedin)
    # Wait, user said "tex tex which is red and yellow should be changed to text color : #822AEE and white text should remain white only"
    # YouTube should stay YouTube color. But any inline red text...
    content = content.replace('color: #FF5252', 'color: var(--primary)')
    
    if original != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated {file_path}')
