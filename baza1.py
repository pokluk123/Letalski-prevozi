import csv

def pobrisi_tabele(conn):
    """
    Pobriše tabele iz baze.
    """
    conn.execute("DROP TABLE IF EXISTS karta;")
    conn.execute("DROP TABLE IF EXISTS let;")
    conn.execute("DROP TABLE IF EXISTS letalisce;")
    conn.execute("DROP TABLE IF EXISTS linije;")
    conn.execute("DROP TABLE IF EXISTS prevoznik;")


def ustvari_tabele(conn):
    """
    Ustvari tabele v bazi.
    """

    conn.execute("""
        CREATE TABLE let (
            id            INTEGER  PRIMARY KEY AUTOINCREMENT,
            odhod         DATETIME,
            prihod        DATETIME,
            stevilka_leta          REFERENCES linije (koda) 
                                NOT NULL
);
    """)
    conn.execute("""
        CREATE TABLE karta (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            ime     TEXT,
            priimek TEXT,
            cena    INTEGER,
            let     TEXT    REFERENCES let (id) 
                            NOT NULL
            );
    """)
    conn.execute("""
        CREATE TABLE letalisce (
            koda_letalisce TEXT PRIMARY KEY,
            ime            TEXT
);
    """)
    conn.execute("""
        CREATE TABLE linije (
            koda             TEXT PRIMARY KEY,
            odhod_dan        TEXT,
            cas_letenja      TIME,
            odhod_letalisce  TEXT REFERENCES letalisce (koda_letalisca),
            prihod_letalisce TEXT REFERENCES letalisce (koda_letalisca),
            CHECK(odhod_letalisce <> prihod_letalisce)
);

    """)

    conn.execute("""
        CREATE TABLE prevoznik (
            koda TEXT PRIMARY KEY,
            ime  TEX
);
    """)

def uvozi_karta(conn):
    """
    Uvozi podatke o igralcih.
    """
    with open('podatki/KARTA_podatki.csv') as datoteka: #spremen
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO karta VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)

def uvozi_let(conn):
    """
    Uvozi podatke o ekipah.
    """
    i = 0
    with open('podatki/LET_podatki.csv') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO let VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            i += 1
            vrstica[0] = i
            conn.execute(poizvedba, vrstica)

def uvozi_letalisce (conn):
    """
    Uvozi podatke o žanrih.
    """
    with open('podatki/letalisca.csv') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO tekme VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)


def uvozi_linje(conn):
    """
    Uvozi podatke o vlogah.
    """
    with open('podatki/LINIJE_podatki.csv') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO linije VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)


def uvozi_prevoznik(conn):
    """
    Uvozi podatke o vlogah.
    """    
    with open('podatki/Prevoznik_podatki.csv') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO prevoznik VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)













def ustvari_bazo(conn):
    """
    Opravi celoten postopek postavitve baze.
    """
    pobrisi_tabele(conn)
    ustvari_tabele(conn)
    uvozi_let(conn)
    uvozi_karta(conn)
    uvozi_linje(conn)
    uvozi_prevoznik(conn)
    uvozi_letalisce(conn)

def ustvari_bazo_ce_ne_obstaja(conn):
    """
    Ustvari bazo, če ta še ne obstaja.
    """
    with conn:
        #conn = conn.execute("SELECT COUNT(*) FROM sqlite_master")
        #if conn.fetchone() == (0, ):
        ustvari_bazo(conn)