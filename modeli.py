import baza
import sqlite3

conn = sqlite3.connect('letalski:prevoyi.db')
baza.ustvari_bazo_ce_ne_obstaja(conn)
conn.execute('PRAGMA foreign_keys = ON')