from flask import Flask, render_template, request, redirect, url_for, flash
from DAL import ProjectDAL

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a random secret key

# Initialize the database
db = ProjectDAL()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/projects')
def projects():
    projects = db.get_all_projects()
    return render_template('projects.html', projects=projects)

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

@app.route('/add_project', methods=['GET', 'POST'])
def add_project():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        image_filename = request.form.get('image_filename')
        technologies = request.form.get('technologies')
        project_url = request.form.get('project_url')
        
        if title and description and image_filename:
            try:
                project_id = db.add_project(title, description, image_filename, technologies, project_url)
                flash('Project added successfully!', 'success')
                return redirect(url_for('projects'))
            except Exception as e:
                flash(f'Error adding project: {str(e)}', 'error')
        else:
            flash('Please fill in all required fields (Title, Description, and Image Filename)', 'error')
    
    return render_template('add_project.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
