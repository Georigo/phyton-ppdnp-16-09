class Human:
    """
    Klasa human opisująca człowieka  w pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda incjalizująca (konstruktor)
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print(f"Nazywam się {self.imie}")

    def wypisz_wzrost(self):
        print(f"Mam {self.wzrost} cm wzrostu")

    def ruszaj(self):
        if self.plec == "k":
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłem w drogę")


# cz1 = Human()  # TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'

cz1 = Human("Anna", 34, 165)
print(cz1.plec)
print(cz1.wiek)
print(cz1.wzrost)
print(cz1.imie)
cz1.powitanie()  # Nazywam się Anna
cz1.wypisz_wzrost()  # Mam 165 cm wzrostu
cz1.ruszaj()  # Ruszyłam w drogę

cz2 = Human("Radek", 39, 178, "m")
cz2.powitanie()
cz2.wypisz_wzrost()
cz2.ruszaj()
# Nazywam się Radek
# Mam 178 cm wzrostu
# Ruszyłem w drogę
