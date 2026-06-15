import re
import os

files = ['index.html', 'pricing.html', 'testimonials.html', 'blogs.html', 'blog-detail.html', 'contact.html', 'features.html']

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        def repl(m):
            home_link = m.group(0)
            features_link = '\n                        <li><a href="features.html">Features</a></li>'
            return home_link + features_link

        new_content = re.sub(r'(<li><a href="index\.html">Home</a></li>)', repl, content, count=1)
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated footer in {filename}')
