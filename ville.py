import numpy as np

class Ville:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    

    def distance (self, ville):
        dx = abs(self.x - ville.x)
        dy = abs(self.y - ville.y)
        distance = np.

