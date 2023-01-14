from message.models import CompletedTasks
from model_bakery import baker


def make_completed_tasks(number: int) -> list[CompletedTasks] | CompletedTasks:
    completed_tasks = baker.make(
        'message.CompletedTasks',
        _quantity=number,
    )
    if number == 1:
        return completed_tasks[0]
    return completed_tasks
