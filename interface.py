from matplotlib import pyplot as plt
from algo_gen import *

def plot_data(data):

    x = [city.x for city in data]
    y = [city.y for city in data]
    
    plt.scatter(x, y, c='blue', marker='o')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Cities')
    plt.show()

plot_data(villes)