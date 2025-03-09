import numpy as np
import random
from ville import Ville

new_pop = []
villes = []

def initialisation_des_villes(nbr_villes):
    global villes
    villes = [Ville(random.randint(0, 50), random.randint(0, 50)) for _ in range(nbr_villes)]
    return villes

def initialisation(taille):
    return [random.sample(villes, len(villes)) for _ in range(taille)]

def total_distance(route):
    return sum(route[i].distance(route[i + 1]) for i in range(len(route) - 1)) + route[-1].distance(route[0])

def evaluation(individus):
    return sorted(individus, key=total_distance)

def selection(pop):
    return evaluation(pop)[:len(pop) // 2]

def recombinaison(parents):
    enfant = []
    for i in range(0, len(parents) - 1, 2):
        parent1, parent2 = parents[i], parents[i + 1]
        cut = len(parent1) // 2
        child1 = parent1[:cut] + [city for city in parent2 if city not in parent1[:cut]]
        child2 = parent2[:cut] + [city for city in parent1 if city not in parent2[:cut]]
        enfant.extend([child1, child2])
    return enfant

def mutation(enfant, mutation_rate=0.05):
    for route in enfant:
        if random.random() < mutation_rate:
            i, j = random.sample(range(len(route)), 2)
            route[i], route[j] = route[j], route[i]
    return enfant

def formation(pop, enfant):
    nouvelle_pop = enfant + pop[:len(pop)//2]  # Garde une partie des anciens
    random.shuffle(nouvelle_pop)
    return nouvelle_pop[:len(pop)]