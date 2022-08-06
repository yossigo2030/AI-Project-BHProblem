import keybinds
from DataStructures import PlayerSpriteGroup
import cooldown
from DataStructures import PlayerSpriteGroup, Directions
from MovementPatterns import PlayerMovementPattern, StraightPattern
from Projectile import Projectile
from Spriteables import BulletHellSprite, out_of_bounds, out_of_bounds_player


class Player(BulletHellSprite):
    def __init__(self, location, sprite, speed=10, shoot_cd=10, hitbox_size=(25, 25), image_size=(40, 40)):
        super().__init__(location, sprite, PlayerMovementPattern(speed, image_size), hitbox_size, image_size)
        PlayerSpriteGroup.add(self)
        self.cd = cooldown.cooldown(shoot_cd)
        self.speed = speed

    def get_location(self):
        return self.location

    def update(self):  # TODO: change the direction implementation to return the dict, and pass that to PlayerMovementPattern via varargs, which will handle the bound checks. this function should probably be update instead of action.
        super().update()
        _, shoot = keybinds.get_input()
        self.cd.update()
        if shoot and self.cd.is_ready():
            self.cd.use()
            Projectile(self.location, "resources\\ball.png", StraightPattern(Directions.Up(10)), playerProjectile= True)
