
from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello world"

if __name__ == '__main__':
    app.run()
