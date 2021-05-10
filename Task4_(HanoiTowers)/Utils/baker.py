from json import dumps
from Utils import HanoiLogic
from DBORM.models import Iteration


def bake(initial_number: str) -> None:
    names = {index: name for index, name in zip(range(len(initial_number)), range(len(initial_number), 0, -1))}

    tower = HanoiLogic(initial_number)

    for percent, (iteration, scheme, disk, from_index, to_index) in enumerate(tower.get_iterations):
        Iteration.create(percent=percent,
                         number=iteration,
                         scheme=dumps(scheme),
                         disk_in_motion=disk,
                         from_index=from_index,
                         to_index=to_index,
                         from_name=names.get(from_index),
                         to_name=names.get(to_index))
