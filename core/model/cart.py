from core import db, app

class CartItem(db.Model):
    __tablename__ = "cart"
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    def __repr__(self):
        return str(self.id)
    
    @classmethod
    def filter(cls, *criterion):
        db_query = db.session.query(cls)
        return db_query.filter(*criterion)
    
    @classmethod
    def get_by_id(cls, _id):
        return cls.filter(cls.id == _id).first()
    @classmethod
    def add_cart(cls):
        with app.app_context():
            new_cart = CartItem()
            db.session.add(new_cart)
            db.session.commit()

            return new_cart.id
    