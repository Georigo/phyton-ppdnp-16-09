# od Pythona 3.10
# match case

lista = []
lang = input("Podaj znany Ci język programowania")

match lang.lower().strip():
    case "python":
        lista.append("Znam Pythona")
    case "java":
        lista.append("Jave też znam")
    case _:  # wartość, działąnie domyślne (odpowiednik else)
        print("Nie znam takiego języka")

print(lista)

match lang:
    case ("python" | "python3"):  # | oznacza or czyli lub,
        print("Znam Pythona")

# Podaj znany Ci język programowaniapython
# ['Znam Pythona']
# Znam Pythona
