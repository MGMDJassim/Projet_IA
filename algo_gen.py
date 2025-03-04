import random
from ville import Ville
new_pop = []
villes = []

def initailisation_des_villes(nbr_villes):
    for i in range(nbr_villes):
        villes.append(Ville(random.randint(0, 100), random.randint(0, 100)))
    return villes

def initialisation(taille, start, end):
    for i in range(taille):
        individu = villes[:]
        random.shuffle(individu)
        individu.insert(0, start)  # Ajouter le point de départ au début
        individu.append(end)       # Ajouter la destination à la fin
        new_pop.append(individu)
    return new_pop

def selection(new_pop):
    pass

def recombinasion(parent):
    pass

def mutation(enfant):
    pass

def formation(pop, enfant):
    pass


def algo_gen():
    new_pop = initialisation()
    while True:
        parent = selection(new_pop)
        enfant = recombinasion(parent)
        enfant = mutation(enfant)
        pop = formation(pop, enfant)

taille = 10

initailisation_des_villes(taille)

point_de_depart = Ville(0, 0)
destination = Ville(100, 100)
initialisation(taille, point_de_depart, destination)

print(villes)

for i, individu in enumerate(new_pop):
    print(f"Individu {i + 1}:")
    for ville in individu:
        print(ville)
    print()  # L
"""
Algo : 
new_pop <- ensemble aléatoie d'individus
Répéter :
| Parent <- selction (pop)
| enfant <- selection(parents)
| enfant <- mutation(enfant)
| pop <- Formation (pop, enfant)
tant qu'on améliore la valeur des individus

"""