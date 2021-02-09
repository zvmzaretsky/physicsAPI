from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/count', methods=['POST'])
def count():
    body = request.json

    # TODO add calculating function here and return the result instead of -1
    return -1


if __name__ == '__main__':
    app.run()
