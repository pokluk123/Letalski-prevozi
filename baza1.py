import csv

def pobrisi_tabele(conn):
    """
    Pobriše tabele iz baze.
    """
    conn.execute("DROP TABLE IF EXISTS karta;")
    conn.execute("DROP TABLE IF EXISTS let;")
    conn.execute("DROP TABLE IF EXISTS letalisce;")
    conn.execute("DROP TABLE IF EXISTS letalo;")
    conn.execute("DROP TABLE IF EXISTS linije;")
    conn.execute("DROP TABLE IF EXISTS model;")
    conn.execute("DROP TABLE IF EXISTS prevoznik;")


def ustvari_tabele(conn):
    """
    Ustvari tabele v bazi.
    """
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
        CREATE TABLE let (
            id            INTEGER  PRIMARY KEY AUTOINCREMENT,
            odhod         DATETIME,
            prihod        DATETIME,
            stevilka_leta          REFERENCES linije (koda) 
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
            odhod_ura        TIME,
            odhod_dan        TEXT,
            cas_letanje      TIME,
            odhod_letalisce  TEXT REFERENCES letalisce (koda_letalisca),
            prihod_letalisce TEXT REFERENCES letalisce (koda_letalisca),
            CHECK(odhod_letalisce <> prihod_letalisce)
);

    """)
    conn.execute("""
        CREATE TABLE model (
            stevilka_modela INTEGER PRIMARY KEY,
            stevilo_sedezev INTEGER
);
    """)
    conn.execute("""
        CREATE TABLE prevoznik (
            koda TEXT PRIMARY KEY,
            ime  TEX
);
    """)
    conn.execute("""
        CREATE TABLE letalo (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            serijska_številka     INTEGER,
            model     TEXT    REFERENCES model (id) 
                            NOT NULL
            );
    """)

def uvozi_karta(conn):
    """
    Uvozi podatke o igralcih.
    """
    conn.execute("DELETE FROM let;")
    conn.execute("DELETE FROM karta;")
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
    conn.execute("DELETE FROM karta;")
    conn.execute("DELETE FROM letalo;")
    conn.execute("DELETE FROM linije;")
    conn.execute("DELETE FROM let;")
    with open('podatki/LET_podatki.csv') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO let VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)

def uvozi_letalisce (conn):
    """
    Uvozi podatke o žanrih.
    """
    conn.execute("DELETE FROM linija;")
    conn.execute("DELETE FROM letalisce;")
    with open('podatki/letalisca.csv') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO tekme VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)

def uvozi_letalo(conn):
    """
    Uvozi podatke o vlogah.
    """
    conn.execute("DELETE FROM let;")
    conn.execute("DELETE FROM model;")
    conn.execute("DELETE FROM letalo;")
    with open('podatki/statistika.csv') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO letalo VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)

def uvozi_linje(conn):
    """
    Uvozi podatke o vlogah.
    """
    conn.execute("DELETE FROM let;")
    conn.execute("DELETE FROM model;")
    conn.execute("DELETE FROM letaalisce;")
    conn.execute("DELETE FROM prevoznik;")
    conn.execute("DELETE FROM linije;")
    with open('podatki/LINIJE_podatki.csv') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO linije VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)

def uvozi_model(conn):
    """
    Uvozi podatke o vlogah.
    """
    conn.execute("DELETE FROM linije;")
    conn.execute("DELETE FROM model;")
    conn.execute("DELETE FROM letalo;")
    with open('podatki/MODEL_podatki.csv') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO model VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)
def uvozi_prevoznik(conn):
    """
    Uvozi podatke o vlogah.
    """
    conn.execute("DELETE FROM linije;")
    conn.execute("DELETE FROM prevoznik;")
    
    with open('podatki/Prevoznik_podatki.csv') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO model VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)













def ustvari_bazo(conn):
    """
    Opravi celoten postopek postavitve baze.
    """
    pobrisi_tabele(conn)
    ustvari_tabele(conn)
    uvozi_karta(conn)
    """
    uvozi_let(conn)
    uvozi_letalo(conn)
    uvozi_linje(conn)
    uvozi_prevoznik(conn)
    uvozi_letalisce(conn)
    uvozi_model(conn) """

def ustvari_bazo_ce_ne_obstaja(conn):
    """
    Ustvari bazo, če ta še ne obstaja.
    """
    with conn:
        #conn = conn.execute("SELECT COUNT(*) FROM sqlite_master")
        #if conn.fetchone() == (0, ):
        ustvari_bazo(conn)