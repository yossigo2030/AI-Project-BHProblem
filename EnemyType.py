from typing import List
from DataStructures import DataStructures
from MovementPatterns import MovePattern
from Spriteables import BulletHellSprite
from Projectile import Projectile
from cooldown import cooldown
import copy


class EnemyType(BulletHellSprite):
    def __init__(self, location, sprite, data, movement_pattern: MovePattern, health=1):
        super().__init__(location, sprite, data, movement_pattern)
        self.health = health

    def on_hit(self, dmg):
        self.health -= dmg
        return self.health > 0


class EnemyShooter(EnemyType):
    # shoot pattern is a list of directions
    def __init__(self, location, sprite, data, movement_pattern: MovePattern, projPatterns: [MovePattern], cd: int or cooldown = 90):
        super().__init__(location, sprite, data, movement_pattern)
        self.projPatterns = projPatterns
        self.cd = cooldown(cd) if isinstance(cd, int) else cooldown
        self.data.EnemySpriteGroup.add(self)

    def __copy__(self, data):
        return EnemyShooter(self.location, self.image, data, self.move_pattern.__copy__(), self.projPatterns, cooldown(self.cd.time, self.cd.counter))  # self.cd.counter

    def update(self):
        super().update()
        self.cd.update()
        if self.cd.is_ready():
            self.cd.use()
            for pattern in self.projPatterns:
                Projectile(self.location, "resources\\ball.png", self.data, movement_pattern=pattern)


class BossShooter(EnemyType):
    # shoot pattern is a list of directions
    def __init__(self, location, sprite, data, movement_pattern: MovePattern, projPatterns: [MovePattern], cooldown=cooldown(90)):
        super().__init__(location, sprite, data, movement_pattern)
        self.projPatterns = projPatterns
        self.cd = cooldown
        self.data.EnemyBossSpriteGroup.add(self)

    def __copy__(self, data):
        return EnemyShooter(self.location, self.image, data, self.move_pattern.__copy__(), self.projPatterns, cooldown(self.cd.time, self.cd.counter))  # self.cd.counter

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
    for sprite in data.EnemyBossSpriteGroup.sprites():
        sprite.update()


def draw_all(data: DataStructures):
    for sprite in data.EnemySpriteGroup.sprites():
        sprite.draw()
    for sprite in data.EnemyBossSpriteGroup.sprites():
        sprite.update()
