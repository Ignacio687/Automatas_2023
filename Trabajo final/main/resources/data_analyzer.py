import datetime, pandas as pd, numpy as np, re
from dask import dataframe as df

class DataAnalyzer():
    def __init__(self, file) -> None:
        self.file = file

    def validateData(self):
        pass