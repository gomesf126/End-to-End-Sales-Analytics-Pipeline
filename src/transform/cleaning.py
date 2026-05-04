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
     data = df['data'].astype(str).str.strip()
     data_us = pd.to_datetime(data, format='%m/%d/%Y', errors='coerce')
     data_br = pd.to_datetime(data, format='%d/%m/%Y', errors='coerce')

     return  df.assign( data = lambda x: data_us.fillna(data_br))

def data_ambiguia(df):
    data = df['data'].astype(str).str.strip()
    data_us = pd.to_datetime(data, format='%m/%d/%Y', errors='coerce')
    data_br = pd.to_datetime(data, format='%d/%m/%Y', errors='coerce')

    ambigua = data_us.notna() & data_br.notna() & (data_us != data_br) #se tiver datas ambigua retorna True
    return  df.assign(data_ambigue =  ambigua)

mapa_mes = {
    1:'Jan', 2 :'Fev', 3:'Mar',4:'Abr', 5:'Mai', 6:'Jun',
    7:'Jul', 8:'Ago', 9:'Set', 10:'Out', 11:'Nov', 12:'Dez'
}
def padrao_data(df):
    return (
        df.assign(
            dia=lambda x: x['data'].dt.day,
            mes_num=lambda x: x['data'].dt.month,
            mes=lambda x: x['data'].dt.month.map(mapa_mes),
            ano=lambda x: x['data'].dt.year
        )
        )



def faturamento(df):
    return (
        df.assign(
            faturamento = lambda x: x['preco_unitario'] * x['quantidade_vendida']
        )
    )

