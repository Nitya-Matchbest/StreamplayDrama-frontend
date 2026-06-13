/* =============================================================
   Drama Platform - Main JavaScript
   ============================================================= */

// ============================================================
// HERO CAROUSEL - AUTO-CHANGING EVERY 5 SECONDS
// ============================================================
document.addEventListener('DOMContentLoaded', function() {
    const slides = document.querySelectorAll('.hero-slide');
    const indicators = document.querySelectorAll('.hero-indicators .indicator');
    let currentSlide = 0;
    let autoPlayInterval;
    
    if (slides.length > 0) {
        // Function to show specific slide
        function showSlide(index) {
            // Remove active class from all slides and indicators
            slides.forEach(slide => {
                slide.classList.remove('active');
            });
            indicators.forEach(indicator => {
                indicator.classList.remove('active');
            });
            
            // Add active class to current slide and indicator
            slides[index].classList.add('active');
            indicators[index].classList.add('active');
        }
        
        // Function to go to next slide
        function nextSlide() {
            currentSlide = (currentSlide + 1) % slides.length;
            showSlide(currentSlide);
        }
        
        // Auto-play carousel every 5 seconds
        function startAutoPlay() {
            autoPlayInterval = setInterval(nextSlide, 5000);
        }
        
        // Stop auto-play
        function stopAutoPlay() {
            clearInterval(autoPlayInterval);
        }
        
        // Click on indicators to change slide
        indicators.forEach((indicator, index) => {
            indicator.addEventListener('click', function() {
                currentSlide = index;
                showSlide(currentSlide);
                
                // Restart auto-play
                stopAutoPlay();
                startAutoPlay();
            });
        });
        
        // Pause on hover (optional)
        const heroSection = document.querySelector('.hero-section');
        if (heroSection) {
            heroSection.addEventListener('mouseenter', stopAutoPlay);
            heroSection.addEventListener('mouseleave', startAutoPlay);
        }
        
        // Start auto-play on page load
        startAutoPlay();
    }
});

// Mobile Menu Toggle
document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.getElementById('ham');
    const navMenu = document.getElementById('nav');
    
    if (hamburger) {
        hamburger.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            hamburger.classList.toggle('active');
        });
    }
    
    // Back to Top Button
    const backToTop = document.getElementById('backToTop');
    
    if (backToTop) {
        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 300) {
                backToTop.style.display = 'flex';
            } else {
                backToTop.style.display = 'none';
            }
        });
        
        backToTop.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }
    
    // Scroll Animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('section-animated');
            }
        });
    }, observerOptions);
    
    // Observe all sections
    const sections = document.querySelectorAll('.section_container');
    sections.forEach(section => {
        observer.observe(section);
    });
    
    // Active navigation highlight
    const navLinks = document.querySelectorAll('.nav-tab');
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    
    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPage) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
});

// Close mobile menu when clicking outside
document.addEventListener('click', function(event) {
    const navMenu = document.getElementById('nav');
    const hamburger = document.getElementById('ham');
    
    if (navMenu && hamburger) {
        if (!navMenu.contains(event.target) && !hamburger.contains(event.target)) {
            navMenu.classList.remove('active');
            hamburger.classList.remove('active');
        }
    }
});

// Hover effects for cards
document.addEventListener('DOMContentLoaded', function() {
    const hoverItems = document.querySelectorAll('.hover-item');
    
    hoverItems.forEach(item => {
        item.addEventListener('mouseenter', function() {
            hoverItems.forEach(i => i.classList.remove('active'));
            this.classList.add('active');
        });
    });
    
    // Set first item as active by default
    if (hoverItems.length > 0) {
        hoverItems[0].classList.add('active');
    }
});

// ============================================================
// Drama Feature Cards - Scroll Animation
// ============================================================
document.addEventListener('DOMContentLoaded', function() {
    const featureCards = document.querySelectorAll('.drama-feature-card');
    
    if (featureCards.length === 0) return;
    
    const observerOptions = {
        threshold: 0.2,
        rootMargin: '0px 0px -100px 0px'
    };
    
    const featureObserver = new IntersectionObserver(function(entries) {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                // Add visible class to trigger animation
                setTimeout(() => {
                    entry.target.classList.add('visible');
                }, index * 150); // Staggered delay
                
                // Stop observing once animated
                featureObserver.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Observe all feature cards
    featureCards.forEach(card => {
        featureObserver.observe(card);
    });
});

// ============================================================
// Smooth Parallax Effect on Feature Images (Optional Enhancement)
// ============================================================
let ticking = false;

function updateParallax() {
    const featureVisuals = document.querySelectorAll('.drama-feature-visual');
    
    featureVisuals.forEach(visual => {
        const rect = visual.getBoundingClientRect();
        const scrolled = window.pageYOffset;
        const rate = scrolled * 0.03;
        
        if (rect.top < window.innerHeight && rect.bottom > 0) {
            const img = visual.querySelector('.visual-frame');
            if (img) {
                img.style.transform = `translateY(${rate}px)`;
            }
        }
    });
    
    ticking = false;
}

window.addEventListener('scroll', function() {
    if (!ticking) {
        window.requestAnimationFrame(updateParallax);
        ticking = true;
    }
});


// ============================================================
// NETFLIX-STYLE CAROUSEL FUNCTIONALITY
// ============================================================
document.addEventListener('DOMContentLoaded', function() {
    const carousel = document.getElementById('dramaCarousel');
    const prevBtn = document.querySelector('.carousel-prev');
    const nextBtn = document.querySelector('.carousel-next');
    const progressBar = document.getElementById('carouselProgress');
    
    if (!carousel || !prevBtn || !nextBtn) return;
    
    const cards = carousel.querySelectorAll('.carousel-card');
    const cardWidth = 220 + 20; // card width + gap
    const scrollAmount = cardWidth * 3; // Scroll 3 cards at a time
    
    // Update progress bar
    function updateProgress() {
        const scrollPercentage = (carousel.scrollLeft / (carousel.scrollWidth - carousel.clientWidth)) * 100;
        progressBar.style.width = scrollPercentage + '%';
        
        // Update button states
        prevBtn.disabled = carousel.scrollLeft <= 0;
        nextBtn.disabled = carousel.scrollLeft >= carousel.scrollWidth - carousel.clientWidth - 10;
    }
    
    // Scroll to previous
    prevBtn.addEventListener('click', function() {
        carousel.scrollBy({
            left: -scrollAmount,
            behavior: 'smooth'
        });
    });
    
    // Scroll to next
    nextBtn.addEventListener('click', function() {
        carousel.scrollBy({
            left: scrollAmount,
            behavior: 'smooth'
        });
    });
    
    // Update progress on scroll
    carousel.addEventListener('scroll', updateProgress);
    
    // Initial progress update
    updateProgress();
    
    // Touch/Swipe support for mobile
    let isDown = false;
    let startX;
    let scrollLeft;
    
    carousel.addEventListener('mousedown', (e) => {
        isDown = true;
        carousel.style.cursor = 'grabbing';
        startX = e.pageX - carousel.offsetLeft;
        scrollLeft = carousel.scrollLeft;
    });
    
    carousel.addEventListener('mouseleave', () => {
        isDown = false;
        carousel.style.cursor = 'grab';
    });
    
    carousel.addEventListener('mouseup', () => {
        isDown = false;
        carousel.style.cursor = 'grab';
    });
    
    carousel.addEventListener('mousemove', (e) => {
        if (!isDown) return;
        e.preventDefault();
        const x = e.pageX - carousel.offsetLeft;
        const walk = (x - startX) * 2;
        carousel.scrollLeft = scrollLeft - walk;
    });
    
    // Touch events for mobile
    let touchStartX = 0;
    let touchEndX = 0;
    
    carousel.addEventListener('touchstart', (e) => {
        touchStartX = e.changedTouches[0].screenX;
    }, { passive: true });
    
    carousel.addEventListener('touchend', (e) => {
        touchEndX = e.changedTouches[0].screenX;
        handleSwipe();
    }, { passive: true });
    
    function handleSwipe() {
        const swipeThreshold = 50;
        const diff = touchStartX - touchEndX;
        
        if (Math.abs(diff) > swipeThreshold) {
            if (diff > 0) {
                // Swipe left - scroll right
                carousel.scrollBy({
                    left: scrollAmount,
                    behavior: 'smooth'
                });
            } else {
                // Swipe right - scroll left
                carousel.scrollBy({
                    left: -scrollAmount,
                    behavior: 'smooth'
                });
            }
        }
    }
    
    // Keyboard navigation
    carousel.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowLeft') {
            carousel.scrollBy({
                left: -scrollAmount,
                behavior: 'smooth'
            });
        } else if (e.key === 'ArrowRight') {
            carousel.scrollBy({
                left: scrollAmount,
                behavior: 'smooth'
            });
        }
    });
    
    // Make carousel focusable for keyboard navigation
    carousel.setAttribute('tabindex', '0');
    
    // Auto-scroll on window resize to maintain position
    let resizeTimer;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(function() {
            updateProgress();
        }, 250);
    });
});


// ============================================================
// FEATURES CAROUSEL - MANUAL NAV (NO AUTO-PLAY)
// ============================================================
document.addEventListener('DOMContentLoaded', function() {
    const featuresCards = document.querySelectorAll('.feature-carousel-card');
    const featuresDots  = document.querySelectorAll('.features-dot');
    const prevBtn       = document.getElementById('featuresPrev');
    const nextBtn       = document.getElementById('featuresNext');
    let currentFeature  = 0;

    if (featuresCards.length === 0) return;

    function showFeature(index) {
        featuresCards.forEach(card => card.classList.remove('active', 'prev'));
        featuresDots.forEach(dot  => dot.classList.remove('active'));

        const prevIndex = currentFeature;
        if (prevIndex !== index) {
            featuresCards[prevIndex].classList.add('prev');
        }

        featuresCards[index].classList.add('active');
        featuresDots[index].classList.add('active');
        currentFeature = index;
    }

    // Dot clicks
    featuresDots.forEach((dot, index) => {
        dot.addEventListener('click', () => showFeature(index));
    });

    // Prev arrow
    if (prevBtn) {
        prevBtn.addEventListener('click', () => {
            const prev = (currentFeature - 1 + featuresCards.length) % featuresCards.length;
            showFeature(prev);
        });
    }

    // Next arrow
    if (nextBtn) {
        nextBtn.addEventListener('click', () => {
            const next = (currentFeature + 1) % featuresCards.length;
            showFeature(next);
        });
    }
});

// ============================================================
// LANDSCAPE CAROUSELS - PREV / NEXT BUTTON HANDLERS
// ============================================================
document.addEventListener('DOMContentLoaded', function () {
    const scrollAmount = 280 * 3; // scroll 3 cards at a time

    document.querySelectorAll('.lc-btn').forEach(function (btn) {
        btn.addEventListener('click', function () {
            const targetId = btn.getAttribute('data-target');
            const track = document.getElementById(targetId);
            if (!track) return;

            if (btn.classList.contains('lc-prev')) {
                track.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
            } else {
                track.scrollBy({ left: scrollAmount, behavior: 'smooth' });
            }
        });
    });
});
