
FEATURES = [

]
def aplicar_features(df, features=FEATURES):
    for func in features:
        df = func(df)
    return df
