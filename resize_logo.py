import glob
import re

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # We will look for <img height="250" ... class="fixed-logo" ...>
    # and replace height="250" with height="180"
    
    def replace_height(match):
        full_tag = match.group(0)
        return full_tag.replace('height="250"', 'height="180"')
        
    new_text = re.sub(r'<img\s+height="250"[^>]*class="fixed-logo"[^>]*>', replace_height, text)
    
    if new_text != text:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_text)
        print(f'Updated {file}')
