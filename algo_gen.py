import numpy as no
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

def evaluation(individu):
    distance = 0
    for i in range(len(individu) - 1):
        distance += individu[i].distance(individu[i + 1])
    return distance
    
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

taille = 8

initailisation_des_villes(taille)

initialisation(taille)


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