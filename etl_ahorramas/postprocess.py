import pandas as pd

# Leer el CSV generado por el ETL
df = pd.read_csv('productos_alimentacion.csv')

# Agrupar productos por nombre, unificando categorías
df_agrupado = (
    df.groupby('nombre')
    .agg({
        'categoria': lambda x: ', '.join(sorted(set(x))),
        'precio': 'first'
    })
    .reset_index()
)

# Guardar nuevo archivo procesado
df_agrupado.to_csv('productos_agrupados.csv', index=False)

print(f"✅ Procesado. Total únicos: {len(df_agrupado)}")
