import statistics
 
wyniki = [4.5, 3.0, 5.0, 4.0, 3.5]
 
print("Liczba ocen:", len(wyniki))
print("Średnia:", statistics.mean(wyniki))

max_wynik = max(wyniki)

print(max_wynik)

print("Mediana:", statistics.median(wyniki))