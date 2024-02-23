from flask import Blueprint
from core.apis.response import APIResponse
from core.model.product import Product

productsapi = Blueprint('productsapi', __name__)

@productsapi.route("/")
def display():
    product_list = Product.get_products()
    return APIResponse.respond(data = product_list)
    return " WelCome"


@productsapi.route('/products', methods=['GET'])
def product_list():
    return APIResponse.respond(data = "Hello")