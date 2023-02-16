from enum import Enum
from config import CleanConfig
import pandas as pd

from sklearn.decomposition import PCA
from sklearn import preprocessing

class RECEPTS(Enum):
    """
    Different recept types
    """
    DEFAULT= 0
    ROWFILL= 1
    ROWDROP= 2
    COLNA= 3
    COLID= 4
    COLONEHOT= 5
    COLBOOL= 6
    COLNAMES= 7
    PCA= 8
    MANUALDROP= 9
    SCALE = 10
    MINMAX = 11

class Recept:
    """
    Generic recept object.
    A recept takes the input dataframe, performs a transformation over it
    and returns the resulting dataframe.
    """
    def __init__(self, value:list) -> None:
        self.value = value

    def run(self, data: pd.DataFrame) -> pd.DataFrame:
        self._prerun(data)
        return self._run(data)

    def _prerun(self, data: pd.DataFrame) -> None:
        pass

    def _run(self, data: pd.DataFrame) -> pd.DataFrame:
        for col in data.columns:
            pass
        return data

class RowRecept(Recept):
    def __init__(self, value:list) -> None:
        Recept.__init__(self, value)

    def _run(self, data: pd.DataFrame) -> pd.DataFrame:
        return data

class RowFillNARecept(RowRecept):
    def __init__(self, value: list) -> None:
        super().__init__(value)
    def _run(self, data: pd.DataFrame) -> pd.DataFrame:
        return data.fillna(0)

class RowDropNARecept(RowRecept):
    def __init__(self, value: list) -> None:
        super().__init__(value)
    def _run(self, data: pd.DataFrame) -> pd.DataFrame:
        return data.dropna(axis=0)

class ColumnNameRecept(Recept):
    def __init__(self, value:list=[]) -> None:
        Recept.__init__(self, value)

    def _prerun(self, data: pd.DataFrame) -> None:
        self.value = data.columns

    def _run(self, data: pd.DataFrame) -> pd.DataFrame:
        data.columns = [x.replace("&", "").replace(",", "") for x in data.columns]
        return data

class ColumnRecept(Recept):
    def __init__(self, value:list) -> None:
        Recept.__init__(self, value)

    def _run(self, data: pd.DataFrame) -> pd.DataFrame:
        for col in self.value:
            if (col != CleanConfig().TARGET):
                data = self._single_op(data, col)
        return data

    def _single_op(self, data: pd.DataFrame, col: str) -> pd.DataFrame:
        return data

class ReceptNAcol(ColumnRecept):
    def __init__(self, value:list=[]) -> None:
        ColumnRecept.__init__(self, value)
        self.thr = 0.2

    def _prerun(self, data: pd.DataFrame) -> None:
        self.value = data.columns

    def _single_op(self,data: pd.DataFrame, col: str) -> pd.DataFrame:
        res = data[col].isna().value_counts()
        if (res.size==2 and res[1] / (res[0] + res[1]) > self.thr):
            return data.drop(columns=[col])
        return data

class ReceptManualColDrop(ColumnRecept):
    def __init__(self, value:list=[]) -> None:
        ColumnRecept.__init__(self, value)
        self.value = CleanConfig().MANUAL_COL_DROP

    def _single_op(self,data: pd.DataFrame, col: str) -> pd.DataFrame:
        return data.drop(columns=[col])

class ReceptIDcol(ColumnRecept):
    def __init__(self, value:list=[]) -> None:
        ColumnRecept.__init__(self, value)

    def _prerun(self, data: pd.DataFrame) -> None:
        self.value = data.columns

    def _single_op(self, data: pd.DataFrame, col: str) -> pd.DataFrame:
        res = len(data[col].unique())
        if (data.shape[0] == res):
            return data.drop(columns=[col])
        return data

class OneHotRecept(ColumnRecept):
    def __init__(self, value: list) -> None:
        ColumnRecept.__init__(self, value)

    def _single_op(self, data: pd.DataFrame, col: str) -> pd.DataFrame:
        data = data.join(pd.get_dummies(data[col]))
        return data.drop(columns=[col])

class Bool2NumRecept(ColumnRecept):
    def __init__(self, value: list) -> None:
        ColumnRecept.__init__(self, value)

    def _single_op(self, data: pd.DataFrame, col: str) -> pd.DataFrame:
        return data[col].apply(lambda s: 1 if s else 0)

class PcaRecept(Recept):
    def __init__(self, value:int) -> None:
        Recept.__init__(self, value)

    def _run(self, data: pd.DataFrame) -> pd.DataFrame:
        pca = PCA(n_components=self.value)
        k = pca.fit_transform(data.drop(columns=[CleanConfig().TARGET]))
        df = pd.DataFrame({"pca1": k[:, 0], "pca2": k[:, 1]})
        return data.join(df)

class ScaleRecept(Recept):
    def __init__(self, value:int) -> None:
        Recept.__init__(self, value)

    def _run(self, data: pd.DataFrame) -> pd.DataFrame:
        data[data.columns] = preprocessing.StandardScaler().fit_transform(data)
        print(data.head())
        return data

class MinMaxRecept(Recept):
    def __init__(self, value:int) -> None:
        Recept.__init__(self, value)

    def _run(self, data: pd.DataFrame) -> pd.DataFrame:
        data[data.columns] = preprocessing.MinMaxScaler().fit_transform(data)
        print(data.head())
        return data


class ReceptFactory:
    def __init__(self):
        self._content = {
            # generic
            RECEPTS.DEFAULT: Recept,

            # row-based
            RECEPTS.ROWFILL: RowFillNARecept,
            RECEPTS.ROWDROP: RowDropNARecept,

            # column-based
            RECEPTS.COLNA: ReceptNAcol,
            RECEPTS.COLID: ReceptIDcol,
            RECEPTS.COLONEHOT: OneHotRecept,
            RECEPTS.COLBOOL: Bool2NumRecept,
            RECEPTS.MANUALDROP: ReceptManualColDrop,  # temporary

            # headers
            RECEPTS.COLNAMES: ColumnNameRecept,
            # feature engineering
            RECEPTS.PCA: PcaRecept,
            # feature transform
            RECEPTS.SCALE: ScaleRecept,
            RECEPTS.MINMAX: MinMaxRecept,
        }
        self._def = []
        self._params = {
            RECEPTS.DEFAULT: self._def,
            RECEPTS.ROWFILL: self._def,
            RECEPTS.ROWDROP: self._def,
            RECEPTS.COLNA: self._def,
            RECEPTS.COLID: self._def,
            RECEPTS.COLONEHOT: CleanConfig().CATEGORICAL_COLS,
            RECEPTS.COLBOOL: CleanConfig().BOOL_COLS,
            RECEPTS.COLNAMES: self._def,
            RECEPTS.PCA: 2,
            RECEPTS.MANUALDROP: CleanConfig().MANUAL_COL_DROP,
            RECEPTS.SCALE: self._def,
            RECEPTS.MINMAX: self._def,
        }

    def make(self, recept:RECEPTS) -> Recept:
        assert recept in RECEPTS, "Wrong recept identifier, {} not in RECEPTS".format(recept)
        return self._make(recept)
    
    def _make(self, recept:RECEPTS) -> Recept:
        return self._content[recept](self._params[recept])
