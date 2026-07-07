import urllib.request
import re

url = 'https://streamplay-drama-frontend.vercel.app/'
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    expert_match = re.search(r'<div class="expert".*?>.*?</div>', html, re.DOTALL | re.IGNORECASE)
    print('VERCEL HTML:')
    print(expert_match.group(0) if expert_match else 'Not found')
except Exception as e:
    print('Vercel error:', e)

with open('index.html', 'r', encoding='utf-8') as f:
    local_html = f.read()
local_expert = re.search(r'<div class="expert".*?>.*?</div>', local_html, re.DOTALL | re.IGNORECASE)
print('\nLOCAL HTML:')
print(local_expert.group(0) if local_expert else 'Not found')
