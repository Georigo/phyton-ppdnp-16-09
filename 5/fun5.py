# storzenie funkcji obliczającej średnią
def liczby(name=None, *cyfry):
    print(cyfry)  # (3, 4, 4, 4, 3, 2)
    print(type(cyfry))  # <class 'tuple'>
    count = len(cyfry)
    suma_sum = sum(cyfry)
    print(suma_sum)
    suma = 0
    try:
        for c in cyfry:
            suma += c
        avg = suma / count
        avg_sum = suma_sum / count
    except Exception as e:
        print("Bład", e)
    else:
        print(f"Średnia dla ucznia {name} wynosi {avg}")
        print(f"Średnia dla ucznia {name} wynosi {avg_sum}")
    finally:
        print("Następny uczeń")


liczby()
liczby(4, 5, 6, 5, 6, 5, 6)
liczby(2, 3, 4, 4, 4, 3, 2)
liczby("Anna", 2, 3, 4, 4, 4, 3, 2)
# ()
# Bład division by zero
# Następny uczeń
# (4, 5, 6, 5, 6, 5, 6)
# Średnia wynosi 5.285714285714286
# Następny uczeń
# (2, 3, 4, 4, 4, 3, 2)
# Średnia wynosi 3.142857142857143
# Następny uczeń
