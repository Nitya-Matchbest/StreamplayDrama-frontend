import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Change overflow: hidden to overflow: visible in .roadmap-card
roadmap_card_pattern = r'(\.roadmap-card\s*\{[^}]*?)overflow:\s*hidden;'
new_text = re.sub(roadmap_card_pattern, r'\1overflow: visible;', text)

# 2. Remove box-shadow from .roadmap-card:hover
roadmap_card_hover_pattern = r'(\.roadmap-card:hover\s*\{[^}]*?)box-shadow:\s*0\s*12px\s*30px\s*rgba\(0,\s*0,\s*0,\s*0\.4\);'
new_text = re.sub(roadmap_card_hover_pattern, r'\1', new_text)

# 3. Remove .roadmap-card, and .roadmap-card:hover, from the grouped selectors
grouped_selector_1 = r'\.roadmap-card,\s*(\.image-feature-card)'
new_text = re.sub(grouped_selector_1, r'\1', new_text)

grouped_selector_2 = r'\.roadmap-card:hover,\s*(\.image-feature-card:hover)'
new_text = re.sub(grouped_selector_2, r'\1', new_text)

if new_text != text:
    with open('assets/css/style.css', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print('Successfully updated roadmap-card styles.')
else:
    print('No changes were made. Please check the regex patterns.')
