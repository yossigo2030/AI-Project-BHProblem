import pygame
import DataStructures
import EnemyType
import Projectile

def collision_check_enemies():
    score = 0
    for enemy in DataStructures.EnemySpriteGroup():
        for projectile in DataStructures.ProjectilePlayerGroup():
            if pygame.Rect.colliderect(enemy.hitbox, projectile.hitbox):
                # kill proj, hit enemy, delete enemy if dead and add score
                print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                pass
    return score