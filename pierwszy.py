import sys

print()  # wypisz/wydrukuj
print()

print()
print("Nazywam się Radek")  # Nazywam się Radek
print('Nazywam się Radek')
# print('Nazywam się Radek")
#   File "C:\Users\CSComarch\PycharmProjects\ppdnp-16-09\pierwszy.py", line 7
#     print('Nazywam się Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 7)
print("R")
print("a")
print("d")
print("e")
print("k")
print("k")
# ctrl D - powielanie lini
print("Nazywam się 'Radek'")  # Nazywam się 'Radek'

# type() - sprawdzenie typu danych
print(type("Radek"))  # <class 'str'>, czyli tekst (string)
# ctrl alt l - dostosowuje kod do zasad PEP8
print('39')  # 39
print(type('39'))  # <class 'str'>
print("39" + "39")  # konkatenacja, łączenie stringów 3939

print(39)
print(type(39))  # integer, <class 'int'> liczby calkowite
print(39 + 39)  # 78 - operacje wykonane na liczbach
print(sys.int_info)
# sys.int_info(
#     bits_per_digit=30,
#     sizeof_digit=4,
#     default_max_str_digits=4300,
#     str_digits_check_threshold=640
# )
# print("39" + 39)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\ppdnp-16-09\pierwszy.py", line 40, in <module>
#     print("39" + 39)
#           ~~~~~^~~~
# TypeError: can only concatenate str (not "int") to str

# silne typowanie - sam nie zamienia typow podczas operacji

print(int("39") + 39)  # int() zamiana(rzutowanie) na typ int, 78

print(5 * "4")  # 44444

# odmienne operacje
print(168 * "45")
print(168 * 45)

# zmienna - pudełko na dane
# przechowuje jedną wartość
# w dowolnym momencie możemy wrzucic dowolny typ danych
# typowanie dynamiczne

# snak_case - konwencja nazewnicza dla zmiennych
# nazwa zmiennej powinna wskazywac co przechowuje zmienna
liczba = 39
print(liczba)  # nazwa zmiennej bez cudzysłowiu, wypisze wartośc zmiennej
print(type(liczba))  # <class 'int'>

print("5" * liczba)

liczba = "39"
print(liczba)
print(type(liczba))  # <class 'str'>

name = "Radek"
print(type(name))
print(name + "Kowalski")  # RadekKowalski

name = 90
# print(name + "Kowalski")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'/
print(str(name) + "Kowalski")  # 90Kowalski

# podpowiedz typu (to nie jest ustawienie typu!!!)
name: str = "Radek"
print(name)
name = 90
print(name)
print(type(name))
# <class 'int'>
# Radek
# 90

age: int = 90
print(age)
print(type(age))
