import pygame

WIDTH = 1000
LENGTH = 1000
screen = pygame.display.set_mode((WIDTH, LENGTH))
BLACK = (0, 0, 0)

def screen_update():
    color = (255,255,255)
    pygame.draw.rect(screen, color, pygame.Rect(100, 100, 10, 10))

def redrawGameWindow():
    pygame.draw.rect(screen, BLACK, pygame.Rect(WIDTH, LENGTH, 0, 0))

def draw_sprite(sprite, location):
    screen.blit(sprite, location)
