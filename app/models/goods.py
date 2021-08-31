from datetime import datetime

from app import db


class Goods(db.Model):
    __tablename__ = 'goods'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(100), nullable=False)  # 标题
    content = db.Column(db.String(200), nullable=False)  # 内容或参数
    telphone = db.Column(db.String(11), nullable=False)  # 电话
    goods_photo = db.Column(db.String(120), nullable=False)  # 照片
    price = db.Column(db.Integer, nullable=False)  # 价格
    gdatetime = db.Column(db.DateTime, default=datetime.now)  # 发布时间
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # 与用户表建立联系
    type_id = db.Column(db.ForeignKey('types.id'), nullable=False)  # 与类型表建立联系

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "telphone": self.telphone,
            "goods_photo": self.goods_photo,
            "price": self.price,
            "type": self.type
        }
