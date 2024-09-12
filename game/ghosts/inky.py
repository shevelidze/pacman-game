import random
from ..ghost import Ghost


class Inky(Ghost):
    _color = (0, 254, 254)

    def _get_target_node(self):
        return random.choice(self._field.get_nodes_storage().get_nodes())
