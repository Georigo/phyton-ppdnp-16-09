# pliki csv - pliki w których dane oddzielone znakiem podziału
# Kowalski,Jan,Kłodzko
# Nowak,Zenon,Szczecin
# Brzęczyszczykiewicz,Grzegorz,Chrząszczyżewoszyce
# ,;tab

import csv

row = ['Radek', 'Coe', 2, 9.1]
fields = ['name', 'branch', 'year', 'cgpa']

dictionary = dict(zip(fields, row))
print(type(dictionary))
print(dictionary)
# <class 'dict'>
# {'name': 'Radek', 'branch': 'Coe', 'year': 2, 'cgpa': 9.1}

filename = "records.csv"

# newline="" - ominięcie problemu pustej linii
with open(filename, "w", newline="") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(fields)
    csvwriter.writerow(row)

filename = 'records_dict.csv'
# zapisanie danych ze słownika do csv
with open(filename, "w", newline="") as f:
    csvwriter = csv.DictWriter(f, fieldnames=fields)
    csvwriter.writeheader()
    csvwriter.writerow(dictionary)

products = [
    {'sku': 1, 'exp_date': "today", 'price': 200},
    {'sku': 2, 'exp_date': "today", 'price': 100},
    {'sku': 3, 'exp_date': "tomorrow", 'price': 500},
    {'sku': 4, 'exp_date': "today", 'price': 25.99},
]

print([i for i in products[0].keys()])
# ['sku', 'exp_date', 'price']
fields_products_temp = [i for i in products[0].keys()]
filename = 'records_list_products.csv'
fields_products = ['sku', 'exp_date', 'price']
with open(filename, "w", newline="") as f:
    # TypeError: "delimiter" must be a 1-character string
    csvwriter = csv.DictWriter(f, fieldnames=fields_products, delimiter=";")
    csvwriter.writeheader()
    csvwriter.writerows(products)

# delimiter=";" - znak podziału
