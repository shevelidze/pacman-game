import pygame
import sys

from .node import Node
from .nodes_storage import NodesStorage
from .original_map_nodes_builder import OriginalMapNodesBuilder
from .pacman import Pacman
from .game_field import GameField
from .ghosts import Blinky, Clyde, Inky, Pinky

pygame.init()


class Game:
    def __init__(self):
        self.__screen = pygame.display.set_mode((800, 600))
        self.__clock = pygame.time.Clock()

        nodes_builder = OriginalMapNodesBuilder()
        nodes_builder.define_default_connections()

        self.__field = GameField(self.__screen)
        self.__nodes = nodes_builder.get_nodes()
        self.__nodes_storage = NodesStorage(self.__nodes)

        pacman = Pacman(
            self.__field,
            self.__nodes_storage.get_node_by_identifier("x6y8"),
            self.__nodes_storage.get_node_by_identifier("x5y8"),
            11,
        )

        blinky = Blinky(
            self.__field,
            self.__nodes_storage.get_node_by_identifier("ghosts_room_x1y1"),
            pacman,
        )

        clyde = Clyde(
            self.__field,
            self.__nodes_storage.get_node_by_identifier("ghosts_room_x2y1"),
            pacman,
        )

        inky = Inky(
            self.__field,
            self.__nodes_storage.get_node_by_identifier("ghosts_room_x1y2"),
            pacman,
        )

        pinky = Pinky(
            self.__field,
            self.__nodes_storage.get_node_by_identifier("ghosts_room_x2y2"),
            pacman,
        )

        self.__objects_on_field = [pacman, blinky, clyde, inky, pinky]

    def runLoop(self):
        edges_positions = self.__nodes[0].get_edges_positions()

        while True:
            self.__clock.tick(60)
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.__screen.fill((0, 0, 0))

            for object_on_field in self.__objects_on_field:
                object_on_field.tick(events)

            for edge_position1, edge_position2 in edges_positions:
                position1 = self.__field.map_graph_position_to_screen(edge_position1)
                position2 = self.__field.map_graph_position_to_screen(edge_position2)

                pygame.draw.line(self.__screen, (0, 0, 255), position1, position2, 2)

            for node in self.__nodes:
                position = self.__field.map_graph_position_to_screen(
                    node.get_position()
                )
                pygame.draw.circle(self.__screen, (0, 0, 225), position, 5)

            for object_on_field in self.__objects_on_field:
                object_on_field.draw(self.__screen)

            pygame.display.flip()
