import os

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Cargar los datos
clientes_df = pd.read_csv('data/clientes.csv')
productos_df = pd.read_csv('data/productos.csv')
pedidos_df = pd.read_csv('data/pedidos.csv')

# 1. Eliminación de datos duplicados
clientes_df = clientes_df.drop_duplicates()
productos_df = productos_df.drop_duplicates()
pedidos_df = pedidos_df.drop_duplicates()

# 2. Manejo de valores faltantes
# Imputar valores faltantes en `clientes_df`
clientes_df['email'] = clientes_df['email'].fillna('unknown@example.com')
clientes_df['telefono'] = clientes_df['telefono'].fillna('000-000-0000')

# Imputar valores faltantes en `productos_df`
productos_df['descripcion'] = productos_df['descripcion'].fillna('No description available')

# Imputar valores faltantes en `pedidos_df`
pedidos_df['cantidad'] = pedidos_df['cantidad'].fillna(pedidos_df['cantidad'].mean())
pedidos_df['monto_total'] = pedidos_df['monto_total'].fillna(pedidos_df['monto_total'].mean())

# 3. Escalado de variables numéricas
scaler = MinMaxScaler()

# Escalar las variables numéricas en `productos_df` (se escalan entre 150 y 400)
productos_df['precio'] = scaler.fit_transform(productos_df[['precio']]) * (400 - 150) + 150

# Escalar las variables numéricas de cantidad en `pedidos_Df (se escalan entre 1 y 10)
pedidos_df['cantidad'] = scaler.fit_transform(pedidos_df[['cantidad']]) * 9 + 1
pedidos_df['cantidad'] = pedidos_df['cantidad'].round().astype(int)

# Escalar las variables numéricas de monto_total en `pedidos_Df (se escalan entre 5 y 500)
pedidos_df['cantidad'] = scaler.fit_transform(pedidos_df[['cantidad']]) * (500 - 5) + 5

# Guardar los datos preprocesados en nuevos archivos CSV
os.makedirs('data/preprocesados', exist_ok=True)

clientes_df.to_csv('data/preprocesados/clientes_preprocesados.csv', index=False)
productos_df.to_csv('data/preprocesados/productos_preprocesados.csv', index=False)
pedidos_df.to_csv('data/preprocesados/pedidos_preprocesados.csv', index=False)
