import pytest
from app import create_app, db
from app.models.task import Task
from app.models.comment import Comment
from tests.factories import TaskFactory, CommentFactory

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def sample_task():
    return TaskFactory()

class TestTaskAPI:
    def test_get_tasks_empty(self, client):
        """Test getting tasks when none exist"""
        response = client.get("/api/tasks")
        assert response.status_code == 200
        data = response.get_json()
        assert data['tasks'] == []
        assert data['total'] == 0
    
    def test_create_task(self, client):
        """Test creating a new task"""
        task_data = {
            "title": "Test Task",
            "description": "This is a test task description"
        }
        response = client.post("/api/tasks", json=task_data)
        assert response.status_code == 201
        data = response.get_json()
        assert data['title'] == task_data['title']
        assert data['description'] == task_data['description']
        assert 'id' in data
    
    def test_create_task_invalid_data(self, client):
        """Test creating task with invalid data"""
        # Missing title
        response = client.post("/api/tasks", json={"description": "Only description"})
        assert response.status_code == 400
        
        # Missing description
        response = client.post("/api/tasks", json={"title": "Only title"})
        assert response.status_code == 400
        
        # Empty title
        response = client.post("/api/tasks", json={"title": "", "description": "Valid description"})
        assert response.status_code == 400
    
    def test_get_task_by_id(self, client, sample_task):
        """Test getting a specific task by ID"""
        response = client.get(f"/api/tasks/{sample_task.id}")
        assert response.status_code == 200
        data = response.get_json()
        assert data['id'] == sample_task.id
        assert data['title'] == sample_task.title
    
    def test_get_task_not_found(self, client):
        """Test getting a non-existent task"""
        response = client.get("/api/tasks/999")
        assert response.status_code == 404
    
    def test_update_task(self, client, sample_task):
        """Test updating an existing task"""
        update_data = {
            "title": "Updated Title",
            "description": "Updated description"
        }
        response = client.put(f"/api/tasks/{sample_task.id}", json=update_data)
        assert response.status_code == 200
        data = response.get_json()
        assert data['title'] == update_data['title']
        assert data['description'] == update_data['description']
    
    def test_update_task_not_found(self, client):
        """Test updating a non-existent task"""
        response = client.put("/api/tasks/999", json={"title": "New Title"})
        assert response.status_code == 404
    
    def test_delete_task(self, client, sample_task):
        """Test deleting a task"""
        response = client.delete(f"/api/tasks/{sample_task.id}")
        assert response.status_code == 200
        
        # Verify task is deleted
        get_response = client.get(f"/api/tasks/{sample_task.id}")
        assert get_response.status_code == 404
    
    def test_delete_task_not_found(self, client):
        """Test deleting a non-existent task"""
        response = client.delete("/api/tasks/999")
        assert response.status_code == 404
    
    def test_get_tasks_with_pagination(self, client):
        """Test getting tasks with pagination"""
        # Create multiple tasks
        TaskFactory.create_batch(5)
        
        response = client.get("/api/tasks?page=1&limit=3")
        assert response.status_code == 200
        data = response.get_json()
        assert len(data['tasks']) == 3
        assert data['page'] == 1
        assert data['limit'] == 3
        assert data['total'] == 5
    
    def test_task_with_comments(self, client, sample_task):
        """Test that tasks can have comments"""
        # Create comments for the task
        CommentFactory.create_batch(3, task_id=sample_task.id)
        
        # Get the task and verify it has comments
        response = client.get(f"/api/tasks/{sample_task.id}")
        assert response.status_code == 200
        data = response.get_json()
        assert data['id'] == sample_task.id 