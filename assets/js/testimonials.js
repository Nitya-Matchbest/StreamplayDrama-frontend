document.addEventListener('DOMContentLoaded', () => {
    
    // API Configuration - Update when deploying
    const API_BASE = 'https://streamplaydrama-backend.onrender.com';

    const TESTIMONIALS_API = `${API_BASE}/api/testimonials`;

    const grid = document.getElementById('testimonialsGrid');

    async function fetchTestimonials() {
        try {
            const res = await fetch(TESTIMONIALS_API);
            const data = await res.json();
            
            if (data.success) {
                renderTestimonials(data.data);
            } else {
                throw new Error(data.message || 'Failed to fetch testimonials');
            }
        } catch (error) {
            console.error('Error fetching testimonials:', error);
            grid.innerHTML = `
                <div class="no-testimonials">
                    <h3>Unable to load testimonials</h3>
                    <p>There was a problem connecting to the server. Please try again later.</p>
                </div>
            `;
        }
    }

    function renderTestimonials(testimonials) {
        if (!testimonials || testimonials.length === 0) {
            grid.innerHTML = `
                <div class="no-testimonials">
                    <h3>No Testimonials Yet</h3>
                    <p>Check back later to see what our clients are saying.</p>
                </div>
            `;
            return;
        }

        let html = '';
        
        testimonials.forEach(t => {
            // Stars HTML
            let starsHtml = '';
            for (let i = 0; i < t.rating; i++) {
                starsHtml += `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>`;
            }

            // Featured Badge HTML
            let featuredHtml = '';
            if (t.isFeatured) {
                featuredHtml = `
                    <div class="testimonial-featured-badge">
                        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="#FBBF24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
                        Featured
                    </div>
                `;
            }

            // Image Source Resolution
            const imgSrc = t.image ? (t.image.startsWith('http') ? t.image : API_BASE + t.image) : 'https://via.placeholder.com/80/1A1A2E/ffffff?text=U';

            html += `
                <div class="testimonial-card">
                    ${featuredHtml}
                    
                    <div class="testimonial-stars">
                        ${starsHtml}
                    </div>
                    
                    <div class="testimonial-text">
                        "${t.text}"
                    </div>
                    
                    <div class="testimonial-divider"></div>
                    
                    <div class="testimonial-reviewer">
                        <img src="${imgSrc}" alt="${t.name}" class="testimonial-avatar" onerror="this.src='https://via.placeholder.com/80/1A1A2E/ffffff?text=U'">
                        <div class="testimonial-info">
                            <span class="testimonial-name">${t.name}</span>
                            <span class="testimonial-company">${t.company}</span>
                        </div>
                    </div>
                </div>
            `;
        });

        grid.innerHTML = html;
    }

    // Initialize
    fetchTestimonials();
});
