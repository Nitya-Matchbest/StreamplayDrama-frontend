import glob
import re

html_files = glob.glob('*.html')
count = 0

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 1. Replace Pricing with Demo
    content = re.sub(r'<a id="pricing-nav"[^>]*>Pricing</a>', r'<a id="demo-nav" class="nav-tab" href="https://demo.streamplay.ai/" title="Demo">Demo</a>', content)
    
    # 2. Update Blog URL
    content = re.sub(r'<a id="blog-nav"[^>]*>Blog</a>', r'<a id="blog-nav" class="nav-tab" href="https://streamplay.ai/blogs" title="Blog">Blog</a>', content)
    
    # 3. Remove Testimonials
    content = re.sub(r'\s*<a id="testimonials-nav"[^>]*>Testimonials</a>', '', content)
    
    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f'Updated {file}')

print(f'Total updated: {count}')
