from pydantic import BaseModel


# class Feature(BaseModel):
#     meanRadius: int
#     meaTexture: int
#     meanPerimeter: int
#     meanArea: float
#     meanSmoothness: float
#     meanCompactness: float
#     meanConcavity: float
#     meanConcavePoints: float
#     meanSymmetry: float
#     meanFractalDimension: float
#     radiusError: float
#     textureError: float
#     perimeterError: float
#     areaError: float
#     smoothnessError: float
#     compactnessError: float
#     concavityError: float
#     concavePointsError: float
#     symmetryError: float
#     fractalDimensionError: float
#     worstRadius: float
#     worstTexture: float
#     worstPerimeter: float
#     worstArea: float
#     worstSmoothness: float
#     worstCompactness: float
#     worstConcavity: float
#     worstConcavePoints: float
#     worstSymmetry: float
#     worstFractalDimension: float



class Feature(BaseModel):
    meanRadius: float
    meaTexture: float
    meanPerimeter: float
    meanArea: float