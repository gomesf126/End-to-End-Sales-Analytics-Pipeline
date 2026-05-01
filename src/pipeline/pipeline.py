import pandas as pd
from Demos.OpenEncryptedFileRaw import dst_fname

from src.transform.feature_limpeza import (
    tratar_number,
    tratar_nulos_number,
    tratar_data
    )
def pipeline(df):
    return (
        df
        .pipeline(tratar_number)
        .pipeline(tratar_nulos_number)
        .pipeline(tratar_data)
    )
