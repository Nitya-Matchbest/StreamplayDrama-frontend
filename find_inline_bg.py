import glob
import re

for html_file in glob.glob('*.html'):
    with open(html_file, 'r', encoding='utf-8') as f:
        text = f.read()
        matches = re.finditer(r'style="[^"]*background[^"]*url\([^)]+\)[^"]*"', text)
        for m in matches:
            print(f'{html_file}: {m.group(0)}')
