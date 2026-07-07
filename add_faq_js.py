import os

js_code = """
// ============================================================
// SMOOTH FAQ ACCORDION
// ============================================================
document.addEventListener('DOMContentLoaded', function() {
    const faqCards = document.querySelectorAll('.faq-card');
    
    faqCards.forEach(card => {
        const header = card.querySelector('.faq-header');
        const body = card.querySelector('.faq-body');
        const icon = header.querySelector('span');
        
        // Initial state setup for smooth animation
        body.style.display = 'block';
        body.style.overflow = 'hidden';
        body.style.height = '0px';
        body.style.paddingTop = '0px';
        body.style.paddingBottom = '0px';
        body.style.marginTop = '0px';
        body.style.opacity = '0';
        body.style.transition = 'all 0.4s cubic-bezier(0.4, 0, 0.2, 1)';
        icon.style.transition = 'transform 0.4s ease';
        
        let isOpen = false;
        
        header.addEventListener('click', () => {
            if (!isOpen) {
                // Close all other open FAQs
                faqCards.forEach(otherCard => {
                    if (otherCard !== card && otherCard.dataset.open === 'true') {
                        otherCard.querySelector('.faq-header').click();
                    }
                });
                
                // Open this FAQ
                card.dataset.open = 'true';
                card.style.background = 'rgba(10, 18, 50, 0.7)';
                card.style.borderColor = 'rgba(255, 255, 255, 0.3)';
                icon.style.transform = 'rotate(45deg)';
                
                // Calculate height by setting it to auto temporarily
                body.style.height = 'auto';
                body.style.paddingTop = '20px';
                body.style.paddingBottom = '24px';
                body.style.marginTop = '-5px';
                const fullHeight = body.scrollHeight + 'px';
                
                // Revert to 0 and trigger reflow
                body.style.height = '0px';
                body.style.paddingTop = '0px';
                body.style.paddingBottom = '0px';
                body.style.marginTop = '0px';
                body.offsetHeight; // trigger reflow
                
                // Animate to full height
                body.style.height = fullHeight;
                body.style.paddingTop = '20px';
                body.style.paddingBottom = '24px';
                body.style.marginTop = '-5px';
                body.style.opacity = '1';
                
                // Reset height to auto after animation so it handles window resize
                setTimeout(() => {
                    if (isOpen) body.style.height = 'auto';
                }, 400);
            } else {
                // Close this FAQ
                card.dataset.open = 'false';
                card.style.background = '#0A1232';
                card.style.borderColor = 'rgba(255, 255, 255, 0.08)';
                icon.style.transform = 'rotate(0deg)';
                
                // Set explicitly from auto to pixels to animate down
                body.style.height = body.scrollHeight + 'px';
                body.offsetHeight; // trigger reflow
                
                body.style.height = '0px';
                body.style.paddingTop = '0px';
                body.style.paddingBottom = '0px';
                body.style.marginTop = '0px';
                body.style.opacity = '0';
            }
            isOpen = !isOpen;
        });
    });
});
"""

with open('assets/js/main.js', 'a', encoding='utf-8') as f:
    f.write(js_code)

print("Appended smooth FAQ JS to main.js")
