from flask import Flask
from flask import request
from flask import jsonify
import config
import functions

token = config.TOKEN

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Start</h1>'


@app.route('/bot', methods=['POST', 'GET'])
def BotHandler():
    if request.method == 'POST':
        r = request.get_json()
        functions.Head(r)
        return jsonify(r)
    return 'Hi'

if __name__ == '__main__':
    app.run()
