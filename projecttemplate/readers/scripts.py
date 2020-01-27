from pathlib import Path
from runpy import run_path

from projecttemplate.project import Project


def python_reader(filename: Path, variable: str, project: Project) -> None:
    file = run_path(str(filename), run_name=variable, init_globals={"project": project})
    if variable in file:
        project.data[variable] = file[variable]


readers = {".py": python_reader}
