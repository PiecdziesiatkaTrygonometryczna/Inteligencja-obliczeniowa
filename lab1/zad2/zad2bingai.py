#bing poradzil sobie podobnie jak chatgpt, czyli nie za bardzo

import math
import random
import matplotlib.pyplot as plt

# Stałe
v0 = 50  # początkowa prędkość w m/s
h = 100  # wysokość trebusza w metrach
g = 9.81  # przyspieszenie ziemskie w m/s^2

def oblicz_odleglosc(alpha):
    # Przeliczamy kąt na radiany
    alpha_rad = math.radians(alpha)
    
    # Obliczamy odległość
    d = ((v0 ** 2) / g) * math.sin(2 * alpha_rad)
    
    return d


# Wybieramy cel
cel = random.randint(50, 340)
print(f"Cel znajduje się w odległości {cel} metrów.")

# Pętla strzałów
liczba_prob = 0
while True:
    # Pytamy użytkownika o kąt
    alpha = float(input("Podaj kąt strzału (w stopniach): "))
    
    # Obliczamy odległość
    d = oblicz_odleglosc(alpha)
    
    # Zwiększamy liczbę prób
    liczba_prob += 1
    
    # Sprawdzamy, czy trafiliśmy
    if abs(d - cel) <= 5:
        print(f"Cel trafiony! Liczba prób: {liczba_prob}")
        break
    else:
        print(f"Pocisk upadł {d} metrów od trebusza.")

def rysuj_trajektorie(alpha):
    # Przeliczamy kąt na radiany
    alpha_rad = math.radians(alpha)
    
    # Obliczamy czas lotu
    t_max = (2 * v0 * math.sin(alpha_rad)) / g
    
    # Generujemy punkty czasu
    t = [i * 0.01 for i in range(int(t_max * 100))]
    
    # Obliczamy trajektorię
    x = [v0 * i * math.cos(alpha_rad) for i in t]
    y = [h + v0 * i * math.sin(alpha_rad) - 0.5 * g * i ** 2 for i in t]
    
    # Rysujemy wykres
    plt.figure(figsize=(10, 5))
    plt.plot(x, y)
    plt.grid(True)
    plt.title("Trajektoria pocisku")
    plt.xlabel("Odległość [m]")
    plt.ylabel("Wysokość [m]")
    plt.savefig("trajektoria_bingai.png")

# Rysujemy trajektorię pocisku, który trafił w cel
rysuj_trajektorie(alpha)
