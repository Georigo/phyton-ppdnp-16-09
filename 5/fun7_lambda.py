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
