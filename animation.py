import manim as mn

class BlockDiagonalMatrix(mn.Scene):
    def construct(self):
        # Блочно-диагональная
        m0 = mn.Matrix([
                           ["A_1"    , 0        , r"\ldots", 0], 
                           [0        ,"A_2"     , r"\dots" , 0],
                           [r"\vdots", r"\vdots", r"\ddots", r"\vdots"],
                           [0        ,         0, r"\ldots", "A_n"]
                       ]
        )
        self.add(m0)
        self.play(mn.Create(m0))
        self.wait(2)

class BisymmetricMatrix(mn.Scene):
    def construct(self):
        # Бисимметричная матрица
        m0 = mn.Matrix([
                           ["a", "b", "c", "d", "e"],
                           ["b", "f", "g", "h", "d"],
                           ["c", "g", "i", "g", "c"],
                           ["d", "h", "g", "f", "b"],
                           ["e", "d", "c", "b", "a"]
                       ]
        )
        self.add(m0)
        self.play(mn.Create(m0))
        self.wait(2)
