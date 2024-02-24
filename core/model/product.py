from core import db, app

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(255))

    def __repr__(self):
        return str(self.id)

    @classmethod
    def filter(cls, *criterion):
        db_query = db.session.query(cls)
        return db_query.filter(*criterion)
    
    @classmethod
    def get_by_id(cls, _id):
        with app.app_context():
            product_data = cls.filter(cls.id == _id)
            p_data = {}
            for data in product_data:
                p_data ={
                    'id' : data.id,
                    'name' : data.name,
                    'description' : data.description,
                    'price' : data.price,
                    'image_url' : data.image_url
                }
            return p_data
    
    @classmethod
    def get_products(cls):
        with app.app_context():
        # return "Hello"
            product_data = db.session.query(cls).all()
            products_data = []
            for data in product_data:
                p_data ={
                    'id' : data.id,
                    'name' : data.name,
                    'description' : data.description,
                    'price' : data.price,
                    'image_url' : data.image_url
                }
                products_data.append(p_data)
            return products_data
    
    @classmethod
    def add_product(cls, name, description, price, image_url):
        with app.app_context():
            # print(name, description, price, image_url)
            new_products = Product(name= name, description= description, price= price, image_url= image_url)
            db.session.add(new_products)
            db.session.commit()
            if new_products.id:
                return new_products.id
            db.session.rollback()
            return 0


