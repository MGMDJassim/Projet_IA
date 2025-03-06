import numpy as np

class Ville:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def distance(self, other):
        return np.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)