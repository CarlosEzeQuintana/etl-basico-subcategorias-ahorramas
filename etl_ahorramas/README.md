# 🛒 ETL de productos de supermercado Ahorramás

Este proyecto realiza un proceso **ETL (Extract, Transform, Load)** sobre los productos de la categoría **"Alimentación"** del sitio oficial de [Ahorramás](https://www.ahorramas.com/), extrayendo datos reales de sus subcategorías internas de manera automatizada.

---

## 📌 ¿Qué hace este proyecto?

- 🔎 Detecta dinámicamente todas las **subcategorías de "Alimentación"**
- 🧱 Extrae el **nombre del producto, categoría y precio**
- 🔄 Agrupa productos con múltiples categorías
- 💾 Guarda los resultados en formato `.csv` listo para análisis

---

## 📦 Estructura del proyecto

```
etl_ahorramas/
├── main.py                    ← Orquesta el flujo ETL
├── extract.py                 ← Scraping de productos y subcategorías
├── transform.py               ← Limpieza básica (por ejemplo, precio a float)
├── load.py                    ← Guarda los datos en CSV
├── postprocess.py             ← Agrupa productos por nombre
├── productos_alimentacion.csv ← Salida sin procesar (con duplicados)
├── productos_agrupados.csv    ← Salida agrupada por producto
├── requirements.txt
└── README.md
```

---

## ▶️ Cómo usar

### 1. Clonar el repositorio

```bash
git clone https://github.com/CarlosEzeQuintana/etl_ahorramas.git
cd etl_ahorramas
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Ejecutar el flujo ETL

```bash
python main.py
```

Esto generará el archivo `productos_alimentacion.csv` con todos los productos encontrados.

### 4. (Opcional) Agrupar productos por nombre

```bash
python postprocess.py
```

Esto generará el archivo `productos_agrupados.csv` con productos únicos y sus categorías consolidadas.

---

## 🧪 Resultado esperado

**Ejemplo de salida (productos agrupados):**

| producto                        | categorias                              | precio |
| ------------------------------- | --------------------------------------- | ------ |
| Aceite de oliva virgen Alipende | aceite-vinagre-y-sal, productos-basicos | 6.99   |
| Arroz SOS 1Kg                   | arroces-pastas-legumbres, sin-gluten    | 1.85   |

---

## 🧠 Consideraciones

- Algunos productos aparecen en múltiples categorías. No se eliminan por defecto.
- Se ofrece un script adicional (`postprocess.py`) para agruparlos por nombre y combinar categorías.

---

## 🚀 Mejoras posibles

- Agregar histórico de precios por fecha
- Guardar en base de datos (SQLite, PostgreSQL)
