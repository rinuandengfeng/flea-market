from flask import Blueprint, request

from app.models.goods import Goods
from app.utils.items_json import items_to_json

items_bp = Blueprint('items_bp',__name__)


@items_bp.route('/goods/list',methods=['GET'])
def goods_page():
    data = request.args
    num = Goods.query.all()
    infos = Goods.query.filter().paginate(int(data['page']),int(data['limit']))
    return {
        "code":20000,
        "items":items_to_json(infos.items),
        "data":len(num)
    }