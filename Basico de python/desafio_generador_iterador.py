#generador numeros inpares 
def my_generator(limit):
    for i in range(1, limite+1,2):
        yield i


limite = 20



for num in my_generator(limite):
    print(num)



print('--------------------')

#generador numeros pares 
def my_generator(limit):
    for i in range(0, limite+1,2):
        yield i


limite = 20



for num in my_generator(limite):
    print(num)