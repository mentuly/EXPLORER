from flask import request
from flask_restful import Resource, reqparse
from models import db, User, Post

class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return {"id": user.id, "username": user.username, "email": user.email}

    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        data = request.get_json()
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        db.session.commit()
        return {"message": "User updated", "user": {"id": user.id, "username": user.username, "email": user.email}}

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted"}

class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return [{"id": user.id, "username": user.username, "email": user.email} for user in users]

    def post(self):
        data = request.get_json()
        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return {"message": "User created", "user": {"id": new_user.id, "username": new_user.username, "email": new_user.email}}, 201

class PostResource(Resource):
    def get(self, post_id):
        post = Post.query.get_or_404(post_id)
        return {"id": post.id, "title": post.title, "body": post.body, "user_id": post.user_id}

    def put(self, post_id):
        post = Post.query.get_or_404(post_id)
        data = request.get_json()
        post.title = data.get('title', post.title)
        post.body = data.get('body', post.body)
        db.session.commit()
        return {"message": "Post updated", "post": {"id": post.id, "title": post.title, "body": post.body, "user_id": post.user_id}}

    def delete(self, post_id):
        post = Post.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        return {"message": "Post deleted"}

class PostListResource(Resource):
    def get(self):
        posts = Post.query.all()
        return [{"id": post.id, "title": post.title, "body": post.body, "user_id": post.user_id} for post in posts]

    def post(self):
        data = request.get_json()
        new_post = Post(title=data['title'], body=data['body'], user_id=data['user_id'])
        db.session.add(new_post)
        db.session.commit()
        return {"message": "Post created", "post": {"id": new_post.id, "title": new_post.title, "body": new_post.body, "user_id": new_post.user_id}}, 201