from pathlib import Path

import pandas as pd  # type: ignore

from projecttemplate.project import Project


def excel_reader(filename: Path, variable: str, project: Project) -> None:
    if filename.name.startswith("~$"):
        return
    xl = pd.ExcelFile(filename)
    for sheet_name in xl.sheet_names:
        varname = "_".join([variable, sheet_name])
        df = xl.parse(sheet_name)
        if df.shape != (0, 0):
            project.data[varname] = df


def csv_reader(filename: Path, variable: str, project: Project) -> None:
    project.data[variable] = pd.read_csv(filename)


readers = {".xlsx": excel_reader, ".xls": excel_reader, ".csv": csv_reader}
