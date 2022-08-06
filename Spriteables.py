import pygame.sprite
import Draw
from DataStructures import AllSpritesGroup
from MovementPatterns import *


class BulletHellSprite(pygame.sprite.Sprite):
    def __init__(self, location, sprite, movement_pattern: MovePattern = StraightPattern((0, 10)), hitbox_size=(25, 25), image_size=(40, 40)):
        super().__init__()
        AllSpritesGroup.add(self)
        self.location = location
        self.image = pygame.transform.scale(pygame.image.load(sprite).convert_alpha(), image_size)
        self.imsize = image_size
        self.hitbox = hitbox_size
        self.move_pattern = movement_pattern

    def update(self):
        self.location = self.move_pattern.get_next_position(self.location)

    def draw(self):
        Draw.draw_sprite(self.image, self.location)


def out_of_bounds(location, sprite_size):
    return location[0] < 0 or location[0] > Draw.WIDTH - sprite_size[0] or location[1] < 0 or location[1] > Draw.LENGTH - sprite_size[1]


def sprite_culling():
    for sprite in AllSpritesGroup.sprites():
        if out_of_bounds(sprite.location, sprite.imsize):
            sprite.kill()
