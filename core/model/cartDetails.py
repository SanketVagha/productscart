from core import db, app
from core.model.cart import CartItem
from core.model.product import Product

class CartDetails(db.Model):
    __tablename__ = "cartDetails"
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    cart_id = db.Column(db.Integer, db.ForeignKey(CartItem.id), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(Product.id), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return str(self.id)
    
    @classmethod
    def filter(cls, *criterion):
        db_query = db.session.query(cls)
        return db_query.filter(*criterion)


    @classmethod
    def get_by_id(cls, _id):
        with app.app_context():
            cart_data = cls.filter(cls.id == _id)
            c_data = {}
            for data in cart_data:
                c_data ={
                    'id' : data.id,
                    'product_id' : data.product_id,
                    'quantity' : data.quantity

                }
            return c_data
    
    
    @classmethod
    def get_by_cartId(cls, _id):
        with app.app_context():
            cart_data =  cls.filter(cls.cart_id == _id).all()
            c_data = {}
            for data in cart_data:
                c_data ={
                    'id' : data.id,
                    'product_id' : data.product_id,
                    'quantity' : data.quantity
                }
            return c_data
    

    @classmethod 
    def get_cartDetails(cls):
        with app.app_context():
            cart_data = db.session.query(cls).all()
            carts_data = []
            for data in cart_data:
                p_data ={
                    'id' : data.id,
                    'product_id' : data.product_id,
                    'quantity' : data.quantity

                }
                carts_data.append(p_data)
            return carts_data
    


    @classmethod
    def add_cartDetails(cls, product_id, quantity):
        with app.app_context():
            cart_id = CartItem.add_cart()
            if cart_id:
                new_cart = CartDetails(cart_id= cart_id, product_id= product_id, quantity= quantity)
                db.session.add(new_cart)
                db.session.commit()
                if new_cart.id:
                    return new_cart.id
                db.session.rollback()
                return 0
            
    @classmethod
    def delete_cartDetails(cls,_id):
        with app.app_context():
            new_items = CartDetails.query.get(_id)
            if new_items:
                db.session.delete(new_items)
                db.session.commit()
                if new_items.id:
                    return new_items.id
                db.session.rollback()
                return 0