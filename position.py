from typing import List

from point import Point


class Position:
    def __init__(self, position: List[float]):
        """
        Передаются координаты 2х точек: левая верхняя и нижняя правая точки
        """
        self.left_top = Point(position[0], position[1])
        self.right_bottom = Point(position[2], position[3])

    def __str__(self):
        return str([self.left_top.x, self.left_top.y, self.right_bottom.x, self.right_bottom.y])

