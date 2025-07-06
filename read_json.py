import json

file_path = 'products.json'
#Lectura de archvio
with open('products.json',mode='r') as file :
    prducts = json.load(file)


for produc in prducts:
   # print(produc)
   print(f"producto {produc['name']}")




new_producto = {
    'name': "Cargador",
    'price':"75",
    "quantity":'100'
}


prducts.append(new_producto)


with open(file_path , mode='w') as file :
    json.dump(prducts, file , indent='')