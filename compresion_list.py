squares = [x**2 for x in  range(1,11)]


#print('Los cuadrados son:', squares)



celcius = [0,10,20,30,40]
fahrenheit = [(temp * 9/5)* 32 for temp in celcius]
#print('temperatura en grados farenheit: ',  fahrenheit)



evens = [x for x in range(1,21) if x%2 != 0]

print(evens)


print('---------------------------')


evens = [x for x in range(1,21) if x%2 == 0]

print(evens)



print('--------------------')


matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]
        ]


transpuesta = [[row[i] for row in matrix] for i in range(len(matrix[0]))]


print(matrix)
print(transpuesta)



