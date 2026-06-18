import os

files = [f for f in os.listdir('.') if f.endswith('.html')]

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
        
    original = text

    text = text.replace('<ul class=\"footer-contact-info\">\n                    </ul>', '<ul class=\"footer-contact-info\">\n                        <li><a href=\"contact.html\">Contact Us</a></li>\n                    </ul>')

    if original != text:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f'Updated {file_path}')
