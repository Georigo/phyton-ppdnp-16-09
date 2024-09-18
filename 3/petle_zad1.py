# pętle - dająmożliwośc wykonania wielokrotnie tego samego kodu
# for - pętla iteracyjna
import random

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
