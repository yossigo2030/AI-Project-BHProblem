import pygame
import DataStructures
import EnemyType
import Projectile

def collision_check_enemies():
    score = 0
    for enemy in DataStructures.EnemySpriteGroup:
        for projectile in DataStructures.ProjectilePlayerGroup:
            if pygame.Rect.colliderect(enemy.get_hitbox(), projectile.get_hitbox()):
                # kill proj, hit enemy, delete enemy if dead and add score
                if(enemy.hit(1)):
                    enemy.kill()
                projectile.kill()
    return score

def collision_check_player():
    for player in DataStructures.PlayerSpriteGroup:
        for projectile in DataStructures.ProjectileEnemyGroup:
            if pygame.Rect.colliderect(player.get_hitbox(),
                                       projectile.get_hitbox()):
                # kill proj, hit player
                if(player.hit(1)):
                    player.kill()
                projectile.kill()
