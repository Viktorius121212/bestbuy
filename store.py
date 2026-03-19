from products import Product

# Holt das Etikett "List" aus der Typen-Bibliothek.
# um später die Autovervollständigung (z.B. .buy()) für die Listen-Elemente anzubieten.
from typing import List

class Store:
    # Nimmt bei Erstellung des Stores eine fertige Liste entgegen und speichert sie.
    def __init__(self, products):
        self.products = products

    # Hängt ein neues Produkt ans Ende der Store-Liste an.
    def add_product(self, product):
        self.products.append(product)

    # Sucht das spezifische Produkt in der Liste und löscht es.
    def remove_product(self, product):
        self.products.remove(product)

    # Zählt den gesamten Lagerbestand aller Produkte zusammen.
    def get_total_quantity(self) -> int:
        total = 0
        for product in self.products:
            total += product.quantity
        return total

    # Filtert die Hauptliste und gibt eine neue Liste NUR mit aktiven Produkten zurück.
    def get_all_products(self) -> List[Product]:
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    # Verarbeitet eine Liste aus Tupeln (Pärchen aus Produkt und Menge).
    def order(self, shopping_list) -> float:
        total_price = 0.0
        for product, quantity in shopping_list:
            # product.buy() reduziert den Bestand
            # im Produkt selbst und gibt uns praktischerweise direkt den Teilpreis zurück.
            total_price += product.buy(quantity)
        return total_price


product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250),
]

best_buy = Store(product_list)
products = best_buy.get_all_products()

print(best_buy.get_total_quantity())
print(best_buy.order([(products[0], 1), (products[1], 2)]))