# src/controllers/routes.py

from flask import Blueprint, request, render_template, jsonify
import pandas as pd
from src.inference import predict_aqi_category

routes = Blueprint("routes", __name__)

@routes.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@routes.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json

        mapping = {
            "AQI_Value": "AQI Value",
            "CO_AQI_Value": "CO AQI Value",
            "CO_AQI_Category": "CO AQI Category",
            "Ozone_AQI_Value": "Ozone AQI Value",
            "Ozone_AQI_Category": "Ozone AQI Category",
            "NO2_AQI_Value": "NO2 AQI Value",
            "NO2_AQI_Category": "NO2 AQI Category",
            "PM25_AQI_Value": "PM2.5 AQI Value",
            "PM25_AQI_Category": "PM2.5 AQI Category"
        }

        df = pd.DataFrame([data])
        df.rename(columns=mapping, inplace=True)

        prediction = predict_aqi_category(df)

        return jsonify({"prediction": prediction.tolist()})

    except Exception as e:
        return jsonify({"error": str(e)})