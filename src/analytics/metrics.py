import pandas as pd


def cliente_top(df: pd.DataFrame, top_5: int =5) -> pd.DataFrame:
    return (df
      .query("ano in [2018] and mes_num in [6]")
      [['nome_completo', 'ltv_cliente', 'ultima_compra_cliente','dias_compra_cliente','ranking_cliente']]
     .drop_duplicates('nome_completo')
     .sort_values('ltv_cliente', ascending=False)
     .head(top_5)
     .reset_index(drop=True))



def metricas(df: pd.DataFrame) -> dict:
    return {
        'cliente_top': cliente_top(df)
    }
