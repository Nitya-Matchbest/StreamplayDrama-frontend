import re

def update_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    # Remove the old style block completely
    style_regex = r'<style>\s*details > summary::-webkit-details-marker.*?details\[open\] > div.*?overflow: hidden;.*?}</style>'
    text = re.sub(style_regex, '', text, flags=re.DOTALL)

    # Convert <details> to <div class="faq-card">
    text = re.sub(
        r'<details (style="[^"]*")>', 
        r'<div class="faq-card" \1>', 
        text
    )
    
    # Convert <summary> to <div class="faq-header">
    text = re.sub(
        r'<summary style="([^"]*)">', 
        r'<div class="faq-header" style="\1">', 
        text
    )
    
    # Convert </summary> to </div>
    text = re.sub(r'</summary>', r'</div>', text)
    
    # Convert </details> to </div>
    text = re.sub(r'</details>', r'</div>', text)
    
    # Convert the content div to have faq-body class
    text = re.sub(
        r'<div style="padding: 0 30px 24px; color: #9CA3AF;([^"]*)">',
        r'<div class="faq-body" style="padding: 0 30px 24px; color: #9CA3AF;\1; display: none;">',
        text
    )
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
    print('Updated', filename)

update_file('index.html')
update_file('pricing.html')
