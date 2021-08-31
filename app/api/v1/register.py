from flask import Blueprint, request, session
from werkzeug.security import generate_password_hash

from app.models.user import User
from app.utils.response import SUCCESS
from app import db

register_bp = Blueprint('register_bp', __name__)


# 注册用户
@property
@register_bp.route('/user/register', methods=['POSt'])
def register():
    a = request
    username = request.form.get('username')  # 登录的名字
    username = User.query.filter(User.username == username).first()
    if not username:
        username = request.form.get('username')
        passwd = request.form.get('password')  # 密码
        name = request.form.get('name')  # 用户名
        tel = request.form.get('telphone')  # 电话
        passwd = generate_password_hash(passwd)
        user = User()
        user.username = username
        user._password = passwd
        user.name = name
        user.telphone = tel
        db.session.add(user)
        db.session.commit()
        return SUCCESS
    else:
        return {
            "code": 500,
            "msg": "用户名已经被注册!"
        }
