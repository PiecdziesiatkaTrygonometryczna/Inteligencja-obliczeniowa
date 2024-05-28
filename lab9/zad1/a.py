import math
import pyswarms as ps
import numpy as np
from pyswarms.utils.plotters import plot_cost_history
import matplotlib.pyplot as plt

def endurance(params):
    x, y, z, u, v, w = params
    return math.exp(-2 * (y - math.sin(x)) ** 2) + math.sin(z * u) + math.cos(v * w)

def fitness_function(x):
    n_particles = x.shape[0]
    j = [endurance(x[i]) for i in range(n_particles)]
    return -np.array(j)

options = {'c1': 0.5, 'c2': 0.8, 'w': 0.9}
bounds = (np.zeros(6), np.ones(6))

optimizer = ps.single.GlobalBestPSO(n_particles=30, dimensions=6, options=options, bounds=bounds)

cost, pos = optimizer.optimize(fitness_function, iters=1000)

print("Najlepsza wytrzymałość (endurance):", -cost)
print("Najlepsze rozwiązanie (proporcje metali):", pos)


plot_cost_history(optimizer.cost_history)
plt.title('Koszt vs generacja')
plt.xlabel('Generacja')
plt.ylabel('Koszt')
plt.savefig("koszt.png")


# d@ubuntu:/media/d/dvol/code/Inteligencja-obliczeniowa/lab9/zad1$ python3 zad1.py 
# 2024-05-27 21:15:06,336 - pyswarms.single.global_best - INFO - Optimize for 1000 iters with {'c1': 0.5, 'c2': 0.8, 'w': 0.9}
# pyswarms.single.global_best: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████|1000/1000, best_cost=-2.82
# 2024-05-27 21:15:06,598 - pyswarms.single.global_best - INFO - Optimization finished | best cost: -2.8184631544467207, best pos: [0.681437   0.70473654 0.98068224 0.99944929 0.29932351 0.14774992]
# Najlepsza wytrzymałość (endurance): 2.8184631544467207
# Najlepsze rozwiązanie (proporcje metali): [0.681437   0.70473654 0.98068224 0.99944929 0.29932351 0.14774992]
# d@ubuntu:/media/d/dvol/code/Inteligencja-obliczeniowa/lab9/zad1$ 
