import os 
os.system('clear')


class Persona:
    def __init__(self, name , age):
        self.name = name
        self.age = age 

    def greet(self):
        print(f"Hola mi nombre es {self.name} y tengo {self.age} ")




Persona1 = Persona("Ana", 30 )
Persona2 = Persona("Luis",25)



Persona1.greet()