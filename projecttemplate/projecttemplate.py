# -*- coding: utf-8 -*-
"""ProjectTemplate

Class to describe project templates and create projects from them
"""
from pathlib import Path

import pandas as pd

from .util import AttrDict


class Project:

    _readers = {}

    def __init__(self, projdir=Path()):
        self.projdir = Path(projdir)

        self.data = AttrDict()
        self.lib = None

    @property
    def datadir(self):
        return self.projdir / "data"

    @property
    def mungedir(self):
        return self.projdir / "munge"

    @property
    def libdir(self):
        return self.projdir / "lib"

    @classmethod
    def register_reader(cls, extension, reader, overwrite=False):
        if extension in cls._readers and not overwrite:
            raise ValueError(
                (
                    "Reader for extension {ext!r} already registered,"
                    " use overwite=True to replace the current reader"
                ).format(ext=extension)
            )
        cls._readers[extension] = reader

    def load_libs(self):
        from runpy import run_path

        print("Loading library functions")
        libs = []
        for f in self.libdir.iterdir():
            if f.suffix != ".py":
                continue
            print("\tLoading", repr(f.stem))
            file = run_path(f, run_name=f.stem)
            if f.stem in file:
                libs.append((f.stem, file[f.stem]))
        self.lib = AttrDict(libs)

    def list_data(self):
        """
        list_data Lists all the datasets in the current project

        Lists the files with the corresponding variable name and reader
        to load the dataset.

        Returns
        -------
        pandas.DataFrame
            DataFrame with the files in the 'data' directory, the corresponding
            variable name and the reader function to load the data.
        """
        data = pd.DataFrame(
            [
                {
                    "file": f.name,
                    "variable": f.stem,
                    "reader": self._readers.get(f.suffix, None),
                }
                for f in self.datadir.iterdir()
            ]
        )
        data.loc[data["reader"].isnull(), "variable"] = None
        return data

    def load_data(self):
        print("Loading data from disk")
        for _, row in self.list_data().iterrows():
            if pd.isnull(row["reader"]):
                continue
            print("\tLoading", repr(row["variable"]))
            self.data[row["variable"]] = row["reader"](self.datadir / row["file"])

    def munge_data(self):
        from runpy import run_path

        print("Running munge scripts on data")
        for f in self.mungedir.iterdir():
            if f.suffix != ".py":
                continue
            print("\tRunning", repr(f.stem), "...")
            run_path(f, init_globals={"project": self})

    def load_project(self):
        self.load_libs()
        self.load_data()
        self.munge_data()

    def create_project(self, create_parents=False):
        self.projdir.mkdir(parents=create_parents, exist_ok=True)
        self.libdir.mkdir(exist_ok=True)
        self.datadir.mkdir(exist_ok=True)
        self.mungedir.mkdir(exist_ok=True)
