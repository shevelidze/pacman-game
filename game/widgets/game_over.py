import sys
import pygame
from ..widget import Widget


class GameOverWidget(Widget):
    def __init__(self):
        self.__font = pygame.font.Font(None, 48)

    def draw(self, screen):
        screen_x, screen_y = screen.get_size()

        text_surface = self.__font.render(
            "Game over! Press any key to exit", False, (255, 255, 255)
        )
        screen.blit(
            text_surface,
            (
                screen_x / 2 - text_surface.get_width() / 2,
                screen_y / 2 - text_surface.get_height() / 2,
            ),
        )

    def tick(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                sys.exit()
