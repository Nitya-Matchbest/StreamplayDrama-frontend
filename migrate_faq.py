import re
import os

drama_dir = r'c:\Users\GCV\Desktop\drama-frontend'
streamplay_dir = r'c:\Users\GCV\Desktop\Streamplay-frontend'

# 1. Get HTML from Streamplay
with open(os.path.join(streamplay_dir, 'index.html'), 'r', encoding='utf-8') as f:
    sp_html = f.read()

start_idx = sp_html.find('<section id="faq-block"')
end_idx = sp_html.find('</section>', start_idx) + 10
faq_html_content = sp_html[start_idx:end_idx]

# 2. Get CSS from Streamplay
with open(os.path.join(streamplay_dir, 'assets/css/style.css'), 'r', encoding='utf-8') as f:
    sp_css = f.read()

css_rules = [
    r'\.accordion\s*\{.*?\}',
    r'\.accordion:hover\s*\{.*?\}',
    r'\.accordion-slide\s*\{.*?\}',
    r'\.accordion-slide\.open\s*\{.*?\}',
    r'\.accordion-slide\.open \.accordion\s*\{.*?\}',
    r'\.accordion-wrap\s*\{.*?\}',
    r'\.accordion-slide \.button\s*\{.*?\}',
    r'\.accordion-slide\.open \.panel\s*\{.*?\}',
    r'\.accordion-slide\.open h3\.accordion::before\s*\{.*?\}',
    r'\.accordion-slide\.open h3\.accordion::after\s*\{.*?\}',
    r'\.accordion-slide\s*\{[^}]*box-shadow:[^}]*\}',
]

css_to_add = "/* FAQ ACCORDION CSS FROM STREAMPLAY */\n"
for rule in css_rules:
    matches = re.finditer(rule, sp_css, re.DOTALL)
    for m in matches:
        css_to_add += m.group(0) + "\n"

# 3. Get JS from Streamplay
with open(os.path.join(streamplay_dir, 'assets/js/main.js'), 'r', encoding='utf-8') as f:
    sp_js = f.read()

js_start = sp_js.find('/* ============================================================')
js_start = sp_js.find('FAQ ACCORDION', js_start) - 100
js_end = sp_js.find('})();', js_start) + 5
faq_js_content = sp_js[js_start:js_end]

# --- APPLY TO DRAMA-FRONTEND ---

# Update HTML
with open(os.path.join(drama_dir, 'index.html'), 'r', encoding='utf-8') as f:
    dr_html = f.read()
    
# Find the old FAQ section
old_faq_start = dr_html.find('<section class="section_container sip-bg faq-section"')
old_faq_end = dr_html.find('</section>', old_faq_start) + 10

if old_faq_start != -1:
    new_html = dr_html[:old_faq_start] + faq_html_content + dr_html[old_faq_end:]
    with open(os.path.join(drama_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(new_html)
    print('Replaced HTML.')

# Update CSS
with open(os.path.join(drama_dir, 'assets/css/style.css'), 'r', encoding='utf-8') as f:
    dr_css = f.read()
if 'FAQ ACCORDION CSS FROM STREAMPLAY' not in dr_css:
    with open(os.path.join(drama_dir, 'assets/css/style.css'), 'a', encoding='utf-8') as f:
        f.write('\n\n' + css_to_add)
    print('Appended CSS.')

# Update JS
with open(os.path.join(drama_dir, 'assets/js/main.js'), 'r', encoding='utf-8') as f:
    dr_js = f.read()

# Remove the old script
old_js_pattern = r'const faqCards = document\.querySelectorAll\(\'\.faq-card\'\);.*?\}\);(?:\n\s*\}\);)?'
dr_js_clean = re.sub(old_js_pattern, faq_js_content, dr_js, flags=re.DOTALL)

if dr_js_clean != dr_js:
    with open(os.path.join(drama_dir, 'assets/js/main.js'), 'w', encoding='utf-8') as f:
        f.write(dr_js_clean)
    print('Replaced JS.')
else:
    # If regex failed, just append
    if 'accordions = document.getElementsByClassName' not in dr_js:
        with open(os.path.join(drama_dir, 'assets/js/main.js'), 'a', encoding='utf-8') as f:
            f.write('\n\n' + faq_js_content)
        print('Appended JS.')
