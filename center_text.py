import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# The cards currently have this exact style
target = 'class="roadmap-card" style="display: block; text-decoration: none;"'
replacement = 'class="roadmap-card" style="display: block; text-decoration: none; text-align: center;"'

new_text = text.replace(target, replacement)

if new_text != text:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print('Successfully added text-align: center to the cards.')
else:
    print('No changes made. The target string might not be an exact match.')
