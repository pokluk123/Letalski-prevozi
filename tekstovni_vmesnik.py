import modeli
import datetime

def izberi_moznost(moznosti):
    """
    Funkcija, ki izpiše seznam možnosti in vrne indeks izbrane možnosti

    Če ne voljo ni nobene možnosti, izpiše opozorilo in vrne None
    Če je na voljo samo ena možnost, vrne 0
    >>> izberi_moznost(['dimitar','blaz'])
    1)dimitar
    2)blaz
    Vnesite izbiro: 1
    0
    >>> izberi_moznost([])
    >>> izberi_moznost(['blaz'])
    0
    """

    if len(moznosti) == 0:
        return
    elif len(moznosti) == 1:
        return 0
    else:
        for i, moznost in enumerate(moznosti, 1):
            print('{}){}'.format(i,moznost))
        st_moznosti = len(moznosti)
        while True:
            izbira = input("Vnesite izbiro: ")
            if not izbira.isdigit():
                print("NAPAKA: vnesti morate število")
            else:
                n = int(izbira)
                if 1 <= n <= st_moznosti:
                    return n-1
                else:
                    print("NAPAKA: vnesti morate število med 1 in {}!".format(
                        st_moznosti))

def prikazi_podatke_o_igralcu():
    """
    Prikaže podatke o določenem igralcu. Če podatka ni v bazi, izpiše napako.
    """
    ime = input("Vnesi ime igralca: ")
    while not modeli.id_igralca(ime):
        ime = input("Igralec s tem imenom ne obstaja. Vnesi pravo ime:")
    else:
        podatki = list(modeli.pridobi_podatke(ime))
        print("\nŠt dresa: {0}, polno ime: {1}, pozicija: {2}, visina: {3}, teza: {4}, letnica rojstva: {5}\n".format(*podatki))

def prikazi_podatke_najboljsi():
    """
    Prikaže najboljše igralce v posamezni kategoriji proti določeni ekipi.
    Glede na to, da proti eni ekipi se igra več kot 2x, uporabnika vprašamo 
    naj izbere datum za katerega želi videti statistiko.
    """
    imeEkipe = input("Vnesi ime željene ekipe: ")
    while modeli.ali_ekipa_obstaja(imeEkipe):
        imeEkipe = input("Ime ekipe je napačno! Vnesi pravilnega:")
    else:
        print("Proti ekipi {} je naša ekipa igrala na naslednjih datumih: ".format(imeEkipe))
        seznamDatumov = modeli.poisci_datume(imeEkipe)
        for i in range(len(seznamDatumov)):
            print("{}) {}".format(i+1, seznamDatumov[i]))
        st = int(input("Izberi datum, tako da izbereš število od 1 do {}: ".format(len(seznamDatumov))))
        datum = seznamDatumov[st-1]
        print("\nNa tekmi,ki je bila odigrana {} je statistika bila sledeča: ".format(datum))
        najvec_tock = list(modeli.najvec_tock(datum))
        najvec_podaj = list(modeli.najvec_podaj(datum))
        najvec_skoki = list(modeli.najvec_skoki(datum))
        najvec_ukradenih = list(modeli.najvec_ukradene(datum))
        print("Največ točk je imel {}: {}".format(modeli.ime_igralca(najvec_tock[0]),najvec_tock[1]))
        print("Največ skokov je imel {}: {}".format(modeli.ime_igralca(najvec_skoki[0]),najvec_skoki[1]))
        print("Največ podaj je imel {}: {}".format(modeli.ime_igralca(najvec_podaj[0]),najvec_podaj[1]))
        print("Največ ukradenih žog je imel {}: {}\n".format(modeli.ime_igralca(najvec_ukradenih[0]),najvec_ukradenih[1]))

def tekme_med_datumi():
    """
    Prikaže tekme, ki jih je ekipa odigrala v določenem času.
    """
    print("NBA sezona traja od 2017-10-18 do 2018-04-11!\n")
    zacetniDatum = input("Vnesi začetni datum v obliki YYYY-MM-DD: ")
    koncniDatum = input("Vnesi končni datum v obliki YYYY-MM-DD: ")

    if preveri(zacetniDatum, koncniDatum):
        podatki = modeli.tekme_v_obdobju(zacetniDatum, koncniDatum)    
        for podatek in podatki:
            print("Proti ekipi {} je naša ekipa igrala {} krat.".format(list(podatek)[0],list(podatek)[1]))
        stZmag = list(modeli.stevilo_zmag(zacetniDatum, koncniDatum))[0]
        stPorazov = list(modeli.stevilo_porazov(zacetniDatum, koncniDatum))[0]
        print("\nV tem času je dosegla {} zmag in {} porazov.\n".format(stZmag, stPorazov))
    else:
        print("\nNapisal si napačen datum!\n")
        tekme_med_datumi()


def preveri(zacDat, koncDat):
    """
    Preveri ali sta dana datuma pravilna.
    """
    try:
        l1, m1, d1 = zacDat.split("-")
        l2, m2, d2 = koncDat.split("-")
        datum1 = datetime.datetime(int(l1),int(m1),int(d1))
        datum2 = datetime.datetime(int(l2),int(m2),int(d2))
        if datum2 < datum1:
            return False
    except:
        return False
    return True






def pokazi_moznosti():
    print(50 * '-')
    izbira = izberi_moznost([
        'prikaži podatke o določenem igralcu',
        'prikaži najboljšega igralca na posamezni tekmi',
        'izpiše tekme med dvema datumoma',
        'izhod',
    ])
    if izbira == 0:
        prikazi_podatke_o_igralcu()
        nazaj()
    elif izbira == 1:
        prikazi_podatke_najboljsi()
        nazaj()
    elif izbira == 2:
        tekme_med_datumi()
        nazaj()
    else:
        print('Nasvidenje!')
        exit()

def main():
    print('Pozdravljeni v bazi košarkarske ekipe!')
    while True:
        pokazi_moznosti()

def nazaj():
    """
    Funkcija naredi, da se po uporabnikovi uspešni poizvedbi ne vrnemo takoj na poizvedovanje
    """
    input("Pritisni Enter za nadaljevanje!")
        
main()
