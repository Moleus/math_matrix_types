import manim as mn

class SetRowColorsExample(mn.Scene):
    def construct(self):
        m0 = mn.Matrix([
                           ["A_1"    , 0        , r"\ldots", 0], 
                           [0        ,"A_2"     , r"\dots" , 0],
                           [r"\vdots", r"\vdots", r"\ddots", r"\vdots"],
                           [0        ,         0, r"\ldots", "A_n"]
                       ]
        )
        self.add(m0)
        self.play(mn.Create(m0))
        self.wait(5)
