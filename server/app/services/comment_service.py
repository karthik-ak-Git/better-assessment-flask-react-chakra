from app.repositories.comment_repository import CommentRepository


class CommentService:
    @staticmethod
    def create_comment(data):
        return CommentRepository.create(data)

    @staticmethod
    def get_comments(task_id, page=1, limit=10):
        return CommentRepository.get_by_task(task_id, page, limit)

    @staticmethod
    def update_comment(comment_id, data):
        return CommentRepository.update(comment_id, data)

    @staticmethod
    def delete_comment(comment_id):
        return CommentRepository.delete(comment_id)
