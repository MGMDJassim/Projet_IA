import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QGraphicsView, QGraphicsScene, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QBrush
from algo_gen import initialisation_des_villes, total_distance, selection, recombinaison, mutation, formation

class GraphicsView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

    def draw_path(self, individu):
        self.scene.clear()
        pen = QPen(Qt.blue, 2)
        brush = QBrush(Qt.red)

        coords = [(ville.x * 10, ville.y * 10) for ville in individu]
        for x, y in coords:
            self.scene.addEllipse(x-5, y-5, 10, 10, pen, brush)
        for i in range(len(coords) - 1):
            self.scene.addLine(coords[i][0], coords[i][1], coords[i+1][0], coords[i+1][1], pen)
        self.scene.addLine(coords[-1][0], coords[-1][1], coords[0][0], coords[0][1], pen)

class GeneticAlgorithmGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Évolution des Itinéraires")
        self.setGeometry(300, 300, 1080, 720)
        
        main_layout = QVBoxLayout()

        # Zone de saisie
        input_layout = QHBoxLayout()
        self.entry_villes = QLineEdit(self)
        self.entry_population = QLineEdit(self)
        self.start_button = QPushButton("Démarrer", self)
        self.start_button.clicked.connect(self.run_algorithm)
        
        input_layout.addWidget(QLabel("Nombre de villes:"))
        input_layout.addWidget(self.entry_villes)
        input_layout.addWidget(QLabel("Taille de la population:"))
        input_layout.addWidget(self.entry_population)
        input_layout.addWidget(self.start_button)
        
        main_layout.addLayout(input_layout)

        # Zone d'affichage
        self.graphics_view = GraphicsView(self)
        main_layout.addWidget(self.graphics_view)

        self.setLayout(main_layout)
        self.villes = []
        self.population = None
        self.generation = 0

    def update_generation(self):
        if self.generation < 100:
            parents = selection(self.population)
            enfants = recombinaison(parents)
            enfants = mutation(enfants)
            self.population = formation(self.population, enfants)
            
            best_individu = min(self.population, key=total_distance)
            self.graphics_view.draw_path(best_individu)
            self.generation += 1
            QTimer.singleShot(500, self.update_generation)
        else:
            QMessageBox.information(self, "Fin", "L'algorithme a terminé son exécution.")

    def run_algorithm(self):
        try:
            num_villes = int(self.entry_villes.text())
            taille_population = int(self.entry_population.text())
        except ValueError:
            QMessageBox.critical(self, "Erreur", "Veuillez entrer des valeurs numériques valides.")
            return
        
        self.villes = initialisation_des_villes(num_villes)
        self.population = [random.sample(self.villes, len(self.villes)) for _ in range(taille_population)]
        self.generation = 0
        self.update_generation()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GeneticAlgorithmGUI()
    window.show()
    sys.exit(app.exec_())