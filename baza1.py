import csv

def pobrisi_tabele(conn):
    """
    Pobriše tabele iz baze.
    """
    conn.execute("DROP TABLE IF EXISTS statistika;")
    conn.execute("DROP TABLE IF EXISTS tekme;")
    conn.execute("DROP TABLE IF EXISTS ekipe;")
    conn.execute("DROP TABLE IF EXISTS igralci;")

def ustvari_tabele(conn):
    """
    Ustvari tabele v bazi.
    """
    conn.execute("""
        CREATE TABLE igralci (
            number          INTEGER PRIMARY KEY,
            name            TEXT,
            position        TEXT,
            height          STRING,
            weight          INTEGER,
            year_of_birth   INTEGER
        );
    """)
    conn.execute("""
        CREATE TABLE ekipe (
            tag        STRING PRIMARY KEY,
            trainer    TEXT,
            franchise  TEXT
        );
    """)
    conn.execute("""
        CREATE TABLE tekme (
            date            DATE PRIMARY KEY,
            opponent        STRING REFERENCES ekipe(franchise),
            outcome         STRING,
            pointsteam      INTEGER,
            pointsopponent  INTEGER
        );
    """)
    conn.execute("""
        CREATE TABLE statistika (
            playerREF    INTEGER REFERENCES igralci(number),
            dateREF      DATE REFERENCES tekme(date),
            rebounds     INTEGER,
            assists      INTEGER,
            steals       INTEGER,
            points       INTEGER
        );
    """)

def uvozi_igralci(conn):
    """
    Uvozi podatke o igralcih.
    """
    conn.execute("DELETE FROM statistika;")
    conn.execute("DELETE FROM igralci;")
    with open('Podatki/igralci.csv') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO igralci VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)

def uvozi_ekipe(conn):
    """
    Uvozi podatke o ekipah.
    """
    conn.execute("DELETE FROM tekme;")
    conn.execute("DELETE FROM ekipe;")
    with open('podatki/ekipe.csv') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO ekipe VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)

def uvozi_tekme (conn):
    """
    Uvozi podatke o žanrih.
    """
    conn.execute("DELETE FROM statistika;")
    conn.execute("DELETE FROM tekme;")
    with open('podatki/tekme.csv') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO tekme VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)

def uvozi_statistika(conn):
    """
    Uvozi podatke o vlogah.
    """
    conn.execute("DELETE FROM statistika;")
    with open('podatki/statistika.csv') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO statistika VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)

def ustvari_bazo(conn):
    """
    Opravi celoten postopek postavitve baze.
    """
    pobrisi_tabele(conn)
    ustvari_tabele(conn)
    uvozi_igralci(conn)
    uvozi_ekipe(conn)
    uvozi_tekme(conn)
    uvozi_statistika(conn)

def ustvari_bazo_ce_ne_obstaja(conn):
    """
    Ustvari bazo, če ta še ne obstaja.
    """
    with conn:
        conn = conn.execute("SELECT COUNT(*) FROM sqlite_master")
        if conn.fetchone() == (0, ):
            ustvari_bazo(conn)