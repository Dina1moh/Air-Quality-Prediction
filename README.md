# 🌍 Air Quality Index (AQI) Classification Project

## 📌 Project Overview

This project builds a Machine Learning classification system to predict
the **AQI Category** based on different pollutant measurements.

The project includes: - Data preprocessing - Feature engineering - Model
training & evaluation - Model comparison - Saving the best model - Local
deployment using Flask

------------------------------------------------------------------------

## 📂 Dataset

### Original Columns:

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

### Final Dataset (after preprocessing):

The dataset contains **23,035 records** and **7 columns**:

| Column | Type | Description |
|--------|------|-------------|
| Country | object | Country name |
| AQI Category | object | Target variable (air quality classification) |
| CO AQI Value | int64 | Carbon Monoxide AQI measurement |
| Ozone AQI Value | int64 | Ozone AQI measurement |
| NO2 AQI Value | int64 | Nitrogen Dioxide AQI measurement |
| PM2.5 AQI Value | int64 | Fine Particulate Matter AQI measurement |
| pollution_mean | float64 | Engineered feature (mean of all pollutants) |

------------------------------------------------------------------------

## ⚙️ Feature Engineering

### Feature Selection

**Columns Removed:**
- AQI Value
- CO AQI Category
- Ozone AQI Category
- NO2 AQI Category
- PM2.5 AQI Category

**Rationale:** Removed redundant categorical AQI categories and the aggregate AQI Value column to focus on individual pollutant measurements as predictive features.

### Feature Extraction

**New Feature Created:**

- **pollution_mean**: Average of all four pollutant measurements
  
  ```
  pollution_mean = (CO AQI Value + Ozone AQI Value + NO2 AQI Value + PM2.5 AQI Value) / 4
  ```
  
  **Purpose:** Captures overall pollution level as a composite measure, reducing dimensionality while retaining aggregate pollution information.

------------------------------------------------------------------------

## 🔄 Data Preprocessing & Transformation

### Pipeline Architecture

A **ColumnTransformer** pipeline was created handling both numeric and categorical features:

#### Numeric Features Pipeline:
- **Input Features:** CO AQI Value, Ozone AQI Value, NO2 AQI Value, PM2.5 AQI Value, pollution_mean
- **Processing Steps:**
  1. **Imputation:** Missing values handled with median strategy
  2. **Scaling:** StandardScaler applied for model compatibility

#### Categorical Features Pipeline:
- **Input Features:** Country
- **Processing Steps:**
  1. **Imputation:** Missing values handled with most_frequent strategy
  2. **Encoding:** OneHotEncoder applied (with handle_unknown='ignore')

### Target Variable Processing

- **Label Encoding:** AQI Category converted to numeric labels using LabelEncoder
- **Classes:** Good, Moderate, Unhealthy for Sensitive Groups, Unhealthy, Very Unhealthy

### Train-Test Split

- **Test Size:** 20%
- **Random State:** 42 (for reproducibility)
- **Stratification:** Applied to maintain class distribution

------------------------------------------------------------------------

## 🧠 Models Trained & Evaluated

The following 5 classification algorithms were trained and compared:

-   **Logistic Regression** - Linear classification model
-   **Bernoulli Naive Bayes** - Probabilistic classifier
-   **K-Nearest Neighbors (KNN)** - Distance-based classifier with k=7
-   **Random Forest** - Ensemble method with multiple decision trees
-   **Support Vector Machine (SVM)** - Linear kernel SVM

------------------------------------------------------------------------

## 📊 Model Evaluation & Selection

### Evaluation Metrics

Each model was evaluated using:

-   **Confusion Matrix** - Visualized with heatmap
-   **Classification Report** - Precision, Recall, F1-Score per class
-   **Accuracy Score** - Overall correctness

### Best Model: Random Forest

**Random Forest** was selected as the best performing model based on:
- Highest overall accuracy
- Best precision, recall, and F1-score across classes
- Excellent generalization to test data

### Saved Artifacts

-   **best_model.joblib** - Trained Random Forest classifier
-   **transformations.pkl** - Preprocessing pipeline (scaling + encoding)
-   **target_encoder.pkl** - Label encoder for AQI Categories

------------------------------------------------------------------------

## 🚀 How to Run the Training Notebook

### Prerequisites

1. Install dependencies:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib flask
```

### Running the Model Training

1. Navigate to the `model/` directory
2. Open **model.ipynb** in Jupyter Notebook
3. Execute cells sequentially to:
   - Load preprocessed dataset
   - Perform feature engineering (selection & extraction)
   - Apply data transformations
   - Train all 5 classifiers
   - Compare model performance
   - Save the best model and preprocessing artifacts

### Training Output

The notebook generates and saves:
- `best_model.joblib` - Random Forest classifier
- `transformations.pkl` - Preprocessing pipeline
- `target_encoder.pkl` - Target variable encoder
- Performance comparison charts

------------------------------------------------------------------------

## 🌐 Web Deployment

### Flask Application

The project includes a Flask web application for making predictions on new data.

#### Backend Features:
- Loads pre-trained Random Forest model
- Applies feature engineering automatically
- Transforms input using saved preprocessing pipeline
- Returns AQI Category prediction

#### User Workflow:
1. User enters pollutant measurements (CO, Ozone, NO2, PM2.5) and country
2. Backend automatically creates pollution_mean feature
3. Data is transformed using the saved pipeline
4. Model predicts AQI Category
5. Result displayed on the web interface

### Running the Application

```bash
python main.py
```

Application runs at: `http://127.0.0.1:5000/`

### Required Files for Inference
Ensure these artifacts exist in `src/artifacts/`:
- `best_model.joblib` - Trained model
- `transformations.pkl` - Preprocessing pipeline
- `target_encoder.pkl` - Label encoder

------------------------------------------------------------------------

## 📦 Project Structure

```
Air-Quality-Prediction/
├── main.py                          # Flask application entry point
├── README.md                        # Project documentation
├── requirements.txt                 # Python dependencies
│
├── model/
│   ├── model.ipynb                 # Model training notebook
│   ├── best_model.joblib           # Trained Random Forest model
│   └── preprocessed_global_air_pollution_dataset.csv  # Training data
│
├── preprocessing/
│   ├── cleaning_EDA_with_insights.ipynb  # Data cleaning & analysis
│   └── global air pollution dataset.csv   # Raw dataset
│
└── src/
    ├── __init__.py
    ├── main.py
    ├── controller.py                # API endpoints
    ├── inference.py                 # Prediction logic
    ├── schemas.py                   # Data validation schemas
    ├── artifacts/                   # Saved model artifacts
    │   ├── best_model.joblib
    │   ├── transformations.pkl
    │   └── target_encoder.pkl
    └── templates/
        └── index.html               # Web UI
```

------------------------------------------------------------------------

## ✅ Summary

This project successfully builds an end-to-end AQI classification system with the following highlights:

### Data & Features
- **Dataset:** 23,035 global air quality measurements
- **Target Classes:** 5 AQI categories (Good to Very Unhealthy)
- **Feature Engineering:** Created pollution_mean composite metric
- **2-Stage Processing:** Feature selection + extraction

### Model Performance
- **Best Model:** Random Forest Classifier
- **Architecture:** Complete ML pipeline with automated feature transformation
- **Deployment:** Flask web application for real-time predictions

### Key Technologies
- **ML Framework:** scikit-learn
- **Data Processing:** pandas, numpy
- **Visualization:** matplotlib, seaborn
- **Deployment:** Flask

------------------------------------------------------------------------

**Project Status:** ✅ Complete - Model trained, tested, and deployed
