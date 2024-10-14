from Auto import Auto

class Szemelyauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, utasok_szama):
        super().__init__(rendszam, tipus, berleti_dij)
        self.utasok_szama = utasok_szama

    def autoinfo(self):
        return f"{self.tipus} - {self.rendszam}: Szállítható utasok: {self.utasok_szama}, Bérleti díj {self.berleti_dij}Ft/nap"
