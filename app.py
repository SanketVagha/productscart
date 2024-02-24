from flask import Flask, request, jsonify

from core.apis.products import productsapi
from core.apis.cartDetails import cartDetailsapi


app = Flask(__name__)

app.register_blueprint(productsapi)
app.register_blueprint(cartDetailsapi)

if __name__ == "__main__":
    app.run(debug= True)