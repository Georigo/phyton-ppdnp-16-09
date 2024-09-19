# pliki csv - pliki w których dane oddzielone znakiem podziału
# Kowalski,Jan,Kłodzko
# Nowak,Zenon,Szczecin
# Brzęczyszczykiewicz,Grzegorz,Chrząszczyżewoszyce
# ,;tab

import csv

row = ['Radek', 'Coe', 2, 9.1]

filename = "records.csv"

with open(filename, "w") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(row)
