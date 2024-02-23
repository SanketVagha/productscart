from flask_marshmallow import Marshmallow
from flask import Flask

app = Flask(__name__)


ma = Marshmallow(app)
class ProductSchema(ma.Schema):
    class Meta:
        fields = "__all__"