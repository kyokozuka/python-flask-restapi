from src.models.user import User


class UserRepository:
    
    def __init__(self, db_driver):
        self.db_driver = db_driver
        
    def find_all(self):
        return self.db_driver.session.query(User).all()
    
    def find_by_email(self, email: str) -> User:
        return self.db_driver.session.query(User).filter_by(email=email).first()
    
    def create(self, user: User):
        self.db_driver.session.add(user)
        self.db_driver.session.commit()
        
    def delete(self, user: User):
        self.db_driver.session.delete(user)
        self.db_driver.session.commit()