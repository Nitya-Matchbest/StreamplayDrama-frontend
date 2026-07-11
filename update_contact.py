import re

with open('contact.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the CSS
new_css = '''        .contact-section {
            padding: 120px 0 80px;
            background: var(--background);
        }
        
        .contact-container {
            max-width: 1000px;
            margin: 0 auto;
            background: #0A1232;
            border-radius: 15px;
            border: 1px solid rgba(255, 255, 255, 0.08);
            display: grid;
            grid-template-columns: 1fr 1fr;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }
        
        .form-content {
            padding: 50px;
        }

        .image-content {
            background-image: linear-gradient(rgba(10, 18, 50, 0.6), rgba(130, 42, 238, 0.4)), url('assets/images/Background.png');
            background-size: cover;
            background-position: center;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 40px;
            text-align: center;
        }

        .image-content h2 {
            color: #fff;
            font-size: 28px;
            font-weight: 700;
            line-height: 1.3;
            text-shadow: 0 4px 10px rgba(0,0,0,0.5);
        }
        
        .contact-title {
            font-size: 32px;
            font-weight: 700;
            color: #fff;
            margin-bottom: 15px;
        }
        
        .contact-subtitle {
            font-size: 14px;
            color: #9CA3AF;
            margin-bottom: 30px;
            line-height: 1.6;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 8px;
            color: #fff;
            font-weight: 600;
            font-size: 14px;
        }
        
        .form-group input,
        .form-group textarea,
        .form-group select {
            width: 100%;
            padding: 12px 15px;
            background: #111520;
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 8px;
            color: #fff;
            font-size: 14px;
            transition: all 0.3s;
        }
        
        .form-group input:focus,
        .form-group textarea:focus,
        .form-group select:focus {
            border-color: #822AEE;
            outline: none;
        }
        
        .form-group textarea {
            min-height: 100px;
            resize: vertical;
        }
        
        .form-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }
        
        .submit-btn {
            width: 100%;
            padding: 15px;
            background: #4B1A8A; /* Dark purple default */
            color: #FFFFFF;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
            margin-top: 10px;
        }
        
        .submit-btn:hover {
            background: #822AEE;
            box-shadow: 0 4px 15px rgba(130, 42, 238, 0.4);
        }
        
        .success-message {
            background: #10B981;
            color: #FFFFFF;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
            display: none;
        }
        
        .error-message {
            background: #EF4444;
            color: #FFFFFF;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
            display: none;
        }
        
        @media screen and (max-width: 768px) {
            .contact-container {
                grid-template-columns: 1fr;
            }
            .image-content {
                min-height: 300px;
            }
            .form-content {
                padding: 30px 20px;
            }
            .form-row {
                grid-template-columns: 1fr;
            }
        }'''

# Replace CSS
content = re.sub(r'\.contact-section \{.*?(?=\s*</style>)', new_css, content, flags=re.DOTALL)

# 2. Update HTML
new_html = '''<section class="contact-section">
    <div class="container">
        <div class="contact-container">
            <div class="form-content">
                <h1 class="contact-title">Get a Demo Today</h1>
                <p class="contact-subtitle">For further queries, please complete form, will contact you<br>within 24 hours to help with the CMS and launch.</p>
                
                <div class="success-message" id="successMessage">
                    ? Thank you! Your message has been sent successfully. We'll get back to you soon.
                </div>
                
                <div class="error-message" id="errorMessage">
                    ? Something went wrong. Please try again.
                </div>
                
                <form id="contactForm">
                    <div class="form-row">
                        <div class="form-group">
                            <label for="firstName">First Name</label>
                            <input type="text" id="firstName" name="firstName" required placeholder="John">
                        </div>
                        <div class="form-group">
                            <label for="email">Work Email</label>
                            <input type="email" id="email" name="email" required placeholder="john@company.com">
                        </div>
                    </div>
                    
                    <div class="form-group">
                        <label for="industry">Industry</label>
                        <select id="industry" name="industry" required>
                            <option value="Broadcasting">Broadcasting</option>
                            <option value="Entertainment">Entertainment</option>
                            <option value="Education">Education</option>
                            <option value="Other">Other</option>
                        </select>
                    </div>
                    
                    <div class="form-group">
                        <label for="message">Message</label>
                        <textarea id="message" name="message" required placeholder="How can I help you?"></textarea>
                    </div>
                    
                    <button type="submit" class="submit-btn" id="submitBtn">
                        Request Demo
                    </button>
                </form>
            </div>
            <div class="image-content">
                <h2>Trusted by leading<br>media organizations</h2>
            </div>
        </div>
    </div>
</section>'''

content = re.sub(r'<section class="contact-section">.*?</section>', new_html, content, flags=re.DOTALL)

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(content)

