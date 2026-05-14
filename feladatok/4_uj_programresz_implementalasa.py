"""
4. feladat - Uj programresz implementalasa (5 pont)
TODO:
Keszits egy termekertekeles-feldolgozo programot JSON bemenettel.
Minden implementalt fuggveny 1 pont.
Feladat:
- Egy JSON fajlbol termekertekeleseket kell beolvasni.
- Minden rekord tartalmazza:
  - termek (str)
  - kategoria (str)
  - ertekelesek (lista, 1-5 kozotti egesz szamok)
Implementaland fuggvenyek:
1. beolvas_ertekelesek(fajlnev)
   - Olvassa be a JSON fajlt, terjen vissza rekordok listajaval.
2. validalt_ertekeles(ertek)
   - Ellenorizze, hogy az ertek 1 es 5 kozotti egesz szam-e.
   - Hibas ertek eseten dobjon ValueError kivetelt.
3. termek_atlag(rekord)
   - Szamolja ki egy rekord ertekeleseinek atlagat.
   - Minden egyes ertekest validaljon a validalt_ertekeles() segitsegevel.
4. kategoriak_atlagai(rekordok)
   - Adja vissza dict-kent, hogy kategorianként mi az atlagok atlaga.
   - Pelda: {"elektronika": 4.17, "konyv": 4.67}
5. mentes_osszefoglalo_json(rekordok, fajlnev)
   - Mentse el JSON-be az osszes rekordhoz:
     - termekek_szama
     - termek_atlagok  (dict: termek neve -> atlaga)
     - kategoriak_atlagai
     - legjobb_termek  (a legnagyobb atlagu termek neve)
"""
import json
def beolvas_ertekelesek(fajlnev):
    # TODO: valositsd meg
    with open(fajlnev, "r", encoding="utf-8") as fajl:
        return json.load(fajl)
    raise NotImplementedError("A fuggveny meg nincs implementalva.")

def validalt_ertekeles(ertek):
    # TODO: valositsd meg (dobjon ValueError-t ha nem 1-5 kozotti egesz szam az ertek)
    if not isinstance(ertek, int):
        raise ValueError("Az ertekelesnek egesz szamnak kell lennie.")

    if ertek < 1 or ertek > 5:
        raise ValueError("Az ertekelesnek 1 es 5 kozott kell lennie.")

    return True
    raise NotImplementedError("A fuggveny meg nincs implementalva.")

def termek_atlag(rekord):
    # TODO: valositsd meg, hasznald a validalt_ertekeles()-t
    ertekelesek = rekord["ertekelesek"]

    if not ertekelesek:
        return 0

    osszeg = 0

    for ertek in ertekelesek:
        validalt_ertekeles(ertek)
        osszeg += ertek

    return osszeg / len(ertekelesek)
    raise NotImplementedError("A fuggveny meg nincs implementalva.")

def kategoriak_atlagai(rekordok):
    # TODO: valositsd meg
    kategoriak = {}

    for rekord in rekordok:
        kategoria = rekord["kategoria"]
        atlag = termek_atlag(rekord)

        if kategoria not in kategoriak:
            kategoriak[kategoria] = []

        kategoriak[kategoria].append(atlag)

    eredmeny = {}

    for kategoria, atlagok in kategoriak.items():
        eredmeny[kategoria] = round(sum(atlagok) / len(atlagok), 2)

    return eredmeny
    raise NotImplementedError("A fuggveny meg nincs implementalva.")

def mentes_osszefoglalo_json(rekordok, fajlnev):
    # TODO: valositsd meg
    termek_atlagok = {}

    legjobb_termek = None
    legjobb_atlag = -1

    for rekord in rekordok:
        nev = rekord["termek"]
        atlag = termek_atlag(rekord)

        termek_atlagok[nev] = round(atlag, 2)

        if atlag > legjobb_atlag:
            legjobb_atlag = atlag
            legjobb_termek = nev

    osszefoglalo = {
        "termekek_szama": len(rekordok),
        "termek_atlagok": termek_atlagok,
        "kategoriak_atlagai": kategoriak_atlagai(rekordok),
        "legjobb_termek": legjobb_termek
    }

    with open(fajlnev, "w", encoding="utf-8") as fajl:
        json.dump(osszefoglalo, fajl, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    minta_rekordok = [
        {"termek": "Laptop A", "kategoria": "elektronika", "ertekelesek": [5, 4, 5]},
        {"termek": "Eger X",   "kategoria": "elektronika", "ertekelesek": [4, 4, 3]},
        {"termek": "Konyv Z",  "kategoria": "konyv",       "ertekelesek": [5, 5, 4]},
        {"termek": "Tablet B", "kategoria": "elektronika", "ertekelesek": [3, 4, 4]},
    ]
    print("Laptop A atlaga:", termek_atlag(minta_rekordok[0]))

    print("Kategoriak atlagai:",
          kategoriak_atlagai(minta_rekordok))

    mentes_osszefoglalo_json(
        minta_rekordok,
        "termek_osszefoglalo.json"
    )
    # A TODO-k megoldasa utan ezek hasznalhatok tesztelesre:
    # print("Laptop A atlaga:", termek_atlag(minta_rekordok[0]))
    # print("Kategoriak atlagai:", kategoriak_atlagai(minta_rekordok))
    # mentes_osszefoglalo_json(minta_rekordok, "termek_osszefoglalo.json")
