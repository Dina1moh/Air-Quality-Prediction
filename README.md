# 🌍 Air Quality Index (AQI) Classification Project

## 📌 Project Overview

This project builds a Machine Learning classification system to predict
the **AQI Category** based on different pollutant measurements.

The project includes: - Data preprocessing - Feature engineering - Model
training & evaluation - Model comparison - Saving the best model - Local
deployment using Flask

------------------------------------------------------------------------

## 📂 Dataset

The dataset contains the following columns:

-   Country
-   AQI Value
-   AQI Category (Target)
-   CO AQI Value
-   CO AQI Category
-   Ozone AQI Value
-   Ozone AQI Category
-   NO2 AQI Value
-   NO2 AQI Category
-   PM2.5 AQI Value
-   PM2.5 AQI Category

------------------------------------------------------------------------

## ⚙️ Feature Engineering

Two additional features were created:

### 1️⃣ Max_Pollutant

Maximum value among: - CO AQI Value - Ozone AQI Value - NO2 AQI Value -
PM2.5 AQI Value

### 2️⃣ High_Pollutant_Count

Counts how many pollutants fall into: - Unhealthy - Very Unhealthy -
Hazardous

------------------------------------------------------------------------

## 🧠 Models Used

The following models were trained and evaluated:

-   Logistic Regression
-   Bernoulli Naive Bayes
-   KNN
-   Decision Tree
-   Random Forest
-   Support Vector Machine (SVM)

------------------------------------------------------------------------

## 📊 Evaluation Metrics

Each model was evaluated using:

-   Confusion Matrix
-   Classification Report
-   Accuracy Score

The best performing model was saved as:

    best_model.joblib

The preprocessing pipeline was saved as:

    transformations.pkl

------------------------------------------------------------------------

## 🚀 How to Run the Training Notebook

1.  Install dependencies:

```{=html}
<!-- -->
```
    pip install pandas numpy matplotlib seaborn scikit-learn xgboost joblib flask

2.  Run the training script / notebook.

------------------------------------------------------------------------

## 🌐 Deployment

The project includes a local Flask web application:

-   User inputs pollutant values
-   Backend performs feature extraction
-   Data is transformed
-   Model predicts AQI Category
-   Result displayed on UI

To run locally:

    python main.py

Open browser:

    http://127.0.0.1:5000/

------------------------------------------------------------------------

## 📦 Project Structure

    project_root/
    │
    ├── main.py
    ├── src/
    │   ├── artifacts/
    │   ├── inference/
    │   ├── controllers/
    │   ├── schemas/
    │   └── templates/

------------------------------------------------------------------------

## ✅ Author

Machine Learning Project -- AQI Classification
