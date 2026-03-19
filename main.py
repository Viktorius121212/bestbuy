import products
import store


def start(store_obj):
    """
    Steuert die Benutzeroberfläche des Stores.
    Das 'while True' sorgt dafür, dass das Menü nach jeder Aktion neu erscheint.
    """
    while True:
        # Menü-Anzeige für den Benutzer
        print("\nStore Menu")
        print("----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Holt nur aktive Produkte.
            # Warum: Wir wollen keine ausverkauften/inaktiven Artikel anzeigen.
            active_items = store_obj.get_all_products()
            for item in active_items:
                print(item)

        elif choice == "2":
            # Nutzt die Methode aus Schritt 2 für die Bestandsprüfung.
            total_qty = store_obj.get_total_quantity()
            print(f"Total amount in store: {total_qty}")

        elif choice == "3":
            # Option 3: Bestellung aufgeben
            shopping_list = []
            items = store_obj.get_all_products()

            # Anzeige mit Index (0, 1, 2...), damit der Nutzer Nummern wählen kann.
            print("------")
            for index, item in enumerate(items):
                print(f"{index}. {item}")
            print("------")
            print("Enter empty text to finish your selection.")

            # Innere Schleife, um mehrere Artikel in einen Warenkorb zu legen
            while True:
                product_num = input("Which product # do you want? ")
                if product_num == "":
                    break

                amount = input("Amount? ")
                if amount == "":
                    break

                try:
                    # Umwandlung der Eingaben.
                    # Warum: input() liefert immer Text (String), wir brauchen Zahlen.
                    idx = int(product_num)
                    qty = int(amount)

                    if 0 <= idx < len(items):
                        # Speichert das Produkt-Objekt und die Menge als Paar (Tupel)
                        shopping_list.append((items[idx], qty))
                        print("Added to list!")
                    else:
                        print("Error: Product number out of range.")
                except ValueError:
                    # Fängt ungültige Zeichen ab
                    print("Error: Please enter a valid number.")

            # Wenn die Liste nicht leer ist, wird die Bestellung ausgeführt
            if shopping_list:
                try:
                    # Die Methode 'order' wickelt die Logik und Bestandskürzung ab
                    total_price = store_obj.order(shopping_list)
                    print(f"Order made! Total price: {total_price}")
                except ValueError as e:
                    # Fängt Fehler aus der buy()-Methode ab (z.B. zu wenig Bestand)
                    print(f"Order failed: {e}")

        elif choice == "4":
            # Beendet die Endlosschleife und damit das Programm
            break
        else:
            print("Invalid choice, please select 1-4.")


# Initialisierung des Inventars laut Spezifikation
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
]
best_buy = store.Store(product_list)

# Einstiegspunkt des Programms
if __name__ == "__main__":
    start(best_buy)