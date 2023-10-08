from fastapi import FastAPI, status, HTTPException, Path
import uvicorn
from feature import Feature
from pathlib import Path
from fastapi.responses import JSONResponse
import pickle


app = FastAPI()
__version__ = "1.0.0"
BASE_LOCATION = Path(__file__).resolve(strict=True).parent


@app.get(path="/user/") # , response_model=Feature)
def get_user():
    # task = Feature(meanRadius=0.0, meaTexture=0.0, meanPerimeter=0.0, meanArea=0.0, meanSmoothness=0.0,
    # meanCompactness=0.0, meanConcavity=0.0, meanConcavePoints=0.0, meanSymmetry=0.0, meanFractalDimension=0.0,
    # radiusError=0.0, textureError=0.0, perimeterError=0.0, areaError=0.0, smoothnessError=0.0,
    # compactnessError=0.0,concavityError=0.0, concavePointsError=0.0,symmetryError=0.0, fractalDimensionError=0.0,
    # worstRadius=0.0, worstTexture=0.0, worstPerimeter=0.0, worstArea=0.0, worstSmoothness=0.0, worstCompactness=0.0,
    # worstConcavity=0.0, worstConcavePoints=0.0, worstSymmetry=0.0, worstFractalDimension=0.0)
    return {"N.B:": 'Breast Cancer Detection'}


@app.get(path='/home')
def index(ip: str):
    return {"Note": "Hello Friends", "Your IP": ip}


with open(f"{BASE_LOCATION}/GaussianNB_Irisdatasets.pkl", "rb") as f:
    model = pickle.load(f)
# with open("GaussianNB_BreastCancer-1.0.0.pkl", "rb") as f:
#     model = pickle.load(f)


@app.post(path='/results')
def predicts(data: Feature):
    print(data)
    mr = data.meanRadius
    mt = data.meaTexture
    mp = data.meanPerimeter
    ma = data.meanArea

    prediction = model.predict([[mr, mt, mp, ma]])
    response_data = {"Prediction": int(prediction[0])}
    return JSONResponse(response_data, status_code=200)


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8080)