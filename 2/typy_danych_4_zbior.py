# zbiór - przechowuje unikalne elementy
# nie zachowuje kolejności
# nie posiada indeksu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}
print(type(zbior))  # <class 'set'>

# tworzenie pustego zbioru
zb2 = set()
print(zb2)  # set()
print(type(zb2))  # <class 'set'>

# dodanie do zbioru
zbior.add(33)
zbior.add(18)
zbior.add(18)
zbior.add(18)
zbior.add(24)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55, 24}

# usunięcie elementu ze zbioru
zbior.remove(55)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 24}

# pop() - usunie pierwszy element ze zbioru
print(zbior.pop())  # 33
print(zbior)  # {66, 777, 11, 44, 18, 22, 24}

zbior_copy = zbior.copy()
print(zbior_copy)  # {66, 18, 22, 24, 777, 11, 44}

zbior_2 = {667, 11, 44, 18, 52, 62, 999, 999, 12.34}
print(type(zbior_2))  # <class 'set'>
print(zbior_2)  # {999, 11, 44, 12.34, 18, 52, 667, 62}

# zwracaj anowy zbiór
# suma zbiorów
print(zbior | zbior_2)  # {66, 999, 777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62}
print(zbior.union(zbior_2))  # {66, 999, 777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62}

# częśc wspólna
print(zbior & zbior_2)  # {18, 11, 44}
print(zbior.intersection(zbior_2))  # {18, 11, 44}

# róznica
print(zbior - zbior_2)  # {24, 777, 66, 22}
print(zbior.difference(zbior_2))  # {24, 777, 66, 22}
print(zbior_2.difference(zbior))  # {999, 12.34, 52, 667, 62}

# Uwaga!!! Łączy zbiory, nadpisuje bazowy!!!
zbior.update(zbior_2)
print(zbior)  # {66, 999, 777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62}

krotka = tuple(zbior)
print(krotka)  # (66, 999, 777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62)

lista = list(zbior)
print(lista)  # [66, 999, 777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62]

# sprawdzenie czy lelement istnieje w zbiorze
print(999 in zbior_2)  # True
