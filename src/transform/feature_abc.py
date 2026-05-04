import numpy as np

def feature_produto_abc(df):
    base_bac = (
        df[['produto','faturamento_produto']]
        .drop_duplicates('produto')
        .sort_values('faturamento_produto', ascending=False)
        .reset_index(drop=True)

        .assign(
            percentual = lambda x: x['faturamento_produto'] / x['faturamento_produto'].sum(),
            percentual_acumulado =lambda x: x['percentual'].cumsum(),
            classe_abc = lambda x: np.select([ x['percentual_acumulado'] <= 0.80, x['percentual_acumulado'] <= 0.95  ], ['A' , 'B'], default= 'C' )
        )
    )
    return (
        df.merge(base_bac[['produto','percentual','percentual_acumulado','classe_abc']], on='produto', how='left')
    )