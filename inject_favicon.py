import glob
import re

files = ['blog-detail.html', 'blogs.html', 'contact.html', 'testimonials.html']
for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<link rel="icon"' not in content:
        # Find the <title> tag and insert the link after it
        new_tag = '\n    <link rel="icon" href="assets/images/new-logo-transparent.png" type="image/x-icon">'
        content = re.sub(r'(<title>.*?</title>)', r'\1' + new_tag, content)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Injected into', filename)
