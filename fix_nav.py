import re
import os

files = ['index.html', 'pricing.html', 'testimonials.html', 'blogs.html', 'blog-detail.html', 'contact.html', 'features.html', 'demo.html', 'usecase-kdrama.html', 'usecase-turkish.html', 'usecase-arabic.html', 'usecase-indie.html']

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content.replace('Features ▾', 'Features')
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated text in {filename}')

# Fix CSS
css_path = r'c:\Users\GCV\Desktop\drama-frontend\assets\css\style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()
css = css.replace('.nav-dropdown {\n    position: relative;\n    display: inline-block;\n}', 
                  '.nav-dropdown {\n    position: relative;\n    display: flex;\n    align-items: center;\n}')
with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print('Updated CSS')
