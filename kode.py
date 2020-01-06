import csv

with open("podatki/airports.csv", encoding="UTF-8") as letalisca:
    with open("podatki/kode.csv", "w", encoding="UTF-8", newline="\n") as kode:
        with open("podatki/letalisca.csv", "w", encoding="UTF-8", newline="\n") as let2:
            csv_in = csv.reader(letalisca)
            csv_out = csv.writer(let2)
            csv_mock = csv.writer(kode)
            csv_out.writerow(["koda_letalisce", "ime"])
            for vrstica in csv_in:
                if vrstica[4] == r"\N":
                    continue
                csv_out.writerow([vrstica[4], vrstica[1]])
                csv_mock.writerow([vrstica[4]])

            