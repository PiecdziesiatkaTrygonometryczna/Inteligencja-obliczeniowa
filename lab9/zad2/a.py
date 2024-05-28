import matplotlib.pyplot as plt
import random

from aco import AntColony


plt.style.use("dark_background")


COORDS = (
(20, 52), (43, 50), (20, 84), (70, 65), (29, 90), (87, 83),
(73, 23), (42, 43), (33, 67), (74, 17), (100, 65), (43, 85),
(79, 14), (81, 43), (7, 9), (98, 91), (65, 73), (37, 40), (48, 40),
(98, 45), (45, 81), (43, 11), (3, 91), (81, 78), (35, 40), (59, 23),
(70, 13), (86, 81), (30, 59), (42, 41)
)


def random_coord():
    r = random.randint(0, len(COORDS))
    return r


def plot_nodes(w=12, h=8):
    for x, y in COORDS:
        plt.plot(x, y, "g.", markersize=15)
    plt.axis("off")
    fig = plt.gcf()
    fig.set_size_inches([w, h])


def plot_all_edges():
    paths = ((a, b) for a in COORDS for b in COORDS)

    for a, b in paths:
        plt.plot((a[0], b[0]), (a[1], b[1]))


plot_nodes()

colony = AntColony(COORDS, ant_count=300, alpha=0.5, beta=5, 
                    pheromone_evaporation_rate=0.40, pheromone_constant=1000.0,
                    iterations=30)

optimal_nodes = colony.get_path()

for i in range(len(optimal_nodes) - 1):
    plt.plot(
        (optimal_nodes[i][0], optimal_nodes[i + 1][0]),
        (optimal_nodes[i][1], optimal_nodes[i + 1][1]),
    )


plt.show()

# liczba wierzcholkow zdecydowanie wydluza czas kazdej iteracji.

# zmniejszenie liczby mrowek znacznie przyspiesza znajdywanie rozwiazania,
# kosztem dokładności

# siła feromonów nie ma wpływu na szybkość rozwiązania, ale wtedy
# mrówki są mniej skłonne do szukania własnych ścieżek, tylko szybko
# zaczynają podążać za innymi

# beta, czyli wpływ długości odcinka na decyzje mrówek, również nie mają
# wpływu na szybkość rozwiązania, ale powoduje to znaczne ograniczenie 
# wyboru niektórych ścieżek

# evaporation rate oraz pheromone constant mają wpływ na wybór ścieżek
# przez mrówki, ale nie mają wpływu na czas działania algorytmu

# ilość iteracji oczywiście liniowo wydłuża czas działania algorytmu