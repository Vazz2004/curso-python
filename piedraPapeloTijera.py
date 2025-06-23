import random

piedra = 1
papel = 2 
tijera = 3 

print('Bienvenido a; juego de piedra papel o tijera')
respuesta = int(input('Por favor escoge el numero que este deacudo a tu elecciona 1.Piedra 2.Papel 3.Tijera '))
respuesta2 = random.randint(1, 3)

if respuesta == 1 and respuesta2 == 2:
    print('perdiste el pc a selecionado Papel')
elif respuesta == 2 and respuesta2 == 3:
    print('perdiste el pc selecciono tijera')
elif respuesta == 3 and respuesta2 == 1:
    print('Perdiste el pc a seleccionado piera')
elif respuesta == 1  and respuesta2 == 2:
    print('ganaste el pc a seleccionado tijera')
elif respuesta == 2 and respuesta2 == 1:
    print('Ganaste el pc a seleccionado Piedra')
elif respuesta ==3 and respuesta2 == 2:
    print('Ganaste el pc a seleccionado Papel')
else:
    print('Has seleccionado un numero fuera de rango')