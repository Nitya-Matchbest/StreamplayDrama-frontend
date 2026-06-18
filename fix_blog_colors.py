import re

with open('assets/css/blog.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Replace background colors with #010F29
css = re.sub(r'background:\s*#111827;', 'background: #010F29;', css)
css = re.sub(r'background:\s*linear-gradient\([^)]+\);', 'background: #010F29;', css)

# 2. Replace red #DC2626 with purple #822AEE
css = css.replace('#DC2626', '#822AEE')
css = css.replace('rgba(220, 38, 38', 'rgba(130, 42, 238')

# 3. Text colors: The user requested text color white and #822AEE. 
# Most text colors are already #FFFFFF (white) or #D1D5DB (light gray). 
# We'll just leave light gray alone since it's close to white, or maybe replace #D1D5DB with #FFFFFF.
css = css.replace('color: #D1D5DB;', 'color: #FFFFFF;')

# 4. Loading Spinner gradient:
spinner_old = '''border: 4px solid #374151;
    border-top-color: #822AEE;
    border-radius: 50%;'''

# We use the mask technique to make a gradient border for the spinner
spinner_new = '''border-radius: 50%;
    padding: 4px;
    background: linear-gradient(to right, #581C87, #3B0764);
    -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
    -webkit-mask-composite: xor;
    mask-composite: exclude;'''

css = css.replace(spinner_old, spinner_new)

# In case the spinner replacement didn't match exactly because of formatting:
if 'mask-composite: exclude;' not in css:
    # Alternative regex replace
    css = re.sub(
        r'border:\s*4px solid #374151;\s*border-top-color:\s*#822AEE;\s*border-radius:\s*50%;',
        spinner_new,
        css
    )

with open('assets/css/blog.css', 'w', encoding='utf-8') as f:
    f.write(css)
print('Updated blog.css')
