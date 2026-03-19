class Product:
    def __init__(self, name, price, quantity):
        # Sicherheits-Check: Verhindert, dass fehlerhafte Daten im System gespeichert werden.
        if name == "" or price < 0 or quantity < 0:
            raise ValueError("Ungültige Werte für das Produkt!")

        # Speichern der geprüften Parameter in den Instanzvariablen des Objekts.
        self.name = name
        self.price = price
        self.quantity = quantity
        # Ein neu angelegtes Produkt ist standardmäßig aktiv.
        self.active = True

    def __str__(self):
        # Diese Methode sorgt dafür, dass 'print(produkt)' einen schönen Text ausgibt.
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    # Gibt den aktuell gespeicherten Bestand an den Aufrufer zurück.
    def get_quantity(self):
        return self.quantity

    # Überschreibt den Bestand mit einem neuen Wert und steuert den Aktivitätsstatus.
    def set_quantity(self, quantity):
        # 1. Den neuen Wert in der Instanzvariable speichern.
        self.quantity = quantity

        # 2. Automatische Deaktivierung, falls der Bestand auf 0 fällt.
        if self.quantity == 0:
            self.active = False

    # Gibt den aktuellen Aktivitätsstatus (True oder False) zurück.
    def is_active(self):
        return self.active

    # Schaltet das Produkt manuell auf aktiv.
    def activate(self):
        self.active = True

    # Schaltet das Produkt manuell auf inaktiv.
    def deactivate(self):
        self.active = False

    # Baut die Produktdaten zu einem formatierten String zusammen und gibt diesen aus.
    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    # Führt den Kaufvorgang durch, aktualisiert den Bestand und berechnet den Preis.
    def buy(self, quantity):
        # Abbruch und Fehlermeldung, falls mehr angefragt wird, als auf Lager ist.
        if quantity > self.quantity:
            raise ValueError("Nicht genug auf Lager!")

        # Berechnung des Gesamtpreises für die angefragte Menge.
        total_price = quantity * self.price

        # Aktualisierung des Bestands. Wir nutzen hier die eigene set_quantity-Methode,
        # damit die automatische Prüfung auf Bestand == 0 direkt mit ausgeführt wird.
        self.set_quantity(self.quantity - quantity)

        # Rückgabe des berechneten Preises an das Hauptprogramm.
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