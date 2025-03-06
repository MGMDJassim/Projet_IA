import random
from ville import Ville

villes = []

def initialisation_des_villes(nbr_villes):
    """ Initialise une liste de villes avec des coordonnées aléatoires. """
    global villes
    villes = [Ville(random.randint(0, 100), random.randint(0, 100)) for _ in range(nbr_villes)]

def initialisation(taille):
    """ Génère une population initiale de chemins (permutations de villes). """
    return [random.sample(villes, len(villes)) for _ in range(taille)]  # Copie aléatoire

def calculer_distance(individu):
    """ Calcule la distance totale parcourue dans un itinéraire. """
    return sum(individu[i].distance(individu[i + 1]) for i in range(len(individu) - 1))

def selection(population):
    """ Trie et sélectionne la meilleure moitié de la population. """
    population.sort(key=calculer_distance)
    return population[:max(len(population)//2, 2)]  # Minimum 2 individus pour éviter l'extinction

def recombinaison(parent1, parent2):
    """ Crossover partiel : prend un segment du premier parent et complète avec le second. """
    point = random.randint(1, len(parent1) - 2)
    enfant = parent1[:point] + [ville for ville in parent2 if ville not in parent1[:point]]
    
    if len(enfant) != len(villes):  # Vérification de la taille de l'enfant
        raise ValueError("Erreur dans la recombinaison : enfant incomplet.")
    
    return enfant

def mutation(enfant, taux_mutation=0.05):
    """ Applique une mutation par échange de deux villes. """
    if random.random() < taux_mutation:
        i, j = random.sample(range(len(enfant)), 2)
        enfant[i], enfant[j] = enfant[j], enfant[i]
    return enfant

def formation(population, enfants):
    """ Fusionne parents et enfants, trie et conserve la moitié la plus performante. """
    population.extend(enfants)
    population.sort(key=calculer_distance)
    return population[:max(len(population)//2, 10)]  # Minimum 10 individus pour éviter l'extinction

def algo_gen(taille_population, generations):
    """ Algorithme génétique principal. """
    population = initialisation(taille_population)
        
    if not population:
        raise RuntimeError("Erreur : la population initiale est vide !")

    # Affichage du meilleur itinéraire de la première génération
    afficher_meilleur_itineraire(population, "première génération")

    for generation in range(generations):
        parents = selection(population)

        if len(parents) < 2:  # Vérification pour éviter l'extinction
            print(f"Arrêt à la génération {generation}: Trop peu d'individus pour continuer.")
            break

        enfants = []
        for i in range(0, len(parents) - 1, 2):
            enfant = recombinaison(parents[i], parents[i+1])
            enfant = mutation(enfant)
            enfants.append(enfant)

        population = formation(population, enfants)

    # Affichage du meilleur itinéraire de la dernière génération
    afficher_meilleur_itineraire(population, "dernière génération")

    return population

def afficher_meilleur_itineraire(population, etape):
    """ Affiche le meilleur itinéraire de la population donnée. """
    if not population:
        print(f"Erreur : la population {etape} est vide.")
        return
    
    # Trier la population en fonction de la distance
    population_triee = sorted(population, key=calculer_distance)

    # Affichage du meilleur itinéraire
    meilleur_individu = population_triee[0]
    print(f"\n=== Meilleur itinéraire {etape} ===")

    print(f"Distance du meilleur itinéraire {etape} :", calculer_distance(meilleur_individu))

# Lancement de l'algorithme
taille = 28
initialisation_des_villes(taille)

# Exécution de l'algorithme génétique
population_finale = algo_gen(100, 6)