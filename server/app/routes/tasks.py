from flask import Blueprint, request, jsonify
from app.services.task_service import TaskService
from app.schemas.task import TaskSchema

task_bp = Blueprint('tasks', __name__)

@task_bp.route("/api/tasks", methods=["GET"])
def get_tasks():
    """Get all tasks with pagination"""
    try:
        page = request.args.get('page', 1, type=int)
        limit = request.args.get('limit', 10, type=int)
        
        tasks = TaskService.get_tasks(page, limit)
        schema = TaskSchema(many=True)
        
        return jsonify({
            'tasks': schema.dump(tasks),
            'page': page,
            'limit': limit,
            'total': TaskService.get_tasks_count()
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@task_bp.route("/api/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    """Get a specific task by ID"""
    try:
        task = TaskService.get_task(task_id)
        if not task:
            return jsonify({'error': 'Task not found'}), 404
        
        schema = TaskSchema()
        return jsonify(schema.dump(task)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@task_bp.route("/api/tasks", methods=["POST"])
def create_task():
    """Create a new task"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        task = TaskService.create_task(data)
        return jsonify(task), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@task_bp.route("/api/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    """Update an existing task"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        task = TaskService.update_task(task_id, data)
        return jsonify(task), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@task_bp.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    """Delete a task"""
    try:
        TaskService.delete_task(task_id)
        return jsonify({'message': 'Task deleted successfully'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500 