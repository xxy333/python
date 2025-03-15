class Sklad:
    def __init__(self):
        # Sklad je reprezentován slovníkem, kde klíčem je název produktu
        # a hodnotou další slovník s kategorií a množstvím
        self.produkty = {}

    def pridej_produkt(self, nazev, kategorie, mnozstvi):
        """Přidá nový produkt nebo zvýší množství existujícího."""
        if mnozstvi <= 0:
            return "Množství musí být kladné číslo."
        
        if nazev in self.produkty:
            self.produkty[nazev]['mnozstvi'] += mnozstvi
        else:
            self.produkty[nazev] = {'kategorie': kategorie, 'mnozstvi': mnozstvi}
        
        return f"Produkt {nazev} byl přidán nebo aktualizován."

    def odeber_produkt(self, nazev, mnozstvi):
        """Odebere zadané množství produktu, pokud je k dispozici."""
        if nazev not in self.produkty:
            return f"Produkt {nazev} nebyl nalezen."
        
        if mnozstvi <= 0:
            return "Množství k odebrání musí být kladné číslo."
        
        if self.produkty[nazev]['mnozstvi'] < mnozstvi:
            return f"Nedostatek na skladě. Aktuální množství: {self.produkty[nazev]['mnozstvi']}."
        
        self.produkty[nazev]['mnozstvi'] -= mnozstvi
        
        if self.produkty[nazev]['mnozstvi'] == 0:
            del self.produkty[nazev]  # Odstraní produkt, pokud je množství 0
        
        return f"Produkt {nazev} byl odebrán v množství {mnozstvi}."

    def zobraz_produkty(self):
        """Zobrazí všechny produkty ve skladu."""
        if not self.produkty:
            return "Sklad je prázdný."
        
        produkty_list = []
        for nazev, info in self.produkty.items():
            produkty_list.append(f"{nazev} - {info['kategorie']} - {info['mnozstvi']} ks")
        
        return "\n".join(produkty_list)

    def vyhledej_produkt(self, nazev):
        """Vyhledá informace o konkrétním produktu."""
        if nazev not in self.produkty:
            return f"Produkt {nazev} nebyl nalezen."
        
        info = self.produkty[nazev]
        return f"{nazev} - Kategorie: {info['kategorie']}, Množství: {info['mnozstvi']} ks"

    def celkove_mnozstvi(self):
        """Vrátí celkové množství všech produktů ve skladu."""
        return sum(info['mnozstvi'] for info in self.produkty.values())

    def produkty_v_kategorii(self, kategorie):
        """Vrátí seznam produktů v dané kategorii."""
        produkty = [nazev for nazev, info in self.produkty.items() if info['kategorie'] == kategorie]
        if not produkty:
            return f"V kategorii {kategorie} nejsou žádné produkty."
        
        return produkty


# Příklad použití:
muj_sklad = Sklad()

# Přidání produktů
print(muj_sklad.pridej_produkt("Laptop", "Elektronika", 10))
print(muj_sklad.pridej_produkt("Stůl", "Nábytek", 5))
print(muj_sklad.pridej_produkt("Chleba", "Potraviny", 20))

# Zobrazení produktů
print("\n--- Produkty ve skladu ---")
print(muj_sklad.zobraz_produkty())

# Odebrání produktů
print("\n--- Odebrání chleba ---")
print(muj_sklad.odeber_produkt("Chleba", 5))
print(muj_sklad.zobraz_produkty())

# Vyhledání konkrétního produktu
print("\n--- Informace o produktu Laptop ---")
print(muj_sklad.vyhledej_produkt("Laptop"))

# Statistiky
print("\n--- Statistiky skladu ---")
print(f"Celkové množství: {muj_sklad.celkove_mnozstvi()} ks")
print(f"Produkty v kategorii 'Elektronika': {muj_sklad.produkty_v_kategorii('Elektronika')}")
