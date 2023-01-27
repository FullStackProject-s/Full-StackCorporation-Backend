from typing import Callable

from model_bakery import baker


def create_model_factory(
        path_model: str,
        **kwargs
) -> Callable[[int], list | object]:
    def make_object_func(number: int) -> list[object] | object:
        nonlocal kwargs
        objects = baker.make(
            path_model,
            _quantity=number,
            **kwargs
        )
        if number == 1:
            return objects[0]
        return objects

    return make_object_func
