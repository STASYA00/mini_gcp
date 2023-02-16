import pandas as pd

from singleton_meta import SingletonMeta

class Log(metaclass=SingletonMeta):
    """
    Object that contains the parameters for the detection algorithm
    :params: category       category of the objects to detect, int
    :params: confidence     min confidence to accept, float
    """
    def __init__(self) -> None:

        self._name = "log.csv"
        self._initiate()
        self.content = pd.read_csv(self._name)

    def _initiate(self):
        _empty = pd.DataFrame(columns=["id", "name", "model", "res"])
        _empty.to_csv(self._name)

    def write(self, d):
        self.content = pd.concat([self.content, pd.DataFrame(d)])
        self.content.to_csv(self._name)