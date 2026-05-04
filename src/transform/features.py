from src.transform.cleaning import tratar_number,tratar_nulos_number,tratar_data,faturamento,data_ambiguia,feature_tempo
from src.transform.feature_customer import feature_customer
from src.transform.feature_product import feature_produto
from src.transform.feature_abc import feature_produto_abc
from src.transform.feature_churn import feature_churn_produto
FEATURES = [
    tratar_number,
    tratar_nulos_number,
    tratar_data,
    data_ambiguia,
    faturamento,
    feature_customer,
    feature_tempo,
    feature_produto,
    feature_produto_abc,
    feature_churn_produto
]
def aplicar_features(df, features=FEATURES):
    for func in features:
        df = func(df)
    return df
