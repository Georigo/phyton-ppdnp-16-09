# krotka (tupla) - kolekcja niemutowalna
# pozwala efektywniej zarządzać pamięcią
# krotka jednoelementowa - stała - zmienna
from time import perf_counter
from traceback import print_tb

tupla = ("Radek")
print(type(tupla))  # <class 'str'>

tupla_2 = "Radek",
print(type(tupla_2))  # <class 'tuple'>

# PEP8 zaleca dla tupli jedoelemntowej uzywać nawiasów
tupla_3 = ("Radek",)
print(type(tupla_3))  # <class 'tuple'>
print(tupla_3)  # ('Radek',)

tupla_liczby = 43, 55, 22.34, 11, 200
print(type(tupla_liczby))  # <class 'tuple'>

# tupla jest niemutowalna
# tupla_liczby[2] = 123  # TypeError: 'tuple' object does not support item assignment

# mozna usunąć całą tuple
del tupla_liczby
# print(tupla_liczby)  # NameError: name 'tupla_liczby' is not defined

tupla_imiona = "Radek", "Tomek", "Zenek", "Michał", "Mariusz", "Grzegorz"
print(tupla_imiona)  # ('Radek', 'Tomek', 'Zenek', 'Michał', 'Mariusz', 'Grzegorz')
print(type(tupla_imiona))  # <class 'tuple'>

print(tupla_imiona.count("Radek"))  # wystepuje 1 raz
print(tupla_imiona.index("Mariusz"))  # index numer 4

# rozpakowanie tupli (krotki)
tup = 1, 2
print(type(tup))  # <class 'tuple'>

a, b = 1, 2
print(a, b)  # 1 2
a, b = b, a
print(a, b)  # 2 1
a, b = tup
print(a, b)  # 1,2
# a, b = 1, 2, 3# ValueError: too many values to unpack (expected 2)
tup_3_elementy = 1, 2, 3
# a, b = tup_3_elementy
a, *b = tup_3_elementy
print(a, b)  # 1 [2, 3] * worek na pozostale dane
*a, b = tup_3_elementy
print(a, b)  # [1, 2] 3

print(tupla_imiona)
print(len(tupla_imiona))

# name1, name2, name3, name4
print(tupla_imiona)  # ('Radek', 'Tomek', 'Zenek', 'Michał', 'Mariusz', 'Grzegorz')
name1, *name2, name3, name4 = tupla_imiona
print(name1, name2, name3, name4)
# Radek ['Tomek', 'Zenek', 'Michał'] Mariusz Grzegorz
name1, name2, *name3, name4 = tupla_imiona
print(name1, name2, name3, name4)
# Radek Tomek ['Zenek', 'Michał', 'Mariusz'] Grzegorz

# sortowanie krotki zwraca listę
print(sorted(tupla_imiona))  # ['Grzegorz', 'Mariusz', 'Michał', 'Radek', 'Tomek', 'Zenek']
print(tupla_imiona)  # ('Radek', 'Tomek', 'Zenek', 'Michał', 'Mariusz', 'Grzegorz')

lista = list(tupla_imiona)
print(lista)  # ['Radek', 'Tomek', 'Zenek', 'Michał', 'Mariusz', 'Grzegorz']
print(type(lista))  # <class 'list'>
