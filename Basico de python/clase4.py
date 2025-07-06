#Cosulta de tipos de datos en Python
name = 'Samuel'
print(type(name))  # <class 'str'>



caracter = 'A'
print(type(caracter))  # <class 'str'>


name2 = '''Samuel

Vasquez
'''


print(name2)  # Samuel\n\nVasquez\n


print(name2[0])
print(name2[1])
print(name2[2])
print(name2[3])



print(name2[-1])



name3 = 'Samuel'
last_name = ' Vasquez '
print(name3+ ' '+ last_name)  # Samuel Vasquez





#name = 'Samuel'
print(name * 5)




print(len(last_name))
print(len(name))

#metodos
print(name.lower())
print(name.upper())

print(last_name.strip())  # Elimina espacios al inicio y al final