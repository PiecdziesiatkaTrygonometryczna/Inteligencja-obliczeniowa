import random

COORDS = (
    (20, 52),
    (43, 50),
    (20, 84),
    (70, 65),
    (29, 90),
    (87, 83),
    (73, 23),
)

def generate_additional_vertices(coords, num_vertices=30, x_range=(0, 100), y_range=(0, 100)):
    vertices = list(coords)
    while len(vertices) < num_vertices:
        x = random.randint(x_range[0], x_range[1])
        y = random.randint(y_range[0], y_range[1])
        vertices.append((x, y))
    return vertices

vertices = generate_additional_vertices(COORDS, 30)

for vertex in vertices:
    print(f"({vertex[0]}, {vertex[1]})", end=', ')
