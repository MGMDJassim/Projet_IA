from matplotlib import pyplot as plt
from algo_gen import *

def plot_data(data):

    x = [city.x for city in data]
    y = [city.y for city in data]
    
    plt.scatter(x, y, c='blue', marker='o')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Villes')
    plt.show()

villes= initailisation_des_villes(10)
plot_data(villes)


# import tkinter as tk
# from tkinter import ttk
# import matplotlib.pyplot as plt

# def afficher_graphique():
#     valeur = float(entree_valeur.get())
#     x = [0, 1]
#     y = [0, valeur]

#     plt.plot(x, y, marker='o')
#     plt.title("Valeur saisie par l'utilisateur")
#     plt.xlabel("Index")
#     plt.ylabel("Valeur")
#     plt.grid(True)
#     plt.show()

# # Créer la fenêtre principale
# fenetre = tk.Tk()
# fenetre.title("Interface Utilisateur")

# # Créer un champ d'entrée pour la valeur
# label_valeur = ttk.Label(fenetre, text="Veuillez entrer une valeur :")
# label_valeur.pack(pady=5)

# entree_valeur = ttk.Entry(fenetre)
# entree_valeur.pack(pady=5)

# # Créer un bouton pour afficher le graphique
# bouton_afficher = ttk.Button(fenetre, text="Afficher le graphique", command=afficher_graphique)
# bouton_afficher.pack(pady=10)

# # Lancer la boucle principale de l'interface utilisateur
# fenetre.mainloop()
