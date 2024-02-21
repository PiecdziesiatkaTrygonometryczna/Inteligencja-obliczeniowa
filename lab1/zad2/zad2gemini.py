# gemini zwrócił najlepsze rozwiązanie, jakie udało mi się wygenerować.
# i tak wiele brakuje do prawidłowego rozwiązania.
# żaden z botów nie jest w stanie zrozumieć, że 
# pocisk ma lądować, gdy y=0, a nie, gdy y=100, tak jak katapulta.
# nawet, jeżeli wkleję im prawidłowy wzór.


import random
import math
import matplotlib.pyplot as plt
import numpy as np

# Ustawienia początkowe
v0 = 50  # m/s
h = 100  # m
margines_bledu = 5  # m

# Przyspieszenie ziemskie
g = 9.81  # m/s^2

# Funkcja obliczająca odległość pocisku
def oblicz_odleglosc(kat):
    theta = kat * math.pi / 180
    t_lot = 2 * v0 * math.sin(theta) / (g * math.cos(theta))
    xmax = v0 * t_lot * math.cos(theta)
    return xmax

# Funkcja obliczająca wysokość pocisku
def oblicz_wysokosc(kat, x, t_lot):
    theta = kat * math.pi / 180
    y = h + v0 * t_lot * x / xmax * math.sin(theta) - 0.5 * 9.81 * (t_lot * x / xmax)**2
    return y - h  # Odejmij wysokość początkową (h)

# Funkcja wyświetlająca informację o trafieniu
def wyswietl_trafienie(odleglosc, cel):
    if cel - margines_bledu <= odleglosc <= cel + margines_bledu:
        print("Cel trafiony!")
    else:
        print(f"Pomyłka! Pocisk uderzył {odleglosc - cel:.2f} metrów od celu.")
cel = random.randint(50, 340)
print(f"Cel znajduje się w odległości {cel} metrów.")
# Główny program
while True:
    # Losowy cel


    # Kąt strzału
    kat = float(input("Podaj kąt strzału (w stopniach): "))

    # Obliczenie odległości pocisku
    odleglosc = oblicz_odleglosc(kat)
    theta = kat * math.pi / 180

    # Trafienie w cel?
    wyswietl_trafienie(odleglosc, cel)

    # Rysowanie trajektorii
    t_lot = 2 * v0 * math.sin(theta) / (g * math.cos(theta))
    xmax = oblicz_odleglosc(kat)
    x = np.linspace(0, xmax, 100)

    # Lista wysokości
    y = []
    for i in range(len(x)):
        y.append(oblicz_wysokosc(kat, x[i], t_lot))

    plt.plot(x, y, color="blue")
    plt.xlabel("Odległość (m)")
    plt.ylabel("Wysokość (m)")
    plt.title("Trajektoria pocisku")
    plt.grid()

    # Wyświetlanie maksymalnej wysokości
    ymax = h + v0**2 * math.sin(theta)**2 / (2 * 9.81)
    print(f"Maksymalna wysokość: {ymax:.2f} m")

    # Dodanie punktu uderzenia
    plt.scatter(odleglosc, 0, color="red", marker="x")

    plt.savefig("trajektoria_gemini.png")
