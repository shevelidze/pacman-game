import pygame
from ..widget import Widget


class TimeoutCounterWidget(Widget):
    def __init__(self, target_time):
        self.__target_time = target_time
        self.__font = pygame.font.Font(None, 96)

    def draw(self, screen):
        screen_x, screen_y = screen.get_size()

        time_left = (self.__target_time - pygame.time.get_ticks()) // 1000 + 1

        text_surface = self.__font.render(str(time_left), False, (255, 255, 255))
        screen.blit(
            text_surface,
            (
                screen_x / 2 - text_surface.get_width() / 2,
                screen_y / 2 - text_surface.get_height() / 2,
            ),
        )

    def is_alive(self):
        return self.__target_time >= pygame.time.get_ticks()
