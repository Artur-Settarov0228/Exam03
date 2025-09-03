class Cart:
    def __init__(self):
        self.item = []

    def add_item(self, name , price):
        self.item.append((name, price))

    def get_total(self):
        return sum(price for _, price in self.item)   

cart = Cart()
cart.add_item("Laptop", 2000)
cart.add_item("Mouse", 100)
print(cart.get_total())
