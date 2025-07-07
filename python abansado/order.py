class Order:

    @staticmethod
    def calcukle_tax(amount, tax_rate):
        return amount * (tax_rate/100)
    

print(Order.calcukle_tax(1000, 18))