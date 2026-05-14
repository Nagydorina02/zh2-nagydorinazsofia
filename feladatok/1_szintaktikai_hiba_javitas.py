"""
1. feladat - Szintaktikai hibas kod javitasa (5 pont)
TODO:
- Javitsd ki az 5 szintaktikai hibat ugy, hogy a program hiba nelkul fusson.
- A program celja:
  1. kiszamolni az osszes termek keszletetertekat (darab * egysegar),
  2. visszaadni azoknak a termekeknek a nevet, amelyek keszleten vannak,
  3. megtalalni a legdragabb termek nevet.
- A program logikajat ne valtoztasd meg, csak a szintaktikai hibakat javitsd.
- Minden javitas 1 pont.
Elvart kimenet a javitas utan:
- Keszlet osszertek: 1109800
- Elerheto termekek: ['Billentyuzet', 'Monitor', 'Fejhallgato']
- Legdragabb termek: Monitor
"""
termekek = [
    {"nev": "Billentyuzet", "darab": 12, "egysegar": 7500},
    {"nev": "Eger", "darab": 0, "egysegar": 4200},
    {"nev": "Monitor", "darab": 4, "egysegar": 68500},
    {"nev": "Fejhallgato", "darab": 9, "egysegar": 15900},
]
def keszlet_ertek_osszesen(adatok):
    osszeg = 0
    for termek in adatok:
        osszeg += termek["darab"] * termek["egysegar"]
    return osszeg
def elerheto_termekek(adatok):
    return [termek["nev"] for termek in adatok if termek["darab"] > 0]
def legdragabb_termek(adatok):
    legjobb = adatok[0]
    for termek in adatok[1:]:
        if termek["egysegar"] > legjobb["egysegar"]:
            legjobb = termek
            return legjobb["nev"]

if __name__ == "__main__":
    print("Keszlet osszertek:", keszlet_ertek_osszesen(termekek))
    print("Elerheto termekek:", elerheto_termekek(termekek))
    print("Legdragabb termek:", legdragabb_termek(termekek))
