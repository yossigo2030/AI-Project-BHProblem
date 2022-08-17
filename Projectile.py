import pygame.sprite

from DataStructures import Directions, DataStructures
from MovementPatterns import StraightPattern, MovePattern
from Spriteables import BulletHellSprite


class Projectile(BulletHellSprite):
    def __init__(self, location, sprite, data, damage_value=1, movement_pattern: MovePattern = StraightPattern(Directions.Up(10)), player_projectile=False):
        super().__init__(location, sprite, data, movement_pattern=movement_pattern)
        self.data.ProjectileSpriteGroup.add(self)
        if player_projectile:
            self.data.ProjectilePlayerGroup.add(self)
        else:
            self.data.ProjectileEnemyGroup.add(self)

        self.damage_value = damage_value

    def on_hit(self):
        self.kill()
        return self.damage_value


def update_all(data: DataStructures):
    for sprite in data.ProjectileSpriteGroup.sprites():
        sprite.update()


def draw_all(data: DataStructures):
    for sprite in data.ProjectileSpriteGroup.sprites():
        sprite.draw()
