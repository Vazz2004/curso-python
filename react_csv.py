import csv

#leer un archivo 
'''with open('products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)'''

#mostrar la informacion por colimnas
'''with open('products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(F"productos: {row['name']}, Precio {row['price']}")'''


new_producto = {
    'name': "Cargador",
    'price':"75",
    "quantity":'100'
}

with open('products.csv', mode='a', newline='') as file:
    file.write('\n')
    csv_writer = csv.DictWriter(file,fieldnames= new_producto.keys())
    csv_writer.writer(new_producto)