"""Compute NDVI from Landsat imagery using Google Earth Engine."""

import argparse
import ee


def parse_args() -> argparse.Namespace:
    """Return command line arguments."""
    parser = argparse.ArgumentParser(description="Compute NDVI with Google Earth Engine")
    parser.add_argument("--lat", type=float, default=37.901, help="Latitude for the AOI center")
    parser.add_argument("--lon", type=float, default=-122.292, help="Longitude for the AOI center")
    parser.add_argument("--start", type=str, default="2020-06-01", help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end", type=str, default="2020-06-30", help="End date (YYYY-MM-DD)")
    parser.add_argument(
        "--export",
        action="store_true",
        help="Export the resulting NDVI image to Google Drive",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    # Initialize the Earth Engine API. Make sure you authenticated first.
    ee.Initialize()

    aoi = ee.Geometry.Point([args.lon, args.lat])

    collection = (
        ee.ImageCollection("LANDSAT/LC08/C01/T1_SR")
        .filterDate(args.start, args.end)
        .filterBounds(aoi)
    )

    image = collection.first()
    if image is None:
        raise RuntimeError("No imagery found for the specified parameters.")

    ndvi = image.normalizedDifference(["B5", "B4"]).rename("NDVI")
    print("NDVI image info:", ndvi.getInfo())

    if args.export:
        task = ee.batch.Export.image.toDrive(
            image=ndvi,
            description="ndvi_example",
            folder="earth-engine-exports",
            fileNamePrefix="ndvi_example",
            region=aoi.buffer(10000).bounds().getInfo()["coordinates"],
            scale=30,
        )
        task.start()
        print("Export task started. Check the Earth Engine tasks panel.")


if __name__ == "__main__":
    main()
