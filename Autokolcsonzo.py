from Berles import Berles

class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def hozzaad_auto(self, auto):
        self.autok.append(auto)

    def autok_listazasa(self):
        for auto in self.autok:
            status = "elérhető✔️" if not auto.berelve else "bérbeadva❌"
            print(f"{auto.autoinfo()} - {status}")

    def berles(self, rendszam, datum, auto_tipus):
        for auto in self.autok:
            if auto.rendszam == rendszam and isinstance(auto, auto_tipus) and not auto.berelve:
                auto.berelve = True
                uj_berles = Berles(auto, datum)
                self.berlesek.append(uj_berles)
                print(f"Sikeresen kibérelted: {auto.tipus} ({auto.rendszam})")
                return
        print(f"❌Az autó {rendszam} nem érhető el bérlésre.❌")

    def berlesek_listazasa(self):
        if not self.berlesek:
            print("❌Jelenleg nincs aktív bérlés.❌")
        else:
            for berles in self.berlesek:
                print(berles.berlesinfo())

    def berles_lemondasa(self, rendszam):
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam:
                berles.auto.berelve = False
                self.berlesek.remove(berles)
                print(f"✔️Bérlés lemondva: {rendszam}✔️")
                return
        print(f"❌Nincs ilyen bérlés: {rendszam}❌")
