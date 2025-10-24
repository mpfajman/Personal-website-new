# Database Integration for Personal Website

This document describes the database integration added to the personal website project.

## Files Added/Modified

### New Files
- `DAL.py` - Data Access Layer for database operations
- `templates/add_project.html` - Form to add new projects
- `populate_database.py` - Script to populate database with initial data
- `projects.db` - SQLite database file (created automatically)

### Modified Files
- `app.py` - Added database routes and functionality
- `templates/projects.html` - Updated to display projects from database
- `static/styles.css` - Added styles for table and form components

## Database Schema

The `projects` table has the following structure:
- `id` - Primary key (auto-increment)
- `title` - Project title (required)
- `description` - Project description (required)
- `image_filename` - Name of image file in static/images folder (required)
- `technologies` - Technologies used (optional)
- `project_url` - Project URL (optional)
- `created_at` - Timestamp when project was created
- `updated_at` - Timestamp when project was last updated

## How to Use

### 1. Running the Application
```bash
python app.py
```

### 2. Viewing Projects
- Navigate to `/projects` to see all projects in a table format
- Projects are displayed with images, titles, descriptions, technologies, and links

### 3. Adding New Projects
- Navigate to `/add_project` to access the form
- Fill in the required fields (Title, Description, Image Filename)
- Add optional fields (Technologies, Project URL)
- Click "Add Project" to save

### 4. Image Management
- Place project images in the `static/images/` folder
- Enter the exact filename (including extension) in the form
- Images will be displayed in the projects table

## Database Operations

The `DAL.py` file provides the following methods:
- `get_all_projects()` - Retrieve all projects
- `get_project_by_id(id)` - Get a specific project
- `add_project(title, description, image_filename, technologies, project_url)` - Add new project
- `update_project(id, ...)` - Update existing project
- `delete_project(id)` - Delete project
- `search_projects(term)` - Search projects

## Initial Data

Run `python populate_database.py` to populate the database with sample projects based on the existing HTML content.

## Features

- ✅ SQLite database integration
- ✅ Projects displayed in HTML table format
- ✅ Form to add new projects
- ✅ Image display from static folder
- ✅ Responsive design
- ✅ Flash messages for user feedback
- ✅ Form validation
- ✅ Mobile-friendly interface

## Next Steps

Future enhancements could include:
- Image upload functionality
- Project editing capabilities
- Project deletion
- Search functionality
- Categories/tags for projects
- Admin authentication
