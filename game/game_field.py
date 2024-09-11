from typing import Callable
import pygame
from .game_clock import GameClock


class GameField:
    def __init__(
        self,
        screen: pygame.Surface,
        game_clock: GameClock,
        handle_pacman_eaten: Callable,
    ):
        self.__screen = screen
        self.__size = (210, 232)
        self.__game_clock = game_clock
        self.__lives = 3
        self.__handle_pacman_eaten = handle_pacman_eaten

    def handle_pacman_eaten(self):
        if self.__lives <= 0 or not self.__game_clock.is_started():
            return

        self.__lives -= 1
        self.__handle_pacman_eaten()

    def get_lives(self):
        return self.__lives

    def get_game_clock(self):
        return self.__game_clock

    def map_graph_coordinate_to_screen(self, coordinate: float):
        return coordinate * 2

    def map_graph_position_to_screen(self, position):
        screen_width, screen_height = self.__screen.get_size()
        field_width, field_heigh = self.__size
        x, y = position
        x_margin = (screen_width - self.map_graph_coordinate_to_screen(field_width)) / 2
        y_margin = (
            screen_height - self.map_graph_coordinate_to_screen(field_heigh)
        ) / 2
        return x_margin + self.map_graph_coordinate_to_screen(
            x
        ), y_margin + self.map_graph_coordinate_to_screen(y)
