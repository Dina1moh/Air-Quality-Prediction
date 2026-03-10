from flask import Blueprint, request, render_template, jsonify
import pandas as pd
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from src.inference import predict_aqi_category

controller = Blueprint("controller", __name__)

@controller.route("/")
def home():
    return render_template("index.html")

@controller.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        df = pd.DataFrame([data])

        mapping = {
            "CO_AQI_Value": "CO AQI Value",
            "Ozone_AQI_Value": "Ozone AQI Value",
            "NO2_AQI_Value": "NO2 AQI Value",
            "PM25_AQI_Value": "PM2.5 AQI Value"
        }
        df.rename(columns=mapping, inplace=True)

        numerical_cols = ["CO AQI Value", "Ozone AQI Value", "NO2 AQI Value", "PM2.5 AQI Value"]

        for col in numerical_cols:
            value = df.at[0, col]
            if isinstance(value, list):
                value = value[0]
            df.at[0, col] = pd.to_numeric(value, errors='raise')

        prediction = predict_aqi_category(df)
        return jsonify({"prediction": prediction.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)})