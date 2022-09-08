import manim as mn

def new_matrix(self, matrix: list[list]):
    m0 = mn.Matrix(matrix)
    self.add(m0)
    self.play(mn.Create(m0))
    self.wait(2)


class BlockDiagonalMatrix(mn.Scene):
    def construct(self):
        # Блочно-диагональная
        matrix = [
            ["A_1"    , 0        , r"\ldots", 0], 
            [0        ,"A_2"     , r"\dots" , 0],
            [r"\vdots", r"\vdots", r"\ddots", r"\vdots"],
            [0        ,         0, r"\ldots", "A_n"]
        ]
        new_matrix(self, matrix)

class BisymmetricMatrix(mn.Scene):
    def construct(self):
        # Бисимметричная матрица
        matrix = [
            ["a", "b", "c", "d", "e"],
            ["b", "f", "g", "h", "d"],
            ["c", "g", "i", "g", "c"],
            ["d", "h", "g", "f", "b"],
            ["e", "d", "c", "b", "a"]
        ]
        new_matrix(self, matrix)
