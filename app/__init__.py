from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# 创建db实例


db = SQLAlchemy()
cors = CORS()  # 设置跨域
migrate = Migrate()


# 创建注册蓝图函数
def register_buleprints(app):
    # 导入蓝图实例
    from app.api.v1.login import login_bp
    # 注册蓝图
    app.register_blueprint(login_bp, url_prefix='/v1')


# 注册插件
def register_plugin(app):
    # 配置跨域
    cors.init_app(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})
    db.init_app(app)
    from app.models.user import User


# 创建工厂函数
def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.settings')
    app.config.from_object('app.config.secure')
    register_buleprints(app)
    register_plugin(app)
    return app
