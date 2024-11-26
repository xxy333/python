


class Sklad:
    def __init__(self, nazev, kategorie, mnozstvi):
        self.nazev = nazev
        self.kategorie = kategorie
        self.mnozstvi = mnozstvi



    def pridej_produkt(self, nazev, kategorie, mnozstvi):
        self.nazev = nazev
        self.kategorie = kategorie
        self.mnozstvi = mnozstvi




muj_sklad = Sklad()




produkt_1 = Sklad("Telefon", "Elektronika", 5)
produkt_2 = Sklad("Melouny", "Potraviny", 15)
produkt_3 = Sklad("Postel", "Nábytek", 2)


print(muj_sklad.pridej_produkt(produkt_1))

#print(produkt_1.pridej_produkt())
#print(produkt_2.pridej_produkt())
#print(produkt_3.pridej_produkt())



