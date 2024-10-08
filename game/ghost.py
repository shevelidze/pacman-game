import pygame
import random
from typing import Callable

from .movable_object_on_field import MovableObjectOnField
from .pacman import Pacman
from .utils import get_distance


class Ghost(MovableObjectOnField):
    def __init__(
        self,
        field,
        previous_node,
        pacman: Pacman,
        get_total_dots_count: Callable[[], int],
        get_eaten_dots_count: Callable[[], int],
        next_node=None,
        distance_from_previous_node=None,
    ):
        super().__init__(field, previous_node, next_node, distance_from_previous_node)
        self._pacman = pacman
        self._get_total_dots_count = get_total_dots_count
        self._get_eaten_dots_count = get_eaten_dots_count

    def _get_target_node(self):
        raise NotImplementedError

    def _get_random_next_node(self):
        direction = self._get_direction()

        next_node_by_direction = self.get_last_node().get_connected_node_by_direction(
            direction
        )

        if not next_node_by_direction is None:
            return next_node_by_direction

        suitable_nodes = (
            self._previous_node.get_connected_nodes()
            if self._next_node is None
            else list(
                filter(
                    lambda node: not self._next_node.get_node_direction(
                        node
                    ).is_opposite_to(self._get_direction()),
                    self._next_node.get_connected_nodes(),
                )
            )
        )

        return random.choice(suitable_nodes)

    def _on_reached_node(self):
        target_node = self._get_target_node()

        if (
            self._next_node is None and self._previous_node == target_node
        ) or self._next_node == target_node:
            self._set_next_node(self._get_random_next_node())
        else:
            nodes_storage = self._field.get_nodes_storage()

            shortest_path = self.get_last_node().get_shortest_path_to(
                target_node,
                self._previous_node if not self._next_node is None else None,
                (
                    None
                    if self._can_exit_room()
                    else [
                        (
                            nodes_storage.get_node_by_identifier(
                                "ghosts_room_outer_exit"
                            ),
                            nodes_storage.get_node_by_identifier(
                                "ghosts_room_inner_exit"
                            ),
                        )
                    ]
                ),
            )

            if shortest_path is None:
                self._set_next_node(self._get_random_next_node())
            else:
                self._set_next_node(shortest_path[1])

    def tick(self, events):
        super().tick(events)

        if get_distance(self._get_position(), self._pacman._get_position()) < 10:
            self._field.handle_pacman_eaten()

        if not self._is_moving():
            self._start_moving()

    def draw(self, screen):
        size = 25
        center_x, center_y = self._get_position_on_screen()
        rect = pygame.Rect((center_x - size / 2, center_y - size / 2), (size, size))

        pygame.draw.rect(screen, self._color, rect)

    def _can_exit_room(self):
        return False

    def _get_speed(self):
        return self._initial_speed + (self._field.get_level() * 0.011)

    _pacman: Pacman
    _initial_speed = 0.04
