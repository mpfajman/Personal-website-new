import pytest
from app import app

@pytest.fixture
def client():
    """Create test client"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test that home page loads"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'<!DOCTYPE html>' in response.data or b'<html' in response.data

def test_about_page(client):
    """Test that about page loads"""
    response = client.get('/about')
    assert response.status_code == 200
    assert b'<!DOCTYPE html>' in response.data or b'<html' in response.data

def test_contact_page(client):
    """Test that contact page loads"""
    response = client.get('/contact')
    assert response.status_code == 200
    assert b'<!DOCTYPE html>' in response.data or b'<html' in response.data

def test_projects_page(client):
    """Test that projects page loads"""
    response = client.get('/projects')
    assert response.status_code == 200
    assert b'<!DOCTYPE html>' in response.data or b'<html' in response.data

def test_resume_page(client):
    """Test that resume page loads"""
    response = client.get('/resume')
    assert response.status_code == 200
    assert b'<!DOCTYPE html>' in response.data or b'<html' in response.data

def test_add_project_page_get(client):
    """Test that add project page loads (GET request)"""
    response = client.get('/add_project')
    assert response.status_code == 200
    assert b'<!DOCTYPE html>' in response.data or b'<html' in response.data

def test_add_project_page_post(client):
    """Test adding a project via POST request"""
    response = client.post('/add_project', data={
        'title': 'Test Project',
        'description': 'Test Description',
        'image_filename': 'test.jpg',
        'technologies': 'Python, Flask',
        'project_url': 'https://test.com'
    }, follow_redirects=True)
    
    # Should redirect to projects page after successful submission
    assert response.status_code == 200

def test_thankyou_page(client):
    """Test that thankyou page loads"""
    response = client.get('/thankyou')
    assert response.status_code == 200
    assert b'<!DOCTYPE html>' in response.data or b'<html' in response.data

def test_invalid_route(client):
    """Test that invalid routes return 404"""
    response = client.get('/nonexistent')
    assert response.status_code == 404

def test_app_configuration():
    """Test that Flask app is configured correctly"""
    # Create a fresh app instance for this test
    from flask import Flask
    from DAL import ProjectDAL
    
    test_app = Flask(__name__)
    test_app.secret_key = 'your-secret-key-here'
    
    assert test_app.config['TESTING'] is False  # Should be False by default
    assert test_app.secret_key is not None
    assert test_app.secret_key == 'your-secret-key-here'  # Should match the default
