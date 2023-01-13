from message.models import Reassignment
from model_bakery import baker


def make_reassignment(number: int) -> list[Reassignment] | Reassignment:
    reassignments = baker.make(
        'message.Reassignment',
        _quantity=number,
    )
    if number == 1:
        return reassignments[0]
    return reassignments
