from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

def get_product(product_id):
    response = requests.get(f'http://productapp:5000/products/{product_id}')
    return response.json()

def get_quantities(product_id):
    response = requests.get(f'http://cartapp:5001/cart/quantity/{product_id}')
    return response.json()['total_quantity']

def get_reviews(product_id):
    response = requests.get(f'http://reviewapp:5003/reviews/{product_id}')
    return response.json()


@app.route('/product/<int:product_id>')
def get_info(product_id):
    product_info = get_product(product_id)
    product_sold = get_quantities(product_id)
    product_reviews = get_reviews(product_id)

    return render_template('index.html', info=product_info, sold=product_sold, reviews=product_reviews)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=5004)
