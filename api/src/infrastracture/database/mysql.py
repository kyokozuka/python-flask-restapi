class MysqlConfig:
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
      'user': 'root',
      'password': 'password',
      'host': 'localhost',
      'db_name': 'python-flask-rest-api'
  })

config = MysqlConfig