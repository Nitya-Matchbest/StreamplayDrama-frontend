import glob

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    new_text = text.replace('style="height: 45px; width: auto;" src="assets/images/9 1.png"', 'style="height: 35px; width: auto;" src="assets/images/9 1.png"')
    
    if new_text != text:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_text)
        print(f'Updated {file}')
