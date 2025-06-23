#Listas 

to_do = ["Dirigirnos al hotel",
         "Ir a almorzar",
         "Visitar un museo",
         "Volver a un hotel"
         ]




print(to_do)

numbers = [1,2,3,4,"Cinco"]

#clase list
print(type(numbers))


#mix de datos 
mix = ["uno",2,3,4,5,True,[1,2,3,4,5]]


print(mix)

print(len(mix))

#iterar en la lsita 


#primer elemento
print("primer elemento", mix[0])



#ultimo elemento 
print("primer elemento", mix[-1])


#iterar en un ramgo 
print(mix[0:2])



print(mix)


#metodo agregando data al final de la lista 
mix.append(False)
print(mix)



mix.append(['a','b','v'])
print(mix)


#metodo para insertar en la posisison deseada 
mix.insert(1,['a','b'])
print(mix)


#consultar datos en lsita 
print(mix.index(['a','b']))



#consultar numeros mayores y menores  

numbers = [1,2,3,4,57070]
print('Mayor',max(numbers))

print('Menor',min(numbers))


#borrar posisiones
del numbers[-1]

print(numbers)

del numbers[:2]
print(numbers)

#Se elimina toda la lista :(
del numbers



