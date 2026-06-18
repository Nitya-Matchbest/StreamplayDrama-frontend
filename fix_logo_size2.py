import os

files = [f for f in os.listdir('.') if f.endswith('.html')]

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
        
    original = text

    # Update navbar logo size
    text = text.replace(
        '<img height="120" style="width: auto;" src="assets/images/new-logo-transparent.png" class="fixed-logo"',
        '<img height="150" style="width: auto;" src="assets/images/new-logo-transparent.png" class="fixed-logo"'
    )

    # Update footer logo size
    text = text.replace(
        '<img style="height: 90px; width: auto; vertical-align: middle; margin-top: 5px;" src="assets/images/new-logo-transparent.png" alt="StreamPlay Drama Logo" class="footer-logo">',
        '<img style="height: 110px; width: auto; vertical-align: middle; margin-top: 5px;" src="assets/images/new-logo-transparent.png" alt="StreamPlay Drama Logo" class="footer-logo">'
    )

    if original != text:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f'Updated {file_path}')
