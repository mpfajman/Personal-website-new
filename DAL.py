import sqlite3
import os
from datetime import datetime

class ProjectDAL:
    def __init__(self, db_path='projects.db'):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize the database and create the projects table if it doesn't exist"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create projects table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                image_filename TEXT NOT NULL,
                technologies TEXT,
                project_url TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def get_all_projects(self):
        """Retrieve all projects from the database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, title, description, image_filename, technologies, project_url, created_at, updated_at
            FROM projects
            ORDER BY created_at DESC
        ''')
        
        projects = cursor.fetchall()
        conn.close()
        
        # Convert to list of dictionaries for easier template usage
        project_list = []
        for project in projects:
            project_dict = {
                'id': project[0],
                'title': project[1],
                'description': project[2],
                'image_filename': project[3],
                'technologies': project[4],
                'project_url': project[5],
                'created_at': project[6],
                'updated_at': project[7]
            }
            project_list.append(project_dict)
        
        return project_list
    
    def get_project_by_id(self, project_id):
        """Retrieve a specific project by ID"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, title, description, image_filename, technologies, project_url, created_at, updated_at
            FROM projects
            WHERE id = ?
        ''', (project_id,))
        
        project = cursor.fetchone()
        conn.close()
        
        if project:
            return {
                'id': project[0],
                'title': project[1],
                'description': project[2],
                'image_filename': project[3],
                'technologies': project[4],
                'project_url': project[5],
                'created_at': project[6],
                'updated_at': project[7]
            }
        return None
    
    def add_project(self, title, description, image_filename, technologies=None, project_url=None):
        """Add a new project to the database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO projects (title, description, image_filename, technologies, project_url)
            VALUES (?, ?, ?, ?, ?)
        ''', (title, description, image_filename, technologies, project_url))
        
        project_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return project_id
    
    def update_project(self, project_id, title, description, image_filename, technologies=None, project_url=None):
        """Update an existing project"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE projects 
            SET title = ?, description = ?, image_filename = ?, technologies = ?, project_url = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        ''', (title, description, image_filename, technologies, project_url, project_id))
        
        rows_affected = cursor.rowcount
        conn.commit()
        conn.close()
        
        return rows_affected > 0
    
    def delete_project(self, project_id):
        """Delete a project from the database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM projects WHERE id = ?', (project_id,))
        
        rows_affected = cursor.rowcount
        conn.commit()
        conn.close()
        
        return rows_affected > 0
    
    def search_projects(self, search_term):
        """Search projects by title or description"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, title, description, image_filename, technologies, project_url, created_at, updated_at
            FROM projects
            WHERE title LIKE ? OR description LIKE ? OR technologies LIKE ?
            ORDER BY created_at DESC
        ''', (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))
        
        projects = cursor.fetchall()
        conn.close()
        
        # Convert to list of dictionaries
        project_list = []
        for project in projects:
            project_dict = {
                'id': project[0],
                'title': project[1],
                'description': project[2],
                'image_filename': project[3],
                'technologies': project[4],
                'project_url': project[5],
                'created_at': project[6],
                'updated_at': project[7]
            }
            project_list.append(project_dict)
        
        return project_list
