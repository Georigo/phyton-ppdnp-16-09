# funkcje - wydzielony fragment kodu, można go wykonać w dowolnym momencie
# funkcja musi byc najpierw zadeklarowana
# w miejscu deklaracji funkcja się nie wykonuje
# zeby wykonać funkcę, trzeba ją wywołać

a = 6
b = 8


# deklaracja funkcji
# tu się nie wykonuje
def dodaj():  # funkcja bezargumentowa
    print(a + b)


def dodaj2(a, b):  # dwa obowiązkowe argumenty
    print(a + b)


def odejmij(a, b, c=0):  # c jest domyslne
    print(a - b - c)


# wywołanie funkcji
# nazwa funkcji, nawiasy ()
# <function dodaj at 0x000001F5389AA840>
dodaj()  # 14
# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'

# argumenty po pozycji
dodaj2(10, 45)  # 55

odejmij(3, 4, 5)  # c=5
odejmij(3, 4)  # c=0

# argumentów po nazwie
odejmij(c=9, a=7, b=14)  # -16
odejmij(b=8, a=78)

# argumenty mieszane
odejmij(1, c=9, b=8)
# odejmij(a=1, b=9, 8)  # SyntaxError: positional argument follows keyword argument

# wypisz wynik działania funkcji dodaj()
print(dodaj())
# 14
# None

# print(dodaj() + dodaj2(5, 8))  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
