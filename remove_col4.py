import glob
import re
import os

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regex to match Col 4 and its entire div content
    # We use re.DOTALL to match across newlines
    pattern = r'(\s*<!-- Col 4: Contact Us & Status -->\s*<div class="footer-col">.*?<div class="platform-badges-row">.*?</div>\s*</div>\s*</div>)'
    
    if re.search(pattern, content, re.DOTALL):
        new_content = re.sub(pattern, '', content, flags=re.DOTALL)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Removed Col 4 from {file}")
    else:
        print(f"Col 4 not found in {file}")

