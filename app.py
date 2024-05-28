from flask import Flask
from flask_restful import Api
from models import db, User, Post
from resources import UserResource, UserListResource, PostResource, PostListResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myapp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
api = Api(app)

with app.app_context():
    db.create_all()

api.add_resource(UserListResource, '/users')
api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(PostListResource, '/posts')
api.add_resource(PostResource, '/posts/<int:post_id>')

if __name__ == '__main__':
    app.run(debug=True) 