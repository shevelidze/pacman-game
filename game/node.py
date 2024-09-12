from typing import Callable, Self, Iterable, Tuple
import math
from .utils import flatten, get_angle_direction, get_vector, get_distance
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

    def get_edges_positions(self):
        return map(
            lambda edge: (edge[0].get_position(), edge[1].get_position()),
            self.get_edges_recursively(),
        )

    def get_edges_recursively(
        self, edges: list[("Node", "Node")] = None, visited_nodes: set["Node"] = None
    ):
        if visited_nodes is None:
            visited_nodes = set()

        if self in visited_nodes:
            return set()

        if edges is None:
            edges = set()

        visited_nodes.add(self)

        for node in self.__connected_nodes:
            if (self, node) in edges or (node, self) in edges:
                continue

            edges.add((self, node))

        for connected_node in self.__connected_nodes:
            connected_node.get_edges_recursively(edges, visited_nodes)

        return edges

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

    def get_shortest_path_to(
        self,
        node: "Node",
        forbidden_on_start_node: "Node" = None,
        forbidden_edges: Iterable[Tuple["Node", "Node"]] = None,
    ):
        distances = self.find_shortest_distances(
            forbidden_on_start_node, forbidden_edges
        )

        if not node in distances:
            return None

        path = []

        current_node = node

        while current_node != self:
            path.append(current_node)

            connected_nodes = current_node.__connected_nodes

            if current_node == forbidden_on_start_node:
                connected_nodes = filter(
                    lambda filter_node: not filter_node == self, connected_nodes
                )

            current_node = min(
                connected_nodes,
                key=lambda min_node: (
                    distances[min_node] if min_node in distances else float("inf")
                ),
            )

        path.append(self)

        return list(reversed(path))

    # Dijkstra's algorithm
    def find_shortest_distances(
        self,
        forbidden_on_start_node: "Node" = None,
        forbidden_edges: Iterable[Tuple["Node", "Node"]] = None,
    ):
        nodes = set([self])
        visited_nodes = set()
        distances = {self: 0}
        if forbidden_edges is None:
            forbidden_edges = []

        current_node = self
        is_start = True

        while not current_node is None:
            visited_nodes.add(current_node)
            nodes = nodes.union(current_node.__connected_nodes)

            if is_start and forbidden_on_start_node in current_node.__connected_nodes:
                visited_nodes.add(forbidden_on_start_node)

            for node in current_node.__connected_nodes:
                if (
                    node in visited_nodes
                    or (node, current_node) in forbidden_edges
                    or (current_node, node) in forbidden_edges
                ):
                    continue

                new_distance = distances[current_node] + current_node.get_distance_to(
                    node
                )

                if not node in distances or new_distance < distances[node]:
                    distances[node] = new_distance

            ordered_unvisited_nodes = sorted(
                filter(
                    lambda node: not node in visited_nodes and node in distances, nodes
                ),
                key=lambda node: distances[node],
            )

            if len(ordered_unvisited_nodes) == 0:
                current_node = None
            else:
                current_node = ordered_unvisited_nodes[0]

            is_start = False

        return distances

    def get_distance_to(self, node: "Node"):
        return get_distance(self.get_position(), node.get_position())
