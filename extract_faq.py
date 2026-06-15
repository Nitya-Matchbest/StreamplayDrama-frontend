import re

with open(r'C:\Users\GCV\.gemini\antigravity\brain\922e5b38-0668-4e12-89ca-9a18d766ef35\.system_generated\steps\1527\content.md', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'<section id="faq-block".*?</section>', text, re.IGNORECASE | re.DOTALL)
if match:
    with open('faq_section.html', 'w', encoding='utf-8') as out:
        out.write(match.group(0))
    print('FAQ saved to faq_section.html')
else:
    print('FAQ block not found')
