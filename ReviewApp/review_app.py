from flask import Flask, jsonify

app = Flask(__name__)

product_reviews = [ 
    {"user_id": 1, "product_id": 1, "rating":4, "review": "Menghilangkan ketombe bagus !!"},
    {"user_id": 2, "product_id": 2, "rating":4, "review": "Nikmat"},
    {"user_id": 3, "product_id": 2, "rating":5, "review": "Enak bos"},
    {"user_id": 2, "product_id": 3, "rating":3, "review": "Biasa aja"}
]

@app.route('/reviews')
def get_reviews():
    return jsonify(product_reviews)

@app.route('/reviews/<int:product_id>')
def get_review(product_id):
    reviews = [review for review in product_reviews if review['product_id'] == product_id]

    if reviews:
        return jsonify(
            {"reviews": reviews}
        )
    else:
        return jsonify(
            {"message": "Product isn't found"}, 404
        )

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5003)