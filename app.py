from flask import Flask, request, jsonify

from core.apis.products import productsapi


app = Flask(__name__)

app.register_blueprint(productsapi)

if __name__ == "__main__":
    app.run(debug= True)