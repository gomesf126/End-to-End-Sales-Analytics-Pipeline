import pandas as pd
from src.config.paths import DATA_RAW
import logging
logger = logging.getLogger(__name__)

def ler_csv(arquivo):
    try:
        df = pd.read_csv(arquivo , sep="," , encoding='utf8')
    except Exception:
        logger.exception('Erro ao ler o arquivo %s',arquivo)
        raise
    return df

def tratar_coluna(df):
    df.columns= df.columns.astype(str).str.strip().str.lower()
    df = df.loc[:,~df.columns.str.contains('^unnamed', case=False) ]
    df = df.rename(columns={'quantidade vendida':'quantidade_vendida','primeiro nome':'primeiro_nome', 'preco unitario':'preco_unitario'  })
    return df

def validar_coluna(df , arquivo):
    SCHEMAS = ['sku', 'produto', 'quantidade_vendida', 'primeiro_nome', 'sobrenome','data', 'loja', 'preco_unitario']
    obrigatorias = set(SCHEMAS)
    colunas      = set(df.columns)
    faltando     = obrigatorias - colunas
    extra        = colunas      - obrigatorias

    if faltando:
        logger.error(f'Arquivo {arquivo} com colunas faltando {faltando}')
    if extra:
        logger.warning(f'Arquivo com {extra} com colunas extras {arquivo}')
    return df

def extrair_arquivos():
    tabelas =[]
    arquivos_falhos=[]

    for arquivo in DATA_RAW.glob('*.csv'):
        df = ler_csv(arquivo)
        df = tratar_coluna(df)
        df = validar_coluna(df, arquivo)
        tabelas.append(df)
    if not tabelas:
        raise ValueError(f'Nenhum arquivo carregado {arquivo}')
        arquivos_falhos.append(df)

    return tabelas , arquivos_falhos

def montar_tabela(tabelas):
    if not tabelas:
        raise ValueError(f'Erro ao montar a tabela {tabelas}')
    return pd.concat(tabelas, ignore_index=True)
