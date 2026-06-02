import os
from fastapi import FastAPI
import joblib
from contextlib import asynccontextmanager
from pydantic import BaseModel
import pandas as pd

ROOT = os.path.dirname(os.path.abspath(__file__))   
MODELS_DIR = os.path.join(ROOT, "models") 

@asynccontextmanager
async def lifespan(app: FastAPI):
    rf_path = os.path.join(MODELS_DIR, "rf.pkl")

    try:
        with open(rf_path, "rb") as f:
            bundle = joblib.load(f)
        app.state.pipeline = bundle["pipeline"]
        app.state.encoder = bundle["label_encoder"]
        print("RF model loaded")
    except Exception as e:
        app.state.pipeline = None
        app.state.encoder = None
        print(f"RF load error: {e}")

    yield
    print("RF service shutting down")

app = FastAPI(lifespan=lifespan)

@app.get("/ready")
def ready():
    return {"ready": app.state.pipeline is not None}

class Features(BaseModel):
    contrast_level: str
    eye_cat: str
    hair_cat: str
    skin_tone: str

@app.post("/predict")
def predict(features: Features):
    data = features.model_dump()
    cols = app.state.pipeline.feature_names_in_
    row_df = pd.DataFrame([data], columns=cols)
    encoded = app.state.pipeline.predict(row_df)[0]
    decoded = app.state.encoder.inverse_transform([encoded])[0]
    return {"season": decoded}