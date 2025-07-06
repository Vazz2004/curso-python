# limpiar_consola.py debe tener la función definida correctamente
import limpiar_consola
limpiar_consola.limpiarConsola()


class Carro:
    def __init__(self, modelo, precio):
        self.modelo = modelo
        self.precio = precio
        self.disponible = True 

    def compra_carro(self):
        if self.disponible:
            self.disponible = False
            print(f"El carro {self.modelo} ha sido comprado exitosamente por {self.precio}")
        else:
            print("El carro no se encuentra disponible")

    def __str__(self):
        return f"{self.modelo} - ${self.precio}"


class Concesionario:
    def __init__(self):
        self.carros = []
        self.users = []

    def agregar_carros(self, carro):
        self.carros.append(carro)    
        print(f"El carro {carro} ha sido agregado con éxito")
    
    def agregar_usuario(self, usuario):
        self.users.append(usuario)

    def ver_carros(self):
        for carro in self.carros:
            if carro.disponible:
                print(carro)


class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.carros_comprados = []

    def compra_carro(self, carro):
        if carro.disponible:
            carro.compra_carro()
            self.carros_comprados.append(carro)
            print(f'El carro {carro} fue agregado a la lista de compras de {self.nombre} (ID: {self.user_id})')


# Uso del programa
carro1 = Carro('Audi cd4', '1200000')
carro2 = Carro('Logan cd4', '4200000')

user1 = Usuario('Samuel Vasquez', '001')

mi_concesionario = Concesionario()
mi_concesionario.agregar_carros(carro1)
mi_concesionario.agregar_carros(carro2)

user1.compra_carro(carro1)

print("\nCarros disponibles en concesionario:")
mi_concesionario.ver_carros()
