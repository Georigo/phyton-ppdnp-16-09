# while - pętla sterowana warunkiem

# pętla nieskończona
# while True:
#     print("Komunikat 1 !")

licznik = 0
while True:
    licznik += 1
    print("Komunikat 1 !")
    if licznik > 10:
        break
        # przerywa pętle

print(licznik)  # 11
licznik = 0
while licznik < 10:
    licznik += 1
    print("Komunikat 2 !!")
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!

# password = input("Podaj hasło")
# while password != "secret":
#     password = input("Błędne hasło, podaj ponownie")
# print("Hasło prawidłowe")
# Podaj hasłorewrwe
# Błędne hasło, podaj ponowniesdfs
# Błędne hasło, podaj ponowniefsdfsd
# Błędne hasło, podaj ponowniefsfs
# Błędne hasło, podaj ponowniesecret
# Hasło prawidłowe

lista = []
lista_int = []
while True:
    wej = input("Podaj liczbę")
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista_int.append(int(wej))
print(lista)  # ['1', '5', '78', '90', '000']
print(lista_int)
# ['1', '2', '3', '4', '5', '6']
# [1, 2, 3, 4, 5, 6]

my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
element_to_remove = 5
while element_to_remove in my_list:
    my_list.remove(element_to_remove)

print(my_list)  # [1, 2, 3, 4, 6]
