from flask import Blueprint, request
from core.apis.response import APIResponse
from core.model.product import Product


productsapi = Blueprint('productsapi', __name__)

@productsapi.route('/products', methods= ['GET'])
def product_list():
    data = {}
    product_data = Product.get_products()
    if not product_data:
        data['message'] = "Product Data Not Display"
        return APIResponse.respond(data= data)
    data['data'] = product_data
    return APIResponse.respond(data = data)

@productsapi.route('/products/<int:id>', methods= ['GET'])
def product_get_by_id(id):
    data = {}
    product_data = Product.get_by_id(id)
    if not product_data:
        data['message'] = "Product Id Invalid"
        return APIResponse.respond(data= data)
    data['data'] = product_data
    data['message'] = "Product Data Display"
    return APIResponse.respond(data = data)

@productsapi.route('/add_products', methods= ['POST'])
def add_product():
    data = {}
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    image_url = request.json['image_url']

    product_data = Product.add_product(name, description, price, image_url)
    if product_data == 0:
        data['message'] = "Product Not Added"
        return APIResponse.respond(data= data)
    data['data'] = product_data
    data['message'] = "Add Products"
    # product_data = request.json['name']
    return APIResponse.respond(data= product_data)