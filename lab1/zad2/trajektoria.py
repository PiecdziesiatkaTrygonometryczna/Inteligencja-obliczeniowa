import math

# Podaj wartości
g = 9.8  # przykładowa wartość dla g
v0 = 50   # przykładowa wartość dla v0
alpha = math.radians(45)  # konwersja stopni na radiany, przykładowa wartość dla alpha
x = 0    # przykładowa wartość dla x
h = 100   # przykładowa wartość dla h

# Obliczanie y na podstawie podanego równania
y = (-g / (2 * v0**2 * math.cos(alpha)**2)) * x**2 + (math.sin(alpha) / math.cos(alpha)) * x + h

print(y)
