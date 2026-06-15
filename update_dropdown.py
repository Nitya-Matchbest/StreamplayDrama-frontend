import re
import os

files = ['index.html', 'pricing.html', 'testimonials.html', 'blogs.html', 'blog-detail.html', 'contact.html', 'features.html', 'demo.html']

dropdown_html = '''<div class="nav-dropdown">
                            <a id="features-nav" class="nav-tab" href="features.html" title="Features">Features ▾</a>
                            <div class="nav-dropdown-content">
                                <a href="features.html">All Features</a>
                                <a href="usecase-kdrama.html">K-Drama Platforms</a>
                                <a href="usecase-turkish.html">Turkish Platforms</a>
                                <a href="usecase-arabic.html">Arabic Platforms</a>
                                <a href="usecase-indie.html">Indie Platforms</a>
                            </div>
                        </div>'''

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace the <a id="features-nav"...>Features</a> with the dropdown_html
        # Notice we have to be careful about the "active" class
        # It's easier to just match <a id="features-nav" ...>Features</a>
        
        # Regex to match the features-nav anchor
        pattern = re.compile(r'<a\s+id="features-nav"[^>]*>Features</a>', re.IGNORECASE)
        
        if pattern.search(content):
            new_content = pattern.sub(dropdown_html, content)
            
            if new_content != content:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f'Updated {filename}')
        else:
            print(f'No features-nav link found in {filename}')
