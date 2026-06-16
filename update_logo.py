import glob

for filename in glob.glob('*.html'):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    old_str = 'width="280" height="54" src="assets/images/new-logo-transparent.png"'
    new_str = 'width="360" height="69" src="assets/images/new-logo-transparent.png"'
    
    if old_str in content:
        content = content.replace(old_str, new_str)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Updated', filename)
