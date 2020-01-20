from bottle import route, run, template, get, static_file, post, request, redirect
import os.path
import modeli


@get('/')
def glavna_stran():
    return template('glavna_stran',
                    leti = modeli.prvih_deset()
                    )


@get('/isci/')
def isci():
    iskalni_niz = request.query.getunicode('iskalni_niz')
    let=modeli.poisci(iskalni_niz)
    #osebe = Oseba.poisci(iskalni_niz)
    return template(
        'rezultati_iskanja.html',
        iskalni_niz=iskalni_niz,
        let=let
    )




























# @get('/igralci/')
# def igralci():
#     vsi = modeli.igralci_vsi()
#     return template('igralci',
#                      igralci = vsi
#                      )

# @get('/igralci/<id:int>/')
# def igralec(id):
#     podatki_o_igralcu = modeli.pridobi_podatke(id)
#     seznam_tekem = modeli.statistika_igralca_s_tekem(id)
#     obstaja = ali_slika_obstaja(id)
#     return template('igralec',
#                      podatki_o_igralcu = podatki_o_igralcu,
#                      seznam_tekem = seznam_tekem,
#                      id = id,
#                      slika_obstaja = obstaja
#                      )

# @post('/igralci/<id:int>/')
# def odstrani_igralca(id):
#     neki = modeli.pobrisi_igralca(id)
#     vsi = modeli.igralci_vsi()
#     return template('igralci',
#                      igralci = vsi
#                      )

# @get('/ekipa/')
# def ekipa():
#     podatki = modeli.podatki_o_ekipi()
#     seznam_igralcev = modeli.igralci_vsi()
#     return template('ekipa',
#                     podatki_o_ekipi = podatki,
#                     seznam_igralcev = seznam_igralcev)

# @get('/ekipa/tekme/')
# def tekme():
#     zacDatum = request.query.zacetek
#     konDatum = request.query.konec
#     tekme = modeli.tekme_v_obdobju_vse(zacDatum, konDatum)
#     return template('tekme',
#                     zac_datum = zacDatum,
#                     kon_datum = konDatum,
#                     tekme = tekme)


# @get("/static/<filepath>")
# def js(filepath):
#     return static_file(filepath, root="static")

# @get('/povprecja/')
# def povprecja():
#     igralci = modeli.igralci_vsi()
#     return template('povprecja',
#                     vse_osebe = igralci)

# @get('/povprecja/povpigralec/')
# def povpigralec():
#     ime = request.query.igralci
#     id = modeli.id_igralca(ime)[0]
#     maximum = modeli.max_stevilo_tock(id)[0]
#     average = modeli.avg_stevilo_tock(id)[0]
#     obstaja = ali_slika_obstaja(id)
#     return template('povpigralec',
#                     ime = ime,
#                     id = id,
#                     slika_obstaja = obstaja,
#                     max = maximum,
#                     avg = average)

# @get('/dodaj_igralca/')
# def dodaj_igralca():
#     return template('dodaj_igralca', napaka =False)

# @post('/dodaj_igralca/')
# def dodajanje_igralca():
#     try:
#         if (int(request.forms.stDresa) >= 0) and (int(request.forms.teza) > 0):
#             id = modeli.dodaj_igralca(
#                 stDresa = request.forms.stDresa,
#                 imeIgralca = request.forms.imeIgralca,
#                 pozicija = request.forms.pozicija,
#                 visina = request.forms.visina,
#                 teza = request.forms.teza,
#                 letoRojstva = request.forms.letoRojstva
#             )
#         else: raise Exception('Negativna vrednost')
#     except:
#         st_dresa = request.forms.stDresa
#         imeZDresom = modeli.ime_igralca(st_dresa)
#         return template('dodaj_igralca', 
#                         st = st_dresa, 
#                         ime = imeZDresom,
#                         imeIgralca = request.forms.imeIgralca,
#                         pozicija = request.forms.pozicija,
#                         visina = request.forms.visina,
#                         teza = request.forms.teza,
#                         letoRojstva = request.forms.letoRojstva,
#                         napaka = True)
#     redirect('/igralci/')

# def ali_slika_obstaja(id):
#     """ funkcija preveri, če fotografija obstaja na naslovu /static/id.png"""
#     nekaj = os.path.exists("./static/" + str(id) + ".png")
#     return nekaj


# @get('/najboljsi/')
# def najboljsi():
#     ekipe = modeli.ekipe()
#     return template('najboljsi', seznamEkip = ekipe, stevec = 1)

# @post('/najboljsi/')
# def najboljsi_igralec():
#     if request.forms.get("izbiraEkipe"):
#         izbranaEkipa = request.forms.izbiraEkipe
#         sezDatumov = modeli.poisci_datume(str(izbranaEkipa))
#         return template('najboljsi', ekipa = izbranaEkipa, seznamDatumov = sezDatumov, stevec = 2)
#     elif request.forms.get("izbiraDatuma"):
#         izbraniDatum = request.forms.izbiraDatuma
#         ekipa = modeli.vrni_ekipo(str(izbraniDatum))
#         najvecTock = list(modeli.najvec_tock(izbraniDatum))
#         najvecPodaj = list(modeli.najvec_podaj(izbraniDatum))
#         najvecSkokov = list(modeli.najvec_skoki(izbraniDatum))
#         najvecUkradenih = list(modeli.najvec_ukradene(izbraniDatum))
#         najvecTock.append(modeli.ime_igralca(najvecTock[0]))
#         najvecPodaj.append(modeli.ime_igralca(najvecPodaj[0]))
#         najvecSkokov.append(modeli.ime_igralca(najvecSkokov[0]))
#         najvecUkradenih.append(modeli.ime_igralca(najvecUkradenih[0]))
#         return template('najboljsi', datum = izbraniDatum, stevec = 3, ekipa = ekipa, najvecT = najvecTock,
#                         najvecP = najvecPodaj, najvecS = najvecSkokov, najvecU = najvecUkradenih)

run(host='localhost', port=8080, reloader=True, debug=True)
