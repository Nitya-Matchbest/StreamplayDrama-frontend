import glob
import re

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    def replace_navbar_style(match):
        full_tag = match.group(0)
        # Remove height="180" or height="45" and style="width: auto;"
        new_tag = re.sub(r'\s*height=\"\d+\"\s*', ' ', full_tag)
        new_tag = new_tag.replace('style="width: auto;"', 'style="height: 45px; width: auto;"')
        # Just in case there is no style tag yet
        if 'style=' not in new_tag:
            new_tag = new_tag.replace('class="fixed-logo"', 'style="height: 45px; width: auto;" class="fixed-logo"')
        return new_tag
        
    new_text = re.sub(r'<img[^>]*class=\"fixed-logo\"[^>]*>', replace_navbar_style, text)
    
    if new_text != text:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_text)
        print(f'Updated {file}')
