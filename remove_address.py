import re
import os

files = ['index.html', 'pricing.html', 'testimonials.html', 'blogs.html', 'blog-detail.html', 'contact.html']

pattern = re.compile(r'\s*<li>\s*<div class="contact-item">\s*<svg.*?<span class="info-label">HQ Address</span>.*?</li>', re.IGNORECASE | re.DOTALL)

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = pattern.sub('', content)
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated {filename}')
        else:
            print(f'No changes in {filename}')
