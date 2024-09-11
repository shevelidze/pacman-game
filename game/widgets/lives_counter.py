import pygame
from ..widget import Widget
from ..game_field import GameField


class LivesCounterWidget(Widget):
    def __init__(self, game_field: GameField):
        self.__game_field = game_field
        self.__size = 15
        self.__gap = 10
        self.__margin = 20

    def draw(self, screen):
        for i in range(self.__game_field.get_lives()):
            pygame.draw.circle(
                screen,
                (255, 255, 0),
                (
                    self.__margin + self.__size + i * (self.__size * 2 + self.__gap),
                    self.__margin + self.__size,
                ),
                self.__size,
            )
