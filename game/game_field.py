import pygame


class GameField:
    def __init__(self, screen: pygame.Surface):
        self.__screen = screen
        self.__size = (210, 232)

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
