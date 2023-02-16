import pandas as pd

from config import CleanConfig
from experiment import BaseExperiment

if __name__ == "__main__":
    conf = CleanConfig()
    df = pd.read_csv(conf.FILENAME, index_col=0)
    exp = BaseExperiment()
    exp.run(df)