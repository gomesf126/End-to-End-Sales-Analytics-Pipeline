import logging

from src.extract.extract import extrair_arquivos,montar_tabela
from src.pipeline.pipeline import pipeline
from src.analytics.metrics import metricas
from src.load.load import salvar_df,salvar_metricas
import pandas as pd
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(message)s"
)
def main():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_colwidth', None)

    arquivo, erros = extrair_arquivos()
    logging.info("Iniciando extração")

    if erros:
        logging.warning(f"Arquivo com erro: {erros}")

    df = montar_tabela(arquivo)

    df = pipeline(df)

    metrica = metricas(df)

    logging.info("Salvando dados...")
    salvar_df(df)
    salvar_metricas(metrica)

    for nome , tabela in metrica.items():
        print(nome)
        print(tabela)

    return df

if "__main__" == __name__:
    main()