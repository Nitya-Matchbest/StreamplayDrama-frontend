import glob
import re

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    matches = re.finditer(r'<img[^>]*src="[^"]*"[^>]*>', text)
    for m in matches:
        if 'logo' in m.group(0).lower():
            print(f'{file}: {m.group(0)}')
