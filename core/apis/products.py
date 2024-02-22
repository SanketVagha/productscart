from flask import Blueprint

productsapi = Blueprint('productsapi', __name__)

@productsapi.route("/")
def display():
    return " WelCome"


@productsapi.route('/products', methods=['GET'])
def product_list():
    return "Hello"