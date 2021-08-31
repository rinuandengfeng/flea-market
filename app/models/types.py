from app import db


class Type(db.Model):
    __tablename__ = 'types'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(40), nullable=True)  # 类型的名字
    goodss = db.relationship('Goods', backref='types')  # 跟goods表建立多对多的联系
