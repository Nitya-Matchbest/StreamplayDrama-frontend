import re
import os

files = ['index.html', 'pricing.html', 'testimonials.html', 'blogs.html', 'blog-detail.html', 'contact.html']

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        def repl(m):
            home_link = m.group(0)
            features_link = '\n                        <a id="features-nav" class="nav-tab" href="features.html" title="Features">Features</a>'
            return home_link + features_link

        if 'features.html' not in content:
            # We match the Home link inside the nav-center div.
            new_content = re.sub(r'(<a[^>]*href="index\.html"[^>]*>Home</a>)', repl, content, count=1)
            
            if new_content != content:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f'Updated {filename}')
            else:
                print(f'Regex failed for {filename}')
        else:
            print(f'features.html already in {filename}')
