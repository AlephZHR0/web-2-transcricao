from flask import abort, make_response, jsonify
from domain.user import User
from app import db
from sqlalchemy import exc

class UserRepository:

    @staticmethod
    def add_user(user):
        try:
            db.session.add(user)
            db.session.commit()
            return user
        except exc.IntegrityError:
           abort(make_response( jsonify({ "message" : "Erro ao criar usuario"}),400))

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def update_user(user_id, updated_data):
        user = User.query.get(user_id)
        if not user:
            return None
        user.username = updated_data.get('username', user.username)
        user.ra = updated_data.get('ra',user.ra)
        user.birthdate = updated_data.get('birthdate', user.birthdate)
        user.email = updated_data.get('email', user.email)
        user.password = updated_data.get('password', user.password)

        db.session.commit()
        return user

    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if not user:
            return None
        db.session.delete(user)
        db.session.commit()
        return user