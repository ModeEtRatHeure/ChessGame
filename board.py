from pieces import *

class Board:
    def __init__(self):
        self.board = [[Rook("w"), Knight("w"), Bishop("w"), Queen("w"), King("w"), Bishop("w"), Knight("w"), Rook("w")],
                      [Pawn("w"), Pawn("w"), Pawn("w"), Pawn("w"), Pawn("w"), Pawn("w"), Pawn("w"), Pawn("w")],
                      ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "], ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                      ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "], ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                      [Pawn("b"), Pawn("b"), Pawn("b"), Pawn("b"), Pawn("b"), Pawn("b"), Pawn("b"), Pawn("b")],
                      [Rook("b"), Knight("b"), Bishop("b"), Queen("b"), King("b"), Bishop("b"), Knight("b"), Rook("b")]]


    def display(self):
        """Affiche le plateau"""
        count = 0
        letters = "abcdefgh"
        split = "   --   --   --   --   --   --   --   -- "
        for i in self.board:
            count += 1
            print(count, "|", end=" ")
            for j in i:
                print(str(j), "|", end=" ")
            print(f"\n", split)
        print("   ", "    ".join(letters))



