from typing import Callable, Self
import math
from .utils import flatten, get_angle_direction, get_vector
from .direction import Direction


class Node:
    def __init__(
        self,
        position: (float, float),
        identifier=None,
    ):
        self.__connected_nodes = []
        self.__position = position
        self.__identifier = identifier

    def is_directly_connected_to(self, node: "Node"):
        return node in self.__connected_nodes

    def get_connected_nodes(self):
        return self.__connected_nodes.copy()

    def get_position(self):
        return self.__position

    def get_identifier(self):
        return self.__identifier

    def connect(self, node: "Node"):
        self.__connected_nodes.append(node)
        node.__connected_nodes.append(self)

    def get_edges_positions(self, visited_nodes: set["Node"] = set()):
        if self in visited_nodes:
            return set()

        edges_positions: set[((float, float), (float, float))] = set()

        visited_nodes.add(self)

        for node in self.__connected_nodes:
            edges_positions.add((self.__position, node.__position))

        return edges_positions.union(
            flatten(
                list(connected_node.get_edges_positions())
                for connected_node in self.__connected_nodes
            )
        )

    def get_node_direction(self, node: "Node") -> Direction:
        other_node_position = node.get_position()
        self_position = self.get_position()

        vector = get_vector(self_position, other_node_position)

        angle = math.atan2(*vector)

        return get_angle_direction(angle)

    def get_connected_node_by_direction(self, direction: Direction) -> Self | None:
        for node in self.__connected_nodes:
            if self.get_node_direction(node) == direction:
                return node

        return None

    def bfs(callback: Callable[["Node"], bool]):
        visited_nodes = set()

        queue = [self]

        while queue:
            node = queue.pop(0)

            if node in visited_nodes:
                continue

            visited_nodes.add(node)

            if callback(node):
                return

            queue.extend(node.__connected_nodes)
