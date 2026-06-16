import glob

for filename in glob.glob('*.html'):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    old_str = 'style="height: 90px; width: auto;" src="assets/images/new-logo-transparent.png"'
    new_str = 'style="height: 90px; width: auto; transform: translateY(8px);" src="assets/images/new-logo-transparent.png"'
    
    if old_str in content:
        content = content.replace(old_str, new_str)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Updated', filename)
