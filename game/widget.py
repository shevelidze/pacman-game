import pygame


class Widget:
    def draw(self, screen: pygame.Surface):
        raise NotImplementedError

    def tick(self, events: list[pygame.event.Event]):
        pass

    def is_alive(self):
        return True
