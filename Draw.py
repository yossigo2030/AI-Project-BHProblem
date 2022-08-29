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

def write_score_and_hp(score, hp):
    write_text(f"score: %d" % score, (WIDTH*0.5, 20))
    write_text(f"lives: %d" % hp, (WIDTH*0.5, 50))


def write_text(substance, location):
    font = pygame.font.Font('freesansbold.ttf', WIDTH// 30)
    text = font.render(substance, True, (255,255,255))
    textRect = text.get_rect()
    screen.blit(text, (location[0] -textRect.width // 2 , location[1]))

def redrawGameWindow():
    pygame.draw.rect(screen, BLACK, pygame.Rect(0, 0, WIDTH, LENGTH))


def draw_sprite(sprite: pygame.Surface, location):
    size = sprite.get_size()
    screen.blit(sprite, (location[0] - size[0] / 2, location[1] - size[1] / 2))
