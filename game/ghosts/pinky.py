from ..ghost import Ghost
from ..utils import move_in_direction


class Pinky(Ghost):
    _color = (255, 184, 253)

    def _get_target_node(self):
        pacman_position = self._pacman._get_position()
        pacman_direction = self._pacman._get_direction()

        return (
            self._field.get_nodes_storage().get_closest_node_to_position(
                move_in_direction(pacman_position, pacman_direction, 50),
            )
            if not pacman_direction is None
            else self._pacman.get_previous_node()
        )

    def _can_exit_room(self):
        return True
