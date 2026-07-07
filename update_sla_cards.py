import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the specific inline style pattern for the SLA cards
old_pattern = r'<div style=\"background: #0A1232; border: 1px solid rgba\(255, 255, 255, 0.08\); border-radius: 16px; padding: 40px 30px; text-align: center; transition: transform 0.3s; cursor: default;\" onmouseover=\"this.style.transform=\'translateY\(-5px\)\';\" onmouseout=\"this.style.transform=\'translateY\(0\)\';\">'
new_replacement = '<div class="roadmap-card" style="padding: 40px 30px; text-align: center; cursor: default;">'

new_text = re.sub(old_pattern, new_replacement, text)

if new_text != text:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print('Updated Enterprise Support cards to use roadmap-card class')
else:
    print('No changes made. Pattern might not match.')
