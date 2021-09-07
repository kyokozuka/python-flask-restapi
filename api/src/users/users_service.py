from src.models.user import User


class UserService:
    def __init__(self, user_repo):
        self.user_repo = user_repo
    
    def create(self, data: dict):
        user = User( 
            email=data['email'], first_name=data['first_name'],
            last_name=data['last_name'],first_name_kana=data['first_name_kana'],
            last_name_kana=data['last_name_kana'],gender=data['gender'], 
            address=data['address'])
        self.user_repo.create(user)
        return user
        
    def find_all(self):
        return self.user_repo.find_all()
    
    def update(self, data: dict):
        user = self.user_repo.find_by_email(data['email'])
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.first_name_kana = data['first_name_kana']
        user.last_name_kana = data['last_name_kana']
        user.gender = data['gender']
        user.address = data['address']
        self.user_repo.create(user)
        return user
    
    def delete(self, email: str):
        user = self.user_repo.find_by_email(email)
        self.user_repo.delete(user)