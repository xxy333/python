class Auto:
    def __init__(self, znacka, model, r_vyroby, tachometr, kapacita_nadrze, stav_nadrze):
        self.znacka = znacka
        self.model = model
        self.r_vyroby = r_vyroby
        self.tachometr = tachometr
        self.kapacita_nadrze = kapacita_nadrze
        self.stav_nadrze = stav_nadrze


    def vypis_info(self):
        return f"Značka auta je {self.znacka} {self.model}, rok výroby {self.r_vyroby}. Stav tachometru je {self.tachometr}Km. Kapacita nádrže je {self.kapacita_nadrze}l, aktuální stav paliva v nádrži je {self.stav_nadrze}l."
     
    

    #clear
    def jed(self, vzdalenost):

        self.tachometr = self.tachometr + vzdalenost
        self.stav_nadrze = self.stav_nadrze - ((vzdalenost / 100) * 7)
        if self.stav_nadrze < 0:
            return "Není dostatek paliva na cestu"
        else:
            return f"Nový stav tachometru je {self.tachometr} a nový stav paliva je {self.stav_nadrze}"        

    def natankuj(self, kapacita):
        
        if self.kapacita_nadrze < self.stav_nadrze + kapacita:
            return "Nádrž je plná"
            

        else:
            self.stav_nadrze = self.stav_nadrze + kapacita
            return f"Aktuální stav paliva je {self.stav_nadrze}"
         




auto_1 = Auto("Skoda","Superb",2020 ,110000 ,50 ,45)

vzdalenost = 1000
dotankuj = 4

print(auto_1.natankuj(dotankuj))
