from app.main import db
from app.main.model.topic import Topic
from app.main.model.blog import Blog

def get_posts():
    return Blog.query.all()

def save_new_post(data):
    try:
        new_blog = Blog(**data)
        db.session.add(new_blog)
        db.session.commit()
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Error occured creating post %r' % e,
        }
        return response_object, 500
