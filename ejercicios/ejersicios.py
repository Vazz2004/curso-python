#✅ Ejercicio 1: Sumar todos los números de una lista

numeros = [2,3,4,5,3,6]

j = 0

for i in numeros:
    print(i)
    suma = j + i 
    j = suma
    print('suma',j)



# Ejercicio 2: Mostrar los números impares del 1 al 20
for i in range(1,21): 
    if i % 2 != 0:
        continue
    print(i)


#✅ Ejercicio 3: Buscar una fruta en una lista
frutas = ["manzana", "pera", "naranja", "uva"]

fruta_user = str(input('Escribe la fruta que esats bucando: '))


for i in frutas:
    if i == fruta_user:
        print('se econtro',fruta_user,'y esta en la pocision',frutas.index(i))
    else:
        print('No de ha encontrado la fruta')


#✅ Ejercicio 4: Imprimir los primeros 5 números, pero saltar el 3
x = 0

while x < 5: 

    x += 1
    if x == 3:
        continue
    print(x)


#✅ Ejercicio 5: Contar cuántos números son mayores que 10

numeros = [5, 11, 20, 3, 18, 1]
contador = 0 
for i in numeros:
    if i > 10 :
        contador += 1

print('Numeros mayores a 10 son ',contador)