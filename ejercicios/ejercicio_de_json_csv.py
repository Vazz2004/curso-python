import json
import csv
import limpiar_consola

limpiar_consola.limpiarConsola()

file_path_json = 'products.json'
file_path_csv = 'products_new.csv'

# Abrir el JSON y cargar los productos
with open(file_path_json, mode='r') as file_json:
    products_json = json.load(file_json)

# Preparar archivo CSV
with open(file_path_csv, mode='w', newline='') as file:
    fieldnames = ['name', 'price', 'quantity']
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

    csv_writer.writeheader()  # Escribir encabezado

    for row in products_json:
        product_object = {
            'name': row['name'],
            'price': row['price'],
            'quantity': row['quantity']
        }
        csv_writer.writerow(product_object)
