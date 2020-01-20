try:
    import geopandas as gpd

    readers = {".shp": gpd.read_file}
except ImportError:
    pass
