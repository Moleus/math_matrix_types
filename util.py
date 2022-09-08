from typing import Callable, Dict
import manim as mn
from dataclasses import dataclass


@dataclass
class Font:
  type: str
  size: int


def get_index2color(elements_count: int, color: mn.utils.color.Colors, condition: Callable[[int], bool]) -> Dict[int, mn.utils.color.Colors]:
    return {i: color for i in range(elements_count) if condition(i)}


def color_groups(matrixObj: mn.Matrix, index2color: Dict[int, mn.color.Colors]):
    entries = matrixObj.get_entries()
    for k in range(len(entries)):
        entries[k].set_color(index2color[k])


def create_equation(label: str, bodies: list[mn.VMobject]) -> mn.VGroup:
    group = mn.VGroup()
    m_label = mn.MathTex(label)
    group.add(m_label)
    prev_target = m_label
    for target in bodies:
        equal_sign = mn.Text("=").next_to(prev_target)
        target.next_to(equal_sign)
        prev_target = target
        group.add(equal_sign, target)
    return group
    

def zoom_object(self, target): 
    self.play(mn.ApplyPointwiseFunction(lambda x: 2 * x, target))
    self.wait(2);

    self.play(mn.ApplyPointwiseFunction(lambda x: x / 2, target))
    

def create_header() -> mn.VGroup:
    box = mn.Rectangle( height=1.1, width=3, fill_color=mn.RED, fill_opacity=0, stroke_color=mn.RED)
    formula = mn.MathTex(r"a_{ji} = - a_{ij}").move_to(box.get_center())
    return mn.VGroup(box, formula)