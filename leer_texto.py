import limpiar_consola
limpiar_consola.limpiarConsola()

#Leer un archivo linea por linea
'''with open('cuento.txt','r') as file:
    for lineas in file:
        print(lineas)'''


#Leer todas las lieneas en una lista
'''with open('cuento.txt','r') as file:
    lines = file.readlines()
    print(lines)'''


#Escribir al final
'''with open('cuento.txt','a') as file:
    file.write("holaaaa")'''

#Sobre escribir el texto 
'''with open('cuento.txt','w') as file:
    file.write('Hola')'''


#Reto de conteo de lineas del cuento

contador= 0

with open('cuento.txt','r') as file:
    for lineas in file:
        print(lineas) 
        contador += 1


print('Lineas de este cuento',contador)