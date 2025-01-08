import pandas as pd


def get_producao_csv(ano):
    df = pd.read_csv("files/Producao.csv", sep =';', usecols=['id', 'control', 'produto', str(ano)])
    print(df)


get_producao_csv(2023)