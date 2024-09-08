import pygame
from .node import Node
from .utils import get_distance, get_vector, add_vectors, multiply_vector_by_scalar
from .game_field import GameField


class ObjectOnField:
    def __init__(
        self,
        field: GameField,
        previous_node: Node,
        next_node: Node = None,
        distance_from_previous_node: float = None,
    ):
        self.__field = field
        self._previous_node = previous_node
        self._next_node = next_node
        self._distance_from_previous_node = distance_from_previous_node

    def draw(self, screen: pygame.Surface):
        raise NotImplementedError

    def tick(self):
        pass

    def _get_position(self, additional_distance=None):
        if self._next_node is None:
            return self._previous_node.get_position()

        previous_node_position = self._previous_node.get_position()
        next_node_position = self._next_node.get_position()

        traveled_ratio = self._get_traveled_ratio(
            additional_distance=additional_distance
        )

        if traveled_ratio >= 1:
            return next_node_position

        vector = multiply_vector_by_scalar(
            get_vector(previous_node_position, next_node_position), traveled_ratio
        )

        return add_vectors(previous_node_position, vector)

    def _get_position_on_screen(self, additional_distance=None):
        return self.__field.map_graph_position_to_screen(
            self._get_position(additional_distance=additional_distance)
        )

    def _get_traveled_ratio(self, additional_distance=None):
        previous_node_position = self._previous_node.get_position()
        next_node_position = self._next_node.get_position()

        full_distance = get_distance(previous_node_position, next_node_position)

        return (
            self._distance_from_previous_node
            + (0 if additional_distance is None else additional_distance)
        ) / full_distance
