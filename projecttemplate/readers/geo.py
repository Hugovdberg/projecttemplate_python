from pathlib import Path
from projecttemplate.project import Project

try:
    import geopandas as gpd  # type: ignore

    def shapefile_reader(filename: Path, variable: str, project: Project):
        project.data[variable] = gpd.read_file(filename)

    readers = {".shp": shapefile_reader}
except ImportError:
    readers = {}
