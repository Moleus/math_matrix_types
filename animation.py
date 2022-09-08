import manim as mn
from typing import Callable, Dict
import util
from functools import partial


def new_matrix(self, matrix: list[list], modifier: Callable[[mn.Matrix], None] = None):
    matrixObj = mn.Matrix(matrix)
    if modifier:
        modifier(matrixObj)
    self.add(matrixObj)
    self.play(mn.Create(matrixObj))
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

class BlockMatrix(mn.Scene):
    def construct(self):
        # Блочная матрица
        matrix = [
            [1, 1, 2, 2],
            [1, 1, 2, 2],
            [3, 3, 4, 4],
            [3, 3, 4, 4],
        ]

        elements = len(matrix[0]) * len(matrix)
        index2color = util.get_index2color(elements_count=elements, color=mn.BLUE, condition=lambda i: i % 4 <= 1 and i < 6) \
            | util.get_index2color(elements_count=elements, color=mn.GREEN, condition=lambda i: i % 4 > 1 and i < 8) \
            | util.get_index2color(elements_count=elements, color=mn.YELLOW, condition=lambda i: i % 4 <= 1 and i >= 8) \
            | util.get_index2color(elements_count=elements, color=mn.RED, condition=lambda i: i % 4 > 1 and i >= 8)
        new_matrix(self, matrix, partial(util.color_groups, index2color=index2color))