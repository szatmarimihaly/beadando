class Berles:
    def __init__(self, auto, berles_datum):
        self.auto = auto
        self.berles_datum = berles_datum

    def berlesinfo(self):
        return f"Autó: {self.auto.tipus} - {self.auto.rendszam} | Dátum: {self.berles_datum}"
