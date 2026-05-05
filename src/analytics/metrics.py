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
        [['produto','classe_abc','percentual']]
        .drop_duplicates('produto')
        .sort_values('produto')
        .reset_index(drop=True)
     )
def produto_A(df):
    return (
        df
        .query("classe_abc == 'A'")
        [['produto','classe_abc','percentual']]
        .drop_duplicates('produto')
        .sort_values('percentual',ascending=False)
        .reset_index(drop=True)
     )
#drop_duplicates('produto')   1 linha por produto
#groupby('classe_abc')        agrupa por classe
#agg(sum)                     soma faturamento
def faturamento_abc(df):
    return(df
       [['produto','classe_abc','faturamento_produto', 'percentual']]
       .drop_duplicates('produto')
       .groupby('classe_abc', as_index=False)
       .agg(faturamento_abc=('faturamento_produto','sum'))
       .assign(percentual_abc = lambda x: (x['faturamento_abc'] / x['faturamento_abc'].sum()))
       .sort_values('classe_abc')
       .reset_index(drop=True)
    )

def churn_cliente(df):
    return (df
        [['nome_completo','dias_sem_comprar','cliente_inativo','ltv_cliente']]
        .drop_duplicates('nome_completo')
        .assign(
        segmento = lambda x: pd.cut(x['dias_sem_comprar'],
                                    bins=[-1,30,90,180,float('inf')],
                                    labels=['Ativo','Risco','Inativo','Perdido']
                                    )
        )
        .sort_values('dias_sem_comprar', ascending=False)
        .reset_index(drop=True)
    )

def cliente_churn_risco(df):
    return(
            churn_cliente(df)
            .query("segmento == 'Risco'")
           [['nome_completo','dias_sem_comprar','cliente_inativo','segmento','ltv_cliente']]
           .sort_values('ltv_cliente', ascending=False)
           .head(10)
           .reset_index(drop=True)
    )

def metricas(df: pd.DataFrame) -> dict:
    return {
        'cliente_top':         cliente_top(df),
        'produto_top_mes_ano': produto_top_mes_ano(df),
        'produto_top':         produto_top(df),
        'produto_abc':         produto_abc(df),
        'produto_A':           produto_A(df),
        'faturamento_abc':     faturamento_abc(df),
        'churn_cliente':       churn_cliente(df),
        'cliente_churn_risco': cliente_churn_risco(df)
    }
