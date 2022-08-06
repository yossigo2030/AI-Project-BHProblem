from MovementDir import MovePattern
from Spriteables import BulletHellSprite


class EnemyType(BulletHellSprite):

    def __init__(self, location, sprite, velocity: MovePattern, health=1):
        super().__init__(location, sprite, velocity)
        self.health = health
