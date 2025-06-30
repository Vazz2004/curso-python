import limpiar_consola
limpiar_consola.limpiarConsola()

class BackAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True


    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Se ha depositado {amount}. Saldo actual {self.balance}")
        else:
            print("La cuenta se encunetra inactiva por favor comuniquese al 101010101010")
     
    def withraw(self , amount):
        if self.active:
            if amount <= self.balence:
                self.balence -= amount
                print(f"Se ha retirado {amount}. saldo actual {self.balence}")

    def desactive_account(self):
        self.is_active =False 
        print(f'La cuneta  ha sido desactivada')

    def active_account(self):
        self.is_active = True 
        print(f'La cuneta  ha sido activada')



account1 = BackAccount("Ana", 500)
account2 = BackAccount("Ana", 200)


#LLamada a los metodods 


account1.deposit(200)
account2.deposit(100)
account1.desactive_account()
account1.deposit(50)

    