# pętle - dająmożliwośc wykonania wielokrotnie tego samego kodu
# for - pętla iteracyjna
import random
from encodings.utf_7 import encode

for i in range(5):  # od 0 do 4
    print(i)

for i in range(10):
    pass  # nic nie rób

for _ in range(10):  # niema zmienna
    print("Test podłoga")
    print(_)
# Test podłoga
# 0
# Test podłoga
# 1
# Test podłoga
# 2
# Test podłoga
# 3
# Test podłoga
# 4
# Test podłoga
# 5
# Test podłoga
# 6
# Test podłoga
# 7
# Test podłoga
# 8
# Test podłoga
# 9
for i in range(20):
    print(i * 2)

# przerobic na petle lotto
lista_kule = list(range(1, 50))
lista_wyn = []
for _ in range(6):
    wyn = random.choice(lista_kule)
    lista_kule.remove(wyn)
    # print(wyn)
    lista_wyn.append(wyn)

print(lista_wyn)  # [8, 30, 2, 43, 40, 21]

for i in range(10):
    if i % 2 == 0:  # modulo/reszta z dzielenia
        print(i, "parzysta")
# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

# list comprehension
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

print(lista_wyn)  # [4, 42, 5, 46, 28, 49]

for c in lista_wyn:
    if c > 10:
        print("Większe od 10", c)
    else:
        print("Mniejsze (równe) od 10", c)
# Większe od 10 37
# Mniejsze (równe) od 10 4
# Większe od 10 22
# Większe od 10 20
# Większe od 10 25
# Większe od 10 29

for i in range(0, 10, 2):  # start, stop, krok
    print(i)

for i in range(10, 0, -2):  # krok ujemny, krok wstecz
    print(i)
# 10
# 8
# 6
# 4
# 2

for i in range(-10, 0):
    print(i)

# jakie wartosci przyjmie c?
# [0, 2, 4, 6, 8]
for c in lista3:
    if c == 2:
        c += 1
        print(c)
    print("Przy kazdym elemencie pętli", c)
# Przy kazdym elemencie pętli 0
# 3
# Przy kazdym elemencie pętli 3
# Przy kazdym elemencie pętli 4
# Przy kazdym elemencie pętli 6
# Przy kazdym elemencie pętli 8

imiona = ["Radek", "Tomek", "Zenek", "Anna"]
print(imiona)
print(type(imiona))
# ['Radek', 'Tomek', 'Zenek', 'Anna']
# <class 'list'>

for p in imiona:
    print(p)
# Radek
# Tomek
# Zenek
# Anna

# jak te elementy wyswietlic w postaci 0 Radek
for p in imiona:
    print(imiona.index(p), p)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Anna

for i in range(len(imiona)):  # range(4) -> 0123
    print(i, imiona[i])
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Anna

# enumerate()
for p in enumerate(imiona):
    print(p)
# (0, 'Radek')
# (1, 'Tomek')
# (2, 'Zenek')
# (3, 'Anna') -> 0 Radek
a, b = (2, 'Zenek')
print(a, b)  # 2 Zenek

for i, o in enumerate(imiona):
    print(i, o)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Anna
for i, o in enumerate(imiona, start=1):
    print(i, o)
# 1 Radek
# 2 Tomek
# 3 Zenek
# 4 Anna

ludzie = ['Radek', "Tomek", "Zenek", 'Magda']
wiek = [44, 55, 32, 27]
# wypisac to tak: Radek 44
for p in ludzie:
    print(p, wiek[ludzie.index(p)])
# Radek 44
# Tomek 55
# Zenek 32
# Magda 27
ludzie = ['Radek', "Tomek", "Zenek", 'Magda', "Marek"]
wiek = [44, 55, 32, 27]
# for p in ludzie:
#     print(p, wiek[ludzie.index(p)])# IndexError: list index out of range

# zip() - łączy elemnty w kolekcje
for i in zip(ludzie, wiek):
    print(i)
# ('Radek', 44)
# ('Tomek', 55)
# ('Zenek', 32)
# ('Magda', 27)
for l, w in zip(ludzie, wiek):
    print(l, w)
# Radek 44
# Tomek 55
# Zenek 32
# Magda 27

# 0 Radek 44
for i in enumerate(zip(ludzie, wiek)):
    print(i)
    # (0, ('Radek', 44))  -> 0 Radek 44
    # (1, ('Tomek', 55))
    # (2, ('Zenek', 32))
    # (3, ('Magda', 27))
a, b = (0, ('Radek', 44))
print(a, b)  # 0 ('Radek', 44)
c, d = ('Radek', 44)
print(c, d)  # Radek 44
print(a, c, d)  # 0 Radek 44
a, (c, d) = (0, ('Radek', 44))
print(a, c, d)  # 0 Radek 44
for i, (l, w) in enumerate(zip(ludzie, wiek)):
    print(i, l, w)
# 0 Radek 44
# 1 Tomek 55
# 2 Zenek 32
# 3 Magda 27
