import pygame


class GameClock:
    def __init__(self):
        self.__started_at = 0
        self.__stopped_at = 0

    def get_time(self):
        if self.__started_at is None:
            return self.__stopped_at

        return self.__stopped_at + (pygame.time.get_ticks() - self.__started_at)

    def is_started(self):
        return self.__started_at is not None

    def stop(self):
        self.__stopped_at = self.get_time()
        self.__started_at = None

    def start(self):
        self.__started_at = pygame.time.get_ticks()

    def toggle(self):
        if self.is_started():
            self.stop()
        else:
            self.start()
