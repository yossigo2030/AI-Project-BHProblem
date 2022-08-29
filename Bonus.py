from DataStructures import Directions, DataStructures
import MovementPatterns
from Spriteables import BulletHellSprite
import pygame


class Bonus(BulletHellSprite):
    def __init__(self, data, score, location):
        "resources\\BONUS.png"
        self.score = score
        self.data = data
        self.location = location
        super().__init__(self.location, r"resources\BONUS.png", self.data,
                         movement_pattern=MovementPatterns.StraightPattern((0, 1)))
        self.data.BonusGroup.add(self)

    def on_hit(self):
        self.kill()
        return self.score