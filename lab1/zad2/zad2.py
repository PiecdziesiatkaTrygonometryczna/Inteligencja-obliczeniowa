# z mojego doświadczenia, spośród ChataGPT 3.5, Google Barda, oraz BingAI najlepiej z matematyką radzi sobie BingAI.

# w tym przypadku, próbowałem różnych promptów: wklejając  polecenie, tłumaczyć co mam dane, jaka jest sytuacja, i co chcę policzyć,
# lecz żaden z powyższych modeli językowych nie podał mi wzoru, ani tym bardziej jego implementacji w pythonie, która zwracałaby
# prawidłowy wynik. 

# więc w tym momencie dałem Bingowi zdjęcie ostatniego wzoru z pdfa zadania, i spytałem, jak ten wzór wyglądałby w Pythonie.
# tutaj odziwo poradził sobie doskonale, jego odpowiedź jest w pliku rownanie.py, oraz trajektoria.py


import random
import math
import matplotlib.pyplot as plt
import numpy as np


targetPosition = random.randint(50, 340)

print(targetPosition)

triesCount = 0

def hit(angle):
    # Podaj wartości
    v0 = 50  # prędkość początkowa
    alpha = math.radians(angle)  # kąt w radianach
    g = 9.8  # stała grawitacji
    h = 100    # wysokość


    odleglosc = ((v0 * math.sin(alpha)) + 
                math.sqrt((v0 * math.sin(alpha))**2 + 2*g*h)) * (v0 * math.cos(alpha)) / g

    print("Odległość:", odleglosc)
    return odleglosc

while True:
    print("Podaj kąt: ", end='')
    userAngle = int(input())
    hitSpot = hit(userAngle)
    triesCount += 1
    if hitSpot < targetPosition + 5 and hitSpot > targetPosition - 5:
        print("Trafiłeś! Łączna liczba strzałów: " + str(triesCount))
        break
    else:
        print("Nie trafiłeś. Spróbuj ponownie.")


# -------
# ---3---
# -------
        
# Podaj wartości
g = 9.8  # przykładowa wartość dla g
v0 = 50   # przykładowa wartość dla v0
alpha = math.radians(userAngle)  # konwersja stopni na radiany, przykładowa wartość dla alpha
h = 100   # przykładowa wartość dla h

# Obliczanie y na podstawie podanego równania
xArray = np.arange(hitSpot + 1).tolist()
yArray = []
for x in xArray:
    y = (-g / (2 * v0**2 * math.cos(alpha)**2)) * x**2 + (math.sin(alpha) / math.cos(alpha)) * x + h
    yArray.append(y)


xpoints = np.array([0, 340])
ypoints = np.array([0, 170])
plt.title("Trajektoria pocisku")
plt.xlabel("Odległość (m)")
plt.ylabel("Wysokość (m)")

plt.plot(xArray, yArray)
plt.grid(True)
plt.show()
plt.savefig('trajektoria.png')








