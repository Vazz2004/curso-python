def suma(a: int,b:int ) :
    res = a + b
    return res

def resta(a: int,b:int ) :
    res = a - b
    return res


def multiplicacion(a: int,b:int ) :
    res = a * b
    return res

def divicion(a: int,b:int ) :
    if b == 0:
        raise ValueError('El divisor deber ser difente a 0')
    return a/b

if __name__ == '__main__':
    print('Opéraciones')
    res_1 = suma(3,4)
    print(f'la suma es {res_1}')
