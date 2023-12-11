import joblib
import pandas as pd
from flask_cors import CORS
from flask import Flask, request, jsonify

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}}, support_credentials=True)
model = joblib.load("model/rf_regressor.joblib")
preprocessor = joblib.load("model/preprocessor.joblib")

def get_change(current, previous):
    if current == previous:
        return 0
    try:
        return (abs(current - previous) / previous) * 100.0
    except ZeroDivisionError:
        return float('inf')

@app.route("/", methods=["GET"])
def home():
    return "API is running..."

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    df = pd.DataFrame([data])
    df_preprocessed = preprocessor.transform(df)
    prediction = model.predict(df_preprocessed)
    return jsonify({ "predictedPrice": prediction[0], "isReasonable": True if get_change(data["price"], prediction[0]) <= 15 else False })

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=1780)
