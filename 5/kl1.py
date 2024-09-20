# klasa - element programowania obiektowego
# klasa - szablon, przepis
# pola - zmienne - cechy
# metody - funkcje
# hermetezycja, dziedziczenie, polimorfizm, abstrakcja
# definicja klasy nie uruchmia klasy
# budowanie obiektu uruchamia odpowiednieelemnty klasy


class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """
    imie = ""
    wiek = None
    plec = "k"


cz1 = Human()
print(Human.__doc__)  # dokumentacja kodu
print(print.__doc__)

# pydoc -b  - uruchomienie serwera z dokumentacją
# pydoc -w kl1 - wygenerowanie pliku html z dokumentacją

print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
cz1.imie = "Anna"
cz1.wiek = "34"
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
# Anna
# 34
# k

cz2 = Human()
cz2.imie = "Jan"
cz2.wiek = "34"
cz2.plec = "m"
print(cz2.imie)
print(cz2.wiek)
print(cz2.plec)
