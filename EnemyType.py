from typing import List
from DataStructures import DataStructures
from MovementPatterns import MovePattern
from Spriteables import BulletHellSprite
from Projectile import Projectile
from cooldown import cooldown


class EnemyType(BulletHellSprite):
    def __init__(self, location, sprite, data, movement_pattern: MovePattern, health=1):
        super().__init__(location, sprite, data, movement_pattern)
        self.data.EnemySpriteGroup.add(self)
        self.health = health


    def on_hit(self, dmg):
        self.health -= dmg
        return self.health > 0


class EnemyShooter(EnemyType):
    # shoot pattern is a list of directions
    def __init__(self, location, sprite, data, movement_pattern: MovePattern, projPatterns: [MovePattern]):
        super().__init__(location, sprite, data, movement_pattern)
        self.projPatterns = projPatterns
        self.cd = cooldown(90)


    def __copy__(self, data):
        return EnemyShooter(self.location, self.sprite, data, self.move_pattern, self.projPatterns)

    def update(self):
        super().update()
        self.cd.update()
        if self.cd.is_ready():
            self.cd.use()
            for pattern in self.projPatterns:
                Projectile(self.location, "resources\\ball.png", self.data, movement_pattern=pattern)


def update_all(data: DataStructures):
    for sprite in data.EnemySpriteGroup.sprites():
        sprite.update()


def draw_all(data: DataStructures):
    for sprite in data.EnemySpriteGroup.sprites():
        sprite.draw()

