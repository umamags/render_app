import os
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    timestamp = datetime.now().isoformat()
    return f"hello from render - {timestamp}"


@app.route('/hello', methods=['GET'])
def hello():
    timestamp = datetime.now().isoformat()
    return jsonify({"message": "hello from render", "timestamp": timestamp}), 200


@app.route('/fetch_comment', methods=['GET'])
def fetch_comment():
    return jsonify({"message": "Fetch comments from google drive"}), 200


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='127.0.0.1', port=port)
