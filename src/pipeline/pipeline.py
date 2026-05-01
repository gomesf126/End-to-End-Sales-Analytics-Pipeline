import pandas as pd

from src.transform.cleaning import (
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
