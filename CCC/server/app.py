from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/r', methods=['POST'])
def rec():
    data = request.json
    print(data)
    return {
        'success' : 'true'
    }
