from app import db


class Goods(db.Model):
    __tablename__ = 'goods'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    telphone = db.Column(db.String(11), nullable=False)
    photo = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "telphone": self.telphone,
            "photo": self.photo,
            "price": self.price
        }
