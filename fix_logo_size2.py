import glob

for filename in glob.glob('*.html'):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    old_str1 = 'height="75" style="width: auto;" src="assets/images/new-logo-transparent.png"'
    new_str1 = 'height="90" style="width: auto;" src="assets/images/new-logo-transparent.png"'
    
    old_str2 = 'style="height: 75px; width: auto;" src="assets/images/new-logo-transparent.png"'
    new_str2 = 'style="height: 90px; width: auto;" src="assets/images/new-logo-transparent.png"'
    
    changed = False
    if old_str1 in content:
        content = content.replace(old_str1, new_str1)
        changed = True
    if old_str2 in content:
        content = content.replace(old_str2, new_str2)
        changed = True
        
    if changed:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Updated', filename)
