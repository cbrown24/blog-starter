from flask_restplus import Api
from flask import Blueprint

# from .api 
from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.topic_controller import api as topic_ns
from .main.controller.post_controller import api as post_ns

blueprint = Blueprint('api', __name__)
authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
}
api = Api(blueprint,
          title='Office App microblog',
          version='1.0',
          description='a flask microblog with a restplus web service',
          security='Bearer Auth', authorizations=authorizations)

api.add_namespace(user_ns, path='/user')
api.add_namespace(topic_ns, path='/topic')
api.add_namespace(post_ns, path='/post')
api.add_namespace(auth_ns)