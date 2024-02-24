from flask import Blueprint, request
from core.apis.response import APIResponse
from core.model.product import Product


productsapi = Blueprint('productsapi', __name__)

@productsapi.route("/")
def display():
    product_data = Product.get_products()
    return APIResponse.respond(data = product_data)
    return " WelCome"


@productsapi.route('/products', methods= ['GET'])
def product_list():
    product_data = Product.get_products()
    return APIResponse.respond(data = product_data)

@productsapi.route('/add_products', methods= ['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    image_url = request.json['image_url']

    product_data = Product.add_product(name, description, price, image_url)
    # product_data = request.json['name']
    return APIResponse.respond(data= product_data)