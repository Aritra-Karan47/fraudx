from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd
import os

from .blockchain_service import get_wallet_transactions
from .feature_engineering import compute_features

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
features = joblib.load(os.path.join(BASE_DIR, "model_features.pkl"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/analyze")
def analyze_wallet(data: dict):

    wallet = data["wallet"]

    transactions = get_wallet_transactions(wallet)

    if not transactions:
        return {"error": "No transactions found"}

    feature_dict = compute_features(wallet, transactions)

    input_df = pd.DataFrame([feature_dict])[features]

    prob = model.predict_proba(input_df)[0][1]

    risk_score = int(prob * 100)

    return {
        "wallet": wallet,
        "risk_score": risk_score,
        "fraud_probability": prob
    }
