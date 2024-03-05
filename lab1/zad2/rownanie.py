import math

# Podaj wartości
v0 = 10  # prędkość początkowa
alpha = math.radians(45)  # kąt w radianach
g = 9.8  # stała grawitacji
h = 5    # wysokość

# Obliczanie odległości za pomocą podanego wzoru
odleglosc = ((v0 * math.sin(alpha)) + 
            math.sqrt((v0 * math.sin(alpha))**2 + 2*g*h)) * (v0 * math.cos(alpha)) / g

print("Odległość:", odleglosc)



