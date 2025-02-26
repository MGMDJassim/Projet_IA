import random
from Individu import Individu
new_pop = []


def initialisation(taille):
    for _ in range(taille):
        new_pop.append(Individu(random.randint(0, 100), random.randint(0, 100)))
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

initialisation(10)

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