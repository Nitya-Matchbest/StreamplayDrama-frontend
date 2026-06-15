import re
import os

files = ['index.html', 'pricing.html', 'testimonials.html', 'blogs.html', 'blog-detail.html', 'contact.html', 'features.html']

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace the Request Demo button
        # Original: <a rel="nofollow" id="sales-header" href="contact.html" title="Request Demo">Request Demo</a>
        # New:      <a rel="nofollow" id="sales-header" href="demo.html" title="Watch Demo">Watch Demo</a>
        
        new_content = re.sub(
            r'<a\s+rel="nofollow"\s+id="sales-header"\s+href="contact\.html"\s+title="Request Demo"\s*>Request Demo</a>',
            '<a rel="nofollow" id="sales-header" href="demo.html" title="Watch Demo">Watch Demo</a>',
            content
        )
        
        # In case the title is not exactly "Request Demo" or there's no title:
        new_content = re.sub(
            r'<a\s+rel="nofollow"\s+id="sales-header"\s+href="contact\.html"[^>]*>Request Demo</a>',
            '<a rel="nofollow" id="sales-header" href="demo.html" title="Watch Demo">Watch Demo</a>',
            new_content
        )
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated {filename}')
        else:
            print(f'No changes in {filename}')
