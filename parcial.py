import pandas as pd
import random

sucursales = ['San Salvador', 'Santa Ana', 'San Miguel', 'La Libertad', 'Sonsonate']
productos = ['Laptop', 'Monitor', 'Teclado', 'Mouse', 'Impresora']
categorias = ['Computación', 'Periféricos', 'Impresión']

datos = []
for i in range(100):
    datos.append({
        'ID_Producto': i + 1,
        'Producto': random.choice(productos),
        'Categoria': random.choice(categorias),
        'Precio': round(random.uniform(15.0, 800.0), 2),
        'Stock': random.randint(10, 100),
        'Sucursal': random.choice(sucursales)
    })

dfInventario = pd.DataFrame(datos)
dfInventario.to_csv('inventario.csv', index=False)
print("Archivo 'inventario.csv' generado con éxito.")