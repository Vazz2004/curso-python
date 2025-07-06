try:
    divisor = int(input('Ingrsa un numero divisaor'))
    result = 100/divisor
    print(result)
except ZeroDivisionError as e :
    print('Error el divisor no pueder dividido')
    print("A ocurrido un error",e)
except ValueError as e:
    print("Deber introducir un numero valido",e)