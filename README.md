\# Customer Churn Prediction API



A machine learning project that predicts whether a telecom customer is likely to leave the service using a trained XGBoost classifier. The model is served through a REST API built with FastAPI.



\## Project Overview



Customer churn prediction helps businesses identify customers who may leave their service. This project takes customer information as input and returns a churn prediction and its estimated probability.



\## Tech Stack



\- Python

\- Pandas and NumPy

\- Scikit-learn

\- XGBoost

\- FastAPI

\- Pydantic

\- Pytest



\## How It Works



1\. Customer details are submitted to the API.

2\. FastAPI validates the input.

3\. A saved preprocessing pipeline transforms the data.

4\. The trained XGBoost model predicts the probability of churn.

5\. The API returns the prediction as JSON.



The model and preprocessor are loaded from saved files. The API performs inference; it does not retrain the model for every request.



\## API Endpoints



| Method | Endpoint | Description |

|---|---|---|

| GET | `/health | Checks whether the API is running |

| POST | `/predict` | Predicts customer churn |



Interactive API documentation is available at `/docs` when the server is running.



\## Example Prediction



Send a POST request to `/predict` with customer details such as:



{

&#x20; "gender": "Female",

&#x20; "SeniorCitizen": 0,

&#x20; "Partner": "Yes",

&#x20; "Dependents": "No",

&#x20; "tenure": 12,

&#x20; "PhoneService": "Yes",

&#x20; "MultipleLines": "No",

&#x20; "InternetService": "Fiber optic",

&#x20; "OnlineSecurity": "No",

&#x20; "OnlineBackup": "Yes",

&#x20; "DeviceProtection": "No",

&#x20; "TechSupport": "No",

&#x20; "StreamingTV": "Yes",

&#x20; "StreamingMovies": "Yes",

&#x20; "Contract": "Month-to-month",

&#x20; "PaperlessBilling": "Yes",

&#x20; "PaymentMethod": "Electronic check",

&#x20; "MonthlyCharges": 85.5,

&#x20; "TotalCharges": 1026.0

}



Example response:





{

&#x20; "churn\_prediction": 1,

&#x20; "churn\_probability": 0.5643

}



A prediction of 1 indicates predicted churn, while 0 indicates predicted non-churn. The probability is the model's estimate, not a guarantee.



\## Run Locally



\### 1. Clone the repository



git clone https://github.com/keerthisuresh06/churn-api.git

cd churn-api



\### 2. Create and activate a virtual environment



On Windows:



```cmd

python -m venv .venv

.venv\\Scripts\\activate



\### 3. Install dependencies



pip install -r requirements.txt



\### 4. Start the API



python -m uvicorn app.main:app --reload



Open 'http://127.0.0.1:8000/docs' to try the API.



\## Run Tests



python -m pytest tests -v



\## Project Structure



churn-api/

├── app/

│   ├── main.py

│   └── schemas.py

├── models/

│   ├── churn\_classifier.json

│   └── churn\_preprocessor.joblib

├── tests/

│   └── test\_api.py

├── .gitignore

├── requirements.txt

└── README.md



\## Future Improvements



\- Document model evaluation metrics.

\- Add tests for invalid inputs and edge cases.

\- Containerize the API using Docker.

\- Explore deployment options.



