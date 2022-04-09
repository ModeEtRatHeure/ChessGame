from pieces import *

class Board:
    def __init__(self):
        self.board = [[Rook("w"), Knight("w"), Bishop("w"), Queen("w"), King("w"), Bishop("w"), Knight("w"), Rook("w")],
                      [Pawn("w"), Pawn("w"), Pawn("w"), Pawn("w"), Pawn("w"), Pawn("w"), Pawn("w"), Pawn("w")],
                      ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "], ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                      ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "], ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                      [Pawn("b"), Pawn("b"), Pawn("b"), Pawn("b"), Pawn("b"), Pawn("b"), Pawn("b"), Pawn("b")],
                      [Rook("b"), Knight("b"), Bishop("b"), Queen("b"), King("b"), Bishop("b"), Knight("b"), Rook("b")]]
        self.letters = "abcdefgh"


    def display(self):
        """Affiche le plateau"""
        count = 0
        split = "   --   --   --   --   --   --   --   -- "
        for i in self.board:
            count += 1
            print(count, "|", end=" ")
            for j in i:
                print(str(j), "|", end=" ")
            print(f"\n", split)
        print("   ", "    ".join(self.letters))


    def convert(self, cos):
        """Convertis les coordonnées passées en argumant en int"""
        coordinates = [self.letters.find(cos[0].lower()), int(cos[1]) - 1]
        return coordinates


    def get_piece(self, coordinates):
        """Récupère la pièce se situant aux coordonnées spécifiées"""
        cos = self.convert(coordinates[:2])
        piece = self.board[cos[1]][cos[0]]
        return piece


    def is_empty(self, cos):
        """Vérifie que la case est vide"""
        coordinates = self.convert(cos)
        if self.board[coordinates[1]][coordinates[0]] == "  ":
            return True
        return False


    def move_piece(self, piece_address, cos):
        piece = None
        for i in self.board:
            for j in i:
                if j.__repr__() == piece_address:
                    piece = j
        #if