from cart import Cart

class User:
    def __init__(self, data):
        self.f_name = data['f_name']
        self.l_name = data['l_name']
        self.email = data['email']
        self.balance = 0
        self.cart = Cart()

    @staticmethod
    def static_method(data):
        if type(data["f_name"]) != "string":
            return("that doesn't work")

    @classmethod
    def class_method(cls):
        # Go to Database, grab one User
        # pass the result through constructor
        #  cls(results)
        pass

    def add_funds(self, amount):
        self.balance += amount
        return self
    
    def buy_item(self, product):
        self.cart.add_item(product)
        return self
    
    def rem_item(self, product_name):
        self.cart.remove_item(product_name)

    def checkout(self):
        if self.balance < self.cart.total:
            print("Sorry you don't have enough funds!")
        else:
            self.balance -= self.cart.total
            print("You have just purchased:")
            for item in self.cart.items:
                print(f'{item.name} for ${item.price}')
            print(f'A total of {self.cart.total} has been deducted from your balance.')
            print("Your new balance is $" + self.balance)
            self.cart.items = []
            self.cart.total = 0
        return self