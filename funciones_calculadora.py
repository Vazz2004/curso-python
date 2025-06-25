def add(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calculadora():
    while True:
        print("\nSeleccione una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        
        option = int(input("Ingrese la opción deseada: "))

        if option == 5:
            print("Saliendo de la calculadora")
            break

        if option in [1, 2, 3, 4]:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            if option == 1:
                print("La suma es:", add(num1, num2))
            elif option == 2:
                print("La resta es:", restar(num1, num2))
            elif option == 3:
                print("La multiplicación es:", multiplicar(num1, num2))
            elif option == 4:
                if num2 != 0:
                    print("La división es:", dividir(num1, num2))
                else:
                    print("Error: No se puede dividir por cero.")
        else:
            print("La opción es incorrecta")

calculadora()
