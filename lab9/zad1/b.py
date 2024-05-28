import math
import pyswarms as ps
import numpy as np


def endurance(params):
    x, y, z, u, v, w = params
    return math.exp(-2 * (y - math.sin(x)) ** 2) + math.sin(z * u) + math.cos(v * w)


def fitness_function(x):
    n_particles = x.shape[0]
    j = [endurance(x[i]) for i in range(n_particles)]
    return -np.array(j)


options = {'c1': 0.5, 'c2': 0.8, 'w': 0.9}
bounds = (np.ones(6), np.full(6, 2))

optimizer = ps.single.GlobalBestPSO(n_particles=30, dimensions=6, options=options, bounds=bounds)

cost, pos = optimizer.optimize(fitness_function, iters=1000)

print("Najlepsza wytrzymałość (endurance):", -cost)
print("Najlepsze rozwiązanie (proporcje metali):", pos)
