from flask import Flask
from flask_cors import CORS

from src.users.router import users_api
from src.infrastracture.database import init_db
from src.infrastracture.database.mysql import config

def create_app():
    # Flask APP
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'

    # CORS対応
    CORS(app)
    
    # Blueprint
    app.register_blueprint(users_api, url_prefix='/api/user')

    # DB設定
    app.config.from_object(config)
    init_db(app)
    
    return app

app = create_app()
