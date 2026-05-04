
def feature_produto(df):
    return (
        df.assign(
            faturamento_produto         = lambda x: (x.groupby('produto')['faturamento'].transform('sum')),
            rank_produto                = lambda x: (x['faturamento_produto'].rank(method='dense', ascending=False).astype(int)),
            faturamento_produto_mes_ano = lambda x: (x.groupby(['produto','ano','mes_num'])['faturamento'].transform('sum')),
            rank_produto_mes_ano        = lambda x: (x.groupby(['ano','mes_num'])['faturamento_produto_mes_ano'].rank(method='dense', ascending=False).astype(int))
        )
    )
