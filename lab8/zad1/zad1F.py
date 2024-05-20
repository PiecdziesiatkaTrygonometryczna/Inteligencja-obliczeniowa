import numpy as np
import pygad
import time
# A - słownik najłatwiejszy i mozliwe że najwydajniejszy
items = [
    {"name": "zegar", "value": 100, "weight": 7},
    {"name": "obraz-pejzaż", "value": 300, "weight": 7},
    {"name": "obraz-portret", "value": 200, "weight": 6},
    {"name": "radio", "value": 40, "weight": 2},
    {"name": "laptop", "value": 500, "weight": 5},
    {"name": "lampka nocna", "value": 70, "weight": 6},
    {"name": "srebrne sztućce", "value": 100, "weight": 1},
    {"name": "porcelana", "value": 250, "weight": 3},
    {"name": "figura z brązu", "value": 300, "weight": 10},
    {"name": "skórzana torebka", "value": 280, "weight": 3},
    {"name": "odkurzacz", "value": 300, "weight": 15}
]

# B
max_weight = 25
target_value = 1630

def fitness_func(model, solution, solution_idx):
    fitness = np.sum(solution * [item['value'] for item in items])
    weight = np.sum(solution * [item['weight'] for item in items])
    
    if weight > max_weight:
        return 0  # jeżeli waga przekracza maksymalną wagę, to zerujemy
    else:
        return fitness

fitness_function = fitness_func


#C
#definiujemy parametry chromosomu
#geny to liczby: 0 lub 1
gene_space = [0, 1]


#ile chromsomów w populacji
#ile genow ma chromosom
sol_per_pop = 20
num_genes = len(items)

#ile wylaniamy rodzicow do "rozmanazania" (okolo 50% populacji)
#ile pokolen
#ilu rodzicow zachowac (kilka procent)
num_parents_mating = 10
num_generations = 100
keep_parents = 2

#jaki typ selekcji rodzicow?
#sss = steady, rws=roulette, rank = rankingowa, tournament = turniejowa
parent_selection_type = "sss"

#w il =u punktach robic krzyzowanie?
crossover_type = "single_point"

#mutacja ma dzialac na ilu procent genow?
#trzeba pamietac ile genow ma chromosom
mutation_type = "random"
mutation_percent_genes = 10

def callback_generation(ga_instance):
    if ga_instance.best_solution()[1] >= target_value:
        ga_instance.run_completed = True

ga_instance = pygad.GA(
    gene_space=gene_space,
    num_generations=num_generations,
    num_parents_mating=num_parents_mating,
    fitness_func=fitness_function,
    sol_per_pop=sol_per_pop,
    num_genes=num_genes,
    parent_selection_type=parent_selection_type,
    keep_parents=keep_parents,
    crossover_type=crossover_type,
    mutation_type=mutation_type,
    mutation_percent_genes=mutation_percent_genes,
    on_generation=callback_generation
)

times = []

for _ in range(10):
    start = time.time()
    ga_instance.run()
    end = time.time()
    times.append(end - start)

average_time = np.mean(times)
print(f"Średni czas: {average_time:.4f}")

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

selected_items = [items[i] for i in range(len(solution)) if solution[i] == 1]
selected_names = [item['name'] for item in selected_items]
total_value = sum(item['value'] for item in selected_items)
total_weight = sum(item['weight'] for item in selected_items)

print("Najlepsze przedmioty: ", selected_names)
print("Ich wartość: ", total_value)
print("Waga: ", total_weight)

ga_instance.plot_fitness()

# Średni czas: 0.1776
# Parameters of the best solution : [0. 1. 1. 0. 1. 0. 1. 1. 0. 1. 0.]
# Fitness value of the best solution = 1630.0
# Najlepsze przedmioty:  ['obraz-pejzaż', 'obraz-portret', 'laptop', 'srebrne sztućce', 'porcelana', 'skórzana torebka']
# Ich wartość:  1630
# Waga:  25