class Product:
    """Represents a product in the store with stock and price management."""

    def __init__(self, name: str, price: float, quantity: int):
        """Initializes a new product with strict validation rules."""
        if not name or not str(name).strip():
            raise ValueError("Invalid name: cannot be empty or only whitespace.")
        if price < 0 or quantity < 0:
            raise ValueError("Invalid price or quantity: cannot be negative.")

        self.name = str(name).strip()
        self.price = float(price)
        self.quantity = int(quantity)
        self.active = True

    def __str__(self) -> str:
        """Returns a formatted string containing product details."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def get_quantity(self) -> int:
        """Returns the current stock quantity."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """Updates the stock quantity and deactivates if stock reaches zero."""
        self.quantity = quantity
        if self.quantity <= 0:
            self.active = False

    def is_active(self) -> bool:
        """Returns True if the product is active, False otherwise."""
        return self.active

    def activate(self):
        """Activates the product manually."""
        self.active = True

    def deactivate(self):
        """Deactivates the product manually."""
        self.active = False

    def show(self):
        """Prints the formatted product details to the console."""
        print(self.__str__())

    def buy(self, quantity: int) -> float:
        """Processes a purchase, updates stock, and returns the total price."""
        if quantity <= 0:
            raise ValueError("Quantity to buy must be greater than zero.")
        if not self.active:
            raise ValueError(f"Product '{self.name}' is currently inactive.")
        if quantity > self.quantity:
            raise ValueError(f"Not enough stock for '{self.name}'.")

        total_price = quantity * self.price
        self.set_quantity(self.quantity - quantity)
        return total_price


if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()