import math
import numpy as np
import pygad
import matplotlib.pyplot as plt

def endurance(x, y, z, u, v, w):
 return math.exp(-2*(y-math.sin(x))**2)+math.sin(z*u)+math.cos(v*w)


gene_space = [(0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1)]

def fitness_func(model, solution, solution_idx):
    x, y, z, u, v, w = solution
    return endurance(x, y, z, u, v, w)

num_generations = 50
num_parents_mating = 4
mutation_percent_genes = 17
sol_per_pop = 10
num_genes = 6

initial_population = np.random.rand(sol_per_pop, num_genes)

# print("initial: ", initial_population)

ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_func,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       gene_type=float,
                       gene_space=gene_space,
                       initial_population=initial_population,
                       mutation_percent_genes=mutation_percent_genes)

ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : ", solution)
print("Fitness value of the best solution =", solution_fitness)

fitness_values = ga_instance.best_solutions_fitness
plt.plot(fitness_values)
plt.xlabel('Generacja')
plt.ylabel('Fitness')
plt.grid()
plt.savefig("plot2.png")