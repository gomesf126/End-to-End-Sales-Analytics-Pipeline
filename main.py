from src.extract.extract import extrair_arquivos,montar_tabela

def main():

    arquivo, erros = extrair_arquivos()

    if erros:
        raise ValueError(f'Erro ao carregar o arquivo {arquivo}: {erros} ')

    df = montar_tabela(arquivo)
    print(df.head(2))
    return df

if "__main__" == __name__:
    main()