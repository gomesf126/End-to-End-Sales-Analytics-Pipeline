from src.transform.cleaning import tratar_number,tratar_nulos_number,tratar_data,faturamento,data_ambiguia,padrao_data
from src.transform.feature_customer import feature_customer
FEATURES = [
    tratar_number,
    tratar_nulos_number,
    tratar_data,
    data_ambiguia,
    faturamento,
    feature_customer,
    padrao_data
]
def aplicar_features(df, features=FEATURES):
    for func in features:
        df = func(df)
    return df
