import glob
import re

html_files = glob.glob('*.html')
count = 0

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 1. Update Demo link to include target="_blank"
    content = re.sub(
        r'(<a[^>]*href="https://demo\.streamplay\.ai/"[^>]*)>',
        lambda m: m.group(1) + ' target="_blank">' if 'target=' not in m.group(1) else m.group(0),
        content, flags=re.IGNORECASE
    )
    
    # 2. Update Blog link to include target="_blank"
    content = re.sub(
        r'(<a[^>]*href="https://streamplay\.ai/blogs"[^>]*)>',
        lambda m: m.group(1) + ' target="_blank">' if 'target=' not in m.group(1) else m.group(0),
        content, flags=re.IGNORECASE
    )
    
    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f'Updated {file}')

print(f'Total updated: {count}')
