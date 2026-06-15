import os
import glob

# Get all html files in the current directory
html_files = glob.glob('*.html')

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the problematic viewport tag
    # The tag might be slightly different in spacing, but we'll try a strict match first
    # Or just replace the specific string
    new_content = content.replace(
        'content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0"',
        'content="width=device-width, initial-scale=1"'
    )
    
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed viewport in {filename}")
    else:
        # Try a more flexible regex if strict replace failed
        import re
        new_content = re.sub(
            r'content="width=device-width,\s*initial-scale=1,\s*maximum-scale=1,\s*user-scalable=0"',
            'content="width=device-width, initial-scale=1"',
            content
        )
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed viewport (regex) in {filename}")
