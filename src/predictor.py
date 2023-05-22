from enum import Enum
from joblib import load

from recept import RECEPTS
from step import CleaningStep

class PREDS(Enum):
    CLASS= "Result"
    LOG= "Log_Proba"

class Prediction:
    def __init__(self, keys:list=[]) -> None:
        self._keys = keys
        self._fmt = {x:0 for x in self._keys}

    def fmt(self, data:list):
        assert len(data) >= len(self._keys)
        for i in len(self._keys):
            self._fmt[self._keys[i]] = data[i]
        return self._fmt
    
class PredictionClass(Prediction):
    def __init__(self, keys:list=[PREDS.CLASS]) -> None:
        Prediction.__init__(self, keys)

class PredictionLogProba(Prediction):
    def __init__(self, keys:list=[PREDS.CLASS]) -> None:
        Prediction.__init__(self, keys)

class PredictionComposedClass(Prediction):
    def __init__(self, keys:list=[PREDS.CLASS, PREDS.LOG]) -> None:
        Prediction.__init__(self, keys)

    
class Predictor:
    def __init__(self):
        self._sequence = [CleaningStep]
        self._recept = self._load_recept()
        self._model = self._load()
        self._prediction = PredictionClass()

    def run(self, data):
        return self._run(data)

    def _load(self):
        return None 
    
    def _load_recept(self):
        return []
    
    def _fmt_pred(self, data):
        return {"Result": data[0],
                "Log_proba": data[1]
                }
    
    def _run(self, data):
        for step in self._sequence:
            if step==CleaningStep:
                s = step(self._recepts)
            else:
                s = step()
            data = s.run(data)
        res = self._model.predict(data)
        return self._prediction.fmt(res)