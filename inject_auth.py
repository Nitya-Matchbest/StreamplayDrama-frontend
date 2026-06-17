import os

files = ['index.html', 'manage.html', 'add-testimonial.html', 'manage-testimonials.html']
auth_script = '\n    <!-- Auth Guard -->\n    <script src="js/auth.js"></script>'

for filename in files:
    filepath = os.path.join('drama-admin', filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False

    # Inject auth script
    if 'js/auth.js' not in content:
        content = content.replace('</head>', auth_script + '\n</head>')
        changed = True

    # Inject logout button
    logout_btn = '<button onclick="logoutAdmin()" class="btn-primary" style="padding: 5px 10px; font-size: 12px; margin-left: 10px;">Logout</button>'
    if 'logoutAdmin()' not in content:
        content = content.replace('<div class="topbar-avatar">A</div>', '<div class="topbar-avatar">A</div>\n        ' + logout_btn)
        changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Injected auth and logout into', filename)
