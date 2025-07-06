
def divide(a: int , b :int) -> float:
   #validar que anbos parametros sean enteros
   if not isinstance(a,int) or not isinstance(b,int):
      raise TypeError('Ambos parametros debe ser enteros')
   if b == 0 :
      raise ValueError('B deber ser difente de 0 ')
   return a/b


#Ejemplo de uso 

try:
   res = divide(10, 2)
   print(res)

except (ValueError, TypeError) as e :
    print(f'Error {e}')

