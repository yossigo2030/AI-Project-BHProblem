from DataStructures import PlayerSpriteGroup
import cooldown
from DataStructures import PlayerSpriteGroup, Directions
from MovementPatterns import PlayerMovementPattern, StraightPattern
from Projectile import Projectile
from Spriteables import BulletHellSprite, out_of_bounds, out_of_bounds_player


class Player(BulletHellSprite):
    def __init__(self, location, sprite, speed=10, shoot_cd=10):
        super().__init__(location, sprite, PlayerMovementPattern((1, 1)))
        PlayerSpriteGroup.add(self)
        self.cd = cooldown.cooldown(shoot_cd)
        self.speed = speed

    def get_location(self):
        return self.location

    def action(self, direction, shoot):  # TODO: change the direction implementation to return the dict, and pass that to PlayerMovementPattern via varargs, which will handle the bound checks. this function should probably be update instead of action.
        new_loc = self.location + direction * self.speed

        if not out_of_bounds_player(new_loc, (self.imsize[0] / 2, self.imsize[1] / 2)):
            self.location = new_loc
        self.cd.update()

        if shoot and self.cd.is_ready():
            self.cd.use()
            Projectile(self.location, "resources\\ball.png", StraightPattern(Directions.Up(10)))
            print("powpow")
