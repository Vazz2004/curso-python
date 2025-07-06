#Doble de los Números
#Dada una lista de números [1, 2, 3, 4, 5], crea una nueva lista que contenga el doble de cada número usando una List Comprehensio

numbers = [1,2,3,4,5]
numbers2 = [x+x for x in numbers]

print('El doble de la lista es: ',numbers2)


print('--------------------------------------------------------------')


#Filtrar y Transformar en un Solo Paso
#Tienes una lista de palabras ["sol", "mar", "montaña", "rio", "estrella"] y quieres obtener una nueva lista con las palabras que tengan más de 3 letras y estén en mayúsculas.

palabras = ["sol", "mar", "montaña", "rio", "estrella"]

resultado = [palabra.upper() for palabra in palabras if len(palabra) > 3]

print(resultado)



