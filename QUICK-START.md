# 🚀 Drama Platform - Quick Start Guide

## ⚡ Get Running in 3 Minutes

### Step 1: Install Backend Dependencies (1 minute)

```bash
cd drama-frontend/drama-backend
npm install
```

### Step 2: Start Backend Server (30 seconds)

```bash
npm start
```

You should see:
```
✅ MongoDB Connected: 43.205.217.221
📦 Database: streamplay
📊 Collection: dramablogs
🚀 Drama Backend Server is running on http://localhost:5001
```

✅ **Backend is ready!**

### Step 3: Open Admin Panel (30 seconds)

1. Open your browser
2. Navigate to: `drama-frontend/drama-admin/index.html`
3. You'll see the blog creation form

✅ **Admin panel is ready!**

### Step 4: Create Your First Blog Post (1 minute)

1. Fill in the title: "Welcome to Drama Platform"
2. Add excerpt: "Your journey to premium drama streaming starts here"
3. Select category: "Latest Article"
4. Upload an image (or skip for now)
5. Add a content section
6. Click "Create Blog Post"

✅ **First blog created!**

---

## 🎯 What to Do Next

### View Your Website
Open `drama-frontend/index.html` in your browser

### View Your Blog Posts
Open `drama-frontend/blogs.html` in your browser

### Test Contact Form
```bash
cd drama-frontend
php -S localhost:8000
# Then visit: http://localhost:8000/contact.html
```

### Add Images
Place your images in `drama-frontend/assets/images/`

---

## 🔧 Quick Configuration

### Change Email Recipient
Edit `drama-frontend/send-email.php` line 38:
```php
$to = 'your-email@example.com';
```

### Update Backend URL (for deployment)
Edit these 4 files and change line 2 or 6:
- `drama-admin/js/admin.js`
- `drama-admin/js/manage.js`
- `assets/js/blogs.js`
- `assets/js/blog-detail.js`

From:
```javascript
const API_BASE = 'http://localhost:5001';
```

To:
```javascript
const API_BASE = 'https://your-backend-url.com';
```

---

## 📂 Project Structure

```
drama-frontend/
├── index.html              ← Homepage
├── contact.html            ← Contact form
├── blogs.html              ← Blog listing
├── blog-detail.html        ← Single blog
├── assets/                 ← Styles & scripts
├── drama-backend/          ← Backend server (Port 5001)
└── drama-admin/            ← Admin panel
    ├── index.html          ← Create blog
    └── manage.html         ← Manage blogs
```

---

## 🎨 Theme Colors

| Color | Hex | Usage |
|-------|-----|-------|
| Midnight Navy | #111827 | Background |
| Crimson Red | #DC2626 | Buttons |
| Pure White | #FFFFFF | Text |
| Amber Gold | #F59E0B | Accents |

---

## 🗄️ Database Info

**Already configured - no setup needed!**

- Database: streamplay
- Collection: dramablogs
- Port: 27030

---

## ✅ Quick Test Checklist

- [ ] Backend running on port 5001
- [ ] Admin panel opens without errors
- [ ] Can create a blog post
- [ ] Can view blog in "Manage Blogs"
- [ ] Frontend homepage loads
- [ ] Blog listing page works
- [ ] Can view single blog post
- [ ] Contact form displays

---

## 🚨 Common Issues

**Backend won't start?**
```bash
# Make sure you're in the right folder
cd drama-frontend/drama-backend
npm install
npm start
```

**Can't connect to backend from admin panel?**
- Check backend is running on http://localhost:5001
- Open browser console (F12) to see errors

**Contact form not working?**
- Requires PHP server
- Use: `php -S localhost:8000`

**Images not showing?**
- Add images to `assets/images/` folder
- Or use placeholders (already configured)

---

## 📱 Pages Available

✅ Homepage (`index.html`)
✅ Contact Page (`contact.html`)
✅ Blog Listing (`blogs.html`)
✅ Blog Detail (`blog-detail.html`)
✅ Admin - Create Blog (`drama-admin/index.html`)
✅ Admin - Manage Blogs (`drama-admin/manage.html`)

---

## 🎯 Key Features

✅ Crimson Cinema theme (Red/Navy)
✅ Responsive design
✅ Blog management system
✅ Image upload
✅ Search & filter
✅ Category system
✅ Contact form
✅ SEO-friendly URLs
✅ View counter
✅ Related articles

---

## 📝 Need More Help?

Read the detailed guides:
- **README.md** - Full documentation
- **SETUP-GUIDE.md** - Detailed setup
- **PROJECT-SUMMARY.md** - Complete overview

---

## 🎬 You're All Set!

Your Drama platform is ready to use. Enjoy building your streaming empire!

**Backend**: http://localhost:5001
**Admin**: drama-admin/index.html
**Website**: index.html

🎭 Happy Streaming! 🎭
