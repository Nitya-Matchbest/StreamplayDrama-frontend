import os, re

files = [f for f in os.listdir('.') if f.endswith('.html')]

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
        
    original = text

    # Update logo height
    text = text.replace('height: 130px;', 'height: 70px;')

    # Extract and move supported-platforms if it is in Col 1
    match = re.search(r'(\s*<div class=\"supported-platforms\">.*?</div>\s*)</div>\s*<!-- Col 2: Platforms We Build -->', text, re.DOTALL)
    
    if match:
        inner_block = match.group(1)
        
        # Remove from Col 1
        text = text.replace(inner_block + '</div>\n                <!-- Col 2: Platforms We Build -->', '\n                </div>\n                <!-- Col 2: Platforms We Build -->')
        
        # Append to Col 4
        col4_end_target = '</div>\n                </div>\n            </div>\n\n            <div class=\"footer-bottom\">'
        replacement_col4 = '</div>\n' + inner_block + '                </div>\n            </div>\n\n            <div class=\"footer-bottom\">'
        
        text = text.replace(col4_end_target, replacement_col4)

    if original != text:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f'Updated {file_path}')
