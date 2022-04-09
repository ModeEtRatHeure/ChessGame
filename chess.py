from board import Board
from pieces import *

class Chess:
    def __init__(self):
        self.board = Board()
        self.is_running = True
        self.player = "Joueur 1"
        self.is_chess = False
        self.color_tour = "w"
        self.tour = ""

    def castle(self):
        """Roque"""
        pass

    def eat(self):
        """Mange une pièce"""
        pass

    def move(self):
        """Déplace une pièce"""
        cos = input("Entrez les coordonnées de la pièce a bouger et de sa destination sous cette forme: cos1/cos2" 
                    "(exemple: a1/a2")


    def ask(self):
        """Demande au joueur l'action qu'il veut effectuer"""
        self.tour = input(self.player + ", à vous de jouer ('m' pour bouger, 'e' pour manger, 'c' pour roquer):")
        if self.player[-1] == "1":
            self.player = "Joueur 2"
            self.color_tour = "b"
        else:
            self.player = "Joueur 1"
            self.color_tour = "w"
        self.verify_input()

    def verify_input(self):
        """Determine l'action a réaliser"""
        if self.tour.lower() == "m":
            self.move()
        elif self.tour.lower() == "e":
            self.eat()
        elif self.tour.lower() == "c":
            self.castle()
        else:
            self.tour = input("Je n'ai pas compris, réessayez:")
            self.verify_input()

    def run(self):
        """Fonction pour la boucle de jeu"""
        if self.is_chess:
            self.is_running = False
        self.board.display()
        self.ask()


game = Chess()
while game.is_running:
    game.run()