
from flask import Flask
from flask import request

# Create a flask
app = Flask(__name__)

# Create an API end point
@app.route("/api/v1.0/predict", methods=['GET'])
def make_prediction():
    x1 = request.args.get("x1", 0, type=float)
    x2 = request.args.get("x2", 0, type=float)
    
    # "model"
    if sum([x1, x2]) > 5.8:
        pred = 1
    else:
        pred = 0

    return {"prediction": pred, "features": {"x1": x1, "x2": x2}}

if __name__ == '__main__':
    app.run()
