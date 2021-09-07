from flask import Blueprint

from src.users.users_controller import UserController

from src.infrastracture.database import db
from src.models.user import User

users_api = Blueprint('users_api', __name__)

user = UserController(db)

users_api.add_url_rule('/', view_func=user.users, methods=['GET'])
users_api.add_url_rule('/add', view_func=user.add_todo, methods=['POST'])
users_api.add_url_rule('/update', view_func=user.update_todo, methods=['PUT'])
users_api.add_url_rule('/del', view_func=user.remove_todo, methods=['DELETE'])