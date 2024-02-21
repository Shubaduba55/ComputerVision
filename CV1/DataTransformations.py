# Homogeneous coordinates
from typing import List

from graphics import Point
import numpy as np


def make_homogeneous(coordinates: np.ndarray) -> np.ndarray:
    """
    Turns 2d array of coordinates into 2d array of homogeneous coordinates
    :param coordinates: 2d array of coordinates arranged in arrays [x, y]
    :return: 2d array of coordinates arranged in arrays [x, y, 1]
    """

    ones = [1 for _ in range(len(coordinates))]
    coordinates = np.append(coordinates, np.expand_dims(ones, axis=1), axis=1)

    return coordinates


def turn_coordinates_into_points(coordinates: np.ndarray) -> List[Point]:
    """
    Turns ndarray of coordinates into List of points that can be directly passed to Polygon()
    :param coordinates: ndarray of coordinates arranged in arrays [x, y] or [x, y, 1]
    :return:
    """
    return [Point(c[0], c[1]) for c in coordinates]


def generate_homogenous_movement_matrix(dx: float, dy: float) -> np.ndarray:
    """
    Generates homogeneous movement matrix \n
    [1  0  0] \n
    [0  1  0] \n
    [dx dy 1]
    :param dx: Movement X
    :param dy: Movement Y
    :return: homogeneous movement matrix
    """
    matrix = np.eye(3)
    matrix[2, 0] = dx
    matrix[2, 1] = dy
    return matrix
