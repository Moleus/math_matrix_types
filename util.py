from typing import Callable, Dict
import manim as mn


def get_index2color(elements_count: int, color: mn.utils.color.Colors, condition: Callable[[int], bool]) -> Dict[int, mn.utils.color.Colors]:
    return {i: color for i in range(elements_count) if condition(i)}


def color_groups(matrixObj: mn.Matrix, index2color: Dict[int, mn.color.Colors]):
    entries = matrixObj.get_entries()
    for k in range(len(entries)):
        entries[k].set_color(index2color[k])
