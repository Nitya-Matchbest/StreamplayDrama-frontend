import glob
import re

html_files = glob.glob('*.html')

for filename in html_files:
    if filename == 'developers.html':
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check if developer API is already in there
    if 'developers.html' in content and '>Developer API<' in content:
        continue
        
    # Find the resources ul
    # Typically looks like:
    # <li><a href="contact.html">Contact Us</a></li>
    # </ul>
    # We will insert the Developer API link right before </ul> inside the footer-links
    
    # We need to find the footer block
    # A safer way: replace `<li><a href="contact.html">Contact` with the developer link then contact link.
    
    new_content = re.sub(
        r'(<li>\s*<a[^>]*href="contact\.html"[^>]*>.*?Contact.*?</a>\s*</li>)',
        r'<li><a href="developers.html">Developer API</a></li>\n                        \1',
        content,
        flags=re.IGNORECASE
    )
    
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Added Developer API link to {filename}")
    else:
        print(f"Failed to match contact link in {filename}")
