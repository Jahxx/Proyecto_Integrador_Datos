import os

import pandas as pd
from faker import Faker
import random

fake = Faker(['es_MX'])

nombres_pizzas = [
    "Margherita", "Pepperoni", "Hawaiana", "Cuatro Quesos", "Vegetariana",
    "Barbacoa", "Pollo y Champiñones", "Mexicana", "Carbonara", "Prosciutto"
]

descripciones_pizzas = [
    "Pizza clásica con tomate, mozzarella y albahaca.",
    "Pizza con pepperoni, mozzarella y salsa de tomate.",
    "Pizza con jamón, piña y mozzarella.",
    "Pizza con una mezcla de mozzarella, gorgonzola, parmesano y queso azul.",
    "Pizza con una variedad de verduras frescas y mozzarella.",
    "Pizza con salsa barbacoa, pollo, cebolla y mozzarella.",
    "Pizza con pollo, champiñones, mozzarella y salsa de tomate.",
    "Pizza con jalapeños, chorizo, frijoles y mozzarella.",
    "Pizza con crema, panceta, cebolla y mozzarella.",
    "Pizza con jamón crudo, rúcula y mozzarella."
]


def generar_clientes(n):
    clientes = []
    for _ in range(n):
        cliente = {
            "cliente_id": _ + 1,
            "nombre": fake.name(),
            "direccion": fake.address(),
            "email": fake.email(),
            "telefono": fake.phone_number()
        }
        clientes.append(cliente)
    return pd.DataFrame(clientes)


def generar_productos():
    productos = []
    for _, (nombre, descripcion) in enumerate(zip(nombres_pizzas, descripciones_pizzas)):
        producto = {
            "producto_id": _ + 1,
            "nombre": nombre,
            "descripcion": descripcion,
            "precio": round(random.uniform(150.0, 400.0), 2)
        }
        productos.append(producto)
    return pd.DataFrame(productos)


def generar_pedidos(n, clientes, productos):
    pedidos = []
    for _ in range(n):
        pedido = {
            "pedido_id": _ + 1,
            "cliente_id": random.choice(clientes)['cliente_id'],
            "producto_id": random.choice(productos)['producto_id'],
            "fecha_pedido": fake.date_between(start_date='-1y', end_date='today'),
            "cantidad": random.randint(1, 10),
            "monto_total": round(random.uniform(5.0, 500.0), 2)
        }
        pedidos.append(pedido)
    return pd.DataFrame(pedidos)


# Crear la carpeta 'data' si no existe
os.makedirs('data', exist_ok=True)

# Generar los datos
clientes_df = generar_clientes(100)
productos_df = generar_productos()
pedidos_df = generar_pedidos(500, clientes_df.to_dict('records'), productos_df.to_dict('records'))

# Guardar los datos en archivos CSV
clientes_df.to_csv('data/clientes.csv', index=False)
productos_df.to_csv('data/productos.csv', index=False)
pedidos_df.to_csv('data/pedidos.csv', index=False)
