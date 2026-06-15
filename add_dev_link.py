import glob

html_files = glob.glob('*.html')

for filename in html_files:
    if filename == 'developers.html':
        continue # Already added in the template
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Find the resources list in the footer
    if '<li><a href="pricing.html">Pricing</a></li>' in content and '<li><a href="developers.html">Developer API</a></li>' not in content:
        new_content = content.replace(
            '<li><a href="pricing.html">Pricing</a></li>',
            '<li><a href="pricing.html">Pricing</a></li>\n                        <li><a href="developers.html">Developer API</a></li>'
        )
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Added Developer API link to {filename}")
