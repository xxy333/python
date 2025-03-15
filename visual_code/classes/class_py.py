class BankovniUcet:
    def __init__(self, cislo_uctu, majitel, zustatek):
        self.cislo_uctu = cislo_uctu
        self.majitel = majitel
        self.zustatek = zustatek


    def vloz_penez(self, castka):
        if castka > 0:
            self.zustatek += castka
            return f"{self.zustatek}"
        else:
            return "Nelze vložit zápornou hodnotu"
        

    def vyber_penez(self, castka):
        if castka < self.zustatek:
            self.zustatek -= castka
            return f"Aktuální zůstatek je {self.zustatek}Kč, vybral jste {castka}Kč"
        else:
            return f"Nelze vybrat {castka}, aktuální zůstatek je {self.zustatek}"
        
    def zobraz_stav_penez(self):
        return f"Pro číslo účtu {self.cislo_uctu}, jehož majitel je {self.majitel}, je zůstatek {self.zustatek} Kč"



vybrana_castka = 21000
vlozena_castka = 500
c_u_1 = BankovniUcet(12341234, "Vladimír Vondráček", 20000)


#print(c_u_1.vloz_penez(vlozena_castka))
print(c_u_1.vyber_penez(vybrana_castka))
print(c_u_1.zobraz_stav_penez())

