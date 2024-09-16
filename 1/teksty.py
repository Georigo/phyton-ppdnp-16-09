tekst = "Witaj świecie"
print(tekst)
print(type(tekst))
# Witaj świecie
# <class 'str'>

# teksty w pythonie są niemutowalne
tekst.upper()
# "" Return a copy of the string converted to uppercase. """
print(tekst)  # Witaj świecie
print(tekst.upper())  # WITAJ ŚWIECIE
tekst_upper = tekst.upper()
print(tekst_upper)
print(tekst)

print(tekst.lower())  # witaj świecie

# witaj świecie
# 01234567
print(tekst.index("j"))  # na indeksie numer 4 (pozycja 5)
print(tekst.index("i"))  # 1
print(tekst.count("i"))  # 3 razy
print(tekst.count("j", 0, 4))  # wystepuje 0 razy, z prawej strony zbiór otwarty, 0123

print(tekst.removeprefix("Witaj"))  # " świecie"
print(tekst.removesuffix("świecie"))  # "Witaj "

tekst_zamiana = "Witaj dobry świecie"
print(tekst_zamiana.replace('dobry', ""))  # "Witaj  świecie"
print(tekst.removesuffix("świecie").strip())  # "Witaj", strip() - usunięcie białych znaków np.: spacji

print(tekst[4])  # litera na indeksie 4 -> "j"

# kodowanie znaków
encode_s = tekst.encode('utf-8')
print(encode_s)  # b'Witaj \xc5\x9bwiecie', typ bajtowy
# \xc5\x9 - zapis szesnastkowy wartosci w bajtach, \xc5 - 197 dziesietnie
print(type(encode_s))  # <class 'bytes'>
print(encode_s.decode('utf-8'))  # Witaj świecie

imie = "Radek"
# f - fstring - string sformatowany
tekst_format = f"Mam na imię {imie} i lubię pythona."
print(tekst_format)  # Mam na imię Radek i lubię pythona.
tekst_format_1 = f"\tMam na imię {imie}\n i lubię pythona.\b"
print(tekst_format_1)
# "	Mam na imię Radek
# i lubię pythona"
# \t tabulator
# \n nowa linia
# \b backspace

starszy = "Witaj %s!"  # %s - string
print(starszy % imie)  # Witaj Radek!
print(starszy % ("\b" * 3))  # Wit!

 je

# tekst wielolinijkowy
print("""Tekst
    wielolinijkowy""")
# "Tekst
#    wielolinijkowy"
