import pygame
import sys

from .node import Node
from .nodes_storage import NodesStorage
from .original_map_nodes_builder import OriginalMapNodesBuilder
from .game_clock import GameClock
from .timeout_clock import TimeoutClock
from .pacman import Pacman
from .game_field import GameField
from .ghosts import Blinky, Clyde, Inky, Pinky
from .widgets import (
    TimeoutCounterWidget,
    LivesCounterWidget,
    GameOverWidget,
    LevelWidget,
)
from .point import Point

pygame.init()
pygame.font.init()


class Game:
    def __init__(self):
        self.__screen = pygame.display.set_mode((800, 600))
        self.__clock = pygame.time.Clock()
        self.__game_clock = GameClock()
        self.__timeout_clock = TimeoutClock()

        self.__game_clock.stop()

        nodes_builder = OriginalMapNodesBuilder()
        nodes_builder.define_default_connections()

        self.__nodes = nodes_builder.get_nodes()
        self.__nodes_storage = NodesStorage(self.__nodes)

        self.__field = GameField(
            self.__screen,
            self.__game_clock,
            self.__nodes_storage,
            self.__handle_pacman_eaten,
            self.__handle_start_next_level,
        )

        self.__widgets = [LivesCounterWidget(self.__field), LevelWidget(self.__field)]
        self.__pacman = None
        self.__ghosts = None
        self.__points = None

        self.__reset_points()

        self.__start_game()

    def run_loop(self):
        while True:
            self.__clock.tick(60)
            self.__timeout_clock.tick()

            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.__start_game()

            self.__screen.fill((0, 0, 0))

            self.__tick_widgets(events)
            self.__tick_objects_on_field(events)

            self.__draw_field()
            self.__draw_objects_on_field()
            self.__draw_widgets()

            pygame.display.flip()

    def __get_pacman(self):
        return self.__pacman

    def __get_total_points_count(self):
        return len(self.__points)

    def __get_eaten_points_count(self):
        return len(list(filter(lambda point: point.is_eaten(), self.__points)))

    def __handle_pacman_eaten(self):
        if self.__field.get_lives() <= 0:
            self.__game_clock.stop()
            self.__widgets.append(GameOverWidget())
        else:
            self.__start_game()

    def __handle_start_next_level(self):
        self.__reset_points()
        self.__start_game()

    def __start_game(self):
        self.__game_clock.stop()
        self.__reset_pacman_and_ghosts()
        game_starts_at = self.__timeout_clock.add_timeout(self.__game_clock.start, 3000)
        self.__widgets.append(TimeoutCounterWidget(game_starts_at))

    def __reset_pacman_and_ghosts(self):
        self.__pacman = self.__create_pacman()
        self.__ghosts = self.__create_ghosts(self.__pacman)

    def __reset_points(self):
        self.__points = Point.generate_points(
            self.__field,
            self.__get_pacman,
            self.__get_total_points_count,
            self.__get_eaten_points_count,
        )

    def __get_objects_on_field(self):
        if self.__pacman is None:
            return []

        return self.__points + [self.__pacman] + self.__ghosts

    def __create_pacman(self):
        return Pacman(
            self.__field,
            self.__nodes_storage.get_node_by_identifier("x6y8"),
            self.__nodes_storage.get_node_by_identifier("x5y8"),
            11,
        )

    def __create_ghosts(self, pacman):
        blinky = Blinky(
            self.__field,
            self.__nodes_storage.get_node_by_identifier("x6y9"),
            pacman,
            self.__get_total_points_count,
            self.__get_eaten_points_count,
        )

        clyde = Clyde(
            self.__field,
            self.__nodes_storage.get_node_by_identifier("ghosts_room_x2y1"),
            pacman,
            self.__get_total_points_count,
            self.__get_eaten_points_count,
        )

        inky = Inky(
            self.__field,
            self.__nodes_storage.get_node_by_identifier("ghosts_room_x1y2"),
            pacman,
            self.__get_total_points_count,
            self.__get_eaten_points_count,
        )

        pinky = Pinky(
            self.__field,
            self.__nodes_storage.get_node_by_identifier("ghosts_room_x2y2"),
            pacman,
            self.__get_total_points_count,
            self.__get_eaten_points_count,
        )

        return [blinky, clyde, inky, pinky]

    def __draw_field(self):
        edges_positions = self.__nodes[0].get_edges_positions()

        for edge_position1, edge_position2 in edges_positions:
            position1 = self.__field.map_graph_position_to_screen(edge_position1)
            position2 = self.__field.map_graph_position_to_screen(edge_position2)

            pygame.draw.line(self.__screen, (39, 16, 172), position1, position2, 2)

        # for node in self.__nodes:
        #     position = self.__field.map_graph_position_to_screen(node.get_position())
        #     pygame.draw.circle(self.__screen, (0, 0, 225), position, 5)

    def __tick_objects_on_field(self, events):
        for object_on_field in self.__get_objects_on_field():
            object_on_field.tick(events)

    def __draw_objects_on_field(self):
        for object_on_field in self.__get_objects_on_field():
            object_on_field.draw(self.__screen)

    def __tick_widgets(self, events):
        for widget in self.__widgets:
            widget.tick(events)

        self.__widgets = list(filter(lambda widget: widget.is_alive(), self.__widgets))

    def __draw_widgets(self):
        for widget in self.__widgets:
            widget.draw(self.__screen)
