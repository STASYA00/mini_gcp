import pandas as pd
from sklearn.utils import resample

from collection import *
from config import CleanConfig
from model import *
from recept import *

class Step:
    def __init__(self, value:list) -> None:
        self.value = value

    def run(self, *args):
        return self._run(*args)

    def _run(self, *args):
        return

class CleaningStep(Step):
    def __init__(self, value:list) -> None:
        Step.__init__(self, value)

    def _run(self, *args) -> pd.DataFrame:
        df = args[0]
        f = ReceptFactory()
        for recept in self.value:
            r = f.make(recept)
            df = r.run(df)
        return df

class DownSamplingStep(Step):
    def __init__(self, value: list=[]) -> None:
        Step.__init__(self, value)
        self._config = CleanConfig()

    def _run(self, *args) -> pd.DataFrame:
        df = args[0]
        downsample = resample(df[df[self._config.TARGET]==self._config.MAJ_CLASS],
             replace=True,
             n_samples=len(df[df[self._config.TARGET]==self._config.MIN_CLASS]),
             random_state=42)
        df = pd.concat([downsample, df[df[self._config.TARGET]==self._config.MIN_CLASS]])
        df.index = range(downsample.shape[0] * 2)
        return df.reindex(index=range(downsample.shape[0] * 2))

class ModelStep(Step):
    def __init__(self, value: list) -> None:
        Step.__init__(self, value)
        # value - list of models, MODELS
        self._config = CleanConfig()

    def _run(self, *args) -> dict:
        df = args[0]
        est = Estimator()
        f = ModelFactory()
        split = self._internal_step(df)
        x = split["x"]
        y = split["y"]

        res = {}

        for m in self.value:
            mod = f.make(m)
            print(mod)
            res[m] = est.cross_val(mod, x, y)

        return res

    def _internal_step(self, df: pd.DataFrame)-> dict:
        _step = SplitYStep()
        return _step.run(df)

class SplitStep(Step):
    def __init__(self, value:list=[]) -> None:
        Step.__init__(self, value)
        self._config = CleanConfig()

    def _run(self, *args) -> dict:
        df = args[0]
        train = df[df[self._config.TARGET].isna()!=True]
        test = df[df[self._config.TARGET].isna()==True]
        return {
            "train": train,
            "test": test
        }

class SplitYStep(Step):
    def __init__(self, value:list=[]) -> None:
        Step.__init__(self, value)
        self._config = CleanConfig()

    def _run(self, *args) -> dict:
        df = args[0]
        
        y = df[self._config.TARGET]
        df.drop(columns=[self._config.TARGET], inplace=True)
        return {
            "x": df,
            "y": y
        }

