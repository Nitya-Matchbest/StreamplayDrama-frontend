import glob
import re

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 1. Replace Pricing with Demo in navbar
    # Look for <a> tags with 'nav-tab' that link to pricing.html
    content = re.sub(
        r'<a([^>]*class="[^"]*nav-tab[^"]*"[^>]*)href="pricing\.html"([^>]*)>[^<]*Pricing[^<]*</a>',
        r'<a\1href="https://demo.streamplay.ai/"\2>Demo</a>',
        content, flags=re.IGNORECASE
    )
    # Also handle if title is Pricing
    content = re.sub(r'title="Pricing"', 'title="Demo"', content)
    
    # 2. Update Blog URL in navbar
    content = re.sub(
        r'<a([^>]*class="[^"]*nav-tab[^"]*"[^>]*)href="blogs\.html"([^>]*)>[^<]*Blog[^<]*</a>',
        r'<a\1href="https://streamplay.ai/blogs"\2>Blog</a>',
        content, flags=re.IGNORECASE
    )
    
    # 3. Remove Testimonials from navbar
    content = re.sub(
        r'\s*<a[^>]*class="[^"]*nav-tab[^"]*"[^>]*href="testimonials\.html"[^>]*>[^<]*Testimonials[^<]*</a>',
        '',
        content, flags=re.IGNORECASE
    )
    
    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated {file}')

