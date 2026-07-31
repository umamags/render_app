import os
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return "hello from render"


@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "hello from render"}), 200


@app.route('/fetch_comment', methods=['GET'])
def fetch_comment():
    return jsonify({"message": "Fetch comments from google drive"}), 200


@app.route('/post_comment', methods=['POST'])
def post_comment():
    return jsonify({"message": "Posted comments to google drive"}), 200


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)
