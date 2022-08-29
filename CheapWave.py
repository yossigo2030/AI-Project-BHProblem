import random
from copy import copy
from typing import Tuple

import DataStructures
import EnemyType
import MovementPatterns
from cooldown import Cooldown


class CheapWave:
    def __init__(self, board_size: Tuple[int, int], data: DataStructures.DataStructures, eps=0.05):
        self.board_size = board_size
        self.data = data
        self.eps = eps
        self.random = random.Random(138561857482)

    def __copy__(self, data):
        obj = CheapWave(self.board_size, data, self.eps)
        obj.random = copy(self.random)
        return obj

    def update(self):
        if self.random.uniform(0, 1) < self.eps:
            pos = [self.random.uniform(0, self.board_size[0]), -10]
            EnemyType.EnemyShooter(pos, r"resources\en.png", self.data,
                                   MovementPatterns.StraightPattern((0, 1)),
                                   [MovementPatterns.TargetPosPattern(2, self.data.PlayerSpriteGroup.sprites()[0].location)])
                                   # [MovementPatterns.StraightPattern((0, 2))])

