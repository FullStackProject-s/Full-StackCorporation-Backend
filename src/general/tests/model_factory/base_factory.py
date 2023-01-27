from typing import Callable

from model_bakery import baker


def create_model_factory(path_model: str) -> Callable[[int], list | object]:
    def make_object_func(number: int) -> list[object] | object:
        objects = baker.make(
            path_model,
            _quantity=number,
        )
        if number == 1:
            return objects[0]
        return objects

    return make_object_func
