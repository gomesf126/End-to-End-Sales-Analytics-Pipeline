from src.extract.extract import extrair_arquivos,montar_tabela
from src.pipeline.pipeline import pipeline
from src.analytics.metrics import metricas
import pandas as pd

def main():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_colwidth', None)

    arquivo, erros = extrair_arquivos()
    if erros:
        raise ValueError(f'Erro ao carregar o arquivo {arquivo}: {erros} ')

    df = montar_tabela(arquivo)

    df = pipeline(df)
    metrica = metricas(df)


    for nome , tabela in metrica.items():
        print(nome)
        print(tabela)

    return df

if "__main__" == __name__:
    main()