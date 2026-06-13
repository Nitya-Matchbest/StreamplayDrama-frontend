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
// NETFLIX-STYLE CAROUSEL - DOTS + SCROLL FUNCTIONALITY
// ============================================================
document.addEventListener('DOMContentLoaded', function() {
    var carousel  = document.getElementById('dramaCarousel');
    var prevBtn   = document.querySelector('.carousel-prev');
    var nextBtn   = document.querySelector('.carousel-next');
    var dotsWrap  = document.getElementById('dramaCarouselDots');
    var swipeHint = document.querySelector('.drama-swipe-hint');

    if (!carousel) return;

    var cards       = Array.from(carousel.querySelectorAll('.carousel-card'));
    var cardCount   = cards.length;
    var dots        = [];
    var scrollAmount = (cards[0] ? cards[0].offsetWidth + 20 : 200) * 3;

    // --- Build dots ---
    if (dotsWrap && cardCount > 0) {
        cards.forEach(function(_, i) {
            var btn = document.createElement('button');
            btn.className = 'drama-dot' + (i === 0 ? ' active' : '');
            btn.setAttribute('aria-label', 'Go to card ' + (i + 1));
            btn.addEventListener('click', function() {
                cards[i].scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
                setActiveDot(i);
            });
            dotsWrap.appendChild(btn);
            dots.push(btn);
        });
    }

    function setActiveDot(index) {
        dots.forEach(function(d) { d.classList.remove('active'); });
        if (dots[index]) dots[index].classList.add('active');
    }

    // --- IntersectionObserver: which card is most visible ---
    var observer = new IntersectionObserver(function(entries) {
        var best = -1, bestRatio = 0;
        entries.forEach(function(entry) {
            if (entry.intersectionRatio > bestRatio) {
                bestRatio = entry.intersectionRatio;
                best = cards.indexOf(entry.target);
            }
        });
        if (best !== -1) setActiveDot(best);
    }, { root: carousel, threshold: [0.3, 0.5, 0.7] });

    cards.forEach(function(card) { observer.observe(card); });

    // --- Fade swipe hint after first scroll ---
    var hintFaded = false;
    carousel.addEventListener('scroll', function() {
        if (!hintFaded && swipeHint) {
            swipeHint.style.opacity = '0';
            swipeHint.style.transition = 'opacity 0.5s ease';
            hintFaded = true;
        }
    }, { passive: true });

    // --- Prev / Next buttons ---
    if (prevBtn) {
        prevBtn.addEventListener('click', function() {
            carousel.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
        });
    }
    if (nextBtn) {
        nextBtn.addEventListener('click', function() {
            carousel.scrollBy({ left: scrollAmount, behavior: 'smooth' });
        });
    }

    // --- Touch swipe ---
    var touchStartX = 0;
    carousel.addEventListener('touchstart', function(e) {
        touchStartX = e.changedTouches[0].screenX;
    }, { passive: true });
    carousel.addEventListener('touchend', function(e) {
        var diff = touchStartX - e.changedTouches[0].screenX;
        if (Math.abs(diff) > 50) {
            carousel.scrollBy({ left: diff > 0 ? scrollAmount : -scrollAmount, behavior: 'smooth' });
        }
    }, { passive: true });

    // --- Mouse drag ---
    var isDown = false, startX, scrollLeft;
    carousel.addEventListener('mousedown', function(e) { isDown = true; startX = e.pageX - carousel.offsetLeft; scrollLeft = carousel.scrollLeft; });
    carousel.addEventListener('mouseleave', function() { isDown = false; });
    carousel.addEventListener('mouseup', function() { isDown = false; });
    carousel.addEventListener('mousemove', function(e) {
        if (!isDown) return;
        e.preventDefault();
        carousel.scrollLeft = scrollLeft - (e.pageX - carousel.offsetLeft - startX) * 2;
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

// ============================================================
// PLATFORM OWNERSHIP - MOBILE SWIPE CAROUSEL WITH DOTS
// ============================================================
document.addEventListener('DOMContentLoaded', function () {
    var grid      = document.getElementById('ownershipGrid');
    var dots      = document.querySelectorAll('#ownershipDots .ownership-dot');
    var swipeHint = document.querySelector('.ownership-swipe-hint');
    var cards     = grid ? grid.querySelectorAll('.ownership-card') : [];

    if (!grid || cards.length === 0 || dots.length === 0) return;

    function isMobile() { return window.innerWidth <= 768; }

    function setActiveDot(index) {
        dots.forEach(function (d) { d.classList.remove('active'); });
        if (dots[index]) dots[index].classList.add('active');
    }

    function setActiveCard(index) {
        cards.forEach(function (c) { c.classList.remove('carousel-active'); });
        if (cards[index]) cards[index].classList.add('carousel-active');
    }

    // IntersectionObserver: detect which card is most visible
    var observer = new IntersectionObserver(function (entries) {
        if (!isMobile()) return;
        var best = -1, bestRatio = 0;
        entries.forEach(function (entry) {
            if (entry.intersectionRatio > bestRatio) {
                bestRatio = entry.intersectionRatio;
                best = Array.prototype.indexOf.call(cards, entry.target);
            }
        });
        if (best !== -1) {
            setActiveDot(best);
            setActiveCard(best);
        }
    }, { root: grid, threshold: [0.4, 0.6, 0.8] });

    cards.forEach(function (card) { observer.observe(card); });

    // Fade swipe hint after first scroll
    var hintFaded = false;
    grid.addEventListener('scroll', function () {
        if (!hintFaded && swipeHint) {
            swipeHint.style.opacity = '0';
            hintFaded = true;
        }
    }, { passive: true });

    // Dot click: scroll matching card into view
    dots.forEach(function (dot, i) {
        dot.addEventListener('click', function () {
            if (!isMobile()) return;
            cards[i].scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
            setActiveDot(i);
            setActiveCard(i);
        });
    });

    // On resize: reset when returning to desktop
    window.addEventListener('resize', function () {
        if (!isMobile()) {
            cards.forEach(function (c) { c.classList.remove('carousel-active'); });
            dots.forEach(function (d) { d.classList.remove('active'); });
            if (dots[0]) dots[0].classList.add('active');
        }
    });

    // Init
    setActiveDot(0);
    setActiveCard(0);
});
