class Sklad:
    def __init__(self):

        self.produkt = {}



    def pridej_produkt(self, nazev, pocet, cena):
        if cena and pocet > 0:
            if nazev in self.produkt:
                self.produkt[nazev]["nazev"] += pocet
                return f"Existující produkt {nazev} vložen do skladu. Aktuální počet ve skladu je {pocet} kusů"
            elif nazev not in self.produkt:
                self.produkt[nazev] = {"pocet": pocet, "nazev" : nazev}
                return f"Nový produkt {nazev} s cenou {cena} přidán do skladu. Aktuální stav kusů je {pocet}"
        else:
            return "Nelze vkládat hodnoty s nulovou cenou nebo počtem"
        


    def odebrat_polozku(self, nazev, mnozstvi):
        if mnozstvi in self.produkt > mnozstvi:
            if nazev in self.produkt:
                self.produkt[nazev]["nazev"] -= mnozstvi
            else:
                return f"Položka s názvem {nazev} se ve skladu nevyskytuje"
        else:
            return f"Bylo překročeno množstvi, takový počet kusů produktu ve skladu není"
        


    def zobraz_sklad(self):

        return f"Aktuální stav položek ve skladu je {self.produkt}"
    

    def celkova_hodnota_skladu(self):
        return f"Celková hodnota skladu je {self.produkt}"





muj_sklad = Sklad()



print(muj_sklad.pridej_produkt("iPhone 15", 10, 15000))
print(muj_sklad.odebrat_polozku("iPhone 15", 5))