from flask import Blueprint, request

from app import create_app
from app.models.user import User
from app.utils import response
from app.utils.response import response_data
from app.utils.token import get_token

login_bp = Blueprint('login_bp', __name__)


@login_bp.route('/user/login', methods=['POST'])
def login():
    data = request.form
    username = data['username']
    password = data['password']
    current_user = User.verify(username, password)

    if current_user:
        token = get_token(username, password)

    return {
        "code": 20000,
        "data": "admin_token"
    }

@login_bp.route('/user/info',methods=['GET'])
def get_info():
    return {
        "code": 20000,
        "data": {
            "roles": ["admin"],
            "introduction": "introduction",
            "avatar": "https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif",
            # "name": info.name
            "name": "Super Admin"
        }
    }



@login_bp.route('/user/logout', methods=['POST'])
def logout():
    return response_data(response.SUCCESS)
