from app.models.comment import Comment
from app import db


class CommentRepository:
    @staticmethod
    def create(data):
        comment = Comment(**data)
        db.session.add(comment)
        db.session.commit()
        return comment

    @staticmethod
    def get_by_task(task_id, page=1, limit=10):
        return Comment.query.filter_by(task_id=task_id)\
            .order_by(Comment.created_at.desc())\
            .paginate(page=page, per_page=limit, error_out=False).items

    @staticmethod
    def update(comment_id, data):
        comment = Comment.query.get(comment_id)
        if comment:
            for key, value in data.items():
                setattr(comment, key, value)
            db.session.commit()
        return comment

    @staticmethod
    def delete(comment_id):
        comment = Comment.query.get(comment_id)
        if comment:
            db.session.delete(comment)
            db.session.commit()
        return comment
