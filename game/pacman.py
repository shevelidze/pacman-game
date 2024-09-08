import random
import pygame
from .object_on_field import ObjectOnField

SPEED = 0.1


class Pacman(ObjectOnField):
    def tick(self):
        if self.started_moving_at is None:
            self.started_moving_at = pygame.time.get_ticks()

        if (
            self._get_traveled_ratio(additional_distance=self.__get_passed_distance())
            >= 1
        ):
            self._distance_from_previous_node = 0
            self._previous_node = self._next_node
            self._next_node = random.choice(self._next_node.get_connected_nodes())
            self.started_moving_at = pygame.time.get_ticks()

    def __get_passed_distance(self):
        time_passed = pygame.time.get_ticks() - self.started_moving_at
        return time_passed * SPEED

    def draw(self, screen):

        pygame.draw.circle(
            screen,
            (255, 255, 0),
            self._get_position_on_screen(
                additional_distance=self.__get_passed_distance()
            ),
            15,
        )

    started_moving_at = None
