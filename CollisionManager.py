import pygame
import DataStructures
import EnemyType
import Projectile
import MovementPatterns


def collision_check_enemies(data: DataStructures):
    score = 0
    for projectile in data.ProjectilePlayerGroup:
        for enemy in data.EnemySpriteGroup:
            if pygame.Rect.colliderect(enemy.get_hitbox(), projectile.get_hitbox()):
                # kill proj, hit enemy, delete enemy if dead and add score
                if not enemy.on_hit(1):
                    enemy.kill()
                    score = 20
                projectile.kill()
        if score > 0:
            for boss in data.EnemyBossSpriteGroup:
                if pygame.Rect.colliderect(boss.get_hitbox(), projectile.get_hitbox()):
                    # kill proj, hit enemy, delete enemy if dead and add score
                    if not boss.on_hit(1):
                        boss.kill()
                        score = 200
                    projectile.kill()
    return score


def collision_check_player(data: DataStructures):
    for player in data.PlayerSpriteGroup:
        for group in [data.ProjectileEnemyGroup, data.EnemySpriteGroup]:
            for target in group:
                if pygame.Rect.colliderect(player.get_hitbox(),
                                           target.get_hitbox()):
                    # kill proj, hit player
                    if not player.on_hit():
                        player.kill()
                    target.kill()
        for boss in data.EnemyBossSpriteGroup:
            if pygame.Rect.colliderect(player.get_hitbox(),
                                       boss.get_hitbox()):
                if not player.on_hit():
                    player.kill()
