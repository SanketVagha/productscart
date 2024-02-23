from core import db

class CartItem(db.Model):
    __tablename__ = "cart"
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    def __repr__(self):
        return self.id
    
    @classmethod
    def filter(cls, *criterion):
        db_query = db.session.query(cls)
        return db_query.filter(*criterion)
    
    @classmethod
    def get_by_id(cls, _id):
        return cls.filter(cls.id == _id).first()
