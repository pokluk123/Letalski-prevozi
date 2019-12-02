import baza1 as baza
import sqlite3

conn = sqlite3.connect('letalski_prevozi.db')
baza.ustvari_bazo_ce_ne_obstaja(conn)
conn.execute('PRAGMA foreign_keys = ON')