import manim as mn
from manim import Write, ApplyMethod
from typing import Callable, Dict
import util
from functools import partial
import numpy as np


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


class AntisymmetricMatrix(mn.Scene):
    def construct(self):
        FONT = util.Font(type="monospace", size=48)
        PLAY_KW = {"run_time": 0.5}

        # Антисимметричная матрица
        matrix = np.array([
            [0, 2, -45],
            [-2, 0, -4],
            [45, 4, 4],
        ])
        
        antisymmetric = np.zeros(matrix.shape, dtype="int64")
        for iy, ix in np.ndindex(matrix.shape):
            antisymmetric[ix][iy] = int(matrix[iy][ix])
            
        # text:
        header = mn.VGroup()  # create a VGroup
        box = mn.Rectangle(  # create a box
            height=1.1, width=3, fill_color=mn.RED,
            fill_opacity=0, stroke_color=mn.RED
        )
        formula = mn.MathTex(r"a_{ji} = - a_{ij}", font_size=FONT.size).move_to(box.get_center())
        header.add(box, formula)  # add both objects to the VGroup

        self.play(Write(header))
        self.play(ApplyMethod(header.shift, mn.UP*3))

        # first matrix objects
        m_label = mn.MathTex("A", font_size=FONT.size)
        m_label.shift(mn.LEFT)
        equal_sign = mn.Text("=", font_size=FONT.size, font=FONT.type)
        origin_matrix = mn.Matrix(matrix.tolist())
        orig_m_group = mn.VGroup(m_label, equal_sign, origin_matrix)
        
        # first matrix operations
        equal_sign.next_to(m_label)
        origin_matrix.next_to(equal_sign)

        # animate
        self.play(Write(m_label), Write(equal_sign))
        self.play(Write(origin_matrix))
        self.play(ApplyMethod(orig_m_group.shift, mn.LEFT*5.5))
        self.play(ApplyMethod(orig_m_group.shift, mn.UP*1))

        # antisymmetric matrix objects
        antisym_matrix = mn.Matrix(antisymmetric)
        neg_m_label = mn.MathTex("-A", font_size=FONT.size)
        neg_m_label.shift(mn.LEFT)
        equal_sign2 = equal_sign.copy()
        equal_sign3 = equal_sign.copy()
        transpose_label = mn.MathTex("A^T", font_size=FONT.size)
        neg_m_group = mn.VGroup(neg_m_label, equal_sign2, antisym_matrix)

        # antisymmetric matrix operations
        equal_sign2.next_to(neg_m_label)
        antisym_matrix.next_to(equal_sign2)

        self.play(Write(neg_m_label), Write(equal_sign2))
        self.play(Write(antisym_matrix))
        self.play(ApplyMethod(neg_m_group.shift, mn.DOWN*2))
        self.play(ApplyMethod(neg_m_group.shift, mn.LEFT*5.5))

        equal_sign3.next_to(antisym_matrix)
        transpose_label.next_to(equal_sign3)

        self.play(Write(equal_sign3))
        self.play(Write(transpose_label))