import glob
import re

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # 1. Decrease navbar logo from 180 to 45
    def replace_navbar_height(match):
        full_tag = match.group(0)
        return full_tag.replace('height="180"', 'height="45"')
        
    new_text = re.sub(r'<img\s+height="180"[^>]*class="fixed-logo"[^>]*>', replace_navbar_height, text)
    
    # 2. Decrease footer logo from 110px to 50px
    def replace_footer_height(match):
        full_tag = match.group(0)
        return full_tag.replace('height: 110px;', 'height: 50px;')
        
    new_text = re.sub(r'<img[^>]*class="footer-logo"[^>]*>', replace_footer_height, new_text)
    
    if new_text != text:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_text)
        print(f'Updated {file}')
