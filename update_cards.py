import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# We will replace all <a> tags that link to usecase-*.html inside the 'One Platform' section

match = re.search(r'<span>One</span> Platform\. <span>Every</span> Use Case\..*?</section>', text, re.DOTALL | re.IGNORECASE)
if match:
    section_html = match.group(0)
    
    # regex to find <a href="usecase..." style="..." onmouseover="..." onmouseout="...">
    new_section_html = re.sub(
        r'<a href="(usecase-[^"]*\.html)"\s+style="[^"]*"\s+onmouseover="[^"]*"\s+onmouseout="[^"]*">',
        r'<a href="\1" class="roadmap-card" style="display: block; text-decoration: none;">',
        section_html
    )
    
    new_text = text.replace(section_html, new_section_html)
    
    if new_text != text:
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_text)
        print('Updated use case cards to use roadmap-card class')
    else:
        print('No changes made. Regex might have failed.')
else:
    print('Section not found')
