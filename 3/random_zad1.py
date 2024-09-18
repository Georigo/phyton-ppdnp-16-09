import random

print(random)
# <module 'random' from 'C:\\Users\\CSComarch\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\random.py'>

# do generowania liczb pseudolosowych

print(random.randint(1, 100))  # int od 1 to 100
print(random.randrange(1, 100))  # od 1 do 99
print(random.randrange(100))  # int od 0 do 99
print(random.random())  # 0.3737094487098441 float od 0 do 0.9999999
print(random.random() * 10)  # 0.3737094487098441 float od 0 do 9.9999999

lista = [67, 45, 32, 68, 89, 90, 42]
print(random.choice(lista))  # element 68

lista_kule = list(range(1, 50))
print(lista_kule)

wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)

print(random.choices(lista_kule, k=6))  # losowanie z powtórzeniami [39, 39, 3, 6, 13, 31]
print(random.sample(lista_kule, k=6))  # [44, 45, 28, 14, 25, 46]
print(random.sample(lista_kule, 6))  # losowanie bez powtórzen [14, 38, 37, 45, 24, 39]
