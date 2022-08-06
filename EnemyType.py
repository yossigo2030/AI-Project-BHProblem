from DataStructures import EnemySpriteGroup
from MovementDir import MovePattern
from Spriteables import BulletHellSprite


class EnemyType(BulletHellSprite):

    def __init__(self, location, sprite, velocity: MovePattern, health=1):
        super().__init__(location, sprite, velocity)
        EnemySpriteGroup.add(self)
        self.health = health


class EnemyShooter(EnemyType):

    # shoot pattern is a list of diretions
    def __init__(self, location, sprite, velocity: MovePattern, projPatterns : MovePattern):
        super().__init__(location, sprite, velocity)
        self.projPatterns = projPatterns

    def behaivour(self):
        for pattern in self.projPatterns:
            Projectile(self.location, "resources\\ball.png",  pattern)