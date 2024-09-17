# kolekcja - wile danych w jednym pudełko
# lista - przechowuje wiele danych różnego typu na raz
# zachowuje kolejność przy dodawaniu elementów
from sys import base_prefix

lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(type(pusta_lista))  # <class 'list'>
print(pusta_lista)  # []

# append() - dowanie elementów do listy
lista.append("Radek")
lista.append("Tomek")
lista.append("Zenek")
lista.append("Grzegorz")
lista.append("Mariusz")
lista.append("Ja")
lista.append("Malwina")
print(lista)
# ['Radek', 'Tomek', 'Zenek', 'Grzegorz', 'Mariusz', 'Ja', 'Malwina']
#     0         1        2        3           4        5       6
#    -7        -6       -5       -4          -3       -2       -1
print(lista[0])  # Radek
print(lista[2])  # Zenek
print(lista[4])  # Mariusz
# dla elemntu(ndeksu) spoza listy mamy błąd:
# print(lista[7])  # IndexError: list index out of range
print(len(lista))  # 7
# 7 - 1
print(len(lista) - 1)
print(lista[-1])  # Malwina, ostatni elemnt z listy
print(lista[-3])  # Mariusz
print(lista[-2])  # Ja

# wyswietlanie fragmentu listy (slicownie)
print(lista[0:3])  # start:stop -> 012 zbior otwarty, ['Radek', 'Tomek', 'Zenek']
print(lista[:3])  # ['Radek', 'Tomek', 'Zenek']
print(lista[2:])  # ['Zenek', 'Grzegorz', 'Mariusz', 'Ja', 'Malwina'] 2,3,4,5,6
print(lista[2:6])  # ['Zenek', 'Grzegorz', 'Mariusz', 'Ja'] 2,3,4,5
print(lista[2:7])  # ['Zenek', 'Grzegorz', 'Mariusz', 'Ja', 'Malwina']
print(lista[2:15])  # ['Zenek', 'Grzegorz', 'Mariusz', 'Ja', 'Malwina']
print(lista[:])  # ['Radek', 'Tomek', 'Zenek', 'Grzegorz', 'Mariusz', 'Ja', 'Malwina']
print(lista[2:3])  # ['Zenek']
print(lista[2:2])  # []
print(lista[10:29])  # []

# ['Radek', 'Tomek', 'Zenek', 'Grzegorz', 'Mariusz', 'Ja', 'Malwina']
#     0         1        2        3           4        5       6
#    -7        -6       -5       -4          -3       -2       -1
print(lista[-2:0])  # [-2:-7], [4:0] -> []
print(lista[0:-2])  # ['Radek', 'Tomek', 'Zenek', 'Grzegorz', 'Mariusz']

lista_15 = list(range(15))  # 0 do 14
print(lista_15)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(lista_15[0:15:2])  # start:stop:krok, [0, 2, 4, 6, 8, 10, 12, 14]
print(lista_15[-10])  # 5
print(list(range(0, 15, 2)))  # [0, 2, 4, 6, 8, 10, 12, 14]

# nadpisanie elementu w liście
# zmieniana jest bazowa lista
lista[3] = "Mikołaj"
print(lista)
# ['Radek', 'Tomek', 'Zenek', 'Mikołaj', 'Mariusz', 'Ja', 'Malwina']

# insert() wstawienie elementu we wskazanym indeksie
lista.insert(1, "Karol")
print(lista)  # ['Radek', 'Karol', 'Tomek', 'Zenek', 'Mikołaj', 'Mariusz', 'Ja', 'Malwina']

# sprawdzenie indeksu elementu
print(lista.index("Mikołaj"))  # 4
lista.append("Mikołaj")
print(lista)  # ['Radek', 'Karol', 'Tomek', 'Zenek', 'Mikołaj', 'Mariusz', 'Ja', 'Malwina', 'Mikołaj']
print(lista.index("Mikołaj"))  # 4 zwraca pierwsze wystąpienie

# usunięcie elemntu, pierwsze wystąpienie
lista.remove("Mikołaj")
print(lista)  # ['Radek', 'Karol', 'Tomek', 'Zenek', 'Mariusz', 'Ja', 'Malwina', 'Mikołaj']

# usunięcie po indeksie
print(lista.pop(5))  # Ja usunięty elemnt na indeksie 5, zwraca usunięty element
print(lista.pop(-2))  # Malwina
print(lista)  # ['Radek', 'Karol', 'Tomek', 'Zenek', 'Mariusz', 'Mikołaj']
print(lista.pop())  # Mikołaj

a = 1
b = 3
a = b
print(a, b)  # 3 3
b = 7
print(a, b)  # 3 7

lista_2 = lista  # a = b, kopiuje referencje (adres)
lista_copy = lista.copy()  # kopia elemntów listy
lista.clear()  # b =7 , czyszcenie listy
print(lista)  # []
print(lista_2)  # []
print(lista_copy)
print(id(lista))  # 1418136260992
print(id(lista_2))  # 1418136260992
print(id(lista_copy))  # 2122795319040
print(type(lista_copy))  # <class 'list'>
