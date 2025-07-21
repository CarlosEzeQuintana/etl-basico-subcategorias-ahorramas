from extract import obtener_productos_categoria, obtener_subcategorias_alimentacion
from transform import transformar_productos
from load import guardar_en_csv

# Extraer dinámicamente las subcategorías reales de "Alimentación"
categorias = obtener_subcategorias_alimentacion()

print(f"Subcategorías encontradas: {list(categorias.keys())}")

# Extraer productos de cada subcategoría
todos = []
for categoria, url in categorias.items():
    print(f"Extrayendo: {categoria}")
    productos = obtener_productos_categoria(categoria, url, max_paginas=20)
    todos.extend(productos)

# Transformar y guardar
df = transformar_productos(todos)
guardar_en_csv(df, ruta='productos_alimentacion.csv')
print(f"\n✅ Proceso completo. Total productos: {len(df)}")
