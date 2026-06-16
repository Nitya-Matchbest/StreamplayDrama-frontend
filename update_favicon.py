import glob

for filename in glob.glob('*.html'):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    old_str = '<link rel="icon" href="assets/images/drama-icon.png" type="image/x-icon">'
    new_str = '<link rel="icon" href="assets/images/new-logo-transparent.png" type="image/x-icon">'
    
    if old_str in content:
        content = content.replace(old_str, new_str)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Updated', filename)
