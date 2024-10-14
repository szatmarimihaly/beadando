from Autokolcsonzo import Autokolcsonzo
from Szemelyauto import Szemelyauto
from Teherauto import Teherauto
from user_interface import user_interface

if __name__ == "__main__":
    kolcsonzo = Autokolcsonzo("JóAutó Autókölcsönző")

    kolcsonzo.hozzaad_auto(Szemelyauto("AAAA-000", "Toyota Corolla", 10000, 5))
    kolcsonzo.hozzaad_auto(Szemelyauto("FORD-001", "Ford Fiesta", 8000, 3))
    kolcsonzo.hozzaad_auto(Szemelyauto("MERC-450", "Mercedes E450", 8000, 3))
    kolcsonzo.hozzaad_auto(Szemelyauto("MERC-063", "Mercedes G63", 80000, 5))

    kolcsonzo.hozzaad_auto(Teherauto("BBBB-000", "Iveco Daily", 15000, 3000))
    kolcsonzo.hozzaad_auto(Teherauto("MERC-100", "Mercdes Sprinter", 20000, 3500))
    kolcsonzo.hozzaad_auto(Teherauto("BBBB-002", "Iveco Daily", 18000, 3200))

    kolcsonzo.berles('AAAA-000', '2024-10-14', Szemelyauto)
    kolcsonzo.berles('BBBB-000', '2024-10-16', Teherauto)

    user_interface(kolcsonzo)
