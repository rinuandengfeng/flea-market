import os

BASEAIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
UPLOAD_FOLDER = '/upload/images/'
SQLALCHEMY_TRACK_MODIFICATIONS = False

TOKEN_EXPIRATION = 30 * 24 * 3600  # 令牌过期时间

# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Dallasryp123!!@rm-2ze9c7bp86pc6m9qd3o.mysql.rds.aliyuncs.com:3306/biaodan'

SECRET_KEY = '123456'