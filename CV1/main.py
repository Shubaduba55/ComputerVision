import time

import cv2 as cv
from typing import List
import numpy as np

import graphics
from graphics import Polygon, GraphWin, Point
import math as m

# My modules
from DataTransformations import make_homogeneous, turn_coordinates_into_points
from SpaceTransformations import move_coordinates, scale_coordinates


"""
(0, 1.0)
(0.9510565162951535, 0.30901699437494745)
(0.5877852522924731, -0.8090169943749473)
(-0.587785252292473, -0.8090169943749475)
(-0.9510565162951536, 0.30901699437494734)
"""


def draw_polygon(coordinates: np.ndarray, win: GraphWin, color: str = "black"):
    """
    Draws polygon with given coordinates.
    :param coordinates: coordinates of the polygon
    :param win: window in which we display figure
    :param color: color of the figure
    :return:
    """
    pentagon = Polygon(turn_coordinates_into_points(coordinates))
    pentagon.setOutline(color=color)
    pentagon.draw(win)
    time.sleep(0.25)


def main():
    # Pentagon coordinates
    pentagon_coordinates = [[0, 1.0],
                            [0.9510565162951535, 0.30901699437494745],
                            [0.5877852522924731, -0.8090169943749473],
                            [-0.587785252292473, -0.8090169943749475],
                            [-0.9510565162951536, 0.30901699437494734]]
    # Setup size of pentagon (*50 makes it bigger)
    pentagon_coordinates = [[c[0] * 50, c[1] * 50] for c in pentagon_coordinates]
    # Setup initial position of pentagon
    pentagon_coordinates = [[c[0] + 50, c[1] + 50] for c in pentagon_coordinates]

    # Setup pentagon coordinates in numpy array
    pentagon_coordinates = np.array(pentagon_coordinates)
    # Make coordinates homogeneous
    pentagon_homogeneous = make_homogeneous(pentagon_coordinates)

    # Setup window
    xw, yw = 600, 600
    win = GraphWin("Pentagon", xw, yw)
    win.setBackground('white')

    # Initial polygon view
    draw_polygon(pentagon_homogeneous, win)

    # Perform 10 times actions: scale bigger, move, scale smaller
    for _ in range(10):
        pentagon_homogeneous = scale_coordinates(pentagon_homogeneous, 3, 3)
        draw_polygon(pentagon_homogeneous, win, "red")
        pentagon_homogeneous = move_coordinates(pentagon_homogeneous, 100, 50)
        draw_polygon(pentagon_homogeneous, win, "green")
        pentagon_homogeneous = scale_coordinates(pentagon_homogeneous, 0.25, 0.25)
        draw_polygon(pentagon_homogeneous, win, "blue")

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
