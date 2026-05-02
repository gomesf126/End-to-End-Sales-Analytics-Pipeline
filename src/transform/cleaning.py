import pandas as pd

def tratar_number(df):
    return ( df
             .assign(
                quantidade_vendida = lambda x:pd
                                    .to_numeric(x['quantidade_vendida']
                                    .astype(str)
                                    .str.strip() ,errors='coerce'),
                preco_unitario     =lambda x: pd.to_numeric(x['preco_unitario']
                                   .astype(str)
                                   .str.strip()
                                   .str.replace(r'[^\d,.-]','', regex=True)
                                   .str.replace('.','', regex=False)
                                   .str.replace(',','.', regex=False))
            )

    )#
def tratar_nulos_number(df):
    return (
        df.assign(
                quantidade_vendida = lambda x: x['quantidade_vendida'].fillna(0).astype(int),
                preco_unitario     = lambda x: x['preco_unitario'].fillna(x['preco_unitario'].median()).astype(float)
        )
    )

def tratar_data(df):
     df = df.assign(
            data = lambda x: pd.to_datetime(x['data']
                    .astype(str)
                    .str.strip()
                    , format='%m/%d/%Y'
                    , errors= 'coerce')
        )

     return df



def faturamento(df):
    return (
        df.assign(
            faturamento = lambda x: x['preco_unitario'] * x['quantidade_vendida']
        )
    )

