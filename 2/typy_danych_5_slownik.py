# słownik - para klucz-wartosc
# {"user":"Radek", "wiek":67}
# słownik jest odpowiednikiem jsona w pythonie
# klucze nie mogą się powtórzyc

# pusty słownik
dictionary = dict()
print(type(dictionary))  # <class 'dict'>
print(dictionary)  # {}

dictionary_1 = {}
print(dictionary_1)  # {}
print(type(dictionary_1))  # <class 'dict'>

# dodawanie elementów do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}
dictionary["wiek"] = 38
print(dictionary)  # {'imie': 'Radek', 'wiek': 38}

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
# dict_keys(['imie', 'wiek'])
# dict_values(['Radek', 38])
# dict_items([('imie', 'Radek'), ('wiek', 38)])

# wypisanie elementów
print(dictionary['imie'])  # Radek
# print(dictionary['Imie'])  # KeyError: 'Imie'
print(dictionary.get("Imie"))  # None - domyslna wartośc, gdy brak klucza w słowniku
print(dictionary.get("Imie", "Domyślna"))  # Domyślna

dictionary.update({'data': '12-1aa a2-2024'})
print(dictionary)  # {'imie': 'Radek', 'wiek': 38, 'data': '12-12-2024'}

dict_small = {'x': 2}
dict_small.update([('y', 3), ('z', 5)])
print(dict_small)  # {'x': 2, 'y': 3, 'z': 5}

# input() - pobiera dane od użytkownika np.: z klawiatury
tekst = input("Podaj imie")
print(tekst)
print(type(tekst))  # <class 'str'> zawsze zwraca string

# napisac program kalkulator
# pobrac dwie liczby -> 2 x input
# wyswietlic wynik -> print
a = float(input("Podaj pierwszą liczbę"))
b = input("Podaj drugą liczbę")
print(a + int(b))  # 11.0

# napisac słownik pol-ang
# słownik zawierający pary pol-ang
# wypisac klucze
# pobrac słowo od uzytkownika
# wyswietlic tłumaczenie (wartosc dla klucza)
pol_ang = {'kot': 'cat', 'pies': 'dog'}
print(f"Znam takie slowka: {pol_ang.keys()}")
odp = input("Podaj słowko do przetłumaczenia").lower()
print(pol_ang[odp.lower().replace(" ", "")])
print(pol_ang.get(odp, "nie mo"))
