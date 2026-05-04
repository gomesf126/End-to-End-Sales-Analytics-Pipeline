from src.transform.cleaning import tratar_number,tratar_nulos_number,tratar_data,faturamento,data_ambiguia,padrao_data
from src.transform.feature_customer import feature_customer
from src.transform.feature_product import feature_produto
from src.transform.feature_abc import feature_produto_abc
FEATURES = [
    tratar_number,
    tratar_nulos_number,
    tratar_data,
    data_ambiguia,
    faturamento,
    feature_customer,
    padrao_data,
    feature_produto,
    feature_produto_abc
]
def aplicar_features(df, features=FEATURES):
    for func in features:
        df = func(df)
    return df
