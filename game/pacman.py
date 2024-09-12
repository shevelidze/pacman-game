import random
import pygame
from .movable_object_on_field import MovableObjectOnField
from .direction import Direction


class Pacman(MovableObjectOnField):
    def __init__(
        self,
        field,
        previous_node,
        next_node=None,
        distance_from_previous_node=None,
    ):
        super().__init__(field, previous_node, next_node, distance_from_previous_node)

    def tick(self, events):
        super().tick(events)

        if not self._is_moving():
            self._start_moving()

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.__next_direction = Direction.LEFT
                if event.key == pygame.K_RIGHT:
                    self.__next_direction = Direction.RIGHT
                if event.key == pygame.K_UP:
                    self.__next_direction = Direction.UP
                if event.key == pygame.K_DOWN:
                    self.__next_direction = Direction.DOWN

        if not self.__next_direction is None and self.__next_direction.is_opposite_to(
            self._get_direction()
        ):
            self._turn_around()

    def _on_reached_node(self):
        if self.__next_direction is None:
            return

        next_node = self._next_node.get_connected_node_by_direction(
            self.__next_direction
        )

        if next_node is None:
            return

        self._set_next_node(next_node)

    def draw(self, screen):

        pygame.draw.circle(
            screen,
            (253, 255, 59),
            self._get_position_on_screen(),
            15,
        )

    __next_direction: Direction | None = Direction.LEFT
    _speed = 0.07
