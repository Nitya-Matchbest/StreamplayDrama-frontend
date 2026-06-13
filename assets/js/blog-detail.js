/* =============================================================
   Drama Platform - Blog Detail JavaScript
   ============================================================= */

// API Configuration - Update when deploying
const API_BASE = ' https://streamplaydrama-backend.onrender.com';
const API_URL = `${API_BASE}/api/blogs`;

// Get slug from URL
const urlParams = new URLSearchParams(window.location.search);
const blogSlug = urlParams.get('slug');

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    if (blogSlug) {
        loadBlogPost();
    } else {
        showError('No blog post specified');
    }
});

// Load blog post
async function loadBlogPost() {
    const blogContent = document.getElementById('blogContent');
    
    try {
        const response = await fetch(`${API_URL}/slug/${blogSlug}`);
        const data = await response.json();

        if (data.success && data.data) {
            renderBlogPost(data.data);
            
            // Load related articles if available
            if (data.data.relatedArticles && data.data.relatedArticles.length > 0) {
                renderRelatedArticles(data.data.relatedArticles);
            }
        } else {
            showError('Blog post not found');
        }
    } catch (error) {
        console.error('Error loading blog post:', error);
        showError('Failed to load blog post. Please try again later.');
    }
}

// Render blog post
function renderBlogPost(blog) {
    const blogContent = document.getElementById('blogContent');
    
    // Update page title and meta description
    document.getElementById('pageTitle').textContent = blog.title + ' - Drama Platform';
    document.getElementById('pageDescription').setAttribute('content', blog.metaDescription || blog.excerpt);

    // Format date
    const date = new Date(blog.publishDate).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });

    // Handle image URL
    const imageUrl = blog.featuredImage.startsWith('/api/image/') 
        ? API_BASE + blog.featuredImage 
        : blog.featuredImage;

    // Render content — supports new single-body format AND legacy sections array
    let contentHTML = '';
    if (typeof blog.body === 'string' && blog.body.trim()) {
        // New format: one rich HTML body
        contentHTML = `<div class="section-body-content">${blog.body}</div>`;
    } else if (Array.isArray(blog.content) && blog.content.length) {
        // Legacy format: array of {sectionTitle, sectionContent}
        contentHTML = blog.content.map(section => `
            <div class="blog-content-section">
                <h2>${section.sectionTitle}</h2>
                <div class="section-body-content">${section.sectionContent}</div>
            </div>
        `).join('');
    }

    // Render tags
    const tagsHTML = blog.tags && blog.tags.length > 0 ? `
        <div class="blog-tags">
            ${blog.tags.map(tag => `<span class="blog-tag">#${tag}</span>`).join('')}
        </div>
    ` : '';

    const html = `
        <div class="blog-detail-header">
            <span class="blog-detail-category">${blog.category}</span>
            <h1 class="blog-detail-title">${blog.title}</h1>
            <div class="blog-detail-meta">
                <span class="blog-detail-meta-item">
                    📅 ${date}
                </span>
                <span class="blog-detail-meta-item">
                    👁️ ${blog.views} views
                </span>
            </div>
        </div>
        
        <img src="${imageUrl}" alt="${blog.title}" class="blog-detail-image"
             onerror="this.src='data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%22900%22 height=%22500%22%3E%3Crect fill=%22%23374151%22 width=%22900%22 height=%22500%22/%3E%3Ctext x=%2250%25%22 y=%2250%25%22 text-anchor=%22middle%22 dy=%22.3em%22 fill=%22%23DC2626%22 font-size=%2232%22%3EDrama Platform%3C/text%3E%3C/svg%3E'">
        
        <div class="blog-detail-content">
            ${contentHTML}
        </div>
        
        ${tagsHTML}
        
        <div style="text-align: center; margin-top: 50px;">
            <a href="blogs.html" class="button">← Back to Blog</a>
        </div>
    `;

    blogContent.innerHTML = html;
}

// Render related articles
function renderRelatedArticles(articles) {
    const relatedSection = document.getElementById('relatedArticlesSection');
    const relatedGrid = document.getElementById('relatedArticles');
    
    const html = articles.map(blog => {
        const date = new Date(blog.publishDate).toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'short',
            day: 'numeric'
        });

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
                        <span class="blog-card-date">📅 ${date}</span>
                    </div>
                </div>
            </div>
        `;
    }).join('');

    relatedGrid.innerHTML = html;
    relatedSection.style.display = 'block';
}

// Show error message
function showError(message) {
    const blogContent = document.getElementById('blogContent');
    blogContent.innerHTML = `
        <div class="error-message-box">
            <h2>Oops!</h2>
            <p>${message}</p>
            <a href="blogs.html" class="button">← Back to Blog</a>
        </div>
    `;
}
