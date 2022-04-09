class Piece():
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def __str__(self):
        return self.name[:2].upper()



class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color, "Pawn")

    def can_move(self, *loc):
        """Pour vérifier si le mouvement est 'légal'"""
        if loc[1] == 1 and loc[0] == 0:
            return True
        return False



class Rook(Piece):
    def __init__(self, color):
        super().__init__(color, "Rook")
        self.has_moved = False

    def can_move(self, *loc):
        """Pour vérifier si le mouvement est 'légal'"""
        if (loc[0] == 0 and loc[1] != 0) or (loc[0] != 0 and loc[1] == 0):
            return True
        return False



class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color, "Bishop")

    def can_move(self, *loc):
        """Pour vérifier si le mouvement est 'légal'"""
        if abs(loc[0]) == abs(loc[1]):
            return True
        return False



class Knight(Piece):
    def __init__(self, color):
        super().__init__(color, "Knight")

    def can_move(self, *loc):
        """Pour vérifier si le mouvement est 'légal'"""
        if (abs(loc[0]) == 1 and abs(loc[1]) == 3) or (abs(loc[1]) == 1 and abs(loc[0]) == 3):
            return True
        return False



class Queen(Piece):
    def __init__(self, color):
        super().__init__(color, "Queen")

    def can_move(self, *loc):
        """Pour vérifier si le mouvement est 'légal'"""
        if (abs(loc[0]) == abs(loc[1])) or ((loc[0] == 0 and loc[1] != 0) or (loc[0] != 0 and loc[1] == 0)):
            return True
        return False



class King(Piece):
    def __init__(self, color):
        super().__init__(color, "Knight")
        self.has_moved = False

    def can_move(self, *loc):
        """Pour vérifier si le mouvement est 'légal'"""
        if abs(loc[0]) == 1 or abs(loc[1]) == 1:
            return True
        return False

    def can_catsle(self, rook):
        """Pour vérifier si les conditions requises au roque sont respectées"""
        if not rook.has_moved and not self.has_moved:
            return True
        return False