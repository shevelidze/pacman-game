import pygame
import sys

from .node import Node
from .nodes_storage import NodesStorage
from .original_map_nodes_builder import OriginalMapNodesBuilder
from .pacman import Pacman
from .game_field import GameField

pygame.init()


class Game:
    def __init__(self):
        self.__screen = pygame.display.set_mode((800, 600))

        nodes_builder = OriginalMapNodesBuilder()
        nodes_builder.define_default_connections()

        self.__field = GameField(self.__screen)
        self.__nodes = nodes_builder.get_nodes()
        self.__nodes_storage = NodesStorage(self.__nodes)
        self.__objects_on_field = [
            Pacman(
                self.__field,
                self.__nodes_storage.get_node_by_identifier("x6y8"),
                self.__nodes_storage.get_node_by_identifier("x5y8"),
                11,
            )
        ]

    def runLoop(self):

        edges_positions = self.__nodes[0].get_edges_positions()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.__screen.fill((0, 0, 0))

            for object_on_field in self.__objects_on_field:
                object_on_field.tick()

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
