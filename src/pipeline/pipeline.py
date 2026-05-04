from src.transform.features import aplicar_features
def pipeline(df):
    return (
        df
        .pipe(aplicar_features)

    )
