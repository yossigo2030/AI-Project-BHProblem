import pygame.sprite

from DataStructures import ProjectileSpriteGroup, Directions, ProjectileEnemyGroup, ProjectilePlayerGroup
from MovementPatterns import StraightPattern, MovePattern
from Spriteables import BulletHellSprite


class Projectile(BulletHellSprite):
    def __init__(self, location, sprite, damage_value=1, movement_pattern: MovePattern = StraightPattern(Directions.Up(10)), player_projectile=False):
        super().__init__(location, sprite, movement_pattern=movement_pattern)
        ProjectileSpriteGroup.add(self)
        if player_projectile:
            ProjectilePlayerGroup.add(self)
        else:
            ProjectileEnemyGroup.add(self)

        self.damage_value = damage_value

    def on_hit(self):
        self.kill()
        return self.damage_value


def update_all():
    for sprite in ProjectileSpriteGroup.sprites():
        sprite.update()


def draw_all():
    for sprite in ProjectileSpriteGroup.sprites():
        sprite.draw()
