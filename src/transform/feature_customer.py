
def feature_customer(df):
     return df.assign(
                  nome_completo = lambda x: x['primeiro_nome'].fillna('').str.strip() +' '+ x['sobrenome'].fillna('').str.strip(),
                  ltv_cliente = lambda x: x.groupby('nome_completo')['faturamento'].transform('sum'),
                  quantidade_compra_cliente = lambda x: x.groupby('nome_completo')['quantidade_vendida'].transform('sum')
            ).assign(
                  ticket_medio_cliente    = lambda x: x['ltv_cliente'] / x['quantidade_compra_cliente'],
                  ultima_compra_cliente   = lambda x: x.groupby('nome_completo')['data'].transform('max'),
                  primeira_compra_cliente = lambda x: x.groupby('nome_completo')['data'].transform('min'),
                  dias_ultima_compra_cliente = lambda x: (x['data'].max() - x['ultima_compra_cliente']).dt.days
      )


