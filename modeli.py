import baza1 as baza
import sqlite3

conn = sqlite3.connect('letalski_prevozi.db')
baza.ustvari_bazo_ce_ne_obstaja(conn)
conn.execute('PRAGMA foreign_keys = ON')

def commit(fun):
    """
    Dekorator, ki ustvari kurzor, ga poda dekorirani funkciji,
    in nato zapiše spremembe v bazo.
    Originalna funkcija je na voljo pod atributom nocommit.
    """
    def funkcija(*largs, **kwargs):
        ret = fun(conn.cursor(), *largs, **kwargs)
        conn.commit()
        return ret
    funkcija.__doc__ = fun.__doc__
    funkcija.__name__ = fun.__name__
    funkcija.__qualname__ = fun.__qualname__
    fun.__qualname__ += '.nocommit'
    funkcija.nocommit = fun
    return funkcija
  
def id_karte(ime):
    """
    Vrne ID karte, če je karta s tem imenom obstaja
    Če karte ni, vrne False.
    """
    vrstica = conn.execute("SELECT number FROM karta WHERE karta.ime = ?",[ime]).fetchone()
    if vrstica is not None:
        return vrstica
    return False


def ime_potnika(let):
    """
    Vrne ime igralca na podlagi leta na karti
    """
    return  ''.join(conn.execute("SELECT ime FROM karta WHERE let = ?",[let]).fetchone())

def vsi_prevozi():
    """
    Vrne orvih 10 linij
    """
    return conn.execute("""SELECT * FROM linije """).fetchone()

def prvih_deset():
    """
    Vrne prvih 10 letov
    """
    return conn.execute("""SELECT id, odhod, prihod, odhod_dan, cas_letenja, odhod_letalisce, prihod_letalisce
                            FROM let JOIN  linije ON let.stevilka_leta = linije.koda
                            WHERE odhod > date('now') 
                            ORDER BY odhod
                            LIMIT 50;

                             """).fetchall()

def poisci(id):
    """
    Vrne vse podatke o letu glede na njegov ID.
    """
    sql ="""SELECT id, odhod, prihod, odhod_dan, cas_letenja, odhod_letalisce, prihod_letalisce FROM let JOIN  linije ON let.stevilka_leta = linije.koda WHERE id = ?"""
    return conn.execute(sql, [id]).fetchone()


def ime_letalisca(niz):
    """
    Vrne ime letalisca glede na njegovo kodo
    """
    sql ="""SELECT koda_letalisce FROM letalisca WHERE koda_letalisce LIKE ?"""
    return conn.execute(sql, [niz]).fetchone()

