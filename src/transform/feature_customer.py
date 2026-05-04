
def feature_customer(df):
     return df.assign(
                  nome_completo = lambda x: x['primeiro_nome'].fillna('').str.strip() +' '+ x['sobrenome'].fillna('').str.strip(),
                  ltv_cliente = lambda x: x.groupby('nome_completo')['faturamento'].transform('sum'),
                  quantidade_compra_cliente = lambda x: x.groupby('nome_completo')['quantidade_vendida'].transform('sum')
            ).assign(
                  ultima_compra_cliente   = lambda x: x.groupby('nome_completo')['data'].transform('max'),
                  primeira_compra_cliente = lambda x: x.groupby('nome_completo')['data'].transform('min'),
                  dias_compra_cliente = lambda x: (x['data'].max() - x['ultima_compra_cliente']).dt.days
            ).assign(
                  ranking_cliente = lambda x: x['ltv_cliente'].rank(method='dense', ascending=False).astype(int)
     )


