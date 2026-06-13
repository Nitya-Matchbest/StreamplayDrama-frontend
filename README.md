# 🎬 Drama Platform - Complete Streaming Solution

A premium drama streaming platform built with HTML, CSS, JavaScript, PHP, and Node.js backend. Features the **Crimson Cinema** theme with a professional OTT platform interface.

## 📁 Project Structure

```
drama-frontend/
├── assets/
│   ├── css/
│   │   ├── style.css                 # Main stylesheet with Crimson Cinema theme
│   │   └── mobile-responsive.css     # Mobile responsive styles
│   ├── js/
│   │   └── main.js                   # Frontend JavaScript functionality
│   └── images/                       # Image assets (upload your images here)
├── drama-backend/                    # Backend Node.js server
│   ├── blog/
│   │   ├── config/                   # Database & upload configuration
│   │   ├── controllers/              # API controllers
│   │   ├── models/                   # MongoDB models
│   │   └── routes/                   # API routes
│   ├── public/uploads/blog/          # Uploaded images storage
│   ├── server.js                     # Main server file
│   ├── package.json                  # Backend dependencies
│   └── .env                          # Environment variables
├── drama-admin/                      # Admin panel for blog management
│   ├── css/
│   │   ├── admin.css                 # Admin panel styles
│   │   └── manage.css                # Manage blogs styles
│   ├── js/
│   │   ├── admin.js                  # Create blog functionality
│   │   └── manage.js                 # Manage blogs functionality
│   ├── index.html                    # Create blog page
│   └── manage.html                   # Manage blogs page
├── index.html                        # Homepage
├── contact.html                      # Contact page
├── blogs.html                        # Blogs listing page (create this)
├── blog-detail.html                  # Single blog page (create this)
├── send-email.php                    # Contact form email handler
└── README.md                         # This file
```

## 🎨 Crimson Cinema Theme Colors

- **Midnight Navy**: `#111827` - Background
- **Crimson Red**: `#DC2626` - Primary buttons & accents
- **Pure White**: `#FFFFFF` - Text & secondary elements
- **Amber Gold**: `#F59E0B` - Highlights & hover states

## 🚀 Quick Start

### 1. Backend Setup

```bash
cd drama-backend
npm install
npm start
```

Backend runs on: `http://localhost:5001`

### 2. Frontend Setup

Simply open `index.html` in your browser or use a local server:

```bash
# Using Python
python -m http.server 8000

# Using PHP
php -S localhost:8000

# Using Node.js http-server
npx http-server
```

### 3. Admin Panel Setup

1. Make sure backend is running
2. Open `drama-admin/index.html` in your browser
3. Create your first blog post!

## 📊 Database Configuration

The backend uses the **same MongoDB database** as StreamPlay:

- **Host**: 43.205.217.221:27030
- **Database**: streamplay
- **Collection**: dramablogs
- **Auth**: Already configured in `.env`

No additional database setup required!

## 🔧 Configuration

### Update Backend URL (When Deploying)

Update these files with your production backend URL:

**drama-admin/js/admin.js:**
```javascript
const API_BASE = 'https://your-backend-url.com';
```

**drama-admin/js/manage.js:**
```javascript
const API_BASE = 'https://your-backend-url.com';
```

### Update Email Recipient

**send-email.php:**
```php
$to = 'your-email@example.com';  // Line 38
```

## 📝 Features

### Frontend
- ✅ Responsive design (mobile, tablet, desktop)
- ✅ Cinematic Crimson Cinema theme
- ✅ Smooth animations and transitions
- ✅ Contact form with PHP email
- ✅ Blog listing and detail pages
- ✅ SEO-friendly structure

### Backend (Node.js + Express)
- ✅ RESTful API
- ✅ MongoDB integration
- ✅ Image upload with GridFS
- ✅ Blog CRUD operations
- ✅ Category filtering
- ✅ Search functionality
- ✅ Pagination support

### Admin Panel
- ✅ Create blog posts
- ✅ Edit existing posts
- ✅ Delete posts
- ✅ Image upload
- ✅ Search and filter
- ✅ Category management
- ✅ Tag support

## 🖼️ Adding Images

Place your images in the `assets/images/` folder. Required images:

**Logos & Branding:**
- `drama-logo-transparent.png` (280x54px)
- `drama-icon.png` (favicon)

**Hero & Features:**
- `drama-hero.png` (1428x499px)
- `ownership-platform.png`
- `revenue-graph.png`
- `revenue-chart.png`
- `customization-cursor.png`
- `customization-ui.png`
- `customization-preview.png`
- `branding-logos.png`
- `hosting-infrastructure.png`
- `whitelabel-platform.png`

**Content Management:**
- `cms-dashboard.png`
- `video-player.png`
- `drm-security.png`
- `analytics-dashboard.png`

**Monetization Models:**
- `subscription-model.png`
- `ad-supported-model.png`
- `ppv-model.png`
- `hybrid-model.png`
- `catchup-model.png`
- `premium-tiers.png`

## 📱 Pages Structure

### Homepage (`index.html`)
- Hero banner with value proposition
- Platform ownership section
- Features showcase
- Monetization models
- CTA sections

### Contact (`contact.html`)
- Contact form with validation
- PHP email integration
- Responsive design

### Blogs (`blogs.html`) - *To be created*
- Blog listing with categories
- Search and filter
- Pagination
- Category badges

### Blog Detail (`blog-detail.html`) - *To be created*
- Full blog content
- Related articles
- Social sharing
- Comments section

## 🔌 API Endpoints

### Blogs
```
GET    /api/blogs                    # Get all blogs
GET    /api/blogs/id/:id             # Get blog by ID
GET    /api/blogs/slug/:slug         # Get blog by slug
POST   /api/blogs                    # Create blog
PUT    /api/blogs/:id                # Update blog
DELETE /api/blogs/:id                # Delete blog
GET    /api/blogs/categories         # Get categories
```

### Upload
```
POST   /api/upload                   # Upload image
GET    /api/image/:filename          # Get image
```

## 🌐 Deployment

### Frontend Deployment
Upload to any static hosting:
- Netlify
- Vercel
- GitHub Pages
- AWS S3 + CloudFront

### Backend Deployment
Deploy to:
- Heroku
- AWS EC2
- DigitalOcean
- Render.com

Update `API_BASE` in admin JS files after deployment.

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3 (with custom properties)
- Vanilla JavaScript
- Responsive design

### Backend
- Node.js
- Express.js
- MongoDB with Mongoose
- Multer (file uploads)
- CORS
- Slugify

### Admin Panel
- HTML/CSS/JavaScript
- Fetch API for HTTP requests
- Modern ES6+ JavaScript

## 📄 License

This project is based on StreamPlay and adapted for drama streaming.

## 🤝 Support

For issues or questions:
1. Check backend logs: `npm run dev` in drama-backend folder
2. Check browser console for frontend errors
3. Verify MongoDB connection in backend logs
4. Ensure all API endpoints are accessible

## 🎯 Next Steps

1. **Add Images**: Place all required images in `assets/images/`
2. **Create Blog Pages**: Build `blogs.html` and `blog-detail.html`
3. **Test Backend**: Run backend and test all API endpoints
4. **Test Admin Panel**: Create and manage sample blog posts
5. **Deploy**: Deploy frontend and backend to production

---

**Built with ❤️ for Drama Streaming Platforms**
