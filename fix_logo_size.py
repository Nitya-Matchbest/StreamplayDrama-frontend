import glob

for filename in glob.glob('*.html'):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    old_str1 = 'width="360" height="69" src="assets/images/new-logo-transparent.png"'
    new_str = 'height="75" style="width: auto;" src="assets/images/new-logo-transparent.png"'
    
    old_str2 = 'src="assets/images/new-logo-transparent.png" alt="StreamPlay Drama Logo"'
    new_str2 = 'style="height: 75px; width: auto;" src="assets/images/new-logo-transparent.png" alt="StreamPlay Drama Logo"'
    
    if old_str1 in content or old_str2 in content:
        content = content.replace(old_str1, new_str)
        content = content.replace(old_str2, new_str2)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Updated', filename)
