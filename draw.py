
WIDTH = 1000
LENGTH = 1000
screen = pygame.display.set_mode((WIDTH, LENGTH))

def screen_update():
    pass


def draw_sprite(sprite, location):
    screen.blit(sprite, location)
