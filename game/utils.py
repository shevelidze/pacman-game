import math
from .direction import Direction


def flatten(list_):
    return [item for sublist in list_ for item in sublist]


def get_angle_direction(angle):
    if angle > -math.pi / 4 and angle <= math.pi / 4:
        return Direction.RIGHT
    if angle > math.pi / 4 and angle <= 3 * math.pi / 4:
        return Direction.UP
    if angle > 3 * math.pi / 4 or angle <= -3 * math.pi / 4:
        return Direction.LEFT
    else:
        return Direction.DOWN


def get_distance(position1, position2):
    return math.sqrt(
        (position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2
    )


def get_vector(tail_position, head_position):
    return (
        head_position[0] - tail_position[0],
        head_position[1] - tail_position[1],
    )


def add_vectors(vector1, vector2):
    return (
        vector1[0] + vector2[0],
        vector1[1] + vector2[1],
    )


def multiply_vector_by_scalar(vector, scalar):
    return (vector[0] * scalar, vector[1] * scalar)
