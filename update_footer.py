import glob
import re

html_files = glob.glob('*.html')
count = 0

new_resources_block = '''                <!-- Col 3: Resources -->
                <div class="footer-col">
                    <h4>Resources</h4>
                    <ul class="footer-links">
                        <li><a href="index.html">Home</a></li>
                        <li><a href="features.html">Features</a></li>
                        <li><a href="https://demo.streamplay.ai/" target="_blank">Demo</a></li>
                        <li><a href="https://streamplay.ai/blogs" target="_blank">Blog</a></li>
                        <li><a href="developers.html">Developer API</a></li>
                        <li><a href="contact.html">Contact Sales</a></li>
                    </ul>
                </div>'''

# Regex to match the resources column
# We match <!-- Col 3: Resources --> up to the next </div> that closes the footer-col
pattern = re.compile(r'<!--\s*Col 3: Resources\s*-->\s*<div class="footer-col">\s*<h4>Resources</h4>\s*<ul class="footer-links">.*?</ul>\s*</div>', re.DOTALL | re.IGNORECASE)

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if pattern.search(content):
        new_content = pattern.sub(new_resources_block, content)
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
            print(f'Updated {file}')

print(f'Total updated: {count}')
