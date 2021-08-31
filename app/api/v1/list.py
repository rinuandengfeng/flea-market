from flask import Blueprint, request

from app.models.goods import Goods
from app.models.user import User
from app.utils.items_json import items_to_json

goods_bp = Blueprint('goods_bp',__name__)


@goods_bp.route('/goods/list',methods=['GET'])
def goods_page():
    data = request.args
    num = Goods.query.all()
    infos = Goods.query.filter().paginate(int(data['page']),int(data['limit']))
    return {
        "code":20000,
        "items":items_to_json(infos.items),
        "data":len(num)
    }

@goods_bp.route('/goods/type',methods=['get'])
def type_list():
    tid = request.args.get('tid')
    type_goods = Goods.query.filter(Goods.type_id == tid).all()
    return {
        "code":20000,
        "type_goods":items_to_json(type_goods)
    }
