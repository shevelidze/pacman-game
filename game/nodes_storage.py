from .utils import get_distance


class NodesStorage:
    def __init__(self, nodes):
        self.__nodes = nodes
        self.__nodes_by_identifier = dict(
            (node.get_identifier(), node) for node in nodes
        )

    def get_closest_node_to_position(self, position):
        return min(
            self.__nodes, key=lambda node: get_distance(node.get_position(), position)
        )

    def get_nodes(self):
        return self.__nodes

    def get_node_by_identifier(self, identifier):
        return self.__nodes_by_identifier[identifier]

    def connect_nodes_by_identifiers(self, identifier1, identifier2):
        node1 = self.get_node_by_identifier(identifier1)
        node2 = self.get_node_by_identifier(identifier2)

        node1.connect(node2)
