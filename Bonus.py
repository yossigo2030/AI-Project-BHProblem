from DataStructures import Directions, DataStructures
import MovementPatterns
from Spriteables import BulletHellSprite
import pygame


class Bonus(BulletHellSprite):
    def __init__(self, data, score = 10, location = (0,0)):
        super().__init__(location, r"resources\BONUS.png", data,
                         movement_pattern=MovementPatterns.StraightPattern((0, 1)))
        self.score = score
        self.data.BonusGroup.add(self)

    def on_hit(self):
        self.kill()
        return self.score