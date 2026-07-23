import ee

PROJECT_ID = "agrimind-503213"

ee.Initialize(project=PROJECT_ID)

print("Connected!")

image = (
    ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
    .limit(1)
    .first()
)

print(image.getInfo()["id"])