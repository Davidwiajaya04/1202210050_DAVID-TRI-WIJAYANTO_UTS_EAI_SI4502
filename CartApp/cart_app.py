from flask import Flask, jsonify, request

app = Flask(__name__)

cart_items = [
    {"user_id": 2, "product_id": 1, "quantity": 4},
    {"user_id": 1, "product_id": 2, "quantity": 3},
    {"user_id": 2, "product_id": 2, "quantity": 1},
    {"user_id": 3, "product_id": 3, "quantity": 5}
]

@app.route('/cart', methods=['GET'])
def get_cart():
    return jsonify(cart_items)

@app.route('/cart/quantity/<int:product_id>', methods=['GET'])
def get_total_quantity(product_id):
    total_quantity = sum(item['quantity'] for item in cart_items if item['product_id'] == product_id)
    return jsonify({'product_id': product_id, 'total_quantity': total_quantity})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
