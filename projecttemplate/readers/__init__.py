from projecttemplate.project import Project
from projecttemplate.readers import geo, scripts, tabular

__all__ = ["readers"]

readers = {}
readers.update(tabular.readers)
readers.update(scripts.readers)
readers.update(geo.readers)

for extension, reader in readers.items():
    Project.register_reader(extension, reader)
