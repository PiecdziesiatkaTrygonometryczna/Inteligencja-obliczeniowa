# chatgpt 3.5

# wkleiłem mu całe polecenie, i wytłumaczyłem mu też, że h=100 oznacza, że katapulta
# znajduje się na wysokości 100m, pocisk leci do góry, osiąga maksimum,
# po czym opada, mija wartość 100, i ląduje dopiero, gdy y=0.
# wytlumaczyłem mu to, bo gdy wcześniej pytałem go o wzory,
# to myślał, że w zadaniu chodzi o to, aby policzyć,
# dla jakiego x wysokość pocisku osiągnie 100m.

# oczywiście, mimo wytlumaczenia, na początku zrobił, że pocisk ląduje
# na wysokości 100m. zwrocilem mu na to uwagę, to zrobił wysokość (-100, 0).
# wytlumaczylem mu jeszcze raz, prostym językiem. dalej pocisk ląduje na tej samej wysokości,
# z której startuje. poza tym zauważyłem, że niezależnie jaki kąt wpiszemy,
# trajektoria pocisku to zawsze ten sam kąt, wizualnie wygląda to na 45 stopni.

# bazowo nie zawarl pytania uzytkownika o kąt w pętli while, mimo że było tak
# w poleceniu, ale gdybym mu o tym przypomniał, na pewno by to poprawił

# mimo zwrocenia wielokrotnie uwagi, nie wie, jak prawidlowo policzyc trajektorie.
# po prostu uzywa złych wzorów.


import random
import math
import numpy as np
import matplotlib.pyplot as plt

def oblicz_odleglosc(v0, h, alpha):
    alpha_rad = math.radians(alpha)
    d = (v0 ** 2 * math.sin(2 * alpha_rad)) / 9.81
    return d

def trajektoria(v0, h, alpha):
    alpha_rad = np.radians(alpha)
    x_ground = (v0 ** 2 * np.sin(2 * alpha_rad)) / 9.81  # zasięg lotu

    t = np.linspace(0, x_ground / (v0 * np.cos(alpha_rad)), num=1000)
    x = v0 * np.cos(alpha_rad) * t
    y = h + (v0 * np.sin(alpha_rad) * t) - (0.5 * 9.81 * t ** 2)
    return x, y

# Losowy wybór celu w zakresie od 50 do 340 metrów
cel = random.randint(50, 340)
print("Cel do zniszczenia znajduje się w odległości:", cel, "metrów")

# Wartości początkowe
v0 = 50  # m/s
h = -100  # m

# Pobranie kąta strzału od użytkownika
alpha = float(input("Podaj kąt strzału w stopniach: "))

# Obliczenie odległości, na którą pocisk doleci
odleglosc = oblicz_odleglosc(v0, h, alpha)
print("Pocisk doleci na odległość:", odleglosc, "metrów")

# Rysowanie trajektorii pocisku
x, y = trajektoria(v0, h, alpha)
plt.plot(x, y, color='blue')
plt.grid(True)
plt.xlabel('Odległość (m)')
plt.ylabel('Wysokość (m)')
plt.title('Trajektoria pocisku Warwolf')
plt.savefig('trajektoria_chatgpt.png')
plt.show()
