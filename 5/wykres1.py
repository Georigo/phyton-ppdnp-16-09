import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 5, 7, 9, 12]

plt.plot(x, y, color="red")
plt.title("Wykres liniowy")
plt.xlabel("Oś X")
plt.xlabel("Oś Y")

plt.savefig('wykres.png')
plt.savefig('wykres.pdf')
plt.show()
