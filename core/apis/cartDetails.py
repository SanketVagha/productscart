from flask import Blueprint, request
from core.apis.response import APIResponse
from core.model.product import Product
from core.model.cartDetails import CartDetails


cartDetailsapi = Blueprint('cartDetailsapi', __name__)

@cartDetailsapi.route('/cart', methods= ['POST'])
def add_cartDetails():
    data = {}
    product_id = request.json['product_id']
    quantity = request.json['quantity']

    product_data = Product.get_by_id(product_id)
    if not product_data:
        data['message'] = "Product Id Invalid"
        return APIResponse.respond(data = data)


    cart_id = CartDetails.add_cartDetails(product_id, quantity)
    data['id'] = cart_id
    return APIResponse.respond(data = data)



@cartDetailsapi.route('/cart', methods= ['GET'])
def cartDetails_list():
    data = {}
    cartDetails_data = CartDetails.get_cartDetails()
    if not cartDetails_data:
        data['message'] = "Cart Data Not Display"
        return APIResponse.respond(data= data)
    data['message'] = "sucessfully Cart Data Display"
    data['data'] = cartDetails_data
    return APIResponse.respond(data = data)


@cartDetailsapi.route('/cart/<int:id>', methods= ['DELETE'])
def cartDetails_delete(id):
    data = {}
    cartDetails = CartDetails.get_by_id(id)
    if not cartDetails:
        data['message'] = "Cart Id Invalid"
        return APIResponse.respond(data = data)
        
    id = cartDetails['id']
    
    cart_id = CartDetails.delete_cartDetails(id)
    if cart_id == 0:
        data['message'] = "Cart Not Delete"
    else:
        data['id'] = cart_id
        data['message'] = "Cart Successfully Deleted"
    return APIResponse.respond(data = data)


