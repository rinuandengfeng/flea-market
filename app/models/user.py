
from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from app.utils.error_code import AuthFailed, ParameterException


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(40), nullable=False)  # 登录用户名
    _password = db.Column(db.String(120), nullable=False)  # 密码
    auth = db.Column(db.Integer, default=1)  # 权限
    name = db.Column(db.String(40), nullable=False)  # 用户名
    telphone = db.Column(db.String(11), nullable=False)  # 电话
    icon = db.Column(db.String(100))  # 头像
    udatetime = db.Column(db.DateTime, default=datetime.now)

    @staticmethod
    def verify(username, password):
        user = User.query.filter_by(username=username).first()
        if not user:
            raise AuthFailed()
        if not user.check_password(password):
            raise ParameterException()
        scope = 'SuperAdminScope'
        return {'uid': user.username}

    @property
    # 增加password属性
    def password(self):
        return self._password

    @password.setter
    # 给密码进行加密
    def password(self, raw):
        self._password = generate_password_hash(raw)

    # 给密码解密进行比对。
    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)
