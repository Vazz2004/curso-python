import random

piedra = 1
papel = 2 
tijera = 3 

print('Bienvenido al juego de piedra papel o tijera')
name_player = str(input('Cual es tu nombre: '))

respuesta = int(input('Por favor escoge el numero que este deacudo a tu elecciona 1.Piedra 2.Papel 3.Tijera '))
respuesta2 = random.randint(1, 3)

if respuesta == 1 and respuesta2 == 2:
    print('perdiste el pc a selecionado Papel','perdio' ,name_player)
elif respuesta == 2 and respuesta2 == 3:
    print('perdiste el pc selecciono tijera','perdio' ,name_player)
elif respuesta == 3 and respuesta2 == 1:
    print('Perdiste el pc a seleccionado piera','perdio' ,name_player)
elif respuesta == 1  and respuesta2 == 2:
    print('ganaste el pc a seleccionado tijera','gano' ,name_player)
elif respuesta == 2 and respuesta2 == 1:
    print('Ganaste el pc a seleccionado Piedra', 'gano' ,name_player)
elif respuesta ==3 and respuesta2 == 2:
    print('Ganaste el pc a seleccionado Papel', 'gano' ,name_player )
else:
    print('Has seleccionado un numero fuera de rango')