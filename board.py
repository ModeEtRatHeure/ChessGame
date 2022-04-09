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
        coordinates2 = self.convert(cos)
        coordinates1 = []
        for i in self.board:
            for j in i:
                if id(j) == piece_address:
                    piece = j
                    coordinates1 = [self.board.index(i), self.board[self.board.index(i)].index(j)]
        if piece:
            self.board[coordinates2[1]][coordinates2[0]] = piece
            self.board[coordinates1[0]][coordinates1[1]] = "  "