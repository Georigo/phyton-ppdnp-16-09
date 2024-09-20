from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Kalsa opisująca ptaka w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        """
        Metoda iniclizująca (konstruktor)
        :param gatunek:
        :param szybkosc:
        """

        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkoscią", self.szybkosc)

    # metoda abstarkcyjna
    # TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
    @abstractmethod
    def wydaj_odglos(self):
        pass


class Kura(Ptak):  # klasa Kura dziedziczy po klasie Ptak
    def __init__(self, gatunek):
        # obowiązkowo musimy wywołąc konstruktor wyzszej klasy super()
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("Ko ko ko ko")


class Orzel(Ptak):
    """
    klasa Orzel
    """

    def wydaj_odglos(self):
        print("Kier kir kier")

    def poluj(self):
        print(f"Tu {self.gatunek}, ropoczynam polowanie.")


# TypeError: Can't instantiate abstract class Sowa without an implementation for abstract method 'wydaj_odglos'
class Sowa(Ptak):
    """
    klasa sowa
    """


# or1 = Ptak("OrzeL", 50)
# or1.latam()  # Tu OrzeL Lecę z szybkoscią 50
# kur1 = Ptak("Kura domowa", 0)
# kur1.latam()  # Tu Kura domowa Lecę z szybkoscią 0

kur2 = Kura("Kura domowa")
kur2.latam()  # Tu Kura domowa Ja nie latam
or2 = Orzel("Orzel bielik", 55)
or2.latam()
# Tu Kura domowa Ja nie latam
# Tu Orzel bielik Lecę z szybkoscią 55

kur2.wydaj_odglos()
or2.wydaj_odglos()
or2.poluj()

# polimorfizm - wspolne cechy obiektów różnych klas dziedziczących po jedej wspólnej klasie
lista = [or2, kur2]
for i in lista:
    i.wydaj_odglos()

# TypeError: Can't instantiate abstract class Sowa without an implementation for abstract method 'wydaj_odglos'
# sow = Sowa("Sowa", 25)
