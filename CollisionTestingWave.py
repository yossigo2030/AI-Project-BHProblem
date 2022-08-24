import random
from typing import Tuple

import DataStructures
import EnemyType
import MovementPatterns


class CollisionTestingWave:
    """ Username checks out """

    def __init__(self, board_size: Tuple[int, int], data: DataStructures.DataStructures):
        self.board_size = board_size
        self.data = data


        c = 10
        for i in range(c):
            pos = [i * self.board_size[0] / c + 20, self.board_size[1] / 3]
            EnemyType.EnemyShooter(pos, r"resources\en.png", self.data,
                                   MovementPatterns.StraightPattern((0, 0)),
                                   [MovementPatterns.TargetPosPattern(2, self.data.PlayerSpriteGroup.sprites()[0].location)])

    def __copy__(self, data):
        return CollisionTestingWave(self.board_size, data)

    def update(self):
        pass
