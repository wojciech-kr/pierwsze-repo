import matplotlib.pyplot as plt
 
wyniki = [4.5, 3.0, 5.0, 4.0, 3.5]
 
plt.hist(wyniki, bins=5)
plt.title("Rozkład ocen")
plt.xlabel("Ocena")
plt.ylabel("Liczba studentów")
plt.savefig("rozklad_ocen.png")
