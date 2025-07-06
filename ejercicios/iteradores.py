#ejemplo de iteradores 

my_list = [1,2,3,4]


#obtener un iterador
my_iter = iter(my_list)



print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


#iterar en cadenas de texto

text = "Hola mundo"


iter_tex = iter(text)


for char in iter_tex:
    print(char)

