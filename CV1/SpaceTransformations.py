import numpy as np

from DataTransformations import generate_homogenous_movement_matrix


def move_coordinates(coordinates: np.ndarray, dx: float, dy: float) -> np.ndarray:
    """
    Changes position of given set of coordinates by given dx and dy
    :param coordinates:
    :param dx:
    :param dy:
    :return:
    """
    movement_matrix = generate_homogenous_movement_matrix(dx, dy)
    moved_coordinates = np.dot(coordinates, movement_matrix)
    return moved_coordinates


def scale_coordinates(coordinates: np.ndarray, sx: float, sy: float) -> np.ndarray:
    """
    Changes scale of given set of coordinates by given sx and sy \n
    Scaling matrix: \n
    [sx 0 0] \n
    [0 sy 0] \n
    [0 0 1]
    :param coordinates:
    :param sx: Scaling by X
    :param sy: Scaling by Y
    :return: scaled coordinates
    """
    scaling_matrix = np.diag([sx, sy, 1])
    scaled_coordinates = np.dot(coordinates, scaling_matrix)
    return scaled_coordinates
