import glob
import sys

html_files = glob.glob('*.html')

ig_old = '<a href="#" aria-label="Instagram" class="social-link">'
ig_new = '<a href="https://www.instagram.com/thestreamplay.ai?utm_source=ig_web_button_share_sheet&amp;igsh=ZDNlZDc0MzIxNw%3D%3D" aria-label="Instagram" class="social-link" target="_blank">'

yt_old = '<a href="#" aria-label="YouTube" class="social-link">'
yt_new = '<a href="https://www.youtube.com/@thestreamplayAI" aria-label="YouTube" class="social-link" target="_blank">'

li_old = '<a href="#" aria-label="LinkedIn" class="social-link">'
li_new = '<a href="https://www.linkedin.com/company/streamplayai/" aria-label="LinkedIn" class="social-link" target="_blank">'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if ig_old in content or yt_old in content or li_old in content:
        new_content = content.replace(ig_old, ig_new).replace(yt_old, yt_new).replace(li_old, li_new)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated {file}')
    else:
        print(f'No matching links found in {file}')
