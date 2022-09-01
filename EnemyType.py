from Cooldown import Cooldown
from DataStructures import DataStructures
from MovementPatterns import MovePattern
from Projectile import Projectile
from Spriteables import BulletHellSprite


class EnemyType(BulletHellSprite):
    def __init__(self, location, sprite, data, movement_pattern: MovePattern, health=1, hitbox_size=(25, 25), image_size=(40, 40)):
        super().__init__(location, sprite, data, movement_pattern, hitbox_size=(25, 25), image_size=image_size)
        self.health = health

    def on_hit(self, dmg):
        self.health -= dmg
        return self.health > 0


class EnemyShooter(EnemyType):
    # shoot pattern is a list of directions
    def __init__(self, location, sprite, data, movement_pattern: MovePattern, proj_patterns: [MovePattern], cd: Cooldown or int = 90, hitbox_size=(25, 25), image_size=(40, 40)):
        super().__init__(location, sprite, data, movement_pattern, hitbox_size=(25, 25), image_size=image_size)
        self.projPatterns = proj_patterns
        self.cd = Cooldown(cd) if isinstance(cd, int) else cd
        self.data.EnemySpriteGroup.add(self)

    def __copy__(self, data):
        return EnemyShooter(self.location, self.image, data, self.move_pattern.__copy__(), self.projPatterns, self.cd.__copy__())  # self.cd.counter

    def update(self):
        super().update()
        self.cd.update()
        if self.cd.is_ready():
            self.cd.use()
            for pattern in self.projPatterns:
                Projectile(self.location, "resources\\en_ball.png", self.data, movement_pattern=pattern, hitbox_size=(15, 15), image_size=(20, 20))


class BossShooter(EnemyType):
    # shoot pattern is a list of directions
    def __init__(self, location, sprite, data, movement_pattern: MovePattern, projPatterns: [MovePattern], cooldown=Cooldown(90)):
        super().__init__(location, sprite, data, movement_pattern)
        self.projPatterns = projPatterns
        self.cd = cooldown
        self.data.EnemyBossSpriteGroup.add(self)

    def __copy__(self, data):
        return EnemyShooter(self.location, self.image, data, self.move_pattern.__copy__(), self.projPatterns, Cooldown(self.cd.time, self.cd.counter))  # self.cd.counter

    def update(self):
        super().update()
        self.cd.update()
        if self.cd.is_ready():
            self.cd.use()
            for pattern in self.projPatterns:
                Projectile(self.location, "resources\\en_ball.png", self.data, movement_pattern=pattern)


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
