class Product:
    def __init__(self, name, price, quantity):
        if name == "" or price < 0 or quantity < 0:
            raise ValueError("Ungültige Werte für das Produkt!")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        # 1. Den neuen Wert in der Instanzvariable speichern
        self.quantity = quantity

        # 2. Prüfen, ob das Produkt deaktiviert werden muss
        if self.quantity == 0:
            self.active = False

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        if quantity > self.quantity:
            raise ValueError ("Nicht genug auf Lager!")
        total_price = quantity * self.price
        self.set_quantity(self.quantity - quantity)
        return total_price

bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()


