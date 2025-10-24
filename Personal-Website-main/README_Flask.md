# Flask Personal Website

This is a Flask version of Makayla Fajman's personal portfolio website.

## Setup Instructions

1. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment:**
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask Application:**
   ```bash
   python app.py
   ```

5. **Open in Browser:**
   Navigate to `http://127.0.0.1:5000/` to view the website.

## Website Structure

- **Home** (`/`) - Welcome page with introduction
- **About** (`/about`) - Personal information and photo gallery
- **Resume** (`/resume`) - Resume PDF viewer and download
- **Projects** (`/projects`) - Portfolio of past projects
- **Contact** (`/contact`) - Contact information and form
- **Thank You** (`/thankyou`) - Form submission confirmation

## Features

- Responsive design with CSS styling
- Interactive photo gallery with JavaScript
- Contact form with validation
- PDF resume viewer
- Consistent navigation across all pages
- Mobile-friendly design

## Files Structure

```
flask_app/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/            # HTML templates
│   ├── base.html        # Base template with navigation
│   ├── index.html       # Home page
│   ├── about.html       # About page with gallery
│   ├── contact.html     # Contact page with form
│   ├── projects.html    # Projects showcase
│   ├── resume.html      # Resume viewer
│   └── thankyou.html    # Thank you page
└── static/              # Static files
    ├── styles.css       # CSS styling
    └── images/          # All images and PDFs
```
