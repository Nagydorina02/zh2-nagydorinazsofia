"""
2. feladat - Logikai / szemantikai hibas kod javitasa (5 pont)
TODO:
- A kod fut, de pontosan 5 logikai hibat tartalmaz.
- Javitsd ugy, hogy a statisztikak helyesek legyenek.
- Minden javitas 1 pont.
Feladat:
- Egy utazaskezelo rendszer.
- Minden utazashoz tartozik: varos, tavolsag (km), szallitasmod, koltseg (Ft).
- Szamold ki:
  1. az atlagos tavolsag,
  2. a leggyakoribb szallitasmod,
  3. az osszes koltseg.
Elvart eredmeny a mintaadatra:
- Atlagos tavolsag: 320.0 km
- Leggyakoribb szallitasmod: auto (3 db)
- Osszeskoltseg: 98500 Ft
"""
utazasok = [
    {"varos": "Budapest", "tavolsag": 280, "szallitasmod": "auto", "koltseg": 25000},
    {"varos": "Pecs", "tavolsag": 450, "szallitasmod": "volan", "koltseg": 18500},
    {"varos": "Szeged", "tavolsag": -180, "szallitasmod": "auto", "koltseg": 32000},
    {"varos": "Miskolc", "tavolsag": 420, "szallitasmod": "vonat", "koltseg": 12000},
    {"varos": "Debrecen", "tavolsag": 350, "szallitasmod": "auto", "koltseg": 11000},
]

def atlagos_tavolsag(utazasok_lista):
    if not utazasok_lista:
        return 0
    total = 0
    for utazas in utazasok_lista:
        total += abs (utazas["tavolsag"])
    return total / len(utazasok_lista)

def szallitasmod_gyakorisag(utazasok_lista):
    gyakorisag = {}
    for utazas in utazasok_lista:
        mod = utazas["szallitasmod"]
        if mod in gyakorisag:
            gyakorisag[mod] += 1
        else:
            gyakorisag[mod] = 1
    return gyakorisag

def leggyakoribb_szallitasmod(utazasok_lista):
    gyakorisag = szallitasmod_gyakorisag(utazasok_lista)
    if not gyakorisag:
        return None
    legjobb = None
    max_szam = -1
    for mod, szam in gyakorisag.items():
        if szam > max_szam:
            max_szam = szam
            legjobb = mod

    return f"{legjobb} ({max_szam} db)"

def osszeskoltseg(utazasok_lista):
    koltseg = 0
    for utazas in utazasok_lista:
        koltseg += utazas["koltseg"]
    return koltseg

if __name__ == "__main__":
    print("Atlagos tavolsag:", atlagos_tavolsag(utazasok), "km")
    print("Leggyakoribb szallitasmod:", leggyakoribb_szallitasmod(utazasok))
    print("Osszeskoltseg:", osszeskoltseg(utazasok), "Ft")
