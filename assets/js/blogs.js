/* =============================================================
   Drama Platform - Blogs Listing JavaScript
   ============================================================= */

// API Configuration - Update when deploying
const API_BASE = 'https://streamplaydrama-backend.onrender.com';
const API_URL = `${API_BASE}/api/blogs`;

let currentPage = 1;
let totalPages = 1;
let currentCategory = 'all';
let searchQuery = '';

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    loadBlogs();
    setupFilters();
});

// Setup filters
function setupFilters() {
    // Category buttons
    const categoryButtons = document.querySelectorAll('.category-btn');
    categoryButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            categoryButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            currentCategory = btn.getAttribute('data-category');
            currentPage = 1;
            loadBlogs();
        });
    });

    // Search input with debounce
    let searchTimeout;
    const searchInput = document.getElementById('searchInput');
    searchInput.addEventListener('input', (e) => {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(() => {
            searchQuery = e.target.value;
            currentPage = 1;
            loadBlogs();
        }, 500);
    });
}

// Load blogs from API
async function loadBlogs() {
    const blogGrid = document.getElementById('blogGrid');
    blogGrid.innerHTML = `
        <div class="loading-spinner">
            <div class="spinner"></div>
            <p>Loading articles...</p>
        </div>
    `;

    try {
        let url = `${API_URL}?page=${currentPage}&limit=9`;
        
        if (currentCategory !== 'all') {
            url += `&category=${encodeURIComponent(currentCategory)}`;
        }
        
        if (searchQuery) {
            url += `&search=${encodeURIComponent(searchQuery)}`;
        }

        const response = await fetch(url);
        const data = await response.json();

        if (data.success && data.data.length > 0) {
            totalPages = data.totalPages;
            renderBlogs(data.data);
            renderPagination();
        } else {
            showNoResults();
        }
    } catch (error) {
        console.error('Error loading blogs:', error);
        showError('Failed to load articles. Please try again later.');
    }
}

// Render blog cards
function renderBlogs(blogs) {
    const blogGrid = document.getElementById('blogGrid');
    
    const html = blogs.map(blog => {
        const date = new Date(blog.publishDate).toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'short',
            day: 'numeric'
        });

        // Handle image URL
        const imageUrl = blog.featuredImage.startsWith('/api/image/') 
            ? API_BASE + blog.featuredImage 
            : blog.featuredImage;

        return `
            <div class="blog-card" onclick="window.location.href='blog-detail.html?slug=${blog.slug}'">
                <img src="${imageUrl}" alt="${blog.title}" class="blog-card-image" 
                     onerror="this.src='data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%22400%22 height=%22220%22%3E%3Crect fill=%22%23374151%22 width=%22400%22 height=%22220%22/%3E%3Ctext x=%2250%25%22 y=%2250%25%22 text-anchor=%22middle%22 dy=%22.3em%22 fill=%22%23DC2626%22 font-size=%2220%22%3EDrama Platform%3C/text%3E%3C/svg%3E'">
                <div class="blog-card-content">
                    <span class="blog-card-category">${blog.category}</span>
                    <h3 class="blog-card-title">${blog.title}</h3>
                    <p class="blog-card-excerpt">${blog.excerpt}</p>
                    <div class="blog-card-meta">
                        <span class="blog-card-date">
                            📅 ${date}
                        </span>
                        <span class="blog-card-views">
                            👁️ ${blog.views} views
                        </span>
                    </div>
                </div>
            </div>
        `;
    }).join('');

    blogGrid.innerHTML = html;
}

// Render pagination
function renderPagination() {
    const pagination = document.getElementById('blogPagination');
    
    if (totalPages <= 1) {
        pagination.innerHTML = '';
        return;
    }

    const html = `
        <button class="pagination-btn" onclick="changePage(${currentPage - 1})" ${currentPage <= 1 ? 'disabled' : ''}>
            ← Previous
        </button>
        <span class="pagination-info">Page ${currentPage} of ${totalPages}</span>
        <button class="pagination-btn" onclick="changePage(${currentPage + 1})" ${currentPage >= totalPages ? 'disabled' : ''}>
            Next →
        </button>
    `;

    pagination.innerHTML = html;
}

// Change page
function changePage(page) {
    if (page < 1 || page > totalPages) return;
    currentPage = page;
    loadBlogs();
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Show no results message
function showNoResults() {
    const blogGrid = document.getElementById('blogGrid');
    blogGrid.innerHTML = `
        <div class="no-results">
            <div class="no-results-icon">🔍</div>
            <h3>No articles found</h3>
            <p>${searchQuery ? 'Try adjusting your search terms' : 'Check back later for new content'}</p>
        </div>
    `;
    document.getElementById('blogPagination').innerHTML = '';
}

// Show error message
function showError(message) {
    const blogGrid = document.getElementById('blogGrid');
    blogGrid.innerHTML = `
        <div class="error-message-box">
            <h2>Oops!</h2>
            <p>${message}</p>
            <button class="button" onclick="loadBlogs()">Try Again</button>
        </div>
    `;
}
