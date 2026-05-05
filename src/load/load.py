from pywinauto.handleprops import parent

from src.config.paths import DATA_PROCESSED
import logging
logger= logging.getLogger(__name__)

def salvar_df(df, name_arquivo='vendas_tratadas.csv'):
    DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
    caminho = DATA_PROCESSED / name_arquivo

    #aqui o arquivo é salvo
    df.to_csv(caminho, index=False, encoding='utf-8-sig')
    logger.info('Arquivo salvo em %s', caminho)

def salvar_metricas(metricas: dict):
    DATA_PROCESSED.mkdir(parents=True, exist_ok=True)

    for nome , df in metricas.items():
        caminho =  DATA_PROCESSED / f"{nome}.csv"
        df.to_csv(caminho, index=False, encoding='utf-8-sig')
        logger.info('Metricas %s salvo em %s',nome, caminho)