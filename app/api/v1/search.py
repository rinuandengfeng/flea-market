from flask import Blueprint, request

from app.models.goods import Goods

search_bp = Blueprint('search_bp', __name__)


# 搜索页面
@search_bp.route('/user/search', methods=['GET'])
def grabble():
    info = []
    data = request.args
    type = data['type']
    contents = data['content']
    infos = Goods.query.filter(Goods.type.like('%' + type + '%')).all()
    num = Goods.query.filter(Goods.type.like('%' + type + '%')).count()
    for i in infos:
        info.append(Goods.to_json(i))

    return {
        "code": 20000,
        "data": {
            "total": num,
            "messages": info
        }

    }
