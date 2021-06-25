from flask import Blueprint, request

from app import create_app
from app.models.user import User
from app.utils.token import get_token

login_bp = Blueprint("login_bp", __name__)


@login_bp.route('/list', methods=['POST'])
def login():
    data = request.form
    username = data['username']
    password = data['password']
    current_user = User.verify(username, password)

    if current_user:
        token = get_token(username, password)

    return {
        "code":20000,
        "data":"admin_token"
    }
