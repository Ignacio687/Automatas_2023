import datetime, pandas as pd, numpy as np, re
from dask import dataframe as df

class IncorrectFileFormat(Exception):
    pass

class DataValidator():
    def __init__(self, file: str) -> None:
        self.file == file

    def validate(self):
        pass

    def generateFile(self, filter: bool):
        pass