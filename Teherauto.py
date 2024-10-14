from Auto import Auto

class Teherauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, max_teher):
        super().__init__(rendszam, tipus, berleti_dij)
        self.max_teher = max_teher

    def autoinfo(self):
        return f"{self.tipus} - {self.rendszam}: Max teher: {self.max_teher}, Bérleti díj {self.berleti_dij}Ft/nap"
