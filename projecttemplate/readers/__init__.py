from projecttemplate.projecttemplate import Project
import pandas as pd
from projecttemplate.readers import geo

readers = {".xlsx": pd.read_excel, ".xls": pd.read_excel, ".csv": pd.read_csv}
readers.update(geo.readers)

for extension, reader in readers.items():
    Project.register_reader(extension, reader)
del extension, reader
