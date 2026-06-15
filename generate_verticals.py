import os

def get_template(title, hero_title, hero_subtitle, feature1, feature2, feature3, image_src):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title} - StreamPlay Drama Platform</title>
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0">
    <meta name="description" content="Launch your {title} with StreamPlay.">
    <meta name="theme-color" content="#1E1233">
    <link rel="icon" href="assets/images/drama-icon.png" type="image/x-icon">
    <link rel="stylesheet" href="https://use.typekit.net/nuo5dim.css">
    <link rel="stylesheet" href="assets/css/style.css">
    <link rel="stylesheet" href="assets/css/mobile-responsive.css">
    <style>
        .uc-hero {{
            padding-top: 140px;
            padding-bottom: 80px;
            background: radial-gradient(circle at center top, #2d0a4e 0%, #090910 70%);
            border-bottom: 1px solid rgba(255,255,255,0.05);
            text-align: center;
        }}
        .uc-title {{
            font-size: 3.5rem;
            line-height: 1.2;
            margin-bottom: 20px;
            color: #fff;
        }}
        .uc-subtitle {{
            font-size: 1.25rem;
            color: #9CA3AF;
            max-width: 800px;
            margin: 0 auto;
            line-height: 1.6;
        }}
        .uc-main {{
            padding: 80px 0;
            background-color: #07070B;
        }}
        .uc-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 30px;
            margin-top: 50px;
        }}
        .uc-card {{
            background: rgba(10, 18, 50, 0.4);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 40px 30px;
            text-align: left;
        }}
        .uc-card h3 {{
            color: #fff;
            font-size: 1.3rem;
            margin-bottom: 15px;
        }}
        .uc-card p {{
            color: #D1D5DB;
            font-size: 1.05rem;
            line-height: 1.6;
        }}
    </style>
</head>
<body class="home-header drama-menu">

    <!-- Header Starts -->
    <header class="header" id="drama-menu-new">
        <div class="header-section">
            <div class="container clearfix">
                <div class="logo-image">
                    <a class="logo" href="index.html">
                        <img width="280" height="54" src="assets/images/logo.png" class="fixed-logo" alt="Drama Platform Logo">
                    </a>
                </div>

                <div class="hamburger" id="ham">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>

                <nav class="nav nav-menu" id="nav">
                    <div class="nav-center">
                        <a id="home-nav" class="nav-tab" href="index.html" title="Home">Home</a>
                        <div class="nav-dropdown">
                            <a id="features-nav" class="nav-tab" href="features.html" title="Features">Features</a>
                            <div class="nav-dropdown-content">
                                <a href="features.html">All Features</a>
                                <a href="usecase-kdrama.html">K-Drama Platforms</a>
                                <a href="usecase-turkish.html">Turkish Platforms</a>
                                <a href="usecase-arabic.html">Arabic Platforms</a>
                                <a href="usecase-indie.html">Indie Platforms</a>
                            </div>
                        </div>
                        <a id="pricing-nav" class="nav-tab" href="pricing.html" title="Pricing">Pricing</a>
                        <a id="blog-nav" class="nav-tab" href="blogs.html" title="Blog">Blog</a>
                        <a id="testimonials-nav" class="nav-tab" href="testimonials.html" title="Testimonials">Testimonials</a>
                    </div>
                    <div class="expert">
                        <a rel="nofollow" class="request-demo" href="contact.html" title="Contact Sales">Contact Sales</a>
                        <a rel="nofollow" id="sales-header" href="demo.html" title="Watch Demo">Watch Demo</a>
                    </div>
                </nav>
            </div>
        </div>
    </header>

    <main>
        <section class="uc-hero">
            <div class="container">
                <h1 class="uc-title">{hero_title}</h1>
                <p class="uc-subtitle">{hero_subtitle}</p>
                <div style="margin-top: 40px; margin-bottom: 60px;">
                    <a href="demo.html" class="btn-primary" style="padding: 14px 32px; font-size: 1.1rem; border-radius: 8px;">Watch Platform Demo</a>
                </div>
                <div>
                    <img src="{image_src}" alt="Platform Template Preview" style="max-width: 400px; width: 100%; margin: 0 auto; border-radius: 12px; box-shadow: 0 20px 50px rgba(0,0,0,0.6); border: 1px solid rgba(255,255,255,0.1);">
                </div>
            </div>
        </section>

        <section class="uc-main">
            <div class="container">
                <div class="section-head text-center">
                    <h2 class="section-title">Built for Your <span>Audience</span></h2>
                </div>
                <div class="uc-grid">
                    <div class="uc-card">
                        <h3>{feature1['title']}</h3>
                        <p>{feature1['desc']}</p>
                    </div>
                    <div class="uc-card">
                        <h3>{feature2['title']}</h3>
                        <p>{feature2['desc']}</p>
                    </div>
                    <div class="uc-card">
                        <h3>{feature3['title']}</h3>
                        <p>{feature3['desc']}</p>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col brand-col">
                    <img src="assets/images/logo.png" alt="StreamPlay Drama Logo" class="footer-logo">
                    <p class="brand-desc">Launch, host, and scale your dedicated OTT drama streaming service with 100% platform ownership and zero revenue sharing.</p>
                </div>
                <div class="footer-col">
                    <h4>Resources</h4>
                    <ul class="footer-links">
                        <li><a href="index.html">Home</a></li>
                        <li><a href="features.html">Features</a></li>
                        <li><a href="pricing.html">Pricing</a></li>
                        <li><a href="contact.html">Contact Sales</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p class="copyright">&copy; 2026 StreamPlay Drama Play. All rights reserved.</p>
            </div>
        </div>
    </footer>
    <script src="assets/js/main.js"></script>
</body>
</html>"""


pages = [
    {
        'filename': 'usecase-kdrama.html',
        'title': 'K-Drama Streaming Platforms',
        'hero_title': 'Launch the Ultimate <span class="highlight-text">K-Drama</span> Streaming App',
        'hero_subtitle': 'Capitalize on the Hallyu wave. Deploy a dedicated K-Drama platform globally with multi-language subtitle pipelines, AI-driven watchlists, and robust DRM.',
        'f1': {'title': 'Multi-Language Subtitles', 'desc': 'Automated pipelines to manage English, Spanish, and regional subtitles across thousands of episodes seamlessly.'},
        'f2': {'title': 'Idol & Actor Profiles', 'desc': 'Rich metadata tagging allows fans to browse content by their favorite K-Drama stars and idols.'},
        'f3': {'title': 'Global Delivery', 'desc': 'Reach global audiences with low-latency Edge CDNs tailored for high-demand simulcast releases.'},
        'image': 'assets/images/k-drama.png'
    },
    {
        'filename': 'usecase-turkish.html',
        'title': 'Turkish Drama Platforms',
        'hero_title': 'Globalize Your <span class="highlight-text">Turkish Drama</span> Catalog',
        'hero_subtitle': 'Turkish Dizi are taking the world by storm. Reach viewers in Latin America, MENA, and Europe with a localized streaming super app.',
        'f1': {'title': 'Multi-Audio Dubbing', 'desc': 'Easily manage and stream multiple audio tracks (Spanish, Arabic, English) for global syndication.'},
        'f2': {'title': 'Long-Form Series CMS', 'desc': 'Built to handle 100+ episode seasons with bulk ingestion and automated next-episode playback.'},
        'f3': {'title': 'Regional Payment Gateways', 'desc': 'Monetize globally with localized currencies and payment integrations across LATAM and MENA.'},
        'image': 'assets/images/turkish-drama.png'
    },
    {
        'filename': 'usecase-arabic.html',
        'title': 'Arabic Series Platforms',
        'hero_title': 'Premium OTT for <span class="highlight-text">Arabic Series</span>',
        'hero_subtitle': 'From Ramadan exclusives to classic Egyptian cinema, deliver a premium viewing experience with full RTL support and high-end DRM.',
        'f1': {'title': 'Full RTL Interface', 'desc': 'Native Right-to-Left design support across Web, iOS, and Smart TV applications.'},
        'f2': {'title': 'Ramadan Premiere Scheduling', 'desc': 'Time-embargo capabilities for dropping episodes exactly on schedule during peak viewing seasons.'},
        'f3': {'title': 'Advanced Geoblocking', 'desc': 'Enforce complex territorial licensing agreements with pinpoint IP whitelisting and VPN detection.'},
        'image': 'assets/images/saudi-drama.png'
    },
    {
        'filename': 'usecase-indie.html',
        'title': 'Indie Web Series Platforms',
        'hero_title': 'Monetize Your <span class="highlight-text">Indie Web Series</span>',
        'hero_subtitle': 'Don\'t give up 40% to YouTube. Own your audience, collect subscriber data, and keep 100% of your revenue with a dedicated platform.',
        'f1': {'title': 'Zero Revenue Share', 'desc': 'Keep every dollar you earn. Our fixed-fee B2B model ensures you scale without penalties.'},
        'f2': {'title': 'Direct Audience Ownership', 'desc': 'Access first-party data, emails, and viewing analytics to market directly to your fans.'},
        'f3': {'title': 'Flexible Monetization', 'desc': 'Offer fans SVOD subscriptions, one-time TVOD purchases, or ad-supported free tiers (AVOD).'},
        'image': 'assets/images/action-2.png'
    }
]

for p in pages:
    html = get_template(p['title'], p['hero_title'], p['hero_subtitle'], p['f1'], p['f2'], p['f3'], p['image'])
    with open(p['filename'], 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Created {p['filename']}")
