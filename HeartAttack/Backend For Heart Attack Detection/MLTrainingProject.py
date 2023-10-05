from fastapi import FastAPI
import uvicorn
from pathlib import Path
import pickle
from fastapi.responses import JSONResponse
from allColumns import Features

app = FastAPI()
__version__ = "1.0.0"
BASE_LOCATION = Path(__file__).resolve(strict=True).parent


@app.get(path="/users")
def get_user():
    return {"Project Title": "Heart Attack Diagnostics Classification using Bernoulli Naive Bayes"}


with open(f"{BASE_LOCATION}/BernoulliNB_HeartAttackDetection.pkl", "rb") as file:
    model = pickle.load(file)


@app.post(path="/results")
def forecast(data: Features):
    prediction = model.predict([[data.age, data.sex, data.cp, data.trtbps, data.chol, data.fbs,
                                 data.restecg, data.thalachh, data.exng, data.oldpeak, data.slp,
                                 data.caa, data.thall]])
    response_data = {"Heart Attack Diagnostics Classification : ": float(prediction[0])}
    return JSONResponse(response_data, status_code=200)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
