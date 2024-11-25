from flask import Flask, request, jsonify
import json
import pandas as pd
import xgboost as xgb
import numpy as np
from static.header_column import header_column
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

with open('static/disease_data.json', 'r', encoding='utf-8') as json_disease:
    disease_data = json.load(json_disease)

MODEL_IMAGE = xgb.Booster()
MODEL_IMAGE.load_model('models/modelv3.json')
MODEL_IMAGE.set_param({'feature_names': header_column})

@app.route('/')
def home():
    return 'Hello World!'

@app.route('/diseasePrediction', methods=['POST'])
def predictFromDisease():
    features = request.json
    features = features['inputGejala']
    features = pd.DataFrame([features], columns=header_column)
    dmat = xgb.DMatrix(features)
    pred = MODEL_IMAGE.predict(dmat)
    pred = np.argmax (pred, axis=1)
    pred = int(pred)
    pred = disease_data[pred]
    return jsonify(pred)

if __name__ == "__main__":
    app.run(debug=True)