import csv

new_producto = {
    'name': "Cargador",
    'price':'75',
    "quantity":'100',
    'brand':'ChargeMaster',
    'category':'Accesories'

}

with open('products.csv', mode='a', newline='') as file:
    file.write('\n')
    csv_writer = csv .DictWriter(file,fieldnames= new_producto.keys())
    csv_writer.writerow(new_producto)