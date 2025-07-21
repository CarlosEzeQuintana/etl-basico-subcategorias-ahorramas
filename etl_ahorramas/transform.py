import pandas as pd

def transformar_productos(productos):
    df = pd.DataFrame(productos)
    df['precio'] = df['precio'].str.replace('€', '').str.replace(',', '.').astype(float)
    return df
