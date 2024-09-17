# krotka (tupla) - kolekcja niemutowalna
# pozwala efektywniej zarządzać pamięcią
# krotka jednoelementowa - stała - zmienna

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
