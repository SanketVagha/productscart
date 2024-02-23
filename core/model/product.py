from core import db

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(255))

    def __repr__(self):
        return self.id

    @classmethod
    def filter(cls, *criterion):
        db_query = db.session.query(cls)
        return db_query.filter(*criterion)
    
    @classmethod
    def get_by_id(cls, _id):
        return cls.filter(cls.id == _id).first()
    
    def get_products(cls):
        return db.session.query().all()