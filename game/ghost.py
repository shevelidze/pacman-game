import pygame
import random

from .movable_object_on_field import MovableObjectOnField
from .pacman import Pacman


class Ghost(MovableObjectOnField):
    def __init__(
        self,
        field,
        previous_node,
        pacman: Pacman,
        next_node=None,
        distance_from_previous_node=None,
    ):
        super().__init__(field, previous_node, next_node, distance_from_previous_node)
        self.__pacman = pacman

    def _get_target_node(self):
        # raise NotImplementedError
        return self.__pacman.get_previous_node()

    def _on_reached_node(self):
        target_node = self._get_target_node()
        last_node = self.get_last_node()

        shortest_path = last_node.get_shortest_path_to(target_node)

        target_next_node = (
            None
            if shortest_path is None or len(shortest_path) < 2
            else shortest_path[1]
        )

        if (
            self._next_node is None and self._previous_node == target_next_node
        ) or self._next_node == target_next_node:
            direction = self._get_direction()

            next_node_by_direction = last_node.get_connected_node_by_direction(
                direction
            )

            if not next_node_by_direction is None:
                self._set_next_node(next_node_by_direction)
            else:
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

                self._set_next_node(random.choice(suitable_nodes))

        else:
            self._set_next_node(target_next_node)

    def tick(self, events):
        super().tick(events)

        if not self._is_moving():
            self._start_moving()

    def draw(self, screen):
        size = 25
        center_x, center_y = self._get_position_on_screen()
        rect = pygame.Rect((center_x - size / 2, center_y - size / 2), (size, size))

        pygame.draw.rect(screen, self._color, rect)

    __pacman: Pacman
