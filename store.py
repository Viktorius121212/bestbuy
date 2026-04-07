from products import Product
from typing import List, Tuple


class Store:
    """Manages a collection of products and handles bulk orders."""

    def __init__(self, products: List[Product]):
        """Initializes the store with an initial list of products."""
        self.products = products

    def add_product(self, product: Product):
        """Adds a single product to the store inventory."""
        self.products.append(product)

    def remove_product(self, product: Product):
        """Removes a specific product from the store inventory."""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Calculates and returns the total quantity of all active products."""
        total = 0
        for product in self.products:
            if product.is_active():
                total += product.quantity
        return total

    def get_all_products(self) -> List[Product]:
        """Returns a list containing only the active products."""
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """Validates and processes a complete order, returning the total cost."""
        for product, quantity in shopping_list:
            if quantity <= 0:
                raise ValueError(f"Invalid quantity {quantity} requested for {product.name}.")
            if not product.is_active():
                raise ValueError(f"Product {product.name} is completely out of stock/inactive.")
            if quantity > product.quantity:
                raise ValueError(f"Cannot process order. Not enough stock for {product.name}.")

        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price


if __name__ == "__main__":
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
    active_prods = best_buy.get_all_products()

    print(best_buy.get_total_quantity())
    print(best_buy.order([(active_prods[0], 1), (active_prods[1], 2)]))