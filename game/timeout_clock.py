import pygame


class TimeoutClock:
    def __init__(self):
        self.__timeouts = []

    def add_timeout(self, callback, execute_in):
        current_time = self.__get_time()

        self.__timeouts.append((callback, execute_in, current_time))

        return current_time + execute_in

    def tick(self):
        current_time = self.__get_time()

        for timeout in self.__timeouts:
            callback, execute_in, start_time = timeout

            if current_time - start_time >= execute_in:
                callback()
                self.__timeouts.remove(timeout)

    def __get_time(self):
        return pygame.time.get_ticks()
