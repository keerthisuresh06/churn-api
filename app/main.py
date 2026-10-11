
import joblib
import pandas as pd
import xgboost as xgb
from fastapi import FastAPI
from app.schemas import CustomerFeatures

THRESHOLD = 0.5

app = FastAPI(title="Customer Churn Prediction API")

# Load preprocessing steps
preprocessor = joblib.load("models/churn_preprocessor.joblib")

# Load the trained XGBoost classifier
model = xgb.XGBClassifier()
model.load_model("models/churn_classifier.json")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(customer: CustomerFeatures):
    # Convert customer details into a DataFrame
    X = pd.DataFrame([customer.model_dump()])

    # Apply the same preprocessing used during training
    X_processed = preprocessor.transform(X)

    # Predict churn probability
    probability = float(model.predict_proba(X_processed)[0, 1])
    prediction = int(probability >= THRESHOLD)

    return {
        "churn_prediction": prediction,
        "churn_probability": round(probability, 4)
    }