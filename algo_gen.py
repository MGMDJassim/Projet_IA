import numpy as np
import random
from ville import Ville

new_pop = []
villes = []

def initailisation_des_villes(nbr_villes):
    for i in range(nbr_villes):
        villes.append(Ville(random.randint(0, 100), random.randint(0, 100)))
    return villes

def initialisation(taille):
    for i in range(taille):
        individu = villes[:]
        random.shuffle(individu)
        new_pop.append(individu)
    return new_pop

def total_distance(route):
    return sum([route[i].distance(route[(i + 1) % len(route)]) for i in range(len(route))])

def evaluation(individus):
    distances = [(i, total_distance(individu)) for i, individu in enumerate(individus)]
    return sorted(distances, key=lambda x: x[1])

def selection(new_pop):
    evaluated = evaluation(new_pop)
    pop_select = [new_pop[evaluated[i][0]] for i in range(len(evaluated) // 2)]
    return pop_select

def recombinaison(parents):
    enfant = []
    for i in range(0, len(parents) - 1, 2):
        parent1 = parents[i]
        parent2 = parents[i + 1]
        cut = len(parent1) // 2
        child1 = parent1[:cut] + [city for city in parent2 if city not in parent1[:cut]]
        child2 = parent2[:cut] + [city for city in parent1 if city not in parent2[:cut]]
        enfant.append(child1)
        enfant.append(child2)
    return enfant

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

def formation(pop, enfant):
    nouvelle_pop = []
    for i in range(len(pop)):
        nouvelle_pop.append(pop[i])
    for i in range(len(enfant)):
        nouvelle_pop.append(enfant[i])
    return nouvelle_pop

def algo_gen(max_iterations=5):
    new_pop = initialisation(10)
    iteration = 0
    while iteration < max_iterations:
        parents = selection(new_pop)
        enfant = recombinaison(parents)
        enfant = mutation(enfant)
        new_pop = formation(new_pop, enfant)
        iteration += 1
initailisation_des_villes(10)


# Test
algo_gen()

"""
Algo : 
new_pop <- ensemble aléatoire d'individus
Répéter :
| Parent <- selection (pop)
| enfant <- recombinaison(parents)
| enfant <- mutation(enfant)
| pop <- Formation (pop, enfant)
tant qu'on améliore la valeur des individus
"""