from enum import Enum
from joblib import dump
import sklearn
from sklearn.linear_model import LogisticRegression
from catboost import CatBoostClassifier, Pool
from xgboost import XGBClassifier
import lightgbm as lgb

from config import CleanConfig

class MODELS(Enum):
    BASE= 0
    XGB = 1
    LGBM= 2
    CATB= 3

class ModelFactory:
    def __init__(self) -> None:
        self._content = {
            MODELS.BASE: LogisticRegression(random_state=0),
            MODELS.XGB: XGBClassifier(n_estimators=12, 
                                      max_depth=2, 
                                      learning_rate=0.5, 
                                      objective='binary:logistic'),
            MODELS.LGBM: lgb.LGBMClassifier(class_weight={0:1., 1:1.}),
            MODELS.CATB: CatBoostClassifier(iterations=2,
                                            depth=2,
                                            learning_rate=1,
                                            loss_function='Logloss',
                                            verbose=True)
        }

    def make(self, ind:MODELS):
        assert ind in MODELS, "Model {} is not implemented".format(ind)
        return self._content[ind]

class Estimator:
    def __init__(self) -> None:
        self._splits = 10

    def measure(self, y_pred, y_test):
        return sklearn.metrics.accuracy_score(y_pred, y_test)

    def cross_val(self, model, X_train, y_train):
        return sklearn.model_selection.cross_val_score(model, X_train, y_train, cv=self._splits).mean()

class Register:
    def __init__(self) -> None:
        self._content = {
            MODELS.BASE: Register.dump,
            MODELS.XGB: Register.dump_bst,
            MODELS.LGBM: Register.dump,
            MODELS.CATB: Register.dump,
        }
    
    def run(self, model, model_type):
        return self._run(model, model_type) 

    def _run(self, model, model_type):
        return self._content[model_type](model)

    @staticmethod
    def dump(model):
        dump(model, "{}/{}.joblib".format(CleanConfig().MODEL_REGISTRY, "model"))

    @staticmethod
    def dump_bst(model):
        model.save_model("{}/{}.bst".format(CleanConfig().MODEL_REGISTRY, "model"))

