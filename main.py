import products
import store

def start(store_obj: store.Store):
    """Initializes and runs the interactive command-line interface for the store."""
    while True:
        print("\nStore Menu")
        print("----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            active_items = store_obj.get_all_products()
            for item in active_items:
                print(item)

        elif choice == "2":
            total_qty = store_obj.get_total_quantity()
            print(f"Total amount in store: {total_qty}")

        elif choice == "3":
            shopping_list = []
            items = store_obj.get_all_products()

            print("------")
            for index, item in enumerate(items):
                print(f"{index}. {item}")
            print("------")
            print("Enter empty text to finish your selection.")

            while True:
                product_num = input("Which product # do you want? ")
                if product_num == "":
                    break

                amount = input("Amount? ")
                if amount == "":
                    break

                try:
                    idx = int(product_num)
                    qty = int(amount)

                    if 0 <= idx < len(items):
                        selected_product = items[idx]

                        # NEU: Sofortige Validierung VOR dem Hinzufügen zur Liste
                        if qty <= 0:
                            print("Error: Amount must be greater than zero.")
                        elif qty > selected_product.get_quantity():
                            print(f"Error: Not enough stock! Only {selected_product.get_quantity()} available.")
                        else:
                            shopping_list.append((selected_product, qty))
                            print("Added to list!")
                    else:
                        print("Error: Product number out of range.")
                except ValueError:
                    print("Error: Please enter a valid number.")
            if shopping_list:
                try:
                    total_price = store_obj.order(shopping_list)
                    print(f"Order made! Total price: {total_price}")
                except ValueError as e:
                    print(f"Order failed: {e}")

        elif choice == "4":
            break
        else:
            print("Invalid choice, please select 1-4.")


product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
]
best_buy = store.Store(product_list)

if __name__ == "__main__":
    start(best_buy)