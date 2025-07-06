#Crear un iterador de numeros impares

#se establec eun avariable de liminte 
limit = 10 


#se crea un iterador con la funccion iter se le agrega un rango 1 como inicio y se le aplica como fianl el limeite que balla abamsado de dos en dos 
#odd_itter = iter(range(1,limit+1,2))


#usar el iterador

#for num in odd_itter:
 #   print(num)



limt2 = 23 


#de esra manera se ven los numero en secuancia nomar 1,2,3,4,5,6,7,8

add_iteter = iter(range(0, limt2+2))


for num in add_iteter:
    print(num)


print('----------------------------------------------')


add_iteter = iter(range(1, limt2+1,2))


for num in add_iteter:
    print(num)