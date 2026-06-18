import os, re

files = [f for f in os.listdir('.') if f.endswith('.html')]

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
        
    original = text

    # Standardize footer-contact-info across all files
    # Match <ul class="footer-contact-info"> ... </ul> (could contain anything)
    text = re.sub(
        r'<ul\s+class=\"footer-contact-info\">.*?</ul>', 
        '<ul class=\"footer-contact-info\">\n                        <li><a href=\"contact.html\">Contact Us</a></li>\n                    </ul>', 
        text, 
        flags=re.DOTALL
    )

    if original != text:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f'Updated {file_path}')
