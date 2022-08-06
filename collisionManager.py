import pygame
import DataStructures
import EnemyType
import Projectile

def collision_check_enemies():
    score = 0
    for enemy in DataStructures.EnemySpriteGroup():
        for projectile in DataStructures.ProjectilePlayerGroup():
            if pygame.Rect.colliderect(enemy.get_hitbox(), projectile.get_hitbox()):
                # kill proj, hit enemy, delete enemy if dead and add score
                pass
    return score