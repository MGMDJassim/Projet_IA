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
    pop_selct = [new_pop[evaluated[i][0]] for i in range(len(evaluated) // 2)]
    
    print("Population sélectionnée :")
    for pop in pop_selct:
        print(f"Évaluation = {total_distance(pop)}")
        for ville in pop:
            print(ville)
        print()
    
    return pop_selct

def recombinasion(parents):
    pass

def mutation(enfant):
    mutation_rate = 0.01  # Taux de mutation
    # Itère sur chaque ville dans l'itinéraire
    for swapped in range(len(enfant)):
        # Vérifie si une mutation doit se produire, basé sur le taux de mutation
        if random.random() < mutation_rate:
            # Sélectionne une deuxième ville aléatoire dans l'itinéraire pour l'échange
            swap_with = int(random.random() * len(enfant))
            # Échange les deux villes
            city1 = enfant[swapped]
            city2 = enfant[swap_with]
            enfant[swapped] = city2
            enfant[swap_with] = city1
    return enfant  # Retourne l'itinéraire muté

def formation(pop, enfant):
    pass

def algo_gen():
    new_pop = initialisation()
    while True:
        parents = selection(new_pop)
        enfant = recombinasion(parents)
        enfant = mutation(enfant)
        pop = formation(pop, enfant)

taille = 10

initailisation_des_villes(taille)

initialisation(taille)

print("\nFitness de chaque individu dans la population :")
for i, individu in enumerate(new_pop):
    print(f"Individu {i + 1} : Fitness = {total_distance(individu)}")
    for ville in individu:
        print(ville)
    print()

# Test de la fonction selection
selection(new_pop)

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