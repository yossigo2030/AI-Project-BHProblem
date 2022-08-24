import pygame

WIDTH = 500
LENGTH = 500
screen = pygame.display.set_mode((WIDTH, LENGTH))
BLACK = (0, 0, 0)


def screen_update(loc):
    color = (255, 255, 255)
    pygame.draw.rect(screen, color, pygame.Rect(loc[0], loc[1], 10, 10))


def draw_blank_square_at_loc(loc):
    color = (255, 255, 255)
    pygame.draw.rect(screen, color, pygame.Rect(loc[0], loc[1], 10, 10))


def redrawGameWindow():
    pygame.draw.rect(screen, BLACK, pygame.Rect(0, 0, WIDTH, LENGTH))


def draw_sprite(sprite: pygame.Surface, location):
    size = sprite.get_size()
    screen.blit(sprite, (location[0] - size[0] / 2, location[1] - size[1] / 2))
