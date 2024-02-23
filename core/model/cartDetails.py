from core import db
from core.model.cart import CartItem
from core.model.product import Product

class CartDetails(db.Model):
    __tablename__ = "cartDetails"
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    cart_id = db.Column(db.Integer, db.ForeignKey(CartItem.id), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(Product.id), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return self.id
    
    @classmethod
    def filter(cls, *criterion):
        db_query = db.session.query(cls)
        return db_query.filter(*criterion)


    @classmethod
    def get_by_id(cls, _id):
        return cls.filter(cls.id == _id).first()
    
    @classmethod
    def get_by_cartId(cls, _id):
        return cls.filter(cls.cart_id == _id).all()
