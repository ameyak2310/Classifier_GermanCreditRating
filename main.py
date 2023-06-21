""" 
Flask app to serve churn model.
"""

# Libraries
import pickle
import pandas as pd
from flask import Flask, request, jsonify

# Third party
from src.encoder import encode
from src.inference import infer



app = Flask("status")

with open("bin/oneHotEncoder.bin", "rb") as f_in:
    enc = pickle.load(f_in)

with open("bin/clf_log1.bin", "rb") as f_in:
    model = pickle.load(f_in)


@app.route("/predict", methods=["POST"])
def predict():
    """Prediction function

    Returns:
        dict: Returns probability and decesion.
    """
    payload = request.get_json()
    encoder = enc
    
    X_en = encode(payload=payload, encoder=enc)
    y_prob = infer(payload_en=X_en, model=model)[0]
    verdict = int(y_prob >= 0.5)

    result = {'VERDICT': verdict, 'PROBABILITY':y_prob.round(3)}
 
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=6000)
