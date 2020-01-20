from .. import db, flask_bcrypt
import datetime


class Blog(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "blog"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_by = db.Column(db.String(255), unique=False, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    title = db.Column(db.String(100), unique=False)
    body = db.Column(db.String(800), unique=False)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'))

    def __init__(self ,*args, **kwargs):
        self.created_by = "test"
        self.created_on = datetime.datetime.utcnow()
        for k in kwargs:
            setattr(self, k, kwargs[k])
