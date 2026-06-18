import os, re

files = [f for f in os.listdir('.') if f.endswith('.html')]

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
        
    original = text

    # We want to replace an empty or nearly empty footer-contact-info with the new one
    # Use re.sub to match <ul class="footer-contact-info">\s*</ul>
    text = re.sub(r'<ul\s+class=\"footer-contact-info\">\s*</ul>', '<ul class=\"footer-contact-info\">\n                        <li><a href=\"contact.html\">Contact Us</a></li>\n                    </ul>', text)

    if original != text:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f'Updated {file_path}')
