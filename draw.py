import pygame

WIDTH = 1000
LENGTH = 1000
screen = pygame.display.set_mode((WIDTH, LENGTH))
BLACK = (0, 0, 0)

def screen_update(loc):
    color = (255,255,255)
    pygame.draw.rect(screen, color, pygame.Rect(loc[0], loc[1], 10, 10))

def redrawGameWindow():
    pygame.draw.rect(screen, BLACK, pygame.Rect(0, 0, WIDTH, LENGTH))

def draw_sprite(sprite, location):
    screen.blit(sprite, location)
