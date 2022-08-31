from MovementPatterns import *
from DataStructures import DataStructures
from Spriteables import BulletHellSprite


class Bonus(BulletHellSprite):
    def __init__(self, data, score=10, location=(0, 0)):
        super().__init__(location, r"resources\BONUS.png", data, movement_pattern=StraightPattern((0, 1)))
        self.score = score
        self.data.BonusGroup.add(self)

    def on_hit(self):
        self.kill()
        return self.score

    def __copy__(self, data):
        return Bonus(data, self.score, self.location)


def update_all(data: DataStructures):
    for sprite in data.BonusGroup.sprites():
        sprite.update()
