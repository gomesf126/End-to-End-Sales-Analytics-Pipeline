import pandas as pd


def feature_churn_produto(df:pd.DataFrame, dias_churn: int= 90)->pd.DataFrame:
    data_maxima = df['data'].max()
    return(df
           .assign(
             ultima_compra = lambda x:(x.groupby('nome_completo')['data'].transform('max')),
             dias_sem_comprar = lambda x: ( data_maxima -  x['ultima_compra']).dt.days,
             cliente_inativo  = lambda x:(x['dias_sem_comprar'] > dias_churn)
        )
      )