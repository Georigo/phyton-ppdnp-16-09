# kolekcja - wile danych w jednym pudełko
# lista - przechowuje wiele danych różnego typu na raz
# zachowuje kolejność przy dodawaniu elementów

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
print(lista[-3]) # Mariusz
print()