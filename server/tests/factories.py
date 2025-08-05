import factory
from app.models.comment import Comment
from app.models.task import Task
from app import db


class TaskFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Task
        sqlalchemy_session = db.session

    title = factory.Faker('sentence', nb_words=3)
    description = factory.Faker('paragraph')


class CommentFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Comment
        sqlalchemy_session = db.session

    task_id = 1
    content = factory.Faker('sentence')
