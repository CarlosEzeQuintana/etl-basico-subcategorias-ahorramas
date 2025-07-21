def guardar_en_csv(df, ruta='productos.csv'):
    df.to_csv(ruta, index=False)
