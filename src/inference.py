import joblib
import pandas as pd

# load artifacts
model = joblib.load("src/artifacts/best_model.joblib")
transformations = joblib.load("src/artifacts/transformations.pkl")
target_encoder = joblib.load("src/artifacts/target_encoder.pkl")


def create_features(df: pd.DataFrame):

    df["pollution_mean"] = (
        df["CO AQI Value"]
        + df["Ozone AQI Value"]
        + df["NO2 AQI Value"]
        + df["PM2.5 AQI Value"]
    ) / 4

    return df


def predict_aqi_category(input_df: pd.DataFrame):

    df = create_features(input_df.copy())

    X_processed = transformations.transform(df)

    preds_encoded = model.predict(X_processed)

    preds = target_encoder.inverse_transform(preds_encoded)

    return preds