import random
from ..ghost import Ghost


class Inky(Ghost):
    _color = (0, 254, 254)

    def _get_target_node(self):
        return random.choice(self._field.get_nodes_storage().get_nodes())

    def _can_exit_room(self):
        return self._get_eaten_dots_count() > 30
