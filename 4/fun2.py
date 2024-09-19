# funkcje wracające wynik
# kończy się komendą return
# gdy napotka return wychodzi z funkcji

def dodaj(a, b):
    return a + b


def odejmij(a=0, b=0, c=0):
    return a - b - c


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(dodaj(6, 8))  # 14
wynik = dodaj(6, 9)
print("Wynik działania", wynik)  # Wynik działania 15

print(odejmij())
print(odejmij(3, 4))
print(odejmij(3, 4, 8))
print(odejmij(3, c=4, b=48))

print(oblicz_vat(1000))
print(oblicz_vat(1000, 7))
print(oblicz_vat(cena=100, vat=18))
# 1230.0
# 1070.0
# 118.0
zm = oblicz_vat(1000)
if zm == 1230:
    print("ok")  # ok

print(oblicz_vat(1000) + dodaj(5, 89))  # 1324.0
