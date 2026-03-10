import joblib
import pandas as pd

# Load artifacts
model = joblib.load("src/artifacts/best_model.joblib")
transformations = joblib.load("src/artifacts/transformations.pkl")
target_encoder = joblib.load("src/artifacts/target_encoder.pkl")


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Extract additional features: pollution_mean
    
    This feature captures the overall pollution level as a composite measure
    of all four pollutants (CO, Ozone, NO2, PM2.5).
    """
    df['pollution_mean'] = df[['CO AQI Value', 'Ozone AQI Value', 'NO2 AQI Value', 'PM2.5 AQI Value']].mean(axis=1)
    return df


def predict_aqi_category(input_df: pd.DataFrame):
    """
    Predict AQI Category for given input data.
    
    Parameters:
        input_df: DataFrame with columns [Country, CO AQI Value, Ozone AQI Value, NO2 AQI Value, PM2.5 AQI Value]
    
    Returns:
        Array of predicted AQI Categories
    """
    # Add engineered features
    df = add_features(input_df.copy())

    # Transform features using the preprocessing pipeline
    X_processed = transformations.transform(df)

    # Make predictions
    preds_encoded = model.predict(X_processed)

    # Decode predictions back to original labels
    preds = target_encoder.inverse_transform(preds_encoded)

    return preds
