import glob
import re

html_files = glob.glob('*.html')
count = 0

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    # Look for <link rel="icon" href="assets/images/9 1.png" type="image/x-icon">
    # Replace href with Frame 1116606591.png
    content = re.sub(
        r'<link\s+rel="icon"\s+href="[^"]*"\s+type="image/x-icon"\s*>',
        r'<link rel="icon" href="assets/images/Frame%201116606591.png" type="image/x-icon">',
        content, flags=re.IGNORECASE
    )
    
    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f'Updated {file}')

print(f'Total updated: {count}')
