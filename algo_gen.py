import numpy as np
import random
from ville import Ville

new_pop = []
villes = []
# Initialisation des villes
def initailisation_des_villes(nbr_villes):
    for i in range(nbr_villes):
        villes.append(Ville(random.randint(0, 100), random.randint(0, 100)))
    return villes

# Initialisation de la population
def initialisation(taille):
    for i in range(taille):
        individu = villes[:]
        random.shuffle(individu)
        new_pop.append(individu)
    return new_pop

# Calcul de la distance totale
def total_distance(route):
    return sum([route[i].distance(route[(i + 1) % len(route)]) for i in range(len(route))])

# Evaluation de la population
def evaluation(individus):
    distances = [(i, total_distance(individu)) for i, individu in enumerate(individus)]
    return sorted(distances, key=lambda x: x[1])

# Selection des individus
def selection(new_pop):
    evaluated = evaluation(new_pop)
    pop_select = [new_pop[evaluated[i][0]] for i in range(len(evaluated) // 2)]
    return pop_select

# Recombinaison des parents
def recombinasion(parents):
    enfant = []
    for i in range(len(parents)):
        parent1 = parents[i]
        parent2 = parents[(i + 1) % len(parents)]
        start = random.randint(0, len(parent1) - 1)
        end = random.randint(0, len(parent1) - 1)
        if start > end:
            start, end = end, start
        enfant.append(parent1[start:end])
        for ville in parent2:
            if ville not in enfant[i]:
                enfant[i].append(ville)
    return enfant

# Mutation
def mutation(enfant):
    mutation_rate = 0.05  
    for swapped in range(len(enfant)):
        if random.random() < mutation_rate:
            swap_with = int(random.random() * len(enfant))
            city1 = enfant[swapped]
            city2 = enfant[swap_with]
            enfant[swapped] = city2
            enfant[swap_with] = city1
    return enfant 


# Formation de la nouvelle population
def formation(pop, enfant):
    nouvelle_pop = []
    for i in range(len(pop)):
        nouvelle_pop.append(pop[i])
    for i in range(len(enfant)):
        nouvelle_pop.append(enfant[i])
    return nouvelle_pop

# Algorithme génétique
def algo_gen():
    new_pop = initialisation()
    while True:
        parents = selection(new_pop)
        enfant = recombinasion(parents)
        enfant = mutation(enfant)
        pop = formation(new_pop, enfant)


# Test
initailisation_des_villes(10)
new_pop = initialisation(10)

"""
Algo : 
new_pop <- ensemble aléatoire d'individus
Répéter :
| Parent <- selection (pop)
| enfant <- recombinasion(parents)
| enfant <- mutation(enfant)
| pop <- Formation (pop, enfant)
tant qu'on améliore la valeur des individus
"""