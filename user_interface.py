from Szemelyauto import Szemelyauto
from Teherauto import Teherauto

def user_interface(kolcsonzo):
    while True:
        print("\nAutókölcsönző Rendszer")
        print("1. Autók listázása")
        print("2. Autó bérlése")
        print("3. Bérlés lemondása")
        print("4. Bérlések listázása")
        print("5. Kilépés")

        valasztas = input("Válassz egy lehetőséget (1-5): ")

        if valasztas == "1":
            print('')
            print(40*'-')
            kolcsonzo.autok_listazasa()
            print(40*'-')
        elif valasztas == "2":
            tipus_valasztas = input("Milyen típusú autót szeretnél bérelni? (1: Személyautó, 2: Teherautó): ")
            if tipus_valasztas == "1":
                auto_tipus = Szemelyauto
            elif tipus_valasztas == "2":
                auto_tipus = Teherauto
            else:
                print("❌Érvénytelen választás.❌")
                continue
            rendszam = input("Add meg az autó rendszámát: ")
            berles_datum = input("Add meg a bérlés dátumát (YYYY-MM-DD): ")
            kolcsonzo.berles(rendszam, berles_datum, auto_tipus)
        elif valasztas == "3":
            rendszam = input("Add meg a rendszámot a bérlés lemondásához: ")
            kolcsonzo.berles_lemondasa(rendszam)
        elif valasztas == "4":
            print('')
            print(40*'-')
            kolcsonzo.berlesek_listazasa()
            print(40*'-')
        elif valasztas == "5":
            print("Köszönjük, hogy minket választott...")
            break
        else:
            print(40*'-')
            print("❌ÉRVÉNYTELEN VÁLASZTÁS, PRÓBÁLD ÚJRA!❌")
            print(40*'-')
