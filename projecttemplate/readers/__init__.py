from projecttemplate.project import Project
from projecttemplate.readers import geo, tabular

__all__ = ["readers"]

readers = {}
readers.update(tabular.readers)
readers.update(geo.readers)

for extension, reader in readers.items():
    Project.register_reader(extension, reader)
