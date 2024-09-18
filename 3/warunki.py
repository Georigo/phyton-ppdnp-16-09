# instrukcje warunkowe
# instrukcje sterowania przpływem programu
# w zaleznosci od warunku (True lub False) wykona jeden lub drugi blok programu
# if

odp = True
print(bool(odp))  # True
# odp = False
if odp:
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print("Dalsza częśc programu")
# True
# Brawo
# Brawo
# Brawo
# Brawo
# Dalsza częśc programu
# dla odp= False wynik:
# True
# Dalsza częśc programu

odp = "Radek"
print(bool(odp))

if odp:
    print("Radek")
# Radek

if odp == "Radek":
    print("Radek")
# True
# Radek
# Radek
odp = "Tomek"
if odp == "Radek":
    print("Radek")
else:  # działanie domyslne
    print("To nie jest Radek")

a = "Radek"
# długosc tekstu wieksza niz 3
if len(a) > 3:
    print("Długośc większa niz 3, wynosi:", len(a))

a = "Radek"
# długosc tekstu wieksza niz 3
n = len(a)
if n > 3:
    print("Długośc większa niz 3, wynosi:", n)

# walrus operator, operator morsa
a = 'Radek'
if (n := len(a)) > 3:
    print("Długośc większa niz 3, wynosi:", n)
# Długośc większa niz 3, wynosi: 5
# Długośc większa niz 3, wynosi: 5
# Długośc większa niz 3, wynosi: 5

# podatek = 0
# zarobki = int(input("Podaj zarobki"))
# if zarobki < 10000:
#     podatek = 0
# elif zarobki < 30000:
#     podatek = 0.2
# elif zarobki < 100000:
#     podatek = 0.4
# else:
#     podatek = 0.9
#
# print(f"Podatek wynosi {podatek * zarobki}")
# # podatek 0.2 dla przedziału 10000 do 29999


suma_zam = 150

if suma_zam > 100:
    rabacik = 25
else:
    rabacik = 0

print(f"Rabat wynosi {rabacik}")
# Rabat wynosi 25

rabat = 25 if suma_zam > 100 else 0
print(f"Rabat wynosi {rabat}")

# zasymulujemy sytem zbierannia logów
# zmienne beda przechowyc dane, krtóre przyszły z zewnętrznego systemu
# email, console, inny
# dla console : "Stało się coś strasnego"
# dla email: "System email"
# gdy system email to
# dodaj opis błedu i umiesc go w liscie błedów
alert_system = 'email'
error = 'error'
lista_b = []

if alert_system == 'console':
    print('Stało się coś strasznego')
elif alert_system == "email":
    print("System email")
    if error == 'error':
        lista_b.append("Bład krytyczny")
    elif error == 'medium':
        lista_b.append("Ostrzeżenie")
    else:
        print("inny błąd")
else:
    print("Nieznany system")

print(lista_b)
# System email
# ['Bład krytyczny']