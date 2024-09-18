dictionary = {"imie": "Radek", 'nazwisko': "Kowalski"}
print(type(dictionary))  # <class 'dict'>

# wyświetli klucze
for i in dictionary:
    print(i)
# imie
# nazwisko

for i in dictionary.keys():
    print(i)
# imie
# nazwisko

# wyswietli wartosci
for i in dictionary.values():
    print(i)
# Radek
# Kowalski

# wyswietla pary
for i in dictionary.items():
    print(i)
# ('imie', 'Radek')
# ('nazwisko', 'Kowalski')
for k, v in dictionary.items():
    print(k, "=>", v)
# imie => Radek
# nazwisko => Kowalski
# Prints the values to a stream, or to sys.stdout by default.
#
# sep
#   string inserted between values, default a space. - default " "
# end
#   string appended after the last value, default a newline.
for k, v in dictionary.items():
    print(k, v, sep="=>")
# imie=>Radek
# nazwisko=>Kowalski
for k, v in dictionary.items():
    print(k, v, end="<=>")
    # imie Radek<=>nazwisko Kowalski<=>
print("Coś")  # imie Radek<=>nazwisko Kowalski<=>Coś
print("Nowa linia")
# imie Radek<=>nazwisko Kowalski<=>Coś
# Nowa linia

pol_ang = {'kot': 'cat', 'pies': 'dog'}
ang_pol = {}
for k, v in pol_ang.items():
    ang_pol[v] = k
print(ang_pol)  # {'cat': 'kot', 'dog': 'pies'}

print({value: key for key, value in pol_ang.items()})
# {'cat': 'kot', 'dog': 'pies'}
