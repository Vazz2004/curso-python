#🧩 Ejercicio 1: Suma total en una lista de listas

numeros = [
    [1, 2, 3],
    [4, 5],
    [6]
]

contador = 0

for i in numeros:
    resultado = i
    for b in resultado:
        contador += b 


print(contador)

