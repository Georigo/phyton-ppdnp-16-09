a = 10
b = 10


def dodaj():
    a = 7  # zmienne lokalne
    b = 8
    print(a + b)


def dodaj2():
    print(a + b)  # użyje wartości globalnych


def dodaj3():
    global a
    a = 7  # uzywa a globalne, nadpisze globalna wartość a
    b = 34
    print(a + b)


print(f"Zmienna a globalna (z góry) {a=}")  # Zmienna a globalna (z góry) a=10
dodaj()  # 15
print(f"Zmienna a globalna (z góry) {a=}")  # Zmienna a globalna (z góry) a=10
dodaj2()  # 20
print(f"Zmienna a globalna (z góry) {a=}")  # Zmienna a globalna (z góry) a=10
dodaj3()  # 41
print(f"Zmienna a globalna (z góry) {a=}")  # Zmienna a globalna (z góry) a=7
dodaj2()
print(f"Zmienna a globalna (z góry) {a=}")  # Zmienna a globalna (z góry) a=7
