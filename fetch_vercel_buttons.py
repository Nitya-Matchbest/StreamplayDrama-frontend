import urllib.request
import re

url = 'https://streamplay-drama-frontend.vercel.app/'
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    
    # Extract the header/navbar section
    header_match = re.search(r'<header[^>]*>.*?</header>', html, re.DOTALL | re.IGNORECASE)
    if header_match:
        header_html = header_match.group(0)
        
        # Look for the expert div or any links in the right side
        expert_match = re.search(r'<div class="expert".*?>.*?</div>', header_html, re.DOTALL | re.IGNORECASE)
        if expert_match:
            print("--- Buttons HTML ---")
            print(expert_match.group(0))
        else:
            print("Expert div not found, printing whole header:")
            print(header_html[:1000])
            
    else:
        print('Header not found')
        
    # Let's also fetch the CSS for these buttons.
    # Usually it's in assets/css/style.css
    css_url = 'https://streamplay-drama-frontend.vercel.app/assets/css/style.css'
    req_css = urllib.request.Request(css_url, headers={'User-Agent': 'Mozilla/5.0'})
    css_response = urllib.request.urlopen(req_css)
    css_text = css_response.read().decode('utf-8')
    
    # Search for button CSS like .request-demo, .watch-demo, .expert a
    print("\n--- Button CSS ---")
    btn_css_matches = re.finditer(r'\.(request-demo|watch-demo|expert a|btn-outline)[^\{]*\{[^}]+\}', css_text)
    for m in btn_css_matches:
        print(m.group(0))

except Exception as e:
    print('Error:', e)
