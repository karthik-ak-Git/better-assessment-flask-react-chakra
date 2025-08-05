from app.models.task import Task
from app import db
from sqlalchemy import desc

class TaskRepository:
    @staticmethod
    def get_all(page=1, limit=10):
        offset = (page - 1) * limit
        return Task.query.order_by(desc(Task.created_at)).offset(offset).limit(limit).all()
    
    @staticmethod
    def get_by_id(task_id):
        return Task.query.get(task_id)
    
    @staticmethod
    def create(task_data):
        task = Task(**task_data)
        db.session.add(task)
        db.session.commit()
        return task
    
    @staticmethod
    def update(task_id, task_data):
        task = TaskRepository.get_by_id(task_id)
        if task:
            for key, value in task_data.items():
                setattr(task, key, value)
            db.session.commit()
        return task
    
    @staticmethod
    def delete(task_id):
        task = TaskRepository.get_by_id(task_id)
        if task:
            db.session.delete(task)
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def count():
        return Task.query.count() 