import pygame
import DataStructures
import EnemyType
import Projectile
import MovementPatterns

def collision_check_enemies():
    score = 0
    for enemy in DataStructures.EnemySpriteGroup:
        for projectile in DataStructures.ProjectilePlayerGroup:
            if pygame.Rect.colliderect(enemy.get_hitbox(), projectile.get_hitbox()):
                # kill proj, hit enemy, delete enemy if dead and add score
                if not enemy.on_hit(1):
                    enemy.kill()
                    EnemyType.EnemyShooter([100, 100],
                                           r"resources\en.png",
                                           MovementPatterns.StraightPattern((0, 1)),
                                           [MovementPatterns.StraightPattern((-1, 0))])
                projectile.kill()
    return score

def collision_check_player():
    for player in DataStructures.PlayerSpriteGroup:
        for projectile in DataStructures.ProjectileEnemyGroup:
            if pygame.Rect.colliderect(player.get_hitbox(),
                                       projectile.get_hitbox()):
                # kill proj, hit player
                if not player.on_hit():
                    player.kill()
                projectile.kill()
