from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "user1", "email":"user1@gmail.com"},
    {"id": 2, "name": "user2", "email":"user2@gmail.com"}
]

@app.route('/users')
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True, port=5002)