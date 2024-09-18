# wyjątki -
# błedy podczas wykonywania programu
# przerywaja działanie programu

# print(5 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\ppdnp-16-09\3\wyjatki.py", line 5, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero

try:
    # print(5 / 0)
    # print("A" + 9)
    # print(int("A"))
    # raise KeyError("Brak klucza")  # rzucenie błedu
    wynik = 90 / 33
except ZeroDivisionError:
    print("Nie dziel przez zero")
except TypeError:
    print("Błąd typu")
except ValueError:
    print("Błąd wartosci")
except Exception as e:  # obsługa pozostałych błedów
    print("Bład", e)
else:  # wykonuje się tylko gdy nie ma błedu
    print(f"Wynik działania {wynik}")
finally:  # wykonuje sie zawsze
    print("Zakończyłem obliczenie")

print("program nadal działa")
# Nie dziel przez zero
# program nadal działa
# Błąd typu
# program nadal działa
# Błąd wartosci
# program nadal działa
# Bład 'Brak klucza'
# program nadal działa
# Wynik działania 2.727272727272727
# Zakończyłem obliczenie
# program nadal działa

# za pomocą kontrukcji try - except [else - finally]
