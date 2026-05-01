import pandas as pd
from jupyter_core.migrate import regex

from src.extract.extract import extrair_arquivos,montar_tabela

arquivo, errors = extrair_arquivos()
df              = montar_tabela(arquivo)

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
    return(
        df.assign(
            data = lambda x: pd.to_datetime(x['data'].astype(str).str.strip(), errors = 'coerce' , dayfirst=True)
        )
    )

df = tratar_number(df)
df = tratar_nulos_number(df)
df = tratar_data(df)
print(df.columns)
print(df.info())
print(df.isna().sum())