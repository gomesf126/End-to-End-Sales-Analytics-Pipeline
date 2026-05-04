import pandas as pd


def cliente_top(df: pd.DataFrame, top_5: int =5) -> pd.DataFrame:
    return (df
      .query("ano in [2018] and mes_num in [6]")
      [['nome_completo', 'ltv_cliente', 'ultima_compra_cliente','dias_compra_cliente','ranking_cliente']]
     .drop_duplicates('nome_completo')
     .sort_values('ltv_cliente', ascending=False)
     .head(top_5)
     .reset_index(drop=True))

def produto_top_mes_ano(df: pd.DataFrame, top_5: int=5)->pd.DataFrame:
    return (
        df.query(" ano == 2018 and mes_num == 6 ")
        [['produto','faturamento_produto_mes_ano','rank_produto_mes_ano','mes','ano']]
        .drop_duplicates('produto')
        .sort_values('faturamento_produto_mes_ano', ascending=False)
        .head(top_5)
        .reset_index(drop=True)#limpa indice e evita criar coluna index
    )

def produto_top(df: pd.DataFrame, top_5: int=5)->pd.DataFrame:
    return(df
        [['produto','faturamento_produto','rank_produto']]
        .drop_duplicates('produto')
        .sort_values('faturamento_produto')
        .head(top_5)
        .reset_index(drop=True)
    )

def produto_abc(df):
    return (
        df
        [[]]
     )









def metricas(df: pd.DataFrame) -> dict:
    return {
        'cliente_top':         cliente_top(df),
        'produto_top_mes_ano': produto_top_mes_ano(df),
        'produto_top'        : produto_top(df)
    }
