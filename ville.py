class Ville:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, autre_ville):
        return ((self.x - autre_ville.x)**2 + (self.y - autre_ville.y)**2)**0.5