from typing import Callable
import pygame

from .object_on_field import ObjectOnField
from .pacman import Pacman
from .utils import get_distance
from .game_field import GameField


class Point(ObjectOnField):
    def __init__(
        self,
        field,
        previous_node,
        get_pacman: Callable[[], Pacman],
        get_total_dots_count: Callable[[], int],
        get_eaten_dots_count: Callable[[], int],
        next_node=None,
        distance_from_previous_node=None,
    ):
        super().__init__(field, previous_node, next_node, distance_from_previous_node)
        self.__get_pacman = get_pacman
        self.__get_total_dots_count = get_total_dots_count
        self.__get_eaten_dots_count = get_eaten_dots_count

    def tick(self, events):
        if self.__is_eaten:
            return

        pacman = self.__get_pacman()

        if pacman is None:
            return

        if get_distance(self._get_position(), pacman._get_position()) < 5:
            self.__is_eaten = True

            if self.__get_total_dots_count() == self.__get_eaten_dots_count():
                self._field.start_next_level()

    def draw(self, screen):
        if self.__is_eaten:
            return

        pygame.draw.circle(
            screen,
            (255, 185, 184),
            self._get_position_on_screen(),
            3,
        )

    def is_eaten(self):
        return self.__is_eaten

    @staticmethod
    def generate_points(
        field: GameField,
        get_pacman: Callable[[], Pacman],
        get_total_dots_count: Callable[[], int],
        get_eaten_dots_count: Callable[[], int],
    ):
        points = []

        edges = field.get_nodes_storage().get_nodes()[0].get_edges_recursively()

        desired_interval = 10

        no_points_nodes_identifiers = [
            "ghosts_room_outer_exit",
            "ghosts_room_inner_exit",
            "ghosts_room_x1y1",
            "ghosts_room_x1y2",
            "ghosts_room_x2y1",
            "ghosts_room_x2y2",
            "x4y4",
            "x5y4",
            "x5y4",
            "x6y4",
            "x4y5",
            "x7y5",
            "x4y6",
            "x7y6",
            "x7y4",
        ]

        for node1, node2 in edges:
            if (
                node1.get_identifier() in no_points_nodes_identifiers
                and node2.get_identifier() in no_points_nodes_identifiers
            ):
                continue

            edge_length = get_distance(node1.get_position(), node2.get_position())
            points_count = int(edge_length / desired_interval)

            interval = edge_length / points_count

            for i in range(1, points_count):
                distance_from_previous_node = i * interval

                points.append(
                    Point(
                        field,
                        node1,
                        get_pacman,
                        get_total_dots_count,
                        get_eaten_dots_count,
                        next_node=node2,
                        distance_from_previous_node=distance_from_previous_node,
                    )
                )

        for node in field.get_nodes_storage().get_nodes():
            if node.get_identifier() in no_points_nodes_identifiers:
                continue

            points.append(
                Point(
                    field,
                    node,
                    get_pacman,
                    get_total_dots_count,
                    get_eaten_dots_count,
                )
            )

        return points

    __is_eaten = False
