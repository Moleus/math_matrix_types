import manim as mn
from manim import *
from typing import Callable, Dict
import util
from functools import partial
import numpy as np


def new_matrix(self, matrix: list[list], modifier: Callable[[mn.Matrix], None] = None):
    matrixObj = mn.Matrix(matrix)
    if modifier:
        modifier(matrixObj)
    mn.Create(matrixObj)
    util.zoom_object(self, matrixObj)
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


class AntisymmetricMatrix(mn.Scene):
    def construct(self):
        FONT = util.Font(type="monospace", size=48)
        PLAY_KW = {"run_time": 1.5}

        # Антисимметричная матрица
        matrix = Matrix([
            [0, 2, -45],
            [-2, 0, -4],
            [45, 4, 4],
        ])

        antisymmetric = Matrix([
            [0, -2, 45],
            [2, 0, 4],
            [-45, -4, 4],
        ])

        colors1 = [
            WHITE, GREEN, YELLOW, 
            WHITE, WHITE, RED, 
            WHITE, WHITE, WHITE
            ]

        colors2 = [
            WHITE, WHITE, WHITE, 
            GREEN, WHITE, WHITE, 
            YELLOW, RED, WHITE
            ]
        
        for i, (entry1, entry2) in enumerate(zip(matrix.get_entries(), antisymmetric.get_entries())):
            entry1.set_color(colors1[i])
            entry2.set_color(colors2[i])
        
        # text:
        header = util.create_header()

        util.zoom_object(self, header)

        # self.play(Write(header))
        self.play(ApplyMethod(header.shift, mn.UP*3))

        # first matrix objects
        equation1 = util.create_equation("A", [matrix])

        # animate
        equation1.shift(mn.LEFT*2)
        self.play(Write(equation1), **PLAY_KW)
        self.wait(3)
        self.play(ApplyMethod(equation1.shift, mn.LEFT*4.5))

        # antisymmetric matrix objects
        equation2 = util.create_equation("-A", [antisymmetric, mn.MathTex("A^T")])

        equation2.shift(mn.LEFT*.5)
        self.play(Write(equation2), **PLAY_KW)
