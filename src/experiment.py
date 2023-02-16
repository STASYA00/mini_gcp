import uuid

from log import Log
from recept import RECEPTS
from step import *

class Experiment:
    def __init__(self) -> None:
        self._name = "generic"
        self._sequence = []  # steps
        self._recepts = []   # recepts
        self._models = []
        self._logger = Log()

    def run(self, df):
        return self._run(df)

    def _run(self, df):
        for step in self._sequence:
            print(step)
            if step==CleaningStep:
                s = step(self._recepts)
            elif step==ModelStep:
                s = step(self._models)
            else:
                s = step()
            df = s.run(df)
        for model, res in df.items():
            print(model, res)
            self._log(self._name, model, res)

    def _log(self, name, model, res):
        self._logger.write({"id": [uuid.uuid4()],
                            "name": [name], 
                            "model": [model],
                            "res": [res]})

class BaseExperiment(Experiment):
    def __init__(self) -> None:
        Experiment.__init__(self)
        self._name = "base"
        self._sequence = [CleaningStep, DownSamplingStep, ModelStep]
        self._models = [MODELS.BASE, MODELS.XGB, MODELS.LGBM, MODELS.CATB]
        self._recepts = [
            
            RECEPTS.COLID,
            RECEPTS.COLNA,
            RECEPTS.COLONEHOT,
            RECEPTS.MANUALDROP,
            RECEPTS.ROWFILL,
            RECEPTS.PCA,
            
            RECEPTS.COLNAMES,
            RECEPTS.MINMAX,
        ]
