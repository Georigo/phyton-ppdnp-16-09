# funkcja lambda - skrócony zapis funkcji
# funkcja zwraca wyni, domyślnie ma return
# funkcja anonimowa, mozliwosc deklaracji w miejscu wykonania

def odejmij(a, b):
    return a - b


print(odejmij(23, 8))  # 15

odejmij2 = lambda a, b: a - b  # to oznacza return a - b
print(odejmij2(23, 8))  # 15

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(5))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(17))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(25))  # dorosły

lista_wyn = []
lista = [1, 2, 3, 10, 20, 30, 50, 70, 200, 250]
for i in lista:
    lista_wyn.append(i * 2)

print(lista_wyn)  # [2, 4, 6, 20, 40, 60, 100, 140, 400, 500]
print([i * 2 for i in lista])  # [2, 4, 6, 20, 40, 60, 100, 140, 400, 500]


def zmiana(x):
    return x * 2


lista_wyn2 = []
for i in lista:
    lista_wyn2.append(zmiana(i))
print(lista_wyn2)  # [2, 4, 6, 20, 40, 60, 100, 140, 400, 500]

# funkcje wyzszego rzedu
# map() - pobiera element, wykonuje na nim wskazaną funkcję
print(f"Zastosowanie map(): {list(map(zmiana, lista))}")
# Zastosowanie map(): [2, 4, 6, 20, 40, 60, 100, 140, 400, 500]
# użycie lambdy jako funkcji anonimowej
print(f"Zastosowanie map(): {list(map(lambda x: x * 2, lista))}")
print(f"Zastosowanie map(): {list(map(lambda x: x * 4, lista))}")
print(f"Zastosowanie map(): {list(map(lambda x: x * 12, lista))}")
# Zastosowanie map(): [4, 8, 12, 40, 80, 120, 200, 280, 800, 1000]
# Zastosowanie map(): [12, 24, 36, 120, 240, 360, 600, 840, 2400, 3000]

# filtrowanie danych

l3 = []
for i in lista:
    if i < 20:
        l3.append(i)

print(l3)  # [1, 2, 3, 10]

# filter() - wraca tylko dane spełniające warunek
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 20, lista))}")  # Zastosowanie filter(): [1, 2, 3, 10]
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 20, lista))}")  # Zastosowanie filter(): [1, 2, 3, 10]
print(
    f"Zastosowanie filter(): {list(filter(lambda x: x > 5 and x < 100, lista))}")  # Zastosowanie filter(): [1, 2, 3, 10]
# Zastosowanie filter(): [1, 2, 3, 10]
# Zastosowanie filter(): [30, 50, 70, 200, 250]
# Zastosowanie filter(): [10, 20, 30, 50, 70]
print(f"Zastosowanie filter(): {list(filter(lambda x: 5 < x < 100, lista))}")
# Zastosowanie filter(): [10, 20, 30, 50, 70]

# functools
