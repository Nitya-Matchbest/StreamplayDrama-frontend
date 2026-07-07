import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# The roadmap section ends before the support & SLA section
# Let's search for "<!-- Section 3.5: Support & SLA -->"
match = re.search(r'(</section>\s*)(<!-- Section 3\.5: Support & SLA -->)', text)

if match:
    new_section = """
    <!-- Section 3.4: Universal Device Compatibility -->
    <section class="section_container sip-bg" style="padding: 80px 0 100px;">
        <div class="container">
            <div class="section-head text-center" style="margin-bottom: 70px;">
                <h2 class="section-title">Universal Device Compatibility</h2>
            </div>
            
            <div style="display: flex; flex-wrap: wrap; justify-content: center; align-items: center; gap: 50px;">
                <img src="assets/images/Paragraph.png" alt="Web and Desktop Compatibility" style="height: 90px; width: auto; object-fit: contain; transition: transform 0.3s ease;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                <img src="assets/images/Paragraph (1).png" alt="iOS and Android Compatibility" style="height: 90px; width: auto; object-fit: contain; transition: transform 0.3s ease;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                <img src="assets/images/Paragraph (2).png" alt="Apple TV and Roku Compatibility" style="height: 90px; width: auto; object-fit: contain; transition: transform 0.3s ease;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                <img src="assets/images/Paragraph (3).png" alt="PlayStation and Xbox Compatibility" style="height: 90px; width: auto; object-fit: contain; transition: transform 0.3s ease;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                <img src="assets/images/Paragraph (4).png" alt="Chromecast and AirPlay Compatibility" style="height: 90px; width: auto; object-fit: contain; transition: transform 0.3s ease;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
            </div>
        </div>
    </section>
"""
    # Insert new section
    text = text[:match.start(1)] + match.group(1) + new_section + match.group(2) + text[match.end(2):]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Successfully added Universal Device Compatibility section.")
else:
    print("Could not find the insertion point.")
