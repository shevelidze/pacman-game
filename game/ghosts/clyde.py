from ..ghost import Ghost
from ..utils import get_distance


class Clyde(Ghost):
    _color = (255, 186, 91)

    def _get_target_node(self):
        pacman_position = self._pacman._get_position()
        pacman_direction = self._pacman._get_direction()

        if get_distance(self._get_position(), self._pacman._get_position()) < 50:
            return self._field.get_nodes_storage().get_node_by_identifier("x5y9")

        return self._pacman.get_previous_node()
