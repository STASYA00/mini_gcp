from fastapi import FastAPI, Body
from joblib import load

from predictor import Predictor

app = FastAPI(title="Prediction", description="Endpoint for prediction", version="1.0")
pred = None

@app.on_event("startup")
async def load_model():
    pred = Predictor()
    pass

@app.post("/get", tags=["prediction"])
async def predict(data):
    return pred.run(data)