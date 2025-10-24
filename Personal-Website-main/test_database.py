import pytest
import sqlite3
import os
from DAL import ProjectDAL

def test_database_connection():
    """Test that database connection works"""
    db = ProjectDAL()
    assert db is not None

def test_database_initialization():
    """Test that database initializes properly"""
    db = ProjectDAL('test.db')
    # Test that we can get projects (should return empty list initially)
    projects = db.get_all_projects()
    assert isinstance(projects, list)
    
    # Clean up test database
    if os.path.exists('test.db'):
        os.remove('test.db')

def test_add_project():
    """Test adding a project to database"""
    db = ProjectDAL('test.db')
    project_id = db.add_project(
        title="Test Project",
        description="Test Description", 
        image_filename="test.jpg",
        technologies="Python, Flask",
        project_url="https://test.com"
    )
    assert project_id is not None
    
    # Clean up test database
    if os.path.exists('test.db'):
        os.remove('test.db')

def test_get_projects():
    """Test retrieving projects from database"""
    db = ProjectDAL('test.db')
    # Add a test project first
    db.add_project("Test", "Description", "test.jpg")
    
    projects = db.get_all_projects()
    assert len(projects) >= 1
    assert projects[0]['title'] == "Test"
    
    # Clean up test database
    if os.path.exists('test.db'):
        os.remove('test.db')

def test_search_projects():
    """Test searching projects in database"""
    db = ProjectDAL('test.db')
    # Add a test project first
    db.add_project("Python Web App", "A Flask application", "app.jpg", "Python, Flask")
    
    # Search for projects
    results = db.search_projects("Python")
    assert len(results) >= 1
    assert "Python" in results[0]['title'] or "Python" in results[0]['technologies']
    
    # Clean up test database
    if os.path.exists('test.db'):
        os.remove('test.db')

def test_update_project():
    """Test updating a project in database"""
    db = ProjectDAL('test.db')
    # Add a test project first
    project_id = db.add_project("Original Title", "Original Description", "original.jpg")
    
    # Update the project
    success = db.update_project(
        project_id, 
        "Updated Title", 
        "Updated Description", 
        "updated.jpg",
        "Python, Flask, SQLite",
        "https://updated.com"
    )
    assert success is True
    
    # Verify the update
    project = db.get_project_by_id(project_id)
    assert project['title'] == "Updated Title"
    assert project['description'] == "Updated Description"
    
    # Clean up test database
    if os.path.exists('test.db'):
        os.remove('test.db')

def test_delete_project():
    """Test deleting a project from database"""
    db = ProjectDAL('test.db')
    # Add a test project first
    project_id = db.add_project("To Delete", "This will be deleted", "delete.jpg")
    
    # Delete the project
    success = db.delete_project(project_id)
    assert success is True
    
    # Verify deletion
    project = db.get_project_by_id(project_id)
    assert project is None
    
    # Clean up test database
    if os.path.exists('test.db'):
        os.remove('test.db')
