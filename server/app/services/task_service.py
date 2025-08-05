from app.repositories.task_repository import TaskRepository
from app.schemas.task import TaskCreateSchema, TaskUpdateSchema, TaskSchema
from marshmallow import ValidationError

class TaskService:
    @staticmethod
    def get_tasks(page=1, limit=10):
        return TaskRepository.get_all(page, limit)
    
    @staticmethod
    def get_task(task_id):
        return TaskRepository.get_by_id(task_id)
    
    @staticmethod
    def create_task(data):
        try:
            # Validate input data
            schema = TaskCreateSchema()
            validated_data = schema.load(data)
            
            # Create task
            task = TaskRepository.create(validated_data)
            
            # Return serialized task
            result_schema = TaskSchema()
            return result_schema.dump(task)
        except ValidationError as e:
            raise ValueError(f"Validation error: {e.messages}")
    
    @staticmethod
    def update_task(task_id, data):
        try:
            # Validate input data
            schema = TaskUpdateSchema()
            validated_data = schema.load(data)
            
            # Update task
            task = TaskRepository.update(task_id, validated_data)
            
            if not task:
                raise ValueError("Task not found")
            
            # Return serialized task
            result_schema = TaskSchema()
            return result_schema.dump(task)
        except ValidationError as e:
            raise ValueError(f"Validation error: {e.messages}")
    
    @staticmethod
    def delete_task(task_id):
        success = TaskRepository.delete(task_id)
        if not success:
            raise ValueError("Task not found")
        return True
    
    @staticmethod
    def get_tasks_count():
        return TaskRepository.count() 