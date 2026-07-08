import glob
import re

html_files = glob.glob('*.html')
count = 0

def replace_a_tag(match):
    a_tag = match.group(0)
    open_tag = match.group(1)
    inner_html = match.group(2)
    close_tag = match.group(3)
    
    # Remove HTML tags to get pure text
    text_content = re.sub(r'<[^>]+>', '', inner_html).strip()
    text_content = re.sub(r'\s+', ' ', text_content)
    
    if text_content.lower() in ['watch demo', 'request demo', 'request custom demo']:
        # Update href
        if 'href="' in open_tag:
            open_tag = re.sub(r'href="[^"]*"', 'href="https://demo.streamplay.ai/"', open_tag)
        else:
            open_tag = open_tag.replace('<a ', '<a href="https://demo.streamplay.ai/" ')
            
        # Update target
        if 'target="' not in open_tag:
            open_tag = open_tag.replace('<a ', '<a target="_blank" ')
            
        return open_tag + inner_html + close_tag
        
    return a_tag

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    content = re.sub(r'(<a\s[^>]*>)(.*?)(</a>)', replace_a_tag, content, flags=re.IGNORECASE | re.DOTALL)
    
    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f'Updated {file}')

print(f'Total updated: {count}')
