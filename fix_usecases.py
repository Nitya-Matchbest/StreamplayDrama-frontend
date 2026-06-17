import os

files = ['usecase-arabic.html', 'usecase-indie.html', 'usecase-kdrama.html', 'usecase-turkish.html']

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update theme color meta
    content = content.replace('content="#1E1233"', 'content="#0D0D1A"')
    
    # Update radial gradient to red theme
    content = content.replace('background: radial-gradient(circle at center top, #2d0a4e 0%, #090910 70%);', 'background: radial-gradient(circle at center top, #1A0000 0%, var(--background) 70%);')
    
    # Update solid background color to theme variable
    content = content.replace('background-color: #07070B;', 'background-color: var(--background);')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
