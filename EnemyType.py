from DataStructures import EnemySpriteGroup
from MovementPatterns import MovePattern
from Spriteables import BulletHellSprite
from Projectile import Projectile
from cooldown import cooldown

class EnemyType(BulletHellSprite):
    def __init__(self, location, sprite, movement_pattern: MovePattern, health=1):
        super().__init__(location, sprite, movement_pattern)
        EnemySpriteGroup.add(self)
        self.health = health

class EnemyShooter(EnemyType):
    # shoot pattern is a list of diretions
    def __init__(self, location, sprite, movement_pattern: MovePattern, projPatterns : [MovePattern]):
        super().__init__(location, sprite, movement_pattern)
        self.projPatterns = projPatterns
        self.cd = cooldown(10)

    def update(self):
        super().update()
        self.cd.update()
        if self.cd.is_ready():
            self.cd.use()
            for pattern in self.projPatterns:
                Projectile(self.location, "resources\\ball.png",  pattern)
