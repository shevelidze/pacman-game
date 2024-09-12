from ..ghost import Ghost


class Blinky(Ghost):
    _color = (255, 29, 24)

    def _get_target_node(self):
        return self._pacman.get_previous_node()
