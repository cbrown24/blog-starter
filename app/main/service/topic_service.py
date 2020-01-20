from app.main import db
from app.main.model.topic import Topic
from app.main.model.blog import Blog

def get_topics():
    return Topic.query.all()

def save_new_topic(data):
    topic = Topic.query.filter_by(name=data['name']).first()
    if not topic:
        new_topic = Topic(**data)
        db.session.add(new_topic)
        db.session.commit()
    else:
        response_object = {
            'status': 'fail',
            'message': 'Topic already exists.',
        }
        return response_object, 409

