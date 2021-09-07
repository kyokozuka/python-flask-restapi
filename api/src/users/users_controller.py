import json

from flask import request

from src.users.users_service import UserService
from src.users.users_repositry import UserRepository

class UserController():

    def __init__(self, db_driver):
        self.db_driver = db_driver
        user_repo = UserRepository(db_driver)
        self.user = UserService(user_repo)
    
    def users(self):
        results = self.user.find_all()
        return { 'items':  results}
    
    def add_todo(self):
        data = json.loads(request.data)
        result = self.user.create(data=data)
        return {'items': result}
    
    def update_todo(self):
        data = json.loads(request.data)
        result = self.user.update(data=data)
        return {'items': result}
    
    def remove_todo(self):
        data = json.loads(request.data)
        print(data['email'])
        self.user.delete(email=data['email'])
        return {"items": True}