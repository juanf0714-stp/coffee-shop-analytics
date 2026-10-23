#

# Cargar librerías necesarias e importar el dataset
from pathlib import Path
import pandas as pd

file_path = Path("data/Coffee Shop Sales.xlsx")

df = pd.read_excel(file_path)

print("\n--- DIMENSIONES DEL DATASET ---")
print(f"Filas: {df.shape[0]:,}")
print(f"Columnas: {df.shape[1]}")

print("\n--- COLUMNAS ---")
print(df.columns.tolist())

print("\n--- TIPOS DE DATOS ---")
print(df.dtypes)

print("\n--- VALORES FALTANTES ---")
print(df.isna().sum())

print("\n--- REGISTROS DUPLICADOS ---")
print(df.duplicated().sum())

print("\n--- PRIMERAS 5 FILAS ---")
print(df.head())

print("\n--- RANGO DE FECHAS ---")
dates = pd.to_datetime(df["transaction_date"], errors="coerce")
print(f"Fecha mínima: {dates.min()}")
print(f"Fecha máxima: {dates.max()}")
print(f"Fechas inválidas: {dates.isna().sum()}")

# Cálculo de métricas de negocio
print("\n--- VALIDACIONES DE NEGOCIO ---")

print("Cantidad mínima:", df["transaction_qty"].min())
print("Cantidad máxima:", df["transaction_qty"].max())

print("Precio mínimo:", df["unit_price"].min())
print("Precio máximo:", df["unit_price"].max())

print("Transacciones únicas:", df["transaction_id"].nunique())

print("Locales:")
print(df["store_location"].value_counts())

print("\nCategorías:")
print(df["product_category"].value_counts())

# Calcular ingresos por línea de producto
df["revenue"] = df["transaction_qty"] * df["unit_price"]

total_revenue = df["revenue"].sum()
total_transactions = df["transaction_id"].nunique()
total_units = df["transaction_qty"].sum()
average_ticket = total_revenue / total_transactions

print("\n--- KPIs INICIALES ---")
print(f"Ingresos totales: ${total_revenue:,.2f}")
print(f"Transacciones: {total_transactions:,}")
print(f"Unidades vendidas: {total_units:,}")
print(f"Ticket promedio: ${average_ticket:,.2f}")

print("\n--- INGRESOS POR LOCAL ---")
print(
    df.groupby("store_location")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

# Validar si una misma transacción tiene más de una fila o varios productos
print("\n--- VALIDACIÓN DE TRANSACCIONES ---")

rows_per_transaction = df.groupby("transaction_id").size()

print("Transacciones con más de una fila:",
      (rows_per_transaction > 1).sum())

print("Máximo de filas por transacción:",
      rows_per_transaction.max())

print("Transacciones con más de una unidad:",
      (df["transaction_qty"] > 1).sum())

print("\n--- INGRESOS POR CATEGORÍA ---")
print(
    df.groupby("product_category")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .round(2)
)

