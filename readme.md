# Proyecto Integrador: Datos Preprocesados

## Descripción

Este repositorio contiene el conjunto de datos ficticios preprocesados generados con la biblioteca Faker para el
proyecto integrador que simula un sistema de gestión de pizzerías. Los datos incluyen información sobre clientes,
productos y pedidos.

## Estructura del repositorio

- `data/`: Carpeta que contiene los archivos de datos generados.
    - `clientes.csv`: Datos de los clientes.
    - `productos.csv`: Datos de los productos.
    - `pedidos.csv`: Datos de los pedidos.
    - `preprocesados/`: Carpeta que contiene los archivos de datos preprocesados
        - `clientes_preprocesados.csv`: Datos de los clientes preprocesados.
        - `productos_preprocesados.csv`: Datos de los productos preprocesados.
        - `pedidos_preprocesados.csv`: Datos de los pedidos preprocesados.
- `scripts/`: Carpeta que contiene los scripts utilizados para el preprocesamiento de los datos.
    - `generar_datos.py`: Script para generar datos ficticios.
    - `preprocesar_datos.py`: Script para preprocesar los datos generados.
- `README.md/`: Documentación del proceso de preprocesamiento.

## Proceso de Generación de Datos

Se utilizó la biblioteca **Faker** de Python para la generación de datos ficticios debido a su flexibilidad y capacidad
para generar diversos tipos de datos de manera sencilla.

### Instrucciones para la Generación de datos

1. **Instalación de Faker**
   ```bash
      pip install faker
   ```
2. **Ejecución del script**
    - El script `generar_datos.py` genera tres archivos CSV (`clientes.csv`, `productos.csv`, `pedidos.csv`) con datos
      ficticios.
    - Para ejecutar el script, se usa el siguiente comando:
   ```bash
      python scripts/generar_datos.py
   ```

## Descripción del Script `generar_datos.py`

El script `generar_datos.py` realiza las siguientes operaciones.

### Generación de Datos para la Tabla de Clientes

* Genera 100 registros de clientes con los campos: `cliente_id`, `nombre`, `direccion`, `email` y `telefono`.

### Generación de Datos para la Tabla de Productos

* Genera 10 registros de productos con los campos: `producto_id`, `nombre`, `descripcion` y `precio`.

### Generación de Datos para la Tabla de Pedidos

* Genera 500 registros de pedidos con los campos: `pedido_id`, `cliente_id`, `producto_id`, `fecha_pedido`, `cantidad`
  y `monto_total`.
* Los campos `cliente_id` y `producto_id` son seleccionados aleatoriamente de las tablas de clientes y productos,
  respectivamente, para simular relaciones entre las tablas.

## Archivos Generados

* **clientes.csv**
    * Contiene los datos de los clientes generados.
    * Columnas: `cliente_id`, `nombre`, `direccion`, `email`, `telefono`.
* **productos.csv**
    * Contiene los datos de los productos generados.
    * Columnas: `producto_id`, `nombre`, `descripcion`, `precio`.
* **pedidos.csv**
    * Contiene los datos de los pedidos generados.
    * Columnas: `pedido_id`, `cliente_id`, `producto_id`, `fecha_pedido`, `cantidad`, `monto_total`.

## Proceso del Preprocesamiento de Datos

El preprocesamiento de Datos incluye la limpieza y transformación de los datos generados para asegurar su calidad y
consistencia antes de ser utilizados en análisis posteriores.

### Técnicas de Preprocesamiento Aplicadas

1. **Eliminación de Duplicados**:
    - Se verifican y eliminan registros duplicados en cada archivo de datos.
2. **Transformación de Datos**:
    - Se imputan valores faltantes utilizando técnicas adecuadas (p. ej. rellenar con la media o la moda) o se eliminan
      registros con valores faltantes críticos.
3. **Corrección de Errores**:
    - Se revisan y corrigen errores en los datos como fechas no válidas o formatos incorrectos de números de teléfono.
4. **Escalado de Variables Numéricas**:
    - Se normalizan o estandarizan las variables numéricas para asegurarse de que estén en una escala comparable.

### Instrucciones para el Preprocesamiento de Datos

1. **Ejecución del script de preprocesamiento**
    * El script `preprocesar_datos.py` realiza las operaciones de preprocesamiento mencionadas anteriormente.
    * Para ejecutar el script, usa el siguiente comando:
    ```bash
      python scripts/preprocesar_datos.py
    ```

### Descripción del Script `preprocesar_datos.py`

El script `preprocesar_datos.py` realiza las siguientes operaciones:

**Limpieza de datos**

* **Eliminación de duplicados**: Verifica y elimina registros duplicados.
* **Manejo de valores faltantes**: Imputa o elimina registros con valores faltantes.

**Transformación de datos**

* **Escalado de variables numéricas**: Normaliza o estandariza las variables numéricas.

## Enlace al Repositorio

- [Repositorio de datos preprocesados]()
