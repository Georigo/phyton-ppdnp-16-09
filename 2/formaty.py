user = "Tomek"  # str
wiek = 39  # int
wersja = 3.900001  # <class 'float'>
print(type(wersja))  # <class 'float'>, liczby zmiennoprzecinkowe
liczba = 456123789654  # int
print(type(liczba))  # <class 'int'>

print("Witaj %s, masz teraz %d lat." % (user, wiek))
# Witaj Tomak, masz teraz 39 lat.

# ten sposób wyświetlania sprawdza typy
# print("Witaj %s, masz teraz %d lat." % (wiek, user))
print("Witaj %s, masz teraz %d lat." % (wiek, wersja))  # dla float zadziałą, Witaj 39, masz teraz 3 lat.
print("Witaj %s, masz teraz %d lat.%s,%s" % (wiek, wersja, user, user))  # Witaj 39, masz teraz 3 lat.Tomek,Tomek
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\ppdnp-16-09\2\formaty.py", line 10, in <module>
#     print("Witaj %s, masz teraz %d lat." % (wiek, user))
#           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~
# TypeError: %d format: a real number is required, not str
# %s - łańcuch znaków (string)
# %d: formatowanie liczb całkowitych
print("Witaj %(user)s, masz teraz %(wiek)d lat." % {'user': user, 'wiek': wiek})
# Witaj Tomek, masz teraz 39 lat.
print("Witaj %(user)s, masz teraz %(wiek)d lat. %(user)s" % {'user': user, 'wiek': wiek})
# Witaj Tomek, masz teraz 39 lat. Tomek

print("Witaj {}, masz teraz {} lat".format(user, wiek))  # Witaj Tomek, masz teraz 39 lat

print(f"Witaj {user}, masz teraz {wiek} lat")  # Witaj Tomek, masz teraz 39 lat
# f - fstring, sformatowany string

print("Uzywamy wersji Pythona %i" % 3)  # Uzywamy wersji Pythona 3
print("Uzywamy wersji Pythona %f" % 3)  # UUzywamy wersji Pythona 3.000000
print("Uzywamy wersji Pythona %f" % 3.9)  # Uzywamy wersji Pythona 3.900000
print("Uzywamy wersji Pythona %.2f" % 3.9)  # Uzywamy wersji Pythona 3.90
print("Uzywamy wersji Pythona %.1f" % 3.9)  # Uzywamy wersji Pythona 3.9
print("Uzywamy wersji Pythona %.0f" % 3.9)  # Uzywamy wersji Pythona 4
print("Uzywamy wersji Pythona %.f" % 3.9)  # Uzywamy wersji Pythona 4

print("Wynik = %.2f" % 3.8765)  # Wynik = 3.88
x = 3.14
print("Zero miejsc po przecinku %.f" % x)
# Zero miejsc po przecinku 3
print("X nie zostało zmienione", x)  # X nie zostało zmienione 3.14

y = round(x)
print("y=", y, "x=", x)  # y= 3 x= 3.14

x = 3.1415
print(round(x, 2))  # 3.14

print(f'Uzywamy wersji pythona {wersja}')
# Uzywamy wersji pythona 3.900001
print(f'Uzywamy wersji pythona {wersja:.1f}')
print(f'Uzywamy wersji pythona {wersja:.2f}')
print(f'Uzywamy wersji pythona {wersja:.0f}')
# Uzywamy wersji pythona 3.9
# Uzywamy wersji pythona 3.90
# Uzywamy wersji pythona 4

print(f"{user:>10}")  # "     Tomek"  - wyrównał do prawej
print(f"{user:<20}")  # "Tomek               "
print(f"{user:^25}")  # "          Tomek          "

print(liczba)  # 456123789654
print(f"Nasza duża liczba {liczba:,}")  # Nasza duża liczba 456,123,789,654
print(f"Nasza duża liczba {liczba:_}")  # Nasza duża liczba 456_123_789_654
print(f"Nasza duża liczba {liczba:,}".replace(",", " "))  # Nasza duża liczba 456 123 789 654
print(f"Nasza duża liczba {liczba:,}".replace(",", "."))  # Nasza duża liczba 456.123.789.654

# liczba_2 = 15000000
liczba_2 = 15_000_000
print(type(liczba_2))  # <class 'int'>
print(liczba_2)  # 15000000
