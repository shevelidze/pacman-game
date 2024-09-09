from .nodes_storage import NodesStorage
from .node import Node


class OriginalMapNodesBuilder:
    def __init__(self):
        self.__nodes = [
            Node((12, 11), identifier="x1y1"),
            Node((49, 11), identifier="x3y1"),
            Node((94, 11), identifier="x5y1"),
            #
            Node((116, 11), identifier="x6y1"),
            Node((161, 11), identifier="x8y1"),
            Node((198, 11), identifier="x10y1"),
            ##
            Node((12, 41), identifier="x1y2"),
            Node((49, 41), identifier="x3y2"),
            Node((72, 41), identifier="x4y2"),
            Node((94, 41), identifier="x5y2"),
            #
            Node((116, 41), identifier="x6y2"),
            Node((138, 41), identifier="x7y2"),
            Node((161, 41), identifier="x8y2"),
            Node((198, 41), identifier="x10y2"),
            ##
            Node((12, 64), identifier="x1y3"),
            Node((49, 64), identifier="x3y3"),
            Node((72, 64), identifier="x4y3"),
            Node((94, 64), identifier="x5y3"),
            #
            Node((116, 64), identifier="x6y3"),
            Node((138, 64), identifier="x7y3"),
            Node((161, 64), identifier="x8y3"),
            Node((198, 64), identifier="x10y3"),
            ##
            Node((72, 86), identifier="x4y4"),
            Node((94, 86), identifier="x5y4"),
            #
            Node((116, 86), identifier="x6y4"),
            Node((138, 86), identifier="x7y4"),
            ##
            Node((49, 108), identifier="x3y5"),
            Node((72, 108), identifier="x4y5"),
            #
            Node((138, 108), identifier="x7y5"),
            Node((161, 108), identifier="x8y5"),
            ##
            Node((72, 132), identifier="x4y6"),
            #
            Node((138, 132), identifier="x7y6"),
            ##
            Node((12, 154), identifier="x1y7"),
            Node((49, 154), identifier="x3y7"),
            Node((72, 154), identifier="x4y7"),
            Node((94, 154), identifier="x5y7"),
            #
            Node((116, 154), identifier="x6y7"),
            Node((138, 154), identifier="x7y7"),
            Node((161, 154), identifier="x8y7"),
            Node((198, 154), identifier="x10y7"),
            ##
            Node((12, 176), identifier="x1y8"),
            Node((26, 176), identifier="x2y8"),
            Node((49, 176), identifier="x3y8"),
            Node((72, 176), identifier="x4y8"),
            Node((94, 176), identifier="x5y8"),
            #
            Node((116, 176), identifier="x6y8"),
            Node((138, 176), identifier="x7y8"),
            Node((161, 176), identifier="x8y8"),
            Node((184, 176), identifier="x9y8"),
            Node((198, 176), identifier="x10y8"),
            ##
            Node((12, 198), identifier="x1y9"),
            Node((26, 198), identifier="x2y9"),
            Node((49, 198), identifier="x3y9"),
            Node((72, 198), identifier="x4y9"),
            Node((94, 198), identifier="x5y9"),
            #
            Node((116, 198), identifier="x6y9"),
            Node((138, 198), identifier="x7y9"),
            Node((161, 198), identifier="x8y9"),
            Node((184, 198), identifier="x9y9"),
            Node((198, 198), identifier="x10y9"),
            ##
            Node((12, 221), identifier="x1y10"),
            Node((94, 221), identifier="x5y10"),
            #
            Node((116, 221), identifier="x6y10"),
            Node((198, 221), identifier="x10y10"),
            #
            Node((105, 86), identifier="ghosts_room_outer_exit"),
            Node((105, 104), identifier="ghosts_room_inner_exit"),
            Node((90, 104), identifier="ghosts_room_x1y1"),
            Node((90, 114), identifier="ghosts_room_x1y2"),
            Node((120, 104), identifier="ghosts_room_x2y1"),
            Node((120, 114), identifier="ghosts_room_x2y2"),
        ]
        self.__storage = NodesStorage(self.__nodes)

    def define_default_connections(self):
        self.__storage.connect_nodes_by_identifiers("x1y1", "x3y1")
        self.__storage.connect_nodes_by_identifiers("x1y1", "x1y2")
        self.__storage.connect_nodes_by_identifiers("x1y2", "x1y3")
        self.__storage.connect_nodes_by_identifiers("x1y3", "x3y3")
        self.__storage.connect_nodes_by_identifiers("x3y3", "x3y5")
        self.__storage.connect_nodes_by_identifiers("x3y5", "x3y7")
        self.__storage.connect_nodes_by_identifiers("x3y7", "x1y7")
        self.__storage.connect_nodes_by_identifiers("x1y7", "x1y8")
        self.__storage.connect_nodes_by_identifiers("x1y8", "x2y8")
        self.__storage.connect_nodes_by_identifiers("x2y8", "x2y9")
        self.__storage.connect_nodes_by_identifiers("x2y9", "x1y9")
        self.__storage.connect_nodes_by_identifiers("x1y9", "x1y10")
        self.__storage.connect_nodes_by_identifiers("x1y10", "x5y10")
        self.__storage.connect_nodes_by_identifiers("x5y10", "x6y10")
        self.__storage.connect_nodes_by_identifiers("x6y10", "x10y10")
        self.__storage.connect_nodes_by_identifiers("x10y10", "x10y9")
        self.__storage.connect_nodes_by_identifiers("x10y9", "x9y9")
        self.__storage.connect_nodes_by_identifiers("x9y9", "x9y8")
        self.__storage.connect_nodes_by_identifiers("x9y8", "x10y8")
        self.__storage.connect_nodes_by_identifiers("x10y8", "x10y7")
        self.__storage.connect_nodes_by_identifiers("x10y7", "x8y7")
        self.__storage.connect_nodes_by_identifiers("x8y7", "x8y5")
        self.__storage.connect_nodes_by_identifiers("x8y5", "x8y3")
        self.__storage.connect_nodes_by_identifiers("x8y3", "x10y3")
        self.__storage.connect_nodes_by_identifiers("x10y3", "x10y2")
        self.__storage.connect_nodes_by_identifiers("x10y2", "x10y1")
        self.__storage.connect_nodes_by_identifiers("x10y1", "x8y1")
        self.__storage.connect_nodes_by_identifiers("x8y1", "x8y2")
        self.__storage.connect_nodes_by_identifiers("x8y2", "x10y2")
        self.__storage.connect_nodes_by_identifiers("x8y2", "x8y3")
        self.__storage.connect_nodes_by_identifiers("x8y2", "x7y2")
        self.__storage.connect_nodes_by_identifiers("x7y2", "x7y3")
        self.__storage.connect_nodes_by_identifiers("x7y3", "x6y3")
        self.__storage.connect_nodes_by_identifiers("x6y3", "x6y4")
        self.__storage.connect_nodes_by_identifiers("x6y4", "x7y4")
        self.__storage.connect_nodes_by_identifiers("x7y4", "x7y5")
        self.__storage.connect_nodes_by_identifiers("x7y5", "x8y5")
        self.__storage.connect_nodes_by_identifiers("x7y5", "x7y6")
        self.__storage.connect_nodes_by_identifiers("x7y6", "x4y6")
        self.__storage.connect_nodes_by_identifiers("x4y6", "x4y5")
        self.__storage.connect_nodes_by_identifiers("x4y5", "x3y5")
        self.__storage.connect_nodes_by_identifiers("x4y5", "x4y4")
        self.__storage.connect_nodes_by_identifiers("x4y4", "x5y4")
        self.__storage.connect_nodes_by_identifiers("x5y4", "x5y3")
        self.__storage.connect_nodes_by_identifiers("x5y3", "x4y3")
        self.__storage.connect_nodes_by_identifiers("x4y3", "x4y2")
        self.__storage.connect_nodes_by_identifiers("x4y2", "x3y2")
        self.__storage.connect_nodes_by_identifiers("x3y2", "x1y2")
        self.__storage.connect_nodes_by_identifiers("x3y2", "x3y3")
        self.__storage.connect_nodes_by_identifiers("x3y2", "x3y1")
        self.__storage.connect_nodes_by_identifiers("x3y1", "x5y1")
        self.__storage.connect_nodes_by_identifiers("x5y1", "x5y2")
        self.__storage.connect_nodes_by_identifiers("x5y2", "x4y2")
        self.__storage.connect_nodes_by_identifiers("x5y2", "x6y2")
        self.__storage.connect_nodes_by_identifiers("x6y2", "x6y1")
        self.__storage.connect_nodes_by_identifiers("x6y2", "x7y2")
        self.__storage.connect_nodes_by_identifiers("x6y1", "x8y1")
        #
        self.__storage.connect_nodes_by_identifiers("x2y9", "x3y9")
        self.__storage.connect_nodes_by_identifiers("x3y9", "x3y8")
        self.__storage.connect_nodes_by_identifiers("x3y8", "x3y7")
        self.__storage.connect_nodes_by_identifiers("x3y8", "x4y8")
        self.__storage.connect_nodes_by_identifiers("x4y8", "x4y9")
        self.__storage.connect_nodes_by_identifiers("x4y9", "x5y9")
        self.__storage.connect_nodes_by_identifiers("x5y9", "x5y10")
        self.__storage.connect_nodes_by_identifiers("x4y8", "x5y8")
        self.__storage.connect_nodes_by_identifiers("x5y8", "x6y8")
        self.__storage.connect_nodes_by_identifiers("x6y8", "x7y8")
        self.__storage.connect_nodes_by_identifiers("x7y8", "x7y9")
        self.__storage.connect_nodes_by_identifiers("x7y9", "x6y9")
        self.__storage.connect_nodes_by_identifiers("x6y9", "x6y10")
        self.__storage.connect_nodes_by_identifiers("x4y6", "x4y7")
        self.__storage.connect_nodes_by_identifiers("x4y7", "x3y7")
        self.__storage.connect_nodes_by_identifiers("x4y7", "x5y7")
        self.__storage.connect_nodes_by_identifiers("x5y7", "x5y8")
        self.__storage.connect_nodes_by_identifiers("x9y9", "x8y9")
        self.__storage.connect_nodes_by_identifiers("x8y9", "x8y8")
        self.__storage.connect_nodes_by_identifiers("x8y8", "x7y8")
        self.__storage.connect_nodes_by_identifiers("x6y8", "x6y7")
        self.__storage.connect_nodes_by_identifiers("x6y7", "x7y7")
        self.__storage.connect_nodes_by_identifiers("x7y7", "x8y7")
        self.__storage.connect_nodes_by_identifiers("x8y8", "x8y9")
        self.__storage.connect_nodes_by_identifiers("x8y8", "x8y7")
        self.__storage.connect_nodes_by_identifiers("x7y6", "x7y7")
        #
        self.__storage.connect_nodes_by_identifiers("x5y4", "ghosts_room_outer_exit")
        self.__storage.connect_nodes_by_identifiers("x6y4", "ghosts_room_outer_exit")
        self.__storage.connect_nodes_by_identifiers(
            "ghosts_room_inner_exit", "ghosts_room_outer_exit"
        )
        self.__storage.connect_nodes_by_identifiers(
            "ghosts_room_x1y1", "ghosts_room_inner_exit"
        )
        self.__storage.connect_nodes_by_identifiers(
            "ghosts_room_x2y1", "ghosts_room_inner_exit"
        )
        self.__storage.connect_nodes_by_identifiers(
            "ghosts_room_x1y1", "ghosts_room_x1y2"
        )
        self.__storage.connect_nodes_by_identifiers(
            "ghosts_room_x1y2", "ghosts_room_x2y2"
        )
        self.__storage.connect_nodes_by_identifiers(
            "ghosts_room_x2y1", "ghosts_room_x2y2"
        )

    def get_nodes(self):
        return self.__nodes.copy()
