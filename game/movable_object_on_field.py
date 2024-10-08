import random
from .object_on_field import ObjectOnField
from .node import Node


class MovableObjectOnField(ObjectOnField):
    def __init__(
        self,
        field,
        previous_node,
        next_node=None,
        distance_from_previous_node=None,
    ):
        super().__init__(field, previous_node, next_node, distance_from_previous_node)

    def tick(self, events):
        if self._has_reached_node():
            self._on_reached_node()

    def _has_reached_node(self):
        return self._next_node is None or (
            self._get_traveled_ratio(additional_distance=self.__get_passed_distance())
            >= 1
        )

    def _get_position(self, additional_distance=None):
        final_additional_distance = self.__get_passed_distance()

        if additional_distance is not None:
            final_additional_distance += additional_distance

        return super()._get_position(additional_distance=final_additional_distance)

    def get_position(self):
        return self._get_position()

    def _is_moving(self):
        return self.__started_moving_at is not None

    def _on_reached_node(self):
        pass

    def _stop_moving(self):
        self._distance_from_previous_node = (
            self._distance_from_previous_node + self.__get_passed_distance()
        )
        self.__started_moving_at = None

    def _start_moving(self):
        self.__started_moving_at = self._get_game_time()

    def _set_next_node(self, next_node: Node):
        if not self._next_node is None:
            self._previous_node = self._next_node

        self._next_node = next_node
        self._distance_from_previous_node = 0
        self.__started_moving_at = None

    def _get_direction(self):
        return (
            self._previous_node.get_node_direction(self._next_node)
            if self._next_node
            else None
        )

    def __get_passed_distance(self):
        if self.__started_moving_at is None:
            return 0

        time_passed = self._get_game_time() - self.__started_moving_at
        return time_passed * self._get_speed()

    def _turn_around(self):
        self._distance_from_previous_node = (
            self._get_distance_between_nodes()
            - self._distance_from_previous_node
            - self.__get_passed_distance()
        )

        if self._distance_from_previous_node < 0:
            self._distance_from_previous_node = 0

        self._next_node, self._previous_node = self._previous_node, self._next_node

        if self._is_moving():
            self._start_moving()

    def _get_speed(self) -> float:
        raise NotImplementedError

    __started_moving_at = None
