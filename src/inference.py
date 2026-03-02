# src/inference/predictor.py
import joblib
import numpy as np
import pandas as pd

# Load model and transformations
model = joblib.load("src/artifacts/best_model.joblib")
transformations = joblib.load("src/artifacts/transformations.pkl")
target_encoder = joblib.load("src/artifacts/target_encoder.pkl")  # لو حفظتيه

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Extract additional features: Max_Pollutant, High_Pollutant_Count
    """
    # Max pollutant
    df['Max_Pollutant'] = df[['CO AQI Value','Ozone AQI Value','NO2 AQI Value','PM2.5 AQI Value']].max(axis=1)
    
    # Count of high pollutants
    high_categories = ['Unhealthy','Very Unhealthy','Hazardous']
    df['High_Pollutant_Count'] = (
        df['CO AQI Category'].isin(high_categories).astype(int) +
        df['Ozone AQI Category'].isin(high_categories).astype(int) +
        df['NO2 AQI Category'].isin(high_categories).astype(int) +
        df['PM2.5 AQI Category'].isin(high_categories).astype(int)
    )
    return df

def predict_aqi_category(input_df: pd.DataFrame):
    """
    input_df: DataFrame with raw user inputs (without Max_Pollutant or High_Pollutant_Count)
    Returns: predicted AQI Category
    """
    # Step 1: Add features automatically
    df_features = add_features(input_df.copy())
    
    # Step 2: Transform features
    X_processed = transformations.transform(df_features)
    
    # Step 3: Predict and decode
    preds_encoded = model.predict(X_processed)
    preds = target_encoder.inverse_transform(preds_encoded)
    
    return preds