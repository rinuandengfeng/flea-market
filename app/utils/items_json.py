from app.models.goods import Goods


def items_to_json(items):
    lic=[]
    for i in items:
        lic.append(
            Goods.to_json(i)
        )
    return lic