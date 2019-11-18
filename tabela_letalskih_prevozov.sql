--
-- File generated with SQLiteStudio v3.2.1 on pon. nov. 18 11:44:18 2019
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: karta
CREATE TABLE karta (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    ime     TEXT,
    priimek TEXT,
    cena    INTEGER,
    let     TEXT    REFERENCES let (id) 
                    NOT NULL
);

-- Table: let
CREATE TABLE let (
    id            INTEGER  PRIMARY KEY AUTOINCREMENT,
    odhod         DATETIME,
    prihod        DATETIME,
    stevilka_leta          REFERENCES linije (koda) 
                           NOT NULL
);

-- Table: letalisce
CREATE TABLE letalisce (
    koda_letalisce TEXT PRIMARY KEY,
    ime            TEXT
);

-- Table: letalo
CREATE TABLE letalo (
    id                INTEGER PRIMARY KEY AUTOINCREMENT,
    serijska_stevilka INTEGER,
    vrsta             TEXT    REFERENCES model (stevlika_modela) NOT NULL
);

-- Table: linije
CREATE TABLE linije (
    koda             TEXT PRIMARY KEY,
    odhod_ura        TIME,
    odhod_dan        TEXT,
    cas_letanje      TIME,
    odhod_letalisce  TEXT REFERENCES letalisce (koda_letalisca),
    prihod_letalisce TEXT REFERENCES letalisce (koda_letalisca),
    CHECK(odhod_letalisce <> prihod_letalisce)
);

-- Table: model
CREATE TABLE model (
    stevilka_modela INTEGER PRIMARY KEY,
    stevilo_sedezev INTEGER
);

-- Table: prevoznik
CREATE TABLE prevoznik (
    koda TEXT PRIMARY KEY,
    ime  TEX
);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
