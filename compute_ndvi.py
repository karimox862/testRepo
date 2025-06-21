"""Example script to compute NDVI using the Google Earth Engine API."""

import ee

# Initialize the Earth Engine API. This requires prior authentication.
ee.Initialize()

# Define your area of interest (AOI)
aoi = ee.Geometry.Point([-122.292, 37.901])  # Example: near San Francisco, CA

# Select a satellite image collection. Here we use Landsat 8 surface reflectance data.
collection = (
    ee.ImageCollection('LANDSAT/LC08/C01/T1_SR')
    .filterDate('2020-06-01', '2020-06-30')
    .filterBounds(aoi)
)

# Get the first image from the collection.
image = collection.first()

# Compute NDVI = (NIR - RED) / (NIR + RED)
ndvi = image.normalizedDifference(['B5', 'B4']).rename('NDVI')

# Print the NDVI image details.
print('NDVI image:', ndvi.getInfo())

# Export to Google Drive (uncomment to use; requires export permissions)
# task = ee.batch.Export.image.toDrive(
#     image=ndvi,
#     description='ndvi_example',
#     folder='earth-engine-exports',
#     fileNamePrefix='ndvi_example',
#     region=aoi.buffer(10000).bounds().getInfo()['coordinates'],
#     scale=30
# )
# task.start()
