from message.models import Task
from model_bakery import baker


def make_task(number: int) -> list[Task] | Task:
    tasks = baker.make(
        'message.Task',
        _quantity=number,
    )
    if number == 1:
        return tasks[0]
    return tasks
