number = {1:'uno', 2:'dos', 3:'tre'}
print(number)


print(number[2])


information = {"nombre":'samuel',
               "apellido":'vasquez'}



print(information)
del information["apellido"]
print(information)
claves = information.keys()
print(claves)

values = information.values()
print(values)


pares = information.items()
print(pares)


constactos = {'samuel':
    {'nombre': 'Samuel',
     'apellido':'Vasquez',
    'telefono:':'999999'},


    'Thiago':
    {'nombre': 'Thiago',
     'apellido':'Vasquez',
    'telefono:':'999999'},
    }

print(constactos['samuel'])