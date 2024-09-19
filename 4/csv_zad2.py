import csv

fields = []
rows = []

# filename = 'records.csv'
# filename = 'records_dict.csv'
filename = 'records_list_products.csv'

with open(filename, "r") as f:
    dialect = csv.Sniffer().sniff(f.read(1024))
    print(dialect.delimiter)  # ;
    f.seek(0)  # powrót na początek pliku
    # csvreader = csv.reader(f, delimiter=";")
    csvreader = csv.reader(f, delimiter=dialect.delimiter)

    print(csvreader)  # <_csv.reader object at 0x0000023624CC57E0>
    fields = next(csvreader)  # pobierze pierwszy element
    for row in csvreader:  # wystartuje od kolejnego elementu
        # print(row)
        rows.append(row)

print("Fields:", fields)
print("Rows:", rows)
# <_csv.reader object at 0x0000022B636A57E0>
# Fields: ['sku', 'exp_date', 'price']
# Rows: [['1', 'today', '200'],
#        ['2', 'today', '100'],
#        ['3', 'tomorrow', '500'],
#        ['4', 'today', '25.99']]
