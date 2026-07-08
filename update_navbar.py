import glob
import re

html_files = glob.glob('*.html')
count = 0

pattern = r'<a id="pricing-nav" class="nav-tab" href="pricing\.html" title="Pricing">Pricing</a>\s*<a id="blog-nav" class="nav-tab" href="blogs\.html" title="Blog">Blog</a>\s*<a id="testimonials-nav" class="nav-tab" href="testimonials\.html" title="Testimonials">Testimonials</a>'

replacement = '<a id="demo-nav" class="nav-tab" href="https://demo.streamplay.ai/" title="Demo">Demo</a>\n                        <a id="blog-nav" class="nav-tab" href="https://streamplay.ai/blogs" title="Blog">Blog</a>'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if re.search(pattern, content):
        content = re.sub(pattern, replacement, content)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f'Updated {file}')

print(f'Total updated: {count}')
