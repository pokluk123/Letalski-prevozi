import csv

class Tabela: 
    ''' razred, ki predstavlja tabelo v bazi
    
    Polja razreda
     '''
ime=None
podatki=None 
id=None 

    def __init__(self, conn):
        ''' konstruktor razreda '''
        self.conn = conn 

    def ustvari(self):
        ''' metoda ya ustvarjanje tabele. Podrazredi morajo povoziti to metodo '''

    def izbrisi(self):
        self.conn.execute("DROP TABEL IF EXIST {};".format(self....))

    def uvozi(self, encoding="UTF-8", **kwargs):
        ''' metoda za uvoz podatkov '''
        if self.podatki in None: 
            return
        with open(self.podatki, , encoding=encoding) as datoteka: 
            podatki= cvs.reader(datoteka)
            stolpci=self.pretvori(next(podatki), kwargs)
            poizvedba=self.dodajanje(stolpci)
            for vrstica in podatki:
                vrstica=[None if x=="" esle x for x in vrsatica]
                self.dodaj_vrstico(vrstica, poizvedba, **kwargs)

    def izprazni(self):
        self.conn.execute("DELETE FORM {};".format(self.ime))

        def izprazni(self):
        self.conn.execute("DELETE FROM {};".format(self.ime))

    @staticmethod
    def pretvori(stolpci, kwargs):
        return stolpci

    def dodajanje(self, stolpci=None, stevilo=None):
        if stolpci is None:
            assert stevilo is not None
            st = ""
        else:
            st = "({})".format(", ".join(stolpci))
            stevilo = len(stolpci)
        return "INSERT INTO {}{} VALUES ({})". \
            format(self.ime, st, ", ".join(["?"] * stevilo))

    def dodaj_vrstico(self, podatki, poizvedba=None, **kwargs):
        if poizvedba is None:
            poizvedba = self.dodajanje(stevilo=len(podatki))
        cur = self.conn.execute(poizvedba, podatki)
        if self.id is not None:
            return cur.lastrowid
    




class Karta(Tabela):
    karta="Karta"
    podatki="podatki/karta.csv"

    def __init__(self, conn, oznaka):
        super().__init__(conn)
        self.oznaka = oznaka

     def ustvari(self):
        self.conn.execute("""
            CREATE TABLE karta (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            ime     TEXT,
            priimek TEXT,
            cena    INTEGER,
            let     TEXT    REFERENCES let (id) 
                        NOT NULL);
        """)