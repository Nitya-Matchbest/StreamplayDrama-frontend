import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'<span>One</span> Platform\. <span>Every</span> Use Case\..*?</section>', text, re.DOTALL | re.IGNORECASE)
if match:
    section_html = match.group(0)
    # Find classes of the cards inside this section
    cards = re.finditer(r'class="([^"]*card[^"]*)"', section_html)
    for c in cards:
        print(c.group(1))
