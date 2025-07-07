class Order:
    global_disccount = 10 


    def __init__(self, amount):
        self.amount = amount
    @classmethod
    def update_global_discount(cls, new_discount):
        cls.global_disccount = new_discount


Order.global_disccount(15)
print(Order.global_disccount)