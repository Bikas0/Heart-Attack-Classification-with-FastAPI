from pydantic import BaseModel


class Features(BaseModel):
    age: float
    sex: float
    cp: float
    trtbps: float
    chol: float
    fbs: float
    restecg: float
    thalachh: float
    exng: float
    oldpeak: float
    slp: float
    caa: float
    thall: float
