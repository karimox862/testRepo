# testRepo

This repository contains an example Python script to calculate the Normalized Difference Vegetation Index (NDVI) using the Google Earth Engine API.

## Prerequisites

1. Sign up for [Google Earth Engine](https://earthengine.google.com/).
2. Install the Earth Engine Python package:

```bash
pip install earthengine-api
```

3. Authenticate your Earth Engine account:

```bash
earthengine authenticate
```

## Running the example

The script `compute_ndvi.py` demonstrates how to select a Landsat 8 image over a point of interest and compute NDVI. It prints image details and includes commented code showing how to export the result to Google Drive.

Run the script with:

```bash
python compute_ndvi.py
```

Edit the script to customize the date range, location, or export settings as needed.
