import glob

for filename in glob.glob('*.html'):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to replace the height 90px and transform with height 120px and flex centering
    old_str1 = 'style="height: 90px; width: auto; transform: translateY(8px);" src="assets/images/new-logo-transparent.png"'
    new_str1 = 'style="height: 130px; width: auto; vertical-align: middle; margin-top: 5px;" src="assets/images/new-logo-transparent.png"'
    
    old_str2 = 'style="height: 90px; width: auto;" src="assets/images/new-logo-transparent.png"'
    new_str2 = 'style="height: 130px; width: auto; vertical-align: middle; margin-top: 5px;" src="assets/images/new-logo-transparent.png"'
    
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
