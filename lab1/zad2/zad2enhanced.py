# uzylem chatgpt 3.5

# wysłałem mu poprzedni program, i nakazałem go "ulepszyć"
# co zmienił? wartości używane kilkukrotnie, zdefiniował  na początku
# skryptu. pozmieniał nazwy na, według niego, czytelniejsze, i ogólnie formatowanie.
# do funckji hit przekazał dane jako argumenty, zamiast, tak jak
# zrobiłem ja, definiować je w funkcji.


import math
import matplotlib.pyplot as plt
import numpy as np

# Stałe
PRZYSPIESZENIE_GRAWITACYJNE = 9.8
PREDKOSC_POCZATKOWA = 50
WYSOKOSC = 100

def hit(angle, v0, g, h):
    alpha = math.radians(angle)  # Konwersja stopni na radiany

    # Obliczenie odległości
    odleglosc = ((v0 * math.sin(alpha)) + 
                math.sqrt((v0 * math.sin(alpha))**2 + 2 * g * h)) * (v0 * math.cos(alpha)) / g

    print("Odległość:", odleglosc)
    return odleglosc

targetPosition = np.random.randint(50, 340)
print(targetPosition)

triesCount = 0

while True:
    print("Podaj kąt: ", end='')
    userAngle = int(input())
    hitSpot = hit(userAngle, PREDKOSC_POCZATKOWA, PRZYSPIESZENIE_GRAWITACYJNE, WYSOKOSC)
    triesCount += 1
    if targetPosition - 5 < hitSpot < targetPosition + 5:
        print(f"Trafiłeś! Łączna liczba strzałów: {triesCount}")
        break
    else:
        print("Nie trafiłeś. Spróbuj ponownie.")

# Obliczanie trajektorii
xArray = np.arange(hitSpot + 1)
yArray = (-PRZYSPIESZENIE_GRAWITACYJNE / (2 * PREDKOSC_POCZATKOWA**2 * math.cos(math.radians(userAngle))**2)) * xArray**2 + (math.sin(math.radians(userAngle)) / math.cos(math.radians(userAngle))) * xArray + WYSOKOSC

# Rysowanie trajektorii
plt.plot(xArray, yArray)
plt.title("Trajektoria pocisku")
plt.xlabel("Odległość (m)")
plt.ylabel("Wysokość (m)")
plt.grid(True)
plt.savefig('plot.png')
plt.show()
