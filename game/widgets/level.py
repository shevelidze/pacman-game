import pygame
from ..widget import Widget
from ..game_field import GameField


class LevelWidget(Widget):
    def __init__(self, game_field: GameField):
        self.__game_field = game_field
        self.__margin = 20
        self.__font = pygame.font.Font(None, 48)

    def draw(self, screen):
        screen_x, screen_y = screen.get_size()

        text_surface = self.__font.render(
            f"Level {self.__game_field.get_level() + 1}", False, (255, 255, 255)
        )
        screen.blit(
            text_surface,
            (
                screen_x - text_surface.get_width() - self.__margin,
                self.__margin,
            ),
        )
