from shapely.geometry import Point
import geopandas as gpd
import time

from config import *

def load_boundaries():
    start = time.time()
    lad_gdf = gpd.read_file(BOUNDS_PATH)
    lad_gdf = lad_gdf.to_crs(epsg=4326)

    duration = time.time() - start
    print(f"Completed in {duration}s")

    return lad_gdf

def gps_to_region(lat, lon, lad_gdf):
    point = Point(lon, lat)
    photo_gdf = gpd.GeoDataFrame(geometry=[point], crs="EPSG:4326")
    result = gpd.sjoin(photo_gdf, lad_gdf, how="left", predicate="within")

    if result.empty:
        return "Unknown"
    return result['LAD25NM'].iloc[0]

